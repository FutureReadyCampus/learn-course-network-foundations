---
id: m5-u04-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표와 오늘의 계획

지난 Unit 들에서 계정 잠금 · IP 차단 같은 자동 조치를 실행하고, 잘못된 조치를 되돌리고, 사건마다 티켓을 남겼습니다. 오늘은 자동 조치가 **실행되기 직전**과 **실행된 뒤**를 다룹니다. 실행 직전에는 사람의 승인이 필요한 조치를 가려내고(승인 게이트), 실행된 뒤에 오탐으로 밝혀지면 원래 상태로 되돌립니다.

**오늘의 계획 (약 2시간 40분)**

| 순서 | 시간 | 하는 일 |
|---|---|---|
| 1. 시작하기 | 15분 | 이 레슨을 읽고 `soar_response` 폴더의 이전 파일을 확인합니다 |
| 2. 핵심 실습 | 약 110분 | 실습 4-1 · 4-2 를 차례로 합니다. 보고서의 꼭 채울 칸도 이때 씁니다 |
| 3. 글쓰기 | 20분 | 「오늘의 글 쓰기」 레슨에서 세 문장 글 한 편을 씁니다 |
| 4. 마무리 | 15분 | 실습 4-2 끝의 「이번 Unit 마무리 · 깃허브에 올리기」에서 파일을 확인하고 올립니다 |

없는 이전 파일은 「이전 파일이 없을 때」 코드 상자로 만듭니다. 보고서는 실습 시간 안에서, 실습마다 끝에 나오는 안내에 따라 그때그때 씁니다. 꼭 채울 칸은 세 칸(실습 4-1 (가) · 실습 4-2 (가) · 마무리 (가))이고, 나머지는 응용입니다. 하루 3시간에서 남는 20분쯤은 밀린 곳을 따라잡는 여유 시간입니다.

**오늘 만들 것 두 가지**

1. **실습 4-1**: 조치 요청마다 위험 점수(risk score, 리스크 스코어: 조치의 위험을 점수로 나타낸 값)를 더해 「자동 · 승인 필요 · 차단 금지」로 나누는 승인 게이트를 만듭니다. <mark style="background:#ffdcb0">승인 기준은 설정 파일에 따로 둡니다</mark>(`approval_gate.py`).
2. **실습 4-2**: 오탐(false positive, 폴스 포지티브: 위협이 아닌 활동을 위협으로 잘못 판정한 알림) 신고를 받으면 먼저 영향 확인(impact assessment: 조치가 실제로 바꾼 대상을 파악하는 일)을 합니다. 그다음 <mark style="background:#e0d4ff">Unit 3 실습 3-1 의 되돌리기 함수</mark>로 롤백(rollback, 롤백: 조치 이전 상태로 되돌리는 일)하고, 복구 확인(recovery verification: 실제 상태가 되돌아왔는지 다시 점검하는 일)까지 합니다(`false_positive.py`).

**응용 4-1 ~ 4-5는 여유가 되면 해 보세요.** 핵심 실습 두 개와 글쓰기를 마치고 시간이 남을 때, 하고 싶은 것만 골라 합니다. 응용을 하지 않아도 다음 Unit 을 따라갈 수 있습니다.

| 응용 | 하는 일 | 더 필요한 것 |
|---|---|---|
| 응용 4-1 | 응답 기한을 넘긴 티켓을 상급자에게 올리기 | `flask` · `requests`, 알림 서버 |
| 응용 4-2 | 근무 3시간 시뮬레이션과 대응 지표 | 응용 4-1 과 같음 |
| 응용 4-3 | 초동 대응 리포트 파일 만들기 | 판다스(`pandas`) |
| 응용 4-4 | 자동 조치 리스크 평가 문서 쓰기 | 판다스 |
| 응용 4-5 | 오늘 만든 것을 평가 기준으로 자동 점검 | 판다스, 실습 4-1 · 4-2 파일, 응용 4-3 이 만드는 파일(없으면 응용 4-5 의 상자와 「제공 파일」 `report.py`) |

