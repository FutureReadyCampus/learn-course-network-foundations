---
id: m3-u08-l04
title: 4교시 (12:00–12:50) · 회수 실행하고 이력 남기기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/090_day05_am_revoke.md
  mission_id: GichanSource.m3-1030-am-revoke
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 4교시 (12:00–12:50) · 회수 실행하고 이력 남기기

## 4교시 (12:00–12:50) · 회수 실행하고 이력 남기기

> 📨 **오늘 들어온 일**
>
> A사 관제 담당이 보낸 메시지:
> 「승인이 필요 없거나 승인된 것만 실제로 회수하고, 회수한 내용을 이력 파일로 남겨 주세요. 아직 승인되지 않은 것은 실행하지 말고 「대기」로 남겨 주세요.
>
> 회수한 뒤에는 같은 사용자 · 권한으로 접근을 다시 판정해서 정말 막혔는지 확인해 주세요. 회수했다고 적어 놓고 여전히 접근이 허용되면 안 됩니다.」
> - **왜 중요한가**: 회수했다는 기록만으로는 부족합니다. 다시 판정해 보아야 정말 막혔는지 알 수 있고, 이력이 있어야 나중에 누가 언제 왜 없앴는지 설명할 수 있습니다.

> 📖 **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「✍️ 문제」 전까지는 이 교시의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 📖 왜 필요한가

> 📖 **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 승인 상태까지 정해진 계획을 이제 실행합니다. 승인 상태가 「승인 불필요」 또는 「승인됨」인 계획만 실행하고, 「승인 대기」인 계획은 실행하지 않습니다.
2. 실행한 뒤에는 **같은 사용자 · 권한을 다시 판정**합니다. 10/22(목)의 `evaluate_access` 가 회수 전과 후에 같은 요청을 어떻게 판정하는지 비교하면 회수가 정말 효과가 있었는지 알 수 있습니다.
3. 실행한 내용은 **회수 이력**(`revocation_log.json`)으로 남깁니다. 어제의 「사용 이력」(권한을 마지막으로 쓴 시각의 기록)과 다른 것입니다. 회수 이력은 오늘 무엇을 회수했는지의 기록입니다.

## 📖 4.1 실행 방법과 이력

> 📖 **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

| 방법 | 실제로 하는 일 |
|---|---|
| 예외 삭제 | 예외 리스트(`EXCEPTIONS`)에서 번호가 `target` 인 예외 한 건을 지움 |
| 역할 해제 | `users[target]["role"]` 을 빈 문자열(`""`)로 바꿈. 어떤 역할의 권한도 받지 않게 됨 |
| 역할에서 권한 빼기 | `roles[target]` 권한 리스트에서 그 권한을 지움 |

- 이력 한 건은 여섯 키로 이루어집니다: `time`(회수 시각) · `user` · `permission` · `method` · `approval`(승인 상태) · `result`(「실행」 또는 「대기」).
  - `result` 의 「대기」는 `approval` 이 「승인 대기」라서 실행하지 않았다는 뜻입니다.
- **직접 쓰는 곳은 세 함수**입니다. 판단이 필요한 함수마다 3 ~ 5줄만 쓰고, 나머지는 미리 채웠습니다.
  - `remove_exception`(1 ~ 3번): 번호가 같은 예외를 찾아 지웁니다(`리스트.remove(값)` 은 리스트에서 그 값을 지웁니다).
  - `apply_plan`(4 ~ 8번): 회수 방법별로 실제로 지우는 일(세 곳)입니다.
  - `execute_revocation`(9 ~ 13번): 계획마다 「대기」인지 「실행」인지 정합니다.
- **미리 채운 함수**
  - `save_log`: 이력을 JSON 파일로 저장합니다(판단이 없는 저장이라 미리 채움, 10/23(금)의 `save_requests` 와 같은 방법입니다).
- 회수한 뒤에 다시 판정하면 결과가 달라질 수 있습니다.
  - `execute_revocation` 이 바꾼 `USERS` · `ROLES` · `EXCEPTIONS` 를 `evaluate_access` 도 같은 것으로 읽기 때문입니다.
  - `evaluate_access(사용자, 자원, 행위, 시각)` 는 `(허용 여부, 이유)` 두 값을 리턴합니다(10/22(목)).
