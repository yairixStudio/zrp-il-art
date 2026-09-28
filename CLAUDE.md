# CLAUDE.md — Zielinski & Rozen Art Galleries (SPINE)

> **חובה לקרוא לפני כל משימה**, ולעדכן בסיום.
> זה ה-spine: כללים, מבנה, חוזים ו-workflow. **המצב וכללי-העריכה של כל דף חיים ב-`docs/routes/<משפחה>.md` — חובה לקרוא את הקובץ של המשפחה לפני שנוגעים בדף** (מפה ב-§1).
> ההיסטוריה המלאה של הקובץ הישן (עד 2026-09-27): `docs/history/CLAUDE-2026-09-27.md` — ארכיון לקריאה בלבד; מסמך עדכני גובר עליו.

---

## 0. TL;DR לסוכנים חדשים

1. אתה בונה **דף אחד מתוך אתר**. לא פרויקט בועתי.
2. **לפני עריכת דף — קרא את ה-route doc שלו** (`docs/routes/…`, §1). שם: מבנה נוכחי, הכרעות משתמש, "אל תתקן", מה לסנכרן. ה-spine לא מחליף אותו.
3. **🔗 קישורי Figma:** ב-[`FIGMA_LINKS.md`](./FIGMA_LINKS.md) (+ nodes לכל דף ב-route doc). אם הדף חסר — הוסף לפני שאתה מתחיל.
4. פונטים ב-`./פונטים/` — תמיד `@font-face`. **אסור Google Fonts**.
5. נתונים מ-`./data/*.json`. שדה חסר → תוסיף ל-JSON קודם (חוזים: `docs/data-contracts.md`). **אחרי כל שינוי ב-JSON → `python3 tools/sync_data.py`** (מייצר את כל העותקים האוטומטיים; §6).
6. תמונות ב-`./images/<category>/<slug>/`. **לפני הורדה — `ls` קודם.**
7. **כל דף = שני לינקים מהמשתמש (desktop + mobile)**. **אל תזהה לפי שם node** — הוא משקר. תזהה לפי `absoluteBoundingBox.width`: 1440=desktop, 390=mobile. **node-id אינו מצביע יציב** — המעצבת משכתבת פריימים in-place (קרה: soos→sumii).
8. **מובייל ≠ דסקטופ מצומצם.** sections ייחודיים, סדר שונה, overlay אחר. תבדוק שני frames לפני CSS.
9. **אינטראקטיביות נסתרת.** Figma סטטי; באתר יש גלילה אופקית, lightbox, hover scale. ראה `docs/lessons.md §1` — Static-vs-Dynamic. **שאל אם לא ברור.**
10. **כל אנגלית באתר = Copperplate UPPERCASE.** הכלל ב-CSS גלובלי. פרטים: `docs/conventions.md §5`.
11. **עברית+אנגלית באותה שורה/מחרוזת:** FbEzmel לעברית, `<span class="lat">` + Copperplate ל-Latin — **גודל ויזואלי** (em optical), לא אותו `font-size` px. פרטים: `docs/conventions.md §5.2`.
12. **כל אזכור אומן = קישור** (`docs/artist-linking.md`). הפרה = הדף לא מוכן.
13. **🔴 כל דף/פוסט חדש = רשומה ב-`sitemap.xml`, באותו קומיט** (כלל-זהב 15). בלי זה הדף לא קיים לגוגל.
14. **בדיקה ויזואלית/טיפוגרפית — רק דרך http** (`python3 -m http.server`, מוגדר ב-`.claude/launch.json`). ב-file:// כרום **חוסם את ה-`@font-face`** (CORS, origin null) והדף מוצג בפונטי fallback — אל תשפוט טיפוגרפיה משם.
15. **שינוי שנוגע בהרבה דפים** (הפצת תבנית, CSS/JS משותף, צנרת דאטה) → **חובה** harness הרגרסיה (§7.1) לפני קומיט.
16. **סשנים מקבילים עובדים על אותו ריפו.** Re-Read לפני edit, וקומיט רק של הקבצים שלך (`git add <paths>`, לא `-A`) — **כולל כל קובץ ש-`sync_data.py` כתב** (כלל-זהב 14).
17. **🔴 לפני שיוצרים דף/רשומה — לחפש שאריות של אותה ישות** (כרטיס "בקרוב", רשומה עם `route:null`, id תפוס) — §7 שלב 2. קיימת ⇒ לשאול ולקדם אותה, **לא לשכפל id**.
18. בסוף — עדכן את ה-route doc (מצב **נוכחי**, לא יומן — §7.2), את שורת ה-§4 אם הסטטוס השתנה **או שנוסף/נמחק דף במשפחה**, `FIGMA_LINKS.md` אם גילית URL חדש, `docs/data-contracts.md` אם נוסף שדה, ולקח חדש ב-`docs/lessons.md §4`.

---

## 1. Required Reading Map — תפתח לפי מה שאתה עושה

> **כלל ברזל:** לפני שאתה כותב CSS/HTML או נוגע בתוכן — תוודא שקראת את ה-docs הרלוונטיים. אל תנחש מהזיכרון. הקבצים האלה הם המקור הסמכותי.

