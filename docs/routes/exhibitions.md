# Exhibitions, curator & open calls — route notes

> לקרוא לפני עריכה של `exhibitions/*/index.html`, `curators/korin-avraham/index.html` או `opencalls/*/index.html`, וגם לפני שינוי ב-`data/exhibitions.json`, `data/curators.json` או `data/opencalls.json`, או בתמונות `images/events/loneliness/{invite-01..03,atmosphere,second-01..03}` (גלריית ה-hero של `exhibitions/loneliness/`). המסמך מתאר את המצב הנוכחי ואת הכללים הפעילים. ההיסטוריה נמצאת ב-`docs/history/CLAUDE-2026-09-27.md` §4.

## Pages

- `/exhibitions/` (אינדקס) → ⏳ לא נבנה, ואין לו עיצוב. בפועל האינדקס הוא הארכיון בהומפייג' (`#exhibitions`, ראה `docs/routes/homepage.md`).
- `/exhibitions/loneliness/` → `exhibitions/loneliness/index.html` · ✅ data-driven מהתבנית
  - Figma desktop `XhGH...::119:156` · mobile `XhGH...::119:331`
- `/exhibitions/how-many/` → `exhibitions/how-many/index.html` · ✅ data-driven מהתבנית
  - Figma desktop `XhGH...::119:435` · mobile `XhGH...::119:642`
- `/exhibitions/the-peeler/` (הקולפן, גלריית כיכר המדינה, אוצרת קורין אברהם) → `exhibitions/the-peeler/index.html` · ✅ **סטטי קפוא** (עריכה ידנית ב-HTML)
  - Figma desktop `XhGH...::721:14300` · mobile `XhGH...::721:14513`
- סקשן האוצרת בתוך דף תערוכה (מתחת לאומנים): Figma desktop `XhGH...::301:2` · mobile `XhGH...::119:702`.
- `/curators/korin-avraham/` → `curators/korin-avraham/index.html` · ✅ data-driven
  - Figma desktop `XhGH...::314:4` · mobile `XhGH...::314:97` · תמונת הפרופיל `XhGH...::314:122`
- `/opencalls/` (אינדקס) → ⏳ לא נבנה, ואין לו עיצוב.
- `/opencalls/the-peeler/` → `opencalls/the-peeler/index.html` · ✅ data-driven
  - Figma desktop `Zn3N...::1213:2417` · mobile `Zn3N...::1213:2518`
  - רשימת מעוררי הרגש (שבירות השורות): `XhGH...::119:2587`
- `/opencalls/how-many/` → `opencalls/how-many/index.html` · ✅ data-driven
  - Figma desktop `Zn3N...::1213:2340` · mobile `Zn3N...::1213:2263`
- קישורי Figma מלאים: `FIGMA_LINKS.md` § "תערוכות יחידות", "אוצרת — קורין אברהם", "קולות קוראים". ⚠️ שם הסקשן שם הוא `/opencall/:slug`, אבל ה-route בפועל הוא `opencalls/` (ברבים).

## מפת הדאטה (מי קורא מאיפה)

