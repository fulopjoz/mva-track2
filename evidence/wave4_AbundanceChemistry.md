# Wave 4 - AbundanceChemistry (Q12): is the WATCH/stabilization chemistry class complete, or does it gain members?

**Scope (from shared context):** small molecules with human or strong-preclinical evidence of RAISING BUBR1/Bub1b abundance or stability, beyond arimoclomol/NMN-WATCH - DUB/E3 axis, NAMPT/SIRT activators, methylene-blue-class proteostasis probes, BUB1B-directed HSF-program compounds, and any HTS campaign whose readout was SAC-protein abundance. Resolve the SIRT2/NAD+ direction statement against the current sirtuin literature.
**Basis:** PubMed EUtilities (all identifiers verified this session), Europe PMC full-text index, OpenAlex works API, Google Patents full-text (xhr/query), scite.ai tallies via the scite client.
**Ground truth assumed, not re-litigated:** disease variable = BubR1 ABUNDANCE (~13 % competent / ~6 % failing, Suijkerbuijk 2010); hypomorph alleles are HSP90 clients destabilized ~5–10× and proteasome-cleared (PMID 20516114); wave2_StabilizationAxis already admitted arimoclomol (adjunct, assay-gated), closed celastrol (CONTRA), PBA/TUDCA (compartment), proteasome-damping (no chronic member), and demoted NMN/SIRT2 to WATCH.
**Grades:** A = human RCT · B = human clinical/observational/tissue · C = human cells or independent-lab animal · D = mouse-only / single-lab.
**Termination criterion (declared up front):** each chemical-class sub-question (DUB/E3 axis; NAMPT/SIRT-activator class; methylene-blue class; HSF-program beyond arimoclomol; HTS/screen census; peptide/biologic class) has a verdict AND a recorded query set (queries + databases + hit counts + date). An overturn (a new compound with a verified BubR1-abundance readout) would terminate the census with a member added.

---

## VERDICT (verdict-first)

**The WATCH/stabilization chemistry class is documented COMPLETE - it gains zero members, and it does not extend beyond one WATCH member (NAD+-boosting class) plus the separately adjudicated adjunct (arimoclomol, already in the map).** Screen-census logic:

