---
id: m3-u08-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/090_day05_am_revoke.md
  mission_id: GichanSource.m3-1030-am-revoke
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답을 보는 방법

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## Exercise 8-1 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise8-1_run.py
```

**채운 코드** (한 예) — 직접 쓰는 곳은 네 함수의 다섯 군데입니다.

① `exception_id` 안(미리 채운 첫 줄 아래)

```python
    number_text = number_text.replace("번", "")                   # "번" 을 지워 "3" 으로 만든다
    return int(number_text)                                      # 문자열 "3" 을 숫자 3 으로 바꿔 리턴한다
```

② `count_users_by_role` 안(미리 채운 `role` 줄 아래)

```python
        old_count = counts.get(role, 0)                          # 그 역할의 지금까지 센 수(처음이면 0)
        counts[role] = old_count + 1                             # 1 늘려서 다시 적는다
```

③ `build_plan` 안(`if method == "역할 해제":` 아래)

```python
        role_permissions = roles[info["role"]]                   # 그 사용자의 역할에 든 권한 리스트
        impact = len(role_permissions)                           # 영향은 그 역할에 든 권한 수
```

④ `build_plan` 안(마지막 `return` 위)

```python
    impact = role_counts[info["role"]]                           # 역할에서 권한 빼기: 영향은 그 역할을 가진 사용자 수(각자 그 권한 1건을 잃는다)
```

⑤ `plan_revocation` 안(미리 채운 `info` 줄 아래)

```python
        if "예외" in finding["source"]:                          # 예외로 받은 권한이면
            method = "예외 삭제"                                 # 그 예외를 지운다
        elif not info["employed"]:                               # 퇴사한 사용자의 역할 권한이면
            method = "역할 해제"                                 # 그 사용자의 역할을 해제한다
        else:                                                    # 재직 중인 사용자의 역할 권한이면
            method = "역할에서 권한 빼기"                        # 역할에서 그 권한을 뺀다
