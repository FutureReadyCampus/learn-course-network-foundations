---
id: m5-u08-l02
title: Exercise 8-1 · 초동 대응 리포트 파일 생성
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/130_day05_am_report_gate.md
  mission_id: GichanSource.m5-1113-am-report-gate
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 8-1 · 초동 대응 리포트 파일 생성

## 이번에 만들 것: 초동 대응 리포트

> **오늘 들어온 일**
>
> - **상황**: <mark style="background:#e0d4ff">Unit 7의 Exercise 7-2 프로그램</mark>은 티켓 7장을 파일로 저장했습니다. 화면에는 근무 중 발생한 사건 · 평균 확인 시간 · 평균 해결 시간 · 응답 기한(SLA)을 넘긴 티켓 수 · 다음 근무자에게 인계할 티켓 목록이 나왔습니다. 이번 Unit에서 팀장이 「Unit 7 근무의 초동 대응 리포트를 고객사에 보낼 수 있게 파일로 만들어 주세요」라고 요청합니다. **초동 대응**(initial response, 이니셜 리스폰스)은 사건이 발생한 직후 처음 한 대응입니다.
> - **문제**: 티켓 파일과 조치 기록 파일이 따로 있어서, 사람이 손으로 옮겨 적으면 누락이 생기기 쉽습니다. 예를 들어 `INC-212`(`yuna` 계정 잠금)는 조치는 실행됐는데 티켓이 없습니다(티켓 추적 누락). <mark style="background:#ffc4d6">티켓만 보고 리포트를 쓰면 이 사건이 누락됩니다.</mark>
> - **부탁**: 티켓 파일은 판다스 표로 바꿔 집계하고, 조치 기록 파일은 티켓과 대조해 주세요. 그 결과를 리포트 파일 하나로 써 주세요. 리포트에는 여섯 가지가 들어갑니다. 티켓별 상태, 탐지 규칙별 티켓 수, 등급별 평균 확인 시간, 응답 기한(SLA)을 넘겨 확인한 티켓, 티켓이 없는 조치, 높음 등급 티켓의 처리 경위입니다. 평균 확인 시간(MTTA, Mean Time To Acknowledge, 엠티티에이)은 티켓 생성부터 담당자가 처음 확인하기까지 걸린 평균 시간입니다. 처리 경위는 생성 → 확인 → 해결 시각을 시간순으로 이은 기록입니다.
> - **바뀌는 점**: 실행 한 번으로 `incident_report_20261112.md` <mark style="background:#bde3ff">32줄</mark>이 생성됩니다. 오늘 샘플에서는 응답 기한(SLA)을 넘겨 확인한 티켓 <mark style="background:#bde3ff">2장</mark>(`TCK-3` · `TCK-4`)과 티켓이 없는 조치 <mark style="background:#bde3ff">1건</mark>(`INC-212`)이 리포트에 따로 적힙니다. 상황과 이름은 설명을 위한 예시입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다. (문법 상자의 코드는 눈으로 읽어도 되고, 따라 쳐 보아도 됩니다.)

## 읽기 · 1.1 인시던트 리포트에 담을 네 가지

| 리포트의 절 | 읽는 사람이 알고 싶은 것 | 만드는 방법 |
|---|---|---|
| 1. 티켓별 초동 대응 | 사건마다 지금 상태와 조치 기록 수 | 티켓을 한 장씩 읽어 한 줄씩 쓴다 (미리 채움) |
| 2. 규칙별 티켓 수 | 어떤 탐지 규칙의 사건이 많았나 (규칙별 건수) | `value_counts()`(값마다 개수를 세는 판다스 함수) (2 · 8번) |
| 3. 등급별 평균 확인 시간 | 심각도(severity, 시버리티: 사건의 위험 정도) 등급(high 높음 · mid 중간 · low 낮음) 가운데 급한 등급을 빨리 확인했나 | 확인까지 걸린 분 열을 만들고, 확인한 티켓만 필터링(조건에 맞는 행만 남기기)해 등급마다 평균 확인 시간(MTTA)을 구한다 (1 · 3 · 4번) |
| 4. 응답 기한을 넘겨 확인한 티켓 | 응답 기한 위반(SLA breach, 에스엘에이 브리치: 약속한 응답 기한을 지키지 못한 일) 티켓은 무엇인가 | <mark style="background:#ffdcb0">`acked_at` 이 `sla_due` 보다 큰</mark> 행(row, 로우: 표의 가로 줄)만 필터링한다 (5번) |
| 5. 티켓이 없는 조치 | 티켓 없이 실행되어 추적에서 누락될 뻔한 조치는 무엇인가 | 조치 기록의 인시던트 번호를 티켓의 인시던트 번호와 대조해, 어느 티켓에도 없는 것을 찾는다 (6 · 7번) |
| 6. 높음(high) 티켓의 처리 경위 | 높음 등급 사건은 어떤 순서로 처리됐는가 | 티켓의 생성 · 확인 · 해결 시각을 시간순으로 이은 한 줄을 만든다(미리 채움) |

