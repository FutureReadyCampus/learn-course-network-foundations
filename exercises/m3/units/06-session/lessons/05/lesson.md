---
id: m3-u06-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/086_day04_am_access_review.md
  mission_id: GichanSource.m3-1029-am-access-review
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## Exercise Exercise 5-2 정답

 **터미널에 입력합니다.**

```bash
python day04_2-1_run.py
```

**채운 코드** (한 예)

```python
    access_list = []                                             # 현황을 담을 빈 리스트
    for user, info in USERS.items():                             # 사용자를 한 명씩 꺼낸다
        role_list = role_entries(user, info)                     # 그 사용자가 역할로 받은 권한 리스트를 만든다
        access_list = access_list + role_list                    # 현황 뒤에 이어 붙인다
    for exception in EXCEPTIONS:                                 # 예외를 하나씩 꺼낸다
        user = exception["user"]                                 # 예외를 받은 사용자 이름을 꺼낸다
        user_info = USERS[user]                                  # 그 사용자의 정보 딕셔너리를 꺼낸다
        exception_id = exception["id"]                           # 예외 번호를 꺼낸다
        source_text = f"예외 {exception_id}번"                      # 받은 방식 문자열을 만든다
        entry = {                                                # 현황의 권한 한 건을 만든다
            "user": user,                                        # 사용자
            "permission": exception["permission"],               # 권한
            "source": source_text,                               # 받은 방식
            "employed": user_info["employed"],                   # 재직 여부
        }
        entry["expires"] = exception["expires"]                  # 예외에만 있는 만료 시각 키를 추가한다
        access_list.append(entry)                                # 현황에 추가한다
    return access_list                                           # 현황을 리턴한다
```

**결과**

- (가) 출력은 다음과 같고, 부여돼 있는 권한은 모두 **14건**입니다. 역할로 받은 권한이 9건, 예외로 받은 권한이 5건입니다. 사용자별 개수는 seoyeon · junho · gaeun · dami 가 3건씩, batch-night 가 2건이고, 사용자 파일에 있는 tester 는 권한이 하나도 없습니다. tester 의 역할 `intern` 이 역할 파일에 없어서 받은 권한이 없기 때문입니다.

```
--- 단계 1: 현황 - 부여돼 있는 권한 14 건
seoyeon SALES:QUERY <- 역할 sales | 재직 True
seoyeon SALES:CHANGE <- 역할 sales | 재직 True
junho SALES:QUERY <- 역할 finance | 재직 True
junho SETTLE:QUERY <- 역할 finance | 재직 True
gaeun ACCOUNT:QUERY <- 역할 account_admin | 재직 True
gaeun ACCOUNT:CHANGE <- 역할 account_admin | 재직 True
dami SALES:QUERY <- 역할 sales | 재직 False
dami SALES:CHANGE <- 역할 sales | 재직 False
batch-night SETTLE:QUERY <- 역할 batch | 재직 True
seoyeon SETTLE:QUERY <- 예외 1번 | 재직 True
junho SALES:CHANGE <- 예외 2번 | 재직 True
dami SALES:QUERY <- 예외 3번 | 재직 False
batch-night SALES:QUERY <- 예외 4번 | 재직 True
gaeun SETTLE:QUERY <- 예외 5번 | 재직 True
--- 단계 2: 점검 - 사용자별 권한 개수
{'seoyeon': 3, 'junho': 3, 'gaeun': 3, 'dami': 3, 'batch-night': 2}
```

- (나) 판정 함수(`check_permission` · `evaluate_access`)가 이미 거부하는 권한이 리스트에 들어 있습니다. 예를 들어 퇴사한 dami 의 권한들(역할 2건 + 예외 3번)은 「퇴사한 계정」으로 거부되고, 만료 시각이 지난 예외(1 · 2 · 4 · 5번)는 판정에 쓰이지 않습니다. 그래도 리스트에서 빼지 않는 이유는, 점검의 목적이 「지금 거부되는가」가 아니라 「부여 기록에 남아 있는 필요 없는 권한을 찾아 정리하는가」이기 때문입니다. 거부되는 권한을 빼 버리면 Exercise 6-2에서 퇴사자나 만료된 예외를 찾을 수 없습니다. 또 판정 함수는 접근을 막을 뿐 기록을 지우지 않으므로, 기록이 남아 있는 한 재직 표시가 실수로 바뀌면 다시 접근할 수 있게 됩니다. 리스트에 남겨야 정리 대상을 알 수 있습니다.

