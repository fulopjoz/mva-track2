# Pharmacochaperone literature, Wave 2 (2026-09-08)

Extends `PHARMACOCHAPERONE_LIT.md` (wave 1). Sources of this wave:
a premium full-text and citation-graph deep dive (scite.ai), PubMed perimeter /
GEO / trials-freshness searches, seven open-access full texts (three paywall-logged),
and a local Zotero collection (10 items).

## 1. What wave 2 changed versus wave 1

1. **Rezatapopt phase corrected down.** Wave 1's "registrational phase 2" was
   overstated: PYNNACLE NCT04585750 remains Phase 1/2, Recruiting (registry
   updated 2026-08-07; Phase 2 monotherapy portion enrolling), plus a NEW Phase 1b
   rezatapopt+azacitidine combo NCT06616636 (Recruiting since 2025-01-30). No
   phase 3 record exists.
2. **The ATP-pocket-occupancy idea now carries its own falsifier on record.**
   Suijkerbuijk 2012 (PMID 22698286) reports
   that **AMP-PNP/Mg2+ did NOT stabilize the recombinant BubR1 kinase domain**.
   Pocket occupancy alone is insufficient. The surviving concept is
   occupancy-plus-conformational-repair, whose quantitative template is p53
   Y220C: PC14586 lifts Y220C-DBD Tm from ~34 C to ~42 C, i.e., to WT level
   (Vu 2024, PMC11726359; Puzio-Kuter 2025, PMC12130801).
3. **Catalysis contradiction logged honestly.** Huang 2019 (PMID 31201382)
   finds measurable catalytic activity in human WT BubR1 (K795A/D911A lower
   kcat/Km 5.1x/10x), contradicting the pure-pseudokinase reading of
   Suijkerbuijk. Consequence: classic ATP-competitive inhibitors are an
   **anti-class** again; only non-inhibitory stabilizer binders serve the concept.
4. **No experimental human BubR1 kinase domain structure exists, confirmed by
   coordinate parsing.** 5KHU/5LCW/6TLJ (MCC-APC/C cryo-EM, Yamaguchi 2016,
   Alfieri 2016/2020) resolve BUBR1 only to residue <=345 (TPR + degron
   fragments). The human AlphaFold model is the only structural view of the
   kinase domain; 6JKK's fly numbering does not discuss the N1002-equivalent
   contact (human BubR1c was SWISS-MODEL'd onto 6JKK in that paper).
5. **Suijkerbuijk details now exact:** stability mutants K795R/A, D882N/A,
   D911N, V793R (+731X, KEN-box); K795A Tm 34.7 C vs WT 39.1 C (intrinsic
   fluorescence, His6 domain aa 721-1044); low temperature (27/33 C) rescues
   levels and checkpoint function. The cold-rescue datum is direct support that
   conformational stabilization restores function in this protein.
6. **Lequeue 2025 validation chain corrected:** 30/2,320 FDA-drug hits at
   >=3-fold, validated by bacterial-lysate dose-response + CB-Dock docking ONLY.
   No DSF, no mammalian cells. Thinner than wave 1 implied; usable as a methods
   shape, not as a rigor model.
7. **Operational ddG rubric with citation mass:** Tokuriki 2007 cited by 435
   papers (382 contexts); citing literature operationally uses >1 to >3 kcal/mol
   cutoffs, with **>3 kcal/mol = "highly/severely destabilizing"** the commonest
   rubric (5 documented examples). Our FoldX gate now has a citable threshold.
8. **Two near-precedents for pocket-mediated pseudokinase stabilization** (from
   the paperclip perimeter): STRADA type-II binders (Smith et al. 2021, PMID
   33440120) and the ATP-pocket conformation-stabilization argument (Claus et
   al. 2013, PMID 23863183).
9. **Novelty claim hardened:** the pseudokinase x pharmacological-chaperone
   intersection returned EMPTY across three PubMed queries (logs dated
   2026-09-08). "First pharmacochaperone screen for a pseudokinase interface"
   is the defensible wording.

## 2. Concept statement as it now stands

Concept: rescue functional BubR1 abundance from the N1002K allele via a small
molecule that binds the kinase domain and restores folding stability, without
inhibiting its residual catalytic role. Site logic: N1002K destabilizes a
semi-buried, conserved packing contact (SASA 26.8 A^2 total, 15.9 A^2 side
chain, 15 of 16 non-local contact atoms to residues 977/978; pLDDT 91) - the
mechanism site. Intervention surface: the ATP pocket, on two conditions (a)
the binder must thermally stabilize, not merely occupy (AMP-PNP negative
datum), and (b) it must not act as a catalytic inhibitor (Huang contradiction).
Decision gates: FoldX ddG(N1002K) against the Tokuriki rubric (>3 kcal/mol =
severe); in-silico screen (Glide funnel on the 6,050 approved-drug library,
GNINA cross-check) cannot crown a winner alone; the experiment that decides is
thermal stabilization of a recombinant kinase-domain construct.

## 3. Assay feasibility (the DSF gate)

No recombinant BUB1B kinase-domain dataset exists anywhere (GEO/bioRxiv/PMC
searches dated 2026-09-08, NOT-FOUND). The DSF assay therefore requires de-novo
protein production; closest platform templates are the Demirci-group 2025
bioRxiv kinase-domain pipelines. Readout design copies the p53 validated
template: baseline Tm of the destabilized domain, rescue delta of >=2 C as a
first-pass hit criterion (PC14586 rescued ~8 C; K795A sits 4.4 C below WT).

## 4. Trial watchlist (as of 2026-09-08)

| Compound | Trial | Phase | Status | Class relevance |
|---|---|---|---|---|
| rezatapopt (PC14586) | NCT04585750 (PYNNACLE) | 1/2 | Recruiting | intracellular corrector benchmark |
| rezatapopt + azacitidine | NCT06616636 | 1b | Recruiting | combo expansion |
| ambroxol (GBA1) | NCT05778617 (ASPro-PD) | 3 | Recruiting (1,260 mg/day) | chaperone-with-caveat |
| tezacaftor | NCT02516410 | 3 | Completed | corrector class sanity |
| ambroxol Gaucher | NCT03950050 | - | Completed | chaperone dose precedent |

## 5. Anchor-source integrity

Five most-cited wave-1 anchors crosschecked (Suijkerbuijk 2012 Hughes 2017,
Van Goor 2011, Okiyoneda 2024, Huang 2019): no retractions, expressions of
concern, or errata. Two author-field misattributions were
caught and corrected during the verification pass itself.

## 6. Remaining gaps wave 2 could not settle

1. Vertex's proprietary corrector screen size (not peer-reviewed-disclosed).
2. GNINA-as-chaperone-screen novelty (unpublishable negative; "first" stays
   confined to pseudokinases).
3. Any BUB1B N1002K-specific functional datum (none exists anywhere).
4. Cyske 2024, Lequeue 2025, Tokuriki 2007 remain paywalled (logged with exact
   API response classes logged in-session).
5. BUB1B kinase-domain recombinant expression feasibility (no protocol located;
   blocker for the DSF gate).

## Verdict

Gate-0 memo remains warranted: the concept is literature-anchored,
falsifiable at defined gates, novel in the defensible sense, and now carries
its best counterarguments on record. It does NOT enter the submission.
