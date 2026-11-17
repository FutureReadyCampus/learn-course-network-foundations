---
id: m4-u06-l03
title: Exercise 6-2 · SaaS 이상 사용 세 가지 찾기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/106_day04_am_suspicious_logs.md
  mission_id: GichanSource.m4-1105-am-suspicious-logs
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 6-2 · SaaS 이상 사용 세 가지 찾기

## 이번 의뢰: SaaS 이상 사용 찾기

> **이번 Exercise에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「우리 회사는 파일 보관 서비스(SaaS)를 씁니다. 이 서비스는 회사 밖 어디서나 로그인할 수 있습니다. 11/2 에는 02:14 에 새벽 로그인 시도가 있었고, 17:38 에는 seoyeon 이 평소와 다른 IP 로 로그인한 뒤 파일을 5번 연속으로 내려받았습니다.
>
> 다음 세 가지를 각각 찾아서 어느 사용자가 해당하는지 알려 주세요. ① 업무 시간 밖 로그인 ② 평소와 다른 IP 로 로그인 ③ 파일 5번 이상 내려받기. 평소 기록이 없는 사용자는 IP 를 비교할 수 없으니 IP 확인에서는 빼 주세요.」
> - **왜 중요한가**: <mark>SaaS 는 회사 밖에서도 로그인할 수 있어서 로그인에 성공했다는 것만으로는 본인인지 알 수 없고, 세 규칙을 따로 확인하면 담당자가 확인할 대상을 구분할 수 있습니다.</mark>

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「문제」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다. (판다스 문법 상자의 코드는 눈으로 읽으면 됩니다.)

## 읽기 · 왜 규칙 세 개를 따로 찾는가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. Unit 4의 Exercise 4-1에서 **평소 기준**을 정했습니다. 이번 Exercise에서는 사용자마다 평소가 다르므로 **사용자별 평소 IP** 를 딕셔너리로 둡니다.
2. SaaS 이상 사용을 보는 규칙은 세 가지이고, <mark>세 규칙은 각각 따로 찾습니다.</mark>
   - **업무 시간 밖 로그인**: 로그인한 시각의 시(hour)가 8 보다 작거나 20 보다 큰 로그인 시도입니다(오전 8시 전, 오후 9시 이후). 20시대(20:00 ~ 20:59)는 업무 시간 안입니다.
   - **평소와 다른 IP**: 사용자의 평소 IP 와 다른 IP 로 로그인했습니다.
   - **대량 다운로드**: 파일을 5번 이상 내려받았습니다(이 규칙은 미리 채워져 있습니다).
3. 평소 IP 기록이 없는 사용자(`gaeun`)는 <mark>비교할 기준이 없으므로 「평소와 다른 IP」 규칙에서만 뺍니다.</mark> 다른 두 규칙에는 그대로 포함합니다.

## 읽기 · 2.1 SaaS 로그와 세 규칙

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

샘플에서 `source` 가 `saas` 인 이벤트 14개입니다.

| 시각 | 사용자 | IP | 행동 | 결과 | 해당하는 규칙 |
|---|---|---|---|---|---|
| 02:14 | jiwoo | 203.0.113.80 | `login` | 실패 | 업무 시간 밖 · 평소와 다른 IP |
| 09:05 | seoyeon | 198.51.100.9 | `login` | 성공 | 해당 없음 |
| 09:30 | junho | 192.0.2.41 | `login` | 성공 | 해당 없음 |
| 10:12 | gaeun | 198.51.100.77 | `login` | 성공 | 평소 기록이 없어 IP 규칙에서 제외 |
| 11:25 | seoyeon | 198.51.100.9 | `file.download` | 성공 | 다운로드 1번 |
| 13:50 | junho | 192.0.2.41 | `file.upload` | 성공 | 해당 없음 |
| 15:20 | junho | 192.0.2.41 | `login` | 성공 | 해당 없음 |
| 16:02 | jiwoo | 198.51.100.52 | `login` | 성공 | 해당 없음 |
| 17:38 | seoyeon | 203.0.113.80 | `login` | 성공 | 평소와 다른 IP |
| 17:40 ~ 17:42 | seoyeon | 203.0.113.80 | `file.download` 5번 | 성공 | 다운로드 합계 6번(대량) |

