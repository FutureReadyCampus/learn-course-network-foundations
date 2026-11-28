---
id: m4-u01-l02
title: 실습 1-1 · 접속 로그 한 줄 조각내기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/096_day01_pm_log_basics.md
  mission_id: GichanSource.m4-1102-pm-log-basics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 1-1 · 접속 로그 한 줄 조각내기

## 목표: 로그 한 줄 파서

> **오늘 들어온 일**
>
> A사 웹서비스 담당이 보낸 메시지입니다(Module 3의 판정 서버가 아니라 게시판 웹서버가 남기는 접속 로그 이야기입니다):
> 「얼마 전 한 직원이 "게시판 로그인이 계속 안 된다"고 문의했습니다. 그 직원의 기록을 찾으려고 접속 로그 파일을 열어 눈으로 한 줄씩 읽었고, 오래 걸렸습니다. 접속 로그는 하루에 수만 줄이 쌓입니다.
>
> 로그 한 줄은 주소 · 시각 · 요청 · 결과가 나뉘지 않은 하나의 문자열이라 프로그램이 값을 꺼내 쓰지 못합니다. 한 줄을 접속자 주소 · 요청 방법 · 경로 · 상태 코드로 나눠 주세요. 끝이 잘리거나 깨진 줄은 읽지 않고 넘어가되, 읽기에 성공한 줄과 읽기에 실패한 줄이 몇 줄씩인지 알려 주세요.」
> - **왜 중요한가**: <mark>부분으로 나누지 못하면 「상태 코드가 401 인 줄이 몇 개인가」 같은 질문에 사람이 한 줄씩 읽어서 답해야 합니다.</mark> 나눠 두면 세고 비교하는 일을 코드가 합니다. 읽기 실패한 줄 수는 로그가 잘 쌓이고 있는지 보는 기준이 됩니다. 이 함수가 Module 4 내내 모든 탐지의 첫 단계가 됩니다.
> - **이 실습에서 하는 일**: 로그 한 줄을 나누는 `log_parse.py` 를 만듭니다. 대부분은 미리 채워 두었고, 한 줄을 세 조각으로 나누는 줄과 상태 코드를 정수로 바꾸는 줄, 두 줄만 직접 씁니다.
> - **끝나면 쓰는 것**: 자기 점검 질문 (가) · (다) 답. (나)는 여유가 되면 하는 응용입니다.

## 왜 로그를 조각으로 나누는가

1. 서버는 요청을 받을 때마다 로그를 한 줄씩 남깁니다. Module 3 응용 4-3에서 판정 서버(`access_server.py`)를 만들었다면 그 서버도 요청마다 한 줄씩 남겼습니다. <mark>Module 4에서는 이런 서버 로그에서 **평소와 다른 접속**을 찾습니다.</mark>
   - 평소와 다른 접속의 예: 같은 주소에서 로그인을 연달아 실패함, 관리자 페이지를 반복해서 요청함, 짧은 시간에 요청이 몰림
2. <mark>찾으려면 로그를 **읽을 수 있는 값**으로 바꿔야 합니다.</mark>
   - 로그 한 줄은 하나의 긴 문자열이라 <mark>그대로는 「상태 코드가 401 인 줄」을 셀 수 없습니다.</mark>
   - 실습 1-1에서는 한 줄을 접속자 주소 · 방법 · 경로 · 상태 코드로 나눕니다. 실습 1-2에서는 나눈 값을 불러 다른 로그와 같은 모양의 이벤트로 바꿉니다.

## 로그 · 이벤트 · 알림

| 말 | 뜻 | 예 |
|---|---|---|
| 로그(log, 로그) | 시스템이 일어난 일을 한 줄씩 적은 기록. 의미를 판단하지 않은 원재료 | `203.0.113.50 … "POST /login" 401` |
| 이벤트(event, 이벤트) | 로그 중에서 보안에서 의미가 있다고 볼 수 있는 일 | 같은 주소에서 로그인 실패 5번 |
| 알림(alert, 얼럿) | 이벤트 중에서 사람이 봐야 한다고 판단해 알려 주는 것 | 담당자에게 가는 경고 메시지 |

- 로그가 가장 많고, 이벤트는 그보다 적고, 알림은 더 적습니다. <mark>걸러질수록 사람이 볼 양이 줄어듭니다.</mark>
- 알림은 「먼저 살펴볼 곳」이라는 뜻이고 <mark>**공격이 확정됐다는 뜻이 아닙니다.**</mark>

