# Wave-2 Adversarial Review - revisions R1–R5 to the Track-2 evidence pack

**Reviewer:** AdversarialKimi (out-of-family red team) · **Date:** 2026-09-05
**Scope:** R1–R5 consensus revisions against TRACK2_ATTACK_MAP.md and the four wave-2 documents.
**Sources actually read in full:** TRACK2_ATTACK_MAP.md; wave2_NonsenseAxis.md; wave2_StabilizationAxis.md;
wave2_SenolyticAxis.md; wave2_CINSyndromeAxis.md. External spot-verifications via PubMed/PMC are
noted per finding with DOI links (PubMed was used for those lookups - attribution per NCBI terms).
**Headline:** No BLOCKER found. No revision flips on the evidence as written. Every revision survives
only with conditions; the weakest links are (i) the un-analyzed allele non-specificity and
boundary-arithmetic optimism behind R2, (ii) a live cross-document contradiction (SIRT2/NAD+)
under R3, and (iii) an overbroad precedent claim behind R5 (Lynch/CAPP2).

## Verdicts per revision

| Revision | Verdict | Basis |
|---|---|---|
| R1 - demote readthrough/ataluren | **ACCEPT-WITH-CONDITIONS** | Direction correct; the arithmetic statement "does not bridge the 6→13% gap" is corner-false (F3) and f_escape is modeled as fixed when the cited class itself perturbs it. Reword, keep demotion. |
| R2 - promote ASO exon-17 skipping to dominant allele-level strategy | **ACCEPT-WITH-CONDITIONS** | Correct as a research-ordering *conditional on product function*; the revision text as circulated drops that conditional force ("⇒ +13–15%", "modules retained") while the wave doc itself gates everything on the Δ716-761 construct. Allele non-specificity never modeled (F1); KARD boundary arithmetic off by one residue (F2). |
| R3 - arimoclomol conditional adjunct only | **ACCEPT-WITH-CONDITIONS** | Sound for arimoclomol itself (safety Established, efficacy gap honest, HSF1 flag handled correctly). Condition: reconcile the unresolved SIRT2/NAD+ node that StabilizationAxis omits but SenolyticAxis cites as in-vivo proof (F4) - the "exactly one feasible node" completeness claim is false. |
| R4 - senolysis gate-first research priority | **ACCEPT-WITH-CONDITIONS** | Grading matches its own evidence (single-lab, 15 y unreplicated, zero human MVA data). Condition: add the omitted oncologic-safety objection - senescence of aneuploid cells is tumor-suppressive - to Gate 0 and the decision rule (F6). |
| R5 - "no approved CIN/constitutional cancer-risk preventive exists" frame | **ACCEPT-WITH-CONDITIONS** | True only after scoping to *chromosomal*-instability syndromes. As written it is contradicted by CAPP2 aspirin in Lynch syndrome (genomic-instability disorder, RCT-proven, guideline-recommended) and qualified by everolimus-TSC (approved mechanism-matched drug in a tumor-predisposition syndrome) (F7). |

---

## Numbered findings (severity / claim / evidence / failure mode / falsification test)

