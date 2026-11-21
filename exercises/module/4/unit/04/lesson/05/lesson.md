---
id: m4-u04-l05
title: 응용 4-1 · 로그를 한 사용자로 연결하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/108_day04_pm_correlation_risk.md
  mission_id: GichanSource.m4-1105-pm-correlation-risk
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 응용 4-1 · 로그를 한 사용자로 연결하기

## 목표: 한 사용자 기준 사건 연결

> **여유가 되면 해 보세요.** 핵심 실습 4-1 · 4-2와 글쓰기를 먼저 마칩니다. 이 응용에서는 제공 파일로 받아 쓴 `correlation.py` 를 직접 써 봅니다. 아래 골격을 붙여 넣으면 제공 파일이 덮어써져 다 채울 때까지 실습 4-1이 동작하지 않으니, 다 쓴 뒤 `exercise4-1_run.py` 를 다시 실행해 결과가 같은지 확인합니다. 하지 않아도 다음 Unit을 따라가는 데 문제가 없습니다.

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「서버 · SaaS · 웹 로그를 각각 따로 탐지했더니 결과 목록이 세 개가 됐습니다. 목록을 번갈아 보다가 같은 사람 이름이 서버 결과에도, SaaS 결과에도 나오는 것을 봤습니다. 같은 사용자가 짧은 시간 안에 여러 로그에서 이상 징후를 보였다면 하나의 사건일 수 있습니다.
>
> 같은 사용자에게 서로 다른 로그의 이벤트가 짧은 시간 안에 모여 있으면 하나의 사건으로 연결해서 알려 주세요. 웹 로그에는 사용자 이름이 없고 IP 만 있으니, SaaS 에 로그인한 기록에서 IP 로 사용자를 찾아 연결해 주세요.」
> - **왜 중요한가**: <mark>로그 하나에서는 작은 이상 징후도 같은 사용자에게 짧은 시간 안에 여러 로그에서 겹치면 먼저 확인할 이유가 분명하지만, 아침과 저녁처럼 시간이 멀리 떨어진 기록까지 한 사건으로 보면 안 됩니다.</mark>

## 왜 IP 로 사용자를 채워 연결하는가

1. 서버 로그와 SaaS 로그에는 사용자(`user`)가 있고, 웹 로그에는 IP 만 있습니다. SaaS 의 <mark>**성공한 로그인**</mark>은 IP 와 사용자가 함께 있으므로 「IP → 사용자」 딕셔너리를 만들어 웹 로그의 IP 로 사용자를 찾습니다.
2. 세 로그를 표 하나로 합쳐 **사용자 순, 같은 사용자는 시각 순**으로 놓으면 <mark>사용자별 이벤트를 시각 순서로 확인할 수 있습니다.</mark>
3. 연결됐다고 보는 조건은 둘입니다. ① 서로 다른 로그(`source`)가 2종류 이상이다. ② 그 사용자의 첫 이벤트부터 마지막 이벤트까지가 60분 이내이다. <mark>하나만 맞으면 연결된 것으로 보지 않습니다.</mark>

## 1.1 사용자 채우고 표 잇고 정렬하기

SaaS 의 성공한 로그인에서 만든 「IP → 사용자」 딕셔너리는 이렇게 생깁니다(`make_ip_user_map` 이 만들며, 미리 채워져 있습니다).

| IP | 사용자 | 만들어진 곳 |
|---|---|---|
| 198.51.100.9 | seoyeon | 09:05 성공한 로그인 |
| 192.0.2.41 | junho | 09:30 성공한 로그인 |
| 198.51.100.77 | gaeun | 10:12 성공한 로그인 |
| 198.51.100.52 | jiwoo | 16:02 성공한 로그인 |
| 203.0.113.80 | seoyeon | 17:38 성공한 로그인 |

