# Galleries — route notes

> לקרוא לפני עריכה של `galleries/medina/index.html` או `galleries/dizengoff/index.html`, וגם לפני שינוי ב-`data/galleries.json` או ברשומות של גלריה ב-`data/exhibitions.json`. המסמך מתאר את המצב הנוכחי ואת הכללים הפעילים. ההיסטוריה נמצאת ב-`docs/history/CLAUDE-2026-09-27.md` §4.

## Pages

- `/galleries/` (אינדקס) → **אין קובץ**. ⏳ אין עיצוב. בפועל סקשן `#galleries` בהומפייג' משמש אינדקס, והכרטיסים שם הם קישורים לדפי הגלריות (מ-2026-08-12). פרטים ב-`docs/routes/homepage.md`.
- `/galleries/medina/` → `galleries/medina/index.html` · ✅ (2026-08-12)
  - Figma desktop: `XhGH...::1468:305` · Figma mobile: `XhGH...::1467:840`
  - nodes לפי סקשן (מתוך הערות ה-CSS): hero `1467:798`, exhibitions `1467:455`, artworks `1468:665`, manager `1468:363`. מובייל: hero `1467:861`+`1467:885`, tri `1467:900`, manager `1467:1110`.
- `/galleries/dizengoff/` → `galleries/dizengoff/index.html` · ✅ (2026-08-12)
  - Figma desktop: `XhGH...::1473:311` · Figma mobile: `XhGH...::1473:447`
  - nodes לפי סקשן: hero `1473:337`, exhibitions `1473:360`, artworks `1473:394`, manager `1473:404`. מובייל: hero `1473:469`, exhibitions `1473:509`, tri `1473:550`, manager `1473:564`.
- **flea-market:** אין עיצוב ולכן אין דף (`route:null` ב-`galleries.json`). בהומפייג' הכרטיס שלו נשאר `<article>` לא-קליקאבילי עם "coming soon".
- **berlin:** אין דף גלריה (`route:null`). קיים רק כסקשן בהומפייג' (`docs/routes/homepage.md`).
- ⚠️ **זיהוי פריימים ב-Figma:** שמות הפריימים "event-hmp1-*" משקרים. מזהים לפי רוחב ותוכן.
- ⚠️ `Zn3N...::1213:2725` / `Zn3N...::1213:2820` / `Zn3N...::1213:2854` **אינם** דפי גלריה. אלה מצבי lightbox של יצירת אומנות (`docs/components.md`).
- **קישורים נכנסים (מצב נוכחי).** מי שמזיז דף גלריה או מסיר אותו צריך לעדכן את כל אלה:
  - כרטיסי `#galleries` בהומפייג' (`index.html`, כ-`<a>`).
  - שני בלוקי הפוטר ב-`components/site-chrome.js`: `.footer-menu` בדסקטופ ו-`.footer-mobile-mini` במובייל ("גלריית כיכר המדינה" / "גלריית כיכר דיזינגוף").
  - ה-chip "גלריית כיכר דיזינגוף" ב-`sponsors/sumii/index.html` → `galleries/dizengoff/`.
  - הקישור בגוף הכתבה `press/the-shared-list/index.html` → `galleries/medina/`.
  - ה-JSON-LD של חלק מדפי האירועים: `location` מסוג `ArtGallery` עם `@id` ‏`…/galleries/<slug>/#gallery`, ‏`url` וכתובת (`streetAddress`). היום: מדינה — `jessica-tabarovsky`, `maria-artamonova`, `nir-giorgio-levin-medina`; דיזינגוף — חמשת דפי אירועי רזידנסי SUMII. למצוא: `grep -rl 'galleries/<slug>/#gallery' --include='*.html' .`
    - 🔴 ה-`@id` הזה מפנה ל-`@id` של ה-`ArtGallery` ב-JSON-LD של דף הגלריה. **לא לשנות אותו** בדף הגלריה בלי לעדכן את כל דפי האירועים.
  - `sitemap.xml`.
  - `route` ב-`galleries.json`. השדה הצהרתי, ואף רנדרר לא קורא אותו.
  - גם ב-`data/site.json :: footer.links_he` ובעותקי `#fallback-site` שלו (`exhibitions/how-many|loneliness/`, `opencalls/*/`) יש hrefs לגלריות. הם לא מרונדרים, כי הפוטר מגיע מ-`site-chrome.js`, אבל כדאי ליישר גם אותם.

## ⚠️ הערות מיושנות בקוד — המסמך הזה גובר

ההערות בתוך ה-HTML נכתבו לפני שינוי המנגנון. אל תפעל לפיהן:
- ליד `#fallback-galleries` כתוב "כל שינוי ב-data/galleries.json חייב סנכרון לכאן". זה כבר לא נכון. המירור הזה נוצר עכשיו ע"י `python3 tools/sync_data.py`, ואסור לערוך אותו ביד.
- הערות ה-CSS של `.g-art` מדברות על "3 baked 2×3 collages" (מדינה) ועל "3 interior photos" (דיזינגוף). גם זה מיושן: הסקשן הוא קרוסלת כל היצירות.

