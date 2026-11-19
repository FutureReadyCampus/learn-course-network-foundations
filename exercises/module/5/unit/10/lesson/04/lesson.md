---
id: m5-u10-l04
title: 실습 10-3 · 정책 준수 점검과 회고 문서
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/134_day06_am_soar_engine.md
  mission_id: GichanSource.m5-1116-am-soar-engine
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 10-3 · 정책 준수 점검과 회고 문서

## 목표: 정책 점검 표와 회고

> **오늘 들어온 일**
>
> - **상황**: 실습 10-1과 실습 10-2에서 엔진을 실행하면 처리 결과 로그가 남습니다(`engine_log.json` 8건 · `risk_engine_log.json` 5건). 이번 Unit에서 고객사 보안 담당자가 「승인 게이트와 허용 목록 · VIP 예외가 정책대로 지켜졌는지 로그로 확인해 달라」고 요청합니다. 시험 운영 때 승인 게이트를 끄고 알림 5건(`INC-401` · `INC-403` ~ `INC-406`)을 처리한 로그 `gate_off_log.json` 도 점검 대상입니다.
> - **문제**: 로그를 사람이 한 줄씩 읽으면 알림이 늘수록 놓치기 쉽습니다. 게다가 로그의 `decision`(결정) 값은 엔진이 적은 값이라서, 게이트를 끈 로그에는 모든 조치가 「자동」으로 적혀 있습니다. <mark style="background:#ffc4d6">결정 값만 읽으면 게이트를 끈 로그에서 위반을 찾지 못합니다.</mark>
> - **부탁**: 로그마다 네 가지(게이트 우회 실행 · 허용 목록 IP 차단 · VIP 계정 잠금 · 티켓 없는 조치)를 자동으로 점검해 PASS · FAIL 표를 만들어 주세요. 게이트 우회 실행은 로그에 저장된 조치 요청으로 <mark style="background:#e0d4ff">Unit 8의 `decide_gate`</mark> 를 다시 호출해 결정을 새로 구한 뒤, 실행 여부와 비교합니다. 점검이 끝나면 Unit 1~10 전체 회고 문서를 쓰고 저장소에 올려 주세요.
> - **바뀌는 점**: 점검 12개 가운데 <mark style="background:#bde3ff">FAIL 2개</mark>가 나오고, 모두 `gate_off_log.json` 에서 나옵니다. 이번 Unit의 실습 10-1 · 실습 10-2에서 만든 로그 두 개는 점검 8개가 모두 PASS 입니다. 상황과 이름은 설명을 위한 예시입니다.

## 3.1 로그로 정책 준수 점검하기

| 점검 | 위반으로 보는 것 | 찾는 방법 | 번호 |
|---|---|---|---|
| ① 게이트 우회 실행 | 다시 구한 결정이 「자동」이 아닌데 실행한 조치 | 로그의 `request` 로 `decide_gate` 를 다시 호출 | 1 · 2번 |
| ② 허용 목록 IP 차단 | 조치 후 상태가 「차단됨」인 허용 목록 IP | `target` 과 `after` 를 허용 목록과 비교 | 3번 |
| ③ VIP 계정 잠금 | 조치 후 상태가 「잠김」인 VIP 계정 | `target` 과 `after` 를 VIP 리스트와 비교 | 4번 |
| ④ 티켓 없는 조치 | 실행한 조치가 있는데 `ticket` 이 빈 알림 | `count_executed` 로 센 뒤 `ticket` 확인 | 5번 |

