---
id: m4-u08-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/110_day05_am_false_alarm_tuning.md
  mission_id: GichanSource.m4-1106-am-false-alarm-tuning
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

---

## Exercise 8-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python day05_2-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `find_false_alarms` 안

```python
    is_false = ~is_real                               # True 와 False 를 뒤집어 문제가 아니었던 알림을 True 로 만든다
    false_alarms = alerts[is_false]                   # True 인 행만 골라 새 표로 만든다
    false_alarm_rule_counts = false_alarms["rule"].value_counts()  # 오탐이 규칙마다 몇 개인지 센다
```

② `find_missed` 안

```python
    caught_ids = real_alerts["problem"]               # 진짜 알림이 가리키는 문제 번호를 꺼낸다
    is_missed = ~is_caught                            # 알림이 나지 않은 문제를 True 로 만든다
    missed_problems = problems[is_missed]             # True 인 행만 골라 새 표로 만든다
```

③ `count_real_alerts` 안

```python
    real_alert_count = is_real.sum()                  # True 가 몇 개인지 더해서 센다 (True 는 1, False 는 0)
```

내가 채운 코드는 위의 코드입니다. <mark>줄 수가 달라도 주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같고, 알림은 <mark style="background:#bde3ff">**7개**</mark>, 오탐은 <mark style="background:#bde3ff">**4개**</mark>, 미탐은 <mark style="background:#bde3ff">**2개**</mark>입니다.

```
--- 단계 1: 알림 전체 ---
알림 수: 7
--- 단계 2: 진짜 문제였던 알림 (맞게 찾은 알림) ---
진짜 문제였던 알림 수: 3
--- 단계 3: 오탐 (문제가 아닌데 난 알림) ---
오탐 수: 4
오탐이 난 규칙과 오탐 수:
rule
SaaS 평소와 다른 IP      2
서버 반복 거절            1
SaaS 업무 시간 밖 로그인    1
Name: count, dtype: int64
--- 단계 4: 미탐 (알림이 나지 않은 진짜 문제) ---
미탐 수: 2
놓친 문제: P4 203.0.113.50 로그인 5번 실패 뒤 성공하고 관리자 화면을 요청함
놓친 문제: P5 seoyeon 권한 없는 정산 조회를 시도함
```

- (나) A2(gaeun)는 규칙이 정한 조건(서버 거절 3번 이상)에는 맞았지만, 조사해 보니 <mark style="background:#bde3ff">서버 설정 오류였고 공격이나 권한 문제가 아니었습니다.</mark> 그래서 오탐입니다.
  - 그래도 한 번은 확인해야 했던 이유: 조사하기 전에는 설정 오류인지 공격인지 알 수 없기 때문입니다. <mark style="background:#bde3ff">오탐인지는 확인한 뒤에야 알 수 있습니다.</mark>
  - 오탐을 세는 것은 확인한 알림 중 문제가 아니었던 것의 개수를 세는 일입니다.
- (다) P5(seoyeon 의 `SETTLE:QUERY`)는 서버가 한 번 거절했을 뿐이라 「3번 이상 거절」 규칙에 걸리지 않았습니다. 그래서 <mark style="background:#bde3ff">알림이 나지 않았습니다.</mark>
  - 필요한 규칙의 예: 정산처럼 중요한 자원에 권한 없이 접근을 시도하면 한 번만 거절돼도 알리는 규칙입니다.
  - 이런 규칙은 횟수가 아니라 대상의 중요도를 보기 때문에 오탐이 늘 수 있습니다.

**왜**

- <mark>오탐과 미탐은 줄여야 하는 방향이 반대입니다.</mark> 오탐을 줄이려고 규칙을 엄격하게 만들면 미탐이 늘고, 미탐을 줄이려고 규칙을 느슨하게 만들면 오탐이 늡니다. 그래서 둘을 따로 세어 둡니다.

**자주 틀리는 곳**

- `is_false = ~is_real` 대신 `not is_real` 이라고 쓰면 `ValueError` 오류가 납니다. <mark>**표의 열에는 `not` 이 아니라 `~` 를 씁니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`The truth value of a Series is ambiguous`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/day05_2-1_run.py", line 14, in <module>
  File "…/anomaly_detection/evaluation.py", line 31, in find_false_alarms
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

  - 줄 번호는 사람마다 다릅니다.
