---
id: m5-u04-l09
title: 응용 4-5 · 평가 기준 자동 점검과 점검 목록
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/132_day05_pm_risk_check.md
  mission_id: GichanSource.m5-1113-pm-risk-check
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 응용 4-5 · 평가 기준 자동 점검과 점검 목록

## 목표: Unit 4 점검 프로그램

> **여유가 되면 해 보세요.** 핵심 실습 4-1 · 4-2와 글쓰기를 먼저 마칩니다. 이 응용은 실습 4-1 · 4-2 의 파일과 응용 4-3 의 결과물을 함께 점검합니다. 응용 4-3 을 하지 않았다면 다음 페이지 「2.1 기대 결과와 실제 결과 비교」의 「준비할 파일」대로 만들면 됩니다.

> **오늘 들어온 일**
>
> - **상황**: <mark style="background:#e0d4ff">이 Unit 에서 리포트 · 승인 게이트 · 오탐 복구를 따로 구현하고</mark> 하나씩 실행해 출력을 사람이 읽어 검증했습니다(수동 검증). 이 과정에서 정한 Unit 4 평가 기준은 <mark style="background:#ffdcb0">① 근무 데이터가 리포트에 빠짐없이 들어갔는가 ② 위험에 따라 자동 · 승인이 맞게 나뉘는가 ③ 오탐 복구가 신속하고 완전한가</mark>, 세 가지입니다. 오늘 점검 프로그램은 ①을 「티켓 번호와 티켓 없는 조치의 인시던트 번호가 리포트에 들어 있는가」로 판정합니다.
> - **문제**: 출력을 사람이 읽는 수동 검증만으로는 승인 기준 숫자를 바꾸거나 리포트 틀을 고친 뒤에 <mark style="background:#ffc4d6">무엇이 달라졌는지 놓치기 쉽습니다.</mark> 예를 들어 <mark style="background:#ffdcb0">승인 기준을 3점에서 4점으로 올리면</mark> `REQ-5`(함께 쓰는 IP, 3점)의 결정이 승인 필요에서 「자동」으로 바뀌는데, 출력 8줄을 다시 읽어야 알 수 있습니다. 변경 뒤에는 같은 점검을 다시 실행해 결과를 비교하는 방법이 필요합니다.
> - **부탁**: 세 기준을 한 번에 검증하는 점검 프로그램을 만들어 주세요. 승인 게이트는 <mark>기대한 결정(기대 결과)을 미리 적어 둔 시험 사례 7개로 검증해 주세요.</mark>
> - **바뀌는 점**: 실행 한 번으로 점검 목록 `unit09_checklist.md` 5줄이 생성되고, 오늘 샘플에서는 <mark style="background:#bde3ff">세 기준이 모두 「통과」</mark>입니다. 기준을 지키지 못하면 <mark style="background:#ffc4d6">「확인 필요」와 문제 문장</mark>이 나옵니다. 상황과 숫자는 설명을 위한 예시입니다.

## 2.1 기대 결과와 실제 결과 비교

| 기준 | 기대한 결과(미리 적어 둔 것) | 실제 결과 | 불일치로 남기는 것(문제 목록) |
|---|---|---|---|
| ① 리포트 반영 | 티켓 번호 7개 + 티켓 없는 조치의 인시던트 번호 1개 | <mark style="background:#e0d4ff">응용 4-3 에서 만드는 `incident_report_20261112.md`</mark> 의 본문 | 리포트에 없는 번호 (1 · 2번) |
| ② 자동 · 승인 분기 | `gate_cases.json` 의 사례마다 기대한 결정 | <mark style="background:#e0d4ff">실습 4-1 의 `decide_gate`</mark> 의 결정 | 기대와 다른 사례 (3 · 4번) |
| ③ 오탐 복구 | <mark style="background:#ffdcb0">남은 대상 0개 · 30분 안</mark> · 정탐(진짜 공격) 계정 `dami` 는 잠김 유지 | <mark style="background:#e0d4ff">실습 4-2 의 `handle_false_positive`</mark> 의 결과와 처리 뒤 상태 | 복구 안 된 대상 · 시간 초과(5번) · 잠금이 풀린 정탐 계정(6 · 7번) |

오늘 쓰는 시험 용어는 아래와 같습니다.

