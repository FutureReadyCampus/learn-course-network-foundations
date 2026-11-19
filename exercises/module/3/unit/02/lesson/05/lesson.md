---
id: m3-u02-l05
title: 제공 파일
render: markdown
---

# 제공 파일

## `req_grant.py` 만들기

**`req_grant.py`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.

```python
from rbac import check_permission                                # Unit 1에서 만든 역할 판정 함수를 불러온다
from exception_policy import EXCEPTIONS                          # Unit 1에서 만든 예외 리스트를 불러온다


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