- 정책 준수 점검(policy compliance check)은 통제가 설계한 대로 작동했는지 실제 기록으로 확인하는 일이고, 이때 로그가 증거(audit evidence, 오딧 에비던스: 사실을 뒷받침하는 기록)가 됩니다.
- ①은 재수행(re-performance, 리퍼포먼스: 기록된 입력으로 판단을 다시 계산해 기록된 결과와 비교하는 방법)입니다. 로그의 `request` 는 <mark style="background:#e0d4ff">Unit 8의 승인 게이트가 본 입력</mark>이라서, 같은 정책으로 다시 계산하면 그 조치가 원래 자동이었는지 알 수 있습니다.
- ②와 ③은 불변 조건(invariant, 인베리언트: 어떤 경우에도 항상 지켜져야 하는 조건)을 점검합니다. 게이트의 계산을 거치지 않고 결과만 보므로 <mark>게이트 코드에 오류가 있어도 위반을 찾습니다.</mark>
- <mark style="background:#e0d4ff">Unit 4의 `lock_account` 는 VIP 계정이면 잠그지 않고 이유를 기록합니다.</mark> 그래서 VIP 계정은 승인 게이트를 꺼도 잠기지 않을 수 있습니다. 다만 방어를 여러 겹 두는 것(다층 방어, defense in depth)과 각 겹을 따로 점검하는 것은 별개입니다.
- 점검 결과는 `judge`(6번)가 PASS 또는 FAIL 로 정하고, 실행 파일이 로그마다 네 줄씩 출력합니다. FAIL 이 나오면 위반한 알림 번호로 로그를 열어 그 알림의 `request` 와 `decision` 을 확인합니다.

함수 일곱 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
policy_check.py   count_executed         : 실행한 조치 수를 센다 (미리 채움)
                  find_gate_bypass       : 저장된 조치 요청으로 결정을 다시 구하고 (1번) 자동이 아닌데 실행했으면 (2번) 모은다
                  find_allowlist_blocks  : 허용 목록 IP 가 차단되었으면 (3번) 모은다
                  find_vip_locks         : VIP 계정이 잠겼으면 (4번) 모은다
                  find_missing_tickets   : 실행했는데 티켓이 없으면 (5번) 모은다
                  run_checks             : 점검 네 가지를 한꺼번에 실행한다 (미리 채움)
                  judge                  : 위반이 없으면 PASS 를 리턴한다 (6번)
실행 파일         exercise10-3_run.py       : 로그를 읽고 (7번) 점검에 실패하면 (8번) 세고, 결과를 저장한다 (9번)
```

## 실습 10-3 · 정책 준수 PASS · FAIL 표

**이런 상황이 있습니다**

- **지금은**: <mark>엔진은 로그를 남기지만, 승인 게이트와 허용 목록 · VIP 예외가 지켜졌는지 자동으로 확인하는 점검이 없습니다</mark>.
- **만드는 것**: 점검 네 가지와 PASS · FAIL 판정(`policy_check.py`), 로그 세 개를 읽어 점검하고 결과를 저장하기(`exercise10-3_run.py`).
- **실행하면**: <mark>단계 1: 점검할 로그 수, 단계 2: 로그마다 네 점검의 PASS · FAIL 과 위반한 알림 번호, 단계 3: FAIL 이 나온 점검 수, 단계 4: 저장한 파일이 나옵니다.</mark>

**할 일**: 데이터 파일 한 개와 코드 파일 두 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 를 읽은 뒤, 회고 문서를 쓰고 깃허브에 올립니다.

**`gate_off_log.json`** — 시험 운영 때 승인 게이트를 끄고(모든 조치 요청의 결정을 「자동」으로 바꾸고) 알림 5건을 처리한 로그입니다.

- 알림 한 건이 한 줄입니다. 실습 10-1 `engine_log.json` 과 같은 꼴이고, 조치마다 `executed` · `before` · `after` 와 승인 게이트가 본 조치 요청 `request` 가 들어 있습니다.
- 모든 `decision` 이 「자동」이고 이유가 「승인 게이트 끔」입니다.

```
[
  {"incident": "INC-401", "entity": "dami", "grade": "high", "playbook": "PB-001", "outcome": "자동 실행", "steps": [{"action": "계정 잠금", "target": "dami", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "잠기지 않음", "after": "잠김", "request": {"id": "INC-401", "incident": "INC-401", "action": "계정 잠금", "target": "dami", "grade": "high", "users_on_ip": 0, "target_count": 1}}], "ticket": "TCK-1", "error": ""},
  {"incident": "INC-403", "entity": "198.51.100.45", "grade": "low", "playbook": "PB-003", "outcome": "자동 실행", "steps": [{"action": "IP 차단", "target": "198.51.100.45", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "차단되지 않음", "after": "차단됨", "request": {"id": "INC-403", "incident": "INC-403", "action": "IP 차단", "target": "198.51.100.45", "grade": "low", "users_on_ip": 0, "target_count": 1}}], "ticket": "TCK-2", "error": ""},
  {"incident": "INC-404", "entity": "203.0.113.80", "grade": "high", "playbook": "PB-003", "outcome": "자동 실행", "steps": [{"action": "IP 차단", "target": "203.0.113.80", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "차단되지 않음", "after": "차단됨", "request": {"id": "INC-404", "incident": "INC-404", "action": "IP 차단", "target": "203.0.113.80", "grade": "high", "users_on_ip": 2, "target_count": 1}}], "ticket": "TCK-3", "error": ""},
  {"incident": "INC-405", "entity": "192.0.2.41", "grade": "mid", "playbook": "PB-003", "outcome": "자동 실행", "steps": [{"action": "IP 차단", "target": "192.0.2.41", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "차단되지 않음", "after": "차단됨", "request": {"id": "INC-405", "incident": "INC-405", "action": "IP 차단", "target": "192.0.2.41", "grade": "mid", "users_on_ip": 2, "target_count": 1}}], "ticket": "TCK-4", "error": ""},
  {"incident": "INC-406", "entity": "gaeun", "grade": "high", "playbook": "PB-001", "outcome": "자동 실행", "steps": [{"action": "계정 잠금", "target": "gaeun", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "변경 없음", "after": "변경 없음", "request": {"id": "INC-406", "incident": "INC-406", "action": "계정 잠금", "target": "gaeun", "grade": "high", "users_on_ip": 0, "target_count": 1}}], "ticket": "TCK-5", "error": ""}
]
```

**`policy_check.py`** — 정책 점검 함수 모음입니다. 직접 쓰는 곳은 1 ~ 6번입니다.

- 2번 · 3번 · 4번 · 5번 · 6번은 `if` 한 줄만 쓰고, 그 아래 미리 채운 줄이 `if` 안쪽입니다. 1번과 2번은 같은 함수에 있고 둘 다 같은 들여쓰기에서 시작합니다.

```python
from approval_gate import decide_gate                                                      # Unit 8 파일의 승인 게이트 함수를 불러온다


