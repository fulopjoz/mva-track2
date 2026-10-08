# A child's rare disease, examined properly - what the evidence does (and does not) support

**Track 2 of the "Rare Disease, Real Kid" MVA Hackathon 2026 - evidence program, explained for readers without a biology background.**
Version 1.0 · 2026-09-05 · DRAFT - not yet human-approved for submission use (see §12).

---

## 0. How to read this report

This document was written for people who are not biologists. Every technical word is
explained where it first appears, and again in the Glossary (§11). Every factual claim
carries a bracketed tag like **[E42]** that points to an entry in the References section
(§10), where you find the real scientific source, a clickable link, and a one-line note on
how that source was verified. Nothing in this report asserts anything beyond what those
sources support - where honest science must say "nobody knows", this report says exactly that.
One more convention: a tag like **[P2-1]** marks a correction our own adversarial reviewers
caught mid-process - we keep these visible on purpose. And a tag like **[E40-P2]** points to
the internal review document recording that fix.

Two warnings up front, kept short and honest:

1. **This is not medical advice.** It is an analysis of published research, prepared for a
   scientific competition. Any decision about a real child's treatment belongs to that
   child's doctors and family.
2. **No drug discussed here is proven to help the patient.** The report's most important
   section is the one about what we are *not* claiming (§8).

---

## 1. The challenge, and the child, in plain terms

A 2026 public science competition (the "MVA Hackathon", run as a HuggingFace challenge
space [E44]) presents a real pediatric case: a young child with an ultra-rare inherited
disease called **MVA** - short for *Mosaic Variegated Aneuploidy* - caused by faults in a
gene called **BUB1B**. Children with MVA have a substantially elevated risk of kidney
cancer (Wilms tumor) and a muscle-lineage cancer (rhabdomyosarcoma), plus blood cancers;
current medicine offers no drug to reduce that risk - only surveillance scans to catch
tumors early [E20][E21].

The competition's Track 1 asks teams to interpret the child's genome. Track 2 - the
subject of this report - asks a harder question:

> **Is there any already-approved drug that could be safely repurposed to help this child?**

Our team answered that question the slow, careful way: instead of picking a popular
candidate, we mapped every reasonable way to attack the disease, ran three waves of
independent research, and then subjected our conclusions to **four separate adversarial
reviews** - major findings running 8 → 2 → 2 → 0 - *designed to destroy them*. What survived is
summarized here. The short answer, fully unpacked in §5:

- **The named repurposing candidate** is **everolimus** - an approved drug with solid
  pediatric safety data - proposed only inside a strict, monitored, gate-first protocol,
  with its risks stated as plainly as its rationale.
- **The precision medicine of the future** for this child may be a tailored gene-patch
  (an "exon-skipping" drug) - and we show exactly why that idea is scientifically
  sound *and* what the one decisive experiment is.
- Several widely-hyped ideas in this disease area are **documented dead ends** for this
  child, with reasons.

## 2. The one minute of biology you need

Your body is made of ~37 trillion cells. Cells multiply by dividing: one cell becomes two.
Before dividing, each cell must copy its instruction book (the genome) and then split the
copies perfectly between the two daughter cells. Splitting is perilous - so cells evolved a
**quality-control checkpoint** that halts division until every copy is correctly attached
to the machinery that pulls them apart.

**BubR1 is a protein that guards that checkpoint.** Think of it as the air-traffic
controller at cell division: without it, chromosomes land on random runways. A chromosome
is one of the 46 bound volumes the instruction book comes in - and every new cell must get
exactly one copy of every volume. Cells with too
little BubR1 activity end up with the wrong number of chromosomes - a state called
**aneuploidy** - and aneuploidy is a well-established cancer driver - in the closest animal experiments, mice with
broken BubR1 develop tumors [E17a][E20b]. Honesty demands the other half too: aneuploid cells are
also actively hunted and cleared by the immune system, which is why this is a race, not a
certainty [E17].

**MVA (Mosaic Variegated Aneuploidy)** is what happens when a person is born with too
little working BubR1: "mosaic" because only a portion of cells go wrong, "variegated"
because the wrongness varies, "aneuploidy" because the chromosome counts break [E18][E20].
The condition was defined genetically in 2004 when mutations in **BUB1B** (the gene that
encodes BubR1) were found to cause it [E20].

## 3. This child's two mutations - and why both matter

Each of us carries two copies of every gene: one from mother, one from father. This child's
**two BUB1B copies are both broken, but in two different ways** [E01] (the case document):

**(a) The "stop-sign" mutation - medical shorthand p.Leu737Ter, also written L737\*.**
(These letter-number codes are labels, not information; we show them once so your doctors
can match this report to the genetic report.)  A gene's instruction text is read
in three-letter words; one copy of this child's BUB1B text has a spelling change that turns
a normal word ("build here") into the word "STOP" at position 737. The cellular machinery
that reads the book therefore stops building the protein three-quarters of the way through
 -  and unfinished proteins are usually destroyed by the cell's recycling system
(a quality process called nonsense-mediated decay; in this exact gene's geometry
there is no documented escape route - the evidence says
"escape is unlikely"; we use that wording, not "guaranteed," because the process is
probabilistic [E42]). That copy makes **almost no working BubR1**.

**(b) The "shape" mutation - p.Asn1002Lys (N1002K).**  The other copy has a single-letter
spelling change deep inside the protein's enzymatic core (its "kinase domain"). Swapping
that one building block changes the local chemistry so that the protein likely folds
incorrectly, becomes unstable, and gets degraded faster than normal. Evidence for this is
unusually strong for a single-letter change: a widely used computer program trained to flag
dangerous mutations (AlphaMissense) rates this change 0.92 out of 1.0 - "likely pathogenic"
[E38]; the same position is conserved from humans to fruit flies, and in
the fruit-fly crystal structure (a structure measured in a real laboratory experiment, not a computer prediction) the
equivalent residue sits 2.9 Å - about the width of two atoms touching, direct molecular
contact, not merely "nearby" - from a matching partner, exactly
the contact that breaking would destabilize [E39]. (See Figure 1.)

