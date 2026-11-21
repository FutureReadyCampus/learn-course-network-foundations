---
id: m4-u01-l07
title: 정답
render: markdown
---

# 정답

## 정답을 보는 방법

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

1. **핵심 실습**: 실습 1-1 · 1-2 정답입니다. 오늘 모두가 하는 실습이니 먼저 맞춰 봅니다.
2. **응용(여유가 되면)**: 응용 1-1 ~ 1-3 정답입니다. 여유가 되면 해 보세요. 응용을 한 사람만 봅니다.
3. 정답마다 채운 코드, 결과, 왜, 자주 틀리는 곳, 관제에서는 순서로 읽습니다.

---

## 실습 1-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise1-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise1-1_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 곳(① · ②)입니다.

① `split_request` 안

```python
    # ① line 을 큰따옴표(")로 두 번만 나눠 prefix, request_text, suffix 세 이름에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    prefix, request_text, suffix = line.split('"', 2)  # 큰따옴표 두 개를 기준으로 앞 · 요청 · 뒤 세 조각으로 나눈다
```

② `read_status` 안

```python
    # ② status_text 를 정수로 바꿔 status 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    status = int(status_text)  # 숫자로 바꿔야 400 이상인지 비교할 수 있다
```

- 채우기 전 출력은 `NameError: name 'prefix' is not defined`, ① 만 채우면 `NameError: name 'status' is not defined` 입니다. ② 까지 채우면 아래 출력이 나옵니다.

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

| 실수 | 나타나는 것 | 이유 |
|---|---|---|
| ① 에서 <mark>나눌 횟수 `2` 를 빼고 `line.split('"')` 로 씀</mark> | <mark>`too many values to unpack`</mark> 오류 | 큰따옴표 여섯 개로 일곱 조각이 되어 세 이름에 담을 수 없음 |
| ② 에서 `int(…)` 를 빼고 `status = status_text` 로 씀 | 실습 1-1 출력은 `'status': '401'` 처럼 <mark>따옴표가 붙은 문자열로 나오고 오류는 나지 않음</mark> | 실습 1-2 `convert_result` · 응용 1-1 `is_error` 에서 `400` 과 비교할 때 비로소 `TypeError` 가 남 |
| ① · ② 를 4칸이 아니라 줄 맨 앞(0칸)에서 씀 | `IndentationError: unexpected indent` | 함수 밖 줄이 되어 아래 `return` 이 갑자기 들여 쓴 줄이 됨 |

- `int(…)` 를 빼먹었을 때 나는 오류는 `TypeError: '>=' not supported between instances of 'str' and 'int'` 입니다.
- 나눌 횟수 `2` 를 빼고 실행하면 다음 오류가 납니다(<mark>`too many values to unpack`</mark> 이면 이 실수입니다).

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

**채운 코드** (한 예) — 직접 쓰는 곳은 두 곳(① · ②)입니다.

① `convert_time` 안

```python
    # ① local_time 을 공통 모양(COMMON_TIME_FORMAT)의 문자열로 바꿔 time_out 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    time_out = local_time.strftime(COMMON_TIME_FORMAT)        # 공통 모양의 문자열로 바꾼다
```

② `convert_result` 안

```python
    # ② status 가 400 이상이면   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    if status >= 400:  # 400 이상이면 요청이 실패한 것이다
```

- 채우기 전에는 `IndentationError: unexpected indent` 가 나오고, ① 만 채워도 같습니다. ② 만 채우고 ① 을 비우면 `NameError: name 'time_out' is not defined` 입니다. 둘 다 채우면 아래 출력이 나옵니다.

**결과**

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

**왜**

- <mark>모양이 다른 시각은 나란히 놓을 수도 정렬할 수도 없습니다.</mark> 하나의 모양으로 맞추면 이후 모든 단계가 같은 기준을 씁니다.
  - 성공 · 실패도 `401` · `true` · `success` 를 `실패` / `성공` 두 가지로 줄이면 규칙을 한 번만 만듭니다.

**자주 틀리는 곳**

