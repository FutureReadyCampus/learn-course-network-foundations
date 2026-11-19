---
id: m3-u04-l04
title: 제공 파일
render: markdown
---

# 제공 파일

## `revoke_input.py` 만들기

**`revoke_input.py`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from review_list import build_access_list                        # 실습 3-1에서 만든 현황 함수를 불러온다
from review_rules import find_stale                              # 도전 3-1에서 만든 규칙 점검 함수를 불러온다
from review_unused import load_last_used, find_unused            # 실습 3-2에서 만든 안 쓴 권한 점검 함수를 불러온다
from overprivilege import generate_report                        # 도전 3-2에서 만든 리포트 함수를 불러온다
from report_exclude import load_exclude_map, split_by_exclude    # 도전 3-3에서 만든 회수 제외 함수를 불러온다

REVIEW_TIME = datetime.strptime("2026-10-29 14:00", "%Y-%m-%d %H:%M")   # Unit 3에서 점검한 시각(고정). 같은 결과를 얻으려고 그 시각을 쓴다
TIME_FORMAT = "%Y-%m-%d %H:%M"                                   # 시각 문자열의 형식


def load_to_revoke():                                            # Unit 3의 점검 결과를 다시 만드는 함수
    """Unit 3의 점검에서 나온 「회수 대상」 리스트(8개)를 리턴한다.
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

## `revoke_plan.py` 만들기

**`revoke_plan.py`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.

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
