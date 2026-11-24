---
id: m5-u04-l02
title: 실습 4-1 · 계정 잠금 실행과 감사 기록 남기기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/122_day03_am_containment.md
  mission_id: GichanSource.m5-1111-am-containment
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 4-1 · 계정 잠금 실행과 감사 기록 남기기

## 목표: 잠금 실행과 감사 기록

> **오늘 들어온 일**
>
> - **상황**: 오늘 계정 잠금 요청이 세 건 들어옵니다. **계정 잠금**(account lockout, 어카운트 락아웃)은 해당 계정의 로그인을 비활성화하는 조치입니다. `INC-001` 은 퇴사한 `dami`, `INC-003` 은 계정 관리자 `gaeun`, `INC-006` 은 이미 잠겨 있던 `junho` 입니다. Unit 1에서 만든 `run_action` 에 이 세 계정을 그대로 넘기면, 세 건 모두 계정 이름을 잠긴 계정 리스트에 추가하고 「잠금 완료」라는 결과만 기록합니다.
> - **문제**:
> - 사후 검증(post-action verification: 조치 후 실제 상태를 다시 확인하는 일, 1.1 에서 설명)이 없습니다. 잠금이 실제로 적용됐는지 확인하지 않으므로 실제 서버에서 잠금 명령이 실패해도 「잠금 완료」로 기록됩니다.
> - 조치 전 상태(before)를 기록하지 않습니다. `junho` 는 원래 잠겨 있었습니다. 나중에 알림이 오탐(false positive, 폴스 포지티브: 정상 활동을 공격으로 잘못 판정한 것)으로 판명되어 자동 대응이 잠근 계정을 한꺼번에 해제(롤백, rollback: 조치 이전 상태로 되돌리는 일)한다고 해 봅시다. 조치 전 상태가 기록에 없으므로 원래 잠겨 있던 `junho` 까지 해제됩니다.
> - Unit 2에서는 계정 관리자 알림을 승인 경로로 분기했습니다. 그러나 이 경로를 거치지 않고 잠금 함수를 직접 호출하면 `gaeun` 계정도 잠겨, 직원들의 계정 관리 업무가 중단됩니다.
> - **부탁**: 계정을 잠근 후 실제로 잠겼는지 사후 검증하고, 조치 전 · 후 상태를 감사 기록으로 남겨 주세요. 계정 관리자(VIP) 계정은 이 함수에서도 잠그지 않아야 하며, 오탐으로 판명되면 해제할 수 있어야 합니다.
> - **바뀌는 점**: 사후 검증으로 확인된 상태만 「잠김」으로 기록되고, 원래 잠겨 있던 계정(`junho`)과 이번에 잠근 계정(`dami`)이 조치 전 상태(before)로 구분됩니다. 오늘 샘플에서는 세 건 중 `dami` 한 건만 새로 잠기고 `gaeun` 은 잠기지 않습니다. 상황과 이름은 설명을 위한 예시입니다.

## 1.1 대응 조치는 「실행 · 사후 검증 · 감사 기록」 세 단계를 모두 마쳐야 완료된다

계정 잠금 같은 **대응 조치**는 ① 실행(execution), ② 사후 검증, ③ 감사 기록의 세 단계를 모두 마쳐야 완료된 것으로 봅니다. ②의 **사후 검증**(post-action verification, 포스트 액션 베리피케이션: 조치 후 시스템의 실제 상태가 의도한 대로 바뀌었는지 다시 확인하는 일)은 이후 문서에서 「조치 후 확인」이라고도 부릅니다. 사후 검증은 명령이 오류 없이 종료됐지만 실제로는 적용되지 않은 경우를 탐지합니다. 예를 들어 `dami` 를 잠근 후 잠긴 계정 리스트에 `dami` 가 실제로 있는지 다시 조회합니다. ③의 **감사 기록**(audit log, 오딧 로그: 어떤 조치를 어떤 대상에 했는지 순서대로 남긴 기록) 한 건에는 다음 여섯 가지를 남깁니다.

| 키 | 뜻 | 예 |
|---|---|---|
| `action` | 수행한 조치의 종류 | `"계정 잠금"` |
| `target` | 조치 대상(계정 이름 또는 IP) | `"dami"` |
| `incident` | 인시던트(incident: 처리해야 하는 보안 사건 한 건) 번호 | `"INC-001"` |
| `before` | 조치 전 상태 | `"잠기지 않음"` |
| `after` | 사후 검증으로 **확인한** 조치 후 상태 | `"잠김"` |
| `reason` | 조치 사유 | `"퇴사한 계정의 서버 요청"` |

