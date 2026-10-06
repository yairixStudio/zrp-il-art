# Homepage — route notes

> **לקרוא לפני עריכה של:** `index.html` (route `/`), `images/homepage/**`, `data/homepage.json` — וגם לפני שינוי בכרטיס-הומפייג' שנגזר מ-`press.json` / `galleries.json` / `works.json :: works[]`.
> מצב נוכחי + כללים פעילים. היסטוריה: `docs/history/CLAUDE-2026-09-27.md` §4 (שורת `/`). פרטי הרה-דיזיין: `docs/redesign-2026-08.md`. קישורי Figma: `FIGMA_LINKS.md` (כותרות "Homepage — …"). ⚠️ שם, רשומה נוכחית מסומנת "✅ המצב הנוכחי" בכותרת **או** בהערה בגוף ("(עיצוב נוכחי …)" / "(מקור ל-layout בלבד …)"); "legacy" = מיושן. ה-nodes של 2026-09-27 (`1873:1146`, `1124:819`/`1318:418`, `1873:1074`/`1738:347`, `1877:1101`) עדיין לא נוספו שם. בכל סתירה — ה-node שמופיע בסקשן כאן גובר.

## Page

- `/` → `index.html` · Figma desktop `XhGH...::144:317` (older `Zn3N...::1213:3093`) · Figma mobile `XhGH...::144:2` (ב-`FIGMA_LINKS.md` מסומן legacy — המקור הסמכותי כיום `1318:363`; older `Zn3N...::1213:3360`) · ✅
- 🔴 **מאז רה-דיזיין אוגוסט (הושלם 2026-08-05, כל 12 המשימות) המקור הסמכותי = פריים המובייל `XhGH...::1318:363` "homepage-mobileNew"; הדסקטופ = אדפטציה — חוץ מסקשן שמצוטט כאן עם פריים דסקטופ מפורש, ושם הפריים מחייב** (למשל `#exhibitions-now` `1124:819`, `#artworks` `1124:988` (layout בלבד) / `1124:1003` (curator), `#galleries-berlin` `1859:2668`, `#tribe-teaser` `250:87`, `#exhibitions` `1124:947`, `#opencall` `1124:792` (תיבות תמונה 4:5 — הכרעת משתמש, ראה הסקשן), `.social` `144:431`; `#events-upcoming` `1873:1074` — פוסטרים בלבד, ראה הסקשן). פריימים ישנים שמשמשים חלקית: `homepage-desktop 1124:754` / `homepage-mobile 1124:21` (רק איפה שמצוין).
- ⚠️ כמה nodes בתוך `1318:363` נקראים "Exhibitions Archive" — **השם משקר**; לזהות לפי תוכן.

## Shared rules

### סדר הסקשנים (מאומת בקוד)
hero → `.announce` → `#mobile-cta` (מובייל) / `#opencall` (דסקטופ) → `#exhibitions-now` → `#perfume-promo` → `#perfume-savlanut` → `#events-upcoming` → `#big-news` → `#artworks` → `#x-our-artists` → `#galleries` → `#galleries-berlin` → `#sumii` → `#soos` → `#tribe-teaser` → `#exhibitions` (ארכיון) → `.social` → `#press` → `<site-footer>`.

### דאטה
- **כל הדף = HTML סטטי שנכתב ידנית.** `data/homepage.json` = composition layer **דקלרטיבי בלבד** (אין `fetch`). כל שינוי תוכן = לערוך את ה-HTML **וגם** לעדכן ידנית את הבלוק ב-`homepage.json` ואת ה-JSON המקורי (`press.json` / `galleries.json` / `works.json`).
- `python3 tools/sync_data.py` **לא נוגע ב-`index.html`**. מריצים אותו (ואז `--check`) אחרי עריכת כל JSON שהוא מנהל — `galleries.json` (מירורי `#fallback-galleries` בדפי הגלריה ובעמוד האוצרת), `works.json`, `artists.json`, `exhibitions.json` (`data/generated/ex-order.js`).
- ⚠️ **drift ידוע (נבדק 2026-09-27) — ה-HTML גובר**; ב-`homepage.json` מיושנים: `hero` (`description_he`, `image: hero.webp`), `x_our_artists.figma_node_desktop` / `figma_node_mobile` (`412:334` / `640:249`), `soos_sponsor.credit_line` (סדר ישן), `tribe_teaser._note` ("thumb-5 = duplicate" — כבר יש `video.mp4` ו-thumb-5 שונה). לא לשחזר HTML מהם.
- ⚠️ הערות-קוד מיושנות ב-`index.html` — הערת ה-CSS של `#press` וההערה שלפני `<section class="press">` ("9 static cards", "1-5 / 6-10"; בפועל 13, `repeat(7,auto)` — ההערה שבתוך הסקשן כבר נכונה), CSS של `#artworks` ("`<picture media>`"), `.sumii-gname` ("23px"; בפועל 24), CSS של `#x-our-artists` ("38 slides"; בפועל 39; הכותרת "`228:67` / `228:101`" וגם "Figma 228:101" במובייל), כותרות CSS/HTML של `#exhibitions-now` + הערות ה-CSS שלו ("`237:1285` / `237:935`", "`237:1290`"; בפועל `1124:819` / `1318:418`), כותרות CSS/HTML של הארכיון ("`474:97` / `467:45`"; בפועל `1124:947` / `1318:487`); ובבלוק `≤768` כללי `.opencall-*` מתים (הסקשן `.only-desktop`, מוסתר ב-`≤768`). הקוד והמסמך הזה גוברים.

### עוגנים שחייבים לשרוד (לא לשנות id בלי לעדכן את המפנים)
- `#opencall` (דסקטופ) + `#mobile-cta` (מובייל) — פריט הניווט "open call" ב-`components/site-chrome.js` (`syncOpenCallHref`: `≤768` → `#mobile-cta`, אחרת `#opencall`) + `404.html` (`/#opencall`).
- `#exhibitions` (הארכיון `.ex-archive`) — פריט הניווט "exhibitions" ב-`site-chrome.js` + `404.html` (`/#exhibitions`).
- `#galleries` — פריט הניווט "the galleries", "גלריית שוק הפשפשים" בפוטר, `/#galleries` מדפי האומנים והיצירות, דפי הגלריות, עמוד האוצרת, הצ'יפ ב-`sponsors/soos/`, הכתבה `press/manicure-against-darkness/` וכתובת `#big-news`. משמש בפועל כאינדקס הגלריות (אין `/galleries/`).
- `#press` — נשמר (הכרעה). ה-nav "press & events" → `press/`, לא לעוגן.
- `#x-our-artists` (+ `.xa-prev`/`.xa-next`) ו-`#igTrack` (+ `.ig-prev`/`.ig-next`) — נקראים ע"י הסקריפטים inline בתחתית `index.html` (חיצי הקרוסלה, קרוסלת האינסטגרם). 🔴 סקריפט האינסטגרם תופס את `.ig-prev`/`.ig-next` **הראשונים בדף** (`document.querySelector`) — לא לתת את המחלקות האלה לכפתורים בסקשן אחר (לכן בקרוסלת האומנים `.xa-prev`/`.xa-next`; רק העטיפה `.ig-nav` משותפת).

### טיפוגרפיה ורספונסיב
- Breakpoint ראשי: מובייל `≤768` / דסקטופ `≥769`; נוספים `≤1199`, `≤1100`, `≤400`.
- Copperplate שלנו רחב מזה של Figma ⇒ **כיול אופטי ללטינית** (ערכים בכל סקשן). **עברית (FbEzmel) = px של Figma verbatim. גליף בודד (`X`) = verbatim.**
- `<br class="mbr">` = שבירה שמוצגת רק ב-`≤768`.
- **Solway** (`--sol`, `@font-face` Light בלבד) — **רק** לפס `EXHIBITION • VOLUME 1` (Figma `1877:1101`) בכרטיס הארכיון (הוחזר 2026-09-27; לא להסיר).
- font-size ≥48px במובייל → `clamp()` + בדיקת רוחב מילה מול 320px. `overflow-x` רק על `html`, **אסור על `body`** (שובר sticky header, חותך צמרות Copperplate) — `docs/lessons.md` 2026-05-11/06-15/06-16. ⚠️ ב-CSS של `index.html` עדיין יש legacy `body{…overflow-x:clip…}`, מנוטרל בזמן ריצה ע"י `site-chrome.css` (`body:not(.menu-open){overflow-x:visible !important}`) — לא להוסיף עוד; אם נוגעים — לתקן במקור.
- אחרי שינוי layout/טיפוגרפיה — לוודא שכותרות Copperplate caps (`line-height ≤1.2`) לא נחתכות מלמעלה.
- כל אזכור אומן = קישור (רצועת האומנים, כיתובי הקרוסלה, קרדיטי tribe) — `docs/artist-linking.md`.

