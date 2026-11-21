---
id: m5-u03-l02
title: 실습 3-1 · 자동 조치 되돌리기와 불가 표시
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/124_day03_pm_rollback_drill.md
  mission_id: GichanSource.m5-1111-pm-rollback-drill
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 3-1 · 자동 조치 되돌리기와 불가 표시

## 목표: 조치 되돌리기

> **오늘 들어온 일**
>
> - **상황**: Unit 2 실습 2-2에서 자동 대응이 두 건의 조치를 했습니다. `INC-001` 은 `dami` 의 계정을 잠그고 세션을 종료했습니다. `INC-006` 은 이미 잠겨 있던 `junho` 의 계정은 그대로 두고 세션만 종료했습니다. 여기에 `INC-005` 의 IP `198.51.100.90` 차단이 더해집니다. 이 차단은 Unit 2 응용 2-3에서 다룬 조치라서, 오늘 실습 3-1 실행 파일이 먼저 한 번 다시 실행해 기록에 넣습니다. 그런데 인사 담당자가 「`dami` 는 휴직 복귀 처리 중이라 퇴사자가 아닙니다」라고 알려 왔고, 세 건 모두 **오탐**(false positive, 폴스 포지티브: 위협이 아닌데 위협으로 낸 알림)으로 확인됐습니다(이 실습에서만 가정한 상황이고, Unit 1 `users_info.json` 에서는 `dami` 가 퇴사자입니다).
> - **문제**:
> - 사람이 계정 화면에서 직접 풀면, 어느 것이 자동 대응이 한 일인지 알 수 없습니다. 그래서 원래 잠겨 있던 `junho` 까지 풀 수 있습니다.
> - 세션 종료는 되돌릴 수 없습니다(사용자가 다시 로그인해야 합니다). 그런데 「모두 원래대로 되돌렸다」고 보고하면 사실과 다릅니다.
> - **부탁**: 조치 기록을 보고 **자동 대응이 바꾼 것만** 거꾸로 되돌려 주세요. 되돌릴 수 없는 조치는 따로 표시해서 사람이 확인하게 해 주세요.
> - **바뀌는 점**: 자동 대응이 잠근 `dami` 와 차단한 IP 만 풀리고, 원래 잠겨 있던 `junho` 는 그대로 남습니다. `dami` 와 `junho` 의 세션 종료는 「되돌릴 수 없음」으로 따로 표시됩니다. 상황과 이름은 설명을 위한 예시입니다.

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
- 순서를 뒤집는 줄 `list(reversed(found))` 는 `find_incident_records` 에 이미 채워져 있습니다. `reversed(found)` 가 리스트를 뒤에서부터 읽게 하고, `list(…)` 가 그 결과를 다시 리스트로 만듭니다.
- 미리 채운 `should_undo` 의 `in` 은 두 가지로 쓰입니다. `"확인 실패" in record["after"]` 는 문자열 안에 그 글자가 들어 있는지, `record["action"] in UNDOABLE_ACTIONS` 는 리스트에 그 이름이 있는지 검사합니다.

**직접 쓰는 곳은 두 군데**(① · ②)입니다. 함수는 세 파일에 나뉘어 있고, 나머지는 모두 미리 채워 두었습니다.

| 파일 | 함수 | 직접 쓰는 곳 | 하는 일 |
|---|---|---|---|
| `undo_actions.py` | `undo_account` · `undo_ip` | 없음 | 계정 해제 · IP 해제로 되돌린다 |
| `undo_actions.py` | `undo_record` | 없음 | 조치 종류에 맞는 되돌리기를 고른다 |
| `rollback.py` | `find_incident_records` | 없음 | 그 인시던트(알림 한 건)의 기록만 모은다 |
| `rollback.py` | `should_undo` | ① · ② | 조치 전과 후가 같으면 되돌리지 않는다 |
| `rollback.py` | `rollback_incident` | 없음 | 되돌릴 수 있는 기록은 되돌린다 |
| `exercise3-1_run.py` | (실행 파일) | 없음 | 실습 2-2가 저장한 기록을 읽는다 |

