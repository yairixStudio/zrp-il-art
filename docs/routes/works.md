# Works — route notes

> **קרא לפני עריכה של:** `works/index.html`, `works/<id>/index.html` (150 עמודים), ולפני שינוי ב-`data/works.json` (`art_works[]`, `exhibition_statements[]`).
> מצב נוכחי + כללים פעילים (2026-09-27). היסטוריה: `docs/history/CLAUDE-2026-09-27.md` §4. חוזה השדות המלא: `docs/data-contracts.md`.

## Pages
- **`/works/`** → `works/index.html` · desktop `XhGH...::542:467` (עמוד מלא; **הגריד הקנוני = `542:500`**, מ-2026-06-11) · mobile `XhGH...::542:1365` (גריד `542:1390`) · ✅
  - ⚠️ **בפיגמה סדר היצירות במובייל שונה מהדסקטופ.** לאתר data אחד ⇒ **הדסקטופ `542:500` קובע את הסדר.** בבדיקת "1:1 מול פיגמה" — לציין מול איזה frame.
  - legacy (לא לעבוד מהם): `542:499` (היה הקישור לפני המובייל החדש; היום זה עוטף-הסקשן של `542:500` בתוך `542:467` — לעבוד מ-`542:467`/`542:500`; הערות CSS עדיין מזכירות אותו ואת `489:4`), `491:928`, `489:4`, `Zn3N...::1213:2615`.
- **`/works/:id/`** → `works/<id>/index.html` × **150** (= כל `art_works[]`, כולן `page:true`) · desktop `XhGH...::674:14072` · mobile `XhGH...::674:14022` · ✅
- **`/works/livay-levi-3/`** (collab "interdependence", ליוואי לוי × הדס טובל) · desktop `XhGH...::668:13584` · mobile — · ✅ (2026-08-12)
- **Node ids בלי prefix במסמך הזה הם בקובץ `XhGH...` (landing)**; `1213:*` = `Zn3N...` (graphics) — כמו ב-`docs/routes/artists.md`.

## Shared rules

### דאטה וסנכרון
- מקור-אמת: `data/works.json` — `art_works[]` + `exhibition_statements[]` (טקסט-אומן-על-קבוצה, מפתח `(artist_slug, exhibition_title_he)` **מדויק**, `===`).
- **כל שינוי ב-JSON → `python3 tools/sync_data.py`**; בסוף משימה `--check` חייב לעבור נקי (exit 0 **ובלי שורות `!` ב-stderr** — ראה מתכון ההוספה, שלב 5). הוא מחדש כאן:
  - `works/index.html #works-data` (כל `art_works[]`).
  - `#artwork-data` בכל `works/<id>/` — הרשומה + **fallback סטייטמנט**: `statement_he` של היצירה → אחרת `exhibition_statements[(artist_slug, exhibition_title_he)]` → אחרת בלי. המפתח = `artist_slug` של הרשומה.
  - במורד הזרם: `data/generated/art-works.js`/`ex-statements.js` (דפי אומן) ו-`#g-artworks-data` בדפי הגלריות (לפי `gallery_slug`, סדר המערך, בלי `hidden`).
- 🔴 **לא לערוך ידנית JSON בתוך `#works-data`/`#artwork-data`** — נדרס. עורכים את ה-JSON ומריצים.
- 🔴 `sync_data.py` **לא** יוצר עמודים, **לא** נוגע ב-`<head>`/SEO, ב-renderer או ב-`_staging/`. שינוי טקסט שמופיע ב-head (כותרת יצירה → `<title>`/description/OG/JSON-LD של העמוד; ביו/סטייטמנט → meta/OG/twitter/JSON-LD של דף האומן, תקדים jessica-tabarovsky 2026-07-06) = עדכון ידני.
- 🔴 **עותק ידני שאינו של `sync_data.py`:** כרטיסי FIGURES ו-PRODUCTS ב-`sponsors/sumii/index.html` מעתיקים ביד מ-`works.json` את `shira-turbowicz-1..3` ו-`melani-hekimoglu-1..5` — כותרות (כולל `title_en`), נתיב תמונה, `width`/`height`, רוחבי srcset וקישור `works/<id>/` (`docs/routes/sponsors.md`). שינוי באחת הרשומות האלה = לעדכן ידנית גם שם.
- `tools/sync_works_mirrors.py` = עטיפה ל-`sync_data.py`. `tools/migrate_exhibition_statements.py` בדימוס — לא להריץ. `works.json :: works[]` (3 אריחים) = הומפייג', לא הנתיב הזה.

### סדר, תצוגה, כתיב
- **סדר המערך = סדר הגריד ב-`/works/`**; `artist_page_pos` נצרך רק בדפי האומנים (כללי ה-pos: `docs/routes/artists.md`).
- `hidden:true` מסונן **רק** בגריד `/works/` (JS `!w.hidden`) וב-`#g-artworks-data` (`sync_data.py`). 🔴 **לא מסתיר את עמוד היצירה ולא את הכרטיס בדף האומן**: `data/generated/art-works.js` כולל את הרשומה ורנדררי דפי האומן (44 עותקים) לא בודקים `hidden` — הכרטיס ממשיך לקשר (`data-artwork-page`) לעמוד היצירה, שב-`_staging` = 404. כך גם הכרטיסים הידניים ב-`sponsors/sumii/` (shira/melani).
  - הסתרה אמיתית: תיקייה ל-`_staging/works-<id>/` (gitignored ⇒ 404), הוצאה מ-sitemap, `robots:noindex`. הסתרת אומן שלם = גם דף האומן ל-`_staging` (תקדים tali-zelnik, `docs/routes/artists.md`).
  - ⚠️ ליצירה בודדת של אומן גלוי אין היום מנגנון הסתרה בדף האומן. אפשרויות (לא נוסו — טעון הכרעה לפני שימוש): להוציא את הרשומה מ-`art_works[]` לזמן ההסתרה (לשמור בצד), או להוסיף סינון `!w.hidden` לכל וריאנטי הרנדרר בדפי האומן + regress.
  - בחשיפה: `mv` חזרה, הסרת `hidden`/החזרת הרשומה, `sync_data.py`, sitemap, ולוודא ש-canonical/`og:url`/JSON-LD לא מצביעים ל-`_staging`. (כרגע אין `hidden`.)
