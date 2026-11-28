---
id: m3-u04-l08
title: 정답
render: markdown
---

# 정답

## 정답을 보는 방법

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## 실습 4-1 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise4-1_run.py
```

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 세 함수입니다.

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

<h2>결과</h2>

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
  - 예를 들어 junho 의 `SALES:QUERY` 는 재직자의 권한이지만 마지막 사용이 90일보다 오래됐다고 Unit 3의 점검에서 나왔고 영향이 1건이라 승인 없이 회수합니다.
- (다) 실습 4-2에서 junho 의 `SALES:CHANGE`(예외 2번) 계획은 실행하지 않고 「대기」로 남습니다.
  - 승인이 오래 나지 않으면 이 예외가 정리되지 않은 채 남아 점검에 계속 나오고 담당자가 같은 계획을 거듭 확인해야 합니다.
  - 그 예외는 이미 만료되어 접근은 막혀 있지만, 만료 시각이 고쳐지는 등의 일이 생기면 다시 쓰일 수 있어 오래 두면 위험합니다.

<h2>왜</h2>

- 쓰기 같은 중요한 권한과, 한 번의 회수로 권한이 여러 개 사라지는 회수는 한 사람이 혼자 정하지 않고 승인을 받습니다.
  - 승인 상태를 계획마다 적어 두면 실습 4-2이 「승인 대기」인 계획만 빼고 실행할 수 있습니다.
  - 같은 사용자의 역할 해제 두 건(dami)은 같은 변경(`role` 비우기)이므로 함께 결정해야 합니다.
  - 코드는 이를 막지 않으므로, 한쪽만 승인하면 승인받지 않은 권한까지 함께 없어집니다.

<h2>자주 틀리는 곳</h2>

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

<h2>관제에서는</h2>

- 승인 대기 중인 계획에는 처리 기한을 정해 두고, 넘으면 담당자에게 알립니다.
  - 승인한 사람과 요청한 사람은 달라야 합니다.

---

## 실습 4-2 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise4-2_run.py
```

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 `remove_exception` 의 한 곳, `apply_plan` 의 세 곳, `execute_revocation` 의 한 곳입니다.

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

<h2>결과</h2>

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
  - 「이 권한이 왜 없어졌나요?」에 답하려면 ① 회수 이유(퇴사 · 만료 · 90일 미사용 중 무엇 때문인지. Unit 3의 점검 결과의 `reasons` 키에 적혀 있습니다) ② 승인한 사람의 이름 ③ 승인한 시각이 있어야 합니다.
  - 지금 이력에는 승인 상태(`승인됨`)만 있고 누가 승인했는지와 회수 이유가 없습니다.
  - `revoke_reason`(회수 이유) · `approver`(승인한 사람) · `approved_at`(승인한 시각) 키를 추가하면 됩니다.
  - 다만 승인한 사람을 남기려면 보안 책임자의 결정(`decisions`)에 사람 이름도 함께 적어 두어야 합니다.
  - 지금 결정에는 「승인」이라는 문자열만 있습니다.

<h2>왜</h2>

- 회수는 실행한 뒤에 다시 판정해 보아야 효과를 압니다.
  - 실행한 7건 중 6건은 회수 전에도 이미 막혀 있어서 판정이 바뀌지 않았고, 이력은 「막혀 있던 권한까지 정리했다」는 증거입니다.
  - 이력이 있어야 나중에 누가 언제 무엇을 왜 없앴는지 설명할 수 있습니다.

<h2>자주 틀리는 곳</h2>

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

<h2>관제에서는</h2>

- 회수 이력은 지우지 않고 보관하고, 승인 대기가 길어지는 계획은 담당자에게 알립니다.
  - 회수한 뒤 다시 판정해서 막혔는지 확인하는 점검을 정기적으로 돌립니다.

---

## 도전 4-1 정답

**터미널에 입력합니다.**

```bash
pwd
python challenge4-1_run.py
```

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 네 함수의 다섯 군데입니다.

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

<h2>결과</h2>

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

<h2>왜</h2>

- 회수는 되돌리기 어려운 변경이라 지우기 전에 방법과 영향을 먼저 표로 확인합니다.
  - 같은 8건이라도 방법에 따라 영향받는 사람이 1명일 수도, 여러 명일 수도 있습니다.
  - 퇴사자는 역할 정의가 아니라 그 사람의 `role` 만 해제하므로 같은 역할의 재직자에게 영향이 없습니다.

<h2>자주 틀리는 곳</h2>

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

<h2>관제에서는</h2>

- 회수 도구는 실제로 지우기 전에 계획(드라이 런)을 만들어 담당자에게 보여 주고, 한 번에 권한이 여러 개 사라지는 변경은 따로 확인합니다.

