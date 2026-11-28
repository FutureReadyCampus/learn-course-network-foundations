---
id: m4-u02-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/098_day02_am_normalize.md
  mission_id: GichanSource.m4-1103-am-normalize
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답을 읽는 방법

<mark>설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.</mark>

---

## 실습 2-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise2-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-1_run.py` 파이썬으로 실행 파일 실행

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 두 함수입니다.

① `convert_time` 안

```python
    parsed = datetime.strptime(time_text, NGINX_TIME_FORMAT)  # 문자열을 시각 값으로 바꾼다(시간대 +0900 포함)
    local_time = parsed.replace(tzinfo=None)                  # 시간대 정보를 지우고 한국 시각만 남긴다
    time_out = local_time.strftime(COMMON_TIME_FORMAT)        # 공통 모양의 문자열로 바꾼다
```

② `convert_result` 안

```python
    if status >= 400:  # 400 이상이면 요청이 실패한 것이다
        return "실패"  # 실패를 리턴한다
    return "성공"      # 그 밖에는 성공을 리턴한다
```

<h2>결과</h2>

- (가) 출력은 다음과 같고, 정규화한 이벤트는 <mark>**28개**</mark>, 읽기 실패는 <mark>**2줄**</mark>, 결과는 성공 <mark>**15**</mark> · 실패 <mark>**13**</mark> 입니다.

```
--- 단계 1: 정규화한 이벤트 28 개 · 읽기 실패 2 줄
{'time': '2026-11-02 09:01:05', 'source': 'web', 'user': None, 'ip': '198.51.100.21', 'action': 'GET /', 'result': '성공', 'raw': '198.51.100.21 - - [02/Nov/2026:09:01:05 +0900] "GET / HTTP/1.1" 200 1204 "-" "Mozilla/5.0"'}
--- 단계 2: 처음 나오는 실패 이벤트
{'time': '2026-11-02 09:12:03', 'source': 'web', 'user': None, 'ip': '203.0.113.50', 'action': 'POST /login', 'result': '실패', 'raw': '203.0.113.50 - - [02/Nov/2026:09:12:03 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"'}
--- 단계 3: 성공 · 실패별 이벤트 수
{'성공': 15, '실패': 13}
```

- (나) 시각을 `02/Nov/2026:09:00:00 +0900` 같은 모양 그대로 문자열로 정렬하면 <mark>시간 순서가 틀립니다.</mark>
  - 문자열은 앞 문자부터 차례로 비교하므로, 맨 앞이 일(`02`, `01`)입니다. <mark>12월 1일(`01/Dec/…`)이 11월 2일(`02/Nov/…`)보다 앞에 놓입니다.</mark>
  - 공통 모양 `2026-11-02 09:00:00` 은 연 · 월 · 일 · 시 · 분 · 초 순서라서, <mark>문자열 순서가 곧 시간 순서입니다.</mark>
  - 아래 코드로 확인할 수 있습니다.

```python
december_first = "01/Dec/2026:09:00:00 +0900"   # nginx 모양의 12월 1일 시각
november_second = "02/Nov/2026:09:00:00 +0900"  # nginx 모양의 11월 2일 시각
print(december_first < november_second)         # 문자열 순서로 12월 1일이 앞인지 비교한다
common_december = "2026-12-01 09:00:00"         # 공통 모양의 12월 1일 시각
common_november = "2026-11-02 09:00:00"         # 공통 모양의 11월 2일 시각
print(common_december < common_november)        # 문자열 순서로 12월 1일이 앞인지 비교한다
```

실행 결과:

```
True
False
```

- (다) `raw` 는 <mark>정규화 코드가 틀렸는지 확인하고 알림의 근거를 보여 주기 위해 남깁니다.</mark>
  - 정규화는 원래 정보 일부를 바꾸거나 버립니다(예: 상태 코드 `401` 이 `실패` 로 바뀌면 어떤 오류였는지 사라집니다). <mark>원래 줄이 있으면 `401` 이었는지 `500` 이었는지 다시 볼 수 있습니다.</mark>
  - 정규화 결과가 이상할 때 원본과 비교해 어디서 틀렸는지 찾을 수 있습니다.