```

**결과**

- (가) 출력은 다음과 같고, 방법별 건수는 예외 삭제 **5건** · 역할 해제 **2건** · 역할에서 권한 빼기 **1건**입니다.
  - 역할별 사용자 수는 `finance` **1명**(junho) · `sales` **2명**(seoyeon · dami)입니다.

```
--- 단계 1: 계획 - 회수 대상 8 건의 회수 방법
junho SALES:QUERY <- 역할 finance | 역할에서 권한 빼기 | 영향 1 건
dami SALES:QUERY <- 역할 sales | 역할 해제 | 영향 2 건
dami SALES:CHANGE <- 역할 sales | 역할 해제 | 영향 2 건
seoyeon SETTLE:QUERY <- 예외 1번 | 예외 삭제 | 영향 1 건
junho SALES:CHANGE <- 예외 2번 | 예외 삭제 | 영향 1 건
dami SALES:QUERY <- 예외 3번 | 예외 삭제 | 영향 1 건
batch-night SALES:QUERY <- 예외 4번 | 예외 삭제 | 영향 1 건
gaeun SETTLE:QUERY <- 예외 5번 | 예외 삭제 | 영향 1 건
--- 단계 2: 집계 - 방법별 건수
{'역할에서 권한 빼기': 1, '역할 해제': 2, '예외 삭제': 5}
--- 단계 3: 확인 - 역할별 사용자 수와 이름
finance 1 명 ['junho']
sales 2 명 ['seoyeon', 'dami']
```

- (나) `sales` 역할에서 `SALES:QUERY` 를 뺐다면 `sales` 역할을 가진 **seoyeon 과 dami 두 사람**이 모두 그 권한을 잃습니다(단계 3의 `sales` 2명, 퇴사한 dami 도 센 수입니다). dami 는 퇴사했으니 문제가 없어도 seoyeon 은 지금도 일하는 사람이라 영업 조회 업무가 멈춥니다.
  - 그래서 퇴사한 dami 는 역할 자체는 그대로 두고 dami 의 `role` 만 해제하는 「역할 해제」로 정합니다.
  - dami 1명이 영향을 받고, 사라지는 권한은 2건(영향 2건)입니다.
- (다) 계획을 먼저 리스트로 만들어 보면 좋은 점이 셋 있습니다. ① 지우기 전에 방법이 맞는지, 영향받는 사람이 누구인지 사람이 확인할 수 있습니다. ② 계획 단계에서는 잘못된 방법을 고칠 수 있습니다. ③ 계획 리스트가 승인과 이력의 근거가 됩니다.
  - 실제 서비스에서는 한 번 지우면 되돌리기 어렵다는 점도 계획을 먼저 확인하는 이유입니다.
  - dami 3건을 처리하는 작업의 종류는 **두 가지**입니다.
  - 계획은 3건이지만 역할 해제 2건은 같은 변경이라 종류로는 하나입니다.
  - dami 의 `role` 을 비우는 역할 해제 한 번이 역할로 받은 두 건(`SALES:QUERY` · `SALES:CHANGE`)을 함께 처리하고, 예외 3번 삭제가 한 번입니다.
  - 코드는 계획 3건을 차례로 실행하므로 역할 해제를 두 번 하지만, 같은 값을 다시 쓰는 것이라 결과는 같습니다.

**왜**

- 회수는 되돌리기 어려운 변경이라 지우기 전에 방법과 영향을 먼저 표로 확인합니다.
  - 같은 8건이라도 방법에 따라 영향받는 사람이 1명일 수도, 여러 명일 수도 있습니다.
  - 퇴사자는 역할 정의가 아니라 그 사람의 `role` 만 해제하므로 같은 역할의 재직자에게 영향이 없습니다.

**자주 틀리는 곳**

- `elif not info["employed"]` 검사를 `"예외"` 검사보다 먼저 쓰면, 퇴사한 dami 의 예외 3번이 「예외 삭제」가 아니라 「역할 해제」로 계획됩니다.
  - 오류는 나지 않고 숫자만 달라집니다.
  - 실행하면 다음처럼 됩니다(예외 3번 권한이 「역할 해제」로 나오고 방법별 건수가 예외 삭제 4건 · 역할 해제 3건이면 이 실수입니다).

```
--- 단계 1: 계획 - 회수 대상 8 건의 회수 방법
junho SALES:QUERY <- 역할 finance | 역할에서 권한 빼기 | 영향 1 건
dami SALES:QUERY <- 역할 sales | 역할 해제 | 영향 2 건
dami SALES:CHANGE <- 역할 sales | 역할 해제 | 영향 2 건
seoyeon SETTLE:QUERY <- 예외 1번 | 예외 삭제 | 영향 1 건
junho SALES:CHANGE <- 예외 2번 | 예외 삭제 | 영향 1 건
dami SALES:QUERY <- 예외 3번 | 역할 해제 | 영향 2 건
batch-night SALES:QUERY <- 예외 4번 | 예외 삭제 | 영향 1 건
gaeun SETTLE:QUERY <- 예외 5번 | 예외 삭제 | 영향 1 건
--- 단계 2: 집계 - 방법별 건수
{'역할에서 권한 빼기': 1, '역할 해제': 3, '예외 삭제': 4}
--- 단계 3: 확인 - 역할별 사용자 수와 이름
finance 1 명 ['junho']
sales 2 명 ['seoyeon', 'dami']
```

**관제에서는**

- 회수 도구는 실제로 지우기 전에 계획(드라이 런)을 만들어 담당자에게 보여 주고, 한 번에 권한이 여러 개 사라지는 변경은 따로 확인합니다.

---

## Exercise 8-2 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise8-2_run.py
```

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `plan_key` 안(미리 채운 `permission` 줄 아래)

```python
    return f"{user}:{permission}"                                # 사용자와 권한을 : 로 이어 붙인다
```

② `needs_approval` 안

```python
    is_sensitive = plan["permission"] in sensitive               # 권한이 민감한 권한 리스트에 있는지(True 또는 False)
    is_big_impact = plan["impact"] >= 2                          # 영향이 2건 이상인지(True 또는 False)
    return is_sensitive or is_big_impact                         # 둘 중 하나라도 참이면 True 를 리턴한다
```

③ `mark_approvals` 안(미리 채운 `needs` 줄 아래)

```python
        if not needs:                                            # 승인이 필요하지 않으면
            item["approval"] = "승인 불필요"                     # 바로 회수할 수 있다
        elif decision == "승인":                                  # 승인이 필요한데 보안 책임자가 승인했으면
            item["approval"] = "승인됨"                          # 회수할 수 있다
        else:                                                    # 승인이 필요한데 아직 결정이 없으면
            item["approval"] = "승인 대기"                       # 결정이 날 때까지 기다린다
```

**결과**

- (가) 출력은 다음과 같고, 승인 불필요 **5건** · 승인됨 **2건** · 승인 대기 **1건**입니다.
  - 승인이 필요한 계획은 3건(dami 의 역할 해제 두 건과 junho 의 `SALES:CHANGE` 예외 2번)이고, 그중 dami 의 두 건은 보안 책임자가 승인하기로 결정해서 「승인됨」, junho 의 예외 2번은 결정이 없어서 「승인 대기」입니다.

