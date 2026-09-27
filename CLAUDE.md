# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MetricBase is a data-driven content brand. metricbase.org is a static portal that links out to six products on their own subdomains (World, apps, og, Portabase, Bingkai, PumpBid/bid), three Blogger verticals, and four social platforms, and hosts the native **Journal** (weekly briefs, research reports, editorials).

- **Audience:** Tech enthusiasts, professionals, students, traders, and investors (mostly male, 25–34) who want informative, data-driven content.
- **Tone:** Sharp, intelligent, slightly contrarian. No hype. No fluff.
- **Positioning:** "Bridging data and digital logic"
- **Tagline:** "Precision growth. No wasted motion."

## Content Platforms

| Platform | URL |
|---|---|
| X / Twitter | https://x.com/MetricBase |
| Instagram | https://instagram.com/MetricBase |
| TikTok | https://tiktok.com/@MetricBase |
| Email Subscription | https://subs.metricbase.org |
| Blog — Energy | https://energy.metricbase.org |
| Blog — Crypto & Technology | https://chain.metricbase.org |
| Blog — Pasar Saham Indonesia | https://saham.metricbase.org |

## Deployment

No build system, package manager, tests, or linters. Development is editing files directly. The one script is `node scripts/build-feed.mjs`, which regenerates `feed.json` (JSON Feed 1.1) from the `<head>` meta of every `journal/*.html` (canonical, `og:title`, `og:description`, `article:published_time`; category comes from the filename prefix `weekly-brief-` / `research-` / `editorial-`). Re-run it and commit `feed.json` whenever a journal page is added or its meta changes: apps.metricbase.org reads this feed to email subscribers about new content.

URLs are extensionless (`https://metricbase.org/journal/weekly-brief-7` → `journal/weekly-brief-7.html`); GitHub Pages resolves them. Use that form in canonicals, OG tags, the sitemap, and internal links.

Pushing to `main` triggers `.github/workflows/jekyll-gh-pages.yml`, which builds with Jekyll and deploys to GitHub Pages at metricbase.org. Jekyll only serves static files here — there is no `_config.yml`, no Liquid templates, and no Jekyll-specific features in use. The workflow treats the repo root as the source.

To preview locally: open `index.html` directly in a browser. Blog templates (`blogs/*.html`) are Blogger XML and must be uploaded to the Blogger admin panel — they cannot be previewed locally.

## Weekly Brief workflow (recurring — keep it current)

The Journal publishes a **Weekly Brief** every week, and it must not be allowed to lapse. This is a standing instruction from the site owner, not a one-off (see the wiki memory `MetricBase-wiki/memory/metricbase/project-weekly-brief-workflow.md`). At session start, check whether the latest `journal/weekly-brief-<N>.html` is current for today's date; if it has fallen behind, write the missing edition(s) to catch up.

**Cadence & dating:** one numbered edition per week, **published Monday**, covering market data **through the prior Friday close**. Editions are strictly sequential (`#1` 5 May 2026 → `#7` 15 Jun 2026 → `#8` ~22 Jun …). Each edition spans the same three verticals in order: **01 Energy Markets · 02 Crypto & Technology · 03 Pasar Saham Indonesia (IDX)**.

**Continuity is the point.** Before writing edition `N`, read edition `N-1`: each brief must resolve the previous "Watch Next Week" items and carry the running cross-vertical narrative (price levels, theses, call-backs) forward consistently.

