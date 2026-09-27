# Sponsors — route notes

> קרא לפני עריכה של: `sponsors/soos/index.html`, `sponsors/sumii/index.html`, `data/sponsors.json`, `images/sponsors/**`.
> כאן: המצב הנוכחי והכללים הפעילים. היסטוריה: `docs/history/CLAUDE-2026-09-27.md` §4.

## Pages

- `/sponsors/soos/` → `sponsors/soos/index.html` · Figma: **🔴 אין מקור חי** (ה-nodes ההיסטוריים `XhGH...::1318:3287` / `XhGH...::1318:3480` שוכתבו לעיצוב sumii) · ✅ (2026-08-04)
- `/sponsors/sumii/` → `sponsors/sumii/index.html` · desktop `XhGH...::1637:134` ("sumii - desktop", canonical) · mobile `XhGH...::1318:3480` ("sumii - mobile") · ✅ (2026-08-18; רה-דיזיין 2026-08-23 — מארח גם את הרזידנסי של melani-hekimoglu)

## Shared rules (משפחת `sponsors/`)

### מבנה ודאטה
- **עמודים סטטיים.** הגוף כתוב ב-HTML. `data/sponsors.json` מחזיק meta בלבד, לפי התקדים של כתבות long-form. החוזה המלא: `docs/data-contracts.md`.
- **`python3 tools/sync_data.py` לא נוגע בעמודים האלה.** אין בהם שום script של דאטה.
- **הבסיס = פאנל משפחת ה-artist-talk:**
  - פאנל `#EEF0EF` בשתי עמודות: עמודת טקסט משמאל (`padding:0 16px`, `gap:32px`), וכל התוכן בה מיושר לימין (RTL). מימין כרטיס hero בגודל 492×744.
  - צ'יפ ממוסגר: `1px #1B1B1B`, `padding 4/8`, בלי מילוי. FbEzmel Light 18 בדסקטופ / 16 במובייל.
  - לוקאפ `<h1 class="lockup">` בשורה, `gap:16px`.
  - גוף: FbEzmel Light 18/16, `line-height` ‎19.468/17.305.
  - divider בגודל 72×1, עם הזחה ימנית 16 (`padding 24/16/16`).

### Breakpoints
- **`≥1320`:** ‏`--pad-x:96px`. **מתחת:** ‏48.
- **טאבלט (769–1319):** השורה ב-`gap:32px`. כרטיס ה-hero בגודל `max-width:400px; height:640px`.
- **מובייל (`≤768`):**
  - `--pad-x:16px`.
  - hero ברוחב מלא 390×520, מתחת ל-header.
  - אחריו עמודה לבנה אחת: `display:contents` על העטיפות, ו-`order` על הבלוקים.
  - קצב של 24px בין הבלוקים (`padding 24/16`).

### גליף X וכיול Copperplate
- **גליף X בודד = גודל הפיגמה verbatim.** לא מכיילים אותו: כיול ה-~28% של Copperplate נועד לרוחב של טקסט רץ, לא לגליף בודד.
- **כיול Copperplate — למדוד, לא להניח גורם** (`docs/lessons.md` 2026-08-23).
  - בעמודים האלה יצאו גורמים שונים באותו דף: כותרות המוצר ‎.875 (בפיגמה `textCase:UPPER` — השוואה caps מול caps), הלוקאפ של מלאני ‎.87 והלוקאפ שבהירו ‎.767.
  - הסיבה לפער: הלוקאפים בפיגמה הם `textCase:LOWER` (small-caps), והאתר כופה UPPERCASE — גליפים גבוהים יותר ⇒ font-size קטן יותר. מתכון המדידה: `docs/lessons.md` 2026-08-23.

### 🔴 מלכודות קוד
- **שם מחלקה: אסור `logo`.** ‏`site-chrome.js` מזריק בזמן ריצה את `site-chrome.css`, ובו `.logo` גלובלי. ההתנגשות נראית רק אחרי `load`.
  - השמות הקיימים: `soos-logo`, `sumii-logo`, `mel-logo`.
  - לפני שם מחלקה גנרי (`nav`, `menu`, `toast`…): `grep "\.<name>[{,. ]" components/site-chrome.css components/site-boot.css`.
- **`picture-upgrade.js` עוטף כל `<img>` ב-`<picture>` בזמן ריצה.**
  - לכן לכל מיכל תמונה יש `picture{display:contents}` + `img{width:100%;height:100%}`: ‏`.card>picture`, `.g picture`, `.shot picture`, `.mel-logo picture`, `.img picture`.
  - בלי זה התמונה מתכווצת לגובה הטבעי שלה, ורקע הכרטיס השחור נחשף. **חובה בכל תמונה חדשה.**
- **ה-hero הוא ה-LCP:** ‏`fetchpriority="high"` + `srcset`. בשאר התמונות: `loading="lazy" decoding="async"`.

### קישורי אומנים
- כל אזכור של אומן או אוצרת → `a.artist-link` (קו תחתון `rgba(27,27,27,.25)`).
  - ה-CSS של `a.artist-link` קיים **רק בעמוד sumii**. אזכור ראשון ב-soos (או בעמוד ספונסר חדש) = להעתיק את שני הכללים (`a.artist-link` + `:hover`) מ-sumii.
- `SUMII`/`sumii` לבד = שם מותג, לא אזכור אומן.
- דן סרוסי (soos) אינו אומן גלריה — לא מקשרים אותו.

### SEO
- **מי יצר את בלוק `<!-- SEO:auto -->` בכל עמוד:**
  - **sumii** — הבלוק נוצר ע"י הענף (2026-08-23). סימנים: `@id …#webpage`, ‏`isPartOf`/`publisher`, ‏`about` = מערך Brands, ‏`og:image:width/height`.
  - **soos** — הבלוק **נכתב ידנית** בבניית העמוד (2026-08-04), לפני שהענף נוסף, ומעולם לא נוצר מחדש. סימנים: `@id …#page`, ‏`about` = ‏`Organization`, בלי מידות OG.
  - ⇒ **הרצת `inject.py` על soos אינה no-op** — היא תחליף את הבלוק הידני. לעשות זאת רק בכוונה, ולבדוק את ה-diff.