- `before` 는 롤백할 때 복원할 원래 상태를 알려 주므로 남깁니다.
- 조치 전에 이미 잠겨 있던 계정은 `잠김 → 잠김`(상태 변경 없음)으로 기록합니다. 그래야 나중에 오탐으로 판명되어 롤백할 때 `junho` 처럼 원래 잠겨 있던 계정을 해제 대상에서 뺄 수 있습니다.
- 이미 잠긴 계정에 잠금을 다시 요청해도 시스템 상태가 바뀌지 않는 성질을 멱등성(idempotency, 아이뎀포턴시: 같은 조치를 여러 번 실행해도 결과가 한 번 실행한 것과 같은 성질)이라고 합니다.
- 연습용 시스템의 상태 `state` 는 잠긴 계정(`locked_users`) · 차단한 IP · 열린 세션을 저장하는 딕셔너리입니다. 이 상태는 실행할 때마다 초기값에서 다시 시작하므로 결과를 똑같이 다시 만들 수 있습니다.
- 조치 기록은 파일에 추가한 순서대로 남습니다. 그래서 이 기록은 감사 추적(audit trail, 오딧 트레일: 어떤 일이 어떤 순서로 있었는지 다시 짚어 볼 수 있게 남긴 시간순 기록)으로 쓸 수 있습니다.

**문법 상자 — `리스트.remove(값)` 은 리스트에서 그 값을 제거한다**

```python
locked = ["junho", "dami"]
locked.remove("dami")
print(locked)
```
| 코드 | 뜻 |
|---|---|
| `locked.remove("dami")` | 리스트에서 `dami` 를 제거한다. 리스트에 없으면 `ValueError`(밸류 에러: 값이 맞지 않아 나는 오류)가 난다 |
| 위 코드의 출력 | `['junho']` |

함수는 두 파일에 나뉘어 있고 실행 파일이 하나 더 있습니다. 직접 쓰는 곳은 **아홉 군데**입니다.

```
containment_store.py  make_record       : 위 표의 여섯 키를 가진 조치 기록 한 건을 만든다 (1번)
                      append_log        : 기록을 기록 파일에 한 건 더한다 (2번)
account_actions.py    check_policy      : VIP 계정이면 자동 조치를 막는 이유를 리턴한다 (3 · 4번)
                      verify_locked     : 실제로 잠긴 계정 리스트에 있는지 확인한다 (5번)
                      lock_account      : 잠그고, 확인하고, 기록을 만든다 (6번이 잠그는 줄)
                      unlock_account    : 해제하고, 확인하고, 기록을 만든다 (7번이 해제하는 줄)
실행 파일             exercise4-1_run.py  : 잠금 요청마다 잠그고 (8번) 기록을 남긴다 (9번)
```

## 실습 4-1 · 계정 잠금 실행과 감사 기록 남기기

**이런 상황이 있습니다**

- **지금은**: <mark>잠금 호출만 있고 사후 검증도 조치 전 상태 기록도 없어서, 「잠갔다」는 기록이 실제 상태를 입증하지 못합니다</mark>.
- **만드는 것**: 조치 기록 생성과 기록 파일 추가(`containment_store.py`), VIP 정책 검사 · 잠금 사후 검증 · 잠금 · 해제(`account_actions.py`), 잠금 요청 처리(`exercise4-1_run.py`).
- **실행하면**: <mark>단계 1: 조치 전 잠긴 계정, 단계 2: 잠금 요청 3건의 조치 전 → 후, 단계 3: 해제, 단계 4: 파일에 저장해 둔 잠긴 계정과 조치 기록 수를 다시 읽은 결과가 나옵니다.</mark>

**할 일**: 파일 세 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 ~ 4 를 읽습니다.

**`containment_store.py`** — 연습용 시스템의 상태와 조치 기록 파일을 관리합니다. 실습 4-2 · 실습 4-3에서도 이 파일의 함수를 불러와 사용합니다. 직접 쓰는 곳은 1 · 2번입니다. `INITIAL_STATE` 의 `junho` 는 수업 전부터 잠겨 있는 계정입니다.

