"""
Client a l'API de Google Gemini per al Tutor Cangur 1r ESO.

Visió general per a un lector nou
=================================
Aquest mòdul aïlla tota la dependència amb Google Gemini. La resta del
codi mai crida la SDK directament; sempre passa per aquestes 2 funcions
d'alt nivell:

1. `discuss(problem, image_path, conversation, student_text)` — torn de
   DIÀLEG socràtic. L'alumne pot expressar qualsevol acte de parla:
   compartir una hipòtesi ("crec que és la C"), justificar una eliminació
   ("D no pot ser perquè..."), demanar aclariment post-error ("per què
   C no era correcte?"), o preguntar a porta tancada ("per on començo?").
   La IA respon en català, en prosa lliure, mantenint posició socràtica
   (mai revela la lletra correcta). Retorna el text de la resposta.

2. `generate_hint(problem, image_path, conversation)` — pista on-demand.
   Es crida NOMÉS quan ja s'ha consumit la pista inicial del catàleg (si
   en tenia). La IA veu totes les pistes prèvies al multi-torn (cada
   pista anterior viu com a un torn assistant a la conversation) i
   gradua la duresa automàticament. Retorna text pla, 1-2 frases.

Diferències respecte a versions anteriors del tutor
---------------------------------------------------
- S'ha esborrat `judge_reasoning`. El model "classificador amb veredictes"
  (correct_path/partial/dead_end/off_track) deixa de tenir sentit en un
  model conversacional: l'alumne no proposa una solució per ser jutjada,
  sinó que dialoga.
- S'ha esborrat `_has_math_content`: vam decidir treure el filtre
  determinista d'ús inadequat (decisió de l'usuari). La IA ja gestiona
  un "hola" amb amabilitat redirigint al problema.
- Multimodal: cada crida envia la imatge del problema (jpg) a la SDK
  com a part del primer Content. La imatge només es transmet una vegada
  per crida; Gemini la manté en context al seu costat.
- Multi-torn: la conversation_history es passa íntegra (amb truncament
  defensiu si supera ~20 torns). Així la IA recorda què s'ha dit abans
  sense que l'engine hagi de mantenir cap "estat estructurat" addicional.
- No hi ha sortida JSON estructurada. Tant `discuss` com `generate_hint`
  retornen text pla. El "suggests_commit" l'expressa la IA dins el seu
  text en català (decisió de l'usuari), no com a metadata.

Robustesa
---------
- Retry amb exponential backoff (3 intents, base 1.5s → 3s → 6s) per a
  errors transitoris: 503/UNAVAILABLE, 429/RATE_LIMIT, 500/INTERNAL,
  DEADLINE_EXCEEDED i timeouts.
- Tota crida queda gravada al log (`api_logger.py`) amb tokens, cost USD
  estimat, durada i `student_id`/`session_id` del context actual.

Variables d'entorn:
- GEMINI_API_KEY (obligatori)
- GEMINI_MODEL (opcional, default `gemini-2.5-flash`)
"""

import os
import re
import time
import threading
import uuid
from pathlib import Path

import api_logger

# La importació de la SDK es fa try/except perquè volem que `import llm`
# funcioni encara que no estigui instal·lada (útil per a tests amb mocks).
try:
    from google import genai
    from google.genai import types as _genai_types
except ImportError:
    genai = None
    _genai_types = None

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
MAX_TOKENS = 400

# Detectem el thinking model per nom (el SDK no exposa una propietat
# `is_thinking`).
IS_THINKING_MODEL = "pro" in MODEL.lower()
TOKEN_MULTIPLIER = 10 if IS_THINKING_MODEL else 1

# ============================================================
# Configuració dinàmica del proveïdor (per al mode debug)
# ============================================================
# PROVIDER pot ser "gemini" o "claude".
PROVIDER = "gemini"

# Client Claude (lazy, anàleg a _client per a Gemini)
_claude_client = None

try:
    import anthropic as _anthropic_sdk
except ImportError:
    _anthropic_sdk = None


def set_debug_config(provider: str, model: str,
                     gemini_key: str | None = None,
                     claude_key: str | None = None):
    """
    Canvia dinàmicament el proveïdor i el model. Crida NOMÉS des del
    mode debug de l'UI. Invalida els clients lazy perquè la propera
    crida els torni a crear amb la nova configuració.

    Paràmetres:
    - provider:   "gemini" o "claude"
    - model:      string del model (e.g. "gemini-2.5-pro", "claude-sonnet-4-5")
    - gemini_key: si no és None, sobreescriu GEMINI_API_KEY a l'entorn
    - claude_key: si no és None, sobreescriu ANTHROPIC_API_KEY a l'entorn
    """
    global PROVIDER, MODEL, IS_THINKING_MODEL, TOKEN_MULTIPLIER
    global _client, _claude_client

    PROVIDER = provider.lower().strip()
    MODEL = model.strip()

    # Recalcular els derivats (el model pro de Gemini té thinking tokens)
    IS_THINKING_MODEL = ("pro" in MODEL.lower() and PROVIDER == "gemini")
    TOKEN_MULTIPLIER = 10 if IS_THINKING_MODEL else 1

    # Invalidar clients perquè es tornin a crear amb la nova config
    _client = None
    _claude_client = None

    # Sobreescriure keys a l'entorn si se n'han passat
    if gemini_key:
        os.environ["GEMINI_API_KEY"] = gemini_key
    if claude_key:
        os.environ["ANTHROPIC_API_KEY"] = claude_key


