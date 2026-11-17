---
id: m3-u04-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/082_day03_am_request.md
  mission_id: GichanSource.m3-1023-am-request
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## Exercise Exercise 4-3 정답

 **터미널에 입력합니다.**

```bash
python day03_2-1_run.py
```

**채운 코드** (한 예)

```python
    if user not in USERS:                                        # 사용자 파일에 없는 이름이면
        return False, "등록되지 않은 사용자"                       # 접수하지 않고 이유를 알린다
    if reason == "":                                             # 이유가 비어 있으면
        return False, "이유가 없음"                                # 접수하지 않고 이유를 알린다
    if until <= received_at:                                             # 희망 만료 시각이 접수 시각보다 늦지 않으면(같은 형식의 문자열은 앞에서부터 비교해도 시각 순서와 같다)
        return False, "만료 시각이 이미 지났음"                     # 접수하지 않고 이유를 알린다
    request_id = len(REQUESTS) + 1                               # 다음 요청 번호(지금 개수 + 1)
    permission = f"{resource}:{action}"                          # "자원:행위" 모양 권한 문자열
    request = {                                                  # 요청서 한 장. 상태는 검토 중으로 시작한다
        "id": request_id,                                        # 요청 번호
        "user": user,                                            # 요청자
        "resource": resource,                                    # 자원
        "action": action,                                        # 행위
        "permission": permission,                                # 권한
        "until": until,                                          # 희망 만료 시각
        "reason": reason,                                        # 요청 이유
        "requested_at": received_at,                             # 접수 시각
        "status": "reviewing",                                   # 상태: 검토 중
    }
    REQUESTS.append(request)                                     # 요청서 리스트 끝에 추가한다
    return True, request                                         # 접수했다고 알리고 요청서를 리턴한다
```

**결과**

- (가) 출력은 다음과 같고, 접수되지 않은 세 건은 `hana`(`user not in USERS` 조건에 걸림, 사용자 파일에 없는 이름), `seoyeon` 의 `ACCOUNT:QUERY`(`reason == ""` 조건에 걸림, 이유가 비어 있음), `gaeun` 의 `ACCOUNT:QUERY`(`until <= received_at` 조건에 걸림, 희망 만료 시각 10/22(목) 18:00 이 접수 시각 10/23(금) 09:15 보다 앞)입니다. 줄 수가 달라도 주석이 말한 일을 하면 코드는 맞습니다.

```
--- 단계 1: 접수 - 요청 일곱 건을 하나씩 넣는다
seoyeon SETTLE QUERY -> 접수됨, 요청 번호 1
gaeun SALES QUERY -> 접수됨, 요청 번호 2
dami SALES QUERY -> 접수됨, 요청 번호 3
junho SETTLE QUERY -> 접수됨, 요청 번호 4
hana SALES QUERY -> 접수 안 됨: 등록되지 않은 사용자
seoyeon ACCOUNT QUERY -> 접수 안 됨: 이유가 없음
gaeun ACCOUNT QUERY -> 접수 안 됨: 만료 시각이 이미 지났음
--- 단계 2: 점검 - 요청서 리스트
1 seoyeon SETTLE:QUERY reviewing
2 gaeun SALES:QUERY reviewing
3 dami SALES:QUERY reviewing
4 junho SETTLE:QUERY reviewing
```

- (나) 요청자가 적은 기간을 그대로 믿으면 안 됩니다. 요청자는 일이 끝난 뒤에도 불편하지 않게 길게 적기 쉽습니다. 승인자가 확인할 것: ① 이유에 적힌 일이 실제로 언제 끝나는지, 그 일에 필요한 가장 짧은 기간인지 ② 요청자가 이 권한을 받는 것이 업무에 맞는지(영업이 정산을 보려는 이유가 분명한지) ③ 만료 시각이 너무 먼 미래는 아닌지(접수 단계는 이미 지난 시각만 거르므로 최대 기간을 정해 둡니다). 필요하면 기간을 줄여서 승인합니다.

