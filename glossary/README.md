# glossary

본문에서 하이라이트할 용어 목록(`terms.yaml`). 설계와 결정은 이슈 #76, 적용은 #95(시범)·#94(stage 화면).
원고에는 이모지·호버를 넣지 않고, 화면이 이 파일을 읽어 렌더링 시점에 붙인다.

| 필드 | 설명 |
| --- | --- |
| `id` | 영문 소문자 slug. 고유. |
| `tier` | `hero`(이모지 있음) · `family`(주인공의 가족, 부모 이모지 상속) · `none`(호버만) |
| `category` | hero 전용. 등장인물·표식·물건·장소·약속·동작과 값 |
| `emoji` | hero 전용. ZWJ 금지, 과정 전체에서 중복 금지 |
| `parent` | family 전용. hero 용어 id |
| `ko`, `en` | 표기. 본문은 「한글(영어)」 |
| `aliases` | 본문 매칭용 표기. 낱개로 쓴다. 대소문자만 다른 중복은 쓰지 않는다 |
| `hover` | 호버 설명 한두 문장 |
| `anchor` | 정의 Page: `{lesson: <Lesson id>, page: <Page ID>}`. Page ID는 원고의 `<!-- learn-page-id: ... -->` |
| `anchor_hint` | 아직 Page ID 표식이 없는 용어의 임시 위치. 가능하면 `anchor`로 바꾼다 |
| `only_in`, `not_in` | 적용하거나 제외할 Lesson id 목록 |

검사는 `scripts/build_course.py`가 한다(id·이모지 중복, parent, anchor 존재, 별칭 충돌).
보류: `osi`, `tcpip`는 정의 Page가 한 곳이 아니라 Unit 1 정리(#65) 뒤에 확정한다.
