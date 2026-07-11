# Worklog — JCAfterSchool

요청 내역과 결과 기록. 최신 항목이 맨 위. 규칙은 CLAUDE.md "Worklog 규칙" 참조.

## 2026-07-10 — 여름캠프 2주차 피날레(포스터 갤러리 완성) 블로그
- **요청**: `pic/20260710/` 사진 + memp.png(Diane 코멘트) 반영해 오늘자 블로그 포스팅.
- **결과**:
  - 사진 23장 검토, 12장 선별·최적화(`web/blog/img/camp-wk2day5-0710-*.jpg`).
  - 신규 `web/blog/camp-wk2day5-2026-07-10.html` — 구성: 🖼️완성된 포스터 갤러리 벽(hero) / ✍️마감 작업(Canada Goose·Different Kinds of Mice) / 🖼️하이라이트(Mouse Family·All the Types of Gyaru·캐나다 국기) / 🍕피자 금요일 / 🎹피아노 & Diane 셀피. Diane 메시지 카드("월요일 인터랙티브 발표 준비 완료, 좋은 주말") + 월요일(7/13) 발표 예고 배너. h1만 한글, 본문 영어.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가. 이미지 Read 검증 + 헤드리스 크롬 렌더 확인.

## 2026-07-09 — 여름캠프 2주차 4일차(로체스터 파크 필드트립) 블로그
- **요청**: `pic/20260709/` 사진으로 블로그 포스팅 (전날 예고된 로체스터 파크 필드트립 날).
- **결과**:
  - 사진 32장 검토, 14장 선별·최적화(`web/blog/img/camp-wk2day4-0709-*.jpg`).
  - 신규 `web/blog/camp-wk2day4-2026-07-09.html` — 구성: 🎨오전 포스터 작업(고양이·토끼) & 피아노 / 🍱점심(쌀밥·김치·김·불고기) / 🚌출발 / ⛲스플래시 패드 물놀이 / 🏖️모래놀이·피크닉 간식 / 🫐야생 블랙베리 따기. "여벌옷 유용" · "4시 전 귀원" 등 전날 안내와 호응하는 문구 포함. h1만 한글, 본문 영어.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가. 이미지 Read 검증 + 헤드리스 크롬 렌더 확인.

## 2026-07-08 — 여름캠프 2주차 3일차(리서치 포스터·팔씨름) 블로그
- **요청**: `pic/20260708/` 사진 + memo.png(수요·금요 튜터 공지) 반영해 블로그 업데이트.
- **결과**:
  - 사진 20장 검토, 15장 선별·최적화(`web/blog/img/camp-wk2day3-0708-*.jpg`).
  - 신규 `web/blog/camp-wk2day3-2026-07-08.html` — 구성: 📋화이트보드 하루 계획 / 🎨리서치 포스터(Cute Birds·토끼·버블티, 발표 연습 컷) / ✏️자유 그림(Spooky) / 🧩스도쿠 / 🍱불고기 점심(메모의 메뉴: 쌀밥·김치·김·불고기·동그랑땡·군만두) / 💪팔씨름 대결 / 🌳놀이터. **내일(7/9) 로체스터 파크 필드트립 안내 박스**(여벌옷·타올·부스터시트, 1:30 출발→4시 전 귀원, 한글 공지) 포함.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가. 이미지 Read 검증 + 헤드리스 크롬 렌더 확인.

## 2026-07-07 — 홈페이지 첫 방문 언어를 브라우저 locale로 자동 결정
- **요청**: 영문 locale 사용자에게는 영문이 먼저 보이게 할 수 없나 → locale 보고 결정하도록.
- **결과**: `web/index.html` 언어 초기화 로직 변경 — 우선순위: localStorage 수동 선택 > `navigator.languages[0]`(ko*면 한국어, 그 외 영어) > ko. 헤드리스 크롬(en-GB 환경)에서 첫 방문 시 영어 UI 렌더 확인, 판별식(ko/ko-KR→ko, en/fr/ja→en) 단위 검증. 한 번 언어를 고르면(또는 자동 결정되면) localStorage에 저장돼 이후 방문에 유지.

