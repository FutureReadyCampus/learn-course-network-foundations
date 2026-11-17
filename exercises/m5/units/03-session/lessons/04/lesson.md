---
id: m5-u03-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/120_day02_pm_approval_retry_flow.md
  mission_id: GichanSource.m5-1110-pm-approval-retry-flow
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## Exercise 3-1 정답

**채운 코드** (한 예)

`audit.py` 의 1번입니다.

```python
    # 1. 키 "incident"(item 의 "id"), "playbook"(item 의 "playbook"), "action"(action), "result"(text) 를 가진 딕셔너리를 entry 에 담는다
    entry = {"incident": item["id"], "playbook": item["playbook"], "action": action, "result": text}  # 기록 한 건을 딕셔너리로 만든다
```

`approvals.py` 의 2 ~ 7번입니다.

```python
    # 2. approver 가 APPROVERS 안에 있는지(in)의 결과를 리턴한다
    return approver in APPROVERS                                   # 권한 목록 안에 있는지 확인한 결과를 리턴한다
        # 3. run_action(action, item, state) 의 결과를 result 에 담는다
        result = run_action(action, item, state)                   # 액션을 실행해 결과 문장을 받는다
    # 4. is_authorized(approver) 가 거짓이면 (if, not)
    if not is_authorized(approver):                                # 승인 권한이 없으면
    # 5.   reject_unauthorized(item, approver, action_log) 의 결과를 리턴한다
        return reject_unauthorized(item, approver, action_log)     # 기록만 남기고 멈춘다
    # 6. decision["result"] 가 "승인" 이면 (if, ==)
    if decision["result"] == "승인":                               # 결정이 승인이면
    # 7.   execute_actions(item, state, action_log, approver) 의 결과를 리턴한다
        return execute_actions(item, state, action_log, approver)  # 액션을 실행하고 그 결과를 리턴한다
```

`exercise3-1_run.py` 의 8 · 9번입니다.

```python
    # 8. item["id"] 가 decisions 안에 있으면 (if, in)
    if item["id"] in decisions:                                                       # 이 건에 대한 담당자 결정이 있으면
    # 9.   apply_decision(item, decisions[item["id"]], state, action_log) 의 결과를 result_text 에 담는다
        result_text = apply_decision(item, decisions[item["id"]], state, action_log)  # 결정을 적용한다
```

**결과**

- (가) 출력은 다음과 같습니다. 티켓은 <mark style="background:#bde3ff">**1건**</mark>, 담당자 알림은 <mark style="background:#bde3ff">**1건**</mark>이고, `분류됨` 으로 남은 건은 <mark style="background:#bde3ff">**INC-005**</mark> 입니다.

```
--- 단계 1: 승인 대기 건
INC-002 seoyeon · PB-002 · 플레이북 승인 값이 담당자 승인 필요
INC-003 gaeun · VIP 확인 · VIP 계정이라 경로가 승인 필요
INC-005 198.51.100.90 · PB-003 · 플레이북 승인 값이 담당자 승인 필요
--- 단계 2: 담당자 결정 처리
INC-002 seoyeon -> 실행 완료 (상태: 조치됨)
INC-003 gaeun -> 거절 처리 (상태: 종료)
INC-005 198.51.100.90 -> 권한 없음 (상태: 분류됨)
--- 단계 3: 처리 뒤 연습용 시스템 상태
잠긴 계정: []
차단한 IP: []
티켓: 1 건 · 담당자 알림: 1 건
--- 단계 4: 감사 기록
INC-002 PB-002 담당자 알림 : 담당자 알림 전송 (승인: kim.sec)
INC-002 PB-002 티켓 생성 : 티켓 TCK-1 생성 (승인: kim.sec)
INC-003 VIP 확인 전체 : 거절됨 (승인: kim.sec — 계정 관리자의 정상 작업으로 확인됨)
INC-005 PB-003 전체 : 권한 없음 — 승인 시도: intern01
```

