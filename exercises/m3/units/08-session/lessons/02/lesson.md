---
id: m3-u08-l02
title: Exercise 8-1 · 회수 대상의 회수 계획 세우기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/090_day05_am_revoke.md
  mission_id: GichanSource.m3-1030-am-revoke
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 8-1 · 회수 대상의 회수 계획 세우기

## 개요

> **오늘 들어온 일**
>
> A사 관제 담당이 보낸 메시지:
> 「어제 점검 결과에서 회수할 권한이 8건 나왔습니다. 그런데 바로 지워도 되는지 걱정됩니다. 예외로 받은 권한은 그 예외만 지우면 되지만, 역할로 받은 권한은 같은 역할을 가진 다른 사람에게도 영향이 갈 수 있기 때문입니다.
>
> 지우기 전에 8건을 어떤 방법으로 회수할지, 그 회수로 몇 건의 권한이 사라지는지를 먼저 리스트로 보여 주세요.」
> - **왜 중요한가**: 권한을 잘못 지우면 일하던 사람이 갑자기 접근하지 못합니다. 지우기 전에 방법과 영향을 먼저 확인하면 실수를 줄일 수 있습니다.

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「 문제」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 읽기 · 앞 수업 흐름 복습

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

| 날짜 | 한 일 | 오늘 이어지는 것 |
|---|---|---|
| 10/29(목) | 현황 리스트 → 규칙(퇴사 · 만료)과 사용 이력(권한을 마지막으로 쓴 시각의 기록. 90일)으로 후보 찾기 → 후보 10건에서 회수 제외 2건을 뺌 | 회수 대상 8건(`load_to_revoke` 가 리턴하는 리스트, 코드에서는 `findings`). 회수 제외 리스트의 3건 중 dami 의 권한은 「퇴사한 계정」이라 제외하지 않아, 실제 제외는 gaeun 의 `ACCOUNT:CHANGE` · seoyeon 의 `SALES:CHANGE` 2건입니다. |
| 10/22(목) | 역할 부여 · 퇴사 처리(`revoke_access`), 예외 만료, 최종 판정 `evaluate_access` | 오늘 Exercise 8-3의 회수 확인에 다시 씀 |

## 읽기 · 왜 회수 계획이 필요한가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 점검에서 찾은 8건은 「회수해야 할 권한」입니다. 하지만 권한을 받은 방식에 따라 회수 방법이 다르고, 방법에 따라 영향받는 사람이 다릅니다.
2. 권한을 받은 방식에 따라 지우는 대상이 다릅니다.
   - **예외로 받은 권한**은 그 예외 한 건만 지우면 됩니다.
   - **역할로 받은 권한**은 사용자의 역할을 해제하거나, 역할 자체에서 그 권한을 빼야 합니다.
     - 역할에서 권한을 빼면 그 역할을 가진 **모든 사용자**가 권한을 잃습니다.
3. 그래서 지우기 전에 방법과 영향을 정리한 **회수 계획**을 먼저 만듭니다. 계획은 실제로는 아무것도 지우지 않는 미리보기(dry-run · 드라이 런)입니다.

## 읽기 · 1.1 회수 방법과 영향 범위

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

- **회수 방법**은 권한을 없애려고 **어느 데이터를 고칠지**입니다.
  - 권한은 두 길로 받습니다. 예외(`EXCEPTIONS`)로 받거나, 사용자의 역할(`USERS` 의 `role` 이 가리키는 `ROLES`)로 받습니다.
  - 그래서 방법은 **예외 삭제 · 역할 해제 · 역할에서 권한 빼기** 세 가지입니다.
- **영향**(impact · 임팩트)은 이 회수로 사용자들이 잃는 권한을 하나씩 센 수입니다(예: dami 가 권한 2개를 잃으면 2).
- **오늘 쓰는 데이터의 모양**
  - `USERS`: `{"seoyeon": {"role": "sales", "employed": True}, "junho": {"role": "finance", "employed": True}, "dami": {"role": "sales", "employed": False}, …}`
  - `ROLES`: `{"sales": ["SALES:QUERY", "SALES:CHANGE"], "finance": ["SALES:QUERY", "SETTLE:QUERY"], …}` (역할 이름 → 권한 리스트)
  - `EXCEPTIONS`: 예외 한 건은 `{"id": 3, "user": "dami", "permission": "SALES:QUERY", …}` 모양입니다.
  - `findings`: 회수 대상 8건의 리스트이고, `finding` 은 그 한 건입니다.
    - `finding` 한 건에는 `user` · `permission` · `source`(권한을 받은 경로: 「예외 3번」 또는 「역할 sales」) · `reasons`(어제 점검에서 나온 이유의 리스트)가 들어 있습니다.
    - 회수 대상은 (사용자, 권한, 받은 경로)마다 한 건이라, 같은 방법의 계획이 여러 건 나올 수 있습니다(dami 의 역할 해제 2건).

