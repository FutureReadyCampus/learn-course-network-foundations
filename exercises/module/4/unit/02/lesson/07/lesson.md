---
id: m4-u02-l07
title: 정답
render: markdown
---

# 정답

## 정답을 읽는 방법

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

1. **핵심 실습**: 실습 2-1 ~ 2-3 정답입니다. 오늘 모두가 하는 실습이니 먼저 맞춰 봅니다.
2. **응용(여유가 되면)**: 응용 2-1 · 2-2 정답입니다. 응용을 한 사람만 봅니다.
3. 정답마다 채운 코드, 결과, 왜, 자주 틀리는 곳, 관제에서는 순서로 읽습니다.
4. 오류 메시지의 줄 번호와 `^^^^` 표시 줄은 사람마다, 파이썬 버전마다 다를 수 있습니다. 마지막 줄의 오류 이름과 내용을 봅니다.

---

## 실습 2-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise2-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-1_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 곳(① · ②)입니다.

① `load_events` 안

```python
    # ① pd.read_json 으로 path 의 파일을 읽어 events 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    events = pd.read_json(path)  # 파일을 읽어 표로 만든다
```

② `count_values` 안

```python
    # ② values 에서 값별 개수를 value_counts() 로 세어 value_event_counts 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    value_event_counts = values.value_counts()  # 값별 개수를 센다
```

**결과**

- (가) 출력은 다음과 같습니다. 표는 <mark>**57행 6열**</mark>이고, 성공은 <mark>**34**</mark>개, 실패는 <mark>**23**</mark>개입니다. 실패한 이벤트의 소스별 개수는 web <mark>**13**</mark> · server <mark>**9**</mark> · saas <mark>**1**</mark> 입니다.

```
--- 단계 1: 표 크기(행 수, 열 수)와 처음 3개 시각
(57, 6)
2026-11-02 02:14:08
2026-11-02 09:01:05
2026-11-02 09:01:06
--- 단계 2: 성공 · 실패별 개수
result
성공    34
실패    23
Name: count, dtype: int64
--- 단계 3: 실패한 이벤트 23 개의 소스별 개수
source
web       13
server     9
saas       1
Name: count, dtype: int64
--- 단계 4: 전체 이벤트의 소스별 개수
source
web       28
server    15
saas      14
Name: count, dtype: int64
```

- 읽는 법: 첫 줄 `source` 는 센 열의 이름이고, 아래 줄은 <mark>왼쪽이 값, 오른쪽이 나온 횟수</mark>입니다. 28 + 15 + 14 = 57 이라 이벤트 전체 개수와 같습니다.

- (나) 개수만 보면 web 이 13개로 가장 많지만, <mark>그것만으로 web 이 가장 문제가 큰 소스라고 말할 수는 없습니다</mark>.
  - 소스마다 전체 이벤트 수가 다릅니다. 전체 중 실패의 비율로 보면 이렇습니다.

  | 소스 | 전체 이벤트 | 실패 | 실패 비율 |
  |---|---|---|---|
  | web | 28 | 13 | 13/28 = 약 46% |
  | server | 15 | 9 | 9/15 = 60% |
  | saas | 14 | 1 | 1/14 = 약 7% |

  - <mark>비율로는 server 가 가장 높습니다.</mark> 개수는 전체 규모의 영향을 받으므로, 소스끼리 비교할 때는 전체 대비 비율도 함께 봅니다.
- (다) 예상은 이렇습니다.
  - 사용자 이름으로 세려 해도 <mark>web 실패 13개는 `user` 가 비어 있어서 들어갈 사용자가 없습니다</mark>. web 실패 13개가 사용자별로 세어지지 않는다는 것을 실습 2-2에서 확인합니다.
  - 대신 `ip` 열을 봅니다. 같은 주소에서 실패가 여러 번 난 것을 찾으면 누구인지는 몰라도 같은 대상이 반복했는지 알 수 있습니다.

**왜**

- <mark>이벤트를 표로 읽으면 「걸러 내기 → 세기」가 몇 줄로 끝나고, 이벤트가 57개일 때나 5만 개일 때나 같은 코드를 씁니다.</mark>
  - 조건 비교(`==`)는 줄마다 `True` 또는 `False` 를 만들고, `표[조건]` 은 `True` 인 행만 남깁니다.

**자주 틀리는 곳**