---

## 도전 4-2 정답

**터미널에 입력합니다.**

```bash
pwd
python challenge4-2_run.py
```

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 세 함수입니다.

① `is_work_time` 안

```python
    start_hour, end_hour = rule["hours"]                                   # 허용 시작 시와 끝 시를 꺼낸다
    hour = now.hour                                              # 요청 시각의 시를 꺼낸다
    return start_hour <= hour < end_hour                                   # 시작 시 이상이고 끝 시 미만인지(True 또는 False)를 리턴한다
```

② `is_allowed_network` 안

```python
    allowed_networks = rule["networks"]                          # 허용된 접속 위치 리스트를 꺼낸다
    return network in allowed_networks                           # 그 리스트에 들어 있는지(True 또는 False)를 리턴한다
```

③ `evaluate_conditional` 안(미리 채운 `if rule["permission"] == permission:` 아래)

```python
            if not is_work_time(rule, now):                      # 업무 시간 안이 아니면
                return False, "업무 시간 밖"                       # 거부한다
            if not is_allowed_network(rule, network):            # 허용된 접속 위치가 아니면
                return False, "허용되지 않은 접속 위치"            # 거부한다
```

<h2>결과</h2>

- (가) 출력은 다음과 같고, 허용은 **3건**(1 · 2 · 6번), 거부는 **5건**입니다.
  - 조건 때문에 거부된 요청은 **4건**(3 · 4 · 5 · 7번)이고, 8번은 기본 판정에서 퇴사한 계정으로 거부됐습니다.

```
--- 단계 1: 판정 - 요청 8 건
1 seoyeon SALES:QUERY office 10:00 -> 허용(역할 권한)
2 seoyeon SALES:CHANGE office 09:00 -> 허용(역할 권한)
3 seoyeon SALES:CHANGE office 18:00 -> 거부(업무 시간 밖)
4 seoyeon SALES:CHANGE external 10:00 -> 거부(허용되지 않은 접속 위치)
5 seoyeon SALES:CHANGE external 22:00 -> 거부(업무 시간 밖)
6 junho SETTLE:QUERY vpn 19:30 -> 허용(역할 권한)
7 gaeun ACCOUNT:CHANGE vpn 10:00 -> 거부(허용되지 않은 접속 위치)
8 dami SALES:QUERY office 10:00 -> 거부(퇴사한 계정)
--- 단계 2: 확인 - 조건 파일에 적힌 조건
SALES:CHANGE | 9시부터 18시 전까지 | office, vpn
SETTLE:QUERY | 8시부터 20시 전까지 | office, vpn
ACCOUNT:CHANGE | 9시부터 18시 전까지 | office
```

- (나) 정상 사용자에게는 어긋난 조건을 모두 알려 주는 쪽이 낫습니다.
  - 한 번에 무엇을 고쳐야 하는지 알 수 있기 때문입니다.
  - 계정을 가로챈 사람에게는 이유를 하나만 알려 주는 쪽이 낫습니다.
  - 어떤 조건이 걸려 있는지 덜 알려 주기 때문입니다.
  - 두 경우가 서로 반대라서, 실제 서비스에서는 요청한 사람에게 보내는 응답에는 이유를 줄이고 서버 로그에는 어긋난 조건을 모두 남기는 방법을 많이 씁니다.
  - 관제 담당자에게는 어긋난 조건을 **모두** 아는 쪽이 낫습니다.
  - 어긋난 조건이 여러 개인 요청이 몇 건인지 세면 평소와 다른 접속이 얼마나 되는지 볼 수 있기 때문입니다.
  - 이번 실습의 코드는 첫 번째 이유만 리턴하므로, 모두 알리려면 코드를 바꿔야 합니다.
- (다) 권한이 있어도 계정을 다른 사람이 가로챘다면 그 요청은 정상 사용자가 보낸 것이 아닙니다.
  - 로그인할 때 한 번만 확인하면 가로챈 계정이 새벽 2시에 외부에서 들어와도 막지 못하고, 쓰기 권한이 있는 데이터까지 바꿀 수 있습니다.
  - 요청마다 시간과 접속 위치를 확인하면(서버가 그 값을 직접 알아낼 수 있을 때) 평소와 다른 접속을 바로 막을 수 있습니다.

<h2>왜</h2>

- 권한이 있다는 것만으로 모든 요청을 믿지 않고, 요청마다 조건을 함께 봅니다.
  - 기본 판정이 거부이면 조건을 볼 필요가 없어서 먼저 확인하고 바로 끝냅니다.
  - 조건은 파일에 두어서 업무 시간이 바뀌어도 코드를 고치지 않습니다.