**방법 ① 예외 삭제 — 예외로 받은 권한**

- **상황**: dami 가 예외 3번으로 `SALES:QUERY` 를 받았습니다.
- **하는 일**: `EXCEPTIONS` 리스트에서 번호가 3인 예외를 지웁니다.
- **사라지는 것**: 예외로 받은 그 권한 1개라서 **영향 1**입니다. dami 는 같은 권한을 `sales` 역할로도 받지만, 그쪽은 방법 ②에서 따로 회수합니다.
- **지울 대상**(`target`): 예외 번호 3
- **왜 이 방법인가**: 예외 한 건에만 들어 있는 권한이라 그 예외만 지우면 됩니다.

**방법 ② 역할 해제 — 퇴사한 사용자가 역할로 받은 권한**

- **상황**: dami 는 퇴사했고, 역할 `sales` 로 `SALES:QUERY` · `SALES:CHANGE` 를 받았습니다.
- **하는 일**: `USERS` 에서 dami 의 `role` 을 빈 문자열(`""`)로 바꿉니다. dami 는 어떤 역할의 권한도 받지 않게 됩니다.
- **사라지는 것**: dami 가 `sales` 로 받던 권한 2개가 모두 사라져서 **영향 2**입니다.
- **지울 대상**(`target`): 사용자 이름 dami
- **왜 이 방법인가**: 퇴사한 사람은 어떤 권한도 필요 없어서 역할째로 끊습니다. `sales` 역할에서 권한을 빼면 재직 중인 seoyeon 도 그 권한을 잃으므로, 역할이 아니라 dami 의 `role` 만 비웁니다.

**방법 ③ 역할에서 권한 빼기 — 재직 중인 사용자가 역할로 받은 권한**

- **상황**: 재직 중인 junho 가 역할 `finance` 로 `SALES:QUERY` 를 받았습니다.
- **하는 일**: `ROLES` 의 `finance` 권한 리스트에서 `SALES:QUERY` 를 뺍니다.
- **사라지는 것**: `finance` 역할을 가진 사용자 모두가 그 권한을 잃습니다. 오늘은 junho 1명이라 **영향 1**입니다.
- **지울 대상**(`target`): 역할 이름 finance
- **왜 이 방법인가**: junho 의 `role` 을 비우면 `finance` 의 다른 권한(`SETTLE:QUERY`)까지 모두 사라지므로, 그 권한만 뺍니다.

- **참고**: 10/22(목)의 `revoke_access` 는 `employed` 만 `False` 로 바꾸고 `role` 은 그대로 두었습니다. 오늘의 역할 해제는 `role` 을 비웁니다.

**어떤 방법을 고르나**

- 아래 「`plan_revocation` 의 흐름」 그림의 두 갈림길로 정합니다.
  - 예외로 받았나? 그렇다 → ① 예외 삭제
  - 아니고, 퇴사한 사용자인가? 그렇다 → ② 역할 해제
  - 그 밖(재직 중인 사용자의 역할 권한) → ③ 역할에서 권한 빼기

**한 장 정리**

| 받은 방식 | 쓰는 방법 | 지울 대상(`target`) | 사라지는 권한 수(`impact`) |
|---|---|---|---|
| 예외로 받음(`source` 가 「예외 N번」) | 예외 삭제 | 예외 번호 N | 1건 |
| 역할로 받음 + 퇴사한 사용자(`employed` 가 `False`) | 역할 해제 | 그 사용자의 이름 | 그 역할에 든 권한 수(dami 의 `sales` 는 2건) |
| 역할로 받음 + 재직 중인 사용자 | 역할에서 권한 빼기 | 역할 이름 | 그 역할을 가진 사용자 수(사용자마다 그 권한 1건) |

- **계획**(`plan`) 한 건: 회수 대상 한 건에 `method`(회수 방법) · `target`(지울 대상) · `impact`(영향) 키를 추가한 딕셔너리입니다.