**왜** — 점검은 「누가 어떤 권한을 어떤 방법(역할 · 예외)으로 갖고 있나」를 먼저 한곳에 모아야 시작됩니다. 역할 파일 · 예외 파일 · 사용자 파일을 따로 보면 같은 사람의 권한이 나뉘어 있어 놓치기 쉽습니다. 출처(`source`)를 권한마다 적어 두면 나중에 「어느 방법으로 받은 권한을 거둘지」 정할 수 있습니다.

**자주 틀리는 곳** — `access_list = access_list + role_list` 에서 앞의 `access_list =` 를 빼먹는 경우가 많습니다. 이은 리스트가 어디에도 담기지 않아 역할로 받은 권한이 모두 사라집니다. 오류는 나지 않고 예외로 받은 5건만 나옵니다. 실행하면 다음처럼 됩니다(`부여돼 있는 권한 5 건`이면 이 실수입니다).

```
--- 단계 1: 현황 - 부여돼 있는 권한 5 건
seoyeon SETTLE:QUERY <- 예외 1번 | 재직 True
junho SALES:CHANGE <- 예외 2번 | 재직 True
dami SALES:QUERY <- 예외 3번 | 재직 False
batch-night SALES:QUERY <- 예외 4번 | 재직 True
gaeun SETTLE:QUERY <- 예외 5번 | 재직 True
--- 단계 2: 점검 - 사용자별 권한 개수
{'seoyeon': 1, 'junho': 1, 'dami': 1, 'batch-night': 1, 'gaeun': 1}
```

예외 권한에 `entry["expires"]` 를 추가하는 줄을 빼먹으면 Exercise 6-2에서 예외 만료를 판단할 수 없습니다. 이 오류는 Exercise 6-1 출력에는 보이지 않고 Exercise 6-2에서 나타납니다.

**관제에서는** — 현황표는 점검을 시작할 때 가장 먼저 뽑는 표입니다. 점검 때마다 같은 형식으로 뽑아 두면 지난 점검과 비교해 새로 생긴 권한 · 사라진 권한을 찾을 수 있습니다.

---

## Exercise Exercise 5-2 정답

 **터미널에 입력합니다.**

```bash
python day04_3-1_run.py
```

**채운 코드** (한 예)

```python
    stale = []                                                   # 걸린 권한을 담을 빈 리스트
    for entry in access_list:                                    # 현황의 권한을 한 건씩 꺼낸다
        expires = entry.get("expires")                           # 만료 시각을 꺼낸다(역할로 받은 권한에는 이 키가 없어 None)
        reason = ""                                              # 이유를 빈 문자열로 시작한다
        if not entry["employed"]:                                # 퇴사한 사용자의 권한이면
            reason = "퇴사한 계정"                                 # 이유를 적는다
        elif expires is not None:                                # 아니고, 만료 시각이 적혀 있으면(예외로 받은 권한이면)
            expires_at = datetime.strptime(expires, TIME_FORMAT)  # 만료 시각 문자열을 시각으로 바꾸고
            if expires_at <= now:                                # 지금과 같거나 이전이면(만료됐으면)
                reason = "만료된 예외"                             # 이유를 적는다
        if reason != "":                                         # 이유가 적혔으면(규칙에 걸렸으면)
            stale_entry = entry.copy()                           # 권한을 복사해서
            stale_entry["reason"] = reason                       # 복사본에 이유를 적고
            stale.append(stale_entry)                            # 걸린 리스트에 추가한다
    return stale                                                 # 걸린 리스트를 리턴한다
```

**결과**

- (가) 출력은 다음과 같고, 규칙에 걸린 권한은 **7건**입니다. 퇴사한 계정이 3건(dami 의 역할 권한 2건과 예외 3번), 만료된 예외가 4건(1 · 2 · 4 · 5번)입니다. dami 의 예외 3번은 만료 시각(10/31(토))이 아직 안 지났지만 퇴사한 계정이라 퇴사로 걸렸습니다.

