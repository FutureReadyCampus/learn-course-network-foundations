---
id: m4-u03-l03
title: 실습 3-2 · 실패를 묶어 세고 CSV로 저장
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/100_day02_pm_pandas_basics.md
  mission_id: GichanSource.m4-1103-pm-pandas-basics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 3-2 · 실패를 묶어 세고 CSV로 저장

## 목표: 실패 집계표와 CSV

> **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「실패한 이벤트가 23개라는 것은 알았습니다. 이제 두 가지를 알려 주세요.
>
> - 누가 얼마나 실패했는지: 사용자별로, 많은 순서대로
> - 하루 중 언제 많이 났는지: 몇 시에 몇 개인지
>
> 그리고 실패한 이벤트만 따로 파일로 저장해 주세요. 담당자가 엑셀로 열어 근거를 확인합니다.」
> - **왜 중요한가**: <mark>실패 23개를 전체 합계로만 보면 평범한 숫자입니다.</mark> 사용자별 · 시간대별로 묶으면 한 사용자나 한 시간대에 많이 난 실패가 드러납니다. 근거 이벤트를 파일로 저장해야 담당자가 알림이 왜 났는지 확인할 수 있습니다. Unit 4에서 평소 기준을 세우는 기초 계산이기도 합니다.

## 왜 실패를 묶어서 세는가

1. 실습 3-1에서는 열 하나의 값별 개수를 셌습니다(`value_counts`). 이번에는 **조건에 맞는 행들을 다른 열 기준으로 묶어** 셉니다. 예를 들어 「실패한 이벤트를 사용자별로」 묶어 세는 것입니다.
2. `time` 열의 `"2026-11-02 09:01:05"` 는 문자열이라서 「시」만 꺼낼 수 없습니다. <mark>그래서 먼저 날짜·시간 값으로 바꾼 뒤 「시」(예: 9)를 꺼냅니다.</mark>
3. 분석한 결과(실패한 이벤트)는 **CSV(씨에스브이, 값을 쉼표(,)로 구분해 적은 텍스트 파일)** 로 저장하면 엑셀 같은 도구로 열어 볼 수 있습니다.

## 2.1 묶고 세기 · 시간 다루기 · 저장하기

**판다스 문법 상자 — 같은 값끼리 묶기**

**<mark>`groupby("열")`</mark> 는 그 열의 값이 같은 줄끼리 묶습니다**

「소스별로 실패가 몇 개인가」를 알려면 먼저 `source` 값이 같은 행끼리 그룹(group)으로 묶어야 합니다. <mark>`groupby` 는 이 묶기만 하고, 개수는 세지 않습니다.</mark>

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {  # 실패한 이벤트만 적은 연습용 작은 데이터
    "source": ["web", "server", "web", "saas", "web", "server"],  # source 열에 들어갈 값들
    "action": ["GET /board", "POST /login", "GET /report", "login", "GET /admin", "ACCOUNT:CHANGE"],  # action 열에 들어갈 값들
}
failed = pd.DataFrame(data)  # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
print(failed)  # 표를 출력한다
grouped = failed.groupby("source")  # source 값이 같은 줄끼리 묶는다 — 아직 개수가 아니라 그룹만 만든 상태
print(grouped)  # 묶은 결과를 출력한다 — 개수가 아니라 `DataFrameGroupBy` 라는 이름이 나온다
```

실행 결과:

```
   source          action