- כתיב שמות עברית = הקנוני של `artists.json`; ב-`details_he` תמיד `ס"מ` (לא `ס״מ`).
  - 🔴 חריגים מכוונים ב-`artist_he` (לא לקצץ לשם מ-`artists.json`): `tali-zelnik-1/2` = "טלי זלניק | סטודיו פיס אוף מיין סטודיו" (בקשת האמנית 2026-07-06, `docs/routes/artists.md`); `shira-turbowicz-1..3` = "שירה טורבוביץ | sumii" (הלטינית ב-`.lat`); `livay-levi-3` = "ליוואי לוי × הדס טובל" (קרדיט ה-collab).
  - 🔴 **"טורבוביץ" — בלי גרש** (הכרעה 2026-09-27, בכל האתר; `docs/routes/sponsors.md`). חל גם על ה-head של `works/shira-turbowicz-1..3` (`<title>`, description, `og:*`, `twitter:*`) — עותקים ידניים, `sync_data.py` לא נוגע ב-head. לא להחזיר את הגרש.
  - סטיות נוספות מהקנוני בלי הכרעה → Open issues.
- איות אנגלי קנוני (Audit 2026-07-09, הכרעת משתמש): **"adi duek"**, **"zohar shitrit"**; ה-slugs נשארים `adi-duak`/`zohar-shtrit`.
- `artist_he:null` ⇒ מוצג השם הלטיני (`sami-david` "samy d.", `la-raz-porta`).

### כללי-זהב רלוונטיים
- כל טקסט מ-JSON שעשוי להכיל לטינית → `.lat`/Copperplate (`latHtml()`; בפרטים `detailsHtml()`→`.det-en`). `esc()` לבד = באג פונט. לבדוק **כל** שדה: כותרת/אמן/פרטים/גלריה/תערוכה/statement.
- כל אזכור אומן = קישור (`docs/artist-linking.md`).
- תמונות `images/works/v2/<img>.{webp,avif}`. `widths[]`: **האחרון = רוחב `<img>.webp` הראשי**, השאר `<img>-<w>w.webp` + אח avif לכל אחד. `w`/`h` = הקובץ הראשי.
  - וריאנטים **חובה** כש-≥80KB וגם ≥800px (כלל-זהב 12). מתחת לסף — רשות, אבל בפועל **כל** יצירה ברוחב ≥480 נושאת `480w` (למשל `zohar-ron-1..4` ב-690, `melani-hekimoglu-1` ב-548). ל-`livay-levi-4` (406) ול-`alice-debellis-1` (238) יש `widths:[<natural>]` רק כי הן צרות מ-480 (וריאנט 480w = הגדלה) — לא תקדים לדלג על 480w ביצירה רחבה יותר.
- לא לדרוס תמונה — צילום חדש = `<img>-v2` + עדכון `img` (תקדים `hadas-tuval-2-v2`).
  - OG: יצירה חדשה = `og/works-v2-<id>.jpg`. צילום חדש ליצירה קיימת = לאפות מחדש **את הקובץ שה-head כבר מפנה אליו** + לעדכן מידות. שני המקרים הקיימים שונים: `hadas-tuval-2` → לפי id (`og/works-v2-hadas-tuval-2.jpg`, נאפה מחדש 998×1330); `zohar-ron-dan-ben-ari-1` → לפי img (`og/works-v2-zohar-ron-dan-ben-ari-1-v2.jpg`).
- `images/works/v2/*` ממוחזרות מחוץ ל-`works/`/`artists/` — `grep -r` לפני שינוי שם/תוכן:
  - `press/the-shared-list/`: `zohar-ron-5`, `nir-giorgio-levin-8`, `elsa-ars-brush-1` + `og/works-v2-zohar-ron-5.jpg`.
  - כרטיס הכתבה ב-`index.html #press`, ב-`press/index.html` וב-`data/press.json`: `zohar-ron-5`.
  - `exhibitions/the-peeler/` (רצועת האומנים): `alice-debellis-2`, `amnon-lipkin-13`, `elsa-ars-brush-1`, `maria-artamonova-1`, `michael-konovalenko-1`, `noemi-safir-2`.
  - `sponsors/sumii/`: `shira-turbowicz-1..3`, `melani-hekimoglu-1..5`; ב-`data/sponsors.json` — `cover_image` = `melani-hekimoglu-4`.
  - קרוסלות הגלריות (`#g-artworks-data`); `tools/seo/og-dims.json`.

### קישורים נכנסים (לכן לא משנים id — כלל-זהב 6)
- גריד `/works/`; כל 44 דפי האומנים (לייטבוקס עם `data-artwork-page` ⇒ קליק על התמונה / "לעמוד היצירה"); שקופית המרכז בקרוסלת `galleries/<slug>/`; `sponsors/sumii/` (FIGURES → `shira-turbowicz-1..3`; PRODUCTS → melani: plates=4, vases=1, dessert-bowl=2, lamp=5, planter=3); `press/peeling-a-layer/` → `jessica-tabarovsky-1`.

