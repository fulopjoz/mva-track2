# Native image provenance

All URLs live-fetched 2026-09-22. Highlight variants were exported with the
Reactome `flg=O60566` selection flag. **Controls:** (1) the exporter is
deterministic — two unflagged fetches of the same diagram are byte-identical
(delta sum 0, 0 diff clusters), so flag-vs-plain pixel differences are real
render changes, not timestamps or noise; (2) cross-checking the diff clusters
against node geometry from https://reactome.org/download/current/diagram/{stId}.json
shows the flagged regions do NOT correspond to a drawn BUBR1 node on
R-HSA-68877 or R-HSA-5663220 — BUB1B is never a standalone node in those two
diagrams; Reactome flags it through component membership in kinetochore
complexes (per diagram JSON node names intersecting each cluster:
"Kinetochore", "Microtubule-bound kinetochore",
"Kinetochore:CDC42:GTP:DIAPH2-2"). On R-HSA-69620 the flag DOES cover the
explicitly drawn entities (verified against diagram JSON): the `BUB1B`
protein node, `hBUBR1:hBUB3:MAD2*:CDC20 complex` (the MCC), and
`MCC:APC/C complex` — those panels are starred (*) in the readable set.

An earlier revision of this file claimed the diff clusters proved "BUBR1
diagram occurrences" on all three diagrams; withdrawn 2026-09-23 in favor of
the complex-level statement above.

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

## Derived zoom set (`readable_*.png`) — built 2026-09-23

- `readable_<stId>_overview.png`: full native diagram with numbered markers at
  the `flg=O60566` render regions.
- `readable_<stId>_zoom.png`: 90-px-padded crops of those regions at
  4x max scale; per-panel node names and explicit-BUB1B star marks come from
  the diagram JSON geometry, not from the diff pixels.
- `diagram_<stId>.json`: Reactome diagram layout JSON used for the node
  geometry (source: https://reactome.org/download/current/diagram/{stId}.json).