## מבנה משותף (שני הדפים)

- שני הדפים הם **עותקים נפרדים**. השלד, ה-hero, סקשן היצירות וסקשן המנהלת זהים. **כרטיסי התערוכות שונים** בין הדפים (ראה סקשן לכל דף). שינוי CSS/JS משותף = לערוך את שני הקבצים.
- סדר הסקשנים: hero → `gallery exhibitions` (`#g-ex`) → `the artworks` (`.g-art`) → `the gallery manager` (`#g-mgr`).
- Breakpoints: טאבלט `≤1100` (`--pad-x:48px`), מובייל `≤768` (`--pad-x:16px`). המובייל בנוי לפי פריים המובייל, והוא לא דסקטופ מצומצם.
- כותרות הסקשנים (`.g-sec-head`): Copperplate Light 22px, במובייל 16px.

### Hero
- **דסקטופ:** פס אפור `#EEF0EF` (padding `48/96/40`), הטקסט מיושר לימין, והצילום בצד ימין.
  - שם עברי (`h1`): FbEzmel 80px, px של Figma כמו-שהם. בטאבלט 64px, במובייל 32px.
  - כתובת EN: Copperplate 28 בפיגמה → **22px** בקוד (כיול אופטי). במובייל 12.5px במדינה ו-13px בדיזינגוף. הרחוב והאזור מופרדים בריבוע 4×4 (`.sq`).
  - divider `72×1` `#D8D8D8`. מוסתר במובייל.
  - שעות: FbEzmel 18px verbatim, בשורה `direction:rtl` עם ריבועי 4px. במובייל Light 16px, ממורכז ועם wrap.
  - צילום `204.34×309` ב-`cover`.
- **מובייל:** הצילום ראשון, full-bleed `390×520`, בלי scrim. אחריו בלוק מידע לבן וממורכז (`column-reverse`).
- **דאטה:** השם, הכתובת, השעות ופרטי המנהלת מרונדרים ב-JS. הטעינה היא fetch-first ל-`../../data/galleries.json`, עם נפילה למירור ה-inline `#fallback-galleries` ב-file:// (אותו דפוס כמו בעמוד האוצרת). ה-lookup הוא לפי `slug`:
  - `name_he` → `h1`.
  - `address_street_en` + `address_area_en` → שורת הכתובת. היא מוצגת UPPERCASE לפי הכלל הגלובלי.
  - `hours[]` → `days_he + ' ' + time`.
- 🔴 **ה-`<img>` של ה-hero סטטי ב-HTML.** השדה `image_page_hero` ב-JSON הוא הצהרתי בלבד, והרנדרר לא קורא אותו. החלפת צילום = לערוך את ה-`<img>` (src/srcset/width/height/alt), וגם לעדכן את השדה ב-JSON.
- **תמונות:**
  - מדינה: צילום חלון-ראווה ייעודי `images/galleries/medina/page-hero.webp` (896×1194, +480w/768w), imageRef `281cf784…` crop `10b0bd`. הוא **נפרד** מ-`image_hero` (`hero-v2`), שמשמש את כרטיס ההומפייג'.
  - דיזינגוף: מיחזור של `images/galleries/dizengoff/hero-v2.webp` (822×996, +480w) ב-`cover`.
    - ה-imageRef `c937cf2f` שמופיע בפריימי דיזינגוף הוא רקע שמכוסה לגמרי (leftover של מדינה). מתעלמים ממנו.
    - STRETCH לא-אחיד של Figma על ה-hero של דיזינגוף: מצב נוכחי = `cover` על `hero-v2`, בלי עיוות. ה-note ב-`galleries.json` אומר "do not reproduce the distortion", אבל באותה נשימה מציג "cover מול קרופ מתוח אפוי" כהחלטה פתוחה. לא לשנות בלי הכרעת משתמש.
  - קבצי `hero.webp` הישנים לא נגעו (כלל-זהב 8).
