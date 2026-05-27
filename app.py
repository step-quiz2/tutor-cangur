"""
Tutor Cangur 1r ESO — UI Streamlit.

Per executar:
    export GEMINI_API_KEY=...
    streamlit run app.py

Mode debug: afegeix `?debug=1` a la URL per veure el cost de l'API,
el rastre intern de la sessió i mètriques.

Disseny UI
----------
- L'enunciat del problema apareix com a imatge (jpg de data/).
- Sota la imatge, una tarjeta discreta amb les 5 lletres A-E (només
  com a marcador d'eliminades; el text de les opcions ja és a la imatge).
- El cos central és un FIL DE XAT amb els torns de la conversa
  (alumne / IA / pistes). Els system_events (commit fallit, etc.)
  apareixen com a text discret al mig del fil.
- Tres botons al peu:
    [📩 Enviar missatge]   — envia el text al diàleg amb la IA
    [💡 Demanar pista]      — invoca la pista (catàleg o IA segons compti)
    [✋ Ja tinc la resposta] — entra al mode commit (5 botons A-E)
"""

import os
import uuid
from datetime import datetime

import streamlit as st

import problems as PB
import tutor as T
import llm as L
import api_logger


# ============================================================
# ENABLE_AI: gate global per a TOTES les crides API a la IA
# ============================================================
# Per defecte les crides a la IA estan DESACTIVADES, per evitar despeses
# no intencionades en desplegaments públics. Per activar-les cal definir
# el secret `ENABLE_AI = "1"` (o `ENABLE-AI = "1"`) als secrets de
# Streamlit Cloud (o exportar la variable d'entorn en local).
#
# Aquí copiem el valor de `st.secrets` a `os.environ` perquè `llm.py`
# (que no importa Streamlit) pugui llegir-lo amb un simple `os.environ`.
# Streamlit Cloud ja propaga alguns secrets a env vars automàticament,
# però fer-ho explícitament aquí ens dona un comportament uniforme
# (local + cloud) i no és destructiu si la variable ja està definida.
def _propagate_enable_ai_to_env():
    try:
        secrets = st.secrets
    except Exception:
        return
    for name in ("ENABLE_AI", "ENABLE-AI"):
        try:
            if name in secrets:
                os.environ[name] = str(secrets[name]).strip()
        except Exception:
            continue


_propagate_enable_ai_to_env()


# ============================================================
# Helpers UI
# ============================================================
def _is_debug_mode() -> bool:
    """`?debug=1` a la URL activa info addicional al sidebar i main pane."""
    if "debug_mode" not in st.session_state:
        try:
            qp = st.query_params.get("debug")
        except Exception:
            qp = None
        st.session_state.debug_mode = (qp == "1")
    return st.session_state.debug_mode


def _init_state():
    """Inicialitza les claus de `st.session_state` necessàries."""
    if "tutor_state" not in st.session_state:
        st.session_state.tutor_state = None
    if "input_counter" not in st.session_state:
        st.session_state.input_counter = 0


