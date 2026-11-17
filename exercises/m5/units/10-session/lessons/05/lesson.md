---
id: m5-u10-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/134_day06_am_soar_engine.md
  mission_id: GichanSource.m5-1116-am-soar-engine
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답

아래 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## 정답 2-1

💻 **터미널에 입력합니다.**

```bash
pwd
python day06_2-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`soar_engine.py` 의 1 ~ 8번입니다.

```python
        # 1. count_users_on_ip(alert["entity"], context["ip_users"]) 의 결과를 users_on_ip 에 저장한다
        users_on_ip = count_users_on_ip(alert["entity"], context["ip_users"])  # 그 IP 를 쓰는 계정 수를 센다
        # 2. lock_account(request["target"], state, vip_accounts, request["incident"], ENGINE_REASON) 의 결과를 record 에 저장한다
        record = lock_account(request["target"], state, vip_accounts, request["incident"], ENGINE_REASON)  # 계정을 잠그고 조치 기록을 받는다
        # 3. block_ip(request["target"], state, request["incident"], ENGINE_REASON, DEFAULT_TTL) 의 결과를 record 에 저장한다
        record = block_ip(request["target"], state, request["incident"], ENGINE_REASON, DEFAULT_TTL)  # IP 를 차단하고 조치 기록을 받는다
    # 4. decide_gate(request, context["policy"]) 의 두 결과를 decision, reasons 에 저장한다
    decision, reasons = decide_gate(request, context["policy"])                # 승인 게이트의 결정과 이유 리스트를 함께 받는다
    # 5. decision 이 "자동" 이면 (if, ==)
    if decision == "자동":                                                     # 게이트가 자동으로 정했으면
            # 6. action 이 CONTAINMENT_ACTIONS 안에 있으면 (if, in)
            if action in CONTAINMENT_ACTIONS:                                  # 게이트를 거쳐 실행하는 조치이면
            # 7. run_soar_pipeline(alert, context) 의 결과를 result 에 저장한다
            result = run_soar_pipeline(alert, context)                         # 알림 한 건을 처음부터 끝까지 처리한다
        # 8. 어떤 종류의 오류든 error 에 저장해 받는다 (except, Exception, as)
        except Exception as error:                                             # 어떤 종류의 오류든 error 에 저장해 받는다
```

위 줄만으로는 `if` · `else` · `try` 안에 들어가는 줄이 어느 것인지 알기 어려우니, 미리 채운 줄까지 넣은 네 함수의 완성된 모양을 함께 봅니다.

**전체 모양 — `execute_action`**

```python
def execute_action(request, context):                 # 조치 요청과 엔진 재료를 받는 함수
    """계정 잠금이면 lock_account, IP 차단이면 block_ip 로 조치를 실행하고 조치 기록 한 건을 리턴한다. 승인 게이트가 자동으로 정한 조치를 실제로 실행할 때 쓴다."""
    state = context["state"]                          # 연습용 시스템 상태 — 미리 채운 줄
    vip_accounts = context["policy"]["vip_accounts"]  # VIP 계정 리스트 — 미리 채운 줄
    if request["action"] == "계정 잠금":              # 조치가 계정 잠금이면 — 미리 채운 줄
        record = lock_account(request["target"], state, vip_accounts, request["incident"], ENGINE_REASON)  # 계정을 잠그고 조치 기록을 받는다
    else:                                             # 아니면 IP 차단이다 — 미리 채운 줄
        record = block_ip(request["target"], state, request["incident"], ENGINE_REASON, DEFAULT_TTL)  # IP 를 차단하고 조치 기록을 받는다
    return record                                     # 조치 기록을 리턴한다 — 미리 채운 줄
```

**전체 모양 — `run_step`**

```python
def run_step(alert, action, context):                            # 알림 · 조치 이름 · 엔진 재료를 받는 함수
    """조치 하나를 승인 게이트에 묻고, 자동으로 정해졌을 때만 실행해서 결정 · 이유 · 실행 여부를 담은 딕셔너리를 리턴한다. 조치마다 한 번씩 쓴다."""
    request = make_request(alert, action, context)               # 승인 게이트에 보낼 조치 요청을 만든다 — 미리 채운 줄
    decision, reasons = decide_gate(request, context["policy"])  # 승인 게이트의 결정과 이유 리스트를 함께 받는다
    step = {                                                     # 조치 하나의 결과 : 처음에는 실행하지 않은 것으로 적는다 — 미리 채운 줄
        "action": action,                                        # 조치 이름
        "target": alert["entity"],                               # 조치 대상
        "decision": decision,                                    # 승인 게이트의 결정
        "reasons": reasons,                                      # 결정 이유 리스트
        "executed": False,                                       # 실행했는지
        "before": "",                                            # 조치 전 상태
        "after": "",                                             # 조치 후 상태
        "request": request,                                      # 승인 게이트가 본 조치 요청(나중에 점검할 때 다시 쓴다)
    }
    if decision == "자동":                                       # 게이트가 자동으로 정했으면
        record = execute_action(request, context)                # 조치를 실행하고 조치 기록을 받는다 — 미리 채운 줄
        step["executed"] = True                                  # 실행했다고 적는다 — 미리 채운 줄
        step["before"] = record["before"]                        # 조치 전 상태를 적는다 — 미리 채운 줄
        step["after"] = record["after"]                          # 조치 후 상태를 적는다 — 미리 채운 줄
    return step                                                  # 조치 하나의 결과를 리턴한다 — 미리 채운 줄
