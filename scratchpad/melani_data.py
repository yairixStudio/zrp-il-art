# -*- coding: utf-8 -*-
"""Add melani hekimoglu (artist + 5 works + residency statement) and move the two
   residency artists out of the top of the lists into the middle (designer note)."""
import json, io, collections

def load(p): return json.load(open(p, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
def save(p, d): 
    open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")

# ---------- 1) artists.json ----------
A = load("data/artists.json")
arts = A["artists"]
assert not any(a["slug"] == "melani-hekimoglu" for a in arts)
melani = collections.OrderedDict([
    ("id", "melani-hekimoglu"),
    ("slug", "melani-hekimoglu"),
    ("name_en", "melani hekimoglu"),
    ("name_he", "מלאני הקימוגלו"),
    ("portrait", "images/artists/melani-hekimoglu/portrait.webp"),
    ("work_image", None),
    ("instagram_handle", "@melani.ceramics"),
    ("bio_he",
     "מלאני הקימוגלו היא אמנית ומעצבת, שעשייתה נעה בין אמנות עכשווית לעיצוב פונקציונלי. "
     "בעבודתה, המבוססת בעיקר על חומר קרמי, היא חוקרת חומר וצורה דרך פיסול, מיצב ואובייקטים "
     "פונקציונליים ואספניים.\n\n"
     "הפרקטיקה האמנותית שלה עוסקת בזמן, שינוי ומחזוריות, ומבקשת להחזיר את תשומת הלב לרגעים "
     "בודדים בעולם שהולך ונעשה מהיר יותר. הצורות הקרמיות שלה חוקרות נזילות שקפאה בזמן, ולוכדות "
     "תנועה בחומר בין כוונה לספונטניות, כאשר כל פריט מעוצב באופן אינדיבידואלי ויחיד במינו."),
    ("bio_en", None),
    ("works", []),
    ("curator_slug", "korin-avraham"),
    ("figma_artist_page_mobile", "XhGH289YTRcW811wrufRJz::1634:188"),
    ("figma_artist_page_desktop", None),
    ("homepage_featured", False),
])
arts.append(melani)
save("data/artists.json", A)
print("artists.json:", len(arts), "artists")

# ---------- 2) works.json ----------
W = load("data/works.json")
AW = W["art_works"]
assert not any(w["id"].startswith("melani-hekimoglu") for w in AW)

GALLERY = ("dizengoff", "Dizengoff Square Gallery")
VASE_DETAILS = ("כל אגרטל משתנה בגובהו ובצורתו עקב תהליך היצירה הבלתי צפוי. "
                "הגבהים נעים בדרך כלל בין 6 ל-25 ס\"מ.")
SPECS = [
    # (n, title_en, details_he, w, h, widths)
    (1, "flow vases",          VASE_DETAILS, 548, 628,  [480, 548]),
    (2, "flow dessert bowl",   "קערת קינוחים\n12x12 ס\"מ", 789, 981, [480, 789]),
    # NOTE: Figma reuses the FLOW VASES details string verbatim on BLOOM PLANTER
    # ("every vase varies in height") — kept verbatim, logged in docs/todo.md.
    (3, "bloom planter",       VASE_DETAILS, 1241, 927, [480, 768, 1080, 1241]),
    (4, "flow plates & bowls",
     "צלחת קינוחים רוחב 16 ס\"מ\nצלחת מנה ראשונה רוחב 22 ס\"מ\nצלחת מנה עיקרית רוחב 27 ס\"מ",
     791, 988, [480, 791]),
    (5, "flow lamp",
     "מנורות Flow\nהגודל משתנה עקב תהליך היצירה הבלתי צפוי.\nרוחב של +- 45 ס\"מ.",
     967, 1208, [480, 768, 967]),
]
mel_works = []
for n, ten, det, w, h, widths in SPECS:
    mel_works.append(collections.OrderedDict([
        ("id", "melani-hekimoglu-%d" % n),
        ("artist_slug", "melani-hekimoglu"),
        ("artist_he", "מלאני הקימוגלו"),
        ("artist_en", "melani hekimoglu"),
        ("title_he", None),
        ("title_en", ten),
        ("gallery_slug", GALLERY[0]),
        ("gallery_en", GALLERY[1]),
        ("sold", False),
        ("details_he", det),
        ("img", "melani-hekimoglu-%d" % n),
        ("w", w), ("h", h), ("widths", widths),
        ("artist_page_pos", n),
        # No exhibition: the residency has no group heading in the frame (1634:188).
        ("exhibition_title_he", None),
        ("exhibition_slug", None),
        ("exhibition_route", None),
        ("kind", "residency"),
        ("page", True),
    ]))

shira = [w for w in AW if w["artist_slug"] == "shira-turbowicz"]
assert len(shira) == 3 and AW[:3] == shira, "expected shira's 3 works at the head"
rest = AW[3:]
block = shira + mel_works
INSERT_AT = 70                      # centres the 8-work block in the 149-item grid
W["art_works"] = rest[:INSERT_AT] + block + rest[INSERT_AT:]
print("art_works:", len(W["art_works"]), "| block at 1-based",
      W["art_works"].index(block[0]) + 1, "-", W["art_works"].index(block[-1]) + 1)

W["exhibition_statements"].append(collections.OrderedDict([
    ("artist_slug", "melani-hekimoglu"),
    ("exhibition_title_he", None),
    ("exhibition_slug", None),
    ("exhibition_route", None),
    ("statement_he", [
        "בין התאריכים 28.09.2026–05.10.2026 תהפוך הגלריה של ארז זילינסקי רוזן בכיכר דיזנגוף "
        "לסטודיו זמני ולמרחב עבודה פתוח",
        "מלאני תעבוד במקום על יצירה חדשה ותשתמש בזמן ובחלל למחקר, ניסוי ופיתוח רעיונות דרך "
        "טקסטורה, צורה, חומר ותנועה.",
        "העבודה תתרחש ותתפתח בגלריה בזמן אמת, ללא תוצאה שנקבעה מראש. גם הקהל יהפוך לחלק "
        "מהתהליך: המבקרים יוכלו להיכנס, לפגוש את מלאני בזמן העבודה, להתבונן, לשוחח ולהגיב, "
        "כשהמפגשים עצמם עשויים להשפיע על הדרך שבה העבודה מתפתחת.",
        "שבוע שבו הגלריה אינה רק המקום שבו מציגים אמנות, אלא המקום שבו היא נוצרת.",
    ]),
]))
save("data/works.json", W)
print("exhibition_statements:", len(W["exhibition_statements"]))
