// Build /feed.json (JSON Feed 1.1) from the journal article pages.
// Reads each journal/*.html, pulls canonical URL, og:title, meta description,
// article:published_time, and category (from filename), and emits a
// newest-first feed. Re-run after publishing a new journal piece:
//   node scripts/build-feed.mjs
// The MetricBase platform (apps.metricbase.org) fetches this feed to email
// opted-in users about new content (see platform lib/content.ts).

import { readdir, readFile, writeFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..')
const JOURNAL_DIR = join(ROOT, 'journal')
const SITE = 'https://metricbase.org'

function pick(html, re) {
  const m = html.match(re)
  return m ? m[1].trim() : ''
}

function categoryFor(file) {
  if (file.startsWith('research-')) return 'Research Report'
  if (file.startsWith('editorial-')) return 'Editorial'
  if (file.startsWith('weekly-brief-')) return 'Weekly Brief'
  return 'Journal'
}

function cleanTitle(ogTitle, fallback) {
  const t = (ogTitle || fallback || '').split(' · MetricBase')[0].trim()
  return t || fallback
}

const files = (await readdir(JOURNAL_DIR)).filter((f) => f.endsWith('.html'))
const items = []

for (const file of files) {
  const html = await readFile(join(JOURNAL_DIR, file), 'utf8')
  const url =
    pick(html, /<link rel="canonical" href="([^"]+)"/) ||
    `${SITE}/journal/${file.replace(/\.html$/, '')}`
  const title = cleanTitle(
    pick(html, /<meta property="og:title" content="([^"]+)"/),
    pick(html, /<title>([^<]+)<\/title>/),
  )
  const summary =
    pick(html, /<meta property="og:description" content="([^"]+)"/) ||
    pick(html, /<meta name="description" content="([^"]+)"/)
  const published = pick(html, /<meta property="article:published_time" content="([^"]+)"/)
  const image = pick(html, /<meta property="og:image" content="([^"]+)"/) || `${SITE}/assets/og-image.webp`
  if (!title || !published) continue

  items.push({
    id: url,
    url,
    title,
    summary,
    image,
    // Publish morning, WIB (UTC+7) — valid RFC3339 for JSON Feed.
    date_published: `${published}T08:00:00+07:00`,
    tags: [categoryFor(file)],
    authors: [{ name: 'Bun' }],
  })
}

items.sort((a, b) => new Date(b.date_published) - new Date(a.date_published))

const feed = {
  version: 'https://jsonfeed.org/version/1.1',
  title: 'MetricBase Journal',
  home_page_url: `${SITE}/journal`,
  feed_url: `${SITE}/feed.json`,
  description:
    'Cross-vertical research, editorials, and weekly market briefs across energy, crypto, and Indonesian equities.',
  icon: `${SITE}/assets/MetricBase.webp`,
  language: 'en',
  authors: [{ name: 'Bun', url: `${SITE}/about` }],
  items,
}

await writeFile(join(ROOT, 'feed.json'), JSON.stringify(feed, null, 2) + '\n')
console.log(`feed.json written — ${items.length} items (newest: ${items[0]?.title ?? 'none'})`)