- `is_real.sum()` 에서 괄호를 빼고 `is_real.sum` 으로 쓰면 오류는 나지 않지만 <mark>**숫자가 아니라 `<bound method Series.sum of …>` 라는 긴 글자가 나옵니다.**</mark> 단계 2의 `진짜 문제였던 알림 수:` 줄에 숫자 대신 `<bound method Series.sum of …>` 가 나오면 이 실수입니다. `.sum()` 은 괄호까지 써야 합니다.
- `is_missed = ~is_caught` 에서 `~` 를 빼고 `is_missed = is_caught` 로 쓰면 오류는 나지 않지만 <mark>**단계 4의 `미탐 수:` 가 2가 아니라 3으로 나옵니다.**</mark> 알림이 난 P1 · P2 · P3 이 놓친 문제로 나오는 것이 이 실수의 모습입니다.

**관제에서는**

- 오탐을 세는 것은 담당자의 시간을 지키는 일이고, 미탐을 세는 것은 놓친 위험을 줄이는 일입니다. <mark>규칙을 평가할 때는 이 두 숫자를 함께 보고합니다.</mark>

---

## Exercise 8-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python day05_3-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `apply_exception` 안

```python
    is_ip_rule = alerts["rule"] == IP_RULE            # 각 알림이 IP 규칙의 알림인지 비교한다
    is_trusted = alerts["ip"].isin(TRUSTED_IPS)       # 각 알림의 IP 가 믿는 IP 리스트에 있는지 구한다
    is_removed = is_ip_rule & is_trusted              # IP 규칙의 알림이면서 믿는 IP 에서 온 것만 True 로 만든다
    kept_alerts = alerts[is_kept]                     # True 인 행만 골라 새 표로 만든다
```

② `count_real_removed` 안

```python
    is_real_removed = removed_alerts["real"]          # real 열(진짜 문제이면 True)을 꺼낸다
    real_removed = removed_alerts[is_real_removed]    # True 인 행만 골라 새 표로 만든다
```

③ `find_removed_users` 안

```python
    removed_users = removed_alerts["user"].unique()   # 같은 사용자는 한 번씩만 꺼낸다
```

내가 채운 코드는 위의 코드입니다. <mark>줄 수가 달라도 주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같고, 오탐은 <mark style="background:#bde3ff">**4개에서 2개**</mark>로 줄었고 빠진 알림은 <mark style="background:#bde3ff">**A4 · A5**</mark>(사용자 jiwoo · seoyeon), 빠진 진짜 문제 알림은 <mark style="background:#bde3ff">**0개**</mark>입니다.

```
--- 단계 1: 예외 규칙을 적용하기 전 ---
알림 수: 7
오탐 수: 4
--- 단계 2: 예외 규칙으로 빠진 알림 ---
빠진 알림 수: 2
빠진 알림: A4 SaaS 평소와 다른 IP jiwoo 203.0.113.80
빠진 알림: A5 SaaS 평소와 다른 IP seoyeon 203.0.113.80
빠진 알림의 사용자: ['jiwoo' 'seoyeon']
--- 단계 3: 예외 규칙을 적용한 뒤 ---
알림 수: 5
오탐 수: 2
--- 단계 4: 빠진 알림 중 진짜 문제였던 것 ---
진짜 문제였던 알림 수: 0
```

- (나) 오탐이 <mark style="background:#bde3ff">4개에서 2개로 줄었습니다.</mark> A3 은 같은 IP `203.0.113.80` 에서 왔지만 규칙이 `SaaS 업무 시간 밖 로그인` 이라서, <mark style="background:#bde3ff">예외 규칙이 `IP_RULE` 의 알림만 빼도록 정했기 때문에</mark> 그대로 남았습니다.
  - A3 까지 빼려면 그 규칙에도 예외를 따로 정해야 하고, 그때도 빠진 진짜 문제가 없는지 다시 확인합니다.