```
--- 단계 1: 승인 상태 - 계획 8건
junho SALES:QUERY <- 역할 finance | 역할에서 권한 빼기 | 영향 1 건 | 승인 불필요
dami SALES:QUERY <- 역할 sales | 역할 해제 | 영향 2 건 | 승인됨
dami SALES:CHANGE <- 역할 sales | 역할 해제 | 영향 2 건 | 승인됨
seoyeon SETTLE:QUERY <- 예외 1번 | 예외 삭제 | 영향 1 건 | 승인 불필요
junho SALES:CHANGE <- 예외 2번 | 예외 삭제 | 영향 1 건 | 승인 대기
dami SALES:QUERY <- 예외 3번 | 예외 삭제 | 영향 1 건 | 승인 불필요
batch-night SALES:QUERY <- 예외 4번 | 예외 삭제 | 영향 1 건 | 승인 불필요
gaeun SETTLE:QUERY <- 예외 5번 | 예외 삭제 | 영향 1 건 | 승인 불필요
--- 단계 2: 집계 - 승인 상태별 건수
{'승인 불필요': 5, '승인됨': 2, '승인 대기': 1}
```

- (나) 민감한 권한(쓰기 권한)과, 한 번의 회수로 권한이 여러 개 사라지는 회수는 잘못되면 그 권한으로 일하던 사람의 업무가 멈추고 피해가 큽니다.
  - 한 사람이 혼자 정하면 실수나 잘못된 사용이 생길 수 있어서, 다른 사람(보안 책임자)이 이유를 확인하고 승인하게 합니다.
  - 반면 조회 같은 일반 권한 한 건은 영향이 작고, 필요하면 다시 요청해서 받을 수 있어 되돌리기 쉽습니다.
  - 예를 들어 junho 의 `SALES:QUERY` 는 재직자의 권한이지만 마지막 사용이 90일보다 오래됐다고 Unit 7의 점검에서 나왔고 영향이 1건이라 승인 없이 회수합니다.
- (다) Exercise 8-3에서 junho 의 `SALES:CHANGE`(예외 2번) 계획은 실행하지 않고 「대기」로 남습니다.
  - 승인이 오래 나지 않으면 이 예외가 정리되지 않은 채 남아 점검에 계속 나오고 담당자가 같은 계획을 거듭 확인해야 합니다.
  - 그 예외는 이미 만료되어 접근은 막혀 있지만, 만료 시각이 고쳐지는 등의 일이 생기면 다시 쓰일 수 있어 오래 두면 위험합니다.

**왜**

- 쓰기 같은 중요한 권한과, 한 번의 회수로 권한이 여러 개 사라지는 회수는 한 사람이 혼자 정하지 않고 승인을 받습니다.
  - 승인 상태를 계획마다 적어 두면 Exercise 8-3이 「승인 대기」인 계획만 빼고 실행할 수 있습니다.
  - 같은 사용자의 역할 해제 두 건(dami)은 같은 변경(`role` 비우기)이므로 함께 결정해야 합니다.
  - 코드는 이를 막지 않으므로, 한쪽만 승인하면 승인받지 않은 권한까지 함께 없어집니다.

**자주 틀리는 곳**

- 보안 책임자의 결정을 확인하는 `elif decision == "승인":` 줄을 빼먹으면, 승인하기로 한 dami 의 두 건도 「승인 대기」로 나옵니다.
  - 오류는 나지 않고 상태만 달라집니다.
  - 실행하면 다음처럼 됩니다(「승인됨」이 하나도 없고 「승인 대기」가 3건이면 이 실수입니다).

```
--- 단계 1: 승인 상태 - 계획 8건
junho SALES:QUERY <- 역할 finance | 역할에서 권한 빼기 | 영향 1 건 | 승인 불필요
dami SALES:QUERY <- 역할 sales | 역할 해제 | 영향 2 건 | 승인 대기
dami SALES:CHANGE <- 역할 sales | 역할 해제 | 영향 2 건 | 승인 대기
seoyeon SETTLE:QUERY <- 예외 1번 | 예외 삭제 | 영향 1 건 | 승인 불필요
junho SALES:CHANGE <- 예외 2번 | 예외 삭제 | 영향 1 건 | 승인 대기
dami SALES:QUERY <- 예외 3번 | 예외 삭제 | 영향 1 건 | 승인 불필요
batch-night SALES:QUERY <- 예외 4번 | 예외 삭제 | 영향 1 건 | 승인 불필요
gaeun SETTLE:QUERY <- 예외 5번 | 예외 삭제 | 영향 1 건 | 승인 불필요
--- 단계 2: 집계 - 승인 상태별 건수
{'승인 불필요': 5, '승인 대기': 3}
```