### קומפוננטות ותמונות
- בשימוש: `.tri` (`#x-our-artists`, `#mobile-cta`), `artwork-lightbox` (`#tribe-teaser`). `stacked-gallery` כבר לא נטען בהומפייג' (חי רק בגלריית המובייל של `opencalls/<slug>/`). לא לבנות חלופות — `docs/components.md`.
- `picture-upgrade.js` **מדלג על `<img>` שכבר בתוך `<picture>`** — שם כל `<source>` AVIF נכתב ידנית. ⚠️ פער קיים: כרטיסי `#galleries` / `#galleries-berlin` עטופים ב-`<picture>` **בלי** `<source>` AVIF ⇒ מוגשים WebP בלבד (קבצי ה-avif קיימים). בנגיעה בהם — להוסיף `<source type="image/avif" srcset=… sizes=…>` ידני, או להסיר את ה-`<picture>` המיותר כדי ש-`picture-upgrade.js` יעטוף.
- קבצים שהוחלפו נשארים בדיסק לא-מקושרים (כלל-זהב 8); גרסה חדשה = קובץ `-vN`, לא דריסה.

### אימות
- בדיקה ויזואלית **רק דרך http** (`python3 -m http.server`, ב-`.claude/launch.json`) — ב-file:// כרום חוסם `@font-face`.
- ⚠️ headless Chrome במק לא יורד מרוחב חלון 500 — צילום ישיר ב-390 נחתך ומטעה; לצלם 390 דרך iframe.
- שינוי שמוגבל ל-`index.html` (CSS/markup/IIFE בתוך הקובץ) שנוגע בכמה סקשנים: `node tools/regress/snapshot.mjs --label before --only index.html` → שינוי → `node tools/regress/snapshot.mjs --label after --only index.html` (**אותו `--only` ואותו `--widths` בשתי הריצות** — `diff.mjs` סופר עמוד שקיים רק בסנפשוט אחד כהבדל) → `node tools/regress/diff.mjs before after`. בעבודת layout/טיפוגרפיה — `--widths 390,1024,1366,1440` (ברירת המחדל 390,1440 לא רואה את בלוקי 769–1100 / 769–1199). שינוי שאמור לשנות פלט ⇒ diff יוצא 1 — לקרוא אותו ולוודא שרק הסקשנים/האלמנטים המכוונים השתנו.
- 🔴 שינוי בקובץ תחת `components/` (`triptych-gallery`, `site-chrome`, `picture-upgrade`, `artwork-lightbox`) — גם אם הסיבה היא ההומפייג', הם נטענים בדפים רבים ⇒ להריץ **בלי `--only`** (כל הדפים).
- בסיום: `python3 tools/seo/refresh_sitemap_lastmod.py`.

## hero
- `h1` "THE ART GALLERIES" / `h2` "ZIELINSKI & ROZEN"; תמונה `images/homepage/hero-landscape.webp` 1320×1095 + srcset = ה-LCP (`fetchpriority="high"`), עטופה בקישור → `about/`. (הערת Figma בקוד: `landing::144:343` / `144:24`.)
- `.hero-desc` = הביו של ארז ("…רוקח בשמים ואוצר תרבות…"), המותג ב-`<span class="lat">`.
- `.hero-more` — כפתור ממוסגר **"read more" → `about/`, מובייל בלבד** (`display:none` בדסקטופ). ה-`scroll-prompt` הוסר (2026-08-28).
- ⚠️ unverified: מקור ה-Figma של שינוי ההירו מ-2026-08-28 לא תועד (`docs/todo.md`).

## announcement / #mobile-cta / #opencall
- **`.announce`** — marquee **"קול קורא חדש באוויר !"** (בקשת משתמש 2026-09-27; Figma מובייל `landing::1318:397`. בפריים הדסקטופ `1124:789` עדיין הנוסח האנגלי הישן — באתר העברית בכל ה-breakpoints). מקור הטקסט: `site.json :: announcement` (+ `#fallback-site` בשני דפי הקול הקורא).
  - modifier `.announce.announce--he`: FbEzmel Regular **20px verbatim בכל ה-breakpoints**, line box 22, padding 32 (פס 86px), `letter-spacing:0`; הספציפיות (0,2,0) גוברת על כללי ה-`.announce` (13/12px, padding 20) בבלוקי `≤768`/`≤400`. פריטים `<span class="announce-item heb">` (RTL — ה-"!" בקצה השמאלי); כיוון הגלילה לא השתנה (שמאלה). `prefers-reduced-motion`: פריט סטטי יחיד ממורכז.
  - 🔴 **20 פריטים זהים — לא לצמצם:** הלופ מזיז את ה-track עד `translateX(-50%)`, ולכן חצי track חייב להיות ≥ רוחב המסך, אחרת בסוף כל מחזור נפער פס ריק. פריט ≈171.7px + gap (96 דסקטופ / 48 מובייל) ⇒ חצי track ≈2677px / 2197px. המשכים 63s דסקטופ / 52s מובייל (כלל `≤768`) שומרים על ≈42px/s של קודם.
  - **החלפת טקסט** = 20 ה-spans + `aria-label` + `site.json` + שני ה-`#fallback-site`; אורך אחר ⇒ לחשב מחדש מספר פריטים ומשכים. טקסט אנגלי ⇒ להסיר את `announce--he` (הסגנונות האנגליים נשארו ב-`.announce`; 6 הפריטים הישנים הספיקו למחרוזת האנגלית הארוכה, אם כי חצי ה-track שלה, 1706px, כבר השאיר פס ריק במסכים רחבים מ-~1706px).
- **`#mobile-cta`** (מובייל בלבד; Figma `landing::1318:401`, מחליף את `144:38`): "קול קורא" + separator + קרוסלת 3 הקולות הקוראים על `.tri` המשותף (`components/triptych-gallery.*`) — החליפה את `stacked-gallery`, שכבר לא נטען בהומפייג'.
  - סדר DOM חדש→ישן: obsession (שקופית 0, `data-tri-start="0"` ⇒ במרכז בטעינה) · the-peeler (peek ימני) · how-many (peek שמאלי).
  - גאומטריה verbatim: במה 380.05px, full-bleed (`.mobile-cta .tri{margin:0 -16px}` — ה-peeks בפריים נמשכים עד קצות המסך); מרכז 234.58×292.05, peeks 147.91×184.15, כולם ממורכזים אנכית; gaps 31.09 (שמאל) / 31.42 (ימין) ⇒ `--tri-peek-left:calc(50% - 222.335px)` / `--tri-peek-right:calc(50% + 222.665px)`; peeks בלי עמעום (`opacity:1`); בלי dots. נבדק מול רינדור הפריים ב-390: מיקומים בטווח 0.3px.
  - טאפ על peek / swipe / חיצי מקלדת = סיבוב; טאפ במרכז = ניווט דרך `<a>` שעוטף את ה-img (`<a href="opencalls/<slug>/"><img class="tri-slide"></a>`, הדפוס של `events/close-look`). כולל obsession (`opencalls/obsession/`).
  - 🔴 **wrap עם 3 שקופיות בדיוק:** בכל סיבוב שקופית אחת עוברת peek→peek וחוצה את הבמה מאחורי המרכז. הסקריפט ה-inline מסמן אותה `.is-wrapping` (`transition:none; opacity:0`), מאלץ reflow ומסיר — היא קופצת בלתי-נראית ונכנסת ב-fade בצד השני. לא להסיר.
  - **`.oc-info`** (status / date / location; Copperplate Light 16 verbatim; גריד `1fr auto 1fr` ⇒ התאריך ממורכז בדיוק; `aria-live="polite"`): טקסט התחלתי סטטי ב-HTML (online / 22.10.2026 / tel aviv); סקריפט inline בסוף ה-`<body>` מאזין ל-`tri:change` **על ה-`.tri` עצמו** (הקומפוננטה משגרת בלי `bubbles`) ומעתיק את `data-info-status` / `data-info-date` / `data-info-location` של השקופית שבמרכז. 🔴 הסקריפט חייב להישאר inline (לא `defer`) — כך הוא נרשם לפני שה-init הדחוי מרנדר לראשונה.
  - תמונות `images/opencalls/<slug>-card.webp` (כולן 4:5) + srcset, `sizes="235px"`.
