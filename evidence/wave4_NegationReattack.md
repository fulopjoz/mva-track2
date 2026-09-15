# Wave 4 - Q11 NegationReattack: adversarial re-verification of the four most consequential recorded negatives

**Registry access obstacles (recorded negatives, query + date + method):**
- ISRCTN - `https://www.isrctn.com/search?q={senolytic|navitoclax|dasatinib quercetin|fisetin}` → 1.2 kB JS shell, no server-side results (2026-09-05); `https://www.isrctn.com/api/query/format/json?q=navitoclax` → HTTP 400 (2026-09-05). No recoverable records this wave; DDG site-search returned no ISRCTN senolytic records.
- ANZCTR - `https://www.anzctr.org.au/TrialSearch.aspx` with senolytic/navitoclax/dasatinib-quercetin/fisetin queries → HTTP 403, bot-blocked (2026-09-05).
- Google Patents - `https://patents.google.com/xhr/query?url=q%3D...` ("splice switching oligonucleotide" liver/GalNAc variants; BUB1B variants) → HTTP 503 (2026-09-05); headless-browser attempt → Google "Sorry"/challenge page (2026-09-05). **Substitute used: WIPO Patentscope result.jsf (works, HTML-scraped, 4 queries logged under (d)).** Patent evidence can at most show R&D activity, never human precedent - noted inline.
- Date of every query below: **2026-09-05** unless stated otherwise.

**Term from assignment:** each negative re-attacked through ≥3 query designs on ≥2 non-PubMed sources → met (see per-negative tables).

---

## (a) "NO human non-muscle/non-CNS systemic splice-switching precedent" (ASO rate-limiter)

### VERDICT: **OVERTURNED-IN-PART.** The literal sentence is false as written: approved human systemic (oral, body-wide) splice-switching precedent EXISTS - the small-molecule splice-modifier class (risdiplam, branaplam) with measured peripheral pharmacodynamics. The *operative* limb - oligonucleotide/ASO exon-skipping outside muscle and CNS in humans - **SURVIVED** every new design. Attack-map sentence requires re-scoping to the oligonucleotide basis; the delivery constraint itself is unchanged.

### Evidence for the overturned half (small-molecule systemic splice-switching, humans)

| Datum | What it shows | Source (verified 2026-09-05) | Grade |
|---|---|---|---|
| Risdiplam phase 1 (PMID 30302786) | Oral, "centrally AND peripherally distributed" SMN2 splicing modifier; dose-dependent SMN2 mRNA effect measured in healthy volunteers - human systemic splice-switching PD | Europe-PMC full record, DOI 10.1111/bcp.13786 | human ph1 |
| Risdiplam in EU-CTR | Roche 2016-004184-39: RO7034067 PK/PD study "IN ADULT AND PEDIATRIC PATIENTS" with SMA - splice-switcher dosed systemically in children | EU-CTR live search 2026-09-05 | human pediatric trial |
| Branaplam VIBRANT-HD (PMID 41491108) | Oral HTT mRNA splicing modulator, phase 2b RCT in HD (Novartis), 2026, Nat Med - second systemic splice modulator taken through randomized dosing | Europe-PMC, DOI 10.1038/s41591-025-04117-4; scite 1/0/0, no notices | human ph2 RCT |

### Evidence that the ASO limb SURVIVES

Every oligonucleotide systemic splice-switching program found remains muscle (DMD eteplirsen/viltolarsen/golodirsen/casimersen lineage + Dyne/Sarepta/PepGen next-gen) or CNS-intrathecal (nusinersen, zorevunersen, atipeksen) or local ocular (ultevursen - trial NCT05158296 terminated). Non-muscle organ programs (Alport COL4A5 exon skipping, WT1 FSGS) are **organoid/mouse only** in 2025–2026 literature. Atipeksen (NCT07215416, ATM c.7865C>T splice rescue, age 0–17) is explicitly **intrathecal** - CNS, not systemic.

### New query designs logged (all 2026-09-05)

