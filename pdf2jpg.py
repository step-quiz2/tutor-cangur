"""
pdf2jpg.py — Stage 1 of the Cangur ingestion pipeline.

Split a 4-page Cangur PDF (CAN-<LEVEL>-<YEAR>.pdf) into 30 JPG crops,
one per question, saved as data/CAN-<LEVEL>-<YEAR>-NN.jpg with NN
zero-padded (01-30). See PIPELINE.md, Stage 1.

Usage:
    python pdf2jpg.py path/to/CAN-3ESO-2025.pdf
    python pdf2jpg.py path/to/CAN-3ESO-2025.pdf --output-dir data
    python pdf2jpg.py path/to/CAN-3ESO-2025.pdf --dpi 180

Each crop covers a horizontal slice of the page from the question's label
('1.', '2.', …) down to the next question's label (or the bottom of the
page if it is the last question on that page). The full statement, all
five options A–E, and any inline figure are included; content from
adjacent questions is excluded.

Validation: exits non-zero if fewer than 30 anchors are detected or if any
output file is smaller than 20 KB (suggests a failed crop).
"""

import argparse
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF


EXPECTED_QUESTIONS = 30
MIN_FILE_SIZE_BYTES = 20 * 1024  # PIPELINE.md Stage 1 validation threshold

# Lines starting with "N." followed by a space and some non-space content.
# Cangur questions all begin this way; numbered sub-items inside an option
# (e.g. "a) ...") don't match.
QUESTION_LABEL_RE = re.compile(r"^\s*(\d{1,2})\.\s+\S")

# Filename pattern: CAN-<LEVEL>-<YEAR>.pdf, e.g. CAN-3ESO-2025.pdf
PDF_NAME_RE = re.compile(r"^CAN-([1-4]ESO)-(\d{4})\.pdf$", re.IGNORECASE)


def parse_pdf_name(pdf_path: Path) -> tuple[str, int]:
    """Extract LEVEL ('3ESO') and YEAR (2025) from the input filename."""
    match = PDF_NAME_RE.match(pdf_path.name)
    if not match:
        raise ValueError(
            f"Filename '{pdf_path.name}' does not match CAN-<LEVEL>-<YEAR>.pdf "
            f"(expected something like 'CAN-3ESO-2025.pdf')."
        )
    return match.group(1).upper(), int(match.group(2))


def find_question_anchors(doc: "fitz.Document") -> dict[int, tuple[int, float]]:
    """Locate the top-y coordinate of each question's label.

    Returns {qnum: (page_idx, y_top)} for qnum in 1..30 (as found).
    Scans top-to-bottom on each page, advancing the 'next expected
    question number' counter monotonically — a stray '1.' deep in the
    document cannot rebind question 1 once we've moved past it.
    """
    anchors: dict[int, tuple[int, float]] = {}
    next_expected = 1

    for page_idx, page in enumerate(doc):
        # Collect (y_top, qnum) candidates on this page
        candidates: list[tuple[float, int]] = []
        for block in page.get_text("dict").get("blocks", []):
            if block.get("type", 0) != 0:  # 0 = text block
                continue
            for line in block.get("lines", []):
                text = "".join(span["text"] for span in line.get("spans", []))
                m = QUESTION_LABEL_RE.match(text)
                if m:
                    qnum = int(m.group(1))
                    if 1 <= qnum <= EXPECTED_QUESTIONS:
                        y_top = float(line["bbox"][1])
                        candidates.append((y_top, qnum))

        candidates.sort()  # top of page first
        for y_top, qnum in candidates:
            if qnum == next_expected:
                anchors[qnum] = (page_idx, y_top)
                next_expected += 1
                if next_expected > EXPECTED_QUESTIONS:
                    return anchors

    return anchors