| 용어 | 뜻 |
|---|---|
| **시험 사례**(test case, 테스트 케이스) | 입력과 기대한 결과를 짝지어 적어 둔 것 |
| **경계값 분석**(boundary value analysis, 바운더리 밸류 애널리시스) | 기준 숫자 바로 앞뒤의 값, 즉 경계값으로 시험 사례를 만드는 방법 |
| 경계 조건 오류(off-by-one error) | 기준 숫자를 하나 잘못 포함하거나 빠뜨리는 오류 |
| **회귀 시험**(regression test, 리그레션 테스트) | 변경 뒤에 기존에 되던 것이 깨지지 않았는지 다시 확인하는 시험 |

- 시험 사례는 경계값 분석에 따라 경계의 양쪽을 꼭 포함합니다. 오늘은 대상 3개(1점, 자동)와 대상 4개(3점, 승인 필요)를 함께 포함해 <mark style="background:#ffdcb0">「4개 이상」 경계</mark>를 검증합니다. 경계에서는 `>` 를 `>=` 로 잘못 쓰는 경계 조건 오류가 가장 잘 드러나기 때문입니다.
- 리포트 점검은 번호 문자열이 리포트 본문 안에 포함되어 있는지(`in`)로 판정합니다. 번호의 포함 여부만 검사하고, <mark style="background:#ffc4d6">줄의 모양(형식)은 검사하지 않습니다.</mark>
- 오탐 복구 점검은 <mark style="background:#e0d4ff">실습 4-2 와 같은 입력으로 다시 처리한 결과</mark>를 대상으로 합니다. 같은 입력이면 같은 결과가 나오므로(재현성) 실습 4-2 출력과 같은 결과가 나와야 합니다.
- 기준 숫자나 코드를 바꾼 뒤 같은 점검을 다시 실행해, 이전에 맞던 결과가 그대로 맞는지 확인하는 방식이 회귀 시험입니다. 오늘의 점검 프로그램은 이 회귀 시험으로 쓸 수 있습니다.

**준비할 파일** — 점검 프로그램은 아래 파일을 읽거나 불러 씁니다. 모두 `soar_response` 폴더에 있어야 합니다.

| 묶음 | 파일 | 없을 때 볼 곳 |
|---|---|---|
| 실습 4-1 · 4-2 파일 | `approval_gate.py` · `config/approval_policy.json` · `false_positive.py` · `fp_state.json` · `fp_log.json` · `fp_reports.json` | |
| Unit 2 · 3 파일 | `false_positive.py` 가 불러 쓰는 `rollback.py` 등 | 「시작하기」 레슨에서 확인 |
| 응용 4-3 파일 | `report.py` | 「선택 과제용 에스컬레이션·리포트 함수 준비」 레슨의 완성본 |
| 응용 4-3 파일 | `unit10_tickets.json` · `unit10_actions.json` | 응용 4-3 레슨의 코드 상자 |
| 리포트 파일 | `incident_report_20261112.md` | 아래 내용으로 직접 만듦 |

리포트 파일은 응용 4-3 의 `apply4-3_run.py` 를 실행하면 생깁니다. 응용 4-3 을 하지 않았다면 아래 내용으로 직접 만듭니다. 응용 4-3 을 정답대로 실행했을 때 저장되는 파일과 내용이 같습니다(32줄).

<h2><code>incident_report_20261112.md</code></h2>

응용 4-3 이 만드는 초동 대응 리포트입니다.

<pre class="copyable"><code>&#35; 초동 대응 리포트 — 2026-11-12(목) 오전 근무

&#35;# 1. 티켓별 초동 대응
- TCK-1 [high] dami — 퇴사한 계정 · 상태 해결 · 조치 기록 4건
- TCK-2 [low] 198.51.100.90 — 경로 스캔 · 상태 열림 · 조치 기록 2건
- TCK-3 [mid] gaeun — 규칙은 허용인데 서버가 거절 · 상태 해결 · 조치 기록 0건
- TCK-4 [mid] seoyeon — 대량 다운로드 · 상태 확인 중 · 조치 기록 0건
- TCK-5 [low] 203.0.113.250 — 경로 스캔 · 상태 열림 · 조치 기록 1건
- TCK-6 [mid] hana — 업무 시간 밖 로그인 · 상태 해결 · 조치 기록 0건
- TCK-7 [high] dami — 퇴사한 계정 · 상태 확인 중 · 조치 기록 2건

&#35;# 2. 규칙별 티켓 수
- 퇴사한 계정: 2장
- 경로 스캔: 2장
- 규칙은 허용인데 서버가 거절: 1장
- 대량 다운로드: 1장
- 업무 시간 밖 로그인: 1장

