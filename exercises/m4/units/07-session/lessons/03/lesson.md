---
id: m4-u07-l03
title: Exercise 7-2 · 위험 점수를 매겨 등급과 이유 저장하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/108_day04_pm_correlation_risk.md
  mission_id: GichanSource.m4-1105-pm-correlation-risk
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 7-2 · 위험 점수를 매겨 등급과 이유 저장하기

## 개요

> **이번 Exercise에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「Unit 6과 Exercise 7-1에서 탐지된 규칙이 여러 개인데, 결과가 모두 `탐지됨` 이라고만 나와서 어느 대상부터 확인할지 정할 수 없습니다. 퇴사한 계정이 계속 시도한 것과 파일을 한 번 더 내려받은 것이 같은 무게일 수는 없습니다.
>
> 탐지된 규칙마다 점수를 정하고 대상(사용자 또는 IP)마다 더해서 high · mid · low 로 나눠 주세요. 담당자가 왜 그 등급인지 알 수 있게, 탐지된 규칙 이름도 같이 파일에 적어 주세요.」
> - **왜 중요한가**: <mark>점수만 있고 이유가 없으면 담당자가 근거를 확인하기 어려워서, 탐지된 규칙 이름을 이유로 함께 저장합니다.</mark>

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「문제」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다. (판다스 문법 상자의 코드는 눈으로 읽으면 됩니다.)

## 읽기 · 왜 필요한가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 규칙마다 **점수**를 주고, 대상(사용자 또는 IP)마다 탐지된 규칙의 점수를 **더합니다**. <mark>같은 규칙이 한 대상의 여러 이벤트에서 탐지되어도 그 규칙의 점수는 대상마다 한 번만 더합니다.</mark>
2. 합계를 high · mid · low 로 나누고, <mark>탐지된 규칙 이름을 함께 저장하면 담당자가 점수가 나온 근거를 확인할 수 있습니다.</mark>

## 읽기 · 2.1 규칙마다 점수와 등급 기준

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문은 없습니다. 판다스 문법 상자의 코드는 눈으로 읽으면 됩니다.

| 탐지된 규칙 | 점수 | 어느 단계에서 탐지되나 |
|---|---|---|
| 퇴사한 계정 | 60 | Exercise 6-1: 서버가 거절한 요청을 `check_permission` 으로 다시 판정했을 때 나온 이유 단어 |
| 권한 없음 | 20 | Exercise 6-1 |
| 규칙은 허용인데 서버가 거절 | 10 | Exercise 6-1 |
| 업무 시간 밖 로그인 | 15 | Exercise 6-2 |
| 평소와 다른 IP | 20 | Exercise 6-2 |
| 대량 다운로드 | 25 | Exercise 6-2 |
| 경로 스캔 | 30 | Exercise 6-3: 대상이 사용자가 아니라 IP |
| 여러 로그 연결 | 30 | Exercise 7-1 |

- 등급 기준은 점수가 **60 이상이면 high, 35 이상 60 미만이면 mid, 35 미만이면 low** 입니다. 「이상」은 `>=` 이고, <mark>높은 기준(high)부터 먼저 검사합니다.</mark> 등급은 위험이 없다는 판정이 아니라 **확인할 순서를 정하는 기준**입니다.
- 표의 「규칙」은 **탐지 규칙의 이름**입니다. 서버 거절은 판정 이유 단어(`퇴사한 계정` · `권한 없음` · `허용`)를 그대로 이름으로 쓰고, `허용` 은 「규칙은 허용인데 서버가 거절」이라는 이름으로 바꿔 씁니다.
- 대상은 사용자(`seoyeon` · `dami` …)와 IP(경로 스캔)입니다. 코드의 `entity`(엔티티, 점수를 매길 대상)가 이 대상입니다. 이 숫자들은 <mark>이번 Exercise에서 정해 고정한 값</mark>이고, 현업에서는 조직이 정합니다.
- 출력 맨 아래의 `dtype: int64` 는 값이 정수라는 표시이고 읽지 않아도 됩니다(Unit 3과 Unit 5에서 본 줄과 같습니다).

