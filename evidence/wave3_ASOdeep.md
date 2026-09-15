# Wave 3 - Q7 ASOdeep: sequence feasibility of BUB1B exon-17 skipping, constitutional delivery census, and deliverability/IP

Proband: BUB1B p.Leu737Ter (c.2210T>G, exon 17/23) + p.Asn1002Lys. Disease variable = BubR1
ABUNDANCE (~13 % competent / ~6 % failing). Primary candidate from wave 1: ASO-mediated
exon-17 skipping. **Termination criterion (declared): stop when the delivery-census table
is complete AND each of sub-questions (a)/(c) reaches a stated verdict.** Both met; verdicts below.

**VERDICT SUMMARY (verdict-first)**

| # | Sub-question | Verdict | Confidence |
|---|--------------|---------|------------|
| a | Sequence-level feasibility of exon-17 skipping | **SEQUENCE-GREEN.** Exon 17 is a clean skip substrate: frame-preserving (141 bp), PTC-removing, enhancer-rich / silencer-free motif architecture statistically indistinguishable from successfully-skipped DMD exons (eteplirsen/casimersen class), strong native splice junctions, and **zero cryptic donor/acceptor candidates above MaxEnt thresholds inside the exon**. ESE-dense landing pad for ASO placement identified at the exon's 3′ third. Junction codon E715G verified. | High on computed facts; Medium on the inference that motif comparability predicts skipping success |
| b | Constitutional (whole-body) delivery census | **DELIVERY IS THE RATE-LIMITER, AS WAVE 1 HELD - NOW QUANTIFIED.** Approved splice-switching chemistry reaches: CNS only if intrathecal (nusinersen/milasen); skeletal muscle at weekly systemic PMO but at ~1 %-of-normal product levels (eteplirsen); liver via systemic 2′MOE-PS (mipomersen/inotersen/volanesorsen) and hepatocyte-only GalNAc (inclisiran/givosiran). **No approved splice-switching drug demonstrates efficacy in a non-muscle, non-CNS somatic tissue in humans.** Bone marrow/gut epithelium reach at PMO dosing is plausible from animal biodistribution but **unvalidated in humans** - remains the binding gap for a constitutional-CIN indication. | High (this is a negative-space finding; the affirmative entries are trial- and label-verified) |
| c | Deliverability / IP / funding | **DELIVERABLE THROUGH THE n-of-1 CHANNEL.** The foundational PMO chemistry patent estate is expired; milasen proved a bespoke splice-ASO IND is achievable in <12 months with a 3-month single-species rodent tox package plus in-vitro data (now codified in three FDA guidances); n-Lorem industrializes this at ~USD 1 M per patient-for-life with >30 INDs granted, ~58 % acceptance, and ~9 % of its accepted patients requiring splicing ASOs - i.e., the exact class this candidate belongs to. IP risk is process/know-how and economics, not composition-of-matter. | High for process/funding facts; Medium for FTO (patent-landscape sketch, not a legal opinion) |

**Bottom line for the submission frame:** exon-17 skipping passes the *sequence* gate cleanly;
the deliverable claim is "**druggable in principle today via the n-of-1 ASO channel**"; what
stays flagged is (i) Δ716-761+E715G product function (assay #4 of the attack map - unchanged,
still decisive), (ii) non-muscle/CNS tissue reach, and (iii) chronic pay-forability.

---

## (a) Sequence-level feasibility of exon-17 skipping in BUB1B

All coordinates GRCh38, MANE ENST00000287598.11 (Ensembl REST, live fetch 2026-09-05). Raw
sequences + full numeric output: `q7a_sequence_analysis.md` in this directory.

### Target geometry (verified, consistent with wave 1–2)
- Exon 17 = ENSE00001029409, chr15:40,209,635–40,209,775 (+ strand), 141 bp, 141 = 47×3 exactly.
- PTC c.2210 sits at exon offset 67 (TTA codon at offsets 66–68 → TGA); 75 nt upstream of the
  17|18 junction; 6 downstream EJCs (NMD-triggering per wave 2).
- Skipping ligates codon 715 (GAA) to codon 762, producing fusion codon **GGT = E715G**
  (verified against the CDS sequence directly in this wave), deleting residues 716–761;
  kinase N-lobe start ~766 untouched.
- Flanking introns are short: intron 16 ≈ 865 bp, intron 17 = 335 bp (favorable for ASO
  synthesis target space and reduces cryptic splice surface relative to DMD-class megaintrons).

