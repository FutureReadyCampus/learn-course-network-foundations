---
id: m4-u04-l03
title: 실습 4-2 · 로그인 실패 5번 이상인 주소 찾기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/102_day03_am_baseline_login.md
  mission_id: GichanSource.m4-1104-am-baseline-login
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 4-2 · 로그인 실패 5번 이상인 주소 찾기

## 이번 의뢰: 로그인 실패가 많은 주소

> **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「실습 4-1에서 정한 대로, 같은 주소가 하루에 로그인에 5번 이상 실패하면 담당자에게 알리기로 했습니다.
>
> 샘플 이벤트 57개 중에서 로그인 요청(`POST /login`)이 실패한 것이 모두 몇 개인지 세 주세요. 주소별로 몇 번씩 실패했는지 정리하고, 5번 이상 실패한 주소가 있으면 알려 주세요.」
> - **왜 중요한가**: <mark>로그인에 연달아 실패하는 것은 다른 사람이 비밀번호를 맞혀 보는 대표적인 모습입니다.</mark> 이벤트 수만 개를 사람이 하나씩 읽지 않고, 알림 기준(5번) 이상인 주소만 추출해 보여 주면 담당자가 먼저 볼 곳이 정해집니다.

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「실습」 전까지는 이 실습의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 왜 세 단계로 찾는가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 실습 4-1에서 「한 주소가 하루에 로그인에 5번 이상 실패하면 알린다」는 알림 기준(임계값)을 정했습니다. <mark>이제 이벤트 57개에 그 기준을 적용합니다.</mark>
2. <mark>찾는 순서는 세 단계입니다</mark>: ① **로그인 요청이면서 실패한 것**만 고르고, ② **IP 주소별로 센** 뒤, ③ **5번 이상인 주소**만 남깁니다.

## 2.1 로그인 실패 규칙과 문법 상자 네 개

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문은 없습니다. 판다스 문법 상자의 코드는 눈으로 읽으면 됩니다.

샘플에서 203.0.113.50 이 보낸 이벤트 전부입니다(9개, 표에서의 행 번호 포함).

| 행 번호 | 시각 | `action` | `result` | 로그인 요청인가 | 실패인가 | 둘 다인가 |
|---|---|---|---|---|---|---|
| 9 | 09:12:01 | `GET /login` | 성공 | 아니오 | 아니오 | 아니오 |
| 10 | 09:12:03 | `POST /login` | 실패 | 예 | 예 | **예** |
| 11 | 09:12:06 | `POST /login` | 실패 | 예 | 예 | **예** |
| 12 | 09:12:09 | `POST /login` | 실패 | 예 | 예 | **예** |
| 13 | 09:12:12 | `POST /login` | 실패 | 예 | 예 | **예** |
| 14 | 09:12:15 | `POST /login` | 실패 | 예 | 예 | **예** |
| 15 | 09:12:18 | `POST /login` | 성공 | 예 | 아니오 | 아니오 |
| 16 | 09:12:25 | `GET /admin` | 실패 | 아니오 | 예 | 아니오 |
| 17 | 09:12:27 | `GET /admin/users` | 실패 | 아니오 | 예 | 아니오 |

- `GET /login` 은 로그인 화면을 보여 달라는 요청이고, `POST /login` 은 아이디와 비밀번호를 보내는 요청입니다. <mark>이번 Unit에서는 `POST /login` 이 실패한 이벤트만 셉니다.</mark>
- SaaS 의 `login` 실패 1건(jiwoo, 02:14)은 Unit 6에서 다루므로 이번 Unit에서는 세지 않습니다. <mark>그래서 로그인 실패 이벤트는 5개입니다.</mark>

**알아 둘 것 — 열 꺼내기와 평균도 실무에서는 한 줄로 씁니다**