**`plan_revocation` 의 흐름**

```
+-----------------------------------------+
| plan_revocation(findings, users, roles) |
+-----------------------------------------+
   |
   v
+-------------------------------------+
| plans = []  (계획을 담을 빈 리스트) |
+-------------------------------------+
   |
   v
+---------------------------------------------------------------------+
| role_counts = 역할별 사용자 수 딕셔너리  (반복 전에 한 번만 만든다) |
+---------------------------------------------------------------------+
   |
   v
+---------------------------------------------------------+
| 회수 대상을 하나씩 꺼내 그 사용자의 정보(info)를 꺼낸다 |
+---------------------------------------------------------+
   |
   v
+----------------------------+
| source 에 「예외」가 있나? |
+----------------------------+
   |
   +--> 있다 --> method = 「예외 삭제」 --> 아래 「build_plan」으로
   |
   v  없다
+----------------------------------------------+
| info["employed"] 가 거짓(퇴사한 사용자)인가? |
+----------------------------------------------+
   |
   +--> 그렇다 --> method = 「역할 해제」 --> 아래 「build_plan」으로
   |
   v  아니다   method = 「역할에서 권한 빼기」
+-----------------------------------------------------------------------------------------------------------------------+
| build_plan(finding, method, …) 으로 지울 대상(target)과 영향(impact)을 정한 계획 한 건을 만든다 (영향 계산은 직접 씀) |
+-----------------------------------------------------------------------------------------------------------------------+
   |
   v
+----------------------------------------------------+
| 계획을 plans 에 추가하고 다음 회수 대상으로 (반복) |
+----------------------------------------------------+
   |
   v  모든 회수 대상을 꺼낸 뒤
plans 를 리턴한다
```

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise 8-1 · 회수 대상 8건의 회수 방법과 영향 범위 정하기

** 이런 상황이 있습니다**

- **지금은**: 어제 찾은 회수 대상 8건이 리스트로만 있습니다. 각각 어떤 방법으로 지워야 하는지, 지우면 누가 영향을 받는지는 담당자가 파일을 열어 따져야 합니다.
- **그래서 만드는 것**: `plan_revocation` 입니다.
  - 회수 대상을 하나씩 보고 회수 방법을 정합니다.
  - 예외로 받은 것은 「예외 삭제」, 퇴사한 사용자의 역할 권한은 「역할 해제」, 재직 중인 사용자의 역할 권한은 「역할에서 권한 빼기」입니다.
  - 지울 대상과 영향(사라지는 권한 건수)은 `build_plan` 이 계획에 적습니다.
- **실행하면**: 단계 1은 8건의 회수 방법과 영향을 출력하고, 단계 2는 방법별 건수, 단계 3은 `finance` · `sales` 역할의 사용자 수와 이름을 출력합니다.
- **현업에서는**: 권한 회수 도구도 실제로 지우기 전에 「무엇을 어떻게 지울지」 계획을 먼저 보여 줍니다.

** 할 일**

1. `revoke_input.py` · `revoke_plan.py` · `exercise8-1_run.py` 세 파일을 만들고, `exception_id` · `count_users_by_role` · `build_plan` · `plan_revocation` 에서 직접 쓰는 곳 다섯 군데를 씁니다.
2. 실행해서 <mark>회수 방법과 영향</mark>(단계 1: 계획), <mark>방법별 건수</mark>(단계 2: 집계), <mark>역할별 사용자 수와 이름</mark>(단계 3: 확인)를 읽습니다.

**`revoke_input.py`** — 그대로 붙여 넣습니다. 어제 점검 결과(회수 대상 8건)를 다시 만드는 도우미입니다. 학생이 쓰는 줄은 없습니다. 10/29(목)에 결석했다면 이 코드 대신 바로 아래 「결석한 학생용」 코드를 붙여 넣습니다.

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from review_list import build_access_list                        # 10/29(목) 오전 Exercise 8-1에 만든 현황 함수를 불러온다
from review_rules import find_stale                              # 10/29(목) 오전 Exercise 8-2에 만든 규칙 점검 함수를 불러온다
from review_unused import load_last_used, find_unused            # 10/29(목) 오전 Exercise 8-3에 만든 안 쓴 권한 점검 함수를 불러온다
from overprivilege import generate_report                        # 10/29(목) Exercise 7-1에 만든 리포트 함수를 불러온다
from report_exclude import load_exclude_map, split_by_exclude    # 10/29(목) Exercise 7-2에 만든 회수 제외 함수를 불러온다

