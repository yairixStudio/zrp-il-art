# About — route notes

> לקרוא לפני עריכה של `about/index.html` (וגם של `images/about/`). המסמך מתאר את המצב הנוכחי ואת הכללים הפעילים. ההיסטוריה נמצאת ב-`docs/history/CLAUDE-2026-09-27.md` §4.

## Pages

- `/about/` ("Biography of Erez") → `about/index.html` · ✅
  - Figma desktop: `XhGH...::1699:1406` ("biography-erez-desktop")
  - Figma mobile: `XhGH...::1699:1291` ("biography-erez-mobile")
  - Legacy frames: `Zn3N...::1213:2970` / `Zn3N...::1213:2888`. הם הוחלפו ברה-דיזיין המלא של 2026-09-01. **לא בונים מהם.**
  - Nodes לפי סקשן (desktop / mobile):
    - hero: `1699:1432` / `1699:1313`
    - carousel: `1699:1447` / `1699:1324`
    - bio: `1699:1460` (desktop). במובייל — בלוק התמונה `1699:1345`
    - quote: `1699:1477` (desktop). במובייל — תמונת הטלפון `1699:1357`, טקסט הציטוט `1699:1360`
    - close: `1699:1484` (desktop). במובייל — חלון הראווה `1699:1355` (358×566)
    - ⚠️ במובייל אין node נפרד לכל סקשן: hero עד הציטוט יושבים כולם בתוך סקשן אחד, `1699:1312`.
    - korin: `1699:1506` / `1699:1362`. טקסט הביו: `1699:1523` / `1699:1378`
    - natalie: `1699:1524` / `1699:1379`
  - קישורי Figma מלאים: `FIGMA_LINKS.md` § "אודות / Biography of Erez".

## 🔴 אין דאטה — HTML סטטי כתוב ביד

- כל התוכן כתוב ישירות ב-HTML: הביו, הציטוט, קורין ונטלי. אין מקור JSON.
- `python3 tools/sync_data.py` לא נוגע בעמוד, ואין לו רשומה ב-Mirror registry. שינוי תוכן = עריכה ישירה של `about/index.html`, בלי שום צעד סנכרון.
- פריט ה-nav מרונדר **hardcoded** ב-`components/site-chrome.js` (`abs('about/')`, וזיהוי הפריט הפעיל לפי ה-path). שינוי תווית או נתיב = עריכה של `site-chrome.js`. הרשומה `about` ב-`data/site.json` (`nav[]`) היא **דקלרטיבית בלבד**: אף קוד לא קורא אותה בזמן ריצה. מעדכנים אותה רק לשם עקביות.
- ⚠️ **כפילויות שמתוחזקות ביד. אם משנים את המקור, לעדכן גם כאן:**
  - הידית של קורין `@yasalamfashionblog` מופיעה גם ב-`data/curators.json` (`instagram_handle`). גם הפורטרט שלה כאן הוא קובץ **נפרד**: `images/about/people/korin-avraham.*`, ולא `images/curators/korin-avraham/portrait.webp`.
  - הפרטים של נטלי מופיעים גם ב-`data/galleries.json::manager`. בעמוד הזה הפורטרט הוא קובץ **נפרד**: `images/about/people/natalie-zigel.*`, ולא `images/galleries/managers/natalie-zigel.*`.
  - ה-`mailto` כאן הוא `Nataliesiegel8@gmail.com` עם N גדולה, ואילו ב-JSON הכתובת כולה באותיות קטנות.

## מבנה

### תוכן (2026-09-01)
- ביו חדש: 6 פסקאות. האחרונה נפתחת ב"כדבריו של ארז:" ואחריה ציטוט.
- intro מעודכן בהירו.
- פס הציטוט האפור והחתימה האנכית הוסרו (ראה בסוף המסמך).

