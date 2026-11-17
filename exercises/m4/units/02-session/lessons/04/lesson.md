---
id: m4-u02-l04
title: Exercise 2-3 · 세 로그를 하나로 합쳐 시간순으로 저장하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/098_day02_am_normalize.md
  mission_id: GichanSource.m4-1103-am-normalize
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 2-3 · 세 로그를 하나로 합쳐 시간순으로 저장하기

## 개요

> **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「세 로그가 같은 모양이 되었습니다. 하나로 합쳐 시간 순서로 정렬해 파일로 저장해 주세요. Unit 3에서 이 파일로 실패가 몇 번 났는지 세겠습니다.
>
> 소스별로 이벤트가 몇 개씩인지, 사용자나 주소가 비어 있는 이벤트가 몇 개인지도 알려 주세요. 합친 결과로 gaeun 이 한 일을 시간순으로 보여 주세요.」
> - **왜 중요한가**: <mark>로그가 따로 있을 때는 보이지 않던 같은 계정의 일이 시간순으로 합치면 보입니다.</mark> 값이 비어 있는 이벤트 수는 분석에서 빠지는 이벤트가 얼마나 되는지 미리 알려 줍니다. 저장한 파일은 Unit 3 분석의 입력이 됩니다.

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「Exercise」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 읽기 · 왜 필요한가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. Exercise 2-1 · Exercise 2-2에서 만든 함수는 로그 한 종류씩 공통 이벤트 리스트를 만듭니다. 이제 세 리스트를 **합치고, 시간순으로 정렬하고, 파일로 저장**합니다.
2. 순서는 이렇습니다.
   - 웹 서버 이벤트 28개 · 판정 서버 이벤트 15개 · SaaS 이벤트 14개를 각각 만듭니다.
   - 하나의 리스트로 이어 붙입니다(57개).
   - `time` 문자열 순서로 정렬합니다. 공통 모양(`2026-11-02 09:12:03`)은 연 · 월 · 일 · 시 · 분 · 초 순서라서 <mark>문자열 순서가 곧 시간 순서입니다.</mark>
   - `normalized_events.json` 파일로 저장합니다.

## 읽기 · 3.1 이어 붙이기 · 정렬하기 · 저장하기

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문은 없습니다. 문법 상자의 코드는 눈으로 읽어도 되고, 따라 쳐 보아도 됩니다.

**문법 상자 — 리스트를 이벤트의 time 값 순서로 정렬하기**

**<mark>`리스트.sort(key=함수)`</mark> 는 각 이벤트를 함수에 전달해 리턴된 값의 순서로 리스트를 정렬합니다**

두 리스트를 `+` 로 이어 붙이는 것은 파이썬에서 배운 대로입니다. 새로 나오는 것은 `sort(key=함수)` 하나입니다.

```python
web_events = [{"time": "2026-11-02 11:00:00", "source": "server"}, {"time": "2026-11-02 09:12:03", "source": "web"}]  # 이벤트 두 개
saas_events = [{"time": "2026-11-02 10:12:55", "source": "saas"}]  # 이벤트 한 개
merged = web_events + saas_events                                  # 리스트 두 개를 이어 붙인다


def get_time(event):                                               # 이벤트 하나를 받는 함수
    """정렬 기준으로 쓸 시각 문자열을 리턴한다.
    이벤트를 시간순으로 정렬할 때 쓴다.
    """
    return event["time"]                                           # 이벤트의 time 값을 리턴한다


merged.sort(key=get_time)                                          # get_time 이 리턴하는 time 이 이른 것부터(오름차순) 정렬한다
for event in merged:                                               # 이벤트를 하나씩 꺼낸다
    print(event["time"], event["source"])                          # 시각과 소스를 출력한다
```

실행 결과:

```
2026-11-02 09:12:03 web
2026-11-02 10:12:55 saas
2026-11-02 11:00:00 server
```

- `a + b` 는 리스트 `a` 뒤에 `b` 를 이어 붙인 새 리스트입니다(배운 대로입니다).
- `events.sort(key=get_time)` 은 리스트 `events` 의 각 이벤트를 `get_time` 함수에 전달해 리턴된 값(`time`) 순서로 정렬합니다. <mark>`get_time` 뒤에 괄호를 붙이지 않습니다</mark>(함수를 호출하는 것이 아니라 함수 자체를 전달하는 것입니다).