- (다) 믿는 IP 에서 <mark style="background:#bde3ff">계정이 도용되어 로그인해도</mark> 이 규칙은 알림을 내지 않습니다. 예를 들어 협력사 사무실에 있는 누군가가 다른 직원의 계정으로 접속해도 「평소와 다른 IP」 알림은 나지 않습니다.
  - 그래서 다른 규칙(대량 다운로드 등)은 예외에서 빼고 그대로 둡니다. 예외는 근거와 함께 기록하고 주기적으로 다시 검토합니다.

**왜**

- <mark>예외를 규칙 하나에만 적용하면 오탐은 줄이면서 다른 규칙이 찾는 진짜 문제는 지키는 효과가 있습니다.</mark> 단계 4의 `진짜 문제였던 알림 수:` 가 0인 것은 빠진 알림 A4 · A5 가 모두 오탐이었다는 뜻입니다.

**자주 틀리는 곳**

- `is_removed = is_ip_rule & is_trusted` 에서 `is_ip_rule &` 를 빼고 `is_removed = is_trusted` 로 쓰면 오류는 나지 않지만 <mark>**단계 4의 `진짜 문제였던 알림 수:` 가 0이 아니라 1로 나옵니다.**</mark> 같은 IP 에서 온 A3 · A6 까지 빠지고, 빠진 A6 은 진짜 문제입니다.
  - 이때 출력은 다음과 같습니다(<mark style="background:#ffc4d6">`빠진 알림 수: 4`</mark> 와 <mark style="background:#ffc4d6">`진짜 문제였던 알림 수: 1`</mark> 이 나오면 이 실수입니다).

```
--- 단계 1: 예외 규칙을 적용하기 전 ---
알림 수: 7
오탐 수: 4
--- 단계 2: 예외 규칙으로 빠진 알림 ---
빠진 알림 수: 4
빠진 알림: A3 SaaS 업무 시간 밖 로그인 jiwoo 203.0.113.80
빠진 알림: A4 SaaS 평소와 다른 IP jiwoo 203.0.113.80
빠진 알림: A5 SaaS 평소와 다른 IP seoyeon 203.0.113.80
빠진 알림: A6 SaaS 대량 다운로드 seoyeon 203.0.113.80
빠진 알림의 사용자: ['jiwoo' 'seoyeon']
--- 단계 3: 예외 규칙을 적용한 뒤 ---
알림 수: 3
오탐 수: 1
--- 단계 4: 빠진 알림 중 진짜 문제였던 것 ---
진짜 문제였던 알림 수: 1
```

**관제에서는**

- 예외 규칙은 오탐을 빠르게 줄이는 방법이지만, <mark>예외를 넣은 뒤에는 빠진 알림 중 진짜 문제가 있는지 항상 확인합니다.</mark> 예외 리스트는 근거와 함께 기록해 두고, 협력사 계약이 끝나면 지웁니다.

---

## Exercise 8-3 정답

 **터미널에 입력합니다.**

```bash
pwd
python day05_4-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `merge_alerts` 안

```python
    all_alerts = pd.concat([alerts, login_alerts])    # 두 알림 표를 위아래로 이어 붙인다
```

② `evaluate` 안

```python
    caught_ids = all_alerts["problem"].dropna()       # 문제 번호가 비어 있는 알림(오탐)을 빼고 번호만 남긴다
    is_caught = problems["id"].isin(caught_ids)       # 각 문제 번호가 그 안에 있는지 구한다
    is_missed = ~is_caught                            # 알림이 나지 않은 문제를 True 로 만든다
    missed_problems = problems[is_missed]             # True 인 행만 골라 새 표로 만든다
```

③ `make_summary` 안

```python
    summary = "알림 " + str(alert_count) + "개 중 오탐 " + str(false_alarm_count) + "개 · 놓친 문제 " + str(missed_count) + "개"  # 문자열과 숫자를 이어 한 문장으로 만든다