- 딕셔너리에는 <mark>**성공한 로그인**만</mark> 넣습니다. 02:14 에 jiwoo 가 203.0.113.80 으로 시도한 로그인은 실패였으므로 넣지 않고, 같은 IP 로 성공한 17:38 의 seoyeon 이 이 IP 의 사용자로 기록됩니다.
- 서버 로그는 실패 이벤트 **전체**(9개)를 씁니다. 먼저 확인할 이벤트만 고르면 어떤 사용자가 서버 로그에 나오는지가 반복 거절 기준(Unit 3 실습 3-2의 3번)에 따라 달라지기 때문입니다.
- 웹 실패 이벤트의 IP 가 위 표에 있으면 그 사용자의 이벤트로 연결해 분석할 수 있고, <mark>딕셔너리에 IP 가 없으면 사용자를 확인할 수 없어 이번 연결에서 제외합니다.</mark>

**판다스 문법 상자 — 딕셔너리로 값을 바꾸기 `map`**

**<mark>`열.map(딕셔너리)`</mark> 은 열의 값을 딕셔너리에서 찾아, 짝지어진 값으로 바꿉니다. 딕셔너리에 없는 값은 `NaN`(연결할 값이 없다는 표시)이 됩니다**

실습 4-1 문법 상자에서 규칙 이름을 점수로 바꿀 때 쓴 `map` 입니다. 아래에서는 웹 로그의 IP 를 사용자 이름으로 바꿉니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                    # 표에 넣을 내용(열 이름: 값들)
    "ip": ["203.0.113.80", "198.51.100.77", "192.0.2.15"],  # ip 열
    "action": ["GET /admin", "GET /admin", "GET /board"],   # action 열
}
df = pd.DataFrame(data)                                     # 내용으로 표(DataFrame)를 만든다
print(df)                                                   # 표를 출력한다
```

실행 결과:

```
              ip      action
0   203.0.113.80  GET /admin
1  198.51.100.77  GET /admin
2     192.0.2.15  GET /board
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
ip_user = {"203.0.113.80": "seoyeon", "198.51.100.77": "gaeun"}  # IP → 사용자 딕셔너리(세 번째 IP 는 없다)
users = df["ip"].map(ip_user)                                    # ip 열의 각 값을 딕셔너리에서 찾아 사용자 이름으로 바꾼다
print(users)                                                     # 바뀐 값을 출력한다
```

실행 결과:

```
0    seoyeon
1      gaeun
2        NaN
Name: ip, dtype: object
```

- 읽는 법: <mark style="background:#bde3ff">앞의 두 IP 는 딕셔너리에 있어서 `seoyeon` 과 `gaeun` 이 되고, 세 번째 IP 는 딕셔너리에 없어서 `NaN`</mark> 입니다. 맨 아래 `Name: ip, dtype: object` 줄은 몰라도 됩니다(판다스 3 이상에서는 `dtype: str` 로 나옵니다).

**판다스 문법 상자 — 표를 위아래로 이어 붙이기 `pd.concat`**

**<mark>`pd.concat([표1, 표2, …])`</mark> 는 열 이름이 같은 표 여러 개를 위아래로 이어 붙여 표 하나로 만듭니다. 표는 대괄호 `[ ]` 안의 리스트로 전달합니다**

아래에서는 판정 서버 로그 표와 SaaS 로그 표를 하나로 이어 붙입니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

server_data = {                                      # 판정 서버 로그에 넣을 내용
    "user": ["gaeun", "gaeun"],                      # user 열
    "action": ["ACCOUNT:CHANGE", "ACCOUNT:CHANGE"],  # action 열
}
server_logs = pd.DataFrame(server_data)              # 내용으로 표(DataFrame)를 만든다
print(server_logs)                                   # 판정 서버 표를 출력한다
```

실행 결과:

```
    user          action
0  gaeun  ACCOUNT:CHANGE
1  gaeun  ACCOUNT:CHANGE
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
saas_data = {                        # SaaS 로그에 넣을 내용 — 열 이름이 서버 표와 같다
    "user": ["gaeun"],               # user 열
    "action": ["login"],             # action 열
}
saas_logs = pd.DataFrame(saas_data)  # 내용으로 표(DataFrame)를 만든다
print(saas_logs)                     # SaaS 표를 출력한다
```

실행 결과:

```
    user action
0  gaeun  login
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
both = pd.concat([server_logs, saas_logs])  # 표 두 개를 위아래로 이어 붙여 표 하나로 만든다
print(both)                                 # 이어 붙인 표를 출력한다
```