## 접속 로그 한 줄의 여섯 부분

웹서버 **nginx(엔진엑스)** 는 요청이 들어올 때마다 로그를 한 줄씩 남깁니다. 한 줄은 이렇게 생겼습니다.

```
203.0.113.50 - - [02/Nov/2026:09:12:03 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
```

| 부분 | 값의 예 | 뜻 |
|---|---|---|
| 접속자 주소 | `203.0.113.50` | 요청을 보낸 쪽의 IP 주소 |
| 시각 | `[02/Nov/2026:09:12:03 +0900]` | 서버가 요청을 받은 때(+0900 은 한국 시간대) |
| 요청 | `"POST /login HTTP/1.1"` | 방법(POST) · 경로(/login) · 통신 규칙의 버전(HTTP/1.1) |
| 상태 코드 | `401` | 요청이 어떻게 끝났는지를 나타내는 세 자리 숫자 |
| 응답 크기 | `312` | 서버가 응답으로 보낸 데이터의 크기(바이트) |
| 요청 프로그램 | `"python-requests/2.31.0"` | 요청을 보낸 프로그램의 이름 |

요청 프로그램 칸에는 보낸 쪽에 따라 이런 이름이 적힙니다.

| 보낸 쪽 | 적히는 이름 |
|---|---|
| 브라우저 | `Mozilla/5.0` 같은 이름 |
| 파이썬 프로그램 | `python-requests` |
| 명령 도구 | `curl`(컬) |

- 맨 앞 주소 뒤의 `- -` 두 개는 쓰지 않는 칸이고, 요청 뒤의 `"-"` 는 어디서 왔는지(참조 주소)가 없다는 뜻입니다.
- <mark>이 로그에 들어 있는 것은 위 여섯 부분이 전부입니다.</mark>
- 요청 방법 `GET` 은 페이지를 읽어 오는 요청이고, `POST` 는 로그인 정보처럼 데이터를 보내는 요청입니다.
- 경로의 `?` 뒤는 요청에 덧붙인 값입니다. 예를 들어 `/board?page=2` 는 게시판의 2쪽을 달라는 뜻입니다.

상태 코드는 약속된 숫자이고 공식 이름이 있습니다.

| 상태 코드 | 공식 이름 | 뜻 |
|---|---|---|
| 200 | OK | 정상 처리 |
| 301 · 302 | Moved Permanently · Found | 다른 주소로 이동하라는 응답(로그인에 성공하면 302 가 자주 나옵니다) |
| 401 | Unauthorized | 로그인이 필요하거나 로그인 정보가 틀림 |
| 403 | Forbidden | 로그인했어도 그 주소를 볼 권한이 없음 |
| 404 | Not Found | 그 경로가 없음 |
| 500 | Internal Server Error | 서버 안에서 오류가 남 |

<mark>숫자의 첫 자리가 큰 구분입니다.</mark>

| 첫 자리 | 뜻 |
|---|---|
| 2 | 성공 |
| 3 | 이동 |
| 4 | 요청한 쪽 문제 |
| 5 | 서버 문제 |

<h2>문법 상자 — 큰따옴표로 두 번만 나누기</h2>

**<mark>`split`</mark> 에 나눌 횟수를 주면 앞에서부터 그만큼만 나눕니다**

보기 1 — 횟수를 주지 않고 모두 나누면 몇 조각이 되는지 봅니다.

```python
line = 'a "GET /login HTTP/1.1" 401 312 "-" "Mozilla/5.0"'  # 큰따옴표가 여섯 개 들어 있는 줄
parts = line.split('"')                                     # 큰따옴표를 기준으로 모두 나눈다
count = len(parts)                                          # 나뉜 조각의 개수를 센다
print(count)                                                # 조각의 개수를 출력한다
```

실행 결과:

```
7
```

보기 2 — 횟수 2 를 주고 나누면 어떻게 달라지는지 봅니다.

```python
line = 'a "GET /login HTTP/1.1" 401 312 "-" "Mozilla/5.0"'  # 큰따옴표가 여섯 개 들어 있는 줄
prefix, request_text, suffix = line.split('"', 2)           # 앞의 큰따옴표 두 개에서만 나눠 세 조각에 담는다
print(request_text)                                         # 가운데 조각(요청)을 출력한다
print(suffix)                                               # 뒤 조각을 출력한다
```

