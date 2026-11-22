---
id: m4-u02-l03
title: 실습 2-2 · 실패를 묶어 세고 CSV로 저장
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/100_day02_pm_pandas_basics.md
  mission_id: GichanSource.m4-1103-pm-pandas-basics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 2-2 · 실패를 묶어 세고 CSV로 저장

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
> - **왜 중요한가**: <mark>실패 23개를 전체 합계로만 보면 평범한 숫자입니다.</mark> 사용자별 · 시간대별로 묶으면 한 사용자나 한 시간대에 많이 난 실패가 드러납니다. 근거 이벤트를 파일로 저장해야 담당자가 알림이 왜 났는지 확인할 수 있습니다. 실습 2-3에서 주소별 로그인 실패를 셀 때도 이 묶어 세기를 씁니다.
> - 이 실습에서 하는 일: 실패한 이벤트를 사용자별 · 시간대별로 묶어 세고, CSV 파일로 저장합니다. 대부분은 미리 채워 두었고, 사용자별로 묶는 줄과 큰 순서로 정렬하는 줄 두 곳만 직접 씁니다.
> - 끝나면 쓰는 것: 보고서 (가) 답. (나) · (다)는 여유가 되면 하는 응용입니다

## 왜 실패를 묶어서 세는가

1. 실습 2-1에서는 열 하나의 값별 개수를 셌습니다(`value_counts`). 이번에는 **조건에 맞는 행들을 다른 열 기준으로 묶어** 셉니다. 예를 들어 「실패한 이벤트를 사용자별로」 묶어 세는 것입니다.
2. `time` 열의 `"2026-11-02 09:01:05"` 는 문자열이라서 「시」만 꺼낼 수 없습니다. <mark>그래서 먼저 날짜·시간 값으로 바꾼 뒤 「시」(예: 9)를 꺼냅니다.</mark>
3. 분석한 결과(실패한 이벤트)는 **CSV(씨에스브이, 값을 쉼표(,)로 구분해 적은 텍스트 파일)** 로 저장하면 엑셀 같은 도구로 열어 볼 수 있습니다.

## 2.1 묶고 세기 · 시간 다루기 · 저장하기

**판다스 문법 상자 — 같은 값끼리 묶기 (빈칸 ① 에 씁니다)**

**<mark>`groupby("열")`</mark> 는 그 열의 값이 같은 줄끼리 묶습니다**

「소스별로 실패가 몇 개인가」를 알려면 먼저 `source` 값이 같은 행끼리 그룹(group)으로 묶어야 합니다. <mark>`groupby` 는 이 묶기만 하고, 개수는 세지 않습니다.</mark>

```python
import pandas as pd                                                                                   # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                                                              # 실패한 이벤트만 적은 연습용 작은 데이터
    "source": ["web", "server", "web", "saas", "web", "server"],                                      # source 열에 들어갈 값들
    "action": ["GET /board", "POST /login", "GET /report", "login", "GET /admin", "ACCOUNT:CHANGE"],  # action 열에 들어갈 값들
}
failed = pd.DataFrame(data)                                                                           # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
print(failed)                                                                                         # 표를 출력한다
grouped = failed.groupby("source")                                                                    # source 값이 같은 줄끼리 묶는다 — 아직 개수가 아니라 그룹만 만든 상태
print(grouped)                                                                                        # 묶은 결과를 출력한다 — 개수가 아니라 `DataFrameGroupBy` 라는 이름이 나온다
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
<pandas.api.typing.DataFrameGroupBy object at 0x10656da90>
```

- `data` 는 열 이름을 키로, 그 열에 위에서부터 들어갈 값들의 리스트를 값으로 둔 딕셔너리입니다. `pd.DataFrame(data)` 는 리스트에서 같은 자리(0번째, 1번째 …)에 있는 값끼리 한 행으로 묶어 표를 만듭니다. 파일 없이 연습용 표를 만들 때 씁니다.
- 읽는 법: <mark>마지막 줄에는 그룹의 개수나 내용이 없습니다.</mark> 묶기만 했고 아직 세지 않았기 때문입니다. `0x` 로 시작하는 부분은 실행할 때마다 다르고, `DataFrameGroupBy` 앞부분은 판다스 버전에 따라 달라도 괜찮습니다(예: `pandas.core.groupby.generic.`).
- <mark>묶기만 해서는 그룹마다 몇 개인지 알 수 없습니다.</mark> 개수는 다음 상자의 `.size()` 로 셉니다.

