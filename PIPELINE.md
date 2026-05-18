# Tutor Cangur — Problem Ingestion Pipeline

> **Audience:** An AI assistant that will execute or supervise this pipeline.  
> **Scope:** Any yearly edition of the Catalan Kangaroo math competition (Cangur Catalunya), any ESO level (1ESO–4ESO).  
> **Goal:** Transform a competition PDF into fully populated entries inside `problems_<level>eso.py`, plus the human-readable exports (XLSX of classifications, DOCX of hints, DOCX of distractors).

---

## Overview

```
ANSWER KEY  ─────────────────────────────────────┐
                                                 │
PDF                                              ▼
 └─► 30 × JPG          (one image per question, crop + naming)
      └─► 30 × JSON     (Sonnet justifies the GIVEN answer, produces hint + distractors)
           └─► verify   (consistency check: JSON vs image, justification vs given answer)
                └─► .py (Opus appends verified entry to problems_<level>eso.py)
                     └─► exports (XLSX classification + DOCX hints + DOCX distractors)
```

Each stage has a **single responsibility**. Never skip or merge stages — the verification gate between JSON and .py is what prevents silent errors from accumulating in the knowledge base.

---

## Stage 0 — Answer key (mandatory input)

**Who does it:** human curator, before any AI is involved.

**Input:** the official answer key for `CAN-<LEVEL>-<YEAR>` (published by the organisers — usually a one-page PDF or a row in a results table).  
**Output:** `data/CAN-<LEVEL>-<YEAR>-answers.json`, a flat mapping:

```json
{ "01": "B", "02": "D", "03": "A", "...": "...", "30": "C" }
```

**Why this stage exists — and why it is non-negotiable:**

The AI **never solves the problems**. The correct answer is always provided as input to Stage 2. This is a deliberate design choice, not a shortcut:

- Sonnet is a generalist; it makes occasional reasoning slips on competition problems, and any wrong answer it produces will poison the *entire* downstream record (`expected_reasoning`, distractor comments, hint, classification).
- When the answer is known up front, Sonnet works *backwards from the truth*: it can write a correct justification, identify exactly *why each wrong option is wrong* (rather than guessing what a student might think), and target the hint to the genuine solution path.
- Pedagogically this is the right shape too: the value of these records is the *explanation*, not a re-derivation of an already-published answer.

**Validation:** the file must contain exactly 30 entries, all keys zero-padded `01`–`30`, all values one of `A`–`E`.

---

## Stage 1 — PDF → JPG

**Who does it:** automated script (e.g. `pdf2jpg.py` using `pdfplumber` or `pymupdf`).

**Input:** `CAN-<LEVEL>-<YEAR>.pdf` (4 pages, 30 questions).  
**Output:** `data/CAN-<LEVEL>-<YEAR>-<NN>.jpg`, where `NN` is zero-padded (01–30).

**Rules:**
- One JPG per question. The crop must include the full question text, all answer options (A–E), and any associated figure or diagram. It must **not** include content from adjacent questions.
- Questions 1–10 are worth 3 points, 11–20 are worth 4 points, 21–30 are worth 5 points. This maps to the `punts` field later.
- Resolution: 150–200 dpi is enough; higher wastes tokens in Stage 2.
- Naming is strict: `CAN-3ESO-2026-07.jpg`, never `CAN-3ESO-2026-7.jpg`.

**Validation:** After extraction, confirm that exactly 30 files exist and that file sizes are non-trivial (> 20 KB each). A tiny file means a failed crop.

---

## Stage 2 — JPG + answer → JSON (Sonnet)

**Who does it:** Claude Sonnet (vision). One API call per question. Calls can be parallelised across the 30 questions — they are fully independent.

**Inputs (both required):**
1. The question image: `CAN-<LEVEL>-<YEAR>-<NN>.jpg`
2. The correct answer letter, looked up from `data/CAN-<LEVEL>-<YEAR>-answers.json`

**Output:** a JSON object with the fields below.

### JSON schema

```json
{
  "id":                   "CAN-3ESO-2026-07",
  "categoria":            "3ESO",
  "any":                  2026,
  "numero":               7,
  "punts":                3,
  "tema":                 "aritmètica",
  "imatge":               "CAN-3ESO-2026-07.jpg",
  "enunciat":             null,
  "opcions":              {"A": null, "B": null, "C": null, "D": null, "E": null},
  "resposta_correcta":    "C",
  "pista_inicial":        "...",
  "expected_reasoning":   "...",
  "comentaris_distractors": {
    "A": "...",
    "B": "...",
    "D": "...",
    "E": "..."
  },
  "errors_tipics":        ["LOG_dada_ignorada"],
  "dependencies":         []
}
```

