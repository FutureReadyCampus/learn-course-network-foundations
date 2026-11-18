---
id: m5-u03-l02
title: 실습 3-1 · 담당자 승인·거절 적용과 권한 확인
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/120_day02_pm_approval_retry_flow.md
  mission_id: GichanSource.m5-1110-pm-approval-retry-flow
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 3-1 · 담당자 승인·거절 적용과 권한 확인

## 이번 의뢰: 승인 결과 받기

> **오늘 들어온 일**
>
> - **상황**: 알림 5건 가운데 3건이 담당자의 허락(승인)을 기다리는 상태입니다. `INC-002`(`seoyeon` 의 대량 다운로드), `INC-003`(계정 관리자 `gaeun`, 잠기면 업무에 큰 영향을 주는 VIP 계정), `INC-005`(서버의 여러 주소에 차례로 요청을 보내 약점을 찾는 경로 스캔을 한 IP `198.51.100.90`)입니다. 오늘 담당자가 메신저에서 승인이나 거절을 눌렀습니다.
> - **문제**:
> - 프로그램이 담당자가 누른 결과를 받지 못해서, 담당자가 계정 관리 화면을 열어 같은 일을 다시 해야 합니다.
> - 결과를 받는 기능을 만들더라도 누른 사람을 확인하지 않으면, 승인 권한이 없는 인턴 계정 `intern01` 의 승인으로 IP 차단이 실행됩니다.
> - **부탁**: 승인 권한이 있는 담당자의 결정만 받아서, 승인이면 실행하고 거절이면 알림을 끝내 주세요. 누가 무엇을 결정했는지는 모두 기록해 주세요.
> - **바뀌는 점**: 담당자는 단추 한 번으로 끝납니다. 권한이 없는 승인은 실행되지 않고 기록으로만 남습니다. 오늘 샘플에서는 `INC-002` 는 실행되고, `INC-003` 은 거절로 끝나고, `INC-005` 는 권한이 없어 멈춥니다. 상황과 이름은 설명을 위한 예시입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 1.1 승인 처리는 「권한 확인 → 실행 또는 종료 → 기록」 순서다

담당자가 승인이나 거절을 누르면 프로그램이 그 결정을 받아 처리해야 합니다. 순서는 세 단계입니다.

1. **권한 확인**: 누른 사람이 승인 권한이 있는 사람인지 먼저 봅니다. 권한이 없는 사람의 승인으로 실행되면 안 되기 때문입니다.
2. **실행 또는 종료**: 승인이면 멈춰 있던 액션을 실행하고, 거절이면 알림을 종료합니다.
3. **기록**: 어느 경우든 누가 무엇을 했는지 감사 기록에 남깁니다. 나중에 누가 허락했는지 확인하려면 기록이 필요하기 때문입니다.

오늘 담당자 결정은 세 건입니다.

| 알림 | 결정한 사람 | 결과 | 기대하는 처리 |
|---|---|---|---|
| INC-002 | `kim.sec` (권한 있음) | 승인 | 액션을 실행하고 상태를 `조치됨` 으로 바꾼다 |
| INC-003 | `kim.sec` (권한 있음) | 거절 | 실행하지 않고 `종료` 로 옮기고 이유를 기록한다 |
| INC-005 | `intern01` (권한 없음) | 승인 | <mark>결과가 승인이어도 실행하지 않고</mark> 「권한 없는 사람이 승인하려 했다」는 기록만 남긴다 |

- **`item`**: 승인 대기 알림 한 건입니다. `pending.json` 에 들어 있는 알림 하나입니다.
- **`decision`**: 담당자의 결정 한 건입니다. 누가 눌렀는지, 승인인지 거절인지, 남긴 한마디가 들어 있습니다.
- **`APPROVERS`**: 승인 권한이 있는 담당자 이름 리스트입니다.
- **`action_log`**: 감사 기록 한 건씩을 추가해 모으는 리스트입니다.

함수는 파일 세 곳에 나뉘어 있고, 직접 쓰는 곳은 **아홉 군데**입니다.

