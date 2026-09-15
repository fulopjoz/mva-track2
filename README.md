# MVA Hackathon 2026 - Track 2: drug repurposing

Team `fulopjoz` (individual). Task: for a five-year-old with biallelic BUB1B Mosaic
Variegated Aneuploidy (nonsense p.Leu737Ter + missense p.Asn1002Lys destabilizing the
kinase core), decide what drug repurposing could offer.

## Verdict

**Surveillance-first care.** No drug is recommended for this child today. One candidate
is named for discussion with the care team inside monitoring gates: **everolimus**, the
only drug with a proven multi-year pediatric safety record (TSC trials, median exposure
47 months), with its mechanistic fit explicitly labeled low-grade. The committed research
direction is **ASO exon-17 skipping** past the premature stop codon. Senolytics,
full-dose read-through agents, SAC/kinase inhibitors, and immune-enhancing axes are
excluded behind laboratory gates.

Full reasoning: `TRACK2_REPORT.md` (or `.pdf`). Family-facing version:
`TRACK2_LAY_REPORT.md` (or `.docx` / `.pdf`).

## Repository contents

| Path | What it is |
|---|---|
| `TRACK2_REPORT.md` / `.pdf` | The submitted report |
| `TRACK2_LAY_REPORT.md` / `.docx` / `.pdf` | Family-facing version of the same evidence |
| `candidates.tsv` | The 20-row candidate table with per-row verdicts |
| `figures/` | F1-F5: structure, protein map, gene schematic, decision instrument, process figure |
| `evidence/` | The 19 analytical memos backing every claim (manifest: `evidence/MEMO_MANIFEST.md`), plus the four adversarial review passes, the contested-anchor adjudication, and the structural analyses |
| `checks/check_citations.py` | Re-verifies the reference census (count of defined vs cited entries) |

## Validation

Every external claim carries `[E#]` pointers into the report's reference list, each with
a verification trail. `python3 checks/check_citations.py` recounts defined vs cited
entries and must print `CENSUS OK`.