**판다스 문법 상자 — 그룹마다 합계 `sum`**

**<mark>`그룹["열"].sum()`</mark> 은 `groupby` 로 만든 그룹마다 그 열의 숫자를 모두 더합니다**

Unit 6에서 같은 값끼리 묶는 `groupby` 를 썼습니다. 아래는 탐지된 규칙마다 점수를 적은 표이고, 대상(`entity`)마다 점수를 더합니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                       # 표에 넣을 내용(열 이름: 값들)
    "entity": ["seoyeon", "seoyeon", "dami"],  # entity 열
    "points": [20, 25, 60],                    # points 열
}
df = pd.DataFrame(data)                        # 내용으로 표(DataFrame)를 만든다
print(df)                                      # 표를 출력한다
```

실행 결과:

```
    entity  points
0  seoyeon      20
1  seoyeon      25
2     dami      60
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
grouped = df.groupby("entity")    # entity 가 같은 행끼리 그룹으로 묶는다
totals = grouped["points"].sum()  # 그룹에서 points 열을 골라 바로 합계를 구한다
print(totals)                     # 대상별 점수 합계를 출력한다
```

실행 결과:

```
entity
dami       60
seoyeon    45
Name: points, dtype: int64
```

- 읽는 법: <mark style="background:#bde3ff">`seoyeon` 은 20 과 25 를 더한 45, `dami` 는 60</mark> 입니다. 문제에서는 딕셔너리 리스트로 표를 만드는 `pd.DataFrame(리스트)` 줄이 미리 채워져 있습니다.
- <mark>`groupby` 결과는 이름순(dami → seoyeon)으로 나옵니다.</mark> 문제에서는 미리 채운 줄이 점수가 높은 순으로 다시 정렬합니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `collect_findings` | 이벤트 표 · 연결된 사건 | 탐지된 규칙 리스트(미리 채움) |
| `score_findings` | 탐지된 규칙 리스트 | 대상별 점수(높은 순) |
| `make_grade` | 점수 | `"high"` · `"mid"` · `"low"` |
| `collect_reasons` · `save_records` | 탐지된 규칙 · 기록 리스트 | 대상별 규칙 이름 · 저장한 건수(미리 채움) |
| `make_records` | 대상별 점수 · 이유 | 점수 · 등급 · 이유 기록 리스트 |

- `make_records` 의 `totals.items()` 는 점수 집계 결과(시리즈)에서 「대상, 점수」를 한 쌍씩 꺼냅니다. 딕셔너리의 `.items()` 와 같은 모양입니다.
- **직접 쓰는 곳은 다섯 군데**(번호 1 ~ 5)이고, 함수 세 개 안에 나뉘어 있습니다.
  - `score_findings`(1 · 2번): 규칙마다 점수를 `map` 으로 채우고 대상마다 `sum` 으로 더합니다.
  - `make_grade`(3 · 4번): 점수가 high 기준 이상이면 `"high"` 를 리턴합니다. mid 와 low 는 같은 모양이라 미리 채웠습니다.
  - `make_records`(5번): 대상 · 점수 · 등급 · 이유를 딕셔너리로 만듭니다.

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise 7-2 · 탐지된 규칙에 점수를 매겨 등급과 이유를 unit05_risk_scores.json 에 저장하기

**이런 상황이 있습니다**

- **지금은**: <mark>Unit 6과 Exercise 7-1에서 탐지된 규칙이 8건 있지만 대상별 우선순위가 정해져 있지 않습니다</mark>.
- **그래서 만드는 것**: `risk_scores.py` 입니다.
  - 규칙마다 점수를 채우고 대상마다 더합니다.
  - 점수로 high · mid · low 등급을 정합니다.
  - 대상 · 점수 · 등급 · 이유를 `unit05_risk_scores.json` 한 파일에 저장합니다.
- **실행하면**: <mark>단계 1: 탐지된 규칙 수, 단계 2: 대상별 점수, 단계 3: 저장한 건수, 단계 4: 저장된 기록이 한 건씩 나옵니다.</mark>
- **현업에서는**: 점수와 이유를 함께 남기면 등급이 올라간 근거를 설명할 수 있습니다. 조직은 필요에 따라 점수 기준을 바꿀 수 있고, 바꾼 날짜와 이유를 기록합니다.

**할 일**

1. `risk_scores.py` · `exercise7-2_run.py` 두 파일을 만들고, `risk_scores.py` 의 세 함수에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>탐지된 규칙 수</mark>(단계 1), <mark>대상별 점수</mark>(단계 2), <mark>저장한 건수</mark>(단계 3), <mark>저장된 기록</mark>(단계 4)를 읽고, 새로 생긴 `unit05_risk_scores.json` 을 VS Code 에서 열어 봅니다.

`collect_findings` 는 읽기만 하는 미리 채운 함수입니다. Unit 6의 탐지 결과를 (대상, 규칙) 쌍으로 모으는 일이라 직접 쓰는 곳이 없습니다.

**`risk_scores.py`**

```python
import json                                        # 점수를 JSON 파일로 쓰기 위해 json 을 불러온다
import pandas as pd                                    # 판다스를 pd 라는 짧은 이름으로 불러온다
from access_detection import load_events, pick_server_failures, pick_suspicious, judge_failure, EVENTS_PATH  # Exercise 6-1 함수를 불러온다
from saas_detection import pick_saas, pick_logins, find_off_hours_logins, find_new_ip_users, find_bulk_download_users  # Exercise 6-2 함수를 불러온다
from malicious_detection import pick_web_failures, find_scan_ips  # Exercise 6-3 함수를 불러온다

