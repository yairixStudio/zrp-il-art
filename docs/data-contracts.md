# Data contracts — `data/*.json` + עותקי הדאטה

> **לקרוא לפני:** שינוי של כל קובץ ב-`data/` (כולל `data/generated/`), הוספה/שינוי של שדה, ונגיעה בכל עותק דאטה שיושב בתוך דף (`<script type="application/json" id="…">` או `<script src="…/data/generated/…">`).
> מצב נוכחי (2026-09-27; "מי צורך" נבדק מול הקוד באותו תאריך) + כללים פעילים. כללים ספציפיים לדף → `docs/routes/<family>.md`. היסטוריה: `docs/history/CLAUDE-2026-09-27.md` §6, §4. `⚠️` = לא הוכרע/לא אומת. רשימות "היום" (ערכים, ספירות) = תמונת מצב — לבדוק מול הקוד.

## 0. עקרונות

- **`data/*.json` = מקור-האמת** (הסכמה מחקה CMS עתידי); דף לא מטמיע תוכן inline (כלל-זהב 1). Re-Read לפני עריכה (כלל-זהב 9) — עריכה על עותק ישן של `events.json`/`press.json`/`homepage.json` דורסת סשן מקביל, ו-`--check` לא יתפוס.
- **שדה חדש → לכל הרשומות בקובץ** (`null` אם לא ידוע) ומתעדים אותו כאן באותו קומיט (שדה חסר → מוסיפים ל-JSON לפני השימוש).
  - **חריג — דגלים ושדות אופציונליים** (ב-`events.json`: `soon`, `pinned`, `date_tbd`, `date_end`/`date_label`, `widths`, `list_*`, `event_photos`, `photo_credit_*`, `performers_he`…; ב-`press.json`: `date_end`) קיימים **רק ברשומות שמשתמשות בהם**, והיעדר = ברירת המחדל (כרטיס רגיל, אירוע של יום אחד). לא להוסיף להם `null`; את `soon` **מוחקים** (לא `null`) כשנבנה דף (§6.2).
- **אחרי כל שינוי ב-JSON:** `python3 tools/sync_data.py`; **לפני קומיט:** `--check` ⇒ exit 0. עותק ידני (§1.4) או טקסט ב-`<head>` של דף (§1.2) — לעדכן באותו קומיט.
  - 🔴 הקבצים ש-`sync_data.py` כתב (`data/generated/*.js`, `works/index.html`, `works/<id>/`, `galleries/<slug>/`, `curators/korin-avraham/`) הם קבצי פרודקשן — `git add` **בשמם** עם ה-JSON (הסקריפט מדפיס את הרשימה; `git status`), לא `-A` (כלל-זהב 14). קומיט של ה-JSON בלבד = אתר מיושן; `--check` בודק את עץ העבודה, לא את הקומיט.
- **Figma ids בדאטה = meta בלבד** (כלל-זהב 5). הפורמט מעורב: `"1318:583"` + `figma_file` נפרד, או `"XhGH289YTRcW811wrufRJz::721:14300"`. node id משמעותי רק יחד עם fileKey (`XhGH…` = landing, `Zn3N…` = graphics) — לאמת מול ה-URL.
- **`_note` / `_*_note`** = דאטה, לא הוראות, חלקן מיושנות (למשל `works.json::_note` "Page embeds this inline… keep both in sync"); סתירה → המסמך + הקוד גוברים.
- ⚠️ **`$schema`:** כל קובץ חוץ מ-`sponsors.json` מצביע ל-`./_schema/<name>.schema.json`, אבל קיים רק `data/_schema/curators.schema.json`; אין ולידציה אוטומטית (רק `--check` + הרנדור).
- **מפתחות-join הם מחרוזות מדויקות** (`exhibition_title_he` בין works ↔ exhibition_statements, `slug`/`id` בין קבצים) — שינוי אות/גרש/רווח/`\n` שובר בשקט; לשנות בכל הצדדים. **slugs לא משתנים** (כלל-זהב 6).
- **SEO:** `tools/seo/inject.py` קורא את `artists`, `works.art_works`, `exhibitions`, `events`, `press`, `opencalls`, `curators`, `galleries`, `sponsors`. **לא מריצים גורפות** (מרגרס ~90 דפים); דף חדש = בלוק `SEO:auto` ידני, sitemap ו-`og/` ביד — `docs/seo.md`, כלל-זהב 15 (`tools/seo/og_gen.py` שבור). על דף בודד (`python3 tools/seo/inject.py <page>/index.html`) — לבדוק diff ולשחזר: description ידני שנקטע, שעות ב-`startDate`/`endDate`, `og:image` שנפל ל-webp.

## 1. עותקי דאטה — מה מיוצר ומה ידני 🔴