def count_executed(result):                                                                # 결과 기록 한 건을 받는 함수
    """결과 기록에서 실제로 실행한 조치가 몇 개인지 센다. 실행한 조치가 있는데 티켓이 없는 알림을 찾을 때 쓴다."""
    executed_count = 0                                                                     # 실행한 조치 수 : 처음에는 0
    for step in result["steps"]:                                                           # 조치 결과를 하나씩 꺼낸다
        if step["executed"]:                                                               # 실행한 조치이면
            executed_count = executed_count + 1                                            # 실행한 조치 수를 1 늘린다
    return executed_count                                                                  # 실행한 조치 수를 리턴한다


def find_gate_bypass(results, policy):                                                     # 결과 기록 리스트와 승인 정책을 받는 함수
    """저장된 조치 요청으로 승인 게이트의 결정을 다시 구해, 자동이 아닌데 실행된 조치가 있는 알림 번호를 리스트로 리턴한다. 게이트를 거치지 않았거나 결정을 바꿔 쓴 실행을 찾을 때 쓴다."""
    violations = []                                                                        # 위반한 알림 번호를 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                                                 # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        for step in result["steps"]:                                                       # 조치 결과를 하나씩 꺼낸다 — 미리 채운 줄
            # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
            # 1. decide_gate(step["request"], policy) 의 두 결과를 new_decision, new_reasons 에 저장한다
            # 2. new_decision 이 "자동" 이 아니고(and) step["executed"] 가 참이면 (if, !=, and)
                violations.append(result["incident"])                                      # 알림 번호를 위반 리스트에 추가한다 — 미리 채운 줄
    return violations                                                                      # 위반한 알림 번호 리스트를 리턴한다 — 미리 채운 줄