## 2026-07-07 — 여름캠프 2주차 2일차(꼬마 작가 스토리북) 블로그
- **요청**: `pic/20260707/` 사진으로 블로그 포스팅. Diane 코멘트는 메시지로 직접 전달("young writers — wrote, revised, and illustrated their own original stories… Fantastic work, Everyone!!!").
- **결과**:
  - 사진 49장 검토, 16장 선별·최적화(`web/blog/img/camp-wk2day2-0707-*.jpg`).
  - 신규 `web/blog/camp-wk2day2-2026-07-07.html` — 구성: ✍️영 라이터스 워크숍(마인드맵→초고→퇴고→삽화) / 📖대표작 "Stop Giving Up!" by Chloe(주인공 Peace, 표지·첫장·삽화·마지막장 4컷) / 📚다른 완성작("Be Friends!" 등) / 🍕피자 간식 / 🌳놀이터 / 🌸학원 앞 화단 물주기. Diane 메시지 카드. h1만 한글, 본문 영어.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가. 저장 이미지 Read 검증 + 헤드리스 크롬 렌더 확인.
  - 책 표지의 작가 이름(Chloe·Sua·Lona)은 아이가 직접 쓴 표지 사진 그대로 노출. 영상 5개 미사용.

## 2026-07-06 — 여름캠프 2주차 첫날(월드컵 BINGO·캔디 낚시·공원) 블로그
- **요청**: `pic/20260706/` 사진으로 2주차 블로그 포스팅. memo(memo.png)의 Diane 코멘트 반영.
- **결과**:
  - 사진 45장 검토(뒤쪽 39·40번은 41·42번과 동일 파일 크기의 중복 전송분), 18장 선별·최적화(`web/blog/img/camp-wk2-0706-*.jpg`).
  - 신규 `web/blog/camp-wk2day1-2026-07-06.html` — 2주차 첫날(월). 구성: 🔤월드컵 어휘 BINGO(직접 카드 제작) / 🗣️스피킹 연습(축구공 인형) / 🍱한식 점심 / ✂️Diane 공예(종이인형) / 🧁컵케이크 / 🎣캔디 낚시 게임 / 🌳공원+맥도날드. Diane 메시지 카드("research presentations 준비 시작·confidence-building") + 이번 주 리서치 발표 예고 배너. h1만 한글, 본문 영어.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가. 저장 이미지 Read 검증 + 헤드리스 크롬 렌더 확인.
  - 영상 8개 미사용. 아이 얼굴 노출 사진 포함 — 기존 캠프 포스트와 동일 기준(학부모 동의 전제).

## 2026-07-03 — 여름캠프 1주차 피날레(스포츠·과학·생일 피냐타) 블로그
- **요청**: `pic/20260703/` 사진으로 블로그 업데이트. Diane이 챗창에 남긴 메시지(comment.png) 반영.
- **결과**:
  - 사진 89장 md5 중복 제거→고유 83장 검토, 16장 선별·최적화(`web/blog/img/camp-day4-0703-*.jpg`).
  - 신규 `web/blog/camp-day4-2026-07-03.html` — 1주차 마지막 날. 구성: ⚽스포츠 데이(월드컵 테마) / 🔬과학 실험(베이킹소다+식초 풍선) / 🧲공예(단풍잎 자석·비즈 팔찌) / 🍱한식 점심 / 🎉생일 파티 & 피냐타. Diane 선생님 1주차 마무리 메시지 카드 + "Happy Birthday Sarah" 생일 배너. h1 제목만 한글, 본문 영어.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가, Day3↔Day4 상호링크. 헤드리스 크롬 렌더 확인.
  - 주의: 생일 주인공 이름(Sarah)을 화이트보드·Diane 메시지 근거로 표기 — 필요시 익명화 가능. 영상 10개·미선정 사진 미사용.

## 2026-07-02 — 여름캠프 필드트립(카메론 도서관+실내놀이터) 블로그
- **요청**: `pic/20260702/` 오늘 사진으로 블로그 업데이트. 로히드몰 Cameron Library와 실내놀이터 방문(목요일 필드트립).
- **결과**:
  - 사진 68장 중 md5 중복 제거 → 고유 31장, 그중 16장 선별·최적화(`web/blog/img/camp-day3-0702-*.jpg`).
  - 신규 `web/blog/camp-day3-2026-07-02.html` — 필드트립 테마. 구성: 🍱출발 전(오전 학습·한식 점심) / 📚카메론 도서관(단체사진·독서 코너·책 구경·선생님) / 🎪실내놀이터(클라이밍) / 🛍️몰 나들이(벽화·라운지·에스컬레이터·미니소·벤치). h1 제목만 한글, 본문 영어. Article JSON-LD·OG/Twitter.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가, Day2↔Day3 상호링크. 헤드리스 크롬 렌더 확인.
  - 참고: 영상 5개·중복/미선정 사진 미사용.

