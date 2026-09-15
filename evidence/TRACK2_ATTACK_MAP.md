# Track 2 - Precision attack map v3 (post-consensus closure, 2026-09-05)
# Numbering convention: wave-N = artifact filenames (wave2_/wave3_/wave4_ docs, adversarial passes 1-4).
# Closure state: adversarial decay 8->2->2->0 majors; CLOSED-WITH-RESIDUAL-RISK (pass 4) (P4-1/P4-4).

Supersedes v1 (2026-09-05). Changes forced by the wave-1 evidence loops and the out-of-family
adversarial review (wave2_ADVERSARIAL_REVIEW.md - no blockers, all revisions accepted
with conditions; every condition is incorporated below). Consensus record: WORKFLOW_CONSENSUS.md;
votes: candidates.tsv `consensus_status` column.

Genotype: BUB1B p.Leu737Ter (canonical NMD substrate: exon 17/23, 75 nt upstream of nearest
junction, 6 downstream EJCs - escape unlikely) + p.Asn1002Lys (C-lobe hypomorph; AM 0.9229;
human↔fly conserved; crystal-validated packing interface).
Disease variable = BubR1 ABUNDANCE (catalysis dispensable at SAC; Established).
Checkpoint competence curve: ~13 % of WT abundance competent, ~6 % failing (Suijkerbuijk 2010).

## Consensus verdicts

### Level 1 - Genotype-targeted

**PRIMARY: ASO-mediated exon-17 skipping (ADMIT-WITH-CONDITIONS).**
Skipping the 141-bp in-frame exon 17 removes the PTC, restores the reading frame and escapes
NMD mechanistically - pediatric chemistry precedent exists (eteplirsen/viltolarsen/golodirsen/
nusinersen class). BUT (adversarial conditions, all load-bearing):
- The deleted product is Δ716-761 + junction substitution E715G. The construct's function is
  UNMEASURED and is the entire decision: (F1) skipping is NOT allele-specific - both transcripts
  (null allele AND N1002K hypomorph) skip the exon at equal rate; corrected benefit model is
  (1-s)·b + 0.5·s ≈ 16–22 % abundance IF the Δ-product is functional (band corrected per P2-4:
  corner s=0.3, b=10 % yields 22 %), and WORSE than nothing if
  it is not (both alleles lose function). Conditional: "IF Δ716-761+E715G works".
- KARD-region caution (F2): the deletion alters two residues at the KARD boundary (716 deleted,
  715 substituted) - the "error-correction modules retained" claim is weakened, flagged for the
  assay readout (kinetochore localization + error-correction reporters, not abundance alone).
- Suijkerbuijk 2010 1-730 fragment support is [INFERENCE], honestly labeled.
- Sequence feasibility (wave-3 Q7a; full audit trail in q7a_sequence_analysis.md): exon 17 is a
  textbook-clean skip substrate - RESCUE-ESE density 113.5/kb (eteplirsen-target DMD51: 107.3),
  ZERO PESS silencer octamers, native junctions strong bilaterally (MaxEnt donor 9.66 / acceptor
  9.29 vs DMD51's 3.73), no in-exon cryptic sites (intronic watch-list: intron16 -135 donor
  10.67, intron17 +879 acceptor 10.02), and an ESE-dense ASO landing pad at exon offsets
  ~108-138; PTC at offset 67, E715G junction codon re-verified from CDS. Strong junctions imply
  efficient-ASO-with-partial-skip as the realistic efficiency model. The sequence layer does not
  block the program; skipping efficiency itself is patient-cell ddPCR (assay list).
- Delivery is the honest rate-limiter (wave-3 Q7b; rescoped Q11): the unprecedented limb is
  specifically OLIGONUCLEOTIDE-class - no human non-muscle/non-CNS ASO splice correction exists;
  for a constitutional (whole-body) target this is the binding constraint, stated bluntly in the
  report - and CNS reach would need a SEPARATE intrathecal program (dual-compartment hybrid
  regimen), since systemic PMO does not cross the blood-brain barrier (P2-8 correction).
  Splice-switching as a MODALITY does have human systemic precedent - the small-molecule class
  (risdiplam: approved, oral, peripherally distributed with blood-level SMN2 splicing PD;
  branaplam ph2b RCT - early-terminated for peripheral neuropathy, 85.7% initial cohort, the adverse datum the disclosure must carry) - disclosed so the report distinguishes modality from chemistry; a
  small-molecule exon-17 skipper would be a screen-level program, not a near-term arm (Q11
  correction).
- Deliverability (wave-3 Q7c + F13): PMO chemistry core patents EXPIRED; FDA n-of-1 ASO
  guidance family exists; n-Lorem-type cost profile ~$1M/lifetime, philanthropically structured
  (milasen precedent) - the economics/dossier path is real even while the delivery biology is not.

