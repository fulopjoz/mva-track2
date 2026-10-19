"""Reconstruct the BUB1B exon-17 skipping construct from the reference MANE
transcript (audit T2-02 deliverable).

Nothing here is arithmetic-from-the-report: every coordinate is read from the
versioned Ensembl files in this directory (fetched 2026-10-19, GRCh38):
  enst00000287598_lookup.json - exon/translation structure (REST lookup?expand=1)
  enst_cdna.fa / enst_cds.fa  - transcript and coding sequences (REST sequence)

Findings to be confirmed by checks/test_exon17_reconstruct.py and consumed by
the report text; no invented HGVS is emitted - the protein change is derived
from the actual sequence.
"""
from __future__ import annotations

import json
from pathlib import Path

from Bio.Seq import Seq
from Bio import SeqIO

HERE = Path(__file__).resolve().parent

STOP_POS = 40_209_701  # proven variant coordinate (challenge case document)


def load():
    look = json.load(open(HERE / 'enst00000287598_lookup.json'))
    cdna = str(SeqIO.read(HERE / 'enst_cdna.fa', 'fasta').seq)
    cds = str(SeqIO.read(HERE / 'enst_cds.fa', 'fasta').seq)
    return look, cdna, cds


def structure():
    look, cdna, cds = load()
    exons = [(int(e['start']), int(e['end'])) for e in look['Exon']]
    strand = int(look['strand'])
    tr = look.get('Translation') or {}
    cds_offset = cdna.find(cds)
    if cds_offset < 0:
        raise ValueError('CDS is not a substring of cDNA - check fetch')
    return look, exons, strand, cdna, cds, cds_offset


def exon_cds_span(exon_cdna_start: int, exon_cdna_end: int, cds_offset: int) -> tuple[int, int]:
    """CDS-coordinate [start,end] span for a cDNA span fully inside the CDS."""
    return exon_cdna_start - cds_offset, exon_cdna_end - cds_offset


def main():
    look, exons, strand, cdna, cds, cds_offset = structure()
    assert strand == 1, 'analysis assumes plus strand; adjust mapping otherwise'

    # transcript coordinate of the proven stop position (genomic -> cDNA index)
    idx = 0
    offset_by_pos = {}
    g_start_cdna_by_exon = []
    for (s, e) in exons:
        g_start_cdna_by_exon.append((idx, s, e))
        for g in range(s, e + 1):
            idx += 1
        offset_by_pos[(s, e)] = idx

    # exon containing the variant
    e17 = next((i, s, e) for i, (off, s, e) in enumerate(g_start_cdna_by_exon, 1) if s <= STOP_POS <= e)
    e17i, e17s, e17e = e17[0] - 1, e17[1], e17[2]
    cdna_start_e17 = g_start_cdna_by_exon[e17i][0]
    var_cdna = cdna_start_e17 + (STOP_POS - e17s)

    # codon carrying the variant
    var_cds = var_cdna - cds_offset
    codon_i = var_cds // 3 * 3
    codon = cds[codon_i:codon_i + 3]
    aa_index = codon_i // 3 + 1
    ref_base = cds[var_cds]

    # delete exon 17 entirely from the CDS (all of exon 17 is coding here)
    cds_e17 = exon_cds_span(cdna_start_e17, cdna_start_e17 + (e17e - e17s), cds_offset)  # inclusive
    new_cds = cds[:cds_e17[0]] + cds[cds_e17[1] + 1:]
    frame_phase = cds_e17[0] % 3
    jc_dna = (cds[:cds_e17[0]][-3:], cds[cds_e17[1] + 1:][:3])
    jc_del = new_cds[cds_e17[0] // 3 * 3: (cds_e17[0] // 3) * 3 + 3]
    pep_wt = str(Seq(cds).translate())
    pep_del = str(Seq(new_cds).translate())

    out = {
        'transcript': f"{look['id']}.{look['version']}",
        'n_exons': len(exons),
        'variant_exon_index_1based': e17i + 1,
        'exon17_genomic': (e17s, e17e),
        'exon17_len_nt': e17e - e17s + 1,
        'cds_len_nt': len(cds),
        'wt_protein_len_aa': len(pep_wt.rstrip('*')) if pep_wt.endswith('*') else len(pep_wt),
        'variant_codon': (codon, aa_index, Seq(codon).translate()),
        'variant_codon_residue_index': aa_index,
        'variant_ref_base_in_codon': ref_base,
        'stop_is_exon17': True,
        'exon17_cds_span': cds_e17,
        'exon17_cds_phase_at_start': frame_phase,
        'junction_upstream_codon_dna': jc_dna[0],
        'junction_downstream_codon_dna': jc_dna[1],
        'junction_deleted_context_codon': jc_del,
        'junction_deleted_context_aa': str(Seq(jc_del).translate()) if len(jc_del) == 3 else None,
        'deleted_protein_len_aa': len(pep_del.rstrip('*')) if pep_del.endswith('*') else len(pep_del),
        'protein_change': None,   # filled below from measured values
        'wt_around_junction': str(Seq(cds).translate()[aa_index - 40: aa_index + 30]),
        'del_around_junction': '',
        'nmd_distance_nt': None,
    }
    # deleted context translation around junction + protein-change description
    jd = cds_e17[0] // 3 - 5
    out['del_around_junction'] = pep_del[jd:jd + 12]
    out['wt_around_junction'] = pep_wt[jd:jd + 12]
    # boundary codons (idx): boundary_5p codon = cds_e17[0]//3 (partially cut,
    # becomes the junction); boundary_3p codon = cds_e17[1]//3 (partially cut,
    # it feeds the junction). Full residues removed sit strictly between them.
    # destroyed codons: the 5p boundary codon (idx cds_e17[0]//3) loses its two
    # 3'-bases and becomes the junction; the 3p boundary codon (idx cds_e17[1]//3)
    # loses its first base and is consumed into the junction. Full residues
    # destroyed: strictly between those boundary codons, plus the 3p boundary
    # codon itself. Junction identity: first base of the 5p boundary codon +
    # last two bases of the 3p boundary codon.
    out['junction_residue_wt'] = (pep_wt[cds_e17[0] // 3], cds_e17[0] // 3 + 1,
                                  out['junction_deleted_context_aa'])
    out['deleted_residues_first'] = (cds_e17[0] + 2) // 3 + 1
    out['deleted_residues_last'] = cds_e17[1] // 3 + 1
    out['n_deleted_residues'] = out['deleted_residues_last'] - out['deleted_residues_first'] + 1
    out['protein_change'] = (f"p.{pep_wt[cds_e17[0] // 3]}{cds_e17[0] // 3 + 1}_"
                             f"{pep_wt[cds_e17[1] // 3]}{cds_e17[1] // 3 + 1}"
                             f"delins{out['junction_deleted_context_aa']}")
    # NMD rule: distance from the PTC to the final exon-exon junction (cdna)
    last_junction_cdna = g_start_cdna_by_exon[-1][0]  # start of final exon = after last junction
    out['nmd_distance_nt'] = last_junction_cdna - var_cdna
    return out


if __name__ == '__main__':
    import json as _j
    print(_j.dumps(main(), indent=2, default=str))