<h2>왜</h2>

- <mark>모양이 다른 시각은 나란히 놓을 수도 정렬할 수도 없습니다.</mark> 하나의 모양으로 맞추면 이후 모든 단계가 같은 기준을 씁니다.
  - 성공 · 실패도 `401` · `true` · `success` 를 `실패` / `성공` 두 가지로 줄이면 규칙을 한 번만 만듭니다.

<h2>자주 틀리는 곳</h2>

- `strptime` 에 nginx 형식(`NGINX_TIME_FORMAT`) 대신 공통 형식(`COMMON_TIME_FORMAT`)을 넣으면 문자열 모양과 형식이 달라 `ValueError` 오류가 납니다. <mark>두 형식 이름을 헷갈리지 않습니다.</mark>
  - 실행하면 다음 오류가 납니다(<mark>`does not match format`</mark> 이면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise2-1_run.py", line 7, in <module>
    event = normalize_web(line)  # 한 줄을 공통 이벤트로 바꾼다
  File "…/anomaly_detection/normalize_web.py", line 57, in normalize_web
    time_out = convert_time(time_text)  # 공통 모양의 시각으로 바꾼다
  File "…/anomaly_detection/normalize_web.py", line 25, in convert_time
    parsed = datetime.strptime(time_text, COMMON_TIME_FORMAT)  # 문자열을 시각 값으로 바꾼다(시간대 +0900 포함)
ValueError: time data '02/Nov/2026:09:01:05 +0900' does not match format '%Y-%m-%d %H:%M:%S'
```

  - 줄 번호는 사람마다 다릅니다.
- `replace(tzinfo=None)` 를 빼도 오류는 나지 않고 `strftime` 결과도 같습니다. <mark>이 수업에서는 세 로그의 시각 값을 같은 종류(시간대 없음)로 맞춰 두려고 지웁니다.</mark>

<h2>관제에서는</h2>

- 로그 수집 도구의 파서 설정은 시각 형식을 직접 적습니다. 로그 형식이 바뀌면 파서가 읽지 못하고, <mark>읽지 못한 줄이 갑자기 늘면 수집에 문제가 생겼다는 신호입니다.</mark>

---

## 실습 2-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise2-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-2_run.py` 파이썬으로 실행 파일 실행

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 세 함수입니다.

① `convert_server_time` 안

```python
    parsed = datetime.strptime(time_text, SERVER_TIME_FORMAT)  # 문자열을 시각 값으로 바꾼다
    time_out = parsed.strftime(COMMON_TIME_FORMAT)             # 공통 모양의 문자열로 바꾼다(초는 00 이 된다)
```

② `normalize_server` 안(`allowed` 를 꺼낸 줄 아래)

```python
    result = ALLOWED_MAP[allowed]  # True 면 "성공", False 면 "실패"
```

③ `normalize_saas` 안

```python
    account_parts = row["account"].split("@")  # 메일 주소를 @ 앞뒤로 나눈다
    user = account_parts[0]                    # @ 앞이 사용자 이름이다
    result = RESULT_MAP[outcome]               # success 면 "성공", failure 면 "실패"
```

<h2>결과</h2>

- (가) 출력은 다음과 같고, 판정 서버 이벤트는 <mark>**15개**</mark>(성공 6 · 실패 9), SaaS 이벤트는 <mark>**14개**</mark>(성공 13 · 실패 1)입니다.

```
--- 단계 1: 판정 서버 이벤트 15 개
{'성공': 6, '실패': 9}
--- 단계 2: SaaS 이벤트 14 개
{'실패': 1, '성공': 13}
--- 단계 3: 각 로그의 첫 이벤트
{'time': '2026-11-02 09:40:00', 'source': 'server', 'user': 'seoyeon', 'ip': None, 'action': 'SALES:QUERY', 'result': '성공', 'raw': '{"time": "2026-11-02T09:40", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}'}
{'time': '2026-11-02 02:14:08', 'source': 'saas', 'user': 'jiwoo', 'ip': '203.0.113.80', 'action': 'login', 'result': '실패', 'raw': {'time': '2026-11-02 02:14:08', 'account': 'jiwoo@a-corp.example', 'event': 'login', 'ip_address': '203.0.113.80', 'outcome': 'failure'}}
```

- (나) 판정 서버 로그에는 접속 주소가 원래 없기 때문에 <mark>`ip` 를 `None` 으로 둡니다.</mark>
  - 임의의 주소(예: `0.0.0.0`)를 채우면 이후 주소별로 셀 때 그 가짜 주소가 이벤트 15개를 가진 주소로 세어집니다.
  - 그러면 없는 주소에서 15번 요청이 온 것처럼 보이는 잘못된 분석이 됩니다. <mark>없다는 사실 자체를 `None` 으로 남겨야 이후 코드가 「이 이벤트는 주소가 없다」고 판단할 수 있습니다.</mark>
- (다) 정규화하면 비교하기 쉬워지는 대신 로그 종류만 갖고 있던 정보 일부가 공통 이벤트의 키에 들어가지 않습니다.
  - 판정 서버 로그의 <mark>`reason`(거부 이유)과 `network`(접속 위치)는 공통 이벤트의 키에 없습니다.</mark>
  - <mark>잃은 정보는 `raw` 에 그대로 있으므로 필요할 때 원래 줄에서 찾습니다.</mark> 그래서 `raw` 를 남깁니다.

<h2>왜</h2>

- <mark>로그마다 사용자 · 결과를 다르게 적기 때문에, 공통 이벤트로 바꿔야 같은 규칙으로 셀 수 있습니다.</mark>
  - 값을 바꾸는 딕셔너리(`ALLOWED_MAP` · `RESULT_MAP`)를 쓰면 바꾸는 규칙이 한곳에 모이고, 예상 못 한 값이 오면 `KeyError` 로 바로 드러납니다.

<h2>자주 틀리는 곳</h2>

- `account_parts[0]` 대신 `account_parts[1]` 을 쓰면 사용자 이름이 아니라 `a-corp.example` 이 나옵니다. <mark>`@` 앞이 이름입니다.</mark>
- 판정 서버의 `allowed` 를 바꿀 때 **`ALLOWED_MAP` 대신 `RESULT_MAP` 을 쓰면 `KeyError: True` 오류가 납니다.** 두 딕셔너리는 키가 다릅니다(`True` · `False` 와 `"success"` · `"failure"`).
  - 실행하면 다음 오류가 납니다(<mark>`KeyError: True`</mark> 이면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise2-2_run.py", line 3, in <module>
    server_events = load_server("server_log.jsonl")  # 판정 서버 로그를 공통 이벤트로 바꾼다
  File "…/anomaly_detection/normalize_json_csv.py", line 78, in load_server
    event = normalize_server(line)  # 공통 이벤트로 바꾼다
  File "…/anomaly_detection/normalize_json_csv.py", line 33, in normalize_server
    result = RESULT_MAP[allowed]  # True 면 "성공", False 면 "실패"
KeyError: True
```

  - 줄 번호는 사람마다 다릅니다.

<h2>관제에서는</h2>

- 로그 종류가 새로 늘 때는 파서 하나를 더 만들고 같은 공통 이벤트를 리턴하게 합니다. <mark>탐지 규칙은 고치지 않습니다.</mark>

---

## 실습 2-3 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise2-3_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise2-3_run.py` 파이썬으로 실행 파일 실행

<h2>채운 코드 (한 예)</h2>

직접 쓰는 곳은 세 함수입니다.

① `merge_events` 안

```python
    events = web + server + saas  # 리스트 세 개를 이어 붙여 하나로 만든다
    events.sort(key=get_time)     # time 이 이른 것부터(오름차순, = 시간순) 정렬한다
```

② `count_by_source` 안(`for` 안쪽)

```python
        source = event["source"]                                              # 이 이벤트의 소스
        source_event_counts[source] = source_event_counts.get(source, 0) + 1  # 그 소스의 횟수를 1 늘린다
```

③ `save_events` 안(`with` 안쪽)

```python
        json.dump(events, events_file, ensure_ascii=False, indent=2)  # 한글은 그대로, 들여쓰기를 해서 저장한다
```

<h2>결과</h2>

- (가) 출력은 다음과 같고, 소스별 이벤트는 web <mark>**28**</mark> · server <mark>**15**</mark> · saas <mark>**14**</mark>, `user` 가 비어 있는 이벤트는 <mark>**28개**</mark>, `ip` 가 비어 있는 이벤트는 <mark>**15개**</mark>, 저장된 이벤트는 <mark>**57개**</mark>입니다.

```
--- 단계 1: 소스별 이벤트 수
{'saas': 14, 'web': 28, 'server': 15}
--- 단계 2: user · ip 가 None 인 이벤트 수
user 가 비어 있는 이벤트 28 개
ip 가 비어 있는 이벤트 15 개
--- 단계 3: gaeun 의 이벤트를 시간순으로
2026-11-02 10:05:00 server ACCOUNT:CHANGE 실패
2026-11-02 10:09:00 server ACCOUNT:CHANGE 실패
2026-11-02 10:12:55 saas login 성공
2026-11-02 10:14:00 server ACCOUNT:CHANGE 실패
2026-11-02 16:10:00 server SALES:QUERY 성공
--- 단계 4: 저장한 파일 normalized_events.json
저장된 이벤트 57 개
```

- (나) gaeun 의 이벤트를 시간순으로 놓으면 <mark>판정 서버와 SaaS 의 일이 번갈아 나옵니다.</mark>
  - 10:05 · 10:09 판정 서버에서 `ACCOUNT:CHANGE` 가 실패하고, 10:12 SaaS 에 로그인이 성공하고, 10:14 판정 서버에서 다시 실패합니다.
  - 정규화 전에는 판정 서버 로그와 SaaS 로그를 따로 열어야 해서 이 순서를 한 번에 볼 수 없습니다.
  - <mark>이 순서만으로 원인을 알 수는 없습니다.</mark> 같은 사용자가 두 곳에서 어떤 일을 했는지 함께 확인할 단서가 생겼다고 보면 됩니다.
- (다) `user` 가 비어 있는 이벤트 28개는 <mark>웹 서버 이벤트 전부입니다.</mark> 웹 서버 로그에는 사용자 이름이 원래 없기 때문입니다.
  - 사용자 이름으로 세거나 묶는 분석을 하면 <mark>이 28개는 어느 사용자에도 들어가지 못하고 빠집니다.</mark>
  - 그래서 사용자별 숫자만 보면 웹 서버에서 난 일을 놓칩니다. Unit 3에서 판다스로 직접 확인합니다.

<h2>왜</h2>

- <mark>로그가 시간순으로 함께 보이면 여러 로그에 걸친 같은 계정의 일이 보입니다.</mark>
  - 시간순 정렬은 `time` 문자열이 연 · 월 · 일 · 시 · 분 · 초 순서라서 문자열 정렬만으로 됩니다.

<h2>자주 틀리는 곳</h2>

- **`events = events.sort(key=get_time)` 처럼 `sort` 의 결과를 변수에 담으면 `events` 가 `None` 이 되어 다음 줄에서 오류가 납니다.** `sort` 는 리스트 자체를 바꾸고 아무것도 리턴하지 않습니다.
  - 실행하면 다음 오류가 납니다(<mark>`'NoneType'`</mark> 이 들어간 오류이면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise2-3_run.py", line 24, in <module>
    source_event_counts = count_by_source(events)  # 소스별 개수를 센다
  File "…/anomaly_detection/normalize.py", line 45, in count_by_source
    for event in events:  # 이벤트를 하나씩 꺼낸다
TypeError: 'NoneType' object is not iterable
```

  - 줄 번호는 사람마다 다릅니다.
- `json.dump` 에서 `ensure_ascii=False` 를 빼면 **오류는 나지 않지만 한글이 `\uc131\uacf5` 같은 코드로 저장됩니다.**

<h2>관제에서는</h2>

- <mark>정규화된 이벤트를 한곳에 모으는 것이 SIEM(심)의 수집 · 정규화 단계의 결과입니다.</mark> 이 저장소를 기준으로 탐지 규칙과 조사가 이어집니다.
  - 값이 비어 있는 이벤트 수는 <mark>분석에서 빠지는 이벤트가 얼마나 되는지 알려 주는 품질 점검입니다.</mark>

---

## 정답 마무리

 **터미널에 입력합니다.**

```bash
pwd
ls
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기

<h2>결과</h2>

- <mark>이번 Unit에서 만든 파일 아홉 개와 `report_u2.md` 가 보여야 합니다.</mark> 깃허브에 올리는 일은 Unit 3의 실습 3-2 마지막에 합니다.

---

## 앞 Unit 파일 완성본

Unit 1의 파일이 없거나 잘 안 될 때 이 코드로 만듭니다. <mark>`anomaly_detection` 폴더 바로 아래에 같은 이름으로 만듭니다.</mark>

**`log_parse.py`** (Unit 1의 실습 1-1 완성본)

```python
def split_request(line):                                # 로그 한 줄(문자열)을 받는 함수
    """로그 한 줄을 큰따옴표 기준으로 앞 · 요청 · 뒤 세 조각으로 나눈다.
    나뉘지 않은 하나의 문자열인 로그에서 값을 꺼내기 시작할 때 쓴다.
    """
    prefix, request_text, suffix = line.split('"', 2)   # 큰따옴표 두 개를 기준으로 앞 · 요청 · 뒤 세 조각으로 나눈다
    return prefix, request_text, suffix                 # 세 조각을 리턴한다


def read_request(request_text):                         # 요청 조각(예: GET /login HTTP/1.1)을 받는 함수
    """요청 조각에서 방법(method)과 경로(path)를 꺼낸다.
    무엇을 요청했는지 알고 싶을 때 쓴다.
    """
    method, path, protocol = request_text.split()       # 공백 기준으로 나눈 세 값을 세 이름에 한꺼번에 담는다
    return method, path                                 # 방법과 경로를 리턴한다


def read_status(suffix):                                # 요청 뒤 조각(예:  401 312 "-" "Mozilla/5.0")을 받는 함수
    """요청 뒤 조각에서 상태 코드를 꺼내 정수로 리턴한다.
    요청이 성공했는지 실패했는지 판정할 때 쓴다.
    """
    parts = suffix.split()                              # 공백 기준으로 나눈 조각 리스트를 만든다
    status_text = parts[0]                              # 첫 조각이 상태 코드 문자열이다
    status = int(status_text)                           # 숫자로 바꿔야 400 이상인지 비교할 수 있다
    return status                                       # 상태 코드(정수)를 리턴한다


def read_client(prefix):                                # 요청 앞 조각(예: 203.0.113.50 - - [02/Nov/2026:09:12:03 +0900] )을 받는 함수
    """요청 앞 조각에서 접속자 주소를 꺼낸다.
    어느 주소가 요청했는지 알고 싶을 때 쓴다.
    """
    parts = prefix.split()                              # 공백 기준으로 나눈 조각 리스트를 만든다
    client_ip = parts[0]                                # 첫 조각이 접속자 주소이다
    return client_ip                                    # 접속자 주소를 리턴한다


def parse_line(line):                                   # 로그 한 줄을 받는 함수
    """로그 한 줄을 ip · method · path · status 딕셔너리로 바꾼다.
    깨진 줄이면 None 을 리턴한다.
    접속 로그를 분석하기 전에 한 줄을 값으로 나눌 때 쓴다.
    """
    if line.count('"') < 2:                             # 큰따옴표가 두 개보다 적은 줄이면(잘렸거나 깨진 줄이면)
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
```

**`access_sample.log`** (Unit 1 시작하기 5번의 샘플 로그, 30줄) — 끝이 잘린 줄과 마지막 줄의 `-` 는 <mark>일부러 형식을 틀리게 만든 줄이니 지우지 않습니다</mark>.

```
198.51.100.21 - - [02/Nov/2026:09:01:05 +0900] "GET / HTTP/1.1" 200 1204 "-" "Mozilla/5.0"
198.51.100.21 - - [02/Nov/2026:09:01:06 +0900] "GET /static/app.css HTTP/1.1" 200 3120 "-" "Mozilla/5.0"
198.51.100.34 - - [02/Nov/2026:09:03:47 +0900] "GET /login HTTP/1.1" 200 1830 "-" "Mozilla/5.0"
198.51.100.34 - - [02/Nov/2026:09:03:59 +0900] "POST /login HTTP/1.1" 302 0 "-" "Mozilla/5.0"
198.51.100.34 - - [02/Nov/2026:09:04:00 +0900] "GET /board HTTP/1.1" 200 5410 "-" "Mozilla/5.0"
192.0.2.15 - - [02/Nov/2026:09:05:21 +0900] "GET /board?page=2 HTTP/1.1" 200 5322 "-" "Mozilla/5.0"
192.0.2.15 - - [02/Nov/2026:09:05:40 +0900] "GET /board/12 HTTP/1.1" 200 2210 "-" "Mozilla/5.0"
203.0.113.50 - - [02/Nov/2026:09:12:01 +0900] "GET /login HTTP/1.1" 200 1830 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:03 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:06 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:09 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:12 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:15 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:18 +0900] "POST /login HTTP/1.1" 302 0 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:25 +0900] "GET /admin HTTP/1.1" 403 287 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:27 +0900] "GET /admin/users HTTP/1.1" 403 287 "-" "python-requests/2.31.0"
198.51.100.90 - - [02/Nov/2026:09:20:10 +0900] "GET /.env HTTP/1.1" 404 153 "-" "curl/8.4.0"
198.51.100.90 - - [02/Nov/2026:09:20:11 +0900] "GET /wp-login.php HTTP/1.1" 404 153 "-" "curl/8.4.0"
198.51.100.90 - - [02/Nov/2026:09:20:12 +0900] "GET /phpmyadmin HTTP/1.1" 404 153 "-" "curl/8.4.0"
198.51.100.21 - - [02/Nov/2026:09:22:30 +0900] "GET /board/99 HTTP/1.1" 404 153 "-" "Mozilla/5.0"
198.51.100.34 - - [02/Nov/2026:09:25:02 +0900] "GET /report HTTP/1.1" 500 177 "-" "Mozilla/5.0"
192.0.2.15 - - [02/Nov/2026:09:26:44 +0900] "GET /search?q=network HTTP/1.1" 200 4010 "-" "Mozilla/5.0"
192.0.2.88 - - [02/Nov/2026:09:28:13 +0900] "GET / HTTP/1.1" 200 1204 "-" "Mozilla/5.0"
192.0.2.88 - - [02/Nov/2026:09:28:20 +0900] "GET /board HTTP/1.1" 200 5410 "-" "Mozilla/5.0"
198.51.100.21 - - [02/Nov/2026:09:31:15 +0900] "GET /board HTTP/1.1" 301 169 "-" "Mozilla/5.0"
198.51.100.21 - - [02/Nov/2026:09:31:40 +0900] "GET /board/5 HTTP/1.1
198.51.100.77 - - [02/Nov/2026:09:33:51 +0900] "GET /admin HTTP/1.1" 403 287 "-" "Mozilla/5.0"
192.0.2.88 - - [02/Nov/2026:09:35:02 +0900] "GET /logout HTTP/1.1" 302 0 "-" "Mozilla/5.0"
198.51.100.21 - - [02/Nov/2026:09:36:10 +0900] "GET /board/12 HTTP/1.1" 200 2210 "-" "Mozilla/5.0"
-
```
