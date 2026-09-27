#!/usr/bin/env node
/**
 * Regression snapshot — renders every page of the site in headless Chrome and
 * records what a visitor would actually get, so a before/after pair can prove
 * that a cross-page change (refactor, shared CSS, data plumbing) broke nothing.
 *
 * Per page × width × mode it records:
 *   - the post-JS DOM (scripts/styles/links/comments stripped — i.e. the RESULT)
 *   - a hash of the FULL computed style of every element (+ ::before/::after)
 *   - every element's bounding box, and the document scroll size
 *   - console errors, page errors, failed local requests, HTTP >= 400
 *
 * Deterministic by construction: Date/Math.random are frozen, every non-local
 * request is aborted (Instagram, analytics, zrp.co.il), lazy images are forced
 * eager and awaited, fonts are awaited, running animations are finished.
 *
 * Usage (from repo root):
 *   node tools/regress/snapshot.mjs --label before
 *   node tools/regress/snapshot.mjs --label after --only artists/,events/
 *   node tools/regress/diff.mjs before after
 *
 * Options:
 *   --label NAME         output dir .regress/NAME (required)
 *   --modes http,file    http = served by a local http.server (production-like),
 *                        file = file:// (how the site is browsed locally)
 *   --widths 390,1440
 *   --only a/,b/         only pages whose path starts with one of these prefixes
 *   --concurrency N      parallel tabs (default 6)
 *   --shots              also save a first-screen JPEG per page
 *   --full               store the full computed-style map per element (debug;
 *                        use with --only — output is large)
 *   --root DIR           snapshot another checkout (default: this repo)
 *
 * Output: $REGRESS_OUT/<label> (default: <os tmpdir>/zrp-regress/<label>).
 */
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import http from 'node:http';
import os from 'node:os';
import crypto from 'node:crypto';
import { pathToFileURL, fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer-core';

const HARNESS_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const CHROME = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const FIXED_NOW = Date.parse('2026-09-27T12:00:00'); // any constant works; before/after just must match
const PORT = Number(process.env.REGRESS_PORT || 8791);

// ---------- args ----------
const argv = process.argv.slice(2);
const opt = (name, dflt) => {
  const i = argv.indexOf('--' + name);
  if (i < 0) return dflt;
  const v = argv[i + 1];
  return v === undefined || v.startsWith('--') ? true : v;
};
const label = opt('label');
if (!label || label === true) { console.error('--label NAME is required'); process.exit(2); }
const MODES = String(opt('modes', 'http,file')).split(',');
const WIDTHS = String(opt('widths', '390,1440')).split(',').map(Number);
const ONLY = opt('only') ? String(opt('only')).split(',') : null;
const CONC = Number(opt('concurrency', 6));
const SHOTS = !!opt('shots', false);
const FULL = !!opt('full', false);
// --root DIR: snapshot another checkout of the site (e.g. a pristine clone of HEAD)
// while keeping the harness, node_modules and the .regress/ output here.
const ROOT = path.resolve(opt('root', HARNESS_ROOT) === true ? HARNESS_ROOT : opt('root', HARNESS_ROOT));
// Output lives OUTSIDE the repo by default (the repo sits in iCloud, which spawns "name 2.json"
// conflict copies inside rapidly rewritten folders). Override with REGRESS_OUT.
const OUT_BASE = process.env.REGRESS_OUT || path.join(os.tmpdir(), 'zrp-regress');
const OUT = path.join(OUT_BASE, label);

// ---------- page list: every tracked, published .html ----------
const EXCLUDE = /^(trash|scratchpad|_staging|_originals|node_modules|newsletter-backend|lighthouse-reports|\.regress)\//;
const pages = execFileSync('git', ['-C', ROOT, 'ls-files', '*.html'], { encoding: 'utf8' })
  .split('\n').filter(Boolean)
  .filter(p => !EXCLUDE.test(p))
  .filter(p => !ONLY || ONLY.some(pre => p.startsWith(pre)))
  .sort();

const key = p => p.replace(/\/index\.html$/, '').replace(/\.html$/, '').replace(/\//g, '__') || 'home';
const urlFor = (mode, p) => mode === 'file'
  ? pathToFileURL(path.join(ROOT, p)).href
  : `http://127.0.0.1:${PORT}/${p.replace(/(^|\/)index\.html$/, '$1')}`;

// ---------- in-page code ----------
function preload(FIXED) {
  // freeze time (keeps new Date(...args) working; bare Date() / new Date() / Date.now() are fixed)
  const _Date = Date;
  function FDate(...a) {
    if (!(this instanceof FDate)) return new _Date(FIXED).toString();
    return a.length ? new _Date(...a) : new _Date(FIXED);
  }
  FDate.prototype = _Date.prototype;
  FDate.now = () => FIXED; FDate.parse = _Date.parse; FDate.UTC = _Date.UTC;
  window.Date = FDate;
  let seed = 42;
  Math.random = () => ((seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296);
  // force lazy media eager so "which images happened to load" is not a variable
  new MutationObserver(ms => {
    for (const m of ms) for (const n of m.addedNodes) {
      if (n.nodeType !== 1) continue;
      const list = n.matches && n.matches('img,iframe') ? [n] : (n.querySelectorAll ? n.querySelectorAll('img,iframe') : []);
      for (const el of list) if (el.getAttribute('loading') === 'lazy') el.setAttribute('loading', 'eager');
    }
  }).observe(document, { childList: true, subtree: true });
}

function capture(FULL) {
  function hash(str) { // cyrb53
    let h1 = 0xdeadbeef, h2 = 0x41c6ce57;
    for (let i = 0; i < str.length; i++) {
      const ch = str.charCodeAt(i);
      h1 = Math.imul(h1 ^ ch, 2654435761); h2 = Math.imul(h2 ^ ch, 1597334677);
    }
    h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
    h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
    return (4294967296 * (2097151 & h2) + (h1 >>> 0)).toString(36);
  }
  function styleStr(cs) {
    // Chrome enumerates custom properties (--vars) in a run-dependent order → sort names.
    const names = []; for (let i = 0; i < cs.length; i++) names.push(cs[i]);
    names.sort();
    let s = '';
    for (const n of names) s += n + ':' + cs.getPropertyValue(n) + ';';
    return s;
  }
  const SKIP = new Set(['SCRIPT', 'STYLE', 'LINK', 'NOSCRIPT', 'TEMPLATE', 'META', 'TITLE', 'BASE', 'HEAD']);
  const r1 = v => Math.round(v * 10) / 10;
  const els = [], full = [];
  const all = [document.documentElement, ...document.documentElement.querySelectorAll('*')];
  for (const el of all) {
    if (SKIP.has(el.tagName) || el.closest('head')) continue;
    const id = el.id ? '#' + el.id : '';
    const cls = (el.getAttribute('class') || '').trim().split(/\s+/).filter(Boolean).slice(0, 3).map(c => '.' + c).join('');
    const name = el.tagName.toLowerCase() + id + cls;
    const s = styleStr(getComputedStyle(el));
    let pseudo = '';
    for (const p of ['::before', '::after']) {
      const pc = getComputedStyle(el, p);
      const c = pc.getPropertyValue('content');
      if (c && c !== 'none' && c !== 'normal') pseudo += p + '{' + styleStr(pc) + '}';
    }
    const b = el.getBoundingClientRect();
    els.push([name, hash(s + pseudo), [r1(b.x), r1(b.y + scrollY), r1(b.width), r1(b.height)]]);
    if (FULL) full.push(s + pseudo);
  }
  // result DOM: strip executable/styling plumbing + comments, keep everything rendered
  const clone = document.documentElement.cloneNode(true);
  clone.querySelectorAll('script,style,link,noscript,template').forEach(n => n.remove());
  const walker = document.createTreeWalker(clone, NodeFilter.SHOW_COMMENT);
  const comments = []; while (walker.nextNode()) comments.push(walker.currentNode);
  comments.forEach(c => c.remove());
  const dom = clone.outerHTML;
  return {
    title: document.title,
    scroll: [document.documentElement.scrollWidth, document.documentElement.scrollHeight],
    domHash: hash(dom), dom, els, full: FULL ? full : undefined,
  };
}

function normalizeRoot(str, mode) {
  const roots = mode === 'file'
    ? [pathToFileURL(ROOT).href + '/', 'file://' + ROOT + '/', 'file://' + encodeURI(ROOT) + '/', ROOT + '/']
    : [`http://127.0.0.1:${PORT}/`];
  // also the percent-encoded forms (e.g. location.href inside a mailto: body)
  for (const r of [...roots.map(encodeURIComponent), ...roots]) str = str.split(r).join('ROOT/');
  return str;
}

// ---------- run ----------
async function snapOne(browser, mode, width, p) {
  // own context = own window: a background tab gets its timers throttled, which made
  // page boot code (setTimeout-based) finish at random times across runs.
  const ctx = await browser.createBrowserContext();
  const page = await ctx.newPage();
  const errors = [], failed = [];
  let blocked = 0;
  const local = mode === 'file' ? 'file://' : `http://127.0.0.1:${PORT}/`;
  await page.setRequestInterception(true);
  page.on('request', r => {
    const u = r.url();
    if (u.startsWith(local) || u.startsWith('data:') || u.startsWith('blob:') || u.startsWith('about:')) r.continue();
    else { blocked++; r.abort('blockedbyclient'); }
  });
  // strip the machine-specific root so messages read as repo paths
  const ROOT_URL = mode === 'file' ? pathToFileURL(ROOT).href + '/' : local;
  const rel = s => String(s).split(ROOT_URL).join('');
  page.on('pageerror', e => errors.push('pageerror: ' + rel(String(e.message || e).split('\n')[0])));
  page.on('console', m => {
    if (m.type() !== 'error') return;
    const t = m.text().split('\n')[0];
    if (/ERR_BLOCKED_BY_CLIENT/.test(t)) return; // our own abort of external requests
    errors.push('console: ' + rel(t));
  });
  page.on('requestfailed', r => {
    const f = (r.failure() && r.failure().errorText) || '';
    // BLOCKED_BY_CLIENT = our abort of external URLs; ERR_ABORTED = the page itself cancelled
    // the request (e.g. picture-upgrade swapping <img> for <picture>) — timing noise, not a bug.
    if (f.startsWith('net::ERR_BLOCKED_BY_CLIENT') || f === 'net::ERR_ABORTED') return;
    failed.push(rel(r.url()) + ' ' + f);
  });
  page.on('response', r => { if (r.status() >= 400 && r.url().startsWith(local)) failed.push(rel(r.url()) + ' HTTP ' + r.status()); });
  await page.evaluateOnNewDocument(preload, FIXED_NOW);
  await page.setViewport(width < 768
    ? { width, height: 844, deviceScaleFactor: 1, isMobile: true, hasTouch: true }
    : { width, height: 900, deviceScaleFactor: 1 });
  let navErr = null;
  try { await page.goto(urlFor(mode, p), { waitUntil: 'load', timeout: 45000 }); }
  catch (e) { navErr = String(e.message || e); }
  await page.evaluate(async () => {
    const until = (ms) => new Promise(r => setTimeout(r, ms));
    await Promise.race([document.fonts.ready, until(5000)]);
    const imgs = [...document.images].filter(i => !i.complete);
    await Promise.race([Promise.all(imgs.map(i => new Promise(r => { i.onload = i.onerror = r; }))), until(8000)]);
    await until(1800); // > site-chrome's 1500ms boot ceiling
    // site-chrome marks <body class="is-ready"> when the shell has booted — wait for it (bounded)
    for (let i = 0; i < 30 && document.querySelector('site-header,site-footer') && !document.body.classList.contains('is-ready'); i++) await until(100);
    for (const a of document.getAnimations()) { try { a.finish(); } catch { a.pause(); a.currentTime = 0; } }
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  }).catch(e => errors.push('settle: ' + e.message));
  let snap;
  try { snap = await page.evaluate(capture, FULL); }
  catch (e) { snap = { captureError: String(e.message || e) }; }
  if (snap.dom) {
    // JS-built absolute URLs embed the checkout root — normalize so two checkouts compare equal
    snap.dom = normalizeRoot(snap.dom, mode);
    snap.domHash = crypto.createHash('md5').update(snap.dom).digest('hex');
  }
  if (SHOTS) {
    const dir = path.join(OUT, `${mode}-${width}`, '_shots');
    fs.mkdirSync(dir, { recursive: true });
    await page.screenshot({ path: path.join(dir, key(p) + '.jpg'), type: 'jpeg', quality: 70 }).catch(() => {});
  }
  await ctx.close();
  return { page: p, mode, width, navErr, errors: [...new Set(errors)].sort(), failed: [...new Set(failed)].sort(), blocked, ...snap };
}

async function main() {
  // Tiny static server (python's http.server has a 5-connection backlog and resets
  // connections under parallel load — that showed up as flaky failed requests).
  let server = null;
  if (MODES.includes('http')) {
    const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8',
      '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml', '.webp': 'image/webp',
      '.avif': 'image/avif', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.ico': 'image/x-icon',
      '.mp4': 'video/mp4', '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.otf': 'font/otf', '.xml': 'application/xml', '.txt': 'text/plain' };
    server = http.createServer((req, res) => {
      let u = decodeURIComponent(new URL(req.url, 'http://x').pathname);
      let f = path.join(ROOT, u);
      if (!f.startsWith(ROOT)) { res.writeHead(403); return res.end(); }
      fs.stat(f, (err, st) => {
        if (!err && st.isDirectory()) { f = path.join(f, 'index.html'); }
        fs.readFile(f, (e2, buf) => {
          if (e2) { res.writeHead(404); return res.end('not found'); }
          res.writeHead(200, { 'content-type': TYPES[path.extname(f).toLowerCase()] || 'application/octet-stream', 'cache-control': 'no-store' });
          res.end(buf);
        });
      });
    });
    await new Promise(r => server.listen(PORT, '127.0.0.1', r));
  }
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: true, protocolTimeout: 120000,
    args: ['--disable-background-timer-throttling', '--disable-backgrounding-occluded-windows',
      '--disable-features=IntensiveWakeUpThrottling,CalculateNativeWinOcclusion',
      '--disable-renderer-backgrounding', '--font-render-hinting=none', '--hide-scrollbars'],
  });
  const jobs = [];
  for (const mode of MODES) for (const width of WIDTHS) for (const p of pages) jobs.push({ mode, width, p });
  fs.rmSync(OUT, { recursive: true, force: true });
  let done = 0, next = 0;
  const t0 = Date.now();
  async function worker() {
    while (next < jobs.length) {
      const j = jobs[next++];
      let res;
      for (let attempt = 1; attempt <= 3; attempt++) {
        res = await snapOne(browser, j.mode, j.width, j.p).catch(e => ({ page: j.p, mode: j.mode, width: j.width, captureError: String(e.message || e), errors: [], failed: [] }));
        const flaky = res.captureError || res.navErr || (res.errors || []).some(x => x.startsWith('settle:')) ||
          [...(res.errors || []), ...(res.failed || [])].some(x => /ERR_CONNECTION_RESET|ERR_CONNECTION_REFUSED|ERR_EMPTY_RESPONSE/.test(x));
        if (!flaky) break;
        res.attempts = attempt;
      }
      const dir = path.join(OUT, `${j.mode}-${j.width}`);
      fs.mkdirSync(dir, { recursive: true });
      fs.writeFileSync(path.join(dir, key(j.p) + '.json'), JSON.stringify(res));
      done++;
      if (done % 50 === 0 || done === jobs.length)
        process.stdout.write(`  ${done}/${jobs.length}  (${Math.round((Date.now() - t0) / 1000)}s)\n`);
    }
  }
  try { await Promise.all(Array.from({ length: CONC }, worker)); }
  finally { await browser.close(); if (server) server.close(); }
  fs.writeFileSync(path.join(OUT, '_meta.json'), JSON.stringify({ label, root: ROOT, port: PORT, modes: MODES, widths: WIDTHS, pages: pages.length, fixedNow: FIXED_NOW }, null, 1));
  console.log(`snapshot "${label}": ${pages.length} pages × ${WIDTHS.length} widths × ${MODES.length} modes of ${ROOT} → ${OUT}`);
}
main().catch(e => { console.error(e); process.exit(1); });
