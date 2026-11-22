---
id: m4-u02-l02
title: 실습 2-1 · 이벤트 표에서 실패만 골라 세기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/100_day02_pm_pandas_basics.md
  mission_id: GichanSource.m4-1103-pm-pandas-basics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 2-1 · 이벤트 표에서 실패만 골라 세기

## 목표: 소스별 실패 횟수

> **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다(판정 서버 로그도 포함해 세 가지 로그를 같은 모양으로 맞춘 이벤트 이야기입니다):
> 「이벤트 파일이 생겼습니다. 지금은 57개뿐이지만 실제로는 하루에 수만 개가 쌓입니다. 지금까지는 파이썬 리스트와 딕셔너리를 `for` 로 돌려 하나씩 세었는데, 이벤트가 늘수록 코드도 길어집니다.
>
> 이 파일을 표로 읽어 몇 개가 들어 있는지 알려 주세요. 성공과 실패가 각각 몇 개인지, 실패는 어느 소스(웹 서버 · 판정 서버 · SaaS)에서 몇 개씩 났는지도 알려 주세요.」
> - **왜 중요한가**: <mark>실패한 이벤트만 걸러 내고 소스별로 세는 일은 로그를 조사할 때마다 합니다.</mark> 표로 읽으면 이 일이 몇 줄로 끝나고, 이벤트가 57개든 5만 개든 같은 코드를 씁니다.
> - 이 실습에서 하는 일: 이벤트 파일을 표로 읽고, 실패한 이벤트를 소스별로 셉니다. 대부분은 미리 채워 두었고, 파일을 읽는 줄과 개수를 세는 줄 두 곳만 직접 씁니다.
> - 끝나면 쓰는 것: 보고서 (가) 답. (나) · (다)는 여유가 되면 하는 응용입니다

## 왜 판다스로 표를 읽는가

1. 지금까지 이벤트나 요청은 파이썬 **리스트와 딕셔너리**로 다뤘습니다. <mark>값별로 세려면 `for` 로 하나씩 꺼내 딕셔너리에 더해 가야 했습니다.</mark>
2. **판다스(pandas)** 는 데이터를 표로 읽고, <mark>짧은 코드로 걸러 내고 셀 수 있게 해 주는 파이썬 라이브러리</mark>입니다.
   - 판다스의 표를 **데이터프레임(DataFrame)** 이라고 부릅니다.
   - 가로 한 줄이 **행**, 세로 한 줄이 **열**입니다. 이 수업에서는 <mark>행 하나가 이벤트 1개이고, 열 하나는</mark> `time` 같은 키 하나의 값 전체입니다.
3. 오늘 쓰는 판다스는 로그 분석에 실제로 자주 쓰는 것만 골랐습니다. 실습 2-1에서는 읽기 · 걸러 내기 · 세기를, 실습 2-2에서는 묶기 · 시간 다루기 · 저장을, 실습 2-3에서는 두 조건으로 걸러 내기를 다룹니다.
4. 라이브러리(library)는 다른 사람이 미리 만들어 둔 파이썬 코드입니다. 판다스는 시작하기에서 설치했고, <mark>코드 맨 위에서 `import pandas as pd` 로 불러와 씁니다</mark>.
   - 판다스 문법은 두 가지 모양입니다. `pd.read_json(...)` 처럼 `pd.` 로 시작하는 것과, `events.shape` · `sources.value_counts()` 처럼 표나 열 뒤에 `.이름` 이 붙은 것입니다.
   - 함수 · `for` · 딕셔너리 같은 파이썬 문법도 판다스 문법과 함께 나옵니다.

## 1.1 정규화된 이벤트의 모양

정규화는 서로 다른 모양의 로그를 같은 키로 맞추는 일입니다. 먼저 이번 Unit에서 쓰는 이벤트가 **어느 로그에서 왔는지**부터 봅니다. 로그는 세 종류입니다.

