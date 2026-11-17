---
id: m5-u10-l02
title: Exercise 10-1 · 알림 처리 통합 엔진 만들기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/134_day06_am_soar_engine.md
  mission_id: GichanSource.m5-1116-am-soar-engine
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 10-1 · 알림 처리 통합 엔진 만들기

## 이번에 만들 것: 통합 엔진

> **오늘 들어온 일**
>
> - **상황**: Unit 1의 `match_playbooks` 는 알림에 맞는 플레이북을 찾고, Unit 4의 `lock_account` · `block_ip` 는 조치를 실행하고, Unit 6의 `make_ticket` 은 티켓을 만들고, Unit 8의 `decide_gate` 는 자동 · 승인 필요 · 차단 금지를 정합니다. <mark style="background:#e0d4ff">Unit 3의 `flow.py` 는 알림 처리 흐름을 한 번에 실행하지만, 조치는 Unit 1의 간단한 `run_action` 으로 실행합니다.</mark> 그래서 Unit 4 이후에 만든 함수는 그 흐름에 연결되어 있지 않습니다. 이번 Unit에서 알림 8건(`INC-401` ~ `INC-408`)이 들어옵니다.
> - **문제**: 함수를 사람이 순서대로 호출하면 승인 게이트를 건너뛰고 `lock_account` 를 바로 호출하는 실수를 막을 수 없습니다. 또 알림 한 건에서 오류가 나면 프로그램 전체가 멈춥니다. `INC-402` 는 등급(`grade`) 키가 없어서 플레이북을 찾는 단계에서 오류가 납니다. <mark style="background:#ffc4d6">오류를 처리하지 않으면 앞의 `INC-401` 은 `dami` 계정을 이미 잠갔는데 로그와 티켓 파일이 저장되지 않고, 뒤의 알림 6건은 처리되지 않습니다.</mark>
> - **부탁**: 알림 한 건을 「플레이북 찾기 → 승인 게이트 → 조치 실행 → 티켓」 순서로 처리하는 통합 엔진 `soar_engine.py` 를 만들어 주세요. 오류가 난 알림은 오류 이름과 함께 실패로 기록하고, 다음 알림을 계속 처리해야 합니다.
> - **바뀌는 점**: 알림 8건이 <mark style="background:#bde3ff">자동 실행 2 · 승인 대기 2 · 차단 금지 1 · 조치 없음 2 · 실패 1</mark>로 처리되고, 티켓 <mark style="background:#bde3ff">7장</mark>이 `engine_tickets.json` 에 저장됩니다. 상황과 이름은 설명을 위한 예시입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다. (문법 상자의 코드는 눈으로 읽어도 되고, 따라 쳐 보아도 됩니다.)

## 읽기 · 1.1 알림 처리 순서와 오류 격리

| 순서 | 하는 일 | 가져다 쓰는 함수 | 엔진의 함수 |
|---|---|---|---|
| 1. 플레이북 찾기 | 알림의 탐지 규칙과 등급이 맞는 플레이북을 찾는다 | Unit 1 `match_playbooks` | `run_soar_pipeline` (6번) |
| 2. 조치 요청 만들기 | 조치 이름 · 대상 · 등급 · 그 IP 를 쓰는 계정 수를 담은 딕셔너리를 만든다 | Unit 4 `count_users_on_ip` | `make_request` (1번) |
| 3. 승인 게이트 | 자동 · 승인 필요 · 차단 금지를 정한다 | Unit 8 `decide_gate` | `run_step` (4 · 5번) |
| 4. 조치 실행 | 자동으로 정해진 조치만 실행한다 | Unit 4 `lock_account` · `block_ip` | `execute_action` (2 · 3번) |
| 5. 티켓 | 처리 결과를 티켓 한 장으로 남긴다 | Unit 6 `make_ticket` | `open_ticket` (미리 채움) |
| 6. 오류 격리 | 알림 하나의 오류를 그 알림의 실패 기록으로 한정하고 다음 알림으로 넘어간다 | `try` / `except` | `run_all` (7 · 8번) |

