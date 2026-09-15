# Consensus research workflow (standing procedure) - MVA Track 2

Adopted 2026-09-05 per user directive: when undecisive, fan out across every
available research tool, review, and vote by consensus - engineered as a graph
of loops (skill://graph-engineering + skill://loop-engineering applied; both
read 2026-09-05 and baked in below).

## Org graph (policy)

| Node | Role | Tooling |
|---|---|---|
| Searchers (≤4 concurrent, e-INFRA cap) | Axis-deep evidence loops (observe→reason→act→verify each) | scite (Smart Citations) + pubmed MCP + paperclip (full text/verification) + database-lookup + ddg |
| Join verifier (deterministic) | Check every claim's PMID/DOI resolves; schema-validate candidates.tsv | local pandas/pubmed spot-check |
| Adversarial reviewer | Out-of-family red team on the merged evidence + attack map | kimi (deliberately different model family) |
| Consensus integrator | Update candidates.tsv + TRACK2_ATTACK_MAP.md per rules below | controller (Main) |
| Human gate | Any submission, any clinical statement | user |

## Work graph (execution procedure)

1. **Wave N dispatch**: ≤4 searcher nodes, each with explicit contract
   (Target/Change/Acceptance), termination criterion declared up front,
   artifacts to files, sequential tool calls inside each node.
2. **Join**: verify every load-bearing claim's identifier resolves
   (deterministic spot-check ≥5 per wave document) before the document
   enters the consensus pool.
3. **Adversarial pass**: kimi reviews merged memos against these failure
   modes: human/mouse conflation, retracted/corrected sources, dose-context
   mismatch with pediatric chronic setting, survivorship of contradictions,
   inferences silent-labeled.
4. **Consensus voting (per candidate/axis)**:
   - ADMIT: ≥2 independent verified supporting sources, survives adversarial
     critique, pediatric-feasibility class recorded.
   - DOWNGRADE: single-study or mouse-only → research-priority framing.
   - EXCLUDE: any verified contradicting evidence or genotype-specific
     hazard (HSP90i precedent); exclusion rationale preserved verbatim.
   - Every change to candidates.tsv cites the wave document + tallies.
5. **Durable state**: this file + TRACK2_ATTACK_MAP.md +
   candidates.tsv (versioned in submission repo); agent_logs/architecture.md
   for Track 1; nothing lives only in conversation.
6. **Hill-climbing**: after each wave, record what failed/surprised into
   this file's changelog; adjust searcher contracts next wave.

## Changelog
- 2026-09-05 wave-1 dispatched: NonsenseAxis / StabilizationAxis / SenolyticAxis /
  CINSyndromeAxis (4/4 slots). Triggers: exon-17 in-frame discovery (ASO route),
  arimoclomol 2024 pediatric-HSF1 recency, senolysis mouse-only gap,
  CIN-syndrome prevention-precedent gap.
