# Integració total — Cangur 2025

Aquest ZIP conté **133 fitxers** organitzats en l'estructura final del repo.
Per integrar-ho:

## Mètode senzill (recomanat)

1. Clona o descarrega el repo `tutor-cangur` al teu disc.
2. Descomprimeix aquest ZIP sobre l'arrel del repo, deixant que sobreescrigui.
3. Comprova que tot estigui al seu lloc amb la validació de més avall.
4. Commit i push.

Els 4 fitxers que es sobreescriuen són els únics que ja existien al repo amb
el mateix nom; tots els altres són nous.

## Mapa exhaustiu

```
Arrel del repo:
├── pdf2jpg.py                          NOU   (Fase 1 agent X — Stage 1)
├── export.py                           NOU   (Fase 1 agent X — Stage 5)
├── problems_1eso.py                    REEMPLAÇA (agent p1, 60 problemes)
├── problems_2eso.py                    REEMPLAÇA (agent p2, 60 problemes)
├── problems_3eso.py                    REEMPLAÇA (agent f1, 60 problemes)
├── problems_4eso.py                    REEMPLAÇA (agent f2, 60 problemes)
│
├── data/
│   ├── CAN-1ESO-2025-{01..30}.jpg     30 NOUS (Fase 1)
│   ├── CAN-2ESO-2025-{01..30}.jpg     30 NOUS (Fase 1)
│   ├── CAN-3ESO-2025-{01..30}.jpg     30 NOUS (Fase 1)
│   ├── CAN-4ESO-2025-{01..30}.jpg     30 NOUS (Fase 1)
│   ├── CAN-1ESO-2025-answers.json     NOU   (Fase 1, Model A)
│   ├── CAN-2ESO-2025-answers.json     NOU   (Fase 1, Model A)
│   ├── CAN-3ESO-2025-answers.json     NOU   (Fase 1, Model A)
│   └── CAN-4ESO-2025-answers.json     NOU   (Fase 1, Model A)
│
└── exports/                            CARPETA NOVA
    ├── classificacio.xlsx              NOU   (Fase 3 — Stage 5a, 240 files)
    ├── pistes_inicials.docx            NOU   (Fase 3 — Stage 5b, 240 entrades)
    └── distractors.docx                NOU   (Fase 3 — Stage 5c, 240 entrades)
```

## Què NO es toca

Aquests fitxers ja existeixen al repo i continuen IGUAL — no estan a aquest ZIP:

```
PIPELINE.md, README.md, SCHEMA.md       (congelats)
problems.py, problems_shared.py         (congelats)
app.py, tutor.py, llm.py                (modificats per l'humà; respecto)
api_logger.py, requirements.txt         (congelats)
.streamlit/                             (config)
data/CAN-*-2026-*.jpg                   (120 JPGs del 2026, ja al repo)
```

## Validació post-integració

Al teu disc, des de l'arrel del repo, executa:

```bash
# 1. Comprovar que cada nivell té 60 problemes (30 del 2025 + 30 del 2026)
python3 -c "
import problems_1eso, problems_2eso, problems_3eso, problems_4eso
for mod, lvl in [(problems_1eso,'1ESO'),(problems_2eso,'2ESO'),
                 (problems_3eso,'3ESO'),(problems_4eso,'4ESO')]:
    n = len(mod.PROBLEMS)
    years = sorted({p['any'] for p in mod.PROBLEMS.values()})
    assert n == 60 and years == [2025, 2026], f'{lvl} té {n}, anys={years}'
    print(f'  {lvl}: {n} problemes OK')
"

# 2. Comprovar que data/ té 240 JPGs i 4 JSON
ls data/CAN-*.jpg | wc -l    # esperat: 240
ls data/*.json | wc -l        # esperat: 4

# 3. Comprovar que els exports compten 240
python3 -c "
from openpyxl import load_workbook
wb = load_workbook('exports/classificacio.xlsx')
print('  Files XLSX:', wb.active.max_row - 1, '(esperat 240)')
"

# 4. Regenerar els exports per garantir reproducibilitat
python3 export.py
```

Si els 4 passos passen, la integració és OK.

— Agent X
