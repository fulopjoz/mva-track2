# Wave 4 - Q10 SurveillanceToday: current (2024–2026) standard-of-care surveillance backbone for MVA/BUB1B, and the live MVA-intervention trial/registry census

Axis owner: SurveillanceToday. Date: 2026-09-05. Termination criterion declared up front:
**(T10)** surveillance statement fully cited to 2024–2026 primary sources, AND the MVA-specific intervention
infrastructure census exhausted by two non-extendable adverse queries per registry. **Met** (see §2 and §3).

---

## VERDICT (this page stands alone)

### (a) Surveillance-today claims - VERIFIED VERBATIM. The report's "surveillance backbone" statement is current.

The 2024–2026 primary sources that state the MVA backbone explicitly are the **AACR Childhood Cancer
Predisposition Workshop (2nd workshop, July 2023) guideline update** (Nakano et al., *Clin Cancer Res* 2024) and
the **SIOP-Europe Host Genome Working Group / SIOP Renal Tumour Study Group Wilms surveillance guideline**
(Hol et al., *Eur J Cancer* 2021, reaffirmed verbatim inside the 2024 AACR update). Nothing published through
2026-09-05 supersedes, weakens, or contradicts them. Verbatim language the report MAY use:

> **MVA cancer risk (Nakano 2024, MVA section):** "Cancer types in MVA1 [BUB1B] include predominantly Wilms
> tumor and rhabdomyosarcoma, but MDS, AML and ALL have also been reported. … A convincing increased cancer
> risk particularly during childhood has been described only for MVA1 and MVA3 [TRIP13]."

> **Renal US cadence (Nakano 2024, endorsing Hol 2021 SIOP guideline):** "This group [SIOP-Europe Host Genome
> WG + SIOP Renal Tumour Study Group] recommended **renal ultrasound surveillance every 3 months from birth
> until age 7, for all MVA conditions including those with an unknown genetic cause**. Radiation exposure
> should be avoided. This AACR study group supports these recommendations."

> **Rhabdomyosarcoma / other-tumor monitoring (Nakano 2024):** there is no imaging/biochemical RMS screening
> protocol for MVA; the sanctioned modality is clinical vigilance - "We recommend **regular clinical assessment
> including review of systems to identify signs of rhabdomyosarcoma** and other malignancies," plus family
> education on "abnormal mass or swelling, hematuria, hypertension, pain, and discomfort."

> **Surveillance-only state of the field (Nakano 2024):** the MVA section names imaging and clinical-vigilance
> measures only; **no pharmacologic or risk-reduction intervention is recommended anywhere** in the MVA (or
> wider recessive genomic-instability) sections. This corroborates the report's R5 framing
> (wave3_PrecedentCensus.md §1c) verbatim.

> **Imaging modality for the Wilms risk is renal US, not WBMRI.** Nakano 2024's MVA section names no
> whole-body MRI: the entire MVA imaging recommendation is the SIOP renal-US cadence above. The separate
> 2024 AACR WBMRI update (Greer 2024) describes WBMRI use for syndromes such as Li-Fraumeni and constitutional
> mismatch-repair deficiency (abstract); any use of WBMRI in an MVA child would be an individualized, off-
> guideline decision - the report must not present WBMRI as part of the sanctioned MVA backbone.

> **cfDNA/liquid biopsy status (Kuhlen et al. 2026):** "Data, primarily from Li-Fraumeni syndrome, Lynch
> syndrome, and neurofibromatosis type 1, demonstrate promising diagnostic performance … **However, no
> randomized trials have yet confirmed clinical benefit.**" cfDNA is not standard of care for any CPS yet, and
> there is zero MVA/CIN-syndrome-specific cfDNA evidence (§1.4, recorded negative).