실행 결과:

```
GET /login HTTP/1.1
 401 312 "-" "Mozilla/5.0"
```

- <mark>큰따옴표로 모두 나누면 7조각이 됩니다.</mark> 이 줄에는 큰따옴표가 여섯 개 있기 때문입니다.
- `split('"', 2)` 는 <mark>앞의 큰따옴표 두 개에서만 나눠 **앞 · 요청 · 뒤** 세 조각이 됩니다.</mark> 요청은 첫 번째 큰따옴표 안의 문자열입니다.
- 세 조각을 세 이름에 한꺼번에 담을 수 있습니다(`prefix, request_text, suffix = …`).
- 함수가 `return method, path` 처럼 값 여러 개를 리턴하면 받는 쪽도 `method, path = read_request(…)` 로 한꺼번에 받습니다.
- `parse`(파스)는 글을 읽어 부분으로 나눈다는 뜻이고, 변수 `entry`(엔트리)는 읽은 요청 한 개를 가리킵니다.

보기 3 — 로그에서 꺼낸 상태 코드는 `'401'` 같은 **문자열**입니다. <mark>`int(문자열)`</mark> 로 정수로 바꿔야 `400` 같은 숫자와 크기를 비교할 수 있습니다.

```python
status_text = "401"                  # 로그에서 꺼낸 상태 코드는 문자열이다
status = int(status_text)            # 정수로 바꿔 status 에 담는다
print([status_text, status])         # 둘을 리스트로 나란히 출력한다
print(status >= 400)                 # 정수라서 400 과 비교할 수 있다
```

실행 결과:

```
['401', 401]
True
```

- 리스트로 출력하면 문자열에는 따옴표(`'401'`)가 붙고 정수에는 붙지 않아서 둘이 구분됩니다.

<figure class="page-figure"><img src="assets/u01l02_f01.svg" alt="로그 한 줄을 큰따옴표로 세 조각으로 나누고, 조각마다 읽는 함수가 다르다"></figure>

<h2>한 장 정리</h2>

| 함수 | 받는 것 | 리턴하는 것 | 직접 쓰는 곳 |
|---|---|---|---|
| `split_request` | 로그 한 줄(문자열) | 앞 · 요청 · 뒤 세 조각 | ① 한 줄 |
| `read_request` | 요청 조각 | 방법과 경로 | 없음(미리 채움) |
| `read_status` | 뒤 조각 | 상태 코드(정수) | ② 한 줄 |
| `read_client` | 앞 조각 | 접속자 주소 | 없음(미리 채움) |
| `parse_line` | 로그 한 줄 | 딕셔너리, 깨진 줄이면 `None` | 없음(미리 채움) |

- **직접 쓰는 곳은 두 곳**(① · ②), 한 줄씩입니다. 나머지는 미리 채웠고, 줄마다 주석으로 하는 일을 적었습니다.
- `parse_line` 은 미리 채웠습니다. 큰따옴표가 두 개보다 적은 깨진 줄이면 `None` 을 리턴하고, 아니면 네 값을 `{"ip", "method", "path", "status"}` 딕셔너리로 묶습니다.

## 실습 1-1 · 로그 한 줄에서 네 값 꺼내기

<h2>이런 상황이 있습니다</h2>

- **지금은**: 로그 30줄이 모두 긴 문자열이라, 상태 코드가 401 인 요청이 몇 개인지 세려면 사람이 한 줄씩 읽어야 합니다. 잘리거나 깨진 줄도 섞여 있습니다.
- **그래서 만드는 것**: `log_parse.py` 입니다.
  - 한 줄을 접속자 주소 · 방법 · 경로 · 상태 코드로 나눠 딕셔너리로 만듭니다.
  - <mark>깨진 줄은 읽기 실패로 세고 넘어갑니다.</mark>
- **실행하면**: 단계 1: 전체 줄 수와 읽기 성공 · 읽기 실패 줄 수, 단계 2: 로그 첫 3줄을 읽은 결과(딕셔너리), 단계 3: 값이 덧붙은 요청(경로에 `?` 포함)이 나옵니다.
- **현업에서는**: 로그 분석은 한 줄을 부분으로 나누는 일부터 시작합니다. 깨진 줄 수는 로그가 잘 쌓이고 있는지 확인하는 데 씁니다.

