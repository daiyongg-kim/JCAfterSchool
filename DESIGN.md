# Design System — JC After School (정철 애프터스쿨)

> "Warm Trust · Refined" — 크림 배경 + 샤프한 모서리 + 절제된 앰버 + 소프트 그림자
> 작성: 2026-05-23 · /design-consultation

## Product Context
- **What this is:** 한인 이민 가정 대상 방과후 돌봄(After School Care) + 학업 튜터링 + 성인 어학 학원의 홍보·등록 사이트
- **Who it's for:** ① 맞벌이 한인 학부모(자녀 K–12 돌봄·학습) ② 성인 이민자(IELTS·프랑스어)
- **Space/industry:** 캐나다 BC(Coquitlam, Tri-City, Surrey) 방과후·튜터링·어학
- **Project type:** 마케팅·리드 생성 사이트 (한글 기본 / 영어 옵션, i18n)
- **Memorable thing:** "안심하고 맡기고, 성적까지 챙겨주는, 동네에서 가장 믿음직한 방과후."
- **Brand equity:** 인스타 @jc_afterschool — 레드 "JC" 마크 + 일출/크림 톤, 한·영 이중 로고

## Aesthetic Direction
- **Direction:** 클린 에디토리얼 + 웜 (clean editorial + warm)
- **Decoration level:** intentional — 로고의 일출을 옅은 웜 그라데이션으로만 암시, 소프트 그림자로 깊이
- **Mood:** 정돈됐지만 따뜻한. 차가운 코퍼릿 회피, 위압적 기관 이미지 회피
- **Reference:** The Math Guru(친근·가격투명성), CECFQ(이민목적별 분기), York Region(과목×학년 IA) — `BENCHMARK.md`

## Typography
- **Display/Hero:** Pretendard 800 — 한글 우선, 신뢰의 표준
- **Body:** Pretendard 400/600
- **UI/Labels:** Pretendard (same as body)
- **English accent (선택적):** Fraunces italic — 영문 마케팅 헤드라인·섹션 라벨에만 절제 사용
- **Loading:** Pretendard `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css` · Fraunces (Google Fonts)
- **Scale (px):** hero clamp(34→52) / sec-title 30 / h3 21 / body 16 / lead 18 / small 13.5
- **Letter-spacing:** 헤딩 -.02 ~ -.03em (한글 헤딩 타이트하게)

## Color
- **Approach:** restrained — 레드는 "점"(CTA·로고·포인트)으로만, 면으로 쓰지 않음
- **Background (크림):** `#FBF8F3` · 보조 표면 `#F4EEE4`
- **Text/Headings (잉크 네이비):** `#1C2A3A` · 본문 보조 `#34465A`
- **Primary / Brand (레드):** `#D6402F` · hover `#B8331F`
- **Secondary accent (선라이즈 앰버):** `#E8A33D` — 아주 절제 (불릿·일출·글로우만)
- **Neutral (웜 그레이):** `#8A8178` · 보더 `#E7DFD3`
- **Semantic:** success `#2E8B57` / warning `#E8A33D` / error `#D6402F` / info `#34465A`
- **Dark mode:** 추후 — 네이비를 표면으로, 크림 텍스트, 채도 10–20% 감소

## Spacing
- **Base unit:** 8px
- **Density:** comfortable~spacious (깔끔 = 넉넉한 여백)
- **Section padding:** 72px (모바일 축소)
- **Scale:** 2xs(2) xs(4) sm(8) md(16) lg(24) xl(32) 2xl(48) 3xl(72)

## Layout
- **Approach:** hybrid — 정돈된 그리드 + 실제 사진 주도 히어로
- **Grid:** 히어로 1.05fr/.95fr, 카드 3열(태블릿 2열, 모바일 1열)
- **Max content width:** 1140px
- **Border radius (샤프):** sm 6px / md 8px / lg 12px / button 8px (pill 사용 안 함)
- **Shadows (소프트):** sm `0 10px 26px -16px rgba(28,42,58,.30)` / md `0 20px 50px -28px rgba(28,42,58,.42)` / lg `0 34px 72px -34px rgba(28,42,58,.5)`

