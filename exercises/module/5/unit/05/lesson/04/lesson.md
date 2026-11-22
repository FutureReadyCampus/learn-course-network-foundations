---
id: m5-u05-l04
title: 실습 5-2 · 정책 준수 점검과 회고 문서
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/134_day06_am_soar_engine.md
  mission_id: GichanSource.m5-1116-am-soar-engine
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 5-2 · 정책 준수 점검과 회고 문서

## 목표: 정책 점검 표와 회고

> **오늘 들어온 일**
>
> - **상황**: 엔진을 실행하면 처리 결과 로그가 남습니다. 실습 5-1의 `engine_log.json`(알림 8건)과 「제공 파일」 레슨의 `risk_engine_log.json`(Module 4 탐지 결과 5건)입니다. 이번 Unit에서 고객사 보안 담당자가 「승인 게이트와 허용 목록 · VIP 예외가 정책대로 지켜졌는지 로그로 확인해 달라」고 요청합니다. 시험 운영 때 승인 게이트를 끄고 알림 5건(`INC-401` · `INC-403` ~ `INC-406`)을 처리한 로그 `gate_off_log.json` 도 점검 대상입니다.
> - **문제**: 로그를 사람이 한 줄씩 읽으면 알림이 늘수록 놓치기 쉽습니다. 게다가 로그의 `decision`(결정) 값은 엔진이 적은 값이라서, 게이트를 끈 로그에는 모든 조치가 「자동」으로 적혀 있습니다. <mark style="background:#ffc4d6">결정 값만 읽으면 게이트를 끈 로그에서 위반을 찾지 못합니다.</mark>
> - **부탁**: 로그마다 네 가지(게이트 우회 실행 · 허용 목록 IP 차단 · VIP 계정 잠금 · 티켓 없는 조치)를 자동으로 점검해 PASS(통과: 위반 없음) · FAIL(실패: 위반 있음) 표를 만들어 주세요. 게이트 우회 실행은 로그에 저장된 조치 요청으로 <mark style="background:#e0d4ff">Unit 4 실습 4-1 `decide_gate`</mark> 를 다시 호출해 결정을 새로 구한 뒤, 실행 여부와 비교합니다. 점검이 끝나면 Module 5 전체를 돌아보는 회고 문서를 쓰고 저장소에 올려 주세요.
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
3. 실행해서 단계 2 를 읽은 뒤, 다음 페이지에서 최종 회고 문서를 씁니다.

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

1. **[터미널]** 먼저 점검할 로그 두 개가 있는지 확인합니다. <mark>`ls` 결과에 `engine_log.json` 과 `risk_engine_log.json` 이 보이면</mark> 됩니다. `engine_log.json` 이 없으면 `python exercise5-1_run.py` 를 먼저 실행하고(맥북은 `python3`), `risk_engine_log.json` 이 없으면 「제공 파일」 레슨에서 만듭니다. 그다음 **[VS Code]** 에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `gate_off_log.json` · `policy_check.py` · `exercise5-2_run.py` 파일을 만들어 이 페이지의 코드 상자를 붙여 넣고 저장합니다.
   ```bash
   pwd
   ls
   ```
2. **[VS Code]** `policy_check.py` 의 ① · ② 를 씁니다. 2.1 의 「재수행」 설명과 아래 「직접 쓰는 곳」을 보고 씁니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise5-2_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 · 단계 3 · 단계 4 는 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 로그마다 제목 줄 1줄과 점검 결과 4줄이라 모두 15줄입니다.
5. **[VS Code]** 새로 생긴 `policy_check.json` 을 열어 <mark>12개 점검이 들어 있는지</mark> 봅니다.
6. **[보고서]** `report_u5.md` 의 `## 실습 5-2` 아래를 채웁니다(보고서 파일은 「보고서 쓰기」 레슨에서 만듭니다). 다 채웠으면 「최종 회고 문서 쓰기」 페이지로 갑니다.
   - (가) [핵심 질문] 실행한 출력 전체를 붙여 넣고, FAIL 이 나온 로그와 FAIL 이 나온 점검 이름 · 위반한 알림 번호를 적어 주세요.
   - (나) [핵심 질문] `gate_off_log.json` 의 `INC-405` 는 `decision` 이 「자동」인데 점검 ①에서 위반으로 나옵니다. 그 `request` 의 `users_on_ip` 와 승인 정책의 점수를 근거로 다시 구한 결정을 적고, 로그의 `decision` 만 읽으면 위반을 놓치는 이유를 적어 주세요.
   - (다) [응용] `INC-406`(`gaeun`)은 점검 ①은 FAIL 인데 점검 ③은 PASS 입니다. 그 알림의 `before` · `after` 를 근거로 `gaeun` 이 잠기지 않은 이유를 Unit 2 실습 2-1 `lock_account` 와 연결해 적고, 점검 ③이 게이트와 별도로 필요한 이유를 적어 주세요.

