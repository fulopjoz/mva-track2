# Wave 2 - Q3 Senolytic Axis: translation path for senolysis from the INK-ATTAC BubR1-hypomorph proof

Grades: **A** = human RCT · **B** = human clinical/observational · **C** = human cells or independent-lab animal · **D** = mouse-only / single-lab · **[INFERENCE]** flagged per claim.

---

## VERDICT

**Senolysis in MVA is a genuine genotype-matched research hypothesis but currently fails translation on three seam-specific points: (1) the core efficacy result rests on one laboratory (Mayo/van Deursen) and one mouse line - no independent group has ever replicated senolysis in a BubR1-hypomorphic animal; (2) there is zero direct evidence of a senescent-cell burden in human BUB1B-MVA tissue, so the disease-model premise itself is unmeasured in patients; (3) no senolytic has any pediatric exposure - the only components with pediatric chronic-safety data are senomorphic-class drugs (rapalogs, metformin) and, surprisingly, dasatinib (approved in children ≥1 y for Ph⁺ leukemia).** The realistic near-term deliverable is therefore NOT a senolytic drug for the proband; it is (a) a patient-derived-cell senescence-burden assay (Gate 0, feasible inside the existing consent envelope) and (b) a biomarker-gated n-of-1 adaptive design built on the TAME framework with p16^INK4a^ in peripheral-blood T-cells as the gating readout, in which the chronic-senomorphic arm (rapalog/metformin) is fallback-feasible today and any dasatinib-containing senolytic arm is investigational-only. Confidence: **medium-high** for the replication/feasibility findings (searches are negative-evidence with explicit query records below); **low** that senolysis itself ever becomes a pediatric-prevention node without the Gate-0 human-burden data.

---

## Q3a - Replication status of the Baker 2011 INK-ATTAC × BubR1-hypomorph result

