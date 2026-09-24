#!/usr/bin/env python3
"""Rebuild readable <stId>_overview.png / readable <stId>_zoom.png.

Usage: python3 make_readable.py R-HSA-68877 [outdir]
Reads inputs from this script's directory; writes PNGs to outdir (default: cwd).
outdir is NEVER the inputs dir requirement — safe to use a temp dir for the
regenerated-vs-committed comparison without touching the tree.

Inputs expected next to this script:
  reactome_<stId>.png                 - unflagged exporter PNG
  reactome_<stId>_flg_BUBR1.png       - exporter PNG with ?flg=O60566
  diagram_<stId>.json                 - layout JSON (download/current/diagram/)

Method (all constants visible):
  - pixel diff flagged vs plain, threshold 30 (RGB channel sum), clusters >200px
  - merge clusters whose boxes are within 60px; pad crops by 90px; clamp to image
  - node-name/stars: crop box intersected with diagram-JSON node bboxes via an
    EXTENT-FIT transform (png size / json node extent) - approximate; the star
    only asserts containment of a BUB1B/hBUBR1/MCC node at that tolerance.
"""
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

META = {
    "R-HSA-68877": ("Mitotic Prometaphase",
        "BUB1B is NOT drawn as a standalone node in this diagram; Reactome flags it via "
        "membership in kinetochore-containing complexes. Panels = regions the exporter "
        "renders differently when the O60566 flag is applied (nodes named per diagram JSON)."),
    "R-HSA-69620": ("Cell Cycle Checkpoints",
        "Panels = regions the exporter renders differently when the O60566 flag is applied. "
        "Panel numbers marked * contain the explicitly drawn 'BUB1B' entity / "
        "hBUBR1:hBUB3:MAD2*:CDC20 (MCC) / MCC:APC/C complexes per diagram JSON."),
    "R-HSA-5663220": ("RHO GTPases Activate Formins",
        "BUB1B is NOT drawn as a standalone node in this diagram; the O60566 flag maps onto "
        "kinetochore complexes (Reactome lists BUB1B as a Kinetochore component). Panels = "
        "regions the exporter renders differently with the flag."),
}


def bf(px): return ImageFont.truetype(FB, px)
def rf(px): return ImageFont.truetype(FR, px)