```
audit.py        log_line          : 기록 한 건을 딕셔너리로 만든다 (1번)
approvals.py    is_authorized     : 승인한 사람이 권한 목록에 있는지 확인한다 (2번)
                execute_actions   : 액션을 하나씩 실행한다 (3번)
                apply_decision    : 권한이 없으면 기록만 남기고 멈춘다 (4 · 5번)
                finish_decision   : 승인이면 실행하고 끝낸다 (6 · 7번) / 아니면 종료하고 거절 사유를 기록한다 (미리 채움)
실행 파일       exercise3-1_run.py  : 대기 건마다 결정이 있으면 apply_decision 을 호출한다 (8 · 9번)
```

> **여기부터 문제입니다.**

## 실습 3-1 · 권한 확인 후 담당자 결정 적용

**이런 상황이 있습니다**

- **지금은**: <mark>승인 대기 3건이 멈춰 있고, 담당자 결정 3건(승인 · 거절 · 권한 없는 승인)이 들어와 있습니다</mark>.
- **만드는 것**: 기록 한 건 만들기(`audit.py`), 권한 확인 · 실행 · 종료(`approvals.py`), 결정을 적용하는 함수를 부르는 실행 파일(`exercise3-1_run.py`).
- **실행하면**: <mark>단계 1: 승인 대기 건, 단계 2: 결정 적용 결과, 단계 3: 처리 뒤 연습용 시스템 상태, 단계 4: 감사 기록이 나옵니다.</mark>

**할 일**: 파일 세 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 ~ 4 를 읽습니다.

**`audit.py`** — 감사 기록 한 건을 만듭니다. `approvals.py` 와 실습 3-2 `flow.py` 가 불러다 씁니다. 직접 쓰는 곳은 1번입니다.

```python
def log_line(item, action, text):  # 인시던트 · 액션 · 결과 문장을 받는 함수
    """감사 기록(어떤 알림에 · 어떤 액션을 해서 · 결과가 무엇인지) 한 건을 딕셔너리로 만들어 리턴한다.
    모든 대응을 같은 모양으로 남겨 두면 나중에 한 목록으로 되짚을 수 있어서 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. 키 "incident"(item 의 "id"), "playbook"(item 의 "playbook"), "action"(action), "result"(text) 를 가진 딕셔너리를 entry 에 담는다
    return entry                   # 기록 한 건을 리턴한다
```

**`approvals.py`** — 권한을 확인하고 결정을 적용합니다. 실습 3-2 `flow.py` 도 불러다 씁니다. 직접 쓰는 곳은 2 ~ 7번입니다.

