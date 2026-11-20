---
id: m4-u04-l08
title: 정답
render: markdown
---

# 정답

## 정답 보는 법

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

1. **핵심 실습**: 실습 4-1 · 4-2 정답입니다. 오늘 모두가 하는 실습이니 먼저 맞춰 봅니다.
2. **도전(선택)**: 도전 4-1 ~ 4-3 정답입니다. 도전을 한 사람만 봅니다.
3. 정답마다 채운 코드, 결과, 왜, 자주 틀리는 곳, 관제에서는 순서로 읽습니다.

---

## 실습 4-1 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise4-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise4-1_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `score_findings` 안 — 1번과 2번 주석 사이에 미리 채운 `findings_table["points"] = points` 줄과 `grouped = …` 줄이 있습니다. 두 줄을 한 번에 붙이지 말고, 아래 상자를 하나씩 해당 번호 주석 바로 아래에 붙입니다.

1번 주석 아래

```python
    points = findings_table["rule"].map(WEIGHTS)       # rule 열을 꺼내 바로 규칙마다 점수를 채운다(map)
```

2번 주석 아래(미리 채운 `grouped = …` 줄보다 아래)

```python
    totals = grouped["points"].sum()                   # 그룹에서 points 열을 골라 바로 합계를 구한다(sum)
```

② `make_grade` 안

```python
    if score >= HIGH_LIMIT:                            # 점수가 high 기준 이상이면
        return "high"                                  # high 이다
```

③ `make_records` 안

```python
        record = {"entity": entity, "score": int(score), "grade": grade, "reasons": reasons[entity]}  # 대상 · 점수 · 등급 · 이유를 딕셔너리로 만든다
```

내가 채운 코드는 위의 코드입니다. <mark>줄 수가 달라도 주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같고, high 는 <mark style="background:#bde3ff">**dami**</mark>, mid 는 <mark style="background:#bde3ff">**seoyeon · gaeun · jiwoo**</mark>, low 는 <mark style="background:#bde3ff">**198.51.100.90**</mark> 입니다.

```
--- 단계 1: 탐지된 규칙 8 건
--- 단계 2: 대상별 점수
entity
dami             60
seoyeon          45
gaeun            40
jiwoo            35
198.51.100.90    30
Name: points, dtype: int64
--- 단계 3: unit05_risk_scores.json 에 5 건 저장
--- 단계 4: 등급 · 대상 · 점수 · 이유
high dami 60 ['퇴사한 계정']
mid seoyeon 45 ['평소와 다른 IP', '대량 다운로드']
mid gaeun 40 ['규칙은 허용인데 서버가 거절', '여러 로그 연결']
mid jiwoo 35 ['업무 시간 밖 로그인', '평소와 다른 IP']
low 198.51.100.90 30 ['경로 스캔']
```

- (나) seoyeon 의 45점은 <mark>평소와 다른 IP 20 + 대량 다운로드 25</mark> 를 더한 값입니다.
  - 이유를 함께 저장하는 까닭은 담당자가 점수만으로는 왜 올라왔는지 알 수 없기 때문입니다. 규칙 이름이 있으면 「평소와 다른 IP · 대량 다운로드(SaaS)」로 근거를 바로 설명하고, 기준을 바꿀 때 어떤 규칙이 영향을 주는지도 따질 수 있습니다.
- (다) 198.51.100.90 은 경로 스캔 30점뿐이라 <mark>mid 기준 35에 못 미쳐 low</mark> 입니다.
  - <mark>low 는 점수 기준상 낮은 등급이라는 뜻이고, 기록을 무시해도 된다는 뜻은 아닙니다.</mark> 샘플에서 이 IP 는 09:20:10 ~ 09:20:12 에 스캐너 경로 3종류를 요청했고 모두 실패했습니다. IP 에 적용되는 규칙은 경로 스캔(30점) 하나뿐이라 mid 기준 35 에 닿을 수 없어서 항상 low 입니다. 그래도 이 IP 의 이벤트는 다시 확인할 수 있게 남깁니다.

**왜**

- <mark>규칙이 겹칠수록 점수가 오릅니다.</mark> 사용자 하나에 여러 규칙이 겹치면 먼저 볼 이유가 늘고, 하나뿐이면 순서가 뒤로 갑니다. 이유를 같이 저장해 두면 그 순서를 설명할 수 있습니다.

**자주 틀리는 곳**

- `.sum()` 에서 괄호를 빼면 오류가 납니다. 괄호 없는 `grouped["points"].sum` 은 값이 아니라 메서드라서 다음 줄의 `totals.sort_values` 에서 `AttributeError` 가 납니다.
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`'function' object has no attribute 'sort_values'`</mark> 또는 비슷한 문구가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise4-1_run.py", line 11, in <module>
    totals = score_findings(findings)                      # 대상마다 점수를 더한다
  File "…/anomaly_detection/risk_scores.py", line 74, in score_findings
    totals = totals.sort_values(ascending=False)       # 점수가 높은 순으로 정렬한다 — 미리 채운 줄