def find_allowlist_blocks(results, allowlist_ips):                                         # 결과 기록 리스트와 허용 목록을 받는 함수
    """허용 목록 IP 를 실제로 차단한 알림 번호를 리스트로 리턴한다. 승인 게이트와 별개로, 업무에 필요한 IP 가 차단되지 않았는지 확인할 때 쓴다."""
    violations = []                                                                        # 위반한 알림 번호를 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                                                 # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        for step in result["steps"]:                                                       # 조치 결과를 하나씩 꺼낸다 — 미리 채운 줄
            # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
            # 3. step["target"] 이 allowlist_ips 안에 있고(and) step["after"] 가 "차단됨" 이면 (if, in, ==, and)
                violations.append(result["incident"])                                      # 알림 번호를 위반 리스트에 추가한다 — 미리 채운 줄
    return violations                                                                      # 위반한 알림 번호 리스트를 리턴한다 — 미리 채운 줄


def find_vip_locks(results, vip_accounts):                                                 # 결과 기록 리스트와 VIP 계정 리스트를 받는 함수
    """VIP 계정을 실제로 잠근 알림 번호를 리스트로 리턴한다. 승인 게이트와 별개로, VIP 계정이 자동으로 잠기지 않았는지 확인할 때 쓴다."""
    violations = []                                                                        # 위반한 알림 번호를 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                                                 # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        for step in result["steps"]:                                                       # 조치 결과를 하나씩 꺼낸다 — 미리 채운 줄
            # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
            # 4. step["target"] 이 vip_accounts 안에 있고(and) step["after"] 가 "잠김" 이면 (if, in, ==, and)
                violations.append(result["incident"])                                      # 알림 번호를 위반 리스트에 추가한다 — 미리 채운 줄
    return violations                                                                      # 위반한 알림 번호 리스트를 리턴한다 — 미리 채운 줄


def find_missing_tickets(results):                                                         # 결과 기록 리스트를 받는 함수
    """조치를 실행했는데 티켓이 없는 알림 번호를 리스트로 리턴한다. 실행한 조치가 담당자에게 인계되지 않고 사라지지 않았는지 확인할 때 쓴다."""
    violations = []                                                                        # 위반한 알림 번호를 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                                                 # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        executed_count = count_executed(result)                                            # 실행한 조치 수를 센다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. executed_count 가 0 보다 크고(and) result["ticket"] 이 "" 이면 (if, >, ==, and)
            violations.append(result["incident"])                                          # 알림 번호를 위반 리스트에 추가한다 — 미리 채운 줄
    return violations                                                                      # 위반한 알림 번호 리스트를 리턴한다 — 미리 채운 줄


def run_checks(results, policy):                                                           # 결과 기록 리스트와 승인 정책을 받는 함수
    """점검 네 가지를 모두 실행해 점검 이름마다 위반한 알림 번호 리스트를 담은 딕셔너리를 리턴한다. 로그 하나를 정책에 비추어 한 번에 점검할 때 쓴다."""
    checks = {}                                                                            # 점검 이름 → 위반한 알림 번호 리스트 — 미리 채운 줄
    checks["게이트 우회 실행"] = find_gate_bypass(results, policy)                         # 점검 ① — 미리 채운 줄
    checks["허용 목록 IP 차단"] = find_allowlist_blocks(results, policy["allowlist_ips"])  # 점검 ② — 미리 채운 줄
    checks["VIP 계정 잠금"] = find_vip_locks(results, policy["vip_accounts"])              # 점검 ③ — 미리 채운 줄
    checks["티켓 없는 조치"] = find_missing_tickets(results)                               # 점검 ④ — 미리 채운 줄
    return checks                                                                          # 점검 결과 딕셔너리를 리턴한다 — 미리 채운 줄


def judge(violations):                                                                     # 위반한 알림 번호 리스트를 받는 함수
    """위반이 하나도 없으면 「PASS」, 하나라도 있으면 「FAIL」을 리턴한다. 점검 결과를 한눈에 보이게 출력할 때 쓴다."""
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 6. violations 가 빈 리스트 [] 이면 (if, ==)
        return "PASS"                                                                      # 위반이 없으면 PASS 를 리턴한다 — 미리 채운 줄
    return "FAIL"                                                                          # 위반이 있으면 FAIL 을 리턴한다 — 미리 채운 줄
```

**`exercise10-3_run.py`** — 7 · 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다.

```python
from incident import load_json, save_json                                                   # Unit 1 파일의 JSON 읽기 · 쓰기 함수를 불러온다
from policy_check import run_checks, judge                                                  # 방금 만든 점검 함수를 불러온다

