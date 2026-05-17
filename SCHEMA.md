# SCHEMA.md — Estructures de dades: Tutor Cangur 1r ESO

Aquest document descriu el contracte de dades de tot el sistema. És el
punt de referència únic per a qualsevol edició de `problems.py` i per
entendre els missatges del rastre JSON.

Tots els camps amb text visible per a l'alumne (enunciat, opcions...)
són **strings monolingües en català**.

---

## PROBLEMS

Cada entrada de `PROBLEMS` té:

```python
{
    # Identificació
    "id":                   str,    # "CAN-1ESO-2026-03"
    "categoria":            str,    # "1ESO"
    "any":                  int,    # any de la prova original (2026, 2025...)
    "numero":               int,    # posició a la prova (1..30)
    "punts":                int,    # 3 | 4 | 5

    # Classificació pedagògica
    "tema":                 str | None,  # "aritmètica" | "geometria" | "comptatge"
                                         # | "lògica" | "divisibilitat" | ...

    # Contingut visible per a l'alumne (UN dels dos; imatge té prioritat)
    "imatge":               str | None,  # nom de fitxer a data/
                                         # (p.ex. "CAN-1ESO-2026-01.jpg")
    "enunciat":             str | None,  # text pla (alternativa quan no hi ha imatge)
    "opcions":              dict,        # {"A": str|None, ..., "E": str|None}
                                         # valors poden ser None quan hi ha imatge
    "resposta_correcta":    str,         # una lletra "A" | "B" | "C" | "D" | "E"

    # Contingut NO visible per a l'alumne (només per a la IA)
    "pista_inicial":          str | None,  # 1a pista del catàleg pre-escrita
    "expected_reasoning":     str | None,  # solució desenvolupada
    "comentaris_distractors": dict,        # {"A": "per què algú trià A", ...}
                                           # claus = totes les lletres EXCEPTE
                                           # la correcta
    "errors_típics":          list,        # ["GEO_perimetre_vs_area", ...]
                                           # claus d'ERROR_CATALOG
    "dependencies":           list,        # ids de conceptes prerequisit (no usat al MVP)
}
```

### Camps obligatoris vs opcionals

| Camp | Obligatori? | Si manca... |
|---|---|---|
| `id`, `categoria`, `any`, `numero`, `punts` | ✅ Sí | Excepció a `_validate_catalog` o problema invisible |
| `imatge` o `enunciat` | ✅ Sí (un dels dos) | Problema invisible a la UI si cap dels dos existeix |
| `opcions` (5 claus A-E) | ✅ Sí | Problema invisible; valors poden ser None si hi ha `imatge` |
| `resposta_correcta` | ✅ Sí | Problema invisible a la UI |
| `tema` | ⚠️ Recomanat | Apareix com "tema no especificat" a la UI |
| `pista_inicial` | 🟡 Opcional | La 1a pista que demani l'alumne ja la genera la IA |
| `expected_reasoning` | 🟡 Opcional | La IA llegeix la imatge i raona pel seu compte (risc en problemes amb truc). **Recomanable poblar-lo per a problemes que han mostrat baix èxit al pilot.** |
| `comentaris_distractors` | 🟡 Opcional | La IA no té context sobre per què algú podria triar cada distractor; les preguntes post-error tindran qualitat més baixa |
| `errors_típics` | 🟡 Opcional | No es fa servir al codi viu del MVP; reservat per a Fase 2 |
| `dependencies` | 🟡 Opcional | Reservat per al retrocés a prereqs (no actiu al MVP) |

### Plantilla per omplir un problema (com els 30 actuals)

```python
# — Forma A: contingut com a imatge (cas habitual al Cangur) —
PROBLEMS["CAN-1ESO-2026-XX"] = {
    "id":         "CAN-1ESO-2026-XX",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     XX,
    "punts":      3,                # o 4 o 5
    "tema":       "...",            # "aritmètica" | "geometria" | ...
    "imatge":     "CAN-1ESO-2026-XX.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta": "X",

    # Opcionals (afegir a mesura que es prepara material):
    "pista_inicial":          None,   # str amb 1a pista; None → 1a pista la genera IA
    "expected_reasoning":     None,
    "comentaris_distractors": {},
    "errors_típics":          [],
    "dependencies":           [],
}
```

---

## ERROR_CATALOG

```python
{
    error_label: str,   # "Descripció en català del patró d'error"
}
```

El `error_label` segueix el prefix per famílies temàtiques:
- `ARI_*`  — errors aritmètics (càlcul, ordre operacions)
- `GEO_*`  — errors geomètrics
- `COMP_*` — errors de comptatge/combinatòria simple
- `LOG_*`  — errors de lògica/interpretació de l'enunciat
- `GEN_*`  — errors genèrics

Avui poblat mínimament. S'amplia quan documentes errors típics als problemes.

---

## Estat de sessió (`tutor.py`)

```python
{
    # --- Identificació ---
    "session_id":             str,        # 12 hex chars, generats al new_session_state
    "student_id":             None,       # sempre None: sessió anònima
    "problem_id":             str,
    "problem":                dict,       # còpia del problema
    "started_at":             str,        # ISO 8601
    "started_at_ts":          float,      # epoch seconds

    # --- Mode i progrés del problema ---
    "mode":                   str,        # "reasoning" | "committing"
    "eliminated_options":     list,       # ["A", "D"] lletres ja descartades per commit fallit
    "commit_letter":          str | None, # lletra final si solved
    "commit_attempts":        list,       # cronològic: ["A", "D", "C"]

    # --- Conversa amb la IA ---
    "conversation_history":   list,       # vegeu sub-secció més avall
    "pistes_count":           int,        # nº total de pistes donades en aquest problema

    # --- Veredicte final ---
    "verdict_final":          str | None, # None | "solved"

    # --- UI transitòria i rastre ---
    "messages":               list,       # missatges flash UI (no part del diàleg)
    "history":                list,       # cronològic complet per al rastre JSON
}
```

