# רה-דיזיין אוגוסט 2026 — מפת שינויים + פרומפטים לסוכנים

> נבנה 2026-08-04 מתוך הערות המעצבת (הערות מוצמדות בפיגמה) + קריאה מלאה של 9 ה-frames החדשים.
> **עיקרון-על:** עמוד הבית עוצב **במובייל בלבד** (`1318:363`) — המובייל הוא המקור הסמכותי לתוכן ולסדר; **הדסקטופ = אדפטציה על דעת המפתח**, נאמנה לשפה הדסקטופית הקיימת של האתר. ארבעת העמודים החדשים עוצבו בשני breakpoints.
> כל פרומפט למטה הוא **עצמאי** — מיועד להדבקה כמו-שהוא לסוכן נפרד.

---

## א. מפת השינויים (תמצית)

### עמודים חדשים (4)

| # | עמוד | Route מוצע | Figma desktop | Figma mobile |
|---|---|---|---|---|
| 1 | אירועים קרובים (upcoming events) | `/events/` | `1318:1728` | `1318:2012` |
| 2 | כל העיתונות והאירועים (press & events) | `/press/` | `1323:244` (⚠️ שם ה-node "phone" — משקר) | `1323:528` |
| 3 | עמוד ספונסר soos | `/sponsors/soos/` | `1318:3287` | `1318:3480` |
| 4 | אירוע חדש "The Space Between" (מור צופיה געש, 3.9.2026, כיכר המדינה) | `/events/the-space-between/` | `1361:434` | `1361:232` |

### שינויים בעמוד הבית (לפי `1318:363`)

| # | סקשן | מה משתנה |
|---|---|---|
| 5 | new perfume | עיצוב חדש לבושם how-many (תמונה חדשה אחת במקום גלריית 5 thumbs) + **סקשן בושם חדש "סבלנות"** (הקולפן) — בלי כפתור רכישה (אין עמוד מוצר) |
| 6 | upcoming events | **מחיקת העיגול המסתובב + הקרוסלה**; במקום: כותרת מוערמת + 2 פוסטרים ("הרשימות") + כפתור `view all` → `/events/` |
| 7 | big news | עיצוב חדש: **טקסט בלבד**, בלי תמונה ובלי טבעת BIG |
| 8 | the art works | עיצוב חדש: **גריד שחמט 2×3** (תמונות חדשות) + בלוק curator ממורכז עם כפתור |
| 9 | x our artists | עיצוב חדש: **קרוסלת פוקוס** (יצירה מרכזית גדולה + הצצות צד בשקיפות) במקום גריד/קרוסלת 38; **מיקום חדש** בעמוד |
| 10 | press & events | צמצום ל-**9 כרטיסים** (כל העיתונות + 2 אירועי פתיחה בלבד — בקשת קורין) + כפתור `more press & events` → `/press/` |
| 11 | הקולפן X soos | **סקשן חדש** (חסות רמקולים) + כפתור `read more` → `/sponsors/soos/` |
| 12 | סדר סקשנים | reorder מלא (ראה סדר יעד למטה) + סנכרון tribe/archive/instagram לפריים |

**סדר היעד בעמוד הבית** (per `1318:363`):
hero → announcement → קול קורא → exhibitions now (+רצועת our artists) → **perfume how-many** → **perfume סבלנות** → **upcoming events** → **big news** → **the art works + curator** → **x our artists** → the galleries → **הקולפן X soos** → loneliness X the tribe → exhibitions archive → instagram → **press & events (9)** → newsletter/footer.
(רצועת "sponsored by" + לוגו זילינסקי בתחתית הפריים = הפוטר הגלובלי הקיים ב-`site-chrome.js` — אין עבודה. node `1323:926` "view" בסוף הפריים = שארית עיצוב, להתעלם.)

### שינוי גלובלי
- **nav:** הפריט `press & events` ב-`components/site-chrome.js` יפנה מ-`/#press` אל `/press/` (משפיע על כל הדפים).

---

## ב. הכרעות רוחביות (כל הסוכנים מחויבים להן)