<h2>자주 틀리는 곳</h2>

- `is_work_time` 의 끝 시각 비교를 `hour < end` 대신 `hour <= end` 로 쓰면 18시 정각 요청도 허용됩니다.
  - 오류는 나지 않고 결과만 달라집니다.
  - 실행하면 다음처럼 됩니다(3번 줄 18:00 요청이 허용으로 나오면 이 실수입니다).

```
--- 단계 1: 판정 - 요청 8 건
1 seoyeon SALES:QUERY office 10:00 -> 허용(역할 권한)
2 seoyeon SALES:CHANGE office 09:00 -> 허용(역할 권한)
3 seoyeon SALES:CHANGE office 18:00 -> 허용(역할 권한)
…
```

<h2>관제에서는</h2>

- 접근 제어 서비스는 사용자를 확인한 뒤에도 접속 시간, 위치, 기기 상태를 요청마다 다시 확인하고, 평소와 다른 요청은 한 번 더 확인하거나 막습니다.
  - 이번 실습에서 단순화한 부분은 두 가지입니다.
  - 첫째, 실습에서는 접속 위치(`network`)와 시각(`time`)을 요청하는 쪽이 적어 보내지만, 실제 서비스는 서버에 접속해 온 쪽의 주소(IP)와 서버 시계로 직접 알아냅니다.
  - 둘째, 조건 파일을 읽지 못하면 이번 실습의 코드는 조건 없이 모두 허용하는데, 실제 서비스는 읽지 못하면 서버를 켜지 않거나 모두 거부하는 쪽으로 만듭니다.

---

## 도전 4-3 정답

**터미널에 입력합니다.**

터미널 1:

```bash
pwd
python access_server.py
```

터미널 2:

```bash
cd access_control
pwd
python send_checks.py
```

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 세 함수의 다섯 군데입니다.

① `parse_time` 안(미리 채운 `try` 아래)

```python
        return datetime.strptime(text, TIME_FORMAT)              # 문자열을 시각으로 바꿔 리턴한다
```

② `parse_time` 안(미리 채운 `except` 아래)

```python
        return None                                              # 모양이 틀렸으면 없다고 알린다
```

③ `write_log` 안(`with` 위)

```python
    mode = "a"                                                   # 파일을 여는 모드: 덧붙이기("a")
```

④ `check` 안(미리 채운 400 처리 아래)

```python
    allowed, reason = evaluate_conditional(user, resource, action, network, now, RULES)   # 조건까지 판정한다
```

⑤ `check` 안(미리 채운 `write_log` 줄 아래)

```python
    if allowed:                                                  # 허용이면
        return {"allowed": True, "reason": reason}, 200          # 상태 코드 200 으로 답한다
    return {"allowed": False, "reason": reason}, 403             # 거부이면 상태 코드 403 으로 답한다
```

<h2>결과</h2>

- (가) 출력은 다음과 같고, 상태 코드는 200 이 **3건**(1 · 4 · 5번), 403 이 **5건**(2 · 3 · 6 · 7 · 8번), 400 이 **1건**(9번)입니다.
  - 서버가 남긴 로그는 **8줄**입니다(400 요청은 기록하지 않습니다).

```
--- 단계 1: 응답 - 요청 9 건
1 seoyeon SALES:CHANGE -> 200 역할 권한
2 seoyeon SALES:CHANGE -> 403 업무 시간 밖
3 seoyeon SALES:CHANGE -> 403 허용되지 않은 접속 위치
4 seoyeon SALES:QUERY -> 200 역할 권한
5 junho SETTLE:QUERY -> 200 역할 권한
6 junho SETTLE:QUERY -> 403 허용되지 않은 접속 위치
7 gaeun ACCOUNT:CHANGE -> 403 허용되지 않은 접속 위치
8 dami SALES:QUERY -> 403 퇴사한 계정
9 seoyeon SALES:CHANGE -> 400 입력이 잘못됨
--- 단계 2: 로그 - 서버가 남긴 8 줄
seoyeon SALES:CHANGE office 2026-10-30T09:00 -> True 역할 권한
seoyeon SALES:CHANGE office 2026-10-30T18:00 -> False 업무 시간 밖
seoyeon SALES:CHANGE external 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
seoyeon SALES:QUERY external 2026-10-30T23:00 -> True 역할 권한
junho SETTLE:QUERY vpn 2026-10-30T19:30 -> True 역할 권한
junho SETTLE:QUERY external 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
gaeun ACCOUNT:CHANGE vpn 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
dami SALES:QUERY office 2026-10-30T10:00 -> False 퇴사한 계정
--- 단계 3: 대조 - 판정까지 간 응답과 로그
판정까지 간 응답 8 건 / 로그에 남은 줄 8 줄
```