&#35;# 3. 등급별 평균 확인 시간(분)
- high: 10.0분
- mid: 85.0분

&#35;# 4. 응답 기한을 넘겨 확인한 티켓
- TCK-3 · 기한 68분 · 확인 80분
- TCK-4 · 기한 72분 · 확인 140분

&#35;# 5. 티켓이 없는 조치 (사람이 티켓을 만들어야 함)
- INC-212 · 계정 잠금 · yuna

&#35;# 6. 높음(high) 티켓의 처리 경위
- TCK-1 · dami: 0분 티켓 생성 → 10분 담당자 확인 → 45분 해결
- TCK-7 · dami: 95분 티켓 생성 → 105분 담당자 확인
</code></pre>

<h2><code>gate_cases.json</code></h2>

승인 게이트 시험 사례 7개입니다. `case` 는 사례 이름, `expected` 는 기대한 결정(기대 결과), `request` 는 <mark style="background:#e0d4ff">실습 4-1 요청</mark>에서 `incident` 만 뺀 형식의 조치 요청입니다.

<pre class="copyable"><code>[
  {"case": "high 등급 한 명", "expected": "자동", "request": {"id": "T-1", "action": "계정 잠금", "target": "dami", "grade": "high", "users_on_ip": 0, "target_count": 1}},
  {"case": "VIP 계정", "expected": "승인 필요", "request": {"id": "T-2", "action": "계정 잠금", "target": "gaeun", "grade": "low", "users_on_ip": 0, "target_count": 1}},
  {"case": "함께 쓰는 IP", "expected": "승인 필요", "request": {"id": "T-3", "action": "IP 차단", "target": "198.51.100.77", "grade": "mid", "users_on_ip": 2, "target_count": 1}},
  {"case": "대상 4개", "expected": "승인 필요", "request": {"id": "T-4", "action": "계정 잠금", "target": "minsu", "grade": "mid", "users_on_ip": 0, "target_count": 4}},
  {"case": "대상 3개", "expected": "자동", "request": {"id": "T-5", "action": "계정 잠금", "target": "minsu", "grade": "mid", "users_on_ip": 0, "target_count": 3}},
  {"case": "허용 목록 IP", "expected": "차단 금지", "request": {"id": "T-6", "action": "IP 차단", "target": "203.0.113.80", "grade": "high", "users_on_ip": 4, "target_count": 1}},
  {"case": "점검 서버", "expected": "차단 금지", "request": {"id": "T-7", "action": "IP 차단", "target": "192.0.2.10", "grade": "low", "users_on_ip": 0, "target_count": 1}}
]
</code></pre>

함수 네 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
unit09_check.py   check_report    : 있어야 할 번호가 리포트에 없으면 (1번) 추가한다 (2번)
                check_gate      : 사례마다 결정을 받아 (3번) 기대와 다르면 (4번) 남긴다
                check_recovery  : 시간 안에 끝나지 않았거나 (5번) 진짜 공격 계정이 풀렸으면 (6 · 7번) 남긴다
                mark            : 문제가 없으면 「통과」, 있으면 「확인 필요」를 리턴한다 (미리 채움)
실행 파일       apply4-5_run.py : 리포트 점검 결과 (8번) · 오탐 복구 점검 결과 (9번)를 받아 점검 목록을 쓴다
```

<!-- checklist optional -->
- [ ] 「준비할 파일」 표의 파일이 `soar_response` 폴더에 모두 있다(응용 4-3 을 하지 않았으면 `incident_report_20261112.md` 를 위 상자로 만들어 저장했다)
<!-- /checklist -->

## 응용 4-5 · 평가 기준 자동 점검과 점검 목록

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>리포트 · 승인 게이트 · 오탐 복구가 기준을 충족하는지 사람이 출력을 하나씩 읽어 수동으로 검증합니다</mark>.
- **만드는 것**: 리포트 반영 · 승인 게이트 분기 · 오탐 복구 점검 함수(`unit09_check.py`), 점검 목록 출력과 저장(`apply4-5_run.py`).
- **실행하면**: <mark style="background:#bde3ff">단계 1: 점검 재료의 수, 단계 2: 기준마다 「통과」 또는 「확인 필요」와 문제 수, 단계 3: 저장한 점검 목록이 나옵니다.</mark>

**할 일**: `soar_response` 폴더에 데이터 파일 하나(`gate_cases.json`)와 코드 파일 두 개(`unit09_check.py` · `apply4-5_run.py`)를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 를 읽습니다.

<h3><code>unit09_check.py</code></h3>

점검 함수 모음입니다. 직접 쓰는 곳은 1 ~ 7번입니다. 파일 이름 속 `unit09` 는 원래 자료의 번호라서, Unit 4 와 숫자가 달라도 바꾸지 않고 그대로 씁니다(`unit09_checklist.md` 도 같습니다).

- 4번과 5번은 `if` 한 줄만 씁니다. 그 아래 미리 채운 `append` 줄이 `if` 안쪽입니다.

```python exercise
from report import find_missing_incidents                        # 응용 4-3 의 티켓 없는 조치 찾기 함수를 불러온다
from approval_gate import decide_gate                            # 실습 4-1 의 승인 게이트 함수를 불러온다


