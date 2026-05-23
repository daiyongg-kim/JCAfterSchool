#!/usr/bin/env python3
"""
JC After School — Google 리뷰 자동 수집
MarketingTeam/scripts/fetch-gsc.py 와 같은 패턴. Google Places API (New) 사용.

- GCP 프로젝트는 기존 'sosofamily-marketing' 재사용 (Places API만 추가로 enable).
- API 키 인증(서비스계정/OAuth 아님). 키는 코드에 넣지 말고 아래 경로/환경변수로.
- 공개 리뷰만 가져오며 Google 제한상 '최대 5개'만 반환됨.
- 결과: web/reviews.json  (사이트가 이 파일을 읽어 Warm Trust 카드로 렌더)

사용:
  # 키: 환경변수 GOOGLE_PLACES_API_KEY  또는  .credentials/places-api-key.txt
  # Place ID: 환경변수 JC_PLACE_ID  또는  아래 PLACE_ID 상수
  python3 scripts/fetch-reviews.py
"""
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

# ── 설정 ─────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
OUT = ROOT / "web" / "reviews.json"
CRED = ROOT / ".credentials" / "places-api-key.txt"

PLACE_ID = os.environ.get("JC_PLACE_ID", "ChIJ4YzXflV5hlQRVbvCp3d9zhA")  # JC After School (Coquitlam)
MIN_TEXT_LEN = 2          # 이 길이 미만(별점만 등)은 제외
LANGUAGE = "ko"


def get_api_key() -> str:
    key = os.environ.get("GOOGLE_PLACES_API_KEY", "").strip()
    if not key and CRED.exists():
        key = CRED.read_text(encoding="utf-8").strip()
    if not key or key.startswith("YOUR_"):
        sys.exit("❌ API 키가 없습니다. GOOGLE_PLACES_API_KEY 또는 "
                 ".credentials/places-api-key.txt 를 설정하세요.")
    return key


def fetch_place(api_key: str, place_id: str) -> dict:
    url = f"https://places.googleapis.com/v1/places/{place_id}?languageCode={LANGUAGE}"
    field_mask = "id,displayName,rating,userRatingCount,reviews"
    req = urllib.request.Request(url, headers={
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": field_mask,
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")
        sys.exit(f"❌ Places API 오류 {e.code}: {body}")


def main() -> None:
    if PLACE_ID.startswith("YOUR_"):
        sys.exit("❌ Place ID가 없습니다. JC_PLACE_ID 환경변수 또는 PLACE_ID 상수를 설정하세요.")
    data = fetch_place(get_api_key(), PLACE_ID)

    reviews = []
    for rv in data.get("reviews", []):
        text = (rv.get("text") or {}).get("text") or (rv.get("originalText") or {}).get("text") or ""
        text = text.strip()
        if len(text) < MIN_TEXT_LEN:
            continue  # 별점만 있는 리뷰는 제외
        author = (rv.get("authorAttribution") or {}).get("displayName", "익명")
        reviews.append({
            "name": author,
            "rating": rv.get("rating", 5),
            "text": text,
            "when": rv.get("relativePublishTimeDescription", ""),
        })

    out = {
        "rating": data.get("rating"),
        "total": data.get("userRatingCount"),
        "reviews": reviews,
        "place_id": PLACE_ID,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 리뷰 {len(reviews)}개 저장 (전체 평점 {out['rating']}, 리뷰수 {out['total']})")
    print(f"   → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
