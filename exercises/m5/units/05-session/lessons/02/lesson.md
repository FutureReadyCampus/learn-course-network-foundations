---
id: m5-u05-l02
title: 실습 5-1 · 자동 조치 되돌리기와 불가 표시
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/124_day03_pm_rollback_drill.md
  mission_id: GichanSource.m5-1111-pm-rollback-drill
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 5-1 · 자동 조치 되돌리기와 불가 표시

## 목표: 조치 되돌리기

> **오늘 들어온 일**
>
> - **상황**: Unit 4에서 자동 대응이 세 건의 조치를 했습니다. `INC-001` 은 `dami` 의 계정을 잠그고 세션을 종료했습니다. `INC-006` 은 이미 잠겨 있던 `junho` 의 계정은 그대로 두고 세션만 종료했습니다. `INC-005` 는 IP `198.51.100.90` 을 차단했습니다(오늘 실습 5-1 실행 파일이 이 차단을 다시 만듭니다). 그런데 인사 담당자가 「`dami` 는 휴직 복귀 처리 중이라 퇴사자가 아닙니다」라고 알려 왔고, 세 건 모두 **오탐**(false positive, 폴스 포지티브: 위협이 아닌데 위협으로 낸 알림)으로 확인됐습니다(이 실습에서만 가정한 상황이고, Unit 2의 `users_info.json` 의 `dami` 는 퇴사자입니다).
> - **문제**:
> - 사람이 계정 화면에서 직접 풀면, 어느 것이 자동 대응이 한 일인지 알 수 없습니다. 그래서 원래 잠겨 있던 `junho` 까지 풀 수 있습니다.
> - 세션 종료는 되돌릴 수 없습니다(사용자가 다시 로그인해야 합니다). 그런데 「모두 원래대로 되돌렸다」고 보고하면 사실과 다릅니다.
> - **부탁**: 조치 기록을 보고 **자동 대응이 바꾼 것만** 거꾸로 되돌려 주세요. 되돌릴 수 없는 조치는 따로 표시해서 사람이 확인하게 해 주세요.
> - **바뀌는 점**: 자동 대응이 잠근 `dami` 와 차단한 IP 만 풀리고, 원래 잠겨 있던 `junho` 는 그대로 남습니다. `dami` 와 `junho` 의 세션 종료는 「되돌릴 수 없음」으로 따로 표시됩니다. 상황과 이름은 설명을 위한 예시입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 2.1 되돌리기는 「기록을 거꾸로 읽고, 자동이 바꾼 것만 푼다」

**되돌리기**(rollback, 롤백: 자동 조치가 바꾼 것을 조치 전 상태로 바꾸는 것)는 조치 기록의 `before`(조치 전)와 `after`(조치 후)를 비교해 무엇을 되돌릴지 정합니다. 되돌릴 때는 나중에 한 조치부터 거꾸로 읽습니다. 세션 종료처럼 뒤 조치는, 계정 잠금 같은 앞 조치가 끝난 상태에서 한 일이기 때문입니다. 예를 들어 `dami` 는 계정을 먼저 잠그고 세션을 종료했으므로, 세션 종료 기록을 먼저 보고 그다음에 계정 잠금 기록을 봅니다.

| 기록 | 되돌릴까 | 이유 |
|---|---|---|
| 계정 잠금 `잠기지 않음 → 잠김` | 되돌린다 (계정 해제) | 자동이 바꾼 것이다 |
| 계정 잠금 `잠김 → 잠김` (변경 없음) | 되돌리지 않는다 | 조치 전부터 잠겨 있었다 |
| IP 차단 `차단되지 않음 → 차단됨` | 되돌린다 (IP 해제) | 자동이 바꾼 것이다 |
| 세션 종료 `세션 N개 → 세션 0개` | 되돌릴 수 없다 | 사용자가 다시 로그인해야 하므로 따로 표시한다 |
| 조치 후 상태에 `확인 실패` | 되돌리지 않는다 | 실제로 바뀐 적이 없다 |

