# todo.md — Known Gaps & TODO

> **קרא את הקובץ הזה כש:** אתה בודק אם משימה כבר נעשתה, מקבל בקשה הקשורה ל-assets חסרים (logo/placeholder hero), placeholder data, או infrastructure שעוד לא קיים. **בסוף משימה — סמן `[x]` ל-TODO שסגרת ועדכן אם נדבק שמשהו חסר.**

---

## פתוח

- [ ] **שירה טורבוביץ׳ (SUMII) — שאלות פתוחות מהפריים `1608:5728` (2026-08-20):** (1) פרטי היצירה "פסל מודפס בתלת מימד **ממשי** PLA" — כנראה "מ-PLA משי" (בביו: "ביו־פלסטיק משי"); נשמר verbatim. (2) "קימור ו**בשם**" בסטייטמנט — אותו חשד כמו בעמוד הספונסר. (3) הכתיב "טורבוביץ׳" אומץ כקנוני (5 מופעים בפריים הזה) ועמוד `/sponsors/sumii/` + `sponsors.json` תוקנו מ"טורוביץ׳" — **בפריימי הספונסר בפיגמה עדיין "טורוביץ׳"**, לתקן שם. (4) אין frame דסקטופ לדף — הדסקטופ = אדפטציה (שם בשורה אחת ב-64px).
- [x] ~~**הכרעת איות — כתובת דיזינגוף "1 Raines st." (דפי גלריה, 2026-08-12)**~~ **✅ הוכרע 2026-08-13: Reines** (הרחוב קרוי על שם הרב ריינס; "Raines" בפיגמה = typo). תוקן בכל האתר: `galleries.json` + 3 מירורי `#fallback-galleries` (שני דפי הגלריה + עמוד האוצרת), JSON-LD של דף דיזינגוף, `data/events.json`, ו-5 דפי אירועי how-many (zohar-ron, liel-salman, anat-wegier, nir-giorgio-levin, risa-and-noemi) שנשאו את האיות השגוי עוד מהפריימים הישנים. **בפיגמה עדיין Raines — לתקן שם.**
- [ ] **הכרעת איות — מנהלת הגלריות (2026-08-12):** בפיגמה הכותרת "Zigel" אבל האימייל "Nataliesiegel8@gmail.com" (**siegel**). נשמר verbatim ב-`galleries.json::manager` ובשני דפי הגלריה. אחרי הכרעה — לעדכן שם/קובץ פורטרט (`images/galleries/managers/natalie-zigel.*`) אם צריך.
- [ ] **דף אירוע חסר — כרטיס "בקרוב" בעמוד `/events/`:** `zohar-ron-medina` (artist talk with zohar ron, כיכר המדינה, 9.9.2026) — קיים בפיגמה רק ככרטיס בפריימי אינדקס האירועים (דסקטופ `1318:3218` / מובייל `1403:999`, תמונה imageRef `951e06ff…`); `route:null` ב-`events.json`, `soon:true` במירור `#events-list-data` → כרטיס לא-קליקאבילי + טוסט "בקרוב". כשיהיה frame לדף — לבנות דף (משפחת artist-talk), לעדכן `route`, להסיר `soon`; לשקול אז גם כרטיס ב-`/press/` (כרונולוגית ראשון) + רשומת `press.json`.
- [ ] **דף אירוע חסר — כרטיס "בקרוב" בעמוד `/press/`:** `event-tal-nehoray-talk` (how many... with tal nehoray, 29.6.2026), `route:null` ב-`press.json`; הכרטיס `pcard--soon` ב-`press/index.html` מציג טוסט "בקרוב" בלחיצה. (מאז press-9 של 2026-08-04 הכרטיס כבר לא בהומפייג'.) כשיהיה frame בפיגמה — לבנות דף, לעדכן `route` ולהחליף `href="#"`. (~~event-anat-wegier-talk~~ ✅ נבנה 2026-07-24 — `events/anat-wegier/`, Figma `1107:2090`/`1107:1981`.)
- [ ] **🔴 `tools/seo/og_gen.py` שבור ו-`inject.py` מרגרס ~90 דפים — אל תריץ אותם גורפות (אושר שוב 2026-08-23):** `og_gen.py` **קורס מיידית** — הוא טוען `/tmp/seo_inject.py` שלא קיים בצ'קאאוט (`FileNotFoundError`). בלעדיו `inject.py` רץ בלי מפת ה-`_dims` ואז **משכתב בשקט את בלוק ה-SEO בכל דף**: `og:image` יורד מ-`og/*.jpg` ל-webp הגולמי (ואיתו נעלמים `og:image:width/height`), `startDate` מאבד את השעה, `endDate` נמחק לגמרי, ותיאורים שנכתבו ביד מוחלפים בקטיעה אוטומטית. **ב-2026-08-23 זה פגע ב-92 דפים בהרצה אחת** (שוחזרו ב-`git checkout`; ראה lessons). **עד שיתוקן — המתכון לדף חדש:** להריץ רק את `refresh_sitemap_lastmod.py`, ואז ידנית: `magick images/events/<slug>/hero.webp -resize 1200x -strip -quality 82 og/events-<slug>-hero.jpg` + להעתיק בלוק `SEO:auto` מדף אחות ולערוך (כולל `startDate`/`endDate` אמיתיים — התצוגה `12:30-11:00` הפוכה מהסכימה). לתיקון אמיתי: לשחזר/להטמיע את `/tmp/seo_inject.py`, לג'נרט `og-dims.json` מלא מ-`og/`, ולפלטר crumbs לפי קיום הדף.
- [ ] **ל-`press/index.html` אין בלוק `SEO:auto` בכלל (התגלה 2026-08-23):** אין canonical, אין OG, אין JSON-LD — בעוד `events/index.html` ושאר עמודי האינדקס כן. `inject.py` יודע לייצר לו בלוק תקין (WebPage + `og/homepage-hero-landscape.jpg`), אבל הרצתו גורפת = הרגרסיה שלמעלה. לסגור יחד עם תיקון ה-tooling, או להדביק ידנית בלוק בודד.
- [ ] **`tools/seo/inject.py` מיושן מול ה-HTML המקומיט (התגלה 2026-07-26):** `og-dims.json` חלקי (160/209 — ההשלמה חיה ב-`/tmp/og_dims.json` שאבד) ו-`breadcrumb()` עדיין מפנה ל-`/press/` ו-`/curators/` שלא נבנו. הרצה גורפת = רגרסיה של ~70 דפים. לתקן: לג'נרט og-dims מלא מ-`og/` + פילטר crumbs לפי קיום הדף. עד אז — להריץ רק על דפים חדשים ולשחזר את השאר (ראה lessons 2026-07-26).
- [ ] **Dizengoff archive thumbs** — `archive_thumbnails.tabs[0]` עדיין `_placeholder:true`. כשהגלריה תיפתח ויהיו צילומים מהתערוכה — לעדכן את 4 ה-`image` paths ב-`data/exhibitions.json` *ובמקביל* ב-fallback inline JSON ב-`index.html` (id=`fallback-archive`).
- [ ] `images/brand/logo.svg` עוד לא קיים.
- [ ] **גלריית הפשפשים — אין צילום:** מאז 2026-08-06 כרטיס ההומפייג' = ירוק שטוח `#2B4C39` per Figma `1318:686` (שכבות התמונה מוסתרות); קבצי `flea-market/hero.*` בדיסק הם עדיין עותק-placeholder של dizengoff, לא מקושרים. כשיהיה צילום אמיתי — לאפות hero חדש ולהחזיר `<picture>` לכרטיס + `image_hero` ב-`galleries.json`.
- [ ] **פערי טקסט בסקשן `#galleries` מול Figma `1318:657` (התגלו 2026-08-06, לא סונכרנו — המשתמש ביקש עדכון תמונות בלבד; דורש הכרעה):** ~~(1) שעות מדינה~~ ~~(2) שעות דיזינגוף~~ **✅ נסגרו 2026-08-12** — השעות סונכרנו בכל האתר (הומפייג' + `galleries.json` + דפי הגלריה החדשים) לערכי פריימי דפי-הגלריה: א'-ה' 11:00-18:00, ו' 11:00-14:00, שבת סגור (לשתי הגלריות). עדיין פתוח: (3) כתובת פשפשים בפיגמה "שוק הפשפשים, תל אביב" מול "שוק הפשפשים, יפו" באתר; (4) בכרטיס מדינה בפיגמה אין שורת כתובת. לוודא מול הלקוח אם אלו עדכונים אמיתיים או רשלנות-פריים.
- [ ] **סדר תאריכי הרזידנסי של SUMII לא עקבי בפיגמה (הועתק verbatim בכל מקום — טעון הכרעת מעצבת):** בכרטיס `#g-ex` של דף דיזינגוף (nodes `1546:3894`/`1555:120`) כתוב **"05.10.2026 - 31.08.2026"** (סוף-לפני-התחלה), בעוד בטיזר ההומפייג' (`1318:316`) ובעמוד `sponsors/sumii/` כתוב **"31.08.2026 - 05.10.2026"**; גם כרטיס how-many הסמוך באותו סקשן = התחלה-לפני-סוף. אם המעצבת תיישר — לעדכן את `dates_text` במירור `#g-exhibitions-data` של דיזינגוף.
- [ ] **`sponsors/sumii/` — חשדות טעות-כתיב בפיגמה (הועתקו verbatim, טעונים אישור מעצבת/לקוח):** (1) "במרכזו אובייקטים **בפסל חומר** מפוסל ביד" — אולי "בפועל/פסלי חומר"; (2) "נשיות דרך צורה, קימור **ובשם**" — אולי "ובושם"/"ושם". בנוסף: פסקה 7 מכילה יפנית (住井) שנופלת ל-fallback של המערכת — אין פונט CJK בפרויקט (זניח: 2 גליפים).
- [ ] 5 דפי-אומן (`zohar-ron`, `eitan-goldson`, `zohar-shtrit`, `hila-loterstein`, `adi-duak`) — placeholder בלי Figma design.
- [ ] Newsletter form — `event.preventDefault()` בלבד (אין backend).
- [ ] Contact + Accessibility — אין Figma.
- [ ] meta tags / OG / favicon.
- [ ] i18n switcher — data תומך (`*_he`/`*_en`), אין UI.
- [ ] JSON Schema validators ב-`data/_schema/`.
- [ ] **Build step:** הטמעת JSON אוטומטית כ-fallback בכל דף דינמי (כיום ידני).
- [ ] **Partial loader** ל-nav/footer כשנעבור 8 דפים.
- [ ] **Routing decision:** static multi-file vs SPA. **המלצה:** static פשוט עד שמשהו ידרוש דינמיקה.
- [ ] שדות `title`, `year`, `dimensions`, `medium` ב-`data/works.json` וב-`artists.json::works[]`.
- [ ] FbEzmel ל-`components/artwork-lightbox.css` font-stack כשנדרש caption עברי.

---

## סגור

- [x] **ארכיון תערוכות בהומפייג': התאמת thumbs ↔ exhibition_id** (2026-05-11): `archive_thumbnails` הפך ל-array של tabs פר-גלריה. medina → loneliness (4 thumbs אמיתיים). dizengoff → how-many (4 thumbs placeholder).