- 🔴 **שעות:** `hours[].time` שמור בקונבנציית ה-bidi: `"18:00-11:00"` ו-`"14:00-11:00"`. הכרעת משתמש: הספרות נשמרות ומוצגות LTR כמו בטקסט הגולמי של Figma, ו**לא "מתקנים" את הסדר**. המשמעות: א'-ה' 11:00–18:00, ו' 11:00–14:00, שבת סגור.
  - **דוגמה מעובדת:** המשתמש מוסר ליום ו' פתיחה 10:00 וסגירה 15:00 ⇒ שומרים `"15:00-10:00"` (סגירה-פתיחה). המקף מחבר את שני המספרים לריצת LTR אחת, ולכן על המסך הם מופיעים בדיוק כמו במחרוזת, ושעת הפתיחה (10:00) צמודה מימין לתווית היום — באותה צורה כמו שורת א'-ה'. אם על המסך מופיע `10:00-15:00`, המחרוזת נשמרה הפוך. ב-JSON-LD (`opens`/`closes`) הסדר לוגי רגיל: `"opens":"10:00"`, `"closes":"15:00"`.
  - **היום השעות זהות בשתי הגלריות, byte-identical:** בשתי הרשומות ב-`galleries.json`, בשני כרטיסי `#galleries` בהומפייג' (`<span>ו' 14:00-11:00</span>` מופיע פעמיים ב-`index.html`) ובשני בלוקי ה-JSON-LD. שינוי לגלריה אחת = עריכה ממוקדת לפי רשומה/כרטיס (לא replace גורף), ולשאול את המשתמש אם גם הגלריה השנייה משתנה.

### Gallery exhibitions (`#g-ex`)
- מרונדר מהמירור **הידני** `#g-exhibitions-data`. זה slice של `exhibitions.json`, ובדיזינגוף יש בו גם רשומה שקיימת רק שם (SUMII).
- 🔴 **סינון לפי `gallery_id` בלבד. אין סינון סטטוס או תאריך באף אחד מהדפים.** הארכיון מוצג, וכרטיס לא נעלם כשהתערוכה מסתיימת (כך ב-Figma: מדינה מציגה את בדידות). השדה `status` במירור הוא מידע בלבד.
- מיון לפי `start_date` יורד. הגריד `.g-ex__grid` הוא `direction:rtl` בשני הדפים, ולכן **החדשה ביותר מימין** (ראשונה ב-DOM).
- כרטיס → `exhibitions/<slug>/`. חריג: רשומת residency מקשרת ל-`route` שלה.
- תאריכים: `dd.mm.yyyy - dd.mm.yyyy`, **התחלה→סיום**, בתוך `.gx-date` (Copperplate Bold 28 → 22px, במובייל 10.5px) עם `direction:ltr`. היפוך ה-bidi שמופיע ברינדור של Figma **לא שוחזר**. החריג היחיד הוא `dates_text` של SUMII.
- scrim: `linear-gradient(180deg, rgba(102,102,102,.2) 0%, rgba(0,0,0,.8) 81%)`. במובייל הוא מתחיל שקוף (`rgba(102,102,102,0)`).
- הסקשן `hidden` כברירת מחדל, ונחשף רק כשהרנדרר מוצא פריטים.
- 🔴 **מובייל:** כרטיסי `177×214.55` (הגאומטריה של `.ex-now` בהומפייג') עם **`column-gap:4px`**. לפי Figma `1473:509`: 177+4+177=358. עם gap של 8 שני הכרטיסים גולשים לשתי שורות. `row-gap:8px`.
- `picture-upgrade.js` עוטף את ה-`<img>` ב-`<picture>`. לכן ה-CSS מעצב גם את `.gx-card>picture` וגם את `.gx-card>img`, והרנדרר קורא ל-`PictureUpgrade.refresh(grid)` אחרי ההזרקה. לשמור על שניהם.

### The artworks (`.g-art`)
- 🔴 **הכרעת משתמש 2026-08-12 — סטייה מכוונת מ-Figma.** בפריימים מופיעים 3 צילומי חלל. במקומם יש קרוסלת `.tri` (הקומפוננטה המשותפת `components/triptych-gallery.*`) של **כל היצירות שמוצגות בגלריה**.
  - בלי dots ובלי חיצים. ניווט ב-swipe, בקליק על peek, או במקלדת.
  - `data-tri-loop="true"`, `data-tri-start="0"`.
- **מקור:** `#g-artworks-data`, מירור **שנוצר אוטומטית** ע"י `sync_data.py`. זו הקרנה של `works.json art_works[]` לפי `gallery_slug`: בסדר המערך הקנוני, בלי רשומות `hidden`.
  - נכון ל-2026-09-27: מדינה 99, דיזינגוף 51. לא לקבע את המספרים בקוד או בטקסט.
  - יצירה עם `gallery_slug` אחר (למשל flea-market) לא מופיעה באף דף.
- השקופיות ב-`object-fit:contain` על `#F9F9F9`. **לא חותכים אומנות.**
- כיתוב `tri-caption` = `artist_en` → דף האומן (כלל-זהב 10). Copperplate Light 16px, `#989898`.
- קליק על השקופית המרכזית → `works/<id>/`. זה עובר דרך `data-artist-href`, שהוא ה-href של קליק-מרכז בקומפוננטה. ה-`alt` הוא "כותרת — אומן".
- 🔴 **טעינה הדרגתית:** השקופיות נבנות עם `data-src`/`data-srcset`. רק ±2 סביב האינדקס הנוכחי מקבלים `src`, דרך האירוע `tri:change`. לא להפוך לטעינה מלאה, כי אז כ-100 תמונות יורדות בבת אחת. `sizes` = `(max-width:768px) 216px, 481px`.
- **גאומטריה:**
  - דסקטופ: מרכז `481×841`, peeks `302×528` ב-opacity `.6` (hover `.85`) ב-`calc(50% ± 473px)`. גובה frame 841.
  - טאבלט (≤1100): `380×665` / `239×418` ב-`±374`. frame 665.
  - מובייל: `216×378` / `117×204.75` ב-`±194.5`. frame 443. ה-tri זולג מעבר לשוליים: `width:calc(100% + 32px); margin:0 -16px`.
- מערך ריק → הסקשן מוסתר.

### The gallery manager (`#g-mgr`)
- נטלי זיגל — אותה מנהלת בשני הדפים. 🔴 **ב-`galleries.json` אובייקט ה-`manager` משוכפל**: יש עותק זהה ונפרד ברשומת `medina` וברשומת `dizengoff`, וכל דף קורא את הרשומה שלו לפי `slug`. שינוי בפרטי המנהלת = לערוך **את שני העותקים**, ואז `python3 tools/sync_data.py`. **היא מנהלת גלריה ולא אומנית, ולכן אין קישור אומן.**
- שם: `name_en_first` ב-Bold ו-`name_en_last` ב-Light. Copperplate 80 בפיגמה → **64px** (כיול אופטי). בטאבלט 48px. במובייל 26px, ושם המשפחה ב-Regular 400.
- אימייל: Copperplate 28 → 22px (במובייל 13px). מוצג UPPERCASE לפי הכלל הגלובלי. ה-`href` הוא `mailto:` באותיות קטנות (`String(email).toLowerCase()`). ב-HTML יש `href` סטטי כ-fallback.
- פורטרט משותף: `images/galleries/managers/natalie-zigel.webp` 1080×1206 (+480w/768w).
  - דסקטופ: קופסה `492×744`, והתמונה `492×652` (`height:87.634%`) ממורכזת אנכית.
  - מובייל: הפורטרט ראשון, `358×448` ב-`cover`.
- 🔴 **ה-src/srcset של הפורטרט סטטיים ב-HTML.** מה-JSON נלקח רק ה-`alt`, כי החלפת `src` כשיש `srcset` לא עושה כלום (לקח 2026-07-09). החלפת פורטרט = לערוך את ה-`<img>` בשני הדפים.
- `manager:null` → הסקשן מוסתר. אין `email` → שורת האימייל מוסתרת.
- נטלי מופיעה גם ב-`about/index.html`, עם פורטרט נפרד (`images/about/people/natalie-zigel.*`) ו-mailto כתוב ביד. ראה `docs/routes/about.md`.

### SEO / OG
- OG: `og/galleries-<slug>-hero.jpg`. שני הדפים רשומים ב-`sitemap.xml`.
- 🔴 **בלוק ה-SEO (`SEO:auto`) מתוחזק ביד.** יש בו JSON-LD מסוג `ArtGallery` עם כתובת ו-`openingHoursSpecification` (א'-ה' opens 11:00 closes 18:00, ו' 11:00–14:00). במדינה יש גם `employee` (Natalie Zigel).
  - ל-`tools/seo/inject.py` **אין ענף galleries**. הרצה שלו על הדפים האלה תחליף את הבלוק ב-WebPage גנרי ותמונת OG ברירת מחדל. **לא להריץ אותו כאן.**
  - שינוי שעות, כתובת או מנהלת = לעדכן את ה-JSON-LD ביד. `employee` (המנהלת) קיים **רק ב-JSON-LD של מדינה**. בדיזינגוף אין `employee`.

## medina — פרטים ייחודיים

- כרטיס תערוכה גמיש: `flex:1 1 0`, `max-width:616px`, `aspect-ratio:616/592`, `min-width:min(280px,100%)`. ה-`direction:ltr` מוגדר על הכרטיס.
- אוברליי: תאריך → פס Solway `EXHIBITION • VOLUME N` → כותרת עברית.
  - הפס: Solway 26px verbatim (אותו פונט כמו ב-Figma), נקודה עגולה 6px, gap 13. במובייל 12px ונקודה 2.82px.
  - הכותרת: `title_he`, FbEzmel 29/31 verbatim. במובייל 14px.
- הרנדרר **תומך ב-`srcset`**. הנתיבים יחסיים לשורש, ומקבלים `../../` בזמן ריצה. `sizes="(max-width:768px) 50vw, 616px"`.
- **מבנה רשומה ב-`#g-exhibitions-data`:** `slug, gallery_id, status, title_en, title_he, volume_en, start_date, end_date, img, w, h, srcset|null, alt`.
- תמונת כרטיס = קרופ ייעודי `images/galleries/medina/ex-card-<slug>.webp`.
- כרגע: `loneliness` (VOLUME 1, `ex-card-loneliness.webp` 690×663) ו-`the-peeler` (VOLUME 2, `ex-card-the-peeler.webp` 817×823 +480w). לפי Figma: בדידות משמאל, הקולפן מימין.
  - התאריכים לא מועתקים לכאן, כי הם משתנים. המקור הוא `data/exhibitions.json` והרשומה ב-`#g-exhibitions-data`, ושניהם מתעדכנים ביד יחד (ראה "שינוי תאריכים או סטטוס של תערוכה" למטה).
- כתובת: `131 jabotinsky st. tel aviv` / `kikar hamedina`.

## dizengoff — פרטים ייחודיים

- כרטיס תערוכה **קבוע** `394×592` (במובייל `177×214.55`).
- אוברליי: תאריך → **כותרת אנגלית** `title_en` ב-Solway 26/31 verbatim (`.gx-ttl`, `max-width:313px`, `text-wrap:balance`). במובייל 12/14.56px, `max-width:147px`. **אין** פס volume ואין כותרת עברית.
- 🔴 `.gx-ov{direction:ltr}` הכרחי. הגריד הוא rtl, ובלי זה ה-"?" של how-many קופץ לראש השורה.
- `.g-ex__grid` קיבל `direction:rtl` ב-2026-08-18 (לפני כן היה חסר). כך הרשומה החדשה (SUMII) יושבת מימין, כמו ב-Figma.
- ⚠️ **הרנדרר מתעלם מ-`srcset`.** צריך להפנות לקובץ שכבר בגודל מתאים. SUMII משתמש ב-`hero-768w.webp`. how-many משתמש ב-`images/exhibitions/how-many/hero.webp` בגודל מלא 1068×1600.
- **מבנה רשומה רגילה:** `slug, gallery_id, status, title_en, start_date, end_date, img, w, h, alt`.
- כרגע: `how-many` ורשומת הרזידנסי `sumii`. התאריכים נמצאים במירור `#g-exhibitions-data` (ושל how-many גם ב-`data/exhibitions.json`). לא מעתיקים אותם לכאן.
- 🔴 **כתובת: `1 Reines st. tel aviv`** / `dizengoff square`. הכרעת משתמש 2026-08-13: הרחוב על שם הרב ריינס. בפיגמה עדיין כתוב "Raines", וזו שגיאת הקלדה. **לא להעתיק בחזרה.**

### כרטיס רזידנסי SUMII (2026-08-18)
- Figma: `1546:3894` (בתוך `1473:360`, דסקטופ) / `1555:120` (בתוך `1473:509`, מובייל).
- **רשומה ב-`#g-exhibitions-data` בלבד** (מהמירור, ה-`alt` מקוצר): `{"slug":"sumii","kind":"residency","route":"sponsors/sumii/","gallery_id":"dizengoff","status":"current","title_en":"pop up art residency","start_date":"2026-08-31","end_date":"2026-10-05","dates_text":"05.10.2026 - 31.08.2026","img":"images/sponsors/sumii/hero-768w.webp","w":768,"h":1024,"alt":"…"}`.
  - 🔴 `gallery_id` חובה: הרנדרר מסנן לפיו לפני ענף ה-residency, ובלעדיו הכרטיס נעלם בשקט. `title_en` הוא הטקסט של שורה 1 באוברליי (`pop up art residency`).
- 🔴 **לא להוסיף ל-`exhibitions.json`.** זו לא תערוכה, והיא הייתה מזהמת את דירוג `__EX_ORDER_INLINE__` בדפי האומנים. היא חיה רק במירור של דיזינגוף.
- הרנדרר מזהה `kind === "residency"` ובונה אנטומיה אחרת (במקום תאריך + כותרת Solway). הקישור הולך ל-`route` → **`sponsors/sumii/`**, ולא ל-exhibitions. `start_date`/`end_date` משמשים רק למיון.
- **שורות האוברליי, מלמעלה למטה:**
  1. `pop up art residency`: Copperplate Light 16 → 13px (במובייל 14 → 10px).
  2. תאריכים: Bold, ב-`.gx-date` הקיים. `dates_text` מוצג verbatim.
  3. `the art gallery by` / `erez zielinski & rozen`: 24 → 19px, עם `letter-spacing:.1em` בשורה הראשונה (במובייל 12 → 9.5px).
  4. `X`: 28.8px, במובייל 16px. verbatim — גליף בודד לא מכיילים.
  5. לוגו Sumii לבן `70.38×32` (במובייל `47×21.37`), דרך `<use href="#sumii-mark">`. ה-`<symbol id="sumii-mark">` מוזרק מיד אחרי `<site-header>`.
- ה-`<symbol id="sumii-mark">` (מקור: Figma `1546:3899`, `currentColor`) הוא עותק ידני, אחד מכמה עותקים inline של הלוגו באתר (עמוד הספונסר, דפי אירועי הרזידנסי, ההומפייג'). שינוי בלוגו = לעדכן את כולם — הרשימה ומתכון ה-grep שמוצא אותם: `docs/routes/sponsors.md` (Assets).
- scrim: בדסקטופ ייחודי, `linear-gradient(0deg,#000,transparent)`. במובייל ה-scrim הסטנדרטי.
- תמונה: `images/sponsors/sumii/hero-768w.webp` ב-`cover`.
- 🔴 **`"05.10.2026 - 31.08.2026"` נשמר verbatim** משני הפריימים: סוף לפני התחלה, הפוך מכרטיס how-many שלידו. לא "לתקן" עד הכרעת מעצבת (ראה Open).

## שינוי X → לגעת ב-Y

- **יצירה ב-`works.json art_works[]`** (הוספה, הסרה, `gallery_slug`, `hidden`, סדר, תמונה): עורכים את ה-JSON ומריצים `python3 tools/sync_data.py`. זה מעדכן את `#g-artworks-data` בשני הדפים. **לא לערוך את המירור ביד.**
  - שדות ההקרנה נגזרים מ-**הרשומה הראשונה** במירור של כל דף (כרגע: `id, artist_slug, artist_en, artist_he, title_he, title_en, img, w, h, widths`). כשהמירור ריק (`[]`) משתמשים ב-`G_ARTWORK_FIELDS` שב-`sync_data.py`.
  - **החריג היחיד לאיסור עריכה ידנית:** כדי להוסיף שדה להקרנה מוסיפים את המפתח **לרשומה הראשונה בלבד**, **בכל דף בנפרד** (מדינה + דיזינגוף). מיד אחר כך מריצים `python3 tools/sync_data.py`, ואז מעדכנים את רנדרר הקרוסלה בשני הדפים כך שיקרא את השדה. מפתח שנוסף לרשומה שאינה הראשונה נמחק בריצה הבאה.
- **`galleries.json`** (שם, כתובת, שעות, מנהלת, רשומה חדשה): עורכים את ה-JSON ומריצים `sync_data.py`. זה מייצר מחדש את שלושת המירורים `#fallback-galleries`: שני דפי הגלריה ועמוד האוצרת. **בנוסף, ביד:**
  - ה-JSON-LD בדף או בדפים הרלוונטיים.
  - הטקסט הכתוב ביד של `.gallery-card` בהומפייג' (`index.html`): השם העברי (`.name`) וה-`aria-label`, הכתובת העברית (`.addr`), השעות (`.hours`) ותמונת `image_hero` (`.img`).
  - שינוי **שעות מדינה**: גם בלוק "שעות פתיחה" (`.info-block`) ב-`contact/index.html`. הוא כתוב ביד בפורמט משלו — סדר לוגי פתיחה–סגירה עם en-dash, `·` ו-`׳` (`ו׳ · 10:00–14:00`), **הפוך** ממחרוזת ה-bidi של `hours[].time` (ה-en-dash לא מחבר את המספרים לריצת LTR אחת), ולכן לא מעתיקים אותה לשם. ⚠️ הבלוק מיושן מאז 2026-08-12 (עדיין השעות הישנות, 10:00–19:00) — לעדכן בפורמט של הדף או לשאול את המשתמש (`docs/data-contracts.md` §1.4).
  - 🔴 **שינוי כתובת או שם של גלריה:** הם כתובים ביד גם מחוץ לרשימה הזו.
    - בבלוק ה-SEO של הדף עצמו: השם האנגלי ב-`<title>`, `og:title`, `twitter:title` ו-`og:image:alt`, והשם העברי בשלושת ה-description. במדינה ה-`meta`/`og`/`twitter` description כוללים גם את הכתובת העברית.
    - מחוץ לדף: שורות הכתובת בדפי האירועים (`events/*` — כולל `streetAddress` ב-JSON-LD `location`), `data/events.json`, `data/homepage.json`, `contact/`, הכתובת בסקשן `#big-news` בהומפייג' (`.nb-sub-addr` ב-`index.html`, בצורת `׳` בלבד) וחלק מכתבות `press/*`. תקדים: תיקון Reines (`docs/todo.md`).
    - לפני סיום צריך לחפש את הכתובת הישנה בכל הצורות שלה: אנגלית ועברית, עם כל סוג גרש (`'` ו-`׳` מופיעים שניהם באתר). לחפש מחרוזות קבועות (`-F`), ובעברית רק את החלק **שאחרי** הגרש — כך נתפסת כל צורת גרש, בכל locale. מדינה: `grep -rliF -e jabotinsky -e 'בוטינסקי' --include='*.html' --include='*.json' . | grep -vE '(^|/)(trash|docs/history)/'`. דיזינגוף: אותו דבר עם `-e reines -e 'ריינס'`. כל מופע צריך עדכון.
      - ⚠️ לא לכתוב את הגרש כ-bracket (`['׳]`). ב-`/usr/bin/grep` של macOS בלי locale של UTF-8, ה-bracket מפספס בשקט כל מופע עם `׳` (בבדיקה נעלמו כך `contact/`, `data/homepage.json` ושלוש כתבות `press/*`). אם בכל זאת צריך regex עם תווים עבריים — להריץ עם `LC_ALL=en_US.UTF-8`.
    - 🔴 **חריג:** מופעים בתוך `<script id="fallback-galleries">` (שני דפי הגלריה ועמוד האוצרת) מתחדשים ע"י `python3 tools/sync_data.py`. **לא לערוך אותם ביד.**
  - כשמשנים תמונה: את ה-`<img>` הסטטי (hero או פורטרט).
  - שינוי אימייל המנהלת צריך לגעת בשלושה מקומות:
    - ה-`href="mailto:…"` הסטטי של `#mgr-email` בשני הדפים (fallback ללא JS, באותיות קטנות).
    - `employee.email` ב-JSON-LD של מדינה.
    - הקישור הכתוב ביד בעמוד האודות, `about/index.html` `.p-handle`: גם ה-`href` וגם הטקסט הגלוי (`docs/routes/about.md`).
  - רשומת berlin: הסקשן `#galleries-berlin` ב-`index.html` כתוב ביד (כתובת + handle; ראה `docs/routes/homepage.md`).
  - רשומה חדשה בלי דף (למשל berlin) לא משפיעה על דפי הגלריה, כי ה-lookup הוא לפי slug.
  - שים לב: עמוד האוצרת מציג את `name_en` של הגלריה לפי `id` בכרטיסי התערוכות. אין צעד ידני (המירור מתחדש), אבל שינוי `id`/`name_en` משפיע עליו.
  - **תיעוד אחרי שינוי שעות/כתובת/מנהלת:** לעדכן כאן את `🔴 שעות` (Hero) ואת `SEO / OG`, ואת בולט השעות ב-`docs/routes/homepage.md` (`## #galleries`), לערך הנוכחי **לכל גלריה בנפרד** (להסיר "זהות בשתי הגלריות" כשזה כבר לא נכון). ערך שהמשתמש מסר ולא נלקח מהפיגמה = לרשום כהכרעת משתמש + "בפיגמה (`1318:657` ופריימי הדף של הגלריה — Pages) עדיין הערך הישן — לא לשחזר בסנכרון פיגמה"; אותה הערה גם ב-`note` של הרשומה ב-`galleries.json` (תקדים Reines) ופריט "לתקן בפיגמה" ב-`docs/todo.md`.
- **תערוכה חדשה בגלריה:**
  1. להוסיף אותה **בסוף** המערך ב-`exhibitions.json` ולהריץ `sync_data.py` (דירוג התערוכות בדפי האומנים). ראה `docs/routes/exhibitions.md`.
  2. **ביד:** להוסיף רשומה ל-`#g-exhibitions-data` של הגלריה, במבנה הרשומה של אותו דף (מדינה ודיזינגוף שונים).
  3. במדינה: לאפות גם קרופ כרטיס `images/galleries/medina/ex-card-<slug>.webp` (+480w אם צריך).
  4. במדינה: ה-`<meta name="description">` מונה את שמות התערוכות בסוגריים ("הקולפן, בדידות בתוך סביבה תוססת"). לעדכן אותו ביד (בלוק ה-SEO כתוב ידנית, ראה SEO / OG).
- **שינוי תאריכים או סטטוס של תערוכה:** `exhibitions.json` **וגם** הרשומה ב-`#g-exhibitions-data`. לשינוי סטטוס יש עוד מירורים ידניים: `#fallback-exhibitions` ב-`exhibitions/how-many/` וב-`exhibitions/loneliness/`, והתג הסטטי בדף הקולפן. ראה `docs/routes/exhibitions.md` ואת ה-Mirror registry ב-`docs/data-contracts.md` §1.4.
- **תאריכי SUMII:** ביד ב-`dates_text` / `start_date` / `end_date` במירור של דיזינגוף. במקביל: `sponsors.json` (`date_start`/`date_end`), `sponsors/sumii/` (`docs/routes/sponsors.md`) והטיזר `#sumii` בהומפייג'.
- **דף גלריה חדש** (flea-market או berlin, כשיהיה עיצוב). משכפלים דף קיים ואז:
  - **בתוך הדף:**
    - 🔴 להחליף את ה-slug הקשיח **בשני מקומות** ברנדרר: ה-lookup `x.slug === '<slug>'` והסינון `x.gallery_id === '<slug>'`. אם שוכחים, הדף מציג בשקט את פרטי הגלריה שממנה הועתק.
    - ⚠️ הרשומות של שתי הגלריות האלה לא מוכנות לרנדרר המשוכפל. הוא קורא רק `name_he`, `address_street_en` + `address_area_en`, `hours[]` ו-`manager`, ושכפול ישיר ירונדר בלי שגיאה אבל חסר. להתאים את הרנדרר או את הרשומה לפני הבנייה.
      - berlin: `name_he:null` ולכן ה-`h1` ריק. `hours:[]`, `manager:null`. הכתובת המלאה (3 שורות, כולל `hotel amano berlin`) נמצאת ב-`address_lines_en[]` / `address_lines_en_mobile[]`, שהרנדרר לא קורא, ולכן שורת המלון תיעלם.
      - flea-market: `address_street_en`/`address_area_en` הם `null` ולכן שורת הכתובת ריקה. גם `hours:[]`, `manager:null`.
    - שם התיקייה חייב להיות זהה ל-`gallery_slug` ב-`works.json`. `sync_data.py` גוזר את ה-slug מהתיקייה.
    - להשאיר בדף את התגיות `<script id="g-artworks-data">` ו-`<script id="fallback-galleries">`. `sync_data.py` מעדכן רק תגיות שכבר קיימות. 🔴 התוכן של `#g-artworks-data` חייב להיות לפחות `[]` ולא ריק: הסקריפט מריץ עליו `json.loads`, ותוכן ריק מפיל את כל הריצה. `[]` נופל לסדר השדות ברירת המחדל. אחר כך להריץ `python3 tools/sync_data.py`.
    - לבחור רנדרר כרטיסי תערוכה. של מדינה: srcset + פס volume, בלי residency. של דיזינגוף: residency, בלי srcset. ולמלא `#g-exhibitions-data` ביד.
    - להחליף ביד את ה-`<img>` של ה-hero, את `<img id="mgr-img">` (אם יש מנהל/ת) ואת בלוק ה-SEO/JSON-LD.
  - **חיווט חיצוני:**
    - `route` ב-`galleries.json`.
    - כרטיס ההומפייג' כ-`<a>`.
    - קישור בפוטר ב-`components/site-chrome.js`, בשני בלוקי הפוטר (`.footer-menu` בדסקטופ ו-`.footer-mobile-mini` במובייל). כרגע הקישור "גלריית שוק הפשפשים" מפנה ל-`/#galleries`.
    - רשומה ב-`sitemap.xml`.
    - OG `og/galleries-<slug>-hero.jpg`.
- **לפני קומיט:**
  - `python3 tools/sync_data.py --check`.
  - לכל שינוי CSS/JS: `node tools/regress/snapshot.mjs --label before --only galleries/`, אחרי השינוי אותו דבר עם `--label after`, ואז `node tools/regress/diff.mjs before after`.
  - בדיקת טיפוגרפיה רק דרך http, לא דרך file:// (שם הפונטים חסומים).

## Open

- מתועדים גם ב-`docs/todo.md`: Zigel/siegel; סדר תאריכי SUMII. "Raines" מופיע שם כפריט **סגור** (באתר כבר הוכרע ותוקן ל-Reines), ונותר רק לתקן בפיגמה. שאר הפריטים כאן (STRETCH ושני הפריטים המסומנים ⚠️) לא מופיעים ב-todo.
- **Zigel / siegel:** בפיגמה הכותרת "Zigel" והאימייל `nataliesiegel8@gmail.com`. נשמר verbatim ב-`galleries.json::manager` ובשני הדפים. אחרי הכרעה: לעדכן את `manager` **בשתי הרשומות** ב-`galleries.json` (medina + dizengoff) ולהריץ `sync_data.py`; את ה-`href` הסטטי של `#mgr-email` בשני הדפים; את `employee` ב-JSON-LD של מדינה (בדיזינגוף אין `employee`); אולי את שם קובץ הפורטרט; ואת `about/`.
- **סדר תאריכי SUMII:** בכרטיס כתוב "05.10.2026 - 31.08.2026" (סוף לפני התחלה). במקומות האחרים ההתחלה ראשונה: בטיזר ההומפייג' "31.08.2026 - 05.10.2026", ובעמוד הספונסר `<bdi dir="ltr">31.08.2026–05.10.2026</bdi>` (en dash, בלי רווחים). אם המעצבת תיישר, לעדכן את `dates_text` במירור של דיזינגוף.
- **"Raines" בפיגמה:** לתקן שם ל-Reines. באתר כבר תוקן.
- **STRETCH של ה-hero בדיזינגוף:** מצב נוכחי `cover` על `hero-v2`, בלי עיוות. ה-note ב-`galleries.json` עדיין מציג "cover מול קרופ מתוח אפוי" כהחלטה פתוחה (ראה Hero). לא לשנות בלי הכרעת משתמש.
- ⚠️ לא הוכרע: היצירה המשותפת `livay-levi-3` (מדינה) מוצגת בכיתוב הקרוסלה כ-"livay levi × hadas tuval" **כקישור אחד** ל-`artists/livay-levi/`. הרנדרר לא מטפל ב-`collab[]`, ולכן הדס טובל לא מקושרת בנפרד. זה פער אפשרי מול כלל-זהב 10.
- ⚠️ לא הוכרע: ב-description של דיזינגוף (`meta description`, `og:description`, `twitter:description` — שלושה עותקים לעדכן ביד) כתוב "התערוכה הנוכחית, צילומי החלל". שני החלקים מיושנים: הסקשן מציג יצירות, ו-`#g-ex` מציג את כל הכרטיסים (how-many + רזידנסי SUMII).

## Removed / do not restore

- **3 צילומי החלל של הפריימים** (`images/galleries/medina/artworks-{left,center,right}*`, `images/galleries/dizengoff/interior-0{1,2,3}*`): הוחלפו בקרוסלת היצירות (הכרעת משתמש 2026-08-12). נשארו בדיסק לא-מקושרים (כלל-זהב 8). **לא לחבר מחדש**, גם אם Figma עדיין מציג אותם.
- **היפוך ה-bidi של תאריכי הכרטיסים** שמופיע ברינדור של Figma: לא לשחזר. מוצג התחלה→סיום. החריג היחיד הוא `dates_text` של SUMII.
- **סינון סטטוס או תאריך** ב-`#g-ex`: לא להוסיף.
- **SUMII ב-`exhibitions.json`:** לא להוסיף.