<h2>할 일</h2>

1. <mark>`log_parse.py` · `exercise1-1_run.py` 두 파일</mark>을 만들고, `log_parse.py` 에서 `# ←` 가 있는 <mark>두 곳</mark>(`split_request` 의 ① · `read_status` 의 ②)을 한 줄씩 채웁니다.
2. 채우기 <mark>전과 후</mark>에 한 번씩 실행해서 <mark>읽기 성공 · 읽기 실패 줄 수</mark>(단계 1: 읽기), <mark>로그 첫 3줄을 읽은 결과</mark>(단계 2), <mark>값이 덧붙은 요청</mark>(단계 3)을 읽습니다.

<h3><code>log_parse.py</code></h3>

‘정답 보기’를 누르면 아래 코드의 ①과 ②에 정답 줄이 표시됩니다.

<pre><code class="language-python">def split_request(line):                                # 로그 한 줄(문자열)을 받는 함수
    """로그 한 줄을 큰따옴표 기준으로 앞 · 요청 · 뒤 세 조각으로 나눈다.
    나뉘지 않은 하나의 문자열인 로그에서 값을 꺼내기 시작할 때 쓴다.
    """
    # ① line 을 큰따옴표(")로 두 번만 나눠 prefix, request_text, suffix 세 이름에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
<span data-answer-line="    prefix, request_text, suffix = line.split(&#x27;&quot;&#x27;, 2)"></span>
    return prefix, request_text, suffix                 # 세 조각을 리턴한다


def read_request(request_text):                         # 요청 조각(예: GET /login HTTP/1.1)을 받는 함수
    """요청 조각에서 방법(method)과 경로(path)를 꺼낸다.
    무엇을 요청했는지 알고 싶을 때 쓴다.
    """
    method, path, protocol = request_text.split()       # 공백 기준으로 나눈 세 값을 세 이름에 담는다(버전 protocol 은 쓰지 않음)
    return method, path                                 # 방법과 경로를 리턴한다


def read_status(suffix):                                # 요청 뒤 조각(예:  401 312 "-" "Mozilla/5.0")을 받는 함수
    """요청 뒤 조각에서 상태 코드를 꺼내 정수로 리턴한다.
    요청이 성공했는지 실패했는지 가를 때 쓴다.
    """
    parts = suffix.split()                              # 공백 기준으로 나눠 조각 리스트를 만든다
    status_text = parts[0]                              # 첫 조각이 상태 코드 문자열이다(예: '401')
    # ② status_text 를 정수로 바꿔 status 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
<span data-answer-line="    status = int(status_text)"></span>
    return status                                       # 상태 코드(정수)를 리턴한다


def read_client(prefix):                                # 요청 앞 조각(예: 203.0.113.50 - - [02/Nov/2026:09:12:03 +0900] )을 받는 함수
    """요청 앞 조각에서 접속자 주소를 꺼낸다.
    어느 주소가 요청했는지 알고 싶을 때 쓴다.
    """
    parts = prefix.split()                              # 공백 기준으로 나눠 조각 리스트를 만든다
    client_ip = parts[0]                                # 첫 조각이 접속자 주소이다
    return client_ip                                    # 접속자 주소를 리턴한다


def parse_line(line):                                   # 로그 한 줄을 받는 함수
    """로그 한 줄을 ip · method · path · status 딕셔너리로 바꾼다.
    깨진 줄이면 None 을 리턴한다.
    접속 로그를 분석하기 전에 한 줄을 값으로 나눌 때 쓴다.
    """
    if line.count('"') &lt; 2:                             # 큰따옴표가 두 개보다 적은 깨진 줄이면
        return None                                     # 읽을 수 없으니 None 을 리턴한다
    prefix, request_text, suffix = split_request(line)  # 세 조각으로 나눈다
    method, path = read_request(request_text)           # 요청 조각에서 방법과 경로를 꺼낸다
    status = read_status(suffix)                        # 뒤 조각에서 상태 코드를 꺼낸다
    client_ip = read_client(prefix)                     # 앞 조각에서 접속자 주소를 꺼낸다
    entry = {                                           # 꺼낸 값을 딕셔너리로 묶는다
        "ip": client_ip,                                # 접속자 주소
        "method": method,                               # 요청 방법
        "path": path,                                   # 요청 경로
        "status": status,                               # 상태 코드(정수)
    }
    return entry                                        # 딕셔너리를 리턴한다
