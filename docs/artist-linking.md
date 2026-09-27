# artist-linking.md — Artist Linking (כלל-ברזל) 🔴

> **קרא את הקובץ הזה כש:** אתה מוסיף או מרנדר תוכן שמזכיר אומן — שם, תמונה, פורטרט, פסקה ב-press article, caption, alt text, פסקת body כלשהי. **חובה לפני סיום משימה** שמגעת באומן.

---

## 0. הכלל

**כל אזכור של אומן באתר — שם, תמונה, או קלף — חייב להיות קישור לדף האומן שלו.** זה כלל-ברזל, לא suggestion. נכשל בזה = הדף לא נחשב מוכן.

חוסר קישור = בעיה ב-UX (משתמש לא מבין שהשם clickable) **וגם** ב-SEO (Google לא מקשר בין הדפים).

---

## 1. על מי חל הכלל?

על כל אומן שיש לו רשומה ב-`data/artists.json` עם `slug` — ולכן דף `artists/<slug>/index.html` (היום 44). הרשימה הקנונית = `artists.json`; לא להסתמך על רשימה מועתקת.

- **placeholder** — `_pending_artist_pages` ב-`artists.json` (היום `dan-ben-ary`, `racheli-reuven`): קישור חובה מעמוד `/artists/`; בתערוכות/טקסטים — לא לקשר עד שיש תוכן (כך racheli reuven ברצועת how-many ובטקסט של `events/how-many/`).
  - `dan-ben-ary` — הדף שלו מפנה ל-`artists/zohar-ron-dan-ben-ari/`, ולשם מקשרים את האזכורים שלו (כרטיס `/artists/` דרך `link`, רצועת how-many, `events/how-many/`).
- `gal-rotem`, `raz-ronen` — דפים מלאים (לא placeholder) ⇒ חובה לקשר.
- `shira-turbowicz` (שירה טורבוביץ / SUMII) — דף אומנית מלא ⇒ חובה לקשר, כולל בעמוד הספונסר `/sponsors/sumii/`. `SUMII`/`sumii` לבדו = שם מותג, לא אזכור אומן.

---

## 2. איפה חובה לקשר

| מקום | מה לקשר | איך |
|---|---|---|
| גריד `/artists/` (`artists/index.html`) | הכרטיס כולו (תמונה + שם) | `<a class="artist" href="../artists/<slug>/">` — מרונדר מ-`#artists-grid-data`; `link` בכרטיס = slug של דף אחר |
| גריד `/works/` (`works/index.html`) | שם האומן | `<a class="artist" href="../artists/<slug>/">`; ביצירה משותפת (`collab[]`) — כל שם בנפרד. התמונה → עמוד היצירה `<id>/`, לא דף האומן (§4) |
| "our artists" בהומפייג' (`.artists-list` תחת `#exhibitions-now`) | פורטרט + שם | `<a class="artist" href="artists/<slug>/">` סביב הקלף השלם |
| קרוסלת `#x-our-artists` בהומפייג' | השקופית + הכיתוב | `data-artist-href` + `data-caption-href` = `artists/<slug>/` על `<img class="tri-slide">` (`components/triptych-gallery.js` מנווט) |
| Artist strip בדף תערוכה | תמונה + שם | קלף `<a class="card is-linked">` (slug ב-JSON או `_ARTIST_SLUGS` map) |
| רצועת אומנים בדף אירוע | תמונה + שם | `<a class="artist-card" href="../../artists/<slug>/">` סביב התמונה והשם |
| תמונה בכתבה (press) — **פורטרט / צילום אדם** (התמונה עצמה היא האומן) | התמונה | `<a class="artist-img-link" href="../../artists/<slug>/">` סביב `<img>` בלבד (לא `<figure>`) |
| תמונה בכתבה (press) — **יצירה, מיצב, תיעוד תערוכה, גלריה** | אין קישור על התמונה | `<img>` ישירות ב־`<div class="img …">`. הקישור לדף האומן נשאר ב־`<figcaption>` (`artist-link`) ובטקסט הגוף — לא מנווטים מקליק על היצירה לדף האומן |
| `<figcaption>` שמזכיר אומן | השם בלבד | `<a class="artist-link" href="../../artists/<slug>/">` סביב המופע הראשון |
| פסקת body (`<p>...האומנת X...`) | כל מופע של שם | `<a class="artist-link">` |
| `<aside>`, `pull-quote`, `caption` | אותו דבר | `<a class="artist-link">` |
| Lightbox כותרת | טקסט שמכיל שם אומן | קשר את השם |

---

## 3. CSS להעתקה

אין stylesheet משותף: הבלוק מועתק לכל דף שמשתמש ב-`a.artist-link` (כתבות, דפי אירוע, `sponsors/`, `opencalls/`, ומעט דפי אומן/יצירה). `a.artist-img-link` — היום רק ב-`press/walla/`. (בעתיד להעביר ל-`components/site-chrome.css`.)

```css
a.artist-link{
  color:inherit;text-decoration:underline;
  text-decoration-color:rgba(27,27,27,.25);
  text-underline-offset:3px;
  transition:text-decoration-color .2s,opacity .2s;
}
a.artist-link:hover{text-decoration-color:currentColor;opacity:.75}
a.artist-img-link{display:block;color:inherit;text-decoration:none}
a.artist-img-link img{transition:filter .25s}
a.artist-img-link:hover img{filter:brightness(.96)}
```

---

## 4. למה לא lightbox? ומתי קליק על תמונה → דף אומן?

