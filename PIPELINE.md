# Tutor Cangur — Problem Ingestion Pipeline

> **Audience:** An AI assistant that will execute or supervise this pipeline.  
> **Scope:** Any yearly edition of the Catalan Kangaroo math competition (Cangur Catalunya), any ESO level (1ESO–4ESO).  
> **Goal:** Transform a competition PDF into fully populated entries inside `problems_<level>eso.py`.

---

## Overview

```
PDF
 └─► 30 × JPG          (one image per question, crop + naming)
      └─► 30 × JSON     (Sonnet reads image, produces structured metadata)
           └─► verify   (hallucination check: JSON vs image, logic vs answer)
                └─► .py (Opus appends verified entry to problems_<level>eso.py)
```

Each stage has a **single responsibility**. Never skip or merge stages — the verification gate between JSON and .py is what prevents silent errors from accumulating in the knowledge base.

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

## Stage 2 — JPG → JSON (Sonnet)

**Who does it:** Claude Sonnet (vision). One API call per question. Calls can be parallelised across the 30 questions — they are fully independent.

**Input:** `CAN-<LEVEL>-<YEAR>-<NN>.jpg`  
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
- `resposta_correcta` is the letter of the correct answer, derived by solving the problem.
- `pista_inicial`: a single pedagogical nudge — not the solution, not the answer. It should redirect attention without giving anything away.
- `expected_reasoning`: full step-by-step solution written for the AI tutor, not for the student. Include all intermediate steps and the final answer letter.
- `comentaris_distractors`: for each **wrong** option, one sentence explaining the typical mistake that leads a student to choose it. Omit the correct option's key.
- `errors_tipics`: zero or more keys from `ERROR_CATALOG` in `problems.py`. Leave empty (`[]`) if none apply cleanly.

**Prompt guidance for Sonnet:**  
Tell Sonnet: (a) the level and year, (b) the question number and point value, (c) to solve the problem before writing `expected_reasoning`, (d) to write in Catalan, (e) to return only valid JSON with no markdown fences.

---

## Stage 3 — Verification (hallucination gate)

**Who does it:** a human reviewer, or a second Sonnet pass with explicit instructions to challenge the first pass.

**This stage exists because:** Sonnet can misread a figure, invent a distractor explanation that contradicts the image, or produce a `resposta_correcta` that is wrong. Catching this here costs seconds; catching it after it is in the .py costs a debugging session.

### Checklist per question

1. **Answer is correct.** Independently verify `resposta_correcta` by solving the problem from the image. Do not trust Sonnet's answer blindly.
2. **Reasoning is complete.** `expected_reasoning` must reach the answer step by step. If it jumps to a conclusion, reject it.
3. **Distractors are plausible.** Each `comentaris_distractors` entry must describe a real mistake (wrong formula, off-by-one, misread figure) — not a vague "student may confuse X with Y."
4. **`pista_inicial` is not a spoiler.** It must not name the method, give an intermediate result, or hint at the answer letter.
5. **`tema` is consistent.** Check against the list of accepted values: `geometria`, `aritmètica`, `combinatòria`, `lògica`, `àlgebra`, `probabilitat`, `estadística`.
6. **JSON is valid.** Parse it programmatically before proceeding.

**Output of this stage:** the same JSON, possibly corrected. A diff log of what was changed is useful for calibrating Sonnet's prompts over time.

---

## Stage 4 — JSON → `problems_<level>eso.py` (Opus)

**Who does it:** Claude Opus. One call per question (or one call per batch of 10, grouped by point value).

**Input:** the verified JSON for one question + the target `problems_<level>eso.py` file.  
**Output:** the file with the new entry appended to the `PROBLEMS` dict.

**Critical constraint:** Opus must receive **only** the relevant `problems_<level>eso.py`, never the full combined file. At ~36 KB per level file, the context is manageable and rate limits are not hit. Passing the full 145 KB monolith is what causes the "come back in 5 hours" limit.

**Opus's task is mechanical:** convert the JSON to a Python dict literal and insert it into `PROBLEMS` with `str_replace`. The creative work was done in Stage 2. Opus should not re-solve the problem or rewrite the reasoning.

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

## Cross-level deduplication (token economy)

Approximately 30% of questions are identical between 1ESO↔2ESO and 3ESO↔4ESO, with further overlap between 2ESO and 3ESO.

**Before running Stage 2 for a new level**, check whether the question image matches an existing entry in another level's .py file. If it does:
- Copy `expected_reasoning` and `comentaris_distractors` directly.
- Adjust `id`, `categoria`, `numero`, and `punts` for the new level.
- Re-evaluate `pista_inicial` — the same hint may need rewording for a different age group.

This check alone can eliminate 6–9 Sonnet calls per level per year.

---

## File naming and placement conventions

| Artefact | Path |
|---|---|
| Source PDF | `(external — not committed)` |
| Question images | `data/CAN-<LEVEL>-<YEAR>-<NN>.jpg` |
| Per-level problem database | `problems_<level>eso.py` (e.g. `problems_3eso.py`) |
| Shared error catalogue | `problems_shared.py` (contains `ERROR_CATALOG` and `DEPENDENCIES`) |

`app.py` imports all four level files and merges them at runtime. No level file imports another.

---

## Repeating for a new year

The pipeline is stateless and year-agnostic. To ingest `CAN-<LEVEL>-2025.pdf`:

1. Run Stage 1 with `YEAR=2025`.
2. Run Stage 2–4 as above.
3. The new entries live alongside 2026 entries in the same `problems_<level>eso.py`, distinguished by the `any` field.
4. The UI can optionally expose a year filter; the data model already supports it.

No code changes are needed between years — only data.