**The abundance logic that runs the whole analysis.**  This child has one copy making ~0%
of its protein and one copy making a reduced amount of a fragile protein. Total working
BubR1 in the child's cells therefore sits at some small fraction of normal. Laboratory
measurements in patient-derived cells have shown that the checkpoint works almost normally
when a person has roughly ~13% of the normal BubR1 level, and fails badly at ~6% [E04].
Nobody has measured this child's actual BubR1 level - that is assay #6 in §6. But the
arithmetic of one nearly silent copy plus one fragile copy puts the child somewhere in that
dangerously narrow band. **That is why every serious treatment idea
below is, at heart, about raising - or not further lowering - the amount of working
BubR1** - not about the enzyme's chemical activity, which careful reading of the literature
shows is largely *not* what the failing checkpoint needs [E04, E04b]. The confusing part,
in plain terms: the checkpoint needs the protein to *be present*, not to *perform* its
chemical trick - so it is the *amount* of BubR1 that drives everything below, and that is
why we dwell on how much survives, not on what the enzyme does.

## 4. How we made this trustworthy - and how you can audit it

**Method in one paragraph.**  We did not pick a favorite drug and defend it. We (1)
assembled every reasonable attack route (biology-first), (2) sent four independent
AI research agents (independent automated literature workers with recorded search logs)
into the primary literature as three research waves - covering
nonsense-suppression, protein stabilization, senescence ("cell-ageing") clearance,
chromosome-instability medicine precedents, pediatric dosing, surveillance standards,
negation re-attacks, and abundance chemistry, then (3) subjected the assembled evidence to
**four** adversarial reviews by agents spawned with fresh context and a hostile mandate [E40]. One honesty note
on those reviews: the checkers ran inside the same AI lineage as the drafters - independence was
by role, not by vendor, so a genuinely different-vendor review is still on our to-do list. Findings were scored
*major / minor* and every finding was fixed, with the fix itself reviewed in the next pass.
The majors per adversarial review ran **8 → 2 → 2 → 0** across the four reviews, where stopping at zero was the
pre-declared rule (Figure 5) [E41]. In parallel, every load-bearing citation was
re-verified against live registries: **90 of 90 sampled identifiers resolve to real papers**
[E40]. Nothing was accepted until a human (this project's lead) approved it, per our own rule.
The full audit trail ships in this repository (`evidence/WORKFLOW_CONSENSUS.md`, the four
adversarial-review memos, and 19 research memos with recorded search logs).

**One extra check that is not yet in the official guidance, and why it is missing.** Two further
sources written for this condition both add a **blood test every three months, to look for
leukaemia**, alongside the kidney ultrasound: a 2026 guide written for this exact gene by the MVA
Society with Unique and reviewed by a consultant geneticist [E73], and Japan's national handbook for
this syndrome, which schedules a blood count at every visit from three months of age onwards [E74].
The reason it is absent from the main guidance is specific. The companion guideline covering blood
cancers in children with a genetic predisposition does not mention this syndrome, or any of its
genes, anywhere in its text [E75]. Set against that, one child with this condition did develop a
bone-marrow disorder and died after a transplant [E76]. We are not making this a recommendation:
the sources are a family guide and a national handbook rather than a formal guideline, and the
marrow evidence is a single case. We report it because a three-monthly blood test is cheap and
low-risk, and because a family should be able to raise it with their team and ask whether it fits.

**Three honesty features unusual enough to name:**
1. Several of our own earlier statements were caught and corrected by the adversarial
   passes - the corrections are preserved inline so you can see them (e.g., a misattributed
   mouse experiment [P2-1], an overstated trial result [P2-2]).
2. Where no evidence exists, the report says "**no evidence located**" and shows the
   search queries that were tried [E40].
3. Where the honest answer is "this must be tested in a lab before anyone can responsibly
   conclude anything," we name the exact experiment (§6) rather than papering over it.

---

*PART 1 of 2 - sections 5–12 follow in this same file*

## 5. The verdicts, explained

### 5a. Today's real standard of care - and it is *not* a drug
Verified against the two governing sources as they stand in 2026 [E21][E22]: for **all**
children with MVA, from birth to age 7, a **kidney ultrasound every 3 months**, plus
regular clinical review with attention to muscle pain or blood in urine, and deliberate
**avoidance of unnecessary radiation**. (Why 7? That is the window where Wilms-tumor risk
concentrates; what to do after that age is less settled - a question for the child's care
team.) No whole-body MRI is recommended. Newer blood-based
tumor-DNA tests ("liquid biopsy" / cfDNA) are **not** standard of care in any predisposition
syndrome - promising trials exist, but the largest one explicitly excludes MVA-type
chromosome-instability syndromes [E47] - not because the tests fail these children, but
because their constant background chromosome noise would scramble what the trial is measuring.

An important honesty note about risk numbers: one widely-used patient source lists Wilms
tumor risk in this disease as ">85 %", while the 2024 AACR workshop paper says the disease
is too rare for accurate risk estimation. Both are quoted, and this report refuses to pick
a single number [E20][E22].

And here is the finding that quietly shapes everything below: a live census of every major
trial registry in the world (with positive controls proving the search worked) confirmed
**there is no registered intervention trial - of any kind - for MVA anywhere** [E21a].
Whatever is eventually tried for this child would be, verifiably, the first of its kind  - 
which is precisely why this report recommends nothing outside monitored gates: being first
is a reason for more controls, never fewer.

![Figure 4 - the decision map used throughout this report](figures/F4_decision_instrument.png)
*Figure 4. The decision map. Every box is a verdict that survived three research waves and four adversarial
reviews; each arrow is labeled with its condition. Source: consensus record (`evidence/TRACK2_ATTACK_MAP.md`).*

### 5b. The named repurposing candidate: everolimus - with its risks in the same paragraph
**What it is.**  Everolimus is an approved drug used for years in children with a
tumor-predisposition condition (tuberous sclerosis, TSC) to shrink specific tumors [E23].
It targets a growth-signal hub called **mTOR**.
**Why it is the only defensible name.**  Not because any study shows it helps in MVA - none
does, and we say so in every relevant sentence - but because it is the *only* drug in the
entire mapped landscape with a proven multi-year safety profile in children this young,
used chronically [E23][E23a]. Mechanistically there is a plausible (honestly labeled,
low-grade) mechanistic hope: that the drug might slow the chromosome-abnormal cells more
than the healthy ones. Honest answer: the pertinent animal evidence is two studies, and
neither shows benefit. One mouse-based study was neutral, and it was never run on
Bub1b-deficient cells [E58]. A second, newer study - a 2026 fruit-fly model of this disease
family - found the drug barely helped, and one brain measure got slightly worse. In the flies,
adding extra copies of the protective genes - genetic changes, not a medicine - restored
the brain completely; no drug of this kind has been tried in any condition of this type
[E62]. So we claim
**no** direction here; the recommendation below rests on pediatric safety data plus
monitoring, never on expected benefit. One honest closing note. After our formal review steps were finished and had found
nothing left, one more challenge to this specific recommendation still arrived - so we
went back to the original papers and checked it again, properly. A human, not the AI,
then decided to keep the recommendation, and that challenge is printed alongside it
(E62a). That same fly study
points at what we would test first in the laboratory after the gene-repair program (5c):
supporting the protein's folding machinery - which is why the validation plan tests it in
the child's own cells first (assay 5 of 6) rather than naming any drug.
**The exact, monitorable window the report names** (from the drug's own label and
trial-validated bands [E24][E25]): dose **4.5–5 mg/m²/day** (about 3.4–3.8 mg/day at
age 5), with the blood level held at **5–15 ng/mL** by regular lab checks; a
trial-validated lower band of **3–7 ng/mL** is effective in the TSC setting from about 2 years 2 months of age.
Multi-year use at exactly this age is documented (median four years, with growth and
puberty unaffected over that period [E23a]); children of ~4.7 years on the sibling drug
sirolimus even kept their vaccine responses, including live vaccines [E29].
**The honesty data that must travel with the recommendation** [E25]: in the largest trial,
the children under six had far more infections than the children six and over - every one of
them on the drug (96 % vs 67 %; serious infections 35 % vs 7 %; that trial had no untreated
group to compare with, so these are treatment-exposure numbers, accumulated over that
trial's multi-year monitoring [E23]) - and the largest
trials recorded **two treatment-related deaths, both in children**. Any family–doctor
conversation starts from *that* sentence, not from the mechanism. **Prevention precedent**
for the general idea: a 2024 trial (PREVENT) gave a rapalog *prophylactically* to
symptom-free infants in TSC and held dosing in target - the only prophylactic rapalog ever
trialed in symptom-free infants [E30]. But an honesty caveat belongs in the same breath:
PREVENT was a Phase-1 feasibility study, it did not test tumor prevention, and **no drug has
ever been shown to prevent tumors in any predisposition syndrome** (aspirin in Lynch
syndrome and metformin in Li-Fraumeni families (the MILI study, adults only) are the neighboring precedents  - 
risk-reduction signals, never proven prevention) [E45][E60].
**One real biological tension, monitored by rule:** this drug class can dampen the natural
killer (NK) immune cells that the body uses to dispose of aneuploid cells [E27][E28]  - 
ironic for this disease. The protocol therefore defines NK-count monitoring with a
pre-specified hold-dose trigger, and chooses the trial-validated low band. (Some adult-cancer
headlines suggested low "immune-boosting" rapalog doses improved older adults' vaccine
responses; that was studied in the elderly, and our evidence sweep found it does not
translate to children - so this protocol uses the trial-validated pediatric band instead [E26].)

### 5c. The precision program: patching the instruction book (exon-17 skipping)
**The idea in one breath.**  Remember the stop-sign mutation (§3a). The cell's instruction
book is read three letters at a time; the stop-sign ruins everything after it. Now the
lucky break: the stop-sign lives inside one of the gene's 23 blocks - **exon 17 - which is
exactly 141 letters long, a multiple of 3** [E42]. If a short, tailor-made molecular instruction (the drug class is called an **ASO**; more
on it below) could make the cell *skip* block 17 while copying the gene, the reading frame continues unbroken. We
computed this from the reference genome ourselves [E42] - see Figure 3.

![Figure 3 - the BUB1B gene and the skippable exon: 23 instruction blocks, block 17 highlighted red](figures/F3_BUB1B_gene_exon17.png)
*Figure 3. The 23 instruction blocks of BUB1B; the stop-sign sits in block 17 (red), whose
length happens to be divisible by three. Source: Ensembl MANE transcript (live fetch, cached).*

**Does this drug class exist?**  Yes - "splice-switching" drugs (ASOs) are approved for
other genetic diseases, including in very young children (muscular dystrophy
[eteplirsen class], spinal muscular atrophy [nusinersen]) [E34]; and a specialized
"n-of-1" ecosystem now builds such drugs for single ultra-rare patients: the proof of
concept, milasen, went from diagnosis to the child's first dose in **under 12 months**;
the foundation that industrialized this path prices the full per-patient journey at roughly
$1M for life, mostly philanthropically financed [E31][E32]. The original chemistry patents
have expired [E33].
**Before the problems, one "why":** why is delivery even a problem, if muscle and spinal
cords are already reachable by this drug class? Because the chromosome instability lives in
*every* tissue of a child with MVA - these children's cancers have arisen in kidney, muscle,
and elsewhere - so a drug reaching only muscle or spinal cord would cover, at best, a
fraction of the risk.
**The two honest problems:**
1. **The patched protein must actually work.** Skipping block 17 removes the 46 building
   blocks it encodes (the chain from position 716 through 761) and changes one neighbor
   (position 715) - in scientific shorthand "Δ716-761 + E715G" [E42]. No one has tested
   whether that shortened BubR1 is functional. Worse - the patch is *not* mutation-specific:
   it would skip exon 17 in the child's *other, shape-mutated copy too*. Our back-of-envelope
   arithmetic (assumptions documented in the evidence pack) estimates that if the shortened
   protein works, benefit lands at ~16–22 % of normal levels - an estimate, not a measurement  - 
   above the ~13 % competence line; and if it doesn't, the patch would break the remaining
   copy too [E40-P2]. **That is exactly why the program's first step makes the shortened
   protein in a lab dish and checks whether it works - before any child anywhere touches it**
   (assay #4 in §6).
2. **Delivery is unprecedented.** No approved ASO has ever been shown to fix splicing in
   *whole-body / non-muscle, non-brain* tissues in humans; muscle and spinal-cord delivery
   are proven, everything else is not [E36] (a small-molecule class that *is* systemic,
   risdiplam [E37], shows the concept can reach the body - but engineering a small
   molecule from scratch is a longer road).
**Verdict:** the primary precision *research* program - correct, powerful, honest about its
single decisive unknown.

### 5d. Adjuncts (behind lab assays only)
- **Arimoclomol**: an approved booster of the cell's own stress-defense machinery (the
  heat-shock response), with pediatric chronic use from age 2.
  It is *conceivable* it stabilizes the fragile copy - but no study has ever shown such
  drugs raise a mutant kinase's levels; one flagged hazard (its amplified pathway can itself
  spark aneuploidy [E52]) keeps it **adjunct-only, behind abundance assay #5** [E50][E51].
- **NMN (vitamin-B3 pathway)**: a mouse study found boosting NAD⁺/SIRT2 biology raised
  BubR1 levels - the only documented chemical lever on this protein's abundance [E54]; but
  our own candidate sweep also weighed the *opposite* chemistry - drugs that block SIRT2  - 
  and ruled it dangerous, because the chemical marks it would strip are checkpoint-protective
  [E55]. So: **SIRT2 inhibitors are off-limits**, full stop. Watch status; cheap cell
  test alongside assay #5. Overdosing the other direction has its own cancer-linked risk  - 
  a target window, not a ceiling [E59a].
- **Metformin**: only a ≤100 µM dish-level co-test remains (high doses demonstrably
  *damage* checkpoint regulation [E59]).

> **For families reading this section:** nothing here is a home treatment. NMN is sold over
> the counter and metformin is a common prescription drug - but giving either (or any other
> substance named in this report) to a child with MVA, outside supervised laboratory gates
> and medical oversight, is exactly the unmonitored action this report exists to prevent.
> If you are a parent, bring this section to the care team; never act on it yourself.

### 5e. Senolysis - the mouse-to-child gap, framed honestly
In a famous 2011 experiment, clearing "aged" cells from BubR1-deficient mice prevented
their tissue decline [E05]. One caution: that landmark result comes from a single
laboratory; a later experiment by the same lab, in ordinary aging mice, did not repeat it
[E07] - and no independent laboratory has ever reproduced it. The idea remains the only *genotype-matched* preclinical proof in this
field. What our deep check added: **pediatric experience with the senolytic drug class does
exist after all** (navitoclax, in cancer-treatment regimens from age 4 [E16]) - a genuine
feasibility upgrade nobody had; a proven intermittent dosing pattern in adults [E14]; and a
thorough census showing **no evidence anywhere that clearing senescent cells increases
tumor incidence** [E07][E08][E09] (the opposite fear our advisers raised). What still
doesn't exist: any senescence measurement in MVA patient tissue, and any pediatric
senolytic *indication*. Therefore: **research-priority only, behind the patient-cell
Gate-0 assay and pre-specified malignancy stop-rules.**

### 5f. Do NOT use, for this child - documented exclusions
- **HSP90 inhibitors (17-AAG class)**: the fragile shape-mutated copy very likely depends
  on the HSP90 chaperone to hold its fold; cutting that lifeline would degrade the
  patient's remaining protein - a genotype-specific hazard *against* the general
  anti-aneuploidy rationale this drug class carries [E39][E17a]. The door that is closed is the one that *removes* chaperone help, not the one that
  adds it (see 5b: supporting the fold is a test-first research axis). The clearest closed door
  in the whole analysis.
- **KIF18A, TRIP13, and direct SAC (Mps1) inhibitors**: biologically wrong direction  - 
  weakening the checkpoint further in a child whose checkpoint already runs on too little
  BubR1; TRIP13 loss *causes*
  a related MVA type [E20b].
- **Autophagy-manipulation drugs (chloroquine family)**: no pediatric justification in a
  pre-malignant setting; class contradictions recorded [E40].
- **Celastrol / proteasome-based stabilizer ideas**: closed on toxicity or dependency
  direction [E40].
- **AICAR/energy-stress axis**: closed - the 2011 paper behind it tested only compounds
  with no pediatric-feasible member on that genotype, and kill-selectivity tracked cell
  aneuploidy, not the carrier state [E58].
Full table: candidates.tsv in the evidence pack (19 rows, each with its verdict and reason).

## 6. What has to be proven *in a laboratory* before anything is given
Everything below fits inside routine ethics-committee consent; none invades the child.
1. **Gate-0 - the patient's own cells**: senescence burden + aneuploid fraction + immune
   panel (baseline for every downstream decision) [E14][E17].
2. **NMD-escape fraction** of the stop-sign copy - a blood-RNA count that asks whether
   even a little of the broken copy's protein slips past the cell's recycling system  - 
   decides whether any drug direction targeting the stop-sign is even discussable [E42].
3. **Stability of the shape-mutated copy**: a standard "label-and-watch" experiment (a
   so-called pulse-chase) that times how quickly the fragile protein is destroyed - a direct
   test of the degradation prediction [E39].
4. **★ The decisive experiment**: build the Δ716-761+E715G patched protein and test
   does it appear in cells at all, does it hold its shape, does it reach the protein's
   workstation at the chromosomes, **and** does it restore the checkpoint function. This one
   assay decides the entire exon-skipping program [E40-P2][E44a].
5. **Abundance ± arimoclomol (± NMN)**, with an HSP90-inhibitor pulse as the positive
   control for degradation - directly calibrates every §5d adjunct [E50][E54].
6. **Checkpoint-timing test of where the child actually sits on the 6 → 13 % competence
   curve**: a standard live-cell test that measures how long the checkpoint holds before
   cells slip through division ([E04]; laboratories call it a mitotic-escape assay).

## 7. What we are NOT claiming (read this before anything else)
- No drug is proven to prevent, treat, or slow MVA or its cancers - in this child or anyone.
- Everolimus is proposed **inside surveillance + gates**, not as a prescription.
- The exon-skipping program is a research plan, not a therapy; its decisive experiment has
  never been run.
- "No evidence located" statements in this report mean *searched and not found* (queries
  recorded), never "proven impossible".
- Sources were verified as of **2026-09-05** and re-checked against the live
  trial registries and literature on **2026-09-09**: nothing in this report
  changed; the RAVEN children's trial entry now includes its posted results.

## 8. Where we stand, and how sure we are

**Where we stand (2026-09-05).**  The evidence program behind every verdict in §5 is
*complete to its own stopping rule*: three research waves, 19 verified research memos,
four adversarial reviews with measured error-decay 8 → 2 → 2 → 0 (Figure 5),
and a frozen, fully-traced decision record [E40][E41]. By our own rule, a person - never
the AI - reviews and signs off on this report before it is used anywhere.
(Competition housekeeping - what we submit, deadlines, remaining work - has been moved to
§12, out of your way.)

**How sure are we?**  Honest calibration, itemized:
- Surveillance standard, exclusion list, "no MVA trial exists", allele math, exon-17
  geometry: **high confidence** (multiple independent verifications each; adversarially
  survived).
- **On everolimus, in plain words.** We are confident the *decision rule* is sound  - 
  "name it, but only inside monitoring and stop-gates" - because that rule leans mainly on
  well-documented safety data and the trial-validated pediatric window. The evidence that
  the drug would actually *help against this disease* is weak - laboratory-level at best;
  no study in people with MVA has ever tested this drug; the only experiment in an
  animal model of this disease family leaned slightly against (see 5b). Both
  sentences are true at once, and the second never travels
  without the gates.
- Δ716-761+E715G function: **decidable but UNMEASURED** - by design the claim is
  conditional on assay #4.
- **What can go stale before submission** (drug approvals, trial statuses, screening
  guidelines): every time-sensitive claim will be re-checked in one scheduled
  pre-submission sweep (step 2 above).

## 9. The figures, in one place
- **Figure 1** - where the shape mutation sits (human AlphaFold + fly crystal):
  [figures/F1_variant_structure.png](figures/F1_variant_structure.png)
- **Figure 2** - protein map (UniProt-driven bands + 3-D render):
  [figures/F2_BubR1_protein_map.png](figures/F2_BubR1_protein_map.png)
- **Figure 3** - the gene and the skippable exon (§5c above).
- **Figure 4** - the decision map (§5a above).
- **Figure 5** - how the evidence was stress-tested (adversarial decay + verification):

![Figure 5 - consensus stress-test](figures/F5_consensus_process.png)
*Figure 5. Left: majors found per independent adversarial pass (the pre-declared stop rule
met at zero). Right: identifier verification per wave (all sampled sources resolve to real
papers). Source: evidence/WORKFLOW_CONSENSUS.md changelog.*

![Figure 1 - where the second mutation sits](figures/F1_variant_structure.png)
*Figure 1. Left: human BubR1 kinase domain - a computer-predicted structure of the normal,
healthy protein - with residue 1002 marked red (the position of the child's shape mutation,
which is not modeled in this picture) and a neighboring regulatory switch-point (T1008) in
magenta. Right: the fruit-fly crystal structure (6JKK), measured in a real laboratory
experiment, where the equivalent residue touches its partner within 2.9 Å - validating that
this exact spot is load-bearing across 600 million years of evolution. Source:
`evidence/STRUCTURAL_VALIDATION.md`; PyMOL render.*

![Figure 2 - the protein map](figures/F2_BubR1_protein_map.png)
*Figure 2. BubR1's four parts (colors = UniProt feature table), the two mutation
positions, and the 3-D view of the folded core. Source: UniProt O60566 + AlphaFold model.*

## 10. References (every claim's source, with its verification trail)

Convention: **[E#]** in the text → entry below. Internal artifacts ("evidence pack") are
files under `evidence/` in this repository, all content-verified through multiple passes;
external sources carry the link and how/when it was verified. PMID links:
pubmed.ncbi.nlm.nih.gov/&lt;PMID&gt;/.

**The case & the diagnosis**
- **E01** Challenge case document (genotype: BUB1B p.Leu737Ter + p.Asn1002Lys). File
  Challenge_Clinical_Phenotype_1.docx, dataset page (gated):
  https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data · read 2026-08-31.
- **E18** Hanks et al. 2004 - discovery that biallelic BUB1B mutations cause MVA. *Nature
  Genetics* 36:1159-61. https://doi.org/10.1038/ng1449 · verified via PubMed/DOI, 2026-09-05.
- **E20** GeneReviews - BUB1B-related MVA (NBK1294); risk-figure source.
  https://www.ncbi.nlm.nih.gov/books/NBK1294/ · read 2026-09-05.
- **E20b** Yost et al. 2017 - TRIP13 mutations cause related MVA/Wilms predisposition.
  https://doi.org/10.1038/ng.3883 · verified 2026-09-05.

**The biological mechanics**
- **E04** Suijkerbuijk et al. 2010 - patient-cell checkpoint dose-response (~13 % competent
  / ~6 % failing); kinase-activity question. *Cancer Research* 70:4891-900. PMID 20516114.
  https://pubmed.ncbi.nlm.nih.gov/20516114/ · verified + scite-graded 2026-09-05.
- **E04b** Catalysis-dispensable cluster: Malureanu 2009 (PMID 19154723), Suijkerbuijk 2012
  pseudokinase (PMID 22698286), Breit 2015 (no in-vitro catalysis, PMID 26658523).
  https://pubmed.ncbi.nlm.nih.gov/19154723/ · https://pubmed.ncbi.nlm.nih.gov/22698286/ ·
  https://pubmed.ncbi.nlm.nih.gov/26658523/ · verified 2026-09-05. (evidence pack: MECHANISM_G1)
- **E17** Santaguida et al. 2017 - newly aneuploid/senescent untransformed cells are
  NK-cleared. https://doi.org/10.1016/j.devcel.2017.05.022 · verified 2026-09-05.
- **E17a** Park et al. 2013 - BUBR1 K243-acetylation site is checkpoint-protective; mutant
  mice degrade BubR1 and develop tumors. https://pubmed.ncbi.nlm.nih.gov/23878276/ ·
  verified 2026-09-05.
- **E19** Wang et al. 2021 - NF-κB central to NK clearance of aneuploid senescent cells.
  https://doi.org/10.15252/embr.202052032 · verified 2026-09-05.
- **E39** Structural validation of the N1002 position - repo artifact
  STRUCTURAL_VALIDATION.md (AlphaFold model AF-O60566
  https://alphafold.ebi.ac.uk/entry/O60566; fly crystal 6JKK
  https://www.rcsb.org/structure/6JKK; 2.86 Å contact measured from the deposited
  coordinates in `evidence/STRUCTURAL_VALIDATION.md`). Verified
  2026-09-05.
- **E42** Nonsense/NMD/exon-17 analysis - repo artifacts wave2_NonsenseAxis.md +
  q7a_sequence_analysis.md (exon 17 = 141 nt in-frame; 75 nt from junction → canonical NMD
  substrate; UGAA context; readthrough-yield model). Exon data:
  http://www.ensembl.org/Homo_sapiens/Transcript/Summary?t=ENST00000287598 · 2026-09-05.
- **E38** AlphaMissense pathogenicity scoring (0.9229 for N1002K, computed in our variant
  panel): Cheng et al. 2023, *Science*. https://pubmed.ncbi.nlm.nih.gov/37733863/ ·
  pipeline artifact VARIANT_PROTEIN_IMPACT.md.

**Surveillance & prevention precedents**
- **E21** Hol JA, Jongmans MCJ, et al. 2021 - SIOP-RTSG/EEPGN Wilms-tumour surveillance in
  at-risk children (renal US q3mo birth→7 for defined syndromes). *Eur J Cancer* 153:51–63.
  https://doi.org/10.1016/j.ejca.2021.05.014 · PMID 34134020 · verified against
  wave4_SurveillanceToday.md §1.2, 2026-09-05. (Earlier entry mis-pointed to
  10.1016/j.pediatrneurol.2021.07.011 - the Northrup TSC-criteria paper; corrected.)
- **E22** Nakano et al. 2024 - AACR 2nd Childhood Cancer Predisposition Workshop update,
  genomic-instability disorders (endorses the same cadence). PMID 39264246.
  https://pubmed.ncbi.nlm.nih.gov/39264246/ · verified 2026-09-05.
- **E21a** Live registry census (ClinicalTrials.gov, CTIS, EU-CTR, ISRCTN, ANZCTR with
  everolimus positive controls): **zero MVA-specific intervention trials/registries**  - 
  repo artifact wave4_SurveillanceToday.md (query log + API dates 2026-09-05).
- **E47** Kuhlen 2026 + CHARM2 trial NCT06726642 (cfDNA RCT; MVA/CIN exclusion verified
  live). https://clinicaltrials.gov/study/NCT06726642 · evidence pack wave4 doc.
- **E30** Capal et al. 2024 - PREVENT: prophylactic sirolimus in TSC infants (94 % of
  troughs in target). PMID 39726432. https://pubmed.ncbi.nlm.nih.gov/39726432/ · verified.
- **E45** CAPP3 first results 2026 - Lynch aspirin dose study; **NOTE correctly scoped**
  (no formal non-inferiority per the trial's rule; 100 mg similar risk, less bleeding).
  PMID 42425127 · https://pubmed.ncbi.nlm.nih.gov/42425127/ · scoping verified by adversarial
  pass 2.
- **E46** Rüschoff et al. - aspirin mechanism in Lynch (antiplatelet/anti-inflammatory,
  not MMR/CIN-directed). PMID 9736731. https://pubmed.ncbi.nlm.nih.gov/9736731/ · verified.

**Everolimus / rapalog facts**
- **E23** French et al. 2016 - EXIST-3 (everolimus in TSC, incl. low-exposure 3–7 ng/mL
  band ≥2.2 y). *Lancet*, PMID 27613521. https://pubmed.ncbi.nlm.nih.gov/27613521/ ·
  band attribution re-verified adversarially (P3-1).
- **E23a** Franz et al. - EXIST-1 final analysis (median 47 months exposure; growth/puberty
  unaffected); Kotulska 2013 (children <3 y, 35-month follow-up). PMID 27351628 ·
  https://pubmed.ncbi.nlm.nih.gov/27351628/ · PMID 23567018
  https://pubmed.ncbi.nlm.nih.gov/23567018/ · verified 2026-09-05.
- **E24** FDA label - Afinitor/Afinitor Disperz (dose 4.5-5 mg/m² titration, trough
  5-15 ng/mL, monitoring calendar, age-stratified infections). DailyMed:
  https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=afinitor · read via label text in
  wave4_PediatricRapalogDosing.md.
- **E25** EXIST-3 safety incl. <6 y infection strata and two treatment-related pediatric
  deaths. PMC full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC6276348/ · quoted datum
  verified verbatim by independent adversarial pass 3.
- **E26** Mannick et al. 2018 - low-dose mTOR inhibition ENHANCES vaccination responses in
  elderly adults (why we cannot transplant the regimen to a child, documented & hypothesized).
  https://pubmed.ncbi.nlm.nih.gov/29997249/ · verified 2026-09-05.
- **E27** Marçais et al. 2014 - mTOR is essential for NK-cell function (mouse AND human).
  https://doi.org/10.1038/ni.2936 · scite-graded s65/c2.
- **E28** Besson et al. 2021 - everolimus contracts peripheral NK pool in adults.
  https://pubmed.ncbi.nlm.nih.gov/33931486/ · verified.
- **E29** Yuan et al. 2025/2026 - children ~4.7 y on sirolimus retain vaccine
  immunogenicity (incl. live MMR). PMID 41012109 · https://pubmed.ncbi.nlm.nih.gov/41012109/
  · PMID 42154819. Verified; flagged single-region cohorts.

**The exon-skipping / ASO program**
- **E31** Kim et al. 2019 - milasen: diagnosis-to-dosed-patient <12 months for an
  individualized ASO. *NEJM*, PMID 31597037. https://pubmed.ncbi.nlm.nih.gov/31597037/ ·
  full text reviewed (PMC6961983).
- **E32** Crooke et al. 2026 - the n-Lorem model (~$1M/lifetime, >30 INDs, splice-ASO
  fraction). https://doi.org/10.1093/nar/gkag504 · verified.
- **E33** PMO core chemistry patent US 5,185,444 - status Expired-Lifetime.
  https://patents.google.com/patent/US5185444A/en · status checked live 2026-09-05.
- **E34** Splice-switching approved precedents (eteplirsen/viltolarsen/golodirsen class  - 
  muscle; nusinersen - spinal), pediatric. Census references in wave3_ASOdeep.md
  (all identifiers join-checked).
- **E36** Delivery census verdict - no human non-muscle/non-CNS ASO splice correction
  (oligonucleotide limb), corrected scope per negation re-attack. wave3_ASOdeep.md +
  wave4_NegationReattack.md.
- **E37** Risdiplam - approved oral small-molecule systemic splice modifier (blood-level
  SMN2 splicing pharmacodynamics in humans, incl. children). PMID 30302786.
  https://pubmed.ncbi.nlm.nih.gov/30302786/ · verified 2026-09-05; branaplam noted WITH its
  adverse datum (early termination for peripheral neuropathy, 85.7 %  - 
  https://doi.org/10.1038/s41591-025-04117-4).

**Senolysis**
- **E05** Baker et al. 2011 - clearing p16+ senescent cells in BubR1-hypomorphic mice
  (genotype-matched mouse proof). https://pubmed.ncbi.nlm.nih.gov/22048312/ ·
  single-lab flag + scite-graded.
- **E07** Baker et al. 2016 - WT-background natural-aging repeat; **full text verified**:
  no tumor-incidence change, increased latency, NK populations unchanged.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC4845101/ · verified by pass-3 arbiter.
- **E08** Lalinde-Gutiérrez et al. 2026 - early senolysis accelerated PyMT tumors
  (macrophage/CCL2; late = protective): the real timing counterweight.
  https://doi.org/10.1126/sciadv.adx2988 · verified.
- **E09** Protective census: Haston et al. 2023 (PMID 37267953,
  https://pubmed.ncbi.nlm.nih.gov/37267953/); Ming et al. 2025 (PMID 39623223
  https://pubmed.ncbi.nlm.nih.gov/39623223/); Zhou et al. 2026
  (https://doi.org/10.1158/2159-8290.CD-25-1212); census log in wave3_SenolysisF6verifier.md.
- **E14** Intermittent-dosing pattern: Justice et al. 2019 (PMID 30616998,
  https://pubmed.ncbi.nlm.nih.gov/30616998/) + Xu et al. 2018 hit-and-run (PMID 29988130,
  https://pubmed.ncbi.nlm.nih.gov/29988130/) · verified.
- **E15** Gore et al. 2018 - dasatinib pediatric experience (n=113, leukemia-schedule).
  https://pubmed.ncbi.nlm.nih.gov/29498925/ · verified.
- **E16** Pullarkat et al. 2021 - **pediatric navitoclax exposure** (combination regimens,
  RP2D 25 mg <45 kg). PMID 33593877. https://pubmed.ncbi.nlm.nih.gov/33593877/ · NCT03181126 live registry; RAVEN NCT05192889
  (ages 4-30, actively dosed). **This overturned our own earlier "zero pediatric senolytic"
  claim - kept on record as the correction that made the axis honest.**

**Stabilization & abundance chemistry**
- **E50** Arimoclomol (Miplyffa) - US FDA approval 2024 (with miglustat, NPC; children ≥2 y).
  FDA press + label, verified 2026-09-05 (wave2_StabilizationAxis.md).
- **E51** Kirkegaard et al. 2016 - arimoclomol mechanism = lysosomal HSP70 support
  (the actual proven action). PMID 27605553. https://pubmed.ncbi.nlm.nih.gov/27605553/ ·
  verified.
- **E52** HSF1–Cdc20 hazard - HSF1 overexpression binds Cdc20, inhibits APC/C, produces
  aneuploidy. PMID 18059335. https://pubmed.ncbi.nlm.nih.gov/18059335/ · verified 2 passes.
- **E53** Arimoclomol ALS phase-3 failure (efficacy outside lysosomal disease unproven).
  PMID 38782015. https://pubmed.ncbi.nlm.nih.gov/38782015/ · verified.
- **E54** North et al. 2014 - SIRT2/NAD⁺ raises BubR1 abundance in vivo (exact hypomorph
  mouse). https://doi.org/10.15252/embj.201386907 · verified 2026-09-05.
- **E55** (see E17a) - the site-dependence that makes SIRT2 *inhibition* prohibited chemistry.
- **E56** Irie et al. 2020 - NAD⁺-precursor human safety RCT (adult). PMID 31685720.
  https://pubmed.ncbi.nlm.nih.gov/31685720/ · verified.
- **E57** Bursch 2024 - no selective SIRT2-activator compound exists.
  https://doi.org/10.3390/molecules29051185 · verified.
- **E59** Lyu et al. 2022 - metformin at mM doses deregulates BUBR1/MAD2 (genotoxic;
  grounds the ≤100 µM cap). PMID 35568294. https://pubmed.ncbi.nlm.nih.gov/35568294/ · verified.
- **E59a** BUB1B overexpression drives chemo-resistance (the abundance target is a window,
  not a ceiling). https://pubmed.ncbi.nlm.nih.gov/34545188/ · verified (negation re-attack).

**Closed axes**
- **E58** Tang et al. 2011 - mTOR arms neutral on trisomic MEFs (never tested on Bub1b^H/H
  cells); AICAR arm killed aneuploid-fraction-high cells. *Cell*, **PMID 21315436** (the
  corrected identifier - an earlier mis-citation of 21546338 remains deleted from all
  artifacts). https://pubmed.ncbi.nlm.nih.gov/21315436/ · full-text verified twice.
- **E60** MILI trial protocol - metformin prevention in Li-Fraumeni (adults ≥16; mechanism
  differs - does not transfer to CIN precedent). https://doi.org/10.1186/s13063-024-07929-w ·
  verified.

**Readthrough (closed as primary)**
- **E61** EMA EPAR page, ataluren/Translarna (non-renewal 2023 status as of fetch).
  https://www.ema.europa.eu/en/medicines/human/EPAR/translarna · status verified 2026-09-05;
  FDA CRL 2025 + NDA-resubmission withdrawal 2026 per PTC Therapeutics announcement
  (verified live in adversarial pass 3); modeled-yield analysis in wave2_NonsenseAxis.md.

**Animal-model honesty datum (adjudication)**
- **E62** González-Blanco et al. 2026 - fruit-fly model of this chromosome-instability
  disease family (bub3/rod knockdown); rapamycin marginal-to-negative on brain measures;
  chaperone/ROS rescue complete. *Nature Communications* 17:3829.
  https://doi.org/10.1038/s41467-026-70521-0 · PMID 41820377, PMC13121444 · verified 2026-09-12 via PMC full text plus the authors' own Source Data workbook.

**Process & provenance (incl. post-closure re-adjudication)**
- **E62a** Post-closure re-adjudication of the everolimus candidate anchor (separate,
  deliberately declared, *not* a fifth adversarial pass). Internal artifacts in the
  evidence pack: evidence/adjudication_rapalog_contested_anchor.md (integrated memo and
  human-decision record: the coordinator kept the candidate with its disclosure box,
  Option A) + the three wave briefs evidence/cycle1_nk.md, evidence/cycle1_fly.md,
  evidence/cycle1_mech.md (verbatim primary-source quotes and per-source verdicts).
- **E40** evidence/WORKFLOW_CONSENSUS.md (+ adversarial pass memos wave2/3/4/5_ADVERSARIAL*.md):
  3 waves, 19 memos, decay 8→2→2→0, 90/90 identifiers registry-verified (32+34+24 across the waves); P2/P3/PR fix tags, PR = lay-report review fixes.
- **E40-P2** wave2_ADVERSARIAL_REVIEW.md - the allele-non-specificity analysis + KARD
  off-by-one caution (F1/F2) that made the ASO section honest.
- **E40-SD** evidence/SCOPE_DECISION.md - options, deterministic weighted matrix (O1 = 88.6,
  rank-stable under ±20 % weight perturbations), decision log + revisit record.
- **E41** wave5_ADVERSARIAL_PASS4.md - final independent review returning zero majors
  (closure document).
- **E44** Competition: challenge space https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026
  && dataset https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data · submission
  window 2026-08-24 → 2026-10-24, scite partnership terms (per organizer pages).
- **E44a** Assay #4 specification: evidence/TRACK2_ATTACK_MAP.md §Validation plan; construct details
- **E73** MVA Society and Unique, *Mosaic variegated aneuploidy syndrome 1 (BUB1B)* guide, 2026, reviewed by a consultant in clinical and paediatric genetics. Says no clinical practice guidelines exist for this genotype, and recommends abdominal ultrasound every three months plus a blood check every three months to detect leukaemia. A family guide, not a formal guideline. https://mvasociety.org/wp-content/uploads/2026/07/MVA-BUB1B-guide.pdf
- **E74** Japanese national management handbook for PCS/MVA syndrome, March 2017, Health Labour Sciences Research Grant: schedules abdominal ultrasound and a full blood count at every visit from three months of age into adulthood. https://raredis.nibn.go.jp/malformation/management_guidelines_notebook/32.pdf
- **E75** Maese et al. 2024, *Clinical Cancer Research*, AACR surveillance update for children predisposed to blood cancers. Cited for a verified absence: its full text names neither this syndrome nor any of its genes. https://doi.org/10.1158/1078-0432.CCR-24-0685
- **E76** Laberko et al. 2019, *Orphanet Journal of Rare Diseases*, the only reported stem cell transplant in this syndrome, in a child with myelodysplasia and monosomy 7; graft rejection at day +47 and death at day +156. https://doi.org/10.1186/s13023-019-1073-x
  Δ716-761 + E715G with KARD-boundary caution (wave3_ASOdeep.md §(a)).

## 11. Glossary (every technical word in this report)

**Allele** - one of the two inherited copies of a gene (one from mother, one from father).
**Amino acid** - the 20 kinds of building blocks proteins are assembled from; BubR1 is a chain of 1050.
**Aneuploidy** - the wrong number of chromosomes in a cell.
**ASO (antisense oligonucleotide)** - a short synthetic DNA-like molecule that can steer how a gene's instruction blocks are assembled.
**Checkpoint (SAC)** - the cell-division quality-control checkpoint; see *SAC* below.
**Chromosome** - one of the 46 bound volumes the genome's instruction book comes in; every new cell must receive exactly one copy of each.
**CIN (chromosomal instability)** - an ongoing rate of chromosome-count errors.
**cfDNA / liquid biopsy** - fragments of DNA floating in blood that can carry tumor signals.
**Conserved** - kept unchanged by evolution across species; usually a sign of importance.
**Euploid** - having the correct chromosome count ("euploid cells" = the chromosome-normal ones).
**Exon** - one instruction block of a gene (genes are read block by block).
**Exon skipping** - chemically persuading the cell to omit one block while copying, to dodge a defect.
**Gate-0** - our mandatory first lab check on the child's own cells before any drug discussion.
**In-frame** - when a removed block's letter count is divisible by 3, the three-letter reading rhythm survives.
**Kinase** - a protein that adds phosphate tags to other proteins (a molecular switch).
**Mosaic** - made of a mixture; here, a body whose cells have varying chromosome counts.
**mTOR** - a master growth-signal protein; everolimus partially brakes it.
**NK (natural killer) cells** - immune cells that seek and destroy damaged or abnormal cells.
**NMD (nonsense-mediated decay)** - the cell's recycling of messages that contain a premature stop-sign.
**n-of-1** - a drug or trial designed for a single patient.
**Nonsense mutation** - a spelling change that writes a premature "STOP".
**PK (pharmacokinetics)** - how the body absorbs, distributes, and clears a drug.
**Protein** - a working molecular machine assembled from amino acids; BubR1 is one.
**qPCR / ddPCR** - lab tests that count how much of a molecule is present.
**Reading frame** - the three-letter rhythm in which the gene's text is read; shifting it scrambles everything after.
**RP2D** - recommended phase-2 dose (the dose a pediatric trial picks).
**SAC (spindle assembly checkpoint)** - the division quality-control checkpoint.
**SASP** - the inflammatory secretions of aged (senescent) cells.
**Senescence** - the biologically "aged" state cells enter after damage or stress.
**Senolysis** - clearing senescent cells with drugs.
**Systemic** - reaching the whole body (as opposed to one organ).
**TDM** - therapeutic drug monitoring: measuring the drug's blood level.
**TSC** - tuberous sclerosis complex (the pediatric precedent disease).
**Trough** - the lowest blood level of a drug between doses (ng/mL).
**Whole-exome/genome sequencing** - reading the protein-coding, or full, genome of a patient.

## 12. Provenance, method, and AI-use disclosure

**Submission housekeeping (moved out of §8 for readability).** Submission-period deadline:
2026-10-24 [E44]. Next steps, in order: (1) human review and sign-off of this report;
(2) one pre-submission freshness sweep re-checking time-locked claims (rules, trials,
guidance), scheduled mid-October; (3) Track 1 genome-interpretation pipeline on the
challenge's 85 GB sequence dataset (infrastructure already staged on the compute host);
(4) assemble the formal Track-2 submission from this evidence tree - the §5 layered
answer (surveillance backbone; **everolimus** named inside gates with every honesty
datum; **exon-17 skipping** as the precision research program with its decisive assay;
the documented DO-NOT-USE list; the 6-assay validation plan) was selected in a structured
comparison of four candidate architectures (weights and scores in SCOPE_DECISION.md,
§10 E40-SD), and the choice stayed the same under every tested weighting assumption;
(5) if wet-lab access materializes: Gate-0 + assay #4 are first.
- All scientific content derives from the evidence pack in `evidence/` (manifest
  `MEMO_MANIFEST.md`): literature sweeps, mechanism/phenotype loops,
  variant/structural analyses, three research waves with recorded query logs, four
  adversarial reviews, and the consensus decision record. Nothing here asserts a fact beyond those artifacts; editorial corrections visible
  inline as [P2-#]/[P3-#] tags.
- Figures: committed PNGs in `figures/`, generated from the data sources named in each
  caption.
- **AI use**: research memos and adversarial reviews were drafted by AI agents inside one
  hosted lineage (e-INFRA Kimi-class; reviewers separated by role and fresh context, not
  by vendor) with deterministic identifier verification; source texts of primary papers were used by those
  agents where stated. This lay report was drafted by an AI assistant and requires
  human review & approval prior to any submission (per the challenge's methods/AI
  disclosure rule, to be completed at submission time).
- **No patient-identifying information appears anywhere in this document.**

---

*End of report - version 1.1 - post-review integrated draft for human review.*