```

**전체 모양 — `run_soar_pipeline`**

```python
def run_soar_pipeline(alert, context):                                 # 알림 한 건과 엔진 재료를 받는 함수
    """알림 한 건을 플레이북 찾기 → 조치마다 승인 게이트 → 티켓 만들기 순서로 처리하고 결과 기록 한 건을 리턴한다. 알림마다 한 번씩 쓴다."""
    playbooks = match_playbooks(alert, context["registry"])            # 월요일 함수로 맞는 플레이북을 찾는다 — 미리 채운 줄
    playbook_id = "없음"                                               # 맞는 플레이북이 없으면 「없음」으로 남긴다 — 미리 채운 줄
    steps = []                                                         # 조치마다 결과를 모을 빈 리스트 — 미리 채운 줄
    for playbook in playbooks:                                         # 맞는 플레이북을 하나씩 꺼낸다 — 미리 채운 줄
        playbook_id = playbook["id"]                                   # 플레이북 번호를 적는다 — 미리 채운 줄
        for action in playbook["actions"]:                             # 플레이북의 액션을 하나씩 꺼낸다 — 미리 채운 줄
            if action in CONTAINMENT_ACTIONS:                          # 게이트를 거쳐 실행하는 조치이면
                step = run_step(alert, action, context)                # 승인 게이트를 거쳐 실행한다 — 미리 채운 줄
                steps.append(step)                                     # 조치 결과를 추가한다 — 미리 채운 줄
    outcome = decide_outcome(steps)                                    # 알림 전체의 처리 결과를 정한다 — 미리 채운 줄
    ticket = open_ticket(alert, steps, playbook_id, outcome, context)  # 티켓을 만든다 — 미리 채운 줄
    result = {                                                         # 알림 한 건의 결과 기록 — 미리 채운 줄
        "incident": alert["id"],                                       # 알림 번호
        "entity": alert["entity"],                                     # 대상
        "grade": alert["grade"],                                       # 등급
        "playbook": playbook_id,                                       # 플레이북 번호
        "outcome": outcome,                                            # 처리 결과
        "steps": steps,                                                # 조치마다 결과 리스트
        "ticket": ticket["id"],                                        # 티켓 번호
        "error": "",                                                   # 오류 문장 : 정상이면 비어 있다
    }
    return result                                                      # 결과 기록을 리턴한다 — 미리 채운 줄
```

**전체 모양 — `run_all`**

```python
def run_all(alerts, context):                           # 알림 리스트와 엔진 재료를 받는 함수
    """알림을 하나씩 처리하되, 오류가 난 알림은 실패 기록만 남기고 다음 알림으로 넘어간다. 알림 하나의 오류가 나머지 알림의 처리를 막지 않게 할 때 쓴다."""
    results = []                                        # 알림마다 결과 기록을 모을 빈 리스트 — 미리 채운 줄
    for alert in alerts:                                # 알림을 하나씩 꺼낸다 — 미리 채운 줄
        try:                                            # 오류가 날 수 있는 처리를 시작한다 — 미리 채운 줄
            result = run_soar_pipeline(alert, context)  # 알림 한 건을 처음부터 끝까지 처리한다
        except Exception as error:                      # 어떤 종류의 오류든 error 에 저장해 받는다
            result = make_failure_result(alert, error)  # 실패 기록을 만든다 — 미리 채운 줄
        results.append(result)                          # 정상 결과든 실패 기록이든 결과 리스트에 추가한다 — 미리 채운 줄
    return results                                      # 결과 기록 리스트를 리턴한다 — 미리 채운 줄
```

`day06_2-1_run.py` 의 9번입니다.

```python
    # 9. counts[outcome] 에 counts[outcome] + 1 을 저장한다 (1 늘린다)
    counts[outcome] = counts[outcome] + 1  # 이 처리 결과의 알림 수를 1 늘린다
```

**결과**

- (가) 출력은 다음과 같습니다. 자동 실행 <mark style="background:#bde3ff">**2건**</mark> · 승인 대기 <mark style="background:#bde3ff">**2건**</mark> · 차단 금지 <mark style="background:#bde3ff">**1건**</mark> · 조치 없음 <mark style="background:#bde3ff">**2건**</mark> · 실패 <mark style="background:#bde3ff">**1건**</mark>이고, 승인 대기는 <mark style="background:#bde3ff">`INC-405` · `INC-406`</mark> 입니다.

```
--- 단계 1: 불러온 알림 8 건 · 플레이북 3 개 · 승인 기준 3 점
--- 단계 2: 알림마다 처리 결과
INC-401 dami high → 자동 실행 · PB-001 · 티켓 TCK-1
    계정 잠금 dami → 자동 · 등급 high +2, 합계 2점
    실행: 잠기지 않음 → 잠김
INC-402 hana → 실패 · KeyError: 'grade'
INC-403 198.51.100.45 low → 자동 실행 · PB-003 · 티켓 TCK-2
    IP 차단 198.51.100.45 → 자동 · 등급 low +0, 합계 0점
    실행: 차단되지 않음 → 차단됨
INC-404 203.0.113.80 high → 차단 금지 · PB-003 · 티켓 TCK-3
    IP 차단 203.0.113.80 → 차단 금지 · 허용 목록 대상
INC-405 192.0.2.41 mid → 승인 대기 · PB-003 · 티켓 TCK-4
    IP 차단 192.0.2.41 → 승인 필요 · 등급 mid +1, 함께 쓰는 IP +2, 합계 3점
INC-406 gaeun high → 승인 대기 · PB-001 · 티켓 TCK-5
    계정 잠금 gaeun → 승인 필요 · 등급 high +2, VIP 계정 +3, 합계 5점
