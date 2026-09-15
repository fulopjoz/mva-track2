# Cycle-1 Mechanistic Corroboration Brief
**Adjudication question:** Do three newer mechanistic papers (PMID 25205676, 39247952, 40527892) independently upgrade the HSF1/chaperone (arimoclomol-class) and mitochondrial (elamipretide-class) routes above rapalog contention for constitutional MVA rescue?

**Disease context:** Mosaic variegated aneuploidy type 1 (biallelic BUB1B LoF), 5-year-old, Wilms/RMS predisposition. Track-2 candidate: everolimus/rapalogs. Independent table: hard-PENALIZE on rapalogs (chronic mTORC1 immunosuppression blocks NK clearance of aneuploid cells, PMID 28633018 - not re-examined here).

**Sources & date of retrieval:** All quotes verbatim from PubMed metadata (via PubMed MCP `get_article_metadata`) and PMC open-access full text (`pmc.ncbi.nlm.nih.gov/articles/PMC4253526/`, `PMC11611680/`, `PMC12174339/`), retrieved 2026-09-12. Full-text coverage: Donnelly 2014 (abstract, intro, results, discussion, methods); Ippolito 2024 (abstract through methods incl. discussion); Amponsah 2025 (abstract through methods incl. discussion). Keyword sweeps for intervention terms performed on full text.

---

