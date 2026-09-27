# Data contracts — `data/*.json` + עותקי הדאטה

> **לקרוא לפני:** שינוי של כל קובץ ב-`data/` (כולל `data/generated/`), הוספה/שינוי של שדה, ונגיעה בכל עותק דאטה שיושב בתוך דף (`<script type="application/json" id="…">` או `<script src="…/data/generated/…">`).
> המסמך מתאר מצב נוכחי (2026-09-27) + כללים פעילים. כללים ספציפיים לדף → ה-route doc שלו (`docs/routes/<family>.md`). היסטוריה: `docs/history/CLAUDE-2026-09-27.md` §6 (החוזים) ו-§4.
> כל טענה על "מי צורך" שדה נבדקה מול הקוד ב-2026-09-27. `⚠️` = לא הוכרע/לא אומת. רשימות "היום" (ערכים, ספירות) הן תמונת מצב — לבדוק מול הקוד לפני שמסתמכים עליהן.

## 0. עקרונות

- **`data/*.json` = מקור-האמת** (הסכמה מחקה CMS עתידי). דף קורא JSON ולא מטמיע תוכן inline (כלל-זהב 1).
- 🔴 **Re-Read לפני עריכה של כל `data/*.json`** (כלל-זהב 9) — סשנים מקבילים עורכים את `events.json`/`press.json`/`homepage.json` כמעט בכל בניית אירוע; עריכה על עותק ישן דורסת את השינוי שלהם, ו-`sync_data.py --check` לא יתפוס את זה.
- **שדה חסר → מוסיפים ל-JSON לפני השימוש.** **שדה חדש → לכל הרשומות בקובץ** (`null` אם לא ידוע) ומתעדים אותו כאן באותו קומיט.
  - **חריג — דגלים ושדות אופציונליים** (ב-`events.json`: `soon`, `pinned`, `date_tbd`, `date_end`/`date_label`, `widths`, `list_*`, `event_photos`…; ב-`press.json`: `date_end`) קיימים **רק ברשומות שמשתמשות בהם**, והיעדר = ברירת המחדל (כרטיס רגיל, אירוע של יום אחד). לא להוסיף להם `null` לכל הרשומות; את `soon` **מוחקים** (לא `null`) כשנבנה דף (§6.2).
- **אחרי כל שינוי ב-JSON:** `python3 tools/sync_data.py`. **לפני קומיט:** `python3 tools/sync_data.py --check` ⇒ exit 0. אם ל-JSON ששינית יש עותק ידני (§1.4) או טקסט שמופיע ב-`<head>` של דף (§1.2) — לעדכן גם אותו, באותו קומיט.
  - 🔴 **הקבצים ש-`sync_data.py` כתב הם קבצי פרודקשן — לקמט אותם באותו קומיט עם ה-JSON:** `data/generated/*.js` וכל דף שהסקריפט כתב אליו (`works/index.html`, `works/<id>/`, `galleries/<slug>/`, `curators/korin-avraham/`). הסקריפט מדפיס רק את 8 הראשונים (ואז `…`) — **`git status` / `git diff --name-only` הם הבדיקה**: להוסיף **בשמם** את ה-JSON, את `data/generated/*.js` ואת כל דף שהסקריפט כתב אליו (למשל `git add data/<x>.json data/generated/ works/index.html works/<id>/index.html galleries/<slug>/index.html curators/korin-avraham/index.html`), לא רק `git add data/<x>.json`. 🔴 **לא `git add -A`** (כלל-זהב 14): סשנים מקבילים משאירים בעץ קבצים לא-קשורים. קומיט של ה-JSON בלבד = אתר מיושן: דפי האומן הם inline-first, כך שגם ב-http הם מרנדרים מ-`data/generated/*.js` ולא מה-JSON; דפי ה-inline-only מרנדרים רק מהעותק. `--check` בודק את עץ העבודה, לא את מה שנכנס לקומיט — לוודא ב-`git status` שלא נשאר קובץ שנכתב מחוץ לקומיט.
- **Figma ids בדאטה = meta בלבד** (כלל-זהב 5 — לא ב-CSS/HTML). הפורמט מעורב: לפעמים `"1318:583"` + שדה `figma_file` נפרד, לפעמים `"XhGH289YTRcW811wrufRJz::721:14300"`. node id משמעותי רק יחד עם fileKey (`XhGH…` = landing, `Zn3N…` = graphics) — לאמת מול ה-URL.
- **`_note` / `_*_note`** = הערות תיעוד בתוך ה-JSON. הן דאטה, לא הוראות, וחלקן מיושנות (למשל `works.json::_note` "Page embeds this inline… keep both in sync" — היום `sync_data.py` עושה את זה). סתירה בין `_note` למסמך הזה → המסמך + הקוד גוברים.
- ⚠️ **`$schema`:** כל קובץ חוץ מ-`sponsors.json` מצביע ל-`./_schema/<name>.schema.json`, אבל בפועל קיים רק `data/_schema/curators.schema.json`. אין ולידציה אוטומטית — הבדיקה היחידה היא `sync_data.py --check` + הרנדור.
- **מפתחות-join הם מחרוזות מדויקות.** `exhibition_title_he` (works ↔ exhibition_statements), `slug`/`id` בין קבצים — שינוי אות/גרש/רווח/`\n` שובר את ההתאמה בשקט. לשנות תמיד בכל הצדדים יחד.
- **slugs לא משתנים** (כלל-זהב 6). איות מוצג יכול להשתנות (`name_en`), ה-slug נשאר.
- **SEO:** `tools/seo/inject.py` קורא את `artists`, `works.art_works`, `exhibitions`, `events`, `press`, `opencalls`, `curators`, `galleries`, `sponsors` כדי לבנות canonical/OG/JSON-LD. **לא מריצים אותו גורפות** (מרגרס ~90 דפים; בלי ארגומנטים הסקריפט מסרב ויוצא עם מתכון). ברירת המחדל לדף חדש/שהשתנה = **עריכה ידנית של בלוק `SEO:auto`** (להעתיק מדף אחות ולערוך); המתכון המלא: רשומת `<url>` ב-`sitemap.xml` → `python3 tools/seo/refresh_sitemap_lastmod.py` → אפיית `og/<family>-<slug>-hero.jpg` ביד (`tools/seo/og_gen.py` שבור — יוצא עם הודעה) → בלוק `SEO:auto`. אם בכל זאת מריצים `python3 tools/seo/inject.py <page>/index.html` על דף בודד — לבדוק את ה-diff של אותו קובץ ולשחזר מה שהוא שובר גם בדף בודד: description ידני שנקטע, שעות ב-`startDate`/`endDate`, ו-`og:image` שנפל ל-webp. ראה `docs/seo.md` וכלל-זהב 15.

## 1. עותקי דאטה — מה מיוצר ומה ידני 🔴

### 1.1 למה יש עותקים, ושלושה דפוסי טעינה
דף שנפתח ב-file:// לא יכול `fetch`. לכן כל דף שמרנדר מדאטה גם מקומית נושא (או טוען) עותק:
- **inline-only** — הרנדרר קורא רק את העותק: `works/index.html #works-data`, `works/<id>/ #artwork-data`, `galleries/<slug>/ #g-artworks-data` + `#g-exhibitions-data`, `events/index.html #events-list-data`, `artists/index.html #artists-grid-data`, `events/ktuba/ #fallback-ktuba-artists`. **עותק מיושן = באג גלוי גם בפרודקשן.**
- **inline-first → fetch** — דפי האומן: `window.__ARTISTS_INLINE__` (מ-`data/generated/artists.js`); אם חסר → `fetch("../../data/artists.json")`.
- **fetch-first → fallback** (`loadJson(path, embeddedId)`) — `curators/korin-avraham/`, `exhibitions/how-many|loneliness/`, `opencalls/how-many|the-peeler/`, `galleries/<slug>/` (לגבי `#fallback-galleries`). ב-HTTP נקרא ה-JSON; העותק משמש רק ב-file:// ⇒ **עותק מיושן לא נראה בפרודקשן, רק מקומית** — קל לפספס. `#fallback-galleries` (בדפי הגלריה ובעמוד האוצרת) = **generated** — רק `python3 tools/sync_data.py`, לא לערוך ביד. שאר העותקים ברשימה הזו ידניים — לעדכן ביד לפי §1.4.
- 🔴 **בדיקה ויזואלית/טיפוגרפית רק דרך http** (`python3 -m http.server`, מוגדר ב-`.claude/launch.json`): ב-file:// כרום חוסם `@font-face` (CORS, origin null) והדף נראה בפונטי fallback.