**확인** — 단계 3 이 `FAIL 이 나온 점검 2 개 · 전체 점검 12 개` 이고, FAIL 두 줄이 모두 `[gate_off_log.json]` 아래에 있으면 성공입니다. 안 나오면 「정답」 레슨의 실습 5-2 출력과 한 줄씩 맞춰 보고, `FAIL 이 나온 점검 4 개` 면 위 「직접 쓰는 곳」의 채우기 전 설명을 다시 봅니다.

<!-- checklist -->
- [ ] `soar_response` 폴더에 `gate_off_log.json` 을 만들어 붙여 넣고 저장했다(`engine_log.json` · `risk_engine_log.json` 이 있는 것도 확인했다)
- [ ] `soar_response` 폴더에 `policy_check.py` 를 만들어 붙여 넣고 ① · ② 를 채워 저장했다
- [ ] `soar_response` 폴더에 `exercise5-2_run.py` 를 만들어 붙여 넣고 저장했다
- [ ] `python exercise5-2_run.py` 를 실행해 단계 3 이 `FAIL 이 나온 점검 2 개 · 전체 점검 12 개` 로 나왔다
<!-- /checklist -->

## 실습 5-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 결정 다시 구하기 (①) | `new_decision, new_reasons = decide_gate(step["request"], policy)` |
| 자동 아닌데 실행했으면 (②) | `if new_decision != "자동" and step["executed"]:` |
| 허용 목록 IP 가 차단됐으면 | `if step["target"] in allowlist_ips and step["after"] == "차단됨":` |
| 실행했는데 티켓이 없으면 | `if executed_count > 0 and result["ticket"] == "":` |
| 위반이 없으면 PASS | `if violations == []:` |

---

## 최종 회고 문서 쓰기

Module 5의 마지막 정리입니다(약 10분). 실습 5-2 실행까지 마친 뒤 합니다. 회고 문서 `unit10_final_retrospective.md` 는 저장소에 남기는 **정리표**입니다. 표의 칸마다 한두 문장으로 사실만 적습니다. 왜 그렇게 만들었는지, 무엇을 고민했는지는 이 문서에 길게 쓰지 않고 「오늘의 글 쓰기」 레슨에서 질문 하나를 골라 글로 풉니다. 파일 이름의 `unit10` 은 이전 판의 번호라 그대로 둡니다.

1. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `unit10_final_retrospective.md` 파일을 만든 뒤, 아래 틀을 복사해 붙여 넣고 `…` 를 채웁니다. 틀의 제목과 표 머리는 지우지 않고 그대로 둡니다.
   1. 1절은 엔진이 각 Unit의 파일을 어디에 쓰는지 한 문장씩 씁니다. 실습 5-1 `soar_engine.py` 의 `import` 여섯 줄이 근거입니다. Unit 1 줄은 본보기로 채워 두었습니다. 나머지 줄은 실습 5-1 레슨 「1.1 알림 처리 순서와 오류 격리」 표의 「하는 일」 칸을 보고 같은 모양으로 씁니다.
   2. 2절은 <mark>오늘 출력이나 코드에서 근거를 찾아</mark> 운영에서 깨질 수 있는 곳 두 가지와 막는 방법을 씁니다. 예를 들어 실습 5-1 단계 2 의 `INC-402` 실패나, 실습 5-2 의 `gate_off_log.json` FAIL 이 근거가 됩니다.
      - 한 줄은 이렇게 씁니다. 깨질 곳 「Module 4 결과에 `grade` 키가 빠지면 그 알림이 실패로만 남는다」 · 근거 「실습 5-1 단계 2 `INC-402` → 실패 · KeyError: 'grade'」 · 막는 방법 「엔진에 넣기 전에 필수 키가 있는지 확인한다」.
      - 막는 방법은 「무엇을 · 언제 확인한다」를 한 문장으로 쓰면 됩니다.
   3. 3절은 캡스톤(capstone · 캡스톤: 과정 마지막에 지금까지 만든 파일을 모아 주제 하나를 정해 완성하는 종합 프로젝트) 주제 가운데 하나를 고르고, 새 코드를 쓰지 않고 설정 파일만 바꿔 시작할 수 있는 것을 씁니다.
      - 표의 「쓰는 폴더」는 그 주제에 쓰는 작업 폴더입니다. `access_control` 은 Module 3, `anomaly_detection` 은 Module 4, `soar_response` 는 Module 5 폴더입니다. ZT 는 제로 트러스트(Zero Trust · 제로 트러스트: 회사 안에서 온 접속도 믿지 않고 요청마다 확인하는 보안 방식)의 줄임말입니다.
      - 설정 파일은 코드 없이 값만 담은 `config` 폴더의 JSON 파일입니다. 예를 들어 `config/approval_policy.json` 의 승인 기준 점수(`approval_score`)나 `config/playbook_registry.json` 의 트리거 규칙을 바꾸면 코드를 고치지 않고 엔진의 동작이 바뀝니다.
      - 「그대로 가져다 쓸 내 파일 3개」는 1절 표에 적은 파일 가운데에서 고릅니다.