- (나) INC-005 는 결정한 `intern01` 이 <mark style="background:#bde3ff">`APPROVERS` 에 없어서</mark> 실행되지 않았습니다.
  - 근거: 단계 2 에 `권한 없음 (상태: 분류됨)`, 단계 3 에 `차단한 IP: []`, 단계 4 에 `권한 없음 — 승인 시도: intern01` 이 나옵니다.
  - 위험: 이 확인이 없으면 권한 없는 사람이 `승인` 만 눌러도 IP 가 차단됩니다.
  - 같은 IP 를 여러 사람이 쓰면 정상 사용자의 업무가 막힙니다.
  - 승인 권한이 있는 담당자의 허락 없이 차단한 것이라, 왜 차단했는지 나중에 설명할 수 없습니다.
- (다) INC-003 은 `pending.json` 의 이유가 <mark style="background:#bde3ff">`VIP 계정이라 경로가 승인 필요`</mark> 입니다. Unit 2의 Exercise 2-2에서 VIP 계정(막히면 업무에 큰 영향을 주는 중요한 계정)은 담당자가 확인하기 전에는 처리하지 않도록 `승인 필요` 경로로 보냈기 때문입니다.
  - 거절된 뒤 상태는 <mark style="background:#bde3ff">`종료`</mark> 이고, 감사 기록에 `거절됨 (승인: kim.sec — 계정 관리자의 정상 작업으로 확인됨)` 이 남습니다. 누가 어떤 사유로 닫았는지 사고 뒤에 설명할 수 있습니다.

**왜**: <mark>승인은 「누가 눌렀는지 확인」과 「누가 눌렀는지 기록」이 둘 다 있어야 믿을 수 있습니다.</mark> 누른 사람이 누구인지 확인하지 않고 실행하면, 아무나 자동 대응을 실행시킬 수 있습니다. 누가 허락했는지 기록이 없으면, 나중에 누구 책임인지 설명할 수 없습니다.

**자주 틀리는 곳**

- 1번을 비워 두면 기록 한 건을 만들지 못해 오류가 납니다. <mark>**`entry` 변수에 딕셔너리를 저장해 두지 않으면 `return entry` 가 실패합니다.**</mark>

```
--- 단계 2: 담당자 결정 처리
NameError: name 'entry' is not defined
```

- 2번을 비워 두면 `is_authorized` 가 `return` 이 없어 `None`(값 없음)을 리턴하고, `if not None` 이 참이 되어 <mark>**권한 있는 담당자도 모두 「권한 없음」이 됩니다.**</mark>

```
--- 단계 2: 담당자 결정 처리
INC-002 seoyeon -> 권한 없음 (상태: 분류됨)
INC-003 gaeun -> 권한 없음 (상태: 분류됨)
INC-005 198.51.100.90 -> 권한 없음 (상태: 분류됨)
```

- 4 · 5번을 비워 두면 오류는 나지 않지만 <mark>**권한 없는 `intern01` 의 승인으로 IP 가 차단됩니다.**</mark> 이 실수를 하면 단계 2 에서 INC-005 가 `실행 완료` 로 나옵니다.

```
--- 단계 2: 담당자 결정 처리
INC-002 seoyeon -> 실행 완료 (상태: 조치됨)
INC-003 gaeun -> 거절 처리 (상태: 종료)
INC-005 198.51.100.90 -> 실행 완료 (상태: 조치됨)
--- 단계 3: 처리 뒤 연습용 시스템 상태
잠긴 계정: []
차단한 IP: ['198.51.100.90']
티켓: 2 건 · 담당자 알림: 1 건
```

- 6 · 7번을 비워 두면 <mark>**승인한 건도 모두 거절 처리됩니다.**</mark>

```
--- 단계 2: 담당자 결정 처리
INC-002 seoyeon -> 거절 처리 (상태: 종료)
INC-003 gaeun -> 거절 처리 (상태: 종료)
INC-005 198.51.100.90 -> 권한 없음 (상태: 분류됨)
```

- 7번에서 `return` 을 빼고 `execute_actions(…)` 만 호출하면 <mark>**`return` 이 없으면 함수가 거기서 끝나지 않습니다. 그래서 실행한 다음 줄도 실행되어 거절 기록까지 남습니다.**</mark> INC-002 가 `거절 처리` 인데 상태는 `조치됨` 이고, 단계 4 에 실행 기록과 거절 기록이 함께 남습니다. 서로 맞지 않는 이런 결과가 나오면 이 실수입니다.