1. **The entire published pharmacology that demonstrably RAISES BubR1 abundance in vivo is one NAD+/SIRT2 axis (North 2014, mouse, grade D) - no second compound of any class has a verified BubR1-abundance readout anywhere in PubMed, Europe PMC full text, OpenAlex, or the patent record (census below).** The one genuinely new BUBR1-raising *agent class* found this wave - the progerin C-terminal peptide UPCP ("progerinin", Zhang 2023 *Nat Aging*) - raises BUBR1 in HGPS cells **mechanism-locked to progerin**: it blocks progerin–BUBR1 nuclear-membrane sequestration and PTBP1 interference. There is no progerin in MVA; the target lesion does not exist in the proband. Named and closed without a WATCH seat.
2. **The SIRT2/NAD+ direction statement is resolved** (§D below): for the chronic-abundance axis that matters to MVA, **NAD+/SIRT2 activity UP → BubR1 UP**; age-linked NAD+/SIRT2 decline → BubR1 decline. The phrase "SIRT2 down raises BubR1" (as circulated in the task framing) is **wrong for the abunance axis**; the correct reading of North 2014 is that age-driven SIRT2/NAD+ *decline* is the *cause* of BubR1 loss and NMN reverses it. The one complicating fact pattern - mitotic-site acetylation at K243/250 is *protective* (its loss degrades BubR1 mid-mitosis and promotes tumors in mice; Park 2013) versus interphase-site K668 acetylation being the *degradation* mark (CBP-antagonized-by-SIRT2; North 2014; Suematsu 2014) - is a **site-dependence nuance, not a direction reversal**, and it kills any naive "SIRT2 inhibitor to treat MVA" proposal in two directions at once (wrong on K668 abundance, hazardous on K243/250 SAC maintenance).
3. **No selective pharmacologic SIRT2 *activator* exists at any development stage** (Bursch 2024 review, *Molecules*; the extensive SIRT2-AcT literature is knockout/transgenic or NR-mediated). The class's only human-reachable lever is the NAD+-precursor arm (NMN/NR), which has human RCT safety/metabolism data (Irie 2020; Yoshino 2021) but **zero BubR1 readout in any human study** and no pediatric sirtuin-axis data. The WATCH member stays a WATCH member and gains no company.
4. **DUB/E3 pharmacology is absent in the abundance-raising direction.** The only DUB with a documented SAC-plex role, USP9X, protects the mitotic checkpoint *complex* (limits MCC turnover; Skowyra 2018, grade C) - it does not stabilize the BubR1 monomer, no DUB-*activator* class exists anywhere in pharmacology, and USP-family *inhibitors* on this node go the tumor-promoting direction (Skowyra's own loss-of-USP9X CIN datum). The E3 that clears HSP90-released hypomorph BubR1 is not named in any located source [recorded gap]; in its absence there is no druggable E3-inhibition proposal. No clinical-stage CHIP/STUB1 modulator exists (wave2 closure stands).
5. **HTS census: no screen, anywhere, has used "raise a SAC protein's abundance" as its readout** (PubMed 201 hits, Europe PMC 70 + 21, OpenAlex 254/727/1,033 relevance-triaged; google patents 0/1,393 across targeted queries) - every BubR1-adjacent screen is either oncology kill-direction (checkpoint inhibition, synthetic lethality) or bioinformatics hub-gene mining. Cross-referenced against Q11 (NegationReattack), which re-attacks the "no BUB1B-targeted drug screen" negative on different databases; this document searched the open-literature and patent layer and found none.

**Bottom line for the attack map:** Level 2 / WATCH is closed as written. The NMN/SIRT2 WATCH row should carry two corrections of form (not direction): (i) the stimulus wording - "**NAD+/SIRT2 activity ↑ raises BubR1** (North 2014), age-linked NAD+/SIRT2 ↓ drives BubR1 ↓; do not phrase as 'SIRT2 down'"; (ii) the site-dependence caveat - "BubR1 acetylation is bidirectional by site (K243/250-mitotic protective, Park 2013; K668-interphase destabilizing, North 2014); therefore SIRT2 **inhibitors** are prohibited chemistry for this axis, and generic 'deacetylation' claims without a site are prohibited sentences." One longevity-related honesty item: Wu 2023 (Sinclair lab itself) found SIRT2-Tg does **not** extend lifespan on a wild-type background - it does not touch the hypomorph-specific BubR1-stability interaction, but it blocks any "SIRT2 overexpression prolongs life, therefore…" argument; cite it whenever North 2014's lifespan leg is leaned on.

---

## Class-by-class sub-verdicts

### C1 - DUB/E3 (ubiquitin-proteasome) axis - **NO member; two nodes documented, neither druggable in the right direction**

| Node | Evidence | Direction for MVA | Druggability |
|---|---|---|---|
| **USP9X** (DUB) | Limits mitotic checkpoint complex turnover → strengthens SAC; USP9X loss elevates segregation defects and CIN (Skowyra 2018, *Cell Rep* 23:852; PMID 29669289; scite s3/c0/m42). Human cells, grade C. | An activator would be *theoretically* SAC-supportive - but the substrate is the MCC, not BubR1's own abundance. | **No DUB-activator pharmacology exists in any class** (DUBs have inhibitors only; none for USP9X). USP *inhibition* is anti-thetical (weakens SAC, raises CIN). |
| Chronic BubR1 clearance E3 | North 2014: CBP-K668 acetylation marks interphase BubR1 for proteasomal loss; MG132 rescues (Suijkerbuijk 2010). The *identity of the E3 ubiquitin ligase* executing steady-state hypomorph clearance is **not named in any located source** (apart from APC/C^Cdc20 for the mitotic-exit pool, Suematsu 2014 / Choi 2009 lineage). | An E3 inhibitor would be the mechanistically cleanest abundance-raise imaginable. | No such named target, hence no existing compound. **[INFERENCE]** CHIP/STUB1 is the conventional HSP90-client E3; no CHIP-selective clinical compound exists (wave2 closure). |

Recorded queries (2026-09-05): PubMed `BubR1[Title/Abstract] AND (deubiquitinase OR deubiquitination OR "ubiquitin-specific protease" OR USP1 OR USP9 OR USP14)` → **1 hit** (generic UBE2C review, PMID 24361302 - excluded); PubMed `BubR1[TA] AND ("E3 ligase" OR "ubiquitin ligase" OR ubiquitination OR CHIP OR UBR5 OR "beta-TrCP")` → 64 hits (all cancer-biology mass citations; triaged - no BubR1-stability E3 named); PubMed `BubR1[TA] AND ("protein stability" OR "half-life" OR proteasomal)` → 7 hits (none pharmacologic); OpenAlex `BubR1 deubiquitinase` → 127 works relevance-triaged (USP9X/USP44 rows above; no new DUB). **No evidence located for a BubR1-abundance-raising DUB or E3 compound.**

### C2 - NAMPT/SIRT-activator class - **one WATCH member (already holds a seat); nothing added**

- **Direction limb (mouse, grade D, single-lab lineage but internally replicated across readouts):** SIRT2 overexpression or NMN treatment raises BubR1 abundance in vivo; in the exact BubR1^H/H hypomorph strain SIRT2-Tg extends lifespan (North 2014, *EMBO J* 33:1438; PMID 24825348, DOI 10.15252/embj.201386907; scite s2/c1/m220, no editorial notices). The single scite "contradicting" classification could not be itemized via the token's available endpoints this session (citation-list API routes returned 400/404; recorded as a limitation, not suppressed).
- **Honesty/anti-overclaim datum:** SIRT2-Tg does **not** extend lifespan on a WT background (Wu 2023, *Aging Cell* 22:e14027; PMID 38009412; scite s1/c0) - the lifespan leg is hypomorph-specific; the BubR1-stability leg is not challenged.
- **Human evidence for the NAD+ arm (grade A/B, metabolic endpoints only, zero BubR1 readout):** Irie 2020 (*Endocr J* 67:153; oral NMN safe in healthy men, N=10; PMID 31685720; scite s3/c3/m160); Yoshino 2021 (*Science* 372:1224; NMN 250 mg/d × 10 wk, prediabetic women, N=25; raised NAD metabolome, no BubR1 measurement - PMID 33888596; scite s6/c1/m328). No pediatric NAD+-axis exposure data located [recorded gap].
- **NAMPT activators (P7C3 class, SBI-class):** no BubR1 linkage anywhere (PubMed cross-query NAMPT/P7C3/SRT2104/"sirtuin activator" × BubR1 → 2 hits, neither a NAMPT activator). Human-cell datum (grade C): NAMPT overexpression prevents age/high-glucose-driven endothelial **polyploidy** via SIRT1 (Borradaile 2010, *AJP Cell Physiol* 298:C66; PMID 19846757; scite s2/c0/m36) - chromosome-content protection in human vascular cells; tangential, no BubR1 measurement, records the axis's widest human-cell reach.
- **No selective SIRT2-activating small molecule exists** at any development stage (Bursch 2024 review, *Molecules* 29:1185; PMID 38474697; the "activator" field is SIRT1-biased STACs, all preclinical or failed-clinical).

Recorded queries (2026-09-05): PubMed `SIRT2[TA] AND (BubR1 OR BUB1B)` → 11; `(NMN OR "nicotinamide mononucleotide" OR "nicotinamide riboside" OR NAD)[TA] AND (BubR1 OR BUB1B)` → 8; `sirtuin[TA] AND (BubR1 OR BUB1B)` → 8; `(NAMPT OR "NAMPT activator" OR P7C3 OR SRT2104 OR metformin OR "sirtuin activator")[TA] AND (BubR1 OR BUB1B)` → 2; `"SIRT2 activator"[TA] OR "sirt2 activation"[TA] OR "SIRT2-activating"[TA]` → 18 (every hit genetic, NR-mediated, or inhibitory); `(MIB-626 OR "nicotinamide mononucleotide")[TA] AND (trial OR randomized OR safety)` → 96 (metabolic/safety RCTs only); Europe PMC `"nicotinamide mononucleotide" AND "BubR1"` full-text → 50 (reviews + Pun 2025, no new compound).

### C3 - Methylene-blue-class proteostasis probes - **class empty on this target**

PubMed `"methylene blue"[TA] AND (BubR1 OR "spindle checkpoint" OR "mitotic checkpoint" OR aneuploidy)` → **0 hits** (2026-09-05). No member; recorded negative.

### C4 - HSF-program compounds beyond arimoclomol - **closed as documented by wave-2; no new member**

Wave 2 already admitted arimoclomol (adjunct, assay #5-gated), closed celastrol (CONTRA; HSP90-Cdc37 disrupting + complex-I poison), shelved BGP-15 (no pediatric data), and ruled the HSP90-potentiator class absent (S3). This wave's residual sweep found: Europe PMC `("geranylgeranylacetone" OR "HSF1A" OR "heat shock response" OR "HSF1 activator") AND "BubR1"` → 13 hits, none pharmacology-on-BubR1 (nearest: heat-shock-induced mitotic arrest requires HSP105 for SAC activation, PMID 30496702 - basic biology, no compound). **No HSF-program compound has ever reported a BubR1 (or any client-kinase-mutant) abundance readout** - the wave-2 Gap 1 stands verbatim, and the class is documented complete at one adjudicated member (arimoclomol).

### C5 - HTS campaigns with a SAC-protein-abundance readout - **none located**

PubMed `(BubR1 OR BUB1B)[TA] AND ("small molecule" OR compound OR drug OR "high-throughput" OR screen)` → 201 hits, top-60 by relevance title-triaged (zero abundance-RAISE screens; all oncology kill-direction or hub-gene bioinformatics); PubMed increase/stabilize cross-query → 75 hits title-triaged (only North 2014 / Wu 2023 as in-vivo abundance modulation; no compound); Europe PMC `"BubR1" AND "high-throughput screening"` → 70; `BUB1B AND "drug screen"` → 21 (all synthetic-lethality or pediatric-predisposition papers); OpenAlex searches (`BubR1 small molecule increase abundance` 727; `BubR1 protein stability drug screen` 1,033; `BUB1B high-throughput screen compound` 254) - relevance-triaged top pages: no campaign whose readout was raising any SAC protein. Q11 (NegationReattack) independently re-attacks the "no BUB1B-targeted screen" recorded negative on registries/full-text engines; converge on its yield for the registry layer.

### C6 - Peptide/biologic class (out-of-scope bonus row, named for census completeness) - **one BUBR1-raising agent exists and it is mechanism-locked out of MVA**

UPCP/progerinin: a progerin C-terminal peptide that dissociates progerin–BUBR1 nuclear-membrane binding and *enhances BUBR1 expression* in HGPS patient cells; ameliorates progeroid phenotypes and extends lifespan of Lmna^G609G/G609G mice (Zhang 2023, *Nat Aging* 3:185; PMID 37118121; scite s0/c0/m17; has an author-correction, non-substantive). Grade C (human cells + independent-lab mouse). **Mechanism requires progerin, which does not exist in MVA** → closed; noted because it is the single non-NAD+ agent anywhere that demonstrably raises BUBR1 abundance, and reviewers may cite it - the report should name-and-dismiss it explicitly rather than let a reviewer raise it.

### C7 - Metformin WATCH-residue reinforcement (no new member; one caution datum)

High-dose (1–16 mM) metformin **deregulates BUBR1/MAD2** and drives genotoxic stress in cancer *and* non-cancer cells (Lyu 2022, *Food Chem Toxicol* 165:113129; PMID 35568294; grade C human cells). Supratherapeutic-dose datum, but it supports the attack map's ≤100 µM cap discipline on the metformin WATCH residue rather than any abundance hope.

---

## D - SIRT2/NAD+ direction statement, resolved against the sirtuin literature state

**Correct statement (for the report, verbatim-safe):** *In the chronic-abundance axis (the MVA disease variable), BubR1 interphase stability is CBP-SIRT2-titrated at lysine 668: CBP acetylation marks BubR1 for proteasomal degradation; NAD+-dependent SIRT2 deacetylation of K668 stabilizes it. Age-linked NAD+/SIRT2 decline lowers BubR1; NAD+ restoration (NMN) or SIRT2 overexpression raises BubR1 abundance in vivo, including in the BubR1-hypomorph strain (North 2014). Raised SIRT2 activity does not extend lifespan without the hypomorph context (Wu 2023). Separately and without contradiction, mitotic K243/250 acetylation (PCAF, BRCA2-reinforced) is SAC-PROTECTIVE: it restrains APC/C-dependent BubR1 destruction during prometaphase, and mice carrying an acetylation-deficient K243R allele degrade BubR1 prematurely, weaken their SAC, and develop tumors (Choi 2009/2012; Park 2013; Suematsu 2014). Consequentially: (i) "acetylation stabilizes/destabilizes BubR1" is a prohibited sentence unless a site is named; (ii) SIRT2 INHIBITORS are blocked chemistry for this axis (wrong direction at K668, hazardous at K243/250); (iii) no site-selective pharmacology exists, so the deliverable lever remains the NAD+-precursor blunt end (NMN/NR), grade D hypothesis, WATCH.*

Supporting row set:

| Claim | Source | Species/grade | scite (s/c/m) |
|---|---|---|---|
| SIRT2 OE or NMN raises BubR1 in vivo; SIRT2-Tg extends BubR1^H/H lifespan; K668 is the stability site (CBP counteracts) | North 2014 *EMBO J* (PMID 24825348) | mouse, D | 2/1/220 |
| Age-linked BubR1 decline reconfirmed as an actionable deficiency (human HF tissue + rodent + cardiomyocyte KD; human decline observed, no compound) | Pun 2025 *Aging Cell* (PMID 40607964) | human tissue + rodent, B/C | 0/0/0 (new) |
| SIRT2-Tg does NOT extend lifespan on WT background (lifespan leg is hypomorph-specific) | Wu 2023 *Aging Cell* (PMID 38009412) | mouse, D | 1/0/0 |
| SIRT2 deacetylates mitotic K250; SIRT2-KD raises K250 acetylation but did NOT change total BubR1 or mitotic timing | Suematsu 2014 *BBRC* (PMID 25285631) | human cell line, C | 2/0/25 |
| Acetylation-DEFICIENT BubR1 (K243R/+) → premature mitotic degradation, weakened SAC, spontaneous tumors | Park 2013 *J Cell Biol* (PMID 23878276; DOI 10.1083/jcb.201210099) | mouse + MEFs, D | 6/0/90 |
| BRCA2 recruits PCAF to reinforce mitotic BubR1 acetylation → SAC integrity; interrupted association → aneuploidy + tumors | Choi 2012 *Dev Cell* (PMID 22340495) | mouse + human tissue, C | 8/0/100 |
| BubR1 acetylation at prometaphase required to modulate APC/C and mitotic timing (foundational site-paper) | Choi 2009 *EMBO J* (PMID 19407811) | human cell line, C | 24/0/596 |
| Oocyte axis: aging-linked Sirt2 loss → BubR1-K243 hyperacetylation → meiotic defects; K243R rescues | Qiu 2018 *Aging Cell* (PMID 29067790) | mouse oocytes, D | 4/0/55 |
| Axis review state (BubR1–SIRT2 mutual reinforcement across aging/aneuploidy contexts) | Pun 2024 *Semin Cancer Biol* (PMID 39490401; DOI 10.1016/j.semcancer.2024.10.005) | review | 5 mentions |

Resolution of the framing phrase: the task text's "North 2014 says SIRT2 down/NMN up raises BubR1" conflates cause and lever. North 2014's finding is: **age-driven SIRT2/NAD+ DOWN causes BubR1 DOWN; NMN (NAD+ UP) raises BubR1**. No limb of North 2014, and no located literature 2014–2026, shows SIRT2 *downregulation* raising BubR1. The K243/250 protective-acetylation papers are the only conceivable source of directional confusion; they govern mitotic-spindle-phase stability at a different site and do not transfer to the chronic-abundance axis.

---

## Recorded negatives (all 2026-09-05)

1. "Any compound raises BubR1 abundance besides the NAD+/SIRT2 axis and HGPS-locked UPCP": **no evidence located** (queries in C1–C6; PubMed/EPMC/OpenAlex/Google Patents).
2. "A BubR1-specific DUB exists": **no evidence located** (PubMed DUB cross-query: 1 hit, generic; OpenAlex: USP9X/USP44 rows triaged out).
3. "A named E3 clears hypomorph BubR1 (CHIP or otherwise)": **no evidence located** - gap, not closure.
4. "A selective pharmacologic SIRT2 activator exists (any stage)": **no evidence located** (PubMed 18-hit triage + Bursch 2024 review).
5. "A methylene-blue-class probe touches SAC/BubR1": **no evidence located** (0 hits).
6. "Any HTS campaign used SAC-protein abundance as its readout": **no evidence located** (PubMed 201 + EPMC 70/21 + OpenAlex 2,014 combined hits, relevance-triaged top pages; none).
7. "Any patent claims a small-molecule BubR1 stabilizer": **no evidence located** (`"BubR1" "stabiliz" small molecule` → 0 grants/applications; `"BUB1B" "increase" "expression" compound` → 1,393 hits, top titles are TCR-peptide and kinase-DEGRADER filings - one Dana-Farber kinase-PROTAC family hits "BUB1B" in a degradation list, i.e., the **opposite direction**, recorded here so nobody miscites it).
8. "Human BubR1 readout under any NAD+ intervention": **no evidence located** (96 NMN-trial hits, titular/abstract level: metabolic endpoints only).
9. "Pediatric NAD+-axis / sirtuin-axis exposure data": **no evidence located**.

Scite tooling limitation (recorded): citation-list endpoints returned 400/404 with the session token; tallies were available and are used; the 1 "contradicting" classification on North 2014 was contextualized via the direct-literature check (no retracting/challenging primary paper located; the only in-axis challenge, Wu 2023, targets the lifespan generalization, not the stability interaction). Editorial notices: none on any load-bearing DOI.

## Gaps (explicit, unresolved)

1. Identity of the E3 ubiquitin ligase executing steady-state clearance of destabilized BubR1 - un-named. If ever named (CHIP/STUB1 is the conventional HSP90-client candidate, [INFERENCE]), an E3-inhibitor node would open; today there is no compound.
2. No human BubR1-abundance readout exists for any intervention, including the WATCH member (NMN/NR); patient-cell NMN/NR co-test remains the assay-#5 adjunct, unchanged from the map.
3. Site-resolved acetylation state of the proband's N1002K protein (K668 vs K243/250 occupancy) is unmeasured and is the sharpest possible mechanistic check for whether NAD+-axis WATCH could engage in this genotype; feasible as an MS add-on to assay #2/#5.
4. K668 numbering is mouse/ortholog-convention-dependent in places (human K668 vs K250 literature) - site mapping onto the proband's construct was not re-derived here; flagged for the MS workup, no literature conflict on the N1002K allele specifically.

## Termination declared & met

Declared criterion: each class sub-question has a verdict + recorded queries. Met:

| Sub-question | Verdict | Queries recorded |
|---|---|---|
| DUB/E3 axis | NO member (USP9X documented, undruggable; E3 un-named) | C1: 4 query sets + OpenAlex |
| NAMPT/SIRT activators | WATCH stays one member (NAD+ class); no SIRT2-selective activator | C2: 7 query sets + EPMC |
| Methylene-blue class | Empty on target | C3: 1 query (0 hits) |
| HSF-program beyond arimoclomol | Closed as wave-2 documented | C4: 1 query set |
| HTS with SAC-abundance readout | None located; cross-ref Q11 registry layer | C5: 5 query sets |
| Peptide/biologic class | UPCP named and mechanism-locked out | C6 (found within EPMC/OpenAlex rows) |
| SIRT2/NAD+ direction statement | Resolved (site-dependence nuance; two prohibited foreseeable errors) | §D table |

## References (APA, DOI-linked; all identifiers re-verified via NCBI EUtilities / Europe PMC 2026-09-05)

Borradaile, N. M., & Pickering, J. G. (2010). Polyploidy impairs human aortic endothelial cell function and is prevented by nicotinamide phosphoribosyltransferase. *American Journal of Physiology-Cell Physiology, 298*(1), C66–C74. [doi:10.1152/ajpcell.00357.2009](https://doi.org/10.1152/ajpcell.00357.2009) (PMID 19846757) - human cells.
Bursch, K. L., Goetz, C. J., & Smith, B. C. (2024). Current trends in sirtuin activator and inhibitor development. *Molecules, 29*(5), 1185. [doi:10.3390/molecules29051185](https://doi.org/10.3390/molecules29051185) (PMID 38474697) - review.
Choi, E., Choe, H., Min, J., Choi, J. Y., Kim, J., & Lee, H. (2009). BubR1 acetylation at prometaphase is required for modulating APC/C activity and timing of mitosis. *The EMBO Journal, 28*(14), 2077–2089. [doi:10.1038/emboj.2009.29](https://doi.org/10.1038/emboj.2009.29) (PMID 19407811) - human cell line.
Choi, E., Park, P. G., Lee, H. O., et al. (2012). BRCA2 fine-tunes the spindle assembly checkpoint through reinforcement of BubR1 acetylation. *Developmental Cell, 22*(2), 295–308. [doi:10.1016/j.devcel.2012.01.009](https://doi.org/10.1016/j.devcel.2012.01.009) (PMID 22340495) - mouse + human tissue.
Irie, J., Inagaki, E., Fujita, M., et al. (2020). Effect of oral administration of nicotinamide mononucleotide on clinical parameters and nicotinamide metabolite levels in healthy Japanese men. *Endocrine Journal, 67*(2), 153–160. [doi:10.1507/endocrj.EJ19-0313](https://doi.org/10.1507/endocrj.EJ19-0313) (PMID 31685720) - human, adult.
Lyu, T., Zhou, H., Wang, Y., et al. (2022). High-dose metformin induces a low-glucose dependent genotoxic stress. *Food and Chemical Toxicology, 165*, 113129. [doi:10.1016/j.fct.2022.113129](https://doi.org/10.1016/j.fct.2022.113129) (PMID 35568294) - human cell lines.
North, B. J., Rosenberg, M. A., Jeganathan, K. B., et al. (2014). SIRT2 induces the checkpoint kinase BubR1 to increase lifespan. *The EMBO Journal, 33*(13), 1438–1453. [doi:10.15252/embj.201386907](https://doi.org/10.15252/embj.201386907) (PMID 24825348) - mouse (BubR1^H/H).
Park, I., Lee, H. O., Choi, E., et al. (2013). Loss of BubR1 acetylation causes defects in spindle assembly checkpoint signaling and promotes tumor formation. *Journal of Cell Biology, 202*(2), 295–309. [doi:10.1083/jcb.201210099](https://doi.org/10.1083/jcb.201210099) (PMID 23878276) - mouse + MEFs.
Pun, R., Haas, A. L., Thapa, A., et al. (2025). BubR1 insufficiency drives transcriptomic alterations and pathology associated with cardiac aging and heart failure. *Aging Cell, 24*(9), e70160. [doi:10.1111/acel.70160](https://doi.org/10.1111/acel.70160) (PMID 40607964) - human tissue + rodent.
Qiu, D., Hou, X., Han, L., Li, X., Ge, J., & Wang, Q. (2018). Sirt2-BubR1 acetylation pathway mediates the effects of advanced maternal age on oocyte quality. *Aging Cell, 17*(1), e12698. [doi:10.1111/acel.12698](https://doi.org/10.1111/acel.12698) (PMID 29067790) - mouse oocytes.
Skowyra, A., Allan, L. A., Saurin, A. T., & Clarke, P. R. (2018). USP9X limits mitotic checkpoint complex turnover to strengthen the spindle assembly checkpoint and guard against chromosomal instability. *Cell Reports, 23*(3), 852–865. [doi:10.1016/j.celrep.2018.03.100](https://doi.org/10.1016/j.celrep.2018.03.100) (PMID 29669289) - human cells.
Suematsu, T., Li, Y., Kojima, H., Nakajima, K., Oshimura, M., & Inoue, T. (2014). Deacetylation of the mitotic checkpoint protein BubR1 at lysine 250 by SIRT2 and subsequent effects on BubR1 degradation during the prometaphase/anaphase transition. *Biochemical and Biophysical Research Communications, 453*(3), 588–594. [doi:10.1016/j.bbrc.2014.09.128](https://doi.org/10.1016/j.bbrc.2014.09.128) (PMID 25285631) - human cell line.
Suijkerbuijk, S. J. E., van Osch, M. H. J., et al. (2010). Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy. *Cancer Research, 70*(12), 4891–4900. [doi:10.1158/0008-5472.CAN-09-4319](https://doi.org/10.1158/0008-5472.CAN-09-4319) (PMID 20516114) - human patient cells (repo full-text verified; cross-reference).
Wu, L. E., Fiveash, C. E., Bentley, N. L., et al. (2023). SIRT2 transgenic over-expression does not impact lifespan in mice. *Aging Cell, 22*(12), e14027. [doi:10.1111/acel.14027](https://doi.org/10.1111/acel.14027) (PMID 38009412) - mouse.
Yoshino, M., Yoshino, J., Kayser, B. D., et al. (2021). Nicotinamide mononucleotide increases muscle insulin sensitivity in prediabetic women. *Science, 372*(6547), 1224–1229. [doi:10.1126/science.abe9985](https://doi.org/10.1126/science.abe9985) (PMID 33888596) - human RCT.
Pun, R., Kumari, N., Monieb, R. H., Wagh, S., & North, B. J. (2024). BubR1 and SIRT2: Insights into aneuploidy, aging, and cancer. *Seminars in Cancer Biology, 106–107*, 201–216. [doi:10.1016/j.semcancer.2024.10.005](https://doi.org/10.1016/j.semcancer.2024.10.005) (PMID 39490401) - review.
Zhang, N., Hu, Q., Sui, T., et al. (2023). Unique progerin C-terminal peptide ameliorates Hutchinson–Gilford progeria syndrome phenotype by rescuing BUBR1. *Nature Aging, 3*(2), 185–201. [doi:10.1038/s43587-023-00361-w](https://doi.org/10.1038/s43587-023-00361-w) (PMID 37118121; author correction 10.1038/s43587-023-00427-9) - human HGPS cells + mouse.
