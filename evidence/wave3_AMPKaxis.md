# Wave-3 Q6 - AMPK / energy-stress axis (reopened branch F5): verdict-first decision

**Agent:** AMPKaxis · **Date:** 2026-09-05 · **Scope:** decide the reopened F5 branch
(Tang 2011 selective-kill of Bub1b^H/H MEFs) for the BUB1B p.Leu737Ter + p.Asn1002Lys MVA proband.
**Termination criterion (declared, per consensus rules):** stop when each sub-question is
verdict-decided - (a) Tang 2011 re-analysis, (b) pediatric metformin chronic-safety census,
(c) metformin-in-predisposition precedent (MILI), (d) feasibility map of AMPK mimetics in a
child, (e) branch promote/downgrade/close verdict. **All five decided below → criterion met.**
**scite note:** the scite MCP route was not mounted in my tool inventory this session
(pubmed/serena/open-targets only); PubMed metadata and PMC full text were used for identifier
and claim verification instead. Where a prior scite Smart-Citation tally exists in the repo it is
quoted with its sweep date (Tang 2011: s24/c3/m378, LITERATURE_SWEEP, 2026-09-05 wave-1).

---

## VERDICT

**CLOSE the AMPK/energy-stress branch as a self-standing therapeutic candidate;
do not promote. Retain a narrow DOWNGRADE-TO-WATCH residue** (metformin-only) as a
zero-cost co-observation inside the everolimus-class Level-3 monitoring arm, with stated
conditions. F5 is resolved: Tang 2011's genotype-matched datum is real but is a
**tumor-treatment, kill-direction finding in primary mouse MEFs at culture doses**, and its
one pediatric-feasible member (metformin) was the *weakest* arm of the paper, was **never run
on Bub1b^H/H cells**, and acts at exposures a child cannot chronically reach. There is no
mechanism-matched human precedent in any chromosomal-instability syndrome; the MILI
(Li-Fraumeni) precedent targets a different lesion class (p53-mutant mitochondrial metabolism).
The branch cannot be *excluded as physically dangerous* - Tang's own data argue that
selectivity tracks the per-cell aneuploid load, not the BUB1B carrier state, so clinical-dose
metformin is more likely neutral-inert than systematically harmful in a hypomorph child - so
"watch", not "CONTRA".