- (나) 403 은 요청이 제대로 도착했고 서버가 판정(인가)까지 마친 뒤 거부했다는 뜻이라, 같은 요청을 다시 보내도 결과가 같습니다.
  - 400 은 요청 자체가 잘못됐다는 뜻이라, 값을 고쳐 다시 보내면 결과가 달라질 수 있습니다.
  - 요청을 보내는 쪽이 둘을 구별하면 400 이면 자기 프로그램의 오류로 보고 고치고, 403 이면 접근 거부로 처리할 수 있습니다.
  - 구별하지 않으면 거부를 입력 오류로 오해해 같은 요청을 계속 다시 보내거나, 입력 오류를 거부로 오해해 방치하게 됩니다.
- (다) `"w"` 로 열면 요청이 올 때마다 파일이 새로 써져서 앞의 기록이 지워지고 마지막 한 건만 남습니다.
  - 한 달 뒤에 지난주 거부 기록을 찾으면 그 기록은 이미 없습니다.
  - 로그는 시간이 지나도 앞의 기록이 남아 있어야 하므로 끝에 덧붙이는 `"a"` 방식이 알맞습니다.
  - 한 줄에 한 건씩 쓰면 파일이 아무리 커져도 한 줄씩 읽어 처리할 수 있습니다.

<h2>왜</h2>

- 판정을 서버로 만들어 주소로 요청하게 하면 여러 프로그램이 같은 규칙으로 물을 수 있습니다.
  - 상태 코드로 허용(200) · 거부(403) · 잘못된 요청(400)을 숫자로 구별해 알려 주고, 요청마다 한 줄씩 로그를 남겨 나중에 볼 수 있게 합니다.
  - 응답과 서버 로그를 세어 맞춰 보면 판정까지 간 요청이 빠짐없이 로그에 남았는지 알 수 있습니다.
  - 입력 오류(400)가 로그에 없다는 점도 이 대조로 알 수 있습니다.

<h2>자주 틀리는 곳</h2>

- 거부 응답의 상태 코드를 `403` 대신 `200` 으로 쓰면 화면에 보이는 내용은 같아서 알아채기 어렵습니다.
  - 하지만 상태 코드만 보는 프로그램은 거부를 허용으로 오해합니다.
  - 실행하면 다음처럼 됩니다(거부 요청인데 `->` 뒤 숫자가 `200` 이면 이 실수입니다).

```
--- 단계 1: 응답 - 요청 9 건
1 seoyeon SALES:CHANGE -> 200 역할 권한
2 seoyeon SALES:CHANGE -> 200 업무 시간 밖
3 seoyeon SALES:CHANGE -> 200 허용되지 않은 접속 위치
4 seoyeon SALES:QUERY -> 200 역할 권한
5 junho SETTLE:QUERY -> 200 역할 권한
6 junho SETTLE:QUERY -> 200 허용되지 않은 접속 위치
7 gaeun ACCOUNT:CHANGE -> 200 허용되지 않은 접속 위치
8 dami SALES:QUERY -> 200 퇴사한 계정
9 seoyeon SALES:CHANGE -> 400 입력이 잘못됨
--- 단계 2: 로그 - 서버가 남긴 8 줄
seoyeon SALES:CHANGE office 2026-10-30T09:00 -> True 역할 권한
seoyeon SALES:CHANGE office 2026-10-30T18:00 -> False 업무 시간 밖
seoyeon SALES:CHANGE external 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
seoyeon SALES:QUERY external 2026-10-30T23:00 -> True 역할 권한
junho SETTLE:QUERY vpn 2026-10-30T19:30 -> True 역할 권한
junho SETTLE:QUERY external 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
gaeun ACCOUNT:CHANGE vpn 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
dami SALES:QUERY office 2026-10-30T10:00 -> False 퇴사한 계정
--- 단계 3: 대조 - 판정까지 간 응답과 로그
판정까지 간 응답 8 건 / 로그에 남은 줄 8 줄
```

<h2>관제에서는</h2>

- 판정 서버는 요청 로그를 지우지 않고 보관하고, 거부(403)가 갑자기 늘면 담당자에게 알립니다.
  - 400 도 따로 기록해 두어야 많아졌는지 알 수 있습니다.
  - 서버가 요청을 받은 시각은 서버가 직접 적어야 합니다(지금은 요청한 쪽이 보낸 `time` 을 그대로 씁니다).
  - 입력 오류 요청도 따로 기록해 두면 공격 시도를 찾는 데 쓸 수 있습니다.

---
