---
id: m4-u02-l02
title: 실습 2-1 · 웹 서버 로그를 이벤트로 바꾸기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/098_day02_am_normalize.md
  mission_id: GichanSource.m4-1103-am-normalize
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 2-1 · 웹 서버 로그를 이벤트로 바꾸기

## 목표: 웹 서버 로그 이벤트

> **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다(웹 서버 · 판정 서버 · SaaS 서비스, 세 군데의 로그 이야기입니다):
> 「로그가 세 군데에서 쌓이는데 적는 방식이 다 다릅니다.
>
> - 시각
> - 웹 서버: `02/Nov/2026:09:12:03 +0900`
> - 판정 서버: `2026-11-02T09:40`
> - SaaS: `2026-11-02 02:14:08`
> - 성공 · 실패
> - 웹 서버: `200`
> - 판정 서버: `true`
> - SaaS: `success`
>
> 이대로는 같은 계정이 여러 곳에서 한 일을 시간 순서로 볼 수 없습니다. 먼저 웹 서버 로그 한 줄을 언제 · 누가 · 무엇을 · 결과를 같은 키에 담은 이벤트로 바꿔 주세요(키 이름은 아래 1.1 에서 설명합니다). 시각은 `2026-11-02 09:12:03` 모양으로 맞추고, 원래 줄은 그대로 남겨 주세요.」
> - **왜 중요한가**: <mark>모양이 다른 로그는 시간순으로 놓을 수도, 같은 기준으로 셀 수도 없습니다.</mark> 같은 키로 맞추면 탐지 규칙을 로그 종류마다 따로 만들지 않고 한 번만 만들면 됩니다. 원래 줄을 남겨 두면 변환이 틀렸을 때 원본과 대조할 수 있습니다.

## 왜 로그 모양을 맞춰야 하는가

1. SIEM(심)은 여러 곳의 로그를 한곳에 모아 같은 기준으로 찾습니다. <mark>모양이 다르면 같은 기준을 적용할 수 없습니다.</mark>
2. 그래서 로그를 모은 다음 **같은 키 · 같은 모양으로 맞추는 일**이 필요합니다. 이것을 **정규화(normalization, 노멀라이제이션)** 라고 합니다.
3. 이번 Unit에서는 로그 3종류를 같은 키로 맞춘 **공통 이벤트**로 바꿉니다. 키는 아래 1.1 에서 설명합니다.

## 1.1 세 로그의 모양과 공통 이벤트

세 로그는 모두 **언제 · 누가 · 어디서 · 무엇을 · 성공했나**를 적고 있지만, <mark>적는 방식이 다릅니다.</mark>

- **웹 서버 로그**(`access_sample.log`): 웹 서비스를 돌리는 웹 서버(nginx)가 페이지를 열거나 로그인할 때마다 남깁니다.
- **판정 서버 로그**(`server_log.jsonl`): Module 3에서 만든 권한 판정 서버가 「이 권한을 써도 되나?」라는 물음을 받을 때마다 남깁니다.
- **SaaS 로그**(`saas_events.csv`): 회사가 빌려 쓰는 SaaS(인터넷으로 쓰는 소프트웨어, 예: 파일 보관 서비스)에서 로그인하거나 파일을 올리고 내려받을 때마다 남깁니다.

<h2>① 실제 한 줄</h2>

세 줄이 얼마나 다르게 생겼는지만 봅니다.

| 로그 | 샘플의 실제 한 줄 |
|---|---|
| 웹 서버 | `203.0.113.50 - - [02/Nov/2026:09:12:03 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"` |
| 판정 서버 | `{"time": "2026-11-02T09:40", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}` |
| SaaS | `2026-11-02 02:14:08,jiwoo@a-corp.example,login,203.0.113.80,failure` |

<h2>② 이번 Unit에서 맞출 차이</h2>

형광펜으로 표시한 칸은 값이 없거나 메일 주소로 적힌 곳입니다. 시각과 성공 · 실패 행은 로그마다 모양이 달라서 고칩니다. <mark>마지막 열이 공통 이벤트에서의 모양입니다.</mark>

