---
id: m5-u02-l04
title: 실습 2-3 · 중복 실행과 잠금 수 제한하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/118_day02_am_context_route_safety.md
  mission_id: GichanSource.m5-1110-am-context-route-safety
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 2-3 · 중복 실행과 잠금 수 제한하기

## 이번 의뢰: 중복 처리와 대량 잠금

> **오늘 들어온 일**
>
> - **상황**: Unit 1에서 만든 실행기(playbook runner, 플레이북 러너: 플레이북의 액션을 실제로 실행하는 프로그램)는 같은 알림 파일을 두 번 처리하면 `dami` 계정을 두 번 잠그고 티켓(ticket, 티켓: 담당자에게 일을 맡기려고 만드는 작업 요청 기록)을 두 번 생성합니다. 더 큰 위험은 인사 시스템의 오류입니다. 직원 전체가 퇴사자로 잘못 표시되면 퇴사자 알림이 대량으로 들어옵니다. 오늘 샘플에서는 이런 알림 7건(계정 6개)이 한꺼번에 들어옵니다.
> - **문제**: 실행기는 알림 수만큼 계정을 모두 잠급니다. 7건이 들어오면 서로 다른 계정 6개가 잠기고(`dami` 알림이 두 건이라 잠긴 계정 리스트에는 `dami` 가 두 번 기록됩니다), 100건이 들어오면 100개가 잠깁니다. 이 샘플에서 실제 퇴사자는 `dami` 한 명뿐입니다.
> - **부탁**: 이미 끝난 인시던트는 다시 처리하지 말고, 이미 잠긴 계정은 다시 잠그지 마세요. 또 한 번 실행할 때 잠글 수 있는 계정은 최대 3개로 제한해 주세요.
> - **바뀌는 점**: 같은 알림을 두 번 처리해도 `dami` 는 한 번만 잠기고, 알림이 몰려도 잠기는 계정이 3개를 넘지 않습니다. 그 사이에 담당자가 확인할 시간이 생깁니다.

## 3.1 안전장치(guardrail) 두 가지 — 중복 실행 방지와 영향 범위 제한

**안전장치**(guardrail, 가드레일: 자동 대응이 잘못 실행되어도 피해가 커지지 않도록 두는 사전 점검 · 제한 장치)는 실행기가 액션(계정 잠금처럼 대응으로 하는 동작 하나)을 실행하기 전에 「이 액션을 지금 실행해도 되는가」를 한 번 더 점검하는 장치입니다. 위험도가 높은 자동 조치는 신뢰도나 담당자 승인 같은 조건을 통과한 뒤에만 실행하도록 제한하는 것이 일반적인 설계 방식입니다. 코드에 나오는 용어는 다음과 같습니다.

- **`state`**: 연습용 시스템(실제 서버를 대신하는 시스템)의 현재 상태입니다. 잠긴 계정(`locked_users`) · 차단한 IP · 티켓을 저장한 딕셔너리입니다.
- **`DONE_STATUSES`**: 대응이 이미 끝난 상태 `조치됨` · `보고됨` · `종료` 를 모은 리스트입니다.
- **`MAX_LOCKS_PER_RUN`**: 한 번 실행에서 잠글 수 있는 계정의 최대 수이고 값은 3입니다.

| 안전장치 | 방지하는 일 | 오늘 수업에서 |
|---|---|---|
| **중복 실행 방지**(멱등성, idempotency, 아이뎀포턴시: 같은 조치를 여러 번 실행해도 한 번 실행한 것과 결과가 같도록 하는 성질) | 같은 알림이 두 번 와서 같은 대응을 두 번 하는 일 | 이미 끝난 인시던트는 실행하지 않고(미리 채움), 이미 잠긴 계정은 다시 잠그지 않는다 (1 · 2번) |
| **영향 범위 제한**(blast radius limit, 블라스트 레이디어스 리밋: 조치가 잘못됐을 때 영향을 받는 대상의 범위에 상한을 두는 것) | 잘못된 입력으로 계정이 대량으로 잠기는 일 | 한 번 실행에서 잠글 수 있는 계정을 `MAX_LOCKS_PER_RUN`(3개)까지만 허용한다 (3 · 4번) |