- 파일 내려받기는 11:25 에 1번, 17:40 ~ 17:42 에 5번이라 합계 6번입니다. 팀장 메시지의 「5번 연속」은 17:40 ~ 17:42 에 기록된 다운로드 5건을 말합니다.
- `USUAL_IPS` 에 평소 IP 를 둔 사용자는 3명(seoyeon · junho · jiwoo)입니다.
- <mark>규칙에 해당한다고 계정이 도용됐다는 뜻은 아니고,</mark> **먼저 확인할 대상**이라는 뜻입니다.

**알아 둘 것 — 미리 채운 줄의 `pd.to_datetime` 과 `.dt.hour`**

`pd.to_datetime(열)` 로 문자열 시각을 시각 값으로 바꾼 뒤 `.dt.hour` 를 붙이면 시(0 ~ 23)만 숫자로 꺼냅니다(예: 21:40 의 시는 21). `.dt` 는 시각 값에만 쓸 수 있어서 문자열 시각을 먼저 바꿉니다. 문제에서는 이 두 줄이 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다. 자세한 쓰임은 다음에 차차 배웁니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                                            # 표에 넣을 내용(열 이름: 값들)
    "user": ["jiwoo", "seoyeon", "junho"],                                          # user 열
    "time": ["2026-11-02 02:14:08", "2026-11-02 09:05:30", "2026-11-02 21:40:10"],  # time 열
}
df = pd.DataFrame(data)                                                             # 내용으로 표(DataFrame)를 만든다
print(df)                                                                           # 표를 출력한다
```

실행 결과:

```
      user                 time
0    jiwoo  2026-11-02 02:14:08
1  seoyeon  2026-11-02 09:05:30
2    junho  2026-11-02 21:40:10
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
times = pd.to_datetime(df["time"])  # 문자열 시각을 시각 값으로 바꾼다
print(times)                        # 시각 값을 출력한다
```

실행 결과:

```
0   2026-11-02 02:14:08
1   2026-11-02 09:05:30
2   2026-11-02 21:40:10
Name: time, dtype: datetime64[ns]
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
hours = times.dt.hour  # 시각 값에서 시(0~23)만 꺼낸다
print(hours)           # 시를 출력한다
```

실행 결과:

```
0     2
1     9
2    21
Name: time, dtype: int32
```

- 읽는 법: 첫 번째 출력은 시각 값이 된 `time` 열이고, 두 번째 출력은 거기서 시만 꺼낸 값입니다(<mark>02:14 → 2, 09:05 → 9, 21:40 → 21</mark>).

**판다스 문법 상자 — 범위 안인지 `between`**

**<mark>`열.between(작은 값, 큰 값)`</mark> 은 열의 값이 작은 값 이상이고 큰 값 이하이면 `True`, 아니면 `False` 를 줍니다. 작은 값과 큰 값 자체도 포함합니다**

아래는 로그인한 시(`hour`, 0 ~ 23)입니다. 8시부터 20시 사이이면 업무 시간 안입니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                            # 표에 넣을 내용(열 이름: 값들)
    "user": ["gaeun", "dami", "seoyeon", "junho"],  # user 열
    "hour": [9, 2, 20, 21],                         # hour 열
}
df = pd.DataFrame(data)                             # 내용으로 표(DataFrame)를 만든다
print(df)                                           # 표를 출력한다
```

실행 결과:

```
      user  hour
0    gaeun     9
1     dami     2
2  seoyeon    20
3    junho    21
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
in_hours = df["hour"].between(8, 20)  # hour 가 8 ~ 20 사이인지 확인한다
print(in_hours)                       # True · False 를 출력한다
```

실행 결과:

```
0     True
1    False
2     True
3    False
Name: hour, dtype: bool
```

- 읽는 법: 9시와 20시는 `True`, 2시와 21시는 `False` 입니다. <mark>20시도 `True` 인 것은 8 과 20 자체도 사이에 포함하기 때문입니다.</mark>

**판다스 문법 상자 — 조건 뒤집기 `~`**

**<mark>`~조건`</mark> 은 `True` 는 `False` 로, `False` 는 `True` 로 뒤집습니다**