**Content must be factual and up to date — never fabricated.** Every figure (WTI/Brent, EIA, Henry Hub, BTC/ETH-BTC/dominance/OI/funding, IDX, ADRO/ITMG/BBCA/BBRI, USD/IDR) and every event (OPEC+, Bank Indonesia, US CPI) must be a real, sourced data point for the stated week — the actual prior-Friday closes. **Source the data before writing**: crypto via the Crypto.com MCP (`get_candlestick`/`get_ticker`); energy, IDX equities, FX, and macro via live retrieval (WebSearch/WebFetch) or data the owner supplies. Claude's training knowledge (cutoff Jan 2026) cannot supply current-year prices — never write a figure from memory and present it as fact; if it can't be sourced, fetch it with tools or ask. "Up to date" means the latest edition covers the week that just closed, not a post-dated future week. The "educational, not financial advice" disclaimer stays, but it does not license invented numbers. (Editions #1–#7 were drafted as illustrative commentary and still need a sourcing pass before they count as factual. #8 onward are sourced, and each ends with a "Sources" block linking the articles and data behind its figures; keep that block in every new edition.)

**To add an edition** (all in this repo):
1. Copy the structure of the most recent `journal/weekly-brief-<N>.html` — every brief shares an identical `<style>` block, header, footer, and script; only the `<head>` meta/JSON-LD, hero, data-flash, three verticals, watch-list, and related cards change. Keep the brand tokens (`#0a0a0a` / `#c9a84c` gold / Manrope + JetBrains Mono) untouched.
2. Update the new file's edition number (`WB-00N`), `weekly-brief-<N>` canonical/OG/breadcrumb URLs, published + data dates, and the "Related" grid (link the immediately previous brief + the research report).
3. In `journal.html`: add a new `<a class="article-card" … data-category="weekly-brief">` card at the **top** of the brief list (newest first), and bump both `#count-all` and `#count-weekly-brief`.
4. In `sitemap.xml`: add a `<url>` for `/journal/weekly-brief-<N>` (lastmod = publish date) and bump the `/journal` `lastmod`.
5. Run `node scripts/build-feed.mjs` to regenerate `feed.json`, and update the `#journal-preview` cards in `index.html` if the brief should appear there.
6. Verify: no stray non-ASCII, well-formed `sitemap.xml`, card counts match the number of cards.

## Architecture

Every page is a self-contained HTML file: its own inline `<style>` (with its own `:root` tokens) and inline `<script>` before `</body>`. There are no shared CSS/JS files and no includes, so **the header nav, mobile drawer, and footer are duplicated in every page**. A site-wide change to nav/footer links (e.g. adding a product) means editing every `*.html`, `journal/*.html`, and `authors/bun.html` and keeping them in sync.

- `index.html` (~1900 lines) — homepage. Sections in order: `#hero`, `#products` (six product cards), `#verticals`, `#world-teaser`, `#journal-preview` (hand-maintained cards for the latest Journal pieces), `#social`, `#subscribe` (Kit.com form), `#featured-blogs`. Product links carry `data-track="<product>" data-placement="<slot>"`; inline JS sends these as GA `select_product` events. Only `index.html` loads GA and AdSense.
- `journal.html` — Journal index. Cards are `<a class="article-card" data-category="weekly-brief|research|editorial">`; a JS filter bar uses them, and `#count-all` / `#count-<category>` are hardcoded numbers that must match the card counts.
- `journal/*.html` — articles. Filename prefix sets the category (used by `journal.html` and `scripts/build-feed.mjs`). Each carries full OG/Twitter meta, `article:published_time`, and JSON-LD.
- `world.html`, `about.html`, `contact.html`, `authors/bun.html`, and legal pages (`privacy`, `terms`, `cookie-policy`, `disclaimer`, `editorial-standards`) — standalone pages sharing the same look.
- `sitemap.xml`, `robots.txt`, `ads.txt`, `feed.json` — hand-maintained (except `feed.json`, generated). Add a `<url>` to the sitemap for any new page.
- `blogs/energy.html`, `blogs/chain.html`, `blogs/saham.html` — **Blogger XML templates**, not site pages. They use `<b:if>`, `<b:loop>`, `data:blog.*`, and `<b:skin><![CDATA[...]]></b:skin>`; they must be pasted into the Blogger admin and cannot be previewed locally. All three share one structure (OG/Twitter meta with fallback image `https://metricbase.org/assets/MetricBase.webp`, TradingView ticker widget, drawer linking all three verticals, social footer), so a change to one usually belongs in all three.

## Style Guidelines

See `assets/branding-style.md` for the full brand spec.

- Palette: `#0a0a0a` background, `#c9a84c` gold accents, white for contrast, grays only. Use the page's `:root` tokens (`--bg`, `--bg-card`, `--gold`, `--gold-bright`, `--gray-1..4`, `--line`, ...) instead of hardcoding hex values. The one sanctioned exception is the teal `--world-accent*` tokens, scoped to MetricBase World (`#world-teaser`, `world.html`).
- Fonts: Manrope (text) + JetBrains Mono (labels, numbers, data) from Google Fonts, used on every page and in the Blogger templates.
- Class names are plain descriptive (`container`, `section-label`, `section-title`, `vertical-card`, ...); there is no prefix convention.
- No emojis. No corporate tone. Max 2–3 lines per paragraph.
- Mobile-first; main breakpoints 640px and 900px (index also uses 1024px and 400px).

## Key Conventions

- **Scroll animations:** add class `reveal`, optionally `reveal-d1` … `reveal-d4` for stagger. An IntersectionObserver adds `visible`; don't animate from JS directly.
- **Financial disclaimer and cookie consent banner** (every page; consent stored in `localStorage` key `mb_cookie_consent`; `index.html` sets Google Consent Mode to default-denied before gtag loads and upgrades it on acceptance) are legally required. Do not remove them.
- **Google Analytics** `G-HQ2SCQZ3KT` and **AdSense** `pub-6244083942838780` (index, blog templates, `ads.txt`).
- **Kit.com** form endpoint: `https://app.kit.com/forms/9390641/subscriptions`.

## Brand Character

The mascot is "Bun" — a chibi anthropomorphic penguin with a manbun and white-frame 3D glasses (red/blue lenses). Character assets (PNG + WebP pairs) are in `assets/`. Use these for thumbnails and social content. Every visual must derive from the brand's dark-fintech aesthetic: think Bloomberg terminal, not lifestyle blog.
