---
id: m3-u03-l08
title: 정답
render: markdown
---

# 정답

## 정답을 보는 방법

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

1. 핵심 실습: 실습 3-1 · 3-2 정답을 먼저 봅니다.
2. 응용(여유가 되면): 응용 3-1 ~ 3-3 정답은 그 응용을 했을 때만 봅니다. 응용의 채운 코드는 「제공 파일」 레슨의 완성본과 같은 동작을 합니다.

---

## 실습 3-1 정답

**터미널에 입력합니다.**

```bash
python exercise3-1_run.py
```

**채운 코드** (한 예)

```python
        # ① access_list 와 role_list 를 + 로 이은 리스트를 access_list 에 다시 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
        access_list = access_list + role_list                    # 현황 뒤에 이어 붙인다
        # ② access_list 에 entry 를 추가한다 (.append)   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
        access_list.append(entry)                                # 현황에 추가한다
```

**결과**

- 채우기 전 출력은 다음과 같습니다(권한을 하나도 더하지 않아 0 건).

```
--- 단계 1: 현황 - 부여돼 있는 권한 0 건
--- 단계 2: 점검 - 사용자별 권한 개수
{}
```

- (가) 채운 뒤 출력은 다음과 같고, 부여돼 있는 권한은 모두 **14건**입니다. 역할로 받은 권한이 9건, 예외로 받은 권한이 5건입니다. 사용자별 개수는 seoyeon · junho · gaeun · dami 가 3건씩, batch-night 가 2건입니다. 사용자 파일에 있는 tester 는 권한이 하나도 없습니다. tester 의 역할 `intern` 이 역할 파일에 없어서 받은 권한이 없기 때문입니다.

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

- (나) 판정 함수(`check_permission` · `evaluate_access`)가 이미 거부하는 권한이 리스트에 들어 있습니다. 예를 들어 퇴사한 dami 의 권한들(역할 2건 + 예외 3번)은 「퇴사한 계정」으로 거부되고, 만료 시각이 지난 예외(1 · 2 · 4 · 5번)는 판정에 쓰이지 않습니다. 그래도 리스트에서 빼지 않는 이유가 있습니다. 점검의 목적은 「지금 거부되는가」를 보는 것이 아니라, 「부여 기록에 남아 있는 필요 없는 권한을 찾아 정리하는 것」이기 때문입니다. 거부되는 권한을 빼 버리면 실습 3-2 의 규칙 점검(`find_stale`)에서 퇴사자나 만료된 예외를 찾을 수 없습니다. 또 판정 함수는 접근을 막을 뿐 기록을 지우지 않으므로, 기록이 남아 있는 한 재직 표시가 실수로 바뀌면 다시 접근할 수 있게 됩니다. 리스트에 남겨야 정리 대상을 알 수 있습니다.

**왜** — 점검은 「누가 어떤 권한을 어떤 방법(역할 · 예외)으로 갖고 있나」를 먼저 한곳에 모아야 시작됩니다. 역할 파일 · 예외 파일 · 사용자 파일을 따로 보면 같은 사람의 권한이 나뉘어 있어 놓치기 쉽습니다. 출처(`source`)를 권한마다 적어 두면 나중에 「어느 방법으로 받은 권한을 거둘지」 정할 수 있습니다.

**자주 틀리는 곳**

| 실수 | 결과 | 알아보는 법 |
|---|---|---|
| ① 에서 앞의 `access_list =` 를 빼먹음 (가장 많음) | 역할로 받은 권한이 모두 사라지고 예외로 받은 5건만 나옴 (오류 없음) | `부여돼 있는 권한 5 건` |
| ② 를 4칸에 써서 `for` 밖으로 나감 | 예외 다섯 건 가운데 마지막 5번만 추가됨 (오류 없음) | `부여돼 있는 권한 10 건` |

첫째 실수는 이은 리스트가 어디에도 담기지 않아서 생깁니다. 실행하면 다음처럼 됩니다.

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

둘째 실수는 `for` 가 다 돈 뒤에 `append` 를 한 번만 해서 생깁니다. 그때 `entry` 에 남아 있는 것은 마지막 예외(5번) 하나입니다.

**관제에서는** — 현황표는 점검을 시작할 때 가장 먼저 뽑는 표입니다. 점검 때마다 같은 형식으로 뽑아 두면 지난 점검과 비교해 새로 생긴 권한 · 사라진 권한을 찾을 수 있습니다.

---

## 실습 3-2 정답

**터미널에 입력합니다.**

