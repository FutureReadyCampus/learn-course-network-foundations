---
id: m4-u04-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/102_day03_am_baseline_login.md
  mission_id: GichanSource.m4-1104-am-baseline-login
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## Exercise 4-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise4-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise4-1_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 네 함수입니다.

① `load_daily_failures` 안

```python
    daily = pd.read_csv(path)  # CSV 파일을 읽어 표로 만든다 — 한 행이 하루
```

② `average_failures` 안

```python
    daily_failed_logins = daily["failed_logins"]  # failed_logins 열만 꺼낸다 — 하루 실패 횟수 7개가 나열된 열
    average = daily_failed_logins.mean()          # 7개의 평균을 구한다
```

③ `maximum_failures` 안

```python
    daily_failed_logins = daily["failed_logins"]  # failed_logins 열만 꺼낸다 — 하루 실패 횟수 7개가 나열된 열
    maximum = daily_failed_logins.max()           # 7개 중 가장 큰 값을 구한다
```

④ `make_limit` 안

```python
    limit = maximum + 1  # 평소 최댓값보다 1 큰 숫자를 기준으로 삼는다
```

**결과**

- (가) 출력은 다음과 같고, 하루 평균은 <mark>**2.4번**</mark>, 최댓값은 <mark>**4번**</mark>, 알림 기준은 <mark>**5번 이상**</mark>입니다.

```
--- 단계 1: 지난 7일 하루 로그인 실패 횟수
         date  failed_logins
0  2026-10-26              2
1  2026-10-27              3
2  2026-10-28              1
3  2026-10-29              4
4  2026-10-30              2
5  2026-10-31              3
6  2026-11-01              2
--- 단계 2: 하루 평균 2.4 번
--- 단계 3: 하루 최대 4 번
--- 단계 4: 알림 기준(임계값) 5 번 이상
```

- (나) ① 평균(2.4번) 이상인 날은 10/27(3번) · 10/29(4번) · 10/31(3번)으로 7일 중 **3일**입니다.
  - ② 평균을 기준으로 하면 지난 7일 중 위 3일에 알림이 발생하고, <mark>이 3일은 모두 평소와 같은 평범한 날입니다.</mark> 평범한 날에도 알림이 나서 담당자가 알림에 익숙해지고 진짜 알림도 무시하게 됩니다.
  - ③ 최댓값보다 1 큰 숫자(5번)를 기준으로 하면 지난 7일 중 알림이 발생한 날이 **0일**입니다. <mark>평소에는 알림이 나지 않고, 평소보다 많아졌을 때만 알림이 나게 하려는 것입니다.</mark>
- (다) <mark>12번이 섞이면 최댓값은 4번에서 12번이 되고, 알림 기준은 5번에서 13번이 됩니다.</mark> <mark>그러면 5 ~ 12번 실패는 알림이 나지 않아 놓칩니다.</mark>
  - <mark>7일 중 하루만 평소와 달라도 평소 최댓값이 커져서 알림 기준이 높아집니다.</mark> 지난 7일 표가 7일 치뿐이라 그 하루의 영향을 크게 받습니다.
  - 그래서 지난 7일 표에 평소와 다른 날이 섞이지 않았는지 확인하고, 며칠 쓴 뒤에는 새 데이터로 다시 구합니다.

**왜**

- <mark>평소를 구해서 기준을 정하면 숫자에 근거가 생깁니다.</mark> 「왜 5번인가」에 「지난 7일 중 가장 많은 날이 4번이었다」로 답할 수 있습니다.

**자주 틀리는 곳**

- 열 이름을 틀리면 `KeyError` 오류가 납니다. **열 이름은 파일 첫 줄의 `failed_logins` 와 정확히 같아야 합니다.**
  - 실행하면 다음 오류가 납니다(<mark>`KeyError: 'failed_login'`</mark> 처럼 열 이름이 나오면 이 실수입니다).

```
Traceback (most recent call last):
KeyError: 'failed_login'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "…/anomaly_detection/exercise4-1_run.py", line 7, in <module>
    average = average_failures(daily)  # 하루 평균을 구한다
  File "…/anomaly_detection/baseline.py", line 22, in average_failures
    daily_failed_logins = daily["failed_login"]  # 열 이름을 잘못 썼다
KeyError: 'failed_login'
```

  - 줄 번호는 사람마다 다릅니다.
- `daily_failed_logins.mean` 처럼 괄호를 빼면 값이 아니라 메서드가 담겨서, 실행 파일의 `round(average, 1)` 에서 `TypeError` 가 납니다. `mean` 과 `max` 는 **뒤에 괄호를 붙여 호출하는 메서드입니다.**

**관제에서는**

- <mark>알림 기준은 몇 주마다 최근 데이터로 다시 구합니다.</mark> 기준을 구한 날짜와 이유를 남겨 두어야 나중에 바꿀 때 근거가 됩니다.