```python
import copy  # 처음 상태를 복사해 쓰기 위해 copy 를 불러온다
from incident import load_json, save_json  # Unit 1 파일의 파일 읽기 · 쓰기 함수를 불러온다

STATE_PATH = "containment_state.json"  # 연습용 시스템 상태를 저장할 파일 이름
LOG_PATH = "containment_log.json"  # 조치 기록을 저장할 파일 이름
INITIAL_STATE = {  # 수업을 시작할 때의 연습용 시스템 상태
    "locked_users": ["junho"],  # 이미 잠겨 있는 계정 : junho 는 수업 전부터 잠겨 있다
    "blocked_ips": [],  # 차단한 IP 리스트 : 처음에는 비어 있다
    "block_expiry": {},  # IP 별 차단이 끝나는 시각(분) : 처음에는 비어 있다
    "clock": 0,  # 연습용 시스템의 시계(분) : 0 에서 시작한다
    "sessions": {
        "dami": ["S-101", "S-102"],
        "seoyeon": ["S-201"],
        "gaeun": ["S-301"],
        "jiwoo": ["S-401"],
        "junho": ["S-501"],
        "hana": ["S-601"],
    },  # 계정별로 열려 있는 로그인 세션
}


def new_state():  # 인자가 없는 함수
    """처음 상태를 복사해 새 연습용 시스템 상태를 리턴한다.
    실행할 때마다 같은 상태에서 시작해 결과를 비교할 때 쓴다.
    """
    return copy.deepcopy(INITIAL_STATE)  # 처음 상태의 복사본을 리턴한다


def save_state(state):  # 연습용 시스템 상태를 받는 함수
    """상태를 파일에 저장한다.
    다음 프로그램이 이어서 읽을 수 있게 할 때 쓴다.
    """
    save_json(state, STATE_PATH)  # 상태를 JSON 파일로 저장한다


def load_state():  # 인자가 없는 함수
    """저장해 둔 상태 파일을 읽어 리턴한다.
    저장이 제대로 됐는지 확인하거나 이어서 일할 때 쓴다.
    """
    return load_json(STATE_PATH)  # 상태 파일을 읽어 리턴한다


def reset_log():  # 인자가 없는 함수
    """조치 기록 파일을 빈 리스트로 비운다.
    실행할 때마다 기록을 처음부터 추가할 때 쓴다.
    """
    save_json([], LOG_PATH)  # 빈 리스트를 기록 파일로 저장한다


def make_record(action, target, incident_id, before, after, reason):  # 조치 이름 · 대상 · 인시던트 번호 · 조치 전 · 조치 후 · 이유를 받는 함수
    """조치 한 건(무엇을 · 누구에게 · 조치 전 · 조치 후 · 이유)의 기록을 딕셔너리로 만들어 리턴한다.
    조치 전과 후 상태를 함께 남겨 두고 싶을 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. 키 "action"(action), "target"(target), "incident"(incident_id), "before"(before), "after"(after), "reason"(reason) 를 가진 딕셔너리를 record 에 저장한다
    return record  # 기록 한 건을 리턴한다


def append_log(record):  # 기록 한 건을 받는 함수
    """기록 파일을 읽어 기록 한 건을 더하고 다시 저장한다. 파일이 아직 없으면 빈 리스트로 시작한다.
    조치할 때마다 기록을 한 건씩 추가해 둘 때 쓴다.
    """
    try:  # 파일 읽기를 시도한다 — 미리 채운 줄
        log = load_json(LOG_PATH)  # 기록 파일을 읽는다 — 미리 채운 줄
    except FileNotFoundError:  # 파일이 없으면 — 미리 채운 줄
        log = []  # 빈 리스트로 시작한다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. log 에 record 를 추가한다 (append)
    save_json(log, LOG_PATH)  # 기록 파일로 다시 저장한다
```
**`account_actions.py`** — 계정 잠금과 해제를 구현합니다. 실습 4-3에서도 이 파일의 함수를 불러와 사용합니다. 직접 쓰는 곳은 3 ~ 7번입니다.