- `apply_plan` 은 승인 상태를 보지 않습니다. 승인 상태를 보고 실행할지 정하는 것은 `execute_revocation` 이 하는 일입니다.
- `day05_4-1_run.py` 는 회수 전과 후에 계획마다 `evaluate_access` 로 같은 사용자 · 권한을 판정해 「허용(이유)」 또는 「거부(이유)」 문자열로 비교합니다.

```
+----------------------------------------------------------+
| execute_revocation(plans, users, roles, exceptions, now) |
+----------------------------------------------------------+
   |
   v
+-----------------------------------+
| log = []  (이력을 담을 빈 리스트) |
+-----------------------------------+
   |
   v
+----------------------+
| 계획을 하나씩 꺼낸다 |
+----------------------+
   |
   v
+--------------------------------+
| approval 이 「승인 대기」인가? |
+--------------------------------+
   |
   +--> 그렇다 --> result = "대기"   (아무것도 지우지 않음) --> 아래 「이력 한 건」으로
   |
   v  아니다
+----------------------------------------------------------------+
| apply_plan 으로 실제로 회수한다 (방법별로 지우는 일은 직접 씀) |
+----------------------------------------------------------------+
   |
   v
+-----------------+
| result = "실행" |
+-----------------+
   |
   v
+----------------------------------------------------------+
| 이력 한 건을 만들어 log 에 추가하고 다음 계획으로 (반복) |
+----------------------------------------------------------+
   |
   v  모든 계획을 꺼낸 뒤
log 를 리턴한다
```

> ✍️ **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## ✍️ 문제 4-1 · 회수를 실행하고 전후 판정과 이력 남기기

**📍 이런 상황이 있습니다**

- **지금은**: 회수 계획과 승인 상태만 있고 실제로는 아무것도 지워지지 않았습니다. 지운 뒤에 정말 막혔는지 확인하는 방법도, 지운 기록도 없습니다.
- **그래서 만드는 것**: `execute_revocation` 입니다.
  - 승인 상태가 「승인 대기」인 계획은 실행하지 않고 「대기」로 남기고, 나머지는 `apply_plan` 으로 실행해 「실행」으로 남기고, 이력 리스트를 리턴합니다.
- **실행하면**: 단계 1은 계획별 실행 결과, 단계 2는 회수 전후의 판정 비교, 단계 3은 `revocation_log.json` 저장과 다시 읽은 건수를 출력합니다.
- **현업에서는**: 회수 도구도 실행한 뒤 다시 판정해 막혔는지 확인하고, 이력을 지우지 않고 보관합니다.

**🎯 할 일**

1. `revoke.py` 와 `day05_4-1_run.py` 두 파일을 만들고, `remove_exception` · `apply_plan` · `execute_revocation` 에서 직접 쓰는 곳 다섯 군데를 씁니다.
2. 실행해서 <mark>회수 결과</mark>(단계 1: 실행), <mark>회수 전후의 판정</mark>(단계 2: 확인), <mark>저장한 이력</mark>(단계 3: 저장)을 읽고, 새로 생긴 `revocation_log.json` 파일도 열어 봅니다.

**`revoke.py`**