### ESE/ESS motif density vs successfully skipped exons
Comparator set: DMD exons 45 (casimersen), 51 (eteplirsen), 53 (viltolarsen/golodirsen) - the
three exon classes with FDA-approved skipping drugs - plus BUB1B exons 16 and 18 as same-gene
context. Motif resources: RESCUE-ESE 238 hexamers (Fairbrother 2004; list recovered from the
Burge-lab server via Internet Archive), PESE/PESS octamers and full 65,536-octamer z-score
table (Zhang & Chasin 2004; recovered from the Chasin-lab mirror via Internet Archive).

| Exon | len | RESCUE-ESE/kb | PESE/kb | PESS/kb | mean octamer z | GC % |
|---|---|---|---|---|---|---|
| **BUB1B ex17** | 141 | **113.5** | **70.9** | **0.0** | **+0.603** | 43.3 |
| BUB1B ex16 | 134 | 141.8 | 74.6 | 22.4 | +0.521 | 45.5 |
| BUB1B ex18 | 101 | 128.7 | 89.1 | 9.9 | −0.059 | 35.6 |
| DMD ex45 | 176 | 153.4 | 11.4 | 5.7 | +0.546 | 46.0 |
| DMD ex51 | 233 | 107.3 | 85.8 | 17.2 | +0.662 | 46.4 |
| DMD ex53 | 212 | 268.9 | 99.1 | 18.9 | +0.859 | 43.9 |

Read-out: exon 17 sits squarely inside the DMD comparator envelope on every axis  - 
RESCUE-ESE density within ±10 % of exon 51 (the eteplirsen target), PESE density second only
to exons 53/18 among comparators, positive mean octamer balance (enhancer-dominated), and
**zero PESS silencer octamers** (the only silencer-free exon in the set). Nothing in the motif
architecture predicts silencer-driven resistance to skipping. (*INFERENCE: these densities are
correlates of skippability, not validated predictors of ASO efficacy; human empirical skipping
remains to be demonstrated in patient cells.*)

### Native junction strength (MaxEntScan: score5 of the 9-mer donor; score3 of the 23-mer acceptor)

| Exon | Donor (9-mer) | score5 | Acceptor (23-mer) | score3 |
|---|---|---|---|---|
| **BUB1B ex17** | TAG**GT**AAGT | **9.66** | CCTTTCCCTCCCACTGGCAG**AG**AAA | **9.29** |
| DMD ex45 | GAG**GT**AGGG | 7.81 | …CAGGAA | 11.32 |
| DMD ex51 | AAG**GT**ATGA | 9.11 | …TTTAGCTC | 3.73 |
| DMD ex53 | AAG**GT**TAGT | 8.54 | …CTAGTTG | 8.55 |

Interpretation: BUB1B exon 17 has **strong junctions at both ends** - analogous to DMD exon 51's
strong donor but *unlike* exon 51's famously weak acceptor (3.73), which is part of why that
exon skips readily. A strong bilateral junction pair means the skip ASO will likely need to
cover both ESEs and/or junctions, and that partial skipping (not 100 %) is the realistic
pharmacodynamic ceiling - consistent with the attack map's arithmetic, which needs only
s ≈ 0.25–0.30 to cross the 13 % competence line.

### Cryptic splice-site risk scan (exon 17 ± 2 kb, 4,141-nt window; MaxEntScan)
- Candidate donors (score5 ≥ 5.0): 14 sites (3.4/kb). **None inside exon 17 other than the
  native donor.** Three intronic sites score ≥ native: intron 16, −135 (10.67) and −867 (9.79);
  exon 17's native donor is 9.66.
- Candidate acceptors (score3 ≥ 4.0): 33 sites (8.0/kb). **None inside exon 17 other than the
  native acceptor.** One intronic site exceeds native: intron 17, +879 (10.02); two more are
  near-native (+455: 8.99; +704: 8.83), all downstream.
- This is a *benign* profile: no exon-internal backup sites that could produce partial-deletion
  transcripts; strong intronic candidates exist (as in any multi-kb window) and are the correct
  QC targets for post-ASO RNA-seq in patient cells. (*INFERENCE: MaxEntScan scores do not model
  branch-point usage, RNA structure, or context co-operativity - cryptic *activation* risk under
  ASO treatment is formally unresolved and is an assay item, not a literature answer.*)