def check_report(report_text, tickets, actions):                 # 리포트 문자열 · 티켓 리스트 · 조치 기록 리스트를 받는 함수
    """리포트에 들어 있어야 할 티켓 번호와 티켓 없는 조치의 인시던트 번호 가운데, 리포트에 없는 번호를 리스트로 리턴한다.
    고객사에 리포트를 보내기 전에 근무 데이터가 빠짐없이 들어갔는지 확인할 때 쓴다.
    """
    expected = []                                                # 리포트에 있어야 할 번호를 모을 빈 리스트 — 미리 채운 줄
    for ticket in tickets:                                       # 티켓을 하나씩 꺼낸다 — 미리 채운 줄
        expected.append(ticket["id"])                            # 티켓 번호를 추가한다 — 미리 채운 줄
    for action in find_missing_incidents(actions, tickets):      # 티켓이 없는 조치를 하나씩 꺼낸다 — 미리 채운 줄
        expected.append(action["incident"])                      # 그 인시던트 번호를 추가한다 — 미리 채운 줄
    not_found = []                                               # 리포트에 없는 번호를 모을 빈 리스트 — 미리 채운 줄
    for number in expected:                                      # 있어야 할 번호를 하나씩 꺼낸다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 1. number 가 report_text 안에 없으면 (if, not in)
#|         if number not in report_text:
            # 2. not_found 에 number 를 추가한다 (append)
#|             not_found.append(number)
    return not_found                                             # 리포트에 없는 번호 리스트를 리턴한다 — 미리 채운 줄


def check_gate(cases, policy):                                   # 시험 사례 리스트와 승인 정책을 받는 함수
    """시험 사례마다 승인 게이트를 실행해, 결정이 기대한 결정과 다른 사례의 이름을 리스트로 리턴한다.
    승인 기준을 바꾼 뒤에도 자동 · 승인 필요 · 차단 금지가 맞게 나뉘는지 확인할 때 쓴다.
    """
    wrong = []                                                   # 기대와 다른 사례를 모을 빈 리스트 — 미리 채운 줄
    for case in cases:                                           # 시험 사례를 하나씩 꺼낸다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. decide_gate(case["request"], policy) 의 두 결과를 decision, reasons 에 담는다
#|         decision, reasons = decide_gate(case["request"], policy)
        # 4. decision 이 case["expected"] 와 다르면 (if, !=)
#|         if decision != case["expected"]:
            wrong.append(case["case"] + " (기대 " + case["expected"] + ", 결과 " + decision + ")")  # 사례 이름과 두 결정을 추가한다 — 미리 채운 줄
    return wrong                                                 # 기대와 다른 사례 리스트를 리턴한다 — 미리 채운 줄


def check_recovery(results, state, true_positive_users):         # 오탐 처리 결과 · 처리 뒤 상태 · 진짜 공격 계정 리스트를 받는 함수
    """오탐 처리 결과에서 남은 대상 · 시간 초과를 찾고, 진짜 공격 계정이 풀렸는지도 확인해 문제 문장 리스트를 리턴한다.
    오탐 복구가 신속하고 완전했는지, 진짜 공격의 조치는 그대로인지 확인할 때 쓴다.
    """
    problems = []                                                # 문제 문장을 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                       # 오탐 처리 결과를 하나씩 꺼낸다 — 미리 채운 줄
        if result["remaining"] != []:                            # 아직 복구되지 않은 대상이 있으면 — 미리 채운 줄
            problems.append(result["incident"] + " 복구 안 됨")  # 문제를 추가한다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. result["in_time"] 이 False 이면 (if not)
