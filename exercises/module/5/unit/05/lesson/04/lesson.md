---
id: m5-u05-l04
title: 실습 5-2 · 정책 준수 점검
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/134_day06_am_soar_engine.md
  mission_id: GichanSource.m5-1116-am-soar-engine
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 5-2 · 정책 준수 점검

## 목표: 정책 준수 점검

> **오늘 들어온 일**
>
> - **상황**: 엔진을 실행하면 처리 결과 로그가 남습니다. 실습 5-1의 `engine_log.json`(알림 8건)과 「실습 5-2 핵심 입력 · Module 4 탐지 로그」의 `risk_engine_log.json`(Module 4 탐지 결과 5건)입니다. 이번 Unit에서 고객사 보안 담당자가 「승인 게이트와 허용 목록 · VIP 예외가 정책대로 지켜졌는지 로그로 확인해 달라」고 요청합니다. 시험 운영 때 승인 게이트를 끄고 알림 5건(`INC-401` · `INC-403` ~ `INC-406`)을 처리한 로그 `gate_off_log.json` 도 점검 대상입니다.
> - **문제**: 로그를 사람이 한 줄씩 읽으면 알림이 늘수록 놓치기 쉽습니다. 게다가 로그의 `decision`(결정) 값은 엔진이 적은 값이라서, 게이트를 끈 로그에는 모든 조치가 「자동」으로 적혀 있습니다. <mark style="background:#ffc4d6">결정 값만 읽으면 게이트를 끈 로그에서 위반을 찾지 못합니다.</mark>
> - **부탁**: 로그마다 네 가지(게이트 우회 실행 · 허용 목록 IP 차단 · VIP 계정 잠금 · 티켓 없는 조치)를 자동으로 점검해 PASS(통과: 위반 없음) · FAIL(실패: 위반 있음) 표를 만들어 주세요. 게이트 우회 실행은 로그에 저장된 조치 요청으로 <mark style="background:#e0d4ff">Unit 4 실습 4-1 `decide_gate`</mark> 를 다시 호출해 결정을 새로 구한 뒤, 실행 여부와 비교합니다. 점검 결과를 초안에 남기고, 코드와 기록을 저장소에 반영해 주세요.
> - **바뀌는 점**: 점검 12개 가운데 <mark style="background:#bde3ff">FAIL 2개</mark>가 나오고, 모두 `gate_off_log.json` 에서 나옵니다. 승인 게이트를 켜고 처리한 로그 두 개(`engine_log.json` · `risk_engine_log.json`)는 점검 8개가 모두 PASS 입니다. 상황과 이름은 설명을 위한 예시입니다.

## 2.1 로그로 정책 준수 점검하기

| 점검 | 위반으로 보는 것 | 찾는 방법 | 빈칸 |
|---|---|---|---|
| ① 게이트 우회 실행 | 다시 구한 결정이 「자동」이 아닌데 실행한 조치 | 로그의 `request` 로 `decide_gate` 를 다시 호출 | ① · ② |
| ② 허용 목록 IP 차단 | 조치 후 상태가 「차단됨」인 허용 목록 IP | `target` 과 `after` 를 허용 목록과 비교 | 미리 채움 |
| ③ VIP 계정 잠금 | 조치 후 상태가 「잠김」인 VIP 계정 | `target` 과 `after` 를 VIP 리스트와 비교 | 미리 채움 |
| ④ 티켓 없는 조치 | 실행한 조치가 있는데 `ticket` 이 빈 알림 | `count_executed` 로 센 뒤 `ticket` 확인 | 미리 채움 |

- 점검 이름의 ① ~ ④ 는 점검 번호이고, 직접 쓰는 빈칸 ① · ② 는 모두 점검 ①(게이트 우회 실행) 안에 있습니다.