INC-407 seoyeon mid → 조치 없음 · PB-002 · 티켓 TCK-6
INC-408 jiwoo mid → 조치 없음 · 없음 · 티켓 TCK-7
--- 단계 3: 처리 결과별 알림 수
자동 실행 : 2 건
승인 대기 : 2 건
차단 금지 : 1 건
조치 없음 : 2 건
실패 : 1 건
--- 단계 4: engine_log.json 에 8 건 · engine_tickets.json 에 티켓 7 장 저장
```

- (나) `INC-402` 는 `grade` 키가 없어서 `match_playbooks` 가 `incident["grade"]` 를 읽을 때 <mark style="background:#bde3ff">`KeyError: 'grade'`</mark> 가 납니다. `run_all` 의 `except Exception as error` 가 그 오류를 받고 `make_failure_result` 가 오류 이름과 내용을 기록하므로, 엔진은 `INC-403` 부터 계속 처리합니다.
  - `try` / `except` 가 없으면 오류가 `run_all` 밖으로 나와 프로그램이 멈춥니다. <mark style="background:#ffc4d6">단계 2 이후가 출력되지 않고, 로그와 티켓 파일도 저장되지 않으며, `INC-403` ~ `INC-408` 6건이 처리되지 않습니다.</mark> `INC-401` 은 이미 `dami` 를 잠갔는데 그 기록이 남지 않습니다. 아래는 `run_all` 에서 `try` / `except` 를 뺀 채 실행한 결과입니다.

```
KeyError: 'grade'
```

- (다) `INC-404` 의 `203.0.113.80` 은 허용 목록에 있어서 `decide_gate` 가 점수를 보지 않고 「차단 금지」로 정합니다. `INC-406` 의 `gaeun` 은 VIP 라서 <mark style="background:#bde3ff">등급 high +2 와 VIP +3 을 더한 합계 5점</mark>이 승인 기준(3점) 이상이라 「승인 필요」입니다.
  - 허용 목록은 점수와 상관없이 실행하지 않는 대상이고, VIP 는 점수로 사람의 승인을 받는 대상이라 결과가 다릅니다.
  - 조치를 실행한 뒤에는 이미 잠기거나 차단된 계정과 IP 가 업무를 막을 수 있어서, <mark>승인 게이트는 `execute_action` 보다 먼저 판단해야 합니다.</mark> 아래 「자주 틀리는 곳」의 5번처럼 순서나 조건이 거꾸로 되면 허용 목록 IP 가 차단됩니다.

**왜**

- <mark>엔진은 「실행하기 전에 정책으로 막고, 실행한 뒤에는 기록을 남기고, 오류는 알림 한 건에 한정한다」는 순서입니다.</mark> 승인 게이트를 엔진 안에 고정하면 사람이 함수를 직접 호출하면서 게이트를 건너뛰는 실수를 막을 수 있습니다. 오류를 알림 한 건에 한정하면 한 건의 문제가 나머지 알림의 처리를 멈추지 않습니다. 대신 코드의 실수도 실패로 나타나므로(아래 4번), 실패 건수를 매번 확인해야 합니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 비우고 실행한 것입니다(비운 줄의 주석은 남겨 둔 상태입니다).

- 1번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. 2번 · 3번 · 7번을 비워도 같은 오류가 납니다(`if` · `else` · `try` 아래가 빕니다). 파이썬 버전에 따라 뒤에 `after 'if' statement on line …` 같은 설명이 붙습니다.

```
IndentationError: expected an indented block
```

- 4번을 비워 두면 프로그램은 멈추지 않지만 <mark style="background:#ffc4d6">**조치를 처리하는 알림이 모두 실패로 나옵니다.**</mark> `except Exception` 이 코드의 실수까지 받아서 알림마다 실패로 적기 때문입니다. 단계 2 에 `INC-401` 의 실패와 단계 3 의 `실패 : 6 건` 이 나오는 것이 이 실수의 결과입니다.

```
INC-401 dami → 실패 · NameError: name 'decision' is not defined
실패 : 6 건
```

- 5번을 비워 두면 그 아래 미리 채운 줄이 앞줄보다 들여써져 있어 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- 5번에서 `==` 대신 `!=` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**자동이 아닌 조치가 실행됩니다.**</mark> 허용 목록 IP(`INC-404`)가 차단되고, 자동이어야 하는 `dami` 는 잠기지 않습니다. 게이트가 「차단 금지」라고 적었어도 실행 줄이 같이 나오는 것이 이 실수의 결과입니다. 아래는 관련 알림만 발췌한 출력입니다.

```
INC-401 dami high → 자동 실행 · PB-001 · 티켓 TCK-1
    계정 잠금 dami → 자동 · 등급 high +2, 합계 2점
INC-404 203.0.113.80 high → 차단 금지 · PB-003 · 티켓 TCK-3
    IP 차단 203.0.113.80 → 차단 금지 · 허용 목록 대상
    실행: 차단되지 않음 → 차단됨
INC-406 gaeun high → 승인 대기 · PB-001 · 티켓 TCK-5
    계정 잠금 gaeun → 승인 필요 · 등급 high +2, VIP 계정 +3, 합계 5점
    실행: 변경 없음 → 변경 없음
```

- 6번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**`티켓 생성` · `담당자 알림` 까지 조치로 취급돼 `dami` · `seoyeon` 이라는 이름이 IP 로 차단됩니다.**</mark> 계정 이름을 IP 차단 함수에 넣은 결과입니다.

```
INC-401 dami high → 자동 실행 · PB-001 · 티켓 TCK-1
    계정 잠금 dami → 자동 · 등급 high +2, 합계 2점
    실행: 잠기지 않음 → 잠김
    티켓 생성 dami → 자동 · 등급 high +2, 합계 2점
    실행: 차단되지 않음 → 차단됨
INC-407 seoyeon mid → 자동 실행 · PB-002 · 티켓 TCK-6
    담당자 알림 seoyeon → 자동 · 등급 mid +1, 합계 1점
    실행: 차단되지 않음 → 차단됨
    티켓 생성 seoyeon → 자동 · 등급 mid +1, 합계 1점
    실행: 차단되지 않음 → 차단됨