위 코드의 `sort(key=get_time)` 이 하는 일을 따라가 봅니다.

| 정렬 전 순서 | `get_time` 이 리턴하는 값 |
|---|---|
| 1. `server` 이벤트 | `2026-11-02 11:00:00` |
| 2. `web` 이벤트 | `2026-11-02 09:12:03` |
| 3. `saas` 이벤트 | `2026-11-02 10:12:55` |

- `sort` 는 이 값을 서로 비교해 **작은 값부터 큰 값 순서(오름차순)** 로 놓습니다. 시각 문자열은 이른 시각일수록 작은 값이라서 <mark>이른 시각이 앞, 늦은 시각이 뒤에 옵니다.</mark> 결과는 `web`(09:12:03) → `saas`(10:12:55) → `server`(11:00:00) 순서입니다.
- `sort` 는 리스트 자체를 바꾸고 **아무것도 리턴하지 않습니다.** **`events = events.sort(…)` 라고 쓰면 `events` 가 `None` 이 됩니다.**

**문법 상자 — 리스트를 JSON 파일로 저장하기**

**<mark>`json.dump(값, 파일)`</mark> 은 파이썬 값을 JSON 형식으로 파일에 씁니다. `ensure_ascii=False` 는 한글을 그대로, `indent=2` 는 보기 좋게 들여쓰기를 합니다**

```python
import json                                                         # json 모듈을 불러온다

events = [{"user": "seoyeon", "result": "성공"}]                    # 저장할 값
with open("demo_events.json", "w", encoding="utf-8") as demo_file:  # 쓰기 모드("w")로 파일을 연다
    json.dump(events, demo_file, ensure_ascii=False, indent=2)      # 한글은 그대로, 들여쓰기를 해서 파일에 쓴다
with open("demo_events.json", encoding="utf-8") as demo_file:       # 방금 쓴 파일을 다시 연다
    text = demo_file.read()                                         # 내용을 문자열로 읽는다
print(text)                                                         # 파일 내용을 출력한다
```

실행 결과:

```
[
  {
    "user": "seoyeon",
    "result": "성공"
  }
]
```

- `json.dumps` 는 값을 JSON **문자열**로 만들고, <mark>`json.dump` 는 값을 JSON **파일**에 바로 씁니다</mark>(`s` 가 없습니다).
- **`ensure_ascii=False` 를 빼면 한글이 `성공` 같은 코드로 저장됩니다.**

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_web` | 웹 서버 로그 파일 경로 | 공통 이벤트 리스트(미리 채움) |
| `merge_events` | 이벤트 리스트 세 개 | 하나로 합쳐 시간순으로 정렬한 리스트 |
| `count_by_source` | 이벤트 리스트 | `{소스: 개수}` 딕셔너리 |
| `count_missing` | 이벤트 리스트와 키 이름 | 그 키의 값이 `None` 인 이벤트 수(미리 채움) |
| `save_events` | 이벤트 리스트와 파일 이름 | 없음(파일로 저장) |

- **직접 쓰는 곳은 세 함수**(번호 1 ~ 5)입니다.
  - `merge_events`(1 · 2번): 이어 붙이고 시간순으로 정렬합니다.
  - `count_by_source`(3 · 4번): 소스별 이벤트 수를 셉니다. 값별 횟수를 세는 `counts.get(…, 0) + 1` 은 3과목에서 쓴 방식과 같습니다.
  - `save_events`(5번): JSON 파일로 저장합니다.

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise 2-3 · 세 로그의 이벤트를 합쳐 시간순으로 저장하기

**이런 상황이 있습니다**

- **지금은**: 공통 이벤트가 로그 종류별로 따로 있어서, 같은 계정이 여러 곳에서 한 일을 시간순으로 볼 수 없습니다.
- **그래서 만드는 것**: `normalize.py` 입니다.
  - 세 리스트를 하나로 이어 붙여 시간순으로 정렬합니다.
  - 소스별 이벤트 수를 셉니다.
  - `normalized_events.json` 파일로 저장합니다.
- **실행하면**: 단계 1: 소스별 이벤트 수, 단계 2: `user` · `ip` 가 비어 있는 이벤트 수, 단계 3: gaeun 의 이벤트(시간순), 단계 4: 저장한 이벤트 수가 나옵니다.
- **현업에서는**: <mark>같은 모양으로 맞춘 이벤트를 한곳에 쌓아 두면 탐지 규칙은 그곳만 읽으면 됩니다.</mark> 이렇게 쌓아 두는 곳이 SIEM(심)의 저장소입니다.

**할 일**

1. **`normalize.py` · `exercise2-3_run.py`** 두 파일을 만들고, `normalize.py` 의 `merge_events` · `count_by_source` · `save_events` 에서 직접 쓰는 곳을 씁니다. Exercise 2-1의 `normalize_web.py` 와 Exercise 2-2의 `normalize_json_csv.py` 가 필요합니다.
2. 실행해서 <mark>소스별 이벤트 수</mark>(단계 1), <mark>값이 비어 있는 이벤트 수</mark>(단계 2), <mark>gaeun 의 이벤트</mark>(단계 3), <mark>저장된 이벤트 수</mark>(단계 4)를 읽습니다.

**`normalize.py`**

```python
import json                                                 # 파일에 JSON 으로 저장하는 json 모듈을 불러온다
from normalize_web import normalize_web                     # 웹 서버 로그 정규화 함수를 불러온다
from normalize_json_csv import load_server, load_saas       # 판정 서버 · SaaS 로그 읽기 함수를 불러온다

