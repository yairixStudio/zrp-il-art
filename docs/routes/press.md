# Press — route notes

> קרא לפני עריכה של: `press/index.html`, `press/<article>/index.html`, `data/press.json` (וכל כרטיס עיתונות/אירוע בארכיון). מצב נוכחי + כללים פעילים. היסטוריה מלאה: `docs/history/CLAUDE-2026-09-27.md` §4.
> נקשר ל: `docs/routes/homepage.md` (גריד `#press` בהומפייג'), `docs/routes/events.md` (`/events/` — המשלים של הארכיון; ועמודי האירוע שאינם שיחות, כולל 5 אירועי רזידנסי SUMII), `docs/routes/events-talks.md` (עמודי שיחות-האמן שהכרטיסים מפנים אליהם).

## Pages

- `/press/` → `press/index.html` · desktop `XhGH...::1323:244` (⚠️ שם ה-node "press/events-phone" משקר — זה ה-1440) · mobile `XhGH...::1323:528` · ✅ ארכיון עיתונות + אירועי עבר. 🔴 **מקור הסדר = פריים המובייל `1323:528`** (35 כרטיסים; החריגים — "גריד וסדר"); פריים הדסקטופ `1323:244` **מיושן** ברשימת/סדר הכרטיסים (26 כרטיסים) — לא לסנכרן מולו (הפריסה הדו-עמודתית שלו עדיין תקפה).
- `/press/walla/` → `press/walla/index.html` · `XhGH...::119:740` · `XhGH...::119:868` (legacy `Zn3N...::1213:737`/`1213:865`) · ✅
- `/press/press-1/` → `press/press-1/index.html` (פורטפוליו — ראיון עם קורין אברהם) · `XhGH...::119:972` · `XhGH...::119:1163` (legacy `Zn3N...::1213:968`/`1213:1159`) · ✅
- `/press/time-out/` → `press/time-out/index.html` (time out — "דה פיינל קאונטדאון", 31.12.25 — **הכתבה הישנה**) · `XhGH...::119:1340` · `XhGH...::119:1433` · ✅
- `/press/the-last-station/` → `press/the-last-station/index.html` (time out — "התחנה האחרונה: 25 תערוכות", 27.5.26 — **הכתבה החדשה**, על how-many) · `XhGH...::412:1118` · `XhGH...::412:1214` · ✅
- `/press/the-sixth-scent/` → `press/the-sixth-scent/index.html` (ora magazine — ראיון עם ארז, **English long-form**) · `XhGH...::545:1669` · `XhGH...::545:1762` · ✅
- `/press/manicure-against-darkness/` → `press/manicure-against-darkness/index.html` (time out — "מניקור נגד האפלה וגוף אנושי שמתפרק: 18 תערוכות לסופ״ש", 1.7.26 — על הקולפן) · `XhGH...::1051:291` · `XhGH...::1051:396` · ✅
- `/press/peeling-a-layer/` → `press/peeling-a-layer/index.html` (רשת 13 — "מה נפגוש כשנקלף שכבה מהזיכרון שלנו? לתערוכה הבאה יש תשובה", 1.7.26 — על הקולפן) · `XhGH...::1051:26` · `XhGH...::1051:154` · ✅
- `/press/the-shared-list/` → `press/the-shared-list/index.html` (פורטפוליו — "הרשימה המשותפת // 25.6.26" — roundup שכולל את הקולפן) · `XhGH...::1537:2880` (⚠️ שם ה-frame "press-1-desktop" משקר — כתבה חדשה, זוהתה לפי רוחב 1440) · `XhGH...::1537:3091` ("press-1-mobile") · ✅ (2026-08-18)

## Data & sync — כל המשפחה

- 🔴 **שום דבר במשפחה הזו לא בבעלות `python3 tools/sync_data.py`.** כרטיסי `/press/` וכרטיסי `#press` בהומפייג' הם **HTML כתוב-ביד**; `data/press.json` ו-`data/homepage.json` הם מטא-דאטה דקלרטיבי — הדפים לא קוראים אותם בזמן ריצה. שינוי = לערוך את `press.json` **וגם** את הכרטיס/ים ביד. (`tools/seo/inject.py` כן קורא את `press.json` — title/subtitle/cover/date/source → OG/JSON-LD — ולכן דיוק הרשומות עדיין חשוב.)
- **כתבות long-form: הגוף נשאר ב-HTML**, ב-`press.json` רק meta + cover (ה-`_note` של הקובץ).
- **מלכודות id ב-`press.json`:**
  - id `time-out` = הרשומה של **`press/the-last-station/`** (route עודכן, `exhibition_id:how-many`).
  - id `time-out-final-countdown-2025` = הרשומה של **`press/time-out/`**.
  - 🔴 בגלל זה ה-matcher של `inject.py` (`route.endswith(slug)` **או** `id == slug`, הראשון במערך) משייך את `press/time-out/` לרשומת **the-last-station** (id `time-out` מופיע במערך לפני `time-out-final-countdown-2025`) — אסור לג'נרט את ה-SEO של `press/time-out/` עם `inject.py` (משחזר את באג 2026-07-09).
  - `portfolio-loneliness` = alias של `press-1` (`_alias:"press-1"`, **בלי מפתח `route`**, `homepage_visible:false`) — **לא ליצור לו כרטיס**.
  - `press-1.cover_image` עדיין מצביע ל-`00-home-card.webp` הישן (171px); הכרטיסים בפועל משתמשים ב-`00-home-card-v2`.
- **כרטיס בהומפייג' (`index.html #press`):** הכלל שם = כל כתבות העיתונות + שני אירועי הפתיחה (how-many 26.5, loneliness 19.1) + חריגות משתמש (gala-night, hadas-tuval, livay-levi). כתבה חדשה ⇒ בדרך כלל גם כרטיס שם. כיום 13 כרטיסים ⇒ `repeat(7,auto)`. פרטי הגריד (שורות `ceil(n/2)`, סדר) — ב-`docs/routes/homepage.md`.
- **SEO:** `tools/seo/og_gen.py` שבור (יוצא עם הודעה), ו-`tools/seo/inject.py` בלי ארגומנטים **מסרב לרוץ גורף** ומדפיס את המתכון הידני (הרצה גורפת מרגרסת ~90 דפים — `docs/todo.md`; לא לעקוף). OG לכתבה נאפה ידנית: `magick images/<path>.webp -resize '1200x1200>' -strip -quality 82 og/<name>.jpg` (`>` = לא להגדיל מקור קטן; התיבה 1200×1200 = הגאומטריה של `og_gen.py`, ותואמת את מידות כל ה-OG הקיימים — למשל 1000×1246 → 963×1200). מוסכמה לכתבה חדשה: `og/press-<slug>-<image>.jpg` (הקיימים לא אחידים — למשל `og/press-time-out-card.jpg`, `og/press-peeling-a-layer-home-card.jpg`); בלוק `<!-- SEO:auto:start -->…<!-- SEO:auto:end -->` מועתק מכתבה אחות ונערך — כולל `og:image:width`/`og:image:height` לפי המידות האמיתיות של ה-JPG. (שונה בכוונה מ-`-resize 1200x` שב-CLAUDE.md §7 ובהודעות הכלים — `1200x` מגדיל מקור קטן ומוציא פורטרט גבוה מ-1200.) `inject.py <path>` (דף בודד) עובד, אבל על כתבות: אסור על `press/time-out/` (matcher), ובשאר — רק עם בדיקת diff מלאה של בלוק ה-SEO (עלול להחליף תיאור ידני ולאבד `og:image:width/height`).
- 🔴 **אחרי שכפול כתבה-תבנית — לעבור על כל תגי ה-head** (title, description, canonical, og:*, twitter:*, JSON-LD) מול ה-data של הדף. קרה: `press/time-out` נשא את ה-JSON-LD/og של the-last-station (lessons 2026-07-09).
- **חיפוש האתר** (CLAUDE.md כלל 10א): `search-index.js` נבנה אוטומטית ב-`.githooks/pre-commit` → `tools/search/build_index.py`; `press/` מסווג "כתבה". רשומת כתבה = ה-`<title>` (בלי הסיומת " — Zielinski & Rozen") + ה-`meta description` (נחתך ל-120 תווים); ה-JSON-LD `NewsArticle` של הכתבות נושא `headline` ולא `name`, ולכן לא תורם מילות חיפוש — עוד סיבה לעבור על title/description אחרי שכפול כתבה.
- **Sitemap (כלל-זהב 15):** `/press/` + 8 הכתבות רשומים. כתבה חדשה ⇒ `<url>` ליד רשומות `press/` + `python3 tools/seo/refresh_sitemap_lastmod.py`.
- בדיקות ויזואליות/טיפוגרפיה — רק על http (ב-file:// Chrome חוסם את ה-`@font-face`).
- שינוי רוחבי בכמה עמודים (למשל כל 8 הכתבות, או CSS משותף) ⇒ harness רגרסיה (CLAUDE.md §7.1): `node tools/regress/snapshot.mjs --label before --only press/` → שינוי → `node tools/regress/snapshot.mjs --label after --only press/` → `node tools/regress/diff.mjs before after` (אותם `--only`/`--widths` בשתי הריצות). ⚠️ ה-harness מקפיא את השעון ב-2026-09-27 ⇒ כרטיס אירוע שהיום האחרון שלו 27.9 ואילך מוסר בשני הצילומים, והוספה/שינוי שלו נותנים diff exit 0 שלא מוכיח כלום — לבדוק אותו בדפדפן.

## `/press/` — הארכיון (`press/index.html`)

### מבנה
- hero: דסקטופ פס אפור `#EEF0EF` (padding 48/112/40), מובייל **לבן** (32/16/8). כותרת מוערמת צמודה ימין — "press" (Copperplate Bold, `.hb`) / "& events" (Light, `.hl`). כיול: Figma 80 → **60px** דסקטופ / **46** טאבלט (≤1100) / **27** מובייל (≤768) — זהה ל-`events/index.html`.
- `section.cards#press-list` — כל הכרטיסים **סטטיים ב-HTML** (לא JS-rendered), כרונולוגי **חדש→ישן** בסדר ה-DOM.
- nav גלובלי: "press & events" ב-`components/site-chrome.js` → `press/` (דרך `abs()`; היה `/#press`). מצב active `press` נדלק גם ב-`/press/` וגם ב-`/events/`.

### גריד וסדר
- דסקטופ: `grid-template-columns:repeat(2,…)` + `grid-auto-flow:column` + `direction:rtl` ⇒ המחצית הראשונה יורדת בעמודה **הימנית**, השאר בשמאלית (= פריסת ה-Figma, שתי ריצות כרונולוגיות). gap 48 (טאבלט 40/32).
- מובייל (≤768): flex עמודה אחת = סדר ה-DOM, gap 24.
- `grid-template-rows:var(--pc-rows, repeat(N,auto))`: `--pc-rows` מחושב ב-JS מהכרטיסים ששרדו את הפילטר; ה-`repeat(N,auto)` הסטטי הוא **fallback ללא-JS בלבד**.
- 🔴 **הוספת/הסרת כרטיס ⇒ לעדכן את ה-fallback ל-`ceil(כל הכרטיסים ב-markup / 2)`**, אחרת בלי JS נוצרת עמודה שלישית.
- ב-markup כיום: **39 כרטיסים** (31 אירוע + 8 עיתונות) ⇒ fallback `repeat(20,auto)`. כמה מהם גלויים — משתנה מיום ליום (הפילטר); לספור מחדש לפני עריכה: `grep -c '<a class="pcard' press/index.html`.
- 🔴 **`fetchpriority="high"` — שתי שכבות:** (1) **סטטית** ב-HTML על הכרטיס החדש ביותר שתאריכו (היום האחרון) כבר עבר — כיום niki-de-saint-phalle-day (25.9.2026); כרטיסים עתידיים מעליו `loading="lazy"` (כדי שה-preload scanner לא ימשוך תמונה שעומדת להימחק), כמו כל השאר. (2) **בזמן ריצה**, אחרי הפילטר, ה-IIFE נותן לתמונת הכרטיס הראשון ששרד `fetchpriority="high"` + `loading="eager"` ומסיר `fetchpriority` מכל השאר ⇒ בדיוק אחד במסמך. כשאירוע עתידי עובר אין חובה לגעת (ה-runtime מטפל); בעריכת כרטיסים — ליישר את הסטטי לפי (1).
- **מקום ב-DOM = תאריך ההתחלה (`data-date`)**, חדש→ישן — גם באירוע רב-יומי (sumii-melani-hosting 8–11.9 יושב בין jessica-tabarovsky 10.9 ל-maria-artamonova 7.9; yom-kippur-wish-tree 17–18.9 מתחת ל-zohar-ron-medina 24.9). ראש ה-DOM כיום: sumii-live-studio, nir-giorgio-levin-medina, niki-de-saint-phalle-day, zohar-ron-medina, yom-kippur-wish-tree.
- **אותו תאריך ⇒ סדר הפריים הסמכותי** (`1323:528`): זוג 19.1.2026 — כתבת פורטפוליו (`press-1/`) **מעל** אירוע הפתיחה של בדידות (`events/loneliness/`) (2026-09-01). בהיעדר פריים: המאוחר בשעה למעלה — תקדים baruch-torgeman 18:30 מעל elsa-ars-brush 11:00 (6.9). זוג 30.9 (אין פריים שמכריע): sumii-live-studio (30.9–2.10) מעל nir-giorgio-levin-medina (30.9 בלבד) — עקבי עם היפוך המיון של `/events/` (שם, בשוויון התחלה, המסתיים קודם ראשון); ⚠️ לא הכרעת משתמש.
- **חריגים מפריים המובייל** (כפי שסונכרן 2026-09-27; לכל השאר — סדר הפריים):
  - כרטיסים שאינם בפריים — משובצים כרונולוגית ו**נשארים**: sumii-live-studio (30.9–2.10), niki-de-saint-phalle-day (25.9), zohar-ron-medina (24.9), the-shared-list (25.6 — כתבה חיה עם עמוד ו-sitemap). 🔴 **לא למחוק כרטיס בסנכרון מול הפריים.**
  - nir-giorgio-levin-medina — בפריים (כרטיס `1864:3054`) עם 17.9; באתר **30.9.2026** (הכרעת משתמש 2026-09-27). כרטיס הפריים מיושן — **לא לסנכרן חזרה** (וגם לא ל-8.9 הישן).

### פילטר הארכיון (משלים ל-`/events/`)
- 🔴 **`/press/` = עבר בלבד** (בקשת משתמש 2026-08-12): כרטיס אירוע נמחק בזמן ריצה כל עוד **היום האחרון שלו** (`data-date-end`, ואם אין — `data-date`) הוא היום או אחריו; הוא חי ב-`/events/`. הפילטר הוא **המשלים המדויק** של `(date_end || date) >= today` ב-`events/index.html`, ושניהם משווים מחרוזות `YYYY-MM-DD` מול **`todayIL()`** — תאריך ישראל (`Asia/Jerusalem`, לא התאריך המקומי של המבקר; אותו helper בשני הדפים). ⇒ אירוע עובר מ-`/events/` ל-`/press/` מעצמו למחרת היום האחרון שלו. לכל אירוע בית אחד בדיוק. 🔴 שינוי בלוגיקה של אחד הפילטרים ⇒ לשנות את שניהם יחד, אחרת המשלימות נשברת.
- מימוש: IIFE על `.pcard[data-kind="event"]` מסיר כרטיס בשלושה מקרים — (א) יש לו `data-pinned`; (ב) אין לו `data-date` תקין (TBD — חי ב-`/events/`); (ג) היום האחרון ≥ היום. **כרטיסי עיתונות בלי `data-kind` — לעולם לא מסוננים.** אחר כך מחשב `--pc-rows = repeat(ceil(נותרו/2),auto)` ומקדם את ה-LCP (ראה `fetchpriority` ב"גריד וסדר").
- 🔴 ה-IIFE של הפילטר **חייב לרוץ לפני** סקריפט הטוסט (כדי לא לחבר מאזין לכרטיס שעומד להימחק).
- 🔴 **כל אירוע ב-`events.json` = כרטיס אחד כאן** (+ tal-nehoray, שאין לו רשומה שם) — אירוע בלי כרטיס כאן נעלם מכל הרשימות ביום שאחרי שעבר (הדף עצמו נשאר חי). אירוע חדש (כולל אירועי רזידנסי SUMII) מקבל כרטיס כאן כבר ביום שנבנה. כרטיסים עתידיים **נשארים ב-markup וב-`press.json`** — רק מוסתרים, ויופיעו לבד כשיעבור התאריך.
- **`data-pinned="1"`** ⇒ הכרטיס נמחק כאן תמיד, בלי קשר לתאריך (מספיק `data-kind="event"`; על כרטיס עיתונות, בלי `data-kind`, הוא לא עושה כלום). תואם לדגל `pinned:true` ב-`/events/` (אירוע שהמעצבת עדיין מציגה בפריים הרשימה שלה אחרי שעבר). 🔴 **שלושה מקומות לסנכרן יחד:** `data/events.json`, המירור `#events-list-data` ב-`events/index.html`, וה-`data-pinned` בכרטיס כאן. כיום **אף כרטיס לא pinned**; המנגנון נשאר בקוד לשימוש עתידי.
- 🔴 **אירוע TBD** (`date_tbd:true`, או `date` חסר/פגום) — `/events/` מחזיק אותו תמיד. הכרטיס שלו כאן **בלי `data-date`** (ה-IIFE מסיר אותו) — **לעולם לא `data-date` זמני:** `/press/` בודק רק את `data-date`, ולכן אירוע `date_tbd:true` שהכרטיס שלו נושא תאריך יופיע **בשני המקומות** אחרי שהתאריך עובר. (חלופה: `data-pinned="1"`.) כשנקבע תאריך — להסיר `date_tbd` ולתת `data-date`. ה-CSS `.date--tbd` (FbEzmel 14, "פרטים בהמשך") נשאר לשימוש עתידי (כאן נראה רק בלי JS); כיום אין כרטיס TBD.
- 🔴 **אירוע רב-יומי** (yom-kippur-wish-tree 17–18.9, sumii-melani-hosting 8–11.9, sumii-live-studio 30.9–2.10): הכרטיס נושא `data-date` = יום ההתחלה **וגם `data-date-end`** = היום האחרון; הפילטר לפי היום האחרון, המקום ב-DOM לפי ההתחלה. **חמישה מקומות לסנכרן:** `events.json` (`date_end`, +`date_label`), המירור `#events-list-data` (`date_end`), `data-date`+`data-date-end` בכרטיס כאן, התווית הגלויה ב-`<bdi>` של אותו כרטיס, ו-`press.json` (`date_end`). `date_label` נמצא ב-`events.json` בלבד (מידע; שום רנדרר לא קורא אותו) — ראה `docs/data-contracts.md` §6.2.
- התווית של כרטיס רב-יומי ב-`.date` בתוך `<bdi dir="ltr">` — **פורמט אחיד `d.m.yyyy - d.m.yyyy` בכל כרטיסי הטווח:** `17.9.2026 - 18.9.2026` (yom-kippur — אוחד 2026-09-27; לפני כן `17.09.26 - 18.09.26` בנוסח הפיגמה), `8.9.2026 - 11.9.2026`, `30.9.2026 - 2.10.2026`. כרטיס טווח חדש — באותו פורמט, כך ש-`/press/` ו-`/events/` (שבונה את התווית מ-`date`/`date_end`) מציגים אותה תווית. ⚠️ `events.json::date_label` של yom-kippur עדיין בנוסח הישן — שום קוד לא קורא אותו; ליישר כשנוגעים ברשומה.

### אנטומיית כרטיס (`.pcard`, `<a>`)
- שורת flex RTL: `.img` ראשון ב-DOM ⇒ מימין, ו-`.info` משמאלו (עמודת טקסט `space-between`, `text-align:right`: תג → כותרת → תאריך). `.img` 292×162 (`aspect-ratio:292/162`, cover); מובייל 171×108; ≤390 רוחב תמונה 150px, כותרת 15 / EN 12.
- תג chip `.tag` רקע `#EEF0EF` padding 4/8: עברית FbEzmel 14; `.tag.en` Copperplate Light **11.5** (כיול מ-14); לטינית בתוך תג עברי `.tag-lat` .82em + `.tag-sep` "|". כל כרטיסי האירוע = `gallery event`.
- כותרת: עברית `.ttl` FbEzmel 16; `.ttl.en` Copperplate **13px** (כיול מ-16); `.ttl .lat` .88em (לטינית בתוך עברית); `.ttl.en .heb` 1.23em (עברית בתוך אנגלית).
- תאריך `.date` Copperplate 11.5, פורמט `d.m.yyyy` (טווח רב-יומי — ראה פילטר הארכיון).
- מודיפיירים: `.img--contain` (רקע `#FAFAFA`, contain) — time-out הישן; `.img--contain.img--white` (רקע לבן) — לוגו elline של liel-salman; `.pcard--ora` — the-sixth-scent, כותרת EN 10px במובייל.
- 🔴 **תמונות כרטיסי האירוע לא אחידות — לא לנרמל:** מ-michael-konovalenko (17.8) ואילך = `images/events/<slug>/list-card.webp` 876×487 — חוץ מ-the-space-between (`hero.webp`+srcset). הישנים: `card.webp` (zohar-ron 590×328, anat-wegier, gala-night, risa-and-noemi, nir-giorgio-levin, ktuba; `artist-talk/card.webp` משותף ל-artist-talk ול-tal-nehoray), `hero.webp`+srcset (alice-debellis, natasha-zeriker), `liel-salman/logo.webp`, `close-look/card-photo.webp`, `event-how-many-2026-05-26-cover.webp`, `event-4-cover.webp` (loneliness). כרטיס אירוע **חדש** = `list-card.webp`.
- `cover_image` ב-`press.json` = תמונת הכרטיס, חוץ משלוש חריגות ידועות: close-look (`card.webp`, עם הטקסט האפוי), artist-talk (`hero-desktop.webp`), press-1 (`00-home-card.webp` הישן).
- ⚠️ ב-7 אירועים יש ל-`/events/` (המירור `#events-list-data`) קרופ רשימה ייעודי ש-`/press/` לא משתמש בו: michael-konovalenko, bar-cohen, hadas-tuval, maria-artamonova, jessica-tabarovsky (`/events/` = `list-card-v2.webp`, 2026-08-19; אצל michael יצירה אחרת לגמרי), zohar-ron ו-alice-debellis (`/events/` = `list-card.webp`). לא הוכרע אם לסנכרן — לא לשנות בלי הכרעה. (באירועים הישנים — loneliness, ktuba, close-look, artist-talk, liel-salman, nir-giorgio-levin, risa-and-noemi — `/events/` מציג את ה-hero (אין להם `list_image`) ו-`/press/` קרופ כרטיס ייעודי; צפוי — **לא "לסנכרן"**. the-space-between — אותה תמונה, רק גודל: `hero-480w` שם מול `hero`+srcset כאן.)
- תמונה כבדה ⇒ `srcset` + `sizes="(max-width:768px) 171px, 292px"` (כלל-זהב 12). 🔴 החלפת תמונה בכרטיס עם `srcset` ⇒ לעדכן גם את ה-`srcset` (החלפת `src` לבד לא משנה כלום — lessons 2026-07-09).
- כותרת כרטיס אירוע **חדש**: `list_title_en` ב-`events.json` כשקיים (נוסח כרטיס-הרשימה, לא בהכרח הכותרת הקנונית של הדף), אחרת `title_en` — למשל bar-cohen: `artist talk<br>with bar cohen - ‘akra’` (עם מקף; בדף עצמו בלי). קונבנציה: כותרת שיחת-אמן = `artist talk<br>with <name>` (שבירה אחרי "artist talk"); חריגים קיימים: nir-giorgio-levin-medina ו-tal-nehoray בשורה אחת, ו-risa-and-noemi `artists talk<br>with risa brooke oze and<br>noemi safir`. שם האומן/ית באיות האנגלי הקנוני לפי `artists.json name_en` (למשל "elsa ers brosh" — `docs/routes/artists.md`). חריג קיים: כרטיס anat-wegier כתוב "anat wégier" (כמו בפיגמה) בעוד `name_en` = "anat wegier" — לא לנרמל את הכרטיס הקיים, ולא להעתיק את האקסנט לטקסט חדש בלי הכרעה. כותרות הכרטיסים הקיימים נקבעו ידנית/לפי פיגמה (natasha-zeriker, how-many, close-look, ktuba, loneliness, liel-salman, gala-night שונות מ-`title_en`) — **לא לנרמל אותן.**

### הכרעות לכרטיסים ספציפיים (לא "לתקן" לפי הפיגמה)
- **close-look = אוברליי חי**: scrim `rgba(27,27,27,.3)` + "how many partners have u had?" Copperplate Bold 14 (כיול מ-18.06; 11 מובייל) / "מבט מקרוב" FbEzmel 16 (13 מובייל) לבנים, `direction:ltr` על ה-EN, מעל צילום נקי `images/events/close-look/card-photo.{webp,avif}` (584×324, קרופ מרכז מ-imageRef `6658a272…`). 🔴 לא להשתמש כאן ב-`close-look/card.webp` (הטקסט אפוי בו — זו התמונה ש-`press.json` מצביע עליה).
- **פורטפוליו (press-1)**: `images/press/press-1/00-home-card-v2.{webp,avif}` (584×370) — לא ה-`00-home-card` הישן (171px).
- **ktuba**: `כְּתוּבָּה | <span class="lat">QTUBA</span>` (בפריים המובייל הודבקה כותרת שגויה — מוכרע).
- **loneliness**: "בדידות בתוך סביבה תוססת" — הכותרת הרשמית (audit 2026-07-09). אם בפיגמה עדיין כתוב "בתוך בסביבה" (כפל-ב') — טעות מוכרעת, לא לשחזר. (ציטוטי כתבות, כמו ה-h2 של `press/time-out/`, נשארים verbatim.)
- **תג time-out הישן**: `TIME OUT | תרבות` (לא "מגזין timeout"); אותו תג בשלושת כרטיסי time out (time-out, the-last-station, manicure).
- **zohar-ron (how-many)**: 10.8.2026 — תאריך אמיתי (כבר לא "פרטים בהמשך").
- **gala-night**: `gala night - <span class="heb">הקולפן</span>` (Figma `1323:570`), תמונה `images/events/gala-night/card.webp` 584×369 (נאפתה מה-hero עם קרופ הפיגמה).
- **liel-salman**: כותרת `pop up tattoos<br>liel salman noam<br><span class="heb">סטודיו</span> elline`, לוגו contain על לבן.
- ⚠️ **the-space-between**: כאן כותרת EN = `title_en` ("the space between — a conversation about art, materials and human experience"), בעוד ב-`/events/` הכרטיס עברי דרך `list_title_he`. אין פריים `/press/` שמכריע — לא לשנות בלי הכרעה.
- **כרטיסי אירועי רזידנסי SUMII** (sumii-opening, sumii-melani-hosting, yom-kippur-wish-tree, niki-de-saint-phalle-day, sumii-live-studio) **ו-nir-giorgio-levin-medina**: תמונה `images/events/<slug>/list-card.{webp,avif}` 876×487. ל-nir-giorgio-levin-medina, sumii-melani-hosting ו-yom-kippur-wish-tree יש `srcset` (480/768/876) + ה-`sizes` הסטנדרטי; לשאר — `src` יחיד. sumii-melani-hosting / yom-kippur-wish-tree = קרופ מה-imageRef ממורכז על חלון ה-cropTransform של המובייל (כרטיסי הפריים `1816:916` / `1864:3058`).
- ⚠️ תמונת כרטיס יום כיפור = חלון הראווה של דיזינגוף ("HOSTING ART RESIDENCY") — verbatim מהפיגמה, לא "לתקן".
- בפריים המובייל לכרטיסי yom-kippur-wish-tree ו-sumii-melani-hosting יש שבבי שם-גלריה דו-שורתיים; באתר נשאר תג `gallery event` (הסנכרון של 2026-09-27 לא שינה תגיות/כותרות — לא הכרעת משתמש; לשאול לפני שינוי).
- ⚠️ **tal-nehoray**: בקוד וב-`press.json` הכותרת "artist talk with tal nehoray"; החלטת הרה-דיזיין (`docs/redesign-2026-08.md`) קבעה "how many partners have you had? with TAL NEHORAY" per דסקטופ. השינוי נכנס בקומיט לא-קשור (`76e7ed7`) בלי תיעוד — **לבדוק מול פריים המובייל `1323:528` לפני שנוגעים** (הדסקטופ `1323:244` מיושן). סנכרון 2026-09-27 לא שינה כותרות ⇒ הכותרת הנוכחית ב-HTML עומדת עד הכרעה.

### כרטיסי "בקרוב" (`.pcard--soon`)
- אירוע בלי דף: `class="pcard pcard--soon"` + `href="#"` + `data-kind="event"` + `data-date` ⇒ לא-קליקאבילי, קליק מציג טוסט "בקרוב" (`.soon-toast`, תקדים ההומפייג'). הפילטר חל עליהם כרגיל ⇒ צצים בארכיון ביום שאחרי האירוע; הטוסט נקשר רק לכרטיסי `--soon` ששרדו את הפילטר.
- כיום **אחד**: **tal-nehoray** 29.6.2026 (`event-tal-nehoray-talk`, `route:null`, אין לו רשומה ב-`events.json`; תמונה `images/events/artist-talk/card.webp` — משותפת לכרטיס artist-talk; `src` יחיד). פתוח ב-`docs/todo.md`.
- כשייבנה דף: להסיר `--soon` ולהחליף `href="#"` בכרטיס כאן, למלא `route` ב-`press.json`; אם לאירוע יש רשומה ב-`events.json` — למלא שם `route` **ולמחוק את המפתח `soon`** (לא null) גם שם וגם במירור `#events-list-data`; ולהוסיף ל-sitemap.

### צ'קליסט — כרטיס חדש ב-`/press/`
0. `press/index.html` נערך כמעט בכל בניית אירוע (גם בסשנים מקבילים) — Re-Read לפני עריכה, וספור מחדש: `grep -c '<a class="pcard' press/index.html` ⇒ fallback = `repeat(ceil(n/2),auto)`.
1. `<a class="pcard">` במקומו ב-DOM לפי תאריך ההתחלה, חדש→ישן (אירוע: `data-kind="event" data-date=…`, רב-יומי גם `data-date-end` + תווית `<bdi dir="ltr">`; עיתונות: בלי `data-kind`). אירוע בלי דף — כרטיס "בקרוב".
2. fallback `grid-template-rows:repeat(ceil(n/2),auto)` ב-`.cards`.
3. `fetchpriority`/`loading` לפי הכלל ב"גריד וסדר" (סטטי = הכרטיס החדש ביותר שכבר עבר; כרטיס עתידי — `loading="lazy"`).
4. רשומה ב-`press.json` (`type`, `route`, `cover_image`, `date`, רב-יומי `date_end`, `homepage_visible`…).
5. אם בהומפייג': כרטיס ב-`index.html #press` + `homepage_visible:true` + `homepage.json press_section.item_ids` (ראה `docs/routes/homepage.md`).
6. אירוע: רשומה ב-`events.json` + המירור `#events-list-data` (ראה `docs/routes/events.md`).
7. כתבה חדשה (דף חדש תחת `press/<slug>/`): `<url>` ב-`sitemap.xml` ליד רשומות `press/` + `python3 tools/seo/refresh_sitemap_lastmod.py` (כלל-זהב 15, באותו קומיט); OG נאפה ידנית `og/press-<slug>-<image>.jpg` + בלוק `SEO:auto` מועתק מכתבה אחות ונערך (ראה Data & sync). אירוע — sitemap/OG של עמוד האירוע לפי ה-route doc של המשפחה שלו (`docs/routes/events.md` / `docs/routes/events-talks.md`).

### צ'קליסט — שינוי תאריך של אירוע קיים
1. `data-date` בכרטיס **וגם** הטקסט הגלוי ב-`.date` (`d.m.yyyy`; רב-יומי — גם `data-date-end` ותווית ה-`<bdi>`).
2. להזיז את הכרטיס למקומו ב-DOM (לפי תאריך ההתחלה, חדש→ישן).
3. ליישר `fetchpriority`/`loading` לפי הכלל ב"גריד וסדר".
4. `date` ב-`press.json` + `events.json` + המירור `#events-list-data` (רב-יומי — גם `date_end` בשלושתם ו-`date_label` ב-`events.json`; ראה `docs/routes/events.md`) + עמוד האירוע עצמו (`docs/routes/events.md` / `docs/routes/events-talks.md`).
(קרה ב-zohar-ron-medina: עודכן רק `data-date`, והתווית ו-`press.json` נשארו על 9.9 — כל ארבעת השלבים חובה באותו קומיט.)

### SEO של `/press/`
- בלוק כתוב-ביד `<!-- SEO:start -->…<!-- SEO:end -->` (canonical, OG `og/homepage-hero-landscape.jpg` 1200×995, JSON-LD `CollectionPage`).
- ⚠️ `inject.py` מזהה רק `SEO:auto:start/end` ⇒ הרצתו על הדף הזה **תוסיף בלוק כפול**. פריט ה-todo "ל-`press/index.html` אין בלוק SEO" מיושן.

## כתבות — תבנית משותפת

- כל כתבה = HTML עצמאי עם CSS מוטמע (אין stylesheet משותף לכתבות) — שינוי רוחבי = עריכה בכל אחת.
- מבנה: `<article class="article heb">` (the-sixth-scent — `class="article"` בלי `heb`, כתבה אנגלית) → header: `.meta-line` (תג | מקור) → `h1.article-title` (FbEzmel 48 ממורכז / 36 מובייל) → `.article-subtitle` → `.article-meta-bar` (byline: מחבר/תאריך עם נקודה + actions) → בלוקי גוף `.body-block .col` (`h2.body-section-h` + `.body-text`) ו-`figure.article-figure` (`.img cover|fit` + `figcaption.cap`) **בסדר שמשתנה לפי כתבה**: time-out/the-last-station = תמונה ואז גוף; manicure/the-shared-list = גוף מעל התמונות; walla/press-1/the-sixth-scent/peeling-a-layer = שזורים → `.divider-row` → `a.readmore` "לכתבה המלאה" (חיצוני, `target="_blank" rel="noopener"`; אין ב-the-sixth-scent).
- `.meta-line` — ⚠️ שתי גרסאות: בתבנית time-out (time-out, the-last-station, manicure, peeling-a-layer) ה-`.src` הוא Copperplate כברירת מחדל (מקור לטיני `.src.lat`) ⇒ מקור עברי **חייב** `.src.src-heb` (FbEzmel 16); בתבנית walla/press-1/the-shared-list ה-`.src` הוא FbEzmel כברירת מחדל. (the-sixth-scent: `.tag`/`.src` Copperplate 18.)
- כפתורי share (`data-share-btn`) ו-bookmark (`data-bookmark-toggle` + `data-item-id/title/date`) מטופלים ב-`components/site-chrome.js`. ב-6 מ-8 הכתבות `data-item-id` = ה-id ב-`press.json`.
- ⚠️ חריגים: the-last-station `data-item-id="time-out-last-station"`, time-out `data-item-id="time-out"` (= ה-id של the-last-station ב-`press.json`). לא לשנות — bookmarks שמורים עלולים להישבר.
- 🔴 כותרות מעורבות-כיוון (עברית+לטינית): `unicode-bidi:plaintext` על ה-heading + `min-width:0` על `.body-block .col` ועל ילדיו (`.body-block .col>*`) — מונע גלישת flex min-content בנייד צר. קיים היום ב-the-last-station, manicure, the-shared-list (ה-`min-width` גם ב-peeling-a-layer); **חסר** ב-walla, press-1, time-out, the-sixth-scent — להוסיף שם אם נכנסת כותרת מעורבת.
- JSON-LD: `NewsArticle` + `BreadcrumbList` עם פריט יחיד (הכתבה). רמת `/press/` הוסרה ב-audit 2026-07-09 כי האינדקס לא היה קיים — **עכשיו הוא קיים ואפשר להחזיר, ידנית בלבד** (לא דרך `inject.py` גורף).
- קישור אומנים (`docs/artist-linking.md` §2): כל שם אומן בגוף/קפשן = `a.artist-link`. תמונה בכתבה: **פורטרט/צילום של האומן עצמו** ⇒ מותר `<a class="artist-img-link">` סביב ה-`<img>` בלבד; **יצירה/מיצב/תיעוד** ⇒ בלי anchor לדף האומן (הקישור בקפשן). audit 2026-07-09 הסיר מ-peeling-a-layer את עטיפות ה-`a.artist-figure-link` לדפי האומנים בפיגורות 2-3. ⚠️ חריג פתוח: ה-hero של walla — ראה Open issues.
- איות אנגלי קנוני (audit 2026-07-09, הכרעת משתמש): **adi duek**, **zohar shitrit** — אבל ה-slugs נשארו `adi-duak` / `zohar-shtrit` (כלל-זהב 6). הקישורים ב-walla וב-press-1 (`artists/zohar-shtrit/`, `artists/adi-duak/`) **נכונים — לא "לתקן" את ה-href לפי האיות**; בכל טקסט לטיני חדש להשתמש באיות הקנוני.

## `/press/walla/`
- "מותג הבישום פתח גלריה בכיכר המדינה: 100% מהרווחים הולכים לאמנים", וואלה | תרבות, 5.1.2026, `press.json` `walla-medina`.
- תמונות `images/press/walla/01..07-*.webp`; כרטיס `images/press/walla-cover.webp`; OG `og/press-walla-cover.jpg`. "לכתבה המלאה" → `e.walla.co.il/item/3806807`.
- ⚠️ ה-hero (`01-shtrit-hero`) עטוף ב-`a.artist-img-link` → `artists/zohar-shtrit/` — חריג לא-מוכרע (Open issues); לא לשנות ולא לחקות.

## `/press/press-1/`
- פורטפוליו, "איך מרגישה בדידות בתוך סביבה תוססת: תערוכה חדשה בגלריית זילינסקי רוזן", 19.1.2026 (ראיון Q&A עם קורין אברהם), `press.json` `press-1`.
- תמונות `images/press/press-1/00-hero-gal-polk`, `01..15-*` (11-15 = `gallery-1..5`, רצועת תמונות 3); בלוקים ממקור-מובייל (פורטרט ארז, פורטרט קורין, pull quote, Q&A 2.5) מוצגים בכל ה-viewports.
- כרטיס: `00-home-card-v2`; "לכתבה המלאה" → `prtfl.co.il/archives/244442`.
- OG `og/press-press-1-00-home-card.jpg` — ⚠️ **שגוי:** התמונה בפועל היא כרטיס הפלייסטיישן של time-out 2025 (1160×1066, כמעט זהה ל-`og/press-time-out-card.jpg`), לא הכתבה. לאפות מחדש מ-`images/press/press-1/00-home-card-v2.webp` (584×370) או מתמונת ה-hero, ולעדכן `og:image:width/height`; **לא להעתיק את בלוק ה-SEO של הדף הזה כתבנית עד שיתוקן.**

## `/press/time-out/`
- הכתבה **הישנה** (31.12.2025), `press.json` **`time-out-final-countdown-2025`** (לא `time-out`).
- hero `images/press/time-out/hero.*` ב-`.img fit`; כרטיס `images/press/time-out/home-card-2025-12-31.*` (ב-`/press/` עם `.img--contain`); OG `og/press-time-out-card.jpg`.
- ⚠️ ה-h2 "בדידות בסביבה תוססת // גלריה זלינסקי-רוזן" (בלי "בתוך", לא מקושר) — ככל הנראה ציטוט הכתבה; לא לשנות בלי הכרעה.
- 🔴 לא להריץ `inject.py` על הדף הזה — ה-matcher שלו בוחר את רשומת `time-out` (= the-last-station). עדכון SEO = עריכה ידנית של בלוק `SEO:auto`.

## `/press/the-last-station/`
- מבוסס על תבנית `press/time-out/`. `press.json` id **`time-out`** (route `press/the-last-station/`, `exhibition_id:how-many`).
- תמונת גיבור = יצירת **אלסה ארס ברוש** (cover, `images/press/the-last-station/hero.*`, imageRef `2e374464…`); הקפשן מקשר לאומנית, וכותרת הסקשן `HOW MANY PARTNERS HAVE YOU HAD?` (`<span class="lat">`) → `exhibitions/how-many/`.
- "לכתבה המלאה" → timeout.co.il (חיצוני). כרטיס ההומפייג' מפנה **לדף הפנימי**, לא לחיצוני (Figma היסטורי, לפני רה-דיזיין 2026-08: `412:583` דסקטופ / `412:996` מובייל; העיצוב הנוכחי של `#press` — `docs/routes/homepage.md`).
- 🔴 תמונת הכרטיס יושבת תחת **`images/press/time-out/home-card-2026-05-27.*`** (לא בתיקיית the-last-station); OG `og/press-time-out-home-card-2026-05-27.jpg`.

## `/press/the-sixth-scent/`
- ראיון אנגלי (ora magazine | issue 02, 7.6.2026), `press.json` `the-sixth-scent`.
- 🔴 כל הטקסט **Copperplate UPPERCASE** — גובר על `textCase:LOWER` בפיגמה (`docs/conventions.md` §5). כותרת הכתבה Copperplate 48 (גם במובייל); כותרת הסקשן Copperplate Bold 24 מיושרת שמאלה.
- 5 תמונות `images/press/the-sixth-scent/01-hero, 02..05` (05 ב-`.img fit`); כרטיס `home-card.*`.
- **אין "לכתבה המלאה"** בדף. ⚠️ `url` ב-`press.json` לא אמין כאינדיקציה: הוא `null` גם ב-walla/press-1/time-out, שכן יש להן "לכתבה המלאה" — קישור ה-readmore חי רק ב-HTML.
- כרטיס ההומפייג' (היסטורי, לפני רה-דיזיין 2026-08): `551:372` (גריד `551:371`); העיצוב הנוכחי של `#press` — ראה `docs/routes/homepage.md`.

## `/press/manicure-against-darkness/`
- תבנית the-last-station אבל **סדר הפוך — סקשן הגוף מעל תמונת הגיבור** (per Figma): h2 "הקולפן // גלריה ארז זילינסקי רוזן" (18px) + פסקה.
- גיבור = יצירת אלסה ארס ברוש `images/press/manicure-against-darkness/hero.*` (1000×1336, imageRef `37edc008…`); כרטיס `home-card.webp` (1000×555); OG `og/press-manicure-against-darkness-home-card.jpg`. `press.json` `timeout-manicure-against-darkness`.
- 🔴 בפיגמה הקפשן "אלסה ארס ברוס" — **תוקן לכתיב הקנוני "ארס ברוש"**; לא לשחזר.
- קישורים: "הקולפן" → `exhibitions/the-peeler/`; כתובת הגלריה → `../../#galleries` כ-`a.artist-link.location-link` (אדום `#D60000`, מקומי לעמוד); "לכתבה המלאה" → timeout.co.il. כותרת מובייל `clamp(26px, 8.8vw, 36px)`.

## `/press/peeling-a-layer/`
- `press.json` `13tv-peeling-a-layer`; כרטיס `01-hitnaarut.webp`; OG `og/press-peeling-a-layer-home-card.jpg`; "לכתבה המלאה" → 13tv.co.il.
- 3 תמונות `images/press/peeling-a-layer/` בשלוש פרופורציות:
  - `01-hitnaarut` — `.img-wide` 600/338 (מובייל 358/201), "התנערות" של ג׳סיקה טברובסקי; ה-`.img` (לא הקפשן) עטוף ב-`a.artist-figure-link` (CSS מקומי) → **`works/jessica-tabarovsky-1/`** (עמוד היצירה, לא דף האומנית).
  - `02-ishur` — `.img-tall` 600/848 (מובייל 358/542.74), "אישור" של ענת ויז׳ייה.
  - `03-blown-heart` — ברירת מחדל 600/909.62 (מובייל 358/542.74), ירדן אמיר.
  - 🔴 figures 2-3 **בלי** anchor לדף האומן (audit 2026-07-09) — לא להחזיר.
- המקור "רשת 13" עברי ⇒ `.src.src-heb` (FbEzmel 16, לא Copperplate).
- פסקת הפתיחה + שמות האומנים/האוצרת ב-Regular: `.body-text strong{font-weight:400}`. כולם מקושרים: זוהר רון, ג׳סיקה טברובסקי, נעמי ספיר, חן זיו, ברוך תורג׳מן, ענת ויז׳ייה, קורין אברהם.
- "The Art Gallery by Erez Zielinski Rozen" = `<span class="lat">` מקושר להומפייג' (בתת-כותרת ובגוף).

## `/press/the-shared-list/`
- תבנית peeling-a-layer + `.body-section-h` של manicure (18 / 16 מובייל). `press.json` `portfolio-the-shared-list`.
- מבנה: head (מטא "פורטפוליו | אמנות" — `.tag` אמנות + `.src` פורטפוליו, כותרת 48→36, תת-כותרת = רשימת התערוכות עם `Startup` ב-`<span class="lat">`, byline = **תאריך בלבד, בלי מחבר**) → **גוף מעל התמונות** (h2 "הקולפן בגלריה זלינסקי רוזן" + 2 פסקאות) → 3 figures 600/909.62 (מובייל 358/542.74) → divider → "לכתבה המלאה" → `prtfl.co.il/archives/254898`.
- 🔴 **כל 3 התמונות = מיחזור `images/works/v2/`** — `zohar-ron-5` ("דג 1"), `nir-giorgio-levin-8`, `elsa-ars-brush-1` ("חלום השרף"); אפס תמונות חדשות. OG = מיחזור `og/works-v2-zohar-ron-5.jpg`. (אין תלות דאטה — רק קבצי תמונה.)
- **verbatim מהכתבה, לא לתקן:** "זלינסקי רוזן" (בלי י׳), "20 אמנים". (הקפשן "צילומים: מ״ל" בפיגורה 1 — כפי שבכתבה; לא הוכרע במפורש.)
- קישורים: הקולפן (תת-כותרת + h2 + גוף) → `exhibitions/the-peeler/`; הגלריה בגוף → `galleries/medina/`; קורין אברהם → `curators/korin-avraham/`; 3 האומנים בקפשנים מקושרים.
- כרטיסים: ב-`/press/` (25.6.2026) + בגריד `#press` בהומפייג' (בין manicure ל-ora) + `homepage.json item_ids` + sitemap.

## Removed / superseded — do not restore
- `data-pinned` על michael-konovalenko ו-livay-levi — הוסר 2026-09-01; הם גלויים בארכיון. אל תחזיר.
- "פרטים בהמשך" בכרטיס zohar-ron — הוחלף ב-10.8.2026.
- ההערה מעל הגריד ב-HTML ("alice-debellis חסרה בפריים", "the-space-between postdates the frame") — **מיושנת כולה** (שתיהן בפריים המובייל `1323:528`). לא לפעול לפיה.
- zohar-ron-medina 9.9 → **24.9.2026** (`data-date`, `.date`, `press.json`). לא להחזיר 9.9.
- nir-giorgio-levin-medina 8.9 → 17.9 → **30.9.2026** (הכרעת משתמש 2026-09-27). לא להחזיר 8.9 או 17.9 — גם אם כרטיס הפריים `1864:3054` עדיין מציג 17.9.
- כרטיסי "בקרוב" של sumii-opening, nir-giorgio-levin-medina, yom-kippur-wish-tree ו-sumii-melani-hosting — הפכו לקישורים (לכולם דף, 2026-09-27). לא להחזיר `--soon`/`href="#"`, ולא את המפתח `soon` ב-`events.json`/במירור.
- פילטר שמשווה רק את יום ההתחלה (`data-date`) גם באירוע רב-יומי — בוטל: המשלים הוא היום האחרון (`data-date-end`). וההשוואה מול התאריך המקומי של המבקר (`new Date()`) — הוחלפה ב-`todayIL()`. לא להחזיר אף אחד מהם.
- nav "press & events" → `/#press` — הוחלף ב-`press/`.
- `events/amnon-lipkin/` נמחק (2026-08-28) — אין ולא יהיה לו כרטיס כאן או רשומת `press.json`. (nir-giorgio-levin-medina, שישב פעם על המשבצת 8.9 שלו, הוא אירוע אחר.)

## Open issues
- ⚠️ walla — ה-hero (`01-shtrit-hero.webp`, צילום-יצירה של זוהר שטרית) עדיין עטוף ב-`a.artist-img-link` → `artists/zohar-shtrit/`, בניגוד לכלל "יצירה בלי anchor". השימוש היחיד במשפחה — לא להסיר ולא לחקות בלי הכרעה.
- ⚠️ תמונת `/press/` מול רשימת `/events/` — 7 אירועים עם קרופ רשימה ייעודי ב-`/events/` ש-`/press/` לא משתמש בו — לא הוכרע (הרשימה והפער הצפוי באירועים הישנים — ב"אנטומיית כרטיס").
- ⚠️ nir-giorgio-levin-medina — `list-card.webp` (משותף לכרטיס כאן ולרשימת `/events/`) הוא אפייה מעט מעוותת (STRETCH); קרופ `list-card-v2` לא-מעוות פתוח ב-`docs/todo.md`. אם יוחלף: לכרטיס כאן יש `srcset` ⇒ צריך גם וריאנטי 480/768 חדשים ועדכון ה-`srcset` (לא רק `src`), יחד עם `events.json::list_image` והמירור.
- ⚠️ zohar-ron-medina (24.9) ו-niki-de-saint-phalle-day (25.9) עדיין בפריים רשימת `/events/` של המעצבת אבל כבר עברו ⇒ חיים כאן. אם יוכרע להשאיר אותם שם — `pinned` בשלושת המקומות (כולל `data-pinned="1"` בכרטיס כאן). פתוח ב-`docs/todo.md`.
- ⚠️ OG של `press/press-1/` שגוי (כרטיס time-out 2025 במקום הכתבה) — ראה הסקשן שלו; להוסיף גם ל-`docs/todo.md`.
- ⚠️ tal-nehoray — כותרת הכרטיס (ראה למעלה) — לאמת מול פריים המובייל `1323:528`.
- ⚠️ the-space-between — כותרת EN ב-`/press/` מול עברית ב-`/events/` (ראה למעלה).
- 🔴 `inject.py` משייך את `press/time-out/` לרשומה הלא-נכונה (id `time-out`) — לתקן את ה-matcher (התאמה מדויקת ל-`route`) לפני כל הרצה עתידית.
- ⚠️ `press/index.html` — בלוק SEO עם markers לא-סטנדרטיים (`SEO:start`) ⇒ `inject.py` יכפיל; פריט ה-todo "אין בלוק SEO" מיושן — לעדכן את `docs/todo.md`.
- Breadcrumbs של הכתבות — אפשר להחזיר רמת "Press & Events" → `/press/` (ידנית).
- כרטיס "בקרוב" יחיד — tal-nehoray — עדיין בלי דף (`docs/todo.md`).
- ⚠️ bookmark ids לא תואמים ל-`press.json` ב-the-last-station/time-out (לא לשנות בלי החלטה).
- ⚠️ אזכורי ארז (→ `about/` לפי artist-linking §8) וקורין (→ `curators/korin-avraham/`) לא מקושרים ב-walla, press-1, the-sixth-scent — דורש הכרעה אם זו חריגה מכוונת לציטוטי עיתונות.
- `_note`-ים מיושנים ב-`press.json` (לא הוראות): `event-the-space-between` ("כשעמוד /press/ ייבנה…"), `event-tal-nehoray-talk._route_note` (מזכיר טוסט בהומפייג'), `event-michael-konovalenko-talk` ("היחיד שנראה היום"), `event-how-many-artist-talk._homepage_visible_note` ("Restored to the homepage", בעוד `homepage_visible:false`), "האירוע עתידי ולכן מסונן" של jessica-tabarovsky/maria-artamonova/baruch-torgeman/elsa-ars-brush, ו"כרטיס בראש /press/" של zohar-ron-medina/niki-de-saint-phalle-day.
