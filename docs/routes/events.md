# Events — route notes (רשימת `/events/` + עמודי אירוע שאינם artist-talk)

> **קרא לפני עריכה של:** `events/index.html`, `events/ktuba/`, `events/loneliness/`, `events/close-look/`, `events/artist-talk/`, `events/how-many/`, `events/gala-night/`, ועמודי וריאנט הרזידנסי SUMII: `events/niki-de-saint-phalle-day/`, `events/sumii-opening/`, `events/sumii-melani-hosting/`, `events/yom-kippur-wish-tree/`, `events/sumii-live-studio/`.
> עמודי משפחת ה-artist-talk (`events/<artist>/`, the-space-between, zohar-ron-medina, `nir-giorgio-levin-medina` וכו') → `docs/routes/events-talks.md`. הארכיון `/press/` → `docs/routes/press.md`.
> זה המצב הנוכחי + הכללים הפעילים. היסטוריה: `docs/history/CLAUDE-2026-09-27.md` §4.

## Pages

- `/events/` → `events/index.html` · desktop `XhGH...::1318:1728` (גריד הכרטיסים `1318:1761`) · mobile `XhGH...::1732:140` (מחליף את `1318:2012` מ-2026-09-01) · ✅
- `/events/ktuba/` → `events/ktuba/index.html` · desktop `XhGH...::119:1651` (canonical; legacy `Zn3N...::1213:1644`) · mobile `XhGH...::119:1509` (legacy `Zn3N...::1213:1502`) · ✅
- `/events/loneliness/` → `events/loneliness/index.html` · desktop `Zn3N...::1213:1873` · mobile `Zn3N...::1213:2099` · ✅
- `/events/close-look/` → `events/close-look/index.html` · desktop `XhGH...::420:1520` · mobile `XhGH...::420:1625` · ✅
- `/events/artist-talk/` → `events/artist-talk/index.html` · desktop `XhGH...::818:159` · mobile `XhGH...::818:17` · ✅
- `/events/how-many/` → `events/how-many/index.html` · desktop `XhGH...::433:2` · mobile `XhGH...::433:179` · ✅
- `/events/gala-night/` → `events/gala-night/index.html` · desktop `XhGH...::1451:1901` · mobile `XhGH...::1451:2070` · ✅
- `/events/niki-de-saint-phalle-day/` → `events/niki-de-saint-phalle-day/index.html` · desktop `XhGH...::1854:2172` · mobile `XhGH...::1854:2033` · ✅ (**עמוד הבסיס** של וריאנט הרזידנסי SUMII)
- `/events/sumii-opening/` → `events/sumii-opening/index.html` · desktop `XhGH...::1706:2032` · mobile `XhGH...::1706:1919` · ✅
- `/events/sumii-melani-hosting/` → `events/sumii-melani-hosting/index.html` · desktop `XhGH...::1811:270` · mobile `XhGH...::1811:128` · ✅
- `/events/yom-kippur-wish-tree/` → `events/yom-kippur-wish-tree/index.html` · desktop `XhGH...::1847:1614` · mobile `XhGH...::1847:1389` · ✅
- `/events/sumii-live-studio/` → `events/sumii-live-studio/index.html` · desktop `XhGH...::1854:2493` · mobile `XhGH...::1854:2353` · ✅
- ⚠️ שמות הפריימים של כל חמשת עמודי הווריאנט ("event- artist talk with שירה טורבוביץ") משקרים — אלה לא artist talks.

## Shared rules (כל עמודי האירוע)

- **כל העמודים סטטיים** — אין גנרטור, ו-`python3 tools/sync_data.py` **לא נוגע באף קובץ כאן**. כל עותק דאטה בעמודי האירוע הוא מירור ידני (ראה Mirror registry ב-`docs/data-contracts.md`): כשמשנים את `data/events.json` — מעדכנים גם את המירור בעמוד, ולהפך.
- **אירוע חדש (כל סוג, כולל artist-talk) — צ'קליסט:**
  1. רשומה ב-`data/events.json` (+`list_image` כשיש תמונת כרטיס ייעודית — לרוב `images/events/<slug>/list-card.webp` 876×487; ה-`img` במירור = אותו נתיב). אירוע רב-יומי: `date` = יום ההתחלה, `date_end` = היום האחרון, `date_label` = התווית verbatim של כרטיס ה-`/press/` (מידע בלבד — אף רנדרר לא קורא אותו).
  2. רשומה במירור `#events-list-data` ב-`events/index.html` (ראה למטה; רב-יומי — כולל `date_end`).
  3. כרטיס ב-`press/index.html` עם `data-kind="event" data-date="YYYY-MM-DD"` + תווית תאריך נראית `<span class="date">d.m.yyyy</span>` (רב-יומי: **גם** `data-date-end`, והתווית `<span class="date"><bdi dir="ltr">…</bdi></span>`) + לעדכן את ה-fallback הסטטי `grid-template-rows:var(--pc-rows,repeat(N,auto))` ל-N = `ceil(כל הכרטיסים ב-markup/2)` + רשומת `press.json` (כולל `date`, ורב-יומי גם `date_end`; `homepage_visible:false` אלא אם הוכרע אחרת) — פרטים ב-`docs/routes/press.md`.
  4. אם יש דף: `<title>` + meta description טובים (אינדקס החיפוש נבנה מהם ב-pre-commit); `sitemap.xml` באותו קומיט → `python3 tools/seo/refresh_sitemap_lastmod.py`; OG אפוי ביד `og/events-<slug>-hero.jpg`; בלוק `SEO:auto` מועתק מדף-אחות ונערך ביד — JSON-LD Event עם `startDate`/`endDate` ב-`+03:00` ו-`location` = ArtGallery של הגלריה (`galleries/<slug>/#gallery`), כמו בעמודי 2026-09-27.
  - 🔴 **לא להריץ `tools/seo/inject.py` על עמוד אירוע** (גם לא per-page): ענף ה-events בונה את הבלוק מחדש מ-`events.json` — `startDate` בלי שעה, `location` = `#org`, בלי `performer`, ו-og:image מ-`cover_image` דרך `tools/seo/og-dims.json` (בלי רשומה → ה-webp הגולמי). `og_gen.py` שבור.
- **בית אחד לכל אירוע:** `/events/` מציג אירוע כל עוד היום האחרון שלו (`date_end`, ואם אין — `date`) הוא היום או אחריו. הארכיון `/press/` עובר בזמן ריצה על `.pcard[data-kind="event"]` ומסיר: כרטיס שהיום האחרון שלו (`data-date-end`, ואם אין — `data-date`) הוא היום או אחריו; כרטיס עם `data-pinned`; וכרטיס בלי `data-date` תקין (= TBD, שייך ל-`/events/` — ולכן לעולם לא יגיע לארכיון). כרטיס בלי `data-kind` (כתבות) לא מסונן לעולם — כרטיס אירוע בלעדיו יופיע בשני העמודים. שני העמודים משווים מול `todayIL()` (תאריך ישראל, `Asia/Jerusalem`; אותו helper בשניהם), כך שמבקר מחו"ל רואה אותה רשימה ואירוע עובר ל-`/press/` לבד למחרת היום האחרון שלו. **שינוי בפילטר של עמוד אחד = אותו שינוי בשני** (אחרת אירוע רב-יומי נעלם משניהם או מופיע בשניהם). אימות: מטריצת רגעים × אזורי זמן עם שעון מוקפא + בקרה שלילית (`docs/lessons.md` 2026-09-27).
- **לייטבוקס על צילומי-אירוע** (`docs/components.md` §1.7 — הרחבה מאושרת לכל דפי events): על ה-`.tri` — `data-tri-lightbox="true"` + `data-artwork-gallery="<scope>"` (`cursor:zoom-in` ל-`.is-center` כבר מגיע מ-`components/triptych-gallery.css`); ברצועה/גריד (moments) — `data-artwork-gallery` על מיכל הרצועה (`.strip` / `.moments-row`) + `cursor:zoom-in` מקומי על ה-`img`; על כל תמונה — `data-artwork-title`; לטעון `components/artwork-lightbox.css` + `.js`. **חריגים מכוונים:** רצועת `the artworks` ב-close-look (שקופיות עטופות `<a>` לדף האומנית) ו-artist-talk (שקופיות `<video>`). ב-how-many הגלריה השנייה בלי לייטבוקס (מצב הקוד).
- **סדר שקופיות ב-`.tri`:** כשהפריים מצייר שלישייה מסוימת — שלוש שקופיות עוקבות ב-DOM + `data-tri-start` על האמצעית (0-indexed) (`docs/components.md` §4).
- `picture-upgrade.js` עוטף `<img>` ב-`<picture>` בזמן ריצה — מסגרת שממקדת `>img` צריכה `picture{display:contents}`. **אבל** בתוך flex/grid עם `gap` ה-`<source>`-ים שהוא מוסיף הופכים תחת `contents` לפריטים ברוחב 0 ומכפילים את ה-gap ⇒ שם `picture{display:block}` או `source{display:none}` (`docs/lessons.md` 2026-09-27).
- עמודת טקסט `flex:1` ליד תמונה/כרטיס ברוחב קבוע חייבת `min-width:0`. רמפת גודל פונט הולכת **רק** בתוך הטווח השבור (`@media (min-width:769px) and (max-width:1100px)` וכו׳, עם `min()` כך ש-1440 לא זז), ונגזרת מהמילה הארוכה (נמדדת, לא מנוחשת) (`docs/lessons.md` 2026-09-27).
- שינוי שנוגע בכמה עמודים (CSS/JS משותף, הפצה לאחי הווריאנט, דאטה) → harness הרגרסיה: `node tools/regress/snapshot.mjs --label before --only events/` → השינוי → `node tools/regress/snapshot.mjs --label after --only events/` → `node tools/regress/diff.mjs before after`. exit 0 = זהה; שינוי שאמור לשנות פלט יוצא exit 1 — לקרוא את ה-diff ולוודא שהשתנו רק העמודים/האלמנטים המכוונים. **אותם `--only`/`--widths` בשתי הריצות** (עמוד שקיים רק באחת נספר כהבדל); שינוי בפילטר/`todayIL()` → `--only events/,press/`. לעבודת layout/טיפוגרפיה: `--widths 390,1024,1366,1440` — ברירת המחדל (390,1440) לא רואה את רצועות 769–1100 / 1320–1439, שבהן יושבות הרמפות של העמודים כאן. הפלט ב-`$REGRESS_OUT` (ברירת מחדל `<os tmpdir>/zrp-regress/<label>`); עמוד חדש שעוד לא ב-git נכלל. בדיקה טיפוגרפית רק ב-http (ב-file:// הפונטים חסומים).
  - ⚠️ השעון מוקפא (`FIXED_NOW` ב-`snapshot.mjs` = `2026-09-27T12:00`, שעון מקומי; אין override דרך env) ⇒ `/events/` מצולם עם **שני כרטיסים בלבד** (nir-giorgio-levin-medina — יום אחד עם `widths`; sumii-live-studio — רב-יומי). שינוי בכרטיס שלא מיוצג שם (כותרת עברית, TBD, `soon`, `pinned`, רשימה ארוכה) לא נבדק. לשינוי כזה: לשנות זמנית את `FIXED_NOW` (למשל `2026-09-01T12:00:00` ⇒ 12 כרטיסים, כולל הכרטיס העברי ושלושת הרב-יומיים) — **אותו ערך בשתי הריצות** — ולהחזיר אחרי ה-diff; לא לקמט את השינוי, ולא להריץ במקביל לסשן אחר שמצלם baseline. (דריסת `Date` בקונסול לא עובדת — הרנדרר רץ פעם אחת בטעינה, ורענון מוחק את הדריסה.)
- ⚠️ `events.json :: <slug>.homepage_visible` מיושן, ואף קוד לא קורא אותו (`true` בכל ששת העמודים הוותיקים כאן, גם ב-ktuba/close-look/artist-talk שאינם בהומפייג'). גם `press.json` `homepage_visible` לא נקרא בקוד. מה שמרנדר את גריד `#press` בהומפייג' = **כרטיס HTML ידני ב-`index.html`** בלבד; `press.json` `homepage_visible` + `homepage.json :: press_section.item_ids` = רשומות דקלרטיביות שצריך לשמור עקביות מולו (ראה `docs/routes/press.md` / `docs/routes/homepage.md`).

## `/events/` — רשימת האירועים הקרובים

### מבנה
- Hero: רצועה אפורה `#EEF0EF` בדסקטופ (Figma `1318:1754`), לבנה במובייל (`1318:2033` — node מהפריים הישן `1318:2012`; בפריים הנוכחי `1732:140` לא אומת). כותרת מוערמת צמודה-ימין: "upcoming" (Bold) / "events" (Light). **כיול מדוד: 80 Figma → `60px`, `46px` ב-≤1100, 36 → `27px` במובייל** (הערת ה-CSS מזכירה 64 — הערך הנכון 60; אל "תתקן").
- גריד `.ev-list`: 2 עמודות, gap 48 (32 ב-≤1100); מובייל עמודה אחת, gap 24.
- כרטיס = `<a class="ev-card">` שורה: עמודת טקסט (משמאל) `space-between`, מיושרת לימין + תמונה (מימין). תמונה: דסקטופ `aspect-ratio:292/162.25`, מובייל קבוע `171×108`, `object-fit:cover`.
  - תג chip `#EEF0EF` padding 4/8, Copperplate Light 11.5: "gallery event" / שם הגלריה. **תמיד שתי שורות בשני ה-breakpoints, בלי pipe** (`.sep{display:none}`); `fitEventTags()` מקטין את הפונט 11.5→8px עד שנכנס, ושם גלריה ארוך (>20 תווים) נשבר (`.tag--wrap`).
  - שם הגלריה מגיע מטבלת `GALLERY` הקשיחה ברנדרר (`medina`→`kikar hamedina`, `dizengoff`→`dizengoff square`, `flea-market`→`flea market`). ⚠️ `berlin` קיים ב-`galleries.json` אבל לא בטבלה ⇒ אירוע בברלין יקבל תווית ריקה — להוסיף לטבלה קודם.
  - כותרת Copperplate 13px (כיול מ-16). כותרת עברית (`.ttl--he`, `dir=rtl`) = FbEzmel Regular px verbatim: 16 דסקטופ / 14 מובייל.
  - תאריך `d.m.yyyy` Copperplate Light 11.5px; אירוע רב-יומי — `<bdi dir="ltr">d.m.yyyy - d.m.yyyy</bdi>` (נבנה מ-`date`/`date_end`, **לא** מ-`date_label`); TBD — "פרטים ותאריך בהמשך" FbEzmel 14.
- מצב ריק: `#events-none` ("אין אירועים קרובים כרגע…") מוצג כשאף אירוע לא עבר את הפילטר — צפוי, לא באג.
- Inbound: `#events-upcoming` בהומפייג' → `events/`. אין פריט nav "events" — "press & events" → `press/` (מסומן פעיל גם ב-`/events/`).

### רינדור, סדר וסינון (JS בתוך העמוד)
- הכרטיסים מרונדרים מהמירור `<script type="application/json" id="events-list-data">` (file:// לא יכול fetch).
- `todayIL()` = התאריך של היום לפי `Asia/Jerusalem`: קודם Intl `formatToParts`, אחר כך `en-CA`, ובסוף התאריך המקומי של המבקר; כל תוצאה נבדקת ב-regex `YYYY-MM-DD`. אותו helper ב-`press/index.html` — לשנות בשניהם.
- פילטר: כרטיס נשאר אם הוא TBD (`date_tbd`, או `date` חסר/פגום) **או** `pinned` **או** היום האחרון שלו (`date_end` אם תקין ומאוחר מ-`date`, אחרת `date`) ≥ היום.
- מיון: לפי יום ההתחלה (`date`) עולה; באותו יום התחלה — מי שמסתיים קודם ראשון; ואז סדר המירור (יציב). TBD בסוף.
- **דסקטופ = זרימת עמודות RTL:** `grid-auto-flow:column; direction:rtl` על `.ev-list`, וה-JS קובע `--ev-rows = repeat(ceil(n/2),auto)` — הכרונולוגיה יורדת בעמודה הימנית ואז בשמאלית (אותו טריק כמו `/press/`). `repeat(3,auto)` הסטטי = fallback ללא-JS בלבד. מובייל: `grid-auto-flow:row; direction:ltr`, עמודה אחת באותו סדר עולה.
- כרטיס ראשון `fetchpriority="high"`, השאר lazy; אחרי הרינדור `PictureUpgrade.refresh(list)`.
- `soon:true` → `<a class="ev-card ev-card--soon" href="#" aria-disabled="true">` + טוסט "בקרוב" (1.8s), דפוס `/press/` — לאירוע שמוכרז לפני שיש לו דף (דורש `route:null`). **כרגע אף רשומה לא משתמשת בו** (הענף נשאר לעתיד). כשהאירוע מקבל דף — המפתח **נמחק** מ-`events.json` ומהמירור (לא `null`).
- `pinned:true` — הכרטיס שורד את פילטר התאריך (לאירוע שהמעצבת עדיין מציגה בפריים הרשימה אחרי תאריכו). **חייב סנכרון בשלושה מקומות:** `events.json` `pinned`, המירור, ו-`data-pinned="1"` על הכרטיס ב-`press/index.html` (כדי שיוסר מהארכיון). כשהאירוע יורד מהפריים — להסיר בשלושתם. **כרגע אף אירוע לא pinned**; האם להצמיד את niki ו-zohar-ron-medina — פתוח (ראה "מצב נוכחי").
- `date_tbd` — הענף נשאר ברנדרר; כרגע אין אירוע כזה.
- `widths[]` (אופציונלי) — לתמונת כרטיס שחוצה את כלל-זהב 12 (≥80KB וגם ≥800px): הרנדרר בונה `srcset` מ-`<name>-<w>w.webp` (הרוחב ששווה ל-`w` = הקובץ הראשי) + `sizes="(max-width:768px) 171px, 292px"`; חובה אחי AVIF לכל וריאנט. בלי השדה = src יחיד.

### המירור `#events-list-data` (ידני — לא ב-sync_data.py)
- **אירוע חדש = להוסיף ל-`data/events.json` וגם לכאן.** המירור מחזיק את **כל** האירועים, כולל אלה שעברו — לא למחוק רשומות עבר (הפילטר מסתיר אותן בזמן ריצה, ו-`pinned` תלוי בכך שהן קיימות); הוא משקף את `events.json` אחד-לאחד (היום 30 רשומות). סדר הרשומות במירור לא חייב להיות ממוין — הרנדרר ממיין. **חריג:** באירועים עם אותו יום התחלה ואותו יום אחרון המיון יציב, ולכן סדר הרשומות במירור קובע את סדר התצוגה — למקם לפי הפריים. שדות לכל פריט:
  - `slug` — שם התיקייה (ה-href הוא `<slug>/`, לא `route`).
  - `date` (`YYYY-MM-DD`), `gallery_id` (`medina` / `dizengoff` / `flea-market` — ראה טבלת `GALLERY` למעלה).
  - `title_en` = `list_title_en` מ-`events.json` אם קיים, אחרת `title_en` (למשל bar-cohen: בכרטיס "…bar cohen - ‘akra’", בדף בלי המקף). ⚠️ חריגים ישנים (אירועי עבר — לא לנרמל): close-look במירור = "close look — open meeting with tanya shin" (ב-JSON `title_en` = "how many partners have u had?"), gala-night = "gala night — the peeler" (ב-JSON "gala night"); loneliness/how-many ורוב האירועים של 2026-09-27 נבדלים רק ברישיות. הכלל חל על רשומות חדשות.
  - `title_he` = **רק** `list_title_he` מ-`events.json`. 🔴 אל תעתיק לכאן את `title_he` הרגיל של האירוע — כל `title_he` במירור מחליף את הכותרת האנגלית בכרטיס.
  - 🔴 **שמות המפתחות במירור ≠ `events.json`:** הכותרות נכתבות במירור תמיד תחת המפתחות `title_en` / `title_he` — **אסור** להשתמש כאן ב-`list_title_en` / `list_title_he` כשם מפתח. הרנדרר קורא רק `slug, date, date_end, date_tbd, pinned, soon, gallery_id, title_he, title_en, img, w, h, alt, widths`; כל מפתח אחר (כולל `date_label`) נבלע בשקט, והכרטיס מציג כותרת/תאריך שגויים בלי שום שגיאה.
  - `img` = `list_image` אם קיים; אחרת בחירה ידנית (לרוב ה-cover; gala-night = `card.webp`, the-space-between = `hero-480w.webp`). נתיב יחסי לשורש (הרנדרר מוסיף `../`). `w`/`h` אמיתיים. `alt` עברי "<תיאור> — <גלריה>" (נכתב ביד — אין שדה מקביל ב-`events.json`).
  - אופציונליים: `soon`, `pinned`, `date_tbd`, `widths`, `date_end` (היום האחרון של אירוע רב-יומי — הכרטיס נשאר עד היום הזה כולל). `date_label` נמצא רק ב-`events.json` (ובתווית ה-HTML של כרטיס `/press/`), לא במירור.
- ⚠️ `widths` של `nir-giorgio-levin-medina` קיים **רק במירור** — ברשומת `events.json` שלו השדה חסר, אף שחוזה הדאטה מתאר אותו כשדה של `events.json`. כשנוגעים ברשומה — להוסיף גם שם.

### תמונות כרטיס (`list_image` — קרופ רוחבי, לרוב 876×487, ב-`images/events/<slug>/`)
- `list-card-v2` (2026-08-19, מפריימי כרטיסי הרשימה): maria-artamonova / jessica-tabarovsky / hadas-tuval / bar-cohen = אותו צילום כמו ההירו, בחלון STRETCH+cropTransform של הפריים (נמתח בדיוק כמו בפיגמה). **michael-konovalenko חריג** (כרטיס הרשימה `1318:3216`): הכרטיס משתמש ביצירה אחרת (imageRef `63a698c7…`, קולאז׳ פורטרט על לבן, cover ממורכז) — **לא** בקולאז׳ כובע-הפרחים של ההירו. קבצי `list-card.*` הישנים נשארו בדיסק (כלל-זהב 8).
- alice-debellis / zohar-ron: `list-card.webp` = רינדורי-node אפויים מ-2026-08-04 (המקור מונה nodes `1318:3242/3216/3229` ל-alice/zohar/amnon — מיפוי לפי סדר, לא מאומת; amnon נמחק). ⚠️ המעצבת שכתבה את כרטיסי פריים הרשימה in-place — `1318:3216` הוא היום הכרטיס של **michael-konovalenko** (`events.json :: michael-konovalenko._list_image_note`). **לא לרנדר מחדש את ה-nodes האלה** כדי לחדש את כרטיסי alice/zohar — הקבצים הקיימים בדיסק הם המקור. anat-wegier ממחזרת את `card.webp` הקיים (קרופ זהה).
- zohar-ron-medina: `list-card.webp` 876×487 מ-imageRef `951e06ff…` (צילום הדג של זוהר); כרטיס הרשימה בפיגמה `1318:3218` דסקטופ / `1403:999` מובייל.
- sumii-opening: רינדור-node אפוי — בפיגמה ההירו של sumii ב-FIT/contain על `#FAFAFA`, לכן רינדור ולא קרופ מהמקור.
- nir-giorgio-levin-medina: הרינדור מ-2026-09-01 של ה-STRETCH+cropTransform של `1471:256` (+480/768 + `widths` — ה-webp 201KB, ליטוגרפיה מנוקדת שלא נדחסת). ⚠️ מעוות מעט, בניגוד לכלל "לא מעוותים צילום" — פתוח (`docs/todo.md`): קרופ cover לא-מעוות מ-`99781a55` (`list-card-v2`) = החלפת שדה אחד במירור, בכרטיס ב-`/press/` וב-`events.json::list_image`. **לא לרנדר מחדש את `1471:256`** — הוא היום הכרטיס של niki.
- niki-de-saint-phalle-day: `list-card` 876×487 = קרופ cover **מיושר-לתחתית** (שורות 846–1439 של המקור), **לא** רינדור ה-node: הכרטיס בפיגמה (`1471:256` דסקטופ / `1864:3072` מובייל) הוא STRETCH לא-אחיד, וצילומים לא מעוותים.
- sumii-melani-hosting / yom-kippur-wish-tree: `list-card.{webp,avif}` = קרופ 876×487 מה-imageRef (sumii-melani `0f6be5f4…` — קרמיקה+עוגה; yom-kippur `e8ec34f3…` — חלון הראווה של דיזינגוף, ממורכז על חלון ה-cropTransform של הפיגמה) + וריאנטי 480/768; `widths:[480,768,876]` ב-`events.json` **וגם** במירור.
- sumii-live-studio: `list-card.webp` 876×487 (28KB — בלי `widths`).
- תמונות הכרטיס של שאר עמודי ה-talk מתועדות ב-`docs/routes/events-talks.md`.

### מצב נוכחי מול הפיגמה (פריימי הרשימה `1318:1761` / `1732:140`)
- 🔴 **כלל סנכרון (בקשת משתמש 2026-08-19: "אותם אייטמים, אותו סדר"):** כל כרטיס בפריים הרשימה של המעצבת מופיע ב-`/events/` (חוץ ממה שנמחק בהכרעה — ראה Removed), והסדר **נגזר מהתאריכים** (המיון + זרימת העמודות) — לא מסדרים ידנית. פערים נסגרים דרך הדאטה: `pinned` = אירוע שעבר ועדיין בפריים; `soon`+`route:null` = אירוע בפריים בלי דף; תאריך שהשתנה בפיגמה = לעדכן: `date` + `date_he` ב-`events.json` (ורב-יומי גם `date_end`/`date_label`); המירור `#events-list-data`; בכרטיס ב-`press/index.html` **גם** `data-date` (ורב-יומי `data-date-end`) **וגם** תווית ה-`<span class="date">` הנראית; `date` (ורב-יומי `date_end`) ברשומת `press.json`; ואם יש דף — שורת המטא הנראית, ה-descriptions (meta/og/twitter) וה-JSON-LD `startDate`/`endDate` בעמוד האירוע; ובסיום `python3 tools/seo/refresh_sitemap_lastmod.py` (ה-sitemap לא מכיל תאריכי אירועים — רק `lastmod`). (לקח 2026-09-27: עדכון של `data-date` בלבד השאיר תווית ישנה בכרטיס.) **חריג:** אירוע חי שנוסף מחוץ לפריים הרשימה — נשאר ברשימה (תקדימים: the-space-between 2026-08-06; elsa-ars-brush 2026-08-23, נוסף לבקשת המשתמש — ראה `docs/routes/events-talks.md`; sumii-melani-hosting + yom-kippur-wish-tree, שמקורם בפריים המובייל של `/press/` `1323:528` — מקור כרטיסים לגיטימי); לשאול לפני הסרה.
- 🔴 **היום הכלל לא מיושם במלואו — שתי הכרעות משתמש פתוחות (`docs/todo.md`):** (1) פריימי הרשימה מציגים zohar-ron-medina 24.9, niki 25.9 ו-Live Studio — zohar ו-niki כבר עברו ולכן בארכיון `/press/` ולא ברשימה; **לא להוסיף `pinned` בלי הכרעת המשתמש.** (2) nir-giorgio-levin-medina (30.9) חסר בשני הפריימים אבל מוצג (הרשימה data-driven; תקדים elsa-ars-brush) — לא להסיר בלי הכרעה.
- הרשימה בפועל: ב-27.9.2026 בדיוק שני כרטיסים — nir-giorgio-levin-medina (30.9.2026) ו-sumii-live-studio (`30.9.2026 - 2.10.2026`; אותו יום התחלה, מסתיים מאוחר יותר ⇒ שני: דסקטופ nir בעמודה הימנית / live-studio בשמאלית, מובייל nir ראשון). מ-1.10 נשאר רק live-studio; מ-3.10 מוצג המצב הריק.
- 🔴 **תאריכים שהוזזו — לא להחזיר:** zohar-ron-medina 9.9 → **24.9.2026** (הפיגמה עודכנה); nir-giorgio-levin-medina 8.9 → 17.9 → **30.9.2026** (הכרעת משתמש 2026-09-27, לפי פריימי הדף). כרטיס הארכיון בפיגמה `1864:3054` (בתוך `1323:528`) שמציג 17.9 **מיושן — לא לסנכרן ממנו.**
- ⚠️ nodes שהמעצבת שכתבה/מחקה: `1471:256` (כרטיס הרשימה של nir מ-2026-09-01) = היום הכרטיס של niki; `1732:732` (כרטיס המובייל של nir) נמחק.
- ⚠️ הערות הקוד ב-`events/index.html` (הערת ה-CSS מעל `.ev-list` והערת ה-HTML מעל `#events-list`) עדיין מתארות את 8 הכרטיסים של 2026-09-01 (עם תוספת בסוף) — היסטוריה; המירור + המיון בזמן ריצה הם האמת.
- 🔴 ה-slug `nir-giorgio-levin-medina` לפי הגלריה — `nir-giorgio-levin` תפוס ע"י שיחת האמנים שלו ב-how-many/דיזינגוף (17.7.2026). תקדים `zohar-ron-medina`. העמוד עצמו → `docs/routes/events-talks.md`.

### הכרעות verbatim / טעויות פיגמה שלא משחזרים
- כרטיס the-space-between כתוב בפיגמה **בעברית** (`1318:3227` / `1455:2573`) → `list_title_he`: "מור צופיה געש | מה אנחנו באמת זוכרים ממקום?". בפיגמה "צופייה" — נשמר הכתיב הקנוני **"מור צופיה געש"**.
- בפריים הדסקטופ הכרטיס של hadas-tuval (28.8) נושא בטעות את הכיתוב "artist talk with jessica tabarovsky"; המובייל כותב נכון — **האתר מציג hadas**.
- `date_label` של האירועים הרב-יומיים (ב-`events.json` בלבד; שום קוד לא קורא אותו) — `8.9.2026 - 11.9.2026` (sumii-melani-hosting), `30.9.2026 - 2.10.2026` (sumii-live-studio), ו-yom-kippur-wish-tree עדיין `17.09.26 - 18.09.26`. ⚠️ הנוסח של yom-kippur כבר לא תואם את כרטיס `/press/`, שאוחד ב-2026-09-27 ל-`17.9.2026 - 18.9.2026`. הפורמט הנוכחי לכל תוויות הטווח = `d.m.yyyy - d.m.yyyy` (כמו שהכרטיס ב-`/events/` בונה מ-`date`/`date_end`); ליישר את yom-kippur כשנוגעים ברשומה. (תאריך הלוקאפ **בתוך** עמוד yom-kippur — `.ev-lockup-date` `17.09.26 - 18.09.26` — נשאר verbatim מהפיגמה: זה עיצוב העמוד, לא תווית הכרטיס.)

### פתוח (⚠️ חלק מהפריטים עדיין לא רשומים ב-`docs/todo.md`)
- הכרעות המשתמש על הרשימה (להצמיד את zohar-ron-medina/niki? להשאיר את nir?) + כרטיס הרשימה המעוות של nir — `docs/todo.md`.
- ⚠️ במירור `#events-list-data` ל-`liel-salman` רשום `h:1749`, בעוד `images/events/liel-salman/hero.webp` בפועל 984×1312 (מאז החלפת ההירו 2026-07-15) — לתקן ל-`h:1312` (כלל-זהב 12: `width`/`height` אמיתיים; שאר הרשומות תואמות לקבצים). מתועד גם ב-`docs/routes/events-talks.md`. (לא ב-todo.)
- JSON-LD של ששת העמודים הוותיקים כאן (ktuba, loneliness, close-look, artist-talk, how-many, gala-night) — בלי `+03:00` ורובם בלי `endDate`, `location` = `#org`. לתקן ביד בדפוס עמודי 2026-09-27, **לא** דרך `inject.py` (`docs/todo.md`).

## `/events/ktuba/` — מיצג חי (zohar ron, loneliness)

- גוף ה-hero = שיר הכתובה + התיאור **בניקוד, verbatim** (= `events.json :: ktuba.poem_he` + `description_he`; לשנות בשניהם).
- סליידשואו `.tri`: 3 צילומים (סדר DOM `slide-02, slide-03, slide-01`) עם **7 dots** (3 אמיתיים + 4 שמורים per Figma — חריג ידוע לכלל "לא יותר dots מ-slides"). לייטבוקס: `data-tri-lightbox="true"`, scope `event-slideshow`, title "live art performance".
- רצועת אומנים (11) מרונדרת ב-JS **רק** מהמירור `#fallback-ktuba-artists` (אין fetch) = מירור ידני של `events.json :: ktuba.artists` — הנתיבים במירור עם קידומת `../../`. לעדכן את שניהם. מפת `_ARTIST_FOCAL` בעמוד = העתק ידני של `FOCAL_POINTS` מדפי האומנים.
- איות אנגלי קנוני (הכרעת משתמש): "adi duek", "zohar shitrit" — ה-slugs נשארים `adi-duak`, `zohar-shtrit` (כלל-זהב 6).
- כרטיס: רק ב-`/press/` (`press.json :: event-loneliness-3`, `homepage_visible:false`).
- 🔴 טאבלט (2026-09-27): `.event-hero .text-col{min-width:0}` + רמפת `.h-title` לפי המילה הארוכה PERFORMANCE (8.96em) — 769–1100: `max(18px,min(48px,calc((100vw - 608px) / 8.96)))`; 1101–1439.98: `min(64px,calc((100vw - 816px) / 8.96))`, `line-height:1.1875` (ב-1440 ה-64px הבסיסי לא זז). בלעדיהם עמודת התמונה נדחפת מחוץ למסך ב-769–1180. לא להסיר. ראה `docs/lessons.md` 2026-09-27.

## `/events/loneliness/` — אירוע הפתיחה של בדידות

- הטקסט האוצרותי המלא ב-HTML (`events.json` = תקציר). בר share + bookmark (`data-item-id="event-loneliness"`) — היחיד במשפחה הזו.
- סקשנים: invitation tri (6: `invite-01,02,04,05,06,03`; scope `event-invitation`, title "the invitation") → `the atmosphere` (וידאו `images/events/loneliness/reel.mp4` עם poster `atmosphere.webp` וכפתור play + רשימת "אומנים מציגים:" מקושרת) → גלריה שנייה tri (3 `second-*`; scope `event-gallery-2`, title "the atmosphere") → moments grid (14 `opening-*`; scope `event-moments`, title "moments from the opening").
- 🔴 הכותרת הרשמית **"בדידות בתוך סביבה תוססת"**. אם בפיגמה עדיין "בתוך בסביבה" — טעות מוכרעת, לא לשחזר.
- העמוד סטטי, בלי מירור דאטה (ה-`#fallback-*` שייכים ל-`exhibitions/loneliness/`, לא לכאן). כרטיס בהומפייג' `#press` + `/press/` (`event-loneliness-4`).
- 🔴 **תמונות משותפות עם עמוד התערוכה:** `images/events/loneliness/invite-01..03`, `atmosphere` ו-`second-01..03` הם גם גלריית ה-hero של `exhibitions/loneliness/` (`data/exhibitions.json :: loneliness.gallery_images[]` + המירור `#fallback-exhibitions` בעמוד התערוכה). החלפה / קרופ מחדש / שינוי שם של אחת מהן משנה גם את עמוד התערוכה — לבדוק את שניהם (harness `--only events/loneliness/,exhibitions/loneliness/`), ולעדכן את שלוש הרשימות אם הנתיב משתנה. ראה `docs/routes/exhibitions.md`.
- 🔴 טאבלט 769–1100 (2026-09-27, אותה רמפת כרטיס כמו how-many): `--pad-x:48px`, `.event-hero .text{min-width:0}`, כרטיס `flex-basis:380px` / frame 380×575, `.h-eyebrow` `min(80px,calc((100vw - 576px) / 3.02))`, `.gallery` 22px, `.when` `clamp(16px,calc((100vw - 576px) / 11.86),22px)`, banner: bar 18.5px (gap 10) / he 23px / en 9.3px. בלעדיה הכרטיס (492) ושורת התאריך (`nowrap`) דוחפים את ה-hero מחוץ למסך. לא להסיר. ראה `docs/lessons.md` 2026-09-27.

## `/events/close-look/` — מבט מקרוב (tanya shin, how-many)

- h1 עברי "מבט מקרוב" FbEzmel **80/72 verbatim** (56 ב-≤1100, 24 מובייל). גוף = מירור של `events.json :: close-look.description_he` (טניה שין מקושרת). ⚠️ "how many partners have **u** had?" — כך בדאטה וב-HTML; unverified אם מכוון — לא לשנות בלי לשאול.
- `the artworks` — `.tri` של 9 יצירות של טניה שין (מרכז contain על רקע בהיר, peeks cover); **כל שקופית עטופה `<a>` → `artists/tanya-shin/` — בלי לייטבוקס, בכוונה.** רצועת `artists`: tanya shin (`images/artists/tanya-shin/portrait-v2.webp`), חץ → `exhibitions/how-many/`.
  - דאטה: שקופיות `the artworks` = מירור סטטי של `events.json :: close-look.gallery_images[]` (אותו סדר: `slide-01`, `tanya-shin/work-01`, `work-02`, `slide-02..07`); רצועת `artists` = מירור של `events.json :: close-look.artists[]` — לסנכרן את שניהם ידנית.
- **`.event-moments`** (2026-08-18) — בתחתית העמוד, אחרי רצועת האומנים: `.tri` עם **11 צילומים מהמפגש**, `images/events/close-look/moment-01..11.{webp,avif}` +480/768 (1125×2000; מקורות = imageRefs של nodes `1560:5046/5049/5052/5054..5060/5065`). מקור העיצוב: `1560:5014` דסקטופ / `1560:5030` מובייל.
  - גאומטריה: דסקטופ מרכז 481×841, peeks 302×528 ב-`.6`, gap 72 בפיגמה ⇒ peeks ב-`±463.5px`; ≤1100: 360×560 / 220×380 ב-`±326`; מובייל 216×378 / 117×204.75 ב-`±194.5`. כל השקופיות `object-fit:cover` (צילומים, לא יצירות).
  - סדר: השלישייה של הפיגמה קודם — `moment-01` peek שמאלי, `moment-02` מרכז (`data-tri-start="1"`), `moment-03` peek ימני.
  - דוטים מוסתרים ≤768 (אין בפריים המובייל — swipe בלבד).
  - לייטבוקס: `data-tri-lightbox="true"` + `data-artwork-gallery="event-moments"` + `data-artwork-title="moments from the meeting"` על כל שקופית.
  - דאטה: `events.json :: close-look.event_photos[]` (+`figma_node_photos_desktop/mobile`) — **מירור סטטי ב-HTML, לסנכרן את שניהם ידנית.**
- סדר מובייל (`display:contents`+`order`): תמונת hero → כותרת+מטא → artworks → גוף → artists → moments.
- 🔴 **הכרעות משתמש (2026-08-18):** מפריים הרה-דיזיין המלא של העמוד (`1560:4367` דסקטופ / `1560:4254` מובייל, "artist talk with tanya shin"; שם ה-node "בר כהן" משקר) **מומשה רק הגלריה**. שאר הרה-דיזיין (כותרת אנגלית, פאנל אפור במשפחת artist-talk) לא בוצע — לא לממש בלי בקשה. בפיגמה הגלריה מעל רצועת האומנים; באתר בתחתית (בקשת המשתמש).
- כרטיס: רק ב-`/press/` (`event-how-many-close-look-1`).

## `/events/artist-talk/` — gal pollak + elsa ers brosh (how-many, 11.6.2026, כיכר המדינה)

- מבוסס על תבנית close-look, אבל **כותרת באנגלית** (Copperplate UPPER, שני השמות מקושרים): 28px, 48px ב-≥1320, 22px ב-≤920, מובייל 20px. גוף אנגלי = מירור של `events.json :: artist-talk.description_he`.
- Hero: **תמונה אחת בשני ה-breakpoints** — חלון הראווה `images/events/artist-talk/hero-desktop.webp` (+480/768; imageRef `6fb63f12…`), scrim שטוח `rgba(27,27,27,.32)`, אוברליי "artist talk" + "how many partners have you had?". (הערת ה-HTML מעל הכרטיס — "desktop storefront / mobile live-art portrait" — מיושנת; אין hero מובייל נפרד.)
- גלריה: `.tri` של **4 סרטונים** `images/events/artist-talk/clip-01..04.mp4` + poster `clip-0N-poster.webp` (אין אח avif בדיסק, למרות ש-`_image_note` ב-`events.json` אומר webp+avif). ה-mp4 נטען (`data-src`) רק כשהשקופית במרכז, ורק המרכזית מתנגנת. דאטה: `events.json :: artist-talk.gallery_videos[]` — מירור סטטי ב-HTML. **בלי לייטבוקס — בכוונה** (שקופיות וידאו).
- רצועת אומנים: gal-polk (`images/artists/gal-polk/portrait-v2.webp`) + elsa-ars-brush (`images/artists/elsa-ars-brush/portrait.webp`), חץ → `exhibitions/how-many/` (מירור סטטי של `events.json :: artist-talk.artists[]`).
- 🔴 **הוסר — לא לשחזר:** hero מובייל נפרד (מיצג קליגרפיה חיה, `97bfe6a2…`) וטריפטיך 6 התמונות — תמונות הקליגרפיה (`97bfe6a2`/`2ae67900`/`a9cb03d4`) שייכות למיצג החי של זוהר רון (ktuba), לא לאירוע הזה.
- כרטיס: רק ב-`/press/` (`event-how-many-artist-talk`, `homepage_visible:false`) — כבר לא בגריד `#press` של ההומפייג'.

## `/events/how-many/` — אירוע הפתיחה של how-many (26.5.2026, דיזינגוף)

- התבנית של "אירוע פתיחה" (gala-night נבנה עליה). h1 עברי "אירוע הפתיחה" (FbEzmel 64/58); **הטקסט האוצרותי המלא ב-HTML** (`events.json` = תקציר). תמונת hero `images/events/event-how-many-2026-05-26-cover.webp` — **משותפת עם כרטיס ההומפייג'**.
- סקשנים: invitation tri (6; scope `event-invitation`, title "the invitation") → `the atmosphere` (תמונה + "אומנים מציגים:" מקושרים) → גלריה שנייה tri (5 `second-*`, Figma `433:87`, **בלי לייטבוקס**) → moments strip (14 thumbs, Figma `433:96`; scope `event-moments`, title "moments from the opening", `cursor:zoom-in`; חץ הכותרת → `exhibitions/how-many/`; חיצי scroll-cue במובייל). תמונות ב-`images/events/how-many/`.
- גאומטריית ה-`.event-tri`: מרכז 481×841, peeks 302×528 ב-`.6` ב-`-473px`/`+472.5px`; ≤1100 360×560 / 220×380 ב-`±326`; מובייל 216×378 / 117×204.75 ב-`±194.5`; dots פסים `#EEF0EF` / פעיל `#515151`.
- כרטיס בגריד `#press` בהומפייג' + `/press/` (`event-how-many-2026-05-26`).

## `/events/gala-night/` — ערב הגאלה של הקולפן (29.7.2026, כיכר המדינה)

- **תבנית אירוע-פתיחה (בסיס `events/how-many/`), לא משפחת ה-artist-talk.** אין פס presented ואין רצועת artist-cards (`events.json` `artists:[]`).
- **סדר דסקטופ = סדר ה-DOM (אין `order` מעל 768):** hero band → גלריה 1 (`.event-gal-a`) → סקשן אומנים (`.event-atmosphere`) → גלריה 2 (`.event-gal-b`) → moments. במובייל גלריה 2 **לפני** האומנים (ראה "סדר מובייל" למטה). לא לסדר מחדש את ה-DOM כדי ליישר ביניהם.
- Hero band אפור:
  - כותרת Copperplate "gala night": 80 Figma → **64/58**, `letter-spacing:.1em`, `padding-top:.2em` (שומר על ראשי האותיות מחיתוך); 44px ב-≤1100; מובייל 24 → **18px**; ≤400px 17px.
  - מטא: גלריה Regular / תאריך·שעה Light, 28px (22 ב-≤1100, 14 מובייל); נקודה 1×1 per Figma. **השעה `19:30-21:30` verbatim — התחלה-סיום, הפוך משאר המשפחה. לא "לתקן".**
  - **מכתב האוצרת המלא ב-HTML** (`events.json` = תקציר בלבד): FbEzmel Light 18/20 ממורכז (16 מובייל). "Welcome aboard." = `.lat` 18 Figma → 14px (13 מובייל). "הקולפן" הראשון → `exhibitions/the-peeler/`; שורת החתימה (Regular) "אוצרת התערוכה - קורין אברהם" → `curators/korin-avraham/`. שבירות `.dbr` = דסקטופ בלבד.
  - תמונה: פוסטר ההזמנה `images/events/gala-night/hero.webp` 984×1488 +480/768 (imageRef `93313e4b…`), **זהה בשני ה-breakpoints, בלי scrim/אוברליי**; 492×744 דסקטופ, 380×580 ב-≤1100, מובייל full-bleed 390×520. ה-fill השני בפריים המובייל = leftover מוסתר — לא להשתמש.
- **שתי גלריות טריפטיך** `.event-tri` (`gallery1-01..03`, `gallery2-01..03`; 3 שקופיות ו-3 dots-פסים 32×2 כל אחת), **גאומטריית how-many בדיוק** (ראה שם). לייטבוקס: `data-tri-lightbox="true"`, scopes `event-gallery-1` / `event-gallery-2`, title "gala night".
- **סקשן אומנים** `.event-atmosphere`: `atmosphere.webp` (imageRef `b8f85e72…`, מקור לרוחב בקרופ מרכזי 984×1488; שכבות ה-SVG/לבן בפריים לא נראות — לא לשחזר) + רשימת **22 אומנים מקושרים** FbEzmel Light 28/32 ממורכז (max-width 590; 22px ב-≤1100; מובייל 16/20 מתחת לתמונה ברוחב מלא 638h), NNBSP סביב ה-pipes, שבירות שונות לכל breakpoint דרך `.dsep`/`.msep` + `.dbr`/`.mbr`.
  - תיקונים מוכרעים מול הפיגמה (לא להחזיר): נוסף pipe חסר בין מיכאל קונובלנקו לאהרן בס; "אליצ׳ה דבליס" → **"אליס דה בליס"**; "טלי צלניק" → **"טלי זלניק - סטודיו פיס אוף מיין"** (כך מוצג, כולל שם הסטודיו — לא לקצר).
- **רצועת moments** ("moments from the opening"): **13 צילומים** `images/events/gala-night/moment-01..13-v2.{webp,avif}` (Figma `1452:2286…2273`). תאים 178×148 דסקטופ (gap 6) / 100.25×121.52 מובייל (gap 4), `object-fit:cover; object-position:50% 0`, גלילה אופקית עם snap; חיצי scroll-cue במובייל (Figma `1451:2186`); הכותרת "moments from the opening": 28px Light דסקטופ; מובייל Figma 24 → 19px אופטי (Regular, ls .02em); חץ הכותרת → `exhibitions/the-peeler/`. לייטבוקס `data-artwork-gallery="event-moments"`, title "moments from the opening", `cursor:zoom-in`. (14 רינדורי-ה-node הקודמים `moment-01..14.webp` 534² נשארו בדיסק לא-מקושרים — כלל-זהב 8.) ⚠️ `events.json :: gala-night._note` עדיין אומר 14 תאי moments — מיושן; ב-HTML 13 (`-v2`).
- סדר מובייל (`display:contents`+`order`): hero → כותרת → מטא → גלריה 1 → מכתב → גלריה 2 → אומנים → moments.
- Header דסקטופ לבן בעמוד הזה: `body.page-event-gala-night site-header .nav{background:#fff}` (≥769).
- התאריך עבר → הכרטיס נושר מ-`/events/` אוטומטית; קיים ב-`/press/` ובגריד `#press` בהומפייג' (`event-gala-night`, Figma `1323:570`; תמונת כרטיס `images/events/gala-night/card.webp` 584×369). OG `og/events-gala-night-hero.jpg`.

## וריאנט אירועי רזידנסי SUMII — Shared rules

- **העמודים:** `niki-de-saint-phalle-day` (**עמוד הבסיס**), `sumii-opening`, `sumii-melani-hosting`, `yom-kippur-wish-tree`, `sumii-live-studio` — אירועים של ה-POP UP ART RESIDENCY של SUMII (שירה טורבוביץ; `sponsors/sumii/`) בגלריית כיכר דיזינגוף, **בלי תערוכה** (`exhibition_id:null`).
- **מעטפת artist-talk** (בסיס `events/livay-levi/`): פאנל `#EEF0EF`, עמודת טקסט + כרטיס תמונה 492×744 (טאבלט 769–1319: עד 400×640), רצועת אומנים; מובייל `display:contents`+`order` (hero ראשון, כל בלוק על לבן). **בלי** `.h-body`/`.h-presented`/Solway/moments (חוץ מ-sumii-opening). **אח חדש = להעתיק מעמוד הבסיס verbatim ואז למדוד מחדש** מול הפיגמה; תיקון ב-shell של משפחת ה-artist-talk → לבדוק גם כאן (ולהפך).
- **בלוקים לשימוש חוזר:**
  - `.sumii-lockup` — שם הגלריה (`the art gallery by / erez zielinski rozen`, Copperplate Light ls .13em → הומפייג') → `.ev-lockup-logos` → `.ev-lockup-body`.
  - `.ev-lockup-logos` = **שורה** (gap 33) של `.ev-lockup-item` — לוגו מעל שם מקושר (gap 6.58 / 5 מובייל). שותף שני (מלאני) = `.ev-lockup-item` שני: מיחזור `images/sponsors/melani/logo.webp` (רסטר שקוף 450×258) → `artists/melani-hekimoglu/`.
  - `.ev-reg` — הערת הרשמה / כניסה חופשית (FbEzmel Light 16/20; האימייל `.lat` — `href` lowercase `mailto:`, תצוגה UPPERCASE).
  - `.ev-cobrand` — לוקאפ co-brand לבן על התמונה (שם הגלריה / X 28.8 verbatim / לוגואים), `aria-hidden`, בלי קישורים. לוגו מלאני לבן = `filter:brightness(0) invert(1)` על הרסטר.
  - אירוע רב-יומי = `.date` יחיד ב-`.h-meta .row-2`, **בלי נקודה ובלי שעה** (נקודת ה-1×1 בפריים הדסקטופ = leftover). שעות פתיחה = `.ev-schedule` אחרי הגוף (המיקום המדויק משתנה לפי עמוד).
- **שונה מהמשפחה — כל ערך נמדד מול הדיו בפיגמה ומתועד בהערות ה-CSS של העמוד (לקרוא לפני שינוי):**
  1. כותרת 64/72 (או 62/72), line-height **verbatim**, **בלי** ה-`padding-top:.2em` המשפחתי, `.dbr` לשבירות דסקטופ/טאבלט; בטאבלט (ובחלק מהעמודים גם ב-1320+) הגודל עוקב אחרי רוחב העמודה (`min()` / `cqi`), עם מרווח לפס-גלילה קלאסי (`100vw` כולל אותו).
  2. **כיול Copperplate לפי `textCase` של ה-node:** `UPPER` (caps מלאים) → px של הפיגמה **verbatim** (למשל שם הגלריה בלוקאפ); `LOWER` (small caps בפיגמה) → מקטינים (אוברליי 24→21, כתובת 16→14 בשני ה-breakpoints, כותרת מובייל 24→19).
  3. `.lat` בפסקה ובאימייל ב-**1em**, לא .88em.
  4. scrim = `linear-gradient(0deg, rgba(0,0,0,.5), transparent)` בשני ה-breakpoints (sumii-opening: בלי scrim).
  5. אוברליי `.ev-cobrand`: `top:51.4%` דסקטופ / `50%` מובייל (sumii-opening 51% / 50.2%; sumii-melani-hosting 53.3% / 50.2%; sumii-live-studio 53.3% / 50%).
  6. preload ל-woff2 (לא ל-.ttf/.otf של המשפחה).
- כתובת "1 Reines st." בכולם (בפיגמה Raines). הכתיב "שירה טורבוביץ" **בלי גרש**.
- **לוגו Sumii:** class `sumii-logo` (לא `logo` — מתנגש עם `.logo` הגלובלי של `site-chrome.css`); כל עמוד מחזיק עותק של `<symbol id="sumii-mark">` (currentColor; מ-`sponsors/sumii/` — ראה `docs/routes/sponsors.md` — Assets) + `<use>`. קישורים: לוגו Sumii → `sponsors/sumii/`; "שירה טורבוביץ" → `artists/shira-turbowicz/`.
- רצועת אומנים: shira-turbowicz (thumb = מיחזור `images/artists/grid/shira-turbowicz`); החץ ליד "artists" לא מקושר (אין תערוכה). `events.json :: <slug>.artists[]` משקף את הרצועה.
- **SEO ידני:** בלוק `SEO:auto` כתוב ביד — JSON-LD Event עם `startDate`/`endDate` ב-`+03:00`, `location` = ArtGallery `galleries/dizengoff/#gallery` (+PostalAddress), `eventStatus`/`eventAttendanceMode`, ו-`performer` איפה שהוגדר (לא ב-niki). 🔴 לא להריץ `inject.py` על העמודים האלה (ראה Shared rules למעלה): ל-`og-dims.json` יש רשומות ל-niki, sumii-melani-hosting, yom-kippur-wish-tree ו-sumii-live-studio (המפתח = `images/events/<slug>/hero.webp`), ו-cover של sumii-opening ממופה ל-OG של הספונסר (מפתח משותף — ראה בסקשן שלו). אח חדש = להעתיק את הבלוק מאח SUMII ולערוך.
- **חיווט (זהה לכולם):** `events.json` (`route`, `cover_image`, `list_image`, `figma_node_*`, `homepage_visible:false`) + מירור `#events-list-data`, כרטיס ב-`/press/`, `press.json` `event-<slug>` (`homepage_visible:false`), `sitemap.xml`, OG `og/events-<slug>-hero.jpg`. רב-יומי: `date_end` בשלושת הקבצים + `data-date-end` בכרטיס + `date_label` ב-`events.json`.

## `/events/niki-de-saint-phalle-day/` — day of niki de saint phalle (25.9.2026, עמוד הבסיס)

- **תוכן:** יום אחד של הרזידנסי — הגלריה נכנסת לעולמה של ניקי דה סן פאל, שנתנה את שמה ל-**NIKI**, הפסל הראשון בקולקציית FIGURES; 10:00–14:00, כניסה חופשית בהרשמה מראש.
- **מבנה:** כותרת `day of niki de<br class="dbr"> saint phalle` — **לא מקושרת** (ניקי אינה אומנית האתר) → מטא (גלריה; תאריך `·` שעה; `14:00-10:00` verbatim בלי `<bdi>`) → `.sumii-lockup` [שם הגלריה; `.ev-lockup-item` יחיד: לוגו Sumii מעל "שירה טורבוביץ"; פסקת FbEzmel Light 21/25.93 בתיבה 448.63 עם `.lat` NIKI / FIGURES / SUMII, ו-**NIKI → `works/shira-turbowicz-3/`**] → `.ev-reg` ("כניסה חופשית בהרשמה מראש בלבד" + `info@sumiiworld.com`) → כתובת Dizengoff Square / 1 Reines st.
- מובייל: hero → כותרת → מטא → לוקאפ → הרשמה → כתובת → אומנים.
- **כיולים:** כותרת 64/72 (עם 58 כל בלוק מתחת לכותרת ישב גבוה מהפריים); טאבלט 44/50, וב-769–1050 `min(34px, calc((100vw - 577px) / 8.6))` (ב-34 קבוע 4 שורות ב-769–849); מובייל 24→19. שם הגלריה בלוקאפ 21/22 דסקטופ, 16/17 מובייל — **verbatim** (Figma `textCase:UPPER`); אוברליי 24→21, לוגו 85.8×39.07; כתובת 16→14 בשני ה-breakpoints; `.lat` ב-1em (ב-.88em השורה "SUMII של FIGURES." יצאה קצרה).
- **hero:** imageRef `f27f37e5…` (פסל ה-Niki), מקור 1066×1600 לא-חתוך +480/768 — האספקט יושב בין שני חלונות הפיגמה ⇒ קובץ אחד ב-cover (תקדים elsa-ars-brush). **אינו** מיחזור של `shira-turbowicz-3` (אותו פסל, צילום אחר).
- `list-card` — ראה "תמונות כרטיס" (קרופ מיושר-לתחתית, לא רינדור ה-node).
- JSON-LD `2026-09-25T10:00:00+03:00` → `14:00:00+03:00`; OG 1200×1801.
- האירוע עבר ⇒ חי רק ב-`/press/`, והכרטיס שלו שם נושא כרגע את ה-`fetchpriority="high"` הסטטי (`docs/routes/press.md`). עדיין בפריים הרשימה של המעצבת — האם להצמיד פתוח (ראה "מצב נוכחי").

## `/events/sumii-opening/` — opening night event - ART RESIDENCY by sumii (2.9.2026)

- **תוכן:** ערב הפתיחה של ה-POP UP ART RESIDENCY של SUMII / שירה טורבוביץ, 18:00–21:00, בהרשמה מראש.
- **הבדלים מהבסיס:**
  1. **בלי scrim** בשני ה-breakpoints. ב-rect הדסקטופי רשום fill שטוח `.4`, אבל הרינדור לא צובע אותו — לא להוסיף.
  2. **הלוקאפ הוא GROUP אבסולוטי בפיגמה** (`1706:2456` / `1707:253`) ⇒ `gap:0` ו-`margin-top` לכל ילד לפי קואורדינטות ה-y (26.83 / 6.97 / 7.02 / 27.49 / 11.68 בדסקטופ; מובייל ÷1.2966). סדר: שם הגלריה → `hosting an art residency by` → לוגו Sumii 111.25×50.66 מעל שם האמנית → `scented with [Until Ten] by zielinski rozen` → הערת ההרשמה (**בתוך** הלוקאפ, לא בלוק אח). גדלי ה-Copperplate בלוקאפ **verbatim** (20.75 / 17.33 / 15.5; מובייל ו-769–1050 16 / 13.37 / 12) — בפיגמה הריצות האלה `textCase:UPPER`. במובייל הלוקאפ = קופסה קבועה 314 (padding 39 / 42.5).
  3. **כותרת 62/72** (כיול מול דיו ה-small caps). `by&nbsp;sumii` משחזר את השבירה של הפיגמה (4 שורות בדסקטופ / 2 במובייל). **"event - art" = `<span class="nw">` (nowrap)** — `&nbsp;` ליד מקף לא מונע שבירה אחרי המקף (UAX #14), וב-789–818 "ART" נשאר לבד. 1320+: `min(62px, 9.2cqi)` על `container-type` של עמודת הטקסט (תקדים jessica); טאבלט 44/50; 769–1050 34/38; ≤900 כותרת 28/32 ומטא 18, ושורות ה-host וה-scent נשברות (`.host` עם `text-wrap:balance`); מובייל 19px + `text-wrap:balance`. `.h-address` עם `text-wrap:balance`.
  4. **לוגו Until Ten** = SVG inline מ-`1706:2460` (3 paths, `currentColor`, `role="img" aria-label="Until Ten"`), **בלי קישור** (היעד לא ידוע — `docs/todo.md`). "by zielinski rozen" (בית הבשמים) **לא מקושר**.
  5. **רצועת `.event-moments`** (Figma `1815:650` / `1815:622`; הרצועה `1815:651` / `1815:623` = `figma_node_photos_*`), בין הפאנל לרצועת האומנים (מובייל `order:6`): גאומטריית livay-levi (מרכז 481×841, peeks 302×528 ב-`.6`), **peeks מוצמדים 151.5px מהקצוות** (`.is-prev{left:151.5px}` / `.is-next{left:calc(100% - 151.5px)}`, תקדים jessica); טאבלט 769–1319 בקנה .79 (380×665 / 239×417 ב-±373.5); מובייל 216×378 / 117×204.75 ב-±194.5 **ממורכז** (ההיסט של 16px בפיגמה = ארטיפקט flex-end), padding `8px 16px 24px`; **בלי דוטים ובלי חיצים**.
     - **10 צילומים** = ה-nodes הרופפים `1815:665–674` (single-fill, 1638×2048). השלישייה המצוירת ראשונה: moment-01 = `674` (peek שמאל, `a6784abf`), moment-02 = `673` (מרכז, `27f3c765`, `data-tri-start="1"`), moment-03 = `672` (peek ימין, `f74b8988`), ואחריהם 665→671; אף צילום לא הושמט.
     - master 1280×1600 +480/768/1080, `sizes="(max-width:768px) 303px, (max-width:1319px) 532px, 673px"` (cover של 4:5 בתוך 481×841).
     - לייטבוקס scope `event-moments`, title "moments from the opening night".
     - דאטה: `events.json :: sumii-opening.event_photos[]` — **מירור סטטי ב-HTML, לסנכרן את שניהם**.
  6. אוברליי `top:51%` / `50.2%`, לוגו 70.38×32.
- **hero = מיחזור `images/sponsors/sumii/hero.webp`** (1620×2160 +480/768/1080; גם `cover_image` ב-`events.json`), `sizes="(max-width:768px) 100vw, (max-width:1319px) 480px, 558px"` (cover של 3:4 בכרטיס 492×744 מרונדר ברוחב 558).
- קישורים: שם הגלריה → הומפייג', לוגו Sumii → `sponsors/sumii/`, "שירה טורבוביץ" → `artists/shira-turbowicz/`, `mailto:info@sumiiworld.com`.
- JSON-LD `2026-09-02T18:00:00+03:00` → `21:00:00+03:00`, performer שירה טורבוביץ. OG `og/events-sumii-opening-hero.jpg` 1200×1600 — ⚠️ **אין לו רשומה ב-`og-dims.json` ואי אפשר להוסיף** (המפתח = תמונת המקור, ו-`images/sponsors/sumii/hero.webp` כבר ממופה ל-`og/sponsors-sumii-hero.jpg`) ⇒ `inject.py` על הדף יחליף את ה-og:image (`docs/todo.md`).
- `list-card` = רינדור-node (ראה "תמונות כרטיס").

## `/events/sumii-melani-hosting/` — hosting event — sumii & melani hekimoglu (8–11.9.2026)

- **תוכן:** שולחן חג לקראת ראש השנה — פיסול, קרמיקה ופרחים; כניסה חופשית. כרטיס הרשימה בפיגמה: מובייל בלבד `1816:916` (בתוך פריים הארכיון `1323:528`).
- **הבדלים מהבסיס:**
  1. **מטא = טווח** `8 ספטמבר 2026 - 11 ספטמבר 2026`, בלי שעה ובלי נקודה (הנקודה `1811:311` = leftover).
  2. **שורת `hosting event 08.09-11.09`** (`.ev-lockup-host` / `.ev-hosting`, Copperplate Light 17.33 verbatim — בפיגמה UPPER; מובייל 13.37) מעל **שורת לוגואים כפולה**: Sumii + מלאני (79.61×45.7 / 60×35 → `artists/melani-hekimoglu/`), ומתחת לכל לוגו שם עברי מקושר (שירה טורבוביץ / מלאני הקימוגלו); פריטים ברוחב קבוע 115.83 / 126.36 (88 / 96 מובייל).
  3. **`.ev-schedule`** — בלוק שעות פתיחה (FbEzmel Light 16/20, שלוש `<p>` במרווח 20 = השורות הריקות של הפיגמה); בדסקטופ בלוק אח **אחרי** `.sumii-lockup` (`1812:154`), במובייל אחרי הלוקאפ (`order:5`). השעות **verbatim בסדר לוגי עם en-dash** (`10:00–14:00`) בתוך בלוק RTL, **בלי `<bdi>`** ⇒ מוצגות `14:00–10:00` בדיוק כמו בפריים. `Live Installation` = `.lat` 1em.
  4. `.ev-reg` = "הכניסה חופשית" בלבד.
  5. אוברליי ה-hero = שם הגלריה / X / Sumii לבן + **מלאני לבן** (113.26×66.2; בפיגמה trace וקטורי — כמעט זהה), `top:53.3%` / `50.2%`, הלוגו `loading=lazy`; באוברליי `picture{display:block}` (לא `contents`).
- **כותרת** `hosting event<br> sumii & <a>melani<br class="dbr"> hekimoglu</a>` — 3 שורות בדסקטופ, 64/72 ב-1440; מעל 769 **`min(64px, 10.7cqi)` על `container-type` של עמודת הטקסט** (בלי זה ב-1320–1379 "hosting event" נשבר לשתיים; תקדים jessica), טאבלט `min(44px, 10.7cqi)`, 769–1050 `min(34px, 10.7cqi)`; מובייל 19. "melani hekimoglu" בכותרת **מקושר**; "sumii" (מותג) **לא**.
- **hero:** imageRef `0f6be5f4…` **1279×1600 לא-חתוך** (+480/768/1080) — חלון הדסקטופ הוא תת-קבוצה של המובייל ⇒ cover משחזר את שניהם; scrim `.5`. leftovers בפיגמה: `13066b05…` + fill שטוח .4 — לא להשתמש.
- רצועת אומנים: shira-turbowicz + melani-hekimoglu (thumbs גריד; במובייל כרטיסים ברוחב 96 per Figma).
- JSON-LD `2026-09-08T10:00:00+03:00` → `2026-09-11T14:00:00+03:00`, performer שתיהן; OG 1200×1501.
- דאטה: `date_end:"2026-09-11"`, `date_label:"8.9.2026 - 11.9.2026"`; `time_start`/`time_end` = גבולות ה-JSON-LD, בלי `time_label` (השעות משתנות לפי יום).

## `/events/yom-kippur-wish-tree/` — Yom Kippur Event // wish tree (17–18.9.2026)

- **תוכן:** לקראת יום כיפור הגלריה מתמלאת בווידויים ומשאלות בהשראת "עץ המשאלות" של יוקו אונו; חמישי–שישי 10:00–14:00, כניסה חופשית. כרטיס הרשימה בפיגמה: מובייל בלבד `1864:3058` (בתוך `1323:528`).
- **הבדלים מהבסיס:**
  1. מטא = **טווח** `17 ספטמבר 2026 - 18 ספטמבר 2026` ב-`.date` יחיד (שני `<bdi>`), בלי נקודה ובלי שעה (הנקודה `1847:1655` = leftover); ב-769–1050 הטווח נשבר בין שני התאריכים.
  2. `.ev-lockup-when` = שורת התאריך `17.09.26 - 18.09.26` (`.ev-lockup-date`, `dir=ltr`, verbatim; Copperplate 17.33 verbatim, מובייל 13.37) + שורת הלוגואים כתת-עמודה אחת (הלוגו 6.97px מתחת לתאריך, 10px במובייל), כך שהמרווחים החיצוניים של הלוקאפ (22/21px) נשמרים.
  3. השעות **בתוך** `.ev-lockup-body`, verbatim ("חמישי–שישי: 10:00-14:00").
  4. `.ev-reg` = "הכניסה חופשית" בלבד (בלי אימייל).
- **כותרת** `yom kippur<br class="dbr"> event&nbsp;// wish<br class="dbr"> tree` — 62/72 (כיול-מדידה); ב-1320+ הגודל עוקב אחרי העמודה `min(62px, calc((100vw - 781px) / 8.9))` וב-769–1050 `min(34px, calc((100vw - 577px) / 8.9))` ("EVENT // WISH" = 8.9×font-size, עמיד לפס-גלילה קלאסי) — 3 שורות בכל 769–1920; מובייל 18px (ה-19 של niki היה נשבר) + `text-wrap:balance` ("YOM KIPPUR" / "EVENT // WISH TREE").
- כתובת `text-wrap:balance`; בטאבלט 769–794 balance על הגוף + nbsp ב"יוקו&nbsp;אונו".
- **hero:** בפיגמה crop `318b6c` (795×1060, 3:4) נמתח לכרטיס 492×744 (~13% עיוות אנכי) ⇒ נאפה **חלון-איחוד** 795×1202 (x33 y261 מהמקור 900×1600, אותו מרכז) +480. הדסקטופ מציג אותו שלם (אספקט מדויק), ו-cover במובייל חותך בדיוק לקרופ הפיגמה — קובץ אחד, בלי `<picture>`.
- ⚠️ התמונה (וכרטיס הרשימה, imageRef `e8ec34f3…`) = **חלון הראווה של דיזינגוף** ("HOSTING ART RESIDENCY BY SUMII") — verbatim מהפיגמה; לא "לתקן".
- רצועת אומנים = shira-turbowicz. `list-card` 876×487 +480/768 (`widths` — ה-webp 83KB).
- JSON-LD `2026-09-17T10:00:00+03:00` → `2026-09-18T14:00:00+03:00`.
- דאטה: `date_end:"2026-09-18"`, `date_label:"17.09.26 - 18.09.26"` (⚠️ נוסח ישן — כרטיס `/press/` אוחד ל-`17.9.2026 - 18.9.2026`; ראה למעלה).

## `/events/sumii-live-studio/` — Live Studio // Sumii (30.9–2.10.2026)

- **תוכן:** סטודיו חימר LIVE — שלושה ימים שבהם הגלריה הופכת למרחב של מחקר ופיסול חי בחימר, ו-SUMII מארחת את **מלאני הקימוגלו**; 10:00–14:00, כניסה חופשית בהרשמה מראש.
- **הבדלים מהבסיס:**
  1. כותרת = שם האירוע `live studio&nbsp;<span class="sl">/</span>/<br class="dbr"> sumii` — 64/72. nbsp לפני "//" (לא יישאר לבד בשורה); `.sl` מצמצם את ה-"//" (`letter-spacing:-.22em` — הלוכסן שלנו רחב מזה של הפיגמה). ב-1320+ `min(64px, calc((100vw - 781px) / 8.62))` וב-769–1050 `min(34px, calc((100vw - 577px) / 8.62))` (מרווח לפס-גלילה קלאסי); טאבלט 44/50; מובייל 19px.
  2. מטא = טווח `30 ספטמבר 2026 - 2 אוקטובר 2026` (`<bdi>` אחד), בלי נקודה ובלי שעה (נקודת הדסקטופ = leftover).
  3. **לוקאפ שני שותפים בשני ה-breakpoints:** Sumii משמאל ("שירה טורבוביץ" → `artists/shira-turbowicz/`) + לוגו מלאני מימין (→ `artists/melani-hekimoglu/`, "מלאני הקימוגלו"); פריטים 115.83 / 126.36 (88 / 96 ב-≤1050 ובמובייל).
  4. גוף רחב יותר (498) + **לו"ז תלת-יומי** `<p class="ev-schedule">` **בתוך** `.ev-lockup-body` (`30.09 | 10:00-14:00 | סטודיו חימר לייב סומי ומלאני קרמיקה` וכו' — שעות verbatim התחלה-סוף); "מלאני" מקושרת בגוף ובלו"ז.
  5. `.ev-reg` = "כניסה חופשית בהרשמה מראש בלבד" + `info@sumiiworld.com`.
  6. אוברליי ה-co-brand מוסיף את לוגו מלאני הלבן ליד Sumii, `top:53.3%` / `50%`, הלוגו `loading=lazy`; כאן `.ev-cobrand .ev-lockup-logos source{display:none}` (במקום ה-`picture{display:block}` של hosting).
- **QA (לא להסיר):** ב-769–907 שבירות ה-`.dbr` של הגוף מוסתרות (+ balance, ו-nbsp ב"תיראה&nbsp;בסופם."); לו"ז / הרשמה / תאריך מוקטנים עם העמודה ב-769–1050, ורווח הלוגואים מתכווץ (רצפה 8px) לפני שהוא גולש; במובייל <380 שורת הלו"ז הארוכה נשארת אחת; כתובת `text-wrap:balance`; אין גלישה ב-320–1920.
- **hero:** קובץ יחיד לא-חתוך 1086×1448 (+480/768) ב-cover, scrim `.5`.
- רצועת האומנים = shira-turbowicz בלבד (מלאני מקושרת בלוקאפ ובגוף; `artists[]` ב-`events.json` משקף את הרצועה).
- `list-card` 876×487 (28KB, בלי `widths`).
- JSON-LD `2026-09-30T10:00:00+03:00` → `2026-10-02T14:00:00+03:00`, performer שתיהן.
- דאטה: `date_end:"2026-10-02"`, `date_label:"30.9.2026 - 2.10.2026"`; מוצג ב-`/events/` עד 2.10 כולל, והכרטיס ב-`/press/` (`data-date-end`) מוסתר עד 3.10.

## Removed / do not restore

- **`events/amnon-lipkin/` נמחק (2026-08-28, בקשת משתמש)** — הדף, התמונות, ה-OG, והרשומות ב-`events.json`, במירור וב-sitemap. הפריימים בפיגמה (`1145:1124`/`1145:1009`, והכרטיס ב-`1318:1761`) עדיין קיימים — **לא לשחזר בסנכרון.** `nir-giorgio-levin-medina` (imageRef `99781a55…`, נוסף כשהופיע במשבצת 8.9/המדינה) הוא אירוע אחר, היום ב-30.9.2026.
- **`pinned` של michael-konovalenko ו-livay-levi הוסר (2026-09-01)** — המעצבת הורידה אותם מפריים הרשימה; הם ב-`/press/`. לא להחזיר את הדגל.
- **artist-talk:** hero מובייל נפרד וטריפטיך 6 התמונות (קליגרפיה של ktuba) — הוחלפו בחלון-ראווה יחיד + 4 סרטונים.
- **close-look:** שאר הרה-דיזיין של `1560:4367`/`1560:4254` — לא מומש בהכרעת משתמש.
