# Wave 2 - Q1 NonsenseAxis: UGA readthrough, NMD rule, ASO exon-17 skipping

Proband: BUB1B c.2210T>G (p.Leu737Ter; TTA→TGA, **UGA opal**, verified from MANE
ENST00000287598.11/NM_001211 CDS, 3153 nt = 1050 aa) + p.Asn1002Lys. Disease variable =
BubR1 ABUNDANCE; dose curve ≈13% competent / ≈6% failing (Suijkerbuijk 2010, per
program decision record, full-text-read).

**VERDICT SUMMARY (verdict-first)**

| # | Branch | Verdict | Confidence |
|---|--------|---------|------------|
| a | UGA readthrough pharmacology (ataluren / ELX-02 / aminoglycoside analogs) | **Not competitive as a standalone axis.** Best-case modeled contribution is ≈ +0.3–3% of WT BubR1 - it does not bridge the ~6→13% gap alone. Both lead agents are commercially/regulatorily endangered (ataluren de-authorized EU 2023–24, US NDA withdrawn 2026; ELX-02 cystinosis ph2 terminated, no published pediatric efficacy). UGA codon itself is the most permissive stop class-wide, but the actual context is **UGAA** (sub-optimal +4 position). | High (mechanism + math); Medium (exact % - needs the qPCR gate) |
| b | NMD 50–55-nt rule applied to exon 17 | **NMD-TRIGGERING, no escape route.** Exon 17 is #17 of 23 (not last, not penultimate); the PTC sits 75 nt upstream of the 17|18 junction (> 50–55 nt canonical rule) and 748 nt upstream of the LAST junction, with **6 exon-exon junctions downstream**. Every documented escape category fails. Human MVA BUB1B nonsense transcripts are measured significantly reduced (Matsuura 2006). Readthrough axis is therefore NMD-gated and quantitative: peak effect ≪ 3% without NMD escape data. | High (geometry is exact) |
| c | ASO exon-17 skipping | **Feasible as research direction; dominant nonsense-axis strategy IF the Δ716–761 product works.** Skipping is frame-preserving (141 bp; verified: removes nt 2144–2284 → Δ716–761 plus an E715G junction substitution, kinase domain start 766 untouched) and, crucially, *removes the PTC*, so the transcript **escapes NMD mechanistically** - unlike readthrough, which acts on a degraded mRNA. Even 25–30% skipping of one allele adds ~13–15% of WT total abundance, crossing the competence line arithmetically. Pediatric splice-ASO chemistry precedent is established (eteplirsen … milasen). Two genuine risks: (i) systemic/non-muscle delivery for a constitutional multi-organ disease; (ii) the function/stability of BubR1Δ716-761 is unproven - correction: the attack map's "~690–737" is wrong, real span is 716–761, which sits *between* the retained error-correction module (T620/S670/S676–B56 core, ends ≈716) and the kinase N-lobe (start 766). Direct supporting data: a BubR1 1–730 truncation functions in human SAC replacement assays (Suijkerbuijk 2010). | Medium (assay-gated) |

---

## (a) UGA readthrough pharmacology - realistic % and pediatric reality

**Verified pharmacology.**
- UGA is the most readthrough-permissive stop codon class-wide: statistically significant
  UGA > UAG > UAA hierarchy for both basal and gentamicin-induced readthrough in 66
  mammalian nonsense contexts (Floquet et al. 2012, PLoS Genet; scite s10/c1/m171) and
  genome-wide under aminoglycosides by ribosome profiling (Wangen & Green 2020, eLife;
  scite s17/c4/m274; G418 also stabilized PTC-TP53 mRNA 16-fold - aminoglycosides
  themselves blunt NMD). UGAA-context caveat: Floquet's positional analysis ranks the
  +4 base C > A,G,U - the proband's PTC context is **UGAA** (computed from CDS: `TGAA GTG`),
  i.e., the optimal stop triplet but a second-tier +4 base. Loughran 2014 (NAR; scite
  s26/c2/m292): only exceptional contexts (UGA-CUAG) give high basal readthrough
  (OPRL1 ~31%); `UGAA-GTG` is not such a context; the natural BUB1B stop `TGAG` likewise.