**왜** — 요청을 기록으로 받아야 「누가 언제 무엇을 왜 요청했나」를 나중에 증명할 수 있습니다. 필요한 정보가 빠진 요청은 접수 단계에서 걸러 내야 뒤의 승인 · 부여 단계가 단순해집니다. 상태를 `"reviewing"` 으로 시작해 두면 Exercise 4-2가 「검토 중인 것만 처리」라는 규칙을 쓸 수 있습니다.

**자주 틀리는 곳** — `REQUESTS.append(request)` 를 빼먹는 경우가 가장 많습니다. 그러면 요청 번호가 모두 `1` 로 나오고 단계 2의 요청서 리스트가 비어 나옵니다. 실행하면 다음처럼 됩니다(번호가 `1` 만 나오는 것이 신호입니다).

```
--- 단계 1: 접수 - 요청 일곱 건을 하나씩 넣는다
seoyeon SETTLE QUERY -> 접수됨, 요청 번호 1
gaeun SALES QUERY -> 접수됨, 요청 번호 1
dami SALES QUERY -> 접수됨, 요청 번호 1
junho SETTLE QUERY -> 접수됨, 요청 번호 1
hana SALES QUERY -> 접수 안 됨: 등록되지 않은 사용자
seoyeon ACCOUNT QUERY -> 접수 안 됨: 이유가 없음
gaeun ACCOUNT QUERY -> 접수 안 됨: 만료 시각이 이미 지났음
--- 단계 2: 점검 - 요청서 리스트
```

`status` 철자를 `"reviewing"` 이 아니게 쓰면 Exercise 4-2에서 모든 요청서가 「검토 중이 아님」으로 막힙니다. `if reason = ""` 처럼 `=` 한 개를 쓰면 `SyntaxError` 가 납니다.

**관제에서는** — 요청서 리스트는 권한 관리의 첫 기록입니다. 이유 없이 접수하려던 요청 · 사용자 파일에 없는 이름의 요청 · 이미 지난 만료 시각의 요청은 건수를 세어 두고, 같은 사람이 같은 권한을 반복해서 요청하면 역할 설계가 업무와 맞지 않는다는 신호로 봅니다.

---

## Exercise Exercise 4-3 정답

 **터미널에 입력합니다.**

```bash
python day03_3-1_run.py
```

**채운 코드** (한 예)

```python
    if request["status"] != "reviewing":                         # 검토 중이 아니면(이미 처리됐으면)
        return False, "검토 중이 아님"                             # 바꾸지 않고 이유를 알린다
    if request["user"] == approver:                              # 요청한 사람이 스스로 처리하려고 하면
        return False, "본인 요청은 처리할 수 없음"                  # 바꾸지 않고 이유를 알린다
    request["status"] = "approved"                               # 상태를 승인됨으로 바꾼다
    request["approver"] = approver                               # 누가 승인했는지 적어 둔다
    return True, "승인"                                          # 승인했다고 알린다
```

`reject_request` 는 미리 채워진 두 검사 아래 부분입니다.

```python
    request["status"] = "rejected"                               # 상태를 반려됨으로 바꾼다
    request["approver"] = approver                               # 누가 반려했는지 적어 둔다
    return True, "반려"                                          # 반려했다고 알린다
```

**결과**

- (가) 출력은 다음과 같고, 막힌 세 줄은 이렇습니다. 맨 위 `1 본인 승인` 은 요청자 seoyeon 이 자기 1번 요청을 승인하려 해서 `본인 요청은 처리할 수 없음` 입니다. 처리 여섯 건 중 `1 승인` 이 두 번째 나온 줄은 이미 승인된 1번이고, `2 승인` 은 이미 반려된 2번이라 둘 다 `검토 중이 아님` 입니다.

```
--- 단계 1: 처리 - 본인 요청 시험 한 건, 승인 · 반려 여섯 건을 처리한다
1 본인 승인 -> False 본인 요청은 처리할 수 없음
1 승인 -> True 승인
2 반려 -> True 반려
3 승인 -> True 승인
4 승인 -> True 승인
1 승인 -> False 검토 중이 아님
2 승인 -> False 검토 중이 아님
--- 단계 2: 점검 - 요청서 리스트
1 seoyeon approved security_manager
2 gaeun rejected security_manager
3 dami approved security_manager
4 junho approved security_manager
```