### ASO landing pad
A RESCUE-ESE cluster concentrates at the exon's 3′ third: hexamer hits at offsets 91–93 and a
dense cluster at 112–126; the top 30-mer window (offsets ~108–138, adjacent to the donor) holds
**9 RESCUE-ESE hexamers** - the natural placement zone for an eteplirsen-class steric ASO
(mirroring how eteplirsen itself targets an exonic enhancer cluster, and how milasen's designers
placed ASOs on mapped ESEs using the same RESCUE-ESE resource, Kim 2019). A second minor cluster
sits at offsets 46–48. (*INFERENCE as design aid; not an ASO design commitment.*)

**Sub-verdict (a):** nothing at sequence level blocks exon-17 skipping; architecture is
comparable to the three exons with approved skipping drugs; the residual sequence risks
(strong bilateral junctions demanding efficient ASOs; intronic cryptic sites to monitor) are
assay-addressable. The product-function question (Δ716-761+E715G, incl. the KARD-boundary
caution F2) is untouched by this analysis and remains the go/no-go assay.

---

## (b) Constitutional-target delivery census - what reaches which tissue, honestly

BUB1B deficiency is constitutional; the therapeutically relevant compartments are mitotic:
bone marrow, gut epithelium, liver, kidney, gonads, and CNS (microcephaly). The census below
lays out every marketed or clinically-proven oligonucleotide delivery mode against that map.

| Modality (lead drugs) | Route | Demonstrated target tissue in humans | Reach for a constitutional target | Key evidence (all identifiers verified 2026-09-05) |
|---|---|---|---|---|
| PMO, systemic (eteplirsen 30 mg/kg/wk IV; viltolarsen; golodirsen) | Weekly IV, chronic, pediatric | Skeletal muscle - 100 % of treated patients show skipped transcript; product restoration ~1 % of normal | Kidney/liver/marrow exposure high in animal biodistribution; **clinical efficacy demonstrated only in muscle**; cardiac rescue unproven in humans; CNS essentially none (does not cross BBB) | Charleston 2018 (PMID 29752304, s2/c1/m183); Roberts 2020 (PMID 32782413, s5/c1/m2010); animal PK: Amantana & Iversen 2005 (PMID 16087398, s1/c0/m119), Amantana 2007 (PMID 17583927, s12/c0/m172); Sazani 2002 (PMID 12426578, s10/c0/m297) - mouse systemic multi-tissue upregulation |
| 2′MOE-PS, systemic SC (mipomersen, inotersen, volanesorsen) | Weekly SC | Liver (apolipoprotein programs); peripheral nerve via liver-derived TTR reduction | Broad parenchymal distribution driven by PS content (kidney cortex, liver, spleen, marrow); **but these are RNase-H/knockdown drugs - no splice-switching member approved for a non-hepatic systemic target**; class flags: thrombocytopenia (volanesorsen), glomerulonephritis (inotersen/volanesorsen), injection reactions; mipomersen Kynamro NDA 203568 marketing status "Discontinued" (Drugs@FDA, verified) | Raal 2010 (PMID 20227758, s8/c2/m575); Benson 2018 (PMID 29972757, s20/c2/m1336); Witztum 2019 (PMID 31390500, s9/c1/m396); PK review Geary 2015 (PMID 25666165, s38/c2/m811) |
| 2′MOE-PS, intrathecal (nusinersen; milasen n-of-1) | IT bolus, quarterly maintenance | CNS (spinal cord >> brain ~3:1 distribution) | CNS only; systemic exposure negligible. Milasen: 22-mer PS/2′MOE, same chemistry class as nusinersen, 18-g GMP batch, rat-only tox, dosed within 1 year - the template for any CNS leg of a BUB1B ASO | Finkel 2017 (PMID 29091570, s51/c7/m2123); Kim 2019 (PMID 31597037, s4/c0/m645) |
| GalNAc–siRNA / GalNAc–ASO (inclisiran, givosiran) | SC, infrequent maintenance | **Hepatocytes only** (ASGPR-targeted); deep, durable hepatic silencing | Zero help for marrow/gut/CNS; irrelevant to BUB1B unless liver-confined | Ray 2020 inclisiran (PMID 32187462, s33/c0/m1104); Balwani 2020 givosiran (PMID 32521132, s9/c1/m572) |
| LNP (patisiran) | IV, q3wk | Liver (hATTR TTR); small-molecule-era organ restriction persists | Not demonstrated for steric splice-switching ASOs; LNP-PMO/2′MOE splice delivery remains preclinical **[INFERENCE]** | Adams 2018 (PMID 29972753, s45/c0/m2415) |
| PPMO (peptide-PMO; Pip6 class; Sarepta peptide-conjugates) | IV | - (no approval) | In mdx mouse, PPMO markedly improves **cardiac** and diaphragm exon skipping vs bare PMO - the only chemistry with demonstrated heart reach; renal-toxicity signals in the class are the brake | Betts 2012 (PMID 23344180, s5/c0/m235) - preclinical (mouse), human cardiac efficacy **no evidence located** |