- 알림 한 건의 처리 결과(`outcome`)는 <mark>자동 실행 · 승인 대기 · 차단 금지 · 조치 없음 · 실패</mark> 다섯 가지입니다. 조치 없음은 승인 게이트를 거칠 조치가 없는 알림입니다. `decide_outcome` 은 사람이 먼저 봐야 하는 결과가 앞서도록 승인 대기부터 판단합니다.
- <mark style="background:#e0d4ff">Unit 1 플레이북의 승인 값(`approval`)은 이 엔진이 읽지 않습니다.</mark> Unit 8에서 승인 여부를 플레이북 하나에 값 하나로 정하는 대신 요청마다 위험 점수로 정하도록 바꿨기 때문입니다. 플레이북에서는 `actions` 만 읽습니다.
- 플레이북의 액션 가운데 `계정 잠금` · `IP 차단` 만 승인 게이트를 거쳐 실행합니다(`CONTAINMENT_ACTIONS`). 티켓은 처리한 알림마다 항상 만듭니다. 실패한 알림은 티켓이 없어서 알림 8건에 티켓 7장이 됩니다. `담당자 알림` 은 <mark style="background:#e0d4ff">Unit 6 · Unit 7의 알림 서버(5001번 포트)</mark>가 켜져 있어야 보낼 수 있어서 오늘은 연결하지 않고, 담당자에게 넘기는 일은 티켓이 맡습니다.
- 오류 격리(failure isolation, 페일러 아이솔레이션: 한 작업의 오류가 다른 작업으로 번지지 않게 막는 방식)로 오류의 영향 범위를 알림 한 건으로 제한합니다. 대신 <mark style="background:#ffc4d6">코드의 실수도 알림마다 「실패」로 나타납니다.</mark> 실패 건수가 알림 수에 가까우면 데이터가 아니라 코드를 의심합니다.
- `executed` 는 조치 함수를 호출했다는 뜻입니다. 이미 잠긴 계정처럼 호출해도 조치 전 · 후 상태가 같을 수 있어서, 무엇이 바뀌었는지는 `before` · `after` 로 확인합니다.
- 티켓의 시각은 엔진을 실행한 때를 0분으로 놓습니다(Unit 6 티켓처럼 분 단위 숫자입니다). 연습용 시스템(실제 서버를 대신하는 시스템)은 실행할 때마다 처음 상태(`junho` 만 잠김)에서 시작합니다.
- 오늘 엔진에 연결하지 않은 것: Unit 3의 재시도(`run_with_retry`) · Unit 4의 세션 종료 · Unit 7의 에스컬레이션입니다.

**문법 상자 — `except Exception as error` 는 어떤 종류의 오류든 받아서 프로그램이 멈추지 않게 한다**

```python
students = [{"name": "민지", "score": 80}, {"name": "서준"}, {"name": "하은", "score": 95}]  # 서준에게는 score 키가 없다

for student in students:                                                                     # 학생을 하나씩 꺼낸다
    try:                                                                                     # 오류가 날 수 있는 부분을 시작한다
        print(student["name"], student["score"])                                             # 이름과 점수를 출력한다
    except Exception as error:                                                               # 어떤 종류의 오류든 error 에 저장해 받는다
        print(student["name"], "→ 오류:", type(error).__name__, error)                       # 오류의 종류 이름과 내용을 출력한다
```

실행 결과:

```
민지 80
서준 → 오류: KeyError 'score'
하은 95
```

| 코드 | 뜻 |
|---|---|
| `except Exception as error:` | <mark style="background:#e0d4ff">Unit 3의 `except ConnectionError as error` 는 연결 오류 한 종류만 받았습니다.</mark> `Exception` 은 `KeyError` 같은 거의 모든 오류의 부모 이름이라 어떤 종류든 받습니다 |
| `type(error).__name__` | 오류의 종류 이름(`KeyError`)입니다. 오류를 받은 뒤에는 이 이름과 내용을 반드시 기록해서 사람이 볼 수 있게 합니다 |
| 위 코드의 출력 | <mark style="background:#bde3ff">`서준` 줄에서 오류가 나도 `하은` 줄까지 출력됩니다</mark>. `try` 없이 쓰면 `서준` 에서 멈추고 `하은` 은 출력되지 않습니다 |