**Field notes:**
- `enunciat` and `opcions` values are `null` when `imatge` is present — the image is the source of truth for the student UI.
- `resposta_correcta` is **copied verbatim** from the answer key file. Sonnet does not derive it and must not alter it.
- `pista_inicial`: a **single, brief** pedagogical nudge — see the brevity rule below.
- `expected_reasoning`: full step-by-step justification of *why the given answer is correct*, written for the AI tutor (not for the student). Include all intermediate steps and end at the given answer letter.
- `comentaris_distractors`: for each **wrong** option, one sentence explaining the typical mistake that leads a student to choose it. Omit the correct option's key.
- `errors_tipics`: zero or more keys from `ERROR_CATALOG` in `problems_shared.py`. Leave empty (`[]`) if none apply cleanly.
- `tema`: one of `geometria`, `aritmètica`, `combinatòria`, `lògica`, `àlgebra`, `probabilitat`, `estadística`. This drives the XLSX classification export in Stage 5.

### The `pista_inicial` brevity rule

The hint must **not** lay out the full strategy. It is one tap on the shoulder, not a roadmap.

Allowed shapes for a hint (pick one — never combine):
- **First step only.** If the solution has three steps, name the first one and stop. E.g. *"Comença comptant quantes parelles consecutives sumen un múltiple de 3."*
- **Eliminate one option cheaply.** Point out that one wrong option can be ruled out by substitution or a quick parity/order-of-magnitude check. E.g. *"L'opció B és descartable substituint les dades a l'enunciat."*
- **Suggest the meta-strategy.** When the natural method is elimination, say so without doing the eliminating. E.g. *"Aquí va més ràpid falsar les quatre opcions incorrectes que no pas construir la resposta de zero."*

**Forbidden in a hint:** the full method, intermediate numerical results, the answer letter, more than one of the shapes above, or any sentence that begins with *"Primer... després... finalment..."*. If the hint reads like a mini-solution, it is wrong and Stage 3 will reject it.

**Prompt guidance for Sonnet:**  
Tell Sonnet: (a) the level and year, (b) the question number and point value, (c) **the correct answer letter as a given fact** — Sonnet must justify it, not verify it, (d) to write in Catalan, (e) to obey the `pista_inicial` brevity rule above, (f) to return only valid JSON with no markdown fences.

---

## Stage 3 — Verification (consistency gate)

**Who does it:** a human reviewer, or a second Sonnet pass with explicit instructions to challenge the first pass.

**This stage exists because:** even with the answer letter provided, Sonnet can write a justification that doesn't actually reach that letter, invent a distractor explanation that contradicts the image, or produce a hint that gives the game away. Catching this here costs seconds; catching it after it is in the .py costs a debugging session.

### Checklist per question

1. **`resposta_correcta` matches the answer key file.** This is a literal string comparison — if it doesn't match, something has gone wrong in transcription and the entry is rejected outright.
2. **The justification reaches the given answer.** Read `expected_reasoning` end-to-end. The final step must arrive at `resposta_correcta`, with no logical gaps. If the reasoning is internally valid but lands on a different letter, the *reasoning* is wrong (not the answer) and must be redone.
3. **Distractors are plausible.** Each `comentaris_distractors` entry must describe a real mistake (wrong formula, off-by-one, misread figure) — not a vague *"student may confuse X with Y."*
4. **`pista_inicial` obeys the brevity rule.** It must use exactly one of the three allowed shapes (first step / eliminate one option / meta-strategy), and must not name the method in full, give an intermediate result, or hint at the answer letter.
5. **`tema` is consistent** with the list of accepted values and accurately reflects the problem (this matters because it drives the XLSX export).
6. **JSON is valid.** Parse it programmatically before proceeding.

**Output of this stage:** the same JSON, possibly corrected. A diff log of what was changed is useful for calibrating Sonnet's prompts over time.

---

## Stage 4 — JSON → `problems_<level>eso.py` (Opus)

**Who does it:** Claude Opus. One call per question (or one call per batch of 10, grouped by point value).

**Input:** the verified JSON for one question + the target `problems_<level>eso.py` file.  
**Output:** the file with the new entry appended to the `PROBLEMS` dict.

**Critical constraint:** Opus must receive **only** the relevant `problems_<level>eso.py`, never the full combined file. At ~36 KB per level file, the context is manageable and rate limits are not hit. Passing the full 145 KB monolith is what causes the "come back in 5 hours" limit.

**Opus's task is mechanical:** convert the JSON to a Python dict literal and insert it into `PROBLEMS` with `str_replace`. The creative work was done in Stage 2. Opus must not re-solve the problem, rewrite the reasoning, or alter `resposta_correcta`.

**Suggested prompt structure:**
```
Here is problems_3eso.py (full content).
Here is the verified JSON for question CAN-3ESO-2026-07.
Add this entry to the PROBLEMS dict in the correct position (after question 06).
Return only the str_replace old_str and new_str. Do not rewrite the whole file.
```