## Source 1 - PMID 25205676 [CONSTITUTIONAL]
Donnelly N, Passerini V, Dürrbaum M, Stingele S, Storchová Z. **HSF1 deficiency and impaired HSP90-dependent protein folding are hallmarks of aneuploid human cells.** *EMBO J.* 2014;33(20):2374–2387. doi:[10.15252/embj.201488648](https://doi.org/10.15252/embj.201488648). PMCID: PMC4253526.

### Core findings (verbatim)
> "Here, we report that human aneuploid cells are impaired in HSP90-mediated protein folding. We show that aneuploidy impairs induction of the heat shock response suggesting that the activity of the transcription factor heat shock factor 1 (HSF1) is compromised. Indeed, increased levels of HSF1 counteract the effects of aneuploidy on HSP90 expression and protein folding, identifying HSF1 overexpression as the first aneuploidy-tolerating mutation in human cells." - **Abstract**

> "Importantly, the transient ca-HSF1 expression significantly improved the survival of aneuploid cells in the presence of 17-AAG as well as protected the folding of the FlucDM sensor against its effects (Fig 4F and G)." - **Results** ("Endogenous or exogenous overexpression of HSF1 ameliorates the negative effects of aneuploidy on protein folding")

> "Taken together, these results show that increasing the levels of the HSR master regulator HSF1 is sufficient to counteract the impaired HSP90 function of human aneuploid cells." - **Results** (same section)

> "our results suggest that in the context of the cellular response to severe proteotoxic stress (e.g. HSP90 inhibition), augmentation of HSF1 levels and/or activity fulfills a powerful cytoprotective function." - **Discussion**

> "Since trisomy in human cells leads to proliferation defects, we asked whether the difference in HSF1 expression is reflected by changes in proliferative capacity. In line with our hypothesis that HSF1 mitigates some of the phenotypes caused by aneuploidy, we observed that HCT116 clones with high HSF1 expression proliferated markedly faster than HCT116 8/3 c3" - **Results**

### Pharmacological chaperone amplification - tested?
**NO.** The rescue interventions in this paper are exclusively **genetic**: (i) endogenous HSF1 copy gain via micronuclei-mediated transfer of chromosome 8 (clones c1, c2, c4); (ii) transient transfection of a constitutively active truncated HSF1 allele (ca-HSF1). No small-molecule HSF1 activator, no arimoclomol, no HSP90/17-AAG as rescue (17-AAG is used only as a proteotoxic stressor). Grep of the full text confirms no "arimoclomol" or pharmacological chaperone-induction experiment exists.

### Caveat for constitutional use (verbatim)
> "An additional role of HSF1 in promoting carcinogenesis may be to protect cancer cells from the proteotoxic stress induced by aneuploidy. Our results lend strong support to this notion and suggest a causal link between two recurring features of cancer cells: aneuploidy and altered HSF1 activity." - **Discussion** ("Relevance for cancer and other pathologies")

Also: "HSF1 is a critical facilitator of malignant proliferation" (Discussion). Relevant to a child with Wilms/RMS predisposition.

### Direction tag
**[CONSTITUTIONAL]** - the intervention tested (HSF1 up) *tolerates/rescues* aneuploid cells (improved survival, folding, proliferation), i.e., the mosaic-tissue rescue direction; not an aneuploid-cell-killing direction. Caveat: dual-edged, as HSF1 is pro-tumorigenic.

---

## Source 2 - PMID 39247952 [ANTI-TUMOR]
Ippolito MR, Zerbib J, Eliezer Y, ..., Santaguida S, Ben-David U. **Increased RNA and protein degradation is required for counteracting transcriptional burden and proteotoxic stress in human aneuploid cells.** *Cancer Discov.* 2024;14(12):2532–2553. doi:[10.1158/2159-8290.CD-23-0309](https://doi.org/10.1158/2159-8290.CD-23-0309). PMCID: PMC11611680.

### Core findings (verbatim)
> "We found that aneuploid cells cope with transcriptional burden by increasing several RNA degradation pathways, and are consequently more sensitive to the perturbation of RNA degradation. At the protein level, aneuploid cells mitigate proteotoxic stress by reducing protein translation and increasing protein degradation, rendering them more sensitive to proteasome inhibition." - **Abstract**

> "Therefore, we conclude that aneuploid cancer cells upregulate their proteasome activity in response to proteotoxic stress, rendering them more sensitive to proteasome inhibition." - **Results** ("Increased proteasome activity and dependency in aneuploid cells")

> "aneuploidy levels were significantly associated with the response of multiple myeloma patients to proteasome inhibitors. Aneuploid cells are therefore preferentially dependent on several key nodes along the gene expression process, creating clinically actionable vulnerabilities in aneuploid cells." - **Abstract**

> "cardiac glycosides might represent a novel class of anti-aneuploid cancer therapeutics through targeting of NMD; and proteasome inhibitors might be preferentially effective against aneuploid cancer cells due to their increased reliance on the proteasome activity (Fig. 7). Those vulnerabilities might be further exacerbated by the ongoing CIN that characterizes aneuploid cancer cells." - **Discussion** ("Concluding remarks")

### Rapamycin-class autophagy induction - tested positively, or irrelevant/conflicting?
**NOT TESTED - irrelevant to this paper's experimental design.** A full-text keyword sweep for `autophag|rapamycin|mTOR|chloroquine|p62|SQSTM1` returns hits **only in the reference list**: reference 16 is Santaguida S, Vasile E, White E, Amon A. "Aneuploidy-induced cellular stresses limit autophagic degradation." *Genes Dev.* 2015;29:2010–21 (PMID 26404941). No rapamycin, mTOR, or autophagy-perturbation experiment appears anywhere in the results, methods, or figures. The paper's degradation story is the **proteasome** (bortezomib, MG132) and **RNA degradation** (NMD inhibitors ouabain/digoxin; CASC3/DROSHA siRNA) - no macroautophagy induction or inhibition was assayed. The cited Santaguida 2015 title ("stresses limit autophagic degradation") points toward saturated/limited autophagy in aneuploid cells rather than inducible headroom, but that evidence is *cited*, not generated, here.

### Direction tag
**[ANTI-TUMOR]** - every therapeutic experiment exploits the degradation dependency to *kill or sensitize aneuploid cells* (bortezomib EC50 shifts, PRISM screen with reversine + bortezomib, myeloma patient response). There is no experiment rescuing normal aneuploid (mosaic) tissue; the paper is explicitly framed around "clinically-actionable vulnerabilities in aneuploid cells."

---

## Source 3 - PMID 40527892 [CONSTITUTIONAL]
Amponsah PS, Bökenkamp J-E, Kurpa O, ..., Herrmann JM, Räschle M, Storchová Z. **Aneuploidy-induced proteostasis disruption impairs mitochondrial functions and mediates aggregation of mitochondrial precursor proteins through SQSTM1/p62.** *Nat Commun.* 2025;16:5328. doi:[10.1038/s41467-025-60857-4](https://doi.org/10.1038/s41467-025-60857-4). PMCID: PMC12174339.

### Core findings (verbatim)
> "Compared to parental diploids, aneuploid cells suffer from mitochondrial defects, including perinuclearly-clustered mitochondrial networks, elevated reactive oxygen species levels, reduced mitochondrial DNA abundance, and impaired protein import, leading to cytosolic accumulation of mitochondrial precursor proteins. Overexpression of heat shock proteins in aneuploid cells mitigates protein aggregation and decreases the colocalization of p62 with the mitochondrial protein TOMM20." - **Abstract**

> "Strikingly, we observed an increased accumulation of the precursor forms of each of the proteins in whole-cell lysates of the polysomic cells (Fig. 7b). This indicates that mitochondria of polysomic cells exhibit import defects, despite their normal membrane potential" - **Results** ("Mitochondrial protein import is diminished in cells with extra chromosomes")

> "Kinetic import analysis revealed a delayed import of both su9-DHFR and human SOD2 into isolated mitochondria from polysomic cells (Fig. 7c, d, and Supplementary Fig. 10c, d)." - **Results** (same section)

> "We conclude that the proteotoxic stress and mitochondrial defect can be rescued by transient overexpression of cytosolic chaperones, but only in polysomic cells suffering from mild proteotoxic stress. Severe proteotoxic stress, as in the 5/4 cell line with high numbers of extra protein coding genes, could not be fully rescued." - **Results** ("Cytosolic proteostasis critically affects the formation of p62 bodies and mitochondrial function")

> "Overexpression of these constructs was confirmed by Western blot... In all instances, we observed decreased numbers of p62-positive foci, but increased foci sizes" - **Results** (same section; constructs: HSP27, HSP90α-Flag, EGFP-HSF1, constitutively active HSF1)

### Interventions tested (mitochondrial stabilization agents, importers?)
**NO mitochondrial-targeted pharmacological intervention.** The complete intervention inventory is: (i) **rescue:** transient overexpression of HSP27, HSP90α-Flag, EGFP-HSF1, ca-HSF1 (all genetic, all cytosolic chaperone/HSF class); (ii) **stressor/phenocopy controls:** CCCP (membrane-potence uncoupler, 10 µM 6 h), H2O2, MG132 (aggresome positive control); (iii) **assay reagent:** Bafilomycin A1 (autophagosome–lysosome fusion inhibitor, 100 nM 6 h). Full-text sweep for `rapamycin|elamipretide|SS-31|everolimus|mTOR` returns hits **only in reference titles** (e.g., ref. 48, Lam et al. on p62/mTORC1). No elamipretide/SS-31/Bendavia, no cardiolipin-binding peptide, no mitochondrial import-enhancing compound was tested. The only rescue that worked was again the **chaperone class** - and notably the rescue of mitochondrial phenotypes was achieved by fixing *cytosolic* proteostasis, not by stabilizing mitochondria directly.

### Direction tag
**[CONSTITUTIONAL]** - the tested intervention reduces protein aggregation and p62–mitochondria colocalization in aneuploid cells (rescuing/ameliorating the aneuploid state), not killing aneuploid cells. Predominantly a mechanism/description paper with a constitutional-direction rescue experiment.

---

## Sanity sweep - direction table

| PMID | Paper | Intervention direction | Tag |
|---|---|---|---|
| 25205676 | Donnelly 2014, EMBO J | HSF1 gain (chr 8 transfer, ca-HSF1) *tolerates* aneuploid cells → improves folding, survival, proliferation of aneuploids | **[CONSTITUTIONAL]** |
| 39247952 | Ippolito 2024, Cancer Discov | Bortezomib/ouabain *kill/sensitize* aneuploid cells; aneuploidy as biomarker of proteasome-inhibitor response | **[ANTI-TUMOR]** |
| 40527892 | Amponsah 2025, Nat Commun | HSP/HSF1 overexpression *ameliorates* aggregation + p62–TOMM20 colocalization in polysomic cells | **[CONSTITUTIONAL]** |

---

## Analysis: does this move arimoclomol/elamipretide above contested everolimus?

### HSF1/chaperone (arimoclomol-class) - MODERATELY STRENGTHENED
Two independent papers (25205676, 40527892, both from the Storchová group but different model systems/readouts and 11 years apart) converge on: HSF1 activity is limiting in aneuploid cells, and augmenting the HSF1/chaperone axis rescues proteotoxic-stress phenotypes - including the *downstream mitochondrial* phenotype (Amponsah: reduced p62–TOMM20 colocalization, reduced aggresome staining). This is constitutional-direction rescue evidence and directly supports arimoclomol-class co-induction of the heat shock response as the mechanistically best-grounded discussion candidate. **Limits:** (i) all rescue evidence is genetic overexpression, not pharmacological - no arimoclomol, no small-molecule HSF1 activator tested in any of the three papers; (ii) Amponsah shows rescue fails in the most severely affected line (5/4 tetrasomy), so effect size is stress-load-dependent; (iii) both papers themselves flag HSF1 as pro-tumorigenic ("HSF1 is a critical facilitator of malignant proliferation"), a real caution in a Wilms/RMS-predisposed child, though this argues for dosing discussion, not exclusion.

### Mitochondrial (elamipretide-class) - TARGET VALIDATED, INTERVENTION NOT
Amponsah 2025 firmly establishes that chromosome gain *causes* mitochondrial dysfunction (ROS↑, mtDNA↓ ~60–80%, Complex-I oxygen consumption ~50% of parental, delayed precursor import, precursor sequestration in p62 bodies). This is genuine target validation for mitochondrial rescue in constitutional aneuploidy. **However:** the only tested intervention that rescued the mitochondrial phenotype was cytosolic chaperone/HSF1 overexpression - i.e., the paper's own evidence routes the mitochondrial phenotype back through the chaperone axis. No elamipretide/SS-31 or any mitochondrially targeted agent was tested; the mitochondrial defects occurred "despite their normal membrane potential," which is a poor mechanistic fit for elamipretide's cardiolipin/membrane-potential stabilization mechanism. Upgrade for elamipretide-class: weak-to-moderate (rationale only, no intervention data).

### Rapalog (everolimus) - NOT TESTED, NOT RESCUED
None of the three papers tests rapamycin/everolimus or mTORC1 inhibition in any direction. Ippolito 2024 is explicitly anti-tumor-directed (exploit degradation dependency to kill aneuploid cells) and shows aneuploid cells already constitutively downregulate translation - a state mTORC1 inhibition would deepen. Its only autophagy-relevant citation (Santaguida 2015) indicates autophagic degradation is *limited* by aneuploidy-induced stress, which cuts against autophagy-induction rescue headroom, but this is cited, not demonstrated, here. Thus these papers neither support nor refute everolimus for constitutional rescue; the rapalog contention stands or falls on other evidence (including the NK-clearance PENALIZE argument, PMID 28633018, out of scope here).

### Verdict
The three papers **upgrade the HSF1/chaperone (arimoclomol-class) route moderately above rapalogs** as a constitutional-rescue discussion candidate - convergent, constitutional-direction, two-paper rescue evidence, but genetic-only and with a pro-tumor caveat. They **do NOT meaningfully upgrade the elamipretide-class route**: mitochondrial dysfunction is validated as a real consequence of aneuploidy, but the only demonstrated rescue of that phenotype runs through chaperones, and no mitochondrial-targeted agent was tested. Everolimus remains contested on evidence outside these three papers; nothing here rehabilitates it, and the anti-tumor framing of Ippolito 2024 is a reminder that most aneuploidy-drug literature is directed at killing aneuploid cells, not rescuing them.

**Confidence: moderate.** All quotes verified verbatim from PMC full text on 2026-09-12; negative findings (no arimoclomol/rapamycin/elamipretide experiments) verified by exhaustive keyword sweeps of the full retrieved text. Confidence limited by: (i) two of three papers from one group (Storchová) - "independent" only in model systems and readouts, not fully in provenance; (ii) all rescue data from engineered trisomy/tetrasomy cell lines, not primary MVA patient tissue; (iii) genetic-vs-pharmacological extrapolation gap for arimoclomol.

## References
- Donnelly, N., Passerini, V., Dürrbaum, M., Stingele, S., & Storchová, Z. (2014). HSF1 deficiency and impaired HSP90-dependent protein folding are hallmarks of aneuploid human cells. *EMBO Journal, 33*(20), 2374–2387. https://doi.org/10.15252/embj.201488648 (PMID 25205676; PMC4253526)
- Ippolito, M. R., Zerbib, J., Eliezer, Y., et al. (2024). Increased RNA and protein degradation is required for counteracting transcriptional burden and proteotoxic stress in human aneuploid cells. *Cancer Discovery, 14*(12), 2532–2553. https://doi.org/10.1158/2159-8290.CD-23-0309 (PMID 39247952; PMC11611680)
- Amponsah, P. S., Bökenkamp, J.-E., Kurpa, O., et al. (2025). Aneuploidy-induced proteostasis disruption impairs mitochondrial functions and mediates aggregation of mitochondrial precursor proteins through SQSTM1/p62. *Nature Communications, 16*, 5328. https://doi.org/10.1038/s41467-025-60857-4 (PMID 40527892; PMC12174339)
- (Cited-only, not independently verified here) Santaguida, S., Vasile, E., White, E., & Amon, A. (2015). Aneuploidy-induced cellular stresses limit autophagic degradation. *Genes & Development, 29*(19), 2010–2021. https://doi.org/10.1101/gad.269118.115 (PMID 26404941)
