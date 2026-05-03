# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MetricBase is a static marketing/lead-generation website for a market intelligence brand targeting traders in crypto, energy, and macro markets. The site's primary goal is email list growth via a free guide ("5 Signals Smart Money Uses Before a Pump").

## Running Locally

No build step required — open `index.html` directly in a browser, or serve it with:

```bash
python -m http.server 8080
```

## Deployment

Pushing to `main` automatically triggers GitHub Actions (`.github/workflows/jekyll-gh-pages.yml`), which builds with Jekyll and deploys to GitHub Pages (metricbase.org).

There are no tests and no linters configured.

## Architecture

The entire site lives in a single file: **`index.html`** (~1500 lines of HTML, CSS, and JavaScript). There is no build system, no package manager, and no external CSS or JS files. All styles use CSS custom properties defined at the top of the `<style>` block.

**Color tokens:**
- `--gold: #c9a84c` — primary accent
- `--black: #0a0a0a` — background
- `--beige: #e8e0d0` — body text contrast

**JavaScript (~80 lines, inline):** handles mobile drawer toggle, footer accordion, back-to-top scroll, scroll-progress bar, Intersection Observer for `.reveal` animations, and localStorage-based cookie consent.

**External service integrations:**
- **Kit.com** — email form submissions (form action URLs embedded in HTML)
- **Google AdSense** — `pub-6244083942838780` (configured in `ads.txt`)
- **Subdomain blogs** — energy.metricbase.org, chain.metricbase.org, saham.metricbase.org

## Key Conventions

- CSS class prefix `mb-` is used for component namespacing.
- Mobile-first responsive design; breakpoints at 640px and 900px.
- Scroll-triggered animations are applied by adding class `reveal` to elements — the Intersection Observer adds `visible` on entry.
- The site must include a financial disclaimer (non-financial advice) and cookie consent — do not remove these.
