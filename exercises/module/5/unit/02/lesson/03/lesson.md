---
id: m5-u02-l03
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

**실습 2-1 을 마친 뒤, 실습 2-2 를 시작하기 전에** 이 레슨의 파일 세 개를 만듭니다. 오늘 핵심 실습에서는 이 파일을 부르지 않지만, 응용 2-2 와 Unit 3 이 불러 씁니다. 그래서 응용을 하지 않아도 오늘 만들어 두고 함께 깃허브에 올립니다.

1. 파일은 모두 작업 폴더 `network-study-notes/soar_response` 바로 아래에 만듭니다(VS Code 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File**).
2. 파일 이름을 그대로 적고, 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 만들 파일은 세 개입니다.

   | 파일 | 들어 있는 함수 | 불러 쓰는 파일 | 쓰는 곳 |
   |---|---|---|---|
   | `ip_actions.py` | 허용 목록 IP 와 공유 IP 를 가려 차단하고, 유효 기간(TTL)이 지나면 자동 해제 | 실습 2-1 `containment_store.py` | 응용 2-3, Unit 3 실습 3-1 |
   | `audit.py` | 감사 기록 한 건을 딕셔너리로 만드는 `log_line` | 없음 | `approvals.py`, 응용 2-2 `flow.py` |
   | `approvals.py` | 담당자의 승인 · 거절을 권한 확인 뒤 적용 | `audit.py`, Unit 1 실습 1-2 `incident.py` | 응용 2-2 |

4. 세 파일을 다 만들었으면 아래 명령으로 확인하고 실습 2-2 로 갑니다(맥북은 `python3`).
   ```bash
   python -c "from ip_actions import check_ip_policy; from approvals import is_authorized; from audit import log_line; print('제공 파일 정상', check_ip_policy('192.0.2.10', ['192.0.2.10'], {}), is_authorized('intern01'))"
   ```
   - `제공 파일 정상 허용 목록 IP 라서 차단하지 않음 False` 가 나오면 됩니다.
   - `ModuleNotFoundError: No module named 'containment_store'` 가 나오면 실습 2-1 의 `containment_store.py` 가 이 폴더에 없는 것입니다. 실습 2-1 을 먼저 합니다.

> 시간이 남아 응용 2-1 이나 응용 2-3 을 하면, `audit.py` · `approvals.py` 나 `ip_actions.py` 를 빈칸이 있는 골격으로 바꿔 직접 써 봅니다. 그때는 다 채울 때까지 그 파일을 부르는 프로그램이 동작하지 않으니, 다 쓴 뒤 그 응용의 실행 파일로 결과가 정답과 같은지 확인합니다.

**확인** — 4번 명령에서 `제공 파일 정상 허용 목록 IP 라서 차단하지 않음 False` 가 나오면 성공입니다. 안 나오면 오류에 나온 파일 이름의 페이지로 가서 코드 상자를 다시 복사해 붙여 넣습니다.

## `ip_actions.py` 만들기

`soar_response` 폴더에 **`ip_actions.py`** 를 만들고 아래 내용을 붙여 넣습니다. IP 를 차단하기 전에 정책을 검사하고, 차단에는 끝나는 시각을 적어 두었다가 시간이 지나면 풉니다.

| 함수 | 하는 일 | 리턴하는 것 |
|---|---|---|
| `check_ip_policy` | 허용 목록(`config/allowlist_ips.json`)에 있는 IP 인지, 쓰는 계정이 `SHARED_IP_LIMIT`(2) 개 이상인 공유 IP(`ip_users.json`)인지 본다 | 차단을 막는 이유 문장, 막을 이유가 없으면 빈 글자(`""`) |
| `block_ip` | 차단 리스트에 IP 를 넣고 끝나는 시각을 적은 뒤, 실제로 차단됐는지 확인한다 | 기록 한 건 |
| `expire_blocks` | 끝나는 시각이 지금 시각 이하인 차단을 모두 푼다(`unblock_ip`) | 해제 기록 리스트 |

끝나는 시각은 지금 시각(`clock`) + 유지 시간(`ttl`, 기본 `DEFAULT_TTL` 120분)입니다.