- **הענף `sponsors/<slug>/` ב-`tools/seo/inject.py`** בונה את הבלוק מתוך `sponsors.json`:
  - `og:type article`.
  - `og:image` נלקח מ-`cover_image` של **הרשומה הראשונה** ב-`sponsors.json` שה-`route` שלה תואם.
  - JSON-LD: ‏`WebPage`, ו-`about` = כל ה-Brands שחולקים את ה-route.
  - סנטינלים `__TITLE__`/`__DESC__` ממלאים את השם והתיאור מה-`<title>`/`<meta description>` של הדף.
- 🔴 **ב-`sponsors.json` הרשומה `sumii` חייבת להישאר לפני `melani-hekimoglu`** — היא קובעת את ה-OG וה-breadcrumb של העמוד.
- **`og-dims.json` — המפתח = ערך ה-`cover_image` של הרשומה הראשונה על ה-route** (היום `images/sponsors/<slug>/hero.webp` → `{jpg:"og/sponsors-<slug>-hero.jpg", w, h}`; ‏w/h = מידות ה-jpg בפועל). שתי הרשומות קיימות.
  - 🔴 **המפתח `images/sponsors/sumii/hero.webp` משותף בפועל:** זה גם `events.json :: sumii-opening.cover_image`.
    - לכן `inject.py events/sumii-opening/index.html` יחליף את ה-og:image של האירוע ב-`og/sponsors-sumii-hero.jpg` (1200×630).
    - ושינוי או הסרה של הרשומה (כדי "לתקן" את האירוע) ישברו את ה-OG של עמוד הספונסר בהרצת `inject.py` הבאה עליו.
    - פתוח ב-`docs/todo.md` (`og-dims.json` ל-`events/sumii-opening/`).
  - בלי רשומה ב-`og-dims.json`: ה-`og:image` נופל ל-webp הגולמי, ו-`og:image:width/height` נעלמים.
  - קובץ ה-`cover_image` חסר (או `null`): ‏`og:image` = תמונת ברירת המחדל של האתר.
  - 🔴 **אין אף רשומה ב-`sponsors.json` עם `route` תואם** (רשומה חסרה או `route` עם שגיאת כתיב): ‏`og:image` = תמונת ברירת המחדל, ‏`og:type website`, ו**אין JSON-LD כלל**. נכשל בשקט.
- **הרצה מחדש — רק עם נתיבים מפורשים:** ‏`python3 tools/seo/inject.py sponsors/sumii/index.html` (ו-`sponsors/soos/index.html` רק בכוונה — ראו למעלה). אחר כך בודקים את ה-diff של הקבצים האלה בלבד.
  - חלופה: לערוך את הבלוק ביד, לפי דף-אח.
  - 🔴 **לעולם לא להריץ גורף** — זה מרסק כ-93 דפים (`docs/todo.md`). בלי נתיבים הסקריפט מסרב ומדפיס מתכון; **לעולם לא להעביר `--all-pages-i-accept-the-regression`.**
- **תמונות OG:** ‏`og/sponsors-soos-hero.jpg`, ‏`og/sponsors-sumii-hero.jpg`. תמונת OG חדשה נאפית ידנית.

### Sitemap ועמוד חדש
- שני העמודים ב-`sitemap.xml`.
- **עמוד ספונסר חדש:**
  - route `sponsors/<slug>/`.
  - רשומה ב-`sponsors.json` עם כל השדות (`null` כשלא ידוע). **`route` חייב להיות בדיוק `sponsors/<slug>/`** — אחרת אין JSON-LD (ראו SEO).
  - תמונות תחת `images/sponsors/<slug>/`.
  - OG: לאפות ידנית `og/sponsors-<slug>-hero.jpg` (`magick images/sponsors/<slug>/hero.webp -resize 1200x -strip -quality 82 og/sponsors-<slug>-hero.jpg`) + רשומה ב-`tools/seo/og-dims.json`: המפתח = ערך ה-`cover_image` של הרשומה (`images/sponsors/<slug>/hero.webp`) → jpg + w/h של ה-jpg בפועל.
  - בלוק SEO: `python3 tools/seo/inject.py sponsors/<slug>/index.html` (נתיב מפורש בלבד), ואז לבדוק את ה-diff של הקובץ הזה בלבד. חלופה: להעתיק את הבלוק מ-sumii ולערוך.
  - `<url>` ב-sitemap + `python3 tools/seo/refresh_sitemap_lastmod.py` — באותו קומיט (כלל-זהב 15).

### אימות
- ב-file:// הפונטים חסומים, ולכן בודקים טיפוגרפיה רק דרך http.
- שינוי בעמודי הספונסר עצמם (HTML/CSS inline): `node tools/regress/snapshot.mjs --label before --only sponsors/` → השינוי → `node tools/regress/snapshot.mjs --label after --only sponsors/` (**אותו `--only` בשתי הריצות** — עמוד שקיים רק בצילום אחד נספר כהבדל) → `node tools/regress/diff.mjs before after`.
- שינוי בנכס משותף (תמונה או לוגו): `--only` = ‏`sponsors/` + **כל דף שמשתמש בנכס**. את הדפים מוצאים ב-grep על נתיב הקובץ (או במתכון הלוגואים שב-Assets) — לא מרשימה קבועה.
  - 🔴 **להוריד את ה-`./` מפלט ה-grep.** ‏`--only` משווה prefix מול נתיבי `git ls-files` (בלי `./`). נתיב עם `./` לא תופס אף דף ⇒ שתי הריצות מצלמות קבוצה חסרה (אפילו ריקה), וה-diff עובר — ירוק שקרי.
  - למשל: `ONLY="sponsors/,$(grep -rl 'images/sponsors/sumii/hero' --include='*.html' . | sed 's|^\./||' | paste -sd, -)"`, ואז `--only "$ONLY"` — **אותו ערך בריצת before ובריצת after**.
  - ה-prefix `index.html` תופס רק את ההומפייג' (`#sumii`/`#soos`/`#exhibitions-now`). בלעדיו ההומפייג' לא מצולם.
  - דוגמאות מהיום: `hero.*` של sumii → גם `galleries/dizengoff/`, `index.html`, `events/sumii-opening/`. ‏`curator-thumb` → ‏`artists/shira-turbowicz/`, `artists/melani-hekimoglu/`. לוגו מלאני → ‏`events/sumii-melani-hosting/`, `events/sumii-live-studio/`, `index.html`.