- **`#opencall`** (דסקטופ בלבד; Figma `landing::1124:792`, מחליף את `144:355`): "the open call" + 3 כרטיסים: obsession (online · 22.10.2026 · tel aviv) · the-peeler · how-many (שניהם archived) — שלושתם `<a class="opencall-card">` לדף הקול הקורא.
  - 🔴 **הכרעת משתמש 2026-09-27: תיבות התמונה 4:5 כמו כרטיסי המובייל** (290×362.5; כרטיס ה-`size-b`, ברוחב 288, מקבל `aspect-ratio:288/362.5` כדי שהגבהים יתאימו) — **לא** 290×502 של הפיגמה — כדי שכל הפוסטר (לוגו, טקסטים, תאריכים) ייראה בכל רוחב; 4:5 = היחס של תמונות הכרטיס עצמן ⇒ בלי crop. לא לחזור ל-502 ולא לייצוא ה-9:16 של obsession.
  - שורה אחת בכל רוחב דסקטופ: `.opencall-grid{flex-wrap:nowrap}`, כרטיסים `flex:0 1 auto; min-width:0` מתכווצים ושומרים יחס. בבלוק `≤1100`: gap 32, שורת ה-info `grid-template-columns:1fr auto 1fr`, `font-size:clamp(11px,1.4vw,14px)`, padding `0 clamp(4px,1.5vw,16px)`, nowrap (ב-769 הכרטיסים ≈203px).
- **תמונת obsession:** `images/opencalls/obsession-card-v2.{webp,avif}` 1080×1350 + `-480w`/`-768w` (webp+avif) — הפוסטר עם דדליין 22.10.2026, אותו קובץ כמו ה-hero של הדף (`images/opencalls/obsession/hero-v2.*`; Figma `1318:408` = `1906:715`). `obsession-card.*` (16.10) ישן, לא בשימוש. המקור הגולמי + רינדורי ייחוס של הפריימים: `_originals/figma-checks/opencall-2026-09-27/` (gitignored, מקומי בלבד).
- **דאטה:** `opencalls.json` (obsession = הרשומה הראשונה, `status:"open"` — `docs/data-contracts.md` §8) + `homepage.json` — `mobile_cta.card_ids` ו-`open_call_section.card_ids` = `["obsession","the-peeler","how-many"]` (`mobile_cta.card_ids[0]` = במרכז בטעינה), `mobile_cta.info` = התוויות של הכרטיס שבמרכז בטעינה. HTML ידני — שינוי = HTML **וגם** JSON.
- **obsession — דף קיים (`opencalls/obsession/`):** שני הכרטיסים (`#mobile-cta` / `#opencall`) מקשרים אליו. החלפת הסטטוס אחרי הדדליין — Open issues + `docs/todo.md`.

## #exhibitions-now
- **מחולק לערים** (2026-09-27, Figma `XhGH...::1124:819` / `1318:418`). "exhibitions / now", ואז קבוצות `.ex-city` — שם עיר Copperplate Light 36→**29px** (מובייל 30→**24**), gap 12 לכרטיסים; בין הקבוצות gap 64 (מובייל 32). כל הכרטיסים עם תג `current`.
  - **`tel aviv`** — שני כרטיסים:
    - דיזינגוף = **רזידנסי SUMII** → `sponsors/sumii/`; תמונה = מיחזור `images/sponsors/sumii/hero.*` (+srcset). בתחתית שני לוגואים לבנים **inline SVG** (sumii 113.65px + מלאני הקימוגלו 150.03px — Figma 113.65×51.75 / 150.03×87.69, בקוד רק `width`, הגובה מה-viewBox; gap 43.71; מובייל 32.96 / 43.51, gap 12.68; מקור `images/homepage/ex-now/{sumii,melani}-mark-white.svg`) + "pop up art residency" (מובייל `.ttl-en--res` 11px nowrap).
    - **the-peeler / הקולפן** (גלריית כיכר המדינה) → `exhibitions/the-peeler/`, כרטיס `XhGH...::1124:835` / `1124:95`; אוברליי `exhibition • volume 2` (`.title-bar`) + "הקולפן" — במובייל `.title-bar` מוסתר, רק "הקולפן".
  - **`berlin`** — כרטיס רוחב-מלא (1248×693 / מובייל 358×214.55) של **how-many** → `exhibitions/how-many/`: שם גלריה `the art gallery berlin` (`.gname--en`, Copperplate 30→**24px**, מובייל 14→**11**), כיתוב `.ttl-en--sm` (14→**12**, מובייל **11**), תמונה `images/homepage/ex-now/berlin-how-many.{webp,avif}` 930×861 +480w (imageRef `f9a4f63d…`).
- 🔴 תמונת הקולפן **בשני ה-breakpoints = `images/exhibitions/peeler-desktop.{webp,avif}`** (הקרופ בפיגמה זהה בדסקטופ ובמובייל — 807×902 מתוך 1200×1600). `peeler-mobile.*` (קולפן-מטבח אדום — שגוי) **נמחקו, לא לשחזר**. בכרטיס יש **שני** `<img>` (`.ex-now-photo--mob` / `.ex-now-photo--desk`, מוצגים לפי breakpoint) — שניהם מצביעים ל-`peeler-desktop`; החלפת תמונה = לעדכן את שניהם (`src`, `srcset`, `width/height`).
- מובייל: שני כרטיסי ת"א `flex:1 1 0` = רוחב שווה (177px, per Figma `1124:81`).
- זנב: "our artists" → `artists/` + רצועה של 22 פורטרטים מקושרים (ידנית; סדר = `homepage.json :: exhibitions_now.artist_ids`).
- דאטה: `homepage.json :: exhibitions_now.groups[]`. ⚠️ how-many ב-`exhibitions.json` עדיין `gallery_id:dizengoff` — ראה Open issues.

## #perfume-promo + #perfume-savlanut
- Figma מובייל בלבד: `1318:599` (how-many) + `1318:1169` (סבלנות). דסקטופ ≥1200 = אדפטציה two-col (`.pp-media` 492px); savlanut = מראה (`row-reverse`, תמונה מימין). ב-`≤1199` שני הסקשנים עוברים לעמודה ממורכזת (`.pp-media` עד 492, `.pp-title` `clamp(36px,7vw,56px)`; ה-`row-reverse` לא חל שם). רינדורי ייחוס: `_originals/figma-checks/pp-*`.
- `#perfume-promo`: **תמונה אחת** `images/homepage/perfume-promo/how-many-v2.{webp,avif}` 1200² +480/768 (imageRef `69ac0bc6…` crop `af2d6c`); טקסטים ממורכזים; `.pp-logo` מוסתר ב-`≤1199`; כפתור "עוד על הבושם באתר" → `https://www.zrp.co.il/product/how-many-partners-have-you-had`.
- `#perfume-savlanut` (בושם **"סבלנות"**, תערוכת הקולפן): `savlanut.{webp,avif}` 931×934 +480/768 (imageRef `922a369f…` crop `53b863`); "סבלנות" (FbEzmel Regular 20) / "בושם הנושא של תערוכת הקולפן" (Light 300; **"תערוכת הקולפן" מקושרת** → `exhibitions/the-peeler/`, אנדרליין רבע-שקוף כ-`artist-link`) / `.pp-exbar` `EXHIBITION • VOLUME 2` (Copperplate Light, נקודה 4px) / כפתור "עוד על הבושם באתר" → `https://www.zrp.co.il/product/parfume-incense-amber-and-leather`.
- `.pp-info` gap 40 בדסקטופ ובמובייל (טאבלט 32). כיולי מובייל: `.pp-title` 36→**26px**, `.pp-sub-en`/`.pp-exbar` 20→**16px**; ב-how-many `<br class="mbr">` = "HOW MANY PARTNERS / HAVE YOU HAD?"; עברית verbatim; padding 32.
- 🔴 "בלעדי לגלריה" = מצב תוכן, לא עיצוב: כשיש עמוד מוצר — אותו `.pp-cta` (אותו copy, URL אחר), לא copy אופליין (`docs/lessons.md` 2026-08-18).
- דאטה: `homepage.json :: perfume_promo.perfumes[]` (`name_he`, `exhibition_bar_en[]`, `exclusive_he`, `cta_*` — nullable).

