import json, sys, collections
sys.path.insert(0, 'tools')
from ayush_colleges import COLLEGES
d = json.load(open(sys.argv[1]))
def inr(n):
    s = str(n)
    if len(s) <= 3: return s
    h, t = s[:-3], s[-3:]; p = []
    while len(h) > 2: p.insert(0, h[-2:]); h = h[:-2]
    if h: p.insert(0, h)
    return ",".join(p + [t])
def cut(r, code, cat):
    a = [x["air"] for x in d[r] if x["code"] == code and x["cat"] == cat]
    return max(a) if a else None
def fee(code):
    for r in ("a26r1", "a25r3", "a25r2"):
        f = {x["fee"] for x in d[r] if x["code"] == code}
        if f: (v,) = f; return v, r
    return None, None
stems = {x["code"][:4] for r in d.values() for x in r if x["code"][4] == "A"}
assert stems == set(COLLEGES), stems ^ set(COLLEGES)
T = []
for s, (name, loc) in COLLEGES.items():
    gf, gr = fee(s + "AG"); pf, pr = fee(s + "AP")
    kind = "Government" if gf in (25000, 30335) else "Private"
    c = [cut(r, s + "AG", "GM") for r in ("a26r1", "a25r2", "a25r3")]
    pc = cut("a26r1", s + "AP", "OPN")
    T.append(dict(s=s, name=name, loc=loc, kind=kind, gf=gf, gr=gr, pf=pf, pr=pr, c=c, pc=pc))
T.sort(key=lambda t: (t["c"][0] is None, t["c"][0] or t["c"][2] or t["c"][1] or 9e9))
f = lambda v: inr(v) if v else "–"
rows = []
for t in T:
    gfee = "₹" + inr(t["gf"]) + ("" if t["gr"] == "a26r1" else " (2025)")
    pfee = "–" if not t["pf"] else "₹" + inr(t["pf"]) + ("" if t["pr"] == "a26r1" else " (2025)")
    rows.append([t["name"], t["loc"], t["kind"], gfee] + [f(v) for v in t["c"]] + [pfee, f(t["pc"])])
json.dump(rows, open(sys.argv[2], "w"), ensure_ascii=False, indent=0)
print(len(rows), sum(1 for t in T if t["c"][0]), collections.Counter((t["kind"], t["gf"]) for t in T))
for r in rows: print(" | ".join(r))
