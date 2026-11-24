---
id: m4-u05-l02
title: 실습 5-1 · 요청이 갑자기 늘어난 분 찾기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/104_day03_pm_traffic_alerts.md
  mission_id: GichanSource.m4-1104-pm-traffic-alerts
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 5-1 · 요청이 갑자기 늘어난 분 찾기

## 이번 의뢰: 요청이 급증한 시간대

> **오늘 들어온 일**
>
> A사 서버 담당자가 보낸 메시지입니다:
> 「오늘 오전 9시대에 홈페이지가 잠깐 느려졌다는 문의가 들어왔습니다. 웹 서버 이벤트 28개에서 요청이 갑자기 늘어난 때가 있는지 찾아 주세요.
>
> 지난 7일 같은 시간대에는 1분에 평균 2번쯤 요청이 들어왔습니다. 그 3배(6번) 이상이면 급증했다고 보기로 했습니다.」
> - **왜 중요한가**: <mark>요청이 갑자기 늘면 서버가 느려지거나 멈출 수 있고, 공격의 징후일 수도 있습니다.</mark> 하루 전체 요청 수로는 1분 동안의 급증이 보이지 않으므로, 분마다 세어 평소와 비교합니다.

## 왜 초를 버리고 분 단위로 세는가

1. Unit 4의 로그인 실패 규칙은 **같은 주소가 몇 번 실패했는가**를 봤습니다. <mark>이번 Unit의 규칙은 **짧은 시간에 요청이 몇 개 들어왔는가**를 봅니다.</mark>
2. 짧은 시간의 요청 수를 세려면 이벤트를 **같은 분으로 그룹화해야** 합니다. <mark>그런데 이벤트의 시각은 초까지 적혀 있어서(`09:12:03`, `09:12:06`) 그대로 두면 모두 다른 시각입니다.</mark>
3. <mark>그래서 **시각에서 초를 버려** 분까지만 남기고, 같은 분으로 그룹화해 셉니다.</mark>

## 1.1 트래픽 급증 규칙과 판다스 한 가지

| 말 | 뜻 | 이번 Unit의 예 |
|---|---|---|
| 트래픽 급증 | 짧은 시간에 요청이 평소보다 크게 늘어남 | 한 분에 요청이 많이 들어옴 |
| 평소 기준(baseline) | 지난 7일 같은 시간대의 분당 평균 요청 수 | 2번 |
| 급증 기준 | 평소 평균의 3배 | 6번 이상 |

지난 7일의 숫자는 이렇게 생겼습니다(연습용 숫자입니다).

| 날짜 | 1분 평균 요청 수 |
|---|---|
| 10/26 | 2 |
| 10/27 | 2 |
| 10/28 | 3 |
| 10/29 | 2 |
| 10/30 | 1 |
| 10/31 | 2 |
| 11/1 | 2 |

- 평균은 (2 + 2 + 3 + 2 + 1 + 2 + 2) ÷ 7 = **2.0**이고, <mark>급증 기준은 2.0 × 3 = **6.0**번입니다.</mark>
- 실습 4-1과 같은 순서입니다: 평소를 구하고, 그 숫자에서 기준을 정합니다. <mark>달라진 점은 「최댓값 + 1」 대신 「평균의 3배」를 쓴다는 것입니다.</mark> 1분 요청 수는 1 ~ 3개로 자주 달라집니다. 그래서 평균의 3배 이상일 때만 급증으로 봅니다.
- 이번 Unit에서는 이 기준을 **고정**하고, 값을 바꿔 가며 비교하지 않습니다.
- 이 규칙은 분마다 요청이 **몇 개**인지만 봅니다. <mark>요청의 내용(어떤 경로를 요청했는지)은 보지 않습니다.</mark>
- 급증은 이상 징후(평소 범위를 벗어난 일)의 한 종류입니다. <mark>급증이 있다고 공격이 확정되는 것은 아니고,</mark> 먼저 확인할 대상이 정해질 뿐입니다.

**판다스 문법 상자 — 시각에서 초를 버려 분으로 맞추기**