### בדיקה
- שינוי renderer/CSS בהרבה עמודים = חובה:
  1. `node tools/regress/snapshot.mjs --label before --only works/`
  2. השינוי
  3. `node tools/regress/snapshot.mjs --label after --only works/`
  4. `node tools/regress/diff.mjs before after` (exit 0 = זהה)
  - `--only`/`--widths` הם דגלים של `snapshot.mjs`, לא של `diff.mjs` — **אותם ערכים בשתי הריצות** (דף או רוחב שקיים רק בצילום אחד נספר כהבדל). ברירת המחדל 390,1440; לעבודת layout/טיפוגרפיה `--widths 390,1024,1366,1440`.
  - שינוי שנועד לשנות פלט (למשל הפצת `linkNames()`) יוצא ב-exit 1 — לקרוא את ה-diff ולוודא שהשתנו רק העמודים/האלמנטים המכוונים. דף חדש נכלל בצילום גם לפני `git add` (כל `*.html` שאינו ב-`.gitignore`), ולכן עמוד יצירה חדש יופיע כ-`only in after` — צפוי.
- טיפוגרפיה בודקים **רק ב-http** (`python3 -m http.server`); ב-file:// כרום חוסם `@font-face`.

## `/works/` — הגריד
- hero אפור `#EEF0EF`: `THE ART` (Bold) / `works` (Light), 80px (60 ≤1100, מובייל ממורכז `clamp`).
- **3 עמודות דסקטופ / 2 מובייל** (גם ≤390), `column-gap:16` (12 ב-≤390), `row-gap:64/48/40`.
- כרטיס: תמונה `aspect-ratio:33/40` `contain` על `#FAFAFA` → אומן (→ דף האומן; קרדיט מעורב כמו `"שירה טורבוביץ | sumii"` נעטף `.lat`) → כותרת (`is-he`/`is-en`/`is-bi` עם קו מפריד) → `details_he` (`white-space:pre-line`; מידות ב-`.dim` LTR) → "נמכר" אם `sold` → `gallery_en` בשתי שורות → `../#galleries`.
- קליק על התמונה: `page:true` ⇒ `<a href="<id>/">`. לייטבוקס כ-fallback לרשומה בלי `page` (אותה קומפוננטה, scope יחיד לכל כרטיס — `data-artwork-gallery` על כל `<article>`, בלי prev/next) — **בגריד הזה בלבד**: דפי האומן (`data-artwork-page`) ושקופית המרכז בקרוסלות `galleries/<slug>/` מקשרים ל-`works/<id>/` **תמיד**, בלי לבדוק `page` (ולכן `page:false` לא מונע קישור שבור — ראה מתכון ההוספה).
- **טעינה מדורגת:** 12 ואז צ'אנקים של 18, IntersectionObserver על sentinel (`rootMargin:'1800px 0px'`). כל צ'אנק (`appendChunk`) מריץ מיד אחרי ההזרקה `ArtworkLightbox.refreshFocusable()` + `PictureUpgrade.refresh(grid)`; ואז 🔴 re-arm (`unobserve`+`observe`) של ה-sentinel — אחרת נתקע. בלי IO ⇒ רינדור מלא. כרטיס ראשון `fetchpriority="high"`.

### סדר הגריד (150 פריטים)
- 1–70 ו-79–122 = סדר `542:500` ברצף אחד, בלי היסט בראש (אימות מלא אחרון 2026-06-11 — מיקום+תמונה+טקסט גלוי; הוספות מאוחרות כמו `aharon-bas-1` בראש, `bar-cohen-1`, `talia-zoref-2/3`, `elsa-ars-brush-6` שובצו בתוכו — ⚠️ unverified מול הפריים הנוכחי).
- 🔴 **71–78 = בלוק הרזידנסי** (`shira-turbowicz-1..3`, ואז `melani-hekimoglu-1..5`) — הכרעת המעצבת 2026-08-23 "לשים באמצע… שלא תהיה ראשונה". **לא להחזיר לראש.**
- 123–150 = יצירות שאינן ב-`542:500`, בסוף לפי סדר הוספה (the-peeler ×17, noemi-safir-11/12, amnon-lipkin-12/13, tali-zelnik, jessica-tabarovsky-2, hadas-tuval, livay-levi-3, **livay-levi-4 = 150**). **יצירה חדשה שלא בפריים ⇒ לסוף.**
- סדר ויזואלי של `542:500`: היום ה-API מחזיר אותו כ-`mode:grid` (3×37, `gridRow`/`gridColumn` על כל כרטיס) ⇒ למיין לפי (gridRow, gridColumn). ב-2026-06-11 הוא היה `layoutMode:none` (אבסולוטי) ⇒ מיון לפי (y, x).

### הכרעות מול הפיגמה
- **טקסט ב-data של פיגמה ≠ טקסט גלוי** (`get_figma_data` מחזיר שכבות מוסתרות בלי סימון) ⇒ לרנדר את ה-node לפני שמייחסים meta. מוסתר ולכן **לא** נשאב: בולרפלייט "60x80 שמן על קנבס" על 26 כרטיסים אחוריים, "התנערות" על `holy-kadosh-3`, הפרטים של `zohar-shtrit-1`. **גלוי ונשמר:** "קרמיקה" ב-`tal-nehoray-1..5`.
- אימות סדר = **ברמת תמונה**, לא רק טקסט (המעצבת החליפה תמונות בין כרטיסים חסרי-כותרת: tal-nehoray, gal-polk, adi-duak, la-raz-porta).
- כפילויות תמונה בפיגמה — **לא שוכפלו**: jessica=anat-4, noemi-4=risa, noemi-6=alon-1, NGL-2≈alon-1, tanya crop2/aura1=aura2, sami 64=66.
- `sold` רק לפי תג גלוי (2026-06-11 נוספו: anat-wegier-4, alon-2, nir-giorgio-levin-2, la-raz-porta-1, raz-ronen-1/2).

