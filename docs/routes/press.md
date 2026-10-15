# Press — route notes

> קרא לפני עריכה של: `press/index.html`, `press/<article>/index.html`, `data/press.json` (וכל כרטיס עיתונות/אירוע בארכיון). מצב נוכחי + כללים פעילים. היסטוריה מלאה: `docs/history/CLAUDE-2026-09-27.md` §4.
> נקשר ל: `docs/routes/homepage.md` (גריד `#press` בהומפייג'), `docs/routes/events.md` (`/events/` — המשלים של הארכיון; ועמודי האירוע שאינם שיחות, כולל 5 אירועי רזידנסי SUMII), `docs/routes/events-talks.md` (עמודי שיחות-האמן שהכרטיסים מפנים אליהם).

## Pages

- כל כתבה: `press/<slug>/index.html`. `/press/` → `press/index.html` · desktop `XhGH...::1323:244` (⚠️ שם ה-node "press/events-phone" משקר — זה ה-1440) · mobile `XhGH...::1323:528` · ✅ ארכיון עיתונות + אירועי עבר. 🔴 **מקור הסדר = פריים המובייל `1323:528`** (35 כרטיסים; החריגים — "גריד וסדר"); פריים הדסקטופ `1323:244` **מיושן** ברשימת/סדר הכרטיסים (26 כרטיסים) — לא לסנכרן מולו (הפריסה הדו-עמודתית שלו עדיין תקפה).
- `/press/walla/` → `XhGH...::119:740` · `XhGH...::119:868` (legacy `Zn3N...::1213:737`/`1213:865`) · ✅
- `/press/press-1/` (פורטפוליו) → `XhGH...::119:972` · `XhGH...::119:1163` (legacy `Zn3N...::1213:968`/`1213:1159`) · ✅
- `/press/time-out/` (**הכתבה הישנה**, 31.12.25) → `XhGH...::119:1340` · `XhGH...::119:1433` · ✅
- `/press/the-last-station/` (time out — "התחנה האחרונה: 25 תערוכות", 27.5.26 — **הכתבה החדשה**) → `XhGH...::412:1118` · `XhGH...::412:1214` · ✅
- `/press/the-sixth-scent/` (ora magazine, **English long-form**) → `XhGH...::545:1669` · `XhGH...::545:1762` · ✅
- `/press/manicure-against-darkness/` (time out, 1.7.26) → `XhGH...::1051:291` · `XhGH...::1051:396` · ✅
- `/press/peeling-a-layer/` (רשת 13, 1.7.26) → `XhGH...::1051:26` · `XhGH...::1051:154` · ✅
- `/press/the-shared-list/` (פורטפוליו, 25.6.26) → `XhGH...::1537:2880` (⚠️ שם ה-frame "press-1-desktop" משקר — כתבה חדשה, זוהתה לפי רוחב 1440) · `XhGH...::1537:3091` ("press-1-mobile") · ✅ (2026-08-18)

## Data & sync — כל המשפחה

- 🔴 **שום דבר במשפחה הזו לא בבעלות `python3 tools/sync_data.py`.** כרטיסי `/press/` וכרטיסי `#press` בהומפייג' הם **HTML כתוב-ביד**; `data/press.json` ו-`data/homepage.json` הם מטא-דאטה דקלרטיבי שהדפים לא קוראים בזמן ריצה. שינוי = לערוך את `press.json` **וגם** את הכרטיס/ים ביד. (`tools/seo/inject.py` כן קורא את `press.json` — title/subtitle/cover/date/source → OG/JSON-LD.) כתבות long-form: הגוף נשאר ב-HTML, ב-`press.json` רק meta + cover.
- **מלכודות id ב-`press.json`:**
  - id `time-out` = הרשומה של **`press/the-last-station/`** (`exhibition_id:how-many`); id `time-out-final-countdown-2025` = הרשומה של **`press/time-out/`**.
  - 🔴 ה-matcher של `inject.py` (`route.endswith(slug)` **או** `id == slug`, הראשון במערך) משייך את `press/time-out/` לרשומת **the-last-station** — אסור לג'נרט את ה-SEO של `press/time-out/` עם `inject.py` (משחזר את באג 2026-07-09).
  - `portfolio-loneliness` = alias של `press-1` (`_alias:"press-1"`, **בלי מפתח `route`**, `homepage_visible:false`) — **לא ליצור לו כרטיס**.
  - `press-1.cover_image` עדיין מצביע ל-`00-home-card.webp` הישן (171px); הכרטיסים בפועל משתמשים ב-`00-home-card-v2`.
- **כרטיס בהומפייג' (`index.html #press`):** כל כתבות העיתונות + שני אירועי הפתיחה (how-many 26.5, loneliness 19.1) + חריגות משתמש (gala-night, hadas-tuval, livay-levi). כתבה חדשה ⇒ בדרך כלל גם כרטיס שם. כיום 13 כרטיסים ⇒ `repeat(7,auto)` (פרטי הגריד — `docs/routes/homepage.md`).
- **SEO:** `tools/seo/og_gen.py` שבור, ו-`tools/seo/inject.py` בלי ארגומנטים **מסרב לרוץ גורף** (הרצה גורפת מרגרסת ~90 דפים — `docs/todo.md`; לא לעקוף). OG לכתבה נאפה ידנית **מתמונת הכרטיס** (`cover_image` ב-`press.json`): `magick <cover_image> -resize '1200x1200>' -strip -quality 82 og/<name>.jpg` (`>` = לא להגדיל מקור קטן; הודעות הסירוב של הכלים מציגות `-resize 1200x` — לא להשתמש). מוסכמה: `og/press-<slug>-<image>.jpg` (הקיימים לא אחידים); בלוק `<!-- SEO:auto:start -->…<!-- SEO:auto:end -->` מועתק מכתבה אחות ונערך, כולל `og:image:width`/`og:image:height` לפי המידות האמיתיות. `tools/seo/og-dims.json` אופציונלי ורק `inject.py` קורא אותו (בלעדיו, או כשה-JPG שבו לא קיים — כמו peeling-a-layer — נופל ל-webp הגולמי). `inject.py <path>` על כתבות: אסור על `press/time-out/`, ובשאר רק עם בדיקת diff מלאה של בלוק ה-SEO.
- 🔴 **אחרי שכפול כתבה-תבנית — לעבור על כל תגי ה-head** (title, description, canonical, og:*, twitter:*, JSON-LD) מול ה-data של הדף (קרה: `press/time-out` נשא את ה-JSON-LD/og של the-last-station, lessons 2026-07-09). **וגם `[data-bookmark-toggle]` בגוף:** `data-item-id` = ה-id החדש ב-`press.json`, `data-item-title` = `<מקור> — <כותרת>`, `data-item-date` = ISO; id שנשאר מהתבנית ⇒ שמירת הכתבה החדשה מסמנת/מבטלת את הסימנייה של התבנית (`components/site-chrome.js`, localStorage `zr-bookmarks`).
- **חיפוש האתר** (CLAUDE.md כלל 10א): רשומת כתבה = ה-`<title>` + ה-`meta description` (נחתך ל-120 תווים); ה-JSON-LD `NewsArticle` נושא `headline` ולא `name`, ולכן לא תורם מילות חיפוש.
- **Sitemap (כלל-זהב 15):** `/press/` + 8 הכתבות. כתבה חדשה ⇒ `<url>` ב-`sitemap.xml` ליד רשומות `press/` + `python3 tools/seo/refresh_sitemap_lastmod.py`.
- שינוי רוחבי ⇒ harness רגרסיה (CLAUDE.md §7.1) עם `--only press/`. ⚠️ ה-harness מקפיא את השעון ב-2026-09-27 ⇒ כרטיס אירוע שהיום האחרון שלו 27.9 ואילך מוסר בשני הצילומים, והוספה/שינוי שלו נותנים diff exit 0 שלא מוכיח כלום — לבדוק בדפדפן.

## `/press/` — הארכיון (`press/index.html`)

### מבנה
- hero: דסקטופ פס אפור `#EEF0EF` (padding 48/112/40), מובייל **לבן** (32/16/8). כותרת מוערמת צמודה ימין — "press" (Copperplate Bold, `.hb`) / "& events" (Light, `.hl`). כיול: Figma 80 → **60px** דסקטופ / **46** טאבלט (≤1100) / **27** מובייל (≤768) — זהה ל-`events/index.html`.
- `section.cards#press-list` — כל הכרטיסים **סטטיים ב-HTML**, כרונולוגי **חדש→ישן** בסדר ה-DOM.
- nav גלובלי: "press & events" ב-`components/site-chrome.js` → `press/` (דרך `abs()`); מצב active `press` נדלק גם ב-`/press/` וגם ב-`/events/`.

### גריד וסדר
- דסקטופ: `grid-template-columns:repeat(2,…)` + `grid-auto-flow:column` + `direction:rtl` ⇒ המחצית הראשונה יורדת בעמודה **הימנית**, השאר בשמאלית (= פריסת ה-Figma). gap 48 (טאבלט 40/32). מובייל (≤768): flex עמודה אחת = סדר ה-DOM, gap 24.
- `grid-template-rows:var(--pc-rows, repeat(N,auto))`: `--pc-rows` מחושב ב-JS מהכרטיסים ששרדו את הפילטר; ה-`repeat(N,auto)` הסטטי הוא **fallback ללא-JS בלבד**. 🔴 **הוספת/הסרת כרטיס ⇒ לעדכן ל-`ceil(כל הכרטיסים ב-markup / 2)`**, אחרת בלי JS נוצרת עמודה שלישית. ב-markup כיום **39 כרטיסים** (31 אירוע + 8 עיתונות) ⇒ `repeat(20,auto)`; לספור מחדש: `grep -c '<a class="pcard' press/index.html`.
- 🔴 **`fetchpriority="high"` — שתי שכבות:** (1) **סטטית** על **הכרטיס הראשון ב-DOM ששורד את הפילטר היום**: כרטיס עיתונות (בלי `data-kind`) או אירוע שהיום האחרון שלו עבר — כיום niki-de-saint-phalle-day (25.9.2026); כרטיסים עתידיים מעליו `loading="lazy"`. כרטיס עיתונות חדש מעל המחזיק ⇒ ה-`fetchpriority` עובר אליו, ולמחזיק הקודם (niki — שאין לו היום `loading`) מוסיפים `loading="lazy"`. (2) **בזמן ריצה** ה-IIFE נותן לתמונת הכרטיס הראשון ששרד `fetchpriority="high"` + `loading="eager"` ומסיר מכל השאר ⇒ בדיוק אחד במסמך. בעריכת כרטיסים — ליישר את הסטטי לפי (1). כרטיסי `#press` בהומפייג' — כולם `loading="lazy"`.
- **מקום ב-DOM = תאריך ההתחלה (`data-date`)**, חדש→ישן — גם באירוע רב-יומי (sumii-melani-hosting 8–11.9 בין jessica-tabarovsky 10.9 ל-maria-artamonova 7.9; yom-kippur-wish-tree 17–18.9 מתחת ל-zohar-ron-medina 24.9). ראש ה-DOM כיום: sumii-live-studio, nir-giorgio-levin-medina, niki-de-saint-phalle-day, zohar-ron-medina, yom-kippur-wish-tree.
- **אותו תאריך ⇒ סדר הפריים הסמכותי** (`1323:528`): זוג 19.1.2026 — כתבת פורטפוליו (`press-1/`) **מעל** אירוע הפתיחה של בדידות (`events/loneliness/`). בהיעדר פריים: המאוחר בשעה למעלה (תקדים baruch-torgeman 18:30 מעל elsa-ars-brush 11:00, 6.9). זוג 30.9: sumii-live-studio (30.9–2.10) מעל nir-giorgio-levin-medina (30.9 בלבד) — עקבי עם `/events/` (בשוויון התחלה המסתיים קודם ראשון); ⚠️ לא הכרעת משתמש.
- **חריגים מפריים המובייל** (כפי שסונכרן 2026-09-27; לכל השאר — סדר הפריים): כרטיסים שאינם בפריים — משובצים כרונולוגית ו**נשארים**: sumii-live-studio (30.9–2.10), niki-de-saint-phalle-day (25.9), zohar-ron-medina (24.9), the-shared-list (25.6 — כתבה חיה עם עמוד ו-sitemap). 🔴 **לא למחוק כרטיס בסנכרון מול הפריים.** nir-giorgio-levin-medina — בפריים (`1864:3054`) עם 17.9; באתר **30.9.2026** (הכרעת משתמש 2026-09-27); כרטיס הפריים מיושן — **לא לסנכרן חזרה** (וגם לא ל-8.9 הישן).

### פילטר הארכיון (משלים ל-`/events/`)
- 🔴 **`/press/` = עבר בלבד** (בקשת משתמש 2026-08-12): כרטיס אירוע נמחק בזמן ריצה כל עוד **היום האחרון שלו** (`data-date-end`, ואם אין — `data-date`) הוא היום או אחריו; הוא חי ב-`/events/`. הפילטר הוא **המשלים המדויק** של `(date_end || date) >= today` ב-`events/index.html`; שניהם משווים מחרוזות `YYYY-MM-DD` מול **`todayIL()`** (`Asia/Jerusalem`, לא התאריך המקומי של המבקר; אותו helper בשני הדפים). לכל אירוע בית אחד בדיוק. 🔴 שינוי בלוגיקה של אחד הפילטרים ⇒ לשנות את שניהם.
- מימוש: IIFE על `.pcard[data-kind="event"]` מסיר כרטיס אם (א) יש לו `data-pinned`; (ב) אין לו `data-date` תקין (TBD); (ג) היום האחרון ≥ היום. **כרטיסי עיתונות בלי `data-kind` — לעולם לא מסוננים.** אחר כך מחשב `--pc-rows = repeat(ceil(נותרו/2),auto)` ומקדם את ה-LCP. 🔴 ה-IIFE **חייב לרוץ לפני** סקריפט הטוסט.
- 🔴 **כל אירוע ב-`events.json` = כרטיס אחד כאן** (+ tal-nehoray, שאין לו רשומה שם) — אירוע בלי כרטיס נעלם מכל הרשימות ביום שאחרי שעבר. אירוע חדש (כולל רזידנסי SUMII) מקבל כרטיס כאן כבר ביום שנבנה; כרטיסים עתידיים **נשארים ב-markup וב-`press.json`**, רק מוסתרים.
- **`data-pinned="1"`** ⇒ הכרטיס נמחק כאן תמיד (מספיק `data-kind="event"`). תואם ל-`pinned:true` ב-`/events/` (אירוע שהמעצבת עדיין מציגה בפריים הרשימה שלה אחרי שעבר). 🔴 **שלושה מקומות לסנכרן:** `data/events.json`, המירור `#events-list-data` ב-`events/index.html`, `data-pinned` בכרטיס כאן. כיום **אף כרטיס לא pinned**; המנגנון נשאר בקוד.
- 🔴 **אירוע TBD** (`date_tbd:true`, או `date` חסר/פגום) — `/events/` מחזיק אותו תמיד. הכרטיס שלו כאן **בלי `data-date`** — **לעולם לא `data-date` זמני** (אחרת יופיע בשני המקומות אחרי שהתאריך עובר; חלופה: `data-pinned="1"`). כשנקבע תאריך — להסיר `date_tbd` ולתת `data-date`. ה-CSS `.date--tbd` (FbEzmel 14, "פרטים בהמשך") נשאר לשימוש עתידי; כיום אין כרטיס TBD.
- 🔴 **אירוע רב-יומי** (yom-kippur-wish-tree 17–18.9, sumii-melani-hosting 8–11.9, sumii-live-studio 30.9–2.10): `data-date` = התחלה **וגם `data-date-end`** = יום אחרון; הפילטר לפי היום האחרון, המקום ב-DOM לפי ההתחלה. **חמישה מקומות לסנכרן:** `events.json` (`date_end`, +`date_label`), המירור `#events-list-data` (`date_end`), `data-date`+`data-date-end` בכרטיס, התווית הגלויה ב-`<bdi>`, ו-`press.json` (`date_end`). `date_label` ב-`events.json` בלבד (שום רנדרר לא קורא; `docs/data-contracts.md` §6.2).
- תווית כרטיס רב-יומי ב-`.date` בתוך `<bdi dir="ltr">` — **פורמט אחיד `d.m.yyyy - d.m.yyyy`:** `17.9.2026 - 18.9.2026`, `8.9.2026 - 11.9.2026`, `30.9.2026 - 2.10.2026`, כך ש-`/press/` ו-`/events/` (שבונה את התווית מ-`date`/`date_end`) מציגים אותה תווית. ⚠️ `events.json::date_label` של yom-kippur עדיין בנוסח הישן (`17.09.26 - 18.09.26`) — שום קוד לא קורא; ליישר כשנוגעים ברשומה.

### אנטומיית כרטיס (`.pcard`, `<a>`)
- שורת flex RTL: `.img` ראשון ב-DOM ⇒ מימין, `.info` משמאלו (עמודה `space-between`, `text-align:right`: תג → כותרת → תאריך). `.img` 292×162 (`aspect-ratio:292/162`, cover); מובייל 171×108; ≤390 רוחב תמונה 150px, כותרת 15 / EN 12.
- תג chip `.tag` רקע `#EEF0EF` padding 4/8: עברית FbEzmel 14; `.tag.en` Copperplate Light **11.5** (כיול מ-14); לטינית בתוך תג עברי `.tag-lat` .82em + `.tag-sep` "|". כל כרטיסי האירוע = `gallery event`.
- כותרת: עברית `.ttl` FbEzmel 16; `.ttl.en` Copperplate **13px** (כיול מ-16); `.ttl .lat` .88em; `.ttl.en .heb` 1.23em. תאריך `.date` Copperplate 11.5, `d.m.yyyy`.
- מודיפיירים: `.img--contain` (רקע `#FAFAFA`, contain) — time-out הישן; `.img--contain.img--white` — לוגו elline של liel-salman; `.pcard--ora` — the-sixth-scent, כותרת EN 10px במובייל.
- 🔴 **תמונות כרטיסי האירוע לא אחידות — לא לנרמל:** מ-michael-konovalenko (17.8) ואילך = `images/events/<slug>/list-card.webp` 876×487 — חוץ מ-the-space-between (`hero.webp`+srcset). הישנים: `card.webp` (zohar-ron 590×328, anat-wegier, gala-night, risa-and-noemi, nir-giorgio-levin, ktuba; `artist-talk/card.webp` משותף ל-artist-talk ול-tal-nehoray), `hero.webp`+srcset (alice-debellis, natasha-zeriker), `liel-salman/logo.webp`, `close-look/card-photo.webp`, `event-how-many-2026-05-26-cover.webp`, `event-4-cover.webp` (loneliness). כרטיס אירוע **חדש** = `list-card.webp`.
- `cover_image` ב-`press.json` = תמונת הכרטיס, חוץ משלוש חריגות: close-look (`card.webp`, עם הטקסט האפוי), artist-talk (`hero-desktop.webp`), press-1 (`00-home-card.webp` הישן).
- ⚠️ ב-7 אירועים יש ל-`/events/` (`#events-list-data`) קרופ רשימה ייעודי ש-`/press/` לא משתמש בו: michael-konovalenko, bar-cohen, hadas-tuval, maria-artamonova, jessica-tabarovsky (`/events/` = `list-card-v2.webp`, 2026-08-19; אצל michael יצירה אחרת לגמרי), zohar-ron ו-alice-debellis (`/events/` = `list-card.webp`). לא הוכרע אם לסנכרן — לא לשנות בלי הכרעה. באירועים הישנים (loneliness, ktuba, close-look, artist-talk, liel-salman, nir-giorgio-levin, risa-and-noemi) אין `list_image`: `/events/` מציג את ה-hero ו-`/press/` קרופ כרטיס ייעודי; צפוי — **לא "לסנכרן"**. the-space-between — אותה תמונה, `hero-480w` שם מול `hero`+srcset כאן.
- תמונה כבדה ⇒ `srcset` + `sizes="(max-width:768px) 171px, 292px"` (כלל-זהב 12). 🔴 החלפת תמונה בכרטיס עם `srcset` ⇒ לעדכן גם את ה-`srcset` (lessons 2026-07-09).
- כותרת כרטיס אירוע **חדש**: `list_title_en` ב-`events.json` כשקיים, אחרת `title_en` — למשל bar-cohen: `artist talk<br>with bar cohen - ‘akra’` (עם מקף; בדף עצמו בלי). קונבנציה: שיחת-אמן = `artist talk<br>with <name>`; חריגים: nir-giorgio-levin-medina ו-tal-nehoray בשורה אחת, ו-risa-and-noemi `artists talk<br>with risa brooke oze and<br>noemi safir`. שם האומן/ית באיות הקנוני לפי `artists.json name_en` (`docs/routes/artists.md`). חריג: anat-wegier כתוב "anat wégier" (כמו בפיגמה) מול `name_en` "anat wegier" — לא לנרמל, ולא להעתיק את האקסנט לטקסט חדש בלי הכרעה. כותרות הכרטיסים הקיימים (natasha-zeriker, how-many, close-look, ktuba, loneliness, liel-salman, gala-night) נקבעו ידנית/לפי פיגמה ושונות מ-`title_en` — **לא לנרמל.**

### הכרעות לכרטיסים ספציפיים (לא "לתקן" לפי הפיגמה)
- **close-look = אוברליי חי**: scrim `rgba(27,27,27,.3)` + "how many partners have u had?" Copperplate Bold 14 (כיול מ-18.06; 11 מובייל) / "מבט מקרוב" FbEzmel 16 (13 מובייל) לבנים, `direction:ltr` על ה-EN, מעל צילום נקי `images/events/close-look/card-photo.{webp,avif}` (584×324, קרופ מרכז מ-imageRef `6658a272…`). 🔴 לא להשתמש כאן ב-`close-look/card.webp` (הטקסט אפוי בו — התמונה ש-`press.json` מצביע עליה).
- **פורטפוליו (press-1)**: `images/press/press-1/00-home-card-v2.{webp,avif}` (584×370) — לא ה-`00-home-card` הישן (171px).
- **ktuba**: `כְּתוּבָּה | <span class="lat">QTUBA</span>` (בפריים המובייל הודבקה כותרת שגויה — מוכרע).
- **loneliness**: "בדידות בתוך סביבה תוססת" — הכותרת הרשמית (audit 2026-07-09); "בתוך בסביבה" בפיגמה = טעות מוכרעת, לא לשחזר. (ציטוטי כתבות, כמו ה-h2 של `press/time-out/`, נשארים verbatim.)
- **תג time-out הישן**: `TIME OUT | תרבות` (לא "מגזין timeout"); אותו תג בשלושת כרטיסי time out (time-out, the-last-station, manicure).
- **zohar-ron (how-many)**: 10.8.2026 — תאריך אמיתי.
- **gala-night**: `gala night - <span class="heb">הקולפן</span>` (Figma `1323:570`), `images/events/gala-night/card.webp` 584×369 (נאפתה מה-hero עם קרופ הפיגמה).
- **liel-salman**: כותרת `pop up tattoos<br>liel salman noam<br><span class="heb">סטודיו</span> elline`, לוגו contain על לבן.
- ⚠️ **the-space-between**: כאן כותרת EN = `title_en` ("the space between — a conversation about art, materials and human experience"), בעוד ב-`/events/` הכרטיס עברי דרך `list_title_he`. אין פריים שמכריע — לא לשנות בלי הכרעה.
- **כרטיסי אירועי רזידנסי SUMII** (sumii-opening, sumii-melani-hosting, yom-kippur-wish-tree, niki-de-saint-phalle-day, sumii-live-studio) **ו-nir-giorgio-levin-medina**: `images/events/<slug>/list-card.{webp,avif}` 876×487. ל-nir-giorgio-levin-medina, sumii-melani-hosting ו-yom-kippur-wish-tree `srcset` (480/768/876) + ה-`sizes` הסטנדרטי; לשאר `src` יחיד. sumii-melani-hosting / yom-kippur-wish-tree = קרופ מה-imageRef ממורכז על חלון ה-cropTransform של המובייל (כרטיסי הפריים `1816:916` / `1864:3058`).
- ⚠️ תמונת כרטיס יום כיפור = חלון הראווה של דיזינגוף ("HOSTING ART RESIDENCY") — verbatim מהפיגמה, לא "לתקן".
- בפריים המובייל לכרטיסי yom-kippur-wish-tree ו-sumii-melani-hosting יש שבבי שם-גלריה דו-שורתיים; באתר נשאר תג `gallery event` (סנכרון 2026-09-27 לא שינה תגיות/כותרות — לא הכרעת משתמש; לשאול לפני שינוי).
- ⚠️ **tal-nehoray**: בקוד וב-`press.json` הכותרת "artist talk with tal nehoray"; החלטת הרה-דיזיין (`docs/redesign-2026-08.md`) קבעה "how many partners have you had? with TAL NEHORAY" per דסקטופ. השינוי נכנס בקומיט לא-קשור (`76e7ed7`) בלי תיעוד — **לבדוק מול פריים המובייל `1323:528` לפני שנוגעים** (הדסקטופ `1323:244` מיושן). הכותרת הנוכחית ב-HTML עומדת עד הכרעה.

### כרטיסי "בקרוב" (`.pcard--soon`)
- אירוע בלי דף: `class="pcard pcard--soon"` + `href="#"` + `data-kind="event"` + `data-date` ⇒ לא-קליקאבילי, קליק מציג טוסט "בקרוב" (`.soon-toast`). הפילטר חל עליהם כרגיל; הטוסט נקשר רק לכרטיסי `--soon` ששרדו.
- כיום **אחד**: **tal-nehoray** 29.6.2026 (`event-tal-nehoray-talk`, `route:null`, אין לו רשומה ב-`events.json`; תמונה `images/events/artist-talk/card.webp` משותפת; `src` יחיד). פתוח ב-`docs/todo.md`.
- כשייבנה דף: להסיר `--soon` ולהחליף `href="#"`, למלא `route` ב-`press.json`; אם יש רשומה ב-`events.json` — למלא `route` **ולמחוק את המפתח `soon`** (לא null) גם שם וגם במירור `#events-list-data`; להוסיף ל-sitemap.

### צ'קליסט — כרטיס חדש ב-`/press/`
0. `press/index.html` נערך כמעט בכל בניית אירוע (גם בסשנים מקבילים) — Re-Read לפני עריכה, וספור מחדש.
1. `<a class="pcard">` במקומו ב-DOM לפי תאריך ההתחלה, חדש→ישן (אירוע: `data-kind="event" data-date=…`, רב-יומי גם `data-date-end` + `<bdi dir="ltr">`; עיתונות: בלי `data-kind`). אירוע בלי דף — כרטיס "בקרוב".
2. fallback `grid-template-rows:repeat(ceil(n/2),auto)` ב-`.cards`; `fetchpriority`/`loading` לפי "גריד וסדר".
3. רשומה ב-`press.json`: 🔴 **להעתיק רשומה אחות מאותו `type` ולערוך — לעולם לא לבנות מרשימת שדות** (השדות לא אחידים: `tag_en`, `subtitle_en`, `gallery_id`, `figma_home_card*`, `_note`). להחליף: `id` (דפוסים — `docs/data-contracts.md` §7), `route`, `date` (+`date_end`), `cover_image` (= תמונת הכרטיס), `exhibition_id`, `homepage_visible`, `_note`; בכתבה גם `source_he`/`source_en`, `tag_he`, `title_he`/`title_en`, `subtitle_he`, `author_he`, `url`, `figma_article_desktop`/`figma_article_mobile`. תג כתבה — זהה בשני הגרידים: `<span class="tag"><span>שם המקור</span><span class="tag-sep">|</span><span>tag_he</span></span>` — שם המקור לבדו (ב-walla ה-`source_he` כבר מכיל "| תרבות"), מקור לטיני ב-`<span class="tag-lat">` (TIME OUT). חריגים, לא לנרמל: press-1 "מגזין פורטפוליו" (בלי `tag-sep`), ora `.tag.en`.
4. בהומפייג': כרטיס ב-`index.html #press` + `homepage_visible:true` + `homepage.json press_section.item_ids` (`docs/routes/homepage.md`). אירוע: רשומה ב-`events.json` + `#events-list-data` (`docs/routes/events.md`).
5. כתבה חדשה: sitemap + OG + בלוק `SEO:auto` לפי Data & sync (אותו קומיט). מונים שמתיישנים: הערת ה-CSS של הגריד ב-`press/index.html` ("all 39 cards") והמונים במסמך ("8 הכתבות", "6 מ-8", 39 / `repeat(20,auto)`); אם בהומפייג' — `homepage.json::press_section._note` ("→ 13 כרטיסים"), `docs/data-contracts.md` §1.4 ו-§7 ("היום 13"), `docs/routes/homepage.md` `#press` (+ `repeat(7,auto)`) וההערה ב-`<section class="press">` ב-`index.html` ("13 cards", "1-7 / 8-13"); כתבה שמקשרת ל-`exhibitions/<slug>/` — לרשימה ב-`docs/routes/exhibitions.md` "נקודות מגע". אירוע — sitemap/OG לפי `docs/routes/events.md` / `events-talks.md`.

### צ'קליסט — שינוי תאריך של אירוע קיים
כל ארבעת השלבים באותו קומיט (קרה ב-zohar-ron-medina: עודכן רק `data-date`, והתווית ו-`press.json` נשארו על 9.9):
1. `data-date` בכרטיס **וגם** הטקסט ב-`.date` (`d.m.yyyy`; רב-יומי — גם `data-date-end` ותווית ה-`<bdi>`).
2. להזיז את הכרטיס למקומו ב-DOM (לפי ההתחלה, חדש→ישן) וליישר `fetchpriority`/`loading`.
3. `date` ב-`press.json` + `events.json` + המירור `#events-list-data` (רב-יומי — גם `date_end` בשלושתם ו-`date_label` ב-`events.json`).
4. עמוד האירוע עצמו (`docs/routes/events.md` / `events-talks.md`).

### SEO של `/press/`
בלוק כתוב-ביד `<!-- SEO:start -->…<!-- SEO:end -->` (canonical, OG `og/homepage-hero-landscape.jpg` 1200×995, JSON-LD `CollectionPage`). ⚠️ `inject.py` מזהה רק `SEO:auto:start/end` ⇒ הרצתו על הדף תוסיף בלוק כפול. פריט ה-todo "ל-`press/index.html` אין בלוק SEO" מיושן.

## כתבות — תבנית משותפת

- כל כתבה = HTML עצמאי עם CSS מוטמע — שינוי רוחבי = עריכה בכל אחת.
- מבנה: `<article class="article heb">` (the-sixth-scent — `class="article"` בלי `heb`, אנגלית) → `.meta-line` (תג | מקור) → `h1.article-title` (FbEzmel 48 ממורכז / 36 מובייל) → `.article-subtitle` → `.article-meta-bar` (byline + actions) → `.body-block .col` (`h2.body-section-h` + `.body-text`) ו-`figure.article-figure` (`.img cover|fit` + `figcaption.cap`) **בסדר שמשתנה**: time-out/the-last-station = תמונה ואז גוף; manicure/the-shared-list = גוף מעל התמונות; walla/press-1/the-sixth-scent/peeling-a-layer = שזורים → `.divider-row` → `a.readmore` "לכתבה המלאה" (חיצוני, `target="_blank" rel="noopener"`; אין ב-the-sixth-scent).
- `.meta-line` — ⚠️ שתי גרסאות: בתבנית time-out (time-out, the-last-station, manicure, peeling-a-layer) ה-`.src` הוא Copperplate (`var(--cop)`; מקור לטיני `.src.lat`) ⇒ מקור עברי **חייב** `.src.src-heb` (FbEzmel 16). 🔴 הכלל `.meta-line .src.src-heb{font-family:var(--heb);font-size:16px}` קיים **רק ב-peeling-a-layer** — שכפול time-out/the-last-station/manicure למקור עברי מחייב להעתיק גם אותו (אחרת העברית נופלת ל-Times New Roman; כלל-זהב 4). בתבנית walla/press-1/the-shared-list ה-`.src` הוא FbEzmel. **כתבה חדשה עם מקור עברי — לשכפל את the-shared-list (או peeling-a-layer).** (the-sixth-scent: `.tag`/`.src` Copperplate 18.)
- **טקסט הכתבה = ציטוט verbatim של המקור** — לא לתקן כתיב/ניסוח (למשל "זלינסקי רוזן", "20 אמנים", ה-h2 של `press/time-out/`). רק שמות אומנים בקפשנים ובקישורים → הכתיב הקנוני של `artists.json` (ב-manicure: "ארס ברוס" שבפיגמה → "ארס ברוש").
- **תמונות — לבדוק מיחזור לפני הורדה:** כתבה על תערוכה מציגה בדרך כלל יצירות שכבר ב-`images/works/v2/` או `images/artists/` — להשוות (RMSE) ולמחזר; רק תמונה חדשה באמת → `images/press/<slug>/`.
- כתובת/שם גלריה בכתבה חדשה → `../../galleries/<slug>/` (דף רק ל-medina ול-dizengoff), לא `../../#galleries` — ה-`#galleries` של manicure קדם לדפי הגלריות (לא לגעת).
- כפתורי share (`data-share-btn`) ו-bookmark (`data-bookmark-toggle` + `data-item-id/title/date`) ב-`components/site-chrome.js`. ב-6 מ-8 הכתבות `data-item-id` = ה-id ב-`press.json`. ⚠️ חריגים: the-last-station `data-item-id="time-out-last-station"`, time-out `data-item-id="time-out"` (= ה-id של the-last-station ב-`press.json`). לא לשנות — bookmarks שמורים עלולים להישבר.
- 🔴 כותרות מעורבות-כיוון (עברית+לטינית): `unicode-bidi:plaintext` על ה-heading + `min-width:0` על `.body-block .col` ועל ילדיו (`.body-block .col>*`) — מונע גלישת flex min-content בנייד צר. קיים ב-the-last-station, manicure, the-shared-list (ה-`min-width` גם ב-peeling-a-layer); **חסר** ב-walla, press-1, time-out, the-sixth-scent — להוסיף שם אם נכנסת כותרת מעורבת.
- JSON-LD: `NewsArticle` + `BreadcrumbList` עם פריט יחיד (הכתבה). רמת `/press/` הוסרה ב-audit 2026-07-09 כי האינדקס לא היה קיים — **עכשיו הוא קיים ואפשר להחזיר, ידנית בלבד** (לא דרך `inject.py` גורף).
- קישור אומנים (`docs/artist-linking.md` §2): כל שם אומן בגוף/קפשן = `a.artist-link`. תמונה: **פורטרט/צילום של האומן עצמו** ⇒ מותר `<a class="artist-img-link">` סביב ה-`<img>` בלבד; **יצירה/מיצב/תיעוד** ⇒ בלי anchor לדף האומן (הקישור בקפשן). audit 2026-07-09 הסיר מ-peeling-a-layer את עטיפות ה-`a.artist-figure-link` לדף האומנים בפיגורות 2-3. ⚠️ חריג פתוח: ה-hero של walla — Open issues.
- איות אנגלי קנוני (audit 2026-07-09, הכרעת משתמש): **adi duek**, **zohar shitrit** — אבל ה-slugs נשארו `adi-duak` / `zohar-shtrit` (כלל-זהב 6). הקישורים ב-walla וב-press-1 (`artists/zohar-shtrit/`, `artists/adi-duak/`) **נכונים — לא "לתקן" את ה-href**; בטקסט לטיני חדש — האיות הקנוני.

## `/press/walla/`
- "מותג הבישום פתח גלריה בכיכר המדינה: 100% מהרווחים הולכים לאמנים", וואלה | תרבות, 5.1.2026, `press.json` `walla-medina`. תמונות `images/press/walla/01..07-*.webp`; כרטיס `images/press/walla-cover.webp`; OG `og/press-walla-cover.jpg`. "לכתבה המלאה" → `e.walla.co.il/item/3806807`.
- ⚠️ ה-hero (`01-shtrit-hero`) עטוף ב-`a.artist-img-link` → `artists/zohar-shtrit/` — חריג לא-מוכרע (Open issues); לא לשנות ולא לחקות.

## `/press/press-1/`
- פורטפוליו, "איך מרגישה בדידות בתוך סביבה תוססת: תערוכה חדשה בגלריית זילינסקי רוזן", 19.1.2026 (ראיון Q&A עם קורין אברהם), `press.json` `press-1`. תמונות `images/press/press-1/00-hero-gal-polk`, `01..15-*` (11-15 = `gallery-1..5`, רצועת תמונות 3); בלוקים ממקור-מובייל (פורטרט ארז, פורטרט קורין, pull quote, Q&A 2.5) מוצגים בכל ה-viewports. כרטיס `00-home-card-v2`; "לכתבה המלאה" → `prtfl.co.il/archives/244442`.
- OG `og/press-press-1-00-home-card.jpg` — ⚠️ **שגוי:** בפועל כרטיס הפלייסטיישן של time-out 2025 (1160×1066, כמעט זהה ל-`og/press-time-out-card.jpg`), לא הכתבה. לאפות מחדש מ-`images/press/press-1/00-home-card-v2.webp` (584×370) או מה-hero, ולעדכן `og:image:width/height`; **לא להעתיק את בלוק ה-SEO של הדף כתבנית עד שיתוקן.**

## `/press/time-out/`
- time out — "דה פיינל קאונטדאון", הכתבה **הישנה** (31.12.2025), `press.json` **`time-out-final-countdown-2025`** (לא `time-out`). hero `images/press/time-out/hero.*` ב-`.img fit`; כרטיס `images/press/time-out/home-card-2025-12-31.*` (ב-`/press/` עם `.img--contain`); OG `og/press-time-out-card.jpg`.
- ⚠️ ה-h2 "בדידות בסביבה תוססת // גלריה זלינסקי-רוזן" (בלי "בתוך", לא מקושר) — ככל הנראה ציטוט הכתבה; לא לשנות בלי הכרעה.
- 🔴 לא להריץ `inject.py` על הדף — עדכון SEO = עריכה ידנית של בלוק `SEO:auto`.

## `/press/the-last-station/`
- מבוסס על תבנית `press/time-out/`. `press.json` id **`time-out`** (route `press/the-last-station/`, `exhibition_id:how-many`).
- גיבור = יצירת **אלסה ארס ברוש** (`images/press/the-last-station/hero.*`, imageRef `2e374464…`); הקפשן מקשר לאומנית, וכותרת הסקשן `HOW MANY PARTNERS HAVE YOU HAD?` (`<span class="lat">`) → `exhibitions/how-many/`.
- "לכתבה המלאה" → timeout.co.il (חיצוני). כרטיס ההומפייג' מפנה **לדף הפנימי**, לא לחיצוני (Figma היסטורי, לפני רה-דיזיין 2026-08: `412:583` דסקטופ / `412:996` מובייל; העיצוב הנוכחי — `docs/routes/homepage.md`).
- 🔴 תמונת הכרטיס תחת **`images/press/time-out/home-card-2026-05-27.*`** (לא בתיקיית the-last-station); OG `og/press-time-out-home-card-2026-05-27.jpg`.

## `/press/the-sixth-scent/`
- ראיון אנגלי (ora magazine | issue 02, 7.6.2026), `press.json` `the-sixth-scent`. 🔴 כל הטקסט **Copperplate UPPERCASE** — גובר על `textCase:LOWER` בפיגמה (`docs/conventions.md` §5). כותרת הכתבה Copperplate 48 (גם במובייל); כותרת הסקשן Copperplate Bold 24 מיושרת שמאלה.
- 5 תמונות `images/press/the-sixth-scent/01-hero, 02..05` (05 ב-`.img fit`); כרטיס `home-card.*`.
- **אין "לכתבה המלאה"** בדף. ⚠️ `url` ב-`press.json` לא אמין כאינדיקציה: `null` גם ב-walla/press-1/time-out, שיש להן "לכתבה המלאה" — הקישור חי רק ב-HTML.
- כרטיס ההומפייג' (היסטורי, לפני רה-דיזיין 2026-08): `551:372` (גריד `551:371`).

## `/press/manicure-against-darkness/`
- "מניקור נגד האפלה וגוף אנושי שמתפרק: 18 תערוכות לסופ״ש", על הקולפן. תבנית the-last-station אבל **סדר הפוך — הגוף מעל תמונת הגיבור** (per Figma): h2 "הקולפן // גלריה ארז זילינסקי רוזן" (18px) + פסקה.
- גיבור = יצירת אלסה ארס ברוש `images/press/manicure-against-darkness/hero.*` (1000×1336, imageRef `37edc008…`); כרטיס `home-card.webp` (1000×555); OG `og/press-manicure-against-darkness-home-card.jpg`. `press.json` `timeout-manicure-against-darkness`.
- 🔴 בפיגמה הקפשן "אלסה ארס ברוס" — **תוקן לכתיב הקנוני "ארס ברוש"**; לא לשחזר.
- קישורים: "הקולפן" → `exhibitions/the-peeler/`; כתובת הגלריה → `../../#galleries` כ-`a.artist-link.location-link` (אדום `#D60000`, מקומי לעמוד); "לכתבה המלאה" → timeout.co.il. כותרת מובייל `clamp(26px, 8.8vw, 36px)`.

## `/press/peeling-a-layer/`
- "מה נפגוש כשנקלף שכבה מהזיכרון שלנו? לתערוכה הבאה יש תשובה", על הקולפן. `press.json` `13tv-peeling-a-layer`; כרטיס `01-hitnaarut.webp`; OG `og/press-peeling-a-layer-home-card.jpg`; "לכתבה המלאה" → 13tv.co.il.
- 3 תמונות `images/press/peeling-a-layer/` בשלוש פרופורציות: `01-hitnaarut` — `.img-wide` 600/338 (מובייל 358/201), "התנערות" של ג׳סיקה טברובסקי; ה-`.img` (לא הקפשן) עטוף ב-`a.artist-figure-link` (CSS מקומי) → **`works/jessica-tabarovsky-1/`** (עמוד היצירה, לא דף האומנית). `02-ishur` — `.img-tall` 600/848 (מובייל 358/542.74), "אישור" של ענת ויז׳ייה. `03-blown-heart` — ברירת מחדל 600/909.62 (מובייל 358/542.74), ירדן אמיר. 🔴 figures 2-3 **בלי** anchor לדף האומן (audit 2026-07-09) — לא להחזיר.
- המקור "רשת 13" עברי ⇒ `.src.src-heb` (FbEzmel 16). פסקת הפתיחה + שמות האומנים/האוצרת ב-Regular: `.body-text strong{font-weight:400}`; כולם מקושרים (זוהר רון, ג׳סיקה טברובסקי, נעמי ספיר, חן זיו, ברוך תורג׳מן, ענת ויז׳ייה, קורין אברהם). "The Art Gallery by Erez Zielinski Rozen" = `<span class="lat">` מקושר להומפייג' (בתת-כותרת ובגוף).

## `/press/the-shared-list/`
- "הרשימה המשותפת // 25.6.26" — roundup שכולל את הקולפן. תבנית peeling-a-layer + `.body-section-h` של manicure (18 / 16 מובייל). `press.json` `portfolio-the-shared-list`.
- מבנה: head (מטא "פורטפוליו | אמנות" — `.tag` אמנות + `.src` פורטפוליו, כותרת 48→36, תת-כותרת = רשימת התערוכות עם `Startup` ב-`<span class="lat">`, byline = **תאריך בלבד, בלי מחבר**) → **גוף מעל התמונות** (h2 "הקולפן בגלריה זלינסקי רוזן" + 2 פסקאות) → 3 figures 600/909.62 (מובייל 358/542.74) → divider → "לכתבה המלאה" → `prtfl.co.il/archives/254898`.
- 🔴 **כל 3 התמונות = מיחזור `images/works/v2/`** — `zohar-ron-5` ("דג 1"), `nir-giorgio-levin-8`, `elsa-ars-brush-1` ("חלום השרף"); אפס תמונות חדשות. OG = מיחזור `og/works-v2-zohar-ron-5.jpg`.
- **verbatim מהכתבה, לא לתקן:** "זלינסקי רוזן" (בלי י׳), "20 אמנים". (הקפשן "צילומים: מ״ל" בפיגורה 1 — כפי שבכתבה; לא הוכרע במפורש.)
- קישורים: הקולפן (תת-כותרת + h2 + גוף) → `exhibitions/the-peeler/`; הגלריה בגוף → `galleries/medina/`; קורין אברהם → `curators/korin-avraham/`; 3 האומנים בקפשנים מקושרים. כרטיסים: ב-`/press/` (25.6.2026) + בגריד `#press` בהומפייג' (בין manicure ל-ora) + `homepage.json item_ids` + sitemap.

## Removed / superseded — do not restore
- `data-pinned` על michael-konovalenko ו-livay-levi — הוסר 2026-09-01; הם גלויים בארכיון. אל תחזיר.
- "פרטים בהמשך" בכרטיס zohar-ron — הוחלף ב-10.8.2026.
- ההערה מעל הגריד ב-HTML ("alice-debellis חסרה בפריים", "the-space-between postdates the frame") — **מיושנת כולה** (שתיהן בפריים המובייל `1323:528`). לא לפעול לפיה.
- zohar-ron-medina 9.9 → **24.9.2026** (`data-date`, `.date`, `press.json`). לא להחזיר 9.9.
- nir-giorgio-levin-medina 8.9 → 17.9 → **30.9.2026** (הכרעת משתמש 2026-09-27). לא להחזיר 8.9 או 17.9 — גם אם כרטיס הפריים `1864:3054` עדיין מציג 17.9.
- כרטיסי "בקרוב" של sumii-opening, nir-giorgio-levin-medina, yom-kippur-wish-tree ו-sumii-melani-hosting — הפכו לקישורים (לכולם דף, 2026-09-27). לא להחזיר `--soon`/`href="#"`, ולא את המפתח `soon` ב-`events.json`/במירור.
- פילטר שמשווה רק את יום ההתחלה (`data-date`) באירוע רב-יומי — בוטל: המשלים הוא היום האחרון (`data-date-end`). וההשוואה מול התאריך המקומי של המבקר (`new Date()`) — הוחלפה ב-`todayIL()`. לא להחזיר אף אחד מהם.
- nav "press & events" → `/#press` — הוחלף ב-`press/`.
- `events/amnon-lipkin/` נמחק (2026-08-28) — אין ולא יהיה לו כרטיס כאן או רשומת `press.json`. (nir-giorgio-levin-medina, שישב פעם על המשבצת 8.9 שלו, הוא אירוע אחר.)

## Open issues
- ⚠️ walla — ה-hero (`01-shtrit-hero.webp`, צילום-יצירה של זוהר שטרית) עטוף ב-`a.artist-img-link`, בניגוד לכלל "יצירה בלי anchor". השימוש היחיד במשפחה — לא להסיר ולא לחקות בלי הכרעה.
- ⚠️ nir-giorgio-levin-medina — `list-card.webp` (משותף לכאן ולרשימת `/events/`) הוא אפייה מעט מעוותת (STRETCH); קרופ `list-card-v2` פתוח ב-`docs/todo.md`. אם יוחלף: לכרטיס כאן יש `srcset` ⇒ גם וריאנטי 480/768 חדשים ועדכון ה-`srcset` (לא רק `src`), יחד עם `events.json::list_image` והמירור.
- ⚠️ zohar-ron-medina (24.9) ו-niki-de-saint-phalle-day (25.9) עדיין בפריים רשימת `/events/` של המעצבת אבל כבר עברו ⇒ חיים כאן. אם יוכרע להשאיר אותם שם — `pinned` בשלושת המקומות (כולל `data-pinned="1"` כאן). פתוח ב-`docs/todo.md`.
- ⚠️ בלי פירוט כאן (הפירוט בסקשנים): 7 אירועים עם קרופ רשימה ב-`/events/` (אנטומיית כרטיס); OG של press-1 שגוי (להוסיף ל-`docs/todo.md`); tal-nehoray ו-the-space-between (הכרעות לכרטיסים); bookmark ids של the-last-station/time-out (לא לשנות בלי החלטה); בלוק `SEO:start` של `/press/` ו-todo מיושן "אין בלוק SEO" (לעדכן `docs/todo.md`).
- 🔴 `inject.py` משייך את `press/time-out/` לרשומה הלא-נכונה — לתקן את ה-matcher (התאמה מדויקת ל-`route`) לפני כל הרצה עתידית.
- Breadcrumbs של הכתבות — אפשר להחזיר רמת "Press & Events" → `/press/` (ידנית). כרטיס "בקרוב" יחיד — tal-nehoray — בלי דף (`docs/todo.md`).
- ⚠️ אזכורי ארז (→ `about/` לפי artist-linking §8) וקורין (→ `curators/korin-avraham/`) לא מקושרים ב-walla, press-1, the-sixth-scent — דורש הכרעה אם זו חריגה מכוונת לציטוטי עיתונות.
- `_note`-ים מיושנים ב-`press.json` (לא הוראות): `event-the-space-between` ("כשעמוד /press/ ייבנה…"), `event-tal-nehoray-talk._route_note`, `event-michael-konovalenko-talk` ("היחיד שנראה היום"), `event-how-many-artist-talk._homepage_visible_note` ("Restored to the homepage", בעוד `homepage_visible:false`), "האירוע עתידי ולכן מסונן" (jessica-tabarovsky, maria-artamonova, baruch-torgeman, elsa-ars-brush), "כרטיס בראש /press/" (zohar-ron-medina, niki-de-saint-phalle-day).
