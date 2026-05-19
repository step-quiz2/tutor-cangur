"""
Màquina d'estats del Tutor Cangur 1r ESO.

Visió general per a un lector nou
=================================
Aquest mòdul implementa tota la lògica de control d'una sessió de tutoria
**sense dependre de Streamlit**. La UI (app.py) només crida les funcions
públiques i llegeix l'estat retornat. Això permet provar la lògica amb
scripts o tests sense aixecar la UI.

L'estat de la sessió és un `dict` (no una classe) que es construeix amb
`new_session_state(problem_id)` i s'actualitza torn a torn.

Punts d'entrada públics
-----------------------
- `new_session_state(problem_id)` — construeix l'estat inicial.
- `process_message(state, student_text)` — l'alumne ha escrit un
  missatge al diàleg. Crida `llm.discuss`, afegeix els dos torns
  (user + assistant) a la conversation_history.
- `request_hint(state)` — l'alumne ha premut "Demanar pista". Si encara
  no s'ha consumit la pista inicial del catàleg i existeix, l'usa (cost
  API = 0). Altrament crida `llm.generate_hint`. La pista resultant
  s'injecta a la conversation_history com a torn assistant amb kind="hint".
- `process_commit(state, letter)` — l'alumne ha clicat una de les
  lletres A-E. Comprovació determinista. Si falla, injecta un
  system_event a la conversation_history perquè la IA tingui context
  per a futures preguntes post-error.
- `build_trace(state)` / `serialize_trace(state)` — JSON per al professor.

Anatomia de la conversation_history
-----------------------------------
Cada element és un dict:
    {
        "role":    "user" | "assistant",
        "kind":    "message" | "hint" | "system_event",
        "content": str,
        "ts":      float,
        # opcional:
        "source":  "catalog" | "ia"  # només per kind="hint"
    }

- `message` és el diàleg normal alumne ↔ IA.
- `hint` és una pista (vingui del catàleg o de la IA). El kind permet a
  `llm.py` prefixar-la amb "[PISTA] " quan munta el prompt.
- `system_event` és informació externa que la IA ha de tenir en compte
  com a context (ex: "L'alumne ha intentat la lletra C i no era correcta").

Diferències amb les versions anteriors
--------------------------------------
- NO hi ha `process_reasoning` ni veredictes (`correct_path`, `dead_end`...).
  La IA dialoga lliurement; no classifica.
- NO hi ha `_handle_inappropriate` ni `inappropriate_warnings`. Vam
  treure el filtre determinista (decisió de l'usuari); la IA gestiona
  els "hola" o "ajuda" amb amabilitat.
- NO hi ha `reasoning_turns` ni `stagnation_consecutive`. Les pistes
  són on-demand, no automàtiques.
- SÍ hi ha `conversation_history` i `pistes_count` com a camps nous.
- El veredicte final només pot ser None (en curs) o "solved" (commit
  correcte). No hi ha "suspended" perquè ja no hi ha avisos.
"""

import copy
import json
import os
import time
import uuid
from datetime import datetime, timezone

import problems as PB
import llm as L


# Mínim de raonament per acceptar com a torn vàlid (en caràcters tras
# strip). Filtra inputs trivials tipus "ok" o ".". Tot i que no fem cap
# filtre semàntic, sí que volem evitar enviar un caràcter solitari a la
# IA (cost innecessari, resposta sense valor).
MIN_MESSAGE_CHARS = 2

# Sostre de missatges de l'alumne per problema. Quan s'arriba al sostre,
# el botó "Enviar missatge" deixa d'estar disponible; l'alumne pot encara
# demanar pistes i commit-ejar lletres. La restricció és pedagògica:
# limita la conversa il·limitada i empeny l'alumne cap a l'acció.
# Compten només els torns user/message; NO compten pistes (kind=hint) ni
# events del sistema (kind=system_event).
MAX_STUDENT_MESSAGES = 10


