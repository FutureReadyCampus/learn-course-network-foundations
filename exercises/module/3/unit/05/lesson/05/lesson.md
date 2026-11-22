---
id: m3-u05-l05
title: 응용 5-1 · 로그 집계와 주간 보고서 만들기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/094_day06_am_weekly_report.md
  mission_id: GichanSource.m3-1102-am-weekly-report
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 응용 5-1 · 로그 집계와 주간 보고서 만들기

## 목표: 로그 집계와 주간 보고서

> **여유가 되면 해 보세요.** 핵심 실습 5-1 · 5-2와 글쓰기를 먼저 마칩니다. 이 응용을 하지 않아도 주간 보고서는 제공 파일로 이미 만들어졌고, Module 4를 따라가는 데도 문제가 없습니다.

> **이번 응용에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지:
> 「점검 결과 말고 하나 더 있습니다. 판정 서버는 요청마다 로그를 한 줄 남기는데, 그 로그를 제대로 읽어 본 사람이 없습니다. 지난주에 한 직원이 "자꾸 접근이 거부된다"고 문의했을 때 로그 파일을 열어 그 직원의 거부 횟수를 세는 데만 오래 걸렸습니다. 실제 서버의 일주일 치는 수천 줄이고, 이번에 쓰는 샘플은 40줄입니다.
>
> 일주일 동안 요청이 몇 번 허용되고 몇 번 거부됐는지, 거부 사유는 무엇이 많은지, 같은 사람이 반복해서 거부됐는지를 숫자로 알려 주세요. 거부 비율이 평소보다 높으면 먼저 알 수 있게 기준(예: 30%)을 정해 두고, 기준을 넘으면 「경고」라고 표시해 주세요. 점검 결과와 이 숫자를 합쳐 주간 회의에 낼 한 장짜리 보고서까지 만들어 주세요.」
> - **왜 중요한가**: 거부가 갑자기 늘면 퇴사자 계정이나 밖에서 들어오는 시도가 늘었다는 신호일 수 있습니다. 로그를 사람이 세면 오래 걸리고 기준이 사람마다 달라집니다. 코드가 같은 기준으로 세고 경고를 붙이면 담당자는 경고가 붙은 곳부터 볼 수 있습니다. 경고는 공격이 확정됐다는 뜻이 아니라 먼저 살펴볼 곳이라는 뜻입니다.

## 왜 로그를 집계하는가

1. 서버 로그는 한 줄씩 쌓이기만 하고, 그대로는 「이번 주에 무슨 일이 있었나」를 알 수 없습니다.
2. 그래서 로그를 읽어 **세고(집계), 비율을 구하고, 기준과 비교**합니다.
   - 거부율 = 거부된 요청 수 ÷ 전체 요청 수
   - 거부율이 **경고 기준** 이상이면 경고입니다. 기준은 코드가 아니라 `config/alert.json` 에 둡니다.
3. 경고는 「살펴볼 필요가 있다」는 표시이고, 공격이 있었다는 뜻이 아닙니다.

## 2.1 로그 한 줄과 집계 함수

`week_log.jsonl` 의 한 줄은 요청 한 개이고, 아래 여섯 키로 이루어집니다.

| 키 | 뜻 | 값의 예 |
|---|---|---|
| `time` | 요청한 시각 | `"2026-10-26T09:10"` |
| `user` | 요청한 사용자 | `"seoyeon"` |
| `permission` | 요청한 권한(자원:행위) | `"SALES:QUERY"` |
| `network` | 접속 위치 | `"office"` |
| `allowed` | 허용 여부 | `true` · `false` |
| `reason` | 허용 또는 거부 이유 | `"퇴사한 계정"` |

- 이 샘플 로그의 허용 이유는 `역할 권한` 하나이고, 거부 이유는 네 가지입니다.
  - `퇴사한 계정` · `역할이 없음`(사용자의 역할이 역할 파일에 없음) · `업무 시간 밖` · `허용되지 않은 접속 위치`

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 | 직접 쓰는 곳 |
|---|---|---|---|
| `read_log` | 로그 파일 경로 | 요청 딕셔너리의 리스트(JSON 한 줄이 딕셔너리 하나) | 1 · 2번 |
| `count_by` | 요청 리스트, 센 기준(키 이름) | `{값: 횟수}` 딕셔너리(예: 사용자별 · 사유별 횟수) | 3 ~ 5번 |
| `filter_denied` | 요청 리스트 | 거부된 요청의 리스트 | 6 · 7번 |
| `deny_rate` | 요청 리스트 | 거부율(0 ~ 1). 요청이 0개이면 0.0 | 8 · 9번 |
| `find_heavy_users` | 사용자별 거부 횟수 딕셔너리, 기준 횟수 | 기준 이상 거부된 사용자 이름의 리스트 | 10 · 11번 |

