---
id: m3-u04-l03
title: 실습 4-2 · 회수 실행하고 이력 남기기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/090_day05_am_revoke.md
  mission_id: GichanSource.m3-1030-am-revoke
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 4-2 · 회수 실행하고 이력 남기기

## 목표: 회수 실행과 회수 이력

> **이번 실습에 들어온 일**
>
> A사 관제 담당이 보낸 메시지:
> 「승인이 필요 없거나 승인된 것만 실제로 회수하고, 회수한 내용을 이력 파일로 남겨 주세요. 아직 승인되지 않은 것은 실행하지 말고 「대기」로 남겨 주세요.
>
> 회수한 뒤에는 같은 사용자 · 권한으로 접근을 다시 판정해서 정말 막혔는지 확인해 주세요. 회수했다고 적어 놓고 여전히 접근이 허용되면 안 됩니다.」
> - **왜 중요한가**: 회수했다는 기록만으로는 부족합니다. 다시 판정해 보아야 정말 막혔는지 알 수 있고, 이력이 있어야 나중에 누가 언제 왜 없앴는지 설명할 수 있습니다.

## 왜 전후 판정과 이력이 필요한가

1. 승인 상태까지 정해진 계획을 이제 실행합니다. 승인 상태가 「승인 불필요」 또는 「승인됨」인 계획만 실행하고, 「승인 대기」인 계획은 실행하지 않습니다.
2. 실행한 뒤에는 **같은 사용자 · 권한을 다시 판정**합니다. Unit 1의 `evaluate_access` 가 회수 전과 후에 같은 요청을 어떻게 판정하는지 비교하면 회수가 정말 효과가 있었는지 알 수 있습니다.
3. 실행한 내용은 **회수 이력**(`revocation_log.json`)으로 남깁니다. Unit 3의 「사용 이력」(권한을 마지막으로 쓴 시각의 기록)과 다른 것입니다. 회수 이력은 이번 Unit에서 무엇을 회수했는지의 기록입니다.

## 3.1 실행 방법과 이력

| 방법 | 실제로 하는 일 |
|---|---|
| 예외 삭제 | 예외 리스트(`EXCEPTIONS`)에서 번호가 `target` 인 예외 한 건을 지움 |
| 역할 해제 | `users[target]["role"]` 을 빈 문자열(`""`)로 바꿈. 어떤 역할의 권한도 받지 않게 됨 |
| 역할에서 권한 빼기 | `roles[target]` 권한 리스트에서 그 권한을 지움 |

- 이력 한 건은 여섯 키로 이루어집니다: `time`(회수 시각) · `user` · `permission` · `method` · `approval`(승인 상태) · `result`(「실행」 또는 「대기」).
  - `result` 의 「대기」는 `approval` 이 「승인 대기」라서 실행하지 않았다는 뜻입니다.
- 직접 쓰는 부분은 두 곳입니다. ①은 아직 승인 대기인지 가려내고, ②는 그 밖의 계획을 실행합니다.
- `apply_plan`은 회수 방법에 따라 역할을 해제하거나 권한 또는 예외를 지웁니다. `save_log`는 이력을 JSON으로 저장합니다.
- 회수한 뒤에 다시 판정하면 결과가 달라질 수 있습니다.
  - `execute_revocation` 이 바꾼 `USERS` · `ROLES` · `EXCEPTIONS` 를 `evaluate_access` 도 같은 것으로 읽기 때문입니다.
  - `evaluate_access(사용자, 자원, 행위, 시각)` 는 `(허용 여부, 이유)` 두 값을 리턴합니다(Unit 1).
- `apply_plan` 은 승인 상태를 보지 않습니다. 승인 상태를 보고 실행할지 정하는 것은 `execute_revocation` 이 하는 일입니다.
- `exercise4-2_run.py` 는 회수 전과 후에 계획마다 `evaluate_access` 로 같은 사용자 · 권한을 판정해 「허용(이유)」 또는 「거부(이유)」 문자열로 비교합니다.

<figure class="page-figure"><img src="assets/f01.svg" alt="execute_revocation 은 승인 대기면 그대로 두고 아니면 회수한 뒤 계획마다 이력을 남긴다"></figure>

## 실습 4-2 · 회수 실행 후 판정과 이력 남기기

**이런 상황이 있습니다**

- **지금은**: 회수 계획과 승인 상태만 있고 실제로는 아무것도 지워지지 않았습니다. 지운 뒤에 정말 막혔는지 확인하는 방법도, 지운 기록도 없습니다.
- **그래서 만드는 것**: `execute_revocation` 입니다.
  - 승인 상태가 「승인 대기」인 계획은 실행하지 않고 「대기」로 남깁니다.
  - 나머지 계획은 `apply_plan` 으로 실행하고 「실행」으로 남깁니다.
  - 마지막에 이력 리스트를 리턴합니다.
- **실행하면**: 단계 1은 계획별 실행 결과, 단계 2는 회수 전후의 판정 비교, 단계 3은 `revocation_log.json` 저장과 다시 읽은 건수를 출력합니다.
- **현업에서는**: 회수 도구도 실행한 뒤 다시 판정해 막혔는지 확인하고, 이력을 지우지 않고 보관합니다.

**할 일**

1. `revoke.py`와 `exercise4-2_run.py`를 만들고 `revoke.py`의 ①·②를 채웁니다.
2. 실행해서 <mark>회수 결과</mark>(단계 1: 실행), <mark>회수 전후의 판정</mark>(단계 2: 확인), <mark>저장한 이력</mark>(단계 3: 저장)을 읽고, 새로 생긴 `revocation_log.json` 파일도 열어 봅니다.

**`revoke.py`**

