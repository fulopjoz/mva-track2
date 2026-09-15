# MECHANISM_G1 - What does BubR1's kinase domain DO at the checkpoint?

MechanismForge deliverable, 2026-09-05. Gating question for Track-2 precision
repurposing in biallelic-BUB1B MVA1 (proband: p.Leu737Ter [NMD null] + p.Asn1002Lys
[kinase-domain C-lobe, novel]). Companion files: `VARIANT_PROTEIN_IMPACT.md`
(local structural analysis), `LITERATURE_SWEEP.md` (prior sweep).

**Method / verification.** According to PubMed (PubMed MCP, 2026-09-05): every
PMID cited below was resolved against the live NCBI record today, except items
explicitly marked "[sweep record]" carried from `LITERATURE_SWEEP.md`
(scite/pre-expiry). Full text was read from PMC for the load-bearing paper
Suijkerbuijk et al. 2010 ([PMC2887387](https://doi.org/10.1158/0008-5472.CAN-09-4319)).
scite was NOT used (token expired). Grades: **Established** (multiple independent
groups / direct human data), **Supported** (replicated but not definitive or
single-lab with strong design), **Contested** (primary evidence on both sides,
unresolved), **Single-study** (one report, unreplicated).

---

## 1. VERDICT - catalytic output

### Verdict (one line)
**BUBR1's catalytic output is DISPENSABLE for the spindle checkpoint arrest
(Established) and dispensable for error-free chromosome segregation when
BUBR1 abundance is held at wild-type levels (Supported, with a residual
Contested fringe); the kinase domain's essential function is STRUCTURAL  - 
fold integrity that gates whole-protein abundance (Established in MVA patient
alleles).** BUBR1 is best described as an unusual, catalytic-triad-retaining
**pseudokinase** (Contested-to-Supported consensus label; even the leading
pro-activity group now titles its methods chapter "the mitotic checkpoint
pseudokinase BUBR1", Gama Braga et al. 2022,
[DOI 10.1016/bs.mie.2022.03.045](https://doi.org/10.1016/bs.mie.2022.03.045),
PMID 35525552).

### Tiered grades

| Claim | Grade | Key primary evidence (According to PubMed) |
|---|---|---|
| Catalysis dispensable for SAC arrest (APC/C inhibition resides in N-terminus/KEN boxes) | **Established** | Malureanu et al. 2009, Dev Cell 16:118 ([DOI 10.1016/j.devcel.2008.11.004](https://doi.org/10.1016/j.devcel.2008.11.004), PMID 19154723) - conditional KO + domain mutants: N-terminal Cdc20-binding domain essential; C-terminal Cdc20-binding, Bub3-binding and kinase domains not essential for the listed mitotic functions. Elowe et al. 2010, J Cell Sci 123:84 ([DOI 10.1242/jcs.056507](https://doi.org/10.1242/jcs.056507), PMID 20016069) - KEN-box mutations abolish SAC without touching congression; SAC and congression uncoupled. |
| Purified BUBR1 kinase domain has no detectable catalytic activity in vitro (binds nucleotide but cannot deliver catalysis) | **Supported** | Breit et al. 2015, PLoS One 10:e0144673 ([DOI 10.1371/journal.pone.0144673](https://doi.org/10.1371/journal.pone.0144673), PMID 26658523) - in-depth biochemical comparison vs the genuinely active BUB1 paralog. |
| "Putative catalysis by human BUBR1 is dispensable for error-free chromosome segregation"; ATP-contacting residues instead required for conformational stability | **Supported** (single-lab replacement design, convergent with Breit in vitro) | Suijkerbuijk et al. 2012, Dev Cell 22:1321 ([DOI 10.1016/j.devcel.2012.03.009](https://doi.org/10.1016/j.devcel.2012.03.009), PMID 22698286) - pseudokinase paper; this is the published version superseding the preprint flagged in `LITERATURE_SWEEP.md` §1.3. |
| Complete DELETION of the kinase domain (LAP-731X truncation) restores checkpoint, chromosome alignment and normal segregation in human replacement assays | **Supported** (one lab, rigorous design, uncontributed) | Suijkerbuijk et al. 2010, Cancer Res 70:4891 (full text read; above). |
| TENSION-DEPENDENT catalytic claims: BUBR1 is an "active kinase at unattached kinetochores"; kinase-dead point mutants cause attachment/congression defects; CENP-E-dependent autophosphorylation boosts checkpoint strength | **Contested** | Pro: Guo et al. 2012, J Cell Biol 198:205 ([DOI 10.1083/jcb.201202152](https://doi.org/10.1083/jcb.201202152), PMID 22801780) - autophosphorylation claimed in cells, dependent on CENP-E binding; nonphosphorylatable mutant → misalignment + reduced Aurora-B-substrate phosphorylation. Pro (older): Huang & Yen 2009, Cell Cycle 8:1164 ([DOI 10.4161/cc.8.8.8151](https://doi.org/10.4161/cc.8.8.8151), PMID 19282664) - reviews data that Plk1 sites T792/T1008/S676 "stimulate BubR1 kinase activity" and promote attachments. Contra: Breit 2015 (no in vitro activity); Suijkerbuijk 2012 (dispensable in vivo at equal abundance); Suijkerbuijk 2010 (everything reconciles via abundance, not activity). Neutral older datum: Wong & Fang 2006, Mol Biol Cell 17:4390 ([DOI 10.1091/mbc.e06-04-0346](https://doi.org/10.1091/mbc.e06-04-0346), PMID 16885416) - Xenopus extracts: phosphoepitope generation required Mps1 and Bub1 activities but **not** BubR1's. Likely reconciliation: kinase-dead POINT mutants are partially misfolded/dosage-perturbed whereas domain deletions are clean; in-cellulo "autophosphorylation" signals may include contaminating or CENP-E-dependent co-kinases (interpretation lanes laid out in Gama Braga 2022). |

### What this verdict means for N1002K
N1002 sits 19.8 Å from catalytic D882 (`VARIANT_PROTEIN_IMPACT.md`) - far outside
any catalytic geometry, consistent with the verdict that catalysis is not the
readout. The limiting output of a C-lobe allele of this type is **protein
abundance/stability** (see §5), not phosphotransfer.

---

## 2. Substrates and non-catalytic C-lobe functions

**Validated phospho-substrates: none.** No substrate of BUBR1 catalysis is
established. The only claims on record are (i) **autophosphorylation**
(T1008 among others; Plk1-dependent stimulation framings - Huang & Yen 2009;
CENP-E-dependent - Guo 2012) and (ii) loose **CENP-E cross-talk** (CENP-E as
"kinase activator" in Guo 2012). Both sit inside the Contested side of §1 and
are incompatible with the in vitro null result (Breit 2015). Question wording
("CENP-E claims") verdict: **Contested, likely non-catalytic mechanism.**

**What the kinase domain / C-lobe contributes besides catalysis** (the
structural verdict of §1 decomposed):

1. **Fold integrity → protein abundance (Established).** Kinase-domain MVA
   missense alleles cause MVA *through destabilization* (misfolding, HSP90-client
   dependence, ~2-fold faster turnover, proteasomal clearance) - see §5. The
   domain is a stability element, not an enzyme, in the disease-relevant sense.
2. **Contribution to maximal Cdc20/APC-C binding (Supported).** Elowe 2010
   (above): sequences in the BUBR1 C-terminus are needed for *maximal*
   Cdc20/APC-C association even though the KEN boxes carry the qualitative
   interaction. So the C-lobe is part of the MCC assembly surface landscape.
3. **Houses attachment/tension regulatory phosphosites (Established that the
   sites exist and are regulated by other kinases; the effector mechanism they
   feed is partly Contested).** Plk1 sites S676 (tension-sensitive; Elowe et al.
   2007, Genes Dev 21:2205, [DOI 10.1101/gad.436007](https://doi.org/10.1101/gad.436007),
   PMID 17785528), T792 and **T1008** (Huang & Yen 2009); Cdk1 site T620 primes
   Plk1 docking; S670 (Cdk1) anchors the KARD phosphatase-docking module (§4).
   **N1002 lies 6 residues C-terminal of T1008** - the proband's substitution is
   in the immediate sequence environment of the C-lobe's principal regulatory
   phosphosite [INFERENCE about functional consequence; positional fact verified].
4. **Oligomerization: essentially refuted as a self-interaction (Supported).**
   BUBR1:BUB3 is a 1:1 complex with no additional self-oligomerization in
   solution (Breit 2015). What exists instead is a **heterotetramer with
   BUB1:BUB3 via a pseudo-symmetric BUB1–BUBR1 interface** (Overlack et al.
   2015, eLife 4:e05269, [DOI 10.7554/eLife.05269](https://doi.org/10.7554/eLife.05269),
   PMID 25611342) - the interface that makes BUBR1's kinetochore targeting
   serial on BUB1 (§3).
5. **CDC20-binding surface:** primary KEN-box interactions are N-terminal
   (Elowe 2010, Malureanu 2009); C-lobe contributes secondarily (point 2).
   There is no evidence the C-lobe itself harbors an independent Cdc20-binding
   surface - the C-terminal KEN-like/Cdc20 element tested by Malureanu 2009
   maps N-terminal to the kinase domain and was non-essential.

---

## 3. Upstream SAC wiring around BUBR1 recruitment - serial vs parallel

Verified wiring map (all According to PubMed records above/fulltexts):

```
Mps1/TTK (kinetochore-MT dependent; own recruitment gated by Aurora B
          via TPR-domain relief - Nijenhuis et al. 2013, JCB 201:217,
          DOI 10.1083/jcb.201210033, PMID 23569217)
   │ phosphorylates
   ▼
KNL1 MELT repeats (arrayed, graded: more MELTs ⇒ more BUB recruitment,
          Vleugel et al. 2013, JCB 203:943,
          DOI 10.1083/jcb.201307016, PMID 24344183)
   │ read by
   ▼
BUB3 (phospho-MELT reader; interface mutations ⇒ checkpoint defect,
      Primorac et al. 2013, eLife 2:e01030,
      DOI 10.7554/eLife.01030, PMID 24066227)
   │
   ├─► BUB1:BUB3 docked first ──► recruits BUBR1 by direct pseudo-symmetric
   │      heterodimerization; BUBR1 kinetochore targeting is DEPENDENT ON BUB1
   │      (Overlack 2015) - SERIAL leg
   │
   └─► KI motifs of KNL1 bind BUBR1 TPR directly and cooperate with the
          adjacent MELT to seed full SAC-complex assembly (Krenn et al. 2014,
          Curr Biol 24:29, DOI 10.1016/j.cub.2013.11.046, PMID 24361068)
          - PARALLEL short-circuit (enhancer, not independent driver)
```

- **Serial core:** Mps1 → MELT(p) → BUB3:BUB1 → BUBR1. Because BUBR1
  recruitment is subordinated to BUB1 (Overlack 2015), **an upstream boost
  (more Mps1 output) cannot bypass a defective BUBR1 node** - it raises the
  ceiling of a broken leg. [Established wiring + Established-once caution]
- **Parallel components:** (i) KI-motif short-circuit (Krenn 2014); (ii) the
  MAD2 arm - Mps1→MAD1 phosphorylation flux feeds O-MAD2 conversion, and
  BUBR1:BUB3 + MAD2 jointly form the MCC (Tang 2002 / Sudakin 2001 [sweep
  records]). MAD2 flux is the one *parallel* route by which an upstream boost
  could in principle thicken MCC despite a leaky BUBR1 module - no direct
  human-cell evidence that this rescues BUBR1-hypomorph segregation fidelity
  [INFERENCE; no evidence located for the rescue direction].
- **Aurora-B-gated Mps1 recruitment** (Nijenhuis 2013) couples the error-
  correction arm (§4) back into SAC ignition - the two arms share an ignition
  switch.

---

## 4. The Aurora B error-correction arm as the parallel compensatory system

**The arm exists, is mechanistically central and is INTACT - indeed
functionally unopposed - when BUBR1 is dysfunctional (Supported); it is NOT,
on present evidence, "druggable-enhanceable": the cell-validated manipulation
runs in the opposite (damping) direction and carries intrinsic trade-offs.**

Foundation (Established): Aurora B selectively destabilizes incorrectly
attached kinetochore–microtubules and is needed both to correct errors and to
maintain the checkpoint (Hauf et al. 2003, JCB 161:281,
[DOI 10.1083/jcb.200208092](https://doi.org/10.1083/jcb.200208092),
PMID 12707311; review: Lampson & Cheeseman 2011, Trends Cell Biol 21:133,
[DOI 10.1016/j.tcb.2010.10.007](https://doi.org/10.1016/j.tcb.2010.10.007),
PMID 21106376). Its product class - **merotelic attachments - escapes SAC
detection** (Salmon, Cimini & colleagues 2005, Phil Trans R Soc B 360:553,
[DOI 10.1098/rstb.2004.1610](https://doi.org/10.1098/rstb.2004.1610),
PMID 15897180), which is why error-correction throughput, not only arrest,
limits segregation fidelity - exactly the failure mode of BUBR1 hypomorphs.

Coupling to BUBR1 (Established/Supported): BUBR1's KARD domain, via Plk1/Cdk1-
primed S670/S676 phosphorylation, physically recruits **PP2A-B56** to
kinetochores to *counteract* Aurora B; removing BUBR1 or blocking Plk1 lowers
kinetochore PP2A-B56 and raises Aurora-B-substrate phosphorylation, and the
resulting attachment failure is **reverted by inhibiting Aurora B**
(Suijkerbuijk et al. 2012, Dev Cell 23:745,
[DOI 10.1016/j.devcel.2012.09.005](https://doi.org/10.1016/j.devcel.2012.09.005),
PMID 23079597 - the paper already cited by `LITERATURE_SWEEP.md` §1.3 for this
mechanism; direct-binding confirmation: Kruse et al. 2013, J Cell Sci
126:1086, [DOI 10.1242/jcs.122481](https://doi.org/10.1242/jcs.122481),
PMID 23345399).

Interpretation for MVA: there is no evidence of an AURKB-pathway lesion in
MVA - patient cell defects read out as weakened arrest + alignment failure
(Suijkerbuijk 2010; Matsuura 2006), i.e., the destabilizing arm keeps firing
while its BUBR1→PP2A counterweight is thinned. So:

- **Enhancing** Aurora B/error-correction output in a BUBR1-hypomorph cell
  would be expected to worsen attachment stability (more unopposed
  destabilization): **no evidence located** for any approved or pediatric-
  experienced drug that strengthens error correction; by the wiring itself the
  direction is mechanistically wrong. Grade for "intact YES": Supported.
  Grade for "enhanceable": **Contested-to-refuted in principle** in the BUBR1-
  hypomorph context specifically.
- The cell-demonstrated correction direction is *partial Aurora B damping*
  (Suijkerbuijk 2012). But this is a laboratory lever, not a therapy: Aurora B
  inhibition collapses the SAC arm it ignites (Hauf 2003; Nijenhuis 2013) and
  has no pediatric dosing experience - see Implications.

---

## 5. Functional data on kinase-domain hypomorphic BUB1B alleles

### Human / patient-derived (highest evidence tier)

- **Suijkerbuijk et al. 2010** (full text read; Established - direct patient
  cell lines + clean replacement design):
  - MVA lymphoblasts/fibroblasts: checkpoint-deficient (nocodazole/STLC
    escape within 68–114 min vs arrest in controls), 2–3× chromosome
    misalignment; re-expression of WT BUBR1 restores parental-level checkpoint.
  - **Every kinase-domain-region missense allele tested (I909T, R814H, L844F,
    L1012P; plus near-domain R727C) is destabilized 5–10×**; N-terminal
    missense (Y155C, R550Q) are stable → two classes: abundance alleles vs
    separation-of-function alleles.
  - Destabilization mechanism: mRNA normal; protein turnover ~2× faster;
    **mutant folding is HSP90-dependent** (geldanamycin erased mutant protein;
    CHX+GA removed virtually all; MG132 rescued) → misfolding → proteasomal
    clearance.
  - Forced re-expression of I909T or **L1012P to WT abundance FULLY restored
    checkpoint function** → the allele class is functional-if-abundant:
    limiting variable is dose, not catalysis.
  - **Dosage curve is steep and saturating**: ~13% residual BUBR1 → virtually
    no segregation-fidelity impact; ~6% → majority of cells missegregate.
- **Matsuura et al. 2006** (Established, patients): BubR1 protein reduced
  >50%, kinetochore localization diminished, kinetochore p55cdc/Cdc20
  association abolished in PCS/MVA patient cells; restored by chromosome-15
  microcell transfer - [DOI 10.1002/ajmg.a.31069](https://doi.org/10.1002/ajmg.a.31069),
  PMID 16411201.
- **Izumi et al. 2009** (Supported): PCS-patient cells show **Plk1
  hyperactivity and centrosome amplification/multipolar mitoses**; BubR1
  normally restrains interphase Plk1 - a non-checkpoint consequence of low
  BubR1 relevant to tumor initiation  - 
  [DOI 10.1038/onc.2009.141](https://doi.org/10.1038/onc.2009.141),
  PMID 19503101.
- Founder report: Hanks et al. 2004, Nat Genet 36:1159  - 
  [DOI 10.1038/ng1449](https://doi.org/10.1038/ng1449), PMID 15475955.

### Mouse (supporting tier; discordances flagged)

- **Sieben et al. 2020, JCI 130:171**  - 
  [DOI 10.1172/JCI126863](https://doi.org/10.1172/JCI126863), PMID 31738183
  (prior sweep noted an erratum on record for this paper [sweep record]).
  Mouse L1002P mimics the **human MVA allele L1012P**:
  BubR1^X753/L1002P and ^H/X753 mice die prematurely; **BubR1^H/L1002P mice
  are viable with MVA features** (cancer predisposition, dwarfism,
  lipodystrophy, sarcopenia); total-BUBR1 reduction + allelic effects (not
  only dose) drive phenotype heterogeneity; monoallelic carriers develop
  late-onset pathologies with mTORC1 hyperactivity in sarcopenia.
  **Residue map: human L1012P ≡ mouse L1002P** (10-aa isoform offset). Our
  proband's **human N1002 is 10 residues N-terminal of the modeled human
  L1012P** - same C-lobe surface neighborhood.
- **Wijshake et al. 2012, PLoS Genet 8:e1003138**  - 
  [DOI 10.1371/journal.pgen.1003138](https://doi.org/10.1371/journal.pgen.1003138),
  PMID 23300461 (note: this paper appears in prior project context records
  as "2012 J Cell Biol"; the verified venue is **PLoS Genetics**):
  monoallelic 2211insGTTA → shortened lifespan, mild aneuploidy, enhanced
  carcinogen-induced tumor growth.
- **Baker et al. 2004, Nat Genet 36:744**  - 
  [DOI 10.1038/ng1382](https://doi.org/10.1038/ng1382), PMID 15208629:
  graded BubR1 reduction → graded aneuploidy + senescence (the dosage
  principle, mouse).
- Extreme end: near-complete deletion → shortened mitosis, catastrophic
  progenitor death, microcephaly (Simmons/Cho et al. 2019, Hum Mol Genet
  28:1822, [DOI 10.1093/hmg/ddz022](https://doi.org/10.1093/hmg/ddz022),
  PMID 30668728).

**Mouse–human discordance:** monoallelic mouse GTTA is compatible with life
and only mildly aneugenic, while human biallelic MVA1 is a severe pediatric
syndrome; Bub3 haploinsufficiency in mice gives CIN without tumor
predisposition (Kalitsis 2005 [sweep record]). Mouse rescue data therefore
cannot be read as predicting human benefit magnitude.

### N1002K placement against this map
N1002K bears every signature of the **"low-abundance" MVA allele class**:
C-lobe substitution (like I909T/L1012P/L844F/R814H), predicted local
destabilization (AlphaMissense 0.9229; hydrophobic-cluster disruption per
`VARIANT_PROTEIN_IMPACT.md`), 6 aa from regulatory phosphosite T1008, 10 aa
from the validated pathogenic L1012P. Expected phenotype [INFERENCE]:
NMD-null + unstable-hypomorph → total functional BubR1 in the ~10–30% band
→ leaky SAC + alignment defects, matching the MVA1 dosage paradigm. Nothing
in the literature suggests N1002K would behave as a separation-of-function
allele; nothing measures it - it remains unassayed (gap).

---

## 6. Implications for drug targeting

1. **Stabilization/up-regulation is the literature-endorsed intervention class;
   catalytic activation is not.** The verdict (§1) plus the rescue-by-
   re-expression result (§5) say the child's lesion class is a *scaffold-dose*
   defect: WT-abundance mutant protein is checkpoint-competent. Any tolerated
   route that raises residual BubR1 abundance (proteostasis support,
   readthrough+NMD tuning on the null allele, acetylation-axis speculation in
   `LITERATURE_SWEEP.md` Axis e) addresses the limiting variable; an
   "allosteric activator of BubR1 activity" addresses a nonexistent bottleneck.
   Grade: rationale Supported (cellulo direct), no clinical-agent data.
2. **HSP90 inhibition is a mechanistic TRAP here, not merely a cancer axis.**
   Kinase-domain mutant BUBR1 is an HSP90 client: geldanamycin-class
   inhibition collapsed mutant protein levels in patient/replacement systems
   (Suijkerbuijk 2010, direct). Axis-(a) HSP90i candidates in
   `LITERATURE_SWEEP.md` would therefore degrade exactly the N1002K protein
   the proband survives on - a genotype-specific CONTRA consideration for
   chronic/prophylactic HSP90i, sharply reinforcing the sweep's general
   checkpoint-kinase-buffer caveat (Woodford 2016 [sweep record]).
   Grade: **Supported (direct primary evidence), decision-relevant.**
   Proteasome inhibition (MG132) rescued mutant levels in vitro - proof of
   mechanism only; chronic proteasome inhibition is not pediatric-feasible
   and is recorded here only as mechanistic evidence.
3. **Upstream boosting is structurally capped.** BUBR1 recruitment is serial
   through BUB1 (Overlack 2015); Mps1-axis stimulation cannot route around a
   thinned BUBR1 module. The only parallel leg is MAD2-flux into MCC - an
   untested rescue hypothesis, no evidence located. Mps1/TTK inhibitors remain
   CONTRA here (as per `LITERATURE_SWEEP.md` Axis b).
4. **Aurora B arm is intact but points the "wrong way" for prevention.** No
   enhancement drug exists; damping it suppresses the SAC it ignites and lacks
   pediatric experience. Its practical relevance: in a hypothetical MVA1
   tumor, the intact Aurora B dependency argues emerging CIN clones keep
   error-correction rewiring as a viable treatment axis - a treatment-context
   note, not a prevention lever.
5. **Watch-item: Plk1 hyperactivity** (Izumi 2009) in low-BubR1 patient
   cells - centrosome/multipolarity pressure is a plausible co-driver of the
   RMS/aneuploidy phenotype; no pediatric PLK1 agent line established
   (volasertib adult-only, failed) - flag for PhenotypeAxis if a centrosome
   axis emerges.
6. **Measurement priority (gates all of the above):** allele-resolution in
   proband-derived cells - BUBR1 steady-state + CHX-chase half-life,
   geldanamycin/MG132 sensitivity (tests §5 class prediction directly),
   phospho-T1008 status (tests the 6-aa neighbor effect), kinetochore BubR1
   and nocodazole-arrest kinetics (replicates Suijkerbuijk 2010 / Matsuura
   2006 assays). These four assays convert the [INFERENCE]s into data for ~1
   month of wet-lab work.

---

## References (all verified against PubMed, 2026-09-05; [sweep record] = carried from LITERATURE_SWEEP.md)

1. Hanks, S., Coleman, K., Reid, S., et al. (2004). Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. *Nature Genetics, 36*(11), 1159–1161. [https://doi.org/10.1038/ng1449](https://doi.org/10.1038/ng1449) | PMID 15475955
2. Baker, D. J., Jeganathan, K. B., Cameron, J. D., et al. (2004). BubR1 insufficiency causes early onset of aging-associated phenotypes and infertility in mice. *Nature Genetics, 36*(7), 744–749. [https://doi.org/10.1038/ng1382](https://doi.org/10.1038/ng1382) | PMID 15208629
3. Malureanu, L. A., Jeganathan, K. B., Hamada, M., et al. (2009). BubR1 N terminus acts as a soluble inhibitor of cyclin B degradation by APC/C(Cdc20) in interphase. *Developmental Cell, 16*(1), 118–131. [https://doi.org/10.1016/j.devcel.2008.11.004](https://doi.org/10.1016/j.devcel.2008.11.004) | PMID 19154723
4. Elowe, S., Dulla, K., Uldschmid, A., Li, X., Dou, Z., & Nigg, E. A. (2010). Uncoupling of the spindle-checkpoint and chromosome-congression functions of BubR1. *Journal of Cell Science, 123*(1), 84–94. [https://doi.org/10.1242/jcs.056507](https://doi.org/10.1242/jcs.056507) | PMID 20016069
5. Elowe, S., Hümmer, S., Uldschmid, A., Li, X., & Nigg, E. A. (2007). Tension-sensitive Plk1 phosphorylation on BubR1 regulates the stability of kinetochore microtubule interactions. *Genes & Development, 21*(17), 2205–2219. [https://doi.org/10.1101/gad.436007](https://doi.org/10.1101/gad.436007) | PMID 17785528
6. Suijkerbuijk, S. J. E., van Dam, T. J. P., Karagöz, G. E., et al. (2012). The vertebrate mitotic checkpoint protein BUBR1 is an unusual pseudokinase. *Developmental Cell, 22*(6), 1321–1329. [https://doi.org/10.1016/j.devcel.2012.03.009](https://doi.org/10.1016/j.devcel.2012.03.009) | PMID 22698286
7. Suijkerbuijk, S. J. E., Vleugel, M., Teixeira, A., & Kops, G. J. P. L. (2012). Integration of kinase and phosphatase activities by BUBR1 ensures formation of stable kinetochore-microtubule attachments. *Developmental Cell, 23*(4), 745–755. [https://doi.org/10.1016/j.devcel.2012.09.005](https://doi.org/10.1016/j.devcel.2012.09.005) | PMID 23079597
8. Suijkerbuijk, S. J. E., van Osch, M. H. J., Bos, F. L., Hanks, S., Rahman, N., & Kops, G. J. P. L. (2010). Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy. *Cancer Research, 70*(12), 4891–4900. [https://doi.org/10.1158/0008-5472.CAN-09-4319](https://doi.org/10.1158/0008-5472.CAN-09-4319) | PMID 20516114 | full text read, PMC2887387
9. Breit, C., Bange, T., Petrovic, A., et al. (2015). Role of intrinsic and extrinsic factors in the regulation of the mitotic checkpoint kinase Bub1. *PLoS ONE, 10*(12), e0144673. [https://doi.org/10.1371/journal.pone.0144673](https://doi.org/10.1371/journal.pone.0144673) | PMID 26658523
10. Guo, Y., Kim, C., Ahmad, S., Zhang, J., & Mao, Y. (2012). CENP-E-dependent BubR1 autophosphorylation enhances chromosome alignment and the mitotic checkpoint. *Journal of Cell Biology, 198*(2), 205–217. [https://doi.org/10.1083/jcb.201202152](https://doi.org/10.1083/jcb.201202152) | PMID 22801780
11. Huang, H., Hittle, J., Zappacosta, F., Annan, R. S., Hershko, A., & Yen, T. J. (2008). Phosphorylation sites in BubR1 that regulate kinetochore attachment, tension, and mitotic exit. *Journal of Cell Biology, 183*(4), 667–680. [https://doi.org/10.1083/jcb.200805163](https://doi.org/10.1083/jcb.200805163) | PMID 19015317
12. Huang, H., & Yen, T. J. (2009). BubR1 is an effector of multiple mitotic kinases that specifies kinetochore:microtubule attachments and checkpoint. *Cell Cycle, 8*(8), 1164–1167. [https://doi.org/10.4161/cc.8.8.8151](https://doi.org/10.4161/cc.8.8.8151) | PMID 19282664
13. Wong, O. K., & Fang, G. (2006). Loading of the 3F3/2 antigen onto kinetochores is dependent on the ordered assembly of the spindle checkpoint proteins. *Molecular Biology of the Cell, 17*(10), 4390–4399. [https://doi.org/10.1091/mbc.e06-04-0346](https://doi.org/10.1091/mbc.e06-04-0346) | PMID 16885416
14. Gama Braga, L., Garand, C., & Elowe, S. (2022). Considerations for studying phosphorylation of the mitotic checkpoint pseudokinase BUBR1. *Methods in Enzymology, 667*, 507–534. [https://doi.org/10.1016/bs.mie.2022.03.045](https://doi.org/10.1016/bs.mie.2022.03.045) | PMID 35525552
15. Primorac, I., Weir, J. R., Chiroli, E., et al. (2013). Bub3 reads phosphorylated MELT repeats to promote spindle assembly checkpoint signaling. *eLife, 2*, e01030. [https://doi.org/10.7554/eLife.01030](https://doi.org/10.7554/eLife.01030) | PMID 24066227
16. Vleugel, M., Tromer, E., Omerzu, M., et al. (2013). Arrayed BUB recruitment modules in the kinetochore scaffold KNL1 promote accurate chromosome segregation. *Journal of Cell Biology, 203*(6), 943–955. [https://doi.org/10.1083/jcb.201307016](https://doi.org/10.1083/jcb.201307016) | PMID 24344183
17. Krenn, V., Overlack, K., Primorac, I., van Gerwen, S., & Musacchio, A. (2014). KI motifs of human Knl1 enhance assembly of comprehensive spindle checkpoint complexes around MELT repeats. *Current Biology, 24*(1), 29–39. [https://doi.org/10.1016/j.cub.2013.11.046](https://doi.org/10.1016/j.cub.2013.11.046) | PMID 24361068
18. Overlack, K., Primorac, I., Vleugel, M., et al. (2015). A molecular basis for the differential roles of Bub1 and BubR1 in the spindle assembly checkpoint. *eLife, 4*, e05269. [https://doi.org/10.7554/eLife.05269](https://doi.org/10.7554/eLife.05269) | PMID 25611342
19. Nijenhuis, W., von Castelmur, E., Littler, D., et al. (2013). A TPR domain-containing N-terminal module of MPS1 is required for its kinetochore localization by Aurora B. *Journal of Cell Biology, 201*(2), 217–231. [https://doi.org/10.1083/jcb.201210033](https://doi.org/10.1083/jcb.201210033) | PMID 23569217
20. Hauf, S., Cole, R. W., LaTerra, S., et al. (2003). The small molecule Hesperadin reveals a role for Aurora B in correcting kinetochore-microtubule attachment and in maintaining the spindle assembly checkpoint. *Journal of Cell Biology, 161*(2), 281–294. [https://doi.org/10.1083/jcb.200208092](https://doi.org/10.1083/jcb.200208092) | PMID 12707311
21. Lampson, M. A., & Cheeseman, I. M. (2011). Sensing centromere tension: Aurora B and the regulation of kinetochore function. *Trends in Cell Biology, 21*(3), 133–140. [https://doi.org/10.1016/j.tcb.2010.10.007](https://doi.org/10.1016/j.tcb.2010.10.007) | PMID 21106376
22. Salmon, E. D., Cimini, D., Cameron, L. A., & DeLuca, J. G. (2005). Merotelic kinetochores in mammalian tissue cells. *Philosophical Transactions of the Royal Society B, 360*(1455), 553–568. [https://doi.org/10.1098/rstb.2004.1610](https://doi.org/10.1098/rstb.2004.1610) | PMID 15897180
23. Kruse, T., Zhang, G., Larsen, M. S. Y., et al. (2013). Direct binding between BubR1 and B56-PP2A phosphatase complexes regulate mitotic progression. *Journal of Cell Science, 126*(5), 1086–1092. [https://doi.org/10.1242/jcs.122481](https://doi.org/10.1242/jcs.122481) | PMID 23345399
24. Matsuura, S., Matsumoto, Y., Morishima, K.-i., et al. (2006). Monoallelic BUB1B mutations and defective mitotic-spindle checkpoint in seven families with premature chromatid separation (PCS) syndrome. *American Journal of Medical Genetics Part A, 140*(4), 358–367. [https://doi.org/10.1002/ajmg.a.31069](https://doi.org/10.1002/ajmg.a.31069) | PMID 16411201
25. Izumi, H., Matsumoto, Y., Ikeuchi, T., Saya, H., Kajii, T., & Matsuura, S. (2009). BubR1 localizes to centrosomes and suppresses centrosome amplification via regulating Plk1 activity in interphase cells. *Oncogene, 28*(31), 2806–2820. [https://doi.org/10.1038/onc.2009.141](https://doi.org/10.1038/onc.2009.141) | PMID 19503101
26. Sieben, C. J., Jeganathan, K. B., Nelson, G. G., et al. (2020). BubR1 allelic effects drive phenotypic heterogeneity in mosaic-variegated aneuploidy progeria syndrome. *Journal of Clinical Investigation, 130*(1), 171–188. [https://doi.org/10.1172/JCI126863](https://doi.org/10.1172/JCI126863) | PMID 31738183 | erratum on record per prior sweep
27. Wijshake, T., Malureanu, L. A., Baker, D. J., Jeganathan, K. B., van de Sluis, B., & van Deursen, J. M. (2012). Reduced life- and healthspan in mice carrying a mono-allelic BubR1 MVA mutation. *PLoS Genetics, 8*(12), e1003138. [https://doi.org/10.1371/journal.pgen.1003138](https://doi.org/10.1371/journal.pgen.1003138) | PMID 23300461
28. Simmons, A. J., Park, R., Sterling, N. A., et al. (2019). Nearly complete deletion of BubR1 causes microcephaly through shortened mitosis and massive cell death. *Human Molecular Genetics, 28*(11), 1822–1836. [https://doi.org/10.1093/hmg/ddz022](https://doi.org/10.1093/hmg/ddz022) | PMID 30668728

According to PubMed records retrieved via the PubMed MCP on 2026-09-05; DOI
links included per PubMed attribution requirements. Carried-over sweep items
(Tang 2002; Sudakin 2001; Kalitsis 2005; Woodford 2016) were not re-verified
this session and are flagged [sweep record] where used.