- (나) 이미 승인한 요청서를 다시 승인하지 못하게 막는 이유는, 처리가 끝난 요청이 다시 처리되면 같은 요청이 두 번 부여되거나(예외가 중복으로 생김), 승인한 기록이 나중에 바뀌어 감사 기록을 믿을 수 없게 되기 때문입니다. 반려한 요청서를 나중에 승인으로 바꿀 수 있으면 「반려」라는 결정의 의미가 없어집니다. 번복이 필요하면 상태를 고치지 말고 새 요청서를 접수합니다.
- (다) ① 이 검사가 없으면 요청자가 자기 요청을 스스로 승인해, 아무도 확인하지 않은 요청이 통과합니다. ② 이 검사만으로는 요청자가 친구 계정이나 다른 사람에게 부탁해 대신 승인하게 하는 것을 막지 못합니다. 더 필요한 장치의 예: 계정 관리처럼 위험한 권한은 승인자를 두 명으로 하고(이중 승인), 승인자를 요청자와 다른 부서의 정해진 사람으로 두고, 승인 이력을 정기적으로 대조합니다. 근거가 있으면 맞습니다.

**왜** — 상태는 정해진 순서로만 바꿔야 요청서 하나의 처리 순서를 따라갈 수 있습니다. 「바꾸기 전에 지금 상태를 먼저 확인」하는 한 줄이 같은 요청의 중복 처리와 결정 번복을 함께 막습니다. 처리한 사람을 적어 두면 책임이 분명해집니다.

**자주 틀리는 곳** — 상태 확인을 `==` 로 써서(`if request["status"] == "reviewing": return False, …`) 거꾸로 동작하는 경우가 있습니다. 모든 처리가 「검토 중이 아님」으로 막히거나 이미 처리한 것만 통과합니다. `request["status"] = "approved"` 줄을 빼먹으면 `True` 는 나오는데 상태가 그대로라서 같은 요청서를 또 승인해도 통과합니다. 본인 요청 검사를 `==` 대신 `!=` 로 거꾸로 쓰면 security_manager 의 정상 처리가 모두 막힙니다. 실행하면 다음처럼 됩니다(`1 승인 -> True 승인` 줄이 두 번 나오면 상태를 안 바꾼 것입니다).

```
--- 단계 1: 처리 - 본인 요청 시험 한 건, 승인 · 반려 여섯 건을 처리한다
1 본인 승인 -> False 본인 요청은 처리할 수 없음
1 승인 -> True 승인
2 반려 -> True 반려
3 승인 -> True 승인
4 승인 -> True 승인
1 승인 -> True 승인
2 승인 -> False 검토 중이 아님
--- 단계 2: 점검 - 요청서 리스트
1 seoyeon reviewing security_manager
2 gaeun rejected security_manager
3 dami reviewing security_manager
4 junho reviewing security_manager
```

**관제에서는** — 승인 · 반려 이력에 요청서 번호 · 처리한 사람 · 처리 시각을 남기고, 같은 요청서에 두 번째 처리 시도가 있었다면 실수인지 조작인지 확인합니다. 승인자와 요청자가 같은 요청서가 있는지 정기적으로 대조합니다.

---

## Exercise Exercise 4-3 정답

 **터미널에 입력합니다.**

```bash
python day03_4-1_run.py
```

**채운 코드** (한 예)

```python
    if request["status"] != "approved":                          # 승인된 요청서가 아니면
        return False, "승인되지 않음"                              # 부여하지 않고 이유를 알린다
    user = request["user"]                                       # 요청자
    resource = request["resource"]                               # 자원
    action = request["action"]                                   # 행위
    is_allowed, judge_reason = check_permission(user, resource, action)  # 요청자를 지금 정책으로 판정한다
    if is_allowed or judge_reason != "권한 없음":                                # 이미 허용이거나, 사람 자체가 거부 대상이면
        return False, f"부여하지 않음({judge_reason})"                    # 부여하지 않고 판정 이유를 알린다
    exception_id = len(EXCEPTIONS) + 1                           # 다음 예외 번호(지금 개수 + 1)
    exception = {                                                # 요청서 내용으로 예외 한 건을 만든다
        "id": exception_id,                                      # 예외 번호
        "user": request["user"],                                 # 대상 사용자
        "permission": request["permission"],                     # 권한
        "expires": request["until"],                             # 만료 시각(요청서의 희망 만료 시각)
        "reason": request["reason"],                             # 이유
    }
    EXCEPTIONS.append(exception)                                 # 예외 리스트에 추가한다
    request["exception_id"] = exception["id"]                    # 어느 예외를 부여했는지 요청서에 적어 둔다
    request["status"] = "granted"                                # 상태를 부여됨으로 바꾼다
    return True, "부여"                                          # 부여했다고 알린다
```