- 정책 준수 점검(policy compliance check)은 통제가 설계한 대로 작동했는지 실제 기록으로 확인하는 일이고, 이때 로그가 증거(audit evidence, 오딧 에비던스: 사실을 뒷받침하는 기록)가 됩니다.
- ①은 재수행(re-performance, 리퍼포먼스: 기록된 입력으로 판단을 다시 계산해 기록된 결과와 비교하는 방법)입니다. 로그의 `request` 는 <mark style="background:#e0d4ff">Unit 4 실습 4-1 승인 게이트가 본 입력</mark>이라서, 같은 정책으로 다시 계산하면 그 조치가 원래 자동이었는지 알 수 있습니다.
- ②와 ③은 불변 조건(invariant, 인베리언트: 어떤 경우에도 항상 지켜져야 하는 조건)을 점검합니다. 게이트의 계산을 거치지 않고 결과만 보므로 <mark>게이트 코드에 오류가 있어도 위반을 찾습니다.</mark>
- <mark style="background:#e0d4ff">Unit 2 실습 2-1 `lock_account` 는 VIP 계정이면 잠그지 않고 이유를 기록합니다.</mark> 그래서 VIP 계정은 승인 게이트를 꺼도 잠기지 않을 수 있습니다. 다만 방어를 여러 겹 두는 것(다층 방어, defense in depth)과 각 겹을 따로 점검하는 것은 별개입니다. 겹이 여러 개 있어도 그 겹이 실제로 작동했는지는 ③처럼 따로 확인해야 합니다.
- 점검 결과는 `judge` 가 PASS 또는 FAIL 로 정하고, 실행 파일이 로그마다 네 줄씩 출력합니다. FAIL 이 나오면 위반한 알림 번호로 로그를 열어 그 알림의 `request` 와 `decision` 을 확인합니다.

함수 일곱 개와 실행 파일 가운데 직접 쓰는 곳은 **두 줄**(① · ②)입니다. 나머지는 모두 미리 채워 두었습니다.

```
policy_check.py   count_executed         : 실행한 조치 수를 센다
                  find_gate_bypass       : 저장된 조치 요청으로 결정을 다시 구하고 (①) 자동이 아닌데 실행했으면 (②) 모은다
                  find_allowlist_blocks  : 허용 목록 IP 가 차단되었으면 모은다
                  find_vip_locks         : VIP 계정이 잠겼으면 모은다
                  find_missing_tickets   : 실행했는데 티켓이 없으면 모은다
                  run_checks             : 점검 네 가지를 한꺼번에 실행한다
                  judge                  : 위반이 없으면 PASS 를 리턴한다
실행 파일         exercise5-2_run.py       : 로그를 읽고 점검에 실패하면 세고, 결과를 저장한다 (직접 쓰는 줄 없음)
```

## 실습 5-2 · 정책 준수 PASS · FAIL 표

**이런 상황이 있습니다**

- **지금은**: <mark>엔진은 로그를 남기지만, 승인 게이트와 허용 목록 · VIP 예외가 지켜졌는지 자동으로 확인하는 점검이 없습니다</mark>.
- **만드는 것**: 점검 네 가지와 PASS · FAIL 판정(`policy_check.py`), 로그 세 개를 읽어 점검하고 결과를 저장하기(`exercise5-2_run.py`).
- **실행하면**: <mark>단계 1: 점검할 로그 수, 단계 2: 로그마다 네 점검의 PASS · FAIL 과 위반한 알림 번호, 단계 3: FAIL 이 나온 점검 수, 단계 4: 저장한 파일이 나옵니다.</mark>

**할 일**

1. 데이터 파일 한 개와 코드 파일 두 개를 만들어 붙여 넣습니다.
2. `policy_check.py` 의 `# ←` 두 곳(① · ②)을 한 줄씩 채웁니다.
3. 실행해서 단계 2 를 읽고 결과를 기록합니다.

**`gate_off_log.json`** — 시험 운영 때 승인 게이트를 끄고(모든 조치 요청의 결정을 「자동」으로 바꾸고) 알림 5건을 처리한 로그입니다.

- 알림 한 건이 한 줄입니다. 실습 5-1 `engine_log.json` 과 같은 꼴이고, 조치마다 `executed` · `before` · `after` 와 승인 게이트가 본 조치 요청 `request` 가 들어 있습니다.
- 모든 `decision` 이 「자동」이고 이유가 「승인 게이트 끔」입니다.