## `/works/:id/` — עמוד יצירה (תבנית)

### מבנה
- `<html data-artwork-id>` + `#artwork-data` + IIFE שמרנדר ל-`#aw-media`/`#aw-info`. 🔴 שם התיקייה = `data-artwork-id` = `id` בתוך `#artwork-data` (`sync_data.py` לא בודק — סקריפט הבדיקה במתכון ההוספה).
- דסקטופ: תמונה `contain` משמאל (`max-height:640px`), מידע 360px מימין (320 ≤1100); `.aw-info` נשאר LTR (`flex-end` = ימין), `rtl` רק על הטקסט. מובייל: עמודה; 🔴 `.aw-media{flex:0 0 auto}` (לא `flex:1 1 0` — קורס לגובה 0); כפתורים `row-reverse` + `justify-content:flex-start` = ימין.
- תמונה = LCP (`fetchpriority="high"`, `sizes="(max-width:768px) 100vw, 55vw"`), קליק ⇒ לייטבוקס `components/artwork-lightbox.{js,css}` (`[data-artwork-src]`, לא מנווט).
- **contact us** = `mailto:` לקורין אברהם (אוצרת כל התערוכות; הכתובת hard-coded ב-renderer בכל 150 העמודים, מקורה `data/opencalls.json`), נושא+גוף ממולאים (יצירה, אמן, תערוכה, פרטים, קישור). **share** = `[data-share-btn]` (`site-chrome.js`).
- מטא: כותרת אחת (`title_he`, אחרת `title_en` ב-Copperplate), אמן → `../../artists/<artist_slug>/`, פרטים, גלריה → `../../#galleries` **בשורה אחת**.
- **divider + סקשן תערוכה רק אם יש `exhibition_title_he` או `statement_he`.** הכותרת מקושרת ל-`../../<w.exhibition_route>/` (Audit 2026-07-09 — לא hardcode `opencalls/`). routes: הקולפן `exhibitions/the-peeler` (**לא** `opencalls/…`), `exhibitions/how-many`, `exhibitions/loneliness`, shira `sponsors/sumii`, melani `null`; ל-`alon-1/2` אין מפתחות `exhibition_*`.
- שדות אופציונליים שהרנדרר של עמוד היצירה קורא: `exhibition_title_he`, `exhibition_route`, `statement_he[]`, `collab[]`/`collab_connector_he`. `page` — רק הגריד `/works/`; `exhibition_slug` — רק דפי האומן (`exRank`); `art_works[].kind` — מידע בלבד, אף רנדרר לא קורא (ה-`kind:"residency"` שנקרא ב-`galleries/dizengoff/` הוא של רשומת `#g-exhibitions-data`, לא של `art_works`).

### וריאנטי renderer (5)
העמודים זהים פרט ל-data/head ולהבדלי ה-JS וה-CSS האלה. שינוי renderer/CSS = בכל הוריאנטים הרלוונטיים + regress. לזיהוי: `grep -l 'w.collab' / 'wrapDimRuns' / 'NAME_LINKS' / '.aw-artist a{' works/*/index.html`.
- **A** (114): בסיס — בלי collab, בלי `wrapDimRuns`/`.dim`, בלי כלל `.aw-artist a`.
- **Z** (2: `zohar-ron-5/9`): + `wrapDimRuns` + CSS `.dim{direction:ltr;unicode-bidi:isolate}`; בלי `.aw-artist a`.
- **B** (28 — aharon-bas-1, alice-debellis, amnon-lipkin, bar-cohen-1, hadas-tuval, maria-artamonova, michael-konovalenko, shira-turbowicz, tali-zelnik): + `wrapDimRuns`/`.dim` + ענף collab ב-`artistHtml` + CSS `.aw-artist a{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:2px}` + `:hover{opacity:.6}`. ⚠️ הסלקטור תופס רק `<a>` **מקונן** בתוך `span.aw-artist` = שמות collab בלבד. ביצירת אמן יחיד (כל 28 העמודים היום) הקרדיט הוא `<a class="aw-artist">` עצמו ⇒ **בלי** קו תחתון, זהה ל-A.
- **M** (5: `melani-hekimoglu-*`): B (כולל ה-CSS) + `exHead` ריק כשאין כותרת + `linkNames()` (`NAME_LINKS`: "ארז זילינסקי רוזן"→`../../about/`, "קורין אברהם"→`../../curators/korin-avraham/`, CSS `.aw-ex-body a.artist-link`).
- **L** (1: `livay-levi-3`): בסיס + ענף collab + CSS `.aw-artist a{transition:opacity .2s}` + `:hover{opacity:.6}` בלבד — **בלי קו תחתון** על שמות ה-collab, ובלי `wrapDimRuns`/`.dim`.
- עמוד חדש — להעתיק מוריאנט שמכסה את הצרכים: collab ⇒ וריאנט עם ענף collab (B/M/L; L בלי `.dim`); בלי כותרת ⇒ M; מידות מבודדות `.dim` ⇒ Z/B/M. העתקה מ-A מאבדת בשקט את ענף ה-collab ואת `.dim` (עיצוב קישור האמן ביצירת אמן יחיד זהה בכל הוריאנטים). ⚠️ לא הוכרע: B/M מוסיפים קו תחתון לשמות collab, ואילו עמוד ה-collab החי היחיד (`livay-levi-3`, L) מציג אותם בלי ⇒ collab חדש שמועתק מ-B ייראה שונה מ-livay-levi-3. להכריע לפני שימוש (Open issues).