| 실수 | 나타나는 것 | 이유 |
|---|---|---|
| ① 에서 <mark>`NGINX_TIME_FORMAT` 을 넣음</mark> | 오류 없이 시각이 nginx 모양 그대로 나옴 | 형식 이름을 바꿔 넣음. `%z` 자리가 비어 끝에 공백 |
| ② 끝의 `:` 를 빠뜨림 | `SyntaxError: expected ':'` | `if` 줄 끝에는 `:` 가 꼭 있어야 함 |
| ② 에서 `400` 을 `"400"` 으로 씀 | `TypeError: '>=' not supported between instances of 'int' and 'str'` | 정수와 문자열은 크기를 비교할 수 없음 |

- <mark>두 형식 이름을 헷갈리지 않습니다.</mark> `NGINX_TIME_FORMAT` 은 원래 로그의 모양이라 읽을 때(`strptime`) 쓰고, `COMMON_TIME_FORMAT` 은 공통 모양이라 만들 때(`strftime`) 씁니다. ① 에 `NGINX_TIME_FORMAT` 을 넣고 실행하면 단계 1 의 첫 이벤트가 이렇게 나옵니다.

```
{'time': '02/Nov/2026:09:01:05 ', 'source': 'web', …
```

- 단계 3 의 개수(`{'성공': 15, '실패': 13}`)는 그대로라서, 시각 모양이 정답과 같은지 단계 1 의 첫 이벤트로 꼭 확인합니다.

**관제에서는**

- 로그 수집 도구의 파서 설정은 시각 형식을 직접 적습니다. 로그 형식이 바뀌면 파서가 읽지 못하고, <mark>읽지 못한 줄이 갑자기 늘면 수집에 문제가 생겼다는 신호입니다.</mark>

---

## 응용 1-1 정답

> 여기부터는 **응용(여유가 되면)** 정답입니다. 여유가 되면 해 보세요. 핵심 실습 정답은 앞의 실습 1-1 · 1-2 정답에 있습니다.

 **터미널에 입력합니다.**

```bash
pwd
python apply1-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python apply1-1_run.py` 파이썬으로 실행 파일 실행

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
  - 규칙은 단순할수록 놓치는 것이 많아서, 다음 Unit들에서 같은 주소의 반복과 시간 간격을 보는 규칙을 더합니다.

**자주 틀리는 곳**

| 실수 | 나타나는 것 | 이유 |
|---|---|---|
| `classify_line` 에서 `is_error` 를 `is_suspicious` 보다 먼저 확인 | 오류는 나지 않고 숫자만 달라짐(의심 0개, 오류 13개) | <mark>401 · 403 이 모두 「오류」가 됩니다.</mark> |
| `read_status` 에서 `int(…)` 를 빼먹음 | `is_error` 에서 `TypeError` 오류 | <mark>`400` 과 문자열을 비교하게 됩니다.</mark> |

- 확인 순서를 바꾸고 실행하면 다음처럼 됩니다(의심이 0개이고 오류가 13개이면 이 실수입니다).

```
--- 단계 1: 분류별 요청 수 - 전체 28 개
정상 15 · 오류 13 · 의심 0
```

- `int(…)` 를 빼먹고 실행하면 다음 오류가 납니다.

```
Traceback (most recent call last):
  File "…/anomaly_detection/apply1-1_run.py", line 23, in <module>
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

## 응용 1-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python apply1-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python apply1-2_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `convert_server_time` 안

```python
    parsed = datetime.strptime(time_text, SERVER_TIME_FORMAT)  # 문자열을 시각 값으로 바꾼다
    time_out = parsed.strftime(COMMON_TIME_FORMAT)             # 공통 모양의 문자열로 바꾼다(초는 00 이 된다)
```

② `normalize_server` 안(`allowed` 를 꺼낸 줄 아래)

```python
    result = ALLOWED_MAP[allowed]  # True 면 "성공", False 면 "실패"
```

③ `normalize_saas` 안 — 5번과 6번 주석 사이에 미리 채운 `outcome = row["outcome"]` 줄이 있습니다. 세 줄을 한 번에 붙이지 말고, 아래 상자를 하나씩 해당 번호 주석 바로 아래에 붙입니다.

4번 주석 아래

```python
    account_parts = row["account"].split("@")  # 메일 주소를 @ 앞뒤로 나눈다
```

5번 주석 아래

```python
    user = account_parts[0]                    # @ 앞이 사용자 이름이다
```

6번 주석 아래(미리 채운 `outcome = row["outcome"]` 줄보다 아래)

```python
    result = RESULT_MAP[outcome]               # success 면 "성공", failure 면 "실패"
