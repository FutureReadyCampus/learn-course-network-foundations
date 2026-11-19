# Unit 12 Lesson 5 초보자 용어 점검

대상: `units/08-router-and-nat/lessons/restructured/05-포트를-안-열어도-되는-nat-통과/lesson.md`

| 용어 | Page | 왜 어려운가 | 처방 |
| --- | --- | --- | --- |
| 행(변환표) | 1 | 앞 Lesson 지식 전제 | ① "안쪽에서 먼저 나간 통신의 기록" 한 구절 |
| Port Restricted | 2 | 메모에 풀이 없이 등장 | ① 옛 분류 이름이고 뒤 Page에서 풀어 읽는다고 안내 |
| External 칸 | 2 | 변환표 용어 | ① "바깥에 보이는 주소·포트를 적는 칸" |
| UDP | 3 | 처음 나옴 | ① 속도가 중요한 통신에 쓰는 전송 방식 |
| EIF·ADF·APDF | 4 | 약칭이 표에 풀이 없이 등장 | ① 영어 약칭이며 외우지 않아도 된다고 안내 |
| 원격지 제한 없는 포워딩 | 4 | 앞 Lesson 용어 | ① "어느 출발지든 들여보내는 규칙" |
| 매핑이 살아 있다 / 구현 | 4 | 추상적 표현 | ② "변환표에 행이 남아 있는 동안", "만든 방식" |
| STUN | 5 | 프로토콜 이름만 제시 | ① "내 바깥 주소가 어떻게 보이는지 알려 주는 서버와 주고받는 규칙" |
| Symmetric 필터링 "상대와 연관된 조건" | 5 | 모호 | ② "(보낸 그 상대만)" |
| 홀 펀칭 | 6 | 개념 자체가 어렵고 비유가 둘로 갈림(안내 데스크 vs 소개해 준 친구) | ③ 안내 데스크·장부 비유 3문단을 끝까지 이어 씀, "소개해 준 친구" 문단은 데스크 비유로 통일. SVG `u12-l05-p06c-desk-ledger.svg` (생성기 `scripts/svg_pairs/u12_l05_terms.py`) |
| TCP/TLS(443) | 7 | 약어 나열 | ① "웹 접속과 같은 443번 포트의 TCP/TLS(암호화된 연결)로 감싸서" |

Page 1(P2P·피어·소개 서버)과 Page 7의 통신사 NAT·교환원 비유는 이미 풀이가 있어 그대로 둔다.
Page 6 illustrations: 새 SVG를 after_paragraph 3에 추가, 기존 항목과 퀴즈 배치는 본문이 3문단 늘어난 만큼 뒤로 밀었다(2→5, 3→6, 퀴즈 3→6).

## 결과
audit_svg_steps, build_course, test_advanced_restructure(21), test_glossary(18), audit_quiz_choice_length 모두 통과. 금지어 grep 0건. 렌더 PNG 4단계 직접 확인.
