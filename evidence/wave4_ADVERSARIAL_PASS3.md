# Wave-4 Adversarial Review - PASS 3 (stop-rule test)

**Reviewer:** AdversarialKimi3 (out-of-family red team, same lineage as passes 1–2) · **Date:** 2026-09-05
**Scope:** `TRACK2_ATTACK_MAP.md` (post-Q9/Q10/Q11/Q12) · `wave4_PediatricRapalogDosing.md` ·
`wave4_SurveillanceToday.md` · `wave4_NegationReattack.md` · `wave4_AbundanceChemistry.md` ·
`wave3_ADVERSARIAL_PASS2.md` (pass-2 findings, AdversarialKimi2 lineage) ·
`candidates.tsv` · CONTROLLER ERRATA in `wave3_PrecedentCensus.md`, `wave3_SenolysisF6verifier.md`,
`wave3_ASOdeep.md` · `WORKFLOW_CONSENSUS.md`, `SCOPE_DECISION.md` (governance).
**Attacks run per checklist:** A fix-fidelity incl. fix-induced-drift · B overturn-verification of the
now load-bearing Q11 claims · C Q9 dosing arithmetic · D cross-seam consistency (window block vs
rule 2 vs candidates.tsv) · E new omissions.

**External spot-verification this pass (my own re-fetches, not the authors'):**
- PMID 33593877 Pullarkat 2021 - full PubMed abstract read: "pediatric and adult patients…
  A recommended phase II dose of 50 mg navitoclax for adults and **25 mg for patients <45 kg**"
  ([DOI](https://doi.org/10.1158/2159-8290.CD-20-1465)). VERIFIED VERBATIM.
- PMID 27613521 French 2016 EXIST-3 - abstract read: "trough exposure concentrations of
  everolimus, **3-7 ng/mL (low exposure) and 9-15 ng/mL (high exposure)**"
  ([DOI](https://doi.org/10.1016/S0140-6736(16)31419-2)). → grounds finding P3-1.
- PMID 30564495 EXIST-3 extension + **PMC6276348 full text** (JATS XML pulled live): "Two deaths
  occurred during the extension phase - **both in pediatric patients** - because of pneumonia (suspected
  to be treatment related) and SUDEP… Two additional deaths… **1 in a child because of septic shock**
  (suspected to be treatment related)…" → the pack's "two pediatric treatment-related infection
  deaths" honesty datum is VERIFIED VERBATIM (pneumonia + septic shock, both children).
  ([DOI](https://doi.org/10.1212/CPJ.0000000000000514)).
- PMID 25540326 Mannick 2014 ([DOI](https://doi.org/10.1126/scitranslmed.3009892));
  PMID 41491108 branaplam VIBRANT-HD ([DOI](https://doi.org/10.1038/s41591-025-04117-4)) - identities
  confirmed; branaplam abstract contains the **early-termination** fact used in finding P3-5.
- PMID 41012109 Yuan 2025 KHE-vaccine cohort ([DOI](https://doi.org/10.3390/vaccines13090903))  - 
  n=56, live MMR under sirolimus confirmed.
- PMID 39264246 Nakano 2024 ([DOI](https://doi.org/10.1158/1078-0432.CCR-24-1098)) - identity
  confirmed (AACR 2nd workshop, July 2023, MVA in scope).
- PMID 39726432 PREVENT/Capal 2024 ([DOI](https://doi.org/10.1002/cns3.20070)) - n=5, <6 mo,
  94 % of troughs in 5–15 ng/mL target confirmed verbatim.
- ClinicalTrials.gov API v2 live (2026-09-05): **NCT03181126** minimumAge = "4 Years", COMPLETED,
  enrollment 69 actual, interventions venetoclax+navitoclax+chemotherapy ✓. **NCT06726642 (CHARM2)**
  RECRUITING, start 2024-04, enrollment 1000 (ESTIMATED), eligibility = HBOC/Lynch/NF1/LFS/PALB2/HDGC
  - MVA/CIN absent ✓ (verifies Q10's exclusion claim).

---

## STOP-RULE METRIC

**MAJOR COUNT THIS PASS: 2** (P3-1, P3-2) · **BLOCKERS: 0** · **MINOR: 7**

Decay trajectory: 8 → 2 → 2. The line flattens rather than falling - consistent with the pack now
being deep enough that each pass finds errors of diminishing blast radius but constant density
(citation-label fidelity at the controller/consensus layer, not reasoning). Neither major flips a
disposition, shrinks a candidate, or touches the validation plan; both are externally checkable
label errors in exactly the sentence classes passes 1–2 policed.

**STOP-RULE RECOMMENDATION: CONTINUE.** The declared rule (SCOPE_DECISION: two CONSECUTIVE
zero-major passes, the second over fresh axes; hard ceiling pass 4) is NOT met - this pass found
2 majors. Sequence per plan: integrate P3-1/P3-2 (+ minors) at controller layer → pass 4 against the
integrations. If pass 4 returns zero majors, close. The confirmation wave itself (Q9–Q12) is fully
integrated and its fresh claims survived external spot-verification almost intact - the residual
risk is controller-layer label hygiene, and the stop-rule machinery is detecting exactly that.

---

## Per-target verdicts

| Checklist target | Verdict |
|---|---|
| A. Fix-fidelity (P2 fixes + Q9–Q12 integrations vs source docs) | **8 P2 fix-sites text-accurate overall (5 fully, 3 partial); Q10/Q11/Q12 map-side integrations faithful.** P2-1 (Tang attribution), P2-2 (CAPP3, map + census erratum), P2-4 (16–22 % band), P2-6 (Gate-0 panel), P2-7 (Mannick de-flooring), P2-8a (CNS dual-compartment) hold. **Two fix-fidelity breaches (P3-1 band label; P3-2 TSV non-propagation)**; three fix-residue/drift minors (P3-3, P3-4, P3-7). |
| B. Overturn-verification (navitoclax, risdiplam/branaplam treated as fresh claims) | **HELD on the core claims.** Pullarkat 2021 abstract verified verbatim (pediatric + 25 mg <45 kg RP2D); NCT03181126 registry fields verified live (min age 4, COMPLETED, venetoclax+navitoclax+chemo arms); risdiplam ph1 + branaplam ph2b identities verified. Setting-vs-indication distinction correctly carried everywhere. Two honesty-of-compression minors (P3-5, P3-6). |
| C. Dosing arithmetic (4.5–5 mg/m² → 3.4–3.8 mg; 7–40× Mannick ratio; EXIST-3 band attribution) | **2/3 audited quantities pass.** mg/m²→mg: 0.75 m² × 4.5–5 = 3.375/3.75 → ≈3.4/3.8 ✓. Mannick ratio: 3.4/0.5 to 3.8/0.1 = 6.8–38× ≈ "7–40×" ✓. **The EXIST-3 trough-band attribution FAILS: the trial's low-exposure arm is 3–7 ng/mL; the pack now quotes "EXIST-3 low-trough band 3–5" (P3-1, MAJOR).** |
| D. Cross-seam consistency (named-window block vs senolysis rule 2 vs candidates.tsv) | **One story on substance; three documents share the ONE wrong band label (P3-1).** candidates.tsv ASO row did not receive the Q11 rescope (P3-2). Otherwise map/TSV/errata tell a single consistent story (Mannick non-translatable; NK-hold trigger; TDM calendar; honesty datums). |
| E. New omissions the confirmation wave should have caught | Three: branaplam's early termination omitted from the precedent disclosure (P3-5); Q12's therapeutic-window caveat (BUB1B-overexpression chemo-resistance) lives in candidates.tsv but never made the attack map (P3-9a); Q9's own recommended "titrate to 5–10, lower half" neither adopted nor declined (P3-9b). |

---

## Numbered findings

### P3-1 - MAJOR (checklist A+C, confirmation-wave-introduced label error, propagated controller-wide): "EXIST-3 low-trough band" is quoted as 3–5 ng/mL; the trial's arm was 3–7 ng/mL

- **Claims affected (four sites):**
  1. attack map Level 3, named window: "a trial-validated monitoring floor at 3–5 ng/mL (**EXIST-3 low-trough band**, efficacious from age 2.2)";
  2. attack map senolysis rule 2: "floored at a trial-validated pediatric band: trough 3–5 ng/mL (**EXIST-3 low-trough arm**, efficacious from age 2.2)";
  3. candidates.tsv everolimus row: "trough 5-15, low floor 3-5 ng/mL";
  4. WORKFLOW_CONSENSUS line 51: "validated floor 3-5 ng/mL".
  The coinage originates in wave4_PediatricRapalogDosing.md controller-consequence #1 ("floored at
  trough 3–5 ng/mL - the lowest pediatric efficacy-validated band (EXIST-3 LT, ≥2.2 y)") even though
  the same doc states the arm correctly three times elsewhere ("EXIST-3's low-trough arm
  *(3–7 ng/mL)* was efficacious in children from age 2.2").
- **Evidence:** According to PubMed (my own abstract fetch, PMID 27613521,
  [DOI](https://doi.org/10.1016/S0140-6736(16)31419-2)): EXIST-3 randomized to "trough exposure
  concentrations of everolimus, **3-7 ng/mL (low exposure)** and 9-15 ng/mL (high exposure)". There
  is no 3–5 sub-band in the trial.
- **Why MAJOR, not a P2-4-class minor:** it is a *citation attribution* of a quoted numeric
  parameter to a trial that does not contain it, in the single most externally checkable sentence
  class of the pack (a registered-trial dose parameter any judge can read in the abstract). Same
  error class as P2-1/P2-2. It is load-bearing only in the soft sense - the dose-hold floor's
  operating point barely moves, because the floor VALUE 3 ng/mL (lower edge of the 3–7 target) is
  stated correctly elsewhere - but a reviewer running the citation finds "3–7" where the pack says
  "3–5" and discounts the rest of the dosing paragraph.
- **What is TRUE and must be preserved in the fix:** the floor value 3 ng/mL (3–5 is a conservative
  sub-band INSIDE the validated 3–7 target); efficacy from age 2.2 (verified); the two pediatric
  treatment-related infection deaths (verified verbatim against PMC6276348 full text, my fetch  - 
  "both in pediatric patients… 1 in a child because of septic shock").
- **Falsification test:** French 2016 abstract, Methods, first sentence. **Fix (one clause, four
  sites):** "…with a trial-validated floor at 3 ng/mL - the lower edge of EXIST-3's low-trough arm
  (target 3–7 ng/mL, efficacious from age 2.2); the 3–5 ng/mL sub-band is the pack's conservative
  working floor, not the trial's band."

### P3-2 - MAJOR (checklist A+D, fix non-propagation): candidates.tsv ASO row still carries the Q11-overturned sentence; the consensus record and the ASO erratum disagree

- **Claim:** candidates.tsv, ASO exon-17 row `consensus_status`: "delivery = rate-limiter (**no
  human non-muscle/non-CNS splice-switch precedent**); PMO patents expired; n-Lorem ~$1M/lifetime
  path exists".
- **Evidence:** wave4_NegationReattack.md verdict (a): that literal sentence is FALSE as written  - 
  approved human systemic (oral, body-wide) splice-switching precedent exists in the small-molecule
  class (risdiplam, approved, blood-level SMN2 PD, PMID 30302786; branaplam ph2b RCT, PMID
  41491108). The controller rescoped the attack-map delivery bullet ("the unprecedented limb is
  specifically OLIGONUCLEOTIDE-class…") and appended the ASOdeep erratum, whose final sentence
  reads: "**The attack map delivery bullet carries the rescoped wording.**" True - but
  candidates.tsv, the file the workflow defines as THE consensus record ("votes: candidates.tsv
  `consensus_status` column"), was left carrying the overturned form. No erratum covers the TSV.
- **Failure mode:** exact P2-1/P2-2 parity - an externally checkable literal claim, false, in the
  consensus-facing artifact, rows away from rows that WERE updated (senolysis: navitoclax; NMN:
  Q12). Any downstream consumer regenerating report text from candidates.tsv re-instates the error
  the whole Q11 re-attack was commissioned to kill.
- **Falsification test:** read the ASO row of candidates.tsv against wave4_NegationReattack §(a).
  **Fix (one clause):** "delivery = rate-limiter (no human non-muscle/non-CNS OLIGONUCLEOTIDE
  splice correction; small-molecule splice-switching HAS human systemic precedent - risdiplam
  approved, branaplam ph2b - which does not rescue ASO delivery)".

### P3-3 - MINOR (fix residue, P2-3 class): candidates.tsv readthrough row still corner-false

TSV row "Nonsense readthrough (ataluren/ELX-02)": "modeled +0.3-3% WT abundance - **below** ~13%
competence line". Pass-2 P2-3 flagged this dual-locale; the attack map was fixed ("at best
marginal… only in the corner case: 10 % + 3 % = 13 %; f_escape dose-context-dependent"), the TSV
row was not. Harmless for disposition (EXCLUDE-AS-PRIMARY rests on regulation + unreliable yield)
but it is the same arithmetic slogan P2-3 already adjudicated corner-false.
**Fix:** mirror the map's corrected clause in the TSV row.

### P3-4 - MINOR (fix-induced count ambiguity, P2-8 fix): "five models" names four

Attack map senolysis: "Reverse census beyond Baker 2011: **five models**, none pro-incidence
(Haston 2023…; Kumar 2025…; Gallanis 2023…; Ovadya 2018… - not an incidence datum)". Four items are
in the parenthesis; the fifth is Baker 2016, named only in the preceding sentence; and the P2-8
footnote itself demotes Ovadya out of the incidence census (leaving Baker 2016, Haston, Kumar,
Gallanis = four incidence-relevant models). A judge counting the parenthesis gets four, the claim
says five, and its own footnote says the count is fuzzy by design. Truth survives; presentation
invites a miscount.
**Fix:** "four incidence-outcome models (Baker 2016, Haston, Kumar, Gallanis), none pro-incidence;
Ovadya 2018 survival-positive, no tumor endpoint". Falsification test: count the verifier's Q2
table rows minus the counterweight row.

### P3-5 - MINOR (checklist E omission, honesty of disclosure): branaplam precedent quoted without its early termination

Q11 doc's branaplam row reads "human ph2b RCT"; the map repeats "branaplam ph2b RCT" as the second
limb of the small-molecule modality precedent. Per the abstract I fetched (PMID 41491108,
[DOI](https://doi.org/10.1038/s41591-025-04117-4)): "Of the 21 participants in the initial cohort
receiving branaplam 56 mg weekly, 18 (85.7%) showed at least one sign or symptom of peripheral
neuropathy. This safety signal… **triggered the early termination of VIBRANT-HD**." The doc's own
citation-verifier read this abstract (the termination is in the abstract, not the deep text) and
the pack is otherwise scrupulous about adverse datums. The modality-precedent claim is unaffected
(randomized systemic dosing happened), but quoting this citation without its most famous fact is
selective.
**Fix (one clause):** "branaplam ph2b RCT (early-terminated for a peripheral-neuropathy signal;
cited for modality precedent only)".

### P3-6 - MINOR (checklist B compression): navitoclax context lost in the map; TSV mislabels which claim was overturned

(a) Attack map senolysis rule 5: "navitoclax (ABT-263, canonical BCL-xL senolytic) HAS published
pediatric exposure - oncology setting, children ≥4 y". Verified (Pullarkat abstract + NCT03181126
fields): the exposure was **deliberately low-dose navitoclax combined with venetoclax + multi-agent
chemotherapy** (the trial's design was platelet-sparing; monotherapy navitoclax is thrombocytopenia-
limited). The wave-4 doc's own required-correction sentence carries "monotherapy-vs-combination
contexts differ - these data de-risk drug-class pediatric chronic exposure only"; the map's
compression dropped that clause. A reader could over-infer single-agent tolerability.
(b) candidates.tsv senolysis row: "navitoclax pediatric exposure **overturned the no-pediatric-
senolytic claim** (oncology setting); indication gap survives" - what survived (no pediatric
senolytic INDICATION) and what was overturned (no pediatric senolytic-CLASS EXPOSURE) are different
claims; the parenthesis rescues a careful reader but the clause is self-touching.
**Fix:** restore the combination/low-dose-by-design clause at rule 5; rephrase the TSV row to
"overturned: no-pediatric-senolytic-CLASS exposure (oncology, combination therapy); survives:
no pediatric senolytic INDICATION".

### P3-7 - MINOR (fix residue, P2-5 class): WORKFLOW_CONSENSUS line 48 still says "(5 majors: …)"

P2-5 required the pass-1 major count (8) fixed in both governance docs. SCOPE_DECISION was fixed
("8 majors… Empirical calibration (corrected per P2-5)"); WORKFLOW_CONSENSUS line 50 logs the same
correction - but line 48 still reads "13 conditions incorporated (**5 majors:** …)" followed by SIX
listed items (double contradiction: wrong count, and a list that disagrees with its own
parenthesis). Cosmetic-level now that the correction exists two lines below, but the audit trail
should not contradict itself in the same file.
**Fix:** "(8 majors: [the six-item list])".

### P3-8 - MINOR (documentation hygiene): wave-4 docs cited as "wave-3" at four attack-map sites

"Direction resolved (**wave-3 Q12**)"; "Named pediatric exposure window (**wave-3 Q9**…)";
"Surveillance backbone - verified to 2026 standard (**wave-3 Q10**)"; "(**wave-3 Q9 correction** of
the P2-7 interim wording)". Q9–Q12 are wave-4 documents (their own headers; wave-3 was Q5–Q8). The
audit-trail chain (wave# ↔ doc file) breaks at exactly the four freshest joints.
**Fix:** wave-3 → wave-4 at these four sites (Q7 and Q8 references are correctly wave-3).

### P3-9 - MINOR (checklist E): two silently non-adopted wave-4 author recommendations

(a) **Q12 therapeutic-window caveat absent from the attack map.** candidates.tsv NMN row carries it
("BUB1B overexpression drives chemo resistance, PMID 34545188 - abundance targets a window, not a
ceiling"); both wave-4 docs treating it flag it as the one genuinely adversarial datum of the
census (Q12 doc remark; Q11 §(d) caution row); the attack-map Level-2 paragraph closes the
abundance census without it. The single most line-of-fire datum against the whole abundance
strategy deserves the map, not only the TSV.
(b) **Q9 controller-consequence #2 ("titrate to trough 5–10 ng/mL, lower half of label band")
neither adopted nor declined with reasoning.** The map names the full 5–15 label band + floor; the
Q9 author's operational recommendation to *aim* at the lower half is a real, actionable difference
(infection hazard scales with trough). Adopting it or explicitly declining it are both defensible;
silence is not.
**Fix:** (a) one clause in Level 2; (b) one clause in the named-window block.

---

## Pass-2 fix ledger (all 8, verified this pass)

| # | Fixed? | Note |
|---|---|---|
| P2-1 Tang attribution | **YES, text-accurate** | map Level 3 + TSV everolimus row both now state mTOR neutrality = trisomic-MEF datum only, never on Bub1b^H/H |
| P2-2 CAPP3 | **YES, text-accurate** | map framing bullet + census erratum both state "formal non-inferiority not concluded"; per-protocol HR CI crossing the 1.5 boundary quoted correctly; "non-inferior" appears only negated |
| P2-3 readthrough slogan | **PARTIAL** | map fixed; TSV row residue = P3-3 |
| P2-4 band 16–22 % | **YES** | top corner re-derived by me: (1−0.3)·10 % + 50 %·0.3 = 7 + 15 = 22 % ✓; TSV ASO row also updated |
| P2-5 governance count | **PARTIAL** | SCOPE_DECISION fixed; WORKFLOW_CONSENSUS line 48 stale = P3-7 |
| P2-6 Gate-0 immune panel | **YES** | validation plan #0 carries the NK/NF-κB baseline panel verbatim |
| P2-7 Mannick floor | **YES** (band-label defect inside it = P3-1) | rule 2 rewritten; Mannick demoted to direction-setting; "must never be targeted in a child" present |
| P2-8a CNS dual-compartment | **YES** | separate intrathecal-program sentence present |
| P2-8b Ovadya census | **YES-with-wobble** | footnote added; count presentation left ambiguous = P3-4 |

## What survives contact unchanged

1. **The Q9 exposure-window verdict substance.** mg/m²→mg arithmetic, Mannick non-translatability,
   3 ng/mL as the validated efficacy floor, PREVENT as the only true prophylactic analog (94 %
   troughs in target, abstract-verified), the two pediatric treatment-related infection deaths
   (full-text-verified), the <6-y age-stratified infection ratios - all held under external re-fetch.
   Only the band label is wrong (P3-1).
2. **Q10 surveillance backbone + registry census.** Nakano 2024 identity verified; CHARM2's MVA/CIN
   exclusion verified LIVE against the CT.gov record (eligibility = HBOC/Lynch/NF1/LFS/PALB2/HDGC);
   the five-registry zero-MVA census with positive controls is methodologically the strongest
   negative in the pack; risk-point prohibition correctly enforced.
3. **Q11 navitoclax overturn - the load-bearing claim itself.** Pullarkat 2021 abstract verbatim
   ("25 mg for patients <45 kg"), NCT03181126 min-age-4 / COMPLETED / 69-enrolled / combination
   arms, RAVEN + two pediatric expanded-access programs - all check out. The senolytic-INDICATION
   gap survives intact.
4. **Q11 small-molecule splice-modality disclosure** - risdiplam (approved, peripheral PD) and
   branaplam (ph2b RCT) verified as cited; the ASO delivery constraint correctly unchanged.
5. **Q12 abundance census + SIRT2/NAD+ direction resolution** - internally consistent against the
   cited row set (K668 interphase degradation mark vs K243/250 mitotic-protective acetylation);
   SIRT2-inhibitor prohibition and the site-less-phrasing prohibition are sound and safe.
6. **The three CONTROLLER ERRATA** - all accurate against my spot-checks (census erratum matches
   the CAPP3 abstract as I verified it in pass 2; senolysis erratum matches Pullarkat + the live
   registry; ASOdeep erratum matches the Q11 verdict), and erratum-vs-body authorship separation is
   respected everywhere.
7. **The stop-rule machinery itself** - calibration sentence, pass-2 fix ledger, confirmation-wave
   trigger, and the heuristic-decay caveat all behaved as designed.

## Required fixes before pass 4 (blocking order)

1. **P3-1 (MAJOR):** band-label correction at four sites (map named-window, map rule 2, TSV
   everolimus row, WORKFLOW_CONSENSUS line 51) - and its origin in wave4 consequence #1.
2. **P3-2 (MAJOR):** Q11 rescope into candidates.tsv ASO row.
3. P3-3 / P3-4: TSV readthrough clause; reverse-census count sentence.
4. P3-5 / P3-6: branaplam termination clause; navitoclax combination-context clause + TSV claim
   label.
5. P3-7 / P3-8 / P3-9: governance count at line 48; wave-4 label fixes; the two one-clause
   adoptions.

*Verification note: external checks all performed this pass - NCBI PubMed metadata (8 IDs), PMC6276348
JATS full text, ClinicalTrials.gov API v2 (2 studies); every verification quoted above carries its
DOI/PMC/NCT anchor. All repo claims assessed against documents I actually read (paths in header).
No claim above rests on the authors' own verification.*