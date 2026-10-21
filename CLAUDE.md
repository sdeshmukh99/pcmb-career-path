# Notes for Claude: pcmb-career-path

Public career reference site for PCMB students (CBSE 2027 cohort). The owner is not a coder:
explain every step in plain language and say exactly what they need to do.

## Site

- Live: https://per-pcmb-career-path.claim69bobble3.workers.dev/ (Cloudflare Worker `per-pcmb-career-path`).
- Preview of the working branch: https://claude-gracious-goldberg-xy0zw1-per-pcmb-career-path.claim69bobble3.workers.dev
  (Cloudflare also posts the preview link as a comment on each PR).
- `public/content.json` holds all content; `public/index.html` only renders it. `public/` is the only published folder.
- `wrangler.jsonc`: the `name` must stay `per-pcmb-career-path` (a mismatch fails every build), and the empty
  `previews` block is required for branch previews (`wrangler preview`).
- `sources/` holds official documents (KEA PDFs) with descriptive names. Not published; linked from `sources` fields.
- `tools/` holds the one-off scripts used to build the Karnataka table from KEA's 2026 allotment lists
  (`pdftotext -layout` each PDF to r1/r2/r3.txt, then `kea_parse.py`, `colleges.py`, `build_karnataka.py`).
  `build_karnataka.py` looks for the old section heading, so adapt it before reusing it for a new year.
- Karnataka BAMS table: `pdftotext -layout` the three KEA AYUSH lists in `sources/` to a25r2/a25r3/a26r1.txt in one folder,
  then `python3 tools/ayush_parse.py <folder>` and `python3 tools/ayush_table.py <folder>/rows.json <out.json>` (run from the
  repo root; names and locations live in `tools/ayush_colleges.py`). Paste the rows into the BAMS table in `content.json`.

## Workflow (agreed with the owner)

1. Change things on a branch and open a PR. Never push straight to `main`.
2. Wait for the Cloudflare preview build to pass, then send the owner the preview link.
3. Merge (squash) only after the owner says "go live". Merging to `main` deploys to the live site.
4. Confirm the production build: `curl https://api.github.com/repos/sdeshmukh99/pcmb-career-path/commits/<sha>/check-runs`.
   Cloudflare has sometimes missed a push; if no check run appears within a few minutes, push a new commit
   (through a PR) to trigger it again.
5. Bump `site.version` and `site.lastUpdated` in `content.json` on every content change.
6. Ask before substantial changes; the owner often says "wait for my approval".

## Content rules

- No personal information about any individual. Write in neutral terms ("you", "students"), not "her" or "she".
- Never invent facts or sources. Every career entry has `sources` and `lastVerified`; fill them only from sources
  actually checked, and leave `lastVerified` null otherwise.
- Prefer official sources (KEA, NMC, NTA, MCC) over blogs. Say which points come from secondary sites.
- Karnataka table: KEA government-quota seats only (course code ending MG), exact GM category, 2026 Rounds 1 to 3.
  Cutoff = highest AIR allotted a GM government seat in that round. Seats = GM seats filled after Round 2.
- No emojis in published content.

## Open items (as of 21 October 2026)
- Ayurveda: Karnataka BAMS table added (KEA 2026 R1, 2025 R2 and R3). Still missing: KEA 2026 Round 2 list, and AACCC
  (All India) allotment and fee data for colleges outside Karnataka.
- Most Healing Paths and Non-Healing Path entries still have no sources or verification date.
- Fact-check files per tab can be regenerated from `content.json` for checking in Perplexity.
