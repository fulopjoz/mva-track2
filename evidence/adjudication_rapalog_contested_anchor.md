# Adjudication memo - rapalogs as contested constitutional anchor (Cycle-1)

Date: 2026-09-12. Owner: coordinator agent. Status: **PENDING HUMAN ADJUDICATION** (report standard: contested evidence-grading is a human decision). Supporting artifacts: `cycle1_nk.md`, `cycle1_fly.md`, `cycle1_mech.md` (same directory; verbatim-quote briefs).

Trigger: an independent science-agent evidence table (out-of-family, archived at `~/mva_science_salvage/`) hard-PENALIZED everolimus/sirolimus for constitutional MVA (rationale cited: NK-cell clearance of aneuploid cells blocked by chronic mTORC1 immunosuppression, citing PMID 28633018), while our report names everolimus as the constitutional discussion candidate anchored on 47-month pediatric exposure. Cross-check = genuine conflict → adjudicated here rather than smoothed over.

## Citation-audit corrections (all verified against PMC full text, 2026-09-12)
*Per the traceable-source rule: the adjudication task brief itself supplied two identifiers that failed Wave-NK's audit and were replaced - recorded here, not smoothed over. An orthology correction in the reverse direction is also on record: an external advisory claimed rod = BubR1 ortholog; Ensembl Compara shows this is false (see FLY caveats); the wave artifact's original labeling stands.*
- Often-cited Mannick RCTs are **PMID 25540326** (2014, *Sci Transl Med*) and **PMID 29997249** (2018, *Sci Transl Med*) - not 24927573 / 29979249 (unrelated papers).
- Santaguida et al. 2017, PMID 28633018 is **Developmental Cell**, and shows NK killing of complex-karyotype aneuploid cells **in vitro (NK92 co-culture, NKG2D/MICA + DNAM1/CD112-CD155)** - and contains **zero mTOR-inhibitor data**.

## Three-wave verdict summary

### Wave NK (dose-dependent immune effect) - confidence: moderate
- The PENALIZE rationale's own citation ladder fails at rung one: PMID 28633018 says nothing about mTOR; it establishes the *mechanism* (NK recognizes aneuploid/senescent cells), not the *interaction* (drug blocks mechanism).
- At conversational-dose bands (everolimus troughs 3–7 ng/mL), human data point the other way: transplant patients at 3.38–3.85 ng/mL show **expanded, more cytotoxic CD56dim NK** with preserved NKG2D (PMID 30319636); low-dose TORC1 inhibition **improved** immune outcomes in two elderly RCTs (PMIDs 25540326, 29997249); rapamycin upregulated NKG2D on cytotoxic γδ T cells (PMID 27256566); in-vitro 10 ng/mL did not inhibit NK lysis (PMID 24704664).
- Suppression documented only at oncologic dosing (PMID 33931486) and post-HSCT lymphopenic reconstitution (PMID 36966873) - neither is the conversational band.
- Honest gap (stated by the wave, preserved verbatim): **no primary study directly tests mTOR-inhibitor exposure against NK-mediated clearance of aneuploid cells.** Both positions extrapolate; the extrapolation now favors preserve/enhance at low dose.

### Wave FLY (2026 Drosophila MVA model) - confidence: high, with model caveat
- PMID 41820377 (*Nat Commun* 17:3829, 2026): rapamycin gave a small neuroblast-number rescue (+4.9/lobe) but **failed Pros+ progeny and brain size - brain lobe area WORSENED ~21% (p=0.041)**; the authors suggest TOR inhibition impairs proliferation of aneuploid NSCs.
- Chaperone overexpression (Hsp60+Hsp60c): brain lobe size **completely restored** (n.s. vs control); ROS scavengers (Sod2+GTPx-1): same full brain-size restoration; p35 apoptosis blockade: full brain-size restoration.
- Authors name mitochondrial-homeostasis/chaperone/apoptosis routes for translation - TOR not among them.
- **Transfer caveats, orthology-verified (2026-09-12):** the model is worniu-GAL4 > bub3/rod RNAi. `bub3` IS the fly BUB3 ortholog (and biallelic BUB3 disease is itself a variegated-aneuploidy syndrome), but `rod` (rough deal, FBgn0003062) is the RZZ kinetochore-complex scaffold - it is NOT the BubR1/BUB1B ortholog. Ensembl Compara (verified 2026-09-12) maps human BUB1B to fly `Bub1` (FBgn0031696, the ancestral Bub1/Mad3 combined ortholog). So the model is an MVA-family-relevant SAC-core loss, not a knockdown of the patient's own gene; the real transfer limits are RNAi near-complete loss in mitotic neuroblasts vs the patient's ~13% hypomorphic BUB1B, a 48 h acute dosing window vs chronic human dosing, and fly larval-brain tissue vs human developmental context.

### Wave MECH (2024–25 aneuploid-cell biology) - confidence: moderate
- HSF1/chaperone route moderately upgraded: two independent papers show constitutional-direction rescue (PMID 25205676: HSF1 is rate-limiting in aneuploid human cells, genetic overexpression rescues; PMID 40527892: chromosome-gain mitochondrial dysfunction, chaperone OE rescued mild trisomies). **No pharmacological chaperone agent has been tested in any aneuploidy model** - arimoclomol extrapolation remains genetic-to-pharmacological. HSF1 pro-tumor caveat stands in a Wilms/RMS-predisposed child.
- Elamipretide/SS-31 route is **not** upgraded: no mitochondrial-targeted agent tested anywhere in this literature; normal membrane potential in aneuploid cells is a poor mechanistic fit for a cardiolipin/cristae stabilizer.
- Nothing in this wave tests or rehabilitates rapalogs.

## Where the debate actually moved
Entering this cycle, the question was "does the conversational mTOR dose suppress NK clearance of aneuploid cells?" Wave NK answered: probably not at 3-7 ng/mL troughs (and the external table's cited mechanism contains no mTOR data at all). The *open* question is now different: "does TOR inhibition stunt growth of aneuploid tissue?" - one organism-level cell-autonomous signal against (fly, orthology-caveated), zero human data. All three options below are framed against that relocated question.

## Adjudication options (HUMAN TO SELECT ONE)

**Option A - Keep everolimus as named candidate, add honesty paragraph.** *(coordinator`s non-binding reading of the weights: real pediatric exposure data plus dosing-band-matched NK data outweigh one orthology-caveated fly signal; the human decides.)*
Scientific basis: the PENALIZE's citation chain fails; low-dose human data are consistent with immune neutrality/enhancement; pediatric 47-month exposure record stands. The fly model's anti-TOR datum is recorded verbatim **with the not-BUB1B caveat**. Edits: report §4.1 gains a three-paragraph "Contested anchor adjudication" box (this memo linked); candidates.tsv rapalog row gains `contested_adjudicated=2026-09-12; see adjudication memo`.

**Option B - Demote everolimus to conditional (behind chaperone/mitochondrial_ route).**
Scientific basis: fly cell-autonomous datum + convergent chaperone rescue in two papers. Honesty cost: pharmacological chaperone agents untested in aneuploidy models; vs everolimus' real pediatric exposure data; demotion trades measured human data for genetic extrapolation.

**Option C - Drop rapalogs entirely.**
Basis would need direct NK-under-mTORi evidence that does not exist; rejected by Wave NK's gap statement. Listed for completeness.

Post-decision actions (any option): update report section + candidates.tsv row, re-run citation census, one amend-push to the track2 repo. The memo and three wave artifacts ship with the evidence pack regardless of option.
