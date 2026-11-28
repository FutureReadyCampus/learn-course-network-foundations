---
id: m4-u02-l03
title: 실습 2-2 · JSON·CSV 로그를 이벤트로
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/098_day02_am_normalize.md
  mission_id: GichanSource.m4-1103-am-normalize
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 2-2 · JSON·CSV 로그를 이벤트로

## 목표: JSON·CSV 이벤트 변환

> **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「웹 서버 로그는 공통 이벤트로 바꿨습니다. 나머지 두 로그도 같은 모양으로 맞춰 주세요.
>
> - 판정 서버 로그(Module 3에서 만든 서버가 남기는 JSON): 접속 주소가 없습니다.
> - SaaS 로그(CSV): 사용자가 메일 주소(`seoyeon@a-corp.example`)로 적혀 있으니 이름만 꺼내 주세요.
> - 두 로그 모두 성공 · 실패를 웹 서버 로그처럼 `성공` · `실패` 로 통일해 주세요.」
> - **왜 중요한가**: <mark>같은 사람이 로그마다 `seoyeon` 과 `seoyeon@a-corp.example` 로 적히면 사용자별로 세거나 이어 볼 수 없습니다.</mark> 접속 주소가 원래 없는 로그에는 임의의 주소를 채우지 말고 `None` 으로 둡니다. 가짜 주소로 세어지는 이벤트가 생기기 때문입니다.

## 왜 두 로그도 같은 키로 맞추는가

1. 실습 2-1에서는 웹 서버 로그 한 종류를 바꿨습니다. 같은 방법을 나머지 두 종류에 적용합니다.
2. <mark>로그마다 어려운 곳이 다릅니다.</mark>
   - 판정 서버 로그: 시각이 `2026-11-02T09:40` 처럼 `T` 로 나뉘어 있고 초가 없습니다. 접속 주소가 없습니다.
   - SaaS 로그: 시각은 이미 공통 모양입니다. 사용자가 메일 주소입니다.

## 2.1 CSV 읽기와 딕셔너리로 값 바꾸기

<h2>문법 상자 — CSV 파일을 딕셔너리로 읽기</h2>

**<mark>`csv.DictReader`</mark> 는 CSV 파일의 첫 줄을 열 이름으로 삼아, 둘째 줄부터 한 줄씩 「열 이름: 값」 딕셔너리로 읽어 줍니다**

```python
import csv  # CSV 파일을 읽는 csv 모듈을 불러온다

rows = []  # 행을 모을 리스트
with open("saas_events.csv", encoding="utf-8", newline="") as saas_file:  # CSV 파일을 연다
    reader = csv.DictReader(saas_file)  # 첫 줄을 열 이름으로 삼아 행마다 딕셔너리로 읽는다
    for row in reader:  # 행을 하나씩 꺼낸다
        rows.append(row)  # 리스트에 추가한다
first_row = rows[0]  # 첫 행을 꺼낸다
print(first_row)  # 첫 행(딕셔너리)을 출력한다

row_count = len(rows)  # 행이 몇 개인지 센다
print(row_count)  # 행 수를 출력한다
```

실행 결과:

```
{'time': '2026-11-02 02:14:08', 'account': 'jiwoo@a-corp.example', 'event': 'login', 'ip_address': '203.0.113.80', 'outcome': 'failure'}
14
```

CSV 한 줄이 딕셔너리 하나로 바뀌는 모양입니다.

| | 모양 |
|---|---|
| CSV 첫 줄(열 이름) | `time,account,event,ip_address,outcome` |
| CSV 둘째 줄(값) | `2026-11-02 02:14:08,jiwoo@a-corp.example,login,203.0.113.80,failure` |
| `DictReader` 가 만든 딕셔너리 | `{"time": "2026-11-02 02:14:08", "account": "jiwoo@a-corp.example", "event": "login", "ip_address": "203.0.113.80", "outcome": "failure"}` |