**Readthrough of L737Ter - EXCLUDE-AS-PRIMARY (downgraded).** UGA-opal codon is optimal but the
+4 context is UGAA (second tier); modeled yield +0.3–3 % of WT is at best marginal to the ~13 %
competence line (and that only in the corner case: 10 % baseline + 3 % = 13 %), with the
NMD-escape fraction itself unstable under aminoglycoside exposure (aminoglycosides blunt NMD  - 
f_escape is dose-context-dependent, not fixed) (P2-3 correction). Regulatory collapse (ataluren:
EMA non-renewal 2023, FDA CRL 2025, NDA resubmission withdrawn 2026; ELX-02 ph2 cystinosis terminated).
Demotion rests on regulation + insufficient/unreliable yield. Retain as mechanistic footnote.

### Level 2 - Stabilization

**Arimoclomol - ADMIT-WITH-CONDITIONS (adjunct only).** Only chronic pediatric-safe node
(FDA 2024; NPC ≥2 y). Pivotal gap: zero evidence of raising a destabilized client KINASE's
abundance (its proven action is lysosomal HSP70; ALS ph3 failed). HSF1-Cdc20 aneuploidy
hazard flagged. Dose-set by assay #5. Completeness caveat (F4): NMN/SIRT2 node exists
(North 2014 raises BubR1 in vivo in the exact hypomorph mouse) - DOWNGRADE-TO-WATCH:
benign supplement class, zero human analysis, cheaply co-tested in assay #5. Direction resolved
(wave-4 Q12): NAD+/SIRT2 ACTIVITY UP raises BubR1 (deacetylation of the interphase degradation
mark K668); mitotic K243/250 acetylation is conversely SAC-PROTECTIVE (K243R/+ mice degrade
BubR1 and develop tumors) - therefore SIRT2 INHIBITORS ARE PROHIBITED CHEMISTRY and site-less
"acetylation stabilizes/destabilizes" phrasing is prohibited; NAD+ precursors carry human RCT
safety but zero BubR1/pediatric readouts. Census across 4 databases + patents found NO other
member: progerinin is HGPS-locked (closed); no DUB-activator pharmacology exists; the one
BUB1B-directed PROTAC family degrades in the wrong direction (flagged against miscitation);
and abundance targets a WINDOW, not a ceiling - BUB1B overexpression drives chemo
resistance (PMID 34545188).
Closed classes: celastrol (permanent CONTRA), PBA/TUDCA (compartment mismatch),
proteasome-sparing (no tolerable chronic member), and now the rest of abundance chemistry.

### Level 3 - Phenotype

**Everolimus/sirolimus - ADMIT (only chronically feasible), Grade-D rationale.**
Standardized on pediatric RCT safety (EXIST-1/3); mechanism support weak and attributed
exactly: mTOR perturbation was NEUTRAL ON TRISOMIC MEFs (rapamycin/torin1, Tang Fig S3) and
was NEVER tested on Bub1b^H/H cells (only AICAR/17-AAG were) - do not cite Tang for the
Bub1b arm (P2-1 correction). TSC is an mTORopathy, not a CIN-class precedent
(label fixed) - TSC-everolimus teaches pediatric chronic feasibility only, not mechanism match.
**NK-clearance monitoring clause (wave-3 Q8):** rapamycin inhibits NK cytotoxicity (mouse AND
human; Marçais 2014) and chronic everolimus contracts the circulating NK pool in adults
(Besson 2021) - directionally indeterminate in children (no pediatric NK-under-rapalog data;
recorded gap), and the host's documented route for clearing newly aneuploid cells is NK/NF-κB-
dependent surveillance (Santaguida 2017 → Wang 2021; human CIN corroboration in a MAD1L1-MVA
patient, Villarroya-Beltri 2022). Any rapalog arm therefore carries: baseline + periodic NK
count/maturation and NF-κB/inflammatory panel, a pre-defined dose-hold criterion on NK-pool
decline, and intensified imaging surveillance to cover the indeterminate direction.
**Named pediatric exposure window (wave-4 Q9; P2-7 gap narrowed to three explicit missing data
points):** on-label 4.5–5 mg/m²/day (≈3.4–3.8 mg/day at age 5), trough-titrated by LC-MS/MS to
5–15 ng/mL (TDM 1–2 wk post-start/change, then q3–6 mo; canonical target 5–10 ng/mL), with a
trial-validated lower band of 3–7 ng/mL (EXIST-3 low-exposure arm, efficacious from age 2.2;
true floor = its 3 ng/mL lower edge) (P3-1 correction). Age-5-continuous multi-year
exposure is directly documented (EXIST-1 final median 47 mo; ph-1/2 median 68 mo from ≥3 y;
growth/puberty unharmed over ~4 y; children ~4.7 y on sirolimus retain vaccine immunogenicity
incl. live MMR - humoral axis; NK-pool data still absent). Honesty datums the report MUST
quote with the window: infection 96 % vs 67 % and serious infection 35 % vs 7 % in <6 y
(EXIST-1), and two pediatric treatment-related infection deaths in EXIST-3. The only true
prophylactic-rapalog analog anywhere is PREVENT (sirolimus in asymptomatic TSC infants; 94 %
of troughs in target) - mTORopathy class, but it establishes that prevention-context rapalog
exposure in infants is trial-organized medicine, not a thought experiment.