0     web      GET /board
1  server     POST /login
2     web     GET /report
3    saas           login
4     web      GET /admin
5  server  ACCOUNT:CHANGE
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x10a3a7430>
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
group_count = len(grouped)  # 그룹이 몇 개인지 센다
print(group_count)  # 3 이 나온다 — saas · server · web 세 그룹
```

실행 결과:

```
3
```

- 읽는 법: <mark>첫 번째 출력에는 그룹의 개수나 내용이 없습니다.</mark> 묶기만 했고 아직 세지 않았기 때문입니다. `0x` 로 시작하는 부분은 실행할 때마다 달라도 괜찮습니다. <mark>두 번째 출력 `3` 은 그룹이 3개라는 뜻</mark>입니다. `source` 값이 `saas` · `server` · `web` 세 가지이기 때문입니다.
- <mark>묶기만 해서는 그룹마다 몇 개인지 알 수 없습니다.</mark> 개수는 다음 상자의 `.size()` 로 셉니다.

**판다스 문법 상자 — 그룹마다 행 수 세기**

**<mark>`.size()`</mark> 는 그룹마다 행이 몇 개인지 셉니다**

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {  # 실패한 이벤트만 적은 연습용 작은 데이터
    "source": ["web", "server", "web", "saas", "web", "server"],  # source 열에 들어갈 값들
    "action": ["GET /board", "POST /login", "GET /report", "login", "GET /admin", "ACCOUNT:CHANGE"],  # action 열에 들어갈 값들
}
failed = pd.DataFrame(data)  # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
grouped = failed.groupby("source")  # source 값이 같은 줄끼리 묶는다

source_fail_counts = grouped.size()  # 그룹마다 행이 몇 개인지 센다 — 그룹 이름이 왼쪽에 나온다
print(source_fail_counts)  # saas 1 · server 2 · web 3 (그룹 이름 순서)
```

실행 결과:

```
source
saas      1
server    2
web       3
dtype: int64
```

- 읽는 법: 왼쪽이 그룹 이름(`source` 값), 오른쪽이 그 그룹의 행 수입니다. 그룹 이름은 가나다 · 알파벳 순서로 나옵니다. 1 + 2 + 3 = 6 이라 표의 행 수와 같습니다.
- 개수만 세려면 실습 3-1의 `value_counts()` 로도 같은 결과가 나옵니다. <mark>그래도 `groupby` 를 배우는 것은 Unit 4에서 그룹마다 평균 같은 다른 계산도 하기 때문입니다.</mark> 이번 Unit에서는 개수(`size`)만 씁니다.

**알아 둘 것 — 묶고 세기를 한 줄로 쓰기**

`failed.groupby("source").size()` 처럼 묶기와 세기를 한 줄로 이어 쓰기도 합니다. <mark>실습 3-2 에서는 줄마다 하나씩 나눠 쓰고</mark>, 이 모양은 읽기만 합니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

results = events["result"]  # result 열만 꺼낸다
is_fail = results == "실패"  # 행마다 실패면 True, 아니면 False 를 만든다
failed = events[is_fail]  # True 인 행만 남겨 새 표(failed)를 만든다 — 실패한 이벤트만 담긴다

source_fail_counts = failed.groupby("source").size()  # 묶고(groupby) 바로 이어서 그룹마다 행 수를 센다(size) — 앞의 두 줄과 같은 일이다
print(source_fail_counts)  # saas 1 · server 9 · web 13 (그룹 이름 순서)
```

실행 결과:

```
source
saas       1
server     9
web       13
dtype: int64
```

- 읽는 법: 두 줄로 나눠 쓴 앞의 결과와 같습니다. `failed.groupby("source")` 가 만든 그룹에 바로 `.size()` 를 붙여서, 중간 이름(`grouped`)을 따로 만들지 않을 뿐입니다.

**판다스 문법 상자 — 큰 값부터 정렬하기**

**<mark>`.sort_values(ascending=False)`</mark> 는 값이 큰 것부터 다시 정렬합니다**

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {  # 실패한 이벤트만 적은 연습용 작은 데이터
    "source": ["web", "server", "web", "saas", "web", "server"],  # source 열에 들어갈 값들
    "action": ["GET /board", "POST /login", "GET /report", "login", "GET /admin", "ACCOUNT:CHANGE"],  # action 열에 들어갈 값들
}
failed = pd.DataFrame(data)  # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
grouped = failed.groupby("source")  # source 값이 같은 줄끼리 묶는다
source_fail_counts = grouped.size()  # 그룹마다 행이 몇 개인지 센다 — saas 1 · server 2 · web 3
print(source_fail_counts)  # 정렬하기 전의 개수를 출력한다
```

