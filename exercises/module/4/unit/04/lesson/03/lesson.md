---
id: m4-u04-l03
title: 실습 4-1 · 위험 점수와 등급·이유 저장하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/108_day04_pm_correlation_risk.md
  mission_id: GichanSource.m4-1105-pm-correlation-risk
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 4-1 · 위험 점수와 등급·이유 저장하기

## 목표: 점수·등급·이유 파일

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「서버 · SaaS · 웹 로그의 탐지와 로그 연결에서 탐지된 규칙이 여러 개인데, 결과가 모두 `탐지됨` 이라고만 나와서 어느 대상부터 확인할지 정할 수 없습니다. 퇴사한 계정이 계속 시도한 것과 파일을 한 번 더 내려받은 것이 같은 무게일 수는 없습니다.
>
> 탐지된 규칙마다 점수를 정하고 대상(사용자 또는 IP)마다 더해서 high · mid · low 로 나눠 주세요. 담당자가 왜 그 등급인지 알 수 있게, 탐지된 규칙 이름도 같이 파일에 적어 주세요.」
> - **왜 중요한가**: <mark>점수만 있고 이유가 없으면 담당자가 근거를 확인하기 어려워서, 탐지된 규칙 이름을 이유로 함께 저장합니다.</mark>
> - **직접 쓰는 것**: 대부분은 미리 채워 두었고, 점수를 매기고 더하는 두 줄(① · ②)만 직접 씁니다.
> - **끝나면 쓰는 것**: 자기 점검 질문 (가) · (나) 답. (다)는 여유가 되면 하는 응용입니다.

## 왜 점수를 더하고 이유를 남기는가

1. 규칙마다 **점수**를 주고, 대상(사용자 또는 IP)마다 탐지된 규칙의 점수를 **더합니다**. <mark>같은 규칙이 한 대상의 여러 이벤트에서 탐지되어도 그 규칙의 점수는 대상마다 한 번만 더합니다.</mark>
2. 합계를 high · mid · low 로 나누고, <mark>탐지된 규칙 이름을 함께 저장하면 담당자가 점수가 나온 근거를 확인할 수 있습니다.</mark>

## 1.1 규칙마다 점수와 등급 기준

| 탐지된 규칙 | 점수 | 찾는 파일 |
|---|---|---|
| 퇴사한 계정 | 60 | `access_detection.py`(Module 3 Unit 3 실습 3-2) |
| 권한 없음 | 20 | `access_detection.py` |
| 규칙은 허용인데 서버가 거절 | 10 | `access_detection.py` |
| 업무 시간 밖 로그인 | 15 | `risk_inputs.json`(고정 시나리오 입력) |
| 평소와 다른 IP | 20 | `risk_inputs.json`(고정 시나리오 입력) |
| 대량 다운로드 | 25 | `risk_inputs.json`(고정 시나리오 입력) |
| 경로 스캔 | 30 | `risk_inputs.json`(고정 시나리오 입력) |
| 여러 로그 연결 | 30 | `risk_inputs.json`(고정 시나리오 입력) |

- 등급 기준은 점수가 **60 이상이면 high, 35 이상 60 미만이면 mid, 35 미만이면 low** 입니다. 「이상」은 `>=` 이고, <mark>높은 기준(high)부터 먼저 검사합니다.</mark> 등급은 위험이 없다는 판정이 아니라 **확인할 순서를 정하는 기준**입니다.
- 표의 「규칙」은 **탐지 규칙의 이름**입니다. 서버 거절 세 줄은 서버가 거절한 요청을 `check_permission` 으로 다시 판정한 이유 단어(`퇴사한 계정` · `권한 없음` · `허용`)를 이름으로 씁니다. 다만 `허용` 만으로는 뜻이 헷갈려서 「규칙은 허용인데 서버가 거절」이라는 이름으로 바꿔 씁니다.
- 대상은 사용자(`seoyeon` · `dami` …)와 IP(경로 스캔)입니다. 코드의 `entity`(엔티티, 점수를 매길 대상)가 이 대상입니다. 이 숫자들은 <mark>이번 실습에서 정해 고정한 값</mark>이고, 현업에서는 조직이 정합니다.
- 출력 맨 아래의 `dtype: int64` 는 값이 정수라는 표시이고 읽지 않아도 됩니다.

