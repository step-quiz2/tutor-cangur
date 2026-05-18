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
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
  .block-container { padding-top: 2rem !important; font-size: 1.05rem; }
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

  /* HEADER FIXAT amb imatge + fila A-E/botons.
     ----------------------------------------------------
     Implementació basada en el patró del gist mantingut per la comunitat
     Streamlit: https://gist.github.com/toolittlecakes/cf1a5d734cbf5b0b2581c28b2530fec2
     ----------------------------------------------------
     Idea clau: en lloc de hardcodejar `left/right` (que falla perquè depèn
     de l'estat del sidebar i de l'amplada del contingut), apuntem al
     `stVerticalBlockBorderWrapper` que envolta el container amb la clau
     `problem_header` i li apliquem `position: fixed` amb `width: inherit`.
     Així el header hereta l'amplada del seu pare natural en el DOM de
     Streamlit i queda automàticament alineat amb la zona de contingut,
     respectant el sidebar sense haver de detectar-ne l'estat. */
  div[data-testid="stVerticalBlockBorderWrapper"]:has(> div[data-testid="stVerticalBlock"] > .st-key-problem_header) {
      position: fixed;
      top: 3rem;
      width: inherit;
      background-color: #ffffff;
      padding: 0.5rem 0.5rem 0.75rem 0.5rem;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      z-index: 99;
      max-height: 40vh;
      overflow: hidden;
      box-sizing: border-box;
  }
  /* Espai extra (~3×) entre el "Escull un problema" del sidebar/expander
     i el títol del header. */
  .st-key-problem_header h3 {
      margin-top: 1.6rem !important;
      margin-bottom: 0.5rem !important;
  }
  /* Imatge dins el header: respecta proporcions naturals, limitada en
     alçada, mai retallada (object-fit: contain). El margin-bottom 1rem
     dona ~3× del default per separar bé la imatge de la fila A-E. */
  .st-key-problem_header .header-image {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      margin-bottom: 1rem;
  }
  .st-key-problem_header .header-image img {
      max-height: 18vh;
      max-width: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
      display: block;
  }
  /* Placeholder al flux normal: reserva l'alçada total que el header
     fixat ocupa al viewport perquè el contingut posterior (diàleg, input)
     no quedi tapat. Ajustat per acomodar títol + imatge + fila d'accions. */
  .problem-header-placeholder {
      height: 40vh;
      width: 100%;
  }

  /* Missatges flash (errors tècnics, commits) */
  .msg-warning      { border-left: 4px solid #ef4444; padding: 0.4rem 0.8rem; background: #fef2f2; margin: 0.3rem 0; }
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
  /* Hover sobre la targeta A-E (no clicable): mostrar cursor de
     prohibit per recordar a l'alumne que aquí no es contesta. */
  .opcions-card .label-row:hover {
      cursor: not-allowed;
  }

  /* Espai extra entre el selector de problema (al sidebar o un
     expander superior) i el títol del header. Triple del default. */
  .st-key-problem_header h3 {
      margin-top: 2.4rem !important;
      margin-bottom: 0.4rem !important;
  }

  /* Espai vertical extra entre la fila A-E i tot el que es trobi
     en columnes a la mateixa fila (botons d'accions). En realitat
     volem augmentar la separació horitzontal entre la columna A-E
     i la primera columna de botons; ho fem amb columns([5,1,2,2])
     al codi Python, però aquesta classe afegeix una mica de padding
     a la cantonada dreta de la targeta A-E per donar més aire. */
  .opcions-card {
      margin-right: 0.5rem;
  }

  /* Tags del multiselect (3p, 4p, 5p) en gris en lloc de vermell */
  [data-testid="stMultiSelect"] [data-baseweb="tag"] {
      background-color: #6b7280 !important;
  }

  /* Botons d'accio "Vull una pista" i "Ja tinc la resposta".
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

  /* Input del diàleg: fons blau-suau, border negre clar, placeholder
     en cursiva. */
  .st-key-message_input_0 textarea,
  div[class*="st-key-message_input_"] textarea {
      background-color: #dbeafe !important;
      border: 1px solid #1f2937 !important;
      color: #1f2937 !important;
  }
  div[class*="st-key-message_input_"] textarea::placeholder {
      font-style: italic;
      color: #6b7280 !important;
      opacity: 1;
  }

  /* Botó "Enviar missatge": blau-suau (mateix to que l'input),
     hover més fort amb border negre 2px (com els altres botons). */
  .st-key-send_message button {
      background-color: #dbeafe !important;
      border: 1px solid #dbeafe !important;
      color: #1a1a1a !important;
      transition: background-color 0.15s, border-color 0.15s, border-width 0.15s;
  }
  .st-key-send_message button:hover {
      background-color: #60a5fa !important;
      border: 2px solid #000 !important;
      color: #000 !important;
  }

  /* Amplada del sidebar reduïda un 15% (default ~336px → ~286px) */
  [data-testid="stSidebar"] {
      min-width: 286px !important;
      max-width: 286px !important;
  }
  [data-testid="stSidebar"] > div:first-child {
      width: 286px !important;
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


def _render_flash_messages(state):
    """Pinta els missatges UI transitoris (errors API, commit ok/fail)."""
    for m in state.get("messages", []):
        kind = m.get("kind", "warning")
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


# ============================================================
# Sidebar: selector de problema
# ============================================================
with st.sidebar:
    st.title("🦘 Prova Cangur")

    available = PB.get_available_problems()
    if not available:
        st.warning(
            "Encara no hi ha problemes poblats al catàleg. "
            "Edita `problems.py` per afegir els 30 problemes."
        )
    else:
        # Si ja hi ha una sessió activa, replega els filtres dins un expander
        # tancat per defecte. Sense sessió activa, els mostra desplegats per
        # facilitar la primera tria. El selectbox "Problema" i el botó d'iniciar
        # queden sempre visibles a fora.
        _session_active = "tutor_state" in st.session_state
        if _session_active:
            _filter_container = st.expander("Filtres", expanded=False)
        else:
            st.subheader("Filtres")
            _filter_container = st.container()
        with _filter_container:
            curs_filter = st.multiselect(
                "Curs",
                options=["1ESO", "2ESO", "3ESO", "4ESO"],
                default=["1ESO", "2ESO", "3ESO", "4ESO"],
                help="Filtra per curs (1r, 2n, 3r o 4t d'ESO).",
            )
            puntuacions_filter = st.multiselect(
                "Punts",
                options=[3, 4, 5],
                default=[3, 4, 5],
                help="3 punts (fàcils), 4 punts (mitjans), 5 punts (difícils).",
            )
        filtered = [
            pid for pid in available
            if PB.PROBLEMS[pid].get("punts") in puntuacions_filter
            and PB.PROBLEMS[pid].get("categoria") in curs_filter
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

            if st.button("▶ Iniciar problema", key="start_btn",
                         use_container_width=True):
                try:
                    st.session_state.tutor_state = T.new_session_state(selected_pid)
                    st.session_state.input_counter = 0
                    st.rerun()
                except Exception as e:
                    st.error(f"Error iniciant: {e}")

    # Cost API (només en mode debug)
    if _is_debug_mode():
        st.divider()
        st.caption("**Mode debug actiu**")
        st.caption(f"Model: `{L.MODEL}`")
        sid = L.get_session_id()
        cost = api_logger.summarize_session(sid)
        col1, col2 = st.columns(2)
        col1.metric("Cost USD", f"${cost['cost_usd']:.4f}")
        col2.metric("Crides", f"{cost['calls_ok']}/{cost['calls_total']}")


# ============================================================
# Main pane: la sessió actual
# ============================================================
state = st.session_state.tutor_state

if state is None:
    st.info(
        "👋 Et donem la benvinguda a la pràctica de Prova Cangur.\n\n"
        "Selecciona un problema al panell esquerre i prem **▶ Iniciar problema**."
    )
else:
    # Re-aplicar el context de log defensivament (els reruns de Streamlit
    # poden fer que es perdi).
    L.set_log_context(student_id=state.get("student_id"),
                      session_id=state["session_id"])

    problem = state["problem"]

    # Capçalera del problema
    _categoria = problem.get("categoria", "?")
    _any = problem.get("any", "?")
    _numero = problem.get("numero", "?")
    _punts = problem.get("punts", "?")
    _tema_raw = problem.get("tema") or "tema no especificat"
    _tema = _tema_raw[:1].upper() + _tema_raw[1:]

    # Mode actual (per saber si renderitzar la fila d'accions o no dins
    # del header fixat)
    _mode = state.get("mode", "reasoning")
    _verdict = state.get("verdict_final")

    # HEADER FIXAT: títol + imatge + fila A-E/botons. Tot dins d'un
    # st.container amb key, perquè Streamlit hi posa la classe
    # .st-key-problem_header al DOM i el CSS la fa position:fixed. Així
    # tot el bloc d'identificació + control queda sempre visible.
    imatge = problem.get("imatge")
    with st.container(key="problem_header"):
        # Títol del problema
        st.markdown(
            f"### {_categoria}-{_any}. Pregunta {_numero} ({_punts} punts) · {_tema}"
        )
        # Imatge
        if imatge:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(base_dir, "data", imatge)
            if os.path.exists(img_path):
                import base64 as _b64
                with open(img_path, "rb") as _fh:
                    _img_b64 = _b64.b64encode(_fh.read()).decode("ascii")
                _ext = os.path.splitext(imatge)[1].lower().lstrip(".")
                _mime = {"jpg": "jpeg", "jpeg": "jpeg",
                         "png": "png", "gif": "gif", "webp": "webp"}.get(_ext, "jpeg")
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

        # Fila A-E + botons d'acció. En mode "reasoning" mostrem la
        # targeta A-E (no clicable) + botons "Vull una pista" i "Ja
        # tinc la resposta". En mode "committing" la targeta es
        # transforma en 5 botons A-E clicables al mateix lloc, i els
        # botons d'acció es reemplacen per un botó "Cancel·lar".
        if _verdict is None and _mode == "reasoning":
            _col_ae, _spacer, _col_hint, _col_commit = st.columns([5, 1, 2, 2])
            with _col_ae:
                st.markdown(_format_eliminations_card(state),
                            unsafe_allow_html=True)
            with _col_hint:
                if st.button("Vull una pista", key="request_hint",
                             use_container_width=True):
                    pistes_count = state.get("pistes_count", 0)
                    has_initial = bool(state["problem"].get("pista_inicial"))
                    uses_catalog = (pistes_count == 0 and has_initial)
                    if uses_catalog:
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
        elif _verdict is None and _mode == "committing":
            # MODE COMMIT: 5 botons A-E clicables al mateix lloc on hi
            # havia la targeta no clicable. Espacer + botó de cancel·lar
            # ocupen la mateixa estructura horitzontal que les accions.
            _eliminated = set(state.get("eliminated_options", []))
            _col_ae_btns, _spacer, _col_cancel = st.columns([5, 1, 4])
            with _col_ae_btns:
                _btn_cols = st.columns(5)
                for _i, _letter in enumerate(("A", "B", "C", "D", "E")):
                    with _btn_cols[_i]:
                        if st.button(
                            _letter, key=f"commit_{_letter}",
                            disabled=(_letter in _eliminated),
                            use_container_width=True,
                        ):
                            st.session_state.tutor_state = T.process_commit(
                                state, _letter)
                            st.rerun()
            with _col_cancel:
                if st.button("← Tornar a raonar", key="cancel_commit",
                             use_container_width=True):
                    st.session_state.tutor_state = T.cancel_commit_mode(state)
                    st.rerun()
        else:
            # Sessio acabada: només la targeta A-E (mostra estat final).
            st.markdown(_format_eliminations_card(state),
                        unsafe_allow_html=True)

    # Placeholder al flux normal: reserva l'espai vertical que ocupa
    # el header fixat, perquè el contingut posterior (diàleg, input,
    # etc.) no quedi tapat per sota.
    st.markdown(
        '<div class="problem-header-placeholder"></div>',
        unsafe_allow_html=True,
    )

    # Fil de xat
    st.markdown("#### Di\u00e0leg")
    _render_conversation(state)

    # Missatges flash (errors API, commits)
    _render_flash_messages(state)

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
        # Sessio en curs mode dialeg: text area + boto enviar
        st.divider()
        input_key = f"message_input_{st.session_state.input_counter}"
        student_text = st.text_area(
            "El teu missatge",
            key=input_key,
            height=110,
            label_visibility="hidden",
            placeholder="Escriu aquí la teva frase",
        )
        if st.button("Enviar missatge", key="send_message", use_container_width=True):
            with st.spinner("Un moment, si us plau..."):
                st.session_state.tutor_state = T.process_message(state, student_text)
            st.session_state.input_counter += 1
            st.rerun()

    # Rastre cronològic + estat intern (només debug)
    st.divider()
    _render_history_expander(state)

    if _is_debug_mode():
        with st.expander("🔍 Estat intern (debug)"):
            debug_state = {k: v for k, v in state.items() if k != "problem"}
            debug_state["problem_id_only"] = state["problem"]["id"]
            st.json(debug_state)
