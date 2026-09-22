# Native image provenance

All URLs live-fetched 2026-09-22. Highlight variants were exported with the
Reactome `flg=O60566` selection flag; each flagged export was pixel-diffed
against its unflagged twin and the differences resolve to compact localized
clusters at BUBR1's diagram occurrences (10 clusters on R-HSA-68877,
22 on R-HSA-69620) — the highlight is real, not a metadata artifact.

## Reactome ContentService diagram exporter — CC-BY 4.0, cite Reactome (PMID 34788843)

| File | Source |
|---|---|
| `reactome_R_HSA_68877.png` (Mitotic Prometaphase) | https://reactome.org/ContentService/exporter/diagram/R-HSA-68877.png |
| `reactome_R_HSA_68877_flg_BUBR1.png` | same URL, `?flg=O60566` |
| `reactome_R_HSA_69620.png` (Cell Cycle Checkpoints — diagrammed parent of the SAC arm) | https://reactome.org/ContentService/exporter/diagram/R-HSA-69620.png |
| `reactome_R_HSA_69620_flg_BUBR1.png` | same URL, `?flg=O60566` |
| `reactome_R_HSA_5663220.png` (RHO GTPases Activate Formins) | https://reactome.org/ContentService/exporter/diagram/R-HSA-5663220.png |
| `reactome_R_HSA_5663220_flg_BUBR1.png` | same URL, `?flg=O60566` |

Note: the core SAC sub-pathways (R-HSA-141430, R-HSA-141444, R-HSA-141405) and
R-HSA-69618 (Mitotic Spindle Checkpoint) carry `hasDiagram=false`; R-HSA-69620
is the nearest diagrammed ancestor covering the checkpoint events.

## RCSB PDB / PDBe — free to reuse with attribution

| File | Source |
|---|---|
| `rcsb_6jkk_assembly1.jpg` | https://cdn.rcsb.org/images/structures/6jkk_assembly-1.jpeg |
| `rcsb_6jkm_assembly1.jpg` | https://cdn.rcsb.org/images/structures/6jkm_assembly-1.jpeg |
| `pdbe_6jkk_front_200.png` | https://www.ebi.ac.uk/pdbe/static/entry/6jkk_deposited_chain_front_image-200x200.png |
| `pdbe_6jkm_front_200.png` | https://www.ebi.ac.uk/pdbe/static/entry/6jkm_deposited_chain_front_image-200x200.png |

6JKK = track-2 evidence crystal; 6JKM = Gate-0 docking structure. Same fly
BubR1 kinase domain, different crystals — keep their provenance distinct.

## AlphaFold DB — CC-BY 4.0

| File | Source |
|---|---|
| `alphafold_o60566_confidence_v6.json` | https://alphafold.ebi.ac.uk/files/AF-O60566-F1-confidence_v6.json |
| `alphafold_o60566_plddt.png` | per-residue pLDDT plotted from that JSON (matplotlib); residues 737 and 1002 marked |

AFDB serves no native images; the pLDDT strip is the only image-grade
derivative and renders only values present in the official confidence file.
