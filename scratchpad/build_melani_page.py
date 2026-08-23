# -*- coding: utf-8 -*-
"""Build artists/melani-hekimoglu/index.html from the shira-turbowicz page
   (newest artist template: ex-groups + curator strip)."""
import os, re, io

SRC = "artists/shira-turbowicz/index.html"
DST_DIR = "artists/melani-hekimoglu"
DST = DST_DIR + "/index.html"
t = open(SRC, encoding="utf-8").read()

DESC = ("מלאני הקימוגלו — אמנית ומעצבת קרמיקה. הסדרות FLOW ו-BLOOM ברזידנסי בגלריית כיכר "
        "דיזינגוף, 28.09–05.10.2026, באוצרות קורין אברהם.")
TITLE = "melani hekimoglu — Zielinski &amp; Rozen"

def sub1(pat, rep, s, flags=0):
    s2, n = re.subn(pat, lambda _m: rep, s, count=1, flags=flags)
    assert n == 1, "no match: " + pat[:70]
    return s2

# ---- head ----
t = sub1(r'<html lang="he" dir="ltr" data-slug="shira-turbowicz">',
         '<html lang="he" dir="ltr" data-slug="melani-hekimoglu">', t)
t = sub1(r'<title>.*?</title>', '<title>%s</title>' % TITLE, t)
t = sub1(r'<meta name="description" content=".*?">',
         '<meta name="description" content="%s">' % DESC, t)
t = sub1(r'<link rel="canonical" href=".*?">',
         '<link rel="canonical" href="https://art.zrp.co.il/artists/melani-hekimoglu/">', t)
t = sub1(r'<meta property="og:title" content=".*?">',
         '<meta property="og:title" content="%s">' % TITLE, t)
t = sub1(r'<meta property="og:description" content=".*?">',
         '<meta property="og:description" content="%s">' % DESC, t)
t = sub1(r'<meta property="og:url" content=".*?">',
         '<meta property="og:url" content="https://art.zrp.co.il/artists/melani-hekimoglu/">', t)
t = sub1(r'<meta property="og:image" content=".*?">',
         '<meta property="og:image" content="https://art.zrp.co.il/og/artists-melani-hekimoglu-portrait.jpg">', t)
t = sub1(r'<meta property="og:image:width" content=".*?">',
         '<meta property="og:image:width" content="1080">', t)
t = sub1(r'<meta property="og:image:height" content=".*?">',
         '<meta property="og:image:height" content="1080">', t)
t = sub1(r'<meta property="og:image:alt" content=".*?">',
         '<meta property="og:image:alt" content="%s">' % TITLE, t)
t = sub1(r'<meta name="twitter:title" content=".*?">',
         '<meta name="twitter:title" content="%s">' % TITLE, t)
t = sub1(r'<meta name="twitter:description" content=".*?">',
         '<meta name="twitter:description" content="%s">' % DESC, t)
t = sub1(r'<meta name="twitter:image" content=".*?">',
         '<meta name="twitter:image" content="https://art.zrp.co.il/og/artists-melani-hekimoglu-portrait.jpg">', t)

JSONLD = ('<script type="application/ld+json">{"@context":"https://schema.org","@graph":['
 '{"@type":"ProfilePage","@id":"https://art.zrp.co.il/artists/melani-hekimoglu/#webpage",'
 '"url":"https://art.zrp.co.il/artists/melani-hekimoglu/","name":"melani hekimoglu — Zielinski & Rozen",'
 '"isPartOf":{"@id":"https://art.zrp.co.il/#website"},'
 '"mainEntity":{"@id":"https://art.zrp.co.il/artists/melani-hekimoglu/#person"}},'
 '{"@type":"Person","name":"melani hekimoglu","alternateName":"מלאני הקימוגלו",'
 '"url":"https://art.zrp.co.il/artists/melani-hekimoglu/",'
 '"image":"https://art.zrp.co.il/og/artists-melani-hekimoglu-portrait.jpg","jobTitle":"Artist",'
 '"memberOf":{"@id":"https://art.zrp.co.il/#org"},'
 '"description":"%s","sameAs":["https://www.instagram.com/melani.ceramics/"],'
 '"@id":"https://art.zrp.co.il/artists/melani-hekimoglu/#person"},'
 '{"@type":"BreadcrumbList","itemListElement":['
 '{"@type":"ListItem","position":1,"name":"Artists","item":"https://art.zrp.co.il/artists/"},'
 '{"@type":"ListItem","position":2,"name":"melani hekimoglu",'
 '"item":"https://art.zrp.co.il/artists/melani-hekimoglu/"}]}]}</script>') % DESC.replace('"', '\\"')
t = sub1(r'<script type="application/ld\+json">\{"@context".*?</script>', JSONLD, t, re.S)