실행 결과:

```
source
saas      1
server    2
web       3
dtype: int64
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
sorted_source_fail_counts = source_fail_counts.sort_values(ascending=False)
# ascending=False 는 개수가 큰 그룹부터 정렬한다
print(sorted_source_fail_counts)  # web 3 · server 2 · saas 1
```

실행 결과:

```
source
web       3
server    2
saas      1
dtype: int64
```

- 읽는 법: 값은 앞의 묶어 세기와 같고 <mark>행 순서만 바뀐 것</mark>입니다. 그룹 이름 순서(saas → server → web)에서 개수가 큰 순서(web → server → saas)가 되었습니다.
- `ascending=False` 는 큰 값부터 정렬하라는 뜻이고, <mark>이 부분을 빼면 작은 값부터 나옵니다</mark>.

**알아 둘 것 — 정렬까지 이어 쓴 모양도 읽을 수 있어야 합니다**

묶기, 세기, 정렬은 실무에서 아래처럼 점으로 이어 한 줄에 쓰기도 합니다. 왼쪽부터 차례로 하나씩 일어난다고 읽으면 됩니다. 직접 쓰지 않고 읽기만 합니다. 자세한 쓰임은 다음에 차차 배웁니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

results = events["result"]  # result 열만 꺼낸다
is_fail = results == "실패"  # 행마다 실패면 True, 아니면 False 를 만든다
failed = events[is_fail]  # True 인 행만 남겨 새 표(failed)를 만든다

# 묶기 → 세기 → 큰 값부터 정렬을 한 줄로 이은 모양
sorted_source_fail_counts = failed.groupby("source").size().sort_values(ascending=False)
print(sorted_source_fail_counts)  # web 13 · server 9 · saas 1
```

실행 결과:

```
source
web       13
server     9
saas       1
dtype: int64
```

**알아 둘 것 — 문자열 시각을 시각 값으로 바꾸기**

`pd.to_datetime` 은 `"2026-11-02 09:01:05"` 같은 문자열을 날짜·시간 값으로 바꿉니다. <mark>날짜·시간 값이어야 「시」나 「분」 같은 부분만 꺼낼 수 있습니다.</mark> 실습 3-2 의 `add_hour` 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다. 자세한 쓰임은 다음에 차차 배웁니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

time_texts = events["time"]  # time 열만 꺼낸다 — 문자열 시각 57개
times = pd.to_datetime(time_texts)  # 문자열 시각 57개를 시각 값으로 바꾼다
first_times = times.head(3)  # 처음 3개만 남긴다
print(first_times)  # 시각 3개와 열 이름, 종류(datetime64)가 나온다
```

실행 결과:

```
0   2026-11-02 02:14:08
1   2026-11-02 09:01:05
2   2026-11-02 09:01:06
Name: time, dtype: datetime64[ns]
```

- 읽는 법: 겉모습은 같지만, 맨 아래 <mark>`datetime64` 는 이 열이 날짜·시간 값으로 바뀌었다는 표시</mark>입니다.

**알아 둘 것 — 시각 값에서 「시」만 꺼내기**

<mark>`.dt.hour` 는 시각 값에서 「시」만 숫자로 꺼냅니다.</mark> 실습 3-2 의 `add_hour` 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다. 자세한 쓰임은 다음에 차차 배웁니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

time_texts = events["time"]  # time 열만 꺼낸다
times = pd.to_datetime(time_texts)  # 문자열 시각을 시각 값으로 바꾼다

