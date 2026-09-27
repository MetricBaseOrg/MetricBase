# MetricBase

Analyzing data by day, on-chain strategist by night. Data-driven research across energy markets, crypto, and Indonesian equities.

**Precision growth. No wasted motion.**

Live at [metricbase.org](https://metricbase.org).

## What's here

This repo is the static site behind metricbase.org:

- **Portal** (`index.html`): links to MetricBase products, the three blog verticals, and social channels.
- **Journal** (`journal.html`, `journal/`): original research reports, editorials, and the **Weekly Brief**, a cross-vertical market recap published every Monday. It covers energy, crypto, and the IDX through the prior Friday close.
- **Blog templates** (`blogs/`): Blogger XML themes for the three verticals. These are pasted into the Blogger admin panel, not served from here.
- **Standalone pages**: `about`, `contact`, `world`, the author page (`authors/bun.html`), and the legal pages (privacy, terms, cookie policy, disclaimer, editorial standards).

## Network

| | |
|---|---|
| Energy Markets | [energy.metricbase.org](https://energy.metricbase.org) |
| Crypto & Technology | [chain.metricbase.org](https://chain.metricbase.org) |
| Pasar Saham Indonesia | [saham.metricbase.org](https://saham.metricbase.org) |
| Products | [World](https://world.metricbase.org) · [Apps](https://apps.metricbase.org) · [OG-tools](https://og.metricbase.org) · [Portabase](https://portabase.metricbase.org) · [Bingkai](https://bingkai.metricbase.org) · [PumpBid](https://bid.metricbase.org) |
| Newsletter | [subs.metricbase.org](https://subs.metricbase.org) |
| Social | [X](https://x.com/MetricBase) · [Instagram](https://instagram.com/MetricBase) · [TikTok](https://tiktok.com/@MetricBase) |

## Development

Plain HTML/CSS/JS: no build step, package manager, or framework. Each page is self-contained, with inline styles and scripts. The header and footer are duplicated in every page, so a nav or footer change has to be made in all of them.

- **Preview:** open any `.html` file in a browser.
- **Journal feed:** after adding or editing a journal page, regenerate the JSON Feed that powers subscriber emails:
  ```sh
  node scripts/build-feed.mjs
  ```
- **Deploy:** pushing to `main` runs `.github/workflows/jekyll-gh-pages.yml`, which publishes the repo root to GitHub Pages.

Adding a Journal piece also means updating `journal.html` (card plus counts), `sitemap.xml`, and `feed.json`. See `CLAUDE.md` for the full Weekly Brief checklist and brand rules.

## Disclaimer

All content is for informational and educational purposes only and is not financial advice. See the [full disclaimer](https://metricbase.org/disclaimer).