LOG_FILES = ["engine_log.json", "risk_engine_log.json", "gate_off_log.json"]                # 점검할 엔진 로그 파일 세 개
CHECK_PATH = "policy_check.json"                                                            # 점검 결과를 저장할 파일 이름

policy = load_json("config/approval_policy.json")                                           # 승인 정책 파일을 딕셔너리로 읽는다
print("--- 단계 1: 점검할 로그", len(LOG_FILES), "개 · 점검 4가지")                         # 단계 1 시작을 알리는 줄

rows = []                                                                                   # 점검 결과 한 줄씩 모을 빈 리스트
fail_count = 0                                                                              # FAIL 이 나온 점검 수 : 처음에는 0
print("--- 단계 2: 로그마다 점검 결과")                                                     # 단계 2 시작을 알리는 줄
for log_path in LOG_FILES:                                                                  # 로그 파일을 하나씩 꺼낸다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. load_json(log_path) 의 결과를 results 에 저장한다
    checks = run_checks(results, policy)                                                    # 점검 네 가지를 실행한다 — 미리 채운 줄
    print("[" + log_path + "] 알림", len(results), "건")                                    # 로그 이름과 알림 수를 출력한다
    for check_name in checks:                                                               # 점검 이름을 하나씩 꺼낸다
        violations = checks[check_name]                                                     # 그 점검에서 위반한 알림 번호 리스트 — 미리 채운 줄
        verdict = judge(violations)                                                         # 통과 여부를 구한다 — 미리 채운 줄
        # 8. verdict 가 "FAIL" 이면 (if, ==)
            fail_count = fail_count + 1                                                     # FAIL 이 나온 점검 수를 1 늘린다 — 미리 채운 줄
        print("  ", check_name, ":", verdict, "· 위반", len(violations), "건", violations)  # 점검 이름 · 결과 · 위반한 알림 번호 리스트를 출력한다
        rows.append({"log": log_path, "check": check_name, "result": verdict, "violations": violations})  # 점검 결과 한 줄을 추가한다 — 미리 채운 줄