### דסקטופ
- כל סקשן תוכן (חוץ מ-`.about-tri`) מכיל `.row`: עמודת תמונה `492px` ועמודת טקסט שממלאת את השאר, `gap:48`. בעמודת הטקסט יש padding `0 16`. הצדדים מתחלפים בין הסקשנים.
- סדר הסקשנים:
  1. `.about-hero`: תמונה | טקסט. הטקסט = ידית IG, `h1` ("Make you feel like Art"), `intro-he`.
  2. `.about-tri`: קרוסלה.
  3. `.about-bio`: טקסט | תמונה. הטקסט בעמודה של `574px` שצמודה לימין (`align-items:flex-end`). מסגרת התמונה ביחס `492/739`.
  4. `.about-en`: תמונת הטלפון | ציטוט אנגלי.
  5. `.about-close`: הלוגו `images/brand/logo.svg` ברוחב **446px** | חלון הראווה.
     - `images/brand/logo.svg` הוא נכס משותף: הוא גם לוגו ה-Organization ב-JSON-LD של האתר (`index.html`, ו-`ORG.logo` ב-`tools/seo/inject.py`). הקובץ עצמו 177×37, והעמוד מגדיל אותו רק דרך `width="446"` ו-`.brandmark{width:min(446px,100%)}`. **לא להחליף ולא לייצא מחדש את הקובץ בשביל העמוד הזה.** (זה לא הלוגו של ה-header, שהוא קובץ אחר: `images/header:footer:general/logo.svg`.)
  6. `.about-person--curator` (קורין): תמונה | טקסט. הביו ממורכז.
  7. `.about-person--manager` (נטלי): טקסט | תמונה.
- בשני סקשני האנשים מסגרת הפורטרט היא `492×652` (`aspect-ratio:492/652`). בפיגמה היא ממורכזת במשבצת של 744. בקוד אין משבצת כזו: `.img-col{align-items:center}` ממרכז את המסגרת לגובה ה-row.
- 🔴 `picture-upgrade.js` עוטף בזמן ריצה ב-`<picture>` כל `<img>` שה-`src` שלו `.webp`/`.png` (ה-`logo.svg` לא נעטף). לכן אסור להסיר את `.about .img-frame picture{display:contents}` (ובמובייל גם את `.about-bio .img-frame picture{display:block;width:216px;height:378px}`), אחרת התמונות מאבדות את המסגרת.
- בהירו, בציטוט ובסקשן הסגירה גובה התמונה `744px`. ב-769–1100 הוא יורד ל-`574px`, ועמודת התמונה ל-`380px` (הכלל כתוב `max-width:1100px`, אבל בלוק ≤768 דורס אותו).

### מובייל (≤768)
- הסדר נקבע דרך `order` על הסקשנים: hero 1 → tri 2 → bio 3 → **close 4 → en 5** → curator 6 → manager 7. כלומר `about-close` ו-`about-en` מתחלפים: חלון הראווה מופיע לפני הטלפון והציטוט.
- **הצילום באמצע הביו:** הביו מפוצל ב-HTML ל-`.bio-a` (פסקאות 1–3) ול-`.bio-b` (פסקאות 4–6). במובייל `.text-col` ו-`.bio-text` מקבלים `display:contents`, ואז `order`: `bio-a` → `img-col` → `bio-b`. כך הצילום יושב בין שני החצאים בלי לשכפל תוכן. **לא לאחד את `bio-a`/`bio-b` לבלוק אחד.**
  - הצילום מוצג בגודל `216×378`, ממורכז בתוך בלוק לבן בגובה `443px`.
  - ב-`.bio-b` יש `.qspacer`: קו אנכי `var(--divider)` = `#D8D8D8`. הוא מוצג **במובייל בלבד** (בדסקטופ `display:none`).
- חלון הראווה בגודל `358×566` (`aspect-ratio:2589/4095`). **הלוגו מוסתר במובייל** (`.about-close .text-col{display:none}`).
- שאר המסגרות במובייל: hero ואנשים `aspect-ratio:358/448`, הטלפון `358/447.44`.
- בסקשני האנשים התמונה מופיעה ראשונה (`img-col{order:-1}`) ואחריה הלוקאפ הממורכז.
- `.dbr` הוא `<br>` לדסקטופ בלבד: שבירות ה-Figma ב-intro. במובייל הטקסט זורם.

## קרוסלה (`.tri` — קומפוננטה משותפת, `docs/components.md` §4)