EVENTS_PATH = "normalized_events.json"                      # 정규화한 이벤트를 저장할 파일 이름


def load_web(path):                                         # 웹 서버 로그 파일 경로를 받는 함수
    """웹 서버 로그 파일의 모든 줄을 공통 이벤트 리스트로 바꾸고 깨진 줄은 건너뛴다.
    웹 서버 로그를 정규화 결과에 합칠 준비를 할 때 쓴다.
    """
    events = []                                             # 결과를 담을 리스트
    with open(path, encoding="utf-8") as web_file:          # 파일을 연다
        for line in web_file:                               # 한 줄씩 꺼낸다
            event = normalize_web(line)                     # 공통 이벤트로 바꾼다
            if event is not None:                           # 읽을 수 있는 줄이면
                events.append(event)                        # 리스트에 추가한다
    return events                                           # 이벤트 리스트를 리턴한다


def get_time(event):                                        # 이벤트 하나를 받는 함수
    """정렬 기준으로 쓸 시각 문자열을 리턴한다.
    이벤트를 시간순으로 정렬할 때 쓴다.
    """
    return event["time"]                                    # 이벤트의 time 값을 리턴한다


def merge_events(web, server, saas):                        # 세 이벤트 리스트를 받는 함수
    """이벤트 리스트 세 개를 하나로 이어 붙이고 시간순으로 정렬한다.
    여러 로그에서 같은 계정이 한 일을 시간순으로 함께 보고 싶을 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. web, server, saas 를 + 로 이어 붙여 events 에 담는다
    # 2. events.sort(key=get_time) 로 time 이 이른 것부터(오름차순) 정렬한다 (sort 는 events 자체를 바꾸고 아무것도 리턴하지 않는다)
    return events                                           # 시간순으로 정렬한 이벤트 리스트를 리턴한다


def count_by_source(events):                                # 이벤트 리스트를 받는 함수
    """소스별 이벤트 수를 {소스: 개수} 딕셔너리로 센다.
    합친 이벤트가 로그 종류마다 몇 개씩 들어왔는지 확인할 때 쓴다.
    """
    source_event_counts = {}                                # 결과를 담을 딕셔너리
    for event in events:                                    # 이벤트를 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. event 의 "source" 값을 source 에 담는다
        # 4. source_event_counts 에서 source 의 현재 횟수(없으면 0)에 1 을 더해 source_event_counts[source] 에 담는다 (source_event_counts.get)
    return source_event_counts                              # 소스별 개수를 리턴한다


def count_missing(events, key):                             # 이벤트 리스트와 키 이름을 받는 함수
    """key 키의 값이 비어 있는(None) 이벤트 수를 리턴한다.
    분석에서 빠질 이벤트가 얼마나 되는지 미리 알아볼 때 쓴다.
    """
    missing = 0                                             # 비어 있는 개수를 0 으로 시작한다
    for event in events:                                    # 이벤트를 하나씩 꺼낸다
        if event[key] is None:                              # 그 키의 값이 비어 있으면
            missing = missing + 1                           # 비어 있는 개수를 1 늘린다
    return missing                                          # 비어 있는 개수를 리턴한다


def save_events(events, path):                              # 이벤트 리스트와 저장할 파일 이름을 받는 함수
    """이벤트 리스트를 JSON 파일로 저장한다.
    정규화 결과를 다음 분석의 입력으로 남길 때 쓴다.
    """
    with open(path, "w", encoding="utf-8") as events_file:  # 파일을 쓰기 모드("w")로 연다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. json.dump(events, events_file, ensure_ascii=False, indent=2) 로 events 를 events_file 에 저장한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 · 2번은 함수 안이라 앞에 공백 4개이고, 3 · 4번은 `for` 안쪽이라 8개이고, 5번은 `with` 안쪽이라 8개입니다.
- 4번의 `source_event_counts.get(source, 0) + 1` 에서 `get` 은 키가 없으면 두 번째 값(0)을 리턴하는 딕셔너리 메서드입니다. <mark>같은 소스가 나올 때마다 횟수가 1씩 늘어납니다.</mark>
- 번호 주석이 연달아 붙어 있어도(예: 3 · 4번), <mark>주석 사이마다 줄을 끼워 넣어 각 주석 바로 아래 줄에 그 번호의 코드를 하나씩 씁니다.</mark>
- **채우기 전에 실행하면 `IndentationError: expected an indented block` 오류가 납니다.** `for` 아래와 `with` 아래가 주석뿐이기 때문입니다.

**`exercise2-3_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 세 로그를 읽어 합치고 네 단계로 출력합니다.

```python
from normalize import load_web, merge_events, count_by_source, count_missing, save_events, EVENTS_PATH  # 방금 만든 함수를 불러온다
from normalize_json_csv import load_server, load_saas                                                   # 판정 서버 · SaaS 로그 읽기 함수를 불러온다
import json                                                                                             # 저장한 파일을 다시 읽을 수 있게 불러온다


def show_user(events, name):                                                                            # 이벤트 리스트와 사용자 이름을 받는 함수
    """한 사용자의 이벤트를 시각 · 소스 · 행동 · 결과로 한 줄씩 출력한다.
    같은 사용자가 여러 로그에서 한 일을 시간순으로 볼 때 쓴다.
    """
    for event in events:                                                                                # 이벤트를 하나씩 꺼낸다
        if event["user"] == name:                                                                       # 그 사용자의 이벤트이면
            time_text = event["time"]                                                                   # 시각
            source = event["source"]                                                                    # 소스
            action = event["action"]                                                                    # 행동
            result = event["result"]                                                                    # 결과
            print(time_text, source, action, result)                                                    # 한 줄로 출력한다


web = load_web("access_sample.log")                                                                     # 웹 서버 로그를 공통 이벤트로 바꾼다
server = load_server("server_log.jsonl")                                                                # 판정 서버 로그를 공통 이벤트로 바꾼다
saas = load_saas("saas_events.csv")                                                                     # SaaS 로그를 공통 이벤트로 바꾼다
events = merge_events(web, server, saas)                                                                # 하나로 합쳐 시간순으로 정렬한다

source_event_counts = count_by_source(events)                                                           # 소스별 개수를 센다
print("--- 단계 1: 소스별 이벤트 수")                                                                   # 단계 1 시작을 알리는 줄
print(source_event_counts)                                                                              # 소스별 개수를 출력한다

user_missing = count_missing(events, "user")                                                            # user 가 비어 있는 이벤트 수를 센다
ip_missing = count_missing(events, "ip")                                                                # ip 가 비어 있는 이벤트 수를 센다
print("--- 단계 2: user · ip 가 None 인 이벤트 수")                                                     # 단계 2 시작을 알리는 줄
print("user 가 비어 있는 이벤트", user_missing, "개")                                                   # user 가 비어 있는 개수를 출력한다
print("ip 가 비어 있는 이벤트", ip_missing, "개")                                                       # ip 가 비어 있는 개수를 출력한다

print("--- 단계 3: gaeun 의 이벤트를 시간순으로")                                                       # 단계 3 시작을 알리는 줄
show_user(events, "gaeun")                                                                              # gaeun 의 이벤트를 출력한다

save_events(events, EVENTS_PATH)                                                                        # 이벤트를 JSON 파일로 저장한다
with open(EVENTS_PATH, encoding="utf-8") as events_file:                                                # 저장한 파일을 다시 연다
    saved_events = json.load(events_file)                                                               # JSON 을 리스트로 읽는다
saved_count = len(saved_events)                                                                         # 저장된 이벤트 수를 센다
print("--- 단계 4: 저장한 파일", EVENTS_PATH)                                                           # 단계 4 시작을 알리는 줄
print("저장된 이벤트", saved_count, "개")                                                               # 저장된 이벤트 수를 출력한다
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `normalize.py` · `exercise2-3_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `normalize.py` 에서 직접 쓰는 곳 **다섯 군데**를 씁니다. 3.1 의 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise2-3_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-3_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. `--- 단계` 제목 줄은 세지 않고, 단계 1은 1줄, 단계 2는 2줄, 단계 3은 5줄, 단계 4는 1줄입니다.
5. **[VS Code]** 새로 생긴 `normalized_events.json` 을 열어 <mark>이벤트 하나가 7개 키(`time` · `source` · `user` · `ip` · `action` · `result` · `raw`)로 되어 있는지</mark> 봅니다.
6. **[보고서]** Unit 2 의 `## Exercise 2-3` › `### Exercise 2-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 소스별 이벤트 수와 `user` · `ip` 가 비어 있는 이벤트 수, 저장된 이벤트 수를 적어 주세요.
   - (나) [핵심 질문] 단계 3의 gaeun 이벤트를 보고, 서로 다른 소스에서 나온 이벤트가 어떤 순서로 나오는지 적고, 로그를 따로 볼 때와 무엇이 달라지는지 적어 주세요.
   - (다) [핵심 질문] `user` 가 비어 있는 이벤트가 28개입니다. 어느 로그(소스)의 이벤트이고 왜 비어 있는지 적어 주세요. 그리고 사용자 이름별로 개수를 세면 이 28개가 어떻게 될지 예상해 적어 주세요.

## Exercise 2-3 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 리스트 세 개를 하나로 | `events = web + server + saas` |
| 시간순으로 정렬(이른 시각이 앞, 오름차순) | `events.sort(key=get_time)` (`sort` 는 리턴값이 없음) |
| 소스별 개수 | `source = event["source"]` → `source_event_counts[source] = source_event_counts.get(source, 0) + 1` |
| JSON 파일로 저장 | `json.dump(events, f, ensure_ascii=False, indent=2)` |

---

## 마무리 · 이번 Unit 작업 확인하기

이번 Unit의 작업을 깃허브에 올리는 일은 Unit 3의 Exercise 3-2 마지막에 한 번에 합니다. <mark>이번 Unit에서는 파일이 모두 있는지만 확인합니다.</mark>

**순서**

1. **[터미널]** `anomaly_detection` 폴더에서 이번 Unit에서 만든 파일이 있는지 확인합니다.
   ```bash
   pwd
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
   - `normalize_web.py` · `normalize_json_csv.py` · `normalize.py` · `exercise2-1_run.py` · `exercise2-2_run.py` · `exercise2-3_run.py` · `normalized_events.json` · `server_log.jsonl` · `saas_events.csv` 와 이 안내 · 보고서 두 파일이 보여야 합니다.
2. **[보고서]** Unit 2 보고서의 Exercise 2-1 ~ Exercise 2-3 칸에서 `답:` 뒤가 비어 있는 질문이 없는지 봅니다. <mark>못 적은 칸은 `모름 — 막힌 곳: …` 으로 적습니다.</mark>

---

## 이번 Unit 마무리

| 확인 | 문제 |
|---|---|
| 웹 서버 로그 한 줄을 공통 이벤트로 바꿨다 | Exercise 2-1 |
| 판정 서버 로그와 SaaS 로그를 공통 이벤트로 바꿨다 | Exercise 2-2 |
| 세 로그를 합쳐 시간순으로 정렬하고 `normalized_events.json` 으로 저장했다 | Exercise 2-3 |

Unit 3에서는 이 `normalized_events.json` 과 같은 모양의 파일을 **판다스**로 읽어서 실패한 이벤트를 골라 세고, 사용자별 · 시간대별로 묶습니다. 판다스 설치를 Unit 1 마무리 때 미리 했다면 확인만 합니다.

---

<!-- learn:answers -->