실행 결과:

```
    user          action
0  gaeun  ACCOUNT:CHANGE
1  gaeun  ACCOUNT:CHANGE
0  gaeun           login
```

- 읽는 법: <mark style="background:#bde3ff">판정 서버 2행 아래에 SaaS 1행이 붙어 3행이 되었습니다.</mark> 왼쪽 번호는 원래 표의 번호를 그대로 가져와서 0 이 두 번 나옵니다.
- <mark>표를 대괄호 안에 넣지 않고 쉼표로 따로 전달하면 오류가 납니다.</mark>

**판다스 문법 상자 — 열 두 개로 정렬하기 `sort_values([열1, 열2])`**

**<mark>`표.sort_values(["열1", "열2"])`</mark> 는 열1 순으로 정렬하고, 열1 의 값이 같은 행은 열2 순으로 정렬합니다. 열 이름은 리스트로 전달합니다**

아래는 사용자 순서가 섞여 있는 로그입니다. 사용자(`user`) 순으로 먼저 정렬하고, 같은 사용자 안에서는 시각(`time`) 순으로 정렬합니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                               # 표에 넣을 내용(열 이름: 값들)
    "user": ["seoyeon", "gaeun", "seoyeon", "gaeun"],  # user 열
    "time": ["17:38", "10:14", "09:05", "10:05"],      # time 열
}
df = pd.DataFrame(data)                                # 내용으로 표(DataFrame)를 만든다
print(df)                                              # 표를 출력한다
```

실행 결과:

```
      user   time
0  seoyeon  17:38
1    gaeun  10:14
2  seoyeon  09:05
3    gaeun  10:05
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
sorted_df = df.sort_values(["user", "time"])  # user 순으로, 같은 user 는 time 순으로 정렬한다
print(sorted_df)                              # 정렬한 표를 출력한다
```

실행 결과:

```
      user   time
