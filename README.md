# pcmb-career-path
Career Options and Way to Get There for PCMB

## Structure

- `public/content.json` holds all page content. Edit this file to change what the site says.
- `public/index.html` only loads `content.json` and displays it. It holds no career content.
- `wrangler.jsonc` tells Cloudflare to publish the `public` folder as the
  `per-pcmb-career-path` Worker.

Every change merged into `main` is published automatically by Cloudflare Workers Builds.

`sources/` holds the official documents the content is built from. It is not published on the site.

- `sources/mbbs/`: KEA MBBS allotment lists and notices.
- `sources/ayurveda/aaccc/`: AACCC (national) information bulletins, seat matrices, final allotment results and notices.
- `sources/ayurveda/kea/`: KEA AYUSH allotment lists.
- `sources/ayurveda/notes/`: secondary analyses (not official sources).

`index.html` fetches `content.json` over HTTP, so both files must be deployed side by side.
Opening `index.html` directly from disk will not work; preview locally with
`python3 -m http.server -d public` and open http://localhost:8000.

## content.json

- `site.lastUpdated` (`YYYY-MM-DD`) and `site.version` appear in the footer. Update both on every change.
- `tabs[]` are the top tabs, shown in order. The first tab opens by default.
- Each career entry (inside an `accordion` block) has:
  - `id`, `title`, `tag` (`style`: `default`, `alt`, `warn` or `neutral`)
  - `meta[]` (optional label/value grid) and `body[]` (`p`, `note`, `list`, `callout` blocks)
  - `sources[]`: `{ "label": "...", "url": "https://..." }`
  - `lastVerified`: `YYYY-MM-DD`, or `null` if not yet verified
- The Karnataka cutoff table and the exam timeline also carry `sources` and `lastVerified`.

Fields ending in `html` are inserted as markup, so only trusted maintainers should edit this file.
Do not add personal information about any individual.