- Human measured effect sizes: gentamicin in nonsense-DMD boys (Malik et al. 2010, Ann
  Neurol; scite s3/c1/m233): after 6 months dystrophin significantly increased (p=0.027)
  but reached 13–15% of normal in only 3/16 stop-codon patients; **pretreatment stable
  transcripts predicted response - direct patient-level evidence that NMD gates
  readthrough efficacy**; and (notably) in-patient readthrough did NOT track stop
  codon/+4 identity as in vitro data predict. Politano 2003 (Acta Myol): only the
  UGA-carrying patients (3/4) showed dystrophin re-expression. Wilschanski 2003 (NEJM;
  scite s0/c2/m342) and Clancy 2001 (AJRCCM; scite s2/c0/m153): gentamicin corrects CFTR
  function in CF stop-mutation patients (incl. children) with small fractional rescue.
- Ataluren: Welch 2007 (Nature; scite s19/c3/m1022) established PTC124 readthrough
  preclinically and argued CF experience suggests "<1%→5% may greatly reduce severity";
  Roy 2016 (PNAS; scite s13/c4/m255) - near-cognate tRNA insertion mechanism (so the
  readthrough product carries a substituted residue at 737, not WT Leu). Clinical:
  phase 2b trend (Bushby/Finkel et al. 2014, Muscle Nerve 50:477; scite s9/c0/m333;
  post-hoc p=0.056), phase 3 ACT DMD negative overall, nominal in one prespecified
  subgroup (McDonald 2017, Lancet; scite s11/c2/m372). CF ph3 negative (Kerem 2014,
  Lancet Respir Med) with nominal benefit only off chronic inhaled antibiotics
  (Kerem 2020, J Cyst Fibros).
- **Regulatory reality (current, load-bearing):** EMA/CHMP recommended non-renewal of
  Translarna 15 Sep 2023 after Study 041 missed its ADP-subgroup endpoint (p=0.36); the
  drug left the EU market (EMA news 2023-09-15, verified full text). FDA: never approved;
  CRL Aug 2025 (PTC 10-K, SEC); **PTC withdrew the US NDA in Feb 2026** (trade press,
  Feb 2026). STRIDE registry: ~5.5-year real-world exposure incl. young children,
  generally tolerated but CHMP judged efficacy data non-confirmatory (Mercuri et al. 2023, J
  Neurol - STRIDE interim, PMID 37115359).
- ELX-02 (eukaryotic-ribosome-selective glycoside): phase 1 safe, no renal/ototoxicity
  signals at 0.3–7.5 mg/kg SC (Leubitz et al. 2019, Clin Pharmacol Drug Dev; scite
  s3/c1/m71); preclinical readthrough with restored full-length protein (CTNS W138X
  model, PLoS One 2019, scite s3/c0/m33; CFTR organoids, de Poel 2022, scite s1/c0/m28).
  ClinicalTrials.gov (verified live, all trials): ph2 nephropathic cystinosis
  **TERMINATED** (NCT04069260), ph2 CF completed (NCT04135495/41 26473), ph2 Alport
  completed (NCT05448755). **No peer-reviewed pediatric efficacy data exist** (gap).
- Designer aminoglycosides gentamicin-X2 (Huang 2018; scite s3/c0/m40) and NB54
  (Nudelman 2009; scite s5/c0/m199) are preclinical only; oto/nephrotoxicity of the class
  is the binding chronic-pediatric constraint (adult/pediatric trial experience with
  gentamicin itself was short-course).

