---
id: m4-u05-l03
title: 실습 5-2 · 알림을 한 파일로 모으기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/104_day03_pm_traffic_alerts.md
  mission_id: GichanSource.m4-1104-pm-traffic-alerts
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 5-2 · 알림을 한 파일로 모으기

## 이번 의뢰: 알림 형식 맞추기

> **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「로그인 실패 알림 1건, 트래픽 급증 알림 1건이 나왔는데 형식이 달라서 담당자가 따로따로 처리해야 합니다.
>
> 두 알림을 `alerts.json` 한 파일에 같은 모양으로 모아 주세요. 알림마다 종류 · 대상 · 횟수 · 메모를 넣어 주세요. 공격으로 확정된 것은 아니니 처리 상태는 모두 「확인 필요」로 해 주세요.」
> - **왜 중요한가**: <mark>알림 형식이 종류마다 다르면 담당자가 하나씩 해석해야 합니다.</mark> 형식이 같으면 사람도 자동 대응 도구도 같은 방법으로 처리할 수 있습니다.

## 왜 알림 모양을 통일하는가

1. SIEM(심, 보안 로그를 모아 탐지 · 알림하는 시스템)의 네 단계는 **수집 → 정규화 → 탐지 → 알림**입니다. 이번 Unit에서 알림으로 모으는 탐지 결과는 Unit 4의 로그인 실패 규칙과 실습 5-1의 트래픽 급증 규칙, 두 가지입니다. <mark>이제 마지막 단계인 알림을 만듭니다.</mark>
2. <mark>두 규칙의 결과는 모양이 다릅니다.</mark>
   - 로그인 실패 규칙은 「주소와 횟수」(`203.0.113.50` 이 5번)를 냅니다.
   - 트래픽 급증 규칙은 「분과 요청 수」(`09:12` 에 9개)를 냅니다.
3. 알림은 **종류 · 대상 · 횟수 · 메모 · 처리 상태**를 <mark>같은 키로 담아야 한 파일에 모을 수 있습니다.</mark>

## 2.1 알림 한 건의 모양과 지킬 점 두 가지

<mark>알림 한 건은 딕셔너리 하나이고, 키 다섯 개를 가집니다.</mark>

| 키 | 뜻 | 로그인 실패 알림 | 트래픽 급증 알림 |
|---|---|---|---|
| `type` | 알림의 종류 | 비정상 로그인 | 트래픽 급증 |
| `target` | 무엇에 대한 알림인가 | `203.0.113.50`(주소) | `2026-11-02 09:12:00`(분) |
| `count` | 몇 번이었나 | 5 | 9 |
| `note` | 담당자에게 보일 메모 | 로그인 실패가 기준 이상 | 요청이 평소의 3배 이상 |
| `status` | 처리 상태 | 확인 필요 | 확인 필요 |

<mark>처리 상태는 담당자가 조사하면서 바꿉니다.</mark> 예를 들어 「확인 필요」 → 「조사 중」 → 「조사 완료」 순서로 바뀝니다.

알림을 다룰 때 **지킬 점이 둘** 있습니다.

| 지킬 점 | 뜻 | 이 문서에서 |
|---|---|---|
| 알림 있음 ≠ 공격 확정 | 알림은 「먼저 살펴볼 곳」일 뿐이고, 정상적인 일이 기준 이상이 될 수도 있습니다 | `status` 를 모두 「확인 필요」로 둠 |
| 알림 없음 ≠ 안전 | 알림이 없는 것은 규칙에 해당하지 않았다는 뜻일 뿐, 아무 일도 없었다는 뜻이 아닙니다 | 규칙에 해당하지 않으면 알림이 나지 않음 |

**판다스 문법 상자 — 인덱스와 값을 한 쌍씩 꺼내기**

**<mark>`결과.items()`</mark> 는 판다스로 센 결과(시리즈, Series: 인덱스와 값이 한 줄씩 있는 데이터)에서 「인덱스, 값」을 한 쌍씩 꺼냅니다. `for 인덱스, 값 in 결과.items():` 로 반복합니다**

`value_counts()` 나 `groupby().size()` 로 센 결과는 왼쪽이 인덱스(index)이고 오른쪽이 값입니다. 딕셔너리의 `.items()` 와 같은 모양으로, <mark>한 줄이 한 쌍이 됩니다.</mark>