hours = times.dt.hour  # 시각 값에서 「시」만 숫자로 꺼낸다(02:14 → 2, 09:01 → 9)
first_hours = hours.head(3)  # 처음 3개만 남긴다
for hour in first_hours:  # 처음 3개를 하나씩 꺼낸다
    print(hour)  # 2, 9, 9 가 한 줄씩 나온다
```

실행 결과:

```
2
9
9
```

- 읽는 법: 첫 이벤트(02:14)는 2, 둘째와 셋째(09:01)는 9입니다.

**알아 둘 것 — 표에 새 열 붙이기**

`표["새 열 이름"] = 값` 은 <mark>표 맨 오른쪽에 새 열을 붙입니다</mark>. 실습 3-2 의 `add_hour` 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다. 자세한 쓰임은 다음에 차차 배웁니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

time_texts = events["time"]  # time 열만 꺼낸다
times = pd.to_datetime(time_texts)  # 문자열 시각을 시각 값으로 바꾼다
hours = times.dt.hour  # 시각 값에서 「시」만 숫자로 꺼낸다

events["hour"] = hours  # 표 맨 오른쪽에 hour 라는 새 열을 붙인다
shape = events.shape  # 붙인 뒤 표의 크기를 꺼낸다
print(shape)  # (57, 7) — 열이 6개에서 7개가 되었다
```

실행 결과:

```
(57, 7)
```

- 읽는 법: 행은 그대로 57개이고, <mark>열이 6개에서 7개로 늘었습니다</mark>.

**알아 둘 것 — 표를 CSV 파일로 저장하기**

`표.to_csv(파일 이름, index=False)` 는 표를 엑셀로도 열 수 있는 CSV 파일(값을 쉼표(,)로 구분해 적은 텍스트 파일)로 저장합니다. 실습 3-2 의 `save_failed` 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다. 자세한 쓰임은 다음에 차차 배웁니다.

```python
failed.to_csv("failed_events.csv", index=False)  # 표를 failed_events.csv 파일로 저장한다 — index=False 는 행 번호를 저장하지 않는다는 뜻
```