2. **[VS Code]** 저장한 뒤 `…` 가 남은 칸이 없는지 봅니다. 모르는 칸은 `모름 — 막힌 곳: …` 으로 적습니다.

이 문서는 사실만 적는 정리표이고, 「오늘의 글 쓰기」의 세 문장 글과는 따로 씁니다. 글에서는 이 표를 옮겨 적지 않고, 오늘 고민한 것 하나만 내 말로 씁니다.

`network_zt` 와 `agent_core` 는 이 과정에서 만들지 않은 폴더입니다. 내 컴퓨터에 없다면 이 표를 그대로 따르지 말고, 내가 만든 `access_control` · `anomaly_detection` · `soar_response` 만으로 할 수 있는 주제(예: 둘째 줄의 이상행위 자동 차단 에이전트)를 고르거나, 있는 폴더만으로 해 볼 수 있는 범위로 주제를 좁혀 적습니다.

<pre class="copyable"><code>&#35; Module 5 최종 회고 (이름)

&#35;# 1. Unit 1 ~ 5에서 만든 것

엔진이 각 Unit의 파일을 어디에 쓰는지 한 문장씩 씁니다.

| Unit | 엔진과 연결된 파일 | 엔진에서 하는 일 |
|---|---|---|
| Unit 1 | `incident.py` · `config/playbook_registry.json` | 알림의 탐지 규칙과 등급에 맞는 플레이북을 찾는다(`match_playbooks`) |
| Unit 2 | `account_actions.py` · `ip_actions.py` | … |
| Unit 3 | `ticketing.py` | … |
| Unit 4 | `approval_gate.py` | … |
| Unit 5 | `soar_engine.py` · `policy_check.py` | … |

&#35;# 2. 운영하면 깨질 수 있는 곳 2가지

오늘 출력이나 코드에서 근거를 찾아 씁니다.

| 깨질 곳 | 근거(오늘의 파일 · 단계) | 막는 방법 |
|---|---|---|
| … | … | … |
| … | … | … |

&#35;# 3. 캡스톤 주제와 내 모듈

| 캡스톤 주제 | 쓰는 폴더 |
|---|---|
| 과다권한 자동 회수봇 | `access_control` + `agent_core` |
| 이상행위 자동 차단 에이전트 | `anomaly_detection` + `soar_response` |
| ZT 보안 자세 점검 · 스코어링 | `network_zt` + `agent_core` |
| AI 보안 이벤트 분류 · 초동대응봇 | `anomaly_detection` + `soar_response` + `agent_core` |

- 내가 고르고 싶은 주제: …
- 캡스톤 첫날 새 코드 없이 바꿔 볼 설정 파일 2개: …
- 그대로 가져다 쓸 내 파일 3개: …
</code></pre>

**확인** — VS Code 왼쪽 목록의 `soar_response` 아래에 `unit10_final_retrospective.md` 가 보이고, 열어서 `Ctrl + F`(맥북은 `Cmd + F`)로 `…` 를 찾았을 때 `모름 — 막힌 곳: …` 으로 적은 곳 말고는 나오지 않으면 성공입니다. 남은 칸이 있으면 위 1번의 절별 안내를 보고 채우거나 `모름 — 막힌 곳: …` 으로 적습니다.

<!-- checklist -->
- [ ] `soar_response` 폴더에 `unit10_final_retrospective.md` 를 만들어 틀을 붙여 넣었다
- [ ] `unit10_final_retrospective.md` 의 1 ~ 3절 `…` 를 모두 채우고(모르는 칸은 `모름 — 막힌 곳: …`) 저장했다
<!-- /checklist -->

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 「보고서 쓰기」와 「오늘의 글 쓰기」까지 마친 뒤 합니다. 이번 Unit은 Module 5의 마지막이라, 오늘 올리면 Module 5에서 만든 SOAR 모듈과 엔진 · 점검 · 회고 문서가 모두 저장소에 남습니다.

**1. 오늘 한 일 확인**

