# -*- coding: utf-8 -*-
"""Generate the 5 works/melani-hekimoglu-N/ pages from the shira-turbowicz-1 template."""
import json, os, re, html, subprocess, collections

SRC = "works/shira-turbowicz-1/index.html"
tpl = open(SRC, encoding="utf-8").read()
W = json.load(open("data/works.json", encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
BY_ID = {w["id"]: w for w in W["art_works"]}
STMT = [s for s in W["exhibition_statements"] if s["artist_slug"] == "melani-hekimoglu"][0]

BLURB = {
    1: "אגרטלי קרמיקה בעבודת יד",
    2: "קערת קינוחים מקרמיקה",
    3: "אדנית קרמיקה",
    4: "צלחות וקערות קרמיקה",
    5: "מנורת קרמיקה",
}

def sub1(pat, rep, s, flags=0):
    s2, n = re.subn(pat, lambda _m: rep, s, count=1, flags=flags)
    assert n == 1, "no match: " + pat[:60]
    return s2

def ogdims(jpg):
    out = subprocess.run(["magick", "identify", "-format", "%w %h", jpg],
                         capture_output=True, text=True).stdout.split()
    return int(out[0]), int(out[1])

for n in range(1, 6):
    wid = "melani-hekimoglu-%d" % n
    w = BY_ID[wid]
    t = tpl
    title_disp = w["title_en"].upper()
    page_title = "%s · %s — Zielinski &amp; Rozen" % (html.escape(title_disp), w["artist_he"])
    desc = ("%s — %s. %s, רזידנסי בגלריית כיכר דיזינגוף של Zielinski &amp; Rozen, "
            "28.09–05.10.2026." % (html.escape(title_disp), w["artist_he"], BLURB[n]))
    ogjpg = "og/works-v2-%s.jpg" % wid
    ow, oh = ogdims(ogjpg)
    U = "https://art.zrp.co.il/works/%s/" % wid

    t = sub1(r'<html lang="he" dir="ltr" data-artwork-id="shira-turbowicz-1">',
             '<html lang="he" dir="ltr" data-artwork-id="%s">' % wid, t)
    t = sub1(r'<title>.*?</title>', '<title>%s</title>' % page_title, t)
    t = sub1(r'<meta name="description" content=".*?">',
             '<meta name="description" content="%s">' % desc, t)
    t = sub1(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="%s">' % U, t)
    t = sub1(r'<meta property="og:title" content=".*?">',
             '<meta property="og:title" content="%s">' % page_title, t)
    t = sub1(r'<meta property="og:description" content=".*?">',
             '<meta property="og:description" content="%s">' % desc, t)
    t = sub1(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="%s">' % U, t)
    t = sub1(r'<meta property="og:image" content=".*?">',
             '<meta property="og:image" content="https://art.zrp.co.il/%s">' % ogjpg, t)
    t = sub1(r'<meta property="og:image:width" content=".*?">',
             '<meta property="og:image:width" content="%d">' % ow, t)
    t = sub1(r'<meta property="og:image:height" content=".*?">',
             '<meta property="og:image:height" content="%d">' % oh, t)
    t = sub1(r'<meta property="og:image:alt" content=".*?">',
             '<meta property="og:image:alt" content="%s">' % page_title, t)
    t = sub1(r'<meta name="twitter:title" content=".*?">',
             '<meta name="twitter:title" content="%s">' % page_title, t)
    t = sub1(r'<meta name="twitter:description" content=".*?">',
             '<meta name="twitter:description" content="%s">' % desc, t)
    t = sub1(r'<meta name="twitter:image" content=".*?">',
             '<meta name="twitter:image" content="https://art.zrp.co.il/%s">' % ogjpg, t)

    medium = w["details_he"].replace("\n", " ")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "VisualArtwork", "@id": U + "#artwork", "url": U, "name": w["title_en"],
         "image": "https://art.zrp.co.il/images/works/v2/%s.webp" % wid,
         "creator": {"@type": "Person", "name": w["artist_en"],
                     "@id": "https://art.zrp.co.il/artists/melani-hekimoglu/#person",
                     "url": "https://art.zrp.co.il/artists/melani-hekimoglu/"},
         "isPartOf": {"@id": "https://art.zrp.co.il/#org"}, "artMedium": medium},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "The Art Works",
             "item": "https://art.zrp.co.il/works/"},
            {"@type": "ListItem", "position": 2, "name": w["artist_en"],
             "item": "https://art.zrp.co.il/artists/melani-hekimoglu/"},
            {"@type": "ListItem", "position": 3, "name": w["title_en"], "item": U}]}]}
    t = sub1(r'<script type="application/ld\+json">\{"@context".*?</script>',
             '<script type="application/ld+json">%s</script>'
             % json.dumps(ld, ensure_ascii=False, separators=(",", ":")), t, re.S)

    # ---- #artwork-data (compact mirror + statement fallback, like the generator does) ----
    data = collections.OrderedDict(w)
    data["statement_he"] = STMT["statement_he"]
    t = sub1(r'(<script type="application/json" id="artwork-data">).*?(</script>)',
             '<script type="application/json" id="artwork-data">%s</script>'
             % json.dumps(data, ensure_ascii=False, separators=(",", ":")), t, re.S)

    # ---- renderer: no exhibition title on a residency -> don't emit an empty title element ----
    OLD = """  var exHeadInner = latHtml(w.exhibition_title_he||'');
  var exHead = w.exhibition_route
    ? '<a class="aw-ex-title" href="../../'+w.exhibition_route+'/">'+exHeadInner+'</a>'
    : '<span class="aw-ex-title">'+exHeadInner+'</span>';"""
    NEW = """  /* Residency without a show (frame 1634:188): exhibition_title_he is null, so the
     statement stands alone — no empty title element above it. */
  var exHeadInner = latHtml(w.exhibition_title_he||'');
  var exHead = !w.exhibition_title_he ? ''
    : (w.exhibition_route
      ? '<a class="aw-ex-title" href="../../'+w.exhibition_route+'/">'+exHeadInner+'</a>'
      : '<span class="aw-ex-title">'+exHeadInner+'</span>');"""
    assert OLD in t, "exHead anchor missing"
    t = t.replace(OLD, NEW, 1)

    os.makedirs("works/%s" % wid, exist_ok=True)
    open("works/%s/index.html" % wid, "w", encoding="utf-8").write(t)
    print("wrote works/%s/index.html  (og %dx%d)" % (wid, ow, oh))