```python
from containment_store import make_record  # 기록 한 건을 만드는 함수를 불러온다


def check_policy(user, vip_accounts):  # 계정 이름과 VIP 계정 리스트를 받는 함수
    """자동으로 조치하면 안 되는 계정(VIP)이면 그 이유 문장을, 아니면 빈 글자("")를 리턴한다.
    경로에서 이미 `승인 필요` 로 보냈어도 조치 함수가 마지막으로 한 번 더 막고 싶을 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 3. user 가 vip_accounts 안에 있으면 (if, in)
    # 4.   "VIP 계정이라 자동 조치 대상이 아님" 을 리턴한다
    return ""  # 막을 이유가 없으면 빈 글자를 리턴한다 — 미리 채운 줄


def verify_locked(user, state):  # 계정 이름과 연습용 시스템 상태를 받는 함수
    """계정이 잠긴 계정 리스트에 들어 있으면 True, 없으면 False 를 리턴한다.
    잠그라고 호출한 것과 실제로 잠긴 것이 같은지 조치 뒤에 확인할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. user 가 state["locked_users"] 안에 있는지(in)의 결과를 리턴한다


def lock_account(user, state, vip_accounts, incident_id, reason):  # 계정 · 상태 · VIP 리스트 · 인시던트 번호 · 이유를 받는 함수
    """VIP 인지 먼저 확인하고 계정을 잠근 뒤, 실제로 잠겼는지 다시 확인해 조치 기록 한 건을 리턴한다.
    VIP 이거나 이미 잠겨 있으면 잠그지 않고 그 이유를 기록에 남긴다.
    """
    blocked = check_policy(user, vip_accounts)  # 자동 조치를 막을 이유를 구한다 — 미리 채운 줄
    if blocked != "":  # 막을 이유가 있으면 — 미리 채운 줄
        return make_record("계정 잠금", user, incident_id, "변경 없음", "변경 없음", blocked)  # 바꾸지 않고 이유를 기록한다 — 미리 채운 줄
    if user in state["locked_users"]:  # 이미 잠겨 있으면 — 미리 채운 줄
        return make_record("계정 잠금", user, incident_id, "잠김", "잠김", "이미 잠겨 있어 변경 없음")  # 바꾸지 않고 기록한다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 6. state["locked_users"] 에 user 를 추가한다 (append)
    after = "잠김"  # 조치 뒤 상태 : 일단 잠겼다고 적고 — 미리 채운 줄
    if not verify_locked(user, state):  # 실제로 확인해 잠기지 않았으면 — 미리 채운 줄
        after = "잠기지 않음 (확인 실패)"  # 확인 실패라고 고쳐 적는다 — 미리 채운 줄
    return make_record("계정 잠금", user, incident_id, "잠기지 않음", after, reason)  # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄


def unlock_account(user, state, incident_id, reason):  # 계정 · 상태 · 인시던트 번호 · 이유를 받는 함수
    """잠긴 계정을 해제하고 실제로 해제됐는지 확인해 조치 기록 한 건을 리턴한다.
    오탐으로 확인된 계정을 되돌릴 때 쓴다.
    """
    if user not in state["locked_users"]:  # 잠겨 있지 않으면 — 미리 채운 줄
        return make_record("계정 해제", user, incident_id, "잠기지 않음", "잠기지 않음", "잠겨 있지 않아 변경 없음")  # 바꾸지 않고 기록한다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. state["locked_users"] 에서 user 를 제거한다 (remove)
    after = "잠기지 않음"  # 조치 뒤 상태 : 일단 해제됐다고 적고 — 미리 채운 줄
    if verify_locked(user, state):  # 실제로 확인해 아직 잠겨 있으면 — 미리 채운 줄
        after = "잠김 (확인 실패)"  # 확인 실패라고 고쳐 적는다 — 미리 채운 줄
    return make_record("계정 해제", user, incident_id, "잠김", after, reason)  # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄
```
**`exercise4-1_run.py`** — 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다.