| `source` | 무엇이 남기나 | 한 줄이 생기는 때 | 예 |
|---|---|---|---|
| `web` | 회사 게시판 같은 웹 서비스를 돌리는 웹 서버(nginx) | 누가 페이지를 열거나 로그인할 때 | 203.0.113.50 이 `POST /login` 을 요청함 |
| `server` | Module 3에서 만든 권한 판정 서버 | 누가 어떤 권한을 써도 되는지 물을 때 | seoyeon 이 `SALES:CHANGE` 를 요청해 거부됨 |
| `saas` | 회사가 빌려 쓰는 SaaS(인터넷으로 쓰는 소프트웨어, 예: 파일 보관 서비스) | 로그인하거나 파일을 올리고 내려받을 때 | seoyeon 이 `file.download` 를 함 |

이벤트 하나는 위 세 로그 중 한 곳의 로그 한 줄을 같은 형식으로 맞춘 것입니다. <mark>오늘 쓰는 파일의 키는 여섯 개입니다.</mark> 원래 로그 한 줄 전체를 담는 `raw` 키는 길어서 이 샘플 파일에서 뺐습니다.

| 키 | 뜻 | 예 |
|---|---|---|
| `time` | 일어난 시각(한국 시간) | `2026-11-02 09:12:03` |
| `source` | 어느 로그에서 왔는지 | `web`(웹 서버) · `server`(판정 서버) · `saas`(SaaS 서비스) |
| `user` | 누가 했는지 | `seoyeon`. 웹 서버 로그에는 사용자 이름이 없어서 `null` |
| `ip` | 어느 주소에서 왔는지 | `203.0.113.50`. 판정 서버 로그에는 주소가 없어서 `null` |
| `action` | 무엇을 했는지 | `POST /login` · `SALES:CHANGE` · `file.download` |
| `result` | 성공했는지 | `성공` 또는 `실패` |

**로그마다 비어 있는 키가 있습니다.**

| `source` | `null` 인 키 | 이유 |
|---|---|---|
| `web`(웹 서버) | `user` | 웹 서버는 로그인한 계정을 모르기 때문입니다 |
| `server`(판정 서버) | `ip` | 원래 로그에 주소가 없기 때문입니다 |

- 주소(`ip`)는 사람이 아니라 **접속한 곳**입니다. 한 사무실의 여러 사람이 같은 주소로 보일 수도, 한 사람이 집과 회사에서 다른 주소로 접속할 수도 있습니다. 이 수업의 `203.0.113.50` · `198.51.100.x` · `192.0.2.x` 는 문서에서 예시로 쓰라고 정해 둔 주소 범위라서 실제 장비를 가리키지 않습니다.
- 원래 로그에 없는 값(**결측값**, missing value)은 <mark>임의로 채우지 않고 `null` 로 둡니다</mark>. 없는 값을 임의로 채우면 분석 결과가 틀려지기 때문입니다.
  - 이 값은 JSON 파일에서는 `null`, 파이썬과 판다스 표에서는 `None` 또는 `NaN`(「숫자가 아님」이라는 뜻의 Not a Number 줄임말 · 난)으로 보이며, 모두 「값이 없다」는 같은 뜻입니다.
- 판다스로 읽으면 이 파일이 아래 같은 표가 됩니다. 맨 왼쪽 숫자는 판다스가 붙이는 **행 번호**(인덱스, index)입니다.

| 행 번호 | time | source | user | ip | action | result |
|---|---|---|---|---|---|---|
| 0 | 2026-11-02 02:14:08 | saas | jiwoo | 203.0.113.80 | login | 실패 |
| 1 | 2026-11-02 09:01:05 | web | NaN | 198.51.100.21 | GET / | 성공 |
| 2 | 2026-11-02 09:01:06 | web | NaN | 198.51.100.21 | GET /static/app.css | 성공 |

## 1.2 판다스로 표 읽기 · 세기