- 필요한 설치와 파일 준비는 각 응용 레슨의 맨 앞에 있습니다. 「제공 파일」 레슨의 `escalation.py` · `report.py` 는 응용 4-1 · 4-3 을 건너뛰고 그 뒤 응용을 할 때 씁니다.
- 핵심 실습마다 직접 쓰는 곳은 두 줄(① · ②)입니다. 나머지는 미리 채워 두었습니다. 번호 주석 바로 아래에 한 줄을 쓰고, 들여쓰기(줄 앞의 빈칸)는 주석 끝 괄호에 적힌 칸 수(예: `(8칸)`)를 따릅니다. 주석은 지우지 않습니다.
- 보고서의 [핵심 질문] 표시가 붙은 질문은 <mark>내 출력 값을 근거로</mark> 씁니다.

**줄임말 이름 안내** — 응용 4-1 ~ 4-3 의 코드와 파일에는 줄임말로 된 이름이 있습니다. 이미 배포한 파일과 맞추려고 이름은 그대로 쓰고 뜻만 풀어 둡니다.

| 이름 | 원래 말 | 이 문서에서의 뜻 |
|---|---|---|
| `ack` · `acked` | acknowledge(확인하다) · acknowledged(확인했다) | 담당자가 티켓을 처음 확인했다 |
| `sla` | 서비스 수준 협약(SLA, Service Level Agreement) | 응답 기한 |

`acked_at` 은 처음 확인한 시각(분)이고, `sla_due` 는 응답해야 하는 시각입니다.

> **확인** — 오늘 꼭 할 일이 실습 4-1(`approval_gate.py`) · 실습 4-2(`false_positive.py`) · 세 문장 글 한 편이라고 말할 수 있으면 성공입니다. 헷갈리면 위 「오늘의 계획」 표와 「오늘 만들 것 두 가지」를 다시 봅니다.

## 폴더 열고 이전 파일 확인하기

오늘 핵심 실습은 앞 Unit 파일을 `import` 로 불러 씁니다. `soar_response` 폴더에 아래 파일이 있는지 봅니다.

| 어디 파일 | 파일 | 쓰는 곳 |
|---|---|---|
| Unit 1 실습 1-2 | `incident.py`(`load_json` · `save_json`) | 모든 실습 |
| Unit 2 실습 2-1 | `containment_store.py` · `account_actions.py` | 실습 4-2 |
| Unit 2 「제공 파일」 레슨 | `ip_actions.py` | 실습 4-2 |
| Unit 3 실습 3-1 | `undo_actions.py` · `rollback.py` | 실습 4-2 |

**순서**

1. **[VS Code]** `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `soar_response` 폴더로 들어가 파일을 확인합니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. **[터미널]** 여섯 파일을 불러올 수 있는지 확인합니다(맥북은 `python3`). <mark>`이전 파일 정상` 이 나와야</mark> 합니다.
   ```bash
   python -c "import incident, containment_store, account_actions, ip_actions, undo_actions, rollback; print('이전 파일 정상')"
   ```
   - `No module named '…'` 가 나오면 그 이름의 파일이 없다는 뜻입니다. 다음 페이지 「이전 파일이 없을 때」의 코드 상자로 그 파일만 만들고 다시 칩니다.

<!-- checklist -->
- [ ] `soar_response` 폴더에서 3번 명령(`python -c "import incident, …"`)을 쳐서 `이전 파일 정상` 이 나왔는지, 아니면 없는 파일 이름이 무엇인지 확인했다
<!-- /checklist -->

4. **파일은 이렇게 만듭니다.** 따로 내려받는 파일은 없고, 모두 코드 상자에서 복사해 만듭니다.
   1. **[VS Code]** 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. `config/` 로 시작하는 파일은 `soar_response` 폴더 안의 `config` 폴더를 오른쪽 클릭해 만듭니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u4.md` 는 「보고서 쓰기」 레슨의 틀을 복사해 만듭니다.
5. 확인이 끝나면 실습 4-1 로 갑니다. 실습 4-1 은 `incident.py` 만 있으면 되고, 나머지 다섯 파일은 실습 4-2 에서 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark style="background:#ffc4d6">**터미널**에서</mark> 합니다. **앞 Unit 파일은 고치지 않습니다.** 실행할 때마다 같은 입력 파일에서 시작하므로 같은 결과가 나옵니다.

> **확인** — 3번 명령이 `이전 파일 정상` 한 줄을 출력하면 성공입니다. `No module named '…'` 가 나오면 다음 페이지에서 그 이름의 파일만 만들고 3번 명령을 다시 칩니다.

## 이전 파일이 없을 때 (Unit 1 · Unit 2 · Unit 3 파일)