#|         if not result["in_time"]:
            problems.append(result["incident"] + " 30분 넘음")   # 문제를 추가한다 — 미리 채운 줄
    for user in true_positive_users:                             # 진짜 공격 계정을 하나씩 꺼낸다 — 미리 채운 줄
        # 6. user 가 state["locked_users"] 안에 없으면 (if, not in)
#|         if user not in state["locked_users"]:
            # 7. problems 에 user + " 잠금이 풀림" 을 추가한다 (append)
#|             problems.append(user + " 잠금이 풀림")
    return problems                                              # 문제 문장 리스트를 리턴한다 — 미리 채운 줄


def mark(problems):                                              # 문제 리스트를 받는 함수
    """문제 리스트가 비어 있으면 「통과」, 하나라도 있으면 「확인 필요」를 리턴한다.
    점검 결과를 한눈에 보이게 출력할 때 쓴다.
    """
    if problems == []:                                           # 문제가 없으면
        return "통과"                                            # 통과를 리턴한다
    return "확인 필요"                                           # 문제가 있으면 확인 필요를 리턴한다
```

<h3><code>apply4-5_run.py</code></h3>

8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다.

```python exercise
from incident import load_json                                                              # Unit 1 파일의 JSON 읽기 함수를 불러온다
from false_positive import handle_false_positive                                            # 실습 4-2 의 오탐 처리 함수를 불러온다
from unit09_check import check_report, check_gate, check_recovery, mark                       # 방금 만든 점검 함수를 불러온다

REPORT_PATH = "incident_report_20261112.md"                                                 # 응용 4-3 에서 만드는 리포트 파일 이름
TRUE_POSITIVE_USERS = ["dami"]                                                              # 진짜 공격으로 확인된 계정 (오탐 처리로 풀면 안 된다)
NOW = 45                                                                                    # 오탐 신고를 처리하는 지금 시각(분)

tickets = load_json("unit10_tickets.json")                                                   # 근무가 끝났을 때의 티켓 파일을 읽는다
actions = load_json("unit10_actions.json")                                                   # 근무 중 조치 기록 파일을 읽는다
policy = load_json("config/approval_policy.json")                                           # 승인 정책 파일을 읽는다
cases = load_json("gate_cases.json")                                                        # 승인 게이트 시험 사례 파일을 읽는다
print("--- 단계 1: 점검 재료 · 티켓", len(tickets), "장 · 조치 기록", len(actions), "건 · 시험 사례", len(cases), "개")  # 단계 1 시작을 알리는 줄

with open(REPORT_PATH, encoding="utf-8") as report_file:                                    # 리포트 파일을 읽기 모드로 연다
    report_text = report_file.read()                                                        # 파일 내용을 한 문자열로 읽는다
# ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
# 8. check_report(report_text, tickets, actions) 의 결과를 report_problems 에 담는다
#| report_problems = check_report(report_text, tickets, actions)
gate_problems = check_gate(cases, policy)                                                   # 승인 게이트 점검

state = load_json("fp_state.json")                                                          # 오탐 처리 전 연습용 시스템 상태를 읽는다
log = load_json("fp_log.json")                                                              # 자동 조치 기록을 읽는다
results = []                                                                                # 오탐 처리 결과를 담을 빈 리스트
for report in load_json("fp_reports.json"):                                                 # 오탐 신고를 하나씩 꺼낸다
    result = handle_false_positive(report, log, state, NOW)                                 # 신고 한 건을 처리한다
    results.append(result)                                                                  # 처리 결과를 추가한다
# 9. check_recovery(results, state, TRUE_POSITIVE_USERS) 의 결과를 recovery_problems 에 담는다
#| recovery_problems = check_recovery(results, state, TRUE_POSITIVE_USERS)

checks = [                                                                                  # 강의계획서 Unit 4 평가 기준마다 점검 결과
    {"title": "① 근무 데이터가 리포트에 빠짐없이 들어갔다", "problems": report_problems},  # 리포트 점검
    {"title": "② 위험 점수에 따라 자동 · 승인 필요 · 차단 금지가 맞게 나뉜다", "problems": gate_problems},  # 승인 게이트 점검
    {"title": "③ 오탐 복구가 30분 안에 빠짐없이 끝났고 진짜 공격의 잠금은 그대로다", "problems": recovery_problems},  # 오탐 복구 점검
]
print("--- 단계 2: Unit 4 점검 목록")                                                        # 단계 2 시작을 알리는 줄
lines = ["# Unit 4 마무리 점검 — 2026-11-13(금)", ""]                                        # 점검 문서의 제목과 빈 줄
for check in checks:                                                                        # 점검 결과를 하나씩 꺼낸다
    result_mark = mark(check["problems"])                                                   # 통과인지 확인 필요인지 정한다
    print("[" + result_mark + "]", check["title"], "· 문제", len(check["problems"]), "개")  # 점검 한 줄을 출력한다
    lines.append("- [" + result_mark + "] " + check["title"])                               # 점검 문서에 한 줄을 추가한다
    for problem in check["problems"]:                                                       # 문제 문장을 하나씩 꺼낸다
        print("   -", problem)                                                              # 문제를 출력한다
        lines.append("  - " + problem)                                                      # 점검 문서에 문제를 추가한다

