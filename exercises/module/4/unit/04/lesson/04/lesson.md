---
id: m4-u04-l04
title: 실습 4-3 · 이벤트 유형 정하고 유형별로 세기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/102_day03_am_baseline_login.md
  mission_id: GichanSource.m4-1104-am-baseline-login
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 4-3 · 이벤트 유형 정하고 유형별로 세기

## 이번 의뢰: 이벤트 유형 나누기

> **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「알림이 와도 담당자는 어떤 유형의 일인지부터 알아야 다음에 할 일을 정합니다. 이벤트마다 유형을 분류하고, 유형별로 몇 개씩인지 보여 주세요.
>
> 이번에는 두 유형만 구분하면 됩니다. 하나는 로그인에 실패한 것, 다른 하나는 관리자 경로에 접근했다가 실패한 것입니다. 나머지 실패는 「기타 실패」, 성공은 「정상」으로 분류해 주세요.」
> - **왜 중요한가**: <mark>알림이 100개 와도 유형을 모르면 처음부터 하나씩 읽어야 합니다.</mark> 유형별 개수를 보면 비정상 로그인이 많은지, 비인가 접근이 많은지 보고 어디부터 볼지 정할 수 있습니다.

## 왜 이벤트에 유형 이름을 붙이는가

1. 실습 4-2에서는 「로그인 실패」 하나만 찾았습니다. 실제 관제에서는 로그인 실패 · 관리자 경로 접근 · 요청 급증처럼 <mark>평소와 다른 일이 여러 유형으로 동시에 들어옵니다.</mark>
2. 이벤트마다 **유형 이름**을 정해 두면, <mark>유형별로 세고 유형별로 다르게 대응할 수 있습니다.</mark>

## 3.1 이벤트 유형과 이번 Unit에서 쓰는 규칙

관제에서 알리는 일은 다섯 가지 유형으로 나눕니다. 이번 Unit에서는 <mark>표의 첫 두 가지(비정상 로그인 · 비인가 접근)만 구분하고</mark>, 나머지 실패는 「기타 실패」, 성공은 「정상」으로 모읍니다(나머지 유형은 Unit 5와 Unit 6에서 다룹니다).

| 유형 | 로그에서 보이는 모양 | 다루는 Unit |
|---|---|---|
| 비정상 로그인 | 로그인 요청이 실패함 | 이번 Unit |
| 비인가 접근 | 관리자 경로(`/admin`)를 요청했다가 실패함 | 이번 Unit |
| 트래픽 급증 | 짧은 시간에 요청이 많이 들어옴 | Unit 5 |
| SaaS 이상 사용 | 평소와 다른 서비스 사용(대량 내려받기 등) | Unit 6 |
| 악성 행위 징후 | 없는 경로를 차례로 확인하는 시도 등 | Unit 6 |

이번 Unit에서 유형 이름을 정하는 순서입니다. **1번 규칙부터 차례로 확인해서, 처음 조건을 충족하는 규칙의 유형 이름을 붙이고 멈춥니다.** 예: 결과가 실패이고 행동이 `POST /login` 인 이벤트는 1번 조건을 충족하므로 「비정상 로그인」이고, <mark>2번부터는 보지 않습니다.</mark>

| 순서 | 조건 | 유형 이름 |
|---|---|---|
| 1 | 결과가 실패이고 행동이 `POST /login` | 비정상 로그인 |
| 2 | 결과가 실패이고 행동에 `/admin` 이 들어 있음 | 비인가 접근 |
| 3 | 결과가 실패(위 두 가지가 아님) | 기타 실패 |
| 4 | 그 밖(성공) | 정상 |

- 유형 이름은 이벤트 **한 건**에 붙이는 이름입니다.
- <mark>로그인에 1번만 실패한 이벤트도 「비정상 로그인」입니다.</mark> 알림을 낼지는 실습 4-2처럼 실패 횟수로 따로 정합니다.
- 「정상」은 결과가 성공이라는 유형 이름이며, <mark>공격이 아니라는 뜻이 아닙니다.</mark> 실습 4-2의 2.1 표에서 본 203.0.113.50 의 15번 행(`POST /login` 성공)도 유형은 「정상」이고, 실패 뒤 성공이 먼저 살펴볼 일인지는 그 전후의 이벤트를 함께 봐서 판단합니다.
- SaaS 로그의 로그인 실패(jiwoo, 행동 `login`)는 행동이 `POST /login` 이 아니라서 1번 규칙의 <mark>조건을 충족하지 않아 「기타 실패」가 됩니다.</mark>
- 샘플에서 실패한 이벤트는 모두 **23개**입니다.
- 규칙의 `and` 는 <mark>이벤트 한 건의 값 하나씩을 이으므로 `and` 를 씁니다.</mark> 실습 4-2에서 표의 열끼리 이을 때만 `&` 를 썼습니다.