<h2>판다스 문법 상자 — 규칙마다 점수 붙이기 <code>map</code> 과 그룹마다 합계 <code>sum</code></h2>

**<mark>`열.map(딕셔너리)`</mark> 는 열의 값을 딕셔너리에서 찾아 짝지어진 값으로 바꾸고, <mark>`그룹["열"].sum()`</mark> 은 `groupby` 로 만든 그룹마다 그 열의 숫자를 모두 더합니다**

아래는 대상(`entity`)마다 탐지된 규칙(`rule`)을 적은 표입니다. 먼저 규칙 이름을 딕셔너리에서 찾아 점수로 바꿉니다. 딕셔너리에 없는 값은 `NaN`(값이 없다는 표시)이 됩니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

weights = {"평소와 다른 IP": 20, "대량 다운로드": 25, "퇴사한 계정": 60}  # 규칙 → 점수 딕셔너리
data = {                                                     # 표에 넣을 내용(열 이름: 값들)
    "entity": ["seoyeon", "seoyeon", "dami"],                # entity 열
    "rule": ["평소와 다른 IP", "대량 다운로드", "퇴사한 계정"],  # rule 열
}
df = pd.DataFrame(data)                                      # 내용으로 표(DataFrame)를 만든다
df["points"] = df["rule"].map(weights)                       # rule 열의 값을 딕셔너리에서 찾아 점수로 바꿔 points 열로 붙인다
print(df)                                                    # 표를 출력한다
```

실행 결과:

```
    entity       rule  points
0  seoyeon  평소와 다른 IP      20
1  seoyeon    대량 다운로드      25
2     dami     퇴사한 계정      60
```

위 코드에 이어서 실행하는 다음 코드입니다. `groupby` 는 Unit 2 실습 2-2에서 쓴 「같은 값끼리 묶기」입니다.

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

- 읽는 법: 첫 출력에서 <mark style="background:#bde3ff">규칙 이름마다 점수(20 · 25 · 60)가 붙었고</mark>, 두 번째 출력에서 <mark style="background:#bde3ff">`seoyeon` 은 20 과 25 를 더한 45, `dami` 는 60</mark> 입니다.
- 문제에서는 딕셔너리 리스트로 표를 만드는 `pd.DataFrame(리스트)` 줄과 points 열을 붙이는 줄이 미리 채워져 있습니다. 리스트 안의 딕셔너리 하나가 표의 한 행이 되고, 딕셔너리의 키(`entity` · `rule`)가 열 이름이 됩니다. 직접 쓰는 것은 `map` 한 줄과 `sum` 한 줄입니다.
- <mark>`groupby` 결과는 이름순(dami → seoyeon)으로 나옵니다.</mark> 문제에서는 미리 채운 줄이 점수가 높은 순으로 다시 정렬합니다.

<h2>한 장 정리</h2>

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `collect_findings` | 이벤트 표 · 연결된 사건 | 탐지된 규칙 리스트(미리 채움) |
| `score_findings` | 탐지된 규칙 리스트 | 대상별 점수(높은 순) · **직접 쓰는 곳** |
| `make_grade` | 점수 | `"high"` · `"mid"` · `"low"`(미리 채움) |
| `collect_reasons` · `save_records` | 탐지된 규칙 · 기록 리스트 | 대상별 규칙 이름 · 저장한 건수(미리 채움) |
| `make_records` | 대상별 점수 · 이유 | 점수 · 등급 · 이유 기록 리스트(미리 채움) |

- `make_records` 의 `totals.items()` 는 점수 집계 결과(시리즈)에서 「대상, 점수」를 한 쌍씩 꺼냅니다. 딕셔너리의 `.items()` 와 같은 모양입니다.
- **직접 쓰는 곳은 두 곳**(① · ②)이고, 모두 `score_findings` 안에 있습니다. 위 문법 상자의 `map` 한 줄과 `sum` 한 줄입니다.

> **확인** — 문법 상자의 두 코드를 이어 실행했을 때 `seoyeon 45` 와 `dami 60` 이 나오면 성공입니다. 안 나오면 두 번째 코드를 첫 번째 코드 바로 아래에 이어 붙였는지 봅니다.
>
> 실행하는 법: `anomaly_detection` 폴더에 연습 파일 `try_box.py` 를 만들어 두 코드를 차례로 붙여 넣고 저장한 뒤, 터미널에서 `python try_box.py` 를 칩니다.

## 실습 4-1 · 위험 점수와 등급·이유 저장하기

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>세 로그의 탐지 결과와 로그 연결 결과에서 탐지된 규칙이 8건 있지만 대상별 우선순위가 정해져 있지 않습니다</mark>. 8건은 (대상, 규칙) 쌍의 수입니다. 위 점수표의 규칙도 8개이지만 표의 규칙이 모두 탐지된 것은 아닙니다(오늘 데이터에서는 「권한 없음」이 나오지 않아 서로 다른 규칙은 7개입니다).
- **그래서 만드는 것**: `risk_scores.py` 입니다.
  - 규칙마다 점수를 채우고 대상마다 더합니다.
  - 점수로 high · mid · low 등급을 정합니다.
  - 대상 · 점수 · 등급 · 이유를 `unit05_risk_scores.json` 한 파일에 저장합니다.
- **실행하면**: <mark>단계 1: 탐지된 규칙 수, 단계 2: 대상별 점수, 단계 3: 저장한 건수, 단계 4: 저장된 기록이 한 건씩 나옵니다.</mark>
- **현업에서는**: 점수와 이유를 함께 남기면 등급이 올라간 근거를 설명할 수 있습니다. 조직은 필요에 따라 점수 기준을 바꿀 수 있고, 바꾼 날짜와 이유를 기록합니다.

<h2>할 일</h2>

1. `risk_scores.py` · `exercise4-1_run.py` 두 파일을 만들고, `risk_scores.py` 의 `score_findings` 에서 `# ←` 가 있는 <mark>두 곳</mark>(① · ②)을 한 줄씩 채웁니다. 나머지 함수는 모두 미리 채워 두었습니다.
2. 실행해서 <mark>탐지된 규칙 수</mark>(단계 1), <mark>대상별 점수</mark>(단계 2), <mark>저장한 건수</mark>(단계 3), <mark>저장된 기록</mark>(단계 4)를 읽고, 새로 생긴 `unit05_risk_scores.json` 을 VS Code 에서 열어 봅니다.

