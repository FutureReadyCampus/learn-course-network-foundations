# Unit 15 Lesson 4 초보자 용어 점검

대상: `units/15-network-security-solutions/lessons/restructured/04-경보가-쏟아지고-장애가-났다/lesson.md`

| 용어 | Page | 왜 어려운가 | 처방 |
| --- | --- | --- | --- |
| 정탐·오탐, 로그 | 1 | 풀이 없이 등장 | ① "진짜 공격에 울린 경보(정탐)/정상 통신에 잘못 울린 경보(오탐)", "로그(장비가 남기는 기록)" |
| MAC, DHCP 기록 | 1 | 앞 Unit 지식 전제 | ① 한 구절 환기 |
| SIEM·상관 분석·역추적 | 1 | 개념 자체가 추상적 | ③ 경비 기록장 3권 + 총괄 경비 담당 비유 3문단(벽시계 어긋남까지). SVG `u15-l04-p01-ledgers-siem.svg` (생성기 `scripts/svg_pairs/u15_l04_terms.py`) |
| 시각 서버, 802.1X 인증 기록 | 1 | 모호 | ① 한 구절 풀이 |
| 오픈소스 IDS 규칙, Payload, 시그니처 | 2 | 약어·전문 용어 | ① "공개 IDS 도구", "통신에 실린 내용", "찾을 특징으로 삼은 문자열" |
| 세션 한도, TLS 종료, WAF, 부하 분산 | 3 | 앞 Unit 용어 나열 | ① 한 구절 환기 |
| 리버스 프록시, 서버 풀, 미러 포트, Probe, 매개변수 | 4 | 앞 Unit 용어 | ① 한 구절 환기 |
| 오탐과 미탐 | 6 | 미탐 풀이 없음 | ① "공격인데 경보 없음" |

Page 5(우편 비유·식별자)는 이미 풀려 있어 그대로 둔다. 이 Lesson은 쉬운 편이라 고칠 곳이 적다.
Page 1 illustrations: 새 SVG를 after_paragraph 7에 추가, 퀴즈 q01은 5→8로 밀었다.

## 결과
audit_svg_steps, build_course, test_advanced_restructure, test_glossary, audit_quiz_choice_length 통과. 금지어 grep 0건. 렌더 PNG 4단계 직접 확인.
