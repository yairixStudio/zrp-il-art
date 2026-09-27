#!/usr/bin/env node
/**
 * Compare two regression snapshots produced by snapshot.mjs
 * (read from $REGRESS_OUT, default <os tmpdir>/zrp-regress).
 *
 *   node tools/regress/diff.mjs before after            # summary + first diffs per page
 *   node tools/regress/diff.mjs before after --dom      # also print a DOM line-diff excerpt
 *   node tools/regress/diff.mjs before after --json out.json
 *
 * Exit code 0 = identical (DOM, computed styles, boxes, scroll size, errors,
 * failed requests) for every page present in both; 1 = something differs.
 * A page present in only one snapshot also counts as a difference.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import os from 'node:os';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const [A, B] = process.argv.slice(2).filter(a => !a.startsWith('--'));
const SHOW_DOM = process.argv.includes('--dom');
const jsonIdx = process.argv.indexOf('--json');
const JSON_OUT = jsonIdx > 0 ? process.argv[jsonIdx + 1] : null;
if (!A || !B) { console.error('usage: diff.mjs <labelA> <labelB> [--dom] [--json out.json]'); process.exit(2); }
const OUT_BASE = process.env.REGRESS_OUT || path.join(os.tmpdir(), 'zrp-regress');
const dirA = path.join(OUT_BASE, A), dirB = path.join(OUT_BASE, B);
const meta = d => { try { return JSON.parse(fs.readFileSync(path.join(d, '_meta.json'))); } catch { return {}; } };
const metaA = meta(dirA), metaB = meta(dirB);
// strip the checkout root from the DOM so two checkouts compare equal (older snapshots stored it raw)
function norm(dom, m, group) {
  if (!dom || !m.root) return dom || '';
  const roots = group.startsWith('file')
    ? [pathToFileURL(m.root).href + '/', 'file://' + m.root + '/', 'file://' + encodeURI(m.root) + '/', m.root + '/']
    : [`http://127.0.0.1:${m.port || 8791}/`];
  // also the percent-encoded forms (e.g. location.href inside a mailto: body)
  for (const r of [...roots.map(encodeURIComponent), ...roots]) dom = dom.split(r).join('ROOT/');
  return dom;
}

// ignore iCloud conflict copies ("name 2.json") if a snapshot ever lands in a synced folder
const list = d => fs.existsSync(d) ? fs.readdirSync(d).filter(x => !x.startsWith('_') && !/ \d+(\.json)?$/.test(x)) : [];
const groups = [...new Set([...list(dirA), ...list(dirB)])].sort();
const report = [];
let pagesCompared = 0;

function domLineDiff(a, b) {
  const la = a.replace(/></g, '>\n<').split('\n'), lb = b.replace(/></g, '>\n<').split('\n');
  let i = 0; while (i < la.length && i < lb.length && la[i] === lb[i]) i++;
  let ja = la.length - 1, jb = lb.length - 1;
  while (ja > i && jb > i && la[ja] === lb[jb]) { ja--; jb--; }
  const cut = s => s.length > 220 ? s.slice(0, 220) + '…' : s;
  return { at: i, removed: la.slice(i, Math.min(ja + 1, i + 6)).map(cut), added: lb.slice(i, Math.min(jb + 1, i + 6)).map(cut) };
}

for (const g of groups) {
  const fa = new Set(list(path.join(dirA, g)).filter(f => f.endsWith('.json')));
  const fb = new Set(list(path.join(dirB, g)).filter(f => f.endsWith('.json')));
  for (const f of [...new Set([...fa, ...fb])].sort()) {
    const id = `${g}/${f.replace(/\.json$/, '')}`;
    if (!fa.has(f) || !fb.has(f)) { report.push({ id, issues: [`only in ${fa.has(f) ? A : B}`] }); continue; }
    const a = JSON.parse(fs.readFileSync(path.join(dirA, g, f)));
    const b = JSON.parse(fs.readFileSync(path.join(dirB, g, f)));
    pagesCompared++;
    const issues = [];
    if (a.captureError || b.captureError) issues.push(`capture error: ${a.captureError || ''} | ${b.captureError || ''}`);
    if (a.navErr !== b.navErr) issues.push(`navigation: ${a.navErr} → ${b.navErr}`);
    if (norm(a.title, metaA, g) !== norm(b.title, metaB, g)) issues.push(`title: "${a.title}" → "${b.title}"`);
    if (JSON.stringify(a.scroll) !== JSON.stringify(b.scroll)) issues.push(`scroll size ${a.scroll} → ${b.scroll}`);
    const setDiff = (x, y) => ({ gone: (x || []).filter(v => !(y || []).includes(v)), new: (y || []).filter(v => !(x || []).includes(v)) });
    const ed = setDiff(a.errors, b.errors);
    if (ed.gone.length || ed.new.length) issues.push(`errors: -${JSON.stringify(ed.gone)} +${JSON.stringify(ed.new)}`);
    const fd = setDiff(a.failed, b.failed);
    if (fd.gone.length || fd.new.length) issues.push(`failed requests: -${JSON.stringify(fd.gone)} +${JSON.stringify(fd.new)}`);
    let domd = null;
    if (a.domHash !== b.domHash) {
      const da = norm(a.dom, metaA, g), db = norm(b.dom, metaB, g);
      if (da !== db) { issues.push('DOM differs'); domd = domLineDiff(da, db); }
    }
    const ea = a.els || [], eb = b.els || [];
    if (ea.length !== eb.length) issues.push(`element count ${ea.length} → ${eb.length}`);
    const n = Math.min(ea.length, eb.length);
    let styleDiffs = 0, boxDiffs = 0; const firsts = [];
    for (let i = 0; i < n; i++) {
      const sd = ea[i][1] !== eb[i][1], bd = JSON.stringify(ea[i][2]) !== JSON.stringify(eb[i][2]);
      if (ea[i][0] !== eb[i][0] && firsts.length < 5) firsts.push(`#${i} element ${ea[i][0]} → ${eb[i][0]}`);
      if (sd) styleDiffs++;
      if (bd) boxDiffs++;
      if ((sd || bd) && firsts.length < 5) firsts.push(`#${i} ${ea[i][0]}${sd ? ' style' : ''}${bd ? ` box ${JSON.stringify(ea[i][2])}→${JSON.stringify(eb[i][2])}` : ''}`);
    }
    if (styleDiffs) issues.push(`${styleDiffs} elements with different computed style`);
    if (boxDiffs) issues.push(`${boxDiffs} elements with different box`);
    if (issues.length) report.push({ id, issues, firsts, dom: domd });
  }
}

for (const r of report) {
  console.log(`✗ ${r.id}`);
  for (const i of r.issues) console.log(`    ${i}`);
  for (const f of r.firsts || []) console.log(`      ${f}`);
  if (SHOW_DOM && r.dom) {
    console.log(`      DOM @line ${r.dom.at}:`);
    for (const l of r.dom.removed) console.log(`        - ${l}`);
    for (const l of r.dom.added) console.log(`        + ${l}`);
  }
}
if (JSON_OUT) fs.writeFileSync(JSON_OUT, JSON.stringify(report, null, 1));
console.log(`\n${pagesCompared} page-renders compared, ${report.length} differ.`);
process.exit(report.length ? 1 : 0);