**AMPK/energy-stress - CLOSED as candidate (wave-3 Q6, with WATCH residue).** Wave-2 full-text
re-verification of Tang 2011 (correctly: PMID 21315436; the 21546338 earlier cited is a
dermatology paper - citation corrected): only AICAR (direct ZMP-class AMPK ligand) and 17-AAG
were run on Bub1b^H/H MEFs - metformin was NEVER tested on those cells (F5's premise, repeated
in v2, corrected); kill selectivity tracked per-cell aneuploid fraction, not BUB1B carrier state
(no constitutional window-collapse); 2-DG failed selectivity; AICAR is not pediatric-feasible, so
the feasible∧genotype-matched∧exposure-matched triangle is empty. Not CONTRA: metformin retained
as WATCH residue behind a ≤100 µM co-test in the proband-cell battery (zero-cost, no mTORi
co-stacking); MILI-LFS monitored passively (adult ≥16 y, p53-mechanism - does not transfer as
CIN precedent). 17-AAG combination trap explicitly blocked (HSP90i CONTRA stands).

**Senolysis - GATE-FIRST, TIGHTENED (F6 decided with evidence, wave-2 verifier).**
The tumor-suppressive-senescence barrier is real (Braig/Michaloglou/Weaver lineage), but its
load-bearing inverse FAILS: no model/drug shows senolytic removal increasing tumor incidence
("no evidence located", four recorded queries + 2025–26 sweep), and the arbiter datum is
Baker 2016 (full text): chronic p16+ clearance had NO impact on tumor incidence/spectrum,
INCREASED tumor latency, and left NK1.1+/CD4/CD8 populations unchanged (Ext. Data Fig.7);
record corrected - Baker 2008 indeed never tested tumor endpoints. Reverse census beyond
Baker 2011: the post-2011 census, none pro-incidence (Haston 2023 p16-FDR burden−; Kumar 2025 ABT-263
mitigated radiation-GI cancer; Gallanis 2023 metastasis−; Ovadya 2018 ABT-737 survival+ in a
progeroid without tumor endpoints - not an incidence datum) (P2-8 correction); the protective
census grew +4 on re-attack (Ming 2025; Zhou 2026; Hamburger 2026 PRISMA; Valdivieso 2026),
still zero pro-incidence (Q11); one
genuine counterweight - Lalinde-Gutiérrez 2026: EARLY senolysis accelerated PyMT growth
(macrophage/CCL2-dependent, not barrier-release), late was protective → timing matters, not
permission. Decision rules (replacing vague caution):
1. Gate-0 (patient-cell senescence burden) gains pre-specified malignancy stopping criteria +
   cfDNA safety readout; burden-dominance is a go/continue condition - no elevated burden = axis
   stays dormant.
2. Rapalog-arm NK status upgraded from monitoring to PRE-DEFINED dose-hold trigger, floored at
   a trial-validated pediatric band: trough 3–7 ng/mL (EXIST-3 low-exposure arm, efficacious
   from age 2.2; TDM per label calendar) (P3-1 correction). The Mannick elderly-immunoenhancement window does NOT
   translate - its 0.1–0.5 mg/day regimens are ~7–40× below a 5-year-old's label exposure and
   have NO pediatric evidence (two recorded negative queries): Mannick is cited direction-setting
   only and that exposure must never be targeted in a child (wave-4 Q9 correction of the P2-7
   interim wording).
3. If senolytics ever dose, the validated pattern is INTERMITTENT dasatinib (Justice 2019
   adult-pattern; Mustjoki NK/LGL signal if anything protective) - surveillance-preserving by
   construction, NOT chronic.
4. Hard stop on any stemness-reprogramming readout (Milanovic lineage).
5. Pediatric FEASIBILITY correction (Q11 negation re-attack): navitoclax (ABT-263, canonical
   BCL-xL senolytic) HAS published pediatric exposure - oncology setting IN COMBINATION REGIMENS (not monotherapy), children ≥4 y, RP2D
   25 mg <45 kg (Pullarkat 2021), St. Jude RAVEN ages 4–30, plus two pediatric expanded-access
   programs; what remains absent is pediatric SENOLYTIC-INDICATION data (all D+Q trials ≥18 y).
   The axis still lives or dies behind Gate-0/assay data, never on literature momentum.