| 센 결과(`source_event_counts`) | 반복에서 꺼내는 쌍 |
|---|---|
| web 3 | `source` 는 `"web"`, `count` 는 3 |
| server 2 | `source` 는 `"server"`, `count` 는 2 |
| saas 1 | `source` 는 `"saas"`, `count` 는 1 |

```python
import pandas as pd                                               # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                          # 연습용 작은 데이터
    "source": ["web", "server", "web", "saas", "web", "server"],  # source 열에 들어갈 값들
}
logs = pd.DataFrame(data)                                         # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
print(logs)                                                       # 표를 출력한다
source_event_counts = logs["source"].value_counts()               # source 열을 꺼내(["source"]) 바로 값별 개수를 센다(value_counts) — 인덱스(web · server · saas)와 개수

for source, count in source_event_counts.items():                 # 인덱스와 개수를 한 쌍씩 꺼낸다
    print(source, count)                                          # 인덱스와 개수를 출력한다
```

실행 결과:

```
   source
0     web
1  server
2     web
3    saas
4     web
5  server
web 3
server 2
saas 1
```

- 읽는 법: 출력 세 줄이 센 결과의 세 줄에 하나씩 대응합니다. <mark>인덱스가 `source` 에, 값이 `count` 에 들어옵니다.</mark>
- 이번 실습에서는 이 인덱스가 주소(`203.0.113.50`)나 분(`2026-11-02 09:12:00`)이고, <mark>값이 횟수입니다.</mark>

**판다스 문법 상자 — 시각 값을 문자열로 바꾸기**

**<mark>`str(시각 값)`</mark> 은 판다스의 시각 값을 `"2026-11-02 09:01:00"` 같은 문자열로 바꿉니다. JSON 파일에는 문자열 · 숫자 · 리스트 · 딕셔너리만 쓸 수 있어서, 시각 값은 문자열로 바꿔야 합니다**

분 단위로 맞춘 `minutes` 는 시각 값입니다. 알림의 `target` 에 넣어 JSON 으로 저장하려면 <mark>먼저 문자열로 바꿉니다.</mark>

| 이름 | 값 | 종류 | JSON 에 쓸 수 있나 |
|---|---|---|---|
| `first_minute` | 2026-11-02 09:01:00 | 판다스 시각 값 | 쓸 수 없음 |
| `text` (`str(first_minute)`) | `"2026-11-02 09:01:00"` | 문자열 | 쓸 수 있음 |

```python
import pandas as pd                                          # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                     # 연습용 작은 데이터
    "time": ["2026-11-02 09:01:05", "2026-11-02 09:20:10"],  # time 열에 들어갈 값들
}
logs = pd.DataFrame(data)                                    # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
times = pd.to_datetime(logs["time"])                         # 문자열 시각을 시각 값으로 바꾼다
minutes = times.dt.floor("min")                              # 시각에서 초를 버린다
first_minute = minutes[0]                                    # 0번 행의 분을 꺼낸다 — 판다스 시각 값이다

text = str(first_minute)                                     # 시각 값을 문자열로 바꾼다
message = text + " 에 이벤트가 있었음"                       # 문자열이라 글을 이어 붙일 수 있다
print(message)                                               # 이어 붙인 글을 출력한다
```

실행 결과:

```
2026-11-02 09:01:00 에 이벤트가 있었음
```

- 읽는 법: <mark>`str()` 을 거치면 문자열이 되어 `+` 로 글을 이어 붙일 수 있습니다.</mark> **시각 값은 문자열이 아니라서 `+` 로 이어 붙이면 오류가 나고, JSON 에도 쓸 수 없습니다.**
- <mark>두 리스트를 하나로 이을 때는 `+` 를 씁니다</mark>: `[1, 2] + [3]` 은 `[1, 2, 3]` 입니다. 실행 파일이 로그인 실패 알림 리스트와 트래픽 급증 알림 리스트를 이어 붙일 때 씁니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `make_alert` | 종류 · 대상 · 횟수 · 메모 | 알림 한 건(딕셔너리) |
| `make_login_alerts` | 알림 대상 주소와 횟수 | 로그인 실패 알림 리스트 |
| `make_traffic_alerts` | 요청이 급증한 분과 요청 수 | 트래픽 급증 알림 리스트 |
| `save_alerts` | 알림 리스트와 파일 경로 | 저장한 알림 건수(파일에도 저장) |