| דף | מקור התוכן | עותקים inline (file://) | מי מתחזק את העותק |
|---|---|---|---|
| `exhibitions/loneliness/`, `exhibitions/how-many/` | fetch ל-`data/exhibitions.json` + `site.json` + `curators.json` | `#fallback-exhibitions`, `#fallback-site`, `#fallback-curators` | **ביד** |
| `exhibitions/the-peeler/` | **ה-HTML עצמו**. אין fetch ואין JSON | — | — |
| `curators/korin-avraham/` | fetch ל-`curators.json` + `exhibitions.json` + `galleries.json` | `#fallback-curators`, `#fallback-exhibitions-min` (ביד) · `#fallback-galleries` | ביד · **`sync_data.py`** |
| `opencalls/the-peeler/`, `opencalls/how-many/` | fetch ל-`data/opencalls.json` + `site.json` | `#fallback-opencalls`, `#fallback-site` | **ביד** |

- ב-http ה-JSON גובר. העותק ה-inline משמש רק כשהדף נפתח ב-file://.
- `python3 tools/sync_data.py` נוגע בדפים האלה **רק** ב-`#fallback-galleries` של עמוד האוצרת. אסור לערוך אותו ביד.
- כל שאר העותקים ב-family הזה מתוחזקים ביד (Mirror registry ב-`docs/data-contracts.md`). שינוי ב-JSON מחייב לעדכן גם אותם, אחרת file:// מציג תוכן ישן.
- 🔴 **כל עותק מכיל את כל הרשומות, לא רק את זו של הדף:**
  - `#fallback-exhibitions` בשני דפי התבנית מכיל את loneliness **וגם** את how-many.
  - `#fallback-opencalls` בשני דפי הקול הקורא מכיל את the-peeler **וגם** את how-many.
  - לכן שינוי ברשומה אחת = עדכון בשני הקבצים.
- 🔴 **`#fallback-site` — מה חייב להישאר בעותק:**
  - **בדפי התבנית (loneliness/how-many):** `footer.newsletter` (`title`/`placeholder`/`cta`) ו-`footer.links_he`. הרנדרר ניגש ל-`site.footer.newsletter.*` ול-`site.footer.links_he.slice()` בלי בדיקה. הוא קורא גם `site.footer.copyright`; אם הוא חסר הדף לא קורס, אבל הערך יוצא `undefined`.
  - **בדפי הקול הקורא:** הרנדרר קורא רק `site.footer.links_he || []`, ולכן מספיק ש-`site.footer` יתקיים.
  - אם מקצצים את העותק מעבר לזה, הדף קורס ב-file://. (הפוטר עצמו מרונדר ע"י `site-chrome.js`, אבל הקריאה נשארה בקוד.)
- drift ידוע ולא מזיק (אין צורך לתקן):
  - בעותקים חסרים שדות שהרנדרר לא קורא (`start_date`, `figma_node_*`, `bio_he` וכו').
  - ב-`#fallback-exhibitions` של loneliness, לרשומת how-many יש `start_date:null` ו-`end_date:null`.
  - ב-`#fallback-curators` של שני דפי התבנית, `exhibition_slugs` = `["loneliness","how-many"]` (בלי the-peeler). התבנית לא קוראת את השדה, ולכן זה לא מזיק.

## Shared rules

- **כותרת loneliness הרשמית = "בדידות בתוך סביבה תוססת"** (audit 2026-07-09). אם בפיגמה עדיין כתוב "בתוך בסביבה", זו טעות מוכרעת. **לא לשחזר.**
  - ⚠️ **הכותרת הרשמית חלה על `exhibitions.json` ועל הדפים, לא על מפתחות הקבוצה ב-`works.json`.** ב-`art_works[].exhibition_title_he` וב-`exhibition_statements[].exhibition_title_he` כתוב "בדידות בסביבה תוססת" (בלי "בתוך"), כולל תת-הקבוצות ("… | don’t lose your head", "… | ״ערכת בדידות״", "… | כְּתוּבָּה | QTUBA"). זה מפתח ה-join בין יצירות לסטייטמנטים, והוא גם כותרת הקבוצה בדפי האומנים. **לא "לתקן" רשומה בודדת.** שינוי = כל הרשומות בשני המערכים יחד, ואז `python3 tools/sync_data.py` (ראה `docs/data-contracts.md`).
- **איות אנגלי קנוני** (הכרעת משתמש): "adi duek" ו-"zohar shitrit". ה-slugs נשארים `adi-duak` ו-`zohar-shtrit` (כלל-זהב 6). אותו עיקרון לשאר הכרטיסים: השם המוצג לא חייב להתאים ל-slug. דוגמאות: "gal pollak" → `gal-polk`, "samy d." → `sami-david` (⚠️ ב-`exhibitions.json` ובעותקי `#fallback-exhibitions` הרווח הוא U+00A0, כלומר `samy\u00A0d.`. grep עם רווח רגיל לא ימצא אותו. לא להחליף לרווח רגיל בלי לבדוק את שבירת השורה בכרטיס), "risa brooke oze" → `risa-oz`, "alon manjoch" → `alon`, "tal holy kadosh" → `holy-kadosh`, "elsa ers brosh" → `elsa-ars-brush`, "liel salman noam" → `liel-salman`.
- **`exhibition_route` של כל יצירות הקולפן ב-`works.json` = `exhibitions/the-peeler`** (לא `opencalls/the-peeler`). עמודי `works/<id>` בונים את הקישור לתערוכה מ-`w.exhibition_route`, ולא מנתיב קשיח. ⚠️ ב-`FIGMA_LINKS.md` עדיין כתוב "`opencalls/the-peeler`" בשני מקומות, ושניהם מיושנים: בסקשן דפי האומנים של הקולפן, ובסקשן ההומפייג' ("כרטיס הקולפן … →`opencalls/the-peeler/`"; היום הכרטיס ב-`#exhibitions-now` מקשר ל-`exhibitions/the-peeler/`).
- **סטטוס התערוכה ידני:** `status` / `status_label_en` ב-JSON, ובקולפן גם התג הסטטי ב-HTML. אין אוטומציה לפי תאריך.
  - **how-many נשארת `current`** (בקשת משתמש: לא הועברה לארכיון כשנפתח הקולפן).
    - ⚠️ מ-2026-09-27 (Figma `1124:947`/`1318:487`) ההומפייג' כבר מציג את how-many ב**ארכיון** `#exhibitions`, בעוד `exhibitions.json` והתג בדף אומרים `current`. ההכרעה מ-2026-06-25 כבר לא תואמת להומפייג'.
  - ⚠️ נכון ל-2026-09-27: how-many (`end_date` 2026-08-15) הסתיימה ועדיין מסומנת `current`. הקולפן: `end_date` **2026-10-05** (עודכן 2026-09-27 ב-`exhibitions.json` **וגם** ב-`#g-exhibitions-data` של `galleries/medina/`), ולכן עדיין פעילה בצדק; אחרי 2026-10-05 היא תהיה באותו מצב כמו how-many — לשאול, לא להעביר לארכיון לבד. **לא לשנות `status`/`status_label_en` בלי הכרעת משתמש.**
  - אם יוחלט להעביר תערוכה ל-`archived`, לעדכן: `status`/`status_label_en` ב-`exhibitions.json` ובעותקי `#fallback-exhibitions`, את `status` ב-`#g-exhibitions-data` של דף הגלריה, ואת המילה "נוכחית" בשלושת תגי ה-description (`<meta name="description">`, `og:description`, `twitter:description`). ב-how-many גם את `tools/seo/overrides.json['/exhibitions/how-many/'].description`. בקולפן גם את תג ה-status הסטטי ב-HTML.
- **כל כרטיס אומן ברצועות הוא קישור** (`<a class="card is-linked" href="../../artists/<slug>/">`, כלל-זהב 10). הנתיבים יחסיים לעומק 2 (`../../`). חריג יחיד היום: "racheli reuven" ברצועת how-many (placeholder, מחכה להכרעת משתמש; ראה סקשן how-many).
  - ⚠️ **נתיבים מיושנים בתיעוד.** הדוגמאות במקומות האלה מתייחסות ל-`pages/exhibition.html`, `pages/opencall.html` ו-`pages/curators/…`:
    - `docs/artist-linking.md`.
    - `docs/components.md` §1.7 ("ב-`exhibition.html` thumbs של artists…"), §1.8, §2.7, §3.8 (טבלאות ה"שילובים").
    - `docs/lessons.md`: הפריט על `exhibitions` ב-nav (כתוב שם שהוא מצביע ל-`pages/exhibition.html?id=loneliness`; בפועל `/#exhibitions`), פריט ה-thin shells, פריט `<image-gallery>` (2026-05-11), פריט ה-perf pass (2026-05-12), ופריטי 2026-05-14: ה-curator band, דף האוצרת (`pages/curators/korin-avraham.html`) ועומק ה-href ברצועת האומנים.
    - הנתיבים הנכונים: `exhibitions/<slug>/index.html`, `opencalls/<slug>/index.html`, `curators/korin-avraham/index.html`.
- **thumbs של אומנים = פורטרטים. לא לייטבוקס** (`docs/components.md` §1.7). אין `data-artwork-*` על הרצועות.
- **Casing:** כל אנגלית = Copperplate UPPERCASE (`body{text-transform:uppercase}` + פטור `.heb`). הנתונים ב-JSON כתובים באותיות קטנות, וזה תקין.
- **`overflow-x`:**
  - בדפי התבנית, בעמוד האוצרת ובשני דפי הקול הקורא נשאר `body{overflow-x:clip}` inline. הוא מנוטרל ע"י `site-chrome.css` (`body:not(.menu-open){overflow-x:visible !important}`).
  - **לא להוסיף `overflow-x` חדש על `body`**. החיתוך נעשה רק על `html` (lessons 2026-06-15/16). בקולפן זה כבר מיושם: `html{overflow-x:hidden}` ו-`body{overflow-x:visible;max-width:100vw}`.
- **`<image-gallery>`** (`docs/components.md` §2):
  - לא לתת לו `z-index`.
  - ה-`.overlay` שמעליו עם `pointer-events:none`.
  - ה-scrim על `::after` של `.img-frame`, עם `z-index:1`.
- **בדיקה ויזואלית רק ב-http** (`python3 -m http.server`). ב-file:// ה-`@font-face` חסום והדף מוצג בפונטי fallback. file:// משמש רק לבדוק שהעותקים ה-inline עובדים.
- **שינוי שנוגע ביותר מדף אחד** (CSS/renderer משותף, הפצה בין שני דפי התבנית או בין שני דפי הקול הקורא): להריץ את רתמת הרגרסיה לפני קומיט:
  - `node tools/regress/snapshot.mjs --label before --only exhibitions/,curators/,opencalls/` → השינוי → `node tools/regress/snapshot.mjs --label after --only exhibitions/,curators/,opencalls/` → `node tools/regress/diff.mjs before after` (exit 0 = זהה).
  - 🔴 **אותם `--only` ו-`--widths` בדיוק בשני הצילומים.** `diff.mjs` סופר דף (או רוחב) שקיים רק בצילום אחד כהבדל, ולכן `after` בלי `--only` יחזיר exit 1 שגוי.
  - ברירת המחדל היא 390,1440 בלבד. לעבודת layout/טיפוגרפיה: `--widths 390,1024,1366,1440`. הבאגים של ה-family חיו בטאבלט ולא נראו בברירת המחדל: רמפת האימייל בקולות הקוראים (769–1100; 1024 מכסה) וכותרת המכתב בקולפן (1101–1280; להוסיף רוחב בטווח, למשל 1200).
- **SEO:**
  - OG: `og/exhibitions-<slug>-hero.jpg`, `og/opencalls-<slug>-hero.jpg`, `og/curators-korin-avraham-portrait.jpg`.
  - JSON-LD: `ExhibitionEvent` בתערוכות, `WebPage` בקולות הקוראים, `ProfilePage`+`Person` בעמוד האוצרת.
  - **פירורי הלחם ב-JSON-LD הם של הדף בלבד** (פריט יחיד). אין פריט ל-`/exhibitions/`, `/opencalls/` או `/curators/`, כי עמודי האינדקס לא נבנו (audit 2026-07-09). כשייבנו, אפשר להחזיר.
  - 🔴 **לא להריץ `tools/seo/inject.py` על אף דף ב-family הזה, גם לא בהרצה לדף בודד** (`inject.py <path>`, שהסקריפט עצמו מציע בהודעת הסירוב שלו).
    - הענפים `exhibitions/`, `opencalls/` ו-`curators/` בונים פירור לחם עם `/exhibitions/`, `/opencalls/` ו-`/curators/`. אלה אינדקסים שלא קיימים, וזה סותר את הכרעת audit 2026-07-09.
    - ה-title/description הכתובים ביד של 5 מתוך 6 הדפים שמורים גם ב-`tools/seo/overrides.json`, ו-inject.py מעדיף אותם: loneliness (title+description), how-many (description), שני הקולות הקוראים ועמוד האוצרת (title+description). **הקולפן לא נמצא שם**, ולכן הרצה עליו הייתה דורסת את ה-description הכתוב ביד ("…22 אמנים ואמניות…") ב-"The Peeler — הקולפן".
    - ⚠️ עריכה ידנית של `<title>`/description באחד מחמשת הדפים האחרים = לעדכן גם את הרשומה ב-`overrides.json`, אחרת הרצה עתידית תחזיר את הערך הישן.
    - הרצה על כל האתר חסומה ממילא (`og-dims.json` חלקי, ראה `docs/todo.md`).
    - בדף חדש: להעתיק בלוק `SEO:auto` מדף אחות ולערוך ביד.
  - ⚠️ **`<title>` נדרס בזמן ריצה** בחמשת הדפים ה-data-driven. בדפי התבנית ובקולות הקוראים: `title_en + ' — Zielinski & Rozen'`. בעמוד האוצרת: `'KORIN AVRAHAM — CURATOR — ZIELINSKI & ROZEN ART GALLERIES'` (`.toUpperCase()`).
    - בלשונית הדפדפן מופיע ערך ה-renderer. ה-`<title>` וה-`<meta name="description">` הסטטיים הם מה שרואים סורקים בלי JS ואינדקס החיפוש בהידר (`search-index.js`, שנבנה מהם ומ-`name` ב-JSON-LD ע"י `tools/search/build_index.py` — בכל קומיט דרך `.githooks/pre-commit` כשה-hook מופעל, `git config core.hooksPath .githooks`; לא לערוך ביד). `overrides.json` נקרא רק ע"י `inject.py`.
    - שינוי כותרת = ה-`<title>` הסטטי + העותקים בבלוק ה-SEO (`og:title`, `og:image:alt`, `twitter:title`, `name` ב-JSON-LD) + הרשומה ב-`overrides.json` (בחמשת הדפים שיש להם) + השדה ב-JSON שממנו ה-renderer בונה את `document.title` (ובעותקי ה-fallback). הקולפן (סטטי) לא מושפע מה-renderer, אבל העותקים שלו ב-head כתובים ביד באותו אופן.
- **ניווט:** פריטי ה-nav כתובים ישירות ב-`components/site-chrome.js`, ולא נלקחים מ-`site.json`:
  - "exhibitions" → `/#exhibitions`.
  - "open call" → `/#opencall` בדסקטופ, ו-`/#mobile-cta` ב-≤768 (`syncOpenCallHref`).
  - המצב הפעיל מזוהה לפי הנתיב: `/exhibitions/` → `exhibitions`, ו-`/opencalls/` או `/opencall/` → `opencall`.
  - כשייבנה עמוד אינדקס: לעדכן את ה-href ב-`site-chrome.js`, להוסיף ל-`sitemap.xml`, ולהחזיר את פירור הלחם.

## תבנית התערוכה — `exhibitions/loneliness/` + `exhibitions/how-many/`

### איך זה עובד
- שני הקבצים הם עותקים של אותה תבנית, עם `data-slug` על `<html>`.
- `<template id="tpl-page">` + renderer IIFE, ששולף את הרשומה מ-`exhibitions.json` לפי `data-slug` ומרנדר לתוך `<main id="page">`.
- `<body class="is-loading-data">`: ה-renderer מסיר את המחלקה. `site-chrome.js` מחכה להסרה לפני שהוא חושף את הדף.
- **ההבדלים המכוונים בין שני הקבצים:**
  - `data-slug`.
  - מטא/SEO.
  - `line-height` של `.descblock .desc`: loneliness `1.28` (גם במובייל); how-many `1.45` בדסקטופ ו-`1.42` במובייל.
- בנוסף יש drift לא-מכוון בתוכן `#fallback-exhibitions` (ראה "drift ידוע" במפת הדאטה), ו-`diff` בין הקבצים יראה גם אותו. הוא לא מזיק, ואין לסנכרן אותו כחלק מהעברת CSS/renderer.
- שינוי ב-CSS או ב-renderer = לערוך אחד **ולהעביר ידנית לשני**, בלי לדרוס את ההבדלים שלמעלה.

### מבנה
- `.ex-hero` (אפור `#EEF0EF`): עמודת טקסט + מסגרת תמונה `492×744` (≤1100: 380, אספקט `492/744`).
  - תגים `gallery_label_he` + `status_label_en` → `letter-heading` (`hero_letter_heading_en`; מוצג רק כשיש גם `curator_slug` וגם `hero_letter_heading_en`) → המכתב (`description_he`) → curator footer: divider `72×1` + `credit_he` מ-`curators.json` כקישור לדף האוצרת (מוצג רק כשיש `curator_slug` **ו-**`credit_he`).
  - בתמונה: `<image-gallery data-fit="cover">` מתוך `gallery_images[]` (ריק → `hero_image` בלבד; הראשונה `fetchpriority="high"`).
  - אוברליי `label_en` • `volume_en` / `title_he` / `title_en` (Solway, `--exo-title-en`). **גלוי רק בשקופית 0** — `is-hero-slide-0` מתחלף לפי `gallery:change`.
  - דסקטופ: האוברליי ב-`left:90px; top:326px` (≤1100: `left:50px; top:200px; width:280px`). מובייל: התמונה קודם, full-width, scrim שטוח `rgba(27,27,27,.4)` על `::before` (ה-`::after` מוסתר), אוברליי ממורכז; המידע אחריה על לבן.
- `.ex-artists`: רצועה אופקית, כרטיס `178×148` (מובייל `96×80`), שם אפור `#828282`.
- `.ex-curator`: אותה רצועה עם כרטיס יחיד (פורטרט מ-`curators.json`, `object-position:50% 28%`, תווית `badge_en`) → דף האוצרת. מוצגת רק כש-`curator_slug` מוגדר.

### שדות שהתבנית קוראת
- טקסט: `label_en`, `volume_en`, `title_he` (fallback `subtitle_he`), `title_en`, `gallery_label_he`, `status_label_en`, `hero_letter_heading_en`, `hero_image`, `gallery_images[{src,alt}]`, `curator_slug`.
- `description_he[{weight, lines[]}]`:
  - `weight` הוא `regular`, `light` או `heading-en`. השורות מחוברות ב-`<br>`, ו-`heading-en` בשורה אחת.
  - הפסקה מסוג `heading-en` מתכווצת ב-JS (`fitExHeadingEn`) מ-22px עד 9px כדי להישאר בשורה אחת.
- `artists[]`:
  - `name_en` — `\n` בתוך השם שובר שורה (`white-space:pre-line`).
  - `thumb`.
  - `slug`.
  - `artist_page_slug` — מחליף את יעד הקישור (לשיתופי פעולה).
  - `focus` — `object-position` לתמונה.
- **ללא `slug`:** ה-renderer מחפש בטבלת `_ARTIST_SLUGS` (שם → slug) שכתובה בקוד. אם לא נמצא, הכרטיס יוצא `<div>` **לא-מקושר**.
- **ללא `focus`:** נלקח מ-`_ARTIST_FOCAL` בקוד (מירור ידני של `FOCAL_POINTS` בדפי האומנים). ברירת המחדל `center 25%`.
  - **עדיף תמיד `slug` + `focus` ב-JSON** על פני הרחבת הטבלאות בקוד.
- `hero_overlay_en_only:true` (how-many): האוברליי מציג רק את `title_en`. ה-title-bar וה-`title_he` מוסתרים.
- ⚠️ **`hero_overlay_hide_en` לא נתמך ע"י הרנדרר של התבנית** (אין קוד ואין CSS ב-loneliness/how-many). המחלקה `.ex-hero--overlay-hide-en` וה-CSS שלה קיימים רק בקובץ הסטטי של הקולפן, והדגל ב-JSON נקרא היום רק ע"י `buildCard` בעמוד האוצרת. תערוכה חדשה על התבנית עם הדגל = הכותרת האנגלית מוצגת בדף ומוסתרת בכרטיס האוצרת. אם צריך את הדגל, להוסיף תמיכה ברנדרר וב-CSS **בשני** קבצי התבנית.
- **תמונות נוספות ל-hero** = להוסיף ל-`gallery_images[]` ב-JSON **וגם** לרשומה ב-`#fallback-exhibitions` בשני הקבצים (`docs/components.md` §2.8).

## `/exhibitions/loneliness/`

- 11 אומנים ברצועה. thumbs: `images/exhibitions/loneliness/artists/NN-<name>.webp`. לכולם `slug` ב-JSON.
- ה-hero gallery = 8 שקופיות: `images/exhibitions/loneliness/hero.webp` ועוד 7 תמונות מ-**`images/events/loneliness/`** (`invite-01..03`, `atmosphere`, `second-01..03`), רשומות ב-`exhibitions.json :: loneliness.gallery_images[]` **וגם** ב-`#fallback-exhibitions` של **שני** דפי התבנית.
  - 🔴 הקבצים האלה שייכים לדף האירוע `events/loneliness/` (`docs/routes/events.md`). כל שינוי בהם — שם, מחיקה, החלפת תוכן או קרופ — משנה או שובר את הגלריה כאן. שינוי נתיב = לעדכן את שלוש הרשימות.
- `status: archived`, `status_label_en: "previous"`, `volume_en: "VOLUME 1"`, גלריית המדינה, תאריכים 2026-01-19 → 2026-05-20.
- נכנסים: כרטיס `.ex-archive-item` בארכיון `#exhibitions` בהומפייג' (Figma `1124:947`/`1318:487`, `homepage.json :: exhibitions_archive.items[]`, תמונה `images/exhibitions/archive/loneliness-card.*`), הכותרת `.tribe-teaser-head` בהומפייג', כרטיס בעמוד האוצרת, כרטיס ב-`galleries/medina/`, קבוצות התערוכה בדפי האומנים, ועמודי `works/<id>`.

## `/exhibitions/how-many/`

- **15 אומנים** ברצועה. thumbs: `images/exhibitions/how-many/artists/NN-<name>.webp`.
- 🔴 **שיתוף הפעולה zohar ron × dan ben-ary:** שני הכרטיסים מקשרים ל-**`zohar-ron-dan-ben-ari`** (דף השת"פ).
  - "zohar ron": `slug:"zohar-ron"` + `artist_page_slug:"zohar-ron-dan-ben-ari"`.
  - "dan ben-ary": `slug:"zohar-ron-dan-ben-ari"`.
  - המיפוי מוגדר במפורש ב-JSON (`artist_page_slug` נועד לשיתופי פעולה). לא לשנות בלי בקשה. (לשם השוואה: בדף האירוע `events/how-many/` דן בן-ארי מקשר לדף השת"פ, אבל זוהר רון מקשר ל-`artists/zohar-ron/`.)
- ⚠️ **"racheli reuven" (כרטיס 15) יוצא לא-מקושר** (אין `slug`, והשם לא ב-`_ARTIST_SLUGS`). זה **תואם** ל-`docs/artist-linking.md` §1, שמונה אותה כ-placeholder שלא מקשרים אליו מתערוכות "עד שיש תוכן". אבל מאז יש לה יצירה אחת (`racheli-reuven-1`, שעמודה מקשר ל-how-many), והיא בגריד `/artists/` וב-sitemap, בעוד הדף `artists/racheli-reuven/` עדיין placeholder (`_pending_artist_pages`, `bio_he` = השם בלבד). **שאלה פתוחה למשתמש. לא לקשר על דעת עצמנו.** אם יוחלט לקשר: להוסיף `"slug":"racheli-reuven"` לרשומה ב-`exhibitions.json` ובשני עותקי `#fallback-exhibitions`, ולעדכן את `docs/artist-linking.md` §1.
- `hero_overlay_en_only:true`. `gallery_images` = ה-hero בלבד (1 שקופית; `_gallery_note`: להוסיף כשיהיו צילומים).
- `volume_en: "VOLUME 2"`, גלריית דיזינגוף, תאריכים 2026-05-26 → 2026-08-15, `status: current` (ראה Shared rules).
- נכנסים: בהומפייג' **פעמיים** — `#exhibitions-now` תחת `berlin`, וכרטיס `.ex-archive-item` בארכיון `#exhibitions` (→ `exhibitions/how-many/`, `.ex-archive-gal` + `aria-label` = "גלריית כיכר דיזינגוף", תמונה `images/exhibitions/archive/how-many-card.{webp,avif}` +480/768w, דאטה `homepage.json :: exhibitions_archive.items[]`). בנוסף: כרטיס בעמוד האוצרת, `galleries/dizengoff/ #g-exhibitions-data`, שם הבושם ב-`#perfume-promo` בהומפייג' (אזכור כותרת בלבד; הקישור שם הוא ל-zrp.co.il), קבוצות התערוכה בדפי האומנים, ועמודי `works/<id>`.
- ⚠️ **(2026-09-27) ברלין או דיזינגוף — טעון הכרעת משתמש.**
  - בהומפייג', `#exhibitions-now` מציג את how-many תחת קבוצת `berlin` (`the art gallery berlin`, תמונה `images/homepage/ex-now/berlin-how-many.{webp,avif}`, דאטה `homepage.json :: exhibitions_now.groups[]`; ראה `docs/routes/homepage.md`).
  - אבל ב-`exhibitions.json` עדיין `gallery_id:"dizengoff"` + `gallery_label_he` של דיזינגוף. לכן כרטיס האוצרת (שם הגלריה נגזר מ-`gallery_id`), `galleries/dizengoff/ #g-exhibitions-data` ותג ה-hero בדף עדיין אומרים דיזינגוף.
  - גם כרטיס הארכיון **באותו עמוד** כותב "גלריית כיכר דיזינגוף", כלומר ההומפייג' עצמו לא עקבי.
  - **לא לשנות `gallery_id`/`gallery_label_he` בלי הכרעה.** אם יוכרע ברלין: לעדכן את `exhibitions.json`, את שני עותקי `#fallback-exhibitions`, את `#fallback-exhibitions-min` בעמוד האוצרת, להוציא את הרשומה מ-`#g-exhibitions-data` של דיזינגוף, **וגם** לעדכן את כרטיס הארכיון בהומפייג' (`.ex-archive-gal`, `aria-label`, `homepage.json :: exhibitions_archive.items[0].gallery_id`), את `<meta name="description">`, `og:description` ו-`twitter:description` של `exhibitions/how-many/` (כתוב שם "נוכחית בגלריית כיכר דיזינגוף"), ואת `tools/seo/overrides.json['/exhibitions/how-many/'].description`.

## `/exhibitions/the-peeler/` — 🔴 סטטי קפוא

### הכלל
- הדף נבנה במקור על תבנית how-many (אותו `tpl-page`; הדגל `hero_overlay_hide_en` נוסף אז לעותק של הקולפן בלבד).
- **2026-06-25, בקשת משתמש (חופש עיצובי מלא):** הדף "הוקפא". הוסרו ה-`<template id="tpl-page">`, שלושת עותקי ה-`fallback-*` וה-renderer IIFE. שלושת הסקשנים (hero / artists / curator) הם עכשיו markup קבוע בתוך `<main id="page">`. ה-markup נלכד מפלט המנוע, ולכן הוא זהה ויזואלית.
- **התוכן כבר לא נמשך מ-`exhibitions.json`.** שינוי טקסט, אומן או תמונה = עריכה ישירה ב-`exhibitions/the-peeler/index.html`. אין השפעה על דפים אחרים, ודפי התבנית לא הושפעו.
- **לא להחזיר לתבנית ולא לחבר ל-JSON** בלי בקשה מפורשת.
- מאפייני `data-bind*` / `data-curator-*` ב-markup הם שאריות מהמנוע. **שום קוד לא קורא אותם**, ועריכת `exhibitions.json` לא תשנה את הדף. אפשר להשאיר אותם, אבל אין להסתמך עליהם.
- נשארו components: `<site-header>` / `<site-footer>` ריקים, ו-`site-chrome.js` מרנדר אותם.
- `is-loading-data` **הוסר מ-`<body>`. לא להחזיר.** אין renderer שיסיר אותו, ו-`site-chrome.js` יחכה ל-timeout לפני שיחשוף את הדף.
- ערכי הרשומה `the-peeler` ב-`exhibitions.json`: `status:"current"`, `status_label_en:"current"`, `volume_en:"VOLUME 2"`, `gallery_id:"medina"`, `curator_slug:"korin-avraham"`, תאריכים 2026-07-29 → 2026-10-05. הדף עצמו לא קורא אותם (הצרכנים ברשימה הבאה).
- **הרשומה `the-peeler` ב-`exhibitions.json` נשארת ונקראת במקומות אחרים:**
  - עמוד האוצרת: `title_*`, `label_en`/`volume_en`, `hero_overlay_hide_en`, `curator_card_image`, `gallery_id`.
  - `ex-order.js`: הדירוג בדפי האומנים.
  - `galleries/medina/ #g-exhibitions-data`: עותק ידני של הרשומה (`status`, `title_*`, `volume_en`, `start_date`/`end_date`, קרופ כרטיס `images/galleries/medina/ex-card-the-peeler.*`). שינוי תאריך, כותרת או סטטוס = לעדכן גם שם (כך נעשה בשינוי תאריך הסיום, 2026-09-27).
  - `tools/seo/inject.py`: `title_en`, `subtitle_he`, `hero_image`, `start_date`/`end_date` (רק אם מריצים אותו; ראה האיסור ב-Shared rules → SEO).
  - כשמשנים את הדף, לעדכן גם את הרשומה כדי שתישאר עקבית. כך נעשה ב-2026-07-26 עם tali-zelnik וב-2026-07-06 עם hadas-tuval.
  - ⚠️ `gallery_images` ברשומה = ה-hero בלבד, בעוד שבדף יש 7 שקופיות. הדף הוא מקור האמת.
- `volume_en: "VOLUME 2"` / `EXHIBITION • VOLUME 2`: **זהה ל-how-many.** זה verbatim מ-Figma, באישור המשתמש (2026-06-25). **לא "לתקן" ל-VOLUME 3.**

### Hero
- מבנה: `.hero-stack` בתוך `.img-frame` (desktop `492×744`, Figma `721:14345`).
  - שכבת בסיס `hero-base.{webp,avif}` (620×754, `object-fit:cover`). היא ה-LCP (`fetchpriority="high"`).
  - מעליה `.hero-layer-wrap` עם **`<image-gallery data-fit="cover" data-arrows="false">` בן 7 שקופיות.**
- ⚠️ ב-CLAUDE.md הישן נכתב "אין `<image-gallery>` ב-hero" ו-"`is-hero-slide-0` קבוע". **הקוד שונה מאז קומיט `83491e9` (2026-06-25), והקוד גובר.** מה שיש בפועל:
  - שקופית 0 = `hero-art.{webp,avif}` (1200×1600, +480/768/1080w) עם מחלקה `hero-layer--art`: `width:146%; height:128.73%; transform:translate(-14.3%,-11.19%)`. זה הקרופ של Figma (offset `-20.88%/-14.41%` של המסגרת, מחושב יחסית לתמונה המוגדלת).
  - שקופיות 1–6 = יצירות מ-`images/works/v2/` בסדר הזה: `noemi-safir-2`, `elsa-ars-brush-1`, `michael-konovalenko-1`, `maria-artamonova-1`, `alice-debellis-2`, `amnon-lipkin-13`.
  - האוברליי גלוי **רק בשקופית 0**. סקריפט inline בסוף הדף מחליף את `is-hero-slide-0` לפי `gallery:change`.
- **הוספת שקופית ל-hero** = `<img>` נוסף בתוך ה-`<image-gallery>` ב-HTML, כמו השכנים: `srcset`/`sizes` (וריאנטים 480/768/1080 + אחי avif), `width`/`height`, `loading="lazy" decoding="async"`. **לא** `gallery_images[]` ולא `docs/components.md` §2.8, שחלים רק על דפי התבנית. האוברליי נשאר רק בשקופית 0.
- scrim בדסקטופ: `linear-gradient(0deg, rgba(0,0,0,.7), transparent)`. במובייל: `rgba(27,27,27,.4)` שטוח (כמו בתבנית).
- `hero.{webp,avif}` (492×744) = קומפוזיט שטוח של היצירה. משמש רק ל-JSON (`hero_image`) ול-`image` ב-JSON-LD.
- ⚠️ **OG:** `og/exhibitions-the-peeler-hero.jpg` הוא **801×974 ונאפה מ-`hero-base`** (צילום הקולפן-מטבח האדום), **לא** מהקומפוזיט. `tools/seo/og-dims.json` רושם 801×974, אבל ב-`<head>` של הדף `og:image:width`/`og:image:height` = 492/744, כלומר אי-התאמה. בעיה פתוחה: לשאול את המשתמש איזו תמונה אמורה להופיע בכרטיס השיתוף. **לא לאפות מחדש ולא לשנות את המטא על דעת עצמנו.**
- **אוברליי** (Figma `721:14346`):
  - ממורכז (`top:50%`, רוחב 313px): title-bar `EXHIBITION • VOLUME 2` (Copperplate Light 26px, ≤1100 20px, מובייל 22px) + `הקולפן` (FbEzmel 29px, ≤1100 ומובייל 24px).
  - **בלי הכותרת האנגלית.** המחלקה `.ex-hero--overlay-hide-en` עם `.overlay .title-en{display:none}`, ובמקביל `hero_overlay_hide_en:true` ב-JSON.
  - `title_en: "The Peeler"` נשמר רק ל-`<title>`, OG ו-SEO.

### טקסט
- **letter heading** ("letter from the exhibition curator"):
  - דסקטופ (≥1101, `white-space:nowrap`): 32px בשורה אחת, inset שמאלי 24px. `fitLetterHeading` מכווץ **עד מינימום 26px**. אם גם ב-26px הכותרת לא נכנסת, הסקריפט מחזיר לגודל ה-CSS ומוסיף `.is-wrapped` (`white-space:normal; text-wrap:balance`).
  - הסקריפט מתחיל כל ריצה באיפוס (מסיר את `.is-wrapped` ואת ה-`font-size` ה-inline), ורץ רק כש-`white-space` המחושב הוא `nowrap`. ב-≤1100 ובמובייל ה-CSS כבר שובר בעצמו, והסקריפט יוצא.
  - 🔴 **בלי `overflow:hidden` על הכותרת (היום `overflow:visible`), ולא להוריד את הסף מתחת ל-26px.** ב-2026-09-27 הכותרת נקטעה ברוחבי 1101–1280 בגלל שני אלה (תוקן באותו יום, קומיט `bd1fc672`).
  - ≤1100: 30px, `white-space:normal`, שבירה מאוזנת (`text-wrap:balance`).
  - מובייל: 22px/1.42.
- **המכתב:** מכתב אוצרת ארוך. הפסקה הראשונה היא `heading-en` "welcome aboard." (Copperplate Light 18px, מובייל 16px; Figma `721:14337`).
  - המכתב מזכיר "עשרים ושניים אמנים", וזה תואם ל-22 הכרטיסים. גם `<meta name="description">`, `og:description` ו-`twitter:description` של הדף כותבים "22 אמנים ואמניות". אם מוסיפים או מסירים אומן, **לשאול** אם לעדכן את המכתב ואת שלושת תגי המטא. לא לשנות אותם על דעת עצמנו.
- **curator footer:** "אוצרת התערוכה - קורין אברהם" → `../../curators/korin-avraham/`.

### רצועת האומנים — 22 כרטיסים
- **הסדר = Figma desktop `980:92` verbatim:** zohar-ron, noemi-safir, elsa-ars-brush, anat-wegier, yarden-amir, nir-giorgio-levin, jessica-tabarovsky, chen-ziv, baruch-torgeman, gilad-kenan, lahav-barak, livay-levi, natasha-zeriker, talia-zoref, aharon-bas, bar-cohen, amnon-lipkin, alice-debellis, maria-artamonova, michael-konovalenko.
  - **אחריהם hadas-tuval ואז tali-zelnik** (tali נחשפה ב-2026-07-26 ונוספה בסוף).
- **thumbs:**
  - 21 כרטיסים ממחזרים את `images/artists/grid/<slug>.{webp,avif}` (+480w), עם `object-position:50% 40%`.
  - **hadas-tuval** משתמשת ב-thumb ייעודי: `images/exhibitions/the-peeler/artists/hadas-tuval.{webp,avif}` (356×356, רונדר מ-Figma node `980:175`), עם `50% 45%`.
- כל 22 הכרטיסים הם `<a class="card is-linked">`.
- השמות כתובים עם שבירת שורה אמיתית בתוך `.name` (`white-space:pre-line`), למשל "nir giorgio⏎levin" או "alice⏎de bellis".
- **הוספת כרטיס:**
  - להעתיק בלוק `<a class="card is-linked">` קיים (עם `<picture>`, `<source type="image/avif">` ו-`data-pic-done="1"`). אפשרות אחרת: `<img src="….webp">` חשוף, ו-`picture-upgrade.js` יעטוף אותו.
  - במקביל להוסיף את האומן ל-`artists[]` ברשומה ב-`exhibitions.json`.
- 🔴 **amnon-lipkin נשאר ברצועה.** דף האומן `artists/amnon-lipkin/` קיים, ויצירה שלו היא שקופית ב-hero. מה שנמחק ב-2026-08-28 הוא **דף האירוע** `events/amnon-lipkin/`, לא האומן.

### סקשן האוצרת
- זהה לתבנית: כרטיס קורין → `../../curators/korin-avraham/`, תווית "the curator".
- הפורטרט: `images/curators/korin-avraham/portrait` עם srcset 480w.

## `/curators/korin-avraham/`

### איך זה עובד
- data-driven: fetch-first ל-`data/curators.json`, `data/exhibitions.json` ו-`data/galleries.json`. ה-fallbacks הם `#fallback-curators`, `#fallback-exhibitions-min` ו-`#fallback-galleries`.
- הדף בוחר את האוצרת לפי `CUR_SLUG = 'korin-avraham'`, שכתוב בקוד.
- `#fallback-galleries` = `data/galleries.json` verbatim, ו-**`python3 tools/sync_data.py` הוא שמייצר אותו.** לא לערוך אותו ביד.
- `#fallback-curators` ו-`#fallback-exhibitions-min` מתוחזקים **ביד**:
  - `-min` מכיל רק `id, slug, label_en, volume_en, title_he, title_en, gallery_id, hero_image, description_he`, ובנוסף את דגלי האוברליי ואת `curator_card_image` כשיש.
  - כשמשנים את השדות האלה ב-JSON, או מוסיפים תערוכה ל-`exhibition_slugs`, מעדכנים גם כאן.

### Hero (Figma `314:30`–`314:42`)
- **דסקטופ:** פס אפור, גריד `1fr 492px`. עמודת הטקסט: badge `badge_en` ("the curator") → השם (`name_en_first` Bold / `name_en_last` Light) → IG `@`+`instagram_handle` → הביו. מימין פורטרט ריבועי `492×492` (`object-position:50% 32%`).
  - הפורטרט `images/curators/korin-avraham/portrait.webp` (1507×2000, +480w; ייצוא מ-node `314:122`) הוא ה-LCP.
- **ביו** (`bio_he`: מערך פסקאות, כל אחת מערך שורות; Figma desktop `706:2`): FbEzmel Light, עם קו אנכי `#D8D8D8` בצד ימין (`706:5`).
  - הסימון `{en}…{/en}` בתוך השורות הופך ל-`<span class="ltr-en">` (Copperplate, LTR). כך מסומן "YA SALAM". לשמור על הסימון כשעורכים את הביו.
- **מובייל** (Figma `314:97`, `706:10`): הסדר הוא badge → פורטרט (עם scrim `rgba(0,0,0,.6)`→0) → שם ו-IG → ביו בסקשן לבן full-bleed (עד 358px). ה-`.cur-hero__copy` מקבל `display:contents` כדי לאפשר את ה-`order`.

### כרטיסי התערוכות (`section_heading_en` = "the curator's exhibitions")
- הכרטיסים לפי **`curators.json :: exhibition_slugs`**. הסדר הנוכחי הוא loneliness, how-many, the-peeler, והוא סדר הדסקטופ משמאל לימין.
- כרטיס → `../../exhibitions/<slug>/`.
- המסגרת: `736.97px` בדסקטופ, 560 ב-≤1100, `433.939px` במובייל (רוחב עד 358).
- scrim `linear-gradient(0deg, rgba(0,0,0,.7), transparent)`.
- **אוברליי לפי דגלי ה-JSON:**
  - `hero_overlay_en_only` (how-many): ערימת השורות מתוך הפסקה `heading-en` ב-`description_he` (Solway 26px). אם משנים את הפסקה הזו ב-JSON, משתנה גם הכרטיס.
  - `hero_overlay_hide_en` (הקולפן): title-bar + כותרת עברית בלי אנגלית. גם כותרת ה-meta מתחת לכרטיס מוצגת **בעברית**.
  - אחרת (loneliness): title-bar + עברית + אנגלית. הרוחב `min(400px, calc(100% - 32px))` (Figma 400) חל על כל אוברליי שאינו en-only, כלומר גם על כרטיס הקולפן.
- **שם הגלריה** מתחת לכרטיס = `name_en` מ-`galleries.json` לפי `gallery_id`.
- **תמונת הכרטיס** = `curator_card_image` אם קיים, אחרת `hero_image`.
  - לקולפן יש `images/exhibitions/the-peeler/curator-card.{webp,avif}` (822×1243, +480w).
  - ⚠️ **ה-`width`/`height` כתובים בקוד:** loneliness 690×1044; כל השאר 1068×1600; עם `curator_card_image` 822×1243, ו-srcset רק עם 480w. תערוכה חדשה במידות אחרות מחייבת לעדכן את `buildCard`, אחרת יהיה CLS.
- **מובייל:** עמודה אחת, ו-**`.cur-card--how-many{order:-1}`** מעלה את how-many לראש. בפועל הסדר הוא how-many → loneliness → the-peeler.
  - ⚠️ הכלל נכתב כשהיו רק 2 כרטיסים, לפי Figma `314:97`, שקדם לקולפן. לא אומת אם הקולפן אמור להיות ראשון במובייל.

### דאטה כפולה (ביד)
- `instagram_handle` (`yasalamfashionblog`) מופיע גם במקומות האלה, ושינוי handle = לעדכן את כולם:
  - עמוד האודות (`docs/routes/about.md`).
  - כקישור קשיח בגוף הכתבה `press/walla/`.
  - ב-`#fallback-curators` של שני דפי התבנית.
  - ב-`#fallback-curators` של עמוד האוצרת עצמו.
  - ב-JSON-LD שב-`<head>` של עמוד האוצרת (`Person.sameAs` = `https://www.instagram.com/yasalamfashionblog/`, בלוק SEO כתוב ביד).
- `contact_email` (`korinalove5@gmail.com`) מופיע גם ב-`opencalls.json :: contact.email` (ובשני עותקי `#fallback-opencalls`) וב-`mailto` הכתוב ביד בכל עמודי `works/<id>/` (`docs/routes/works.md`). שינוי כתובת = לעדכן את כולם (ובדפי הקול הקורא גם לכייל מחדש את רמפת האימייל בטאבלט, ראה `.oc-hero` בסקשן הקול הקורא).
- `credit_he` ("אוצרת התערוכה - קורין אברהם") נקרא ע"י דפי התבנית, ולכן חייב להופיע ב-`#fallback-curators` שלהם.

## תבנית הקול הקורא — `opencalls/the-peeler/` + `opencalls/how-many/`

### איך זה עובד
- שני הקבצים זהים, פרט למטא/SEO ול-`data-slug`.
- renderer IIFE קורא את `opencalls.json` ו-`site.json` ומרנדר ל-`<main id="page">`, שבו מוצג "loading…" עד הרינדור.
- CSS או renderer = לערוך אחד ולהעביר ידנית לשני.

### מבנה
- **`.oc-hero` אפור:** טקסט RTL ומסגרת תמונה `492×744` (≤1100 `380×560`).
  - 🔴 **טאבלט 769–1100 (בשני הקבצים, 2026-09-27):** בתוך `@media (min-width:769px) and (max-width:1100px)` יש `.oc-hero .text-col{min-width:0}` + `.oc-hero .block .text .email{font-size:clamp(14px,calc((100vw - 552px) / 16.1),18px)}`. האימייל הוא מילה אחת ב-Copperplate שלא נשברת (≈16.1em), ובלי הכלל הוא דוחף את מסגרת התמונה מחוץ למסך. **לא להסיר את `min-width:0` ולא להרחיב את הרמפה מחוץ לטווח** (1440 לא זז). החלפת כתובת האימייל = למדוד מחדש את היחס 16.1. עמודת טקסט חדשה עם `flex:1` צריכה `min-width:0` (lessons 2026-09-27).
  - scrim `linear-gradient(0deg, rgba(0,0,0,.35), transparent 60%)`. במובייל אין scrim, והתמונה עולה לראש (`order:-1`).
  - תגים: `submission_status_he` (אפור) + `gallery_label_he`.
  - כותרת: `title_html` (24px; במובייל `clamp(18px,4.8vw,24px)` + `nowrap`).
  - `description_he` (`weight` `regular`/`light`).
  - אחריהם בלוקים שמופרדים ב-divider של 72px: [מעוררי רגש] → הנחיות הגשה → יצירת קשר.
- 🔴 **`title_html` ו-`submission_instructions_he.intro_html` מוזרקים כ-HTML גולמי, בלי escape.** מערבבים שם `<span class="heb">`/`<span class="lat">`, והתוכן חייב להיות HTML תקין.
  - the-peeler: `<span class="heb">הקולפן</span> | <span class="lat">exhibition volume 2</span>`.
  - how-many: `<span class="lat">how many partners have you had?</span>`.
- **`emotional_triggers`** (the-peeler בלבד; ב-how-many `null`, ואז הבלוק וה-divider שלו לא מרונדרים):
  - הכותרת `title_he`, ואחריה `lines[]`. כל שורה היא `<p class="trigger-line">`, וה-` | ` הופך ל-`.sep` אפור.
  - 🔴 **`lines[]` = שבירות השורות של Figma verbatim** (`XhGH...::119:2587`). הפריטים לא תמיד מופרדים ב-` | ` ולא תמיד שלמים בשורה אחת:
    - "פחד להישאר לבד" + "רציתי יותר ממה שנתנו לי" כתובים "…| פחד להישאר לבד רציתי" / "יותר ממה שנתנו לי | …": פריט שנשבר בין שורות, בלי מפריד.
    - "פחד מקרבה" + "בהמתנה" כתובים "פחד מקרבה בהמתנה": שני פריטים בלי מפריד.
    - **לא להוסיף ` | ` ולא לשבור מחדש.**
  - `items[]` = הרשימה הלוגית. משמשת רק כשאין `lines`.
  - במובייל הבלוק על רקע `#FAFAFA`, full-bleed.
- **יצירת קשר:**
  - `contact.label_he`.
  - האימייל: מוצג ב-Copperplate UPPERCASE, וה-`mailto` באותיות קטנות. בטאבלט הגודל שלו מתכווץ ברמפה (ראה `.oc-hero` למעלה).
  - `deadline_label_he` + `deadline_he` (Copperplate, `direction:ltr`).
  - `note_he` באפור.
- **Hero srcset:** נבנה מ-`hero-{480,768,1080}w.webp` לצד `hero.webp`.
  - 🔴 המידות הטבעיות כתובות בקוד, בטבלת `HERO_DIMS` (`the-peeler` 1601×2000, `how-many` 1600×2000), **בשני הקבצים**.
  - קול קורא חדש = להוסיף שורה ל-`HERO_DIMS` בשני הקבצים ולייצר את הווריאנטים (+avif), אחרת אין `width`/`height`.
- **גלריה (`gallery_images[{image, video, poster}]`)** — the-peeler בלבד; ב-how-many `null`:
  - **דסקטופ `.oc-gallery`:** מסגרות `492×744`, צמודות לימין, `gap:48`.
    - פריט עם `video` מתנגן **inline בתוך הכרטיס**. יש עליו `data-artwork-skip`, והלייטבוקס מדלג עליו.
    - פריט תמונה נפתח ב-artwork-lightbox (scope `opencall-<slug>`).
    - כפתור play: עיגול 72px `rgba(217,217,217,.4)` עם משולש, לפי Figma `119:2495` (לפי הערת ה-CSS).
  - **מובייל:** `.stacked-gallery.sg-mode-lightbox` (scope `opencall-<slug>-mobile`). הווידאו מתנגן inline דרך `stacked-gallery.js`.
  - אחרי הזרקה ה-renderer קורא ל-`ArtworkLightbox.refreshFocusable()` ול-`StackedGallery.refresh()`.
  - שני הפריטים הנוכחיים הם וידאו: `images/opencalls/the-peeler/gallery-0{1,2}.{mp4,webp,avif}` + `-poster.webp`.
  - ⚠️ `docs/components.md` §3.5 אומר ש"וידאו + `sg-mode-lightbox` = לא יציג". כאן זה עובד, כי פריטי הווידאו מסומנים `data-artwork-skip` ומתנגנים inline. לא להסיר את ה-skip.

### דאטה
- `opencalls.json`: `status` (שניהם `archived`), `submission_status_he` ("ההגשה נגמרה"), `deadline`/`deadline_he`, `gallery_id`/`gallery_label_he`, `hero_image`, `card_image`, `contact`, `figma_node_*`.
- `card_image` (`images/opencalls/<slug>-card*.webp`) לא משמש את הדפים. הוא התמונה של כרטיסי הקול הקורא בהומפייג' (`#opencall` / `#mobile-cta`, `docs/routes/homepage.md`).
- שינוי ב-`opencalls.json` = לעדכן ביד את `#fallback-opencalls` **בשני** הקבצים (כל אחד מכיל את שתי הרשומות). `sync_data.py` לא מטפל בזה.

## נקודות מגע: הוספת תערוכה או שינוי בה

המקומות שבהם תערוכה מופיעה היום. כולם צריכים בדיקה כשמוסיפים תערוכה או משנים כותרת, תאריכים, סטטוס או תמונה:

1. **`data/exhibitions.json`:** תערוכה חדשה נכנסת **בסוף המערך**. המערך כרונולוגי עולה, והוא מקור האמת ל"התערוכה החדשה למעלה" בדפי האומנים. אחר כך להריץ **`python3 tools/sync_data.py`**, שמייצר מחדש את `data/generated/ex-order.js`.
   - 🔴 **רזידנסי או פופ-אפ אינו תערוכה** (SUMII, רזידנסי מלאני הקימוגלו וכו'). לא להוסיף אותו ל-`exhibitions.json`: המערך הוא המקור של `data/generated/ex-order.js`, שנטען ב-41 מ-44 דפי האומנים (כולם חוץ מ-alon, dan-ben-ary ו-zohar-ron-dan-ben-ari), ויצירות שיפנו לרשומה כזו ידורגו כ"תערוכה" החדשה ביותר — מעל הקולפן. כרטיס רזידנסי SUMII (`kind:"residency"`, `route:"sponsors/sumii/"`) חי **רק** ב-`#g-exhibitions-data` של `galleries/dizengoff/` ובהומפייג' (`homepage.json :: exhibitions_now.groups[]`); רזידנסי מלאני חולק איתו את `sponsors/sumii/` (רשומה ב-`sponsors.json`). יצירות רזידנסי מסומנות ב-`works.json` עם `kind:"residency"` ו-`exhibition_slug:null`, ולכן יורדות תמיד מתחת לתערוכות. ראה `docs/data-contracts.md`, `docs/routes/galleries.md` ו-`docs/routes/works.md`.
2. **הדף עצמו:** עותק של התבנית (how-many) עם `data-slug`, או דף סטטי כמו הקולפן (לשאול את המשתמש איזה). בגרסת התבנית: הרשומה חייבת להיכנס ל-`#fallback-exhibitions` של העותק החדש; הנוהג הקיים הוא שכל עותק מחזיק את כל רשומות התבנית, כך שמוסיפים אותה גם לשני הקיימים.
3. **עמוד האוצרת:** `curators.json :: exhibition_slugs`, **וגם** אותו מערך ב-`#fallback-curators` של עמוד האוצרת (ביד; ממנו נבנים הכרטיסים ב-file://). בנוסף: הרשומה ב-`#fallback-exhibitions-min` (ביד), מידות הכרטיס ב-`buildCard`, וכלל ה-`order` במובייל.
4. **דף הגלריה:** `#g-exhibitions-data` (ביד), ובמדינה גם קרופ כרטיס. ראה `docs/routes/galleries.md`. (דוגמה: שינוי תאריך סיום = `exhibitions.json` + `#g-exhibitions-data` בדף הגלריה, כמו בקומיט `bd82b1c9`.)
5. **הומפייג':** `#exhibitions-now`, הארכיון `#exhibitions` (`homepage.json :: exhibitions_archive.items[]`) וכרטיסי הקול הקורא. ראה `docs/routes/homepage.md`.
6. **יצירות:** `exhibition_slug` / `exhibition_title_he` / `exhibition_route` ב-`works.json :: art_works[]` ו-`exhibition_statements[]`, ואז `sync_data.py`. ראה `docs/routes/works.md` ו-`docs/routes/artists.md`.
7. **SEO:** רשומה ב-`sitemap.xml` (כלל-זהב 15) + `python3 tools/seo/refresh_sitemap_lastmod.py`. OG `og/exhibitions-<slug>-hero.jpg` נאפה ביד. בלוק `SEO:auto` מועתק מדף אחות.
8. **לפני קומיט:** `python3 tools/sync_data.py --check` (exit 0), ורתמת הרגרסיה אם נגעת ביותר מדף אחד (ראה Shared rules).
   - הרתמה מוכיחה *אי-שינוי*, ולכן בשינוי תוכן מכוון היא תחזיר exit 1. לעבור על הדו"ח ולוודא שההבדלים היחידים הם הצפויים (הכרטיס או הרשומה החדשים בעמוד האוצרת, בדף הגלריה ובהומפייג'). שאר הדפים חייבים לצאת זהים.
   - להרחיב את `--only` לכל מה שצפוי להשתנות, למשל `galleries/`, וההומפייג' = `index.html` (ההתאמה היא לפי תחילת הנתיב). אותם `--only`/`--widths` בשני הצילומים.
   - דף חדש נכלל בצילום גם לפני `git add`: `snapshot.mjs` לוקח את כל ה-`*.html` שב-git **וגם** קבצים חדשים שאינם ב-`.gitignore` (`_staging/`, `trash/` וכו' מוחרגים). דף שנוצר בין שני הצילומים יסומן `only in after` ונספר כהבדל — צפוי כשמוסיפים דף.
9. **קישורים, כותרות ותוויות קשיחים ב-HTML** (לא נגזרים מ-`exhibitions.json`):
   - דפי האירוע: פסי `presented as part of` / `EXHIBITION • VOLUME 2` + "הקולפן" במשפחת artist-talk (`docs/routes/events-talks.md`), וגם `events/gala-night/`, `events/how-many/`, `events/loneliness/`, `events/close-look/`, `events/artist-talk/` (`docs/routes/events.md`).
   - הכתבות `press/the-last-station/`, `press/manicure-against-darkness/`, `press/peeling-a-layer/`, `press/the-shared-list/`.
   - `sponsors/soos/`.
   - `exhibition_id` ב-`events.json` וב-`press.json`.
   - בשינוי כותרת או תווית: `grep -rl 'exhibitions/<slug>' --include=index.html .` **וגם** grep על מחרוזת הכותרת עצמה (למשל `events/loneliness/` לא מקשר ל-`exhibitions/loneliness/` אבל כותב "בדידות"), ולעבור על כל תוצאה. תוצאות ב-`works/*` מגיעות מ-`#artwork-data` שבבעלות `sync_data.py` (סעיף 6), ולא עורכים אותן ביד. **חריג: `works/livay-levi-3/`**, שבו `description`/`og:description`/`twitter:description` כתובים ביד ומזכירים "בתערוכת הקולפן". (ה-slug עצמו לא משתנה — כלל-זהב 6.)

## בעיות פתוחות

- ⚠️ **racheli reuven לא מקושרת ברצועת how-many.** תואם ל-`docs/artist-linking.md` §1 (placeholder), אבל היום יש לה יצירה. פירוט בסקשן how-many. מחכה להכרעת משתמש. לא רשום ב-`docs/todo.md`.
- ⚠️ **סטטוס `current` ל-how-many שהסתיימה (2026-08-15)**, למרות שהיא כבר בארכיון ההומפייג'. מחכה להכרעת משתמש. אחרי 2026-10-05 אותה שאלה חלה על הקולפן. (מה לעדכן אם תועבר ל-`archived`: Shared rules → סטטוס.)
- ⚠️ **how-many: ברלין או דיזינגוף** (2026-09-27). `#exhibitions-now` בהומפייג' מציג אותה תחת ברלין, בעוד כרטיס הארכיון באותו עמוד, `exhibitions.json` וכל מה שנגזר ממנו אומרים דיזינגוף. אם יוכרע ברלין, לעדכן גם את כרטיס הארכיון (`.ex-archive-gal`, `aria-label`, `homepage.json :: exhibitions_archive.items[0].gallery_id`). פירוט בסקשן how-many. מחכה להכרעת משתמש.
- ⚠️ **OG של הקולפן:** הקובץ 801×974 מ-`hero-base` (קולפן-מטבח אדום), והמטא אומר 492×744. פירוט בסקשן Hero של הקולפן. מחכה להכרעת משתמש. לא רשום ב-`docs/todo.md`.
- ⚠️ **הביו של קורין ב-`curators.json` כולל טקסט ספציפי ל-loneliness** ("מכלול העבודות בתערוכה מהוות עבור אברהם סקלה של בדידות…"). זו אותה בעיה שרשומה ב-`docs/todo.md` לגבי עמוד האודות, והיא חלה גם כאן. **לא לשנות** עד הכרעת המעצבת.
- ⚠️ **ה-meta description / OG של עמוד האוצרת** מזכיר רק את "בדידות" ו"כמה שותפים היו לך?", ולא את הקולפן. לא רשום ב-`docs/todo.md`.
- ⚠️ **סדר הכרטיסים במובייל בעמוד האוצרת** (how-many ראשון, הקולפן אחרון) לא אומת מול פריים עדכני.
- **`exhibitions.json :: archive_thumbnails` הוא דאטה מתה.** הצרכן היחיד שלו, ארכיון ה-tabs+thumbs בהומפייג', הוחלף ב-2026-06-08 (הגיבוי ב-`trash/`). מ-2026-09-27 הארכיון הוא שני כרטיסים סטטיים (how-many + loneliness, `homepage.json :: exhibitions_archive.items[]`), ו-`homepage.json` כבר לא מפנה אליו (`thumbs_ref` הוסר). אין לו אף קורא.
  - ⚠️ פריט ה-todo "Dizengoff archive thumbs" מפנה ל-`#fallback-archive` ב-`index.html`, שכבר לא קיים. הפריט מיושן.
  - גם `thumbnails: []` ברשומות לא נקרא.

## Removed / do not restore

- **התבנית בקולפן:** `<template id="tpl-page">`, `#fallback-site` / `#fallback-curators` / `#fallback-exhibitions` וה-renderer IIFE הוסרו ב-2026-06-25 (בקשת משתמש). לא להחזיר את הדף למצב data-driven בלי בקשה.
- **`is-loading-data` על `<body>` בקולפן:** הוסר. לא להחזיר.
- **הסתרת tali-zelnik מהרצועה** (`_staging`, 404) **בוטלה** ב-2026-07-26. היא נחשפה ונמצאת בסוף הרצועה. לא להסתיר שוב.
- **כרטיס hadas-tuval לא-קליקאבילי בוטל** ב-2026-07-06. היום הוא `<a class="card is-linked">` + `slug` ב-JSON.
- **"בתוך בסביבה"** בכותרת loneliness: טעות מוכרעת. לא לשחזר.
- **קישורי תערוכה ל-`opencalls/<slug>`** מעמודי יצירות: הוחלפו ב-`exhibition_route` → `exhibitions/<slug>`. לא לחזור לנתיב הקשיח.
- **נתיבים ישנים** `pages/exhibition.html?id=…`, `pages/opencall.html`, `pages/curators/korin-avraham.html`: לא קיימים יותר. אל תבנה מהם ואל תקשר אליהם.