```
--- 단계 1: 판정 - 규칙에 걸린 권한 7 건 (전체 14 건 중)
dami SALES:QUERY <- 역할 sales | 퇴사한 계정
dami SALES:CHANGE <- 역할 sales | 퇴사한 계정
seoyeon SETTLE:QUERY <- 예외 1번 | 만료된 예외
junho SALES:CHANGE <- 예외 2번 | 만료된 예외
dami SALES:QUERY <- 예외 3번 | 퇴사한 계정
batch-night SALES:QUERY <- 예외 4번 | 만료된 예외
gaeun SETTLE:QUERY <- 예외 5번 | 만료된 예외
--- 단계 2: 점검 - 이유별 건수
{'퇴사한 계정': 3, '만료된 예외': 4}
```

- (나) 예를 들어 **재직 중이고 기한도 안 지났지만 실제로는 쓰지 않는 권한**입니다. 맡은 일이 바뀌었거나 프로젝트가 끝났는데 역할이 그대로인 사람의 권한이 그렇습니다. 이런 권한은 파일에 적힌 사실(퇴사 여부 · 만료 시각)만으로는 알 수 없고, 실제로 그 권한을 썼는지 보여 주는 정보(권한을 마지막으로 쓴 시각)가 있어야 찾을 수 있습니다. 부서 이동 기록을 비교하는 방법도 가능합니다.
- (다) 한 예: 먼저 회수할 것은 **퇴사한 계정 3건**(dami 의 역할로 받은 두 건과 예외 3번)입니다. 기준은 「그 권한을 쓸 사람이 이미 없는가」입니다. 퇴사한 사람의 권한은 업무에 쓰일 일이 없어 회수해도 업무가 멈추지 않습니다. 또 이 세 건은 이유가 퇴사 하나뿐이라, 사용자 파일의 재직 표시(`employed`)가 입력 실수나 인사 변경으로 `True` 로 바뀌면 다시 접근할 수 있게 되어 위험합니다. 반면 만료된 예외 4건은 기간이 이미 끝났고, 누가 `expires` 를 일부러 고치지 않는 한 다시 쓰일 일이 거의 없어 급하지 않습니다. 기준 하나를 정하고 그 기준으로 이유를 대면 맞습니다. 다른 기준(예: 쓰기 권한이 있는 것부터, 예외 전체를 먼저)도 이유가 맞으면 인정합니다.

**왜** — 사실만 보고 판단할 수 있는 점검은 코드가 사람보다 빠르고 빠짐이 없습니다. 이유(`reason`)를 함께 적어 두면 관제 담당이 걸린 이유를 바로 알고 처리할 수 있습니다. 권한 한 건이 두 규칙에 모두 걸릴 때 `elif` 로 하나만 적게 하지 않으면 같은 권한이 두 번 나오거나 이유가 뒤섞입니다.

**자주 틀리는 곳** — `entry.get("expires")` 대신 `entry["expires"]` 로 꺼내는 경우가 가장 많습니다. 역할로 받은 권한에는 `expires` 키가 없어 첫 줄에서 바로 멈춥니다. 실행하면 다음처럼 됩니다.

```
Traceback (most recent call last):
  File "…/파일이름.py", line 8, in <module>
    stale = find_stale(access_list, NOW)                             # 규칙에 걸린 권한을 찾는다
  File "…/파일이름.py", line 11, in find_stale
    expires = entry["expires"]                           # 만료 시각을 꺼낸다
KeyError: 'expires'
```

`if` 두 개를 따로 쓰면(`elif` 대신) 퇴사한 사람의 만료된 예외가 만료 이유로 덮어써질 수 있습니다. 걸린 권한을 복사하지 않고 `entry["reason"] = reason` 으로 원래 현황 권한을 바꾸면 다음 Exercise에 현황 리스트를 다시 쓸 때 `reason` 키가 섞여 들어갑니다.

**관제에서는** — 규칙으로 걸리는 권한은 매주 자동으로 리스트를 뽑아 담당자에게 보내고, 처리하지 않은 채 몇 주째 남아 있는 권한은 따로 표시합니다. 같은 계정이 반복해서 걸리면 퇴사 처리 절차(인사 시스템과 권한 시스템의 연동)에 빠진 곳이 있다는 뜻으로 봅니다.