- **직접 쓰는 곳은 네 함수**(번호 1 ~ 6)입니다.
  - `make_alert`(1번): 키 다섯 개를 딕셔너리로 만듭니다.
  - `make_login_alerts`(2번): 알림 한 건을 만듭니다. 반복문과 메모 문장은 미리 채웠습니다.
  - `make_traffic_alerts`(3 · 4번): 시각 값을 문자열로 바꾸고 알림 한 건을 만듭니다.
  - `save_alerts`(5 · 6번): 파일을 쓰기 위해 열고(5번), 알림 리스트를 JSON 파일에 저장합니다(6번). 저장한 건수를 세어 리턴하는 줄은 미리 채웠습니다.
  - JSON 은 문자열 · 숫자 · 리스트 · 딕셔너리를 담는 텍스트 파일 형식입니다.

## 실습 5-2 · 알림을 alerts.json 한 파일로 모으기

**이런 상황이 있습니다**

- **지금은**: 실습 4-2의 로그인 실패 결과와 실습 5-1의 트래픽 급증 결과가 형식이 달라서, 담당자가 하나씩 열어 확인해야 합니다.
- **그래서 만드는 것**: `alerts.py` 입니다.
  - 알림 한 건을 종류 · 대상 · 횟수 · 메모 · 처리 상태 키 다섯 개로 만듭니다.
  - 두 종류의 알림을 같은 모양으로 만듭니다.
  - 알림을 리스트로 모아 `alerts.json` 에 저장합니다.
- **실행하면**: 단계 1: 로그인 실패 알림 건수, 단계 2: 트래픽 급증 알림 건수, 단계 3: 저장한 건수, 단계 4: 저장된 알림이 한 건씩 나옵니다.
- **현업에서는**: 알림 형식이 같으면 규칙이 늘어도 메신저 · 티켓 · 자동 대응 도구에 같은 방법으로 보낼 수 있습니다. 담당자는 「확인 필요」인 알림부터 확인합니다.

**할 일**

1. `alerts.py` · `exercise5-2_run.py` **두 파일**을 만들고, `alerts.py` 의 **네 함수**에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>알림 건수</mark>(단계 1 ~ 3)와 <mark>저장된 알림</mark>(단계 4)을 확인하고, 새로 생긴 `alerts.json` 을 VS Code 에서 열어 봅니다.

**`alerts.py`**