```bash
python exercise3-2_run.py
```

**채운 코드** (한 예)

```python
        # ① last_used_map 에서 key 로 마지막 사용 시각을 꺼내 used_text 에 담는다 (.get, 이력이 없으면 None)   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
        used_text = last_used_map.get(key)                       # 마지막 사용 시각 문자열을 꺼낸다(이력이 없으면 None)
        # ② 아니고(elif), days_since(used_text, now) 가 limit_days 보다 크면 (>)   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
        elif days_since(used_text, now) > limit_days:            # 사용 이력이 있고 기준 일 수보다 오래 안 썼으면
```

**결과**

- 채우기 전에는 단계 1 일곱 줄이 나온 뒤 `NameError: name 'used_text' is not defined` 로 멈춥니다. ① 만 채우면 오류 없이 끝나지만 `후보 2 건` 에 `gaeun ACCOUNT:CHANGE` 가 두 번 나옵니다. ② 가 비어 있는 동안에는 그 아래 두 줄이 위 `if` 안쪽으로 붙기 때문입니다.
- (가) 채운 뒤 출력은 다음과 같고, 90일 넘게 안 쓴 후보는 **3건**입니다.

| 사용자 | 권한 | 안 쓴 일 수 |
|---|---|---|
| seoyeon | `SALES:CHANGE` | 120일째 안 씀 |
| junho | `SALES:QUERY` | 91일째 안 씀 |
| gaeun | `ACCOUNT:CHANGE` | 사용 이력 없음 |

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

**자주 틀리는 곳**

| 실수 | 결과 | 알아보는 법 |
|---|---|---|
| ② 의 비교를 `>` 대신 `>=` 로 씀 (가장 흔함) | 90일째 쓴 junho 의 `SETTLE:QUERY` 가 후보에 잘못 들어감 | 후보가 4건 |
| ② 에서 `elif` 대신 `if` 로 씀 | 이력 없는 gaeun 의 `ACCOUNT:CHANGE` 도 `days_since` 에 들어가 멈춤 | `TypeError: strptime() argument 1 must be str, not None` |
| ① 에서 `.get(key)` 대신 `last_used_map[key]` 로 씀 | 이력 없는 키를 꺼내려다 멈춤 | `KeyError: 'gaeun:ACCOUNT:CHANGE'` |

첫째 경계 실수를 실행하면 다음처럼 됩니다.

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

둘째 실수는 이력이 없으면 일 수를 계산할 수 없어서 생깁니다. 이력이 있을 때(`elif`)만 계산해야 합니다. 셋째 실수는 `[ ]` 로 꺼내면 없는 키에서 오류가 나기 때문이고, `.get` 은 없는 키에 `None` 을 돌려줍니다.

**관제에서는** — 미사용 후보는 곧바로 회수하지 않고, 권한 소유자와 그 상급자에게 「계속 필요한가」를 확인하는 요청을 보냅니다. 응답이 없으면 한 단계 낮은 권한으로 줄였다가 문제가 없으면 회수합니다. 확인 요청과 응답은 점검 이력으로 남깁니다.

---

## 응용 3-1 정답

> 여기부터는 **응용(여유가 되면)** 정답입니다. 내가 한 응용의 정답만 봅니다.

**터미널에 입력합니다.**

```bash
python apply3-1_run.py
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

- (가) 출력은 다음과 같고, 규칙에 걸린 권한은 **7건**입니다.

| 이유 | 건수 | 걸린 권한 |
|---|---|---|
| 퇴사한 계정 | 3건 | dami 의 역할 권한 2건과 예외 3번 |
| 만료된 예외 | 4건 | 예외 1 · 2 · 4 · 5번 |

dami 의 예외 3번은 만료 시각(2026-10-31 18:00)이 아직 안 지났지만 퇴사한 계정이라 퇴사로 걸렸습니다.

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

**자주 틀리는 곳**

| 실수 | 결과 |
|---|---|
| `entry.get("expires")` 대신 `entry["expires"]` 로 꺼냄 (가장 많음) | 역할로 받은 권한에는 `expires` 키가 없어 첫 줄에서 바로 멈춤 (`KeyError`) |
| `if` 두 개를 따로 씀 (`elif` 대신) | 퇴사한 사람의 만료된 예외가 만료 이유로 덮어써질 수 있음 |
| 걸린 권한을 복사하지 않고 `entry["reason"] = reason` 으로 씀 | 원래 현황 권한이 바뀌어, 같은 현황 리스트를 다른 점검에 다시 쓸 때 `reason` 키가 섞여 들어감 |

첫째 실수를 실행하면 다음처럼 됩니다.

```
Traceback (most recent call last):
  File "…/파일이름.py", line 8, in <module>
    stale = find_stale(access_list, NOW)                             # 규칙에 걸린 권한을 찾는다
  File "…/파일이름.py", line 11, in find_stale
    expires = entry["expires"]                           # 만료 시각을 꺼낸다