# ============================================================
# Configuració de la pàgina
# ============================================================
st.set_page_config(
    page_title="Prova Cangur",
    page_icon="🦘",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  .block-container {
      padding-top: 0.8rem !important;       /* abans 2rem (-60%) */
      padding-left: 0.5rem !important;      /* abans ~1.25rem default (-60%) */
      padding-right: 0.5rem !important;
      font-size: 1.05rem;
  }
  /* Titol de l'app "Prova Cangur". */
  h2.app-title {
      font-size: 1.1rem !important;
      font-weight: 700;
      margin: 0.25rem 0 0.5rem 0 !important;
      padding: 0 !important;
      line-height: 1.3 !important;
  }
  /* Titol del problema "1ESO-2026. Pregunta N...". */
  h3.problem-title {
      font-size: 1.0rem !important;
      font-weight: 700;
      margin: 0.2rem 0 0.4rem 0 !important;
      padding: 0 !important;
      line-height: 1.3 !important;
  }
  /* Titol "Diàleg" del panell dret: un 20% mes petit. `zoom` escala
     tot el bloc del titol (text i marges) exactament al 80%. */
  h4.dialeg-title {
      zoom: 0.8;
  }
  hr { margin: 0.6rem 0 !important; }

  /* --- Fil de xat --- */
  /* Bombolla de l'alumne (a la dreta) */
  .chat-user {
      background: #dbeafe;
      border-radius: 14px 14px 4px 14px;
      padding: 0.6rem 0.9rem;
      margin: 0.4rem 0 0.4rem 15%;
      max-width: 85%;
      color: #1e3a5f;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  }
  /* Bombolla de la IA (a l'esquerra) */
  .chat-ai {
      background: #f1f5f9;
      border-radius: 14px 14px 14px 4px;
      padding: 0.6rem 0.9rem;
      margin: 0.4rem 15% 0.4rem 0;
      max-width: 85%;
      color: #1f2937;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  }
  /* Bombolla de pista (a l'esquerra, més clara/groga) */
  .chat-hint {
      background: #fef9c3;
      border-left: 4px solid #eab308;
      border-radius: 8px 8px 8px 4px;
      padding: 0.6rem 0.9rem;
      margin: 0.4rem 15% 0.4rem 0;
      max-width: 85%;
      color: #713f12;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  }
  /* System events: text discret centrat */
  .chat-system {
      text-align: center;
      color: #6b7280;
      font-size: 0.85rem;
      font-style: italic;
      margin: 0.5rem 25%;
      padding: 0.2rem;
      border-top: 1px dashed #e5e7eb;
      border-bottom: 1px dashed #e5e7eb;
  }

  /* Separador entre blocs pregunta-resposta del diàleg.
     Un bloc comença a cada missatge nou de l'alumne (excepte el primer). */
  .turn-separator {
      border: none;
      border-top: 1px solid #e5e7eb;
      margin: 1.2rem 0 0.4rem 0;
  }

  /* CRITIC per al sticky: cap ancestor de l'element sticky pot tenir
     `overflow` diferent de `visible`. Si en te, l'especificacio CSS diu
     que el sticky es queda "atrapat" dins aquell ancestor i no funciona.
     PERO no podem tocar `stMain` ni `stAppViewContainer`: alguns dels seus
     `overflow` son els que proporcionen el scroll a la pagina sencera.
     Si els forcem a visible, el sticky funciona pero la pagina no fa scroll.
     Per tant: forcem `overflow: visible` nomes als contenidors INTERIORS
     entre el scroll container (stMain) i el sticky element. */
  div[data-testid="stMainBlockContainer"],
  div.main,
  .block-container,
  div[data-testid="stVerticalBlock"],
  div[data-testid="stVerticalBlockBorderWrapper"] {
      overflow: visible !important;
  }

  /* Amaguem la capçalera fixa de Streamlit. Es `position: fixed` i ocupa
     la franja superior del viewport (~3.75rem); si la deixem visible, el
     panell sticky s'enganxa PER SOTA seu i la imatge de l'enunciat queda
     tapada/retallada. Amagant-la, `top: 0.5rem` ja s'enganxa a la vora
     real del viewport. No perdem res util: la sidebar esta col·lapsada,
     l'app ja te el seu propi titol, i els `st.spinner` cobreixen el
     feedback d'"executant". */
  header[data-testid="stHeader"] {
      display: none !important;
  }

  /* LAYOUT EN DUES COLUMNES amb panell del problema STICKY. */
  div[data-testid="stHorizontalBlock"]:has(.st-key-problem_panel) {
      align-items: flex-start !important;
  }
  div[data-testid="stColumn"]:has(.st-key-problem_panel) {
      position: sticky !important;
      top: 0.5rem !important;
      align-self: flex-start !important;
  }
  /* Padding suau al panell del problema per separar-lo visualment */
  .st-key-problem_panel {
      padding: 0.25rem 0.5rem 0.5rem 0.5rem;
  }
  /* Imatge dins el panell del problema: respecta proporcions naturals,
     centrada, mai retallada (object-fit: contain). */
  .st-key-problem_panel .header-image {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      margin: 0.3rem 0;
  }
  .st-key-problem_panel .header-image img {
      max-width: 100%;
      max-height: 45vh;
      width: auto;
      height: auto;
      object-fit: contain;
      display: block;
  }

  /* Missatges flash (errors tècnics, commits) */
  .msg-warning      { border-left: 4px solid #ef4444; padding: 0.4rem 0.8rem; background: #fef2f2; margin: 0.3rem 0; }
  .msg-info         { border-left: 4px solid #3b82f6; padding: 0.4rem 0.8rem; background: #eff6ff; margin: 0.3rem 0; }
  .msg-commit_ok    { border-left: 4px solid #22c55e; padding: 0.6rem 0.9rem; background: #f0fdf4; margin: 0.5rem 0; font-size: 1.1rem; }
  .msg-commit_fail  { border-left: 4px solid #f97316; padding: 0.5rem 0.9rem; background: #fff7ed; margin: 0.3rem 0; }

  /* Tarjeta d'opcions A-E (compacta; el text real és a la imatge) */
  .opcions-card {
      background: #fafafa;
      border: 1px solid #e5e7eb;
      border-radius: 6px;
      padding: 0.5rem 1rem;
      margin: 0.4rem 0 0.8rem 0;
      font-size: 0.95rem;
  }
  .opcions-card .label-row {
      display: inline-block;
      margin-right: 1rem;
      padding: 0.15rem 0.5rem;
      background: white;
      border: 1px solid #d1d5db;
      border-radius: 4px;
      font-weight: 600;
  }
  .opcions-card .label-row.eliminated {
      color: #9ca3af;
      text-decoration: line-through;
      background: #f3f4f6;
  }

  /* Tags del multiselect (3p, 4p, 5p) en gris en lloc de vermell */
  [data-testid="stMultiSelect"] [data-baseweb="tag"] {
      background-color: #6b7280 !important;
  }

  /* Amaguem la indicacio "Press Ctrl+Enter to apply" / "to submit form"
     que Streamlit posa automaticament sota els camps de text. */
  [data-testid="InputInstructions"] {
      display: none !important;
  }

  /* Botons d'accio "Demanar pista" i "Ja tinc la resposta".
     Streamlit genera automaticament una classe .st-key-<key> al container DOM
     de cada widget amb key. Apuntem-hi directament. */
  .st-key-request_hint button {
      background-color: #fef08a !important;
      border: 1px solid #fef08a !important;
      color: #1a1a1a !important;
      transition: background-color 0.15s, border-color 0.15s, border-width 0.15s;
  }
  .st-key-request_hint button:hover {
      background-color: #eab308 !important;
      border: 2px solid #000 !important;
      color: #000 !important;
  }
  .st-key-enter_commit button {
      background-color: #bbf7d0 !important;
      border: 1px solid #bbf7d0 !important;
      color: #1a1a1a !important;
      transition: background-color 0.15s, border-color 0.15s, border-width 0.15s;
  }
  .st-key-enter_commit button:hover {
      background-color: #4ade80 !important;
      border: 2px solid #000 !important;
      color: #000 !important;
  }

  /* Boto "Inicia el problema seguent": border blau gruixut + text en
     negreta; en passar-hi el ratoli, fons blau suau i border negre. */
  .st-key-start_next button {
      border: 3px solid #2563eb !important;
      font-weight: 700 !important;
      color: #1a1a1a !important;
      transition: background-color 0.15s, border-color 0.15s;
  }
  .st-key-start_next button:hover {
      background-color: #dbeafe !important;
      border: 3px solid #000 !important;
      color: #1a1a1a !important;
  }

  /* === Canvis UX recents === */
  /* Canvi 1: espai extra (~3×) entre l'expander "Escull un problema"
     i el títol del problema. */
  h3.problem-title {
      margin-top: 1.6rem !important;
  }

  /* Canvi 2: espai extra (~3×) entre la fila A-E (.opcions-card) i la
     fila de botons d'acció (Vull una pista / Ja tinc la resposta). */
  .st-key-problem_panel .opcions-card {
      margin-bottom: 1.4rem !important;
  }

  /* Canvi 3b: text_area del diàleg amb fons blau-suau, border negre
     clar i placeholder en cursiva. */
  .st-key-message_input textarea {
      background-color: #dbeafe !important;
      border: 1px solid #1f2937 !important;
      color: #1f2937 !important;
  }
  .st-key-message_input textarea::placeholder {
      font-style: italic;
      color: #6b7280 !important;
      opacity: 1;
  }

  /* Canvi 4: botó "Enviar missatge" amb fons blau-suau (mateix to que
     l'input), hover blau més fort + border negre 2px (coherent amb els
     altres botons d'acció). Aquest botó és un st.form_submit_button, i
     com que no acceptem `key` als form_submit_button de Streamlit, el
     localitzem via el formulari ancestre. */
  div[data-testid="stForm"] button[kind="secondaryFormSubmit"],
  div[data-testid="stForm"] button[data-testid="stBaseButton-secondaryFormSubmit"] {
      background-color: #dbeafe !important;
      border: 1px solid #dbeafe !important;
      color: #1a1a1a !important;
      transition: background-color 0.15s, border-color 0.15s, border-width 0.15s;
  }
  div[data-testid="stForm"] button[kind="secondaryFormSubmit"]:hover,
  div[data-testid="stForm"] button[data-testid="stBaseButton-secondaryFormSubmit"]:hover {
      background-color: #60a5fa !important;
      border: 2px solid #000 !important;
      color: #000 !important;
  }

  /* Canvi 6: cursor de prohibit en passar el ratolí per damunt de
     les lletres A-E al panell del problema. Recordatori visual que
     aquí no es contesta (cal clicar "Ja tinc la resposta"). */
  .st-key-problem_panel .opcions-card .label-row:hover {
      cursor: not-allowed;
  }

  /* Mode commit: 5 botons A-E petits amb fons blau-suau. Streamlit
     genera classes `.st-key-commit_A`, `.st-key-commit_B`, etc. */
  .st-key-commit_A button,
  .st-key-commit_B button,
  .st-key-commit_C button,
  .st-key-commit_D button,
  .st-key-commit_E button {
      background-color: #dbeafe !important;
      border: 1px solid #dbeafe !important;
      color: #1a1a1a !important;
      font-weight: 600 !important;
      transition: background-color 0.15s, border-color 0.15s, border-width 0.15s;
  }
  .st-key-commit_A button:hover,
  .st-key-commit_B button:hover,
  .st-key-commit_C button:hover,
  .st-key-commit_D button:hover,
  .st-key-commit_E button:hover {
      background-color: #60a5fa !important;
      border: 2px solid #000 !important;
      color: #000 !important;
  }

  /* Mode commit: botó "← Tornar a raonar" amb fons gris-suau i hover
     coherent amb els altres botons (border negre 2px). */
  .st-key-cancel_commit button {
      background-color: #e5e7eb !important;
      border: 1px solid #e5e7eb !important;
      color: #1a1a1a !important;
      transition: background-color 0.15s, border-color 0.15s, border-width 0.15s;
  }
  .st-key-cancel_commit button:hover {
      background-color: #9ca3af !important;
      border: 2px solid #000 !important;
      color: #000 !important;
  }

  /* El sidebar de Streamlit ja no es fa servir: tots els controls
     (selector de problema, filtres, debug) viuen al main pane dins
     d'un expander compacte a la part superior. Aixi recuperem tota
     l'amplada del viewport per al panell del problema + dialeg. */
  [data-testid="stSidebar"] {
      display: none !important;
  }
  [data-testid="stSidebarCollapsedControl"],
  [data-testid="collapsedControl"] {
      display: none !important;
  }

  /* Alineacio vertical dels botons d'accio amb la targeta A-E */
  .action-btn-wrap {
      display: flex;
      align-items: center;
      height: 100%;
      padding-top: 0.15rem;
  }
  .action-btn-wrap > div {
      width: 100%;
  }

  /* Bloc del mode commit */
  .commit-section {
      background: #fef3c7;
      border: 2px solid #fbbf24;
      border-radius: 8px;
      padding: 1rem 1.2rem;
      margin: 1rem 0;
  }
</style>
""", unsafe_allow_html=True)


# ============================================================
# CSS condicional segons ENABLE_AI
# ============================================================
# Quan AI=off, no hi ha columna de diàleg, només una columna única amb
# l'enunciat + botons. Amb `layout="wide"` aquesta columna ocuparia el
# 100% del viewport, que en pantalles grans és innecessàriament ample.
# Limitem el contenidor principal a 80% del viewport, centrat. Quan
# AI=on no toquem res perquè la distribució 7/3 ja omple bé l'amplada.
if not L.is_ai_enabled():
    st.markdown("""
<style>
  .block-container {
      max-width: 70% !important;
      margin-left: auto !important;
      margin-right: auto !important;
  }
</style>
""", unsafe_allow_html=True)


_init_state()


# ============================================================
# Helpers de presentació
# ============================================================
def _format_eliminations_card(state):
    """Tarjeta compacta amb les 5 lletres; les eliminades es tatxen.
    NO mostrem el text de les opcions perquè ja apareix a la imatge."""
    eliminated = set(state.get("eliminated_options", []))
    chips = []
    for letter in ("A", "B", "C", "D", "E"):
        cls = "label-row eliminated" if letter in eliminated else "label-row"
        chips.append(f'<span class="{cls}">{letter}</span>')
    body = "".join(chips)
    return f'<div class="opcions-card">{body}</div>'


def _format_md(text: str) -> str:
    """Conversió mínima Markdown→HTML per al render dins divs HTML."""
    import re as _re
    html = (text or "").replace("\n\n", "<br/><br/>").replace("\n", "<br/>")
    html = _re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    return html


def _render_hints_only(state):
    """Pinta NOMÉS les pistes del conversation_history (sense estat buit).

    Útil quan AI està desactivada: la columna de diàleg desapareix, però
    si l'alumne ha demanat la pista inicial del catàleg, encara cal
    mostrar-la-li en algun lloc. No es renderitza res si no hi ha pistes.
    """
    history = state.get("conversation_history", [])
    hints = [t for t in history if t.get("kind") == "hint"]
    if not hints:
        return
    for turn in hints:
        content = _format_md(turn.get("content", ""))
        source = turn.get("source", "ia")
        badge = "📘" if source == "catalog" else "💡"
        st.markdown(
            f'<div class="chat-hint"><strong>{badge}</strong><br/>{content}</div>',
            unsafe_allow_html=True,
        )


def _render_conversation(state):
    """Pinta el fil de xat amb tots els torns del conversation_history."""
    history = state.get("conversation_history", [])
    if not history:
        st.markdown(
            '<div style="text-align:center;color:#9ca3af;font-style:italic;'
            'margin:1rem 0;padding:1.5rem;border:1px dashed #e5e7eb;border-radius:8px">'
            "Encara no heu començat a dialogar."
            "</div>",
            unsafe_allow_html=True,
        )
        return
    rendered_anything = False
    for turn in history:
        role = turn.get("role")
        kind = turn.get("kind", "message")
        content = _format_md(turn.get("content", ""))
        if kind == "hint":
            source = turn.get("source", "ia")
            badge = "📘" if source == "catalog" else "💡"
            st.markdown(
                f'<div class="chat-hint"><strong>{badge}</strong><br/>{content}</div>',
                unsafe_allow_html=True,
            )
            rendered_anything = True
        elif kind == "system_event":
            # Els system_events són context intern per al LLM (commits fallits,
            # etc.); no es mostren al fil visible per evitar duplicar info que
            # ja apareix a la targeta A-E o als flash messages.
            continue
        elif role == "user":
            # Cada missatge nou de l'alumne inicia un bloc pregunta-resposta.
            # Posem un separador horitzontal per delimitar visualment del bloc
            # anterior (excepte al primer torn).
            if rendered_anything:
                st.markdown('<hr class="turn-separator"/>',
                            unsafe_allow_html=True)
            st.markdown(
                f'<div class="chat-user">{content}</div>',
                unsafe_allow_html=True,
            )
            rendered_anything = True
        else:
            st.markdown(
                f'<div class="chat-ai">{content}</div>',
                unsafe_allow_html=True,
            )
            rendered_anything = True


def _render_flash_messages(state, only_kind=None, exclude_kind=None):
    """Pinta els missatges UI transitoris (errors API, commit ok/fail).

    Si es passa `only_kind` (string o set), només es pinten els missatges
    d'aquests kinds. Si es passa `exclude_kind` (string o set), els
    missatges d'aquests kinds s'amaguen. Permet decidir des de cada
    columna quins missatges renderitzar."""
    if isinstance(only_kind, str):
        only_kind = {only_kind}
    if isinstance(exclude_kind, str):
        exclude_kind = {exclude_kind}
    for m in state.get("messages", []):
        kind = m.get("kind", "warning")
        if only_kind is not None and kind not in only_kind:
            continue
        if exclude_kind is not None and kind in exclude_kind:
            continue
        html = _format_md(m.get("text", ""))
        st.markdown(f'<div class="msg-{kind}">{html}</div>',
                    unsafe_allow_html=True)


def _render_history_expander(state):
    """Accordion amb el rastre cronològic d'events del professor."""
    history = state.get("history", [])
    if not history:
        return
    with st.expander(f"📋 Rastre d'events ({len(history)})"):
        for i, h in enumerate(history, 1):
            tipus = h.get("type", "?")
            ts = datetime.fromtimestamp(h.get("ts", 0)).strftime("%H:%M:%S")
            if tipus == "discuss":
                st.markdown(
                    f"**{i}. [{ts}] Diàleg**\n\n"
                    f"*Alumne:* {h.get('student', '')}\n\n"
                    f"*IA:* {h.get('ai_response', '')}"
                )
            elif tipus == "hint":
                src = h.get("source", "?")
                st.markdown(
                    f"**{i}. [{ts}] Pista** ({src})\n\n"
                    f"{h.get('content', '')}"
                )
            elif tipus == "commit":
                letter = h.get("letter", "?")
                ok = h.get("correct", False)
                emoji = "✅" if ok else "❌"
                st.markdown(f"**{i}. [{ts}] Commit `{letter}`** {emoji}")
            elif tipus in ("enter_commit_mode", "cancel_commit_mode"):
                st.markdown(f"**{i}. [{ts}] {tipus}**")
            st.markdown("---")


@st.cache_data(show_spinner=False)
def _load_problem_image_b64(img_path: str, mime: str,
                            crop_pct: float = 0.05) -> str:
    """Llegeix la imatge de l'enunciat i en retalla `crop_pct` a cada
    costat horitzontal abans de codificar-la en base64.

    Per que retallem: les imatges escannejades de les proves Cangur
    porten sempre marges blancs laterals que no aporten res. Si els
    treiem, com que el `<img>` ocupa el 100% de l'amplada del seu
    contenidor, el contingut util (text + opcions) queda visualment
    magnificat ~11% sense reescalat ni perdua de qualitat.

    Cachejat amb `@st.cache_data` perque el crop no s'executi a cada
    rerun de Streamlit (el resultat es el mateix per a la mateixa
    imatge en disc).
    """
    from io import BytesIO
    from PIL import Image
    import base64 as _b64

    with Image.open(img_path) as img:
        w, h = img.size
        crop_x = int(w * crop_pct)
        # crop(left, upper, right, lower)
        cropped = img.crop((crop_x, 0, w - crop_x, h))

        fmt_map = {"jpeg": "JPEG", "png": "PNG",
                   "gif": "GIF", "webp": "WEBP"}
        fmt = fmt_map.get(mime, "JPEG")

        # JPEG no admet canal alfa: convertim a RGB si cal
        if fmt == "JPEG" and cropped.mode not in ("RGB", "L"):
            cropped = cropped.convert("RGB")

        buf = BytesIO()
        if fmt == "JPEG":
            cropped.save(buf, format=fmt, quality=92, optimize=True)
        else:
            cropped.save(buf, format=fmt)
        return _b64.b64encode(buf.getvalue()).decode("ascii")


def _next_problem_id(current_pid: str):
    """Retorna l'id del problema SEGUENT dins el mateix curs i any.

    `get_available_problems()` ja ve ordenat (1ESO-01..30, 2ESO-01..30,
    ...), aixi que el seguent es l'element immediatament posterior, sempre
    que sigui del mateix curs/any. Retorna None si el problema actual es
    l'ultim del seu curs (o no es troba al cataleg)."""
    available = PB.get_available_problems()
    if current_pid not in available:
        return None
    idx = available.index(current_pid)
    if idx + 1 >= len(available):
        return None
    nxt = available[idx + 1]
    cur_p = PB.PROBLEMS[current_pid]
    nxt_p = PB.PROBLEMS[nxt]
    same_course = (
        nxt_p.get("categoria") == cur_p.get("categoria")
        and nxt_p.get("any") == cur_p.get("any")
    )
    return nxt if same_course else None


# ============================================================
# Selector de problema al main pane (en lloc del sidebar de
# Streamlit, que ara queda amagat). L'expander es replega
# automaticament quan hi ha una sessio activa per donar tot
# l'espai al panell problema + dialeg.
# ============================================================
_session_active = st.session_state.get("tutor_state") is not None

st.markdown(
    '<h2 class="app-title">🦘 Prova Cangur</h2>',
    unsafe_allow_html=True,
)

# Missatge de benvinguda: ara just sota el titol, abans del selector,
# perque sigui el primer que veu l'alumne en obrir l'app.
if not _session_active:
    st.info(
        "👋 Et donem la benvinguda a la pràctica de Prova Cangur.\n\n"
        "Tria un problema aquí sota i prem **🎯 Inicia el problema**."
    )

with st.expander("📚 Escull un problema", expanded=(not _session_active)):
    available = PB.get_available_problems()
    if not available:
        st.warning(
            "Encara no hi ha problemes poblats al catàleg. "
            "Edita `problems.py` per afegir els 30 problemes."
        )
    else:
        # Curs: ara es seleccio UNICA (abans en permetia diverses).
        curs_filter = st.pills(
            "Curs",
            options=["1ESO", "2ESO", "3ESO", "4ESO"],
            selection_mode="single",
            default="1ESO",
        )
        # Any: seleccio UNICA (mutuament excloent).
        any_filter = st.pills(
            "Any",
            options=[2024, 2025, 2026],
            selection_mode="single",
            default=2026,
        )
        # Punts: continua sent seleccio multiple.
        puntuacions_filter = st.pills(
            "Punts",
            options=[3, 4, 5],
            selection_mode="multi",
            default=[3, 4, 5],
        )
        filtered = [
            pid for pid in available
            if PB.PROBLEMS[pid].get("punts") in (puntuacions_filter or [])
            and PB.PROBLEMS[pid].get("categoria") == curs_filter
            and PB.PROBLEMS[pid].get("any") == any_filter
        ]

        if not filtered:
            st.info("No hi ha cap problema amb els filtres seleccionats.")
        else:
            def _format_option(pid):
                p = PB.PROBLEMS[pid]
                tema = p.get("tema") or "—"
                # Treure prefix "CAN-"; el curs/any/número queda visible
                display_id = pid.removeprefix("CAN-")
                return f"{display_id} · {tema}"

            selected_pid = st.selectbox(
                "Problema",
                options=filtered,
                format_func=_format_option,
                key="problem_selector",
            )
            # Boto d'inici, just sota el desplegable de problema.
            if st.button("🎯 Inicia el problema", key="start_btn",
                         use_container_width=True):
                try:
                    st.session_state.tutor_state = T.new_session_state(selected_pid)
                    st.session_state.input_counter = 0
                    st.rerun()
                except Exception as e:
                    st.error(f"Error iniciant: {e}")

    # Cost API + mode d'engatgament (només en mode debug)
    if _is_debug_mode():
        st.divider()
        st.caption("**Mode debug actiu**")
        _ai_on = L.is_ai_enabled()
        _ai_badge = "🟢 ENABLE_AI=1" if _ai_on else "🔴 ENABLE_AI=0 (default)"
        st.caption(f"Estat IA: {_ai_badge}")
        st.caption(f"Motor: `{L.PROVIDER}` / `{L.MODEL}`")
        sid = L.get_session_id()
        cost = api_logger.summarize_session(sid)
        _col_cost, _col_calls = st.columns(2)
        _col_cost.metric("Cost USD", f"${cost['cost_usd']:.4f}")
        _col_calls.metric("Crides", f"{cost['calls_ok']}/{cost['calls_total']}")

        # Mode d'engatgament del problema actual (classificació feta
        # per la IA torn a torn). Útil per veure en temps real si la
        # IA està detectant bé S vs D durant el pilot.
        _curr_state = st.session_state.get("tutor_state")
        if _curr_state is not None:
            _mode_now = T.current_engagement_mode(_curr_state)
            _n_s = sum(
                1 for t in _curr_state.get("conversation_history", [])
                if t.get("role") == "assistant" and t.get("mode") == "S"
            )
            _n_d = sum(
                1 for t in _curr_state.get("conversation_history", [])
                if t.get("role") == "assistant" and t.get("mode") == "D"
            )
            _label = {"S": "🟢 SITUAT", "D": "🟡 DIVAGANT",
                      None: "— (encara cap torn)"}[_mode_now]
            st.caption(f"**Mode actual:** {_label}")
            st.caption(f"Torns S/D acumulats: {_n_s} / {_n_d}")

        # ---- Selector de motor IA ----
        st.divider()
        with st.expander("⚙️ Motor IA", expanded=True):
            _PROVIDERS = ["gemini", "claude"]
            _GEMINI_MODELS = [
                "gemini-2.5-flash",
                "gemini-2.5-pro",
                "gemini-2.0-flash",
                "gemini-1.5-flash",
            ]
            _CLAUDE_MODELS = [
                "claude-sonnet-4-5",
                "claude-opus-4-5",
                "claude-haiku-4-5",
            ]
            _prov_now = L.PROVIDER
            _prov_sel = st.selectbox(
                "Proveïdor",
                _PROVIDERS,
                index=_PROVIDERS.index(_prov_now) if _prov_now in _PROVIDERS else 0,
                key="dbg_provider",
            )
            _model_list = _CLAUDE_MODELS if _prov_sel == "claude" else _GEMINI_MODELS
            _model_now = L.MODEL if L.MODEL in _model_list else _model_list[0]
            _model_sel = st.selectbox(
                "Model",
                _model_list,
                index=_model_list.index(_model_now),
                key="dbg_model",
            )
            with st.expander("🔑 Claus API (opcional)", expanded=False):
                _gemini_key_in = st.text_input(
                    "GEMINI_API_KEY", type="password",
                    placeholder="deixa buit per usar la del secret",
                    key="dbg_gemini_key",
                )
                _claude_key_in = st.text_input(
                    "ANTHROPIC_API_KEY", type="password",
                    placeholder="deixa buit per usar la del secret",
                    key="dbg_claude_key",
                )
            if st.button("Aplicar motor", key="dbg_apply_engine"):
                L.set_debug_config(
                    provider=_prov_sel,
                    model=_model_sel,
                    gemini_key=_gemini_key_in or None,
                    claude_key=_claude_key_in or None,
                )
                st.success(f"Motor canviat → {_prov_sel} / {_model_sel}")
                st.rerun()


# ============================================================
# Main pane: la sessió actual
# ============================================================
state = st.session_state.tutor_state

if state is not None:
    # Re-aplicar el context de log defensivament (els reruns de Streamlit
    # poden fer que es perdi).
    L.set_log_context(student_id=state.get("student_id"),
                      session_id=state["session_id"])

    problem = state["problem"]
    _mode = state.get("mode", "reasoning")
    _verdict = state.get("verdict_final")

    # ========================================================
    # LAYOUT: si la IA està activa, dues columnes (problema sticky +
    # diàleg amb scroll). Si la IA està desactivada, una sola columna
    # a tota l'amplada (no hi ha res a dialogar, no té sentit la
    # columna dreta).
    # ========================================================
    _ai_on = L.is_ai_enabled()
    if _ai_on:
        col_problem, col_dialeg = st.columns([7, 3], gap="medium")
    else:
        # Contenidor full-width. El CSS sticky de `.st-key-problem_panel`
        # només s'activa quan està dins d'un `stColumn`; aquí no s'aplica,
        # cosa coherent (en single-column no té sentit fer res sticky).
        col_problem = st.container()
        col_dialeg = None

    # --------------------------------------------------------
    # Panell ESQUERRE: enunciat + opcions A-E + botons d'accio
    # --------------------------------------------------------
    with col_problem:
        with st.container(key="problem_panel"):
            # Capcalera del problema
            _categoria = problem.get("categoria", "?")
            _any = problem.get("any", "?")
            _numero = problem.get("numero", "?")
            _tema_raw = problem.get("tema") or "tema no especificat"
            _tema = _tema_raw[:1].upper() + _tema_raw[1:]
            st.markdown(
                f'<h3 class="problem-title">{_categoria} ({_any}) '
                f'Q{_numero} · {_tema}</h3>',
                unsafe_allow_html=True,
            )

            # Imatge
            imatge = problem.get("imatge")
            if imatge:
                base_dir = os.path.dirname(os.path.abspath(__file__))
                img_path = os.path.join(base_dir, "data", imatge)
                if os.path.exists(img_path):
                    _ext = os.path.splitext(imatge)[1].lower().lstrip(".")
                    _mime = {"jpg": "jpeg", "jpeg": "jpeg",
                             "png": "png", "gif": "gif",
                             "webp": "webp"}.get(_ext, "jpeg")
                    _img_b64 = _load_problem_image_b64(img_path, _mime)
                    st.markdown(
                        f'<div class="header-image"><img '
                        f'src="data:image/{_mime};base64,{_img_b64}" '
                        f'alt="Enunciat del problema"/></div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.warning(f"⚠️ Imatge no trobada: `{img_path}`.")
            elif problem.get("enunciat"):
                st.markdown(problem["enunciat"])

            # Targeta A-E (sempre visible, excepte en mode commit que els
            # 5 botons grans ja fan aquesta funcio)
            if _mode != "committing":
                st.markdown(_format_eliminations_card(state),
                            unsafe_allow_html=True)

            # Botons d'accio segons el mode
            if _verdict is None and _mode == "reasoning":
                # Determina si la propera pista requeriria una crida IA
                # (només la 1a pista pot venir del catàleg). Si la IA
                # està desactivada i la propera pista necessitaria IA,
                # amaguem el botó.
                _pistes_count = state.get("pistes_count", 0)
                _has_initial_hint = bool(state["problem"].get("pista_inicial"))
                _next_hint_uses_ai = not (_pistes_count == 0 and _has_initial_hint)
                _can_request_hint = L.is_ai_enabled() or not _next_hint_uses_ai

                _col_hint, _col_commit = st.columns(2)
                with _col_hint:
                    if _can_request_hint:
                        if st.button("Vull una pista", key="request_hint",
                                     use_container_width=True):
                            if not _next_hint_uses_ai:
                                st.session_state.tutor_state = T.request_hint(state)
                            else:
                                with st.spinner("S'està generant una pista..."):
                                    st.session_state.tutor_state = T.request_hint(state)
                            st.rerun()
                with _col_commit:
                    if st.button("Ja tinc la resposta", key="enter_commit",
                                 use_container_width=True):
                        st.session_state.tutor_state = T.request_commit_mode(state)
                        st.rerun()

            # MODE COMMIT: 5 botons A-E al panell del problema. Ocupen
            # aproximadament el mateix espai que la targeta A-E original
            # (botons petits a l'esquerra; spacer a la dreta perque no
            # s'expandeixin). El bloc està marcat amb la classe
            # `.commit-mode-buttons` perquè el CSS els pugui pintar de
            # blau-suau amb hover blau-fort, com la resta de botons.
            elif _verdict is None and _mode == "committing":
                st.markdown("**Escull l'opci\u00f3 que creus correcta:**")
                _eliminated = set(state.get("eliminated_options", []))
                # Cinc botons petits (1/15 d'amplada cadascun) + spacer 10
                _cols = st.columns([1, 1, 1, 1, 1, 10])
                for _i, _letter in enumerate(("A", "B", "C", "D", "E")):
                    with _cols[_i]:
                        if st.button(
                            _letter, key=f"commit_{_letter}",
                            disabled=(_letter in _eliminated),
                            use_container_width=True,
                        ):
                            st.session_state.tutor_state = T.process_commit(
                                state, _letter)
                            st.rerun()
                # Botó "Tornar a raonar" amb amplada limitada (no
                # `use_container_width`, ja que el CSS controlarà la mida).
                if st.button("\u2190 Tornar a raonar", key="cancel_commit"):
                    st.session_state.tutor_state = T.cancel_commit_mode(state)
                    st.rerun()

            # PROBLEMA ACABAT: drecera per passar directament al seguent
            # problema del mateix curs (l'alumne que acaba el 11 normalment
            # voldra el 12). Si ja era l'ultim del curs, no es mostra res.
            elif _verdict is not None:
                # Excepcionalment, el missatge "Correcte!" es renderitza
                # aquí (col_problem) en comptes de la columna del diàleg,
                # perquè quedi just abans del botó "Inicia el problema
                # següent". Així l'alumne veu el feliçitació i el botó
                # d'acció seguits, en lloc d'haver de canviar de columna.
                _render_flash_messages(state, only_kind="commit_ok")
                _next_pid = _next_problem_id(state["problem"]["id"])
                if _next_pid is not None:
                    if st.button(
                        "\u23e9\ufe0e Inicia el problema següent",
                        key="start_next",
                        use_container_width=True,
                        help=f"Comen\u00e7ar {_next_pid.removeprefix('CAN-')}",
                    ):
                        try:
                            st.session_state.tutor_state = T.new_session_state(
                                _next_pid)
                            st.session_state.input_counter = 0
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error iniciant: {e}")

    # --------------------------------------------------------
    # Panell DRET (només si AI activa): dialeg + missatges flash + input
    # --------------------------------------------------------
    if col_dialeg is not None:
        with col_dialeg:
            with st.container(key="dialogue_panel"):
                # Fil de xat
                st.markdown('<h4 class="dialeg-title">Di\u00e0leg</h4>',
                            unsafe_allow_html=True)
                _render_conversation(state)

                # Missatges flash (errors API, commits fallits, etc.).
                # NOTA: el `commit_ok` es renderitza específicament a
                # col_problem (just abans del botó "Inicia el problema
                # següent"), de manera que aquí l'excloem per evitar
                # duplicar-lo a les dues columnes.
                _render_flash_messages(state, exclude_kind="commit_ok")

                # Si la sessio ha acabat, mostrar resum final i amagar inputs.
                if _verdict is not None:
                    st.divider()
                    with st.expander("📄 Veure el rastre JSON de la sessió"):
                        trace = T.build_trace(state)
                        st.json(trace)
                        st.download_button(
                            "⬇ Descarregar rastre JSON",
                            data=T.serialize_trace(state),
                            file_name=f"trace_{state['session_id']}.json",
                            mime="application/json",
                        )
                elif _mode == "reasoning":
                    # Sessio en curs mode dialeg: text area + boto enviar.
                    # Fem servir un st.form perque Ctrl+Enter dins el camp de
                    # text faci el mateix que clicar "Enviar missatge".
                    # `clear_on_submit` buida el camp despres d'enviar (abans
                    # ho feiem amb una `key` dinamica i `input_counter`).
                    st.divider()
                    with st.form("message_form", clear_on_submit=True,
                                 border=False):
                        student_text = st.text_area(
                            "El teu missatge",
                            key="message_input",
                            height=110,
                            label_visibility="hidden",
                            placeholder="Escriu aquí la teva frase",
                        )
                        _submitted = st.form_submit_button(
                            "Enviar missatge", use_container_width=True)
                    if _submitted:
                        with st.spinner("Un moment, si us plau..."):
                            st.session_state.tutor_state = T.process_message(
                                state, student_text)
                        st.rerun()
    else:
        # AI OFF: la columna de diàleg desapareix totalment (sense títol
        # "Diàleg", sense missatge d'estat buit, sense info banner). Però
        # cal mantenir tres coses funcionals, que aquí renderitzem just
        # sota el panell del problema, a tota l'amplada:
        #   1) La pista inicial del catàleg si l'alumne l'ha demanada.
        #   2) Els missatges flash transitoris (p.ex. commit_fail). El
        #      `commit_ok` s'amaga perquè ja es pinta dins col_problem.
        #   3) En acabar la sessió, l'expander amb el rastre JSON
        #      descarregable.
        _render_hints_only(state)
        _render_flash_messages(state, exclude_kind="commit_ok")
        if _verdict is not None:
            st.divider()
            with st.expander("📄 Veure el rastre JSON de la sessió"):
                trace = T.build_trace(state)
                st.json(trace)
                st.download_button(
                    "⬇ Descarregar rastre JSON",
                    data=T.serialize_trace(state),
                    file_name=f"trace_{state['session_id']}.json",
                    mime="application/json",
                )

    # --------------------------------------------------------
    # Rastre cronologic + estat intern (fora de les columnes,
    # a tota l'amplada inferior). Nomes son visibles si l'usuari
    # ha fet prou scroll, aixi que es queden al peu i no
    # interfereixen amb el flux principal.
    # --------------------------------------------------------
    st.divider()
    _render_history_expander(state)

    if _is_debug_mode():
        with st.expander("🔍 Estat intern (debug)"):
            debug_state = {k: v for k, v in state.items() if k != "problem"}
            debug_state["problem_id_only"] = state["problem"]["id"]
            st.json(debug_state)
