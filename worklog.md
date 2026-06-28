# Worklog — JCAfterSchool

요청 내역과 결과 기록. 최신 항목이 맨 위. 규칙은 CLAUDE.md "Worklog 규칙" 참조.

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