- **직접 쓰는 곳은 다섯 함수**(번호 1 ~ 11)입니다. 판단이 필요한 함수마다 2 ~ 3줄만 쓰고, 나머지는 미리 채웠습니다.
  - `deny_rate` 는 요청이 하나도 없는 경우(8 · 9번)를 먼저 처리합니다.
- **미리 채운 것**: 반복 구조, `deny_rate` 의 나눗셈 줄, 마지막 `return` 입니다.

<figure class="page-figure"><img src="assets/f01.svg" alt="요청 로그를 읽어 거부 요청을 세고, 거부율로 경고를 정하는 함수 흐름"></figure>

**문법 상자 — JSON 한 줄 읽기 · 퍼센트 만들기 · 값별로 세기**

**① `json.loads` 는 JSON 문자열을 딕셔너리로 바꿉니다**

```python
import json                                                      # JSON 문자열을 딕셔너리로 바꾸는 모듈을 불러온다

line = '{"user": "dami", "allowed": false}\n'                     # 로그 파일에서 읽은 한 줄(끝에 줄바꿈 문자가 붙어 있다)
entry = json.loads(line)                                         # JSON 문자열을 딕셔너리로 바꾼다
print(entry["user"], entry["allowed"])                           # 사용자와 허용 여부를 출력한다
```

실행 결과:

```
dami False
```

- JSON 의 `false` 가 파이썬에서는 `False` 가 됩니다.
- 로그 파일을 `for line in log_file:` 로 읽으면 한 줄씩 꺼내지고, 각 줄을 `json.loads(line)` 으로 바꾸면 요청 한 개가 딕셔너리가 됩니다.

**② `round(숫자)` 는 소수를 가장 가까운 정수로 반올림합니다**

```python
rate = 16 / 40                                                   # 거부 16개를 전체 40개로 나눈 비율
print(rate)                                                      # 비율 그대로 출력한다

percent = round(rate * 100)                                      # 100 을 곱해 가까운 정수로 반올림한다
print(percent)                                                   # 퍼센트 숫자를 출력한다
```

실행 결과:

```
0.4
40
```

`round(숫자)` 는 정수로 반올림하고, 소수 첫째 자리까지 남기고 싶으면 `round(숫자, 1)` 처럼 뒤에 자리 수를 적습니다(2.43 → 2.4).

숫자 뒤에 `%` 를 붙여 문자열로 만들려면 f-문자열을 씁니다.

```python
percent = 40                                                     # 위에서 구한 퍼센트 숫자
percent_text = f"{percent}%"                                     # 숫자 뒤에 % 를 붙인 문자열을 만든다
print(percent_text)                                              # 만든 문자열을 출력한다
```

실행 결과:

```
40%
```

- 거부율은 0 ~ 1 사이 소수로 계산하고, 보여 줄 때만 100 을 곱해 퍼센트로 바꿉니다.
- 경고 기준과 비교할 때는 퍼센트가 아니라 소수(`rate >= limit`)를 그대로 비교합니다.

**③ `counts.get(값, 0)` 으로 값별 횟수를 셉니다**

```python
names = ["dami", "gaeun", "dami"]                               # 거부된 사용자 이름 리스트
counts = {}                                                      # 값별 횟수를 담을 딕셔너리

for name in names:                                               # 이름을 하나씩 꺼낸다
    old_count = counts.get(name, 0)                              # 지금까지 센 횟수를 꺼낸다(처음이면 0)
    counts[name] = old_count + 1                                 # 횟수를 1 늘려 넣는다

print(counts)                                                    # 이름별 횟수를 출력한다
junho_count = counts.get("junho", 0)                             # 없는 이름은 0 을 준다
print(junho_count)                                               # 없는 이름의 횟수를 출력한다
```

실행 결과:

```
{'dami': 2, 'gaeun': 1}
0
```

- `counts.get(name, 0)` 은 `name` 키의 값을 꺼내고, 키가 아직 없으면 0 을 줍니다. 처음 나온 이름도 같은 두 줄로 셀 수 있습니다.
- `count_by` 는 이 두 줄을 `entry[key]` 로 꺼낸 값에 그대로 씁니다.
- 반복할 때마다 `counts` 가 어떻게 바뀌는지 그려 보고 싶으면 AI 에게 「이 코드에서 for 가 한 번 돌 때마다 counts 가 어떻게 바뀌는지 표로 보여 줘」라고 코드와 함께 물어보세요.

**④ `"\n".join(리스트)` 는 리스트의 문자열을 줄바꿈으로 이어 붙입니다**

```python
lines = ["# 제목", "- 첫째 줄", "- 둘째 줄"]                          # 보고서 줄을 모은 리스트
text = "\n".join(lines)                                          # 줄바꿈 문자로 이어 붙여 문자열 하나로 만든다
print(text)                                                      # 이어 붙인 문자열을 출력한다
```

실행 결과:

```
# 제목
- 첫째 줄
- 둘째 줄
```

- `"\n"` 은 줄바꿈 문자 하나이고, 출력하면 다음 줄로 넘어갑니다.
- 제공 파일 `weekly_report.py` 는 마지막에 `"\n".join(lines) + "\n"` 을 리턴합니다. 뒤의 `+ "\n"` 은 파일 맨 끝도 줄바꿈으로 끝나게 하려고 붙입니다.

## 응용 5-1 · 거부율과 경고 여부 구하기

**이런 상황이 있습니다**

- **지금은**: 로그 40줄을 사람이 하나씩 읽고 세야 합니다. 거부가 늘었는지, 누가 반복해서 거부됐는지 확인하려면 시간이 오래 걸립니다.
- **그래서 만드는 것**: `log_summary.py` 입니다.
  - 로그를 읽고, 거부된 요청을 모으고, 사유별 · 사용자별로 세고, 거부율을 구합니다.
  - 거부율이 경고 기준 이상이면 경고로 표시합니다.
  - 「제공 파일」 레슨에서 완성본으로 받은 `log_summary.py` 를 이번에는 빈칸이 있는 골격으로 바꿔 직접 씁니다.
  - 다 쓰면 제공 파일 `weekly_run.py` 를 다시 실행해, 내가 쓴 함수로도 같은 주간 보고서가 나오는지 확인합니다.
- **실행하면**: 단계 1은 허용 · 거부 · 거부율, 단계 2는 거부 사유별 횟수, 단계 3은 경고 여부와 거부가 많은 사용자를 출력합니다.
- **현업에서는**: 로그를 집계하는 일은 관제(시스템과 로그를 지켜보며 이상한 일을 찾는 일)의 기본입니다. 경고 기준은 코드에 직접 적지 않고 `config/alert.json` 같은 설정 파일에 두어, 쓰다가 필요할 때 바꿉니다.

**할 일** — 작업 폴더는 `network-study-notes/access_control` 이고, 고치는 `log_summary.py` 와 새로 만드는 `apply5-1_run.py` 모두 `access_control` 폴더 바로 아래에 있습니다.

1. `log_summary.py` 의 내용을 아래 골격으로 바꾸고 `apply5-1_run.py` 를 만든 뒤, `read_log` · `count_by` · `filter_denied` · `deny_rate` · `find_heavy_users` 에서 직접 쓰는 곳 다섯 군데를 씁니다.
2. 실행해서 <mark>허용 · 거부 · 거부율</mark>(단계 1: 집계), <mark>거부 사유별 횟수</mark>(단계 2), <mark>경고 여부</mark>(단계 3: 경고 기준)를 읽습니다.
3. 제공 파일 `weekly_run.py` 를 다시 실행해 <mark>주간 보고서</mark>가 「제공 파일」 레슨의 실행 결과와 같은지 확인합니다.

**`log_summary.py`** — 제공 파일로 만든 내용을 모두 지우고 아래 골격을 붙여 넣습니다. 완성본이 다시 필요하면 「제공 파일」 레슨에서 복사하면 됩니다.