print("--- 단계 3: FAIL 이 나온 점검", fail_count, "개 · 전체 점검", len(rows), "개")       # 단계 3 시작을 알리는 줄과 개수
# ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
# 9. rows 를 CHECK_PATH 파일에 저장한다 (save_json)
print("--- 단계 4:", CHECK_PATH, "에", len(rows), "개 저장")                                # 단계 4 시작을 알리는 줄과 저장한 수
```

**순서**

1. **[터미널]** 먼저 실습 10-1 · 실습 10-2 로그가 있는지 확인합니다. <mark>`ls` 결과에 `engine_log.json` 과 `risk_engine_log.json` 이 보이면</mark> 됩니다. 없으면 `python exercise10-1_run.py` 와 `python exercise10-2_run.py` 를 먼저 실행합니다(맥북은 `python3`). 그다음 **[VS Code]** 에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `gate_off_log.json` · `policy_check.py` · `exercise10-3_run.py` 파일을 만들어 이 페이지의 코드 상자를 붙여 넣고 저장합니다.
   ```bash
   pwd
   ls
   ```
2. **[VS Code]** `policy_check.py` 1 ~ 6번, `exercise10-3_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「실습 10-3 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise10-3_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 · 단계 3 · 단계 4 는 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 로그마다 제목 줄 1줄과 점검 결과 4줄이라 모두 15줄입니다.
5. **[VS Code]** 새로 생긴 `policy_check.json` 을 열어 <mark>12개 점검이 들어 있는지</mark> 봅니다.
6. **[VS Code]** Unit 1~10 전체 회고 문서 `unit10_final_retrospective.md` 를 만듭니다. 파일 이름의 `unit10` 은 강의계획서의 Unit 10(이번 Unit)입니다. `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `unit10_final_retrospective.md` 파일을 만든 뒤, 아래 틀을 붙여 넣고 `…` 를 채웁니다. 틀은 지우지 않고 그대로 둡니다.

   - 1절은 엔진이 각 Unit의 파일을 어디에 쓰는지 한 문장씩 씁니다(실습 10-1 `soar_engine.py` 의 `import` 줄과 오늘 만든 파일이 근거입니다).
   - 2절은 <mark>오늘 출력이나 코드에서 근거를 찾아</mark> 운영에서 깨질 수 있는 곳 세 가지와 막는 방법을 씁니다.
   - 3절은 캡스톤 주제 가운데 하나를 고르고, 새 코드를 쓰지 않고 설정 파일만 바꿔 시작할 수 있는 것을 씁니다.

   ````markdown
   # Module 5 Unit 10 최종 회고 (이름)

   ## 1. Unit 1~10에서 만든 것

   엔진이 각 Unit의 파일을 어디에 쓰는지 한 문장씩 씁니다.

   | Unit | 엔진과 연결된 파일 | 엔진에서 하는 일 |
   |---|---|---|
   | Unit 1 · Unit 2 · Unit 3 | `incident.py` · `config/playbook_registry.json` | … |
   | Unit 4 · Unit 5 | `account_actions.py` · `ip_actions.py` | … |
   | Unit 6 · Unit 7 | `ticketing.py` | … |
   | Unit 8 · Unit 9 | `approval_gate.py` | … |
   | Unit 10 | `soar_engine.py` · `engine_input.py` · `policy_check.py` | … |

   ## 2. 운영하면 깨질 수 있는 곳 3가지

   오늘 출력이나 코드에서 근거를 찾아 씁니다.

   | 깨질 곳 | 근거(오늘의 파일 · 단계) | 막는 방법 |
   |---|---|---|
   | … | … | … |
   | … | … | … |
   | … | … | … |

   ## 3. 캡스톤 주제와 내 모듈

   | 캡스톤 주제 | 쓰는 Module 모듈 |
   |---|---|
   | 과다권한 자동 회수봇 | `access_control` + `agent_core` |
   | 이상행위 자동 차단 에이전트 | `anomaly_detection` + `soar_response` |
   | ZT 보안 자세 점검 · 스코어링 | `network_zt` + `agent_core` |
   | AI 보안 이벤트 분류 · 초동대응봇 | `anomaly_detection` + `soar_response` + `agent_core` |

   - 내가 고르고 싶은 주제: …
   - 캡스톤 첫날 새 코드 없이 바꿔 볼 설정 파일 2개: …
   - 그대로 가져다 쓸 내 파일 3개: …
   ````
7. **[보고서]** `report_u10.md` 의 `## 실습 10-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, FAIL 이 나온 로그와 FAIL 이 나온 점검 이름 · 위반한 알림 번호를 적어 주세요.
   - (나) [핵심 질문] `gate_off_log.json` 의 `INC-405` 는 `decision` 이 「자동」인데 점검 ①에서 위반으로 나옵니다. 그 `request` 의 `users_on_ip` 와 승인 정책의 점수를 근거로 다시 구한 결정을 적고, 로그의 `decision` 만 읽으면 위반을 놓치는 이유를 적어 주세요.
   - (다) [핵심 질문] `INC-406`(`gaeun`)은 점검 ①은 FAIL 인데 점검 ③은 PASS 입니다. 그 알림의 `before` · `after` 를 근거로 `gaeun` 이 잠기지 않은 이유를 Unit 4의 `lock_account` 와 연결해 적고, 점검 ③이 게이트와 별도로 필요한 이유를 적어 주세요.

## 실습 10-3 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 두 결과를 함께 받기 | `new_decision, new_reasons = decide_gate(step["request"], policy)` |
| 다르고 그리고 참이면 | `if new_decision != "자동" and step["executed"]:` |
| 리스트 안에 있고 그리고 같으면 | `if step["target"] in allowlist_ips and step["after"] == "차단됨":` |
| 크고 그리고 같으면 | `if executed_count > 0 and result["ticket"] == "":` |
| 빈 리스트와 같으면 | `if violations == []:` |
| 함수 결과를 변수에 저장하기 | `results = load_json(log_path)` |
| 리스트를 파일에 저장하기 | `save_json(rows, CHECK_PATH)` |

---

## 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기

<mark>문제가 아니라 Unit 1~10에서 만든 것을 저장소에 올리는 마무리입니다.</mark> 실습 10-3 마지막 약 10분에 합니다. 어느 터미널을 써도 됩니다. 먼저 `pwd` 로 위치를 확인하고, 결과가 `soar_response` 로 끝나면 아래 1번의 `cd ..` 를 칩니다.