RISK_PATH = "unit05_risk_scores.json"                   # 점수를 저장할 파일 이름
HIGH_LIMIT = 60                                        # 점수가 이 값 이상이면 high
MID_LIMIT = 35                                         # 점수가 이 값 이상이면 mid, 그보다 낮으면 low
WEIGHTS = {"퇴사한 계정": 60, "권한 없음": 20, "규칙은 허용인데 서버가 거절": 10,
           "업무 시간 밖 로그인": 15, "평소와 다른 IP": 20, "대량 다운로드": 25,
           "경로 스캔": 30, "여러 로그 연결": 30}      # 탐지된 규칙마다 점수
SERVER_RULES = {"퇴사한 계정": "퇴사한 계정", "권한 없음": "권한 없음", "허용": "규칙은 허용인데 서버가 거절"}  # 서버 판정 이유를 규칙 이름으로 바꾼다


def add_finding(findings, entity, rule):               # 리스트 · 대상 · 규칙 이름을 받는 함수
    """대상과 탐지된 규칙을 한 건 추가하되 같은 건은 한 번만 추가한다.
    같은 규칙이 여러 이벤트에 해당해도 점수가 중복되지 않게 할 때 쓴다.
    """
    finding = {"entity": entity, "rule": rule}         # 대상과 규칙을 딕셔너리로 만든다
    if finding not in findings:                        # 아직 없는 건이면
        findings.append(finding)                       # 리스트에 추가한다