```python
from containment_store import make_record                                              # 기록 한 건을 만드는 함수를 불러온다

SHARED_IP_LIMIT = 2                                                                    # 한 IP 를 쓰는 계정이 이 수 이상이면 공유 IP 로 본다
DEFAULT_TTL = 120                                                                      # 차단을 유지하는 시간(분)


def is_in_allowlist(ip, allowlist_ips):                                                # IP 와 허용 목록을 받는 함수
    """IP 가 허용 목록에 있으면 True, 없으면 False 를 리턴한다.
    협력사 사무실처럼 차단하면 안 되는 IP 를 찾아낼 때 쓴다.
    """
    return ip in allowlist_ips                                                         # 허용 목록 안에 있는지 확인한 결과를 리턴한다


def count_users_on_ip(ip, ip_users):                                                   # IP 와 IP 별 사용 계정 딕셔너리를 받는 함수
    """그 IP 를 쓰는 계정이 몇 개인지 리턴한다. ip_users.json 에 없는 IP 는 0 을 리턴한다.
    차단하면 정상 사용자가 몇 명 영향을 받는지 확인할 때 쓴다.
    """
    return len(ip_users.get(ip, []))                                                   # 그 IP 를 쓰는 계정 수를 리턴한다 (목록에 없으면 0)


def check_ip_policy(ip, allowlist_ips, ip_users):                                      # IP · 허용 목록 · 사용 계정 딕셔너리를 받는 함수
    """자동으로 차단하면 안 되는 IP 이면 그 이유 문장을, 아니면 빈 글자("")를 리턴한다.
    허용 목록 IP 이거나 여러 계정이 함께 쓰는 IP 를 차단하기 전에 가려낼 때 쓴다.
    """
    if is_in_allowlist(ip, allowlist_ips):                                             # 허용 목록 IP 이면
        return "허용 목록 IP 라서 차단하지 않음"                                       # 이유를 리턴한다
    if count_users_on_ip(ip, ip_users) >= SHARED_IP_LIMIT:                             # 여러 계정이 함께 쓰는 IP 이면
        return "여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요"                        # 이유를 리턴한다
    return ""                                                                          # 막을 이유가 없으면 빈 글자를 리턴한다


def block_ip(ip, state, incident_id, reason, ttl):                                     # IP · 상태 · 인시던트 번호 · 이유 · 유지 시간을 받는 함수
    """IP 를 차단하고 끝나는 시각을 적은 뒤, 실제로 차단됐는지 확인해 기록 한 건을 리턴한다.
    영구 차단 대신, 시간이 지나면 자동으로 풀리는 임시 차단을 만들 때 쓴다.
    """
    state["blocked_ips"].append(ip)                                                    # 차단한 IP 리스트에 추가한다
    state["block_expiry"][ip] = state["clock"] + ttl                                   # 차단이 끝나는 시각을 적는다
    after = "차단됨"                                                                   # 조치 뒤 상태 : 일단 차단됐다고 적고
    if ip not in state["blocked_ips"]:                                                 # 실제로 확인해 차단되지 않았으면
        after = "차단되지 않음 (확인 실패)"                                            # 확인 실패라고 고쳐 적는다
    return make_record("IP 차단", ip, incident_id, "차단되지 않음", after, reason + " (" + str(ttl) + "분 뒤 자동 해제)")  # 조치 전 · 후 상태와 함께 기록한다


def unblock_ip(ip, state, incident_id, reason):                                        # IP · 상태 · 인시던트 번호 · 이유를 받는 함수
    """차단한 IP 를 풀고 끝나는 시각 기록도 지운 뒤 기록 한 건을 리턴한다.
    시간이 끝나서 풀거나 오탐으로 풀 때 쓴다.
    """
    state["blocked_ips"].remove(ip)                                                    # 차단 리스트에서 제거한다
    state["block_expiry"].pop(ip)                                                      # 끝나는 시각 기록도 지운다
    return make_record("IP 해제", ip, incident_id, "차단됨", "차단되지 않음", reason)  # 조치 전 · 후 상태와 함께 기록한다


def expire_blocks(state, incident_id):                                                 # 상태와 인시던트 번호를 받는 함수
    """끝나는 시각이 지난 차단을 모두 풀고 해제 기록 리스트를 리턴한다.
    임시 차단이 사람 손 없이 풀리게 할 때 쓴다.
    """
    records = []                                                                       # 해제 기록을 저장할 빈 리스트
    for ip in list(state["blocked_ips"]):                                              # 차단 리스트의 복사본에서 IP 를 하나씩 꺼낸다 (원본을 바꾸며 돌면 안 되기 때문이다)
        end_time = state["block_expiry"][ip]                                           # 그 IP 의 차단이 끝나는 시각
        if end_time <= state["clock"]:                                                 # 끝나는 시각이 지났으면
            records.append(unblock_ip(ip, state, incident_id, "차단 시간이 끝나 자동 해제"))  # 차단을 풀고 해제 기록을 모은다
    return records                                                                     # 해제 기록 리스트를 리턴한다
```

