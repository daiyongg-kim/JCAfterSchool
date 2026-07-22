# Worklog — JCAfterSchool

요청 내역과 결과 기록. 최신 항목이 맨 위. 규칙은 CLAUDE.md "Worklog 규칙" 참조.

## 2026-07-21 — 7월 17일·20일 블로그 본문 영문화
- **요청**: 7월 17일과 20일 블로그는 제목과 무관하게 내용을 영어로 변경.
- **결과**: 두 게시물의 본문, 섹션 보조 제목, 사진·영상 캡션, 요약 카드와 CTA 등 실제 콘텐츠를 자연스러운 영어로 전환. 제목과 브랜드명은 유지.

## 2026-07-21 — 여름캠프 4주차 1일차(Grammar Jeopardy·공원·피아노·화단 돌보기) 블로그
- **요청**: `pic/20260720/`의 어제 사진과 영상을 기존 블로그 및 `CLAUDE.md` 방식에 맞춰 새 블로그로 제작.
- **결과**: 사진 59장과 영상 2개를 검토해 21장·영상 2개를 선별 및 최적화하고 `web/blog/camp-wk4day1-2026-07-20.html`을 제작. Grammar Jeopardy(질문어·접미사·어근·과거시제), 공원 놀이, 짜파게티 점심, 질문 카드, 피아노, 팝콘·공 균형 게임, 화단 돌보기 순으로 구성했으며 블로그 인덱스와 사이트맵에 추가.

## 2026-07-17 — 여름캠프 3주차 5일차(What Happened?·질문으로 완성한 미니 이야기북) 블로그
- **요청**: `pic/20260717/` 사진 + memo.txt(다이엔 글: 금요일에 어휘·문법·철자·묻고답하기 소통을 다지는 여러 문학 활동·최종 프로젝트는 여섯 질문 각 1페이지 + "What happened?" 창의 답으로 만든 미니 북·큰 아이들은 따옴표/간접화법 문법 워크시트 후 완결된 이야기 책쓰기·월요일에 마저 완성) 반영해 어제자 블로그 포스팅.
- **결과**:
  - 사진 42장 전부 프리뷰로 검토, 35장 선별·최적화(`web/blog/img/camp-wk3day5-0717-*.jpg`). hero=아이들이 Who/What/Where/When/Why/How 문장 그리드 들고 벽 앞에 앉은 컷(FILES[30]). `grammar-write`가 처음 8진수(`09`) 오류+인덱스 혼동으로 배식 컷으로 잘못 들어간 것 발견해 FILES[8](남학생 글쓰기)로 교정, hero·cook-curry·grammar-write 저장본 Read로 검증.
  - 신규 `web/blog/camp-wk3day5-2026-07-17.html` — 구성: hero / 🗯️The Big Six 벽 차트 6종(한글 병기) / 📋Build a Sentence 여섯칸 문장 그리드 / 🖊️"What Happened?" 화이트보드 이야기판 / 📖The Mini Booklet 최종 프로젝트 + 다이엔 메시지 카드 / 📝큰 아이들 따옴표·간접화법·시제표·형누나 도움 / 🫐블루베리+마녀 손가락 간식 / 🍛카레떡볶이+고로케 점심 / 그룹 셀피 / 오늘의 배움(월요일 완성 예정) notice / Thought of the day. h1만 한글, 본문 영어.
  - `web/blog/index.html` 카드 최상단 추가, `web/sitemap.xml` URL 추가. 이미지 전부 1200px·q72, 헤드리스 크롬 전체 렌더 확인.

## 2026-07-16 — 여름캠프 3주차 4일차(Who/What/Where/When/Why/How 질문의 문법) 블로그
- **요청**: `pic/20260716/` 사진 + memo.txt(다이엔 글: 오늘 주제는 Who?What?Where?When?Why?How? 질문하고 답하는 문법·민우가 다시 티처 어시스턴트로 딕테이션 읽어주면 학생들이 질문 유형 체크·학생이 유형 고르면 민우가 그 유형으로 질문·레벨+1 워크시트·말풍선으로 직접 만든 그림 대화·큰 아이들은 각자 언어 니즈에 맞춘 보강 워크시트·블루베리+팝콘 간식 빼고 점심까지 열공) 반영해 오늘자 블로그 포스팅.
- **결과**:
  - 사진 67장 검토, 28장 선별·최적화(`web/blog/img/camp-wk3day4-0716-*.jpg`). hero=Sua가 말풍선 가득한 "Questions" 포스터 든 컷(11). 저장본 전부 Read로 검증 — `lunch-happy`가 말 동상 컷으로 잘못 들어간 것 발견해 [64]로 교정. 작업 중 cwd가 `web/`로 바뀌어 glob이 빈 배열이 된 케이스도 nullglob 경고로 잡고 절대경로로 수정.
  - 신규 `web/blog/camp-wk3day4-2026-07-16.html` — 구성: hero / ✍️Warm-Up 민우 딕테이션·벽 차트 체크 / 질문 6종 차트 갤러리(What·Where·When·Why·How·전체, 한글 병기) + Answer of the day("How?"→"With a hug.") / 📄Level Plus One 워크시트(민우 보강 컷 포함) / 🗯️Make Your Own 그림 대화(말풍선 그리기·"Who will play with me?" 토끼·Panda and Rabbit Sharing·Jua Cho 만화·달력 대화) / 🍿팝콘+블루베리 간식 / 🌳공원(집라인·강아지·말 동상) / 🍚김치볶음밥+김 점심 / 오늘의 배움 notice / Thought of the day. h1만 한글, 본문 영어.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가. 이미지 전부 최적화(1200px·q72), 헤드리스 크롬 전체 렌더 확인.

