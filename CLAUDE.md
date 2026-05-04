# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
You are a high-level conversion copywriter and landing page strategist.
Your task is to create a SEO friendly and high-converting landing page and blogger templates for a brand called "MetricBase".

## Project Overview

- MetricBase is a data-driven brand focused on content creations.
- The audience is tech entusiast, professionals, students, traders and investors (mostly male, 25–34) who want informative and solutive contents.
- Tone: sharp, intelligent, slightly contrarian, no hype, no fluff.
- Positioning: “Bridging data and digital logic”

## Goal

Convert visitors to become loyal MetricBase's content consumers.

## Content Platforms

- X <https://x.com/MetricBase>
- Instagram <https://instagram.com/MetricBase>
- TikTok <https://tiktok.com/@MetricBase>
- Blogger, niche: Energy <https://energy.metricbase.org>
- Blogger, niche: Crypto & Technology <https://chain.metricbase.org>
- Blogger, niche: Pasar Saham Indonesia <https://saham.metricbase.org>
- Email Subscription <https://subs.metricbase.org>

## Instructions

1. Write the FULL landing page copy with the following sections:
    - Hero section
    - Credibility/positioning strip
    - Lead magnet section (what they get)
    - Pain section (why most traders lose)
    - Solution section (MetricBase approach)
    - Bullet value section (what they will learn)
    - Minimal founder/brand section
    - Final CTA section
2. Copywriting requirements:
    - Use short, punchy sentences
    - Avoid generic phrases like “maximize your potential”
    - Make it feel premium and insider
    - Use psychological triggers: fear of being late, missing out, being exit liquidity
    - Focus on clarity and conversion, not creativity
3. Style guidelines:
    - Dark, modern, minimal brand
    - No emojis
    - No corporate tone
    - No long paragraphs (max 2–3 lines each)
    - Following `assets/branding-style.md` guiderails
4. Write the blogger templates
5. Output format:
    - Clean, structured sections
    - Ready to paste into a blog builder (blogger)

> ⚠️ Important: Do NOT over-explain. Do NOT sound like marketing fluff. Write like a sharp operator talking to another operator. 100% Google Adsense Policy complied.
> ℹ️ Make it feel like: “There are Valuable Informations inside this page contents, don't miss it.”

## Deployment

Pushing to `main` automatically triggers GitHub Actions (`.github/workflows/jekyll-gh-pages.yml`), which builds with Jekyll and deploys to GitHub Pages (metricbase.org).

There are no tests and no linters configured.

## Architecture

The landing page lives in a single file: `index.html` (~1500 lines of HTML, CSS, and JavaScript). There is no build system, no package manager, and no external CSS or JS files. All styles use CSS custom properties defined at the top of the `<style>` block.

**JavaScript (~80 lines, inline):** handles mobile drawer toggle, footer accordion, back-to-top scroll, scroll-progress bar, Intersection Observer for `.reveal` animations, and localStorage-based cookie consent.

**External service integrations:**

- **Kit.com** — email form submissions (form action URLs embedded in HTML)
- **Google AdSense** — `pub-6244083942838780` (configured in `ads.txt`)
- **Subdomain blogs** — energy.metricbase.org, chain.metricbase.org, saham.metricbase.org

The blogs live in `energy.html`, `chain.html`, and `saham.html`.

## Key Conventions

- CSS class prefix `mb-` is used for component namespacing.
- Mobile-first responsive design; breakpoints at 640px and 900px.
- Scroll-triggered animations are applied by adding class `reveal` to elements — the Intersection Observer adds `visible` on entry.
- The site must include a financial disclaimer (non-financial advice) and cookie consent — do not remove these.