```python
from incident import change_status, run_action                                           # Unit 1 파일의 함수를 불러온다
from audit import log_line                                                               # 방금 만든 기록 함수를 불러온다

APPROVERS = ["kim.sec", "lee.soc"]                                                       # 승인할 권한이 있는 담당자 이름 리스트


def hold_for_approval(incident, playbook_id, actions, why, action_log):                  # 승인 대기로 멈출 인시던트와 정보를 받는 함수
    """알림의 상태를 분류됨으로 바꾸고 승인 대기 기록을 남긴 뒤, 담당자에게 보여 줄 대기 건 한 건으로 리턴한다.
    승인이 필요한 알림을 실행하지 않고 담당자에게 넘길 때 쓴다(실습 3-2 하루 흐름에서 호출한다).
    """
    incident["playbook"] = playbook_id                                                   # 어떤 플레이북 때문인지 적고
    incident["actions"] = actions                                                        # 승인되면 실행할 액션을 적고
    incident["why"] = why                                                                # 승인이 필요한 이유를 적는다
    change_status(incident, "분류됨")                                                    # 대응을 시작했으니 분류됨으로 옮기고
    action_log.append(log_line(incident, "전체", "승인 대기 — " + why))                  # 승인 대기 기록을 남긴다
    return incident                                                                      # 대기 건을 리턴한다


def is_authorized(approver):                                                             # 승인한 사람 이름을 받는 함수
    """승인한 사람이 승인 권한이 있는 담당자 목록(APPROVERS)에 있으면 True, 없으면 False 를 리턴한다.
    권한이 없는 사람이 누른 승인을 걸러 낼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. approver 가 APPROVERS 안에 있는지(in)의 결과를 리턴한다


def execute_actions(item, state, action_log, approver):                                  # 대기 건 · 연습용 시스템 · 기록 리스트 · 승인자를 받는 함수
    """대기 건에 적힌 액션을 하나씩 실행하고 누가 승인했는지 붙여 기록한 뒤, 알림을 조치됨으로 바꾸고 「실행 완료」를 리턴한다.
    담당자가 승인한 알림을 실제로 처리할 때 쓴다.
    """
    for action in item["actions"]:                                                       # 액션을 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. run_action(action, item, state) 의 결과를 result 에 담는다
        action_log.append(log_line(item, action, result + " (승인: " + approver + ")"))  # 승인자를 붙여 기록한다 — 미리 채운 줄
    change_status(item, "조치됨")                                                        # 모두 실행했으니 조치됨으로 옮긴다
    return "실행 완료"                                                                   # 실행 완료를 리턴한다


def reject_unauthorized(item, approver, action_log):                                     # 대기 건 · 승인자 · 기록 리스트를 받는 함수
    """권한 없는 사람이 승인하려 한 사실을 기록에 남기고 「권한 없음」을 리턴한다. 알림의 상태는 바꾸지 않는다.
    누가 권한 없이 승인하려 했는지 보안 기록으로 남길 때 쓴다.
    """
    action_log.append(log_line(item, "전체", "권한 없음 — 승인 시도: " + approver))      # 권한 없음 기록을 남기고
    return "권한 없음"                                                                   # 권한 없음을 리턴한다


def apply_decision(item, decision, state, action_log):                                   # 대기 건 · 담당자 결정 · 연습용 시스템 · 기록 리스트를 받는 함수
    """담당자의 결정(승인 또는 거절)을 알림에 적용한다. 먼저 결정한 사람에게 권한이 있는지 확인한다.
    담당자의 결정을 받아 처리할 때 쓰고, 결과는 「권한 없음」 · 「실행 완료」 · 「거절 처리」 중 하나로 리턴한다.
    """
    approver = decision["approver"]                                                      # 결정한 담당자 이름 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. is_authorized(approver) 가 거짓이면 (if, not)
    # 5.   reject_unauthorized(item, approver, action_log) 의 결과를 리턴한다
    return finish_decision(item, decision, state, action_log)                            # 권한이 있으면 결정을 적용한다 — 미리 채운 줄


def finish_decision(item, decision, state, action_log):                                  # 대기 건 · 담당자 결정 · 연습용 시스템 · 기록 리스트를 받는 함수
    """권한 확인을 통과한 결정을 처리한다. 승인이면 액션을 실행하고, 거절이면 알림을 종료하고 거절 사유를 기록한다.
    권한이 확인된 뒤 결정 내용에 따라 나눠 처리할 때 쓴다.
    """
    approver = decision["approver"]                                                      # 결정한 담당자 이름 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 6. decision["result"] 가 "승인" 이면 (if, ==)
    # 7.   execute_actions(item, state, action_log, approver) 의 결과를 리턴한다
    change_status(item, "종료")                                                          # 승인이 아니면 거절로 보고 종료로 옮긴다 — 미리 채운 줄
    action_log.append(log_line(item, "전체", "거절됨 (승인: " + approver + " — " + decision["comment"] + ")"))  # 거절 사유를 기록한다 — 미리 채운 줄
    return "거절 처리"                                                                   # 거절 처리를 리턴한다 — 미리 채운 줄
```

**`exercise3-1_run.py`** — 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 실행하면 결과를 출력합니다.