## 2026-07-15 — 여름캠프 3주차 3일차(주니어 티처 데이 3일차·코치 민우 축구 수학) 블로그
- **요청**: `pic/20260715/` 사진 + memo.txt(다이엔 글: 민우가 오전 내내 축구 테마 수학 수업 진행·"Would You Rather" 워밍업·"soccer ball" 행맨·원하는 만큼 워크시트 풀기·민우와 다이엔이 별점 채점·Leah 15장 중 13장 완주·팝콘+직접 만든 포도/블루베리 젤리·"grapes or blueberries?" 질문·젤리는 점심때 굳어 불고기 점심 다 먹고 먹음) 반영해 오늘자 블로그 포스팅.
- **결과**:
  - memo가 `:wq!` 파일명으로 저장돼 있던 것 확인·판독. 사진 47장 검토, 20장 선별·최적화(`web/blog/img/camp-wk3day3-0715-*.jpg`). hero=민우가 자기 "Keep Playing Soccer/MINWOO" 포스터 가리키며 축구공 든 컷(05). Leah가 별점 가득한 "Odd & Even Soccer" 워크시트 든 자랑 컷(16), 젤리 컵 그룹샷(33) 등 실제 Read로 검증.
  - 신규 `web/blog/camp-wk3day3-2026-07-15.html` — 구성: hero / ⚽Coach Minwoo 워밍업·행맨(포스터 디테일 포함) / 🧮Pick Your Challenge 축구 수학 워크시트(민우·다이엔 1:1 지도·별점 채점·Goal 협업·워드서치·이름쓰기) / 🌟Star of the Day Leah 13/15 인내상 / 📄워크시트 샘플 갤러리 4종(2자리 뺄셈·Goal·합=25 찾기·축구공 기하) / 🍇팝콘+직접 만든 포도·블루베리 젤리(굳는 데 시간→불고기 점심 완식 notice) / Question of the day(grapes or blueberries?) / Thought of the day(민우 리더십 칭찬). h1만 한글, 본문 영어.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가. 이미지 전부 최적화(1200px·q72), 헤드리스 크롬 전체 렌더 확인.

## 2026-07-14 — 여름캠프 3주차 2일차(주니어 티처 데이 2일차·새/버블티 발표) 블로그
- **요청**: `pic/20260714/` 사진 + memo.txt(블루베리 간식 / Sua 새 수업 첫 발표 / Jua·Loha 버블티 수업 / "teaching takes learning to another level") 반영해 오늘자 블로그 포스팅.
- **결과**:
  - 사진 49장 검토, 20장 선별·최적화(`web/blog/img/camp-wk3day2-0714-*.jpg`). 첫 hero 후보(00)가 고양이 포스터를 가리켜 새 수업용으로 부적절 → 새 포스터 가리키는 컷(02, 포스터에 "Sua" 서명 확인)으로 교체, 00은 birds-confident로 재활용. 공원 컷은 기울어진 프레임(47) 대신 upright 프레임(48)으로 교체.
  - 신규 `web/blog/camp-wk3day2-2026-07-14.html` — 구성: hero(Teacher Sua & Cute Birds 보드) / 🫐블루베리 간식 / 🐦Teacher Sua "All About Birds"(포인터 강의·워크시트 배부·1:1 지도·채점·Parrots/Let's Learn About Birds 워크시트·하이파이브) / 🧋Teachers Jua & Loha "Bubble Tea"(Boba Core Components·#Boba Girl·Ms.Rose·버블티 math·booklet·별점) / 🍿오후 팝콘 간식 / ☀️플로어 놀이 + 스플래시 파크 물놀이. Thought-of-the-day 카드(memo 인용). h1만 한글, 본문 영어.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가. 이미지 20장 전부 Read 검증 + 헤드리스 크롬 전체 렌더 확인.

## 2026-07-13 — 여름캠프 3주차 1일차(주니어 티처 데이·인터랙티브 발표) 블로그
- **요청**: `pic/20260713/` 사진 + memo.txt(Diane 코멘트: Leah 쥐·SueAh 토끼·Loha·Chloe 갸루, 블루마운틴 파크 필드트립 예고) 반영해 오늘자 블로그 포스팅.
- **결과**:
  - 사진 44장 검토, 18장 선별·최적화(`web/blog/img/camp-wk3day1-0713-*.jpg`).
  - 신규 `web/blog/camp-wk3day1-2026-07-13.html` — 구성: 🎤주니어 티처 데이(hero: Leah & Mouse Family 보드) / 🐭Teacher Leah "Cute Mice"(포인터 강의·1:1 지도·채점·Parts of a Mouse 워크시트) / 🐰Teacher SueAh "Bunnies"(토끼 인형 조교) / 🐱Teacher Loha(첫 발표·고양이 워크시트·최종 과제 수합) / 🎀Junior Teacher Chloe 갸루 발표+페이퍼돌 / 🍱돈까스 점심 / ☀️공원 오후 + 블루마운틴 파크 필드트립 예고 배너. Leah 명언 카드("I would rather be a teacher than a student."). h1만 한글, 본문 영어.
  - `web/blog/index.html` 카드 추가, `web/sitemap.xml` URL 추가. 이미지 Read 검증 + 헤드리스 크롬 렌더 확인.

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