- 중복 실행 방지의 예: `dami` 를 잠그라는 요청이 두 번 들어와도 잠금은 한 번만 실행됩니다. 영향 범위 제한의 예: 알림이 100건 들어와도 이번 실행에서 잠기는 계정은 3개까지입니다.
- 한도는 **잘못된 알림을 알아내지는 못합니다.** 잘못된 알림이 들어와도 잠기는 계정이 3개를 넘지 않게 제한할 뿐이며, 한도를 넘은 건은 「담당자 확인 필요」라고 기록합니다.
- 오늘 `bulk_incidents.json` 은 인사 오류로 몰린 퇴사자 알림 7건(계정 6개, `dami` 알림이 두 건)입니다. `users_info.json` 의 `employed` 를 보면 <mark>실제 퇴사자는 `dami` 한 명뿐입니다.</mark>

<h2>문법 상자 — <code>startswith</code> 는 문자열이 지정한 문자열로 시작하는지 확인한다</h2>

```python
result_text = "건너뜀: 이미 잠겨 있음"
print(result_text.startswith("건너뜀"))
print(result_text.startswith("실행"))
```

| 코드 | 결과 | 뜻 |
|---|---|---|
| `result_text.startswith("건너뜀")` | `True` | 글자가 「건너뜀」으로 시작한다 |
| `result_text.startswith("실행")` | `False` | 「실행」으로 시작하지 않는다 |

직접 쓰는 곳은 함수와 실행 파일을 합쳐 **아홉 군데**입니다.

```
safe_runner.py   find_skip_reason : 이미 잠긴 계정이면 (1 · 2번), 잠근 계정 수가 한도 이상이면 (3 · 4번) 건너뛸 이유를 리턴한다
                 safe_run_action  : 이유가 있으면 그 이유를 리턴하고 (5 · 6번), 없으면 Unit 1의 run_action 으로 실행한다 (7번)
                 run_playbook_safe · process_safe : 결과를 이미 처리됨 · 승인 대기 · 일부 건너뜀 · 실행 완료로 나누고, 결과마다 몇 건인지 센다 (미리 채움)
실행 파일        exercise2-3_run.py : 기록에서 「건너뜀」으로 시작하는 결과만 골라 출력한다 (8 · 9번)
```

## 실습 2-3 · 중복 방지와 잠금 3개 제한

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>같은 알림을 두 번 처리하면 계정이 두 번 잠기고, 인사 오류 알림이 몰리면 모든 계정이 잠깁니다</mark>.
- **만드는 것**: 건너뛸 이유 판정과 안전장치를 적용한 액션 실행(`safe_runner.py`), 건너뛴 액션 선별 출력(`exercise2-3_run.py`).
- **실행하면**: <mark>단계 1 ~ 2: Unit 1 방식의 결과, 단계 3 ~ 4: 안전한 방식의 결과, 마지막에 건너뛴 액션과 이유가 나옵니다.</mark>

**할 일**: 파일 세 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 Unit 1 방식과 안전한 방식의 차이를 읽습니다.

<h3><code>bulk_incidents.json</code></h3>

인사 시스템 오류로 몰린 퇴사자 알림 7건입니다(모두 `퇴사한 계정` · `high`). `INC-B01` 과 `INC-B02` 는 같은 계정 `dami` 의 알림으로, 번호가 다른 알림 두 건이 같은 계정을 가리키는 경우를 일부러 만들어 둔 것입니다.

```
[
  {"id": "INC-B01", "entity": "dami", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B02", "entity": "dami", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B03", "entity": "seoyeon", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B04", "entity": "gaeun", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B05", "entity": "jiwoo", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B06", "entity": "junho", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B07", "entity": "hana", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"}
]
```

<h3><code>safe_runner.py</code></h3>

안전장치를 건 실행기입니다. Unit 3의 실습 3-2에서 실패 처리를 더합니다. 직접 쓰는 곳은 1 ~ 7번입니다.