실습 4-1에서 쓴 두 줄(`daily_failed_logins = daily["failed_logins"]` → `average = daily_failed_logins.mean()`)은 실무에서 아래 한 줄로 자주 씁니다. 같은 일입니다. **직접 쓰지 않고 읽기만 합니다.** 자세한 쓰임은 다음에 차차 배웁니다.

```python
import pandas as pd                         # 판다스를 pd 라는 짧은 이름으로 불러온다
daily = pd.read_csv("baseline_logins.csv")  # CSV 파일을 읽어 표로 만든다 — 한 행이 하루

average = daily["failed_logins"].mean()     # 열 꺼내기와 평균을 한 줄로 쓴 모양 — 위 두 줄과 같은 결과
print(average)                              # 2.4285714285714284 — 소수점 아래가 길게 나오는 것은 round 를 쓰지 않았기 때문이다
```

실행 결과:

```
2.4285714285714284
```

**문법 상자 — `=` 와 `==`**

**`=` 는 오른쪽 값을 왼쪽 이름에 담고, `==` 는 두 값이 같은지 비교합니다. 한 줄에 같이 쓰면 비교(`==`)를 먼저 하고 그 결과를 `=` 로 담습니다**

```python
age = 20              # age 에 20을 담는다 (=)
is_adult = age == 20  # age 가 20과 같은지 비교하고(==), 그 결과를 is_adult 에 담는다(=)
print(is_adult)       # True
```

실행 결과:

```
True
```

- 읽는 법: <mark>오른쪽의 비교 `age == 20` 을 먼저 계산하고,</mark> 그 결과 `True` 를 왼쪽 이름에 담습니다. `(age == 20)` 처럼 괄호를 넣어도 같은 뜻이고, 계산 순서가 눈에 보일 뿐입니다.
- `is_fail = results == "실패"` 를 `is_fail = results = "실패"` 로 잘못 쓰면 그 줄은 오류 없이 지나가지만 `is_fail` 이 열이 아니라 문자열 `"실패"` 가 되어, 다음 줄 `events[is_fail]` 에서 `KeyError` 가 납니다. **비교는 항상 `==` 로 씁니다.**

**판다스 문법 상자 — 조건으로 행 필터링하기**

**<mark>`표[조건]`</mark> 은 조건이 `True` 인 행만 남겨 새 표를 만듭니다**

`results == "실패"` 는 `result` 열의 값을 하나씩 `"실패"` 와 비교합니다. 같으면 `True`, 다르면 `False` 입니다. 결과는 `True` · `False` 로 된 열(시리즈)입니다. <mark>이 열을 `표[…]` 안에 넣으면 `True` 인 행만 남습니다.</mark>

```python
import pandas as pd                                                 # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                            # 연습용 작은 데이터(열 이름: 값들)
    "user": ["gaeun", "dami", "seoyeon", "junho", "dami"],          # user 열에 들어갈 값들
    "action": ["login", "login", "download", "login", "download"],  # action 열에 들어갈 값들
    "result": ["성공", "실패", "실패", "실패", "성공"],             # result 열에 들어갈 값들
}
logs = pd.DataFrame(data)                                           # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
print(logs)                                                         # 표를 출력한다
```

실행 결과:

```
      user    action result
0    gaeun     login     성공
1     dami     login     실패
2  seoyeon  download     실패
3    junho     login     실패
4     dami  download     성공
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
results = logs["result"]     # result 열만 꺼낸다
is_fail = results == "실패"  # 값이 "실패" 와 같은지 하나씩 비교해 True 또는 False 로 만든다
print(is_fail)               # True · False 를 출력한다
```

실행 결과:

```
0    False
1     True
2     True
3     True
4    False
Name: result, dtype: bool
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
failed = logs[is_fail]  # True 인 행만 남겨 새 표(failed)를 만든다
print(failed)           # 새 표를 출력한다
```

실행 결과:

```
      user    action result
1     dami     login     실패
2  seoyeon  download     실패
3    junho     login     실패
```

