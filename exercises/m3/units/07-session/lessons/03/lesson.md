---
id: m3-u07-l03
title: Exercise 7-2 · 회수하지 않을 권한을 가려내기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/088_day04_pm_overprivilege.md
  mission_id: GichanSource.m3-1029-pm-overprivilege
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 7-2 · 회수하지 않을 권한을 가려내기

## 개요

> **오늘 들어온 일**
>
> A사 관제 담당이 보낸 메시지:
> 「점검 결과 후보 10건 가운데 평소에 안 쓰는 것이 정상인 권한이 두 개 있습니다.
> - 가은의 `ACCOUNT:CHANGE`(계정 설정을 바꾸는 권한): 계정에 사고가 났을 때만 씁니다.
> - 서연의 `SALES:CHANGE`(영업 자료를 바꾸는 권한): 6월 말과 12월 말, 반년에 한 번 결산 때만 씁니다.
>
> 내일 권한을 회수할 때 이 두 권한까지 없어지면 필요한 날 일을 못 합니다. 회수하지 않을 권한은 파일에 적어 둘 테니, 후보를 「회수 대상」과 「회수 제외」로 나눠 주세요.」
> - **왜 중요한가**: 후보를 전부 회수하면, 가은은 계정에 사고가 난 날 서연은 결산하는 날 필요한 권한이 없어 일을 못 합니다. 그래서 회수하기 전에 「회수 제외」를 먼저 가려냅니다.

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「 문제」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 읽기 · 왜 필요한가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. Exercise 7-1 리포트의 후보 10건은 「바로 회수할 권한」이 아니라 「확인이 필요한 권한」입니다.
2. 후보 중에는 평소에 안 써도 되는 권한이 있습니다. 담당자가 이런 권한을 **회수 제외 리스트**(exclude list · 익스클루드 리스트, 줄여서 제외 리스트)에 적어 두면, 프로그램이 후보를 「회수 대상」과 「회수 제외」로 나눕니다.
3. 단, 퇴사한 사람의 권한은 제외 리스트에 있어도 제외하지 않습니다. 이미 회사에 없는 사람의 계정에 권한이 열려 있으면 다른 사람이 몰래 쓸 수 있어 위험하기 때문입니다.
4. 제외 리스트는 사람이 적기 때문에 잘못 적을 수 있습니다. 리스트에 있다는 이유만으로 무조건 믿으면, 퇴사한 사람의 권한처럼 제외하면 안 되는 것까지 남게 됩니다.

## 읽기 · 2.1 회수 제외 리스트의 모양

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

`config/exclude_list.json` 의 한 건은 아래 세 키로 이루어집니다. 제외하는 기간을 적는 키는 없습니다.

| 키 | 뜻 | 값의 예 |
|---|---|---|
| `user` | 사용자 | `"gaeun"` |
| `permission` | 권한 | `"ACCOUNT:CHANGE"` |
| `reason` | 제외하는 이유 | `"계정에 사고가 났을 때만 쓰는 권한이라 평소에는 쓰지 않음"` |

- 오늘 리스트에는 권한이 세 건 있습니다.
  - 가은(`gaeun`) `ACCOUNT:CHANGE`, 서연(`seoyeon`) `SALES:CHANGE`, 다미(`dami`) `SALES:QUERY` 입니다.
  - 메시지에는 두 개만 나왔고, 세 번째 다미 권한은 문제 (나)에서 다룹니다.
- 제외 리스트와 후보는 「사용자:권한」 문자열(예: `"gaeun:ACCOUNT:CHANGE"`)이 같은지 비교합니다.
  - Exercise 7-1의 식별 키와 달리 `source`(역할인지 예외인지)는 붙이지 않습니다.
  - 제외 리스트는 어떻게 받은 권한이든 그 사람의 그 권한을 기준으로 적기 때문입니다.
- 함수 네 개를 씁니다.
  - `exclude_key`(1번): 「사용자:권한」 문자열을 만듭니다. Exercise 7-1의 식별 키와 달리 `source` 는 넣지 않습니다.
  - `load_exclude_map`(2번): 파일을 읽어 `{"gaeun:ACCOUNT:CHANGE": "계정에 사고가 …", …}` 모양의 딕셔너리(`exclude_map`)를 만듭니다.
    - 한 줄만 씁니다.
  - `can_exclude`(3 ~ 6번): 후보를 회수 제외해도 되는지 `True` · `False` 로 알려 줍니다.
  - `split_by_exclude`(7 ~ 12번): `can_exclude` 의 결과로 후보를 둘로 나눕니다.