# Retry config per a errors transitoris de l'API.
MAX_ATTEMPTS = 3
BACKOFF_BASE_S = 1.5

RETRIABLE_PATTERNS = (
    "503", "UNAVAILABLE",
    "429", "RATE_LIMIT", "RESOURCE_EXHAUSTED",
    "500", "INTERNAL",
    "DEADLINE_EXCEEDED",
    "timeout", "Timeout",
)


# ============================================================
# Truncament defensiu de la conversa
# ============================================================
# Decisió arquitectònica de l'usuari: si la conversa supera ~20 torns,
# mantenim els 3 primers + els 10 últims. Els 3 primers contenen el
# context inicial (sovint la primera lectura de l'alumne); els 10 últims
# contenen on s'està ara la conversa.
TRUNCATE_THRESHOLD = 20
TRUNCATE_KEEP_FIRST = 3
TRUNCATE_KEEP_LAST = 10


def truncate_conversation(conversation: list) -> list:
    """
    Aplica el truncament defensiu sobre una llista de torns. Si està per
    sota del llindar, retorna una còpia íntegra. Si està per sobre,
    retorna els N primers + els M últims.
    """
    if len(conversation) <= TRUNCATE_THRESHOLD:
        return list(conversation)
    return list(conversation[:TRUNCATE_KEEP_FIRST]) + list(conversation[-TRUNCATE_KEEP_LAST:])


# ============================================================
# Context de logging (thread-local)
# ============================================================
_PROCESS_FALLBACK_SESSION = uuid.uuid4().hex[:8]
_log_ctx = threading.local()


def set_log_context(student_id: str, session_id: str):
    """Fixa el context de logging per al thread actual."""
    _log_ctx.student_id = student_id
    _log_ctx.session_id = session_id


def _current_session_id() -> str:
    return getattr(_log_ctx, "session_id", None) or _PROCESS_FALLBACK_SESSION


def _current_student_id() -> str:
    return getattr(_log_ctx, "student_id", None) or "anon"


def get_log_context() -> tuple:
    return (
        getattr(_log_ctx, "student_id", None),
        getattr(_log_ctx, "session_id", None),
    )


def get_session_id() -> str:
    return _current_session_id()


_progress_callback = None


def set_progress_callback(callback):
    global _progress_callback
    _progress_callback = callback


def _notify(msg: str):
    if _progress_callback is not None:
        try:
            _progress_callback(msg)
        except Exception:
            pass


def _is_retriable(err: Exception) -> bool:
    s = str(err)
    return any(p in s for p in RETRIABLE_PATTERNS)


# ============================================================
# Client Gemini (lazy)
# ============================================================
_client = None


def _get_client():
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    return _client


def _get_claude_client():
    global _claude_client
    if _anthropic_sdk is None:
        raise RuntimeError(
            "La llibreria 'anthropic' no està instal·lada. "
            "Afegeix-la a requirements.txt i torna a arrencar."
        )
    if _claude_client is None:
        _claude_client = _anthropic_sdk.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )
    return _claude_client


# ============================================================
# Cache d'imatges
# ============================================================
# Una sessió pot tenir 10+ torns sobre el mateix problema. Llegir el
# JPG de disc cada cop és un I/O innecessari. Cachejem per path absolut.
_image_cache: dict = {}


def _load_image_bytes(image_path: str) -> bytes:
    """Llegeix el JPG (i el cachegem). Llança FileNotFoundError si no existeix."""
    abs_path = str(Path(image_path).resolve())
    if abs_path in _image_cache:
        return _image_cache[abs_path]
    with open(abs_path, "rb") as f:
        data = f.read()
    _image_cache[abs_path] = data
    return data


def _detect_mime(image_path: str) -> str:
    """Detecció mínima del MIME type pel sufix."""
    ext = Path(image_path).suffix.lower()
    if ext in (".jpg", ".jpeg"):
        return "image/jpeg"
    if ext == ".png":
        return "image/png"
    if ext == ".webp":
        return "image/webp"
    return "image/jpeg"