함수 아홉 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
soar_engine.py  load_context          : 설정 파일을 읽어 엔진 재료를 만든다 (미리 채움)
                make_request          : IP 차단이면 그 IP 를 쓰는 계정 수를 센다 (1번)
                execute_action        : 계정 잠금 (2번) · IP 차단 (3번) 을 실행한다
                run_step              : 승인 게이트에 묻고 (4번) 자동이면 (5번) 실행한다
                decide_outcome        : 조치 결과들로 알림의 처리 결과를 정한다 (미리 채움)
                open_ticket           : 처리 결과로 티켓 한 장을 만든다 (미리 채움)
                run_soar_pipeline     : 게이트를 거칠 조치만 (6번) 처리하고 티켓까지 만든다
                make_failure_result   : 실패한 알림의 결과 기록을 만든다 (미리 채움)
                run_all               : 알림마다 처리하고 (7번) 오류는 실패로 기록한다 (8번)
실행 파일       exercise10-1_run.py      : 처리 결과별 알림 수를 센다 (9번)
```

> **여기부터 문제입니다.**

## Exercise 10-1 · 알림 처리 통합 엔진 만들기

**이런 상황이 있습니다**

- **지금은**: <mark>플레이북 찾기 · 승인 게이트 · 조치 · 티켓이 파일마다 따로 있고, 한 알림의 오류가 전체 처리를 멈춥니다</mark>.
- **만드는 것**: 조치 요청 · 조치 실행 · 승인 게이트 거치기 · 알림 한 건 처리 · 오류 격리(`soar_engine.py`), 처리 결과별 알림 수 세기(`exercise10-1_run.py`).
- **실행하면**: <mark>단계 1: 불러온 알림 수와 승인 기준, 단계 2: 알림마다 처리 결과와 승인 게이트의 결정, 단계 3: 처리 결과별 알림 수, 단계 4: 저장한 로그와 티켓 파일이 나옵니다.</mark>

**할 일**: 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행한 뒤 단계 2 를 알림마다 읽습니다.

**`soar_engine.py`** — 엔진 함수 모음입니다. Exercise 10-2에서 가져와 사용(import)합니다. Exercise 10-3에서는 이 파일을 가져오지 않고 엔진이 남긴 로그 파일을 읽습니다. 직접 쓰는 곳은 1 ~ 8번입니다.

- 1번 · 2번 · 3번은 `if` · `else` 줄이 미리 채워져 있어서 그 아래에 들여쓴 한 줄만 씁니다.
- 5번과 6번은 `if` 한 줄만 씁니다. 그 아래 미리 채운 줄이 `if` 안쪽입니다.
- 7번은 `try:` 아래에 한 줄, 8번은 `except` 줄 한 줄을 씁니다. 8번 아래 미리 채운 줄이 `except` 안쪽입니다.

```python
from incident import load_json, match_playbooks                                         # Unit 1 파일의 JSON 읽기 · 플레이북 찾기 함수를 불러온다
from containment_store import new_state                                                 # Unit 4 파일의 연습용 시스템 상태 함수를 불러온다
from account_actions import lock_account                                                # Unit 4 파일의 계정 잠금 함수를 불러온다
from ip_actions import block_ip, count_users_on_ip, DEFAULT_TTL                         # Unit 4 파일의 IP 차단 · 사용 계정 수 세기 함수와 차단 유지 시간을 불러온다
from approval_gate import decide_gate                                                   # Unit 8 파일의 승인 게이트 함수를 불러온다
from ticketing import make_ticket, NEXT_STEPS                                           # Unit 6 파일의 티켓 함수와 다음 할 일 딕셔너리를 불러온다

