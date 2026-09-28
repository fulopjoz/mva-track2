#!/usr/bin/env bash
# Rebuild TRACK2_TECHNICAL_DOCUMENTATION.pdf (run from repo root).
set -euo pipefail
pandoc docs/TECHNICAL_DOCUMENTATION.md \
  -o TRACK2_TECHNICAL_DOCUMENTATION.pdf \
  --toc --pdf-engine=xelatex \
  --resource-path=docs:docs/figures \
  --metadata title="Track 2 — Technical Documentation" \
  --metadata mainfont="DejaVu Serif"
echo "built TRACK2_TECHNICAL_DOCUMENTATION.pdf"