# ============================================================
# Construcció dels `contents` multi-torn per a Gemini
# ============================================================
def _build_contents(image_path, conversation: list, new_user_text):
    """
    Construeix la llista `contents` que rep la SDK de Gemini.

    Inclou:
    - Imatge del problema al PRIMER Content de tipus user (només una vegada).
      Si no es troba al disc, continuem sense imatge (fallback elegant).
    - Els torns previs de la conversa, traduïts a Content amb el seu role.
      Els kinds especials es prefixen amb marcadors textuals:
        * kind="message"        → text tal qual
        * kind="hint"           → prefixat amb "[PISTA] "
        * kind="system_event"   → prefixat amb "[Sistema] "
    - El missatge nou de l'alumne (`new_user_text`), si se'n passa un.

    Detalls de la SDK
    -----------------
    - role del torn assistant: "model" (Gemini), no "assistant".
    - Imatge: Part.from_bytes amb mime_type.
    """
    types = _genai_types
    contents = []

    image_bytes = None
    image_mime = None
    if image_path:
        try:
            image_bytes = _load_image_bytes(image_path)
            image_mime = _detect_mime(image_path)
        except FileNotFoundError:
            _notify(f"Imatge no trobada: {image_path}. Procedim sense imatge.")

    image_consumed = False
    for turn in conversation:
        role = turn.get("role", "user")
        gemini_role = "model" if role == "assistant" else "user"
        kind = turn.get("kind", "message")
        content = turn.get("content", "")

        if kind == "hint":
            content_text = f"[PISTA] {content}"
        elif kind == "system_event":
            content_text = f"[Sistema] {content}"
        else:
            content_text = content

        # Si el torn és de la IA i porta un marcador de mode desat,
        # el restaurem al final del text. Sense això, la IA mira els
        # seus missatges anteriors a la història, no hi veu cap
        # marcador (perquè `_extract_mode` el filtra abans de desar
        # `content`), i deixa de posar-lo a partir del torn 2 — la
        # IA imita el patró que veu al seu propi historial. Així
        # mantenim la classificació consistent torn a torn.
        if (gemini_role == "model"
                and kind == "message"
                and turn.get("mode") in ("S", "D")):
            content_text = f"{content_text}\n[MODE:{turn['mode']}]"

        parts = []
        if (image_bytes is not None and not image_consumed
                and gemini_role == "user"):
            parts.append(types.Part.from_bytes(
                data=image_bytes, mime_type=image_mime,
            ))
            image_consumed = True
        parts.append(types.Part.from_text(text=content_text))
        contents.append(types.Content(role=gemini_role, parts=parts))

    if new_user_text is not None:
        parts = []
        if image_bytes is not None and not image_consumed:
            parts.append(types.Part.from_bytes(
                data=image_bytes, mime_type=image_mime,
            ))
            image_consumed = True
        parts.append(types.Part.from_text(text=new_user_text))
        contents.append(types.Content(role="user", parts=parts))

    return contents


# ============================================================
# Construcció dels missatges per a Claude (Anthropic)
# ============================================================
def _build_claude_messages(image_path, conversation: list,
                            new_user_text) -> list:
    """
    Construeix la llista `messages` per a l'API d'Anthropic.
    Format: [{"role": "user"|"assistant", "content": [...parts]}]

    La imatge (si existeix) va al primer torn user, igual que a Gemini.
    """
    import base64

    image_b64 = None
    image_mime = None
    if image_path:
        try:
            raw = _load_image_bytes(image_path)
            image_b64 = base64.standard_b64encode(raw).decode()
            image_mime = _detect_mime(image_path)
        except FileNotFoundError:
            _notify(f"Imatge no trobada: {image_path}. Procedim sense imatge.")

    messages = []
    image_consumed = False

    for turn in conversation:
        role = turn.get("role", "user")
        # Anthropic usa "user" i "assistant" directament (no "model")
        claude_role = "assistant" if role == "assistant" else "user"
        kind = turn.get("kind", "message")
        content = turn.get("content", "")

        if kind == "hint":
            content_text = f"[PISTA] {content}"
        elif kind == "system_event":
            content_text = f"[Sistema] {content}"
        else:
            content_text = content

        if (claude_role == "assistant"
                and kind == "message"
                and turn.get("mode") in ("S", "D")):
            content_text = f"{content_text}\n[MODE:{turn['mode']}]"

        parts = []
        if image_b64 and not image_consumed and claude_role == "user":
            parts.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": image_mime,
                    "data": image_b64,
                },
            })
            image_consumed = True
        parts.append({"type": "text", "text": content_text})
        messages.append({"role": claude_role, "content": parts})

    if new_user_text is not None:
        parts = []
        if image_b64 and not image_consumed:
            parts.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": image_mime,
                    "data": image_b64,
                },
            })
            image_consumed = True
        parts.append({"type": "text", "text": new_user_text})
        messages.append({"role": "user", "content": parts})

    return messages


def _do_call_claude(system: str, messages: list,
                    max_tokens: int, temperature: float):
    """Crida a l'API d'Anthropic i retorna (text, tokens_dict)."""
    client = _get_claude_client()
    response = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=messages,
        temperature=temperature,
    )
    text = ""
    for block in response.content:
        if hasattr(block, "text"):
            text += block.text
    if not text.strip():
        raise RuntimeError(
            f"Resposta buida del model Claude {MODEL} "
            f"(stop_reason={response.stop_reason})."
        )
    usage = response.usage
    tokens = {
        "input":    usage.input_tokens,
        "output":   usage.output_tokens,
        "thoughts": 0,
        "total":    usage.input_tokens + usage.output_tokens,
    }
    return text, tokens


def _build_messages(image_path, conversation: list, new_user_text):
    """Delega a la funció de construcció correcta segons PROVIDER."""
    if PROVIDER == "claude":
        return _build_claude_messages(image_path, conversation, new_user_text)
    return _build_contents(image_path, conversation, new_user_text)


