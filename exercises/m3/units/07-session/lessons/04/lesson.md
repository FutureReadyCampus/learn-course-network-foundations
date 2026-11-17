---
id: m3-u07-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/088_day04_pm_overprivilege.md
  mission_id: GichanSource.m3-1029-pm-overprivilege
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## Exercise 7-1 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise7-1_run.py
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
  - 규칙에 걸린 7건과 90일 넘게 안 쓴 8건 가운데 5건이 두 점검에 모두 걸려서(7 + 8 − 5 = 10) 이유가 둘인 후보가 **5건**입니다.
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
  - 후보가 아닌 권한까지 담으면 파일이 길어지지만 「점검했는데 문제없었다」는 근거가 남아 감사(점검 기록을 검토받는 일) 때 도움이 되고 점검이 빠뜨린 권한이 있는지도 확인할 수 있습니다.
  - 실무에서는 두 방법을 섞습니다.
  - 후보를 본문에 담고, 점검한 전체 건수(`total`)와 점검 기준(예: 90일)을 함께 남겨 「몇 건을 어떤 기준으로 봤는지」를 증명합니다.
  - 어느 쪽이든 이유를 들면 맞습니다.

**왜**

- 점검 결과가 여러 곳에서 나올수록 담당자가 맞춰 보는 일이 늘고 빠뜨리기 쉽습니다.
  - 이유를 리스트로 권한 한 건에 모으면 한 장만 보고 처리 순서를 정할 수 있습니다.
  - 식별 키에 `source` 까지 넣은 이유는, dami 의 `SALES:QUERY` 처럼 같은 사용자의 같은 권한이 역할과 예외 두 건으로 나올 때 둘을 구별하기 위해서입니다.

**자주 틀리는 곳**

- `if len(reasons) > 0:` 검사를 빼먹으면 이유가 하나도 없는 권한까지 후보에 들어갑니다.
  - 실행하면 다음처럼 후보가 14건이 됩니다(점검한 14건이 전부 후보로 나오면 이 실수입니다).

```
--- 단계 1: 요약 - 점검 14 건 중 후보 14 건 ( 2026-10-29 14:00 )
seoyeon SALES:QUERY <- 역할 sales |
seoyeon SALES:CHANGE <- 역할 sales | 90일 넘게 안 씀(이력 없음 포함)
junho SALES:QUERY <- 역할 finance | 90일 넘게 안 씀(이력 없음 포함)
…
```

`finding = entry.copy()` 대신 `finding = entry` 로 쓰면 원래 현황 권한에도 `reasons` 키가 붙어 버립니다. 그러면 다른 곳에서 같은 현황을 쓸 때 이유 키가 섞여 나옵니다.

**관제에서는**

- 리포트 한 장에서 이유가 둘 이상인 후보를 먼저 보고, 이유가 하나인 후보는 이유별로 묶어 처리합니다.
  - 후보 리스트와 점검 기준(일 수 · 기준 시각)을 항상 함께 남깁니다.

---

## Exercise 7-2 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise7-2_run.py
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

## 정답 마무리

**터미널에 입력합니다.**

```bash
cd ..
pwd
git status
git add .
git commit -m "Add access control access review and overprivilege report"
git push
```

**결과**

- (가) 한 예: 「줄이 열여섯 개였고(`.py` 열 개 + `config/access_log.json` · `config/exclude_list.json` 두 개 + `.md` 네 개), `.env` · `.venv` 는 없었다」. 이 숫자는 Unit 5의 파일을 이미 올렸고 `__pycache__` 가 보이지 않을 때의 숫자이며, 줄 수와 이름은 학생마다 다를 수 있습니다.
  - `.env` 나 `.venv` 가 보였다면 `.gitignore` 에 한 줄을 적고 `git status` 를 다시 쳤다고 적습니다.

**왜**

- 올리기 전에 올라갈 파일을 확인해야 비밀 키가 섞이지 않습니다.
  - 코드와 이번 Unit에서 만든 회수 제외 리스트가 함께 올라가야 Unit 8의 회수 실습이 같은 기준에서 시작합니다.

**자주 틀리는 곳**

- `.env` 가 보이는데 그대로 `git add .` 를 하는 실수가 가장 위험합니다.
  - `cd ..` 를 두 번 쳐서 `security-agent-toolkit` 바깥으로 나가는 경우도 있습니다.
  - `pwd` 로 확인합니다.

**관제에서는**

- 점검 코드와 회수 제외 리스트는 같은 커밋에 함께 올려, 어느 코드와 어느 리스트로 점검했는지 이력으로 남깁니다.

---

## 앞 Exercise 파일 완성본