```python
import json                                                      # JSON 문자열을 딕셔너리로 바꾸는 모듈을 불러온다


def read_log(path):                                              # 로그 파일 경로를 받는 함수
    """서버 로그 파일을 한 줄씩 읽어 요청 딕셔너리 리스트로 만든다.
    주간 로그를 집계하기 전에 파일을 읽을 때 쓴다.
    """
    entries = []                                                 # 요청 딕셔너리를 모을 리스트
    with open(path, encoding="utf-8") as log_file:                      # 파일을 연다
        for line in log_file:                                           # 파일에서 한 줄씩 꺼낸다
            # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
            # 1. line 의 JSON 문자열을 json.loads 로 딕셔너리 entry 로 바꾼다
            # 2. entry 를 entries 에 추가한다
    return entries                                               # 요청 리스트를 리턴한다


def count_by(entries, key):                                      # 요청 리스트와 센 기준(키 이름)을 받는 함수
    """요청을 key 의 값별로 세어 {값: 횟수} 딕셔너리를 리턴한다.
    사용자별 · 이유별로 몇 번인지 알고 싶을 때 쓴다.
    예: count_by(entries, "user")
    """
    counts = {}                                                  # 값별 횟수를 담을 딕셔너리
    for entry in entries:                                        # 요청을 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. entry[key] 를 value 에 담는다
        # 4. counts 에서 value 의 지금 횟수를 old_count 에 담는다 (없으면 0: counts.get(value, 0))
        # 5. counts[value] 에 old_count + 1 을 넣는다
    return counts                                                # 값별 횟수를 리턴한다


def filter_denied(entries):                                      # 요청 리스트를 받는 함수
    """거부된 요청만 모아 리스트로 리턴한다.
    거부 사유와 사용자를 따로 볼 때 쓴다.
    """
    denied = []                                                  # 거부된 요청을 모을 리스트
    for entry in entries:                                        # 요청을 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 6. entry["allowed"] 가 거짓이면 (if not …)
        # 7.   entry 를 denied 에 추가한다
    return denied                                                # 거부된 요청 리스트를 리턴한다


def deny_rate(entries):                                          # 요청 리스트를 받는 함수
    """전체 요청 중 거부된 요청의 비율(0 ~ 1)을 리턴한다.
    주간 보고서에서 거부율을 구할 때 쓰며, 요청이 없으면 0.0 이다.
    """
    total = len(entries)                                         # 전체 요청 수
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 8. total 이 0 이면 (==)
    # 9.   0.0 을 리턴한다 (0 으로 나눌 수 없으므로)
    denied_entries = filter_denied(entries)                      # 거부된 요청 리스트
    denied = len(denied_entries)                                 # 거부된 요청 수
    return denied / total                                        # 거부 수를 전체 수로 나눈 비율을 리턴한다


def find_heavy_users(denied_counts, limit):                      # 사용자별 거부 횟수 딕셔너리와 기준 횟수를 받는 함수
    """거부 횟수가 limit 이상인 사용자 이름 리스트를 리턴한다.
    거부가 한 사람에게 몰렸는지 확인할 때 쓴다.
    """
    heavy = []                                                   # 기준에 걸린 사용자 이름을 모을 리스트
    for user, count in denied_counts.items():                    # 사용자 이름과 거부 횟수를 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 10. count 가 limit 이상이면 (>=)
        # 11.   user 를 heavy 에 추가한다
    return heavy                                                 # 기준에 걸린 사용자 이름을 리턴한다
```

들여쓰기는 미리 채운 줄에 맞춥니다.

| 번호 | 들어가는 곳 | 앞 공백 |
|---|---|---|
| 1 · 2번 | `read_log` 의 `for line in log_file:` 안쪽 | 12개 |
| 3 ~ 5번 · 6번 · 10번 | `count_by` · `filter_denied` · `find_heavy_users` 의 `for` 안쪽 | 8개 |
| 7번 · 11번 | 그 `for` 안 `if` 의 안쪽 | 12개(4개 더) |
| 8번 | `deny_rate` 함수 안 | 4개 |
| 9번 | 8번 `if` 안쪽의 `return` | 8개 |