```python
from incident import change_status, match_playbooks, run_action, make_log_entry  # Unit 1 파일의 함수를 불러온다

DONE_STATUSES = ["조치됨", "보고됨", "종료"]  # 이미 대응이 끝난 상태들
MAX_LOCKS_PER_RUN = 3  # 한 번 실행에서 잠글 수 있는 계정의 최대 수


def find_skip_reason(action, entity, state):  # 액션 · 대상 · 연습용 시스템을 받는 함수
    """이 액션을 건너뛰어야 하면 그 이유 문장을, 건너뛸 필요가 없으면 빈 글자("")를 리턴한다.
    계정을 잠그기 전에 이미 잠긴 계정인지, 한 번에 잠글 수 있는 수를 넘었는지 확인할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. action 이 "계정 잠금" 이고(and) entity 가 state["locked_users"] 안에 있으면 (if, in)
    # 2.   "건너뜀: 이미 잠겨 있음" 을 리턴한다
    # 3. action 이 "계정 잠금" 이고(and) state["locked_users"] 의 개수(len)가 MAX_LOCKS_PER_RUN 이상이면 (if, >=)
    # 4.   "건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)" 를 리턴한다
    return ""  # 건너뛸 이유가 없으면 빈 글자를 리턴한다 — 미리 채운 줄


def safe_run_action(action, incident, state):  # 액션 · 인시던트 · 연습용 시스템을 받는 함수
    """액션을 실행하기 전에 건너뛸 이유가 있는지 먼저 확인한다. 이유가 있으면 실행하지 않고 그 이유를, 없으면 Unit 1의 run_action 으로 실행한 결과를 리턴한다.
    같은 일을 두 번 하거나 너무 많이 하는 것을 막고 싶을 때 쓴다.
    """
    entity = incident["entity"]  # 대응할 대상
    skip_reason = find_skip_reason(action, entity, state)  # 건너뛸 이유를 구한다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. skip_reason 이 빈 글자("")가 아니면 (if, !=)
    # 6.   skip_reason 을 리턴한다
    # 7. run_action(action, incident, state) 의 결과를 리턴한다 (건너뛸 이유가 없으면 원래대로 실행한다)


def run_playbook_safe(incident, playbook, state, action_log):  # 인시던트 · 플레이북 · 연습용 시스템 · 기록 리스트를 받는 함수
    """알림 한 건을 안전하게 처리한다. 이미 끝난 알림이면 건너뛰고, 승인이 필요하면 멈추고, 아니면 액션을 실행한다.
    처리 결과를 「실행 완료」 · 「승인 대기」 · 「이미 처리됨」 · 「일부 건너뜀」 중 하나로 리턴한다.
    """
    if incident["status"] in DONE_STATUSES:  # 이미 대응이 끝난 인시던트이면
        entry = make_log_entry(incident, playbook, "전체", "이미 처리됨 — 건너뜀")  # 건너뛴 기록을 만들고
        action_log.append(entry)  # 기록 리스트에 추가한다
        return "이미 처리됨"  # 이미 처리됨을 리턴한다
    change_status(incident, "분류됨")  # 대응을 시작하기 전에 분류됨 상태로 옮긴다
    if playbook["approval"] != "자동":  # 승인이 필요하면
        entry = make_log_entry(incident, playbook, "전체", "승인 대기")  # 승인 대기 기록을 만들고
        action_log.append(entry)  # 기록 리스트에 추가한다
        return "승인 대기"  # 승인 대기를 리턴한다
    skipped = False  # 건너뛴 액션이 있는지 : 처음에는 없다
    for action in playbook["actions"]:  # 액션을 하나씩 꺼낸다
        result = safe_run_action(action, incident, state)  # 안전한 방식으로 실행한다
        if result.startswith("건너뜀"):  # 결과 문장이 「건너뜀」으로 시작하면
            skipped = True  # 건너뛴 액션이 있다고 적는다
        entry = make_log_entry(incident, playbook, action, result)  # 기록을 만들고
        action_log.append(entry)  # 기록 리스트에 추가한다
    if skipped:  # 건너뛴 액션이 있으면
        return "일부 건너뜀"  # 조치됨으로 옮기지 않고 일부 건너뜀을 리턴한다
    change_status(incident, "조치됨")  # 모두 실행했으니 조치됨으로 옮긴다
    return "실행 완료"  # 실행 완료를 리턴한다


def process_safe(incidents, registry, state, action_log):  # 인시던트 리스트 · 플레이북 리스트 · 연습용 시스템 · 기록 리스트를 받는 함수
    """알림을 하나씩 맞는 플레이북으로 안전하게 처리하고, 결과를 한 줄씩 출력한다.
    결과마다 몇 건인지 센 딕셔너리를 리턴한다.
    """
    counts = {}  # 실행 결과마다 몇 건인지 셀 딕셔너리
    for incident in incidents:  # 인시던트를 하나씩 꺼낸다
        playbooks = match_playbooks(incident, registry)  # 맞는 플레이북을 찾는다
        result_text = "맞는 플레이북 없음"  # 처음에는 없다고 적어 둔다
        for playbook in playbooks:  # 맞는 플레이북을 하나씩 꺼낸다
            result_text = run_playbook_safe(incident, playbook, state, action_log)  # 안전하게 실행한다
        counts[result_text] = counts.get(result_text, 0) + 1  # 그 결과의 건수를 1 늘린다
        print(incident["id"], incident["entity"], "->", result_text, "(상태: " + incident["status"] + ")")  # 한 줄로 출력한다
    return counts  # 결과별 건수를 리턴한다
```