앞 Exercise 파일을 못 만들고 다음 Exercise로 넘어가야 할 때 그대로 만들어 씁니다. Unit 6의 파일(`review_list.py` · `review_rules.py` · `review_unused.py` · `config/access_log.json`)은 Unit 6 문서 맨 아래에 있습니다. 정답 본문을 함수 머리말과 합친 전체 파일입니다.

**`overprivilege.py`** (Exercise 7-1 완성본)

```python
def entry_key(entry):                                            # 현황의 권한 한 건의 식별 키를 만드는 함수
    """현황의 권한 한 개의 식별 키를 리턴한다.
    키는 user:permission:source 를 이어 붙인 문자열이다.
    같은 권한을 찾아 비교할 때 쓴다.
    """
    key = entry["user"] + ":" + entry["permission"]              # 사용자와 권한을 : 로 이어 붙이고
    key = key + ":" + entry["source"]                            # 받은 방식을 이어 붙여 식별 키를 만든다
    return key                                                   # 식별 키를 리턴한다


def make_stale_reason(stale):                                    # 규칙에 걸린 권한 리스트를 받는 함수
    """규칙에 걸린 권한의 식별 키를 키로, 걸린 이유를 값으로 하는 딕셔너리를 리턴한다.
    필요 없어진 권한에 이유를 붙일 때 쓴다.
    """
    stale_reason = {}                                            # 식별 키 → 걸린 이유를 담을 빈 딕셔너리
    for item in stale:                                           # 규칙에 걸린 권한을 하나씩 꺼낸다
        item_key = entry_key(item)                               # 그 권한의 식별 키를 만든다
        stale_reason[item_key] = item["reason"]                  # 식별 키로 걸린 이유를 찾을 수 있게 담는다
    return stale_reason                                          # 딕셔너리를 리턴한다


def make_unused_keys(unused):                                    # 안 쓴 권한 리스트를 받는 함수
    """안 쓴 권한의 식별 키 리스트를 리턴한다.
    안 쓴 권한을 다른 점검 결과와 비교할 때 쓴다.
    """
    unused_keys = []                                             # 안 쓴 권한의 식별 키를 담을 빈 리스트
    for item in unused:                                          # 안 쓴 권한을 하나씩 꺼낸다
        item_key = entry_key(item)                               # 식별 키를 만든다
        unused_keys.append(item_key)                             # 식별 키를 리스트에 추가한다
    return unused_keys                                           # 리스트를 리턴한다


def collect_reasons(key, stale_reason, unused_keys, days):       # 식별 키 · 걸린 이유 딕셔너리 · 안 쓴 권한의 식별 키 리스트 · 기준 일 수를 받는 함수
    """그 권한에 해당하는 과다권한 이유를 모아 리스트로 리턴한다(없으면 빈 리스트).
    후보마다 왜 걸렸는지 적을 때 쓴다.
    """
    reasons = []                                                 # 이유를 담을 빈 리스트
    if key in stale_reason:                                      # 규칙에 걸린 권한이면
        reasons.append(stale_reason[key])                        # 걸린 이유를 추가한다
    if key in unused_keys:                                       # 안 쓴 권한이면
        reasons.append(f"{days}일 넘게 안 씀(이력 없음 포함)")   # 안 쓴 이유를 추가한다
    return reasons                                               # 이유 리스트를 리턴한다


def generate_report(access_list, stale, unused, days, generated_at):   # 현황 · 규칙 결과 · 안 쓴 결과 · 기준 일 수 · 만든 시각 문자열을 받는 함수
    """과다권한 후보 리포트(딕셔너리)를 리턴하고 후보마다 "reasons" 키에 이유 리스트를 적는다.
    점검 결과를 한눈에 정리해 보고할 때 쓴다.
    """
    stale_reason = make_stale_reason(stale)                      # 규칙에 걸린 권한의 식별 키 → 걸린 이유 딕셔너리를 만든다
    unused_keys = make_unused_keys(unused)                       # 안 쓴 권한의 식별 키 리스트를 만든다
    findings = []                                                # 후보를 담을 빈 리스트
    for entry in access_list:                                    # 현황의 권한을 한 건씩 꺼낸다
        key = entry_key(entry)                                   # 그 권한의 식별 키를 만든다
        reasons = collect_reasons(key, stale_reason, unused_keys, days)   # 그 권한에 해당하는 이유를 모은다
        if len(reasons) > 0:                                     # 이유가 하나라도 있으면
            finding = entry.copy()                               # 권한을 복사해서
            finding["reasons"] = reasons                         # 복사본에 이유 리스트를 적고
            findings.append(finding)                             # 후보에 추가한다
    report = {                                                   # 리포트 딕셔너리를 만든다
        "generated_at": generated_at,                            # 리포트를 만든 시각
        "total": len(access_list),                               # 점검한 전체 권한 수
        "finding_count": len(findings),                          # 후보 수
        "findings": findings,                                    # 후보 리스트
    }
    return report                                                # 리포트를 리턴한다
```