- **7 שקופיות** בסדר ה-DOM הזה: `tri-left`, `tri-center`, `tri-right`, `erez-hero`, `erez-bio`, `erez-quote`, `erez-closing-v2`.
- `data-tri-start="1"`: הקרוסלה נפתחת על `tri-center`, עם `tri-left` ו-`tri-right` כ-peeks. זו השלישייה שמצוירת בפריים. **שלוש השקופיות האלה חייבות להישאר עוקבות, ו-`data-tri-start` חייב להצביע על האמצעית** (כרגע אינדקסים 0–2 ⇒ `data-tri-start="1"`). אם מזיזים אותן, מעדכנים את `data-tri-start`.
- 7 דוטים = 7 שקופיות. אין סנכרון אוטומטי: הוספה או הסרה של שקופית מחייבת להוסיף או להסיר `button.tri-dot` ביד (components §4.7).
- הדוטים הם פסים בצבעים `--tri-dot-color:#EEF0EF` ו-`--tri-dot-active:#515151`. הם מוצגים **מעל 768** (דסקטופ וטאבלט). במובייל (≤768) `display:none`, swipe בלבד. לגבי הרוחב בפועל ראה בעיות פתוחות.
- גאומטריה: דסקטופ ומובייל זהים ל-`events/noemi-safir` (ול-`events/livay-levi`). הטאבלט (769–1319) הוא **דפוס `events/livay-levi`**: מדרגה אחת, בלי מדרגת ≤1050 של noemi-safir. **לא להעתיק את ערכי הטאבלט של noemi-safir.**
  - ≥1320: מרכז `481×841`, peeks `302×528` ב-`opacity:.6`, ממוקמים ב-`±472.5px`. בטווח 1320–1439 ה-row צר מ-1248 וה-peeks נחתכים בקצוות. זה מקובל ומכוון.
  - 769–1319: מרכז `380×665`, peeks `239×417` ב-`±373.5px`.
  - מובייל: מסגרת בגובה `443`, מרכז `216×378`, peeks `117×204.75` ב-`±194.5px`.

## טיפוגרפיה — כיולים אופטיים (Figma → קוד)

- 🔴 הכיולים **נמדדו מול רינדורי הפריימים** ואינם יחס קבוע. לפני שמשנים ערך קוראים את `docs/lessons.md` 2026-09-01: בדף כיול חובה `document.fonts.load` מפורש לכל משקל. ובדיקות טיפוגרפיה נעשות **רק ב-http**, כי ב-file:// ה-`@font-face` חסום.
- הערכים הנוכחיים:

  | רכיב | Figma | קוד | הערות |
  |---|---|---|---|
  | כותרת `h1` | 80 | **60** | |
  | כותרת `h1` במובייל | 24 | **19** | |
  | לוקאפ השם על ההירו (`.name-overlay`) | 40 | **33** | `letter-spacing:.22em`, `line-height:41px`. `right/bottom` = 24 בדסקטופ, 16 במובייל |
  | שמות האנשים (`.p-name`) | 80 | **64** | |
  | שמות האנשים במובייל | 36 | **27** | |
  | ידית IG בהירו | 28 | **21** | |
  | ידית / אימייל אצל האנשים (`.p-handle`) | 28 | **24** | |
  | ציטוט אנגלי (`.qbody`) | 18 | **15.5** | המרכאות (`.qmark`) 40 **verbatim** |

- מדרגות ביניים (לא לבטל):
  - 769–1100 (הכלל כתוב `max-width:1100px`, אבל בלוק ≤768 דורס את כל הערכים שלו): `h1` 45, לוקאפ 25/32 בהיסט 18, שמות 48, ידיות 16/19, ביו 19, ו-`.bio-text` ברוחב 100% במקום 574.
  - מובייל (≤768): ידיות 12/14, ציטוט 14. **הלוקאפ חוזר במפורש ל-33/41 בהיסט 16** (ולא 25/32). הדריסה הזו נדרשת כדי לבטל את מדרגת ≤1100, **ולא למחוק אותה כמיותרת**.
  - ≤360: לוקאפ 30/37, `h1` 17.