def collect_findings(events, chains):                  # 이벤트 표와 연결된 사건을 받는 함수
    """Unit 6의 탐지 3개와 Exercise 7-1 연결 결과를 (대상, 탐지된 규칙) 리스트로 모은다.
    점수를 매기기 전에 한 번에 쓴다.
    """
    findings = []                                      # 탐지된 규칙을 담을 빈 리스트

    server_failures = pick_server_failures(events)     # 판정 서버 실패 이벤트를 고른다
    suspicious = pick_suspicious(server_failures)      # 먼저 확인할 서버 이벤트를 고른다
    suspicious_list = suspicious.to_dict("records")    # 표를 이벤트 딕셔너리 리스트로 바꾼다
    for event in suspicious_list:                      # 이벤트를 하나씩 꺼낸다
        reason, priority = judge_failure(event["user"], event["action"])  # 3과목 규칙으로 다시 판정한다
        rule = SERVER_RULES.get(reason, reason)        # 판정 이유를 규칙 이름으로 바꾼다
        add_finding(findings, event["user"], rule)     # 사용자와 규칙을 추가한다

    saas = pick_saas(events)                           # SaaS 이벤트를 고른다
    logins = pick_logins(saas)                         # 로그인 이벤트를 고른다
    off_hours_logins = find_off_hours_logins(logins)   # 업무 시간 밖 로그인을 찾는다
    off_hours_users = list(off_hours_logins["user"])   # 그 로그인의 사용자 이름만 리스트로 만든다
    new_ip_users = find_new_ip_users(logins)           # 평소와 다른 IP 로 로그인한 사용자를 찾는다
    bulk_users = find_bulk_download_users(saas)        # 대량 다운로드 사용자를 찾는다
    for user in off_hours_users:                       # 업무 시간 밖 로그인 사용자를 하나씩 꺼낸다
        add_finding(findings, user, "업무 시간 밖 로그인")  # 사용자와 규칙을 추가한다
    for user in new_ip_users:                          # 평소와 다른 IP 사용자를 하나씩 꺼낸다
        add_finding(findings, user, "평소와 다른 IP")  # 사용자와 규칙을 추가한다
    for user in bulk_users:                            # 대량 다운로드 사용자를 하나씩 꺼낸다
        add_finding(findings, user, "대량 다운로드")   # 사용자와 규칙을 추가한다

    web_failures = pick_web_failures(events)           # 웹 실패 이벤트를 고른다
    scan_ips, many_kinds = find_scan_ips(web_failures)  # 경로 스캔 IP 를 찾는다
    for ip in scan_ips:                                # 스캔 IP 를 하나씩 꺼낸다
        add_finding(findings, ip, "경로 스캔")         # IP 와 규칙을 추가한다

    for chain in chains:                               # 연결된 사건을 하나씩 꺼낸다
        add_finding(findings, chain["user"], "여러 로그 연결")  # 사용자와 규칙을 추가한다
    return findings                                    # 탐지된 규칙 리스트를 리턴한다


def score_findings(findings):                          # 탐지된 규칙 리스트를 받는 함수
    """대상마다 탐지된 규칙의 점수를 더해 점수가 높은 순으로 정렬한다.
    어느 대상부터 볼지 순서를 정할 때 쓴다.
    """
    findings_table = pd.DataFrame(findings)            # 딕셔너리 리스트를 표로 만든다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. findings_table 의 "rule" 열을 꺼내 .map(WEIGHTS) 를 붙여 규칙마다 점수를 구해 points 에 담는다
    findings_table["points"] = points                  # 표에 points 열을 붙인다 — 미리 채운 줄
    grouped = findings_table.groupby("entity")         # entity 가 같은 행끼리 그룹으로 만든다
    # 2. grouped 에서 "points" 열을 골라 .sum() 을 붙여 그룹마다 점수 합계를 구해 totals 에 담는다
    totals = totals.sort_values(ascending=False)       # 점수가 높은 순으로 정렬한다 — 미리 채운 줄
    return totals                                      # 대상별 점수를 리턴한다