**문법 상자 — 문자열 안에 다른 문자열이 있는지 `in`**

**<mark>`작은 문자열 in 큰 문자열`</mark> 은 큰 문자열 안에 작은 문자열이 들어 있으면 `True`, 없으면 `False` 입니다**

`==` 는 문자열 전체가 같아야 `True` 이지만, <mark>`in` 은 일부만 들어 있어도 `True` 입니다.</mark> 그래서 `GET /admin` 도 `GET /admin/users` 도 `"/admin" in action` 으로 한 번에 찾습니다.

```python
action = "GET /admin/users"                 # 이벤트의 action 값 예
has_admin = "/admin" in action              # action 안에 /admin 이 있는지 True 또는 False 로 구한다
print(has_admin)                            # True

other_action = "GET /login"                 # /admin 이 없는 action 값 예
has_admin_other = "/admin" in other_action  # other_action 안에 /admin 이 있는지 구한다
print(has_admin_other)                      # False
```

실행 결과:

```
True
False
```

- 읽는 법: <mark>첫 번째 출력은 `GET /admin/users` 안에 `/admin` 이 있어서 `True`</mark>, 두 번째 출력은 `GET /login` 안에 없어서 `False` 입니다.
- `if` 조건에 그대로 씁니다(`if "/admin" in action:`). **`== True` 는 붙이지 않습니다.** `for … in` 과는 다른 쓰임입니다.

**판다스 문법 상자 — 표를 딕셔너리 리스트로 바꾸기**

**<mark>`표.to_dict("records")`</mark> 는 표의 행을 딕셔너리 하나씩으로 바꾸고, 그 딕셔너리들을 리스트로 리턴합니다. 열 이름은 키가 되고, 그 행의 데이터는 그 키의 값이 됩니다**

이벤트 표의 한 행이 딕셔너리 하나로 바뀌므로, 이후에는 판다스가 아니라 Module 3(접근통제)에서 쓰던 `for` 와 `event["키"]` 로 하나씩 처리할 수 있습니다.

| 표의 0번 행 | `to_dict("records")` 로 바꾼 뒤 |
|---|---|
| `time` 열이 2026-11-02 02:14:08 | `{"time": "2026-11-02 02:14:08", …}` |
| `user` 열이 jiwoo | `"user": "jiwoo"` |
| `action` 열이 login | `"action": "login"` |

```python
import pandas as pd                                          # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                     # 연습용 작은 데이터 — 행 하나가 이벤트 하나
    "time": ["2026-11-02 02:14:08", "2026-11-02 09:05:30"],  # time 열에 들어갈 값들
    "user": ["jiwoo", "seoyeon"],                            # user 열에 들어갈 값들
    "action": ["login", "login"],                            # action 열에 들어갈 값들
}
events = pd.DataFrame(data)                                  # 데이터로 표를 만든다 — 실제 파일은 read_json 이 표로 읽어 준다
print(events)                                                # 표를 출력한다
event_list = events.to_dict("records")                       # 표를 「한 행이 딕셔너리 하나」인 리스트로 바꾼다
first_event = event_list[0]                                  # 첫 번째 딕셔너리(표의 0번 행)를 꺼낸다
print(first_event)                                           # 열 이름이 키, 그 행의 값이 값이 된 딕셔너리
```

실행 결과:

```
                  time     user action
0  2026-11-02 02:14:08    jiwoo  login
1  2026-11-02 09:05:30  seoyeon  login
{'time': '2026-11-02 02:14:08', 'user': 'jiwoo', 'action': 'login'}
```

