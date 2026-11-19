---
id: m3-u04-l02
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

**실습 4-1을 시작하기 전에** 이 레슨의 파일 두 개를 만듭니다. 실습 4-1과 실습 4-2는 회수 대상 8건과 그 회수 계획에서 출발하는데, 그 둘을 만드는 코드는 오늘 직접 쓰지 않고 완성본을 받아 씁니다.

1. 파일은 모두 `access_control` 폴더 안에 만듭니다(VS Code 왼쪽 목록에서 `access_control` 폴더를 오른쪽 클릭 › **New File**).
2. 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 만들 파일은 두 개입니다.
   1. `revoke_input.py`: Unit 3 점검 결과인 회수 대상 8건을 리스트로 돌려주는 함수 `load_to_revoke`. 시작하기 레슨의 확인 결과에 따라 두 코드 중 하나를 고릅니다.
   2. `revoke_plan.py`: 회수 대상마다 회수 방법 · 지울 대상 · 영향을 적은 회수 계획을 만드는 함수 `plan_revocation`
4. 두 파일을 다 만들었으면 아래 명령으로 확인하고 실습 4-1로 갑니다(맥북은 `python3`).
   ```bash
   python -c "from rbac import USERS, ROLES; from revoke_input import load_to_revoke; from revoke_plan import plan_revocation; print('제공 파일 정상', len(plan_revocation(load_to_revoke(), USERS, ROLES)))"
   ```
   - `제공 파일 정상 8` 이 나오면 됩니다.

> 시간이 남아 도전 4-1을 하면, `revoke_plan.py` 를 빈칸이 있는 골격으로 바꿔 직접 써 봅니다. 그때는 다 채울 때까지 실습 4-1 · 4-2가 동작하지 않으니, 다 쓴 뒤 `exercise4-2_run.py` 를 다시 실행해 결과가 같은지 확인합니다.

## `revoke_input.py` 만들기

**`revoke_input.py`** 를 만들고, 아래 두 코드 중 **하나만** 붙여 넣습니다. 어느 쪽이든 `load_to_revoke()` 가 같은 회수 대상 8건을 돌려줍니다.

1. 시작하기 레슨에서 `Unit 3 파일 정상 14 7 3` 이 나왔다면 첫 번째 코드(Unit 3 파일이 있을 때)를 씁니다. Unit 3 점검을 같은 방법으로 다시 해서 8건을 만듭니다.
2. 오류가 났거나 숫자가 달랐다면 두 번째 코드(Unit 3 파일이 없을 때)를 씁니다. 8건이 코드 안에 그대로 적혀 있습니다.

회수 대상 한 건은 `user` · `permission` · `source`(권한을 받은 방식: 「역할 sales」 또는 「예외 3번」) · `employed`(재직 여부) · `reasons`(Unit 3 점검에서 나온 이유의 리스트)를 담은 딕셔너리입니다.

**Unit 3 파일이 있을 때**

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from review_list import build_access_list                        # 실습 3-1의 현황 함수를 불러온다
from review_rules import find_stale                              # Unit 3 제공 파일의 규칙 점검 함수를 불러온다
from review_unused import load_last_used, find_unused            # 실습 3-2의 안 쓴 권한 점검 함수를 불러온다
from overprivilege import generate_report                        # Unit 3 제공 파일의 리포트 함수를 불러온다
from report_exclude import load_exclude_map, split_by_exclude    # Unit 3 제공 파일의 회수 제외 함수를 불러온다

REVIEW_TIME = datetime.strptime("2026-10-29 14:00", "%Y-%m-%d %H:%M")   # Unit 3 점검 시각(고정). 같은 결과를 얻으려고 그 시각을 쓴다
TIME_FORMAT = "%Y-%m-%d %H:%M"                                   # 시각 문자열의 형식