**판다스 문법 상자 — 파일을 표로 읽기 (빈칸 ① 에 씁니다)**

**<mark>`pd.read_json(파일 이름)`</mark> 은 JSON 파일을 열어 「표」(데이터프레임, DataFrame)로 만듭니다**

표는 가로 한 줄(행)과 세로 한 줄(열)로 이루어집니다. 이 수업의 이벤트 표에서는 **행 하나가 이벤트 1개**이고, **열 하나가 같은 키**(`time` · `source` …)입니다. 지금까지는 `for` 로 이벤트를 하나씩 꺼내 확인했습니다. 파일을 표로 읽으면 걸러 내기와 세기를 코드 한 줄로 할 수 있습니다(아래에서 차례로 배웁니다).

```python
import pandas as pd                              # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 파일 속 이벤트 57개를 표 한 개(events)로 읽는다 — 행 하나가 이벤트 하나
row_count = len(events)                          # 표의 행이 몇 개인지 센다 — 리스트의 길이를 세던 len 과 같다
print(row_count)                                 # 57 이 나온다 — 이벤트 57개
```

실행 결과:

```
57
```

- 읽는 법: <mark>`57` 은 표의 행 수</mark>이고, 행 하나가 이벤트 하나이므로 이벤트 57개라는 뜻입니다.
- `import pandas as pd` 는 판다스를 불러오고, 이름을 `pd` 로 줄여 쓰겠다는 뜻입니다. `read_json` 처럼 표를 만드는 판다스 함수는 앞에 `pd.` 를 붙여 부릅니다.
- `pd.read_json(파일 이름)` 은 JSON 파일의 이벤트 57개를 읽어 표 하나로 만들어 리턴합니다.

**알아 둘 것 — 표의 크기 보기**

`.shape` 는 표가 몇 행 몇 열인지 알려 줍니다. 실습 2-1 의 `describe_events` 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다.

```python
import pandas as pd                              # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

shape = events.shape                             # 표의 크기를 (행 수, 열 수) 로 구한다
print(shape)                                     # (57, 6) 이 나온다 — 이벤트 57개(행), 열 6개
```

실행 결과:

```
(57, 6)
```

- 읽는 법: `(57, 6)` 은 <mark>57행 6열</mark>, 이벤트 57개에 열 6개라는 뜻입니다.

**알아 둘 것 — 열 하나 꺼내기**

**<mark>`표["열 이름"]`</mark> 은 표에서 열 하나를 꺼냅니다. 꺼낸 열을 시리즈(Series)라고 합니다**

실습 2-1 의 `describe_events` · `count_values` 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다. 빈칸 ② 는 이렇게 꺼낸 열에 개수 세기를 붙입니다.

`events["source"]` 로 꺼낸 시리즈입니다. 값마다 그 값이 있던 행의 번호(인덱스)가 왼쪽에 함께 나옵니다. 아래는 처음 4개와 마지막 1개입니다.

| 행 번호 | `events["source"]` |
|---|---|
| 0 | saas |
| 1 | web |
| 2 | web |
| 3 | web |
| … | … |
| 56 | server |

```python
import pandas as pd                              # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

sources = events["source"]                       # source 열 하나를 꺼낸다 — web · server · saas 값이 57개 들어 있다
source_count = len(sources)                      # 꺼낸 열에 값이 몇 개 있는지 센다
print(source_count)                              # 57 이 나온다 — 행마다 값이 하나씩이라 행 수와 같다
```

실행 결과:

```
57
```

- 읽는 법: <mark>`57` 은 꺼낸 열에 든 값의 개수입니다.</mark> 행이 57개이므로 값도 57개입니다.
- `events["source"]` 는 표에서 `source` 열만 꺼냅니다(판다스에서는 열 하나를 Series, 시리즈라고 부릅니다).
- 열 이름은 파일에 적힌 키와 똑같이 써야 합니다. **없는 열 이름을 쓰면 `KeyError` 오류가 납니다.**

