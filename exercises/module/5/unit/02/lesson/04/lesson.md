---
id: m5-u02-l04
title: 제공 파일
render: markdown
---

# 제공 파일

## `ip_actions.py` 만들기

TODO(assemble): `ip_actions.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

```python
from containment_store import make_record             # 기록 한 건을 만드는 함수를 불러온다

DEFAULT_TTL = 120                                     # 차단을 유지하는 시간(분)


def count_users_on_ip(ip, ip_users):                  # IP 와 IP 별 사용 계정 딕셔너리를 받는 함수
    """그 IP 를 쓰는 계정이 몇 개인지 리턴한다. ip_users.json 에 없는 IP 는 0 을 리턴한다.
    차단하면 정상 사용자가 몇 명 영향을 받는지 확인할 때 쓴다.
    """
    return len(ip_users.get(ip, []))                  # 그 IP 를 쓰는 계정 수를 리턴한다 (목록에 없으면 0)


def block_ip(ip, state, incident_id, reason, ttl):    # IP · 상태 · 인시던트 번호 · 이유 · 유지 시간을 받는 함수
    """IP 를 차단하고 끝나는 시각을 적은 뒤, 실제로 차단됐는지 확인해 기록 한 건을 리턴한다.
    영구 차단 대신, 시간이 지나면 자동으로 풀리는 임시 차단을 만들 때 쓴다.
    """
    state["blocked_ips"].append(ip)                   # 차단한 IP 리스트에 추가한다
    state["block_expiry"][ip] = state["clock"] + ttl  # 차단이 끝나는 시각을 적는다
    after = "차단됨"                                  # 조치 뒤 상태 : 일단 차단됐다고 적고 — 미리 채운 줄
    if ip not in state["blocked_ips"]:                # 실제로 확인해 차단되지 않았으면 — 미리 채운 줄
        after = "차단되지 않음 (확인 실패)"           # 확인 실패라고 고쳐 적는다 — 미리 채운 줄
    return make_record("IP 차단", ip, incident_id, "차단되지 않음", after, reason + " (" + str(ttl) + "분 뒤 자동 해제)")  # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄
```

## `audit.py` 만들기

TODO(assemble): `audit.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

```python
def log_line(item, action, text):  # 인시던트 · 액션 · 결과 문장을 받는 함수
    """감사 기록(어떤 알림에 · 어떤 액션을 해서 · 결과가 무엇인지) 한 건을 딕셔너리로 만들어 리턴한다.
    모든 대응을 같은 모양으로 남겨 두면 나중에 한 목록으로 되짚을 수 있어서 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. 키 "incident"(item 의 "id"), "playbook"(item 의 "playbook"), "action"(action), "result"(text) 를 가진 딕셔너리를 entry 에 담는다
    return entry                   # 기록 한 건을 리턴한다
```

## `approvals.py` 만들기

TODO(assemble): `approvals.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

```python
from incident import change_status, run_action                                           # Unit 1 파일의 함수를 불러온다
from audit import log_line                                                               # 방금 만든 기록 함수를 불러온다

APPROVERS = ["kim.sec", "lee.soc"]                                                       # 승인할 권한이 있는 담당자 이름 리스트


def hold_for_approval(incident, playbook_id, actions, why, action_log):                  # 승인 대기로 멈출 인시던트와 정보를 받는 함수
    """알림의 상태를 분류됨으로 바꾸고 승인 대기 기록을 남긴 뒤, 담당자에게 보여 줄 대기 건 한 건으로 리턴한다.
    승인이 필요한 알림을 실행하지 않고 담당자에게 넘길 때 쓴다(도전 2-2 하루 흐름에서 호출한다).
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
