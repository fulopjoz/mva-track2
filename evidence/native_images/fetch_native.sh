#!/usr/bin/env bash
# Regenerates all raw native-image inputs from their original sources.
# Run in this directory. Then: for st in R-HSA-68877 R-HSA-69620 R-HSA-5663220; do
#   python3 make_readable.py $st; done
set -euo pipefail
UA="Mozilla/5.0 (BUB1B native image pull)"

for st in R-HSA-68877 R-HSA-69620 R-HSA-5663220; do
  pn=${st//-/_}
  curl -s -A "$UA" "https://reactome.org/ContentService/exporter/diagram/$st.png" \
    -o "reactome_${pn}.png"
  curl -s -A "$UA" "https://reactome.org/ContentService/exporter/diagram/$st.png?flg=O60566" \
    -o "reactome_${pn}_flg_BUBR1.png"
  curl -s -A "$UA" "https://reactome.org/download/current/diagram/$st.json" \
    -o "diagram_${st}.json"
  curl -s -A "$UA" "https://reactome.org/ContentService/data/participants/$st" \
    -o "participants_${st}.json"
done

curl -s -A "$UA" "https://cdn.rcsb.org/images/structures/6jkk_assembly-1.jpeg" -o rcsb_6jkk_assembly1.jpg
curl -s -A "$UA" "https://cdn.rcsb.org/images/structures/6jkm_assembly-1.jpeg" -o rcsb_6jkm_assembly1.jpg
curl -s -A "$UA" "https://www.ebi.ac.uk/pdbe/static/entry/6jkk_deposited_chain_front_image-200x200.png" -o pdbe_6jkk_front_200.png
curl -s -A "$UA" "https://www.ebi.ac.uk/pdbe/static/entry/6jkm_deposited_chain_front_image-200x200.png" -o pdbe_6jkm_front_200.png
curl -s -A "$UA" "https://alphafold.ebi.ac.uk/files/AF-O60566-F1-confidence_v6.json" -o alphafold_o60566_confidence_v6.json

echo "done; run check that each PNG starts with the magic bytes before use."
