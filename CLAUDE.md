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

## Style Guidelines

- Dark, modern, minimal brand — following `assets/branding-style.md`
- No emojis. No corporate tone. No long paragraphs (max 2–3 lines).
- Strict color palette: `#0a0a0a` background, `#c9a84c` gold accents, white for contrast
- CSS class prefix `mb-` for component namespacing
- Write like a sharp operator talking to another operator. 100% Google AdSense Policy compliant.

## Deployment

Pushing to `main` automatically triggers GitHub Actions (`.github/workflows/jekyll-gh-pages.yml`), which builds with Jekyll and deploys to GitHub Pages (metricbase.org).

There are no tests and no linters configured.

## Architecture

### `index.html` — Content Portal (~1200 lines)

Single-file HTML/CSS/JS content portal. No build system, no package manager, no external CSS or JS files. All styles use CSS custom properties defined at the top of the `<style>` block.

**Page sections (in order):**
1. `#portal-hero` — MetricBase brand mark, tagline, sub-copy, pill links to verticals
2. `#strip` — Credibility strip with four positioning statements
3. `#verticals` — Three content vertical cards (Energy, Crypto, Stocks)
4. `#social` — Four social platform cards (X, Instagram, TikTok, Email)
5. `#subscribe` — Email capture form via Kit.com

**JavaScript (~80 lines, inline):** handles mobile drawer toggle, footer accordion, back-to-top scroll, scroll-progress bar, Intersection Observer for `.reveal` animations, and localStorage-based cookie consent.

### Blog Templates — Blogger XML

`blogs/energy.html`, `blogs/chain.html`, `blogs/saham.html` are Blogger XML templates using Blogger's template syntax (`<b:if>`, `<b:loop>`, `data:blog.*` variables, `<b:skin><![CDATA[...]]></b:skin>`).

Each blog template includes:
- OG + Twitter Card meta tags
- TradingView ticker widget
- Navigation drawer linking to all three verticals
- Footer with social links and copyright

## External Service Integrations

- **Kit.com** — email form submissions (`https://app.kit.com/forms/9390641/subscriptions`)
- **Google AdSense** — `pub-6244083942838780` (configured in `ads.txt`)
- **TradingView** — ticker widget embedded in all three blog templates

## Key Conventions

- Mobile-first responsive design; breakpoints at 640px and 900px.
- Scroll-triggered animations: add class `reveal` (and optionally `reveal-delay-1` through `reveal-delay-4`) to elements — the Intersection Observer adds `visible` on entry.
- The site must include a financial disclaimer (non-financial advice) and cookie consent — do not remove these.
- Use `mb-container` for section-level containers in `index.html`.