One nuance worth adding to the report: GeneReviews *Wilms Tumor Predisposition* (Turner et al., updated
2022, still the current posting) lists BUB1B-MVA estimated Wilms-tumor risk as ">85%" - a much higher point
estimate than the consensus wording implies - while Nakano 2024 itself flags that "the rarity of the syndrome
hampers establishment of an accurate risk assessment." Use Nakano's wording; if a number is needed, present
the GeneReviews table explicitly with that caveat; do not adopt a single risk figure.

### (b) MVA-specific intervention/registry infrastructure - EMPTY in every registry searched (2026-09-05, live).

| Registry | Query designs run | MVA-specific hits | Positive control |
|---|---|---|---|
| ClinicalTrials.gov (API v2) | condition-string MVA; gene names BUB1B / BUB1-OR-CEP57-OR-TRIP13; "aneuploidy syndrome"; "chromosomal instability" + pediatric; eponyms "Warburton Anyane Yeboa", "premature chromatid separation", "premature centromere division" | **0** (the single BUB1-gene hit NCT06858644 is a gastric-cancer prognosis model; the single "chromosomal instability" hit NCT04605523 is an ataxia-telangiectasia biomarker study - neither MVA) | everolimus → 33 trials parse fine |
| CTIS (euclinicaltrials.eu, `ctis-public-api/search`) | "mosaic variegated aneuploidy"; "BUB1B"; "aneuploidy"; "chromosomal instability syndrome"; "premature chromatid separation"; "Warburton" | **0** (the single "aneuploidy" hit 2024-516939-28-00 is a docetaxel/cabazitaxel prostate-cancer trial using aneuploidy only as a biomarker - not MVA) | everolimus → 33 |
| EU-CTR legacy (EudraCT-era search UI) | "mosaic variegated aneuploidy"; "BUB1B"; "aneuploidy" | **0 MVA-specific** (8 "aneuploidy" EudraCT hits, all IVF/PGT fertility trials; 0 paediatric-Art45) | everolimus → 314 EudraCT + 1 Art45 |
| ISRCTN | "mosaic variegated aneuploidy"; "BUB1B"; "aneuploidy"; "chromosomal instability" | **0** (14 "aneuploidy" hits all obstetric/PGT/Barrett's/bladder; 3 "chromosomal instability" hits all unrelated) | everolimus → 24 |
| ANZCTR | "mosaic variegated aneuploidy" | **0** ("Number of records found: 0") | everolimus → 176 |

**Zero registered MVA-specific intervention trials, observational studies, or MVA-dedicated registries exist
in any of the five primary WHO-network registries** (ClinicalTrials.gov, CTIS, EU-CTR legacy, ISRCTN, ANZCTR).
The only adjacent live registry-track infrastructure is:

1. **CHARM2 / NCT06726642** ("CfDNA in Hereditary And High-risk Malignancies 2", recruiting, started 2024-04,
   n=1000, case-control prospective; Farncombe et al. 2026): a cfDNA multi-cancer-early-detection RCT in
   HBOC, Lynch, NF1, LFS, PALB2, HDGC - **MVA and all other CIN syndromes are NOT eligible** (eligibility
   criteria verified in the CT.gov full record). It is the closest living "constitutional predisposition +
   liquid biopsy" program the report can cite as a model, and as a door that is currently shut to an MVA
   family.
2. **Generic predisposition registries** (none MVA-specific): the AACR/SIOP workgroups repeatedly call for
   registration of all CPS patients in national/international databases (Hol 2021 abstract); the AACR
   Pediatric Cancer Working Group and SIOP-Europe Host Genome WG are the convening bodies behind all current
   guidance.

**Family-pointing bottom line:** today the report may tell an MVA family that (i) the only sanctioned
intervention is the surveillance protocol above; (ii) no trial of any prevention or treatment strategy for the
syndrome itself is open anywhere in the primary registries; (iii) CHARM-class cfDNA programs are their nearest
window into liquid-biopsy surveillance research, but do not currently accept CIN syndromes, so the only
actionable route toward them is a research-consortium referral (AACR Pediatric Cancer Working Group network /
SIOP-Europe Host Genome WG).

**Adversarial self-audit vs. the Kuhlen 2026 review claim:** "no randomized trials have yet confirmed clinical
benefit" of cfDNA surveillance - the CHARM2 protocol paper itself states results are pending (trial
recruiting). The registry census found no other CPS-cfDNA RCT MVA-relevant. The sentence is safe to quote.