**<mark>`시각.dt.floor("min")`</mark> 은 시각에서 초를 버리고 분까지만 남깁니다. `09:12:03` 도 `09:12:15` 도 `09:12:00` 이 되어, 같은 분의 이벤트가 같은 값을 갖습니다**

`pd.to_datetime` 으로 문자열 시각을 시각 값으로 바꾼 뒤에 <mark>`.dt` 를 붙여 씁니다</mark>. `.dt.hour` 는 「시」를 숫자 하나로 꺼냈지만, <mark>`.dt.floor("min")` 은 **시각 값 그대로** 두고 초만 0 으로 만듭니다.</mark> `floor` 는 「내림」(작은 쪽으로 맞춤)이라는 뜻이고, `"min"` 은 분(minute)의 줄임말입니다.

| 행 번호 | `time` 열(문자열) | `times`(시각 값) | `minutes`(`.dt.floor("min")`) |
|---|---|---|---|
| 0 | 2026-11-02 09:01:05 | 2026-11-02 09:01:05 | 2026-11-02 09:01:00 |
| 1 | 2026-11-02 09:01:06 | 2026-11-02 09:01:06 | 2026-11-02 09:01:00 |
| 2 | 2026-11-02 09:20:10 | 2026-11-02 09:20:10 | 2026-11-02 09:20:00 |

위 표의 첫 두 줄은 시각이 달랐지만 `minutes` 에서는 같은 값이 됩니다. 같은 값이 몇 번 나오는지(`value_counts`) 세어 차이를 봅니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {  # 연습용 작은 데이터 — 같은 분에 이벤트가 두 개
    "time": ["2026-11-02 09:01:05", "2026-11-02 09:01:06", "2026-11-02 09:20:10"],  # time 열에 들어갈 값들
}
logs = pd.DataFrame(data)  # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
times = pd.to_datetime(logs["time"])  # 문자열 시각을 시각 값으로 바꾼다
time_event_counts = times.value_counts()  # 같은 시각이 몇 번씩 나오는지 센다
print(time_event_counts)  # 초까지 같은 시각은 한 번뿐이다
```

실행 결과:

```
time
2026-11-02 09:01:05    1
2026-11-02 09:01:06    1
2026-11-02 09:20:10    1
Name: count, dtype: int64
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
minutes = times.dt.floor("min")  # 시각에서 초를 버린다 (09:01:05 → 09:01:00)
minute_event_counts = minutes.value_counts()  # 같은 분이 몇 번씩 나오는지 센다
print(minute_event_counts)  # 09:01 분이 두 번 나온다
```

실행 결과:

```
time
2026-11-02 09:01:00    2
2026-11-02 09:20:00    1
Name: count, dtype: int64
```

- 읽는 법: 초까지 있는 `times` 에서는 세 시각이 모두 달라서 각각 **1**번입니다. <mark>분까지만 남긴 `minutes` 에서는 09:01 분이 **2**번 나옵니다.</mark> 같은 분에 이벤트가 여러 개 모여 있는 것이 이번 Unit에서 찾으려는 트래픽 급증입니다.
- **`.dt` 없이 `times.floor("min")` 으로 쓰면 오류가 납니다**(아래 「자주 틀리는 곳」). Unit 3에서 쓴 `times.dt.hour` 처럼 `.dt` 를 먼저 붙입니다.
- 이 예는 연습용 작은 표이고, 문제에서는 웹 서버 이벤트의 시각을 이렇게 분으로 맞춰 셉니다.

**알아 둘 것 — 출력 맨 아래의 `dtype: int64`**

`value_counts()` 나 `groupby().size()` 로 센 결과의 맨 아래에는 `dtype: int64` 가 함께 나옵니다. `dtype` 은 data type(데이터 타입)의 줄임말로 값의 종류를 뜻하고, `int64` 는 정수(소수점 없는 숫자)입니다. <mark>숫자 계산이 되는 정상 상태이므로 지금은 `int64` 가 보이면 됩니다.</mark> 자세한 쓰임은 다음에 차차 배웁니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 파일 속 이벤트 57개를 표 한 개(events)로 읽는다 — 행 하나가 이벤트 하나

source_event_counts = events["source"].value_counts()  # source 열을 꺼내 바로 값별 개수를 센다
print(source_event_counts)  # 맨 아래에 dtype: int64 가 함께 나온다
```