| # | Design (verbatim) | Source | Result |
|---|---|---|---|
| a1 | `TITLE_ABS:(risdiplam OR branaplam OR RG7916 OR RO7034067) AND TITLE_ABS:(splicing OR "exon 7" OR "full-length SMN") AND TITLE_ABS:(blood OR peripheral OR systemic OR plasma)` | Europe-PMC | 28 hits; PMIDs 30302786, 41491108, 41579854 core |
| a2 | EU-CTR queries: `exon skipping` / `splice switching` / `antisense oligonucleotide splice` | EU-CTR | 20 "exon skipping" trials resolved by sponsor+title → all Sarepta/Dyne DMD, MET-exon-14 oncology kinase inhibitor trials (tepotinib/capmatinib - false-positive context), Wings PQ-313 (readthrough, DMD); no non-muscle ASO. "splice switching": 0 |
| a3 | Titles of all 20 EU-CTR exon-skipping trials manually classified | EU-CTR | zero non-muscle exon-skipping drugs |
| a4 | Europe-PMC: `TITLE_ABS:("exon skipping" OR "splice modulation" ...) AND TITLE_ABS:(hepatocyte OR liver OR kidney OR renal OR hematopoietic OR respiratory OR lung) AND TITLE_ABS:(patient OR trial OR phase OR human)` | Europe-PMC | 161 hits; kidney/pancreatic hits are preclinical (organoids/mouse); no human in-vivo non-muscle ASO splice correction |
| a5 | CT.gov API sweeps: `splice-switching oligonucleotide`, `splice modulating antisense`, `exon skipping`, `progerin antisense`; min-age/status/title of all hits | CT.gov v2 | 40 exon-skipping hits → DMD + MET-oncology only; sole novel program NCT07215416 (atipeksen) = intrathecal; no HGPS/progerin ASO trial registered (lonafarnib/progerinin/everolimus-lonafarnib only) |
| a6 | OpenAlex: `systemic antisense oligonucleotide splice correction liver patient trial` (n=8); `exon skipping oligonucleotide non-muscle human tissue validation` (n=8) | OpenAlex | top-ranked results are reviews + preclinical; no human non-muscle validation surfaced |
| a7 | Google Patents XHR `"splice switching oligonucleotide" GalNAc`, `TS=("splice-switching" "liver" "oligonucleotide")`, `"exon skipping" oligonucleotide hepatocyte liver delivery` | Google Patents | **blocked (503 + bot wall)** - recorded negative per method section; no liver/GalNAc splice-ASO human program surfaced elsewhere either |

### Required correction (proposed wording for the report)
Attack-map sentence *"there is NO human precedent for non-muscle/non-CNS systemic splice-switching"* → replace with: *"No oligonucleotide exon-skipping drug is approved outside skeletal muscle; no patient-level splice correction has been demonstrated in a non-muscle, non-CNS human tissue with systemically delivered ASOs. The only human systemic splice-switching precedent is the small-molecule class (risdiplam approved, body-wide distribution incl. blood-level PD; branaplam ph2b), which does not transfer to ASO delivery."* The delivery rate-limiter statement, the Roberts-2020 citation, and the dual-compartment (systemic + intrathecal) program structure are unchanged - small-molecule splice switching does not rescue ASO delivery to non-muscle organs, and no BUB1B-compatible small-molecule splice drug exists.

---

## (b) "NO evidence senolytic removal increases tumor incidence" (F6)

### VERDICT: **SURVIVED.** Three new high-yield design classes (aggressive title/abstract direction-flips, Europe-PMC **section-qualified full-text** search, OpenAlex harm-direction searches) found zero new pro-incidence data. The post-wave-3 census grows by four supportive/non-detrimental rows; the sole inversion remains Lalinde-Gutiérrez 2026 (timing-dependent, macrophage-mediated - already recorded and priced into the F6 decision rule).

### New census rows (2024–2026 window, none pro-incidence)