Verdict-shaped corrections forced by this pass (all verified, §1–§4):
1. The agent-brief identifier **PMID 21546338 is wrong** - it is an occupational-dermatology
   review ([DOI](https://doi.org/10.1684/ejd.2011.1343)); Tang 2011 is **PMID 21315436**
   ([DOI](https://doi.org/10.1016/j.cell.2011.01.017), PMC3532042, confirmed in PMC journal
   metadata).
2. The attack map's line "(AICAR, metformin weakly) selectively killed Bub1b^H/H MEFs" is
   **half-wrong**: in Fig 6A only **AICAR and 17-AAG** (and their combination) were run on
   Bub1b^H/H MEFs; **metformin was not tested on Bub1b^H/H cells** - its datum is trisomic
   MEFs only (Table S1/Fig S1A). The genotype-matched metformin data point does not exist.
3. **2-DG did not share the selective-kill phenotype** - it was "highly toxic even in euploid
   cells" (Tang Fig S6A) and showed no selectivity for trisomic cells. The adversarial review's
   "AICAR direction" framing survives, but "2-DG arm" does not as a class member: among the
   three energy-stress compounds screened, **two of three failed or were weak**; only the
   direct AMPK ligand (AICAR/ZMP) was strongly selective. That is a class-parameter finding,
   not a class finding.

**Conditions attached to the WATCH residue** (metformin-only):
- Cheapest possible disambiguator: add metformin (and AICAR as positive control) to the
  already-planned patient-cell assay battery (validation plan #3/#5-class) to test whether
  *proband* euploid and aneuploid-fraction cells differ in metformin sensitivity at ≤100 µM
  (clinically-relevant exposure; therapeutic pediatric plasma ≈ 10–45 µM). One negative at
  clinical concentration closes the branch permanently.
- If an mTORi (everolimus-class) is ever run in the proband, metformin must not be silently
  co-stacked for the AMPK rationale; both hit metabolism and the combination is
  uncharacterized in any CIN context.
- MILI readouts (≥5-y, adult LFS, ≥16 y) should be monitored passively; a positive MILI **does
  not transfer** as CIN-syndrome precedent (different lesion, different mechanism postulate:
  mitochondrial complex-I/normalization of p53-mutant OXPHOS, not aneuploid-cell kill).

---

## 1. Tang 2011 re-analysis - what the genotype-matched arms actually show

**Source (verified in PMC full text, PMC3532042):** Tang, Y.-C., Williams, B. R., Siegel, J. J.,
& Amon, A. (2011). The energy and proteotoxic stress-inducing compounds AICAR and 17-AAG
antagonize proliferation in aneuploid cells. *Cell*, 144(4), 499–512.
[DOI](https://doi.org/10.1016/j.cell.2011.01.017) | PMID 21315436 · scite tally (wave-1 sweep):
s24/c3/m378.

### 1.1 Screen architecture and hits
Eighteen compounds in three stress classes were assayed for differential antiproliferation of
primary euploid vs trisomic (Chr1/13/16/19) MEFs. Three showed consistent chromosome-size-
correlated selectivity: **AICAR** (energy stress), **17-AAG** (HSP90i), **chloroquine** (late
autophagy blockade). Energy-stress class breakdown, verified in main text + discussion:
- **AICAR (0.2–0.5 mM):** kills trisomic MEFs (cell-number decline, not just arrest); selectivity
  scales with extra-chromosome size.
- **Metformin:** impaired accumulation of trisomy 13/16 cultures, "although the effects were not
  as dramatic" (Table S1, Fig S1A). Weakest energy-class hit. (Exact Table S1 concentration not
  retrievable - author-manuscript supplement is not exposed via PMC/OA or Europe PMC - see Gaps;
  the qualitative ordering is in the main text and is what this analysis uses.)
- **2-Deoxyglucose:** NO trisomic selectivity; "highly toxic even in euploid cells" (Fig S6A).
  Fails both the selectivity and the window test.
- **Rapamycin, torin1, mTOR knockdown:** NEUTRAL - did not inhibit trisomic-MEF proliferation,
  did not add to AICAR (Fig S3). This is the datum the pack already uses correctly for the
  mTORi branch.

### 1.2 Mechanism of the AICAR selective kill (verified, Figure-level)
AMPK → p53 → mitochondrial apoptosis; explicitly NOT the alternatives:
- AMPK-dependence: AMPKα knockdown and compound C suppress the effect (Fig 4A–D); basal AMPK
  activity is NOT elevated in trisomic cells (Fig 4E–F), but AMPK activates *faster* upon AICAR
  in trisomic cells (Fig 4G) - sensitization, not hyperactivation.
- p53 S15 phosphorylation and stabilization occur earlier in trisomic cells; Bax
  mitochondrial insertion is higher (Fig 3D–E); p53 knockdown rescues (Fig 3F–G).
- NOT cell-cycle arrest (Fig S2A), NOT senescence (Fig S2B), NOT necroptosis (Nec-1 no rescue,
  Fig S2C), NOT mTOR (Fig S3).
- Second arm: AICAR *exaggerates* pre-existing aneuploid stress - basal autophagy (LC3-II,
  Bnip3) and inducible Hsp72 are already elevated in trisomic cells and are pushed further
  (Fig 5A–D). Kill = energy stress additive on proteotoxic/bioenergetic stress above an
  apoptosis threshold; **p53 must be functional** for full effect in primary cells.

### 1.3 The Bub1b^H/H arms (Fig 6A–B) - the F5 datum
- AICAR and 17-AAG (and the combination) impeded **Bub1b^H/H** MEF accumulation vs WT; similar
  for Cdc20^AAA. Effects **"not as dramatic as in the trisomic MEFs, presumably because only
  36% and 52% of the Bub1b^H/H and Cdc20^AAA MEFs are aneuploid after several passages"**
  (paper's own interpretation, verified verbatim).
- **Quantitative implication the adversarial pass did not draw:** H/H sensitivity was attenuated
  in proportion to the aneuploid fraction, i.e., the kill signal tracks **per-cell aneuploid
  burden**, not the BubR1-hypomorph genotype per se. Euploid cells inside a Bub1b-hypomorph
  population were, on the paper's own reading, not preferentially killed. This is the
  disposition-decisive nuance: the feared "constitutional collapse of the therapeutic window"
  (every patient cell is BubR1-low ⇒ every cell sensitized) is **not supported** by Tang; the
  window that is supported is aneuploid-cell vs euploid-cell.
- Human-cell corroboration: AICAR/17-AAG (esp. combined) preferentially antiproliferate CIN
  colorectal cancer lines vs near-euploid MIN lines and xenografts (Fig 6C–D, 7); lung-line
  AICAR effects were modest and subset-only - i.e., attenuated and variable in human cells,
  exactly as PHENOTYPE_G3 recorded.

### 1.4 What this means for a CONSTITUTIONAL-CIN child
- The finding is a **therapy-of-established-tumor direction** (kill aneuploid CIN cancer cells),
  for which the pack's KIF18A/17-AAG-class treatment axis already stands. As a **prevention/
  chronic-mosaic-clearance** direction it would require: a pediatric-feasible compound,
  aneuploid-cell selective-kill at chronically-tolerated systemic exposure, functional p53
  (present in the proband), and no systemic cost to high-turnover euploid compartments.
  Tang supplies only the mechanistic plausibility; no compound in the paper meets the rest.
- Immune-surveillance tension (cross-reference to Q8/ImmunoSurveillanceNK, which owns the axis):
  endogenous clearance of newly-aneuploid cells in this proband is NK/senescence-mediated
  (Santaguida 2017; Wang 2021 chain in wave docs). Chronic pharmacologic aneuploid-cell kill
  via energy stress is a **redundant, blunter** version of a surveillance arm the child already
  runs; adding it is not an orthogonal win and nothing in Tang argues it is needed where the
  natural mechanism works.

## 2. Pediatric chronic-safety census - metformin

According to PubMed (identifiers verified via NCBI metadata this session):
- **TODAY (Treatment Options for T2DM in Adolescents and Youth), main RCT:** Zeitler P et al.,
  *N Engl J Med* 2012;366:2247–56. [DOI](https://doi.org/10.1056/NEJMoa1109333) |
  PMID 22540912 · PMC3478667 · NCT00081328. 699 randomized, **ages 10–17**, metformin up to
  **1000 mg twice daily**; mean follow-up 3.86 y. Every participant received run-in metformin;
  arms = metformin alone vs ±rosiglitazone vs ±lifestyle. SAEs in 19.2% overall (trial-level
  figure, all arms); metformin-alone failure rate 51.7% (efficacy datum, not safety).
  **Largest randomized pediatric chronic-metformin exposure; establishes that 2 g/day chronic
  metformin in ≥10-y children is a constitute-able safety baseline** (no idiosyncratic fatal
  signal; SAE denominator is trial-wide).
- **TODAY2 long-term observational extension:** TODAY Study Group, *N Engl J Med*
  2021;385:416–26. [DOI](https://doi.org/10.1056/NEJMoa2100165) | PMID 34320286 (identifier
  verified by exact-title esearch). Cohort followed into young adulthood (~13 y diabetes
  duration): documents complication accumulation of youth-onset T2DM itself - i.e., long
  metformin exposure observed without a drug-attributed oncologic signal; the complication
  burden is disease-owned, not drug-owned. (Complication details not extracted; flagged in Gaps
  as not load-bearing for this verdict.)
- **TODAY2 treatment-arm post-intervention analysis:** TODAY Study Group, *Diabetes Care*
  2021;44:75–80. [DOI](https://doi.org/10.2337/dc20-0622) | PMID 33290248 · PMC7783942  - 
  confirms continued safety-analytic framework out to ~6–7 y post-randomization.
- **One chronic biochemical AE with lifelong-exposure relevance:** long-term metformin →
  vitamin B12 lowering/deficiency - Aroda VR et al., *J Clin Endocrinol Metab* 2016.
  [DOI](https://doi.org/10.1210/jc.2015-3754) | PMID 26900641 (adult DPP/DPPOS; identifier
  verified by esearch). **No TODAY/pediatric-specific B12 paper was located** (two targeted
  PubMed queries returned none) - B12 surveillance is a borrow-from-adults precaution and a
  named pediatric data gap, not a pediatric datum.
- **Regulatory floor:** metformin is labeled for pediatric T2DM from age ≥10 years
  (established label fact); the MVA proband is ~5, so even chronic metformin would be
  **below-label** (not below-known-safety: substantial off-label experience exists in
  obesity/PCOS cohorts, but no RCT-grade record at age 5 - gap).

**Census bottom-line:** metformin is chronically pediatric-feasible in safety terms (Grade-A
pediatric pharmacology) - feasibility is NOT the branch's failure mode.

## 3. Metformin in hereditary cancer predisposition - the MILI precedent, scoped

According to PubMed:
- **Mechanistic line (LFS, not CIN):** increased mitochondrial/OXPHOS activity is a germline
  phenotype of LFS carriers - Wang P.-Y. et al., *N Engl J Med* 2013;368:1027–32.
  [DOI](https://doi.org/10.1056/NEJMoa1214091) | PMID 23484829 · PMC4123210 (human + mouse,
  NCT00406445). Pharmacologic or genetic disruption of mitochondrial respiration (incl.
  metformin) improved cancer-free survival in a TP53-mutant LFS mouse model and reproduced
  the mitochondrial-normalization biomarker set in a small metformin pilot in LFS patients  - 
  Wang P.-Y. et al., *J Clin Invest* 2017;127:132–6. [DOI](https://doi.org/10.1172/JCI88668) |
  PMID 27869650 · PMC5199691.
- **Phase I pilot (n=26, adults):** metformin up to 2000 mg/day × 14 weeks tolerable in LFS;
  grade-1 diarrhea 50%, nausea 46%; IGF-1 lower on-drug - as summarized in Pantziarka P &
  Blagden S, *Cancers* 2022;14:1621. [DOI](https://doi.org/10.3390/cancers14071621) |
  PMID 35406393 · PMC8997074 (review; the pilot itself, NCT01981525, is summarized there, not
  separately indexed - flagged).
- **MILI proper:** Dixon-Zegeye M et al. (Blagden group), *Trials* 2024;25:103.
  [DOI](https://doi.org/10.1186/s13063-024-07929-w) | PMID 38308321 · PMC10837926  - 
  **protocol only**; phase II RCT, 224 LFS **adults (≥16 years)**, metformin ≤2 g/day + MRI
  surveillance vs surveillance, 5-y cancer-free survival primary endpoint; parallel NCI study;
  no efficacy data yet.

**Scoping for the pack:** MILI/LFS is a *constitutional tumor-predisposition metformin-for-
prevention* precedent - strengthening the generic feasibility argument of wave-1's CAPP2-style
framing - but it is **mechanism-mismatched**: its postulated action is mitochondrial/
metabolic normalization of a p53-mutant host, explicitly *not* aneuploid-cell kill, and its
human test population excludes children. It is precedent that a chronic metformin prevention
trial in a rare constitutional syndrome is *operationally fundable/runnable* - useful for the
PrecedentCensus table - and nothing more.

## 4. Feasibility map - AMPK/energy-stress mimetics in a ~5-year-old constitutional-CIN child

| Agent | Selective kill in Tang (system) | Pediatric chronic feasibility | Exposure match to Tang protocol | Disposition |
|---|---|---|---|---|
| **AICAR** | strong, p53-dependent (trisomic MEFs; attenuated on Bub1b^H/H; attenuated/variable in human CIN lines) | **Zero**: not approved; "currently not approved for use in humans" (Tang discussion); no pediatric formulation or experience; purine-nucleoside-class chronic safety uncharacterized | 0.2–0.5 mM culture; no chronically achievable human exposure | **EXCLUDE - not pediatric-feasible** |
| **Metformin** | weak, trisomic MEFs only ("not as dramatic"); **not run on Bub1b^H/H** | **High (≥10 y; RCT-grade TODAY/TODAY2)**; below-label at age 5; B12 monitoring | culture mM-range vs therapeutic plasma ≈10–45 µM - the standard 2–3 log cell-culture↔clinic gap applies (Tang Table S1 concentration not retrievable; gap #3) | **WATCH-ONLY** - no aneuploid-selectivity human data at clinical exposure; co-test at ≤100 µM in proband-cell assay before any claim |
| **2-Deoxyglucose** | **failed selectivity; highly toxic in euploid cells** (Fig S6A) | negligible chronic experience; chronic glycolytic blockade in a growing child unjustified | - | **EXCLUDE - fails selectivity + window** |
| **Compound C / direct small-molecule AMPK activators (e.g., MK-8722 class)** | tool compounds (compound C actually *rescued* trisomic cells - mechanism-control, not therapeutic) | none; systemic AMPK agonism has documented cardiac/cardiomyocyte-hypertrophy class concerns in preclinical work [INFERENCE - not re-verified this session] | - | EXCLUDE |
| **Polyphenol/supplement "AMPK activators" (berberine etc.)** | no Tang data | safety uncharacterized at trial grade; variable bioavailability | no exposure match | EXCLUDE - no evidence located |

**Map bottom-line:** exactly one member is pediatric-feasible (metformin), and it is precisely
the member with (i) the weakest selective-kill signal, (ii) no genotype-matched (Bub1b^H/H)
datum, and (iii) the largest gap between effective culture exposure and achievable chronic
pediatric exposure. The triangle (feasible ∧ genotype-matched ∧ exposure-matched) is empty.

## 5. Contraindications/flags specific to a constitutional-CIN child

1. **Window direction is favorable but unproven:** Tang's aneuploid-fraction-read shows the kill
   window is cell-autonomous (aneuploid vs euploid), so chronic low-dose energy stress is
   unlikely to collapse euploid hypomorph tissue - but the *benefit* at clinical metformin
   exposure is negative-confidence, not positive: at 10–45 µM systemic there is no human or
   in-vivo aneuploidy-selectivity datum at all (searched: 0 PubMed hits for
   metformin×aneuploidy×CIN primary studies post-Tang; one-directional gap).
2. **B12 surveillance mandatory if ever dosed chronically** (adult DPP/DPPOS evidence; no
   pediatric-specific data - gap #2). Renal-function prerequisites per label.
3. **Do not co-stack with mTORi on amphibious rationale:** Tang Fig S3 says mTORi neither kills
   aneuploid cells nor adds to AICAR; everolimus's ADMIT rationale (tissue-rescue/stress relief,
   Grade-D) and the AMPK direction are different games. Combining them imports both AE sets for
   zero established additive benefit.
4. **AICAR/2-DG class permanently closed for this child** (not pediatric-feasible / fails
   selectivity) - this closes the strong arm of Tang 2011 for *this* application; anything
   requiring AICAR-strength AMPK activation is out of reach of pediatric chronic dosing.
5. **p53-dependence note:** the proband's p53 is not implicated (BUB1B-MVA), so the AICAR-class
   p53-dependence would not have been a genotype blocker - recorded for completeness; it is
   why the LFS (p53-mutant) population is a *different* prevention problem, not a comparator.
6. **17-AAG/HSP90i combination trap:** Tang's best in-vitro effect was the AICAR+17-AAG
   combination; 17-AAG is already a named genotype-specific CONTRA in this proband
   (HSP90-client hypomorph). Any future proposal to "recover the Tang effect" via combination
   must be blocked at exactly this point.

## 6. Gaps (explicit)

1. **Tang Table S1 exact metformin/2-DG concentrations not retrieved** - author-manuscript
   supplement (NIHMS276601) is not exposed via PMC OA or Europe PMC APIs (recaptcha-gated);
   the mM-vs-µM exposure gap is asserted from therapeutic-level pharmacology + the standard
   cell-culture range, not from the paper's own table number. What settles it: publisher
   supplement access.
2. **No pediatric-specific metformin-B12 / below-label (age 5) chronic safety corpus located**
   - TODAY band is 10–17 y. What settles it: targeted pharmacy-epidemiology search (off-label
   obesity/PCOS cohorts) if this residue is ever activated.
3. **ZERO post-Tang primary reproduction of metformin/energy-stress selective kill of aneuploid
   cells** located in PubMed - the whole branch rests on one 2011 mouse-primary dataset plus
   attenuated human-cancer-line signals; no MVA1/BUB1B-cell energy-stress data exist anywhere
   (human or animal). What settles it: the ≤100 µM proband-cell co-test (§VERDICT conditions).
4. TODAY2 NEJM 2021 complication detail not extracted (not load-bearing for the verdict).
5. MK-8722-class cardiac concern flagged [INFERENCE] - not load-bearing; the class is excluded
   on zero pediatric feasibility regardless.
6. scite Smart-Citation re-pull pending when the scite route is again mounted; per wave-1
   sweep totals, Tang 2011 s24/c3/m378 - no contradicting-signal tallies recorded.

## References (APA; PubMed-retrieved unless noted)

- Tang, Y.-C., Williams, B. R., Siegel, J. J., & Amon, A. (2011). The energy and proteotoxic
  stress-inducing compounds AICAR and 17-AAG antagonize proliferation in aneuploid cells.
  *Cell*, 144(4), 499–512. [DOI](https://doi.org/10.1016/j.cell.2011.01.017) · PMC3532042  - 
  verified in full text (figures 1–7, S2, S3, S6).
- Zeitler, P., Hirst, K., Pyle, L., et al.; TODAY Study Group. (2012). A clinical trial to
  maintain glycemic control in youth with type 2 diabetes. *N Engl J Med*, 366(24), 2247–56.
  [DOI](https://doi.org/10.1056/NEJMoa1109333) · PMID 22540912 · PMC3478667.
- TODAY Study Group. (2021). Long-term complications in youth-onset type 2 diabetes.
  *N Engl J Med*, 385(5), 416–26. [DOI](https://doi.org/10.1056/NEJMoa2100165) · PMID 34320286.
- TODAY Study Group. (2021). Postintervention effects of varying treatment arms on glycemic
  failure and β-cell function in the TODAY trial. *Diabetes Care*, 44(1), 75–80.
  [DOI](https://doi.org/10.2337/dc20-0622) · PMID 33290248 · PMC7783942.
- Aroda, V. R., Edelstein, S. L., Goldberg, R. B., et al. (2016). Long-term metformin use and
  vitamin B12 deficiency in the Diabetes Prevention Program Outcomes Study.
  *J Clin Endocrinol Metab*, 101(4), 1754–61. [DOI](https://doi.org/10.1210/jc.2015-3754) ·
  PMID 26900641.
- Wang, P.-Y., Ma, W., Park, J.-Y., et al. (2013). Increased oxidative metabolism in the
  Li-Fraumeni syndrome. *N Engl J Med*, 368(11), 1027–32.
  [DOI](https://doi.org/10.1056/NEJMoa1214091) · PMID 23484829 · PMC4123210.
- Wang, P.-Y., Li, J., Walcott, F. L., et al. (2017). Inhibiting mitochondrial respiration
  prevents cancer in a mouse model of Li-Fraumeni syndrome. *J Clin Invest*, 127(1), 132–6.
  [DOI](https://doi.org/10.1172/JCI88668) · PMID 27869650 · PMC5199691.
- Pantziarka, P., & Blagden, S. (2022). Inhibiting the priming for cancer in Li-Fraumeni
  syndrome. *Cancers*, 14(7), 1621. [DOI](https://doi.org/10.3390/cancers14071621) ·
  PMID 35406393 · PMC8997074 (pilot NCT01981525 tolerability summary).
- Dixon-Zegeye, M., Shaw, R., Collins, L., et al. (2024). Cancer Precision-Prevention trial of
  Metformin in adults with Li Fraumeni syndrome (MILI): a randomised controlled trial protocol.
  *Trials*, 25, 103. [DOI](https://doi.org/10.1186/s13063-024-07929-w) · PMID 38308321 ·
  PMC10837926.
- Repo-internal: LITERATURE_SWEEP.md (Tang scite tally), PHENOTYPE_G3.md §1.4,
  the program decision record (F5 line), wave2_ADVERSARIAL_REVIEW.md (F5). PMID 21546338
  (brief-error identifier) resolves to: Géraut, C. et al. (2011). Occupational diseases due to
  cooling fluids. *Eur J Dermatol*, 21(2), 162–9. [DOI](https://doi.org/10.1684/ejd.2011.1343)
  - recorded for audit trail only.

*GenAI-disclosure note for methods: literature retrieval via NCBI E-utilities/PubMed MCP and PMC
full-text reader; analysis drafted by agent; identifiers machine-verified against NCBI metadata.*