### F1 - MAJOR (load-bearing for R2): allele non-specificity of exon-17 skipping is never modeled
- **Claim:** "Even 25–30% skipping of one allele adds ~13–15% of WT total abundance, crossing the competence line arithmetically" (wave2_NonsenseAxis.md §c).
- **Evidence:** A splice-switching ASO targets the exon-17 splice junctions, which are sequence-identical in both transcripts; the L737Ter lesion sits *inside* exon 17 and confers no junction selectivity. Exon 17 will therefore be skipped on the N1002K (hypomorph) allele as well, at the same efficiency s. No document models this.
- **Failure mode / corrected math:** Let baseline hypomorph contribution be b = 5–10%. With skipping s on both alleles: unskipped hypomorph residual = (1−s)·b; null-allele restoration = 0.5·s·q, where q ∈ [0,1] is the unknown stability/function factor of the Δ716-761+E715G product. If q ≈ 1: total ≈ (1−s)·b + 0.5·s - at s=0.25, b=5%: 3.75+12.5 = 16.25% (crosses, but *below* the doc's 17.5% one-allele figure, and closer to threshold if b-decay over-titrates). If q ≈ 0: total = (1−s)·b - worse than doing nothing, for any s. The single-allele model thus **overstates the benefit in the good case and hides the harm in the bad case**; both tails sharpen the same conclusion (the construct-function assay is the whole game), but the arithmetic in the pack is the wrong arithmetic.
- **Falsification test:** ddPCR of the skipped junction in patient cells (will confirm both-allele skipping); model q ∈ {0, 0.5, 1} × s grid explicitly in candidates.tsv before any "dominant strategy" wording ships.

### F2 - MAJOR (load-bearing for R2): KARD retention claim is off by one residue
- **Claim:** "the commonly cited KARD span ends at ≈716, so the deletion clips at most its extreme C-terminal residue" (wave2_NonsenseAxis.md §c, flagged INFERENCE by its authors).
- **Evidence:** The deletion removes residues 716–761 *and* substitutes E715G at the junction (the doc's own verified geometry). Under the cited boundary (span ending at 716), residue 716 is *deleted* and residue 715 is *substituted* - i.e., the C-terminal **two** residues of the defined KARD span are altered, not "at most" one.
- **Failure mode:** "Error-correction modules retained" is stated in R2 without this arithmetic; if KARD's terminal residues contribute to PP2A-B56 docking or K-fiber regulation, the Δ716-761 product could be abundant-and-abundant-but-defective in exactly the module the argument relies on. (The LxxIxE core at ~664–678 and S670/S676 are indeed N-terminally intact - that part of the claim survives.)
- **Falsification test:** assay #4 in the wave doc (PP2A-B56 co-IP + phospho-S670/S676 on the skipped product) settles it empirically; before that, R2's revision text must carry the wave doc's conditional ("IF the Δ716-761 product works"), not a bare "⇒".

### F3 - MAJOR (arithmetic audit, R1): the "does not bridge" statement is false at the optimistic corner; f_escape is not a fixed parameter
- **Claim:** "Best-case modeled contribution is ≈ +0.3–3% of WT BubR1 - it does not bridge the ~6→13% gap alone" (wave2_NonsenseAxis.md, verdict table; propagated verbatim into R1).
- **Evidence:** The doc's own model puts baseline at 5–10%. Double-optimistic corner: 10% + 3% = 13% - touches the competence line exactly. The categorical "does not bridge" is corner-false. Second flaw: Wangen & Green 2020, cited in the same section, shows aminoglycosides themselves blunt NMD (G418 stabilized PTC-TP53 mRNA 16-fold) - so f_escape is *treatment-dependent* for the glycoside class, not the fixed ≤0.1–0.3 the model assumes. (Ataluren does not share that property, and chronic pediatric glycoside use is correctly ruled out on oto/nephrotoxicity - the demotion still holds; the stated reason is slightly wrong.)
- **Failure mode:** a reviewer running the doc's own numbers finds the counterexample, and the whole demotion reads as motivated. R1 survives on (a) regulatory collapse and (b) unreliability, not on "cannot reach".
- **Falsification test:** none needed beyond the pack's own arithmetic; fix wording to "monotherapy readthrough crosses the threshold only at the joint-optimistic corner; not reliable as a standalone axis; qPCR-gated."

### F4 - MAJOR (cross-document contradiction, R3): SIRT2/NAD+ node omitted from the stabilization scan
- **Claims:** StabilizationAxis: "Exactly one feasible chronic stabilization node exists today: … arimoclomol" (wave2_StabilizationAxis.md, VERDICT). SenolyticAxis: North 2014 (PMID 24825348, [DOI](https://doi.org/10.15252/embj.201386907)) is "a published in-vivo proof that a druggable enzyme-class (SIRT2/NAD⁺) raises BubR1 abundance in living animals … relevant to the N1002K allele class" (wave2_SenolyticAxis.md, Q3a cross-feed note).
- **Evidence:** North 2014 (EMBO J, retrieved via PubMed) reports SIRT2 maintaining/inducing BubR1 with age and NMN treatment raising NAD+/BubR1 and extending healthspan in BubR1^H/H mice - arguably the *only* in-vivo, genotype-matched, druggable abundance datum in the entire pack. StabilizationAxis never analyzes the NAD+/SIRT2 node, yet asserts a completeness claim ("exactly one").
- **Failure mode:** R3's join inherits a false completeness statement; an obvious reviewer question ("what about NMN, which already raised BubR1 in the exact mouse model?") has no answer in the document that owns the question. NAD+ boosters are also trivially child-administrable (supplement-class), which strengthens rather than weakens the omission.
- **Falsification test:** add an S7 node analysis (efficacy evidence vs the hypomorph allele class, pediatric NAD+ data, mechanistic fit of a SIRT2-transcriptional route to an already-expressed N1002K protein) or explicitly de-scope it with rationale. Either closes the contradiction.

### F5 - MAJOR (completeness/consistency of source use; attack map G3-6): the Tang 2011 citation supports the *neutral* node and hides its own positive hits
- **Claim:** "Tang 2011 shows mTORi neutral on aneuploid-cell viability - honest label" (TRACK2_ATTACK_MAP.md, Level 3 tissue-rescue).
- **Evidence:** Verified in full text (Tang, Williams, Siegel & Amon, Cell 2011;144:499–512, PMC3532042, [DOI](https://doi.org/10.1016/j.cell.2011.01.017), retrieved via PubMed/PMC): rapamycin, torin1, and mTOR knockdown "did not inhibit the proliferation of trisomic MEFs nor enhanced the anti-proliferative effects of AICAR (Figure S3)". The claim is **true** - but (a) it rests on a supplemental figure in *mouse* primary MEFs, and (b) the same paper's positive hits - AICAR, 17-AAG, chloroquine, and (weakly) metformin - selectively antagonized trisomic MEFs **and Bub1b^H/H MEFs**. The pack cites this paper for the node it found neutral, and nowhere analyzes the energy-stress (AMPK-axis) selective-kill direction the paper actually demonstrates in a BubR1-hypomorph line. (17-AAG is correctly excluded by the HSP90 collision; chloroquine sits inside the "autophagy-axis not pediatric-justified" closure - but the *AMPK/energy-stress* direction, with metformin as its pediatric-feasible member, is unexamined as clone interception.)
- **Failure mode:** the everolimus rationale (Grade D) is built on the weakest datum of the cited source while the source's strongest genotype-matched datum is unused; a sharp reviewer will find Fig 6A and ask why.
- **Falsification test:** one paragraph in the attack map addressing why AICAR/AMPK-direction selective killing of BubR1-hypomorph cells is or is not a candidate (metformin weak positive in the same system; TODAY pediatric chronic data already in the Senolytic doc). Direction of the map unchanged.

### F6 - MAJOR (missing lethal objection, R4): senescence of aneuploid cells is tumor-suppressive; chronic senolysis may remove an anti-tumor barrier
- **Claim (R4):** senolysis as gate-first research priority; wave doc frames residual risk as treadmill-neutrality/stem-cell depletion (Gap 5).
- **Evidence:** The senolytic doc's own human-cell chain (Santaguida 2017, [DOI](https://doi.org/10.1016/j.devcel.2017.05.022); Wang 2021, [DOI](https://doi.org/10.15252/embr.202052032)) shows mis-segregating cells *arrest senescent* and are NK-cleared - i.e., the senescent state is a brake on aneuploid-lineage expansion. In a constitutional-CIN child, chronically ablating p16+ cells (or senomorphic suppression of senescence entry) removes that brake; the Baker 2008 p16-inactivation arm attenuated progeroid phenotypes but never tested tumor endpoints in the cross. This objection - the pro-tumorigenic direction - appears nowhere in the four documents.
- **Failure mode:** first IRB/oncology reviewer raises it; the pack has no pre-drafted answer.
- **Falsification test:** add to Gate 0 and the n-of-1 decision rule: (i) explicit argument why burden-reduction dominates barrier-removal at measured burden levels, (ii) intensified tumor surveillance as a hard component of any senolytic/senomorphic arm, (iii) pre-specified stopping on any malignancy signal. The gate-first ordering itself survives.

### F7 - MAJOR (accuracy of framing, R5): "no approved constitutional cancer-risk preventive exists" is overbroad as written
- **Claim:** "No drug approved today for prevention in ANY constitutional cancer-risk disorder" (wave2_CINSyndromeAxis.md, Key GAPS #3; propagated into R5) and the verdict's "surveillance-only in 2024" universal.
- **Evidence:** In the syndromes surveyed (AACR 2024, Nakano et al., [DOI](https://doi.org/10.1158/1078-0432.CCR-24-1098)) the claim is correct. But as an unscoped statement it is false: Lynch syndrome - a constitutional genomic-instability disorder (MMR deficiency) - has RCT-proven aspirin chemoprevention (CAPP2: Burn et al., Lancet 2011, [DOI](https://doi.org/10.1016/S0140-6736(11)61049-0); 10-yr follow-up Burn et al., JNCI 2020, [DOI](https://doi.org/10.1093/jnci/djaa102)) now guideline-recommended (NICE NG151). The CIN doc never scanned Lynch. Separately, everolimus-TSC is *approved pharmacology in a constitutional tumor-predisposition syndrome* - the doc's own strongest template - so "no approved drug for the disease in children" wording must also distinguish prevention-of-cancer from treatment-of-lesions.
- **Failure mode:** a submission reviewer quotes CAPP2 back and the "no precedent exists" frame collapses rhetorically even though the scoped point (no approved preventive in *chromosomal-instability* syndromes) stands.
- **Falsification test:** rewrite R5 as "no approved pharmacologic *cancer-prevention* agent exists in any constitutional *chromosomal*-instability syndrome (AACR 2024); the nearest exceptions are aspirin in Lynch (MMR-instability, guideline-recommended) and everolimus in TSC (lesion treatment)" - and add CAPP2 to the precedent table.

### F8 - MINOR (arithmetic rounding): "25–30% skipping ⇒ ~13–15%"
0.5 × 0.25 = 12.5%, not ~13%. The conservative direction of the claim is unaffected (even s ≈ 0.16 crosses from the 5% floor at q=1), but the threshold sentence in R2 should carry exact numbers given how load-bearing the arithmetic is.

### F9 - MINOR (assumption hygiene, R1/R2): product-residue substitutions not propagated into the arithmetic
Roy 2016 (near-cognate insertion) means the readthrough product carries Leu737→(Trp/Cys/Arg-class); the +0.3–3% model implicitly assumes WT-functional product. Symmetrically, E715G function is assumed, not shown. The wave doc mentions both but the abundance arithmetic treats 1 rescued transcript = 1 WT-equivalent unit in both axes. Falsification: allele-specific functional assay; wording fix: "at full product function (assumption)".

### F10 - MINOR (documentation hygiene): leaked generation token in CINSyndromeAxis
The "Should NOT claim" section of wave2_CINSyndromeAxis.md contains the literal string `◁sh|endoftext|▷` - an unreviewed generation artifact inside a submission-bound document. Also a minor formatting slip (an unbalanced parenthesis in "fundable, ethics-defensible design"). Remove both before the consensus vote.

### F11 - MINOR (framing, R5 support): TSC labeled a "CIN-class disorder"
TSC is an mTORopathy/hamartoma syndrome, not a chromosomal-instability disorder; the everolimus analogy is valid by *constitutional tumor-predisposition + mechanism-matched approved drug*, not by CIN. One-word fix ("constitutional tumor-predisposition analog") prevents a trivially-attacked mislabel.

### F12 - MINOR (human-data scoping): Matsuura 2006 is a monoallelic-PCS cohort
"Human MVA BUB1B nonsense transcripts are measured significantly reduced (Matsuura 2006)" - the cohort is seven monoallelic-PCS families. Correct as NMD evidence for human BUB1B nonsense transcripts; imprecise as "MVA" characterization. Suijkerbuijk 2010/Hanks 2004 remain the MVA-appropriate citations. Falsification: check Matsuura cohort definition (Am J Med Genet A 140:358).

### F13 - MAJOR (real-world deliverability, R2/R3; checklist item 6): IP/FTO and reimbursement are absent from every candidate
No document addresses freedom-to-operate (PMO chemistry historically Sarepta-dominated; 2'MOE-PS patterned by Ionis; bespoke n-of-1 ASO manufacturing was philanthropically financed for milasen), nor cost/reimbursement for a weekly-IV chronic pediatric PMO (DMD-class pricing ≈ $10^5–10^6/yr) in a patient with no approved indication. Not fatal to the scientific ordering, but candidates.tsv will inherit a silent consensus that delivery+chemistry are the only constraints when a third - pay-forability - is unexamined. Falsification: one FTO/funding-parity paragraph per allelic candidate, citing the milasen precedent as the de-risked path.

---

## What survives contact unchanged (no edit warranted)

1. **NMD geometry for the L737Ter PTC** (75 nt > 50–55 nt rule; 6 downstream EJCs; Lindeboom categories all fail) - internally consistent, correctly hedged, decision-grade.
2. **The HSP90-inhibitor collision** (genotype-specific contra-indication of Axis-a) - stands; celastrol correctly folded into the same collision class by StabilizationAxis.
3. **Direction of the skipping arithmetic** - threshold crossing at modest s is robust to every parameter except the flagged one (product function); the model is *conservative*, not inflated, once rounding (F8) is fixed.
4. **R3's arimoclomol structure** (pediatric safety Established; kinase-client efficacy = pivotal gap; HSF1–Cdc20 hazard as a disclosed flag, not a stopper) - correctly calibrated; the 5-year NPC exposure record with no neoplastic signal is fairly weighed against single-lab overexpression data.
5. **R4's replication audit** (BubR1×INK-ATTAC single-lab, 15 y, PubMed-verified negative queries recorded) and the Gate-0-first design - methodologically the strongest of the four documents.
6. **Everolimus as the only chronically pediatric-feasible mTOR node** (EXIST RCT safety; Grade-D mechanism honestly labeled) - the conclusion survives even though its supporting citation record needs the F5 fix.
7. **The coordinate correction Δ690-737 → Δ716-761+E715G** - an honest supersession that improves the map; exactly how flagged corrections should propagate.
8. **The five-assay validation plan** - each gate is correctly decision-critical; wave-2 additions (Δ716-761 construct panel #3, B56/phospho checks #4, chaperone-limitation assay #5, senescence Gate 0) integrate cleanly.
9. **Celecoxib-FAP handled as a two-sided precedent** - correct; the only precedent-scan omission is CAPP2/Lynch (F7).
10. **No retracted/corrected sources located in load-bearing positions; human-vs-mouse flags are consistently carried in all four wave docs** (checked against in-line species tags; no human/mouse conflation or data-swap found).

## Recommended actions before the consensus vote (ordered)

1. Fix R2 wording to preserve the "IF the Δ716-761 product works" conditional; add the both-allele skipping model (F1) and correct the KARD retention sentence (F2).
2. Reword R1's arithmetic sentence per F3 ("crosses only at the joint-optimistic corner; unreliable and superseded").
3. Resolve the SIRT2/NAD+ node (F4) - analyze or de-scope - so StabilizationAxis's "exactly one node" claim does not contradict SenolyticAxis's own cross-feed.
4. Add the F6 oncologic-safety objection to the R4 gate criteria; add CAPP2/Lynch + TSC scoping to R5 (F7); fix mTORi citation context (F5).
5. Add FTO/reimbursement paragraphs per candidate (F13); scrub the leaked token (F10).

*Verification note: PubMed and PMC were used to verify Tang et al. 2011 (PMID 21315436, [DOI](https://doi.org/10.1016/j.cell.2011.01.017)) and its comment record (Manchado & Malumbres, [DOI](https://doi.org/10.1016/j.cell.2011.01.037)); all other citations were assessed against the wave documents' own claims and flags, not re-fetched.*
