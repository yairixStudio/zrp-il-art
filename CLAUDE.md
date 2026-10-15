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
10. **כל אנגלית באתר = Copperplate UPPERCASE** (כלל-זהב 3, `docs/conventions.md §5`).
11. **עברית+אנגלית באותה שורה/מחרוזת:** FbEzmel לעברית, `<span class="lat">` + Copperplate ל-Latin — **גודל ויזואלי** (em optical), לא אותו px (כלל-זהב 4, `docs/conventions.md §5.2`).
12. **כל אזכור אומן = קישור** (`docs/artist-linking.md`). הפרה = הדף לא מוכן.
13. **🔴 כל דף/פוסט חדש = רשומה ב-`sitemap.xml`, באותו קומיט** (כלל-זהב 15).
14. **בדיקה ויזואלית/טיפוגרפית — רק דרך http.** ב-file:// כרום **חוסם את ה-`@font-face`** (CORS) — אל תשפוט טיפוגרפיה משם. **שרת:** ה-preview לא מריץ שרת מתוך iCloud (`getcwd: Operation not permitted`), ולכן `.claude/launch.json` (`"Site"`) רק **מתחבר** ל-`localhost:3000`. אם `curl -s -o /dev/null localhost:3000` נכשל — Bash ברקע (`run_in_background`): `python3 -m http.server 3000 --bind 127.0.0.1` משורש הריפו, ואז `preview_start {name:"Site"}`. פורט 3000 תפוס בשרת של המשתמש = מצוין, להתחבר אליו.
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
| **סיים דף/פוסט חדש** — sitemap, canonical, OG, JSON-LD | [`docs/seo.md`](./docs/seo.md) — **חובה (כלל-זהב 15)** |
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

**MCP:** הערוץ הראשי = **ה-MCP הרשמי של Figma** (`get_metadata` / `get_design_context` / `get_screenshot` / `download_assets`); לפני `get_design_context` — לטעון את הסקיל `figma:figma-design-to-code`. `get_screenshot` של ה-node = המקור להשוואה ויזואלית ולספירת פריטים. **"needs you to sign in again"** ⇒ לעצור ולבקש מהמשתמש להתחבר מחדש (`/mcp` או הגדרות הקונקטורים ב-claude.ai) — לא לעבור בשקט לכלי אחר. Framelink (`get_figma_data`) — **לא בשימוש** (תוכנית הסטודנט מחזירה 429). TalkToFigma — רק לכתיבה לתוך פיגמה, ורק כשהמשתמש מבקש. `fileKey` הוא parameter — אסור hardcode. (לקחי `get_figma_data` הישנים ב-`docs/lessons.md` — שכבות מוסתרות, סדר fills — תקפים גם בכלים החדשים.)

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
| `/sponsors/soos/`, `/sponsors/sumii/`, `/sponsors/ma-ren/`, `/sponsors/roni-liani/`, `/sponsors/elodie-k/`, `/sponsors/ever-after/`, `/sponsors/desert-queen/` | `sponsors/<slug>/index.html` | ✅ (sumii מארח גם את סקשני הרזידנסי של מלאני הקימוגלו; ma-ren = קולאב WINDOW TAKE OVER; roni-liani + elodie-k + ever-after + desert-queen = HOSTING DESIGNERS POP UP — כולם כיכר המדינה) | sponsors |
| `/contact/`, `/accessibility/`, `/privacy/` | `<dir>/index.html` | ✅ סטטיים (טופס / הצהרה / מדיניות) | — |
| `404.html` | `404.html` | ✅ (`noindex`) | — |

**סטטי (shell):** brand, nav, footer, newsletter copy, copyright, palette + typography — ב-`data/site.json` או CSS; nav/footer מרונדרים ע"י `components/site-chrome.js` (`<site-header>`/`<site-footer>`).
**דינמי (JSON):** galleries, artists, exhibitions, events, press, opencalls, works, instagram, homepage curation, announcement, curators, sponsors.