1. **מובייל הומפייג' = מקור אמת; דסקטופ הומפייג' = אדפטציה** בשפה הדסקטופית הקיימת (גריד 2 עמודות ל-press, פאנלים דו-עמודתיים, padding‏ 96px וכו').
2. **כיול אופטי Copperplate:** הפונט שלנו רחב ~28% מזה שבפיגמה. 80px פיגמה → ‎~64px בקוד; 58→‎~46; 36→‎~26-28; 20→‎~16 (ראה משפחת artist-talk ב-CLAUDE.md). עברית FbEzmel = px של פיגמה כמו-שהם. Solway = verbatim.
3. **תיקוני-פיגמה מוכרעים (לא לשחזר טעויות):**
   - zohar-ron: **"פרטים בהמשך"** ולא ‎19.7.2026 (הפריים המובייל של press&events מיושן; הדסקטופ + state הפרויקט צודקים).
   - הכרטיס מ-25.2.2026 = **"כְּתוּבָּה | QTUBA"** (במובייל הודבקה בטעות כותרת "בדידות...").
   - כותרת loneliness הקנונית: **"בדידות בתוך סביבה תוססת"** (בכרטיס הארכיון בפריים כתוב בלי "בתוך" — טעות מוכרעת).
   - תג הכתבה הישנה של timeout: **"time out | תרבות"** (per דסקטופ; לא "מגזין timeout").
   - כותרת כרטיס tal nehoray: לפי הדסקטופ — `how many partners have you had? with TAL NEHORAY`.
   - `SUBSCRIBE` מופיע בפיגמה ב-Inter — **אסור Inter**; הפוטר הגלובלי הקיים כבר נכון.
4. **חריגת-איות soos (הכרעה: לכבד):** `soos.sound`, `www.soos.audio`, `Bella` נשארים **lowercase** — מסומן בפיגמה `textCase:LOWER` מפורש (מותג צד-ג'). מימוש: מחלקת חריג (למשל `.lc{text-transform:none}`) נקודתית. כל שאר האנגלית — Copperplate UPPERCASE כרגיל.
5. **scrims בעמוד The Space Between:** בפיגמה שכבות ה-scrim שקעו בטעות מתחת לתמונה (אומת ברינדור). **לממש לפי קונבנציית המשפחה:** דסקטופ = גרדיאנט כהה-למעלה `linear-gradient(180deg, rgba(0,0,0,.8), transparent)` (הכותרת בראש התמונה!), מובייל = `rgba(27,27,27,.4)` שטוח.
6. **fills מרובי-שכבות:** בכמה כרטיסים יש מחסנית תמונות — רק אחת גלויה. **חובה לרנדר את ה-node כ-PNG לפני הורדת תמונות** (lessons — לא לנחש מסדר ה-fills).
7. **תמונות:** `ls images/...` לפני כל הורדה — רוב ה-imageRefs כבר קיימים בריפו (אירועי יולי/אוגוסט, כתבות). לא לדרוס קבצים (כלל-זהב 8); crop חדש = קובץ חדש.
8. **file://:** אין fetch — כל דאטה דינמי בעמוד = מירור inline (`<script type="application/json">`), כמו התקדימים.
9. אחרי כל משימה: עדכון `CLAUDE.md` §4 + `sitemap.xml` (עמוד חדש) + `FIGMA_LINKS.md` + **git commit** + סיכום קצר בעברית.

### שאלות פתוחות (לא חוסמות — הפרומפטים כוללים המלצת ברירת-מחדל)
- **אירוע alice debellis (6.8) חסר בעמוד press & events** בפיגמה (19 כרטיסים ותא ריק בגריד) — כנראה השמטה של המעצבת. המלצה: להוסיפו במקום הכרונולוגי (ממלא את התא הריק). לוודא מולה.
- **רוחבי כרטיסי exhibitions-now:** הפריים החדש חוזר על 177px+fill, אבל יש הכרעת משתמש (2026-07-26) לרוחב שווה — ההמלצה: להשאיר רוחב שווה.
- **שני הפוסטרים ("הרשימות") ב-upcoming** הם תמונות מעוצבות שהמעצבת תחליף ידנית מדי תקופה — זה תהליך תוכן, לא קוד.
- הסלאגים/Routes המוצעים (`/events/`, `/press/`, `/sponsors/soos/`, `events/the-space-between/`) — ניתנים לשינוי לפני התחלה; אחרי בנייה אסור (כלל-זהב 6).

---

## ג. הפרומפטים

> סדר מומלץ: 1→4 (עמודים חדשים), אחר-כך 5→11 (סקשני הומפייג', אפשר במקביל בזהירות על index.html — עדיף טורי), ולבסוף 12 (reorder + חיווט). פרומפטים 2 ו-10 תלויים זה בזה רק בכפתור/nav — אפשר לבנות במקביל.

---

### פרומפט 1 — עמוד חדש: אירועים קרובים `/events/`

```
קרא קודם את CLAUDE.md ואת docs/conventions.md. בנה עמוד חדש: events/index.html (route ‎/events/‎) — "upcoming events".
פיגמה (חובה לקרוא את שניהם):
דסקטופ: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-1728&m=dev
מובייל: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-2012&m=dev
מבנה: header/footer גלובליים (site-chrome.js). כותרת מוערמת "upcoming" (Copperplate Bold) מעל "events" (Light) — בפיגמה 80px, בקוד ~64px (כיול אופטי, ראה משפחת artist-talk); מובייל 36→~26px. דסקטופ: פס כותרת רקע ‎#EEF0EF (padding 48px 96px 40px, הכותרת צמודה ימין), גריד כרטיסים 2 עמודות ברוחב 1248, gap 48, כרטיס 600×162. מובייל: header ‎#EEF0EF, גוף לבן, עמודה אחת 358, כרטיס בגובה 108, תמונה 171×108, gap 24.
אנטומיית כרטיס: row gap 16 — עמודת טקסט (צמודה ימין, space-between אנכי): תג רקע ‎#EEF0EF padding 4px 8px ("gallery event | kikar hamedina" / "gallery event | dizengoff square"; במובייל התג בשתי שורות בלי pipe), כותרת (Copperplate Regular 16 לאנגלית / FbEzmel לעברית), ותאריך dd.mm.yyyy (Copperplate Light 14) או "פרטים ותאריך בהמשך" (FbEzmel Light 14) לאירוע בלי תאריך; ואז תמונה. כל כרטיס = קישור לעמוד האירוע.
דינמיקה: הכרטיסים מרונדרים ב-JS ממירור inline של events.json (file:// לא יכול fetch — תקדים ‎#events-upcoming-data ב-index.html): מסנן date >= היום או date_tbd, ממוין עולה (date_tbd בסוף). כך אירועים שעברו נושרים לבד. נכון להיום צריכים להופיע: alice-debellis (6.8), anat-wegier (7.8), zohar-ron (tbd), amnon-lipkin (tbd) — בדיוק 4 הכרטיסים שבפיגמה; ואם קיים כבר האירוע the-space-between (3.9) — גם הוא.
תמונות: כולן כבר בריפו (images/events/<slug>/) — עשה ls קודם, מחזר עם object-fit:cover; אל תוריד מחדש אלא אם crop הפיגמה שונה מהותית (ל-anat יש crop שונה בין breakpoints — פתור עם object-position).
בסיום: הוסף את העמוד ל-sitemap.xml, שורה ב-CLAUDE.md §4, לינקים ל-FIGMA_LINKS.md, OG/meta מלאים, perf checklist (כלל-זהב 12), git commit, וסכם בעברית.
```

---

### פרומפט 2 — עמוד חדש: press & events `/press/`

```
קרא קודם את CLAUDE.md, docs/conventions.md ו-docs/artist-linking.md. בנה עמוד חדש: press/index.html (route ‎/press/‎) — ארכיון מלא של כל העיתונות והאירועים.
פיגמה (חובה לקרוא את שניהם; שם ה-node הדסקטופי הוא "phone" — שקר, זהה לפי width=1440):
דסקטופ: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1323-244&m=dev
מובייל: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1323-528&m=dev
מבנה: כמו עמוד ‎/events/‎ החדש (אם כבר נבנה — מחזר את ה-CSS): כותרת מוערמת "press" (Bold) / "& events" (Light), 80px פיגמה→~64px בקוד (36→~26 במובייל); דסקטופ פס כותרת ‎#EEF0EF וגריד 2×10 (רוחב 1248, gap 48, כרטיס 600×162, תמונה 292×162); מובייל עמודה אחת 358 (כרטיס 108, תמונה 171×108). אין טאבים ואין סינון — רשימה כרונולוגית אחת (חדש→ישן); ההבחנה press/אירוע היא רק בתג.
19 כרטיסים לפי הפריים הדסקטופי (עמודת ימין ואז שמאל = הסדר הכרונולוגי): anat-wegier (7.8) → risa-and-noemi (24.7) → zohar-ron ("פרטים בהמשך" — לא תאריך! ה-19.7 שבפריים המובייל מיושן) → nir-giorgio-levin (17.7) → liel-salman (16.7) → natasha-zeriker (9.7) → רשת 13 (1.7) → time out מניקור (1.7) → tal nehoray (29.6, כותרת per דסקטופ: "how many partners have you had? with TAL NEHORAY", אין לו עמוד → כרטיס --soon עם טוסט "בקרוב" כמו בהומפייג') → artist-talk גל+אלסה (11.6) → ora magazine (7.6) → close-look טניה שין (2.6, עם אוברליי טקסט על התמונה per הפריים) → the-last-station (27.5) → פתיחת how-many (26.5) → כתובה (25.2 — במובייל הודבקה בטעות כותרת "בדידות...", הנכון: "כְּתוּבָּה | QTUBA") → פתיחת loneliness (19.1) → מגזין פורטפוליו (19.1) → וואלה (5.1) → time out דה-פיינל-קאונטדאון (31.12.25, תג "time out | תרבות" per דסקטופ). מומלץ להוסיף גם את alice-debellis (6.8) במקום הכרונולוגי — חסר בפיגמה כנראה בהשמטה (יש תא ריק בגריד); סמן זאת בסיכום.
תוכן/routes/תמונות: הכל קיים — data/press.json + data/events.json + הכרטיסים הסטטיים בסקשן ‎#press ב-index.html (העתק משם טקסטים ותמונות verbatim; התאם את הכתיב לתיקונים שלמעלה). גוף הכרטיסים = HTML סטטי (כמו ‎#press), press.json נשאר מקור-אמת ל-meta.
עדכון גלובלי: ב-components/site-chrome.js שנה את פריט ה-nav ‏"press & events" מ-‎/#press אל ‎press/‎ (עם abs()), ובדוק שמצב active עובד.
בסיום: sitemap.xml, CLAUDE.md §4 (גם שורת ‎/press/‎ מ-⏳ ל-✅), FIGMA_LINKS.md, OG/meta, perf checklist, בדיקת קישורי אומנים (artist-linking §7), git commit, סיכום בעברית.
```

---

### פרומפט 3 — עמוד חדש: ספונסר soos ‏`/sponsors/soos/`

```
קרא קודם את CLAUDE.md ואת docs/conventions.md (§5 חובה). בנה עמוד חדש: sponsors/soos/index.html (route ‎/sponsors/soos/‎) — עמוד חסות של סטודיו הרמקולים soos.sound ("הקולפן X soos").
פיגמה (חובה שניהם):
דסקטופ: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-3287&m=dev
מובייל: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-3480&m=dev
מבנה דסקטופ: header/footer גלובליים; פאנל ‎#EEF0EF (padding 48px 96px 32px) בשתי עמודות — טקסט משמאל, hero ‏492×744 מימין (כמו משפחת עמודי artist-talk); מתחת לפאנל רצועת גלריה על לבן (4 תמונות, gap 8, גובה ~390, הרביעית צרה יותר). מובייל: hero full-bleed ‏390×520 מתחת ל-header ‏#EEF0EF, ואז סקשן תוכן על לבן; סדר במובייל: צ'יפ → לוקאפ → גוף → גלריה (4 תמונות בשורה קטנה) → קרדיט; ה-divider ‏72×1 ‏#D2D2D2 קיים רק בדסקטופ.
תוכן (verbatim מהפיגמה): צ'יפ ממוסגר "גלריית כיכר המדינה" (קשר ל-‎/#galleries); לוקאפ "הקולפן" (FbEzmel Light 36) + "X" (Copperplate Light 36) + לוגו soos (SVG וקטורי — הורד לפי node-id ‏1323:1013 עם download_figma_images, מידות 88×21.59); גוף 3 פסקאות על soos.sound ודן סרוסי (משוך verbatim מהפיגמה, עברית FbEzmel Light 18/16, מיושר ימין; "soos.sound" בתוך העברית = span לטיני); קרדיט "soos.sound | מודל : Bella" + "www.soos.audio" (קשר ל-https://www.soos.audio, target=_blank).
hero: גם באוברליי על התמונה מופיע הלוקאפ (הקולפן / X / לוגו, ממורכז, לבן, gap 8). scrim: דסקטופ גרדיאנט ‎0deg rgba(0,0,0,.7)→transparent‎ (כהה למטה), מובייל ‎rgba(27,27,27,.4)‎ שטוח.
🔴 חריגת-איות מוכרעת: "soos.sound", "www.soos.audio", "Bella" נשארים lowercase (בפיגמה textCase:LOWER מפורש — מותג) — מימוש עם מחלקת text-transform:none נקודתית; כל שאר האנגלית UPPERCASE כרגיל.
תמונות: hero = imageRef ‎69c2a352…‎ (הורד + וריאנטים srcset per כלל-זהב 12); גלריה = ‎6c1a982a…‎ (crop), ‎86f9f41d…‎, ‎2bf4f9cc…‎ (crop), ‎7439af16…‎. רנדר את ה-hero node לוודא שאין שכבות מוסתרות. שמור ב-images/sponsors/soos/. יש בפריים המובייל frames ריקים (1318:3523 ועוד) — שרידי תבנית, לא לבנות.
דאטה: הוסף רשומת meta ל-data חדש sponsors.json (id, slug, name, figma nodes) — הגוף נשאר ב-HTML (תקדים כתבות long-form).
בסיום: sitemap.xml, CLAUDE.md (§4 שורה + §6 contract חדש), FIGMA_LINKS.md, OG/meta, perf checklist, git commit, סיכום בעברית.
```

---

### פרומפט 4 — עמוד אירוע חדש: The Space Between ‏`/events/the-space-between/`

```
קרא קודם את CLAUDE.md (כולל הסעיף "משפחת עמודי האירוע artist talk") ואת docs/conventions.md. בנה עמוד אירוע חדש: events/the-space-between/index.html — ‏"The Space Between — a conversation about art, materials and human experience", ערב הרצאה עם מור צופיה געש (מעצבת פנים אורחת — לא אומנית של האתר, אין לקשר לדף אומן), 3.9.2026 יום חמישי, גלריית כיכר המדינה.
פיגמה (חובה שניהם):
דסקטופ: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1361-434&m=dev
מובייל: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1361-232&m=dev
תבנית: משפחת artist-talk (בסיס natasha-zeriker) אבל בלי LINGER, בלי פס "presented as part of" (אין שיוך תערוכה — קונטיינרי התערוכה בפיגמה ריקים בכוונה), בלי רצועת אומנים ובלי הערת הרשמה. ייחודים: כותרת אנגלית 4 שורות (Copperplate; 80px פיגמה→~64px בקוד, אוברליי 38.5→~30, מובייל 30→~22); הגוף העברי ממורכז (CENTER — לא מיושר ימין כמו שאר המשפחה); השעות בתוך הגוף (19:30 התכנסות וכוס יין / 20:00 הרצאה...), לא בשורת המטא; מטא = גלריה + "3 ספטמבר 2026 · יום חמישי" (דסקטופ 28px עם נקודת מפריד, מובייל 14 בלי נקודה); בלוק כתובת Copperplate בסוף. משוך את כל הטקסטים verbatim מהפיגמה.
🔴 hero: תמונה אחת לשני ה-breakpoints — imageRef ‎8ad5c38a…‎ (מקור 2268×4033, מור בגלריה). בפיגמה שכבות ה-scrim שקעו בטעות מתחת לתמונה — ממש לפי קונבנציית המשפחה אבל בכיוון הנכון לכותרת-עליונה: דסקטופ linear-gradient(180deg, rgba(0,0,0,.8), transparent) (כהה למעלה), מובייל rgba(27,27,27,.4) שטוח. ה-fill הנוסף בהירו הדסקטופי (‎d64bdef…‎ = ההירו של zohar-ron) הוא leftover מוסתר — להתעלם.
חיווט: רשומה חדשה ב-data/events.json (id: the-space-between, date: 2026-09-03, gallery_id: medina, card_title_en, כל השדות לפי החוזה); הוסף את האירוע לעמוד ‎/events/‎ (אם קיים — למירור ה-inline שלו); הוסף כרטיס בראש עמוד ‎/press/‎ אם קיים (תג "gallery event | kikar hamedina"); אל תוסיף לסקשן ‎#press בהומפייג' (per ההנחיה החדשה שם מופיעות רק כתבות + 2 פתיחות).
בסיום: sitemap.xml, CLAUDE.md §4, FIGMA_LINKS.md, OG (og/events-the-space-between-hero.jpg), perf checklist, git commit, סיכום בעברית.
```

---

### פרומפט 5 — הומפייג': סקשן הבשמים (עדכון + בושם חדש)

```
קרא קודם את CLAUDE.md ואת docs/conventions.md. עבודה על index.html (Re-Read לפני עריכה — קובץ shared). מקור: פריים המובייל החדש של עמוד הבית — https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-363&m=dev (סקשנים 1318:599 ו-1318:1169). זהו עיצוב מובייל — עצב דסקטופ בעצמך בהתאמה לשפה הדסקטופית הקיימת של האתר (הסקשן הנוכחי ‎#perfume-promo דו-עמודתי — אפשר לשמר את הרוח).
משימה 1 — עדכון הסקשן הקיים ‎#perfume-promo (בושם how many): החלף את גלריית 5 ה-thumbs בתמונה אחת חדשה — imageRef ‎69ac0bc6823efb31b30040cc5e94e519790dfc17‎ (crop ‎af2d6c‎; הורד כקובץ חדש ל-images/homepage/perfume-promo/, אל תדרוס את perfume-1..5 הקיימים). טקסטים (מובייל, ממורכז): "new perfume" (Copperplate Bold 36→~26 בקוד) / "בושם הנושא של תערוכת" (FbEzmel Light 20) / "HOW MANY PARTNERS HAVE YOU HAD?" (Copperplate Light 20→~16). כפתור ממוסגר (stroke ‎#1B1B1B 1.4px, padding 16px 24px) "עוד על הבושם באתר" → הקישור הקיים ל-zrp.co.il.
משימה 2 — סקשן חדש: בושם "סבלנות" (הקולפן), מיד אחרי הראשון, אותה תבנית: תמונה imageRef ‎922a369f9b3c81015f5b66e2c05f3d1a42d39cf3‎ (crop ‎53b863‎, הורד ל-images/homepage/perfume-promo/); טקסטים ממורכזים: "new perfume" / "סבלנות" (FbEzmel Regular 20 — שם הבושם) / "בושם הנושא של תערוכת הקולפן" (Light 20) / שורת "EXHIBITION • VOLUME 2" (Copperplate Light 20→~16, נקודה 4px ביניהם); ואז קו 32×1 ‎#1B1B1B ומתחתיו "בלעדי לרכישה בגלריה בכיכר המדינה" (FbEzmel Light 18) — 🔴 בלי כפתור ובלי קישור רכישה (אין לבושם עמוד באתר הבישום). "הקולפן" בטקסט = קישור ל-exhibitions/the-peeler/ (וכל אזכור אומן אם יהיה = קישור).
עדכן את בלוק ה-data ב-data/homepage.json (הוסף מבנה דקלרטיבי לשני הבשמים ברוח big_news). וריאנטים/srcset לכל תמונה per כלל-זהב 12.
בסיום: עדכן CLAUDE.md §4 (שורת ה-homepage), git commit, סיכום בעברית.
```

---

### פרומפט 6 — הומפייג': החלפת סקשן upcoming events

```
קרא קודם את CLAUDE.md ואת docs/components.md. עבודה על index.html (Re-Read לפני עריכה). מקור: פריים המובייל של ההומפייג' — https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-363&m=dev (סקשן 1318:476). עצב דסקטופ בעצמך בהתאמה לשפת האתר.
משימה: החלף לגמרי את הסקשן ‎#events-upcoming הקיים (הכותרת המעגלית upcoming-events-circle.svg + קרוסלת הלופ + החיצים + הרנדרר) בעיצוב החדש:
1) כותרת מוערמת "upcoming " (Copperplate Bold 58→~46 בקוד) מעל "events" (Light 91→~72), חפיפה קלה (gap שלילי) — הכותרת קישור ל-‎events/‎.
2) שני כרטיסי פוסטר זה-לצד-זה (מובייל: gap 8, גובה ~301; דסקטופ: גדולים יותר לפי שיקולך) — אלו "הרשימות": תמונות פוסטר מעוצבות שהמעצבת מתחזקת ידנית. 🔴 לפני מימוש חובה לרנדר את nodes ‏1318:482 ו-1318:3259 כ-PNG (ה-text-wrappers שלהם ריקים — הטקסט אפוי בתמונה): הורד את תמונות הפוסטר (imageRefs ‏1d4da191…, 2000bf6f…, רקע 54207a94…) ל-images/homepage/upcoming/, object-fit לפי scaleMode (FIT=contain). שני הכרטיסים = קישור ל-‎events/‎ (הנחיית המעצבת: לחיצה על הרשימות/כותרת מובילה לעמוד האירועים הקרובים, לא לעמוד אירוע ספציפי).
3) כפתור ממוסגר "view all" (Copperplate Light 16, stroke שחור 1px, padding 4px 16px) → ‎events/‎.
נקה: הסר את script ה-JSON ‏#events-upcoming-data ואת ה-IIFE של הקרוסלה (ודא שאין שימוש אחר בהם); את הקבצים בדיסק (SVG, תמונות ישנות) השאר (כלל-זהב 8). הסר את מנגנון ה-hidden (הסקשן כבר לא תלוי-תאריכים).
בסיום: עדכן CLAUDE.md §4, git commit, סיכום בעברית.
```

---

### פרומפט 7 — הומפייג': big news בעיצוב חדש

```
קרא קודם את CLAUDE.md ואת docs/conventions.md. עבודה על index.html (Re-Read לפני עריכה). מקור: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-363&m=dev (סקשן 1318:583). עצב דסקטופ בעצמך (טיפוגרפיה מוגדלת, אותו רוח).
משימה: החלף את הסקשן ‎#big-news הקיים (טקסט+תמונה+טבעת BIG) בעיצוב החדש — טקסט בלבד, ממורכז, על לבן: "big news" (Copperplate Bold 36→~26 בקוד, UPPERCASE) / "פתחנו לכם נקודת\nמכירה נוספת!" (FbEzmel Regular 36) / "חנות חדשה בתוך הגלריה" (FbEzmel Light 24) / "כיכר המדינה, רח׳ ז׳בוטינסקי 131, תל אביב" (FbEzmel Light 18, קישור ל-‎#galleries — כמו היום). בלי תמונה, בלי SVG טבעת, בלי scrim. הסר את ה-markup הישן; את קבצי images/homepage/big-news/ השאר בדיסק (כלל-זהב 8). עדכן את בלוק big_news ב-data/homepage.json שישקף את התוכן החדש (אין יותר שדות תמונה).
בסיום: עדכן CLAUDE.md §4, git commit, סיכום בעברית.
```

---

### פרומפט 8 — הומפייג': the art works — גריד שחמט + curator

```
קרא קודם את CLAUDE.md ואת docs/conventions.md. עבודה על index.html (Re-Read לפני עריכה). מקור: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-363&m=dev (סקשן 1318:560). עצב דסקטופ בעצמך בהתאמה לשפה הדסקטופית.
משימה: החלף את סקשן ‎#artworks הקיים (שורות aw-row מתחלפות) בגריד שחמט 2×3 (מובייל: תאים ~179×179): תא-1 תמונה (imageRef ‎2baf9d2e…‎, object-fit contain על רקע לבן) | תא-2 טקסט "the" (Copperplate Bold 36→~26) | תא-3 טקסט "ART works" בשתי שורות (Bold, ממורכז) | תא-4 תמונה (‎3f0a517d…‎) | תא-5 תמונה (‎99bbf47b…‎) | תא-6 "more" (Copperplate Light 36) + חץ chevron → ‎works/‎. לפני הורדת תמונות עשה ls — ‏‎3f0a517d…‎ כנראה כבר קיים בריפו (hero של natasha); הורד רק חסרות ל-images/homepage/artworks/ עם וריאנטים.
מתחת — בלוק curator חדש (מחליף את ‎.aw-curator): ממורכז, "the curator" (Copperplate Bold 36→~26) / "korin avraham" (Light 36) / כפתור ממוסגר "read more" (Light 16, stroke שחור 1px, padding 4px 16px) → ‎curators/korin-avraham/‎.
את תמונות ה-tiles הישנות (tile-*.webp) השאר בדיסק. דסקטופ: אותו שחמט ברוחב מלא (למשל 3×2 או 2×3 מוגדל) — שיקולך, שמור על ה-casing הגלובלי.
בסיום: עדכן CLAUDE.md §4, git commit, סיכום בעברית.
```

---

### פרומפט 9 — הומפייג': x our artists — קרוסלת פוקוס

```
קרא קודם את CLAUDE.md ואת docs/components.md (כלל-זהב 11 — לא לבנות קומפוננטה קיימת בלי לבדוק). עבודה על index.html (Re-Read לפני עריכה). מקור: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-363&m=dev (סקשן 1318:695). עצב דסקטופ בעצמך.
משימה: החלף את סקשן ‎#x-our-artists הקיים (גריד 38 בדסקטופ / קרוסלה+נקודות במובייל) בקרוסלת פוקוס: כותרת "Zielinski Rozen" (Copperplate Bold 36→~26; ירונדר UPPERCASE לפי הכלל הגלובלי) + "X our artists" (Light 36). גוף: יצירה מרכזית גדולה (מובייל ~219×331, cover) עם כיתוב שם האומן מתחתיה (Copperplate Light 16, אפור ‎#989898), ומשני צדדיה הצצות של היצירות השכנות (~136×204, opacity 0.6, השמאלית זולגת מחוץ למסך) עם כיתובים. אינטראקציה: swipe במובייל וחיצים/גרירה בדסקטופ שמזיזים את הפוקוס; מקור הנתונים נשאר data/homepage.json x_our_artists (כל 38 הפריטים, images/homepage/x-artists/work-N) — הפיגמה מראה מצב התחלתי בלבד (nir giorgio levin במרכז, zohar ron/gilad kenan בצדדים). 🔴 כל כיתוב שם-אומן = קישור לדף האומן (docs/artist-linking.md — חובה). שמור נגישות (aria) וביצועים (טעינה עצלה לתמונות הלא-נראות).
בסיום: עדכן CLAUDE.md §4, git commit, סיכום בעברית.
```

---

### פרומפט 10 — הומפייג': סקשן press & events — צמצום ל-9 + כפתור

```
קרא קודם את CLAUDE.md ואת docs/conventions.md. עבודה על index.html (Re-Read לפני עריכה). מקור: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-363&m=dev (סקשן 1318:777). עצב דסקטופ בעצמך (מומלץ: אנטומיית הכרטיס של עמוד ‎/press/‎ החדש — כרטיס 600×162 בשתי עמודות).
רקע: קורין ביקשה שבהומפייג' יופיעו תמיד כל כתבות העיתונות + שני אירועי הפתיחה בלבד; שאר האירועים עברו לעמוד ‎/press/‎ החדש.
משימה: החלף את גריד 19 הכרטיסים בסקשן ‎#press ב-9 כרטיסים בעיצוב החדש — כרטיס-שורה: תג chip (רקע ‎#EEF0EF) + כותרת + תאריך (צמודים ימין) + תמונה 171×108 (מובייל, עמודה אחת gap 24). הרשימה (חדש→ישן, verbatim מהפריים): 1 רשת 13 (1.7 → press/peeling-a-layer/) 2 time out מניקור (1.7 → press/manicure-against-darkness/) 3 ora magazine (7.6 → press/the-sixth-scent/) 4 time out התחנה האחרונה (27.5 → press/the-last-station/) 5 אירוע פתיחת how many (26.5 → events/how-many/, כותרת "HOW MANY PARTNERS HAVE YOU HAD?" Copperplate) 6 אירוע פתיחת loneliness — "בדידות בתוך סביבה תוססת" (19.1 → events/loneliness/) 7 מגזין פורטפוליו (19.1 → press/press-1/) 8 וואלה (5.1 → press/walla/) 9 time out דה פיינל קאונטדאון (31.12.25 → press/time-out/, תג "time out | תרבות"). טקסטים ותמונות — מחזר מהכרטיסים הקיימים בסקשן (הם כבר בריפו).
מתחת לרשימה: כפתור ממוסגר ממורכז "more press & events" (Copperplate Light 16, stroke שחור 1px, padding 4px 16px) → ‎press/‎.
עדכן homepage_visible ב-data/press.json (true רק ל-9 האלה) ואת item_ids ב-data/homepage.json. שים לב: העוגן ‎#press חייב להמשיך להתקיים (קישורי nav ישנים/חיצוniyים מפנים אליו עד שינוי ה-nav).
בסיום: עדכן CLAUDE.md §4, git commit, סיכום בעברית.
```

---

### פרומפט 11 — הומפייג': סקשן חדש "הקולפן X soos"

```
קרא קודם את CLAUDE.md ואת docs/conventions.md. עבודה על index.html (Re-Read לפני עריכה). מקור: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-363&m=dev (סקשן 1318:316). עצב דסקטופ בעצמך (רוח סקשן tribe-teaser — ממורכז).
משימה: בנה סקשן הומפייג' חדש (id מוצע: ‎#soos) — חסות סטודיו הרמקולים soos: לוקאפ ממורכז "הקולפן" (FbEzmel Light 36) / "X" (Copperplate Light 36) / לוגו soos (SVG, ‏88×21.59 — אם עמוד ‎/sponsors/soos/‎ כבר נבנה מחזר את images/sponsors/soos/logo.svg, אחרת הורד מ-Figma node ‏1323:1013); שורות קרדיט ממורכזות: "soos.sound | מודל : Bella" ו-"www.soos.audio" (Copperplate Light 16 + FbEzmel; 🔴 חריגה מוכרעת: soos.sound / www.soos.audio / Bella נשארים lowercase — מחלקת text-transform:none נקודתית); רצועת 3 תמונות (gap 4, ~100×121 במובייל) — imageRefs ‏6c1a982a… (crop), ‏86f9f41d…, ‏2bf4f9cc… (crop) — משותפות לעמוד הספונסר, מחזר אם קיימות; כפתור ממוסגר "read more" (Copperplate Light 16, stroke שחור 1px) → ‎sponsors/soos/‎. "הקולפן" בלוקאפ = קישור ל-exhibitions/the-peeler/. מקם זמנית אחרי ‎#galleries (המיקום הסופי ייקבע בפרומפט ה-reorder).
בסיום: עדכן CLAUDE.md §4, git commit, סיכום בעברית.
```

---

### פרומפט 12 — הומפייג': סדר סקשנים חדש + סנכרונים + חיווט סופי

```
קרא קודם את CLAUDE.md (כולל שורת ה-homepage ב-§4) ואת docs/lessons.md. עבודה על index.html (Re-Read לפני עריכה). מקור: https://www.figma.com/design/XhGH289YTRcW811wrufRJz/landing?node-id=1318-363&m=dev. הנחת עבודה: הסקשנים החדשים (בשמים×2, upcoming, big-news, artworks, x-our-artists, soos, press-9) כבר נבנו בפרומפטים קודמים.
משימה 1 — reorder: סדר את סקשני ה-body לסדר היעד: hero → announcement → קול קורא (mobile-cta/opencall) → ‎#exhibitions-now (+רצועת our artists) → ‎#perfume-promo (how many) → בושם "סבלנות" → ‎#events-upcoming החדש → ‎#big-news → ‎#artworks → ‎#x-our-artists → ‎#galleries → ‎#soos → ‎#tribe-teaser → ‎#exhibitions (ארכיון) → ‎.social (אינסטגרם) → ‎#press → footer. ודא שה-CSS לא תלוי-סמיכות (סלקטורים כמו +/~) ושהעוגנים ‎#exhibitions/‎#galleries/‎#press ממשיכים לעבוד מה-nav.
משימה 2 — סנכרון סקשנים שזזו, מול הפריים: (א) ‎#tribe-teaser — כותרת "loneliness in a bubbling environment" (Bold 36→~26) + "X the tribe" (Light 36), שורת "sponsored by" + לוגו tribe (imageRef ‏b65146f9…, ‏95×10 — רנדר/השווה מול הלוקאפ הקיים sponsored-by-moet.webp לפני החלפה; אם שונה — קובץ חדש), שמות האומנים מופרדים ב-| — כל שם = קישור לדף האומן (artist-linking!), רצועת 5 תמונות (fills מרובי-שכבות — רנדר nodes לפני הורדה), בלי כפתור. (ב) ‎#exhibitions (ארכיון) — כותרת מוערמת "exhibitions" (Bold 58→~46) / "archive" (Light 91→~72); בכרטיס: "exhibition volume 1" + "בדידות בתוך סביבה תוססת" (🔴 בפיגמה חסר "בתוך" — טעות מוכרעת, לא לשחזר) + תג "גלריית כיכר המדינה". (ג) ‎.social (אינסטגרם) — ודא התאמה: כותרת "follow us on instagram", חיצים, רצועת thumbs (המבנה הקיים קרוב — עדכן רק אם יש פער מהותי). (ד) ‎#exhibitions-now — השאר את רוחבי הכרטיסים השווים (הכרעת משתמש 2026-07-26 גוברת על ה-177+fill שבפריים).
משימה 3 — חיווט: ודא שה-nav (site-chrome.js) מפנה "press & events" → ‎press/‎ (אם טרם שונה); בדוק את כל דפי האתר שהקישור מתעדכן בהם (הקובץ גלובלי — שינוי אחד). עדכן: שורת ה-homepage ב-CLAUDE.md §4 (תיאור מצב חדש מלא), FIGMA_LINKS.md (node ‏1318-363 כפריים ההומפייג' העדכני), docs/lessons.md אם נלמד לקח.
בדיקות סיום: פתיחה ב-file:// וב-HTTP, שני breakpoints, אין overflow-x על body, perf checklist לכל תמונה חדשה, git commit, סיכום בעברית.
```

---

## ד. סטטוס ביצוע

| # | משימה | סטטוס |
|---|---|---|
| 1 | עמוד ‎/events/‎ | ⏳ |
| 2 | עמוד ‎/press/‎ + nav | ⏳ |
| 3 | עמוד ‎/sponsors/soos/‎ | ⏳ |
| 4 | עמוד ‎/events/the-space-between/‎ | ✅ 2026-08-04 — הדף + `events.json` (שדות חדשים `day_he`/`host_he`) + `press.json` (`homepage_visible:false`) + sitemap + OG + שורת CLAUDE.md §4. **בנוסף (מחוץ לפרומפט):** רשומה ב-`#events-upcoming-data` (הקרוסלה הנוכחית) — בקשת משתמש לקישור מההומפייג'; פרומפט 6 שמחליף את הסקשן יכול למחוק אותה בבטחה (האירוע יופיע ב-`/events/`). כרטיס `/press/` ממתין לפרומפט 2 (רשומת ה-meta כבר ב-`press.json`). |
| 5 | בשמים (עדכון + חדש) | ⏳ |
| 6 | upcoming section חדש | ⏳ |
| 7 | big news חדש | ⏳ |
| 8 | the art works שחמט | ⏳ |
| 9 | x our artists קרוסלת פוקוס | ⏳ |
| 10 | press-9 + כפתור | ⏳ |
| 11 | סקשן soos בהומפייג' | ⏳ |
| 12 | reorder + סנכרונים + חיווט | ⏳ |