**알아 둘 것 — 그룹마다 행 수 세기**

**<mark>`.size()`</mark> 는 그룹마다 행이 몇 개인지 셉니다**

실습 2-2 의 `count_by_user` · `count_by_hour` 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다.

위 코드에 이어서 실행하는 다음 코드입니다.

```python
source_fail_counts = grouped.size()  # 그룹마다 행이 몇 개인지 센다 — 그룹 이름이 왼쪽에 나온다
print(source_fail_counts)            # saas 1 · server 2 · web 3 (그룹 이름 순서)
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
- 개수만 세려면 실습 2-1의 `value_counts()` 로도 같은 결과가 나옵니다. <mark>그래도 `groupby` 를 배우는 것은 묶은 그룹마다 평균 같은 다른 계산도 할 수 있기 때문입니다.</mark> 오늘은 개수(`size`)만 씁니다.

**판다스 문법 상자 — 큰 값부터 정렬하기 (빈칸 ② 에 씁니다)**

**<mark>`.sort_values(ascending=False)`</mark> 는 값이 큰 것부터 다시 정렬합니다**

위 코드에 이어서 실행하는 다음 코드입니다.

```python
sorted_source_fail_counts = source_fail_counts.sort_values(ascending=False)  # 개수가 큰 그룹부터 다시 정렬한다(ascending=False 는 큰 값부터 정렬)
print(sorted_source_fail_counts)                                             # web 3 · server 2 · saas 1
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
- `ascending`(어센딩)은 「오름차순(작은 값부터)」이라는 영어 단어입니다. 그래서 `ascending=False`(오름차순 아님)는 큰 값부터 정렬하라는 뜻이고, <mark>이 부분을 빼면 작은 값부터 나옵니다</mark>.

**알아 둘 것 — 묶고 세기를 한 줄로 쓰기**

`failed.groupby("source").size()` 처럼 묶기와 세기를 한 줄로 이어 쓰기도 합니다. <mark>실습 2-2 에서는 줄마다 하나씩 나눠 쓰고</mark>, 이 모양은 읽기만 합니다.

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")       # 이벤트 파일을 표로 읽는다

results = events["result"]                            # result 열만 꺼낸다
is_fail = results == "실패"                           # 행마다 실패면 True, 아니면 False 를 만든다
failed = events[is_fail]                              # True 인 행만 남겨 새 표(failed)를 만든다 — 실패한 이벤트만 담긴다

source_fail_counts = failed.groupby("source").size()  # 묶고(groupby) 바로 이어서 그룹마다 행 수를 센다(size) — 앞의 두 줄과 같은 일이다
print(source_fail_counts)                             # saas 1 · server 9 · web 13 (그룹 이름 순서)
```

실행 결과:

```
source
saas       1
server     9
web       13
dtype: int64
```

- 읽는 법: 이번에는 실제 이벤트 파일의 실패 23개를 셌습니다. `failed.groupby("source")` 가 만든 그룹에 바로 `.size()` 를 붙여서, 중간 이름(`grouped`)을 따로 만들지 않을 뿐입니다.

**알아 둘 것 — 미리 채운 `add_hour` 읽기: 시각에서 「시」만 꺼내 새 열로 붙이기**

`add_hour` 는 세 줄입니다. 실습 2-2 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다. 번호는 아래 코드 주석의 번호입니다.

| 번호 | 문법 | 하는 일 |
|---|---|---|
| 1 | `pd.to_datetime(열)` | `"2026-11-02 09:01:05"` 같은 문자열을 날짜·시간 값으로 바꿉니다 |
| 2 | `.dt.hour` | <mark>시각 값에서 「시」만 숫자로 꺼냅니다</mark>(02:14 → 2, 09:01 → 9) |
| 3 | `표["새 열 이름"] = 값` | <mark>표 맨 오른쪽에 새 열을 붙입니다</mark> |

<mark>날짜·시간 값이어야 「시」나 「분」 같은 부분만 꺼낼 수 있습니다.</mark> `dt` 는 datetime(날짜·시간)의 줄임말입니다.

```python
import pandas as pd                              # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