### 1.1 לפי הדף שאתה עורך — **חובה לפני כל עריכה**

| אם אתה נוגע ב... | קרא חובה |
|---|---|
| `index.html` (עמוד הבית, כל סקשן) | [`docs/routes/homepage.md`](./docs/routes/homepage.md) |
| `about/` | [`docs/routes/about.md`](./docs/routes/about.md) |
| `works/` (הגריד + עמוד לכל יצירה) | [`docs/routes/works.md`](./docs/routes/works.md) |
| `galleries/` | [`docs/routes/galleries.md`](./docs/routes/galleries.md) |
| `exhibitions/`, `curators/`, `opencalls/` | [`docs/routes/exhibitions.md`](./docs/routes/exhibitions.md) |
| `artists/` (הגריד + דף לכל אומן) | [`docs/routes/artists.md`](./docs/routes/artists.md) |
| `press/` (ארכיון + כתבות) | [`docs/routes/press.md`](./docs/routes/press.md) |
| `events/index.html`, `events/{ktuba,loneliness,close-look,artist-talk,how-many,gala-night}/`, וריאנט **אירועי רזידנסי SUMII** `events/{niki-de-saint-phalle-day,sumii-opening,sumii-melani-hosting,yom-kippur-wish-tree,sumii-live-studio}/` | [`docs/routes/events.md`](./docs/routes/events.md) |
| כל `events/<slug>/` אחר (משפחת "artist talk") | [`docs/routes/events-talks.md`](./docs/routes/events-talks.md) |
| `sponsors/` | [`docs/routes/sponsors.md`](./docs/routes/sponsors.md) |
| `data/*.json`, `data/generated/`, כל עותק דאטה בתוך דף | [`docs/data-contracts.md`](./docs/data-contracts.md) |

### 1.2 לפי סוג העבודה

| אם אתה עושה... | קרא חובה |
|---|---|
| כותב CSS חדש, נוגע ב-typography, RTL, casing, `text-transform`, responsive, mixed Hebrew/English, או tokens | [`docs/conventions.md`](./docs/conventions.md) |
| מוסיף/נוגע ב-lightbox, gallery, carousel, slideshow, או רואה ב-Figma תמונות עם dots | [`docs/components.md`](./docs/components.md) |
| מוסיף תוכן/קוד שמזכיר אומן (שם, תמונה, פסקת body, caption, alt) | [`docs/artist-linking.md`](./docs/artist-linking.md) — **חובה לפני סיום משימה** |
| בונה דף חדש או נתקלת ב-Figma quirk / Static-vs-Dynamic decision | [`docs/lessons.md`](./docs/lessons.md) |
| בודק אם משהו כבר נסגר או נתקלת ב-placeholder | [`docs/todo.md`](./docs/todo.md) |
| מתחיל לבנות דף — צריך URLs של Figma | [`FIGMA_LINKS.md`](./FIGMA_LINKS.md) |
| **סיים דף/פוסט חדש** — sitemap, canonical, OG, JSON-LD | [`docs/seo.md`](./docs/seo.md) — **חובה: הדף חייב להיכנס ל-`sitemap.xml` באותו קומיט (כלל-זהב 15)** |
| עבודה על עמוד הבית ברוח רה-דיזיין אוגוסט 2026 | [`docs/redesign-2026-08.md`](./docs/redesign-2026-08.md) |

---

## 2. מה אנחנו בונים

**אתר Zielinski & Rozen** — רשת גלריות אומנות בתל אביב (+ סקשן גלריה בברלין בעמוד הבית), מותג בישום שגם הוא אומנותי. ארז זילינסקי־רוזן (founder) הוא אמן בעצמו.

תוכן: **תערוכות**, **אומנים**, **גלריות פיזיות**, **מאמרי עיתונות**, **אירועים**, **קולות קוראים**, **works**, **ספונסרים/רזידנסי**.

עברית = body content; אנגלית = כותרות, ניווט, branding.

Stack: **HTML + CSS** (single-file per page), נתונים ב-`data/*.json`. JSONs מחקים schema של CMS עתידי. אתר סטטי ב-GitHub Pages (`https://art.zrp.co.il`) — **push = פרסום לפרודקשן**.

---

## 3. Figma files

> **📌 קישורים ישירים לכל דף ב-[`FIGMA_LINKS.md`](./FIGMA_LINKS.md).** אל תחפש URL כאן.

שני קבצים. **תזהה תמיד מה-URL** (`figma.com/design/<FILEKEY>/...`), לא לפי node-id (שני הקבצים ממוספרים מאפס).

| Key | שם | תוכן |
|---|---|---|
| `XhGH289YTRcW811wrufRJz` | **landing** | homepage, exhibitions, artist, press, events (ktuba), open-call section — ורוב הפריימים החדשים |
| `Zn3N3mBQkbYER7tTJMbCcz` | **graphics** | about (legacy), works, artist pages, events (loneliness), opencalls, lightbox states |

**MCP:** `mcp__figma__get_figma_data`, `mcp__figma__download_figma_images`. `fileKey` הוא parameter — אסור hardcode.

**node-id ב-URL = `119-156`. ב-API = `119:156`.** (dash ↔ colon)