AttributeError: 'function' object has no attribute 'sort_values'
```

  - 줄 번호는 사람마다 다릅니다.
- `make_grade` 는 **높은 기준부터 차례로 확인합니다.** high 기준을 먼저 확인하고, 아니면 mid 기준을 확인하는 순서입니다. 순서를 바꿔 mid 를 먼저 확인하면 높은 점수도 mid 가 됩니다.

**관제에서는**

- <mark>점수와 등급 기준은 정해 둔 날과 이유를 남깁니다.</mark> 기준을 바꾸면 같은 로그에서 등급이 달라지기 때문입니다. 실습 4-2에서는 알림이 맞았는지 세고, 같은 원인의 틀린 알림을 줄입니다.

---

## 실습 4-2 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise4-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `apply_exception` 안 — 3번과 4번 주석 사이에 미리 채운 `removed_alerts = …` · `is_kept = …` 두 줄이 있습니다. 네 줄을 한 번에 붙이지 말고, 아래 상자를 하나씩 해당 번호 주석 바로 아래에 붙입니다.

1번 주석 아래

```python
    is_ip_rule = alerts["rule"] == IP_RULE            # 각 알림이 IP 규칙의 알림인지 비교한다
```

2번 주석 아래

```python
    is_trusted = alerts["ip"].isin(TRUSTED_IPS)       # 각 알림의 IP 가 믿는 IP 리스트에 있는지 구한다
```

3번 주석 아래

```python
    is_removed = is_ip_rule & is_trusted              # IP 규칙의 알림이면서 믿는 IP 에서 온 것만 True 로 만든다
```

4번 주석 아래(미리 채운 `is_kept = …` 줄보다 아래)

```python
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
빠진 알림의 사용자: ['jiwoo', 'seoyeon']
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
빠진 알림의 사용자: ['jiwoo', 'seoyeon']
--- 단계 3: 예외 규칙을 적용한 뒤 ---
알림 수: 3
오탐 수: 1
--- 단계 4: 빠진 알림 중 진짜 문제였던 것 ---
진짜 문제였던 알림 수: 1
```

**관제에서는**

- 예외 규칙은 오탐을 빠르게 줄이는 방법이지만, <mark>예외를 넣은 뒤에는 빠진 알림 중 진짜 문제가 있는지 항상 확인합니다.</mark> 예외 리스트는 근거와 함께 기록해 두고, 협력사 계약이 끝나면 지웁니다.

---

## 도전 4-1 정답

> **선택입니다. 시간이 남을 때 합니다.** 여기부터는 도전 정답입니다. 도전을 한 사람만 봅니다. 핵심 실습 정답은 앞의 실습 4-1 · 4-2 정답에 있습니다.

**터미널에 입력합니다.**

```bash
pwd
python challenge4-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python challenge4-1_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `attach_user_to_web` 안

```python
    users = web_part["ip"].map(ip_user)                # ip 열을 꺼내 바로 IP 마다 사용자를 찾아 채운다(map)
```

② `build_timeline` 안

```python
    timeline = pd.concat([server_part, saas_part, web_part])  # 세 표를 위아래로 연결해 표 하나로 만든다
    timeline = timeline.sort_values(["user", "time"])  # user 순으로, 같은 user 는 time 순으로 정렬한다
```

③ `find_chains` 안 — 4번 주석 위의 `if has_many_sources and is_close:` 줄은 이미 있으니 붙이지 않습니다. 두 줄 모두 그 `if` 안쪽입니다.

4번 주석 아래

```python
            reason = "서로 다른 로그 " + str(source_count) + "종류 · " + str(span) + "분 안"  # 문자열을 연결해 이유 문장을 만든다
```

5번 주석 아래

```python
            chains.append({"user": user, "reason": reason})  # 연결된 사건에 사용자와 이유를 추가한다
```

내가 채운 코드는 위의 코드입니다. <mark>줄 수가 달라도 주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같고, 연결된 사건은 <mark style="background:#bde3ff">**gaeun**</mark> 한 명이며 이유는 「서로 다른 로그 3종류 · 41분 안」입니다.

