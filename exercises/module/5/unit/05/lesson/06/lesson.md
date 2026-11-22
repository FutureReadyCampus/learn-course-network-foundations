---
id: m5-u05-l06
title: 정답
render: markdown
---

# 정답

## 정답을 보는 방법

아래 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## 실습 5-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise5-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`soar_engine.py` 의 ① · ② 입니다.

```python
    # ① decision 이 "자동" 이면 (if, ==)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    if decision == "자동":                                       # 게이트가 자동으로 정했으면
        # ② 어떤 종류의 오류든 error 에 저장해 받는다 (except, Exception, as)   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
        except Exception as error:                              # 어떤 종류의 오류든 error 에 저장해 받는다
```

위 줄만으로는 `if` · `try` 안에 들어가는 줄이 어느 것인지 알기 어려우니, 미리 채운 줄까지 넣은 두 함수의 완성된 모양을 함께 봅니다.

**전체 모양 — `run_step`**

```python
def run_step(alert, action, context):                            # 알림 · 조치 이름 · 엔진 재료를 받는 함수
    """조치 하나를 승인 게이트에 묻고, 자동으로 정해졌을 때만 실행해서 결정 · 이유 · 실행 여부를 담은 딕셔너리를 리턴한다. 조치마다 한 번씩 쓴다."""
    request = make_request(alert, action, context)               # 승인 게이트에 보낼 조치 요청을 만든다 — 미리 채운 줄
    decision, reasons = decide_gate(request, context["policy"])  # 승인 게이트의 결정과 이유 리스트를 함께 받는다 — 미리 채운 줄
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
    if decision == "자동":                                       # ① 게이트가 자동으로 정했으면
        record = execute_action(request, context)                # 조치를 실행하고 조치 기록을 받는다 — 미리 채운 줄
        step["executed"] = True                                  # 실행했다고 적는다 — 미리 채운 줄
        step["before"] = record["before"]                        # 조치 전 상태를 적는다 — 미리 채운 줄
        step["after"] = record["after"]                          # 조치 후 상태를 적는다 — 미리 채운 줄
    return step                                                  # 조치 하나의 결과를 리턴한다 — 미리 채운 줄
```

**전체 모양 — `run_all`**