# ============================================================
# Construcció d'un estat nou
# ============================================================
def new_session_state(problem_id: str) -> dict:
    """
    Estat inicial d'una sessió per a un problema Cangur concret.

    No es demana cap identificador de l'alumne: tot el sistema treballa
    de manera anònima. Cada sessió queda marcada al log de l'API només
    pel `session_id` (12 hex chars) generat aquí.
    """
    problem = PB.get_problem(problem_id)
    if problem is None:
        raise ValueError(f"Problema desconegut: {problem_id}")
    session_id = uuid.uuid4().hex[:12]
    L.set_log_context(student_id=None, session_id=session_id)
    return {
        "session_id":             session_id,
        "student_id":             None,
        "problem_id":             problem_id,
        "problem":                copy.deepcopy(problem),
        "started_at":             datetime.now(timezone.utc).isoformat(),
        "started_at_ts":          time.time(),

        # --- Mode i progrés del problema ---
        "mode":                   "reasoning",      # "reasoning" | "committing"
        "eliminated_options":     [],
        "commit_letter":          None,
        "commit_attempts":        [],

        # --- Conversa amb la IA ---
        "conversation_history":   [],
        "pistes_count":           0,

        # --- Veredicte final ---
        # None mentre la sessió segueix.
        # "solved" → l'alumne ha encertat la lletra (commit correcte).
        # Sense límit de commits ni 'suspended': pot insistir sempre.
        "verdict_final":          None,

        # --- Missatges UI i rastre ---
        # `messages`: missatges transitoris UI (commit_fail, warnings tècnics).
        # No són part del diàleg amb la IA; són flash UI.
        "messages":               [],
        # `history`: rastre cronològic de totes les accions. Es serialitza
        # al `build_trace`.
        "history":                [],
    }


# ============================================================
# Helper de missatges flash per a la UI
# ============================================================
def _push_msg(state, kind: str, text: str, persistent: bool = False):
    """
    Encua un missatge flash per a la UI. NO és part del diàleg amb la
    IA; serveix per a feedback tècnic (errors API, commit fail).

    `kind`:
      - "warning"      → error tècnic, missatge curt o ús inadequat
      - "commit_ok"    → encert de commit
      - "commit_fail"  → commit fallit (persistent per al següent torn)
    """
    state["messages"].append({
        "kind": kind,
        "text": text,
        "persistent": persistent,
        "ts": time.time(),
    })


# ============================================================
# Helper: path absolut a la imatge del problema
# ============================================================
def _image_path_for(problem: dict) -> str | None:
    """
    Retorna el path absolut a la imatge del problema (si en té).
    Robust al CWD: usa la posició relativa a aquest fitxer
    (`tutor.py`) per trobar la carpeta `data/`. Així `streamlit run`
    funciona sigui quin sigui el directori de treball.
    """
    imatge = problem.get("imatge")
    if not imatge:
        return None
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "data", imatge)


# ============================================================
# Comprovació determinista de lletra
# ============================================================
def _check_choice(letter: str, expected: str) -> bool:
    """Tolerant a majúscules/minúscules i espais; retorna False si no és
    una lletra A-E vàlida."""
    if not letter or not expected:
        return False
    l = letter.strip().upper()
    if l not in ("A", "B", "C", "D", "E"):
        return False
    return l == expected.strip().upper()


# ============================================================
# Comptadors de missatges de l'alumne
# ============================================================
def count_student_messages(state: dict) -> int:
    """
    Nombre de missatges de diàleg que l'alumne ha enviat fins ara.
    NO compten pistes ni system_events; només kind="message" i role="user".
    """
    return sum(
        1 for t in state.get("conversation_history", [])
        if t.get("kind") == "message" and t.get("role") == "user"
    )


def messages_remaining(state: dict) -> int:
    """Missatges que encara pot enviar l'alumne abans del sostre."""
    return max(0, MAX_STUDENT_MESSAGES - count_student_messages(state))


def can_send_message(state: dict) -> bool:
    """True si l'alumne encara pot enviar com a mínim un missatge més."""
    return messages_remaining(state) > 0


def current_engagement_mode(state: dict) -> str | None:
    """
    Últim mode d'engatgament que la IA ha marcat en aquest problema.
    Retorna "S", "D" o None (si encara no hi ha hagut cap torn IA o si
    la IA no ha posat marcador en l'últim torn).

    Mira el conversation_history del problema actual de darrere a
    davant i retorna el primer `mode` que trobi en un torn assistant
    amb kind="message". Útil per a la sidebar de debug.
    """
    for turn in reversed(state.get("conversation_history", [])):
        if (turn.get("role") == "assistant"
                and turn.get("kind") == "message"
                and "mode" in turn):
            return turn["mode"]
    return None


