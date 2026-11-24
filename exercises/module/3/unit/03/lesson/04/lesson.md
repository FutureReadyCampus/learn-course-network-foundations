---
id: m3-u03-l04
title: 핵심 실습 점검 함수 준비
render: markdown
---

# 핵심 실습 점검 함수 준비

## `review_rules.py`가 필요한 이유

실습 3-2는 사용 이력을 보기 전에 퇴사한 계정과 만료된 예외 권한을 먼저 제외합니다. 이 기준을 `find_stale` 함수로 구현해 `review_rules.py`에 둡니다. 다음 Lesson의 핵심 실습이 이 함수를 불러 쓰므로, 응용 문제를 하지 않아도 진행할 수 있습니다.

1. VS Code에서 `access_control` 폴더를 선택하고 새 파일 `review_rules.py`를 만듭니다.
2. 아래 코드를 붙여 넣고 저장합니다.

```python
from datetime import datetime

from exception_policy import TIME_FORMAT


def find_stale(access_list, now):
    """퇴사했거나 만료된 권한을 이유와 함께 돌려준다."""
    stale = []

    for entry in access_list:
        expires = entry.get("expires")
        reason = ""

        if not entry["employed"]:
            reason = "퇴사한 계정"
        elif expires is not None:
            expires_at = datetime.strptime(expires, TIME_FORMAT)
            if expires_at <= now:
                reason = "만료된 예외"

        if reason:
            stale_entry = entry.copy()
            stale_entry["reason"] = reason
            stale.append(stale_entry)

    return stale
```

- 역할 권한에는 `expires`가 없으므로 `entry.get("expires")`로 읽습니다. 값이 없으면 `None`이 됩니다.
- 만료 시각은 예외 권한에만 있으므로 `expires is not None`일 때만 시각으로 바꿉니다.
- 원래 현황을 바꾸지 않도록 `entry.copy()`로 복사한 뒤 이유를 더합니다.

<!-- checklist -->
- [ ] `review_rules.py`를 만들고 저장했다
<!-- /checklist -->
