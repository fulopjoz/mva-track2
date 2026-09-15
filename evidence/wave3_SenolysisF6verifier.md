# Wave 3 - F6 Verifier: did the Adversarial Reviewer's "senescence of aneuploid cells is a tumor-suppressive barrier; chronic senolysis may remove it" objection survive evidence?

**Basis:** PubMed (EUtilities, all identifiers re-verified 2026-09-05); scite.ai tallies via `~/.config/scite/token` (working token, tallies fetched 2026-09-05)
**Grades:** A = human RCT · B = human clinical/observational · C = human cells or independent-lab animal · D = mouse-only / single-lab · unmeasured conjuncts flagged explicitly.

---

## What F6 claimed and what it asked for

F6 (MAJOR): *"In a constitutional-CIN child, chronically ablating p16+ cells (or senomorphic suppression of senescence entry) removes [the anti-tumor] brake; the Baker 2008 p16-inactivation arm attenuated progeroid phenotypes but never tested tumor endpoints in the cross."* Falsification test proposed by the reviewer: add to Gate 0 and the n-of-1 decision rule (i) an explicit argument why burden-reduction dominates barrier-removal at measured burden levels, (ii) intensified tumor surveillance as a hard component of any senolytic/senomorphic arm, (iii) pre-specified stopping on any malignancy signal.

This document answers four pre-specified questions with graded evidence, then delivers a VERDICT (keep / modify / tighten gate-first) and the explicit decision-rule change.

---

## Q1 - Is senescence of aneuploid/CIN cells demonstrably tumor-SUPPRESSIVE in vivo? And has senolytic removal EVER been shown to increase tumor incidence?

**Answer: the first half (senescent arrest of damaged/polyploid cells is a tumor barrier in vivo) is confirmed at strong animal evidence plus human-tissue concordance. The second, load-bearing half - has senolytic *removal* of senescent cells ever increased tumor incidence, any model, any drug - returns NO EVIDENCE LOCATED. The one genuine inverted-direction datum (Lalinde-Gutiérrez 2026) is macrophage-mediated and stage-dependent, not arrest-mediated.**

### 1a. Senescence-as-barrier evidence chain (supports F6's *premise*)

| Evidence | What it shows | Species / grade | PMID |
|---|---|---|---|
| Braig 2005 *Nature* | Oncogene-induced senescence (Nras^G12V) is an in-vivo barrier to lymphoma progression | mouse, **D** | 16079837 |
| Michaloglou 2005 *Nature* | BRAF^E600 benign nevi (human) are senescent; senescence is the early barrier | human tissue, **B** | 16079850 |
| Kang 2011 *Nature* | CD4+ T-cell-mediated clearance of Nras-induced senescent hepatocytes limits liver cancer in vivo | mouse + human validation, **C** | 22080947 |
| Xue 2007 *Nature* | p53 restoration in liver carcinomas triggers senescence → innate-immune-mediated tumor clearance | mouse, **D** | 17251933 |
| Weaver 2013 *PNAS* | Mis-segregation rate determines whether aneuploidy suppresses (high CIN) or promotes tumors | mouse (CenpE^+/-), **D** | 24133140 |
| Weaver 2016 *MBoC* | High mis-segregation rates **suppress tumor progression but not initiation** - the CIN "barrier" operates at progression | mouse (CenpE), **D** | 27146113 |
| Santaguida 2017 *Dev Cell* + Wang 2021 *EMBO Rep* (already in axis doc) | Mis-segregating cells arrest senescent with pro-inflammatory SASP and are eliminated by NK cells | human cells + in-vivo transfer, **C** | 28633018; 34105235 |

Interpretation: the *arrest* is the protective state; removing arrested cells is the barrier-removal scenario F6 fears. These papers show that *losing* the arrest machine (gene ablation, checkpoint failure) is pro-tumorigenic - but none tests what happens when senescent cells are *cleared* rather than genetically prevented from arresting.

### 1b. Direct evidence that senolytic clearance INCREASED tumor incidence (any model, any drug) - **no evidence located**