REVIEW_TIME = datetime.strptime("2026-10-29 14:00", "%Y-%m-%d %H:%M")   # 어제 점검한 시각(고정). 같은 결과를 얻으려고 어제 시각을 쓴다
TIME_FORMAT = "%Y-%m-%d %H:%M"                                   # 시각 문자열의 형식


def load_to_revoke():                                            # 어제 점검 결과를 다시 만드는 함수
    """어제 점검에서 나온 「회수 대상」 리스트(8개)를 리턴한다.
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

**`revoke_input.py` — 10/29(목)에 결석한 학생용** (출석했다면 위 코드를 씁니다)

```python
# 10/29(목)에 결석한 학생용입니다. 어제 점검 결과인 「회수 대상」 8건을 그대로 담았습니다.
# 10/29(목) 파일(review_list.py 등)이 없어도 오늘 수업을 따라올 수 있습니다. 그대로 붙여 넣고 고치지 않습니다.


def load_to_revoke():                                            # 어제 점검 결과(회수 대상)를 리턴하는 함수
    """어제 점검에서 나온 「회수 대상」 리스트(8개)를 리턴한다.
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

**`revoke_plan.py`**

```python
def exception_id(source):                                        # "예외 3번" 모양 문자열을 받는 함수
    """문자열 「예외 3번」에서 예외 번호(3)를 숫자로 꺼낸다.
    판정 이유에서 어느 예외로 허용했는지 찾을 때 쓴다.
    """
    number_text = source.replace("예외 ", "")                      # "예외 3번" 에서 "예외 " 를 지워 "3번" 으로 만든다 (미리 채움)
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. number_text 에서 "번" 을 지운 문자열을 number_text 에 다시 담는다 (.replace("번", ""))
    # 2. number_text 를 숫자로 바꿔 리턴한다 (int)


def count_users_by_role(users):                                  # 사용자 딕셔너리를 받는 함수
    """역할마다 사용자가 몇 명인지 센다(재직 여부와 상관없이).
    역할을 회수하기 전에 영향을 볼 때 쓴다.
    예: {"finance": 1, "sales": 2}
    """
    counts = {}                                                  # 역할 → 사용자 수를 담을 빈 딕셔너리
    for info in users.values():                                  # 사용자 정보를 하나씩 꺼낸다(.values() 는 딕셔너리의 값만 꺼낸다)
        role = info["role"]                                      # 그 사용자의 역할
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. counts.get(role, 0) 을 old_count 에 담는다 (처음이면 0)
        # 4. counts[role] 를 old_count + 1 로 정한다
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
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. roles[info["role"]] 를 role_permissions 에 담는다 (그 사용자의 역할에 든 권한 리스트)
        # 6. len(role_permissions) 를 impact 에 담는다 (영향은 그 역할에 든 권한 수)
        return make_plan(finding, method, finding["user"], impact)  # 지울 대상은 그 사용자의 이름 (미리 채움)
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. role_counts[info["role"]] 를 impact 에 담는다 (역할에서 권한 빼기: 영향은 그 역할을 가진 사용자 수)
    return make_plan(finding, method, info["role"], impact)      # 지울 대상은 역할 이름 (미리 채움)


def plan_revocation(findings, users, roles):                     # 회수 대상 리스트 · 사용자 딕셔너리 · 역할 딕셔너리를 받는 함수
    """회수 대상마다 회수 방법을 정해 계획 리스트를 리턴한다.
    실제로는 아무것도 지우지 않으며, 회수하기 전에 계획부터 세울 때 쓴다.
    """
    role_counts = count_users_by_role(users)                     # 역할마다 사용자가 몇 명인지 센다(반복 전에 한 번만)
    plans = []                                                   # 계획을 담을 빈 리스트
    for finding in findings:                                     # 회수 대상을 하나씩 꺼낸다
        info = users[finding["user"]]                            # 그 사용자의 정보를 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 8. finding["source"] 안에 "예외" 가 있으면 (in)
        # 9.   method 를 "예외 삭제" 로 정한다
        # 10. 그렇지 않고 info["employed"] 가 거짓이면 (elif not)
        # 11.  method 를 "역할 해제" 로 정한다
        # 12. 그렇지 않으면 (else)
        # 13.  method 를 "역할에서 권한 빼기" 로 정한다
        plan = build_plan(finding, method, users, roles, role_counts)  # 계획 한 건을 만든다
        plans.append(plan)                                       # 방법에 맞는 계획을 만들어 계획 리스트에 추가한다
    return plans                                                 # 계획 리스트를 리턴한다
```