ENGINE_REASON = "자동 대응 엔진"                                                        # 조치 기록의 이유에 적는 실행 주체
CONTAINMENT_ACTIONS = ["계정 잠금", "IP 차단"]                                          # 승인 게이트를 거쳐 실행하는 조치 이름
TICKET_STATUS = {"자동 실행": "조치됨", "승인 대기": "승인 대기", "차단 금지": "조치 없음", "조치 없음": "조치 없음"}  # 처리 결과를 Unit 6 티켓의 알림 상태 이름으로 바꾸는 딕셔너리


def load_context():                                                                     # 인자가 없는 함수
    """설정 파일 네 개를 읽고 새 연습용 시스템 상태를 만들어 딕셔너리 하나로 리턴한다. 엔진이 알림을 처리하는 데 쓰는 재료를 한 번에 준비할 때 쓴다."""
    context = {                                                                         # 엔진이 쓰는 재료를 담을 딕셔너리
        "registry": load_json("config/playbook_registry.json"),                         # 플레이북 리스트
        "policy": load_json("config/approval_policy.json"),                             # 승인 게이트 정책
        "ip_users": load_json("ip_users.json"),                                         # IP 별 사용 계정 딕셔너리
        "ticket_rules": load_json("config/escalation_rules.json"),                      # 등급별 응답 기한(분) 설정
        "state": new_state(),                                                           # 연습용 시스템 상태 : 실행할 때마다 처음 상태에서 시작한다
        "tickets": [],                                                                  # 만든 티켓을 모을 빈 리스트
    }
    return context                                                                      # 재료 딕셔너리를 리턴한다


def make_request(alert, action, context):                                               # 알림 · 조치 이름 · 엔진 재료를 받는 함수
    """알림 한 건과 조치 이름으로 승인 게이트가 읽는 조치 요청 딕셔너리를 만든다. 위험 점수에 쓰는 「그 IP 를 함께 쓰는 계정 수」를 채울 때 쓴다."""
    users_on_ip = 0                                                                     # 그 IP 를 쓰는 계정 수 : 계정 조치이면 0 — 미리 채운 줄
    if action == "IP 차단":                                                             # 조치가 IP 차단이면 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 1. count_users_on_ip(alert["entity"], context["ip_users"]) 의 결과를 users_on_ip 에 저장한다
    request = {                                                                         # 승인 게이트가 읽는 조치 요청 한 건 — 미리 채운 줄
        "id": alert["id"],                                                              # 요청 번호는 알림 번호를 쓴다
        "incident": alert["id"],                                                        # 인시던트 번호
        "action": action,                                                               # 조치 이름
        "target": alert["entity"],                                                      # 조치 대상(계정 또는 IP)
        "grade": alert["grade"],                                                        # 알림 등급
        "users_on_ip": users_on_ip,                                                     # 그 IP 를 쓰는 계정 수
        "target_count": 1,                                                              # 알림 한 건은 대상 하나를 조치한다
    }
    return request                                                                      # 조치 요청을 리턴한다 — 미리 채운 줄


def execute_action(request, context):                                                   # 조치 요청과 엔진 재료를 받는 함수
    """계정 잠금이면 lock_account, IP 차단이면 block_ip 로 조치를 실행하고 조치 기록 한 건을 리턴한다. 승인 게이트가 자동으로 정한 조치를 실제로 실행할 때 쓴다."""
    state = context["state"]                                                            # 연습용 시스템 상태 — 미리 채운 줄
    vip_accounts = context["policy"]["vip_accounts"]                                    # VIP 계정 리스트 — 미리 채운 줄
    if request["action"] == "계정 잠금":                                                # 조치가 계정 잠금이면 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 2. lock_account(request["target"], state, vip_accounts, request["incident"], ENGINE_REASON) 의 결과를 record 에 저장한다
    else:                                                                               # 아니면 IP 차단이다 — 미리 채운 줄
        # 3. block_ip(request["target"], state, request["incident"], ENGINE_REASON, DEFAULT_TTL) 의 결과를 record 에 저장한다
    return record                                                                       # 조치 기록을 리턴한다 — 미리 채운 줄