| Study | Model / design | Tumor direction under senescent-cell clearance | PMID/DOI |
|---|---|---|---|
| Ming 2025 *Nat Aging* | uPAR-targeting chimeric peptide boosts **immune** clearance of senescent cells in tumorigenesis model | clearance reduces tumor (supports inverse) | PMID 39623223; DOI 10.1038/s43587-024-00750-9; scite 11t/0s/0c |
| Zhou 2026 *Cancer Discov* | p21+ senescent stromal cells promote prostate cancer immune suppression - **reversed by senolytic therapy** | clearance protective | PMID 41135083; DOI 10.1158/2159-8290.CD-25-1212 |
| Hamburger 2026 *BMC Cancer* | PRISMA systematic review (PubMed+Scopus+WoS to Aug 2025) of senogenic+senolytic strategies in murine tumor models | "enhance tumor control and can improve survival" - no adverse-incidence signal in the screened corpus | PMID 41620649; DOI 10.1186/s12885-026-15650-x |
| Valdivieso 2026 *Aging Cell* | Timing-dependent p16+ clearance vs radiation-induced accelerated aging | mitigate, not promote | PMID 42649478; DOI 10.1111/acel.70693 |
| FAST-PLV preprint 2024 (Research Square) | Post-development systemic senolysis in naturally aged mice, gene-therapy suicide construct | "reduction in cancer incidence" claim for the INK-ATTAC lineage; therapy frame, no pro-incidence | PPR953813; DOI 10.21203/rs.3.rs-5575296/v1 (preprint) |

### New query designs logged (all 2026-09-05)

| # | Design (verbatim) | Source | Result |
|---|---|---|---|
| b1 | `(TITLE_ABS:"senolytic" OR TITLE_ABS:"senolysis" OR TITLE_ABS:"senescent cell clearance") AND TITLE_ABS:(increase* OR promot* OR accelerat* OR exacerbat*) AND TITLE_ABS:(tumor OR tumour OR cancer OR neoplasm* OR malignan* OR carcinogen*)` | Europe-PMC | 356 hits, top-20 screened: pro-senolytic cancer-therapy papers; no incidence-increasing study |
| b2 | `TITLE_ABS:(senolytic OR senolysis OR "p16-positive" OR "NK-ATTAC" OR "clearance of senescent") AND TITLE_ABS:("tumor incidence" OR "tumour incidence" OR "tumor latency" OR "cancer incidence" OR "tumorigenesis" OR "cancer development" OR "tumor development")` | Europe-PMC | 115 hits, top-30: wave-3 census members (Baker 2016, Haston, Kumar) + protective new rows; nothing pro-incidence |
| b3 | OpenAlex: `senolytic treatment promoted tumour growth metastasis increased` (1341), `depletion of senescent cells accelerates cancer` (15304), `senolysis adverse tumor outcomes mouse model` (559) | OpenAlex | ranked results irrelevant/reviews; no hidden adverse study surfaced by semantic ordering |
| b4 | **Section-qualified full-text**: `SEC:RESULTS:"increased tumor" AND (senolytic OR senolysis OR "senescent cell clearance" OR "senescent cell depletion")` | Europe-PMC full text | **0 hits** - full-RESULTS-section-level negative |
| b5 | Model-name sweep `("INK-ATTAC" OR "p16-3MR" OR "p16-FDR" OR "p21-ATTAC" OR "senescent cell ablation" OR "senescent cell clearance") AND (tumor OR cancer OR neoplasm) AND FIRST_PDATE:[2024-01-01 TO 2026-12-31]` | Europe-PMC | 19 hits; no new incidence-model, no pro-incidence outcome |

**No change required** to attack-map F6 decision rules; the verifier's Q1b/Q2 statements remain accurate; the census row count increases from 6 to 10 models+1 systematic review with zero pro-incidence outcomes.

---

## (c) "NO pediatric senolytic exposure anywhere"

### VERDICT: **OVERTURNED-IN-PART (the most consequential correction of this wave).** Pediatric exposure to a canonical senolytic-class drug - **navitoclax (ABT-263, BCL-xL/BCL-2 inhibitor)** - is real, published, and regulatorily posted: children **as young as 4** were dosed. The narrower limb - no child dosed for a *senolytic indication* - **SURVIVED** (all D+Q/fisetin trials are adult-minimum). The attack-map sentence *"Child-arm feasibility remains zero-evidence"* and the F6-verifier Q3 row *"(D+Q, fisetin, navitoclax - none)"* are factually wrong as written and must be corrected; the corrected record **strengthens** senolytic-class pediatric feasibility framing (drug-class pediatric safety/PK exists) without touching the senolytic-indication gap.