실행 결과:

```
source
web       28
server    15
saas      14
Name: count, dtype: int64
```

| dtype | 뜻 | 예 |
|---|---|---|
| `int64` | 정수 | 5 · 200 |
| `float64` | 소수 | 1.4 |
| `object` | 문자열 | `"실패"` |
| `bool` | `True` · `False` | `is_fail` 열 |
| `datetime64[ns]` | 시각 값 | 2026-11-02 09:12:03 |

- 숫자인데 `object` 로 나오면 <mark>문자열로 읽힌 것이라 합계 · 비교가 맞지 않습니다.</mark>

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_events` | 파일 경로 | 이벤트 표(미리 채움) |
| `add_minute_column` | 이벤트 표 | `minute` 열이 붙은 이벤트 표 |
| `count_web_per_minute` | `minute` 열이 있는 표 | 웹 서버 요청이 분마다 몇 개인지 |
| `make_traffic_limit` | 파일 경로와 3(배) | 급증 기준(평균 × 3) |
| `pick_spike_minutes` | 분마다 요청 수와 급증 기준 | 기준 이상인 분과 요청 수 |

- **직접 쓰는 곳은 네 함수**(번호 1 ~ 6)입니다.
  - `add_minute_column`(1번): 초를 버린 시각을 만듭니다. 그 시각을 `minute` 열로 붙이는 줄은 아직 배우지 않은 문법이라 미리 채웠습니다.
  - `count_web_per_minute`(2 · 3번): 웹 서버 이벤트만 걸러 냅니다. 분마다 그룹화해 세는 줄은 미리 채웠습니다.
  - `make_traffic_limit`(4번): 평균에 3을 곱해 급증 기준을 정합니다. 파일을 읽고 평균을 구하는 줄은 실습 4-1과 같아서 미리 채웠습니다.
  - `pick_spike_minutes`(5 · 6번): 기준 이상인 분만 남깁니다. 실습 4-2의 `pick_alert_ips` 와 같은 모양입니다.

## 실습 5-1 · 분마다 세어 요청 급증 분 찾기

**이런 상황이 있습니다**

- **지금은**: 웹 서버 이벤트 28개가 초 단위로 흩어져 있어서, 어느 1분에 요청이 늘었는지 한눈에 안 보입니다.
- **그래서 만드는 것**: `traffic_detection.py` 입니다.
  - 이벤트마다 초를 버린 시각(`minute`)을 붙입니다.
  - 웹 서버 이벤트만 골라 분마다 요청 수를 셉니다.
  - 지난 7일 평균의 3배를 급증 기준으로 정하고, 기준 이상인 분만 남깁니다.
- **실행하면**: 단계 1: 시각과 분 비교, 단계 2: 분당 요청 수, 단계 3: 급증 기준, 단계 4: 요청이 급증한 분이 나옵니다.
- **현업에서는**: 트래픽 급증 규칙은 서버 장애와 공격을 함께 탐지하는 기본 규칙입니다. 알림이 오면 그 분의 요청을 누가 보냈는지부터 봅니다.

**할 일**

1. `traffic_detection.py` · `exercise5-1_run.py` **두 파일**을 만들고, `traffic_detection.py` 의 **네 함수**에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>시각과 분의 차이</mark>(단계 1), <mark>분당 요청 수</mark>(단계 2), <mark>급증 기준</mark>(단계 3), <mark>요청이 급증한 분</mark>(단계 4)를 읽습니다.

**`traffic_detection.py`**

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"  # 읽을 정규화 이벤트 파일 이름
TRAFFIC_PATH = "baseline_traffic.csv"  # 지난 7일 같은 시간대의 분당 요청 수 파일 이름
SPIKE_MULTIPLE = 3  # 평소 평균의 3배 이상이면 급증으로 본다


def load_events(path):  # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)  # 파일 속 이벤트를 표 한 개로 읽는다
    return events  # 이벤트 표를 리턴한다


def add_minute_column(events):  # 이벤트 표를 받는 함수
    """이벤트마다 시각에서 초를 버린 minute 열을 붙인다.
    분당 요청 수를 세기 전에 같은 분으로 그룹화할 기준을 만들 때 쓴다.
    """
    times = pd.to_datetime(events["time"])  # 문자열 시각을 시각 값으로 바꾼다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. times 에 .dt.floor("min") 을 붙여 초를 버린 시각을 minutes 에 담는다
    events["minute"] = minutes  # 표에 minute 열을 붙인다 — 미리 채운 줄
    return events  # minute 열이 붙은 표를 리턴한다


def count_web_per_minute(events):  # minute 열이 있는 이벤트 표를 받는 함수
    """웹 서버 이벤트만 골라 분마다 요청이 몇 개인지 센다.
    분당 요청 수를 평소와 비교하기 전에 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. events["source"] == "web" 으로 행마다 True 또는 False 를 구해 is_web 에 담는다 (웹 서버 이벤트이면 True)
    # 3. events 에서 is_web 이 True 인 행만 골라 web_events 에 담는다 (events[is_web])
    minute_request_counts = web_events.groupby("minute").size()  # minute 값이 같은 행끼리 그룹으로 만들고(groupby) 바로 그룹마다 행이 몇 개인지(그 분의 요청 수) 센다(size)
    return minute_request_counts  # 분마다 요청 수를 리턴한다


def make_traffic_limit(path, multiple):  # 파일 경로와 몇 배인지를 받는 함수
    """지난 7일 분당 요청 평균의 multiple 배를 급증 기준으로 정한다.
    평소보다 요청이 크게 늘어난 분을 가려낼 급증 기준을 정할 때 쓴다.
    """
    baseline = pd.read_csv(path)  # 지난 7일 파일을 표로 읽는다
    average = baseline["requests_per_minute"].mean()  # 분당 요청 수 열을 꺼내(["requests_per_minute"]) 바로 7개의 평균을 구한다(mean)
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. average 에 multiple 을 곱해 limit 에 담는다
    return limit  # 급증 기준을 리턴한다


def pick_spike_minutes(minute_request_counts, limit):  # 분마다 요청 수와 급증 기준을 받는 함수
    """요청 수가 급증 기준 이상인 분만 골라 리턴한다.
    알림을 보낼 분을 가릴 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. minute_request_counts 가 limit 이상인지 비교한 결과(>=)를 is_spike 에 담는다
    # 6. minute_request_counts 에서 is_spike 가 True 인 것만 골라 spike_minutes 에 담는다 (minute_request_counts[is_spike])
    return spike_minutes  # 요청이 급증한 분과 요청 수를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 6번은 모두 함수 안이라 앞에 공백 4개입니다.
- 미리 채운 두 줄은 동작 두 개를 점으로 이은 한 줄입니다. <mark>왼쪽부터 차례로 읽습니다.</mark> `web_events.groupby("minute").size()` 는 ① minute 이 같은 행끼리 그룹을 만들고 ② 그룹마다 행 수를 세고, `baseline["requests_per_minute"].mean()` 은 ① 분당 요청 수 열을 꺼내 ② 평균을 구합니다.
- 번호 주석이 연달아 붙어 있어도(예: 5 · 6번), <mark>주석 사이마다 줄을 끼워 넣어 각 주석 바로 아래 줄에 그 번호의 코드를 하나씩 씁니다.</mark>
- 채우기 전에 실행하면 `NameError: name 'minutes' is not defined` 오류가 납니다. 1번을 아직 안 써서 `minutes` 가 없기 때문입니다.

**`exercise5-1_run.py`** — **그대로 붙여 넣습니다.** 직접 쓰는 줄은 없습니다. `.head(3)` 는 열의 처음 3개만 꺼냅니다.

```python
from traffic_detection import load_events, add_minute_column, count_web_per_minute, make_traffic_limit, pick_spike_minutes, EVENTS_PATH, TRAFFIC_PATH, SPIKE_MULTIPLE  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)  # 이벤트 파일을 표로 읽는다
events = add_minute_column(events)  # 시각에서 초를 버린 minute 열을 붙인다
times = events["time"]  # time 열만 꺼낸다
minutes = events["minute"]  # minute 열만 꺼낸다
first_times = times.head(3)  # 시각의 처음 3개만 꺼낸다
first_minutes = minutes.head(3)  # 분의 처음 3개만 꺼낸다
print("--- 단계 1: time 열과 minute 열의 처음 3개 비교")  # 단계 1 시작을 알리는 줄
print(first_times)  # 처음 3개의 시각을 출력한다
print(first_minutes)  # 처음 3개의 분을 출력한다