```python
import json


def remove_exception(exceptions, target_id):
    """예외 리스트에서 번호가 target_id 인 예외를 지운다.
    지웠으면 True, 못 찾았으면 False 를 리턴한다.
    지원이 끝난 예외를 회수할 때 쓴다.
    """
    for exception in exceptions:
        if exception["id"] == target_id:
            exceptions.remove(exception)
            return True
    return False


def apply_plan(plan, users, roles, exceptions):
    """계획 한 개의 방법대로 프로그램 안의 데이터를 바꾼다.
    승인된 회수를 실행할 때 쓰며, 승인 확인은 부르는 쪽이 한다.
    """
    if plan["method"] == "예외 삭제":
        remove_exception(exceptions, plan["target"])
    elif plan["method"] == "역할 해제":
        user_info = users[plan["target"]]
        user_info["role"] = ""
    else:
        role_permissions = roles[plan["target"]]
        role_permissions.remove(plan["permission"])


def save_log(log, path):
    """이력 리스트를 JSON 파일로 저장하고 저장한 개수를 리턴한다(한글은 그대로).
    회수 이력을 나중에 확인할 수 있게 남길 때 쓴다.
    """
    with open(path, "w", encoding="utf-8") as log_file:
        json.dump(log, log_file, ensure_ascii=False, indent=2)
    return len(log)


def execute_revocation(plans, users, roles, exceptions, now):
    """승인 불필요이거나 승인된 계획만 실행하고 이력 리스트를 리턴한다.
    승인 대기는 「대기」로 남기며, 회수를 집행할 때 쓴다.
    """
    log = []
    for plan in plans:
        # ① True를 승인 상태가 대기인지 확인하는 조건으로 바꿉니다.
        if True:
            result = "대기"
        else:
            # ② 이 줄을 실제 회수 함수 호출로 바꿉니다.
            raise NotImplementedError("② 회수 함수 호출을 채워 주세요.")
            result = "실행"
        entry = {
            "time": now,
            "user": plan["user"],
            "permission": plan["permission"],
            "method": plan["method"],
            "approval": plan["approval"],
            "result": result,
        }
        log.append(entry)
    return log

```

- ①에서는 `if True:`의 `True`를 바꿉니다. `plan["approval"]`이 `"승인 대기"`와 같은지 `==`로 확인합니다.
- ②에서는 `raise` 줄 전체를 함수 호출 한 줄로 바꿉니다. 위에 있는 `apply_plan`에 `plan`, `users`, `roles`, `exceptions`를 차례로 넘깁니다.
- 시작 코드 그대로 실행하면 수업용 계획은 모두 대기로 남습니다. ①만 채우면 실행할 계획에서 ②를 채우라는 메시지가 나옵니다. 두 곳을 다 채우면 **실행 7건, 대기 1건**, 이력 **8건**이 나옵니다.

**`exercise4-2_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 실습 4-1까지의 계획과 승인 상태를 만든 뒤 회수 전 판정을 모으고, `execute_revocation` 으로 회수하고, 회수 후 판정을 모아 비교하고, 이력을 저장합니다.

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from rbac import USERS, ROLES                                    # Unit 1에서 만든 사용자 · 역할 딕셔너리를 불러온다
from exception_policy import EXCEPTIONS, TIME_FORMAT             # Unit 1에서 만든 예외 리스트와 시각 형식을 불러온다
from policy import evaluate_access                               # Unit 1에서 만든 최종 판정 함수를 불러온다
from config_loader import load_json                              # Unit 1에서 만든 안전한 읽기 함수를 불러온다
from revoke_input import load_to_revoke                          # Unit 3의 점검 결과(회수 대상)를 만드는 함수를 불러온다
from revoke_plan import plan_revocation                          # 준비 Lesson에서 만든 회수 계획 함수를 불러온다
from revoke_approve import load_sensitive, mark_approvals        # 실습 4-1에서 만든 승인 함수를 불러온다
from revoke import execute_revocation, save_log                  # 방금 만든 회수 실행 함수와 이력 저장 함수를 불러온다

NOW_TEXT = "2026-10-30 10:00"                                    # 이번 실습의 지금 시각 문자열(고정)
NOW = datetime.strptime(NOW_TEXT, TIME_FORMAT)                   # 같은 시각을 시각으로 바꾼다. 판정 함수가 쓴다
DECISIONS = {"dami:SALES:QUERY": "승인", "dami:SALES:CHANGE": "승인"}  # 보안 책임자의 결정(실습 4-1와 같다)

to_revoke = load_to_revoke()                                     # Unit 3에서 점검한 회수 대상을 만든다
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

1. **[VS Code]** 파일 `revoke.py` · `exercise4-2_run.py` 를 만들어 위 코드를 붙여 넣습니다. 
   - VS Code: `access_control` 폴더를 선택하고 **새 파일**(New File) 아이콘을 눌러 이름을 입력합니다.
2. **[VS Code]** `revoke.py`의 ①·②를 채웁니다. 3.1의 표와 그림을 참고합니다.
3. **[터미널]** `pwd` 의 결과가 `access_control` 로 끝나는지 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise4-2_run.py
   ```
4. 출력은 세 단계입니다. 단계 1은 계획 여덟 줄과 `실행 N 건, 대기 N 건`, 단계 2는 판정 비교 여덟 줄, 단계 3은 저장 한 줄입니다.
5. **[VS Code]** 왼쪽 목록에 새로 생긴 `revocation_log.json` 을 열어 한글이 그대로 저장됐는지 봅니다.
6. **핵심 작업 기록**: 실습 4-1과 4-2의 결과를 「문제 해결 과정을 블로그에 기록하기」에서 함께 정리합니다.


<!-- answer: 08|실습 4-2 정답 -->

## 실습 4-2 정리

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

<!-- learn:answers -->
