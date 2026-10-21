# Parse AACCC UG final allotment results (PDF tables) into JSON rows.
# Usage: python3 aaccc_parse.py round1.pdf round2.pdf out.json
# Round 1 rows: SNo, Rank, Quota, Institute, Course, Category, Candidate category, Remarks.
# Round 2 rows: SNo, Rank, then the Round 1 seat (Quota, Institute, Course, Remarks)
# and the Round 2 seat (Quota, Institute, Course, Category, Candidate category, Option, Remarks).
import pdfplumber, json, sys

def rows(path):
    out = []
    with pdfplumber.open(path) as p:
        for pg in p.pages:
            for t in pg.extract_tables():
                for r in t:
                    r = [(c or '').replace('\n', ' ').strip() for c in r]
                    if len(r) > 1 and r[0].isdigit() and r[1].isdigit():
                        out.append(r)
    sn = [int(r[0]) for r in out]
    assert sorted(sn) == list(range(1, len(sn) + 1)), path
    return out

d = {'r1': rows(sys.argv[1]), 'r2': rows(sys.argv[2])}
json.dump(d, open(sys.argv[3], 'w'))
print({k: len(v) for k, v in d.items()})