- `make_excluded` 는 후보를 복사해 `exclude_reason` 키(제외 이유)를 적은 복사본을 리턴합니다(판단이 없는 복사라 미리 채움).
- `reason`(제외 리스트 파일에 적힌 제외 이유 문자열)과 `reasons`(Exercise 7-1 후보에 붙은 이유 리스트)는 한 글자 차이이니 헷갈리지 마세요.
- `to_revoke`(투 리보크)는 회수 대상 리스트, `excluded`(익스클루디드)는 제외된 후보 리스트입니다.
  - 두 리스트는 `return to_revoke, excluded` 로 한꺼번에 리턴하고, 받는 쪽은 `to_revoke, excluded = …` 로 두 이름에 나눠 받습니다(리턴한 두 값이 차례로 두 이름에 들어갑니다).

```
+-----------------------------------------+
| split_by_exclude(findings, exclude_map) |
+-----------------------------------------+
   |
   v
+------------------------------------------------------------------+
| to_revoke = [] / excluded = []  (두 리스트를 비워 두고 시작한다) |
+------------------------------------------------------------------+
   |
   v
+---------------------------------------------------------+
| 후보를 하나씩 꺼내 key(「사용자:권한」 문자열)을 만든다 |
+---------------------------------------------------------+
   |
   v
+------------------------------------------------------------------------------------------+
| can_exclude(finding, exclude_map) 가 참인가? (제외 리스트에 있고, 퇴사한 계정이 아닌가?) |
+------------------------------------------------------------------------------------------+
   |
   +--> 그렇다 --> 복사본에 exclude_reason 키를 적어 excluded 에 추가한다
   |
   +--> 아니다 --> 그대로 to_revoke 에 추가한다
   |
   v  모든 후보를 꺼낸 뒤
(to_revoke, excluded) 를 리턴한다
```

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise Exercise 1-3 · 후보를 「회수 대상」과 「회수 제외」로 나누기

** 이런 상황이 있습니다**

- **지금은**: Exercise 7-1 리포트의 후보 10건이 한 리스트에 섞여 있습니다. 회수하지 않을 권한을 담당자가 눈으로 골라야 합니다.
- **그래서 만드는 것**: `split_by_exclude` 입니다.
  - 제외 리스트에 있는 후보는 `exclude_reason` 키를 붙여 「회수 제외」로, 나머지는 「회수 대상」으로 나눕니다.
  - 후보에 붙은 이유(`reasons`)에 「퇴사한 계정」이 있으면 제외 리스트에 있어도 제외하지 않습니다.
- **실행하면**: 단계 1은 분류 건수, 단계 2는 회수 제외한 후보와 이유, 단계 3은 제외 리스트에 있지만 회수 대상으로 남은 후보를 출력합니다.
- **현업에서는**: 자동 점검 도구도 회수 제외 리스트를 두고, 비상용 권한이나 사람이 아닌 프로그램용 계정의 권한을 회수 대상에서 뺍니다.

** 할 일**

1. `config/exclude_list.json` · `report_exclude.py` · `day04_6-1_run.py` 세 파일을 만들고, `exclude_key` · `load_exclude_map` · `can_exclude` · `split_by_exclude` 에서 직접 쓰는 곳 네 군데를 씁니다.
2. 실행해서 <mark>분류 건수</mark>(단계 1: 분류), <mark>회수 제외한 후보</mark>(단계 2: 제외), <mark>회수 대상으로 남은 후보</mark>(단계 3: 확인)를 읽습니다.

**`config/exclude_list.json`** — 그대로 붙여 넣습니다. 회수 제외 리스트입니다. `access_control` 안의 `config` 폴더에 만듭니다.

```json
[
  {"user": "gaeun", "permission": "ACCOUNT:CHANGE", "reason": "계정에 사고가 났을 때만 쓰는 권한이라 평소에는 쓰지 않음"},
  {"user": "seoyeon", "permission": "SALES:CHANGE", "reason": "6월 말 · 12월 말 결산 때만 쓰는 권한"},
  {"user": "dami", "permission": "SALES:QUERY", "reason": "일을 넘겨받을 사람이 정해질 때까지 필요"}
]
```

**`report_exclude.py`**