**`report_exclude.py`** (Exercise 7-2 완성본)

```python
from config_loader import load_json                              # Unit 3에서 만든 안전한 읽기 함수를 불러온다


def exclude_key(entry):                                          # 사용자와 권한이 든 딕셔너리(후보 또는 제외 리스트의 한 건)를 받는 함수
    """「사용자:권한」 문자열을 리턴한다.
    제외 리스트와 점검 후보를 비교하는 키로 쓴다.
    """
    user = entry["user"]                                         # 그 권한의 사용자
    permission = entry["permission"]                             # 그 권한의 권한 이름
    return f"{user}:{permission}"                                # 사용자와 권한을 : 로 이어 붙인다


def make_excluded(finding, reason):                              # 후보 한 건과 제외 이유 문자열을 받는 함수
    """후보를 복사해 "exclude_reason" 키(제외 이유)를 적는다.
    회수에서 뺀 후보에 이유를 남길 때 쓴다(원래 후보는 바꾸지 않음).
    """
    item = finding.copy()                                        # 원래 후보는 바꾸지 않고 복사한다
    item["exclude_reason"] = reason                              # 복사본에 제외 이유를 적는다
    return item                                                  # 복사본을 리턴한다


def load_exclude_map(path):                                      # 회수 제외 리스트 파일 경로를 받는 함수
    """회수 제외 리스트 파일을 읽어 「사용자:권한」을 키로, 제외 이유를 값으로 하는 딕셔너리를 리턴한다.
    계속 필요한 권한을 가려낼 준비를 할 때 쓴다.
    """
    exclude_map = {}                                             # 빈 딕셔너리로 시작한다
    for item in load_json(path, []):                             # 제외 리스트의 권한을 한 건씩 꺼낸다(파일이 없으면 빈 리스트)
        item_key = exclude_key(item)                             # 그 권한의 「사용자:권한」 문자열을 만든다
        exclude_map[item_key] = item["reason"]                   # 그 문자열을 키로, 제외 이유를 값으로 담는다
    return exclude_map                                           # 딕셔너리를 리턴한다


def can_exclude(finding, exclude_map):                           # 후보 한 건과 제외 이유 딕셔너리를 받는 함수
    """후보를 회수 제외해도 되는지 알려 준다.
    계속 필요한 권한을 가려낼 때 쓰며, 퇴사한 계정은 제외하지 않는다.
    """
    key = exclude_key(finding)                                   # 「사용자:권한」 문자열을 만든다
    in_exclude_list = key in exclude_map                         # 제외 리스트에 있는지
    is_resigned = "퇴사한 계정" in finding["reasons"]              # 이유에 「퇴사한 계정」이 있는지
    return in_exclude_list and not is_resigned                   # 제외 리스트에 있고 퇴사한 계정이 아니면 True 를 리턴한다


def split_by_exclude(findings, exclude_map):                     # 후보 리스트와 제외 이유 딕셔너리를 받는 함수
    """후보를 (회수 대상 후보 리스트, 회수 제외 후보 리스트)로 나눠 리턴한다.
    이유에 「퇴사한 계정」이 있으면 제외하지 않으며, 회수할 것과 남길 것을 가를 때 쓴다.
    """
    to_revoke = []                                               # 회수 대상을 담을 빈 리스트
    excluded = []                                                # 회수 제외를 담을 빈 리스트
    for finding in findings:                                     # 후보를 하나씩 꺼낸다
        key = exclude_key(finding)                               # 「사용자:권한」 문자열을 만든다
        if can_exclude(finding, exclude_map):                    # 회수 제외해도 되는 후보이면
            reason = exclude_map[key]                            # 그 후보의 제외 이유
            excluded_entry = make_excluded(finding, reason)      # 회수 제외 후보 한 건을 만든다
            excluded.append(excluded_entry)                      # 제외 이유를 적은 복사본을 회수 제외에 추가한다
        else:                                                    # 그렇지 않으면
            to_revoke.append(finding)                            # 회수 대상에 추가한다
    return to_revoke, excluded                                   # 두 리스트를 함께 리턴한다
```

**`config/exclude_list.json`** (Exercise 7-2 완성본)

```json
[
  {"user": "gaeun", "permission": "ACCOUNT:CHANGE", "reason": "계정에 사고가 났을 때만 쓰는 권한이라 평소에는 쓰지 않음"},
  {"user": "seoyeon", "permission": "SALES:CHANGE", "reason": "6월 말 · 12월 말 결산 때만 쓰는 권한"},
  {"user": "dami", "permission": "SALES:QUERY", "reason": "일을 넘겨받을 사람이 정해질 때까지 필요"}
]
```