**이런 상황이 있습니다**

- **지금은**: <mark>팀장이 「Unit 1~10에서 만든 SOAR 모듈과 엔진 · 점검 · 회고 문서를 저장소에 남겨 달라」고 합니다</mark>.
- **그래서 하는 것**: `git status` 로 올라갈 파일을 확인한 뒤(`.env` 같은 비밀 키 파일이 섞이면 안 됩니다) `git add` → `git commit` → `git push` 순서로 올립니다.
- **끝나면**: 깃허브 저장소의 `soar_response` 폴더에 `soar_engine.py` · `engine_input.py` · `policy_check.py` · `unit10_final_retrospective.md` · `report_u10.md` 와 로그 · 요약 파일(`engine_log.json` · `risk_engine_log.json` · `engine_summary.json` · `policy_check.json`)이 보입니다.

**순서**

0. **[터미널]** 오늘 만든 파일이 있는지 `soar_response` 폴더에서 확인합니다. 두 명령을 하나씩 칩니다. Unit 10 의 모든 질문에서 `답:` 뒤와 코드 상자가 채워졌는지, `unit10_final_retrospective.md` 의 `…` 가 모두 채워졌는지도 확인합니다(마무리 (가)는 3번에서 채웁니다).

   ① 지금 위치를 확인합니다.

   ```bash
   pwd
   ```

   - 하는 일: 지금 있는 폴더의 위치를 보여 줍니다.
   - 나오는 것: <mark style="background:#bde3ff">`soar_response` 로 끝나야</mark> 합니다.

   ② 폴더 안의 파일을 봅니다.

   ```bash
   ls
   ```

   - 하는 일: 폴더 안의 파일 이름을 보여 줍니다.
   - 나오는 것: `soar_engine.py` · `engine_input.py` · `policy_check.py` · `unit10_final_retrospective.md` · `report_u10.md` · `engine_log.json` · `risk_engine_log.json` · `engine_summary.json` · `policy_check.json` · `config` 가 보이면 됩니다.

1. **[터미널]** `security-agent-toolkit` 폴더로 이동합니다. 0번의 `pwd` 결과가 `soar_response` 로 끝날 때만 `cd ..` 를 칩니다. 이미 `…/security-agent-toolkit` 으로 끝나면 `cd ..` 는 건너뛰고 `pwd` 만 칩니다.

   ① 한 단계 위 폴더로 이동합니다.

   ```bash
   cd ..
   ```

   - 하는 일: 한 단계 위 폴더로 이동합니다.
   - 나오는 것: 아무것도 나오지 않습니다.

   ② 지금 위치를 확인합니다.

   ```bash
   pwd
   ```

   - 하는 일: 지금 있는 폴더의 위치를 보여 줍니다.
   - 나오는 것: <mark style="background:#bde3ff">`…/security-agent-toolkit` 으로 끝나면</mark> 됩니다. 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.