**알아 둘 것 — 열의 앞 몇 개만 보기**

`열.head(3)` 은 열의 앞에서 3개만 남깁니다. 실습 2-1 의 `describe_events` 에 미리 채워져 있어서 직접 쓰지 않고 읽기만 합니다.

```python
import pandas as pd                              # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

times = events["time"]                           # 표에서 time 열만 꺼낸다 — 이벤트 57개의 시각이 한 줄로 나열된 열
first_times = times.head(3)                      # 그 열의 처음 3개(0 ~ 2번 행)만 남긴다
for time_text in first_times:                    # 처음 3개를 하나씩 꺼낸다
    print(time_text)                             # 시각 하나를 한 줄에 출력한다(모두 3줄)
```

실행 결과:

```
2026-11-02 02:14:08
2026-11-02 09:01:05
2026-11-02 09:01:06
```

- 읽는 법: 시각 57개 중 앞의 3개입니다.

**판다스 문법 상자 — 값별로 개수 세기 (빈칸 ② 에 씁니다)**

**<mark>`.value_counts()`</mark> 는 열에서 같은 값이 몇 번 나왔는지 세어 많은 순서로 알려 줍니다**

`events["source"]` 열에 `.value_counts()` 를 하면 같은 값끼리 모아 개수를 세고, 많은 값부터 보여 줍니다.

| 값 | 개수 |
|---|---|
| web | 28 |
| server | 15 |
| saas | 14 |

```python
import pandas as pd                              # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

sources = events["source"]                       # source 열 하나를 꺼낸다 — web · server · saas 값이 57개 들어 있다
source_event_counts = sources.value_counts()     # 같은 값이 몇 번 나왔는지 센다 — 많은 값부터 정렬되어 나온다
print(source_event_counts)                       # 값(web · server · saas)과 그 개수가 줄마다 나온다
```

실행 결과:

```
source
web       28
server    15
saas      14
Name: count, dtype: int64
```

- 읽는 법: 첫 줄 `source` 는 센 열의 이름이고, 아래 줄은 <mark>왼쪽이 값, 오른쪽이 나온 횟수</mark>입니다. 28 + 15 + 14 = 57 이라 이벤트 전체 개수와 같습니다.
- `value_counts()` 는 같은 값이 몇 번 나왔는지 세어 **많은 순서**로 리턴합니다. 맨 아래 `Name: count, dtype: int64` 줄은 읽지 않아도 됩니다.
- Module 3에서 딕셔너리로 값별 횟수를 세던 `counts[value] = counts.get(value, 0) + 1` 과 같은 일을 한 줄로 합니다.

**알아 둘 것 — 조건에 맞는 행만 걸러 내기**

`표[조건]` 은 <mark>조건이 `True` 인 행만 남긴 새 표를 만듭니다</mark>. 이 일을 **필터링**(filtering)이라고 합니다. 여기서 조건은 행마다 `True` 또는 `False` 가 하나씩 있는 열입니다(아래 코드의 `is_fail`). 실습 2-1 의 `pick_failed` 에 미리 채워져 있어서 지금은 읽기만 하고, 실습 2-3에서 직접 씁니다.

```python
import pandas as pd                              # 판다스를 pd 라는 짧은 이름으로 불러온다
events = pd.read_json("normalized_events.json")  # 이벤트 파일을 표로 읽는다

results = events["result"]                       # result 열만 꺼낸다 — 성공 · 실패가 57개 나열된 열
is_fail = results == "실패"                      # result 열의 각 값이 "실패"와 같은지 비교해 행마다 True 또는 False 를 하나씩 만든다(57개)
failed = events[is_fail]                         # True 인 행만 남겨 새 표(failed)를 만든다
failed_shape = failed.shape                      # 새 표의 크기를 꺼낸다
print(failed_shape)                              # (23, 6) — 실패한 이벤트 23개, 열은 그대로 6개
```

