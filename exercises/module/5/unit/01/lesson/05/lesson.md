---
id: m5-u01-l05
title: 제공 파일
render: markdown
---

# 제공 파일

## `routing.py` 만들기

TODO(assemble): `routing.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

```python
from incident import change_status                                          # Unit 1 파일의 상태 바꾸기 함수를 불러온다

IP_RELATED_RULES = ["평소와 다른 IP", "업무 시간 밖 로그인"]                # 접속 IP 만 보고 낸 알림의 규칙 이름


def is_only_ip_related(incident):                                           # 인시던트 하나를 받는 함수
    """알림이 난 이유(규칙)가 모두 IP 와 관련된 것이면 True, 하나라도 다른 이유가 있으면 False 를 리턴한다.
    IP 때문에만 난 알림인지, 다른 증거도 있는 알림인지 구별할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. incident["reasons"] 의 규칙을 하나씩 꺼낸다 (for, rule)
    # 2.   rule 이 IP_RELATED_RULES 안에 없으면 (if, not in)
    # 3.     False 를 리턴한다 (IP 와 관계없는 다른 증거가 있다)
    return True                                                             # 모두 IP 관련이면 True 를 리턴한다 — 미리 채운 줄


def decide_route(incident):                                                 # 맥락이 붙은 인시던트를 받는 함수
    """붙어 있는 맥락을 보고 이 알림을 어느 경로(승인 필요 · 오탐 종료 · 기본)로 보낼지 정해, 이유 문장과 함께 리턴한다.
    같은 플레이북이어도 누구의 알림이냐에 따라 처리를 다르게 하고 싶을 때 쓴다.
    """
    context = incident["context"]                                           # 붙어 있는 맥락
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. context 의 "vip" 가 참이면 (if)
    # 5.   "승인 필요" 와 "VIP 계정이라 담당자 승인이 필요함" 을 쉼표로 이어 함께 리턴한다
    # 6. context 의 "ip_trusted" 가 참이고(and) is_only_ip_related(incident) 가 참이면 (if)
    # 7.   "오탐 종료" 와 "신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄" 을 쉼표로 이어 함께 리턴한다
    return "기본", "플레이북 기본 절차대로 처리함"                          # 어느 경우도 아니면 기본 경로로 보낸다


def apply_route(incident, route, reason, incident_log):                     # 인시던트 · 경로 · 이유 · 기록 리스트를 받는 함수
    """정한 경로를 알림에 적용한다. 오탐 종료이면 상태를 분류됨을 거쳐 종료로 바꾸고, 경로와 이유를 기록에 남긴다.
    나중에 「왜 이 알림을 이렇게 처리했나」에 답할 수 있게 하려고 쓴다.
    """
    if route == "오탐 종료":                                                # 오탐 종료이면
        change_status(incident, "분류됨")                                   # 먼저 분류됨으로 옮기고
        change_status(incident, "종료")                                     # 종료로 옮긴다
    entry = {"incident": incident["id"], "route": route, "reason": reason}  # 기록 한 건을 만든다
    incident_log.append(entry)                                              # 기록 리스트에 추가한다
```

## `safe_runner.py` 만들기

TODO(assemble): `safe_runner.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

```python
from incident import change_status, match_playbooks, run_action, make_log_entry     # Unit 1 파일의 함수를 불러온다

DONE_STATUSES = ["조치됨", "보고됨", "종료"]                                        # 이미 대응이 끝난 상태들
MAX_LOCKS_PER_RUN = 3                                                               # 한 번 실행에서 잠글 수 있는 계정의 최대 수


def find_skip_reason(action, entity, state):                                        # 액션 · 대상 · 연습용 시스템을 받는 함수
    """이 액션을 건너뛰어야 하면 그 이유 문장을, 건너뛸 필요가 없으면 빈 글자("")를 리턴한다.
    계정을 잠그기 전에 이미 잠긴 계정인지, 한 번에 잠글 수 있는 수를 넘었는지 확인할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. action 이 "계정 잠금" 이고(and) entity 가 state["locked_users"] 안에 있으면 (if, in)
    # 2.   "건너뜀: 이미 잠겨 있음" 을 리턴한다
    # 3. action 이 "계정 잠금" 이고(and) state["locked_users"] 의 개수(len)가 MAX_LOCKS_PER_RUN 이상이면 (if, >=)
    # 4.   "건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)" 를 리턴한다
    return ""                                                                       # 건너뛸 이유가 없으면 빈 글자를 리턴한다 — 미리 채운 줄


