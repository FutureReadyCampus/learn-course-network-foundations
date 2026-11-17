---
id: m3-u09-l03
title: Exercise 9-2 · 판정 서버 만들고 요청 로그 남기기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/092_day05_pm_conditions.md
  mission_id: GichanSource.m3-1030-pm-conditions
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 9-2 · 판정 서버 만들고 요청 로그 남기기

## 개요

> **이번 Exercise에 들어온 일**
>
> A사 관제 담당이 보낸 메시지:
> 「지금은 판정 함수를 파이썬 파일 안에서만 쓸 수 있습니다. 사내의 다른 프로그램이 「이 사용자가 지금 이 권한을 쓸 수 있나」를 물으려면 주소로 물을 수 있어야 합니다.
>
> 판정을 주소로 요청해 받을 수 있는 서버로 만들어 주세요. 허용이면 200, 거부면 403, 요청에 빠진 값이 있으면 400으로 답하고(처리 결과를 알리는 숫자를 상태 코드라고 합니다), 요청마다 로그를 한 줄씩 남겨 주세요.」
> - **왜 중요한가**: 판정을 한곳에 두고 여러 프로그램이 같은 주소로 물으면 규칙이 한 군데에만 있어서 서로 어긋나지 않습니다. 로그가 있으면 누가 언제 무엇을 요청했는지 나중에 볼 수 있습니다.

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「문제」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 읽기 · 왜 필요한가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 판정 함수를 `import` 해서 쓰면 그 파일을 가진 프로그램만 쓸 수 있습니다. **서버**로 만들면 주소만 알면 어떤 프로그램이든 같은 규칙으로 물을 수 있습니다.
2. 서버는 켜 두고 요청을 기다리는 프로그램입니다.
   - 서버를 켠 터미널(터미널 1)은 계속 실행 중이라 다른 일을 못 하므로, 요청은 다른 터미널(터미널 2)에서 보냅니다.
   - VS Code 터미널 창 오른쪽의 터미널 리스트에서 이름을 누르면 그 터미널 화면으로 바뀝니다.
3. 1과목에서는 노트북 셀 안에서 서버를 만들었습니다. 이번에는 **파일**(`access_server.py`)로 만들어 터미널에서 켭니다.

## 읽기 · 2.1 서버와 요청의 구조

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

```
+---------------------------------------------------------+
| 요청을 보내는 쪽 (터미널 2에서 실행하는 send_checks.py) |
+---------------------------------------------------------+
   |
   |  요청: /check?user=…&resource=…&action=…&network=…&time=…
   v
+--------------------------------------------+
| 서버 쪽 (터미널 1에서 켠 access_server.py) |
+--------------------------------------------+
   |
   |  응답: 상태 코드(200 · 403 · 400)와 {"allowed": …, "reason": …}
   v
요청을 보내는 쪽이 응답을 받는다
```

**주소**(URL · 유알엘)는 서버의 위치를 적은 문자열입니다. 서버 주소(`http://127.0.0.1:5001`) 뒤에 서버 안의 위치인 경로 `/check` 를 붙이고, `?` 뒤에 값 다섯 개를 `이름=값` 으로 이어 붙인 전체를 **요청 주소**라고 부릅니다.

| 주소의 이름 | 뜻 | 값의 예 |
|---|---|---|
| `user` | 사용자 | `seoyeon` |
| `resource` · `action` | 자원 · 행위 | `SALES` · `CHANGE` |
| `network` | 접속 위치 | `office` |
| `time` | 요청 시각. 실습에서는 같은 결과가 나오도록 직접 넣습니다. Exercise 9-1 실행 파일의 `2026-10-30 10:00` 과 달리 주소에서는 공백 대신 `T` 를 씁니다 | `2026-10-30T10:00` |

응답의 **상태 코드**는 요청이 어떻게 처리됐는지를 숫자로 알려 줍니다. 앞자리 `2` 는 성공, `4` 는 **요청을 보낸 쪽에서 고치거나 받아들여야 하는 경우**입니다(1과목에서 배웠습니다).