</code></pre>

- 주석 줄은 그대로 두고, **각 주석 바로 아래 줄**에 씁니다. ① · ② 모두 함수 안의 줄이라 앞에 공백 4개(4칸)에서 시작합니다.
- 미리 채운 `read_request` · `read_status` · `read_client` 의 `split()` 처럼 괄호 안을 비우면 공백(띄어쓰기)을 기준으로 나눕니다. 공백이 여러 칸이거나 `suffix` 처럼 맨 앞에 공백이 있어도 빈 조각을 만들지 않습니다.
- 미리 채운 `parse_line` 의 `line.count('"')` 는 줄 안의 큰따옴표 개수를 셉니다. 정상 줄에는 여섯 개가 있고, 깨진 줄은 두 개보다 적습니다.

<h3>직접 쓰는 곳</h3>

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | `line` 을 큰따옴표로 두 번만 나눠 세 이름에 담기 | 4칸 |
| ② | `status_text` 를 정수로 바꿔 `status` 에 담기 | 4칸 |

- 채우기 전에 실행하면 `NameError: name 'prefix' is not defined` 가 나옵니다. ① 을 아직 안 써서 `split_request` 가 리턴할 `prefix` 가 없기 때문이니 정상입니다.
- ① 확인: ① 을 쓰고 실행하면 오류가 `NameError: name 'status' is not defined` 로 바뀌어야 합니다. ② 를 아직 안 써서 나는 오류이니 정상입니다. 막히면: 문법 상자 보기 2 의 `prefix, request_text, suffix = line.split('"', 2)` 를 그대로 씁니다.
- ② 확인: ② 까지 쓰고 실행하면 단계 1 에 `읽기 성공 28 줄 · 읽기 실패 2 줄` 이 나오고, 단계 2 의 딕셔너리가 `'status': 200` 처럼 따옴표 없는 숫자로 끝나면 성공입니다. 막히면: 문법 상자 보기 3 의 `status = int(status_text)` 와 같은 모양입니다.

<h3><code>exercise1-1_run.py</code></h3>

<mark>그대로 붙여 넣습니다.</mark> 학생이 쓰는 줄은 없습니다. 샘플 로그를 한 줄씩 읽어 세 단계로 출력합니다.

```python
from log_parse import parse_line                                       # 방금 만든 로그 한 줄 읽기 함수를 불러온다

LOG_PATH = "access_sample.log"                                         # 읽을 샘플 로그 파일 이름
entries = []                                                           # 읽은 요청을 모을 리스트
fail_count = 0                                                         # 읽기 실패한 줄 수를 0 으로 시작한다
total = 0                                                              # 전체 줄 수를 0 으로 시작한다
with open(LOG_PATH, encoding="utf-8") as log_file:                     # 로그 파일을 연다
    for line in log_file:                                              # 파일에서 한 줄씩 꺼낸다
        total = total + 1                                              # 전체 줄 수를 1 늘린다
        entry = parse_line(line)                                       # 한 줄을 읽어 딕셔너리로 바꾼다
        if entry is None:                                              # 깨진 줄이라 읽지 못했으면
            fail_count = fail_count + 1                                # 읽기 실패한 줄 수를 1 늘린다
        else:                                                          # 읽었으면
            entries.append(entry)                                      # 요청 리스트에 추가한다

success_count = len(entries)                                           # 읽기 성공한 줄 수를 센다
print("--- 단계 1: 로그 파일 읽기 - 전체", total, "줄")                # 단계 1 시작을 알리는 줄
print("읽기 성공", success_count, "줄 · 읽기 실패", fail_count, "줄")  # 읽기 성공과 읽기 실패한 줄 수를 출력한다
print("--- 단계 2: 로그 첫 3줄을 읽은 결과")                           # 단계 2 시작을 알리는 줄
print(entries[0])                                                      # 첫째 줄에서 읽은 딕셔너리를 출력한다
print(entries[1])                                                      # 둘째 줄에서 읽은 딕셔너리를 출력한다
print(entries[2])                                                      # 셋째 줄에서 읽은 딕셔너리를 출력한다
print("--- 단계 3: 값이 덧붙은 요청 (경로에 ? 포함)")                  # 단계 3 시작을 알리는 줄
for entry in entries:                                                  # 읽은 요청을 하나씩 꺼낸다
    if "?" in entry["path"]:                                           # 경로 안에 ? 가 들어 있으면
        print(entry["ip"], entry["path"])                              # 접속자 주소와 경로를 출력한다
```