앞 Unit 을 하지 못했거나 파일을 지운 경우에만 만듭니다. **이미 있는 파일은 건너뜁니다.** 파일 이름은 `incident.py` · `containment_store.py` · `account_actions.py` · `ip_actions.py` · `undo_actions.py` · `rollback.py` 이고, 앞 페이지의 4번 방법으로 하나씩 만듭니다.

**`incident.py`** — Unit 1 파일에서 오늘 쓰는 두 함수(`load_json` · `save_json`)만 담았습니다. Unit 1 파일 전체가 있으면 그것을 그대로 씁니다.

```python
import json                                                  # JSON 파일을 읽고 쓰기 위해 json 을 불러온다


def load_json(path):                                         # 파일 경로를 받는 함수
    """JSON 파일을 읽어 리스트나 딕셔너리로 리턴한다.
    인시던트와 플레이북 등록 파일을 읽을 때 쓴다.
    """
    with open(path, encoding="utf-8") as file:               # 파일을 읽기 모드로 연다
        data = json.load(file)                               # JSON 글자를 파이썬 값으로 바꾼다
    return data                                              # 읽은 값을 리턴한다


def save_json(data, path):                                   # 저장할 값과 파일 경로를 받는 함수
    """값을 JSON 파일로 저장한다.
    실행 결과 상태와 감사 기록을 남길 때 쓴다.
    """
    with open(path, "w", encoding="utf-8") as file:          # 파일을 쓰기 모드로 연다
        json.dump(data, file, ensure_ascii=False, indent=2)  # 한글은 그대로, 줄을 나눠 저장한다
```

**`containment_store.py`** — Unit 2 실습 2-1 파일입니다. 조치 기록 한 건을 만들고 조치 상태를 파일로 저장하고 읽습니다.

```python
import copy                                                           # 처음 상태를 복사해 쓰기 위해 copy 를 불러온다
from incident import load_json, save_json                             # Unit 1 파일의 파일 읽기 · 쓰기 함수를 불러온다

STATE_PATH = "containment_state.json"                                 # 연습용 시스템 상태를 저장할 파일 이름
LOG_PATH = "containment_log.json"                                     # 조치 기록을 저장할 파일 이름
INITIAL_STATE = {                                                     # 수업을 시작할 때의 연습용 시스템 상태
    "locked_users": ["junho"],                                        # 이미 잠겨 있는 계정 : junho 는 수업 전부터 잠겨 있다
    "blocked_ips": [],                                                # 차단한 IP 리스트 : 처음에는 비어 있다
    "block_expiry": {},                                               # IP 별 차단이 끝나는 시각(분) : 처음에는 비어 있다
    "clock": 0,                                                       # 연습용 시스템의 시계(분) : 0 에서 시작한다
    "sessions": {"dami": ["S-101", "S-102"], "seoyeon": ["S-201"], "gaeun": ["S-301"], "jiwoo": ["S-401"], "junho": ["S-501"], "hana": ["S-601"]},  # 계정별로 열려 있는 로그인 세션
}


def new_state():                                                      # 인자가 없는 함수
    """처음 상태를 복사해 새 연습용 시스템 상태를 리턴한다.
    실행할 때마다 같은 상태에서 시작해 결과를 비교할 때 쓴다.
    """
    return copy.deepcopy(INITIAL_STATE)                               # 처음 상태의 복사본을 리턴한다


def save_state(state):                                                # 연습용 시스템 상태를 받는 함수
    """상태를 파일에 저장한다.
    다음 프로그램이 이어서 읽을 수 있게 할 때 쓴다.
    """
    save_json(state, STATE_PATH)                                      # 상태를 JSON 파일로 저장한다


def load_state():                                                     # 인자가 없는 함수
    """저장해 둔 상태 파일을 읽어 리턴한다.
    저장이 제대로 됐는지 확인하거나 이어서 일할 때 쓴다.
    """
    return load_json(STATE_PATH)                                      # 상태 파일을 읽어 리턴한다


def reset_log():                                                      # 인자가 없는 함수
    """조치 기록 파일을 빈 리스트로 비운다.
    실행할 때마다 기록을 처음부터 쌓을 때 쓴다.
    """
    save_json([], LOG_PATH)                                           # 빈 리스트를 기록 파일로 저장한다


def make_record(action, target, incident_id, before, after, reason):  # 조치 이름 · 대상 · 인시던트 번호 · 조치 전 · 조치 후 · 이유를 받는 함수
    """조치 한 건(무엇을 · 누구에게 · 조치 전 · 조치 후 · 이유)의 기록을 딕셔너리로 만들어 리턴한다.
    조치 전과 후 상태를 함께 남겨 두고 싶을 때 쓴다.
    """
    record = {"action": action, "target": target, "incident": incident_id, "before": before, "after": after, "reason": reason}  # 조치 한 건의 기록을 딕셔너리로 만든다
    return record                                                     # 기록 한 건을 리턴한다


def append_log(record):                                               # 기록 한 건을 받는 함수
    """기록 파일을 읽어 기록 한 건을 더하고 다시 저장한다. 파일이 아직 없으면 빈 리스트로 시작한다.
    조치할 때마다 기록을 한 건씩 쌓아 둘 때 쓴다.
    """
    try:                                                              # 파일 읽기를 시도한다
        log = load_json(LOG_PATH)                                     # 기록 파일을 읽는다
    except FileNotFoundError:                                         # 파일이 없으면
        log = []                                                      # 빈 리스트로 시작한다
    log.append(record)                                                # 기록 한 건을 리스트에 추가한다
    save_json(log, LOG_PATH)                                          # 기록 파일로 다시 저장한다
```

