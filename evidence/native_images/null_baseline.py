#!/usr/bin/env python3
"""Null baseline for the flag-diff coincidence test (step 3 of PROVENANCE.md).

Random 150x150-model-unit boxes are scattered inside each diagram's node
extent; a box 'hits' if it intersects any of the participants-verified
O60566 complex node boxes within +-120 model units. Baseline = hit fraction
over 1000 boxes, seed 42. Prints baseline and one-sided binomial p for the
observed cluster coincidences written in PROVENANCE.md.

Usage: python3 null_baseline.py"""
import json
import random
from scipy.stats import binomtest

PE = {
    "R-HSA-68877": (8, 10, {375303, 375305, 1638796, 2468282, 2484819, 2500242, 9648124}),
    "R-HSA-5663220": (4, 4, {375303, 375305, 5666131, 5666161}),
    "R-HSA-69620": (12, 12, {141410, 141427, 141432, 141436, 141440, 141441, 375305}),
}
N_BOXES, HALF = 1000, 75
TOL = 120
SEED = 42

for st, (obs, n, pe) in PE.items():
    d = json.load(open(f"diagram_{st}.json"))
    bub = [nd for nd in d["nodes"] if nd.get("reactomeId") in pe]
    Wj = max(nd["maxX"] for nd in d["nodes"])
    Hj = max(nd["maxY"] for nd in d["nodes"])
    random.seed(SEED)
    hits = 0
    for _ in range(N_BOXES):
        x = random.uniform(0, Wj); y = random.uniform(0, Hj)
        x0, x1, y0, y1 = x - HALF, x + HALF, y - HALF, y + HALF
        for nd in bub:
            if not (nd["maxX"] < x0 - TOL or nd["minX"] > x1 + TOL
                    or nd["maxY"] < y0 - TOL or nd["minY"] > y1 + TOL):
                hits += 1; break
    p0 = hits / N_BOXES
    p = binomtest(obs, n, p0, alternative="greater").pvalue
    print(f"{st}: baseline {p0:.3f} (seed {SEED}, {N_BOXES} random {2*HALF}-unit boxes, "
          f"{len(bub)} verified nodes) | observed {obs}/{n} -> p = {p:.2e}")