Queries recorded (PubMed, 2026-09-05): `senolysis increased tumorigenesis`; `senolytic tumor incidence mouse`; `p16 ablation clearance tumor increased` / `INK-ATTAC tumor increased`; "depletion senescent (promoted OR increased OR drove) tumor". No study shows pharmacologic or INK-ATTAC/SuSe cell-clearance increasing **de-novo tumor incidence**. Nearest inversions in the direction F6 fears:

| Context | Finding | Direction vs F6 |
|---|---|---|
| **Lalinde-Gutiérrez 2026** *Sci Adv* (SuSe × MMTV-PyMT breast) | **Early** senolysis **accelerated** tumor growth/metastasis; **late** senolysis **decelerated**. Mechanism: depletion expands CCL2-dependent **immunosuppressive protumorigenic macrophages** - not release of an arrested preneoplastic clone | **Partially supports F6's caution** (timing matters), but mechanism is immune-context, not barrier-release; and the same model shows protective late senolysis. Grade D, mouse. |
| **Baker 2016** *Nature* (INK-ATTAC, natural aging) | "AP treatment had **no impact on the incidence or spectrum** of macroscopically detectable tumors at autopsy, **although tumor latency was increased**" (PMC4845101 main text); lifespan extension persisted in tumor-free deaths | **Direct negative** - twice-weekly p16+ clearance from 12 months did not remove any barrier. Grade D. |
| **Baker 2008** *Nat Cell Biol* (BubR1^H/H × p16^Ink4a−/− / p19^Arf−/−) | **No tumor endpoint tested in the cross** (aging phenotypes only; sole tumor mention is the intro noting p16/p19-null mice die of tumors) | F6's factual claim confirmed verbatim. Grade D. |

**Assessment (Q1):** F6's premise (senescent aneuploid cells are a brake) is evidence-supported; its inference (therefore removing them increases tumors) is not. The untested conjunct for the proband is narrow and real: *does clearing p16+ cells in a non-tumor-bearing, high-CIN-child background strip a checkpoint that the Baker/Weaver lineage shows protects against progression?* **Graded as unmeasured risk, not as demonstrated hazard** - it must be handled structurally inside the gate (see VERDICT), not by demoting the axis.

## Q2 - Inverse: senolysis DECREASING tumor incidence in CIN/progeroid models beyond Baker 2011 - full census

**Answer: beyond Baker 2011 (which never measured tumors), five studies measure tumor outcomes under senolysis in chromosomally-dangerous, progeroid, or tumor-prone models. Zero show an increase; four show decrease or no-change. This is the full PubMed census as of 2026-09-05.**

| Study | Model | Senolytic modality | Tumor outcome under senolysis | Species / grade | PMID |
|---|---|---|---|---|---|
| **Baker 2016** *Nature* | INK-ATTAC WT natural aging (two backgrounds) | AP20187 p16+ clearance ×2/wk from 12 mo | **No change in tumor incidence/spectrum; latency increased** | mouse, **D** | 26840489 |
| **Ovadya 2018** *Nat Commun* | LMNA^+/G609G progeroid (± Prf1−/− impaired cytotoxic clearance) | ABT-737 (Bcl-2i) pulses in second half of life | Median survival **increased**; no tumor signal reported (progeria model) | mouse, **D** | 30575733 |
| **Haston 2023** *Cancer Cell* | KRAS^G12D-driven lung; senescent alveolar macrophages are the dominant SnC (p16-FDR reporter line) | genetic (p16-FDR) or senolytic ablation of senescent cells / macrophage depletion | **Tumor burden decreased, survival increased** | mouse, **D** | 37267953 |
| **Kumar 2025** *Aging* | Apc(1638N/+) + γ / ^28Si irradiation | ABT-263 (navitoclax) 5 d/wk | **Radiation-induced GI adenoma/carcinoma development mitigated** | mouse, **D** | 39792466 |
| **Gallanis 2023** *Cancers* | p16-INK-ATTAC, palbociclib-induced stromal senescence + syngeneic mammary cells | AP-depletion of host p16+ stromal cells | **Metastatic lung seeding decreased** (reversed palbociclib effect) | mouse, **D** | 36980794 |
| **Lalinde-Gutiérrez 2026** *Sci Adv* (the F6-side counterweight) | SuSe × MMTV-PyMT | SuSe p16+/IL-6+ depletion, early vs late | **Early: accelerated**; late: decelerated (macrophage-dependent) | mouse, **D** | 41477861 |

