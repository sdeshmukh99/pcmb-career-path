import re, sys, json
REC = re.compile(r'^\s*(\d+)\s+(\d+)\s+(I\d{3}[A-Z]{2})\s+(.*?)(?:\s{2,}((?:BAMS|BHMS|BUMS)-\S+))?\s{2,}(\S+)\s+(\d+)(?:\s+(\S.*?))?\s*$')
SKIP = r'Karnataka Examinations|ALLOTMENT LIST|PUBLISHED ON|All India|SL\.NO|Rank\s+Category|Page \d|B£e'
def parse(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    recs = [(i, REC.match(l)) for i, l in enumerate(lines)]
    recs = [(i, m) for i, m in recs if m]
    n = sum(1 for l in lines if re.match(r'^\s*\d+\s+\d+\s+I\d{3}', l))
    assert len(recs) == n, (len(recs), n)
    out = []
    for k, (i, m) in enumerate(recs):
        lo = (recs[k-1][0] + i) // 2 + 1 if k else i - 8
        hi = (i + recs[k+1][0]) // 2 if k + 1 < len(recs) else i + 8
        parts = []
        for j in range(max(lo, 0), min(hi, len(lines)-1) + 1):
            l = lines[j]
            if j == i: seg = m[4] or ''
            else:
                if re.search(SKIP, l): continue
                seg = l[30:66]
            seg = seg.strip()
            if seg: parts.append(seg)
        out.append(dict(air=int(m[2]), code=m[3], course=m[5], cat=m[6], fee=int(m[7]), status=m[8], name=' '.join(parts)))
    return out
d = sys.argv[1]
data = {r: parse(f'{d}/{r}.txt') for r in ('a25r2', 'a25r3', 'a26r1')}
json.dump(data, open(f'{d}/rows.json', 'w'), ensure_ascii=False)
for r, rows in data.items(): print(r, len(rows))