## Motion
- **Approach:** minimal-functional + 부드러운 페이드인
- **Easing:** enter(ease-out) exit(ease-in) move(ease-in-out)
- **Duration:** micro(50-100ms) short(150-250ms) medium(250-400ms)
- **Hover:** 카드 translateY(-3px) + 그림자 강화, 버튼 translateY(-1px)

## Key Components (구현 기준)
- **CTA 버튼:** 레드 배경 + 소프트 레드 그림자, 모서리 8px. 메인 = "무료 체험 신청"
- **Eyebrow 칩:** 흰 배경 + 보더 + 앰버 닷 + 소프트 그림자
- **차별화 스트립:** 네이비 배경 박스, 🚌픽업 🏠돌봄 🍪간식 📈성적 4칸
- **프로그램 카드:** 흰 카드 + 1px 보더 + 소프트 그림자, 간판(방과후 돌봄)은 크림 강조
- **CTA 밴드:** 네이비 + 앰버 글로우
- **파비콘/앱 아이콘:** 헤더 `.mark`와 동일 — 레드 `#D6402F` 라운드 스퀘어(radius 20%) + 흰 "JC" 세리프.
  에셋: `web/favicon.ico`(16·32·48) · `img/favicon-16|32.png` · `img/apple-touch-icon.png`(180, iOS가 모서리를 깎으므로 풀블리드 정사각) · `img/icon-192|512.png` · `site.webmanifest`(theme-color `#D6402F`).
  Fraunces가 시스템에 없어 렌더링은 CSS 폴백과 동일한 **Georgia Bold**로 생성함. 재생성 시 동일 폰트 유지.
- **언어 토글:** 한국어(기본) · EN (세그먼트 컨트롤)
- **메인 CTA:** "무료 체험 신청" — 전 트랙 통일, 카카오톡 연결(`open.kakao.com`)
- **요금:** 사이트 비공개 (경쟁 학원 가격경쟁 회피). 네비 "문의"로 카톡 상담 유도

## Reference Implementation
- `web/index.html` — **Pretext-native 프로덕션 HTML** (/design-html, 헤드라인 리플로우 + contenteditable + 접근성). 의존성: `web/pretext.js`(인라인 번들). 다크모드 미사용 — 항상 크림 final 디자인 고정
- 디자인 시스템 정의·변형 비교: `~/.gstack/projects/JCAfterSchool/designs/`

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-05-23 | 초기 디자인 시스템 "Warm Trust · Refined" 확정 | /design-consultation. 사용자가 A 기반에 B(샤프 모서리)·C(소프트 그림자) 조합 |
| 2026-05-23 | 레드를 면이 아닌 포인트로 제한 | "깔끔하고 신뢰가는" 목표 — 레드 플러드는 학원 전단지처럼 시끄러움 |
| 2026-05-23 | 차가운 흰색 대신 크림 배경 | 돌봄 브랜드의 가족 같은 따뜻함, 인스타 일출 톤 계승 |
| 2026-05-23 | Pretendard 단일 본문 폰트 | 한글 기본 사이트의 신뢰 표준, 통일성 |
| 2026-05-23 | 요금 사이트 비공개 | 근처 경쟁 학원과 가격경쟁(제살 깎기) 회피. 인스타/카톡 안내 |
| 2026-05-23 | 1차 CTA "무료 체험 신청" 전 트랙 통일 | 성인 트랙 레벨테스트 분기 폐기, 단일 메시지로 단순화 |
| 2026-05-23 | /design-html로 Pretext-native HTML 생성 | 헤드라인 리플로우·contenteditable·다크모드·접근성. `web/index.html` |
