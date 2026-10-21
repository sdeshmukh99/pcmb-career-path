# Build the "Ayurveda Colleges" tab in content.json.
# Usage: python3 build_ayurveda.py tools_dir aaccc.json kea_ayush_r1.json content.json
# aaccc.json comes from aaccc_parse.py, kea_ayush_r1.json from kea_ayush_parse.py.
import json, sys
sys.path.insert(0, sys.argv[1])
from ayush_colleges import COLLEGES

aaccc_path, kea_path, content_path = sys.argv[2], sys.argv[3], sys.argv[4]
TODAY = "2026-10-21"
REPO = "https://github.com/sdeshmukh99/pcmb-career-path/blob/main/sources/ayurveda/"
AACCC_SOURCES = [
    {"label": "AACCC UG 2026 Round 1 final result (16 Sep 2026)",
     "url": REPO + "aaccc/aaccc-ug-2026-round-1-seat-allotment-result-2026-09-16.pdf"},
    {"label": "AACCC UG 2026 Round 2 final result (2 Oct 2026)",
     "url": REPO + "aaccc/aaccc-ug-2026-round-2-seat-allotment-result-2026-10-02.pdf"},
    {"label": "AACCC UG information bulletin 2026-27",
     "url": REPO + "aaccc/aaccc-ug-2026-27-information-bulletin-2026-08-31.pdf"},
    {"label": "AACCC official website", "url": "https://aaccc.gov.in/"},
]
KEA_SOURCES = [
    {"label": "KEA UGNEET 2026 AYUSH Round 1 final allotment list (16 Oct 2026)",
     "url": REPO + "kea/kea-ugneet-2026-ayush-round-1-final-allotment-2026-10-16.pdf"},
    {"label": "KEA official website", "url": "https://kea.kar.nic.in/"},
]

