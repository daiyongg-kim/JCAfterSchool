#!/usr/bin/env python3
"""
블로그 글 메타 보강 (idempotent) — Article JSON-LD + Open Graph + Twitter 카드 주입.

대상: web/blog/*.html (index.html, noindex 글 제외)
- og:title 없으면 OG/Twitter 블록을 canonical 다음 줄에 주입
- application/ld+json 없으면 Article JSON-LD를 </head> 직전에 주입
- DESC_OVERRIDES에 있는 글은 meta description도 교체 (네이버 발췌 정크 정제)

사용: python3 scripts/ensure-blog-meta.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "web" / "blog"
SITE = "https://jcafterschool.ca"
FALLBACK_IMAGE = f"{SITE}/img/hero.jpg"
PUBLISHER = {
    "@type": "Organization",
    "name": "JC After School (정철 애프터스쿨)",
    "url": SITE,
    "logo": {"@type": "ImageObject", "url": FALLBACK_IMAGE},
}

# 네이버 발췌 정크 description 교체 (title 복붙·문장 잘림 정제)
DESC_OVERRIDES = {
    "223008027736.html": "코퀴틀람 한인 방과후 보습학원 '정철 애프터스쿨' 오픈 스토리 — 픽업 라이드, 돌봄, 간식, 한국식 수학·영어까지 맞벌이 부모를 위한 원스톱 방과후를 시작합니다.",
    "223051877908.html": "정철 애프터스쿨 등록 안내 — 한국 정철어학원 출신 부부가 운영하는 코퀴틀람 방과후 학원. 픽업·돌봄·간식·수학·영어 학습까지 등록 절차와 운영 방식을 소개합니다.",
    "223178727582.html": "밴쿠버 한달살기·학기 중 오전수업이 필요한 가정을 위한 '아침 종합반' 개강 안내 — 오전 시간 학습과 활동을 한 번에, 코퀴틀람 정철 애프터스쿨.",
    "223520236152.html": "2024 여름방학캠프 현장 스케치 — 주 5일 풀타임 학습과 즐거운 액티비티로 문전성시를 이룬 코퀴틀람 정철 애프터스쿨 캠프 이야기.",
    "223904216463.html": "중·고등학생 입시전략·내신관리 멘토튜터링 가을반 모집 — 3:1 밀착 지도, 현직 교사·명문대 출신 교사진, 월~목 저녁 수업(저녁 제공). 선착순 마감.",
}

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}


def parse_date(html: str) -> str | None:
    """<div class="meta"> 안의 날짜 → ISO (한국식 '2023. 2. 7.' / 영문 'May 22, 2026')"""
    m = re.search(r'<div class="meta">([^<]*)', html)
    if not m:
        return None
    text = m.group(1)
    k = re.search(r"(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})", text)
    if k:
        return f"{k.group(1)}-{int(k.group(2)):02d}-{int(k.group(3)):02d}"
    e = re.search(r"([A-Z][a-z]+)\s+(\d{1,2}),\s*(\d{4})", text)
    if e and e.group(1) in MONTHS:
        return f"{e.group(3)}-{MONTHS[e.group(1)]:02d}-{int(e.group(2)):02d}"
    return None


def first_image(html: str) -> str | None:
    m = re.search(r'<img src="(img/[^"]+)"', html)
    return f"{SITE}/blog/{m.group(1)}" if m else None


def clean_title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    t = m.group(1).strip() if m else ""
    return re.sub(r"\s*·\s*정철 애프터스쿨( 블로그)?\s*$", "", t)


def get_meta_desc(html: str) -> str:
    m = re.search(r'<meta name="description" content="([^"]*)"', html)
    return m.group(1) if m else ""


def esc(s: str) -> str:
    return s.replace('"', "&quot;")


def process(path: Path) -> list[str]:
    html = path.read_text(encoding="utf-8")
    if "noindex" in html:
        return []
    changes = []

    # 1) description 정제
    if path.name in DESC_OVERRIDES:
        new_desc = DESC_OVERRIDES[path.name]
        cur = get_meta_desc(html)
        if cur != esc(new_desc):
            html = re.sub(
                r'(<meta name="description" content=")[^"]*(")',
                lambda m: m.group(1) + esc(new_desc) + m.group(2),
                html, count=1)
            changes.append("desc")

    title = clean_title(html)
    desc = get_meta_desc(html).replace("&quot;", '"').replace("&#x27;", "'").replace("&amp;", "&")
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    url = canon.group(1) if canon else f"{SITE}/blog/{path.name}"
    date = parse_date(html)
    image = first_image(html) or FALLBACK_IMAGE

    # 2) OG / Twitter
    if "og:title" not in html:
        block = "\n".join([
            f'<meta property="og:type" content="article">',
            f'<meta property="og:title" content="{esc(title)}">',
            f'<meta property="og:description" content="{esc(desc)}">',
            f'<meta property="og:url" content="{url}">',
            f'<meta property="og:image" content="{image}">',
            f'<meta property="og:locale" content="ko_KR">',
            f'<meta name="twitter:card" content="summary_large_image">',
            f'<meta name="twitter:title" content="{esc(title)}">',
            f'<meta name="twitter:description" content="{esc(desc)}">',
            f'<meta name="twitter:image" content="{image}">',
        ])
        html = html.replace(canon.group(0), canon.group(0) + "\n" + block, 1)
        changes.append("og")

    # 3) Article JSON-LD
    if "application/ld+json" not in html:
        ld = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": desc,
            "image": [image],
            "url": url,
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "author": {"@type": "Organization", "name": "JC After School (정철 애프터스쿨)", "url": SITE},
            "publisher": PUBLISHER,
            "inLanguage": "ko",
        }
        if date:
            ld["datePublished"] = date
            ld["dateModified"] = date
        script = ('<script type="application/ld+json">'
                  + json.dumps(ld, ensure_ascii=False)
                  + "</script>\n</head>")
        html = html.replace("</head>", script, 1)
        changes.append("jsonld")

    if changes:
        path.write_text(html, encoding="utf-8")
    return changes


def main():
    total = 0
    for f in sorted(BLOG.glob("*.html")):
        if f.name == "index.html":
            continue
        changes = process(f)
        if changes:
            total += 1
            print(f"  {f.name}: {', '.join(changes)}")
    print(f"✅ {total}개 파일 갱신")
    return 0


if __name__ == "__main__":
    sys.exit(main())