```python
from config_loader import load_json                              # 10/22(목)에 만든 안전한 읽기 함수를 불러온다


def exclude_key(entry):                                          # 사용자와 권한이 든 딕셔너리(후보 또는 제외 리스트의 한 건)를 받는 함수
    """「사용자:권한」 문자열을 리턴한다.
    제외 리스트와 점검 후보를 비교하는 키로 쓴다.
    """
    user = entry["user"]                                         # 그 권한의 사용자
    permission = entry["permission"]                             # 그 권한의 권한 이름
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. f"{user}:{permission}" 을 리턴한다 (사용자와 권한을 : 로 이어 붙인 문자열. 받은 방식 source 는 넣지 않는다)


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
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 2. exclude_map 의 item_key 키에 item["reason"] 을 담는다 (제외 이유)
    return exclude_map                                           # 딕셔너리를 리턴한다


def can_exclude(finding, exclude_map):                           # 후보 한 건과 제외 이유 딕셔너리를 받는 함수
    """후보를 회수 제외해도 되는지 알려 준다.
    계속 필요한 권한을 가려낼 때 쓰며, 퇴사한 계정은 제외하지 않는다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 3. exclude_key(finding) 을 key 에 담는다
    # 4. key 가 exclude_map 에 있는지 (in) 를 in_exclude_list 에 담는다
    # 5. "퇴사한 계정" 이 finding["reasons"] 에 있는지 (in) 를 is_resigned 에 담는다
    # 6. in_exclude_list 이고 is_resigned 가 아니면 True 가 되도록 리턴한다 (and not)


def split_by_exclude(findings, exclude_map):                     # 후보 리스트와 제외 이유 딕셔너리를 받는 함수
    """후보를 (회수 대상 후보 리스트, 회수 제외 후보 리스트)로 나눠 리턴한다.
    이유에 「퇴사한 계정」이 있으면 제외하지 않으며, 회수할 것과 남길 것을 가를 때 쓴다.
    """
    to_revoke = []                                               # 회수 대상을 담을 빈 리스트
    excluded = []                                                # 회수 제외를 담을 빈 리스트
    for finding in findings:                                     # 후보를 하나씩 꺼낸다
        key = exclude_key(finding)                               # 「사용자:권한」 문자열을 만든다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 7. can_exclude(finding, exclude_map) 가 참이면
        # 8.   exclude_map[key] 를 reason 에 담는다
        # 9.   make_excluded(finding, reason) 을 excluded_entry 에 담는다
        # 10.  excluded_entry 를 excluded 에 추가한다
        # 11. 그렇지 않으면 (else)
        # 12.   to_revoke 에 finding 을 추가한다
    return to_revoke, excluded                                   # 두 리스트를 함께 리턴한다
```

- 들여쓰기는 미리 채운 줄에 맞춥니다.
  - `exclude_key` · `can_exclude` 안: 함수 안이라 앞에 공백 4개입니다.
  - `load_exclude_map` 안: 미리 채운 `for` 안쪽이라 8개입니다.
  - `split_by_exclude` 안: 미리 채운 `for` 안쪽이라 `if` · `else` 는 8개이고, 그 안쪽(8 ~ 10번, 12번)은 4개 더(12개)입니다.
- 채우기 전에 실행하면 후보가 모두 `회수 제외 0 건` 으로 나옵니다. `can_exclude` 가 아무것도 리턴하지 않아 거짓으로 취급되기 때문입니다.

**`day04_6-1_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. Exercise 7-1와 같은 방법으로 리포트를 만든 뒤, 회수 제외 리스트를 읽어 후보를 나누고 세 단계로 출력합니다.

```python
from datetime import datetime                                    # 지금 시각을 만드는 데 쓴다
from review_list import build_access_list                        # 오전 Exercise 6-1에 만든 현황 함수를 불러온다
from review_rules import find_stale                              # 오전 Exercise 6-2에 만든 규칙 점검 함수를 불러온다
from review_unused import load_last_used, find_unused            # 오전 Exercise 6-3에 만든 안 쓴 권한 점검 함수를 불러온다
from overprivilege import generate_report                        # 오후 Exercise 7-1에 만든 리포트 함수를 불러온다
from report_exclude import load_exclude_map, split_by_exclude   # 방금 만든 회수 제외 함수를 불러온다

NOW = datetime.strptime("2026-10-29 14:00", "%Y-%m-%d %H:%M")    # 오늘 오후 실습의 지금 시각(고정)
TIME_FORMAT = "%Y-%m-%d %H:%M"                                   # 시각 문자열의 형식

access_list = build_access_list()                                # 현황을 만든다
stale = find_stale(access_list, NOW)                             # 규칙에 걸린 권한을 찾는다
last_used_map = load_last_used()                                 # 마지막 사용 시각 딕셔너리를 읽는다
unused = find_unused(access_list, last_used_map, NOW, 90)        # 같은 현황에서 90일 넘게 안 쓴 권한을 찾는다(규칙에 걸린 권한도 빼지 않고 전부 넣는다)
generated_at = NOW.strftime(TIME_FORMAT)                         # 리포트를 만든 시각을 문자열로 바꾼다
report = generate_report(access_list, stale, unused, 90, generated_at)  # Exercise 7-1와 같은 방법으로 리포트를 만든다

