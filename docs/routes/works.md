# Works — route notes

> **קרא לפני עריכה של:** `works/index.html`, `works/<id>/index.html` (עמוד לכל יצירה), ולפני שינוי ב-`data/works.json` (`art_works[]`, `exhibition_statements[]`).
> מצב נוכחי + כללים פעילים (2026-09-27). היסטוריה: `docs/history/CLAUDE-2026-09-27.md` §4. חוזה השדות המלא: `docs/data-contracts.md`.

## Pages
- **`/works/`** → `works/index.html` · desktop `XhGH...::542:467` (עמוד מלא; **הגריד הקנוני = `542:500`**, מ-2026-06-11) · mobile `XhGH...::542:1365` (גריד `542:1390`) · ✅
  - ⚠️ **בפיגמה סדר היצירות במובייל שונה מהדסקטופ.** לאתר data אחד ⇒ **הדסקטופ `542:500` קובע את הסדר.** בבדיקת "1:1 מול פיגמה" — לציין מול איזה frame.
  - legacy (לא לעבוד מהם): `542:499` (עוטף-הסקשן של `542:500` בתוך `542:467`; הערות CSS עדיין מזכירות אותו ואת `489:4`), `491:928`, `489:4`, `Zn3N...::1213:2615`.
- **`/works/:id/`** → `works/<id>/index.html` — עמוד לכל רשומה ב-`art_works[]` (כולן `page:true`) · desktop `XhGH...::674:14072` · mobile `XhGH...::674:14022` · ✅
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
- 🔴 `sync_data.py` **לא** יוצר עמודים, **לא** נוגע ב-`<head>`/SEO, ב-renderer או ב-`_staging/`. שינוי טקסט שמופיע ב-head (כותרת יצירה → `<title>`/description/OG/JSON-LD של העמוד; ביו/סטייטמנט → meta/OG/twitter/JSON-LD של דף האומן) = עדכון ידני.
- 🔴 **עותק ידני שאינו של `sync_data.py`:** כרטיסי FIGURES ו-PRODUCTS ב-`sponsors/sumii/index.html` מעתיקים ביד מ-`works.json` את `shira-turbowicz-1..3` ו-`melani-hekimoglu-1..5` — כותרות (כולל `title_en`), נתיב תמונה, `width`/`height`, רוחבי srcset וקישור `works/<id>/` (`docs/routes/sponsors.md`). שינוי באחת הרשומות האלה = לעדכן ידנית גם שם.
- `tools/sync_works_mirrors.py` = עטיפה ל-`sync_data.py`. `tools/migrate_exhibition_statements.py` בדימוס — לא להריץ. `works.json :: works[]` (3 אריחים) = הומפייג', לא הנתיב הזה.

### סדר, תצוגה, כתיב
- **סדר המערך = סדר הגריד ב-`/works/`**; `artist_page_pos` נצרך רק בדפי האומנים (כללי ה-pos: `docs/routes/artists.md`).
- `hidden:true` מסונן **רק** בגריד `/works/` (JS `!w.hidden`) וב-`#g-artworks-data` (`sync_data.py`). 🔴 **לא מסתיר את עמוד היצירה ולא את הכרטיס בדף האומן** (הרנדררים לא בודקים `hidden`; הכרטיס ממשיך לקשר ל-`works/<id>/`, שב-`_staging` = 404) — כך גם הכרטיסים הידניים ב-`sponsors/sumii/` (shira/melani). מנגנון staging המלא (הסתרה/חשיפה; יצירה בודדת של אומן גלוי — אפשרויות לא נוסו, טעון הכרעה): `docs/routes/artists.md` → staging. הסתרה אמיתית של יצירה: תיקייה ל-`_staging/works-<id>/`, הוצאה מ-sitemap, `robots:noindex`.
- כתיב שמות עברית = הקנוני של `artists.json`; ב-`details_he` תמיד `ס"מ` (לא `ס״מ`).
  - 🔴 חריגים מכוונים ב-`artist_he` (לא לקצץ לשם מ-`artists.json`): `tali-zelnik-1/2` = "טלי זלניק | סטודיו פיס אוף מיין סטודיו" (בקשת האמנית, `docs/routes/artists.md`); `shira-turbowicz-1..3` = "שירה טורבוביץ | sumii" (הלטינית ב-`.lat`); `livay-levi-3` = "ליוואי לוי × הדס טובל" (קרדיט ה-collab).
  - 🔴 **"טורבוביץ" — בלי גרש** (הכרעה 2026-09-27, בכל האתר; `docs/routes/sponsors.md`). חל גם על ה-head של `works/shira-turbowicz-1..3` (`<title>`, description, `og:*`, `twitter:*`) — עותקים ידניים. לא להחזיר את הגרש.
  - סטיות נוספות מהקנוני בלי הכרעה → Open issues.
- איות אנגלי קנוני (Audit 2026-07-09, הכרעת משתמש): **"adi duek"**, **"zohar shitrit"**; ה-slugs נשארים `adi-duak`/`zohar-shtrit`.
- `artist_he:null` ⇒ מוצג השם הלטיני (`sami-david` "samy d.", `la-raz-porta`).