**Tissue-reach honesty table (what a constitutuional child actually gets at eteplirsen-class dosing):**
- Skeletal muscle: yes (the entire DMD franchise).
- Kidney cortex / liver / spleen / bone marrow: high exposure in animal PK (Amantana 2005,
  Sazani 2002); human functional splice-switching in these tissues **no evidence located**
  (wave-2 gap, re-confirmed this wave).
- Heart: poor with bare PMO; improved only preclinically with PPMO (Betts 2012).
- CNS: no with systemic PMO/2′MOE; yes with IT 2′MOE (nusinersen/milasen).
- Gut epithelium: **no evidence located** for any approved ASO chemistry.

**Sub-verdict (b):** a realistic MVA regimen is a hybrid - weekly systemic PMO (or PPMO if
renal safety allows) for peripheral mitotic compartments plus IT 2′MOE for the neurodevelopmental
leg - with the explicit flags that human non-muscle splice-switching is unproven, gut/marrow
efficacy is a bet on animal biodistribution, and no chemistry in the census reaches everything.

---

## (c) Deliverability / IP / FTO sketch (submission-usable paragraph)

*Chemistry IP.* The foundational morpholino composition patents are expired: US 5,185,444
(Summerton & Weller; priority 1985-03-15; granted 1993-02-09; legal status "**Expired  - 
Lifetime**", anticipated expiry 2010-02-09; current assignee Sarepta - Google Patents/USPTO,
verified 2026-09-05). Generic PMO research-grade synthesis is commercially routine (the DMD
PMOs are now themselves off-patent chemistry), while later conjugate/process claims (PPMO
peptides, stereopure/backbone-chiral variants, and Ionis-patterned 2′MOE claims) remain
active - so the lowest-risk n-of-1 design space is plain PMO or plain 2′MOE-PS, exactly the
two chemistries with pediatric precedent. *[INFERENCE - this is a landscape sketch from public
patent registers, not a formal freedom-to-operate opinion; FTO counsel is required before any
filing.]*

