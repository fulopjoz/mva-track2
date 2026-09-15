# G3 - PhenotypeAxis: Which aneuploidy-stress axis dominates in HUMAN/mammalian data?

**Companion to** `LITERATURE_SWEEP.md` (Axis a–d) and `VARIANT_PROTEIN_IMPACT.md`.
Scope: precision-repurposing gating question G3 for the BUB1B MVA1 proband
(p.Leu737Ter null + p.Asn1002Lys C-lobe hypomorph). Research hypothesis only - this
is not clinical advice. Every identifier below was resolved against PubMed on
2026-09-05 (MCP pubmed); DOIs are given as links for every cited work.
Grading: **established / supported / contested / single-study**, plus a human-vs-mouse
flag on every claim. Mouse-only evidence is never silently upgraded to human.

---

## 0. VERDICTS (read this first)

**V1 - Axis dominance ranking by strength of HUMAN data:**
1. **Proteostasis / HSP90–chaperone axis** - *established in human cells* as a
   dependency phenotype; the *selective-kill* pharmacology is established only in
   mouse primary cells and human cancer cell lines.
2. **p53 / mitotic-stopwatch surveillance axis** - *established in human cells*, but
   it is a **brake**, not a vulnerability; it defines what must be lost for tumors to
   arise, and is not directly druggable in a protective direction for this child.
3. **Micronuclei / cGAS-STING–senescence axis** - *established in human cells and
   human tumor cohorts*; bidirectional (tissue damage when chronic, tumor immunity
   when acute) and directly relevant to the MVA progeroid phenotype - but **zero
   MVA-patient-cell data exist** (searched; gap, §6).
4. **Energy / AMPK axis** - *mouse-only* for the selective-kill claim; attenuated in
   human cell lines; relegated from "co-lead" to **fourth**. The AMPK–HSF1 link means
   it is best understood as a member of the proteostasis axis, not an independent axis.

**V2 - KIF18A paradox: RESOLVED - and it cuts AGAINST KIF18A inhibitors for an MVA1 tumor.**
SAC competency is the primary *determinant* of KIF18A-inhibitor sensitivity
(Tabe et al., 2026, *Cancer Res Commun*): SAC-defective cells - with impaired
kinetochore recruitment of **MAD1 and BUBR1**, i.e. precisely the MVA1 lesion  - 
survive KIF18A inhibition. The killing mechanism (unattached kinetochores →
SAC-dependent prolonged mitotic arrest → death) requires a functional checkpoint.
Independently, the dependency is ploidy-conditioned (WGD⁺/CIN-high/TP53-mutant)
and an MVA tumor is mosaic-near-diploid, not WGD⁺ [INFERENCE from MVA cytogenetics
case literature + dependency-landscape papers]. Two strikes; KIF18Ai is
**not a rational late-line option for an MVA1-originated tumor unless the tumor
genome proves WGD + restored SAC**.

**V3 - Autophagy contradiction: RESOLVED at the node level, NOT at the drug level.**
Chloroquine kills a stressed lysosome's **exit step**; rapamycin supports the
**upstream flux**. Both diagrams are true and non-contradictory mechanistically  - 
but you cannot dose both directions in one child. **Decision for the pediatric,
chronic, pre-malignant setting: neither.** Lysosomal blockade at pediatric-safe
doses is under-powered for clone-killing and is itself CIN-promoting (Almacellas
et al., 2020); mTORC1 inhibition is the only chronic-feasible direction
(FDA/EMA-approved in pediatrics for TSC) but its MVA rationale is extrapolation,
not evidence. Both belong to patient-iPSC/organoid validation, not the child.

**V4 - Pediatric-feasible node shortlist (surviving axes):**