| 정보 | 웹 서버 | 판정 서버 | SaaS | 공통 이벤트에서는 |
|---|---|---|---|---|
| 시각 | `02/Nov/2026:09:12:03 +0900` | `2026-11-02T09:40` | `2026-11-02 02:14:08` | 모두 `2026-11-02 09:12:03` 모양 |
| 사용자 | <mark>없음</mark> | `seoyeon` | <mark>메일 주소</mark> `jiwoo@a-corp.example` | 이름만. 원래 없으면 `None` |
| 접속 주소 | 있음 | <mark>없음</mark> | 있음 | 원래 없으면 `None` |
| 성공 · 실패 | 상태 코드(`200` · `401` …) | `true` 또는 `false` | `success` 또는 `failure` | 모두 `성공` 또는 `실패` |

- 접속 주소(`ip`)는 <mark>사람이 아니라 **접속한 곳**의 주소입니다.</mark> 한 사무실의 여러 사람이 같은 주소로 보일 수 있고, 한 사람이 집과 회사에서 다른 주소로 접속할 수도 있습니다.
- 판정 서버 로그에는 주소 대신 접속 위치(`office` · `vpn` · `external`)만 있습니다. 이 수업의 `203.0.113.50` · `198.51.100.x` · `192.0.2.x` 는 문서에서 예시로 쓰라고 정해 둔 주소 범위라서 <mark>실제 장비를 가리키지 않습니다.</mark>

<h2>③ 공통 이벤트의 키</h2>

로그 한 줄이 답하는 질문은 세 로그가 같습니다. **언제? 어느 로그에서? 누가? 어디서? 무엇을? 성공했나?** 이 여섯 질문의 답을 같은 키에 담고, 원래 줄을 보관하는 키 하나를 더한 것이 **공통 이벤트(키 7개)** 입니다. <mark>이벤트는 「일어난 일 1개」입니다.</mark>

| 키 | 답하는 질문 | 값의 모양 |
|---|---|---|
| `time` | 언제? | `2026-11-02 09:12:03` 문자열(한국 시간) |
| `source` | 어느 로그에서? | `web` · `server` · `saas` |
| `user` | 누가? | 사용자 이름. 원래 없으면 `None` |
| `ip` | 어디서? | 주소 문자열. 원래 없으면 `None` |
| `action` | 무엇을? | `POST /login` · `SALES:CHANGE` · `file.download` |
| `result` | 성공했나? | `성공` 또는 `실패` |
| `raw` | (질문이 아니라 보관용) | 원래 줄(또는 원래 행) 그대로 |

<h2>④ 바뀐 결과</h2>

①의 서로 다르던 세 줄이 같은 일곱 키가 됩니다. 이 표는 키가 세로입니다.

| 키 | 웹 서버 한 줄 | 판정 서버 한 줄 | SaaS 한 줄 |
|---|---|---|---|
| `time` | `2026-11-02 09:12:03` | `2026-11-02 09:40:00` | `2026-11-02 02:14:08` |
| `source` | `web` | `server` | `saas` |
| `user` | `None` | `seoyeon` | `jiwoo` |
| `ip` | `203.0.113.50` | `None` | `203.0.113.80` |
| `action` | `POST /login` | `SALES:QUERY` | `login` |
| `result` | `실패` | `성공` | `실패` |
| `raw` | ①의 원래 줄 | ①의 원래 줄 | ①의 원래 행(딕셔너리) |

- <mark>원래 로그에 없는 값은 임의로 만들어 넣지 않고 `None` 으로 둡니다.</mark> 없는 값을 지어내면 분석 결과가 틀려집니다.
- <mark>`raw` 는 바꾸지 않은 원래 로그입니다.</mark> 정규화 과정에서 사라지는 정보를 나중에 찾아볼 수 있게 남깁니다.

## 1.2 시각 문자열 바꾸기

<h2>문법 상자 — 시각 값을 원하는 모양의 문자열로</h2>