```
--- 단계 2: 담당자 결정 처리
INC-002 seoyeon -> 거절 처리 (상태: 조치됨)
INC-003 gaeun -> 거절 처리 (상태: 종료)
INC-005 198.51.100.90 -> 권한 없음 (상태: 분류됨)
…
--- 단계 4: 감사 기록
INC-002 PB-002 담당자 알림 : 담당자 알림 전송 (승인: kim.sec)
INC-002 PB-002 티켓 생성 : 티켓 TCK-1 생성 (승인: kim.sec)
INC-002 PB-002 전체 : 거절됨 (승인: kim.sec — 대량 다운로드 사유를 확인해야 함)
INC-003 VIP 확인 전체 : 거절됨 (승인: kim.sec — 계정 관리자의 정상 작업으로 확인됨)
INC-005 PB-003 전체 : 권한 없음 — 승인 시도: intern01
```

- 6번에서 `==` 대신 `!=` 를 쓰면 거꾸로 동작합니다. <mark>**승인한 건은 종료되고, 거절한 건이 실행됩니다.**</mark>

```
--- 단계 2: 담당자 결정 처리
INC-002 seoyeon -> 거절 처리 (상태: 종료)
INC-003 gaeun -> 실행 완료 (상태: 조치됨)
INC-005 198.51.100.90 -> 권한 없음 (상태: 분류됨)
```

- 8 · 9번을 비워 두면 <mark>**모든 건이 「결정 없음」으로 남습니다.**</mark>

```
--- 단계 2: 담당자 결정 처리
INC-002 seoyeon -> 결정 없음 (상태: 분류됨)
INC-003 gaeun -> 결정 없음 (상태: 분류됨)
INC-005 198.51.100.90 -> 결정 없음 (상태: 분류됨)
```

**관제에서는**: 승인 요청을 받으면 가장 먼저 「누른 사람이 승인 권한이 있는가」를 확인합니다. <mark>승인 · 거절 · 권한 없는 시도를 같은 감사 기록에 남기면</mark> 사고가 난 뒤에 누가 무엇을 허락했는지 한 목록에서 다시 확인할 수 있습니다.

---

## Exercise 3-2 정답

**채운 코드** (한 예)

`retry_runner.py` 의 1 ~ 3번입니다.

```python
            # 1. flaky_run_action(action, incident, state, fail_plan) 의 결과를 result 에 담는다
            result = flaky_run_action(action, incident, state, fail_plan)  # 액션을 실행해 결과를 받는다
            # 2. result + " (시도 " + str(attempt) + "회)" 를 리턴한다 (성공하면 여기서 끝난다)
            return result + " (시도 " + str(attempt) + "회)"               # 성공하면 시도 횟수를 붙여 리턴하고 끝낸다
            # 3. str(error) 를 last_error 에 담는다 (오류 문장을 기억해 두고 다음 시도로 간다)
            last_error = str(error)                                        # 오류 문장을 기억해 두고 다음 시도로 간다
```

`flow.py` 의 4 · 5번입니다.

```python
        # 4. result 가 "실패" 로 시작하면 (if, startswith)
        if result.startswith("실패"):  # 결과 문장이 「실패」로 시작하면
        # 5.   failed 에 True 를 담는다 (실패한 액션이 있다고 적는다)
            failed = True              # 실패한 액션이 있다고 적는다
```

`failure_report.py` 의 6 · 7번입니다.

```python
        # 6. entry["result"] 가 "실패" 로 시작하면 (if, startswith)
        if entry["result"].startswith("실패"):  # 결과 문장이 「실패」로 시작하면
        # 7.   failures 에 entry 를 추가한다 (append)
            failures.append(entry)              # 실패한 기록을 리스트에 추가한다
```

`exercise3-2_run.py` 의 8 · 9번입니다.

