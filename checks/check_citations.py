#!/usr/bin/env python3
"""Citation census for the professional Track-2 report.
Invariants: every [E#] cited in the body is defined in §8; every defined row is
cited; no duplicate rows. If the §8 heading carries a count it must equal the
number of defined base rows (heading is count-free by design since 2026-09-14  - 
a printed count was demonstrated irreproducible twice). Exit 1 on any break.
Run from anywhere: python3 scripts/check_citations_pro.py <repo-root>."""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
lines = (root / 'TRACK2_REPORT.md').read_text().splitlines()
in_refs = False
defined, cited = {}, set()
for ln in lines:
    if ln.startswith('## 8. References'): in_refs = True
    if in_refs and ln.startswith('## 9.'): in_refs = False
    if in_refs:
        m = re.match(r'- \*\*(E\d+[a-z]?(?:-[A-Z0-9]+)?)\*\*', ln)
        if m: defined[m.group(1)] = defined.get(m.group(1), 0) + 1
    else:
        cited.update(re.findall(r'\[(E\d+[a-z]?(?:-[A-Z0-9]+)?)\]', ln))
dset = set(defined)
fail = []
if (x := sorted(cited - dset)): fail.append(f'cited-not-defined: {x}')
if (x := sorted(dset - cited)): fail.append(f'defined-not-cited: {x}')
if (x := [d for d, c in defined.items() if c > 1]): fail.append(f'duplicate rows: {x}')
base = {d for d in dset if '-' not in d}
subs = dset - base
m = re.search(r'References \((\d+)', '\n'.join(lines))
if m:  # heading used to carry a count; heading is now count-free by design (was 2x wrong)
    hdr = int(m.group(1))
    if hdr != len(base): fail.append(f'header says {hdr} but {len(base)} base rows defined')
    hstr = f', header {hdr}'
else:
    hstr = ''
print(f'citation census: {len(base)} base + {len(subs)} sub-rows defined, {len(cited)} cited{hstr}')
if fail:
    print('FAIL: ' + '; '.join(fail)); sys.exit(1)
print('CENSUS OK')