```python
def run_all(alerts, context):                           # 알림 리스트와 엔진 재료를 받는 함수
    """알림을 하나씩 처리하되, 오류가 난 알림은 실패 기록만 남기고 다음 알림으로 넘어간다. 알림 하나의 오류가 나머지 알림의 처리를 막지 않게 할 때 쓴다."""
    results = []                                        # 알림마다 결과 기록을 모을 빈 리스트 — 미리 채운 줄
    for alert in alerts:                                # 알림을 하나씩 꺼낸다 — 미리 채운 줄
        try:                                            # 오류가 날 수 있는 처리를 시작한다 — 미리 채운 줄
            result = run_soar_pipeline(alert, context)  # 알림 한 건을 처음부터 끝까지 처리한다 — 미리 채운 줄
        except Exception as error:                      # ② 어떤 종류의 오류든 error 에 저장해 받는다
            result = make_failure_result(alert, error)  # 실패 기록을 만든다 — 미리 채운 줄
        results.append(result)                          # 정상 결과든 실패 기록이든 결과 리스트에 추가한다 — 미리 채운 줄
    return results                                      # 결과 기록 리스트를 리턴한다 — 미리 채운 줄
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
  - `try` / `except` 가 없으면 오류가 `run_all` 밖으로 나와 프로그램이 멈춥니다. <mark style="background:#ffc4d6">단계 2 이후가 출력되지 않고, 로그와 티켓 파일도 저장되지 않으며, `INC-403` ~ `INC-408` 6건이 처리되지 않습니다.</mark> `INC-401` 은 이미 `dami` 를 잠갔는데 그 기록이 남지 않습니다. 아래는 `run_all` 에서 `try` / `except` 를 뺀 채 실행한 결과의 마지막 줄입니다. 실제 화면에는 그 위에 `Traceback` 으로 시작하는 여러 줄이 먼저 나옵니다.

```
KeyError: 'grade'
```

- (다) `INC-404` 의 `203.0.113.80` 은 허용 목록에 있어서 `decide_gate` 가 점수를 보지 않고 「차단 금지」로 정합니다. `INC-406` 의 `gaeun` 은 VIP 라서 <mark style="background:#bde3ff">등급 high +2 와 VIP +3 을 더한 합계 5점</mark>이 승인 기준(3점) 이상이라 「승인 필요」입니다.
  - 허용 목록은 점수와 상관없이 실행하지 않는 대상이고, VIP 는 점수로 사람의 승인을 받는 대상이라 결과가 다릅니다.
  - 조치를 실행한 뒤에는 이미 잠기거나 차단된 계정과 IP 가 업무를 막을 수 있어서, <mark>승인 게이트는 `execute_action` 보다 먼저 판단해야 합니다.</mark> 아래 「자주 틀리는 곳」에서 ① 에 `!=` 를 쓴 경우처럼 조건이 거꾸로 되면 허용 목록 IP 가 차단됩니다.

**왜**

- <mark>엔진은 「실행하기 전에 정책으로 막고, 실행한 뒤에는 기록을 남기고, 오류는 알림 한 건에 한정한다」는 순서입니다.</mark> 승인 게이트를 엔진 안에 고정하면 사람이 함수를 직접 호출하면서 게이트를 건너뛰는 실수를 막을 수 있습니다. 오류를 알림 한 건에 한정하면 한 건의 문제가 나머지 알림의 처리를 멈추지 않습니다. 대신 코드의 실수도 실패로 나타나므로(아래 「자주 틀리는 곳」의 `desicion` 오타), 실패 건수를 매번 확인해야 합니다.

**자주 틀리는 곳**

아래 결과는 해당 빈칸을 비우거나 틀리게 쓰고 실행한 것입니다(빈칸의 주석은 남겨 둔 상태입니다).

- ① 을 비워 두면(채우기 전 그대로면) 그 아래 미리 채운 줄이 앞줄보다 들여써져 있어 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- ② 를 비워 두면 `try` 만 있고 `except` 가 없어서 실행하기 전에 멈춥니다. 파이썬 3.9 이하에서는 `SyntaxError: invalid syntax` 로 나옵니다.

```
SyntaxError: expected 'except' or 'finally' block
```

- ② 를 `try:` 보다 깊게(12칸) 쓰면 `except` 가 `try` 의 짝이 되지 못해 실행하기 전에 멈춥니다. `try:` 와 같은 8칸에서 시작합니다.

```
SyntaxError: invalid syntax
```

- ① 에서 `decision` 을 `desicion` 처럼 잘못 쓰면 프로그램은 멈추지 않지만 <mark style="background:#ffc4d6">**조치를 처리하는 알림이 모두 실패로 나옵니다.**</mark> `except Exception` 이 코드의 실수까지 받아서 알림마다 실패로 적기 때문입니다. 단계 2 의 `INC-401` 실패와 단계 3 의 `실패 : 6 건` 이 이 실수의 결과입니다.

```
INC-401 dami → 실패 · NameError: name 'desicion' is not defined
실패 : 6 건
```

- ① 에서 `==` 대신 `!=` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**자동이 아닌 조치가 실행됩니다.**</mark> 허용 목록 IP(`INC-404`)가 차단되고, 자동이어야 하는 `dami` 는 잠기지 않습니다. 게이트가 「차단 금지」라고 적었어도 실행 줄이 같이 나오는 것이 이 실수의 결과입니다. 아래는 관련 알림만 발췌한 출력입니다.

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

**관제에서는**

- 알림 하나의 오류가 전체 처리를 멈추지 않게 하는 방식은 SOAR 에서 흔히 쓰는 설계입니다. 다만 오류를 받은 뒤에는 <mark>실패 건수를 모니터링하고 실패한 알림을 담당자에게 넘기는 절차</mark>를 함께 둬야 실패가 확인되지 않은 채 남지 않습니다. 오늘의 처리 결과 다섯 가지 이름은 이 교재에서 정한 것입니다.

---

## 실습 5-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise5-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`policy_check.py` 의 ① · ② 입니다.

```python
            # ① decide_gate(step["request"], policy) 의 두 결과를 new_decision, new_reasons 에 저장한다   # ← 이 주석 바로 아래 줄에 씁니다 (12칸)
            new_decision, new_reasons = decide_gate(step["request"], policy)  # 저장된 조치 요청으로 게이트의 결정을 다시 구한다
            # ② new_decision 이 "자동" 이 아니고(and) step["executed"] 가 참이면 (if, !=, and)   # ← 이 주석 바로 아래 줄에 씁니다 (12칸)
            if new_decision != "자동" and step["executed"]:                   # 다시 구한 결정이 자동이 아닌데 실행했으면
