#!/usr/bin/env python3
"""
JC After School — 네이버 블로그 → 사이트 블로그 자동 생성
RSS로 글 목록을 받고, 각 글 모바일 페이지에서 본문·이미지를 추출해
web/blog/{logNo}.html (각 글) + web/blog/index.html (목록)을 생성한다.
이미지는 web/blog/img/ 에 Pillow로 최적화 저장(GitHub Action 우분투 호환).

사용: python3 scripts/fetch-blog.py
의존성: Pillow  (pip install pillow)
"""
import re, html, json, sys, urllib.request, io
from pathlib import Path
from datetime import datetime
from email.utils import parsedate_to_datetime
from PIL import Image, ImageOps

BLOG_ID = "8488jy"
BLOG_NAME = "정철 애프터스쿨"
RSS_URL = f"https://rss.blog.naver.com/{BLOG_ID}.xml"
KAKAO = "https://open.kakao.com/o/sn2X2Kii"

ROOT = Path(__file__).parent.parent
OUT = ROOT / "web" / "blog"
IMG = OUT / "img"
MANUAL_JSON = ROOT / "scripts" / "manual-posts.json"
UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"


def fetch(url, referer=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **({"Referer": referer} if referer else {})})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read()


def get_posts():
    xml = fetch(RSS_URL).decode("utf-8", "ignore")
    posts = []
    for it in re.findall(r"<item>(.*?)</item>", xml, re.S):
        def g(tag):
            m = re.search(rf"<{tag}>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</{tag}>", it, re.S)
            return (m.group(1).strip() if m else "")
        link = g("link")
        m = re.search(rf"{BLOG_ID}/(\d+)", link)
        if not m:
            continue
        try:
            d = parsedate_to_datetime(g("pubDate"))
            date_str = f"{d.year}. {d.month}. {d.day}."
            iso = d.strftime("%Y-%m-%d")
        except Exception:
            date_str, iso = "", ""
        posts.append({"logNo": m.group(1), "title": g("title"), "category": g("category"),
                      "date": date_str, "iso": iso})
    return posts


def parse_post(logno):
    """모바일 페이지에서 (텍스트/이미지) 순서 리스트 추출."""
    htmltext = fetch(f"https://m.blog.naver.com/{BLOG_ID}/{logno}").decode("utf-8", "ignore")
    tokens = re.findall(
        r'(<p[^>]*class="se-text-paragraph[^"]*"[^>]*>.*?</p>)|(<img[^>]+class="se-image-resource"[^>]*>)',
        htmltext, re.S)
    items = []
    for ptag, imgtag in tokens:
        if ptag:
            txt = html.unescape(re.sub(r"<[^>]+>", "", ptag)).replace("​", "").replace("﻿", "").strip()
            if txt:
                items.append(("text", txt))
        elif imgtag:
            m = re.search(r'data-lazy-src="([^"]+)"', imgtag) or re.search(r'src="([^"]+)"', imgtag)
            if m:
                items.append(("img", m.group(1).split("?")[0]))
    return items


def save_image(url, dest, max_w=900, quality=62):
    if dest.exists():
        return True
    try:
        raw = fetch(url + "?type=w800", referer=f"https://blog.naver.com/{BLOG_ID}")
        im = ImageOps.exif_transpose(Image.open(io.BytesIO(raw))).convert("RGB")  # EXIF 방향 적용
        if im.width > max_w:
            im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
        dest.parent.mkdir(parents=True, exist_ok=True)
        im.save(dest, "JPEG", quality=quality, optimize=True)
        return True
    except Exception as e:
        print(f"  ! 이미지 실패 {url}: {e}")
        return False


# ── HTML 템플릿 ──────────────────────────────────────────
CSS = """:root{--cream:#FBF8F3;--cream-2:#F4EEE4;--navy:#1C2A3A;--navy-soft:#34465A;--red:#D6402F;--red-dark:#B8331F;--amber:#E8A33D;--gray:#8A8178;--line:#E7DFD3;--kr:'Pretendard',-apple-system,sans-serif;--en:'Fraunces',Georgia,serif;--r-sm:6px;--r-md:8px;--r-lg:12px;--shadow-sm:0 10px 26px -16px rgba(28,42,58,.30);--shadow-md:0 20px 50px -28px rgba(28,42,58,.42)}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:var(--kr);background:var(--cream);color:var(--navy);line-height:1.75;-webkit-font-smoothing:antialiased}a{color:inherit;text-decoration:none}
header{position:sticky;top:0;z-index:50;background:rgba(251,248,243,.9);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.nav{max-width:1000px;margin:0 auto;display:flex;align-items:center;gap:10px;height:64px;padding:0 24px}
.logo{display:flex;align-items:center;gap:8px;font-weight:800;font-size:17px}
.logo .mark{display:grid;place-items:center;width:30px;height:30px;border-radius:var(--r-sm);background:var(--red);color:#fff;font-weight:900;font-size:13px;font-family:var(--en)}
.nav .back{margin-left:auto;font-size:14px;font-weight:700;color:var(--red)}"""