아래에서는 업무 시간 **밖**에 로그인한 기록을 찾습니다. 위에서 만든 「업무 시간 안인지」를 뒤집으면 됩니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                            # 표에 넣을 내용(열 이름: 값들)
    "user": ["gaeun", "dami", "seoyeon", "junho"],  # user 열
    "hour": [9, 2, 20, 21],                         # hour 열
}
df = pd.DataFrame(data)                             # 내용으로 표(DataFrame)를 만든다
in_hours = df["hour"].between(8, 20)                # hour 가 8 ~ 20 사이인지 확인한다
print(in_hours)                                     # 업무 시간 안인지 출력한다
```

실행 결과:

```
0     True
1    False
2     True
3    False
Name: hour, dtype: bool
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
off_hours = ~in_hours  # True 와 False 를 서로 뒤집는다
print(off_hours)       # 업무 시간 밖인지 출력한다
```

실행 결과:

```
0    False
1     True
2    False
3     True
Name: hour, dtype: bool
```

- 읽는 법: <mark>두 출력이 서로 반대입니다.</mark> 업무 시간 안이던 0 · 2번 행은 `False` 가 되고, 밖이던 1 · 3번 행은 `True` 가 됩니다.

**문법 상자 — 다른지 `!=` 와 값이 있는지 `is not None`**

**<mark>`a != b`</mark> 는 두 값이 다르면 `True`, 같으면 `False` 입니다. <mark>`값 is not None`</mark> 은 값이 `None`(값이 없다는 표시)이 아니면 `True` 입니다**

`==` 의 반대가 `!=` 이고, `is None`(값이 없는가)의 반대가 `is not None`(값이 있는가)입니다.

```python
usual_ip = "198.51.100.9"   # 사용자의 평소 IP
ip = "203.0.113.80"         # 이번 로그인의 IP
is_new_ip = ip != usual_ip  # 이번 IP 가 평소 IP 와 다른지 구한다 (!=)
print(is_new_ip)            # True — 서로 다르다
```

실행 결과:

```
True
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
no_record = None                    # 평소 IP 기록이 없는 사용자는 값이 None 이다
has_record = no_record is not None  # 값이 있는지(None 이 아닌지) 구한다 (is not None)
print(has_record)                   # False — 평소 기록이 없다
```

실행 결과:

```
False
```

- 읽는 법: 평소 IP 와 이번 IP 가 달라서 `True` 이고, <mark>값이 `None`(평소 기록 없음)이라 「값이 있는가」를 묻는 결과는 `False`</mark> 입니다.
- `None` 은 어떤 IP 와도 같지 않아서 `ip != None` 은 항상 `True` 입니다. <mark>그래서 평소 기록이 없는 사용자는 `is not None` 으로 먼저 제외합니다.</mark>

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_events` · `pick_saas` · `pick_logins` | 파일 경로 · 이벤트 표 | 이벤트 표 · SaaS 표 · 로그인 표(미리 채움) |
| `find_off_hours_logins` | 로그인 표 | 업무 시간 밖 로그인 표 |
| `find_new_ip_users` | 로그인 표 | 평소와 다른 IP 로 로그인한 사용자 리스트 |
| `find_bulk_download_users` | SaaS 표 | 대량 다운로드 사용자 리스트(미리 채움) |

- **직접 쓰는 곳은 다섯 군데**(번호 1 ~ 5)이고, 함수 두 개 안에 나뉘어 있습니다.
  - `find_off_hours_logins`(1 · 2번, 2곳): 시가 업무 시간 안인지 구하고 뒤집습니다. 시각을 시로 꺼내는 두 줄은 미리 채웠습니다.
  - `find_new_ip_users`(3 ~ 5번, 3곳): 평소 기록이 있는지, 평소와 다른 IP 인지 구하고, `if` 안에서 사용자를 리스트에 추가합니다. `if` 줄은 미리 채웠습니다.

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise 6-2 · SaaS 이상 사용 세 가지 찾기

**이런 상황이 있습니다**

- **지금은**: <mark>SaaS 로그 14개를 사람이 읽어서 이상 사용을 찾고 있고, 어떤 기준으로 볼지 정해져 있지 않습니다</mark>.
- **그래서 만드는 것**: `saas_detection.py` 입니다.
  - 업무 시간 밖 로그인을 찾습니다.
  - 평소와 다른 IP 로 로그인한 사용자를 찾습니다(평소 기록이 없는 사용자는 뺍니다).
  - 대량 다운로드 사용자를 찾습니다(미리 채워져 있습니다).
- **실행하면**: <mark>단계 1: 업무 시간 밖 로그인, 단계 2: 평소와 다른 IP 사용자, 단계 3: 대량 다운로드 사용자가 나옵니다.</mark>
- **현업에서는**: 규칙마다 따로 찾아 두면 Unit 7의 Exercise 7-2에서 규칙마다 점수를 줄 수 있습니다. 평소 기록이 없는 사용자는 기록이 쌓인 뒤에 규칙을 적용합니다.

**할 일**

