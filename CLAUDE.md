# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MetricBase is a data-driven content brand. The site is a content portal linking visitors to three blog verticals and four social platforms.

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

No build system, package manager, tests, or linters. Development is editing files directly.

Pushing to `main` triggers `.github/workflows/jekyll-gh-pages.yml`, which builds with Jekyll and deploys to GitHub Pages at metricbase.org. Jekyll only serves static files here — there is no `_config.yml`, no Liquid templates, and no Jekyll-specific features in use. The workflow treats the repo root as the source.

To preview locally: open `index.html` directly in a browser. Blog templates (`blogs/*.html`) are Blogger XML and must be uploaded to the Blogger admin panel — they cannot be previewed locally.

## Weekly Brief workflow (recurring — keep it current)

The Journal publishes a **Weekly Brief** every week, and it must not be allowed to lapse. This is a standing instruction from the site owner, not a one-off (see the wiki memory `MetricBase-wiki/memory/metricbase/project-weekly-brief-workflow.md`). At session start, check whether the latest `journal/weekly-brief-<N>.html` is current for today's date; if it has fallen behind, write the missing edition(s) to catch up.

**Cadence & dating:** one numbered edition per week, **published Monday**, covering market data **through the prior Friday close**. Editions are strictly sequential (`#1` 5 May 2026 → `#7` 15 Jun 2026 → `#8` ~22 Jun …). Each edition spans the same three verticals in order: **01 Energy Markets · 02 Crypto & Technology · 03 Pasar Saham Indonesia (IDX)**.

**Continuity is the point.** Before writing edition `N`, read edition `N-1`: each brief must resolve the previous "Watch Next Week" items and carry the running cross-vertical narrative (price levels, theses, call-backs) forward consistently.

**Content must be factual and up to date — never fabricated.** Every figure (WTI/Brent, EIA, Henry Hub, BTC/ETH-BTC/dominance/OI/funding, IDX, ADRO/ITMG/BBCA/BBRI, USD/IDR) and every event (OPEC+, Bank Indonesia, US CPI) must be a real, sourced data point for the stated week — the actual prior-Friday closes. **Source the data before writing**: crypto via the Crypto.com MCP (`get_candlestick`/`get_ticker`); energy, IDX equities, FX, and macro via live retrieval (WebSearch/WebFetch) or data the owner supplies. Claude's training knowledge (cutoff Jan 2026) cannot supply current-year prices — never write a figure from memory and present it as fact; if it can't be sourced, fetch it with tools or ask. "Up to date" means the latest edition covers the week that just closed, not a post-dated future week. The "educational, not financial advice" disclaimer stays, but it does not license invented numbers. (Editions #1–#7 were drafted as illustrative commentary and still need a sourcing pass before they count as factual.)

**To add an edition** (all in this repo):
1. Copy the structure of the most recent `journal/weekly-brief-<N>.html` — every brief shares an identical `<style>` block, header, footer, and script; only the `<head>` meta/JSON-LD, hero, data-flash, three verticals, watch-list, and related cards change. Keep the brand tokens (`#0a0a0a` / `#c9a84c` gold / Manrope + JetBrains Mono) untouched.
2. Update the new file's edition number (`WB-00N`), `weekly-brief-<N>` canonical/OG/breadcrumb URLs, published + data dates, and the "Related" grid (link the immediately previous brief + the research report).
3. In `journal.html`: add a new `<a class="article-card" … data-category="weekly-brief">` card at the **top** of the brief list (newest first), and bump both `#count-all` and `#count-weekly-brief`.
4. In `sitemap.xml`: add a `<url>` for `/journal/weekly-brief-<N>` (lastmod = publish date) and bump the `/journal` `lastmod`.
5. Verify: no stray non-ASCII, well-formed `sitemap.xml`, card counts match the number of cards.

## Architecture

### `index.html` — Content Portal (~1200 lines)

Single-file HTML/CSS/JS. All styles are inline in a `<style>` block; all JS is inline before `</body>`. No external CSS or JS files.

CSS custom properties are defined once at the top of the `<style>` block under `:root` and must be used for all color/typography values — never hardcode hex values outside `:root`.

**Page sections (in order):**
1. `#portal-hero` — brand mark, tagline, sub-copy, pill links to verticals
2. `#strip` — credibility strip with four positioning statements
3. `#verticals` — three content vertical cards (Energy, Crypto, Stocks)
4. `#social` — four social platform cards (X, Instagram, TikTok, Email)
5. `#subscribe` — Kit.com email capture form

**JavaScript responsibilities (inline, ~80 lines):** mobile drawer toggle, footer accordion, back-to-top scroll, scroll-progress bar, Intersection Observer for `.reveal` animations, localStorage-based cookie consent.

### Blog Templates — Blogger XML

`blogs/energy.html`, `blogs/chain.html`, `blogs/saham.html` are Blogger XML templates. They use Blogger template syntax: `<b:if>`, `<b:loop>`, `data:blog.*` variables, and `<b:skin><![CDATA[...]]></b:skin>` for styles.

Each template shares the same structure: OG + Twitter Card meta, TradingView ticker widget, navigation drawer linking to all three verticals, and footer with social links. CSS inside `<b:skin>` uses the same `:root` custom properties as `index.html`.

OG image falls back to `https://metricbase.org/assets/MetricBase.png` when no post thumbnail is available — this pattern is consistent across all three templates.

## Style Guidelines

See `assets/branding-style.md` for the full brand spec.

- Strict color palette (no additions): `#0a0a0a` background, `#c9a84c` gold accents, white (`#f5f5f5`) for contrast, subtle grays (`#111`, `#1a1a1a`, `#222`, `#555`, `#888`, `#ccc`)
- Font: Inter (Google Fonts), weights 300/400/500/600/700
- CSS class prefix `mb-` for all component classes in `index.html`
- No emojis. No corporate tone. Max 2–3 lines per paragraph.
- Mobile-first; breakpoints at 640px and 900px

## Key Conventions

- **Scroll animations:** Add class `reveal` to any element. Optionally add `reveal-delay-1` through `reveal-delay-4` for staggered entry. The Intersection Observer adds `visible` on viewport entry. Never trigger animations via JS directly — always use this class pattern.
- **Section containers:** Use `<div class="mb-container">` inside every `<section>` in `index.html`.
- **Financial disclaimer and cookie consent** are legally required — do not remove them.
- **Google Analytics** ID: `G-HQ2SCQZ3KT` (in `index.html` head)
- **AdSense** publisher ID: `pub-6244083942838780` (in `index.html`, blog templates, and `ads.txt`)
- **Kit.com** form endpoint: `https://app.kit.com/forms/9390641/subscriptions`
- **TradingView** ticker widget is embedded in all three blog templates

## Brand Character

The mascot is "Bun" — a chibi anthropomorphic penguin with a manbun and white-frame 3D glasses (red/blue lenses). Character assets are in `assets/`. Use these for thumbnails and social content. Every visual must derive from the brand's dark-fintech aesthetic: think Bloomberg terminal, not lifestyle blog.