<pre class="copyable"><code>[
  {"incident": "INC-401", "entity": "dami", "grade": "high", "playbook": "PB-001", "outcome": "자동 실행", "steps": [{"action": "계정 잠금", "target": "dami", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "잠기지 않음", "after": "잠김", "request": {"id": "INC-401", "incident": "INC-401", "action": "계정 잠금", "target": "dami", "grade": "high", "users_on_ip": 0, "target_count": 1}}], "ticket": "TCK-1", "error": ""},
  {"incident": "INC-403", "entity": "198.51.100.45", "grade": "low", "playbook": "PB-003", "outcome": "자동 실행", "steps": [{"action": "IP 차단", "target": "198.51.100.45", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "차단되지 않음", "after": "차단됨", "request": {"id": "INC-403", "incident": "INC-403", "action": "IP 차단", "target": "198.51.100.45", "grade": "low", "users_on_ip": 0, "target_count": 1}}], "ticket": "TCK-2", "error": ""},
  {"incident": "INC-404", "entity": "203.0.113.80", "grade": "high", "playbook": "PB-003", "outcome": "자동 실행", "steps": [{"action": "IP 차단", "target": "203.0.113.80", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "차단되지 않음", "after": "차단됨", "request": {"id": "INC-404", "incident": "INC-404", "action": "IP 차단", "target": "203.0.113.80", "grade": "high", "users_on_ip": 2, "target_count": 1}}], "ticket": "TCK-3", "error": ""},
  {"incident": "INC-405", "entity": "192.0.2.41", "grade": "mid", "playbook": "PB-003", "outcome": "자동 실행", "steps": [{"action": "IP 차단", "target": "192.0.2.41", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "차단되지 않음", "after": "차단됨", "request": {"id": "INC-405", "incident": "INC-405", "action": "IP 차단", "target": "192.0.2.41", "grade": "mid", "users_on_ip": 2, "target_count": 1}}], "ticket": "TCK-4", "error": ""},
  {"incident": "INC-406", "entity": "gaeun", "grade": "high", "playbook": "PB-001", "outcome": "자동 실행", "steps": [{"action": "계정 잠금", "target": "gaeun", "decision": "자동", "reasons": ["승인 게이트 끔"], "executed": true, "before": "변경 없음", "after": "변경 없음", "request": {"id": "INC-406", "incident": "INC-406", "action": "계정 잠금", "target": "gaeun", "grade": "high", "users_on_ip": 0, "target_count": 1}}], "ticket": "TCK-5", "error": ""}
]
</code></pre>

**`policy_check.py`** — 정책 점검 함수 모음입니다. 직접 쓰는 곳은 `find_gate_bypass` 의 ① · ② 두 줄입니다.

```python
from approval_gate import decide_gate                                                      # Unit 4 파일의 승인 게이트 함수를 불러온다


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
            # ① decide_gate(step["request"], policy) 의 두 결과를 new_decision, new_reasons 에 저장한다   # ← 이 주석 바로 아래 줄에 씁니다 (12칸)
            # ② new_decision 이 "자동" 이 아니고(and) step["executed"] 가 참이면 (if, !=, and)   # ← 이 주석 바로 아래 줄에 씁니다 (12칸)
                violations.append(result["incident"])                                      # 알림 번호를 위반 리스트에 추가한다 — 미리 채운 줄
    return violations                                                                      # 위반한 알림 번호 리스트를 리턴한다 — 미리 채운 줄


def find_allowlist_blocks(results, allowlist_ips):                                         # 결과 기록 리스트와 허용 목록을 받는 함수
    """허용 목록 IP 를 실제로 차단한 알림 번호를 리스트로 리턴한다. 승인 게이트와 별개로, 업무에 필요한 IP 가 차단되지 않았는지 확인할 때 쓴다."""
    violations = []                                                                        # 위반한 알림 번호를 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                                                 # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        for step in result["steps"]:                                                       # 조치 결과를 하나씩 꺼낸다 — 미리 채운 줄
            if step["target"] in allowlist_ips and step["after"] == "차단됨":                 # 허용 목록 IP 가 차단되었으면 — 미리 채운 줄
                violations.append(result["incident"])                                      # 알림 번호를 위반 리스트에 추가한다 — 미리 채운 줄
    return violations                                                                      # 위반한 알림 번호 리스트를 리턴한다 — 미리 채운 줄


def find_vip_locks(results, vip_accounts):                                                 # 결과 기록 리스트와 VIP 계정 리스트를 받는 함수
    """VIP 계정을 실제로 잠근 알림 번호를 리스트로 리턴한다. 승인 게이트와 별개로, VIP 계정이 자동으로 잠기지 않았는지 확인할 때 쓴다."""
    violations = []                                                                        # 위반한 알림 번호를 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                                                 # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        for step in result["steps"]:                                                       # 조치 결과를 하나씩 꺼낸다 — 미리 채운 줄
            if step["target"] in vip_accounts and step["after"] == "잠김":                   # VIP 계정이 잠겼으면 — 미리 채운 줄
                violations.append(result["incident"])                                      # 알림 번호를 위반 리스트에 추가한다 — 미리 채운 줄
    return violations                                                                      # 위반한 알림 번호 리스트를 리턴한다 — 미리 채운 줄


def find_missing_tickets(results):                                                         # 결과 기록 리스트를 받는 함수
    """조치를 실행했는데 티켓이 없는 알림 번호를 리스트로 리턴한다. 실행한 조치가 담당자에게 인계되지 않고 사라지지 않았는지 확인할 때 쓴다."""
    violations = []                                                                        # 위반한 알림 번호를 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                                                 # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        executed_count = count_executed(result)                                            # 실행한 조치 수를 센다 — 미리 채운 줄
        if executed_count > 0 and result["ticket"] == "":                                  # 실행한 조치가 있는데 티켓이 없으면 — 미리 채운 줄
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
    if violations == []:                                                                   # 위반이 없으면 — 미리 채운 줄
        return "PASS"                                                                      # 위반이 없으면 PASS 를 리턴한다 — 미리 채운 줄
    return "FAIL"                                                                          # 위반이 있으면 FAIL 을 리턴한다 — 미리 채운 줄
```