**`account_actions.py`** — Unit 2 실습 2-1 파일입니다. 계정을 잠그고 해제합니다.

```python
from containment_store import make_record                                             # 기록 한 건을 만드는 함수를 불러온다


def check_policy(user, vip_accounts):                                                 # 계정 이름과 VIP 계정 리스트를 받는 함수
    """자동으로 조치하면 안 되는 계정(VIP)이면 그 이유 문장을, 아니면 빈 글자("")를 리턴한다.
    경로에서 이미 걸렀어도 조치 함수가 마지막으로 한 번 더 막고 싶을 때 쓴다.
    """
    if user in vip_accounts:                                                          # VIP 계정이면
        return "VIP 계정이라 자동 조치 대상이 아님"                                   # 막는 이유를 리턴한다
    return ""                                                                         # 막을 이유가 없으면 빈 글자를 리턴한다


def verify_locked(user, state):                                                       # 계정 이름과 연습용 시스템 상태를 받는 함수
    """계정이 잠긴 계정 리스트에 들어 있으면 True, 없으면 False 를 리턴한다.
    잠그라고 호출한 것과 실제로 잠긴 것이 같은지 조치 뒤에 확인할 때 쓴다.
    """
    return user in state["locked_users"]                                              # 잠긴 계정 리스트 안에 있는지 확인한 결과를 리턴한다


def lock_account(user, state, vip_accounts, incident_id, reason):                     # 계정 · 상태 · VIP 리스트 · 인시던트 번호 · 이유를 받는 함수
    """VIP 인지 먼저 확인하고 계정을 잠근 뒤, 실제로 잠겼는지 다시 확인해 조치 기록 한 건을 리턴한다.
    VIP 이거나 이미 잠겨 있으면 잠그지 않고 그 이유를 기록에 남긴다.
    """
    blocked = check_policy(user, vip_accounts)                                        # 자동 조치를 막을 이유를 구한다
    if blocked != "":                                                                 # 막을 이유가 있으면
        return make_record("계정 잠금", user, incident_id, "변경 없음", "변경 없음", blocked)  # 바꾸지 않고 이유를 기록한다
    if user in state["locked_users"]:                                                 # 이미 잠겨 있으면
        return make_record("계정 잠금", user, incident_id, "잠김", "잠김", "이미 잠겨 있어 변경 없음")  # 바꾸지 않고 기록한다
    state["locked_users"].append(user)                                                # 잠긴 계정 리스트에 추가한다
    after = "잠김"                                                                    # 조치 뒤 상태 : 일단 잠겼다고 적고
    if not verify_locked(user, state):                                                # 실제로 확인해 잠기지 않았으면
        after = "잠기지 않음 (확인 실패)"                                             # 확인 실패라고 고쳐 적는다
    return make_record("계정 잠금", user, incident_id, "잠기지 않음", after, reason)  # 조치 전 · 후 상태와 함께 기록한다


def unlock_account(user, state, incident_id, reason):                                 # 계정 · 상태 · 인시던트 번호 · 이유를 받는 함수
    """잠긴 계정을 해제하고 실제로 해제됐는지 확인해 조치 기록 한 건을 리턴한다.
    오탐으로 확인된 계정을 되돌릴 때 쓴다.
    """
    if user not in state["locked_users"]:                                             # 잠겨 있지 않으면
        return make_record("계정 해제", user, incident_id, "잠기지 않음", "잠기지 않음", "잠겨 있지 않아 변경 없음")  # 바꾸지 않고 기록한다
    state["locked_users"].remove(user)                                                # 잠긴 계정 리스트에서 제거한다
    after = "잠기지 않음"                                                             # 조치 뒤 상태 : 일단 해제됐다고 적고
    if verify_locked(user, state):                                                    # 실제로 확인해 아직 잠겨 있으면
        after = "잠김 (확인 실패)"                                                    # 확인 실패라고 고쳐 적는다
    return make_record("계정 해제", user, incident_id, "잠김", after, reason)         # 조치 전 · 후 상태와 함께 기록한다
```