exclude_map = load_exclude_map("config/exclude_list.json")   # 회수 제외 리스트를 읽는다
to_revoke, excluded = split_by_exclude(report["findings"], exclude_map)   # 후보를 회수 대상과 회수 제외로 나눈다

print("--- 단계 1: 분류 - 후보", report["finding_count"], "건 중 회수 대상", len(to_revoke), "건, 회수 제외", len(excluded), "건")   # 단계 1 시작을 알리는 줄
print("--- 단계 2: 제외 - 회수 제외한 후보와 제외 이유")              # 단계 2 시작을 알리는 줄
for item in excluded:                                            # 회수 제외한 후보를 하나씩 꺼낸다
    print(item["user"], item["permission"], "<-", item["source"], "|", item["exclude_reason"])   # 사용자 · 권한 <- 출처 | 제외 이유를 출력한다

print("--- 단계 3: 확인 - 제외 리스트에 있지만 회수 대상으로 남은 후보")        # 단계 3 시작을 알리는 줄
for item in to_revoke:                                           # 회수 대상을 하나씩 꺼낸다
    item_key = item["user"] + ":" + item["permission"]           # 「사용자:권한」 문자열을 만들고
    if item_key in exclude_map:                                  # 제외 리스트에 있는 권한이면
        reasons_text = ", ".join(item["reasons"])                # 이유 리스트를 쉼표로 이어 붙인 문자열로 만든다
        print(item["user"], item["permission"], "<-", item["source"], "|", reasons_text)  # 사용자 · 권한 <- 출처 | 이유들을 출력한다
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `config/exclude_list.json` · `report_exclude.py` · `day04_6-1_run.py` 를 만들어 위 코드를 붙여 넣습니다. 만드는 법은 둘 중 하나를 고릅니다.
   - VS Code: `access_control` 폴더를 선택하고 **새 파일**(New File) 아이콘을 눌러 이름을 입력합니다(`config/…` 이름은 이 폴더를 선택한 채 입력하면 `config` 폴더 안에 만들어집니다).
   - 터미널: `pwd` 로 `access_control` 인지 확인하고 `touch 이름` 으로 만든 뒤 VS Code 에서 열어 붙여 넣습니다(`vim 이름` → `i` → 붙여넣기 → `Esc` → `:wq` 도 됩니다).
2. **[터미널]** `ls config` 로 `exclude_list.json` 이 `access_log.json` 과 같은 `config` 폴더에 있는지 보고, `python -m json.tool config/exclude_list.json`(맥북은 `python3`)로 내용이 정상인지 확인합니다.
   - 깨진 채 두면 제외 리스트를 읽지 못해 아무것도 제외되지 않습니다.
3. **[VS Code]** `report_exclude.py` 에서 직접 쓰는 곳 네 군데(`exclude_key` · `load_exclude_map` · `can_exclude` · `split_by_exclude`)를 씁니다. 2.1 의 표와 그림을 보고 씁니다.
4. **[터미널]** `pwd` 의 결과가 `access_control` 로 끝나는지 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python day04_6-1_run.py
   ```
5. 출력은 세 단계입니다. 단계 1은 분류 건수 한 줄, 단계 2는 회수 제외한 후보와 이유, 단계 3은 제외 리스트에 있지만 회수 대상으로 남은 후보입니다.
6. **[보고서]** `day04_pm_report.md` 의 `## Exercise 7-2` › `### Exercise Exercise 1-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 회수 대상과 회수 제외가 각각 몇 건인지, 회수 제외된 후보와 제외한 이유를 적어 주세요.
   - (나) [핵심 질문] 단계 3 출력을 보면 다미의 `SALES:QUERY` 는 제외 리스트에 있는데 회수 대상으로 남았습니다. 왜 제외하지 않게 만들었을까요? 제외했다면 어떤 위험이 있을지도 적어 주세요.
   - (다) [핵심 질문] 제외 리스트에는 제외하는 기간을 적는 키가 없습니다. 한 번 적은 권한을 아무도 다시 확인하지 않으면 어떤 문제가 생길까요? 리스트에 권한을 추가할 때 누가 확인하면 좋을까요?