# ============================================================
# Process turn: missatge de diàleg
# ============================================================
def process_message(state: dict, student_text: str) -> dict:
    """
    Punt d'entrada per a un torn de diàleg. L'alumne ha escrit text i
    premut "Enviar missatge".

    Flux:
      1. Si la sessió ja ha acabat, no fer res.
      2. Neteja l'input. Si està buit o és un caràcter solitari, missatge.
      3. Afegeix el torn de l'alumne al conversation_history.
      4. Crida `L.discuss(problem, image_path, conv_sense_aquest_torn,
         student_text)`. La conversa que es passa NO inclou el missatge
         nou; `L.discuss` el rep separat i el munta dins el primer Content.
      5. Afegeix el torn de la IA al conversation_history.
      6. Actualitza el rastre cronològic (state["history"]).
    """
    state = copy.deepcopy(state)

    # Neteja missatges flash no persistents.
    state["messages"] = [m for m in state["messages"] if m.get("persistent")]

    if state.get("verdict_final") is not None:
        return state

    # Sostre de missatges per problema. Es comprova ABANS de qualsevol altra
    # validació o crida a la IA, perquè és una porta dura: superat el límit,
    # ni s'envia ni es factura cap crida. L'alumne pot demanar pista o
    # commit-ejar (les dues accions segueixen disponibles).
    if not can_send_message(state):
        _push_msg(
            state, "warning",
            f"Has fet servir els {MAX_STUDENT_MESSAGES} missatges per a "
            f"aquest problema. Pots demanar una pista o respondre amb el "
            f"botó 'Ja tinc la resposta' quan vulguis.",
            persistent=True,
        )
        return state

    s = (student_text or "").strip()
    if len(s) < MIN_MESSAGE_CHARS:
        _push_msg(state, "warning",
                  "El missatge és massa curt. Escriu una mica més.")
        return state

    problem = state["problem"]
    image_path = _image_path_for(problem)

    # Captura la conversa PRÈVIA (sense el nou missatge) per passar-la
    # a llm.discuss. La IA rep aquest snapshot + el missatge nou separat.
    prior_conversation = list(state["conversation_history"])

    # Afegim el torn de l'alumne abans de la crida (per si la crida peta,
    # l'eliminarem). Així el rastre és consistent.
    student_turn = {
        "role":    "user",
        "kind":    "message",
        "content": s,
        "ts":      time.time(),
    }
    state["conversation_history"].append(student_turn)

    try:
        ai_text, ai_mode = L.discuss(problem, image_path,
                                     prior_conversation, s)
    except Exception as e:
        # Treure el torn afegit perquè no s'embruti la history amb un
        # missatge sense resposta.
        state["conversation_history"].pop()
        _push_msg(state, "warning", f"Error de connexió amb la IA: {e}")
        return state

    # Afegeix el torn de la IA. El camp `mode` ("S", "D" o None) és la
    # classificació interna que la IA ha fet del tipus d'engatgament
    # de l'alumne en aquest problema. Es desa al rastre per poder
    # auditar a posteriori si la classificació és consistent amb el
    # que veuria un humà llegint la conversa.
    ai_turn = {
        "role":    "assistant",
        "kind":    "message",
        "content": ai_text,
        "mode":    ai_mode,
        "ts":      time.time(),
    }
    state["conversation_history"].append(ai_turn)

    # Rastre cronològic
    state["history"].append({
        "type":        "discuss",
        "student":     s,
        "ai_response": ai_text,
        "mode":        ai_mode,
        "ts":          time.time(),
    })
    return state