**`ip_actions.py`** — Unit 2 「제공 파일」 레슨의 파일입니다. IP 를 차단하고 해제합니다.

```python
from containment_store import make_record                                                     # 기록 한 건을 만드는 함수를 불러온다

SHARED_IP_LIMIT = 2                                                                           # 한 IP 를 쓰는 계정이 이 수 이상이면 공유 IP 로 본다
DEFAULT_TTL = 120                                                                             # 차단을 유지하는 시간(분)


def is_in_allowlist(ip, allowlist_ips):                                                       # IP 와 허용 목록을 받는 함수
    """IP 가 허용 목록에 있으면 True, 없으면 False 를 리턴한다.
    협력사 사무실처럼 차단하면 안 되는 IP 를 걸러낼 때 쓴다.
    """
    return ip in allowlist_ips                                                                # 허용 목록 안에 있는지 확인한 결과를 리턴한다


def count_users_on_ip(ip, ip_users):                                                          # IP 와 IP 별 사용 계정 딕셔너리를 받는 함수
    """그 IP 를 쓰는 계정이 몇 개인지 리턴한다. ip_users.json 에 없는 IP 는 0 을 리턴한다.
    차단하면 정상 사용자가 몇 명 영향을 받는지 확인할 때 쓴다.
    """
    return len(ip_users.get(ip, []))                                                          # 그 IP 를 쓰는 계정 수를 리턴한다 (목록에 없으면 0)


def check_ip_policy(ip, allowlist_ips, ip_users):                                             # IP · 허용 목록 · 사용 계정 딕셔너리를 받는 함수
    """자동으로 차단하면 안 되는 IP 이면 그 이유 문장을, 아니면 빈 글자("")를 리턴한다.
    허용 목록 IP 이거나 여러 계정이 함께 쓰는 IP 를 차단하기 전에 가려낼 때 쓴다.
    """
    if is_in_allowlist(ip, allowlist_ips):                                                    # 허용 목록 IP 이면
        return "허용 목록 IP 라서 차단하지 않음"                                              # 이유를 리턴한다
    if count_users_on_ip(ip, ip_users) >= SHARED_IP_LIMIT:                                    # 여러 계정이 함께 쓰는 IP 이면
        return "여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요"                               # 이유를 리턴한다
    return ""                                                                                 # 막을 이유가 없으면 빈 글자를 리턴한다


def block_ip(ip, state, incident_id, reason, ttl):                                            # IP · 상태 · 인시던트 번호 · 이유 · 유지 시간을 받는 함수
    """IP 를 차단하고 끝나는 시각을 적은 뒤, 실제로 차단됐는지 확인해 기록 한 건을 리턴한다.
    영구 차단 대신, 시간이 지나면 자동으로 풀리는 임시 차단을 만들 때 쓴다.
    """
    state["blocked_ips"].append(ip)                                                           # 차단한 IP 리스트에 추가한다
    state["block_expiry"][ip] = state["clock"] + ttl                                          # 차단이 끝나는 시각을 적는다
    after = "차단됨"                                                                          # 조치 뒤 상태 : 일단 차단됐다고 적고
    if ip not in state["blocked_ips"]:                                                        # 실제로 확인해 차단되지 않았으면
        after = "차단되지 않음 (확인 실패)"                                                   # 확인 실패라고 고쳐 적는다
    return make_record("IP 차단", ip, incident_id, "차단되지 않음", after, reason + " (" + str(ttl) + "분 뒤 자동 해제)")  # 조치 전 · 후 상태와 함께 기록한다


def unblock_ip(ip, state, incident_id, reason):                                               # IP · 상태 · 인시던트 번호 · 이유를 받는 함수
    """차단한 IP 를 풀고 끝나는 시각 기록도 지운 뒤 기록 한 건을 리턴한다.
    시간이 끝나서 풀거나 오탐으로 풀 때 쓴다.
    """
    state["blocked_ips"].remove(ip)                                                           # 차단 리스트에서 제거한다
    state["block_expiry"].pop(ip)                                                             # 끝나는 시각 기록도 지운다
    return make_record("IP 해제", ip, incident_id, "차단됨", "차단되지 않음", reason)         # 조치 전 · 후 상태와 함께 기록한다


def expire_blocks(state, incident_id):                                                        # 상태와 인시던트 번호를 받는 함수
    """끝나는 시각이 지난 차단을 모두 풀고 해제 기록 리스트를 리턴한다.
    임시 차단이 사람 손 없이 풀리게 할 때 쓴다.
    """
    records = []                                                                              # 해제 기록을 담을 빈 리스트
    for ip in list(state["blocked_ips"]):                                                     # 차단 리스트의 복사본에서 IP 를 하나씩 꺼낸다 (원본을 바꾸며 돌면 안 되기 때문이다)
        end_time = state["block_expiry"][ip]                                                  # 그 IP 의 차단이 끝나는 시각
        if end_time <= state["clock"]:                                                        # 끝나는 시각이 지났으면
            records.append(unblock_ip(ip, state, incident_id, "차단 시간이 끝나 자동 해제"))  # 차단을 풀고 해제 기록을 모은다
    return records                                                                            # 해제 기록 리스트를 리턴한다
```