| 상태 코드 | 뜻 | 이 서버에서 |
|---|---|---|
| 200 | 성공 | 판정이 **허용** |
| 403 | **누구인지는 알겠는데 안 된다.** 요청은 올바르게 도착했지만 **인가**(이 일을 해도 되나)에서 막힘 | 판정이 **거부**(퇴사한 계정 · 권한 없음 · 업무 시간 밖 · 허용되지 않은 접속 위치) |
| 400 | 보낸 쪽 잘못: 요청이 잘못됨 | 요청에 값이 빠졌거나 시각 형식이 틀림(둘 다 「입력이 잘못됨」으로 답함) |

- 403 은 1과목의 `401` 과 다릅니다.
  - `401` 은 「당신이 누구인지 모르겠다」(인증에서 막힘)입니다.
  - 이 서버는 비밀번호나 토큰으로 사용자를 확인하는 단계(인증)가 없고 요청에 적힌 사용자 이름을 그대로 믿으므로 `401` 은 쓰지 않습니다.
- **직접 쓰는 곳은 세 함수**입니다. 판단이 필요한 함수마다 1 ~ 4줄만 쓰고, 나머지는 미리 채웠습니다.
  - `parse_time`(1 · 2번): 시각 문자열을 시각으로 바꾸고, 모양이 틀리면 `None` 을 리턴합니다.
  - `write_log`(3번): 로그 파일을 여는 모드를 정합니다(덧붙이기 `"a"`).
  - `check`(4 ~ 7번): Exercise 9-1의 `evaluate_conditional` 로 판정하고 200 · 403 으로 답합니다.
- **미리 채운 것**
  - `parse_time` 의 `if text is None:` 과 `try` · `except` 틀, `write_log` 의 파일 열기와 쓰기 줄
  - `check` 안의 주소에서 값 다섯 개를 꺼내는 다섯 줄, 값이 빠졌을 때 400 으로 답하는 두 줄, 요청 로그를 남기는 `log_entry` 와 `write_log` 줄
  - 서버를 켜는 맨 아래 두 줄
- **로그**(log)는 요청마다 한 줄씩 남기는 기록 파일(`server_log.jsonl`)입니다.
  - `.jsonl` 은 한 줄에 JSON 한 건씩 적은 파일입니다(JSON Lines · 제이슨 라인즈).
  - 400 으로 답한 요청은 판정을 하지 않아 로그에 남기지 않으므로, 로그 줄 수가 보낸 요청 수보다 적을 수 있습니다.
- `write_log` 는 로그 파일을 `"a"`(덧붙이기) 모드로 엽니다.
  - `"a"` 는 기존 내용 뒤에 쓰고, `"w"`(쓰기)는 열 때마다 내용을 지웁니다. 로그는 쌓아 두어야 해서 `"a"` 를 씁니다.
  - 남기는 `time` 은 시각으로 바꾼 `now` 가 아니라 주소에 적혀 온 글자 그대로입니다.
- **포트**(port)는 서버가 요청을 기다리는 번호입니다.
  - 서버는 `5001` 번 포트로 켜고, 주소는 `http://127.0.0.1:5001` 입니다(`127.0.0.1` 은 내 PC 자신입니다).
- 이 실습에서는 `network` 와 `time` 을 요청하는 쪽이 주소에 적어 보냅니다.
  - 요청하는 쪽이 적은 값은 거짓으로 적을 수 있습니다. 실제 서비스에서는 서버가 접속 위치와 시각을 직접 알아내야 합니다.
- **요청을 보내는 쪽** `send_checks.py` 가 하는 일
  - 요청 아홉 건을 `requests.get(주소, params=딕셔너리)` 로 서버에 보냅니다(1과목과 같은 방식). 딕셔너리의 키와 값이 주소의 `?user=…&resource=…` 가 됩니다.
  - 응답에서 `response.status_code`(상태 코드)와 `response.json()`(내용)을 꺼냅니다.
  - 서버가 남긴 로그 파일을 한 줄씩 읽어 `json.loads(line)` 으로 딕셔너리로 바꿉니다(로그는 한 줄에 JSON 한 건).
  - 9번 요청은 일부러 `network` 를 빠뜨려 400 이 나오고 로그에는 남지 않습니다.
  - 시작할 때 이전 로그 파일을 지웁니다(이번 요청 로그만 보려는 시험용이고, 실제 서비스에서는 로그를 보관합니다).

