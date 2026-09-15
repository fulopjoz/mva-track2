# REMOTE_FRESHNESS_2026-09-09 - Freshness + solvability sweep for Track-2 report limitations

**Scope:** documented limitations of the MVA Hackathon 2026 Track-2 repurposing report (`TRACK2_REPORT.md` and its lay companion in this repository), whose prior external verification is dated **2026-09-05** (wave-4 sweep, `evidence/wave4_SurveillanceToday.md`).
**Sweep date:** 2026-09-09. **Method:** live registry APIs (ClinicalTrials.gov API v2, DailyMed API v2, EMA pages) + PubMed (MCP) with ≥3 query strategies per item; repo-side grep to establish what the report already claims/cites. Verdict per item: **NO-CHANGE** or **CHANGED**. "Nothing changed" is reported explicitly - it is a valid result.

---

## 1. Everolimus regulatory status & TSC pediatric labeling - **NO-CHANGE** (both halves)

**(a) Regulatory status.**
- **FDA:** the current Novartis Afinitor / Afinitor Disperz label is SPL **version 67, published 2026-06-11**, and remains the current version as of the DailyMed database date 2026-09-08 (DailyMed API, `dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?drug_name=afinitor`, setid 2150f73a-179b-4afc-b8ce-67c85cc72f04). No label revision has occurred since the report's 2026-09-05 verification (which already post-dates the June revision). Generic ANDAs (e.g., Amneal everolimus for oral suspension, approved Jan 2025; Novugen everolimus tablets, DailyMed 2026-03-31) add competition but do not alter the reference-label content the report cites.
- **EMA:** Votubia remains **Authorised** (full marketing authorisation since 2015-11-16); EPAR product information last updated **2025-11-20**; page last modified 2025-11-20 (https://www.ema.europa.eu/en/medicines/human/EPAR/votubia). TSC indications unchanged: SEGA (adults and children, unsuitable for surgery), renal angiomyolipoma (adults), add-on partial-onset seizures from **2 years of age**.
- **Implication (one line):** the report's §4.4 everolimus framing (pediatric-chronic-feasibility node, EXIST-1/3, label §8.4 citations) needs no regulatory edit; the "gated everolimus" recommendation stands on unchanged regulatory ground.

**(b) Pediatric rapalog NK/CD8 immune-quantification.** Four independent PubMed strategies (2024–2026; rapalog × NK/lymphocyte-subset × pediatric; TSC/KHE/vascular-anomaly cohorts; broad CD8/NK/lymphopenia sweep) return **no study quantifying NK- or CD8-cell effects of everolimus or sirolimus in children**. Adjacent-but-not-qualifying 2024–2026 data: vaccine-immunogenicity cohorts (Yuan et al. 2025, PMID 41012109, and 2026, PMID 42154819 - already the report's E29; Lin et al. 2025, TSC children on sirolimus, COVID-19 vaccine neutralizing-antibody titers, [DOI 10.1080/21645515.2025.2535120](https://doi.org/10.1080/21645515.2025.2535120), PMID 40830965 - humoral only, no NK/CD8 phenotyping). Adult-only NK quantification (Besson 2021) remains the class evidence.
- **Implication (one line):** the report's "mTOR-immunosuppression monitoring is hypothesis-level in children; NK-under-rapalog unquantified in pediatrics" limitation statement remains literally true - no edit needed; Lin 2025 may optionally be added as a second pediatric-humoral corroboration, clearly labeled as not closing the NK gap.

---

## 2. RAVEN (NCT05192889, pediatric navitoclax/venetoclax) - **NO-CHANGE** in registry status since 2026-09-05; **newly surfaced vs. the report's text: posted summary results**

- **Registry status (live, ClinicalTrials.gov API v2, checked 2026-09-09):** **ACTIVE_NOT_RECRUITING** (status verified 2025-09; last update posted 2025-09-22). Enrollment 35 (ACTUAL). Primary completion **2024-06-13 (ACTUAL)**; study completion estimated 2027-02. Sponsor St. Jude; collaborator AbbVie. https://clinicaltrials.gov/study/NCT05192889
- **Results:** a **summary-results section was posted 2025-09-22** (results first submitted 2025-06-13; QC 2025-09-18). Posted primary outcomes include: end-of-Block-1 MRD-negative response (MRD <0.01% by flow) in **19/30** evaluable patients on venetoclax+navitoclax reinduction; RP2D of venetoclax 240 mg/m²/day for 21 days with blinatumomab (Block 2b), and cytarabine 3000 mg/m²/dose with navitoclax (Block 2a) - navitoclax dosed 25 mg (20–<45 kg) / 50 mg (≥45 kg), matching the Pullarkat 2021 RP2D the report already cites.
- **Peer-reviewed publication:** none found in PubMed (queries "RAVEN/St. Jude + venetoclax + navitoclax + relapsed/refractory + children", 2025-06→present; "navitoclax venetoclax childhood ALL" - most recent hit is Jan 2025 and unrelated). 
- **Verdict nuance:** the registry record has not changed since the report's 2026-09-05 verification (last update 2025-09-22 predates it), so strictly this is NO-CHANGE **since 2026-09-05**; however the report's E16 text ("RAVEN NCT05192889 (ages 4-30, **actively dosed**)") does not reflect the posted results and describes the status loosely.
- **Implication (one line):** upgrade E16's wording to "active, not recruiting (accrual closed 2024; follow-up/analysis ongoing)" and cite the posted CT.gov results (19/30 MRD-negative; RP2D identified) - this quantitatively strengthens the report's own pediatric-navitoclax feasibility correction without changing any disposition.

---

## 3. CHARM2 (NCT06726642, cfDNA surveillance RCT, n=1000) - **NO-CHANGE**

- **Registry status (live, checked 2026-09-09):** **RECRUITING** (status verified 2025-12; last update posted 2025-12-16); primary completion estimated 2029-12, study completion 2031-12. **No results posted** (as expected for an ongoing RCT). https://clinicaltrials.gov/study/NCT06726642
- **Eligibility:** inclusion still restricted to **HBOC, Lynch syndrome, NF1, Li-Fraumeni syndrome, PALB2, HDGC**; MVA and all chromosome-instability syndromes remain absent from eligibility (verified in the live CT.gov record, matching the report's E47).
- **Publications:** the CHARM2 protocol paper (Farncombe et al. 2026, *Eur J Hum Genet* 34(9):1243–1253, [DOI 10.1038/s41431-026-02014-z](https://doi.org/10.1038/s41431-026-02014-z), PMID 41611967) is the only CHARM2-relevant 2026 output and is **already cited in the report's wave-4 evidence pack**. No results publication exists (trial mid-course).
- **Implication (one line):** the report's cfDNA-not-SoC limitation statement ("the closest registered constitutional-predisposition cfDNA RCT excludes MVA/CIN") remains accurate and current - no edit needed.

---

## 4. BUB1B/MVA surveillance or treatment guideline updates (2026) - **NO-CHANGE**

- **Surveillance guidelines:** no SIOP-Europe Wilms, AACR-predisposition, or GeneReviews-class update postdating the report's sources. The most recent guideline-tier document remains the SIOPE Delphi consensus / SCOPE survey (Cavar Pavic et al. 2026, [DOI 10.1038/s41431-026-02040-x](https://doi.org/10.1038/s41431-026-02040-x), PMID 41772285), which the report's wave-4 pack already cites. PubMed sweeps ("mosaic variegated aneuploidy" since 2025-09; Wilms predisposition surveillance 2026) return only case reports and cohort genetics papers.
- **What 2026 did add (below guideline tier, for completeness):**
  - Vempuluru et al. 2026, *Orbit* (MVA3/TRIP13 child with Wilms tumor then orbital rhabdomyosarcoma; [DOI 10.1080/01676830.2026.2715719](https://doi.org/10.1080/01676830.2026.2715719), PMID 42595739) - case report; reinforces the Wilms+RMS spectrum the report already quotes.
  - González-Blanco et al. 2026, *Nat Commun* 17 (Drosophila MVA/microcephaly model: proteostasis failure + mitochondrial dysfunction from complex aneuploidies; [DOI 10.1038/s41467-026-70521-0](https://doi.org/10.1038/s41467-026-70521-0), PMID 41820377) - **mechanistic corroboration of the report's proteotoxic-stress axis in an MVA-relevant model**, but not a treatment or surveillance change.
  - Welter et al. 2026, *Pediatr Blood Cancer* (SIOP/GPOH nephroblastomatosis management; [DOI 10.1002/1545-5017.70354](https://doi.org/10.1002/1545-5017.70354), PMID 42053023) - precursor-lesion strategy in a 65%-CPS cohort; does not alter the renal-US q3mo birth→7y cadence for MVA.
- **Implication (one line):** the surveillance backbone (renal US q3mo birth→7y, no WBMRI, cfDNA not SoC, zero registered MVA intervention trials) stands verbatim; optionally add González-Blanco 2026 as genotype-adjacent mechanistic support for the proteostasis framing.

---

## 5. Gomisin A / aneuploidy rescue - **NO-CHANGE; premise itself unsupported (no evidence located)**

- **PubMed (2026-09-09):** zero papers match gomisin × (aneuploidy OR chromosome segregation OR spindle checkpoint OR BubR1/BUB1B). The ~300 gomisin-indexed papers are hepatoprotective/anti-inflammatory/cell-cycle-arrest studies (e.g., G1 arrest in U937 leukemia cells), none rescuing aneuploidy in mice.
- **Web search:** no 2012–2013 (or any) mouse report of gomisin A rescuing aneuploidy located (DuckDuckGo + multi-provider web search; "gomisin" "aneuploidy" returns no matches).
- **Repo:** the report and its 19-memo evidence pack contain **no mention of gomisin** (grep across this repository = 0 hits), so there is no report limitation statement keyed to it. The report's actual mouse-rescue evidence lines are BubR1-overexpression/NMN (North 2014) and Tang-2011-mTOR-neutrality - none involve gomisin.
- **What would settle it:** the citation the task author had in mind (possible compound-name confusion - e.g., with an AMPK-agent or an HSP90-inhibitor class study). Until a real citation exists, no claim should be added to the report; fabricating a gomisin line would violate the report's own no-fabricated-citations rule.
- **Implication (one line):** nothing to update - the report neither claims nor needs gomisin, and no literature exists to strengthen any mouse-rescue story on its basis.

---

## 6. Direct evidence that rapalogs selectively kill/bias against high-aneuploidy cells (2019–2026) - **NO-CHANGE (mechanism fit remains low-grade)**

- **Core finding:** no 2019–2026 study demonstrates aneuploidy-graded selective killing by rapalogs - i.e., nothing analogous to Tang 2011's AICAR/17-AAG selectivity exists for mTOR inhibitors, so the report's Tang-2011-neutrality datum (P2-1 correction: rapamycin/torin1 neutral on trisomic MEFs, never tested on Bub1b^H/H) stands unrebutted. The entire PubMed literature at the aneuploidy × mTOR-inhibitor intersection since 2019 is small (≈16 papers) and contains:
  - **Chui et al. 2019**, *Cancer Res* 79(21):5536 ([DOI 10.1158/0008-5472.CAN-18-3029](https://doi.org/10.1158/0008-5472.CAN-18-3029), PMID 31530568): chromosome missegregation → proteotoxic stress; **mTORC1 suppression (lowered protein synthesis) is a protective adaptation** in CIN ovarian-cancer spheroids - direction = rescue, not kill; consistent with the report's framing.
  - **Bowers et al. 2022**, *BMC Cancer* 22:410 ([DOI 10.1186/s12885-022-09503-6](https://doi.org/10.1186/s12885-022-09503-6), PMID 35421971): rapamycin inhibited colony outgrowth from polyploid giant cancer cells (52–84%, two ovarian lines) - the only rapalog-"kills"-hyperploid datum located, but ex vivo, colony-formation-stage, and not aneuploid-fraction-graded.
  - **Sieben et al. 2020**, *J Clin Invest* 130(1):171 ([DOI 10.1172/JCI126863](https://doi.org/10.1172/JCI126863), PMID 31738183): in BubR1-mutant (MVA-model) mice, **mTORC1 hyperactivity correlates with sarcopenia** in heterozygous carriers - supports the rescue/stress-relief direction in the report's exact genotype class.
  - **Maués et al. 2025**, *J Cell Mol Med* 29:e70941 ([DOI 10.1111/jcmm.70941](https://doi.org/10.1111/jcmm.70941), PMID 41310823): isolated-trisomy AML - the trisomy-21 subgroup showed ex-vivo sensitivity to PLK/mTOR inhibitors; subgroup-correlative, not aneuploidy-graded rapalog selectivity.
  - **Lim et al. 2024**, *Oncol Rep* 52 ([DOI 10.3892/or.2024.8760](https://doi.org/10.3892/or.2024.8760), PMID 38904203): Mps1-inhibitor + **AICAR** synergy (AMPK chemistry - the class the item excludes).
- **Implication (one line):** the report's "low-grade mechanism fit / no direction claimed" limitation statement survives this sweep intact; if anything, the newest data (Chui 2019, Sieben 2020) reinforce the rescue-direction caution, and Bowers 2022 is the only citable kill-direction footnote - with heavy caveats.

---

## Summary table

| # | Item | Verdict | Action for report |
|---|------|---------|-------------------|
| 1 | Everolimus FDA/EMA status + pediatric labeling; pediatric NK/CD8 quantification | **NO-CHANGE** | none (optional: add Lin 2025 as pediatric-humeral corroboration, labeled non-NK) |
| 2 | RAVEN NCT05192889 | **NO-CHANGE since 2026-09-05** (but report under-cites posted results) | update E16 wording + cite CT.gov posted results (19/30 MRD-neg, RP2D) |
| 3 | CHARM2 NCT06726642 | **NO-CHANGE** | none |
| 4 | 2026 MVA surveillance/treatment guidelines | **NO-CHANGE** | none (optional: González-Blanco 2026 mechanistic footnote) |
| 5 | Gomisin A aneuploidy rescue | **NO-CHANGE - premise unsupported; no evidence located** | none (do not add gomisin; no citation exists) |
| 6 | Direct rapalog-aneuploidy kill evidence 2019–2026 | **NO-CHANGE** | none (optional kill-direction footnote: Bowers 2022) |

## Provenance

- ClinicalTrials.gov API v2 records for NCT05192889 and NCT06726642, fetched live 2026-09-09 (raw JSON retained in session artifacts 2158/2157).
- DailyMed API v2 (`spls.json?drug_name=afinitor`), database date 2026-09-08.
- EMA Votubia EPAR page (https://www.ema.europa.eu/en/medicines/human/EPAR/votubia), fetched 2026-09-09; EN product information last updated 2025-11-20.
- PubMed via MCP, 2026-09-09, query strategies logged above (≈12 distinct queries).
- Repository greps (2026-09-09) establishing the report's existing claims/citations per item.

## References (everything cited in this dossier)

1. ClinicalTrials.gov. (2025). *RAVEN: A Phase I/II Trial Treating Relapsed Acute Lymphoblastic Leukemia With Venetoclax and Navitoclax* (NCT05192889). https://clinicaltrials.gov/study/NCT05192889
2. ClinicalTrials.gov. (2025). *CHARM2: CfDNA in Hereditary And High-risk Malignancies 2* (NCT06726642). https://clinicaltrials.gov/study/NCT06726642
3. DailyMed. (2026). *AFINITOR / AFINITOR DISPERZ (everolimus), Novartis* - SPL setid 2150f73a-179b-4afc-b8ce-67c85cc72f04, version 67 (2026-06-11). https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2150f73a-179b-4afc-b8ce-67c85cc72f04
4. European Medicines Agency. (2025). *Votubia (everolimus) - EPAR medicine overview*. https://www.ema.europa.eu/en/medicines/human/EPAR/votubia
5. Farncombe, K. M., Sobotka, J. A., Aronson, M., et al. (2026). Non-invasive screening in hereditary cancer: a randomized controlled trial to test cell-free DNA-based early detection in the CHARM consortium. *European Journal of Human Genetics, 34*(9), 1243–1253. https://doi.org/10.1038/s41431-026-02014-z (PMID 41611967)
6. Yuan, J., Yuan, Z., Ding, Y., et al. (2025). Safety and immunogenicity of vaccines in children with kaposiform hemangioendothelioma receiving sirolimus. *Vaccines, 13*(9), 903. https://doi.org/10.3390/vaccines13090903 (PMID 41012109)
7. Yuan, J., Ding, Y., Wang, Z., Su, L., & Li, K. (2026). Antibody levels and immune memory in children with kaposiform hemangioendothelioma treated with sirolimus after catch-up vaccination. *Human Vaccines & Immunotherapeutics, 22*(1), 2653585. https://doi.org/10.1080/21645515.2026.2653585 (PMID 42154819)
8. Lin, S., Zhao, X., Li, L., et al. (2025). Prospective study of safety, immunogenicity, and efficacy of inactivated COVID-19 vaccine in tuberous sclerosis complex children on sirolimus. *Human Vaccines & Immunotherapeutics, 21*(1), 2535120. https://doi.org/10.1080/21645515.2025.2535120 (PMID 40830965)
9. Chui, M. H., Doodnauth, S. A., Erdmann, N., et al. (2019). Chromosomal instability and mTORC1 activation through PTEN loss contribute to proteotoxic stress in ovarian carcinoma. *Cancer Research, 79*(21), 5536–5549. https://doi.org/10.1158/0008-5472.CAN-18-3029 (PMID 31530568)
10. Bowers, R. R., Andrade, M. F., Jones, C. M., et al. (2022). Autophagy modulating therapeutics inhibit ovarian cancer colony generation by polyploid giant cancer cells (PGCCs). *BMC Cancer, 22*, 410. https://doi.org/10.1186/s12885-022-09503-6 (PMID 35421971)
11. Sieben, C. J., Jeganathan, K. B., Nelson, G. G., et al. (2020). BubR1 allelic effects drive phenotypic heterogeneity in mosaic-variegated aneuploidy progeria syndrome. *Journal of Clinical Investigation, 130*(1), 171–188. https://doi.org/10.1172/JCI126863 (PMID 31738183)
12. Maués, J. H. da S., Duarte, B. K. L., Svidnicki, M. C. C. M., et al. (2025). Integrated genomic and transcriptomic profiling of isolated trisomies in AML reveals cell cycle dysregulation and therapeutic vulnerabilities. *Journal of Cellular and Molecular Medicine, 29*(22), e70941. https://doi.org/10.1111/jcmm.70941 (PMID 41310823)
13. Lim, J. S., Kim, E., Song, J.-S., & Ahn, S. (2024). Energy-stress-mediated activation of AMPK sensitizes MPS1 kinase inhibition in triple-negative breast cancer. *Oncology Reports, 52*(2). https://doi.org/10.3892/or.2024.8760 (PMID 38904203)
14. González-Blanco, A., Acuña-Higaki, A., Boettger, D., Joy, J., & Milán, M. (2026). Proteostasis failure and mitochondrial dysfunction contribute to chromosomal instability-induced microcephaly. *Nature Communications, 17*. https://doi.org/10.1038/s41467-026-70521-0 (PMID 41820377)
15. Welter, N., Schenk, J.-P., Wegert, J., et al. (2026). The fate (outcome) of clinically apparent single lesion and oligofocal nephroblastomatosis treated according to SIOP/GPOH protocols for Wilms tumor. *Pediatric Blood & Cancer, 73*(7), e70354. https://doi.org/10.1002/1545-5017.70354 (PMID 42053023)
16. Vempuluru, V. S., Sanjeev Patne, G., Chattannavar, G., Mishra, D. K., & Kaliki, S. (2026). Sequential presentation of Wilms' tumor and orbital rhabdomyosarcoma in a child with mosaic variegated aneuploidy syndrome 3. *Orbit*. https://doi.org/10.1080/01676830.2026.2715719 (PMID 42595739)
17. Cavar Pavic, J., et al. (2026). Cancer surveillance in hereditary cancer predisposition syndromes: international SCOPE survey and SIOPE expert consensus recommendations. *European Journal of Human Genetics*. https://doi.org/10.1038/s41431-026-02040-x (PMID 41772285) [already cited by the report; listed for completeness]
18. Tang, Y.-C., Williams, B. R., Siegel, J. J., & Amon, A. (2011). Identification of aneuploidy-selective antiproliferation compounds. *Cell, 144*(4), 499–512. https://doi.org/10.1016/j.cell.2011.01.017 (PMID 21315436) [baseline datum referenced; already cited by the report as E58]

*All PubMed-attributed items retrieved via the PubMed MCP service on 2026-09-09; registry and label records retrieved via their public APIs/pages on 2026-09-09.*