- 리포트 파일은 **마크다운**(Markdown, 마크다운: `#` 로 제목, `-` 로 목록을 쓰는 글 형식) 파일입니다. 이 안내 문서도 마크다운입니다. VS Code 에서 열고 `Ctrl+Shift+V`(맥북은 `Cmd+Shift+V`)를 누르면 제목과 목록 모양으로 볼 수 있습니다.
- 아직 확인하지 않은 티켓(미확인, unacknowledged)은 `acked_at` 이 `-1` 입니다. 그대로 빼면 확인까지 걸린 분이 <mark style="background:#ffc4d6">음수</mark>가 됩니다(예: `TCK-2` 는 −1 − 3 = −4분). 이 값이 평균에 들어가면 평균 확인 시간이 실제보다 짧게 계산되므로, 평균을 구하기 전에 <mark style="background:#ffdcb0">`acked_at` 이 0 이상인 행만 필터링</mark>합니다.
- 확인은 했지만 아직 해결하지 않은 티켓(`TCK-4` · `TCK-7`)은 평균에 포함됩니다. 평균 확인 시간은 확인한 시각까지만 측정하는 지표이고, 해결까지 걸린 평균 시간(MTTR, Mean Time To Resolve, 엠티티알)과는 별개이기 때문입니다.

**판다스 문법 상자 — 그룹마다 평균 `그룹["열"].mean()` 과 반올림 `.round(1)`**

```python
import pandas as pd

table = pd.DataFrame([
    {"grade": "high", "ack_minutes": 10},
    {"grade": "mid", "ack_minutes": 72},
    {"grade": "mid", "ack_minutes": 55},
])
groups = table.groupby("grade")
grade_means = groups["ack_minutes"].mean()
print(grade_means.round(1).to_dict())
```

| 코드 | 뜻 |
|---|---|
| `groups["ack_minutes"].mean()` | <mark style="background:#e0d4ff">4과목에서 배운 `그룹["열"].sum()`</mark> 과 같은 모양입니다. 합계 대신 그룹마다 평균을 구하는 그룹별 집계입니다. 그룹은 `table.groupby("grade")` 처럼 grade 값이 같은 행끼리 묶은 것입니다 |
| `.round(1)` | 소수 첫째 자리까지 반올림합니다 |
| 위 코드의 출력 | <mark style="background:#bde3ff">`{'high': 10.0, 'mid': 63.5}`</mark> 입니다. mid 는 <mark style="background:#bde3ff">(72 + 55) ÷ 2 = 63.5</mark> 입니다 |

- 4절은 <mark style="background:#ffdcb0">확인 시각(`acked_at`)이 응답 기한 시각(`sla_due`)보다 늦은</mark> 티켓, 즉 SLA 위반 티켓만 집계합니다.
- 오늘 샘플에서 아직 확인하지 않은 티켓은 `TCK-2` · `TCK-5` 입니다. 근무는 180분에 끝났는데 둘의 응답 기한 시각은 243분 · 270분이라서, <mark style="background:#bde3ff">기한이 아직 지나지 않았으므로 위반으로 집계하지 않습니다</mark>.
- `table[table["acked_at"] > table["sla_due"]]` 는 <mark style="background:#e0d4ff">4과목에서 배운</mark> 「조건으로 행 필터링(filtering, 필터링: 조건에 맞는 행만 남기기)하기」와 같은 모양입니다. 여기서 `table` 은 DataFrame(데이터프레임: 행과 열로 이루어진 판다스의 표)입니다. 조건에 숫자 대신 다른 열을 쓴 것만 다릅니다. 바로 아래 문법 상자에서 작은 예로 확인합니다.