`score_findings` 의 두 곳 말고는 모두 읽기만 하는 미리 채운 줄입니다. 가장 긴 `collect_findings` 는 Module 3 Unit 3 핵심 서버 탐지와 `risk_inputs.json` 의 고정 시나리오 입력을 (대상, 규칙) 쌍으로 모읍니다.

<h3><code>risk_scores.py</code></h3>

```python
import json                                        # 점수를 JSON 파일로 쓰기 위해 json 을 불러온다
import pandas as pd                                    # 판다스를 pd 라는 짧은 이름으로 불러온다
from access_detection import pick_server_failures, pick_suspicious, judge_failure  # Module 3 Unit 3 핵심 탐지 함수를 불러온다

RISK_INPUTS_PATH = "risk_inputs.json"  # 고정 시나리오 입력 파일

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


def collect_findings(events, risk_inputs_path=RISK_INPUTS_PATH):
    """핵심 서버 탐지와 고정 시나리오 입력을 (대상, 규칙) 목록으로 모은다."""
    findings = []
    server_failures = pick_server_failures(events)
    suspicious = pick_suspicious(server_failures)
    for event in suspicious.to_dict("records"):
        reason, priority = judge_failure(event["user"], event["action"])
        add_finding(findings, event["user"], SERVER_RULES.get(reason, reason))

    with open(risk_inputs_path, encoding="utf-8") as file:
        risk_inputs = json.load(file)
    for item in risk_inputs:
        add_finding(findings, item["entity"], item["rule"])
    return findings


def score_findings(findings):                          # 탐지된 규칙 리스트를 받는 함수
    """대상마다 탐지된 규칙의 점수를 더해 점수가 높은 순으로 정렬한다.
    어느 대상부터 볼지 순서를 정할 때 쓴다.
    """
    findings_table = pd.DataFrame(findings)            # 딕셔너리 리스트를 표로 만든다
    # ① findings_table 의 "rule" 열에 .map(WEIGHTS) 를 붙여 규칙마다 점수를 구해 points 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    findings_table["points"] = points                  # 표에 points 열을 붙인다
    grouped = findings_table.groupby("entity")         # entity 가 같은 행끼리 그룹으로 만든다
    # ② grouped 에서 "points" 열을 골라 .sum() 을 붙여 그룹마다 합계를 구해 totals 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    totals = totals.sort_values(ascending=False)       # 점수가 높은 순으로 정렬한다
    return totals                                      # 대상별 점수를 리턴한다


def make_grade(score):                                 # 점수를 받는 함수
    """점수로 high · mid · low 등급을 정한다.
    점수가 높은 대상부터 먼저 보게 할 때 쓴다.
    """
    if score >= HIGH_LIMIT:                            # 점수가 high 기준 이상이면
        return "high"                                  # high 이다
    if score >= MID_LIMIT:                             # 점수가 mid 기준 이상이면
        return "mid"                                   # mid 이다
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
        record = {"entity": entity, "score": int(score), "grade": grade, "reasons": reasons[entity]}  # 대상 · 점수 · 등급 · 이유를 딕셔너리로 만든다 (int 는 판다스 숫자를 파이썬 정수로 바꾼다)
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

- 주석 줄은 그대로 두고, **각 주석 바로 아래 줄**에 씁니다. ① · ② 모두 함수 안이라 앞에 공백 4칸입니다.

<h3>직접 쓰는 곳</h3>

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | 규칙마다 점수 `points` (`map`) | 4칸 |
| ② | 대상마다 합계 `totals` (`sum`) | 4칸 |

- 채우기 전 확인: 그대로 실행하면 단계 1 줄(`--- 단계 1: 탐지된 규칙 8 건`) 다음에 `NameError: name 'points' is not defined` 가 나옵니다. ① 을 아직 안 써서 나는 오류이니 정상입니다. 오류 끝에 `. Did you mean: 'print'?` 처럼 꼬리가 더 붙어도 같은 오류입니다.
- ① 확인: ① 만 쓰고 실행하면 `UnboundLocalError: cannot access local variable 'totals' …` 가 나옵니다. ② 를 아직 안 써서 나는 오류이니 정상입니다. 막히면: 문법 상자의 `df["rule"].map(weights)` 에서 `df` 를 `findings_table`, `weights` 를 `WEIGHTS` 로 바꿉니다.
- ② 확인: ② 까지 쓰고 실행하면 단계 2에 `dami 60` 부터 `198.51.100.90 30` 까지 다섯 줄이 나오면 성공입니다. 막히면: 문법 상자의 `grouped["points"].sum()` 과 같은 모양이고, 끝의 괄호 `()` 까지 씁니다.

<h2>미리 채운 줄 읽기</h2>

- `make_grade` 는 `return` 을 만나면 함수가 바로 끝납니다. 그래서 high 이면 아래의 mid 검사까지 가지 않습니다.
- `make_records` 의 `int(score)` 는 <mark>판다스의 숫자를 파이썬 정수로 바꾸는 것</mark>입니다. 이번 데이터에서는 빼도 오류가 나지 않지만, 판다스가 돌려준 숫자(`int64`)를 그대로 JSON 으로 저장하려고 하면 `TypeError: Object of type int64 is not JSON serializable` 가 날 수 있어서 미리 바꿔 둡니다.
- `collect_findings` 의 `SERVER_RULES.get(reason, reason)` 은 딕셔너리에서 reason 을 찾고, 없으면 reason 을 그대로 쓴다는 뜻입니다.
  - `표.to_dict("records")` 는 표의 행을 하나씩 딕셔너리로 바꿔 리스트로 줍니다. 그래서 `for` 로 한 행(이벤트)씩 꺼내 `event["user"]` 처럼 읽을 수 있습니다.
  - `scan_ips, many_kinds = find_scan_ips(…)` 는 함수가 리턴한 두 값(스캔 IP 리스트, IP 별 요청 횟수)을 나눠 받습니다. 두 번째 값은 이 함수에서 쓰지 않습니다.
  - `add_finding` 의 `if finding not in findings:` 는 같은 (대상, 규칙) 쌍이 이미 리스트에 있으면 다시 넣지 않습니다. 그래서 dami 의 서버 요청 4번이 모두 「퇴사한 계정」으로 판정되어도 점수는 60 한 번만 더해집니다.

<h3><code>exercise4-1_run.py</code></h3>

그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. `len(리스트)` 는 리스트의 개수입니다.

```python
from access_detection import load_events, EVENTS_PATH  # 실습 3-2 함수를 불러온다
from risk_scores import collect_findings, score_findings, collect_reasons, make_records, save_records, RISK_PATH  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)                      # 이벤트 파일을 표로 읽는다
findings = collect_findings(events)                    # 핵심 서버 탐지와 고정 시나리오 입력을 모은다
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

