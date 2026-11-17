---
id: m4-u01-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/096_day01_pm_log_basics.md
  mission_id: GichanSource.m4-1102-pm-log-basics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답을 읽는 방법

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

---

## 실습 1-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise1-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise1-1_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 다섯 함수입니다.

① `split_request` 안

```python
    prefix, request_text, suffix = line.split('"', 2)  # 큰따옴표 두 개를 기준으로 앞 · 요청 · 뒤 세 조각으로 나눈다
```

② `read_request` 안

```python
    method, path, protocol = request_text.split()  # 공백 기준으로 나눈 세 값을 세 이름에 한꺼번에 담는다
```

③ `read_status` 안

```python
    parts = suffix.split()     # 공백 기준으로 나눈 조각 리스트를 만든다
    status_text = parts[0]     # 첫 조각이 상태 코드 문자열이다
    status = int(status_text)  # 숫자로 바꿔야 400 이상인지 비교할 수 있다
```

④ `read_client` 안

```python
    parts = prefix.split()  # 공백 기준으로 나눈 조각 리스트를 만든다
    client_ip = parts[0]    # 첫 조각이 접속자 주소이다
```

⑤ `parse_line` 안(`if` 줄 하나)

```python
    if line.count('"') < 2:  # 큰따옴표가 두 개보다 적은 줄이면(잘렸거나 깨진 줄이면)
```

**결과**

- (가) 출력은 다음과 같고, 읽기 성공은 <mark>**28**</mark>줄, 읽기 실패는 <mark>**2**</mark>줄입니다.
  - 읽기 실패한 두 줄은 `GET /board/5 HTTP/1.1` 에서 잘린 줄과 `-` 하나만 있는 줄입니다. 큰따옴표가 두 개보다 적어서 읽지 못했습니다.

```
--- 단계 1: 로그 파일 읽기 - 전체 30 줄
읽기 성공 28 줄 · 읽기 실패 2 줄
--- 단계 2: 로그 첫 3줄을 읽은 결과
{'ip': '198.51.100.21', 'method': 'GET', 'path': '/', 'status': 200}
{'ip': '198.51.100.21', 'method': 'GET', 'path': '/static/app.css', 'status': 200}
{'ip': '198.51.100.34', 'method': 'GET', 'path': '/login', 'status': 200}
--- 단계 3: 값이 덧붙은 요청 (경로에 ? 포함)
192.0.2.15 /board?page=2
192.0.2.15 /search?q=network
```

- (나) 로그 한 줄만 보고 알 수 있는 것과 알 수 없는 것은 다음과 같습니다.
  - 알 수 있는 것: 접속자 주소(`203.0.113.50`), 시각, 요청한 방법과 경로, 결과 코드(401), 요청을 보낸 프로그램(`python-requests`).
  - 알 수 없는 것: 접속자가 **누구인지**(사용자 계정 이름이 로그에 없습니다. 같은 주소를 여러 사람이 쓸 수도 있습니다), 로그인 **시도한 계정**, 시도가 **성공했는지**의 확정.
  - 401 이 나온 줄은 로그인 실패로 짐작할 수 있지만, <mark>성공 여부는 그다음 줄들(같은 주소에서 302 가 나왔는지)을 함께 봐야 합니다.</mark>
- (다) <mark>두 경우는 같은 일이 아닙니다.</mark>
  - 198.51.100.21 의 `GET /board/99` 404 는 글이 없거나 주소를 잘못 친 한 번의 오류일 수 있습니다.
  - 198.51.100.90 은 1초 간격으로 `/.env` · `/wp-login.php` · `/phpmyadmin` 을 연달아 요청했고, 모두 404 가 났습니다.
    - 이 세 주소는 서버 설정 파일이나 관리 화면이 있을 때 자주 확인하는 주소입니다(`.env` 는 비밀 설정 파일, `wp-login.php` 는 워드프레스 사이트의 관리자 로그인 화면, `phpmyadmin` 은 데이터베이스 관리 화면의 흔한 주소입니다).
    - 이 서버에는 없어서 404 가 났습니다. 도구(`curl`)로 서버에 무엇이 있는지 차례로 확인하는 탐색으로 볼 수 있습니다.
  - 한 줄만 보면 둘 다 「404」일 뿐이라 구분할 수 없습니다. **같은 주소에서 시간순으로 여러 줄을 묶어 봐야** 반복과 패턴이 보입니다. 이것이 상관분석의 출발점입니다.

**왜**

- <mark>로그는 문자열이라 분석하려면 값으로 나눠야 합니다.</mark>
  - 큰따옴표 안에 요청이 있다는 로그의 약속된 모양을 이용해서, 복잡한 도구 없이 `split` 만으로도 읽을 수 있습니다.
  - 상태 코드는 숫자로 바꿔야 400 이상인지 비교할 수 있습니다.

**자주 틀리는 곳**