```

위 줄만으로는 `if` 안에 들어가는 줄이 어느 것인지 알기 어려우니, 미리 채운 줄까지 넣은 함수의 완성된 모양을 함께 봅니다.

**전체 모양 — `find_gate_bypass`**

```python
def find_gate_bypass(results, policy):                                        # 결과 기록 리스트와 승인 정책을 받는 함수
    """저장된 조치 요청으로 승인 게이트의 결정을 다시 구해, 자동이 아닌데 실행된 조치가 있는 알림 번호를 리스트로 리턴한다. 게이트를 거치지 않았거나 결정을 바꿔 쓴 실행을 찾을 때 쓴다."""
    violations = []                                                           # 위반한 알림 번호를 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                                    # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        for step in result["steps"]:                                          # 조치 결과를 하나씩 꺼낸다 — 미리 채운 줄
            new_decision, new_reasons = decide_gate(step["request"], policy)  # ① 저장된 조치 요청으로 게이트의 결정을 다시 구한다
            if new_decision != "자동" and step["executed"]:                   # ② 다시 구한 결정이 자동이 아닌데 실행했으면
                violations.append(result["incident"])                         # 알림 번호를 위반 리스트에 추가한다 — 미리 채운 줄
    return violations                                                         # 위반한 알림 번호 리스트를 리턴한다 — 미리 채운 줄
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
- (다) `INC-406` 은 `before` 와 `after` 가 모두 <mark style="background:#bde3ff">「변경 없음」</mark>입니다. Unit 2 실습 2-1 `lock_account` 가 VIP 계정(`gaeun`)이면 잠그지 않고 「VIP 계정이라 자동 조치 대상이 아님」을 기록하기 때문에 `gaeun` 은 잠기지 않았습니다. 점검 ①은 그래도 조치 함수를 호출한 것(`executed`)이라서 FAIL 입니다.
  - 점검 ③은 게이트나 `lock_account` 와 별도로 결과(`after`)만 봅니다. `lock_account` 에 VIP 리스트를 잘못 전달하거나 함수가 바뀌면 같은 로그에서도 VIP 가 잠길 수 있는데, 그때는 ③이 FAIL 로 잡습니다. <mark>한 겹의 통제가 깨져도 다른 겹의 점검이 잡도록 각각 점검합니다.</mark>

**왜**

- <mark>통제는 만들어 두는 것만으로는 부족하고, 작동했다는 증거를 로그로 확인해야 합니다.</mark> ①은 재수행으로 엔진이 적은 값을 믿지 않고, ②③은 불변 조건으로 게이트의 계산과 무관하게 결과를 봅니다. 점검을 코드로 만들어 두면 알림이 늘어도 같은 방식으로 반복해서 확인할 수 있습니다.

**자주 틀리는 곳**

