#!/usr/bin/env python3
"""
독립 sitemap 생성기 — web/ 스캔 → web/sitemap.xml 재생성.

네이버 sync 비의존. 글 추가/변경 시 한 번 실행:
    python3 scripts/gen-sitemap.py

규칙:
- web/index.html (홈) priority 1.0, lastmod = 파일 수정일
- web/blog/ 인덱스 priority 0.8, lastmod = 최신 글 날짜
- web/blog/*.html 글: noindex 글 제외, lastmod = 본문 <div class="meta"> 날짜
  (없으면 파일 수정일), priority는 PRIORITY_OVERRIDES 우선, 기본 0.6
"""
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
SITE = "https://jcafterschool.ca"

PRIORITY_OVERRIDES = {
    "summer-camp-2026.html": "0.9",  # 시즌 핵심 모집 페이지
}

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}


def post_date(html: str, path: Path) -> str:
    m = re.search(r'<div class="meta">([^<]*)', html)
    if m:
        text = m.group(1)
        k = re.search(r"(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})", text)
        if k:
            return f"{k.group(1)}-{int(k.group(2)):02d}-{int(k.group(3)):02d}"
        e = re.search(r"([A-Z][a-z]+)\s+(\d{1,2}),\s*(\d{4})", text)
        if e and e.group(1) in MONTHS:
            return f"{e.group(3)}-{MONTHS[e.group(1)]:02d}-{int(e.group(2)):02d}"
    return datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()


def url_entry(loc: str, lastmod: str, priority: str) -> str:
    return (f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>"
            f"<changefreq>weekly</changefreq><priority>{priority}</priority></url>")


def main():
    entries = []
    home = WEB / "index.html"
    entries.append(url_entry(
        f"{SITE}/",
        datetime.date.fromtimestamp(home.stat().st_mtime).isoformat(),
        "1.0"))

    posts = []
    skipped = []
    for f in sorted(WEB.glob("blog/*.html")):
        if f.name == "index.html":
            continue
        html = f.read_text(encoding="utf-8")
        if "noindex" in html:
            skipped.append(f.name)
            continue
        posts.append((post_date(html, f), f.name))

    posts.sort(reverse=True)  # 최신순
    newest = posts[0][0] if posts else datetime.date.today().isoformat()
    entries.append(url_entry(f"{SITE}/blog/", newest, "0.8"))
    for date, name in posts:
        entries.append(url_entry(
            f"{SITE}/blog/{name}", date,
            PRIORITY_OVERRIDES.get(name, "0.6")))

    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(entries) + "\n</urlset>\n")
    (WEB / "sitemap.xml").write_text(xml, encoding="utf-8")
    print(f"✅ sitemap.xml 재생성 — URL {len(entries)}개 (글 {len(posts)}, noindex 제외 {len(skipped)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