- 읽는 법: <mark>두 번째 출력에서 1·2·3번 행이 `True`(실패)</mark>이고, 세 번째 출력은 그 세 행만 남은 표입니다. 열은 그대로 3개입니다. 왼쪽 숫자(1, 2, 3)는 원래 표의 행 번호를 그대로 가져온 것입니다.

**판다스 문법 상자 — 두 조건을 함께 걸기**

**<mark>`조건A & 조건B`</mark> 는 두 조건이 모두 `True` 이면 `True`, 하나라도 `False` 이면 `False` 입니다. 이 열을 `표[…]` 에 넣으면 두 조건을 모두 만족하는 행만 남습니다**

위에서는 조건 하나(`results == "실패"`)로 걸렀습니다. 「로그인 요청이면서 실패」처럼 조건이 둘이면 각각 `True` · `False` 열로 만든 뒤 `&` 로 합칩니다(둘 다 `True` 인 행만 `True`). **`and` 가 아니라 `&` 를 씁니다.**

```python
import pandas as pd                                                 # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                            # 연습용 작은 데이터(열 이름: 값들)
    "user": ["gaeun", "dami", "seoyeon", "junho", "dami"],          # user 열에 들어갈 값들
    "action": ["login", "login", "download", "login", "download"],  # action 열에 들어갈 값들
    "result": ["성공", "실패", "실패", "실패", "성공"],             # result 열에 들어갈 값들
}
logs = pd.DataFrame(data)                                           # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
print(logs)                                                         # 표를 출력한다
```

실행 결과:

```
      user    action result
0    gaeun     login     성공
1     dami     login     실패
2  seoyeon  download     실패
3    junho     login     실패
4     dami  download     성공
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
actions = logs["action"]        # action 열만 꺼낸다
is_login = actions == "login"   # 값이 "login" 과 같은지 하나씩 비교해 True 또는 False 로 만든다
results = logs["result"]        # result 열만 꺼낸다
is_fail = results == "실패"     # 값이 "실패" 와 같은지 하나씩 비교해 True 또는 False 로 만든다

both_true = is_login & is_fail  # 두 조건이 모두 True 인 행만 True 로 만든다
print(both_true)                # True · False 를 출력한다
```

실행 결과:

```
0    False
1     True
2    False
3     True
4    False
dtype: bool
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
login_failures = logs[both_true]  # True 인 행만 남겨 새 표를 만든다
print(login_failures)             # 새 표를 출력한다
```

실행 결과:

```
    user action result
1   dami  login     실패
3  junho  login     실패
```

- 읽는 법: <mark>로그인이면서 실패인 1번 행과 3번 행만 `True`</mark> 이고, 세 번째 출력은 그 두 행만 남은 표입니다.
- 한 줄씩 따라가면 이렇습니다.

| 코드 | 만들어지는 것 |
|---|---|
| `is_login = actions == "login"` | 로그인인 행만 `True` |
| `is_fail = results == "실패"` | 실패인 행만 `True` |
| `both_true = is_login & is_fail` | 둘 다 `True` 인 행만 `True` |
| `login_failures = logs[both_true]` | `True` 인 행만 모은 새 표 |

- `&` 는 파이썬에서 원래 다른 용도로 쓰는 기호인데, 판다스에서는 열 두 개를 같은 줄끼리 짝지어 합치는 데 씁니다. `==` 가 열의 값을 하나씩 비교하는 것과 같은 이유입니다.
- `and` 는 `True` 또는 `False` 하나씩 두 개를 이을 때만 씁니다. 열에는 값이 여러 개 있어서 `and` 로 이을 수 없고(`ValueError` 오류), **열을 이을 때는 `&` 를 씁니다.** 실습 4-3의 `result == "실패" and …` 는 값이 하나씩이라 `and` 를 씁니다.
- 비교를 `&` 로 바로 이을 때는 **괄호가 꼭 필요합니다**: `(a == 1) & (b == 2)`. `&` 가 `==` 보다 먼저 계산되기 때문입니다. 이번 Unit에서는 비교를 이름에 먼저 담은 뒤 `is_login & is_fail` 로 이어서 괄호가 필요 없습니다.