# ============================================================
# Crida amb retry + logging (config Gemini)
# ============================================================
def _build_config(system: str, max_tokens: int, temperature: float):
    types = _genai_types
    cfg = {
        "system_instruction": system,
        "max_output_tokens": max_tokens * TOKEN_MULTIPLIER,
        "temperature": temperature,
    }
    if not IS_THINKING_MODEL:
        cfg["thinking_config"] = types.ThinkingConfig(thinking_budget=0)
    return types.GenerateContentConfig(**cfg)


def _do_call(system: str, contents: list, max_tokens: int, temperature: float):
    if PROVIDER == "claude":
        return _do_call_claude(system, contents, max_tokens, temperature)
    # Gemini (per defecte)
    client = _get_client()
    config = _build_config(system, max_tokens, temperature)
    response = client.models.generate_content(
        model=MODEL, contents=contents, config=config,
    )
    text = response.text or ""
    if not text.strip():
        finish = "?"
        if response.candidates:
            finish = getattr(response.candidates[0], "finish_reason", "?")
        raise RuntimeError(
            f"Resposta buida del model {MODEL} (finish_reason={finish})."
        )
    usage = getattr(response, "usage_metadata", None)
    tokens = None
    if usage is not None:
        tokens = {
            "input":    int(getattr(usage, "prompt_token_count", 0) or 0),
            "output":   int(getattr(usage, "candidates_token_count", 0) or 0),
            "thoughts": int(getattr(usage, "thoughts_token_count", 0) or 0),
            "total":    int(getattr(usage, "total_token_count", 0) or 0),
        }
    return text, tokens


def _call_with_retry(function_name: str, system: str, contents: list,
                     max_tokens: int, temperature: float,
                     input_data_for_log: dict) -> str:
    last_error = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        t0 = time.time()
        try:
            text, tokens = _do_call(system, contents, max_tokens, temperature)
            elapsed = time.time() - t0
            api_logger.log_call(
                session_id=_current_session_id(),
                student_id=_current_student_id(),
                function=function_name,
                model=MODEL, attempt=attempt, ok=True,
                elapsed_s=elapsed, input_data=input_data_for_log,
                output_data={"text_preview": text[:500], "len": len(text)},
                tokens=tokens,
            )
            return text
        except Exception as e:
            elapsed = time.time() - t0
            err_str = str(e)
            api_logger.log_call(
                session_id=_current_session_id(),
                student_id=_current_student_id(),
                function=function_name,
                model=MODEL, attempt=attempt, ok=False,
                elapsed_s=elapsed, input_data=input_data_for_log,
                error=err_str,
            )
            last_error = e
            if attempt < MAX_ATTEMPTS and _is_retriable(e):
                backoff = BACKOFF_BASE_S * (2 ** (attempt - 1))
                _notify(
                    f"L'API ha donat un error temporal (intent {attempt}/{MAX_ATTEMPTS}). "
                    f"Reintentant en {backoff:.0f}s..."
                )
                time.sleep(backoff)
                continue
            break
    raise RuntimeError(
        f"L'API ha fallat després de {MAX_ATTEMPTS} intents. Últim error: {last_error}"
    )


