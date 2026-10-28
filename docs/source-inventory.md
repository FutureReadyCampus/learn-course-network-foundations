# Unit 1 source inventory

- Source repository: `course-network`
- Source checkout at import: `90a5cc40dec981b0e37fa334f3fae8ba673c8f32`
- Wiki path: `studio/wiki/oeweo-network/`
- Course structure follows `catalog.json`, Unit 1: `기초편 1. 들어가기에 앞서...`.
- Learn lessons use Wiki `lesson-01.md` through `lesson-04.md` reading-edition sections, which correspond to catalog items 2–5. Catalog item 1 remains the Unit introduction.
- Beginner-guide additions use `newbie/specs/lesson-01.json` through `lesson-04.json`; relevant SVGs from both `concepts/` and `newbie/anim/` are included and linked to matching pages.
- The source Markdown and beginner-guide lesson-02 through lesson-04 JSON/SVGs were uncommitted in the source checkout at import time. Their copied versions are preserved here. The exact imported files are recorded by paths under `sources/wiki/oeweo-network/`.
- Unit 2–10 are catalog placeholders only; their lesson source has not been imported yet.

## 왕초보 가이드 SVG 추가 보존

2026-10-28에 Course Studio checkout `course-network`의 당시 HEAD `90a5cc40dec981b0e37fa334f3fae8ba673c8f32`에서 왕초보 길잡이 원본 36 JSON과 89 SVG를 복사했다. 원본 파일은 `sources/wiki/oeweo-network/newbie/specs/`와 `sources/wiki/oeweo-network/newbie/anim/`에 유지한다. 당시 원본 checkout에는 미커밋 파일이 포함되어 있었으므로 이 목록은 원본 경로와 파일 내용의 보존 기록이며, upstream 커밋 이력으로 간주하지 않는다.

원본 SVG는 수정하지 않았다. 초기 검토용 일괄 0.3× 파생본은 `anim-slow-0.3x/`에 보존한다. 시각 검토 후 실제 Learn 표시본은 도해별 복잡도에 따라 10–18초로 조정해 `anim-paced/`에 생성한다. 개별 시간표는 [svg-playback.yaml](svg-playback.yaml)에 둔다. Lesson 01에 추가로 만든 초보자용 도해는 `units/01-before-networking/animations/`에 둔다. 실제 Lesson별 원본 그림 대응은 [newbie-asset-map.md](newbie-asset-map.md)를 참조한다.

현재 후보에서 Learn Lesson으로 연결된 Wiki 수업은 Unit 1의 첫 네 Lesson뿐이다. 나머지 원본 SVG와 JSON은 보존·분류되어 있으나 아직 학습 화면에 연결된 것은 아니다.