def run_step(alert, action, context):                                                   # 알림 · 조치 이름 · 엔진 재료를 받는 함수
    """조치 하나를 승인 게이트에 묻고, 자동으로 정해졌을 때만 실행해서 결정 · 이유 · 실행 여부를 담은 딕셔너리를 리턴한다. 조치마다 한 번씩 쓴다."""
    request = make_request(alert, action, context)                                      # 승인 게이트에 보낼 조치 요청을 만든다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. decide_gate(request, context["policy"]) 의 두 결과를 decision, reasons 에 저장한다
    step = {                                                                            # 조치 하나의 결과 : 처음에는 실행하지 않은 것으로 적는다 — 미리 채운 줄
        "action": action,                                                               # 조치 이름
        "target": alert["entity"],                                                      # 조치 대상
        "decision": decision,                                                           # 승인 게이트의 결정
        "reasons": reasons,                                                             # 결정 이유 리스트
        "executed": False,                                                              # 실행했는지
        "before": "",                                                                   # 조치 전 상태
        "after": "",                                                                    # 조치 후 상태
        "request": request,                                                             # 승인 게이트가 본 조치 요청(나중에 점검할 때 다시 쓴다)
    }
    # 5. decision 이 "자동" 이면 (if, ==)
        record = execute_action(request, context)                                       # 조치를 실행하고 조치 기록을 받는다 — 미리 채운 줄
        step["executed"] = True                                                         # 실행했다고 적는다 — 미리 채운 줄
        step["before"] = record["before"]                                               # 조치 전 상태를 적는다 — 미리 채운 줄
        step["after"] = record["after"]                                                 # 조치 후 상태를 적는다 — 미리 채운 줄
    return step                                                                         # 조치 하나의 결과를 리턴한다 — 미리 채운 줄


def decide_outcome(steps):                                                              # 조치 결과 리스트를 받는 함수
    """조치 결과들로 알림 전체의 처리 결과(승인 대기 · 차단 금지 · 자동 실행 · 조치 없음)를 정한다. 사람이 먼저 봐야 하는 결과부터 판단한다."""
    decisions = []                                                                      # 조치마다 승인 게이트의 결정을 모을 빈 리스트
    for step in steps:                                                                  # 조치 결과를 하나씩 꺼낸다
        decisions.append(step["decision"])                                              # 결정을 추가한다
    if "승인 필요" in decisions:                                                        # 승인이 필요한 조치가 있으면
        return "승인 대기"                                                              # 사람의 승인을 기다리는 알림이다
    if "차단 금지" in decisions:                                                        # 차단 금지인 조치가 있으면
        return "차단 금지"                                                              # 실행하지 않은 알림이다
    if "자동" in decisions:                                                             # 자동으로 정해진 조치가 있으면
        return "자동 실행"                                                              # 자동으로 실행한 알림이다
    return "조치 없음"                                                                  # 승인 게이트를 거칠 조치가 없으면 조치 없음이다