**`undo_actions.py`** — Unit 3 실습 3-1 파일입니다. 조치 기록 한 건을 거꾸로 되돌립니다.

```python
from account_actions import unlock_account  # Unit 2 에 있는 계정 해제 함수를 불러온다
from ip_actions import unblock_ip           # Unit 2 에 있는 IP 해제 함수를 불러온다


def undo_account(record, state):            # 되돌릴 조치 기록과 연습용 시스템 상태를 받는 함수
    """계정 잠금 기록 한 건을 되돌려 계정을 해제하고, 해제 기록을 리턴한다.
    자동으로 잠근 계정을 오탐이 확인된 뒤에 원래대로 풀 때 쓴다.
    """
    return unlock_account(record["target"], state, record["incident"], "되돌리기: " + record["reason"])  # 계정 해제를 실행하고 기록을 리턴한다


def undo_ip(record, state):                 # 되돌릴 조치 기록과 연습용 시스템 상태를 받는 함수
    """IP 차단 기록 한 건을 되돌려 IP 차단을 풀고, 해제 기록을 리턴한다.
    자동으로 차단한 IP 를 오탐이 확인된 뒤에 원래대로 풀 때 쓴다.
    """
    return unblock_ip(record["target"], state, record["incident"], "되돌리기: " + record["reason"])  # IP 해제를 실행하고 기록을 리턴한다


def undo_record(record, state):             # 되돌릴 조치 기록과 연습용 시스템 상태를 받는 함수
    """조치 종류(계정 잠금 · IP 차단)에 맞는 되돌리기 함수를 골라 불러서, 해제 기록을 리턴한다.
    기록 한 건을 받아 알맞은 방법으로 되돌릴 때 쓴다.
    """
    if record["action"] == "계정 잠금":     # 계정 잠금 기록이면
        return undo_account(record, state)  # 계정을 해제한다
    return undo_ip(record, state)           # 아니면 IP 차단 기록이므로 IP 를 해제한다
```

**`rollback.py`** — Unit 3 실습 3-1 파일입니다. 인시던트 한 건의 조치 기록을 찾아 되돌립니다.

