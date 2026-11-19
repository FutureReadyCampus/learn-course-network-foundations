# U15 L1 어려운 용어 점검 기록

비유: Page 3 복도 문, Page 5 건물 정문 게이트는 기존 것 유지. 인증서는 U11 L6 Page 4 출입 경비 비유(신분증·도장·경비실 명단)를 이어 씀.

| 용어 | Page | 왜 어려운가 | 처방 |
| --- | --- | --- | --- |
| IPS, SIEM, 방화벽 | 1 | 견적서 장면에서 풀이 없이 나열 | ① 한 구절씩 |
| 경로 안/밖/Proxy, 패킷, Stream | 1 | 앞 Unit 전제만 있음 | ① 길목에 서 있다/길 옆에서 복사본/대신 연결, 통신 한 덩어리/대화 전체 |
| Frame, MAC 주소, Probe 센서 | 2 | 처음 나오는데 풀이 없음 | ① 한 구절씩 |
| 게이트웨이, 윗단 연결선 | 2 | 모호 | ② 밖으로 나가는 출입구 역할 장비, 스위치끼리 잇는 윗단 연결선 |
| L2 링크, 허브 | 3 | 풀이 없음 | ① 한 구절씩 |
| ARP 스푸핑 | 3 | 이름만 나옴 | ① 위조 ARP 응답을 뿌리는 공격 |
| 인증서, TLS, 평문 HTTP, 포털 | 4 | 인증서 경고의 이유가 설명 없이 나옴(U11 L6과 같은 문제) | ① 한 구절 + ③ 신분증 비유 블록 2문단 + SVG |
| 신원, 인증서, AP, VLAN | 5 | 풀이 없음 | ① 한 구절씩(인증서는 앞서 본 신분증과 이음) |
| 핫스팟 | 6 | 풀이 없음 | ① 폰이 만드는 와이파이 |

## 결과
- Page 4에 블록 추가(문단 2개), SVG `u15-l01-p04-cert-fake-server.svg`(생성기 `scripts/svg_pairs/u15_l01_terms.py`), after_paragraph 6. 기존 배치 불변.
- 퀴즈·정답·learn-page-id 불변. 802.1X, RADIUS, NAC, WIPS, 리다이렉트는 이미 풀려 있어 손대지 않음. 오탐, 단말 정책도 기존 풀이 유지.
- 검사: audit_svg_steps, build_course, test_advanced_restructure, test_glossary, audit_quiz_choice_length 통과. 금지어 0건.
