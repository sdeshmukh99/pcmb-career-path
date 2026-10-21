import re, sys, json, collections
REC = re.compile(r'^\s*(\d+)\s+(\d+)\s+(M\d{3}[A-Z]{2})\s+(.*?)\s{2,}(MBBS-\S+)\s+(\S+)\s+(\d+)(?:\s+(\S.*?))?\s*$')
def parse(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    idx = [(i, REC.match(l)) for i, l in enumerate(lines)]
    recs = [(i, m) for i, m in idx if m]
    assert len(recs) == sum(1 for l in lines if re.match(r'^\s*\d+\s+\d+\s+M\d{3}', l))
    out = []
    for k, (i, m) in enumerate(recs):
        lo = (recs[k-1][0] + i) // 2 + 1 if k else i - 6
        hi = (i + recs[k+1][0]) // 2 if k + 1 < len(recs) else i + 6
        parts = []
        for j in range(max(lo, 0), min(hi, len(lines)-1) + 1):
            l = lines[j]
            if j == i:
                seg = m[4]
            else:
                if re.search(r'Karnataka Examinations|ALLOTMENT LIST|PUBLISHED ON|All India|SL\.NO|Rank\s+Category|Page \d', l): continue
                seg = l[30:66]
            seg = seg.strip()
            if seg: parts.append(seg)
        out.append(dict(air=int(m[2]), code=m[3], course=m[5], cat=m[6], fee=int(m[7]), name=' '.join(parts)))
    return out
data = {r: parse(f'{sys.argv[1]}/{r}.txt') for r in ('r1', 'r2', 'r3')}
json.dump(data, open(f'{sys.argv[1]}/rows.json', 'w'))
for r, rows in data.items(): print(r, len(rows))