```

- 8번을 비워 두면 `try` 만 있고 `except` 가 없어서 실행하기 전에 멈춥니다. 파이썬 3.10 이상에서는 `SyntaxError: expected 'except' or 'finally' block` 문구로 나옵니다.

```
SyntaxError: invalid syntax
```

- 9번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**처리 결과별 알림 수가 모두 0건으로 나옵니다.**</mark> 단계 2 의 알림은 정상으로 나오는데 단계 3 만 틀립니다.

```
--- 단계 3: 처리 결과별 알림 수
자동 실행 : 0 건
승인 대기 : 0 건
차단 금지 : 0 건
조치 없음 : 0 건
실패 : 0 건
```

**관제에서는**

- 알림 하나의 오류가 전체 처리를 멈추지 않게 하는 방식은 SOAR 에서 흔히 쓰는 설계입니다. 다만 오류를 받은 뒤에는 <mark>실패 건수를 모니터링하고 실패한 알림을 담당자에게 넘기는 절차</mark>를 함께 둬야 실패가 확인되지 않은 채 남지 않습니다. 오늘의 처리 결과 다섯 가지 이름은 이 수업에서 정한 것입니다.

---

## 정답 3-1

💻 **터미널에 입력합니다.**

```bash
pwd
python day06_3-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`engine_input.py` 의 1 ~ 8번입니다.

```python
        # 1. key 가 record 안에 없으면 (if, not in)
        if key not in record:                                  # 필수 키가 기록에 없으면
    # 2. record["grade"] 가 GRADES 안에 없으면 (if, not in)
    if record["grade"] not in GRADES:                          # 등급 이름을 엔진이 모르면
    # 3. "INC-" 뒤에 str(number) 를 이어 붙여 alert_id 에 저장한다
    alert_id = "INC-" + str(number)                            # 번호 앞에 INC- 를 붙인다
    # 4. 키 "id"(alert_id) · "entity" · "grade" · "score" · "reasons"(record 의 같은 이름 키의 값), "status"("탐지됨") 를 가진 딕셔너리를 alert 에 저장한다
    alert = {                                                  # 엔진이 읽는 알림 딕셔너리
        "id": alert_id,                                        # 알림 번호
        "entity": record["entity"],                            # 대상
        "grade": record["grade"],                              # 등급
        "score": record["score"],                              # 점수
        "reasons": record["reasons"],                          # 탐지된 규칙 이름 리스트
        "status": "탐지됨",                                    # 처음 상태
    }
        # 5. find_schema_problem(record) 의 결과를 problem 에 저장한다
        problem = find_schema_problem(record)                  # 모양 점검 결과를 받는다
        # 6. problem 이 "" 이면 (if, ==)
        if problem == "":                                      # 문제가 없으면
        # 7. outcome_counts[outcome] 에 outcome_counts[outcome] + 1 을 저장한다 (1 늘린다)
        outcome_counts[outcome] = outcome_counts[outcome] + 1  # 이 처리 결과의 알림 수를 1 늘린다
            # 8. step["executed"] 가 참이면 (if)
            if step["executed"]:                               # 실행한 조치이면
```

위 줄만으로는 `if` 안에 들어가는 줄이 어느 것인지 알기 어려우니, 미리 채운 줄까지 넣은 세 함수의 완성된 모양을 함께 봅니다.

**전체 모양 — `find_schema_problem`**

```python
def find_schema_problem(record):                      # 4과목 결과 기록 한 건을 받는 함수
    """엔진이 읽을 수 없는 기록이면 그 이유 문장을, 문제가 없으면 빈 문자열("")를 리턴한다. 4과목 파일의 모양이 바뀌었을 때 엔진이 오류를 내기 전에 걸러 낼 때 쓴다."""
    for key in REQUIRED_KEYS:                         # 필수 키를 하나씩 꺼낸다 — 미리 채운 줄
        if key not in record:                         # 필수 키가 기록에 없으면
            return "필수 키 없음: " + key             # 어떤 키가 없는지 이유로 리턴한다 — 미리 채운 줄
    if record["grade"] not in GRADES:                 # 등급 이름을 엔진이 모르면
        return "알 수 없는 등급: " + record["grade"]  # 등급 이름을 이유로 리턴한다 — 미리 채운 줄
    if record["reasons"] == []:                       # 탐지된 규칙 리스트가 비어 있으면 — 미리 채운 줄
        return "탐지된 규칙이 없음"                   # 이유를 리턴한다 — 미리 채운 줄
    return ""                                         # 문제가 없으면 빈 문자열를 리턴한다 — 미리 채운 줄
```

**전체 모양 — `split_records`**

```python
def split_records(records):                                          # 4과목 결과 기록 리스트를 받는 함수
    """기록마다 모양을 점검해 엔진에 넣을 알림 리스트와 거절한 기록 리스트를 만들고 두 리스트를 함께 리턴한다. 거절한 기록을 이유와 함께 남겨 기록 없이 빠지지 않게 할 때 쓴다."""
    alerts = []                                                      # 엔진에 넣을 알림을 모을 빈 리스트 — 미리 채운 줄
    rejected = []                                                    # 거절한 기록과 이유를 모을 빈 리스트 — 미리 채운 줄
    number = FIRST_NUMBER                                            # 다음에 붙일 알림 번호 — 미리 채운 줄
    for record in records:                                           # 기록을 하나씩 꺼낸다 — 미리 채운 줄
        problem = find_schema_problem(record)                        # 모양 점검 결과를 받는다
        if problem == "":                                            # 문제가 없으면
            alert = make_alert(record, number)                       # 알림 모양으로 바꾼다 — 미리 채운 줄
            alerts.append(alert)                                     # 알림 리스트에 추가한다 — 미리 채운 줄
            number = number + 1                                      # 다음 번호로 넘어간다 — 미리 채운 줄
        else:                                                        # 문제가 있으면 — 미리 채운 줄
            rejected.append({"record": record, "problem": problem})  # 기록과 이유를 거절 리스트에 추가한다 — 미리 채운 줄
    return alerts, rejected                                          # 두 리스트를 함께 리턴한다 — 미리 채운 줄
```