### The overturn evidence

| Source | Record | Pediatric exposure |
|---|---|---|
| CT.gov v2 (live 2026-09-05) | **NCT03181126** - "A Phase 1 Dose Escalation, Open-Label Study of Venetoclax in Combination with Navitoclax and Chemotherapy…R/R ALL/LBL", COMPLETED, **minimum age 4 Years**, enrollment 69 actual (AbbVie M16-106) | children dosed with venetoclax+navitoclax + chemotherapy |
| Publication (Europe-PMC, verified) | Pullarkat et al. 2021, *Cancer Discovery* 11(6) - abstract verbatim: *"evaluated in this phase I dose-escalation study (NCT03181126) in **pediatric and adult patients** … Forty-seven patients received treatment. A recommended phase II dose of 50 mg navitoclax for adults and **25 mg for patients <45 kg** with 400 mg adult-equivalent venetoclax was identified"* | published pediatric dosing/safety for navitoclax; DOI 10.1158/2159-8290.CD-20-1465; PMID 33593877; scite 212t/4s/0c, no editorial notices |
| EU-CTR (live 2026-09-05) | **2017-001541-26** = same trial (EudraCT) with posted results: explicit **"Pediatric" ITT analysis set, "Subjects aged < 18 years"**, drug arms venetoclax+navitoclax 25/50/100 mg + safety expansion; other 7 EU-CTR navitoclax trials are adult-only | confirmatory registry posting of pediatric enrollment |
| CT.gov v2 (live) | **NCT05192889 "RAVEN"** (St. Jude + AbbVie) - Phase I/II venetoclax+navitoclax in relapsed ALL, **ages 4–30**, ACTIVE_NOT_RECRUITING, 35 actual enrollment; started 2022-08 | second pediatric navitoclax program, actively dosed |
| CT.gov v2 (live) | **NCT05215405** - "Expanded Access Program of Venetoclax and Navitoclax for **Pediatric** Patients with Relapsed or Refractory ALL" (min age 4, no longer available); **NCT03592576** - Expanded Access to Navitoclax (min age 4); **NCT05740449** HEM-iSMART-A (min 1 y, withdrawn); NCT05222984 (min 16 y, AML) | pediatric named-patient/expanded-access exposure depository |

### The surviving limb

- D+Q for senolytic intent: 22 CT.gov records (query `dasatinib quercetin`), **all minimum age ≥18** (older: 40–65 for SToMP/ALSENLITE etc.; 18 for survivorship/frailty incl. NCT04733534 adult childhood-cancer survivors).
- Fisetin/quercetin senolytic-intent trials: none pediatric (NCT06113016 min age not stated but breast-cancer survivors).
- Senolytic *indication* in EU-CTR: `senolytic` / `dasatinib quercetin` / `fisetin` queries → **0 trials**.
- ISRCTN/ANZCTR: inaccessible this wave (recorded above); no contradicting records surfaced via DDG.

### Required correction (proposed wording)
Replace *"Child-arm feasibility remains zero-evidence"* with: *"No pediatric exposure to a senolytic-class agent for a senolytic indication exists; however, pediatric safety/PK data for two canonical senolytic-class drugs exist under oncology indications: dasatinib (chronic daily, pediatric CML/ALL - already cited) and **navitoclax/ABT-263** (Pullarkat 2021; children ≥4 y; RP2D 25 mg <45 kg; St. Jude RAVEN ages 4–30; two pediatric expanded-access programs). The dose-regimen, intent, and monotherapy-vs-combination contexts differ - these data de-risk drug-class pediatric chronic exposure only, and do not provide senolytic-fate evidence."* F6-verifier Q3 row update: the parenthetical "(D+Q, fisetin, navitoclax - none)" must drop navitoclax.

---