times = pd.to_datetime(events["time"])           # 1. 문자열 시각 57개를 시각 값으로 바꾼다
hours = times.dt.hour                            # 2. 시각 값에서 「시」만 숫자로 꺼낸다
events["hour"] = hours                           # 3. 표 맨 오른쪽에 hour 라는 새 열을 붙인다
print(times.head(3))                             # 바꾼 시각의 처음 3개 — 맨 아래에 종류(datetime64)가 나온다
print(events.shape)                              # (57, 7) — 열이 6개에서 7개가 되었다
```

실행 결과:

```
0   2026-11-02 02:14:08
1   2026-11-02 09:01:05
2   2026-11-02 09:01:06
Name: time, dtype: datetime64[us]
(57, 7)
```

- 읽는 법: 시각은 겉모습이 같지만, <mark>`datetime64` 는 이 열이 날짜·시간 값으로 바뀌었다는 표시</mark>입니다. 괄호 안(`[us]` · `[ns]`)은 판다스 버전에 따라 다를 수 있습니다. 행은 그대로 57개이고, <mark>`hour` 열이 붙어 열이 7개로 늘었습니다</mark>.

**알아 둘 것 — 표를 CSV 파일로 저장하기**

`표.to_csv(파일 이름, index=False)` 는 표를 엑셀로도 열 수 있는 CSV 파일(값을 쉼표(,)로 구분해 적은 텍스트 파일)로 저장합니다. 실습 2-2 의 `save_failed` 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다.

```python
failed.to_csv("failed_events.csv", index=False)  # 표를 failed_events.csv 파일로 저장한다 — index=False 는 행 번호를 저장하지 않는다는 뜻
```

- 실행하면 같은 폴더에 `failed_events.csv` 파일이 생깁니다. VS Code 로 열면 첫 줄은 열 이름이고, 둘째 줄부터 이벤트가 한 줄씩 있습니다.
- 엑셀로 열었을 때 한글이 깨져 보이면 VS Code 로 열어 확인합니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 | 직접 쓰는 곳 |
|---|---|---|---|
| `load_events` · `pick_failed` | (실습 2-1과 같아서 미리 채움) | 이벤트 표 · 실패한 행만 담은 표 | 없음(미리 채움) |
| `count_by_user` | 실패한 이벤트 표 | 사용자별 실패 횟수(많은 순서) | ① 묶기 · ② 정렬 |
| `add_hour` | 이벤트 표 | `hour` 열이 더해진 표 | 없음(미리 채움) |
| `count_by_hour` | 실패한 이벤트 표 | 시간대별 실패 횟수 | 없음(미리 채움) |
| `save_failed` | 표와 파일 이름 | 없음(CSV 파일로 저장) | 없음(미리 채움) |

- **직접 쓰는 곳은 `count_by_user` 의 두 곳**(① · ②)입니다. 나머지는 미리 채웠습니다. `load_events` 와 `pick_failed` 는 실습 2-1과 같고, `add_hour` 와 `save_failed` 는 아직 배우지 않은 문법이라 읽기만 합니다.
- 미리 채운 `count_by_hour` 는 `count_by_user` 의 묶기 · 세기와 같고 열 이름(`"hour"`)만 다릅니다. ① 을 쓸 때 본보기로 봅니다.

## 2.2 묶을 때 비어 있는 값은 빠집니다

- `groupby("user")` 는 `user` 가 비어 있는 행(`null`)을 그룹에 넣지 않고 **제외합니다.** <mark>웹 서버 이벤트는 `user` 가 없어서 사용자별 개수에 들어가지 않습니다.</mark>
- 그래서 <mark>사용자별 개수를 모두 더하면 실패한 이벤트 전체 개수보다 작아질 수 있습니다</mark>. 숫자를 읽을 때 「빠진 행이 있는가」를 함께 봅니다.
- <mark>오류 메시지는 나오지 않으므로 모르고 지나치기 쉽습니다.</mark>

## 실습 2-2 · 실패를 묶어 세고 CSV로 저장

**이런 상황이 있습니다**

- **지금은**: 실패가 23개라는 것만 알고, 누구에게 많이 났는지, 언제 많이 났는지는 모릅니다.
- **그래서 만드는 것**: `events_time.py` 입니다.
  - 실패를 사용자별로 묶어 많은 순서로 셉니다.
  - 시각에서 「시」를 꺼내 시간대별로 셉니다.
  - 실패한 이벤트를 CSV 파일로 저장합니다.
- **실행하면**: 단계 1: 사용자별 실패 횟수, 단계 2: 시간대별 실패 횟수, 단계 3: 저장한 행 수가 나오고 `failed_events.csv` 파일이 만들어집니다.
- **현업에서는**: 알림이 나면 근거 이벤트를 파일로 남겨 담당자가 열어 봅니다. 사용자별 · 시간대별 집계는 평소와 비교할 때의 출발점입니다.

**할 일**

1. `anomaly_detection` 폴더에 **`events_time.py` · `exercise2-2_run.py` 두 파일**을 만들고, `events_time.py` 의 `# ←` 가 있는 <mark>두 곳</mark>(① · ②)을 한 줄씩 채웁니다.
2. 실행해서 <mark>사용자별 실패 횟수</mark>(단계 1), <mark>시간대별 실패 횟수</mark>(단계 2), <mark>저장한 파일의 행 수</mark>(단계 3)를 읽습니다.