<h2>순서 · 파일 작성과 터미널 실행</h2>

1. **[VS Code]** `anomaly_detection` 폴더에 `log_parse.py` · `exercise1-1_run.py` 두 파일을 만들어, 위의 같은 이름 코드 상자 내용을 각각 붙여 넣고 저장합니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 `log_parse.py` 를 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
- [ ] `anomaly_detection` 폴더에 `exercise1-1_run.py` 를 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
<!-- /checklist -->

2. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지 확인하고</mark> **채우기 전에** 한 번 실행합니다. `NameError: name 'prefix' is not defined` 가 나오면 정상입니다.
   ```bash
   pwd
   python exercise1-1_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise1-1_run.py` 파이썬으로 실행 파일 실행
3. **[VS Code]** `log_parse.py` 의 `# ←` 두 곳(① · ②)을 채웁니다. 「접속 로그 한 줄의 여섯 부분」 쪽의 그림과 문법 상자를 보고 씁니다. 그리고 터미널에서 다시 실행합니다.
   ```bash
   pwd
   python exercise1-1_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise1-1_run.py` 파이썬으로 실행 파일 실행

<!-- checklist -->
- [ ] `log_parse.py` 의 빈칸 ① · ② 를 한 줄씩 채우고 저장했다
<!-- /checklist -->

4. 출력은 세 단계입니다. `--- 단계` 제목 줄은 세지 않고, <mark>단계 1은 한 줄, 단계 2는 딕셔너리 세 줄, 단계 3은 두 줄입니다.</mark> 읽기 실패한 줄은 붙여 넣은 `access_sample.log` 에서 큰따옴표가 두 개보다 적은 줄을 찾습니다.

<!-- checklist -->
- [ ] `python exercise1-1_run.py` 를 실행해 `읽기 성공 28 줄 · 읽기 실패 2 줄` 이 나왔다
<!-- /checklist -->

5. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.
   - (가) [핵심 질문] 실행한 출력을 보고, 읽기 성공한 줄과 읽기 실패한 줄이 각각 몇 줄인지, 읽기 실패한 줄이 어떤 줄인지 적어 주세요.
   - (나) [응용] 로그 한 줄만 보고 알 수 있는 것과 알 수 없는 것을 구분해 적어 주세요. 예를 들어 203.0.113.50 의 요청에서 접속자가 누구인지, 로그인에 성공했는지는 알 수 있나요?
   - (다) [핵심 질문] 404 가 한 번 난 요청과, 같은 주소에서 `/.env` · `/wp-login.php` · `/phpmyadmin` 이 연달아 404 가 난 요청은 같은 일일까요? 샘플 로그에서 두 경우를 찾아 어떻게 다른지, 왜 한 줄만 봐서는 판단하기 어려운지 적어 주세요.

**확인** — 다시 실행했을 때 단계 1 에 `읽기 성공 28 줄 · 읽기 실패 2 줄`, 단계 3 에 `?` 가 들어간 경로 두 줄(`/board?page=2` · `/search?q=network`)이 나오면 성공입니다. 안 나오면 아래의 실습 1-1 정답 펼침과 한 줄씩 맞춰 보고, 다른 줄이 있으면 위 「직접 쓰는 곳」의 확인을 다시 봅니다.

<!-- answer: 07|실습 1-1 정답 -->

## 실습 1-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 한 줄을 세 조각으로 | `prefix, request_text, suffix = line.split('"', 2)` (`split_request`) |
| 요청에서 방법 · 경로 | `method, path, protocol = request_text.split()` (`read_request`) |
| 상태 코드를 숫자로 | `parts = suffix.split()` → `status_text = parts[0]` → `status = int(status_text)` (`read_status`) |
| 접속자 주소 | `parts = prefix.split()` → `client_ip = parts[0]` (`read_client`) |
| 깨진 줄은 읽기 실패 | `if line.count('"') < 2:` → `return None` (`parse_line`) |
| 상태 코드 큰 구분 | 2 성공 · 3 이동 · 4 요청한 쪽 문제 · 5 서버 문제 |

---