실행 결과:

```
(23, 6)
```

- 읽는 법: <mark>실패한 이벤트 23개만 남았다는 뜻</mark>입니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 | 직접 쓰는 곳 |
|---|---|---|---|
| `load_events` | 파일 경로 | 이벤트 표 | ①: 파일을 표로 읽기 |
| `describe_events` | 이벤트 표 | 표 크기와 `time` 열의 처음 3개 | 없음(미리 채움) |
| `pick_failed` | 이벤트 표 | `실패` 인 행만 담은 표 | 없음(미리 채움) |
| `count_values` | 표와 열 이름 | 그 열의 값별 개수 | ②: 값별 개수 세기 |

- **직접 쓰는 곳은 두 곳**(① · ②)입니다. 열을 꺼내는 줄과 1.2 에서 읽기만 한 문법(`.shape` · `.head(3)` · 조건으로 걸러 내기)이 나오는 줄은 미리 채웠습니다. `import` 와 실행 파일도 미리 채웠습니다.

## 실습 2-1 · 실패 이벤트를 소스별로 세기

**이런 상황이 있습니다**

- **지금은**: 이벤트 파일에 57개가 있지만, 실패가 몇 개이고 어느 소스에서 났는지는 사람이 한 줄씩 읽어야 압니다.
- **그래서 만드는 것**: `events_basic.py` 입니다.
  - 파일을 표로 읽습니다.
  - 실패한 이벤트만 골라냅니다.
  - 열 하나의 값별 개수를 셉니다.
- **실행하면**: 단계 1: 표 크기(행 수, 열 수)와 처음 3개 시각, 단계 2: 성공 · 실패 개수, 단계 3: 실패한 이벤트의 소스별 개수, 단계 4: 전체 이벤트의 소스별 개수가 나옵니다.
- **현업에서는**: 관제 화면의 「실패 이벤트 수 · 소스별 분포」 그래프가 이 계산입니다. 어느 소스부터 조사할지 정할 때 봅니다.

**할 일**

1. `anomaly_detection` 폴더에 **`events_basic.py` · `exercise2-1_run.py` 두 파일**을 만들고, `events_basic.py` 의 `# ←` 가 있는 <mark>두 곳</mark>(① · ②)을 한 줄씩 채웁니다.
2. 실행해서 <mark>표 크기(행 수, 열 수)와 처음 3개 시각</mark>(단계 1), <mark>성공 · 실패 개수</mark>(단계 2), <mark>실패한 이벤트의 소스별 개수</mark>(단계 3), <mark>전체 이벤트의 소스별 개수</mark>(단계 4)를 읽습니다.

**`events_basic.py`**

```python
import pandas as pd                     # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"  # 읽을 정규화 이벤트 파일 이름


def load_events(path):                  # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    # ① pd.read_json 으로 path 의 파일을 읽어 events 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)

    return events                       # 표를 리턴한다


def describe_events(events):            # 표를 받는 함수
    """표의 크기와 앞 시각 3개를 구한다.
    새 파일을 받았을 때 내용이 제대로 들어 있는지 확인하는 데 쓴다.
    """
    shape = events.shape                # 표의 크기 (행 수, 열 수)
    times = events["time"]              # time 열 하나를 꺼낸다
    first_times = times.head(3)         # 그 열의 앞 3개만 남긴다
    return shape, first_times           # 크기와 처음 3개를 리턴한다


def pick_failed(events):                # 표를 받는 함수
    """실패한 이벤트만 골라 새 표로 만든다.
    무엇이 잘못됐는지 조사할 때 성공한 이벤트는 빼고 보는 데 쓴다.
    """
    results = events["result"]          # result 열 하나를 꺼낸다
    is_fail = results == "실패"         # 행마다 실패면 True, 아니면 False
    failed = events[is_fail]            # True 인 행만 남긴다
    return failed                       # 실패한 행만 담은 표를 리턴한다


def count_values(table, column):        # 표와 열 이름을 받는 함수
    """한 열의 값별 개수를 센다.
    소스별 · 결과별 · 사용자별로 몇 개인지 알고 싶을 때 쓴다.
    """
    values = table[column]              # column 열 하나를 꺼낸다
    # ② values 에서 값별 개수를 value_counts() 로 세어 value_event_counts 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)

    return value_event_counts           # 값별 개수를 리턴한다
```