```python
import json                                                                             # 알림을 JSON 파일로 쓰기 위해 json 을 불러온다

ALERTS_PATH = "alerts.json"                                                             # 알림을 모아 저장할 파일 이름


def make_alert(alert_type, target, count, note):                                        # 종류 · 대상 · 횟수 · 메모를 받는 함수
    """알림 한 건을 딕셔너리로 만든다.
    알림마다 같은 모양으로 담아 한 파일에 모을 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. 딕셔너리를 alert 에 담는다: 키 "type" 에는 alert_type, "target" 에는 target, "count" 에는 count, "note" 에는 note, "status" 에는 "확인 필요" 를 넣는다 (여러 줄로 나눠 써도 된다)
    return alert                                                                        # 알림 한 건을 리턴한다


def make_login_alerts(alert_ips):                                                       # 알림 대상 주소와 횟수를 받는 함수
    """로그인 실패 알림 대상 주소마다 「비정상 로그인」 알림을 하나씩 만든다.
    실습 4-2에서 추출한 주소를 알림 형식으로 바꿀 때 쓴다.
    """
    alerts = []                                                                         # 알림을 담을 빈 리스트
    for ip_address, count in alert_ips.items():                                         # 주소와 횟수를 한 쌍씩 꺼낸다
        note = "로그인 실패가 기준 이상 — 공격 확정이 아니라 먼저 살펴볼 곳"            # 담당자에게 보일 메모
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 2. make_alert 에 "비정상 로그인" · ip_address · count · note 를 전달해 alert 에 담는다
        alerts.append(alert)                                                            # 알림을 리스트에 추가한다
    return alerts                                                                       # 로그인 실패 알림 리스트를 리턴한다


def make_traffic_alerts(spike_minutes):                                                 # 요청이 급증한 분과 요청 수를 받는 함수
    """요청이 급증한 분마다 「트래픽 급증」 알림을 하나씩 만든다.
    실습 5-1에서 추출한 분을 알림 형식으로 바꿀 때 쓴다.
    """
    alerts = []                                                                         # 알림을 담을 빈 리스트
    for minute, count in spike_minutes.items():                                         # 분과 요청 수를 한 쌍씩 꺼낸다
        note = "요청이 평소의 3배 이상으로 늘어남 — 공격 확정이 아니라 먼저 살펴볼 곳"  # 담당자에게 보일 메모
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. str(minute) 로 시각 값을 문자열로 바꿔 target 에 담는다
        # 4. make_alert 에 "트래픽 급증" · target · count · note 를 전달해 alert 에 담는다
        alerts.append(alert)                                                            # 알림을 리스트에 추가한다
    return alerts                                                                       # 트래픽 급증 알림 리스트를 리턴한다


def save_alerts(alerts, path):                                                          # 알림 리스트와 파일 경로를 받는 함수
    """알림 리스트를 JSON 파일로 저장하고 저장한 건수를 리턴한다.
    담당자와 다른 프로그램이 같은 파일로 알림을 처리하게 할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. path 파일을 쓰기 모드("w")로 열고 file 변수로 쓴다 (with open(path, "w", encoding="utf-8") as file:)
    # 6. json.dump 에 alerts, file 을 이 순서로 전달하고, 뒤에 ensure_ascii=False, indent=2 를 붙여 쓴다 (한글은 그대로, 줄을 나눠 저장)
    saved_count = len(alerts)                                                           # 저장한 알림이 몇 건인지 센다
    return saved_count                                                                  # 저장한 건수를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1번은 함수 안이라 앞에 공백 4개이고, 2 ~ 4번은 `for` 안이라 8개이며, 5번은 함수 안이라 4개, 6번은 `with` 안이라 8개입니다.
- 번호 주석이 연달아 붙어 있어도(예: 3 · 4번), <mark>주석 사이마다 줄을 끼워 넣어 각 주석 바로 아래 줄에 그 번호의 코드를 하나씩 씁니다.</mark>
- 채우기 전에 실행하면 `NameError: name 'alert' is not defined` 오류가 납니다. 2번을 아직 안 써서 `alert` 가 만들어지지 않았기 때문입니다.

**`exercise5-2_run.py`** — **그대로 붙여 넣습니다.** 직접 쓰는 줄은 없습니다. Unit 4의 `login_detection.py` 와 실습 5-1의 `traffic_detection.py` 에 있는 함수를 불러와 알림을 만듭니다. `load_events` 는 두 파일에 같은 이름으로 있어서, <mark>여기서는 `login_detection.py` 의 것 하나만 불러옵니다.</mark>

```python
import json                                                                          # 저장한 파일을 다시 읽기 위해 json 을 불러온다
from login_detection import load_events, pick_login_failures, count_by_ip, pick_alert_ips, EVENTS_PATH, LOGIN_LIMIT  # 실습 4-2에서 만든 함수를 불러온다
from traffic_detection import add_minute_column, count_web_per_minute, make_traffic_limit, pick_spike_minutes, TRAFFIC_PATH, SPIKE_MULTIPLE  # 실습 5-1에서 만든 함수를 불러온다
from alerts import make_login_alerts, make_traffic_alerts, save_alerts, ALERTS_PATH  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)                                                    # 이벤트 파일을 표로 읽는다
login_failures = pick_login_failures(events)                                         # 로그인 실패 이벤트만 골라낸다
ip_login_fail_counts = count_by_ip(login_failures)                                   # 주소별로 실패 횟수를 센다
alert_ips = pick_alert_ips(ip_login_fail_counts, LOGIN_LIMIT)                        # 알림 기준 이상인 주소만 고른다
login_alerts = make_login_alerts(alert_ips)                                          # 주소마다 알림 한 건을 만든다
login_alert_count = len(login_alerts)                                                # 로그인 실패 알림이 몇 건인지 센다
print("--- 단계 1: 로그인 실패 알림", login_alert_count, "건")                       # 단계 1 시작을 알리는 줄과 건수

