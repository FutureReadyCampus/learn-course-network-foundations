---
id: m4-u03-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/100_day02_pm_pandas_basics.md
  mission_id: GichanSource.m4-1103-pm-pandas-basics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답을 읽는 방법

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## 실습 3-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise3-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise3-1_run.py` 파이썬으로 실행 파일 실행

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 세 함수입니다.

① `load_events` 안

```python
    events = pd.read_json(path)  # 파일을 읽어 표로 만든다
```

② `describe_events` 안

```python
    times = events["time"]  # time 열 하나를 꺼낸다
```

③ `count_values` 안

```python
    values = table[column]                      # column 열 하나를 꺼낸다
    value_event_counts = values.value_counts()  # 값별 개수를 센다
```

<h2>결과</h2>

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
  - 소스마다 전체 이벤트 수가 다릅니다(web 28 · server 15 · saas 14). 전체 중 실패의 비율로 보면 web 13/28 = 약 46%, server 9/15 = 60%, saas 1/14 = 약 7% 입니다.
  - <mark>비율로는 server 가 가장 높습니다.</mark> 개수는 전체 규모의 영향을 받으므로, 소스끼리 비교할 때는 전체 대비 비율도 함께 봅니다.
- (다) 예상은 이렇습니다.
  - 사용자 이름으로 세려 해도 <mark>web 실패 13개는 `user` 가 비어 있어서 들어갈 사용자가 없습니다</mark>. web 실패 13개가 사용자별로 세어지지 않는다는 것을 실습 3-2에서 확인합니다.
  - 대신 `ip` 열을 봅니다. 같은 주소에서 실패가 여러 번 난 것을 찾으면 누구인지는 몰라도 같은 대상이 반복했는지 알 수 있습니다.

<h2>왜</h2>

- <mark>이벤트를 표로 읽으면 「걸러 내기 → 세기」가 몇 줄로 끝나고, 이벤트가 57개일 때나 5만 개일 때나 같은 코드를 씁니다.</mark>
  - 조건 비교(`==`)는 줄마다 `True` 또는 `False` 를 만들고, `표[조건]` 은 `True` 인 행만 남깁니다.

<h2>자주 틀리는 곳</h2>