- 직접 쓰는 곳은 위 표 첫 줄, 「`before` 와 `after` 가 같은가?」 검사입니다. 이 두 줄이 「원래 그랬던 것」과 「자동이 바꾼 것」을 가릅니다.
- `should_undo` 에서 확인 실패와 되돌릴 수 없는 조치를 빼는 줄, `rollback_incident` 에서 되돌릴 수 없는 조치를 따로 기록하는 줄은 미리 채워져 있습니다.

#### 문법 상자 · 직접 쓰는 곳의 모양 (예시 값 · 읽기만 합니다)

```python
record = {"before": "잠김", "after": "잠김"}     # 예시 기록 한 건
print(record["before"] == record["after"])       # True  · 두 값이 같으면 True

if record["before"] == record["after"]:          # 같으면 (if 줄 끝에는 : 을 붙인다)
    print("되돌리지 않음")                        # if 안쪽 줄은 4칸 더 들여 쓴다
```

- `==` 는 두 값이 같은지 검사합니다. `=`(저장) 하나만 쓰면 `SyntaxError` 가 납니다.
- 함수 안에서 `return False` 를 만나면 `False` 를 돌려주고 그 자리에서 함수가 끝납니다. 아래 줄은 실행하지 않습니다.

## 실습 3-1 · 기록을 보고 자동이 바꾼 것만 되돌리기

**이런 상황이 있습니다**

- **지금은**: <mark>오탐이 확인돼도 어느 것이 자동 조치인지 구분하는 기능이 없어서, 사람이 추측으로 풀고 있습니다</mark>.
- **만드는 것**: 계정 · IP 되돌리기(`undo_actions.py`), 기록 찾기 · 되돌릴지 정하기 · 되돌리기(`rollback.py`), 기록 읽기(`exercise3-1_run.py`).
- **실행하면**: <mark>단계 1: 실습 2-2가 남긴 파일(그리고 이 실행이 새로 차단한 IP), 단계 2 ~ 4: 인시던트(incident, 인시던트: 알림 한 건을 처리하는 단위) 세 건의 되돌리기 결과, 단계 5: 되돌린 뒤 상태가 나옵니다.</mark>

**할 일**

1. 파일 세 개를 만들어 아래 코드를 붙여 넣습니다.
2. `rollback.py` 의 `# ←` 가 있는 <mark>두 곳</mark>(① · ②)을 한 줄씩 채웁니다.
3. 채우기 <mark>전과 후</mark>의 단계 3 · 단계 5 를 비교합니다.

**`undo_actions.py`** — 되돌리기 실행입니다. 직접 쓰는 곳이 없으니 그대로 붙여 넣습니다.

```python
from account_actions import unlock_account  # Unit 2 실습 2-1 에서 만든 계정 해제 함수를 불러온다
from ip_actions import unblock_ip           # Unit 2 제공 파일의 IP 해제 함수를 불러온다


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

**`rollback.py`** — 기록을 찾고 되돌릴지 판단합니다. 직접 쓰는 곳은 `should_undo` 의 ① · ② 입니다.

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
        action_name = record["action"]                                       # 기록의 조치 이름
        if record["incident"] == incident_id:                                # 그 인시던트의 기록이면
            found.append(record)                                             # 모아 둔다
    return list(reversed(found))                                             # 순서를 뒤집어 리턴한다


def should_undo(record):                                                     # 기록 한 건을 받는 함수
    """자동 조치가 실제로 바꾼 것이고 해제로 되돌릴 수 있으면 True, 아니면 False 를 리턴한다.
    조치 전부터 그 상태였던 것과 확인에 실패한 조치는 되돌리지 않으려고 쓴다.
    """
    # ① record 의 "before" 와 "after" 가 같으면 (if, ==)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    # ② False 를 리턴한다 (바뀐 것이 없으니 되돌릴 것도 없다)   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
    if "확인 실패" in record["after"]:                                       # 확인에 실패한 조치이면
        return False                                                         # 실제로 바뀌지 않았으니 되돌리지 않는다
    return record["action"] in UNDOABLE_ACTIONS                              # 해제로 되돌릴 수 있는 조치 종류인지의 결과를 리턴한다


def rollback_incident(incident_id, log, state):                              # 인시던트 번호 · 기록 리스트 · 연습용 시스템 상태를 받는 함수
    """인시던트의 기록을 거꾸로 훑으며 자동이 바꾼 것만 되돌리고, 되돌릴 수 없는 조치는 따로 기록해 리턴한다.
    조치 전부터 있던 상태를 건드리지 않고 오탐을 복구할 때 쓴다.
    """
    records = []                                                             # 되돌리기 기록을 저장할 빈 리스트
    for record in find_incident_records(log, incident_id):                   # 그 인시던트의 기록을 하나씩 꺼낸다
        if should_undo(record):                                              # 자동이 바꾼 것이고 되돌릴 수 있으면
            records.append(undo_record(record, state))                       # 되돌리고 해제 기록을 모은다
        if record["before"] != record["after"] and not should_undo(record):  # 바뀌었는데 되돌릴 수 없는 조치이면
            note = "되돌릴 수 없는 조치(" + record["action"] + ") — 사용자가 다시 로그인해야 함"  # 이유 문장을 만들고
            records.append(make_record("되돌리기 불가", record["target"], incident_id, record["before"], record["after"], note))  # 기록으로 남긴다
    return records                                                           # 되돌리기 기록 리스트를 리턴한다
```

