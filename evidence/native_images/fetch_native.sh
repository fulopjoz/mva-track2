#!/usr/bin/env bash
# Regenerates native-image inputs from their original sources.
#
# NON-DESTRUCTIVE by default: existing files are kept (the committed set pins
# the 2026-09-22 fetches that the shipped figures derive from). To refresh,
# point OUT at a scratch directory:
#     OUT=/tmp/native_fresh ./fetch_native.sh
# Reactome revises layouts between releases; a fresh fetch is EXPECTED to
# differ from the archived set. The `dbId`/`stableId` inside each diagram JSON
# plus the file date pin which release a given set came from.
#
# The reproducibility check for the figures does NOT need this script:
# run `python3 make_readable.py <stId> <outdir>` against the archived inputs
# and compare with the committed PNGs.
set -euo pipefail
UA="Mozilla/5.0 (BUB1B native image pull)"
OUT="${OUT:-.}"

get() { # url dest
  local f="$OUT/$2"
  if [ -e "$f" ]; then echo "keep $f"; return 0; fi
  mkdir -p "$OUT"
  curl -s -A "$UA" "$1" -o "$f"
  echo "fetched $f"
}

for st in R-HSA-68877 R-HSA-69620 R-HSA-5663220; do
  pn=${st//-/_}
  get "https://reactome.org/ContentService/exporter/diagram/$st.png"            "reactome_${pn}.png"
  get "https://reactome.org/ContentService/exporter/diagram/$st.png?flg=O60566" "reactome_${pn}_flg_BUBR1.png"
  get "https://reactome.org/download/current/diagram/$st.json"                  "diagram_${st}.json"
  get "https://reactome.org/ContentService/data/participants/$st"               "participants_${st}.json"
done

get "https://cdn.rcsb.org/images/structures/6jkk_assembly-1.jpeg" rcsb_6jkk_assembly1.jpg
get "https://cdn.rcsb.org/images/structures/6jkm_assembly-1.jpeg" rcsb_6jkm_assembly1.jpg
get "https://www.ebi.ac.uk/pdbe/static/entry/6jkk_deposited_chain_front_image-200x200.png" pdbe_6jkk_front_200.png
get "https://www.ebi.ac.uk/pdbe/static/entry/6jkm_deposited_chain_front_image-200x200.png" pdbe_6jkm_front_200.png
get "https://alphafold.ebi.ac.uk/files/AF-O60566-F1-confidence_v6.json" alphafold_o60566_confidence_v6.json