### רזידנסי — יצירה בלי תערוכה (גלריית דיזינגוף)
- **עם כותרת** (shira-turbowicz, 2026-08-20): `exhibition_title_he:"POP UP ART RESIDENCY"`, `exhibition_slug:null`, `exhibition_route:"sponsors/sumii"`, `kind:"residency"`. בדף האומן קבוצה רגילה; `exRank(null)=-1` ⇒ תמיד מתחת לתערוכות.
- **בלי כותרת** (melani-hekimoglu, 2026-08-23, פריים `1634:188`): שלושת `exhibition_*` = `null` + `kind:"residency"`, ורשומת `exhibition_statements` עם `exhibition_title_he:null`. 🔴 **`null` מפורש בשני הצדדים** — מפתח חסר לא מתאים ב-`===` והסטייטמנט נעלם בשקט. בעמוד היצירה דורש וריאנט M; בדף האומן — תיקונים מקומיים (`docs/routes/artists.md`).
- ⚠️ `alon-1/2` (בלי `exhibition_*`, עם `statement_he` per-work) על וריאנט A ⇒ `<span class="aw-ex-title">` ריק (קוסמטי).

### הוספת יצירה (מתכון)
1. תמונות ל-`images/works/v2/` (כלל-זהב 12; מקור גולמי ל-`_originals/`).
2. רשומה ב-`art_works[]` במקום הנכון, `page:true`, `artist_page_pos`, שדות תערוכה; `sold`/`details_he` רק לפי מה שגלוי. סטייטמנט-קבוצה → `exhibition_statements[]` (אותה מחרוזת `exhibition_title_he` בדיוק); `statement_he` ברשומה = **טקסט על היצירה הבודדת בלבד** (באנר מעל הכרטיס בדף האומן). 🔴 רשומת `exhibition_statements` חדשה = **חמשת המפתחות** כמו כל 50 הקיימות: `artist_slug`, `exhibition_title_he`, `exhibition_slug`, `exhibition_route`, `statement_he` (`null` מותר, מפתח חסר לא). בלי `artist_slug`/`exhibition_title_he`/`statement_he` ה-`sync_data.py` קורס ב-`KeyError`.
3. להעתיק תיקיית אחות ל-`works/<id>/` ולהחליף: `data-artwork-id`, **ה-`id` בתוך `#artwork-data`** (מספיק `{"id":"<id>"}` — 🔴 sync_data מזהה לפי ה-id שבפנים; id של האחות = העמוד מציג בשקט את האחות), ו**כל ה-head**: `<title>`, description, בלוק `SEO:auto` (canonical, `og:*` + `og:image:width/height`, `twitter:*`, JSON-LD `VisualArtwork`+`BreadcrumbList`) — לקח 2026-07-09: `elsa-ars-brush-6` נשא SEO שלם של talia-zoref-1.
4. OG ידני: `magick images/works/v2/<img>.webp -resize '1200x1200>' -strip -quality 82 og/works-v2-<id>.jpg` (נכנס ב-1200×1200 ולעולם לא מגדיל — 🔴 לא `-resize 1200x` של ה-spine §7, שמגדיל יצירות צרות מ-1200 כמו `livay-levi-4`). את `og:image:width/height` ב-head למלא מ-`magick identify -format '%w %h'` של הקובץ שנוצר. 🔴 **לא להריץ `og_gen.py`/`inject.py` גורפות** (`docs/todo.md`). ⚠️ לפחות 17 מקובצי ה-OG הקיימים (הגבוהים מ-1200) נאפו ב-width-cap `-resize '1200x>'` (למשל `livay-levi-4` 406×1293, `aharon-bas-1` 596×1600). שתי הדרכים לא מגדילות; בתוך משפחה להעדיף את מה שהאחיות משתמשות בו, ובכל מקרה למלא `og:image:width/height` מה-identify.
5. `python3 tools/sync_data.py` + `--check`: 🔴 exit 0 **וגם בלי אף שורת `!` ב-stderr** — `! artwork page id not in works.json` = `id` שגוי/לא-קיים ב-`#artwork-data` (sync_data רק מדלג; `--check` עובר), ועמוד בלי בלוק `#artwork-data` מדולג **בלי שום הודעה**. לכן גם בדיקת ה-1:1 שלמטה.
6. `sitemap.xml` באותו קומיט + `python3 tools/seo/refresh_sitemap_lastmod.py` (כרגע 151 = אינדקס + 150).
   - חיפוש ההידר (`search-index.js`) נבנה מה-`<title>`/description/JSON-LD (`name`, `creator.name`) הסטטיים — ולכן head שהועתק מאחות ולא עודכן מופיע גם בחיפוש. הוא נבנה מחדש בקומיט ע"י `.githooks/pre-commit` **רק אם ה-hook מופעל** (`git config core.hooksPath .githooks`); אחרת: `git add` לעמוד, `python3 tools/search/build_index.py` (מאנדקס רק עמודים שב-git), ולכלול את `search-index.js` בקומיט. לא לערוך אותו ביד.