**판다스 문법 상자 — 기준 이상인 것만 남기기**

**<mark>`ip_fail_counts >= 기준`</mark> 은 값이 기준 이상이면 `True`, 아니면 `False` 로 만들고, 그 열을 `ip_fail_counts[…]` 에 넣으면 `True` 인 것만 남습니다**

위에서 배운 `==` 처럼 `>=` 도 값을 하나씩 비교해 `True` · `False` 를 만듭니다. 아래 `ip_fail_counts` 는 주소별 실패 횟수입니다(왼쪽 인덱스가 주소, 오른쪽이 횟수). `ip_fail_counts >= 3` 은 주소마다 「3번 이상인가」를 `True` · `False` 로 만듭니다.

```python
import pandas as pd                                                                                           # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                                                                      # 실패한 이벤트만 적은 연습용 작은 데이터
    "ip": ["198.51.100.90", "203.0.113.50", "198.51.100.90", "203.0.113.50", "198.51.100.90", "192.0.2.15"],  # ip 열에 들어갈 값들
    "result": ["실패", "실패", "실패", "실패", "실패", "실패"],                                               # result 열에 들어갈 값들
}
failed = pd.DataFrame(data)                                                                                   # 데이터로 표를 만든다
print(failed)                                                                                                 # 표를 출력한다
```

실행 결과:

```
              ip result
0  198.51.100.90     실패
1   203.0.113.50     실패
2  198.51.100.90     실패
3   203.0.113.50     실패
4  198.51.100.90     실패
5     192.0.2.15     실패
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
ip_fail_counts = failed.groupby("ip").size()  # ip 가 같은 행끼리 그룹으로 만들고(groupby) 바로 그룹마다 행이 몇 개인지 센다(size) — 주소별 실패 횟수
print(ip_fail_counts)                         # 주소와 실패 횟수가 줄마다 나온다
```

실행 결과:

```
ip
192.0.2.15       1
198.51.100.90    3
203.0.113.50     2
dtype: int64
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
is_many = ip_fail_counts >= 3   # 주소마다 「3번 이상인가?」를 비교해 True 또는 False 로 만든다
many = ip_fail_counts[is_many]  # True 인 주소만 남긴다
print(many)                     # 3번 이상인 주소와 횟수
```

실행 결과:

```
ip
198.51.100.90    3
dtype: int64
```