- 읽는 법: <mark>출력은 0번 행 하나가 딕셔너리로 바뀐 모양입니다.</mark> 키는 열 이름 3개이고 값은 그 행의 값입니다.
- `"records"` 는 **정해진 문구라서 그대로 씁니다.** 빼거나 다른 문구를 쓰면 행마다 딕셔너리 하나인 리스트가 만들어지지 않습니다.
- `classify_event` 함수는 이벤트 하나의 행동과 결과를 전달받아 규칙(`if`)을 적용합니다. <mark>그래서 표를 딕셔너리 리스트로 바꿔 이벤트를 하나씩 꺼냅니다.</mark> `if` 는 값 하나씩만 판단하기 때문입니다.
- 미리 채운 `type_event_counts.get(type_name, 0) + 1` 은 처음 보는 유형이면 0 에서 시작해 1 을 더한다는 뜻입니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_events` | 파일 경로 | 이벤트 표(미리 채움) |
| `classify_event` | 이벤트 하나의 행동과 결과 | 유형 이름(`비정상 로그인` · `비인가 접근` · `기타 실패` · `정상`) |
| `count_types` | 이벤트 표 | `{유형: 개수}` 딕셔너리 |

- **직접 쓰는 곳은 다섯 군데**(번호 1 ~ 5)이고, 함수 두 개 안에 나뉘어 있습니다.
  - `classify_event`(1 ~ 4번): 위 순서대로 1번 · 2번 규칙을 `if` 로 씁니다. 나머지 두 규칙은 미리 채웠습니다.
  - `count_types`(5번): 표를 딕셔너리 리스트로 바꿉니다. 하나씩 꺼내 세는 줄은 미리 채웠습니다.

## 실습 4-3 · 이벤트 유형 정하고 유형별로 세기

**이런 상황이 있습니다**

- **지금은**: 이벤트 57개는 성공 · 실패만 나뉘어 있어서, 실패가 어떤 일인지 알 수 없습니다.
- **그래서 만드는 것**: `classify.py` 입니다.
  - 이벤트 하나의 행동과 결과로 유형 이름을 정합니다.
  - 유형 이름별로 몇 개인지 셉니다.
- **실행하면**: 단계 1: 유형별 이벤트 수(4줄), 단계 2: 전체 이벤트 수가 나옵니다.
- **현업에서는**: 알림에 유형 이름이 적혀 있으면 담당자가 그 유형의 처리 절차(비밀번호 초기화, 주소 차단 등)를 바로 찾습니다.

**할 일**

1. `classify.py` · `exercise4-3_run.py` **두 파일**을 만들고, `classify.py` 의 `classify_event` · `count_types` 에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>유형별 이벤트 수</mark>(단계 1)와 <mark>전체 이벤트 수</mark>(단계 2)를 읽습니다.

**`classify.py`**

```python
import pandas as pd                                                             # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"                                          # 읽을 정규화 이벤트 파일 이름
TYPE_ORDER = ["비정상 로그인", "비인가 접근", "기타 실패", "정상"]              # 결과를 보여 줄 유형 순서


def load_events(path):                                                          # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                                                 # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                                               # 이벤트 표를 리턴한다


def classify_event(action, result):                                             # 행동과 결과를 받는 함수
    """이벤트 하나의 유형 이름을 정한다.
    알림이 온 이벤트가 어떤 유형의 일인지 담당자가 바로 알 수 있게 할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. if 로 시작한다: result 가 "실패" 이고(and) action 이 "POST /login" 과 같으면
    # 2.   그 if 안쪽에서 "비정상 로그인" 을 리턴한다
    # 3. if 로 시작한다: result 가 "실패" 이고(and) "/admin" in action 이 True 이면
    # 4.   그 if 안쪽에서 "비인가 접근" 을 리턴한다
    if result == "실패":                                                        # 위 두 유형이 아닌 실패이면
        return "기타 실패"                                                      # 기타 실패로 분류한다
    return "정상"                                                               # 실패가 아니면 정상이다


def count_types(events):                                                        # 이벤트 표를 받는 함수
    """유형별 이벤트 수를 {유형: 개수} 딕셔너리로 센다.
    어떤 유형의 일이 얼마나 있는지 한눈에 볼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. events.to_dict("records") 로 표를 딕셔너리 리스트로 바꿔 event_list 에 담는다
    type_event_counts = {}                                                      # 유형별 횟수를 담을 딕셔너리
    for event in event_list:                                                    # 이벤트를 하나씩 꺼낸다
        action = event["action"]                                                # 그 이벤트의 행동
        result = event["result"]                                                # 그 이벤트의 결과
        type_name = classify_event(action, result)                              # 유형 이름을 정한다
        type_event_counts[type_name] = type_event_counts.get(type_name, 0) + 1  # type_event_counts 에 이 유형이 있으면 그 값을, 없으면 0 을 꺼내 1 을 더하고 다시 저장한다
    return type_event_counts                                                    # 유형별 횟수를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 · 3번은 함수 안이라 앞에 공백 4개이고, 2 · 4번의 `return` 은 `if` 안쪽이라 8개이며, 5번은 공백 4개입니다.
- 번호 주석이 연달아 붙어 있어도, 주석 사이마다 줄을 끼워 넣어 **각 주석 바로 아래 줄에 그 번호의 코드를 하나씩 씁니다.**
- 채우기 전에 실행하면 `NameError: name 'event_list' is not defined` 오류가 납니다. 5번을 아직 안 썼기 때문입니다.

**`exercise4-3_run.py`** — <mark>그대로 붙여 넣습니다.</mark> 직접 쓰는 줄은 없습니다. `.values()` 는 딕셔너리의 값(개수)만 꺼내고, `sum(…)` 은 그 숫자를 모두 더합니다.