## (d) "NO BUB1B-targeted drug screen or BUBR1-abundance-raising compound screen exists"

### VERDICT: **SURVIVED.** Six designs across five non-PubMed sources, including two sources never touched by prior waves (PubChem BioAssay target-level assay census, Patentscope patent claims). All BUB1B compound work is **inhibitor-direction** (ccRCC program now peer-reviewed; Volastra preclinical) or siRNA-library hits where BUB1B is the manipulated gene. No screen whose readout or intent was raising BubR1 abundance was found. One genuinely adversarial *caution* surfaced for the abundance-raising direction itself.

### What exists (direction census)

| Item | Direction | Source | Grade |
|---|---|---|---|
| PMID 39818011, *Eur J Med Chem* 2025 - TG-101209-derivative BUB1B inhibitors for ccRCC | **inhibitor** | Europe-PMC; DOI 10.1016/j.ejmech.2025.117247; scite 0 citations | preclinical (now peer-reviewed - census upgrade vs prior waves) |
| Volastra Therapeutics BUB1B inhibitor (PatSnap/synapse listing) | **inhibitor**, preclinical | DDG search 2026-09-05 | company program |
| PubChem BioAssay: 51 AIDs target-genesymbol BUB1B | 47 siRNA/genetic library screens (BUB1B as manipulated gene); AID 1749323 "Inhibition of BUB1B…residual activity at 1 µM"; AIDs 2046584/5 ProQinase selectivity profiling; AID 1403588 "Induction of BubR1 hyperphosphorylation in HeLa" | PubChem PUG-REST, 2026-09-05 | all inhibitor/selectivity/phenotype − none abundance-raising |
| Patentscope queries BUB1B / BUBR1 / inhibitor+compound / aging+senescent | gene-signature diagnostics, mitotic-network oncology, KIF18A/CRBN degraders, senolytic (BCL/GPX4) patents merely naming BubR1 in genomic lists | Patentscope, 2026-09-05 | no abundance-raising claim |
| **Caution row**: PMID 34545188 - *"Increased BUB1B/BUBR1 expression contributes to aberrant DNA repair activity leading to resistance to DNA-damaging agents"* | abundance-raising has a **pro-resistance oncology literature** | Europe-PMC | human-tumor cell data; safety caveat for any future BUBR1-boosting program (context: tumor cells, not MVA prophylaxis) |

### New query designs logged (all 2026-09-05)

| # | Design (verbatim) | Source | Result |
|---|---|---|---|
| d1 | `TITLE_ABS:(BUB1B OR "BubR1" OR "Bub1b") AND TITLE_ABS:(screen OR screening OR "compound library" OR "drug library" OR "high-throughput")` | Europe-PMC | 110 hits; top-25 = biomarker/oncogene, in-silico inhibitor docking, 1 checkpoint-HTS paper (SOD1, not BUB1B abundance), zero abundance-raising screens |
| d2 | `TITLE_ABS:(BubR1 OR BUB1B OR Bub1b) AND TITLE_ABS:(increase* OR restore* OR rais* OR stabiliz* OR upregul*) AND TITLE_ABS:(treatment OR drug OR compound OR inhibitor OR activator OR agonist)` | Europe-PMC | 215 hits; top-25 all oncology/BUB1B-pro-cancer or inhibitor-in-silico; no abundance-raising therapeutic screen |
| d3 | OpenAlex: `BubR1 protein abundance increase small molecule` (725), `BUB1B upregulation drug screen compound` (255), `spindle checkpoint stabilizer screen BubR1 level` (67) | OpenAlex | no screen surfaced |
| d4 | Patentscope: `BUB1B` ; `BUBR1` ; `"BUB1B" AND (inhibitor OR compound)` ; `"BUBR1" AND (aging OR lifespan OR senescent)` | Patentscope | diagnostics/inhibitor/degrader claims only (rows above) |
| d5 | PubChem `assay/target/genesymbol/BUB1B/aids` then batched `/assay/aid/{51 AIDs}/summary` name+type census | PubChem BioAssay | 51/51 classified - zero abundance-raising designs |
| d6 | DDG: `patent "BUB1B" inhibitor OR activator spindle checkpoint composition`; `patent "BUBR1" OR "Bub1b" increase expression stabilizer aging progeria treatment` | DDG web index | inhibitor-direction only (Volastra, ccRCC); no abundance-raising patent |