**<mark>`.strftime(형식)`</mark> 은 시각 값을 원하는 모양의 문자열로 만듭니다. 형식에 적은 모양대로 시각이 문자열이 됩니다**

로그마다 시각 모양이 달라서, <mark>먼저 시각 값으로 바꾼 뒤 공통 모양의 문자열로 다시 만듭니다.</mark> 문자열을 시각 값으로 바꾸는 `strptime` 은 Module 3에서 쓴 방법 그대로라서 여기서는 설명하지 않습니다.

```python
from datetime import datetime  # 날짜와 시각을 다루는 datetime 클래스를 불러온다

time_text = "02/Nov/2026:09:12:03 +0900"  # nginx 시각 문자열
parsed = datetime.strptime(time_text, "%d/%b/%Y:%H:%M:%S %z")  # 문자열을 시각 값으로 바꾼다(모양을 형식으로 알려 준다)
print(parsed)  # 시각 값을 출력한다

time_out = parsed.strftime("%Y-%m-%d %H:%M:%S")  # 시각 값을 공통 모양의 문자열로 바꾼다
print(time_out)  # 문자열을 출력한다
```

실행 결과:

```
2026-11-02 09:12:03+09:00
2026-11-02 09:12:03
```

- 형식 코드는 `%Y`(년) · `%m`(월) 처럼 `%` 로 시작하는 기호로, <mark>시각 문자열의 어느 부분이 일 · 달 · 연도인지 알려 줍니다</mark>.
  - `%d` 는 일, `%b` 는 영어 달 이름(Nov), `%Y` 는 연도 4자리입니다.
  - `%H` `%M` `%S` 는 시 · 분 · 초이고, `%z` 는 시간대(+0900)입니다.

nginx 시각 문자열을 부분마다 형식 코드와 하나씩 맞춰 봅니다.

| 문자열 부분 | 형식 코드 | 뜻 |
|---|---|---|
| `02` | `%d` | 일 |
| `Nov` | `%b` | 영어 달 이름 |
| `2026` | `%Y` | 연도 4자리 |
| `09` | `%H` | 시 |
| `12` | `%M` | 분 |
| `03` | `%S` | 초 |
| `+0900` | `%z` | 시간대 |

- 문자열 `02/Nov/2026:09:12:03 +0900` 에서 부분 사이의 `/` · `:` · 공백은 형식에도 똑같이 적습니다. <mark>그래서 형식은 `%d/%b/%Y:%H:%M:%S %z` 입니다.</mark>
- <mark>`.strftime(형식)` 은 반대로 시각 값을 같은 형식 코드로 문자열로 만듭니다.</mark> 위에서는 `2026-11-02 09:12:03` 모양입니다.
- 이번 Unit에서 새로 나오는 것은 형식 코드 `%b` · `%z` 와, <mark>시각 값을 문자열로 만드는 `strftime` 입니다.</mark>

<h2>문법 상자 — 시간대 정보 지우기</h2>

**시각 값에 붙은 시간대(`+0900`)는 <mark>`.replace(tzinfo=None)`</mark> 으로 지울 수 있고, 지우면 한국 시각만 남은 시각 값이 됩니다**

```python
from datetime import datetime  # 날짜와 시각을 다루는 datetime 클래스를 불러온다

time_text = "02/Nov/2026:09:12:03 +0900"  # nginx 시각 문자열
parsed = datetime.strptime(time_text, "%d/%b/%Y:%H:%M:%S %z")  # 문자열을 시각 값으로 바꾼다
print(parsed.tzinfo)  # 시간대 정보를 출력한다

local_time = parsed.replace(tzinfo=None)  # 시간대 정보를 지우고 한국 시각만 남긴다
print(local_time)  # 시간대 없는 시각을 출력한다
```

실행 결과:

```
UTC+09:00
2026-11-02 09:12:03
```

- 시각 값이 `+0900`(한국 시간대)을 갖고 있으면 **시간대 정보가 없는 시각 값과 직접 비교할 때 오류가 납니다.**
- 세 로그의 시각은 모두 한국 시간이므로, 이번 Unit에서는 <mark>시간대 정보를 지우고 한국 시각만 남겨 세 로그의 시각 값을 같은 종류로 맞춥니다</mark>.