KeyError: 'expires'
```

**관제에서는** — 규칙으로 걸리는 권한은 매주 자동으로 리스트를 뽑아 담당자에게 보내고, 처리하지 않은 채 몇 주째 남아 있는 권한은 따로 표시합니다. 같은 계정이 반복해서 걸리면 퇴사 처리 절차(인사 시스템과 권한 시스템의 연동)에 빠진 곳이 있다는 뜻으로 봅니다.

---

## 응용 3-2 정답

**터미널에 입력합니다.**

```bash
pwd
python apply3-2_run.py
```

**채운 코드** (한 예) — 직접 쓰는 곳은 다섯 함수입니다.

① `entry_key` 안(미리 채운 첫 줄 아래)

```python
    key = key + ":" + entry["source"]                            # 받은 방식을 이어 붙여 식별 키를 만든다
```

② `make_stale_reason` 안(미리 채운 `item_key` 줄 아래)

```python
        stale_reason[item_key] = item["reason"]                  # 식별 키로 걸린 이유를 찾을 수 있게 담는다
```

③ `make_unused_keys` 안(미리 채운 `item_key` 줄 아래)

```python
        unused_keys.append(item_key)                             # 식별 키를 리스트에 추가한다
```

④ `collect_reasons` 안(미리 채운 `reasons = []` 아래)

```python
    if key in stale_reason:                                      # 규칙에 걸린 권한이면
        reasons.append(stale_reason[key])                        # 걸린 이유를 추가한다
    if key in unused_keys:                                       # 안 쓴 권한이면
        reasons.append(f"{days}일 넘게 안 씀(이력 없음 포함)")   # 안 쓴 이유를 추가한다
```

⑤ `generate_report` 안(미리 채운 `reasons = collect_reasons(…)` 아래)

```python
        if len(reasons) > 0:                                     # 이유가 하나라도 있으면
            finding = entry.copy()                               # 권한을 복사해서
            finding["reasons"] = reasons                         # 복사본에 이유 리스트를 적고
            findings.append(finding)                             # 후보에 추가한다