```python
# 8. collect_failures(action_log) 의 결과를 failures 에 담는다
failures = collect_failures(action_log)                        # 실패한 기록을 모은다
    # 9. incident_id · entry["action"] · ":" · entry["result"] 를 출력한다 (print)
    print(incident_id, entry["action"], ":", entry["result"])  # 실패한 액션을 출력한다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 3 에서 `일부 실패` 는 <mark style="background:#bde3ff">**INC-001**</mark>, `승인 대기` 는 <mark style="background:#bde3ff">**INC-002 · INC-003 · INC-005**</mark>, `오탐 종료` 는 <mark style="background:#bde3ff">**INC-004**</mark> 입니다.

```
--- 단계 1: 일시 장애 — 티켓 서비스가 2번 실패한 뒤 복구
티켓 TCK-1 생성 (시도 3회)
만든 티켓: 1 건
--- 단계 2: 서비스 중단 — 티켓 서비스가 계속 실패
실패: 연결 실패: 티켓 생성 서비스가 응답하지 않음 (3회 모두 실패)
만든 티켓: 0 건
--- 단계 3: 하루 흐름 — 티켓 서비스가 계속 실패하는 상황
INC-001 dami -> 일부 실패 (상태: 분류됨)
INC-002 seoyeon -> 승인 대기 (상태: 분류됨)
INC-003 gaeun -> 승인 대기 (상태: 분류됨)
INC-004 jiwoo -> 오탐 종료 (상태: 종료)
INC-005 198.51.100.90 -> 승인 대기 (상태: 분류됨)
--- 단계 4: 담당자 결정 처리
INC-002 seoyeon -> 실행 완료 (상태: 조치됨)
INC-003 gaeun -> 거절 처리 (상태: 종료)
INC-005 198.51.100.90 -> 권한 없음 (상태: 분류됨)
--- 단계 5: 하루가 끝난 뒤 연습용 시스템 상태
잠긴 계정: ['dami']
차단한 IP: []
티켓: 1 건 · 담당자 알림: 1 건
--- 단계 6: 담당자 확인이 필요한 건
INC-001 티켓 생성 : 실패: 연결 실패: 티켓 생성 서비스가 응답하지 않음 (3회 모두 실패)
INC-005 승인 대기 : 플레이북 승인 값이 담당자 승인 필요
```

- (나) 단계 1 의 `fail_plan` 은 <mark style="background:#bde3ff">`{"INC-001|티켓 생성": 2}`</mark> 라서 2번 실패한 뒤 3번째 시도에서 성공합니다(`시도 3회`). 단계 2 의 값은 <mark style="background:#bde3ff">`99`</mark> 라서 3번 모두 실패합니다. 같은 코드라도 서비스 상태에 따라 결과가 다릅니다.
  - 최대 횟수가 없으면 서비스가 계속 멈춰 있을 때 같은 요청을 끝없이 보내서 대응 전체가 멈춥니다.
  - 이미 멈춘 서비스에 요청을 계속 보내면 복구도 늦어집니다.
  - 실제로는 서비스가 복구될 시간을 주려고, 시도 사이의 기다리는 시간을 점점 늘립니다. 오늘 수업은 기다림 없이 횟수만 정합니다.
- (다) INC-001 은 계정 잠금은 성공했고 티켓 생성은 3번 모두 실패했습니다. <mark style="background:#bde3ff">모든 액션이 성공한 것이 아니므로 `조치됨` 으로 옮기지 않고 `분류됨` 에 남기며 `일부 실패` 를 리턴합니다.</mark>
  - 단계 6 의 `INC-001 티켓 생성 : 실패: …` 줄은 담당자에게 「이 알림의 티켓이 아직 없다」는 사실과 이유를 알려 줍니다.
  - 같은 `state` 에서 다시 처리해도 `dami` 가 두 번 잠기지 않는 이유는, Unit 2의 Exercise 2-3의 `safe_run_action` 이 이미 잠긴 계정을 <mark style="background:#bde3ff">「건너뜀: 이미 잠겨 있음」</mark> 으로 리턴하기 때문입니다.
  - 오늘 실행 파일은 실행할 때마다 `state` 를 새로 만듭니다. 그래서 `dami` 가 두 번 잠기지 않는 모습은 같은 `state` 로 한 번 더 처리할 때만 볼 수 있습니다.
  - 티켓과 담당자 알림은 오늘 코드가 중복을 막지 않습니다. 같은 `state` 로 다시 처리하면 한 번 더 만들어집니다.

**왜**: <mark>잠깐 생긴 실패는 정해진 횟수까지 다시 시도해서 해결하고, 끝내 실패하면 숨기지 않고 기록해 사람에게 넘겨야 합니다.</mark> 그래야 자동 대응이 일부만 실행된 채 아무도 모르게 남는 일이 없습니다.

**자주 틀리는 곳**

- `try` 아래를 비워 둔 채 실행하면 파이썬이 실행 전에 멈춥니다. `IndentationError`(인덴테이션 에러: 들여쓰기 오류)로 시작하는 오류입니다(문구는 버전마다 다릅니다).
- 3번 자리에 `pass`(아무 일도 하지 않는 파이썬 문장)만 써 두면 오류는 나지 않지만 <mark>**실패 문장에 이유가 비어 나옵니다.**</mark> 담당자가 왜 실패했는지 알 수 없습니다. 아예 비워 두면 `except` 아래가 비어 `IndentationError` 가 납니다.

```
--- 단계 2: 서비스 중단 — 티켓 서비스가 계속 실패
실패:  (3회 모두 실패)
```

- 2번에서 `return` 대신 `print(result)` 를 쓰면 <mark>**성공했는데도 함수가 끝나지 않습니다. `print` 는 화면에 보여 줄 뿐 함수를 끝내지 않으므로, 반복이 계속되다가 마지막에 실패 문장을 리턴합니다.**</mark> 단계 1 에서 `티켓 TCK-1 생성` 다음에 `실패: …` 가 이어서 나오는 것이 이 실수의 결과입니다.

```
--- 단계 1: 일시 장애 — 티켓 서비스가 2번 실패한 뒤 복구
티켓 TCK-1 생성
실패: 연결 실패: 티켓 생성 서비스가 응답하지 않음 (3회 모두 실패)
만든 티켓: 1 건
```

- 4 · 5번을 비워 두면 오류는 나지 않지만 <mark>**티켓 생성이 실패했는데도 INC-001 이 `실행 완료 (상태: 조치됨)` 으로 나옵니다.**</mark> 단계 3 은 성공이라고 하는데 단계 6 은 실패라고 합니다. 서로 맞지 않는 이런 결과가 나오면 이 실수입니다.

```
--- 단계 3: 하루 흐름 — 티켓 서비스가 계속 실패하는 상황
INC-001 dami -> 실행 완료 (상태: 조치됨)
INC-002 seoyeon -> 승인 대기 (상태: 분류됨)
INC-003 gaeun -> 승인 대기 (상태: 분류됨)
INC-004 jiwoo -> 오탐 종료 (상태: 종료)
INC-005 198.51.100.90 -> 승인 대기 (상태: 분류됨)
…
--- 단계 6: 담당자 확인이 필요한 건
INC-001 티켓 생성 : 실패: 연결 실패: 티켓 생성 서비스가 응답하지 않음 (3회 모두 실패)
INC-005 승인 대기 : 플레이북 승인 값이 담당자 승인 필요
```

- 6 · 7번 자리에 `pass` 만 써 두면 <mark>**실패한 액션이 담당자 확인 목록에서 빠집니다.**</mark> 단계 6 에 `승인 대기` 한 건만 나옵니다. 아예 비워 두면 `for` 아래가 비어 `IndentationError` 가 납니다.

```
--- 단계 6: 담당자 확인이 필요한 건
INC-005 승인 대기 : 플레이북 승인 값이 담당자 승인 필요
```

- 8번을 비워 두면 `failures` 가 만들어지지 않아 오류가 납니다(`NameError`, 네임 에러: 만들지 않은 이름을 쓸 때 나는 오류). 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 붙을 수 있습니다.

```
NameError: name 'failures' is not defined
```

**관제에서는**: 자동 대응을 켤 때는 「외부 서비스가 실패하면 어디까지 다시 시도하고, 그 뒤에는 누구에게 알리는가」를 먼저 정합니다. <mark>실패한 건의 목록은 담당자가 아침에 가장 먼저 보는 목록</mark>입니다. 실제 제품에서도 정해진 시간 안에 응답이 오지 않거나(타임아웃) 서버 오류(서비스 쪽 문제로 요청을 처리하지 못했다는 응답)가 나면, 정해 둔 규칙대로 같은 요청을 다시 보냅니다. 예를 들어 Microsoft Sentinel(보안 관제 제품)의 플레이북이 쓰는 Azure Logic Apps(자동화 서비스)가 그렇게 합니다.

---

## 정답 마무리

- (가) 한 예: <mark>`git status` 에서 `.env` 와 `.venv` 가 보이지 않았습니다.</mark> `__pycache__` 가 보여서 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 다시 확인했습니다.
- 깃허브 `soar_response` 폴더에 오늘 만든 `.py` 파일이 보이면 됩니다.