def open_ticket(alert, steps, playbook_id, outcome, context):                           # 알림 · 조치 결과 리스트 · 플레이북 번호 · 처리 결과 · 엔진 재료를 받는 함수
    """처리 결과를 Unit 6 티켓 형식의 알림으로 바꿔 make_ticket 으로 티켓을 만들고 티켓 리스트에 추가한다. 조치를 했든 안 했든 담당자가 볼 티켓을 남길 때 쓴다."""
    done_list = []                                                                      # 실행한 조치를 「조치: 전 → 후」 문장으로 모을 빈 리스트
    for step in steps:                                                                  # 조치 결과를 하나씩 꺼낸다
        if step["executed"]:                                                            # 실행한 조치이면
            done_text = step["action"] + ": " + step["before"] + " → " + step["after"]  # 조치와 전 · 후 상태를 한 문장으로 만든다
            done_list.append(done_text)                                                 # 문장을 추가한다
    rule_text = ", ".join(alert["reasons"])                                             # 탐지된 규칙 이름을 쉼표로 이어 한 문자열로 만든다
    ticket_alert = {                                                                    # Unit 6 티켓 함수가 읽는 알림 모양
        "id": alert["id"],                                                              # 알림 번호
        "minute": 0,                                                                    # 엔진을 실행한 시각 : 0분
        "entity": alert["entity"],                                                      # 대상
        "rule": rule_text,                                                              # 탐지된 규칙
        "grade": alert["grade"],                                                        # 등급
        "status": TICKET_STATUS[outcome],                                               # 처리 결과에 맞는 알림 상태
        "playbook": playbook_id,                                                        # 플레이북 번호
        "done": done_list,                                                              # 실행한 조치 문장 리스트
    }
    ticket_no = len(context["tickets"]) + 1                                             # 지금까지 만든 티켓 수에 1 을 더해 번호를 만든다
    ticket = make_ticket(ticket_alert, ticket_no, context["ticket_rules"], NEXT_STEPS)  # Unit 6 함수로 티켓을 만든다
    context["tickets"].append(ticket)                                                   # 티켓 리스트에 추가한다
    return ticket                                                                       # 만든 티켓을 리턴한다


def run_soar_pipeline(alert, context):                                                  # 알림 한 건과 엔진 재료를 받는 함수
    """알림 한 건을 플레이북 찾기 → 조치마다 승인 게이트 → 티켓 만들기 순서로 처리하고 결과 기록 한 건을 리턴한다. 알림마다 한 번씩 쓴다."""
    playbooks = match_playbooks(alert, context["registry"])                             # Unit 1 함수로 맞는 플레이북을 찾는다 — 미리 채운 줄
    playbook_id = "없음"                                                                # 맞는 플레이북이 없으면 「없음」으로 남긴다 — 미리 채운 줄
    steps = []                                                                          # 조치마다 결과를 모을 빈 리스트 — 미리 채운 줄
    for playbook in playbooks:                                                          # 맞는 플레이북을 하나씩 꺼낸다 — 미리 채운 줄
        playbook_id = playbook["id"]                                                    # 플레이북 번호를 적는다 — 미리 채운 줄
        for action in playbook["actions"]:                                              # 플레이북의 액션을 하나씩 꺼낸다 — 미리 채운 줄
            # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
            # 6. action 이 CONTAINMENT_ACTIONS 안에 있으면 (if, in)
                step = run_step(alert, action, context)                                 # 승인 게이트를 거쳐 실행한다 — 미리 채운 줄
                steps.append(step)                                                      # 조치 결과를 추가한다 — 미리 채운 줄
    outcome = decide_outcome(steps)                                                     # 알림 전체의 처리 결과를 정한다 — 미리 채운 줄
    ticket = open_ticket(alert, steps, playbook_id, outcome, context)                   # 티켓을 만든다 — 미리 채운 줄
    result = {                                                                          # 알림 한 건의 결과 기록 — 미리 채운 줄
        "incident": alert["id"],                                                        # 알림 번호
        "entity": alert["entity"],                                                      # 대상
        "grade": alert["grade"],                                                        # 등급
        "playbook": playbook_id,                                                        # 플레이북 번호
        "outcome": outcome,                                                             # 처리 결과
        "steps": steps,                                                                 # 조치마다 결과 리스트
        "ticket": ticket["id"],                                                         # 티켓 번호
        "error": "",                                                                    # 오류 문장 : 정상이면 비어 있다
    }
    return result                                                                       # 결과 기록을 리턴한다 — 미리 채운 줄


