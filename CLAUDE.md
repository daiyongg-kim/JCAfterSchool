# JC After School (정철 애프터스쿨) — Project

캐나다 BC Coquitlam의 한인 방과후 돌봄 + 튜터링 + 성인 어학 학원의 홍보·등록 사이트.
한글 기본 / 영어 옵션 (i18n).

## 핵심 컨텍스트
- **포지셔닝:** "맡기면 성적까지" 원스톱 — 픽업 → 돌봄 → 간식 → 수학·과학·영어
- **우선순위:** 1)방과후 돌봄(간판) 2)자녀 튜터링(수학·과학·ELL) 3)성인 어학(IELTS·불어 TEF/TCF)
- **메인 CTA:** 무료 체험(트라이얼) / 성인 트랙은 무료 레벨테스트
- 기획·벤치마킹: `BENCHMARK.md` · 디자인 시스템: `DESIGN.md`

## Design System
Always read `DESIGN.md` before making any visual or UI decisions.
All font choices, colors, spacing, and aesthetic direction are defined there.
Do not deviate without explicit user approval.
In QA mode, flag any code that doesn't match DESIGN.md.

핵심 토큰: 배경 크림 `#FBF8F3` · 텍스트 네이비 `#1C2A3A` · 브랜드 레드 `#D6402F`(포인트로만) ·
앰버 `#E8A33D`(절제) · Pretendard 본문 · 모서리 8px 샤프 · 소프트 그림자.

## Skill routing
When the user's request matches an available skill, invoke it via the Skill tool. When in doubt, invoke the skill.
- Product ideas/brainstorming → /office-hours
- Design system/plan review → /design-consultation or /plan-design-review
- Visual polish → /design-review
- Bugs/errors → /investigate
- QA/testing site behavior → /qa or /qa-only
- Ship/deploy/PR → /ship or /land-and-deploy

## 작업 전 동기화 규칙 (2026-06-21 입고)

이 repo의 **코드/콘텐츠를 수정하기 전에 반드시 최신화**한다:
- 작업 시작 시 `git pull origin main`.
- 이유: 원격이 자동배포/자동커밋(GitHub Pages·Vercel·구글리뷰 자동갱신 등)으로 앞서 있을 수 있어, 먼저 당기지 않으면 push가 non-fast-forward로 거부됨. (이 repo는 `reviews.yml`이 구글 리뷰를 자동 커밋함.)
- 충돌 시 머지로 정리한다.

## 사진 블로그 / 이미지 순서 규칙 (2026-06-29 입고)

`pic/`의 번호 매긴 사진을 골라 블로그 이미지로 만들 때 **순서가 밀리는 실수를 반복하지 말 것.**
- **원인:** 이 환경의 기본 셸은 **zsh(배열 1-index)**, 그런데 `bash`도 3.2라 `mapfile`이 없음. `ls | while read i=$((i+1))`로 매긴 번호와 `arr[idx-1]` 인덱싱을 섞으면 한 칸씩 밀려 **엉뚱한 사진이 저장**됨(실제로 점심 반찬 사진이 hero로 들어간 적 있음).
- **안전 패턴:** 파일 목록은 반드시 **bash glob 배열**로 만든다 (공백 파일명·정렬 안정).
  ```bash
  bash <<'EOF'
  shopt -s nullglob
  FILES=(pic/<날짜>/*.jpeg)        # 0-index, 정렬됨
  opt(){ sips -Z 1200 -s format jpeg -s formatOptions 72 "${FILES[$1]}" --out "web/blog/img/$2"; }
  opt 0 first.jpg   # FILES[0] = 첫 사진
  EOF
  ```
- **검증 필수:** 변환 후 **저장된 파일을 실제로 Read(이미지로 열어)** hero·핵심 컷이 의도한 사진인지 눈으로 확인하고, 헤드리스 크롬으로 페이지 렌더까지 본 뒤 마무리한다.
- 원본은 용량이 크므로 항상 `sips`로 가로 1200px·q72 최적화본만 `web/blog/img/`에 둔다. (`pic/`는 .gitignore 처리됨.)
- 아이 얼굴 사진: 학부모 동의는 이미 확보되어 있으므로 매번 확인하지 않고 바로 게시한다 (2026-07-07 사용자 확인). 단, 민감한 컷(우는 얼굴 등)은 알아서 제외.

## Worklog 규칙 (2026-06-21 입고)

사용자가 작업을 요청하면, **이 repo를 실제로 건드린 경우에 한해** 기록을 남긴다:
- **worklog.md** (repo 루트): 요청 내용과 결과를 1건씩 누적, 최신 항목 맨 위. 형식:
  ```
  ## YYYY-MM-DD — <한 줄 제목>
  - **요청**: <사용자 요청 원문/요지>
  - **결과**: <수행한 일과 산출물(파일/커밋 등)>
  ```
- **CLAUDE.md**: 로그는 넣지 않는다. 이 규칙(인스트럭션)만 유지. 오래 가는 결정/구조 변경 시에만 해당 섹션 갱신.
- worklog.md가 없으면 새로 만든다.