**📬 טופס ניוזלטר (פוטר + פופאפ) = Wix Velo (`POST https://zrp.co.il/_functions/subscribe`), לא Firebase — אל תחזיר Firebase.** ה-backend (מקור ב-`newsletter-backend/wix-velo/`, לייבל, סוד ה-API): `docs/components.md §6.1`. **גילוי פרטיות:** ההרשמה מצרפת גם לרשימת התפוצה של אתר הבשמים (zrp.co.il) — מצוין ב-`privacy/index.html` ובטקסט ההסכמה.

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
├── {exhibitions,opencalls,press,events,curators,galleries,sponsors}/<slug>/index.html
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
│   ├── qa/sweep.mjs           # width sweep 300–1600: sideways overflow / clipped text / overlapping lines (rule 19)
│   ├── search/build_index.py  # search-index.js — run automatically by .githooks/pre-commit (rule 10א)
│   └── seo/                   # refresh_sitemap_lastmod.py (safe); inject.py/og_gen.py (see rule 15)
├── פונטים/                    # Copperplate {300/400/700/900}, FbEzmel {300/400}, NotoSansArabic {300/400}, Solway
├── .nojekyll                  # Tells GitHub Pages to serve files as-is (no Jekyll processing)
├── FIGMA_LINKS.md             # All page-by-page Figma URLs
└── CLAUDE.md                  # ← you are here
```

> **URLs:** תיקייה לכל דף (`/about/`, לא `/pages/about.html`). תבניות (`exhibition`, `opencall`, `artist`) מועתקות לכל slug עם `data-slug` על `<html>` — כל דף עצמאי ב-URL נקי.

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
2. בדוק ב-§4 אם הדף כבר רשום. אם לא — הוסף אותו לשורה (או שורה קומפקטית) + סקשן ב-route doc. **🔴 חיפוש שאריות לפני יצירה:** `grep -rn -i -e '<slug>' -e '<name_en>' -e '<שם בעברית>' data/*.json index.html press/index.html events/index.html docs/todo.md` — וודא שה-ids שתיצור פנויים (למשל `event-<slug>-talk` ב-`press.json`). כרטיס `--soon`/`soon:true`, רשומה עם `route:null` או id קיים ⇒ **לשאול את המשתמש** אם זו אותה ישות; אותה ⇒ לקדם את הקיים (אותו id, להסיר את ה-soon), אחרת ⇒ id חדש וייחודי. (דוגמה פתוחה: tal-nehoray — `docs/routes/press.md`.)
3. קבל URLs מ-`FIGMA_LINKS.md` (או הוסף אם חסרים).
4. קרא את שני ה-frames (desktop + mobile) ב-MCP הרשמי (§3): `get_metadata` (מבנה + רוחב לזיהוי desktop/mobile) → `get_design_context` → `get_screenshot`. frames כבדים — subagent לכל frame, שמחזיר blueprint מובנה: sections (top→bottom), כל הטקסטים verbatim (כולל עברית), צבעים, נכסים, layout (gap/padding/justify/align), **ומספר הפריטים בכל רשימה/גריד/קרוסלה** (כלל-זהב 20). אל תסכם.
5. אסוף נכסים **ייחודיים**. **`ls images/<category>/<slug>/` קודם.** הורד ב-batches מקבילים.
6. **לפני HTML — עדכן JSONs.** קרא את סעיף החוזה ב-`docs/data-contracts.md`, ו**העתק רשומת-אחות מאותו קובץ/תערוכה וערוך אותה — לא לבנות רשומה מרשימת שדות** (צורות שגויות שוברות רנדררים בשקט: `img` ולא `image`, `statement_he` = מערך פסקאות). ואז `python3 tools/sync_data.py`.
7. בנה HTML יחיד עם CSS מוטמע. Pattern: `font-face → tokens → sections → media queries → casing block (conventions.md §5)`. בדרך כלל: העתק דף-אח מאותה משפחה (ה-route doc אומר מאיזה).
8. הוסף לינק לדף ב-nav אם צריך (nav/footer גלובליים ב-`components/site-chrome.js`).
9. **לפני סיום:** `docs/artist-linking.md §7` (בדיקת anchors), `text-transform`/font compliance (`conventions.md §5`), **חיתוך כותרות מלמעלה** (Copperplate caps ב-`line-height ≤1.2`; **אסור `overflow-x` על `body`** — רק על `html` — `lessons.md` 2026-06-16/06-15), perf checklist (כלל-זהב 12), ובדיקה ויזואלית דרך http, לא file:// (TL;DR 14) — ואז כללי-זהב 19–20.
10. **🔴 הוסף את הדף ל-`sitemap.xml`** + `python3 tools/seo/refresh_sitemap_lastmod.py`; תמונת OG + בלוק `SEO:auto` ידניים (**לא** `og_gen.py`/`inject.py` גורפות) — כלל-זהב 15, המתכון ב-`docs/seo.md`.
11. `python3 tools/sync_data.py --check` → exit 0.
12. עדכן docs לפי TL;DR 18, וקומיט של הקבצים שלך בלבד — `git status --short` ולהוסיף **בשמם** גם את כל מה ש-`sync_data.py` ו-hook ה-pre-commit כתבו (כלל-זהב 14).

### 7.1 Harness רגרסיה — לכל שינוי רוחבי

```bash
node tools/regress/snapshot.mjs --label before            # לפני השינוי (אפשר --only artists/,events/ ; --widths 390,1024,1366,1440)
# … השינוי …
node tools/regress/snapshot.mjs --label after
node tools/regress/diff.mjs before after                  # exit 0 = זהה
```
משווה לכל דף (ברירת מחדל 390 + 1440, http + file://): DOM אחרי JS, computed style (כולל ::before/::after), תיבות, גלילה, שגיאות קונסול ובקשות שנכשלו; תאריך/random מוקפאים, בקשות חיצוניות חסומות, דף חדש שעוד לא בקומיט נכלל. **חובה** לפני קומיט של: הפצת תבנית לדפים רבים, שינוי ב-`components/*`, CSS/JS משותף, צנרת דאטה.
- **אותם `--only`/`--widths` בשתי הריצות** (דף שקיים רק באחת = הבדל).
- שינוי **מכוון** → diff יוצא 1 — קרא אותו וודא שרק הדפים/האלמנטים המכוונים השתנו.
- עבודת layout/טיפוגרפיה: הוסף רוחבי ביניים (`--widths 390,1024,1366,1440`) — באגים של משפחות יושבים ב-769–1100 / 1320–1439.
- הפלט ב-`$REGRESS_OUT` (ברירת מחדל: תיקיית tmp של המערכת, `zrp-regress/<label>`) — לא בתוך הריפו.

### 7.2 משמעת תיעוד — כדי שה-spine לא יתנפח שוב 🔴

- **route doc = מצב נוכחי, לא יומן.** כשמשהו משתנה — **ערוך את הבולט הקיים** כך שיתאר את המצב החדש. אל תוסיף פסקת "🔴 2026-xx-xx — …" מעל המצב הישן. היסטוריה = הודעת הקומיט (`git log`).
- **מה חייב להישאר ב-route doc:** הכרעות משתמש, "אל תתקן / verbatim", סטיות מכוונות מהפיגמה, "נמחק — אל תשחזר", מה לסנכרן, gotchas, nodes של פיגמה, ערכי כיול.
- **ה-spine (הקובץ הזה) לא מקבל פרטי-דף.** שורת §4 = שורה אחת. כל השאר → route doc. יעד: ≤ ~30KB.
- **🔴 תקרת גודל: route doc ≤ ~40KB, `lessons.md` ≤ ~40KB.** סוכן חייב לקרוא את ה-route doc לפני כל עריכה, ולכן כל KB מיותר נשרף בכל משימה. מסמך שעבר את התקרה — בעדכון הבא שלו לכווץ: פרטי דף שלא השתנו חודשים → משפט אחד; לקח מ-`lessons.md` שהפך לכלל → לשורה אחת ב-route doc / כאן, ולמחוק את הסיפור (היסטוריה = `git log`). בדיקה: `wc -c docs/routes/*.md docs/lessons.md`.

---

## 8. כללי-זהב (אסור לשבור) 🔴

1. **לא משכפלים תוכן** מ-JSON ל-HTML. שדה חסר → תוסיף ל-JSON. (עותקים נדרשים ל-file:// — רק דרך `tools/sync_data.py` או ברשימת העותקים הידניים, §6.1.)
2. **לא Google Fonts** כתחליף לפונטים מקומיים. **גם לא Inter/sans-serif כברירת מחדל** — אם צריך גופן ללא-Copperplate, להוריד מקומית.
3. **🔴 כל אנגלית = Copperplate UPPERCASE** — כולל אימיילים, handles, URLs, שמות אומנים, caption. הפרה = bug. פרטים ב-`docs/conventions.md §5`. (חריגות מוכרעות ומתועדות בלבד — למשל מותגי soos ב-`.brand`, ראה `docs/routes/sponsors.md`.)
4. **🔴 עברית+אנגלית מעורבבים** (גם במחרוזת/שורה אחת): עברית = FbEzmel (`var(--heb)`), אנגלית = Copperplate UPPERCASE ב-`<span class="lat">` — **התאמת גודל ויזואלי** (לא אותו px). פרטים ב-`docs/conventions.md §5.2`.
   - **🔴 ערבית = Noto Sans Arabic** (300/400) — אוטומטי: fallback בסוף מחסניות `--heb`/`--cop` עם `unicode-range` ערבי בלבד; **בלי span, בלי לגעת ב-data**. שני ה-`@font-face` שלו + ה-fallback הם חלק מבלוק הפונטים שכל דף מעתיק. פרטים: `docs/conventions.md §3.2`.
   - **🔴 ל-FbEzmel אין גליף לטיני `x`** (יש `×`) — מחבר בין שמות = `×` (U+00D7), לא "x".
5. **לא Figma node IDs ב-CSS/HTML.** רק ב-JSONs (כ-meta) וב-docs.
6. **לא לשנות slugs** של entities שכבר קיימים.
7. **לא לעגל pixel values** מהפיגמה. (כיול אופטי מכוון של Copperplate — ה-Copperplate שלנו רחב ~28% מזה שבפיגמה, ולכן למשל 80px בפיגמה ≈ 64px בקוד — **נמדד מול רינדור ה-node**, לא לפי גורם קבוע; ערכים מכוילים מתועדים ב-route docs.)
8. **לא לדרוס תמונות קיימות** — `portrait-v2.webp` אם הצילום שונה. (מקור גולמי ב-`_originals/`, gitignored; ב-`images/` רק WebP+AVIF.) תמונות שהוחלפו נשארות בדיסק.
9. **Re-Read לפני edit** של קובץ shared (`index.html`, `data/*.json`, `CLAUDE.md`, `docs/routes/*`).
10. **🔴 כל אזכור של אומן חייב להיות קישור** לדף האומן (`artists/<slug>/`). פרטים ב-`docs/artist-linking.md` — **קרא לפני סיום משימה**.
10א. **🔎 חיפוש האתר מתעדכן לבד:** `search-index.js` (כפתור הזכוכית, `site-chrome.js` → `wireSearch`) נבנה מה-`<title>`/description/JSON-LD של כל `index.html` שב-git ומסווג לפי תיקיית-העל, ע"י ה-hook `.githooks/pre-commit` — **אין צורך בפעולה ידנית**, רק `<title>`/description טובים. `noindex` ו-`_staging/` לא נכללים. clone חדש: `git config core.hooksPath .githooks`; קומיט עם `--no-verify` מדלג — אז `python3 tools/search/build_index.py` ידנית. פרטים: `docs/data-contracts.md` (`search-index.js`).
11. **לא לבנות קומפוננטה שכבר קיימת** (lightbox, gallery, carousel). `docs/components.md` הוא ה-source of truth.
12. **🔴 Perf checklist לכל `<img>`:** `src="...webp"` (לא `.png`; `picture-upgrade.js` מוסיף AVIF), `width`/`height` מהפיקסלים האמיתיים (CLS), `loading="lazy" decoding="async"` — חוץ מה-img הראשון (ה-LCP) שמקבל `fetchpriority="high"`. **תמונה ≥80KB וגם ≥800px רוחב → חובה srcset**, ולכל וריאנט webp אח avif (ב-`<picture>` ידני — avif ידני). עיבוד מקור (`-auto-orient`, sRGB לפני `-strip`, `'…>'` בגרשיים), מתכון ה-srcset וה-gotchas של `picture-upgrade.js`: `docs/conventions.md §1.1`.
13. **כן** לעדכן את הקובץ הזה כש-state רוחבי משתנה (golden rules, contracts, מבנה) — ופרטי-דף ב-route doc (§7.2).
14. **🔴 git commit אחרי כל מצב-עבודה תקין** — **רק של הקבצים שלך** (`git add <paths> && git commit`), **לא `git add -A`** (סשנים מקבילים — `-A` מקמט עבודה חצי-גמורה שלהם). **"הקבצים שלך" כוללים כל מה ש-`sync_data.py` כתב** (הוא מדפיס את הרשימה — `works/index.html`, עמודי `works/<id>/` של אחיות, דף הגלריה, `data/generated/*`) ואת `search-index.js` מה-hook; בלעדיהם — אתר מיושן בפרודקשן ו-`--check` נכשל על HEAD. אסור לעבוד שעות בלי commit. **הנתונים** (`data/*.json`) הם מקור-האמת; **ה-renderer/CSS בתבנית** (`artists/<slug>/index.html`) הם קוד שאפשר לאבד ב-rebuild שגוי — לפני rebuild גורף של דפי אומנים: commit + harness (§7.1), ותבנית משוחזרת רק מ-git (HEAD). **push = פרסום לפרודקשן** — רק כשהמשתמש מבקש.
15. **🔴 כל דף/פוסט חדש נכנס ל-`sitemap.xml` — באותו קומיט.** אירוע, כתבה, דף אומן, עמוד יצירה, תערוכה, גלריה, ספונסר, עמוד אינדקס — **כולם**. דף שלא ב-sitemap פשוט לא מתגלה בגוגל. חל גם על **חשיפת דף מ-`_staging/`** (+ תיקון `canonical`/`og:url`/JSON-LD שעדיין מצביעים ל-`_staging`) ועל **מחיקת דף** (להסיר את ה-`<url>`). בסיום: `python3 tools/seo/refresh_sitemap_lastmod.py` (אידמפוטנטי) + בדיקת השלמות (מספר `<loc>` = מספר עמודי `index.html` המוגשים). **🔴 OG/מטא — ידני:** לאפות `og/<family>-<slug>-hero.jpg` + להעתיק בלוק `SEO:auto` מדף-אח ולערוך (כולל `startDate`/`endDate` אמיתיים); **אסור `og_gen.py`/`inject.py` גורפות** (שבורים; מרגרסים ~90 דפים). המתכון והפקודות: `docs/seo.md`.
16. **🔴 דאטה → `python3 tools/sync_data.py`.** אחרי כל שינוי ב-`data/artists|works|exhibitions|galleries.json` — להריץ, ולפני קומיט `--check`. לעולם לא לערוך את `data/generated/*` או את `#works-data`/`#artwork-data`/`#g-artworks-data`/`#fallback-galleries` ביד.
17. **🔴 שינוי רוחבי → harness רגרסיה** (§7.1) נקי לפני קומיט.
18. **🔴 לא כותבים מלל.** כל טקסט, תגית, כותרת משנה או סקשן בדף חייבים להגיע מהפיגמה, מה-JSON או מהודעת המשתמש. מה שלא מופיע באף אחד מהם נמחק, או שואלים עליו. בלי שינויי פונט, גודל או סדר שלא התבקשו. (חזר ב-47 סשנים; "אתה לא איש תוכן".)
19. **🔴 לפני "סיימתי": השוואה לפיגמה בשני הגדלים.** צילום מסך של הדף ב-1440 וב-390 (דרך http, TL;DR 14), מול שני ה-frames. אחר כך דוח קצר: מה זהה, ומה שונה ולמה. סטייה מכוונת נרשמת ב-route doc. מבנה הדוח: הסקיל `verify-done`. **ואז `node tools/qa/sweep.mjs`** (בלי ארגומנטים = כל הדפים ששונו) — עובר על 22 רוחבים 300–1600 ומדווח גלישה הצידה, חיתוך בשולי המסך, טקסט חתוך ושורות שעולות זו על זו. exit 1 ⇒ לתקן או לנמק בדוח.
20. **🔴 ספירה לפני "סיימתי".** כל רשימה בפיגמה (יצירות של אומן, תמונות בגלריה/קרוסלה, כרטיסים, כפתורים, שמות) — לספור בפיגמה ובדף ולהציג בדוח: "פיגמה 5 / דף 5". אומן חדש עם יצירות בפיגמה = גם רשומות ב-`works.json` ועמודי `works/<id>/`, לא רק דף אומן. (חזר: "למה לא הכנסת את כל התמונות של מריה", "איפה היצירות שלו? יש לו 5".)
21. **🔴 הכרעת מעצבת/משתמש נרשמת מיד.** הודעה שמועברת מהמעצבת ("בינתיים בלי דף אומן ל-2 הנשים", "בלי תמונה") — לכתוב אותה **מיד** כבולט ב-route doc של המשפחה (סעיף הכרעות), לפני שממשיכים, ולבדוק את הסעיף לפני כל צעד בהמשך הסשן. הוראה שנאמרה פעם אחת לא נשכחת עד סוף הסשן.
22. **🔴 כיוון השינוי — לחזור עליו לפני ביצוע** כשהבקשה עמומה ("טיפונת רווח", "יותר קצר", "תזיז"): משפט אחד בעברית — מה משתנה, לאיזה כיוון ובכמה ("מגדיל את הרווח בין הסקשנים מ-64 ל-96") — ואז לבצע. (חזר: "התכוונתי שתרחיב, לא לקצר".)

---

> *"Yes, the files are everywhere — but the system is in your head. Document it."*