### `conversation_history`

Llista de torns; cada torn és:

```python
{
    "role":    "user" | "assistant",
    "kind":    "message" | "hint" | "system_event",
    "content": str,
    "ts":      float,
    # opcional, només si kind == "hint":
    "source":  "catalog" | "ia",
}
```

#### Kinds

- **`message`**: torn de diàleg normal. `role="user"` és l'alumne, `role="assistant"` és la IA.
- **`hint`**: pista. Sempre `role="assistant"`. El `source` indica si ve del catàleg
  (`pista_inicial`, cost API = 0) o de la IA on-demand (`generate_hint`).
- **`system_event`**: informació externa que la IA ha de tenir en compte. `role="user"`
  per coherència del multi-torn de Gemini (alterna user/model). Avui s'emet quan un
  commit falla (perquè la IA pugui respondre a "per què la X no era correcta?").

#### Marcadors al multi-torn

Quan `llm.py` munta els `contents` per a Gemini, prefixa els kinds especials:
- `kind="hint"` → `[PISTA] ...`
- `kind="system_event"` → `[Sistema] ...`

El system prompt explica a la IA com interpretar aquests marcadors.

### Veredictes finals

| Valor | Significat |
|---|---|
| `None`     | sessió en curs |
| `"solved"` | l'alumne ha encertat la lletra (commit correcte) |

**Important: no existeix `"suspended"` ni `"failed"`.** Decisió de disseny:
- Sense límit de commits (l'alumne pot insistir tants cops com vulgui).
- Sense filtre determinista d'ús inadequat (la IA ja gestiona els "hola" amablement).

---

## Funcions de la IA (`llm.py`)

### `discuss(problem, image_path, conversation, student_text) -> str`

Torn de diàleg socràtic. Multimodal:
- `problem`: dict amb `resposta_correcta`, `expected_reasoning`, `comentaris_distractors`.
  La IA usa la `resposta_correcta` per ancorar-se i `expected_reasoning` + comentaris
  com a context (si estan poblats).
- `image_path`: path absolut al JPG (resolució via `tutor._image_path_for`).
- `conversation`: llista de torns previs SENSE el missatge nou.
- `student_text`: missatge nou que l'alumne acaba d'escriure.

Retorna: text de resposta de la IA (1-3 frases en català). Si la IA creu que l'alumne
està en condicions de comprometre's, ho diu **dins el text mateix** (no com a
metadada).

### `generate_hint(problem, image_path, conversation) -> str`

Pista on-demand. Es crida NOMÉS quan `pistes_count > 0` (la 1a pista, si existeix
`pista_inicial`, ve del catàleg sense crida API).

Veu el multi-torn complet. Les pistes prèvies (catàleg o IA) viuen com a torns
`kind="hint"` al `conversation_history`, prefixades amb `[PISTA] ` al prompt.
Així la IA no les repeteix i gradua la duresa automàticament.

Retorna text pla (1-2 frases).

---

## Truncament defensiu de la conversa

Si `conversation_history` supera **20 torns**, es manté:
- Els **3 primers** torns (context inicial de la sessió)
- Els **10 últims** torns (estat actual del diàleg)

Es perden els torns intermedis. Per a problemes Cangur típics (5-15 torns), no
s'activa mai.

Configurable a `llm.py`:
```python
TRUNCATE_THRESHOLD = 20
TRUNCATE_KEEP_FIRST = 3
TRUNCATE_KEEP_LAST = 10
```

---

## Rastre JSON per al professor

Generat per `tutor.build_trace(state)`:

```python
{
    "session_id":           str,
    "problema": {
        "id":                str,
        "categoria":         str,
        "any":               int,
        "numero":            int,
        "punts":             int,
        "tema":              str | None,
        "imatge":            str | None,
        "resposta_correcta": str,
    },
    "started_at":           str,
    "durada_segons":        float,

    # Diàleg
    "n_dialeg_turns":       int,   # torns user de tipus "message"
    "conversation_history": list,  # íntegra (incloent pistes i system_events)

    # Pistes
    "n_pistes_total":       int,
    "n_pistes_catalog":     int,   # del catàleg (cost API = 0)
    "n_pistes_ia":          int,   # generades on-demand

    # Commits
    "commit_attempts":      list,  # cronològic
    "n_commits":            int,
    "eliminated_options":   list,
    "commit_letter_final":  str | None,

    # Rastre cronològic d'events
    "torns":                list,

    # Veredicte
    "veredicte_final":      str,   # "solved" | "en_curs"
}
```

### Mètriques útils per al pilot

- `n_commits == 1` i `veredicte_final == "solved"` → autonomia màxima.
- `n_commits > 3` → probable necessitat de més suport humà.
- `n_dialeg_turns / n_commits` alt → bon diàleg socràtic abans del commit.
- `n_pistes_total` alt → l'alumne s'estanca; pot indicar conceptes
  prerequisit dèbils o enunciat amb truc.
- Ràtio `n_pistes_catalog / n_pistes_total` baixa → val la pena poblar
  més `pista_inicial` al catàleg.