```
--- 단계 1: IP 로 사용자를 알 수 있는 웹 실패 이벤트 1 개
--- 단계 2: 사용자별로 시간순으로 놓은 이벤트 24 개
gaeun 의 이벤트 (시각 · 로그 · 행동 · 결과)
2026-11-02 09:33:51 web GET /admin 실패
2026-11-02 10:05:00 server ACCOUNT:CHANGE 실패
2026-11-02 10:09:00 server ACCOUNT:CHANGE 실패
2026-11-02 10:12:55 saas login 성공
2026-11-02 10:14:00 server ACCOUNT:CHANGE 실패
--- 단계 3: 60 분 안에 서로 다른 로그로 연결된 사건
{'user': 'gaeun', 'reason': '서로 다른 로그 3종류 · 41분 안'}
--- 단계 4: 로그 종류는 여럿이지만 시간 차가 60분을 초과해 연결되지 않은 사용자
{'user': 'seoyeon', 'source_count': 2, 'span_minutes': 555}
```

- (나) gaeun 의 이벤트 5개는 <mark>웹(`web`) 1개 · 판정 서버(`server`) 3개 · SaaS(`saas`) 1개</mark>이고, 서로 다른 로그가 3종류이며 09:33 부터 10:14 까지 41분 안에 모여 있어서 연결됐습니다.
  - <mark>공격이라고 확정할 수 없습니다.</mark> 서버의 거절 3개는 Module 3(접근통제) 규칙으로는 「허용」이었고, 웹의 `/admin` 실패는 1건이며, SaaS 로그인은 성공했습니다. 같은 시간대에 여러 로그가 확인될 뿐, 원인은 이 기록만으로 알 수 없습니다.
- (다) seoyeon 은 단계 4 에서 <mark>로그 종류 2</mark>(서버 · SaaS)로 조건 ①(2 이상)을 만족하지만, 처음부터 마지막까지가 <mark>555분</mark>(09:05 ~ 18:20)으로 조건 ②(60분 이내)를 만족하지 못해 연결되지 않았습니다.
  - 하나의 사건으로 연결하지 않으면 서버의 `SETTLE:QUERY` 거절(권한 없음)과 실습 4-1에서 본 seoyeon 의 이유(평소와 다른 IP · 대량 다운로드)가 같은 사용자의 기록이라는 점을 <mark>탐지 결과에서 확인하기 어렵습니다.</mark>

**왜**

- <mark>서로 다른 로그와 짧은 시간, 두 조건이 함께 있어야 하나의 사건으로 연결합니다.</mark> 로그 종류만 보면 하루 종일 흩어진 일까지 연결되고, 시간만 보면 한 로그의 반복만 연결됩니다.

**자주 틀리는 곳**

- `pd.concat` 에 표를 쉼표로 따로 전달하면 `TypeError` 오류가 납니다. **표는 대괄호 `[ ]` 안에 넣어 리스트로 전달합니다.**
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`concat() takes 1 positional argument but 3 were given`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/challenge4-1_run.py", line 18, in <module>
    timeline = build_timeline(server_part, saas_part, web_part)  # 세 로그를 합쳐 사용자 · 시각 순으로 정렬한다
  File "…/anomaly_detection/correlation.py", line 45, in build_timeline
    timeline = pd.concat(server_part, saas_part, web_part)  # 세 표를 위아래로 연결해 표 하나로 만든다
TypeError: concat() takes 1 positional argument but 3 were given
```

  - 줄 번호는 사람마다 다릅니다.
- 정렬 결과를 다시 담지 않고 `timeline.sort_values(["user", "time"])` 만 쓰면 오류는 나지 않지만 **정렬한 결과가 사라져서** 단계 2 의 gaeun 이벤트가 시각 순서가 아닙니다. 서버 이벤트 3개(10:05 · 10:09 · 10:14)가 먼저 나오고, 그 뒤에 SaaS 10:12, 웹 09:33 이 나오면 이 실수입니다.

**관제에서는**

- <mark>이벤트 하나씩이 아니라 사용자 단위의 사건으로 연결하면 담당자가 읽을 양이 줄어듭니다.</mark> 시간 기준 밖에 있는 이벤트는 따로 두고, 다른 사건과 섞이지 않게 합니다.

---

## 도전 4-2 정답

**터미널에 입력합니다.**

```bash
pwd
python challenge4-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `find_false_alarms` 안

```python
    is_false = ~is_real                               # True 와 False 를 뒤집어 문제가 아니었던 알림을 True 로 만든다
    false_alarms = alerts[is_false]                   # True 인 행만 골라 새 표로 만든다
    false_alarm_rule_counts = false_alarms["rule"].value_counts()  # 오탐이 규칙마다 몇 개인지 센다
```

② `find_missed` 안 — 4번과 5번 주석 사이에 미리 채운 `is_caught = …` 줄이 있습니다. 세 줄을 한 번에 붙이지 말고, 아래 상자를 하나씩 해당 번호 주석 바로 아래에 붙입니다.

4번 주석 아래(미리 채운 `is_caught = …` 줄보다 위)