- 읽는 법: 두 번째 출력은 주소 3개의 실패 횟수이고, <mark>세 번째 출력은 그중 3번 이상인 주소 1개</mark>입니다(198.51.100.90 이 3번).
- `failed.groupby("ip").size()` 는 Unit 3에서 두 줄로 나눠 배운 동작을 점(`.`)으로 이은 한 줄입니다. 왼쪽부터 차례로 읽습니다. ① `groupby("ip")` 가 ip 가 같은 행끼리 그룹을 만들고, ② 바로 이어서 `.size()` 가 그룹마다 행이 몇 개인지 셉니다. 이 수업에서는 점으로 이어 쓰는 것을 **두 개까지만** 씁니다.
- 이 예는 연습용 작은 표이고, 문제에서는 로그인 요청의 실패 이벤트를 주소별로 셉니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_events` | 파일 경로 | 이벤트 표(미리 채움) |
| `pick_login_failures` | 이벤트 표 | 로그인 요청이면서 실패한 행만 담은 표 |
| `count_by_ip` | 로그인 실패 표 | 주소별 실패 횟수(미리 채움) |
| `pick_alert_ips` | 주소별 횟수와 알림 기준 | 기준 이상인 주소와 횟수 |

- **직접 쓰는 곳은 여덟 군데**(번호 1 ~ 8)이고, 함수 두 개 안에 나뉘어 있습니다.
  - `pick_login_failures`(1 ~ 6번): 로그인 요청인 행과 실패인 행을 `&` 로 이어 걸러 냅니다.
  - `pick_alert_ips`(7 · 8번): 횟수가 기준 이상인 주소만 남깁니다.
- 주소별로 그룹화해 세는 `count_by_ip` 는 Unit 3에서 배운 `groupby().size()` 와 같아서 미리 채웠습니다.

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## 실습 4-2 · 로그인 실패 5번 이상인 주소 찾기

**이런 상황이 있습니다**

- **지금은**: 57개 이벤트 중 로그인 실패가 몇 개이고 어느 주소가 많은지 사람이 하나씩 읽어야 합니다.
- **그래서 만드는 것**: `login_detection.py` 입니다.
  - 로그인 요청이면서 실패한 이벤트를 골라냅니다.
  - IP 주소별로 실패를 셉니다.
  - 횟수가 5번 이상인 주소만 남깁니다.
- **실행하면**: 단계 1: 로그인 실패 이벤트 수, 단계 2: 주소별 횟수, 단계 3: 알림 대상 주소가 나옵니다.
- **현업에서는**: 로그인 실패 규칙은 거의 모든 관제 화면에 있는 기본 규칙입니다. 알림이 난 주소를 막을지 판단하는 첫 단서가 됩니다.

**할 일**

1. `login_detection.py` · `exercise4-2_run.py` **두 파일**을 만들고, `login_detection.py` 의 `pick_login_failures` · `pick_alert_ips` 에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>로그인 실패 이벤트 수</mark>(단계 1), <mark>주소별 횟수</mark>(단계 2), <mark>알림 대상 주소</mark>(단계 3)를 읽습니다.

**`login_detection.py`**

```python
import pandas as pd                                             # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"                          # 읽을 정규화 이벤트 파일 이름
LOGIN_LIMIT = 5                                                 # 알림 기준: 평소 하루 최대가 4번이라 5번 이상이면 알린다


def load_events(path):                                          # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                                 # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                               # 이벤트 표를 리턴한다


def pick_login_failures(events):                                # 이벤트 표를 받는 함수
    """로그인 요청이 실패한 이벤트만 골라 새 표로 만든다.
    로그인 실패가 많은 주소를 조사하기 전에 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. events 의 "action" 열을 꺼내 actions 에 담는다
    # 2. actions 가 "POST /login" 과 같은지 비교한 결과(==)를 is_login 에 담는다
    # 3. events 의 "result" 열을 꺼내 results 에 담는다
    # 4. results 가 "실패" 와 같은지 비교한 결과(==)를 is_fail 에 담는다
    # 5. is_login & is_fail 로 두 조건을 합쳐 both_true 에 담는다 (둘 다 True 인 행만 True)
    # 6. events 에서 both_true 가 True 인 행만 골라 login_failures 에 담는다 (events[both_true])
    return login_failures                                       # 로그인 실패 이벤트만 담은 표를 리턴한다


def count_by_ip(login_failures):                                # 로그인 실패 표를 받는 함수
    """로그인 실패를 IP 주소별로 센다.
    같은 주소가 반복해서 실패했는지 볼 때 쓴다.
    """
    ip_login_fail_counts = login_failures.groupby("ip").size()  # ip 가 같은 행끼리 그룹으로 만들고(groupby) 바로 그룹마다 행이 몇 개인지 센다(size)
    return ip_login_fail_counts                                 # 주소별 실패 횟수를 리턴한다


def pick_alert_ips(ip_login_fail_counts, limit):                # 주소별 횟수와 알림 기준을 받는 함수
    """실패 횟수가 알림 기준 이상인 주소만 골라 리턴한다.
    알림을 보낼 주소를 가릴 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. ip_login_fail_counts 가 limit 이상인지 비교한 결과(>=)를 is_many 에 담는다
    # 8. ip_login_fail_counts 에서 is_many 가 True 인 것만 골라 alert_ips 에 담는다 (ip_login_fail_counts[is_many])
    return alert_ips                                            # 알림 기준 이상인 주소와 횟수를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 8번은 모두 함수 안이라 앞에 공백 4개입니다.