## #events-upcoming
- **סקשן סטטי, לא תלוי-תאריכים** (layout: Figma `1318:476`; דסקטופ = אדפטציה). כותרת מוערמת "upcoming" (Copperplate Bold 58; מובייל `clamp(30px,11.8vw,46px)`) מעל "events" (Light 91; מובייל `clamp(46px,18.46vw,72px)`), חפיפה `-16px` / מובייל `-12px`.
- **שני פוסטרים חודשיים ("הרשימות")**, `object-fit:contain`, aspect `175/301`. מקור נוכחי (2026-09-27): Figma `1873:1074` דסקטופ / `1738:347` מובייל (פריימי התמונה: במובייל דיזינגוף `1863:441` / מדינה `1738:355`; בדסקטופ `1873:1081` / `1873:1082`):
  - דיזינגוף: `images/homepage/upcoming/poster-dizengoff-v4.{webp,avif}` (imageRef `9c2ab33c…`). יש לו שכבת `img.bg` (cover מאחורי ה-contain) — 🔴 **חייבת להצביע לאותו קובץ (ואותו srcset) כמו הפוסטר** (decode אחד); **לא** ל-`poster-bg.webp` (פוסטר יולי-אוגוסט ישן שהציץ ברצועות ה-letterbox).
  - כיכר המדינה: `poster-hamedina-v5.{webp,avif}` (imageRef `b27ea564…`; טקסט אפוי). בלי bg.
  - שניהם נאפו ממקור 9:16 (דיזינגוף 1080×1920, מדינה 1620×2880) ב-**resize לפי רוחב בלבד — בלי crop/`-extent`**: `magick <src> -resize 760x -strip -quality 85 <name>.webp` (avif: `-quality 60`) ⇒ 760×1351 (= 2× כרטיס 380px); `-resize 480x` ל-`-480w` (480×853). `175/301` הוא רק תיבת הכרטיס: הפוסטר ב-contain, ואת רצועות ה-letterbox ממלא בדיזינגוף ה-`.bg` (cover) ובמדינה הרקע הלבן של הכרטיס. `width/height` = פיקסלי הקובץ הראשי; `srcset="…-480w.webp 480w, ….webp 760w"`, `sizes="(max-width:768px) 76vw, 380px"`.
  - ⚠️ `1873:1074` הוא פריים דסקטופ מלא של הסקשן (כותרת 36/36 ממורכזת, gap 24 בין הפוסטרים) — ממנו ומ-`1738:347` נלקחו **רק הפוסטרים** (2026-09-27). ה-layout הדסקטופי באתר עדיין אדפטציה של `1318:476` (כותרת מוערמת 58/91 משמאל, gap 16). (`1738:347` תואם את ה-layout המובייל הנוכחי; הפער בדסקטופ בלבד.) יישור ה-layout לפריים = שינוי עיצוב שדורש הכרעת משתמש.
- דסקטופ: 2-up ממורכז, כרטיס `min(380px,(100% - 16px)/2)`, gap 16. **מובייל: קרוסלת scroll-snap** — `.ev-up-posters` full-bleed (`margin:0 -16px; padding:0 16px; overflow-x:auto; scroll-snap-type:x mandatory`, בלי scrollbar), פוסטר `flex:0 0 76%` עד 340px, `scroll-snap-align:center` (הבא מציץ ~90px), gap 8, **בלי חיצים**.
- `.ev-up-viewall` **view all** (Light 16, border 1px, padding 4px 16px). **כותרת, פוסטרים וכפתור — כולם → `events/`** (הנחיית המעצבת).
- **עדכון הלוח = החלפת קבצי פוסטר** (תהליך תוכן; המקור יכול להיות node בפיגמה או קובץ שהמעצבת מסרה):
  1. המקור הגולמי → `_originals/upcoming-<YYYY-MM-DD>/` בשורש הריפו (gitignored, מקומי בלבד) — לא תחת `images/`.
  2. **קודם להשוות לקיים** — אותו לוח כבר נמסר שוב (2026-09-01) ⇒ לא ליצור גרסה. hash/השוואת בייטים תמיד שונים (ייצוא, דחיסה): להקטין את המקור לגודל הקובץ הנוכחי (`-resize 760x`) ואז `magick compare -metric RMSE <new>.png <current>.webp null:` (הערך בסוגריים = שבר). אותו לוח = ~2–3% (נמדד 1.7% ו-2.9%); לוח מתוקן על אותה תבנית יצא 13% — אין סף "שונה" בטוח, ולכן ההכרעה לפי `magick compare -fuzz 10% <a> <b> diff.png`: שורות טקסט אדומות = תוכן חדש, נקודות מפוזרות = רעש דחיסה.
  3. **לקרוא את הרסטר:** כתובת דיזינגוף באתר = "Reines"; "Raines" בפוסטר (ה-typo של הפיגמה — כך ב-`poster-dizengoff-v4`) = לדווח למעצבת. אירוע בפוסטר בלי רשומה ב-`events.json`/דף (תקדים: סדנאות הפרחים 23–24.9 ב-v4) = לדווח למשתמש/למעצבת. **לא לערוך את התמונה.**
  4. לאפות `-vN` חדש (+`-480w`; webp + avif לכל אחד) לפי המתכון שלמעלה ולעדכן `src`, `srcset`, `width/height`, `alt` (ובדיזינגוף גם את ה-`.bg`).
  5. לאמת ב-1440 וב-390 (390 דרך iframe — ראה אימות); ב-390 הפוסטר השני מציץ בקרוסלה.
  6. תיעוד: כאן — בולט הגלריה (ה-`-vN` הנוכחי + מקור: node, או "קובץ מעצבת `<name>` W×H — לא Figma") והגרסה הקודמת ל-Removed ("בדיסק"); לסגור/לקצץ את פריט ה-[todo] ב-Open issues **וגם** ב-`docs/todo.md`; את השורה של הפוסטר שהוחלף ב-`FIGMA_LINKS.md` ("פוסטר כיכר המדינה" / "פוסטר כיכר דיזינגוף"); ואת הערת הסקשן ב-`index.html` ("posters updated …").

## #big-news
- Figma `1318:583` מובייל בלבד; דסקטופ = אדפטציה. **טקסט בלבד, ממורכז, על לבן:** `BIG NEWS` (Copperplate Bold, **26px מובייל** מכיול 36, `clamp(26px,3.06vw,44px)`) → "פתחנו לכם נקודת / מכירה נוספת!" (`.nb-title`, FbEzmel Regular, `clamp(36px,4.45vw,64px)` — 36 מובייל / עד 64 דסקטופ) → "חנות חדשה בתוך הגלריה" (`.nb-sub-main`, Light `clamp(24px,1.95vw,28px)`) → "כיכר המדינה, רח׳ ז׳בוטינסקי 131, תל אביב" (`.nb-sub-addr`, Light `clamp(18px,1.4vw,20px)`, → `#galleries`).
- דאטה: `homepage.json :: big_news` (`heading_en`, `figma_node_mobile:"1318:583"`, `figma_node_desktop:null`).

## #artworks
- Figma: מובייל `1318:560` (layout + תמונות); דסקטופ `1124:988` "Work Section" (בתוך `1124:754`) — **layout בלבד** (התאים שם מכילים יצירות ישנות).
- **שחמט 2×3 בזרימת source טבעית, אותו DOM בשני ה-breakpoints** (בלי `grid-area`): תמונה/"the" · "art works"/תמונה · תמונה/"more". גריד `repeat(2,minmax(0,1fr))`, `.artworks{max-width:var(--max)}`.
  - מובייל: תאים ריבועיים (~179px), **`object-fit:contain`** (FIT בפיגמה).
  - דסקטופ (≥769): תאים **624×600** (`aspect-ratio:624/600`), padding עליון 32, **cover** ב-CSS; `object-position` תא 1 `50% 10%`, תא 4 `50% 18%` (ראשים בפריים).