### כללי-זהב רלוונטיים
- כל טקסט מ-JSON שעשוי להכיל לטינית → `.lat`/Copperplate (`latHtml()`; בפרטים `detailsHtml()`→`.det-en`). `esc()` לבד = באג פונט. לבדוק **כל** שדה: כותרת/אמן/פרטים/גלריה/תערוכה/statement.
- כל אזכור אומן = קישור (`docs/artist-linking.md`).
- תמונות `images/works/v2/<img>.{webp,avif}`. `widths[]`: **האחרון = רוחב `<img>.webp` הראשי**, השאר `<img>-<w>w.webp` + אח avif לכל אחד. `w`/`h` = הקובץ הראשי.
  - וריאנטים **חובה** כש-≥80KB וגם ≥800px (כלל-זהב 12): כל אחד מ-480/768/1080 שצר מ-90% מהראשי ⇒ ראשי רחב מ-1200 נושא גם `1080w` (`amnon-lipkin-3..7`, `michael-konovalenko-1`). מתחת לסף — רשות, אבל בפועל **כל** יצירה ברוחב ≥480 נושאת `480w` (למשל `zohar-ron-1..4` ב-690, `melani-hekimoglu-1` ב-548). ל-`livay-levi-4` (406) ול-`alice-debellis-1` (238) יש `widths:[<natural>]` רק כי הן צרות מ-480 — לא תקדים לדלג על 480w ביצירה רחבה יותר.
- לא לדרוס תמונה — צילום חדש = `<img>-v2` + עדכון `img` (תקדים `hadas-tuval-2-v2`).
  - OG: יצירה חדשה = `og/works-v2-<id>.jpg`. צילום חדש ליצירה קיימת = לאפות מחדש **את הקובץ שה-head כבר מפנה אליו** + לעדכן מידות: `hadas-tuval-2` → לפי id (`og/works-v2-hadas-tuval-2.jpg`, 998×1330); `zohar-ron-dan-ben-ari-1` → לפי img (`og/works-v2-zohar-ron-dan-ben-ari-1-v2.jpg`).
- `images/works/v2/*` ממוחזרות מחוץ ל-`works/`/`artists/` — `grep -r` לפני שינוי שם/תוכן:
  - `press/the-shared-list/`: `zohar-ron-5`, `nir-giorgio-levin-8`, `elsa-ars-brush-1` + `og/works-v2-zohar-ron-5.jpg`.
  - כרטיס הכתבה ב-`index.html #press`, ב-`press/index.html` וב-`data/press.json`: `zohar-ron-5`.
  - `exhibitions/the-peeler/` (רצועת האומנים): `alice-debellis-2`, `amnon-lipkin-13`, `elsa-ars-brush-1`, `maria-artamonova-1`, `michael-konovalenko-1`, `noemi-safir-2`.
  - `sponsors/sumii/`: `shira-turbowicz-1..3`, `melani-hekimoglu-1..5`; ב-`data/sponsors.json` — `cover_image` = `melani-hekimoglu-4`.
  - קרוסלות הגלריות (`#g-artworks-data`); `tools/seo/og-dims.json`.

### קישורים נכנסים (לכן לא משנים id — כלל-זהב 6)
- גריד `/works/`; כל דפי האומנים (לייטבוקס עם `data-artwork-page` ⇒ קליק על התמונה / "לעמוד היצירה"); שקופית המרכז בקרוסלת `galleries/<slug>/`; `sponsors/sumii/` (FIGURES → `shira-turbowicz-1..3`; PRODUCTS → melani: plates=4, vases=1, dessert-bowl=2, lamp=5, planter=3); `press/peeling-a-layer/` → `jessica-tabarovsky-1`.

### בדיקה
- שינוי renderer/CSS בהרבה עמודים = חובה:
  1. `node tools/regress/snapshot.mjs --label before --only works/`
  2. השינוי
  3. `node tools/regress/snapshot.mjs --label after --only works/`
  4. `node tools/regress/diff.mjs before after` (exit 0 = זהה)
  - `--only`/`--widths` הם דגלים של `snapshot.mjs`, לא של `diff.mjs` — **אותם ערכים בשתי הריצות**. ברירת המחדל 390,1440; לעבודת layout/טיפוגרפיה `--widths 390,1024,1366,1440`.
  - שינוי שנועד לשנות פלט (למשל הפצת `linkNames()`) יוצא ב-exit 1 — לקרוא את ה-diff ולוודא שהשתנו רק העמודים/האלמנטים המכוונים. עמוד יצירה חדש יופיע כ-`only in after` (דף חדש נכלל גם לפני `git add`) — צפוי.