- 미리 채운 `count_by_ip` 의 `groupby("ip").size()` 는 2.1 에서 본 것처럼 두 동작을 점으로 이은 한 줄입니다. ① `groupby("ip")` 로 ip 가 같은 행끼리 그룹을 만들고 ② `.size()` 로 그룹마다 행 수를 셉니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.**
- 채우기 전에 실행하면 `NameError: name 'login_failures' is not defined` 오류가 납니다. 1 ~ 6번을 아직 안 썼기 때문입니다.

**`exercise4-2_run.py`** — <mark>그대로 붙여 넣습니다.</mark> 직접 쓰는 줄은 없습니다. `len(표)` 는 표의 행 수입니다.

```python
from login_detection import load_events, pick_login_failures, count_by_ip, pick_alert_ips, EVENTS_PATH, LOGIN_LIMIT  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)                              # 이벤트 파일을 표로 읽는다
login_failures = pick_login_failures(events)                   # 로그인 실패 이벤트만 골라낸다
failure_count = len(login_failures)                            # 로그인 실패가 모두 몇 개인지 센다
print("--- 단계 1: 로그인 실패 이벤트", failure_count, "개")   # 단계 1 시작을 알리는 줄과 개수

ip_login_fail_counts = count_by_ip(login_failures)             # 주소별로 실패 횟수를 센다
print("--- 단계 2: 주소별 로그인 실패 횟수")                   # 단계 2 시작을 알리는 줄
print(ip_login_fail_counts)                                    # 주소별 횟수를 출력한다

alert_ips = pick_alert_ips(ip_login_fail_counts, LOGIN_LIMIT)  # 알림 기준 이상인 주소만 고른다
print("--- 단계 3: 알림 기준", LOGIN_LIMIT, "번 이상인 주소")  # 단계 3 시작을 알리는 줄과 알림 기준
print(alert_ips)                                               # 알림을 보낼 주소를 출력한다
```

**순서**

1. **[VS Code]** 파일 `login_detection.py` · `exercise4-2_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `login_detection.py` 에서 직접 쓰는 곳 **여덟 군데**를 씁니다. 2.1 의 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise4-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise4-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **세 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1은 숫자가 제목 줄에 함께 나오므로 그 아래 줄이 없고, 단계 2와 단계 3은 각각 3줄입니다.
5. **[보고서]** `report_u4.md` 의 `## 실습 4-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 로그인 실패 이벤트 수와 알림 대상 주소, 그 횟수를 적어 주세요.
   - (나) [핵심 질문] 203.0.113.50 이 알림 대상이 되었습니다. 공격이라고 확정할 수 있는지 적고, 2.1 의 표에서 시각 간격과 성공 뒤에 요청한 경로를 보고 의심스러운 점을 적어 주세요. 그리고 5번 실패가 공격인지 판단하려면 이 표에 없는 정보 중 무엇이 더 필요한지 한 가지 적어 주세요(예: 어떤 사용자 이름으로 시도했는지).
   - (다) [핵심 질문] 한 주소가 로그인에 4번 실패하고 5번째에 성공했습니다. 이 규칙(실패 5번 이상)으로 이 접속에 알림이 생성될까요? 생성된다 · 생성되지 않는다와 이유를 적고, 생성되지 않는다면 담당자가 확인하지 못하는 정보가 무엇인지 적어 주세요.

## 실습 4-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 로그인 요청인 행 | `actions = events["action"]` → `is_login = actions == "POST /login"` |
| 실패인 행 | `results = events["result"]` → `is_fail = results == "실패"` |
| 둘 다인 행 | `both_true = is_login & is_fail` → `login_failures = events[both_true]` |
| 기준 이상인 주소 | `is_many = ip_login_fail_counts >= limit` → `alert_ips = ip_login_fail_counts[is_many]` |

---
