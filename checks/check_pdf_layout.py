#!/usr/bin/env python3
"""Content-free layout audit for PDFs that may hold case-linked text.

Finds the visual defects a reader notices — text past the margin, overlapping blocks,
missing glyphs, blank pages, broken images, unembedded fonts — and reports ONLY structure:
page numbers, defect codes, counts and coordinates.

NO DOCUMENT TEXT IS EVER PRINTED OR RETURNED. That is the point: these files are
patient-derived, so their text must not reach a terminal, a log or a model context. Every
output line is assembled from numbers, fixed defect codes and font names; extracted text is
used only for geometry and comparison inside the process and is never formatted into output.
A final guard re-checks every line before printing.

Usage:  pdf_layout_audit.py FILE.pdf [FILE.pdf ...] [--margin-pt 36] [--json]
Exit:   0 clean, 1 defects found, 2 usage/read error.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import fitz  # PyMuPDF

# Output may contain only these shapes. Anything else is a leak and is refused.
SAFE_LINE = re.compile(r"^[A-Za-z0-9_.,:;()\[\]{}<>/+\-=%*'\"|@#$^~`!?\\ \t]*$")
# A defect code vocabulary, so no free text is ever emitted.
CODES = {
    "OVERFLOW_RIGHT", "OVERFLOW_LEFT", "OVERFLOW_TOP", "OVERFLOW_BOTTOM",
    "BLOCK_OVERLAP", "MISSING_GLYPH", "BLANK_PAGE", "IMAGE_ZERO_SIZE",
    "IMAGE_OFFPAGE", "FONT_NOT_EMBEDDED", "PAGE_SIZE_MISMATCH",
}
# Replacement/notdef glyphs: their presence means the renderer could not draw a character.
BAD_GLYPHS = ("�", "□", "\x00")
# Extractors emit "(cid:NN)" when a glyph has no usable unicode mapping.
CID_UNMAPPED = re.compile(r"\(cid:\d+\)")


def rects_overlap(a, b, tol: float = 1.0) -> float:
    """Area of intersection, ignoring slivers that are just normal line spacing."""
    x0, y0 = max(a.x0, b.x0), max(a.y0, b.y0)
    x1, y1 = min(a.x1, b.x1), min(a.y1, b.y1)
    w, h = x1 - x0 - tol, y1 - y0 - tol
    return w * h if w > 0 and h > 0 else 0.0


def font_embedding(path: Path) -> list[str]:
    """Font names that are NOT embedded (pdffonts 'emb' column == 'no')."""
    try:
        out = subprocess.run(["pdffonts", str(path)], capture_output=True, text=True, timeout=60)
    except Exception:
        return []
    bad = []
    for line in out.stdout.splitlines()[2:]:
        parts = line.split()
        if len(parts) >= 4 and parts[-4:-3] == ["no"] or (len(parts) > 3 and parts[3] == "no"):
            name = re.sub(r"[^A-Za-z0-9+_-]", "", parts[0])[:60]
            if name:
                bad.append(name)
    return sorted(set(bad))


def audit(path: Path, margin: float) -> list[dict]:
    doc = fitz.open(path)
    findings: list[dict] = []
    sizes = set()
    for pno, page in enumerate(doc, start=1):
        r = page.rect
        sizes.add((round(r.width), round(r.height)))
        content = fitz.Rect(margin, margin, r.width - margin, r.height - margin)

        drawn = page.get_text().strip()
        if not drawn and not page.get_images(full=True) and not page.get_drawings():
            findings.append({"page": pno, "code": "BLANK_PAGE"})

        # Span-level geometry. PyMuPDF merges visually adjacent text into one "block", so two
        # labels drawn on top of each other can share a block and hide the collision; spans
        # keep each drawn run separate, which is what a reader actually sees.
        spans = []
        for blk in page.get_text("dict").get("blocks", []):
            if blk.get("type") != 0:
                continue
            for line in blk.get("lines", []):
                for sp in line.get("spans", []):
                    txt = sp.get("text", "")
                    if not txt.strip():
                        continue
                    spans.append((fitz.Rect(sp["bbox"]), txt, blk.get("number", -1)))

        for bb, txt, _ in spans:
            for code, over in (
                ("OVERFLOW_LEFT", content.x0 - bb.x0),
                ("OVERFLOW_RIGHT", bb.x1 - content.x1),
                ("OVERFLOW_TOP", content.y0 - bb.y0),
                ("OVERFLOW_BOTTOM", bb.y1 - content.y1),
            ):
                if over > 1.0:  # 1pt tolerance: rounding, not a real defect
                    findings.append({"page": pno, "code": code, "overflow_pt": round(over, 1),
                                     "bbox": [round(v, 1) for v in bb]})
            # Geometry only: the text itself is inspected but never reported.
            n_bad = sum(txt.count(g) for g in BAD_GLYPHS) + len(CID_UNMAPPED.findall(txt))
            if n_bad:
                findings.append({"page": pno, "code": "MISSING_GLYPH", "count": n_bad,
                                 "bbox": [round(v, 1) for v in bb]})

        for i in range(len(spans)):
            for j in range(i + 1, len(spans)):
                a, b = spans[i][0], spans[j][0]
                # Ignore spans on the same text line: adjacent runs legitimately touch.
                if abs(a.y0 - b.y0) < 1.0 and abs(a.y1 - b.y1) < 1.0:
                    continue
                area = rects_overlap(a, b, tol=2.0)
                if area > 12.0:  # ~ one character cell; smaller is kerning noise
                    findings.append({"page": pno, "code": "BLOCK_OVERLAP",
                                     "area_pt2": round(area, 1),
                                     "bbox": [round(v, 1) for v in (a & b)]})

        for img in page.get_images(full=True):
            try:
                bbox = page.get_image_bbox(img)
            except Exception:
                continue
            if bbox.is_empty or bbox.width < 1 or bbox.height < 1:
                findings.append({"page": pno, "code": "IMAGE_ZERO_SIZE"})
            elif not bbox.intersects(r):
                findings.append({"page": pno, "code": "IMAGE_OFFPAGE",
                                 "bbox": [round(v, 1) for v in bbox]})

    if len(sizes) > 1:
        findings.append({"page": 0, "code": "PAGE_SIZE_MISMATCH", "count": len(sizes)})
    for f in font_embedding(path):
        findings.append({"page": 0, "code": "FONT_NOT_EMBEDDED", "font": f})
    doc.close()
    return findings


def emit(lines: list[str]) -> None:
    """Final guard: refuse to print anything that is not plain structural output."""
    for ln in lines:
        if not SAFE_LINE.match(ln):
            print("REFUSED: output line failed the content-free guard", file=sys.stderr)
            sys.exit(2)
    print("\n".join(lines))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdfs", nargs="+", type=Path)
    ap.add_argument("--margin-pt", type=float, default=36.0, help="content margin in points (default 36 = 0.5in)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    report, total = {}, 0
    for p in a.pdfs:
        if not p.is_file():
            print(f"REFUSED: not a file: {p.name}", file=sys.stderr)
            return 2
        try:
            fs = audit(p, a.margin_pt)
        except Exception as e:  # noqa: BLE001 - never surface a message that may quote content
            print(f"ERROR reading {p.name}: {type(e).__name__}", file=sys.stderr)
            return 2
        for f in fs:
            assert f["code"] in CODES, f["code"]
        report[p.name] = fs
        total += len(fs)

    if a.json:
        emit([json.dumps(report, indent=1, sort_keys=True)])
        return 1 if total else 0

    lines = []
    for name, fs in report.items():
        counts: dict[str, int] = {}
        for f in fs:
            counts[f["code"]] = counts.get(f["code"], 0) + 1
        lines.append(f"== {name}: {len(fs)} finding(s)")
        for code in sorted(counts):
            lines.append(f"   {code}: {counts[code]}")
        for f in fs[:40]:
            detail = " ".join(f"{k}={v}" for k, v in f.items() if k not in ("page", "code"))
            lines.append(f"   p{f['page']:>3} {f['code']} {detail}")
        if len(fs) > 40:
            lines.append(f"   ... {len(fs) - 40} more")
    lines.append(f"METRIC pdf_layout_findings={total}")
    emit(lines)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