---

## Exercise 4-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise4-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise4-2_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 함수입니다.

① `pick_login_failures` 안

```python
    actions = events["action"]           # action 열만 꺼낸다 — 무엇을 했는지가 57개 나열된 열
    is_login = actions == "POST /login"  # 행마다 로그인 요청인지 비교해 True 또는 False 를 만든다
    results = events["result"]           # result 열만 꺼낸다 — 성공 · 실패가 57개 나열된 열
    is_fail = results == "실패"          # 행마다 실패인지 비교해 True 또는 False 를 만든다
    both_true = is_login & is_fail       # 행마다 「로그인 요청이면서 실패」일 때만 True 가 된다
    login_failures = events[both_true]   # True 인 행만 골라 새 표를 만든다
```

② `pick_alert_ips` 안

```python
    is_many = ip_login_fail_counts >= limit    # 주소마다 「횟수가 기준 이상인가?」를 비교해 True 또는 False 를 만든다
    alert_ips = ip_login_fail_counts[is_many]  # True 인 주소만 남긴다
```

**결과**

- (가) 출력은 다음과 같고, 로그인 실패 이벤트는 <mark>**5개**</mark>, 알림 대상은 <mark>**203.0.113.50(5번)**</mark> 한 주소입니다.

```
--- 단계 1: 로그인 실패 이벤트 5 개
--- 단계 2: 주소별 로그인 실패 횟수
ip
203.0.113.50    5
dtype: int64
--- 단계 3: 알림 기준 5 번 이상인 주소
ip
203.0.113.50    5
dtype: int64
```

- (나) <mark>203.0.113.50 이 공격이라고 확정할 수는 없습니다.</mark> 다만 의심할 단서는 여럿 있습니다.
  - 단서: <mark>일정한 3초 간격으로 5번 연달아 실패했고(자동 입력처럼 보임),</mark> 6번째에 로그인에 성공한 뒤 곧바로 관리자 경로(`/admin` · `/admin/users`)를 두 번 요청했습니다.
  - 이 표에 없는 더 필요한 정보: <mark>그 주소가 회사 직원의 주소인지, 로그인에 성공한 계정이 누구인지</mark>입니다(웹 서버 로그에는 계정 이름이 없으므로 판정 서버 · SaaS 로그와 시각을 맞춰 봐야 합니다).
  - **알림은 「먼저 살펴볼 곳」이고 공격의 확정이 아닙니다.**
- (다) <mark>알림이 나지 않습니다.</mark>
  - 이 규칙은 실패한 이벤트만 주소별로 세어 5번 이상인지 봅니다. 4번 실패한 주소는 기준(5번)보다 적고, 5번째의 성공은 세는 대상이 아닙니다. 그래서 그 주소 하나만 있다면 단계 3 이 비어 알림이 나지 않습니다(샘플에서는 203.0.113.50 이 따로 있어 단계 3 에 나옵니다).
  - 그래서 담당자는 이 접속이 있었다는 것을 알림으로는 알 수 없습니다. <mark>알림이 없다는 것은 안전하다는 뜻이 아니라 「이 규칙의 조건을 충족하지 않았다」는 뜻일 뿐</mark>입니다.
  - 알림 기준(5번) 미만으로 천천히 시도하는 공격도 이 규칙의 조건을 충족하지 않습니다. 그래서 <mark>「알림 없음 ≠ 안전」</mark>입니다.

**왜**

- <mark>로그인 실패 5번을 사람이 57개 이벤트에서 직접 찾으면 놓치기 쉽습니다.</mark> 조건 두 개와 주소별 센 값을 이어 쓰면 몇 줄로 끝나고, 이벤트가 수만 개여도 같은 코드입니다.

**자주 틀리는 곳**