**문법 상자 — 주소에서 값 꺼내기**

**`request.args.get("이름")` 은 주소의 `?이름=값` 에서 값을 꺼냅니다**

| 주소 | 코드 | 값 |
|---|---|---|
| `/check?user=seoyeon&network=office` | `request.args.get("user")` | `"seoyeon"` |
| `/check?user=seoyeon&network=office` | `request.args.get("network")` | `"office"` |
| `/check?user=seoyeon&network=office` | `request.args.get("time")` | `None` (주소에 없음) |

- 주소에 없는 이름은 오류가 아니라 `None` 이 나옵니다. 딕셔너리의 `.get` 과 같습니다.

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise 9-2 · 판정 서버를 만들고 요청마다 로그 남기기

**이런 상황이 있습니다**

- **지금은**: 판정 함수는 파이썬 파일 안에서만 부를 수 있습니다. 다른 프로그램은 쓸 수 없고, 누가 언제 물었는지 로그도 없습니다.
- **그래서 만드는 것**: `access_server.py` 의 `check` 함수입니다.
  - 주소에서 꺼낸 다섯 값에 빠진 것이 있으면 400, 없으면 Exercise 9-1의 `evaluate_conditional` 로 판정하고, 요청 로그를 한 줄 남기고, 허용이면 200 · 거부면 403 으로 답합니다.
- **실행하면**: 서버가 켜지고 터미널 1이 요청을 기다립니다. 터미널 2에서 `send_checks.py` 를 실행하면 요청 아홉 건을 보내고, 응답과 서버가 남긴 로그를 세 단계로 출력합니다.
- **현업에서는**: 접근 제어 서비스도 판정을 주소로 받을 수 있게 하고, 요청마다 로그를 남깁니다.

**할 일**

1. `access_server.py` 와 `send_checks.py` 두 파일을 만들고, `parse_time` · `write_log` · `check` 에서 직접 쓰는 곳 네 군데를 씁니다. Exercise 9-1의 `conditional.py` 와 `config/conditions.json` 이 필요합니다.
2. 터미널 1에서 서버를 켜고, 터미널 2에서 `send_checks.py` 를 실행해 <mark>응답</mark>(단계 1: 응답), <mark>서버 로그</mark>(단계 2: 로그), <mark>대조 결과</mark>(단계 3: 대조)를 읽습니다.

**`access_server.py`**