- 🔴 **לכל `id` ב-`art_works[]` חייבת להיות תיקייה `works/<id>/`, ולהפך.** `page` נבדק **רק** בגריד `/works/`; דפי האומנים ושקופית המרכז בקרוסלות `galleries/<slug>/` מקשרים ל-`works/<id>/` תמיד ⇒ רשומה בלי תיקייה (sync_data לא יוצר עמודים ולא מזהיר) = 404, ותיקייה שנשארה אחרי מחיקת רשומה = עמוד יתום — וכל הבדיקות עוברות. בסוף **כל** הוספה או מחיקה להריץ (נקי = השורה `no page: set() orphan: set()` בלבד; בודק גם בלוק חסר ו-`data-artwork-id` = שם התיקייה = `id` ב-`#artwork-data`):

```bash
python3 - <<'EOF'
import json,os,re
ids={w['id'] for w in json.load(open('data/works.json'))['art_works']}
d={x for x in os.listdir('works') if os.path.isdir('works/'+x)}
print('no page:',ids-d,'orphan:',d-ids)
for x in sorted(d):
    t=open('works/%s/index.html'%x).read()
    a=re.search(r'data-artwork-id="([^"]*)"',t); b=re.search(r'id="artwork-data"[^>]*>(\{.*?\})</script>',t,re.S)
    if not a or not b or a[1]!=x or json.loads(b[1]).get('id')!=x: print('mismatch/missing block:',x)
EOF
```

- `/tmp/gen_artwork_pages.py` אינו בריפו ואינו זמין — לא לחפש. **מחיקה:** JSON, תיקייה, sitemap, `grep` לקישורים נכנסים, `sync_data.py`, ובדיקת ה-1:1 שלמעלה.

## `/works/livay-levi-3/` — collab
- **המתכון המאושר ליצירה משותפת** (הכרעת פיגמה `668:13584`; השימוש החי הראשון ב-`collab[]`):
  - **רשומה אחת** (`artist_slug:"livay-levi"`) + `artist_pages:["hadas-tuval"]` + `collab[]` (שני `{slug,name_he,name_en}`) + `collab_connector_he:"×"` ⇒ בגריד **פעם אחת**, בשני דפי האומנים, עמוד קנוני אחד. **לא לשכפל לשתי רשומות** (תמונה כפולה בגריד). ⚠️ `artist_pages` לא נתמך בשלושת דפי ה-legacy (`alon`, `dan-ben-ary`, `zohar-ron-dan-ben-ari` — מסננים לפי `artist_slug` בלבד, `docs/routes/artists.md`). collab שאחד הצדדים שלו הוא דף legacy לא יופיע שם בלי שדרוג הרנדרר של אותו דף, ואחריו regress.
  - **קבוצה ייעודית** `"הקולפן | interdependence"` — הקיבוץ לפי מחרוזת מדויקת, ולכן אי אפשר להתמזג לקבוצות הקיימות של השניים.
  - **רשומת `exhibition_statements` לכל אומן.** כרגע הנוסח מפוצל: ליוואי "…בין ליוואי לוי והדס טובל.", הדס "…בין הדס טובל לליוואי לוי." (`1502:122`); עמוד היצירה מציג את נוסח ליוואי.
  - `artist_page_pos:1` חל בשני הדפים (הקבוצה המשותפת ראשונה בשניהם).
- 🔴 **`×` (U+00D7) ולא `x`** — ל-FbEzmel אין `x` לטיני, והמחבר עובר `esc()` ולא `.lat`. לפני תו לטיני בודד במחרוזת עברית — לבדוק שהגליף קיים ב-FbEzmel (`docs/lessons.md` 2026-08-12).
- `artistHtml` (עמוד + גריד) = שני שמות מקושרים, מחוברים ב-`×` (בלי `collab_connector_he` הרנדרר נופל ל-"בשיתוף"; המתכון המאושר = תמיד `"×"`).
- תמונה `images/works/v2/livay-levi-3.{webp,avif}` 1080×810 +480/768 (imageRef `4ce7697e…`), OG `og/works-v2-livay-levi-3.jpg`.
- כתיב מוכרע מול הפיגמה: "גןף"→**"גוף"**, "ותלוייה"→**"ותלויה"**.
- `title_he_by_artist`/`details_he_by_artist`: נתמכים **רק בכרטיס הגריד של 10 דפי אומן** (`_th`/`_dh` ב-`buildRichCard` — aharon-bas, alice-debellis, amnon-lipkin, bar-cohen, hadas-tuval, maria-artamonova, michael-konovalenko, melani-hekimoglu, shira-turbowicz, tali-zelnik). **חסרים ב-`artists/livay-levi/`** ⇒ ב-`livay-levi-3` הם ישפיעו רק בדף של הדס; לפני שימוש — להפיץ ל-livay-levi (+ regress). `/works/` ו-`works/<id>/` **תמיד קנוניים בכוונה** (`title_he`/`details_he`) — לא להוסיף שם תמיכה. אין היום רשומה שמשתמשת בהם.
- `artist_pages` בלי collab משמש גם את `zohar-ron-dan-ben-ari-1` (מוצגת גם בדף zohar-ron).