**Post-insert validation:**
- Import the file in a Python interpreter: `python -c "import problems_3eso; print(len(problems_3eso.PROBLEMS))"`.
- Confirm the count increased by 1.
- Confirm the new key is present: `"CAN-3ESO-2026-07" in problems_3eso.PROBLEMS`.

---

## Stage 5 — Exports (XLSX + DOCX)

**Who does it:** automated script (e.g. `export.py` using `openpyxl` and `python-docx`). Runs after Stage 4 completes for a full level/year, or on demand against the whole corpus.

**Input:** one or more `problems_<level>eso.py` files (the canonical source — the .py is always authoritative; exports are derived).

**Outputs (three artefacts):**

### 5a. `exports/classificacio.xlsx` — problem classification

One row per problem, intended for curators to see the corpus at a glance and balance topics across levels and years.

| Column | Source field | Notes |
|---|---|---|
| `id` | `id` | e.g. `CAN-3ESO-2026-07` |
| `categoria` | `categoria` | `1ESO`–`4ESO` |
| `any` | `any` | integer |
| `numero` | `numero` | 1–30 |
| `punts` | `punts` | 3 / 4 / 5 |
| `tema` | `tema` | one of the seven accepted values |
| `resposta_correcta` | `resposta_correcta` | A–E |

Sort by `categoria`, then `any`, then `numero`. One worksheet, no per-level splits — pivot tables in Excel are cheaper than maintaining multiple sheets.

### 5b. `exports/pistes_inicials.docx` — initial hints

One section per level, one entry per problem within each section:

> **CAN-3ESO-2026-07** (3 punts · aritmètica)  
> *Pista:* L'opció B és descartable substituint les dades a l'enunciat.

This document is what a workshop facilitator prints when they want to coach a class without showing solutions. It must contain **only** `id`, point value, `tema`, and `pista_inicial` — never `expected_reasoning` and never `resposta_correcta`. Mixing those in would defeat the purpose.

### 5c. `exports/distractors.docx` — studied distractors

One section per level, one entry per problem within each section. Each entry lists the four wrong options and the typical mistake behind each:

> **CAN-3ESO-2026-07** — resposta correcta: C  
> - **A:** confusió típica entre perímetre i àrea.  
> - **B:** errada de signe en la resta final.  
> - **D:** comptar el cas degenerat com a vàlid.  
> - **E:** llegir malament la unitat (cm vs m).

This document is the teacher-facing companion to the hints document: it explains *why a student fell into each trap*, so the teacher can target their feedback. The correct option is named at the top but not commented on (no `comentaris_distractors` entry exists for it).

**Validation:** after generation, open each file and confirm row/section counts match `len(PROBLEMS)` across the level files included.

---

## Cross-level deduplication (token economy)

Approximately 30% of questions are identical between 1ESO↔2ESO and 3ESO↔4ESO, with further overlap between 2ESO and 3ESO.

**Before running Stage 2 for a new level**, check whether the question image matches an existing entry in another level's .py file. If it does:
- Copy `expected_reasoning` and `comentaris_distractors` directly.
- Adjust `id`, `categoria`, `numero`, and `punts` for the new level.
- Re-evaluate `pista_inicial` against the brevity rule — the same hint may need rewording for a different age group, and a hint that was acceptable at 4ESO may be too revealing at 1ESO (or vice versa).

This check alone can eliminate 6–9 Sonnet calls per level per year.

---

## File naming and placement conventions

| Artefact | Path |
|---|---|
| Source PDF | `(external — not committed)` |
| Answer key (per level/year) | `data/CAN-<LEVEL>-<YEAR>-answers.json` |
| Question images | `data/CAN-<LEVEL>-<YEAR>-<NN>.jpg` |
| Per-level problem database | `problems_<level>eso.py` (e.g. `problems_3eso.py`) |
| Shared error catalogue | `problems_shared.py` (contains `ERROR_CATALOG` and `DEPENDENCIES`) |
| Classification export | `exports/classificacio.xlsx` |
| Initial hints export | `exports/pistes_inicials.docx` |
| Distractors export | `exports/distractors.docx` |

`app.py` imports all four level files and merges them at runtime. No level file imports another. The three export files in `exports/` are regenerated from the .py files and should never be edited by hand.

---

## Repeating for a new year

The pipeline is stateless and year-agnostic. To ingest `CAN-<LEVEL>-2025.pdf`:

1. Obtain the official answer key and run Stage 0 → produce `CAN-<LEVEL>-2025-answers.json`.
2. Run Stage 1 with `YEAR=2025`.
3. Run Stage 2–4 as above.
4. Run Stage 5 to regenerate the three export artefacts so they include the new year.
5. The new entries live alongside other years in the same `problems_<level>eso.py`, distinguished by the `any` field.
6. The UI can optionally expose a year filter; the data model already supports it.

No code changes are needed between years — only data.