**전체 모양 — `summarize`**

```python
def summarize(results):                                        # 엔진 결과 기록 리스트를 받는 함수
    """결과 기록을 모아 처리 결과별 알림 수 · 만든 티켓 수 · 실제로 실행한 조치 문장 리스트를 담은 요약 딕셔너리를 리턴한다. 운영 담당자가 한 번에 볼 요약이 필요할 때 쓴다."""
    outcome_counts = {"자동 실행": 0, "승인 대기": 0, "차단 금지": 0, "조치 없음": 0, "실패": 0}  # 처리 결과마다 알림 수 : 처음에는 모두 0 — 미리 채운 줄
    ticket_count = 0                                           # 만든 티켓 수 : 처음에는 0 — 미리 채운 줄
    executed_actions = []                                      # 실제로 실행한 조치 문장을 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                     # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        outcome = result["outcome"]                            # 이 알림의 처리 결과 — 미리 채운 줄
        outcome_counts[outcome] = outcome_counts[outcome] + 1  # 이 처리 결과의 알림 수를 1 늘린다
        if result["ticket"] != "":                             # 티켓이 있으면 — 미리 채운 줄
            ticket_count = ticket_count + 1                    # 티켓 수를 1 늘린다 — 미리 채운 줄
        for step in result["steps"]:                           # 조치 결과를 하나씩 꺼낸다 — 미리 채운 줄
            if step["executed"]:                               # 실행한 조치이면
                action_text = result["incident"] + " " + step["action"] + " " + step["target"] + ": " + step["before"] + " → " + step["after"]  # 알림 · 조치 · 대상 · 전 · 후 상태를 한 문장으로 만든다 — 미리 채운 줄
                executed_actions.append(action_text)           # 문장을 추가한다 — 미리 채운 줄
    summary = {"outcome_counts": outcome_counts, "ticket_count": ticket_count, "executed_actions": executed_actions}  # 요약 딕셔너리 — 미리 채운 줄
    return summary                                             # 요약을 리턴한다 — 미리 채운 줄
```

`day06_3-1_run.py` 의 9번입니다.