**`exercise3-1_run.py`** — 직접 쓰는 곳이 없으니 그대로 붙여 넣습니다. 이 실행 파일은 실습 2-2 결과 파일 두 개를 읽고, INC-005 의 IP 차단을 새로 실행해 기록에 추가한 뒤, 세 인시던트를 되돌립니다. 아래쪽 `for incident_id, title in [...]` 줄은 (번호, 제목) 두 값을 묶은 쌍을 하나씩 꺼내 `incident_id` 와 `title` 에 나눠 담습니다. 결과 파일이 없으면 시작하기 레슨의 「이전 파일이 없을 때」를 봅니다.

```python
from incident import load_json                                                     # Unit 1 파일의 함수를 불러온다
from containment_store import load_state, LOG_PATH                                 # 실습 2-2가 저장한 상태 · 기록 파일을 읽는 함수를 불러온다
from ip_actions import block_ip, DEFAULT_TTL                                       # Unit 2 제공 파일의 IP 차단 함수를 불러온다
from rollback import rollback_incident                                             # 방금 만든 되돌리기 함수를 불러온다

state = load_state()                                                               # 실습 2-2가 저장한 연습용 시스템 상태를 읽는다
log = load_json(LOG_PATH)                                                          # 실습 2-2가 저장한 조치 기록을 읽는다

print("--- 단계 1: 실습 2-2가 남긴 파일")                                             # 단계 1 시작을 알리는 줄
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

- 주석 줄은 그대로 두고, **각 주석 바로 아래 줄**에 씁니다. ① 은 `if` 줄이라 4칸, ② 는 그 `if` 안쪽의 `return` 줄이라 8칸에서 시작합니다.
- 출력은 다섯 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 채운 뒤에는 단계 1 은 3줄, 단계 2 는 2줄, 단계 3 은 1줄, 단계 4 는 1줄, 단계 5 는 2줄입니다.

**직접 쓰는 곳**

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | `before` 와 `after` 가 같으면 (`if`) | 4칸 |
| ② | `False` 를 리턴 (`return`) | 8칸 |

- ① 확인: ① 만 쓰고 실행하면 `IndentationError: expected an indented block after 'if' statement` 가 나옵니다. ② 를 아직 안 써서 나는 오류이니 정상입니다. 막히면: 위 문법 상자의 `if record["before"] == record["after"]:` 와 같은 모양입니다.
- ② 확인: ② 까지 쓰고 실행하면 단계 3 이 `되돌리기 불가` 한 줄뿐이고 단계 5 가 `잠긴 계정: ['junho']` 이면 성공입니다. 그래도 단계 3 에 `계정 해제` 가 나오면 ① 의 `==` 양쪽이 `"before"` 와 `"after"` 인지 봅니다. 막히면: 바로 아래 미리 채운 `return False` 와 같은 모양입니다.
- 채우기 전에 실행해도 오류 없이 돌아갑니다. 다만 ① · ② 가 없으니 조치 전부터 잠겨 있던 `junho` 까지 풀려, 단계 3 에 `INC-006 junho · 계정 해제 · 잠김 → 잠기지 않음 · …` 이 나오고 단계 5 가 `잠긴 계정: []` 이 됩니다. 「같으면 되돌리지 않는다」 한 줄이 빠지면 사람이 원래 잠가 둔 계정까지 풀린다는 것을 보여 주는 결과입니다.

**순서**

1. **[VS Code]** 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 파일 이름 `undo_actions.py` · `rollback.py` · `exercise3-1_run.py` 를 하나씩 그대로 적어 세 개의 파일을 만듭니다. 각 파일에 이 페이지의 코드 상자를 복사해 붙여 넣고 저장합니다(`Ctrl + S`, 맥북은 `Cmd + S`).
2. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고, **채우기 전에** 한 번 실행해서 단계 3 · 단계 5 를 봅니다(보고서 (나)에서 씁니다. 맥북은 `python3`).
   ```bash
   python exercise3-1_run.py
   ```
   - 명령 풀이: `python` 파이썬으로 파일을 실행 · `exercise3-1_run.py` 실행할 파일
   - 이 실행 파일은 결과 파일을 다시 저장하지 않아서, 채우기 전에 실행해도 실습 2-2 결과 파일은 바뀌지 않습니다.
3. **[VS Code]** `rollback.py` 의 `# ←` 두 곳(① · ②)을 채웁니다. 2.1 의 그림에서 맨 위 「before 와 after 가 같은가?」 칸을 보고 씁니다. 막히면 아래 「실습 3-1 정리」를 봅니다.
4. **[터미널]** 다시 실행합니다. 단계 3 에서 `junho` 가 해제되지 않는지 확인합니다.
   ```bash
   python exercise3-1_run.py
   ```