## Exercise 7-2 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 「사용자:권한」 문자열 만들기 | `return f"{user}:{permission}"` (`exclude_key` 안) |
| 제외 이유 딕셔너리에 담기 | `exclude_map[item_key] = item["reason"]` (`load_exclude_map` 안) |
| 제외 리스트에 있는지 | `in_exclude_list = key in exclude_map` (`can_exclude` 안) |
| 이유에 퇴사가 있는지 | `is_resigned = "퇴사한 계정" in finding["reasons"]` (`can_exclude` 안) |
| 제외해도 되는지 | `return in_exclude_list and not is_resigned` (`can_exclude` 안) |
| 제외된 후보 만들기 | `reason = exclude_map[key]` → `excluded_entry = make_excluded(finding, reason)` → `excluded.append(excluded_entry)` (`split_by_exclude` 안) |
| 둘로 나눠 리턴 | `return to_revoke, excluded` |

---

## 마무리 · 오늘 만든 것을 깃허브에 올리기

문제가 아니라 오늘 한 일을 저장소에 올리는 마무리입니다. Exercise 7-2 마지막 10분에 합니다.

** 이런 상황이 있습니다**

- **지금은**: 팀장이 「오늘 만든 접근 점검 코드와 리포트를 저장소에 남겨 달라」고 합니다.
- **그래서 하는 것**: 올라갈 파일을 `git status` 로 먼저 확인하고(비밀 키 파일 `.env` 가 섞이면 안 됩니다), `git add` → `git commit` → `git push` 로 올립니다.
- **끝나면**: 깃허브 저장소의 `access_control` 폴더에서 오늘 만든 파일이 모두 보입니다.

**순서**

1. **[터미널]** `security-agent-toolkit` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/security-agent-toolkit` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
     - 새로 연 뒤 `pwd` 를 한 번 더 쳐서 확인합니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - `.venv` 도 같은 방법으로 합니다.
   - 10/23(금)에 올린 뒤 만든 오늘 파일이 `access_control/review_list.py` 처럼 한 줄씩 보입니다.
     - 지난번에 올리지 않았다면 `access_control/` 한 줄로 보일 수 있습니다.
     - 어느 쪽이든 `Untracked files:` 아래에 보이는 줄을 센 그대로 적습니다.
   - `access_control/config/exclude_list.json` 은 Exercise 7-2에 만든 회수 제외 리스트입니다. 이것도 올라갑니다.
   - `Untracked files:` 는 「아직 깃이 모르는 새 파일」 목록입니다.
   - `access_control/__pycache__/` (파이썬이 실행하면서 자동으로 만드는 임시 폴더)가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - 줄 수는 그 뒤에 다시 셉니다.
3. **[보고서]** `### 마무리 · 오늘 만든 것을 깃허브에 올리기` 아래를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다.
   - (가) `git status` 를 쳤을 때 `Untracked files:` 아래에 줄이 몇 개 보였는지, 그중에 `.env` 나 `.venv` 가 있었는지 적어 주세요.
   - 앞 Exercise에서 못 적은 보고서 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다. 올린 뒤에 이어서 적어 다시 올려도 됩니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add access control day 4 access review and overprivilege report"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다. `git pull` 을 입력해 받아 온 뒤 `git push` 를 다시 합니다
   - `git pull` 뒤에 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다
5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `access_control` 폴더를 열고, VS Code 왼쪽 목록의 `access_control` 폴더에 있는 파일들이 깃허브에도 보이는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.
   - 빠진 이름이 있으면 VS Code 왼쪽 목록의 `access_control` 폴더에 내 PC 에도 있는지 봅니다.
     - 없으면 다른 폴더에 만든 것이니 `access_control` 안으로 옮기고 1 ~ 4번을 다시 합니다.

## 마무리 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 올릴 파일 확인 | `git status` (`.env` · `.venv` 가 보이면 멈춤) |
| 올리기 | `git add .` → `git commit -m "…"` → `git push` |
| 올린 뒤 | 브라우저에서 파일이 모두 있는지 확인 |

---

## 오늘 마무리

| 확인 | 문제 |
|---|---|
| 현황과 규칙 · 안 쓴 결과를 합쳐 이유가 붙은 후보 리포트를 만들었다 | 오후 Exercise 7-1 |
| 후보를 「회수 대상」과 「회수 제외」로 나눴다 | 오후 Exercise 7-2 |
| 오늘 만든 파일과 보고서를 깃허브에 올렸다 | 마무리 |

내일(10/30(금))은 오늘 찾은 후보를 실제로 **회수**하는 일을 하고, 회수한 이력을 남깁니다. 오후에는 판정 함수를 서버로 여는 수업이 이어집니다. 오늘 만든 후보 리포트와 회수 제외 리스트로 내일 회수할 대상을 정합니다.

---

<!-- learn:answers -->
