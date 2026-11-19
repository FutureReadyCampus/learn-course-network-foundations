---
id: m3-u03-l04
title: 제공 파일
render: markdown
---

# 제공 파일

## `review_rules.py` 만들기

**`review_rules.py`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.

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

## `overprivilege.py` 만들기

**`overprivilege.py`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.

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

## `report_exclude.py` 만들기

**`report_exclude.py`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.

```python
from config_loader import load_json                              # Unit 1에서 만든 안전한 읽기 함수를 불러온다


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