def make_failure_result(alert, error):                                                  # 알림 한 건과 오류를 받는 함수
    """처리하지 못한 알림의 결과 기록 한 건을 만든다. 오류 이름과 내용을 남겨 담당자가 어떤 알림이 왜 멈췄는지 알 수 있게 할 때 쓴다."""
    error_name = type(error).__name__                                                   # 오류의 종류 이름(예: KeyError)
    error_text = error_name + ": " + str(error)                                         # 오류 이름과 내용을 한 문장으로 만든다
    result = {                                                                          # 실패한 알림의 결과 기록
        "incident": alert.get("id", "번호 없음"),                                       # 알림 번호 : 키가 없으면 「번호 없음」
        "entity": alert.get("entity", ""),                                              # 대상 : 키가 없으면 빈 문자열
        "grade": alert.get("grade", ""),                                                # 등급 : 키가 없으면 빈 문자열
        "playbook": "없음",                                                             # 플레이북을 찾기 전에 멈췄을 수 있다
        "outcome": "실패",                                                              # 처리 결과는 실패
        "steps": [],                                                                    # 실행한 조치 없음
        "ticket": "",                                                                   # 티켓 없음
        "error": error_text,                                                            # 오류 문장
    }
    return result                                                                       # 실패 기록을 리턴한다


def run_all(alerts, context):                                                           # 알림 리스트와 엔진 재료를 받는 함수
    """알림을 하나씩 처리하되, 오류가 난 알림은 실패 기록만 남기고 다음 알림으로 넘어간다. 알림 하나의 오류가 나머지 알림의 처리를 막지 않게 할 때 쓴다."""
    results = []                                                                        # 알림마다 결과 기록을 모을 빈 리스트 — 미리 채운 줄
    for alert in alerts:                                                                # 알림을 하나씩 꺼낸다 — 미리 채운 줄
        try:                                                                            # 오류가 날 수 있는 처리를 시작한다 — 미리 채운 줄
            # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
            # 7. run_soar_pipeline(alert, context) 의 결과를 result 에 저장한다
        # 8. 어떤 종류의 오류든 error 에 저장해 받는다 (except, Exception, as)
            result = make_failure_result(alert, error)                                  # 실패 기록을 만든다 — 미리 채운 줄
        results.append(result)                                                          # 정상 결과든 실패 기록이든 결과 리스트에 추가한다 — 미리 채운 줄
    return results                                                                      # 결과 기록 리스트를 리턴한다 — 미리 채운 줄
```

**`exercise10-1_run.py`** — 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다.

```python
from incident import load_json, save_json                                                # Unit 1 파일의 JSON 읽기 · 쓰기 함수를 불러온다
from soar_engine import load_context, run_all                                            # 방금 만든 엔진 함수를 불러온다

LOG_PATH = "engine_log.json"                                                             # 처리 결과를 저장할 파일 이름
TICKET_PATH = "engine_tickets.json"                                                      # 만든 티켓을 저장할 파일 이름

context = load_context()                                                                 # 플레이북 · 승인 정책 · 설정 · 연습용 시스템 상태를 한꺼번에 읽는다
alerts = load_json("engine_alerts.json")                                                 # 오늘 들어온 알림 파일을 리스트로 읽는다
print("--- 단계 1: 불러온 알림", len(alerts), "건 · 플레이북", len(context["registry"]), "개 · 승인 기준", context["policy"]["approval_score"], "점")  # 단계 1 시작을 알리는 줄