1. `saas_detection.py` · `exercise6-2_run.py` 두 파일을 만들고, `saas_detection.py` 의 두 함수에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>업무 시간 밖 로그인</mark>(단계 1), <mark>평소와 다른 IP 사용자</mark>(단계 2), <mark>대량 다운로드 사용자</mark>(단계 3)를 읽습니다.

**`saas_detection.py`**

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"                # 읽을 정규화 이벤트 파일 이름
USUAL_IPS = {"seoyeon": "198.51.100.9", "junho": "192.0.2.41", "jiwoo": "198.51.100.52"}  # 사용자별 평소 IP. gaeun 은 평소 기록이 없어 넣지 않았다
BUSINESS_START = 8                                    # 업무 시간이 시작하는 시
BUSINESS_END = 20                                     # 업무 시간이 끝나는 시(20시대, 20:59 까지가 업무 시간)
DOWNLOAD_LIMIT = 5                                    # 파일을 이 횟수 이상 내려받으면 대량 다운로드로 본다


def load_events(path):                                # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                       # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                     # 이벤트 표를 리턴한다


def pick_saas(events):                                # 이벤트 표를 받는 함수
    """SaaS 로그의 이벤트만 골라 새 표로 만든다.
    SaaS 이상 사용을 찾기 전에 쓴다.
    """
    sources = events["source"]                        # source 열만 꺼낸다
    is_saas = sources == "saas"                       # 각 행이 SaaS 이벤트인지 비교해 True 또는 False 를 만든다
    saas = events[is_saas]                            # True 인 행만 골라 새 표로 만든다
    return saas                                       # SaaS 이벤트 표를 리턴한다


def pick_logins(saas):                                # SaaS 이벤트 표를 받는 함수
    """로그인 이벤트만 골라 새 표로 만든다.
    로그인 시각과 IP 를 살펴보기 전에 쓴다.
    """
    actions = saas["action"]                          # action 열만 꺼낸다
    is_login = actions == "login"                     # 각 행이 로그인인지 비교해 True 또는 False 를 만든다
    logins = saas[is_login]                           # True 인 행만 골라 새 표로 만든다
    return logins                                     # 로그인 이벤트 표를 리턴한다


def find_off_hours_logins(logins):                    # 로그인 표를 받는 함수
    """업무 시간 밖에 시도한 로그인만 골라 새 표로 만든다.
    새벽 로그인처럼 평소에 없는 시각을 찾을 때 쓴다.
    """
    times = pd.to_datetime(logins["time"])            # 문자열 시각을 시각 값으로 바꾼다 — 미리 채운 줄
    hours = times.dt.hour                             # 시각 값에서 시(0~23)만 꺼낸다 — 미리 채운 줄

    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. hours 가 BUSINESS_START 이상 BUSINESS_END 이하인지 between 으로 구해 is_business_hour 에 담는다
    # 2. is_business_hour 의 반대를 ~ 로 구해 is_off_hours 에 담는다
    off_hours_logins = logins[is_off_hours]           # True 인 행만 골라 새 표로 만든다
    return off_hours_logins                           # 업무 시간 밖 로그인 표를 리턴한다


def find_new_ip_users(logins):                        # 로그인 표를 받는 함수
    """평소와 다른 IP 로 로그인한 사용자를 골라 리스트로 만든다.
    계정을 다른 사람이 쓰는지 의심할 때 쓴다.
    """
    new_ip_users = []                                 # 사용자를 담을 빈 리스트
    login_list = logins.to_dict("records")            # 표를 이벤트 딕셔너리 리스트로 바꾼다
    for login in login_list:                          # 로그인을 하나씩 꺼낸다
        user = login["user"]                          # 그 로그인의 사용자
        ip = login["ip"]                              # 그 로그인의 IP
        usual_ip = USUAL_IPS.get(user)                # 그 사용자의 평소 IP(기록이 없으면 None)
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. usual_ip 가 None 이 아닌지 구해 has_usual_ip 에 담는다 (None 인지는 is None, 아닌지는 is not None)
        # 4. ip 가 usual_ip 와 다른지 != 로 구해 is_new_ip 에 담는다 (같은지는 ==, 다른지는 !=)
        if has_usual_ip and is_new_ip:                # 평소 IP 기록이 있고, 이번 IP 가 평소와 다르면
            # 5. new_ip_users 에 user 를 추가한다
    return new_ip_users                               # 평소와 다른 IP 로 로그인한 사용자를 리턴한다


