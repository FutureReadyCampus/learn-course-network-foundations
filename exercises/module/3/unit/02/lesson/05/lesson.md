---
id: m3-u02-l05
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

**실습 2-2를 마친 뒤** 이 레슨의 파일 하나를 만듭니다. 요청서 흐름은 접수 → 승인 · 반려 → **부여** 순서인데, 마지막 부여 함수 `grant_request` 는 도전 2-1에서 만드는 것이라 오늘은 완성본을 받아 씁니다.

1. 파일은 `access_control` 폴더 안에 만듭니다. 만드는 방법은 실습 2-1과 같습니다(VS Code 왼쪽 목록에서 `access_control` 폴더를 고르고 **새 파일** 아이콘).
2. 아래 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 만들 파일은 `req_grant.py` 하나입니다. 승인된(`approved`) 요청서를 받아 `rbac.py` 의 `check_permission` 으로 지금 정책을 한 번 더 확인하고, 「권한 없음」일 때만 `exception_policy.py` 의 `EXCEPTIONS` 에 예외 한 건을 추가합니다. 그다음 요청서의 상태를 `granted` 로 바꿉니다.
4. 파일을 만들었으면 터미널에서 불러지는지 확인합니다. `제공 파일 정상` 이 나오면 됩니다(맥북은 `python3`).
   ```bash
   python -c "from req_grant import grant_request; print('제공 파일 정상')"
   ```
5. 오늘 핵심 실습에서는 이 파일을 실행하지 않습니다. 도전 2-3이 이 파일을 불러 쓰고, 「이번 Unit 마무리」에서 다른 파일과 함께 깃허브에 올립니다.

> 시간이 남아 도전 2-1을 하면, 이 파일을 빈칸이 있는 골격으로 바꿔 직접 써 봅니다. 다 쓴 뒤 `challenge2-1_run.py` 의 출력이 도전 2-1 정답과 같으면 이 완성본과 같게 동작하는 것입니다.

## `req_grant.py` 만들기

**`req_grant.py`** 를 만들고 아래 내용을 붙여 넣습니다. 함수가 하는 일은 앞 페이지 3번과 같고, 주석에 줄마다 하는 일이 적혀 있습니다.

```python
from rbac import check_permission                                # rbac.py 의 역할 판정 함수를 불러온다
from exception_policy import EXCEPTIONS                          # exception_policy.py 의 예외 리스트를 불러온다


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