**The load-bearing result:** AP20187-induced clearance of p16^Ink4a^⁺ senescent cells in BubR1 hypomorphic mice delayed onset and attenuated progression of progeroid aging phenotypes in fat, muscle, and eye. Baker DJ et al., *Nature* 2011;479:232–6 - PMID **22048312** ([DOI](https://doi.org/10.1038/nature10600)). Grade **D** (mouse, transgenic drug-like switch, not a pharmacology), human flag: **none**.

**Replication inventory (searched 2026-09-05):**

| Query (PubMed) | Result |
|---|---|
| `BubR1 INK-ATTAC` | 1 paper total - Baker 2011 only |
| `BubR1 senolytic` | 0 papers |
| `BubR1 hypomorphic mice accelerated aging` | 3 papers, all Mayo-authored |

- **Same-lab corroboration exists and is genuine:** genetic (p16^Ink4a^ inactivation attenuates senescence/aging in BubR1-insufficient mice - Baker 2008, *Nat Cell Biol* 10:825–36, PMID **18516091**, [DOI](https://doi.org/10.1038/ncb1744)) and pharmacologic-switch replication in *non*-progeroid wild-type mice (lifespan extension, delayed tumorigenesis on two genetic backgrounds - Baker 2016, *Nature* 530:184–9, PMID **26840489**, [DOI](https://doi.org/10.1038/nature16932)). The 2016 paper is a **within-lab replication of the mechanism class in a different background**, not an independent replication. Grade **D** each (mouse same-lab).
- **Independent-lab replication of the BubR1 senolysis result: none located.** Every BubR1-hypomorph mouse paper in PubMed carries Mayo/van Deursen-associated authorship; the BubR1^H/H^ line is effectively a single-origin research resource (Con: no bibliometric channel searched - flagged as gap §Gaps; positive high-certainty signal that no *PubMed-indexed* independent pharmacologic-senolysis study in a BubR1-mutant animal exists).
- **Partially independent cross-corroboration (different labs, adjacent chains):**
  - Schliekelman et al. 2009 (UNC, Van Dyke lab), *Cancer Res* 69:45–54, PMID **19117986** ([DOI](https://doi.org/10.1158/0008-5472.CAN-07-6330)): an independent SAC-hypomorph mouse (Bub1) shows **high premature senescence** in MEFs - independently supports "SAC insufficiency → senescence burden". Grade **C** (independent, mouse).
  - North et al. 2014 (Sinclair/Harvard + Mayo), *EMBO J* 33:1438–53, PMID **24825348** ([DOI](https://doi.org/10.15252/embj.201386907)): SIRT2/NMN raises BubR1 **abundance in vivo** and extends BubR1^H/H^ lifespan - independent-lab co-lead instrumenting the *abundance–lifespan* link in the same mouse. Grade **C/D**. **Cross-feed note for StabilizationAxis (Q2): this is a published in-vivo proof that a druggable enzyme-class (SIRT2/NAD⁺) raises BubR1 abundance in living animals** - relevant to the N1002K allele class.
  - Baker 2006, *J Cell Biol* 172:529–40, PMID **16476774** ([DOI](https://doi.org/10.1083/jcb.200507081)): Bub3/Rae1-haploinsufficiency → premature senescence; notably, aging speed tracked **senescence, not aneuploidy** across two checkpoint-defective strains. Same lab; Grade **D**.

**Verdict (Q3a):** the Baker 2011 result is internally corroborated but **independently unreplicated 15 years after publication**; treat all dose/efficacy extrapolations from it as single-lab.

## Q3b - Senescent-cell burden in human CIN/MVA tissue

**Direct evidence: none located.** Both targeted searches returned zero relevant records: `mosaic variegated aneuploidy senescence fibroblast` (only an unrelated Werner-syndrome paper) and `BUB1B mutant patient cells senescence p16` (0). **No biopsy, fibroblast, or blood senescence measurement has been published on any BUB1B-MVA patient.** This is the axis's largest gap and also its cheapest-to-close assay (below).

**Indirect evidence (ranked):**

1. **Human phenotypic bridge** - MVA patients show progeroid features (facial dysmorphism, short stature, cataracts) plus childhood-cancer predisposition: Hanks 2004, *Nat Genet* 36:1159–61, PMID **15475955** ([DOI](https://doi.org/10.1038/ng1449)); Wijshake 2012, *PLoS Genet* 8:e1003138, PMID **23300461** ([DOI](https://doi.org/10.1371/journal.pgen.1003138)). Grade **B** (human, descriptive).
2. **Human-cell mechanistic chain** - chromosome mis-segregation in *untransformed human cells* generates senescence-arrested cells with pro-inflammatory SASP that are eliminated by NK cells in vitro: Santaguida 2017, *Dev Cell* 41:638–651.e5, PMID **28633018** ([DOI](https://doi.org/10.1016/j.devcel.2017.05.022)); Wang 2021, *EMBO Rep* 22:e52032, PMID **34105235** ([DOI](https://doi.org/10.15252/embr.202052032)). Grade **C** (human cells, independent groups). Establishes the *aneuploidy→senescence→immune-clearance* pathway is intact in human cells, not whether MVA patient tissue carries an elevated steady-state burden.
3. **Mouse burden evidence** - p16/p19 accumulation and senescence specifically in BubR1^H/H^ muscle and fat (Baker 2008, above). Grade **D** (mouse only).
4. **Human MVA patient-cell biology is studied** (SAC impairment in TRIP13 vs BUB1B mutants; Yost 2017, *Nat Genet* 49:1148–51, PMID **28553959**, [DOI](https://doi.org/10.1038/ng.3883)) - patient-derived material is obtainable and established methods exist; senescence simply was never the readout. Grade **B** for feasibility of Gate 0.

**Verdict (Q3b):** burden premise = **highly plausible but unmeasured**. Any senolytic framing in the submission MUST be gated on proband-cell data, not on the mouse.

## Q3c - Pediatric-feasible senolytic / senomorphic precedents

**True senolytics - pediatric feasibility:**

| Agent | Pediatric evidence | Source/Grade |
|---|---|---|
| **Dasatinib ± quercetin (D+Q)** | **No pediatric senolytic exposure located** (all human senolytic data are adult: D+Q first-in-human IPF pilot, 14 adults, intermittent D 100 mg/Q 1250 mg 3 d/wk × 3 wk, feasible, mild events; Justice 2019, *EBioMedicine* 40:554–63, PMID **30616998**, [DOI](https://doi.org/10.1016/j.ebiom.2018.12.052)). Grade **B⁻** (adult only). |
| *(Component view)* **Dasatinib alone** | **Formal pediatric chronic-safety dataset**: phase II, 113 patients <18 y, chronic daily dosing in pediatric CML, no dasatinib-related pleural/pericardial effusion or pulmonary arterial hypertension, bone-growth events 4 %; Gore 2018, *J Clin Oncol* 36:1330–8, PMID **29498925** ([DOI](https://doi.org/10.1200/JCO.2017.75.9597)). Grade **B** (leukemia-context dosing; intermittent senolytic pulsing untested in children). |
| Quercetin / fisetin | No pediatric trial exposure located. Listed as gap. |

**Senomorphics - pediatric-feasible classes:**

- **Rapalogs (everolimus/sirolimus)** - the only **chronically pediatric-established** class (TSC EXIST RCTs per attack map G3-6; cross-reference, not re-verified here). Geroprotective/senomorphic human proof exists in adults: TORC1-inhibitor RCT in 264 elderly → fewer infections, better vaccine response (Mannick 2018, *Sci Transl Med* 10:eaaq1564, PMID **29997249**, [DOI](https://doi.org/10.1126/scitranslmed.aaq1564)). Grade **A** (adult RCT). Cell-level precedent for rescuing a *progeria-genotype* senescent state in patient fibroblasts: rapamycin (Cenni 2011, *Eur J Histochem* 55:e36, PMID **22297442**, [DOI](https://doi.org/10.4081/ejh.2011.e36)) and temsirolimus (Gabriel 2017, *PLoS One* 11:e0168988, PMID **28033363**, [DOI](https://doi.org/10.1371/journal.pone.0168988)) in HGPS cells. Grade **C**.
- **Metformin** - chronic pediatric administration is RCT-established at 10–17 y for T2DM (TODAY; 699 youth, ~3.9 y follow-up; Zeitler 2012, *N Engl J Med* 366:2247–56, PMID **22540912**, [DOI](https://doi.org/10.1056/NEJMoa1109333)). Grade **A** (pediatric RCT, non-senolytic indication). Geroprotective-trial design framework available (TAME; see Q3d).
- **[INFERENCE] Tension flag:** rapalogs are immunosuppressive at higher exposure, while Santaguida 2017/Wang 2021 show aneuploid-senescent clearance is **NK-immune-mediated**; chronic rapalog dosing could theoretically blunt the very clearance mechanism the model relies on. Direction/magnitude **unmeasured**; resolves only in proband-relevant models. Low-grade but material design consideration for the rapalog arm.

**Verdict (Q3c):** no pediatric senolytic precedent exists at all; pediatric-feasible options are **chronic senomorphics** (rapalog ≫ metformin for CIN-relevance) and, with explicit investigational framing, **intermittent dasatinib-only pulses** - the one true senolytic backboned by pediatric chronic-safety data (efficacy as senolytic in a child: zero evidence located).

## Q3d - Concrete biomarker-gated design for the proband (child, MVA, no current tumor)

Anchors: TAME biomarker selection framework (Justice 2018, *GeroScience* 40:419–36, PMID **30151729**, [DOI](https://doi.org/10.1007/s11357-018-0042-y) - criteria: reliability, aging-relevance, mortality prediction, **responsiveness to intervention**), p16^INK4a^ RNA in peripheral-blood T-cells as a validated human blood senescence-burden readout (Liu 2009, *Aging Cell* 8:439–48, PMID **19485966**, [DOI](https://doi.org/10.1111/j.1474-9726.2009.00489.x)), and the only in-human senolytic dose template (intermittent D+Q; Justice 2019).

**Gate 0 - patient-cell burden assay (prerequisite, non-interventional, cheap):**
proband skin fibroblasts + peripheral-blood T-cells → p16/p21 RNA, SA-β-gal, SASP cytokine panel, aneuploidy fraction vs age-matched controls. This single assay converts the entire axis's premise from mouse to human. Deliverable within the organizing team's existing consent envelope; cost ≈ one lab-quarter.

**Design (only if Gate 0 positive): single-patient, adaptive, biomarker-gated n-of-1 (ABA withdrawal), 12–18 months:**

1. **Primary endpoint (winnable):** within-patient suppression of a senescence-burden composite - p16^INK4a^ T-cell RNA (Liu 2009 assay), plasma SASP panel per TAME shortlist (IL-6, CRP, GDF-15), plus functional MVA-relevant measures (growth velocity, grip/muscle function) selected for **responsiveness to intervention** per the TAME criteria. Tumor latency is explicitly **NOT** the primary endpoint - it is unstatistics-able in n=1 over a feasible horizon.
2. **Secondary/surveillance-linked endpoint (tumor-latency surrogate, honest version):** trend of **circulating aneuploid-cell markers / cell-free DNA copy-number-burden** where assayable + continuation of standard MVA cancer surveillance (embryonal-tumor spectrum per Hanks 2004/2006; BUB1B-relevant Wilms/RMS/AML per Yost 2017). Treated as descriptive trajectory data, never as an efficacy claim.
3. **Arms (sequential, not parallel):**
   - **Arm 1 (fallback-feasible today):** chronic senomorphic - rapalog class (existing pediatric TSC safety; blood-level-targeted immunosuppression-avoidance window), or metformin if rapalog declined; 6-month blocks with 6–8-week biomarker troughs between.
   - **Arm 2 (investigational only, IRB single-patient/compassionate frame):** **intermittent dasatinib-only pulses** modelled on Justice 2019 (3 days on / 3 weeks off × 3 cycles) - excludes quercetin (no pediatric data), leverages Gore 2018 pediatric dasatinib safety; monitored: growth, cardiopulmonary (PAH), marrow.
4. **Safety/efficacy logic keyed to the mouse model's two lessons:** the benefit class is chronic-burden reduction (Baker 2016 natural-aging replication), and removal efficiency may depend on NK immune tone (Wang 2021) - hence rapalog-dose-region flag from Q3c is operationalized: monitor NK numbers; dose-hold criteria predefined.
5. **Decision rule:** continue/escalate only with (i) ≥ pre-specified reduction in Gate-0-defined median burden composite and (ii) zero pre-specified safety triggers; otherwise revert to surveillance-only management, which remains the evidence-consistent default for every CIN syndrome (cross-reference Q4's precedent-classes finding).

**Verdict (Q3d):** a rigorously biomarker-gated n-of-1 is designable today with published assay anchors; what cannot be promised is that any arm moves the biomarkers in this genotype.

---

## GAPS (explicit; none silently closed)

1. **No independent replication** of BubR1-hypomorph senolysis by any non-Mayo group (PubMed-negative evidence; scite citation-context check deferred - token environment flagged in attack map; a bibliometric "cited-by-replicated-experimentally" sweep would formalize this).
2. **Zero human MVA senescence data** - the entire burden premise rests on mouse + generic human-cell aneuploidy work. Gate 0 closes it.
3. **No pediatric senolytic exposure for any agent** (D+Q, fisetin, navitoclax): absence-of-evidence from PubMed searches 2026-09-05, not proof of absence.
4. **Dasatinib intermittent/pulse PK-safety in children unknown** - leukemia safety is daily-dose; per-exposure senolytic pulsing is pharmacologically distinct `[INFERENCE]`.
5. **Unknown whether senescent-cell removal is beneficial or treadmill-neutral against continuously generated mis-segregation** in an MVA child; no mouse longevity model addressed stem-cell depletion risk of chronic p16⁺ ablation in a CIN-high background `[INFERENCE]`.
6. **Rapalog-vs-NK-clearance tension** quantified nowhere (Q3c flag).

## Interfaces to sibling axes

- **→ StabilizationAxis (Q2):** North 2014 (PMID 24825348) is an in-vivo, druggable-class (SIRT2/NAD⁺) BubR1-abundance-raising proof - treat as the only bench-to-animal abundance-stabilization datapoint located in this sweep.
- **→ CINSyndromeAxis (Q4):** rapalog/metformin chronic-pediatric precedents (EXIST, TODAY) and the "no approved preventive in any CIN syndrome" finding overlap; this axis supplied the senescence-biomarker machinery (p16-PBTL, TAME panel) that any MVA prevention trial would reuse.
- **→ NonsenseAxis (Q1):** none direct; if L737Ter readthrough restores BubR1 abundance above the ~13 % threshold, the senolytic hypothesis becomes moot for prevention - senolysis abundance-dependence noted from Baker 2006/2008 (senescence trigger is BubR1 *insufficiency*).

## Methodology / termination

Termination criterion (declared 2026-09-05): each of Q3a–d carries ≥2 PubMed-verified primary sources **or** an explicit, query-recorded "no evidence located" gap. Met - Q3b(2), Q3c(fisetin/quercetin/navt), and Q3a(independent replication) are recorded negatives, not omissions. All 20 cited identifiers verified through PubMed metadata during this sweep; three initially-recalled PMIDs (30653987, 27346422, 21746707, 24874789) failed verification and were re-grounded from search before use. Citation-verifier pass (link works + content relevant + fact check): all 20 pass. Source attribution: all bibliographic data retrieved via PubMed. scite grading unavailable in this environment (per attack-map disclosure, pre-expiry); negative-replication claims therefore rest on recorded PubMed queries, not Smart-Citation tallies - flagged as residual gap 1.

## References (APA, DOI-linked)

Baker, D. J., Wijshake, T., Tchkonia, T., LeBrasseur, N. K., Childs, B. G., van de Sluis, B., Kirkland, J. L., & van Deursen, J. M. (2011). Clearance of p16Ink4a-positive senescent cells delays ageing-associated disorders. *Nature, 479*(7372), 232–236. [doi:10.1038/nature10600](https://doi.org/10.1038/nature10600) (PMID 22048312)
Baker, D. J., Perez-Terzic, C., Jin, F., Pitel, K. S., et al. (2008). Opposing roles for p16Ink4a and p19Arf in senescence and ageing caused by BubR1 insufficiency. *Nature Cell Biology, 10*(7), 825–836. [doi:10.1038/ncb1744](https://doi.org/10.1038/ncb1744) (PMID 18516091)
Baker, D. J., Childs, B. G., Durik, M., et al. (2016). Naturally occurring p16(Ink4a)-positive cells shorten healthy lifespan. *Nature, 530*(7589), 184–189. [doi:10.1038/nature16932](https://doi.org/10.1038/nature16932) (PMID 26840489)
Baker, D. J., Jeganathan, K. B., Malureanu, L., Perez-Terzic, C., Terzic, A., & van Deursen, J. M. (2006). Early aging-associated phenotypes in Bub3/Rae1 haploinsufficient mice. *Journal of Cell Biology, 172*(4), 529–540. [doi:10.1083/jcb.200507081](https://doi.org/10.1083/jcb.200507081) (PMID 16476774)
Cenni, V., Capanni, C., Columbaro, M., et al. (2011). Autophagic degradation of farnesylated prelamin A as a therapeutic approach to lamin-linked progeria. *European Journal of Histochemistry, 55*(4), e36. [doi:10.4081/ejh.2011.e36](https://doi.org/10.4081/ejh.2011.e36) (PMID 22297442)
Gabriel, D., Gordon, L. B., & Djabali, K. (2017). Temsirolimus partially rescues the Hutchinson-Gilford progeria cellular phenotype. *PLoS ONE, 11*(12), e0168988. [doi:10.1371/journal.pone.0168988](https://doi.org/10.1371/journal.pone.0168988) (PMID 28033363)
Gore, L., Kearns, P. R., de Martino Lee, M. L., et al. (2018). Dasatinib in pediatric patients with chronic myeloid leukemia in chronic phase: Results from a phase II trial. *Journal of Clinical Oncology, 36*(13), 1330–1338. [doi:10.1200/JCO.2017.75.9597](https://doi.org/10.1200/JCO.2017.75.9597) (PMID 29498925)
Hanks, S., Coleman, K., Reid, S., et al. (2004). Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. *Nature Genetics, 36*(11), 1159–1161. [doi:10.1038/ng1449](https://doi.org/10.1038/ng1449) (PMID 15475955)
Hanks, S., Coleman, K., Summersgill, B., et al. (2006). Comparative genomic hybridization and BUB1B mutation analyses in childhood cancers associated with mosaic variegated aneuploidy syndrome. *Cancer Letters, 239*(2), 234–238. [doi:10.1016/j.canlet.2005.08.006](https://doi.org/10.1016/j.canlet.2005.08.006) (PMID 16182441)
Justice, J. N., Ferrucci, L., Newman, A. B., et al. (2018). A framework for selection of blood-based biomarkers for geroscience-guided clinical trials: Report from the TAME Biomarkers Workgroup. *GeroScience, 40*(5-6), 419–436. [doi:10.1007/s11357-018-0042-y](https://doi.org/10.1007/s11357-018-0042-y) (PMID 30151729)
Justice, J. N., Nambiar, A. M., Tchkonia, T., et al. (2019). Senolytics in idiopathic pulmonary fibrosis: Results from a first-in-human, open-label, pilot study. *EBioMedicine, 40*, 554–563. [doi:10.1016/j.ebiom.2018.12.052](https://doi.org/10.1016/j.ebiom.2018.12.052) (PMID 30616998)
Liu, Y., Sanoff, H. K., Cho, H., et al. (2009). Expression of p16(INK4a) in peripheral blood T-cells is a biomarker of human aging. *Aging Cell, 8*(4), 439–448. [doi:10.1111/j.1474-9726.2009.00489.x](https://doi.org/10.1111/j.1474-9726.2009.00489.x) (PMID 19485966)
Mannick, J. B., Morris, M., Hockey, H.-U. P., et al. (2018). TORC1 inhibition enhances immune function and reduces infections in the elderly. *Science Translational Medicine, 10*(449), eaaq1564. [doi:10.1126/scitranslmed.aaq1564](https://doi.org/10.1126/scitranslmed.aaq1564) (PMID 29997249)
North, B. J., Rosenberg, M. A., Jeganathan, K. B., et al. (2014). SIRT2 induces the checkpoint kinase BubR1 to increase lifespan. *EMBO Journal, 33*(13), 1438–1453. [doi:10.15252/embj.201386907](https://doi.org/10.15252/embj.201386907) (PMID 24825348)
Santaguida, S., Richardson, A., Iyer, D. R., et al. (2017). Chromosome mis-segregation generates cell-cycle-arrested cells with complex karyotypes that are eliminated by the immune system. *Developmental Cell, 41*(6), 638–651.e5. [doi:10.1016/j.devcel.2017.05.022](https://doi.org/10.1016/j.devcel.2017.05.022) (PMID 28633018)
Schliekelman, M., Cowley, D. O., O'Quinn, R., Oliver, T. G., Lu, L., Salmon, E. D., & Van Dyke, T. (2009). Impaired Bub1 function in vivo compromises tension-dependent checkpoint function leading to aneuploidy and tumorigenesis. *Cancer Research, 69*(1), 45–54. [doi:10.1158/0008-5472.CAN-07-6330](https://doi.org/10.1158/0008-5472.CAN-07-6330) (PMID 19117986)
Wang, R. W., Viganò, S., Ben-David, U., Amon, A., & Santaguida, S. (2021). Aneuploid senescent cells activate NF-κB to promote their immune clearance by NK cells. *EMBO Reports, 22*(8), e52032. [doi:10.15252/embr.202052032](https://doi.org/10.15252/embr.202052032) (PMID 34105235)
Wijshake, T., Malureanu, L. A., Baker, D. J., et al. (2012). Reduced life- and healthspan in mice carrying a mono-allelic BubR1 MVA mutation. *PLoS Genetics, 8*(12), e1003138. [doi:10.1371/journal.pgen.1003138](https://doi.org/10.1371/journal.pgen.1003138) (PMID 23300461)
Yost, S., de Wolf, B., Hanks, S., et al. (2017). Biallelic TRIP13 mutations predispose to Wilms tumor and chromosome missegregation. *Nature Genetics, 49*(7), 1148–1151. [doi:10.1038/ng.3883](https://doi.org/10.1038/ng.3883) (PMID 28553959)
Zeitler, P., Hirst, K., Pyle, L., et al. (TODAY Study Group) (2012). A clinical trial to maintain glycemic control in youth with type 2 diabetes. *New England Journal of Medicine, 366*(24), 2247–2256. [doi:10.1056/NEJMoa1109333](https://doi.org/10.1056/NEJMoa1109333) (PMID 22540912)