**No change required** to the attack map beyond an optional footnote: the ccRCC BUB1B-inhibitor program is now peer-reviewed (was early pipeline), and the resistance-by-overexpression caveat (34545188) is worth one sentence if any future abundance-raising WATCH member enters.

---

## Termination criterion - declared & met

**Declared (before executing):** each negative re-attacked through ≥3 new query designs on ≥2 non-PubMed sources, every query verbatim-logged with hit counts and date; any candidate overturn verified against at least two independent records (registry + publication).

| Negative | Designs | Non-PubMed sources | Verdict |
|---|---|---|---|
| (a) splice-switching precedent | 7 (a1–a7) | Europe-PMC, EU-CTR, CT.gov, OpenAlex, (Google Patents blocked-logged) | **OVERTURNED-IN-PART** (small-molecule precedent exists; ASO limb survived) |
| (b) senolysis ↑ tumor incidence | 5 (b1–b5) | Europe-PMC (incl. SEC:RESULTS full text), OpenAlex | **SURVIVED** (census +4 rows, zero pro-incidence) |
| (c) pediatric senolytic exposure | 5 (EU-CTR navitoclax census; CT.gov 3 sweeps; EPMC publication verify; ISRCTN/ANZCTR blocked-logged; DDG) | EU-CTR, CT.gov, Europe-PMC, DDG | **OVERTURNED-IN-PART** (navitoclax pediatric exposure real & published; senolytic-indication limb survived) |
| (d) BUB1B screen | 6 (d1–d6) | Europe-PMC, OpenAlex, Patentscope, PubChem BioAssay, DDG | **SURVIVED** (all inhibitor-direction or siRNA-library) |

All four criteria met. scite tallies (2026-09-05, token `~/.config/scite/token`: Pullarkat 2021: 212t/4s/0c; risdiplam ph1: 87t/2s/0c; branaplam HD: 1t/0s/0c; Ming 2025: 11t/0s/0c; ccRCC BUB1Bi: 0; Lalinde-Gutiérrez 2026: still 0 citations. Editorial notices: none on any load-bearing ID).

### Citation-verifier pass (Link Works + Relevant Content + Fact Check)
- Pullarkat 2021 - DOI resolves (Europe-PMC); abstract verbatim verified "pediatric and adult patients" + "<45 kg→25 mg" - PASS.
- NCT03181126 / NCT05192889 / NCT05215405 / NCT03592576 / NCT05740449 - CT.gov v2 JSON fields (minAge, status, enrollment) quoted directly - PASS.
- EudraCT 2017-001541-26 - /results page Pediatric ITT set text quoted - PASS.
- Risdiplam ph1 30302786 / branaplam 41491108 abstracts verified via Europe-PMC full records - PASS.
- Ming 2025, Hamburger 2026, Valdivieso 2026, Zhou 2026 - abstracts verified for direction as quoted - PASS.
- PubChem 51-AID census - names fetched live - PASS.
- No claim retained that failed verification; ISRCTN/ANZCTR/Google-Patents inaccessibility disclosed rather than claimed-cleared.

## References (APA, DOI-linked)