**결과**

- (가) 출력은 다음과 같고, 부여를 시도한 네 건의 결과는 이렇습니다(`부여된 예외 번호: 6` 줄은 1번 요청서에 적힌 예외 번호입니다). 1번 seoyeon 은 **부여됨**(예외 6번), 2번 gaeun 은 **부여 안 함**(반려된 요청서라 「승인되지 않음」), 3번 dami 는 **부여 안 함**(퇴사한 계정), 4번 junho 는 **부여 안 함**(이미 허용된 권한).

```
--- 단계 1: 판정 - 부여 전
1 seoyeon SETTLE:QUERY -> False 권한 없음
2 gaeun SALES:QUERY -> False 권한 없음
3 dami SALES:QUERY -> False 퇴사한 계정
4 junho SETTLE:QUERY -> True 역할 권한
--- 단계 2: 부여 - 요청서마다 부여를 시도한다
1 seoyeon granted -> True 부여
2 gaeun rejected -> False 승인되지 않음
3 dami approved -> False 부여하지 않음(퇴사한 계정)
4 junho approved -> False 부여하지 않음(허용)
부여된 예외 번호: 6
--- 단계 3: 점검 - 부여 후
1 seoyeon SETTLE:QUERY -> True 예외 6번
2 gaeun SALES:QUERY -> False 권한 없음
3 dami SALES:QUERY -> False 퇴사한 계정
4 junho SETTLE:QUERY -> True 역할 권한
```

- (나) 승인자는 사람이라서 요청자가 이미 퇴사했는지를 모르고 승인할 수 있습니다. 코드는 지금 사용자 파일과 역할 파일로 판정하므로 퇴사한 계정을 확실히 거릅니다. 승인자의 확인은 「이 요청이 업무에 맞는가」를 판단하고, 코드의 확인은 「이 사람이 지금 정책상 부여를 받을 수 있는 사람인가」를 판단합니다. 둘은 보는 것이 다르므로 함께 써야 합니다. 이 확인이 없으면 퇴사자에게 예외가 만들어져 리스트에 남습니다.
- (다) 요청서의 `until`(2026-10-27 18:00)이 그대로 예외의 `expires` 가 되었습니다. 그 시각이 지나면 어제의 `find_exception` 이 `now < expires` 를 거짓으로 판정해 예외를 쓰지 않으므로 요청자는 다시 「권한 없음」으로 거부됩니다. 다만 만료된 예외가 `EXCEPTIONS` 에 계속 남으므로, 어제 만든 회수 점검(만료됨 · 퇴사자)을 매일 돌려 리스트에서 정리 대상으로 뽑고 회수 이력을 남깁니다. 점검 담당과 주기(예: 보안 담당이 매일 아침)를 정해 두면 맞습니다.

**왜** — 승인과 부여 사이에 정책 확인을 두면, 사람의 승인이 정책 확인 없이 곧바로 부여로 이어지지 않습니다. 부여를 어제 만든 예외 권한으로 처리한 덕분에 새 판정 규칙을 만들 필요가 없고, 만료 시각도 그대로 적용됩니다. 「이미 허용이면 부여하지 않는다」는 규칙은 역할로 이미 가진 권한이 예외로 또 쌓이는 것을 막습니다.

