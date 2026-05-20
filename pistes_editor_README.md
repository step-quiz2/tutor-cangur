# Editor de pistes — Tutor Cangur

Editor visual per revisar les `pista_inicial` del catàleg. Mostra la
imatge de cada problema al costat de la pista actual, deixa escriure'n
una de nova, i serialitza els canvis de tornada cap a
`problems_<nivell>eso.py` preservant tot el format original.

## Posada en marxa

```bash
# des de l'arrel del repo
python3 -m http.server 8000
# obre http://localhost:8000/pistes_editor.html
```

(Cal servir el repo amb un servidor local perquè la pàgina fa `fetch`
del fitxer `.py` i les imatges; no funciona obrint el fitxer com
`file://`.)

## Flux de treball

1. Tria **Any** (2025/2026) i **Curs** (1ESO–4ESO).
2. Per a cada pregunta:
   - **Columna esquerra** — la pista actual del catàleg (només lectura).
   - **Columna dreta** — textarea per escriure'n una de nova.
     - **Buida** = vols validar la pista existent (no es canvia res).
     - **Amb text** = la nova pista substituirà l'actual al desar.
3. Navega amb **‹ Anterior / Següent ›**, els cursors ←/→, o clicant
   qualsevol número al *minimap* de sota.
4. Clica **Desar** (o `Ctrl+S` / `⌘+S`) per veure un resum dels canvis i
   confirmar.

L'estat (selecció + edicions en curs + preguntes ja visitades) es
guarda automàticament a `localStorage`, així que pots tancar la
pestanya i tornar més tard.

## Què passa quan desem

En confirmar, l'editor produeix **dos fitxers**:

### 1. `problems_<nivell>eso.py` (actualitzat)

Només els blocs `"pista_inicial": ( … )` de les preguntes modificades
es reescriuen. Tota la resta del fitxer — comentaris, ordre, format,
qualsevol altre camp — queda **byte-per-byte intacte**.

- En navegadors basats en Chromium amb la *File System Access API*
  (Chrome, Edge, Brave, Arc), l'editor obre un diàleg de "Desar
  arxiu" amb el nom original ja preseleccionat — un sol clic
  sobreescriu el `.py` al seu lloc.
- En altres navegadors, es descarrega un `.py` nou que cal moure
  manualment a l'arrel del repo per substituir l'original.

### 2. `pistes_review_<NIVELL>_<ANY>_<DATA>.json` (log d'auditoria)

Sempre es descarrega. Conté un registre estructurat de la sessió:

```json
{
  "schema": "pistes_review_log/v1",
  "review_session": "2026-05-20T14:30:00Z",
  "catalog_file": "problems_1eso.py",
  "level": "1ESO",
  "year": 2026,
  "summary": { "total_problems": 30, "modified": 3,
               "validated": 24, "pending": 3 },
  "actions": [
    {"problem_id": "CAN-1ESO-2026-01", "numero": 1,
     "action": "validated", "pista": "..."},
    {"problem_id": "CAN-1ESO-2026-07", "numero": 7,
     "action": "modified",
     "pista_before": "...", "pista_after": "..."},
    ...
  ]
}
```

Per què aquest fitxer és útil:
- Traçabilitat: queda registre de qui ha validat quina pista i quan.
- Rollback: pots reconstruir pistes anteriors si una modificació
  resulta problemàtica.
- Commitejable a git al costat del `.py` per documentar revisions.

## Després de desar

Si vols regenerar `exports/pistes_inicials.docx` perquè reflecteixi
els canvis, executa:

```bash
python export.py
```

(El `.docx` és un derivat del `.py`; l'editor només toca el
`.py` font.)

## Verificació interna

Hi ha un test runner a `test_parser.js` que valida (a) que el
parser troba els 240 problemes correctament, (b) que el cicle
parse→emit→parse conserva el text, i (c) que parchejar només
toca els problemes que volem:

```bash
node test_parser.js
```
