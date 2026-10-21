# Parse a KEA UGNEET AYUSH allotment list (pdftotext -layout output) into JSON rows.
# Usage: python3 kea_ayush_parse.py list.txt out.json
import re, sys, json
REC = re.compile(r'^\s*(\d+)\s+(\d+)\s+([A-Z]\d{3}[A-Z]{2})\s+(.*?)\s*((?:BAMS|BHMS|BUMS|BSMS)-\S+)\s+(\S+)\s+(\d+)(?:\s+(\S.*?))?\s*$')
SKIP = r'Karnataka Examinations|ALLOTMENT LIST|PUBLISHED ON|All India|SL\.NO|Rank\s+Category|Page \d'
lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
recs = [(i, m) for i, m in ((i, REC.match(l)) for i, l in enumerate(lines)) if m]
assert len(recs) == sum(1 for l in lines if re.match(r'^\s*\d+\s+\d+\s+[A-Z]\d{3}[A-Z]{2}\s', l))
out = []
for k, (i, m) in enumerate(recs):
    # name lines sit above and below the record line; split the gap between neighbours
    lo = (recs[k-1][0] + i) // 2 + 1 if k else i - 6
    hi = (i + recs[k+1][0]) // 2 if k + 1 < len(recs) else i + 6
    parts = []
    for j in range(max(lo, 0), min(hi, len(lines) - 1) + 1):
        l = lines[j]
        if j == i:
            seg = m[4]
        else:
            if re.search(SKIP, l): continue
            seg = l[30:66]
        seg = seg.strip()
        if seg: parts.append(seg)
    out.append(dict(sl=int(m[1]), air=int(m[2]), code=m[3], course=m[5], cat=m[6], fee=int(m[7]), status=m[8] or '', parts=parts))
# a name line from a neighbouring record can leak in; keep only lines seen in most rows of the same code
from collections import Counter, defaultdict
by = defaultdict(list)
for r in out: by[r['code']].append(r['parts'])
names = {}
for code, plist in by.items():
    cnt = Counter(x for ps in plist for x in set(ps))
    keep = {x for x, c in cnt.items() if c * 2 > len(plist)}
    best = max(plist, key=lambda ps: sum(x in keep for x in ps))
    names[code] = ' '.join(x for x in best if x in keep)
for r in out:
    r['name'] = names[r['code']]
    del r['parts']
json.dump(out, open(sys.argv[2], 'w'))
print(len(out), 'rows; max SL', max(r['sl'] for r in out))