## רישום רשומות — מקורות פיגמה והכרעות תוכן
- **zohar-ron-5..8** ("דג 1/2/3", "בּוּרְקָה | برقع") `613:67..91`; **gal-rotem-1** "טביעה בחשיכה" `607:33`; **raz-ronen-1/2** `616:129/149`.
- **amnon-lipkin** (דף `798:173`) — כל 13 בקבוצה **"הקולפן | מעורר רגש: מאבק מייסר ומרגש"** (`798:203`/`798:214`). pos 1..11 לפי המספור, **13 "קולפן - מילים" = 12, 12 "קולפן - לב" = 13** (לב אחרונה ובודדת — המעצבת, 2026-07-15; לא ליישר). 12/13 = 36/66 ריקמה ידנית (`944:257`/`800:491`). פסקה 1 מסתיימת "…ומציפות את הקונפליקט שבין החלק המייסר במאבק לבין המרגש שבו." בביו: "בדיקנות"→**"בדייקנות"**.
- **jessica-tabarovsky** — **"הקולפן | מעורר רגש: השתוקקות"** (`668:13236`); סטייטמנט 4 פסקאות על שתי היצירות (טקסט `668:13332`, בתוך הסקשן `668:13235` שכולל גם את הכותרת `668:13236`); ביו גוף שלישי (`668:11043`, בתוך הסקשן `668:11042`). **-2** "בחורה ממתינה לרכבת של 6:48" (`1050:16`) = pos 1, **-1** "התנערות" = pos 2 (`668:13241`).
- **natasha-zeriker** — **"הקולפן | מעורר רגש: אובדן שליטה"** (ברשומה + ב-natasha-zeriker-1); סטייטמנט נוכחי = 10 פסקאות שנפתחות ב-"LINGER" (2026-08-28) — node `668:13682` (כותרת `668:13683`, טקסט `668:13708`), שהמעצבת שכתבה in-place מעל הסטייטמנט הישן.
- **hadas-tuval** (`797:106`, יצירות `797:146`) — **"הקולפן | מעורר רגש: החזקה והרפיה"** (`797:148/149`); -1 "falling into movement" 1086×1448; **-2 "סף" = `img:"hadas-tuval-2-v2"`** 998×1330 +480/768 (`797:152`, imageRef `8dfed7d2…`). ביו `797:137`, פורטרט `images/artists/hadas-tuval/`, `@hadastuval.ayni`, דף אומנית מתבנית bar-cohen. בגריד `/artists/` (פריט 42 מתוך 43, לפני tali-zelnik) — בקשת משתמש 2026-07-06 **למרות שאין לה כרטיס ב-`523:145`**; `images/artists/grid/hadas-tuval.{webp,avif}` 810²+480w מהפורטרט.
- **tali-zelnik-1/2** — **"הקולפן | מעורר הרגש: שייכות"** (`854:1082`, כך בפיגמה). מחרוזת-מפתח מול רשומת ה-`exhibition_statements` שלה — שינוי = בשני הצדדים יחד + `sync_data.py`, אחרת הסטייטמנט נעלם בשקט.
- **noemi-safir-11/12** "התמכרות רכה"/"לחץ סגול" (`943:237`/`668:12584`, דף `668:12489`) — pos 4/5 בראש How Many בדף האומן.
- **elsa-ars-brush-6** "מושעה בזמן" `833:944`. **talia-zoref-2/3** "שלווה בסגנון | Serenity in Style" / "להתחבר | Connect" (`668:13734`/`867:1138`/`870:1148`); talia-zoref-1 = pos 2.
- **הקולפן, 6 פריימי מובייל (2026-06-23):** michael-konovalenko ×3 `798:374`, maria-artamonova `798:240`, alice-debellis ×2 `849:963`, amnon-lipkin ×11 `798:173` — `medina`, סטייטמנט לכל אומן.
- **shira-turbowicz-1..3.title_en** ("Gaia"/"Sonia Delaunay"/"Niki de Saint Phalle") נוסף ב-`works.json` בשביל כיתובי FIGURES בעמוד הספונסר (עותק ידני שם).
- **livay-levi-4** (`1500:1551`, `statement_he` per-work) — `docs/routes/artists.md`.
- **zohar-ron-dan-ben-ari-1** ("sex?") + **zohar-ron-9** ("הקוסם") — בלי `exhibition_statements` לזוהר ב-How Many; `statement_he` per-work בשתיהן. כותרת הקבוצה בשתיהן = "How Many Partners Have You Had?" (נקייה) — לא "…| sex?" (אוחד 2026-06-23).

## Open issues
> רשומים ב-`docs/todo.md`: קישור שמות בסטייטמנט, BLOOM PLANTER, Sonia Delaunay. פריטים שמסומנים "נצפה בקוד" ופריט כפילויות התמונה **אינם** רשומים שם — להוסיף ל-`docs/todo.md` כשמטפלים או מכריעים.

- **שמות בתוך הסטייטמנט לא מקושרים בעמודי היצירה** (כלל-זהב 10). רק `melani-hekimoglu-*` (וריאנט M) מריצים `linkNames()`, ו-`NAME_LINKS` שם ממפה שני שמות בלבד: "ארז זילינסקי רוזן"→`../../about/`, "קורין אברהם"→`../../curators/korin-avraham/`.
  - נצפה בקוד (בסטייטמנט המוצג, כולל fallback מ-`exhibition_statements`) — ⚠️ רחב מהרשום ב-`docs/todo.md`:
    - `shira-turbowicz-1..3`: ארז, קורין
    - `livay-levi-3`: ליוואי לוי, הדס טובל
    - `gilad-kenan-1`: גלעד קינן · `natasha-zeriker-1`: נטאשה זריקר · `sami-david-2..4`: סמי די · `zohar-ron-1..4`, `zohar-ron-9`: זוהר רון
  - הפצת ה-snippet כמו-שהוא מתקנת רק את shira. צריך להרחיב את `NAME_LINKS` לשמות האומנים (או lookup מול `artists.json` → `../../artists/<slug>/`), CSS `.aw-ex-body a.artist-link`, ולהפיץ לכל 5 הוריאנטים + regress.
  - ⚠️ פתוח: רוב האזכורים הם של אומן היצירה עצמה; החריג "לא מקשר לעצמו" ב-`docs/artist-linking.md` מנוסח לדף האומן בלבד — להכריע אם חל גם כאן.