| Rank | Node | Drug | Pediatric experience | Grade here |
|---|---|---|---|---|
| 1 | mTORC1 (autophagy-inducing, proteostasis-lifting, rescue direction) | everolimus / sirolimus | **High** - EXIST-1 (age 0–65, SEGA/TSC), EXIST-3 (≥2 y, seizures/TSC) | D-extrapolation for MVA; A for feasibility |
| 2 | Endosomal TLR/STING dampening (chronic cGAS-STING inflammation) | hydroxychloroquine | **High** - chronic use in childhood SLE/JIA documented to >10 y, 4.2±1 mg/kg, no retinopathy observed (Sun et al., 2021) | D - and it imposes the lysosomal-blockade liability (V3) |
| 3 | HSF1 restore / TFEB support | none approved | none | hypothesis only |
| 4 | HSP90 inhibition (clone-kill direction) | 17-AAG / ganetespib class | **None** in pediatrics (verified by search) + HSP90 chaperones SAC kinases (Mps1) → could worsen residual checkpoint | not pediatric-feasible |
| 5 | Senolysis (p16⁺ clearance, progeroid axis) | dasatinib+quercetin / fisetin | none chronic in children; only disease-model-relevant mouse proof (INK-ATTAC in BubR1-hypomorph mice) | C, mouse-only, uniquely genotype-relevant |
| - | KIF18A, Mps1/TTK, TRIP13 | sovilnesib/VLS-1488 etc. | adult-only trials | not feasible here / CONTRA (see V2, sweep) |

---

## 1. Axis ranking in detail (human-data audit per axis)

### 1.1 Proteostasis / HSP90–HSF1 axis - #1, established in human cells