**`events_time.py`**

```python
import pandas as pd                         # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"      # 읽을 정규화 이벤트 파일 이름
FAILED_PATH = "failed_events.csv"           # 실패한 이벤트를 저장할 파일 이름


def load_events(path):                      # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)             # 파일을 읽어 표로 만든다
    return events                           # 표를 리턴한다


def pick_failed(events):                    # 표를 받는 함수
    """실패한 이벤트만 골라 새 표로 만든다.
    무엇이 잘못됐는지 조사할 때 성공한 이벤트는 빼고 보는 데 쓴다.
    """
    results = events["result"]              # result 열 하나를 꺼낸다
    is_fail = results == "실패"             # 행마다 실패면 True, 아니면 False
    failed = events[is_fail]                # True 인 행만 남긴다
    return failed                           # 실패한 행만 담은 표를 리턴한다


def count_by_user(failed):                  # 실패한 이벤트 표를 받는 함수
    """실패 횟수를 사용자별로 세어 많은 순서로 리턴한다.
    누구에게 실패가 많이 났는지 볼 때 쓴다.
    """
    # ① failed 를 "user" 열 기준으로 묶어(groupby) grouped 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)

    user_fail_counts = grouped.size()       # 그룹마다 행이 몇 개인지 센다
    # ② user_fail_counts 를 큰 값부터 정렬해(sort_values, ascending=False) sorted_user_fail_counts 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)

    return sorted_user_fail_counts          # 많은 순서로 정렬한 개수를 리턴한다


def add_hour(events):                       # 표를 받는 함수
    """time 열을 시각으로 바꾸고 「시」만 담은 hour 열을 더한다.
    시간대별로 세기 전에 쓴다.
    """
    times = pd.to_datetime(events["time"])  # 문자열 시각을 시각 값으로 바꾼다
    hours = times.dt.hour                   # 시각에서 「시」(0~23)만 꺼낸다
    events["hour"] = hours                  # hour 라는 새 열로 표에 더한다
    return events                           # hour 열이 더해진 표를 리턴한다


def count_by_hour(failed):                  # 실패한 이벤트 표를 받는 함수
    """실패 횟수를 시간대별로 센다.
    실패가 몇 시에 많이 났는지 볼 때 쓴다.
    """
    grouped = failed.groupby("hour")        # hour 가 같은 행끼리 묶는다
    hour_fail_counts = grouped.size()       # 그룹마다 행이 몇 개인지 센다
    return hour_fail_counts                 # 시간대별 개수를 리턴한다


def save_failed(failed, path):              # 표와 저장할 파일 이름을 받는 함수
    """실패한 이벤트 표를 CSV 파일로 저장한다.
    담당자가 엑셀로 근거를 확인하게 할 때 쓴다.
    """
    failed.to_csv(path, index=False)        # 표를 CSV 파일로 저장한다 — 미리 채운 줄
```