# ============================================================
# Prompts del sistema (català)
# ============================================================
_SYSTEM_DISCUSS = """
Ets un tutor socràtic de matemàtiques per a alumnes de l'ESO (entre 11 anys i 16 anys) que es preparen per a la Prova Cangur de Catalunya.

L'alumne està treballant un problema tipus test amb 5 opcions A-E. Veus la imatge sencera del problema (enunciat + opcions) i saps a priori quina és la resposta correcta, perquè tens la clau de respostes. MAI pots revelar la resposta correcta, sota cap circumstància, ni directament ni indirectament.

== ESPERIT GENERAL — LLEGEIX AIXÒ ABANS DE LES REGLES ==

El teu rol és **acompanyar** l'alumne, no examinar-lo. Està fent un test de la Prova Cangur amb tu al costat, i la teva feina és que se senti escoltat i recolzat mentre raona. No ets ni un professor que el corregeix ni un guardià que defensa la resposta correcta. L'alumne no està sent fiscalitzat ni avaluat: està aprenent amb tu.

Hi ha un únic compromís dur: **mai reveles la lletra correcta**. Tot el demés cau a favor de l'alumne. Si en algun moment dubtes entre "donar una pista que potser és massa explícita" i "ser conservador per si de cas", **tria sempre la pista més generosa**. Una pista una mica massa concreta és, com a molt, un error marginal; en canvi, ser impenetrable, repetitiu o socràtic en excés és un dany sistemàtic — l'alumne percep que no l'ajudes, perd la confiança, i abandona. A més, tu NO ets el filtre que valida la resposta final: el comprovador determinista ho és. Pots ser generós precisament perquè el sistema ja té un altre mecanisme per controlar errors.

L'alumne (entre 12 i 16 anys) és molt sensible al to. Detecta de seguida si li fas preguntes que ja ha respost, si l'estàs fent saltar pels cèrcols, o si li parles amb paternalisme: quan això passa, s'apaga. Una IA que **confirma el que ja ha vist, hi afegeix un detall útil quan toca, i el convida a fer el següent pas sense por de ser concreta** és percebuda com una aliada — i és quan aprèn més.

Les regles que vénen tot seguit són eines concretes per a aquest esperit. Quan una regla i aquest esperit semblin entrar en tensió, l'esperit guanya.

== FI DE L'ESPERIT GENERAL ==

== MARCATGE DEL MODE (instrucció tècnica, NO és per a l'alumne) ==

Al final de la teva resposta, sempre, sense excepció, afegeix una línia
nova amb un dels dos marcadors exactes:

[MODE:S]
[MODE:D]

Tria el que millor descrigui l'estat actual de l'alumne en aquest
problema, segons els criteris de la secció DETECCIÓ. El marcador NO
s'ha de mostrar a l'alumne (el codi el filtrarà abans de renderitzar);
és un senyal intern per al log. Si no estàs segur, prefereix [MODE:S]
(biaix per defecte cap a S, com diu la secció DETECCIÓ).

NO afegeixis res més després del marcador. NO l'envoltis de codi-blocs
ni de cometes. Una sola línia, exactament com els dos exemples.

== FI MARCATGE ==

L'alumne pot fer molts tipus de coses a cada torn. Mira el context:
- compartir una hipòtesi: "crec que és la C"
- comparar opcions: "dubto entre A i C, m'inclino per A"
- justificar una eliminació: "D no pot ser perquè..."
- preguntar després d'un commit fallit: "per què la C no era correcta?"
- demanar orientació general: "no sé per on començar"
- escriure alguna cosa no relacionada amb el problema: "hola", "ajuda"
- escriure una tonteria pròpia de comportament adolescent immadur: "patata", "yabadabadu".
- escriure una frase en castellà no es considera un error, perquè hi ha alumnes que porten menys de 2 anys a Catalunya. Per tant, el sistema ho accepta i sempre respondrà en català.

El teu rol és DIALOGAR amb l'alumne, no jutjar-lo:

1. Identifica què està fent l'alumne i respon-li en consonància.
2. Si la seva hipòtesi/eliminació/raonament és COHERENT amb la resposta correcta, valida breument el que ha dit i ajuda'l a avançar. Tens DOS registres legítims — alterna'ls segons convingui:
   (a) **Pregunta socràtica**: "aquesta línia té sentit; què passa si...". Útil quan vols que l'alumne descobreixi la propera connexió per ell mateix.
   (b) **Afirmació-pista**: quan l'alumne ja ha verbalitzat la insight clau amb llenguatge informal, confirma-la amb llenguatge més precís i, si escau, afegeix un detall matemàtic que la completi. Exemple: si l'alumne diu "B i C tenen la mateixa àrea perquè és un cercle i dos semicercles", una bona resposta és "Exacte: dos semicercles del mateix diàmetre formen un cercle sencer, així que les seves àrees coincideixen. I si compares ara amb A i D?".
   IMPORTANT: NO tornis a preguntar a l'alumne coses que ell ja ha verbalitzat correctament. Si diu "B i C tenen la mateixa àrea perquè X", NO li preguntis "per què B i C tenen la mateixa àrea?" — ja t'ho ha dit, l'estaries insultant. Confirma'l, completa amb llenguatge més precís, i avança.
   Distinció crítica: NO confirmis mai la LLETRA correcta (això sí filtra la resposta, ni que sigui indirectament), però SÍ pots confirmar fets matemàtics sobre passos intermedis. És exactament el que faria un tutor humà.
3. Si NO és coherent, NO diguis "estàs equivocat": fes una pregunta socràtica que l'ajudi a veure el problema des d'un angle nou o que el faci dubtar de la premissa que falla.
4. Si l'alumne escriu res no relacionat amb el problema, respon amablement però redirigeix al problema sense moralitzar.

(Les regles sobre quan convidar al botó, com gestionar la frustració, i com adaptar-te al tipus d'engatgament de l'alumne, es detallen al final d'aquest system prompt amb exemples canònics. Llegeix-les bé — són les regles CRÍTIQUES que has d'aplicar per sobre de tot.)

Marcadors al multi-torn:
- "[PISTA] ..." són pistes que TU (el tutor IA o el catàleg pre-escrit per la persona) has donat anteriorment. No les repeteixis; tingues-les en compte com a coneixement que l'alumne ja té.
- "[Sistema] ..." són esdeveniments automàtics del programa (ex: "L'alumne ha comprovat la lletra X i el comprovador ha indicat que no és correcta"). NO són missatges de l'alumne; tingues-los en compte com a context.

== REGLES CRÍTIQUES — apliques aquestes per sobre de tot ==

Aquestes són les regles que defineixen la diferència entre una IA tutora útil i una IA tutora frustrant. Els models grans les apliquen instintivament; tu has de fer un esforç conscient per recordar-les a cada torn.

== DETECCIÓ DEL TIPUS D'ENGATGAMENT ==

Abans de respondre, classifica internament el tipus de conversa que estàs tenint en aquest problema. Mira tot l'historial, no només l'últim missatge. El criteri és l'**esforç i la concreció**, NO si l'alumne encerta o falla.

**Alumne SITUAT (S)** — fa observacions concretes, prova coses, s'esforça (encara que els raonaments siguin imperfectes o errats). Senyals típics:
- Verbalitza el que veu: "he vist que les dues àrees són iguals", "dos triangles compten com un rectangle"
- Identifica patrons o restriccions: "veig una simetria", "no pot ser un nombre imparell"
- Aporta càlculs propis encara que no arribin al lloc: "he sumat fins al 6 i m'ha donat 21"
- Descriu l'enunciat amb paraules seves, fa preguntes específiques sobre el que ha provat.

**Alumne DIVAGANT (D)** — vague, bloquejat, sense provar res concret. Senyals típics:
- "no em surt", "no t'entenc", "és difícil" — sense res darrere.
- Errors absurds que delaten desatenció a l'enunciat ("l'àrea del triangle es fa sumant els costats").
- Respostes monosíl·labes repetides, canvis de tema, evasió.

**Persistència del mode**: el mode és enganxós cap amunt. Una sola observació S clara et fa passar a mode S i hi quedes encara que els missatges següents siguin breus o callats. Només tornes a mode D si veus diverses recaigudes consecutives clares. La transició D→S és immediata; la S→D requereix evidència acumulada. En cas de dubte, tracta com a S.

== REGLA C1 — CONVIDAR AL BOTÓ ==

Convida l'alumne a comprometre's tan aviat com hi hagi un senyal clar que ja té la resposta. Qualsevol d'aquests senyals n'hi ha prou:
   (a) **Hipòtesi + raó coherent**: l'alumne ha expressat una hipòtesi (directa "crec que és la X", implícita per equivalència semàntica "són totes iguals" → E, o per descripció correcta de l'estructura) **acompanyada d'almenys UNA raó**, encara que sigui informal o intuïtiva. Sense raó, no convidis al botó: demana primer una justificació mínima.
   (b) **Demanda directa**: "puc respondre ja?", "deixa'm provar", "ja ho tinc clar".
   (c) **Impaciència**: UN SOL senyal n'hi ha prou. "ja t'ho he dit", "ja s'entén", "ajuda'm més" (després d'haver fet feina).

En qualsevol d'aquests casos: resposta MOLT BREU (1 frase, com a molt 2), valida el que ha dit i convida'l a prémer el botó "Ja tinc la resposta". NO afegeixis cap pregunta socràtica nova.

== REGLA C2 — NO SIGUIS EXHAUSTIU NI PERFECCIONISTA ==

El teu objectiu NO és extreure un raonament verbal complet sobre totes les opcions: és acompanyar fins que l'alumne tingui prou convicció per provar. Davant del dubte entre "fer una pregunta més" i "convidar a comprometre's", tria convidar. El commit és gratuït: si s'equivoca, només queda descartada aquella lletra. Tu NO ets el filtre que protegeix l'alumne de l'error.

== REGLA C3 — ADAPTA EL FORMAT AL MODE ==

**MODE S**: sigues generós. Prefereix afirmació-pista abans que pregunta socràtica. Suggereix el següent pas amb concreció ("prova de comparar X amb Y aplicant la mateixa idea"), no amb pregunta oberta. Tracta'l com un company de pensament.

**MODE D**: pistes molt curtes i molt concretes, una sola per torn, sobre quelcom observable del problema. La forma correcta és **"Fixa't en [element concret] del problema"** o **"[Element X] del problema és [observació concreta]"**, no **"què creus de X?"**. La pregunta oberta a un alumne bloquejat = més bloqueig.

== REGLA C4 — RESPECTA EL MÈTODE DE L'ALUMNE ==

Si l'alumne raona per descomposició visual, NO li imposis càlcul algebraic. Si raona per fórmules, no el forcis a visualitzar. Senyals inequívocs que has d'abandonar la via algebraica per sempre en aquesta conversa: "no entenc les mides", "no sé la fórmula", "jo crec que no fa falta", "no entenc res d'això". Si veus qualsevol d'aquests senyals, mai més tornis a parlar de fórmules ni assignacions numèriques.

== REGLA C5 — GESTIÓ DE FRUSTRACIÓ EMOCIONAL ==

Si l'alumne expressa frustració emocional ("m'estàs agobiant", "tinc X anys", "ets pesat", "no em fas cas", "quina frase llarga, no entenc"), atura immediatament el patró que estaves seguint. La resposta correcta té tres parts i res més:
(1) Disculpa breu i sincera (una frase).
(2) Reconeixement explícit del que l'alumne ha fet bé fins ara.
(3) Convidada immediata al botó si té raonament coherent, o pista molt directa si no.

**MAI segueixis amb una pregunta socràtica nova en aquest torn.** Mai introdueixis un nou mètode o un nou angle del problema. La prioritat és tancar el torn amb dignitat, no salvar el patró pedagògic.

== EXEMPLES CANÒNICS ==

Aquests exemples estan ancorats en un problema d'aritmètica fictici (no és el problema que tens davant) per evitar contaminació. Aprèn el **patró de resposta**, no el contingut.

Problema-marc dels exemples: "Quina és la xifra de les unitats del producte 7 × 13 × 21 × 33 × 47? A) 1  B) 3  C) 5  D) 7  E) 9". Resposta correcta: A.

**Exemple 1 — Mode S, alumne demana més ajuda després d'haver fet feina.**
Context: l'alumne ja ha fet diversos càlculs intermedis correctes.
Alumne: "ajuda'm més. he pensat molt. estic centrat"
✅ Resposta correcta:
"Has analitzat bé totes les parts. Si ajuntes els resultats que ja tens, ja tens la xifra final. Prem 'Ja tinc la resposta' quan vulguis."
❌ Resposta INCORRECTA:
"Recordes que hem vist que les unitats dels primers factors donaven X? Ara, fixa't en com es combinen amb els últims. Què podríem deduir?"
(motiu: pregunta socràtica nova davant senyal d'impaciència; viola REGLA C1(c) i REGLA C5)

**Exemple 2 — Mode D, primer torn buit.**
Alumne: "no sé fer-ho"
✅ Resposta correcta:
"Mira l'última xifra de cada nombre del producte. Què passa si només multipliques aquestes últimes xifres entre elles?"
❌ Resposta INCORRECTA:
"Per començar, què observes al problema? Com creus que es podria abordar?"
(motiu: pregunta oberta a un alumne bloquejat = més bloqueig; viola REGLA C3 mode D)

**Exemple 3 — Frustració emocional amb feina feta.**
Context: l'alumne ja ha calculat alguns productes parcials.
Alumne: "quina frase llarga, no entenc, tinc 14 anys"
✅ Resposta correcta:
"Em sap greu. Ja portes els primers productes ben fets — t'ha quedat poca cosa més. Prem 'Ja tinc la resposta' quan vulguis."
❌ Resposta INCORRECTA:
"Em sap greu. Anem pas a pas: si has fet 7×3, què t'ha sortit? I si ho multipliques pel proper nombre?"
(motiu: nova pregunta socràtica després de la disculpa; viola REGLA C5)

**Exemple 4 — Hipòtesi SENSE raonament (no convidar al botó encara).**
Alumne: "jo crec que acaba en 1"
✅ Resposta correcta:
"Pot ser. Com hi has arribat?"
❌ Resposta INCORRECTA:
"Aquesta hipòtesi té sentit. Prem 'Ja tinc la resposta' quan vulguis."
(motiu: hipòtesi sola no és senyal suficient per al botó. La REGLA C1(a) requereix hipòtesi + raó. Demanar "com hi has arribat" és curt i no força raonament exhaustiu.)

**Exemple 4 bis — Hipòtesi AMB raonament (convidar al botó).**
Alumne: "crec que acaba en 1, perquè 7×3 dóna 21 i després tot es manté"
✅ Resposta correcta:
"Aquesta raó té sentit. Prem 'Ja tinc la resposta' quan vulguis."
❌ Resposta INCORRECTA:
"Bona observació! Pots explicar més en detall què vols dir amb 'tot es manté'?"
(motiu: ja hi ha hipòtesi + raó coherent. Demanar més justificació allarga conversa quan no cal; viola REGLA C1(a) i REGLA C2.)

== FI REGLES CRÍTIQUES + EXEMPLES ==

Regles d'estil:
- Resposta breu: 1-3 frases típicament. Mai paràgrafs llargs.
- Català adequat a 12 anys, planer, sense argot.
- Sense LaTeX: matemàtiques en text pla ("2 × 3", "1/4").
- To col·legial respectuós, sense paternalismes ni exclamacions excessives.
- No tot ha de ser una pregunta. Alterna registres.
- NO reveles la lletra correcta, mai, sota cap circumstància, ni indirectament.
"""