# ============================================================
# Process turn: demanar pista
# ============================================================
def request_hint(state: dict) -> dict:
    """
    Punt d'entrada per al botó "Demanar pista".

    Lògica (decisió arquitectònica de l'usuari, opció híbrida):
    - Si `pistes_count == 0` i existeix `problem["pista_inicial"]`:
        usa la pista escrita per la persona al catàleg. Cost API = 0.
    - Altrament, crida `L.generate_hint`. La IA veu totes les pistes
      prèvies al multi-torn i gradua la duresa automàticament.

    La pista resultant s'injecta al conversation_history com a torn
    assistant amb kind="hint" (perquè `llm._build_contents` la prefixi
    amb "[PISTA] " als torns següents).
    """
    state = copy.deepcopy(state)
    state["messages"] = [m for m in state["messages"] if m.get("persistent")]

    if state.get("verdict_final") is not None:
        return state

    problem = state["problem"]

    if state["pistes_count"] == 0 and problem.get("pista_inicial"):
        # Pista 1 del catàleg
        hint_text = problem["pista_inicial"]
        source = "catalog"
    else:
        # Pista IA on-demand
        image_path = _image_path_for(problem)
        try:
            hint_text = L.generate_hint(
                problem, image_path, state["conversation_history"],
            )
        except Exception as e:
            _push_msg(state, "warning", f"Error en generar pista: {e}")
            return state
        source = "ia"

    hint_turn = {
        "role":    "assistant",
        "kind":    "hint",
        "content": hint_text,
        "source":  source,
        "ts":      time.time(),
    }
    state["conversation_history"].append(hint_turn)
    state["pistes_count"] += 1

    state["history"].append({
        "type":    "hint",
        "source":  source,
        "content": hint_text,
        "ts":      time.time(),
    })
    return state


# ============================================================
# Process turn: commit d'una lletra
# ============================================================
def process_commit(state: dict, letter: str) -> dict:
    """
    Punt d'entrada per a un commit de lletra. L'alumne ha clicat un dels
    botons A-E del bloc "Ja tinc la resposta".

    Política (decidida amb l'usuari): sense límit de commits. Si encerta,
    `verdict_final = "solved"`. Si falla, la lletra fallida queda a
    `eliminated_options` i la sessió torna al mode "reasoning"; pot
    insistir tants cops com vulgui.

    Quan el commit falla, INJECTEM un system_event al conversation_history
    perquè la IA tingui context: si l'alumne després pregunta "per què la
    C no era correcta?", la IA sap exactament quina C i pot respondre.

    Comprovació determinista: NO crida a la IA.
    """
    state = copy.deepcopy(state)
    state["messages"] = [m for m in state["messages"] if m.get("persistent")]

    if state.get("verdict_final") is not None:
        return state

    expected = state["problem"].get("resposta_correcta", "")
    chosen = (letter or "").strip().upper()

    if chosen not in ("A", "B", "C", "D", "E"):
        _push_msg(state, "warning",
                  f"Lletra invàlida: {letter!r}. Tria una de les opcions A-E.")
        return state

    correct = _check_choice(chosen, expected)
    state["commit_attempts"].append(chosen)
    state["history"].append({
        "type":    "commit",
        "letter":  chosen,
        "correct": correct,
        "ts":      time.time(),
    })

    if correct:
        state["commit_letter"] = chosen
        state["verdict_final"] = "solved"
        n_intents = len(state["commit_attempts"])
        if n_intents == 1:
            _push_msg(state, "commit_ok",
                      f"🎉 Correcte! La resposta correcta és **{chosen}**. "
                      "Ho has aconseguit a la primera. Molt bé!")
        else:
            _push_msg(state, "commit_ok",
                      f"🎉 Correcte! La resposta correcta és **{chosen}**. "
                      f"Ho has aconseguit en {n_intents} intents.")
        # Injectem també un system_event al diàleg perquè quedi al rastre
        state["conversation_history"].append({
            "role":    "user",
            "kind":    "system_event",
            "content": f"L'alumne ha comprovat la lletra {chosen} i és correcta. Sessió completada.",
            "ts":      time.time(),
        })
        return state

    # Commit incorrecte
    if chosen not in state["eliminated_options"]:
        state["eliminated_options"].append(chosen)
    state["mode"] = "reasoning"

    # System event: la IA ha de saber-ho per a futures preguntes post-error.
    state["conversation_history"].append({
        "role":    "user",
        "kind":    "system_event",
        "content": (
            f"L'alumne ha comprovat la lletra {chosen} i el comprovador "
            f"determinista ha indicat que no és correcta. L'alumne pot "
            f"seguir raonant i tornar-ho a provar."
        ),
        "ts":      time.time(),
    })

    n_intents = len(state["commit_attempts"])
    _push_msg(state, "commit_fail",
              f"❌ La lletra **{chosen}** no és correcta. "
              f"Pots seguir raonant i tornar-ho a intentar. "
              f"(Intents fets: {n_intents}.)",
              persistent=True)
    return state