minute_request_counts = count_web_per_minute(events)  # 웹 서버 요청을 분마다 센다
print("--- 단계 2: 웹 서버의 분당 요청 수")  # 단계 2 시작을 알리는 줄
print(minute_request_counts)  # 분마다 요청 수를 출력한다

limit = make_traffic_limit(TRAFFIC_PATH, SPIKE_MULTIPLE)  # 지난 7일 평균으로 급증 기준을 정한다
print("--- 단계 3: 급증 기준(평소 평균의", SPIKE_MULTIPLE, "배)", limit, "번 이상")  # 단계 3 시작을 알리는 줄과 급증 기준

spike_minutes = pick_spike_minutes(minute_request_counts, limit)  # 기준 이상인 분만 고른다
print("--- 단계 4: 요청이 급증한 분")  # 단계 4 시작을 알리는 줄
print(spike_minutes)  # 요청이 급증한 분과 요청 수를 출력한다
```

**순서**

1. **[VS Code]** 파일 `traffic_detection.py` · `exercise5-1_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `traffic_detection.py` 에서 직접 쓰는 곳 **여섯 군데**를 씁니다. 위 판다스 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise5-1_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise5-1_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. `--- 단계` 제목 줄은 세지 않습니다. 단계 1은 시각 4줄과 분 4줄(각각 마지막은 `Name:` 줄), 단계 2는 16줄(`minute` 줄 · 분마다 14줄 · `dtype:` 줄), 단계 3은 제목 줄에 숫자가 함께 나오고, 단계 4는 3줄(`minute` 줄 · 급증한 분 한 줄 · `dtype:` 줄)입니다. 실습 결과 기록의 (나) · (다)에서 이벤트를 찾을 때는 VS Code 로 `normalized_events.json` 을 열고 `Ctrl + F`(맥북은 `Cmd + F`)로 `09:12` 또는 `09:20` 을 검색하고, `source` 가 `web` 인 줄만 셉니다. 이벤트 하나의 키는 `time · source · user · ip · action · result` 입니다.
5. **[실습 결과 기록]** `report_u5.md` 의 `## 실습 5-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 급증 기준과 요청이 급증한 분(시각과 요청 수)을 적어 주세요.
   - (나) [핵심 질문] `normalized_events.json` 에서 `time` 이 `2026-11-02 09:12` 로 시작하는 웹 서버(`source` 가 `web`) 줄을 찾아, ① 요청을 보낸 IP 주소와 ② 행동(`action`)별 횟수를 적어 주세요. 그리고 ③ 이 급증을 공격이라고 확정할 수 있는지 이유와 함께 적어 주세요.
   - (다) [핵심 질문] 09:20 에도 웹 서버 요청이 3개 있었지만 급증으로 탐지되지 않았습니다. ① 3개를 급증 기준과 비교해 왜 탐지되지 않았는지 적고, ② `normalized_events.json` 에서 09:20 의 `web` 줄 3개가 어떤 요청(IP 주소 · 행동 · 결과)인지 적고, ③ 요청 수만 보는 급증 규칙이 이 요청들을 놓치는 이유를 적어 주세요.

<!-- answer: 04|실습 5-1 정답 -->

## 실습 5-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 초를 버려 분으로 | `minutes = times.dt.floor("min")` → `events["minute"] = minutes` |
| 웹 서버 이벤트만 | `is_web = events["source"] == "web"` → `web_events = events[is_web]` |
| 급증 기준 | `limit = average * multiple` (평균 2.0 × 3 = 6.0) |
| 기준 이상인 분 | `is_spike = minute_request_counts >= limit` → `spike_minutes = minute_request_counts[is_spike]` |

---
