# Structural validation of the N1002 interface - AF model cross-checked against experiment

Question (raised by internal review): is the AlphaFold-predicted helix↔β-element packing
interface at N1002 real, or a modeling artifact?

## 1. No human BUB1B kinase-domain structure exists
RCSB query keyed on UniProt O60566 returns 9 entries (2WVI, 3SI5, 4GGD, 5JJA, 5K6S,
5KHU, 5LCW, 5SWF, 6TLJ). Entity-by-entity coverage check: **every experimental
human BUB1B structure covers only N-terminal/middle fragments** (residues 20–42,
57–164, 647–720) - none reaches the kinase domain (766–1050). The AlphaFold v6
model is therefore the best available human structural evidence (recorded, not assumed).

## 2. Closest experimental structure: 6JKK (Drosophila BubR1 kinase domain)
- Fragment: chain A, dm BubR1 residues 1126–1459 (334 CA), X-ray crystal structure.
- Fragment-anchored local alignment, human window 960–1015 vs fly fragment:
  **55 aligned columns, 16/55 identical (29%), score 54 (BLOSUM62, local)**.
- Two independent alignments (full-length and fragment-anchored) agree on all anchors,
  incl. **dm1419 = hs N1002 (N, identical)**, dm1418 = hs L1001 (identical),
  dm1395 = hs W978 (identical); other aromatics (W973/F977) not sequence-conserved in fly.

## 3. Coordinate test in 6JKK - interface is geometrically conserved
- Fly segment 1413–1421 (mapping from hs helix 996–1003) is genuinely helical in the
  crystal: CA i→i+3 = 5.29–5.54 Å (canonical α-helix; the 1418→1421 rise of 9.86 Å
  marks the helix exit, matching the human C-cap geometry).
- Contacts: fly-N-eq 1419 → fly-1395W at **2.86 Å** and fly-1394I at 3.60 Å;
  fly-1395W also packs the helix at 1414/1415/1418 (≤5 Å).
- I.e., **in the experimental crystal structure, the residue equivalent to human N1002
  packs directly against the conserved aromatic residue equivalent to W978** - the same
  interface the human AF model predicts.
- Cα superimposition of the 9-residue helix pair (hs 996–1004 vs fly 1413–1421):
  **RMSD 0.74 Å**.

## Verdict
The N1002 helix↔aromatic-cluster packing interface is real and conserved across
~600 Myr (human AF model vs fly crystal structure). The position is a conserved
structural anchor; N1002K plausibly disrupts a tight Asn NH2–Trp packing contact
(charge inversion into a hydrophobic/aromatic interface) - consistent with the
AlphaMissense 0.9229 likely-pathogenic score and the whole-position constraint
(only Ser near-tolerated).

Provenance: AF-O60566-F1-model_v6.pdb (AlphaFold DB); 6JKK.cif (RCSB);
UniProt A1Z6I7/O60566 sequences; analysis via biotite (local, reproducible).