<h3><code>exercise2-3_run.py</code></h3>

8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. Unit 1의 `playbook_runner.py` 의 완성된 `run_playbook` 이 필요합니다.

```python
from incident import load_json, match_playbooks, INCIDENTS_PATH, REGISTRY_PATH  # Unit 1 파일의 함수를 불러온다
from playbook_runner import run_playbook  # Unit 1에서 만든 실행기를 불러온다
from safe_runner import process_safe, MAX_LOCKS_PER_RUN  # 방금 만든 안전한 실행기를 불러온다

BULK_PATH = "bulk_incidents.json"  # 인사 시스템 오류로 퇴사자 알림이 몰린 상황의 알림 파일 이름


def new_state():  # 인자가 없는 함수
    """잠긴 계정 · 차단한 IP · 티켓이 모두 비어 있는 연습용 시스템 상태를 새로 만들어 리턴한다.
    실험마다 깨끗한 상태에서 시작하고 싶을 때 쓴다.
    """
    state = {"locked_users": [], "blocked_ips": [], "tickets": [], "notifications": []}  # 비어 있는 상태 딕셔너리
    return state  # 상태를 리턴한다


def run_monday_way(incidents, registry, state, action_log):  # Unit 1 방식으로 처리하는 함수
    """Unit 1에서 만든 run_playbook 으로 알림을 모두 처리한다. 오늘 만든 안전장치는 쓰지 않는다.
    안전장치가 없으면 어떤 일이 생기는지 보고 싶을 때 쓴다.
    """
    for incident in incidents:  # 인시던트를 하나씩 꺼낸다
        playbooks = match_playbooks(incident, registry)  # 맞는 플레이북을 찾는다
        for playbook in playbooks:  # 맞는 플레이북을 하나씩 꺼낸다
            run_playbook(incident, playbook, state, action_log)  # Unit 1 방식으로 실행한다


registry = load_json(REGISTRY_PATH)  # 플레이북 등록 파일을 읽는다

print("--- 단계 1: Unit 1 방식(안전장치 없음)으로 같은 알림 5건을 두 번 처리")  # 단계 1 시작을 알리는 줄
incidents = load_json(INCIDENTS_PATH)  # 알림 5건을 읽는다
state = new_state()  # 깨끗한 상태로 시작한다
action_log = []  # 기록 리스트를 만든다
run_monday_way(incidents, registry, state, action_log)  # 첫 번째 처리
run_monday_way(incidents, registry, state, action_log)  # 같은 알림을 한 번 더 처리한다
print("잠긴 계정:", state["locked_users"])  # 잠긴 계정을 출력한다
print("티켓:", len(state["tickets"]), "건")  # 티켓 수를 출력한다

print("--- 단계 2: Unit 1 방식(안전장치 없음)으로 인사 오류 알림 7건 처리")  # 단계 2 시작을 알리는 줄
bulk_incidents = load_json(BULK_PATH)  # 인사 오류 알림 7건을 읽는다
state = new_state()  # 깨끗한 상태로 시작한다
action_log = []  # 기록 리스트를 만든다
run_monday_way(bulk_incidents, registry, state, action_log)  # Unit 1 방식으로 처리한다
locked_count = len(state["locked_users"])  # 잠긴 계정이 몇 개인지 센다
print("잠긴 계정", locked_count, "개:", state["locked_users"])  # 잠긴 계정 수와 이름을 출력한다

print("--- 단계 3: 안전한 방식으로 같은 알림 5건을 두 번 처리")  # 단계 3 시작을 알리는 줄
incidents = load_json(INCIDENTS_PATH)  # 알림 5건을 다시 읽는다
state = new_state()  # 깨끗한 상태로 시작한다
action_log = []  # 기록 리스트를 만든다
print("첫 번째 처리")  # 첫 번째 처리임을 알리는 줄
process_safe(incidents, registry, state, action_log)  # 안전한 방식으로 처리한다
print("두 번째 처리")  # 두 번째 처리임을 알리는 줄
process_safe(incidents, registry, state, action_log)  # 같은 알림을 한 번 더 처리한다
print("잠긴 계정:", state["locked_users"])  # 잠긴 계정을 출력한다
print("티켓:", len(state["tickets"]), "건")  # 티켓 수를 출력한다

print("--- 단계 4: 안전한 방식으로 인사 오류 알림 7건 처리 (한 번에 최대", MAX_LOCKS_PER_RUN, "개)")  # 단계 4 시작을 알리는 줄
bulk_incidents = load_json(BULK_PATH)  # 인사 오류 알림 7건을 다시 읽는다
state = new_state()  # 깨끗한 상태로 시작한다
action_log = []  # 기록 리스트를 만든다
counts = process_safe(bulk_incidents, registry, state, action_log)  # 안전한 방식으로 처리한다
locked_count = len(state["locked_users"])  # 잠긴 계정이 몇 개인지 센다
print("잠긴 계정", locked_count, "개:", state["locked_users"])  # 잠긴 계정 수와 이름을 출력한다
print("결과별 건수:", counts)  # 결과별 건수를 출력한다
print("티켓:", len(state["tickets"]), "건")  # 만든 티켓 수를 출력한다
print("건너뛴 액션과 이유:")  # 건너뛴 액션을 모아 보여 주는 제목 줄
for entry in action_log:  # 기록을 하나씩 꺼낸다
    result_text = entry["result"]  # 기록의 결과 문장
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 8. result_text 가 "건너뜀" 으로 시작하면 (if, startswith)
    # 9.   entry["incident"] · entry["action"] · "->" · result_text 를 출력한다 (print)
```