- **열 이름을 틀리면 `KeyError` 오류가 납니다.** `events["time"]` 을 `events["times"]` 처럼 쓰면 표에 없는 열 이름이라서 `KeyError` 가 납니다.
  - 실행하면 다음 오류가 납니다(<mark>`KeyError: 'times'`</mark> 처럼 틀린 열 이름이 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise3-1_run.py", line 4, in <module>
    shape, first_times = describe_events(events)  # 표 크기와 time 열의 처음 3개를 구한다
  File "…/anomaly_detection/events_basic.py", line 23, in describe_events
    times = events["times"]  # time 열 하나를 꺼낸다
KeyError: 'times'
```

  - 줄 번호는 사람마다 다릅니다. 열 이름은 파일에 적힌 키와 똑같이 써야 합니다. 판다스 안쪽 파일의 줄은 길어서 생략했습니다.
- `count_values` 에서 `values.value_counts()` 의 괄호를 빼면 오류는 나지 않지만 개수가 아니라 `<bound method …>` 가 나옵니다. **`value_counts` 는 뒤에 괄호를 붙여 호출하는 메서드입니다.**

<h2>관제에서는</h2>

- 관제 도구의 「실패 이벤트 수 · 소스별 분포」 화면은 이 계산을 계속 다시 합니다. 분포를 보고 어느 소스부터 조사할지 정합니다.
  - 숫자는 「살펴볼 곳」을 알려 줄 뿐이고, <mark>개수가 많다고 곧 공격이라는 뜻은 아닙니다</mark>.

---

## 실습 3-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise3-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise3-2_run.py` 파이썬으로 실행 파일 실행

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 두 함수입니다.

① `count_by_user` 안

```python
    grouped = failed.groupby("user")                                         # user 가 같은 행끼리 묶는다
    user_fail_counts = grouped.size()                                        # 그룹마다 행이 몇 개인지 센다
    sorted_user_fail_counts = user_fail_counts.sort_values(ascending=False)  # 큰 값부터 순서대로 정렬한다
```

② `count_by_hour` 안

```python
    grouped = failed.groupby("hour")   # hour 가 같은 행끼리 묶는다
    hour_fail_counts = grouped.size()  # 그룹마다 행이 몇 개인지 센다
```

<h2>결과</h2>

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

- (나) 9시의 13개는 실습 3-1 단계 3의 web 실패 13개와 같은 숫자입니다. <mark>웹 서버에서 난 실패가 모두 9시에 났다는 단서</mark>입니다.
  - <mark>숫자가 같다는 것만으로는 확정할 수 없습니다.</mark> 확정하려면 `failed_events.csv` 를 열어 `hour` 가 9인 행의 `source` 를 봅니다(실제로 13개 모두 `web` 입니다).
  - 웹 서버 로그에는 사용자가 없으므로, <mark>먼저 확인할 것은 같은 시간대의 `ip`</mark> 입니다. 같은 주소가 로그인 실패를 반복했는지, 없는 주소를 차례로 요청했는지 봅니다.
  - 한 시간대에 실패가 많이 났을 때는 이어서 세 가지를 봅니다. 어느 소스에서 났는지, 같은 주소나 같은 사용자가 반복했는지, 그 직후에 성공한 이벤트가 있는지입니다.
- (다) 사용자별 합계는 4 + 3 + 2 + 1 = 10이고 실패한 이벤트는 23개라서 <mark>**13개**</mark>가 빠졌습니다.
  - 빠진 13개는 `user` 가 비어 있는 웹 서버 이벤트입니다. `groupby("user")` 가 비어 있는 값의 행을 그룹에 넣지 않았기 때문입니다.
  - 모르고 사용자별 숫자만 보면 <mark>「실패가 10개뿐」이라고 잘못 판단하거나, 가장 많은 실패(웹 서버 13개)를 아예 놓칩니다</mark>.

<h2>왜</h2>

- <mark>묶어서 세면 전체 합계 숫자에서는 보이지 않던 차이가 드러납니다.</mark> 사용자별 · 시간대별 집계는 평소 기준과 비교할 때의 출발점입니다.
  - 시각은 문자열이면 「시」를 꺼낼 수 없으므로 시각 값으로 바꾼 뒤에 `.dt.hour` 를 씁니다.

<h2>자주 틀리는 곳</h2>

- **열 이름을 틀리면 `KeyError` 오류가 납니다.** `groupby("user")` 를 `groupby("users")` 처럼 쓰면 표에 없는 열 이름이라서 `KeyError` 가 납니다.
  - 실행하면 다음 오류가 납니다(<mark>`KeyError: 'users'`</mark> 처럼 틀린 열 이름이 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise3-2_run.py", line 8, in <module>
    by_user = count_by_user(failed)  # 실패 횟수를 사용자별로 센다
  File "…/anomaly_detection/events_time.py", line 31, in count_by_user
    grouped = failed.groupby("users")  # user 가 같은 행끼리 묶는다
KeyError: 'users'
```

  - 줄 번호는 사람마다 다릅니다. 판다스 안쪽 파일의 줄은 길어서 생략했습니다.
- `sort_values` 에서 `ascending=False` 를 빼면 **오류는 나지 않지만 작은 값부터 나옵니다.** 단계 1 의 첫 줄이 dami 가 아니라 jiwoo 가 됩니다.

<h2>관제에서는</h2>

- 집계 결과는 알림을 만들 때 근거가 되는 숫자입니다. 근거가 된 이벤트를 파일로 남기면 담당자가 알림이 왜 났는지 확인할 수 있습니다.
  - <mark>집계에서 빠진 값(`null`)이 있는지 함께 확인하는 것</mark>이 습관입니다.

---

## 정답 마무리

 **터미널에 입력합니다.**

```bash
cd ..
pwd
git status
```
- 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 있는 폴더의 위치 확인 · `git status` 올릴 파일의 상태를 봄

<mark>`.env` 나 `.venv` 가 없는 것을 확인한 뒤에</mark> 아래를 칩니다.

```bash
git add .
git commit -m "Add anomaly detection unit 3 pandas basics"
git push
```
- 명령 풀이: `git add .` 바뀐 파일을 올릴 대상에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림

<h2>결과</h2>

- (가) 한 예: 「`.env` · `.venv` 는 보이지 않았다」. 보였다면 `.gitignore` 에 `.env`(또는 `.venv`) 한 줄을 적고 저장한 뒤 `git status` 를 다시 쳤다고 적습니다.

<h2>왜</h2>

- <mark>올리기 전에 올라갈 파일을 확인해야 비밀 키가 섞이지 않습니다.</mark>

<h2>자주 틀리는 곳</h2>

- **`.env` 가 보이는데 그대로 `git add .` 를 하는 실수가 가장 위험합니다.**
  - `cd ..` 를 두 번 쳐서 `security-agent-toolkit` 바깥으로 나가는 경우도 있습니다. `pwd` 로 확인합니다.

<h2>관제에서는</h2>

- 분석 코드와 샘플 데이터는 같은 저장소에 함께 남겨, <mark>어느 코드로 어떤 데이터를 분석했는지 이력으로 추적합니다</mark>.