**관제에서는**

- 승인 대기 중인 계획에는 처리 기한을 정해 두고, 넘으면 담당자에게 알립니다.
  - 승인한 사람과 요청한 사람은 달라야 합니다.

---

## Exercise 8-3 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise8-3_run.py
```

**채운 코드** (한 예) — 직접 쓰는 곳은 `remove_exception` 의 한 곳, `apply_plan` 의 세 곳, `execute_revocation` 의 한 곳입니다.

① `remove_exception` 안(미리 채운 `for` 아래)

```python
        if exception["id"] == target_id:                               # 번호가 같으면
            exceptions.remove(exception)                               # 리스트에서 그 예외를 지운다
            return True                                          # 지웠다고 알리고 함수를 끝낸다
```

② `apply_plan` 안(미리 채운 `if` 아래)

```python
        remove_exception(exceptions, plan["target"])             # 예외 리스트에서 그 번호의 예외를 지운다
```

③ `apply_plan` 안(미리 채운 `elif` 아래)

```python
        user_info = users[plan["target"]]                        # 그 사용자의 정보 딕셔너리를 꺼낸다
        user_info["role"] = ""                                   # 역할을 빈 문자열로 바꾼다(어떤 역할의 권한도 받지 않게 된다)
```

④ `apply_plan` 안(미리 채운 `else` 아래)

```python
        role_permissions = roles[plan["target"]]                 # 그 역할의 권한 리스트를 꺼낸다
        role_permissions.remove(plan["permission"])              # 그 리스트에서 그 권한을 지운다
```

⑤ `execute_revocation` 안(미리 채운 `for` 아래)

```python
        if plan["approval"] == "승인 대기":                      # 승인을 기다리는 계획이면
            result = "대기"                                      # 실행하지 않고 대기로 남긴다
        else:                                                    # 승인 불필요이거나 승인됨이면
            apply_plan(plan, users, roles, exceptions)           # 실제로 회수한다
            result = "실행"                                      # 실행했다고 남긴다