- **직접 쓰는 곳은 네 함수의 다섯 군데**입니다. 판단이 필요한 함수마다 1 ~ 6줄만 쓰고, 나머지는 미리 채웠습니다.
  - `exception_id`(1 · 2번): 「번」을 지우고 숫자로 바꿉니다.
  - `count_users_by_role`(3 · 4번): 역할마다 사용자 수를 1 늘려 적습니다.
  - `build_plan`(5 · 6번, 7번): 역할 해제와 역할에서 권한 빼기의 영향을 정합니다.
  - `plan_revocation`(8 ~ 13번): 회수 대상마다 **어떤 방법으로 회수할지**(`method`)를 정합니다.
- 들여쓰기는 미리 채운 줄에 맞춥니다.
  - `exception_id` · `count_users_by_role`: 함수 안이라 `for` 밖은 4개, `for` 안쪽은 8개입니다.
  - `build_plan`: `if method == "역할 해제":` 안쪽(5 · 6번)은 8개이고, 7번은 `if` 밖이라 4개입니다.
  - `plan_revocation`: 미리 채운 `for` 안쪽이라 `if` · `elif` · `else` 는 8개, 그 안쪽 `method = …` 는 4개 더(12개)입니다.
- **미리 채운 함수**
  - `make_plan`: 회수 대상을 복사해 세 키를 추가한 계획을 만듭니다(판단이 없는 복사라 미리 채움).
  - `count_users_by_role` 의 `for info in users.values():` 에서 `.values()` 는 딕셔너리의 값만 하나씩 꺼냅니다.
- **`load_to_revoke`**(`revoke_input.py` 에 들어 있고 그대로 붙여 넣습니다): 어제 점검을 같은 방법으로 다시 해서 회수 대상 8건을 만듭니다.
  - 어제와 같은 결과를 얻으려고 점검 시각은 `2026-10-29 14:00` 으로 고정했습니다.
- 오늘 데이터에서 영향이 2건 이상인 계획은 dami 의 역할 해제 두 건(영향 2)이고, Exercise 8-2에서 승인 대상이 됩니다.
- 10번의 `elif not info["employed"]` 는 「재직 여부(`employed`)가 `False` 이면」입니다.
  - 주석 목록의 10번이 `elif` 입니다.
  - `not` 은 참과 거짓을 뒤집습니다.
- 채우기 전에 실행하면 `NameError: name 'method' is not defined` 오류가 납니다.
  - 회수 방법(`method`)을 아직 정하지 않았는데 `build_plan` 에 전달하려 하기 때문입니다. 위의 `exception_id` · `count_users_by_role` · `build_plan` 은 채우기 전에도 오류가 나지 않습니다.

**`exercise8-1_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 어제 점검 결과를 만들고 `plan_revocation` 으로 계획을 세워 세 단계로 출력합니다.

```python
from rbac import USERS, ROLES                                    # 10/21(수)에 만든 사용자 · 역할 딕셔너리를 불러온다
from revoke_input import load_to_revoke                          # 어제 점검 결과(회수 대상)를 만드는 함수를 불러온다
from revoke_plan import plan_revocation                          # 방금 만든 회수 계획 함수를 불러온다

to_revoke = load_to_revoke()                                     # 어제 점검한 회수 대상을 만든다
plans = plan_revocation(to_revoke, USERS, ROLES)                 # 회수 계획을 세운다(실제로는 지우지 않는다)

print("--- 단계 1: 계획 - 회수 대상", len(to_revoke), "건의 회수 방법")   # 단계 1 시작을 알리는 줄
for plan in plans:                                               # 계획을 하나씩 꺼낸다
    print(plan["user"], plan["permission"], "<-", plan["source"], "|", plan["method"], "| 영향", plan["impact"], "건")   # 사용자 · 권한 <- 출처 | 방법 | 영향을 출력한다

print("--- 단계 2: 집계 - 방법별 건수")                           # 단계 2 시작을 알리는 줄
counts = {}                                                      # 방법 → 건수를 담을 빈 딕셔너리
for plan in plans:                                               # 계획을 하나씩 꺼낸다
    count_key = plan["method"]                                   # 세는 기준이 되는 키
    old_count = counts.get(count_key, 0)                         # 그 키의 지금까지 센 수(처음이면 0)
    counts[count_key] = old_count + 1                            # 1 늘려서 다시 적는다