---

## Exercise Exercise 5-2 정답

 **터미널에 입력합니다.**

```bash
python day04_4-1_run.py
```

**채운 코드** (한 예)

```python
    unused = []                                                  # 후보를 담을 빈 리스트
    for entry in access_list:                                    # 현황의 권한을 한 건씩 꺼낸다
        user = entry["user"]                                     # 그 권한의 사용자
        permission = entry["permission"]                         # 그 권한의 권한 이름
        key = f"{user}:{permission}"                             # 그 권한의 「사용자:권한」 문자열을 만든다
        used_text = last_used_map.get(key)                       # 마지막 사용 시각 문자열을 꺼낸다(이력이 없으면 None)
        if used_text is None:                                    # 사용 이력이 없으면
            unused_entry = make_unused(entry, None)              # 안 쓴 권한 한 건을 만든다
            unused.append(unused_entry)                          # 마지막 사용 시각을 None 으로 적은 복사본을 후보에 추가한다
        elif days_since(used_text, now) > limit_days:            # 사용 이력이 있고 기준 일 수보다 오래 안 썼으면
            unused_entry = make_unused(entry, used_text)         # 안 쓴 권한 한 건을 만든다
            unused.append(unused_entry)                          # 마지막 사용 시각을 적은 복사본을 후보에 추가한다
    return unused                                                # 후보 리스트를 리턴한다
```

**결과**

- (가) 출력은 다음과 같고, 90일 넘게 안 쓴 후보는 **3건**입니다. seoyeon 의 `SALES:CHANGE`(120일째 안 씀), junho 의 `SALES:QUERY`(91일째 안 씀), gaeun 의 `ACCOUNT:CHANGE`(사용 이력 없음)입니다.

```
--- 단계 1: 현황 - 규칙에 안 걸린 권한 7 건의 안 쓴 일 수
seoyeon SALES:QUERY -> 2 일째 안 씀
seoyeon SALES:CHANGE -> 120 일째 안 씀
junho SALES:QUERY -> 91 일째 안 씀
junho SETTLE:QUERY -> 90 일째 안 씀
gaeun ACCOUNT:QUERY -> 9 일째 안 씀
gaeun ACCOUNT:CHANGE -> 사용 이력 없음
batch-night SETTLE:QUERY -> 0 일째 안 씀
--- 단계 2: 판정 - 90일 넘게 안 쓴 후보 3 건
seoyeon SALES:CHANGE <- 역할 sales
junho SALES:QUERY <- 역할 finance
gaeun ACCOUNT:CHANGE <- 역할 account_admin
```

- (나) 하루 차이로 나누는 것은 단순하지만, 그 하루 차이가 실제 필요 여부를 뜻하지는 않습니다. 90일은 「대부분의 정기 업무(분기 정산 등)는 그 안에 한 번은 쓴다」는 약속일 뿐이고, 같은 junho 의 `SETTLE:QUERY`(90일째)와 `SALES:QUERY`(91일째)는 사실상 같은 상태입니다. 기준이 필요한 이유는 점검 결과를 사람마다 다르게 해석하지 않고 같은 잣대로 반복해서 뽑기 위해서입니다. 경계 부근(예: 85~95일)의 권한은 후보가 되기 직전이거나 막 후보가 된 것이므로, 담당자가 다음을 추가로 확인합니다. ① 그 권한이 분기 · 반기 · 연 단위 업무에 쓰이는가 ② 사용 이력이 누락된 로그는 없는가 ③ 최근 업무 변경이 있었는가.
- (다) 사용 이력이 없다고 바로 지우면 안 되는 경우는 **평소엔 안 쓰지만 꼭 필요한 순간이 있는 권한**입니다. 예: 장애나 보안 사고 때만 쓰는 비상 권한, 분기 · 연말 결산 때만 쓰는 권한, 아직 한 번도 안 썼지만 곧 시작할 업무를 위해 미리 받은 권한입니다. gaeun 의 `ACCOUNT:CHANGE`(계정 변경)도 계정 관리 담당이 평소엔 조회만 하다가 사고 때 변경해야 한다면 필요한 권한입니다. 그래서 「후보」로만 뽑고, 담당자가 사용 목적을 확인한 뒤에 회수를 결정합니다.