# (short name, location, keyword in the AACCC institute name, share of BAMS seats AACCC fills)
NATIONAL = [
    ("National Institute of Ayurveda (NIA), Jaipur", "Jaipur, Rajasthan", "Jaipur", "100%"),
    ("Faculty of Ayurveda, IMS, Banaras Hindu University", "Varanasi, Uttar Pradesh", "Banaras", "100%"),
    ("Institute of Teaching and Research in Ayurveda (ITRA)", "Jamnagar, Gujarat", "Teaching and Research", "100%"),
    ("National Institute of Ayurveda (NIA), Panchkula", "Panchkula, Haryana", "Panchkula", "100%"),
    ("All India Institute of Ayurveda (AIIA), Goa", "Dhargal, North Goa", "All India Institute of Ayurveda", "50%"),
    ("North Eastern Institute of Ayurveda and Homoeopathy (NEIAH)", "Shillong, Meghalaya",
     "NORTH EASTERN INSTITUTE OF AYURVEDA AND HOMEOPATHY", "50%"),
    ("North Eastern Institute of Ayurveda and Folk Medicine Research (NEIAFMR)", "Pasighat, Arunachal Pradesh",
     "Folk Medicine", "50%"),
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


def national_rows(d):
    # Open (non-PwD) BAMS seats in the Central Universities / National Institutions quota.
    # Round 2 counts only seats allotted in Round 2 (fresh or upgraded), not seats kept from Round 1.
    def ranks(rd, key):
        if rd == 1:
            return [int(r[1]) for r in d["r1"] if r[2].startswith("Central") and "Ayurvedic" in r[4]
                    and r[5] == "Open" and key.lower() in r[3].lower()]
        return [int(r[1]) for r in d["r2"] if r[6].startswith("Central") and "Ayurvedic" in r[8]
                and r[9] == "Open" and key.lower() in r[7].lower()]
    out = []
    for name, loc, key, share in NATIONAL:
        r1, r2 = ranks(1, key), ranks(2, key)
        assert r1 and r2, name
        out.append([name, loc, share, str(len(r1)), inr(max(r1)), inr(max(r2)), "Pending"])
    out.sort(key=lambda r: int(r[4].replace(",", "")))
    return out


def kea_rows(rows):
    seats, fees = {}, {}
    for x in rows:
        if x["course"] != "BAMS-Govt":
            continue
        fees.setdefault(x["code"], set()).add(x["fee"])
        if x["cat"] == "GM":
            seats.setdefault(x["code"], []).append(x["air"])
    assert set(fees) == set(COLLEGES), set(fees) ^ set(COLLEGES)
    assert all(len(f) == 1 for f in fees.values())
    kind = {30335: "Government", 60000: "Aided", 75000: "Private"}
    out = []
    for code, (name, loc) in COLLEGES.items():
        fee = fees[code].pop()
        a = seats.get(code, [])
        out.append((max(a) if a else 10**9,
                    [name, loc, kind[fee], "₹" + inr(fee), str(len(a)), inr(max(a)) if a else "–"]))
    out.sort(key=lambda t: t[0])
    return [r for _, r in out]


aaccc = json.load(open(aaccc_path))
kea = json.load(open(kea_path))
nat = national_rows(aaccc)
kar = kea_rows(kea)
count = {k: sum(r[2] == k for r in kar) for k in ("Government", "Aided", "Private")}

tab = {
    "id": "ayurveda",
    "label": "Ayurveda Colleges",
    "blocks": [
        {"type": "intro", "html": "BAMS (Bachelor of Ayurvedic Medicine and Surgery) admission uses your NEET UG rank. "
         "Two counsellings matter for a Karnataka student: <strong>AACCC</strong> for the national institutes and the 15% "
         "All India Quota, and <strong>KEA</strong> for Karnataka's own seats. All cutoffs below are for the "
         "<strong>Open / General Merit</strong> category only."},
        {"type": "heading", "html": "National Ayurveda Institutes (AACCC)"},
        {"type": "lead", "html": "AACCC (Ayush Admissions Central Counseling Committee) fills these seats on All India "
         "rank, with no state domicile. It fills all BAMS seats at BHU, ITRA, NIA Jaipur and NIA Panchkula, and half the "
         "BAMS seats at AIIA Goa, NEIAH Shillong and NEIAFMR Pasighat, as listed in the AACCC UG information bulletin "
         "2026-27."},
        {"type": "callout", "html": "Each cutoff is the highest NEET All India Rank that got an Open seat at that "
         "institute in that round. A rank lower (better) than the cutoff was within reach in that round. Round 2 fills "
         "only the seats left after Round 1, so its cutoff can be better than Round 1's (NIA Jaipur went from 31,719 to "
         "29,913). The Round 3 result had not been published when this table was made."},
        {"type": "table", "sortable": True, "wide": True,
         "columns": ["Institute", "Location", "BAMS seats via AACCC", "Open seats allotted in R1",
                     "2026 R1 cutoff", "R2 cutoff", "R3 cutoff"],
         "rows": nat, "sources": AACCC_SOURCES, "lastVerified": TODAY},
        {"type": "note", "html": "Data: AACCC UG 2026 final results for Rounds 1 and 2, Central Universities / National "
         "Institutions quota, BAMS, Open category without PwD. The R2 cutoff counts only seats allotted in Round 2, not "
         "seats kept from Round 1. NIA Jaipur also filled 9 seats through the All India Quota Government list; those are "
         "not counted. AIIA New Delhi does not appear in either BAMS result. AACCC does not publish college fees; check "
         "each institute's website."},
        {"type": "heading", "html": "Karnataka BAMS Colleges (KEA Government Seat, General Merit)"},
        {"type": "lead", "html": f"{len(kar)} colleges offered KEA government-quota BAMS seats in Round 1 of 2026: "
         f"{count['Government']} government, {count['Aided']} aided and {count['Private']} private. The fee for a "
         "government seat is fixed by KEA: <strong>₹30,335 a year at government colleges</strong>, ₹60,000 at aided "
         "colleges and <strong>₹75,000 at private colleges</strong>."},
        {"type": "callout", "html": "Each cutoff is the highest NEET All India Rank that got a General Merit (GM) "
         "government seat at that college in Round 1. Only the Round 1 list for 2026 is available here, so later rounds "
         "are not shown. In later rounds cutoffs usually move to worse ranks as seats open up again, so a college just "
         "outside your rank in Round 1 can still come within reach."},
        {"type": "subheading", "html": "All colleges (sorted by Round 1 cutoff)", "collapsible": True},
        {"type": "table", "sortable": True, "wide": True, "filterable": True,
         "columns": ["College", "Location", "Type", "Govt-seat fee / yr", "GM seats allotted in R1", "2026 R1 cutoff"],
         "rows": kar, "sources": KEA_SOURCES, "lastVerified": TODAY},
        {"type": "note", "html": "Data: KEA UGNEET 2026 AYUSH Round 1 final allotment list, only BAMS government-quota "
         "seats (course code ending AG) in the exact GM category. GM seats allotted is a count from the list, not KEA's "
         "seat matrix. Type is inferred from the KEA fee. – means no GM government seat was allotted at that college in "
         "Round 1."},
        {"type": "heading", "html": "How Admission Works"},
        {"type": "accordion", "entries": [
            {"id": "aaccc-ug-counselling", "title": "AACCC counselling (national institutes and 15% All India Quota)",
             "tag": {"text": "Guide", "style": "default"},
             "body": [{"type": "list", "items": [
                 "AACCC fills 15% of seats at government and aided Ayurveda colleges in every state, and the national "
                 "institute seats in the table above. Seats go by NEET UG 2026 rank.",
                 "There are four rounds: Round 1, Round 2, Round 3 and a Stray Vacancy Round (in two phases). Seats left "
                 "after Round 3 go to the Stray Vacancy Round.",
                 "At registration you pick a counselling type. For government, aided and national-institute seats you pay "
                 "a non-refundable fee of ₹1,000 (₹500 for SC, ST and PwBD) plus a refundable security deposit of "
                 "₹20,000. Deemed universities cost ₹5,000 plus ₹50,000.",
                 "Each round has a provisional result first, then a final result. Requests about the allotment are "
                 "accepted only before the final result.",
                 "Free exit (leaving without penalty) applies to Round 1 seats. From Round 2 onward, not joining an "
                 "allotted seat or leaving it forfeits the security deposit.",
                 "A seat allotted in Round 3 or the Stray Vacancy Round cannot be left. A candidate who leaves it loses the "
                 "fees and becomes ineligible for every Ayush UG counselling, central or state, for that year.",
                 "AACCC does not set college fees. The bulletin asks candidates to confirm fees, bond and stipend with each "
                 "college before choosing it.",
             ]}],
             "sources": [AACCC_SOURCES[2], AACCC_SOURCES[3]], "lastVerified": TODAY},
            {"id": "kea-ayush-counselling", "title": "KEA counselling (Karnataka BAMS seats)",
             "tag": {"text": "Guide", "style": "default"},
             "body": [{"type": "list", "items": [
                 "KEA fills Karnataka's government-quota BAMS seats at government, aided and private colleges, using the "
                 "same NEET UG rank. Karnataka state-quota eligibility rules apply.",
                 "The KEA AYUSH list is separate from the MBBS list. In 2026 the AYUSH Round 1 final list came out on "
                 "16 October, ten days after the KEA MBBS Round 3 list (6 October).",
                 "The fee shown in the table is KEA's government-seat fee. Private-quota and management seats at the same "
                 "colleges cost more (₹3,00,000 a year for a private-quota BAMS seat in the 2026 list).",
                 "The MBBS tab explains the KEA round choices (accept, upgrade, give up, exit). Check KEA's AYUSH notices "
                 "for the AYUSH dates, which differ from MBBS.",
             ]}],
             "sources": KEA_SOURCES, "lastVerified": TODAY},
        ]},
    ],
}

c = json.load(open(content_path))
tabs = [t for t in c["tabs"] if t["id"] != "ayurveda"]
i = next(k for k, t in enumerate(tabs) if t["id"] == "colleges")
tabs[i]["label"] = "MBBS Colleges"
tabs.insert(i + 1, tab)
c["tabs"] = tabs
json.dump(c, open(content_path, "w"), ensure_ascii=False, indent=2)
print("national", len(nat), "karnataka", len(kar), count)