5. **[보고서]** `report_u3.md` 의 `## 실습 3-1` 아래를 채웁니다.
   - (가) [핵심 질문] 채운 뒤 실행한 출력 전체를 붙여 넣어 주세요. 그리고 단계 5 의 잠긴 계정과 차단한 IP 를 적어 주세요.
   - (나) [핵심 질문] INC-006 의 `junho` 는 채운 뒤에는 단계 3 에서 계정이 해제되지 않았고 단계 5 에도 잠겨 있습니다. 실습 2-2 기록의 `before` 와 `after` 를 근거로 이유를 적고, 채우기 전(① · ② 가 없을 때)의 단계 3 · 단계 5 와 비교해 무엇이 달랐는지 적어 주세요.
   - (다) [응용] 단계 2 의 `되돌리기 불가` 줄이 나온 이유를 적어 주세요. 또 세션 종료를 기록에 남기지 않고 「모두 원래대로」라고만 보고하면 어떤 문제가 생길지 적어 주세요.

**확인** — 다시 실행했을 때 단계 2 에 `되돌리기 불가` · `계정 해제` 두 줄, 단계 3 에 `되돌리기 불가` 한 줄, 단계 4 에 `IP 해제` 한 줄이 나오고, 단계 5 가 `잠긴 계정: ['junho']` · `차단한 IP: []` 이면 성공입니다. 안 나오면 「정답」 레슨의 실습 3-1 출력과 한 줄씩 맞춰 보고, 다른 줄이 있으면 위 「직접 쓰는 곳」의 확인을 다시 봅니다.

## 실습 3-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 조치 전과 후가 같으면 (①) | `if record["before"] == record["after"]:` |
| 거짓으로 리턴 (②) | `return False` |
| 다른 함수의 결과를 그대로 리턴 | `return unlock_account(…)` |
| 같은 인시던트 기록만 모으기 | `if record["incident"] == incident_id:` → `found.append(record)` |
| 나중 것부터 거꾸로 읽기 | `list(reversed(found))` |
| 함수 결과가 참이면 되돌리기 | `if should_undo(record):` |
| 파일에서 읽어 변수에 저장 | `log = load_json(LOG_PATH)` |

---