<h2>순서</h2>

1. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `bulk_incidents.json` · `safe_runner.py` · `exercise2-3_run.py` 세 파일을 하나씩 만들고(파일 이름 그대로), 코드를 붙여 넣어 저장합니다.
2. **[VS Code]** `safe_runner.py` 1 ~ 7번, `exercise2-3_run.py` 8 · 9번을 씁니다. 막히면 아래 「실습 2-3 정리」를 봅니다.
3. **[터미널]** 실행합니다(맥북은 `python3`).
   ```bash
   python exercise2-3_run.py
   ```
4. 출력은 네 단계와 건너뛴 이유입니다. 단계 1 은 2줄, 단계 2 는 1줄, 단계 3 은 14줄(「첫 번째 처리」 · 「두 번째 처리」 제목 2줄과 결과 10줄, 마지막의 잠긴 계정 · 티켓 2줄), 단계 4 는 알림 7건의 결과 7줄과 요약 3줄(잠긴 계정 · 결과별 건수 · 티켓)입니다. 마지막 `건너뛴 액션과 이유:` 아래는 건너뛴 액션만큼 줄이 나옵니다.
5. **[실습 결과 기록]** `report_u2.md` 의 `## 실습 2-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 단계 1 · 3 · 4 의 잠긴 계정과 티켓 수를 적어 주세요.
   - (나) [핵심 질문] 단계 1(Unit 1 방식)에서는 `dami` 가 두 번 잠기고 티켓이 2건 생성되었는데, 단계 3(안전한 방식)에서는 1건입니다. 단계 3 의 「두 번째 처리」 줄을 근거로 어떤 안전장치가 두 번째 실행을 차단했는지 적어 주세요.
   - (다) [핵심 질문] 단계 4 에서 잠긴 계정 3개 가운데 `users_info.json` 의 `employed` 값으로 볼 때 잘못 잠긴 계정이 있는지 적고, 한도가 없을 때와 비교해 잘못 잠긴 계정이 몇 개 감소했는지 적어 주세요. 한도로 방지하지 못하는 문제가 무엇인지도 적어 주세요. 마지막으로, 실습 2-1의 맥락(보강)과 실습 2-2의 경로 분기 중 무엇을 적용하면 잘못 잠긴 계정을 줄일 수 있는지 적어 주세요.

<!-- answer: 05|실습 2-3 정답 -->

## 실습 2-3 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 두 조건이 모두 참이면 | `if action == "계정 잠금" and entity in state["locked_users"]:` |
| 리스트의 개수 | `len(state["locked_users"])` |
| 이상이면 | `>=` |
| 같지 않으면 | `if skip_reason != "":` |
| 다른 함수의 결과를 그대로 리턴 | `return run_action(action, incident, state)` |
| 글자가 어떤 말로 시작하면 | `if result_text.startswith("건너뜀"):` |

---

## 문제 해결 기록 남기기

`report_u2.md`는 실행 결과와 질문에 대한 근거를 모은 **기술 기록**입니다. 여기에 적은 답을 그대로 옮기기보다, 자동 대응 앞에 맥락 보강과 경로 분기를 둔 이유, 실행 횟수 제한이 막아 준 문제와 막지 못한 문제를 동료가 따라갈 수 있게 기록합니다.

블로그와 GitHub Pages를 처음 설정한다면 [M3 Unit 1의 Jekyll 및 GitHub Pages 설정](__SITE__/exercises/module/3/unit/1/lesson/1/page/4)을 먼저 진행하세요. 이미 설정했다면 `network-study-notes` 저장소의 `_posts` 폴더에 `YYYY-MM-DD-m5-u2-context-safety.md` 형식의 글을 만듭니다.

기록에는 다음 내용을 담습니다.

- **관찰한 맥락:** 알림의 대상, 재직 여부, VIP 여부, 접속 IP, 신뢰 IP 여부가 어떻게 추가됐는지
- **경로 선택의 근거:** VIP 승인 경로와 신뢰 IP 오탐 종료 경로가 어떤 규칙 이름을 근거로 갈렸는지
- **안전장치의 범위:** 중복 처리와 계정 잠금 수 제한이 막은 피해, 한도 안에서도 남은 잘못된 조치
- **다음 확인:** 확인되지 않은 대상의 기본값과, 오탐 여부를 판단하려면 더 필요한 정보를 구분

관찰한 사실과 가능한 설명을 구분합니다. 알림의 맥락만으로 위험을 확정하지 말고, 어떤 추가 정보가 필요한지도 씁니다. 글을 저장하고 `network-study-notes` 저장소에 커밋한 뒤 `git push` 합니다. GitHub Pages에 게시된 글과 링크를 확인하세요.

Unit 3에서는 승인 대기된 인시던트를 담당자가 승인하거나 거절하는 흐름과 실패 기록을 구현합니다.

---

<!-- learn:answers -->