- 먼저 `before` 와 `after` 를 비교합니다. 같으면 원래 그랬던 것이고, 다르면 자동이 바꾼 것입니다. 다만 확인 실패와 세션 종료는 다르더라도 해제로 되돌리지 않습니다.
- 순서를 뒤집는 `reversed` 는 `find_incident_records` 에 이미 채워져 있습니다.

함수는 세 파일에 나뉘어 있고, 직접 쓰는 곳은 **아홉 군데**입니다.

```
undo_actions.py   undo_account         : 계정 잠금 기록을 계정 해제로 되돌린다 (1번)
                  undo_ip              : IP 차단 기록을 IP 해제로 되돌린다 (2번)
                  undo_record          : 조치 종류에 맞는 되돌리기를 고른다 (미리 채움)
rollback.py       find_incident_records: 그 인시던트(알림 한 건)의 기록만 모은다 (3 · 4번)
                  should_undo          : 조치 전과 후가 같으면 되돌리지 않는다 (5 · 6번). 확인 실패와 되돌릴 수 없는 조치는 미리 채운 줄이 되돌리기 대상에서 뺀다
                  rollback_incident    : 되돌릴 수 있는 기록은 되돌리고 (7 · 8번), 되돌릴 수 없는 조치는 따로 기록한다 (미리 채움)
실행 파일         exercise5-1_run.py     : 실습 4-3이 저장한 기록을 읽는다 (9번)
```

> **여기부터 문제입니다.**

## 실습 5-1 · 기록을 보고 자동이 바꾼 것만 되돌리기

**이런 상황이 있습니다**

- **지금은**: <mark>오탐이 확인돼도 어느 것이 자동 조치인지 구분하는 기능이 없어서, 사람이 추측으로 풀고 있습니다</mark>.
- **만드는 것**: 계정 · IP 되돌리기(`undo_actions.py`), 기록 찾기 · 되돌릴지 정하기 · 되돌리기(`rollback.py`), 기록 읽기(`exercise5-1_run.py`).
- **실행하면**: <mark>단계 1: 실습 4-3이 남긴 파일(그리고 이 실행이 새로 차단한 IP), 단계 2 ~ 4: 인시던트(incident, 인시던트: 알림 한 건을 처리하는 단위) 세 건의 되돌리기 결과, 단계 5: 되돌린 뒤 상태가 나옵니다.</mark>

**할 일**: 파일 세 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 ~ 5 를 읽습니다.

**`undo_actions.py`** — 되돌리기 실행입니다. 직접 쓰는 곳은 1 · 2번입니다.

```python
from account_actions import unlock_account  # Unit 4의 실습 4-1에서 만든 계정 해제 함수를 불러온다
from ip_actions import unblock_ip           # Unit 4의 실습 4-2에서 만든 IP 해제 함수를 불러온다


def undo_account(record, state):            # 되돌릴 조치 기록과 연습용 시스템 상태를 받는 함수
    """계정 잠금 기록 한 건을 되돌려 계정을 해제하고, 해제 기록을 리턴한다.
    자동으로 잠근 계정을 오탐이 확인된 뒤에 원래대로 풀 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. unlock_account(record["target"], state, record["incident"], "되돌리기: " + record["reason"]) 의 결과를 리턴한다


def undo_ip(record, state):                 # 되돌릴 조치 기록과 연습용 시스템 상태를 받는 함수
    """IP 차단 기록 한 건을 되돌려 IP 차단을 풀고, 해제 기록을 리턴한다.
    자동으로 차단한 IP 를 오탐이 확인된 뒤에 원래대로 풀 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. unblock_ip(record["target"], state, record["incident"], "되돌리기: " + record["reason"]) 의 결과를 리턴한다


def undo_record(record, state):             # 되돌릴 조치 기록과 연습용 시스템 상태를 받는 함수
    """조치 종류(계정 잠금 · IP 차단)에 맞는 되돌리기 함수를 골라 불러서, 해제 기록을 리턴한다.
    기록 한 건을 받아 알맞은 방법으로 되돌릴 때 쓴다.
    """
    if record["action"] == "계정 잠금":     # 계정 잠금 기록이면 — 미리 채운 줄
        return undo_account(record, state)  # 계정을 해제한다 — 미리 채운 줄
    return undo_ip(record, state)           # 아니면 IP 차단 기록이므로 IP 를 해제한다 — 미리 채운 줄
```