**왜** — 규칙으로 못 찾는 필요 없는 권한은 사용 이력과 비교해야 찾을 수 있습니다. 기준 일 수(`limit_days`)를 함수의 인자로 받으면 90일을 60일이나 180일로 바꿀 때 함수를 고치지 않아도 됩니다. 사용 이력이 없는 권한도 후보에 넣는 것은, 이력에 한 번도 나오지 않았다면 쓰이지 않았을 가능성이 크기 때문입니다.

**자주 틀리는 곳** — 비교를 `days_since(used_text, now) > limit_days` 대신 `>=` 로 쓰는 경계 실수가 가장 흔합니다. 90일째 쓴 junho 의 `SETTLE:QUERY` 가 후보에 잘못 들어갑니다. 실행하면 다음처럼 됩니다(후보가 4건이 되면 이 실수입니다. 줄 번호는 내 파일과 다를 수 있습니다).

```
--- 단계 1: 현황 - 규칙에 안 걸린 권한 7 건의 안 쓴 일 수
seoyeon SALES:QUERY -> 2 일째 안 씀
seoyeon SALES:CHANGE -> 120 일째 안 씀
junho SALES:QUERY -> 91 일째 안 씀
junho SETTLE:QUERY -> 90 일째 안 씀
gaeun ACCOUNT:QUERY -> 9 일째 안 씀
gaeun ACCOUNT:CHANGE -> 사용 이력 없음
batch-night SETTLE:QUERY -> 0 일째 안 씀
--- 단계 2: 판정 - 90일 넘게 안 쓴 후보 4 건
seoyeon SALES:CHANGE <- 역할 sales
junho SALES:QUERY <- 역할 finance
junho SETTLE:QUERY <- 역할 finance
gaeun ACCOUNT:CHANGE <- 역할 account_admin
```

`elif` 대신 `if` 로 쓰면, 사용 이력이 없는 gaeun 의 `ACCOUNT:CHANGE` 도 `days_since` 에 들어가 `TypeError: strptime() argument 1 must be str, not None` 으로 멈춥니다. 이력이 없으면 일 수를 계산할 수 없으므로 이력이 있을 때(`elif`)만 계산해야 합니다.

**관제에서는** — 미사용 후보는 곧바로 회수하지 않고, 권한 소유자와 그 상급자에게 「계속 필요한가」를 확인하는 요청을 보냅니다. 응답이 없으면 한 단계 낮은 권한으로 줄였다가 문제가 없으면 회수합니다. 확인 요청과 응답은 점검 이력으로 남깁니다.

---

## 앞 Exercise 파일 완성본

앞 Exercise 파일을 못 만들고 다음 Exercise로 넘어가야 할 때 그대로 만들어 씁니다. 정답 본문을 함수 머리말과 합친 전체 파일입니다.

**`review_list.py`** (Exercise 6-1 완성본)

