# Wave-3 Adversarial Review - PASS 2 (convergence pass)

**Reviewer:** AdversarialKimi2 (out-of-family red team, same reviewer lineage as pass 1) · **Date:** 2026-09-05
**Scope:** controller-integrated `TRACK2_ATTACK_MAP.md` v2 + five wave-3 docs
(`wave3_PrecedentCensus.md`, `wave3_AMPKaxis.md`, `wave3_ASOdeep.md` + `q7a_sequence_analysis.md`,
`wave3_ImmunoSurveillanceNK.md`, `wave3_SenolysisF6verifier.md`), `candidates.tsv` (`consensus_status`),
`SCOPE_DECISION.md`, `wave2_ADVERSARIAL_REVIEW.md` (my 13 pass-1 conditions), `WORKFLOW_CONSENSUS.md` (seam).
**Attacks run per checklist:** A integration fidelity · B condition compliance (all 13) · C new-evidence
spot-verification · D cross-seam consistency · E residual omissions.
External spot-checks: PubMed metadata re-fetch of the four newest/most load-bearing identifiers
(PMIDs 42425127, 42227334, 41477861, 33931486) - all four REGISTRY-VALID and content-matched
**except one conclusion-level overstatement found (finding P2-2)**. According to PubMed (NCBI E-utilities), the four records and their DOIs are:
CAPP3 first results - [DOI](https://doi.org/10.1016/S2468-1253(26)00114-7) · n-Lorem - [DOI](https://doi.org/10.1093/nar/gkag504) · Lalinde-Gutiérrez - [DOI](https://doi.org/10.1126/sciadv.adx2988) · Besson 2021 J Immunol - [DOI](https://doi.org/10.4049/jimmunol.2001215). Pass-1's own verification of Tang 2011 ([DOI](https://doi.org/10.1016/j.cell.2011.01.017), PMC3532042) is re-used.

---

## STOP-RULE METRIC

**MAJOR findings this pass: 2** (P2-1, P2-2) · **BLOCKERS: 0** · **MINOR: 7**

Neither major flips any candidate disposition; both are citation-attribution/framing errors
in submission-facing sentences, both are one-paragraph fixes, and both live at the most
weakly-reviewed layer the checklist predicted (controller integration + the census's
"scope-safe" sentence). The stop rule is not triggered by disposition risk here; it is
triggered by shipping-precision. The validation plan and candidate order stand.

---

## Per-target verdicts

| Target | Verdict |
|---|---|
| A. Integration fidelity | **HELD WITH TWO CORRUPTIONS** - AMPK closure, senolysis rules, ASO sequence numbers, and the census scope logic are integrated faithfully (numbers verified cell-by-cell against q7a). One controller-layer re-corruption (P2-1) and two compression losses (minors P2-6, P2-8). |
| B. Pass-1 condition compliance | **11/13 fully honored** (F1, F2, F4, F5, F6, F7, F9, F10, F11, F12, F13). **F3 partially honored** (rationale fixed, corner-false slogan retained; f_escape limb never integrated). **F8-honoring introduced a new arithmetic slip** (16–20 % band excludes its own top corner = 22 %). |
| C. New evidence accuracy | Identifiers: 4/4 spot-checked registry-valid with content matched. Conclusions: CAPP3 overstatement (P2-2). Ovadya counted in a tumor-outcome census it has no tumor endpoint for (minor). |
| D. Cross-seam consistency | attack map ↔ candidates.tsv: consistent on every candidate row. attack map ↔ SCOPE_DECISION: "PRIMARY: ASO" vs O1 named-candidate framing needs the decision doc's own scheduled re-run (minor). Governance record: pass-1 major count misrecorded (minor). |
| E. Residual omissions | Base/prime editing deferral is recorded (WORKFLOW_CONSENSUS line 48) and I AGREE with it - the Q7b delivery census applies a fortiori to RNP delivery in a constitutional child. Remaining honest gaps: pediatric anchor for the rapalog "Mannick-window floor" (never named); Q8's Gate-0 immune panel not integrated; CNS second-program point compressed out. |

---

## Numbered findings

### P2-1 - MAJOR (checklist A, controller-layer integration drift): Tang 2011 attribution re-corrupted into the everolimus row
- **Claim (attack map v2, Level 3):** "Tang 2011 neutral on Bub1b^H/H MEFs - verified in full
  text." Repeated in `candidates.tsv` (rapamycin/everolimus row: "Grade-D rationale kept honest
  (Tang 2011 neutral on Bub1bH/H)").
- **Evidence:** Tang's mTOR-perturbation arms (rapamycin, torin1, mTOR knockdown, Fig S3) were run
  on **trisomic** MEFs, not on Bub1b^H/H cells - my pass-1 verification of the full text and the
  wave-3 AMPK doc agree on this verbatim (wave3_AMPKaxis §1.1: "Rapamycin, torin1, mTOR knockdown:
  NEUTRAL - did not inhibit trisomic-MEF proliferation (Fig S3)"; §1.3: the only Bub1b^H/H arms in
  Fig 6A are AICAR, 17-AAG, combination). The wave-3 doc was commissioned precisely to fix
  attribution-to-H/H errors (the metformin case); the controller layer re-introduced the identical
  error class for rapamycin in the adjacent section.
- **Failure mode:** the pack's signature correction (metformin was never run on Bub1b^H/H) sits two
  paragraphs away from a sentence claiming rapalogs *were* run on Bub1b^H/H with neutral results - a
  reviewer reading Tang finds both, and the correction's credibility becomes suspect on the exact
  axis it was built to defend. Even-though the everolimus ADMIT rests on pediatric-safety precedent
  and does not flip, an honestly-graded "Grade-D rationale" cannot cite a datum the citation
  does not contain.
- **Falsification test:** Tang 2011 Fig 6A arm list (AICAR/17-AAG/combination only) vs Fig S3
  (trisomic MEFs). Fix: reword to "mTOR perturbation neutral on trisomic-MEF proliferation
  (Tang Fig S3); never tested on Bub1b^H/H cells - mechanism support for this genotype: absent,
  honestly labeled."

### P2-2 - MAJOR (checklist C, new-evidence error in a framing-load-bearing sentence): CAPP3 "100 mg non-inferior to 600 mg" overstates the trial's formal conclusion
- **Claims:** attack map v2 framing bullet: "CAPP3 first results 2026 - 100 mg aspirin non-inferior
  to 600 mg (= Lancet G&H PMID 42425127)"; census table row 2: "100 mg non-inferior to 600 mg
  (ITT HR 0.97, IRR 0.94)"; and the census's own **recommended scope-safe sentence**: "whose
  low-dose sufficiency CaPP3 confirmed in 2026".
- **Evidence (According to PubMed, abstract of PMID 42425127, [DOI](https://doi.org/10.1016/S2468-1253(26)00114-7)):**
  the pre-specified non-inferiority rule required consistency across **both** ITT and per-protocol
  **and** both HR and IRR analyses. The 100-mg arm met it in ITT but **failed per-protocol
  time-to-first-cancer** (HR 1.00, 95 % CI 0.61–1.63; upper bound 1.63 > 1.5 boundary). The paper's
  verbatim conclusion: *"non-inferiority could not formally be concluded for either 100 mg or
  300 mg of aspirin daily … there was evidence that the 100 mg dose had similar characteristics to
  600 mg … with fewer side-effects and less risk of bleeding."*
- **Failure mode:** the one new factual upgrade wave-3 delivered for the framing ("CAPP3 2026 first
  results") is misquoted in the exact sentence class the census exists to protect - the approved
  "scope-safe" formulation. A judge checking the cited PMID reads the opposite conclusion
  ("confirmed" vs "could not formally be concluded"). The Lynch carve-out itself is unaffected  - 
  100 mg similar-risk-with-less-bleeding still supports the antiplatelet-class argument - but the
  sentence must not say non-inferior was shown.
- **Falsification test:** abstract results (per-protocol HR CI) + conclusion paragraph. Reword all
  three sites to: "CaPP3 2026: 100 mg showed cancer-risk characteristics similar to 600 mg with
  fewer adverse events (formal non-inferiority not concluded for either lower dose) - consistent
  with low-dose antiplatelet action."

### P2-3 - MINOR (condition B residue, F3): corner-false arithmetic slogan survived, plus unintegrated f_escape limb
F3's falsification demanded: reword to "crosses only at the joint-optimistic corner". Instead the
attack map asserts "Kimi condition honored: demotion rests on regulation + insufficient/unreliable
yield, not on the arithmetic slogan" - and then keeps the slogan: "modeled yield +0.3–3 % of WT,
below the competence line". With the pack's own baseline 5–10 %, the top corner is 10 + 3 = 13 %,
touching the line; "below" is corner-false in both the attack map and the candidates.tsv
readthrough row. F3's second limb (aminoglycoside-class NMD-blunting making f_escape
treatment-dependent - Wangen & Green 2020, cited in the same wave-2 section) was never integrated
anywhere. Non-load-bearing only because the demotion rationale is now explicitly correct.
**Fix:** delete "below the competence line", insert the corner-conditional sentence; one clause on
f_escape.

### P2-4 - MINOR (new arithmetic slip while honoring F8): the F1 band is wrong at its own top corner
"(1-s)·b + 0.5·s ≈ 16–20 % abundance" prescribes s ∈ [0.25, 0.30], b ∈ [5, 10] %. The top corner
s = 0.30, b = 10 % gives 7 + 15 = **22 %**, outside the stated band (attack map v2 and
candidates.tsv ASO row, both). Band should read ≈ 16–22 %. Conservative direction again (F8's
spirit), but this is the pack's single most recomputed arithmetic anywhere - judges will run it.

### P2-5 - MINOR (governance record drift, checklist D): pass-1 major count misrecorded, feeding the stop-rule calibration
`SCOPE_DECISION.md`: "adversarial pass 1 caught 5 majors"; `WORKFLOW_CONSENSUS.md` line 48:
"13 conditions incorporated (5 majors: ...)" - immediately followed by a list of **six** items
(internal inconsistency within the parenthesis). The pass-1 review labels **8** findings MAJOR
(F1–F7, F13) and 5 MINOR. The decay model ("p = 0.55 ⇒ pass 2 ≈ 2.3 majors") was calibrated on
n = 5; on the labeled artifact it is n = 8 (≈ 3.7 expected). Does not change this pass's counts or
any disposition, but the stop rule should not rest on a baseline the record misstates; fix both
docs to 8 and note the decay model is heuristic regardless.

### P2-6 - MINOR (checklist A integration loss): Q8's actionable Gate-0 enrichment dropped
wave3_ImmunoSurveillanceNK recommendation 5 - add the cheap immune/NF-κB panel (plasma
IFN/NF-κB-cytokine signature; PBMC NK/γδ immunophenotype) to Gate-0 patient-cell work, converting
the MAD1L1 observation into a BUB1B-proband question - is absent from the attack map's validation
plan (Gate-0 unchanged: "p16/SA-β-gal/SASP + aneuploid fraction"). This was the NK axis's one
feasible deliverable within the consent envelope; the safety clause was integrated, the research
enrichment was not.

### P2-7 - MINOR (checklist E omission): rapalog "Mannick-window floor" has no pediatric anchor, and the rule does not say so
Senolysis decision rule 2 (in attack map v2): NK dose-hold "floored at the Mannick window
(low-dose mTORi is RCT-grade immune-ENHANCING in adults)". The Mannick regimen was an elderly-adult
dose band; no pediatric low-dose rapalog immunology exists (the NK doc's own recorded gap,
faithfully carried in the everolimus section two paragraphs up - but not repeated inside the rule).
Dose-floor feasibility in a 5-year-old is therefore asserted, not named. Fix: one clause, "the
Mannick window is an adult anchor; pediatric low-dose pharmacokinetics/immunology are unmeasured
and are an assay of the monitoring arm itself."

### P2-8 - MINOR (checklist A compression + senolysis census hygiene): two framing residual risks
(a) The ASO delivery summary in the attack map drops the wave-3 doc's dual-compartment
point - systemic-only PMO leaves the neurodevelopmental/MVA-CNS compartment untreated and requires
a second (intrathecal) program; "No human precedent for non-muscle/non-CNS systemic
splice-switching" is necessary but not sufficient. (b) The senolysis "reverse census: five models,
none pro-incidence" (attack map) inherits the verifier's own count wobble: Ovadya 2018 measured
**survival, not tumor incidence** ("no tumor signal reported") - counting it in a tumor-outcome
census inflates the denominator by one; the verifier's Q2 header ("five studies measure tumor
outcomes… four show decrease or no-change") is similarly inconsistent with its own 6-row table.
Conclusion direction unchanged either way.

---

## Pass-1 condition ledger (checklist B, all 13)

| # | Condition | Honored? |
|---|---|---|
| F1 | Allele non-specificity math prominent in ASO section | **YES** - attack map + candidates.tsv carry (1-s)·b + 0.5·s with the harm case stated |
| F2 | KARD off-by-one caution (715 subst + 716 del) | **YES** - verbatim two-residue caution, assay-readout flag added |
| F3 | Reword readthrough arithmetic; f_escape not fixed | **PARTIAL** - P2-3 |
| F4 | SIRT2/NAD+ node reconciliation | **YES** - NMN row: DOWNGRADE-TO-WATCH, co-test in assay #5 |
| F5 | Tang 2011 AMPK-axis analysis | **YES** - reopened and closed with the PMID 21315436 correction; metformin-never-run and 2-DG-failure both integrated (but see P2-1 re-corruption in the everolimus row) |
| F6 | Senolysis oncologic-safety gate rules | **YES** - five decision rules match the verifier 1:1, incl. malignancy stop + cfDNA, burden-dominance gating, Mannick floor, intermittent-only, Milanovic stop |
| F7 | Framing scoped to chromosomal-instability class + CAPP2 census | **YES** - census done with boundary log and prohibited-formulation list (but see P2-2 on the 2026 update) |
| F8 | Exact arithmetic on the threshold sentence | **PARTIAL** - the 13–15 % figure is gone; the replacement band has a new top-corner slip (P2-4) |
| F9 | "at full product function" assumption carried | **YES** - "IF the Δ-product is functional", "WORSE than nothing if it is not" |
| F10 | Scrub leaked generation token | **YES** - grep-verified: token absent from the pack (only my own pass-1 review mentions it) |
| F11 | TSC relabeled (mTORopathy, not CIN-class) | **YES** - "TSC is an mTORopathy, not a CIN-class precedent" |
| F12 | Matsuura 2006 cohort relabeled | **YES** - monoallelic-PCS label fixed |
| F13 | IP/FTO + reimbursement per candidate | **YES** - PMO patent expiry verified + n-of-1/n-Lorem economics integrated; DMD-pricing fallback retained |

---

## What survives contact unchanged

1. **AMPK branch disposition (CLOSED + metformin WATCH residue)** - every load-bearing element of
   wave3_AMPKaxis was spot-consistent with my pass-1 full-text verification: correct PMID, metformin
   never on Bub1b^H/H, 2-DG selectivity failure, aneuploid-fraction-read of the H/H attenuation,
   empty feasible∧genotype∧exposure triangle, no-mTORi-co-stacking, MILI scoping. Sound.
2. **ASO sequence-green numbers** - integrated with zero drift from q7a (motif densities, MaxEnt
   scores, cryptic watch-list, landing-pad offsets, E715G re-verification); the honest INFERENCE
   flags (motif-correlate caveat, SpliceAI not run) were not inflated en route.
3. **Senolysis TIGHTEN integration** - all five decision rules faithful to the verifier; Baker 2016
   (no incidence change, latency+, NK unchanged) and the Lalinde timing counterweight correctly
   represented; the "unmeasured risk, not demonstrated hazard" grading preserved.
4. **NK-monitoring clause on everolimus** - faithful, including the pediatric-data recorded gap;
   candidates.tsv row matches.
5. **Census scope logic** - 30-row table, 11-query boundary log with two non-extendable adverse
   sweeps, prohibited-formulations list; the MSI-only carve-out and mTORopathy relabel are correct.
6. **Gene-editing deferral** - deliberately scoped out (WORKFLOW_CONSENSUS line 48); I agree: the
   delivery census that limits the ASO applies a fortiori to systemic base/prime editing in a
   constitutional child. No fresh axis needed here.
7. **Identifier hygiene of wave-3 docs** - all four spot-checked PMIDs (42425127, 42227334,
   41477861, 33931486) registry-valid and content-matched, including both too-new-for-scite 2026
   papers; the two authors' "no evidence located" gaps (Xu 2024 NK paper; pediatric NK-under-rapalog)
   are honestly recorded rather than silently filled.
8. **Cross-seam candidate rows** - every condition carried into `consensus_status` (ASO [kimi F1],
   KARD note, rapalog NK clause, senolysis rules, NMN watch, NK axis EXCLUDE-with-monitoring-clause).

## Required fixes before the confirmation wave (blocking order)

1. P2-1: reword Tang-neutrality attribution in attack map Level 3 + candidates.tsv rapalog row.
2. P2-2: reword CAPP3 in attack map framing bullet + census row 2 + the census's recommended
   scope-safe sentence; add the corrected form to the census's prohibited-formulation list.
3. P2-3/P2-4: arithmetic rewordings (corner-conditional readthrough sentence; 16–22 % band).
4. P2-5: fix the pass-1 major count (8) in WORKFLOW_CONSENSUS + SCOPE_DECISION; re-run
   SCOPE_DECISION's own wave-2 revisit trigger to reconcile "PRIMARY: ASO" with O1's named-candidate
   framing.
5. P2-6/P2-7/P2-8: one-clause insertions (Gate-0 immune panel; Mannick-floor pediatric caveat; ASO
   dual-compartment sentence; Ovadya census footnote).

*Verification note: PubMed E-utilities used for the four spot-checked identifiers; Tang 2011 claims
assessed against my pass-1 full-text verification of PMC3532042. All other claims assessed against
repo documents I actually read (paths in header). No scite tallies run this pass.*