**판다스 문법 상자 — 두 열로 계산하고 비교하기 `표["열1"] - 표["열2"]` · `표[표["열1"] > 표["열2"]]`**

판다스 표에서 두 열을 같은 행끼리 계산하면 그 결과를 새 열로 추가할 수 있고, 같은 행끼리 비교하면 조건에 맞는 행만 남길 수 있습니다(필터링, filtering). 두 경우 모두 행마다 두 열의 값을 하나씩 확인해서 처리합니다. 아래는 학생 네 명의 수학 · 영어 점수입니다.

```python
import pandas as pd                            # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                       # 표에 넣을 내용(열 이름: 값들)
    "name": ["민지", "서준", "하은", "도윤"],  # name 열 (학생 이름)
    "math": [70, 90, 60, 85],                  # math 열 (수학 점수)
    "english": [85, 80, 75, 85],               # english 열 (영어 점수)
}
df = pd.DataFrame(data)                        # 내용으로 표(DataFrame)를 만든다
print(df)                                      # 표를 출력한다
```

실행 결과:

```
  name  math  english
0   민지    70       85
1   서준    90       80
2   하은    60       75
3   도윤    85       85
```

위 코드에 이어서 실행하는 다음 코드입니다. 영어 점수에서 수학 점수를 뺀 열을 만듭니다.

```python
df["gap"] = df["english"] - df["math"]  # 영어 점수에서 수학 점수를 뺀 값을 gap 열로 추가한다
print(df)                               # 열이 하나 늘어난 표를 출력한다
```

실행 결과:

```
  name  math  english  gap
0   민지    70       85   15
1   서준    90       80  -10
2   하은    60       75   15
3   도윤    85       85    0
```

이어서 실행하는 다음 코드입니다. 영어 점수가 수학 점수보다 높은 학생만 남깁니다.

```python
filtered = df[df["english"] > df["math"]]  # 영어 점수가 수학 점수보다 높은 행만 남긴다
print(filtered)                            # 남은 행을 출력한다
```

실행 결과:

```
  name  math  english  gap
0   민지    70       85   15
2   하은    60       75   15
```

| 코드 | 뜻 |
|---|---|
| `df["english"] - df["math"]` | 같은 행끼리 두 열의 값을 뺍니다. 행마다 결과가 하나씩 나옵니다 |
| `df["gap"] = …` | 그 결과를 `gap` 이라는 새 열로 표에 추가합니다 |
| `df["english"] > df["math"]` | 행마다 영어 점수가 수학 점수보다 크면 `True`, 아니면 `False` 입니다 |
| `df[ … ]` | `True` 인 행만 남깁니다 |
| 위 코드의 출력 | <mark style="background:#bde3ff">`민지`(85 > 70) 와 `하은`(75 > 60) 만 남습니다</mark>. `도윤` 은 85 로 같아서 `>` 조건에 맞지 않으므로 빠집니다 |
| 오늘 문제 | 빼기는 `table["acked_at"] - table["created_at"]`(1번), 비교는 `table[table["acked_at"] > table["sla_due"]]`(5번)와 같은 모양입니다. 확인까지 걸린 분 열을 만들고, 확인 시각이 응답 기한 시각보다 늦은 티켓만 남깁니다 |

함수 일곱 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
report.py   make_ticket_table       : 티켓 리스트를 표로 바꾸고 확인까지 걸린 분 열을 더한다 (1번)
            count_by_rule           : 규칙마다 티켓 수를 센다 (2번)
            mean_ack_by_grade       : 확인한 티켓만 남겨 (3번) 등급마다 평균을 구한다 (4번)
            find_late_tickets       : 기한을 넘겨 확인한 티켓만 남긴다 (5번)
            find_missing_incidents  : 티켓이 없는 조치 기록을 찾는다 (6 · 7번)
            count_actions           : 티켓 한 장의 조치 기록 수를 센다 (미리 채움)
            make_timeline_line      : 티켓 한 장의 생성 · 확인 · 해결 시각을 시간순 한 줄로 만든다 (미리 채움)
            make_report_lines       : 리포트의 줄 리스트를 만든다. 규칙별 줄만 직접 쓴다 (8번)