3    gaeun  10:05
1    gaeun  10:14
2  seoyeon  09:05
0  seoyeon  17:38
```

- 읽는 법: <mark style="background:#bde3ff">먼저 `user` 순(gaeun → seoyeon)으로 놓이고, 같은 사용자 안에서는 `time` 순(10:05 → 10:14, 09:05 → 17:38)으로 놓였습니다.</mark> 왼쪽 번호는 원래 행의 번호라서 바뀐 순서로 나옵니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `make_ip_user_map` | SaaS 로그인 표 | IP → 사용자 딕셔너리(미리 채움) |
| `attach_user_to_web` | 웹 실패 표 · 딕셔너리 | `user` 열이 붙은 웹 이벤트 표 |
| `build_timeline` | 서버 · SaaS · 웹 표 | 사용자 · 시각 순으로 정렬된 표 |
| `find_chains` | 정렬된 표 | 연결된 사건 리스트와 연결되지 않은 사용자 |
| `find_chains_in_events` | 이벤트 표 | 연결된 사건 리스트(미리 채움, 실습 4-1에서 씀) |

미리 채운 줄 가운데 처음 보는 것은 이렇습니다.

| 미리 채운 줄 | 하는 일 |
|---|---|
| `hours * 60 + minutes` | 시각을 「자정부터 몇 분이 지났는지」로 바꿉니다(09:33 → 573) |
| `times.dt.minute` | 시각 값에서 분(0~59)만 꺼냅니다(제공 파일 `saas_detection.py` 의 `.dt.hour` 와 같은 모양) |
| `latest - earliest` | 사용자별로 가장 늦은 시각(분)에서 가장 이른 시각(분)을 뺍니다 |
| `source_counts.index` | 사용자 이름들 |
| `source_counts[user]` | 그 사용자의 값 |
| `.copy()` | 원본 표를 바꾸지 않도록 복사본을 만듭니다 |
| `grouped["source"].nunique()` | 사용자별로 `source` 값이 몇 종류인지 셉니다 |

- `latest - earliest` 로 나온 첫 이벤트와 마지막 이벤트의 시간 차(분)를 60분 기준과 비교합니다. 분 단위로 계산하므로 초는 버립니다.
- `nunique` 줄은 왼쪽부터 ① `grouped["source"]` 가 `source` 열을 고르고 ② `.nunique()` 가 서로 다른 값의 수를 셉니다.

**직접 쓰는 곳은 다섯 군데**(번호 1 ~ 5)이고, 함수 세 개 안에 나뉘어 있습니다.

| 함수 | 번호 | 직접 쓰는 일 |
|---|---|---|
| `attach_user_to_web` | 1번 | IP 마다 사용자를 `map` 으로 채웁니다 |
| `build_timeline` | 2 · 3번 | 세 표를 연결하고 사용자 · 시각 순으로 정렬합니다 |
| `find_chains` | 4 · 5번 | `if` 안에서 이유 문장을 만들어 사건 리스트에 추가합니다 |

- `find_chains` 에서 연결 조건을 확인하는 `if` 줄은 미리 채웠습니다.

## 응용 4-1 · 로그를 한 사용자로 연결하기

**이런 상황이 있습니다**

- **지금은**: <mark>서버 · SaaS · 웹 로그의 탐지 결과가 따로 있어서, 같은 사용자의 기록이 로그별로 나뉘어 있습니다</mark>.
- **그래서 만드는 것**: `correlation.py` 입니다.
  - 웹 이벤트에 IP 로 사용자를 채웁니다.
  - 세 로그를 한 표로 합쳐 사용자 · 시각 순으로 정렬합니다.
  - 서로 다른 로그가 2종류 이상이고 첫 이벤트부터 마지막 이벤트까지 60분 이내인 사용자를 하나의 사건으로 연결합니다.
- **실행하면**: <mark>단계 1: 사용자를 알 수 있는 웹 이벤트 수, 단계 2: 합친 이벤트 수와 한 사용자의 흐름, 단계 3: 연결된 사건, 단계 4: 로그가 2종류 이상이지만 시간 차가 60분을 넘어 연결되지 않은 사용자가 나옵니다.</mark>
- **현업에서는**: 이벤트 하나씩이 아니라 한 사용자 단위의 사건으로 연결하면 담당자가 읽을 양이 줄어듭니다. 시간 기준 밖에 있는 이벤트는 따로 두어 관계없는 일이 섞이지 않게 합니다.

**할 일**

1. `correlation.py` · `apply4-1_run.py` 두 파일을 만들고, `correlation.py` 의 세 함수에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>사용자를 알 수 있는 웹 이벤트 수</mark>(단계 1), <mark>합친 이벤트 수와 한 사용자의 흐름</mark>(단계 2), <mark>연결된 사건</mark>(단계 3), <mark>연결되지 않은 사용자</mark>(단계 4)를 읽습니다.

**`correlation.py`**

```python
import pandas as pd                                    # 판다스를 pd 라는 짧은 이름으로 불러온다
from access_detection import load_events, pick_server_failures, EVENTS_PATH  # 실습 3-2 함수를 불러온다
from saas_detection import pick_saas, pick_logins      # saas_detection.py 의 함수를 불러온다
from malicious_detection import pick_web_failures      # malicious_detection.py 의 함수를 불러온다

MIN_SOURCES = 2                                        # 서로 다른 로그(source)가 이 개수 이상이면 연결된 것으로 본다
WINDOW_MINUTES = 60                                    # 한 사용자의 이벤트가 이 분 안에 모여 있어야 연결된 것으로 본다


def make_ip_user_map(logins):                          # SaaS 로그인 표를 받는 함수
    """성공한 SaaS 로그인에서 IP 마다 사용자를 찾아 딕셔너리로 만든다.
    웹 서버 로그에는 사용자가 없어서 IP 로 사용자를 찾을 때 쓴다.
    """
    ip_user = {}                                       # IP → 사용자 딕셔너리
    login_list = logins.to_dict("records")             # 표를 이벤트 딕셔너리 리스트로 바꾼다
    for login in login_list:                           # 로그인을 하나씩 꺼낸다
        if login["result"] == "성공":                  # 성공한 로그인이면
            ip_user[login["ip"]] = login["user"]       # 그 IP 의 사용자를 딕셔너리에 담는다
    return ip_user                                     # IP → 사용자 딕셔너리를 리턴한다


