# lessons.md — Policies, Recurring Lessons, Recent

> **קרא את הקובץ הזה כש:** אתה מתחיל דף חדש (לבדוק אם יש לקח קרוב לתוכן שאתה בונה), נתקלת ב-Figma quirk, מקבל החלטה Static-vs-Dynamic, או רוצה לתעד לקח חדש. **בסיום משימה — תוסיף לקח ל-§3 רק אם הוא לא חלק מ-§2 (אם קיים — תחזק את הקיים).**

---

## 1. Static-vs-Dynamic Policy

ה-Figma הוא snapshot סטטי. **האתר לא.** לכל section, החלט:

**אינטראקטיבי (אסור לשלוח כתמונה שטוחה):**
- grids של artworks → **lightbox** (components.md §1).
- thumbnails מרובים לתערוכה → **carousel/lightbox**.
- שורות אופקיות (Instagram, archive, artists strip) → **scroll-snap horizontal**. גם בדסקטופ אם items > רוחב.
- גלריות עם `coming soon` → overlay כהה non-clickable; הפתוחה clickable.
- Newsletter form → `event.preventDefault()` עד backend.
- Nav במובייל → hamburger drawer (`.nav-links` כ-fixed inset:0 + `transform:translateX(100%)` → 0).

**Micro-interactions (תמיד הוסף):**
- Card images: `transform:scale(1.04)` ב-hover, `transition:.6-.8s`.
- Links: opacity .6-.7 ב-hover.
- Outline buttons: invert ב-hover.

**סטטי (אל תזייף אינטראקטיביות):**
- Hero, taglines, copyright — לא animations.
- Section headers — לא marquee/scroll animations.
- Overlays/gradients דקורטיביים — לא clickable.

**Rule of thumb:** Figma מציג תמונה curated אחת במקום שבאתר יהיו many → צריך אינטראקציה.

**Implementation default:** vanilla JS, inline `<script>` בסוף body, ללא תלויות. הדוגמה הקנונית: `components/artwork-lightbox.js`.

---

## 2. Recurring Lessons (מאוחד — אם נתקלת בלקח קיים, חזק אותו; אל תכפיל)

### 2.1 Figma quirks