<h2>한 장 정리</h2>

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `read_time_text` | 요청 앞 조각 | 대괄호 안의 시각 문자열(미리 채움) |
| `convert_time` | nginx 시각 문자열 | 공통 모양 시각 문자열 |
| `convert_result` | 상태 코드(정수) | `"성공"` 또는 `"실패"` |
| `normalize_web` | 로그 한 줄 | 공통 이벤트 딕셔너리. 깨진 줄이면 `None`(미리 채움) |

- **직접 쓰는 곳은 두 함수**(번호 1 ~ 6)입니다.
  - `convert_time`(1 ~ 3번): 문자열을 시각 값으로 바꾸고, 시간대를 떼고, 공통 모양 문자열로 만듭니다.
  - `convert_result`(4 ~ 6번): 상태 코드 400 이상이면 `"실패"`, 아니면 `"성공"` 입니다.
- **미리 채운 것**: Unit 1에서 만든 함수를 불러 조각을 꺼내 공통 이벤트로 묶는 `normalize_web` 과 `read_time_text` 입니다.

## 실습 2-1 · 웹 로그 한 줄을 이벤트로

<h2>이런 상황이 있습니다</h2>

- **지금은**: 웹 서버 로그의 시각(`02/Nov/2026:09:12:03 +0900`)은 다른 로그와 비교하기 어렵고, 성공 · 실패는 상태 코드라서 따로 판단해야 합니다.
- **그래서 만드는 것**: `normalize_web.py` 입니다.
  - 시각을 `2026-11-02 09:12:03` 모양으로 바꿉니다.
  - 상태 코드를 `성공` · `실패` 로 바꿉니다.
  - 원래 줄은 `raw` 에 남깁니다.
- **실행하면**: 단계 1: 이벤트 수와 첫 이벤트, 단계 2: 처음 나오는 실패 이벤트, 단계 3: 성공 · 실패별 이벤트 수가 나옵니다.
- **현업에서는**: 로그를 모으는 도구에는 로그 종류마다 이 변환을 하는 부분(파서)이 있습니다. <mark>변환이 틀리면 그 로그 전체가 잘못 분석되므로 `raw` 와 대조합니다.</mark>

<h2>할 일</h2>

1. **`normalize_web.py` · `exercise2-1_run.py`** 두 파일을 만들고, `normalize_web.py` 의 `convert_time` · `convert_result` 에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>정규화한 이벤트 수와 읽기 실패한 줄</mark>(단계 1), <mark>처음 나오는 실패 이벤트</mark>(단계 2), <mark>성공 · 실패별 개수</mark>(단계 3)를 읽습니다.

<h3><code>normalize_web.py</code></h3>