**`exercise5-2_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 로그 세 개를 차례로 읽어 점검 네 가지를 실행하고, FAIL 이 나온 점검 수를 센 뒤 결과를 `policy_check.json` 에 저장합니다.

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
    results = load_json(log_path)                                                           # 로그 파일을 리스트로 읽는다 — 미리 채운 줄
    checks = run_checks(results, policy)                                                    # 점검 네 가지를 실행한다 — 미리 채운 줄
    print("[" + log_path + "] 알림", len(results), "건")                                    # 로그 이름과 알림 수를 출력한다
    for check_name in checks:                                                               # 점검 이름을 하나씩 꺼낸다
        violations = checks[check_name]                                                     # 그 점검에서 위반한 알림 번호 리스트 — 미리 채운 줄
        verdict = judge(violations)                                                         # 통과 여부를 구한다 — 미리 채운 줄
        if verdict == "FAIL":                                                               # 점검에 실패했으면 — 미리 채운 줄
            fail_count = fail_count + 1                                                     # FAIL 이 나온 점검 수를 1 늘린다 — 미리 채운 줄
        print("  ", check_name, ":", verdict, "· 위반", len(violations), "건", violations)  # 점검 이름 · 결과 · 위반한 알림 번호 리스트를 출력한다
        rows.append({"log": log_path, "check": check_name, "result": verdict, "violations": violations})  # 점검 결과 한 줄을 추가한다 — 미리 채운 줄

print("--- 단계 3: FAIL 이 나온 점검", fail_count, "개 · 전체 점검", len(rows), "개")       # 단계 3 시작을 알리는 줄과 개수
save_json(rows, CHECK_PATH)                                                                 # 점검 결과를 파일에 저장한다
print("--- 단계 4:", CHECK_PATH, "에", len(rows), "개 저장")                                # 단계 4 시작을 알리는 줄과 저장한 수
```

**직접 쓰는 곳** — `policy_check.py` 의 `find_gate_bypass` 안 두 줄입니다. 주석 줄은 그대로 두고 각 주석 바로 아래 줄에 씁니다.

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | 저장된 요청으로 결정을 다시 구해 두 값으로 받기 | 12칸 |
| ② | 다시 구한 결정이 「자동」이 아니고 실행했으면 (`if`) | 12칸 |

- ① 확인: ① 만 쓰고 실행하면 `IndentationError: unexpected indent` 가 나옵니다. ② 를 아직 안 써서 그 아래 미리 채운 줄이 앞줄보다 들여써져 있기 때문이니 정상입니다. 막히면: 실습 5-1 `run_step` 의 `decision, reasons = decide_gate(request, context["policy"])` 와 같은 모양이고, 받는 이름이 `new_decision, new_reasons`, 넣는 값이 `step["request"], policy` 로 바뀝니다.
- ② 확인: ② 까지 쓰고 실행하면 `[gate_off_log.json]` 아래 `게이트 우회 실행 : FAIL · 위반 3 건 ['INC-404', 'INC-405', 'INC-406']` 이 나오고, 앞의 두 로그는 PASS 면 성공입니다. 막히면: 「아니고」는 `!=`, 「그리고」는 `and` 입니다. `step["executed"]` 는 이미 참 · 거짓이라 `== True` 를 붙이지 않아도 됩니다.
- 채우기 전에 실행해도 오류 없이 돌아갑니다. 다만 ① · ② 자리가 비어 있으면 미리 채운 `violations.append(…)` 가 `for` 바로 안쪽에서 조치마다 실행되어, <mark style="background:#ffc4d6">조치가 있는 알림이 세 로그 모두 게이트 우회로 나오고</mark> 단계 3 이 `FAIL 이 나온 점검 4 개` 입니다. 결정을 다시 구해 비교하는 두 줄이 빠지면 정상 로그와 위반 로그를 가르지 못한다는 것을 보여 주는 결과입니다.