**Modelled abundance arithmetic (INFERENCE - transparent assumptions).**
Normalizing WT total BubR1 = 1.0 (0.5 per allele): N1002K hypomorph at 5–10×
destabilization gives 0.5×(0.1–0.2) ≈ 0.05–0.10; the L737Ter allele gives ~0 if
NMD-complete (Matsuura 2006: "significantly reduced"). Baseline total ≈ 5–10%  - 
consistent with MVA and with sitting between the 6%/13% boundaries.
Readthrough adds 0.5 × f_escape × r, with f_escape = NMD-escape fraction (unknown;
typical escape ≤ 0.1–0.3 for strong NMD substrates, measured escape for BUB1B = GAP #1)
and r = readthrough per translating ribosome (ataluren realistically ≤ 0.05;
gentamicin-class best case ~0.1–0.2). ⇒ contribution ≈ **+0.25% (realistic) to
+3% (optimistic corner)** of WT. Take-home: **even the optimistic corner of
monotherapy readthrough does not move 5–10% across the 13% line.** Combined with
transient NMD inhibition it is synergistic in models (PMID 33396210, scite s0/c1/m38)
but chronic systemic NMD inhibition is not a pediatrically viable strategy
(LITERATURE_SWEEP consensus retained).

## (b) NMD-escape prediction for the exon-17 PTC - exact geometry (all computed, MANE)

ENST00000287598.11 (23 exons; chr15 + strand; verified live via Ensembl REST 2026-09-05):
- PTC (codon 737) lies in **exon 17 of 23** (ENSE00001029409, chr15:40,209,635–40,209,775,
  141 bp, 141 % 3 = 0), i.e., NOT the last exon and NOT even the penultimate:
  **6 exon-exon junctions lie downstream** (17|18 … 22|23).
- Distance PTC → nearest downstream junction (17|18): **75 nt** (>50–55; canonical rule
  of Nagy & Maquat 1998, TIBS; scite s39/c2/m949 - a termination codon >50–55 nt 5' of an
  exon-exon junction is decay-targeting). PTC → LAST junction: **748 nt**.
- Lindeboom et al. 2016 (Nat Genet; scite s31/c2/m600) data-driven escape categories  - 
  PTC in last exon; PTC <50 nt from the last EJC; PTC in first ~150 nt; PTC in a very
  long exon - **none applies**. Long-exon mechanism also fails: downstream exons are
  short (101–560 bp). Prediction: **efficient NMD; transcript residual small.**
- Human evidence (patient, not animal): Matsuura et al. 2006 (Am J Med Genet A;
  7 MVA/PCS families): BUB1B 1833delT and splice-mutant transcripts "significantly
  reduced, probably due to nonsense-mediated mRNA decay"; modest total BubR1 decrease  - 
  direct evidence that human MVA nonsense BUB1B alleles are NMD-degraded. Hanks et al.
  2004 (Nat Genet; scite s8/c0/m58): truncating BUB1B alleles in MVA families behave as
  nulls. Suijkerbuijk 2010 (Cancer Res; scite s9/c0/m132, full-text-read in G1):
  no truncated protein product detectable.
- Gating assay (unchanged from attack map, now sharper): allele-specific qPCR/ddPCR of
  the L737Ter transcript in patient cells = measured f_escape. This number now has a
  precise interpretation: every 10 points of escape ≈ 5% of WT allele output available
  to any readthrough drug. **No readthrough drug-inference stands before this number.**

## (c) ASO exon-17 skipping - feasibility verdict

**Mechanics (corrected coordinates - the attack map's "Δ690–737" is superseded).**
Skipping exon 17 (141 bp, chr15:40,209,635–40,209,775) deletes CDS nt 2144–2284 and
ligates codons 715 and 762. Exon-boundary phase geometry: deletion removes residues
**716–761** and converts the fusion codon GAA→GGT (**E715G**). Frame preserved
(141 = 47×3 exactly). PTC eliminated → **transcript escapes NMD by mechanism, not by
statistical escape** - the decisive asymmetry versus branch (a). Arithmetic
(INFERENCE): restored output from allele A ≈ 0.5 × s (s = skipping fraction);
s ≥ 0.25–0.30 lifts total from 5–10% to ≥ 13% → **competence threshold crossed with
modest skipping efficiency**, and without dependence on f_escape.

**What the deleted region is (functional-risk audit, corrected).**
- Deleted 716–761 lies between two verified functional landmarks: the error-correction
  module (Cdk1 site T620 → Plk1 docking → Plk1 site S676, Elowe et al. 2007, Genes Dev;
  scite s25/c4/m411; Cdk1 site S670, attachment-sensitive, Huang et al. 2008, JCB 183:667)
  and the kinase N-lobe (start ~766; crystal-validated in this program).
- The PP2A-B56–binding motif centers on hydrophobic residues flanking S670
  (Kruse et al. 2013, J Cell Sci; scite s35/c1/m311) - i.e., **retained** in Δ716-761;
  the commonly cited KARD span ends at ≈716, so the deletion clips at most its extreme
  C-terminal residue [INFERENCE - KARD boundary definitions vary by 1–2 residues across
  papers; the LxxIxE core at ~664–678 is definitely retained].
- No mapped catalytic/structural element occupies 716–761 in current literature
  (verified absence in Kruse, Elowe, Huang 2008, Overlack 2015 (eLife; scite s20/c1/m223),
  Suijkerbuijk 2012 Dev Cell 22/23). **No evidence located** for function of this exact
  segment - the deletion product's fold, stability, Cdc20-kinetic behavior, and any
  unmapped regulatory sites (716–761 carries candidate phosphosites in phosphoproteomics
  databases - unverified) are all unknowns → **durability assay gate, as flagged.**
- Mitigating datum: Suijkerbuijk et al. 2010 showed a BubR1 **1–730 truncation** (LAP-731X,
  missing 731→1050 entirely) restores checkpoint, alignment and segregation in human
  replacement assays - residues 731–761 are dispensable for core SAC function *in that
  construct* [INFERENCE for Δ716-761 internal deletion: supportive, not decisive;
  internal deletions can misfold where terminal truncations do not].

**Chemistry & clinical precedent (pediatric, constitutional use).**
- Approved splice-switching PMOs in children: eteplirsen exon 51
  (Charleston et al. 2018, Neurology; scite s2/c1/m183 - 100% treated patients showed the
  skipped junction; significant but ≤~1%-of-normal dystrophin restoration), viltolarsen
  exon 53 (Clemens et al. 2020, JAMA Neurol; scite s7/c0/m214 - mean 5.7% (3.2–10.3) and
  5.9% (1.1–14.4) of normal after 20–24 wk in boys 4–9y), golodirsen (Frank et al. 2020,
  Neurology; scite s3/c0/m252 - mean 1.019% wk 48) - weekly IV, chronic, pediatric,
  well tolerated.
- Non-muscle constitutional pediatric splice-ASO precedent: nusinersen (2'MOE-PS,
  intrathecal; Finkel et al. 2017 ENDEAR, NEJM; scite s51/c7/m2123) and the n-of-1
  milasen (Kim et al. 2019, NEJM; scite s4/c0/m645 - patient-customized splice-modulating
  ASO designed and dosed in a child within one year, no serious AEs) - establishes
  regulatory feasibility of bespoke splice-ASO in children, the model an MVA ASO would
  follow.
- **The binding constraint is delivery, not chemistry** (Roberts et al. 2020, Nat Rev
  Drug Discov; scite s5/c1/m2010): bare PMO distributes to liver/kidney/spleen/bone
  marrow with weekly IV but achieves best indices in muscle and negligible CNS exposure;
  MVA is a constitutional, multi-organ syndrome with CNS involvement (microcephaly)  - 
  no non-muscle exon-skipping drug is approved; exon-skipping efficiency in non-muscle
  peripheral tissues of patients is essentially unvalidated (gap). Realistic delivery
  hybrid: systemic PMO/PPMO for hematopoietic/peripheral division compartments ±
  intrathecal 2'MOE for CNS [INFERENCE - none of this validated in any CIN syndrome].
- Immunogenicity/quality flags carried from sweep: readthrough/skipped products can
  carry neo-junction (E715G) or substituted (737 near-cognate) residues; Malik 2010
  observed anti-dystrophin T-cell responses post-readthrough - monitor.

## Assay gates this wave adds/sharpens (all in-consent per attack map)
1. Allele-specific ddPCR of L737Ter transcript (f_escape) - gates branch (a) entirely.
2. Western of readthrough product if f_escape ≥ 10% and a drug challenge is entertained.
3. **Δ716-761 construct panel** (adds to map's assay list): express BubR1Δ716-761+E715G
   in the Suijkerbuijk-2010 replacement system; readouts: abundance/stability
   (pulse-chase ± proteasome block), kinetochore localization, Cdc20/Mad2 binding,
   nocodazole-arrest kinetics, error-correction probe (cold-stable MT assay) - because
   catalysis is dispensable but the *scaffold* readout is the whole game.
4. PP2A-B56 co-IP + phospho-S670/S676 antibodies on the skipped product (retention
   prediction check).

## Gaps (explicit)
- Measured NMD-escape fraction of L737Ter: **unmeasured** - decision-critical for (a).
- No readthrough experiment has ever been run on a BUB1B nonsense allele (searched
  PubMed 2026-09-05: no evidence located).
- ELX-02: no peer-reviewed phase-2 efficacy publication; cystinosis ph2 terminated;
  no pediatric data.
- Exon-skipping efficiency of any ASO chemistry in non-muscle human tissues in vivo:
  no evidence located.
- Function/stability of BubR1Δ716-761 and the exact C-terminal KARD boundary
  (±1–2 residues disagreed across Kruse/Suijkerbuijk papers): unresolved; assay #3.
- Any mapped modification/element in 716–761: no evidence located (negative finding,
  not proof of absence).
- Ataluren availability channel post-withdrawal (expanded access? non-EU markets?):
  unresolved - regulatory/Legal question, not literature.

## Methodology disclosure
All PMIDs verified via NCBI E-utilities on 2026-09-05; several memory-candidate PMIDs
were wrong and were corrected through esearch before inclusion. scite tallies pulled
live 2026-09-05 (refreshed token at `~/.config/scite/token`; the `~/.scite_token` copy
is expired) via scite.ai tallies; no editorial notices on any
cited record. Transcript geometry computed live from Ensembl REST (ENST00000287598.11,
GRCh38). Regulatory status from EMA news page (full text read), PTC SEC 10-K, and
ClinicalTrials.gov API (live). Full texts read: Floquet 2012 (PMC3315467), Wangen &
Green 2020 (PMC7089771), EMA decision, Overlack 2015. INFERENCE labels preserved per
claim; human vs preclinical flagged in-line. Several plausible-but-unverified PMIDs
from the prior sweep (e.g., "Lindeboom 2019") were replaced by correctly identified
papers (Lindeboom 2016, PMID 27618451).

## References (APA, DOI links; scite tallies s=supporting/c=contrasting/m=mentioning)
1. Bushby, K., Finkel, R., Wong, B., et al. (2014). Ataluren treatment of patients with nonsense mutation dystrophinopathy. *Muscle & Nerve, 50*(4), 477–487. https://doi.org/10.1002/mus.24332 | PMID 25042182 | s9/c0/m333 | human ph2b
2. McDonald, C. M., et al. (2017). Ataluren in patients with nonsense mutation Duchenne muscular dystrophy (ACT DMD): a phase 3 trial. *The Lancet, 390*, 1489–1498. https://doi.org/10.1016/S0140-6736(17)31611-2 | PMID 28728956 | s11/c2/m372 | human ph3
3. Welch, E. M., et al. (2007). PTC124 targets genetic disorders caused by nonsense mutations. *Nature, 447*, 87–91. https://doi.org/10.1038/nature05756 | PMID 17450125 | s19/c3/m1022 | preclinical + rationale
4. Roy, B., et al. (2016). Ataluren stimulates ribosomal selection of near-cognate tRNAs to promote nonsense suppression. *PNAS, 113*(44). https://doi.org/10.1073/pnas.1605336113 | PMID 27702906 | s13/c4/m255 | mechanism
5. Malik, V., et al. (2010). Gentamicin-induced readthrough of stop codons in Duchenne muscular dystrophy. *Annals of Neurology, 67*(6), 771–780. https://doi.org/10.1002/ana.22024 | PMID 20517938 | s3/c1/m233 | human trial (pediatric cohort included)
6. Politano, L., et al. (2003). Gentamicin administration in Duchenne patients with premature stop codon. *Acta Myologica, 22*, 15–21. | PMID 12966700 (no DOI) | human trial
7. Wilschanski, M., et al. (2003). Gentamicin-induced correction of CFTR function in patients with cystic fibrosis and CFTR stop mutations. *NEJM, 349*, 1433–1441. https://doi.org/10.1056/NEJMoa022170 | PMID 14534336 | s0/c2/m342 | human trial
8. Clancy, J. P., et al. (2001). Evidence that systemic gentamicin suppresses premature stop mutations in patients with cystic fibrosis. *Am J Respir Crit Care Med, 163*, 1683–1692. https://doi.org/10.1164/ajrccm.163.7.2004001 | PMID 11401894 | s2/c0/m153 | human trial
9. Floquet, C., et al. (2012). Statistical analysis of readthrough levels for nonsense mutations in mammalian cells reveals a major determinant of response to gentamicin. *PLoS Genetics, 8*(3), e1002608. https://doi.org/10.1371/journal.pgen.1002608 | PMID 22479203 | s10/c1/m171 | human-cell data (full text read)
10. Wangen, J. R., & Green, R. (2020). Stop codon context influences genome-wide stimulation of termination codon readthrough by aminoglycosides. *eLife, 9*, e52611. https://doi.org/10.7554/eLife.52611 | PMID 31971508 | s17/c4/m274 | human-cell
11. Loughran, G., et al. (2014). Evidence of efficient stop codon readthrough in four mammalian genes. *Nucleic Acids Research, 42*(14), 8928–8938. https://doi.org/10.1093/nar/gku608 | PMID 25013167 | s26/c2/m292 | human-cell
12. Kerem, E., et al. (2014). Ataluren for the treatment of nonsense-mutation cystic fibrosis: a randomised, double-blind, placebo-controlled phase 3 trial. *The Lancet Respiratory Medicine, 2*(7), 539–547. | PMID 24836205 | human ph3 (negative)
13. Leubitz, A., et al. (2019). Safety, tolerability, and pharmacokinetics of single ascending doses of ELX-02. *Clinical Pharmacology in Drug Development, 8*(8), 984–994. https://doi.org/10.1002/cpdd.647 | PMID 30650260 | s3/c1/m71 | human ph1
14. (Eloxx/preclinical) (2019). The novel aminoglycoside ELX-02 permits CTNS^W138X translational read-through and restores cystinosin function. *PLoS One, 14*(12), e0223954. https://doi.org/10.1371/journal.pone.0223954 | PMID 31800572 | s3/c0/m33 | preclinical
15. de Poel, E., et al. (2022). Functional restoration of CFTR nonsense mutations in intestinal organoids. *Journal of Cystic Fibrosis, 21*(3), 436–442. https://doi.org/10.1016/j.jcf.2021.09.020 | PMID 34666947 | s1/c0/m28 | preclinical (patient organoids)
16. Huang, G., et al. (2018). The minor gentamicin complex component X2 is a potent premature stop codon readthrough molecule. *PLoS One, 13*(10), e0206158. https://doi.org/10.1371/journal.pone.0206158 | PMID 30359426 | s3/c0/m40 | preclinical
17. Nudelman, I., et al. (2009). Development of novel aminoglycoside (NB54) with reduced toxicity and enhanced suppression of disease-causing premature stop mutations. *J Med Chem, 52*(9), 2836–2845. https://doi.org/10.1021/jm801640k | PMID 19309154 | s5/c0/m199 | preclinical
18. Nagy, E., & Maquat, L. E. (1998). A rule for termination-codon position within intron-containing genes: when nonsense affects RNA abundance. *TIBS, 23*(6), 198–199. https://doi.org/10.1016/S0968-0004(98)01208-0 | PMID 9644970 | s39/c2/m949 | canonical rule
19. Lindeboom, R. G. H., et al. (2016). The rules and impact of nonsense-mediated mRNA decay in human cancers. *Nature Genetics, 48*, 1112–1118. https://doi.org/10.1038/ng.3664 | PMID 27618451 | s31/c2/m600 | human tumor transcriptomes
20. Matsuura, S., et al. (2006). Monoallelic BUB1B mutations and defective mitotic-spindle checkpoint in seven families with premature chromatid separation (PCS) syndrome. *Am J Med Genet A, 140*(4), 358–367. https://doi.org/10.1002/ajmg.a.31003 | PMID 16411201 | s0/c0/m0 (scite) | human patients, NMD evidence
21. Hanks, S., et al. (2004). Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. *Nature Genetics, 36*, 1159–1161. https://doi.org/10.1038/ng1427 | PMID 15475955 | s8/c0/m58 | human patients
22. Suijkerbuijk, S. J. E., van Osch, M. H. J., et al. (2010). Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy. *Cancer Research, 70*(12), 4891–4900. https://doi.org/10.1158/0008-5472.CAN-09-4319 | PMID 20516114 | s9/c0/m132 | human patient cells + replacement
23. Elowe, S., et al. (2007). Tension-sensitive Plk1 phosphorylation on BubR1 regulates the stability of kinetochore microtubule interactions. *Genes & Development, 21*, 2205–2219. https://doi.org/10.1101/gad.436007 | PMID 17785528 | s25/c4/m411 | human cells
24. Huang, H., et al. (2008). Phosphorylation sites in BubR1 that regulate kinetochore attachment, tension, and mitotic exit. *J Cell Biology, 183*(4), 667–680. https://doi.org/10.1083/jcb.200805163 | PMID 19015317 | human cells
25. Kruse, T., et al. (2013). Direct binding between BubR1 and B56-PP2A phosphatase complexes regulate mitotic progression. *J Cell Science, 126*, 1086–1092. https://doi.org/10.1242/jcs.122481 | PMID 23345399 | s35/c1/m311 | human cells
26. Overlack, K., et al. (2015). A molecular basis for the differential roles of Bub1 and BubR1 in the spindle assembly checkpoint. *eLife, 4*, e05269. https://doi.org/10.7554/eLife.05269 | PMID 25611342 | s20/c1/m223 | human cells (full text read)
27. Suijkerbuijk, S. J. E., Vleugel, M., et al. (2012). Integration of kinase and phosphatase activities by BUBR1 ensures formation of stable kinetochore-microtubule attachments. *Developmental Cell, 23*(4), 745–755. https://doi.org/10.1016/j.devcel.2012.09.005 | PMID 23079597 | s37/c5/m442 | human cells
28. Charleston, J. S., et al. (2018). Eteplirsen treatment for Duchenne muscular dystrophy: exon skipping and dystrophin production. *Neurology, 90*(24), e2146–e2154. https://doi.org/10.1212/WNL.0000000000005680 | PMID 29752304 | s2/c1/m183 | human pediatric
29. Clemens, P. R., et al. (2020). Safety, tolerability, and efficacy of viltolarsen in boys with Duchenne muscular dystrophy amenable to exon 53 skipping: phase 2 trial. *JAMA Neurology, 77*(8), 982–991. https://doi.org/10.1001/jamaneurol.2020.1264 | PMID 32453377 | s7/c0/m214 | human pediatric (4–9 y)
30. Frank, D. E., et al. (2020). Increased dystrophin production with golodirsen in patients with Duchenne muscular dystrophy. *Neurology, 94*(21), e2270–e2282. https://doi.org/10.1212/WNL.0000000000009233 | PMID 32139505 | s3/c0/m252 | human pediatric
31. Finkel, R. S., et al. (2017). Nusinersen versus sham control in infantile-onset spinal muscular atrophy (ENDEAR). *NEJM, 377*, 1723–1732. https://doi.org/10.1056/NEJMoa1702752 | PMID 29091570 | s51/c7/m2123 | human pediatric RCT
32. Kim, J., et al. (2019). Patient-customized oligonucleotide therapy for a rare genetic disease (milasen). *NEJM, 381*, 1644–1652. https://doi.org/10.1056/NEJMoa1813279 | PMID 31597037 | s4/c0/m645 | human pediatric n-of-1
33. Roberts, T. C., et al. (2020). Advances in oligonucleotide drug delivery. *Nature Reviews Drug Discovery, 19*, 673–694. https://doi.org/10.1038/s41573-020-0075-7 | PMID 32782413 | s5/c1/m2010 | review, human
34. (STRIDE registry) (2023). Safety and effectiveness of ataluren in patients with nonsense mutation DMD in the STRIDE registry… *Journal of Neurology, 270*. | PMID 37115359 | real-world pediatric
35. EMA (2023-09-15). *EMA recommends non-renewal of authorisation of Duchenne muscular dystrophy medicine Translarna.* https://www.ema.europa.eu/en/news/ema-recommends-non-renewal-authorisation-duchenne-muscular-dystrophy-medicine-translarna | regulatory
36. PTC Therapeutics Form 10-K, FY2025 (SEC): FDA CRL August 2025 for ataluren NDA; withdrawal announced February 2026. https://www.sec.gov/Archives/edgar/data/1070081/000110465926017575/tmb-20251231x10k.htm | regulatory
37. ClinicalTrials.gov: NCT04069260 (ELX-02 cystinosis ph2, terminated), NCT04135495/NCT04126473 (CF ph2, completed), NCT05448755 (Alport ph2, completed). https://clinicaltrials.gov | registry
38. (NMD-readthrough synergy) (2021). *Int J Mol Sci, 22*(1), 344. https://doi.org/10.3390/ijms22010344 | PMID 33396210 | s0/c1/m38 | preclinical (mouse)
39. Welch-context basal suppression claim cross-checked: Finkel-phase2a open-label ataluren: https://doi.org/10.1371/journal.pone.0081302 | PMID 24349052 | s8/c0/m162 | human ph2a