- **אותן 3 תמונות בשני ה-breakpoints**: `images/homepage/artworks/aw-{1,2,3}.{webp,avif}` (imageRefs `2baf9d2e…` / `3f0a517d…` = hero natasha-zeriker בלי crop / `99bbf47b…`). וריאנטים: aw-1 480/600/1248, aw-2 480/631/1248, aw-3 480/595/690; `sizes="(min-width:769px) min(624px, calc(50vw - 96px)), 50vw"`.
- 🔴 `<picture>` + `<source type="image/avif">` **ידני** — כל וריאנט webp חייב אח avif; חובה `.aw-img picture{display:contents}`.
- אריחי טקסט: "the" ו-"art\works" (תא אחד) = Copperplate **Bold** (`.word`, 700), לא מקושרים; "more"+chevron = Copperplate **Light** (`.more`, 300) = הקישור היחיד → `works/` — מובייל **26px** (כיול מ-36), דסקטופ `clamp(30px,4.45vw,64px)`. **דסקטופ בלבד:** "ART/works" מיושרות שמאלה בתוך הבלוק, **"‹ more" = chevron לפני הטקסט** (`row-reverse` + `scaleX(-1)`); במובייל chevron אחרי.
- **`.aw-curator`** → `curators/korin-avraham/`: דסקטופ (`1124:1003`) **name מעל role** (CSS `order`) ב-**64px** (כיול מ-80) + כפתור **"view"**; מובייל (`1318:575`) role מעל name (`clamp(16px,7.2vw,28px)`) + **"read more"**, `min-height:179px`, padding `0 48px`. התווית מוחלפת ב-CSS (`.lbl-d`/`.lbl-m`).
- דאטה: `works.json :: works[]` = 3 רשומות = אריחי התמונה בלבד (אריחי טקסט = HTML).