- 실행하면 같은 폴더에 `failed_events.csv` 파일이 생깁니다. VS Code 로 열면 첫 줄은 열 이름이고, 둘째 줄부터 이벤트가 한 줄씩 있습니다.
- 엑셀로 열었을 때 한글이 깨져 보이면 VS Code 로 열어 확인합니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_events` · `pick_failed` | (실습 3-1과 같아서 미리 채움) | 이벤트 표 · 실패한 행만 담은 표 |
| `count_by_user` | 실패한 이벤트 표 | 사용자별 실패 횟수(많은 순서) |
| `add_hour` | 이벤트 표 | `hour` 열이 더해진 표 |
| `count_by_hour` | 실패한 이벤트 표 | 시간대별 실패 횟수 |
| `save_failed` | 표와 파일 이름 | 없음(파일로 저장) |

- **직접 쓰는 곳은 두 함수**(번호 1 ~ 5)입니다. 나머지는 미리 채웠습니다. `load_events` 와 `pick_failed` 는 실습 3-1과 같고, `add_hour` 와 `save_failed` 는 아직 배우지 않은 문법이라 읽기만 합니다.
  - `count_by_user`(1 ~ 3번): 사용자별로 묶어 세고 큰 순서로 정렬합니다.
  - `count_by_hour`(4 · 5번): 시간대별로 묶어 셉니다. 묶기와 세기는 1 · 2번과 같고 열 이름만 다릅니다.
  - `add_hour` · `save_failed`(미리 채움): 시각을 바꿔 `hour` 열을 더하고, 실패한 이벤트를 CSV 로 저장합니다. 읽어 보기만 합니다.

## 2.2 묶을 때 비어 있는 값은 빠집니다

- `groupby("user")` 는 `user` 가 비어 있는 행(`null`)을 그룹에 넣지 않고 **제외합니다.** <mark>웹 서버 이벤트는 `user` 가 없어서 사용자별 개수에 들어가지 않습니다.</mark>
- 그래서 <mark>사용자별 개수를 모두 더하면 실패한 이벤트 전체 개수보다 작아질 수 있습니다</mark>. 숫자를 읽을 때 「빠진 행이 있는가」를 함께 봅니다.
- <mark>오류 메시지는 나오지 않으므로 모르고 지나치기 쉽습니다.</mark>

## 실습 3-2 · 실패를 묶어 세고 CSV로 저장

**이런 상황이 있습니다**

- **지금은**: 실패가 23개라는 것만 알고, 누구에게 많이 났는지, 언제 많이 났는지는 모릅니다.
- **그래서 만드는 것**: `events_time.py` 입니다.
  - 실패를 사용자별로 묶어 많은 순서로 셉니다.
  - 시각에서 「시」를 꺼내 시간대별로 셉니다.
  - 실패한 이벤트를 CSV 파일로 저장합니다.
- **실행하면**: 단계 1: 사용자별 실패 횟수, 단계 2: 시간대별 실패 횟수, 단계 3: 저장한 행 수가 나오고 `failed_events.csv` 파일이 만들어집니다.
- **현업에서는**: 알림이 나면 근거 이벤트를 파일로 남겨 담당자가 열어 봅니다. 사용자별 · 시간대별 집계는 평소와 비교할 때의 출발점입니다.

**할 일**

1. **`events_time.py` · `exercise3-2_run.py` 두 파일**을 만들고, `events_time.py` 의 `count_by_user` · `count_by_hour` 에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>사용자별 실패 횟수</mark>(단계 1), <mark>시간대별 실패 횟수</mark>(단계 2), <mark>저장한 파일의 행 수</mark>(단계 3)를 읽습니다.

**`events_time.py`**

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"  # 읽을 정규화 이벤트 파일 이름
FAILED_PATH = "failed_events.csv"  # 실패한 이벤트를 저장할 파일 이름


def load_events(path):  # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)  # 파일을 읽어 표로 만든다
    return events  # 표를 리턴한다


def pick_failed(events):  # 표를 받는 함수
    """실패한 이벤트만 골라 새 표로 만든다.
    무엇이 잘못됐는지 조사할 때 성공한 이벤트는 빼고 보는 데 쓴다.
    """
    results = events["result"]  # result 열 하나를 꺼낸다
    is_fail = results == "실패"  # 행마다 실패면 True, 아니면 False
    failed = events[is_fail]  # True 인 행만 남긴다
    return failed  # 실패한 행만 담은 표를 리턴한다


def count_by_user(failed):  # 실패한 이벤트 표를 받는 함수
    """실패 횟수를 사용자별로 세어 많은 순서로 리턴한다.
    누구에게 실패가 많이 났는지 볼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. failed 를 "user" 열 기준으로 묶어(groupby) grouped 에 담는다
    # 2. grouped.size() 의 결과를 user_fail_counts 에 담는다
    # 3. user_fail_counts 를 큰 값부터 정렬해(sort_values, ascending=False) sorted_user_fail_counts 에 담는다
    return sorted_user_fail_counts  # 많은 순서로 정렬한 개수를 리턴한다


def add_hour(events):  # 표를 받는 함수
    """time 열을 시각으로 바꾸고 「시」만 담은 hour 열을 더한다.
    시간대별로 세기 전에 쓴다.
    """
    times = pd.to_datetime(events["time"])  # 문자열 시각을 시각 값으로 바꾼다
    hours = times.dt.hour  # 시각에서 「시」(0~23)만 꺼낸다
    events["hour"] = hours  # hour 라는 새 열로 표에 더한다
    return events  # hour 열이 더해진 표를 리턴한다


def count_by_hour(failed):  # 실패한 이벤트 표를 받는 함수
    """실패 횟수를 시간대별로 센다.
    실패가 몇 시에 많이 났는지 볼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. failed 를 "hour" 열 기준으로 묶어 grouped 에 담는다
    # 5. grouped.size() 의 결과를 hour_fail_counts 에 담는다
    return hour_fail_counts  # 시간대별 개수를 리턴한다


def save_failed(failed, path):  # 표와 저장할 파일 이름을 받는 함수
    """실패한 이벤트 표를 CSV 파일로 저장한다.
    담당자가 엑셀로 근거를 확인하게 할 때 쓴다.
    """
    failed.to_csv(path, index=False)  # 표를 CSV 파일로 저장한다 — 미리 채운 줄
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 5번은 모두 함수 안이라 앞에 공백 4개입니다.
- 번호 주석이 연달아 붙어 있어도(예: 1 · 2 · 3번), <mark>주석 1번 아래에 코드 한 줄, 주석 2번 아래에 코드 한 줄을 씁니다</mark>.
- **채우기 전에 실행하면 `NameError: name 'sorted_user_fail_counts' is not defined` 오류가 납니다.** 3번까지 쓰지 않았기 때문입니다.

**`exercise3-2_run.py`** — <mark>그대로 붙여 넣습니다.</mark> 직접 쓰는 줄은 없습니다. 이벤트를 읽어 실패만 골라 묶고 저장한 뒤 **세 단계**로 출력합니다. 단계 3에서 `pd.read_csv(파일)` 은 저장한 CSV 를 다시 표로 읽고, `len(표)` 는 그 표의 행 수입니다. 저장이 잘 됐는지 행 수로 확인하는 줄이라 읽기만 합니다.

```python
import pandas as pd  # 저장한 파일을 다시 읽을 수 있게 판다스를 불러온다
from events_time import (
    load_events, add_hour, pick_failed, count_by_user, count_by_hour,
    save_failed, EVENTS_PATH, FAILED_PATH,
)  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)  # 이벤트 파일을 표로 읽는다
events = add_hour(events)  # 시각을 바꾸고 hour 열을 더한다
failed = pick_failed(events)  # 실패한 이벤트만 골라낸다