Adjacent but out-of-scope (therapy-induced senescence in established cancer, not incidence prevention): Demaria 2017 (senolysis depresses relapse/toxicity, PMID 27979832); Ruscetti 2019 *Science* (NK-mediated clearance of senescent tumor cells controls tumor, PMID 30573629); Milanovic 2018 (therapy-induced senescence can reprogram to stemness - see point 5 of the decision rule).

**Assessment (Q2):** the empirical record is uniform: senolytic clearance does not increase tumor incidence in any model tested; where direction is modified it is decreased (Haston, Kumar, Gallanis, Baker-latency) or timing-dependent (Lalinde). **F6 has no empirical incidence data on its side.** What remains is the mechanism-level hedge (arrest-release reprogramming, Milanovic 2018) - real but therapy-context-proven only, and explicitly incorporated into the decision rule below.

## Q3 - Pulsed/intermittent or senomorphic designs claiming to preserve surveillance - human or strong-animal support?

**Answer: yes for the dosing-pattern layer. Intermittent senolytic pulsing is the default human-administration pattern precisely because it leaves wide off-drug windows (largest published human experience: Justice 2019); the mTORi senomorphic class has an RCT-grade human signal showing immune ENHANCEMENT at low dose (Mannick 2018). Neither directly measures "preserved NK clearance of aneuploid cells"; that linkage is mechanistic (Q4), not clinical. No pediatric human support exists for any intermittent senolytic.**

| Design | Evidence pattern | Species / grade | PMID |
|---|---|---|---|
| **Justice 2019** D+Q IPF pilot | 14 adults; D 100 mg + Q 1250 mg, 3 d/wk × 3 wk (intermittent); feasible, mild events | human, **B** | 30616998 |
| **Xu 2018** *Nat Med* | Intermittent oral D+Q in naturally aged + senescent-transplant mice: improved function, increased lifespan. Intermittency is the design principle ("senescent cells re-accumulate slowly, so hit-and-run suffices") | mouse, **C** | 29988130 |
| **Mannick 2018** *Sci Transl Med* | Low-dose everolimus-derivative TORC1 regimen, 6 wk, 264 elderly: **improved** vaccine response, **fewer** infections | human RCT, **A** | 29997249 |
| **Ovadya 2018** | Pulsed ABT-737 extended LMNA progeroid survival without reported immune compromise | mouse, **D** | 30575733 |
| Pediatric intermittent senolytic | **No evidence located** (D+Q, fisetin, navitoclax - none) | - | - |
| Pediatric chronic senomorphic | TSC/rapalog and metformin-TODAY chronic datasets (already graded in axis doc; cross-reference, not re-verified) | human, **A** | 22540912 (metformin) |

**Assessment (Q3):** intermittent designs that (in claim) preserve surveillance do have human support at the *feasibility/toxicity* layer and animal support at the *efficacy* layer; senomorphic low-dose mTORi has the strongest *direct* human immune-preservation datum of the whole pack (Mannick). The only gap - pediatric intermittent exposure - is exactly what the Gate 0→n-of-1 structure is designed to resolve safely rather than bypass.

## Q4 - NK-clearance dependency: does chronic senolysis blunt NK/immune clearance of aneuploid cells (Santaguida–Wang)?

**Answer: the dependency is real (NK/perforin clearance of senescent cells is measurable and load-bearing), but the claimed *blunting by senolysis* is NO EVIDENCE LOCATED - and the within-study measurements point the other way. The live tension is with the *rapalog* arm (mTOR essential for NK), not with intermittent senolysis.**