실행 파일   exercise8-1_run.py        : 표를 만들고 (9번), 결과를 출력하고, 리포트 파일을 쓴다 (미리 채움)
```

> **여기부터 문제입니다.**

## Exercise 8-1 · 초동 대응 리포트 파일 생성

**이런 상황이 있습니다**

- **지금은**: <mark>티켓과 조치 기록이 JSON(제이슨: 키와 값으로 적은 데이터 파일 형식) 파일 두 개에 따로 있고, 사람이 읽을 리포트가 없습니다</mark>.
- **만드는 것**: 표 만들기 · 규칙별 수 · 등급별 평균 · 기한 넘긴 티켓 · 티켓 없는 조치 찾기 · 리포트 줄 만들기(`report.py`), 리포트 파일 쓰기(`exercise8-1_run.py`).
- **실행하면**: <mark>단계 1: 불러온 수, 단계 2: 규칙별 티켓 수, 단계 3: 등급별 평균 확인 시간, 단계 4: 기한을 넘긴 티켓과 티켓이 없는 조치, 단계 5: 저장한 리포트 파일이 나옵니다.</mark>

**할 일**: 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행한 뒤 리포트 파일을 열어 읽습니다.

**`report.py`** — 리포트를 만드는 함수 모음입니다. 직접 쓰는 곳은 1 ~ 8번입니다.

```python
import pandas as pd                                                                        # 표를 다루기 위해 판다스를 pd 라는 이름으로 불러온다

REPORT_TITLE = "# 초동 대응 리포트 — 2026-11-12(목) 오전 근무"                             # 리포트 맨 위 제목


def make_ticket_table(tickets):                                                            # 티켓 리스트를 받는 함수
    """티켓 리스트를 표(DataFrame)로 바꾸고, 확인까지 걸린 분(ack_minutes) 열을 더해 리턴한다.
    티켓마다 담당자가 얼마나 빨리 확인했는지를 표 하나로 계산할 때 쓴다.
    """
    table = pd.DataFrame(tickets)                                                          # 티켓 리스트를 표로 바꾼다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. table["acked_at"] - table["created_at"] 를 table["ack_minutes"] 에 저장한다 (확인까지 걸린 분)
    return table                                                                           # 열을 더한 표를 리턴한다 — 미리 채운 줄


def count_by_rule(table):                                                                  # 티켓 표를 받는 함수
    """탐지 규칙마다 티켓이 몇 장인지 세어 딕셔너리로 리턴한다.
    어떤 규칙의 사건이 많았는지 리포트 첫머리에 보여 줄 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. table["rule"].value_counts() 를 rule_counts 에 저장한다
    return rule_counts.to_dict()                                                           # 센 결과를 딕셔너리로 바꿔 리턴한다 — 미리 채운 줄


def mean_ack_by_grade(table):                                                              # 티켓 표를 받는 함수
    """확인한 티켓만 남겨 등급마다 확인까지 걸린 분의 평균을 구하고, 소수 첫째 자리까지 딕셔너리로 리턴한다.
    급한 등급일수록 빨리 확인했는지 리포트로 보여 줄 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 3. table["acked_at"] >= 0 인 행만 남겨 acked 에 저장한다 (확인한 티켓만)
    groups = acked.groupby("grade")                                                        # 등급이 같은 행끼리 묶는다 — 미리 채운 줄
    # 4. groups["ack_minutes"].mean() 을 grade_means 에 저장한다 (등급마다 평균)
    rounded = grade_means.round(1)                                                         # 소수 첫째 자리까지 반올림한다 — 미리 채운 줄
    return rounded.to_dict()                                                               # 등급별 평균을 딕셔너리로 바꿔 리턴한다 — 미리 채운 줄