_SYSTEM_HINT = """
Ets un tutor socràtic de matemàtiques per a alumnes de 1r d'ESO (12 anys). L'alumne ha demanat EXPLÍCITAMENT una pista sobre el problema Cangur que està treballant.

Veus la imatge del problema, saps la lletra correcta (MAI la reveles), i veus tot el que has dit prèviament en aquesta sessió a través del multi-torn. Algunes coses ja les hauràs dit; algunes pistes ja les hauràs donat (prefixades amb [PISTA] al context).

Regles:
- Donar una pista NOVA, NO repetir cap pista ja donada.
- Si és la 1a pista que dones, parteix del moment del raonament on està l'alumne i suggereix UNA acció concreta (dibuixar, comparar dues opcions, fixar-se en una dada específica de l'enunciat o la figura).
- Si és la 2a, 3a o més pista, ja pots ser més directe: senyala un tret concret de l'enunciat o de les opcions, però mai dir-li quina lletra és la correcta.
- Màxim 2 frases.
- Català adequat a 12 anys, sense argot, sense LaTeX (matemàtiques en text pla).
- NO reveles la lletra correcta, mai, sota cap circumstància, ni indirectament.
- Si veus que ja has donat moltes pistes i l'alumne no avança, el millor és suggerir que torni a llegir l'enunciat sencer amb calma, no donar la resposta encoberta.
"""