```python
from rbac import USERS, ROLES                                    # 10/21(수)에 만든 사용자 · 역할 딕셔너리를 불러온다
from exception_policy import EXCEPTIONS                          # 10/22(목)에 만든 예외 리스트를 불러온다


def role_entries(user, info):                                    # 사용자 이름과 그 사용자의 정보 딕셔너리를 받는 함수
    """사용자 한 명이 역할로 받은 권한을 현황의 권한 한 개씩 만들어 리스트로 리턴한다.
    현재 갖고 있는 권한을 정리하기 시작할 때 쓴다.
    """
    role = info["role"]                                          # 그 사용자의 역할을 꺼낸다
    entries = []                                                 # 역할로 받은 권한을 담을 빈 리스트
    for permission in ROLES.get(role, []):                       # 역할의 권한을 하나씩 꺼낸다(역할 파일에 없는 역할이면 빈 리스트)
        entry = {                                                # 현황의 권한 한 건을 만든다
            "user": user,                                        # 사용자
            "permission": permission,                            # 권한
            "source": f"역할 {role}",                              # 받은 방식
            "employed": info["employed"],                        # 재직 여부
        }
        entries.append(entry)                                    # 리스트에 추가한다
    return entries                                               # 역할로 받은 권한 리스트를 리턴한다


def build_access_list():                                         # 지금 부여돼 있는 권한을 모두 모아 리스트로 만드는 함수
    """부여된 권한을 사용자별 · 권한별 리스트로 모은다.
    정기 점검을 시작할 때 누가 무엇을 갖고 있는지 정리하는 데 쓴다.
    """
    access_list = []                                             # 현황을 담을 빈 리스트
    for user, info in USERS.items():                             # 사용자를 한 명씩 꺼낸다
        role_list = role_entries(user, info)                     # 그 사용자가 역할로 받은 권한 리스트를 만든다
        access_list = access_list + role_list                    # 현황 뒤에 이어 붙인다
    for exception in EXCEPTIONS:                                 # 예외를 하나씩 꺼낸다
        user = exception["user"]                                 # 예외를 받은 사용자 이름을 꺼낸다
        user_info = USERS[user]                                  # 그 사용자의 정보 딕셔너리를 꺼낸다
        exception_id = exception["id"]                           # 예외 번호를 꺼낸다
        source_text = f"예외 {exception_id}번"                      # 받은 방식 문자열을 만든다
        entry = {                                                # 현황의 권한 한 건을 만든다
            "user": user,                                        # 사용자
            "permission": exception["permission"],               # 권한
            "source": source_text,                               # 받은 방식
            "employed": user_info["employed"],                   # 재직 여부
        }
        entry["expires"] = exception["expires"]                  # 예외에만 있는 만료 시각 키를 추가한다
        access_list.append(entry)                                # 현황에 추가한다
    return access_list                                           # 현황을 리턴한다
```

**`review_rules.py`** (Exercise 6-2 완성본)

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from exception_policy import TIME_FORMAT                         # 시각 문자열의 형식("%Y-%m-%d %H:%M")을 불러온다


def find_stale(access_list, now):                                # 현황 리스트와 지금 시각(datetime)을 받는 함수
    """규칙에 걸려 필요 없어진 권한을 리턴하고 걸린 이유를 "reason" 키에 적는다.
    퇴사 · 만료로 남은 권한을 정리할 때 쓴다.
    """
    stale = []                                                   # 걸린 권한을 담을 빈 리스트
    for entry in access_list:                                    # 현황의 권한을 한 건씩 꺼낸다
        expires = entry.get("expires")                           # 만료 시각을 꺼낸다(역할로 받은 권한에는 이 키가 없어 None)
        reason = ""                                              # 이유를 빈 문자열로 시작한다
        if not entry["employed"]:                                # 퇴사한 사용자의 권한이면
            reason = "퇴사한 계정"                                 # 이유를 적는다
        elif expires is not None:                                # 아니고, 만료 시각이 적혀 있으면(예외로 받은 권한이면)
            expires_at = datetime.strptime(expires, TIME_FORMAT)  # 만료 시각 문자열을 시각으로 바꾸고
            if expires_at <= now:                                # 지금과 같거나 이전이면(만료됐으면)
                reason = "만료된 예외"                             # 이유를 적는다
        if reason != "":                                         # 이유가 적혔으면(규칙에 걸렸으면)
            stale_entry = entry.copy()                           # 권한을 복사해서
            stale_entry["reason"] = reason                       # 복사본에 이유를 적고
            stale.append(stale_entry)                            # 걸린 리스트에 추가한다
    return stale                                                 # 걸린 리스트를 리턴한다
