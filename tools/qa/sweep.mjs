#!/usr/bin/env node
/**
 * Width sweep — renders pages in headless Chrome at many viewport widths (300 → 1600)
 * and reports the layout bugs that keep coming back at "in-between" widths:
 *
 *   overflow   the page scrolls sideways (document wider than the viewport) — names the
 *              elements that stick out past the right/left edge
 *   clipped    text cut off by its own box (overflow hidden/clip, incl. Copperplate caps
 *              cut at the top by a tight line-height)
 *   overlap    a wrapped line drawn on top of the line above it (line-height too small
 *              once a heading breaks into two lines)
 *
 * Usage (from repo root):
 *   node tools/qa/sweep.mjs                          # pages changed in the working tree (+ new pages)
 *   node tools/qa/sweep.mjs index.html events/ktuba/ # given pages / directories
 *   node tools/qa/sweep.mjs --only sponsors/,artists/
 *   node tools/qa/sweep.mjs --all                    # every published page (slow: ~250 pages)
 *
 * Options:
 *   --widths 300,390,...   override the width list
 *   --shots                save a screenshot of every failing page × width to $SWEEP_OUT
 *   --concurrency N        parallel tabs (default 6)
 *
 * Exit code: 0 = clean, 1 = issues found, 2 = usage error.
 * Same deterministic setup as tools/regress/snapshot.mjs: own static server,
 * external requests blocked, lazy images forced eager, fonts awaited.
 */
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import os from 'node:os';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer-core';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const CHROME = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = Number(process.env.SWEEP_PORT || 8792);
const OUT = process.env.SWEEP_OUT || path.join(os.tmpdir(), 'zrp-sweep');
// Breakpoint edges of the site (768/769, 1100, 1320/1440) plus common phones.
const DEFAULT_WIDTHS = [300, 320, 360, 375, 390, 414, 480, 600, 768, 769, 834, 900, 1024, 1100, 1180, 1280, 1320, 1366, 1400, 1439, 1440, 1600];

// ---------- args ----------
const argv = process.argv.slice(2);
const flag = n => argv.includes('--' + n);
const opt = (n, d) => { const i = argv.indexOf('--' + n); return i < 0 || argv[i + 1] === undefined || argv[i + 1].startsWith('--') ? d : argv[i + 1]; };
const WIDTHS = opt('widths') ? String(opt('widths')).split(',').map(Number) : DEFAULT_WIDTHS;
const CONC = Number(opt('concurrency', 6));
const SHOTS = flag('shots');
const ONLY = opt('only') ? String(opt('only')).split(',') : null;
const valued = new Set(['--widths', '--concurrency', '--only']);
const positional = argv.filter((a, i) => !a.startsWith('--') && !valued.has(argv[i - 1]));

// ---------- page list ----------
const EXCLUDE = /^(trash|scratchpad|_staging|_originals|node_modules|newsletter-backend|lighthouse-reports|\.regress)\//;
const git = (...a) => execFileSync('git', ['-C', ROOT, ...a], { encoding: 'utf8' }).split('\n').filter(Boolean);
const published = [...new Set([...git('ls-files', '*.html'), ...git('ls-files', '--others', '--exclude-standard', '*.html')])]
  .filter(p => !EXCLUDE.test(p) && fs.existsSync(path.join(ROOT, p)));
let pages;
if (positional.length) {
  pages = positional.flatMap(a => {
    const rel = path.relative(ROOT, path.resolve(a)).replace(/\\/g, '/');
    if (rel.endsWith('.html')) return [rel];
    return published.filter(p => p === `${rel}/index.html` || p.startsWith(rel ? rel.replace(/\/?$/, '/') : ''));
  });
} else if (flag('all')) {
  pages = published;
} else if (ONLY) {
  pages = published.filter(p => ONLY.some(pre => p.startsWith(pre)));
} else {
  // default: pages touched in the working tree (vs HEAD) and new pages
  const changed = new Set([...git('diff', '--name-only', 'HEAD'), ...git('ls-files', '--others', '--exclude-standard')]);
  pages = published.filter(p => changed.has(p));
  if (!pages.length) { console.log('sweep: no changed pages — pass pages, --only or --all'); process.exit(0); }
}
pages = [...new Set(pages)].filter(p => fs.existsSync(path.join(ROOT, p))).sort();
if (!pages.length) { console.error('sweep: no matching pages'); process.exit(2); }