| 실수 | 나오는 것 | 고치는 법 |
|---|---|---|
| ① 에서 `pd.read_json("path")` 처럼 따옴표를 붙임 | `path` 라는 파일을 찾아서 `FileNotFoundError` | 변수 `path` 는 따옴표 없이 씁니다 |
| ② 에서 `value_counts()` 의 괄호를 뺌 | 오류는 없지만 개수 대신 `<bound method …>` | 뒤에 괄호를 붙여 호출합니다 |

- **① 에서 `path` 에 따옴표를 붙이면 `FileNotFoundError` 오류가 납니다(판다스 2.x 에서는 `FutureWarning` 경고 뒤에 `ValueError: Expected object or value` 가 날 수도 있습니다).** `"path"` 는 변수가 아니라 글자 그대로의 파일 이름이 되기 때문입니다. 실행하면 다음 오류가 납니다(<mark>`No such file or directory: 'path'`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise2-1_run.py", line 3, in <module>
    events = load_events(EVENTS_PATH)  # 이벤트 파일을 표로 읽는다
  File "…/anomaly_detection/events_basic.py", line 11, in load_events
    events = pd.read_json("path")  # path 에 따옴표를 붙였다
FileNotFoundError: [Errno 2] No such file or directory: 'path'
```

  - 줄 번호는 사람마다 다릅니다. 판다스 안쪽 파일의 줄은 길어서 생략했습니다.
- `count_values` 의 **`value_counts` 는 뒤에 괄호를 붙여 호출하는 메서드입니다.** 메서드(method · 메서드)는 `열.value_counts()` 처럼 표나 열 뒤에 점(`.`)을 찍어 부르는 함수입니다.

**관제에서는**

- 관제 도구의 「실패 이벤트 수 · 소스별 분포」 화면은 이 계산을 계속 다시 합니다. 분포를 보고 어느 소스부터 조사할지 정합니다.
  - 숫자는 「살펴볼 곳」을 알려 줄 뿐이고, <mark>개수가 많다고 곧 공격이라는 뜻은 아닙니다</mark>.

---

## 실습 2-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise2-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-2_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 `count_by_user` 의 두 곳(① · ②)입니다.

① 은 `# ①` 주석 바로 아래(4칸)에 씁니다.

```python
    grouped = failed.groupby("user")  # user 가 같은 행끼리 묶는다
```

② 는 미리 채운 `user_fail_counts = grouped.size()` 줄 뒤, `# ②` 주석 바로 아래(4칸)에 씁니다. ① 과 ② 는 떨어져 있으니 한 상자처럼 이어 붙이지 않습니다.

```python
    sorted_user_fail_counts = user_fail_counts.sort_values(ascending=False)  # 큰 값부터 순서대로 정렬한다
```

**결과**

- (가) 출력은 다음과 같고, 실패가 가장 많은 사용자는 <mark>**dami(4번)**</mark>, 가장 많이 난 시간대는 <mark>**9시(13번)**</mark>, 저장된 행은 <mark>**23개**</mark>입니다.

```
--- 단계 1: 사용자별 실패 횟수
user
dami       4
gaeun      3
seoyeon    2
jiwoo      1
dtype: int64
--- 단계 2: 시간대별 실패 횟수
hour
2      1
9     13
10     3
11     5
18     1
dtype: int64
--- 단계 3: 저장한 파일 failed_events.csv
저장된 행 23 개
```

- (나) 9시의 13개는 실습 2-1 단계 3의 web 실패 13개와 같은 숫자입니다. <mark>웹 서버에서 난 실패가 모두 9시에 났다는 단서</mark>입니다.
  - <mark>숫자가 같다는 것만으로는 확정할 수 없습니다.</mark> 확정하려면 `failed_events.csv` 를 열어 `hour` 가 9인 행의 `source` 를 봅니다(실제로 13개 모두 `web` 입니다).
  - 웹 서버 로그에는 사용자가 없으므로, <mark>먼저 확인할 것은 같은 시간대의 `ip`</mark> 입니다. 같은 주소가 로그인 실패를 반복했는지, 없는 주소를 차례로 요청했는지 봅니다.
  - 한 시간대에 실패가 많이 났을 때는 이어서 세 가지를 봅니다. 어느 소스에서 났는지, 같은 주소나 같은 사용자가 반복했는지, 그 직후에 성공한 이벤트가 있는지입니다.
- (다) 사용자별 합계는 4 + 3 + 2 + 1 = 10이고 실패한 이벤트는 23개라서 <mark>**13개**</mark>가 빠졌습니다.
  - 빠진 13개는 `user` 가 비어 있는 웹 서버 이벤트입니다. `groupby("user")` 가 비어 있는 값의 행을 그룹에 넣지 않았기 때문입니다.
  - 모르고 사용자별 숫자만 보면 <mark>「실패가 10개뿐」이라고 잘못 판단하거나, 가장 많은 실패(웹 서버 13개)를 아예 놓칩니다</mark>.

**왜**

- <mark>묶어서 세면 전체 합계 숫자에서는 보이지 않던 차이가 드러납니다.</mark> 사용자별 · 시간대별 집계는 평소 기준과 비교할 때의 출발점입니다.
  - 시각은 문자열이면 「시」를 꺼낼 수 없으므로 시각 값으로 바꾼 뒤에 `.dt.hour` 를 씁니다.

**자주 틀리는 곳**

| 실수 | 나오는 것 | 고치는 법 |
|---|---|---|
| ① 에서 `groupby("users")` 처럼 씀 | 표에 없는 열 이름이라서 `KeyError` | 표에 있는 열 이름 `user` 를 씁니다 |
| ② 에서 `ascending=False` 를 뺌 | **오류는 나지 않지만** 작은 값부터 나옴(단계 1 첫 줄이 dami 가 아니라 jiwoo) | `ascending=False` 를 넣습니다 |

- **열 이름을 틀리면 `KeyError` 오류가 납니다.** 실행하면 다음 오류가 납니다(<mark>`KeyError: 'users'`</mark> 처럼 틀린 열 이름이 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise2-2_run.py", line 8, in <module>
    by_user = count_by_user(failed)  # 실패 횟수를 사용자별로 센다
  File "…/anomaly_detection/events_time.py", line 31, in count_by_user
    grouped = failed.groupby("users")  # user 가 같은 행끼리 묶는다
KeyError: 'users'
```

  - 줄 번호는 사람마다 다릅니다. 판다스 안쪽 파일의 줄은 길어서 생략했습니다.

**관제에서는**

- 집계 결과는 알림을 만들 때 근거가 되는 숫자입니다. 근거가 된 이벤트를 파일로 남기면 담당자가 알림이 왜 났는지 확인할 수 있습니다.
  - <mark>집계에서 빠진 값(`null`)이 있는지 함께 확인하는 것</mark>이 습관입니다.

---

## 실습 2-3 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise2-3_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-3_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 곳(① · ②)입니다.

① `pick_login_failures` 안

```python
    # ① is_login 과 is_fail 을 & 로 합쳐 both_true 에 담는다 (둘 다 True 인 행만 True)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    both_true = is_login & is_fail  # 행마다 「로그인 요청이면서 실패」일 때만 True 가 된다
```

② `pick_alert_ips` 안

```python
    # ② ip_login_fail_counts 가 limit 이상인지 비교한 결과(>=)를 is_many 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    is_many = ip_login_fail_counts >= limit  # 주소마다 「횟수가 기준 이상인가?」를 비교해 True 또는 False 를 만든다
```

**결과**

- (가) 출력은 다음과 같고, 로그인 실패 이벤트는 <mark>**5개**</mark>, 알림 대상은 <mark>**203.0.113.50(5번)**</mark> 한 주소입니다.

```
--- 단계 1: 로그인 실패 이벤트 5 개
--- 단계 2: 주소별 로그인 실패 횟수
ip
203.0.113.50    5
dtype: int64
--- 단계 3: 알림 기준 5 번 이상인 주소
ip
203.0.113.50    5
dtype: int64
```

- (나) <mark>203.0.113.50 이 공격이라고 확정할 수는 없습니다.</mark> 다만 의심할 단서는 여럿 있습니다.
  - 단서: <mark>일정한 3초 간격으로 5번 연달아 실패했고(자동 입력처럼 보임),</mark> 6번째에 로그인에 성공한 뒤 곧바로 관리자 경로(`/admin` · `/admin/users`)를 두 번 요청했습니다.
  - 이 표에 없는 더 필요한 정보: <mark>그 주소가 회사 직원의 주소인지, 로그인에 성공한 계정이 누구인지</mark>입니다(웹 서버 로그에는 계정 이름이 없으므로 판정 서버 · SaaS 로그와 시각을 맞춰 봐야 합니다).
  - **알림은 「먼저 살펴볼 곳」이고 공격의 확정이 아닙니다.**
- (다) <mark>알림이 나지 않습니다.</mark>
  - 이 규칙은 실패한 이벤트만 주소별로 세어 5번 이상인지 봅니다. 4번 실패한 주소는 기준(5번)보다 적고, 5번째의 성공은 세는 대상이 아닙니다. 그래서 그 주소 하나만 있다면 단계 3 이 비어 알림이 나지 않습니다. 샘플에서 단계 3 에 나오는 것은 203.0.113.50 이 따로 있기 때문입니다.
  - 그래서 담당자는 이 접속이 있었다는 것을 알림으로는 알 수 없습니다. <mark>알림이 없다는 것은 안전하다는 뜻이 아니라 「이 규칙의 조건을 충족하지 않았다」는 뜻일 뿐</mark>입니다.
  - 알림 기준(5번) 미만으로 천천히 시도하는 공격도 이 규칙의 조건을 충족하지 않습니다. 그래서 <mark>「알림 없음 ≠ 안전」</mark>입니다.

**왜**

- <mark>로그인 실패 5번을 사람이 57개 이벤트에서 직접 찾으면 놓치기 쉽습니다.</mark> 조건 두 개와 주소별 센 값을 이어 쓰면 몇 줄로 끝나고, 이벤트가 수만 개여도 같은 코드입니다.

**자주 틀리는 곳**

| 실수 | 나오는 것 | 고치는 법 |
|---|---|---|
| ① 에서 `&` 대신 `and` 로 이음 | `ValueError` 오류 | 열끼리는 `&` 로 잇습니다 |
| ② 에서 `>=` 대신 `>` 를 씀 | 오류는 없지만 단계 3이 `Series([], dtype: int64)` | 「5번 이상」은 `>=` 로 씁니다 |

- **두 조건을 이을 때 `&` 대신 `and` 를 쓰면 `ValueError` 오류가 납니다.**
  - 실행하면 다음 오류가 납니다(<mark>`The truth value of a Series is ambiguous`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise2-3_run.py", line 4, in <module>
    login_failures = pick_login_failures(events)  # 로그인 실패 이벤트만 골라낸다
  File "…/anomaly_detection/login_detection.py", line 29, in pick_login_failures
    both_true = is_login and is_fail  # & 대신 and 를 썼다
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.item(), a.any() or a.all().
```

  - 줄 번호는 사람마다 다릅니다.

**관제에서는**

- 로그인 실패 규칙의 알림에는 보통 주소와 횟수, 실패 뒤 성공이 있었는지가 함께 표시됩니다. <mark>성공이 있었다면 계정이 탈취됐을 수 있어 우선순위가 올라갑니다.</mark>

---

## 응용 2-1 정답

> 여유가 되면 해 보세요. 여기부터는 **응용(여유가 되면)** 정답입니다. 핵심 실습 정답은 앞의 실습 2-1 ~ 2-3 정답에 있습니다.

 **터미널에 입력합니다.**

```bash
pwd
python apply2-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python apply2-1_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 네 함수입니다.

① `load_daily_failures` 안

```python
    daily = pd.read_csv(path)  # CSV 파일을 읽어 표로 만든다 — 한 행이 하루
```

② `average_failures` 안

```python
    daily_failed_logins = daily["failed_logins"]  # failed_logins 열만 꺼낸다 — 하루 실패 횟수 7개가 나열된 열
    average = daily_failed_logins.mean()          # 7개의 평균을 구한다
```

③ `maximum_failures` 안

```python
    daily_failed_logins = daily["failed_logins"]  # failed_logins 열만 꺼낸다 — 하루 실패 횟수 7개가 나열된 열
    maximum = daily_failed_logins.max()           # 7개 중 가장 큰 값을 구한다
```

④ `make_limit` 안

```python
    limit = maximum + 1  # 평소 최댓값보다 1 큰 숫자를 기준으로 삼는다
```

**결과**

- (가) 출력은 다음과 같고, 하루 평균은 <mark>**2.4번**</mark>, 최댓값은 <mark>**4번**</mark>, 알림 기준은 <mark>**5번 이상**</mark>입니다.

```
--- 단계 1: 지난 7일 하루 로그인 실패 횟수
         date  failed_logins
0  2026-10-26              2
1  2026-10-27              3
2  2026-10-28              1
3  2026-10-29              4
4  2026-10-30              2
5  2026-10-31              3
6  2026-11-01              2
--- 단계 2: 하루 평균 2.4 번
--- 단계 3: 하루 최대 4 번
--- 단계 4: 알림 기준(임계값) 5 번 이상
```

- (나) ① 평균(2.4번) 이상인 날은 10/27(3번) · 10/29(4번) · 10/31(3번)으로 7일 중 **3일**입니다.
  - ② 평균을 기준으로 하면 지난 7일 중 위 3일에 알림이 발생하고, <mark>이 3일은 모두 평소와 같은 평범한 날입니다.</mark> 평범한 날에도 알림이 나서 담당자가 알림에 익숙해지고 진짜 알림도 무시하게 됩니다.
  - ③ 최댓값보다 1 큰 숫자(5번)를 기준으로 하면 지난 7일 중 알림이 발생한 날이 **0일**입니다. <mark>평소에는 알림이 나지 않고, 평소보다 많아졌을 때만 알림이 나게 하려는 것입니다.</mark>
- (다) <mark>12번이 섞이면 최댓값은 4번에서 12번이 되고, 알림 기준은 5번에서 13번이 됩니다.</mark> <mark>그러면 5 ~ 12번 실패는 알림이 나지 않아 놓칩니다.</mark>
  - <mark>7일 중 하루만 평소와 달라도 평소 최댓값이 커져서 알림 기준이 높아집니다.</mark> 지난 7일 표가 7일 치뿐이라 그 하루의 영향을 크게 받습니다.
  - 그래서 지난 7일 표에 평소와 다른 날이 섞이지 않았는지 확인하고, 며칠 쓴 뒤에는 새 데이터로 다시 구합니다.

**왜**

- <mark>평소를 구해서 기준을 정하면 숫자에 근거가 생깁니다.</mark> 「왜 5번인가」에 「지난 7일 중 가장 많은 날이 4번이었다」로 답할 수 있습니다.

**자주 틀리는 곳**

| 실수 | 나오는 것 | 고치는 법 |
|---|---|---|
| 열 이름을 `failed_login` 처럼 틀림 | `KeyError` 오류 | **열 이름은 파일 첫 줄의 `failed_logins` 와 정확히 같아야 합니다.** |
| `daily_failed_logins.mean` 처럼 괄호를 뺌 | 값이 아니라 메서드가 담겨서, 실행 파일의 `round(average, 1)` 에서 `TypeError` | `.mean()` · `.max()` 처럼 괄호를 붙여 호출합니다 |

- 열 이름을 틀리면 `KeyError` 오류가 납니다.
  - 실행하면 다음 오류가 납니다(<mark>`KeyError: 'failed_login'`</mark> 처럼 열 이름이 나오면 이 실수입니다).

```
Traceback (most recent call last):
KeyError: 'failed_login'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "…/anomaly_detection/apply2-1_run.py", line 7, in <module>
    average = average_failures(daily)  # 하루 평균을 구한다
  File "…/anomaly_detection/baseline.py", line 22, in average_failures
    daily_failed_logins = daily["failed_login"]  # 열 이름을 잘못 썼다
KeyError: 'failed_login'
```

  - 줄 번호는 사람마다 다릅니다.
- `mean` 과 `max` 는 **뒤에 괄호를 붙여 호출하는 메서드입니다.**

**관제에서는**

- <mark>알림 기준은 몇 주마다 최근 데이터로 다시 구합니다.</mark> 기준을 구한 날짜와 이유를 남겨 두어야 나중에 바꿀 때 근거가 됩니다.

---

## 응용 2-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python apply2-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python apply2-2_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 함수입니다.

① `classify_event` 안

```python
    if result == "실패" and action == "POST /login":  # 로그인 요청이 실패했으면
        return "비정상 로그인"                        # 비정상 로그인으로 분류한다
    if result == "실패" and "/admin" in action:       # 관리자 경로 요청이 실패했으면
        return "비인가 접근"                          # 비인가 접근으로 분류한다
```

② `count_types` 안

```python
    event_list = events.to_dict("records")  # 표를 딕셔너리 리스트로 바꾼다 — 이벤트 하나가 딕셔너리 하나
```

**결과**

- (가) 출력은 다음과 같고, 비정상 로그인 <mark>**5**</mark>, 비인가 접근 <mark>**3**</mark>, 기타 실패 <mark>**15**</mark>, 정상 <mark>**34**</mark>(합계 57)입니다.

```
--- 단계 1: 유형별 이벤트 수
비정상 로그인 5
비인가 접근 3
기타 실패 15
정상 34
--- 단계 2: 전체 이벤트 57 개
```

- (나) 「기타 실패」 15개에는 <mark>서로 다른 일이 섞여 있습니다.</mark> `server`(판정 서버) 실패 9개, `web`(웹 서버) 실패 5개, `saas`(SaaS) 실패 1개입니다.

  | 소스 | 누가 | 무엇을 | 개수 |
  |---|---|---|---|
  | `server` | gaeun | `ACCOUNT:CHANGE` | 3 |
  | `server` | dami | `SALES:QUERY` | 3 |
  | `server` | dami | `SALES:CHANGE` | 1 |
  | `server` | seoyeon | `SETTLE:QUERY` | 1 |
  | `server` | seoyeon | `SALES:CHANGE` | 1 |
  | `web` | 198.51.100.90 | `/.env` · `/wp-login.php` · `/phpmyadmin` 을 차례로 요청 | 3 |
  | `web` | 198.51.100.21 · 198.51.100.34 | 페이지 요청 실패(`/board/99` · `/report`) | 2 |
  | `saas` | jiwoo | `login` | 1 |

  - 198.51.100.90 은 09:20:10 ~ 09:20:12 에 세 경로를 차례로 요청했습니다.
  - <mark>하나로 묶으면 이 일들이 모두 같은 유형으로 보여서, 담당자가 대응을 정할 수 없습니다.</mark> 예를 들어 같은 사용자의 계정 변경이 3번 실패한 것과 `/.env` · `/wp-login.php` · `/phpmyadmin` 을 차례로 요청한 것은 대응이 전혀 다릅니다. 그래서 다음 Unit 3 은 로그 종류마다 먼저 확인할 일을 따로 찾습니다.
- (다) 「기타 실패」를 맨 위에 두면 결과가 실패인 이벤트 23개가 모두 먼저 조건을 충족해서 **기타 실패 23개**가 되고, 비정상 로그인과 비인가 접근은 **0개**가 됩니다. 정상은 34개 그대로입니다.
  - 담당자는 로그인 실패와 관리자 경로 요청 실패를 구분할 수 없게 되어, 비밀번호 대응과 접근 차단 중 무엇을 할지 정하지 못합니다.
  - 먼저 조건을 충족한 규칙에서 멈추기 때문입니다. <mark>좁은 조건(로그인 실패, 관리자 경로)을 위에 두고 넓은 조건(모든 실패)을 아래에 두어야 유형이 나뉩니다.</mark>

**왜**

- <mark>유형 이름을 정하는 규칙은 위에서부터 차례로 보고 먼저 조건을 충족하는 것을 씁니다.</mark> 로그인 실패를 먼저 보고, 그다음 관리자 경로를 보고, 나머지 실패를 「기타 실패」로 모읍니다.

**자주 틀리는 곳**

| 실수 | 나오는 것 | 고치는 법 |
|---|---|---|
| `to_dict("records")` 를 빼고 `event_list = events` 로 씀 | `for` 가 이벤트가 아니라 **열 이름**을 하나씩 꺼내서 `TypeError` | `event_list = events.to_dict("records")` 로 씁니다 |
| `if` 에 `and` 없이 `result == "실패"` 만 씀 | <mark>모든 실패가 첫 번째 규칙의 조건을 충족해 「비정상 로그인」으로 나옵니다.</mark> | 두 조건을 `and` 로 잇습니다 |

- `to_dict("records")` 를 빼면 실행할 때 오류가 납니다.
  - 실행하면 다음 오류가 납니다(<mark>`string indices must be integers`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/apply2-2_run.py", line 4, in <module>
    type_event_counts = count_types(events)  # 유형별로 센다
  File "…/anomaly_detection/classify.py", line 42, in count_types
    action = event["action"]  # 그 이벤트의 행동
TypeError: string indices must be integers, not 'str'
```

  - 줄 번호는 사람마다 다릅니다.

**관제에서는**

- 유형 규칙은 운영하면서 계속 고칩니다. <mark>「기타」가 너무 크면 규칙이 부족하다는 신호입니다.</mark>

---