```

**결과**

- (가) 출력은 다음과 같고, **실행 7건 · 대기 1건**입니다.
  - 대기는 아직 승인되지 않은 junho 의 `SALES:CHANGE`(예외 2번)입니다.
  - 판정이 바뀐 것은 **junho 의 `SALES:QUERY` 1건**(허용 → 거부)이고, 저장한 이력은 **8건**입니다.

```
--- 단계 1: 실행 - 회수 결과
junho SALES:QUERY | 역할에서 권한 빼기 | 실행
dami SALES:QUERY | 역할 해제 | 실행
dami SALES:CHANGE | 역할 해제 | 실행
seoyeon SETTLE:QUERY | 예외 삭제 | 실행
junho SALES:CHANGE | 예외 삭제 | 대기
dami SALES:QUERY | 예외 삭제 | 실행
batch-night SALES:QUERY | 예외 삭제 | 실행
gaeun SETTLE:QUERY | 예외 삭제 | 실행
실행 7 건, 대기 1 건
--- 단계 2: 확인 - 회수 전후의 판정
junho SALES:QUERY | 허용(역할 권한) -> 거부(권한 없음) | 바뀜
dami SALES:QUERY | 거부(퇴사한 계정) -> 거부(퇴사한 계정) | 그대로
dami SALES:CHANGE | 거부(퇴사한 계정) -> 거부(퇴사한 계정) | 그대로
seoyeon SETTLE:QUERY | 거부(권한 없음) -> 거부(권한 없음) | 그대로
junho SALES:CHANGE | 거부(권한 없음) -> 거부(권한 없음) | 그대로
dami SALES:QUERY | 거부(퇴사한 계정) -> 거부(퇴사한 계정) | 그대로
batch-night SALES:QUERY | 거부(권한 없음) -> 거부(권한 없음) | 그대로
gaeun SETTLE:QUERY | 거부(권한 없음) -> 거부(권한 없음) | 그대로
--- 단계 3: 저장 - 회수 이력
저장 8 건, 다시 읽은 건수 8 건, 첫 이력: junho SALES:QUERY 실행
```

- (나) 실행한 7건 가운데 나머지 6건은 회수 전에도 이미 거부였습니다. 퇴사한 계정(dami 세 건)은 사용자 파일의 재직 표시 때문에, 예외 세 건(seoyeon 1번 · batch-night 4번 · gaeun 5번)은 만료 시각이 지난 예외라 출력에서도 거부(권한 없음)로 나옵니다. 그래도 회수하고 이력을 남기는 이유는 세 가지입니다.
  - ① 데이터에 남아 있으면 퇴사자의 재직 표시가 잘못 바뀌거나 예외 만료 시각이 고쳐질 때 다시 허용될 수 있습니다.
  - ② 점검에 같은 권한이 계속 나와 담당자가 거듭 확인해야 합니다.
  - ③ 정리하지 않은 권한이 남아 있으면 감사에서 문제가 됩니다.
  - 실제로 위험을 줄인 것은 허용되던 junho 의 `SALES:QUERY` 한 건입니다.
- (다) 이 이력만으로는 부족합니다.
  - 「이 권한이 왜 없어졌나요?」에 답하려면 ① 회수 이유(퇴사 · 만료 · 90일 미사용 중 무엇 때문인지. Unit 7의 점검 결과의 `reasons` 키에 적혀 있습니다) ② 승인한 사람의 이름 ③ 승인한 시각이 있어야 합니다.
  - 지금 이력에는 승인 상태(`승인됨`)만 있고 누가 승인했는지와 회수 이유가 없습니다.
  - `revoke_reason`(회수 이유) · `approver`(승인한 사람) · `approved_at`(승인한 시각) 키를 추가하면 됩니다.
  - 다만 승인한 사람을 남기려면 보안 책임자의 결정(`decisions`)에 사람 이름도 함께 적어 두어야 합니다.
  - 지금 결정에는 「승인」이라는 문자열만 있습니다.

**왜**

- 회수는 실행한 뒤에 다시 판정해 보아야 효과를 압니다.
  - 실행한 7건 중 6건은 회수 전에도 이미 막혀 있어서 판정이 바뀌지 않았고, 이력은 「막혀 있던 권한까지 정리했다」는 증거입니다.
  - 이력이 있어야 나중에 누가 언제 무엇을 왜 없앴는지 설명할 수 있습니다.

**자주 틀리는 곳**

- `if plan["approval"] == "승인 대기":` 검사를 빼고 모든 계획을 실행하면, 아직 승인되지 않은 junho 의 예외 2번까지 지워집니다.
  - 오류는 나지 않고 건수만 달라집니다.
  - 실행하면 다음처럼 됩니다(`실행 8 건, 대기 0 건` 이 나오면 이 실수입니다).

```
--- 단계 1: 실행 - 회수 결과
junho SALES:QUERY | 역할에서 권한 빼기 | 실행
dami SALES:QUERY | 역할 해제 | 실행
dami SALES:CHANGE | 역할 해제 | 실행
seoyeon SETTLE:QUERY | 예외 삭제 | 실행
junho SALES:CHANGE | 예외 삭제 | 실행
dami SALES:QUERY | 예외 삭제 | 실행
batch-night SALES:QUERY | 예외 삭제 | 실행
gaeun SETTLE:QUERY | 예외 삭제 | 실행
실행 8 건, 대기 0 건
--- 단계 2: 확인 - 회수 전후의 판정
junho SALES:QUERY | 허용(역할 권한) -> 거부(권한 없음) | 바뀜
dami SALES:QUERY | 거부(퇴사한 계정) -> 거부(퇴사한 계정) | 그대로
dami SALES:CHANGE | 거부(퇴사한 계정) -> 거부(퇴사한 계정) | 그대로
seoyeon SETTLE:QUERY | 거부(권한 없음) -> 거부(권한 없음) | 그대로
junho SALES:CHANGE | 거부(권한 없음) -> 거부(권한 없음) | 그대로
dami SALES:QUERY | 거부(퇴사한 계정) -> 거부(퇴사한 계정) | 그대로
batch-night SALES:QUERY | 거부(권한 없음) -> 거부(권한 없음) | 그대로
gaeun SETTLE:QUERY | 거부(권한 없음) -> 거부(권한 없음) | 그대로
--- 단계 3: 저장 - 회수 이력
저장 8 건, 다시 읽은 건수 8 건, 첫 이력: junho SALES:QUERY 실행
```

**관제에서는**

- 회수 이력은 지우지 않고 보관하고, 승인 대기가 길어지는 계획은 담당자에게 알립니다.
  - 회수한 뒤 다시 판정해서 막혔는지 확인하는 점검을 정기적으로 돌립니다.

---

## 앞 Exercise 파일 완성본

앞 Exercise 파일이 없거나 잘 안 될 때 이 코드로 만듭니다. Unit 6 · Unit 7의 파일이 필요하면 Unit 6 · Unit 7 문서 맨 아래의 「앞 Exercise 파일 완성본」을 씁니다.

**`revoke_input.py`** (Exercise 8-1 도우미)

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from review_list import build_access_list                        # Exercise 6-1에서 만든 현황 함수를 불러온다
from review_rules import find_stale                              # Exercise 6-2에서 만든 규칙 점검 함수를 불러온다
from review_unused import load_last_used, find_unused            # Exercise 6-3에서 만든 안 쓴 권한 점검 함수를 불러온다
from overprivilege import generate_report                        # Exercise 7-1에서 만든 리포트 함수를 불러온다
from report_exclude import load_exclude_map, split_by_exclude    # Exercise 7-2에서 만든 회수 제외 함수를 불러온다

REVIEW_TIME = datetime.strptime("2026-10-29 14:00", "%Y-%m-%d %H:%M")   # Unit 7에서 점검한 시각(고정). 같은 결과를 얻으려고 그 시각을 쓴다
TIME_FORMAT = "%Y-%m-%d %H:%M"                                   # 시각 문자열의 형식


def load_to_revoke():                                            # Unit 7의 점검 결과를 다시 만드는 함수
    """Unit 7의 점검에서 나온 「회수 대상」 리스트(8개)를 리턴한다.
    회수 계획을 세우기 전에 회수할 권한을 준비할 때 쓴다.
    """
    access_list = build_access_list()                            # 현황을 만든다
    stale = find_stale(access_list, REVIEW_TIME)                 # 규칙에 걸린 권한을 찾는다
    last_used_map = load_last_used()                             # 마지막 사용 시각 딕셔너리를 읽는다
    unused = find_unused(access_list, last_used_map, REVIEW_TIME, 90)  # 90일 넘게 안 쓴 권한을 찾는다
    generated_at = REVIEW_TIME.strftime(TIME_FORMAT)             # 리포트를 만든 시각을 문자열로 바꾼다
    report = generate_report(access_list, stale, unused, 90, generated_at)  # 후보 리포트를 만든다
    exclude_map = load_exclude_map("config/exclude_list.json")   # 회수 제외 리스트를 읽는다
    to_revoke, excluded = split_by_exclude(report["findings"], exclude_map)   # 후보를 회수 대상과 회수 제외로 나눈다
    return to_revoke                                             # 회수 대상 리스트만 리턴한다
```

