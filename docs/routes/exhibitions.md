# Exhibitions, curator & open calls — route notes

> לקרוא לפני עריכה של `exhibitions/*/index.html`, `curators/korin-avraham/index.html` או `opencalls/*/index.html`, וגם לפני שינוי ב-`data/exhibitions.json`, `data/curators.json` או `data/opencalls.json`, או בתמונות `images/events/loneliness/{invite-01..03,atmosphere,second-01..03}` (גלריית ה-hero של `exhibitions/loneliness/`). המסמך מתאר את המצב הנוכחי. ההיסטוריה: `docs/history/CLAUDE-2026-09-27.md` §4.

## Pages

- `/exhibitions/` (אינדקס) → ⏳ לא נבנה, אין עיצוב; בפועל הארכיון בהומפייג' (`#exhibitions`, `docs/routes/homepage.md`).
- `/exhibitions/loneliness/` → `exhibitions/loneliness/index.html` · ✅ data-driven מהתבנית · Figma desktop `XhGH...::119:156` · mobile `XhGH...::119:331`
- `/exhibitions/how-many/` → `exhibitions/how-many/index.html` · ✅ data-driven מהתבנית · Figma desktop `XhGH...::119:435` · mobile `XhGH...::119:642`
- `/exhibitions/the-peeler/` (הקולפן, גלריית כיכר המדינה, אוצרת קורין אברהם) → `exhibitions/the-peeler/index.html` · ✅ **סטטי קפוא** (עריכה ידנית ב-HTML) · Figma desktop `XhGH...::721:14300` · mobile `XhGH...::721:14513`
- סקשן האוצרת בתוך דף תערוכה (מתחת לאומנים): Figma desktop `XhGH...::301:2` · mobile `XhGH...::119:702`.
- `/curators/korin-avraham/` → `curators/korin-avraham/index.html` · ✅ data-driven · Figma desktop `XhGH...::314:4` · mobile `XhGH...::314:97` · תמונת הפרופיל `XhGH...::314:122`
- `/opencalls/` (אינדקס) → ⏳ לא נבנה, אין עיצוב.
- `/opencalls/the-peeler/` → `opencalls/the-peeler/index.html` · ✅ data-driven · Figma desktop `Zn3N...::1213:2417` · mobile `Zn3N...::1213:2518` · רשימת מעוררי הרגש (שבירות השורות): `XhGH...::119:2587`
- `/opencalls/how-many/` → `opencalls/how-many/index.html` · ✅ data-driven · Figma desktop `Zn3N...::1213:2340` · mobile `Zn3N...::1213:2263`
- `/opencalls/obsession/` → `opencalls/obsession/index.html` · ✅ data-driven, `theme:"light"` · Figma desktop `XhGH...::1906:664` · mobile `XhGH...::1906:587`
- קישורי Figma מלאים: `FIGMA_LINKS.md` (⚠️ סקשן הקולות הקוראים שם נקרא `/opencall/:slug`, ה-route בפועל `opencalls/`).

## מפת הדאטה (מי קורא מאיפה)