아래 결과는 해당 빈칸을 비우거나 틀리게 쓰고 실행한 것입니다(빈칸의 주석은 남겨 둔 상태입니다).

- ① · ② 를 모두 비워 두면(채우기 전 그대로면) 오류 없이 <mark style="background:#ffc4d6">**조치가 있는 알림이 모두 게이트 우회로 나옵니다.**</mark> 미리 채운 `violations.append(…)` 가 조건 없이 조치마다 실행되기 때문입니다. 정상 로그도 FAIL 이라 단계 3 이 4 개입니다. 아래는 첫 번째 로그와 단계 3 입니다.

```
[engine_log.json] 알림 8 건
   게이트 우회 실행 : FAIL · 위반 5 건 ['INC-401', 'INC-403', 'INC-404', 'INC-405', 'INC-406']
--- 단계 3: FAIL 이 나온 점검 4 개 · 전체 점검 12 개
```

- ① 만 쓰고 ② 를 비워 두면 그 아래 미리 채운 줄이 앞줄보다 들여써져 있어 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- ① 을 비우고 ② 만 쓰면 `new_decision` 을 만들지 못해 오류가 납니다.

```
NameError: name 'new_decision' is not defined
```

- ② 에서 `new_decision` 대신 로그에 적힌 `step["decision"]` 을 쓰면 오류 없이 <mark style="background:#ffc4d6">**게이트를 끈 로그에서 위반을 하나도 찾지 못합니다.**</mark> 로그에는 모든 결정이 「자동」으로 적혀 있기 때문입니다. FAIL 은 허용 목록 점검 하나만 남습니다.

```
[gate_off_log.json] 알림 5 건
   게이트 우회 실행 : PASS · 위반 0 건 []
   허용 목록 IP 차단 : FAIL · 위반 1 건 ['INC-404']
--- 단계 3: FAIL 이 나온 점검 1 개 · 전체 점검 12 개
```

- ② 에서 `!=` 대신 `==` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**정상인 로그에서 위반이 나옵니다.**</mark> 자동으로 정해져 실행한 `INC-401` · `INC-403` 이 게이트 우회로 나옵니다. 아래는 첫 번째 로그의 결과입니다.

```
[engine_log.json] 알림 8 건
   게이트 우회 실행 : FAIL · 위반 2 건 ['INC-401', 'INC-403']
```

- ② 에서 `and step["executed"]` 를 빠뜨리면 오류 없이 <mark style="background:#ffc4d6">**실행하지 않은 조치도 위반으로 나옵니다.**</mark> 정상 로그에서 게이트가 막아 실행하지 않은 `INC-404` · `INC-405` · `INC-406` 이 위반입니다.

```
[engine_log.json] 알림 8 건
   게이트 우회 실행 : FAIL · 위반 3 건 ['INC-404', 'INC-405', 'INC-406']
```

**관제에서는**

- 자동화가 정책대로 동작했는지는 사람이 가끔 읽는 것으로 확인하지 않고, 같은 점검을 로그에 정기적으로 실행해서 확인합니다. 점검에서 FAIL 이 나오면 위반한 알림 번호로 원인을 찾고 담당자에게 알립니다. 승인 게이트를 끈 시험 운영 로그처럼 <mark>통제를 일부러 끈 기록이 운영에 섞이지 않았는지</mark>도 같은 방식으로 확인합니다. 오늘의 네 가지 점검은 예시이고, 실제 점검 내용은 고객사 정책마다 다릅니다.

## 응용 5-1 정답

여유가 되면 해 보세요.

 **터미널에 입력합니다.**