results = run_all(alerts, context)                                                       # 알림을 하나씩 엔진으로 처리한다
counts = {"자동 실행": 0, "승인 대기": 0, "차단 금지": 0, "조치 없음": 0, "실패": 0}     # 처리 결과마다 알림 수 : 처음에는 모두 0
print("--- 단계 2: 알림마다 처리 결과")                                                  # 단계 2 시작을 알리는 줄
for result in results:                                                                   # 결과 기록을 하나씩 꺼낸다
    outcome = result["outcome"]                                                          # 이 알림의 처리 결과 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 9. counts[outcome] 에 counts[outcome] + 1 을 저장한다 (1 늘린다)
    if outcome == "실패":                                                                # 처리하지 못한 알림이면
        print(result["incident"], result["entity"], "→", outcome, "·", result["error"])  # 알림과 오류를 출력한다
    else:                                                                                # 처리한 알림이면
        print(result["incident"], result["entity"], result["grade"], "→", outcome, "·", result["playbook"], "· 티켓", result["ticket"])  # 알림과 처리 결과를 출력한다
    for step in result["steps"]:                                                         # 조치 결과를 하나씩 꺼낸다
        reason_text = ", ".join(step["reasons"])                                         # 결정 이유 리스트를 쉼표로 이어 한 문자열로 만든다
        print("   ", step["action"], step["target"], "→", step["decision"], "·", reason_text)  # 조치와 승인 게이트의 결정을 출력한다
        if step["executed"]:                                                             # 실행한 조치이면
            print("   ", "실행:", step["before"], "→", step["after"])                    # 조치 전 · 후 상태를 출력한다

print("--- 단계 3: 처리 결과별 알림 수")                                                 # 단계 3 시작을 알리는 줄
for outcome in counts:                                                                   # 처리 결과 이름을 하나씩 꺼낸다
    print(outcome, ":", counts[outcome], "건")                                           # 결과 이름과 알림 수를 출력한다

save_json(results, LOG_PATH)                                                             # 결과 기록 리스트를 파일에 저장한다
save_json(context["tickets"], TICKET_PATH)                                               # 만든 티켓 리스트를 파일에 저장한다
print("--- 단계 4:", LOG_PATH, "에", len(results), "건 ·", TICKET_PATH, "에 티켓", len(context["tickets"]), "장 저장")  # 단계 4 시작을 알리는 줄과 저장한 수
```

**순서**

1. **[터미널]** 파일 두 개를 만들고 **[VS Code]** 에서 열어 붙여 넣습니다.
   ```bash
   pwd
   touch soar_engine.py exercise10-1_run.py
   ls
   ```
2. **[VS Code]** `soar_engine.py` 1 ~ 8번, `exercise10-1_run.py` 9번을 씁니다. 막히면 위 문법 상자와 아래 「Exercise 10-1 한눈에」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise10-1_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 과 단계 4 는 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 알림마다 1줄이고, 조치가 있는 알림은 조치마다 1 ~ 2줄이 더 붙습니다. 단계 3 은 5줄입니다.
5. **[VS Code]** 새로 생긴 `engine_log.json` 과 `engine_tickets.json` 을 열어 <mark>`INC-402` 의 `error` 와 `TCK-1` 의 `done`</mark> 을 읽습니다.
6. **[보고서]** Unit 10 의 `## Exercise 10-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 처리 결과별 알림 수와 승인 대기인 알림 번호를 적어 주세요.
   - (나) [핵심 질문] `INC-402` 는 실패인데 `INC-403` ~ `INC-408` 은 처리됐습니다. 단계 2 의 `INC-402` 오류 문장과 `run_all` 의 `except` 줄을 근거로 그 이유를 적고, `try` / `except` 가 없으면 `INC-402` 이후의 알림이 어떻게 되는지 적어 주세요.
   - (다) [핵심 질문] `INC-404` 와 `INC-406` 은 둘 다 high 등급인데 결과가 「차단 금지」와 「승인 대기」로 다릅니다. 단계 2 의 결정 이유를 근거로 그 차이를 적고, 승인 게이트가 `execute_action` 보다 먼저 와야 하는 이유도 적어 주세요.

## Exercise 10-1 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 함수 결과를 변수에 저장하기 | `users_on_ip = count_users_on_ip(alert["entity"], context["ip_users"])` |
| 두 결과를 함께 받기 | `decision, reasons = decide_gate(request, context["policy"])` |
| 같으면 | `if decision == "자동":` |
| 리스트 안에 있으면 | `if action in CONTAINMENT_ACTIONS:` |
| 어떤 종류의 오류든 받기 | `except Exception as error:` |
| 1 늘려 다시 저장하기 | `counts[outcome] = counts[outcome] + 1` |
---