```python
from classify import load_events, count_types, EVENTS_PATH, TYPE_ORDER  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)                                       # 이벤트 파일을 표로 읽는다
type_event_counts = count_types(events)                                 # 유형별로 센다
print("--- 단계 1: 유형별 이벤트 수")                                   # 단계 1 시작을 알리는 줄
for type_name in TYPE_ORDER:                                            # 정해 둔 유형 순서대로 꺼낸다
    count = type_event_counts.get(type_name, 0)                         # 그 유형의 개수(없으면 0)
    print(type_name, count)                                             # 유형과 개수를 출력한다

values = type_event_counts.values()                                     # 유형별 개수만 꺼낸다
total = sum(values)                                                     # 모든 유형의 개수를 더한다
print("--- 단계 2: 전체 이벤트", total, "개")                           # 단계 2 시작을 알리는 줄과 전체 개수
```

**순서**

1. **[VS Code]** 파일 `classify.py` · `exercise4-3_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `classify.py` 에서 직접 쓰는 곳 **다섯 군데**를 씁니다. 3.1 의 규칙 순서와 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise4-3_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise4-3_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **두 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1은 4줄이고, 단계 2는 숫자가 제목 줄에 함께 나오므로 그 아래 줄이 없습니다.
5. **[보고서]** `report_u4.md` 의 `## 실습 4-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 유형별 이벤트 수를 적어 주세요.
   - (나) [핵심 질문] 「기타 실패」(결과가 실패이면서 `POST /login` 도 아니고 `/admin` 도 없는 이벤트)는 실패한 유형 중 15개로 가장 많습니다. 샘플 이벤트에서 `source` 가 `server` 인 이벤트 하나와 `web` 인 이벤트 하나를 찾아, 각각 `action` 과 함께 적어 주세요(예: `server` 의 `ACCOUNT:CHANGE`, `web` 의 `GET /.env` 처럼 규칙 1 · 2번에 걸리지 않는 것). 그리고 이 둘이 같은 이름 「기타 실패」로 묶여 있으면 담당자가 무엇을 하기 어려운지 적어 주세요.
   - (다) [핵심 질문] 유형 규칙은 위에서부터 차례로 보고 먼저 조건을 충족하는 것으로 정합니다. 「기타 실패」(결과가 실패이면 충족)를 맨 위로 옮겼다고 합시다. 그러면 「비정상 로그인」 · 「비인가 접근」 · 「기타 실패」 이벤트는 각각 몇 개가 될까요? 그리고 그때 담당자가 구분하지 못하게 되는 것은 무엇인가요?

## 실습 4-3 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 비정상 로그인 | `if result == "실패" and action == "POST /login":` → `return "비정상 로그인"` |
| 비인가 접근 | `if result == "실패" and "/admin" in action:` → `return "비인가 접근"` |
| 표를 리스트로 | `event_list = events.to_dict("records")` |
| 유형별 세기 | `type_event_counts[type_name] = type_event_counts.get(type_name, 0) + 1` (미리 채움) |

---

## 마무리 · 만든 파일 확인하기

이번 Unit의 작업을 깃허브에 올리는 일은 Unit 5의 실습 5-2 마지막에 한 번에 합니다. <mark>이번 Unit에서는 파일이 모두 있는지만 확인합니다.</mark>

**순서**

1. **[터미널]** `anomaly_detection` 폴더에서 이번 Unit에서 만든 파일이 있는지 확인합니다.
   ```bash
   pwd
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
   - `baseline.py` · `login_detection.py` · `classify.py` · `exercise4-1_run.py` · `exercise4-2_run.py` · `exercise4-3_run.py` · `normalized_events.json` · `baseline_logins.csv` 와 <mark>`report_u4.md` 가 보여야</mark> 합니다.
2. **[보고서]** `report_u4.md` 의 실습 4-1 ~ 실습 4-3 칸에서 `답:` 뒤가 비어 있는 질문이 없는지 봅니다. 못 적은 칸은 `모름 — 막힌 곳: …` 으로 적습니다.

---

## 이번 Unit 마무리

| 확인 | 문제 |
|---|---|
| 지난 7일 숫자로 평소 기준을 구하고 알림 기준(5번)을 정했다 | 실습 4-1 |
| 같은 주소의 로그인 실패가 알림 기준(5번) 이상인 곳을 찾았다 | 실습 4-2 |
| 이벤트의 유형을 정하고 유형별로 셌다 | 실습 4-3 |

Unit 5에서는 분 단위로 요청 수를 세어 **요청이 갑자기 늘어난 때**(트래픽 급증)를 찾고, Unit 4의 알림을 한 파일로 모읍니다.

---

<!-- learn:answers -->