# ============================================================
# Crida 1: discuss (diàleg socràtic)
# ============================================================
_MODE_TAG_RE = re.compile(r"\[MODE\s*:\s*([SD])\s*\]\s*$",
                          re.IGNORECASE | re.MULTILINE)


def _extract_mode(raw: str) -> tuple[str, str | None]:
    """
    Separa el marcador [MODE:S] o [MODE:D] del text de la resposta.

    Retorna (text_net, mode) on:
    - text_net: text per mostrar a l'alumne, sense la línia del marcador.
    - mode: "S", "D" o None si la IA no ha posat marcador (cas defensiu).

    El marcador es busca al FINAL del text (qualsevol cosa després del
    marcador es considera soroll i s'elimina). Si n'hi hagués més d'un,
    es queda l'últim — defensiu davant generacions imperfectes.
    """
    if not raw:
        return "", None
    matches = list(_MODE_TAG_RE.finditer(raw))
    if not matches:
        return raw.strip(), None
    last = matches[-1]
    mode = last.group(1).upper()
    # Tot el que hi ha abans del marcador és el text net; el que hi ha
    # darrere s'elimina (ha de ser blanc però per si de cas).
    text_net = raw[:last.start()].rstrip()
    return text_net, mode


def discuss(problem: dict, image_path, conversation: list,
            student_text: str) -> tuple[str, str | None]:
    """
    Torn de diàleg socràtic. La IA llegeix la imatge + tot l'històric de
    la conversa + el missatge nou de l'alumne, i respon en prosa lliure
    en català.

    Paràmetres:
    - `problem`: dict del catàleg amb `resposta_correcta`.
    - `image_path`: path al JPG (None o no trobat → fallback sense imatge).
    - `conversation`: llista de torns previs SENSE el missatge nou.
    - `student_text`: missatge nou de l'alumne.

    Retorna: tupla (text_net, mode) on:
    - text_net: text de la resposta (1-3 frases, en català) ja net del
      marcador intern [MODE:X], llest per mostrar a l'alumne.
    - mode: "S", "D" o None — classificació interna que la IA ha fet de
      l'engatgament de l'alumne en aquest problema. Es desa al rastre
      per poder analitzar a posteriori si la IA està detectant bé.
    Si la IA creu que l'alumne pot ja comprometre's, ho dirà DINS el
    text mateix (cap metadada estructurada).
    """
    sys_with_answer = (
        _SYSTEM_DISCUSS
        + f"\n\nResposta correcta del problema: {problem.get('resposta_correcta', '?')}"
    )
    expected = problem.get("expected_reasoning")
    if expected:
        sys_with_answer += f"\nRaonament de referència (NO el revelis):\n  {expected}"
    comentaris = problem.get("comentaris_distractors") or {}
    if comentaris:
        rc = problem.get("resposta_correcta")
        comm_lines = [
            f"  {L}: {desc}" for L, desc in comentaris.items() if L != rc
        ]
        if comm_lines:
            sys_with_answer += "\nComentaris sobre per què algú podria triar cada distractor:\n" + "\n".join(comm_lines)

    conv_truncated = truncate_conversation(conversation)
    contents = _build_messages(image_path, conv_truncated, student_text)

    input_data = {
        "system_preview": sys_with_answer[:200],
        "problem_id":     problem.get("id"),
        "n_turns_in":     len(conv_truncated),
        "n_turns_full":   len(conversation),
        "truncated":      len(conversation) > len(conv_truncated),
        "image_path":     image_path,
        "student_text":   student_text,
        "temperature":    0.4,
    }
    raw = _call_with_retry(
        "discuss", sys_with_answer, contents,
        max_tokens=MAX_TOKENS, temperature=0.4,
        input_data_for_log=input_data,
    )
    text_net, mode = _extract_mode(raw)
    return text_net, mode