- שינוי ב-`components/*` (CSS/JS משותף באמת) — צילום של כל האתר, בלי `--only`.

### זהות Figma
- **node-id אינו מצביע יציב — המעצבת משכתבת פריימים in-place.**
- לפני עבודה על node: לקרוא את שם הפריים ואת התוכן, ולוודא שזה עדיין אותו עמוד.

## `/sponsors/soos/`

"הקולפן X soos" — סטודיו הרמקולים soos.sound של דן סרוסי, בגלריית כיכר המדינה (תערוכת the-peeler).

### Figma
- 🔴 **אין לעמוד מקור חי.** ב-2026-08-18 ה-nodes `1318:3287`/`1318:3480` שוכתבו לעיצוב sumii.
  - **לעולם לא "לסנכרן" את soos מול ה-nodes האלה** — זה עיצוב של עמוד אחר.
  - העמוד נשאר כפי שנבנה.
- לוגו soos הווקטורי = node `1323:1013` (88×21.59). זה המקור ההיסטורי: הוא יושב בתוך פריים ששוכתב, וייתכן שכבר לא קיים. המקור החי = ה-SVG ה-inline בעמוד (ראו Assets); `soos-logo.svg` = עותק-ייחוס.

### דסקטופ
- **פאנל:**
  - `padding: 48 / var(--pad-x) / 32`.
  - צ'יפ "גלריית כיכר המדינה" → `../../#galleries`.
  - לוקאפ: [לוגו soos → `https://www.soos.audio`] X [הקולפן → `../../exhibitions/the-peeler/`].
    - "הקולפן" = FbEzmel Light 36.
    - "X" = Copperplate Light 36 verbatim.
  - גוף: 3 פסקאות, `width:358px`, RTL.
  - divider ‏`#D2D2D2` — **בדסקטופ בלבד**.
  - קרדיט: "מודל: Bella | soos.sound", ומתחתיו `www.soos.audio` (קישור).
- **hero 492×744 מימין:**
  - תמונה: `images/sponsors/soos/hero.{webp,avif}` ‏984×1476, + וריאנטים 480/768 (imageRef `69c2a352…`).
  - scrim: ‏`linear-gradient(0deg, rgba(0,0,0,.7), transparent)`.
  - לוקאפ לבן ממורכז ב-`top:50%`, עמודה עם `gap:8`: הקולפן / X / לוגו.
- **רצועת גלריה על לבן, מתחת לפאנל:**
  - 4 תמונות ב-`gap:8`: שלוש ב-`flex:1`, והרביעית צרה — `flex-basis:20.8181%`.
  - הרצועה: `aspect-ratio:1248/389.80853271484375`, ‏`object-fit:cover`.
  - הקבצים: `gallery-01..04` (עד 660px רוחב). הקרופים של 01 ו-03 נאפו מהפיגמה.

### מובייל
- hero ברוחב מלא 390×520, עם scrim שטוח `rgba(27,27,27,.4)`.
- אחריו תוכן על לבן, בסדר: **צ'יפ → לוקאפ → גוף → גלריה → קרדיט.**
  - הגלריה נכנסת בין הגוף לקרדיט — שונה מהדסקטופ.
- הקרדיט ממורכז. ה-divider מוסתר.
- רצועה: `aspect-ratio:358/106.5`. התמונה הצרה ברוחב `70.48px`.

### 🔴 כללים
- **חריגת-איות מוכרעת (הכרעת משתמש 2026-08-04):** ‏`soos.sound`, ‏`www.soos.audio` ו-`Bella` נשארים **lowercase** — מותג, ובפיגמה `textCase:LOWER`.
  - המימוש: `.heb .brand` (עובד רק בתוך מיכל `.heb`; הספציפיות גוברת על `.heb *`) — Copperplate Light + `text-transform:none`, ‏`letter-spacing:.02em`, ‏`direction:ltr; unicode-bidi:isolate`, ‏`font-synthesis:none`.
    - `.brand` מחוץ לאב עם `.heb` לא מקבל שום כלל, ויוצא UPPERCASE בשקט (`body{text-transform:uppercase}`).
  - **גודל `.brand` = ‏`1em` גם בתוך הגוף** (הכרעת משתמש). lowercase ב-Copperplate יוצא small-caps שכבר קטנים אופטית, ו-`.82em` נראה קטן מדי.
  - כל שאר האנגלית: UPPERCASE כרגיל.
  - הרשימה שמורה ב-`sponsors.json :: soos.case_exception`.
- **שורת המודל ב-RTL (הכרעת משתמש 2026-08-04):** ‏`.sp-credit .line--model{direction:rtl}`.
  - כך היא נקראת "מודל: Bella | soos.sound". ה-LTR של הפיגמה הפך את הסדר לקורא עברית.
  - אותו תיקון קיים גם ב-`.soos-line--model` בטיזר של ההומפייג'.
  - שורת האתר נשארת `direction:ltr`.
- **הלוגו = SVG inline פעמיים** (לוקאפ + hero), עם `fill:currentColor`: שחור בעמודה, לבן ב-hero.
  - `images/sponsors/soos/soos-logo.svg` = עותק-ייחוס בלבד — העמוד לא טוען אותו (ראו Assets).
  - מחלקה: `soos-logo`, **לא** `logo`.
- **אין בעמוד אזכורי אומנים.**
- ℹ️ **תצפית, לא כלל:** הצ'יפ עדיין מפנה ל-`/#galleries` (העמוד נבנה לפני דפי הגלריות), בעוד הצ'יפ של sumii כבר מפנה ל-`galleries/dizengoff/`. זה לא הוכרע — לא לשנות בלי בקשה.