2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark style="background:#ffc4d6">빨간 글씨 줄이나 `Untracked files:` 아래에 `.env`(API 키가 들어 있는 파일) 나 `.venv`(가상환경이 들어 있는 폴더)가 보이면 올리지 말고(`.env` 를 올리면 키가 공개되기 때문입니다),</mark> 아래 안내대로 `.gitignore`(깃이 올리지 않을 파일 이름을 적어 두는 파일)를 고친 뒤 `git status` 를 다시 봅니다.

   ① 올릴 파일의 상태를 봅니다.

   ```bash
   git status
   ```

   - 하는 일: 올릴 파일의 상태를 보여 줍니다.
   - 나오는 것: 바뀐 파일의 이름이 나옵니다. `soar_response/` 아래의 새 파일들이 보이면 됩니다.

   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` (파이썬이 실행하면서 자동으로 만드는 임시 폴더)가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 봅니다.

3. **[보고서]** `report_u10.md` 의 `## 마무리` 아래를 채웁니다. <mark>올리기 전에 채워야</mark> 깃허브에 빈칸 없이 올라갑니다.
   - (가) `git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.
   - <mark>Unit 10의 앞선 실습에서 못 적은 보고서 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.</mark> 올린 뒤에 이어서 적어 다시 올려도 됩니다.
4. **[터미널]** 바뀐 파일을 모두 올릴 목록에 추가하고(`add`), 기록하고(`commit`), 올립니다(`push`). 세 명령을 순서대로 하나씩 칩니다.

   ① 바뀐 파일을 모두 올릴 목록에 추가합니다.

   ```bash
   git add .
   ```

   - 하는 일: 바뀐 파일을 올릴 대상에 추가합니다.
   - 나오는 것: 아무것도 나오지 않습니다.

   ② 기록으로 저장합니다.

   ```bash
   git commit -m "Add SOAR engine, engine input check, policy check and final retrospective"
   ```

   - 하는 일: 따옴표 안의 설명을 붙여 기록으로 저장합니다.
   - 나오는 것: 바뀐 파일 수가 적힌 줄이 나옵니다.

   ③ 깃허브로 올립니다.

   ```bash
   git push
   ```

   - 하는 일: 저장한 기록을 깃허브로 올립니다.
   - 나오는 것: 올라간 내용이 몇 줄 나옵니다.

   - <mark style="background:#ffc4d6">`git push` 가 거절(`rejected`)되면 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다.</mark> `git pull --no-rebase`(깃허브의 새 기록을 내 PC 로 받아 와 합치는 명령)를 입력한 뒤 `git push` 를 다시 합니다.
   - 편집기 화면이 뜨면 `Esc` → `:wq`(저장하고 나가기) → `Enter` 를 합니다.
   - `git pull` 만 입력했을 때 `fatal: Need to specify how to reconcile divergent branches` 가 나오면, 내 기록과 깃허브 기록이 갈라졌다는 뜻이므로 `git pull --no-rebase` 를 입력합니다.

5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `soar_response` 폴더를 열고, VS Code 왼쪽 목록의 `soar_response` 폴더에 있는 파일들이 깃허브에도 보이는지 확인합니다. <mark>`__pycache__` 폴더는 없어도 됩니다</mark>.
   - 깃허브에 안 보이는 파일이 있으면, 그 파일이 VS Code 왼쪽 목록의 `soar_response` 폴더에 내 PC 에도 있는지 봅니다.
     - 없으면 다른 폴더에 만든 것이니 `soar_response` 안으로 이동하고, `pwd` 로 위치를 확인한 뒤 2번의 `git status` 부터 다시 합니다.

## 마무리 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 올릴 파일 확인 | `git status` (`.env` · `.venv` 가 보이면 멈춤) |
| 올리기 | `git add .` → `git commit -m "…"` → `git push` |
| 올린 뒤 | 브라우저에서 `soar_response` 폴더와 파일이 있는지 확인 |

---

## 이번 Unit 마무리

| 확인 | 문제 |
|---|---|
| 알림을 승인 게이트를 거쳐 조치하고 티켓을 남기며, 오류가 난 알림은 실패로 격리하는 통합 엔진을 만들었다 | 실습 10-1 |
| Module 4 탐지 결과를 점검해 엔진의 입력으로 바꾸고, 실행해 운영 요약을 만들었다 | 실습 10-2 |
| 엔진 로그를 정책 네 가지로 점검하고, Unit 1~10 전체 회고 문서를 쓰고, 깃허브에 올렸다 | 실습 10-3 · 마무리 |

**강의계획서 평가 기준 확인**

| 기준 | 확인할 곳 |
|---|---|
| Module 4 탐지 결과부터 Module 5 대응까지 종단간으로 오류 없이 동작한다 | 실습 10-2 단계 3 ~ 5 <mark style="background:#bde3ff">(Module 4 5건 → 알림 5건 → 자동 실행 2건 · 조치 없음 3건 · 실패 0건)</mark> |
| 승인 게이트가 위험도에 따라 정확히 작동한다 | 실습 10-1 단계 2 · 3 <mark style="background:#bde3ff">(자동 실행 2 · 승인 대기 2 · 차단 금지 1)</mark>, 실습 10-3 점검 ① |
| 모듈이 서로 이어져 하나의 흐름으로 동작한다 | 실습 10-1 `soar_engine.py` 의 `import` 6줄, 회고 문서 1절 |

---

---

<!-- learn:answers -->
