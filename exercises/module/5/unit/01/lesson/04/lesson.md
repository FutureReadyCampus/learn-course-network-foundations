---
id: m5-u01-l04
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

**실습 1-3을 시작하기 전에** 이 레슨의 파일 두 개를 만듭니다. 두 파일은 응용 1-1 · 1-2에서 직접 쓰는 것인데, 다음 Unit의 응용에서도 불러 쓰므로 오늘은 완성본을 받아 둡니다.

1. 파일은 모두 `soar_response` 폴더 안에 만듭니다. 만드는 방법은 실습 1-2와 같습니다(VS Code 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File**, 파일 이름을 그대로 적기).
2. 아래 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 만들 파일은 두 개입니다.

   | 파일 | 들어 있는 것 | 하는 일 | 응용 |
   |---|---|---|---|
   | `routing.py` | `decide_route` | 맥락이 붙은 알림을 `승인 필요` · `오탐 종료` · `기본` 세 경로 가운데 하나로 나눈다 | 1-1 |
   | `routing.py` | `apply_route` | 정한 경로를 적용하고 기록한다 | 1-1 |
   | `safe_runner.py` | 안전한 실행기 | 이미 끝난 알림은 다시 처리하지 않고, 한 번 실행에서 잠그는 계정을 3개까지로 막는다 | 1-2 |

   - 맥락은 실습 1-3에서 알림에 붙이는 재직 · VIP · 접속 IP 정보입니다.
4. 두 파일 모두 실습 1-2의 `incident.py` 를 불러 씁니다. `incident.py` 가 같은 폴더에 있어야 합니다.
5. 다 만들었으면 터미널에서 두 파일을 불러와 봅니다. <mark>`ok` 가 나오면</mark> 됩니다(맥북은 `python3`).
   ```bash
   python -c "import routing, safe_runner; print('ok')"
   ```
   - 명령 풀이: 두 파일을 불러와(import) 문법 오류가 없는지 확인합니다. `ModuleNotFoundError: No module named 'incident'` 가 나오면 실습 1-2의 `incident.py` 를 먼저 만듭니다.

> 시간이 남아 응용 1-1이나 응용 1-2를 하면, 이 파일을 빈칸이 있는 골격으로 바꿔 직접 써 봅니다. 막히면 이 레슨의 완성본을 다시 붙여 넣으면 됩니다.

**확인** — `soar_response` 폴더에 `incident.py` 가 있으면 다음 쪽으로 넘어갑니다. 없으면 실습 1-2 에서 `incident.py` 를 먼저 만듭니다.

## `routing.py` 만들기