### דאטה
- רשומה `soos` ב-`sponsors.json`.
- `curator_slug`, ‏`date_start`, ‏`date_end` ו-`founder_artist_slug` = `null`.
- השדה `_figma_note` מתעד שאין מקור חי.

## `/sponsors/sumii/`

שתי רזידנסיות בגלריית כיכר דיזינגוף, באוצרות קורין אברהם:
- **SUMII** — המותג של שירה טורבוביץ (→ `artists/shira-turbowicz/`). ‏POP UP ART RESIDENCY, ‏31.08–05.10.2026.
- **מלאני הקימוגלו** (→ `artists/melani-hekimoglu/`), ‏28.09–05.10.2026.

### Figma
- ⚠️ **המובייל `1318:3480` (וה-legacy דסקטופ `1318:3287`) הם אותם node-ids של עמוד soos הישן** — שוכתבו in-place. מזהים לפי שם הפריים ("sumii - desktop/mobile") ולפי התוכן. הדסקטופ ה-canonical `1637:134` הוא פריים חדש.
- **דסקטופ canonical = `1637:134`** (פריים חדש, 2026-08-23).
  - `1318:3287` = הגרסה שלפני תוספת מלאני (legacy) — **לא להשתמש בו.**
- **מובייל = `1318:3480`**. שוכתב in-place, וכולל את שתי הרזידנסיות.
- **תת-nodes (דסקטופ / מובייל):**
  - פאנל sumii: `1637:160` / `1318:3539`.
  - צ'יפ: `1637:164`.
  - לוקאפ: `1637:166`.
  - קבוצת הגוף+divider+אתר+קרדיט (`gap:16`): `1637:183`. הגוף עצמו בדסקטופ: `1637:185`. הגוף במובייל: `1318:3546`.
  - divider: `1637:188` / `1546:3883`.
  - כרטיס hero: `1637:194`.
  - FIGURES: `1637:213` / `1590:181` + `1589:5700` + `1589:5708`.
  - פאנל מלאני: `1637:284` / `1635:348` + `1635:365`. הלוקאפ: `1637:349`. הלוגו: `1637:350`.
  - מוצרים: `1637:379` + `1652:118` / `1652:197`.
  - האוצרת: `1637:240` / `1546:3820`.
  - לוגו Sumii (וקטור): `1546:3666`.

### סדר הסקשנים בדסקטופ
1. פאנל sumii (אפור).
2. FIGURES (אפור).
3. פאנל מלאני (לבן).
4. מוצרים (לבן).
5. `the curator`.

### פאנל SUMII
- **ההבדלים מפאנל soos:**
  - `padding:48px var(--pad-x)` — 48 גם למטה (ב-soos: 32).
  - הגוף ברוחב מלא של עמודת הטקסט (לא 358px).