```

**결과**

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

**왜**

- <mark>로그마다 사용자 · 결과를 다르게 적기 때문에, 공통 이벤트로 바꿔야 같은 규칙으로 셀 수 있습니다.</mark>
  - 값을 바꾸는 딕셔너리(`ALLOWED_MAP` · `RESULT_MAP`)를 쓰면 바꾸는 규칙이 한곳에 모이고, 예상 못 한 값이 오면 `KeyError` 로 바로 드러납니다.

**자주 틀리는 곳**

| 실수 | 나타나는 것 | 이유 |
|---|---|---|
| `account_parts[0]` 대신 `account_parts[1]` 을 씀 | 사용자 이름이 아니라 `a-corp.example` 이 나옴 | <mark>`@` 앞이 이름입니다.</mark> |
| 판정 서버의 `allowed` 를 바꿀 때 **`ALLOWED_MAP` 대신 `RESULT_MAP` 을 씀** | **`KeyError: True` 오류** | 두 딕셔너리는 키가 다름(`True` · `False` 와 `"success"` · `"failure"`) |

- `RESULT_MAP` 을 쓰고 실행하면 다음 오류가 납니다(<mark>`KeyError: True`</mark> 이면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/apply1-2_run.py", line 3, in <module>
    server_events = load_server("server_log.jsonl")  # 판정 서버 로그를 공통 이벤트로 바꾼다
  File "…/anomaly_detection/normalize_json_csv.py", line 78, in load_server
    event = normalize_server(line)  # 공통 이벤트로 바꾼다
  File "…/anomaly_detection/normalize_json_csv.py", line 33, in normalize_server
    result = RESULT_MAP[allowed]  # True 면 "성공", False 면 "실패"
KeyError: True
```

- 줄 번호는 사람마다 다릅니다.

**관제에서는**

- 로그 종류가 새로 늘 때는 파서 하나를 더 만들고 같은 공통 이벤트를 리턴하게 합니다. <mark>탐지 규칙은 고치지 않습니다.</mark>

---

## 응용 1-3 정답

 **터미널에 입력합니다.**

```bash
pwd
python apply1-3_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python apply1-3_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

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

**결과**

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
  - 그래서 사용자별 숫자만 보면 웹 서버에서 난 일을 놓칩니다. 다음 Unit 2는 판다스로 이것을 직접 확인합니다.

**왜**

- <mark>로그가 시간순으로 함께 보이면 여러 로그에 걸친 같은 계정의 일이 보입니다.</mark>
  - 시간순 정렬은 `time` 문자열이 연 · 월 · 일 · 시 · 분 · 초 순서라서 문자열 정렬만으로 됩니다.

**자주 틀리는 곳**

| 실수 | 나타나는 것 | 이유 |
|---|---|---|
| **`sort` 의 결과를 변수에 담음** | **`events` 가 `None` 이 되어 다음 줄에서 오류가 남** | `sort` 는 리스트 자체를 바꾸고 아무것도 리턴하지 않음 |
| `json.dump` 에서 `ensure_ascii=False` 를 뺌 | **오류는 나지 않지만 한글이 `\uc131\uacf5` 같은 코드로 저장됨** | 한글을 그대로 쓰라는 설정이 빠짐 |

- `events = events.sort(key=get_time)` 처럼 쓰고 실행하면 다음 오류가 납니다(<mark>`'NoneType'`</mark> 이 들어간 오류이면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/apply1-3_run.py", line 24, in <module>
    source_event_counts = count_by_source(events)  # 소스별 개수를 센다
  File "…/anomaly_detection/normalize.py", line 45, in count_by_source
    for event in events:  # 이벤트를 하나씩 꺼낸다
TypeError: 'NoneType' object is not iterable
```

- 줄 번호는 사람마다 다릅니다.

**관제에서는**

- <mark>정규화된 이벤트를 한곳에 모으는 것이 SIEM(심)의 수집 · 정규화 단계의 결과입니다.</mark> 이 저장소를 기준으로 탐지 규칙과 조사가 이어집니다.
  - 값이 비어 있는 이벤트 수는 <mark>분석에서 빠지는 이벤트가 얼마나 되는지 알려 주는 품질 점검입니다.</mark>

---