- טיפוגרפיה בודקים **רק ב-http** (`python3 -m http.server`; ב-file:// כרום חוסם `@font-face`). 🔴 אבל **טעינת הדאטה בדף האומן** שבו היצירה מופיעה — **גם ב-file://**, או ברתמה (`--only artists/<slug>/`; ברירת המחדל `--modes http,file`): ב-http `data/generated/artists.js` חסר/שבור נבלע ב-`fetch("../../data/artists.json")` והדף נראה תקין (`docs/routes/artists.md` → Data flow).

## `/works/` — הגריד
- hero אפור `#EEF0EF`: `THE ART` (Bold) / `works` (Light), 80px (60 ≤1100, מובייל ממורכז `clamp`).
- **3 עמודות דסקטופ / 2 מובייל** (גם ≤390), `column-gap:16` (12 ב-≤390), `row-gap:64/48/40`.
- כרטיס: תמונה `aspect-ratio:33/40` `contain` על `#FAFAFA` → אומן (→ דף האומן; קרדיט מעורב כמו `"שירה טורבוביץ | sumii"` נעטף `.lat`) → כותרת (`is-he`/`is-en`/`is-bi` עם קו מפריד) → `details_he` (`white-space:pre-line`; מידות ב-`.dim` LTR) → "נמכר" אם `sold` → `gallery_en` בשתי שורות → `../#galleries`.
- קליק על התמונה: `page:true` ⇒ `<a href="<id>/">`. לייטבוקס כ-fallback לרשומה בלי `page` (scope יחיד לכל כרטיס — `data-artwork-gallery` על כל `<article>`, בלי prev/next) — **בגריד הזה בלבד**: דפי האומן (`data-artwork-page`) ושקופית המרכז בקרוסלות `galleries/<slug>/` מקשרים ל-`works/<id>/` **תמיד**, בלי לבדוק `page` (ולכן `page:false` לא מונע קישור שבור — ראה מתכון ההוספה).
- **טעינה מדורגת:** 12 ואז צ'אנקים של 18, IntersectionObserver על sentinel (`rootMargin:'1800px 0px'`). כל צ'אנק (`appendChunk`) מריץ אחרי ההזרקה `ArtworkLightbox.refreshFocusable()` + `PictureUpgrade.refresh(grid)`; ואז 🔴 re-arm (`unobserve`+`observe`) של ה-sentinel — אחרת נתקע. בלי IO ⇒ רינדור מלא. כרטיס ראשון `fetchpriority="high"`.

### סדר הגריד
- 1–70 ו-79–122 = סדר `542:500` ברצף אחד, בלי היסט בראש (אימות מלא אחרון 2026-06-11; הוספות מאוחרות כמו `aharon-bas-1` בראש, `bar-cohen-1`, `talia-zoref-2/3`, `elsa-ars-brush-6` שובצו בתוכו — ⚠️ unverified מול הפריים הנוכחי).
- 🔴 **71–78 = בלוק הרזידנסי** (`shira-turbowicz-1..3`, ואז `melani-hekimoglu-1..5`) — הכרעת המעצבת 2026-08-23 "לשים באמצע… שלא תהיה ראשונה". **לא להחזיר לראש.**
- 123 והלאה = יצירות שאינן ב-`542:500`, בסוף לפי סדר הוספה (the-peeler ×17, noemi-safir-11/12, amnon-lipkin-12/13, tali-zelnik, jessica-tabarovsky-2, hadas-tuval, livay-levi-3, livay-levi-4). **יצירה חדשה שלא בפריים ⇒ לסוף.**
- סדר ויזואלי של `542:500`: ה-API מחזיר `mode:grid` (3×37, `gridRow`/`gridColumn` על כל כרטיס) ⇒ למיין לפי (gridRow, gridColumn). (ב-2026-06-11 הוא היה `layoutMode:none` אבסולוטי ⇒ מיון לפי (y, x).)

### הכרעות מול הפיגמה
- **טקסט ב-data של פיגמה ≠ טקסט גלוי** (`get_figma_data` מחזיר שכבות מוסתרות בלי סימון) ⇒ לרנדר את ה-node לפני שמייחסים meta. מוסתר ולכן **לא** נשאב: בולרפלייט "60x80 שמן על קנבס" על 26 כרטיסים אחוריים, "התנערות" על `holy-kadosh-3`, הפרטים של `zohar-shtrit-1`. **גלוי ונשמר:** "קרמיקה" ב-`tal-nehoray-1..5`.
- אימות סדר = **ברמת תמונה**, לא רק טקסט (המעצבת החליפה תמונות בין כרטיסים חסרי-כותרת: tal-nehoray, gal-polk, adi-duak, la-raz-porta).
- כפילויות תמונה בפיגמה — **לא שוכפלו**: jessica=anat-4, noemi-4=risa, noemi-6=alon-1, NGL-2≈alon-1, tanya crop2/aura1=aura2, sami 64=66.
- `sold` רק לפי תג גלוי (2026-06-11 נוספו: anat-wegier-4, alon-2, nir-giorgio-levin-2, la-raz-porta-1, raz-ronen-1/2).

## `/works/:id/` — עמוד יצירה (תבנית)

### מבנה
- `<html data-artwork-id>` + `#artwork-data` + IIFE שמרנדר ל-`#aw-media`/`#aw-info`. 🔴 שם התיקייה = `data-artwork-id` = `id` בתוך `#artwork-data` (`sync_data.py` לא בודק — סקריפט הבדיקה במתכון ההוספה).
- דסקטופ: תמונה `contain` משמאל (`max-height:640px`), מידע 360px מימין (320 ≤1100); `.aw-info` נשאר LTR (`flex-end` = ימין), `rtl` רק על הטקסט. מובייל: עמודה; 🔴 `.aw-media{flex:0 0 auto}` (לא `flex:1 1 0` — קורס לגובה 0); כפתורים `row-reverse` + `justify-content:flex-start` = ימין.
- תמונה = LCP (`fetchpriority="high"`, `sizes="(max-width:768px) 100vw, 55vw"`; **לא** `loading="lazy"` — הרנדרר פולט אותה כך בכוונה), קליק ⇒ לייטבוקס `components/artwork-lightbox.{js,css}` (`[data-artwork-src]`, לא מנווט).
- **contact us** = `mailto:` לקורין אברהם (אוצרת כל התערוכות; הכתובת hard-coded ב-renderer בכל עמודי היצירה, מקורה `data/opencalls.json`), נושא+גוף ממולאים (יצירה, אמן, תערוכה, פרטים, קישור). **share** = `[data-share-btn]` (`site-chrome.js`).
- מטא: כותרת אחת (`title_he`, אחרת `title_en` ב-Copperplate), אמן → `../../artists/<artist_slug>/`, פרטים, גלריה → `../../#galleries` **בשורה אחת**.
- **divider + סקשן תערוכה רק אם יש `exhibition_title_he` או `statement_he`.** הכותרת מקושרת ל-`../../<w.exhibition_route>/` (Audit 2026-07-09 — לא hardcode `opencalls/`). routes: הקולפן `exhibitions/the-peeler` (**לא** `opencalls/…`), `exhibitions/how-many`, `exhibitions/loneliness`, shira `sponsors/sumii`, melani `null`; ל-`alon-1/2` אין מפתחות `exhibition_*`.
- שדות אופציונליים שהרנדרר של עמוד היצירה קורא: `exhibition_title_he`, `exhibition_route`, `statement_he[]`, `collab[]`/`collab_connector_he`. `page` — רק הגריד `/works/`; `exhibition_slug` — רק דפי האומן (`exRank`); `art_works[].kind` — מידע בלבד, אף רנדרר לא קורא (ה-`kind:"residency"` ב-`galleries/dizengoff/` הוא של רשומת `#g-exhibitions-data`).

### וריאנטי renderer (5)
העמודים זהים פרט ל-data/head ולהבדלי ה-JS וה-CSS האלה. שינוי renderer/CSS = בכל הוריאנטים הרלוונטיים + regress. לזיהוי: `grep -l 'w.collab' / 'wrapDimRuns' / 'NAME_LINKS' / '.aw-artist a{' works/*/index.html`.
- **A** (כל השאר): בסיס — בלי collab, בלי `wrapDimRuns`/`.dim`, בלי כלל `.aw-artist a`.
- **Z** (`zohar-ron-5/9`): + `wrapDimRuns` + CSS `.dim{direction:ltr;unicode-bidi:isolate}`; בלי `.aw-artist a`.
- **B** (aharon-bas-1, alice-debellis, amnon-lipkin, bar-cohen-1, hadas-tuval, maria-artamonova, michael-konovalenko, shira-turbowicz, tali-zelnik): + `wrapDimRuns`/`.dim` + ענף collab ב-`artistHtml` + CSS `.aw-artist a{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:2px}` + `:hover{opacity:.6}`. ⚠️ הסלקטור תופס רק `<a>` **מקונן** = שמות collab; ביצירת אמן יחיד (כל B היום) הקרדיט הוא `<a class="aw-artist">` עצמו ⇒ **בלי** קו תחתון, כמו A.
- **M** (`melani-hekimoglu-*`): B (כולל ה-CSS) + `exHead` ריק כשאין כותרת + `linkNames()` (`NAME_LINKS`: "ארז זילינסקי רוזן"→`../../about/`, "קורין אברהם"→`../../curators/korin-avraham/`, CSS `.aw-ex-body a.artist-link`).
- **L** (`livay-levi-3`): בסיס + ענף collab + CSS `.aw-artist a{transition:opacity .2s}` + `:hover{opacity:.6}` בלבד — **בלי קו תחתון** על שמות ה-collab, ובלי `wrapDimRuns`/`.dim`.
- עמוד חדש — להעתיק מוריאנט שמכסה את הצרכים: collab ⇒ וריאנט עם ענף collab (B/M/L; L בלי `.dim`); בלי כותרת ⇒ M; מידות מבודדות `.dim` ⇒ Z/B/M. העתקה מ-A מאבדת בשקט את ענף ה-collab ואת `.dim`. ⚠️ לא הוכרע: B/M מוסיפים קו תחתון לשמות collab, ואילו `livay-levi-3` (L) מציג אותם בלי ⇒ collab חדש שמועתק מ-B ייראה שונה ממנו (Open issues).

### רזידנסי — יצירה בלי תערוכה (גלריית דיזינגוף)
- **עם כותרת** (shira-turbowicz): `exhibition_title_he:"POP UP ART RESIDENCY"`, `exhibition_slug:null`, `exhibition_route:"sponsors/sumii"`, `kind:"residency"`. בדף האומן קבוצה רגילה; `exRank(null)=-1` ⇒ תמיד מתחת לתערוכות.
- **בלי כותרת** (melani-hekimoglu, פריים `1634:188`): שלושת `exhibition_*` = `null` + `kind:"residency"`, ורשומת `exhibition_statements` עם `exhibition_title_he:null`. 🔴 **`null` מפורש בשני הצדדים** — מפתח חסר לא מתאים ב-`===` והסטייטמנט נעלם בשקט. בעמוד היצירה דורש וריאנט M; בדף האומן — תיקונים מקומיים (`docs/routes/artists.md`).
- ⚠️ `alon-1/2` (בלי `exhibition_*`, עם `statement_he` per-work) על וריאנט A ⇒ `<span class="aw-ex-title">` ריק (קוסמטי).

### הוספת יצירה (מתכון)
1. **מקור התמונה = ה-imageRef של הכרטיס בפריים.** ה-fill הראשון הוא בדרך כלל הנראה ומה שמתחתיו leftovers — אבל הכלל הוא **לרנדר את ה-node** (`get_figma_data` מחזיר גם שכבות מוסתרות; lessons 2026-08-12/08-19/08-28). `cropTransform` על ה-fill = קרופ של המעצבת — לאפות אותו (תקדים `livay-levi-4`). התקבל רק "Artworks Section" בודד ⇒ למשוך את פריים דף-האומן ההורה ולגזור את ה-`artist_page_pos` של **כל** הקבוצה מקריאת LTR שלו (lessons 2026-07-15, 2026-08-28; artists.md → קריאת פריים). את ה-node לרשום ב-`FIGMA_LINKS.md`. תמונות ל-`images/works/v2/` (כלל-זהב 12; מקור גולמי ל-`_originals/`).
2. **רשומה ב-`art_works[]` = להעתיק רשומת אחות מ-`data/works.json` ולערוך — לא לבנות מרשימת שדות.** קודם `docs/data-contracts.md` §9.2–9.3.
   - אחות מאותה תערוכה (הקולפן: `maria-artamonova-1`; רזידנסי עם כותרת: `shira-turbowicz-1`; בלי כותרת: `melani-hekimoglu-1`; collab: `livay-levi-3`). 🔴 לא מ-`#artwork-data` של עמוד יצירה — שם `sync_data.py` מוסיף `statement_he` מה-fallback, ורשומה שנושאת אותו מקבלת באנר per-work כפול בדף האומן.
   - הצורה: 16 שדות בסיס — `id, artist_slug, artist_he, artist_en, title_he, title_en, gallery_slug, gallery_en, sold, details_he, img, w, h, widths, artist_page_pos, page` (`img` = שם בסיס, בלי נתיב/סיומת) — ועוד `exhibition_title_he/slug/route`. 🔴 **לא** הצורה של `artists.json::works[]` (`image`/`year`/`medium`).
   - מקום: **סוף המערך** (סדר המערך = סדר הגריד `/works/` וסדר הקרוסלה בדף הגלריה), אלא אם גריד `542:500` ממקם אותה (ראה "סדר הגריד"). `page:true`; `artist_page_pos` לפי `docs/routes/artists.md` (לא 0, ייחודי באומן רב-קבוצתי); `sold`/`details_he` רק לפי מה שגלוי.
   - סטייטמנטים: טקסט-קבוצה → `exhibition_statements[]` (אותה מחרוזת `exhibition_title_he` בדיוק); `statement_he` ברשומה = **טקסט על היצירה הבודדת בלבד** (באנר מעל הכרטיס בדף האומן). בשני המקומות `statement_he` = **מערך פסקאות** (`["¶1","¶2"]`), לעולם לא מחרוזת — הרנדררים קוראים `.map` וקורסים. 🔴 רשומת `exhibition_statements` חדשה = העתק של קיימת עם **חמשת המפתחות**: `artist_slug`, `exhibition_title_he`, `exhibition_slug`, `exhibition_route`, `statement_he` (`null` מותר, מפתח חסר לא) — בלי `artist_slug`/`exhibition_title_he`/`statement_he` ה-`sync_data.py` קורס ב-`KeyError`.
   - **2א. פריים חדש לאומן קיים** — להשוות **מילה-במילה** כותרת קבוצה, סטייטמנט קבוצה וביו מול הדאטה, לא רק להוסיף את היצירה (תקדימים: `livay-levi-4` — `הקולפן` הפכה ל-`הקולפן | מעורר רגש: מרחק שקט`; `jessica-tabarovsky-2` — הסטייטמנט הורחב והביו הוחלף). כותרת שהשתנתה = `exhibition_title_he` בכל יצירות הקבוצה **וגם** המפתח ברשומת `exhibition_statements`, באותו שינוי, ואז `sync_data.py`. ביו שהשתנה = גם ה-`<head>` של דף האומן (artists.md → Data flow). טקסט על יצירה אחת → `statement_he` שלה, לא סטייטמנט הקבוצה.
3. להעתיק תיקיית אחות ל-`works/<id>/` ולהחליף: `data-artwork-id`, **ה-`id` בתוך `#artwork-data`** (מספיק `{"id":"<id>"}` — 🔴 sync_data מזהה לפי ה-id שבפנים; id של האחות = העמוד מציג בשקט את האחות), ו**כל ה-head**: `<title>`, description, בלוק `SEO:auto` (canonical, `og:*` + `og:image:width/height`, `twitter:*`, JSON-LD `VisualArtwork`+`BreadcrumbList`) — `elsa-ars-brush-6` נשא פעם SEO שלם של talia-zoref-1.
4. OG ידני: `magick images/works/v2/<img>.webp -resize '1200x1200>' -strip -quality 82 og/works-v2-<id>.jpg` (נכנס ב-1200×1200 ולעולם לא מגדיל — 🔴 לא `-resize 1200x` של ה-spine §7, שמגדיל יצירות צרות מ-1200 כמו `livay-levi-4`). `og:image:width/height` ב-head — מ-`magick identify -format '%w %h'` של הקובץ שנוצר. 🔴 **לא להריץ `og_gen.py`/`inject.py` גורפות** (`docs/todo.md`). ⚠️ לפחות 17 מקובצי ה-OG הגבוהים מ-1200 נאפו ב-`-resize '1200x>'` (למשל `livay-levi-4` 406×1293, `aharon-bas-1` 596×1600); בתוך משפחה להעדיף את מה שהאחיות משתמשות בו. רשות: רשומה ב-`tools/seo/og-dims.json` — `"images/works/v2/<img>.webp": {"jpg": "og/works-v2-<id>.jpg", "w": …, "h": …}`; בלעדיה `inject.py <page>` מפיל את `og:image` ל-webp.
5. `python3 tools/sync_data.py` — מדפיס את **הרשימה המלאה** של הקבצים שכתב, ו**כל אחד מהם נכנס לאותו קומיט עם ה-JSON**: בדרך כלל `data/generated/art-works.js` (+`ex-statements.js` כשנגעת בסטייטמנטים), `works/index.html`, `works/<id>/index.html` החדש, עמודי `works/<id>/` של אחיות שהרשומה/ה-fallback שלהן השתנו, ו-`galleries/<gallery_slug>/index.html`. בקומיט: `git status --short` ו-`git add` **בשמם** + ה-JSON, תיקיית העמוד החדש (`??`), התמונות, ה-OG, `sitemap.xml` ושאר מה שערכת (`FIGMA_LINKS.md`, `tools/seo/og-dims.json`, ה-`<head>` של דף האומן ב-2א); לא `-A` ולא glob. קומיט בלעדיהם = היצירה חסרה בפרודקשן ב-`/works/` ובקרוסלת הגלריה, ו-`--check` נכשל על HEAD.
   - `--check`: 🔴 exit 0 **וגם בלי אף שורת `!` ב-stderr** — `! artwork page id not in works.json` = `id` שגוי/לא-קיים ב-`#artwork-data` (sync_data רק מדלג; `--check` עובר), ועמוד בלי בלוק `#artwork-data` מדולג **בלי שום הודעה**. לכן גם בדיקת ה-1:1 שלמטה.
6. `sitemap.xml` באותו קומיט + `python3 tools/seo/refresh_sitemap_lastmod.py`; בדיקת השלמות של כלל-זהב 15 (`<loc>` מול `index.html` מוגשים) חייבת לצאת **שווה בדיוק**.
   - חיפוש ההידר (`search-index.js`) נבנה מה-`<title>`/description/JSON-LD (`name`, `creator.name`) הסטטיים — head שהועתק ולא עודכן מופיע גם בחיפוש. נבנה מחדש ע"י `.githooks/pre-commit` **רק אם ה-hook מופעל** (`git config core.hooksPath .githooks`); אחרת `python3 tools/search/build_index.py` (מאנדקס רק עמודים שב-git) וכלול את `search-index.js` בקומיט. לא לערוך ביד.
- 🔴 **לכל `id` ב-`art_works[]` חייבת להיות תיקייה `works/<id>/`, ולהפך.** `page` נבדק **רק** בגריד `/works/`; דפי האומנים ושקופית המרכז בקרוסלות `galleries/<slug>/` מקשרים ל-`works/<id>/` תמיד ⇒ רשומה בלי תיקייה (sync_data לא יוצר עמודים ולא מזהיר) = 404, ותיקייה שנשארה אחרי מחיקה = עמוד יתום — וכל הבדיקות עוברות. בסוף **כל** הוספה או מחיקה להריץ (נקי = השורה `no page: set() orphan: set()` בלבד; בודק גם בלוק חסר ו-`data-artwork-id` = שם התיקייה = `id` ב-`#artwork-data`):

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

- **מחיקה:** JSON, תיקייה, sitemap, `grep` לקישורים נכנסים, `sync_data.py`, ובדיקת ה-1:1 שלמעלה.

## `/works/livay-levi-3/` — collab
- **המתכון המאושר ליצירה משותפת** (הכרעת פיגמה `668:13584`; השימוש החי הראשון ב-`collab[]`): להעתיק מ-`data/works.json` את `livay-levi-3` ואת שתי רשומות ה-`exhibition_statements` שלה ולערוך (מתכון ההוספה, שלב 2):
  - **רשומה אחת** (`artist_slug:"livay-levi"`) + `artist_pages:["hadas-tuval"]` + `collab[]` (שני `{slug,name_he,name_en}`) + `collab_connector_he:"×"` ⇒ בגריד **פעם אחת**, בשני דפי האומנים, עמוד קנוני אחד. **לא לשכפל לשתי רשומות** (תמונה כפולה בגריד). ⚠️ `artist_pages` לא נתמך בדפי ה-legacy (`alon`, `dan-ben-ary`, `zohar-ron-dan-ben-ari` — artists.md); collab שצד שלו הוא legacy לא יופיע שם בלי שדרוג הרנדרר + regress.
  - **קבוצה ייעודית** `"הקולפן | interdependence"` — הקיבוץ לפי מחרוזת מדויקת, ולכן אי אפשר להתמזג לקבוצות הקיימות של השניים.
  - **רשומת `exhibition_statements` לכל אומן.** כרגע הנוסח מפוצל: ליוואי "…בין ליוואי לוי והדס טובל.", הדס "…בין הדס טובל לליוואי לוי." (`1502:122`); עמוד היצירה מציג את נוסח ליוואי.
  - `artist_page_pos:1` חל בשני הדפים (הקבוצה המשותפת ראשונה בשניהם).
- 🔴 **`×` (U+00D7) ולא `x`** — ל-FbEzmel אין `x` לטיני, והמחבר עובר `esc()` ולא `.lat`. לפני תו לטיני בודד במחרוזת עברית — לבדוק שהגליף קיים ב-FbEzmel (`docs/lessons.md` 2026-08-12).
- `artistHtml` (עמוד + גריד) = שני שמות מקושרים, מחוברים ב-`×` (בלי `collab_connector_he` הרנדרר נופל ל-"בשיתוף"; המתכון המאושר = תמיד `"×"`).
- תמונה `images/works/v2/livay-levi-3.{webp,avif}` 1080×810 +480/768 (imageRef `4ce7697e…`), OG `og/works-v2-livay-levi-3.jpg`.
- כתיב מוכרע מול הפיגמה: "גןף"→**"גוף"**, "ותלוייה"→**"ותלויה"**.
- `title_he_by_artist`/`details_he_by_artist`: נתמכים **רק בכרטיס הגריד של 10 דפי אומן** (`_th`/`_dh` ב-`buildRichCard`; artists.md → 7-variant). **חסרים ב-`artists/livay-levi/`** ⇒ ב-`livay-levi-3` ישפיעו רק בדף של הדס; לפני שימוש — להפיץ ל-livay-levi (+ regress). `/works/` ו-`works/<id>/` **תמיד קנוניים בכוונה** (`title_he`/`details_he`). אין היום רשומה שמשתמשת בהם.
- `artist_pages` בלי collab משמש גם את `zohar-ron-dan-ben-ari-1`.

## רישום רשומות — מקורות פיגמה והכרעות תוכן
> כותרות קבוצה, סטייטמנטים, ביוגרפיות ו-pos של אומני הקולפן — בסעיפי האומן ב-`docs/routes/artists.md`; כאן רק מה שייחודי לרשומות היצירה.
- **zohar-ron-5..8** ("דג 1/2/3", "בּוּרְקָה | برقع") `613:67..91`; **gal-rotem-1** "טביעה בחשיכה" `607:33`; **raz-ronen-1/2** `616:129/149`.
- **amnon-lipkin** (`798:173`; כותרת הקבוצה/סדר 12–13/"בדייקנות" — artists.md): 12/13 = 36/66 ריקמה ידנית (`944:257`/`800:491`); הסדר 12/13 הוא החלטת המעצבת 2026-07-15, לא ליישר. פסקה 1 מסתיימת "…ומציפות את הקונפליקט שבין החלק המייסר במאבק לבין המרגש שבו."
- **jessica-tabarovsky** — כותרת/סטייטמנט/pos: artists.md. הסטייטמנט (`668:13332`) יושב בתוך הסקשן `668:13235` שכולל גם את הכותרת `668:13236`; הביו (`668:11043`) בתוך הסקשן `668:11042`. -1 "התנערות" = pos 2.
- **natasha-zeriker** — **"הקולפן | מעורר רגש: אובדן שליטה"** (ברשומה + ב-natasha-zeriker-1); סטייטמנט נוכחי = 10 פסקאות שנפתחות ב-"LINGER" — node `668:13682` (כותרת `668:13683`, טקסט `668:13708`), שהמעצבת שכתבה in-place מעל הישן.
- **hadas-tuval** (`797:106`; כותרת/ביו/סטייטמנט — artists.md; יצירות `797:146`): -1 "falling into movement" 1086×1448; **-2 "סף" = `img:"hadas-tuval-2-v2"`** 998×1330 +480/768 (`797:152`, imageRef `8dfed7d2…`). פורטרט `images/artists/hadas-tuval/`, `@hadastuval.ayni`, דף אומנית מתבנית bar-cohen. כרטיס גריד `images/artists/grid/hadas-tuval.{webp,avif}` 810²+480w מהפורטרט (פריט 42; המיקום — artists.md).
- **tali-zelnik-1/2** — "הקולפן | מעורר הרגש: שייכות" (`854:1082`) verbatim, מפתח משותף עם `exhibition_statements` (artists.md → Verbatim).
- **noemi-safir-11/12** "התמכרות רכה"/"לחץ סגול" (`943:237`/`668:12584`, דף `668:12489`) — pos 4/5 בראש How Many בדף האומן.
- **elsa-ars-brush-6** "מושעה בזמן" `833:944`. **talia-zoref-2/3** "שלווה בסגנון | Serenity in Style" / "להתחבר | Connect" (`668:13734`/`867:1138`/`870:1148`); talia-zoref-1 = pos 2.
- **הקולפן, 6 פריימי מובייל (2026-06-23):** michael-konovalenko ×3, maria-artamonova, alice-debellis ×2, amnon-lipkin ×11 (nodes — artists.md) — `medina`, סטייטמנט לכל אומן.
- **shira-turbowicz-1..3.title_en** ("Gaia"/"Sonia Delaunay"/"Niki de Saint Phalle") נוסף לכיתובי FIGURES בעמוד הספונסר (עותק ידני שם).
- **zohar-ron-dan-ben-ari-1** ("sex?") + **zohar-ron-9** ("הקוסם") — כותרת הקבוצה בשתיהן = "How Many Partners Have You Had?" (נקייה), לא "…| sex?" (שאר הפרטים: artists.md → zohar-ron).

## Open issues
> רשומים ב-`docs/todo.md`: קישור שמות בסטייטמנט, BLOOM PLANTER, Sonia Delaunay. פריטים שמסומנים "נצפה בקוד" ופריט כפילויות התמונה **אינם** רשומים שם — להוסיף ל-`docs/todo.md` כשמטפלים או מכריעים.

- **שמות בתוך הסטייטמנט לא מקושרים בעמודי היצירה** (כלל-זהב 10; ברנדרר דף האומן — artists.md → Open issues). רק `melani-hekimoglu-*` (M) מריצים `linkNames()`, ו-`NAME_LINKS` שם ממפה שני שמות: "ארז זילינסקי רוזן"→`../../about/`, "קורין אברהם"→`../../curators/korin-avraham/`.
  - נצפה בקוד (בסטייטמנט המוצג, כולל fallback) — ⚠️ רחב מהרשום ב-`docs/todo.md`: `shira-turbowicz-1..3` (ארז, קורין) · `livay-levi-3` (ליוואי לוי, הדס טובל) · `gilad-kenan-1` (גלעד קינן) · `natasha-zeriker-1` (נטאשה זריקר) · `sami-david-2..4` (סמי די) · `zohar-ron-1..4`, `zohar-ron-9` (זוהר רון).
  - הפצת ה-snippet כמו-שהוא מתקנת רק את shira; צריך להרחיב את `NAME_LINKS` לשמות האומנים (או lookup מול `artists.json` → `../../artists/<slug>/`), CSS `.aw-ex-body a.artist-link`, ולהפיץ לכל 5 הוריאנטים + regress. ⚠️ להכריע אם החריג "לא מקשר לעצמו" ב-`docs/artist-linking.md` (מנוסח לדף האומן) חל גם כאן.
- ⚠️ נצפה בקוד — `artist_he` שסוטה מהקנוני של `artists.json` בלי הכרעה (לשאול לפני נרמול): `zohar-ron-dan-ben-ari-1` "דן בן-ארי" (קנוני "בן ארי"); `holy-kadosh-1..3` "טל קדוש" (קנוני "טל הולי קדוש"); `hila-loterstein-1..3` "הילה לוטרשטרין" (קנוני "לוטרשטיין" — נראה כטעות הקלדה).
- `melani-hekimoglu-3` (BLOOM PLANTER): `details_he` זהה ל-FLOW VASES (copy-paste של המעצבת, נשמר verbatim עד הכרעה).
- "Sonia Delaun" בפיגמה → "Sonia Delaunay" ב-`shira-turbowicz-2` (+ `docs/routes/sponsors.md`).
- כפילויות התמונה בפיגמה — לדווח למעצבת / לתקן בפיגמה (⚠️ לא ב-`docs/todo.md`; מקור: `docs/lessons.md` 2026-06-10).
- ⚠️ נצפה בקוד: `tali-zelnik-1/2` עם SEO שארית-staging (OG ברירת מחדל, JSON-LD `WebPage` בלבד, אין `og/works-v2-tali-zelnik-*.jpg`); 25 עמודים בלי `og:image:width/height` ו-3 עם מידות שגויות (`noemi-safir-11/12`, `talia-zoref-1` — קובצי ה-OG רחבים מה-webp; לאפות מחדש לפי שלב 4); ב-`tools/seo/og-dims.json` הרשומה של `hadas-tuval-2-v2` מצביעה ל-`og/works-v2-hadas-tuval-2-v2.jpg` שאינו קיים (העמוד מפנה ל-`og/works-v2-hadas-tuval-2.jpg`), ול-`livay-levi-4` אין בו רשומה.
- ⚠️ נצפה בקוד: קו תחתון על שמות collab לא אחיד. שם של אמן יחיד לא מקבל קו תחתון באף מקום — `.aw-artist a` (B/M) ו-`.meta .artist a` (גריד) תופסים רק `<a>` מקונן = ענף ה-collab. ההבדל הנראה: ב-`livay-levi-3` בכרטיס הגריד שמות ה-collab עם קו תחתון, ובעמוד היצירה (L) בלי. יישור = הכרעת משתמש + הפצה + regress.
- ⚠️ נצפה בקוד: קישור הגלריה (בגריד ובכל עמודי היצירה) עדיין `/#galleries`, לא `galleries/<slug>/` — שינוי = הכרעת משתמש + הפצה לכל הוריאנטים.
- כותרת קבוצת loneliness ב-`works.json` (34 יצירות + 11 רשומות `exhibition_statements`) = "בדידות בסביבה תוססת" (+ סיומות) מול הרשמית ב-`exhibitions.json` "בדידות בתוך סביבה תוססת" (Audit 2026-07-09); ⚠️ טעון הכרעת משתמש, ואיחוד = כל הרשומות וה-statements יחד + `sync_data.py`. 🔴 "בדידות בתוך בסביבה תוססת" (כפל-ב') בפיגמה — טעות מוכרעת, לא להעתיק. פירוט: artists.md → Verbatim.

## Removed / do not restore
- דאטה inline בדפי אומן (`__ART_WORKS_INLINE__` בתוך HTML) — עכשיו `data/generated/*.js`. לייטבוקס בכרטיסי גריד עם עמוד; פיצול שם הגלריה בעמוד היצירה; `.aw-media{flex:1 1 0}` במובייל. shira/melani בראש הגריד (בוטל 2026-08-23). הכתיב "טורבוביץ׳" (עם גרש) ב-`artist_he` וב-head של `shira-turbowicz-1..3` — הוחלף ב-"טורבוביץ" (2026-09-27).
- `opencalls/the-peeler` כ-`exhibition_route` של היצירות, או קישור hardcoded ל-`opencalls/` ברנדרר עמוד היצירה (העמוד `opencalls/the-peeler/` עצמו חי ולא מושפע).
- קולאב `aharon-bas-1` × bar-cohen (פוצל 2026-06-24 לשתי יצירות עצמאיות; ראה artists.md) — לא לאחד.
- טקסט מוסתר מהפיגמה (60x80, "התנערות", פרטי zohar-shtrit-1).
- סטייטמנט natasha הישן (6 פסקאות, "לאורך השנים אני חוקרת…"; היה באותו node `668:13682`, שמחזיק היום את נוסח LINGER).
- `hadas-tuval-2.*` 900×1747 (נשאר בדיסק לא-מקושר, כלל-זהב 8).
- `/tmp/gen_artwork_pages.py` (לא בריפו, לא זמין). `tools/migrate_exhibition_statements.py` עדיין בריפו אך בדימוס (יוצא עם הודעה) — לא להריץ.