```python
import json                                                      # JSON 파일을 쓰는 모듈을 불러온다


def remove_exception(exceptions, target_id):                     # 예외 리스트와 지울 예외 번호를 받는 함수
    """예외 리스트에서 번호가 target_id 인 예외를 지운다.
    지웠으면 True, 못 찾았으면 False 를 리턴한다.
    지원이 끝난 예외를 회수할 때 쓴다.
    """
    for exception in exceptions:                                       # 예외를 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 1. exception["id"] 가 target_id 와 같으면 (==)
        # 2.   exceptions 에서 exception 를 지운다 (.remove)
        # 3.   True 를 리턴한다 (지웠다고 알리고 함수를 끝낸다)
    return False                                                 # 끝까지 못 찾았으면 False 를 리턴한다


def apply_plan(plan, users, roles, exceptions):                  # 계획 한 건 · 사용자 · 역할 · 예외 리스트를 받는 함수
    """계획 한 개의 방법대로 프로그램 안의 데이터를 바꾼다.
    승인된 회수를 실행할 때 쓰며, 승인 확인은 부르는 쪽이 한다.
    """
    if plan["method"] == "예외 삭제":                            # 방법이 예외 삭제이면
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 4. remove_exception(exceptions, plan["target"]) 을 호출한다 (예외 리스트에서 그 번호의 예외를 지운다)
    elif plan["method"] == "역할 해제":                          # 방법이 역할 해제이면
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. users[plan["target"]] 를 user_info 에 담는다 (그 사용자의 정보 딕셔너리)
        # 6. user_info["role"] 을 빈 문자열 "" 로 바꾼다 (어떤 역할의 권한도 받지 않게 된다)
    else:                                                        # 방법이 역할에서 권한 빼기이면
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 7. roles[plan["target"]] 를 role_permissions 에 담는다 (그 역할의 권한 리스트)
        # 8. role_permissions 에서 plan["permission"] 을 지운다 (.remove)


def save_log(log, path):                                         # 이력 리스트와 저장할 파일 경로를 받는 함수
    """이력 리스트를 JSON 파일로 저장하고 저장한 개수를 리턴한다(한글은 그대로).
    회수 이력을 나중에 확인할 수 있게 남길 때 쓴다.
    """
    with open(path, "w", encoding="utf-8") as log_file:                 # 파일을 쓰기 모드("w")로 연다
        json.dump(log, log_file, ensure_ascii=False, indent=2)          # 이력을 파일에 JSON 으로 쓴다
    return len(log)                                              # 저장한 건수를 리턴한다


def execute_revocation(plans, users, roles, exceptions, now):    # 계획 · 사용자 · 역할 · 예외 리스트 · 지금 시각 문자열을 받는 함수
    """승인 불필요이거나 승인된 계획만 실행하고 이력 리스트를 리턴한다.
    승인 대기는 「대기」로 남기며, 회수를 집행할 때 쓴다.
    """
    log = []                                                     # 이력을 담을 빈 리스트
    for plan in plans:                                           # 계획을 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 9. plan["approval"] 이 "승인 대기" 이면 (==)
        # 10.  result 를 "대기" 로 정한다
        # 11. 그렇지 않으면 (else)
        # 12.  apply_plan(plan, users, roles, exceptions) 를 호출한다
        # 13.  result 를 "실행" 으로 정한다
        entry = {                                                 # 회수 이력 한 개의 값을 묶는다(여러 줄)
            "time": now,                                         # 시각
            "user": plan["user"],                                # 사용자
            "permission": plan["permission"],                    # 권한
            "method": plan["method"],                            # 회수 방법
            "approval": plan["approval"],                        # 승인 상태
            "result": result,                                    # 결과(실행 또는 대기)
        }
        log.append(entry)                                        # 이력 한 건을 만들어 이력 리스트에 추가한다
    return log                                                   # 이력 리스트를 리턴한다

```

- 직접 쓰는 곳은 세 함수이고, 모두 함수 안이라 앞에 공백 4개를 기본으로 넣습니다(Tab 키 한 번).
  - `remove_exception` 안: 미리 채운 `for` 안쪽이라 1번 `if` 는 8개이고, 그 안쪽(2 · 3번)은 4개 더(12개)입니다.
  - `apply_plan` 안: 미리 채운 `if` · `elif` · `else` 가 4개이고, 그 안쪽 줄(4 ~ 8번)은 4개 더(8개)입니다.
  - `execute_revocation` 안: 미리 채운 `for` 안쪽이라 `if` · `else` 는 8개이고, 그 안쪽은 4개 더(12개)입니다.
  - 나머지 줄은 미리 채워 두었으니 그대로 둡니다.
- 채우기 전에 실행하면 `IndentationError: expected an indented block` 오류가 납니다(파이썬 버전에 따라 뒤에 `after 'if' statement on line …` 가 붙습니다). `remove_exception` 의 `for` 아래에 실행할 줄이 아직 없기 때문입니다.