- `split_request` 에서 <mark>나눌 횟수 `2` 를 빼고 `line.split('"')` 로 쓰면</mark>, 큰따옴표 여섯 개로 일곱 조각이 되어 세 이름에 담을 수 없습니다.
  - 실행하면 다음 오류가 납니다(<mark>`too many values to unpack`</mark> 이면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise1-1_run.py", line 10, in <module>
    entry = parse_line(line)  # 한 줄을 읽어 딕셔너리로 바꾼다
  File "…/anomaly_detection/log_parse.py", line 43, in parse_line
    prefix, request_text, suffix = split_request(line)  # 세 조각으로 나눈다
  File "…/anomaly_detection/log_parse.py", line 5, in split_request
    prefix, request_text, suffix = line.split('"')  # 큰따옴표 두 개를 기준으로 앞 · 요청 · 뒤 세 조각으로 나눈다
ValueError: too many values to unpack (expected 3)
```

  - 줄 번호는 사람마다 다릅니다.
- `read_status` 에서 `int(…)` 를 빼먹으면 실습 1-1 출력은 `'status': '401'` 처럼 <mark>따옴표가 붙은 문자열로 나오고 오류는 나지 않습니다.</mark> 실습 1-2에서 `400` 과 비교할 때 비로소 `TypeError` 가 납니다.

**관제에서는**

- 로그 분석 도구는 먼저 한 줄을 부분으로 나누고, 읽지 못한 줄은 개수를 세어 따로 봅니다. <mark>읽지 못한 줄이 갑자기 늘면 로그 형식이 바뀌었거나 수집이 깨졌다는 신호입니다.</mark>

---

## 실습 1-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise1-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise1-2_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `is_suspicious` 안

```python
    bad_status = entry["status"] in SUSPICIOUS_STATUS  # 상태 코드가 401 이나 403 인지(True 또는 False)
    admin_path = "/admin" in entry["path"]             # 경로에 /admin 이 들어 있는지(True 또는 False)
    return bad_status or admin_path                    # 둘 중 하나라도 참이면 True 를 리턴한다
```

② `is_error` 안

```python
    return entry["status"] >= 400  # 400 이상이면 True 를 리턴한다
```

③ `classify_line` 안(미리 채운 `return "정상"` 앞)

```python
    if is_suspicious(entry):  # 의심 조건에 맞으면
        return "의심"         # 의심으로 가른다
    if is_error(entry):       # 의심은 아니지만 오류 조건에 맞으면
        return "오류"         # 오류로 가른다
```

**결과**

- (가) 출력은 다음과 같고, 정상 <mark>**15**</mark>, 오류 <mark>**5**</mark>, 의심 <mark>**8**</mark> 입니다.
  - 의심 8개 중 같은 주소에서 반복된 것은 203.0.113.50 의 `POST /login` 401 이 **5번**과, 같은 주소의 `/admin` · `/admin/users` 403 이 2번입니다. 198.51.100.77 의 `/admin` 403 은 한 번뿐입니다.

```
--- 단계 1: 분류별 요청 수 - 전체 28 개
정상 15 · 오류 5 · 의심 8
--- 단계 2: 의심으로 분류한 요청
203.0.113.50 POST /login 401
203.0.113.50 POST /login 401
203.0.113.50 POST /login 401
203.0.113.50 POST /login 401
203.0.113.50 POST /login 401
203.0.113.50 GET /admin 403
203.0.113.50 GET /admin/users 403
198.51.100.77 GET /admin 403
--- 단계 3: 오류로 분류한 요청
198.51.100.90 GET /.env 404
198.51.100.90 GET /wp-login.php 404
198.51.100.90 GET /phpmyadmin 404
198.51.100.21 GET /board/99 404
198.51.100.34 GET /report 500
```

- (나) 놓친 예 두 가지는 다음과 같습니다.
  - 203.0.113.50 이 401 을 5번 받은 **뒤에** `POST /login` 302 가 나온 줄은 「정상」입니다. 상태 코드만 보면 정상 이동이지만, <mark>연속 실패 뒤의 성공이라 로그인에 성공했을 수 있어 가장 먼저 봐야 합니다.</mark> 규칙이 줄 하나만 보기 때문에 놓쳤습니다.
  - 198.51.100.90 의 `/.env` · `/wp-login.php` · `/phpmyadmin` 은 「오류」(404)입니다. 한 줄씩 보면 흔한 404 이지만, 1초 간격으로 연속해서 서버에 무엇이 있는지 확인하는 탐색입니다. <mark>규칙이 같은 주소의 반복을 보지 못했습니다.</mark>
  - 그 밖에 파일 크기, 시각, 요청 도구(`python-requests`, `curl`)도 보지 않아 사람이 보면 의심스러운 단서를 쓰지 못합니다. <mark>이런 것을 놓치는 것이 미탐입니다.</mark>
- (다) 한 예: <mark>② 클라우드(SaaS) 또는 ④ 관리형 보안관제 서비스를 고릅니다.</mark>
  - 보안 전담이 1명이면 직접 운영하기 어렵습니다. 서비스 대부분이 클라우드에 있으면 로그도 클라우드에 있어서, 클라우드 방식의 SIEM(심)이 로그를 모으기 쉽습니다. 예를 들어 Microsoft Sentinel 처럼 설치 없이 쓰는 제품입니다.
  - 24시간 감시가 필요하면 ④로 외부 업체에 맡기는 것도 방법입니다.
  - 맞지 않는 방식 예: ① 설치형은 장비 구입과 운영을 1명이 감당하기 어렵습니다. ⑤ 오픈소스 직접 구축은 저장소와 규칙 관리를 모두 직접 해야 해서 1명에게 부담이 큽니다.
  - 이유가 로그 양 · 인력 · 데이터 위치에 닿아 있으면 다른 방식을 골라도 맞습니다.

**왜**

- <mark>하루 수만 줄을 사람이 다 볼 수 없으니 단순한 규칙으로 1차로 가르고 의심만 먼저 조사합니다.</mark>
  - 의심을 오류보다 먼저 확인하는 이유는, 401 · 403 은 400 이상이기도 해서 순서가 바뀌면 로그인 실패가 오류로 분류되어 의심에서 빠지기 때문입니다.
  - 규칙은 단순할수록 놓치는 것이 많아서, Unit 2 이후 같은 주소의 반복과 시간 간격을 보는 규칙을 더합니다.

**자주 틀리는 곳**

- `classify_line` 에서 `is_error` 를 `is_suspicious` 보다 먼저 확인하면, <mark>401 · 403 이 모두 「오류」가 됩니다.</mark> 오류는 나지 않고 숫자만 달라집니다.
  - 실행하면 다음처럼 됩니다(의심이 0개이고 오류가 13개이면 이 실수입니다).

```
--- 단계 1: 분류별 요청 수 - 전체 28 개
정상 15 · 오류 13 · 의심 0
```

- `read_status` 에서 `int(…)` 를 빼먹으면 `is_error` 에서 <mark>`400` 과 문자열을 비교하게 되어 다음 오류가 납니다.</mark>

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise1-2_run.py", line 23, in <module>
    labeled = label_entries(entries)  # 요청마다 분류를 적는다
  File "…/anomaly_detection/log_classify.py", line 38, in label_entries
    item["group"] = classify_line(entry)  # 분류를 복사본에 적는다
  File "…/anomaly_detection/log_classify.py", line 26, in classify_line
    if is_error(entry):  # 의심은 아니지만 오류 조건에 맞으면
  File "…/anomaly_detection/log_classify.py", line 17, in is_error
    return entry["status"] >= 400  # 400 이상이면 True 를 리턴한다
TypeError: '>=' not supported between instances of 'str' and 'int'
```

  - 줄 번호는 사람마다 다릅니다. `TypeError` 가 같으면 이 실수입니다.

**관제에서는**

- SIEM(심)의 탐지 규칙은 처음에는 이렇게 단순하게 시작해서 오탐과 미탐을 보며 고칩니다. <mark>규칙을 많이 만들수록 오탐도 늘어서 담당자가 경고를 무시하게 될 수 있습니다.</mark>
  - 경고는 공격이라는 뜻이 아니라 「먼저 살펴볼 곳」입니다.

---

## 정답 마무리

 **터미널에 입력합니다.**

```bash
cd ..
pwd
git status
```
- 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 있는 폴더의 위치 확인 · `git status` 올릴 파일의 상태를 봄

`.env` 나 `.venv` 가 없는 것을 확인한 뒤에 아래를 칩니다.

```bash
git add .
git commit -m "Add access control and anomaly detection unit 1"
git push
```
- 명령 풀이: `git add .` 바뀐 파일을 올릴 대상에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림

**결과**

- (가) 한 예: 「`.env` · `.venv` 는 보이지 않았다」. 보였다면 `.gitignore` 에 `.env`(또는 `.venv`) 한 줄을 적고 저장한 뒤 `git status` 를 다시 쳤다고 적습니다.

**왜**

- <mark>올리기 전에 올라갈 파일을 확인해야 비밀 키가 섞이지 않습니다.</mark>
  - 새 Module 폴더는 처음 올리는 것이라 `anomaly_detection/` 한 줄로 보일 수 있습니다.

**자주 틀리는 곳**

- <mark>`.env` 가 보이는데 그대로 `git add .` 를 하는 실수가 가장 위험합니다.</mark>
  - `cd ..` 를 두 번 쳐서 `security-agent-toolkit` 바깥으로 나가는 경우도 있습니다. `pwd` 로 확인합니다.

**관제에서는**

- 분석 코드와 샘플 로그는 같은 저장소에 함께 남겨, <mark>어느 코드로 어떤 로그를 분석했는지 이력으로 추적합니다.</mark>

---

## 앞 실습 파일 완성본

앞 실습 파일이 없거나 잘 안 될 때 이 코드로 만듭니다. 샘플 로그는 「시작하기」 6번의 내용입니다.

**`log_parse.py`** (실습 1-1 완성본)

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
    요청이 성공했는지 실패했는지 가를 때 쓴다.
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
