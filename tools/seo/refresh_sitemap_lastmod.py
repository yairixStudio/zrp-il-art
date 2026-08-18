#!/usr/bin/env python3
"""Refresh <lastmod> in sitemap.xml from the real last-change date of each page.

Date source per URL: last git commit that touched its index.html.
If the file has uncommitted changes (or is untracked) → filesystem mtime.

Idempotent, and surgical: URL order, indentation, <changefreq>/<priority>
and every other tag stay byte-identical — only the text inside <lastmod>
is rewritten. Also reports URLs whose page file is missing on disk.

Run from anywhere:  python3 tools/seo/refresh_sitemap_lastmod.py
"""
import re, sys, subprocess, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITEMAP = ROOT / "sitemap.xml"
BASE = "https://art.zrp.co.il/"


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args],
                          capture_output=True, text=True).stdout


def page_for(loc):
    rel = loc[len(BASE):] if loc.startswith(BASE) else loc.lstrip("/")
    return ROOT / (rel + "index.html")


def main():
    dirty = set(git("diff", "--name-only", "HEAD").split()) | \
            set(git("ls-files", "--others", "--exclude-standard").split())
    xml = SITEMAP.read_text(encoding="utf-8")
    blocks = re.findall(r"<url>.*?</url>", xml, re.S)
    updated = missing = 0

    for block in blocks:
        loc = re.search(r"<loc>([^<]+)</loc>", block).group(1)
        page = page_for(loc)
        if not page.exists():
            missing += 1
            print(f"  ! no page file for {loc}", file=sys.stderr)
            continue
        relpath = str(page.relative_to(ROOT))
        date = "" if relpath in dirty else git("log", "-1", "--format=%cs", "--", relpath).strip()
        if not date:
            date = datetime.date.fromtimestamp(page.stat().st_mtime).isoformat()
        old = re.search(r"<lastmod>([^<]*)</lastmod>", block).group(1)
        if date != old:
            xml = xml.replace(block, block.replace(f"<lastmod>{old}</lastmod>",
                                                   f"<lastmod>{date}</lastmod>"), 1)
            updated += 1

    SITEMAP.write_text(xml, encoding="utf-8")
    print(f"urls={len(blocks)} updated={updated} missing_files={missing}")


if __name__ == "__main__":
    main()
