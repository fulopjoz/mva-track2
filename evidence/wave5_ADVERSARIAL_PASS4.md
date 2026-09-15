# Wave-5 Adversarial Review - PASS 4 (FINAL, hard-ceiling closure pass)

**Reviewer:** AdversarialKimi4 (out-of-family red team; passes 1–3 were AdversarialKimi,
AdversarialKimi2, AdversarialKimi3 lineage) · **Date:** 2026-09-05
**Scope (read complete, current state):** `TRACK2_ATTACK_MAP.md` · `candidates.tsv` (raw,
untruncated) · `SCOPE_DECISION.md` · `WORKFLOW_CONSENSUS.md` (full incl. raw tail) ·
`wave4_ADVERSARIAL_PASS3.md` (my predecessor's findings - each P3 fix verified at its tagged
site) · CONTROLLER ERRATA at the tails of `wave3_PrecedentCensus.md`, `wave3_SenolysisF6verifier.md`,
`wave3_ASOdeep.md`.
**Attacks run per the pass-4 checklist (deliberately different from pass 3):**
A fix-induced drift (each P3-tagged fix read standalone) · B blind-spot swap - (i) overclaim of
EFFICACY (mirror of pass 3's risk framing), (ii) "recorded negative" claims quoted stronger than
their query-log anchor, (iii) timeline/regulatory freshness vs an Oct-2026 submission,
(iv) internal dates/version-stamp coherence · C fresh end-to-end read of the attack map as ONE
coherent decision instrument.

**External spot-verification this pass (my own fetches/searches, not the authors'):**
- **Ataluren regulatory state - LIVE re-check (DDG, 2026-09-05):** PTC Therapeutics press release
  dated Feb 12, 2026 (ir.ptcbio.com/news-releases/news-release-details/ptc-therapeutics-provides-
  regulatory-update-translarnatm-2; corroborated by FiercePharma, PharmExec, RareDiseaseAdvisor,
  CureDuchenne): PTC **WITHDREW its NDA resubmission** for Translarna after FDA feedback that the
  data were unlikely to meet the approval threshold. → The pack's "FDA CRL 2025, NDA withdrawn
  2026" is **VERIFIED CURRENT** (one compression nuance: the withdrawn object was the NDA
  *resubmission*, i.e. regulatory collapse is if anything deeper than the map states - the last
  revival attempt also failed). The readthrough exclusion datum is NOT stale.
- **Human MET splice-switching ASO program - queried (DDG, 2026-09-05):** all 10 hits on
  "MET exon 14 skipping antisense oligonucleotide clinical trial human patients" concern METΔex14
  as a *mutation-driven* oncology target treated with TKIs (gumarontinib, ensartinib, capmatinib-
  class) or amivantamab. **No human splice-correction ASO program for MET located.** Grounds
  finding P4-2.

---

## STOP-RULE METRIC

**EXPLICIT MAJOR COUNT THIS PASS: 0** · **BLOCKERS: 0** · **MINOR: 5** (P4-1…P4-5)

Decay trajectory: **8 → 2 → 2 → 0.** The two pass-3 majors (P3-1, P3-2) fixed at the controller
layer hold standalone-true at every tagged site; no fix regressed; no P2 fix-site drifted further
(re-audited inline this pass). Nothing disposition-bearing moved: every candidate verdict, the
six-assay validation plan, and every dose/exposure parameter in the live artifacts survive this
pass unchanged.

**CLOSURE VERDICT: CLOSED-WITH-RESIDUAL-RISK.** Condition per SCOPE_DECISION ("two consecutive
zero-major passes, the second over fresh axes; hard ceiling pass 4; pass-4 zero = sufficient
closure with residual risk declared") is **SATISFIED at the hard ceiling**. No pass 5 exists.
Named residuals (non-gating, presentation/audit-trail class only): P4-1…P4-5 below, recommended
for one last controller micro-integration before report generation. Methodological residual
(declared, per the runbook's heuristic-decay caveat): a zero-major pass bounds *detected* majors,
it does not prove their absence - that is why closure carries the residual-risk label and not a
clean bill.

---

## P3 fix ledger - all nine fixes verified at tagged sites

| # | Verdict | Evidence (standalone read) |
|---|---|---|
| P3-1 (EXIST-3 band) | **FIXED, 4/4 sites, zero drift** | Map named window: "trial-validated lower band of **3–7 ng/mL** (EXIST-3 low-exposure arm, efficacious from age 2.2; **true floor = its 3 ng/mL lower edge**)" + "**canonical target 5–10**" (also discharges P3-9b). Map rule 2: "trough 3–7 ng/mL (EXIST-3 low-exposure arm…)". TSV everolimus row: "low band 3-7 ng/mL (P3-1)". WORKFLOW line 51: "validated low band 3-7 ng/mL [P3-1-corrected]". Grep for `3–5`/`3-5` across map/TSV/governance: only surviving hit is pass-3's own changelog entry *describing* the error (historical record, correct as written). Controller dropped the 3–5 coinage entirely rather than retaining it as a "pack working floor" - cleaner than the pass-3 suggested fix; no fix-induced drift. |
| P3-2 (TSV ASO oligo-scope) | **FIXED, true standalone** | TSV ASO row consensus_status: "no human non-muscle/non-CNS **OLIGONUCLEOTIDE** splice correction (small-molecule class precedented: risdiplam/branaplam) (P3-2)". Matches map delivery bullet and the ASOdeep erratum rescope. (Residual erratum-side tension = P4-2, minor.) |
| P3-3 (readthrough MoA) | **FIXED** | TSV readthrough MoA now: "at best marginal to the ~13% competence line (corner case 10%+3%=13% only) (P3-3)" - mirrors the map's P2-3-corrected clause verbatim. |
| P3-4 (census ordinal) | **FIXED** | Map senolysis now: "**the post-2011 census**, none pro-incidence" - ordinal removed; Ovadya demotion clause retained. Count ambiguity eliminated exactly as prescribed. |
| P3-5 (branaplam datum) | **FIXED** | Map delivery bullet: "branaplam ph2b RCT - **early-terminated for peripheral neuropathy, 85.7% initial cohort, the adverse datum the disclosure must carry**". Matches pass-3's abstract-verified datum (PMID 41491108). |
| P3-6 (navitoclax context) | **FIXED, both demanded sites** | Map rule 5: "oncology setting **IN COMBINATION REGIMENS (not monotherapy)**, children ≥4 y, RP2D 25 mg <45 kg (Pullarkat 2021)". TSV senolysis row now names which claim fell and which survived: "overturned the no-pediatric-senolytic-**CLASS-drug-exposure** claim (combination-regimen oncology setting, P3-6); **indication gap survives**". |
| P3-7 (governance count) | **FIXED** | WORKFLOW line 48 now: "(**recounted 8 majors** incl. F3,F13 per pass-2 P2-5/pass-3 P3-7; **the five listed here were the top-severity subset**: …)" - both contradictions killed (8=7+1 internally consistent with SCOPE_DECISION's "F1–F7 + F13"; the five-item list explicitly labeled a subset). |
| P3-8 (wave-4 labels) | **FIXED at all 4 tagged sites; convention side-effect = P4-1** | Map now reads wave-4 Q9 / Q10 / Q12 / Q9-correction at every pass-3-tagged joint. But the fix adopted the file-prefix convention at those four sites while Q5–Q8 references elsewhere in the *same document* still use campaign numbering ("wave-2 Q5/Q6/Q7a/Q7b/Q7c/Q8") - see P4-1. |
| P3-9 (two adoptions) | **FIXED, both limbs** | (a) Level 2: "**abundance targets a WINDOW, not a ceiling - BUB1B overexpression drives chemo resistance (PMID 34545188)**" now in the map (previously TSV-only). (b) Named window carries "canonical target 5–10 ng/mL" (Q9 consequence #2 adopted, not silently skipped). |

Pass-2 fix-sites re-audited this pass: P2-1 (Tang attribution) and P2-2 ("non-inferior" appears
only negated, both artifacts) remain text-accurate; P2-4 (16–22 % band) corner arithmetic
re-derived once more: (1−0.3)·10 % + 0.5·0.3 = 7 % + 15 % = 22 % ✓.

---

## Numbered findings (all MINOR; none touches a disposition, dose parameter, or the assay plan)

### P4-1 - MINOR (blind-spot swap iv + end-to-end; P3-8 side-effect): mixed wave-numbering conventions inside one decision instrument

- **Claim:** the attack map cites Q5–Q8 as "**wave-2** Q5", "**wave-2** Q6", "**wave-2** Q7a/b/c",
  "**wave-2** Q8" (framing heading; AMPK paragraph; Level-1 delivery bullets; NK-monitoring
  clause) - campaign numbering - while the same map cites Q9–Q12 as "wave-4" (P3-8 fix) and its own
  provenance block pairs campaign numbers with the file convention (wave-1 docs = `wave2_*.md`).
  `candidates.tsv` uses the *file* convention throughout for the same works: "wave-3 Q6", "wave-3
  Q7", "[wave3 Q8]" (files exist as `wave3_AMPKaxis.md`, `wave3_ASOdeep.md`,
  `wave3_ImmunoSurveillanceNK.md`). `WORKFLOW_CONSENSUS.md` line 49 calls the same dispatch
  "wave-2".
- **Why it matters (and why not MAJOR):** no claim is false under *its own* convention - the
  discrepancy is pure audit-trail join-fuzz, and every citation also names the question (Q#) and
  usually the doc file, so a reader can reconcile. But the P3-8 fix adopted file numbering at the
  four freshest joints and left the older campaign-numbered sites in place, so the FINAL decision
  instrument now mixes both conventions in adjacent paragraphs - precisely the label-hygiene class
  the adversarial layer exists to police. Falsification test: `grep "wave-2 Q" / "wave-3 Q"` on the
  two live artifacts - two conventions, one document family. **Fix (one pass):** standardize to
  file numbering ("wave-3 Q5–Q8") everywhere in the map, or add one convention-declaring footnote.
- **Why pass 3 could not see this:** pass 3's checklist (D) compared the four *freshest* labels
  against the file names and confirmed them correct - it never ran the cross-document convention
  sweep. This is the pass-3-structurally-invisible class the pass-4 brief anticipated.

### P4-2 - MINOR (blind-spot swap ii inverted: unlogged positive claim; P3-2 fix-surface residue): "MET-oncology" inside the ASOdeep erratum's surviving-programs list

- **Claim:** `wave3_ASOdeep.md` erratum: "(survived: **all human ASO splice programs are DMD /
  MET-oncology / intrathecal / ocular**)". On its face, a *human oncology (non-muscle, non-CNS)
  splice-ASO program* contradicts the very rescope the erratum derives - the P3-2 wording now in
  both live artifacts: "no human non-muscle/non-CNS OLIGONUCLEOTIDE splice correction".
  "MET-oncology" appears nowhere else in the doc (only occurrence), carries no citation, and my
  external query located no human MET splice-correction ASO program (retrieved literature treats
  METΔex14 as a mutation target for TKIs/antibodies).
- **Why MINOR, not MAJOR:** the claim lives only in the erratum's parenthetical, not in any
  decision row; the load-bearing fix sentences in map/TSV are unopposed by locatable evidence
  (no counterexample found); worst case the author meant a preclinical MET program - making the
  parenthetical wrong, not the decision artifacts. Falsification test: produce the human MET
  splice-ASO program citation, or delete "MET-oncology" from the list. **Fix (three words).**

### P4-3 - MINOR (end-to-end cross-row tension): "metformin senomorphic fallback" (senolysis row) vs AMPK-axis closure (AICAR row)

- **Claim:** TSV senolysis approval_status: "rapalog/**metformin senomorphic fallback**". TSV AICAR
  row + map AMPK paragraph: the energy-stress triangle is EMPTY, metformin = "WATCH residue behind
  a ≤100 µM proband-cell co-test", Lyu 2022 1–16 mM genotoxicity cap. A closed-candidate molecule
  reappears in another row as a "fallback" without the WATCH constraint traveling with it. The map
  itself is clean (senolysis rules contain no metformin arm); the tension is TSV-internal.
  Falsification test: read both TSV rows against each other. **Fix (one clause):** "metformin
  senomorphic *availability* noted; candidacy governed by AMPK-axis closure (WATCH only)".

### P4-4 - MINOR (blind-spot swap iv: version-stamp coherence): attack-map banner is two integrations stale

Map header: "**v2 (post-wave-1 consensus, 2026-09-05). Supersedes v1**" - but the document body now
carries wave-3 and wave-4 integrations and P1/P2/P3 corrections. `SCOPE_DECISION.md`'s stop-rule
passage now says "hard ceiling pass 4" while `WORKFLOW_CONSENSUS.md` line 49 still records
"**expected 2 more passes, hard ceiling 3**" - the standing-procedure document and the executed
sequence disagree on the hard ceiling. Both are label-layer, no decision content. Falsification
test: the two quoted lines. **Fix:** bump the map banner to "(post-confirmation-wave,
P1–P3-integrated)"; correct line 49's ceiling to 4 with a one-clause note.

### P4-5 - MINOR (blind-spot swap iii, residue class): no finding of substance - one compression worth a footnote

The one live timeline claim I re-checked externally (ataluren) is current, but the map's "NDA
withdrawn 2026" elides that the withdrawn object was the *resubmission* - a reader could
under-read the depth, and a hostile judge could over-read the compression. Direction is safe (the
strengthened datum helps the exclusion). Falsification test: PTC PR Feb 12, 2026. **Fix
(optional):** "NDA resubmission withdrawn 2026 (PTC PR)". Downgraded from a substantive finding:
no stale claim exists anywhere I tested (CAPP3 2026 results integrated; Nakano 2024 + 2026-census
publications present; FDA "Plausible Mechanism Framework (2026)" guidance ref current; PREVENT 2024).

---

## Blind-spot attack results

| Attack class | Outcome |
|---|---|
| **B(i) Efficacy-overclaim** (do live artifacts claim drug benefit for THIS genotype?) | **CLEAN.** Every efficacy-adjacent sentence is hedged at its load point: everolimus = "Grade-D rationale / pediatric chronic feasibility only, not mechanism match"; ASO = conditional "IF Δ716-761+E715G works", "WORSE than nothing if not"; arimoclomol = "adjunct only… UNPROVEN"; NMN = WATCH; senolysis = gate-first, "lives or dies behind Gate-0/assay data, never on literature momentum"; Suijkerbuijk fragment support explicitly [INFERENCE]-tagged; SCOPE_DECISION's GRADE rule ("no strong recommendation rests on a very-low-grade claim") is actually obeyed. No corrective finding. |
| **B(ii) Negative-claim overreach** (recorded negatives quoted stronger than their query logs) | **CLEAN where checkable from the artifact set.** Load-bearing negatives carry their anchors: senolysis "four recorded queries + 2025–26 sweep"; Mannick "two recorded negative queries"; ped-NK-under-rapalog "recorded gap"; MVA-roll "five-registry live census (positive controls per registry)"; abundance census "4 databases + patents"; cfDNA "no benefit-confirming RCT; CHARM2 excludes MVA" (pass-3 verified the CHARM2 eligibility list live - MVA absent). The one unanchored claim found is the inverse problem (P4-2, an unlogged positive). |
| **B(iii) Timeline freshness for Oct-2026** | **CLEAN.** Ataluren verified current live (above, strengthened); 2026-dated corroborations present in the artifact set (Lalinde-Gutiérrez 2026, Zhou 2026, Hamburger 2026, Valdivieso 2026, Pharmacol Rev 2026, CAPP3 Lancet G&H 2026); registry censuses re-dated 2026-09-05; no pre-2026 claim I sampled has gone stale. Residue = P4-5 (compression, optional). |
| **B(iv) Dates/version coherence** | Two ambiguities, both MINOR: wave-convention split (P4-1) and governance stamps (P4-4). Same-day v1→v2 supersession is sprint-consistent. |
| **C End-to-end fresh read** | The map reads as ONE coherent instrument: genotype → conditional ASO program → adjunct stabilization → Grade-D rapalog with mandatory honesty datums → gate-first senolysis → verified surveillance backbone → exclusion jurisprudence ↔ census framing all cross-resolve without contradiction; allele math, competence-curve anchors, and floor/band numbers are consistent across map and TSV. Residual presentation cracks are P4-1 and P4-3 only. |

## What survives contact unchanged

1. **All nine P3 fixes** (ledger above) - every one reads standalone-true at its tagged sites;
   P3-1's band/floor/canonical-target trifecta is now exactly right at four sites and the 3–5
   coinage is extinct from every live artifact.
2. **Every P2 fix re-audited** - P2-1, P2-2, P2-4 remain text-accurate; "non-inferior" survives
   only in negated form.
3. **The ataluren exclusion datum** - external re-check shows the regulatory collapse deepened
   (resubmission also withdrawn, Feb 2026); no staleness exposure for the Oct-2026 submission.
4. **Every dispositive claim pass 3 marked sound** - the Q9 window arithmetic, Q10 registry zero
   with positive controls, Q11 overturns (with P3-6's which-claim-fell labeling now exact), Q12
   SIRT2-direction resolution and window sentence, the three controller errata.
5. **The decision substance end-to-end** - dispositions, the six-assay stack, exposure windows,
   honesty datums, exclusion jurisprudence: untouched by anything found this pass.
6. **The stop-rule machinery** - four passes, decay 8→2→2→0; the two majors in each of passes
   2–3 were integration/label defects, none ever touched underlying evidence or dispositions.

## Named residual risk (declared, per closure rule)

- **R1:** minors P4-1…P4-5 remain unfixed at this pass's read; all are presentation/audit-trail  - 
  none changes a decision. Recommended single controller micro-integration before report
  generation (total: ~5 sentence-level edits).
- **R2 (methodological):** zero majors bounds *detected* majors; adversarial review is a sampling
  process. The runbook's heuristic-decay caveat stands; the "first-intervention" and
  "class-closed" negatives rest on the census logs cited, periodically re-attackable if the field
  moves before October submission.
- **R3:** the pack's deepest load remains the UNMEASURED Δ716-761+E715G construct function - that
  is by design (it is the gated decision), flagged so closure is not read as claiming otherwise.

*Verification note: this pass's external checks were my own - live ataluren PR corroboration and
the MET-program query (sources quoted above). All repo claims are assessed against files I actually
read in full, current state, paths in the header. No finding rests on the authors' own
verification.*