POST_CSS = """article{max-width:760px;margin:0 auto;padding:44px 24px 80px}
.cat{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--red);margin-bottom:14px}
h1{font-size:clamp(28px,5vw,38px);line-height:1.25;letter-spacing:-.02em;font-weight:800;margin-bottom:14px}
.meta{font-size:13.5px;color:var(--gray);padding-bottom:24px;margin-bottom:32px;border-bottom:1px solid var(--line)}
article p{font-size:17px;color:#2b3a4a;margin:0 0 20px}article p.tags{font-size:13.5px;color:var(--amber);font-weight:700;margin-bottom:6px;word-break:keep-all}
article figure{margin:28px 0}article figure img{width:100%;border-radius:var(--r-lg);border:1px solid var(--line);box-shadow:var(--shadow-sm);display:block}
.source{margin-top:40px;padding:18px 20px;background:var(--cream-2);border:1px solid var(--line);border-radius:var(--r-md);font-size:13.5px;color:var(--navy-soft)}.source a{color:var(--red);font-weight:700}
.cta{margin-top:36px;display:flex;gap:12px;flex-wrap:wrap}.btn{font-weight:700;border-radius:var(--r-sm);padding:12px 22px;font-size:15px;display:inline-block}.btn-primary{background:var(--red);color:#fff}.btn-ghost{border:1.5px solid var(--navy);color:var(--navy)}
.langsw{display:inline-flex;gap:2px;font-size:13px;font-weight:700;border:1px solid var(--line);border-radius:var(--r-sm);overflow:hidden;margin-bottom:18px}.langsw a{padding:5px 12px;color:var(--gray)}.langsw a.on{background:var(--navy);color:var(--cream)}"""

INDEX_CSS = """.wrap{max-width:1000px;margin:0 auto;padding:48px 24px 80px}
.head{margin-bottom:36px}.head .lbl{font-family:var(--en);font-style:italic;font-size:16px;color:var(--red)}
.head h1{font-size:34px;font-weight:800;letter-spacing:-.02em;margin:6px 0 8px}.head p{color:var(--navy-soft)}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.post{background:var(--cream);border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow-sm);transition:.2s;display:flex;flex-direction:column}
.post:hover{transform:translateY(-3px);box-shadow:var(--shadow-md)}
.post .thumb{aspect-ratio:16/10;background:linear-gradient(160deg,#FDF3E3,#F4EEE4);overflow:hidden}
.post .thumb img{width:100%;height:100%;object-fit:cover;display:block}
.post .body{padding:18px 20px 20px;display:flex;flex-direction:column;flex:1}
.post .cat{font-size:11px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:var(--red)}
.post h2{font-size:18px;font-weight:800;letter-spacing:-.01em;margin:8px 0 8px;line-height:1.35}
.post .ex{font-size:14px;color:var(--navy-soft);flex:1;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.post .date{font-size:12.5px;color:var(--gray);margin-top:14px}
footer{border-top:1px solid var(--line);padding:30px 24px;text-align:center;font-size:13.5px;color:var(--navy-soft)}footer a{color:var(--red);font-weight:700}
@media(max-width:880px){.grid{grid-template-columns:1fr 1fr}}@media(max-width:560px){.grid{grid-template-columns:1fr}}"""


def head_html(title, desc, canonical, htmllang="ko"):
    return f"""<!DOCTYPE html>
<html lang="{htmllang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css" />
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;1,9..144,500&display=swap" rel="stylesheet">
<style>{CSS}\n{{extra}}</style>
</head>
<body>
<header><div class="nav">
  <a class="logo" href="{{home}}"><span class="mark">JC</span> {BLOG_NAME}</a>
  <a class="back" href="{{back_href}}">{{back_txt}}</a>
</div></header>"""