## 2026-06-30 — 여름캠프 2일차(캐나다데이) 블로그 + Day1 본문 영어화
- **요청**: (1) Day1 블로그 본문을 제목만 한글로 두고 모두 영어로 변경. (2) `pic/20260630/` 2일차 사진으로 Day1과 비슷한 형식의 블로그 제작. memo.png(Diane 선생님 메시지) 반영.
- **결과**:
  - `camp-day1-2026-06-29.html`: 본문·캡션·alt·메타·CTA·infocard 전부 영어화(h1 제목·title 태그만 한글). index 카드 발췌문도 영어.
  - 신규 `web/blog/camp-day2-2026-06-30.html` — 캐나다데이 스페셜 테마. 사진 54장 중 아이 등장 19장 선별·최적화(`web/blog/img/camp-day2-0630-*.jpg`). 구성: 🍁오전 학습·캐나다 공예 / 🧁팀 베이킹 / 🎂딸기 캐나다 케이크·컵케이크 / 🍱한식 점심 / 🎉국기 축하·단체사진. Diane 선생님 영어 메시지 카드(.msgcard)와 7/1 캐나다데이 휴무·목요일 필드트립 안내(.note) 포함. Article JSON-LD·OG/Twitter 메타.
  - `web/blog/index.html` 최상단 카드 추가, `web/sitemap.xml` URL 추가. 헤드리스 크롬 전체 렌더 확인.
  - 참고: 영상(.mp4 10개)·나머지 사진은 미사용.

## 2026-06-29 — 여름캠프 첫날 현장 스케치 블로그 (사진)
- **요청**: `pic/20260629/` 사진(시간 역순 저장, 오전 수업·점심·오후 등)으로 아이가 한 명이라도 나오는 블로그를 만들어 달라. 사진은 다 안 써도 됨.
- **결과**:
  - 37장 검토 후 아이가 등장하는 18장 선별 → `sips`로 웹 최적화(가로 1200px, q72) → `web/blog/img/camp-day1-0629-*.jpg`.
  - 신규 `web/blog/camp-day1-2026-06-29.html` 생성 — 디자인 시스템 적용, 하루 흐름(🌅오전 수업·만들기 / 🍱점심 한식 / 🎨오후 놀이·간식)으로 구성. grid2 사진 배치, figcaption, Article JSON-LD, OG/Twitter 메타 포함.
  - `web/blog/index.html` 최상단 카드 추가, `web/sitemap.xml`에 URL 추가.
  - 헤드리스 크롬 렌더 확인. (주의: zsh 배열 1-index 차이로 첫 변환이 한 칸 밀려 bash glob 배열로 재변환·검증함.)

## 2026-06-28 — 여름캠프 시작 안내 블로그 + 상단 배너 교체
- **요청**: 6/29(월) 캠프 시작 공지(준비물·간식/알러지·하루 일정·무료돌봄)를 블로그로 예쁘게 만들고, 상단 캠프 배너를 이 안내 바로가기로 바꾸기.
- **결과**:
  - 신규 `web/blog/summer-camp-start-2026.html` 생성 — 디자인 시스템(크림/네이비/레드, Pretendard) 적용. 준비물 체크리스트 카드, 알러지 강조 노트, 하루 일정 타임라인(8:30~19:00, 무료돌봄 하이라이트), CTA, EducationEvent JSON-LD, OG/Twitter 메타 포함.
  - `web/index.html` 상단 campbanner 링크를 `summer-camp-2026.html` → `summer-camp-start-2026.html`로 교체, 배지/타이틀/서브/CTA 문구를 "시작 안내"로 변경(한/영 i18n 동시).
  - `web/blog/index.html` 최상단에 새 글 카드 추가, `web/sitemap.xml`에 URL 추가.
  - 로컬 렌더 확인(콘솔 에러 없음), 배너 표시 확인.

## 2026-06-21 — Worklog 규칙 도입
- **요청**: 요청 내용과 결과를 모든 프로젝트의 CLAUDE.md/worklog.md에 기록. CLAUDE.md엔 인스트럭션, worklog.md엔 명령+결과.
- **결과**: 기존 CLAUDE.md에 "Worklog 규칙" 섹션 추가, worklog.md 신규 생성(이 항목).