- 2026-09-05 wave-1 JOIN passed (32/32 DOIs registry-verified); kimi adversarial: no blockers, 5 ACCEPT-WITH-CONDITIONS; 13 conditions incorporated (recounted 8 majors incl. F3,F13 per pass-2 P2-5/pass-3 P3-7; the five listed here were the top-severity subset: ASO allele-non-specificity math, KARD off-by-one, Lynch-aspirin CAPP2 scope fix, NMN/SIRT2 completeness fix, Tang-2011 AMPK reopen + senolysis tumor-suppression objection). SURPRISES worth keeping the red team for: every wave doc independently missed CAPP2; "exactly one node" claims are always wrong until the adversarial pass runs. Scrubbed leaked generation token from wave2_CINSyndromeAxis.md (F10). Consensus applied: candidates.tsv v2 (19 rows + consensus_status), TRACK2_ATTACK_MAP.md v2.
- 2026-09-05 wave-2 dispatched (PrecedentCensus / AMPKaxis / ASOdeep / ImmunoSurveillanceNK) targeting adversarial-forced gaps and two omission axes found by controller scan (NK-immunosurveillance; base-editing deferred as delivery-infeasible today). Loop-count decision recorded: stop rule = zero-major adversarial pass + zero-major confirmation pass over fresh axes; expected 2 more passes, hard ceiling 3 SEARCH WAVES (4 adversarial passes counting the closure pass). Strategy decision aid executed per scientific-brainstorming (deterministic matrix CLI): O1 rank-1 at 88.6, rank-stable [1,1] under ±20% weight perturbations; O2/O3 rejected on repurposing-compliance gate. SCOPE_DECISION.md written; awaiting wave-2 for scheduled re-evaluation.
- 2026-09-05 adversarial pass 2 (kimi, over wave-2 pack + controller integrations): 2 MAJOR / 7 MINOR / 0 blockers. BOTH majors were controller-layer (integration-fidelity class - the surface pass 1 never reviewed): P2-1 Tang attribution re-corrupted at integration (mTOR neutrality = trisomic-MEF datum, never tested on H/H); P2-2 CAPP3 overstated as "non-inferior" (trial's own rule: not formally concluded). Minors P2-3..P2-8 (arithmetic corner/band, Gate-0 panel drop, Mannick pediatric anchor, CNS dual-compartment, Ovadya census miscount). ALL FIXED at controller layer with P2-tags; census doc corrected via appended controller erratum (authorship separation preserved). GOVERNANCE CORRECTION (P2-5): pass-1 major count was 8 (F1-F7+F13), not 5 - decay calibration updated in SCOPE_DECISION. Pass-2 condition ledger: 11/13 pass-1 conditions fully honored; integration fidelity otherwise clean ("ASO sequence-green numbers integrated with zero drift"). Survival list logged. Stop-rule status: NOT met (2 majors) → confirmation wave fires per plan.
- 2026-09-05 confirmation wave delivered (4/4) and integrated: Q9 rapalog window NAMED (4.5-5 mg/m2, trough 5-15, validated low band 3-7 ng/mL [P3-1-corrected]; Mannick non-translatable - corrected rule 2; honesty datums incl. 2 pediatric treatment-related deaths made mandatory quotation); Q10 surveillance backbone verbatim-verified to 2026 + zero MVA intervention infrastructure (5 registries, positive controls); Q11 negation re-attack: 2 overturned-in-part (navitoclax pediatric exposure; risdiplam/branaplam small-molecule splice precedent) + 2 survived with census growth; Q12 abundance census closed + SIRT2 direction resolved + SIRT2-inhibitors prohibited. All integrated with controller errata appended on affected agent docs (authorship separation). Join gate 24/24 (running total 90/90). Adversarial PASS 3 (stop-rule test) dispatched.
- 2026-09-05 adversarial PASS 3: 2 MAJOR / 7 MINOR / 0 blockers; recommendation CONTINUE→pass 4. P3-1 (MAJOR): EXIST-3 low band mis-attributed as 3-5 (true: 3-7 ng/mL) at 3 live sites + this log [history line corrected inline]. P3-2 (MAJOR): TSV ASO row still carried the Q11-overturned literal (map was fixed; TSV wasn't) - fixed; class-note: the consensus record is a SECOND live document and needs the same fix fan-out discipline as the map. Minors: P3-3 readthrough corner-false in TSV MoA [fixed], P3-4 'five models'/four names [fixed], P3-5 branaplam neuropathy adverse datum now carried [fixed], P3-6 navitoclax combination-context + which-claim-overturned labeling [fixed], P3-7 stale '(5 majors)' here [corrected in-line prior entry], P3-8 wave-4 docs mislabeled wave-3 in map [fixed], P3-9 Q9 titrate-to-5-10 + Q12 therapeutic-window sentence adopted [fixed]. pass-3 verified-sound: all confirmation-wave substance survived independent re-fetch; stop-rule machinery behaved as designed; decay 8→2→2. PASS 4 (FINAL, hard ceiling) dispatched.
- 2026-09-05 adversarial PASS 4 (FINAL, hard ceiling): **0 MAJOR / 0 blockers / 5 presentation-level minors - STOP RULE MET** (decay 8→2→2→0). Verdict: CLOSED-WITH-RESIDUAL-RISK. All nine P3 fixes verified standalone-true with zero fix-induced drift; blind-spot attacks (efficacy overclaim, negative overreach, timeline freshness to Feb-2026 PR sources, version coherence) all CLEAN; end-to-end read coherent. Presentation minors P4-1..P4-5 applied (file-numbering standardization + convention line; MET-oncology unverifiable parenthetical removed from ASOdeep erratum; metformin fallback wording constrained to WATCH bound; map banner v3; ceiling wording clarified; ataluren withdrawal object precision). RESIDUALS DECLARED: R1 no further passes (no pass 5 exists); R2 negatives re-attackable if field moves before Oct submission - remedies: one scheduled Judge/pre-submission refresh sweep; R3 the deepest load is intentionally UNMEASURED decidable only in vitro: Δ716-761+E715G construct function (assay #4) - the consensus closes around it, not over it.