**`revoke_plan.py`** (Exercise 8-1 완성본)

```python
def exception_id(source):                                        # "예외 3번" 모양 문자열을 받는 함수
    """문자열 「예외 3번」에서 예외 번호(3)를 숫자로 꺼낸다.
    판정 이유에서 어느 예외로 허용했는지 찾을 때 쓴다.
    """
    number_text = source.replace("예외 ", "")                      # "예외 3번" 에서 "예외 " 를 지워 "3번" 으로 만든다
    number_text = number_text.replace("번", "")                   # "번" 을 지워 "3" 으로 만든다
    return int(number_text)                                      # 문자열 "3" 을 숫자 3 으로 바꿔 리턴한다


def count_users_by_role(users):                                  # 사용자 딕셔너리를 받는 함수
    """역할마다 사용자가 몇 명인지 센다(재직 여부와 상관없이).
    역할을 회수하기 전에 영향을 볼 때 쓴다.
    예: {"finance": 1, "sales": 2}
    """
    counts = {}                                                  # 역할 → 사용자 수를 담을 빈 딕셔너리
    for info in users.values():                                  # 사용자 정보를 하나씩 꺼낸다(.values() 는 딕셔너리의 값만 꺼낸다)
        role = info["role"]                                      # 그 사용자의 역할
        old_count = counts.get(role, 0)                          # 그 키의 지금까지 센 수(처음이면 0)
        counts[role] = old_count + 1                             # 1 늘려서 다시 적는다
    return counts                                                # 역할별 사용자 수를 리턴한다


def make_plan(finding, method, target, impact):                  # 회수 대상 · 방법 · 대상 · 영향 범위를 받는 함수
    """회수 대상을 복사해 method · target · impact 키를 더한 계획 한 개를 만든다.
    impact 는 이 회수로 사라지는 (사용자, 권한)의 수이고, 회수 전에 영향을 가늠할 때 쓴다.
    """
    plan = finding.copy()                                        # 원래 권한은 바꾸지 않고 복사한다
    plan["method"] = method                                      # 회수 방법을 적는다
    plan["target"] = target                                      # 실제로 지울 대상(예외 번호 · 사용자 · 역할)을 적는다
    plan["impact"] = impact                                      # 사라지는 (사용자, 권한)의 수를 적는다
    return plan                                                  # 계획 한 건을 리턴한다


def build_plan(finding, method, users, roles, role_counts):      # 회수 대상 한 건 · 회수 방법 · 사용자 · 역할 · 역할별 사용자 수를 받는 함수
    """회수 방법에 맞게 지울 대상과 영향을 정해 계획 한 개를 만든다.
    회수 계획을 세울 때 쓴다.
    """
    info = users[finding["user"]]                                # 그 사용자의 정보를 꺼낸다
    if method == "예외 삭제":                                    # 방법이 예외 삭제이면
        target = exception_id(finding["source"])                 # 지울 대상은 예외 번호
        return make_plan(finding, method, target, 1)             # 영향은 권한 1건
    if method == "역할 해제":                                    # 방법이 역할 해제이면
        role_permissions = roles[info["role"]]                   # 그 사용자의 역할에 든 권한 리스트
        impact = len(role_permissions)                           # 영향은 그 역할에 든 권한 수
        return make_plan(finding, method, finding["user"], impact)  # 지울 대상은 그 사용자의 이름
    impact = role_counts[info["role"]]                           # 역할에서 권한 빼기: 영향은 그 역할을 가진 사용자 수(각자 그 권한 1건을 잃는다)
    return make_plan(finding, method, info["role"], impact)      # 지울 대상은 역할 이름


def plan_revocation(findings, users, roles):                     # 회수 대상 리스트 · 사용자 딕셔너리 · 역할 딕셔너리를 받는 함수
    """회수 대상마다 회수 방법을 정해 계획 리스트를 리턴한다.
    실제로는 아무것도 지우지 않으며, 회수하기 전에 계획부터 세울 때 쓴다.
    """
    role_counts = count_users_by_role(users)                     # 역할마다 사용자가 몇 명인지 센다(반복 전에 한 번만)
    plans = []                                                   # 계획을 담을 빈 리스트
    for finding in findings:                                     # 회수 대상을 하나씩 꺼낸다
        info = users[finding["user"]]                            # 그 사용자의 정보를 꺼낸다
        if "예외" in finding["source"]:                          # 예외로 받은 권한이면
            method = "예외 삭제"                                 # 그 예외를 지운다
        elif not info["employed"]:                               # 퇴사한 사용자의 역할 권한이면
            method = "역할 해제"                                 # 그 사용자의 역할을 해제한다
        else:                                                    # 재직 중인 사용자의 역할 권한이면
            method = "역할에서 권한 빼기"                        # 역할에서 그 권한을 뺀다
        plan = build_plan(finding, method, users, roles, role_counts)  # 계획 한 건을 만든다
        plans.append(plan)                                       # 방법에 맞는 계획을 만들어 계획 리스트에 추가한다
    return plans                                                 # 계획 리스트를 리턴한다
```