```bash
pwd
python apply5-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`engine_input.py` 의 1 ~ 8번입니다.

```python
        # 1. key 가 record 안에 없으면 (if, not in)   (8칸)
        if key not in record:                                  # 필수 키가 기록에 없으면
    # 2. record["grade"] 가 GRADES 안에 없으면 (if, not in)   (4칸)
    if record["grade"] not in GRADES:                          # 등급 이름을 엔진이 모르면
    # 3. "INC-" 뒤에 str(number) 를 이어 붙여 alert_id 에 저장한다   (4칸)
    alert_id = "INC-" + str(number)                            # 번호 앞에 INC- 를 붙인다
    # 4. 키 "id"(alert_id) · "entity" · "grade" · "score" · "reasons"(record 의 같은 이름 키의 값), "status"("탐지됨") 를 가진 딕셔너리를 alert 에 저장한다   (4칸)
    alert = {                                                  # 엔진이 읽는 알림 딕셔너리
        "id": alert_id,                                        # 알림 번호
        "entity": record["entity"],                            # 대상
        "grade": record["grade"],                              # 등급
        "score": record["score"],                              # 점수
        "reasons": record["reasons"],                          # 탐지된 규칙 이름 리스트
        "status": "탐지됨",                                    # 처음 상태
    }
        # 5. find_schema_problem(record) 의 결과를 problem 에 저장한다   (8칸)
        problem = find_schema_problem(record)                  # 모양 점검 결과를 받는다
        # 6. problem 이 "" 이면 (if, ==)   (8칸)
        if problem == "":                                      # 문제가 없으면
        # 7. outcome_counts[outcome] 에 outcome_counts[outcome] + 1 을 저장한다 (1 늘린다)   (8칸)
        outcome_counts[outcome] = outcome_counts[outcome] + 1  # 이 처리 결과의 알림 수를 1 늘린다
            # 8. step["executed"] 가 참이면 (if)   (12칸)
            if step["executed"]:                               # 실행한 조치이면
```

위 줄만으로는 `if` 안에 들어가는 줄이 어느 것인지 알기 어려우니, 미리 채운 줄까지 넣은 세 함수의 완성된 모양을 함께 봅니다.

**전체 모양 — `find_schema_problem`**

```python
def find_schema_problem(record):                      # Module 4 결과 기록 한 건을 받는 함수
    """엔진이 읽을 수 없는 기록이면 그 이유 문장을, 문제가 없으면 빈 문자열("")을 리턴한다. Module 4 파일의 모양이 바뀌었을 때 엔진이 오류를 내기 전에 걸러 낼 때 쓴다."""
    for key in REQUIRED_KEYS:                         # 필수 키를 하나씩 꺼낸다 — 미리 채운 줄
        if key not in record:                         # 필수 키가 기록에 없으면
            return "필수 키 없음: " + key             # 어떤 키가 없는지 이유로 리턴한다 — 미리 채운 줄
    if record["grade"] not in GRADES:                 # 등급 이름을 엔진이 모르면
        return "알 수 없는 등급: " + record["grade"]  # 등급 이름을 이유로 리턴한다 — 미리 채운 줄
    if record["reasons"] == []:                       # 탐지된 규칙 리스트가 비어 있으면 — 미리 채운 줄
        return "탐지된 규칙이 없음"                   # 이유를 리턴한다 — 미리 채운 줄
    return ""                                         # 문제가 없으면 빈 문자열을 리턴한다 — 미리 채운 줄
```

**전체 모양 — `split_records`**

```python
def split_records(records):                                          # Module 4 결과 기록 리스트를 받는 함수
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

`apply5-1_run.py` 의 9번입니다.

```python
# 9. run_all(alerts, context) 의 결과를 results 에 저장한다   (0칸)
results = run_all(alerts, context)  # 알림을 하나씩 엔진으로 처리한다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 5 의 처리 결과는 자동 실행 <mark style="background:#bde3ff">**2건**</mark> · 승인 대기 <mark style="background:#bde3ff">**0건**</mark> · 차단 금지 <mark style="background:#bde3ff">**0건**</mark> · 조치 없음 <mark style="background:#bde3ff">**3건**</mark> · 실패 <mark style="background:#bde3ff">**0건**</mark>이고, 실제로 실행한 조치는 <mark style="background:#bde3ff">`INC-501` 의 `dami` 계정 잠금 · `INC-505` 의 `198.51.100.90` 차단</mark>입니다.

```
--- 단계 1: Module 4 탐지 결과 5 건
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