```python
import json                                                      # JSON 문자열을 만드는 모듈을 불러온다
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from flask import Flask, request                                 # 서버를 만드는 Flask 와 요청 정보를 담은 request 를 불러온다
from conditional import load_rules, evaluate_conditional         # Exercise 9-1에서 만든 조건 판정 함수를 불러온다

app = Flask(__name__)                                            # 서버 프로그램을 만든다
app.json.ensure_ascii = False                                    # 응답의 한글이 \uXXXX 로 깨지지 않게 한다
RULES = load_rules("config/conditions.json")                     # 조건 파일을 서버를 켤 때 한 번 읽는다
LOG_PATH = "server_log.jsonl"                                    # 요청 로그를 남길 파일 이름
TIME_FORMAT = "%Y-%m-%dT%H:%M"                                   # 주소로 받는 시각 문자열의 형식(예: 2026-10-30T10:00)


def parse_time(text):                                            # 시각 문자열을 받는 함수
    """2026-10-30T10:00 모양 문자열을 시각으로 바꾼다.
    없거나 모양이 틀리면 None 을 리턴한다.
    판정 서버가 요청 시각을 읽을 때 쓴다.
    """
    if text is None:                                             # 시각 문자열이 아예 없으면
        return None                                              # 없다고 알린다
    try:                                                         # 아래를 시도한다 (미리 채움)
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 1. datetime.strptime(text, TIME_FORMAT) 의 결과(시각)를 리턴한다
    except ValueError:                                           # 모양이 틀렸으면 (미리 채움)
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 2. None 을 리턴한다 (없다고 알린다)


def write_log(entry):                                            # 로그에 쓸 딕셔너리를 받는 함수
    """딕셔너리 한 개를 JSON 한 줄로 만들어 로그 파일 끝에 덧붙인다.
    판정 서버가 요청마다 기록을 남길 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 3. 파일을 여는 모드 "a"(덧붙이기: 기존 내용 뒤에 쓴다)를 mode 에 담는다
    with open(LOG_PATH, mode, encoding="utf-8") as log_file:            # 파일을 mode(덧붙이기 모드)로 연다
        text = json.dumps(entry, ensure_ascii=False)             # 딕셔너리를 JSON 문자열로 만든다(한글은 그대로)
        log_file.write(text + "\n")                                     # 한 줄로 파일 끝에 쓴다


@app.route("/check")                                             # 주소 /check 로 오는 요청을 아래 함수가 받는다
def check():                                                     # 요청 한 건을 처리하는 함수
    """주소의 값으로 판정해 허용이면 200, 거부이면 403, 값이 빠졌으면 400 으로 답한다.
    판정 서버가 요청을 받을 때마다 쓴다.
    """
    user = request.args.get("user")                              # 요청 주소에서 user 값을 꺼낸다(주소에 없으면 None)
    resource = request.args.get("resource")                      # 요청 주소에서 resource 값을 꺼낸다
    action = request.args.get("action")                          # 요청 주소에서 action 값을 꺼낸다
    network = request.args.get("network")                        # 요청 주소에서 network 값을 꺼낸다
    time_text = request.args.get("time")                         # 요청 주소에서 time 값을 꺼낸다(없으면 None)
    now = parse_time(time_text)                                  # 시각으로 바꾼다(없거나 모양이 틀리면 None)
    if None in (user, resource, action, network, now):           # 빠졌거나 모양이 틀린 값이 하나라도 있으면 (미리 채움)
        return {"allowed": False, "reason": "입력이 잘못됨"}, 400   # 요청이 잘못됐다는 상태 코드 400 으로 답한다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. evaluate_conditional(user, resource, action, network, now, RULES) 의 결과를 allowed, reason 으로 받는다
    log_entry = {                                                 # 로그 한 줄에 담을 값을 묶는다(여러 줄)
        "time": request.args.get("time"),                        # 시각
        "user": user,                                            # 사용자
        "permission": f"{resource}:{action}",                    # 권한
        "network": network,                                      # 접속 위치
        "allowed": allowed,                                      # 허용 여부
        "reason": reason,                                        # 이유
    }
    write_log(log_entry)                                         # 요청 로그를 한 줄 덧붙인다 (미리 채움)
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. allowed 가 참이면
    # 6.   {"allowed": True, "reason": reason} 과 상태 코드 200 을 함께 리턴한다
    # 7. {"allowed": False, "reason": reason} 과 상태 코드 403 을 함께 리턴한다 (if 밖, 함수 안쪽 줄에 맞춘다)

if __name__ == "__main__":                                       # 이 파일을 직접 실행했을 때만
    app.run(port=5001)                                           # 5001번 포트로 서버를 켠다
```

- 들여쓰기는 미리 채운 줄에 맞춥니다.
  - `parse_time`: 미리 채운 `try` · `except` 안쪽이라 8개입니다(1 · 2번).
  - `write_log`: 함수 안이라 4개입니다(3번).
  - `check`: 함수 안이라 4개이고, 5번 `if allowed:` 도 4개입니다. `if` 안쪽 `return`(6번)은 4개 더(8개)이고, 7번 `return` 은 `if` 밖이라 4개입니다.
  - 400 으로 답하는 `if None in …` 과 `log_entry` · `write_log` 줄은 미리 채워 두었으니 그대로 둡니다.
