#!/usr/bin/env bash
# Rebuild the Track-2 PDFs and gate them on layout (run from anywhere).
#
# The gate is the point: build_figs.py already self-gates figure labels against their boxes, but
# nothing checked the BUILT PDFs, so text running past the page edge shipped unnoticed — five
# such runs were present before this change (measured, see checks/check_pdf_layout.py).
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

for tool in pandoc xelatex python3; do
  command -v "$tool" >/dev/null || { echo "missing required tool: $tool" >&2; exit 3; }
done

build() {  # build <source.md> <target.pdf> <title>
  pandoc "$1" -o "$2" \
    --toc --pdf-engine=xelatex \
    --resource-path=docs:docs/figures:. \
    --include-in-header=docs/pdf_style.tex \
    -V geometry:margin=1in \
    -V colorlinks=true -V linkcolor=black -V urlcolor=blue \
    --metadata title="$3" \
    --metadata mainfont="DejaVu Serif"
  echo "built $2"
}

build docs/TECHNICAL_DOCUMENTATION.md TRACK2_TECHNICAL_DOCUMENTATION.pdf "Track 2 — Technical Documentation"
[ -f TRACK2_REPORT.md ]     && build TRACK2_REPORT.md     TRACK2_REPORT.pdf     "Track 2 — Report"
[ -f TRACK2_LAY_REPORT.md ] && build TRACK2_LAY_REPORT.md TRACK2_LAY_REPORT.pdf "Track 2 — Lay Report"


# Parity rule: XeLaTeX embeds per-build metadata, so the byte hash of a PDF is
# NOT deterministic. The parity contract this repo keeps is content-extract equality:
# after a rebuild, `pdftotext <pdf> | sha256sum` must match the recorded fingerprint.
# Refresh the recorded fingerprints whenever source text changes, in this commit.

echo "--- layout gate ---"
# Hard gate: text past the PHYSICAL PAGE EDGE is clipped on screen and in print. Non-zero exit
# fails the build.
#
# A margin-level check is deliberately NOT run: running headers and page-number footers sit
# outside the text block by design, so checking against the 1in margin reports hundreds of
# findings that are not defects. The page edge is the line that actually matters.
python3 checks/check_pdf_layout.py --margin-pt 0 TRACK2_*.pdf || {
  echo "FAIL: text runs past the page edge in a built PDF (see findings above)" >&2; exit 5; }
echo "layout gate: clean"