ב-`/works/` קליק על התמונה → עמוד היצירה `works/<id>/` (לא lightbox ולא דף האומן); הקישור לדף האומן = השם בכרטיס, ושוב בעמוד היצירה. ה-lightbox חי בעמוד היצירה (קליק על התמונה) ובכרטיסי היצירות שבדפי האומן (`artists/<slug>/`).

**בכתבי press:** קליק על **תמונת פורטרט / אדם** עשוי לעטוף ב־`artist-img-link` לדף האומן. תמונת **יצירה או תיעוד תערוכה** — בלי anchor על ה־`<img>` (הקישור בכיתוב או בגוף הטקסט מספיק; קליק על היצירה לא אמור לפתוח דף אומן).

---

## 5. נתיבים יחסיים (לדף `alon`)

תמיד יחסי ועם `/` בסוף — בלי `.html`, בלי `index.html`, בלי `/artists/…` מוחלט: `'../'` × עומק הדף + `artists/alon/`.

| מאיפה | href |
|---|---|
| `index.html` (root) | `artists/alon/` |
| עומק 1 — `works/index.html`, `artists/index.html`, `about/index.html`, `press/index.html`, `events/index.html` | `../artists/alon/` |
| עומק 2 — `press/<slug>/`, `events/<slug>/`, `exhibitions/<slug>/`, `works/<id>/`, `galleries/<slug>/`, `sponsors/<slug>/`, `curators/<slug>/` | `../../artists/alon/` |
| בתוך `artists/<slug>/` (לאומן אחר) | `../../artists/alon/` (כך כל ה-hrefs בקוד; `../alon/` שקול) |

href שנבנה ב-JS נפתר מול כתובת **הדף**, ולכן כל רנדרר מקודד את העומק של הדף שלו: `'../artists/'+slug+'/'` ב-`works/index.html` וב-`artists/index.html`; `'../../artists/'+slug+'/'` ב-`works/<id>/`, `galleries/<slug>/`, `exhibitions/how-many/`, `artists/<slug>/`. העתקת רנדרר לדף בעומק אחר ⇒ לתקן את הקידומת.

---

## 6. רנדור דינמי מ-JSON

אם דף מרנדר תוכן אומנים מ-JSON (כמו רצועת האומנים ב-`exhibitions/how-many/` וב-`exhibitions/loneliness/`, מ-`data/exhibitions.json`):

1. **הוסף `slug` לכל אומן ב-JSON.** רנדור ללא slug → name→slug lookup שביר, שוכח אומנים. (`artist_page_slug` = קישור לדף של אומן אחר — לשיתופי פעולה.)
2. **בקוד הרנדור:** אם יש slug → `<a href="../../artists/${slug}/">` (הקידומת לפי עומק הדף — §5). אם null → `<div>` רגיל. אסור לקשר ל-slug שאין לו `artists/<slug>/index.html` (404).
3. **דוגמה:** `exhibitions/how-many/` — `a.slug || _ARTIST_SLUGS[name_en]`, `artist_page_slug`, `linkable ? 'a' : 'div'`.

---

## 7. בדיקה לפני סיום (חובה)

```bash
# כל תמונה לאומן עטופה ב-anchor? (להריץ משורש הריפו)
python3 -c "
import re, pathlib
SKIP={'node_modules','trash','_staging','scratchpad'}
for p in pathlib.Path('.').rglob('*.html'):
    if SKIP & set(p.parts): continue
    if p.parts[0]=='artists' and len(p.parts)==3: continue   # artists/<slug>/index.html — הדף של האומן עצמו (§8)
    h=p.read_text(encoding='utf-8')
    for m in re.finditer(r'<img[^>]+src=\"([^\"]*(?:/artists/[a-z-]+/|/works/grid/|/exhibitions/[a-z-]+/artists/)[^\"]*)\"[^>]*>', h):
        pre=h[max(0,m.start()-400):m.start()]
        oa=pre.rfind('<a ')
        ca=pre.rfind('</a>')
        ok=oa>ca and 'artists/' in pre[oa:]
        if not ok: print('UNWRAPPED:', p, m.start())
"
# expected output: (empty)

# שמות עבריים בלי anchor — eyeball test על דף חדש.
```

⚠️ הבדיקה רואה HTML סטטי בלבד, ורק תמונות מ-`images/artists/`, `images/works/grid/` ו-`images/exhibitions/<slug>/artists/`. לא נבדקים: כרטיסים שמרונדרים ב-JS (גרידי `/artists/` ו-`/works/`, רצועות how-many/loneliness), `data-artist-href` של הקרוסלה, ו-thumbs מתיקיות אחרות (למשל `images/events/<slug>/artist-thumb.webp`) — אותם לבדוק בעין.

---

## 8. חריגים יחידים

- שם אומן בתוך עצם דף האומן (`artists/<slug>/index.html`) — לא מקשר לעצמו.
- אומן placeholder (`_pending_artist_pages` — היום `dan-ben-ary`, `racheli-reuven`) — קישור מעמוד `/artists/` חובה; בתערוכות/טקסטים — לפי §1.
- שם הבעלים/founder (`ארז זילינסקי רוזן`) → `about/` (מדף בעומק 2: `../../about/`), לא `/artists/`.

---

## 9. תזכורת — תמיד לקשר

גם בכותרת. גם ב-alt. גם ב-aria-label. גם בקפשן. גם ב-aside. אל תוסיף "סטטי טקסט עם שם אומן" בלי לקשר.