- `exhibitions/loneliness/`, `exhibitions/how-many/`: fetch ל-`data/exhibitions.json` + `site.json` + `curators.json`; inline (file://): `#fallback-exhibitions`, `#fallback-site`, `#fallback-curators` — **ביד**.
- `exhibitions/the-peeler/`: **ה-HTML עצמו**, בלי fetch ובלי JSON.
- `curators/korin-avraham/`: fetch ל-`curators.json` + `exhibitions.json` + `galleries.json`; inline: `#fallback-curators`, `#fallback-exhibitions-min` (ביד), `#fallback-galleries` (**`sync_data.py`**, אסור ביד).
- `opencalls/{obsession,the-peeler,how-many}/`: fetch ל-`opencalls.json` + `site.json`; inline: `#fallback-opencalls`, `#fallback-site` — **ביד**.
- ב-http ה-JSON גובר; ה-inline רק ב-file://. שאר העותקים ביד (Mirror registry ב-`docs/data-contracts.md`); שינוי ב-JSON מחייב לעדכנם.
- 🔴 **כל עותק מכיל את כל הרשומות:** `#fallback-exhibitions` בשני דפי התבנית = loneliness **וגם** how-many; `#fallback-opencalls` בשלושת דפי הקול הקורא = obsession, the-peeler, how-many. שינוי ברשומה אחת = עדכון בכל הקבצים.
- 🔴 **`#fallback-site` — מה חייב להישאר:** בדפי התבנית `footer.newsletter` (`title`/`placeholder`/`cta`) ו-`footer.links_he` (הרנדרר ניגש ל-`site.footer.newsletter.*` ו-`site.footer.links_he.slice()` בלי בדיקה; `copyright` חסר = `undefined`, בלי קריסה). בדפי הקול הקורא רק `site.footer.links_he || []` — מספיק ש-`site.footer` קיים. קיצוץ מעבר = קריסה ב-file://.
- drift ידוע ולא מזיק (אין לתקן): שדות שהרנדרר לא קורא חסרים בעותקים (`start_date`, `figma_node_*`, `bio_he`); ב-`#fallback-exhibitions` של loneliness לרשומת how-many `start_date:null`/`end_date:null`; ב-`#fallback-curators` של דפי התבנית `exhibition_slugs` = `["loneliness","how-many"]` (לא נקרא).

## Shared rules

- **כותרת loneliness הרשמית = "בדידות בתוך סביבה תוססת"** (audit 2026-07-09). "בתוך בסביבה" בפיגמה = טעות מוכרעת. **לא לשחזר.**
  - ⚠️ היא חלה על `exhibitions.json` ועל הדפים, **לא על מפתחות הקבוצה ב-`works.json`**: ב-`art_works[].exhibition_title_he` וב-`exhibition_statements[].exhibition_title_he` כתוב "בדידות בסביבה תוססת" (בלי "בתוך"), כולל תת-הקבוצות ("… | don’t lose your head", "… | ״ערכת בדידות״", "… | כְּתוּבָּה | QTUBA"). זה מפתח ה-join בין יצירות לסטייטמנטים וכותרת הקבוצה בדפי האומנים. **לא "לתקן" רשומה בודדת**; שינוי = כל הרשומות בשני המערכים + `python3 tools/sync_data.py`.
- **איות אנגלי קנוני** (הכרעת משתמש): "adi duek" ו-"zohar shitrit"; ה-slugs נשארים `adi-duak` ו-`zohar-shtrit` (כלל-זהב 6). השם המוצג לא חייב להתאים ל-slug: "gal pollak" → `gal-polk`, "samy d." → `sami-david` (⚠️ הרווח ב-`exhibitions.json` ובעותקי `#fallback-exhibitions` הוא U+00A0, `samy\u00A0d.`; grep עם רווח רגיל לא ימצא; לא להחליף בלי לבדוק שבירת שורה בכרטיס), "risa brooke oze" → `risa-oz`, "alon manjoch" → `alon`, "tal holy kadosh" → `holy-kadosh`, "elsa ers brosh" → `elsa-ars-brush`, "liel salman noam" → `liel-salman`.
- **`exhibition_route` של כל יצירות הקולפן ב-`works.json` = `exhibitions/the-peeler`** (לא `opencalls/the-peeler`); `works/<id>` בונים את הקישור מ-`w.exhibition_route`. ⚠️ `FIGMA_LINKS.md` עדיין כותב `opencalls/the-peeler` בשני מקומות — מיושן.
- **סטטוס התערוכה ידני:** `status` / `status_label_en` ב-JSON (בקולפן גם התג הסטטי ב-HTML), בלי אוטומציה לפי תאריך. **לא לשנות בלי הכרעת משתמש.**
  - **how-many נשארת `current`** (בקשת משתמש 2026-06-25) אף ש-`end_date` 2026-08-15 עבר ומ-2026-09-27 (Figma `1124:947`/`1318:487`) ההומפייג' מציג אותה ב**ארכיון** `#exhibitions`. הקולפן: `end_date` **2026-10-05** (ב-`exhibitions.json` **וגם** ב-`#g-exhibitions-data` של `galleries/medina/`); אחריו אותה שאלה — לשאול, לא להעביר לארכיון לבד.
  - העברה ל-`archived`: `status`/`status_label_en` ב-`exhibitions.json` ובעותקי `#fallback-exhibitions`; `status` ב-`#g-exhibitions-data`; "נוכחית" בשלושת תגי ה-description (`<meta name="description">`, `og:description`, `twitter:description`); ב-how-many גם `tools/seo/overrides.json['/exhibitions/how-many/'].description`; בקולפן גם תג ה-status הסטטי.
- **כל כרטיס אומן ברצועות הוא קישור** (`<a class="card is-linked" href="../../artists/<slug>/">`, נתיב `../../`, כלל-זהב 10); חריג יחיד: "racheli reuven" ב-how-many. thumbs = פורטרטים, **לא לייטבוקס** (`docs/components.md` §1.7), בלי `data-artwork-*`. ⚠️ הנתיבים `pages/exhibition.html`, `pages/opencall.html`, `pages/curators/…` שבדוקים אחרים (`docs/artist-linking.md`, `docs/components.md`, `docs/lessons.md`) מיושנים; הנכונים `exhibitions/<slug>/index.html`, `opencalls/<slug>/index.html`, `curators/korin-avraham/index.html`.
- **Casing:** `body{text-transform:uppercase}` + פטור `.heb`; ב-JSON באותיות קטנות, וזה תקין.
- **`overflow-x`:** בדפי התבנית, עמוד האוצרת ושני דפי הקול הקורא נשאר `body{overflow-x:clip}` inline, מנוטרל ע"י `site-chrome.css` (`body:not(.menu-open){overflow-x:visible !important}`). **לא להוסיף `overflow-x` על `body`**; חיתוך רק על `html` (lessons 2026-06-15/16). בקולפן: `html{overflow-x:hidden}` ו-`body{overflow-x:visible;max-width:100vw}`.
- **`<image-gallery>`** (`docs/components.md` §2): בלי `z-index`; `.overlay` שמעליו `pointer-events:none`; scrim על `::after` של `.img-frame` עם `z-index:1`.
- **רתמת הרגרסיה** (CLAUDE.md §7.1): `--only exhibitions/,curators/,opencalls/`, 🔴 אותם `--only`/`--widths` בשני הצילומים; ל-layout/טיפוגרפיה `--widths 390,1024,1366,1440`. באגי ה-family חיו בטאבלט: רמפת האימייל בקולות הקוראים (769–1100; 1024 מכסה) וכותרת המכתב בקולפן (1101–1280; להוסיף רוחב בטווח, למשל 1200).
- **SEO:** OG `og/exhibitions-<slug>-hero.jpg`, `og/opencalls-<slug>-hero.jpg`, `og/curators-korin-avraham-portrait.jpg`. JSON-LD: `ExhibitionEvent` בתערוכות, `WebPage` בקולות הקוראים, `ProfilePage`+`Person` בעמוד האוצרת. **פירורי הלחם הם של הדף בלבד** — אין פריט ל-`/exhibitions/`, `/opencalls/`, `/curators/` כי האינדקסים לא נבנו (audit 2026-07-09).
  - 🔴 **לא להריץ `tools/seo/inject.py` על אף דף ב-family, גם לא `inject.py <path>`:** הענפים `exhibitions/`, `opencalls/`, `curators/` בונים פירור לחם עם האינדקסים שלא קיימים (בניגוד להכרעת audit 2026-07-09), וה-title/description הכתובים ביד של 5 מ-6 הדפים שמורים ב-`tools/seo/overrides.json` (loneliness title+description, how-many description, שני הקולות הקוראים ועמוד האוצרת title+description) ש-inject.py מעדיף — **הקולפן לא שם**, והרצה עליו תדרוס את ה-description שלו ("…22 אמנים ואמניות…") ב-"The Peeler — הקולפן". ⚠️ עריכה ידנית של `<title>`/description באחד מחמשת הדפים = לעדכן גם `overrides.json`. בדף חדש: להעתיק בלוק `SEO:auto` מדף אחות ולערוך ביד.
  - ⚠️ **`<title>` נדרס בזמן ריצה** בחמשת הדפים ה-data-driven: בתבנית ובקולות הקוראים `title_en + ' — Zielinski & Rozen'`; בעמוד האוצרת `'KORIN AVRAHAM — CURATOR — ZIELINSKI & ROZEN ART GALLERIES'` (`.toUpperCase()`). ה-`<title>` והתיאור הסטטיים הם מה שרואים סורקים בלי JS ו-`search-index.js`. שינוי כותרת = `<title>` סטטי + בלוק ה-SEO (`og:title`, `og:image:alt`, `twitter:title`, `name` ב-JSON-LD) + `overrides.json` + השדה ב-JSON שממנו ה-renderer בונה `document.title` (ובעותקי ה-fallback); בקולפן העותקים ב-head ביד.
- **ניווט:** ה-nav ב-`components/site-chrome.js`, לא ב-`site.json`: "exhibitions" → `/#exhibitions`; "open call" → `/#opencall` בדסקטופ, `/#mobile-cta` ב-≤768 (`syncOpenCallHref`). פעיל לפי נתיב: `/exhibitions/` → `exhibitions`, `/opencalls/` או `/opencall/` → `opencall`. כשייבנה אינדקס: href ב-`site-chrome.js`, `sitemap.xml`, פירור לחם.

## תבנית התערוכה — `exhibitions/loneliness/` + `exhibitions/how-many/`

### איך זה עובד
- שני עותקים של אותה תבנית עם `data-slug` על `<html>`: `<template id="tpl-page">` + renderer IIFE שמרנדר את הרשומה ל-`<main id="page">`; ה-renderer מסיר `is-loading-data` מ-`<body>` ו-`site-chrome.js` מחכה לכך לפני חשיפת הדף.
- **הבדלים מכוונים:** `data-slug`; מטא/SEO; `line-height` של `.descblock .desc` — loneliness `1.28` (גם במובייל), how-many `1.45` בדסקטופ ו-`1.42` במובייל. שינוי CSS/renderer = לערוך אחד **ולהעביר ידנית לשני**, בלי לדרוס את ההבדלים.

### מבנה
- `.ex-hero` (אפור `#EEF0EF`): עמודת טקסט + מסגרת תמונה `492×744` (≤1100: 380, אספקט `492/744`). תגים `gallery_label_he` + `status_label_en` → `letter-heading` (`hero_letter_heading_en`; רק עם `curator_slug` וגם `hero_letter_heading_en`) → המכתב (`description_he`) → curator footer: divider `72×1` + `credit_he` מ-`curators.json` כקישור לדף האוצרת (רק עם `curator_slug` **ו-**`credit_he`).
  - בתמונה `<image-gallery data-fit="cover">` מ-`gallery_images[]` (ריק → `hero_image`; הראשונה `fetchpriority="high"`).
  - אוברליי `label_en` • `volume_en` / `title_he` / `title_en` (Solway, `--exo-title-en`), **גלוי רק בשקופית 0** (`is-hero-slide-0` לפי `gallery:change`): דסקטופ `left:90px; top:326px` (≤1100 `left:50px; top:200px; width:280px`). מובייל: התמונה קודם, full-width, scrim שטוח `rgba(27,27,27,.4)` על `::before` (`::after` מוסתר), אוברליי ממורכז; המידע אחריה על לבן.
- `.ex-artists`: רצועה אופקית, כרטיס `178×148` (מובייל `96×80`), שם אפור `#828282`. `.ex-curator`: כרטיס יחיד (פורטרט מ-`curators.json`, `object-position:50% 28%`, תווית `badge_en`) → דף האוצרת; רק עם `curator_slug`.

### שדות שהתבנית קוראת
- שדות הרשומה: `docs/data-contracts.md` §5. `title_he` (fallback `subtitle_he`), `gallery_images[{src,alt}]` (אחר מ-`{image,video,poster}` של הקול הקורא), `description_he[{weight, lines[]}]`: `weight` = `regular`/`light`/`heading-en`; `heading-en` בשורה אחת, מתכווץ ב-JS `fitExHeadingEn` מ-22px עד 9px.
- `artists[]`: `name_en` (`\n` שובר שורה, `white-space:pre-line`), `thumb`, `slug`, `artist_page_slug` (מחליף יעד קישור, לשיתופי פעולה), `focus` (`object-position`). ללא `slug`: חיפוש ב-`_ARTIST_SLUGS` בקוד, לא נמצא = `<div>` **לא-מקושר**; ללא `focus`: `_ARTIST_FOCAL` בקוד (מירור ידני של `FOCAL_POINTS` בדפי האומנים), ברירת מחדל `center 25%`. **עדיף תמיד `slug` + `focus` ב-JSON** על הרחבת הטבלאות.
- `hero_overlay_en_only:true` (how-many): האוברליי מציג רק `title_en`; title-bar ו-`title_he` מוסתרים.
- ⚠️ **`hero_overlay_hide_en` לא נתמך ברנדרר התבנית** (אין קוד ואין CSS); `.ex-hero--overlay-hide-en` רק בקולפן הסטטי, והדגל ב-JSON נקרא רק ע"י `buildCard` בעמוד האוצרת. תערוכה חדשה על התבנית עם הדגל = כותרת אנגלית מוצגת בדף ומוסתרת בכרטיס האוצרת. אם צריך: תמיכה ברנדרר וב-CSS **בשני** קבצי התבנית.
- **תמונות נוספות ל-hero** = `gallery_images[]` **וגם** `#fallback-exhibitions` בשני הקבצים (`docs/components.md` §2.8).

## `/exhibitions/loneliness/`

- 11 אומנים (`images/exhibitions/loneliness/artists/NN-<name>.webp`, לכולם `slug`). `status: archived`, `status_label_en: "previous"`, `volume_en: "VOLUME 1"`, גלריית המדינה, 2026-01-19 → 2026-05-20.
- hero gallery = 8 שקופיות: `images/exhibitions/loneliness/hero.webp` + 7 מ-**`images/events/loneliness/`** (`invite-01..03`, `atmosphere`, `second-01..03`), ב-`exhibitions.json :: loneliness.gallery_images[]` **וגם** ב-`#fallback-exhibitions` של **שני** דפי התבנית. 🔴 הקבצים שייכים לדף האירוע `events/loneliness/` (`docs/routes/events.md`); שינוי בהם (שם, מחיקה, החלפה, קרופ) שובר את הגלריה; שינוי נתיב = לעדכן את שלוש הרשימות.
- כרטיס בארכיון ההומפייג' (`.ex-archive-item`, Figma `1124:947`/`1318:487`, `images/exhibitions/archive/loneliness-card.*`), `.tribe-teaser-head`, עמוד האוצרת, `galleries/medina/`.

## `/exhibitions/how-many/`

- **15 אומנים** (`images/exhibitions/how-many/artists/NN-<name>.webp`). `hero_overlay_en_only:true`; `gallery_images` = ה-hero בלבד (`_gallery_note`: להוסיף כשיהיו צילומים). `volume_en: "VOLUME 2"`, גלריית דיזינגוף, 2026-05-26 → 2026-08-15, `status: current`.
- 🔴 **שיתוף הפעולה zohar ron × dan ben-ary:** שני הכרטיסים מקשרים ל-**`zohar-ron-dan-ben-ari`** (דף השת"פ): "zohar ron" = `slug:"zohar-ron"` + `artist_page_slug:"zohar-ron-dan-ben-ari"`; "dan ben-ary" = `slug:"zohar-ron-dan-ben-ari"`. מפורש ב-JSON; לא לשנות בלי בקשה. (ב-`events/how-many/` דן בן-ארי מקשר לדף השת"פ, זוהר רון ל-`artists/zohar-ron/`.)
- ⚠️ **"racheli reuven" (כרטיס 15) לא-מקושר** (אין `slug`, לא ב-`_ARTIST_SLUGS`) — תואם ל-`docs/artist-linking.md` §1 (placeholder). אבל יש לה יצירה (`racheli-reuven-1`, שעמודה מקשר ל-how-many), היא בגריד `/artists/` וב-sitemap, ו-`artists/racheli-reuven/` עדיין placeholder (`_pending_artist_pages`, `bio_he` = השם בלבד). **שאלה פתוחה למשתמש; לא לקשר על דעת עצמנו.** אם יוחלט: `"slug":"racheli-reuven"` ב-`exhibitions.json` ובשני עותקי `#fallback-exhibitions`, ועדכון `docs/artist-linking.md` §1.
- בהומפייג' **פעמיים**: `#exhibitions-now` תחת `berlin`, וכרטיס `.ex-archive-item` בארכיון `#exhibitions` (→ `exhibitions/how-many/`, `.ex-archive-gal` + `aria-label` = "גלריית כיכר דיזינגוף", `images/exhibitions/archive/how-many-card.{webp,avif}` +480/768w, `homepage.json :: exhibitions_archive.items[]`). וגם: עמוד האוצרת; `galleries/dizengoff/ #g-exhibitions-data`; שם הבושם ב-`#perfume-promo` (אזכור כותרת בלבד).
- ⚠️ **(2026-09-27) ברלין או דיזינגוף — טעון הכרעת משתמש.** `#exhibitions-now` מציג אותה תחת `berlin` (`the art gallery berlin`, `images/homepage/ex-now/berlin-how-many.{webp,avif}`, `homepage.json :: exhibitions_now.groups[]`; `docs/routes/homepage.md`), אך `exhibitions.json` עדיין `gallery_id:"dizengoff"` + `gallery_label_he` של דיזינגוף — ולכן כרטיס האוצרת (נגזר מ-`gallery_id`), `galleries/dizengoff/ #g-exhibitions-data`, תג ה-hero וכרטיס הארכיון באותו עמוד אומרים דיזינגוף. **לא לשנות `gallery_id`/`gallery_label_he` בלי הכרעה.** אם יוכרע ברלין: `exhibitions.json`, שני עותקי `#fallback-exhibitions`, `#fallback-exhibitions-min`, להוציא מ-`#g-exhibitions-data` של דיזינגוף, **וגם** כרטיס הארכיון בהומפייג' (`.ex-archive-gal`, `aria-label`, `homepage.json :: exhibitions_archive.items[0].gallery_id`), תגי ה-description של `exhibitions/how-many/` ("נוכחית בגלריית כיכר דיזינגוף"), ו-`tools/seo/overrides.json['/exhibitions/how-many/'].description`.

## `/exhibitions/the-peeler/` — 🔴 סטטי קפוא

### הכלל
- **2026-06-25, בקשת משתמש (חופש עיצובי מלא):** הדף "הוקפא" (נבנה במקור על how-many): אין `<template id="tpl-page">`, `fallback-*` או renderer IIFE; hero / artists / curator הם markup קבוע ב-`<main id="page">`. **התוכן לא נמשך מ-`exhibitions.json`**: שינוי טקסט, אומן או תמונה = עריכה ישירה ב-HTML. **לא להחזיר לתבנית ולא לחבר ל-JSON** בלי בקשה מפורשת.
- `data-bind*` / `data-curator-*` ב-markup הם שאריות ש**שום קוד לא קורא**; אפשר להשאיר, אין להסתמך. `<site-header>` / `<site-footer>` ריקים ו-`site-chrome.js` מרנדר אותם. `is-loading-data` **הוסר מ-`<body>`. לא להחזיר** (אין renderer שיסיר אותו, ו-`site-chrome.js` יחכה ל-timeout).
- הרשומה `the-peeler` ב-`exhibitions.json` (`status:"current"`, `status_label_en:"current"`, `volume_en:"VOLUME 2"`, `gallery_id:"medina"`, `curator_slug:"korin-avraham"`, 2026-07-29 → 2026-10-05) לא נקראת ע"י הדף אבל **נשארת ונקראת במקומות אחרים**: עמוד האוצרת (`title_*`, `label_en`/`volume_en`, `hero_overlay_hide_en`, `curator_card_image`, `gallery_id`); `ex-order.js` (דירוג בדפי האומנים); `tools/seo/inject.py` (`title_en`, `subtitle_he`, `hero_image`, `start_date`/`end_date`; ראה האיסור ב-SEO); `galleries/medina/ #g-exhibitions-data` — עותק ידני (`status`, `title_*`, `volume_en`, `start_date`/`end_date`, קרופ כרטיס `images/galleries/medina/ex-card-the-peeler.*`), שינוי תאריך/כותרת/סטטוס = לעדכן גם שם. כשמשנים את הדף, לעדכן גם את הרשומה. ⚠️ `gallery_images` ברשומה = ה-hero בלבד, בדף 7 שקופיות; הדף מקור האמת.
- `volume_en: "VOLUME 2"` / `EXHIBITION • VOLUME 2`: **זהה ל-how-many**, verbatim מ-Figma, באישור המשתמש (2026-06-25). **לא "לתקן" ל-VOLUME 3.**

### Hero
- `.hero-stack` בתוך `.img-frame` (desktop `492×744`, Figma `721:14345`): שכבת בסיס `hero-base.{webp,avif}` (620×754, `object-fit:cover`) = ה-LCP (`fetchpriority="high"`); מעליה `.hero-layer-wrap` עם **`<image-gallery data-fit="cover" data-arrows="false">` בן 7 שקופיות** (הקוד גובר על ההערה הישנה ב-CLAUDE.md ש"אין `<image-gallery>` ב-hero").
  - שקופית 0 = `hero-art.{webp,avif}` (1200×1600, +480/768/1080w) עם `hero-layer--art`: `width:146%; height:128.73%; transform:translate(-14.3%,-11.19%)` — קרופ Figma (offset `-20.88%/-14.41%` של המסגרת, יחסית לתמונה המוגדלת).
  - שקופיות 1–6 = `images/works/v2/`: `noemi-safir-2`, `elsa-ars-brush-1`, `michael-konovalenko-1`, `maria-artamonova-1`, `alice-debellis-2`, `amnon-lipkin-13`. האוברליי גלוי **רק בשקופית 0** (סקריפט inline בסוף הדף מחליף `is-hero-slide-0` לפי `gallery:change`).
- **הוספת שקופית** = `<img>` בתוך ה-`<image-gallery>` ב-HTML כמו השכנים: `srcset`/`sizes` (480/768/1080 + avif), `width`/`height`, `loading="lazy" decoding="async"`. **לא** `gallery_images[]` ולא `docs/components.md` §2.8.
- scrim בדסקטופ `linear-gradient(0deg, rgba(0,0,0,.7), transparent)`; במובייל `rgba(27,27,27,.4)` שטוח. `hero.{webp,avif}` (492×744) = קומפוזיט שטוח, רק ל-`hero_image` ול-`image` ב-JSON-LD.
- ⚠️ **OG:** `og/exhibitions-the-peeler-hero.jpg` הוא **801×974 ונאפה מ-`hero-base`** (צילום הקולפן-מטבח האדום), **לא** מהקומפוזיט. `tools/seo/og-dims.json` רושם 801×974, אבל ב-`<head>` `og:image:width`/`og:image:height` = 492/744. פתוח: לשאול את המשתמש איזו תמונה. **לא לאפות מחדש ולא לשנות מטא על דעת עצמנו.**
- **אוברליי** (Figma `721:14346`): ממורכז (`top:50%`, רוחב 313px): title-bar `EXHIBITION • VOLUME 2` (Copperplate Light 26px, ≤1100 20px, מובייל 22px) + `הקולפן` (FbEzmel 29px, ≤1100 ומובייל 24px). **בלי הכותרת האנגלית:** `.ex-hero--overlay-hide-en` עם `.overlay .title-en{display:none}` + `hero_overlay_hide_en:true` ב-JSON. `title_en: "The Peeler"` רק ל-`<title>`, OG ו-SEO.

### טקסט
- **letter heading** ("letter from the exhibition curator"): דסקטופ (≥1101, `white-space:nowrap`) 32px בשורה אחת, inset שמאלי 24px; `fitLetterHeading` מכווץ **עד מינימום 26px**, ואם לא נכנס — חוזר לגודל ה-CSS ומוסיף `.is-wrapped` (`white-space:normal; text-wrap:balance`); הסקריפט מתחיל באיפוס (מסיר `.is-wrapped` ו-`font-size` inline) ורץ רק כש-`white-space` המחושב `nowrap`. ≤1100: 30px, `white-space:normal`, `text-wrap:balance`. מובייל: 22px/1.42.
  - 🔴 **בלי `overflow:hidden` על הכותרת (היום `overflow:visible`), ולא להוריד את הסף מתחת ל-26px** (ב-2026-09-27 הכותרת נקטעה ברוחבי 1101–1280 בגלל שני אלה).
- **המכתב:** הפסקה הראשונה `heading-en` "welcome aboard." (Copperplate Light 18px, מובייל 16px; Figma `721:14337`). אומר "עשרים ושניים אמנים" (תואם ל-22 הכרטיסים), וכך `<meta name="description">`, `og:description`, `twitter:description` ("22 אמנים ואמניות"). הוספה/הסרה של אומן → **לשאול** אם לעדכן את המכתב ושלושת תגי המטא.
- **curator footer:** "אוצרת התערוכה - קורין אברהם" → `../../curators/korin-avraham/`. סקשן האוצרת כמו בתבנית: כרטיס קורין, תווית "the curator", פורטרט `images/curators/korin-avraham/portrait` עם srcset 480w.

### רצועת האומנים — 22 כרטיסים
- **הסדר = Figma desktop `980:92` verbatim:** zohar-ron, noemi-safir, elsa-ars-brush, anat-wegier, yarden-amir, nir-giorgio-levin, jessica-tabarovsky, chen-ziv, baruch-torgeman, gilad-kenan, lahav-barak, livay-levi, natasha-zeriker, talia-zoref, aharon-bas, bar-cohen, amnon-lipkin, alice-debellis, maria-artamonova, michael-konovalenko; **אחריהם hadas-tuval ואז tali-zelnik** (נחשפה 2026-07-26, בסוף).
- **thumbs:** כולם חוץ מ-hadas-tuval ממחזרים `images/artists/grid/<slug>.{webp,avif}` (+480w), `object-position:50% 40%`. **hadas-tuval**: `images/exhibitions/the-peeler/artists/hadas-tuval.{webp,avif}` (356×356, Figma node `980:175`), `50% 45%`.
- כל הכרטיסים `<a class="card is-linked">`; השמות עם שבירת שורה אמיתית ב-`.name` (`white-space:pre-line`), למשל "nir giorgio⏎levin".
- **הוספת כרטיס:** להעתיק בלוק `<a class="card is-linked">` קיים (`<picture>`, `<source type="image/avif">`, `data-pic-done="1"`). `.name` **וגם** `aria-label="לדף האומן <name>"` = השם **באנגלית lowercase** עם שבירת שורה אמיתית (`hadas⏎tuval`), לא עברית. במקביל `artists[]` ב-`exhibitions.json` — העתק פריט אחות (`{name_en, thumb, slug, focus}`, `name_en` עם `\n`). לעדכן את המספר בכותרת הסקשן, ולשאול על המכתב ושלושת תגי המטא.
- 🔴 **amnon-lipkin נשאר ברצועה** (דף האומן `artists/amnon-lipkin/` קיים, יצירה שלו בהירו). מה שנמחק ב-2026-08-28 הוא **דף האירוע** `events/amnon-lipkin/`, לא האומן.

## `/curators/korin-avraham/`

### איך זה עובד
- fetch-first ל-`curators.json`, `exhibitions.json`, `galleries.json`; fallbacks `#fallback-curators`, `#fallback-exhibitions-min`, `#fallback-galleries`. האוצרת נבחרת לפי `CUR_SLUG = 'korin-avraham'` בקוד.
- `#fallback-galleries` = `data/galleries.json` verbatim (**`sync_data.py`**). `#fallback-curators` ו-`#fallback-exhibitions-min` **ביד**: `-min` רק `id, slug, label_en, volume_en, title_he, title_en, gallery_id, hero_image, description_he`, + דגלי האוברליי ו-`curator_card_image` כשיש. שינוי בשדות האלה או תערוכה חדשה ב-`exhibition_slugs` = לעדכן גם כאן.

### Hero (Figma `314:30`–`314:42`)
- **דסקטופ:** פס אפור, גריד `1fr 492px`; עמודת טקסט: badge `badge_en` ("the curator") → שם (`name_en_first` Bold / `name_en_last` Light) → IG `@`+`instagram_handle` → ביו. מימין פורטרט ריבועי `492×492` (`object-position:50% 32%`), `images/curators/korin-avraham/portrait.webp` (1507×2000, +480w; node `314:122`) = ה-LCP.
- **ביו** (`bio_he`: מערך פסקאות, כל אחת מערך שורות; Figma desktop `706:2`): FbEzmel Light, קו אנכי `#D8D8D8` בצד ימין (`706:5`). `{en}…{/en}` בשורות הופך ל-`<span class="ltr-en">` (Copperplate, LTR) — כך מסומן "YA SALAM"; לשמור בעריכה.
- **מובייל** (Figma `314:97`, `706:10`): badge → פורטרט (scrim `rgba(0,0,0,.6)`→0) → שם ו-IG → ביו בסקשן לבן full-bleed (עד 358px). `.cur-hero__copy` עם `display:contents` כדי לאפשר `order`.

### כרטיסי התערוכות (`section_heading_en` = "the curator's exhibitions")
- לפי **`curators.json :: exhibition_slugs`**; סדר loneliness, how-many, the-peeler (דסקטופ משמאל לימין). כרטיס → `../../exhibitions/<slug>/`. מסגרת `736.97px` בדסקטופ, 560 ב-≤1100, `433.939px` במובייל (עד 358). scrim `linear-gradient(0deg, rgba(0,0,0,.7), transparent)`.
- **אוברליי לפי דגלים:** `hero_overlay_en_only` (how-many): ערימת השורות מהפסקה `heading-en` ב-`description_he` (Solway 26px; שינוי הפסקה משנה גם את הכרטיס). `hero_overlay_hide_en` (הקולפן): title-bar + עברית בלי אנגלית, וגם כותרת ה-meta מתחת לכרטיס **בעברית**. אחרת (loneliness): title-bar + עברית + אנגלית. הרוחב `min(400px, calc(100% - 32px))` (Figma 400) חל על כל אוברליי שאינו en-only, גם הקולפן.
- **שם הגלריה** = `name_en` מ-`galleries.json` לפי `gallery_id`. **תמונת הכרטיס** = `curator_card_image` אם קיים, אחרת `hero_image`; לקולפן `images/exhibitions/the-peeler/curator-card.{webp,avif}` (822×1243, +480w). ⚠️ **`width`/`height` כתובים בקוד:** loneliness 690×1044; כל השאר 1068×1600; עם `curator_card_image` 822×1243, srcset רק 480w. תערוכה חדשה במידות אחרות = לעדכן `buildCard`, אחרת CLS.
- **מובייל:** עמודה אחת, **`.cur-card--how-many{order:-1}`** מעלה את how-many לראש (how-many → loneliness → the-peeler). ⚠️ נכתב כשהיו 2 כרטיסים לפי Figma `314:97` (קדם לקולפן); לא אומת מול פריים עדכני אם הקולפן אמור להיות ראשון במובייל.

### דאטה כפולה (ביד)
- `instagram_handle` (`yasalamfashionblog`) גם ב: `docs/routes/about.md`; קישור קשיח בגוף `press/walla/`; `#fallback-curators` (שני דפי התבנית + עמוד האוצרת); JSON-LD של עמוד האוצרת (`Person.sameAs` = `https://www.instagram.com/yasalamfashionblog/`). שינוי = לעדכן הכול.
- `contact_email` (`korinalove5@gmail.com`) גם ב-`opencalls.json :: contact.email` (+ עותקי `#fallback-opencalls`) וב-`mailto` ביד בכל `works/<id>/` (`docs/routes/works.md`); שינוי = לעדכן הכול ולכייל מחדש את רמפת האימייל בטאבלט (`.oc-hero`).
- `credit_he` ("אוצרת התערוכה - קורין אברהם") נקרא ע"י דפי התבנית, ולכן חייב להופיע ב-`#fallback-curators` שלהם.

## תבנית הקול הקורא — `opencalls/{obsession,the-peeler,how-many}/`

### איך זה עובד
- שלושת הקבצים זהים פרט למטא/SEO ו-`data-slug`; renderer IIFE קורא `opencalls.json` ו-`site.json` ומרנדר ל-`<main id="page">` ("loading…" עד הרינדור). CSS/renderer = לערוך אחד ולהעביר ידנית לשני האחרים (+ harness עם `--only opencalls/`).

### מבנה
- **`.oc-hero` אפור:** טקסט RTL ומסגרת תמונה `492×744` (≤1100 `380×560`).
  - 🔴 **טאבלט 769–1100 (בשני הקבצים, 2026-09-27):** ב-`@media (min-width:769px) and (max-width:1100px)`: `.oc-hero .text-col{min-width:0}` + `.oc-hero .block .text .email{font-size:clamp(14px,calc((100vw - 552px) / 16.1),18px)}`. האימייל הוא מילה אחת ב-Copperplate שלא נשברת (≈16.1em) ובלי הכלל דוחף את מסגרת התמונה מחוץ למסך. **לא להסיר `min-width:0` ולא להרחיב את הרמפה מחוץ לטווח** (1440 לא זז). החלפת כתובת = למדוד מחדש את 16.1. עמודת טקסט חדשה עם `flex:1` צריכה `min-width:0` (lessons 2026-09-27).
  - scrim `linear-gradient(0deg, rgba(0,0,0,.35), transparent 60%)`; במובייל אין scrim והתמונה עולה לראש (`order:-1`).
  - תגים `submission_status_he` (אפור) + `gallery_label_he`; כותרת `title_html` (24px; במובייל `clamp(18px,4.8vw,24px)` + `nowrap`); `description_he` (`weight` `regular`/`light`); אחריהם בלוקים מופרדים ב-divider של 72px: [מעוררי רגש] → הנחיות הגשה → יצירת קשר.
- 🔴 **`title_html` ו-`submission_instructions_he.intro_html` מוזרקים כ-HTML גולמי, בלי escape** (`<span class="heb">`/`<span class="lat">`; חייב להיות HTML תקין). the-peeler: `<span class="heb">הקולפן</span> | <span class="lat">exhibition volume 2</span>`; how-many: `<span class="lat">how many partners have you had?</span>`.
- **`emotional_triggers`** (the-peeler בלבד; ב-how-many `null` והבלוק וה-divider לא מרונדרים): `title_he` ואחריו `lines[]`, כל שורה `<p class="trigger-line">`, ו-` | ` הופך ל-`.sep` אפור; `items[]` = הרשימה הלוגית, רק כשאין `lines`. במובייל רקע `#FAFAFA`, full-bleed.
  - 🔴 **`lines[]` = שבירות השורות של Figma verbatim** (`XhGH...::119:2587`): פריט יכול להישבר בין שורות בלי מפריד ("…| פחד להישאר לבד רציתי" / "יותר ממה שנתנו לי | …"), ו"פחד מקרבה בהמתנה" הם שני פריטים בלי מפריד. **לא להוסיף ` | ` ולא לשבור מחדש.**
- **יצירת קשר:** `contact.label_he`; האימייל ב-Copperplate UPPERCASE ו-`mailto` באותיות קטנות; `deadline_label_he` + `deadline_he` (Copperplate, `direction:ltr`); `note_he` באפור.
- **Hero srcset:** מ-`hero-{480,768,1080}w.webp` + `hero.webp`. 🔴 המידות הטבעיות בטבלת `HERO_DIMS` בקוד (`obsession` 1080×1350, `the-peeler` 1601×2000, `how-many` 1600×2000), **בשלושת הקבצים**; קול קורא חדש = שורה ב-`HERO_DIMS` בכולם + וריאנטים (+avif), אחרת אין `width`/`height`.
- **גלריה (`gallery_images[{image, video, poster}]`)** — the-peeler בלבד; ב-how-many `null`:
  - **דסקטופ `.oc-gallery`:** מסגרות `492×744`, צמודות לימין, `gap:48`. פריט `video` מתנגן **inline בכרטיס** (`data-artwork-skip`, הלייטבוקס מדלג); פריט תמונה נפתח ב-artwork-lightbox (scope `opencall-<slug>`). כפתור play: עיגול 72px `rgba(217,217,217,.4)` עם משולש (Figma `119:2495`).
  - **מובייל:** `.stacked-gallery.sg-mode-lightbox` (scope `opencall-<slug>-mobile`); וידאו inline דרך `stacked-gallery.js`. אחרי הזרקה: `ArtworkLightbox.refreshFocusable()` ו-`StackedGallery.refresh()`.
  - שני הפריטים וידאו: `images/opencalls/the-peeler/gallery-0{1,2}.{mp4,webp,avif}` + `-poster.webp`. ⚠️ `docs/components.md` §3.5 ("וידאו + `sg-mode-lightbox` = לא יציג") לא חל כאן כי הווידאו `data-artwork-skip`; לא להסיר את ה-skip.

### וריאנט light — obsession (`theme:"light"`, Figma `1906:664` / `1906:587`)
- `oc.theme === "light"` ⇒ `.oc-hero.is-light`; הכללים בבלוק ה-CSS "LIGHT THEME" (אחרי בלוק המובייל, כדי שה-media שלו יגבר).
- רקע לבן (לא `--bg-grey`), בלי scrim; `line-height:1.06` (ה-auto של FbEzmel בפיגמה); מרווח פסקה = שורה ריקה (`1lh`); dividers של 72px בשני ה-breakpoints (דסקטופ inset 16 מימין; מובייל `#EFEFEF`). דסקטופ: קצב 24px (סטטוס→כותרת 32), בלוקים ברוחב 390 (`Gallery Note Container`). מובייל: קצב 32 (סטטוס→כותרת 24, כותרת→טקסט 16), בלוקים בלי padding. נמדד מול הרינדור: סטיות ≤5px.
- תג הסטטוס בדיו (לא אפור) כש-`status==="open"` (`.badge.status.is-open`) — גנרי לכל קול קורא פתוח.
- שדות אופציונליים גנריים ברנדרר (`docs/data-contracts.md` §8): `hero_mobile_ratio` (באנר מובייל 390/520), `submission_instructions_he.lead_he` (`.block.follow`, בלי divider), `.items_html` (HTML גולמי — `PDF` ב-`.lat`), `.bullet:"disc"` (•), `contact.intro_he[]`, `contact.deadline_first`, `contact.label_html`.
- תאריך הדדליין = FbEzmel (כמו בפיגמה), לא Copperplate; `deadline_he` = `22.10.2026` (נקודות). 🔴 שינוי דדליין נוגע גם ב: הפוסטר (התאריך צרוב בתמונה — `hero-v2` + כרטיס ההומפייג' `obsession-card-v2`; גרסה חדשה = `-v3`, כלל-זהב 8), `homepage.json :: mobile_cta.info` + שלושת התאריכים ב-`index.html` (`data-info-date`, `.oc-info .dt`, `.info .date`), `#fallback-opencalls` בשלושת הקבצים, התיאור ב-meta/OG/JSON-LD + `tools/seo/overrides.json`, ותמונת ה-OG (`og/opencalls-obsession-hero-v2.jpg`).
- srcset של ה-hero מסנן וריאנטים ברוחב >90% מהמקור (ל-obsession, 1080×1350, אין `-1080w`). מקור גולמי: `_originals/opencalls/obsession/` (הפוסטר הנוכחי: `hero-v2-figma-1906-715.png`).

### דאטה
- `opencalls.json`: `status` (the-peeler ו-how-many `archived`; obsession `open`), `submission_status_he` ("ההגשה נגמרה"), `deadline`/`deadline_he`, `gallery_id`/`gallery_label_he`, `hero_image`, `card_image`, `contact`, `figma_node_*`. `card_image` (`images/opencalls/<slug>-card*.webp`) לא משמש את הדפים אלא את כרטיסי ההומפייג' (`#opencall` / `#mobile-cta`, `docs/routes/homepage.md`).
- **obsession:** ראשונה במערך (חדש→ישן). **הסטטוס ידני** — אחרי הדדליין (22.10.2026) לשאול את המשתמש לפני `archived` (+ `submission_status_he` "ההגשה נגמרה"; התג חוזר לאפור אוטומטית; הרשימה המלאה: `docs/todo.md`).
- שינוי ב-`opencalls.json` = לעדכן ביד `#fallback-opencalls` ב**שלושת** הקבצים (`sync_data.py` לא מטפל). קול קורא חדש: העתק רשומת אחות (קודם `docs/data-contracts.md` §8), **בראש המערך**, גם בכל עותקי `#fallback-opencalls`, + שורה ב-`HERO_DIMS`.

## נקודות מגע: הוספת תערוכה או שינוי בה

כולם נבדקים כשמוסיפים תערוכה או משנים כותרת, תאריכים, סטטוס או תמונה. הליך כללי (sitemap, OG, `sync_data.py --check`): CLAUDE.md §7.

1. **`data/exhibitions.json`:** תערוכה חדשה **בסוף המערך** (כרונולוגי עולה, מקור "החדשה למעלה" בדפי האומנים); הרשומה = העתק אחות ועריכה (`docs/data-contracts.md` §5). 🔴 `hero_overlay_en_only` (how-many), `hero_overlay_hide_en` ו-`curator_card_image` (the-peeler) הם הכרעות של תערוכה אחת — **לא להעתיק**; האחות הנקייה = `loneliness`. אחר כך **`python3 tools/sync_data.py`** (מייצר `data/generated/ex-order.js`).
   - 🔴 **רזידנסי או פופ-אפ אינו תערוכה** (SUMII, רזידנסי מלאני הקימוגלו וכו'): לא להוסיף ל-`exhibitions.json`. המערך הוא מקור `data/generated/ex-order.js` (נטען בכל דפי האומנים חוץ מ-alon, dan-ben-ary, zohar-ron-dan-ben-ari), ויצירות שיפנו לרשומה כזו ידורגו כ"תערוכה" החדשה ביותר — מעל הקולפן. כרטיס רזידנסי SUMII (`kind:"residency"`, `route:"sponsors/sumii/"`) חי **רק** ב-`#g-exhibitions-data` של `galleries/dizengoff/` ובהומפייג' (`homepage.json :: exhibitions_now.groups[]`); רזידנסי מלאני חולק איתו את `sponsors/sumii/`. יצירות רזידנסי ב-`works.json`: `kind:"residency"`, `exhibition_slug:null` (תמיד מתחת לתערוכות). ראה `docs/data-contracts.md`, `docs/routes/galleries.md`.
2. **הדף עצמו:** עותק של התבנית (how-many) עם `data-slug`, או דף סטטי כמו הקולפן (לשאול איזה). בגרסת התבנית הרשומה נכנסת ל-`#fallback-exhibitions` של החדש ושל שני הקיימים.
3. **עמוד האוצרת:** `curators.json :: exhibition_slugs` **וגם** ב-`#fallback-curators`; הרשומה ב-`#fallback-exhibitions-min` (העתק שכנה; דגלי שלב 1 רק אם הוכרעו לחדשה); מידות הכרטיס ב-`buildCard`; כלל ה-`order` במובייל.
4. **דף הגלריה:** `#g-exhibitions-data` (ביד — העתק תערוכה שכנה; לא של `sumii` בדיזינגוף, ש-`kind:"residency"` שלה מרנדר כרטיס רזידנסי), ובמדינה גם קרופ כרטיס (`docs/routes/galleries.md`).
5. **הומפייג':** `#exhibitions-now`, הארכיון `#exhibitions` (`homepage.json :: exhibitions_archive.items[]`), כרטיסי הקול הקורא (`docs/routes/homepage.md`). **יצירות:** `exhibition_slug` / `exhibition_title_he` / `exhibition_route` ב-`works.json :: art_works[]` ו-`exhibition_statements[]`, ואז `sync_data.py` (`docs/routes/works.md`, `docs/routes/artists.md`).
6. **רתמה:** בשינוי מכוון תחזיר exit 1 — לוודא שההבדלים הם הצפויים בלבד (הכרטיס/הרשומה החדשים בעמוד האוצרת, בדף הגלריה ובהומפייג'); להרחיב `--only` (למשל `galleries/`; ההומפייג' = `index.html`). דף חדש מסומן `only in after` — צפוי.
7. **קישורים, כותרות ותוויות קשיחים ב-HTML** (לא נגזרים מ-`exhibitions.json`): דפי האירוע — פסי `presented as part of` / `EXHIBITION • VOLUME 2` + "הקולפן" במשפחת artist-talk (`docs/routes/events-talks.md`), `events/gala-night/`, `events/how-many/`, `events/loneliness/`, `events/close-look/`, `events/artist-talk/` (`docs/routes/events.md`); הכתבות `press/the-last-station/`, `press/manicure-against-darkness/`, `press/peeling-a-layer/`, `press/the-shared-list/`; `sponsors/soos/`; `exhibition_id` ב-`events.json` וב-`press.json`.
   - בשינוי כותרת/תווית: `grep -rl 'exhibitions/<slug>' --include=index.html .` **וגם** grep על מחרוזת הכותרת (`events/loneliness/` לא מקשר ל-`exhibitions/loneliness/` אך כותב "בדידות"). תוצאות ב-`works/*` מגיעות מ-`#artwork-data` (`sync_data.py`) — לא ביד. **חריג: `works/livay-levi-3/`**, ש-`description`/`og:description`/`twitter:description` בו ביד ומזכירים "בתערוכת הקולפן". (ה-slug לא משתנה — כלל-זהב 6.)

## בעיות פתוחות

מחכות להכרעת משתמש/מעצבת (פירוט בסקשנים): racheli reuven (how-many; לא ב-`docs/todo.md`); סטטוס how-many/הקולפן (Shared rules); ברלין או דיזינגוף (how-many); OG של הקולפן (Hero; לא ב-`docs/todo.md`); סדר הכרטיסים במובייל בעמוד האוצרת.
- ⚠️ **הביו של קורין ב-`curators.json` כולל טקסט ספציפי ל-loneliness** ("מכלול העבודות בתערוכה מהוות עבור אברהם סקלה של בדידות…") — אותה בעיה כמו ב-`docs/todo.md` לגבי עמוד האודות. **לא לשנות** עד הכרעת המעצבת.
- ⚠️ meta description / OG של עמוד האוצרת מזכיר רק "בדידות" ו"כמה שותפים היו לך?", לא את הקולפן; לא ב-`docs/todo.md`.
- `exhibitions.json :: archive_thumbnails` ו-`thumbnails: []` הם דאטה מתה (אין קורא; הארכיון בהומפייג' = שני כרטיסים סטטיים ב-`homepage.json :: exhibitions_archive.items[]`, `thumbs_ref` הוסר). פריט ה-todo "Dizengoff archive thumbs" מפנה ל-`#fallback-archive` ב-`index.html`, שלא קיים — מיושן.

## Removed / do not restore

- **הקולפן:** `<template id="tpl-page">`, `#fallback-site` / `#fallback-curators` / `#fallback-exhibitions`, ה-renderer IIFE ו-`is-loading-data` על `<body>` הוסרו ב-2026-06-25 (בקשת משתמש). לא להחזיר data-driven בלי בקשה.
- **הסתרת tali-zelnik מהרצועה** (`_staging`, 404) **בוטלה** ב-2026-07-26 (היא בסוף הרצועה); **כרטיס hadas-tuval לא-קליקאבילי בוטל** ב-2026-07-06 (`<a class="card is-linked">` + `slug`). לא להחזיר.
- **"בתוך בסביבה"** בכותרת loneliness: טעות מוכרעת. לא לשחזר.
- **קישורי תערוכה ל-`opencalls/<slug>`** מעמודי יצירות: הוחלפו ב-`exhibition_route` → `exhibitions/<slug>`. לא לחזור לנתיב הקשיח.
- **נתיבים ישנים** `pages/exhibition.html?id=…`, `pages/opencall.html`, `pages/curators/korin-avraham.html`: לא קיימים. אל תבנה מהם ואל תקשר אליהם.