| Evidence | What it shows | Species / grade | PMID |
|---|---|---|---|
| Wang 2021 + Santaguida 2017 (axis doc) | Aneuploid senescent cells activate NF-κB → promote own NK clearance; pathway intact in human cells | human cells, **C** | 34105235; 28633018 |
| Sagiv 2013 *Oncogene* | Perforin-mediated NK clearance of senescent cells (granule exocytosis) | mouse, **D** | 22751116 |
| **Ovadya 2018** *Nat Commun* | Prf1−/− (impaired cytotoxicity): MORE senescent burden, more aging disorders, lower survival - clearance pathway matters; and pharmacologic ABT-737 clearance (immune-independent) alleviated the accelerated aging - i.e., blocking NK makes senolysis MORE needed, not more dangerous | mouse, **C** | 30575733 |
| **Baker 2016** Extended Data Fig. 7 | ~6-month chronic INK-ATTAC clearance: "Senescent cell clearance has **no impact on hematological parameters and age-related changes in leukocyte populations**" including NK1.1+ cells (% PBMC), CD4+, CD8+ (verified in PMC full text) | mouse, **D** (same lab) | 26840489 |
| **Marçais 2014** *Nat Immunol* | mTOR is essential for IL-15-dependent NK development/activation - the hazard lives HERE (chronic mTORi), not in senolysis per se | mouse, **C** | 24973821 |
| **Mustjoki 2009** *Leukemia* | Chronic daily dasatinib in CML: clonal T/NK LGL expansion (NK cells are preserved under dasatinib, and at chronic daily exposure T/NK LGLs clonally expand), with expansions associated with favorable CML responses | human observational, **B** | 19295545 |
| Dasatinib acute in-vitro NK inhibition | reported in the field literature; not re-verified in this sweep - recorded as a residual pre-pulse check | in vitro, **C** | - |

**Assessment (Q4):** no study shows chronic senolysis blunting NK clearance of aneuploid/senescent cells; the one chronic-clearance study that measured blood NK numbers found no change (Baker 2016). The genuine NK-blunting hazard belongs to the *rapalog/arm-1* dose window (Marçais), and Mannick 2018 shows the human low-dose window does not manifest it. For intermittent dasatinib, the human LGL-expansion signal (Mustjoki) is if anything in the protective direction. **Decision: NK monitoring becomes a defined dose-hold trigger for Arm 1 only; no change to Arm 2's pediatric-interest framing.**

---

## VERDICT

**TIGHTEN - the R4 gate-first stance survives with hardening of the surveillance stack inside the gate; F6 partially survives (premise confirmed, empirical direction rejected) and does not displace the ordering.**

Consolidated hold against each F6 limb:
1. **"Senescence of aneuploid cells is tumor-suppressive"** - CONFIRMED (Q1a chain; Weaver 2013/2016 adds the CIN-specific layer: high mis-segregation suppresses progression).
2. **"Chronic senolysis may remove an anti-tumor barrier"** - NOT CONFIRMED: no senolytic-removal-increases-incidence datum exists in any model (Q1b); the inverse census (Q2) shows decrease or no change uniformly; the only inversion (Lalinde 2026) is macrophage-mediated and stage-dependent. The correct grade is **unmeasured mechanism (arrest-release/Milanovic-class plasticity), not demonstrated hazard**.
3. **"Baker 2008 never tested tumor endpoints"** - CONFIRMED (full-text verified, PMC2594014). This gap is real and is inherited into Gate 0's design rather than being bench-demonstrable here.

### Decision-rule change - load into Gate 0 and the n-of-1 of `wave2_SenolyticAxis.md` Q3d:

1. **Gate 0 gains a hard tumor-surveillance module.** Standard MVA surveillance (Hanks 2004/2006 spectrum: Wilms, RMS, AML; TRIP13 spectrum per Yost 2017) moves from "continued" to a **pre-specified stopping criterion**: any malignancy signal immediately halts interventional arms; cfDNA copy-number burden trajectory joins the secondary endpoint as a defined safety-burden readout, descriptive only.