def load_to_revoke():                                            # Unit 3 점검 결과를 다시 만드는 함수
    """Unit 3 점검에서 나온 「회수 대상」 리스트(8개)를 리턴한다.
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

**Unit 3 파일이 없을 때**

```python
# Unit 3 파일이 없을 때 쓰는 revoke_input.py 입니다. Unit 3 점검 결과인 「회수 대상」 8건을 그대로 담았습니다.
# review_list.py 같은 Unit 3 파일이 없어도 오늘 실습을 똑같이 따라올 수 있습니다. 그대로 붙여 넣고 고치지 않습니다.


def load_to_revoke():                                            # Unit 3 점검 결과(회수 대상)를 리턴하는 함수
    """Unit 3 점검에서 나온 「회수 대상」 리스트(8개)를 리턴한다.
    회수 계획을 세우기 전에 회수할 권한을 준비할 때 쓴다.
    """
    to_revoke = [                                                # 회수 대상 8건(역할로 받은 3건 + 예외로 받은 5건)
        {"user": "junho", "permission": "SALES:QUERY", "source": "역할 finance", "employed": True, "reasons": ["90일 넘게 안 씀(이력 없음 포함)"]},
        {"user": "dami", "permission": "SALES:QUERY", "source": "역할 sales", "employed": False, "reasons": ["퇴사한 계정"]},
        {"user": "dami", "permission": "SALES:CHANGE", "source": "역할 sales", "employed": False, "reasons": ["퇴사한 계정", "90일 넘게 안 씀(이력 없음 포함)"]},
        {"user": "seoyeon", "permission": "SETTLE:QUERY", "source": "예외 1번", "employed": True, "expires": "2026-10-22 18:00", "reasons": ["만료된 예외", "90일 넘게 안 씀(이력 없음 포함)"]},
        {"user": "junho", "permission": "SALES:CHANGE", "source": "예외 2번", "employed": True, "expires": "2026-10-20 18:00", "reasons": ["만료된 예외", "90일 넘게 안 씀(이력 없음 포함)"]},
        {"user": "dami", "permission": "SALES:QUERY", "source": "예외 3번", "employed": False, "expires": "2026-10-31 18:00", "reasons": ["퇴사한 계정"]},
        {"user": "batch-night", "permission": "SALES:QUERY", "source": "예외 4번", "employed": True, "expires": "2026-10-23 09:00", "reasons": ["만료된 예외", "90일 넘게 안 씀(이력 없음 포함)"]},
        {"user": "gaeun", "permission": "SETTLE:QUERY", "source": "예외 5번", "employed": True, "expires": "2026-10-22 12:00", "reasons": ["만료된 예외", "90일 넘게 안 씀(이력 없음 포함)"]},
    ]
    return to_revoke                                             # 회수 대상 리스트를 리턴한다
```

- 점검 시각은 `2026-10-29 14:00` 으로 고정했습니다. 날짜가 바뀌어도 같은 8건이 나오게 하려는 것입니다.

## `revoke_plan.py` 만들기

**`revoke_plan.py`** 를 만들고 아래 내용을 붙여 넣습니다. 회수 대상을 하나씩 보고 회수 방법을 정해 **회수 계획** 리스트를 돌려줍니다. 계획만 세우고 실제로는 아무것도 지우지 않습니다.

회수 방법은 권한을 받은 방식으로 정합니다.

1. 예외로 받은 권한 → **예외 삭제**: 지울 대상은 예외 번호, 영향은 1건
2. 퇴사한 사용자가 역할로 받은 권한 → **역할 해제**(그 사용자의 `role` 을 비움): 지울 대상은 사용자 이름, 영향은 그 역할에 든 권한 수
3. 재직 중인 사용자가 역할로 받은 권한 → **역할에서 권한 빼기**: 지울 대상은 역할 이름, 영향은 그 역할을 가진 사용자 수

계획 한 건은 회수 대상 한 건에 `method`(회수 방법) · `target`(지울 대상) · `impact`(영향: 이 회수로 사라지는 권한 수) 키를 더한 딕셔너리입니다.

```python
def exception_id(source):                                        # "예외 3번" 모양 문자열을 받는 함수
    """문자열 「예외 3번」에서 예외 번호(3)를 숫자로 꺼낸다.
    회수 대상의 받은 방식(「예외 3번」)에서 지울 예외 번호를 꺼낼 때 쓴다.
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

- 오늘 데이터에서는 예외 삭제 5건, 역할 해제 2건(dami, 영향 2), 역할에서 권한 빼기 1건(junho 의 `SALES:QUERY`, 영향 1)이 나옵니다.
- 방법을 고르는 순서와 영향을 세는 방법은 도전 4-1 레슨에서 자세히 다룹니다.