**figma_node_id מקבל משמעות רק יחד עם fileKey** — frames יכולים לעבור בין קבצים. אמת מה-URL של המשתמש תמיד.

---

## 4. SITEMAP

> טבלה קומפקטית: שורה אחת לכל route/משפחה. **הפרטים (nodes, מבנה, הכרעות, gotchas) — ב-route doc.** אל תכתוב כאן יומן שינויים (§7.2). שורת משפחה מונה את ה-slugs שלה — **דף שנוסף/נמחק = לעדכן את השורה** (בלי ספירות: הן מתיישנות).

| Route | קובץ | סטטוס | route doc |
|---|---|---|---|
| `/` | `index.html` | ✅ רה-דיזיין אוגוסט 2026 הושלם; מקור סמכותי = פריים מובייל `1318:363` | homepage |
| `/about/` | `about/index.html` | ✅ רה-דיזיין 2026-09-01 (landing `1699:1406`/`1699:1291`) | about |
| `/works/` | `works/index.html` | ✅ גריד כל היצירות, סדר = `works.json art_works[]` | works |
| `/works/:id/` | `works/<id>/index.html` (עמוד לכל יצירה) | ✅ טמפלט data-driven (`#artwork-data` מיוצר ע"י `sync_data.py`) | works |
| `/galleries/` | — | ⏳ אין עיצוב; `#galleries` בהומפייג' משמש אינדקס | galleries |
| `/galleries/medina/`, `/galleries/dizengoff/` | `galleries/<slug>/index.html` | ✅ (flea-market ו-berlin — בלי דף) | galleries |
| `/exhibitions/` | — | ⏳ (כיום ארכיון בהומפייג') | exhibitions |
| `/exhibitions/loneliness/`, `/exhibitions/how-many/` | `exhibitions/<slug>/index.html` | ✅ data-driven מתבנית | exhibitions |
| `/exhibitions/the-peeler/` | `exhibitions/the-peeler/index.html` | ✅ **סטטי קפוא** — עריכה ידנית ב-HTML | exhibitions |
| `/curators/korin-avraham/` | `curators/korin-avraham/index.html` | ✅ | exhibitions |
| `/opencalls/` · `/opencalls/obsession/` · `/opencalls/the-peeler/` · `/opencalls/how-many/` | `opencalls/<slug>/index.html` | ⏳ · ✅ (light) · ✅ · ✅ | exhibitions |
| `/artists/` | `artists/index.html` | ✅ גריד האומנים (`#artists-grid-data`) | artists |
| `/artists/:slug/` | `artists/<slug>/index.html` (דף לכל אומן) | ✅ תבנית משותפת + `data-slug`; דאטה מ-`data/generated/*.js` | artists |
| `/press/` | `press/index.html` | ✅ ארכיון **עבר** (אירועים עתידיים נושרים בזמן ריצה) | press |
| `/press/<article>/` | walla, press-1, time-out, the-last-station, the-sixth-scent, manicure-against-darkness, peeling-a-layer, the-shared-list | ✅ | press |
| `/events/` | `events/index.html` | ✅ אירועים **קרובים** (מירור `#events-list-data`) | events |
| `/events/{ktuba,loneliness,close-look,artist-talk,how-many,gala-night}/` | `events/<slug>/index.html` | ✅ | events |
| `/events/<sumii-event>/` | niki-de-saint-phalle-day, sumii-opening, sumii-melani-hosting, yom-kippur-wish-tree, sumii-live-studio | ✅ וריאנט "אירועי רזידנסי SUMII" (כיכר דיזינגוף, בלי תערוכה; בסיס = niki-de-saint-phalle-day) | events |
| `/events/<talk>/` | natasha-zeriker, liel-salman, nir-giorgio-levin, risa-and-noemi, zohar-ron, alice-debellis, anat-wegier, the-space-between, zohar-ron-medina, noemi-safir, hadas-tuval, livay-levi, michael-konovalenko, bar-cohen, maria-artamonova, jessica-tabarovsky, elsa-ars-brush, baruch-torgeman, nir-giorgio-levin-medina | ✅ משפחת "artist talk" — עמודים סטטיים עצמאיים | events-talks |
| ~~`/events/amnon-lipkin/`~~ | — | 🗑️ נמחק 2026-08-28 (בקשת משתמש) — **הפריימים עדיין בפיגמה; אל תשחזר** | events-talks |
| `/sponsors/soos/`, `/sponsors/sumii/` | `sponsors/<slug>/index.html` | ✅ (sumii מארח גם את סקשני הרזידנסי של מלאני הקימוגלו) | sponsors |
| `/contact/`, `/accessibility/`, `/privacy/` | `<dir>/index.html` | ✅ סטטיים (טופס / הצהרה / מדיניות) | — |
| `404.html` | `404.html` | ✅ (`noindex`) | — |

**סטטי (shell):** brand, nav, footer, newsletter copy, copyright, palette + typography — ב-`data/site.json` או CSS; nav/footer מרונדרים ע"י `components/site-chrome.js` (`<site-header>`/`<site-footer>`).
**דינמי (JSON):** galleries, artists, exhibitions, events, press, opencalls, works, instagram, homepage curation, announcement, curators, sponsors.

**📬 טופס ניוזלטר (פוטר) = Wix Velo, לא Firebase — אל תחזיר Firebase** (Spark חוסם קריאות יוצאות, Functions דורש Blaze). `components/site-chrome.js` שולח `POST https://zrp.co.il/_functions/subscribe` (אתר ה-Wix "ZIELINSKI & ROZEN", siteId `03bb4cff-b492-498b-9864-9258e743d0a2`). מקור ה-backend: `newsletter-backend/wix-velo/http-functions.js` → מדביקים ל-Backend ב-Wix ומפרסמים. כל נרשם: honeypot (שדה `website`) + rate-limit לפי IP (5/דקה, קולקשן אופציונלי `NewsletterThrottle` עם שדה `ip`; fail-open) → `appendOrCreateContact` → לייבל `custom.art-newsletter` ("Art Newsletter") → סימון SUBSCRIBED דרך REST Email Subscriptions API, שדורש **Wix API key** ("Manage Email Subscriptions") בסוד `WIX_API_KEY` ב-Wix Secrets Manager (Velo לבדו לא יכול לשנות `subscriptionStatus` — read-only; בלי הסוד איש הקשר נוצר+מתויג אך לא מסומן מנוי). נרשמים רואים ב-Wix → Contacts מסונן ל-label "Art Newsletter". **גילוי פרטיות:** ההרשמה מצרפת גם לרשימת התפוצה של אתר הבשמים (zrp.co.il) — מצוין ב-`privacy/index.html` ובטקסט ההסכמה.

**הכרעות רוחביות (audit 2026-07-09 — לא לשחזר את המצב הישן):** (1) כותרת loneliness הרשמית = **"בדידות בתוך סביבה תוססת"** (אם בפיגמה "בתוך בסביבה" — טעות מוכרעת). (2) `exhibition_route` של כל יצירות הקולפן = `exhibitions/the-peeler`; עמודי `works/<id>` בונים את קישור התערוכה מ-`w.exhibition_route`. (3) איות אנגלי קנוני: **"adi duek", "zohar shitrit"** (ה-slugs נשארו `adi-duak`, `zohar-shtrit` — כלל-זהב 6). (4) BreadcrumbList ב-JSON-LD לא מפנה לעמודי אינדקס שלא נבנו.

---

## 5. STACK & FILE LAYOUT

```
.
├── index.html                 # Homepage entry → /
├── about/index.html           # → /about/
├── works/index.html           # → /works/  (+ works/<id>/index.html — one per artwork)
├── contact/, accessibility/, privacy/   # Static pages, each <dir>/index.html
├── artists/<slug>/index.html  # Per-artist pages (shared template + data-slug)
├── exhibitions/<slug>/index.html
├── opencalls/<slug>/index.html
├── press/<slug>/index.html
├── events/<slug>/index.html
├── curators/<slug>/index.html
├── galleries/<slug>/index.html
├── sponsors/<slug>/index.html
├── components/                # artwork-lightbox, gallery, stacked-gallery, triptych-gallery, site-chrome, picture-upgrade, analytics, embed-iframe
├── data/                      # JSON content (mirrors future CMS) — SOURCE OF TRUTH
│   └── generated/             # GENERATED by tools/sync_data.py — never edit by hand
├── images/                    # see docs/conventions.md §1 (WebP+AVIF only; raw originals in _originals/, gitignored)
├── og/                        # share-image JPGs (og:image)
├── docs/
│   ├── routes/                # ← per-page-family current state + rules (read before editing)
│   ├── data-contracts.md      # full JSON contracts + mirror registry
│   ├── history/               # frozen archive (read-only)
│   └── conventions, components, artist-linking, lessons, todo, seo, redesign-2026-08
├── tools/
│   ├── sync_data.py           # regenerate all generated data copies (--check to verify)
│   ├── regress/               # snapshot.mjs + diff.mjs — before/after regression harness
│   ├── search/build_index.py  # search-index.js — run automatically by .githooks/pre-commit (rule 10א)
│   └── seo/                   # refresh_sitemap_lastmod.py (safe); inject.py/og_gen.py (see rule 15)
├── פונטים/                    # Copperplate {300/400/700/900}, FbEzmel {300/400}, NotoSansArabic {300/400}, Solway
├── .nojekyll                  # Tells GitHub Pages to serve files as-is (no Jekyll processing)
├── FIGMA_LINKS.md             # All page-by-page Figma URLs
└── CLAUDE.md                  # ← you are here
```

> **URLs:** Directory-based for clean paths. `/about/` instead of `/pages/about.html`. Templates (`exhibition`, `opencall`, `artist`) are copied per slug with `data-slug` attribute on `<html>` so each page is fully self-contained at its own clean URL.

**שמות:** kebab-case, ASCII. סלאגים = `id` ב-JSON. תיקיות עברית רק לפונטים ולקובץ הזה.

**תיקיות חסרות** — תיצור. **אל תשנה חלוקה קיימת.** `scratchpad/`, `trash/`, `media/`, `_staging/`, `_originals/` = מקומיים בלבד (gitignored) — לא מתפרסמים.

---

## 6. JSON Data

**עיקרון:** דף קורא JSONs, לא מטמיע inline. שדה חסר → תוסיף ל-JSON לפני שימוש. שדה חדש → לכל הרשומות (null אם לא ידוע). **החוזים המלאים (כל שדה, משמעות, מי צורך) — [`docs/data-contracts.md`](./docs/data-contracts.md). חובה לקרוא לפני הוספה/שינוי של שדה.**

| קובץ | תוכן (בקצרה) |
|---|---|
| `site.json` | brand, nav, footer, announcement, social — גלובלי |
| `galleries.json` | גלריות: כתובות, שעות (bidi "18:00-11:00"), hero, manager |
| `artists.json` | אומנים: שמות, ביו, פורטרט, works[], instagram, `studio_en`, `curator_slug` … |
| `exhibitions.json` | תערוכות — **סדר המערך כרונולוגי עולה = מקור הדירוג "החדשה למעלה" בדפי אומן**; תערוכה חדשה → לסוף המערך |
| `events.json` | אירועים: date, gallery_id, list_* לכרטיסים, soon/pinned, event_photos[] … |
| `press.json` | כתבות+אירועים לכרטיסים: type, tag, route, cover, date, `homepage_visible` (גוף כתבה = HTML) |
| `opencalls.json` | קולות קוראים |
| `works.json` | `works[]` (שחמט ההומפייג') · `art_works[]` (כל היצירות) · `exhibition_statements[]` |
| `homepage.json` | composition layer — ids לפריטים מ-JSONs אחרים + בלוקים דקלרטיביים |
| `curators.json`, `sponsors.json`, `instagram.json` | אוצרת · ספונסרים/רזידנסי (meta בלבד) · snapshot |

### 6.1 עותקי דאטה — מה אוטומטי ומה ידני 🔴

דפים שנפתחים ב-file:// לא יכולים `fetch`, ולכן יש עותקים של הדאטה בתוך/ליד הדפים:
- **אוטומטי — `python3 tools/sync_data.py`** (אחרי **כל** שינוי ב-`artists/works/exhibitions/galleries.json`; `--check` לפני קומיט): `data/generated/{artists,art-works,ex-statements,ex-order}.js` (נטענים ע"י כל דפי האומן ב-`<script src>`), `works/index.html #works-data`, `works/<id>/ #artwork-data`, `galleries/<slug>/ #g-artworks-data`, ו-`#fallback-galleries` (2 דפי גלריה + דף האוצרת).
- **🔴 אסור להדביק דאטה לתוך דף אומן** (`window.__ARTISTS_INLINE__=…` inline) — זו השיטה הישנה; `sync_data.py --check` מתריע עליה.
- **ידני** (עותקים מעובדים — לעדכן יחד עם ה-JSON): `events/index.html #events-list-data`, `artists/index.html #artists-grid-data`, `galleries/*/ #g-exhibitions-data`, ה-`#fallback-*` בדפי exhibitions/opencalls/curators/ktuba, `event_photos` הסטטיים בדפי אירוע, וכרטיסי `#press`/`/press/` הכתובים ב-HTML. **הרשימה המלאה עם המקור לכל אחד — "Mirror registry" ב-`docs/data-contracts.md`.**

---

## 7. WORKFLOW לדף חדש

1. קרא `CLAUDE.md` + **ה-route doc של המשפחה** (§1.1).
2. בדוק ב-§4 אם הדף כבר רשום. אם לא — הוסף אותו לשורה (או שורה קומפקטית) + סקשן ב-route doc. **🔴 חיפוש שאריות לפני יצירה:** `grep -rn -i -e '<slug>' -e '<name_en>' -e '<שם בעברית>' data/*.json index.html press/index.html events/index.html docs/todo.md` — וודא שה-ids שתיצור פנויים (למשל `event-<slug>-talk` ב-`press.json`). כרטיס `--soon`/`soon:true`, רשומה עם `route:null` או id קיים ⇒ **לשאול את המשתמש** אם זו אותה ישות; אותה ⇒ לקדם את הקיים (אותו id, להסיר את ה-soon), אחרת ⇒ id חדש וייחודי. (היום: tal-nehoray — `press.json::event-tal-nehoray-talk` + כרטיס `pcard--soon` ב-`/press/`, בלי דף.)
3. קבל URLs מ-`FIGMA_LINKS.md` (או הוסף אם חסרים).
4. ספאון 2 subagents במקביל (desktop + mobile) לקרוא Figma. Prompt:
   > "קרא את הקובץ `<path>` ב-chunks של 600 שורות. החזר blueprint מובנה: dimensions, sections (top→bottom), כל הטקסטים verbatim (כולל עברית), צבעים, imageRefs, layout (gap/padding/justify/align). אל תסכם."
5. אסוף imageRefs **ייחודיים**. **`ls images/<category>/<slug>/` קודם.** הורד ב-batches מקבילים.
6. **לפני HTML — עדכן JSONs.** קרא את סעיף החוזה ב-`docs/data-contracts.md`, ו**העתק רשומת-אחות מאותו קובץ/תערוכה וערוך אותה — לא לבנות רשומה מרשימת שדות** (צורות שגויות שוברות רנדררים בשקט: `img` ולא `image`, `statement_he` = מערך פסקאות). ואז `python3 tools/sync_data.py`.
7. בנה HTML יחיד עם CSS מוטמע. Pattern: `font-face → tokens → sections → media queries → casing block (conventions.md §5)`. בדרך כלל: העתק דף-אח מאותה משפחה (ה-route doc אומר מאיזה).
8. הוסף לינק לדף ב-nav אם צריך (nav/footer גלובליים ב-`components/site-chrome.js`).
9. **לפני סיום:** עבור על `docs/artist-linking.md §7` (בדיקת anchors), וודא `text-transform`/font compliance (`conventions.md §5`), **בדוק חיתוך כותרות מלמעלה** (Copperplate caps ב-`line-height ≤1.2`; **אסור `overflow-x` על `body`** — רק על `html` — ראה `lessons.md` 2026-06-16/06-15), והרץ perf checklist (כלל-זהב 12): כל `<img>` עם `src="*.webp"` + `width`/`height` + `loading="lazy" decoding="async"` (חוץ מה-LCP שמקבל `fetchpriority="high"`). בדוק ויזואלית דרך http, לא file:// (TL;DR 14).
10. **🔴 הוסף את הדף ל-`sitemap.xml`** (כלל-זהב 15) ואז `python3 tools/seo/refresh_sitemap_lastmod.py`. **SEO/OG ידני — לפי המתכון במסמך המשפחה:** אירועים/ספונסרים `magick <hero>.webp -resize 1200x -strip -quality 82 og/<family>-<slug>-hero.jpg` (~≤300KB); יצירות/כתבות `-resize '1200x1200>'` (כתבה — מתמונת הכרטיס `cover_image`) + העתקת בלוק `SEO:auto` מדף-אח ועריכתו. **אל תריץ `og_gen.py`/`inject.py` גורפות** (שבורים — ראה כלל 15).
11. `python3 tools/sync_data.py --check` → exit 0.
12. עדכן: ה-route doc (מצב נוכחי — §7.2), שורת §4 (סטטוס / דף שנוסף במשפחה), `docs/data-contracts.md` אם הוספת שדה, `docs/lessons.md §4` אם יש לקח חדש. קומיט של הקבצים שלך בלבד — `git status --short` ולהוסיף **בשמם** גם את כל מה ש-`sync_data.py` ו-hook ה-pre-commit כתבו.

**שיתוף קבצים:** לפני edit ל-`index.html`, `data/*.json`, `CLAUDE.md`, `docs/routes/*`, או כל קובץ shared — **Re-Read קודם**. סוכנים/סשנים מקבילים יוצרים race conditions.

### 7.1 Harness רגרסיה — לכל שינוי רוחבי

```bash
node tools/regress/snapshot.mjs --label before            # לפני השינוי (אפשר --only artists/,events/ ; --widths 390,1024,1366,1440)
# … השינוי …
node tools/regress/snapshot.mjs --label after
node tools/regress/diff.mjs before after                  # exit 0 = זהה
```
משווה לכל דף (ברירת מחדל 390 + 1440, http + file://): DOM אחרי JS, computed style של כל אלמנט (כולל ::before/::after), תיבות, גודל גלילה, שגיאות קונסול ובקשות שנכשלו. תאריך/random מוקפאים, בקשות חיצוניות חסומות, דף חדש שעוד לא בקומיט נכלל. **חובה** לפני קומיט של: הפצת תבנית לדפים רבים, שינוי ב-`components/*`, CSS/JS משותף, צנרת דאטה.
- **אותם `--only`/`--widths` בשתי הריצות** (דף שקיים רק באחת = הבדל).
- שינוי **מכוון** → diff יוצא 1 — קרא אותו וודא שרק הדפים/האלמנטים המכוונים השתנו.
- עבודת layout/טיפוגרפיה: הוסף רוחבי ביניים (`--widths 390,1024,1366,1440`) — באגים של משפחות יושבים ב-769–1100 / 1320–1439.
- הפלט ב-`$REGRESS_OUT` (ברירת מחדל: תיקיית tmp של המערכת, `zrp-regress/<label>`) — לא בתוך הריפו.

### 7.2 משמעת תיעוד — כדי שה-spine לא יתנפח שוב 🔴

- **route doc = מצב נוכחי, לא יומן.** כשמשהו משתנה — **ערוך את הבולט הקיים** כך שיתאר את המצב החדש. אל תוסיף פסקת "🔴 2026-xx-xx — …" מעל המצב הישן. היסטוריה = הודעת הקומיט (`git log`).
- **מה חייב להישאר ב-route doc:** הכרעות משתמש, "אל תתקן / verbatim", סטיות מכוונות מהפיגמה, "נמחק — אל תשחזר", מה לסנכרן, gotchas, nodes של פיגמה, ערכי כיול.
- **ה-spine (הקובץ הזה) לא מקבל פרטי-דף.** שורת §4 = שורה אחת. כל השאר → route doc. יעד: ≤ ~30KB.

---

## 8. כללי-זהב (אסור לשבור) 🔴

1. **לא משכפלים תוכן** מ-JSON ל-HTML. שדה חסר → תוסיף ל-JSON. (עותקים נדרשים ל-file:// — רק דרך `tools/sync_data.py` או ברשימת העותקים הידניים, §6.1.)
2. **לא Google Fonts** כתחליף לפונטים מקומיים. **גם לא Inter/sans-serif כברירת מחדל** — אם צריך גופן ללא-Copperplate, להוריד מקומית.
3. **🔴 כל אנגלית = Copperplate UPPERCASE** — כולל אימיילים, handles, URLs, שמות אומנים, caption. הפרה = bug. פרטים ב-`docs/conventions.md §5`. (חריגות מוכרעות ומתועדות בלבד — למשל מותגי soos ב-`.brand`, ראה `docs/routes/sponsors.md`.)
4. **🔴 עברית+אנגלית מעורבבים** (גם במחרוזת/שורה אחת): עברית = FbEzmel (`var(--heb)`), אנגלית = Copperplate UPPERCASE ב-`<span class="lat">` — **התאמת גודל ויזואלי** (לא אותו px). פרטים ב-`docs/conventions.md §5.2`.
   - **🔴 ערבית = Noto Sans Arabic** (OFL, `./פונטים/NotoSansArabic-{Light,Regular}.woff2`, 300/400). אוטומטי — fallback בסוף מחסניות `--heb`/`--cop` עם `unicode-range` ערבי בלבד; **בלי span, בלי לגעת ב-data**. כל גליף ערבי מנותב אליו (FbEzmel/Copperplate חסרי ערבית). שני ה-`@font-face` של Noto + ה-fallback במחסניות הם חלק מבלוק הפונטים שכל דף מעתיק. פרטים: `docs/conventions.md §3.2`.
   - **🔴 ל-FbEzmel אין גליף לטיני `x`** (יש `×`) — מחבר בין שמות = `×` (U+00D7), לא "x".
5. **לא Figma node IDs ב-CSS/HTML.** רק ב-JSONs (כ-meta) וב-docs.
6. **לא לשנות slugs** של entities שכבר קיימים.
7. **לא לעגל pixel values** מהפיגמה. (כיול אופטי מכוון של Copperplate — ה-Copperplate שלנו רחב ~28% מזה שבפיגמה, ולכן למשל 80px בפיגמה ≈ 64px בקוד — **נמדד מול רינדור ה-node**, לא לפי גורם קבוע; ערכים מכוילים מתועדים ב-route docs.)
8. **לא לדרוס תמונות קיימות** — `portrait-v2.webp` אם הצילום שונה. (מקור גולמי ב-`_originals/`, gitignored; ב-`images/` רק WebP+AVIF.) תמונות שהוחלפו נשארות בדיסק.
9. **Re-Read לפני edit** של קובץ shared (`index.html`, `data/*.json`, `CLAUDE.md`, `docs/routes/*`).
10. **🔴 כל אזכור של אומן חייב להיות קישור** לדף האומן (`artists/<slug>/`). פרטים ב-`docs/artist-linking.md` — **קרא לפני סיום משימה**.
10א. **🔎 חיפוש האתר מתעדכן לבד:** כפתור הזכוכית בהידר (`components/site-chrome.js` → `wireSearch`) טוען את `search-index.js`, שנבנה מה-`<title>`, ה-`meta description` וה-JSON-LD (`name`/`alternateName`/`creator`) של **כל `index.html` שב-git**; הסיווג לפי תיקיית-העל (`artists`→דף אומן, `works`→יצירה, `events`→אירוע, `press`→כתבה…; תיקייה לא מוכרת → "עמוד"). ה-hook `.githooks/pre-commit` מריץ `python3 tools/search/build_index.py` ומוסיף את הקובץ לכל קומיט — **אין צורך בפעולה ידנית**, רק לתת לדף `<title>`/description טובים. דפים עם `noindex` ו-`_staging/` לא נכללים. מכונה/clone חדשים: `git config core.hooksPath .githooks`. קומיט עם `--no-verify` מדלג — אז להריץ ידנית.
11. **לא לבנות קומפוננטה שכבר קיימת** (lightbox, gallery, carousel). `docs/components.md` הוא ה-source of truth.
12. **🔴 Perf checklist לכל `<img>`:**
    - `src="...webp"` (לא `.png`. `picture-upgrade.js` מוסיף source ל-AVIF אוטומטית.)
    - `width="N" height="N"` (מהפיקסלים האמיתיים, מונע CLS).
    - `loading="lazy" decoding="async"` — חוץ מה-img הראשון בדף.
    - ה-img הראשון בדף = ה-LCP, מקבל `fetchpriority="high"` במקום `loading="lazy"`.
    - **עיבוד מקור:** `magick src -auto-orient -colorspace sRGB -resize '1600x1600>' -strip -quality 85 out.webp` — `-auto-orient` (סיבוב EXIF של צילומי טלפון) והמרה ל-sRGB **לפני** `-strip` (מקורות Display P3); **גאומטריה עם `>` תמיד בגרשיים** (בלי — zsh מפנה לקובץ בשם `-strip`, מדלג על ה-strip ומגדיל). בלי upscale.
    - **תמונה ≥80KB וגם ≥800px רוחב → חובה srcset:** צור וריאנטים `<name>-{480,768,1080}w.webp+avif` (וריאנט קיים כשרוחבו ≤90% מרוחב המקור — למשל `-1080w` לכל master ≥1200: `magick src.webp -resize 480x -strip -quality 85 out.webp`, avif עם `-quality 60`), והוסף `srcset="...-480w.webp 480w, ..., <name>.webp <naturalW>w" sizes="100vw"`. `picture-upgrade.js` ממפה את ה-srcset ל-AVIF אוטומטית — חובה ש**כל** וריאנט webp יהיה לו אח avif.
    - **🔴 `picture-upgrade.js` מדלג על `<img>` שכבר בתוך `<picture>`** — ב-`<picture>` ידני (למשל `source media` לקרופ מובייל) כל webp חייב אח avif **ידני**. והוא עוטף `<img>` ב-`<picture>` בזמן ריצה — סלקטור `.x>img` מפסיק להתאים (פתרון: `.x>picture{display:contents}`).
13. **כן** לעדכן את הקובץ הזה כש-state רוחבי משתנה (golden rules, contracts, מבנה) — ופרטי-דף ב-route doc (§7.2).
14. **🔴 git commit אחרי כל מצב-עבודה תקין** — **רק של הקבצים שלך** (`git add <paths> && git commit`), **לא `git add -A`**: סשנים מקבילים עובדים על אותו working tree, ו-`-A` מקמט עבודה חצי-גמורה שלהם. **"הקבצים שלך" כוללים כל מה ש-`sync_data.py` כתב** (הוא מדפיס את הרשימה המלאה — למשל `works/index.html`, עמודי `works/<id>/` של אחיות, דף הגלריה, `data/generated/*`) ואת `search-index.js` מה-hook: קומיט בלעדיהם = אתר מיושן בפרודקשן ו-`--check` נכשל על HEAD. אסור לעבוד שעות בלי commit. **הנתונים** (`data/*.json`) הם מקור-האמת; **ה-renderer/CSS בתבנית** (`artists/<slug>/index.html`) הם קוד שאפשר לאבד ב-rebuild שגוי (קרה: כל לוגיקת ה-`buildExGroups` נמחקה כי תבנית-מקור ישנה דרסה את zohar). לפני כל rebuild גורף של דפי אומנים — commit + harness (§7.1); לשחזר תבנית מ-git (HEAD), לא מקובץ-אחר-שאולי-נסוג. **push = פרסום לפרודקשן** — רק כשהמשתמש מבקש.
15. **🔴 כל דף/פוסט חדש נכנס ל-`sitemap.xml` — באותו קומיט.** אירוע, כתבה, דף אומן, עמוד יצירה, תערוכה, גלריה, ספונסר, עמוד אינדקס — **כולם**. דף שלא ב-sitemap פשוט לא מתגלה בגוגל. הכלל חל גם על:
    - **חשיפת דף מ-`_staging/`** — לא רק `mv`: להוסיף ל-sitemap **וגם** לתקן `canonical`/`og:url`/JSON-LD שעדיין מצביעים ל-`_staging` (קרה, ראה `docs/lessons.md` 2026-07-26).
    - **מחיקת/הסרת דף** — למחוק את רשומת ה-`<url>` שלו, אחרת נשארת כתובת מתה ב-sitemap.
    - **הרצה בסיום:** `python3 tools/seo/refresh_sitemap_lastmod.py` (אידמפוטנטי) — ממלא `lastmod` מתאריך הקומיט האחרון של כל עמוד, ומדפיס אזהרה לכל `<loc>` שאין לו קובץ.
    - **🔴 OG/מטא — ידני, לא `og_gen.py`/`inject.py` גורפות:** `og_gen.py` שבור (תלוי ב-`/tmp/seo_inject.py` שלא קיים) ו-`inject.py` גורף מרגרס ~90 דפים (קרה פעמיים: 2026-07-26, 2026-08-23). שני הכלים מסרבים לרוץ גורפות. המתכון: לאפות `og/<family>-<slug>-hero.jpg` ידנית + להעתיק בלוק `SEO:auto` מדף-אח ולערוך (כולל `startDate`/`endDate` אמיתיים). פרטים: `docs/todo.md`.
    - **בדיקת שלמות (שנייה אחת):** מספר הרשומות ב-sitemap חייב להשתוות למספר עמודי ה-`index.html` המוגשים — `find . -name index.html -not -path "./node_modules/*" -not -path "./_staging/*" -not -path "./trash/*" -not -path "./scratchpad/*" | wc -l` מול `grep -c "<loc>" sitemap.xml`.
16. **🔴 דאטה → `python3 tools/sync_data.py`.** אחרי כל שינוי ב-`data/artists|works|exhibitions|galleries.json` — להריץ, ולפני קומיט `--check`. לעולם לא לערוך את `data/generated/*` או את `#works-data`/`#artwork-data`/`#g-artworks-data`/`#fallback-galleries` ביד.
17. **🔴 שינוי רוחבי → harness רגרסיה** (§7.1) נקי לפני קומיט.

---

> *"Yes, the files are everywhere — but the system is in your head. Document it."*