2. **Burden-dominance is now a *go/continue* condition, not a retrospective argument.** Intervention starts only if proband p16+/p21+ burden is measurably elevated vs age-matched controls (Gate 0 composite) AND a second channel (SASP panel or NK-activity readout) indicates active senescent turnover. If Gate 0 shows no elevated burden, the senolytic axis **stays dormant** - surveillance-only default continues, F6 objection disarmed by never removing a barrier that carries no burden.

3. **Arm-1 rapalog NK-blunting tension operationalized as dosing rule, not removed.** NK count + monocyte/NK functional status become per-protocol **dose-hold triggers** with a Mannick-window floor (target the low-dose immunoenhancing region, not immunosuppressive troughs). This encodes Marçais 2014 without conceding the arm.

4. **Arm-2 intermittent dasatinib pulse design upgraded from "template match" to "surveillance-preserving by construction":** the 3-on/18-off window is now justified by the Wang/Santaguida mechanism (NK clearance operates in off-drug windows) in addition to Justice 2019 exposure precedent and Gore 2018 pediatric safety. Mustjoki 2009's NK/LGL-expansion signal noted as supportive, not load-bearing.

5. **Milanovic hedge added.** If the proband sentinel-cell assays detect stemness/reprogramming features associated with a senescent state (the Milanovic 2018 signature class), treat as a hard stop for senolytic arms → revert to surveillance-only + consider senomorphic-only. Off-context (no therapy-induced senescence in the proband) but cheap to check at Gate 0.

**Why gate-first rather than demote:** none of Q1–Q4 returns evidence strong enough to rank the senolytic axis below surveillance-only for a child with measured senescent burden; what they return is (a) no incidence-evidence against, (b) five-model inverse census for, (c) human pulsed-feasibility, (d) NK tension localized to the rapalog arm and manageable by dosing rule. Tightening the surveillance stack inside the gate captures every legitimate limb of F6 (burden-dominance argument, surveillance hardening, brain-stopping rules) without discarding the genotype-matched hypothesis class the axis exists to test.

## Termination declared & met

Declared criterion: each of Q1–Q4 has a graded answer or a recorded "no evidence located." Met:

| Question | Status |
|---|---|
| Q1 (senescence tumor-suppressive in vivo / senolysis ever increases incidence) | Graded **D** for barrier-half (confirmed); **no evidence located** for senolysis-increases-incidence (queries listed above; nearest counter Lalinde 2026 logged with mechanism grade D) |
| Q2 (senolysis decreasing tumors beyond Baker 2011 - census) | Graded; full census in §Q2 (6 rows; 5 non-Baker-2011 models; zero pro-tumor incidence) |
| Q3 (pulsed/senomorphic preserving surveillance) | Graded; pediatric-intermittent subpoint = **no evidence located** |
| Q4 (senolysis blunting NK clearance) | **No evidence located** for blunting-by-senolysis; tension correctly relocated to rapalog arm (Marçais 2014, mouse grade C) |

Verification record: 28 PMIDs verified via NCBI ESummary 2026-09-05; Baker 2016 tumor + leukocyte-population statements verified against PMC full text (PMC4845101, main text + Extended Data Fig. 7 legend); Baker 2008 and Wijshake 2012 checked in PMC full text for tumor-endpoint absence/presence (PMC2594014; PMC3531486). scite tallies (fetched 2026-09-05) for all load-bearing claims - **zero contrasting/disputing citations on any load-bearing ID**:

| Claim anchor | scite total | supporting | contrasting/disputing |
|---|---|---|---|
| Baker 2011 (10.1038/nature10600) | 3297 | 75 | 0 / 0 |
| Baker 2016 (10.1038/nature16932) | 2569 | 63 | 0 / 0 |
| Ovadya 2018 (10.1038/s41467-018-07825-3) | 454 | 6 | 0 / 0 |
| Marçais 2014 (10.1038/ni.2936) | 793 | 65 | 0 / 0 |
| Mustjoki 2009 (10.1038/leu.2009.46) | 346 | 23 | 0 / 0 |
| Milanovic 2018 (10.1038/nature25167) | 1044 | 44 | 0 / 0 |
| Xu 2018 (10.1038/s41591-018-0092-9) | 2078 | 60 | 0 / 0 |
| Xue 2007 (10.1038/nature05529) | 2151 | 64 | 0 / 0 |
| Kang 2011 (10.1038/nature10599) | 1577 | 49 | 0 / 0 |
| Braig 2005 (10.1038/nature03841) | 1041 | 25 | 0 / 0 |
| Justice 2019 (10.1016/j.ebiom.2018.12.052) | 924 | 12 | 0 / 0 |
| Mannick 2018 (10.1126/scitranslmed.aaq1564) | 404 | 8 | 0 / 0 |
| Haston 2023 (10.1016/j.ccell.2023.05.004) | 154 | 9 | 0 / 0 |
| Kumar 2025 (10.18632/aging.206183) | 13 | 2 | 0 / 0 |
| Lalinde-Gutiérrez 2026 (10.1126/sciadv.adx2988) | 0 | 0 | - (too new to be cited yet; grade D stands, mechanism treated cautiously) |

## References (APA, DOI-linked)