def wrap_px(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if font.getlength(trial) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines


HERE = os.path.dirname(os.path.abspath(__file__))

def main(st, outdir="."):
    title, note = META[st]
    d = json.load(open(os.path.join(HERE, f"diagram_{st}.json")))
    nodes = d["nodes"]
    Wj = max(n["maxX"] for n in nodes)
    Hj = max(n["maxY"] for n in nodes)
    bub_nodes = [n for n in nodes if ("BUB1B" in n["displayName"]
                                      or "hBUBR1" in n["displayName"]
                                      or "MCC:" in n["displayName"])]
    pn = st.replace("-", "_")
    plain = Image.open(os.path.join(HERE, f"reactome_{pn}.png")).convert("RGB")
    flagged = np.asarray(
        Image.open(os.path.join(HERE, f"reactome_{pn}_flg_BUBR1.png")).convert("RGB")).astype(int)
    base = np.asarray(plain).astype(int)
    H, W = base.shape[:2]
    sx, sy = W / Wj, H / Hj
    diff = (np.abs(base - flagged).sum(2) > 30).astype(np.uint8)
    lab, n = ndimage.label(diff, structure=np.ones((3, 3)))
    boxes = []
    for i in range(1, n + 1):
        ys, xs = np.where(lab == i)
        if len(ys) > 200:
            boxes.append([xs.min(), ys.min(), xs.max(), ys.max(), len(ys)])
    boxes.sort(key=lambda b: -b[4])
    merged = []
    for b in boxes:
        for m in merged:
            if not (b[2] < m[0] - 60 or b[0] > m[2] + 60
                    or b[3] < m[1] - 60 or b[1] > m[3] + 60):
                m[0] = min(m[0], b[0]); m[1] = min(m[1], b[1])
                m[2] = max(m[2], b[2]); m[3] = max(m[3], b[3])
                break
        else:
            merged.append(b)
    PAD = 90
    crops = [(max(0, x0 - PAD), max(0, y0 - PAD), min(W, x1 + PAD), min(H, y1 + PAD))
             for x0, y0, x1, y1, _ in merged]

    def jbox(nd):
        return (nd["minX"] * sx, nd["minY"] * sy, nd["maxX"] * sx, nd["maxY"] * sy)

    def contains_bub(crop):
        x0, y0, x1, y1 = crop
        return any(not (b[2] < x0 or b[0] > x1 or b[3] < y0 or b[1] > y1)
                   for b in map(jbox, bub_nodes))

    def crop_names(crop, kmax=4):
        x0, y0, x1, y1 = crop
        hits = []
        for nd in nodes:
            if nd["renderableClass"] == "Chemical":
                continue
            b = jbox(nd)
            if not (b[2] < x0 or b[0] > x1 or b[3] < y0 or b[1] > y1):
                if nd["displayName"] not in hits:
                    hits.append(nd["displayName"])
        return hits[:kmax]

    ov = plain.copy()
    sh = 1600 / W
    ov = ov.resize((1600, int(H * sh)))
    dr = ImageDraw.Draw(ov)
    f = bf(28)
    for k, (x0, y0, x1, y1) in enumerate(crops, 1):
        cx, cy = int((x0 + x1) / 2 * sh), int((y0 + y1) / 2 * sh)
        r = 26
        dr.ellipse([cx - r, cy - r, cx + r, cy + r],
                   fill=(208, 96, 88), outline=(255, 255, 255), width=4)
        dr.text((cx, cy), str(k), anchor="mm", fill="white", font=f)
    os.makedirs(outdir, exist_ok=True)
    ov.save(os.path.join(outdir, f"readable_{pn}_overview.png"))

    cols = 3
    rows = (len(crops) + cols - 1) // cols
    cell_w, cell_h, label_h = 940, 700, 84
    img_area_h = cell_h - label_h - 56
    grid = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
    dr = ImageDraw.Draw(grid)
    ft, fs = bf(30), rf(19)
    for k, crop in enumerate(crops, 1):
        x0, y0, x1, y1 = crop
        c = plain.crop(crop)
        s = min((cell_w - 40) / c.width, img_area_h / c.height, 4.0)
        c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))))
        gx, gy = (k - 1) % cols * cell_w, (k - 1) // cols * cell_h
        dr.rectangle([gx + 8, gy + 8, gx + cell_w - 8, gy + cell_h - 8],
                     outline=(180, 180, 180))
        cx0, cy0 = gx + (cell_w - c.width) // 2, gy + 50
        grid.paste(c, (cx0, cy0))
        star = "*" if contains_bub(crop) else ""
        chip_w = int(ft.getlength(f"{k}{star}") + 16)
        dr.rectangle([cx0, cy0, cx0 + chip_w, cy0 + 34], fill=(255, 255, 255),
                     outline=(208, 96, 88))
        dr.text((cx0 + 8, cy0 + 4), f"{k}{star}", fill=(208, 96, 88), font=ft)
        names = crop_names(crop)
        text = "; ".join(names)
        lines = wrap_px(text, fs, cell_w - 48)
        while len(lines) > 2 and names:
            names = names[:-1]
            lines = wrap_px("; ".join(names) + " …", fs, cell_w - 48)
            if len(lines) <= 2: break
        if len(lines) > 2:
            lines = lines[:2]
            lines[1] = lines[1][:-3] + "…"
        ly = gy + cell_h - 24 - (len(lines) - 1) * 22 - 18
        dr.rectangle([gx + 16, ly - 6, gx + cell_w - 16,
                      ly - 6 + len(lines) * 22 + 12],
                     fill=(255, 255, 255), outline=(200, 200, 200))
        for j, line in enumerate(lines):
            dr.text((gx + 24, ly + j * 22), line, fill=(60, 60, 60), font=fs)
    cap_h = 110
    cap = Image.new("RGB", (cols * cell_w, cap_h), "white")
    drc = ImageDraw.Draw(cap)
    drc.text((cols * cell_w // 2, 28),
             f"{title} (Reactome {st}) — native diagram, flg=O60566 render regions zoomed",
             anchor="mm", fill=(60, 60, 60), font=bf(26))
    for j, line in enumerate(wrap_px(note, rf(18), cols * cell_w - 120)[:3]):
        drc.text((cols * cell_w // 2, 64 + j * 22), line, anchor="mm",
                 fill=(90, 90, 90), font=rf(18))
    out = Image.new("RGB", (cols * cell_w, rows * cell_h + cap_h), "white")
    out.paste(grid, (0, 0))
    out.paste(cap, (0, rows * cell_h))
    out.save(os.path.join(outdir, f"readable_{pn}_zoom.png"))
    print(st, "panels:", len(crops), "starred:", sum(contains_bub(c) for c in crops))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ".")