- 6번 · 7번의 `return` 은 `return 딕셔너리, 상태코드` 로 두 값을 함께 리턴합니다.
  - 상태 코드가 응답의 숫자가 됩니다.
  - 1과목에서 `return {…}, 200` 으로 쓴 방식과 같습니다.
- 미리 채운 `None in (…)` 는 괄호 안 값 중 `None` 이 하나라도 있으면 참입니다.
  - 예: `None in ("seoyeon", None)` 는 `True`, `None in ("seoyeon", "office")` 는 `False` 입니다.
- 채우기 전에 서버를 켜면 `IndentationError: expected an indented block` 오류가 납니다.
  - `parse_time` 의 `try` 아래에 실행할 줄이 아직 없기 때문입니다.

**`send_checks.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 서버에 요청 아홉 건을 보내 응답을 출력하고, 서버가 남긴 로그를 읽어 출력하고, 둘을 대조합니다.

```python
import json                                                      # JSON 문자열을 읽는 모듈을 불러온다
import os                                                        # 파일이 있는지 보고 지우는 데 쓴다
import requests                                                  # 서버에 요청을 보내는 모듈을 불러온다

BASE_URL = "http://127.0.0.1:5001"                               # 서버 주소
LOG_PATH = "server_log.jsonl"                                    # 서버가 남기는 로그 파일 이름
CASES = [                                                        # 서버에 보낼 요청 아홉 건. 주소의 ?user=… 로 들어가는 값이다
    {"user": "seoyeon", "resource": "SALES", "action": "CHANGE", "network": "office", "time": "2026-10-30T09:00"},     # 1. 시작 시각 정각, 사내망
    {"user": "seoyeon", "resource": "SALES", "action": "CHANGE", "network": "office", "time": "2026-10-30T18:00"},     # 2. 끝 시각 정각
    {"user": "seoyeon", "resource": "SALES", "action": "CHANGE", "network": "external", "time": "2026-10-30T10:00"},   # 3. 외부 접속
    {"user": "seoyeon", "resource": "SALES", "action": "QUERY", "network": "external", "time": "2026-10-30T23:00"},    # 4. 조건이 없는 조회
    {"user": "junho", "resource": "SETTLE", "action": "QUERY", "network": "vpn", "time": "2026-10-30T19:30"},          # 5. 정산 조회는 20시까지
    {"user": "junho", "resource": "SETTLE", "action": "QUERY", "network": "external", "time": "2026-10-30T10:00"},     # 6. 외부 접속
    {"user": "gaeun", "resource": "ACCOUNT", "action": "CHANGE", "network": "vpn", "time": "2026-10-30T10:00"},        # 7. 계정 변경은 사내망만
    {"user": "dami", "resource": "SALES", "action": "QUERY", "network": "office", "time": "2026-10-30T10:00"},         # 8. 퇴사한 사용자
    {"user": "seoyeon", "resource": "SALES", "action": "CHANGE", "time": "2026-10-30T10:00"},                          # 9. 접속 위치(network)를 빠뜨린 요청
]

if os.path.exists(LOG_PATH):                                     # 이전에 남은 로그 파일이 있으면
    os.remove(LOG_PATH)                                          # 지운다(이번 요청 로그만 보려고. 실제 서비스에서는 로그를 지우지 않고 보관한다)

print("--- 단계 1: 응답 - 요청", len(CASES), "건")               # 단계 1 시작을 알리는 줄
results = []                                                     # 서버의 응답을 담을 빈 리스트
case_count = len(CASES)                                          # 개수를 먼저 구한다
for index in range(case_count):                                  # 번호 index 로 요청을 하나씩 꺼낸다
    case = CASES[index]                                          # index 번째 요청
    response = requests.get(BASE_URL + "/check", params=case)    # 서버의 /check 에 요청을 보낸다(params 의 값이 주소의 ?user=… 가 된다)
    body = response.json()                                       # 응답의 JSON 문자열을 딕셔너리로 바꾼다
    result = {                                                    # 응답 한 개의 값을 묶는다(여러 줄)
        "status": response.status_code,                          # 응답 상태 코드
        "allowed": body["allowed"],                              # 허용 여부
        "reason": body["reason"],                                # 이유
    }
    results.append(result)                                       # 상태 코드 · 허용 여부 · 이유를 응답 리스트에 추가한다
    permission = case["resource"] + ":" + case["action"]         # 자원과 행위를 : 로 이어 붙여 권한 문자열을 만든다
    print(index + 1, case["user"], permission, "->", response.status_code, body["reason"])  # 번호 · 사용자 · 권한 -> 상태 코드 · 이유를 출력한다

