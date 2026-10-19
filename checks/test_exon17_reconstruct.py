"""T2-02: exon-17 skipping construct reconstruction vs the MANE reference.

Locks the exact exon structure and deletion arithmetic of ENST00000287598.11
(fetched 2026-10-19, committed under evidence/exon_skip/) against the
sequence-derived construct description. Values are recomputed from the files,
never typed from the report text.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent.parent / 'evidence' / 'exon_skip'
sys.path.insert(0, str(HERE))
from reconstruct_exon17 import main as reconstruct  # noqa: E402


@pytest.fixture(scope='module')
def r():
    return reconstruct()


def test_transcript_identity_and_version(r):
    assert r['transcript'] == 'ENST00000287598.11'


def test_exon_count_and_exon17_geometry(r):
    assert r['n_exons'] == 23
    s, e = r['exon17_genomic']
    assert (s, e) == (40209635, 40209775)
    assert r['exon17_len_nt'] == 141


def test_cds_length_and_wt_protein(r):
    assert r['cds_len_nt'] == 3153          # 1050 aa + stop codon, %3 == 0
    assert r['wt_protein_len_aa'] == 1050   # p.N1002* etc. refer to this length


def test_variant_codon_is_L737_in_exon17(r):
    assert r['variant_codon'] == ('TTA', 737, 'L')
    assert r['variant_codon_residue_index'] == 737
    assert r['variant_exon_index_1based'] == 17


def test_nmd_position_rule_satisfied(r):
    # PTC sits far upstream of the final exon-exon junction (>50-55 nt rule)
    assert r['nmd_distance_nt'] > 55


def test_junction_and_deleted_span(r):
    """Sequence-derived construct: junction residue re-forms p.E715 -> p.G715;
    destroyed residues are 716..762 inclusive (-47 aa, consistency check with
    the 141-nt deletion = 46 full interior residues + 2 boundary codons)."""
    assert r['junction_residue_wt'][0] == 'E'
    assert r['junction_residue_wt'][1] == 715
    assert r['junction_residue_wt'][2] == 'G'
    assert r['deleted_residues_first'] == 716
    assert r['deleted_residues_last'] == 762
    assert r['n_deleted_residues'] == 47
    assert r['protein_change'] == 'p.E715_G762delinsG'
    # deleted protein length must equal 1050 - 47 exactly (frame preserved)
    assert r['deleted_protein_len_aa'] == 1003
    # downstream of the junction the sequence resumes at WT residue 763
    assert r['del_around_junction'][6:12] == 'NEDYCI'
    assert r['del_around_junction'][5] == 'G'


def test_reconstruction_is_deterministic(r):
    j1 = subprocess.run([sys.executable, str(HERE / 'reconstruct_exon17.py')],
                        capture_output=True, text=True)
    j2 = subprocess.run([sys.executable, str(HERE / 'reconstruct_exon17.py')],
                        capture_output=True, text=True)
    assert j1.returncode == j2.returncode == 0
    assert j1.stdout == j2.stdout
    payload = json.loads(j1.stdout)
    assert payload['protein_change'] == 'p.E715_G762delinsG'