**`day05_4-1_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 3교시까지의 계획과 승인 상태를 만든 뒤 회수 전 판정을 모으고, `execute_revocation` 으로 회수하고, 회수 후 판정을 모아 비교하고, 이력을 저장합니다.

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from rbac import USERS, ROLES                                    # 10/21(수)에 만든 사용자 · 역할 딕셔너리를 불러온다
from exception_policy import EXCEPTIONS, TIME_FORMAT             # 10/22(목)에 만든 예외 리스트와 시각 형식을 불러온다
from policy import evaluate_access                               # 10/22(목)에 만든 최종 판정 함수를 불러온다
from config_loader import load_json                              # 10/22(목)에 만든 안전한 읽기 함수를 불러온다
from revoke_input import load_to_revoke                          # 어제 점검 결과(회수 대상)를 만드는 함수를 불러온다
from revoke_plan import plan_revocation                          # 2교시에 만든 회수 계획 함수를 불러온다
from revoke_approve import load_sensitive, mark_approvals        # 3교시에 만든 승인 함수를 불러온다
from revoke import execute_revocation, save_log                  # 방금 만든 회수 실행 함수와 이력 저장 함수를 불러온다

NOW_TEXT = "2026-10-30 10:00"                                    # 오늘 오전 실습의 지금 시각 문자열(고정)
NOW = datetime.strptime(NOW_TEXT, TIME_FORMAT)                   # 같은 시각을 시각으로 바꾼다. 판정 함수가 쓴다
DECISIONS = {"dami:SALES:QUERY": "승인", "dami:SALES:CHANGE": "승인"}  # 보안 책임자의 결정(3교시와 같다)

to_revoke = load_to_revoke()                                     # 어제 점검한 회수 대상을 만든다
plans = plan_revocation(to_revoke, USERS, ROLES)                 # 회수 계획을 세운다
sensitive = load_sensitive("config/sensitive.json")              # 민감한 권한 리스트를 읽는다
plans = mark_approvals(plans, sensitive, DECISIONS)              # 계획마다 승인 상태를 적는다

def judge(plan):                                                 # 계획 한 건을 받는 함수
    """계획의 사용자 · 권한을 지금 판정해 「허용(이유)」 또는 「거부(이유)」 문자열을 리턴한다.
    회수 전후의 판정을 비교할 때 쓴다.
    """
    resource, action = plan["permission"].split(":")             # "SALES:QUERY" 를 자원과 행위로 나눈다
    is_allowed, reason = evaluate_access(plan["user"], resource, action, NOW)  # 최종 판정을 한다
    if is_allowed:                                                       # 허용이면
        return "허용(" + reason + ")"                            # 허용과 이유를 하나의 문자열로 합친다
    return "거부(" + reason + ")"                                # 거부와 이유를 하나의 문자열로 합친다


def judge_all(plans):                                            # 계획 리스트를 받는 함수
    """계획마다 judge 로 판정한 문자열을 같은 순서의 리스트로 리턴한다.
    회수 전후의 판정을 한꺼번에 비교할 때 쓴다.
    """
    results = []                                                 # 판정을 담을 빈 리스트
    for plan in plans:                                           # 계획을 하나씩 꺼낸다
        verdict = judge(plan)                                    # 계획 한 건을 판정한다
        results.append(verdict)                                  # 판정해서 추가한다
    return results                                               # 판정 리스트를 리턴한다


before = judge_all(plans)                                        # 회수하기 전의 판정을 모두 구해 둔다
log = execute_revocation(plans, USERS, ROLES, EXCEPTIONS, NOW_TEXT)  # 회수를 실행한다
after = judge_all(plans)                                         # 회수한 뒤의 판정을 모두 구한다

print("--- 단계 1: 실행 - 회수 결과")                            # 단계 1 시작을 알리는 줄
executed_count = 0                                                         # 실행한 건수를 0 으로 시작한다
for entry in log:                                                # 이력을 하나씩 꺼낸다
    print(entry["user"], entry["permission"], "|", entry["method"], "|", entry["result"])  # 사용자 · 권한 | 방법 | 결과를 출력한다
    if entry["result"] == "실행":                                # 실행한 건이면
        executed_count = executed_count + 1                                          # 건수를 1 늘린다
print("실행", executed_count, "건, 대기", len(log) - executed_count, "건")           # 실행과 대기 건수를 출력한다

print("--- 단계 2: 확인 - 회수 전후의 판정")                     # 단계 2 시작을 알리는 줄
plan_count = len(plans)                                          # 개수를 먼저 구한다
for index in range(plan_count):                                  # 번호 index 로 회수 전 리스트와 회수 후 리스트를 짝지어 꺼낸다
    mark = "그대로"                                              # 표시를 그대로로 시작한다
    if before[index] != after[index]:                                    # 회수 전후의 판정이 다르면
        mark = "바뀜"                                            # 바뀜으로 고친다
    print(plans[index]["user"], plans[index]["permission"], "|", before[index], "->", after[index], "|", mark)  # 전후 판정과 표시를 출력한다

print("--- 단계 3: 저장 - 회수 이력")                            # 단계 3 시작을 알리는 줄
count = save_log(log, "revocation_log.json")                     # 이력을 파일로 저장한다
saved = load_json("revocation_log.json", [])                     # 저장한 파일을 다시 읽어
print("저장", count, "건, 다시 읽은 건수", len(saved), "건, 첫 이력:", saved[0]["user"], saved[0]["permission"], saved[0]["result"])  # 건수와 첫 이력을 출력한다
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `revoke.py` · `day05_4-1_run.py` 를 만들어 위 코드를 붙여 넣습니다. 만드는 법은 둘 중 하나를 고릅니다.
   - VS Code: `access_control` 폴더를 선택하고 **새 파일**(New File) 아이콘을 눌러 이름을 입력합니다.
   - 터미널: `pwd` 로 `access_control` 인지 확인하고 `touch 이름` 으로 만든 뒤 VS Code 에서 열어 붙여 넣습니다(`vim 이름` → `i` → 붙여넣기 → `Esc` → `:wq` 도 됩니다).
2. **[VS Code]** `revoke.py` 에서 `remove_exception` · `apply_plan` · `execute_revocation` 의 직접 쓰는 곳 다섯 군데를 씁니다. 4.1 의 표와 그림을 보고 씁니다.
3. **[터미널]** `pwd` 의 결과가 `access_control` 로 끝나는지 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python day05_4-1_run.py
   ```
