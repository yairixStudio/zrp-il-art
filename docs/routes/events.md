# Events — route notes (רשימת `/events/` + עמודי אירוע שאינם artist-talk)

> **קרא לפני עריכה של:** `events/index.html`, `events/ktuba/`, `events/loneliness/`, `events/close-look/`, `events/artist-talk/`, `events/how-many/`, `events/gala-night/`, ועמודי וריאנט הרזידנסי SUMII: `events/niki-de-saint-phalle-day/`, `events/sumii-opening/`, `events/sumii-melani-hosting/`, `events/yom-kippur-wish-tree/`, `events/sumii-live-studio/`.
> עמודי משפחת ה-artist-talk (`events/<artist>/`, the-space-between, zohar-ron-medina, `nir-giorgio-levin-medina` וכו') → `docs/routes/events-talks.md`. הארכיון `/press/` → `docs/routes/press.md`.
> זה המצב הנוכחי + הכללים הפעילים. היסטוריה: `docs/history/CLAUDE-2026-09-27.md` §4.

## Pages

כל עמוד = `events/<slug>/index.html`, ✅ בכולם.
- `/events/` — desktop `XhGH...::1318:1728` (גריד `1318:1761`) · mobile `XhGH...::1732:140` (מחליף את `1318:2012`; **שוכתב in-place 2026-10-15** — 6 כרטיסים; פריים הדסקטופ לא עודכן ⇒ דסקטופ = הפריסה הקיימת עם אותם כרטיסים)
- `ktuba` — desktop `XhGH...::119:1651` (canonical; legacy `Zn3N...::1213:1644`) · mobile `XhGH...::119:1509` (legacy `Zn3N...::1213:1502`)
- `loneliness` — desktop `Zn3N...::1213:1873` · mobile `Zn3N...::1213:2099`
- `close-look` — desktop `XhGH...::420:1520` · mobile `XhGH...::420:1625`
- `artist-talk` — desktop `XhGH...::818:159` · mobile `XhGH...::818:17`
- `how-many` — desktop `XhGH...::433:2` · mobile `XhGH...::433:179`
- `gala-night` — desktop `XhGH...::1451:1901` · mobile `XhGH...::1451:2070`
- `niki-de-saint-phalle-day` — desktop `XhGH...::1854:2172` · mobile `XhGH...::1854:2033` (**עמוד הבסיס** של וריאנט SUMII)
- `sumii-opening` — desktop `XhGH...::1706:2032` · mobile `XhGH...::1706:1919`
- `sumii-melani-hosting` — desktop `XhGH...::1811:270` · mobile `XhGH...::1811:128`
- `yom-kippur-wish-tree` — desktop `XhGH...::1847:1614` · mobile `XhGH...::1847:1389`
- `sumii-live-studio` — desktop `XhGH...::1854:2493` · mobile `XhGH...::1854:2353`
- ⚠️ שמות הפריימים של חמשת עמודי הווריאנט ("event- artist talk with שירה טורבוביץ") משקרים — אלה לא artist talks.

## Shared rules (כל עמודי האירוע)

- **כל העמודים סטטיים** — `python3 tools/sync_data.py` **לא נוגע באף קובץ כאן**. כל עותק דאטה בעמודי האירוע = מירור ידני (Mirror registry ב-`docs/data-contracts.md`): משנים `data/events.json` ⇒ מעדכנים גם את המירור בעמוד, ולהפך.
- **אירוע חדש (כל סוג, כולל artist-talk) — צ'קליסט:**
  1. `data/events.json` (+`list_image`, לרוב `images/events/<slug>/list-card.webp` 876×487; `img` במירור = אותו נתיב). רב-יומי: `date` = התחלה, `date_end` = היום האחרון, `date_label` = התווית verbatim של כרטיס `/press/` (מידע בלבד — אף רנדרר לא קורא).
  2. מירור `#events-list-data` ב-`events/index.html` (רב-יומי — כולל `date_end`).
  3. כרטיס ב-`press/index.html`: `data-kind="event" data-date="YYYY-MM-DD"` + `<span class="date">d.m.yyyy</span>` (רב-יומי: **גם** `data-date-end`, ותווית `<span class="date"><bdi dir="ltr">…</bdi></span>`) + ה-fallback `grid-template-rows:var(--pc-rows,repeat(N,auto))` ל-N = `ceil(כל הכרטיסים ב-markup/2)` + רשומת `press.json` (`date`, רב-יומי `date_end`; `homepage_visible:false` אלא אם הוכרע) — `docs/routes/press.md`.
  4. אם יש דף: `<title>` + meta description; `sitemap.xml` באותו קומיט → `python3 tools/seo/refresh_sitemap_lastmod.py`; OG אפוי ביד `og/events-<slug>-hero.jpg`; `SEO:auto` מועתק מדף-אחות — JSON-LD Event עם `startDate`/`endDate` ב-`+03:00` ו-`location` = ArtGallery (`galleries/<slug>/#gallery`).
  - 🔴 **לא להריץ `tools/seo/inject.py` על עמוד אירוע:** ענף ה-events בונה מחדש מ-`events.json` — `startDate` בלי שעה, `location` = `#org`, בלי `performer`, ו-og:image מ-`cover_image` דרך `tools/seo/og-dims.json` (בלי רשומה → ה-webp הגולמי). `og_gen.py` שבור.
- **בית אחד לכל אירוע:** `/events/` מציג אירוע כל עוד יומו האחרון (`date_end`, ואם אין — `date`) ≥ היום. `/press/` מסיר בזמן ריצה מ-`.pcard[data-kind="event"]`: כרטיס שיומו האחרון (`data-date-end`, ואם אין — `data-date`) ≥ היום; כרטיס עם `data-pinned`; וכרטיס בלי `data-date` תקין (= TBD, שייך ל-`/events/`). כרטיס בלי `data-kind` (כתבות) לא מסונן — כרטיס אירוע בלעדיו יופיע בשני העמודים. שניהם משווים מול `todayIL()` (`Asia/Jerusalem`; אותו helper). **שינוי בפילטר של עמוד אחד = אותו שינוי בשני.** אימות: מטריצת רגעים × אזורי זמן עם שעון מוקפא + בקרה שלילית (`docs/lessons.md` 2026-09-27).
- **לייטבוקס על צילומי-אירוע** (`docs/components.md` §1.7 — הרחבה מאושרת לכל דפי events): על `.tri` — `data-tri-lightbox="true"` + `data-artwork-gallery="<scope>"` (`cursor:zoom-in` ל-`.is-center` כבר מגיע מ-`components/triptych-gallery.css`); ברצועה/גריד (moments) — `data-artwork-gallery` על מיכל הרצועה (`.strip` / `.moments-row`) + `cursor:zoom-in` מקומי על ה-`img`; על כל תמונה `data-artwork-title`; לטעון `components/artwork-lightbox.css` + `.js`. **חריגים מכוונים:** `the artworks` ב-close-look (שקופיות `<a>`), artist-talk (`<video>`), הגלריה השנייה ב-how-many. שלישייה מצוירת ב-`.tri` = שלוש שקופיות עוקבות ב-DOM + `data-tri-start` על האמצעית (0-indexed) (`docs/components.md` §4).
- **גאומטריית טריפטיך משותפת** (`.event-tri` / `.event-moments`): מרכז 481×841, peeks 302×528 ב-`.6`; ≤1100 360×560 / 220×380 ב-`±326`; מובייל 216×378 / 117×204.75 ב-`±194.5`. בעמוד בלי ערכים משלו — אלה.
- `picture-upgrade.js` עוטף `<img>` ב-`<picture>` — מסגרת שממקדת `>img` צריכה `picture{display:contents}`; **אבל** בתוך flex/grid עם `gap` ה-`<source>`-ים הופכים לפריטים ברוחב 0 ומכפילים את ה-gap ⇒ `picture{display:block}` או `source{display:none}` (`docs/lessons.md` 2026-09-27; נמדד: שורת הלוגואים באוברליי של sumii-melani-hosting גדלה מ-234px ל-267px). ⚠️ `.event-hero .card img{width:100%;height:100%}` (0,2,1) תופס גם לוגו `<img>` באוברליי ומנצח `.ev-cobrand .x` (0,2,0) — ללוגו צריך סלקטור 0,3,0 ומעלה.
- עמודת טקסט `flex:1` ליד תמונה/כרטיס ברוחב קבוע — `min-width:0`. רמפת גודל פונט **רק** בתוך הטווח השבור (`@media (min-width:769px) and (max-width:1100px)` וכו׳, עם `min()` כך ש-1440 לא זז), נגזרת מהמילה הארוכה (נמדדת) (`docs/lessons.md` 2026-09-27).
- שינוי רוחבי → harness הרגרסיה (CLAUDE.md §7.1) עם `--only events/` (פילטר/`todayIL()` → `--only events/,press/`); ל-layout `--widths 390,1024,1366,1440` (הרמפות כאן ב-769–1100 / 1320–1439). טיפוגרפיה רק ב-http.
  - ⚠️ השעון מוקפא (`FIXED_NOW` ב-`snapshot.mjs` = `2026-09-27T12:00`, שעון מקומי; אין override דרך env) ⇒ `/events/` מצולם עם **שני כרטיסים בלבד** (nir-giorgio-levin-medina — יום אחד עם `widths`; sumii-live-studio — רב-יומי); כותרת עברית, TBD, `soon`, `pinned` ורשימה ארוכה לא נבדקים. לבדיקה כזו: לשנות זמנית את `FIXED_NOW` (למשל `2026-09-01T12:00:00` ⇒ 12 כרטיסים) — **אותו ערך בשתי הריצות** — ולהחזיר; לא לקמט, ולא להריץ במקביל לסשן אחר שמצלם baseline. (דריסת `Date` בקונסול לא עובדת.)
- ⚠️ `events.json :: <slug>.homepage_visible` מיושן ואף קוד לא קורא אותו (`true` בכל ששת העמודים הוותיקים כאן, גם בשאינם בהומפייג'; גם `press.json` `homepage_visible` לא נקרא). גריד `#press` בהומפייג' = **כרטיס HTML ידני ב-`index.html`** בלבד; `press.json` `homepage_visible` + `homepage.json :: press_section.item_ids` = רשומות דקלרטיביות לעקביות (`docs/routes/press.md` / `docs/routes/homepage.md`).

## `/events/` — רשימת האירועים הקרובים

### מבנה
- Hero: רצועה אפורה `#EEF0EF` בדסקטופ (Figma `1318:1754`), לבנה במובייל (`1318:2033` — node מהפריים הישן `1318:2012`; בנוכחי `1732:140` לא אומת). כותרת מוערמת צמודה-ימין: "upcoming" (Bold) / "events" (Light). **כיול מדוד: 80 Figma → `60px`, `46px` ב-≤1100, 36 → `27px` במובייל** (הערת ה-CSS מזכירה 64 — הנכון 60; אל "תתקן").
- `.ev-list`: 2 עמודות, gap 48 (32 ב-≤1100); מובייל עמודה אחת, gap 24.
- כרטיס `<a class="ev-card">`: עמודת טקסט (משמאל) `space-between`, מיושרת לימין + תמונה (מימין); דסקטופ `aspect-ratio:292/162.25`, מובייל `171×108`, `object-fit:cover`.
  - chip `#EEF0EF` padding 4/8, Copperplate Light 11.5: "gallery event" / שם הגלריה. **תמיד שתי שורות בשני ה-breakpoints, בלי pipe** (`.sep{display:none}`); `fitEventTags()` מקטין 11.5→8px עד שנכנס, ושם ארוך (>20 תווים) נשבר (`.tag--wrap`).
  - שם הגלריה מטבלת `GALLERY` ברנדרר (`medina`→`kikar hamedina`, `dizengoff`→`dizengoff square`, `flea-market`→`flea market`). ⚠️ `berlin` קיים ב-`galleries.json` אבל לא בטבלה ⇒ אירוע בברלין יקבל תווית ריקה — להוסיף קודם.
  - כותרת Copperplate 13px (כיול מ-16); עברית (`.ttl--he`, `dir=rtl`) FbEzmel Regular px verbatim: 16 דסקטופ / 14 מובייל.
  - תאריך `d.m.yyyy` Copperplate Light 11.5px; רב-יומי `<bdi dir="ltr">d.m.yyyy - d.m.yyyy</bdi>` (מ-`date`/`date_end`, **לא** `date_label`); TBD — "פרטים ותאריך בהמשך" FbEzmel 14.
- מצב ריק `#events-none` ("אין אירועים קרובים כרגע…") — צפוי, לא באג. Inbound: `#events-upcoming` בהומפייג' → `events/`; אין פריט nav "events" ("press & events" → `press/`, פעיל גם ב-`/events/`).

### רינדור, סדר וסינון
- מרונדר מהמירור `<script type="application/json" id="events-list-data">`. `todayIL()`: Intl `formatToParts`, אחר כך `en-CA`, ובסוף התאריך המקומי; כל תוצאה ב-regex `YYYY-MM-DD`; אותו helper ב-`press/index.html` — לשנות בשניהם.
- פילטר: נשאר אם TBD (`date_tbd`, או `date` חסר/פגום) **או** `pinned` **או** היום האחרון (`date_end` אם תקין ומאוחר מ-`date`, אחרת `date`) ≥ היום. מיון: `date` עולה; אותו יום התחלה — מסתיים קודם ראשון; ואז סדר המירור (יציב); TBD בסוף.
- **דסקטופ = זרימת עמודות RTL:** `grid-auto-flow:column; direction:rtl` על `.ev-list`, JS קובע `--ev-rows = repeat(ceil(n/2),auto)` — הכרונולוגיה יורדת בעמודה הימנית ואז בשמאלית (כמו `/press/`); `repeat(3,auto)` = fallback ללא-JS. מובייל: `grid-auto-flow:row; direction:ltr`. כרטיס ראשון `fetchpriority="high"`, השאר lazy; אחרי רינדור `PictureUpgrade.refresh(list)`.
- `soon:true` → `<a class="ev-card ev-card--soon" href="#" aria-disabled="true">` + טוסט "בקרוב" (1.8s) — אירוע שמוכרז לפני שיש לו דף (דורש `route:null`). **כרגע אף רשומה לא משתמשת.** כשהאירוע מקבל דף — המפתח **נמחק** מ-`events.json` ומהמירור (לא `null`). `date_tbd` — הענף נשאר; כרגע אין.
- `pinned:true` — שורד את פילטר התאריך (אירוע שהמעצבת עדיין מציגה בפריים הרשימה אחרי תאריכו). **סנכרון בשלושה מקומות:** `events.json` `pinned`, המירור, `data-pinned="1"` על הכרטיס ב-`press/index.html`; כשהאירוע יורד מהפריים — להסיר בשלושתם. **כרגע אף אירוע לא pinned.**
- `widths[]` (אופציונלי) — לתמונת כרטיס ≥80KB וגם ≥800px (כלל-זהב 12): `srcset` מ-`<name>-<w>w.webp` (הרוחב ששווה ל-`w` = הקובץ הראשי) + `sizes="(max-width:768px) 171px, 292px"`; חובה אחי AVIF לכל וריאנט.

### המירור `#events-list-data` (ידני — לא ב-sync_data.py)
- **אירוע חדש = `data/events.json` וגם כאן.** המירור מחזיק **כל** האירועים כולל עבר — לא למחוק (הפילטר מסתיר בזמן ריצה, ו-`pinned` תלוי בכך); אחד-לאחד עם `events.json` (היום 36 רשומות). אירועים עם אותו יום התחלה ואותו יום אחרון — סדר הרשומות במירור קובע את סדר התצוגה: למקם לפי הפריים. שדות:
  - `slug` — שם התיקייה; ה-href = `<slug>/`, **אלא אם יש `route`** במירור — אז `../<route>` (נכתב רק כשהיעד אינו `events/<slug>/`, למשל כרטיסי הספונסרים `sponsors/<slug>/`).
  - אופציונליים (2026-10-15): `date_start_only:true` — מציג רק את תאריך ההתחלה (כמו בפריים) כש-`date_end` קובע עד מתי הכרטיס ברשימה; `date_text` — טקסט חופשי לשורת התאריך (גובר על הכל; כרגע "פרטים בקרוב..." בכרטיס podcast-station); `gallery_label` — דורס את טבלת `GALLERY` בצ'יפ בלבד ("kikar Dizengoff"); `title_he_suffix` — זנב עברי בכותרת לטינית (`<span class="he">`, FbEzmel).
  - `date` (`YYYY-MM-DD`), `gallery_id` (`medina` / `dizengoff` / `flea-market`).
  - `title_en` = `list_title_en` אם קיים, אחרת `title_en` (bar-cohen: בכרטיס "…bar cohen - ‘akra’", בדף בלי המקף). ⚠️ חריגים ישנים (עבר — לא לנרמל): close-look במירור = "close look — open meeting with tanya shin" (ב-JSON "how many partners have u had?"), gala-night = "gala night — the peeler" (ב-JSON "gala night"); loneliness/how-many ורוב אירועי 2026-09-27 נבדלים רק ברישיות. הכלל חל על חדשות.
  - `title_he` = **רק** `list_title_he`. 🔴 לא להעתיק את `title_he` הרגיל — כל `title_he` במירור מחליף את הכותרת האנגלית בכרטיס.
  - 🔴 **שמות המפתחות במירור ≠ `events.json`:** תמיד `title_en` / `title_he` — **אסור** `list_title_en` / `list_title_he` כשם מפתח. הרנדרר קורא רק `slug, date, date_end, date_tbd, pinned, soon, gallery_id, title_he, title_en, img, w, h, alt, widths`; מפתח אחר (כולל `date_label`) נבלע בשקט והכרטיס מציג כותרת/תאריך שגויים בלי שגיאה.
  - `img` = `list_image` אם קיים; אחרת ידנית (לרוב ה-cover; gala-night = `card.webp`, the-space-between = `hero-480w.webp`); נתיב יחסי לשורש (הרנדרר מוסיף `../`). `w`/`h` אמיתיים. `alt` עברי "<תיאור> — <גלריה>" (ביד). אופציונליים: `soon`, `pinned`, `date_tbd`, `widths`, `date_end`.
- ⚠️ `widths` של `nir-giorgio-levin-medina` קיים **רק במירור** — ברשומת `events.json` חסר; כשנוגעים — להוסיף גם שם.

### תמונות כרטיס (`list_image` — קרופ רוחבי, לרוב 876×487, ב-`images/events/<slug>/`)
- `list-card-v2`: maria-artamonova / jessica-tabarovsky / hadas-tuval / bar-cohen = אותו צילום כמו ההירו בחלון STRETCH+cropTransform של הפריים. **michael-konovalenko חריג:** יצירה אחרת (imageRef `63a698c7…`, קולאז׳ פורטרט על לבן, cover ממורכז) — **לא** קולאז׳ כובע-הפרחים של ההירו. קבצי `list-card.*` הישנים נשארו בדיסק (כלל-זהב 8).
- alice-debellis / zohar-ron: רינדורי-node אפויים מ-2026-08-04 (nodes `1318:3242/3216/3229` ל-alice/zohar/amnon — מיפוי לפי סדר, לא מאומת; amnon נמחק). ⚠️ המעצבת שכתבה את הכרטיסים in-place (`1318:3216` = היום michael-konovalenko, `events.json :: michael-konovalenko._list_image_note`). **לא לרנדר מחדש את ה-nodes האלה** — הקבצים בדיסק הם המקור. anat-wegier ממחזרת `card.webp` (קרופ זהה).
- zohar-ron-medina: imageRef `951e06ff…` (צילום הדג); כרטיס בפיגמה `1318:3218` דסקטופ / `1403:999` מובייל. sumii-opening: רינדור-node (ההירו ב-FIT/contain על `#FAFAFA`).
- nir-giorgio-levin-medina: רינדור STRETCH+cropTransform של `1471:256` (+480/768 + `widths` — ה-webp 201KB, ליטוגרפיה מנוקדת). ⚠️ מעוות מעט, בניגוד לכלל "לא מעוותים צילום" — פתוח (`docs/todo.md`): קרופ cover מ-`99781a55` (`list-card-v2`) = החלפת שדה אחד במירור, בכרטיס `/press/` וב-`events.json::list_image`. **לא לרנדר מחדש את `1471:256`** — היום הכרטיס של niki.
- niki-de-saint-phalle-day: קרופ cover **מיושר-לתחתית** (שורות 846–1439 של המקור), **לא** רינדור ה-node (`1471:256` דסקטופ / `1864:3072` מובייל — STRETCH לא-אחיד).
- sumii-melani-hosting / yom-kippur-wish-tree: `list-card.{webp,avif}` קרופ מה-imageRef (`0f6be5f4…` / `e8ec34f3…`, האחרון ממורכז על חלון ה-cropTransform) + 480/768; `widths:[480,768,876]` ב-`events.json` **וגם** במירור. sumii-live-studio: 28KB בלי `widths`. שאר ה-talk: `docs/routes/events-talks.md`.

### מצב נוכחי מול הפיגמה (פריימי הרשימה `1318:1761` / `1732:140`)
- 🔴 **כלל סנכרון (בקשת משתמש 2026-08-19: "אותם אייטמים, אותו סדר"):** כל כרטיס בפריים הרשימה מופיע ב-`/events/` (חוץ ממה שנמחק בהכרעה — Removed), והסדר **נגזר מהתאריכים** — לא מסדרים ידנית. פערים נסגרים דרך הדאטה: `pinned` = אירוע שעבר ועדיין בפריים; `soon`+`route:null` = בפריים בלי דף. תאריך שהשתנה בפיגמה = לעדכן בכל מקומות הצ'קליסט: `date` + `date_he` ב-`events.json` (רב-יומי `date_end`/`date_label`), המירור, כרטיס `press/index.html` (`data-date`/`data-date-end` **וגם** התווית הנראית), `press.json`, ואם יש דף — שורת המטא, descriptions (meta/og/twitter), JSON-LD `startDate`/`endDate`; בסיום `refresh_sitemap_lastmod.py`. **חריג:** אירוע חי שנוסף מחוץ לפריים — נשאר (תקדימים: the-space-between; elsa-ars-brush, לבקשת המשתמש; sumii-melani-hosting + yom-kippur-wish-tree, מפריים המובייל של `/press/` `1323:528`); לשאול לפני הסרה.
- 🔴 **שתי הכרעות משתמש פתוחות (`docs/todo.md`):** (1) פריימי הרשימה מציגים zohar-ron-medina 24.9, niki 25.9 ו-Live Studio — zohar ו-niki עברו ולכן ב-`/press/` ולא ברשימה; **לא להוסיף `pinned` בלי הכרעת המשתמש.** (2) nir-giorgio-levin-medina (30.9) חסר בשני הפריימים אבל מוצג (data-driven; תקדים elsa-ars-brush) — לא להסיר בלי הכרעה.
- **פריים `1732:140` מ-2026-10-15 (6 כרטיסים):** פופ-אפ elodie k (15.10) · desert queen (15.10) · ever after (18.10) · roni liani (27.10) · window take over (installation) | ma ren (19.10) · the z&r | podcast station | תחנת השידור (בלי תאריך — "פרטים בקרוב...", kikar dizengoff). רשומות `events.json`: `popup-elodie-k`, `popup-desert-queen`, `popup-ever-after`, `popup-roni-liani`, `window-takeover-ma-ren` (route → `sponsors/<slug>/`, `date_start_only` + `date_end` = סוף טווח הספונסר) ו-`podcast-station` (`soon:true`, `date_tbd`, `route:null` — אין דף). **אין להם דפי `events/<slug>/` ואין כרטיסי `/press/`** ⇒ כשייגמרו הם ייעלמו מ-`/events/` בלי ארכיון (פתוח — `docs/todo.md`). הסדר באתר נגזר מהתאריכים: ma ren (19.10) לפני roni (27.10) — בפריים הפוך (נראה לא ממוין); לשאול אם להצמיד.
- 🔴 **תאריכים שהוזזו — לא להחזיר:** zohar-ron-medina 9.9 → **24.9.2026**; nir-giorgio-levin-medina 8.9 → 17.9 → **30.9.2026** (הכרעת משתמש 2026-09-27, לפי פריימי הדף). כרטיס הארכיון `1864:3054` (בתוך `1323:528`) שמציג 17.9 **מיושן — לא לסנכרן ממנו.**
- ⚠️ `1732:732` (כרטיס המובייל של nir) נמחק; `1471:256` (כרטיס nir מ-2026-09-01) = היום niki.
- ⚠️ הערות הקוד ב-`events/index.html` (CSS מעל `.ev-list`, HTML מעל `#events-list`) עדיין מתארות 8 כרטיסים של 2026-09-01 — המירור + המיון בזמן ריצה הם האמת.
- 🔴 ה-slug `nir-giorgio-levin-medina` לפי הגלריה — `nir-giorgio-levin` תפוס ע"י שיחת האמנים שלו ב-how-many/דיזינגוף (17.7.2026); תקדים `zohar-ron-medina`.
- ⚠️ במירור ל-`liel-salman` רשום `h:1749`, בעוד `images/events/liel-salman/hero.webp` בפועל 984×1312 — לתקן ל-`h:1312` (כלל-זהב 12; גם ב-`events-talks.md`; לא ב-todo).
- JSON-LD של ששת העמודים הוותיקים (ktuba, loneliness, close-look, artist-talk, how-many, gala-night) — בלי `+03:00`, רובם בלי `endDate`, `location` = `#org`. לתקן ביד בדפוס עמודי 2026-09-27, **לא** דרך `inject.py` (`docs/todo.md`).

### הכרעות verbatim / טעויות פיגמה שלא משחזרים
- כרטיס the-space-between כתוב בפיגמה **בעברית** (`1318:3227` / `1455:2573`) → `list_title_he`: "מור צופיה געש | מה אנחנו באמת זוכרים ממקום?". בפיגמה "צופייה" — נשמר הכתיב הקנוני **"מור צופיה געש"**.
- בפריים הדסקטופ הכרטיס של hadas-tuval (28.8) נושא בטעות "artist talk with jessica tabarovsky"; המובייל נכון — **האתר מציג hadas**.
- `date_label` של הרב-יומיים (ב-`events.json` בלבד): `8.9.2026 - 11.9.2026` (sumii-melani-hosting), `30.9.2026 - 2.10.2026` (sumii-live-studio), ו-yom-kippur-wish-tree עדיין `17.09.26 - 18.09.26` — ⚠️ לא תואם את כרטיס `/press/` (`17.9.2026 - 18.9.2026`). פורמט נוכחי = `d.m.yyyy - d.m.yyyy`; ליישר את yom-kippur כשנוגעים. (`.ev-lockup-date` `17.09.26 - 18.09.26` **בתוך** עמוד yom-kippur נשאר verbatim מהפיגמה — עיצוב העמוד, לא תווית הכרטיס.)

## `/events/ktuba/` — מיצג חי (zohar ron, loneliness)

- גוף ה-hero = שיר הכתובה + התיאור **בניקוד, verbatim** (= `events.json :: ktuba.poem_he` + `description_he`; לשנות בשניהם).
- `.tri`: 3 צילומים (סדר DOM `slide-02, slide-03, slide-01`) עם **7 dots** (3 אמיתיים + 4 שמורים per Figma — חריג ידוע). לייטבוקס: scope `event-slideshow`, title "live art performance".
- רצועת אומנים (11) מרונדרת ב-JS **רק** מהמירור `#fallback-ktuba-artists` (אין fetch) = מירור ידני של `events.json :: ktuba.artists` — נתיבים עם `../../`; לעדכן שניהם. `_ARTIST_FOCAL` בעמוד = העתק ידני של `FOCAL_POINTS` מדפי האומנים.
- איות אנגלי קנוני (הכרעת משתמש): "adi duek", "zohar shitrit" — ה-slugs נשארים `adi-duak`, `zohar-shtrit` (כלל-זהב 6). כרטיס: רק ב-`/press/` (`press.json :: event-loneliness-3`, `homepage_visible:false`).
- 🔴 טאבלט (לא להסיר; `docs/lessons.md` 2026-09-27): `.event-hero .text-col{min-width:0}` + רמפת `.h-title` לפי המילה הארוכה PERFORMANCE (8.96em) — 769–1100: `max(18px,min(48px,calc((100vw - 608px) / 8.96)))`; 1101–1439.98: `min(64px,calc((100vw - 816px) / 8.96))`, `line-height:1.1875` (ב-1440 ה-64px הבסיסי לא זז). בלעדיהם עמודת התמונה נדחפת מחוץ למסך ב-769–1180.

## `/events/loneliness/` — אירוע הפתיחה של בדידות

- הטקסט האוצרותי המלא ב-HTML (`events.json` = תקציר). בר share + bookmark (`data-item-id="event-loneliness"`) — היחיד במשפחה.
- סקשנים: invitation tri (6: `invite-01,02,04,05,06,03`; scope `event-invitation`, title "the invitation") → `the atmosphere` (וידאו `images/events/loneliness/reel.mp4`, poster `atmosphere.webp`, כפתור play + "אומנים מציגים:" מקושרת) → גלריה שנייה tri (3 `second-*`; scope `event-gallery-2`, title "the atmosphere") → moments grid (14 `opening-*`; scope `event-moments`, title "moments from the opening").
- 🔴 הכותרת הרשמית **"בדידות בתוך סביבה תוססת"**; "בתוך בסביבה" בפיגמה = טעות מוכרעת, לא לשחזר.
- בלי מירור דאטה (ה-`#fallback-*` שייכים ל-`exhibitions/loneliness/`). כרטיס בהומפייג' `#press` + `/press/` (`event-loneliness-4`).
- 🔴 **תמונות משותפות עם עמוד התערוכה:** `images/events/loneliness/invite-01..03`, `atmosphere`, `second-01..03` הן גם גלריית ה-hero של `exhibitions/loneliness/` (`data/exhibitions.json :: loneliness.gallery_images[]` + `#fallback-exhibitions`). החלפה / קרופ / שינוי שם משנה גם אותו — לבדוק את שניהם (harness `--only events/loneliness/,exhibitions/loneliness/`) ולעדכן את שלוש הרשימות (`docs/routes/exhibitions.md`).
- 🔴 טאבלט 769–1100 (אותה רמפת כרטיס כמו how-many; לא להסיר): `--pad-x:48px`, `.event-hero .text{min-width:0}`, כרטיס `flex-basis:380px` / frame 380×575, `.h-eyebrow` `min(80px,calc((100vw - 576px) / 3.02))`, `.gallery` 22px, `.when` `clamp(16px,calc((100vw - 576px) / 11.86),22px)`, banner: bar 18.5px (gap 10) / he 23px / en 9.3px. בלעדיה הכרטיס (492) ושורת התאריך (`nowrap`) דוחפים את ה-hero מחוץ למסך.

## `/events/close-look/` — מבט מקרוב (tanya shin, how-many)

- h1 עברי "מבט מקרוב" FbEzmel **80/72 verbatim** (56 ב-≤1100, 24 מובייל). גוף = מירור של `events.json :: close-look.description_he` (טניה שין מקושרת). ⚠️ "how many partners have **u** had?" — כך בדאטה וב-HTML; unverified אם מכוון — לא לשנות בלי לשאול.
- `the artworks` — `.tri` של 9 יצירות של טניה שין (מרכז contain על רקע בהיר, peeks cover); **כל שקופית עטופה `<a>` → `artists/tanya-shin/` — בלי לייטבוקס, בכוונה.** רצועת `artists`: tanya shin (`images/artists/tanya-shin/portrait-v2.webp`), חץ → `exhibitions/how-many/`. דאטה: שקופיות = מירור סטטי של `events.json :: close-look.gallery_images[]` (אותו סדר: `slide-01`, `tanya-shin/work-01`, `work-02`, `slide-02..07`); `artists` = מירור של `close-look.artists[]` — לסנכרן ידנית.
- **`.event-moments`** — בתחתית, אחרי רצועת האומנים: `.tri` של **11 צילומים מהמפגש**, `images/events/close-look/moment-01..11.{webp,avif}` +480/768 (1125×2000; imageRefs של nodes `1560:5046/5049/5052/5054..5060/5065`). מקור העיצוב: `1560:5014` דסקטופ / `1560:5030` מובייל. גאומטריה משותפת, אבל gap 72 בפיגמה ⇒ peeks ב-`±463.5px`; `object-fit:cover`. `moment-01` peek שמאלי, `moment-02` מרכז (`data-tri-start="1"`), `moment-03` peek ימני. דוטים מוסתרים ≤768. לייטבוקס: `data-artwork-gallery="event-moments"` + `data-artwork-title="moments from the meeting"` על כל שקופית. דאטה: `events.json :: close-look.event_photos[]` (+`figma_node_photos_desktop/mobile`) — **מירור סטטי ב-HTML, לסנכרן ידנית.**
- סדר מובייל (`display:contents`+`order`): hero → כותרת+מטא → artworks → גוף → artists → moments.
- 🔴 **הכרעות משתמש (2026-08-18):** מפריים הרה-דיזיין המלא (`1560:4367` דסקטופ / `1560:4254` מובייל, "artist talk with tanya shin"; שם ה-node "בר כהן" משקר) **מומשה רק הגלריה**. שאר הרה-דיזיין (כותרת אנגלית, פאנל אפור במשפחת artist-talk) לא בוצע — לא לממש בלי בקשה. בפיגמה הגלריה מעל רצועת האומנים; באתר בתחתית (בקשת המשתמש).
- כרטיס: רק ב-`/press/` (`event-how-many-close-look-1`).

## `/events/artist-talk/` — gal pollak + elsa ers brosh (how-many, 11.6.2026, כיכר המדינה)

- תבנית close-look, אבל **כותרת באנגלית** (Copperplate UPPER, שני השמות מקושרים): 28px, 48px ב-≥1320, 22px ב-≤920, מובייל 20px. גוף אנגלי = מירור של `events.json :: artist-talk.description_he`.
- Hero: **תמונה אחת בשני ה-breakpoints** — חלון הראווה `images/events/artist-talk/hero-desktop.webp` (+480/768; imageRef `6fb63f12…`), scrim שטוח `rgba(27,27,27,.32)`, אוברליי "artist talk" + "how many partners have you had?". (הערת ה-HTML מעל הכרטיס — "desktop storefront / mobile live-art portrait" — מיושנת.)
- גלריה: `.tri` של **4 סרטונים** `images/events/artist-talk/clip-01..04.mp4` + poster `clip-0N-poster.webp` (אין אח avif בדיסק, למרות ש-`_image_note` ב-`events.json` אומר webp+avif). ה-mp4 נטען (`data-src`) רק כשהשקופית במרכז, ורק המרכזית מתנגנת. דאטה: `events.json :: artist-talk.gallery_videos[]` — מירור סטטי. **בלי לייטבוקס — בכוונה.**
- רצועת אומנים: gal-polk (`images/artists/gal-polk/portrait-v2.webp`) + elsa-ars-brush (`images/artists/elsa-ars-brush/portrait.webp`), חץ → `exhibitions/how-many/` (מירור סטטי של `events.json :: artist-talk.artists[]`).
- 🔴 **הוסר — לא לשחזר:** hero מובייל נפרד (מיצג קליגרפיה חיה, `97bfe6a2…`) וטריפטיך 6 התמונות — תמונות הקליגרפיה (`97bfe6a2`/`2ae67900`/`a9cb03d4`) שייכות למיצג החי של זוהר רון (ktuba).
- כרטיס: רק ב-`/press/` (`event-how-many-artist-talk`, `homepage_visible:false`).

## `/events/how-many/` — אירוע הפתיחה של how-many (26.5.2026, דיזינגוף)

- תבנית "אירוע פתיחה" (gala-night נבנה עליה). h1 עברי "אירוע הפתיחה" (FbEzmel 64/58); **הטקסט האוצרותי המלא ב-HTML** (`events.json` = תקציר). hero `images/events/event-how-many-2026-05-26-cover.webp` — **משותפת עם כרטיס ההומפייג'**.
- סקשנים: invitation tri (6; scope `event-invitation`, title "the invitation") → `the atmosphere` (תמונה + "אומנים מציגים:" מקושרים) → גלריה שנייה tri (5 `second-*`, Figma `433:87`, **בלי לייטבוקס**) → moments strip (14 thumbs, Figma `433:96`; scope `event-moments`, title "moments from the opening", `cursor:zoom-in`; חץ הכותרת → `exhibitions/how-many/`; חיצי scroll-cue במובייל). תמונות ב-`images/events/how-many/`.
- `.event-tri`: גאומטריה משותפת, peeks ב-`-473px`/`+472.5px`; dots פסים `#EEF0EF` / פעיל `#515151`. כרטיס בגריד `#press` בהומפייג' + `/press/` (`event-how-many-2026-05-26`).

## `/events/gala-night/` — ערב הגאלה של הקולפן (29.7.2026, כיכר המדינה)

- **תבנית אירוע-פתיחה (בסיס `events/how-many/`), לא משפחת ה-artist-talk.** אין פס presented ואין רצועת artist-cards (`events.json` `artists:[]`).
- **סדר דסקטופ = סדר ה-DOM (אין `order` מעל 768):** hero band → גלריה 1 (`.event-gal-a`) → סקשן אומנים (`.event-atmosphere`) → גלריה 2 (`.event-gal-b`) → moments. מובייל (`display:contents`+`order`): hero → כותרת → מטא → גלריה 1 → מכתב → גלריה 2 → אומנים → moments. לא לסדר מחדש את ה-DOM.
- Hero band אפור:
  - כותרת Copperplate "gala night": 80 Figma → **64/58**, `letter-spacing:.1em`, `padding-top:.2em` (מונע חיתוך ראשי אותיות); 44px ב-≤1100; מובייל 24 → **18px**; ≤400px 17px.
  - מטא: גלריה Regular / תאריך·שעה Light, 28px (22 ב-≤1100, 14 מובייל); נקודה 1×1 per Figma. **השעה `19:30-21:30` verbatim — התחלה-סיום, הפוך משאר המשפחה. לא "לתקן".**
  - **מכתב האוצרת המלא ב-HTML**: FbEzmel Light 18/20 ממורכז (16 מובייל). "Welcome aboard." = `.lat` 18 Figma → 14px (13 מובייל). "הקולפן" הראשון → `exhibitions/the-peeler/`; חתימה (Regular) "אוצרת התערוכה - קורין אברהם" → `curators/korin-avraham/`. `.dbr` = דסקטופ בלבד.
  - תמונה: פוסטר ההזמנה `images/events/gala-night/hero.webp` 984×1488 +480/768 (imageRef `93313e4b…`), **זהה בשני ה-breakpoints, בלי scrim/אוברליי**; 492×744 דסקטופ, 380×580 ב-≤1100, מובייל full-bleed 390×520. ה-fill השני בפריים המובייל = leftover מוסתר — לא להשתמש.
- **שתי גלריות טריפטיך** `.event-tri` (`gallery1-01..03`, `gallery2-01..03`; dots-פסים 32×2), גאומטריית how-many. לייטבוקס: scopes `event-gallery-1` / `event-gallery-2`, title "gala night".
- **סקשן אומנים** `.event-atmosphere`: `atmosphere.webp` (imageRef `b8f85e72…`, קרופ מרכזי 984×1488; שכבות ה-SVG/לבן בפריים לא נראות — לא לשחזר) + **22 אומנים מקושרים** FbEzmel Light 28/32 ממורכז (max-width 590; 22px ב-≤1100; מובייל 16/20 מתחת לתמונה ברוחב מלא 638h), NNBSP סביב ה-pipes, שבירות לכל breakpoint דרך `.dsep`/`.msep` + `.dbr`/`.mbr`. תיקונים מוכרעים מול הפיגמה (לא להחזיר): נוסף pipe חסר בין מיכאל קונובלנקו לאהרן בס; "אליצ׳ה דבליס" → **"אליס דה בליס"**; "טלי צלניק" → **"טלי זלניק - סטודיו פיס אוף מיין"** (כולל שם הסטודיו — לא לקצר).
- **רצועת moments**: **13 צילומים** `images/events/gala-night/moment-01..13-v2.{webp,avif}` (Figma `1452:2286…2273`). תאים 178×148 דסקטופ (gap 6) / 100.25×121.52 מובייל (gap 4), `object-fit:cover; object-position:50% 0`, גלילה אופקית עם snap; חיצי scroll-cue במובייל (Figma `1451:2186`); כותרת "moments from the opening": 28px Light דסקטופ; מובייל Figma 24 → 19px אופטי (Regular, ls .02em); חץ → `exhibitions/the-peeler/`. לייטבוקס `event-moments`, `cursor:zoom-in`. (14 רינדורי-node הישנים `moment-01..14.webp` 534² נשארו בדיסק לא-מקושרים — כלל-זהב 8.) ⚠️ `events.json :: gala-night._note` אומר 14 תאים — מיושן; ב-HTML 13.
- Header דסקטופ לבן: `body.page-event-gala-night site-header .nav{background:#fff}` (≥769).
- התאריך עבר → נושר מ-`/events/`; קיים ב-`/press/` ובגריד `#press` בהומפייג' (`event-gala-night`, Figma `1323:570`; כרטיס `images/events/gala-night/card.webp` 584×369). OG `og/events-gala-night-hero.jpg`.

## וריאנט אירועי רזידנסי SUMII — Shared rules

- **העמודים:** `niki-de-saint-phalle-day` (**עמוד הבסיס**), `sumii-opening`, `sumii-melani-hosting`, `yom-kippur-wish-tree`, `sumii-live-studio` — אירועי ה-POP UP ART RESIDENCY של SUMII (שירה טורבוביץ; `sponsors/sumii/`) בגלריית כיכר דיזינגוף, **בלי תערוכה** (`exhibition_id:null`).
- **מעטפת artist-talk** (בסיס `events/livay-levi/`): פאנל `#EEF0EF`, עמודת טקסט + כרטיס תמונה 492×744 (טאבלט 769–1319: עד 400×640), רצועת אומנים; מובייל `display:contents`+`order` (hero ראשון, כל בלוק על לבן). **בלי** `.h-body`/`.h-presented`/Solway/moments (חוץ מ-sumii-opening). **אח חדש = להעתיק מעמוד הבסיס verbatim ואז למדוד מחדש** מול הפיגמה; תיקון ב-shell של משפחת ה-artist-talk → לבדוק גם כאן (ולהפך).
- **בלוקים לשימוש חוזר:**
  - `.sumii-lockup` — שם הגלריה (`the art gallery by / erez zielinski rozen`, Copperplate Light ls .13em → הומפייג') → `.ev-lockup-logos` → `.ev-lockup-body`. `.ev-lockup-logos` = **שורה** (gap 33) של `.ev-lockup-item` — לוגו מעל שם מקושר (gap 6.58 / 5 מובייל); שותף שני (מלאני) = `.ev-lockup-item` שני: `images/sponsors/melani/logo.webp` (רסטר שקוף 450×258) → `artists/melani-hekimoglu/`.
  - `.ev-reg` — הרשמה / כניסה חופשית (FbEzmel Light 16/20; האימייל `.lat` — `href` lowercase `mailto:`, תצוגה UPPERCASE).
  - `.ev-cobrand` — co-brand לבן על התמונה (שם הגלריה / X 28.8 verbatim / לוגואים), `aria-hidden`, בלי קישורים; לוגו מלאני לבן = `filter:brightness(0) invert(1)` על הרסטר.
  - רב-יומי = `.date` יחיד ב-`.h-meta .row-2`, **בלי נקודה ובלי שעה** (נקודת ה-1×1 בפריים הדסקטופ = leftover). שעות פתיחה = `.ev-schedule` אחרי הגוף.
- **שונה מהמשפחה — כל ערך נמדד מול הדיו בפיגמה ומתועד בהערות ה-CSS של העמוד (לקרוא לפני שינוי):**
  1. כותרת 64/72 (או 62/72), line-height **verbatim**, **בלי** ה-`padding-top:.2em` המשפחתי, `.dbr` לשבירות דסקטופ/טאבלט; בטאבלט (ובחלק מהעמודים גם ב-1320+) הגודל עוקב אחרי רוחב העמודה (`min()` / `cqi`), עם מרווח לפס-גלילה קלאסי (`100vw` כולל אותו).
  2. **כיול Copperplate לפי `textCase` של ה-node:** `UPPER` → px של הפיגמה **verbatim** (למשל שם הגלריה בלוקאפ); `LOWER` (small caps בפיגמה) → מקטינים (אוברליי 24→21, כתובת 16→14 בשני ה-breakpoints, כותרת מובייל 24→19).
  3. `.lat` בפסקה ובאימייל ב-**1em**, לא .88em.
  4. scrim = `linear-gradient(0deg, rgba(0,0,0,.5), transparent)` בשני ה-breakpoints (sumii-opening: בלי).
  5. אוברליי `.ev-cobrand`: `top:51.4%` דסקטופ / `50%` מובייל (sumii-opening 51% / 50.2%; sumii-melani-hosting 53.3% / 50.2%; sumii-live-studio 53.3% / 50%).
  6. preload ל-woff2 (לא ל-.ttf/.otf).
- כתובת "1 Reines st." בכולם (בפיגמה Raines). הכתיב "שירה טורבוביץ" **בלי גרש**.
- **לוגו Sumii:** class `sumii-logo` (לא `logo` — מתנגש עם `.logo` הגלובלי של `site-chrome.css`); כל עמוד מחזיק עותק של `<symbol id="sumii-mark">` (currentColor; מ-`sponsors/sumii/` — `docs/routes/sponsors.md` — Assets) + `<use>`. לוגו Sumii → `sponsors/sumii/`; "שירה טורבוביץ" → `artists/shira-turbowicz/`.
- רצועת אומנים: shira-turbowicz (thumb = מיחזור `images/artists/grid/shira-turbowicz`); החץ ליד "artists" לא מקושר (אין תערוכה). `events.json :: <slug>.artists[]` משקף את הרצועה.
- **SEO ידני** (`SEO:auto` ביד; 🔴 לא `inject.py`): `location` = ArtGallery `galleries/dizengoff/#gallery` (+PostalAddress), `eventStatus`/`eventAttendanceMode`, `performer` איפה שהוגדר (לא ב-niki). ל-`og-dims.json` יש רשומות ל-niki, sumii-melani-hosting, yom-kippur-wish-tree ו-sumii-live-studio (המפתח = `images/events/<slug>/hero.webp`), ו-cover של sumii-opening ממופה ל-OG של הספונסר (מפתח משותף — בסקשן שלו). אח חדש = להעתיק את הבלוק מאח SUMII.
- **חיווט:** כמו הצ'קליסט ב-Shared rules, עם `homepage_visible:false` ב-`events.json` וב-`press.json` (`event-<slug>`); `events.json` כולל `route`, `cover_image`, `list_image`, `figma_node_*`. רב-יומי: `date_end` בשלושת הקבצים + `data-date-end` בכרטיס + `date_label` ב-`events.json`.

## `/events/niki-de-saint-phalle-day/` — day of niki de saint phalle (25.9.2026, עמוד הבסיס)

- 10:00–14:00, כניסה חופשית בהרשמה מראש; **NIKI** = הפסל הראשון בקולקציית FIGURES. JSON-LD `2026-09-25T10:00:00+03:00` → `14:00:00+03:00`; OG 1200×1801.
- **מבנה:** כותרת `day of niki de<br class="dbr"> saint phalle` — **לא מקושרת** (ניקי אינה אומנית האתר) → מטא (גלריה; תאריך `·` שעה; `14:00-10:00` verbatim בלי `<bdi>`) → `.sumii-lockup` [שם הגלריה; `.ev-lockup-item` יחיד: לוגו Sumii מעל "שירה טורבוביץ"; פסקת FbEzmel Light 21/25.93 בתיבה 448.63 עם `.lat` NIKI / FIGURES / SUMII, ו-**NIKI → `works/shira-turbowicz-3/`**] → `.ev-reg` ("כניסה חופשית בהרשמה מראש בלבד" + `info@sumiiworld.com`) → כתובת Dizengoff Square / 1 Reines st. מובייל: hero → כותרת → מטא → לוקאפ → הרשמה → כתובת → אומנים.
- **כיולים:** כותרת 64/72 (עם 58 הבלוקים מתחתיה ישבו גבוה מהפריים); טאבלט 44/50, וב-769–1050 `min(34px, calc((100vw - 577px) / 8.6))` (ב-34 קבוע 4 שורות ב-769–849); מובייל 24→19. שם הגלריה בלוקאפ 21/22 דסקטופ, 16/17 מובייל — **verbatim** (Figma `textCase:UPPER`); אוברליי 24→21, לוגו 85.8×39.07; כתובת 16→14; `.lat` ב-1em (ב-.88em השורה "SUMII של FIGURES." יצאה קצרה).
- **hero:** imageRef `f27f37e5…` (פסל ה-Niki), מקור 1066×1600 לא-חתוך +480/768 — האספקט בין שני חלונות הפיגמה ⇒ קובץ אחד ב-cover (תקדים elsa-ars-brush). **אינו** מיחזור של `shira-turbowicz-3` (אותו פסל, צילום אחר).
- האירוע עבר ⇒ חי רק ב-`/press/`, והכרטיס שלו נושא כרגע את ה-`fetchpriority="high"` הסטטי (`docs/routes/press.md`). 

## `/events/sumii-opening/` — opening night event - ART RESIDENCY by sumii (2.9.2026)

- ערב הפתיחה, 18:00–21:00, בהרשמה מראש. JSON-LD `2026-09-02T18:00:00+03:00` → `21:00:00+03:00`. **הבדלים מהבסיס:**
  1. **בלי scrim** בשני ה-breakpoints. ב-rect הדסקטופי רשום fill שטוח `.4`, אבל הרינדור לא צובע אותו — לא להוסיף.
  2. **הלוקאפ הוא GROUP אבסולוטי בפיגמה** (`1706:2456` / `1707:253`) ⇒ `gap:0` ו-`margin-top` לכל ילד לפי קואורדינטות ה-y (26.83 / 6.97 / 7.02 / 27.49 / 11.68 בדסקטופ; מובייל ÷1.2966). סדר: שם הגלריה → `hosting an art residency by` → לוגו Sumii 111.25×50.66 מעל שם האמנית → `scented with [Until Ten] by zielinski rozen` → הערת ההרשמה (**בתוך** הלוקאפ). גדלי Copperplate בלוקאפ **verbatim** (20.75 / 17.33 / 15.5; מובייל ו-769–1050 16 / 13.37 / 12; `textCase:UPPER`). מובייל: קופסה קבועה 314 (padding 39 / 42.5).
  3. **כותרת 62/72** (כיול מול דיו ה-small caps). `by&nbsp;sumii` משחזר את שבירת הפיגמה (4 שורות דסקטופ / 2 מובייל). **"event - art" = `<span class="nw">` (nowrap)** — `&nbsp;` ליד מקף לא מונע שבירה אחרי המקף (UAX #14), וב-789–818 "ART" נשאר לבד. 1320+: `min(62px, 9.2cqi)` על `container-type` של עמודת הטקסט (תקדים jessica); טאבלט 44/50; 769–1050 34/38; ≤900 כותרת 28/32 ומטא 18, שורות ה-host וה-scent נשברות (`.host` `text-wrap:balance`); מובייל 19px + `text-wrap:balance`. `.h-address` `text-wrap:balance`.
  4. **לוגו Until Ten** = SVG inline מ-`1706:2460` (3 paths, `currentColor`, `role="img" aria-label="Until Ten"`), **בלי קישור** (היעד לא ידוע — `docs/todo.md`). "by zielinski rozen" **לא מקושר**.
  5. **רצועת `.event-moments`** (Figma `1815:650` / `1815:622`; הרצועה `1815:651` / `1815:623` = `figma_node_photos_*`), בין הפאנל לרצועת האומנים (מובייל `order:6`): גאומטריה משותפת, אבל **peeks מוצמדים 151.5px מהקצוות** (`.is-prev{left:151.5px}` / `.is-next{left:calc(100% - 151.5px)}`, תקדים jessica); טאבלט 769–1319 בקנה .79 (380×665 / 239×417 ב-±373.5); מובייל **ממורכז** (ההיסט של 16px בפיגמה = ארטיפקט flex-end), padding `8px 16px 24px`; **בלי דוטים ובלי חיצים**. **10 צילומים** = ה-nodes הרופפים `1815:665–674` (single-fill, 1638×2048): השלישייה המצוירת ראשונה — moment-01 = `674` (peek שמאל, `a6784abf`), moment-02 = `673` (מרכז, `27f3c765`, `data-tri-start="1"`), moment-03 = `672` (peek ימין, `f74b8988`), ואחריהם 665→671; אף צילום לא הושמט. master 1280×1600 +480/768/1080, `sizes="(max-width:768px) 303px, (max-width:1319px) 532px, 673px"` (cover של 4:5 בתוך 481×841). לייטבוקס scope `event-moments`, title "moments from the opening night". דאטה: `events.json :: sumii-opening.event_photos[]` — **מירור סטטי ב-HTML, לסנכרן ידנית**.
  6. אוברליי `top:51%` / `50.2%`, לוגו 70.38×32.
- **hero = מיחזור `images/sponsors/sumii/hero.webp`** (1620×2160 +480/768/1080; גם `cover_image`), `sizes="(max-width:768px) 100vw, (max-width:1319px) 480px, 558px"` (cover של 3:4 בכרטיס 492×744 מרונדר ברוחב 558). קישורים: שם הגלריה → הומפייג', `mailto:info@sumiiworld.com`. performer שירה טורבוביץ. `list-card` = רינדור-node.
- OG `og/events-sumii-opening-hero.jpg` 1200×1600 — ⚠️ **אין רשומה ב-`og-dims.json` ואי אפשר להוסיף** (המפתח = תמונת המקור, ו-`images/sponsors/sumii/hero.webp` כבר ממופה ל-`og/sponsors-sumii-hero.jpg`) ⇒ `inject.py` על הדף יחליף את ה-og:image (`docs/todo.md`).
- **`.ev-scent` במובייל = `min-height:27.48px` + `flex-wrap:wrap`** (לא `height` קבוע): כשורה אחת זהה לפיגמה (360+); ב-≤~330 "by zielinski rozen" יורד לשורה שנייה במקום לגלול את הדף הצידה (נמצא ב-`tools/qa/sweep.mjs`, 2026-10-15).

## `/events/sumii-melani-hosting/` — hosting event — sumii & melani hekimoglu (8–11.9.2026)

- שולחן חג לקראת ראש השנה, כניסה חופשית. כרטיס הרשימה בפיגמה: מובייל בלבד `1816:916` (בתוך `1323:528`). **הבדלים מהבסיס:**
  1. **מטא = טווח** `8 ספטמבר 2026 - 11 ספטמבר 2026`, בלי שעה ובלי נקודה (הנקודה `1811:311` = leftover).
  2. **שורת `hosting event 08.09-11.09`** (`.ev-lockup-host` / `.ev-hosting`, Copperplate Light 17.33 verbatim — בפיגמה UPPER; מובייל 13.37) מעל **שורת לוגואים כפולה**: Sumii + מלאני (79.61×45.7 / 60×35 → `artists/melani-hekimoglu/`), ומתחת לכל לוגו שם עברי מקושר (שירה טורבוביץ / מלאני הקימוגלו); פריטים ברוחב קבוע 115.83 / 126.36 (88 / 96 מובייל).
  3. **`.ev-schedule`** — שעות פתיחה (FbEzmel Light 16/20, שלוש `<p>` במרווח 20 = השורות הריקות של הפיגמה); בדסקטופ בלוק אח **אחרי** `.sumii-lockup` (`1812:154`), במובייל אחרי הלוקאפ (`order:5`). השעות **verbatim בסדר לוגי עם en-dash** (`10:00–14:00`) בבלוק RTL, **בלי `<bdi>`** ⇒ מוצגות `14:00–10:00` כמו בפריים. `Live Installation` = `.lat` 1em.
  4. `.ev-reg` = "הכניסה חופשית" בלבד.
  5. אוברליי ה-hero = שם הגלריה / X / Sumii לבן + **מלאני לבן** (113.26×66.2; בפיגמה trace וקטורי — כמעט זהה), `top:53.3%` / `50.2%`, הלוגו `loading=lazy`; באוברליי `picture{display:block}` (לא `contents`).
- **כותרת** `hosting event<br> sumii & <a>melani<br class="dbr"> hekimoglu</a>` — 3 שורות בדסקטופ, 64/72 ב-1440; מעל 769 **`min(64px, 10.7cqi)` על `container-type` של עמודת הטקסט** (בלי זה ב-1320–1379 "hosting event" נשבר לשתיים; תקדים jessica), טאבלט `min(44px, 10.7cqi)`, 769–1050 `min(34px, 10.7cqi)`; מובייל 19. "melani hekimoglu" בכותרת **מקושר**; "sumii" (מותג) **לא**.
- **hero:** imageRef `0f6be5f4…` **1279×1600 לא-חתוך** (+480/768/1080) — חלון הדסקטופ תת-קבוצה של המובייל ⇒ cover משחזר את שניהם; scrim `.5`. leftovers בפיגמה: `13066b05…` + fill שטוח .4 — לא להשתמש.
- רצועת אומנים: shira-turbowicz + melani-hekimoglu (thumbs גריד; במובייל כרטיסים ברוחב 96 per Figma). performer שתיהן; OG 1200×1501; JSON-LD `2026-09-08T10:00:00+03:00` → `2026-09-11T14:00:00+03:00`. דאטה: `date_end:"2026-09-11"`, `date_label:"8.9.2026 - 11.9.2026"`; `time_start`/`time_end` = גבולות ה-JSON-LD, בלי `time_label` (השעות משתנות לפי יום).

## `/events/yom-kippur-wish-tree/` — Yom Kippur Event // wish tree (17–18.9.2026)

- בהשראת "עץ המשאלות" של יוקו אונו; חמישי–שישי 10:00–14:00, כניסה חופשית. כרטיס הרשימה בפיגמה: מובייל בלבד `1864:3058` (בתוך `1323:528`). **הבדלים מהבסיס:**
  1. מטא = **טווח** `17 ספטמבר 2026 - 18 ספטמבר 2026` ב-`.date` יחיד (שני `<bdi>`), בלי נקודה ובלי שעה (הנקודה `1847:1655` = leftover); ב-769–1050 הטווח נשבר בין שני התאריכים.
  2. `.ev-lockup-when` = שורת התאריך `17.09.26 - 18.09.26` (`.ev-lockup-date`, `dir=ltr`, verbatim; Copperplate 17.33 verbatim, מובייל 13.37) + שורת הלוגואים כתת-עמודה אחת (הלוגו 6.97px מתחת לתאריך, 10px במובייל), כך שהמרווחים החיצוניים של הלוקאפ (22/21px) נשמרים.
  3. השעות **בתוך** `.ev-lockup-body`, verbatim ("חמישי–שישי: 10:00-14:00"). `.ev-reg` = "הכניסה חופשית" בלבד (בלי אימייל).
- **כותרת** `yom kippur<br class="dbr"> event&nbsp;// wish<br class="dbr"> tree` — 62/72; ב-1320+ `min(62px, calc((100vw - 781px) / 8.9))`, ב-769–1050 `min(34px, calc((100vw - 577px) / 8.9))` ("EVENT // WISH" = 8.9×font-size, עמיד לפס-גלילה קלאסי) — 3 שורות בכל 769–1920; מובייל 18px (ה-19 של niki היה נשבר) + `text-wrap:balance` ("YOM KIPPUR" / "EVENT // WISH TREE"). כתובת `text-wrap:balance`; בטאבלט 769–794 balance על הגוף + nbsp ב"יוקו&nbsp;אונו".
- **hero:** בפיגמה crop `318b6c` (795×1060, 3:4) נמתח לכרטיס 492×744 (~13% עיוות אנכי) ⇒ נאפה **חלון-איחוד** 795×1202 (x33 y261 מהמקור 900×1600, אותו מרכז) +480; דסקטופ מציג אותו שלם, cover במובייל חותך בדיוק לקרופ הפיגמה — קובץ אחד, בלי `<picture>`.
- ⚠️ התמונה (וכרטיס הרשימה, imageRef `e8ec34f3…`) = **חלון הראווה של דיזינגוף** ("HOSTING ART RESIDENCY BY SUMII") — verbatim מהפיגמה; לא "לתקן".
- רצועת אומנים = shira-turbowicz. `list-card` 876×487 +480/768 (`widths` — ה-webp 83KB). JSON-LD `2026-09-17T10:00:00+03:00` → `2026-09-18T14:00:00+03:00`. דאטה: `date_end:"2026-09-18"`, `date_label:"17.09.26 - 18.09.26"` (⚠️ נוסח ישן — ראה "הכרעות verbatim").

## `/events/sumii-live-studio/` — Live Studio // Sumii (30.9–2.10.2026)

- סטודיו חימר LIVE, שלושה ימים; SUMII מארחת את **מלאני הקימוגלו**; 10:00–14:00, כניסה חופשית בהרשמה מראש. **הבדלים מהבסיס:**
  1. כותרת `live studio&nbsp;<span class="sl">/</span>/<br class="dbr"> sumii` — 64/72. nbsp לפני "//" (לא יישאר לבד בשורה); `.sl` מצמצם את ה-"//" (`letter-spacing:-.22em` — הלוכסן שלנו רחב מזה של הפיגמה). ב-1320+ `min(64px, calc((100vw - 781px) / 8.62))`, ב-769–1050 `min(34px, calc((100vw - 577px) / 8.62))`; טאבלט 44/50; מובייל 19px.
  2. מטא = טווח `30 ספטמבר 2026 - 2 אוקטובר 2026` (`<bdi>` אחד), בלי נקודה ובלי שעה (נקודת הדסקטופ = leftover).
  3. **לוקאפ שני שותפים בשני ה-breakpoints:** Sumii משמאל ("שירה טורבוביץ" → `artists/shira-turbowicz/`) + לוגו מלאני מימין (→ `artists/melani-hekimoglu/`, "מלאני הקימוגלו"); פריטים 115.83 / 126.36 (88 / 96 ב-≤1050 ובמובייל).
  4. גוף רחב יותר (498) + **לו"ז תלת-יומי** `<p class="ev-schedule">` **בתוך** `.ev-lockup-body` (`30.09 | 10:00-14:00 | סטודיו חימר לייב סומי ומלאני קרמיקה` וכו' — שעות verbatim התחלה-סוף); "מלאני" מקושרת בגוף ובלו"ז.
  5. `.ev-reg` = "כניסה חופשית בהרשמה מראש בלבד" + `info@sumiiworld.com`.
  6. אוברליי co-brand מוסיף את לוגו מלאני הלבן ליד Sumii, `top:53.3%` / `50%`, הלוגו `loading=lazy`; כאן `.ev-cobrand .ev-lockup-logos source{display:none}` (במקום `picture{display:block}` של hosting).
- **QA (לא להסיר):** ב-769–907 שבירות ה-`.dbr` של הגוף מוסתרות (+ balance, ו-nbsp ב"תיראה&nbsp;בסופם."); לו"ז / הרשמה / תאריך מוקטנים עם העמודה ב-769–1050, ורווח הלוגואים מתכווץ (רצפה 8px) לפני שהוא גולש; במובייל <380 שורת הלו"ז הארוכה נשארת אחת; כתובת `text-wrap:balance`; אין גלישה ב-320–1920.
- **hero:** קובץ יחיד לא-חתוך 1086×1448 (+480/768) ב-cover, scrim `.5`. רצועת האומנים = shira-turbowicz בלבד (מלאני מקושרת בלוקאפ ובגוף). `list-card` 876×487 (28KB, בלי `widths`). performer שתיהן; JSON-LD `2026-09-30T10:00:00+03:00` → `2026-10-02T14:00:00+03:00`. דאטה: `date_end:"2026-10-02"`, `date_label:"30.9.2026 - 2.10.2026"`; מוצג ב-`/events/` עד 2.10 כולל, והכרטיס ב-`/press/` (`data-date-end`) מוסתר עד 3.10.

## Removed / do not restore

- **`events/amnon-lipkin/` נמחק (2026-08-28, בקשת משתמש)** — הדף, התמונות, ה-OG, והרשומות ב-`events.json`, במירור וב-sitemap. הפריימים בפיגמה (`1145:1124`/`1145:1009`, והכרטיס ב-`1318:1761`) עדיין קיימים — **לא לשחזר בסנכרון.** `nir-giorgio-levin-medina` (imageRef `99781a55…`, נוסף כשהופיע במשבצת 8.9/המדינה) הוא אירוע אחר, היום ב-30.9.2026.
- **`pinned` של michael-konovalenko ו-livay-levi הוסר (2026-09-01)** — המעצבת הורידה אותם מפריים הרשימה; הם ב-`/press/`. לא להחזיר את הדגל.
- **artist-talk:** hero מובייל נפרד וטריפטיך 6 התמונות (קליגרפיה של ktuba) — הוחלפו בחלון-ראווה יחיד + 4 סרטונים.
- **close-look:** שאר הרה-דיזיין של `1560:4367`/`1560:4254` — לא מומש בהכרעת משתמש.