**`rollback.py`** — 기록을 찾고 되돌릴지 판단합니다. 직접 쓰는 곳은 3 ~ 8번입니다.

```python
from containment_store import make_record                                    # 기록 한 건을 만드는 함수를 불러온다
from undo_actions import undo_record                                         # 방금 만든 되돌리기 함수를 불러온다

UNDOABLE_ACTIONS = ["계정 잠금", "IP 차단"]                                  # 해제로 되돌릴 수 있는 조치 이름


def find_incident_records(log, incident_id):                                 # 기록 리스트와 인시던트 번호를 받는 함수
    """기록 중 그 인시던트(알림 한 건)의 기록만 모은 뒤, 나중에 한 일이 먼저 오도록 순서를 뒤집어 리턴한다.
    조치를 거꾸로 되돌릴 때 쓴다.
    """
    found = []                                                               # 그 인시던트의 기록을 저장할 빈 리스트
    for record in log:                                                       # 기록을 하나씩 꺼낸다
        action_name = record["action"]                                       # 기록의 조치 이름 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. record 의 "incident" 가 incident_id 와 같으면 (if, ==)
        # 4.   found 에 record 를 추가한다 (append)
    return list(reversed(found))                                             # 순서를 뒤집어 리턴한다 — 미리 채운 줄


def should_undo(record):                                                     # 기록 한 건을 받는 함수
    """자동 조치가 실제로 바꾼 것이고 해제로 되돌릴 수 있으면 True, 아니면 False 를 리턴한다.
    조치 전부터 그 상태였던 것과 확인에 실패한 조치는 되돌리지 않으려고 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. record 의 "before" 와 "after" 가 같으면 (if, ==)
    # 6.   False 를 리턴한다 (바뀐 것이 없으니 되돌릴 것도 없다)
    if "확인 실패" in record["after"]:                                       # 확인에 실패한 조치이면 — 미리 채운 줄
        return False                                                         # 실제로 바뀌지 않았으니 되돌리지 않는다 — 미리 채운 줄
    return record["action"] in UNDOABLE_ACTIONS                              # 해제로 되돌릴 수 있는 조치 종류인지의 결과를 리턴한다 — 미리 채운 줄


def rollback_incident(incident_id, log, state):                              # 인시던트 번호 · 기록 리스트 · 연습용 시스템 상태를 받는 함수
    """인시던트의 기록을 거꾸로 훑으며 자동이 바꾼 것만 되돌리고, 되돌릴 수 없는 조치는 따로 기록해 리턴한다.
    조치 전부터 있던 상태를 건드리지 않고 오탐을 복구할 때 쓴다.
    """
    records = []                                                             # 되돌리기 기록을 저장할 빈 리스트
    for record in find_incident_records(log, incident_id):                   # 그 인시던트의 기록을 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 7. should_undo(record) 가 참이면 (if)
        # 8.   undo_record(record, state) 의 결과를 records 에 추가한다 (append)
        if record["before"] != record["after"] and not should_undo(record):  # 바뀌었는데 되돌릴 수 없는 조치이면 — 미리 채운 줄
            note = "되돌릴 수 없는 조치(" + record["action"] + ") — 사용자가 다시 로그인해야 함"  # 이유 문장을 만들고 — 미리 채운 줄
            records.append(make_record("되돌리기 불가", record["target"], incident_id, record["before"], record["after"], note))  # 기록으로 남긴다 — 미리 채운 줄
    return records                                                           # 되돌리기 기록 리스트를 리턴한다
```

**`exercise5-1_run.py`** — 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 이 실행 파일은 먼저 INC-005 의 IP 차단을 새로 실행해 기록에 추가한 뒤, 그것을 되돌립니다.