- עברית (FbEzmel) = **ערכי ה-px של Figma כמו שהם**, עם `line-height` שנמדד מהפריימים ולא ברירת המחדל של הדפדפן:
  - ביו: 22/1.09. מובייל: 16/1.06.
  - intro ופסקאות האנשים: 18/1.06, ממורכזים. מובייל: 16, **מיושרים לימין** (`text-align:right`).
  - הרווח בין פסקאות **הביו** (`--pgap`, רק ב-`.about-bio`): 24 בדסקטופ, 17 במובייל. בפסקאות האנשים (`.p-bio`) הרווח הוא `gap` של 19px בדסקטופ ו-17px במובייל.
- בביו:
  - "ארז זילינסקי רוזן" בפתיחה = `.lead` (משקל 400).
  - `ZIELINSKI & ROZEN` = `<span class="lat">`: Copperplate 300, `.88em`.
- ⚠️ ה-`textCase:LOWER` שבפריימים **נדחה**. כלל ה-UPPERCASE הגלובלי גובר.
- 🔴 `.about-hero h1{max-width:680px}` (2026-09-01, אחרי הרה-דיזיין). ב-1440 עמודת הטקסט היא 676px. מעל 1440 היא מתרחבת, עד 868px כשה-row נעצר על 1440 (בוויופורט ≥1632). הרוחב המרבי שומר על שבירת השורות של "Make you feel like Art" גם מעל 1440. **לא להסיר.**

## תמונות ו-scrim

- **כל 9 התמונות שבפריימים ממוחזרות** (הותאמו לקבצים קיימים ב-`images/about/`): `tri-left`, `tri-center`, `tri-right`, `erez-hero`, `erez-bio`, `erez-quote`, `people/korin-avraham`, `people/natalie-zigel`, וחלון הראווה = `erez-closing` (המקור — כבר לא מקושר; מוגש היום **רק** דרך הקרופ `erez-closing-v2`, ראה למטה).
- נאפו שני קרופים חדשים מה-Figma:
  - `erez-closing-v2.{webp,avif}` + וריאנטים (crop `3bb3a4`): חלון הראווה. משמש **גם** בסקשן הסגירה **וגם** כשקופית 7 בקרוסלה.
  - `erez-bio-crop.{webp,avif}` + וריאנטים (crop `7dd04d`): התמונה של סקשן הביו.
- המקורות הישנים נשארים בדיסק (כלל-זהב 8):
  - `erez-bio.*` עדיין בשימוש כשקופית בקרוסלה.
  - `erez-closing.*` (הישן, 1500×2000) כבר לא מקושר מאף מקום. הקרופ הנוכחי הוא `erez-closing-v2`. לא למחוק.
- LCP = `erez-hero` בהירו (`fetchpriority="high"`). כל שאר התמונות `loading="lazy"`.
- scrim:
  - הירו בדסקטופ: `linear-gradient(0deg, rgba(0,0,0,.7), transparent)`.
  - הירו וקורין במובייל: `linear-gradient(0deg, #000 0%, rgba(27,27,27,0) 55%)`. לקורין **אין** scrim בדסקטופ.
  - נטלי: בלי scrim בשום breakpoint.
- OG/SEO: בלוק `<!-- SEO:auto -->` נוצר במקור ע"י `tools/seo/inject.py`. ענף `about` מייצר `AboutPage` + `Person`, ו-og:image = `DEFAULT_OG` ⇒ `og/homepage-hero-landscape.jpg` (דרך `og-dims.json`). אין OG ייעודי לעמוד.
  - 🔴 **הבלוק נערך ביד ברה-דיזיין 2026-09-01. לא להריץ `inject.py` על העמוד.** הרצה של `inject.py about/index.html` דורסת בשקט:
    - את `jobTitle` ב-JSON-LD: מ-"Founder & Perfumer & Culture Curator" חזרה ל-"Founder & Artist" (הערך מקודד בענף `about`).
    - את `<meta name="description">`, `og:description` ו-`twitter:description`: שלושתם מוחלפים בטקסט הישן "…אמן ומייסד…". מקור הטקסט הישן הוא רשומת `"/about/"` ב-`tools/seo/overrides.json`.
    - היום `twitter:description` קצר יותר מ-`og:description`. הרצה תאחד את שניהם לאותו טקסט.
  - שינוי SEO = עריכה ידנית של הבלוק. כדי לחזור לכלי, קודם מעדכנים גם את ענף `about` ב-`inject.py` וגם את רשומת `/about/` ב-`overrides.json`.

