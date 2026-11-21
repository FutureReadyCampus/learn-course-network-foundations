---
id: m3-u03-l03
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

**실습 3-2를 시작하기 전에** 이 레슨의 파일 네 개를 만듭니다. 실습 3-2 의 실행 파일이 퇴사 · 만료 규칙 함수 `find_stale` 을 불러 쓰는데, 그 함수는 응용 3-1 에서 만드는 것이라 오늘은 완성본을 받아 씁니다. 나머지 세 파일은 다음 Unit 4 가 쓰는 파일이라 오늘 함께 만들어 둡니다.

만들 파일은 네 개입니다.

| 파일 | 들어 있는 것 | 하는 일 | 쓰는 곳 |
|---|---|---|---|
| `review_rules.py` | 함수 `find_stale` | 퇴사한 계정과 만료된 예외를 찾음 | 실습 3-2 |
| `overprivilege.py` | 함수 `generate_report` | 규칙 결과와 안 쓴 결과를 합쳐 과다권한 후보 리포트를 만듦 | Unit 4 |
| `report_exclude.py` | 함수 `split_by_exclude` | 후보를 「회수 대상」과 「회수 제외」로 나눔 | Unit 4 |
| `config/exclude_list.json` | 회수 제외 리스트 | 회수하지 않을 권한 세 건을 적어 둠 | Unit 4 |

1. 파일은 모두 `access_control` 폴더 안에 만듭니다. 만드는 방법은 실습 3-1 과 같습니다(VS Code 왼쪽 목록에서 `access_control` 폴더를 고르고 **새 파일** 아이콘).
2. 아래 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 네 파일을 다 만들었으면 터미널에서 `ls` 와 `ls config` 로 파일 이름이 보이는지 확인하고 실습 3-2로 돌아갑니다.

> 응용 3-1 ~ 3-3(여유가 되면 해 보세요)을 하면, 이 파일들을 빈칸이 있는 골격으로 바꿔 직접 써 봅니다. 그때는 본문을 다 채울 때까지 실습 3-2 가 동작하지 않을 수 있으니, 다 쓴 뒤 `exercise3-2_run.py` 를 다시 실행해 결과가 같은지 확인합니다.

> **확인** — 만들 파일 네 개의 이름과, 그중 오늘 실습 3-2 가 쓰는 파일이 `review_rules.py` 라는 것을 말할 수 있으면 성공입니다. 헷갈리면 위 표의 「쓰는 곳」 칸을 봅니다.

## `review_rules.py` 만들기

**`review_rules.py`** 를 만들고 아래 내용을 붙여 넣습니다. `find_stale` 은 현황의 권한마다 퇴사한 계정인지, 만료된 예외인지를 차례로 보고, 걸린 권한을 복사해 이유(`reason`)를 적은 리스트를 리턴합니다.

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

> **확인** — VS Code 왼쪽 목록에서 `access_control` 바로 아래(`config` 안이 아님)에 `review_rules.py` 이 보이고, 탭 제목 옆에 저장 안 됨 표시(●)가 없으면 성공입니다. `config` 안에 만들어졌으면 `access_control` 로 끌어다 옮깁니다.

## `overprivilege.py` 만들기

**`overprivilege.py`** 를 만들고 아래 내용을 붙여 넣습니다. `generate_report` 는 권한 한 건마다 「사용자:권한:받은 방식」 식별 키(권한 한 건을 다른 권한과 구별하는 문자열)를 만들어 두 점검 결과의 이유를 모으고, 이유가 있는 권한만 후보로 담은 리포트 딕셔너리를 리턴합니다. 오늘 실습에서는 쓰지 않고, 다음 Unit 4 가 씁니다.

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

> **확인** — VS Code 왼쪽 목록에서 `access_control` 바로 아래(`config` 안이 아님)에 `overprivilege.py` 이 보이고, 탭 제목 옆에 저장 안 됨 표시(●)가 없으면 성공입니다. `config` 안에 만들어졌으면 `access_control` 로 끌어다 옮깁니다.

## `report_exclude.py` 만들기

**`report_exclude.py`** 를 만들고 아래 내용을 붙여 넣습니다. `split_by_exclude` 는 후보가 회수 제외 리스트에 있으면 「회수 제외」로, 아니면 「회수 대상」으로 나눕니다. 퇴사한 계정의 권한은 제외 리스트에 있어도 회수 대상에 둡니다. 오늘 실습에서는 쓰지 않고, 다음 Unit 4 가 씁니다.

```python
from config_loader import load_json                              # config_loader.py 의 안전한 읽기 함수를 불러온다


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

> **확인** — VS Code 왼쪽 목록에서 `access_control` 바로 아래(`config` 안이 아님)에 `report_exclude.py` 이 보이고, 탭 제목 옆에 저장 안 됨 표시(●)가 없으면 성공입니다. `config` 안에 만들어졌으면 `access_control` 로 끌어다 옮깁니다.

## `config/exclude_list.json` 만들기

**`config/exclude_list.json`** 을 만들고 아래 내용을 붙여 넣습니다. `access_control` 안의 `config` 폴더에 만듭니다(`access_control` 폴더를 선택한 채로 이름에 `config/exclude_list.json` 을 입력하면 `config` 폴더 안에 만들어집니다). 담당자가 「평소에 안 써도 회수하면 안 되는 권한」을 적어 둔 회수 제외 리스트이고, 한 줄이 한 건입니다.

<pre class="copyable"><code>[
  {"user": "gaeun", "permission": "ACCOUNT:CHANGE", "reason": "계정에 사고가 났을 때만 쓰는 권한이라 평소에는 쓰지 않음"},
  {"user": "seoyeon", "permission": "SALES:CHANGE", "reason": "6월 말 · 12월 말 결산 때만 쓰는 권한"},
  {"user": "dami", "permission": "SALES:QUERY", "reason": "일을 넘겨받을 사람이 정해질 때까지 필요"}
]
</code></pre>

- 저장한 뒤 터미널에서 JSON 규칙에 맞는지 확인합니다. 세 건이 다시 정리되어 나오면 됩니다.
  ```bash
  python -m json.tool config/exclude_list.json
  ```
  - 명령 풀이: `python -m json.tool` 파이썬의 JSON 검사 도구를 실행 · `config/exclude_list.json` 검사할 파일 (맥북은 `python3`)
- 모두 만들었으면 터미널에서 확인합니다. `review_rules.py` · `overprivilege.py` · `report_exclude.py` 와 `config` 안의 `exclude_list.json` 이 보이면 실습 3-2로 갑니다.
  ```bash
  ls
  ls config
  python -c "import review_rules, overprivilege, report_exclude; print('제공 파일 정상')"
  ```
  - 마지막 줄은 세 파일을 불러와 보는 명령입니다(맥북은 `python3`).

> **확인** — 마지막 줄에 `제공 파일 정상` 이 나오면 성공입니다. `ModuleNotFoundError` 가 나면 그 이름의 파일이 `access_control` 바로 아래에 없는 것이고, `SyntaxError` 가 나면 붙여 넣을 때 글자가 빠진 것이니 그 파일을 지우고 다시 복사합니다.