entries = []                                                     # 로그에서 읽은 기록을 담을 빈 리스트
with open(LOG_PATH, encoding="utf-8") as log_file:                      # 로그 파일을 읽기 모드로 연다
    for line in log_file:                                               # 파일에서 한 줄씩 꺼낸다
        entry = json.loads(line)                                 # JSON 한 줄을 딕셔너리로 바꾼다
        entries.append(entry)                                    # 그 줄의 JSON 문자열을 딕셔너리로 바꿔 추가한다
print("--- 단계 2: 로그 - 서버가 남긴", len(entries), "줄")      # 단계 2 시작을 알리는 줄
for entry in entries:                                            # 로그의 기록을 하나씩 꺼낸다
    print(entry["user"], entry["permission"], entry["network"], entry["time"], "->", entry["allowed"], entry["reason"])  # 사용자 · 권한 · 접속 위치 · 시각 -> 결과를 출력한다

answered = 0                                                     # 판정까지 간 응답 수를 0 으로 시작한다
for result in results:                                           # 응답을 하나씩 꺼낸다
    if result["status"] != 400:                                  # 입력 부족(400)이 아니면 서버가 판정까지 한 것이다
        answered = answered + 1                                  # 판정까지 간 응답 수를 1 늘린다
print("--- 단계 3: 대조 - 판정까지 간 응답과 로그")              # 단계 3 시작을 알리는 줄
print("판정까지 간 응답", answered, "건 / 로그에 남은 줄", len(entries), "줄")  # 두 수가 같은지 출력한다
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `access_server.py` · `send_checks.py` 를 만들어 위 코드를 붙여 넣습니다. 만드는 법은 둘 중 하나를 고릅니다.
   - VS Code: `access_control` 폴더를 선택하고 **새 파일**(New File) 아이콘을 눌러 이름을 입력합니다.
   - 터미널: `pwd` 로 `access_control` 인지 확인하고 `touch 이름` 으로 만든 뒤 VS Code 에서 열어 붙여 넣습니다(`vim 이름` → `i` → 붙여넣기 → `Esc` → `:wq` 도 됩니다).
2. **[VS Code]** `access_server.py` 의 `parse_time` · `write_log` · `check` 에서 직접 쓰는 곳 네 군데를 씁니다. 2.1 의 표와 그림을 보고 씁니다.
3. **[터미널 1]** 서버를 켭니다(맥북은 `python3`).
   ```bash
   pwd
   python access_server.py
   ```
   - `Running on http://127.0.0.1:5001` 이 나오고 입력을 받지 않으면 정상입니다. 이 터미널은 켠 채로 두고 다른 명령을 치지 않습니다.
   - `Address already in use` 가 나오면 이미 켜진 서버가 있는 것이니, 그 터미널에서 `Ctrl + C` 로 끄고 다시 켭니다.
   - 코드나 `config/conditions.json` 을 고쳤으면 `Ctrl + C` 로 끄고 다시 켭니다(서버는 켤 때 한 번만 읽습니다).
   - 켤 때 `[경고] 설정 파일 …` 줄이 나오면 Exercise 9-1의 `config/conditions.json` 을 확인합니다.
4. **[터미널 2]** VS Code 터미널 창 오른쪽 위의 `+` 단추로 새 터미널을 엽니다(서버를 켠 터미널은 그대로 둡니다).
   ```bash
   cd access_control
   pwd
   python send_checks.py
   ```
   - 새 터미널이 이미 `access_control` 에서 열렸다면 `cd access_control` 은 건너뜁니다(맥북은 `python3`, 결과 줄 앞의 `NotOpenSSLWarning` 은 무시합니다).
   - `Connection refused` 가 나오면 터미널 1에서 서버가 켜져 있는지 확인합니다.
   - `No module named 'requests'` 가 나오면 `pip install requests`(맥북은 `pip3`)를 치고 다시 실행합니다.