```python
from containment_store import make_record                                    # 기록 한 건을 만드는 함수를 불러온다
from undo_actions import undo_record                                         # 되돌리기 함수를 불러온다

UNDOABLE_ACTIONS = ["계정 잠금", "IP 차단"]                                  # 해제로 되돌릴 수 있는 조치 이름


def find_incident_records(log, incident_id):                                 # 기록 리스트와 인시던트 번호를 받는 함수
    """기록 중 그 인시던트(알림 한 건)의 기록만 모은 뒤, 나중에 한 일이 먼저 오도록 순서를 뒤집어 리턴한다.
    조치를 거꾸로 되돌릴 때 쓴다.
    """
    found = []                                                               # 그 인시던트의 기록을 담을 빈 리스트
    for record in log:                                                       # 기록을 하나씩 꺼낸다
        if record["incident"] == incident_id:                                # 그 인시던트의 기록이면
            found.append(record)                                             # 모아 둔다
    return list(reversed(found))                                             # 순서를 뒤집어 리턴한다


def should_undo(record):                                                     # 기록 한 건을 받는 함수
    """자동 조치가 실제로 바꾼 것이고 해제로 되돌릴 수 있으면 True, 아니면 False 를 리턴한다.
    조치 전부터 그 상태였던 것과 확인에 실패한 조치는 되돌리지 않으려고 쓴다.
    """
    if record["before"] == record["after"]:                                  # 조치 전과 후가 같으면
        return False                                                         # 바뀐 것이 없으니 되돌리지 않는다
    if "확인 실패" in record["after"]:                                       # 확인에 실패한 조치이면
        return False                                                         # 실제로 바뀌지 않았으니 되돌리지 않는다
    return record["action"] in UNDOABLE_ACTIONS                              # 해제로 되돌릴 수 있는 조치 종류인지의 결과를 리턴한다


def rollback_incident(incident_id, log, state):                              # 인시던트 번호 · 기록 리스트 · 연습용 시스템 상태를 받는 함수
    """인시던트의 기록을 거꾸로 훑으며 자동이 바꾼 것만 되돌리고, 되돌릴 수 없는 조치는 따로 기록해 리턴한다.
    조치 전부터 있던 상태를 건드리지 않고 오탐을 복구할 때 쓴다.
    """
    records = []                                                             # 되돌리기 기록을 담을 빈 리스트
    for record in find_incident_records(log, incident_id):                   # 그 인시던트의 기록을 하나씩 꺼낸다
        if should_undo(record):                                              # 자동이 바꾼 것이고 되돌릴 수 있으면
            records.append(undo_record(record, state))                       # 되돌리고 해제 기록을 모은다
        if record["before"] != record["after"] and not should_undo(record):  # 바뀌었는데 되돌릴 수 없는 조치이면
            note = "되돌릴 수 없는 조치(" + record["action"] + ") — 사용자가 다시 로그인해야 함"  # 이유 문장을 만들고
            records.append(make_record("되돌리기 불가", record["target"], incident_id, record["before"], record["after"], note))  # 기록으로 남긴다
    return records                                                           # 되돌리기 기록 리스트를 리턴한다
```

> **확인** — 만든 뒤 앞 페이지 3번 명령(`python -c "import incident, …"`)을 다시 쳐서 `이전 파일 정상` 이 나오면 성공입니다. 또 오류가 나면 다음 페이지 「오류가 나면」의 표에서 그 메시지를 찾습니다.

<!-- checklist -->
- [ ] `No module named '…'` 에 나온 파일만 `soar_response` 폴더에 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다(모두 있었으면 바로 체크)
- [ ] 앞 쪽 3번 명령을 다시 쳐서 `이전 파일 정상` 이 나왔다
<!-- /checklist -->

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError` 는 그 이름의 파일이 이 폴더에 없다는 뜻입니다. 모두 앞 페이지 「이전 파일이 없을 때」의 코드 상자로 만듭니다.

| 오류 메시지 | 뜻 |
|---|---|
| `No module named 'incident'` | <mark style="background:#ffc4d6">Unit 1 파일 `incident.py` 가 이 폴더에 없음</mark> |
| `No module named 'ip_actions'` | Unit 2 파일이 없음 |
| `No module named 'rollback'` | Unit 3 파일이 없음 |

- 먼저 오류 전체와 내가 친 명령을 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 그래도 막히면 이 Unit 의 정답 레슨을 봅니다. 그래도 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> **확인** — 표의 오류가 사라지고 `이전 파일 정상` 이 나오면 성공입니다. 표에 없는 오류가 나오면 오류의 맨 아래 줄을 위 첫 줄의 방법대로 AI 에게 먼저 묻습니다.

---
