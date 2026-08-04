# todo.md — Known Gaps & TODO

> **קרא את הקובץ הזה כש:** אתה בודק אם משימה כבר נעשתה, מקבל בקשה הקשורה ל-assets חסרים (logo/placeholder hero), placeholder data, או infrastructure שעוד לא קיים. **בסוף משימה — סמן `[x]` ל-TODO שסגרת ועדכן אם נדבק שמשהו חסר.**

---

## פתוח

- [ ] **דף אירוע חסר — כרטיס "בקרוב" בעמוד `/press/`:** `event-tal-nehoray-talk` (how many... with tal nehoray, 29.6.2026), `route:null` ב-`press.json`; הכרטיס `pcard--soon` ב-`press/index.html` מציג טוסט "בקרוב" בלחיצה. (מאז press-9 של 2026-08-04 הכרטיס כבר לא בהומפייג'.) כשיהיה frame בפיגמה — לבנות דף, לעדכן `route` ולהחליף `href="#"`. (~~event-anat-wegier-talk~~ ✅ נבנה 2026-07-24 — `events/anat-wegier/`, Figma `1107:2090`/`1107:1981`.)
- [ ] **`tools/seo/inject.py` מיושן מול ה-HTML המקומיט (התגלה 2026-07-26):** `og-dims.json` חלקי (160/209 — ההשלמה חיה ב-`/tmp/og_dims.json` שאבד) ו-`breadcrumb()` עדיין מפנה ל-`/press/` ו-`/curators/` שלא נבנו. הרצה גורפת = רגרסיה של ~70 דפים. לתקן: לג'נרט og-dims מלא מ-`og/` + פילטר crumbs לפי קיום הדף. עד אז — להריץ רק על דפים חדשים ולשחזר את השאר (ראה lessons 2026-07-26).
- [ ] **Dizengoff archive thumbs** — `archive_thumbnails.tabs[0]` עדיין `_placeholder:true`. כשהגלריה תיפתח ויהיו צילומים מהתערוכה — לעדכן את 4 ה-`image` paths ב-`data/exhibitions.json` *ובמקביל* ב-fallback inline JSON ב-`index.html` (id=`fallback-archive`).
- [ ] `images/brand/logo.svg` עוד לא קיים.
- [ ] `images/galleries/flea-market/hero.png` — placeholder (עותק של dizengoff).
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