def find_bulk_download_users(saas):                   # SaaS 이벤트 표를 받는 함수
    """파일을 기준 횟수 이상 내려받은 사용자를 리스트로 만든다.
    자료를 한꺼번에 빼 가는 사용자를 찾을 때 쓴다.
    """
    actions = saas["action"]                          # action 열만 꺼낸다
    is_download = actions == "file.download"          # 각 행이 다운로드인지 비교해 True 또는 False 를 만든다
    downloads = saas[is_download]                     # True 인 행만 골라 새 표로 만든다
    counts = downloads.groupby("user").size()         # user 가 같은 행끼리 그룹으로 만들고(groupby) 바로 그룹마다 행이 몇 개인지 센다(size) — 사용자별 다운로드 횟수
    is_bulk = counts >= DOWNLOAD_LIMIT                # 사용자마다 횟수가 기준 이상인지 비교해 True 또는 False 를 만든다
    bulk_counts = counts[is_bulk]                     # 기준 이상인 사용자와 횟수만 남긴다
    bulk_users = list(bulk_counts.index)              # 사용자 이름만 리스트로 만든다
    return bulk_users                                 # 대량 다운로드 사용자를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 · 2번은 함수 안이라 앞에 공백 4개이고, 3 · 4번은 `for` 안이라 8개이며, 5번은 `if` 안이라 12개입니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.**
- 채우기 전에 실행하면 `IndentationError: expected an indented block` 오류가 납니다(파이썬 버전에 따라 뒤에 `after 'if' statement on line …` 이 붙기도 합니다). `if` 안쪽의 5번이 비어 있기 때문입니다.

**`exercise6-2_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. `list(열)` 은 열의 값을 리스트로 만듭니다.

```python
from saas_detection import load_events, pick_saas, pick_logins, find_off_hours_logins, find_new_ip_users, find_bulk_download_users, EVENTS_PATH  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)                            # 이벤트 파일을 표로 읽는다
saas = pick_saas(events)                                     # SaaS 이벤트만 골라낸다
logins = pick_logins(saas)                                   # 로그인 이벤트만 골라낸다

off_hours_logins = find_off_hours_logins(logins)             # 업무 시간 밖 로그인만 골라낸다
off_hours_count = len(off_hours_logins)                      # 업무 시간 밖 로그인이 몇 건인지 센다
print("--- 단계 1: 업무 시간 밖 로그인", off_hours_count, "건")  # 단계 1 시작을 알리는 줄과 건수
print(off_hours_logins)                                      # 그 로그인 표를 출력한다

new_ip_users = find_new_ip_users(logins)                     # 평소와 다른 IP 로 로그인한 사용자를 찾는다
print("--- 단계 2: 평소와 다른 IP 로 로그인한 사용자", new_ip_users)  # 단계 2 시작을 알리는 줄과 사용자

bulk_users = find_bulk_download_users(saas)                  # 파일을 대량으로 내려받은 사용자를 찾는다
print("--- 단계 3: 파일을 5번 이상 내려받은 사용자", bulk_users)  # 단계 3 시작을 알리는 줄과 사용자
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `saas_detection.py` · `exercise6-2_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `saas_detection.py` 에서 <mark>직접 쓰는 곳 다섯 군데를 씁니다</mark>. 2.1 의 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise6-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise6-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **세 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1은 표 2줄이고, 단계 2와 3은 사용자가 제목 줄에 함께 나오므로 그 아래 줄이 없습니다.
5. **[보고서]** Unit 6 의 `## Exercise 6-2` › `### Exercise 6-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 규칙마다 해당한 사용자를 적어 주세요.
   - (나) [핵심 질문] jiwoo 는 업무 시간 밖(02:14)과 평소와 다른 IP 두 규칙에 해당하지만 그 로그인은 실패였습니다. 이 기록만으로 계정 도용을 확정할 수 있나요? 그렇게 판단한 이유와, 샘플 로그에서 더 찾아볼 수 있는 것을 한 가지 적어 주세요.
   - (다) [핵심 질문] gaeun 은 평소 IP 기록이 없어 「평소와 다른 IP」 규칙에서 제외됩니다. 제외하지 않으면 어떤 일이 생기고, 제외하면 어떤 위험이 남나요?

## Exercise 6-2 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 범위 안인지 | `is_business_hour = hours.between(BUSINESS_START, BUSINESS_END)` |
| 조건 뒤집기 | `is_off_hours = ~is_business_hour` |
| 평소 기록이 있는지 | `has_usual_ip = usual_ip is not None` |
| 평소 IP 와 다른지 | `is_new_ip = ip != usual_ip` |

---