// ---------- in-page checks ----------
function check(WIDTH) {
  const vw = document.documentElement.clientWidth;
  const out = { overflow: [], clipped: [], overlap: [] };
  const name = el => {
    const id = el.id ? '#' + el.id : '';
    const cls = (el.getAttribute('class') || '').trim().split(/\s+/).filter(Boolean).slice(0, 2).map(c => '.' + c).join('');
    return el.tagName.toLowerCase() + id + cls;
  };
  const visible = (el, cs) => cs.display !== 'none' && cs.visibility !== 'hidden' && +cs.opacity !== 0 && el.getClientRects().length;
  const text = el => (el.innerText || el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 40);
  // is el horizontally clipped by an ancestor (overflow hidden/auto/clip) — then sticking out is fine
  const clippedByAncestor = el => {
    for (let a = el.parentElement; a && a !== document.documentElement && a !== document.body; a = a.parentElement) {
      const ox = getComputedStyle(a).overflowX;
      if (ox !== 'visible') return true;
    }
    return false;
  };
  const all = [...document.body.querySelectorAll('*')];

  // 1. content wider than the screen. Two flavours:
  //    scrolls  — the visitor can pan sideways (or a phone zooms the page out: the
  //               "white strip on the right" bug)
  //    edge     — html{overflow-x:hidden} stops the scroll, but the content is cut at the screen edge
  const sw = Math.max(document.documentElement.scrollWidth, document.body.scrollWidth);
  if (sw > vw + 1 || innerWidth > WIDTH + 1) {
    window.scrollTo(100000, window.scrollY);
    const scrolls = window.scrollX > 0 || innerWidth > WIDTH + 1;
    window.scrollTo(0, window.scrollY);
    const culprits = [];
    for (const el of all) {
      const cs = getComputedStyle(el);
      if (!visible(el, cs) || cs.position === 'fixed') continue;
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) continue;
      if (r.right <= 0 || r.left >= vw) continue; // fully off-canvas on purpose (skip links, closed drawers)
      if ((r.right > vw + 1 || r.left < -1) && !clippedByAncestor(el)) {
        // keep only the outermost culprit of each subtree
        if (culprits.some(c => c.el.contains(el))) continue;
        culprits.push({ el, r });
      }
    }
    if (scrolls || culprits.length)
      out.overflow.push({ scrolls, els: culprits.slice(0, 5).map(c => `${name(c.el)} "${text(c.el)}"`) });
  }

  // 2 + 3. text boxes: clipped by own overflow, or wrapped lines drawn over each other
  for (const el of all) {
    const own = [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim());
    if (!own.length) continue;
    const cs = getComputedStyle(el);
    if (!visible(el, cs)) continue;
    if (el.closest('[aria-hidden="true"],.sr-only,.visually-hidden')) continue;
    const r = el.getBoundingClientRect();
    if (r.right < 0 || r.left > vw) continue; // off-canvas slides/drawers
    const clipX = cs.overflowX !== 'visible', clipY = cs.overflowY !== 'visible';
    if (clipX && cs.textOverflow !== 'ellipsis' && el.scrollWidth > el.clientWidth + 2)
      out.clipped.push(`${name(el)} "${text(el)}" — width ${el.clientWidth} < ${el.scrollWidth}`);
    else if (clipY && el.scrollHeight > el.clientHeight + 2 && !(+cs.webkitLineClamp > 0))
      out.clipped.push(`${name(el)} "${text(el)}" — height ${el.clientHeight} < ${el.scrollHeight}`);
    // line overlap: glyph boxes of consecutive lines intersect by more than 40% of a line
    const range = document.createRange();
    const rects = [];
    for (const n of own) { range.selectNodeContents(n); rects.push(...[...range.getClientRects()].filter(q => q.width > 1)); }
    const lines = [];
    for (const q of rects.sort((a, b) => a.top - b.top)) {
      const last = lines[lines.length - 1];
      if (last && Math.abs(q.top - last.top) < 2) { last.bottom = Math.max(last.bottom, q.bottom); continue; }
      lines.push({ top: q.top, bottom: q.bottom });
    }
    for (let i = 1; i < lines.length; i++) {
      const h = lines[i].bottom - lines[i].top, ov = lines[i - 1].bottom - lines[i].top;
      if (h > 0 && ov / h > 0.4) { out.overlap.push(`${name(el)} "${text(el)}" — line ${i + 1} overlaps line ${i} by ${Math.round(ov / h * 100)}%`); break; }
    }
  }
  return out;
}