- CSV(씨에스브이)는 값을 쉼표로 나눠 적은 표 파일입니다. <mark>첫 줄은 열 이름(`time,account,event,…`)입니다.</mark>
- `csv.DictReader(saas_file)` 로 만든 `reader` 를 `for row in reader:` 로 돌리면 행마다 `{"time": …, "account": …}` 딕셔너리가 나옵니다. <mark>그래서 `row["account"]` 처럼 이름으로 값을 꺼냅니다.</mark>
- <mark>CSV 파일을 열 때는 `newline=""` 을 함께 씁니다.</mark> 줄바꿈을 csv 모듈이 직접 처리하게 하는 관례입니다.

<h2>문법 상자 — 딕셔너리로 값을 다른 값으로 바꾸기</h2>

**딕셔너리에 「원래 값: 바꿀 값」을 짝지어 두면 <mark>`딕셔너리[키]`</mark> 한 줄로 값을 다른 값으로 바꿀 수 있습니다. 예: `"failure"` → `"실패"`**

```python
RESULT_MAP = {"success": "성공", "failure": "실패"}  # SaaS 의 outcome 을 바꾸는 딕셔너리
outcome = "failure"  # 바꿀 값
result = RESULT_MAP[outcome]  # 딕셔너리에서 "failure" 에 짝지은 값을 꺼낸다
print(result)  # 바꾼 값을 출력한다

ALLOWED_MAP = {True: "성공", False: "실패"}  # 판정 서버의 allowed 를 바꾸는 딕셔너리
allowed = True  # 바꿀 값
allowed_result = ALLOWED_MAP[allowed]  # 딕셔너리에서 True 에 짝지은 값을 꺼낸다
print(allowed_result)  # 바꾼 값을 출력한다
```

실행 결과:

```
실패
성공
```

- `RESULT_MAP = {"success": "성공", "failure": "실패"}` 처럼 왼쪽(키)과 오른쪽(바꾼 값)을 짝지어 둡니다. <mark>`RESULT_MAP["failure"]` 는 `"실패"` 입니다.</mark>
- 판정 서버의 `allowed` 는 `true` / `false` 이고 파이썬에서는 `True` / `False` 입니다. `ALLOWED_MAP = {True: "성공", False: "실패"}` 로 만들면 <mark>`ALLOWED_MAP[True]` 가 `"성공"` 입니다.</mark>
- **딕셔너리에 없는 키로 꺼내면 `KeyError` 오류가 납니다.** 예상 못 한 값(`pending` 등)이 들어오면 멈추기 때문에 오류가 나는 것이 오히려 단서가 됩니다.

<h2>한 장 정리</h2>

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `convert_server_time` | 판정 서버 시각 문자열 | 공통 모양 시각 문자열 |
| `normalize_server` | 판정 서버 로그 한 줄(JSON 문자열) | 공통 이벤트(`ip` 는 `None`) |
| `normalize_saas` | CSV 한 행(딕셔너리) | 공통 이벤트(`user` 는 메일에서 꺼낸 이름) |
| `load_server` · `load_saas` | 파일 경로 | 공통 이벤트 리스트(미리 채움) |

- **직접 쓰는 곳은 세 함수**(번호 1 ~ 6)입니다.
  - `convert_server_time`(1 · 2번): 실습 2-1과 같은 방식으로 시각 모양을 바꿉니다(시간대가 없어서 `replace` 는 필요 없습니다).
  - `normalize_server`(3번): 딕셔너리에서 `allowed` 를 `"성공"` / `"실패"` 로 바꿉니다.
  - `normalize_saas`(4 ~ 6번): 메일 주소에서 이름을 꺼내고, 딕셔너리에서 `outcome` 을 바꿉니다.
- **미리 채운 것**: 파일을 읽어 이벤트 리스트로 만드는 `load_server` · `load_saas` 와 이벤트를 묶는 줄입니다.

## 실습 2-2 · JSON·CSV 로그를 이벤트로

<h2>이런 상황이 있습니다</h2>

