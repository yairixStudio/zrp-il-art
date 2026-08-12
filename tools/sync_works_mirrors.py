#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync all inline mirrors from data/works.json (the single source of truth) AND
upgrade the per-work statement banner to the Figma design (short rule + work-title
heading + statement, as a full-width "featured" block above its own card).

Unlike tools/migrate_exhibition_statements.py this does NOT extract/strip anything —
works.json (art_works + exhibition_statements) is treated as authoritative:
  - art_works[].statement_he  = per-work text (rendered as a featured banner)
  - exhibition_statements[]    = (artist x exhibition) group text

Idempotent. Run from repo root:  python3 tools/sync_works_mirrors.py
"""
import json, re, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

d = json.load(open("data/works.json", encoding="utf-8"))
ART = d["art_works"]
STORE = d["exhibition_statements"]
BY_ID = {w["id"]: w for w in ART}

# Exhibition recency for artist pages: data/exhibitions.json is ordered chronologically
# ASCENDING, so a later index = a newer show. The artist page sorts its exhibition groups
# by this rank DESCENDING (user decision 2026-08-12: newest exhibition on top).
# Adding a new exhibition = append it to exhibitions.json and re-run this script.
EX_ORDER = [e["slug"] for e in json.load(open("data/exhibitions.json", encoding="utf-8"))["exhibitions"]]


def replace_js_array(text, var_name, arr):
    payload = "window.%s=%s" % (var_name, json.dumps(arr, separators=(",", ":"), ensure_ascii=False))
    pat = re.compile(r"window\." + re.escape(var_name) + r"=\[.*?\](?=;?</script>)", re.S)
    return pat.subn(lambda _: payload, text, count=1)


# ---- renderer upgrade snippets (idempotent) ----
# v3: statement banner spans full grid width, but the artwork CARD stays a normal
# half-width grid item (even when alone) — banner and card are SEPARATE grid children
# (no full-width .work-featured wrapper that stretched the image edge-to-edge).
OLD_JS = ('        var cards=g.items.map(function(w){if(w.statement_he&&w.statement_he.length){'
          'var _wt=(w.title_he||w.title_en||"");'
          'var _wh=_wt?\'<div class="ws-head">\'+mixedHtml(_wt)+\'</div>\':"";'
          'return \'<div class="work-featured"><div class="work-statement"><span class="ws-rule"></span>\''
          '+_wh+\'<div class="ws-body">\'+statementHtml(w.statement_he)+\'</div></div>\'+buildRichCard(w,gi++)+\'</div>\';}'
          'return buildRichCard(w,gi++);}).join("");')
NEW_JS = ('        var cards=g.items.map(function(w){if(w.statement_he&&w.statement_he.length){'
          'var _wt=(w.title_he||w.title_en||"");'
          'var _wh=_wt?\'<div class="ws-head">\'+mixedHtml(_wt)+\'</div>\':"";'
          'return \'<div class="work-statement"><span class="ws-rule"></span>\''
          '+_wh+\'<div class="ws-body">\'+statementHtml(w.statement_he)+\'</div></div>\'+buildRichCard(w,gi++);}'
          'return buildRichCard(w,gi++);}).join("");')

OLD_CSS = ('.work-featured{grid-column:1/-1;display:flex;flex-direction:column;gap:24px}'
           '.work-statement{direction:rtl;text-align:right;font-family:var(--heb);color:var(--ink)}'
           '.ws-rule{display:block;width:72px;height:1px;background:#EFEFEF;margin:0 0 16px auto}'
           '.ws-head{font-size:16px;letter-spacing:.02em;margin:0 0 8px;line-height:1.3}'
           '.ws-head .lat{font-family:var(--cop)}'
           '.ws-body{font-size:16px;line-height:1.7}.ws-body p{margin:0 0 .7em}.ws-body p:last-child{margin-bottom:0}')
NEW_CSS = ('.work-statement{grid-column:1/-1;direction:rtl;text-align:right;font-family:var(--heb);'
           'color:var(--ink);margin-bottom:-40px}'
           '.ws-rule{display:block;width:72px;height:1px;background:#EFEFEF;margin:0 0 16px auto}'
           '.ws-head{font-size:16px;letter-spacing:.02em;margin:0 0 8px;line-height:1.3}'
           '.ws-head .lat{font-family:var(--cop)}'
           '.ws-body{font-size:16px;line-height:1.7}.ws-body p{margin:0 0 .7em}.ws-body p:last-child{margin-bottom:0}')


# ---- exhibition-group ordering upgrade (idempotent) ----
# OLD: groups render in the order their first work appears (artist_page_pos).
# NEW: groups are sorted by exhibition recency first; ties (and unknown exhibitions)
#      keep their previous relative order, so per-artist Figma order still rules
#      inside a group and between groups of the same show.
OLD_GROUP_JS = (
    '    function buildExGroups(list){\n'
    '      var groups=[], byKey={};\n'
    '      list.forEach(function(w){\n'
    '        var key=w.exhibition_title_he||"__ungrouped__";\n'
    '        if(!byKey[key]){byKey[key]={title:w.exhibition_title_he,route:w.exhibition_route,'
    'statement:exStatement(a.slug,w.exhibition_title_he),items:[]};groups.push(byKey[key]);}\n'
    '        byKey[key].items.push(w);\n'
    '      });\n'
    '      var gi=0;\n')
NEW_GROUP_JS = (
    '    /* Newest exhibition on top (user decision 2026-08-12). Rank = position in\n'
    '       data/exhibitions.json (chronological ascending) -> sorted descending here.\n'
    '       Unknown/ungrouped ranks -1 and sinks to the bottom; equal ranks keep the\n'
    '       artist_page_pos order, so Figma still decides inside a show. */\n'
    '    function exRank(slug){var L=window.__EX_ORDER_INLINE__||[];var i=L.indexOf(slug);return i<0?-1:i;}\n'
    '    function buildExGroups(list){\n'
    '      var groups=[], byKey={};\n'
    '      list.forEach(function(w){\n'
    '        var key=w.exhibition_title_he||"__ungrouped__";\n'
    '        if(!byKey[key]){byKey[key]={title:w.exhibition_title_he,route:w.exhibition_route,'
    'slug:w.exhibition_slug,statement:exStatement(a.slug,w.exhibition_title_he),items:[]};groups.push(byKey[key]);}\n'
    '        byKey[key].items.push(w);\n'
    '      });\n'
    '      groups=groups.map(function(g,i){return {g:g,i:i,r:exRank(g.slug)};})\n'
    '        .sort(function(x,y){return (y.r-x.r)||(x.i-y.i);})\n'
    '        .map(function(o){return o.g;});\n'
    '      var gi=0;\n')


def main():
    # ---- 1) artist pages ----
    artist_files = sorted(glob.glob("artists/*/index.html"))
    patched = 0
    for fp in artist_files:
        t = open(fp, encoding="utf-8").read()
        orig = t
        t, _ = replace_js_array(t, "__ART_WORKS_INLINE__", ART)
        if "function buildExGroups(list){" in t:
            # ex-statements inline
            ex_script = '<script id="ex-statements-inline">window.__EX_STATEMENTS_INLINE__=%s</script>' % \
                json.dumps(STORE, separators=(",", ":"), ensure_ascii=False)
            if 'id="ex-statements-inline"' in t:
                t = re.sub(r'<script id="ex-statements-inline">window\.__EX_STATEMENTS_INLINE__=\[.*?\]</script>',
                           lambda _: ex_script, t, count=1, flags=re.S)
            # exhibition order inline (file:// can't fetch exhibitions.json) — create or refresh
            order_script = '<script id="ex-order-inline">window.__EX_ORDER_INLINE__=%s</script>' % \
                json.dumps(EX_ORDER, separators=(",", ":"), ensure_ascii=False)
            if 'id="ex-order-inline"' in t:
                t = re.sub(r'<script id="ex-order-inline">window\.__EX_ORDER_INLINE__=\[.*?\]</script>',
                           lambda _: order_script, t, count=1, flags=re.S)
            elif 'id="ex-statements-inline"' in t:
                t = t.replace(ex_script, ex_script + "\n" + order_script, 1)
            # exhibition-group ordering upgrade (idempotent: OLD vanishes after replace)
            if OLD_GROUP_JS in t:
                t = t.replace(OLD_GROUP_JS, NEW_GROUP_JS, 1)
            elif "function exRank(slug){" not in t:
                print("  ! group-order anchor not found:", fp, file=sys.stderr)
            # banner renderer upgrade (idempotent: OLD vanishes after replace)
            if OLD_JS in t:
                t = t.replace(OLD_JS, NEW_JS, 1)
            elif NEW_JS not in t:
                print("  ! banner JS anchor not found:", fp, file=sys.stderr)
            if OLD_CSS in t:
                t = t.replace(OLD_CSS, NEW_CSS, 1)
            elif NEW_CSS not in t:
                print("  ! banner CSS anchor not found:", fp, file=sys.stderr)
            patched += 1
        if t != orig:
            open(fp, "w", encoding="utf-8").write(t)
    print("  artist pages: %d scanned, %d with grouping renderer" % (len(artist_files), patched))

    # ---- 2) works/index.html grid mirror ----
    fp = "works/index.html"
    t = open(fp, encoding="utf-8").read()
    pretty = "\n" + json.dumps(ART, ensure_ascii=False, indent=2) + "\n"
    t2, n = re.subn(r'(<script[^>]*id="works-data"[^>]*>).*?(</script>)',
                    lambda m: m.group(1) + pretty + m.group(2), t, count=1, flags=re.S)
    if n and t2 != t:
        open(fp, "w", encoding="utf-8").write(t2)
    print("  works/index.html #works-data refreshed:", bool(n))

    # ---- 3) single artwork pages: refresh from works.json. statement_he shown =
    #         per-work text if any, ELSE the artist's exhibition statement from the
    #         store, ELSE nothing (the renderer reads w.statement_he verbatim). ----
    store_lut = {(r["artist_slug"], r["exhibition_title_he"]): r["statement_he"] for r in STORE}
    single = changed = missing = 0
    for fp in sorted(glob.glob("works/*/index.html")):
        if fp == "works/index.html":
            continue
        t = open(fp, encoding="utf-8").read()
        m = re.search(r'(<script[^>]*id="artwork-data"[^>]*>)(\{.*?\})(</script>)', t, re.S)
        if not m:
            continue
        single += 1
        rec_old = json.loads(m.group(2))
        wid = rec_old.get("id")
        base = BY_ID.get(wid)
        if not base:
            missing += 1
            print("  ! single page id not in works.json:", wid, fp, file=sys.stderr)
            continue
        rec = dict(base)
        if not rec.get("statement_he"):
            stmt = store_lut.get((rec["artist_slug"], rec.get("exhibition_title_he")))
            if stmt:
                rec["statement_he"] = stmt  # fall back to artist's exhibition statement
            else:
                rec.pop("statement_he", None)  # nothing to show -> leave empty
        compact = json.dumps(rec, separators=(",", ":"), ensure_ascii=False)
        if compact != m.group(2):
            t = t[:m.start(2)] + compact + t[m.end(2):]
            open(fp, "w", encoding="utf-8").write(t)
            changed += 1
    print("  single pages: %d scanned, %d updated, %d id-mismatch" % (single, changed, missing))
    print("done.")


if __name__ == "__main__":
    main()