### 1.2 מיוצר אוטומטית — `python3 tools/sync_data.py`
- **פקודה אחת** מייצרת מחדש כל עותק שהוא פונקציה מדויקת של ה-JSON. להריץ אחרי **כל** שינוי ב-`artists.json` / `works.json` / `exhibitions.json` / `galleries.json`. אידמפוטנטי (ריצה שנייה לא משנה כלום). `--check` = לא כותב, exit 1 + רשימת יעדים מיושנים ובעיות בדפי אומן.
- **בבעלותו (לעולם לא לערוך ביד):**
  - `data/generated/artists.js` ← `artists.json` **כולו** → `window.__ARTISTS_INLINE__`. זה **אובייקט** (`{"$schema",…,"artists":[…]}`), לא מערך; הרנדרר מפרק `.artists` (בדיקת `.length` על האובייקט הייתה הבאג של 2026-07-15 — "ARTIST NOT FOUND" ב-file://).
  - `data/generated/art-works.js` ← `works.json::art_works` → `window.__ART_WORKS_INLINE__`.
  - `data/generated/ex-statements.js` ← `works.json::exhibition_statements` → `window.__EX_STATEMENTS_INLINE__`.
  - `data/generated/ex-order.js` ← סדר ה-`slug` ב-`exhibitions.json` → `window.__EX_ORDER_INLINE__` (היום `["loneliness","how-many","the-peeler"]`).
  - `works/index.html #works-data` ← `art_works` (JSON מעוצב).
  - `works/<id>/index.html #artwork-data` ← הרשומה מ-`art_works` לפי ה-`id` שכבר כתוב בעותק (compact) + **fallback סטייטמנט**: `statement_he` של היצירה עצמה → אחרת טקסט `exhibition_statements[(artist_slug, exhibition_title_he)]` → אחרת בלי השדה.
  - `galleries/<slug>/index.html #g-artworks-data` ← `art_works` עם `gallery_slug == <slug>`, בסדר המערך, **בלי `hidden:true`**. סט השדות = מפתחות הרשומה הראשונה שכבר בעמוד (היום `id, artist_slug, artist_en, artist_he, title_he, title_en, img, w, h, widths`). **החריג היחיד לכלל "לא לערוך ביד": להוספת שדה להטלה — להוסיף את המפתח (בכל ערך) לרשומה הראשונה בעמוד, פעם אחת, ואז להריץ; הסקריפט דורס את כל הערכים מ-`works.json`.**
  - `#fallback-galleries` ב-`galleries/medina/`, `galleries/dizengoff/`, `curators/korin-avraham/` ← `galleries.json` verbatim.
- 🔴 **לא בבעלותו — ה-`<head>` של אף דף.** `<title>` ו-meta description (בראש הדף), וה-canonical/`og:*`/`twitter:*`/JSON-LD (בלוק `SEO:auto`) הם עותקים ידניים של ערכי JSON. כשמשנים ב-JSON טקסט שמופיע ב-head — לעדכן ידנית את הדף הנוגע, באותו קומיט: כותרת/אומן של יצירה → `works/<id>/`; שם/ביו/סטייטמנט של אומן → `artists/<slug>/`; כותרת/תאריך/שעה של אירוע → `events/<slug>/` (כולל `startDate`/`endDate`). עריכה ידנית של הבלוק, **לא** `inject.py` גורף (§0). `--check` לא יתפוס head מיושן. (תקדים: jessica-tabarovsky 2026-07-06 — meta/OG/twitter/JSON-LD עודכנו ביד אחרי שינוי ביו.)
- **`search-index.js`** (שורש הריפו; לא של `sync_data.py`) — נבנה אוטומטית בכל קומיט ע"י `.githooks/pre-commit` → `python3 tools/search/build_index.py -q` ואז `git add search-index.js`, מכל `index.html` שבמעקב/staged: `<title>`, meta description, שמות JSON-LD (`name`/`alternateName`/`creator.name`) — לכן דף חדש צריך `<title>`/description טובים; דפי `noindex` ו-`_staging/` מוחרגים. פעיל כש-`core.hooksPath=.githooks` (הגדרה per-clone: `git config core.hooksPath .githooks`). לא לערוך ביד; כשל בבנייה חוסם את הקומיט. לכן תיקון ידני של ה-`<head>` (למעלה) נכנס לאינדקס החיפוש בהדר **באותו קומיט** שבו הוא מקומט (ה-hook בונה מחדש מתוכן עץ העבודה ומוסיף את `search-index.js` לפני יצירת הקומיט).
- **לא סורק את `_staging/`** — רק `artists/*/`, `works/*/`, `galleries/*/` ו-`curators/korin-avraham/`. עמוד שהועבר ל-`_staging/` (הסתרה) נשאר עם `#artwork-data` קפוא, וגם בדיקת דפי האומן של `--check` לא רצה עליו. **אחרי החזרת דף מ-`_staging/` לעץ המוגש — `python3 tools/sync_data.py` ואז `--check` מיד** (בנוסף ל-sitemap ול-canonical, כלל-זהב 15).
- כל קובץ ב-`data/generated/` מתחיל ב-header "GENERATED by tools/sync_data.py … do not edit by hand".
- ⚠️ **הערות ישנות בתוך דפים** שאומרות לסנכרן/להעתיק ביד יעדים שבבעלות `sync_data.py` — מיושנות, לא לפעול לפיהן: ב-`galleries/medina/` וב-`galleries/dizengoff/` מעל `#fallback-galleries` ("כל שינוי ב-data/galleries.json חייב סנכרון לכאן…"), ב-`works/index.html` ("…art_works[]; keep in sync"), ובכל 150 עמודי `works/<id>/` מעל `#artwork-data` ("copy this file, change <html data-artwork-id>, and swap #artwork-data"). עמוד יצירה חדש = לזרוע רק `{"id":"<id>"}` בשורה אחת (§1.5) — **לא** להדביק רשומה מלאה ביד (רשומה מעוצבת עם רווח/שורה חדשה ⇒ הדף מדולג בשקט ו-`--check` ירוק). לעומת זאת ההערות "Keep in sync" / "MUST mirror" מעל ה-`#fallback-*` ב-`exhibitions/how-many|loneliness/`, `opencalls/*` ו-`events/ktuba/`, והערות ה-"MIRROR SLICE" מעל `#g-exhibitions-data` בדפי הגלריה — **נכונות** (עותקים ידניים, §1.4).
- **שמות ישנים:** `tools/sync_works_mirrors.py` = wrapper דק שמריץ `sync_data.py` (מעביר ארגומנטים, כולל `--check`) — לשימוש `sync_data.py` ישירות. `tools/migrate_exhibition_statements.py` = **פרוש** (יוצא עם הודעה; **לא להשתמש בדגל העקיפה `--i-know-this-is-retired`**): הרצה חוזרת הייתה מחלצת סטייטמנטים per-work כטקסט-תערוכה (שגוי) ומטפלת בעותקי inline שכבר לא קיימים.

### 1.3 דפי האומן וה-generated scripts
- כל `artists/<slug>/index.html` טוען `<script src="../../data/generated/<name>.js"></script>` (במקום שבו פעם ישבו העותקים). **41 דפים טוענים 4** (`artists`, `art-works`, `ex-statements`, `ex-order`); **3 דפי legacy** (`alon`, `dan-ben-ary`, `zohar-ron-dan-ben-ari` — renderer ישן בלי קיבוץ תערוכות/סטייטמנטים) טוענים 2 (`artists`, `art-works`). שמות ה-globals וקוד הרנדרר לא השתנו. עובד ב-file:// וב-http.
- 🔴 **אסור להדביק דאטה לתוך דף אומן** (`<script id="artists-inline|art-works-inline|ex-statements-inline|ex-order-inline">window.__…__=…</script>`) ואסור לערוך את `data/generated/*`. `sync_data.py` (גם ב-`--check`) נכשל על עותק inline שחזר (**רק בצורת התג הישנה המדויקת** `<script id="artists-inline">` וכו' — השמה של `window.__…__=` בתג אחר לא נתפסת, ואם היא רצה אחרי ה-`<script src>` היא דורסת בשקט את `data/generated`) ועל `<script src>` חסר (`ex-statements`/`ex-order` נדרשים רק בדף שמכיל `function buildExGroups(list){`).
- 🔴 **צורת התגים ומיקומם קבועים.** תגי `<script src="../../data/generated/<name>.js"></script>` (4, או 2 ב-legacy) יושבים **מיד לפני** ה-`<script>` של הרנדרר (למשל `artists/aharon-bas/`, שורות 305–308), והם **סינכרוניים**.
  - **לא להזיז אותם אחרי הרנדרר ולא להוסיף `defer`/`async`.** הרנדרר (IIFE רגיל) קורא את ה-globals בזמן ה-parse: רק ל-`__ARTISTS_INLINE__` יש fallback ל-`fetch`, ושלושת האחרים נקראים כ-`window.__…__||[]` ⇒ היצירות, הסטייטמנטים וסדר הקבוצות נעלמים בשקט — ב-file:// מופיע "artist not found", וב-http התוצאה תלויה בתזמון מול ה-fetch (במקרה הגרוע נופלת ל-`artists.json works[]` השטוח). `--check` בודק רק שהתגים **קיימים**, לא איפה ⇒ הזזה **לא נתפסת**.
  - **התג byte-exact: בלי `defer`/`async`/`?v=N`** (שונה מהקונבנציה של `components/*.js?v=6`). `--check` מזהה את התג לפי המחרוזת המילולית (`SRC_RE`), ותג שהשתנה מדווח כ-"missing <script src>" — הודעה מטעה: התג קיים, רק שונה.
- **אומן/יצירה/סטייטמנט חדש = לערוך JSON → `sync_data.py`.** אין יותר "regen `__ARTISTS_INLINE__` בכל 42 הדפים" ואין "`__ART_WORKS_INLINE__` זהה בכל הקבצים — ערוך את התבנית והפץ".
- `sync_data.py` **לא מנתח קוד renderer.** האילוץ הישן לשמור את בלוקי `NEW_JS`/`NEW_GROUP_JS` byte-identical (העוגנים של `sync_works_mirrors.py` הישן) — **בוטל**; תיקון page-local יכול להיות ב-JS או ב-CSS (כלל ההפצה הזהירה עדיין חל). **היוצא-מן-הכלל:** המחרוזת המילולית `function buildExGroups(list){` משמשת את `--check` כדי לדרוש `ex-statements.js`+`ex-order.js` — לא לשנות את הניסוח שלה (רווחים, שם פרמטר), אחרת `--check` יפסיק לדרוש את שני הסקריפטים בשקט.
- **renderer/CSS** של דפי האומן עדיין per-file: 44 עותקים של התבנית, כמה וריאנטים (standard / aharon-bas-variant / legacy / page-local). הקבצים זהים פרט ל-`data-slug` ולתוספות page-local מתועדות — ערוך אחד והפץ בזהירות. פירוט: `docs/routes/artists.md`.

### 1.4 Mirror registry — עותקים ידניים (לא בבעלות `sync_data.py`)
לכל שינוי במקור — לעדכן את העותק ביד באותו קומיט.

- **`events/index.html` · `#events-list-data`** (inline-only) ← `data/events.json`. מכיל את **כל** האירועים, כולל עבר — הרנדרר מסנן. הטלה לכל רשומה:
  - `slug`, `date`, `gallery_id`; `alt` — **נכתב ביד כאן** (אין שדה מקביל ב-`events.json`)
  - `title_en` ← `list_title_en` אם קיים, אחרת `title_en` (לאירועים חדשים). ⚠️ בכמה רשומות הכותרת במירור שונה מ-`title_en` — ניסוח אחר (close-look, gala-night) או אותיות קטנות בלבד (loneliness, how-many, niki-de-saint-phalle-day, sumii-live-studio; מוצג UPPERCASE ממילא) — לא "לתקן" אותן לפי הכלל.
  - `title_he` ← `list_title_he` (רק כשקיים; נוכחותו מחליפה את הכותרת לעברית `.ttl--he`)
  - `img`/`w`/`h` ← `list_image` וממדיו; בלי `list_image` → קרופ/וריאנט של ה-hero (the-space-between: `hero-480w.webp` 480×726)
  - אופציונליים: `soon`, `pinned`, `date_tbd`, `widths`, `date_end` (§6.2 — הרנדרר קורא `date_end`: טווח תאריכים + פילטר לפי היום האחרון). `date_label` **לא** נכנס למירור — `/events/` מחשב את התווית בעצמו.
  - **אירוע חדש = להוסיף ל-`events.json` וגם כאן** (+`list_image`).
  - ⚠️ הרנדרר ב-`events/index.html`: תווית הגלריה מגיעה מטבלת `GALLERY` הקשיחה (`medina`/`dizengoff`/`flea-market` — **אין `berlin`** ⇒ אירוע בברלין דורש הוספה לטבלה, אחרת התווית ריקה), והקישור נבנה מ-`slug` (`<slug>/`), לא מ-`route` ⇒ תיקייה ששמה שונה מה-slug = 404. פירוט: `docs/routes/events.md`.
- **`artists/index.html` · `#artists-grid-data`** (inline-only) — `[{slug, name:"first\nlast", link?}]`: סדר תצוגה + שמות דו-שורתיים; `link` (אופציונלי) = slug של דף אחר שהכרטיס מקשר אליו (היום `dan-ben-ary` → `zohar-ron-dan-ben-ari`). **לא נגזר מ-`artists.json`** (הסדר = Figma `523:145` + הכרעות מאוחרות — `docs/routes/artists.md`). אומן בגריד = לערוך כאן + תמונות גריד **810×810** `images/artists/grid/<slug>.{webp,avif}` **וגם** `<slug>-480w.{webp,avif}` — ה-srcset (480w + 810w) וה-`width`/`height` קבועים ברנדרר.
- **`galleries/<slug>/index.html` · `#g-exhibitions-data`** (inline-only) — slice של `exhibitions.json` לפי `gallery_id` עם שדות כרטיס (`slug, gallery_id, status, title_en, title_he?, volume_en?, start_date, end_date, img, w, h, srcset?, alt` — `img`/`srcset`/`alt` נכתבים כאן ביד, אין להם מקור ב-JSON). תמונת כרטיס: במדינה קרופ ייעודי `images/galleries/medina/ex-card-<slug>.webp`; בדיזינגוף ממוחזרת תמונה קיימת (`images/exhibitions/how-many/hero.webp`, `images/sponsors/sumii/hero-768w.webp`). **תערוכה חדשה = להוסיף ל-`exhibitions.json` וגם לסלייס של דף הגלריה** (+תמונת כרטיס).
  - דיזינגוף בלבד: רשומת **רזידנסי SUMII** (`slug:"sumii"`, `kind:"residency"`, `route:"sponsors/sumii/"`, `dates_text`, …) **קיימת רק כאן**. 🔴 לא להוסיף אותה ל-`exhibitions.json` — היא אינה תערוכה והייתה מזהמת את דירוג `__EX_ORDER_INLINE__`.
- **`curators/korin-avraham/index.html` · `#fallback-curators`** ← subset של `curators.json` (היום בלי `contact_email`, `credit_he`); **`#fallback-exhibitions-min`** ← subset של `exhibitions.json`. fetch-first. שדה חדש שהדף קורא — להוסיף גם לעותק. (ה-`#fallback-galleries` באותו דף — generated.)
- **`exhibitions/how-many/`, `exhibitions/loneliness/` · `#fallback-site`** (subset מיושן: `brand` = רק `name_en`; `footer` בלי `social` ובלי קישור "מדיניות פרטיות"), **`#fallback-curators`** (subset — בלי `bio_he`/`contact_email`, ו-`exhibition_slugs` מיושן; הדפים קוראים ממנו את `credit_he`, שקיים), **`#fallback-exhibitions`** (subset; drift ידוע — בדף loneliness לרשומת how-many יש `start_date`/`end_date` = `null`, `docs/routes/exhibitions.md`). fetch-first.
- **`exhibitions/the-peeler/`** = סטטי קפוא, לא קורא דאטה — שינוי תוכן = עריכת HTML **וגם** עדכון הרשומה `the-peeler` ב-`exhibitions.json`, שעדיין נקראת ע"י עמוד האוצרת (כותרות, `label_en`/`volume_en`, `hero_overlay_hide_en`, `curator_card_image`, `gallery_id` — ובעותק `#fallback-exhibitions-min` שלו), `ex-order.js`, `inject.py` (כותרת/תאריכים/hero), והסלייס הידני `#g-exhibitions-data` במדינה (כותרת/תאריכים/סטטוס; תקדים: `end_date` → 2026-10-05, 2026-09-27). אומן חדש ב-strip ⇒ גם `artists[]` ברשומה. ⚠️ `gallery_images` ברשומה = ה-hero בלבד; הדף (7 שקופיות) הוא מקור האמת. פירוט: `docs/routes/exhibitions.md`.
- **`opencalls/how-many/`, `opencalls/the-peeler/` · `#fallback-site`** (עותק מלא של 5 המפתחות העליונים של `site.json` — היום זהה למקור, בלי `$schema`), **`#fallback-opencalls`** (subset). fetch-first.
  - ⚠️ בארבעת הדפים (exhibitions how-many/loneliness + opencalls) **אף ערך מ-`site.json` לא מרונדר בפועל** — ה-footer מגיע מ-`site-chrome.js`; ב-`exhibitions/*` למפתחות ה-`footer_*` שב-ctx אין `data-bind` תואם, וב-`opencalls/*` `rowHtml()` מוגדר ולא נקרא. 🔴 **לא למחוק את `#fallback-site` וגם לא לקצץ את המפתחות שלו:** `loadJson` זורק כשה-fetch נכשל ואין עותק, ו-`Promise.all` מחליף אז את כל הדף ב-"failed to load" (file://); ובנוסף `exhibitions/*` ניגשים מחוץ ל-try ל-`site.footer.newsletter.{title,placeholder,cta}`, `site.footer.copyright` ו-`site.footer.links_he`, ו-`opencalls/*` ל-`site.footer.links_he` — עותק מקוצץ (למשל `{}`) זורק TypeError ב-file:// והדף נתקע במצב טעינה.
- **`events/ktuba/index.html` · `#fallback-ktuba-artists`** ← `events.json::ktuba.artists` (אותם `name_en`/`slug`, ל-`image` מתווסף `../../`). inline-only — ההערה בדף אומרת "rendered from events.json" אבל הקוד קורא רק את התג.
- **דפי אירוע עם רצועת צילומים מהאירוע (`event_photos[]`)** (close-look, natasha-zeriker, risa-and-noemi, noemi-safir, livay-levi, maria-artamonova, jessica-tabarovsky, sumii-opening — היום בכל השמונה ה-HTML וה-JSON תואמים בסדר וב-alt) — שקופיות סטטיות ב-HTML ← `events.json::<slug>.event_photos[]` (+`figma_node_photos_*`, `photo_credit_*`). "מירור סטטי ב-HTML — לסנכרן את שניהם": הוספה/הסרה/שינוי סדר או alt של צילום = בשני המקומות.
  - ⚠️ גם ב-`events/gala-night/` וב-`events/how-many/` (`section.event-moments`) וב-`events/loneliness/` (`section.moments`) יש גריד "moments from the opening" — תמונות אפויות בלי מקור ב-JSON; **אינן** מירור של `event_photos[]` — לא להוסיף להן `event_photos`.
- **`index.html` (עמוד הבית) — כל הסקשנים HTML כתוב ביד.** `homepage.json` ורשומות שהוא מפנה אליהן **דקלרטיביים** (העמוד לא קורא אותם). בפרט:
  - `#press` ← `press.json::homepage_visible` + `homepage.json::press_section.item_ids` (שני אלה חייבים להתאים זה לזה ולכרטיסים; היום 13 ⇔ 13 ⇔ 13 כרטיסים).
  - `#galleries` (שמות/כתובות/שעות) ← `galleries.json` — שינוי שעות = `galleries.json` **וגם** `.gallery-card .hours` ב-`index.html`.
  - שאר הבלוקים (`x_our_artists`, `big_news`, `perfume_promo`, `sumii_sponsor`, `soos_sponsor`, `tribe_teaser`, `galleries_berlin_section`…) ← `homepage.json`.
- **`press/index.html` · כרטיסי `.pcard` סטטיים** ← `press.json` (+ לאירועים `data-kind="event" data-date="YYYY-MM-DD"`; לאירוע רב-יומי גם `data-date-end` ותווית `<bdi>` = `date_label`; `data-pinned` כשרלוונטי). כתובים ביד. כרטיס `.pcard--soon` (`href="#"` + טוסט "בקרוב") — היום רק tal-nehoray. פרטים: `docs/routes/press.md`.
- 🔴 **`sponsors/sumii/index.html` · כרטיסי FIGURES + PRODUCTS (HTML סטטי)** ← `works.json::art_works` — `shira-turbowicz-1..3` (FIGURES) ו-`melani-hekimoglu-1..5` (PRODUCTS). כל כרטיס מעתיק ביד: נתיב `img` (`images/works/v2/<img>.webp`), `width`/`height`, רוחבי ה-srcset (`widths`), הכותרת (FIGURES: `title_he | <span class="lat">title_en</span>`, כשהשנים שבתוך `title_he` עטופות `<bdi dir="ltr">…</bdi>` — shira-turbowicz-2/3, לא להעתיק את `title_he` כמו-שהוא; PRODUCTS: `title_en` בלבד) והקישור `../../works/<id>/`. בעמוד אין script דאטה ⇒ **`sync_data.py` לא נוגע בו**. שינוי באחת מ-8 הרשומות (כותרת, תמונה/ממדים, id, מחיקה) = `python3 tools/sync_data.py` **וגם** עריכה ידנית של הכרטיס בעמוד, באותו קומיט. טקסטי התיאור בכרטיסים: FIGURES — קיימים רק בעמוד (לא נגזרים מ-`details_he`); PRODUCTS — זהים ל-`details_he` חוץ מ-melani-hekimoglu-5 (בעמוד נקודה אחרי "Flow") — שינוי `details_he` = לעדכן גם את הכרטיס. פרטים: `docs/routes/sponsors.md`.
- **טבלאות lookup ידניות בקוד** שמצלות על דאטה של אומנים: `FOCAL_POINTS` (object-position לפורטרט) בכל 44 דפי האומן; `_ARTIST_FOCAL` ב-`events/ktuba/` ובתבנית `exhibitions/how-many|loneliness/`; `_ARTIST_SLUGS` (שם→slug) באותה תבנית; `CURATORS` (slug→שם+thumb של האוצרת) ו-`NAME_LINKS` (שם→קישור בתוך הסטייטמנט) ב-`artists/shira-turbowicz/` וב-`artists/melani-hekimoglu/` (`NAME_LINKS` גם ב-`works/melani-hekimoglu-1..5/`). **הדרך המועדפת = שדות הדאטה** (`artists.json::portrait_focus`, `exhibitions.json::artists[].focus` / `.slug`) — לא להרחיב את הטבלאות. בנוסף: `HERO_DIMS` (slug → ממדי ה-hero הטבעיים) ב-`opencalls/how-many/` וב-`opencalls/the-peeler/` — החלפת `opencalls.json::hero_image` או קול קורא חדש = לעדכן את הטבלה **בשני הקבצים** (+ וריאנטים 480/768/1080 ואחי avif), `docs/routes/exhibitions.md`; וטבלת `GALLERY` ב-`events/index.html` (למעלה).
- **גופי כתבות/אירועים/ספונסרים** (long-form) חיים ב-HTML; ב-JSON רק meta/תקציר. אין סנכרון אוטומטי — אם משנים meta (תאריך, כותרת, route), לשנות גם בדף.

### 1.5 עמוד יצירה חדש (`works/<id>/`)
- להעתיק דף קיים **מוריאנט renderer שמכסה את הצרכים** (collab ⇒ דף שיש בו `w.collab`, למשל `works/livay-levi-3/`; פירוט הוריאנטים: `docs/routes/works.md`), להחליף `data-artwork-id` ב-`<html>`, meta ו-OG (`og/works-v2-<id>.jpg`), ולזרוע את `#artwork-data` **בשורה אחת בדיוק, בלי רווח/שורה חדשה בין התגים ל-JSON:** `<script type="application/json" id="artwork-data">{"id":"<id>"}</script>`. `sync_data.py` ממלא את הרשומה המלאה (לפי ה-`id` שבעותק).
- 🔴 **ה-id החדש חייב להיכנס גם ל-`#artwork-data` וגם ל-`data-artwork-id`.** אם בדף המועתק נשאר ה-id הישן ב-`#artwork-data`, `sync_data.py` ימלא אותו בשקט ברשומה של היצירה **הישנה**.
- 🔴 **כשלים שקטים:** רווח/שורה חדשה **לפני** ה-`{` ⇒ הדף **מדולג בלי אזהרה**; רווח/שורה חדשה **אחרי** ה-`}` ⇒ מדולג, או — אם בהמשך הקובץ יש `}</script>` — הסקריפט קורס ב-`json.loads`; id שלא קיים ב-`works.json` ⇒ רק אזהרה ל-stderr והדף מדולג. **בשני סוגי הדילוג `--check` נשאר ירוק (exit 0)** — אחרי יצירת עמוד לוודא שה-`#artwork-data` שלו התמלא ברשומה המלאה.
- הגנרטור הישן `/tmp/gen_artwork_pages.py` **לא בריפו** — לא להסתמך עליו.
- **דף גלריה חדש (עתידי):** לזרוע `<script type="application/json" id="g-artworks-data">[]</script>` — רשימה ריקה ⇒ ההטלה נופלת לסט ברירת המחדל (`G_ARTWORK_FIELDS` בסקריפט). גם `#fallback-galleries` מתמלא **רק אם התג כבר קיים בדף** — לזרוע `<script type="application/json" id="fallback-galleries">{}</script>` וכו'. דף בלי התגים פשוט לא מסונכרן (בלי שגיאה).

### 1.6 כתיבת סקריפט הזרקה משלך
- אם אי-פעם כותבים סקריפט שמזריק JSON ל-HTML (לעותק ידני): `json.dumps` + slicing או replacement **function** — **לא** מחרוזת החלפה ל-`re.sub`. אחרת `\n` שבתוך ה-JSON הופך לתו-שורה אמיתי ושובר את ה-JS (קרה: ביו עם שורות שבר את `__ARTISTS_INLINE__` ב-file://).

### 1.7 שינוי שנוגע בהרבה דפים
- הפצת תבנית, CSS/JS משותף, או שינוי צנרת דאטה — חובה regression harness לפני קומיט: `node tools/regress/snapshot.mjs --label before` → שינוי → `node tools/regress/snapshot.mjs --label after` → `node tools/regress/diff.mjs before after`.
  - exit 0 = DOM/computed styles/boxes/scroll/errors/failed requests זהים לכל דף, http + file://. רוחבים כברירת מחדל 390,1440; לעבודת layout/טיפוגרפיה `--widths 390,1024,1366,1440`. `--only artists/,events/` לצמצום. 🔴 **אותם `--only`/`--widths` בשני הצילומים** — דף שקיים רק בצד אחד נספר כהבדל. `diff.mjs … --dom` מציג גם diff של ה-DOM.
  - exit 1 = הבדל. בשינוי שאמור לשנות פלט (למשל עדכון דאטה) זה הצפוי — לקרוא את ה-diff ולוודא שהשתנו **רק** הדפים/האלמנטים המיועדים.
  - רשימת הדפים = כל `*.html` שבמעקב git + קבצים חדשים שאינם ignored (בלי `trash/`, `_staging/`, `node_modules/`…) ⇒ דף חדש נצלם גם בלי `git add` (ב-`before` הוא לא קיים ⇒ יופיע ב-diff, צפוי).
  - הפלט נשמר **מחוץ לריפו**: `$REGRESS_OUT/<label>` (ברירת מחדל `<os tmpdir>/zrp-regress/<label>` — בכוונה, בגלל עותקי-קונפליקט של iCloud; ה-`.regress/NAME` בטקסט העזרה של הסקריפט מיושן).
- לפני הפצה גורפת — `git commit` (כלל-זהב 14). שחזור תבנית — מ-git HEAD, לא מדף אחר.

## 2. `site.json`
- מבנה בפועל: `brand` (`name_en`, `name_he`, `tagline_en`, `founder`, `logo`), `nav[]` (`key`, `label_en`, `href`), `footer` (`newsletter{title,placeholder,cta}`, `links_he[]{label,href}`, **`social[]{platform,url}`**, `copyright`), `announcement`, **`contact{instagram_handle}`**. (החוזה הישן מנה `social` כשדה עליון — בפועל הוא תחת `footer`.)
- "גלובלי בכל דף" = דקלרטיבי: ה-nav וה-footer בפועל מרונדרים ע"י `components/site-chrome.js` (ערכים hard-coded שם — לא נקרא מ-`site.json`). שינוי nav/footer = `site-chrome.js` **וגם** `site.json`.
- נטען (fetch-first + `#fallback-site`) ע"י `exhibitions/how-many|loneliness/` ו-`opencalls/*`, אבל **אף ערך ממנו לא מרונדר בפועל** (ה-footer מגיע מ-`site-chrome.js`). ⚠️ לא למחוק את `#fallback-site` וגם לא לקצץ אותו: `loadJson` זורק כשאין עותק, וב-file:// כל הדף נופל להודעת שגיאה; ועותק מקוצץ זורק TypeError על `site.footer.*` (§1.4).
- טופס הניוזלטר בפוטר = Wix Velo (`site-chrome.js` → `zrp.co.il/_functions/subscribe`), לא Firebase — לא קשור ל-JSON הזה.

## 3. `galleries.json`
`{ galleries: [...] }` — היום 4: `medina`, `dizengoff`, `flea-market`, `berlin`.
- `id`, `slug`
- `name_he`, `name_en`; `address_he`, `address_en`; `city` (`"tel aviv"` / `"berlin"`)
- `status`: `open` | `coming-soon` | `closed`
- `hours[]`: `{days_he, days_en, time}` — `time` nullable ("שבת סגור"). ⚠️ **`time` שמור בקונבנציית bidi `"18:00-11:00"`** — הכרעת משתמש: ספרות נשמרות/מוצגות LTR כמו בטקסט הגולמי של Figma, **לא "לתקן" את הסדר**. `[]` = אין בלוק שעות.
- `image_hero` — תמונת כרטיס ההומפייג' (null לפשפשים — כרטיס ירוק שטוח).
- `route` (nullable) — `galleries/<slug>/`; null = אין דף (פשפשים, ברלין).
- `image_page_hero` — hero של דף הגלריה, **נפרד** מ-`image_hero`.
- `address_street_en` / `address_area_en` — הכתובת כפי שמוצגת בדף הגלריה, verbatim מהפיגמה — **חוץ מ:** 🔴 דיזינגוף = `1 Reines st. tel aviv` (הכרעת משתמש 2026-08-13: הרחוב על שם הרב ריינס; "Raines" בפיגמה = typo). **לא להעתיק "Raines" בחזרה** — גם לא ל-`events.json::address_en` (5 אירועי how-many בדיזינגוף) ולא לשורות הכתובת בדפי `events/*`.
- `manager` (nullable) — `{name_en_first, name_en_last, email, portrait{src,width,height,alt_he,figma_image_ref}, note}`. `email` נשמר **lowercase** (ל-`mailto:`); התצוגה UPPERCASE דרך הכלל הגלובלי. נטלי זיגל = אותה מנהלת במדינה ובדיזינגוף (פורטרט משותף `images/galleries/managers/natalie-zigel.webp`). ⚠️ פער Zigel/siegel באימייל — פתוח (`docs/todo.md`). ⚠️ כפילות ידנית: פרטי נטלי כתובים גם ב-`about/index.html` (פורטרט נפרד `images/about/people/`, ו-`mailto` עם N גדולה) — `docs/routes/about.md`.
- `figma_node_desktop` / `figma_node_mobile` (כרטיס), `figma_page_desktop` / `figma_page_mobile` (דף הגלריה), `note`.
- אופציונליים (ברלין, 2026-09-27): `address_lines_en[]`, `address_lines_en_mobile[]`, `instagram_handle`, `instagram_url`.
- **צרכנים:** `galleries/<slug>/` (lookup לפי `slug`) ו-`curators/korin-avraham/` (lookup לפי `id`, רק `name_en` לכרטיסי התערוכות) — fetch-first; `#fallback-galleries` **generated** — `sync_data.py`; רשומה חדשה לא משפיעה על הדפים. דפי הגלריה קוראים בזמן ריצה רק: `name_he`, `address_street_en`/`address_area_en`, `hours[]`, `manager` (שם, `email`, `portrait.alt_he`). ⚠️ `image_page_hero` ו-`manager.portrait.src` **דקלרטיביים** — תמונת ה-hero ופורטרט המנהלת כתובים סטטית ב-HTML של הדף; החלפת תמונה = לערוך את ה-HTML (וגם את ה-JSON). + `inject.py`, ו**כרטיסי `#galleries`/`#galleries-berlin` בהומפייג' (HTML ידני — §1.4)**.
- 🔴 **שינוי שם/כתובת של גלריה — עותקים ידניים מחוץ ל-`sync_data.py`:**
  - `index.html`: כרטיסי `#galleries` (`.name`/`aria-label`/`.addr`/`.hours`), `.gname` בכרטיסי `#exhibitions-now`, ה-alt של פוסטרי `#events-upcoming`, `.nb-sub-addr` (+ `homepage.json::big_news.address_he`); ב-`homepage.json` גם `exhibitions_now.groups[].cards[].gallery_name_en` (ברלין).
  - בלוק ה-SEO של דף הגלריה (שם ב-title/og/twitter/JSON-LD; `streetAddress` ב-JSON-LD בשני הדפים; במדינה גם הכתובת העברית ב-description/og:description).
  - שורות הכתובת בדפי `events/*` + `events.json::address_en`; `contact/index.html`; חלק מכתבות `press/*` (⚠️ טקסט מצוטט מכתבה חיצונית, כמו כותרת וואלה, כנראה נשאר כפי שפורסם — לפי תקדים `press/the-shared-list/`; לא הוכרע).
  - (א) הפוטר ב-`components/site-chrome.js` — שמות הגלריות בעברית בשני בלוקים (`.footer-menu` דסקטופ, `.footer-mobile-mini` מובייל) — **וגם** `site.json::footer.links_he` (דקלרטיבי) ועותקי `#fallback-site` שלו (`exhibitions/how-many|loneliness/`, `opencalls/*`).
  - (ב) **`gallery_label_he`** — עותק של שם הגלריה ב-`events.json`, `exhibitions.json` ו-`opencalls.json`, מרונדר בזמן ריצה ב-`exhibitions/how-many|loneliness/` וב-`opencalls/*` ⇒ לעדכן גם את `#fallback-exhibitions`/`#fallback-opencalls`, ואת העמוד הקפוא `exhibitions/the-peeler/` (ה-badge + description/og/twitter).
  - (ג) `works.json::art_works[].gallery_en` בכל 150 הרשומות (נפרד מ-`name_en`) ⇒ אחריו `python3 tools/sync_data.py`.
  - (ד) טבלת `GALLERY` (תוויות באנגלית) ב-`events/index.html`.
  - (ה) ה-`<head>` (description/og/twitter/JSON-LD, §1.2) של דפים שמזכירים את הגלריה — אירועים, ספונסרים, חלק מדפי האומנים והיצירות — ו-`tools/seo/overrides.json` (תיאורים ש-`inject.py` מזריק מחדש); צ'יפ הגלריה בראש `sponsors/soos/` ו-`sponsors/sumii/`.
  - **לחפש** את הערך הישן בכל הצורות (אנגלית/עברית, `'` וגם `׳`): `grep -rliE "jabotinsk[iy]|ז('|׳)בוטינסקי" --include='*.html' --include='*.json' --include='*.js' --exclude-dir=node_modules . | grep -vE '^(\./)?(trash|docs/history|data/generated|search-index\.js)'` (שני האחרונים מיוצרים — `sync_data.py` וה-pre-commit hook; לא לערוך ביד) (דיזינגוף: `reines|ריינס`). ⚠️ חלופה `('|׳)` ולא סוגריים `['׳]` — ב-locale C (כמו ב-shell של סוכן) BSD grep לא מתאים תו רב-בייטי בתוך `[…]` ומפספס בשקט את הכתיב העברי. ⚠️ ב-natasha-zeriker (בדף וב-`events.json`) הכתיב הוא `jabotinski` — `docs/routes/events-talks.md`. לשם גלריה — לחפש את השם הישן בעברית ובאנגלית עם אותם `--include` (לדיזינגוף שני כתיבים עבריים: `דיזינגוף`/`דיזנגוף`).
  - מופעים בתוך `#fallback-galleries` — רק `sync_data.py`. תקדים: תיקון Reines. פירוט: `docs/routes/galleries.md`.
- ⚠️ פער פתוח: בכרטיס הפשפשים ב-`index.html` השם = "גלריית יפו, שוק הפשפשים" והכתובת = "שוק הפשפשים, יפו"; ב-JSON: `name_he` "גלריית שוק הפשפשים", `address_he` "שוק הפשפשים, תל אביב" (הכתובת — כך גם ב-Figma). בכרטיס מדינה בפיגמה אין כתובת רחוב (האתר מציג). לא הוכרע — `docs/todo.md`.

## 4. `artists.json`
`{ artists: [...] (44), _pending_artist_pages: [...], _note }`
- `id`, `slug` (= שם התיקייה `artists/<slug>/`)
- `name_he`, `name_en` — כתיב קנוני. כתיב עברי של אומן בכל מקום אחר באתר (כולל `works.json::artist_he`) = הכתיב של הקובץ הזה.
- `portrait` (נתיב); `portrait_focus` (אופציונלי, object-position לפורטרט; עדיפות ברנדרר: `portrait_focus` → טבלת `FOCAL_POINTS[slug]` שבכל עותק תבנית → `center 25%`. לאומן חדש — להעדיף את השדה, בלי הפצה).
- `work_image` — התמונה שמוצגת **רק בדף placeholder** (כש-`bio_he` ריק וגם `works[]` ריק): `work_image || portrait`. ה-hero הרגיל לא קורא אותו.
- `bio_he`, `bio_en` (nullable). פסקאות מופרדות ב**שורה ריקה** (`\n\n`); `\n` יחיד בתוך פסקה = `<br>`; שורה בלי עברית = `.en-line` (Copperplate). **הפסקה הראשונה = intro** (מוצגת בנפרד מהגוף, לפני ה-divider — כשיש יותר מפסקה אחת).
- `works[]` — אובייקטים **inline** `{id, title, image, year?, medium?}` (לא ref ל-`works.json`). משמשים רק כ-fallback: דף האומן מציג את `works.json::art_works` המסוננים (`artist_slug === slug || artist_pages.includes(slug)`); **רק אם אין אף רשומה** → `artists.json works[]` (שם+כותרת+medium).
- `instagram_handle` (nullable). כש-handle בפיגמה הוא leftover של אומן אחר → `null` (תקדים gal-rotem/raz-ronen).
- `hero_images[]` — דואו תמונות hero; `hero_image_focus[]` — object-position לכל תמונה בדואו (אינדקס מקביל).
- `hero_collab` — hero שיתופי: `{artists:[{name_en:[שורות], bio_he_short, instagram}]}` (≥2; `name_en` הוא **מערך שורות**, לא מחרוזת), Figma מובייל `119:3917` (⚠️ fileKey לא מתועד). היום רק `zohar-ron-dan-ben-ari`.
- `figma_artist_page_desktop` / `figma_artist_page_mobile`. ⚠️ `homepage_featured` (בכל 44) — אין צרכן בקוד; ההומפייג' כתוב ביד (`homepage.json` + HTML).
- **אופציונלי `studio_en`** — שם סטודיו. כשקיים, ה-hero מציג שם מלא בשורה אחת + הסטודיו בשורה/ות מתחת. נצרך **page-local** ב-`heroNameParts` של `tali-zelnik` ("piece of mine studio") ו-`shira-turbowicz` ("sumii") בלבד — אומן שלישי צריך את הלוגיקה בדף שלו.
- **אופציונלי `curator_slug`** (2026-08-20) — slug מ-`curators.json`; דף האומן מרנדר רצועת `the curator` אחרי היצירות (לאומן שמציג מחוץ לתערוכה רגילה, למשל רזידנסי). נצרך page-local ב-`shira-turbowicz` ו-`melani-hekimoglu` בלבד. 🔴 הרנדרר **לא קורא את `curators.json`**: שם/thumb מגיעים מטבלה hard-coded `var CURATORS={'korin-avraham':{…}}` בכל אחד משני הדפים — slug אחר (או שינוי שם/תמונה של האוצרת) דורש עריכת הטבלה בדף (§1.4).
- **אופציונלי `works_caption_each_image`** — `true` = כיתוב תמיד מתחת לכל תמונה (נדרש כשכותרות זהות אך ההקשר How Many ולא loneliness). היום רק ב-`zohar-ron-dan-ben-ari`. ⚠️ לא נמצא צרכן בקוד הנוכחי (grep 2026-09-27) — מתועד כחוזה.
- ⚠️ `works_grid_order` (12 רשומות) — אין צרכן בקוד.
- `hidden` (אופציונלי, לא בשימוש היום) — חלק ממנגנון ההסתרה (defense-in-depth). **דפי האומן מתעלמים ממנו**; הסתרה אמיתית = העברת התיקייה ל-`_staging/` (gitignored ⇒ 404). פרטים: `docs/routes/artists.md`.
- `_pending_artist_pages` (עליון) — אומנים שחסר להם תוכן (היום `dan-ben-ary`, `racheli-reuven`). ⚠️ זו רשימת מעקב, לא מתג: הרנדרר מציג placeholder רק כש-`bio_he` ריק **וגם** `works[]` ריק (לא סופר `art_works` — ראה route doc) — racheli-reuven (`bio_he` = "רחלי ראובן") מרונדרת כדף רגיל עם קבוצת How Many; רק dan-ben-ary (`bio_he` null) מרונדר כ-placeholder.
- **צרכנים:** כל `artists/<slug>/` (דרך `data/generated/artists.js`), `inject.py`. אחרי שינוי → `sync_data.py`.

## 5. `exhibitions.json`
`{ exhibitions: [...], archive_thumbnails, _note }`
- 🔴 **סדר המערך = כרונולוגי עולה (ישן→חדש)**, והוא מקור-האמת לדירוג "התערוכה החדשה למעלה" בדפי האומנים (`__EX_ORDER_INLINE__`; הכרעת משתמש 2026-08-12). **תערוכה חדשה נוספת בסוף המערך**, ואז `sync_data.py`. היום: `loneliness` → `how-many` → `the-peeler`.
- שדות: `id`, `slug`, `label_en`, `volume_en`, `title_he`, `title_en`, `subtitle_he` (nullable), `status` (`current` | `upcoming` | `archived`), `status_label_en`, `gallery_id`, `gallery_label_he`, `start_date` / `end_date` (`YYYY-MM-DD`), `hero_image`, `hero_letter_heading_en`, `thumbnails[]` (ריק היום; חסר ב-the-peeler), `gallery_images[]`, `figma_node_desktop` / `figma_node_mobile`.
- `volume_en`: ל-`how-many` ול-`the-peeler` **שניהם `"VOLUME 2"`** — verbatim מ-Figma, הכרעת משתמש 2026-06-25; **לא "לתקן" ל-VOLUME 3** (`docs/routes/exhibitions.md`).
- `description_he` — פסקאות `[{weight, lines:[...]}]` (`weight`: `regular`/`light`…). ⚠️ `description_en` ו-`artist_ids[]` שהופיעו בחוזה הישן **לא קיימים בדאטה**.
- `artists[]` — פריט: `name_en` (`\n` = שבירת שורה), `thumb`, `slug` (אופציונלי — בלעדיו התבנית מחפשת לפי `name_en` בטבלת `_ARTIST_SLUGS` שבדף; בלי התאמה הכרטיס לא קליקאבילי), `focus` (אופציונלי, object-position; אחרת טבלת `_ARTIST_FOCAL` → `center 25%`), `artist_page_slug` (אופציונלי = הכרטיס מקשר לדף אומן **אחר** — לשיתופי פעולה; היום zohar-ron ב-how-many → `zohar-ron-dan-ben-ari`).
- `curator_slug` (אופציונלי) — slug מ-`curators.json`; מציג סקשן אוצרת מתחת לאומנים בדפי התבנית (how-many/loneliness).
- `hero_overlay_en_only` (אופציונלי, `true`) — אוברליי תמונת הגיבור מציג רק `title_en`, בלי פס volume / כותרת עברית (how-many). נקרא ע"י דפי התבנית ועמוד האוצרת.
- `hero_overlay_hide_en` (אופציונלי, `true`) — האוברליי מציג title-bar + `title_he` בלי הכותרת האנגלית; `title_en` נשמר ל-`<title>`/OG/SEO (the-peeler). נקרא היום רק ע"י עמוד האוצרת — עמוד the-peeler קפוא ולא קורא JSON.
- `curator_card_image` (אופציונלי) — תמונת הכרטיס בעמוד האוצרת (אחרת `hero_image`); היום the-peeler. ⚠️ המידות קשיחות ב-`buildCard` (822×1243 + חובה אח `-480w`; hero: loneliness 690×1044, השאר 1068×1600) — תערוכה במידות אחרות = לעדכן את `buildCard` (CLS). ראה `docs/routes/exhibitions.md`.
- ⚠️ `archive_thumbnails` (עליון) — שריד ארכיון הטאבים הישן (הוחלף 2026-06-08); אין לו צרכן (מוזכר רק ב-`trash/` וב-`docs/todo.md`). רדום — לא להסתמך עליו. `homepage.json::exhibitions_archive` כבר לא מפנה אליו (היום `items[]`, §10).
- `the-peeler`: העמוד קפוא, אבל הרשומה עדיין נקראת במקומות אחרים — כל שינוי בדף = לעדכן גם אותה (§1.4). `end_date` = 2026-10-05 (עודכן 2026-09-27 גם ב-`#g-exhibitions-data` של מדינה).
- **כותרת loneliness הרשמית = "בדידות בתוך סביבה תוססת"** (Audit 2026-07-09; אם ב-Figma עדיין "בתוך בסביבה" — טעות מוכרעת, לא לשחזר). כותרות הקבוצה ב-`works.json` משתמשות היום ב-"בדידות בסביבה תוססת" — זה מפתח-join (§9.3); לא לשנות בלי כל הצדדים.
- **צרכנים:** `exhibitions/how-many|loneliness/` (fetch-first + `#fallback-exhibitions`), עמוד האוצרת (`#fallback-exhibitions-min`), `#g-exhibitions-data` בדפי הגלריות (ידני), `data/generated/ex-order.js`, `inject.py`.
- רזידנסי (SUMII) **אינו** תערוכה ולא נכנס לכאן (§1.4).

## 6. `events.json`
`{ events: [...] }` — אירוע = רשומה. רוב דפי האירוע **סטטיים**; ה-JSON הוא meta. הצרכן החי העיקרי = המירור `#events-list-data` (§1.4).

### 6.1 שדות בסיס
- `id`, `slug` (= `events/<slug>/`). 🔴 slug תפוס (אומן עם אירוע קודם) → slug לפי הגלריה: `zohar-ron-medina`, `nir-giorgio-levin-medina` (כלל-זהב 6).
- `title_he`, `title_en` (הכותרת הקנונית של הדף), `subtitle_he` (nullable).
- `date` (`YYYY-MM-DD`; באירוע רב-יומי = יום ההתחלה — `date_end`, §6.2), `date_he`, `time_start`, `time_end` (nullable) — הסדר המכונתי (התחלה/סוף); ה-`startDate`/`endDate` ב-JSON-LD של הדף (ידני, §1.2) תואמים להם. `time_label` (אופציונלי) — מחרוזת התצוגה **verbatim מהפיגמה**: ברוב שיחות האמנים סוף-התחלה בקונבנציית bidi (`"20:30-18:30"`), אבל התחלה-סוף ב-gala-night (`"19:30-21:30"`), yom-kippur-wish-tree ו-sumii-live-studio (`"10:00-14:00"`), ו-risa-and-noemi `"11:00"` — לא לנרמל. אף קוד לא קורא את שדות השעה — התצוגה בדף כתובה ביד.
- `gallery_id`, `gallery_label_he`, `address_en[]` (שורות כתובת; דיזינגוף = `1 Reines st. tel aviv` — §3).
- `exhibition_id` — `null` = אירוע בלי שיוך תערוכה (אין פס `presented as part of`); `exhibition_volume`.
- `cover_image` (hero; null לאירוע בלי דף), `description_he` (מערך שורות או מחרוזת; `inject.py` גוזר ממנו את ה-description וה-JSON-LD של הדף).
- `artists[]` — `{name_en, slug, image}` (רצועת האומנים); `artists_he`.
- `route` (nullable) — `events/<slug>/`; `null` = אין דף (היום לכל 30 הרשומות יש דף).
- `figma_node_desktop` / `figma_node_mobile`, `figma_file`.
- `card_title_en` — כותרת קצרה לכרטיס (נוצר ל-`#events-upcoming` בהומפייג'). **הקרוסלה הזו הוסרה 2026-08-04 ⇒ אין היום צרכן**; השדה קיים בכל הרשומות (`null` בחמשת אירועי וריאנט רזידנסי SUMII בדיזינגוף — sumii-opening, sumii-melani-hosting, yom-kippur-wish-tree, niki-de-saint-phalle-day, sumii-live-studio) — להמשיך למלא לפי כלל "שדה חדש → לכל הרשומות", לא למחוק.
- `homepage_visible` — ⚠️ לא נקרא ע"י שום קוד, ולא מסונכרן עם `press.json::homepage_visible` (למשל the-space-between: `true` כאן, `false` שם). מה שקובע את ההומפייג' = `press.json` + `homepage.json` (§7).
- נוכחים ברשומות בודדות: `gallery_images[]`, `gallery_videos[]`, `poem_he`, `statement_title_en`, `statement_he`, `note_en`, `note_he`.
- ⚠️ **כיסוי מפתחות לא אחיד** — הכלל "שדה חדש → לכל הרשומות" לא נאכף כאן היסטורית: רשומות ישנות (loneliness, how-many, ktuba, close-look, artist-talk) חסרות חלק מ-`address_en`/`artists`/`date_he`/`figma_file`/`subtitle_he`/`time_end`/`time_label`; the-space-between בלי `subtitle_he`/`time_label`; sumii-melani-hosting בלי `time_label`; sumii-opening בלי `description_he` (ה-description שייגזר ממנו ריק); `exhibition_volume` קיים רק ברשומות עם תערוכה. לבדוק כיסוי בפועל לפני שמניחים "בכל הרשומות".

### 6.2 שדות אופציונליים
- `day_he` (2026-08-04) — יום־בשבוע, מוצג במטא במקום שעה (the-space-between).
- `host_he` (2026-08-04) — מנחה/יזם אורח שאינו אומן האתר ⇒ **בלי קישור לדף אומן**.
- `list_image` (2026-08-04) — קרופ רוחבי לכרטיס ב-`/events/` (רינדור-node אפוי `images/events/<slug>/list-card.webp`, או מיחזור קרופ קיים). בלעדיו → cover של ה-hero.
- `list_title_en` (2026-08-18) — כותרת הכרטיס כשהמעצבת ניסחה אותה אחרת מהפריים של הדף; מזין את `#events-list-data` ואת הכרטיס ב-`/press/`, בעוד `title_en` נשאר קנוני לדף. (bar-cohen: `"…bar cohen - ‘akra’"` בכרטיס מול `"…bar cohen ‘akra’"` בדף.)
- `list_title_he` (2026-08-19) — כותרת הכרטיס **בעברית** במקום אנגלית; מרונדרת ב-`.ttl--he` (FbEzmel, px verbatim 16/14, `dir=rtl`) במקום Copperplate. (the-space-between.)
- `soon` (`true`) — אירוע בלי דף → כרטיס לא-קליקאבילי + טוסט "בקרוב". **דורש `route:null`.** **אין היום שימוש חי:** ארבע הרשומות שנשאו אותו (sumii-opening, nir-giorgio-levin-medina, yom-kippur-wish-tree, sumii-melani-hosting) קיבלו דפים ב-2026-09-27 והמפתח **נמחק** מהן (לא `null`); הענף ברנדרר נשאר לעתיד. ב-`/press/` נשאר כרטיס `.pcard--soon` יחיד — tal-nehoray, שאין לו רשומה ב-`events.json` (רק `press.json::event-tal-nehoray-talk`, `route:null`). **כשנבנה דף:** למחוק את `soon` (ב-JSON ובמירור — לא להשאיר `null`), למלא `route` ב-`events.json` **וב-`press.json`**, למלא ב-`events.json` את `cover_image` ואת `description_he` (`card_title_en` — אין צרכן (§6.1), אפשר `null`), להפוך את כרטיס `.pcard--soon` (`href="#"`) ב-`press/index.html` לקישור רגיל לדף, ולהוסיף ל-`sitemap.xml`.
- `pinned` (`true`, 2026-08-19) — הכרטיס שורד את פילטר התאריך ב-`/events/` (אירוע שהמעצבת עדיין מציגה בפריים הרשימה אחרי שעבר). **שלושה מקומות לסנכרן:** `events.json`, המירור `#events-list-data`, ו-`data-pinned="1"` על הכרטיס המקביל ב-`press/index.html` (כדי שהארכיון יסיר אותו — בית אחד לכל אירוע). **אין היום רשומה עם `pinned`** (הוסר מ-michael-konovalenko ו-livay-levi ב-2026-09-01 — לא להחזיר); הענפים בקוד נשארו. להסיר את הדגל בשלושת המקומות כשהאירוע יורד מהפיגמה.
- `date_tbd` (`true`) — תאריך לא ידוע ("פרטים ותאריך בהמשך"), `date:null`; תמיד "upcoming", ממוין בסוף. אין היום רשומה; הענף ברנדרר נשאר. 🔴 אותו ענף תופס גם `date` חסר/לא-ISO במירור — בשקט (§6.3).
- `date_end` + `date_label` (2026-09-27) — אירוע רב-יומי. `date` = יום ההתחלה, `date_end` = היום האחרון (חסר = אירוע של יום אחד). שתי הרשימות מסננות לפי היום האחרון (§6.3), ו-`/events/` מציג `d.m.yyyy - d.m.yyyy` שהוא מחשב בעצמו. `date_label` = התווית verbatim של כרטיס `/press/` — מידע בלבד, שום רנדרר לא קורא אותו (התווית כתובה ביד ב-`<bdi>` של הכרטיס). תווית הטווח בכרטיסי `/press/` = **פורמט אחיד `d.m.yyyy - d.m.yyyy`** (yom-kippur אוחד ל-`17.9.2026 - 18.9.2026` ב-2026-09-27), כך ש-`/events/` ו-`/press/` מציגים אותה תווית. ⚠️ `date_label` של yom-kippur-wish-tree ב-`events.json` עדיין בנוסח הישן `17.09.26 - 18.09.26` — לא נקרא ע"י קוד; ליישר כשנוגעים ברשומה. **חמישה מקומות לסנכרן:** `events.json` (`date`/`date_end`/`date_label`), המירור `#events-list-data` (`date`/`date_end`), `data-date` + `data-date-end` בכרטיס ב-`press/index.html`, התווית הגלויה ב-`<bdi>` של אותו כרטיס (= `date_label`), ו-`press.json` (`date`/`date_end`). שימוש חי: yom-kippur-wish-tree, sumii-melani-hosting, sumii-live-studio.
- `widths[]` (2026-09-01) — רוחבי srcset לכרטיס ב-`/events/` כשתמונת ה-876w חוצה את כלל-זהב 12 (≥80KB וגם ≥800px). הרנדרר בונה `srcset` מ-`<name>-<w>w.webp` (הרוחב ששווה ל-`w` = הקובץ הראשי) + `sizes="(max-width:768px) 171px, 292px"`; בלי השדה = src יחיד. הרנדרר קורא **רק מהמירור** `#events-list-data`. ⚠️ היום: ב-`events.json` השדה קיים ב-yom-kippur-wish-tree ו-sumii-melani-hosting (`[480,768,876]`), אבל ל-nir-giorgio-levin-medina הוא **רק במירור** — כשנוגעים ברשומה, לרשום אותו גם ב-`events.json`.
- `event_photos[]` (2026-08-18) — `[{src, alt}]` + provenance **אופציונלי** `figma_node` / `figma_image_ref` לכל צילום (מ-2026-08-28; ברשומות ישנות פשוט חסר — לא למלא null). צילומים **מהאירוע עצמו** אחרי שהתרחש — נפרד מ-`gallery_images[]` (היצירות המוצגות). מרונדר בסקשן `.event-moments` + לייטבוקס — רצועת `.tri` כשיש כמה צילומים (close-look, natasha-zeriker, noemi-safir, livay-levi, maria-artamonova, jessica-tabarovsky, sumii-opening), `figure` בודד כשיש צילום אחד (risa-and-noemi). **מירור סטטי ב-HTML — לסנכרן את שניהם** (§1.4). + `figma_node_photos_desktop` / `figma_node_photos_mobile`.
- `photo_credit_stills` / `photo_credit_video` (2026-08-28) — קרדיטי הצילום מעל גלריית הצילומים (natasha-zeriker) + `figma_node_credits_desktop` / `figma_node_credits_mobile`.

### 6.3 כללי רשימות
- `/events/` מציג אירוע כשהיום האחרון שלו (`date_end`, ואם אין — `date`) הוא היום או אחריו **לפי תאריך ישראל** (`todayIL()`, `Asia/Jerusalem` — מבקר בחו"ל רואה אותה רשימה), או כשהוא TBD, או `pinned`. מיון: אירועים עם תאריך עולה לפי `date` (באותו יום התחלה — מי שמסתיים קודם, ואז סדר המירור), TBD בסוף. `/press/` מסיר בזמן ריצה (אותו `todayIL()`) כל כרטיס אירוע שהיום האחרון שלו (`data-date-end`, ואם אין — `data-date`) הוא היום או אחריו, כל כרטיס אירוע בלי `data-date` תקין (TBD — שייך ל-`/events/`) וכל `data-pinned` ⇒ **המשלים המדויק**: אירוע עובר מ-`/events/` ל-`/press/` לבד למחרת היום האחרון. כרטיסי עיתונות (בלי `data-kind`) לא מסוננים.
- 🔴 **כשלים שקטים (אין שגיאה):** `date` חסר/לא-ISO ברשומת המירור ⇒ האירוע נחשב TBD ונשאר ב-`/events/` לתמיד עם "פרטים ותאריך בהמשך"; `data-date` לא תקין בכרטיס `/press/` ⇒ הכרטיס נמחק שם; `date_end`/`data-date-end` לא תקין או לא אחרי ההתחלה ⇒ אירוע של יום אחד.
- אירוע חדש = `events.json` + `#events-list-data` + (כשיש לו כרטיס ארכיון) רשומת `press.json` + כרטיס `.pcard` ב-`press/index.html` + sitemap. פרטים: `docs/routes/events.md`, `docs/routes/press.md`.

## 7. `press.json`
`{ items: [...] }` — כתבות עיתונות + כרטיסי אירועים (לכרטיסי `#press` בהומפייג' ו-`/press/`).
- `id` — יציב (לא לשנות; `homepage.json` מפנה אליו). דוגמאות קיימות: `timeout-manicure-against-darkness`, `13tv-peeling-a-layer`, `portfolio-the-shared-list`; אירועים `event-<slug>` / `event-<slug>-talk` (לשיחות האמנים החדשות — זה הדפוס).
- `type`: `press` | `event`.
- `tag_he` / `tag_en`, `source_he` / `source_en`, `title_he` / `title_en`, `subtitle_he` (+`subtitle_en`), `author_he`, `date`, `cover_image`, `exhibition_id`, `gallery_id`, `event_id`.
- `date_end` (2026-09-27, אופציונלי) — אירוע רב-יומי: מראה של `events.json::date_end`, והכרטיס ב-`/press/` נושא אותו כ-`data-date-end`; `date` = יום ההתחלה. אין כאן `date_label` (§6.2). שימוש חי: `event-yom-kippur-wish-tree`, `event-sumii-melani-hosting`, `event-sumii-live-studio`.
- `route` (nullable) — דף פנימי. כרטיס **אירוע** עם `route:null` = `--soon` + טוסט "בקרוב" (היום רק `event-tal-nehoray-talk`). חריג: `portfolio-loneliness` (בלי `route`, `url:null`, `_alias:"press-1"`) = רשומת alias ישנה של הכתבה `press-1` (`press/press-1/`) — לא כרטיס soon ולא כתבה נפרדת; לא לבנות לה כרטיס. `url` — קישור חיצוני לכתבה המקורית.
- `homepage_visible` — **דקלרטיבי**: כרטיסי `#press` בהומפייג' כתובים ביד ב-HTML ולא נמשכים מכאן בזמן ריצה. חייב להתאים ל-`homepage.json::press_section.item_ids` ולכרטיסים ב-`index.html` (היום 13).
- `figma_article_desktop` / `figma_article_mobile`, `figma_home_card` / `figma_home_card_desktop` / `figma_home_card_mobile` (+`_legacy_figma_*`, `_alias`).
- **כתבות long-form: הגוף נשאר ב-HTML, רק meta ב-JSON.**
- אירועים עתידיים **נשארים** ב-`press.json` וב-markup של `/press/` (מוסתרים בזמן ריצה עד שיעבור התאריך) — לא למחוק אותם.

## 8. `opencalls.json`
`{ opencalls: [...] }` — היום `how-many`, `the-peeler` (שניהם `archived`).
- `id`, `slug`, `title_en`, `title_he`, `title_html`, `status` (`open` | `archived`), `submission_status_he`, `gallery_id`, `gallery_label_he`, `deadline` + `deadline_he`, `city`, `hero_image`, `card_image`, `description_he`, `submission_instructions_he`, `contact{label_he, email, deadline_label_he, note_he}`, `figma_node_desktop` / `figma_node_mobile`.
- אופציונליים: `emotional_triggers` (`{title_he, items[], lines[]?}` — `lines[]` אופציונלי לשבירת שורות כמו ב-Figma; כשקיים ולא ריק, הרנדרר משתמש בו במקום `items[]` (שמחוברים ב-` | `); null ב-how-many), `gallery_images[]`.
- `submission_instructions_he` = `{intro_html, items[], outro_he?}` — `intro_html` הוא HTML מוכן (כולל `<span class="lat">`); `outro_he` רק ב-how-many. `gallery_images[]` = `[{image, video, poster}]` (the-peeler: וידאו + poster; how-many: `null`).
- `contact.email` של קורין — גם ה-`mailto` hard-coded ב-renderer של 150 עמודי היצירה (`docs/routes/works.md`).
- **צרכנים:** `opencalls/*` (fetch-first + `#fallback-opencalls`), `inject.py`.

## 9. `works.json`
`{ works: [...], art_works: [...], exhibition_statements: [...], _note }`

### 9.1 `works[]` — 3 אריחי התמונה של שחמט ההומפייג'
- `{id: "aw-1..3", image, figma_image_ref, artist_id}` (רה-דיזיין 2026-08). אריחי הטקסט (the / art works / more) = HTML סטטי. `components/artwork-lightbox.js` מחפש `data-artwork-id` ב-`works[]` (fetch, HTTP בלבד).

### 9.2 `art_works[]` — כל היצירות (150)
- **סדר המערך = סדר התצוגה ב-`/works/`** (1:1 מול Figma `542:500`; `542:499` = legacy). הכרעות מיקום (רזידנסי באמצע, יצירות שאינן בגריד הפיגמה בסוף) — `docs/routes/works.md`.
- `id` (= `works/<id>/`), `artist_slug` (→ קישור לדף האומן).
- `artist_he` / `artist_en` — אם `artist_he` = null → השם הלטיני מוצג (la-raz-porta). קרדיט מעורב אפשרי (`"שירה טורבוביץ | sumii"` — Latin עטוף `.lat`).
- `title_he` / `title_en` — אופציונלי, דו-לשוני.
- `gallery_slug` + `gallery_en` (→ `/#galleries`) — `medina` | `dizengoff`.
- `sold` (bool → תג "נמכר").
- `details_he` — טקסט אפור אופציונלי; `\n` נשמר (`white-space:pre-line`); גרשיים מנורמלים ל-`ס"מ`.
- `img` (שם בסיס תחת `images/works/v2/`), `w` / `h`, `widths[]` — לבניית srcset; **האחרון = רוחב הקובץ הראשי `<img>.webp`**, השאר `<img>-<w>w.webp` + אח avif לכל אחד.
- `artist_page_pos` (int / null) — סדר בדף האומן (לפי frames `artist-pages-*`). הרנדרר ממיין `(pos || 1e9)` ⇒ null = לסוף לפי סדר המערך. 🔴 **`pos:0` אסור** (`0||1e9` מפיל אותו לסוף). `/works/` מתעלם ממנו. קונבנציית קריאה LTR-פיגמה/RTL-אתר — `docs/lessons.md` 2026-07-15.
- `page` (bool; היום `true` בכל 150) — ב-`/works/` כרטיס עם `page:true` = `<a href="<id>/">`. דפי האומן מתעלמים (הכרטיס שם = לייטבוקס).
- `exhibition_title_he`, `exhibition_slug`, `exhibition_route` — שיוך קבוצה/תערוכה (ראה 9.3). 🔴 **`exhibition_route` של כל יצירות הקולפן = `exhibitions/the-peeler`** (לא `opencalls/…`; עמודי היצירה בונים את הקישור מהשדה, לא hardcode). אחרות: `exhibitions/how-many`, `exhibitions/loneliness`, `sponsors/sumii`.
- `statement_he[]` — **טקסט על יצירה בודדת (per-work)**, לא טקסט-תערוכה (ראה 9.4).
- `kind` — `"residency"` = מידע בלבד (יצירות בלי תערוכה; shira-turbowicz, melani-hekimoglu).
- `hidden` (אופציונלי, לא בשימוש היום) — `/works/` מסנן (`!w.hidden`) ו-`sync_data.py` מוציא מ-`#g-artworks-data`; **לא מסתיר את עמוד היצירה ולא את דף האומן** (להסתרה אמיתית: `_staging/`, `docs/routes/works.md`). ⚠️ `sync_data.py` לא סורק את `_staging/` — אחרי החזרת דף משם להריץ `python3 tools/sync_data.py` (ו-`--check`) לפני קומיט (§1.2).
- collab — ראה 9.5.
- **צרכנים:** `/works/` (`#works-data`), `works/<id>/` (`#artwork-data`), דפי אומן (`art-works.js`), דפי גלריה (`#g-artworks-data`) — כולם generated; `inject.py`; **ועותק ידני:** כרטיסי FIGURES/PRODUCTS ב-`sponsors/sumii/` (8 רשומות, §1.4).

### 9.3 קיבוץ בדפי האומן + `exhibition_statements[]`
- **קבוצה = `exhibition_title_he` (מחרוזת מדויקת)**, לא slug. לכן שתי קבוצות באותה תערוכה אפשריות (`הקולפן` + `הקולפן | interdependence`), וכל הבדל כתיב יוצר קבוצה נפרדת (למשל `'מרחק שקט'` עם גרשיים אצל נעמי מול `מרחק שקט` אצל ליוואי — verbatim, מכוון). `\n` בתוך הכותרת קיים היום (yarden-amir-1/2: `הקולפן | רגש נבחר – נשארתי\nלמרות שידעתי`) והוא **חלק ממפתח ה-join** — לשמור זהה בדיוק ב-`art_works` וב-`exhibition_statements`. ⚠️ הוא **לא** מרונדר כשבירת שורה: ל-`.ex-heading` (דף האומן) ול-`.aw-ex-title` (עמוד היצירה) אין `white-space:pre-line`, ו-`mixedHtml`/`latHtml` לא ממירים `\n` ⇒ מוצג כרווח. שבירה אמיתית = שינוי renderer.
- **דירוג הקבוצות:** `exRank(exhibition_slug)` = האינדקס ב-`__EX_ORDER_INLINE__`, ממוין יורד (החדשה למעלה). slug לא מוכר / `null` ⇒ `-1` ⇒ תמיד מתחת לתערוכות אמיתיות. שוויון (אותה תערוכה) ⇒ סדר ההופעה הראשונה לפי `artist_page_pos` — כלומר **הקבוצה שה-pos הנמוך ביותר שלה קטן יותר עולה ראשונה**; הפיגמה קובעת בתוך תערוכה דרך ה-pos.
- **`exhibition_statements[]`** (top-level, מ-2026-06-23) — טקסט-האומן-על-התערוכה, רשומה לכל `(artist, group)`:
  - `{artist_slug, exhibition_title_he, exhibition_slug, exhibition_route, statement_he[]}`.
  - **מפתח לוגי = `(artist_slug, exhibition_title_he)`**; ה-lookup בדף האומן (`exStatement`) הוא `===` על שניהם.
  - מרונדר בראש הקבוצה (`.ex-group-head`: `h3.ex-heading` מקושר ל-`exhibition_route` + `.ex-statement`).
  - קבוצה בלי רשומה = קבוצה בלי סטייטמנט (לגיטימי — היום: zohar-ron, raz-ronen ו-racheli-reuven בקבוצת `How Many Partners Have You Had?`). ⚠️ ל-hadas-tuval **יש** רשומה לקבוצת `הקולפן | מעורר רגש: החזקה והרפיה` (מ-2026-07-09) — לא דוגמה לקבוצה בלי סטייטמנט.
  - שני אומנים באותה קבוצה משותפת = **שתי רשומות**, ואפשר לנסח כל אחת אחרת בלי שינוי קוד (חי: `הקולפן | interdependence` — בדף הדס השמות בסדר שלה). ⚠️ עמוד היצירה הקנוני (`works/<id>/`) מקבל את ה-fallback לפי `artist_slug` בלבד ⇒ ב-`works/livay-levi-3/` מוצג הנוסח של ליוואי. לנוסח אחר בעמוד היצירה — `statement_he` per-work ברשומה.
- **קבוצה בלי תערוכה — שני וריאנטים:**
  - **עם כותרת** (shira-turbowicz): `exhibition_title_he:"POP UP ART RESIDENCY"`, `exhibition_slug:null`, `exhibition_route:"sponsors/sumii"`, `kind:"residency"` ⇒ קבוצה רגילה, תמיד מתחת לתערוכות.
  - **בלי כותרת** (melani-hekimoglu): שלושת `exhibition_*` = **`null`**, `kind:"residency"`, ורשומת `exhibition_statements` עם `exhibition_title_he:null`. 🔴 **`null` מפורש בשני הצדדים** — ה-lookup ב-JS הוא `===`, ומפתח **חסר** (`undefined`) לא מתאים ל-`null`. (ב-`sync_data.py` ה-`.get()` של Python מתייחס ביצירה לחסר כ-`None`, כך שעמוד היצירה היה מוצא את הטקסט בעוד דף האומן לא — עוד סיבה ל-null מפורש.) דורש renderer page-local בדף האומן ובעמודי היצירה — `docs/routes/artists.md`, `docs/routes/works.md`.
- 🔴 **בכל רשומת `exhibition_statements` שלושת המפתחות `artist_slug`, `exhibition_title_he`, `statement_he` חובה** (ערך `null` מותר, השמטה לא): `sync_data.py` ניגש אליהם ב-`r["…"]`, ורשומה בלי אחד מהם מפילה את הריצה ב-`KeyError` **באמצע** — `data/generated/*.js` ו-`works/index.html` כבר נכתבו, אבל עמודי `works/<id>/`, `#g-artworks-data`, `#fallback-galleries` ובדיקת דפי האומן לא רצים ⇒ עץ חצי-מסונכרן (ב-`--check` — traceback במקום דוח). לתקן את הרשומה, להריץ שוב, ו-`--check` לפני קומיט.
- **legacy:** `alon`, `dan-ben-ary`, `zohar-ron-dan-ben-ari` רצים על renderer ישן בלי קיבוץ/סטייטמנטים/באנר — לא לגעת. `alon-1/2` נשארו עם `statement_he` per-work ובלי מפתחות `exhibition_*` בכלל.

### 9.4 `statement_he` per-work (הבאנר)
- `art_works[].statement_he` = טקסט על **יצירה אחת**. בדף האומן (renderer עם קיבוץ) מרונדר כבאנר רוחב-מלא **מעל** הכרטיס: `.work-statement` (`grid-column:1/-1`) = `.ws-rule` (קו 72px) + `.ws-head` (כותרת היצירה `title_he || title_en`, mixedHtml — Copperplate ללטינית, FbEzmel לעברית) + `.ws-body`. **הכרטיס עצמו נשאר אייטם-גריד רגיל (חצי רוחב)** גם כשהוא יחיד — באנר וכרטיס הם ילדי-גריד נפרדים (ה-wrapper הישן `.work-featured` שמתח את התמונה לרוחב מלא — לא להחזיר); `margin-bottom:-40px` על הבאנר מצמצם את המרווח. (Figma `863:228`.) מופיע רק כש-`statement_he` לא ריק; קבוצות עם `exhibition_statements` לא מושפעות. דף שבו שורת הטקסט הראשונה כבר נושאת את השם מסתיר את `.ws-head` page-local ב-CSS (livay-levi).
- בשימוש היום: `zohar-ron-dan-ben-ari-1` (sex?) ו-`zohar-ron-9` (הקוסם) — How Many; **אין לזוהר `exhibition_statements` בקבוצה הזו**, וכותרת הקבוצה של שתיהן = "How Many Partners Have You Had?" הנקייה (לא "…| sex?"); `livay-levi-4`; `alon-1/2` (מוצגים **רק בעמודי היצירה** — דף alon הוא legacy ומתעלם מ-`statement_he`). הבאנר של `zohar-ron-dan-ben-ari-1` מופיע בדף zohar-ron (דרך `artist_pages`), לא בדף ה-legacy.
- בעמוד היצירה הבודד: `#artwork-data.statement_he` = per-work אם יש, אחרת ה-fallback מ-`exhibition_statements` (§1.2). ה-divider + סקשן התערוכה שם מרונדרים רק אם יש `exhibition_title_he` או `statement_he`.

### 9.5 יצירה משותפת (collab)
- **המתכון המאושר** (חי מ-2026-08-12: `livay-levi-3` "interdependence", ליוואי לוי × הדס טובל, הכרעת Figma `668:13584`):
  - **רשומה אחת** ב-`art_works[]` (`artist_slug` = אומן ראשי).
  - `artist_pages[]` — slugs נוספים שבדפיהם היצירה תוצג (הפילטר: `artist_slug===slug || artist_pages.includes(slug)`). אפשר גם **בלי** `collab` — היום `zohar-ron-dan-ben-ari-1` (`artist_pages:["zohar-ron"]`) מוצגת גם בדף זוהר רון עם קרדיט רגיל. (דפי ה-legacy מתעלמים מהשדה.)
  - `collab[]` — `[{slug, name_he, name_en}]` ⇒ קרדיט שבו **כל שם מקושר בנפרד** (כלל-זהב 10).
  - `collab_connector_he` — ברירת מחדל ברנדרר "בשיתוף". 🔴 **להשתמש ב-`"×"` (U+00D7), לא "x"** — ל-FbEzmel אין גליף `x` לטיני, ו-"x" נופל מהפונט העברי.
  - `exhibition_title_he` ייעודי לקבוצה המשותפת (לא מתמזג לקבוצות הקיימות של השניים) + **רשומת `exhibition_statements` לכל אומן**.
  - ⇒ בגריד `/works/` פעם אחת; בדפי האומנים פעמיים (בדפים נפרדים); עמוד יצירה קנוני אחד.
  - ה-`artist_page_pos` הוא שדה יחיד — חל על שני הדפים.
- **היכן הקרדיט המשותף מרונדר:** `artistCreditHtml` ב-41 דפי האומן (לא ב-3 ה-legacy, שגם מתעלמים מ-`artist_pages`), `artistHtml` ב-`works/index.html`, ו-`artistHtml` בעמוד היצירה — **רק ב-34 מתוך 150 עמודי היצירה** (אלה שמכילים `w.collab`). עמוד ליצירה משותפת חדשה — להעתיק מאחד מהם (§1.5).
- **`title_he_by_artist{slug:"…"}` / `details_he_by_artist{slug:"…"}`** — כותרת/פרטים שונים לכל אומן ביצירה משותפת (`buildRichCard`: `title_he_by_artist[a.slug] || title_he`, `details_he_by_artist[a.slug] || details_he`). **ממומשים רק ב-10 דפי אומן** (וריאנט aharon-bas: aharon-bas, alice-debellis, amnon-lipkin, bar-cohen, hadas-tuval, maria-artamonova, michael-konovalenko + tali-zelnik, shira-turbowicz, melani-hekimoglu). שאר הדפים מתעלמים; `/works/` ו-`/works/<id>/` תמיד קנוניים. **אין היום רשומה שמשתמשת בהם.** לפני שמוסיפים `title_he_by_artist`/`details_he_by_artist` לרשומת `livay-levi-3` — להעתיק את הלוגיקה ל-`artists/livay-levi/` (חסרה שם; ב-`artists/hadas-tuval/` קיימת). 🔴 כלל כללי: יצירה משותפת שמשתמשת בשדות האלה דורשת את הלוגיקה ב-`buildRichCard` **בכל דף אומן שבו היא מוצגת** (`artist_slug` + כל `artist_pages`); דף בלי הלוגיקה מציג בשקט את הערך הקנוני. להעתיק מאחד מ-10 הדפים ולהפיץ בזהירות (regression harness, §1.7).
- כל שדות ה-collab additive / backward-compatible.

## 10. `homepage.json`
- **composition layer** — מפתחות `*_id` / `*_ids` לפריטים מ-JSONs אחרים + בלוקים דקלרטיביים. **`index.html` לא קורא את הקובץ** (HTML כתוב ביד — §1.4); הקובץ מתעד את ההרכב ויש לעדכן אותו יחד עם הדף.
- בלוקים היום: `hero`, `mobile_cta` (`linked_opencall_id`), `open_call_section` (`card_ids`), `exhibitions_now` (`exhibition_ids` — היום `["the-peeler","how-many"]`, `artist_ids`, **`groups[]`** — קיבוץ לפי עיר (2026-09-27): `{city_en, cards[]}`, כרטיס = `{kind: "residency"|"exhibition", gallery_id, route, exhibition_id?, title_en?, image?, logos[]?, gallery_name_en?}`; how-many תחת `berlin` בעוד ב-`exhibitions.json` היא `gallery_id:dizengoff` — פתוח, `docs/routes/homepage.md`), `exhibitions_archive` (`items[]` — `{exhibition_id, gallery_id, image}`, שני כרטיסים; `thumbs_ref`/`active_gallery_id` הוסרו), `art_works_words` / `art_works_words_mobile`, `big_news` (`heading_en`, `title_he`, `subtitle_he`, `address_he`, `gallery_id`, figma), `perfume_promo.perfumes[]` (`name_he`, `exhibition_bar_en[]`, `exclusive_he`, `cta_he`/`cta_url` — nullable), `social_section` (`feed_ref: "instagram.posts"`), `galleries_section` (`gallery_ids`), `galleries_berlin_section`, `x_our_artists` (`items[]` — סדר Figma "mobile order" `1873:1146` (קנוני 2026-09-27, מחליף את `1124:1181`; גם ב-`figma_node_order`), תמונה `work-N.webp` 1:1 למיקום — חוץ מ-work-10/23/31 שמצביעים ל-`work-N-v2.webp` (הקבצים הישנים נשארו, כלל-זהב 8); היום 39 פריטים), `sumii_sponsor`, `soos_sponsor`, `tribe_teaser`, `press_section` (`item_ids`, `view_all_route`).
- `tribe_teaser` — כותרת/קרדיטים/גלריה מעל `#press`; `gallery_images[]`; `figma_gallery_strip_desktop` `361:420` / `figma_gallery_strip_mobile` `363:649`; thumbs = לייטבוקס **בלי CTA** (`docs/components.md` §1.4.1).
- `press_section.item_ids` ⇔ `press.json::homepage_visible` ⇔ כרטיסי `#press` — שלושתם תמיד תואמים. חריגות מכלל "רק כתבות + שני אירועי פתיחה" מתועדות ב-`_note` שלו (gala-night, hadas-tuval, livay-levi — הכרעות משתמש).
- פרטי כל סקשן: `docs/routes/homepage.md`.

## 11. `curators.json`
`{ curators: [...] }` — היום `korin-avraham` בלבד. יש לו schema: `data/_schema/curators.schema.json`.
- `id`, `slug`, `name_en_first` / `name_en_last`, `instagram_handle`, `contact_email`, `badge_en`, `section_heading_en`, `credit_he`, `bio_he`, `portrait` (`src`, `width`, `height`, `alt_he`), `figma_desktop` / `figma_mobile` (עם prefix fileKey).
- `exhibition_slugs[]` — התערוכות בעמוד האוצרת; **סדר = דסקטופ שמאל→ימין**; מובייל — CSS `order` אם נדרש. תערוכה חדשה של קורין → להוסיף כאן.
- מופנה ע"י `curator_slug` ב-`exhibitions.json`, `artists.json`, `sponsors.json`.
- **צרכנים:** עמוד האוצרת (fetch-first + `#fallback-curators`), `exhibitions/how-many|loneliness/` (`#fallback-curators`), `inject.py`.
- ⚠️ כפילויות ידניות (לעדכן ביד אם משתנה): ה-handle `yasalamfashionblog` כתוב גם ב-`about/index.html`, ב-`press/walla/index.html` (בגוף הכתבה) וב-JSON-LD של עמוד האוצרת (head, §1.2); ה-`contact_email` כתוב גם ב-`opencalls.json::contact.email` (ובמירורי `#fallback-opencalls`) וב-`mailto` ה-hard-coded של כל 150 עמודי היצירה.

## 12. `sponsors.json`
`{ sponsors: [...], _note }` — עמודי `sponsors/<slug>/`. **meta בלבד — גוף העמוד ב-HTML** (תקדים כתבות long-form). אין `$schema`.
- `id`, `slug`, `name`, `founder_he`, `title_lockup`
- `exhibition_slug` / `exhibition_route` (nullable — רזידנסי בלי תערוכה), `gallery_id`
- `curator_slug` (nullable → `curators.json`, רצועת `the curator`), `date_start` / `date_end` (nullable — טווח רזידנסי/שיתוף)
- `website`, `model_credit` (nullable), `route`, `cover_image`, `logo`
- `case_exception[]` — מחרוזות מותג שנשארות **lowercase** (Figma `textCase:LOWER`), גוברות על כלל ה-UPPERCASE הגלובלי דרך מחלקה ממוקדת `.brand` (`text-transform:none`) — הכרעת משתמש 2026-08-04. soos: `soos.sound`, `www.soos.audio`, `Bella`; sumii ו-melani: `[]` (הכלל הגלובלי חל).
- `founder_artist_slug` (2026-08-20, nullable) — slug של דף האומן כשהמייסד/ת הוא/היא אומן/ית באתר (sumii → `shira-turbowicz`, melani → `melani-hekimoglu`, soos → null).
- `figma_file`, `figma_node_desktop`, `figma_node_mobile`, `figma_logo_node`.
- **כמה רשומות יכולות לחלוק `route`:** `melani-hekimoglu` חולקת `route:"sponsors/sumii/"` (אין לה עמוד משלה). ב-`inject.py` **הרשומה הראשונה על ה-route קובעת את ה-OG** (`cover_image` → og:image, og:type `article`) וכל הרשומות על ה-route הופכות ל-`about` Brand ב-JSON-LD ⇒ **סדר המערך משנה** (sumii לפני melani).
- ⚠️ פריימי soos בפיגמה (`1318:3287`/`1318:3480`) שוכתבו in-place לעיצוב sumii — ה-node ids ברשומת soos כבר לא מצביעים על עיצוב soos.

## 13. `instagram.json`
- `{handle, posts[{id, image, url}], _note}` — snapshot סטטי מ-Figma (מימוש אמיתי עתידי דרך Instagram Graph API). מופנה דקלרטיבית מ-`homepage.json::social_section.feed_ref`; אין צרכן בזמן ריצה.

## 14. הכרעות קנוניות שנוגעות לדאטה (Audit 2026-07-09 ואילך)
- כותרת loneliness = **"בדידות בתוך סביבה תוססת"** (§5).
- `exhibition_route` של יצירות הקולפן = `exhibitions/the-peeler` (§9.2).
- איות אנגלי קנוני: **"adi duek"**, **"zohar shitrit"** (הכרעת משתמש); ה-slugs נשארים `adi-duak`, `zohar-shtrit` (כלל-זהב 6).
- כתיב עברי של אומנים = `artists.json` (למשל "טלי זלניק", "ארס ברוש") — גם כשב-Figma כתוב אחרת. **"טורבוביץ" — בלי גרש** (הכרעה 2026-09-27: `artists.json`, `works.json::artist_he` = `"שירה טורבוביץ | sumii"`, `sponsors.json::founder_he`); לא להחזיר "טורבוביץ׳" (עם גרש) ולא "טורוביץ׳".
- רחוב דיזינגוף = **Reines** (לא "Raines" של הפיגמה) — `galleries.json`, `events.json::address_en`, דפי האירועים (§3).
- **ערכים ב-JSON שסוטים מהפיגמה בכוונה — לא "לסנכרן" חזרה:**
  - `works.json::shira-turbowicz-2.title_en` = "Sonia Delaunay" (בפיגמה "Sonia Delaun" — קיטוע).
  - `events.json::the-space-between.list_title_he` + `press.json` = "מור צופיה געש" (בפיגמה "צופייה").
  - `events.json::maria-artamonova.description_he` = "האמנית תחשוף" (הכרעת משתמש 2026-08-18; בפיגמה "אמנית").
  - `nir-giorgio-levin-medina` — `date` = 2026-09-30 ב-`events.json`, במירור, ב-`press.json` ובכרטיס `/press/` (הכרעת משתמש 2026-09-27; פריימי הדף `1498:882`/`1498:769` מציגים 30.9, וכרטיס הארכיון בפיגמה `1864:3054` עם 17.9 מיושן — **לא לסנכרן ממנו**).
  - `artists.json::amnon-lipkin.bio_he` = "בדייקנות" (בפיגמה "בדיקנות").
  - `exhibition_statements` של `הקולפן | interdependence` = "גוף", "ותלויה" (בפיגמה "גןף", "ותלוייה").
- **ולהפך — verbatim מכוון שלא "מתקנים":** `details_he` של `melani-hekimoglu-3` (bloom planter) = הטקסט של flow vases (copy-paste של המעצבת, פתוח ב-`docs/todo.md`); `'מרחק שקט'` עם גרשיים אצל נעמי בלבד (§9.3); `volume_en` VOLUME 2 (§5); `time_label` (§6.1); `hours[].time` בקונבנציית bidi (§3).
- פירוט: `docs/routes/works.md`, `sponsors.md`, `events.md`, `events-talks.md`, `artists.md`, `galleries.md`.

## 15. הוסר / לא להחזיר / לא להשתמש
- 🔴 **עותקי דאטה inline בדפי אומן** (`#artists-inline`, `#art-works-inline`, `#ex-statements-inline`, `#ex-order-inline`) — הוחלפו ב-`data/generated/*.js`. לא להחזיר; `--check` נכשל עליהם.
- הוראות ישנות "regen `__ARTISTS_INLINE__` בכל הדפים", "הרץ `sync_works_mirrors.py`", "סנכרן `#g-artworks-data` בשני דפי הגלריה", "סנכרן את מירור `fallback-galleries`", "סנכרן 4 מקומות" — כולן = **`python3 tools/sync_data.py`**.
- `tools/migrate_exhibition_statements.py` — פרוש, לא להריץ.
- `statement_he_by_artist{slug:[…]}` — שדה של המנגנון שלפני 2026-06-23 (קיים רק בסקריפט הפרוש); **אין לו צרכן**. במקומו — רשומת `exhibition_statements` לכל אומן.
- גזירת סטייטמנט-קבוצה מ-"`statement_he` של היצירה הראשונה" — בוטלה (2026-06-23); `statement_he` = per-work בלבד.
- יצירת הקולאב המאוחדת הישנה `aharon-bas-1` (title/details per-artist) — פוצלה ל-`aharon-bas-1` + `bar-cohen-1` עצמאיות; לא למזג ולא להחזיר שדות collab אליהן.
- `homepage.json::tribe_teaser.figma_gallery_strip` (`250:98`) — הוחלף במפתחות `_desktop`/`_mobile`.
- `homepage.json::big_news` — `ring_text_en`, `badge_en`, `image` הוסרו (2026-08-04, סקשן טקסט בלבד).
- הקרוסלה (ה-renderer) של `#events-upcoming` ומירור `#events-upcoming-data` בהומפייג' — הוסרו 2026-08-04 (לכן `card_title_en` בלי צרכן). הסקשן `#events-upcoming` עצמו קיים — סטטי (שני פוסטרים), לא נגזר מ-`events.json`.
- אירוע `amnon-lipkin` — נמחק 2026-08-28 מ-`events.json`, מהמירור ומה-sitemap. הפריימים עדיין בפיגמה — **לא לשחזר**; `nir-giorgio-levin-medina` הוא אירוע אחר (נפל במקור על אותה משבצת 8.9 במדינה; היום 30.9 — §14).
- `pinned` של michael-konovalenko ו-livay-levi — הוסר 2026-09-01; לא להחזיר.
- רזידנסי SUMII **לא** נכנס ל-`exhibitions.json` (חי רק ב-`#g-exhibitions-data` של דיזינגוף).
- Firebase לניוזלטר — נפסל; לא להחזיר (Wix Velo).