def attach_user_to_web(web_failures, ip_user):         # 웹 실패 표와 IP → 사용자 딕셔너리를 받는 함수
    """IP 로 사용자를 알 수 있는 웹 실패 이벤트에 user 열을 붙인다.
    웹 로그를 서버 · SaaS 로그와 같은 사용자 기준으로 연결해 분석할 때 쓴다.
    """
    ips = web_failures["ip"]                           # ip 열만 꺼낸다
    known_ips = list(ip_user)                          # 딕셔너리의 키(IP)만 리스트로 만든다
    is_known = ips.isin(known_ips)                     # 행마다 사용자를 아는 IP 인지 구해 True 또는 False 를 만든다
    known_web = web_failures[is_known]                 # True 인 행만 골라 새 표를 만든다
    web_part = known_web.copy()                        # 원본을 바꾸지 않도록 복사한다 — 미리 채운 줄

    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. web_part 의 "ip" 열을 꺼내 .map(ip_user) 를 붙여 IP 마다 사용자를 구해 users 에 담는다
    web_part["user"] = users                           # 표에 user 열을 붙인다 — 미리 채운 줄
    return web_part                                    # user 열이 붙은 웹 이벤트 표를 리턴한다


def build_timeline(server_part, saas_part, web_part):  # 세 로그의 표를 받는 함수
    """세 로그의 표를 하나로 합쳐 사용자 · 시각 순으로 정렬하고, 하루 중 몇 분인지 열을 붙인다.
    사용자마다 서로 다른 로그의 이벤트를 시간순으로 놓고 볼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. pd.concat 에 [server_part, saas_part, web_part] 리스트를 전달해 timeline 에 담는다
    # 3. timeline 에 .sort_values 를 붙이고 ["user", "time"] 리스트를 전달해 사용자 순, 같은 사용자는 시각 순으로 정렬한 결과를 timeline 에 담는다
    times = pd.to_datetime(timeline["time"])           # 문자열 시각을 시각 값으로 바꾼다
    hours = times.dt.hour                              # 시각 값에서 시(0~23)만 꺼낸다
    minutes = times.dt.minute                          # 시각 값에서 분(0~59)만 꺼낸다
    timeline["minute_of_day"] = hours * 60 + minutes   # 자정부터 몇 분이 지났는지 열을 붙인다 — 미리 채운 줄
    return timeline                                    # 정렬된 이벤트 표를 리턴한다


def find_chains(timeline):                             # 정렬된 이벤트 표를 받는 함수
    """서로 다른 로그가 짧은 시간 안에 한 사용자에게 모여 있는 사건을 찾는다.
    이벤트 하나씩이 아니라 한 사용자의 사건으로 연결해 분석할 때 쓴다.
    """
    grouped = timeline.groupby("user")                 # user 가 같은 행끼리 그룹으로 만든다
    source_counts = grouped["source"].nunique()        # 그룹마다 서로 다른 로그(source)가 몇 종류인지 센다
    latest = grouped["minute_of_day"].max()            # 그룹마다 가장 늦은 시각(분)을 구한다
    earliest = grouped["minute_of_day"].min()          # 그룹마다 가장 이른 시각(분)을 구한다
    spans = latest - earliest                          # 그룹마다 처음부터 마지막까지 몇 분인지 구한다

    chains = []                                        # 연결된 사건을 담을 빈 리스트
    not_chained = []                                   # 로그 종류는 여럿이지만 시간 차가 60분을 초과해 연결되지 않은 사용자 정보
    for user in source_counts.index:                   # 사용자를 하나씩 꺼낸다
        source_count = source_counts[user]             # 그 사용자의 로그 종류 수
        span = spans[user]                             # 그 사용자의 처음부터 마지막까지 분
        has_many_sources = source_count >= MIN_SOURCES  # 로그 종류가 기준 이상인지 구한다
        is_close = span <= WINDOW_MINUTES              # 시간 간격이 기준 이내인지 구한다
        if has_many_sources and is_close:              # 로그 종류도 충분하고 60분 이내이면 — 미리 채운 줄
            # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
            # 4. "서로 다른 로그 " 와 str(source_count) 와 "종류 · " 와 str(span) 과 "분 안" 을 + 로 연결해 reason 에 담는다
            # 5. chains 에 키 "user" 에 user, 키 "reason" 에 reason 을 담은 딕셔너리를 추가한다
        if has_many_sources and not is_close:          # 로그 종류는 여럿인데 시간 차가 60분을 초과하면 — 미리 채운 줄
            not_chained.append({"user": user, "source_count": int(source_count), "span_minutes": int(span)})  # 연결되지 않은 사용자와 두 숫자를 추가한다
    return chains, not_chained                         # 연결된 사건과 연결되지 않은 사용자를 리턴한다


def find_chains_in_events(events):                     # 이벤트 표를 받는 함수
    """이벤트 표 하나로 위 함수를 차례로 불러 연결된 사건 리스트를 만든다.
    실습 4-1에서 점수를 매기기 전에 한 번에 쓴다.
    """
    server_failures = pick_server_failures(events)     # 판정 서버 실패 이벤트를 고른다
    server_part = server_failures                      # 서버 실패 이벤트 전체를 쓴다
    saas_part = pick_saas(events)                      # SaaS 이벤트를 고른다
    logins = pick_logins(saas_part)                    # 로그인 이벤트를 고른다
    ip_user = make_ip_user_map(logins)                 # IP → 사용자 딕셔너리를 만든다
    web_failures = pick_web_failures(events)           # 웹 실패 이벤트를 고른다
    web_part = attach_user_to_web(web_failures, ip_user)  # 사용자를 아는 웹 이벤트에 user 열을 붙인다
    timeline = build_timeline(server_part, saas_part, web_part)  # 세 로그를 합쳐 정렬한다
    chains, not_chained = find_chains(timeline)        # 연결된 사건을 찾는다
    return chains                                      # 연결된 사건 리스트를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 3번은 함수 안이라 앞에 공백 4개이고, 4 · 5번은 `for` 와 `if` 안이라 12개입니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.**
- 정렬은 새 표를 만들어 주므로 3번은 <mark>`timeline = timeline.sort_values(…)` 로 다시 담아야</mark> 합니다. `timeline.sort_values(…)` 만 쓰면 정렬한 결과가 사라집니다.
- 4번의 완성 모양은 `서로 다른 로그 2종류 · 30분 안` 입니다(숫자는 사용자마다 다릅니다). <mark>공백 하나까지 같아야 출력이 같습니다.</mark>
- 채우기 전에 실행하면 `IndentationError: expected an indented block` 오류가 납니다. `if` 안쪽의 4 · 5번이 비어 있기 때문입니다.

**`apply4-1_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다.

```python
from access_detection import load_events, pick_server_failures, EVENTS_PATH  # 실습 3-2 함수를 불러온다
from saas_detection import pick_saas, pick_logins      # saas_detection.py 의 함수를 불러온다
from malicious_detection import pick_web_failures      # malicious_detection.py 의 함수를 불러온다
from correlation import make_ip_user_map, attach_user_to_web, build_timeline, find_chains, WINDOW_MINUTES  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)                      # 이벤트 파일을 표로 읽는다
server_failures = pick_server_failures(events)         # 판정 서버 실패 이벤트를 고른다
server_part = server_failures                           # 서버 실패 이벤트 전체를 쓴다
saas_part = pick_saas(events)                          # SaaS 이벤트를 고른다
logins = pick_logins(saas_part)                        # 로그인 이벤트를 고른다
ip_user = make_ip_user_map(logins)                     # 성공한 로그인에서 IP → 사용자 딕셔너리를 만든다

web_failures = pick_web_failures(events)               # 웹 실패 이벤트를 고른다
web_part = attach_user_to_web(web_failures, ip_user)   # 사용자를 아는 웹 이벤트에 user 열을 붙인다
web_count = len(web_part)                              # 그 이벤트가 몇 개인지 센다
print("--- 단계 1: IP 로 사용자를 알 수 있는 웹 실패 이벤트", web_count, "개")  # 단계 1 시작을 알리는 줄과 개수

timeline = build_timeline(server_part, saas_part, web_part)  # 세 로그를 합쳐 사용자 · 시각 순으로 정렬한다
timeline_count = len(timeline)                         # 합친 이벤트가 몇 개인지 센다
print("--- 단계 2: 사용자별로 시간순으로 놓은 이벤트", timeline_count, "개")  # 단계 2 시작을 알리는 줄과 개수
print("gaeun 의 이벤트 (시각 · 로그 · 행동 · 결과)")  # 아래 줄들이 gaeun 의 이벤트라는 것을 알리는 줄

users = timeline["user"]                               # user 열만 꺼낸다
is_gaeun = users == "gaeun"                            # 행마다 gaeun 인지 비교해 True 또는 False 를 만든다
gaeun_rows = timeline[is_gaeun]                        # True 인 행만 골라 gaeun 의 이벤트 표를 만든다
gaeun_list = gaeun_rows.to_dict("records")             # 표를 이벤트 딕셔너리 리스트로 바꾼다
for event in gaeun_list:                               # gaeun 의 이벤트를 시간순으로 하나씩 꺼낸다
    print(event["time"], event["source"], event["action"], event["result"])  # 시각 · 로그 · 행동 · 결과를 출력한다

chains, not_chained = find_chains(timeline)            # 연결된 사건과 연결되지 않은 사용자를 찾는다
print("--- 단계 3:", WINDOW_MINUTES, "분 안에 서로 다른 로그로 연결된 사건")  # 단계 3 시작을 알리는 줄
for chain in chains:                                   # 연결된 사건을 하나씩 꺼낸다
    print(chain)                                       # 사건을 출력한다

print("--- 단계 4: 로그 종류는 여럿이지만 시간 차가 60분을 초과해 연결되지 않은 사용자")  # 단계 4 시작을 알리는 줄
for item in not_chained:                               # 연결되지 않은 사용자를 하나씩 꺼낸다
    print(item)                                        # 사용자 · 로그 종류 수 · 첫 이벤트부터 마지막 이벤트까지의 분을 출력한다
```

**순서**

1. **[VS Code]** 파일 `correlation.py` · `apply4-1_run.py` 를 `anomaly_detection` 폴더에 만들어 위 코드를 붙여 넣습니다. `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 로 만듭니다.
2. **[VS Code]** `correlation.py` 에서 <mark>직접 쓰는 곳 다섯 군데를 씁니다</mark>. 1.1 의 문법 상자를 보고 쓰고, 막히면 아래 「응용 4-1 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python apply4-1_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python apply4-1_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1은 숫자가 제목 줄에 함께 나오므로 그 아래 줄이 없고, 단계 2는 제목 아래 6줄(`gaeun 의 이벤트 …` 안내 줄 1줄과 gaeun 의 이벤트 5줄), 단계 3은 1줄, 단계 4는 제목 아래 1줄입니다.
5. **[보고서]** `report_u4.md` 의 `## 응용 4-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 연결된 사건의 사용자와 이유를 적어 주세요.
   - (나) [핵심 질문] 단계 2에 나온 gaeun 의 이벤트 5개는 어느 로그(`source`)에서 왔고, 왜 한 사건으로 연결됐나요? 이 사건만으로 공격이라고 확정할 수 있는지도 적어 주세요.
   - (다) [핵심 질문] seoyeon 은 서로 다른 로그에 나오지만 연결되지 않았습니다. 단계 4 의 두 숫자(로그 종류 수와 처음부터 마지막까지의 분)로 두 조건을 비교해 연결되지 않은 이유를 설명하고, 하나의 사건으로 연결하지 않아서 탐지하지 못할 수 있는 것을 실습 4-1 출력의 seoyeon 이유(규칙)와 연결해 적어 주세요.

## 응용 4-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| IP 로 사용자 채우기 | `users = web_part["ip"].map(ip_user)` |
| 표 위아래로 잇기 | `timeline = pd.concat([server_part, saas_part, web_part])` |
| 열 두 개로 정렬 | `timeline = timeline.sort_values(["user", "time"])` |
| 이유 문장 만들기 | `reason = "서로 다른 로그 " + str(source_count) + "종류 · " + str(span) + "분 안"` |

---