```

**`review_unused.py`** (Exercise 6-3 완성본)

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from config_loader import load_json                              # 10/22(목)에 만든 안전한 읽기 함수를 불러온다
from exception_policy import TIME_FORMAT                         # 시각 문자열의 형식("%Y-%m-%d %H:%M")을 불러온다


def load_last_used():                                            # 사용 이력 파일을 읽어 「마지막 사용 시각」 딕셔너리를 만드는 함수
    """「사용자:권한」을 키로, 마지막 사용 시각 문자열을 값으로 하는 딕셔너리를 리턴한다.
    안 쓰는 권한을 찾기 전에 사용 기록을 불러올 때 쓴다.
    """
    last_used_map = {}                                           # 빈 딕셔너리로 시작한다
    for log in load_json("config/access_log.json", []):          # 사용 이력을 한 건씩 꺼낸다(파일이 없으면 빈 리스트)
        user = log["user"]                                       # 그 기록의 사용자
        permission = log["permission"]                           # 그 기록의 권한
        key = f"{user}:{permission}"                             # 「사용자:권한」 문자열을 키로 만든다
        last_used_map[key] = log["last_used"]                    # 그 키의 값에 마지막 사용 시각 문자열을 담는다
    return last_used_map                                         # 딕셔너리를 리턴한다


def make_unused(entry, used_text):                               # 현황의 권한 한 건과 마지막 사용 시각 문자열을 받는 함수
    """권한 한 개를 복사해 "last_used" 키(마지막 사용 시각, 이력이 없으면 None)를 더한다.
    안 쓴 권한 후보를 만들 때 쓴다(원래 권한은 바꾸지 않음).
    """
    unused_entry = entry.copy()                                  # 원래 권한은 바꾸지 않고 복사한다
    unused_entry["last_used"] = used_text                        # 복사본에 마지막 사용 시각(없으면 None)을 적는다
    return unused_entry                                          # 복사본을 리턴한다


def days_since(used_text, now):                                  # 마지막 사용 시각 문자열과 지금 시각을 받는 함수
    """마지막 사용 시각부터 지금까지 안 쓴 일 수를 리턴한다.
    오래 안 쓴 권한을 점검할 때 쓴다.
    """
    used_at = datetime.strptime(used_text, TIME_FORMAT)          # 문자열을 시각으로 바꾼다
    return (now - used_at).days                                  # 지금 - 마지막 사용 시각의 일 수를 리턴한다


def find_unused(access_list, last_used_map, now, limit_days):    # 현황 · 마지막 사용 시각 딕셔너리 · 지금 시각 · 기준 일 수를 받는 함수
    """마지막 사용이 limit_days 일보다 오래됐거나 이력이 없는 권한을 리턴한다.
    후보마다 "last_used" 키에 마지막 사용 시각(없으면 None)을 적는다.
    안 쓰는 권한을 찾을 때 쓴다.
    """
    unused = []                                                  # 후보를 담을 빈 리스트
    for entry in access_list:                                    # 현황의 권한을 한 건씩 꺼낸다
        user = entry["user"]                                     # 그 권한의 사용자
        permission = entry["permission"]                         # 그 권한의 권한 이름
        key = f"{user}:{permission}"                             # 그 권한의 「사용자:권한」 문자열을 만든다
        used_text = last_used_map.get(key)                       # 마지막 사용 시각 문자열을 꺼낸다(이력이 없으면 None)
        if used_text is None:                                    # 사용 이력이 없으면
            unused_entry = make_unused(entry, None)              # 안 쓴 권한 한 건을 만든다
            unused.append(unused_entry)                          # 마지막 사용 시각을 None 으로 적은 복사본을 후보에 추가한다
        elif days_since(used_text, now) > limit_days:            # 사용 이력이 있고 기준 일 수보다 오래 안 썼으면
            unused_entry = make_unused(entry, used_text)         # 안 쓴 권한 한 건을 만든다
            unused.append(unused_entry)                          # 마지막 사용 시각을 적은 복사본을 후보에 추가한다
    return unused                                                # 후보 리스트를 리턴한다
```

**`config/access_log.json`** (Exercise 6-3 사용 이력)

```json
[
  {"user": "seoyeon", "permission": "SALES:QUERY", "last_used": "2026-10-27 09:10"},
  {"user": "seoyeon", "permission": "SALES:CHANGE", "last_used": "2026-06-30 14:00"},
  {"user": "junho", "permission": "SALES:QUERY", "last_used": "2026-07-30 09:00"},
  {"user": "junho", "permission": "SETTLE:QUERY", "last_used": "2026-07-31 10:00"},
  {"user": "gaeun", "permission": "ACCOUNT:QUERY", "last_used": "2026-10-20 08:00"},
  {"user": "batch-night", "permission": "SETTLE:QUERY", "last_used": "2026-10-29 02:00"},
  {"user": "dami", "permission": "SALES:QUERY", "last_used": "2026-10-10 13:00"}
]
```