def render_post(post, items, imgmap):
    parts = []
    img_i = 0
    for kind, val in items:
        if kind == "text":
            cls = ' class="tags"' if val.startswith("#") else ""
            parts.append(f"<p{cls}>{html.escape(val)}</p>")
        else:
            img_i += 1
            fn = imgmap.get(img_i)
            if fn:
                parts.append(f'<figure><img src="img/{fn}" alt="" loading="lazy"></figure>')
    body = "\n      ".join(parts)
    excerpt = next((v for k, v in items if k == "text" and not v.startswith("#") and len(v) > 12), post["title"])
    head = head_html(f'{post["title"]} · {BLOG_NAME} 블로그', excerpt[:120],
                     f'https://jcafterschool.ca/blog/{post["logNo"]}.html')
    head = head.replace("{extra}", POST_CSS).replace("{home}", "../index.html").replace("{back_href}", "index.html").replace("{back_txt}", "← 블로그 목록")
    return head + f"""
<article>
  <span class="cat">{html.escape(post["category"] or "소식")}</span>
  <h1>{html.escape(post["title"])}</h1>
  <div class="meta">{BLOG_NAME} · {post["date"]}</div>
  {body}
  <div class="cta">
    <a class="btn btn-primary" href="../index.html#contact">무료 체험 신청 →</a>
    <a class="btn btn-ghost" href="index.html">블로그 목록</a>
  </div>
</article>
</body>
</html>"""


def render_index(cards):
    head = head_html(f"블로그 · {BLOG_NAME}", f"{BLOG_NAME}의 소식, 캠프, 수업 이야기.",
                     "https://jcafterschool.ca/blog/")
    head = head.replace("{extra}", INDEX_CSS).replace("{home}", "../index.html").replace("{back_href}", "../index.html").replace("{back_txt}", "← 홈으로")
    return head + f"""
<div class="wrap">
  <div class="head">
    <div class="lbl">Blog</div>
    <h1>블로그 · 소식</h1>
    <p>방과후 돌봄, 캠프, 수업 이야기를 전합니다.</p>
  </div>
  <div class="grid">
    {cards}
  </div>
</div>
</body>
</html>"""