by_user = count_by_user(failed)  # 실패 횟수를 사용자별로 센다
print("--- 단계 1: 사용자별 실패 횟수")  # 단계 1 시작을 알리는 줄
print(by_user)  # 많은 순서로 출력한다

by_hour = count_by_hour(failed)  # 실패 횟수를 시간대별로 센다
print("--- 단계 2: 시간대별 실패 횟수")  # 단계 2 시작을 알리는 줄
print(by_hour)  # 시간대 순서로 출력한다

save_failed(failed, FAILED_PATH)  # 실패한 이벤트를 CSV 로 저장한다
saved = pd.read_csv(FAILED_PATH)  # 저장한 파일을 다시 읽어 확인한다
saved_count = len(saved)  # 저장된 행이 몇 개인지 센다
print("--- 단계 3: 저장한 파일", FAILED_PATH)  # 단계 3 시작을 알리는 줄
print("저장된 행", saved_count, "개")  # 저장된 행 수를 출력한다
```

**순서**

1. **[VS Code]** 파일 **`events_time.py` · `exercise3-2_run.py`** 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `events_time.py` 에서 **직접 쓰는 곳 다섯 군데**를 씁니다. 2.1 의 판다스 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise3-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise3-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **세 단계**입니다. `--- 단계` 제목 줄은 세지 않고, 단계 1은 6줄, 단계 2는 7줄, 단계 3은 1줄입니다.
5. **[VS Code]** 새로 생긴 `failed_events.csv` 를 열어 첫 줄이 열 이름(`time,source,user,ip,action,result,hour`)인지 보고, <mark>`hour` 가 9 인 행의 `source` 를 봅니다</mark>.
6. **[실습 기록]** `report_u3.md` 의 `## 실습 3-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 실패가 가장 많은 사용자와 횟수, 실패가 가장 많이 난 시간대와 횟수, 저장된 행 수를 적어 주세요.
   - (나) [핵심 질문] 시간대별 결과에서 실패가 가장 많이 난 시간대의 개수를 보세요. 이 개수는 실습 3-1 단계 3의 어느 소스 개수와 같은가요? 그 실패가 어느 소스에서 났는지 적고(근거는 숫자가 같다는 것까지 쓰면 됩니다), 이어서 확인할 것도 적어 주세요.
   - (다) [핵심 질문] 사용자별 실패 횟수를 모두 더하면 실패한 이벤트 전체보다 적습니다. 몇 개가 모자라고 왜 모자란지 적어 주세요. 그리고 이 차이를 모르고 사용자별 숫자만 보면 어떤 잘못된 판단을 할 수 있을지도 적어 주세요.