# ---- page-local CSS: replace shira's block with melani's ----
OLD_CSS_START = "\n/* ===== shira turbowicz (sumii) — page-local ===== */"
i = t.index(OLD_CSS_START)
j = t.index("</style>", i)
NEW_CSS = '''
/* ===== melani hekimoglu — page-local (Figma XhGH…::1634:188, mobile only; desktop = adaptation) ===== */
/* The frame puts the FULL name on ONE Bold line (1634:214, Copperplate Bold 36, centered) —
   unlike the two-line bold/light split every other artist frame uses (cf. hadas-tuval 797:106).
   Optical calibration (our Copperplate runs ~33% wider than Figma's): the frame renders
   "MELANI HEKIMOGLU" 326.7px wide inside the 358px column -> 27px here matches it exactly.
   Desktop has no frame: 54px = 653px, the widest that clears the 676px text column. */
.hero-name .first{white-space:nowrap}
.hero-name .first,.hero-name .last{font-size:54px}
@media (min-width:1101px){
  .hero-name .first,.hero-name .last{font-size:54px}
}
/* residency statement (1634:230/231): lead line FbEzmel Regular 20, body Light 18 — Hebrew px verbatim.
   :first-child = the lead paragraph of exhibition_statements[].statement_he. */
.ex-statement{font-size:18px;gap:14px}
.ex-statement p:first-child{font-size:20px;font-weight:400}
/* statement: founder / curator mentions are links (docs/artist-linking.md) */
.ex-statement a.artist-link{color:inherit;text-decoration:underline;text-decoration-color:rgba(27,27,27,.25);text-underline-offset:3px;transition:text-decoration-color .2s,opacity .2s}
.ex-statement a.artist-link:hover{text-decoration-color:currentColor;opacity:.75}
/* THE CURATOR — artists-strip pattern (event pages / sponsors/sumii), single card → curator page (Figma 1634:261) */
.curator-strip{padding:0 var(--pad-x) 48px;display:flex;justify-content:center;background:var(--white)}
.curator-strip .inner{display:flex;flex-direction:column;gap:16px;width:100%;max-width:var(--max)}
.curator-strip .label{font-family:var(--cop);font-weight:300;font-size:28px;color:var(--ink);text-align:left;letter-spacing:.02em}
.curator-strip .strip{display:flex;flex-direction:row;gap:6px}
.curator-strip .strip>a.artist-card{flex:0 0 178px;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;color:inherit}
.curator-strip .strip .img{width:178px;height:148px;overflow:hidden;background:#f3f1ee}
.curator-strip .strip .img picture{display:contents}
.curator-strip .strip .img img{width:100%;height:100%;object-fit:cover;transition:filter .25s}
.curator-strip .strip .name{font-family:var(--cop);font-weight:300;font-size:18px;line-height:18px;color:var(--artist);text-align:center;letter-spacing:.04em}
a.artist-card:hover .img img{filter:brightness(.92)}
a.artist-card:hover .name{color:var(--ink)}
@media (max-width:768px){
  .hero-name .first,.hero-name .last{font-size:27px}
  .ex-statement{font-size:18px;line-height:1.45;gap:14px}
  .ex-statement p:first-child{font-size:20px}
  .curator-strip{padding:0 16px 32px}
  .curator-strip .label{font-size:20px}
  .curator-strip .strip>a.artist-card{flex:0 0 112px}
  .curator-strip .strip .img{width:96px;height:80px}
  .curator-strip .strip .name{font-size:13px;line-height:16px}
}
@media (max-width:400px){
  /* 27px = 326.7px, 1px shy of the 328px column at a 360px viewport — step down */
  .hero-name .first,.hero-name .last{font-size:25px}
}
'''
t = t[:i] + NEW_CSS + t[j:]

# ---- renderer: full name on one line (no studio_en mechanism here) ----
OLD_NP = '''    function heroNameParts(nameEn){
      /* artist with a studio/brand: full name stays on ONE line (.first), studio name
         goes on the line below (.last) — Figma 1608:5754/5755 ("Shira Turbowicz" / "sumii") */
      if(a.studio_en){
        return {first:String(nameEn||"").trim(),last:String(a.studio_en).trim()};
      }
'''
NEW_NP = '''    function heroNameParts(nameEn){
      /* Melani's frame (1634:214) sets the FULL name on one Bold line, so it is not split
         into the template's bold-first / light-last pair. */
      return {first:String(nameEn||"").trim(),last:""};
      /* eslint-disable no-unreachable */
'''
assert OLD_NP in t
t = t.replace(OLD_NP, NEW_NP, 1)

# ---- renderer: allow a statement with no group heading ----
OLD_GATE = '      if(rich.some(function(w){return w.exhibition_title_he;})){'
NEW_GATE = ('      /* Residency without a show: exhibition_title_he is null, but the group still\n'
            '         carries a statement (works.json exhibition_statements, keyed on a null title). */\n'
            '      if(rich.some(function(w){return w.exhibition_title_he||exStatement(a.slug,w.exhibition_title_he);})){')
assert OLD_GATE in t
t = t.replace(OLD_GATE, NEW_GATE, 1)

OLD_HEAD = '''        var head="";
        if(g.title){
          var hi=mixedHtml(g.title);
          var hh='<h3 class="ex-heading">'+(g.route?'<a href="../../'+escapeHtml(g.route)+'/">'+hi+'</a>':hi)+'</h3>';
          var st=g.statement?('<div class="ex-statement">'+statementHtml(g.statement)+'</div>'):'';
          head='<header class="ex-group-head">'+hh+st+'</header>';
        }'''
NEW_HEAD = '''        var head="";
        /* Frame 1634:188 shows the residency text with NO group heading above it, so the
           header renders for a statement alone as well as for a titled exhibition. */
        if(g.title||g.statement){
          var hh="";
          if(g.title){
            var hi=mixedHtml(g.title);
            hh='<h3 class="ex-heading">'+(g.route?'<a href="../../'+escapeHtml(g.route)+'/">'+hi+'</a>':hi)+'</h3>';
          }
          var st=g.statement?('<div class="ex-statement">'+statementHtml(g.statement)+'</div>'):'';
          head='<header class="ex-group-head">'+hh+st+'</header>';
        }'''
assert OLD_HEAD in t
t = t.replace(OLD_HEAD, NEW_HEAD, 1)

os.makedirs(DST_DIR, exist_ok=True)
open(DST, "w", encoding="utf-8").write(t)
print("wrote", DST, len(t), "bytes")