```python
# 9. run_all(alerts, context) 의 결과를 results 에 저장한다
results = run_all(alerts, context)  # 알림을 하나씩 엔진으로 처리한다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 5 의 처리 결과는 자동 실행 <mark style="background:#bde3ff">**2건**</mark> · 승인 대기 <mark style="background:#bde3ff">**0건**</mark> · 차단 금지 <mark style="background:#bde3ff">**0건**</mark> · 조치 없음 <mark style="background:#bde3ff">**3건**</mark> · 실패 <mark style="background:#bde3ff">**0건**</mark>이고, 실제로 실행한 조치는 <mark style="background:#bde3ff">`INC-501` 의 `dami` 계정 잠금 · `INC-505` 의 `198.51.100.90` 차단</mark>입니다.

```
--- 단계 1: 4과목 탐지 결과 5 건
--- 단계 2: 모양 점검 시험 (일부러 틀린 기록)
hana → 필수 키 없음: grade
minsu → 알 수 없는 등급: critical
--- 단계 3: 엔진에 넣을 알림 5 건 · 거절한 기록 0 건
INC-501 dami high 60 ['퇴사한 계정']
INC-502 seoyeon mid 45 ['평소와 다른 IP', '대량 다운로드']
INC-503 gaeun mid 40 ['규칙은 허용인데 서버가 거절', '여러 로그 연결']
INC-504 jiwoo mid 35 ['업무 시간 밖 로그인', '평소와 다른 IP']
INC-505 198.51.100.90 low 30 ['경로 스캔']
--- 단계 4: 엔진 처리 결과
INC-501 dami → 자동 실행 · PB-001 · 티켓 TCK-1
INC-502 seoyeon → 조치 없음 · PB-002 · 티켓 TCK-2
INC-503 gaeun → 조치 없음 · 없음 · 티켓 TCK-3
INC-504 jiwoo → 조치 없음 · 없음 · 티켓 TCK-4
INC-505 198.51.100.90 → 자동 실행 · PB-003 · 티켓 TCK-5
--- 단계 5: 운영 요약
자동 실행 2 건 · 승인 대기 0 건 · 차단 금지 0 건 · 조치 없음 3 건 · 실패 0 건
티켓 5 건 · 실제로 실행한 조치 2 건
INC-501 계정 잠금 dami: 잠기지 않음 → 잠김
INC-505 IP 차단 198.51.100.90: 차단되지 않음 → 차단됨
--- 단계 6: risk_engine_log.json · engine_summary.json · risk_tickets.json 저장
```

- (나) `seoyeon`(`INC-502`)은 플레이북 `PB-002`(대량 다운로드)가 맞지만, 그 플레이북의 액션이 `담당자 알림` · `티켓 생성` 뿐이라 승인 게이트를 거칠 조치(계정 잠금 · IP 차단)가 없습니다. `gaeun`(`INC-503`)과 `jiwoo`(`INC-504`)는 단계 4 의 플레이북 번호가 <mark style="background:#bde3ff">「없음」</mark>입니다. 월요일 플레이북 3개의 트리거 규칙은 퇴사한 계정 · 대량 다운로드 · 경로 스캔이고, 두 대상의 이유(`규칙은 허용인데 서버가 거절` · `여러 로그 연결` / `업무 시간 밖 로그인` · `평소와 다른 IP`)는 그 규칙에 없기 때문입니다.
  - 티켓이 없으면 세 알림은 엔진이 한 일도 남은 기록도 없어서 담당자가 알 방법이 없습니다. <mark style="background:#ffc4d6">티켓이 조치 없는 알림을 사람에게 넘기는 유일한 경로입니다.</mark> 세 알림의 티켓(`TCK-2` ~ `TCK-4`)에는 다음 할 일로 「자동 조치가 없는 알림이니 직접 보고 조치가 필요한지 정한다」가 적힙니다.
- (다) `minsu` 기록은 등급이 `critical` 이라 엔진이 아는 등급(`GRADES`: high · mid · low)에 없어서 <mark style="background:#bde3ff">`알 수 없는 등급: critical`</mark> 로 거절됩니다. 거절하면 거절 리스트에 이유가 남아 4과목 쪽을 고칠 수 있습니다.
  - 거절 없이 엔진에 넣으면 `match_playbooks` 가 `GRADE_ORDER["critical"]` 을 찾다가 오류를 내고, 2교시 `INC-402` 처럼 그 알림만 실패로 기록됩니다. 조치도 티켓도 없고 원인은 오류 문장에만 남습니다. 아래는 그렇게 실행한 결과입니다.

```
실패 · KeyError: 'critical'
```

**왜**

- <mark>입력 검증은 엔진이 오류를 내기 전에 문제를 이유와 함께 남기고, 오류 격리는 걸러지지 않은 문제를 알림 한 건에 한정합니다.</mark> 둘 중 하나만 있으면 잘못된 기록이 조치도 티켓도 없이 사라지거나, 엔진이 멈춥니다. 운영 요약은 처리 결과를 한 장으로 모아, 근무 인계와 보고에서 「무엇을 실행했고 무엇이 사람에게 남았는지」를 바로 알게 합니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 비우고 실행한 것입니다(비운 줄의 주석은 남겨 둔 상태입니다).

- 1번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**모든 기록이 「필수 키 없음: entity」로 거절됩니다.**</mark> `return` 줄이 `if` 없이 첫 번째 키에서 바로 실행되기 때문입니다. 4과목 기록 5건이 모두 거절되어 엔진에 넣을 알림이 0건입니다.

```
hana → 필수 키 없음: entity
minsu → 필수 키 없음: entity
--- 단계 3: 엔진에 넣을 알림 0 건 · 거절한 기록 5 건
```

- 2번을 비워 두면 `return` 줄이 `for` 안쪽에서 실행되어, 첫 번째 키만 보고 `record["grade"]` 를 읽다가 `grade` 키가 없는 시험 기록에서 오류가 납니다.

```
KeyError: 'grade'
```

- 2번에서 `not in` 대신 `in` 을 쓰면 오류 없이 <mark style="background:#ffc4d6">**엔진이 아는 등급(high · mid · low)이 모두 거절됩니다.**</mark> 단계 3 에서 엔진에 넣을 알림이 0건입니다.

```
--- 단계 3: 엔진에 넣을 알림 0 건 · 거절한 기록 5 건
```

- 3번을 비워 두면 `alert_id` 를 만들지 못해 오류가 납니다. 4번을 비우면 `alert` 가 만들어지지 않아 `return alert` 에서 오류가 나고, 5번을 비우면 `problem` 이 만들어지지 않아 오류가 납니다.

```
NameError: name 'alert_id' is not defined
```

```
NameError: name 'alert' is not defined
```

```
NameError: name 'problem' is not defined
```

- 6번을 비워 두면 그 아래 미리 채운 줄이 앞줄보다 들여써져 있어 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- 7번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**처리 결과별 알림 수가 모두 0건으로 나옵니다.**</mark> 티켓 수와 실행한 조치는 정상입니다.

```
--- 단계 5: 운영 요약
자동 실행 0 건 · 승인 대기 0 건 · 차단 금지 0 건 · 조치 없음 0 건 · 실패 0 건
티켓 5 건 · 실제로 실행한 조치 2 건
INC-501 계정 잠금 dami: 잠기지 않음 → 잠김
INC-505 IP 차단 198.51.100.90: 차단되지 않음 → 차단됨
```

- 8번을 비워 두면 오류는 나지 않고 출력도 정답과 같습니다. 오늘 샘플은 조치가 모두 실행된 것이라 `if` 가 없어도 같은 결과가 나옵니다. <mark style="background:#ffc4d6">**승인 대기 · 차단 금지 알림이 있는 결과에서는 실행하지 않은 조치까지 「실행한 조치」에 들어갑니다.**</mark> 출력이 맞아도 코드를 다시 읽어 확인합니다.
- 9번을 비워 두면 `results` 가 만들어지지 않아 오류가 납니다.

```
NameError: name 'results' is not defined
```

**관제에서는**

- 탐지와 대응은 다른 팀이나 다른 제품이 만드는 경우가 많아서 데이터 모양이 어긋나기 쉽습니다. 둘 사이에 입력 검증을 두고 <mark>거절한 기록 수를 모니터링</mark>하면, 거절이 갑자기 늘었을 때 상류의 형식이 바뀐 것을 알 수 있습니다. 오늘의 필수 키 네 개와 등급 세 가지는 이 수업의 공통 스키마입니다.

---

## 정답 4-1

💻 **터미널에 입력합니다.**

```bash
pwd
python day06_4-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`policy_check.py` 의 1 ~ 6번입니다.