**Surveillance backbone - verified to 2026 standard (wave-4 Q10).** Renal ultrasound every
3 months from birth until age 7 for ALL MVA conditions (SIOP-Europe Host Genome WG, Hol 2021;
endorsed verbatim by AACR 2nd Childhood-Cancer-Predisposition Workshop update, Nakano 2024) +
clinical review-of-systems for rhabdomyosarcoma/pain/hematuria + radiation avoidance. No
WBMRI. cfDNA is NOT standard of care in any predisposition syndrome (no benefit-confirming RCT;
the CHARM2 cfDNA RCT explicitly EXCLUDES MVA/CIN). MVA1 spectrum quotable verbatim:
"predominantly Wilms tumor and rhabdomyosarcoma, but MDS, AML and ALL". Risk-point prohibition:
GeneReviews ">85 %" Wilms risk vs Nakano "rarity hampers accurate risk assessment" - the report
never cites a point value. Five-registry live census (positive controls per registry): ZERO
MVA-specific intervention trials or registries exist anywhere - the submission verifiably
proposes the first intervention attempt in this disease.

**Still closed:** HSP90i (genotype-specific hazard), KIF18Ai (SAC-defective resistance + WGD
gate), direct SAC inhibition, TRIP13i (MVA3/Wilms causation), autophagy-flux drugs
(pediatric-unjustified), Aurora-B manipulation (self-defeating).

## Framing, census-hardened (F7, wave-2 Q5)
No approved pharmacologic exists for cancer prevention in a constitutional CHROMOSOMAL-
INSTABILITY syndrome (surveillance-only field; MVA report claims to propose the first). This
survives the complete 30-row prevention-in-predisposition census (wave3_PrecedentCensus.md,
11-query boundary log, two non-extendable adverse sweeps) with scope-safe carve-outs:
- **Lynch/MSI class** is the one genuine prevention exception (CAPP2 RCT-proven). CAPP3 first
  results (Lancet G&H 2026, PMID 42425127): 100 mg showed similar cancer risk with less
  bleeding than 600 mg, but the trial's own multi-criterion rule (consistency across ITT AND
  per-protocol AND HR AND IRR) meant formal NON-INFERIORITY could NOT be concluded for either
  lower dose (P2-2 correction - the word "non-inferior" is prohibited). Aspirin's mechanism is
  antiplatelet/anti-inflammatory, NOT CIN- or MMR-directed (Rüschoff lineage + Pharmacol Rev
  2026) - disclosed as an exception class, not a mechanistic precedent for CIN.
- **mTORopathy/burden-control class** (everolimus-TSC, belzutifan-VHL, alpelisib-PROS,
  mirdametinib-NF1, selumetinib-NF1) is approved for lesion burden, not mutation-directed
  cancer prevention - teaches pediatric feasibility only.
- Celecoxib-FAP remains the cautionary withdrawn precedent (CV withdrawal 2012).
- Matsuura 2006 refers to monoallelic premature-chromatid-separation carriers, not an MVA
  cohort (label fixed). Prohibited formulations are listed in the census doc; the report may
  only use the scope-safe sentence forms given there.

## Validation plan (feasible inside the organizers' consent envelope)
0. Gate-0 senescence burden in patient cells (p16/SA-β-gal/SASP + aneuploid fraction), enriched
   per Q8 with the immune/NF-κB baseline panel (NK count/maturation + inflammatory markers - the
   same panel the rapalog-arm rules read against) (P2-6 correction).
1. NMD-escape fraction of the L737Ter transcript (qPCR/ddPCR) - gates any nonsense-direction claim.
2. N1002K stability pulse-chase ± proteasome rescue (tests allele-class prediction).
3. Checkpoint-timing assay (nocodazole) - locates proband on the 6–13 % competence curve.
4. (∗∗DECISIVE∗∗) Δ716-761+E715G construct: abundance, fold/stability, kinetochore localization,
   CDC20-binding kinetics, error-correction reporter - the ASO go/no-go.
5. N1002K abundance ± arimoclomol (± NMN co-test), HSP90i pulse as positive control.
6. T1008 phospho-proximity probe (MS) - 6 residues from N1002 (INFERENCE-gated).

## Provenance
Wave-1 docs: wave2_NonsenseAxis / StabilizationAxis / SenolyticAxis / CINSyndromeAxis (all
identifiers verified by authors; join check 32/32 sampled DOIs registry-verified).
Adversarial: wave2_ADVERSARIAL_REVIEW.md (kimi out-of-family). Prior layers: LITERATURE_SWEEP,
MECHANISM_G1, PHENOTYPE_G3, VARIANT_PROTEIN_IMPACT, STRUCTURAL_VALIDATION.
GenAI disclosure per hackathon rule: to be reported in methods form (provider/tier/data-handling).