- **지금은**: 판정 서버 로그는 시각 가운데에 `T` 가 있고 접속 주소가 없습니다. SaaS 로그는 사용자가 메일 주소이고 결과가 `success` / `failure` 입니다.
- **그래서 만드는 것**: `normalize_json_csv.py` 입니다.
  - 판정 서버: 시각을 공통 모양으로, `allowed` 를 `성공` · `실패` 로 바꿉니다.
  - SaaS: 메일 주소에서 이름만 꺼내고, `outcome` 을 `성공` · `실패` 로 바꿉니다.
- **실행하면**: 단계 1: 판정 서버 이벤트 수와 성공 · 실패별 개수, 단계 2: SaaS 이벤트 수와 성공 · 실패별 개수, 단계 3: 각 로그의 첫 이벤트가 나옵니다.
- **현업에서는**: 로그 종류가 늘면 변환 코드를 하나 더 만듭니다. <mark>결과 모양이 같아서 뒤의 탐지 코드는 고치지 않아도 됩니다.</mark>

<h2>할 일</h2>

1. **`normalize_json_csv.py` · `exercise2-2_run.py`** 두 파일을 만들고, `normalize_json_csv.py` 의 `convert_server_time` · `normalize_server` · `normalize_saas` 에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>판정 서버 이벤트 수와 성공 · 실패별 개수</mark>(단계 1), <mark>SaaS 이벤트 수와 성공 · 실패별 개수</mark>(단계 2), <mark>각 로그의 첫 이벤트</mark>(단계 3)를 읽습니다.

<h3><code>normalize_json_csv.py</code></h3>