- **Human-cell dependency (established):** Aneuploid human cells are impaired in
  HSP90-mediated folding and depleted of HSF1; restoring HSF1 ameliorates the
  fitness defect (Donnelly et al., 2014, EMBO J |
  [DOI](https://doi.org/10.15252/embj.201488648) | PMID 25205676). Protein-complex
  stoichiometric imbalance → aggregation in aneuploid human cells (Brennan et al.,
  2019, G&D; verified in LITERATURE_SWEEP, s8/c0/m128).
- **Human-cell lysosomal stress (established):** autophagic cargo accumulates in
  lysosomes of aneuploid human cells; TFEB lysosomal-stress response activated  - 
  "a universal feature of the aneuploid state" (Santaguida et al., 2015, G&D |
  [DOI](https://doi.org/10.1101/gad.269118.115) | PMID 26404941).
- **Selective-kill pharmacology (established in mouse; supported in human cancer
  lines):** 17-AAG (±AICAR) selectively antiproliferative to trisomic MEFs and  - 
  with attenuated strength - to human CIN colorectal cancer lines (Tang et al.,
  2011, Cell | [DOI](https://doi.org/10.1016/j.cell.2011.01.017) | PMID 21315436;
  human-line data from the same paper's supplement, per scite excerpts in
  scite.ai tallies).
- **Downgrade reason:** the kill side rests on mouse primary cells + established
  cancer lines; **no human primary (non-transformed) aneuploid kill data**; HSP90
  also chaperones mitotic/checkpoint kinases (Mps1 is an HSP90 client, Woodford
  et al., 2016 - see sweep §2a), so chronic use in a checkpoint-hypomorphic child
  is mechanistically double-edged. **Pediatric feasibility: none found** (no
  pediatric ganetespib/onalespib trial in PubMed as of 2026-09-05).

### 1.2 p53 / mitotic-stopwatch axis - #2, established in human cells, but a brake

- Aneuploidy limits proliferation of human cells via p53 (Thompson & Compton, 2010,
  JCB | [DOI](https://doi.org/10.1083/jcb.200905057) | PMID 20123995 - human cell
  lines, not mouse).
- A 53BP1–USP28 module transmits prolonged mitosis/centrosome loss to p53 arrest
  in normal human cells (Meitinger et al., 2016, JCB |
  [DOI](https://doi.org/10.1083/jcb.201604081) | PMID 27432897); cancer-associated
  USP28 mutations that break this stopwatch are documented (Belal et al., 2025,
  Nat Commun | [DOI](https://doi.org/10.1038/s41467-025-66341-3) | PMID 41365927).
- Missegregation → further instability → arrest + senescence + immunogenic signals
  that recruit immune clearance (Santaguida et al., 2017, Dev Cell |
  [DOI](https://doi.org/10.1016/j.devcel.2017.05.022) | PMID 28633018 - human cells).
- **Implication:** this axis explains the MVA tumor-initiation logic (a
  p53/aneuploidy-tolerant escape clone is the seed), but offers **no pediatric
  druggable node**: you do not want to suppress p53 in any cell, and there is no
  approved "p53-restore" prophylactic. It converts to a **biomarker axis**
  (p53 status + stopwatch genes in surveillance biopsies), not a drug axis.

### 1.3 Micronuclei / cGAS-STING / senescence axis - #3, established in human cells + cohorts

- Micronuclei from missegregation rupture → cGAS recruitment → type-I interferon;
  demonstrated in human cancer cells and mouse autoinflammation model (Mackenzie
  et al., 2017, Nature | [DOI](https://doi.org/10.1038/nature23449) |
  PMID 28738408; Harding et al., 2017, Nature |
  [DOI](https://doi.org/10.1038/nature23470) | PMID 28759889).
- Cytoplasmic chromatin → cGAS-STING drives the senescence-associated secretory
  phenotype in **primary human cells** (Dou et al., 2017, Nature |
  [DOI](https://doi.org/10.1038/nature24050) | PMID 28976970).
- Human-tumor consequence: aneuploid tumors are immunologically colder and less
  immunotherapy-responsive (Davoli et al., 2017, Science |
  [DOI](https://doi.org/10.1126/science.aaf8399) | PMID 28104840 - human cohorts);
  chronic CIN-driven STING promotes metastasis (Bakhoum et al., 2018, Nature |
  [DOI](https://doi.org/10.1038/nature25432) | PMID 29342134).
- **Bidirectional danger (must be stated):** dampening chronic cGAS-STING in
  mosaic tissue (HCQ, JAKi) blunts exactly the immunosurveillance that clears
  arrested missegregated cells (Santaguida 2017, above) and that holds back
  emerging clones. This axis ranks below proteostasis because its direction
  is unresolved *even in principle* for MVA.

### 1.4 Energy / AMPK axis - #4, mouse-only for the kill claim

- AICAR kills trisomic **MEFs** via AMPK→p53 apoptosis; metformin gave a milder
  version of the same; effects in human CRC CIN lines were less dramatic
  (Tang et al., 2011 - supplements, per scite.ai tallies).
- Mechanistic bridge to axis #1 in human cells: metabolic stress via AMPK
  *suppresses* the HSF1 proteotoxic-stress response (Dai et al., 2014, EMBO J |
  [DOI](https://doi.org/10.15252/embj.201489062); human-cell experiments).
- **Verdict:** not an independent axis; grade **mouse-only / contested** for
  pediatric repurposing. Metformin is pediatric-approved (T2DM ≥10 y) but its
  aneuploidy selectivity is untested - a tool-compound story, not a candidate.

---

## 2. KIF18A paradox - evidence and resolution

**Question:** does SAC competence modulate KIF18A-inhibitor sensitivity, and does
it matter for a hypothetical MVA1 tumor?

**Direct evidence (decisive):**
- **Tabe et al., 2026**, SCLC: response to KIF18Ai is determined by **SAC functional
  integrity**, not by CIN metrics, KIF18A expression, or NE subtype. SAC-proficient
  cells → sustained mitotic arrest → apoptosis; **SAC-defective cells survive**.
  Resistant cells show impaired kinetochore recruitment of **MAD1 and BUBR1**.
  Transient MPS1 inhibition (acute CIN induction) partially restores sensitivity.
  (*Cancer Res Commun*, peer-reviewed version of the 2026 preprint previously
  flagged in the sweep | [DOI](https://doi.org/10.1158/2767-9764.CRC-26-0560) |
  PMID 42647139; preprint | [DOI](https://doi.org/10.64898/2026.07.30.741836) |
  PMID 42619900.) - **single-study but mechanistic and directly on-point.**
- **Gliech et al., 2024**, EMBO J: KIF18Ai sensitivity tracks a **SAC:APC/C
  imbalance** - cells with persistent SAC signaling + weak APC/C are sensitive;
  KIF18Ai works by *pushing SAC signaling up and delaying mitosis*. A defective
  SAC removes the weapon ([DOI](https://doi.org/10.1038/s44318-024-00031-6) |
  PMID 38279026).
- **Fonseca/Stumpff et al., 2026 preprint**: in sensitive CIN cells, KIF18Ai
  creates unattached-kinetochore polar chromosomes → **SAC recruitment → prolonged
  arrest** ([DOI](https://doi.org/10.64898/2026.04.15.718686) | PMID 42039568;
  preprint, single-study).
- **Dependency landscape:** WGD⁺ cells are selectively KIF18A-dependent and *more*
  SAC-dependent (Quinton et al., 2021, Nature |
  [DOI](https://doi.org/10.1038/s41586-020-03133-3) | PMID 33505027; erratum
  [DOI](https://doi.org/10.1038/s41586-021-03591-3) | PMID 33976417). Aneuploid
  cancer cells are more dependent on core SAC components *and* selectively
  KIF18A-dependent, while being less acutely sensitive to SAC *inhibitors*  - 
  KIF18A overexpression restores their response to SAC inhibition
  (Cohen-Sharir et al., 2021, Nature |
  [DOI](https://doi.org/10.1038/s41586-020-03114-6) | PMID 33505028).
  Enrichment in TP53-mutant, CCNE1-amplified CIN tumors; sovilnesib/VLS-1488 class
  now in adult phase 1–2 with manageable toxicity, HGSOC activity signaled
  (Payton et al., 2023, Nat Cancer |
  [DOI](https://doi.org/10.1038/s43018-023-00699-5) | PMID 38151625; Phillips
  et al., 2025, Nat Commun VLS-1272 |
  [DOI](https://doi.org/10.1038/s41467-024-55300-z) | PMID 39747049; review:
  Truong et al., 2026 |
  [DOI](https://doi.org/10.1080/13543784.2026.2616752) | PMID 41543111).

**Resolution for MVA1:** the "paradox" was an artifact of conflating two reads of
"SAC." KIF18Ai is lethal *through* the SAC (arrest-dependent death), so
SAC-hypomorphic MVA tumor cells are predicted **resistant** - and "resistance via
impaired kinetochore MAD1/BUBR1 recruitment" in Tabe 2026 is *definitionally* the
BUB1B-loss phenotype. Separately, the WGD/ploidy gate means the compound acts on
CIN-high adult-type tumors, not mosaic near-diploid embryonal tumors
[RMS/Wilms karyotypes in MVA are whole-chromosome mosaic, without reported WGD
selection - INFERENCE from case literature, no tumor-genome dataset exists for MVA].
The one counterpoint available: an MVA tumor *clone* that has restored SAC (e.g.
via second-site TP53 loss is NOT restorative; but acquired BUBR1-dosage or
MAD-pathway changes could be) and undergone WGD would re-enter the dependency
window - a tumor-genome call, not an a-priori one.

**Downstream consequence for the sweep:** the sweep's grade-C KIF18A row stands,
with the "may be less sensitive in SAC-defective contexts" caveat now **upgraded
from preprint to a peer-reviewed, mechanism-resolved finding**. Also adds one
nuance against any ATAC of the checkpoint: Cohen-Sharir 2021 shows aneuploid
cells depend on *residual* SAC - consistent with MVA tumors needing at least the
N1002K hypomorph's remaining activity.

---

## 3. Autophagy contradiction - evidence and resolution

**The two observations:**
1. *Kill direction:* chloroquine (late-autophagy/lysosomal-exit blockade) is
   preferentially antiproliferative against aneuploid cells (Tang et al., 2011 |
   PMID 21315436 - trisomic **MEFs**, mouse; selectivity weaker than 17-AAG/AICAR);
   mechanistically, the lysosomal degradation step is the bottleneck in aneuploid
   **human** cells (Santaguida et al., 2015 | PMID 26404941).
2. *Rescue direction:* raising autophagic flux / proteostasis should support
   survival of mosaic tissues; rapamycin/torin1/mTOR-KD were **not**
   antiproliferative to trisomic MEFs in Tang 2011 (supplement, per
   scite.ai tallies) - i.e. mTOR inhibition was direction-neutral
   for aneuploid cell viability, inconsistent with a kill story and consistent
   with a rescue story. Grade D-extrapolation for MVA.

**Reconciliation (mechanistic, decisive):** the two interventions act on opposite
ends of one pathway - upstream induction (rapalogs) vs downstream exit blockade
(CQ/HCQ). Santaguida 2015 localizes the aneuploid defect to the *exit* step;
Tang's CQ result is the same defect exploited, not a contradiction. Nothing here
is experimentally falsified.

**But the clinical-level reconciliation does NOT license either drug in the child:**
- **CQ/HCQ kill-strategy fails on three grounds.** (i) Dose: the Tang effect sits
  at culture doses with a modest selectivity window (~"preferential", "less
  dramatic than 17-AAG"), i.e. far above what chronic pediatric HCQ
  (4.2±1 mg/kg) delivers systemically. (ii) Self-defeating: lysosomal impairment
  itself delays mitosis and **promotes** chromosomal instability (Almacellas
  et al., 2020, *Autophagy* |
  [DOI](https://doi.org/10.1080/15548627.2020.1764727) | PMID 32573315) - chronic
  administration would manufacture more of the lesion. (iii) It blocks the same
  exit step in euploid bystander cells; no constitutional-mosaicism interception
  data exist.
- **Rescue direction (rapalog) fails only on evidence level, not feasibility:**
  everolimus is approved in pediatrics (EXIST-1, phase 3, age 0–65, TSC/SEGA  - 
  [DOI](https://doi.org/10.1016/s0140-6736(12)61134-9) | PMID 23158522; EXIST-3,
  ≥2 y, TSC seizures - [DOI](https://doi.org/10.1016/s0140-6736(16)31419-2) |
  PMID 27613521), so a chronic pediatric trial is *logistically* possible; but
  the aneuploidy rationale is unsupported extrapolation, and Tang 2011's own
  data say mTORi does nothing to clear aneuploid cells - the benefit would be
  confined to stress relief in euploid/mosaic tissue, with the theoretical risk
  of softening selection against aneuploid clones (sweep Axis-a caveat).
- **Verdict language for the hackathon:** the contradiction is *resolved*  - 
  "chloroquine–kill vs rapamycin–rescue describe one pathway blocked at two
  different nodes, on two different hypothetical objectives (clone interception
  vs tissue support). For a chronic pediatric pre-malignant setting, the
  clone-kill objective is under-powered at safe doses and mechanistically
  counterproductive; the tissue-support objective is feasible but unproven.
  Net: neither direction is justified in-patient today; both are ranked by
  patient-model (iPSC/organoid) interrogation."

---

## 4. Pediatric-feasible druggable nodes per surviving axis (with grading)

| Axis | Node | Agent | Pediatric safety evidence (graded) | MVA rationale grade | Net |
|---|---|---|---|---|---|
| Proteostasis (kill) | HSP90 ATPase | 17-AAG / ganetespib / onalespib | **None found in PubMed** (searched ganetespib + onalespib pediatric, 0 hits) | C-preclinical; Mps1-client hazard | NOT pediatric-feasible |
| Proteostasis (rescue) | mTORC1 | everolimus, sirolimus | **High**: RCT evidence in children incl. infants (EXIST-1/EXIST-3); known AE profile (stomatitis, infections, metabolic) | **D-extrapolation** - no MVA data; Tang 2011 neutral | Feasible, unproven - research-only |
| Proteostasis (rescue) | TFEB activation / lysosomal capacity | none approved | none | hypothesis | NOT feasible |
| p53 / stopwatch | - | none safe in mosaic tissue | n/a | biomarker axis only | NOT a drug axis |
| Micronuclei / cGAS-STING (dampen) | Endosomal TLR/STING | hydroxychloroquine | **Supported**: chronic pediatric use documented, 397/528 children evaluable, median 2.5 y, max 10.6 y, no retinopathy observed (Sun et al., 2021, Zhonghua Er Ke Za Zhi | [DOI](https://doi.org/10.3760/cma.j.cn112140-20200622-00656) | PMID 33548956); decades of JIA/childhood-SLE practice | **D**, + contradicts kill direction, + immunosurveillance caveat (§1.3) |
| Micronuclei / cGAS-STING (dampen) | JAK-STAT | baricitinib / ruxolitinib | Moderate in pediatric interferonopathies | **D**; immunosurveillance hazard in a cancer-predisposition child | NOT feasible as prophylaxis |
| Senescence (p16⁺ clearance) | senolytics | dasatinib+quercetin, fisetin | none chronic in children | **C** - but the only axis with genotype-specific in-vivo proof (INK-ATTAC in BubR1-hypomorph mice delays progeroid pathology: Baker et al., 2011, Nature | [DOI](https://doi.org/10.1038/nature10600) | PMID 22048312; graded mouse-only) | Research priority, not pediatric-feasible yet |
| CIN-tumor treatment | KIF18A | sovilnesib, VLS-1488, AM-1882 | adult-only trials | **D here** (V2: SAC-defective + non-WGD) | NOT a candidate for MVA tumors without tumor-genome qualification |

---

## 5. Mouse–human discordances and honesty notes (required)

1. **Selective aneuploid-cell killing (AICAR/CQ/17-AAG) is mouse-primary.** Human
   CRC CIN lines show attenuated effects; no human primary-cell kill data
   (all from Tang 2011 and its supplements; counts as *established-mouse /
   supported-human*).
2. **Proteotoxic-stress phenotype is human-confirmed** (Donnelly 2014; Santaguida
   2015; Brennan 2019) - the *dependency* is not a mouse artifact, but 2024-era
   work shows proteome diversity tunes aneuploidy tolerance across backgrounds
   (Muenzner/Schukken et al., 2024, Nature; sweep ref #41) → tissue/species
   tolerance is variable; do not assume a fixed kill window.
3. **p53-response and cGAS-STING micronucleus biology are human-confirmed**
   (references §1.2–1.3; primary human cells and human tumor cohorts).
4. **Senolytic benefit is mouse-only**, even though run in the BubR1-hypomorph
   model itself (Baker 2011) - extrapolating drug-flinching
   benefit to the human MVA child is unsupported.
5. The earlier sweep discordance stands and is restated: haploinsufficient-Bub3
   mice show CIN without cancer predisposition (Kalitsis et al., 2005; sweep ref
   #34) vs human MVA cancer predisposition (Hanks et al., 2004, PMID 15475955)  - 
   mouse rescue ↔ human benefit is not guaranteed in either direction.
6. MVA-tumor genome space assumptions (WGD-negative, near-diploid mosaic) are
   **[INFERENCE]** from syndrome cytogenetics and case reports - no sequenced
   MVA tumor series exists; this is also a gap (below).

## 6. Gaps found by this pass

1. **No MVA patients cell/tissue data on ANY stress axis** - senescence markers,
   cGAS-STING/interferon signatures, lysosomal load in MVA fibroblasts or
   patient-derived models: searched (PubMed, "mosaic variegated aneuploidy
   patient cells senescence inflammation interferon" → 0 hits). This is the
   single most decisive missing assay for G3 and is directly addressable with
   proband fibroblasts/iPSC.
2. No pediatric trial data for any HSP90 inhibitor (verified).
3. No sequenced MVA-tumor cohort → V2's WGD/SAC judgment needs tumor exome at
   first tumor event.
4. No direct measurement that MTR-inhibition relieves aneuploid mosaic tissue
   stress in any mammalian germline-CIN model - the rescue direction's key
   absence.

**Termination criterion (declared; met):** each axis carries ≥2 PubMed-verified
primary sources with human-vs-mouse attribution; both named contradictions carry
a mechanistic resolution; the pediatric table cites approval-level or documented
chronic pediatric-use evidence for every "feasible" entry (EXIST-1, EXIST-3,
Sun 2021) and negative verification (no hits) for the "not feasible" entries;
all DOIs/PMIDs resolved via PubMed MCP on 2026-09-05; no scite use (token expired).

---

## References (APA-ish; every entry PubMed-verified 2026-09-05)

- Almacellas, E., et al. (2020). Lysosomal degradation ensures accurate chromosomal segregation to prevent chromosomal instability. *Autophagy*, 17(3). https://doi.org/10.1080/15548627.2020.1764727 | PMID 32573315 - human/mouse cell data.
- Bakhoum, S. F., et al. (2018). Chromosomal instability drives metastasis through a cytosolic DNA response. *Nature*, 553. https://doi.org/10.1038/nature25432 | PMID 29342134 - human cells + models.
- Baker, D. J., et al. (2004). BubR1 insufficiency causes early onset of aging-associated phenotypes and infertility in mice. *Nat Genet*. https://doi.org/10.1038/ng1382 | PMID 15208629 - mouse.
- Baker, D. J., et al. (2011). Clearance of p16Ink4a-positive senescent cells delays ageing-associated disorders. *Nature*, 479. https://doi.org/10.1038/nature10600 | PMID 22048312 - mouse (BubR1-hypomorph background).
- Belal, H., et al. (2025). Cancer-associated USP28 missense mutations disrupt 53BP1 interaction and p53 stabilization. *Nat Commun*, 16. https://doi.org/10.1038/s41467-025-66341-3 | PMID 41365927 - human.
- Cohen-Sharir, Y., et al. (2021). Aneuploidy renders cancer cells vulnerable to mitotic checkpoint inhibition. *Nature*, 590. https://doi.org/10.1038/s41586-020-03114-6 | PMID 33505028 - human cancer cell lines.
- Dai, S., et al. (2015). Suppression of the HSF1-mediated proteotoxic stress response by the metabolic stress sensor AMPK. *EMBO J*, 34. https://doi.org/10.15252/embj.201489062 - human cells.
- Davoli, T., et al. (2017). Tumor aneuploidy correlates with markers of immune evasion and with reduced response to immunotherapy. *Science*, 355. https://doi.org/10.1126/science.aaf8399 | PMID 28104840 - human tumor cohorts.
- Donnelly, N., et al. (2014). HSF1 deficiency and impaired HSP90-dependent protein folding are hallmarks of aneuploid human cells. *EMBO J*, 33. https://doi.org/10.15252/embj.201488648 | PMID 25205676 - human.
- Dou, Z., et al. (2017). Cytoplasmic chromatin triggers inflammation in senescence and cancer. *Nature*, 550. https://doi.org/10.1038/nature24050 | PMID 28976970 - primary human cells + mouse.
- Fonseca, C., et al. (2026). KIF18A maintains kinetochore–microtubule attachments in CIN cells by limiting microtubule polymerization. *bioRxiv* (preprint). https://doi.org/10.64898/2026.04.15.718686 | PMID 42039568 - preprint; single-study.
- Franz, D. N., et al. (2013). Efficacy and safety of everolimus for SEGA associated with tuberous sclerosis (EXIST-1): phase 3 RCT. *Lancet*, 381. https://doi.org/10.1016/s0140-6736(12)61134-9 | PMID 23158522 - pediatric incl. infants.
- French, J. A., et al. (2016). Adjunctive everolimus for treatment-resistant focal seizures in tuberous sclerosis (EXIST-3). *Lancet*, 388. https://doi.org/10.1016/s0140-6736(16)31419-2 | PMID 27613521 - pediatric ≥2 y.
- Gliech, C. R., et al. (2024). Weakened APC/C activity at mitotic exit drives cancer vulnerability to KIF18A inhibition. *EMBO J*, 43. https://doi.org/10.1038/s44318-024-00031-6 | PMID 38279026.
- Hanks, S., et al. (2004). Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. *Nat Genet*, 36. https://doi.org/10.1038/ng1449 | PMID 15475955 - human patients.
- Harding, S. M., et al. (2017). Mitotic progression following DNA damage enables pattern recognition within micronuclei. *Nature*, 548. https://doi.org/10.1038/nature23470 | PMID 28759889 - human tumor cells + mouse.
- Mackenzie, K. J., et al. (2017). cGAS surveillance of micronuclei links genome instability to innate immunity. *Nature*, 548. https://doi.org/10.1038/nature23449 | PMID 28738408 - human cells + mouse model.
- Meitinger, F., et al. (2016). 53BP1 and USP28 mediate p53 activation and G1 arrest after centrosome loss or extended mitotic duration. *J Cell Biol*, 214. https://doi.org/10.1083/jcb.201604081 | PMID 27432897 - human cells.
- Phillips, A. F., et al. (2025). Targeting chromosomally unstable tumors with a selective KIF18A inhibitor (VLS-1272). *Nat Commun*, 16. https://doi.org/10.1038/s41467-024-55300-z | PMID 39747049.
- Payton, M., et al. (2023). Small-molecule inhibition of kinesin KIF18A reveals a mitotic vulnerability enriched in chromosomally unstable cancers. *Nat Cancer*, 5. https://doi.org/10.1038/s43018-023-00699-5 | PMID 38151625 - human cancer cell lines/xenografts.
- Quinton, R. J., et al. (2021). Whole-genome doubling confers unique genetic vulnerabilities on tumour cells. *Nature*, 590. https://doi.org/10.1038/s41586-020-03133-3 | PMID 33505027 (erratum: https://doi.org/10.1038/s41586-021-03591-3 | PMID 33976417).
- Santaguida, S., et al. (2015). Aneuploidy-induced cellular stresses limit autophagic degradation. *Genes Dev*, 29. https://doi.org/10.1101/gad.269118.115 | PMID 26404941 - human + yeast.
- Santaguida, S., et al. (2017). Chromosome mis-segregation generates cell-cycle-arrested cells with complex karyotypes that are eliminated by the immune system. *Dev Cell*, 41. https://doi.org/10.1016/j.devcel.2017.05.022 | PMID 28633018 - human.
- Sun, L., et al. (2021). Application and safety of hydroxychloroquine in chronic disease among children. *Zhonghua Er Ke Za Zhi*, 59(2). https://doi.org/10.3760/cma.j.cn112140-20200622-00656 | PMID 33548956 - pediatric chronic use cohort.
- Tabe, C., et al. (2026). Spindle assembly checkpoint competency determines sensitivity to KIF18A inhibition in small-cell lung cancer. *Cancer Res Commun*. https://doi.org/10.1158/2767-9764.crc-26-0560 | PMID 42647139 (preprint: https://doi.org/10.64898/2026.07.30.741836 | PMID 42619900).
- Tang, Y.-C., et al. (2011). Identification of aneuploidy-selective antiproliferation compounds. *Cell*, 144. https://doi.org/10.1016/j.cell.2011.01.017 | PMID 21315436 - mouse primary + human cancer lines.
- Thompson, S. L., & Compton, D. A. (2010). Proliferation of aneuploid human cells is limited by a p53-dependent mechanism. *J Cell Biol*, 188. https://doi.org/10.1083/jcb.200905057 | PMID 20123995 - human.
- Truong, J. Q., et al. (2026). KIF18A inhibition and its rising role in cancer therapy trials. *Expert Opin Investig Drugs*, 35(1). https://doi.org/10.1080/13543784.2026.2616752 | PMID 41543111 - review (adult trials status).
- Liu, G., et al. (2025). Targeting KIF18A triggers antitumor immunity and enhances PD-1 blockade in CIN colorectal cancer. *Cell Death Discov*, 11. https://doi.org/10.1038/s41420-025-02437-5 | PMID 40175357 - links KIF18Ai to cGAS-STING (single-study).