- 주석 줄은 그대로 두고, **각 주석 바로 아래 빈 줄**에 씁니다. ① · ② 모두 함수 안이라 앞에 공백 4개(4칸)로 시작합니다.
- `describe_events` 의 `events["time"]` 과 `count_values` 의 `table[column]` 은 같은 열 꺼내기이고, 뒤의 것은 열 이름을 `column` 이라는 변수로 받는 것이 다릅니다.

**직접 쓰는 곳**

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | 파일을 표로 읽어 `events` 에 담기 | 4칸 |
| ② | `values` 의 값별 개수를 `value_event_counts` 에 담기 | 4칸 |

- 채우기 전에 실행하면 `NameError: name 'events' is not defined` 오류가 납니다. `events` 를 만드는 ① 이 비어 있기 때문이니 정상입니다.
- ① 확인: ① 만 쓰고 실행하면 단계 1(`(57, 6)` 과 시각 세 줄)이 나온 뒤 `NameError: name 'value_event_counts' is not defined` 가 나옵니다. ② 를 아직 안 써서 나는 오류이니 정상입니다. 막히면: 1.2 의 첫 문법 상자 `pd.read_json("normalized_events.json")` 에서 파일 이름 자리에 따옴표 없이 `path` 를 넣습니다.
- ② 확인: ② 까지 쓰고 실행하면 단계 2에 `성공    34` · `실패    23` 이 나오면 성공입니다. `<bound method …>` 가 나오면 `value_counts` 뒤에 괄호 `()` 가 있는지 봅니다. 막히면: 1.2 의 값별 개수 문법 상자에서 `sources.value_counts()` 의 `sources` 자리에 `values` 를 넣습니다.

**`exercise2-1_run.py`** — <mark>그대로 붙여 넣습니다.</mark> 학생이 쓰는 줄은 없습니다. 이벤트 파일을 읽어 **네 단계**로 출력합니다. `len(표)` 는 표의 행 수입니다.

```python
from events_basic import load_events, describe_events, pick_failed, count_values, EVENTS_PATH  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)                                                              # 이벤트 파일을 표로 읽는다
shape, first_times = describe_events(events)                                                   # 표 크기와 time 열의 처음 3개를 구한다
print("--- 단계 1: 표 크기(행 수, 열 수)와 처음 3개 시각")                                     # 단계 1 시작을 알리는 줄
print(shape)                                                                                   # (행 수, 열 수)를 출력한다
for time_text in first_times:                                                                  # 처음 3개 시각을 하나씩 꺼낸다
    print(time_text)                                                                           # 시각 하나를 한 줄에 출력한다(모두 3줄)

result_event_counts = count_values(events, "result")                                           # result 열의 값별 개수를 센다
print("--- 단계 2: 성공 · 실패별 개수")                                                        # 단계 2 시작을 알리는 줄
print(result_event_counts)                                                                     # 성공 · 실패 개수를 출력한다

failed = pick_failed(events)                                                                   # 실패한 이벤트만 골라낸다
failed_count = len(failed)                                                                     # 실패한 이벤트가 몇 개인지 센다
source_fail_counts = count_values(failed, "source")                                            # 실패한 이벤트의 소스별 개수를 센다
print("--- 단계 3: 실패한 이벤트", failed_count, "개의 소스별 개수")                           # 단계 3 시작을 알리는 줄
print(source_fail_counts)                                                                      # 소스별 개수를 출력한다

source_event_counts = count_values(events, "source")                                           # 전체 이벤트의 소스별 개수를 센다
print("--- 단계 4: 전체 이벤트의 소스별 개수")                                                 # 단계 4 시작을 알리는 줄
print(source_event_counts)                                                                     # 소스별 전체 개수를 출력한다
```