- 4번의 `counts.get(value, 0)` 은 문법 상자 ③의 `get` 과 같습니다. 처음 나온 값은 0 에서 시작합니다.
- 8 · 9번은 요청이 하나도 없을 때 0 으로 나누는 오류를 막는 줄입니다. 로그가 비는 경우의 결과는 정답 레슨 「응용 5-1 정답」의 「자주 틀리는 곳」에서 읽습니다.
- 채우기 전에 실행하면 `IndentationError: expected an indented block` 오류가 납니다.
  - 다만 `deny_rate` 의 8 · 9번만 비워 두면 오류가 나지 않습니다. 그 아래에 미리 채운 줄이 있어 들여쓰기 오류가 없고, 이번 로그는 비어 있지 않아 0 으로 나누지도 않기 때문입니다. 로그가 빈 날에만 문제가 드러납니다.

**`apply5-1_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 샘플 로그를 집계해 세 단계로 출력합니다.

```python
import json                                                      # 경고 기준 파일을 읽는 데 쓴다
from log_summary import read_log, count_by, filter_denied, deny_rate, find_heavy_users   # 방금 만든 집계 함수를 불러온다

LOG_PATH = "week_log.jsonl"                                      # 집계할 로그 파일 이름
with open("config/alert.json", encoding="utf-8") as alert_file:           # 경고 기준 파일을 연다
    ALERT = json.load(alert_file)                                         # 경고 기준 딕셔너리로 읽는다

entries = read_log(LOG_PATH)                                     # 로그를 읽어 요청 리스트로 만든다
denied = filter_denied(entries)                                  # 거부된 요청만 모은다
rate = deny_rate(entries)                                        # 거부율(0 ~ 1)을 구한다
percent = round(rate * 100)                                      # 거부율을 퍼센트 숫자로 바꾼다
limit = ALERT["deny_rate_limit"]                                 # 거부율 경고 기준(0 ~ 1)
limit_percent = round(limit * 100)                               # 경고 기준을 퍼센트 숫자로 바꾼다
user_limit = ALERT["user_denied_limit"]                          # 사용자별 거부 횟수 기준

entry_count = len(entries)                                       # 요청이 모두 몇 건인지 센다
print("--- 단계 1: 집계 - 요청", entry_count, "건")              # 단계 1 시작을 알리는 줄
denied_count = len(denied)                                       # 거부된 요청이 몇 건인지 센다
allowed_count = entry_count - denied_count                       # 허용된 요청 수
print("허용", allowed_count, "· 거부", denied_count, "· 거부율", f"{percent}%")  # 허용 · 거부 · 거부율을 출력한다
print("--- 단계 2: 거부 사유별")                                    # 단계 2 시작을 알리는 줄
reason_counts = count_by(denied, "reason")                       # 거부된 요청을 사유별로 센다
for reason, count in reason_counts.items():                      # 사유와 횟수를 하나씩 꺼낸다
    print(reason, count)                                         # 거부 사유와 횟수를 출력한다
print("--- 단계 3: 경고 기준")                                      # 단계 3 시작을 알리는 줄
if rate >= limit:                                                # 거부율이 기준 이상이면
    print(f"거부율 {percent}% >= 기준 {limit_percent}% -> 경고")    # 경고라고 출력한다
else:                                                            # 기준보다 낮으면
    print(f"거부율 {percent}% < 기준 {limit_percent}% -> 경고 없음")   # 경고 없음이라고 출력한다
user_counts = count_by(denied, "user")                           # 거부된 요청을 사용자별로 센다
heavy = find_heavy_users(user_counts, user_limit)                # 기준 이상 거부된 사용자를 찾는다
print("거부", user_limit, "번 이상 사용자:", heavy)                  # 사용자 이름을 출력한다
```

**순서**

1. **[VS Code]** `access_control` 폴더의 `log_summary.py` 를 열어 내용을 모두 지우고(`Ctrl + A` 뒤 `Delete`, 맥북은 `Cmd + A`) 위 `log_summary.py` 골격을 붙여 넣고 저장합니다. 이어서 `access_control` 폴더를 오른쪽 클릭 › **New File** 로 `apply5-1_run.py` 를 만들어 `apply5-1_run.py` 코드 상자의 내용을 붙여 넣고 저장합니다.

<!-- checklist optional -->
- [ ] `access_control` 폴더 바로 아래에 `apply5-1_run.py` 를 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
<!-- /checklist -->

2. **[VS Code]** `log_summary.py` 에서 직접 쓰는 곳 다섯 군데를 씁니다. 2.1 의 표와 그림, 문법 상자를 보고 씁니다.

<!-- checklist optional -->
- [ ] `log_summary.py` 의 내용을 골격으로 바꾸고 1 ~ 11번을 채워 저장했다
<!-- /checklist -->

3. **[터미널]** `pwd` 의 결과가 `access_control` 로 끝나는지 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python apply5-1_run.py
   ```