```python
import csv  # CSV 파일을 읽는 csv 모듈을 불러온다
import json  # JSON 을 다루는 json 모듈을 불러온다
from datetime import datetime  # 날짜와 시각을 다루는 datetime 클래스를 불러온다

SERVER_TIME_FORMAT = "%Y-%m-%dT%H:%M"  # 판정 서버 시각의 모양(예: 2026-11-02T09:40)
COMMON_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"  # 공통 시각의 모양(예: 2026-11-02 09:40:00)
ALLOWED_MAP = {True: "성공", False: "실패"}  # 판정 서버의 allowed 값을 공통 결과로 바꾸는 딕셔너리
RESULT_MAP = {"success": "성공", "failure": "실패"}  # SaaS 의 outcome 값을 공통 결과로 바꾸는 딕셔너리


def convert_server_time(time_text):  # 판정 서버 시각 문자열을 받는 함수
    """판정 서버 시각을 공통 모양의 문자열로 바꾼다.
    예: 2026-11-02T09:40 → 2026-11-02 09:40:00.
    판정 서버 로그를 공통 이벤트로 만들 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. datetime.strptime(time_text, SERVER_TIME_FORMAT) 의 결과를 parsed 에 담는다
    # 2. parsed.strftime(COMMON_TIME_FORMAT) 의 결과를 time_out 에 담는다
    return time_out  # 공통 모양의 시각 문자열을 리턴한다


def normalize_server(line):  # 판정 서버 로그 한 줄(JSON 문자열)을 받는 함수
    """판정 서버 로그 한 줄을 공통 이벤트 딕셔너리로 바꾼다.
    판정 서버 로그를 다른 로그와 같은 모양으로 맞출 때 쓴다.
    """
    item = json.loads(line)  # JSON 문자열을 딕셔너리로 바꾼다
    time_out = convert_server_time(item["time"])  # 공통 모양의 시각으로 바꾼다
    allowed = item["allowed"]  # 허용이었는지(True 또는 False)
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 3. ALLOWED_MAP 에서 allowed 에 해당하는 값을 꺼내 result 에 담는다 (ALLOWED_MAP[allowed])
    raw_text = line.strip()  # 원래 줄(양끝 공백과 줄바꿈 뺀 것)을 보관한다
    event = {  # 공통 이벤트의 키로 묶는다
        "time": time_out,  # 일어난 시각
        "source": "server",  # 어느 로그에서 왔는지
        "user": item["user"],  # 요청한 사용자
        "ip": None,  # 판정 서버 로그에는 접속 주소가 없다
        "action": item["permission"],  # 요청한 권한
        "result": result,  # 성공인지 실패인지
        "raw": raw_text,  # 원래 로그 줄
    }
    return event  # 공통 이벤트를 리턴한다


def normalize_saas(row):  # SaaS CSV 한 행(딕셔너리)을 받는 함수
    """SaaS 로그 한 행을 공통 이벤트 딕셔너리로 바꾼다.
    SaaS 로그를 다른 로그와 같은 모양으로 맞출 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. row["account"] 를 "@" 기준으로 나눠 account_parts 에 담는다 (account 예: seoyeon@a-corp.example)
    # 5. account_parts 의 첫 값을 user 에 담는다
    outcome = row["outcome"]  # success 또는 failure
    # 6. RESULT_MAP 에서 outcome 에 해당하는 값을 꺼내 result 에 담는다
    event = {  # 공통 이벤트의 키로 묶는다
        "time": row["time"],  # SaaS 시각은 이미 공통 모양이라 그대로 쓴다
        "source": "saas",  # 어느 로그에서 왔는지
        "user": user,  # 메일 주소에서 꺼낸 사용자 이름
        "ip": row["ip_address"],  # 접속 주소
        "action": row["event"],  # 무엇을 했는지
        "result": result,  # 성공인지 실패인지
        "raw": row,  # 원래 CSV 행(딕셔너리)을 보관한다
    }
    return event  # 공통 이벤트를 리턴한다


def load_server(path):  # 판정 서버 로그 파일 경로를 받는 함수
    """판정 서버 로그 파일의 모든 줄을 공통 이벤트 리스트로 바꾼다.
    판정 서버 로그를 정규화 결과에 합칠 준비를 할 때 쓴다.
    """
    events = []  # 결과를 담을 리스트
    with open(path, encoding="utf-8") as server_file:  # 파일을 연다
        for line in server_file:  # 한 줄씩 꺼낸다
            event = normalize_server(line)  # 공통 이벤트로 바꾼다
            events.append(event)  # 리스트에 추가한다
    return events  # 이벤트 리스트를 리턴한다


def load_saas(path):  # SaaS CSV 파일 경로를 받는 함수
    """SaaS CSV 파일의 모든 행을 공통 이벤트 리스트로 바꾼다.
    SaaS 로그를 정규화 결과에 합칠 준비를 할 때 쓴다.
    """
    events = []  # 결과를 담을 리스트
    with open(path, encoding="utf-8", newline="") as saas_file:  # 파일을 연다(CSV 는 newline="" 을 붙인다)
        reader = csv.DictReader(saas_file)  # 첫 줄을 열 이름으로 삼아 행마다 딕셔너리로 읽는다
        for row in reader:  # 행을 하나씩 꺼낸다
            event = normalize_saas(row)  # 공통 이벤트로 바꾼다
            events.append(event)  # 리스트에 추가한다
    return events  # 이벤트 리스트를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 6번은 모두 함수 안이라 앞에 공백 4개입니다.
- 4번의 `split("@")` 는 Unit 1의 `split('"', 2)` 처럼 구분 문자로 나눈 리스트를 만듭니다. `seoyeon@a-corp.example` 은 `["seoyeon", "a-corp.example"]` 이 되고, <mark>5번에서 첫 값(`account_parts[0]`)을 씁니다.</mark>
- 번호 주석이 연달아 붙어 있어도(예: 4 · 5번), <mark>주석 사이마다 줄을 끼워 넣어 각 주석 바로 아래 줄에 그 번호의 코드를 하나씩 씁니다.</mark>
- **채우기 전에 실행하면 `UnboundLocalError` 또는 `NameError` 가 납니다.** 예를 들어 1 · 2번을 아직 안 썼으면 `time_out` 을 찾지 못합니다.

<h3><code>exercise2-2_run.py</code></h3>

그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 두 로그를 공통 이벤트로 바꿔 세 단계로 출력합니다.

```python
from normalize_json_csv import load_server, load_saas  # 방금 만든 파일 읽기 함수를 불러온다