- ⚠️ נצפה בקוד — `artist_he` שסוטה מהקנוני של `artists.json` בלי הכרעה (לשאול לפני נרמול): `zohar-ron-dan-ben-ari-1` "דן בן-ארי" (קנוני "בן ארי"); `holy-kadosh-1..3` "טל קדוש" (קנוני "טל הולי קדוש"); `hila-loterstein-1..3` "הילה לוטרשטרין" (קנוני "לוטרשטיין" — נראה כטעות הקלדה).
- `melani-hekimoglu-3` (BLOOM PLANTER): `details_he` זהה ל-FLOW VASES (copy-paste של המעצבת, נשמר verbatim עד הכרעה).
- "Sonia Delaun" בפיגמה → "Sonia Delaunay" ב-`shira-turbowicz-2` (+ `docs/routes/sponsors.md`).
- כפילויות התמונה בפיגמה — לדווח למעצבת / לתקן בפיגמה (⚠️ לא רשום ב-`docs/todo.md`; מקור: `docs/lessons.md` 2026-06-10).
- ⚠️ נצפה בקוד: `tali-zelnik-1/2` עם SEO שארית-staging (OG ברירת מחדל, JSON-LD `WebPage` בלבד, אין `og/works-v2-tali-zelnik-*.jpg`); 25 עמודים בלי `og:image:width/height` ו-3 עם מידות שגויות (`noemi-safir-11/12`, `talia-zoref-1` — קובצי ה-OG שלהם גם רחבים מה-webp של היצירה; בתיקון לאפות מחדש לפי שלב 4 במתכון); ב-`tools/seo/og-dims.json` הרשומה של `hadas-tuval-2-v2` מצביעה ל-`og/works-v2-hadas-tuval-2-v2.jpg` שאינו קיים (העמוד מפנה ל-`og/works-v2-hadas-tuval-2.jpg`).
- ⚠️ נצפה בקוד: קו תחתון על שמות collab לא אחיד. שם של אמן יחיד לא מקבל קו תחתון באף מקום — הכללים `.aw-artist a` (B/M) ו-`.meta .artist a` (גריד) תופסים רק `<a>` מקונן = ענף ה-collab. ההבדל הנראה היחיד היום הוא ב-`livay-levi-3`: בכרטיס הגריד `/works/` שמות ה-collab עם קו תחתון, ובעמוד היצירה שלו (וריאנט L) בלי. יישור = הכרעת משתמש + הפצה + regress.
- ⚠️ נצפה בקוד: קישור הגלריה (גריד + 150 עמודים) עדיין `/#galleries`, לא `galleries/<slug>/` — שינוי = הכרעת משתמש + הפצה לכל הוריאנטים.
- נצפה בקוד: כותרת קבוצת loneliness ב-`works.json` (34 יצירות + 11 רשומות `exhibition_statements`) = "בדידות בסביבה תוססת" (+ סיומות), בעוד הכותרת הרשמית ב-`exhibitions.json` = "בדידות בתוך סביבה תוססת" (Audit 2026-07-09).
  - ⚠️ לא ידוע אם הפער מכוון — טעון הכרעת משתמש. מחרוזת-מפתח: אם מאחדים — כל הרשומות וכל ה-statements יחד, ואז `sync_data.py`.
  - 🔴 אם בפיגמה מופיע "בדידות בתוך בסביבה תוססת" (כפל-ב') — טעות מוכרעת, לא להעתיק ל-`exhibition_title_he`.

## Removed / do not restore
- דאטה inline בדפי אומן (`__ART_WORKS_INLINE__` בתוך HTML) — עכשיו `data/generated/*.js`.
- לייטבוקס בכרטיסי גריד עם עמוד; פיצול שם הגלריה בעמוד היצירה; `.aw-media{flex:1 1 0}` במובייל.
- `opencalls/the-peeler` כ-`exhibition_route` של היצירות, או קישור hardcoded ל-`opencalls/` ברנדרר עמוד היצירה (העמוד `opencalls/the-peeler/` עצמו חי ולא מושפע).
- shira/melani בראש הגריד (בוטל 2026-08-23).
- הכתיב "טורבוביץ׳" (עם גרש) ב-`artist_he` וב-head של `shira-turbowicz-1..3` — הוחלף ב-"טורבוביץ" (2026-09-27).
- קולאב `aharon-bas-1` × bar-cohen (פוצל 2026-06-24 לשתי יצירות עצמאיות בלי קרדיט-שיתוף: `aharon-bas-1` אהרן בלבד, `bar-cohen-1` בר בלבד עם תמונה משוכפלת) — לא לאחד.
- טקסט מוסתר מהפיגמה (60x80, "התנערות", פרטי zohar-shtrit-1).
- סטייטמנט natasha הישן (6 פסקאות, "לאורך השנים אני חוקרת…"; היה באותו node `668:13682`, שמחזיק היום את נוסח LINGER).
- `hadas-tuval-2.*` 900×1747 (נשאר בדיסק לא-מקושר, כלל-זהב 8).
- `/tmp/gen_artwork_pages.py` (לא בריפו, לא זמין). `tools/migrate_exhibition_statements.py` עדיין בריפו אך בדימוס (יוצא עם הודעה) — לא להריץ.