- 주석 줄은 그대로 두고, **각 주석 바로 아래 빈 줄**에 씁니다. ① · ② 모두 함수 안이라 앞에 공백 4개(4칸)로 시작합니다.

**직접 쓰는 곳**

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | `failed` 를 `"user"` 로 묶어 `grouped` 에 담기 | 4칸 |
| ② | 큰 값부터 정렬해 `sorted_user_fail_counts` 에 담기 | 4칸 |

- 채우기 전에 실행하면 `NameError: name 'grouped' is not defined` 오류가 납니다. ① 이 비어 있어 미리 채운 `grouped.size()` 줄이 `grouped` 를 찾지 못하기 때문이니 정상입니다.
- ① 확인: ① 만 쓰고 실행하면 `NameError: name 'sorted_user_fail_counts' is not defined` 가 나옵니다(파이썬 버전에 따라 뒤에 `Did you mean: …` 이 붙습니다). ② 를 아직 안 써서 나는 오류이니 정상입니다. 막히면: 아래 `count_by_hour` 의 `failed.groupby("hour")` 에서 `"hour"` 자리에 `"user"` 를 넣습니다.
- ② 확인: ② 까지 쓰고 실행하면 단계 1의 첫 줄이 `dami       4` 이면 성공입니다. 첫 줄이 `jiwoo      1` 이면 `ascending=False` 가 빠진 것입니다. 막히면: 2.1 의 정렬 문법 상자 `source_fail_counts.sort_values(ascending=False)` 에서 앞 이름만 `user_fail_counts` 로 바꿉니다.

**`exercise2-2_run.py`** — <mark>그대로 붙여 넣습니다.</mark> 직접 쓰는 줄은 없습니다. 이벤트를 읽어 실패만 골라 묶고 저장한 뒤 **세 단계**로 출력합니다. 단계 3에서 `pd.read_csv(파일)` 은 저장한 CSV 를 다시 표로 읽고, `len(표)` 는 그 표의 행 수입니다. 저장이 잘 됐는지 행 수로 확인하는 줄이라 읽기만 합니다.

```python
import pandas as pd                            # 저장한 파일을 다시 읽을 수 있게 판다스를 불러온다
from events_time import load_events, add_hour, pick_failed, count_by_user, count_by_hour, save_failed, EVENTS_PATH, FAILED_PATH  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)              # 이벤트 파일을 표로 읽는다
events = add_hour(events)                      # 시각을 바꾸고 hour 열을 더한다
failed = pick_failed(events)                   # 실패한 이벤트만 골라낸다

by_user = count_by_user(failed)                # 실패 횟수를 사용자별로 센다
print("--- 단계 1: 사용자별 실패 횟수")        # 단계 1 시작을 알리는 줄
print(by_user)                                 # 많은 순서로 출력한다

by_hour = count_by_hour(failed)                # 실패 횟수를 시간대별로 센다
print("--- 단계 2: 시간대별 실패 횟수")        # 단계 2 시작을 알리는 줄
print(by_hour)                                 # 시간대 순서로 출력한다

save_failed(failed, FAILED_PATH)               # 실패한 이벤트를 CSV 로 저장한다
saved = pd.read_csv(FAILED_PATH)               # 저장한 파일을 다시 읽어 확인한다
saved_count = len(saved)                       # 저장된 행이 몇 개인지 센다
print("--- 단계 3: 저장한 파일", FAILED_PATH)  # 단계 3 시작을 알리는 줄
print("저장된 행", saved_count, "개")          # 저장된 행 수를 출력한다
```