**[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 **`routing.py`** 를 만들고 아래 내용을 붙여 넣어 저장합니다. `decide_route` 는 위에서부터 차례로 확인해 정한 경로를 이유와 함께 두 값으로 리턴합니다.

| 알림이 이러면 | 경로 |
|---|---|
| VIP 계정이다 | `승인 필요` |
| 신뢰 IP 에서 왔고, 탐지 규칙이 모두 IP 관련이다 | `오탐 종료` |
| 둘 다 아니다 | `기본` |

```python
from incident import change_status                                          # 실습 1-2 의 incident.py 에서 상태 바꾸기 함수를 불러온다

IP_RELATED_RULES = ["평소와 다른 IP", "업무 시간 밖 로그인"]                             # 접속 IP 만 보고 낸 알림의 규칙 이름


def is_only_ip_related(incident):                                           # 인시던트 하나를 받는 함수
    """알림이 난 이유(규칙)가 모두 IP 와 관련된 것이면 True, 하나라도 다른 이유가 있으면 False 를 리턴한다.
    IP 때문에만 난 알림인지, 다른 증거도 있는 알림인지 구별할 때 쓴다.
    """
    for rule in incident["reasons"]:                                        # 탐지된 규칙을 하나씩 꺼낸다
        if rule not in IP_RELATED_RULES:                                    # IP 관련 규칙이 아닌 것이 있으면
            return False                                                    # 다른 증거가 있으니 False 를 리턴한다
    return True                                                             # 모두 IP 관련이면 True 를 리턴한다


def decide_route(incident):                                                 # 맥락이 붙은 인시던트를 받는 함수
    """붙어 있는 맥락을 보고 이 알림을 어느 경로(승인 필요 · 오탐 종료 · 기본)로 보낼지 정해, 이유 문장과 함께 리턴한다.
    같은 플레이북이어도 누구의 알림이냐에 따라 처리를 다르게 하고 싶을 때 쓴다.
    """
    context = incident["context"]                                           # 붙어 있는 맥락
    if context["vip"]:                                                      # VIP 계정이면
        return "승인 필요", "VIP 계정이라 담당자 승인이 필요함"                              # 경로와 이유를 함께 리턴한다
    if context["ip_trusted"] and is_only_ip_related(incident):              # 신뢰 IP 이고 규칙이 모두 IP 관련이면
        return "오탐 종료", "신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄"                  # 경로와 이유를 함께 리턴한다
    return "기본", "플레이북 기본 절차대로 처리함"                                         # 어느 경우도 아니면 기본 경로로 보낸다


def apply_route(incident, route, reason, incident_log):                     # 인시던트 · 경로 · 이유 · 기록 리스트를 받는 함수
    """정한 경로를 알림에 적용한다. 오탐 종료이면 상태를 분류됨을 거쳐 종료로 바꾸고, 경로와 이유를 기록에 남긴다.
    나중에 「왜 이 알림을 이렇게 처리했나」에 답할 수 있게 하려고 쓴다.
    """
    if route == "오탐 종료":                                                    # 오탐 종료이면
        change_status(incident, "분류됨")                                      # 먼저 분류됨으로 옮기고
        change_status(incident, "종료")                                       # 종료로 옮긴다
    entry = {"incident": incident["id"], "route": route, "reason": reason}  # 기록 한 건을 만든다
    incident_log.append(entry)                                              # 기록 리스트에 추가한다
```

**확인** — 터미널에서 `python -c "import routing; print('ok')"`(맥북은 `python3`)를 쳐서 `ok` 가 나오면 성공입니다. `SyntaxError` 나 `IndentationError` 가 나오면 복사가 덜 된 것이니 파일 내용을 모두 지우고 코드 상자를 다시 복사해 붙여 넣습니다.

<!-- checklist -->
- [ ] `routing.py` 를 `soar_response` 폴더에 만들고 코드 상자 내용을 붙여 넣어 저장했다
- [ ] `python -c "import routing; print('ok')"` 를 실행해 `ok` 가 나왔다
<!-- /checklist -->

## `safe_runner.py` 만들기

**[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 **`safe_runner.py`** 를 만들고 아래 내용을 붙여 넣어 저장합니다. `find_skip_reason` 이 「이미 잠긴 계정」과 「잠금 한도 3개」를 점검하고, `run_playbook_safe` 는 이미 끝난 알림을 건너뛰고 승인이 필요하면 멈춥니다.

```python
from incident import change_status, match_playbooks, run_action, make_log_entry                           # 실습 1-2 의 incident.py 에서 함수를 불러온다

DONE_STATUSES = ["조치됨", "보고됨", "종료"]                                                                      # 이미 대응이 끝난 상태들
MAX_LOCKS_PER_RUN = 3                                                                                     # 한 번 실행에서 잠글 수 있는 계정의 최대 수


def find_skip_reason(action, entity, state):                                                              # 액션 · 대상 · 연습용 시스템을 받는 함수
    """이 액션을 건너뛰어야 하면 그 이유 문장을, 건너뛸 필요가 없으면 빈 글자("")를 리턴한다.
    계정을 잠그기 전에 이미 잠긴 계정인지, 한 번에 잠글 수 있는 수를 넘었는지 확인할 때 쓴다.
    """
    if action == "계정 잠금" and entity in state["locked_users"]:                                             # 계정 잠금인데 이미 잠긴 계정이면
        return "건너뜀: 이미 잠겨 있음"                                                                            # 건너뛸 이유를 리턴한다
    if action == "계정 잠금" and len(state["locked_users"]) >= MAX_LOCKS_PER_RUN:                             # 잠근 계정이 한도 이상이면
        return "건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)"                                                   # 건너뛸 이유를 리턴한다
    return ""                                                                                             # 건너뛸 이유가 없으면 빈 글자를 리턴한다


def safe_run_action(action, incident, state):                                                             # 액션 · 인시던트 · 연습용 시스템을 받는 함수
    """액션을 실행하기 전에 건너뛸 이유가 있는지 먼저 확인한다. 이유가 있으면 실행하지 않고 그 이유를, 없으면 incident.py 의 run_action 으로 실행한 결과를 리턴한다.
    같은 일을 두 번 하거나 너무 많이 하는 것을 막고 싶을 때 쓴다.
    """
    entity = incident["entity"]                                                                           # 대응할 대상
    skip_reason = find_skip_reason(action, entity, state)                                                 # 건너뛸 이유를 구한다
    if skip_reason != "":                                                                                 # 건너뛸 이유가 있으면
        return skip_reason                                                                                # 실행하지 않고 이유를 리턴한다
    return run_action(action, incident, state)                                                            # 이유가 없으면 원래 run_action 으로 실행한 결과를 리턴한다


def run_playbook_safe(incident, playbook, state, action_log):                                             # 인시던트 · 플레이북 · 연습용 시스템 · 기록 리스트를 받는 함수
    """알림 한 건을 안전하게 처리한다. 이미 끝난 알림이면 건너뛰고, 승인이 필요하면 멈추고, 아니면 액션을 실행한다.
    처리 결과를 「실행 완료」 · 「승인 대기」 · 「이미 처리됨」 · 「일부 건너뜀」 중 하나로 리턴한다.
    """
    if incident["status"] in DONE_STATUSES:                                                               # 이미 대응이 끝난 인시던트이면
        entry = make_log_entry(incident, playbook, "전체", "이미 처리됨 — 건너뜀")                                  # 건너뛴 기록을 만들고
        action_log.append(entry)                                                                          # 기록 리스트에 추가한다
        return "이미 처리됨"                                                                                   # 이미 처리됨을 리턴한다
    change_status(incident, "분류됨")                                                                        # 대응을 시작하기 전에 분류됨 상태로 옮긴다
    if playbook["approval"] != "자동":                                                                      # 승인이 필요하면
        entry = make_log_entry(incident, playbook, "전체", "승인 대기")                                         # 승인 대기 기록을 만들고
        action_log.append(entry)                                                                          # 기록 리스트에 추가한다
        return "승인 대기"                                                                                    # 승인 대기를 리턴한다
    skipped = False                                                                                       # 건너뛴 액션이 있는지 : 처음에는 없다
    for action in playbook["actions"]:                                                                    # 액션을 하나씩 꺼낸다
        result = safe_run_action(action, incident, state)                                                 # 안전한 방식으로 실행한다
        if result.startswith("건너뜀"):                                                                      # 결과 문장이 「건너뜀」으로 시작하면
            skipped = True                                                                                # 건너뛴 액션이 있다고 적는다
        entry = make_log_entry(incident, playbook, action, result)                                        # 기록을 만들고
        action_log.append(entry)                                                                          # 기록 리스트에 추가한다
    if skipped:                                                                                           # 건너뛴 액션이 있으면
        return "일부 건너뜀"                                                                                   # 조치됨으로 옮기지 않고 일부 건너뜀을 리턴한다
    change_status(incident, "조치됨")                                                                        # 모두 실행했으니 조치됨으로 옮긴다
    return "실행 완료"                                                                                        # 실행 완료를 리턴한다


def process_safe(incidents, registry, state, action_log):                                                 # 인시던트 리스트 · 플레이북 리스트 · 연습용 시스템 · 기록 리스트를 받는 함수
    """알림을 하나씩 맞는 플레이북으로 안전하게 처리하고, 결과를 한 줄씩 출력한다.
    결과마다 몇 건인지 센 딕셔너리를 리턴한다.
    """
    counts = {}                                                                                           # 실행 결과마다 몇 건인지 셀 딕셔너리
    for incident in incidents:                                                                            # 인시던트를 하나씩 꺼낸다
        playbooks = match_playbooks(incident, registry)                                                   # 맞는 플레이북을 찾는다
        result_text = "맞는 플레이북 없음"                                                                        # 처음에는 없다고 적어 둔다
        for playbook in playbooks:                                                                        # 맞는 플레이북을 하나씩 꺼낸다
            result_text = run_playbook_safe(incident, playbook, state, action_log)                        # 안전하게 실행한다
        counts[result_text] = counts.get(result_text, 0) + 1                                              # 그 결과의 건수를 1 늘린다
        print(incident["id"], incident["entity"], "->", result_text, "(상태: " + incident["status"] + ")")  # 한 줄로 출력한다
    return counts                                                                                         # 결과별 건수를 리턴한다
```

**확인** — 터미널에서 첫 쪽 5번의 `python -c "import routing, safe_runner; print('ok')"` 를 쳐서 `ok` 가 나오면 성공입니다. 오류가 나면 오류에 적힌 파일 이름(`routing.py` 또는 `safe_runner.py`)의 내용을 모두 지우고 코드 상자를 다시 복사해 붙여 넣습니다.

<!-- checklist -->
- [ ] `safe_runner.py` 를 `soar_response` 폴더에 만들고 코드 상자 내용을 붙여 넣어 저장했다
- [ ] `python -c "import routing, safe_runner; print('ok')"` 를 실행해 `ok` 가 나왔다
<!-- /checklist -->