**`revoke_approve.py`** (Exercise 8-2 완성본)

```python
from config_loader import load_json                              # Unit 3에서 만든 안전한 읽기 함수를 불러온다


def load_sensitive(path):                                        # 민감한 권한 파일 경로를 받는 함수
    """민감한 권한 파일을 읽어 「자원:행위」 리스트로 리턴하고, 없거나 깨졌으면 빈 리스트를 리턴한다.
    승인이 필요한 회수를 가릴 때 쓴다.
    """
    return load_json(path, [])                                   # 안전하게 읽어 그대로 리턴한다


def plan_key(plan):                                              # 계획 한 건을 받는 함수
    """「사용자:권한」 문자열(예: "dami:SALES:CHANGE")을 리턴한다.
    계획에 맞는 승인 결정을 찾는 키로 쓴다.
    """
    user = plan["user"]                                          # 계획의 사용자
    permission = plan["permission"]                              # 계획의 권한
    return f"{user}:{permission}"                                # 사용자와 권한을 : 로 이어 붙인다


def needs_approval(plan, sensitive):                             # 계획 한 건과 민감한 권한 리스트를 받는 함수
    """민감한 권한이거나 영향이 2개 이상이면 True, 아니면 False 를 리턴한다.
    승인이 필요한 회수를 가려낼 때 쓴다.
    """
    is_sensitive = plan["permission"] in sensitive               # 권한이 민감한 권한 리스트에 있는지(True 또는 False)
    is_big_impact = plan["impact"] >= 2                          # 영향이 2건 이상인지(True 또는 False)
    return is_sensitive or is_big_impact                         # 둘 중 하나라도 참이면 True 를 리턴한다


def mark_approvals(plans, sensitive, decisions):                 # 계획 리스트 · 민감한 권한 리스트 · 승인 결정 딕셔너리를 받는 함수
    """계획마다 "approval" 키(승인 불필요 · 승인됨 · 승인 대기)를 적은 복사본 리스트를 리턴한다.
    어떤 회수가 보안 책임자의 승인을 기다려야 하는지 가를 때 쓴다.
    """
    results = []                                                 # 결과를 담을 빈 리스트
    for plan in plans:                                           # 계획을 하나씩 꺼낸다
        item = plan.copy()                                       # 원래 계획은 바꾸지 않고 복사한다
        key = plan_key(plan)                                     # 승인 결정을 찾는 「사용자:권한」 문자열을 만든다
        decision = decisions.get(key)                            # 보안 책임자의 결정을 꺼낸다(결정이 없으면 None)
        needs = needs_approval(plan, sensitive)                  # 승인이 필요한 계획인지 알아본다(True 또는 False)
        if not needs:                                            # 승인이 필요하지 않은 계획이면
            item["approval"] = "승인 불필요"                     # 승인 불필요라고 적는다
        elif decision == "승인":                                  # 승인이 필요하고, 보안 책임자가 승인하기로 결정한 계획이면
            item["approval"] = "승인됨"                          # 승인됨이라고 적는다
        else:                                                    # 승인이 필요한데 아직 결정이 없으면
            item["approval"] = "승인 대기"                       # 승인 대기라고 적는다
        results.append(item)                                     # 결과 리스트에 추가한다
    return results                                               # 결과 리스트를 리턴한다
```