- **צ'יפ:** "גלריית כיכר דיזינגוף" → `../../galleries/dizengoff/`.
- **לוקאפ:** [לוגו Sumii ‏49.14×22.35 → `https://www.sumiiworld.com`] X [`the art gallery by` / `erez zielinski rozen` → הומפייג' `../../`].
  - X = ‏`20.1117px` verbatim.
  - שם הגלריה: Copperplate Light. ‏16 בפיגמה → ‏**13px** בקוד. בשורה 1 ‏`letter-spacing:.05em`.
- **הלוגו מוגדר inline פעם אחת בעמוד,** כ-`<symbol id="sumii-mark">` מיד אחרי `<site-header>`.
  - המקור: `1546:3666`, מנוקה ל-`currentColor`. ‏10 paths — path הזבל עם `fill-opacity:.05` הושמט.
  - בעמוד יש שני `<use href="#sumii-mark">`, במחלקה `sumii-logo`.
  - הקובץ `images/sponsors/sumii/sumii-logo.svg` = עותק-ייחוס בלבד (`sponsors.json :: logo`) — אף דף לא טוען אותו. עותקים נוספים של הווקטור: ראו Assets.
- **גוף — 7 פסקאות עבריות:**
  - ריצות לטיניות ב-`<span class="lat">`: ‏Copperplate UPPERCASE ב-`.88em` (SUMII / POP UP ART RESIDENCY / FIGURES / CENTRAL SAINT MARTINS / LVMH).
  - **אין חריגת lowercase** ל-sumii (`case_exception:[]`).
  - טווח התאריכים עטוף `<bdi dir="ltr">`, ומוצג התחלה→סוף. היפוך ה-bidi של הפיגמה לא שוחזר.
  - פסקה 7 מכילה יפנית (住井). היא נופלת לפונט מערכת, כי אין בפרויקט פונט CJK — מקובל.
- 🔴 **משקל פסקת הפתיחה:**
  - מובייל = **Regular — גם העברית וגם הריצות הלועזיות** (בתוך `≤768`: ‏`.sp-body--sumii p:first-child{font-weight:400}` + ‏`.sp-body--sumii p:first-child .lat{font-weight:400}`; Figma `1318:3546` ts2/ts3).
    - בלי הכלל השני, `.heb .lat{font-weight:300}` משאיר את SUMII / POP UP ART RESIDENCY ב-Light בתוך פסקה Regular.
  - דסקטופ = Light (Figma `1637:185`). ‏`.lat` בשאר הפסקאות = Light בשני ה-breakpoints (ts4).
  - מכוון — לא לאחד.
- **קישורים בגוף:**
  - "ארז זילינסקי רוזן" (האזכור הראשון) → `about/`.
  - שני האזכורים של "שירה טורבוביץ" בשם מלא (פסקאות 1 ו-4) → `artists/shira-turbowicz/`.
- **הכתיב הקנוני: "טורבוביץ" — בלי גרש** (הכרעה 2026-09-27, בכל האתר). חל על הגוף, על ה-meta description / og / twitter / JSON-LD של העמוד, על `sponsors.json :: sumii.founder_he` ועל `works.json :: artist_he` ("שירה טורבוביץ | sumii").
  - לא לשחזר אף נוסח קודם: לא "טורבוביץ׳" (עם גרש — הקנוני 2026-08-20→09-27) ולא "טורוביץ׳" (עדיין כתוב בפריימי הספונסר בפיגמה).
  - ⚠️ אם בקובץ **אתר** (HTML/JSON/JS) עדיין מופיע "טורבוביץ׳" — זה עותק שלא עודכן, לא ראיה נגדית: לתקן אותו לכתיב הקנוני. אזכורי "לא לשחזר" בתיעוד ובארכיון `docs/history/` נשארים כמו שהם.
- **אחרי הגוף, לפי הסדר:**
  - divider: ‏`#D2D2D2` בדסקטופ. **מוצג גם במובייל** — שם `#EFEFEF`, ‏`padding 24/32/0` (בניגוד ל-soos).
  - `www.sumiiworld.com`: ‏Copperplate UPPERCASE, ‏14px (מובייל 13; בפיגמה 18/16).
  - קרדיט: דסקטופ "אוצרות: " / מובייל "אוצרת התערוכה - ".
    - ההחלפה דרך `.only-d`/`.only-m`.
    - השם "קורין אברהם" מקושר ל-`curators/korin-avraham/` בשני הנוסחים.
- **hero 492×744:**
  - **אין scrim בשני ה-breakpoints** — בפיגמה אין שכבת כהות, והתמונה כהה מעצמה.
  - אוברליי לבן ממורכז ב-`top:50%`. דסקטופ: שם הגלריה ‏23px (בפיגמה 30) / X ‏36 / לוגו 87.97×40.
  - מובייל: ‏18px (בפיגמה 24) / X ‏28.8 / לוגו 70.38×32, ‏`gap:6.4px`, ‏`width:286.4px`.
- **תמונת ה-hero:** ‏`images/sponsors/sumii/hero.{webp,avif}` ‏1620×2160, + וריאנטים 480/768/1080.
  - זה "חלון-איחוד" באספקט המובייל 3:4: קרופ מרכזי 2025×2700 מהמקור 2160×2700.
  - ה-`cover` בדסקטופ משחזר את קרופ הפיגמה. במובייל רואים את הקובץ במלואו.
  - **לא לחתוך מחדש לאספקט הדסקטופ.**

### FIGURES — 3 היצירות של shira-turbowicz
- **מיקום:** בדסקטופ סקשן אפור (`1637:213`). במובייל הכרטיסים זורמים לתוך העמודה הלבנה.
- **גריד:**
  - 3 עמודות, `--col-gap:87px` (1248−3×358=174 → 87; בטאבלט 48).
  - `direction:rtl`. סדר ה-DOM — גאיה → סוניה → ניקי — הוא סדר הקריאה RTL, וגם סדר המובייל. בדסקטופ ניקי יוצאת משמאל.
- **תא:**
  - `aspect-ratio:358/434.17` ב-`object-fit:cover` (= FILL ממורכז בפיגמה).
  - ממחזר את `images/works/v2/shira-turbowicz-1..3` ‏(832×1208 + 480/768).
  - מקשר ל-`works/shira-turbowicz-N/`.
- **כותרת:**
  - המבנה: `<שם> | <bdi dir="ltr">שנים</bdi> | <span class="lat">title_en</span>`, מתוך `works.json`. ה-`title_en` נוסף ל-3 היצירות ("Gaia" / "Sonia Delaunay" / "Niki de Saint Phalle") בשביל הכיתוב הזה.
    - ה-`title_he` ב-`works.json` כבר כולל את השנים ("סוניה דלונה | 1885–1979"). בהעתקה ידנית — לעטוף את קטע השנים ב-`<bdi>`, לא להדביק verbatim. גאיה ("גאיה, אלת האדמה") בלי שנים.
  - FbEzmel Regular 20 verbatim.
  - השם הלועזי ב-`<span class="lat">` ‏(.88em ≈ 17.6px — מתאים לכיול שנמדד).
  - שנות-החיים ב-`<bdi dir="ltr">` ‏(`1885–1979`, `1930–2002`). הפיגמה מרנדרת אותן הפוך ("2002–1930") — לא לשחזר.
- **תיאור:**
  - FbEzmel Light 16 עם `white-space:pre-line`.
  - 🔴 **שבירות השורה הממשיות ב-HTML הן תוכן.** לא להזיח, לא לעצב מחדש ולא לאחד שורות.
- **ריווח:** תמונה → 24 → כותרת → 24 → תיאור, בשני ה-breakpoints.
- 🔴 **"Sonia Delaunay".** בפיגמה (`1637:229` / `1589:5705`) כתוב "Sonia Delaun" — קיטוע.
  - תוקן בעמוד וב-`works.json` (`shira-turbowicz-2.title_en`).
  - לא לשחזר.
- **מקור הטקסטים:** התיאורים קיימים **רק כאן**, מפריים הספונסר. ב-`works.json` ה-`details_he` הוא שורת החומר הטכנית.

### פאנל מלאני
- **פריסה = מראה הפוכה של sumii:** הלוקאפ משמאל והטקסט מימין, על רקע לבן.
  - הלוקאפ יושב בתוך כרטיס 492 **לבן בלי תמונה**. בפיגמה זו תיבה ריקה של 492×744, והלוקאפ ב-`x55 / y42.83`, רוחב 372, ‏`gap:16`.
- **לוקאפ דסקטופ, מלמעלה למטה:**
  - לוגו raster ‏224.98×129.16 → `https://www.melanihekimoglu.com`.
  - X ‏`44.7998px` verbatim.
  - שם הגלריה: ‏35.6407 בפיגמה → ‏**31px**. בשורה 1 ‏`letter-spacing:.05em`.
  - `white-space:nowrap` בדסקטופ ובטאבלט (לא במובייל) — בפיגמה צומת הטקסט hug וגולש מתיבת ה-372.
- **טאבלט:** לוגו 190×109.1, X ‏38, שם ‏26, ‏`margin-left:0`.
- **מובייל:** הלוקאפ הופך ל**שורה** צמודת-ימין — לוגו 134×126, X ‏20.1117, שם 13px.
  - שם עם `white-space:normal`. ‏`nowrap` היה חותך מתחת ל-390.
- **הלוגו:** ‏`images/sponsors/melani/logo.{webp,avif}` ‏450×258. **בעמוד הזה raster, לא SVG** (בהומפייג' יש גם עותק וקטורי לבן — ראו Assets).
  - זה הקרופ ההדוק מ-cropTransform `7f17b2` של `1637:350` (ה-favicon.png שהמעצבת העלתה).
  - ה-imageRef בפריים המובייל הוא קובץ אחר, אבל אותה תמונה (נבדל רק באלפא). משתמשים בקובץ הקיים.
- **גוף — 7 פסקאות:**
  - פסקת הפתיחה `.lede` = FbEzmel **Regular בשני ה-breakpoints** (Figma ts4 / ts2). השאר Light.
  - תאריכים ב-`<bdi dir="ltr">`.
  - קישורים: "ארז זילינסקי רוזן" (האזכור הראשון בלבד, פסקה 1) → `about/`. "מלאני הקימוגלו" בשם מלא (פסקאות 1 ו-2) → `artists/melani-hekimoglu/`.
- **אחרי הגוף:** divider + `www.melanihekimoglu.com` + "אוצרת התערוכה - קורין אברהם" (מקושר).
  - הנוסח **זהה בשני ה-breakpoints**, בניגוד ל-sumii.

### מוצרי מלאני (FLOW / BLOOM)
- **גריד:** 5 כרטיסים ב-3 עמודות, ‏`row-gap:64px`.
- **השורה השנייה בעמודות 2–3:** ‏`.prod:nth-child(4){grid-column:2}`, ‏`.prod:nth-child(5){grid-column:3}`.
  - בפיגמה זו שורת flex-end עם gap 87, שנופלת בדיוק על רשת העמודות.
- 🔴 **ל-`.prods` אין `direction:rtl`** (בניגוד ל-`.figs`).
  - סדר ה-DOM = סדר הפיגמה: plates (4), vases (1), dessert-bowl (2), lamp (5), planter (3).
  - הוספת `rtl` תזיז את השורה השנייה.
- **תמונות:** ממחזר את `images/works/v2/melani-hekimoglu-1..5` ומקשר ל-`works/melani-hekimoglu-N/`.
  - **אין קבצים כפולים תחת `images/sponsors/melani/`** — שם יש רק את הלוגו.
- **כותרת:** Copperplate Regular. ‏20 בפיגמה → ‏**17.5px** (כיול-מדידה). UPPERCASE מהכלל הגלובלי.
- **תיאור:** FbEzmel Light 16, ‏`pre-line` — אותו כלל שבירות-שורה כמו ב-FIGURES.
- **טקסט bloom planter:** זהה verbatim לטקסט של flow vases ("כל אגרטל משתנה…").
  - זה copy-paste של המעצבת (Figma `1641:398`). נשמר verbatim — פתוח ב-`docs/todo.md`.
- **ריווח במובייל:**
  - 64px בין כרטיסים (`padding-top:64`; הראשון 24, ממשיך את קצב ה-24).
  - כותרת → תיאור: **8px** (בדסקטופ 24).

### `the curator`
- דפוס רצועת האומנים של דפי האירועים, עם כרטיס יחיד → `curators/korin-avraham/`.
- label: ‏28px (מובייל 16).
- כרטיס: 178×148 (מובייל 96×80, רוחב כרטיס 112).
- שם: אפור `#828282`, ‏18px (מובייל 13).
- **thumb:** ‏`images/sponsors/sumii/curator-thumb.{webp,avif}` ‏712×561.
  - נאפה מקרופ הפיגמה `1b9e5e` של `7f582c67…` — אותו צילום של פורטרט האוצרת.
  - ה-fill השני בכרטיס (`889e3ab7…`, צילום של זוהר רון) = leftover מוסתר. **לא להשתמש בו.**

### סדר המובייל (`order` 1–21)
- 1: hero.
- 2: צ'יפ.
- 3: לוקאפ sumii.
- 4: גוף sumii.
- 5–7: שלוש ה-figures.
- 8–10: divider / אתר / קרדיט של sumii. ל-`.sp-credit--sumii` יש `padding-bottom:0`.
- 11: לוקאפ מלאני.
- 12: גוף מלאני.
- 13–17: חמשת המוצרים.
- 18–20: divider / אתר / קרדיט של מלאני.
- 21: `the curator`.

### דאטה ומה לסנכרן
- **`sponsors.json`:**
  - רשומה `sumii`: ‏`figma_node_desktop:"1637:134"`, ‏`curator_slug:"korin-avraham"`, ‏`date_start`/`date_end`, ‏`founder_artist_slug:"shira-turbowicz"`, ‏`case_exception:[]`.
  - רשומה `melani-hekimoglu`: עם **`route:"sponsors/sumii/"`** — חולקת את העמוד, אין לה route משלה.
    - `founder_artist_slug:"melani-hekimoglu"`.
    - `cover_image` = `images/works/v2/melani-hekimoglu-4.webp`.
  - **הסדר: `sumii` לפני `melani-hekimoglu`** (ראו SEO).
  - `curator_slug` הוא meta בלבד. רצועת `the curator` בעמוד כתובה ידנית ב-HTML — שינוי בשדה לא ירנדר אותה מחדש.
    - ⚠️ ה-`_note` ב-`sponsors.json` ("renders a 'the curator' strip") ו-`docs/data-contracts.md` §12 מנוסחים כאילו השדה מרנדר רצועה — בעמוד הספונסר זה לא נכון: שום קוד בעמוד לא קורא את `sponsors.json`. השדה שכן מרנדר רצועה הוא `artists.json :: curator_slug`, בדפי האומן. כאן החלפת אוצרת = עריכת ה-HTML של `.sp-curator`.
- 🔴 **כרטיסי FIGURES ו-PRODUCTS הם עותקים ידניים של `works.json`.** הם מעתיקים את נתיב התמונה, `width`/`height`, רוחבי ה-srcset, הכותרות והקישור `works/<id>/`.
  - **כל שינוי ב-8 הרשומות האלה** (`shira-turbowicz-1..3`, `melani-hekimoglu-1..5`) נעשה כך:
    1. לערוך את `data/works.json`.
    2. להריץ `python3 tools/sync_data.py`. הסקריפט מעדכן את `#works-data` בגריד `/works/`, את `#artwork-data` בעמודי היצירה, את `#g-artworks-data` בדף דיזינגוף ואת `data/generated/*.js` (שדפי האומנים טוענים — הדפים עצמם לא נערכים).
    3. **ולערוך ידנית את `sponsors/sumii/index.html`.**
  - טקסטי המוצרים קרובים ל-`details_he` אבל לא זהים. למשל `מנורות <span class="lat">Flow</span>.` כולל נקודה ו-span — להשוות לפני העתקה.
- **ה-route קבוע.** היצירות `shira-turbowicz-1..3` נושאות `exhibition_route:"sponsors/sumii"` + `kind:"residency"`, ולכן כותרת הקבוצה בדף האומנית ועמודי היצירה מקשרים לכאן.
  - לעולם לא לשנות את ה-slug (כלל-זהב 6).

## Related pages — מקשרים לכאן או מעתיקים מכאן

הכללים שלהם נמצאים ב-route docs שלהם.

- **הומפייג' `index.html`:**
  - `#sumii` (`homepage.json :: sumii_sponsor`) — מקשר ל-`sponsors/sumii/`, ומשתמש ב-`hero-thumb`, ‏`gallery-02` ו-`gallery-01` של sumii.
  - `#soos` (`homepage.json :: soos_sponsor`) — מקשר ל-`sponsors/soos/`, ומשתמש ב-`gallery-01..03` של soos. כולל את תיקון `.soos-line--model{direction:rtl}`.
  - `#exhibitions-now` (קבוצת `tel aviv`, 2026-09-27) — כרטיס דיזינגוף = רזידנסי SUMII → `sponsors/sumii/`. משתמש ב-`images/sponsors/sumii/hero.webp` + ‏`hero-{480,768,1080}w` (srcset מלא), ובאוברליי שני לוגואים לבנים inline — `svg.res-sumii` ו-`svg.res-melani`.
  - → `docs/routes/homepage.md`.
- **`galleries/dizengoff/`:** כרטיס רזידנסי SUMII במירור הידני `#g-exhibitions-data`. הרשומה קיימת **רק שם**, עם `kind:"residency"` ו-`route:"sponsors/sumii/"`.
  - התמונה: `images/sponsors/sumii/hero-768w.webp`.
  - `dates_text` כתוב verbatim סוף→התחלה — פתוח ב-todo.
  - → `docs/routes/galleries.md`.
- **`events/` — חמשת דפי האירוע של רזידנסי SUMII** (וריאנט אירועים בלי תערוכה, כיכר דיזינגוף): `niki-de-saint-phalle-day` (עמוד הבסיס), `sumii-opening`, `sumii-melani-hosting`, `yom-kippur-wish-tree`, `sumii-live-studio`.
  - בכל אחד: לוגו Sumii → `sponsors/sumii/`, דרך עותק של `<symbol id="sumii-mark">` (ראו Assets).
  - `sumii-opening`: ההירו = `images/sponsors/sumii/hero.*` (srcset מלא), והקובץ הוא גם ה-`cover_image` שלו ב-`events.json` (ראו SEO — מפתח og-dims משותף).
  - `sumii-melani-hosting`, `sumii-live-studio`: לוגו מלאני raster ‏(`images/sponsors/melani/logo.webp`, ‏`img.melani-logo`).
  - כולם מחווטים: `route` ב-`events.json` וב-`press.json`, מירור `#events-list-data`, כרטיס ב-`press/index.html`, sitemap.
  - → `docs/routes/events.md` (הוריאנט של רזידנסי SUMII), `docs/routes/press.md`.
- **`artists/shira-turbowicz/`, ‏`artists/melani-hekimoglu/`:** רצועת `the curator` שלהם ממחזרת את `curator-thumb.webp`. → `docs/routes/artists.md`.
- **`works/shira-turbowicz-*`, ‏`works/melani-hekimoglu-*`:** → `docs/routes/works.md`.

## Assets — לא למחוק ולא לשנות שם

- **`images/sponsors/sumii/`:**
  - `hero.*` + ‏`hero-{480,768,1080}w.*` — עמוד הספונסר.
    - `hero-768w.webp` משמש גם את כרטיס דיזינגוף.
    - גם כרטיס `#exhibitions-now` בהומפייג' (`img.ex-now-photo` — כל הוריאנטים ב-srcset).
    - גם ההירו של `events/sumii-opening/` (כל הוריאנטים ב-srcset) + ה-`cover_image` שלו ב-`events.json`.
    - `hero.webp` רשום ב-`og-dims.json` — מפתח משותף לעמוד הספונסר ול-sumii-opening (ראו SEO).
  - `hero-thumb.*` (נוצר עבור ההומפייג'), ‏`gallery-01.*`, ‏`gallery-02.*` (הוסרו מעמוד הספונסר ב-2026-08-23) — **בשימוש בהומפייג' `#sumii`**.
  - `gallery-03.*` — לא בשימוש בשום מקום. נשאר בדיסק (כלל-זהב 8).
  - `curator-thumb.*` — העמוד הזה + מפת `var CURATORS` ב-`artists/shira-turbowicz/index.html` וב-`artists/melani-hekimoglu/index.html` (נתיב + `w:712,h:561` — אם משתנה, לעדכן בשתיהן).
  - `sumii-logo.svg` — עותק-ייחוס (`sponsors.json :: logo`).
- **`images/sponsors/soos/`:**
  - `hero.*` + וריאנטים (ו-`og-dims.json`).
  - `gallery-01..03.*` — העמוד + **הומפייג' `#soos`**.
  - `gallery-04.*` — העמוד.
  - `soos-logo.svg` — עותק-ייחוס (`sponsors.json :: logo`).
- **`images/sponsors/melani/logo.*`** — עמוד הספונסר (`.mel-logo`) + ‏`img.melani-logo` ב-`events/sumii-melani-hosting/` וב-`events/sumii-live-studio/`.
- 🔴 **הלוגואים הווקטוריים הם עותקים ידניים. אף דף לא טוען את קובצי ה-`.svg`.** ‏`soos-logo.svg` ו-`sumii-logo.svg` הם נכס-ייחוס בלבד (`sponsors.json :: logo`), וכך גם `images/homepage/ex-now/{sumii,melani}-mark-white.svg`.
  - **Sumii** (נכון ל-2026-09-27: 9 עותקים ב-8 קבצים):
    - `<symbol id="sumii-mark">` זהה בשבעה קבצים, תמיד מיד אחרי `<site-header>`: `sponsors/sumii/index.html` (המקור), `galleries/dizengoff/index.html` (בשימוש של `.gx-res-logo`), וחמשת דפי אירועי הרזידנסי — `events/{niki-de-saint-phalle-day,sumii-opening,sumii-melani-hosting,yom-kippur-wish-tree,sumii-live-studio}/index.html` (בשימוש של `.sumii-logo`).
    - `<path>`-ים inline, בלי symbol, ב-`index.html` `#sumii` (`.sumii-logo`).
    - `svg.res-sumii` inline ב-`index.html` `#exhibitions-now` (לבן, viewBox `0 0 114 52`; מקור `images/homepage/ex-now/sumii-mark-white.svg`). ⚠️ העותק הזה עדיין כולל את path הזבל `fill-opacity:.05`.
  - **מלאני:**
    - raster — `images/sponsors/melani/logo.webp`, בשלושה דפים (ראו למעלה). החלפה במקום (אותו שם קובץ) מעדכנת את שלושתם. לוגו חדש בשם חדש (כלל-זהב 8) = לעדכן את כל ה-`<img>`-ים.
    - וקטור — `svg.res-melani` inline ב-`index.html` `#exhibitions-now` (לבן, viewBox `0 0 151 88`; מקור `images/homepage/ex-now/melani-mark-white.svg`). נערך בנפרד.
  - **soos** (2 קבצים): SVG inline פעמיים ב-`sponsors/soos/index.html` (לוקאפ + hero) + פעם אחת ב-`index.html` `#soos` (`.soos-logo`).
  - **החלפת לוגו = לערוך את כל העותקים** (ולעדכן גם את קובץ ה-`.svg` לשם הסדר). עריכה של קובץ ה-`.svg` בלבד לא משנה דבר באתר.
  - **לפני החלפת לוגו — למצוא את כל העותקים, לא לסמוך על הרשימה:** `grep -rln 'sumii-mark\|res-sumii\|sumii-logo\|soos-logo\|res-melani\|melani/logo' --include='*.html' .` — דפים חדשים מעתיקים את ה-symbol ואת ה-`<img>`, והרשימה למעלה מתיישנת. הפלט הזה, אחרי הורדת ה-`./` (ראו אימות), הוא גם רשימת ה-`--only` לצילום ה-regress.

## Open issues (`docs/todo.md`)

- **חשדות לטעויות כתיב בפיגמה, בגוף של sumii (הועתקו verbatim, טעונים אישור מעצבת/לקוח):**
  - "במרכזו אובייקטים **בפסל חומר** מפוסל ביד".
  - "נשיות דרך צורה, קימור **ובשם**".
- **"טורוביץ׳"** עדיין מופיע בפריימי הספונסר בפיגמה — לתקן שם (לכתיב "טורבוביץ"), לא באתר.
- **"Sonia Delaun" → "Sonia Delaunay".** אם המעצבת התכוונה אחרת: לערוך את `works.json` → `python3 tools/sync_data.py` → ולתקן ידנית את כרטיס FIGURES בעמוד.
- **טקסט bloom planter שהועתק מ-flow vases.** כשיוכרע: לערוך את `details_he` ב-`works.json` → `python3 tools/sync_data.py` → ולערוך ידנית את כרטיס המוצר בעמוד.
- **סדר תאריכי הרזידנסי לא עקבי בפיגמה** (הועתק verbatim בכל מקום, טעון הכרעת מעצבת). כאן ובהומפייג' כתוב התחלה→סוף; בכרטיס דיזינגוף כתוב סוף→התחלה. אם המעצבת תיישר — לעדכן את `dates_text` במירור הידני `#g-exhibitions-data` בדף דיזינגוף.
- **`inject.py` בהרצה גורפת עדיין שבור.** הענף של `sponsors/` תקין — להריץ רק עם נתיבים.
- **צ'יפ soos → `/#galleries`** — תצפית, לא הוכרע ואינו רשום ב-`docs/todo.md` (ראו למעלה). אם מוכרע לשנות — להוסיף ל-todo.

## Removed / do not restore

- **רצועת הגלריה של 3 התמונות בעמוד sumii** — הוסרה ב-2026-08-23. היא לא קיימת באף אחד משני הפריימים. הקבצים נשארו (ראו Assets).
- **סנכרון soos מול `1318:3287`/`1318:3480`** — שם יושב עכשיו עיצוב sumii. וגם `1318:3287` כמקור לדסקטופ של sumii — הוחלף ב-`1637:134`.
- **הפריימים הריקים במובייל של soos** — `1318:3523` (Banner Text Container) ו-wrappers ריקים בשורות הקרדיט (`1318:3617`/`1318:3621`).
  - אלה שרידי תבנית ה-artist-talk. לא נבנו, ואין לבנות אותם.
- **המצב "שירה טורבוביץ בלי קישור"** — בוטל ב-2026-08-20, כשקיבלה דף אומנית. גם הכתיבים "טורוביץ׳" ו-"טורבוביץ׳" (עם גרש) לא חוזרים.
- **"Sonia Delaun"**, ושנות-חיים וטווחי תאריכים בסדר bidi הפוך.
- **ה-fill `889e3ab7…` (זוהר רון) כ-thumb לאוצרת.**
- **`.brand` ב-`.82em`**, ושורת המודל של soos ב-LTR.
- **מחלקה בשם `logo`.**