```

**결과**

- (가) 출력은 다음과 같고, 후보는 **10건**입니다.
  - 규칙에 걸린 권한이 7건, 90일 넘게 안 쓴 권한이 8건이고, 그중 5건은 두 점검에 모두 걸렸습니다. 그래서 7 + 8 − 5 = 10건이 후보이고, 이유가 둘인 후보는 **5건**입니다.
  - 후보가 아닌 권한은 4개(`seoyeon SALES:QUERY` · `junho SETTLE:QUERY` · `gaeun ACCOUNT:QUERY` · `batch-night SETTLE:QUERY`)입니다.

```
--- 단계 1: 요약 - 점검 14 건 중 후보 10 건 ( 2026-10-29 14:00 )
seoyeon SALES:CHANGE <- 역할 sales | 90일 넘게 안 씀(이력 없음 포함)
junho SALES:QUERY <- 역할 finance | 90일 넘게 안 씀(이력 없음 포함)
gaeun ACCOUNT:CHANGE <- 역할 account_admin | 90일 넘게 안 씀(이력 없음 포함)
dami SALES:QUERY <- 역할 sales | 퇴사한 계정
dami SALES:CHANGE <- 역할 sales | 퇴사한 계정, 90일 넘게 안 씀(이력 없음 포함)
seoyeon SETTLE:QUERY <- 예외 1번 | 만료된 예외, 90일 넘게 안 씀(이력 없음 포함)
junho SALES:CHANGE <- 예외 2번 | 만료된 예외, 90일 넘게 안 씀(이력 없음 포함)
dami SALES:QUERY <- 예외 3번 | 퇴사한 계정
batch-night SALES:QUERY <- 예외 4번 | 만료된 예외, 90일 넘게 안 씀(이력 없음 포함)
gaeun SETTLE:QUERY <- 예외 5번 | 만료된 예외, 90일 넘게 안 씀(이력 없음 포함)
--- 단계 2: 확인 - 후보가 아닌 권한
['seoyeon SALES:QUERY', 'junho SETTLE:QUERY', 'gaeun ACCOUNT:QUERY', 'batch-night SETTLE:QUERY']
```

- (나) 출력에서 이유가 둘인 후보는 예를 들어 `seoyeon SETTLE:QUERY <- 예외 1번 | 만료된 예외, 90일 넘게 안 씀(이력 없음 포함)` 입니다.
  - 기간이 끝난 예외인데 사용 이력도 없다는 뜻입니다.
  - 회수해도 되는 근거가 둘이라, 이유가 하나뿐인 후보보다 회수해도 되는지 판단하기 쉽습니다.
  - 이유를 리스트로 담으면 담당자가 ① 이유가 여럿인 권한을 확신 있게 먼저 처리하고 ② 이유가 하나뿐인 권한은 그 이유가 퇴사처럼 충분히 강한지, 더 확인이 필요한지 가려서 처리하고 ③ 나중에 이유별로 집계할 수 있습니다.
  - 이유를 문자열 하나로 담으면 둘 중 하나가 덮어써져 사라지고, 이유가 둘인 권한도 하나뿐인 권한과 구별되지 않습니다.
- (다) 후보만 담으면 파일이 짧아 읽기 쉽고, 담당자가 바로 처리할 대상만 보입니다.
  - 후보가 아닌 권한까지 담으면 파일이 길어지지만 「점검했는데 문제없었다」는 근거가 남아 감사(점검 기록을 검토받는 일) 때 도움이 됩니다. 또 점검이 빠뜨린 권한이 있는지도 확인할 수 있습니다.
  - 실무에서는 두 방법을 섞습니다.
  - 후보를 본문에 담고, 점검한 전체 건수(`total`)와 점검 기준(예: 90일)을 함께 남겨 「몇 건을 어떤 기준으로 봤는지」를 증명합니다.
  - 어느 쪽이든 이유를 들면 맞습니다.

**왜**

- 점검 결과가 여러 곳에서 나올수록 담당자가 맞춰 보는 일이 늘고 빠뜨리기 쉽습니다.
  - 이유를 리스트로 권한 한 건에 모으면 한 장만 보고 처리 순서를 정할 수 있습니다.
  - 식별 키에 `source` 까지 넣은 이유는, dami 의 `SALES:QUERY` 처럼 같은 사용자의 같은 권한이 역할과 예외 두 건으로 나올 때 둘을 구별하기 위해서입니다.

**자주 틀리는 곳**

| 실수 | 결과 |
|---|---|
| `if len(reasons) > 0:` 검사를 빼먹음 | 이유가 하나도 없는 권한까지 후보에 들어감 (점검한 14건이 전부 후보) |
| `finding = entry.copy()` 대신 `finding = entry` 로 씀 | 원래 현황 권한에도 `reasons` 키가 붙어, 다른 곳에서 같은 현황을 쓸 때 이유 키가 섞여 나옴 |

첫째 실수를 실행하면 다음처럼 후보가 14건이 됩니다.

```
--- 단계 1: 요약 - 점검 14 건 중 후보 14 건 ( 2026-10-29 14:00 )
seoyeon SALES:QUERY <- 역할 sales |
seoyeon SALES:CHANGE <- 역할 sales | 90일 넘게 안 씀(이력 없음 포함)
junho SALES:QUERY <- 역할 finance | 90일 넘게 안 씀(이력 없음 포함)
…
```

**관제에서는**

- 리포트 한 장에서 이유가 둘 이상인 후보를 먼저 보고, 이유가 하나인 후보는 이유별로 묶어 처리합니다.
  - 후보 리스트와 점검 기준(일 수 · 기준 시각)을 항상 함께 남깁니다.

---

## 응용 3-3 정답

**터미널에 입력합니다.**

```bash
pwd
python apply3-3_run.py
```

**채운 코드** (한 예) — 직접 쓰는 곳은 네 함수입니다.

① `exclude_key` 안(미리 채운 `permission` 줄 아래)

```python
    return f"{user}:{permission}"                                # 사용자와 권한을 : 로 이어 붙인다
```

② `load_exclude_map` 안(미리 채운 `item_key` 줄 아래)

```python
        exclude_map[item_key] = item["reason"]                   # 그 문자열을 키로, 제외 이유를 값으로 담는다
