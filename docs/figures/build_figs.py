#!/usr/bin/env python3
"""Generate technical-doc figures for Track 2.
Outputs two PNGs next to this script (DPI 200, DejaVu Sans):
- F_workflow_overview.png  - sources -> evidence memos -> adversarial passes -> report
- F_evidence_verification.png - native-image verification chain, numbers from
  evidence/native_images/PROVENANCE.md
"""
import os

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
INK = (0.12, 0.12, 0.16)
FILL = (0.95, 0.95, 0.97)
ACCENT = (0.24, 0.35, 0.66)



def _assert_fits(fig, ax, checks, margin=0.010):
    """Fail loudly if any text extends outside its box.
    checks: list of (text_artist, x, y, w, h) in axes coordinates."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    bad = []
    for t, x, y, w, h in checks:
        bb = t.get_window_extent(r)
        (x0, y0), (x1, y1) = ax.transData.inverted().transform(
            [(bb.x0, bb.y0), (bb.x1, bb.y1)])
        if x0 < x - margin or x1 > x + w + margin \
                or y0 < y - margin / 2 or y1 > y + h + margin / 2:
            bad.append((t.get_text().split("\n")[0][:40], round(x0, 3),
                        round(x1, 3), round(x, 3), round(x + w, 3)))
    if bad:
        raise SystemExit(f"text overflow outside box: {bad}")

def draw_workflow(path):
    fig, ax = plt.subplots(figsize=(11, 3.6))
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    cols = [0.02, 0.27, 0.52, 0.77]
    w, h, y = 0.21, 0.62, 0.18
    boxes = [
        ("Sources", "RCSB PDB \u00b7 PDBe\nAlphaFold DB\nReactome \u00b7 UniProt"),
        ("Evidence memos", "19 analytical memos\nevidence/\nMEMO_MANIFEST.md"),
        ("Adversarial passes", "major-count decay\n8 \u2192 2 \u2192 2 \u2192 0"),
        ("Deliverables", "TRACK2_REPORT\ncandidates.tsv\nfigures F1\u2013F4"),
    ]
    checks = []
    for (title, note), x in zip(boxes, cols):
        ax.add_patch(Rectangle((x, y), w, h, linewidth=1.1,
                               edgecolor=INK, facecolor=FILL))
        checks.append((ax.text(x + w / 2, y + h - 0.12, title, ha="center",
                               va="center", fontsize=11, weight="bold",
                               color=ACCENT), x, y, w, h))
        checks.append((ax.text(x + w / 2, y + h * 0.40, note, ha="center",
                               va="center", fontsize=8.5, color=INK),
                       x, y, w, h))
    for i in range(len(cols) - 1):
        ax.add_patch(FancyArrowPatch((cols[i] + w, y + h / 2),
                                     (cols[i + 1], y + h / 2),
                                     arrowstyle="-|>", mutation_scale=14,
                                     linewidth=1.2, color=INK))
    ax.text(cols[2] + w / 2, y + h + 0.06, "CLOSED-WITH-RESIDUAL-RISK",
            ha="center", fontsize=9, color=(0.55, 0.15, 0.15), weight="bold")
    _assert_fits(fig, ax, checks)
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def draw_verification(path):
    steps = [
        ("1. Fetch native inputs", "fetch_native.sh",
         "Reactome diagrams, RCSB/PDBe, AlphaFold"),
        ("2. Exporter determinism", "plain-vs-plain byte compare (control)",
         "0 differing pixels"),
        ("3. O60566 membership", "Reactome participants endpoint + diagram JSON",
         "7 / 4 / 7 complexes per diagram"),
        ("4. Flag-diff coincidence", "null_baseline.py (seed 42)",
         "R-HSA-68877: 8/10, p\u22480.15   R-HSA-5663220: 4/4, p\u22480.023   "
         "R-HSA-69620: 12/12, p\u22489e-13"),
        ("5. Verdict", "PROVENANCE.md",
         "BUB1B-containing complexes; 2 unexplained R-HSA-68877 clusters;\n"
         "6 PNGs byte-identical to regeneration"),
    ]
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    w, h = 0.72, 0.145
    x = 0.14
    top, gap = 0.925, 0.045
    checks = []
    for i, (title, script, note) in enumerate(steps):
        y = top - i * (h + gap) - h
        ax.add_patch(Rectangle((x, y), w, h, linewidth=1.1,
                               edgecolor=INK, facecolor=FILL))
        checks = [] if not checks else checks
        checks.append((ax.text(x + w / 2, y + h - 0.032, title, ha="center",
                               va="center", fontsize=10, weight="bold",
                               color=ACCENT), x, y, w, h))
        checks.append((ax.text(x + w / 2, y + h * 0.44, f"[ {script} ]",
                               ha="center", va="center", fontsize=7.5,
                               style="italic", color=INK), x, y, w, h))
        checks.append((ax.text(x + w / 2, y + h * 0.16, note, ha="center",
                               va="center", fontsize=7.5, color=INK),
                       x, y, w, h))
        if i < len(steps) - 1:
            ax.add_patch(FancyArrowPatch((x + w / 2, y),
                                         (x + w / 2, y - gap),
                                         arrowstyle="-|>", mutation_scale=13,
                                         linewidth=1.2, color=INK))
    _assert_fits(fig, ax, checks)
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    draw_workflow(os.path.join(HERE, "F_workflow_overview.png"))
    draw_verification(os.path.join(HERE, "F_evidence_verification.png"))
    print("wrote", os.listdir(HERE))