**순서**

1. **[터미널]** 먼저 점검할 로그 두 개가 있는지 확인합니다. <mark>`ls` 결과에 `engine_log.json` 과 `risk_engine_log.json` 이 보이면</mark> 됩니다. `engine_log.json` 이 없으면 `python exercise5-1_run.py` 를 먼저 실행하고, `risk_engine_log.json` 이 없으면 「실습 5-2 핵심 입력 · Module 4 탐지 로그」 레슨에서 준비합니다. 그다음 **[VS Code]** 에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `gate_off_log.json` · `policy_check.py` · `exercise5-2_run.py` 파일을 만들어 이 페이지의 코드 상자를 붙여 넣고 저장합니다.
   ```bash
   pwd
   ls
   ```

<!-- checklist -->
- [ ] `soar_response` 폴더에 `gate_off_log.json` 을 만들어 붙여 넣고 저장했다(`engine_log.json` · `risk_engine_log.json` 이 있는 것도 확인했다)
- [ ] `soar_response` 폴더에 `policy_check.py` 와 `exercise5-2_run.py` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

2. **[VS Code]** `policy_check.py` 의 ① · ② 를 씁니다. 2.1 의 「재수행」 설명과 위 「직접 쓰는 곳」을 보고 씁니다.

<!-- checklist -->
- [ ] `policy_check.py` 의 ① · ② 를 채워 저장했다
<!-- /checklist -->

3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다.
   ```bash
   python exercise5-2_run.py
   ```

<!-- checklist -->
- [ ] `python exercise5-2_run.py` 를 실행해 단계 3 이 `FAIL 이 나온 점검 2 개 · 전체 점검 12 개` 로 나왔다
<!-- /checklist -->

4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 · 단계 3 · 단계 4 는 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 로그마다 제목 줄 1줄과 점검 결과 4줄이라 모두 15줄입니다.
5. **[VS Code]** 새로 생긴 `policy_check.json` 을 열어 <mark>12개 점검이 들어 있는지</mark> 봅니다.
6. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.
   - 확인 질문: FAIL 이 나온 로그와 점검 이름을 출력에서 찾습니다. `INC-405` 의 `users_on_ip` 와 승인 정책 점수로 다시 구한 결정이 무엇인지, 저장된 `decision` 만 보면 위반을 놓치는 이유가 무엇인지 설명할 수 있는지 확인합니다. 답은 아래 펼침에서 확인합니다.


**확인** — 단계 3 이 `FAIL 이 나온 점검 2 개 · 전체 점검 12 개` 이고, FAIL 두 줄이 모두 `[gate_off_log.json]` 아래에 있으면 성공입니다. 안 나오면 바로 아래 정답 펼침과 한 줄씩 맞춰 보고, `FAIL 이 나온 점검 4 개` 면 위 「직접 쓰는 곳」의 채우기 전 설명을 다시 봅니다.

## 실습 5-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 결정 다시 구하기 (①) | `new_decision, new_reasons = decide_gate(step["request"], policy)` |
| 자동 아닌데 실행했으면 (②) | `if new_decision != "자동" and step["executed"]:` |
| 허용 목록 IP 가 차단됐으면 | `if step["target"] in allowlist_ips and step["after"] == "차단됨":` |
| 실행했는데 티켓이 없으면 | `if executed_count > 0 and result["ticket"] == "":` |
| 위반이 없으면 PASS | `if violations == []:` |

---

## 핵심 코드 저장소에 반영하기

핵심 실습을 마친 뒤 실습 코드를 GitHub 저장소에 올립니다. 포트폴리오 글쓰기와 선택 과제 전에 진행합니다.

1. **[터미널]** `soar_response` 폴더에서 `git status` 를 실행합니다. `.env` 나 `.venv` 가 목록에 있으면 올리지 말고 `.gitignore` 를 확인합니다.
2. `network-study-notes` 저장소 루트에서 아래 명령을 한 줄씩 실행합니다.
   ```bash
   git add .
   git commit -m "Add SOAR engine and policy checks"
   git push
   ```
3. GitHub 저장소의 `soar_response` 폴더에서 `soar_engine.py` · `policy_check.py` 가 보이는지 확인합니다.

<!-- checklist -->
- [ ] 실습 결과에서 글감과 연결할 근거를 확인했다
<!-- /checklist -->

<!-- answer: 06|실습 5-2 정답 -->