- 기록 한 건은 실습 2-1 의 `make_record` 가 만듭니다. 그래서 IP 조치도 계정 잠금과 같은 여섯 키(`action` · `target` · `incident` · `before` · `after` · `reason`)로 남습니다.

처음 보는 모양 세 가지입니다.

| 코드 | 뜻 |
|---|---|
| `str(ttl)` | 숫자를 글자로 바꾼다 |
| `state["block_expiry"].pop(ip)` | 딕셔너리에서 그 키와 값을 지운다 |
| `list(state["blocked_ips"])` | 리스트의 복사본을 만든다 |

숫자는 `+` 로 글자와 바로 이어 붙일 수 없어서 `str(ttl)` 로 바꿉니다.

- 허용 목록과 공유 IP 를 왜 먼저 거르는지, 끝나는 시각을 어떻게 비교하는지는 응용 2-3 레슨에서 자세히 다룹니다.

**확인** — `python -c "from ip_actions import check_ip_policy; print('ip_actions 정상')"` 를 쳐서 `ip_actions 정상` 이 나오면 성공입니다. `ModuleNotFoundError: No module named 'containment_store'` 가 나오면 실습 2-1 의 `containment_store.py` 를 먼저 만듭니다.

<!-- checklist -->
- [ ] `ip_actions.py` 를 만들어 코드 상자를 붙여 넣고 저장한 뒤, 확인 명령으로 `ip_actions 정상` 이 나왔다
<!-- /checklist -->

## `audit.py` 만들기

`soar_response` 폴더에 **`audit.py`** 를 만들고 아래 내용을 붙여 넣습니다. 알림 한 건에 어떤 액션을 해서 결과가 무엇이었는지를 딕셔너리 한 건(`incident` · `playbook` · `action` · `result`)으로 만듭니다.

```python
def log_line(item, action, text):  # 인시던트 · 액션 · 결과 문장을 받는 함수
    """감사 기록(어떤 알림에 · 어떤 액션을 해서 · 결과가 무엇인지) 한 건을 딕셔너리로 만들어 리턴한다.
    모든 대응을 같은 모양으로 남겨 두면 나중에 한 목록으로 되짚을 수 있어서 쓴다.
    """
    entry = {"incident": item["id"], "playbook": item["playbook"], "action": action, "result": text}  # 기록 한 건을 딕셔너리로 만든다
    return entry                   # 기록 한 건을 리턴한다
```

- 모든 대응을 같은 모양으로 남겨 두면 승인 · 거절 · 실패를 한 목록에서 다시 볼 수 있습니다. `approvals.py` 와 응용 2-2 의 `flow.py` 가 이 함수를 씁니다.

**확인** — `python -c "from audit import log_line; print(log_line({'id': 'INC-001', 'playbook': 'PB-001'}, '계정 잠금', '확인'))"` 를 쳐서 `{'incident': 'INC-001', 'playbook': 'PB-001', 'action': '계정 잠금', 'result': '확인'}` 이 나오면 성공입니다. 안 나오면 코드 상자를 다시 복사해 붙여 넣습니다.

<!-- checklist -->
- [ ] `audit.py` 를 만들어 코드 상자를 붙여 넣고 저장한 뒤, 확인 명령으로 기록 딕셔너리 한 건이 나왔다
<!-- /checklist -->

## `approvals.py` 만들기

`soar_response` 폴더에 **`approvals.py`** 를 만들고 아래 내용을 붙여 넣습니다. 승인이 필요한 알림을 멈춰 두고(`hold_for_approval`), 담당자의 결정이 오면 권한부터 확인한 뒤 적용합니다(`apply_decision`).

권한은 결정한 사람이 승인 권한이 있는 담당자 목록 `APPROVERS`(`kim.sec` · `lee.soc`)에 있는지로 봅니다.