def compute_crop_bounds(
    anchors: dict[int, tuple[int, float]],
    doc: "fitz.Document",
    bottom_margin_points: float = 2.0,
) -> list[tuple[int, int, float, float]]:
    """Return [(qnum, page_idx, y_top, y_bottom), ...] in question order.

    Each crop ends 2 points above the next question's anchor (same page)
    or at the bottom of the current page (if the next question lives on
    a later page, or this is question 30).
    """
    items = []
    sorted_qs = sorted(anchors.keys())
    for i, qnum in enumerate(sorted_qs):
        page_idx, y_top = anchors[qnum]
        page_bottom = float(doc[page_idx].rect.y1)
        if i + 1 < len(sorted_qs):
            next_qnum = sorted_qs[i + 1]
            next_page_idx, next_y_top = anchors[next_qnum]
            if next_page_idx == page_idx:
                y_bottom = max(y_top + 1.0, next_y_top - bottom_margin_points)
            else:
                y_bottom = page_bottom
        else:
            y_bottom = page_bottom
        items.append((qnum, page_idx, y_top, y_bottom))
    return items


def render_crop_jpeg(
    doc: "fitz.Document",
    page_idx: int,
    y_top: float,
    y_bottom: float,
    dpi: int,
    quality: int,
) -> bytes:
    """Render a horizontal slice of a page as JPEG bytes."""
    page = doc[page_idx]
    page_rect = page.rect
    clip = fitz.Rect(page_rect.x0, y_top, page_rect.x1, y_bottom)
    matrix = fitz.Matrix(dpi / 72.0, dpi / 72.0)
    pix = page.get_pixmap(matrix=matrix, clip=clip, colorspace=fitz.csRGB, alpha=False)
    return pix.tobytes("jpeg", jpg_quality=quality)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("pdf", type=Path, help="Path to CAN-<LEVEL>-<YEAR>.pdf")
    ap.add_argument(
        "--output-dir", type=Path, default=Path("data"),
        help="Output directory (default: data/)",
    )
    ap.add_argument(
        "--dpi", type=int, default=180,
        help="Render resolution in dpi (default: 180; PIPELINE.md recommends 150-200)",
    )
    ap.add_argument(
        "--jpeg-quality", type=int, default=85,
        help="JPEG quality 1-100 (default: 85)",
    )
    args = ap.parse_args()

    if not args.pdf.is_file():
        print(f"ERROR: PDF not found: {args.pdf}", file=sys.stderr)
        return 1

    try:
        level, year = parse_pdf_name(args.pdf)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)

    with fitz.open(args.pdf) as doc:
        anchors = find_question_anchors(doc)
        missing = [n for n in range(1, EXPECTED_QUESTIONS + 1) if n not in anchors]
        if missing:
            print(
                f"ERROR: could not locate question labels for: {missing}.\n"
                f"  Found {len(anchors)}/{EXPECTED_QUESTIONS} anchors.\n"
                f"  Inspect the PDF — perhaps an unusual layout or non-standard "
                f"numbering. You may need to tweak QUESTION_LABEL_RE.",
                file=sys.stderr,
            )
            return 2

        bounds = compute_crop_bounds(anchors, doc)

        saved: list[tuple[str, int]] = []
        for qnum, page_idx, y_top, y_bottom in bounds:
            jpeg_bytes = render_crop_jpeg(
                doc, page_idx, y_top, y_bottom, args.dpi, args.jpeg_quality
            )
            filename = f"CAN-{level}-{year}-{qnum:02d}.jpg"
            out_path = args.output_dir / filename
            out_path.write_bytes(jpeg_bytes)
            saved.append((filename, len(jpeg_bytes)))

    print(f"Generated {len(saved)} JPG files in {args.output_dir}/")
    too_small = []
    for filename, size in saved:
        marker = ""
        if size < MIN_FILE_SIZE_BYTES:
            marker = "  ⚠ UNDER 20 KB"
            too_small.append(filename)
        print(f"  {filename}  {size / 1024:6.1f} KB{marker}")

    if len(saved) != EXPECTED_QUESTIONS:
        print(
            f"\nVALIDATION FAILED: expected {EXPECTED_QUESTIONS} files, got {len(saved)}.",
            file=sys.stderr,
        )
        return 3
    if too_small:
        print(
            f"\nVALIDATION FAILED: {len(too_small)} file(s) under {MIN_FILE_SIZE_BYTES} bytes: "
            f"{too_small}.\n  Likely a failed crop — inspect them manually.",
            file=sys.stderr,
        )
        return 4

    print(
        f"\nValidation OK: all {len(saved)} crops are ≥ "
        f"{MIN_FILE_SIZE_BYTES // 1024} KB."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