events = add_minute_column(events)                                                   # 시각에서 초를 버린 minute 열을 붙인다
minute_request_counts = count_web_per_minute(events)                                 # 웹 서버 요청을 분마다 센다
limit = make_traffic_limit(TRAFFIC_PATH, SPIKE_MULTIPLE)                             # 급증 기준을 정한다
spike_minutes = pick_spike_minutes(minute_request_counts, limit)                     # 요청이 급증한 분만 고른다
traffic_alerts = make_traffic_alerts(spike_minutes)                                  # 분마다 알림 한 건을 만든다
traffic_alert_count = len(traffic_alerts)                                            # 트래픽 급증 알림이 몇 건인지 센다
print("--- 단계 2: 트래픽 급증 알림", traffic_alert_count, "건")                     # 단계 2 시작을 알리는 줄과 건수

all_alerts = login_alerts + traffic_alerts                                           # 두 리스트를 이어 붙여 알림 하나의 리스트로 모은다
saved_count = save_alerts(all_alerts, ALERTS_PATH)                                   # 모은 알림을 파일에 저장하고 저장한 건수를 받는다
print("--- 단계 3:", ALERTS_PATH, "에 알림", saved_count, "건 저장")                 # 단계 3 시작을 알리는 줄과 건수

with open(ALERTS_PATH, encoding="utf-8") as file:                                    # 저장한 파일을 읽기 모드로 연다
    saved_alerts = json.load(file)                                                   # JSON 을 파이썬 리스트로 읽는다
print("--- 단계 4: 저장된 알림")                                                     # 단계 4 시작을 알리는 줄
for alert in saved_alerts:                                                           # 알림을 하나씩 꺼낸다
    print(alert)                                                                     # 알림 한 건을 출력한다
```

**순서**

1. **[VS Code]** 파일 `alerts.py` · `exercise5-2_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `alerts.py` 에서 직접 쓰는 곳 **여섯 군데**를 씁니다. 위 알림 한 건의 모양 표와 판다스 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise5-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise5-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. `--- 단계` 제목 줄은 세지 않고, 단계 1 ~ 3은 제목 줄에 숫자가 함께 나오고, 단계 4는 알림 한 건이 한 줄씩 2줄입니다.
5. **[VS Code]** 새로 생긴 `alerts.json` 을 열어 <mark>알림 두 건이 보이는지</mark> 확인합니다.
6. **[보고서]** `report_u5.md` 의 `## 실습 5-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, `alerts.json` 의 내용도 붙여 넣은 뒤 알림이 모두 몇 건인지 적어 주세요.
   - (나) [핵심 질문] ① 203.0.113.50 이 `normalized_events.json` 의 `source` 가 `web` 인 줄에 몇 시에 나오는지 찾아 주세요. ② 그 시각이 급증 알림의 분(09:12)과 같은지 비교해 주세요. ③ 두 알림이 같은 일과 관련이 있는지 적고, 담당자가 두 건을 한 건으로 합쳐 조사할지 따로 조사할지 고른 이유도 적어 주세요.
   - (다) [핵심 질문] 203.0.113.50 알림을 조사해 보니 직원이 비밀번호를 잊어 반복해서 입력한 것이었습니다. ① `status` 를 어떤 값으로 바꿀지(이 Unit 실습 5-2 레슨 2.1 의 처리 상태 순서를 참고), ② `note` 에 무엇을 더 적을지, ③ 알림을 지우지 않고 남겨 두는 편이 좋은 이유를 적어 주세요. 코드는 고치지 않고 글로만 적습니다.

## 실습 5-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 알림 한 건 | `alert = {"type": alert_type, "target": target, "count": count, "note": note, "status": "확인 필요"}` |
| 센 결과를 한 쌍씩 | `for ip_address, count in alert_ips.items():` (미리 채움) |
| 시각 값을 문자열로 | `target = str(minute)` |
| 파일에 저장 | `with open(path, "w", encoding="utf-8") as file:` → `json.dump(alerts, file, ensure_ascii=False, indent=2)` |

---

## 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기

문제가 아니라 이번 Unit에서 한 일을 저장소에 올리는 마무리입니다. 실습 5-2 마지막 약 10분에 합니다. 어느 터미널을 써도 되고, `pwd` 로 위치를 먼저 확인한 뒤 <mark>결과가 `anomaly_detection` 으로 끝나면 아래 1번의 `cd ..` 를 칩니다.</mark>

**이런 상황이 있습니다**

- **지금은**: 팀장이 「이번 Unit에서 만든 탐지 코드와 알림 파일을 저장소에 남겨 달라」고 합니다.
- **그래서 하는 것**: `git status` 로 올라갈 파일을 확인한 뒤<mark>(`.env` 같은 비밀 키 파일이 섞이면 안 됩니다)</mark> `git add` → `git commit` → `git push` 순서로 올립니다.
- **끝나면**: 깃허브 저장소의 `anomaly_detection` 폴더에 Unit 4와 Unit 5에서 만든 파일이 보입니다.

**순서**

0. **[터미널]** 이번 Unit에서 만든 파일이 있는지 `anomaly_detection` 폴더에서 확인합니다. `report_u5.md` 의 실습 5-2 칸에서 <mark>`답:` 뒤와 코드 상자가 비어 있는 질문이 없는지도 봅니다</mark>(마무리 (가)는 3번에서 채웁니다).
   ```bash
   pwd
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
   - <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나야 합니다.</mark> 파일은 `baseline.py` · `login_detection.py` · `classify.py` · `traffic_detection.py` · `alerts.py` · `exercise4-1_run.py` ~ `exercise5-2_run.py` 다섯 개 · `normalized_events.json` · `baseline_logins.csv` · `baseline_traffic.csv` · `alerts.json` 과 `report_u4.md` · `report_u5.md` 가 보여야 합니다. `__pycache__` 폴더는 파이썬이 만든 임시 폴더라 있어도 됩니다.
   - 빠진 파일이 있으면 그 문제를 다시 풀어 만듭니다.
   - `pwd` 가 `security-agent-toolkit` 으로 끝나면 `cd anomaly_detection` 을 먼저 칩니다.