## קישורים

- **יוצאים:**
  - `@erezzielinskirozen` → Instagram.
  - `@yasalamfashionblog` → Instagram.
  - הצ'יפ "exhibitions curator" (`a.p-role`, בריחוף מתהפך לשחור) → `../curators/korin-avraham/`. לעומתו "international art department manager" ו-"the gallery manager" הם `span` ולא קישורים.
  - האימייל של נטלי → `mailto:`.
  - העמוד לא מזכיר אומנים, ולכן אין בו קישורי `artist-link`.
- **נכנסים** (לא לשבור את הנתיב `about/`):
  - nav "about" ב-`components/site-chrome.js`.
  - בהומפייג': תמונת ההירו (`.hero-image-link`) והכפתור `.hero-more` "read more" (מובייל בלבד).
  - `NAME_LINKS` ב-`artists/shira-turbowicz/` וב-`artists/melani-hekimoglu/`, ו-`linkNames()` ב-5 עמודי `works/melani-hekimoglu-*`: "ארז זילינסקי רוזן" → `about/`.
  - `sponsors/sumii/index.html`: שני `a.artist-link` סטטיים על "ארז זילינסקי רוזן" (בגוף של sumii וב-lede של מלאני) → `../../about/`.
  - `404.html`: קישור `/about/` ברשימת ה-useful links. וגם הרשומה ב-`sitemap.xml`.
- הכלל: שם המייסד מקשר ל-`/about/`, לא ל-`/artists/`. ⚠️ הנתיב המיושן `pages/about.html` עדיין כתוב ב-`docs/artist-linking.md` (שורות 84, 129) וב-`docs/components.md` §4.6 (טבלת השילובים של `.tri`). הנתיב הנכון הוא `about/` (הקובץ `about/index.html`).

## בעיות פתוחות

- **הביו של קורין** (`docs/todo.md`): פסקאות 4–5 הן טקסט אוצרותי מתערוכת loneliness ("…סקלה של בדידות"). הוא הועתק verbatim מהפריימים. **לא לשנות** עד שהמעצבת תכריע.
- **Zigel / siegel** (`docs/todo.md`): הכותרת "zigel" והאימייל `…siegel8@…` נשמרו verbatim. ⚠️ רשומת ה-todo מזכירה רק את `galleries.json` ואת דפי הגלריה, **לא את `/about/`**. אחרי הכרעה צריך לעדכן גם את העמוד הזה ביד: השם וה-`mailto`, ואת שם קובץ הפורטרט `images/about/people/natalie-zigel.*` **רק אם הוחלט לשנות גם שמות קבצים**.
- **רוחב הדוטים בקרוסלה** (נמדד 2026-09-27; **לא רשום ב-`docs/todo.md`**):
  - המטרה היא פסים של 32×2. בפועל הם מרונדרים ברוחב של כ-21.7px, ב-1440 וגם ב-1024.
  - הסיבה: ברירת המחדל של הקומפוננטה `.tri-dots{max-width:200px}` דוחסת 7×32 + 6×8 = 272px לתוך 200.
  - התיקון (לא בוצע): `.about-tri .tri-dots{max-width:none}` **בלבד**. את `--tri-dot-w` משאירים על ברירת המחדל 32px (ה-24px של הקומפוננטה חל רק ב-≤768, שם העמוד ממילא מסתיר את הדוטים). **לא** להעתיק את `--tri-dot-w:24px` מ-`events/noemi-safir`: שם יש 19 דוטים, וכאן המטרה 32×2.

## Removed / do not restore

- **פס הציטוט האפור** הוסר ברה-דיזיין 2026-09-01. לא להחזיר.
- **החתימה האנכית** הוסרה יחד עם ה-JS שלה. לא להחזיר.
- **הפריימים הישנים** `Zn3N...::1213:2970` / `1213:2888` הם legacy. לא לבנות מהם.