- (나) `seoyeon`(`INC-502`)은 플레이북 `PB-002`(대량 다운로드)가 맞지만, 그 플레이북의 액션이 `담당자 알림` · `티켓 생성` 뿐이라 승인 게이트를 거칠 조치(계정 잠금 · IP 차단)가 없습니다. `gaeun`(`INC-503`)과 `jiwoo`(`INC-504`)는 단계 4 의 플레이북 번호가 <mark style="background:#bde3ff">「없음」</mark>입니다. Unit 1 플레이북 3개의 트리거 규칙은 퇴사한 계정 · 대량 다운로드 · 경로 스캔이고, 두 대상의 이유(`규칙은 허용인데 서버가 거절` · `여러 로그 연결` / `업무 시간 밖 로그인` · `평소와 다른 IP`)는 그 규칙에 없기 때문입니다.
  - 티켓이 없으면 세 알림은 엔진이 한 일도 남은 기록도 없어서 담당자가 알 방법이 없습니다. <mark style="background:#ffc4d6">티켓이 조치 없는 알림을 사람에게 넘기는 유일한 경로입니다.</mark> 세 알림의 티켓(`TCK-2` ~ `TCK-4`)에는 다음 할 일로 「자동 조치가 없는 알림이니 직접 보고 조치가 필요한지 정한다」가 적힙니다.
- (다) `minsu` 기록은 등급이 `critical` 이라 엔진이 아는 등급(`GRADES`: high · mid · low)에 없어서 <mark style="background:#bde3ff">`알 수 없는 등급: critical`</mark> 로 거절됩니다. 거절하면 거절 리스트에 이유가 남아 Module 4 쪽을 고칠 수 있습니다.
  - 거절 없이 엔진에 넣으면 `match_playbooks` 가 `GRADE_ORDER["critical"]` 을 찾다가 오류를 내고, 실습 5-1 `INC-402` 처럼 그 알림만 실패로 기록됩니다. 조치도 티켓도 없고 원인은 오류 문장에만 남습니다. 아래는 그렇게 실행했을 때 그 알림의 결과 줄에서 끝부분(처리 결과와 오류 문장)만 옮긴 것입니다.

```
실패 · KeyError: 'critical'
```

**왜**

- <mark>입력 검증은 엔진이 오류를 내기 전에 문제를 이유와 함께 남기고, 오류 격리는 걸러지지 않은 문제를 알림 한 건에 한정합니다.</mark> 둘 중 하나만 있으면 잘못된 기록이 조치도 티켓도 없이 사라지거나, 엔진이 멈춥니다. 운영 요약은 처리 결과를 한 장으로 모아, 근무 인계와 보고에서 「무엇을 실행했고 무엇이 사람에게 남았는지」를 바로 알게 합니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 비우고 실행한 것입니다(비운 줄의 주석은 남겨 둔 상태입니다).

- 1번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**모든 기록이 「필수 키 없음: entity」로 거절됩니다.**</mark> `return` 줄이 `if` 없이 첫 번째 키에서 바로 실행되기 때문입니다. Module 4 기록 5건이 모두 거절되어 엔진에 넣을 알림이 0건입니다.

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

- 탐지와 대응은 다른 팀이나 다른 제품이 만드는 경우가 많아서 데이터 모양이 어긋나기 쉽습니다. 둘 사이에 입력 검증을 두고 <mark>거절한 기록 수를 모니터링</mark>하면, 거절이 갑자기 늘었을 때 상류의 형식이 바뀐 것을 알 수 있습니다. 오늘의 필수 키 네 개와 등급 세 가지는 이 교재의 공통 스키마입니다.

---