**자주 틀리는 곳** — `check_permission` 의 결과를 확인하지 않고 바로 부여하면 퇴사자와 이미 권한이 있는 사람에게도 예외가 만들어집니다. 실행하면 다음처럼 3번과 4번도 `granted` 가 됩니다. 단계 3의 판정은 어제의 「사람 먼저 검사」가 막아 주지만, 쓸모없는 예외가 리스트에 남고 이후 회수 점검에도 걸립니다.

```
--- 단계 1: 판정 - 부여 전
1 seoyeon SETTLE:QUERY -> False 권한 없음
2 gaeun SALES:QUERY -> False 권한 없음
3 dami SALES:QUERY -> False 퇴사한 계정
4 junho SETTLE:QUERY -> True 역할 권한
--- 단계 2: 부여 - 요청서마다 부여를 시도한다
1 seoyeon granted -> True 부여
2 gaeun rejected -> False 승인되지 않음
3 dami granted -> True 부여
4 junho granted -> True 부여
부여된 예외 번호: 6
부여된 예외 번호: 7
부여된 예외 번호: 8
--- 단계 3: 점검 - 부여 후
1 seoyeon SETTLE:QUERY -> True 예외 6번
2 gaeun SALES:QUERY -> False 권한 없음
3 dami SALES:QUERY -> False 퇴사한 계정
4 junho SETTLE:QUERY -> True 역할 권한
```

`is_allowed or judge_reason != "권한 없음"` 을 `and` 로 쓰면 거의 모든 경우에 부여 쪽으로 넘어갑니다. `EXCEPTIONS` 에 추가한 뒤 `request["status"]` 를 바꾸지 않으면 같은 요청서가 두 번 부여됩니다.

**관제에서는** — 오늘 요청서에 적은 `exception_id` 가 「이 예외는 어느 요청에서 나왔나」를 찾는 연결 정보입니다. 부여한 시각과 승인자까지 함께 남기면 감사에서 그대로 보여 줄 수 있습니다. 승인은 됐는데 부여가 막힌 요청서는 따로 모아 승인자에게 알립니다. 반복해서 부여되는 같은 권한은 예외를 계속 만들 것이 아니라 역할을 고쳐야 한다는 신호입니다.

---

## 앞 Exercise 파일 완성본

앞 Exercise 파일을 못 만들고 다음 Exercise로 넘어가야 할 때 그대로 만들어 씁니다. 정답 본문을 함수 머리말과 합친 전체 파일입니다.

**`req_create.py`** (Exercise 4-1 완성본)

```python
from rbac import USERS                                           # 10/21(수)에 만든 사용자 딕셔너리를 불러온다

REQUESTS = []                                                    # 접수한 요청서를 모아 두는 리스트(프로그램이 끝나면 사라진다)


def create_request(user, resource, action, until, reason, received_at):  # 요청자 · 자원 · 행위 · 희망 만료 시각 · 이유 · 접수 시각을 받는 함수
    """권한 요청서를 만들어 REQUESTS 에 넣고 (True, 요청서)를 리턴한다.
    직원이 권한을 요청할 때 쓰며, 접수할 수 없으면 (False, 이유)를 리턴한다.
    """
    if user not in USERS:                                        # 사용자 파일에 없는 이름이면
        return False, "등록되지 않은 사용자"                       # 접수하지 않고 이유를 알린다
    if reason == "":                                             # 이유가 비어 있으면
        return False, "이유가 없음"                                # 접수하지 않고 이유를 알린다
    if until <= received_at:                                             # 희망 만료 시각이 접수 시각보다 늦지 않으면(같은 형식의 문자열은 앞에서부터 비교해도 시각 순서와 같다)
        return False, "만료 시각이 이미 지났음"                     # 접수하지 않고 이유를 알린다
    request_id = len(REQUESTS) + 1                               # 다음 요청 번호(지금 개수 + 1)
    permission = f"{resource}:{action}"                          # "자원:행위" 모양 권한 문자열
    request = {                                                  # 요청서 한 장. 상태는 검토 중으로 시작한다
        "id": request_id,                                        # 요청 번호
        "user": user,                                            # 요청자
        "resource": resource,                                    # 자원
        "action": action,                                        # 행위
        "permission": permission,                                # 권한
        "until": until,                                          # 희망 만료 시각
        "reason": reason,                                        # 요청 이유
        "requested_at": received_at,                             # 접수 시각
        "status": "reviewing",                                   # 상태: 검토 중
    }
    REQUESTS.append(request)                                     # 요청서 리스트 끝에 추가한다
    return True, request                                         # 접수했다고 알리고 요청서를 리턴한다
```