text = "\n".join(lines) + "\n"                                                              # 줄 리스트를 줄바꿈으로 이어 한 문자열로 만든다
with open("unit09_checklist.md", "w", encoding="utf-8") as check_file:                        # 점검 문서 파일을 쓰기 모드("w")로 연다
    check_file.write(text)                                                                  # 점검 문서를 파일에 쓴다
print("--- 단계 3: unit09_checklist.md", len(lines), "줄 저장")                               # 단계 3 시작을 알리는 줄과 저장한 줄 수
```

<h2>순서</h2>

1. **[터미널]** 판다스를 설치합니다. `report.py` 가 판다스를 쓰기 때문입니다. 이미 설치했다면 바로 다음 줄로 갑니다. 그다음 준비할 파일을 확인합니다. <mark>`점검 준비 정상` 이 나와야</mark> 합니다.
   ```bash
   python -m pip install pandas
   python - <<'PY'
import report
import approval_gate
import false_positive

for path in ['incident_report_20261112.md', 'unit10_tickets.json', 'unit10_actions.json']:
    open(path, encoding='utf-8').close()
print('점검 준비 정상')
PY
   ```
   - `No module named '…'` 나 `FileNotFoundError` 가 나오면 위 「준비할 파일」에서 그 이름의 파일을 찾아 만듭니다.

<!-- checklist optional -->
- [ ] 1번 명령에서 `점검 준비 정상` 이 나왔다
<!-- /checklist -->

2. **[VS Code]** 파일 세 개 `gate_cases.json` · `unit09_check.py` · `apply4-5_run.py` 를 만듭니다. 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고 파일 이름을 그대로 적은 뒤, 코드 상자의 내용을 붙여 넣고 저장합니다(`Ctrl + S`).

<!-- checklist optional -->
- [ ] `soar_response` 폴더에 `gate_cases.json` · `unit09_check.py` · `apply4-5_run.py` 를 만들고 붙여 넣은 뒤 저장했다
<!-- /checklist -->

3. **[VS Code]** `unit09_check.py` 1 ~ 7번, `apply4-5_run.py` 8 · 9번을 씁니다. 막히면 아래 「응용 4-5 정리」를 봅니다.

<!-- checklist optional -->
- [ ] `unit09_check.py` 1 ~ 7번과 `apply4-5_run.py` 8 · 9번을 쓰고 저장했다
<!-- /checklist -->

4. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다.
   ```bash
   python apply4-5_run.py
   ```
5. 출력은 세 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 과 단계 3 은 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 기준마다 한 줄씩 3줄입니다. 문제가 있으면 문제마다 한 줄이 더 나옵니다.

<!-- checklist optional -->
- [ ] `python apply4-5_run.py` 를 실행해 단계 2 의 세 기준이 `통과` 로 나왔다
<!-- /checklist -->

<!-- answer: 10|응용 4-5 정답 -->

7. **[터미널]** 서버를 끈 뒤 저장소 루트 `network-study-notes` 에서 응용 파일을 올립니다.

<!-- checklist optional -->
- [ ] 응용 파일을 깃허브에 올렸다
<!-- /checklist -->

## 응용 4-5 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 문자열 안에 없으면 | `if number not in report_text:` |
| 두 결과를 함께 받기 | `decision, reasons = decide_gate(case["request"], policy)` |
| 다르면 | `if decision != case["expected"]:` |
| 거짓이면 | `if not result["in_time"]:` |
| 리스트 안에 없으면 | `if user not in state["locked_users"]:` |
| 문자열을 이어 붙여 추가 | `problems.append(user + " 잠금이 풀림")` |
| 함수 결과를 변수에 저장하기 | `report_problems = check_report(report_text, tickets, actions)` |

---