4. 출력은 세 단계입니다. 단계 1은 한 줄, 단계 2는 거부 사유 네 줄, 단계 3은 두 줄입니다.

<!-- checklist optional -->
- [ ] `python apply5-1_run.py` 를 실행해 세 단계 출력이 나왔다
<!-- /checklist -->

5. **[터미널]** 제공 파일 `weekly_run.py` 를 다시 실행합니다. 이번에는 내가 쓴 `log_summary.py` 의 함수로 보고서가 만들어집니다.
   ```bash
   python weekly_run.py
   ```
   - 단계 3의 보고서가 「제공 파일」 레슨의 실행 결과와 같으면 됩니다. 같은 이름의 보고서 파일은 `"w"` 로 열어 새로 쓰므로 덮어써집니다.

<!-- checklist optional -->
- [ ] `python weekly_run.py` 를 다시 실행해 보고서가 「제공 파일」 레슨의 실행 결과와 같았다
<!-- /checklist -->

6. **[터미널]** 보고서 4절에 나온 거부가 많은 사용자의 요청을 로그에서 직접 찾아 봅니다.
   ```bash
   grep gaeun week_log.jsonl
   grep dami week_log.jsonl
   ```
   - 명령 풀이: `grep 단어 파일` 파일에서 그 단어가 들어간 줄만 보여 줌
7. **[보고서]** `access_control` 폴더의 `report_u5.md` 에서 `## 응용 5-1` 아래를 채웁니다.
   - (가) `apply5-1_run.py` 의 출력을 붙여 넣고, 허용 · 거부 · 거부율, 경고 여부, 거부 사유 중 가장 많은 것을 적어 주세요. `weekly_run.py` 를 다시 실행한 보고서가 제공 파일 때와 같았는지도 적어 주세요.
   - (나) [핵심 질문] 보고서 4절에 거부가 4번 이상인 사용자로 gaeun 과 dami 가 나왔습니다. 순서 6번에서 찾은 두 사람의 요청을 비교해 주세요. 그리고 두 사람에게 같은 조치를 하면 안 되는 이유와, 각각 무엇부터 확인해야 하는지 적어 주세요.
   - (다) [핵심 질문] 서버가 멈춰서 로그가 빈 주에는 `deny_rate` 가 0.0 을 리턴해 보고서에 「거부율 0%」가 나옵니다. 이 보고서만 보고 「이번 주는 안전했다」고 판단해도 되는지 적어 주세요. 그리고 보고서에서 함께 확인해야 하는 정보와 그 이유도 적어 주세요.

<!-- checklist optional -->
- [ ] `report_u5.md` 의 `## 응용 5-1` (가) ~ (다)에 답을 썼다
<!-- /checklist -->

## 응용 5-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 로그 한 줄을 딕셔너리로 | `entry = json.loads(line)` → `entries.append(entry)` (`read_log` 안) |
| 셀 값 꺼내기 | `value = entry[key]` |
| 지금 횟수 꺼내기 | `old_count = counts.get(value, 0)` |
| 1 늘려 넣기 | `counts[value] = old_count + 1` |
| 거부된 요청만 모으기 | `if not entry["allowed"]:` → `denied.append(entry)` |
| 거부율 | `if total == 0:` → `return 0.0` 뒤에 `denied / total` |
| 거부가 많은 사용자 | `if count >= limit:` → `heavy.append(user)` |
| 경고 여부 | `rate >= limit` 이면 경고 (소수끼리 비교) |
| 퍼센트로 보여 주기 | `round(rate * 100)` |
| 보고서 줄 모으기 | `lines.append("…")` → `"\n".join(lines)` |
| 파일 열기 | `open(file_name, "w", encoding="utf-8")` |
| 파일에 쓰기 | `report_file.write(text)` |

보고서 줄 모으기와 파일 열기 · 쓰기는 제공 파일 `weekly_report.py` 의 코드입니다.

---