print(counts)                                                    # 방법별 건수를 출력한다

print("--- 단계 3: 확인 - 역할별 사용자 수와 이름")                    # 단계 3 시작을 알리는 줄
names_by_role = {"finance": [], "sales": []}                     # 역할 → 그 역할을 가진 사용자 이름 리스트
for name, info in USERS.items():                                 # 사용자를 하나씩 꺼낸다
    if info["role"] in names_by_role:                            # finance 나 sales 역할이면
        names_by_role[info["role"]].append(name)                 # 그 역할의 이름 리스트에 이름을 추가한다
for role in names_by_role:                                       # 두 역할을 하나씩 꺼낸다
    names = names_by_role[role]                                  # 그 역할의 이름 리스트
    print(role, len(names), "명", names)                         # 역할 · 사용자 수 · 이름을 출력한다
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `revoke_input.py` · `revoke_plan.py` · `exercise8-1_run.py` 를 만들어 위 코드를 붙여 넣습니다. 만드는 법은 둘 중 하나를 고릅니다.
   - VS Code: `access_control` 폴더를 선택하고 **새 파일**(New File) 아이콘을 눌러 이름을 입력합니다.
   - 터미널: `pwd` 로 `access_control` 인지 확인하고 `touch 이름` 으로 만든 뒤 VS Code 에서 열어 붙여 넣습니다(`vim 이름` → `i` → 붙여넣기 → `Esc` → `:wq` 도 됩니다).
   - 10/29(목)에 결석했다면 `revoke_input.py` 에 「결석한 학생용」 코드를 붙여 넣습니다.
2. **[VS Code]** `revoke_plan.py` 에서 직접 쓰는 곳 다섯 군데(`exception_id` · `count_users_by_role` · `build_plan` · `plan_revocation`)를 씁니다. 1.1 의 카드와 표, 흐름 그림을 보고 씁니다.
3. **[터미널]** `pwd` 의 결과가 `access_control` 로 끝나는지 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise8-1_run.py
   ```
4. 출력은 세 단계입니다. 단계 1은 `회수 대상 8 건의 회수 방법` 줄과 계획 여덟 줄, 단계 2는 방법별 건수 딕셔너리 한 줄, 단계 3은 역할 두 줄(사용자 수와 이름)입니다.
5. **[보고서]** Unit 8 의 `## Exercise 8-1` › `### Exercise 8-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 회수 방법별 건수와 `finance` · `sales` 역할의 사용자 수를 적어 주세요.
   - (나) [핵심 질문] dami 의 역할 `sales` 권한 `SALES:QUERY` 를 「`sales` 역할에서 `SALES:QUERY` 권한 빼기」로 회수했다면 누가 영향을 받았을까요? 코드가 퇴사한 dami 를 「역할 해제」로 정한 이유도 적어 주세요.
   - (다) [핵심 질문] 회수 대상 8건 가운데 dami 의 권한이 3건입니다. 실제로 지우기 전에 회수 계획을 리스트로 먼저 만들어 보는 이유와, dami 3건을 처리하려고 데이터를 실제로 바꾸는 작업의 종류가 몇 가지인지(`users` 의 dami 정보를 바꾸는 일, 예외 리스트 `EXCEPTIONS` 에서 지우는 일 중 몇 가지가 필요한지) 적어 주세요.

## Exercise 8-1 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 예외로 받은 권한인지 | `if "예외" in finding["source"]:` |
| 퇴사한 사용자인지 | `elif not info["employed"]:` |
| 회수 방법 정하기 | `method = "예외 삭제"` · `method = "역할 해제"` · `method = "역할에서 권한 빼기"` |
| 계획 한 건 만들기 | `build_plan(finding, method, users, roles, role_counts)` (지울 대상과 영향을 정함. 역할 두 경우의 영향은 직접 씀) |
| 예외 번호 꺼내기 | `number_text = number_text.replace("번", "")` → `return int(number_text)` |
| 역할별 사용자 수 세기 | `old_count = counts.get(role, 0)` → `counts[role] = old_count + 1` |
| 역할 해제의 영향 | `role_permissions = roles[info["role"]]` → `impact = len(role_permissions)` |
| 역할에서 권한 빼기의 영향 | `impact = role_counts[info["role"]]` |

---