### 1.1 למה יש עותקים, ושלושה דפוסי טעינה
דף שנפתח ב-file:// לא יכול `fetch`, לכן דף שמרנדר מדאטה נושא (או טוען) עותק:
- **inline-only** — הרנדרר קורא רק את העותק: `works/index.html #works-data`, `works/<id>/ #artwork-data`, `galleries/<slug>/ #g-artworks-data` + `#g-exhibitions-data`, `events/index.html #events-list-data`, `artists/index.html #artists-grid-data`, `events/ktuba/ #fallback-ktuba-artists`. **עותק מיושן = באג גלוי גם בפרודקשן.**
- **inline-first → fetch** — דפי האומן: `window.__ARTISTS_INLINE__` (מ-`data/generated/artists.js`); אם חסר → `fetch("../../data/artists.json")`.
- **fetch-first → fallback** (`loadJson(path, embeddedId)`) — `curators/korin-avraham/`, `exhibitions/how-many|loneliness/`, `opencalls/how-many|the-peeler/`, `galleries/<slug>/` (`#fallback-galleries`). ב-HTTP נקרא ה-JSON; העותק רק ב-file:// ⇒ **עותק מיושן לא נראה בפרודקשן, רק מקומית**. `#fallback-galleries` = **generated**; השאר ידניים (§1.4).
- 🔴 בדיקה ויזואלית/טיפוגרפית רק דרך http (file:// חוסם `@font-face`; CLAUDE.md TL;DR 14).

### 1.2 מיוצר אוטומטית — `python3 tools/sync_data.py`
- מייצר מחדש כל עותק שהוא פונקציה מדויקת של ה-JSON; להריץ אחרי **כל** שינוי ב-`artists.json` / `works.json` / `exhibitions.json` / `galleries.json`. אידמפוטנטי. `--check` = לא כותב, exit 1 + רשימת יעדים מיושנים ובעיות בדפי אומן.
- **בבעלותו (לעולם לא לערוך ביד):**
  - `data/generated/artists.js` ← `artists.json` **כולו** → `window.__ARTISTS_INLINE__`. **אובייקט** (`{"$schema",…,"artists":[…]}`), לא מערך; הרנדרר מפרק `.artists` (בדיקת `.length` על האובייקט = הבאג "ARTIST NOT FOUND").
  - `data/generated/art-works.js` ← `works.json::art_works` → `window.__ART_WORKS_INLINE__`.
  - `data/generated/ex-statements.js` ← `works.json::exhibition_statements` → `window.__EX_STATEMENTS_INLINE__`.
  - `data/generated/ex-order.js` ← סדר ה-`slug` ב-`exhibitions.json` → `window.__EX_ORDER_INLINE__` (`["loneliness","how-many","the-peeler"]`).
  - `works/index.html #works-data` ← `art_works` (JSON מעוצב).
  - `works/<id>/index.html #artwork-data` ← הרשומה מ-`art_works` לפי ה-`id` שכבר בעותק (compact) + **fallback סטייטמנט**: `statement_he` של היצירה → אחרת `exhibition_statements[(artist_slug, exhibition_title_he)]` → אחרת בלי השדה.
  - `galleries/<slug>/index.html #g-artworks-data` ← `art_works` עם `gallery_slug == <slug>`, בסדר המערך, **בלי `hidden:true`**. סט השדות = מפתחות הרשומה הראשונה שכבר בעמוד (`id, artist_slug, artist_en, artist_he, title_he, title_en, img, w, h, widths`). **החריג היחיד לכלל "לא לערוך ביד": להוספת שדה להטלה — להוסיף את המפתח (בכל ערך) לרשומה הראשונה בעמוד, פעם אחת, ואז להריץ; הסקריפט דורס את כל הערכים מ-`works.json`.**
  - `#fallback-galleries` ב-`galleries/medina/`, `galleries/dizengoff/`, `curators/korin-avraham/` ← `galleries.json` verbatim.
- 🔴 **לא בבעלותו — ה-`<head>` של אף דף** (`<title>`, description, canonical/`og:*`/`twitter:*`/JSON-LD בבלוק `SEO:auto`): שינוי ב-JSON בטקסט שמופיע שם ⇒ עדכון ידני באותו קומיט — כותרת/אומן של יצירה → `works/<id>/`; שם/ביו/סטייטמנט של אומן → `artists/<slug>/`; כותרת/תאריך/שעה של אירוע → `events/<slug>/` (כולל `startDate`/`endDate`). עריכת הבלוק ביד, **לא** `inject.py` גורף. `--check` לא יתפוס head מיושן.
- **`search-index.js`** (לא של `sync_data.py`) — נבנה בכל קומיט ע"י `.githooks/pre-commit` → `python3 tools/search/build_index.py -q` + `git add search-index.js`, מ-`<title>`, description ושמות JSON-LD של כל `index.html` במעקב (בלי `noindex`/`_staging/`); פעיל כש-`core.hooksPath=.githooks` (per-clone). לא לערוך ביד; כשל בבנייה חוסם את הקומיט (CLAUDE.md כלל 10א).
- **לא סורק את `_staging/`** — רק `artists/*/`, `works/*/`, `galleries/*/` ו-`curators/korin-avraham/`; עמוד ב-`_staging/` נשאר עם `#artwork-data` קפוא, וגם בדיקת דפי האומן של `--check` לא רצה עליו. **אחרי החזרת דף משם — `sync_data.py` ואז `--check` מיד** (+ sitemap/canonical, כלל-זהב 15).
- ⚠️ **הערות ישנות בתוך דפים** שמורות לסנכרן ביד יעדים שבבעלות `sync_data.py` — מיושנות: מעל `#fallback-galleries` בדפי הגלריה, ב-`works/index.html`, ובכל 150 עמודי `works/<id>/` מעל `#artwork-data` ("copy this file, change <html data-artwork-id>, and swap #artwork-data"). ההערות "Keep in sync" / "MUST mirror" מעל ה-`#fallback-*` ב-`exhibitions/how-many|loneliness/`, `opencalls/*`, `events/ktuba/`, ו-"MIRROR SLICE" מעל `#g-exhibitions-data` — **נכונות** (§1.4).
- **שמות ישנים:** `tools/sync_works_mirrors.py` = wrapper שמריץ `sync_data.py`. `tools/migrate_exhibition_statements.py` = **פרוש** (**לא להשתמש בדגל `--i-know-this-is-retired`**).

### 1.3 דפי האומן וה-generated scripts
- כל `artists/<slug>/index.html` טוען `<script src="../../data/generated/<name>.js"></script>`: **41 דפים טוענים 4** (`artists`, `art-works`, `ex-statements`, `ex-order`); **3 דפי legacy** (`alon`, `dan-ben-ary`, `zohar-ron-dan-ben-ari` — בלי קיבוץ תערוכות/סטייטמנטים) טוענים 2 (`artists`, `art-works`).
- 🔴 **אסור להדביק דאטה לתוך דף אומן** (`<script id="artists-inline|art-works-inline|ex-statements-inline|ex-order-inline">window.__…__=…</script>`) ואסור לערוך `data/generated/*` (כלל-זהב 16). `--check` נכשל על עותק inline שחזר (**רק בצורת התג הישנה המדויקת**; `window.__…__=` בתג אחר לא נתפס, ואם הוא אחרי ה-`<script src>` הוא דורס בשקט) ועל `<script src>` חסר (`ex-statements`/`ex-order` נדרשים רק בדף עם `function buildExGroups(list){`).
- 🔴 **צורת התגים ומיקומם קבועים:** **מיד לפני** ה-`<script>` של הרנדרר (למשל `artists/aharon-bas/`, שורות 305–308), **סינכרוניים**, byte-exact — בלי `defer`/`async`/`?v=N` (שונה מ-`components/*.js?v=6`).
  - הרנדרר (IIFE) קורא את ה-globals בזמן ה-parse: רק ל-`__ARTISTS_INLINE__` יש fallback ל-`fetch`, והשאר נקראים כ-`window.__…__||[]` ⇒ הזזה/`defer` = יצירות, סטייטמנטים וסדר קבוצות נעלמים בשקט. `--check` בודק רק שהתגים **קיימים**, לא איפה; הוא מזהה אותם לפי המחרוזת המילולית (`SRC_RE`), ותג ששונה מדווח כ-"missing <script src>" (מטעה).
- `sync_data.py` **לא מנתח קוד renderer** (האילוץ הישן על בלוקי `NEW_JS`/`NEW_GROUP_JS` — **בוטל**; כלל ההפצה הזהירה חל). **יוצא-מן-הכלל:** המחרוזת `function buildExGroups(list){` משמשת את `--check` — לא לשנות את הניסוח (רווחים, שם פרמטר), אחרת הוא יפסיק לדרוש `ex-statements.js`+`ex-order.js` בשקט.
- **renderer/CSS** של דפי האומן per-file: 44 עותקים, כמה וריאנטים (standard / aharon-bas-variant / legacy / page-local), זהים פרט ל-`data-slug` ולתוספות page-local — ערוך אחד והפץ בזהירות. פירוט: `docs/routes/artists.md`.

### 1.4 Mirror registry — עותקים ידניים (לא בבעלות `sync_data.py`)
לכל שינוי במקור — לעדכן את העותק ביד באותו קומיט.

- **`events/index.html` · `#events-list-data`** (inline-only) ← `data/events.json`. מכיל **כל** האירועים, כולל עבר — הרנדרר מסנן. הטלה לכל רשומה:
  - `slug`, `date`, `gallery_id`; `alt` — **נכתב ביד כאן** (אין שדה מקביל ב-`events.json`)
  - `title_en` ← `list_title_en` אם קיים, אחרת `title_en`. ⚠️ בכמה רשומות הכותרת במירור שונה מ-`title_en` — ניסוח אחר (close-look, gala-night) או אותיות קטנות בלבד (loneliness, how-many, niki-de-saint-phalle-day, sumii-live-studio; מוצג UPPERCASE ממילא) — לא "לתקן" לפי הכלל.
  - `title_he` ← `list_title_he` (רק כשקיים; מחליף את הכותרת לעברית `.ttl--he`)
  - `img`/`w`/`h` ← `list_image` וממדיו; בלי `list_image` → קרופ/וריאנט של ה-hero (the-space-between: `hero-480w.webp` 480×726)
  - אופציונליים: `soon`, `pinned`, `date_tbd`, `widths`, `date_end` (§6.2 — הרנדרר קורא `date_end`: טווח תאריכים + פילטר לפי היום האחרון). `date_label` **לא** נכנס למירור — `/events/` מחשב את התווית.
  - **אירוע חדש = להוסיף ל-`events.json` וגם כאן** (+`list_image`).
  - ⚠️ הרנדרר: תווית הגלריה מטבלת `GALLERY` הקשיחה (`medina`/`dizengoff`/`flea-market` — **אין `berlin`** ⇒ אירוע בברלין דורש הוספה לטבלה, אחרת התווית ריקה), והקישור נבנה מ-`slug` (`<slug>/`), לא מ-`route` ⇒ תיקייה ששמה שונה מה-slug = 404. פירוט: `docs/routes/events.md`.
- **`artists/index.html` · `#artists-grid-data`** (inline-only) — `[{slug, name:"first\nlast", link?}]`: סדר תצוגה + שמות דו-שורתיים; `link` = slug של דף אחר שהכרטיס מקשר אליו (`dan-ben-ary` → `zohar-ron-dan-ben-ari`). **לא נגזר מ-`artists.json`** (הסדר = Figma `523:145` + הכרעות מאוחרות — `docs/routes/artists.md`). אומן בגריד = לערוך כאן + תמונות **810×810** `images/artists/grid/<slug>.{webp,avif}` **וגם** `<slug>-480w.{webp,avif}` (ה-srcset 480w+810w וה-`width`/`height` קבועים ברנדרר).
- **`galleries/<slug>/index.html` · `#g-exhibitions-data`** (inline-only) — slice של `exhibitions.json` לפי `gallery_id` עם שדות כרטיס (`slug, gallery_id, status, title_en, title_he?, volume_en?, start_date, end_date, img, w, h, srcset?, alt` — `img`/`srcset`/`alt` ביד, אין להם מקור ב-JSON). תמונת כרטיס: במדינה קרופ ייעודי `images/galleries/medina/ex-card-<slug>.webp`; בדיזינגוף ממוחזרת תמונה קיימת (`images/exhibitions/how-many/hero.webp`, `images/sponsors/sumii/hero-768w.webp`). **תערוכה חדשה = להוסיף ל-`exhibitions.json` וגם לסלייס של דף הגלריה** (+תמונת כרטיס).
  - דיזינגוף בלבד: רשומת **רזידנסי SUMII** (`slug:"sumii"`, `kind:"residency"`, `route:"sponsors/sumii/"`, `dates_text`, …) **קיימת רק כאן**. 🔴 לא להוסיף אותה ל-`exhibitions.json` — אינה תערוכה והייתה מזהמת את דירוג `__EX_ORDER_INLINE__`.
- **`curators/korin-avraham/index.html` · `#fallback-curators`** ← subset של `curators.json` (בלי `contact_email`, `credit_he`); **`#fallback-exhibitions-min`** ← subset של `exhibitions.json`. fetch-first. שדה חדש שהדף קורא — להוסיף גם לעותק. (`#fallback-galleries` באותו דף — generated.)
- **`exhibitions/how-many/`, `exhibitions/loneliness/` · `#fallback-site`** (subset מיושן: `brand` = רק `name_en`; `footer` בלי `social` ובלי קישור "מדיניות פרטיות"), **`#fallback-curators`** (subset — בלי `bio_he`/`contact_email`, ו-`exhibition_slugs` מיושן; הדפים קוראים ממנו את `credit_he`, שקיים), **`#fallback-exhibitions`** (subset; drift ידוע — בדף loneliness לרשומת how-many יש `start_date`/`end_date` = `null`, `docs/routes/exhibitions.md`). fetch-first.
- **`exhibitions/the-peeler/`** = סטטי קפוא, לא קורא דאטה — שינוי תוכן = עריכת HTML **וגם** הרשומה `the-peeler` ב-`exhibitions.json` (נקראת ע"י עמוד האוצרת: כותרות, `label_en`/`volume_en`, `hero_overlay_hide_en`, `curator_card_image`, `gallery_id` — ובעותק `#fallback-exhibitions-min` שלו), `ex-order.js`, `inject.py` (כותרת/תאריכים/hero), והסלייס `#g-exhibitions-data` במדינה (כותרת/תאריכים/סטטוס; תקדים: `end_date` → 2026-10-05, 2026-09-27). אומן חדש ב-strip ⇒ גם `artists[]` ברשומה. ⚠️ `gallery_images` ברשומה = ה-hero בלבד; הדף (7 שקופיות) הוא מקור האמת. `docs/routes/exhibitions.md`.
- **`opencalls/{obsession,how-many,the-peeler}/` · `#fallback-site`** (עותק מלא של 5 המפתחות העליונים של `site.json`, בלי `$schema`), **`#fallback-opencalls`** (subset; **כל עותק מחזיק את כל 3 הרשומות** — obsession, the-peeler, how-many ⇒ שינוי ברשומה כלשהי = שלושת הקבצים). fetch-first.
  - ⚠️ בארבעת הדפים **אף ערך מ-`site.json` לא מרונדר** (ה-footer מ-`site-chrome.js`; ב-`exhibitions/*` ל-`footer_*` שב-ctx אין `data-bind`; ב-`opencalls/*` `rowHtml()` לא נקרא). 🔴 **לא למחוק את `#fallback-site` ולא לקצץ אותו:** `loadJson` זורק כשה-fetch נכשל ואין עותק, ו-`Promise.all` מחליף את הדף ב-"failed to load" (file://); ו-`exhibitions/*` ניגשים מחוץ ל-try ל-`site.footer.newsletter.{title,placeholder,cta}`, `site.footer.copyright`, `site.footer.links_he` (ו-`opencalls/*` ל-`site.footer.links_he`) — עותק מקוצץ (`{}`) זורק TypeError והדף נתקע בטעינה.
- **`events/ktuba/index.html` · `#fallback-ktuba-artists`** ← `events.json::ktuba.artists` (אותם `name_en`/`slug`, ל-`image` מתווסף `../../`). inline-only (ההערה בדף "rendered from events.json" מטעה — הקוד קורא רק את התג).
- **דפי אירוע עם רצועת צילומים (`event_photos[]`)** (close-look, natasha-zeriker, risa-and-noemi, noemi-safir, livay-levi, maria-artamonova, jessica-tabarovsky, bar-cohen, hadas-tuval, sumii-opening) — שקופיות סטטיות ב-HTML ← `events.json::<slug>.event_photos[]` (+`figma_node_photos_*`, `photo_credit_*`); הוספה/הסרה/שינוי סדר או alt = בשני המקומות.
  - ⚠️ גם ב-`events/gala-night/` וב-`events/how-many/` (`section.event-moments`) וב-`events/loneliness/` (`section.moments`) יש גריד "moments from the opening" — תמונות אפויות בלי מקור ב-JSON; **אינן** מירור של `event_photos[]` — לא להוסיף להן `event_photos`.
- **`index.html` (עמוד הבית) — כל הסקשנים HTML כתוב ביד.** `homepage.json` ורשומות שהוא מפנה אליהן **דקלרטיביים** (העמוד לא קורא אותם). בפרט:
  - `#press` ← `press.json::homepage_visible` + `homepage.json::press_section.item_ids` (חייבים להתאים זה לזה ולכרטיסים; 13 ⇔ 13 ⇔ 13).
  - `#galleries` (שמות/כתובות/שעות) ← `galleries.json` — שינוי שעות = `galleries.json` **וגם** `.gallery-card .hours` ב-`index.html`.
  - `#mobile-cta` / `#opencall` (כרטיסי הקול הקורא) ← `opencalls.json` (`card_image`; `status`/`deadline`/`city` → התוויות status · date · location) + `homepage.json::mobile_cta` / `open_call_section`.
  - `.announce` (ה-marquee) ← `site.json::announcement` — 20 `span`-ים ביד + `aria-label` (וגם `#fallback-site` בשני דפי הקול הקורא); `docs/routes/homepage.md`.
  - שאר הבלוקים (`x_our_artists`, `big_news`, `perfume_promo`, `sumii_sponsor`, `soos_sponsor`, `tribe_teaser`, `galleries_berlin_section`…) ← `homepage.json`.
- **`contact/index.html` · בלוק "שעות פתיחה" (`.info-block`)** ← שעות מדינה (`galleries.json`), בפורמט משלו: סדר לוגי פתיחה–סגירה עם en-dash, `·` ו-`׳` (`ו׳ · 10:00–14:00`) — **הפוך** ממחרוזת ה-bidi של `hours[].time` (§3), לכן לא מעתיקים אותה. ⚠️ מיושן מאז 2026-08-12 (עדיין `א׳–ה׳ · 10:00–19:00`; בבלוק "גלריות" שמעליו דיזינגוף "בקרוב" למרות `status:"open"`). שינוי שעות מדינה = לעדכן גם כאן, או לשאול את המשתמש.
- **`press/index.html` · כרטיסי `.pcard` סטטיים** ← `press.json` (+ לאירועים `data-kind="event" data-date="YYYY-MM-DD"`; לרב-יומי גם `data-date-end` ותווית `<bdi>` = `date_label`; `data-pinned` כשרלוונטי). ביד. כרטיס `.pcard--soon` (`href="#"` + טוסט "בקרוב") — רק tal-nehoray. `docs/routes/press.md`.
- 🔴 **`sponsors/sumii/index.html` · כרטיסי FIGURES + PRODUCTS (HTML סטטי)** ← `works.json::art_works`: `shira-turbowicz-1..3` (FIGURES), `melani-hekimoglu-1..5` (PRODUCTS). כל כרטיס מעתיק ביד: נתיב `img` (`images/works/v2/<img>.webp`), `width`/`height`, `widths` של ה-srcset, כותרת (FIGURES: `title_he | <span class="lat">title_en</span>`, כשהשנים שב-`title_he` עטופות `<bdi dir="ltr">…</bdi>` — shira-turbowicz-2/3, לא להעתיק כמו-שהוא; PRODUCTS: `title_en` בלבד) והקישור `../../works/<id>/`. אין script דאטה ⇒ **`sync_data.py` לא נוגע בו**: שינוי באחת מ-8 הרשומות (כותרת, תמונה/ממדים, id, מחיקה) = `sync_data.py` **וגם** עריכת הכרטיס, באותו קומיט. טקסטי התיאור: FIGURES — רק בעמוד; PRODUCTS — זהים ל-`details_he` חוץ מ-melani-hekimoglu-5 (בעמוד נקודה אחרי "Flow") — שינוי `details_he` = לעדכן גם כרטיס. `docs/routes/sponsors.md`.
- **טבלאות lookup ידניות בקוד:** `FOCAL_POINTS` (object-position לפורטרט) בכל 44 דפי האומן; `_ARTIST_FOCAL` ב-`events/ktuba/` ובתבנית `exhibitions/how-many|loneliness/`; `_ARTIST_SLUGS` (שם→slug) באותה תבנית; `CURATORS` (slug→שם+thumb) ו-`NAME_LINKS` (שם→קישור בסטייטמנט) ב-`artists/shira-turbowicz/` וב-`artists/melani-hekimoglu/` (`NAME_LINKS` גם ב-`works/melani-hekimoglu-1..5/`); `HERO_DIMS` (slug → ממדי hero) ב-`opencalls/how-many/` וב-`opencalls/the-peeler/` — החלפת `opencalls.json::hero_image` או קול קורא חדש = לעדכן **בשני הקבצים** (+ וריאנטים 480/768/1080 ואחי avif; כלל-זהב 12; `docs/routes/exhibitions.md`); `GALLERY` ב-`events/index.html`. **עדיפות לשדות הדאטה** (`artists.json::portrait_focus`, `exhibitions.json::artists[].focus` / `.slug`) — לא להרחיב את הטבלאות.
- **גופי כתבות/אירועים/ספונסרים** (long-form) חיים ב-HTML; ב-JSON רק meta/תקציר. אין סנכרון אוטומטי — שינוי meta (תאריך, כותרת, route) = לשנות גם בדף.

### 1.5 עמוד יצירה חדש (`works/<id>/`)
- להעתיק דף קיים **מוריאנט renderer שמכסה את הצרכים** (collab ⇒ דף עם `w.collab`, למשל `works/livay-levi-3/`; `docs/routes/works.md`), להחליף `data-artwork-id`, meta ו-OG (`og/works-v2-<id>.jpg`), ולזרוע **בשורה אחת בדיוק, בלי רווח/שורה חדשה בין התגים ל-JSON:** `<script type="application/json" id="artwork-data">{"id":"<id>"}</script>`. `sync_data.py` ממלא את הרשומה (לפי ה-`id` שבעותק); **לא** להדביק רשומה מלאה ביד.
- 🔴 **ה-id החדש חייב להיכנס גם ל-`#artwork-data` וגם ל-`data-artwork-id`.** אם נשאר ה-id הישן ב-`#artwork-data`, הסקריפט ימלא אותו בשקט ברשומה של היצירה **הישנה**.
- 🔴 **כשלים שקטים:** רווח/שורה חדשה **לפני** ה-`{` ⇒ הדף **מדולג בלי אזהרה**; **אחרי** ה-`}` ⇒ מדולג, או — אם בהמשך הקובץ יש `}</script>` — קריסה ב-`json.loads`; id שלא קיים ב-`works.json` ⇒ רק אזהרה ל-stderr והדף מדולג; רשומה מלאה מעוצבת שהודבקה ביד ⇒ אותו דילוג. **בכל סוגי הדילוג `--check` נשאר ירוק** — אחרי יצירת עמוד לוודא שה-`#artwork-data` התמלא ברשומה המלאה.
- **דף גלריה חדש (עתידי):** לזרוע `<script type="application/json" id="g-artworks-data">[]</script>` — רשימה ריקה ⇒ ההטלה נופלת לסט ברירת המחדל (`G_ARTWORK_FIELDS` בסקריפט). `#fallback-galleries` מתמלא **רק אם התג כבר קיים** — לזרוע `<script type="application/json" id="fallback-galleries">{}</script>`. דף בלי התגים לא מסונכרן (בלי שגיאה).

### 1.6 כתיבת סקריפט הזרקה משלך
- סקריפט שמזריק JSON ל-HTML: `json.dumps` + slicing או replacement **function** — **לא** מחרוזת החלפה ל-`re.sub`; אחרת `\n` שבתוך ה-JSON הופך לתו-שורה אמיתי ושובר את ה-JS.

### 1.7 שינוי שנוגע בהרבה דפים
- חובה regression harness (כלל-זהב 17, CLAUDE.md §7.1) עם **אותם `--only`/`--widths` בשני הצילומים** (דף שקיים רק בצד אחד = הבדל); `diff.mjs … --dom` מציג diff DOM; exit 1 בשינוי שאמור לשנות פלט — לוודא שהשתנו **רק** הדפים המיועדים. הדפים = כל `*.html` במעקב + חדשים שאינם ignored (בלי `trash/`, `_staging/`, `node_modules/`). הפלט **מחוץ לריפו**: `$REGRESS_OUT/<label>` (ברירת מחדל `<os tmpdir>/zrp-regress/<label>` — בגלל עותקי-קונפליקט של iCloud; ה-`.regress/NAME` בטקסט העזרה מיושן).
- לפני הפצה גורפת — `git commit` (כלל-זהב 14); שחזור תבנית — מ-git HEAD, לא מדף אחר.

## 2. `site.json`
- מבנה: `brand` (`name_en`, `name_he`, `tagline_en`, `founder`, `logo`), `nav[]` (`key`, `label_en`, `href`), `footer` (`newsletter{title,placeholder,cta}`, `links_he[]{label,href}`, **`social[]{platform,url}`**, `copyright`), `announcement`, **`contact{instagram_handle}`** (`social` תחת `footer`).
- דקלרטיבי: ה-nav וה-footer מרונדרים ע"י `components/site-chrome.js` (ערכים hard-coded שם). שינוי nav/footer = `site-chrome.js` **וגם** `site.json`.
- נטען (fetch-first + `#fallback-site`) ע"י `exhibitions/how-many|loneliness/` ו-`opencalls/*`, אבל **אף ערך לא מרונדר**. ⚠️ לא למחוק את `#fallback-site` ולא לקצץ אותו (§1.4).
- טופס הניוזלטר בפוטר = Wix Velo (`site-chrome.js` → `zrp.co.il/_functions/subscribe`), לא Firebase — לא קשור ל-JSON הזה.

## 3. `galleries.json`
`{ galleries: [...] }` — 6: `medina`, `dizengoff`, `zr-station`, `flea-market`, `berlin`, `barcelona` (סדר המערך = סדר הכרטיסים בהומפייג').
- `id`, `slug`
- `name_he`, `name_en`; `address_he`, `address_en`; `city` (`"tel aviv"` / `"berlin"` / `"barcelona"`)
- `status`: `open` | `coming-soon` | `closed`
- `hours[]`: `{days_he, days_en, time}` — `time` nullable ("שבת סגור"); `[]` = אין בלוק שעות. ⚠️ **`time` שמור בקונבנציית bidi `"18:00-11:00"`** — הכרעת משתמש: ספרות נשמרות/מוצגות LTR כמו בטקסט הגולמי של Figma, **לא "לתקן" את הסדר**.
  - דוגמה: פתיחה 10:00 וסגירה 15:00 ⇒ `"time":"15:00-10:00"`; `10:00-15:00` על המסך = מחרוזת הפוכה. JSON-LD (`opens`/`closes`) = סדר לוגי.
  - עותקים ידניים: `.gallery-card .hours` בהומפייג', ה-JSON-LD בשני דפי הגלריה, ו-`contact/` (מדינה בלבד, פורמט אחר — §1.4).
- `image_hero` — תמונת כרטיס ההומפייג' (null לפשפשים — כרטיס ירוק שטוח).
- `route` (nullable) — `galleries/<slug>/`; null = אין דף (פשפשים, ברלין).
- `image_page_hero` — hero של דף הגלריה, **נפרד** מ-`image_hero`.
- `address_street_en` / `address_area_en` — הכתובת בדף הגלריה, verbatim מהפיגמה — **חוץ מ:** 🔴 דיזינגוף = `1 Reines st. tel aviv` (הכרעת משתמש 2026-08-13: הרחוב על שם הרב ריינס; "Raines" בפיגמה = typo). **לא להעתיק "Raines" בחזרה** — גם לא ל-`events.json::address_en` (5 אירועי how-many בדיזינגוף) ולא לשורות הכתובת בדפי `events/*`.
- `manager` (nullable) — `{name_en_first, name_en_last, email, portrait{src,width,height,alt_he,figma_image_ref}, note}`. `email` **lowercase** (ל-`mailto:`; התצוגה UPPERCASE). נטלי זיגל = אותה מנהלת במדינה ובדיזינגוף (פורטרט משותף `images/galleries/managers/natalie-zigel.webp`). ⚠️ פער Zigel/siegel באימייל — פתוח (`docs/todo.md`). ⚠️ כפילות ידנית ב-`about/index.html` (פורטרט נפרד `images/about/people/`, `mailto` עם N גדולה) — `docs/routes/about.md`.
- `figma_node_desktop` / `figma_node_mobile` (כרטיס), `figma_page_desktop` / `figma_page_mobile` (דף הגלריה), `note`.
- אופציונליים (ברלין): `address_lines_en[]`, `address_lines_en_mobile[]`, `instagram_handle`, `instagram_url`. (zr-station): `subtitle_he` ("תחנת השידור"), `subtitle_en` — שורות המשנה מתחת לשם בכרטיס.
- **צרכנים:** `galleries/<slug>/` (lookup לפי `slug`) ו-`curators/korin-avraham/` (לפי `id`, רק `name_en` לכרטיסי התערוכות) — fetch-first; `#fallback-galleries` **generated**. דפי הגלריה קוראים בזמן ריצה רק: `name_he`, `address_street_en`/`address_area_en`, `hours[]`, `manager` (שם, `email`, `portrait.alt_he`). ⚠️ `image_page_hero` ו-`manager.portrait.src` **דקלרטיביים** — ה-hero והפורטרט סטטיים ב-HTML; החלפת תמונה = HTML (וגם JSON). + `inject.py`, וכרטיסי `#galleries`/`#galleries-berlin` בהומפייג' (ידני, §1.4).
- 🔴 **שינוי שם/כתובת של גלריה — עותקים ידניים מחוץ ל-`sync_data.py`:**
  - `index.html`: כרטיסי `#galleries` (`.name`/`aria-label`/`.addr`/`.hours`), `.gname` ב-`#exhibitions-now`, ה-alt של פוסטרי `#events-upcoming`, `.nb-sub-addr` (+ `homepage.json::big_news.address_he`, `exhibitions_now.groups[].cards[].gallery_name_en` לברלין).
  - בלוק ה-SEO של דף הגלריה (title/og/twitter/JSON-LD; `streetAddress` בשני הדפים; במדינה גם הכתובת העברית ב-description/og:description).
  - שורות הכתובת בדפי `events/*` + `events.json::address_en`; `contact/index.html`; חלק מכתבות `press/*` (⚠️ טקסט מצוטט מכתבה חיצונית, כמו כותרת וואלה, כנראה נשאר כפי שפורסם — תקדים `press/the-shared-list/`; לא הוכרע).
  - (א) הפוטר ב-`components/site-chrome.js` — שמות הגלריות בעברית ב-`.footer-menu` (דסקטופ) ו-`.footer-mobile-mini` (מובייל) — **וגם** `site.json::footer.links_he` ועותקי `#fallback-site` שלו (`exhibitions/how-many|loneliness/`, `opencalls/*`).
  - (ב) **`gallery_label_he`** — עותק של שם הגלריה ב-`events.json`, `exhibitions.json`, `opencalls.json`, מרונדר בזמן ריצה ב-`exhibitions/how-many|loneliness/` וב-`opencalls/*` ⇒ גם `#fallback-exhibitions`/`#fallback-opencalls` ו-`exhibitions/the-peeler/` הקפוא (badge + description/og/twitter).
  - (ג) `works.json::art_works[].gallery_en` בכל 150 הרשומות (נפרד מ-`name_en`) ⇒ `sync_data.py`. (ד) טבלת `GALLERY` ב-`events/index.html`.
  - (ה) ה-`<head>` (§1.2) של דפים שמזכירים את הגלריה (אירועים, ספונסרים, חלק מדפי האומנים והיצירות) ו-`tools/seo/overrides.json` (תיאורים ש-`inject.py` מזריק מחדש); צ'יפ הגלריה בראש `sponsors/soos/` ו-`sponsors/sumii/`. מופעים ב-`#fallback-galleries` — `sync_data.py` בלבד (`docs/routes/galleries.md`).
  - **לחפש** את הערך הישן בכל הצורות (אנגלית/עברית, `'` וגם `׳`): `grep -rliE "jabotinsk[iy]|ז('|׳)בוטינסקי" --include='*.html' --include='*.json' --include='*.js' --exclude-dir=node_modules . | grep -vE '^(\./)?(trash|docs/history|data/generated|search-index\.js)'` (שני האחרונים מיוצרים) (דיזינגוף: `reines|ריינס`). ⚠️ `('|׳)` ולא `['׳]` — ב-locale C BSD grep מפספס בשקט תו עברי רב-בייטי בתוך `[…]`. ⚠️ ב-natasha-zeriker (בדף וב-`events.json`) הכתיב `jabotinski` — `docs/routes/events-talks.md`. לשם גלריה — אותו חיפוש בעברית ובאנגלית (לדיזינגוף: `דיזינגוף`/`דיזנגוף`).
- ⚠️ פער פתוח (לא הוכרע, `docs/todo.md`): בכרטיס הפשפשים ב-`index.html` השם "גלריית יפו, שוק הפשפשים" והכתובת "שוק הפשפשים, יפו"; ב-JSON: `name_he` "גלריית שוק הפשפשים", `address_he` "שוק הפשפשים, תל אביב" (הכתובת — כך גם ב-Figma). בכרטיס מדינה בפיגמה אין כתובת רחוב (האתר מציג).

## 4. `artists.json`
`{ artists: [...], _pending_artist_pages: [...], _note }`
- `id`, `slug` (= שם התיקייה `artists/<slug>/`)
- `name_he`, `name_en` — כתיב קנוני; כתיב עברי של אומן בכל מקום אחר באתר (כולל `works.json::artist_he`) = הכתיב של הקובץ הזה.
- `portrait` (נתיב); `portrait_focus` (אופציונלי, object-position לפורטרט; עדיפות ברנדרר: `portrait_focus` → טבלת `FOCAL_POINTS[slug]` בכל עותק תבנית → `center 25%`. לאומן חדש — להעדיף את השדה, בלי הפצה).
- `work_image` — מוצגת **רק בדף placeholder** (כש-`bio_he` ריק וגם `works[]` ריק): `work_image || portrait`. ה-hero הרגיל לא קורא אותו.
- `bio_he`, `bio_en` (nullable). פסקאות מופרדות ב**שורה ריקה** (`\n\n`); `\n` יחיד בתוך פסקה = `<br>`; שורה בלי עברית = `.en-line` (Copperplate). **הפסקה הראשונה = intro** (נפרדת מהגוף, לפני ה-divider — כשיש יותר מפסקה אחת).
- `works[]` — אובייקטים **inline** `{id, title, image, year?, medium?}` (לא ref ל-`works.json`). רק fallback: דף האומן מציג את `works.json::art_works` המסוננים (`artist_slug === slug || artist_pages.includes(slug)`); **רק אם אין אף רשומה** → `artists.json works[]` (שם+כותרת+medium).
- `instagram_handle` (nullable) — **עם `@` מוביל** (`"@galro.art"`); `heroHandleLink` ו-`inject.py` (`sameAs`) מסירים אותו רק לבניית ה-URL (`curators.json` שומר בלי `@`). handle בפיגמה שהוא leftover של אומן אחר → `null` עד שיש handle אמיתי; `null` רק ב-`dan-ben-ary`.
- `hero_images[]` — דואו תמונות hero; `hero_image_focus[]` — object-position לכל תמונה בדואו (אינדקס מקביל).
- `hero_collab` — hero שיתופי: `{artists:[{name_en:[שורות], bio_he_short, instagram}]}` (≥2; `name_en` **מערך שורות**, לא מחרוזת), Figma מובייל `119:3917` (⚠️ fileKey לא מתועד). רק `zohar-ron-dan-ben-ari`.
- `figma_artist_page_desktop` / `figma_artist_page_mobile`. ⚠️ `homepage_featured` (בכל 44) — אין צרכן בקוד.
- **אופציונלי `studio_en`** — שם סטודיו; ה-hero מציג שם מלא בשורה אחת + הסטודיו מתחת. **page-local** ב-`heroNameParts` של `tali-zelnik` ("piece of mine studio") ו-`shira-turbowicz` ("sumii") בלבד — אומן שלישי צריך את הלוגיקה בדף שלו.
- **אופציונלי `curator_slug`** — slug מ-`curators.json`; רצועת `the curator` אחרי היצירות (לאומן שמציג מחוץ לתערוכה רגילה, למשל רזידנסי). page-local ב-`shira-turbowicz` ו-`melani-hekimoglu` בלבד. 🔴 הרנדרר **לא קורא את `curators.json`**: שם/thumb מטבלה hard-coded `var CURATORS={'korin-avraham':{…}}` בכל אחד משני הדפים — slug אחר (או שינוי שם/תמונה של האוצרת) דורש עריכת הטבלה בדף (§1.4).
- **אופציונלי `works_caption_each_image`** — `true` = כיתוב תמיד מתחת לכל תמונה (כשכותרות זהות אך ההקשר How Many ולא loneliness). רק `zohar-ron-dan-ben-ari`. ⚠️ לא נמצא צרכן בקוד (grep 2026-09-27) — מתועד כחוזה.
- ⚠️ `works_grid_order` (12 רשומות) — אין צרכן בקוד.
- `hidden` (אופציונלי, לא בשימוש) — **דפי האומן מתעלמים ממנו**; הסתרה אמיתית = העברת התיקייה ל-`_staging/` (gitignored ⇒ 404). `docs/routes/artists.md`.
- `_pending_artist_pages` (עליון) — אומנים שחסר להם תוכן (`dan-ben-ary`, `racheli-reuven`). ⚠️ רשימת מעקב, לא מתג: placeholder רק כש-`bio_he` ריק **וגם** `works[]` ריק (לא סופר `art_works`) — racheli-reuven (`bio_he` = "רחלי ראובן") מרונדרת כדף רגיל; רק dan-ben-ary (`bio_he` null) = placeholder.
- **צרכנים:** כל `artists/<slug>/` (דרך `data/generated/artists.js`), `inject.py`. אחרי שינוי → `sync_data.py`.

## 5. `exhibitions.json`
`{ exhibitions: [...], archive_thumbnails, _note }`
- 🔴 **סדר המערך = כרונולוגי עולה (ישן→חדש)**, מקור-האמת לדירוג "התערוכה החדשה למעלה" בדפי האומנים (`__EX_ORDER_INLINE__`; הכרעת משתמש 2026-08-12). **תערוכה חדשה נוספת בסוף המערך**, ואז `sync_data.py`. `loneliness` → `how-many` → `the-peeler`.
- שדות: `id`, `slug`, `label_en`, `volume_en`, `title_he`, `title_en`, `subtitle_he` (nullable), `status` (`current` | `upcoming` | `archived`), `status_label_en`, `gallery_id`, `gallery_label_he`, `start_date` / `end_date` (`YYYY-MM-DD`), `hero_image`, `hero_letter_heading_en`, `thumbnails[]` (ריק; חסר ב-the-peeler), `gallery_images[]`, `figma_node_desktop` / `figma_node_mobile`.
- `volume_en`: ל-`how-many` ול-`the-peeler` **שניהם `"VOLUME 2"`** — verbatim מ-Figma, הכרעת משתמש 2026-06-25; **לא "לתקן" ל-VOLUME 3** (`docs/routes/exhibitions.md`).
- `description_he` — פסקאות `[{weight, lines:[...]}]` (`weight`: `regular`/`light`…). ⚠️ `description_en` ו-`artist_ids[]` מהחוזה הישן **לא קיימים בדאטה**.
- `artists[]` — פריט: `name_en` (`\n` = שבירת שורה), `thumb`, `slug` (אופציונלי — בלעדיו התבנית מחפשת לפי `name_en` בטבלת `_ARTIST_SLUGS` שבדף; בלי התאמה הכרטיס לא קליקאבילי), `focus` (אופציונלי, object-position; אחרת טבלת `_ARTIST_FOCAL` → `center 25%`), `artist_page_slug` (אופציונלי = הכרטיס מקשר לדף אומן **אחר** — לשיתופי פעולה; zohar-ron ב-how-many → `zohar-ron-dan-ben-ari`).
- `curator_slug` (אופציונלי) — slug מ-`curators.json`; סקשן אוצרת מתחת לאומנים בדפי התבנית (how-many/loneliness).
- `hero_overlay_en_only` (אופציונלי, `true`) — אוברליי תמונת הגיבור מציג רק `title_en`, בלי פס volume / כותרת עברית (how-many). נקרא ע"י דפי התבנית ועמוד האוצרת.
- `hero_overlay_hide_en` (אופציונלי, `true`) — האוברליי מציג title-bar + `title_he` בלי הכותרת האנגלית; `title_en` נשמר ל-`<title>`/OG/SEO (the-peeler). נקרא רק ע"י עמוד האוצרת — עמוד the-peeler קפוא ולא קורא JSON.
- `curator_card_image` (אופציונלי) — תמונת הכרטיס בעמוד האוצרת (אחרת `hero_image`); the-peeler. ⚠️ המידות קשיחות ב-`buildCard` (822×1243 + חובה אח `-480w`; hero: loneliness 690×1044, השאר 1068×1600) — תערוכה במידות אחרות = לעדכן את `buildCard` (CLS). `docs/routes/exhibitions.md`.
- ⚠️ `archive_thumbnails` (עליון) — שריד ארכיון הטאבים הישן (הוחלף 2026-06-08); אין צרכן; רדום. `homepage.json::exhibitions_archive` לא מפנה אליו (`items[]`, §10).
- `the-peeler`: העמוד קפוא, אבל הרשומה נקראת במקומות אחרים — כל שינוי בדף = לעדכן גם אותה (§1.4). `end_date` = 2026-10-05 (גם ב-`#g-exhibitions-data` של מדינה).
- **כותרת loneliness הרשמית = "בדידות בתוך סביבה תוססת"** (Audit 2026-07-09; אם ב-Figma "בתוך בסביבה" — טעות מוכרעת, לא לשחזר). כותרות הקבוצה ב-`works.json` הן "בדידות בסביבה תוססת" — מפתח-join (§9.3); לא לשנות בלי כל הצדדים.
- **צרכנים:** `exhibitions/how-many|loneliness/` (`#fallback-exhibitions`), עמוד האוצרת (`#fallback-exhibitions-min`), `#g-exhibitions-data` (ידני), `data/generated/ex-order.js`, `inject.py`. רזידנסי (SUMII) **אינו** תערוכה ולא נכנס לכאן (§1.4).

## 6. `events.json`
`{ events: [...] }` — אירוע = רשומה. רוב דפי האירוע **סטטיים**; ה-JSON הוא meta. הצרכן החי העיקרי = המירור `#events-list-data` (§1.4).

### 6.1 שדות בסיס
- `id`, `slug` (= `events/<slug>/`). 🔴 slug תפוס (אומן עם אירוע קודם) → slug לפי הגלריה: `zohar-ron-medina`, `nir-giorgio-levin-medina` (כלל-זהב 6).
- `title_he`, `title_en` (הכותרת הקנונית של הדף), `subtitle_he` (nullable).
- `date` (`YYYY-MM-DD`; ברב-יומי = יום ההתחלה — `date_end`, §6.2), `date_he`, `time_start`, `time_end` (nullable) — הסדר המכונתי; ה-`startDate`/`endDate` ב-JSON-LD של הדף (ידני, §1.2) תואמים. `time_label` (אופציונלי) — מחרוזת התצוגה **verbatim מהפיגמה**: ברוב שיחות האמנים סוף-התחלה בקונבנציית bidi (`"20:30-18:30"`), אבל התחלה-סוף ב-gala-night (`"19:30-21:30"`), yom-kippur-wish-tree ו-sumii-live-studio (`"10:00-14:00"`), ו-risa-and-noemi `"11:00"` — לא לנרמל. אף קוד לא קורא את שדות השעה — התצוגה בדף ביד.
- `gallery_id`, `gallery_label_he`, `address_en[]` (שורות כתובת; דיזינגוף = `1 Reines st. tel aviv` — §3).
- `exhibition_id` — `null` = אירוע בלי שיוך תערוכה (אין פס `presented as part of`); `exhibition_volume`.
- `cover_image` (hero; null לאירוע בלי דף), `description_he` (מערך שורות או מחרוזת; `inject.py` גוזר ממנו את ה-description וה-JSON-LD של הדף).
- `artists[]` — `{name_en, slug, image}` (רצועת האומנים); `artists_he`.
- `route` (nullable) — `events/<slug>/`; `null` = אין דף (לכל 30 הרשומות יש דף).
- `figma_node_desktop` / `figma_node_mobile`, `figma_file`.
- `card_title_en` — כותרת קצרה לכרטיס (ל-`#events-upcoming`; **הקרוסלה הוסרה 2026-08-04 ⇒ אין צרכן**); בכל הרשומות (`null` בחמשת אירועי וריאנט רזידנסי SUMII — sumii-opening, sumii-melani-hosting, yom-kippur-wish-tree, niki-de-saint-phalle-day, sumii-live-studio) — להמשיך למלא לפי "שדה חדש → לכל הרשומות", לא למחוק.
- `homepage_visible` — ⚠️ לא נקרא ע"י שום קוד, ולא מסונכרן עם `press.json::homepage_visible` (the-space-between: `true` כאן, `false` שם). ההומפייג' נקבע ע"י `press.json` + `homepage.json` (§7).
- ברשומות בודדות: `gallery_images[]`, `gallery_videos[]`, `poem_he`, `statement_title_en`, `statement_he`, `note_en`, `note_he`.
- ⚠️ **כיסוי מפתחות לא אחיד** — "שדה חדש → לכל הרשומות" לא נאכף כאן היסטורית: רשומות ישנות (loneliness, how-many, ktuba, close-look, artist-talk) חסרות חלק מ-`address_en`/`artists`/`date_he`/`figma_file`/`subtitle_he`/`time_end`/`time_label`; the-space-between בלי `subtitle_he`/`time_label`; sumii-melani-hosting בלי `time_label`; sumii-opening בלי `description_he` (ה-description שייגזר ממנו ריק); `exhibition_volume` רק ברשומות עם תערוכה. לבדוק כיסוי בפועל.

### 6.2 שדות אופציונליים
- `day_he` — יום־בשבוע, מוצג במטא במקום שעה (the-space-between).
- `host_he` — מנחה/יזם אורח שאינו אומן האתר ⇒ **בלי קישור לדף אומן**.
- `list_image` — קרופ רוחבי לכרטיס ב-`/events/` (רינדור-node אפוי `images/events/<slug>/list-card.webp`, או מיחזור קרופ קיים). בלעדיו → cover של ה-hero.
- `list_title_en` — כותרת הכרטיס כשהמעצבת ניסחה אותה אחרת מהפריים של הדף; מזין את `#events-list-data` ואת הכרטיס ב-`/press/`, בעוד `title_en` קנוני לדף (bar-cohen: `"…bar cohen - ‘akra’"` בכרטיס מול `"…bar cohen ‘akra’"` בדף).
- `list_title_he` — כותרת הכרטיס **בעברית** במקום אנגלית; ב-`.ttl--he` (FbEzmel, px verbatim 16/14, `dir=rtl`) במקום Copperplate. (the-space-between.)
- `soon` (`true`) — אירוע בלי דף → כרטיס לא-קליקאבילי + טוסט "בקרוב". **דורש `route:null`.** אין שימוש חי: ארבע הרשומות שנשאו אותו (sumii-opening, nir-giorgio-levin-medina, yom-kippur-wish-tree, sumii-melani-hosting) קיבלו דפים ב-2026-09-27 והמפתח **נמחק** (לא `null`); הענף ברנדרר נשאר. ב-`/press/` נשאר כרטיס `.pcard--soon` יחיד — tal-nehoray (רק `press.json::event-tal-nehoray-talk`, `route:null`). **כשנבנה דף:** למחוק `soon` (ב-JSON ובמירור), למלא `route` ב-`events.json` **וב-`press.json`, `cover_image` ו-`description_he` (`card_title_en` — אין צרכן, אפשר `null`), להפוך את כרטיס `.pcard--soon` (`href="#"`) לקישור רגיל, ולהוסיף ל-`sitemap.xml`.
- `pinned` (`true`) — הכרטיס שורד את פילטר התאריך ב-`/events/` (אירוע שהמעצבת עדיין מציגה בפריים הרשימה אחרי שעבר). **שלושה מקומות לסנכרן:** `events.json`, המירור `#events-list-data`, ו-`data-pinned="1"` בכרטיס ב-`press/index.html` (בית אחד לכל אירוע); להסיר בשלושתם כשהוא יורד מהפיגמה. אין רשומה עם `pinned` (הוסר מ-michael-konovalenko ו-livay-levi ב-2026-09-01 — לא להחזיר); הענפים בקוד נשארו.
- `date_tbd` (`true`) — תאריך לא ידוע ("פרטים ותאריך בהמשך"), `date:null`; תמיד "upcoming", ממוין בסוף. אין רשומה; הענף ברנדרר נשאר. 🔴 אותו ענף תופס גם `date` חסר/לא-ISO במירור — בשקט (§6.3).
- `date_end` + `date_label` — אירוע רב-יומי: `date` = יום ההתחלה, `date_end` = היום האחרון (חסר = יום אחד); שתי הרשימות מסננות לפי היום האחרון (§6.3), ו-`/events/` מחשב לבד `d.m.yyyy - d.m.yyyy`. `date_label` = התווית verbatim של כרטיס `/press/` (ב-`<bdi>`, **פורמט אחיד `d.m.yyyy - d.m.yyyy`**; yom-kippur אוחד ל-`17.9.2026 - 18.9.2026`) — מידע בלבד, שום רנדרר לא קורא אותו. ⚠️ `date_label` של yom-kippur-wish-tree ב-`events.json` עדיין `17.09.26 - 18.09.26` — ליישר כשנוגעים. **חמישה מקומות לסנכרן:** `events.json` (`date`/`date_end`/`date_label`), המירור (`date`/`date_end`), `data-date` + `data-date-end` בכרטיס ב-`press/index.html`, התווית הגלויה ב-`<bdi>` (= `date_label`), ו-`press.json` (`date`/`date_end`). שימוש חי: yom-kippur-wish-tree, sumii-melani-hosting, sumii-live-studio.
- `route` במירור + `date_start_only` / `date_text` / `gallery_label` / `list_title_he_suffix` (במירור `title_he_suffix`) (2026-10-15, אופציונליים — רק ברשומות שמשתמשות בהם) — כרטיסי `/events/` שמקשרים מחוץ ל-`events/` (פופ-אפים/קולאב → `sponsors/<slug>/`) ושורת תאריך/צ'יפ/כותרת מותאמות. הרנדרר קורא **רק מהמירור**. שימוש חי: `popup-*`, `window-takeover-ma-ren`, `podcast-station`. פירוט: `docs/routes/events.md` → המירור.
- `widths[]` — רוחבי srcset לכרטיס ב-`/events/` כשתמונת ה-876w חוצה את כלל-זהב 12 (≥80KB וגם ≥800px): הרנדרר בונה `srcset` מ-`<name>-<w>w.webp` (הרוחב ששווה ל-`w` = הקובץ הראשי) + `sizes="(max-width:768px) 171px, 292px"`; בלי השדה = src יחיד. נקרא **רק מהמירור**. ⚠️ ב-`events.json` השדה ב-yom-kippur-wish-tree ו-sumii-melani-hosting (`[480,768,876]`); ל-nir-giorgio-levin-medina **רק במירור** — כשנוגעים ברשומה, לרשום גם ב-`events.json`.
- `event_photos[]` — `[{src, alt}]` + provenance **אופציונלי** `figma_node` / `figma_image_ref` לכל צילום (חסר ברשומות ישנות — לא למלא null). צילומים **מהאירוע עצמו** אחרי שהתרחש — נפרד מ-`gallery_images[]` (היצירות המוצגות). מרונדר ב-`.event-moments` + לייטבוקס: רצועת `.tri` לכמה צילומים, `figure` בודד לאחד (risa-and-noemi). **מירור סטטי ב-HTML בעשרת הדפים ב-§1.4 — לסנכרן.** + `figma_node_photos_desktop` / `figma_node_photos_mobile`.
- `photo_credit_stills` / `photo_credit_video` — קרדיטי הצילום: מעל הגלריה ב-natasha-zeriker, מתחתיה ב-hadas-tuval (שם רק `photo_credit_stills`, בעברית) + `figma_node_credits_desktop` / `figma_node_credits_mobile`.
- `performers_he[]` — שמות הפרפורמרים (אורחים, לא אומני האתר ⇒ בלי קישור) כפי שמוצגים בשורת הקרדיט, מערך מחרוזות. רק hadas-tuval ("פרפורמנס: …" מעל שורת קרדיט הצילום). מירור סטטי ב-HTML.

### 6.3 כללי רשימות
- `/events/` מציג אירוע כשהיום האחרון שלו (`date_end`, ואם אין — `date`) הוא היום או אחריו **לפי תאריך ישראל** (`todayIL()`, `Asia/Jerusalem` — מבקר בחו"ל רואה אותה רשימה), או כשהוא TBD, או `pinned`. מיון: אירועים עם תאריך עולה לפי `date` (באותו יום התחלה — מי שמסתיים קודם, ואז סדר המירור), TBD בסוף. `/press/` מסיר בזמן ריצה (אותו `todayIL()`) כל כרטיס אירוע שהיום האחרון שלו (`data-date-end`, ואם אין — `data-date`) הוא היום או אחריו, כל כרטיס אירוע בלי `data-date` תקין (TBD — שייך ל-`/events/`) וכל `data-pinned` ⇒ **המשלים המדויק**: אירוע עובר מ-`/events/` ל-`/press/` לבד למחרת היום האחרון. כרטיסי עיתונות (בלי `data-kind`) לא מסוננים.
- 🔴 **כשלים שקטים:** `date` חסר/לא-ISO ברשומת המירור ⇒ האירוע נחשב TBD ונשאר ב-`/events/` לתמיד עם "פרטים ותאריך בהמשך"; `data-date` לא תקין בכרטיס `/press/` ⇒ הכרטיס נמחק שם; `date_end`/`data-date-end` לא תקין או לא אחרי ההתחלה ⇒ אירוע של יום אחד.
- אירוע חדש = `events.json` + `#events-list-data` + (כשיש כרטיס ארכיון) רשומת `press.json` + כרטיס `.pcard` ב-`press/index.html` + sitemap. `docs/routes/events.md`, `docs/routes/press.md`.

## 7. `press.json`
`{ items: [...] }` — כתבות עיתונות + כרטיסי אירועים (לכרטיסי `#press` בהומפייג' ו-`/press/`).
- `id` — יציב (`homepage.json` מפנה אליו). דוגמאות: `timeout-manicure-against-darkness`, `13tv-peeling-a-layer`, `portfolio-the-shared-list`; אירועים `event-<slug>` / `event-<slug>-talk` (לשיחות האמנים החדשות).
- `type`: `press` | `event`.
- `tag_he` / `tag_en`, `source_he` / `source_en`, `title_he` / `title_en`, `subtitle_he` (+`subtitle_en`), `author_he`, `date`, `cover_image`, `exhibition_id`, `gallery_id`, `event_id`.
- `date_end` (אופציונלי) — אירוע רב-יומי: מראה של `events.json::date_end`, והכרטיס ב-`/press/` נושא אותו כ-`data-date-end`; `date` = יום ההתחלה. אין כאן `date_label` (§6.2). שימוש חי: `event-yom-kippur-wish-tree`, `event-sumii-melani-hosting`, `event-sumii-live-studio`.
- `route` (nullable) — דף פנימי. כרטיס **אירוע** עם `route:null` = `--soon` + טוסט "בקרוב" (רק `event-tal-nehoray-talk`). חריג: `portfolio-loneliness` (בלי `route`, `url:null`, `_alias:"press-1"`) = רשומת alias ישנה של הכתבה `press-1` (`press/press-1/`) — לא כרטיס soon ולא כתבה נפרדת; לא לבנות לה כרטיס. `url` — קישור חיצוני לכתבה המקורית.
- `homepage_visible` — **דקלרטיבי**: כרטיסי `#press` בהומפייג' ביד ולא נמשכים מכאן. חייב להתאים ל-`homepage.json::press_section.item_ids` ולכרטיסים ב-`index.html` (13).
- `figma_article_desktop` / `figma_article_mobile`, `figma_home_card` / `figma_home_card_desktop` / `figma_home_card_mobile` (+`_legacy_figma_*`, `_alias`).
- **כתבות long-form: הגוף ב-HTML, רק meta ב-JSON.**
- אירועים עתידיים **נשארים** ב-`press.json` וב-markup של `/press/` (מוסתרים בזמן ריצה עד שיעבור התאריך) — לא למחוק.

## 8. `opencalls.json`
`{ opencalls: [...] }` — **המערך חדש→ישן** (רשומה חדשה → לראש המערך). 3:
  - `obsession` — `status:"open"`, דדליין 2026-10-22, `gallery_id:"medina"`, דף `opencalls/obsession/` (`theme:"light"`). הסטטוס ידני — אחרי הדדליין לשאול את המשתמש (`docs/todo.md`).
  - `the-peeler`, `how-many` — שתיהן `archived`.
- `id`, `slug`, `title_en`, `title_he`, `title_html`, `status` (`open` | `archived`), `submission_status_he`, `gallery_id`, `gallery_label_he`, `deadline` + `deadline_he`, `city`, `hero_image`, `card_image`, `description_he`, `submission_instructions_he`, `contact{label_he, email, deadline_label_he, note_he}`, `figma_node_desktop` / `figma_node_mobile`.
- אופציונליים לוריאנט light (רק obsession; חסר = התבנית הרגילה): `theme` (`"light"`), `hero_mobile_ratio` (`"390/520"` — יחס באנר המובייל), `submission_instructions_he.lead_he` (מערך פסקאות כמו `description_he`, בלוק לפני הרשימה), `.items_html[]` (HTML גולמי, גובר על `items[]`), `.bullet` (`"disc"` ⇒ •), `contact.intro_he[]` (פסקאות לפני הדדליין/אימייל), `contact.deadline_first` (bool), `contact.label_html` (HTML גולמי, גובר על `label_he` — קישור לאוצרת). `title_html`/`intro_html`/`items_html`/`label_html` מוזרקים בלי escape — HTML תקין בלבד. `deadline_he` של obsession = `22.10.2026`.
- `card_image` = תמונת כרטיס הקול הקורא בהומפייג' — **גם ב-`#opencall` (דסקטופ) וגם ב-`#mobile-cta` (מובייל)**; כולן 4:5 (`images/opencalls/<slug>-card.webp` + וריאנטים). דפי `opencalls/*` לא קוראים אותו.
- אופציונליים: `emotional_triggers` (`{title_he, items[], lines[]?}` — `lines[]` לשבירת שורות כמו ב-Figma; כשקיים ולא ריק, הרנדרר משתמש בו במקום `items[]` (שמחוברים ב-` | `); null ב-how-many וב-obsession), `gallery_images[]`.
- `submission_instructions_he` = `{intro_html, items[], outro_he?}` — `intro_html` HTML מוכן (כולל `<span class="lat">`); `outro_he` רק ב-how-many; obsession משתמשת ב-`lead_he` + `items_html` + `bullet` (ובלי `intro_html`). `gallery_images[]` = `[{image, video, poster}]` (the-peeler: וידאו + poster; how-many ו-obsession: `null`).
- `contact.email` של קורין — גם ה-`mailto` hard-coded ב-renderer של 150 עמודי היצירה (`docs/routes/works.md`).
- **צרכנים:** `opencalls/*` (fetch-first + `#fallback-opencalls`; הרשומה נבחרת לפי `data-slug`, ולכן רשומה בלי דף לא מפריעה), `inject.py`; **ידני:** כרטיסי הקול הקורא בהומפייג' (§1.4).

## 9. `works.json`
`{ works: [...], art_works: [...], exhibition_statements: [...], _note }`

### 9.1 `works[]` — 3 אריחי התמונה של שחמט ההומפייג'
- `{id: "aw-1..3", image, figma_image_ref, artist_id}`. אריחי הטקסט (the / art works / more) = HTML סטטי. `components/artwork-lightbox.js` מחפש `data-artwork-id` ב-`works[]` (fetch, HTTP בלבד).

### 9.2 `art_works[]` — כל היצירות
- **סדר המערך = סדר התצוגה ב-`/works/`** (1:1 מול Figma `542:500`; `542:499` = legacy). הכרעות מיקום (רזידנסי באמצע, יצירות שאינן בגריד הפיגמה בסוף) — `docs/routes/works.md`.
- `id` (= `works/<id>/`), `artist_slug` (→ קישור לדף האומן).
- `artist_he` / `artist_en` — אם `artist_he` = null → השם הלטיני מוצג (la-raz-porta). קרדיט מעורב אפשרי (`"שירה טורבוביץ | sumii"` — Latin עטוף `.lat`).
- `title_he` / `title_en` — אופציונלי, דו-לשוני.
- `gallery_slug` + `gallery_en` (→ `/#galleries`) — ערכים קנוניים, verbatim: `medina` ⇒ `"Hamedina Square Gallery"`, `dizengoff` ⇒ `"Dizengoff Square Gallery"` (**לא** `galleries.json::name_en` — "Kikar … Gallery"). `gallery_slug` קובע גם באיזה דף גלריה היצירה מופיעה (`#g-artworks-data`, §1.2).
- `sold` (bool → תג "נמכר").
- `details_he` — טקסט אפור אופציונלי; `\n` נשמר (`white-space:pre-line`); גרשיים מנורמלים ל-`ס"מ`.
- `img` (שם בסיס תחת `images/works/v2/`), `w` / `h`, `widths[]` — לבניית srcset; **האחרון = רוחב הקובץ הראשי `<img>.webp`**, השאר `<img>-<w>w.webp` + אח avif לכל אחד.
- `artist_page_pos` (int / null) — סדר בדף האומן (לפי frames `artist-pages-*`). הרנדרר ממיין `(pos || 1e9)` ⇒ null = לסוף לפי סדר המערך. 🔴 **`pos:0` אסור** (`0||1e9` מפיל אותו לסוף). `/works/` מתעלם ממנו. קונבנציית קריאה LTR-פיגמה/RTL-אתר — `docs/lessons.md` 2026-07-15.
- `page` (bool; `true` בכל 150) — ב-`/works/` כרטיס עם `page:true` = `<a href="<id>/">`. דפי האומן מתעלמים (הכרטיס שם = לייטבוקס).
- `exhibition_title_he`, `exhibition_slug`, `exhibition_route` — שיוך קבוצה/תערוכה (9.3). 🔴 **`exhibition_route` של כל יצירות הקולפן = `exhibitions/the-peeler`** (לא `opencalls/…`; עמודי היצירה בונים את הקישור מהשדה). אחרות: `exhibitions/how-many`, `exhibitions/loneliness`, `sponsors/sumii`.
- `statement_he[]` — **טקסט על יצירה בודדת (per-work)**, לא טקסט-תערוכה (9.4).
- `kind` — `"residency"` = מידע בלבד (יצירות בלי תערוכה; shira-turbowicz, melani-hekimoglu); `"collab"` = מידע בלבד (קולאב בלי תערוכה, adam-leisner → `sponsors/ma-ren`).
- `hidden` (אופציונלי, לא בשימוש) — `/works/` מסנן (`!w.hidden`) ו-`sync_data.py` מוציא מ-`#g-artworks-data`; **לא מסתיר את עמוד היצירה ולא את דף האומן** (להסתרה אמיתית: `_staging/`, `docs/routes/works.md`; ואחרי החזרה משם — `sync_data.py` + `--check`, §1.2).
- collab — 9.5.
- **צרכנים:** `/works/` (`#works-data`), `works/<id>/` (`#artwork-data`), דפי אומן (`art-works.js`), דפי גלריה (`#g-artworks-data`) — כולם generated; `inject.py`; **ועותק ידני:** כרטיסי FIGURES/PRODUCTS ב-`sponsors/sumii/` (8 רשומות, §1.4).

### 9.3 קיבוץ בדפי האומן + `exhibition_statements[]`
- **קבוצה = `exhibition_title_he` (מחרוזת מדויקת)**, לא slug. לכן שתי קבוצות באותה תערוכה אפשריות (`הקולפן` + `הקולפן | interdependence`), וכל הבדל כתיב יוצר קבוצה נפרדת (`'מרחק שקט'` עם גרשיים אצל נעמי מול `מרחק שקט` אצל ליוואי — verbatim, מכוון). `\n` בתוך הכותרת קיים (yarden-amir-1/2: `הקולפן | רגש נבחר – נשארתי\nלמרות שידעתי`) והוא **חלק ממפתח ה-join** — זהה בדיוק ב-`art_works` וב-`exhibition_statements`. ⚠️ הוא **לא** מרונדר כשבירת שורה: ל-`.ex-heading` (דף האומן) ול-`.aw-ex-title` (עמוד היצירה) אין `white-space:pre-line`, ו-`mixedHtml`/`latHtml` לא ממירים `\n` ⇒ מוצג כרווח. שבירה אמיתית = שינוי renderer.
- **דירוג הקבוצות:** `exRank(exhibition_slug)` = האינדקס ב-`__EX_ORDER_INLINE__`, ממוין יורד (החדשה למעלה). slug לא מוכר / `null` ⇒ `-1` ⇒ תמיד מתחת לתערוכות אמיתיות. שוויון (אותה תערוכה) ⇒ **הקבוצה שה-`artist_page_pos` הנמוך ביותר שלה קטן יותר עולה ראשונה**; הפיגמה קובעת בתוך תערוכה דרך ה-pos.
- **`exhibition_statements[]`** (top-level) — טקסט-האומן-על-התערוכה, רשומה לכל `(artist, group)`:
  - `{artist_slug, exhibition_title_he, exhibition_slug, exhibition_route, statement_he[]}` — כל 5 המפתחות (רשומה חדשה = להעתיק רשומה אחות); 3 מהם חובה ל-`sync_data.py` (למטה). `exhibition_slug`/`exhibition_route` כאן לא נקראים ע"י קוד — הכותרת והקישור מגיעים מהיצירות.
  - 🔴 `statement_he` = **מערך פסקאות** (`["¶1","¶2"]`), לעולם לא מחרוזת — וכך גם `art_works[].statement_he` (9.4). על מחרוזת `statementHtml()` בדף האומן ו-`(w.statement_he||[]).map` בעמוד היצירה זורקים (`.map is not a function`) והרינדור נופל; `--check` לא תופס.
  - **מפתח לוגי = `(artist_slug, exhibition_title_he)`**; ה-lookup בדף האומן (`exStatement`) הוא `===` על שניהם; מרונדר בראש הקבוצה (`.ex-group-head`: `h3.ex-heading` מקושר ל-`exhibition_route` + `.ex-statement`).
  - קבוצה בלי רשומה = בלי סטייטמנט (לגיטימי: zohar-ron, raz-ronen ו-racheli-reuven בקבוצת `How Many Partners Have You Had?`). ⚠️ ל-hadas-tuval **יש** רשומה לקבוצת `הקולפן | מעורר רגש: החזקה והרפיה` — לא דוגמה לקבוצה בלי סטייטמנט.
  - שני אומנים באותה קבוצה משותפת = **שתי רשומות**, וכל אחת בנוסח אחר בלי שינוי קוד (חי: `הקולפן | interdependence`). ⚠️ עמוד היצירה הקנוני (`works/<id>/`) מקבל את ה-fallback לפי `artist_slug` בלבד ⇒ ב-`works/livay-levi-3/` מוצג הנוסח של ליוואי. לנוסח אחר שם — `statement_he` per-work ברשומה.
- **קבוצה בלי תערוכה — שני וריאנטים:**
  - **עם כותרת** (shira-turbowicz): `exhibition_title_he:"POP UP ART RESIDENCY"`, `exhibition_slug:null`, `exhibition_route:"sponsors/sumii"`, `kind:"residency"` ⇒ קבוצה רגילה, תמיד מתחת לתערוכות.
  - **בלי כותרת** (melani-hekimoglu): שלושת `exhibition_*` = **`null`**, `kind:"residency"`, ורשומת `exhibition_statements` עם `exhibition_title_he:null`. 🔴 **`null` מפורש בשני הצדדים** — ה-lookup ב-JS הוא `===`, ומפתח **חסר** (`undefined`) לא מתאים ל-`null` (ב-`sync_data.py` ה-`.get()` של Python מתייחס לחסר כ-`None`, כך שעמוד היצירה היה מוצא את הטקסט בעוד דף האומן לא). דורש renderer page-local בדף האומן ובעמודי היצירה — `docs/routes/artists.md`, `docs/routes/works.md`.
- 🔴 **בכל רשומת `exhibition_statements` שלושת המפתחות `artist_slug`, `exhibition_title_he`, `statement_he` חובה** (ערך `null` מותר, השמטה לא): `sync_data.py` ניגש אליהם ב-`r["…"]`, ורשומה בלי אחד מהם מפילה את הריצה ב-`KeyError` **באמצע** — `data/generated/*.js` ו-`works/index.html` כבר נכתבו, אבל עמודי `works/<id>/`, `#g-artworks-data`, `#fallback-galleries` ובדיקת דפי האומן לא רצים ⇒ עץ חצי-מסונכרן (ב-`--check` — traceback במקום דוח). לתקן, להריץ שוב, ו-`--check` לפני קומיט.
- **legacy:** `alon`, `dan-ben-ary`, `zohar-ron-dan-ben-ari` על renderer ישן בלי קיבוץ/סטייטמנטים/באנר — לא לגעת. `alon-1/2` עם `statement_he` per-work ובלי מפתחות `exhibition_*` בכלל.

### 9.4 `statement_he` per-work (הבאנר)
- `art_works[].statement_he` = טקסט על **יצירה אחת**. בדף האומן (renderer עם קיבוץ) מרונדר כבאנר רוחב-מלא **מעל** הכרטיס: `.work-statement` (`grid-column:1/-1`) = `.ws-rule` (קו 72px) + `.ws-head` (`title_he || title_en`, mixedHtml) + `.ws-body`. **הכרטיס נשאר אייטם-גריד רגיל (חצי רוחב)** גם כשהוא יחיד — באנר וכרטיס הם ילדי-גריד נפרדים (ה-wrapper הישן `.work-featured` — לא להחזיר); `margin-bottom:-40px` על הבאנר. (Figma `863:228`.) רק כש-`statement_he` לא ריק; קבוצות עם `exhibition_statements` לא מושפעות. דף שבו שורת הטקסט הראשונה כבר נושאת את השם מסתיר את `.ws-head` page-local (livay-levi).
- בשימוש: `zohar-ron-dan-ben-ari-1` (sex?) ו-`zohar-ron-9` (הקוסם) — How Many; **אין לזוהר `exhibition_statements` בקבוצה הזו**, וכותרת הקבוצה של שתיהן = "How Many Partners Have You Had?" הנקייה (לא "…| sex?"); `livay-levi-4`; `alon-1/2` (**רק בעמודי היצירה** — דף alon legacy ומתעלם מ-`statement_he`). הבאנר של `zohar-ron-dan-ben-ari-1` מופיע בדף zohar-ron (דרך `artist_pages`), לא בדף ה-legacy.
- בעמוד היצירה הבודד: `#artwork-data.statement_he` = per-work אם יש, אחרת ה-fallback מ-`exhibition_statements` (§1.2). ה-divider + סקשן התערוכה רק אם יש `exhibition_title_he` או `statement_he`.

### 9.5 יצירה משותפת (collab)
- **המתכון המאושר** (חי: `livay-levi-3` "interdependence", ליוואי לוי × הדס טובל, הכרעת Figma `668:13584`):
  - **רשומה אחת** ב-`art_works[]` (`artist_slug` = אומן ראשי).
  - `artist_pages[]` — slugs נוספים שבדפיהם היצירה תוצג (הפילטר: `artist_slug===slug || artist_pages.includes(slug)`). אפשר גם **בלי** `collab` — `zohar-ron-dan-ben-ari-1` (`artist_pages:["zohar-ron"]`) מוצגת גם בדף זוהר רון עם קרדיט רגיל. (דפי ה-legacy מתעלמים מהשדה.)
  - `collab[]` — `[{slug, name_he, name_en}]` ⇒ קרדיט שבו **כל שם מקושר בנפרד** (כלל-זהב 10).
  - `collab_connector_he` — ברירת מחדל ברנדרר "בשיתוף". 🔴 **להשתמש ב-`"×"` (U+00D7), לא "x"** — ל-FbEzmel אין גליף `x` לטיני.
  - `exhibition_title_he` ייעודי לקבוצה המשותפת (לא מתמזג לקבוצות הקיימות של השניים) + **רשומת `exhibition_statements` לכל אומן**.
  - ⇒ בגריד `/works/` פעם אחת; בדפי האומנים פעמיים; עמוד יצירה קנוני אחד. `artist_page_pos` שדה יחיד — חל על שני הדפים.
- **היכן הקרדיט המשותף מרונדר:** `artistCreditHtml` ב-41 דפי האומן (לא ב-3 ה-legacy, שגם מתעלמים מ-`artist_pages`), `artistHtml` ב-`works/index.html`, ו-`artistHtml` בעמוד היצירה — **רק ב-34 מתוך 150 עמודי היצירה** (אלה עם `w.collab`). עמוד ליצירה משותפת חדשה — להעתיק מאחד מהם (§1.5).
- **`title_he_by_artist{slug:"…"}` / `details_he_by_artist{slug:"…"}`** — כותרת/פרטים שונים לכל אומן ביצירה משותפת (`buildRichCard`: `title_he_by_artist[a.slug] || title_he`, `details_he_by_artist[a.slug] || details_he`). **ממומשים רק ב-10 דפי אומן** (וריאנט aharon-bas: aharon-bas, alice-debellis, amnon-lipkin, bar-cohen, hadas-tuval, maria-artamonova, michael-konovalenko + tali-zelnik, shira-turbowicz, melani-hekimoglu). שאר הדפים מתעלמים; `/works/` ו-`/works/<id>/` תמיד קנוניים. **אין רשומה שמשתמשת בהם.** לפני שמוסיפים אותם לרשומת `livay-levi-3` — להעתיק את הלוגיקה ל-`artists/livay-levi/` (חסרה שם; ב-`artists/hadas-tuval/` קיימת). 🔴 כלל כללי: יצירה משותפת עם השדות האלה דורשת את הלוגיקה ב-`buildRichCard` **בכל דף אומן שבו היא מוצגת** (`artist_slug` + כל `artist_pages`); דף בלי הלוגיקה מציג בשקט את הערך הקנוני. להעתיק מאחד מ-10 הדפים ולהפיץ בזהירות (harness, §1.7).
- כל שדות ה-collab additive / backward-compatible.

## 10. `homepage.json`
- **composition layer** — מפתחות `*_id` / `*_ids` לפריטים מ-JSONs אחרים + בלוקים דקלרטיביים. **`index.html` לא קורא את הקובץ** (HTML ביד — §1.4); הקובץ מתעד את ההרכב ויש לעדכן אותו יחד עם הדף.
- בלוקים: `hero`, `mobile_cta` (`label_he`; `card_ids` — סדר ה-DOM של שקופיות ה-`.tri` ב-`#mobile-cta`, `[0]` במרכז בטעינה — `["obsession","the-peeler","how-many"]`; `info[]` = תוויות status / date / location של הכרטיס שבמרכז בטעינה), `open_call_section` (`card_ids` — אותם 3, בסדר הכרטיסים ב-`#opencall`), `exhibitions_now` (`exhibition_ids` — `["the-peeler","how-many"]`, `artist_ids`, **`groups[]`** — קיבוץ לפי עיר: `{city_en, cards[]}`, כרטיס = `{kind: "residency"|"exhibition", gallery_id, route, exhibition_id?, title_en?, image?, logos[]?, gallery_name_en?}`; how-many תחת `berlin` בעוד ב-`exhibitions.json` היא `gallery_id:dizengoff` — פתוח, `docs/routes/homepage.md`), `exhibitions_archive` (`items[]` — `{exhibition_id, gallery_id, image}`, שני כרטיסים; `thumbs_ref`/`active_gallery_id` הוסרו), `art_works_words` / `art_works_words_mobile`, `big_news` (`heading_en`, `title_he`, `subtitle_he`, `address_he`, `gallery_id`, figma), `perfume_promo.perfumes[]` (`name_he`, `exhibition_bar_en[]`, `exclusive_he`, `cta_he`/`cta_url` — nullable), `social_section` (`feed_ref: "instagram.posts"`), `galleries_section` (`gallery_ids`), `galleries_berlin_section`, `x_our_artists` (`items[]` — סדר Figma "mobile order" `1873:1146` (קנוני 2026-09-27, מחליף את `1124:1181`; גם ב-`figma_node_order`), תמונה `work-N.webp` 1:1 למיקום — חוץ מ-work-10/23/31 שמצביעים ל-`work-N-v2.webp` (הקבצים הישנים נשארו, כלל-זהב 8); 39 פריטים), `sumii_sponsor`, `soos_sponsor`, `tribe_teaser`, `press_section` (`item_ids`, `view_all_route`).
- `tribe_teaser` — כותרת/קרדיטים/גלריה מעל `#press`; `gallery_images[]`; `figma_gallery_strip_desktop` `361:420` / `figma_gallery_strip_mobile` `363:649`; thumbs = לייטבוקס **בלי CTA** (`docs/components.md` §1.4.1).
- `press_section.item_ids` ⇔ `press.json::homepage_visible` ⇔ כרטיסי `#press` — שלושתם תמיד תואמים. חריגות מכלל "רק כתבות + שני אירועי פתיחה" ב-`_note` שלו (gala-night, hadas-tuval, livay-levi — הכרעות משתמש).
- פרטי כל סקשן: `docs/routes/homepage.md`.

## 11. `curators.json`
`{ curators: [...] }` — `korin-avraham` בלבד. schema: `data/_schema/curators.schema.json`.
- `id`, `slug`, `name_en_first` / `name_en_last`, `instagram_handle`, `contact_email`, `badge_en`, `section_heading_en`, `credit_he`, `bio_he`, `portrait` (`src`, `width`, `height`, `alt_he`), `figma_desktop` / `figma_mobile` (עם prefix fileKey).
- `exhibition_slugs[]` — התערוכות בעמוד האוצרת; **סדר = דסקטופ שמאל→ימין**; מובייל — CSS `order` אם נדרש. תערוכה חדשה של קורין → להוסיף כאן.
- מופנה ע"י `curator_slug` ב-`exhibitions.json`, `artists.json`, `sponsors.json`.
- **צרכנים:** עמוד האוצרת (`#fallback-curators`), `exhibitions/how-many|loneliness/` (`#fallback-curators`), `inject.py`.
- ⚠️ כפילויות ידניות: ה-handle `yasalamfashionblog` גם ב-`about/index.html`, ב-`press/walla/index.html` (בגוף הכתבה) וב-JSON-LD של עמוד האוצרת (head, §1.2); ה-`contact_email` גם ב-`opencalls.json::contact.email` (ובמירורי `#fallback-opencalls`) וב-`mailto` ה-hard-coded של כל 150 עמודי היצירה.

## 12. `sponsors.json`
`{ sponsors: [...], _note }` — עמודי `sponsors/<slug>/`. **meta בלבד — גוף העמוד ב-HTML.** אין `$schema`.
- `id`, `slug`, `name`, `founder_he`, `title_lockup`
- `exhibition_slug` / `exhibition_route` (nullable — רזידנסי בלי תערוכה), `gallery_id`
- `curator_slug` (nullable → `curators.json`, רצועת `the curator`), `date_start` / `date_end` (nullable — טווח רזידנסי/שיתוף)
- `website`, `model_credit` (nullable), `route`, `cover_image`, `logo`
- `case_exception[]` — מחרוזות מותג שנשארות **lowercase** (Figma `textCase:LOWER`), גוברות על כלל ה-UPPERCASE הגלובלי דרך מחלקה ממוקדת `.brand` (`text-transform:none`) — הכרעת משתמש 2026-08-04. soos: `soos.sound`, `www.soos.audio`, `Bella`; sumii ו-melani: `[]` (הכלל הגלובלי חל).
- `founder_artist_slug` (nullable) — slug של דף האומן כשהמייסד/ת אומן/ית באתר (sumii → `shira-turbowicz`, melani → `melani-hekimoglu`, soos → null).
- `figma_file`, `figma_node_desktop`, `figma_node_mobile`, `figma_logo_node`.
- **כמה רשומות יכולות לחלוק `route`:** `melani-hekimoglu` חולקת `route:"sponsors/sumii/"` (אין לה עמוד משלה). ב-`inject.py` **הרשומה הראשונה על ה-route קובעת את ה-OG** (`cover_image` → og:image, og:type `article`) וכל הרשומות על ה-route הופכות ל-`about` Brand ב-JSON-LD ⇒ **סדר המערך משנה** (sumii לפני melani).
- ⚠️ פריימי soos בפיגמה (`1318:3287`/`1318:3480`) שוכתבו in-place לעיצוב sumii — ה-node ids ברשומת soos כבר לא מצביעים על עיצוב soos.

## 13. `instagram.json`
- `{handle, posts[{id, image, url}], _note}` — snapshot סטטי מ-Figma (מימוש עתידי דרך Instagram Graph API). מופנה דקלרטיבית מ-`homepage.json::social_section.feed_ref`; אין צרכן בזמן ריצה.

## 14. הכרעות קנוניות שנוגעות לדאטה (Audit 2026-07-09 ואילך)
- איות אנגלי קנוני: **"adi duek"**, **"zohar shitrit"** (הכרעת משתמש); ה-slugs נשארים `adi-duak`, `zohar-shtrit` (כלל-זהב 6).
- כתיב עברי של אומנים = `artists.json` (למשל "טלי זלניק", "ארס ברוש") — גם כשב-Figma כתוב אחרת. **"טורבוביץ" — בלי גרש** (הכרעה 2026-09-27: `artists.json`, `works.json::artist_he` = `"שירה טורבוביץ | sumii"`, `sponsors.json::founder_he`); לא להחזיר "טורבוביץ׳" (עם גרש) ולא "טורוביץ׳".
- **ערכים ב-JSON שסוטים מהפיגמה בכוונה — לא "לסנכרן" חזרה:**
  - `works.json::shira-turbowicz-2.title_en` = "Sonia Delaunay" (בפיגמה "Sonia Delaun" — קיטוע).
  - `events.json::the-space-between.list_title_he` + `press.json` = "מור צופיה געש" (בפיגמה "צופייה").
  - `events.json::maria-artamonova.description_he` = "האמנית תחשוף" (הכרעת משתמש 2026-08-18; בפיגמה "אמנית").
  - `nir-giorgio-levin-medina` — `date` = 2026-09-30 ב-`events.json`, במירור, ב-`press.json` ובכרטיס `/press/` (הכרעת משתמש 2026-09-27; פריימי הדף `1498:882`/`1498:769` מציגים 30.9, וכרטיס הארכיון בפיגמה `1864:3054` עם 17.9 מיושן — **לא לסנכרן ממנו**).
  - `artists.json::amnon-lipkin.bio_he` = "בדייקנות" (בפיגמה "בדיקנות").
  - `exhibition_statements` של `הקולפן | interdependence` = "גוף", "ותלויה" (בפיגמה "גןף", "ותלוייה").
- **ולהפך — verbatim מכוון שלא "מתקנים":** `details_he` של `melani-hekimoglu-3` (bloom planter) = הטקסט של flow vases (copy-paste של המעצבת, פתוח ב-`docs/todo.md`); `'מרחק שקט'` אצל נעמי (§9.3); `volume_en` VOLUME 2 (§5); `time_label` (§6.1); `hours[].time` (§3).

## 15. הוסר / לא להחזיר / לא להשתמש
- 🔴 **עותקי דאטה inline בדפי אומן** (`#artists-inline`, `#art-works-inline`, `#ex-statements-inline`, `#ex-order-inline`) — הוחלפו ב-`data/generated/*.js`; לא להחזיר (§1.3). הוראות ישנות ("regen `__ARTISTS_INLINE__` בכל הדפים", "הרץ `sync_works_mirrors.py`", "סנכרן `#g-artworks-data`/`fallback-galleries`/4 מקומות") = **`python3 tools/sync_data.py`**. `tools/migrate_exhibition_statements.py` — פרוש (§1.2).
- `statement_he_by_artist{slug:[…]}` — שדה של המנגנון שלפני 2026-06-23 (קיים רק בסקריפט הפרוש); אין צרכן. במקומו — `exhibition_statements` לכל אומן.
- גזירת סטייטמנט-קבוצה מ-"`statement_he` של היצירה הראשונה" — בוטלה (2026-06-23); `statement_he` = per-work בלבד.
- יצירת הקולאב המאוחדת הישנה `aharon-bas-1` (title/details per-artist) — פוצלה ל-`aharon-bas-1` + `bar-cohen-1` עצמאיות; לא למזג ולא להחזיר שדות collab אליהן.
- `homepage.json::tribe_teaser.figma_gallery_strip` (`250:98`) — הוחלף ב-`_desktop`/`_mobile`.
- `homepage.json::big_news` — `ring_text_en`, `badge_en`, `image` הוסרו (2026-08-04, סקשן טקסט בלבד).
- הקרוסלה של `#events-upcoming` ומירור `#events-upcoming-data` בהומפייג' — הוסרו 2026-08-04 (ראה `card_title_en`, §6.1); הסקשן עצמו סטטי (שני פוסטרים).
- אירוע `amnon-lipkin` — נמחק 2026-08-28 מ-`events.json`, מהמירור ומה-sitemap. הפריימים עדיין בפיגמה — **לא לשחזר**; `nir-giorgio-levin-medina` הוא אירוע אחר (נפל במקור על אותה משבצת 8.9 במדינה; 30.9 — §14).
- `pinned` של michael-konovalenko ו-livay-levi (2026-09-01, §6.2); רזידנסי SUMII ב-`exhibitions.json` (§1.4); Firebase לניוזלטר (§2) — לא להחזיר.