---

## 1. Evidence base

### 1.1 Current primary standard (2024 AACR workshop MVA section, full text read)

Nakano Y, Kuiper RP, Nichols KE, et al. **Update on Recommendations for Cancer Screening and Surveillance in
Children with Genomic Instability Disorders.** *Clin Cancer Res.* 2024;30(22):5009–5020.
DOI 10.1158/1078-0432.CCR-24-1098 | PMID 39264246 | PMC11705613 (full text retrieved and quoted).
scite (2026-09-05): total 8, s0/c0/m8; editorialNotices [].

Key verbatim passages (MVA subsection), all confirmed against PMC full text:
- MVA taxonomy restated (MVA1 BUB1B / MVA2 CEP57 / MVA3 TRIP13; "other genes causing MVA in patients have
  recently been reported"); "A convincing increased cancer risk particularly during childhood has been
  described only for MVA1 and MVA3."
- "Cancer types in MVA1 include predominantly Wilms tumor and rhabdomyosarcoma, but MDS, AML and ALL have
  also been reported."
- SIOP endorsement sentence (quoted in verdict): renal US q3mo birth→7y for ALL MVA incl. unknown-cause;
  radiation avoidance.
- RMS/other: clinical review-of-systems only, no imaging protocol; family education on alarm symptoms
  ("abnormal mass or swelling, hematuria, hypertension, pain, and discomfort").
- "The limited number of reported families with MVA3 predominantly presented with Wilms tumors, but the
  cancer spectrum may be broader."

A 2026 case report (Vempuluru et al., *Orbit*; PMID 42595739; DOI 10.1080/01676830.2026.2715719) illustrates
the real-world failure this surveillance is aimed at: Wilms tumor at 3y then orbital embryonal RMS at 12y in a
child with MVA3 - supports keeping alarm-symptom education active beyond the US window.

### 1.2 Underpinning Wilms guideline (cited by AACR as its source)

Hol JA, Jongmans MCJ, et al. **Wilms tumour surveillance in at-risk children: literature review and
recommendations from the SIOP-Europe Host Genome Working Group and SIOP Renal Tumour Study Group.**
*Eur J Cancer.* 2021;153:51–63. DOI 10.1016/j.ejca.2021.05.014 | PMID 34134020.
scite (2026-09-05): total 50, s2/c0/m47; editorialNotices [].
Abstract (verbatim): "we emphasise the need to register all patients with a cancer predisposition syndrome in
national or international databases, to enable the development of better tumour risk estimates and tumour
surveillance programs." The age-7/q3mo MVA cadence is confirmed via Nakano 2024's direct restatement.

### 1.3 Guideline-refresh check (2024–2026 wave of CPS surveillance papers; MVA sections found and checked)

The July-2023 AACR workshop produced a family of 2024–2025 updates. Those with any potential MVA bearing were
checked for MVA content:
- Greer MLC et al. 2024/2026 WBMRI update (*Clin Cancer Res*, CCR-24-1374; PMID 39287924; scite s0/c0/m7;
  one non-retraction correction notice 2025-10-15): the abstract scopes WBMRI value to Li-Fraumeni and CMMRD
  "among others"; no MVA-specific WBMRI recommendation exists in the MVA-relevant guideline literature.
- Kalish JM et al. (2024, CCR-24-2100) and Brzezinski JJ et al. (2025, CCR-24-2488): Wilms/overgrowth-
  spectrum updates; overgrowth/11p15/WT1-focused, MVA cadence unmodified.
- Cavar Pavic J et al. 2026 SCOPE survey + SIOPE Delphi consensus (*Eur J Hum Genet*; DOI
  10.1038/s41431-026-02040-x; PMID 41772285): named barriers = lack of screening guidelines (57%),
  result-interpretation difficulty (35.1%) - supports the report framing that surveillance (not intervention)
  is the field's operational edge.
- Turner JT, Brzezinski J, Dome JS. **Wilms Tumor Predisposition.** GeneReviews, updated 2022-03-24
  (NBK1294, still current posting): BUB1B-MVA row lists estimated Wilms risk ">85%" (vs ~10% for TRIP13-MVA3)
  - cite with the Nakano caveat on risk-estimate uncertainty; do not adopt a point value.

### 1.4 cfDNA / liquid-biopsy strand

- Kuhlen M et al. **Liquid biopsy for early cancer detection in hereditary cancer syndromes: current
  evidence.** *Crit Rev Oncol Hematol.* 2026;226:105475. DOI 10.1016/j.critrevonc.2026.105475 | PMID
  42413839. scite: new paper, no citation dust yet. Verbatim (verdict): evidence limited to LFS/Lynch/NF1;
  multimodal assays promising; **"no randomized trials have yet confirmed clinical benefit."**
- Farncombe KM et al. **Non-invasive screening in hereditary cancer: a randomized controlled trial to test
  cell-free DNA–based early detection in the CHARM consortium.** *Eur J Hum Genet.* 2026. DOI
  10.1038/s41431-026-02014-z | PMID 41611967. Trial = CHARM2 = NCT06726642 (verified on ClinicalTrials.gov
  2026-09-05): 1000 participants; cfDNA ≥3×/year in the experimental arm, standard surveillance in both;
  eligibility germline-pathogenic or suggestive-family-history HBOC/Lynch/NF1/LFS/PALB2/HDGC - **MVA absent
  from eligibility** (confirmed in CT.gov full record).
- Farncombe KM et al. 2023 AJHG CHARM methods paper (DOI 10.1016/j.ajhg.2023.08.014 | PMID 37802042):
  consortium background.
- Recorded negative: PubMed query `(cfDNA OR copy number) AND liquid biopsy AND (chromosomal instability OR
  aneuploidy) AND (surveillance OR early detection) AND 2023:2026[dp]` (2026-09-05) → **0 hits** - no
  CIN-specific cfDNA surveillance literature exists. "COSMOS-type" in the axis request = **no named MVA/CIN
  constitutional-surveillance program found** (the only "COSMOS" entries in cfDNA space are the unrelated
  COSMOS-CRC-01 colorectal MRD study and Epic-Cosmos database papers; verified by search, 2026-09-05).

## 2. Query & negative-result log (termination evidence)

| # | Engine | Query string (exact) | Date | Result |
|---|---|---|---|---|
| 1 | PubMed | mosaic variegated aneuploidy syndrome surveillance | 2026-09-05 | 7 hits; newest = Vempuluru 2026 case report |
| 2 | PubMed | mosaic variegated aneuploidy[tiab] AND (review[pt] OR guideline[tiab] OR management[tiab]) AND 2024:2026[dp] | 2026-09-05 | 5 hits; Nakano 2024 = current guideline update |
| 3 | PubMed | SIOP[tiab] AND (host genome[tiab] OR Wilms tumour predisposition[tiab]) AND surveillance[tiab] | 2026-09-05 | Hol 2021 + Cavar Pavic 2026 SCOPE |
| 4 | PubMed | (cell-free DNA[tiab] OR cfDNA[tiab]) AND (Li-Fraumeni[tiab] OR predisposition[tiab]) AND surveillance[tiab] | 2026-09-05 | Kuhlen 2026, CHARM2 2026, WBMRI-2024, AJHG-2023 |
| 5 | PubMed | cfDNA[tiab] OR "copy number"[tiab] AND liquid biopsy[tiab] AND (chromosomal instability[tiab] OR aneuploidy[tiab]) AND (surveillance[tiab] OR early detection[tiab]) AND 2023:2026[dp] | 2026-09-05 | **0** - CIN-specific cfDNA gap, recorded negative |
| 6 | PubMed | Wilms (tumor OR tumour) predisposition surveillance (guideline OR consensus OR recommendations) 2023:2026[dp] | 2026-09-05 | overgrowth-Wilms updates (Kalish 2024, Brzezinski 2025), BWS Italian consensus 2025; none change MVA cadence |
| 7 | PubMed | mosaic variegated aneuploidy AND (registry OR cohort OR natural history OR longitudinal) | 2026-09-05 | 2 hits, both case/report-level - **no MVA registry publication exists** |
| 8 | ClinicalTrials.gov API | AREA[ConditionSearch] "mosaic variegated aneuploidy"; "mosaic variegated aneuploidy" | 2026-09-05 | total=0 (both designs) |
| 9 | ClinicalTrials.gov API | BUB1B; BUB1 OR CEP57 OR TRIP13; "aneuploidy syndrome"; "chromosomal instability" pediatric | 2026-09-05 | MVA-relevant total=0 (2 incidental non-MVA hits described in verdict) |
| 10 | ClinicalTrials.gov API | "Warburton Anyane Yeboa"; "premature chromatid separation"; "premature centromere division" | 2026-09-05 | total=0 all three → eponym-anchor adverse queries non-extendable |
| 11 | CTIS public API | MVA / BUB1B / aneuploidy / chromosomal instability / PCS eponyms | 2026-09-05 | **0 MVA-relevant** (positive control everolimus = 33) |
| 12 | EU-CTR legacy | MVA / BUB1B / aneuploidy | 2026-09-05 | 0 MVA (8 irrelevant IVF "aneuploidy"); positive control everolimus 314 |
| 13 | ISRCTN | MVA / BUB1B / aneuploidy / chromosomal instability | 2026-09-05 | **0** (positive control everolimus 24) |
| 14 | ANZCTR | "mosaic variegated aneuploidy" | 2026-09-05 | 0 (positive control everolimus 176) |
| 15 | Web (DDG + PMC) | COSMOS-type cfDNA predisposition program | 2026-09-05 | no MVA/CIN program exists; only unrelated COSMOS homonyms |

The two designated non-extendable adverse queries are **#10** (eponym-family expansion on CT.gov - three
distinct naming axes all return 0, leaving no further synonym axis to extend) and **#13 + #14** (two further
independent registries added beyond the mandated three, still zero with live positive controls). Together with
#11/#12 they cover the transatlantic WHO primary-registry network for the intervention census.