```python
from incident import load_json                                                     # Unit 1 파일의 함수를 불러온다
from containment_store import load_state, LOG_PATH                                 # 실습 4-3이 저장한 상태 · 기록 파일을 읽는 함수를 불러온다
from ip_actions import block_ip, DEFAULT_TTL                                       # Unit 4의 실습 4-2의 IP 차단 함수를 불러온다
from rollback import rollback_incident                                             # 방금 만든 되돌리기 함수를 불러온다

state = load_state()                                                               # 실습 4-3이 저장한 연습용 시스템 상태를 읽는다
# ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
# 9. load_json(LOG_PATH) 의 결과를 log 에 저장한다 (실습 4-3이 저장한 조치 기록을 읽는다)

print("--- 단계 1: 실습 4-3이 남긴 파일")                                             # 단계 1 시작을 알리는 줄
print("잠긴 계정:", state["locked_users"])                                         # 잠긴 계정을 출력한다
print("조치 기록:", len(log), "건")                                                # 기록 수를 출력한다
log.append(block_ip("198.51.100.90", state, "INC-005", "경로 스캔", DEFAULT_TTL))  # INC-005 의 IP 차단을 이 실행에서 추가한다
print("차단한 IP:", state["blocked_ips"])                                          # 차단한 IP 를 출력한다

for incident_id, title in [("INC-001", "단계 2: INC-001 은 오탐으로 확인됨 — 되돌리기"), ("INC-006", "단계 3: INC-006 도 오탐으로 확인됨 — 되돌리기"), ("INC-005", "단계 4: INC-005 도 오탐으로 확인됨 — 되돌리기")]:  # 되돌릴 인시던트 3건 : (번호, 제목)
    print("---", title)                                                            # 단계 제목을 출력한다
    for record in rollback_incident(incident_id, log, state):                      # 되돌리기 기록을 하나씩 꺼낸다
        print(record["incident"], record["target"], "·", record["action"], "·", record["before"], "→", record["after"], "·", record["reason"])  # 기록 한 건을 출력한다

print("--- 단계 5: 되돌린 뒤 상태")                                                # 단계 5 시작을 알리는 줄
print("잠긴 계정:", state["locked_users"])                                         # 잠긴 계정을 출력한다
print("차단한 IP:", state["blocked_ips"])                                          # 차단한 IP 를 출력한다
```

**순서**

1. **[터미널]** 파일 세 개를 만들고 **[VS Code]** 에서 열어 붙여 넣습니다.
   ```bash
   pwd
   touch undo_actions.py rollback.py exercise5-1_run.py
   ls
   ```
2. **[VS Code]** `undo_actions.py` 1 · 2번, `rollback.py` 3 ~ 8번, `exercise5-1_run.py` 9번을 씁니다. 막히면 아래 「실습 5-1 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise5-1_run.py
   ```
4. 출력은 다섯 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 3줄, 단계 2 는 2줄, 단계 3 은 1줄, 단계 4 는 1줄, 단계 5 는 2줄입니다.
5. **[보고서]** Unit 5 의 `## 실습 5-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣어 주세요. 그리고 단계 5 의 잠긴 계정과 차단한 IP 를 적어 주세요.
   - (나) [핵심 질문] INC-006 의 `junho` 는 단계 3 에서 계정이 해제되지 않았고 단계 5 에도 잠겨 있습니다. 실습 4-3 기록의 `before` 와 `after` 를 근거로 이유를 적고, `should_undo` 의 5 · 6번이 없었다면 어떤 일이 생겼을지 적어 주세요.
   - (다) [핵심 질문] 단계 2 의 `되돌리기 불가` 줄이 나온 이유를 적어 주세요. 또 세션 종료를 기록에 남기지 않고 「모두 원래대로」라고만 보고하면 어떤 문제가 생길지 적어 주세요.

## 실습 5-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 다른 함수의 결과를 그대로 리턴 | `return unlock_account(record["target"], state, record["incident"], "되돌리기: " + record["reason"])` |
| 값이 같으면 | `if record["incident"] == incident_id:` |
| 리스트에 추가 | `found.append(record)` |
| 조치 전과 후가 같으면 | `if record["before"] == record["after"]:` |
| 거짓으로 리턴 | `return False` |
| 함수 결과가 참이면 | `if should_undo(record):` |
| 파일에서 읽어 변수에 저장 | `log = load_json(LOG_PATH)` |

---
