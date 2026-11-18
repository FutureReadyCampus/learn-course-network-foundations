# 상황 SVG 지침 (Unit 12~15, Page마다 하나) — 관리자 튜토리얼 판

사용자 요청(2026-11-16): Unit 11은 이야기는 좋지만 글이 많다. 글은 줄이지 않고, **각 Page의 상황(네트워크 관리자 지우의 티켓 이야기)을 SVG로도 보여 준다.** 기존 개념 SVG는 그대로 두고, 상황 SVG를 Page마다 하나씩 더한다.

## 4단계 규약
① 장면(누가·어디서) → ② 일어난 일(문제·사건) → ③ 말·걱정(말풍선, 한 단계에 하나씩) → ④ 이 Page에서 알아볼 것(`question()` 알약). 단계당 바뀌는 것 하나만 주황 테두리, 라벨은 단계당 3개 이하(이름표 제외), 글자 16px 이상.

## 지켜야 할 것
- 공통 도구 `scripts/svg_pairs/hangyeol_cast.py`(인물 `person`, 말풍선 `bubble`/`thought`, 소품 `monitor`/`chat_window`/`doc`/`alert_card`/`clock`, 배경 `office_bg`, 규약 `scene`/`new`/`mark`/`question`)와 데모 `hangyeol_cast_demo.py`를 import만 하고 수정하지 않는다. 인물 색: 지우 파랑, 박 팀장 주황 계열, 서 이사 보라, 직원 회색, 고객 청록. 강조 주황(#ffb454)은 "방금 바뀐 것"에만.
- **충실성**: 말풍선·장면은 그 Page 본문에 실제로 있는 내용만. 본문에 대사가 없으면 상황(소품·표정)과 최소한의 생각 풍선으로. 그림을 그린 뒤 본문을 다시 읽어 모든 글자가 본문으로 뒷받침되는지 확인.
- **용어**: 그 문단까지 풀이된 말이나 쉬운 말만. 주소는 `lcnf-advanced/docs/advanced-redesign/BRIEF.md`의 장부 값만.
- 개념의 작동 원리를 되풀이하지 않는다(기존 개념 SVG의 몫). 상황 SVG는 문제·질문·사람을 보여 준다.
- 장면이 없는 Page도 하나는 만든다: 그 Page의 질문을 던지는 사람(서 이사의 질문, 지우의 의문, 박 팀장의 요청)과 소품으로 구성. 새 이야기를 지어내지 않는다.

## 넣는 법
- 새 생성기 `scripts/svg_pairs/u11_l{LL}_story.py`, SVG는 해당 Lesson `assets/animations/u11-l{LL}-p{P}-story-<slug>.svg`. 기존 파일은 지우지 않는다.
- lesson.md는 front matter `page_metadata[].illustrations`에 **항목만 추가**(file, title, alt, caption, after_paragraph). 본문·퀴즈·제목·기존 그림 항목은 그대로.
- `after_paragraph`는 이야기 장면을 서술한 마지막 문단 번호(0 기반, 빈 줄로 나뉜 블록, 표 하나는 한 블록). 한 Page의 항목은 **오름차순**·범위 안. 같은 값은 빌드가 허용한다.
- alt는 4단계를 한 문장으로, 캡션은 한 줄(쉬운 말).

## 확인
새 SVG의 4단계 프레임을 모두 렌더해 PNG로 직접 보고 고친다(`python3 /tmp/svgwork/snap_l2.py <svg> <png>`; 도구가 없으면 playwright로 `data-stage-count`를 읽어 단계별 프레임을 찍는 같은 도구를 다시 만든다). `audit_svg_steps.py`, `build_course.py`, `test_advanced_restructure.py` 통과, `illustrations` 파일 존재와 `after_paragraph` 확인, 본문·퀴즈·ID가 stage와 같은지 확인. 기록은 `docs/advanced-redesign/svg-situation/u11-l{LL}.md`에 Page마다 한 줄(장면 요약 / 말풍선과 본문 근거 / `after_paragraph` / 남은 한계).

## Unit 12~15 판 추가 사항 (2026-11-17)
- 사용자 요청: "전체적으로 SVG를 (Unit 11처럼) 상황 설명용으로 더 넣어 줘." Unit 11은 이미 Page마다 상황 SVG가 있다. 이번에는 **Unit 12~15의 모든 Page**에 하나씩 넣는다. 기존 개념 SVG·본문·퀴즈·ID는 바꾸지 않는다.
- 이야기 틀은 `docs/advanced-redesign/admin-tutorial/BRIEF.md`(신입 네트워크 관리자 지우, 박 팀장=요청하는 직원, 서 이사=결정권자, 서비스 대응표·주소 장부). AI·한결디자인·디자인팀·시안·도면·쇼룸 표현을 쓰지 않는다. 서비스는 외부 클라우드 저장소, 사내 그룹웨어, 고객용 예약·문의 사이트, 공유 자료 NAS, 도쿄 지사.
- 기준 예시: Unit 11 생성기 `scripts/svg_pairs/u11_l01_story.py`와 SVG `units/07-network-devices/lessons/restructured/01-*/assets/animations/u11-l01-p0N-story-*.svg`. 지우의 역할 줄("신입 네트워크 관리자")과 박 팀장("팀장") 덮어쓰기 방식은 그 스크립트를 따른다(`hangyeol_cast.py`는 수정 금지).
- 파일 이름은 `u{UU}-l{LL}-p{P}-story-<slug>.svg`(UU=12~15), 생성기는 `scripts/svg_pairs/u{UU}_l{LL}_story.py`, 기록은 `docs/advanced-redesign/svg-situation/u{UU}-l{LL}.md`. Page 번호 P는 본문 순서(1부터).
- 본문에 장면(티켓·대화)이 없는 Page도 하나는 만든다: 그 Page의 질문을 던지는 사람(서 이사의 질문, 지우의 의문, 박 팀장의 요청)과 소품으로 구성하고 새 이야기를 지어내지 않는다.
- 공용 파일(`hangyeol_cast.py`, `kit.py`, `u1N_*common.py`, unit.md, course.yaml, 계약 JSON)과 다른 Lesson은 건드리지 않는다. lesson.md는 해당 Page `illustrations`에 항목만 추가(기존 항목·본문·퀴즈 그대로). `after_paragraph`는 이야기 장면 문단 번호이고 기존 항목과 합쳐 오름차순이어야 한다(기존 개념 그림보다 앞에 놓으려면 0 또는 더 작은 값).
- 확인: `audit_svg_steps.py`, `build_course.py --output /tmp/<lesson>.json`, `test_advanced_restructure.py`, 렌더(`python3 /tmp/svgwork/snap_l2.py <svg> <png>`)를 PNG로 직접 확인. 금지어 grep(AI|시안|디자인|도면|한결|쇼룸|GPU) 0건. 커밋 금지.