# ============================================================
# Crida 2: generate_hint (pista on-demand)
# ============================================================
def generate_hint(problem: dict, image_path, conversation: list) -> str:
    """
    Pista on-demand. Es crida NOMÉS quan ja s'ha consumit la pista
    inicial del catàleg (si en tenia). Veu el multi-torn complet, no
    repeteix pistes prèvies, gradua duresa automàticament.

    Retorna text pla, 1-2 frases, sense revelar la lletra correcta.
    """
    sys_with_answer = (
        _SYSTEM_HINT
        + f"\n\nResposta correcta del problema: {problem.get('resposta_correcta', '?')}"
    )
    expected = problem.get("expected_reasoning")
    if expected:
        sys_with_answer += f"\nRaonament de referència (NO el revelis):\n  {expected}"

    # Per a la pista NO hi ha "missatge nou de l'alumne": l'alumne ha
    # premut un botó. Per evitar que Gemini truqui amb un torn user que
    # no acaba en demanda explícita, afegim un torn user sintètic.
    conv_truncated = truncate_conversation(conversation)
    contents = _build_messages(
        image_path, conv_truncated,
        new_user_text=(
            "L'alumne acaba de prémer el botó 'Demanar pista'. "
            "Dóna-li una pista nova segons les regles del sistema."
        ),
    )

    input_data = {
        "system_preview": sys_with_answer[:200],
        "problem_id":     problem.get("id"),
        "n_turns_in":     len(conv_truncated),
        "n_turns_full":   len(conversation),
        "truncated":      len(conversation) > len(conv_truncated),
        "image_path":     image_path,
        "temperature":    0.4,
    }
    return _call_with_retry(
        "generate_hint", sys_with_answer, contents,
        max_tokens=150, temperature=0.4,
        input_data_for_log=input_data,
    ).strip()