```python
    caught_ids = real_alerts["problem"]               # 진짜 알림이 가리키는 문제 번호를 꺼낸다
```

5번 주석 아래

```python
    is_missed = ~is_caught                            # 알림이 나지 않은 문제를 True 로 만든다
```

6번 주석 아래

```python
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
  File "…/anomaly_detection/challenge4-2_run.py", line 14, in <module>
  File "…/anomaly_detection/evaluation.py", line 31, in find_false_alarms
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

  - 줄 번호는 사람마다 다릅니다.
- `is_real.sum()` 에서 괄호를 빼고 `is_real.sum` 으로 쓰면 오류는 나지 않지만 <mark>**숫자가 아니라 `<bound method Series.sum of …>` 라는 긴 글자가 나옵니다.**</mark> 단계 2의 `진짜 문제였던 알림 수:` 줄에 숫자 대신 `<bound method Series.sum of …>` 가 나오면 이 실수입니다. `.sum()` 은 괄호까지 써야 합니다.
- `is_missed = ~is_caught` 에서 `~` 를 빼고 `is_missed = is_caught` 로 쓰면 오류는 나지 않지만 <mark>**단계 4의 `미탐 수:` 가 2가 아니라 3으로 나옵니다.**</mark> 알림이 난 P1 · P2 · P3 이 놓친 문제로 나오는 것이 이 실수의 모습입니다.

**관제에서는**

- 오탐을 세는 것은 담당자의 시간을 지키는 일이고, 미탐을 세는 것은 놓친 위험을 줄이는 일입니다. <mark>규칙을 평가할 때는 이 두 숫자를 함께 보고합니다.</mark>

---

## 도전 4-3 정답

**터미널에 입력합니다.**

```bash
pwd
python challenge4-3_run.py
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
  - 오탐이 늘지 않은 이유: A8 은 조사해 보니 진짜 문제(`real` 이 `True`)였기 때문에, 오탐은 실습 4-2에서 줄인 2개(A2 · A3) 그대로입니다.
- (다) P5 를 찾으려면 <mark style="background:#bde3ff">정산처럼 중요한 자원에 권한 없이 접근하면 한 번만 거절돼도 알리는 규칙</mark>이 필요합니다.
  - 그 규칙을 더하면 업무상 실수로 권한 없는 곳을 한 번 건드린 사용자까지 알림이 나서 <mark style="background:#bde3ff">오탐이 늘 수 있습니다.</mark>
  - 그래서 규칙을 더한 뒤에는 도전 4-2에서 한 것처럼 오탐과 미탐을 다시 세어 봅니다.

**왜**

- <mark>규칙을 합치면 놓친 문제는 줄지만, 합친 뒤에 다시 세어 봐야 오탐이 늘지 않았는지 알 수 있습니다.</mark> 숫자 세 개를 한 문장으로 만들어 두면 다음에 규칙을 고칠 때 전후를 바로 비교할 수 있습니다.

**자주 틀리는 곳**

- `pd.concat([alerts, login_alerts])` 대신 `pd.concat(alerts, login_alerts)` 라고 쓰면 `TypeError` 오류가 납니다. <mark>**표는 대괄호 `[ ]` 안에 리스트로 묶어 전달합니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`concat() takes 1 positional argument but 2 were given`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/challenge4-3_run.py", line 14, in <module>
  File "…/anomaly_detection/final_check.py", line 37, in merge_alerts
TypeError: concat() takes 1 positional argument but 2 were given
```

  - 줄 번호는 사람마다 다릅니다.
- `.dropna()` 에서 괄호를 빼면 `TypeError` 오류가 납니다. <mark>**`.dropna()` 는 괄호까지 써야 합니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`only list-like objects are allowed to be passed to isin()`</mark> 로 시작하는 줄이 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/challenge4-3_run.py", line 19, in <module>
  File "…/anomaly_detection/final_check.py", line 53, in evaluate
TypeError: only list-like objects are allowed to be passed to isin(), you passed a `method`
```

  - 줄 번호는 사람마다 다릅니다.
- `is_missed = ~is_caught` 에서 `~` 를 빼면 오류는 나지 않지만 <mark>**놓친 문제로 알림이 난 문제가 나옵니다.**</mark> 단계 4의 `놓친 문제:` 줄에 P1 · P2 · P3 · P4 가 나오는 것이 이 실수의 모습입니다.

**관제에서는**

- 새 규칙을 운영에 넣기 전에 오탐과 미탐을 세어 전후를 비교하는 것은 흔한 절차입니다. <mark>숫자를 보고서에 한 줄로 남겨 두면 어떤 규칙이 효과가 있었는지 나중에 확인할 수 있습니다.</mark>

---