**순서**

1. **[VS Code]** `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 로 **`events_time.py` · `exercise2-2_run.py`** 를 만들고, 위의 같은 이름 코드 상자 내용을 각각 붙여 넣어 저장합니다.
2. **[VS Code]** `events_time.py` 의 `# ←` 두 곳(① · ②)을 채웁니다. 2.1 의 판다스 문법 상자를 보고 씁니다.

<!-- checklist -->
- [ ] `events_time.py` 를 만들어 붙여 넣고 빈칸 ① · ② 를 채워 저장했다
- [ ] `exercise2-2_run.py` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise2-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **세 단계**입니다. `--- 단계` 제목 줄은 세지 않고, 단계 1은 6줄, 단계 2는 7줄, 단계 3은 1줄입니다.

<!-- checklist -->
- [ ] `python exercise2-2_run.py` 를 실행해 단계 1 ~ 3 이 아래 「확인」과 같게 나왔다
<!-- /checklist -->

5. **[VS Code]** `anomaly_detection` 폴더에 새로 생긴 `failed_events.csv` 를 열어 첫 줄이 열 이름(`time,source,user,ip,action,result,hour`)인지 보고, <mark>`hour` 가 9 인 행의 `source` 를 봅니다</mark>.

<!-- checklist -->
- [ ] 새로 생긴 `failed_events.csv` 를 VS Code 로 열어 첫 줄의 열 이름을 봤다
<!-- /checklist -->

6. **[보고서]** `report_u2.md` 의 `## 실습 2-2` 아래를 채웁니다.
   - (가) [핵심 질문] 실행한 출력 전체를 붙여 넣고, 실패가 가장 많은 사용자와 횟수, 실패가 가장 많이 난 시간대와 횟수, 저장된 행 수를 적어 주세요.
   - (나) [응용] 시간대별 결과에서 실패가 가장 많이 난 시간대의 개수를 보세요. 이 개수는 실습 2-1 단계 3의 어느 소스 개수와 같은가요? 그 실패가 어느 소스에서 났는지 적고(근거는 숫자가 같다는 것까지 쓰면 됩니다), 이어서 확인할 것도 적어 주세요.
   - (다) [응용] 사용자별 실패 횟수를 모두 더하면 실패한 이벤트 전체보다 적습니다. 몇 개가 모자라고 왜 모자란지 적어 주세요. 그리고 이 차이를 모르고 사용자별 숫자만 보면 어떤 잘못된 판단을 할 수 있을지도 적어 주세요.

**확인** — 단계 1이 dami 4 · gaeun 3 · seoyeon 2 · jiwoo 1 순서, 단계 2의 9시가 13, 단계 3이 `저장된 행 23 개` 이고 `failed_events.csv` 가 생겼으면 성공입니다. 안 나오면 「정답」 레슨의 실습 2-2 출력과 한 줄씩 맞춰 보고, 다른 줄이 있으면 위 「직접 쓰는 곳」의 확인을 다시 봅니다.

## 실습 2-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 같은 값끼리 묶기 | `grouped = failed.groupby("user")` |
| 그룹마다 개수 세기 | `user_fail_counts = grouped.size()` |
| 큰 값부터 정렬 | `sorted_user_fail_counts = user_fail_counts.sort_values(ascending=False)` |
| 문자열 시각을 시각 값으로 | `times = pd.to_datetime(events["time"])` |
| 「시」만 꺼내기 | `hours = times.dt.hour` |
| 새 열로 붙이기 | `events["hour"] = hours` |
| CSV 로 저장 | `failed.to_csv(path, index=False)` |
| 비어 있는 값 | `groupby` 는 비어 있는 값(`null`)의 행을 빼고 센다 |

---