```python
            # 1. decide_gate(step["request"], policy) 의 두 결과를 new_decision, new_reasons 에 저장한다
            new_decision, new_reasons = decide_gate(step["request"], policy)   # 저장된 조치 요청으로 게이트의 결정을 다시 구한다
            # 2. new_decision 이 "자동" 이 아니고(and) step["executed"] 가 참이면 (if, !=, and)
            if new_decision != "자동" and step["executed"]:                    # 다시 구한 결정이 자동이 아닌데 실행했으면
            # 3. step["target"] 이 allowlist_ips 안에 있고(and) step["after"] 가 "차단됨" 이면 (if, in, ==, and)
            if step["target"] in allowlist_ips and step["after"] == "차단됨":  # 허용 목록 IP 가 차단되었으면
            # 4. step["target"] 이 vip_accounts 안에 있고(and) step["after"] 가 "잠김" 이면 (if, in, ==, and)
            if step["target"] in vip_accounts and step["after"] == "잠김":     # VIP 계정이 잠겼으면
        # 5. executed_count 가 0 보다 크고(and) result["ticket"] 이 "" 이면 (if, >, ==, and)
        if executed_count > 0 and result["ticket"] == "":                      # 실행한 조치가 있는데 티켓이 없으면
    # 6. violations 가 빈 리스트 [] 이면 (if, ==)
    if violations == []:                                                       # 위반이 없으면
```

위 줄만으로는 `if` 안에 들어가는 줄이 어느 것인지 알기 어려우니, 미리 채운 줄까지 넣은 두 함수의 완성된 모양을 함께 봅니다. 3 · 4 · 5번도 `if` 아래의 미리 채운 `violations.append(…)` 줄이 `if` 안쪽입니다.

**전체 모양 — `find_gate_bypass`**

```python
def find_gate_bypass(results, policy):                                        # 결과 기록 리스트와 승인 정책을 받는 함수
    """저장된 조치 요청으로 승인 게이트의 결정을 다시 구해, 자동이 아닌데 실행된 조치가 있는 알림 번호를 리스트로 리턴한다. 게이트를 거치지 않았거나 결정을 바꿔 쓴 실행을 찾을 때 쓴다."""
    violations = []                                                           # 위반한 알림 번호를 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                                    # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        for step in result["steps"]:                                          # 조치 결과를 하나씩 꺼낸다 — 미리 채운 줄
            new_decision, new_reasons = decide_gate(step["request"], policy)  # 저장된 조치 요청으로 게이트의 결정을 다시 구한다
            if new_decision != "자동" and step["executed"]:                   # 다시 구한 결정이 자동이 아닌데 실행했으면
                violations.append(result["incident"])                         # 알림 번호를 위반 리스트에 추가한다 — 미리 채운 줄
    return violations                                                         # 위반한 알림 번호 리스트를 리턴한다 — 미리 채운 줄
```

**전체 모양 — `judge`**

```python
def judge(violations):    # 위반한 알림 번호 리스트를 받는 함수
    """위반이 하나도 없으면 「PASS」, 하나라도 있으면 「FAIL」을 리턴한다. 점검 결과를 한눈에 보이게 출력할 때 쓴다."""
    if violations == []:  # 위반이 없으면
        return "PASS"     # 위반이 없으면 PASS 를 리턴한다 — 미리 채운 줄
    return "FAIL"         # 위반이 있으면 FAIL 을 리턴한다 — 미리 채운 줄
```

`day06_4-1_run.py` 의 7 ~ 9번입니다. 8번 아래 미리 채운 `fail_count` 줄이 `if` 안쪽입니다.

```python
    # 7. load_json(log_path) 의 결과를 results 에 저장한다
    results = load_json(log_path)  # 로그 파일을 리스트로 읽는다
        # 8. verdict 가 "FAIL" 이면 (if, ==)
        if verdict == "FAIL":      # 점검에 실패했으면
# 9. rows 를 CHECK_PATH 파일에 저장한다 (save_json)
save_json(rows, CHECK_PATH)        # 점검 결과를 파일에 저장한다
```

**결과**

- (가) 출력은 다음과 같습니다. FAIL 이 나온 로그는 <mark style="background:#bde3ff">`gate_off_log.json`</mark> 하나이고, FAIL 점검은 <mark style="background:#bde3ff">게이트 우회 실행(`INC-404` · `INC-405` · `INC-406`)과 허용 목록 IP 차단(`INC-404`)</mark> 두 개입니다.

```
--- 단계 1: 점검할 로그 3 개 · 점검 4가지
--- 단계 2: 로그마다 점검 결과
[engine_log.json] 알림 8 건
   게이트 우회 실행 : PASS · 위반 0 건 []
   허용 목록 IP 차단 : PASS · 위반 0 건 []
   VIP 계정 잠금 : PASS · 위반 0 건 []
   티켓 없는 조치 : PASS · 위반 0 건 []
[risk_engine_log.json] 알림 5 건
   게이트 우회 실행 : PASS · 위반 0 건 []
   허용 목록 IP 차단 : PASS · 위반 0 건 []
   VIP 계정 잠금 : PASS · 위반 0 건 []
   티켓 없는 조치 : PASS · 위반 0 건 []
[gate_off_log.json] 알림 5 건
   게이트 우회 실행 : FAIL · 위반 3 건 ['INC-404', 'INC-405', 'INC-406']
   허용 목록 IP 차단 : FAIL · 위반 1 건 ['INC-404']
   VIP 계정 잠금 : PASS · 위반 0 건 []
   티켓 없는 조치 : PASS · 위반 0 건 []
--- 단계 3: FAIL 이 나온 점검 2 개 · 전체 점검 12 개
--- 단계 4: policy_check.json 에 12 개 저장
```

- (나) `INC-405` 의 `request` 는 등급 mid 에 `users_on_ip` 가 2 입니다. 승인 정책에서 mid <mark style="background:#ffdcb0">1점</mark>과 함께 쓰는 IP(2개 이상) <mark style="background:#ffdcb0">2점</mark>을 더한 <mark style="background:#bde3ff">합계 3점</mark>이 `approval_score`(3점) 이상이라, `decide_gate` 를 다시 호출하면 「승인 필요」입니다. 그런데 `executed` 가 참이라서 위반입니다.
  - 로그의 `decision` 은 게이트를 끈 엔진이 적은 값(「자동」, 이유 「승인 게이트 끔」)이라 <mark style="background:#ffc4d6">`decision` 만 읽으면 위반이 보이지 않습니다.</mark> 저장된 입력(`request`)으로 다시 구해야 엔진이 적은 값과 상관없이 확인할 수 있습니다.