def find_late_tickets(table):                                                              # 티켓 표를 받는 함수
    """응답 기한 시각(sla_due)보다 늦게 확인한 티켓을 딕셔너리 리스트로 리턴한다.
    응답 기한을 넘긴 티켓을 리포트에 이름으로 남길 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. table["acked_at"] > table["sla_due"] 인 행만 남겨 late 에 저장한다
    return late.to_dict("records")                                                         # 남은 행을 딕셔너리 리스트로 바꿔 리턴한다 — 미리 채운 줄


def find_missing_incidents(actions, tickets):                                              # 조치 기록 리스트와 티켓 리스트를 받는 함수
    """조치 기록 가운데 어느 티켓에도 들어 있지 않은 인시던트의 기록을 리스트로 리턴한다.
    조치는 했는데 티켓이 없어 리포트에서 빠지는 사건을 찾을 때 쓴다.
    """
    covered = []                                                                           # 티켓에 들어 있는 인시던트 번호를 모을 빈 리스트 — 미리 채운 줄
    for ticket in tickets:                                                                 # 티켓을 하나씩 읽는다 — 미리 채운 줄
        for incident_id in ticket["incidents"]:                                            # 티켓에 합쳐진 인시던트 번호를 하나씩 읽는다 — 미리 채운 줄
            covered.append(incident_id)                                                    # 번호를 추가한다 — 미리 채운 줄
    missing = []                                                                           # 티켓이 없는 조치 기록을 모을 빈 리스트 — 미리 채운 줄
    for action in actions:                                                                 # 조치 기록을 하나씩 읽는다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 6. action["incident"] 가 covered 안에 없으면 (if, not in)
            # 7. missing 에 action 을 추가한다 (append)
    return missing                                                                         # 티켓이 없는 조치 기록 리스트를 리턴한다 — 미리 채운 줄


def count_actions(ticket, actions):                                                        # 티켓 한 장과 조치 기록 리스트를 받는 함수
    """티켓에 합쳐진 인시던트의 조치 기록이 몇 건인지 세어 리턴한다.
    리포트의 티켓 줄에 조치 기록 수를 함께 적을 때 쓴다.
    """
    count = 0                                                                              # 조치 기록 수 : 처음에는 0
    for action in actions:                                                                 # 조치 기록을 하나씩 읽는다
        if action["incident"] in ticket["incidents"]:                                      # 이 티켓의 인시던트 기록이면
            count = count + 1                                                              # 1 늘린다
    return count                                                                           # 센 수를 리턴한다


def make_timeline_line(ticket):                                                            # 티켓 한 장을 받는 함수
    """티켓 한 장의 생성 · 확인 · 해결 시각을 시간순으로 이은 한 줄을 리턴한다.
    높음 등급 사건이 어떤 순서로 처리됐는지 리포트에 처리 경위로 남길 때 쓴다.
    """
    steps = [str(ticket["created_at"]) + "분 티켓 생성"]                                   # 생성 시각으로 시작한다
    if ticket["acked_at"] >= 0:                                                            # 확인했으면 (확인 전이면 -1)
        steps.append(str(ticket["acked_at"]) + "분 담당자 확인")                           # 확인 시각을 추가한다
    if ticket["resolved_at"] >= 0:                                                         # 해결했으면 (해결 전이면 -1)
        steps.append(str(ticket["resolved_at"]) + "분 해결")                               # 해결 시각을 추가한다
    return "- " + ticket["id"] + " · " + ticket["entity"] + ": " + " → ".join(steps)       # 시각을 화살표로 이어 한 줄로 리턴한다


def make_report_lines(tickets, actions, rule_counts, grade_means, late_tickets, missing):  # 리포트에 넣을 재료를 받는 함수
    """리포트에 넣을 재료로 마크다운 문서의 줄 리스트를 만들어 리턴한다.
    근무가 끝난 뒤 사람이 읽을 초동 대응 리포트를 자동으로 쓸 때 쓴다.
    """
    lines = [REPORT_TITLE, ""]                                                             # 제목과 빈 줄로 시작한다 — 미리 채운 줄
    lines.append("## 1. 티켓별 초동 대응")                                                 # 1절 제목 — 미리 채운 줄
    for ticket in tickets:                                                                 # 티켓을 하나씩 읽는다 — 미리 채운 줄
        action_count = count_actions(ticket, actions)                                      # 이 티켓의 조치 기록 수 — 미리 채운 줄
        head = "- " + ticket["id"] + " [" + ticket["grade"] + "] " + ticket["entity"] + " — " + ticket["rule"]  # 티켓 번호 · 등급 · 대상 · 규칙 — 미리 채운 줄
        lines.append(head + " · 상태 " + ticket["status"] + " · 조치 기록 " + str(action_count) + "건")  # 티켓 한 줄을 추가한다 — 미리 채운 줄
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 2. 규칙별 티켓 수")                                                   # 2절 제목 — 미리 채운 줄
    for rule in rule_counts:                                                               # 규칙 이름을 하나씩 읽는다 — 미리 채운 줄
        count = rule_counts[rule]                                                          # 그 규칙의 티켓 수 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 8. "- " + rule + ": " + str(count) + "장" 을 lines 에 추가한다 (append)
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 3. 등급별 평균 확인 시간(분)")                                        # 3절 제목 — 미리 채운 줄
    for grade in grade_means:                                                              # 등급을 하나씩 읽는다 — 미리 채운 줄
        lines.append("- " + grade + ": " + str(grade_means[grade]) + "분")                 # 등급 한 줄을 추가한다 — 미리 채운 줄
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 4. 응답 기한을 넘겨 확인한 티켓")                                     # 4절 제목 — 미리 채운 줄
    for ticket in late_tickets:                                                            # 늦게 확인한 티켓을 하나씩 읽는다 — 미리 채운 줄
        lines.append("- " + ticket["id"] + " · 기한 " + str(ticket["sla_due"]) + "분 · 확인 " + str(ticket["acked_at"]) + "분")  # 티켓 한 줄을 추가한다 — 미리 채운 줄
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 5. 티켓이 없는 조치 (사람이 티켓을 만들어야 함)")                     # 5절 제목 — 미리 채운 줄
    for action in missing:                                                                 # 티켓이 없는 조치 기록을 하나씩 읽는다 — 미리 채운 줄
        lines.append("- " + action["incident"] + " · " + action["action"] + " · " + action["target"])  # 기록 한 줄을 추가한다 — 미리 채운 줄
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 6. 높음(high) 티켓의 처리 경위")                                      # 6절 제목 — 미리 채운 줄
    for ticket in tickets:                                                                 # 티켓을 하나씩 읽는다 — 미리 채운 줄
        if ticket["grade"] == "high":                                                      # 높음 등급 티켓이면 — 미리 채운 줄
            lines.append(make_timeline_line(ticket))                                       # 처리 경위 한 줄을 추가한다 — 미리 채운 줄
    return lines                                                                           # 완성한 줄 리스트를 리턴한다 — 미리 채운 줄
```

**`exercise8-1_run.py`** — 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다.

```python
from incident import load_json                                                                # Unit 1 파일의 JSON 읽기 함수를 불러온다
from report import make_ticket_table, count_by_rule, mean_ack_by_grade, find_late_tickets, find_missing_incidents, make_report_lines  # 방금 만든 리포트 함수를 불러온다

REPORT_PATH = "incident_report_20261112.md"                                                   # 리포트를 저장할 파일 이름

tickets = load_json("unit10_tickets.json")                                                     # Unit 7 근무의 티켓 파일을 리스트로 읽는다
actions = load_json("unit10_actions.json")                                                     # Unit 7 근무의 조치 기록 파일을 리스트로 읽는다
print("--- 단계 1: 불러온 티켓", len(tickets), "장 · 조치 기록", len(actions), "건")          # 단계 1 시작을 알리는 줄

# ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
# 9. make_ticket_table(tickets) 의 결과를 table 에 저장한다
rule_counts = count_by_rule(table)                                                            # 규칙별 티켓 수
grade_means = mean_ack_by_grade(table)                                                        # 등급별 평균 확인 시간
late_tickets = find_late_tickets(table)                                                       # 응답 기한을 넘겨 확인한 티켓
missing = find_missing_incidents(actions, tickets)                                            # 티켓이 없는 조치 기록

print("--- 단계 2: 규칙별 티켓 수")                                                           # 단계 2 시작을 알리는 줄
for rule in rule_counts:                                                                      # 규칙 이름을 하나씩 읽는다
    print(rule, ":", rule_counts[rule], "장")                                                 # 규칙과 티켓 수를 출력한다

print("--- 단계 3: 등급별 평균 확인 시간(분)")                                                # 단계 3 시작을 알리는 줄
for grade in grade_means:                                                                     # 등급을 하나씩 읽는다
    print(grade, ":", grade_means[grade], "분")                                               # 등급과 평균을 출력한다

print("--- 단계 4: 응답 기한을 넘겨 확인한 티켓", len(late_tickets), "장 · 티켓이 없는 조치", len(missing), "건")  # 단계 4 시작을 알리는 줄
for ticket in late_tickets:                                                                   # 늦게 확인한 티켓을 하나씩 읽는다
    print(ticket["id"], "기한", ticket["sla_due"], "분 · 확인", ticket["acked_at"], "분")     # 티켓과 두 시각을 출력한다
for action in missing:                                                                        # 티켓이 없는 조치 기록을 하나씩 읽는다
    print(action["incident"], action["action"], action["target"], "→ 티켓 없음")              # 기록을 출력한다

lines = make_report_lines(tickets, actions, rule_counts, grade_means, late_tickets, missing)  # 리포트 줄 리스트를 만든다
text = "\n".join(lines) + "\n"                                                                # 줄 리스트를 줄바꿈으로 이어 한 문자열로 만든다
with open(REPORT_PATH, "w", encoding="utf-8") as report_file:                                 # 리포트 파일을 쓰기 모드("w")로 연다
    report_file.write(text)                                                                   # 리포트 문자열을 파일에 쓴다
print("--- 단계 5: 리포트 파일", REPORT_PATH, "·", len(lines), "줄 저장")                     # 단계 5 시작을 알리는 줄과 저장한 줄 수
```

**순서**

1. **[터미널]** 파일 두 개를 만들고 **[VS Code]** 에서 열어 붙여 넣습니다.
   ```bash
   pwd
   touch report.py exercise8-1_run.py
   ls
   ```
2. **[VS Code]** `report.py` 1 ~ 8번, `exercise8-1_run.py` 9번을 씁니다. 막히면 위 문법 상자와 아래 「Exercise 8-1 한눈에」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise8-1_run.py
   ```
4. 출력은 다섯 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 과 단계 5 는 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 5줄, 단계 3 은 2줄입니다.
   - 단계 4 는 숫자가 제목 줄에 함께 나오고 그 아래 3줄입니다.
5. **[VS Code]** 왼쪽 목록에서 `incident_report_20261112.md` 를 열고 `Ctrl+Shift+V`(맥북은 `Cmd+Shift+V`)로 모양을 봅니다. <mark>1 ~ 6절이 보이면</mark> 됩니다.
6. **[보고서]** Unit 8 의 `## Exercise 8-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 티켓이 가장 많은 규칙 두 개와 리포트 파일의 줄 수를 적어 주세요.
   - (나) [핵심 질문] 단계 3 에 low 등급이 없습니다. `unit10_tickets.json` 의 low 티켓 두 장(`TCK-2` · `TCK-5`)의 `acked_at` 을 근거로 그 이유를 적어 주세요. 또 `report.py` 3번(확인한 티켓만 필터링하는 줄)이 없으면 low 의 평균 확인 시간(MTTA)이 얼마로 나오는지도 적어 주세요.
   - (다) [핵심 질문] 리포트 5절에 `INC-212` 가 나왔습니다. `find_missing_incidents` 의 `covered` 리스트를 근거로 그 이유를 적고, 이 절이 없으면 고객사에 보내는 리포트에서 어떤 사건이 추적 누락되는지 적어 주세요.

## Exercise 8-1 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 두 열을 빼서 새 열 만들기 | `table["ack_minutes"] = table["acked_at"] - table["created_at"]` |
| 값마다 개수 세기 | `rule_counts = table["rule"].value_counts()` |
| 조건으로 행 필터링하기 | `acked = table[table["acked_at"] >= 0]` |
| 등급이 같은 행끼리 그룹으로 나누고 그룹마다 평균 | `groups = acked.groupby("grade")` → `grade_means = groups["ack_minutes"].mean()` |
| 다른 열과 비교해 행 필터링하기 | `late = table[table["acked_at"] > table["sla_due"]]` |
| 리스트에 없으면 | `if action["incident"] not in covered:` |
| 리스트에 추가 | `missing.append(action)` |
| 문자열을 이어 붙여 추가 | `lines.append("- " + rule + ": " + str(count) + "장")` |
| 함수 결과를 변수에 저장하기 | `table = make_ticket_table(tickets)` |

---