| 권한 | 결정 | 처리 |
|---|---|---|
| 없음 | 승인 · 거절 모두 | 실행하지 않고 「권한 없음」 기록만 남긴다 |
| 있음 | 「승인」 | 멈춰 있던 액션을 실행하고 알림을 `조치됨` 으로 옮긴다 |
| 있음 | 「거절」 | 알림을 `종료` 로 옮기고 거절 사유를 기록한다 |

```python
from incident import change_status, run_action                                           # Unit 1 파일의 함수를 불러온다
from audit import log_line                                                               # audit.py 의 기록 함수를 불러온다

APPROVERS = ["kim.sec", "lee.soc"]                                                       # 승인할 권한이 있는 담당자 이름 리스트


def hold_for_approval(incident, playbook_id, actions, why, action_log):                  # 승인 대기로 멈출 인시던트와 정보를 받는 함수
    """알림의 상태를 분류됨으로 바꾸고 승인 대기 기록을 남긴 뒤, 담당자에게 보여 줄 대기 건 한 건으로 리턴한다.
    승인이 필요한 알림을 실행하지 않고 담당자에게 넘길 때 쓴다(응용 2-2 하루 흐름에서 호출한다).
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
    return approver in APPROVERS                                                         # 권한 목록 안에 있는지 확인한 결과를 리턴한다


def execute_actions(item, state, action_log, approver):                                  # 대기 건 · 연습용 시스템 · 기록 리스트 · 승인자를 받는 함수
    """대기 건에 적힌 액션을 하나씩 실행하고 누가 승인했는지 붙여 기록한 뒤, 알림을 조치됨으로 바꾸고 「실행 완료」를 리턴한다.
    담당자가 승인한 알림을 실제로 처리할 때 쓴다.
    """
    for action in item["actions"]:                                                       # 액션을 하나씩 꺼낸다
        result = run_action(action, item, state)                                         # 액션을 실행해 결과 문장을 받는다
        action_log.append(log_line(item, action, result + " (승인: " + approver + ")"))  # 승인자를 붙여 기록한다
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
    approver = decision["approver"]                                                      # 결정한 담당자 이름
    if not is_authorized(approver):                                                      # 승인 권한이 없으면
        return reject_unauthorized(item, approver, action_log)                           # 기록만 남기고 멈춘다
    return finish_decision(item, decision, state, action_log)                            # 권한이 있으면 결정을 적용한다


def finish_decision(item, decision, state, action_log):                                  # 대기 건 · 담당자 결정 · 연습용 시스템 · 기록 리스트를 받는 함수
    """권한 확인을 통과한 결정을 처리한다. 승인이면 액션을 실행하고, 거절이면 알림을 종료하고 거절 사유를 기록한다.
    권한이 확인된 뒤 결정 내용에 따라 나눠 처리할 때 쓴다.
    """
    approver = decision["approver"]                                                      # 결정한 담당자 이름
    if decision["result"] == "승인":                                                     # 결정이 승인이면
        return execute_actions(item, state, action_log, approver)                        # 액션을 실행하고 그 결과를 리턴한다
    change_status(item, "종료")                                                          # 승인이 아니면 거절로 보고 종료로 옮긴다
    action_log.append(log_line(item, "전체", "거절됨 (승인: " + approver + " — " + decision["comment"] + ")"))  # 거절 사유를 기록한다
    return "거절 처리"                                                                   # 거절 처리를 리턴한다
```

- 액션 실행은 Unit 1 실습 1-2 의 `incident.py` 에 있는 `run_action` 이 합니다.
- 권한 확인을 왜 가장 먼저 하는지는 응용 2-1 레슨에서 자세히 다룹니다.

**확인** — 세 파일을 다 만든 뒤 이 레슨 첫 페이지 4번의 명령을 쳐서 `제공 파일 정상 허용 목록 IP 라서 차단하지 않음 False` 가 나오면 성공입니다. `ModuleNotFoundError: No module named 'audit'` 가 나오면 `audit.py` 가 `soar_response` 폴더에 있는지 봅니다.

<!-- checklist -->
- [ ] `approvals.py` 를 만들어 코드 상자를 붙여 넣고 저장했다
- [ ] 첫 페이지 4번 명령을 쳐 `제공 파일 정상 허용 목록 IP 라서 차단하지 않음 False` 가 나왔다
<!-- /checklist -->

---