1. **[터미널]** `security-agent-toolkit` 폴더로 옮기고 위치를 확인합니다. <mark>결과가 `…/security-agent-toolkit` 으로 끝나야 합니다.</mark>
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 있는 폴더의 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark>빨간 글씨 줄에 `.env` 나 `.venv` 가 보이면 올리지 말고,</mark> 아래 안내대로 `.gitignore` 를 고친 뒤 `git status` 를 다시 봅니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `anomaly_detection/__pycache__/` (파이썬이 실행하면서 자동으로 만드는 임시 폴더)가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
3. **[보고서]** `report_u5.md` 의 `## 마무리` 아래를 채웁니다. <mark>올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다.</mark>
   - (가) `git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.
   - 앞 실습에서 못 적은 보고서 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다. 올린 뒤에 이어서 적어 다시 올려도 됩니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add anomaly detection unit 4 and unit 5 baseline and alerts"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 대상에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - <mark>`git push` 가 거절(`rejected`)되면</mark> 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다. <mark>`git pull` 을 입력해 받아 온 뒤 `git push` 를 다시 합니다</mark>
   - `git pull` 뒤에 편집기 화면이 뜨면 <mark>`Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다</mark>
5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `anomaly_detection` 폴더를 열고, VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 있는 <mark>파일들이 깃허브에도 보이는지 확인합니다.</mark> `__pycache__` 폴더는 없어도 됩니다.
   - 빠진 이름이 있으면 VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 내 PC 에도 있는지 봅니다.
     - 없으면 다른 폴더에 만든 것이니 `anomaly_detection` 안으로 옮기고, `pwd` 로 위치를 확인한 뒤 2번의 `git status` 부터 다시 합니다.

## 마무리 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 올릴 파일 확인 | `git status` (`.env` · `.venv` 가 보이면 멈춤) |
| 올리기 | `git add .` → `git commit -m "…"` → `git push` |
| 올린 뒤 | 브라우저에서 `anomaly_detection` 폴더와 파일이 있는지 확인 |

---

## 이번 Unit 마무리

| 확인 | 문제 |
|---|---|
| 웹 서버 요청을 분마다 세고 평소 평균의 3배 이상으로 늘어난 분을 찾았다 | 실습 5-1 |
| 로그인 실패 알림과 트래픽 급증 알림을 같은 모양으로 만들어 `alerts.json` 에 모았다 | 실습 5-2 |
| 이번 Unit에서 만든 파일과 보고서를 깃허브에 올렸다 | 마무리 |

다음은 Unit 6입니다. 이번 Unit에서 만든 알림 형식에 SaaS 이상 사용과 악성 행위 징후 같은 유형을 더해 갑니다.

---

<!-- learn:answers -->