```

③ `can_exclude` 안

```python
    key = exclude_key(finding)                                   # 「사용자:권한」 문자열을 만든다
    in_exclude_list = key in exclude_map                         # 제외 리스트에 있는지
    is_resigned = "퇴사한 계정" in finding["reasons"]              # 이유에 「퇴사한 계정」이 있는지
    return in_exclude_list and not is_resigned                   # 제외 리스트에 있고 퇴사한 계정이 아니면 True 를 리턴한다
```

④ `split_by_exclude` 안(미리 채운 `key` 줄 아래)

```python
        if can_exclude(finding, exclude_map):                    # 회수 제외해도 되는 후보이면
            reason = exclude_map[key]                            # 그 후보의 제외 이유
            excluded_entry = make_excluded(finding, reason)      # 회수 제외 후보 한 건을 만든다
            excluded.append(excluded_entry)                      # 제외 이유를 적은 복사본을 회수 제외에 추가한다
        else:                                                    # 그렇지 않으면
            to_revoke.append(finding)                            # 회수 대상에 추가한다
```

**결과**

- (가) 출력은 다음과 같고, 후보 10건 중 회수 대상은 **8건**, 회수 제외는 **2건**입니다.
  - 회수 제외는 서연의 `SALES:CHANGE`(6월 말 · 12월 말 결산 때만 씀)와 가은의 `ACCOUNT:CHANGE`(계정에 사고가 났을 때만 씀)입니다.

```
--- 단계 1: 분류 - 후보 10 건 중 회수 대상 8 건, 회수 제외 2 건
--- 단계 2: 제외 - 회수 제외한 후보와 제외 이유
seoyeon SALES:CHANGE <- 역할 sales | 6월 말 · 12월 말 결산 때만 쓰는 권한
gaeun ACCOUNT:CHANGE <- 역할 account_admin | 계정에 사고가 났을 때만 쓰는 권한이라 평소에는 쓰지 않음
--- 단계 3: 확인 - 제외 리스트에 있지만 회수 대상으로 남은 후보
dami SALES:QUERY <- 역할 sales | 퇴사한 계정
dami SALES:QUERY <- 예외 3번 | 퇴사한 계정
```

- (나) 다미는 퇴사한 계정이기 때문입니다.
  - 퇴사한 사람의 권한을 「일을 넘겨받을 사람이 정해질 때까지 필요」라는 이유로 남겨 두면, 이미 회사에 없는 사람의 계정에 권한이 계속 부여된 채로 남습니다.
  - 그 계정을 다른 사람이 몰래 쓸 수 있습니다.
  - 그래서 퇴사한 계정은 제외 리스트에 있어도 제외하지 않고 회수 대상에 둡니다.
  - 일을 넘겨받는 사람이 필요하면 그 사람에게 권한을 따로 부여해야 합니다.
- (다) 제외 리스트에는 제외하는 기간을 적는 곳이 없어서, 한 번 적은 권한을 아무도 다시 확인하지 않으면 필요 없어진 뒤에도 권한이 계속 남습니다.
  - 리스트가 길어지면 어떤 권한이 아직 필요한지 아무도 모르게 됩니다.
  - 리스트에 권한을 추가할 때는 적은 담당자와 다른 사람(예: 팀장이나 보안 책임자)이 이유를 보고 확인하고, 권한마다 다시 확인할 날짜를 정해 두는 방법이 좋습니다.
  - 이유가 맞으면 다른 방법도 인정합니다.

**왜**

- 점검 결과는 판단을 돕는 자료이고 최종 결정이 아닙니다.
  - 사람이 정한 회수 제외 리스트를 코드가 반영해야 필요한 권한이 없어지지 않습니다.
  - 다만 리스트에 잘못 적혀도 퇴사한 사람의 권한만큼은 열려 있으면 위험하므로, 퇴사한 계정은 코드가 막습니다.

**자주 틀리는 곳**

- `can_exclude` 의 `and not is_resigned` 조건을 빼먹으면 퇴사한 다미까지 회수 제외가 됩니다.
  - 오류는 나지 않고 숫자만 달라집니다.
  - 실행하면 다음처럼 됩니다(회수 제외가 2건이어야 하는데 4건이 되고 단계 3이 비면 이 실수입니다).

```
--- 단계 1: 분류 - 후보 10 건 중 회수 대상 6 건, 회수 제외 4 건
```

**관제에서는**

- 회수 제외 리스트를 바꿀 때마다 바꾼 사람 · 승인한 사람 · 날짜를 남기고, 점검 리포트에 제외한 건수를 함께 적습니다.
  - 권한을 적은 날짜를 따로 기록해 두고, 가장 오래된 권한도 같이 봅니다.

---