<h2>순서</h2>

1. **[VS Code]** `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 로 `risk_scores.py` 와 `exercise4-1_run.py` 를 만들어 위 코드를 각각 붙여 넣고 저장합니다.
2. **[VS Code]** `risk_scores.py` 의 <mark>`# ←` 두 곳(① · ②)을 채웁니다</mark>. 문법 상자의 `map` 줄과 `sum` 줄을 보고 씁니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 `risk_scores.py` 를 만들어 붙여 넣고, 빈칸 ① · ② 를 채워 저장했다
- [ ] `anomaly_detection` 폴더에 `exercise4-1_run.py` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다.
   ```bash
   pwd
   python exercise4-1_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise4-1_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1과 단계 3은 숫자가 제목 줄에 함께 나오고, 단계 2는 제목 아래 7줄(맨 위 `entity`, 대상 5줄, 맨 아래 `Name: points, dtype: int64`), 단계 4는 5줄입니다.

<!-- checklist -->
- [ ] `python exercise4-1_run.py` 를 실행해 단계 4가 `high dami 60 ['퇴사한 계정']` 으로 시작하는 다섯 줄로 나왔다
<!-- /checklist -->

5. **[VS Code]** 새로 생긴 `unit05_risk_scores.json` 을 열어 <mark>대상 5개가 점수 순으로 들어 있는지</mark> 확인합니다. 이 파일은 Module 4 Unit 5와 Module 5에서 다시 쓰니 지우거나 이름을 바꾸지 않습니다.

<!-- checklist -->
- [ ] 새로 생긴 `unit05_risk_scores.json` 을 VS Code 에서 열어 대상 5개를 확인했다
<!-- /checklist -->

6. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.
   - (가) [핵심 질문] 실행한 출력을 보고, high · mid · low 에 각각 어떤 대상이 들어갔는지 적어 주세요.
   - (나) [핵심 질문] seoyeon 의 점수가 어떤 규칙의 점수를 더해 나왔는지 적고, 점수만 저장하지 않고 이유(`reasons`)를 함께 저장하는 까닭을 적어 주세요.
   - (다) [응용] 198.51.100.90 은 경로 스캔 하나에 해당하지만 low 입니다. low 는 점수 기준상 낮은 등급이라는 뜻입니다. low 인 이유를 점수와 기준으로 설명하고, 이 IP 의 기록을 무시해도 되는지 샘플의 값(그 IP 의 요청 3개의 `result`)으로 판단해 적어 주세요.
     - 요청 3개는 VS Code 로 `normalized_events.json` 을 열고 `Ctrl + F` 로 `198.51.100.90` 을 검색해 찾습니다.

**확인** — 단계 4가 `high dami 60 ['퇴사한 계정']` 으로 시작하는 다섯 줄이고 맨 아래가 `low 198.51.100.90 30 ['경로 스캔']` 이면 성공입니다. 안 나오면 아래 실습 4-1 정답 펼침의 출력과 한 줄씩 맞춰 보고, 오류가 나면 위 「직접 쓰는 곳」의 확인을 다시 봅니다.

## 실습 4-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| ① 규칙마다 점수 채우기 | `points = findings_table["rule"].map(WEIGHTS)` |
| ② 대상마다 점수 더하기 | `totals = grouped["points"].sum()` |
| 등급 정하기(미리 채움) | `if score >= HIGH_LIMIT:` → `return "high"` |
| 기록 만들기(미리 채움) | `record = {"entity": entity, "score": int(score), …}` |

---
<!-- answer: 08|실습 4-1 정답 -->