1. 알림 8건을 승인 게이트를 거쳐 조치하고 티켓을 남기며, 오류가 난 알림은 실패로 격리하는 통합 엔진을 만들었다 (실습 5-1)
2. 엔진 로그 세 개를 정책 네 가지로 점검해 FAIL 2개가 `gate_off_log.json` 에서 나오는 것을 확인했다 (실습 5-2)
3. 최종 회고 문서 `unit10_final_retrospective.md` 에 `…` 가 남은 칸이 없다 (실습 5-2)
4. 보고서 `report_u5.md` 의 꼭 채울 다섯 칸(5-1 (가) · (나), 5-2 (가) · (나), 마무리 (가))에 `답:` 뒤가 비어 있지 않다

**강의계획서 평가 기준 확인**

| 기준 | 확인할 곳 |
|---|---|
| Module 4 탐지 결과부터 Module 5 대응까지 오류 없이 이어진다 | `risk_engine_log.json`: Module 4 5건 → 자동 실행 2 · 조치 없음 3 · 실패 0 |
| 승인 게이트가 위험도에 따라 정확히 작동한다 | 실습 5-1 단계 2 · 3, 실습 5-2 점검 ① |
| 모듈이 서로 이어져 하나의 흐름으로 동작한다 | `soar_engine.py` 의 `import` 6줄, 회고 문서 1절 |

- 첫 줄의 연결을 직접 만들어 보려면 응용 5-1(여유가 되면)을 합니다. 응용 5-1 단계 3 ~ 5 가 같은 결과를 보여 줍니다.

**2. 파일 확인** — **[터미널]** `soar_response` 폴더에서 확인합니다.

```bash
pwd
ls
```

- `pwd` 결과가 `…/soar_response` 로 끝나야 합니다.
- `ls` 결과에 아래 파일이 보여야 합니다. 응용 5-1 줄은 응용을 했을 때만 보입니다.

| 만든 곳 | 보여야 할 파일 |
|---|---|
| 시작하기 | `engine_alerts.json` |
| 실습 5-1 | `soar_engine.py` · `exercise5-1_run.py` · `engine_log.json` · `engine_tickets.json` |
| 제공 파일 | `risk_engine_log.json` |
| 실습 5-2 | `gate_off_log.json` · `policy_check.py` · `exercise5-2_run.py` · `policy_check.json` · `unit10_final_retrospective.md` |
| 보고서 쓰기 | `report_u5.md` |
| 응용 5-1(여유가 되면) | `unit05_risk_scores.json` · `engine_input.py` · `apply5-1_run.py` · `engine_summary.json` · `risk_tickets.json` |

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark style="background:#ffc4d6">빨간 목록에 `.env`(API 키가 들어 있는 파일)나 `.venv`(가상환경 폴더)가 보이면 올리지 않고 멈춥니다.</mark>
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.
3. **[보고서]** `report_u5.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`). 세 명령을 하나씩 칩니다.
   ```bash
   git add .
   git commit -m "Add SOAR engine, policy check and Module 5 final retrospective"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).
5. **[브라우저]** 깃허브의 내 저장소 `network-study-notes` 를 새로 고쳐 `soar_response` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.
   - 깃허브에 안 보이는 파일이 있으면 그 파일이 VS Code 왼쪽 목록의 `soar_response` 폴더 안에 있는지 봅니다. 다른 폴더에 만들었다면 `soar_response` 안으로 옮긴 뒤 2번의 `git status` 부터 다시 합니다.

- 시간이 남아 응용 5-1을 했다면 응용 파일까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**확인** — 깃허브의 `soar_response` 폴더에 2번 표의 파일(응용 줄 빼고)이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이는 파일이 있으면 `git status` 를 다시 쳐서 그 파일이 빨간 목록에 남아 있는지 보고 4번을 다시 합니다.

<!-- checklist -->
- [ ] `soar_response` 폴더에서 2번 표의 파일이 모두 있는 것을 확인했다
- [ ] `network-study-notes` 폴더에서 `git status` 를 실행해 `.env` · `.venv` 가 목록에 없는 것을 확인했다
- [ ] `git add .` · `git commit` · `git push` 를 차례로 실행해 깃허브에 올렸다
- [ ] 깃허브의 `network-study-notes` 저장소 `soar_response` 폴더에서 오늘 만든 파일이 모두 보였다
<!-- /checklist -->

**4. 이어지는 곳**

1. Module 5는 여기서 끝납니다. 플레이북 · 계정과 IP 조치 · 티켓 · 승인 게이트 · 통합 엔진이 `soar_response` 폴더에 모두 들어 있습니다.
2. 캡스톤에서는 회고 문서 3절에 적은 주제 · 설정 파일 · 내 파일로 시작합니다. 회고 문서 2절에 적은 깨질 곳은 캡스톤에서 먼저 막을 일의 목록이 됩니다.

---

<!-- learn:answers -->