*Regulatory path.* The n-of-1 channel is now codified: FDA has issued four guidance documents
directly applicable - "Nonclinical Testing of Individualized Antisense Oligonucleotide Drug
Products for Severely Debilitating or Life-Threatening Diseases", "IND Submissions ...
Administrative and Procedural Recommendations", "IND Submissions ... Clinical Recommendations",
and "IND submissions ... CMC Recommendations" (all FDA guidance for sponsor-investigators;
cited and applied in Crooke et al. 2026) - plus the 2026 "Plausible Mechanism" framework
guidance. Milasen (Kim 2019, full text reviewed): diagnosis → dosed patient in **<12 months**,
single-species (rat) three-dose tox, 18-g GMP batch, no SAEs in year 1 - the entire package a
BUB1B exon-skipping ASO would replicate, with one explicit strengthening: our Δ-product
function assay (attack-map #4) is *better defined* than milasen's lysosomal-vacuole readout.

*Economics / funding structure.* Milasen was philanthropically funded (Mila's Miracle
Foundation, Boston Children's, Harvard Catalyst/NCATS, Mooney Family Fund). The n-Lorem
Foundation (Crooke et al. 2026, NAR gkag504, scite tallies n/a - too new; context s0/c0/m0)
industrialized the model: "for free, for life", **~USD 1 M per patient for lifetime
treatment**, goal 18–24 months acceptance→first dose (actual average >2 years due to demand),
329 applications processed, ~58 % accepted, **9 % of accepted patients needed splice-
modulating ASOs** (this candidate's exact class), >30 INDs approved under the individualized-ASO
guidance (incl. Health Canada), safety database aggregated in Crooke et al. 2021–2026. The
removal of pricing as a blocker is real but conditional on philanthropic capacity, not on any
payer mechanism; a commercial weekly-IV PMO at DMD pricing (~10^5–10^6 USD/yr class, wave-2
F13) remains the fallback and is exactly why F13 flagged reimbursement. *[Cost figure is the
publisher's own stated operating number in Crooke et al. 2026, not an audited price.]*

**Sub-verdict (c):** the submission may claim the candidate is *deliverable through a proven
philanthropic n-of-1 channel on a ~1–2-year clock at order-of-10^6 USD*, with FTO appearing
clear for plain PMO/2′MOE chemistry; it must flag that this rests on nonprofit capacity and a
formal FTO opinion, not payer approval.

---

## What the submission MAY claim vs what stays flagged

**May claim (verified this wave):**
1. Exon 17 is a text-book clean skip substrate at sequence level: frame-preserving,
   PTC-ablating, silencer-free, enhancer-rich at DMD-proven-comparator density, strong native
   junctions, no intra-exonic cryptic splice-site candidates, ESE-dense ASO landing pad
   mapped (Section a).
2. Splice-ASOs for pediatric constitutional use are regulatorily precedented and industrially
   routinized (nusinersen; milasen <12 months; FDA individualized-ASO guidance family;
   n-Lorem ~$1 M/patient-for-life) (Section c).
3. Plain PMO and 2′MOE-PS chemistries are off the foundational-composition patents
   (US 5,185,444 expired) - no composition-of-matter blocker located (Section c).

**Stays flagged (gaps, explicitly):**
- Δ716-761+E715G product function/stability/KARD-boundary: **unmeasured**; attack-map assay #4
  remains the single decisive gate (F1/F2 conditions from the adversarial review unchanged).
- Skipping efficiency achievable on **strong bilateral junctions** in patient cells: unmeasured
  (ddPCR/minigene required; the DMD51-style weak acceptor we lack is part of what made that exon easy).
- Human splice-switching outside muscle/CNS (marrow, gut): **no evidence located** - the
  constitutional reach of any ASO chemistry is asserted from animal biodistribution only.
- Cryptic splice-site *activation* under ASO treatment (intron 16 −135 donor, intron 17 +879
  acceptor are the top watch-list entries): RNA-seq QC item.
- CNS reach requires a second (IT) drug program; bone-brain duality of MVA pathology means
  systemic-only ASO treatment would leave the neurodevelopmental compartment untreated.
- Funding depends on philanthropic n-of-1 capacity; no payer pathway exists for an unapproved
  bespoke ASO. Formal FTO opinion pending (chemistry appears clear; delivery-conjugate and
  process claims not exhausted).
- MaxEntScan/motif metrics are correlates; no deep-learning splice model (e.g., SpliceAI) was
  run this wave - recommended as a cheap add-on QC, not a blocker.

## Methodology disclosure
Sequences: Ensembl REST GRCh38 (region/sequence, overlap/id, lookup expand, CDS fetch) live
2026-09-05; exon lookup cross-check vs ENSE00001029409 exact match. Splice scoring:
MaxEntScan via `maxentpy` (compiled kepbod/maxentpy) implementing Yeo & Burge 2004
(10.1089/1066527041410418, s18/c1/m1452). Motif sets: RESCUE-ESE 238 hexamers (Fairbrother
2004, PMID 15215377, 10.1093/nar/gkh393, s4/c0/m244 - list recovered from
genes.mit.edu/burgelab/rescue-ese/ESE.txt via Internet Archive 2019-01 snapshot; parse count
exactly 238/238 unique) and Zhang & Chasin 2004 PESE (2,060) / PESS (1,019) octamers + full
octamer z-table (PMID 15145827, 10.1101/gad.1195304, s5/c1/m506 - recovered from the
columbia.edu/chasin mirror via Internet Archive 2007 snapshot). DMD exon set from
ENST00000357033 (79 exons; lengths cross-checked against published amenable-exon sizes
176/233/212). Identifiers: all PMIDs resolved via NCBI E-utilities and Europe PMC (several
memory-candidate DOIs were wrong and corrected - Sazani nbt759, Amantana coph.2005.07.001,
Zhang-Chasin gad.1195304); scite tallies pulled live 2026-09-05 (token
~/.config/scite/token); no editorial notices
returned on any cited record; n-Lorem 2026 (gkag504) too new for scite tallies (0/0/0).
Regulatory facts: Drugs@FDA NDA 203568 page (Kynamro "Discontinued", verified live);
FDA guidance titles taken from the primary reference list of Crooke et al. 2026.
Patent: US5185444A verified at Google Patents/USPTO (status "Expired - Lifetime").
Full texts read: Kim et al. 2019 (PMC6961983), Crooke et al. 2026 (PMC13227102).
Full computed artifacts: `q7a_sequence_analysis.md` in this directory.

## References (APA, DOI links; s/c/m = scite supporting/contrasting/mentioning)
1. Fairbrother, W. G., Yeo, G. W., Yeh, R., et al. (2004). RESCUE-ESE identifies candidate exonic splicing enhancers in vertebrate exons. *Nucleic Acids Research, 32*, W187–W190. https://doi.org/10.1093/nar/gkh393 | PMID 15215377 | s4/c0/m244 | method
2. Zhang, X. H.-F., & Chasin, L. A. (2004). Computational definition of sequence motifs governing constitutive exon splicing. *Genes & Development, 18*, 1241–1250. https://doi.org/10.1101/gad.1195304 | PMID 15145827 | s5/c1/m506 | method
3. Yeo, G., & Burge, C. B. (2004). Maximum entropy modeling of short sequence motifs with applications to RNA splicing signals. *Journal of Computational Biology, 11*(2–3), 377–394. https://doi.org/10.1089/1066527041410418 | PMID 15285897 | s18/c1/m1452 | method
4. Charleston, J. S., et al. (2018). Eteplirsen treatment for Duchenne muscular dystrophy: exon skipping and dystrophin production. *Neurology, 90*(24), e2146–e2154. https://doi.org/10.1212/WNL.0000000000005680 | PMID 29752304 | s2/c1/m183 | human pediatric
5. Roberts, T. C., Langer, R., & Wood, M. J. A. (2020). Advances in oligonucleotide drug delivery. *Nature Reviews Drug Discovery, 19*, 673–694. https://doi.org/10.1038/s41573-020-0075-7 | PMID 32782413 | s5/c1/m2010 | review (human)
6. Sazani, P., et al. (2002). Systemically delivered antisense oligomers upregulate gene expression in mouse tissues. *Nature Biotechnology, 20*, 1228–1233. https://doi.org/10.1038/nbt759 | PMID 12426578 | s10/c0/m297 | animal (mouse)
7. Amantana, A., & Iversen, P. L. (2005). Pharmacokinetics and biodistribution of phosphorodiamidate morpholino antisense oligomers. *Current Opinion in Pharmacology, 5*(5), 550–555. https://doi.org/10.1016/j.coph.2005.07.001 | PMID 16087398 | s1/c0/m119 | review (animal/human)
8. Amantana, A., et al. (2007). Pharmacokinetics, biodistribution, stability and toxicity of a cell-penetrating peptide-morpholino oligomer conjugate. *Bioconjugate Chemistry, 18*(4), 1325–1331. https://doi.org/10.1021/bc070060v | PMID 17583927 | s12/c0/m172 | animal
9. Geary, R. S., Norris, D., Yu, R., & Bennett, C. F. (2015). Pharmacokinetics, biodistribution and cell uptake of antisense oligonucleotides. *Advanced Drug Delivery Reviews, 87*, 46–51. https://doi.org/10.1016/j.addr.2015.01.008 | PMID 25666165 | s38/c2/m811 | review (human)
10. Raal, F. J., et al. (2010). Mipomersen, an apolipoprotein B synthesis inhibitor, for lowering of LDL cholesterol concentrations in patients with homozygous familial hypercholesterolaemia. *The Lancet, 375*, 998–1006. https://doi.org/10.1016/S0140-6736(10)60284-X | PMID 20227758 | s8/c2/m575 | human ph3
11. Benson, M. D., et al. (2018). Inotersen treatment for patients with hereditary transthyretin amyloidosis. *NEJM, 379*, 22–31. https://doi.org/10.1056/NEJMoa1716793 | PMID 29972757 | s20/c2/m1336 | human ph3
12. Witztum, J. L., et al. (2019). Volanesorsen and triglyceride levels in familial chylomicronemia syndrome. *NEJM, 381*, 531–542. https://doi.org/10.1056/NEJMoa1715944 | PMID 31390500 | s9/c1/m396 | human ph3
13. Ray, K. K., et al. (2020). Two phase 3 trials of inclisiran in patients with elevated LDL cholesterol. *NEJM, 382*, 1507–1519. https://doi.org/10.1056/NEJMoa1912387 | PMID 32187462 | s33/c0/m1104 | human ph3 (pooled ORION-10/11)
14. Balwani, M., et al. (2020). Phase 3 trial of RNAi therapeutic givosiran for acute intermittent porphyria. *NEJM, 382*, 2289–2301. https://doi.org/10.1056/NEJMoa1913147 | PMID 32521132 | s9/c1/m572 | human ph3
15. Adams, D., et al. (2018). Patisiran, an RNAi therapeutic, for hereditary transthyretin amyloidosis. *NEJM, 379*, 11–21. https://doi.org/10.1056/NEJMoa1716153 | PMID 29972753 | s45/c0/m2415 | human ph3
16. Betts, C., et al. (2012). Pip6-PMO, a new generation of peptide–oligonucleotide conjugates with improved cardiac exon skipping activity for DMD treatment. *Molecular Therapy–Nucleic Acids, 1*, e38. https://doi.org/10.1038/mtna.2012.30 | PMID 23344180 | s5/c0/m235 | animal (mouse)
17. Finkel, R. S., et al. (2017). Nusinersen versus sham control in infantile-onset spinal muscular atrophy. *NEJM, 377*, 1723–1732. https://doi.org/10.1056/NEJMoa1702752 | PMID 29091570 | s51/c7/m2123 | human pediatric RCT
18. Kim, J., et al. (2019). Patient-customized oligonucleotide therapy for a rare genetic disease (milasen). *NEJM, 381*, 1644–1652. https://doi.org/10.1056/NEJMoa1813279 | PMID 31597037 | s4/c0/m645 | human pediatric n-of-1 (full text read)
19. Crooke, S. T., et al. (2026). Addressing the needs of nano-rare patients: the n-Lorem experience. *Nucleic Acids Research, 54*(10), gkag504. https://doi.org/10.1093/nar/gkag504 | PMID 42227334 | scite 0/0/0 (too new) | full text read - n-of-1 process economics/IND record
20. Crooke, S. T. (2021). A call to arms against ultra-rare diseases. *Nature Biotechnology, 39*, 671–677. https://doi.org/10.1038/s41587-021-00945-0 | PMID 34089038 | s1/c0/m35 | perspective
21. Ziegler, A., et al. (2024). Antisense oligonucleotide therapy in an individual with KIF1A-associated neurological disorder. *Nature Medicine, 30*, 2782–2786. https://doi.org/10.1038/s41591-024-03197-y | PMID 39122967 | s0/c0/m28 | human n-of-1 (second published n-Lorem-class case)
22. U.S. FDA. Guidance for Sponsor-Investigators: (i) *Nonclinical Testing of Individualized Antisense Oligonucleotide Drug Products*; (ii) *IND Submissions for Individualized ASO Drug Products: Administrative and Procedural Recommendations*; (iii) *IND Submissions ... Clinical Recommendations*; (iv) *IND submissions ... CMC Recommendations*; (v) *Plausible Mechanism Framework* (2026). fda.gov regulatory-information pages (as cited in ref 19) | regulatory
23. U.S. Patent US 5,185,444 A (Summerton & Weller, 1993). *Uncharged morpholino-based polymers having phosphorous containing chiral intersubunit linkages.* Status: Expired - Lifetime (anticipated 2010-02-09); assignee Sarepta. Google Patents/USPTO, verified 2026-09-05 | patent
24. Drugs@FDA: KYNAMRO (mipomersen sodium), NDA 203568 - marketing status "Discontinued" (accessdata.fda.gov, verified 2026-09-05) | regulatory

---
## CONTROLLER ERRATUM (2026-09-05, Q11 negation re-attack)

The Q7b delivery census sentence "no human precedent for non-muscle/non-CNS systemic
splice-switching" is too broad as written: the unprecedented limb is OLIGONUCLEOTIDE-class
(survived: all locatable human ASO splice programs are DMD / intrathecal / ocular).
Splice-switching as a modality HAS human systemic precedent in the small-molecule class
(risdiplam - approved, oral, peripherally distributed, blood-level SMN2 splicing PD in humans;
branaplam - ph2b RCT). The attack map delivery bullet carries the rescoped wording.