def safe_run_action(action, incident, state):                                       # 액션 · 인시던트 · 연습용 시스템을 받는 함수
    """액션을 실행하기 전에 건너뛸 이유가 있는지 먼저 확인한다. 이유가 있으면 실행하지 않고 그 이유를, 없으면 Unit 1의 run_action 으로 실행한 결과를 리턴한다.
    같은 일을 두 번 하거나 너무 많이 하는 것을 막고 싶을 때 쓴다.
    """
    entity = incident["entity"]                                                     # 대응할 대상
    skip_reason = find_skip_reason(action, entity, state)                           # 건너뛸 이유를 구한다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. skip_reason 이 빈 글자("")가 아니면 (if, !=)
    # 6.   skip_reason 을 리턴한다
    # 7. run_action(action, incident, state) 의 결과를 리턴한다 (건너뛸 이유가 없으면 원래대로 실행한다)


def run_playbook_safe(incident, playbook, state, action_log):                       # 인시던트 · 플레이북 · 연습용 시스템 · 기록 리스트를 받는 함수
    """알림 한 건을 안전하게 처리한다. 이미 끝난 알림이면 건너뛰고, 승인이 필요하면 멈추고, 아니면 액션을 실행한다.
    처리 결과를 「실행 완료」 · 「승인 대기」 · 「이미 처리됨」 · 「일부 건너뜀」 중 하나로 리턴한다.
    """
    if incident["status"] in DONE_STATUSES:                                         # 이미 대응이 끝난 인시던트이면
        entry = make_log_entry(incident, playbook, "전체", "이미 처리됨 — 건너뜀")  # 건너뛴 기록을 만들고
        action_log.append(entry)                                                    # 기록 리스트에 추가한다
        return "이미 처리됨"                                                        # 이미 처리됨을 리턴한다
    change_status(incident, "분류됨")                                               # 대응을 시작하기 전에 분류됨 상태로 옮긴다
    if playbook["approval"] != "자동":                                              # 승인이 필요하면
        entry = make_log_entry(incident, playbook, "전체", "승인 대기")             # 승인 대기 기록을 만들고
        action_log.append(entry)                                                    # 기록 리스트에 추가한다
        return "승인 대기"                                                          # 승인 대기를 리턴한다
    skipped = False                                                                 # 건너뛴 액션이 있는지 : 처음에는 없다
    for action in playbook["actions"]:                                              # 액션을 하나씩 꺼낸다
        result = safe_run_action(action, incident, state)                           # 안전한 방식으로 실행한다
        if result.startswith("건너뜀"):                                             # 결과 문장이 「건너뜀」으로 시작하면
            skipped = True                                                          # 건너뛴 액션이 있다고 적는다
        entry = make_log_entry(incident, playbook, action, result)                  # 기록을 만들고
        action_log.append(entry)                                                    # 기록 리스트에 추가한다
    if skipped:                                                                     # 건너뛴 액션이 있으면
        return "일부 건너뜀"                                                        # 조치됨으로 옮기지 않고 일부 건너뜀을 리턴한다
    change_status(incident, "조치됨")                                               # 모두 실행했으니 조치됨으로 옮긴다
    return "실행 완료"                                                              # 실행 완료를 리턴한다


def process_safe(incidents, registry, state, action_log):                           # 인시던트 리스트 · 플레이북 리스트 · 연습용 시스템 · 기록 리스트를 받는 함수
    """알림을 하나씩 맞는 플레이북으로 안전하게 처리하고, 결과를 한 줄씩 출력한다.
    결과마다 몇 건인지 센 딕셔너리를 리턴한다.
    """
    counts = {}                                                                     # 실행 결과마다 몇 건인지 셀 딕셔너리
    for incident in incidents:                                                      # 인시던트를 하나씩 꺼낸다
        playbooks = match_playbooks(incident, registry)                             # 맞는 플레이북을 찾는다
        result_text = "맞는 플레이북 없음"                                          # 처음에는 없다고 적어 둔다
        for playbook in playbooks:                                                  # 맞는 플레이북을 하나씩 꺼낸다
            result_text = run_playbook_safe(incident, playbook, state, action_log)  # 안전하게 실행한다
        counts[result_text] = counts.get(result_text, 0) + 1                        # 그 결과의 건수를 1 늘린다
        print(incident["id"], incident["entity"], "->", result_text, "(상태: " + incident["status"] + ")")  # 한 줄로 출력한다
    return counts                                                                   # 결과별 건수를 리턴한다
```