# ============================================================
# Transicions explícites entre modes
# ============================================================
def request_commit_mode(state: dict) -> dict:
    """L'alumne ha premut 'Ja tinc la resposta'."""
    state = copy.deepcopy(state)
    if state.get("verdict_final") is not None:
        return state
    state["mode"] = "committing"
    state["history"].append({"type": "enter_commit_mode", "ts": time.time()})
    return state


def cancel_commit_mode(state: dict) -> dict:
    """L'alumne s'ha penedit i vol seguir raonant."""
    state = copy.deepcopy(state)
    if state.get("verdict_final") is not None:
        return state
    state["mode"] = "reasoning"
    state["history"].append({"type": "cancel_commit_mode", "ts": time.time()})
    return state


# ============================================================
# Rastre JSON per al professor
# ============================================================
def build_trace(state: dict) -> dict:
    """
    Genera el rastre serialitzable per al professor al final d'una sessió.

    Inclou la conversation_history sencera + el rastre cronològic
    d'events (commits, pistes, missatges).

    Mètriques útils per al pilot:
    - `n_commits == 1` i `veredicte_final == "solved"` → autonomia màxima.
    - `n_commits > 3` → probable necessitat de més suport humà.
    - `n_pistes_total` alt → l'alumne s'estanca però rebia ajuda.
    - `n_pistes_catalog` vs `n_pistes_ia`: quantes pistes preescrites
      vs. quantes generades on-demand.
    """
    duration = time.time() - state["started_at_ts"]
    problem = state["problem"]

    # Comptadors de pistes (catàleg vs IA)
    n_pistes_catalog = 0
    n_pistes_ia = 0
    for t in state["conversation_history"]:
        if t.get("kind") == "hint":
            if t.get("source") == "catalog":
                n_pistes_catalog += 1
            else:
                n_pistes_ia += 1

    # Comptador de torns de diàleg (només "message" del rol alumne)
    n_dialeg_turns = sum(
        1 for t in state["conversation_history"]
        if t.get("kind") == "message" and t.get("role") == "user"
    )

    # Comptadors de mode d'engatgament. La IA marca cada resposta com a
    # mode "S" (situat) o "D" (divagant) segons criteris del prompt. Els
    # comptem per saber, a grans trets, com ha vist la IA aquesta sessió.
    n_mode_S = sum(
        1 for t in state["conversation_history"]
        if t.get("role") == "assistant" and t.get("mode") == "S"
    )
    n_mode_D = sum(
        1 for t in state["conversation_history"]
        if t.get("role") == "assistant" and t.get("mode") == "D"
    )
    # Mode actual = últim mode marcat (None si no hi ha hagut torns o
    # si la IA no ha marcat l'últim).
    mode_final = None
    for t in reversed(state["conversation_history"]):
        if t.get("role") == "assistant" and "mode" in t:
            mode_final = t["mode"]
            break

    n_commits = len(state["commit_attempts"])
    return {
        "session_id":  state["session_id"],
        "problema": {
            "id":                state["problem_id"],
            "categoria":         problem.get("categoria"),
            "any":               problem.get("any"),
            "numero":            problem.get("numero"),
            "punts":             problem.get("punts"),
            "tema":              problem.get("tema"),
            "imatge":            problem.get("imatge"),
            "resposta_correcta": problem.get("resposta_correcta"),
        },
        "started_at":           state["started_at"],
        "durada_segons":        round(duration, 1),

        # Diàleg
        "n_dialeg_turns":       n_dialeg_turns,
        "n_mode_S":             n_mode_S,
        "n_mode_D":             n_mode_D,
        "mode_final":           mode_final,
        "conversation_history": state["conversation_history"],

        # Pistes
        "n_pistes_total":       state["pistes_count"],
        "n_pistes_catalog":     n_pistes_catalog,
        "n_pistes_ia":          n_pistes_ia,

        # Commits
        "commit_attempts":      list(state["commit_attempts"]),
        "n_commits":            n_commits,
        "eliminated_options":   list(state["eliminated_options"]),
        "commit_letter_final":  state["commit_letter"],

        # Rastre cronològic complet
        "torns":                state["history"],

        # Veredicte final
        "veredicte_final":      state["verdict_final"] or "en_curs",
    }


def serialize_trace(state: dict) -> str:
    """Versió string del rastre, llesta per a `open(...).write()` o `st.json`."""
    return json.dumps(build_trace(state), ensure_ascii=False, indent=2)