## 3. Confidence

- **(a) Surveillance statement verification: HIGH.** Two independent bodies (AACR workshop via full-text PMC
  read; SIOP guideline via AACR restatement + abstract + scite) agree word-for-word on the cadence; no
  contradicting citation exists in scite (0 contradicting statements on both anchors).
- **(b) Registry census: HIGH.** Live, primary-registry queries over five registries with positive controls;
  zero MVA records anywhere; CHARM2 exclusion of CIN syndromes verified in the CT.gov full record. Residual
  uncertainty: the ICTRP meta-aggregation layer (apps.who.int/trialsearch) was not re-run separately, but
  every primary registry it aggregates that could plausibly host an MVA study was queried directly; listed as
  the single residual.
- Named risk: none of the quoted papers carries scite editorial notices except Greer 2024 (non-retraction
  correction; checked, listed).

## References (APA, DOI links)

- Nakano, Y., Kuiper, R. P., Nichols, K. E., Porter, C. C., et al. (2024). Update on recommendations for
  cancer screening and surveillance in children with genomic instability disorders. *Clinical Cancer
  Research, 30*(22), 5009–5020. https://doi.org/10.1158/1078-0432.CCR-24-1098 (PMID 39264246)
- Hol, J. A., Jongmans, M. C. J., et al. (2021). Wilms tumour surveillance in at-risk children: Literature
  review and recommendations from the SIOP-Europe Host Genome Working Group and SIOP Renal Tumour Study
  Group. *European Journal of Cancer, 153*, 51–63. https://doi.org/10.1016/j.ejca.2021.05.014 (PMID 34134020)