// ---------- runner ----------
async function sweepOne(browser, p, width) {
  const ctx = await browser.createBrowserContext();
  const page = await ctx.newPage();
  const local = `http://127.0.0.1:${PORT}/`;
  await page.setRequestInterception(true);
  page.on('request', r => (r.url().startsWith(local) || /^(data|blob|about):/.test(r.url())) ? r.continue() : r.abort('blockedbyclient'));
  await page.evaluateOnNewDocument(() => {
    new MutationObserver(ms => { for (const m of ms) for (const n of m.addedNodes) {
      if (n.nodeType !== 1) continue;
      for (const el of (n.matches('img,iframe') ? [n] : n.querySelectorAll('img,iframe'))) if (el.loading === 'lazy') el.loading = 'eager';
    } }).observe(document, { childList: true, subtree: true });
  });
  await page.setViewport(width < 768 ? { width, height: 844, isMobile: true, hasTouch: true } : { width, height: 900 });
  try {
    await page.goto(local + p.replace(/(^|\/)index\.html$/, '$1'), { waitUntil: 'load', timeout: 45000 });
    await page.evaluate(async () => {
      await document.fonts.ready;
      await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 4000); })));
      document.getAnimations().forEach(a => { try { a.finish(); } catch {} });
      await new Promise(r => setTimeout(r, 150));
    });
    const res = await page.evaluate(check, width);
    const n = res.overflow.length + res.clipped.length + res.overlap.length;
    if (n && SHOTS) {
      fs.mkdirSync(OUT, { recursive: true });
      await page.screenshot({ path: path.join(OUT, `${p.replace(/\/?index\.html$/, '').replace(/\//g, '__') || 'home'}-${width}.jpg`), type: 'jpeg', quality: 70, fullPage: true }).catch(() => {});
    }
    return res;
  } catch (e) {
    return { error: String(e.message || e).split('\n')[0] };
  } finally { await ctx.close(); }
}

async function main() {
  const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
    '.svg': 'image/svg+xml', '.webp': 'image/webp', '.avif': 'image/avif', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif',
    '.mp4': 'video/mp4', '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.otf': 'font/otf', '.ico': 'image/x-icon' };
  const server = http.createServer((req, res) => {
    let f = path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname));
    if (!f.startsWith(ROOT)) { res.writeHead(403); return res.end(); }
    fs.stat(f, (err, st) => {
      if (!err && st.isDirectory()) f = path.join(f, 'index.html');
      fs.readFile(f, (e2, buf) => {
        if (e2) { res.writeHead(404); return res.end(); }
        res.writeHead(200, { 'content-type': TYPES[path.extname(f).toLowerCase()] || 'application/octet-stream' });
        res.end(buf);
      });
    });
  });
  await new Promise(r => server.listen(PORT, '127.0.0.1', r));
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ['--hide-scrollbars', '--font-render-hinting=none', '--disable-renderer-backgrounding'] });
  console.log(`sweep: ${pages.length} page(s) × ${WIDTHS.length} widths (${WIDTHS[0]}–${WIDTHS[WIDTHS.length - 1]})`);
  const jobs = pages.flatMap(p => WIDTHS.map(w => ({ p, w })));
  const results = new Map();
  let next = 0;
  async function worker() { while (next < jobs.length) { const j = jobs[next++]; results.set(`${j.p}|${j.w}`, await sweepOne(browser, j.p, j.w)); } }
  try { await Promise.all(Array.from({ length: CONC }, worker)); }
  finally { await browser.close(); server.close(); }

  // group identical findings across widths: "same issue at 300–375" instead of 4 lines
  let issues = 0;
  for (const p of pages) {
    const found = new Map(); // message -> widths[]
    for (const w of WIDTHS) {
      const r = results.get(`${p}|${w}`);
      const add = m => { if (!found.has(m)) found.set(m, []); found.get(m).push(w); };
      if (r.error) { add(`error: ${r.error}`); continue; }
      for (const o of r.overflow) add(`${o.scrolls ? 'overflow: page scrolls sideways' : 'edge: cut at the screen edge'} — ${o.els.join(', ') || '(no single culprit)'}`);
      for (const c of r.clipped) add('clipped: ' + c.replace(/ — (width|height) \d+ < \d+/, ' — $1'));
      for (const o of r.overlap) add('overlap: ' + o.replace(/ by \d+%/, ''));
    }
    if (!found.size) { console.log(`  ✓ ${p}`); continue; }
    console.log(`  ✗ ${p}`);
    for (const [m, ws] of found) { issues++; console.log(`      @ ${ws.join(',')}  ${m}`); }
  }
  console.log(issues ? `sweep: ${issues} issue(s)${SHOTS ? ` — screenshots in ${OUT}` : ''}` : 'sweep: clean');
  process.exit(issues ? 1 : 0);
}
main().catch(e => { console.error(e); process.exit(2); });
