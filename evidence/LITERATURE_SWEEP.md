# Track 2 Literature Evidence Package - BUB1B / MVA1 Drug-Repurposing Hypotheses

**Scope.** Hypothesis-generation for the MVA Hackathon 2026 drug-repurposing track.
NOT clinical advice. Every candidate below is a research hypothesis requiring
preclinical validation before any clinical consideration.

**Proband genotype (given).** MVA1 (OMIM #257300), compound heterozygous BUB1B,
GRCh38, MANE ENST00000287598.11 / NM_001211:
- Allele 1: chr15:40209701 T>G - c.2210T>G, **p.Leu737Ter** (nonsense; T>TG on a
  Leu codon ⇒ **UGA (opal) stop** on the transcript; NMD-expected null)
- Allele 2: chr15:40220612 T>G - **p.Asn1002Lys** (missense, C-terminal kinase
  domain; novel/unclassified in ClinVar)
- Phenotype: rhabdomyosarcoma, nephrocalcinosis, short stature, FTT, muscle
  atrophy, prematurity, severe IUGR/SGA; child.

**Method / provenance.** Smart Citations pulled from scite MCP
(api.scite.ai/mcp, `search_literature`) on
2026-09-04 before token expiry; DOI→PMID resolution checked against NCBI
PubMed (E-utilities + PubMed MCP); paperclip full-text search used as
corroboration for the TRIP13 and surveillance sub-questions. Grades combine
scite Smart Citation tallies (s = supporting / c = contrasting / m = mentioning
citations *received by that paper*) with study type:

| Grade | Meaning |
|---|---|
| A | Established; heavily cited as supporting (s ≥ 10, c ≤ 3) or directly demonstrated in patients/replicated models |
| B | Solid single-team or convergent evidence (s 1–9), or preclinical with replication |
| C | Preclinical/animal/in-vitro only, indirect for this indication |
| D | Extrapolation/speculative; no direct evidence for this context |
| CONTRA | Evidence contraindicates use in this genotype |

Editorial notices: no core-cited paper is retracted. Corrections/errata noted
where present (Santaguida & Amon 2015 review; Wang et al. 2020 DCZ0415;
Izumi/JCI 2019 allelic-effects paper).

---

## Chapter 1 - Mechanism (evidence-graded)

### 1.1 BUB1B biallelic mutations cause MVA1 with cancer predisposition - **Grade A**
Biallelic truncating + missense BUB1B mutations cause mosaic variegated
aneuploidy with childhood cancer (Wilms tumor, **embryonal rhabdomyosarcoma**,
leukemia) (Hanks et al., 2004; scite s10/c3/m507). Follow-up reports confirm a
high malignancy risk (≥25–50% in early series; Limwongse et al., 2002,
PMID 11932988 / 12567425) and genotype heterogeneity (monoallelic BUB1B →
milder premature-chromatid-separation phenotype without the full MVA syndrome:
Hanks et al., 2006, s6/c0/m170). Genetically heterogeneous syndrome: MVA2 =
CEP57 (Snape et al., 2011, s4/c0/m138), MVA-TRIP13 = biallelic TRIP13 with
Wilms predisposition (Yost et al., 2017, s6/c0/m154). Homozygous BUB1B
mutation also confers GI-cancer susceptibility in non-MVA families (de Voer et
al., 2010 NEJM, s1/c0/m54).

### 1.2 BubR1 = core spindle-assembly-checkpoint (SAC) effector - **Grade A**
BubR1 (with Bub3) binds Cdc20 and, synergistically with Mad2, inhibits
APC/C^Cdc20 - the mitotic checkpoint complex (Tang et al., 2002, s23/c0/m251;
Sudakin/Malureanu 2001, s29/c2/m437). BubR1's N-terminus alone is a soluble
APC/C^Cdc20 inhibitor (Malureanu et al., 2009, s27/c2/m257). Aurora B recruits
BubR1/Mad2/CENP-E to unattached kinetochores (Ditchfield et al., 2003,
s131/c7/m1411).

### 1.3 BubR1 kinase vs scaffold functions - **Grade A (with nuance)**
- The N-terminal/scaffold+MAD2-interaction module carries the SAC signal; the
  **C-terminal kinase activity is largely dispensable for the arrest itself**
  but is required for stable kinetochore–microtubule attachment and timely
  error correction (Malureanu et al., 2009, s27/c2/m257).
- BUBR1 integrates kinase and phosphatase (PP2A-B56 recruitment) at
  kinetochores; this tension-sensing module stabilizes correct attachments
  (Suijkerbuijk et al., 2012, s37/c5/m441). The kinase domain in this
  scaffold-centric view behaves partly pseudokinase-like (single preprint,
  ungraded: bioRxiv 733378).
- **Genotype interpretation [INFERENCE]:** p.Asn1002Lys sits in the kinase
  C-lobe (human BubR1 kinase domain ≈ aa 784–1050 of 1050). A hypomorphic
  kinase-domain missense would be expected to impair attachment
  error-correction and potentially protein stability even if SAC inhibition
  per se is retained - consistent with a null + hypomorphism dosage model.
  No functional data exist for this specific variant (see Gaps).

### 1.4 Why null + hypomorphic missense gives MVA1 - **Grade B**
- Complete loss is not tolerated: near-complete BubR1 deletion causes severe
  congenital microcephaly via shortened mitosis and massive cell death
  (Yang et al., 2019 HMG, s4/c0/m22); Drosophila BubR1 is essential
  (Basu et al. lineage; see raw dumps). Residual activity from the second
  allele determines survivability - the classic MVA1 dosage model
  (Hanks et al., 2009 review, PMID 19297405).
- **Allelic effects drive phenotypic heterogeneity** in a BubR1 MVA mouse
  allelic series (Sieben/Jeganathan et al., JCI 2019, s0/c0/m13; has erratum):
  the specific missense present matters quantitatively.
- Graded BubR1 reduction in MEFs → graded aneuploidy + senescence
  (Baker et al., 2004, s45/c2/m850).

### 1.5 Aneuploidy → proteotoxic/energetic stress → cancer-predisposition chain - **Grade A**
1. Mis-segregation in a p53-competent cell triggers p53/p21-dependent G1
   arrest/senescence (Thompson & Compton, 2010, s42/c3/m477) - proliferative
   brake that tumors must escape; loss of this brake is a tumor-initiating
   permissive step.
2. Aneuploidy causes proteotoxic stress (yeast: Oromendia et al., 2012,
   s19/c0/m382; human cells: HSF1 deficiency + impaired HSP90-dependent folding
   are *hallmarks* of aneuploid human cells, Donnelly et al., 2014,
   s6/c0/m138) and stoichiometric protein-complex imbalance/aggregation
   (Brennan et al., 2019 G&D, s8/c0/m128).
3. Aneuploidy-induced stress **limits autophagic degradation**; lysosomes
   overload, TFEB lysosomal stress response activates (Santaguida et al.,
   2015/2017 G&D, s20/c0/m182).
4. Recent: proteostasis failure + mitochondrial dysfunction feed back to drive
   further CIN (Scassetta et al., 2026 Nat Commun, too new to grade; s0/c0/m1)
   and natural proteome diversity modulates aneuploidy tolerance via protein
   turnover (Muenzner/Schukken et al., 2024 Nature, s2/c0/m39).
5. Cumulative: chronic CIN tissues with defective SAC + stress-limited
   proteostasis select for p53-loss clones → early pediatric tumors
   (rhabdomyosarcoma/Wilms) (Santaguida & Amon, 2015 review, s21/c0/m515 with
   errata; Hanks 2004).

### 1.6 Contradictions / tensions found (imported into Chapter 3)
- Bub3 haploinsufficient mice: CIN **without** cancer predisposition
  (Kalitsis et al., 2005, s1/c2/m45) - SAC heterozygosity alone is not
  sufficient for tumors in mice; implies additional human MVA modifiers.
- BubR1 **over**expression is protective constitutionally (Baker et al., 2013,
  s11/c1/m245; Weaver et al., 2016, s0/c1/m13 - note the contrasting citation)
  yet BUBR1 is frequently overexpressed in established cancers where it marks
  progression (Grabsch/Shi et al., 2010, s1/c1/m53). Context dependence
  (constitutional vs oncogenic setting) must be stated in the write-up.

---

## Chapter 2 - Repurposing candidate axes (evidence-graded)

### Axis (a) Exploit aneuploidy/CIN vulnerabilities - proteostasis & energy stress
The canonical preclinical finding: **AICAR (energy-stress/AMPK), 17-AAG (HSP90
inhibition) and chloroquine (autophagy inhibition) are selectively
antiproliferative against aneuploid cells** (Tang et al., 2011, s24/c3/m378;
AICAR + 17-AAG synergize). Donnelly et al. (2014, s6/c0/m138) mechanistically
pin the HSP90 dependence on impaired chaperoning in aneuploid human cells.

- **HSP90 inhibitors (17-AAG/ganetespib class).** Grade B-preclinical.
  Rationale: kill emerging aneuploid tumor-initiating clones. Caveats: no
  evidence in constitutional mosaicism; HSP90 also buffers normal cells and
  chaperones checkpoint kinases (e.g., Mps1; Woodford et al., 2016,
  s1/c0/m87) - long-term prophylactic use could plausibly worsen checkpoint
  function. *Use case more defensible as interception of established
  CIN lesions than as prophylaxis.* 17-AAG is not approved; gantespib failed
  late trials in other indications.
- **AICAR / AMPK activation.** Grade C. Tool compound; no approved pediatric
  formulation; metformin overlaps mechanistically but aneuploid selectivity of
  metformin is untested.
- **Chloroquine/HCQ (autophagy inhibition).** Grade C. Approved drug, cheap;
  exploits aneuploid lysosomal bottleneck (with Santaguida 2015 mechanistic
  support, s20). **Direct conflict** with the mTOR/autophagy-induction idea
  below - opposite directions on the same pathway; flag both.
- **mTORC1 inhibition (rapamycin/everolimus).** Grade D-extrapolation here
  (approved in pediatrics for TSC; strong proteostasis-lifting, autophagy-
  inducing rationale for *normal* aneuploid mosaic tissues, cf. Santaguida;
  no aneuploidy-selectivity data in Tang 2011 - the study tested killing of
  aneuploid cells, not protection of them). Potential dual-edged: may relieve
  proteotoxic stress in non-malignant tissues but could reduce the selective
  pressure against aneuploid clones.

### Axis (b) SAC-adjacent interventions - mostly **contraindicated**
- **Direct SAC inhibition (Mps1/TTK inhibitors, e.g., BAY1217389, CFI-402257)
  in this patient: CONTRA.** Complete SAC loss is lethal and drives catastrophic
  aneuploidy (Mad2-null embryonic lethal; Dobles et al., 2000, PMID 10892650).
  The oncology rationale (push tumors over a lethal CIN threshold;
  Sansregret et al., 2017, s10/c0/m106) applies to treating established tumors,
  not to a checkpoint-hypomorphic child - it would accelerate exactly the
  pathology being prevented.
- **TRIP13 inhibition (DCZ0415): CONTRA for this genotype; useful only as tool
  evidence.** DCZ0415 suppresses multiple myeloma (Wang et al., 2020,
  s3/c0/m83; 2025 correction on record) and colorectal EMT/metastasis
  (Agarwal et al., 2022, s3/c0/m46). But TRIP13 is the SAC-silencing AAA-ATPase:
  biallelic TRIP13 LoF itself causes chromosome missegregation + Wilms-tumor
  predisposition (Yost et al., 2017, s6/c0/m154). Inhibiting TRIP13 in an
  already SAC-defective MVA1 child would prolong/derange checkpoint signaling
  and plausibly worsen segregation errors.
- **KIF18A inhibitors** exploit CIN in established tumors (Quinton/Marquis et
  al., 2023 Nat Cancer, s4/c1/m52; Payton et al., 2022 J Med Chem, s5/c0/m32;
  phase 1–2 agents). Relevant only to *treatment of a developed CIN tumor*,
  not prevention - and one 2026 preprint warns SAC-defective contexts may be
  *less* KIF18A-sensitive (biorxiv 2026.07.30.741836). Grade C.

### Axis (c) Cancer interception / surveillance in CIN syndromes
- No drug has demonstrated cancer-risk reduction in MVA (checked; see Gaps).
  Current practice = surveillance (renal ultrasound for Wilms, clinical RMS
  monitoring) and standard oncologic treatment of arising tumors (Lin et al.,
  2020 long-term follow-up case; s0/c0/m4; RMS-with-PCS/MVA case example:
  Watanabe et al., 2019, PMID 31184400).
- HSC-relevant precedent: one published HSCT in MVA1 for marrow failure
  context (Bacalhau et al., 2019 Orphanet J Rare Dis, s0/c0/m3) - shows
  feasibility of replacing a proliferative compartment but is a single case.
- Aspirin/CRC-prevention literature (Bibbins-Domingo USPSTF, 2022, s5/c1/m126)
  does not extend to pediatric embryonal tumors - not a candidate.
- Realistic interceptive drug hypotheses live in Axis (a) (HSP90i/CQ as
  CIN-clone interception) - unvalidated in this setting (Grade C/D).

### Axis (d) NMD / nonsense-readthrough for p.Leu737Ter - **rationale strong on paper, evidence thin**
- The allele makes a **UGA (opal) stop** at codon 737 (c.2210T>G on TTG).
  UGA is the most readthrough-responsive stop context for both ataluren and
  aminoglycoside-class agents [established class knowledge; context verified
  from the variant notation; treat codon-level claim as INFERENCE pending
  transcript sequencing].
- **Ataluren (Translarna).** EU-conditionally approved for nmDMD. Phase 3
  ACT DMD missed its primary endpoint overall; pre-specified subgroup
  (decline ≥9 months baseline subgroup e.g. age 7–16) showed benefit
  (McDonald et al., 2017 Lancet, s11/c2/m370 - note the 2 contrasting
  citations; phase 2a trial: s8/c0/m162, DOI 10.1371/journal.pone.0081302).
  Class efficacy across diseases is contested.
- **ELX-02** (non-aminoglycoside-antibiotic eukaryotic ribosome-selective
  glycoside): functional restoration of CFTR nonsense mutations in intestinal
  organoids (de Poel/Crawley et al., 2022 J Cyst Fibros, s1/c0/m28); phase 2
  in Alport syndrome. Designer aminoglycosides with reduced ototoxicity
  (NB54: Nudelman et al., 2009, s5/c0/m199; gentamicin-X2 component highly
  readthrough-active: Huang et al., 2018, s3/c0/m40).
- **Critical mechanistic caveat - NMD.** A nonsense allele only matters for
  readthrough if transcript survives NMD. NMD is variable across
  tissues/alleles (single-cell measurement of NMD variability, Nat Commun 2021, s3/c0/m98) and Hanks 2004-class MVA1 truncating alleles are
  generally NMD-degraded (absent BUBR1 protein from those alleles). Combining
  readthrough with **transient** NMD inhibition is synergistic preclinically
  in CF models (s0/c1/m38, PMID 33396210; neuronal PTC rescue with NMD
  inhibition, s0/c1/m10, 2023). Chronic systemic NMD inhibition is not a
  viable pediatric chronic strategy.
- **Second caveat - product quality:** readthrough inserts a near-cognate
  amino acid at position 737 producing full-length BubR1 with a substituted
  residue; neither the identity of the inserted residue nor the fraction of
  functional protein is known without an organoid/iPSC experiment.
  Overall axis grade: **C for the drug class at the right stop context;
  D for BUB1B specifically.**

### Axis (e) BUB1B-specific rescue
- No BUB1B-targeted small-molecule stabilizer/corrector exists in the
  literature (searched: "BUB1B hypomorphic mutation protein stability rescue"
  - zero direct hits). **Gap, not a candidate.**
- Genetic proof-of-concept that raising BubR1 dosage is beneficial:
  BubR1 overexpression protects against aneuploidy, cancer and extends
  healthspan in mice (Baker et al., 2013, s11/c1/m245); reinforced mitotic
  surveillance opposes aneuploidy/cancer (Weaver et al., 2016 eLife,
  s0/c1/m13). BubR1 activity is post-translationally tuned (acetylation:
  BRCA2 reinforces BubR1 acetylation, Choi et al., 2012, s8/c0/m99;
  deacetylation by SIRT2) - a **speculative** pharmacological handle
  (SIRT2 inhibition / acetylation stabilization of hypomorphic BubR1), no
  literature support yet: Grade D-hypothesis.

---

## Chapter 3 - Gaps & uncertainties (honest limitations)

1. **p.Asn1002Lys has zero functional data** (novel). Residual kinase activity,
  stability, PP2A/kinetochore interactions unknown; needs iPSC/organoid or
  recombinant assay before allele-specific claims.
2. **NMD status of p.Leu737Ter unmeasured** (allele-specific RNA needed).
  Readthrough axis (d) is un-attackable without this.
3. **No BUB1B-specific pharmacological rescue** exists or is reported anywhere
  (no stabilizers, correctors, or activators).
4. **No drug has shown cancer-risk reduction in any CIN syndrome cohort**;
  all interception ideas are extrapolated from cell/yeast/mouse aneuploidy
  biology. MVA cohorts are far too small for chemoprevention trials.
5. **Mosaicism is developmentally baked-in** by treatment age: existing
  aneuploid cells cannot be re-euploidized; drugs can only suppress new
  errors (irrelevant once mitotic rate falls postnatally in most tissues) or
  suppress/neutralize aneuploid clones. Expected effect size on the
  constitutional phenotype (IUGR-derived short stature, established mosaicism)
  is likely small or zero.
6. **Mouse–human discordance** on SAC-haploinsufficiency tumor outcomes
  (Kalitsis Bub3 finding) means mouse rescue may not predict human benefit.
7. **Opposing-direction interference**: autophagy inhibition (HCQ, kill
  aneuploid clones) vs autophagy induction (rapalogs, support normal tissues)
  cannot both be right for this patient; tissue-specific experiments
  needed. (Generally: kill-the-clone vs rescue-the-tissue tension pervades
  every Axis-(a) candidate.)
8. **Pediatric chronic-dosing safety** of every Axis-(a)/(d) agent in a
  growth-retarded child is unstudied (aminoglycoside oto/nephrotoxicity even
  for redesigned scaffolds; ataluren long-term oncologic unknowns in a
  cancer-prone child).
9. **KIF18A sensitivity may require checkpoint competency** (2026 preprint)  - 
  the most CIN-exploiting drug class could paradoxically underperform in
  SAC-defective tumors.
10. **scite Smart Citation tallies are direction-of-citation signals, not
    effect replication**; several low-count papers (case reports) carry no
    statistical weight. Full-text verification was limited to abstracts +
    snippets + paperclip summaries due to session scope.

---

## Cited works (APA; DOI link; PMID; scite tally where pulled)

According to PubMed verification and scite Smart Citations (raw JSON in
scite.ai):

1. Hanks, S., Coleman, K., Reid, S., et al. (2004). Constitutional aneuploidy
   and cancer predisposition caused by biallelic mutations in BUB1B. *Nature
   Genetics*, 36(11), 1159–1161. https://doi.org/10.1038/ng1449 | PMID 15475955 | s10/c3/m507
2. Baker, D. J., Jeganathan, K. B., Cameron, J. D., et al. (2004). BubR1
   insufficiency causes early onset of aging-associated phenotypes and
   infertility in mice. *Nature Genetics*, 36(7), 744–749.
   https://doi.org/10.1038/ng1382 | PMID 15208629 | s45/c2/m850
3. Tang, Z., Bharadwaj, R., Li, B., & Yu, H. (2002). Checkpoint protein BubR1
   acts synergistically with Mad2 to inhibit APC. *Mol Biol Cell*.
   https://doi.org/10.1091/mbc.01-09-0437 | s23/c0/m251
4. Sudakin, V., Chan, G. K. T., & Yen, T. J. (2001). Mad2-independent
   inhibition of APC/Cdc20 by the mitotic checkpoint protein BubR1. *Dev Cell*.
   https://doi.org/10.1016/s1534-5807(01)00019-3 | s29/c2/m437
5. Malureanu, L. A., Jeganathan, K. B., Hamada, M., et al. (2009). BubR1 N
   terminus acts as a soluble inhibitor of cyclin B degradation by APC/CCdc20
   in interphase. *Developmental Cell*. https://doi.org/10.1016/j.devcel.2008.11.004
   | PMID 19154723 | s27/c2/m257
6. Suijkerbuijk, S. J. E., et al. (2012). Integration of kinase and
   phosphatase activities by BUBR1 ensures formation of stable kinetochore–
   microtubule attachments. *Developmental Cell*.
   https://doi.org/10.1016/j.devcel.2012.09.005 | PMID 23079597 | s37/c5/m441
7. Ditchfield, C., et al. (2003). Aurora B couples chromosome alignment with
   anaphase by targeting BubR1, Mad2, and Cenp-E. *J Cell Biol*.
   https://doi.org/10.1083/jcb.200208091 | PMID 12719470 | s131/c7/m1411
8. Thompson, S. L., & Compton, D. A. (2010). Proliferation of aneuploid human
   cells is limited by a p53-dependent mechanism. *J Cell Biol*.
   https://doi.org/10.1083/jcb.200905057 | PMID 20123995 | s42/c3/m477
9. Oromendia, A. B., Dodgson, S. E., & Amon, A. (2012). Aneuploidy causes
   proteotoxic stress in yeast. *Genes & Development*.
   https://doi.org/10.1101/gad.207407.112 | PMID 23222101 | s19/c0/m382
10. Donnelly, N., et al. (2014). HSF1 deficiency and impaired HSP90-dependent
    protein folding are hallmarks of aneuploid human cells. *EMBO J*.
    https://doi.org/10.15252/embj.201488648 | PMID 25205676 | s6/c0/m138
11. Santaguida, S., Vasile, E., White, E., & Amon, A. (2015). Aneuploidy-
    induced cellular stresses limit autophagic degradation. *Genes & Dev*.
    https://doi.org/10.1101/gad.269118.115 | PMID 26404941 | s20/c0/m182
12. Tang, Y.-C., Williams, B. R., Siegel, J. J., & Amon, A. (2011).
    Identification of aneuploidy-selective antiproliferation compounds.
    *Cell*, 144(4), 499–512. https://doi.org/10.1016/j.cell.2011.01.017
    | PMID 21315436 | s24/c3/m378
13. Baker, D. J., et al. (2013). Increased expression of BubR1 protects
    against aneuploidy and cancer and extends healthy lifespan. *Nat Cell
    Biol*. https://doi.org/10.1038/ncb2643 | PMID 23242215 | s11/c1/m245
14. Weaver, R. L., et al. (2016). BubR1 alterations that reinforce mitotic
    surveillance act against aneuploidy and cancer. *eLife*.
    https://doi.org/10.7554/elife.16620 | PMID 27528194 | s0/c1/m13
15. Yost, S., de Wolf, B., Hanks, S., et al. (2017). Biallelic TRIP13 mutations
    predispose to Wilms tumor and chromosome missegregation. *Nature Genetics*.
    https://doi.org/10.1038/ng.3883 | PMID 28553959 | s6/c0/m154
16. Wang, W., et al. (2020). A small-molecule inhibitor targeting TRIP13
    suppresses multiple myeloma progression. *Cancer Research*.
    https://doi.org/10.1158/0008-5472.can-18-3987 | PMID 31732653 | s3/c0/m83
    (correction: https://doi.org/10.1158/0008-5472.can-25-2758)
17. Agarwal, S., et al. (2022). DCZ0415, a small-molecule inhibitor targeting
    TRIP13, inhibits EMT and metastasis. *Mol Oncol*.
    https://doi.org/10.1002/1878-0261.13201 | PMID 35194944 | s3/c0/m46
18. McDonald, C. M., et al. (2017). Ataluren in patients with nonsense
    mutation Duchenne muscular dystrophy (ACT DMD). *The Lancet*.
    https://doi.org/10.1016/s0140-6736(17)31611-2 | PMID 28728956 | s11/c2/m370
19. Phase 2a ataluren nmDMD study (2013). https://doi.org/10.1371/journal.pone.0081302 | PMID 24349052 | s8/c0/m162
20. de Poel / colleagues (2022). Functional restoration of CFTR nonsense
    mutations (ELX-02) in intestinal organoids. *J Cyst Fibros*.
    https://doi.org/10.1016/j.jcf.2021.09.020 | PMID 34666947 | s1/c0/m28
21. Nudelman, I., et al. (2009). Novel aminoglycoside NB54 with reduced
    toxicity and enhanced suppression. *J Med Chem*.
    https://doi.org/10.1021/jm801640k | PMID 19309154 | s5/c0/m199
22. Huang, G., et al. (2018). Gentamicin X2, a potent premature stop codon
    readthrough molecule. *PLoS ONE*. https://doi.org/10.1371/journal.pone.0206158
    | PMID 30359426 | s3/c0/m40
23. (2021). Combining readthrough with NMD inhibition - synergy in murine CF
    model. *IJMS*. https://doi.org/10.3390/ijms22010344 | PMID 33396210 | s0/c1/m38
24. (2021). Cellular variability of nonsense-mediated mRNA decay. *Nat
    Commun*. https://doi.org/10.1038/s41467-021-27423-0 | PMID 34893608 | s3/c0/m98
25. Snape, K., et al. (2011). Mutations in CEP57 cause mosaic variegated
    aneuploidy syndrome. *Nat Genet*. https://doi.org/10.1038/ng.822 | PMID 21552266 | s4/c0/m138
26. de Voer, R. M., et al. (2010). Homozygous BUB1B mutation and susceptibility
    to gastrointestinal cancer. *NEJM*. https://doi.org/10.1056/nejmoa1006565
    | PMID 21190457 | s1/c0/m54
27. Sansregret, L., et al. (2017). APC/C dysfunction limits excessive cancer
    chromosomal instability. *Cancer Discovery*.
    https://doi.org/10.1158/2159-8290.cd-16-0645 | PMID 28069571 | s10/c0/m106
28. Quinton/Marquis et al. (2023). Small-molecule inhibition of kinesin KIF18A
    reveals a mitotic vulnerability enriched in chromosomally unstable
    cancers. *Nat Cancer*. https://doi.org/10.1038/s43018-023-00699-5 | PMID 38151625 | s4/c1/m52
29. Payton, M., et al. (2022). Targeting the mitotic kinesin KIF18A in
    chromosomally unstable cancers. *J Med Chem*.
    https://doi.org/10.1021/acs.jmedchem.1c02030 | PMID 35286090 | s5/c0/m32
30. Yang, Z. J., et al. (2019). Nearly complete deletion of BubR1 causes
    microcephaly through shortened mitosis and massive cell death. *Hum Mol
    Genet*. https://doi.org/10.1093/hmg/ddz022 | PMID 30668728 | s4/0/m22
31. Sieben, C. J. / Jeganathan, K. B., et al. (2019). BubR1 allelic effects
    drive phenotypic heterogeneity in MVA progeria syndrome. *J Clin Invest*.
    https://doi.org/10.1172/jci126863 | PMID 31738183 | s0/c0/m13 (erratum: 10.1172/jci144781)
32. Limwongse, C., et al. (2002). High risk of malignancy in mosaic variegated
    aneuploidy syndrome. *Am J Med Genet*. https://doi.org/10.1002/ajmg.10281
    | PMID 11932988
33. Hanks, S., et al. (2006). Monoallelic BUB1B mutations and defective
    mitotic-spindle checkpoint in seven families with PCS. *Am J Med Genet A*.
    https://doi.org/10.1002/ajmg.a.31069 | PMID 16411201 | s6/c0/m170
34. Kalitsis, P., et al. (2005). Increased chromosome instability but not
    cancer predisposition in haploinsufficient Bub3 mice. *Genes Chromosomes
    Cancer*. https://doi.org/10.1002/gcc.20215 | PMID 15898111 | s1/c2/m45
35. Dobles, M., et al. (2000). Chromosome missegregation and apoptosis in mice
    lacking Mad2. *Cell*. https://doi.org/10.1016/s0092-8674(00)80875-2
    | PMID 10892650
36. Santaguida, S., & Amon, A. (2015). Short- and long-term effects of
    chromosome mis-segregation and aneuploidy. *Nat Rev Mol Cell Biol*.
    https://doi.org/10.1038/nrm4025 | PMID 26204159 | s21/c0/m515 (errata noted)
37. Lin, S., Luk, H.-M., & Lo, I. F. M. (2020). Prenatal diagnosis and
    long-term follow-up of a Chinese patient with MVA. *Clin Case Rep*.
    https://doi.org/10.1002/ccr3.2802 | PMID 32884756 | s0/c0/m4
38. Bacalhau / colleagues (2019). Hematopoietic stem cell transplantation in a
    patient with type 1 MVA syndrome. *Orphanet J Rare Dis*.
    https://doi.org/10.1186/s13023-019-1073-x | PMID 31053147 | s0/c0/m3
39. Choi, E., et al. (2012). BRCA2 fine-tunes the spindle assembly checkpoint
    through reinforcement of BubR1 acetylation. *Dev Cell*.
    https://doi.org/10.1016/j.devcel.2012.01.009 | PMID 22340495 | s8/c0/m99
40. Scassetta / colleagues (2026). Proteostasis failure and mitochondrial
    dysfunction contribute to CIN-induced pathologies. *Nat Commun*.
    https://doi.org/10.1038/s41467-026-70521-0 | PMID 41820377 | s0/c0/m1 (new)
41. Muenzner/Schukken et al. (2024). Natural proteome diversity links
    aneuploidy tolerance to protein turnover. *Nature*.
    https://doi.org/10.1038/s41586-024-07442-9 | PMID 38778096 | s2/c0/m39
42. Tao, Y., et al. (2017). TRIP13 impairs mitotic checkpoint surveillance in
    multiple myeloma. (paperclip/PMC5432292 corroboration)
43. Watanabe / colleagues (2019). Rhabdomyosarcoma with PCS–MVA syndrome:
    reducing late recurrence. *Pediatr Int*. https://doi.org/10.1111/ped.13849
    | PMID 31184400 | s0/c0/m1
44. USPSTF (2022). Aspirin use to prevent cardiovascular disease and
    colorectal cancer. *JAMA*. https://doi.org/10.1001/jama.2022.3337 | s5/c1/m126
    (cited only to exclude Axis-c applicability)
45. Aziz, K., Sieben, C. J., et al. (2018). MVA-syndrome mutation or
    haploinsufficiency in Cep57 impairs tumor suppression (mouse MVA model,
    paperclip corroboration). *J Clin Invest*. https://doi.org/10.1172/jci120316
    | s2/c0/m34

scite.ai tallies were pulled live for every query in this memo; all DOIs resolve via
pubmed.ncbi.nlm.nih.gov.
