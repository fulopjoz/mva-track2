# Native image provenance

All URLs live-fetched 2026-09-22; verification and the readable zoom set built
2026-09-24. Highlight variants were exported with the Reactome `flg=O60566`
selection flag.

**Verification chain (each step independently checkable):**

1. **Exporter determinism (negative control, 2026-09-24).** Two unflagged
   fetches of R-HSA-68877 are byte-identical (delta sum 0, 0 diff clusters) —
   the exporter is deterministic, so flag-vs-plain differences are real render
   changes, not timestamps or noise.
2. **O60566 membership (authority: participants endpoint).**
   `/ContentService/data/participants/{stId}` (raw responses committed as
   `participants_*.json`) lists uniprot:O60566 BUB1B as a component of:
   - R-HSA-68877: 7 complexes — Kinetochore (375305), Microtubule-bound
     kinetochore (375303), three Ac-Cohesin:…:Kinetochores:Microtubules
     cohesin complexes (2468282/2484819/2500242, plus p-STAG2,RAD21 variant
     1638796), p-S274,S326-NUDC:EML4:Microtubule-bound kinetochore (9648124);
     **BUB1B is never drawn as a standalone node in this diagram** (diagram
     JSON name search).
   - R-HSA-5663220: 4 complexes — 375303, 375305, Kinetochore:CDC42:GTP:
     DIAPH2-2 (5666131), Kinetochore:CDC42:GTP:p-S196-DIAPH2-2 (5666161);
     likewise no standalone BUB1B node.
   - R-HSA-69620: 7 entities including the explicitly drawn `BUB1B` protein
     (141436), `hBUBR1:hBUB3:MAD2*:CDC20 complex` (141440, the MCC),
     `MCC:APC/C complex` (141410), Mad1:kinetochore complexes and
     Kinetochore (375305).
3. **Flag-diff coincidence (cross-check of 1 against 2, with null baselines).**
   Diff clusters (>30 RGB channel sum, >200 px) mapped onto diagram-JSON node
   geometry via an extent-fit scale (approximate, ±120 model units tolerance).
   Baseline = fraction of 1000 random 150-unit boxes landing on the same
   verified node set; p = one-sided binomial test vs that baseline:
   - R-HSA-69620: **12/12 coincide** (incl. the explicit BUB1B/MCC nodes)
     vs baseline 10.7% — p ≈ 2e-12. Decisive.
   - R-HSA-5663220: **4/4 coincide** vs baseline 38.6% — p = 0.022.
     Significant.
   - R-HSA-68877: 8/10 coincide vs baseline 58.6% — p = 0.15. The diagram is
     so dense in large kinetochore containers that this test carries no
     discriminative power; on this diagram the kinetochore membership in
     step 2 (participants endpoint) — not pixel coincidence — is the evidence
     that the flagged regions are BUB1B-containing complexes. **2 unexplained
     clusters** (≈model coordinates 59,52 and 430,77, near the "Mitotic
     Prophase" and "S Phase" compartment labels, which contain no O60566
     component) — recorded as unexplained, not folded into the story.

Conclusion: flag-vs-plain differences mark **BUB1B-containing complexes**
(never a larger claim). An earlier revision of this file called the clusters
"BUBR1 diagram occurrences"; withdrawn 2026-09-24 in favor of the
complex-level statement above, which is what the three-step chain supports.

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

## Derived zoom set (`readable_*.png`) — built 2026-09-24

- `readable_<stId>_overview.png`: full native diagram with numbered markers at
  the `flg=O60566` render regions.
- `readable_<stId>_zoom.png`: 90-px-padded crops of those regions at
  4x max scale. Crop boxes come from the flg-vs-plain diff clusters; per-panel
  node names and the explicit-BUB1B star are assigned by intersecting each crop
  with diagram-JSON node boxes (extent-fit transform) — star = crop contains a
  BUB1B/hBUBR1/MCC node per step 2, names = diagram nodes inside the crop.
- `diagram_<stId>.json`: Reactome diagram layout JSON used for the node
  geometry (source: https://reactome.org/download/current/diagram/{stId}.json).
- `participants_<stId>.json`: participants-endpoint responses used for step 2.
- `participants_<stId>.json` and `diagram_<stId>.json` are regenerated by
  `fetch_native.sh`; zoom sheets are rebuilt by `make_readable.py`.