- **שמות nodes משקרים על device.** `the art works-phone` היה 1440, `artist1-13` הם 390. תמיד `absoluteBoundingBox.width`. 1440=desktop, 390=mobile.
- **שני קבצי Figma עם תוכן מראה.** `XhGH...::119:3` ≡ `Zn3N...::1213:3` (artist-alon). תאמת `fileKey` מה-URL.
- **JSON ענק → subagents חובה.** קריאה ישירה של frames גדולים נכשלת על token budget. דפי-יחיד קטנים (about) נכנסים ישירות.
- **`depth:1-2`** לסקירת canvas — מספיק בלי להציף קונטקסט.
- **`{ts1}/{ts2}/{ts3}/{ts4}` markers** = textCase metadata. רנדר כ-`<span class="lat">` (Copperplate Light), אלא אם זה לינק אמיתי → `<a>` עם `var(--link)`.
- **טעויות עיצוב ב-Figma** (כותרת loneliness בתוך how-many; caption של אומן אחד על תמונה של אחר; 4 imageRefs בערימה כאשר רק אחד רלוונטי) — **שיקול דעת**, בחר את המתאים לתמונה/JSON, לא מעתיק טעות.
- **`gap` שלילי** = `margin-top` שלילי על הילד (overlap מכוון בהומפייג').
- **`\n`/`\L`** → `<br>`.
- **figma_node_id מקבל משמעות רק יחד עם fileKey** — frames יכולים לעבור בין קבצים. אמת מה-URL.
- **שכבות מוסתרות מזהמות את ה-MCP data (06-10):** `get_figma_data` מחזיר text layers עם `visible:false` בלי לציין. כך "60x80 ס״מ\nשמן על קנבס" (leftover מכרטיס ג׳סיקה טברובסקי) נשאב ל-27 כרטיסי `works.json`, וכותרת "התנערות" זלגה ל-holy-kadosh-3. **טקסט מה-data ≠ טקסט גלוי:** לרנדר את הכרטיס כ-PNG (nodeId בלי imageRef) ולוודא. אימות סיטונאי: ספירת "קבוצות שורות" ברצועת הטקסט (min-brightness לכל שורה, `-alpha remove`) מול מספר השורות מה-JSON; `rendered < expected` = שדה מוסתר.
- **סדר fills (08-12, 08-19, 09-27):** אינדקס 0 ב-`get_figma_data` = השכבה העליונה והנראית; צבע שבראש הרשימה (`["rgba(27,27,27,0.7)", IMAGE]`) מצויר מעל התמונה (אלפא = `(base-render)/(base-27)` על שתי רצועות; מספר זהה = scrim אמיתי). אין להסיק מ"האחרון בסטאק". בדיקה זולה: אח (למשל פריים מובייל) עם fill יחיד = ה-imageRef הראשון ברשימה; בלי כזה — לרנדר (RMSE 0.9–1.1% לנראית מול 28–49% למוסתרות). שכבה חבויה שהיא תוכן אמיתי — לשאול. על scrim ו-`%[fx:mean]` — ראה 2026-08-06.
- **node-id אינו מצביע יציב:** frames עוברים בין קבצים (05-11) והמעצבת משכתבת in-place (08-18) — לאמת שם פריים ותוכן לפני עבודה על node ממופה.

### 2.2 Image handling

- **stacked imageRefs ב-fill** — רוב artist/hero images כוללים 2-4 imageRefs (אמיתית + Figma placeholders כמו `cb002e02e2090...`, `41074587...`, או hero של דף אחר). **בחר לפי סמנטיקה, לא לפי "אחרון בסטאק".** הורד רק את הרלוונטי.
- **`cropTransform` לא חובה** — `object-fit:cover` ב-CSS פותר. הוסף רק אם תוצאה ויזואלית שונה דרסטית.
- **בדוק קיום + hash compare לפני הנחת reuse.** ב-about, 7/7 התמונות היו חדשות למרות שצפיתי ל-hero משותף.
- **`portrait.png` קיים → אל תדרוס.** שמור figma version כ-`portrait-v2.png` ועדכן ב-`artists.json`.
- **נתיבי קבצים בעברית** (`url("פונטים/...")`) עובדים בדפדפנים מודרניים בלי URL-encoding.

### 2.3 Page architecture

- **Dynamic template + thin shells** לסטים גדולים. דפוס: `pages/<type>.html` קורא `?slug=`/`?id=` מ-URL + fetches JSON. shells per-slug `location.replace()`. דוגמאות: `pages/exhibition.html`, `pages/artists/artist.html`, `pages/opencall.html`. **כניסה חדשה = JSON entry, אין שינוי קוד.**
- **שדות אופציונליים ב-JSON** מאפשרים variant per slug בלי קוד-מותנה (`opencalls.json::emotional_triggers`, `gallery_images`). הרנדרר בודק קיום ומדלג בשקט.
- **fetch + inline JSON fallback.** ב-`file://` חלק מהדפדפנים חוסמים `fetch`. הטמע `<script type="application/json" id="fallback-...">`. **כשמעדכנים JSON — חייבים לעדכן גם fallback** עד שתהיה build infra.
- **Shared shell pattern** (nav+drawer+footer+JS): מועתק 1:1 בין דפים. אין partial loader. שינוי גלובלי = search-replace. **מעל 8 דפים — לעבור ל-partial loader.**
- **Hamburger drawer:** `.nav-links` הקיים *הוא* ה-drawer. אל תשכפל את הרשימה. `body.menu-open{overflow:hidden}`, `visibility:hidden` על drawer סגור (focus trap).
- **Logo → home בכל דף** עם `aria-label="home"`.
- **תוכן long-form (כתבות 5000+ מילים) נשאר ב-HTML**, רק meta ב-JSON. CMS עתידי יעביר.
- **דסקטופ + מובייל עם תוכן שונה → באתר חי, אחד.** Figma snapshot. הצג את כל התוכן בכל ה-viewports באופן רספונסיבי.
- **`exhibitions` ב-nav** מצביע ל-`pages/exhibition.html?id=loneliness`. כשייבנה `/exhibitions` index — search-replace בכל הדפים.

### 2.4 Lightbox

- **Event delegation** על `document.click` → תוכן מוזרק דינמית "תופס" בלי handlers. אחרי `innerHTML=...` קרא `ArtworkLightbox.refreshFocusable()` רק לנגישות-מקלדת.
- **font-stack של `.alb` הוא Copperplate בלבד** — עברית ב-caption נופלת ל-fallback מערכת. הוסף FbEzmel ב-`artwork-lightbox.css` אם נדרש.

### 2.5 Hebrew / data

- **שמות עבריים ב-Figma הם source of truth** ל-`name_he`. תמיד תמשוך, אל תשאיר null.
- **אומנים חדשים שמתגלים** בעת בנייה — עדכן `artists.json`, אל תתעלם.

---

## 3. New Lessons (template)

הוסף **רק** אם הוא לא חלק מ-§2. הפורמט: `**<topic>:** <one-line lesson>.` אם קיים — תחזק את ה-§2 הקיים.

---

## 4. Recent Lessons (timestamped)

> קצר: כלל + למה, בלי סיפור (היסטוריה = `git log`). לקח שהפך לכלל של משפחת דפים — עבר ל-route doc שלה.

- **2026-10-06 — לינקי-עוגן (`/#…`) נחתו 200–280px אחרי היעד:** `site-chrome.css` מוזרק ב-JS, ולכן בזמן קפיצת ה-fragment ה-`<site-header>` הוא ~290px של לינקים לא מעוצבים ואז מתכווץ ל-53. מקומית ה-CSS בזיכרון והבאג לא נראה. תיקון: `settleHashTarget()` ב-`reveal()` (`site-chrome.js`) מיישר מחדש ל-`location.hash` אלא אם המבקר כבר גלל (`wheel`/`touchmove`/`keydown`). **לבדוק עוגנים רק בכרום עם פרופיל נקי ורשת מואטת** (CDP `Network.emulateNetworkConditions`), לא ב-Browser pane (מוסתר ⇒ `scroll-behavior:smooth` לא מתקדם). טריגר 50% של פופאפ הניוזלטר נספר רק אחרי גלילת מבקר.
- **2026-09-27 — `python3 -m http.server` מאפס חיבורים כשדף טוען עשרות תמונות (`ERR_CONNECTION_RESET`):** תמונות חסרות/שבורות בלי פגם בדף. לא לאבחן "תמונה חסרה": לבדוק `complete && naturalWidth` אחרי המתנה, או לצלם בכרום חסר-ממשק עם `page.setRequestInterception` מהדיסק. webp ב-`requestfailed` אחרי ש-`picture-upgrade.js` עבר ל-avif = ביטולים צפויים.
- **2026-09-27 — רצועת צילומים שהועתקה בין פריימים — לזהות לפי ה-imageRefs הנראים ברינדור, לא לפי כל ה-fills:** ב-bar-cohen (`1873:206`/`1873:212`) כל ה-imageRefs הראשונים זהים לרצועת ג׳סיקה (`1873:132`/`1873:170`) = copy-paste; כשהגיעו הצילומים הוצבו **מעל** ה-fills המועתקים (שכבות מוסתרות). לרנדר את ה-node ולהשוות שכבה נראית מול פריימים-אחים; התאמה מלאה = לעצור ולשאול.
- **2026-09-27 — סט צילומים שנמסר ≠ סט לפרסום:** מ-13 ה-nodes של maria-artamonova הושמטו פריים וידאו מטושטש + 4 קולאז׳י 2×2 של וואטסאפ (8 פורסמו). לסרוק כל node לפני אפייה (גודל, חדות, רשת-קולאז׳) ולתעד מה הושמט ולמה. JPEG של טלפון/וואטסאפ נדחס גרוע: master 900×1600 = 393KB מול ~80KB לצילום DSLR.
- **2026-09-27 — band שעוקב בדיוק אחרי רוחב העמודה לא משאיר מרווח:** ב-nir-giorgio-levin-medina השיפוע `7.5vw-48px` השאיר 4px ב-1320. למדוד את רוחב השורה המרונדרת (Range rect מול `clientWidth` של ה-h1), לא רק מספר שורות; לשפוע תלול כך שבקצה התחתון נשארים ~15–20px ובקצה העליון הוא נוחת על הבסיס `calc(8.75vw - 66px)`.
- **2026-09-27 — `tools/seo/og-dims.json` ממופתח לפי תמונת המקור:** דף שה-OG שלו נאפה מתמונה שכבר ממופה (sumii-opening ממחזר `images/sponsors/sumii/hero.webp` ⇒ `og/sponsors-sumii-hero.jpg`) לא יכול לקבל רשומה משלו, ו-`inject.py` יחליף לו את ה-og:image.
- **2026-09-27 — סוכני QA מקבילים חולקים scratchpad:** סוכן דרס את `scratchpad/qa/page-*.png` של אחר וההשוואה רצה מול maria במקום jessica. תת-תיקייה לכל slug (`scratchpad/qa-<slug>/`); בעוטף iframe לחפש frame לפי `/events/<slug>/` ולא `<slug>`.
- **2026-09-27 — טכני:** (1) RMSE של תמונה מנוקדת (dithered) מול רינדור node הוא ~8% גם כשנכונה — להשוות אחרי טשטוש σ4 בשני הצדדים. (2) ב-zsh `$VAR` לא-מצוטט עם `-resize x1600` לא מתפצל ו-`magick` דוחה — `bash -c` עם מערך (`R=(-resize x1600); magick "$f" "${R[@]}" …`). (3) כרטיס רשימה בפיגמה הוא לרוב STRETCH עם cropTransform לא-אחיד (niki: 0.82×0.72) — לחשב את שני יחסי הסקייל; אם שונים, לאפות קרופ cover מהמקור ולא את רינדור ה-node.
- **2026-09-27 — סקריפט fit "שורה אחת" + `overflow:hidden` = טקסט שנקטע בשקט; עמודת טקסט בלי `min-width:0` דוחפת את התמונה:** (1) the-peeler: "letter from the exhibition curator" כווץ לרצפה 20px ועדיין נחתך ב-1101–1280 ("…EXHIBITIO") — לסקריפט fit חייב fallback לשורות (`.is-wrapped`), ולעולם לא `overflow:hidden` על טקסט. (2) ktuba, loneliness, `opencalls/*`, רצועת tribe: עמודת `flex:1` בלי `min-width:0` + מילה ארוכה ב-Copperplate (PERFORMANCE, אימייל, תאריך `nowrap`) או כרטיס קבוע 492px דחפו את התמונה מחוץ ל-769–1180 — `min-width:0` + רמפת גודל **בטווח השבור בלבד** (`@media (min-width:769px) and (max-width:1100px)`, `min()` כך ש-1440 לא זז), מחושבת מיחס רוחב/גודל של המילה (נמדד). כלי: `tools/qa/sweep.mjs`, ואז `tools/regress` ב-390/1440 = 0 הבדלים; חיתוך דיו של גליפים נראה רק בצילום.
- **2026-09-01 — דף-כיול פונטים חייב `document.fonts.load` מפורש לכל משקל לפני מדידה (`/about/`):** `document.fonts.ready` התממש לפני ש-Copperplate 400 נטען (lazy), והכיול החזיר מטריקות Light — 70px במקום 60 (+14%). מתכון: `Promise.all([document.fonts.load('300 100px F'), ('400 …'), ('700 …')])` ורק אז למדוד, ולוודא שהעמוד האמיתי מתכנס לאותם מספרים (ink של צילום העמוד `-fuzz 20% -trim` מול ה-target מרינדור הפריים). קצב-השורות של FbEzmel בפריימים ~**1.06** (17px@16 / 19px@18 / 24px@22) ולא ה-normal של הדפדפן (~1.45) — למדוד pitch מהרינדור (פרופיל שורות כהות), אחרת בלוקי עברית יוצאים גבוהים ב-30%.
- **2026-08-28 — 🔴 חיתוך caps של Copperplate: יש נוסחה (`.h-title` במשפחת artist-talk):** Canvas TextMetrics: `actualBoundingBoxAscent/fontSize` = **0.6983** (קבוע בכל הגדלים) מול `fontBoundingBoxAscent/fontSize` ≈ **0.578** ⇒ ה-ink חורג **0.12em מעל ה-content-box**; `line-height < font-size` מוסיף half-leading שלילי `(fs−lh)/2`. **`padding-top ≥ 0.12em + (fs−lh)/2/fs`** — ב-64/58 `0.167em`, ולכן `.14em` חתך 1.73px (ב-44/42 — 0.56px; ב-56/50 — 2.26px). תוקן ל-`.2em` ב-19 עמודי אירוע (>1px clearance בגדלי המשפחה 64/60/56/55/53/44/34). לא overflow אלא גבול ה-paint של האלמנט (מחזק 2026-06-16 ב׳, שם `.15em` בניחוש לא הספיק). לאמת עם `measureText` (headless לא משחזר את החיתוך, המדידה מדויקת). **שורש נוסף בפונט (2026-09-27):** ב-`פונטים/Copperplate.woff2` (Regular 400) `head.yMax`/CFF FontBBox = **.432em** מול caps של .667em (Light .921, Bold 1.043 תקינים); כששורת כותרת נוחתת מתחת לגבול טייל-רסטר של 256px הראשים נחתכים גם עם ה-padding (maria-artamonova ב-1440, y≈254) — מקומית `will-change:transform` על `.h-title`; האמיתי: לכתוב מחדש FontBBox/`head.yMax` ל-~.70em (`docs/todo.md`). `fullPage:true` של puppeteer **לא מראה** את החיתוך — רק crop ב-viewport (1x ו-2x).
- **2026-08-28 — `statement_he` per-work שפותח בשם היצירה:** `ws-head` (מ-`title_he`, renderer משותף `NEW_JS`) מדפיס את השם שוב ב-`livay-levi-4` (פריים `1500:1551`, הסטייטמנט צומת אחד ששורתו הראשונה "היצירה - השתקפות של חומר"). פתרון: `.work-statement .ws-head{display:none}` **ב-CSS ולא ב-JS** (שינוי `NEW_JS` מפיל את ה-`replace` האידמפוטנטי של `tools/sync_works_mirrors.py`). לקרוא את הפסקה הראשונה של כל `statement_he` חדש, ולאמת ב-`--dump-dom`.
- **2026-08-28 — סדר קבוצות בדף אומן = ה-`artist_page_pos` הנמוך ביותר בקבוצה, ויצירה משותפת כובלת שני דפים:** פריימי ליוואי (`668:11841`) והדס (`797:106`) שמים `הקולפן | interdependence` מעל הקבוצה השנייה ⇒ ל-`livay-levi-3` ה-pos הנמוך בשני הדפים (הוסטו גם `hadas-tuval-1/2` ב-+1). `pos:0` אסור (`pos||1e9`). בתיקו בין שתי קבוצות של אותה תערוכה (`הקולפן` ו-`הקולפן | interdependence`) מוקדם יותר במערך עולה — היצירה החדשה נכנסה בסוף `art_works[]` (index 149 מול 148), ולכן ה-pos חייב להיות **ייחודי** לא רק "נכון". לתכנן pos משני הדפים ולאמת את שניהם ב-`--dump-dom`.
- **2026-08-28 — לבקש את פריים דף-האומן המלא, לא רק הסקשן:** נמסר `1500:1551` (Artworks Section בודד); הסדר מול הסקשן האחר היה הפוך ונדרש תיקון. ההורה `668:11841` מראה את הסדר. לפני מימוש סקשן — לשאול מי ההורה ולמשוך גם אותו.
- **2026-08-28 — `.tri`: ה-offset של peek נגזר מה-gap של הפיגמה:** ב-`events/noemi-safir` השורה `space-between` ברוחב 1248 ⇒ 302+481+303=1086 ⇒ רווחים 81 ⇒ **`±472.5px`** ולא `±463.5` של close-look (רווח 72). תמיד `center_w/2 + gap + peek_w/2` מהפריים; מעל ~11 שקופיות `.tri-dots{max-width:200px}` מכווץ דוטים ל-~3px (`max-width:none` + `--tri-dot-w:24px`) — `docs/components.md §4.4`.
- **2026-08-28 — הסדר שהמעצבת מוסרת ≠ סדר ה-DOM כשהקומפוננטה מגדירה preview:** `.tri` מרנדרת רק שקופיות **עוקבות** כ-peek/מרכז/peek ⇒ 3 התמונות שהפריים מצייר הועלו למקומות 1-3 (`data-tri-start="1"`), שאר ה-16 בסדר שנמסר. הסיבה ב-`_photos_note` וגם בהערת HTML — אחרת סנכרון "יתקן" את הסדר.
- **2026-08-23 — כיול Copperplate: למדוד, לא להחיל גורם. `textCase:LOWER` מסביר פערים:** ב-`sponsors/sumii/` שני גורמים באותו דף — כותרות מוצר `20→17.5px` (.875) והלוקאפ של מלאני `35.64→31px` (.87), מול הירו קיים `30→23px` (.767) ו"~28% רחב" (.78). כותרות המוצר `textCase:UPPER` ⇒ caps מול caps; הלוקאפים `LOWER` — הפיגמה מרנדרת small-caps והאתר UPPERCASE גלובלי ⇒ גליפים גבוהים ⇒ font-size קטן יותר. מתכון: `magick <render> -crop <תיבת שורה> +repage -fuzz 40% -trim -format "%wx%h" info:` על הרינדור ועל הצילום, `size × (ink_figma / ink_mine)`. **חיזוק 2026-09-27 (לוקאפי SUMII):** ריצות `UPPER` נחתו על ה-px של הפיגמה verbatim (21→21 / 16→16; sumii-opening 20.75/17.33/15.5); רק `LOWER` דרשו כיול: כותרת 80→64, אוברליי 24→21, כתובת 16→14. `.lat` בתוך עברית (`ts1`, UPPER) התאים ב-**1em** ולא ב-.88em (ב-.88em "SUMII של FIGURES." יצאה קצרה ב-18px).
- **2026-08-23 — טקסט hug בפיגמה גולש מהתיבה; ב-CSS נשבר:** בלוקאפ מלאני (`1637:352`) התיבה 372px והטקסט hug ~375px ("EREZ ZIELINSKI ROZEN") ⇒ שורה שלישית, גובה 266px→311px. בלי `white-space:nowrap`. לבדוק **גובה** תיבת הדיו מול הרינדור, לא רק רוחב.
- **2026-08-23 — "התבנית מנצחת את הפריים" היא הנחה — להשוות לפריים-אח:** `artists/melani-hekimoglu/` (`1634:214`) מצייר שם מלא בשורה אחת Bold, ה-renderer מפצל `.first` Bold + `.last` Light. פריים אומנית אחרת (`hadas-tuval 797:106`) מראה "HADAS"/"TUVAL" בשתי שורות בשני משקלים ⇒ המעצבת מבדילה והסטייה אמיתית ⇒ page-local. אותו כלי להכרעת fills (`724f6d54…` = צילום קטלוגי ממותג "SHORASHIM" — leftover).
- **2026-08-23 — לפני fork של renderer משותף: מה `tools/sync_works_mirrors.py` משכתב?** הסקריפט מחזיר לאחור אזורי renderer שלמים (`OLD_GROUP_JS`→`NEW_GROUP_JS`, `OLD_JS`→`NEW_JS`) בכל `artists/*/index.html`, בשקט. `grep` ב-`tools/` אחרי המחרוזת שמשנים, והרץ מיד אחרי (0 אזהרות `anchor not found`). `exhibition_statements` הוא `===` על `exhibition_title_he` ⇒ "קבוצה בלי כותרת" = **`null` מפורש בשני הצדדים** (מפתח חסר ⇒ הסטייטמנט נעלם בשקט).
- **🔴 2026-08-23 — לפני `git checkout`/כתיבה גורפת: HEAD יכול לזוז (סשן מקביל באותה תיקייה, קומיט את הקבצים הלא-מקומיטים שלך):** (1) `git log --oneline -3` לפני כל revert/rewrite גורף; (2) עריכות ממוקדות (`str.replace`) > כתיבה-מחדש, גם בקובץ שיצרת בסשן; (3) בחפיפה — לבדוק אם הסשן השני יצר assets (כאן `melani-hekimoglu-1..5`, RMSE<1%) ולמחזר.
- **🔴 2026-08-23 / 08-20 / 07-26 — `tools/seo/inject.py` ו-`og_gen.py` גורפים = רגרסיה (3 פעמים: 93, ~90, 74 דפים):** inject מייצר תיאור ברירת-מחדל מהדאטה לכל דף בלי רשומה ב-`tools/seo/overrides.json` (כפילויות מקטיעה, `og:image` יורד ל-webp, `og:image:alt` מוחלף); `og-dims.json` בריפו חלקי (160 מול 209 JPG); `breadcrumb()` לא מסנן אינדקסים שלא נבנו; `og_gen.py` תלוי ב-`/tmp/seo_inject.py`. שחזור: `git status --porcelain` → keep → `tr '\n' '\0' | xargs -0 git checkout --`, ואז `sync_works_mirrors.py`. **דף חדש: `refresh_sitemap_lastmod.py` בלבד + בלוק SEO ידני מדף-אח** (CLAUDE.md כלל-זהב 15, `docs/todo.md`); אם צריך inject לנתיב — להוסיף ענף ולהשלים `og-dims.json`.
- **2026-08-20 — אומן בלי תערוכה = קבוצת `exhibition_title_he` עם `exhibition_slug:null`:** שירה טורבוביץ (SUMII): `exhibition_title_he:"POP UP ART RESIDENCY"` + `exhibition_slug:null` + `exhibition_route:"sponsors/sumii"` + רשומת `exhibition_statements` — ה-renderer הקיים נותן בדיוק את מבנה הפיגמה. `exRank(null)` = ‎-1 ⇒ קבוצה כזו שוקעת מתחת לתערוכות אמיתיות. **לפני שדה/ענף חדש — לבדוק אם צירוף שדות nullable כבר מייצר את העיצוב.** קרדיט מעורב `"שירה טורבוביץ | sumii"` ב-`artist_he` נפל ל-fallback כי ה-renderers עטפו ב-`esc()` בלבד — `latHtml`/`mixedHtml` כשיש Latin.
- **2026-08-19 — שני אריחים עם אותה תמונה = פלייסהולדר, לא גלריה של שתיים:** `events/risa-and-noemi/` (`1578:5349` / `1578:5334`). לרנדר ולוודא שהתוכן שונה; אריח כפול נבנה **פעם אחת**. תמונה בודדת מ-2-up מובייל (152×266) עולה ל-216×378. שכבה חבויה שהיא תוכן אמיתי — לשאול.
- **2026-08-18 — גם node-id אינו מצביע יציב: המעצבת משכתבת פריימים in-place:** `XhGH…::1318:3287`/`1318:3480` (soos) שוכתבו ל-**sumii** (שם הפריים "sumii - desktop/mobile"). ה-id נשאר, הזהות התחלפה. **לפני עבודה על node ממופה — לקרוא את שם הפריים והתוכן.** שוכתב = עמוד חדש; לעמוד הישן אין מקור חי (לתעד ברשומה). קרה שוב 2026-09-27: `1471:256` (כרטיס nir-giorgio-levin-medina) שוכתב לכרטיס niki-de-saint-phalle-day.
- **2026-08-12 — "התערוכה החדשה למעלה" בדף אומן (הכרעת משתמש):** הסדר היה נכון ב-8 האומנים הרב-תערוכתיים רק כתוצר-לוואי של `artist_page_pos`. מיון לפי מיקום התערוכה ב-`exhibitions.json` (עולה ⇒ מיון יורד), מירור `__EX_ORDER_INLINE__` (`ex-order.js`). **כלל שכבר "עובד" — לוודא שהוא נאכף** ולבדוק עם דאטה מכוון-הפוך. שוויון-דירוג = stable sort (הקולפן + "הקולפן | interdependence" בסדר הפיגמה).
- **2026-08-12 — יצירה משותפת: מחבר `×` ולא `x`, ורשומה אחת מנצחת שכפול:** `livay-levi-3` ("interdependence", ליוואי לוי × הדס טובל): ל-FbEzmel אין גליף `x` (U+0078) אך יש `×` (U+00D7); הרנדררים עוטפים את המחבר ב-`escapeHtml` ולא `mixedHtml`. תקדים `zohar ron × dandan nusha`. רשומה אחת עם `artist_pages`+`collab`+קבוצה ייעודית (`exhibition_title_he` משלה) + `exhibition_statements` לכל אומן — הקיבוץ הוא לפי `exhibition_title_he` מדויק; שכפול = אותה תמונה פעמיים ב-`/works/`.
- **2026-08-06 — scrim מול רינדור Figma: `%[fx:mean]` מכליל את ערוץ האלפא ומהפך את המסקנה:** ב-`events/zohar-ron-medina/` hero עם `rgba(27,27,27,.4)` + תמונה; בהירות 0.679 מול 0.517 נראתה "אין scrim" — אבל רינדורי Figma הם PNG עם אלפא ו-`(0.358+1)/2 = 0.679`. אחרי `-background white -alpha remove -alpha off`: 0.3577 מול 0.3523 (scrim כן מוחל; RMSE 5.9% = הטקסט הלבן). **לפני כל השוואת בהירות/RMSE מול רינדור Figma — `-alpha remove -alpha off` בשני הצדדים.** imageRef בפרופיל Adobe98: המרה ל-sRGB משנה ממוצע ב-0.4% בלבד.
- **2026-07-26 — Audit לינקים/מירורים/קונסול + שני באגים:** (1) חשיפת עמוד מ-`_staging` חייבת לעדכן גם `canonical`/`og:url`/JSON-LD (tali-zelnik נחשפו אך הצביעו על `art.zrp.co.il/_staging/...`). (2) `sitemap.xml` פיגר ב-37 דפים — דף חדש/חשיפה = sitemap באותו קומיט, ו-grep `_staging` אחרי כל mv (כלל-זהב 15). `13tv.co.il` מחזיר 403 ל-curl (הגנת בוטים) — הלינק תקין בדפדפן.
- **2026-07-15 — סדר עבודות בדף אומן (amnon, Figma `798:173`):** גריד הפיגמה LTR (`gridColumn` 1 = שמאל), `.works-grid` באתר `direction:rtl` ⇒ **הרצף** (קריאת LTR) הוא הקנוני ל-`artist_page_pos`, השורות ממוררות פר-שורה; פריט בודד בשורה אחרונה נופל ימינה (המעצבת מיקמה ב-`gridColumn:2`). אימות סדר = צילום headless ברוחב 1440; ב-390 ה-headless לא מפעיל אמולציית מובייל (ארטיפקט).
- **2026-07-15 — טקסט מעגלי (TEXT_PATH) ו-`textLength` בכרום (`#big-news`, טבעת "BIG"×6 סביב "news"):** `textLength`+`lengthAdjust` על `<text>` עם `<textPath>` לא נאכף בכרום. פתרון: `<textPath>` נפרד לכל מילה עם `startOffset` שווה (0/16.666/33.333/50/66.666/83.333%) על אותו `<path>`. כיול: "news" 55.7px בפיגמה ⇒ 56px אצלנו (171px מרונדר); טבעת 45.9px ⇒ 36px על רדיוס 101 (viewBox 248).
- **2026-07-15 — שני לינקים מהמשתמש ≠ בהכרח אותו סקשן:** נמסרו `1124:240` (מובייל של **news**) ו-`1124:1030` (דסקטופ של **perfume promo**, כבר בנוי). בני-הזוג אותרו ב-`depth:2` על ההורים (`homepage-desktop 1124:754` / `homepage-mobile 1124:21`) + רינדור. לפני בנייה — לרנדר את שני ה-nodes, ואם לא אותו סקשן לחפש בני-זוג בהורה ולבדוק אם הסקשן כבר קיים.
- **2026-07-09 — Audit רוחבי (48 ממצאים, 35 תוקנו ב-`b18bacc`) — שלושה דפוסי-באג:** (1) החלפת `src` על `<img>` עם `srcset` לא עושה כלום (וגם `picture-upgrade.js` מדלג על imgs עם srcset) — `removeAttribute('srcset')`+`('sizes')` **לפני** שינוי `src` (קרה בפרומו הבשמים). (2) שכפול עמוד-תבנית בלי לעדכן את כל ה-head (`works/elsa-ars-brush-6` נשא SEO של talia-zoref-1; `press/time-out` נשא JSON-LD/og של the-last-station) — לעבור על title, description, canonical, og:*, twitter:*, JSON-LD. (3) JS "נראה-תקין" שמת בשקט: `el.tabIndex = el.tabIndex || 0` לעולם לא מציב 0 (ברירת מחדל -1 truthy); `!img.loading` תמיד false (לבדוק attribute). אימות ששרד: סריקה סטטית של href/src/srcset מול הדיסק + `sync_works_mirrors.py` כבדיקת drift + אימות אדברסרי לכל ממצא (6/54 נפסלו).
- **2026-06-16 (ג) — עמוד היצירה לא עטף אנגלית ב-Copperplate:** `works/<id>/` רינדר `exhibition_title_he`, `statement_he` ושם אומן לטיני דרך `esc()` בלבד ⇒ serif fallback. נוספה `latHtml()` + `.lat` (Copperplate UPPERCASE, `unicode-bidi:isolate`, `font-size:.86em`) ב-111 עמודים. **כל renderer שמוציא טקסט JSON — לעטוף runs לטיניים; `esc()` לבד = bug פונט; לבדוק את כל השדות.**
- **2026-06-16 — 🔴 `overflow-x` על `<body>` חותך גם אנכית ראשי אותיות Copperplate:** כל `overflow-x` לא-`visible` מקדם `overflow-y` ל-`auto` ⇒ body הופך scroll-container שחותך תוכן שגולש מעל תיבתו; ה-ink של שמות ה-hero (Copperplate 60–80px, `line-height:1`) גולש ~12–18% מעל ה-line-box. תיקון ב-34 דפי אומן: `html{…;overflow-x:hidden}` + `body{…;overflow-x:visible}`. ⚠️ ה-override ב-`site-chrome.css` לא מנצח inline (מוזרק לפני CSS הדף) — **לתקן במקור**. אימות: puppeteer-core `element.screenshot()` על הכותרת, או `range.getClientRects().top` מול `el.getBoundingClientRect().top`. **לעולם לא `overflow-x` (hidden/clip) על `body`/קונטיינר עם כותרות.**
- **2026-06-16 (ב) — חיתוך-מלמעלה של Copperplate ש"מסתדר ב-hover" = glitch של גבולות-paint:** ב-`.ex-heading` בדפי אומן (`How Many Partners Have You Had? | sex?`) ראשי ה-`<span class="lat">` נחתכו בפיינט הראשון בלבד (ריחוף מאלץ repaint); התו `|` ב-FbEzmel לא נחתך. ה-ink נוגע בקצה העליון של תיבת ה-paint (ink-top == box-top). לא משוחזר ב-headless. תיקון: `.ex-heading{padding-top:.15em}` ב-31 דפים (לגדלים צפופים — הנוסחה ב-2026-08-28). אם נשאר: `line-height` גבוה או `transform:translateZ(0)` (סיכון טשטוש).
- **2026-06-15 — 🔴 Sticky header נשבר מ-`overflow-x` על `<body>`:** כל overflow לא-`visible` על הורה של sticky הופך אותו ל-scroll-container, וה-sticky נצמד ל-body ולא לחלון. **`clip` שובר כמו `hidden`.** חיתוך אופקי **רק על `<html>`**, `body{overflow-x:visible}`; תיקון יחיד ב-`site-chrome.css` (מוזרק אחרי CSS הדף) תיקן ~50 דפים. אומת ב-Chrome CDP עם גלילת wheel (header.top נשאר 0, דסקטופ ומובייל).
- **2026-06-10 — דפי אומן קולפן (`XhGH...::560:3384`, 14 frames מובייל):** (1) 🔴 שמות בפריימים משקרים גם ברמת התוכן — frame livay-levi נשא Profile Text "lahav barak"; לזהות לפי ביו ויצירות. (2) פסקאות leftover בין פריימים (בביו chen-ziv 2 פסקאות של ג'סיקה טברובסקי "הציור התנערות...") — לסנן מול frames אחרים. (3) רוב היצירות כבר ב-`art_works[]` — להשוות frame↔JSON לפי כותרות (פער ניר 9↔2; "הסרף"→"השרף" אצל אלסה). (4) יצירה חדשה — להזריק צמוד ליצירות הקיימות. (5) ב-dump של MCP `\_` הוא גם underscore (האנדלים) וגם nbsp (פרוזה). (6) סדר יצירות בדף אומן ≠ עמוד works (5 אומנים שונים, ירדן אמיר כמעט הפוך) ⇒ `artist_page_pos` + מיון בדפי האומן בלבד; לא לסדר מחדש את המערך.
- **2026-06-10 — Artists index (`/artists/`, `523:107`/`523:2`):** שמות אומנים UPPERCASE למרות `textCase:LOWER` בפיגמה (כלל-זהב 3). אומן חדש בעיצוב ללא רשומה ⇒ placeholder (`!bio_he && works.length===0`), רשום ב-`_pending_artist_pages`. תמונות גריד ריבועיות `-resize 810x810^ -gravity center -extent 810x810` (+480w).
- **2026-06-10 — אימות סדר תמונות ברמת הפיקסלים:** בגריד works התאמת artist+title עברה 1:1 אך המעצב סידר מחדש תמונות בין כרטיסים חסרי-כותרת (tal-nehoray, gal-polk, adi-duak, la-raz-porta). שיטה: perceptual hash (24×24 grayscale, RMSE) לכל מיקום מול הקבצים המקומיים + cross-match חריגים; קבצים שעברו מסגור-מחדש (adi-duak) מנפחים RMSE ⇒ montage. כפילויות תמונה בפיגמה עצמו (אותו imageRef על כרטיסי אמנים שונים) = טעויות מעצב — לדווח.
- **2026-06-10 — טעינה מדורגת לגרידים גדולים (works):** צ'אנק ראשון 12, אחר כך 18 דרך IntersectionObserver על sentinel (`rootMargin:1800px`). ⚠️ חובה re-arm (`unobserve`+`observe`) אחרי כל צ'אנק, אחרת נתקע; אחריו `ArtworkLightbox.refreshFocusable()`; fallback בלי IO = רינדור מלא.
- **2026-06-11 — works: דסקטופ ומובייל בסדר גריד שונה:** מובייל (`542:1390` בתוך `542:1365`) שונה מדסקטופ (`542:500`) ב-63 מתוך 109 מיקומים ⇒ **הדסקטופ קנוני**; "סדר 1:1 מול פיגמה" — לציין מול איזה frame.
- **2026-06-11 — סיווג שדות כרטיס לפי textStyle ו-node-id binding:** `textStyle` לכל node (סגנונות אמן, כותרת, פרטים, "נמכר", גלריה) = שיוך שדות דטרמיניסטי; ה-IDs של הסגנונות משתנים בין fetches — לזהות מחדש לפי דוגמאות. בעדכון גריד לממפות כרטיס→רשומה לפי node-id (עדכון 102→109 ירד ל-11 שינויים) — **בכפוף ללקח 2026-08-18** (ה-id יכול להישאר כשהזהות התחלפה: לאמת שם/תוכן).
- **2026-06-02 — Perf pass (srcset ל-109 תמונות כבדות; events/how-many 12.5MB→2.6MB):** (1) `embed-iframe.js` חייב `defer`. (2) LCP עם `loading="lazy"` = אנטי-פאטרן: רק הראשון `fetchpriority="high"`. (3) 🔴 אסור `media="print"` async-CSS על קומפוננטה שנוגעת ב-DOM סטטי (`artwork-lightbox.css` — `[data-artwork-src]{cursor:zoom-in}`); stacked/triptych/gallery.css נשארים blocking. (4) 🔴 Lighthouse על iCloud Drive = רעש (LCP 8.9s→11.9s→33.1s) — להשוות back-to-back, לסמוך על הציון. (5) תמונות שמרונדרות ב-JS לא קיבלו srcset (דורש סכמת JSON). תוצאות: events/how-many -79%, homepage -55%, about -43%.
- **2026-05-11 — Mobile horizontal-scroll מ-titles גדולים:** `.ex-now .titles .l` (91px) ו-`.exhibitions-titles .b` (58px) גרמו scroll אופקי. (1) `html{overflow-x:hidden}` בלבד (⚠️ אחרי 2026-06-15: לא על `body`). (2) `clamp(min, vw-value, max)` ל-≥48px; `vw-value` ≈ `figma_px / figma_viewport × 100`. (3) `white-space:nowrap` + `max-width:100%;overflow:hidden` על הקונטיינר. **font-size ≥48px במובייל ⇒ clamp() + בדיקת רוחב מילה מול 320px.**
- **2026-05-13 — Lang-aware font routing ל-JSON:** כותרת `״DON'T LOSE YOUR HEAD״` נפלה ל-serif fallback כי `.work .title` היה `font-family:var(--heb)` ול-FbEzmel אין Latin (אותו דבר ב-`.alb-title`/`.alb-alt`, `.bm-title`). זיהוי שפה ב-render (regex `[א-ת]`, גרשיים `״` לא נספרים) + `is-he`/`is-en`; דפוס ב-`docs/conventions.md §5.1`. `titleHtml()` מעביר `<span class="lat">` בלבד. **כל אלמנט שמרנדר ערך JSON — lang-class; לא להניח שפה.**
- **2026-08-04 — התנגשות שם מחלקה עם ה-CSS ש-site-chrome מזריק (`.logo`):** ב-`sponsors/soos/` SVG עם `class="logo"` ירש `.logo` גלובלי של ההדר (`display:flex` + כללי מובייל). ההזרקה אחרי `load` — computed styles ב-`onload` נראים תקינים. שם ייחודי `soos-logo`. לפני שם גנרי (`logo`, `nav`, `menu`, `toast`…): `grep "\.<name>[{,. ]" components/site-chrome.css components/site-boot.css`.
- **2026-08-04 — צילום מובייל 390 ב-headless chrome:** `--headless=new --window-size=390,...` לא נותן viewport 390 (מינימום ~500) ⇒ הכל "גולש מימין". פתרון: עוטף עם `<iframe width=390>` (query param), צילום העוטף ברוחב 800 + `--allow-file-access-from-files`, crop ל-390. צילום חתוך אחיד מימין = קודם לצלם דף ביקורת תקין (anat-wegier) באותם דגלים.
- **2026-07-26 — אימות תמונה בלי הורדה:** מידות המקור בסקשן Assets בפיגמה (למשל 850×1276) מול `sips -g pixelWidth` על ה-webp המקומי; התאמה מלאה = אותו קובץ. (ערוץ MCP לא מחובר ⇒ לעצור ולבקש התחברות, לא לעבור לכלי אחר — CLAUDE.md §3.)
