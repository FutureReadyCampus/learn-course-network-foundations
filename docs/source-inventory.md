# Network Wiki source inventory

## Snapshot

The imported source is the Wiki revision deployed to Studio when this
migration was prepared: `d1b650e39cb0fd01f4b67adb76926172dbd517c9` (`Animate
Unit 7 to 10 flow maps`). The import is preserved under
`sources/wiki/oeweo-network/`; authored Learn-oriented Markdown lives under
`units/`. The imported materials include the original lesson Markdown, beginner
specifications, concept diagrams, and source animation SVGs. The separately
timed runtime SVGs live under `newbie/anim-paced/`.

## Unit and source mapping

| Unit | Imported section | Source lessons | Lessons |
| --- | --- | --- | ---: |
| 1 · 들어가기에 앞서... | Basic orientation and prerequisites | beginner guide materials | 4 |
| 2 · Internet 기반 네트워크 입문 | Basic items 6–8 | `lesson-05`–`lesson-07` | 3 |
| 3 · L2수준에서 외울 것들 | Basic items 9–11 | `lesson-08`–`lesson-10` | 3 |
| 4 · L3 수준에서 외울 것들 | Basic items 12–25 | `lesson-11`–`lesson-24` | 14 |
| 5 · L4 수준 대표주자 TCP와 UDP | Basic items 26–31 | `lesson-25`–`lesson-30` | 6 |
| 6 · 웹을 이루는 핵심기술 | Basic items 32–37 | `lesson-31`–`lesson-36` | 6 |
| 7 · 네트워크 장치의 구조 | Advanced lessons 1–9 | `advanced/lesson-01`–`lesson-09` | 9 |
| 8 · 인터넷 공유기 작동원리 | Advanced lessons 10–16 | `advanced/lesson-10`–`lesson-16` | 7 |
| 9 · 부하분산 시스템 작동원리 | Advanced lessons 17–18 | `advanced/lesson-17`–`lesson-18` | 2 |
| 10 · VPN과 네트워크 보안 솔루션 | Advanced lessons 19–23 | `advanced/lesson-19`–`lesson-23` | 5 |

The advanced print-material lesson 04 has no concept SVG in the source. It is
retained as a text Lesson. This import contains 59 Lessons in total; later
editorial changes should keep these source references and stable course IDs.

## Publication roles

- `main` is the reviewed Markdown source Learn is expected to import at a pinned
  commit. Learn deployment remains a separate release path.
- `stage` builds the static GitHub Pages reader for cross-device review. Pages
  output labels the exact source commit.
