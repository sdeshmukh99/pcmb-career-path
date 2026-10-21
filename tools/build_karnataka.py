import json, sys, collections
sys.path.insert(0, sys.argv[1])
from colleges import COLLEGES

rows_path, content_path = sys.argv[2], sys.argv[3]
d = json.load(open(rows_path))
TODAY = "2026-10-21"
REPO = "https://github.com/sdeshmukh99/pcmb-career-path/blob/main/"
SOURCES = [
    {"label": "KEA UGNEET 2026 Round 1 final allotment list (28 Aug 2026)",
     "url": REPO + "KEA-UG-NEET-2026-MEDICAL-1st-ROUND-FINAL-SEAT-ALLOTMENT-LIST-.pdf"},
    {"label": "KEA Round 2 final allotment list (16 Sep 2026)",
     "url": REPO + "UGNEET_ALLOT_2026_2nd_MFINAL_16092026_R2_SECONDenglish%20(1).pdf"},
    {"label": "KEA Round 3 final allotment list (6 Oct 2026)",
     "url": REPO + "UGNEET_ALLOT_2026_3rd_MFINAL_06102026_R3english_76becbbd8c1e7eaf230f25d1e66b7056.pdf"},
    {"label": "KEA official website", "url": "https://kea.kar.nic.in/"},
]


def inr(n):
    s = str(n)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts + [tail])


def gm(rows, code):
    return [x for x in rows if x["code"] == code and x["cat"] == "GM"]


fees = collections.defaultdict(set)
for r in d.values():
    for x in r:
        if x["code"].endswith("MG"):
            fees[x["code"]].add(x["fee"])

assert set(fees) == set(COLLEGES), set(fees) ^ set(COLLEGES)

table = []
for code, (name, loc, region) in COLLEGES.items():
    (fee,) = fees[code]
    kind = "Government" if fee == 64350 else "ESIC (central govt)" if fee == 109350 else "Private"
    cut = [max((x["air"] for x in gm(d[r], code)), default=None) for r in ("r1", "r2", "r3")]
    seats = len(gm(d["r2"], code))
    table.append(dict(code=code, name=name, loc=loc, region=region, kind=kind, fee=fee, seats=seats, cut=cut))

table.sort(key=lambda t: (t["cut"][0] is None, t["cut"][0] or t["cut"][1]))
fmt = lambda v: inr(v) if v is not None else "–"

main_rows = [[t["name"], t["loc"], t["kind"], "₹" + inr(t["fee"]), str(t["seats"])] + [fmt(c) for c in t["cut"]]
             for t in table]

# Summary by region
agg = collections.OrderedDict()
for t in table:
    a = agg.setdefault(t["region"], collections.Counter())
    a["colleges"] += 1
    a[t["kind"]] += 1
    a["seats"] += t["seats"]
summary = sorted(agg.items(), key=lambda kv: -kv[1]["seats"])
sum_rows = [[reg, str(a["colleges"]), str(a["Government"]), str(a["ESIC (central govt)"]), str(a["Private"]), inr(a["seats"])]
            for reg, a in summary]
tot = collections.Counter()
for _, a in summary:
    tot.update(a)
sum_rows.append(["<strong>All Karnataka</strong>"] + [f"<strong>{v}</strong>" for v in (
    str(tot["colleges"]), str(tot["Government"]), str(tot["ESIC (central govt)"]), str(tot["Private"]), inr(tot["seats"]))])

blr = agg["Bengaluru"]
lead = (f"{tot['colleges']} colleges offered KEA government-quota (GMG) MBBS seats in 2026: "
        f"{tot['Government']} government, {tot['ESIC (central govt)']} ESIC and {tot['Private']} private. "
        "These seats are filled through KEA counselling for candidates eligible under Karnataka's state-quota rules. "
        "The fee for a government seat is fixed by KEA: <strong>₹64,350 a year at government colleges</strong>, "
        "₹1,09,350 at ESIC colleges, and usually <strong>₹1,53,571 or ₹1,56,621 at private colleges</strong> "
        "(a few private colleges differ; see the table).")

how_to = ("<strong>How to read the cutoffs:</strong> each cutoff is the highest NEET All India Rank that got a General Merit (GM) "
          "government seat at that college in that round. If your rank is lower (better) than a college's cutoff, "
          "that college was within reach in that round. Example: with rank 10,000, BMCRI (2,655) was out of reach in Round 1, "
          "while ESIC Bengaluru (11,745) was within reach. Cutoffs move every year, so treat them as a guide.")

note = ("Data: KEA UGNEET 2026 final allotment lists, only government-quota seats (course code ending MG) in the exact GM category. "
        "GM seats = GM government seats filled after Round 2, counted from the lists; KEA's official seat matrix may differ slightly. "
        "The Round 3 list covers only candidates who took part in Round 3, so a Round 3 cutoff can be lower than Round 2. "
        "– means no GM government seat was allotted at that college in that round (Bagalkote Medical College first appears in Round 2). "
        "Type is inferred from the KEA fee. Fees are as listed by KEA, including ₹0 at Sri Madhusudan Sai and ₹6,09,084 at "
        "Jagadguru Gangadhar Mahaswamigalu Moorusavirmath Medical College. Tap a column heading to sort.")

blocks = [
    {"type": "heading", "html": "Karnataka MBBS Colleges (KEA Government Seat, General Merit)"},
    {"type": "lead", "html": lead},
    {"type": "callout", "html": how_to},
    {"type": "subheading", "html": "Summary by district"},
    {"type": "table", "sortable": True,
     "columns": ["District", "Colleges", "Government", "ESIC", "Private", "GM govt seats"],
     "rows": sum_rows, "sortExclude": "last",
     "sources": SOURCES, "lastVerified": TODAY},
    {"type": "subheading", "html": "All colleges (sorted by Round 1 cutoff)"},
    {"type": "table", "sortable": True, "wide": True,
     "columns": ["College", "Location", "Type", "Govt-seat fee / yr", "GM seats", "2026 R1 cutoff", "R2 cutoff", "R3 cutoff"],
     "rows": main_rows, "sources": SOURCES, "lastVerified": TODAY},
    {"type": "note", "html": note},
]

c = json.load(open(content_path, encoding="utf-8"))
tab = next(t for t in c["tabs"] if t["id"] == "colleges")
B = tab["blocks"]
start = next(i for i, b in enumerate(B) if b["type"] == "heading" and b["html"].startswith("Karnataka Government Colleges"))
end = next(i for i, b in enumerate(B) if i > start and b["type"] == "heading")
B[start:end] = blocks

# ESIC Bengaluru entry in Central Government Colleges
esic = ("<strong>Open-category cutoff:</strong> ESIC Bangalore closes around AIR 8,000-15,000 in recent cycles.")
s = json.dumps(c, ensure_ascii=False)
assert s.count(json.dumps(esic, ensure_ascii=False)[1:-1]) == 1
t66 = next(t for t in table if t["code"] == "M066MG")
new = (f"<strong>KEA 2026 state-quota GM government seat:</strong> closing AIR {inr(t66['cut'][0])} (Round 1), "
       f"{inr(t66['cut'][1])} (Round 2), {inr(t66['cut'][2])} (Round 3); fee ₹1,09,350 a year. See the Karnataka table below.")
s = s.replace(json.dumps(esic, ensure_ascii=False)[1:-1], json.dumps(new, ensure_ascii=False)[1:-1])
c = json.loads(s)
json.dump(c, open(content_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("colleges", tot["colleges"], "seats", tot["seats"], "bengaluru", dict(blr))
for r in sum_rows: print(r)