**`config/sensitive.json`** (Exercise 8-2 완성본)

```json
["SALES:CHANGE", "ACCOUNT:CHANGE", "SETTLE:CHANGE"]
```

**`revoke.py`** (Exercise 8-3 완성본)

```python
import json                                                      # JSON 파일을 쓰는 모듈을 불러온다


def remove_exception(exceptions, target_id):                     # 예외 리스트와 지울 예외 번호를 받는 함수
    """예외 리스트에서 번호가 target_id 인 예외를 지운다.
    지웠으면 True, 못 찾았으면 False 를 리턴한다.
    지원이 끝난 예외를 회수할 때 쓴다.
    """
    for exception in exceptions:                                       # 예외를 하나씩 꺼낸다
        if exception["id"] == target_id:                               # 번호가 같으면
            exceptions.remove(exception)                               # 리스트에서 그 예외를 지운다
            return True                                          # 지웠다고 알리고 함수를 끝낸다
    return False                                                 # 끝까지 못 찾았으면 False 를 리턴한다


def apply_plan(plan, users, roles, exceptions):                  # 계획 한 건 · 사용자 · 역할 · 예외 리스트를 받는 함수
    """계획 한 개의 방법대로 프로그램 안의 데이터를 바꾼다.
    승인된 회수를 실행할 때 쓰며, 승인 확인은 부르는 쪽이 한다.
    """
    if plan["method"] == "예외 삭제":                            # 방법이 예외 삭제이면
        remove_exception(exceptions, plan["target"])             # 예외 리스트에서 그 번호의 예외를 지운다
    elif plan["method"] == "역할 해제":                          # 방법이 역할 해제이면
        user_info = users[plan["target"]]                        # 그 사용자의 정보 딕셔너리를 꺼낸다
        user_info["role"] = ""                                   # 역할을 빈 문자열로 바꾼다(어떤 역할의 권한도 받지 않게 된다)
    else:                                                        # 방법이 역할에서 권한 빼기이면
        role_permissions = roles[plan["target"]]                 # 그 역할의 권한 리스트를 꺼낸다
        role_permissions.remove(plan["permission"])              # 그 리스트에서 그 권한을 지운다


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
        if plan["approval"] == "승인 대기":                      # 아직 승인을 기다리는 계획이면
            result = "대기"                                      # 실행하지 않고 대기로 남긴다
        else:                                                    # 승인 불필요이거나 승인된 계획이면
            apply_plan(plan, users, roles, exceptions)           # 실제로 회수한다
            result = "실행"                                      # 실행했다고 적는다
        entry = {                                                 # 회수 이력 한 개의 값을 묶는다(여러 줄)
            "time": now,                                         # 시각
            "user": plan["user"],                                # 사용자
            "permission": plan["permission"],                    # 권한
            "method": plan["method"],                            # 회수 방법
            "approval": plan["approval"],                        # 승인 상태
            "result": result,                                    # 결과(실행 또는 대기)
        }
        log.append(entry)                                        # 이력 한 건을 이력 리스트에 추가한다
    return log                                                   # 이력 리스트를 리턴한다
```