**`req_review.py`** (Exercise 4-2 완성본)

```python
def approve_request(request, approver):                          # 요청서와 승인자 이름을 받는 함수
    """검토 중인 요청서를 승인한다.
    보안 담당자가 권한 요청을 처리할 때 쓰고 (성공 여부, 이유)를 리턴한다.
    """
    if request["status"] != "reviewing":                         # 검토 중이 아니면(이미 처리됐으면)
        return False, "검토 중이 아님"                             # 바꾸지 않고 이유를 알린다
    if request["user"] == approver:                              # 요청한 사람이 스스로 처리하려고 하면
        return False, "본인 요청은 처리할 수 없음"                  # 바꾸지 않고 이유를 알린다
    request["status"] = "approved"                               # 상태를 승인됨으로 바꾼다
    request["approver"] = approver                               # 누가 승인했는지 적어 둔다
    return True, "승인"                                          # 승인했다고 알린다


def reject_request(request, approver):                           # 요청서와 반려하는 사람 이름을 받는 함수
    """검토 중인 요청서를 반려한다.
    보안 담당자가 권한 요청을 거절할 때 쓰며 (성공 여부, 이유)를 리턴한다.
    """
    if request["status"] != "reviewing":                         # 검토 중이 아니면(이미 처리됐으면)
        return False, "검토 중이 아님"                             # 바꾸지 않고 이유를 알린다
    if request["user"] == approver:                              # 요청한 사람이 스스로 처리하려고 하면
        return False, "본인 요청은 처리할 수 없음"                  # 바꾸지 않고 이유를 알린다
    request["status"] = "rejected"                               # 상태를 반려됨으로 바꾼다
    request["approver"] = approver                               # 누가 반려했는지 적어 둔다
    return True, "반려"                                          # 반려했다고 알린다
```

**`req_grant.py`** (Exercise 4-3 완성본)

```python
from rbac import check_permission                                # 10/21(수)에 만든 역할 판정 함수를 불러온다
from exception_policy import EXCEPTIONS                          # 10/22(목)에 만든 예외 리스트를 불러온다


def grant_request(request):                                      # 요청서를 받는 함수
    """승인된 요청서를 정책으로 한 번 더 확인하고 통과하면 예외 권한을 부여한다.
    승인 뒤 실제로 권한을 줄 때 쓰며 (성공 여부, 이유)를 리턴한다.
    """
    if request["status"] != "approved":                          # 승인된 요청서가 아니면
        return False, "승인되지 않음"                              # 부여하지 않고 이유를 알린다
    user = request["user"]                                       # 요청자
    resource = request["resource"]                               # 자원
    action = request["action"]                                   # 행위
    is_allowed, judge_reason = check_permission(user, resource, action)  # 요청자를 지금 정책으로 판정한다
    if is_allowed or judge_reason != "권한 없음":                                # 이미 허용이거나, 사람 자체가 거부 대상이면
        return False, f"부여하지 않음({judge_reason})"                    # 부여하지 않고 판정 이유를 알린다
    exception_id = len(EXCEPTIONS) + 1                           # 다음 예외 번호(지금 개수 + 1)
    exception = {                                                # 요청서 내용으로 예외 한 건을 만든다
        "id": exception_id,                                      # 예외 번호
        "user": request["user"],                                 # 대상 사용자
        "permission": request["permission"],                     # 권한
        "expires": request["until"],                             # 만료 시각(요청서의 희망 만료 시각)
        "reason": request["reason"],                             # 이유
    }
    EXCEPTIONS.append(exception)                                 # 예외 리스트에 추가한다
    request["exception_id"] = exception["id"]                    # 어느 예외를 부여했는지 요청서에 적어 둔다
    request["status"] = "granted"                                # 상태를 부여됨으로 바꾼다
    return True, "부여"                                          # 부여했다고 알린다
```