Baranello, G., et al. (2021). (Context for risdiplam program; not load-bearing here.)
Hamburger, E. C. B., Brigato, P., Rosenzweig, D. H., & Haglund, L. (2026). Senogenic-senolytic treatment strategies enhance tumor control and can improve survival in murine cancer models: A systematic review. *BMC Cancer*. [doi:10.1186/s12885-026-15650-x](https://doi.org/10.1186/s12885-026-15650-x) (PMID 41620649)
Lewis, J., Garcia, H., Brown, D., et al. (2024). Systemic senolysis in naturally aged mice using a FAST-PLV gene therapy approach [Preprint]. *Research Square*. [doi:10.21203/rs.3.rs-5575296/v1](https://doi.org/10.21203/rs.3.rs-5575296/v1)
Ming, X., Yang, Z., Huang, Y., et al. (2025). A chimeric peptide promotes immune surveillance of senescent cells in injury, fibrosis, tumorigenesis and aging. *Nature Aging, 5*. [doi:10.1038/s43587-024-00750-9](https://doi.org/10.1038/s43587-024-00750-9) (PMID 39623223)
Pullarkat, V. A., Lacayo, N. J., Jabbour, E., et al. (2021). Venetoclax and navitoclax in combination with chemotherapy in patients with relapsed or refractory acute lymphoblastic leukemia and lymphoblastic lymphoma. *Cancer Discovery, 11*(6), 1440–1453. [doi:10.1158/2159-8290.CD-20-1465](https://doi.org/10.1158/2159-8290.CD-20-1465) (PMID 33593877)
Valdivieso, K., Weigand, M., Costa, D. G., et al. (2026). Timing-dependent clearance of p16-positive cells mitigates radiation-induced accelerated aging. *Aging Cell*. [doi:10.1111/acel.70693](https://doi.org/10.1111/acel.70693) (PMID 42649478)
Zhou, L., DeMarco, K. D., Murphy, K. C., et al. (2026). p21-positive senescent stromal cells promote prostate cancer immune suppression and progression that can be reversed by senolytic therapy. *Cancer Discovery*. [doi:10.1158/2159-8290.CD-25-1212](https://doi.org/10.1158/2159-8290.CD-25-1212) (PMID 41135083)
Lalinde-Gutiérrez, M., et al. (2026). Immunosuppressive macrophages determine the effect of cellular senescence on tumor progression. *Science Advances, 12*(1), eadx2988. [doi:10.1126/sciadv.adx2988](https://doi.org/10.1126/sciadv.adx2988) (PMID 41477861)
[Branaplam VIBRANT-HD] (2026). Oral splicing modulator branaplam in Huntington's disease: A phase 2 randomized controlled trial. *Nature Medicine*. [doi:10.1038/s41591-025-04117-4](https://doi.org/10.1038/s41591-025-04117-4) (PMID 41491108)
[Risdiplam phase 1] (2019). A phase 1 healthy male volunteer single escalating dose study of the pharmacokinetics and pharmacodynamics of risdiplam (RG7916, RO7034067), a SMN2 splicing modifier. *British Journal of Clinical Pharmacology, 85*. [doi:10.1111/bcp.13786](https://doi.org/10.1111/bcp.13786) (PMID 30302786)
[TG-101209-derivative BUB1B inhibitors] (2025). Synthesis and biological assessment of BUB1B inhibitors for the treatment of clear cell renal cell carcinoma. *European Journal of Medicinal Chemistry, 285*. [doi:10.1016/j.ejmech.2025.117247](https://doi.org/10.1016/j.ejmech.2025.117247) (PMID 39818011)
[BUB1B/DNA-repair resistance] (2021). Increased BUB1B/BUBR1 expression contributes to aberrant DNA repair activity leading to resistance to DNA-damaging agents. [PMID 34545188]
ClinicalTrials.gov records (API v2, 2026-09-05): NCT03181126, NCT05192889, NCT05215405, NCT03592576, NCT05740449, NCT07215416, NCT04063124, NCT04733534. https://clinicaltrials.gov
EU Clinical Trials Register (2026-09-05): EudraCT 2017-001541-26 (results-posted), 2007-002143-25, 2009-012152-24, 2012-000606-29, 2015-000193-35, 2017-001398-17, 2020-000097-15, 2020-000557-27 (all navitoclax; adult-only except 2017-001541-26), 2016-004184-39 (RO7034067/risdiplam, adult+pediatric). https://www.clinicaltrialsregister.eu
PubChem BioAssay records (2026-09-05): 51 AIDs under gene target BUB1B, incl. 1749323 (BUB1B inhibition), 2046584/2046585 (ProQinase selectivity), 1403588 (BubR1 hyperphosphorylation induction). https://pubchem.ncbi.nlm.nih.gov