5. 출력은 세 단계입니다. 단계 1은 `요청 9 건` 제목 줄과 응답 아홉 줄, 단계 2는 `서버가 남긴 8 줄` 제목 줄과 로그 여덟 줄, 단계 3은 대조 두 줄입니다.
6. **[터미널 1]** 서버를 켠 터미널(오른쪽 터미널 리스트에서 선택)에는 요청마다 `"GET /check?… HTTP/1.1" 200 -` 줄이 찍혔습니다. 끝의 숫자가 상태 코드입니다.
   - 확인한 뒤 그 터미널에서 `Ctrl + C` 로 서버를 끕니다(Windows 에서 안 꺼지면 한 번 더 누릅니다).
7. **[보고서]** Unit 9 의 `## Exercise 9-2` › `#### Exercise 9-2` 아래를 채웁니다.
   - (가) 터미널 2의 출력 전체를 붙여 넣고, 응답의 상태 코드별 건수(200 · 403 · 400)와 서버가 남긴 로그 줄 수를 적어 주세요.
   - (나) [핵심 질문] 거부는 403, 값이 빠진 요청은 400 으로 상태 코드를 다르게 답했습니다. 요청을 보내는 쪽이 이 둘을 구별해야 하는 이유와, 구별하지 않으면 생길 수 있는 일을 적어 주세요.
   - (다) [핵심 질문] 서버 로그를 요청마다 새로 쓰면(`"w"` 모드) 한 달 뒤에 지난주의 거부 기록을 찾으려 할 때 어떻게 되나요? 로그에는 끝에 덧붙이는 방식이 알맞은 이유를 적어 주세요.

## 서버가 안 켜지거나 오류가 나면

- 먼저 터미널 맨 앞에 가상환경 이름(예: `(.venv)`)이 보이는지, 서버를 켠 터미널과 요청을 보내는 터미널을 헷갈리지 않았는지 봅니다.
  - `No module named 'flask'` · `No module named 'requests'`: `python -m pip install flask requests` 를 치고(맥북은 `python3 -m pip`) 다시 실행합니다. 새로 연 터미널이면 가상환경이 켜져 있는지 봅니다.
  - `Address already in use`: 이미 켜진 서버가 5001번 포트를 쓰고 있습니다. 서버를 켠 터미널에서 `Ctrl + C` 로 끕니다.
- AI 에게 물을 때는 운영체제와 터미널(예: Windows Git Bash), 친 명령 한 줄, 오류 전체를 함께 붙여 넣습니다. `.env` 내용이나 API 키가 보이면 지우고 붙여 넣습니다.
- AI 가 알려 준 명령은 뜻을 읽고 치고, `rm` · `del` · `kill` 처럼 지우거나 끄는 명령은 뜻을 되물은 뒤에 칩니다. 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

## Exercise 9-2 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 주소에서 값 꺼내기 | `user = request.args.get("user")` (미리 채움) |
| 값이 하나라도 빠졌는지 | `if None in (user, resource, action, network, now):` (미리 채움) |
| 상태 코드와 함께 답하기 | `return {"allowed": True, "reason": reason}, 200` |
| 요청 로그 한 줄 남기기 | `write_log(log_entry)` (이 줄은 미리 채움) |
| 로그 파일 여는 모드 | `mode = "a"` (`write_log` 안. 덧붙이기) |
| 시각 문자열 바꾸기 | `try:` → `return datetime.strptime(text, TIME_FORMAT)` · `except ValueError:` → `return None` (`parse_time` 안) |
| 서버 켜기 · 끄기 | `python access_server.py` · `Ctrl + C` |
| 요청 보내기 | `python send_checks.py` (다른 터미널) |

---

## 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기