<!-- answer: 04|실습 3-2 정답 -->

## 실습 3-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 같은 값끼리 묶어 개수 세기 | `grouped = failed.groupby("user")` → `user_fail_counts = grouped.size()` |
| 큰 값부터 정렬 | `sorted_user_fail_counts = user_fail_counts.sort_values(ascending=False)` |
| 문자열 시각을 시각 값으로 | `times = pd.to_datetime(events["time"])` |
| 「시」만 꺼내 새 열로 | `hours = times.dt.hour` → `events["hour"] = hours` |
| CSV 로 저장 | `failed.to_csv(path, index=False)` |
| 비어 있는 값 | `groupby` 는 비어 있는 값(`null`)의 행을 빼고 센다 |

---

## 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기

문제가 아니라 이번 Unit에서 한 일을 저장소에 올리는 마무리입니다. 실습 3-2 마지막 약 10분에 합니다. 어느 터미널을 써도 되고, <mark>`pwd` 로 위치를 먼저 확인한 뒤 결과가 `anomaly_detection` 으로 끝나면 아래 1번의 `cd ..` 를 칩니다</mark>.

**이런 상황이 있습니다**

- **지금은**: 팀장이 「이번 Unit에서 만든 집계 코드와 실패 이벤트 파일을 저장소에 남겨 달라」고 합니다.
- **그래서 하는 것**: `git status` 로 올라갈 파일을 확인한 뒤(**`.env` 같은 비밀 키 파일이 섞이면 안 됩니다**) `git add` → `git commit` → `git push` 순서로 올립니다.
- **끝나면**: 깃허브 저장소의 `anomaly_detection` 폴더에 이번 Unit에서 만든 파일이 보입니다.

**순서**

0. **[터미널]** 이번 Unit에서 만든 파일이 있는지 `anomaly_detection` 폴더에서 확인합니다. `report_u3.md` 의 실습 3-2 칸에서 `답:` 뒤가 비어 있는 질문이 없는지도 봅니다.
   ```bash
   ls
   ```
   - 명령 풀이: `ls` 폴더 안의 파일 이름 보기
   - `normalized_events.json` · `events_basic.py` · `events_time.py` · `exercise3-1_run.py` · `exercise3-2_run.py` · `failed_events.csv` 와 `report_u3.md` 가 보여야 합니다.
1. **[터미널]** `security-agent-toolkit` 폴더로 옮기고 위치를 확인합니다. <mark>결과가 `…/security-agent-toolkit` 으로 끝나야</mark> 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 글씨 줄에 <mark>`.env` 나 `.venv` 가 보이면 올리지 말고</mark>, 아래 안내대로 `.gitignore` 를 고친 뒤 `git status` 를 다시 봅니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - `.venv` 도 같은 방법으로 합니다.
   - `anomaly_detection/__pycache__/` (파이썬이 실행하면서 자동으로 만드는 임시 폴더)가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