def make_grade(score):                                 # 점수를 받는 함수
    """점수로 high · mid · low 등급을 정한다.
    점수가 높은 대상부터 먼저 보게 할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 3. if 로 시작한다: score 가 HIGH_LIMIT 이상이면
    # 4.   그 if 안쪽에서 "high" 를 리턴한다
    if score >= MID_LIMIT:                             # 점수가 mid 기준 이상이면 — 미리 채운 줄 (위 high 와 같은 모양)
        return "mid"                                   # mid 이다 — 미리 채운 줄
    return "low"                                       # 둘 다 아니면 low 이다


def collect_reasons(findings):                         # 탐지된 규칙 리스트를 받는 함수
    """대상마다 탐지된 규칙 이름을 모아 딕셔너리로 만든다.
    왜 그 등급인지 이유를 함께 저장할 때 쓴다.
    """
    reasons = {}                                       # 대상 → 규칙 이름 리스트 딕셔너리
    for finding in findings:                           # 탐지된 규칙을 하나씩 꺼낸다
        entity = finding["entity"]                     # 그 건의 대상
        if entity not in reasons:                      # 처음 나온 대상이면
            reasons[entity] = []                       # 빈 리스트를 만든다
        reasons[entity].append(finding["rule"])        # 그 대상의 규칙 이름을 추가한다
    return reasons                                     # 대상별 규칙 이름을 리턴한다


def make_records(totals, reasons):                     # 대상별 점수와 이유를 받는 함수
    """대상마다 점수 · 등급 · 이유를 담은 딕셔너리 리스트를 만든다.
    담당자가 읽을 파일의 내용을 만들 때 쓴다.
    """
    records = []                                       # 기록을 담을 빈 리스트
    for entity, score in totals.items():               # 대상과 점수를 한 쌍씩 꺼낸다
        grade = make_grade(score)                      # 점수로 등급을 정한다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. 키 "entity" 에 entity, "score" 에 int(score), "grade" 에 grade, "reasons" 에 reasons[entity] 를 담은 딕셔너리를 record 에 담는다 (int 는 JSON 저장용)
        records.append(record)                         # 기록을 리스트에 추가한다
    return records                                     # 기록 리스트를 리턴한다


def save_records(records, path):                       # 기록 리스트와 파일 경로를 받는 함수
    """기록 리스트를 JSON 파일로 저장하고 저장한 건수를 리턴한다.
    담당자와 다른 프로그램이 같은 파일을 읽게 할 때 쓴다.
    """
    with open(path, "w", encoding="utf-8") as file:    # path 파일을 쓰기 모드로 연다
        json.dump(records, file, ensure_ascii=False, indent=2)  # 한글은 그대로, 줄을 나눠 저장한다
    saved_count = len(records)                         # 저장한 기록이 몇 건인지 센다
    return saved_count                                 # 저장한 건수를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 · 2번은 함수 안이라 앞에 공백 4개이고, 3 · 4번도 함수 안이라 `if` 는 4개, `return` 은 8개이며, 5번은 `for` 안이라 8개입니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.**
- 5번의 `int(score)` 는 <mark>JSON 으로 저장하려고 판다스의 숫자를 파이썬 정수로 바꾸는 것</mark>입니다. 빼면 저장할 때 `TypeError: Object of type int64 is not JSON serializable` 오류가 납니다.
- `collect_findings` 는 읽기만 하는 미리 채운 함수입니다. `SERVER_RULES.get(reason, reason)` 은 딕셔너리에서 reason 을 찾고, 없으면 reason 을 그대로 쓴다는 뜻입니다.
- 채우기 전에 실행하면 `NameError: name 'points' is not defined` 오류가 납니다. 1번을 아직 안 썼기 때문입니다.

**`exercise7-2_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. `len(리스트)` 는 리스트의 개수입니다.

```python
from access_detection import load_events, EVENTS_PATH  # Exercise 6-1 함수를 불러온다
from correlation import find_chains_in_events          # Exercise 7-1 함수를 불러온다
from risk_scores import collect_findings, score_findings, collect_reasons, make_records, save_records, RISK_PATH  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)                      # 이벤트 파일을 표로 읽는다
chains = find_chains_in_events(events)                 # Exercise 7-1에서 만든 연결된 사건을 찾는다
findings = collect_findings(events, chains)            # Unit 6의 탐지와 연결 결과에서 탐지된 규칙을 모은다
finding_count = len(findings)                          # 탐지된 규칙이 모두 몇 건인지 센다
print("--- 단계 1: 탐지된 규칙", finding_count, "건")    # 단계 1 시작을 알리는 줄과 건수

totals = score_findings(findings)                      # 대상마다 점수를 더한다
print("--- 단계 2: 대상별 점수")                       # 단계 2 시작을 알리는 줄
print(totals)                                          # 점수가 높은 순으로 출력한다

reasons = collect_reasons(findings)                    # 대상마다 탐지된 규칙 이름을 모은다
records = make_records(totals, reasons)                # 점수 · 등급 · 이유를 담은 기록을 만든다
saved_count = save_records(records, RISK_PATH)         # 기록을 파일에 저장한다
print("--- 단계 3:", RISK_PATH, "에", saved_count, "건 저장")  # 단계 3 시작을 알리는 줄과 건수

print("--- 단계 4: 등급 · 대상 · 점수 · 이유")         # 단계 4 시작을 알리는 줄
for record in records:                                 # 기록을 하나씩 꺼낸다
    print(record["grade"], record["entity"], record["score"], record["reasons"])  # 등급 · 대상 · 점수 · 이유를 출력한다
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `risk_scores.py` · `exercise7-2_run.py` 를 `anomaly_detection` 폴더에 만들어 위 코드를 붙여 넣습니다. 터미널에서는 `touch risk_scores.py exercise7-2_run.py` 로 만든 뒤 VS Code 에서 엽니다.
2. **[VS Code]** `risk_scores.py` 에서 <mark>직접 쓰는 곳 다섯 군데를 씁니다</mark>. 2.1 의 표와 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise7-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise7-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1과 단계 3은 숫자가 제목 줄에 함께 나오고, 단계 2는 제목 아래 7줄(맨 위 `entity`, 대상 5줄, 맨 아래 `Name: points, dtype: int64`), 단계 4는 5줄입니다.
5. **[VS Code]** 새로 생긴 `unit05_risk_scores.json` 을 열어 <mark>대상 5개가 점수 순으로 들어 있는지</mark> 확인합니다.
6. **[보고서]** Unit 7 의 `## Exercise 7-2` › `### Exercise 7-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, high · mid · low 에 각각 어떤 대상이 들어갔는지 적어 주세요.
   - (나) [핵심 질문] seoyeon 의 점수가 어떤 규칙의 점수를 더해 나왔는지 적고, 점수만 저장하지 않고 이유(`reasons`)를 함께 저장하는 까닭을 적어 주세요.
   - (다) [핵심 질문] 198.51.100.90 은 경로 스캔 하나에 해당하지만 low 입니다. low 는 점수 기준상 낮은 등급이라는 뜻입니다. low 인 이유를 점수와 기준으로 설명하고, 이 IP 의 기록을 무시해도 되는지 샘플의 값(그 IP 의 요청 3개의 `result`)으로 판단해 적어 주세요.

## Exercise 7-2 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 규칙마다 점수 채우기 | `points = findings_table["rule"].map(WEIGHTS)` |
| 대상마다 점수 더하기 | `totals = grouped["points"].sum()` |
| 등급 정하기 | `if score >= HIGH_LIMIT:` → `return "high"` |
| 기록 만들기 | `record = {"entity": entity, "score": int(score), …}` |

---

## 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기

<mark>문제가 아니라 이번 Unit에서 한 일을 저장소에 올리는 마무리입니다.</mark> Exercise 7-2 마지막 약 10분에 합니다. 어느 터미널을 써도 되고, `pwd` 로 위치를 먼저 확인한 뒤 결과가 `anomaly_detection` 으로 끝나면 아래 1번의 `cd ..` 를 칩니다.

**이런 상황이 있습니다**

- **지금은**: <mark>팀장이 「이번 Unit에서 만든 탐지 코드와 점수 파일을 저장소에 남겨 달라」고 합니다</mark>.
- **그래서 하는 것**: `git status` 로 올라갈 파일을 확인한 뒤(`.env` 같은 비밀 키 파일이 섞이면 안 됩니다) `git add` → `git commit` → `git push` 순서로 올립니다.
- **끝나면**: 깃허브 저장소의 `anomaly_detection` 폴더에 Unit 6과 Unit 7에서 만든 파일이 보입니다.

**순서**

0. **[터미널]** 이번 Unit에서 만든 파일이 있는지 `anomaly_detection` 폴더에서 확인합니다. Unit 7 의 Exercise 7-1 · 7-2 칸에서 `답:` 뒤와 코드 상자가 비어 있는 질문이 없는지도 봅니다(마무리 (가)는 3번에서 채웁니다).
   ```bash
   pwd
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
   - <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나야 합니다.</mark> Unit 6 파일(`access_detection.py` · `saas_detection.py` · `malicious_detection.py` · `advanced_detection.py`)과 Unit 7 파일(`correlation.py` · `risk_scores.py` · `exercise7-1_run.py` · `exercise7-2_run.py` · `unit05_risk_scores.json`)이 보이면 됩니다. `advanced_detection.py` 는 Exercise 6-3에서 만든 파일입니다.
1. **[터미널]** `security-agent-toolkit` 폴더로 옮기고 위치를 확인합니다. 0번의 `pwd` 결과가 `anomaly_detection` 으로 끝날 때만 `cd ..` 를 칩니다. 이미 `…/security-agent-toolkit` 으로 끝나면 `cd ..` 는 건너뛰고 `pwd` 만 칩니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 있는 폴더의 위치 확인
   - <mark>결과가 다르면</mark> VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark>빨간 글씨 줄에 `.env` 나 `.venv` 가 보이면 올리지 말고,</mark> 아래 안내대로 `.gitignore` 를 고친 뒤 `git status` 를 다시 봅니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `anomaly_detection/__pycache__/` (파이썬이 실행하면서 자동으로 만드는 임시 폴더)가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 봅니다.
3. **[보고서]** `### 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기` 아래를 채웁니다. <mark>올리기 전에 채워야</mark> 깃허브에 빈칸 없이 올라갑니다.
   - (가) `git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.
   - <mark>앞 Exercise에서 못 적은 보고서 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.</mark> 올린 뒤에 이어서 적어 다시 올려도 됩니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add anomaly detection day 4 detections, correlation and risk scores"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 대상에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - <mark>`git push` 가 거절(`rejected`)되면 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다.</mark> `git pull` 을 입력해 받아 온 뒤 `git push` 를 다시 합니다
   - `git pull` 뒤에 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다
5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `anomaly_detection` 폴더를 열고, VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 있는 파일들이 깃허브에도 보이는지 확인합니다. <mark>`__pycache__` 폴더는 없어도 됩니다</mark>.
   - 빠진 이름이 있으면 VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 내 PC 에도 있는지 봅니다.
     - 없으면 다른 폴더에 만든 것이니 `anomaly_detection` 안으로 옮기고, `pwd` 로 위치를 확인한 뒤 2번의 `git status` 부터 다시 합니다.

## 마무리 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 올릴 파일 확인 | `git status` (`.env` · `.venv` 가 보이면 멈춤) |
| 올리기 | `git add .` → `git commit -m "…"` → `git push` |
| 올린 뒤 | 브라우저에서 `anomaly_detection` 폴더와 파일이 있는지 확인 |

---

## 이번 Unit 마무리

| 확인 | 문제 |
|---|---|
| 세 로그를 한 사용자 기준으로 연결해 60분 안에 모인 사건을 찾았다 | Exercise 7-1 |
| 탐지된 규칙에 점수를 매겨 등급과 이유를 `unit05_risk_scores.json` 에 저장했다 | Exercise 7-2 |
| 이번 Unit에서 만든 파일과 보고서를 깃허브에 올렸다 | 마무리 |

다음은 Unit 8입니다. <mark>이번 Unit에서 만든 탐지가 맞았는지를 직접 세어 봅니다.</mark> 알림이 났는데 문제가 아니었던 것(오탐)과 알림이 나야 하는데 안 난 것(미탐)을 찾습니다.

---

<!-- learn:answers -->
