# Protein impact analysis - BUB1B compound-het pair (proband PROBAND01)

Protein: O60566, Mitotic checkpoint serine/threonine-protein kinase BUB1 beta (BubR1), 1050 aa.
Kinase domain: 766–1050. Catalytic proton acceptor: D882. ATP-binding: 772–795.
MANE transcript: ENST00000287598 (AlphaMissense annotates as .10; pipeline uses .11 - identical CDS).

## Allele 1 - p.Leu737Ter (c.2210T>G, chr15:40209701 T>G, het)
- Type: nonsense, codon 737/1050 - terminates translation ~30 aa BEFORE the kinase domain (starts 766).
- NMD: termination codon lies >50 nt upstream of the final exon junction (exon ~15-16 of 23) → predicted **NMD substrate → functional null**. Any escape product lacks the entire kinase domain (nonfunctional).
- ClinVar: Pathogenic/Likely-pathogenic, MVA1 (multiple submitters, no conflicts).
- gnomAD v4.1 exomes AF: 7.87e-05 (ultrarare, consistent with disease-allele frequencies).

## Allele 2 - p.Asn1002Lys (c.3006T>G, chr15:40220612 T>G, het) - NOVEL
- Type: missense, kinase domain C-lobe, 120 residues C-terminal of catalytic D882.
- AlphaFold v6 model: region pLDDT 91.1 (rigid, well-structured); positioned C-lobe, ~19.8 Å from D882 Cα,
  ~18.2 Å from DFG region - fold-support region, not the active-site pocket.
- SASA (ProtOr): relSASA 0.44 - partially exposed surface residue; N→K swaps an uncharged amide for a
  positive charge in a hydrophobic-clustered stretch (W993/F996/F997) → predicted local electrostatic
  perturbation, stability/activity reduction rather than fold collapse.
- **AlphaMissense (hg38, local lookup): score 0.9229 - likely_pathogenic.**
  Position constraint: only N1002S is ambiguous (0.3477); ALL other substitutions are
  likely_pathogenic (D 0.7452, H 0.6051, Y 0.7327, I 0.8808, T 0.7235) - N1002K is the most
  radical tolerated-looking change and scores worst.
- gnomAD v4.1 exomes AF: 6.84e-07 (essentially absent).
- ClinVar: unclassified at T>G (same-nucleotide T>A = VUS, T>C = likely-benign).

## In-trans model (matches MVA1 dosage paradigm)
null (L737*) + hypomorph (N1002K, kinase-domain) → residual low BubR1 kinase activity →
leaky spindle assembly checkpoint → constitutional mosaic aneuploidy → MVA1
(rhabdomyosarcoma predisposition, IUGR/growth restriction, parental reproductive loss).
Pattern matches the literature cluster of kinase-domain hypomorphic MVA1 alleles
(see LITERATURE_SWEEP.md, mechanism chapter).

Provenance: UniProt O60566 features; AF-O60566-F1-model_v6.pdb (computed locally,
biotite); AlphaMissense_hg38.tsv.gz row lookup (local file, no API); gnomAD AF via
pipeline GnomadAfJoin (chr15:40209701, chr15:40220612).