3. **[실습 기록]** `report_u3.md` 의 `## 저장소 반영 확인` 아래를 채웁니다. <mark>올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다</mark>.
   - (가) `git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.
   - 앞 실습에서 못 적은 기록 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다. 올린 뒤에 이어서 적어 다시 올려도 됩니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add anomaly detection unit 3 pandas basics"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 대상에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다. <mark>`git pull` 을 입력해 받아 온 뒤 `git push` 를 다시 합니다</mark>
   - `git pull` 뒤에 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다
5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `anomaly_detection` 폴더를 열고, VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 있는 파일들이 깃허브에도 보이는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.
   - 빠진 이름이 있으면 VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 내 PC 에도 있는지 봅니다.
     - 없으면 다른 폴더에 만든 것이니 `anomaly_detection` 안으로 옮기고, `pwd` 로 위치를 확인한 뒤 2번의 `git status` 부터 다시 합니다.

<!-- answer: 04|정답 마무리 -->

## 문제 해결 과정을 블로그에 기록하기

두 실습을 마친 뒤, 실패 이벤트를 어떤 기준으로 집계했고 결과를 어떻게 확인했는지 GitHub 블로그에 기록합니다. `report_u3.md`는 실행 출력과 질문 답을 남기는 기술 실습 기록입니다. 블로그 글에는 문제를 해석하고 근거를 확인한 과정, 선택한 집계 기준과 그 한계를 다른 개발자가 따라갈 수 있도록 정리합니다.

M3 Unit 1에서 만든 `network-study-notes` 저장소의 `_posts` 폴더에 글을 작성합니다. GitHub Pages와 Jekyll을 아직 설정하지 않았다면 [M3 Unit 1의 Jekyll·GitHub Pages 설정 안내](__SITE__/exercises/module/3/unit/1/lesson/1/page/4)를 먼저 따라 합니다.

이번 Unit의 샘플 데이터에서 직접 확인한 사실만 씁니다. 실패 개수만으로 어느 로그가 더 위험하다고 판단할 수 없는 이유, `user`가 비어 있는 웹 이벤트가 사용자별 집계에서 빠지는 점, 시간대 집계에서 확인한 단서를 고를 수 있습니다. 관찰한 사실과 추측을 나누고, 추가로 확인해야 할 자료도 적습니다. AI를 사용했다면 질문과 답 중 직접 실행하거나 자료와 대조한 내용을 요약합니다.

아래 틀을 복사해 `_posts/YYYY-MM-DD-m4-u3-failure-analysis.md`로 저장하고 날짜와 제목을 실제 경험에 맞게 바꿉니다.

<pre class="copyable"><code>---
layout: post
title: "실패 이벤트를 집계할 때 확인한 기준과 한계"
date: YYYY-MM-DD
module: 4
unit: 3
---

&#35;# 문제 상황
어떤 이벤트를 세고 무엇을 확인하려 했나요?

&#35;# 확인한 근거
어떤 표나 실행 결과를 직접 봤나요?

&#35;# 가능한 원인
실패가 몰린 이유로 무엇을 생각했나요? 사실과 추측을 구분합니다.

&#35;# 집계 기준과 이유
어떤 열로 묶어 세었고, 그 기준을 선택한 이유는 무엇인가요?

&#35;# 다시 확인한 결과
CSV와 집계 결과에서 직접 확인한 내용은 무엇인가요?

&#35;# 남은 질문
추가로 확인하려면 어떤 자료가 더 필요할까요?

&#35;# AI 도움 (사용했다면)
어떤 질문을 했고 답변 중 무엇을 직접 확인했나요?
</code></pre>

`network-study-notes` 저장소에서 글을 커밋해 올리고, GitHub Pages에서 새 글을 확인합니다.

```bash
cd ~/network-study-notes
git status --short
git add _posts
git commit -m "Record M4 Unit 3 problem solving"
git push
```

다음 Unit에서는 이번 Unit의 집계 결과를 **평소 기준(baseline)** 과 비교해, 평소보다 많은 로그인 실패와 요청 급증을 찾는 탐지 규칙을 만듭니다.

---

<!-- learn:answers -->