## #x-our-artists
- **קרוסלת פוקוס `.tri` בשני ה-breakpoints** (Figma מובייל `1318:695`; דסקטופ = אדפטציה). כותרת "zielinski rozen / x our artists".
- **39 שקופיות**, `data-tri-loop="true"`, **`data-tri-start="13"`** (0-based ⇒ nir giorgio levin = `work-14`, עם zohar ron / gilad kenan בצדדים per הפריים). לכל שקופית `data-caption`/`data-caption-href`/`data-artist-href` — קליק במרכז/בכיתוב → דף האומן.
- **מקור-אמת לסדר: `homepage.json :: x_our_artists.items[]`** = Figma `XhGH...::1873:1146` "mobile order" (קנוני 2026-09-27; מחליף את `1124:1181`; נשמר גם כ-`figma_node_order`). הגריד הדסקטופי בפריים = מקור הסדר והתמונות לשני ה-breakpoints.
- תמונות `images/homepage/x-our-artists/work-N.{webp,avif}` = רינדורי-node (crop/FIT/רקע `#FAFAFA` אפויים ⇒ `object-fit:cover`). פריטים 10/23/31 מוגשים כ-`work-10-v2` (קרופ שונה) / `work-23-v2` (הישן בצבעים דהויים) / `work-31-v2` (צילום אחר, על לבן) — הישנים בדיסק (כלל-זהב 8), לא להחזיר אליהם; פריט 39 = shira turbowicz (`work-39` → `artists/shira-turbowicz/`). רינדורי ייחוס של 39 המלבנים מ-`1873:1146`: `_originals/figma-checks/xoa-2026-09-27/` (`_originals/` = gitignored, מקומי בלבד) — להשוות מולם לפני שמחליפים `work-N`.
- היום `work-N` ↔ מיקום `N` במיפוי 1:1 (פריטים 10/23/31 דרך `-v2`). תמונה חלופית = `work-N-vM` חדש (לא לדרוס — כלל-זהב 8); פריט חדש בסוף = `work-<N+1>`. ⚠️ שינוי סדר ישבור את ה-1:1: לא לשנות שמות קבצים קיימים (דריסה = הפרת כלל-זהב 8) — לערוך את `items[]` ואת סדר ה-`<img>` בלבד, ולתעד כאן שהמיפוי כבר לא 1:1. אחרי כל שינוי: `items[]` וה-`<img>` באותו סדר, ו-`data-tri-start` מצביע על השקופית הנכונה.
- ⚠️ פתוח: פריט 3 — בפיגמה `1873:1146` **וגם** ב-`artists.json :: name_en` כתוב "elsa ers brosh"; באתר "elsa ars brush" בשלושה מקומות: `data-caption` של השקופית, `homepage.json :: x_our_artists.items[2].name_en`, ושם הפורטרט (`.nm`) ברצועת "our artists" ב-`#exhibitions-now`. שאר 38 הכיתובים תואמים לפריים (נבדק 2026-09-27). טעון הכרעה — לא לשנות בלי אישור; אם מיישרים — את שלושת המקומות יחד.
- דסקטופ: מרכז 481×726, peeks 302×453 ב-`.6` (hover .85) ב-`±415px`; **חיצים בדפוס `ig-nav`** (`.only-desktop`) — IIFE משגר `KeyboardEvent` ArrowLeft/Right ל-`.tri`.
- מובייל: swipe בלבד, frame 420px, מרכז 56%, peeks 28%×75% שזולגים מהקצוות.
- **אין dots גלויים** (אין dots בפריים) — ה-markup (38 `button.tri-dot`, `is-on` סטטי על #14) עדיין קיים ומוסתר ב-`.x-artists .tri-dots{display:none}`; ה-JS לא דורש התאמת מספר. אם מחזירים dots — להשוות את מספר הכפתורים למספר השקופיות ולהזיז את `is-on`.
- כיתוב Copperplate Light 16 `#989898`.

## #galleries
- "the galleries / tel aviv" (`.galleries-title`, Copperplate 36). כרטיסים (Figma `1318:657`; דסקטופ = אותם קבצים):
  - **מדינה** `<a>` → `galleries/medina/` — `images/galleries/medina/hero-v2.{webp,avif}` (חלון הראווה עם כיתוב הקולפן, imageRef `c937cf2f…`).
  - **דיזינגוף** `<a>` → `galleries/dizengoff/` — `images/galleries/dizengoff/hero-v2.{webp,avif}` (פנים עם חלון How Many, imageRef `a67703c8…` בקרופ Figma).
  - שתיהן 822×996 (cover ל-33/40 בשני ה-breakpoints) + `-480w` + srcset.
  - **פשפשים** — `<article>` לא-קליקאבילי, **ירוק שטוח `#2B4C39` בלי תמונה** + "coming soon" (`dim--green`), כי ב-Figma `1318:686` שכבות התמונה מוסתרות. `flea-market/hero.*` בדיסק = placeholder של dizengoff — לא לחבר. כשיהיה צילום אמיתי: hero חדש כ-`<img src="….webp">` רגיל (ש-`picture-upgrade.js` יעטוף עם AVIF) או `<picture>` עם `<source type="image/avif">` ידני — לא `<picture>` ריק כמו בכרטיסי מדינה/דיזינגוף; + `image_hero` ב-`galleries.json`, ואז `python3 tools/sync_data.py`.
- **שעות (זהות במדינה ובדיזינגוף):** "א'-ה' 18:00-11:00" / "ו' 14:00-11:00" / "שבת סגור". 🔴 **הכרעת משתמש: verbatim כמו ב-Figma — ספרות LTR כמו אותיות לועזיות, לא "לתקן" סדר.** זהה ל-`galleries.json :: hours[].time`. הנוסח השמור (ב-`galleries.json` וב-HTML) הוא "18:00-11:00" / "14:00-11:00" — `docs/todo.md` מתאר את המשמעות (11:00-18:00), לא את מה שנשמר; לא להפוך. ⚠️ הבולט מתעד מצב נוכחי, לא ערך קבוע: שינוי שעות = לעדכן אותו (ואת `docs/routes/galleries.md` → Hero, שם גם דוגמה מעובדת לקונבנציה).
- מובייל: גריד `174px 1fr` (תמונה 174×210 משמאל, שם מימין); `.gallery-card--flea .addr` מוסתר.
- דאטה: `galleries.json` (`image_hero` = תמונת הכרטיס כאן, נפרד מ-`image_page_hero`; `figma_node_mobile` לשלושתן) + `homepage.json :: galleries_section`. הסקשן ידני — שינוי JSON = לערוך גם את `index.html`, ואז `python3 tools/sync_data.py`.
- ⚠️ פערים פתוחים (לא התבקש לתקן, `docs/todo.md`): (1) כתובת פשפשים ב-HTML "שוק הפשפשים, **יפו**" מול "…**תל אביב**" ב-JSON וב-Figma (גם השם ב-HTML "גלריית יפו, שוק הפשפשים" ≠ `name_he`); (2) בכרטיס מדינה בפיגמה **אין שורת כתובת** — האתר מציג "ז'בוטינסקי 131, תל אביב"; טעון בירור. שאר טקסטי `1318:657` לא סונכרנו (רק תמונות ושעות).

## #galleries-berlin
- "the gallery / berlin", **מיד מתחת ל-`#galleries`** (בקשת משתמש 2026-09-27). Figma `1859:2668` / `1856:433`. הרווח מ-`#galleries` = `padding-bottom` של `#galleries` (96 / מובייל 32 — מהבלוק הראשי `@media (max-width:768px)`, שדורס את הכלל המוקדם `.galleries{padding:32px 16px 48px}`; עריכת המוקדם לא תשנה דבר) + `padding-top` של `.galleries--berlin` (56 / מובייל 32). שינוי הרווח = לגעת ב-`.galleries--berlin` בלבד.
- כרטיס בודד **LTR באנגלית (Copperplate)**; כותרת ממחזרת `.galleries-title` (36 verbatim). כרטיס 410.667 בגאומטריית ת"א (תמונה 33:40, צמוד שמאל), מתחת: `the art gallery berlin` / כתובת 3 שורות / handle.
- **כיול מכויל-מדידה:** דסקטופ שם 28→**22px**, כתובת 18→**14**, handle 16→**13.5**; מובייל שם 22→**16.8** (חייב 2 שורות בעמודת 168px), כתובת 14→**11**, handle 13→**11**.
- מובייל: גריד `174px 1fr` — תמונה 174×210.91 + כתובת מתחתיה משמאל, שם+handle מימין (`.txt{display:contents}` + grid-areas); handle מתחת לכתובת בדסקטופ / מתחת לשם במובייל (`.only-d`/`.only-m`).
- **כתובת verbatim שונה לפי breakpoint:** דסקטופ "hotel amano **berlin**", מובייל "hotel amano" (`.only-d-inline`). "AUGUSTSTRASSE" (UPPERCASE של `auguststraße`) = כמו בפיגמה.
- handle: בפיגמה "@erez rozen_artgallery" (עם רווח) = טעות הקלדה של המעצבת. **מוכרע: `@erezrozen_artgallery` בלי רווח** — הפרופיל הקיים (Art Gallery by Zielinski & Rozen, נבדק 2026-10-06); `erez_rozen_artgallery` לא קיים, ושם משתמש באינסטגרם לא יכול להכיל רווח. אל "תתקן" לפי הפיגמה.
- תמונה = רינדור-node של `1859:2678` (fill `d287a3c1…`, crop `517382` — מלון Amano) → `images/galleries/berlin/hero.{webp,avif}` 822×996 +480w; קרופ המובייל שונה ~2% ⇒ אותו קובץ ב-cover.
- **אין דף גלריה** — הכרטיס לא קליקאבילי; רק ה-handle → אינסטגרם.
- **ברצלונה (עמודה שנייה, Figma `1859:2668` col `1965:21` / מובייל `1964:110`):** דסקטופ = גריד 2 עמודות של 592 (1248 − gap 64), כל עמודה = כותרת "the gallery / barcelona" + כרטיס; הכרטיס של ברלין התרחב מ-410.667 ל-592 (`.galleries--berlin .berlin-card{max-width:none}`). מובייל = ערימה (ברלין ואז כותרת+כרטיס ברצלונה, רווח 32 — לא נמדד בפיגמה). `.berlin-card--soon`: תמונה `images/galleries/barcelona/hero.{webp,avif}` (1280×1600 + 480/768/1080w) + שכבת `rgba(0,0,0,.55)` ב-CSS + `<span class="coming">` (דסקטופ 66→**50px**, מובייל 20→**15px**, כיול מדוד), בלי כתובת — רק שם + handle (אותו handle כמו ברלין, בלי הרווח). רשומת `barcelona` ב-`galleries.json` (`status:"coming-soon"`, `city:"barcelona"`, מערכי כתובת ריקים) + `gallery_ids` ב-`galleries_berlin_section`. כתובת — כשתהיה, להוסיף `.addr-lines` לכרטיס וכתובת ל-JSON.
- דאטה: רשומה `berlin` ב-`galleries.json` (`city:"berlin"`, אופציונליים `address_lines_en[]` / `address_lines_en_mobile[]` / `instagram_handle` / `instagram_url`) + `homepage.json :: galleries_berlin_section`; אחרי עריכה → `python3 tools/sync_data.py`. הרשומה מגיעה דרך `sync_data.py` גם למירורי `#fallback-galleries` (בדפי medina/dizengoff ובעמוד האוצרת). היום היא לא מזיקה, כי שם מחפשים גלריה לפי slug או id בלבד. ⚠️ ב-`berlin` השדות `name_he`/`address_he`/`route`/`image_page_hero` = null ו-`hours:[]`, ולכן קוד חדש שעובר על כל `galleries[]` חייב לטפל בזה (או לסנן לפי `city`).

## #sumii
- טיזר רזידנסי SUMII, **מעל `#soos`** (בקשת משתמש 2026-08-18). Figma `1318:316` מובייל — ⚠️ **שוכתב in-place מעל מקור סקשן soos** (אותו id, זהות חדשה); דסקטופ = אדפטציה.
- לוקאפ: `the art gallery by / erez zielinski rozen` (Copperplate 30→**24px**, ls .05em) / `X` 36 verbatim / **לוגו Sumii inline SVG 87.97×40** (`currentColor`, class `sumii-logo`).
- מידע gap 8: `pop up art residency` (Copperplate **Regular** 400, 18→**14**) / `31.08.2026 - 05.10.2026` (16→**13**) / `www.sumiiworld.com` (16→**13**, חיצוני) (תאריכים ואתר = Light 300) / "אוצרות: קורין אברהם" (FbEzmel 16 verbatim; השם → `curators/korin-avraham/`, אנדרליין רבע-שקוף).
- **רצועת 3 תמונות `object-fit:contain`** (FIT — שלא כמו soos): hero שחור / `gallery-02` / `gallery-01`. אריח 1 = `images/sponsors/sumii/hero-thumb.{webp,avif}` 624×780 (4:5 מקורי) — **לא `hero.webp`** (קרופ 3:4 ⇒ פסים לבנים). דסקטופ 158px/gap 16, מובייל 100.25px/gap 4.
- **קליקאבילי → `sponsors/sumii/`** (בקשת משתמש): הלוגו (`.sumii-logo-link`), שורת `pop up art residency` (`a.sumii-title`), הרצועה (`a.sumii-strip`, `<a>` אחד), `read more` (`.sumii-more`). שם הגלריה בלוקאפ (`.sumii-gname`) — **לא** מקושר.
- `padding-bottom:0` — הרווח מ-`#soos` = ה-padding העליון שלו.
- דאטה: `homepage.json :: sumii_sponsor`.

## #soos
- חסות soos.sound, **מעל `#tribe-teaser`** (הכרעת משתמש 2026-08-04, גוברת על "אחרי `#galleries`"). **אין לו יותר מקור חי בפיגמה** (`1318:316` שוכתב ל-sumii) — נשאר כפי שנבנה; דסקטופ = אדפטציה.
- לוקאפ: "הקולפן" (FbEzmel Light 36 → `exhibitions/the-peeler/`) / `X` (Copperplate Light 36 verbatim) / לוגו soos SVG inline 88×21.59 (`fill:currentColor`) → `sponsors/soos/`.
- 🔴 class הלוגו = **`soos-logo`, לא `logo`** — `.logo` גלובלי מוזרק ע"י `site-chrome.css` ומתנגש.
- קרדיטים gap 8: **"מודל: Bella | soos.sound"** (`.soos-line--model{direction:rtl}` — הכרעת משתמש 2026-08-04, כמו בעמוד `sponsors/soos/`) + `www.soos.audio` (חיצוני).
- 🔴 **חריגת lowercase:** `soos.sound` / `www.soos.audio` / `Bella` דרך `.soos-brand` (`text-transform:none`; = `sponsors.json :: case_exception`). שאר האנגלית UPPERCASE.
- 3 תמונות סטטיות (cover, **בלי לייטבוקס**) = מיחזור `images/sponsors/soos/gallery-01..03.webp`: **דסקטופ בגאומטריית thumbs של tribe** (158px, gap 16; יחס `100.25/121.52`), **מובייל Figma verbatim** (100.25px, gap 4).
- `read more` ממוסגר (4px 16px, border 1px) → `sponsors/soos/`. דאטה: `homepage.json :: soos_sponsor`.

## #tribe-teaser
- "loneliness / in a bubbling environment / x the tribe" — Figma דסקטופ `250:87` (+ sponsor `361:393`, gallery `361:420`); מובייל `363:618` (+ `363:622`, strip `363:649`); מדיה קנונית של הרצועה `250:98`.
- `.tribe-teaser-head` → `exhibitions/loneliness/` = **הקישור היחיד לתערוכה בתוך הסקשן** (ה-thumbs = לייטבוקס בלבד, לא ניווט). מחוץ לסקשן גם כרטיס הארכיון `#exhibitions` מקשר לשם. לוקאפ `sponsored-by-moet.webp`; 5 אומנים מקושרים בקרדיטים.
- 5 thumbs (`thumb-5` = וידאו `video.mp4`): **לייטבוקס בלבד** — `div.tribe-thumb-card` + `data-artwork-src`/`data-artwork-title`, **בלי `data-artwork-link`** (⇒ אין CTA), בתוך `data-artwork-gallery="tribe-teaser"` (`docs/components.md` §1.4.1).
- טאבלט 769–1100: `.tribe-gallery-track` `width:100%; max-width:854px` + thumbs `flex:1 1 0; min-width:0` — הרצועה (854px) גלשה ב-769–820 (2026-09-27); לא להסיר.
- דאטה: `homepage.json :: tribe_teaser`.

## #exhibitions (ארכיון)
- Figma `XhGH...::1124:947` / `1318:487` (2026-09-27). "exhibitions / archive" + **שני כרטיסים זה-לצד-זה בשני ה-breakpoints**: how-many (דיזינגוף) משמאל → `exhibitions/how-many/`, loneliness (מדינה) מימין → `exhibitions/loneliness/`.
- שם הגלריה בעברית **מעל** כל כרטיס (`.ex-archive-gal`, FbEzmel Light 36 / טאבלט 26 / מובייל 14, מיושר ימין, padding-right 8) — **אין תג שחור על התמונה**. כרטיס 620×693 (gap 8, שם→תמונה 18) / מובייל 177×214.55 (gap 4 / 8); טאבלט 769–1199 = אספקט `620/693` + גדלים ב-clamp.
- אוברליי שמאל-תחתון: how-many = "how many partners / have you had?" (Copperplate Light 36→**29px**, מובייל 14→**11.3px**); loneliness דסקטופ = פס **Solway** `EXHIBITION • VOLUME 1` (26 verbatim, נקודה 6px, gap 13) + עברית 36; מובייל = Copperplate `exhibition volume 1` (`.bar-m`, 14→**11.8px**) + עברית 14.
- גרדיאנט: `.ex-archive-card--up` (loneliness) = `0deg rgba(0,0,0,.7)→0` (בקוד — בכל ה-breakpoints); how-many = ה-180deg הרגיל. כותרת מובייל `clamp(30px,11.95vw,47px)` / `clamp(46px,19.7vw,77px)` (כויל לרוחב הפריים).
- תמונות `images/exhibitions/archive/how-many-card.{webp,avif}` 1275×1600 (imageRef `a8040b35…`) + `loneliness-card` 1240² (imageRef `fb3e17bb…` crop `555719`) + וריאנטי 480/768.
- 🔴 הכותרת הרשמית = **"בדידות בתוך סביבה תוססת"** (בפיגמה — גם בפריים החדש — הנוסח שונה: "בתוך בסביבה" / בלי "בתוך" = טעות מוכרעת, לא לשחזר).
- דאטה: `homepage.json :: exhibitions_archive.items[]`.

## .social
- "follow us / on instagram" — **שתי השורות Bold** (Figma `144:431`). קרוסלה אינסופית (שכפול ×3), חיצי `ig-nav`, מקלדת, swipe; 9 פוסטים `images/instagram/1..9` → שני חשבונות האינסטגרם. snapshot: `data/instagram.json` (זמני).

## #press
- Figma `1322:258` (מובייל; דסקטופ = אנטומיית הכרטיס של `/press/`). **כלל (בקשת קורין): כל כתבות העיתונות + שני אירועי הפתיחה** (how-many 26.5.2026, loneliness 19.1.2026); שאר האירועים — רק ב-`/press/`.
- **חריגות (הכרעת משתמש 2026-08-12, גם ב-`press_section._note`):** `events/gala-night/` (Figma `1323:570`), שיחת hadas-tuval, שיחת livay-levi. `press/the-shared-list/` = כתבה רגילה. **לא בגריד:** the-space-between (`homepage_visible:false`), tal nehoray, artist-talk, close-look, ktuba, שיחות יולי וכל שאר האירועים — לא להחזיר בלי הכרעת משתמש.
- **13 כרטיסים, חדש→ישן = סדר ה-DOM:** hadas-tuval (28.8) · livay-levi (18.8) · gala-night (29.7) · peeling-a-layer (1.7) · manicure-against-darkness (1.7) · the-shared-list (25.6) · the-sixth-scent/ora (7.6) · the-last-station (27.5) · how-many opening (26.5) · loneliness opening (19.1) · press-1/פורטפוליו (19.1) · walla (5.1) · time-out/קאונטדאון (31.12.2025). כולם לעמודים פנימיים (the-last-station → `press/the-last-station/`, לא timeout.co.il).
- כרטיס = chip `#EEF0EF` + כותרת + תאריך + תמונה **292×162 / 171×108 מובייל** (150 ב-≤400). כיולים כמו `press/index.html`: תג/תאריך EN **11.5**, כותרת EN **13**, HE **16**.
  - `.ttl.en .heb` (1.23em) — מילה עברית בכותרת אנגלית (gala-night). `.tag-lat` — "TIME OUT" בתג עברי; תג `press/time-out/` הישן = **"TIME OUT | תרבות"** (לא "מגזין TIMEOUT").
  - `.img--contain` (רקע `#FAFAFA`) — time-out הישן. `.press-card--ora .ttl.en` 10px במובייל. פורטפוליו → `images/press/press-1/00-home-card-v2`.
- **דסקטופ:** `grid-auto-flow:column` + `direction:rtl` על `grid-template-rows:repeat(7,auto)`, gap 48 ⇒ 1-7 בעמודה הימנית, 8-13 בשמאלית. 🔴 **הוספה/הסרה = לעדכן ל-`repeat(ceil(n/2),auto)`**, אחרת עמודה שלישית. **מובייל:** flex עמודה אחת.
- "press / & events" — שתי השורות → `press/`; מתחת `.press-viewall` **"more press & events"** (מתכון `.ev-up-viewall`) → `press/`.
- 🔴 **סטטי: בלי JS, בלי קרוסלה, בלי סינון תאריכים** (הכרעת משתמש 2026-07-23) — גם אירועים שעברו מוצגים (סינון רק ב-`/press/` וב-`/events/`).
- דאטה (ידני): `press.json :: homepage_visible` (**true בדיוק ל-13 האלה**) + `homepage.json :: press_section.item_ids` (אותו סדר). כרטיס חדש = HTML + שני ה-JSON + `repeat(N,auto)`.
- סדר 19.1.2026 בהומפייג' = Figma `1322:258` (פתיחת loneliness **לפני** פורטפוליו/press-1). ב-`/press/` הסדר הפוך לפי `1323:244` (2026-09-01). לא ליישר בלי הכרעת משתמש.

## Open issues
(פריטים שמסומנים [todo] רשומים ב-`docs/todo.md`; השאר מתועדים רק כאן)
- [todo] מקור Figma של שינוי ההירו (2026-08-28).
- [todo] handle ברלין (רווח בפיגמה).
- [todo] פשפשים: "יפו" מול "תל אביב"; אין צילום. כרטיס מדינה בפיגמה בלי שורת כתובת.
- [todo] תאריכי הרזידנסי: כאן `31.08.2026 - 05.10.2026`, בכרטיס `#g-ex` בדף דיזינגוף הפוך — טעון הכרעת מעצבת.
- [todo] 🔴 פוסטרים לאוקטובר: `poster-dizengoff-v4` / `poster-hamedina-v5` הם לוחות **ספטמבר** (האירוע האחרון מסתיים ב-2.10) — מ-3.10 `#events-upcoming` מציג לוח שכולו עבר. לבקש מהמעצבת לוחות אוקטובר; ההחלפה = תהליך ה-`-vN` שבסקשן.
- [todo] 🔴 **קול קורא obsession:** **הסטטוס ידני:** אחרי הדדליין (22.10.2026) — **לשאול את המשתמש**, ואז "online" → archived בכרטיס הדסקטופ (`.info .status`), ב-`data-info-status` של שקופית המובייל + הטקסט הסטטי ב-`.oc-info`, וב-`homepage.json :: mobile_cta.info` (ב-`opencalls.json` + `submission_status_he`, ובשלושת ה-`#fallback-opencalls` — `docs/todo.md`). לשאול גם אם להחליף אז את ה-marquee "קול קורא חדש באוויר !".
- how-many: `gallery_id:dizengoff` ב-`exhibitions.json` מול כרטיס berlin ב-`#exhibitions-now` (ובארכיון תחת דיזינגוף); והיא מוצגת גם כ-`current` ב-`#exhibitions-now` וגם בארכיון `#exhibitions` — טעון הכרעה. **כשיוכרע:** לעדכן `exhibitions.json` (`gallery_id`/`status`), את המירור הידני `#g-exhibitions-data` ב-`galleries/dizengoff/index.html` (לא בבעלות `sync_data.py` — ראה `docs/routes/galleries.md`), את `homepage.json :: exhibitions_archive.items[]` + `exhibitions_now.groups[]`, ואת התווית "גלריית כיכר דיזינגוף" בכרטיס הארכיון ב-`index.html` (`.ex-archive-gal` + ה-`aria-label`); וגם את המירורים הידניים `#fallback-exhibitions` ב-`exhibitions/how-many/index.html` וב-`exhibitions/loneliness/index.html` (`gallery_id`, `status`, `gallery_label_he`) ו-`#fallback-exhibitions-min` ב-`curators/korin-avraham/index.html` (`gallery_id`) — לא בבעלות `sync_data.py`, ראה Mirror registry ב-`docs/data-contracts.md` §1.4; ואז `python3 tools/sync_data.py` ו-`--check`.
- כתיב elsa: "elsa ars brush" באתר (קרוסלה + `homepage.json` + רצועת our artists) מול "elsa ers brosh" בפיגמה וב-`artists.json`.
- `FIGMA_LINKS.md` עודכן חלקית ל-2026-09-27 (ארכיון `1124:947`/`1318:487`, ברלין `1859:2668`/`1856:433`, והקול הקורא `1124:792`/`1318:401` + פס ה-announcement `1318:397`/`1124:789` נמצאים שם; החסרים — ברשימה שבכותרת).
- drift של `homepage.json` + הערות-קוד מיושנות (ראה Shared rules).
- ⚠️ פריט ה-todo "Dizengoff archive thumbs" מפנה ל-`#fallback-archive` ב-`index.html` — **המזהה לא קיים**; הפריט מיושן.

## Removed / do not restore
- **`#events-upcoming` הקודמים:** כותרת מעגלית (`images/homepage/upcoming-events-circle.svg`), קרוסלת לופ + חיצים, מירור `#events-upcoming-data` + IIFE, מנגנון `hidden` לפי תאריך, כרטיסים עם `gallery_en[]` (השדה נמחק) / טוסט "בקרוב" בהומפייג'. (מנגנון ה-`soon` עצמו **לא מת** — הרנדרר של `events/index.html` עדיין תומך ב-`soon:true` במירור, אף שאף רשומה ב-`events.json` לא נושאת אותו היום, ו-`/press/` משתמש במחלקה סטטית `pcard--soon` + טוסט; הוסרה רק הצריכה בהומפייג'. לא למחוק אותם כקוד מת.) בדיסק: `poster-dizengoff(-v2,-v3).*`, `poster-hamedina(-v2,-v3,-v4).*`, `poster-bg*`, `images/events/anat-wegier/upcoming.*`. `events.json :: card_title_en` נשאר בלי צרכן.
- **Solway לקרוסלת האירועים** (הוסר 2026-08-04). ⚠️ Solway **כן** חי היום — לפס הארכיון בלבד (ראה Shared rules); לא להסיר.
- **`#press` כקרוסלה / עם סינון תאריכים** (בוטל — הכרעת משתמש 2026-07-23), `#press-data` + renderer, `.soon-toast` + `press-card--soon`, `.press-row--swap` / `.press-row--right` (מבנה השורות הישן; ⚠️ **`.press-rows` הוא הגריד הנוכחי — לא להסיר**), `.desc-lat` / `.desc-lat-sm`, `.img--white`.
- **`#big-news` עם תמונה** (`images/homepage/big-news/shop.*`, scrim, טבעת "BIG"×6, `.nb-media/.nb-overlay/.nb-ring/.nb-info`; `ring_text_en`/`badge_en`/`image` ב-JSON). טקסט מעגלי בעתיד: `textLength` על `textPath` לא נאכף בכרום — `docs/lessons.md` 2026-07-15.
- **`#perfume-promo`:** גלריית 5 thumbs (`perfume-1..5.*` בדיסק), `ppMain`, `pp-bio`; בסבלנות — קו 32×1 + "בלעדי לרכישה בגלריה בכיכר המדינה".
- **`#x-our-artists`:** גריד 38 הדסקטופי (נמחק מה-markup 2026-08-05). `work-10` / `work-23` / `work-31` הישנים (בדיסק) — הוחלפו ב-`-v2`, לא להפנות אליהם שקופיות. dots גלויים — אין בפריים; לא להחזיר בלי הכרעת משתמש (מוסתרים ב-CSS בלבד; אם מוחזרים — ראה ההוראות בסקשן).
- **`#artworks`:** כללי `grid-area` 3×2, `<source media>` לתמונות דסקטופ נפרדות (`aw-*-desktop*` = רינדורי `1124:991/996/997`, יצירות אחרות — בדיסק), אריחי `images/works/tile-*`.
- **hero:** `scroll-prompt` ("SCROLL"+חץ).
- **`peeler-mobile.*`** — נמחקו (תמונה שגויה); לא ליצור מחדש.
- **`#galleries`:** `<picture>` בכרטיס הפשפשים; `images/galleries/{medina,dizengoff}/hero.{webp,avif}` הישנים (בדיסק, לא מקושרים).
- **`#exhibitions-now`:** כרטיס how-many בקבוצת ת"א (`images/exhibitions/how-many-mobile.*`, בדיסק) — הוחלף בכרטיס berlin (2026-09-27).
- **ארכיון:** כרטיס loneliness גדול יחיד (`474:97` / `467:45`) + התג השחור על התמונה (`.ex-archive-badge`) — הוחלפו 2026-09-27 (`images/exhibitions/loneliness-mobile.*` בדיסק); לפניו tabs+thumbs — גיבוי ב-`trash/index-loneliness-card-and-tabs-archive.html`.
- **`#mobile-cta` על `stacked-gallery sg-mode-swap`** (Figma `144:38`: 2 פריטים main+peek, the-peeler ראשי, + `.sg-info`) — הוחלף ב-`.tri` (2026-09-27), ו-`stacked-gallery.{css,js}` כבר לא נטענים בהומפייג'. ⚠️ הקומפוננטה עצמה **חיה** בגלריית המובייל של `opencalls/<slug>/` — לא למחוק את הקבצים.
- **`#opencall`:** תיבות התמונה 290×502 של הפיגמה (הוחלפו ב-4:5 — הכרעת משתמש 2026-09-27); ייצוא ה-9:16 של פוסטר obsession בפריים הדסקטופ (imageRef `8f00a7f8…`) — לא בשימוש; הכלל הטאבלטי `.opencall-card{width:280px}` (היה מת — נדרס ע"י `.size-a/.size-b`) ו-`.img{height:420px}`. לא להחזיר.
- **marquee "coming soon our europe galleries"** (6 פריטים) — הוחלף ב-"קול קורא חדש באוויר !" (2026-09-27). סגנונות ה-`.announce` האנגליים נשארו בכוונה, לטקסט אנגלי עתידי — לא למחוק.