def render_manual(pair, lang, solo=False):
    """수동 글. lang='ko'|'en'. solo=True면 단일 언어(토글 없음, {slug}.html)."""
    data = pair[lang]
    self_url = f'{pair["slug"]}.html' if (solo or lang == "ko") else f'{pair["slug"]}-en.html'
    cat = pair[f"category_{lang}"]
    date = pair[f"date_{lang}"]
    L = {"ko": {"home": "../index.html", "back": "← 블로그 목록", "by": "정철 애프터스쿨",
                "trial": "무료 체험 신청 →", "list": "블로그 목록"},
         "en": {"home": "../index.html", "back": "← Blog", "by": "JC After School",
                "trial": "Get a Free Trial →", "list": "Blog"}}[lang]
    parts = []
    for b in data["blocks"]:
        if b["t"] == "text":
            cls = ' class="tags"' if b["v"].startswith("#") else ""
            parts.append(f'<p{cls}>{html.escape(b["v"])}</p>')
        else:
            parts.append(f'<figure><img src="img/{b["v"]}" alt="" loading="lazy"></figure>')
    body = "\n      ".join(parts)
    head = head_html(f'{data["title"]} · {BLOG_NAME}', data["title"],
                     f'https://jcafterschool.ca/blog/{self_url}', htmllang=lang)
    head = head.replace("{extra}", POST_CSS).replace("{home}", L["home"]).replace("{back_href}", "index.html").replace("{back_txt}", L["back"])
    if solo:
        toggle = ""
    else:
        ko_cls = "on" if lang == "ko" else ""
        en_cls = "on" if lang == "en" else ""
        toggle = (f'<div class="langsw"><a href="{pair["slug"]}.html" class="{ko_cls}">한국어</a>'
                  f'<a href="{pair["slug"]}-en.html" class="{en_cls}">EN</a></div>')
    return head + f"""
<article>
  {toggle}
  <span class="cat">{html.escape(cat)}</span>
  <h1>{html.escape(data["title"])}</h1>
  <div class="meta">{L["by"]} · {date}</div>
  {body}
  <div class="cta">
    <a class="btn btn-primary" href="../index.html#contact">{L["trial"]}</a>
    <a class="btn btn-ghost" href="index.html">{L["list"]}</a>
  </div>
</article>
</body>
</html>"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    IMG.mkdir(parents=True, exist_ok=True)
    posts = get_posts()
    print(f"RSS 글 {len(posts)}개")
    cards = []  # (iso, html) 튜플로 모아 날짜순 정렬
    for p in posts:
        try:
            items = parse_post(p["logNo"])
        except Exception as e:
            print(f"  ! {p['logNo']} 파싱 실패: {e}")
            items = []
        # 이미지 저장
        imgmap = {}
        n = 0
        for kind, val in items:
            if kind == "img":
                n += 1
                fn = f'{p["logNo"]}-{n}.jpg'
                if save_image(val, IMG / fn):
                    imgmap[n] = fn
        # 본문이 없으면(파싱 실패) 스킵하지 않고 요약+링크만이라도
        (OUT / f'{p["logNo"]}.html').write_text(render_post(p, items, imgmap), encoding="utf-8")
        # 인덱스 카드
        thumb = f'<img src="img/{imgmap[1]}" alt="" loading="lazy">' if imgmap.get(1) else ""
        excerpt = next((v for k, v in items if k == "text" and not v.startswith("#") and len(v) > 12), "")
        cards.append((p["iso"], f'''<a class="post" href="{p["logNo"]}.html">
      <div class="thumb">{thumb}</div>
      <div class="body"><span class="cat">{html.escape(p["category"] or "소식")}</span>
        <h2>{html.escape(p["title"])}</h2>
        <p class="ex">{html.escape(excerpt[:100])}</p>
        <div class="date">{p["date"]}</div></div></a>'''))
        print(f'  ✓ {p["logNo"]} {p["title"][:30]} (이미지 {len(imgmap)})')

    # ── 수동 글(영/한) 병합 ──
    manual = []
    if MANUAL_JSON.exists():
        manual = json.loads(MANUAL_JSON.read_text(encoding="utf-8"))
    for pair in manual:
        langs = pair.get("publish", ["ko", "en"])
        solo = len(langs) == 1
        if solo:
            lg = langs[0]
            (OUT / f'{pair["slug"]}.html').write_text(render_manual(pair, lg, solo=True), encoding="utf-8")
            # 단일 언어이므로 -en 페이지가 남아있으면 제거
            stray = OUT / f'{pair["slug"]}-en.html'
            if stray.exists():
                stray.unlink()
            card_lang = lg
        else:
            (OUT / f'{pair["slug"]}.html').write_text(render_manual(pair, "ko"), encoding="utf-8")
            (OUT / f'{pair["slug"]}-en.html').write_text(render_manual(pair, "en"), encoding="utf-8")
            card_lang = "ko"
        data = pair[card_lang]
        thumb_img = next((b["v"] for b in data["blocks"] if b["t"] == "img"), None)
        thumb = f'<img src="img/{thumb_img}" alt="" loading="lazy">' if thumb_img else ""
        excerpt = next((b["v"] for b in data["blocks"] if b["t"] == "text" and not b["v"].startswith("#")), "")
        cards.append((pair["iso"], f'''<a class="post" href="{pair["slug"]}.html">
      <div class="thumb">{thumb}</div>
      <div class="body"><span class="cat">{html.escape(pair["category_" + card_lang])}</span>
        <h2>{html.escape(data["title"])}</h2>
        <p class="ex">{html.escape(excerpt[:100])}</p>
        <div class="date">{pair["date_" + card_lang]}</div></div></a>'''))
        print(f'  ✓ [수동] {pair["slug"]} ({"/".join(langs)})')

    # 날짜 내림차순 정렬
    cards.sort(key=lambda c: c[0], reverse=True)
    (OUT / "index.html").write_text(render_index("\n    ".join(h for _, h in cards)), encoding="utf-8")

    # ── sitemap.xml 자동 생성 (홈 + 블로그 목록 + 모든 글) ──
    today = __import__("datetime").date.today().isoformat()
    urls = [("https://jcafterschool.ca/", today, "1.0"),
            ("https://jcafterschool.ca/blog/", today, "0.8")]
    for p in posts:
        urls.append((f'https://jcafterschool.ca/blog/{p["logNo"]}.html', p["iso"] or today, "0.6"))
    for pair in manual:
        lg = pair.get("publish", ["ko", "en"])
        urls.append((f'https://jcafterschool.ca/blog/{pair["slug"]}.html', pair["iso"], "0.6"))
        if len(lg) > 1:
            urls.append((f'https://jcafterschool.ca/blog/{pair["slug"]}-en.html', pair["iso"], "0.6"))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, mod, pri in urls:
        sm.append(f'  <url><loc>{loc}</loc><lastmod>{mod}</lastmod><changefreq>weekly</changefreq><priority>{pri}</priority></url>')
    sm.append('</urlset>')
    (ROOT / "web" / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    print(f"\n✅ 완료: web/blog/index.html + RSS {len(posts)}개 + 수동 {len(manual)}쌍")
    print(f"   sitemap.xml: {len(urls)}개 URL")


if __name__ == "__main__":
    main()