4. 출력은 세 단계입니다. 단계 1은 계획 여덟 줄과 `실행 N 건, 대기 N 건`, 단계 2는 판정 비교 여덟 줄, 단계 3은 저장 한 줄입니다.
5. **[VS Code]** 왼쪽 목록에 새로 생긴 `revocation_log.json` 을 열어 한글이 그대로 저장됐는지 봅니다.
6. **[보고서]** `day05_am_report.md` 의 `## 4교시` › `### 문제 4-1` 아래를 채웁니다.
   - (가) 출력 전체를 붙여 넣고, 이력의 결과가 「실행」인 건수와 「대기」인 건수, 회수 전후 판정이 바뀐 권한, 저장한 이력 건수를 적어 주세요.
   - (나) 🔍 회수를 실행한 7건 가운데 회수 전후 판정이 바뀐 것은 일부입니다. 바뀌지 않은 권한이 그대로인 이유와, 그래도 회수하고 이력을 남기는 이유를 적어 주세요.
   - (다) 🔍 회수 이력에는 시각 · 사용자 · 권한 · 방법 · 승인 상태 · 결과가 들어 있습니다. 반년 뒤 감사(점검 기록을 검토받는 일)에서 「이 권한이 왜 없어졌나요?」라고 물으면 이 이력만으로 답할 수 있을까요? 이력에 없는 정보가 있다면 무엇인지, 어떤 키를 추가하면 되는지 적어 주세요.

## 4교시 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 아직 승인을 기다리는 계획인지 | `if plan["approval"] == "승인 대기":` |
| 실제로 회수하기 | `apply_plan(plan, users, roles, exceptions)` (방법별로 지우는 일은 `apply_plan` 안에서 직접 씀) |
| 번호가 같은 예외 찾기 | `if exception["id"] == target_id:` → `exceptions.remove(exception)` → `return True` (`remove_exception` 안) |
| 예외 삭제 | `remove_exception(exceptions, plan["target"])` |
| 역할 해제 | `user_info = users[plan["target"]]` → `user_info["role"] = ""` |
| 역할에서 권한 빼기 | `role_permissions = roles[plan["target"]]` → `role_permissions.remove(plan["permission"])` |
| 이력 한 건 | `{"time": now, "user": …, "result": result}` 딕셔너리를 `log.append(…)` |

---

## 오전 마무리 — 보고서 2 · 3 · 4교시 칸 확인

`day05_am_report.md` 의 2 · 3 · 4교시 칸에서 `답:` 뒤가 비어 있는 질문이 없는지 봅니다. `access_control` 폴더에 오늘 만든 파일이 있는지 확인합니다.

```bash
ls
ls config
```

- `revoke_input.py` · `revoke_plan.py` · `revoke_approve.py` · `revoke.py` · `day05_2-1_run.py` · `day05_3-1_run.py` · `day05_4-1_run.py` · `revocation_log.json` 이 보여야 합니다.
  - `config` 안에는 `sensitive.json` 이 새로 보여야 합니다.

오후에는 회수한 뒤에도 조건을 따져 접근을 판단하는 **조건기반 정책**과 판정 함수를 서버로 여는 수업을 합니다. 올리기(git)는 오후 6교시 마지막에 한 번에 합니다.

---

<!-- learn:answers -->