```

내가 채운 코드는 위의 코드입니다. <mark>줄 수가 달라도 주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같고, 한 문장 요약은 <mark style="background:#bde3ff">**「알림 6개 중 오탐 2개 · 놓친 문제 1개」**</mark>입니다.

```
--- 단계 1: 믿는 IP 예외 규칙 적용 ---
빠진 알림 수: 2
남은 알림 수: 5
--- 단계 2: 로그인 규칙의 알림 합치기 ---
합친 뒤 알림 수: 6
--- 단계 3: 합친 알림의 오탐 ---
오탐 수: 2
--- 단계 4: 아직 놓친 진짜 문제 ---
미탐 수: 1
놓친 문제: P5 seoyeon 권한 없는 정산 조회를 시도함
--- 단계 5: 한 문장 요약 ---
알림 6개 중 오탐 2개 · 놓친 문제 1개
```

- (나) 놓친 문제가 <mark style="background:#bde3ff">2개(P4 · P5)에서 1개(P5)로 줄었습니다.</mark>
  - P4 가 잡힌 이유: 로그인 규칙의 알림 A8 이 `problem` 열에 `P4` 를 가리키기 때문에 「알림이 난 문제」에 들어갑니다.
  - 오탐이 늘지 않은 이유: A8 은 조사해 보니 진짜 문제(`real` 이 `True`)였기 때문에, 오탐은 Exercise 8-2에서 줄인 2개(A2 · A3) 그대로입니다.
- (다) P5 를 찾으려면 <mark style="background:#bde3ff">정산처럼 중요한 자원에 권한 없이 접근하면 한 번만 거절돼도 알리는 규칙</mark>이 필요합니다.
  - 그 규칙을 더하면 업무상 실수로 권한 없는 곳을 한 번 건드린 사용자까지 알림이 나서 <mark style="background:#bde3ff">오탐이 늘 수 있습니다.</mark>
  - 그래서 규칙을 더한 뒤에는 오늘처럼 오탐과 미탐을 다시 세어 봅니다.

**왜**

- <mark>규칙을 합치면 놓친 문제는 줄지만, 합친 뒤에 다시 세어 봐야 오탐이 늘지 않았는지 알 수 있습니다.</mark> 숫자 세 개를 한 문장으로 만들어 두면 다음에 규칙을 고칠 때 전후를 바로 비교할 수 있습니다.

**자주 틀리는 곳**

- `pd.concat([alerts, login_alerts])` 대신 `pd.concat(alerts, login_alerts)` 라고 쓰면 `TypeError` 오류가 납니다. <mark>**표는 대괄호 `[ ]` 안에 리스트로 묶어 전달합니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`concat() takes 1 positional argument but 2 were given`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/day05_4-1_run.py", line 14, in <module>
  File "…/anomaly_detection/final_check.py", line 37, in merge_alerts
TypeError: concat() takes 1 positional argument but 2 were given
```

  - 줄 번호는 사람마다 다릅니다.
- `.dropna()` 에서 괄호를 빼면 `TypeError` 오류가 납니다. <mark>**`.dropna()` 는 괄호까지 써야 합니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`only list-like objects are allowed to be passed to isin()`</mark> 로 시작하는 줄이 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/day05_4-1_run.py", line 19, in <module>
  File "…/anomaly_detection/final_check.py", line 53, in evaluate
TypeError: only list-like objects are allowed to be passed to isin(), you passed a `method`
```

  - 줄 번호는 사람마다 다릅니다.
- `is_missed = ~is_caught` 에서 `~` 를 빼면 오류는 나지 않지만 <mark>**놓친 문제로 알림이 난 문제가 나옵니다.**</mark> 단계 4의 `놓친 문제:` 줄에 P1 · P2 · P3 · P4 가 나오는 것이 이 실수의 모습입니다.

**관제에서는**

- 새 규칙을 운영에 넣기 전에 오탐과 미탐을 세어 전후를 비교하는 것은 흔한 절차입니다. <mark>숫자를 보고서에 한 줄로 남겨 두면 어떤 규칙이 효과가 있었는지 나중에 확인할 수 있습니다.</mark>

---

## 정답 마무리

- `ls` 결과에 오늘 파일들과 이 안내 · 보고서 두 파일이 모두 보이면 됩니다.
- 보고서에 빈 `답:` 이 없으면 됩니다. 못 적은 칸은 `모름 — 막힌 곳: …` 으로 적습니다.