문제가 아니라 이번 Unit에서 한 일을 저장소에 올리는 마무리입니다. Exercise 9-2 마지막 10분에 합니다. 서버를 끈 뒤에는 터미널 1 이나 터미널 2 중 아무 터미널을 써도 됩니다. 어느 쪽이든 `pwd` 로 위치를 먼저 확인하고, 결과가 `access_control` 로 끝나면 아래 1번의 `cd ..` 를 칩니다.

**이런 상황이 있습니다**

- **지금은**: 팀장이 「Unit 8에서 만든 회수 코드(`revoke.py` 등)와 이번 Unit에서 만든 판정 서버를 저장소에 남겨 달라」고 합니다.
- **그래서 하는 것**: 올라갈 파일을 `git status` 로 먼저 확인하고(비밀 키 파일 `.env` 가 섞이면 안 됩니다), `git add` → `git commit` → `git push` 로 올립니다.
- **끝나면**: 깃허브 저장소의 `access_control` 폴더에서 이번 Unit에서 만든 파일이 모두 보입니다.

**순서**

1. **[터미널]** `security-agent-toolkit` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/security-agent-toolkit` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
     - 새로 연 뒤 `pwd` 를 한 번 더 쳐서 확인합니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - `.venv` 도 같은 방법으로 합니다.
   - Unit 7까지 올렸다면 Unit 8 · Unit 9에서 만든 파일이 `access_control/revoke.py` 처럼 한 줄씩 보입니다.
     - 올리지 않았다면 `access_control/` 한 줄로 보일 수 있습니다.
     - 어느 쪽이든 `Untracked files:` 아래에 보이는 줄을 센 그대로 적습니다.
   - `access_control/revocation_log.json` 은 Exercise 8-3에서, `access_control/server_log.jsonl` 은 Exercise 9-2에서 서버가 만든 기록 파일입니다.
     - 이것도 올라갑니다.
   - `Untracked files:` 는 「아직 깃이 모르는 새 파일」 목록입니다.
   - `access_control/__pycache__/` (파이썬이 실행하면서 자동으로 만드는 임시 폴더)가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - 줄 수는 그 뒤에 다시 셉니다.
3. **[보고서]** `#### 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기` 아래를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다.
   - (가) `git status` 를 쳤을 때 `Untracked files:` 아래에 줄이 몇 개 보였는지, 그중에 `.env` 나 `.venv` 가 있었는지 적어 주세요.
   - 앞 Exercise에서 못 적은 보고서 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다. 올린 뒤에 이어서 적어 다시 올려도 됩니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add access control revocation, conditional policy and check server"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다. `git pull` 을 입력해 받아 온 뒤 `git push` 를 다시 합니다
   - `git pull` 뒤에 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다
5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `access_control` 폴더를 열고, VS Code 왼쪽 목록의 `access_control` 폴더에 있는 파일들이 깃허브에도 보이는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.
   - 빠진 이름이 있으면 VS Code 왼쪽 목록의 `access_control` 폴더에 내 PC 에도 있는지 봅니다.
     - 없으면 다른 폴더에 만든 것이니 `access_control` 안으로 옮기고, `pwd` 로 위치를 확인한 뒤 2번의 `git status` 부터 다시 합니다.

## 마무리 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 올릴 파일 확인 | `git status` (`.env` · `.venv` 가 보이면 멈춤) |
| 올리기 | `git add .` → `git commit -m "…"` → `git push` |
| 올린 뒤 | 브라우저에서 파일이 모두 있는지 확인 |

---

## Unit 9 마무리

| 확인 | 문제 |
|---|---|
| 기본 판정 뒤에 업무 시간과 접속 위치 조건을 확인했다 | Exercise 9-1 |
| 판정 서버를 만들고, 요청을 보내 응답과 서버 로그를 대조했다 | Exercise 9-2 |
| 이번 Unit에서 만든 파일과 보고서를 깃허브에 올렸다 | 마무리 |

다음 Unit은 Unit 10입니다. 이번 Unit에서 서버가 남긴 `server_log.jsonl` 을 읽어 **점검 체크리스트와 주간 보고서**를 만들고 3과목을 마무리합니다.

---

<!-- learn:answers -->