```python
from datetime import datetime  # 날짜와 시각을 다루는 datetime 클래스를 불러온다
from log_parse import split_request, read_request, read_status, read_client  # Unit 1에서 만든 로그 읽기 함수를 불러온다

NGINX_TIME_FORMAT = "%d/%b/%Y:%H:%M:%S %z"  # nginx 시각의 모양(예: 02/Nov/2026:09:12:03 +0900)
COMMON_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"  # 공통 시각의 모양(예: 2026-11-02 09:12:03)


def read_time_text(prefix):  # 요청 앞 조각을 받는 함수
    """요청 앞 조각에서 대괄호 안의 시각 문자열을 꺼낸다.
    웹 서버 로그의 시각을 공통 모양으로 바꾸기 전에 쓴다.
    """
    parts = prefix.split()  # 공백 기준으로 나눈다
    bracket_text = parts[3] + " " + parts[4]  # '[02/Nov/2026:09:12:03' 과 '+0900]' 를 이어 붙인다
    time_text = bracket_text.strip("[]")  # 양쪽 끝의 대괄호를 지운다
    return time_text  # 대괄호 없는 시각 문자열을 리턴한다


def convert_time(time_text):  # nginx 시각 문자열을 받는 함수
    """nginx 시각을 공통 모양의 문자열로 바꾼다.
    예: 02/Nov/2026:09:12:03 +0900 → 2026-11-02 09:12:03.
    웹 서버 로그를 공통 이벤트로 만들 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. datetime.strptime(time_text, NGINX_TIME_FORMAT) 의 결과를 parsed 에 담는다
    # 2. parsed.replace(tzinfo=None) 의 결과를 local_time 에 담는다 (+0900 정보를 떼고 한국 시각만 남긴다)
    # 3. local_time.strftime(COMMON_TIME_FORMAT) 의 결과를 time_out 에 담는다
    return time_out  # 공통 모양의 시각 문자열을 리턴한다


def convert_result(status):  # 상태 코드(정수)를 받는 함수
    """상태 코드가 400 이상이면 「실패」, 아니면 「성공」을 리턴한다.
    웹 서버 로그의 결과를 공통 이벤트의 result 로 바꿀 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. status 가 400 이상이면 (if)
    # 5.   "실패" 를 리턴한다
    # 6. 그 밖에는 "성공" 을 리턴한다


def normalize_web(line):  # 로그 한 줄을 받는 함수
    """웹 서버 로그 한 줄을 공통 이벤트 딕셔너리로 바꾸고, 깨진 줄이면 None 을 리턴한다.
    웹 서버 로그를 다른 로그와 같은 모양으로 맞출 때 쓴다.
    """
    if line.count('"') < 2:  # 큰따옴표가 두 개보다 적은 깨진 줄이면
        return None  # 읽지 않고 None 을 리턴한다
    prefix, request_text, suffix = split_request(line)  # 세 조각으로 나눈다
    method, path = read_request(request_text)  # 요청 조각에서 방법과 경로를 꺼낸다
    status = read_status(suffix)  # 뒤 조각에서 상태 코드를 꺼낸다
    client_ip = read_client(prefix)  # 앞 조각에서 접속자 주소를 꺼낸다
    time_text = read_time_text(prefix)  # 앞 조각에서 시각 문자열을 꺼낸다
    time_out = convert_time(time_text)  # 공통 모양의 시각으로 바꾼다
    result = convert_result(status)  # 상태 코드를 성공 · 실패로 바꾼다
    action = method + " " + path  # 방법과 경로를 하나의 행동으로 합친다
    raw_text = line.strip()  # 원래 줄(양끝 공백과 줄바꿈 뺀 것)을 보관한다
    event = {  # 공통 이벤트의 키로 묶는다
        "time": time_out,  # 일어난 시각
        "source": "web",  # 어느 로그에서 왔는지
        "user": None,  # 웹 서버 로그에는 사용자가 없다
        "ip": client_ip,  # 접속자 주소
        "action": action,  # 무엇을 했는지
        "result": result,  # 성공인지 실패인지
        "raw": raw_text,  # 원래 로그 줄
    }
    return event  # 공통 이벤트를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 6번은 함수 안이라 앞에 공백 4개이고, 그중 5번의 `return` 만 `if` 안쪽이라 공백 8개입니다.
- 번호 주석이 연달아 붙어 있어도(예: 1 · 2 · 3번), <mark>주석 사이마다 줄을 끼워 넣어 각 주석 바로 아래 줄에 그 번호의 코드를 하나씩 씁니다.</mark>
- **채우기 전에 실행하면 `NameError: name 'time_out' is not defined` 오류가 납니다.** 1 ~ 3번을 아직 안 썼기 때문입니다.
- `convert_result` 는 6번까지 쓰면 끝나는 함수라서 아래에 미리 채운 `return` 이 없습니다. <mark>5번과 6번의 `return` 을 직접 씁니다.</mark>

<h3><code>exercise2-1_run.py</code></h3>

그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 샘플 로그를 한 줄씩 공통 이벤트로 바꿔 세 단계로 출력합니다. `len(리스트)` 는 리스트의 개수입니다.

```python
from normalize_web import normalize_web  # 방금 만든 웹 서버 로그 정규화 함수를 불러온다

