# Tutor Cangur 1r ESO

Tutor Socràtic per a problemes de la **Prova Cangur de Catalunya**, categoria 1r d'ESO.
Interfície monolingüe en català; sessions anònimes; problemes tipus test amb 5 opcions A-E.

## Filosofia

L'alumne **dialoga** amb un tutor IA sobre el problema (no proposa "una resposta" per ser
jutjada). Tres accions deterministes complementen el diàleg:

- **Enviar missatge** → torn de conversa amb la IA (multimodal: la IA veu la imatge i
  tot l'historial de la sessió).
- **Demanar pista** → primera pista del catàleg (escrita per la persona), següents
  generades per la IA on-demand.
- **Ja tinc la resposta** → mode commit amb 5 botons A-E, comprovació determinista
  sense crida a la IA. Sense límit d'intents.

La IA mai revela la lletra correcta. La validació final és sempre del comprovador
determinista; això garanteix que la IA pugui ser sincera sense por de filtrar la
resposta.

## Execució

```bash
pip install -r requirements.txt
export GEMINI_API_KEY=...
streamlit run app.py
```

Mode debug (cost API + estat intern + rastre JSON):

```
http://localhost:8501/?debug=1
```

Opcional: canviar el model. Per defecte `gemini-2.5-flash`.

```bash
export GEMINI_MODEL=gemini-2.5-pro       # més qualitat, més lent, més car
export GEMINI_MODEL=gemini-2.5-flash-lite # més barat
```

## Estructura

| Fitxer | Responsabilitat |
|---|---|
| `tutor.py`         | Màquina d'estats. Entry points: `process_message`, `request_hint`, `process_commit`. |
| `llm.py`           | 2 crides a Gemini, totes multimodals: `discuss` (diàleg), `generate_hint` (pista). |
| `api_logger.py`    | Logger JSONL append-only amb tracking de cost USD. |
| `app.py`           | UI Streamlit estil chat (no té lògica de domini). |
| `problems.py`      | Catàleg de 30 problemes amb camp opcional `pista_inicial`. |
| `data/`            | Imatges JPG dels 30 enunciats (`CAN-1ESO-2026-XX.jpg`). |
| `SCHEMA.md`        | Esquema complet de les estructures de dades. |

## Flux d'una sessió

1. **Selecció**: l'alumne tria un problema del sidebar (filtrat per dificultat 3/4/5 punts).
2. **Diàleg**: el bloc del problema mostra la imatge i un fil de xat buit. Tres botons:
   - 📩 **Enviar missatge** → escriu el que penses ("dubto entre A i C", "no entenc per
     què la D pot ser") i la IA respon socràticament.
   - 💡 **Demanar pista** → primera pista del catàleg si està escrita, següents IA.
   - ✋ **Ja tinc la resposta** → entra al mode commit.
3. **Commit**: 5 botons A-E. Les lletres ja descartades per un commit fallit apareixen
   desactivades. Comprovació determinista (sense crida a la IA).
4. **Si encerta** → `solved`, sessió tancada amb resum.
5. **Si falla** → la lletra queda a `eliminated_options`, torna al mode diàleg. **Sense
   límit d'intents**; pot insistir tants cops com vulgui. Pot preguntar a la IA "per què
   la X no era correcta?" — la IA té al context que el comprovador ha rebutjat la X.

## Memòria conversacional

Cada crida a la IA passa **tota la `conversation_history`** truncada defensivament
(3 primers torns + 10 últims si supera 20). La imatge del problema es passa al primer
torn user de la conversa i Gemini la manté en context per als següents. La IA recorda:

- Què ha dit l'alumne als torns anteriors
- Quines pistes ha donat (prefixades amb `[PISTA] ` al multi-torn)
- Quins commits han fallat (prefixats amb `[Sistema] ` al multi-torn)

L'engine **no manté cap estat estructurat** sobre lletres "considerades" o "argumentades
a eliminar" (decisió arquitectònica): tot el seguiment viu dins del prompt multi-torn.
La UI només marca eliminades les lletres rebutjades pel commit determinista.

## Estat del catàleg

El catàleg `problems.py` cobreix una prova sencera de Cangur 1r ESO 2026: **30 problemes**
(10 de 3 punts, 10 de 4 punts, 10 de 5 punts), tots amb la imatge i la `resposta_correcta`
populats.

Camps opcionals encara per omplir manualment (degradació elegant: la IA opera sense ells,
amb qualitat més baixa):

- `pista_inicial`: 1a pista del catàleg, pre-escrita per la persona.
- `expected_reasoning`: solució desenvolupada per ancorar la IA.
- `comentaris_distractors`: per què algú podria triar cada lletra errònia.
- `tema`: classificació pedagògica (geometria, aritmètica...).
- `errors_típics`: etiquetes de l'`ERROR_CATALOG`.

## Estructura de fitxers de contingut

Les imatges dels enunciats van a la carpeta `data/`. El nom de fitxer ha de coincidir
amb el camp `imatge` de cada problema a `problems.py`.

Convenció recomanada: `{id}.jpg` (p.ex. `CAN-1ESO-2026-01.jpg`).

```
tutor-cangur/
├── app.py
├── problems.py
├── tutor.py
├── llm.py
├── api_logger.py
├── requirements.txt
└── data/
    ├── CAN-1ESO-2026-01.jpg
    ├── CAN-1ESO-2026-02.jpg
    └── ... (30 fitxers)
```

## Cost esperat

Cada torn de diàleg fa una crida a `discuss` multimodal. El cost depèn del model i de
la mida de la conversa acumulada:

- `gemini-2.5-flash` amb una conversa de 5-10 torns: ~$0.001-0.005 USD per torn.
- `gemini-2.5-pro`: ~5-8x més.

La imatge JPG de Cangur (~100 KB) val ~250-500 tokens d'input al primer torn de cada
crida. Una sessió típica completa: ~$0.005-0.02 USD amb `flash`.

## Limitacions conegudes (MVP)

- **Sense retrocés a prerequisits**: si un alumne no entén un concepte bàsic
  (perímetre, divisibilitat...), el tutor li dóna pistes però no l'envia a un
  mini-exercici de reforç. Es pot afegir més endavant.
- **Sense bateria de test exhaustiu**: el catàleg s'ha de validar a base de
  sessions reals fins que es construeixi un `TEST_CASES` per a sessions
  simulades.
- **Sense `expected_reasoning` poblat**: la IA llegeix la imatge i raona pel seu
  compte; pot equivocar-se en problemes amb truc. Quan poblis aquest camp, la
  qualitat del diàleg pujarà significativament.

## Mode professor

Aquesta versió és per provar el sistema un mateix abans del pilot real. No
fa pseudonimització, no demana consentiment, i guarda el rastre només a memòria
de Streamlit (es perd quan tanques la finestra). Per a desplegament real cal:

- Afegir un camp "Codi de l'alumne" al sidebar i propagar-lo a `set_log_context`.
- Document informatiu i consentiment a famílies.
- Sostre de despesa configurat a la consola de Google AI Studio.
- Persistència del rastre en disc (al final de la sessió o
  després d'una inactivitat de N segons).