```python
from incident import load_json  # Unit 1 파일의 함수를 불러온다
from containment_store import new_state, save_state, load_state, reset_log, append_log  # 방금 만든 상태 · 기록 함수를 불러온다
from account_actions import lock_account, unlock_account  # 방금 만든 계정 조치 함수를 불러온다

vip_accounts = load_json("config/vip_accounts.json")  # VIP 계정 리스트를 읽는다
requests = [
    ("INC-001", "dami", "퇴사한 계정의 서버 요청"),
    ("INC-003", "gaeun", "여러 로그 연결"),
    ("INC-006", "junho", "퇴사 처리 확인"),
]  # 잠금 요청 3건 : (인시던트 번호, 계정, 이유)
state = new_state()  # 처음 상태에서 시작한다
reset_log()  # 기록 파일을 비운다

print("--- 단계 1: 조치 전에 잠겨 있는 계정")  # 단계 1 시작을 알리는 줄
print(state["locked_users"])  # 잠긴 계정을 출력한다

print("--- 단계 2: 잠금 요청 3건")  # 단계 2 시작을 알리는 줄
for incident_id, user, reason in requests:  # 요청을 하나씩 꺼낸다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 8. lock_account(user, state, vip_accounts, incident_id, reason) 의 결과를 record 에 저장한다
    # 9. append_log(record) 를 호출한다 (조치 기록을 파일에 남긴다)
    print(record["incident"], record["target"], "·", record["before"], "→", record["after"], "·", record["reason"])  # 기록 한 건을 출력한다

print("--- 단계 3: 오탐으로 확인되어 dami 해제")  # 단계 3 시작을 알리는 줄
record = unlock_account("dami", state, "INC-001", "오탐으로 확인되어 해제")  # 해제한다
append_log(record)  # 해제 기록도 남긴다
print(record["incident"], record["target"], "·", record["before"], "→", record["after"], "·", record["reason"])  # 기록 한 건을 출력한다

save_state(state)  # 상태를 파일에 저장한다
print("--- 단계 4: 파일에 저장된 값 다시 읽기")  # 단계 4 시작을 알리는 줄
saved_state = load_state()  # 저장한 상태 파일을 읽는다
saved_log = load_json("containment_log.json")  # 저장한 기록 파일을 읽는다
print("잠긴 계정:", saved_state["locked_users"])  # 파일에 저장된 잠긴 계정을 출력한다
print("조치 기록:", len(saved_log), "건")  # 파일에 저장된 기록 수를 출력한다
```
**순서**

1. **[VS Code]** 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 파일 이름 `containment_store.py` · `account_actions.py` · `exercise4-1_run.py` 을(를) 하나씩 그대로 적어 세 개의 파일을 만듭니다. 각 파일에 이 페이지의 코드 상자를 복사해 붙여 넣고 저장합니다(`Ctrl + S`, 맥북은 `Cmd + S`).
2. **[VS Code]** `containment_store.py` 1 · 2번, `account_actions.py` 3 ~ 7번, `exercise4-1_run.py` 8 · 9번을 씁니다. 막히면 아래 「실습 4-1 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise4-1_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 1줄, 단계 2 는 3줄, 단계 3 은 1줄, 단계 4 는 2줄입니다. 실행하면 `containment_state.json` 과 `containment_log.json` 이 생깁니다.
5. **[실습 결과 기록]** `report_u4.md` 의 `## 실습 4-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 단계 4 의 잠긴 계정과 조치 기록 수를 적어 주세요.
   - (나) [핵심 질문] INC-003 의 `gaeun` 은 잠기지 않았습니다. 단계 2 의 줄을 근거로 이유를 적어 주세요. 그리고 Unit 2의 실습 2-2의 경로가 VIP 계정을 이미 `승인 필요` 경로로 분기했는데도 조치 함수가 정책을 한 번 더 검사하는 이유도 적어 주세요.
   - (다) [핵심 질문] INC-006 의 `junho` 는 `잠김 → 잠김` 으로 기록됐고, 단계 3 에서 해제한 `dami` 는 `잠김 → 잠기지 않음` 입니다. `before` 를 남기면 롤백할 때 어떤 판단이 가능해지는지 적어 주세요. 그리고 잠금 뒤 사후 검증(`verify_locked`)이 없으면 어떤 문제가 생기는지도 적어 주세요.

## 실습 4-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 딕셔너리를 만들어 변수에 저장하기 | `record = {"action": action, ..., "reason": reason}` |
| 리스트에 추가 | `log.append(record)` |
| 리스트 안에 있으면 | `if user in vip_accounts:` |
| 리스트 안에 있는지 확인한 결과 리턴 | `return user in state["locked_users"]` |
| 리스트에서 제거 | `state["locked_users"].remove(user)` |
| 함수 결과를 변수에 저장하기 | `record = lock_account(user, state, vip_accounts, incident_id, reason)` |

<!-- answer: 05|실습 4-1 정답 -->

---