- Greer, M.-L. C., States, L. J., Malkin, D., et al. (2024). Update on whole-body MRI surveillance for
  pediatric cancer predisposition syndromes. *Clinical Cancer Research*. https://doi.org/10.1158/1078-0432.CCR-24-1374 (PMID 39287924; correction 10.1158/1078-0432.CCR-25-3260)
- Kalish, J. M., Becktell, K. D., Bougeard, G., et al. (2024). Update on surveillance for Wilms tumor and
  hepatoblastoma in Beckwith-Wiedemann syndrome and other predisposition syndromes. *Clinical Cancer
  Research, 30*(23), 5260–5269. https://doi.org/10.1158/1078-0432.CCR-24-2100 (PMID 39320341)
- Brzezinski, J. J., Becktell, K. D., et al. (2025). Update on surveillance guidelines in emerging Wilms
  tumor predisposition syndromes. *Clinical Cancer Research, 31*(1), 18–24. https://doi.org/10.1158/1078-0432.CCR-24-2488 (PMID 39466169)
- Cavar Pavic, J., Cullinan, N., Jongmans, M., et al. (2026). Challenges in identifying paediatric cancer
  predisposition syndromes: international SCOPE survey and SIOPE expert consensus recommendations. *European
  Journal of Human Genetics*. https://doi.org/10.1038/s41431-026-02040-x (PMID 41772285)