Baker, D. J., Wijshake, T., Tchkonia, T., LeBrasseur, N. K., Childs, B. G., van de Sluis, B., Kirkland, J. L., & van Deursen, J. M. (2011). Clearance of p16Ink4a-positive senescent cells delays ageing-associated disorders. *Nature, 479*(7372), 232–236. [doi:10.1038/nature10600](https://doi.org/10.1038/nature10600) (PMID 22048312)
Baker, D. J., Childs, B. G., Durik, M., et al. (2016). Naturally occurring p16(Ink4a)-positive cells shorten healthy lifespan. *Nature, 530*(7589), 184–189. [doi:10.1038/nature16932](https://doi.org/10.1038/nature16932) (PMID 26840489)
Baker, D. J., Perez-Terzic, C., Jin, F., Pitel, K. S., et al. (2008). Opposing roles for p16Ink4a and p19Arf in senescence and ageing caused by BubR1 insufficiency. *Nature Cell Biology, 10*(7), 825–836. [doi:10.1038/ncb1744](https://doi.org/10.1038/ncb1744) (PMID 18516091)
Braig, M., Lee, S., Loddenkemper, C., et al. (2005). Oncogene-induced senescence as an initial barrier in lymphoma development. *Nature, 436*(7051), 660–665. [doi:10.1038/nature03841](https://doi.org/10.1038/nature03841) (PMID 16079837)
Gallanis, G. T., Sharif, G. M., Schmidt, M. O., et al. (2023). Stromal Senescence following Treatment with the CDK4/6 Inhibitor Palbociclib Alters the Lung Metastatic Niche and Increases Metastasis of Drug-Resistant Mammary Cancer Cells. *Cancers, 15*(6), 1908. [doi:10.3390/cancers15061908](https://doi.org/10.3390/cancers15061908) (PMID 36980794)
Haston, S., Gonzalez-Gualda, E., Morsli, S., et al. (2023). Clearance of senescent macrophages ameliorates tumorigenesis in KRAS-driven lung cancer. *Cancer Cell, 41*(7), 1242–1260.e6. [doi:10.1016/j.ccell.2023.05.004](https://doi.org/10.1016/j.ccell.2023.05.004) (PMID 37267953)
Kang, T. W., Yevsa, T., Woller, N., Hoenicke, L., et al. (2011). Senescence surveillance of pre-malignant hepatocytes limits liver cancer development. *Nature, 479*(7374), 547–551. [doi:10.1038/nature10599](https://doi.org/10.1038/nature10599) (PMID 22080947)
Lalinde-Gutiérrez, M., Pérez-Ramos, S., Rodilla, V., et al. (2026). Immunosuppressive macrophages determine the effect of cellular senescence on tumor progression. *Science Advances, 12*(1), eadx2988. [doi:10.1126/sciadv.adx2988](https://doi.org/10.1126/sciadv.adx2988) (PMID 41477861)
Mannick, J. B., Morris, M., Hockey, H.-U. P., et al. (2018). TORC1 inhibition enhances immune function and reduces infections in the elderly. *Science Translational Medicine, 10*(449), eaaq1564. [doi:10.1126/scitranslmed.aaq1564](https://doi.org/10.1126/scitranslmed.aaq1564) (PMID 29997249)
Marçais, A., Cherfils-Vicini, J., Viant, C., et al. (2014). The metabolic checkpoint kinase mTOR is essential for IL-15 signaling during the development and activation of NK cells. *Nature Immunology, 15*(8), 749–757. [doi:10.1038/ni.2936](https://doi.org/10.1038/ni.2936) (PMID 24973821)
Michaloglou, C., Vredeveld, L. C., Soengas, M. S., et al. (2005). BRAFE600-associated senescence-like cell cycle arrest of human naevi. *Nature, 436*(7051), 720–724. [doi:10.1038/nature03890](https://doi.org/10.1038/nature03890) (PMID 16079850)
Milanovic, M., Fan, D. N. Y., Belenki, D., et al. (2018). Senescence-associated reprogramming promotes cancer stemness. *Nature, 553*(7686), 96–100. [doi:10.1038/nature25167](https://doi.org/10.1038/nature25167) (PMID 29258294)
Mustjoki, S., Ekblom, M., Arstila, T. P., et al. (2009). Clonal expansion of T/NK-cells during tyrosine kinase inhibitor dasatinib therapy. *Leukemia, 23*(8), 1398–1405. [doi:10.1038/leu.2009.46](https://doi.org/10.1038/leu.2009.46) (PMID 19295545)
Ovadya, Y., Landsberger, T., Leins, H., et al. (2018). Impaired immune surveillance accelerates accumulation of senescent cells and aging. *Nature Communications, 9*(1), 5435. [doi:10.1038/s41467-018-07825-3](https://doi.org/10.1038/s41467-018-07825-3) (PMID 30575733)
Sagiv, A., Biran, A., Yon, M., et al. (2013). Granule exocytosis mediates immune surveillance of senescent cells. *Oncogene, 32*(15), 1971–1977. [doi:10.1038/onc.2012.206](https://doi.org/10.1038/onc.2012.206) (PMID 22751116)
Santaguida, S., Richardson, A., Iyer, D. R., et al. (2017). Chromosome mis-segregation generates cell-cycle-arrested cells with complex karyotypes that are eliminated by the immune system. *Developmental Cell, 41*(6), 638–651.e5. [doi:10.1016/j.devcel.2017.05.022](https://doi.org/10.1016/j.devcel.2017.05.022) (PMID 28633018)
Wang, R. W., Viganò, S., Ben-David, U., Amon, A., & Santaguida, S. (2021). Aneuploid senescent cells activate NF-κB to promote their immune clearance by NK cells. *EMBO Reports, 22*(8), e52032. [doi:10.15252/embr.202052032](https://doi.org/10.15252/embr.202052032) (PMID 34105235)
Silk, A. D., Zasadil, L. M., Holland, A. J., Vitre, B., Cleveland, D. W., & Weaver, B. A. (2013). Chromosome missegregation rate predicts whether aneuploidy will promote or suppress tumors. *Proceedings of the National Academy of Sciences, 110*(43), E4134–E4141. [doi:10.1073/pnas.1317042110](https://doi.org/10.1073/pnas.1317042110) (PMID 24133140)
Zasadil, L. M., Britigan, E. M., Ryan, S. D., Kaur, C., Guckenberger, D. J., Beebe, D. J., Moser, A. R., & Weaver, B. A. (2016). High rates of chromosome missegregation suppress tumor progression but do not inhibit tumor initiation. *Molecular Biology of the Cell, 27*(13), 1981–1989. [doi:10.1091/mbc.E15-10-0747](https://doi.org/10.1091/mbc.E15-10-0747) (PMID 27146113)
Xue, W., Zender, L., Miething, C., et al. (2007). Senescence and tumour clearance is triggered by p53 restoration in murine liver carcinomas. *Nature, 445*(7128), 656–660. [doi:10.1038/nature05529](https://doi.org/10.1038/nature05529) (PMID 17251933)
Xu, M., Pirtskhalava, T., Farr, J. N., et al. (2018). Senolytics improve physical function and increase lifespan in old age. *Nature Medicine, 24*(8), 1246–1256. [doi:10.1038/s41591-018-0092-9](https://doi.org/10.1038/s41591-018-0092-9) (PMID 29988130)
Demaria, M., O'Leary, M. N., Chang, J., et al. (2017). Cellular Senescence Promotes Adverse Effects of Chemotherapy and Cancer Relapse. *Cancer Discovery, 7*(2), 165–176. [doi:10.1158/2159-8290.CD-16-0241](https://doi.org/10.1158/2159-8290.CD-16-0241) (PMID 27979832)
Ruscetti, M., Leibold, J., Bott, M. J., et al. (2019). NK cell-mediated cytotoxicity contributes to tumor control by a cytostatic drug combination. *Science, 362*(6421), 1416–1422. [doi:10.1126/science.aas9090](https://doi.org/10.1126/science.aas9090) (PMID 30573629)
Hanks, S., Coleman, K., Reid, S., et al. (2004). Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. *Nature Genetics, 36*(11), 1159–1161. [doi:10.1038/ng1449](https://doi.org/10.1038/ng1449) (PMID 15475955)
Yost, S., de Wolf, B., Hanks, S., et al. (2017). Biallelic TRIP13 mutations predispose to Wilms tumor and chromosome missegregation. *Nature Genetics, 49*(7), 1148–1151. [doi:10.1038/ng.3883](https://doi.org/10.1038/ng.3883) (PMID 28553959)
Gore, L., Kearns, P. R., de Martino Lee, M. L., et al. (2018). Dasatinib in pediatric patients with chronic myeloid leukemia in chronic phase: Results from a phase II trial. *Journal of Clinical Oncology, 36*(13), 1330–1338. [doi:10.1200/JCO.2017.75.9597](https://doi.org/10.1200/JCO.2017.75.9597) (PMID 29498925)
Justice, J. N., Nambiar, A. M., Tchkonia, T., et al. (2019). Senolytics in idiopathic pulmonary fibrosis: Results from a first-in-human, open-label, pilot study. *EBioMedicine, 40*, 554–563. [doi:10.1016/j.ebiom.2018.12.052](https://doi.org/10.1016/j.ebiom.2018.12.052) (PMID 30616998)
Kumar, K., Moon, B. H., Kumar, S., Angdisen, J., Kallakury, B. V. S., Fornace, A. J., & Suman, S. (2025). Senolytic agent ABT-263 mitigates low- and high-LET radiation-induced gastrointestinal cancer development in Apc(1638N/+) mice. *Aging, 17*(1), 97–115. [doi:10.18632/aging.206183](https://doi.org/10.18632/aging.206183) (PMID 39792466)
Zeitler, P., Hirst, K., Pyle, L., et al. (TODAY Study Group) (2012). A clinical trial to maintain glycemic control in youth with type 2 diabetes. *New England Journal of Medicine, 366*(24), 2247–2256. [doi:10.1056/NEJMoa1109333](https://doi.org/10.1056/NEJMoa1109333) (PMID 22540912)

---
## CONTROLLER ERRATUM (2026-09-05, Q11 negation re-attack)

The Q3 pediatric-senolytic row "(D+Q, fisetin, navitoclax - none)" is partially wrong:
navitoclax (ABT-263) HAS published pediatric exposure - NCT03181126 (min age 4; Pullarkat 2021
Cancer Discov, RP2D 25 mg <45 kg; EU-CTR Pediatric ITT set), St. Jude RAVEN NCT05192889
(ages 4–30, actively dosed), and two pediatric expanded-access programs (NCT05215405,
NCT03592576). What survives: no pediatric SENOLYTIC-INDICATION data (all D+Q trials ≥18 y).
See wave4_NegationReattack.md for the full registry census.