events = []  # 정규화한 이벤트를 모을 리스트
fail_count = 0  # 읽기 실패한 줄 수를 0 으로 시작한다
with open("access_sample.log", encoding="utf-8") as log_file:  # 샘플 로그 파일을 연다
    for line in log_file:  # 파일에서 한 줄씩 꺼낸다
        event = normalize_web(line)  # 한 줄을 공통 이벤트로 바꾼다
        if event is None:  # 깨진 줄이라 읽지 못했으면
            fail_count = fail_count + 1  # 읽기 실패한 줄 수를 1 늘린다
        else:  # 바꿨으면
            events.append(event)  # 이벤트 리스트에 추가한다

event_count = len(events)  # 정규화한 이벤트 수를 센다
print("--- 단계 1: 정규화한 이벤트", event_count, "개 · 읽기 실패", fail_count, "줄")  # 단계 1 시작을 알리는 줄
first_event = events[0]  # 첫 이벤트를 꺼낸다
print(first_event)  # 첫 이벤트를 출력한다

first_failed = None  # 처음 나오는 실패 이벤트를 담을 변수(아직 없음)
for event in events:  # 이벤트를 하나씩 꺼낸다
    if event["result"] == "실패" and first_failed is None:  # 실패 이벤트이고 아직 담은 것이 없으면
        first_failed = event  # 이 이벤트를 담는다
print("--- 단계 2: 처음 나오는 실패 이벤트")  # 단계 2 시작을 알리는 줄
print(first_failed)  # 처음 나오는 실패 이벤트를 출력한다

result_counts = {}  # 결과별 횟수를 담을 딕셔너리
for event in events:  # 이벤트를 하나씩 꺼낸다
    result = event["result"]  # 그 이벤트의 결과
    result_counts[result] = result_counts.get(result, 0) + 1  # 그 결과의 횟수를 1 늘린다
print("--- 단계 3: 성공 · 실패별 이벤트 수")  # 단계 3 시작을 알리는 줄
print(result_counts)  # 성공 · 실패별 개수를 출력한다
```

<h2>순서</h2>

1. **[VS Code]** 파일 `normalize_web.py` · `exercise2-1_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `normalize_web.py` 에서 직접 쓰는 곳 **여섯 군데**를 씁니다. 1.2 의 문법 상자를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise2-1_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-1_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **세 단계**입니다. `--- 단계` 제목 줄은 세지 않고, 단계 1은 1줄, 단계 2는 1줄, 단계 3은 1줄입니다.
5. **[실습 기록]** `report_u2.md` 의 `## 실습 2-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 정규화한 이벤트 수와 읽기 실패한 줄 수, 성공과 실패 개수를 적어 주세요.
   - (나) [핵심 질문] 시각을 `02/Nov/2026:09:00:00 +0900` 모양 그대로 문자열로 정렬하면 12월 1일 요청(`01/Dec/2026:…`)과 11월 2일 요청(`02/Nov/2026:…`) 중 어느 쪽이 앞에 놓일지 예상하고, 공통 모양(`2026-11-02 09:00:00`)으로 바꾸면 무엇이 달라지는지 이유와 함께 적어 주세요.
   - (다) [핵심 질문] 이벤트에 원래 로그 줄(`raw`)을 그대로 남겨 두는 이유는 무엇인가요? 정규화하면 사라지는 정보를 한 가지 예로 들어 함께 적어 주세요.

<!-- answer: 05|실습 2-1 정답 -->

## 실습 2-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 문자열 시각을 시각 값으로 | `parsed = datetime.strptime(time_text, NGINX_TIME_FORMAT)` |
| 시간대 정보 떼기 | `local_time = parsed.replace(tzinfo=None)` |
| 공통 모양 문자열로 | `time_out = local_time.strftime(COMMON_TIME_FORMAT)` |
| 상태 코드 → 결과 | `if status >= 400:` → `return "실패"` → `return "성공"` |

---