- **두 조건을 이을 때 `&` 대신 `and` 를 쓰면 `ValueError` 오류가 납니다.**
  - 실행하면 다음 오류가 납니다(<mark>`The truth value of a Series is ambiguous`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise4-2_run.py", line 4, in <module>
    login_failures = pick_login_failures(events)  # 로그인 실패 이벤트만 골라낸다
  File "…/anomaly_detection/login_detection.py", line 29, in pick_login_failures
    both_true = is_login and is_fail  # & 대신 and 를 썼다
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

  - 줄 번호는 사람마다 다릅니다.
- `GET /login` 까지 세는 실수가 있습니다. 이 규칙은 로그인 정보를 보내는 **`POST /login` 만 셉니다.**

**관제에서는**

- 로그인 실패 규칙의 알림에는 보통 주소와 횟수, 실패 뒤 성공이 있었는지가 함께 표시됩니다. <mark>성공이 있었다면 계정이 탈취됐을 수 있어 우선순위가 올라갑니다.</mark>

---

## Exercise 4-3 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise4-3_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise4-3_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 함수입니다.

① `classify_event` 안

```python
    if result == "실패" and action == "POST /login":  # 로그인 요청이 실패했으면
        return "비정상 로그인"                        # 비정상 로그인으로 분류한다
    if result == "실패" and "/admin" in action:       # 관리자 경로 요청이 실패했으면
        return "비인가 접근"                          # 비인가 접근으로 분류한다
```

② `count_types` 안

```python
    event_list = events.to_dict("records")  # 표를 딕셔너리 리스트로 바꾼다 — 이벤트 하나가 딕셔너리 하나
```

**결과**

- (가) 출력은 다음과 같고, 비정상 로그인 <mark>**5**</mark>, 비인가 접근 <mark>**3**</mark>, 기타 실패 <mark>**15**</mark>, 정상 <mark>**34**</mark>(합계 57)입니다.

```
--- 단계 1: 유형별 이벤트 수
비정상 로그인 5
비인가 접근 3
기타 실패 15
정상 34
--- 단계 2: 전체 이벤트 57 개
```

- (나) 「기타 실패」 15개에는 <mark>서로 다른 일이 섞여 있습니다.</mark>
  - `server`(판정 서버) 실패 9개: gaeun 의 `ACCOUNT:CHANGE` 3번, dami 의 `SALES:QUERY` 3번과 `SALES:CHANGE` 1번, seoyeon 의 `SETTLE:QUERY` 1번과 `SALES:CHANGE` 1번입니다.
  - `web`(웹 서버) 실패 5개: 198.51.100.90 이 09:20:10 ~ 09:20:12 에 `/.env` · `/wp-login.php` · `/phpmyadmin` 을 차례로 요청한 것 3개와, 페이지 요청 실패 2개(`/board/99` · `/report`)입니다.
  - `saas`(SaaS) 실패 1개: jiwoo 의 `login` 입니다.
  - <mark>하나로 묶으면 이 일들이 모두 같은 유형으로 보여서, 담당자가 대응을 정할 수 없습니다.</mark> 예를 들어 같은 사용자의 계정 변경이 3번 실패한 것과 `/.env` · `/wp-login.php` · `/phpmyadmin` 을 차례로 요청한 것은 대응이 전혀 다릅니다. 그래서 Unit 6에서 유형을 더 나눕니다.
- (다) 「기타 실패」를 맨 위에 두면 결과가 실패인 이벤트 23개가 모두 먼저 조건을 충족해서 **기타 실패 23개**가 되고, 비정상 로그인과 비인가 접근은 **0개**가 됩니다. 정상은 34개 그대로입니다.
  - 담당자는 로그인 실패와 관리자 경로 요청 실패를 구분할 수 없게 되어, 비밀번호 대응과 접근 차단 중 무엇을 할지 정하지 못합니다.
  - 먼저 조건을 충족한 규칙에서 멈추기 때문입니다. <mark>좁은 조건(로그인 실패, 관리자 경로)을 위에 두고 넓은 조건(모든 실패)을 아래에 두어야 유형이 나뉩니다.</mark>

**왜**

- <mark>유형 이름을 정하는 규칙은 위에서부터 차례로 보고 먼저 조건을 충족하는 것을 씁니다.</mark> 로그인 실패를 먼저 보고, 그다음 관리자 경로를 보고, 나머지 실패를 「기타 실패」로 모읍니다.

**자주 틀리는 곳**

- `events.to_dict("records")` 를 빼고 `event_list = events` 로 쓰면, `for event in event_list` 가 이벤트가 아니라 **열 이름**을 하나씩 꺼내서 오류가 납니다.
  - 실행하면 다음 오류가 납니다(<mark>`string indices must be integers`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise4-3_run.py", line 4, in <module>
    type_event_counts = count_types(events)  # 유형별로 센다
  File "…/anomaly_detection/classify.py", line 42, in count_types
    action = event["action"]  # 그 이벤트의 행동
TypeError: string indices must be integers
```

  - 줄 번호는 사람마다 다릅니다.
- `if` 두 조건을 `and` 로 잇지 않고 `result == "실패"` 만 쓰면 <mark>모든 실패가 첫 번째 규칙의 조건을 충족해 「비정상 로그인」으로 나옵니다.</mark>

**관제에서는**

- 유형 규칙은 운영하면서 계속 고칩니다. <mark>「기타」가 너무 크면 규칙이 부족하다는 신호입니다.</mark>

---

## 정답 마무리

 **터미널에 입력합니다.**

```bash
pwd
ls
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기

**결과**

- 이번 Unit에서 만든 파일 **여덟 개**와 안내 · 보고서 두 파일이 보여야 합니다. 깃허브에 올리는 일은 Unit 5의 Exercise 5-2 마지막에 합니다.