```python
from incident import load_json                                                              # Unit 1 파일의 함수를 불러온다
from approvals import apply_decision                                                        # 방금 만든 결정 적용 함수를 불러온다

pending = load_json("pending.json")                                                         # 승인 대기 3건을 읽는다
decisions = load_json("decisions.json")                                                     # 담당자 결정을 읽는다
state = {"locked_users": [], "blocked_ips": [], "tickets": [], "notifications": []}         # 깨끗한 연습용 시스템 상태
action_log = []                                                                             # 감사 기록을 담을 빈 리스트

print("--- 단계 1: 승인 대기 건")                                                           # 단계 1 시작을 알리는 줄
for item in pending:                                                                        # 대기 건을 하나씩 꺼낸다
    print(item["id"], item["entity"], "·", item["playbook"], "·", item["why"])              # 번호 · 대상 · 플레이북 · 이유를 출력한다

print("--- 단계 2: 담당자 결정 처리")                                                       # 단계 2 시작을 알리는 줄
for item in pending:                                                                        # 대기 건을 하나씩 꺼낸다
    result_text = "결정 없음"                                                               # 결정이 없으면 이 글자가 남는다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 8. item["id"] 가 decisions 안에 있으면 (if, in)
    # 9.   apply_decision(item, decisions[item["id"]], state, action_log) 의 결과를 result_text 에 담는다
    print(item["id"], item["entity"], "->", result_text, "(상태: " + item["status"] + ")")  # 한 줄로 출력한다

print("--- 단계 3: 처리 뒤 연습용 시스템 상태")                                             # 단계 3 시작을 알리는 줄
print("잠긴 계정:", state["locked_users"])                                                  # 잠긴 계정을 출력한다
print("차단한 IP:", state["blocked_ips"])                                                   # 차단한 IP 를 출력한다
print("티켓:", len(state["tickets"]), "건 · 담당자 알림:", len(state["notifications"]), "건")  # 티켓과 알림 수를 출력한다

print("--- 단계 4: 감사 기록")                                                              # 단계 4 시작을 알리는 줄
for entry in action_log:                                                                    # 기록을 하나씩 꺼낸다
    print(entry["incident"], entry["playbook"], entry["action"], ":", entry["result"])      # 인시던트 · 플레이북 · 액션 · 결과를 출력한다
```

**순서**

1. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `audit.py` · `approvals.py` · `exercise3-1_run.py` 세 파일을 하나씩 만들고(파일 이름 그대로), 코드를 붙여 넣어 저장합니다.
2. **[VS Code]** `audit.py` 1번, `approvals.py` 2 ~ 7번, `exercise3-1_run.py` 8 · 9번을 씁니다. 막히면 아래 「실습 3-1 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise3-1_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 3줄, 단계 2 도 3줄, 단계 3 은 3줄, 단계 4 는 감사 기록 4줄입니다.
5. **[보고서]** `report_u3.md` 의 `## 실습 3-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 처리 뒤 티켓 수 · 담당자 알림 수 · `분류됨` 으로 남은 알림의 번호를 각각 적어 주세요.
   - (나) [핵심 질문] INC-005 는 결정이 `승인` 인데 실행되지 않았습니다. 단계 2 와 단계 4 의 출력을 근거로 그 이유를 적어 주세요. 그리고 권한 확인이 없을 때 생길 위험도 적어 주세요.
   - (다) [핵심 질문] INC-003 이 승인 대기가 된 이유(단계 1), 거절된 뒤의 상태, 감사 기록에 남은 내용을 각각 적어 주세요.

## 실습 3-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 딕셔너리를 만들어 변수에 저장하기 | `entry = {"incident": item["id"], ..., "result": text}` |
| 리스트 안에 있는지 확인해 참(`True`) 또는 거짓(`False`)을 리턴한다 | `return approver in APPROVERS` |
| 함수 결과를 변수에 담기 | `result = run_action(action, item, state)` |
| 거짓이면 | `if not is_authorized(approver):` |
| 다른 함수의 결과를 그대로 리턴 | `return reject_unauthorized(item, approver, action_log)` · `return execute_actions(item, state, action_log, approver)` |
| 값이 같으면 | `if decision["result"] == "승인":` |
| 키가 있으면 | `if item["id"] in decisions:` |

---