**순서**

1. **[VS Code]** `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 로 **`events_basic.py` · `exercise2-1_run.py`** 를 만들고, 위의 같은 이름 코드 상자 내용을 각각 붙여 넣어 저장합니다.
2. **[VS Code]** `events_basic.py` 의 `# ←` 두 곳(① · ②)을 채웁니다. 1.2 의 판다스 문법 상자를 보고 씁니다.

<!-- checklist -->
- [ ] `events_basic.py` 를 만들어 붙여 넣고 빈칸 ① · ② 를 채워 저장했다
- [ ] `exercise2-1_run.py` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다.
   ```bash
   pwd
   python exercise2-1_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-1_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. `--- 단계` 제목 줄은 세지 않고, 단계 1은 4줄, 단계 2는 4줄, 단계 3은 5줄, 단계 4는 5줄입니다.

<!-- checklist -->
- [ ] `python exercise2-1_run.py` 를 실행해 단계 1 ~ 4 가 아래 「확인」과 같게 나왔다
<!-- /checklist -->

5. **[보고서]** `report_u2.md` 의 `## 실습 2-1` 아래에 (가)를 채웁니다. (나) · (다)[응용]은 여유가 되면 `## 실습 응용 질문` 칸의 `2-1 (나)` · `2-1 (다)` 에 씁니다. 파일이 아직 없으면 [「보고서 쓰기」 레슨 첫 페이지](__SITE__/exercises/module/4/unit/2/lesson/1/page/3)를 보고 `anomaly_detection` 폴더에 먼저 만듭니다.
   - (가) [핵심 질문] 실행한 출력 전체를 붙여 넣고, 표의 행 수와 열 수, 성공과 실패 개수, 실패한 이벤트의 소스별 개수를 적어 주세요.
   - (나) [응용] 실패 개수만 보면 web 이 가장 많습니다. 그렇다면 web 이 가장 문제가 큰 소스라고 말할 수 있을까요? 단계 4의 전체 이벤트 수와 함께 보고 이유를 적어 주세요.
   - (다) [응용] web 이벤트에는 `user` 가 비어 있습니다. 사용자 이름으로 실패를 세려 할 때 web 의 실패 13개는 어떻게 될지 예상하고, 사용자 대신 어떤 열을 보면 같은 대상이 반복했는지 알 수 있을지 이유와 함께 적어 주세요.

**확인** — 단계 1이 `(57, 6)`, 단계 2가 성공 34 · 실패 23, 단계 3의 제목 줄에 `23 개` 가 나오고 web 13 · server 9 · saas 1 이면 성공입니다. 안 나오면 「정답」 레슨의 실습 2-1 출력과 한 줄씩 맞춰 보고, 다른 줄이 있으면 위 「직접 쓰는 곳」의 확인을 다시 봅니다.

## 실습 2-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 판다스 불러오기 | `import pandas as pd` |
| JSON 파일을 표로 읽기 | `events = pd.read_json(path)` (`load_events`) |
| 표 크기 | `shape = events.shape` (`describe_events`) |
| 열 하나 꺼내기 | `times = events["time"]` |
| 처음 3개만 보기 | `first_times = times.head(3)` |
| 결과 열 꺼내기 | `results = events["result"]` (`pick_failed`) |
| 행마다 실패인지 비교 | `is_fail = results == "실패"` |
| 실패한 행만 걸러 내기 | `failed = events[is_fail]` |
| 이름으로 받은 열 꺼내기 | `values = table[column]` (`count_values`) |
| 값별 개수 | `value_event_counts = values.value_counts()` |

---