- (다) `INC-406` 은 `before` 와 `after` 가 모두 <mark style="background:#bde3ff">「변경 없음」</mark>입니다. 수요일의 `lock_account` 가 VIP 계정(`gaeun`)이면 잠그지 않고 「VIP 계정이라 자동 조치 대상이 아님」을 기록하기 때문에 `gaeun` 은 잠기지 않았습니다. 점검 ①은 그래도 조치 함수를 호출한 것(`executed`)이라서 FAIL 입니다.
  - 점검 ③은 게이트나 `lock_account` 와 별도로 결과(`after`)만 봅니다. `lock_account` 에 VIP 리스트를 잘못 전달하거나 함수가 바뀌면 같은 로그에서도 VIP 가 잠길 수 있는데, 그때는 ③이 FAIL 로 잡습니다. <mark>한 겹의 통제가 깨져도 다른 겹의 점검이 잡도록 각각 점검합니다.</mark>

**왜**

- <mark>통제는 만들어 두는 것만으로는 부족하고, 작동했다는 증거를 로그로 확인해야 합니다.</mark> ①은 재수행으로 엔진이 적은 값을 믿지 않고, ②③은 불변 조건으로 게이트의 계산과 무관하게 결과를 봅니다. 점검을 코드로 만들어 두면 알림이 늘어도 같은 방식으로 반복해서 확인할 수 있습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 비우고 실행한 것입니다(비운 줄의 주석은 남겨 둔 상태입니다).

- 1번을 비워 두면 `new_decision` 을 만들지 못해 오류가 납니다.

```
NameError: name 'new_decision' is not defined
```

- 2번 · 5번 · 6번 · 8번을 비워 두면 그 아래 미리 채운 줄이 앞줄보다 들여써져 있어 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- 2번에서 `!=` 대신 `==` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**정상인 로그에서 위반이 나옵니다.**</mark> 자동으로 정해져 실행한 `INC-401` · `INC-403` 이 게이트 우회로 나옵니다. 아래는 첫 번째 로그의 결과입니다.

```
[engine_log.json] 알림 8 건
   게이트 우회 실행 : FAIL · 위반 2 건 ['INC-401', 'INC-403']
   허용 목록 IP 차단 : PASS · 위반 0 건 []
   VIP 계정 잠금 : PASS · 위반 0 건 []
   티켓 없는 조치 : PASS · 위반 0 건 []
```

- 3번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**조치 요청이 있는 알림이 모두 위반으로 나옵니다.**</mark> `if` 가 없어서 조건과 상관없이 `append` 가 실행되기 때문입니다. 4번을 비워도 같은 꼴이 점검 ③에 나타납니다.

```
[engine_log.json] 알림 8 건
   게이트 우회 실행 : PASS · 위반 0 건 []
   허용 목록 IP 차단 : FAIL · 위반 5 건 ['INC-401', 'INC-403', 'INC-404', 'INC-405', 'INC-406']
   VIP 계정 잠금 : PASS · 위반 0 건 []
   티켓 없는 조치 : PASS · 위반 0 건 []
```

- 3번에서 `and step["after"] == "차단됨"` 을 빠뜨리면 오류 없이 <mark style="background:#ffc4d6">**차단하지 않은 알림도 위반으로 나옵니다.**</mark> `INC-404` 는 허용 목록 IP 라서 승인 게이트가 차단 금지로 막았는데도 위반입니다. 허용 목록에 있는지만 보고 실제로 차단됐는지는 보지 않았기 때문입니다.

```
[engine_log.json] 알림 8 건
   게이트 우회 실행 : PASS · 위반 0 건 []
   허용 목록 IP 차단 : FAIL · 위반 1 건 ['INC-404']
   VIP 계정 잠금 : PASS · 위반 0 건 []
   티켓 없는 조치 : PASS · 위반 0 건 []
```

- 6번에서 `==` 대신 `!=` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**위반이 없는 점검이 모두 FAIL 로 나옵니다.**</mark> 판정이 거꾸로 되어, 위반이 있는 로그(승인 게이트를 끈 로그)가 PASS 가 됩니다.

```
[engine_log.json] 알림 8 건
   게이트 우회 실행 : FAIL · 위반 0 건 []
   허용 목록 IP 차단 : FAIL · 위반 0 건 []
   VIP 계정 잠금 : FAIL · 위반 0 건 []
   티켓 없는 조치 : FAIL · 위반 0 건 []
```

- 7번을 비워 두면 `results` 가 만들어지지 않아 오류가 납니다.

```
NameError: name 'results' is not defined
```

- 9번을 비워 두면 오류 없이 화면에는 저장했다고 나오지만 <mark style="background:#ffc4d6">**`policy_check.json` 파일이 만들어지지 않습니다.**</mark> 실행한 뒤 `ls` 로 파일이 생겼는지 확인합니다.

```
--- 단계 4: policy_check.json 에 12 개 저장
```

**관제에서는**

- 자동화가 정책대로 동작했는지는 사람이 가끔 읽는 것으로 확인하지 않고, 같은 점검을 로그에 정기적으로 실행해서 확인합니다. 점검에서 FAIL 이 나오면 위반한 알림 번호로 원인을 찾고 담당자에게 알립니다. 승인 게이트를 끈 시험 운영 로그처럼 <mark>통제를 일부러 끈 기록이 운영에 섞이지 않았는지</mark>도 같은 방식으로 확인합니다. 오늘의 네 가지 점검은 예시이고, 실제 점검 내용은 고객사 정책마다 다릅니다.