server_events = load_server("server_log.jsonl")  # 판정 서버 로그를 공통 이벤트로 바꾼다
saas_events = load_saas("saas_events.csv")  # SaaS 로그를 공통 이벤트로 바꾼다

server_count = len(server_events)  # 판정 서버 이벤트 수를 센다
server_result_counts = {}  # 결과별 횟수를 담을 딕셔너리
for event in server_events:  # 이벤트를 하나씩 꺼낸다
    result = event["result"]  # 그 이벤트의 결과
    server_result_counts[result] = server_result_counts.get(result, 0) + 1  # 그 결과의 횟수를 1 늘린다
print("--- 단계 1: 판정 서버 이벤트", server_count, "개")  # 단계 1 시작을 알리는 줄
print(server_result_counts)  # 성공 · 실패별 개수를 출력한다

saas_count = len(saas_events)  # SaaS 이벤트 수를 센다
saas_result_counts = {}  # 결과별 횟수를 담을 딕셔너리
for event in saas_events:  # 이벤트를 하나씩 꺼낸다
    result = event["result"]  # 그 이벤트의 결과
    saas_result_counts[result] = saas_result_counts.get(result, 0) + 1  # 그 결과의 횟수를 1 늘린다
print("--- 단계 2: SaaS 이벤트", saas_count, "개")  # 단계 2 시작을 알리는 줄
print(saas_result_counts)  # 성공 · 실패별 개수를 출력한다

first_server = server_events[0]  # 판정 서버 첫 이벤트를 꺼낸다
first_saas = saas_events[0]  # SaaS 첫 이벤트를 꺼낸다
print("--- 단계 3: 각 로그의 첫 이벤트")  # 단계 3 시작을 알리는 줄
print(first_server)  # 판정 서버 첫 이벤트를 출력한다
print(first_saas)  # SaaS 첫 이벤트를 출력한다
```

<h2>순서</h2>

1. **[VS Code]** 파일 `normalize_json_csv.py` · `exercise2-2_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `normalize_json_csv.py` 에서 직접 쓰는 곳 **여섯 군데**를 씁니다. 2.1 의 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise2-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **세 단계**입니다. `--- 단계` 제목 줄은 세지 않고, 단계 1은 1줄, 단계 2는 1줄, 단계 3은 2줄입니다.
5. **[실습 기록]** `report_u2.md` 의 `## 실습 2-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 판정 서버와 SaaS 이벤트의 수와 성공 · 실패별 개수를 적어 주세요.
   - (나) [핵심 질문] 판정 서버 로그에는 접속 주소가 없어서 `ip` 를 `None` 으로 두었습니다. `None` 대신 가짜 주소 `0.0.0.0` 을 넣으면 주소별로 셀 때 어떤 문제가 생길까요? 이유도 함께 적어 주세요.
   - (다) [핵심 질문] 정규화하면서 공통 이벤트의 키에 들어가지 않은 정보를 판정 서버 로그에서 찾아 적고, 그 정보를 나중에 어디서 찾을 수 있는지 적어 주세요.

<!-- answer: 05|실습 2-2 정답 -->

## 실습 2-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 판정 서버 시각 바꾸기 | `parsed = datetime.strptime(time_text, SERVER_TIME_FORMAT)` → `time_out = parsed.strftime(COMMON_TIME_FORMAT)` |
| `allowed` → 성공 · 실패 | `result = ALLOWED_MAP[allowed]` |
| 메일 주소에서 이름 꺼내기 | `account_parts = row["account"].split("@")` → `user = account_parts[0]` |
| `outcome` → 성공 · 실패 | `result = RESULT_MAP[outcome]` |
| CSV 를 딕셔너리로 읽기 | `reader = csv.DictReader(saas_file)` → `for row in reader:` |

---