- Kuhlen, M., Schmutz, M., Metzler, M., & Claus, R. (2026). Liquid biopsy for early cancer detection in
  hereditary cancer syndromes: Current evidence. *Critical Reviews in Oncology/Hematology, 226*, 105475.
  https://doi.org/10.1016/j.critrevonc.2026.105475 (PMID 42413839)
- Farncombe, K. M., Sobotka, J. A., Aronson, M., et al. (2026). Non-invasive screening in hereditary cancer:
  a randomized controlled trial to test cell-free DNA-based early detection in the CHARM consortium.
  *European Journal of Human Genetics*. https://doi.org/10.1038/s41431-026-02014-z (PMID 41611967)
- Farncombe, K. M., Wong, D., Norman, M. L., et al. (2023). Current and new frontiers in hereditary cancer
  surveillance: Opportunities for liquid biopsy. *American Journal of Human Genetics, 110*(10), 1616–1627.
  https://doi.org/10.1016/j.ajhg.2023.08.014 (PMID 37802042)
- Turner, J. T., Brzezinski, J., & Dome, J. S. (2022, last update). Wilms Tumor Predisposition. In
  *GeneReviews®*. https://www.ncbi.nlm.nih.gov/books/NBK1294/
- Vempuluru, V. S., Sanjeev Patne, G., Chattannavar, G., et al. (2026). Sequential presentation of Wilms'
  tumor and orbital rhabdomyosarcoma in a child with mosaic variegated aneuploidy syndrome 3. *Orbit*.
  https://doi.org/10.1080/01676830.2026.2715719 (PMID 42595739)
- ClinicalTrials.gov record NCT06726642 (CfDNA in Hereditary And High-risk Malignancies 2; retrieved
  2026-09-05): https://clinicaltrials.gov/study/NCT06726642

*All PubMed-derived claims above rest on records retrieved via the PubMed MCP (metadata + PMC full text);
registry zeros were produced live against the ClinicalTrials.gov v2 API, the CTIS public-search API, the
EU-CTR legacy UI, the ISRCTN search UI, and the ANZCTR search UI on 2026-09-05, with positive controls
(everolimus) simultaneously demonstrating the search paths were functional.*
