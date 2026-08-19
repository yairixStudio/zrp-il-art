# Zielinski & Rozen — The Art Galleries

**The official website of the Zielinski & Rozen art galleries in Tel Aviv — a hand-built static site with responsive AVIF + WebP image delivery.**

Live site: **[art.zrp.co.il](https://art.zrp.co.il/)**

Zielinski & Rozen runs a network of contemporary art galleries in Tel Aviv (Kikar HaMedina, Dizengoff Square) showing Israeli artists. This repository is the production site: ~230 static HTML pages covering 42 artists, 140+ individual artworks, exhibitions, events, press coverage, and open calls — Hebrew-first content with the brand's bilingual Hebrew/English typography. No framework and no build step: the repository root is exactly what GitHub Pages serves.

## Highlights

- **AVIF + WebP only** — roughly 1,500 image pairs ship as `{name}.webp` + `{name}.avif`; original PNG/JPG masters stay out of the repo (`_originals/`, gitignored). Pages reference the `.webp`, and [`components/picture-upgrade.js`](components/picture-upgrade.js) wraps each `<img>` into a `<picture>` with an `image/avif` source at runtime — so modern browsers fetch AVIF while the WebP `<img>` remains the fetch-before-JS fallback. Responsive `srcset`/`sizes` are mirrored onto the AVIF source, and a `MutationObserver` upgrades images injected later by JS.
- **Performance conventions on every image** — explicit `width`/`height` (no layout shift), `loading="lazy"` + `decoding="async"` everywhere, `fetchpriority="high"` on the LCP image, and responsive `srcset` variants for hero images. Lighthouse audit scripts are wired up in `package.json` (the only dev dependency).
- **Self-hosted fonts, no third-party font CDNs** — Copperplate (Latin), FbEzmel (Hebrew), Solway, and Noto Sans Arabic served from the repo as WOFF2 (with OTF/TTF fallbacks), with `font-display: swap` and preload hints.
- **JSON as the single source of truth** — site content (artists, works, exhibitions, events, press, galleries…) lives in [`data/`](data/) with JSON Schemas in `data/_schema/`; Python tools in [`tools/`](tools/) keep the inline HTML mirrors in sync.
- **Shared vanilla-JS components** — artwork lightbox, three gallery/carousel variants, site chrome, and an analytics loader (GA4 + Microsoft Clarity) in [`components/`](components/); no framework, no bundler.
- **SEO & sharing** — full `sitemap.xml`, `robots.txt`, per-page Open Graph cards pre-rendered as JPGs in [`og/`](og/), and a custom 404 page.
- **Newsletter signup** — the static form posts to a Wix Velo HTTP function; the backend source lives in [`newsletter-backend/`](newsletter-backend/) and is deployed on the brand's Wix site (spam honeypot, per-IP rate limiting, email validation).

## Structure

```
index.html            Homepage
artists/<slug>/       42 artist pages
works/<slug>/         Individual artwork pages (140+)
exhibitions/          Exhibition pages
events/               Event pages (openings, artist talks)
galleries/            Gallery-location pages (Medina, Dizengoff)
press/                Press articles
opencalls/            Open-call pages
about/ contact/ …     Info, accessibility, privacy pages
components/           Shared CSS/JS (lightbox, galleries, picture-upgrade, analytics)
data/                 JSON content + JSON Schemas (single source of truth)
images/               Processed WebP + AVIF assets only
og/                   Pre-rendered Open Graph share images
פונטים/               Self-hosted WOFF2/OTF fonts
tools/, scripts/      Python sync tools, local dev server
docs/                 Internal conventions and component docs
```

## Run locally

Any static file server works. The repo includes an idempotent dev-server script (Python 3, port 8765):

```bash
git clone https://github.com/yairixStudio/zrp-il-art.git
cd zrp-il-art
./scripts/local-dev-server.sh    # → http://127.0.0.1:8765/
```

Or simply:

```bash
python3 -m http.server 8765
```

Optional Lighthouse audits (requires `npm install` first):

```bash
npm run lighthouse           # or lighthouse:mobile / lighthouse:desktop
```

## Deployment

Served by **GitHub Pages** from the `main` branch root (`.nojekyll`), on the custom domain **art.zrp.co.il** (`CNAME`) with HTTPS enforced. Pushing to `main` deploys the site — there is no build pipeline; image conversion to WebP/AVIF happens before assets are committed.

## Links

- Live site: [https://art.zrp.co.il](https://art.zrp.co.il)
- Instagram: [@erezzielinskirozen](https://www.instagram.com/erezzielinskirozen/)
- Repository: [https://github.com/yairixStudio/zrp-il-art](https://github.com/yairixStudio/zrp-il-art)

## Author

Site built and maintained by **Yairix Studio** (yairixstudio@gmail.com) for Zielinski & Rozen. All artwork images, photographs, and brand assets belong to Zielinski & Rozen and the respective artists.
