---
id: m4-u06-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/106_day04_am_suspicious_logs.md
  mission_id: GichanSource.m4-1105-am-suspicious-logs
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

---

## Exercise 6-1 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise6-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 함수입니다.

① `pick_suspicious` 안

```python
    repeated_names = repeated_users.index             # 반복된 사용자의 이름들(인덱스)을 꺼낸다
    is_repeated_user = users.isin(repeated_names)     # 각 행의 사용자가 반복된 사용자 이름 안에 있는지 구해 True 또는 False 를 만든다
    suspicious = server_failures[is_repeated_user]    # True 인 행만 골라 새 표로 만든다
```

② `judge_failure` 안

```python
    parts = action.split(":")                         # ":" 로 나눠 두 조각의 리스트로 만든다
    is_allowed, reason = check_permission(user, resource, permission_action)  # 3과목(접근통제) 판정 결과를 허용 여부와 이유로 나눠 받는다
    priority = PRIORITY.get(reason, 4)                # 이유의 우선순위를 꺼낸다(없으면 4)
```

내가 채운 코드는 위의 코드입니다. <mark>줄 수가 달라도 주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같고, 서버 실패는 <mark>**9개**</mark>, 먼저 확인할 이벤트는 <mark>**7개**</mark>, 1순위 사용자는 <mark>**dami**</mark> 입니다.

```
--- 단계 1: 판정 서버의 실패 이벤트 9 개
--- 단계 2: 먼저 확인할 실패 이벤트 7 개
--- 단계 3: 우선순위
1 퇴사한 계정 dami SALES:QUERY 2026-11-02 11:02:00
1 퇴사한 계정 dami SALES:QUERY 2026-11-02 11:03:00
1 퇴사한 계정 dami SALES:CHANGE 2026-11-02 11:05:00
1 퇴사한 계정 dami SALES:QUERY 2026-11-02 11:08:00
3 규칙은 허용인데 서버가 거절 gaeun ACCOUNT:CHANGE 2026-11-02 10:05:00
3 규칙은 허용인데 서버가 거절 gaeun ACCOUNT:CHANGE 2026-11-02 10:09:00
3 규칙은 허용인데 서버가 거절 gaeun ACCOUNT:CHANGE 2026-11-02 10:14:00
```

- (나) ① dami 의 실패 4개는 3과목(접근통제) 규칙으로 <mark>「퇴사한 계정」</mark>으로 판정됩니다.
  - 퇴사한 계정이 서버에 4번 요청했다는 것은 <mark>계정이 정리되지 않았다는 뜻이라 1순위</mark>입니다.
  - 실패 4번은 `SALES:QUERY` 3번과 `SALES:CHANGE` 1번이고, 모두 11:02 ~ 11:08 에 있습니다.
- ② gaeun 의 `ACCOUNT:CHANGE` 실패 3개는 규칙으로는 <mark>「허용」</mark>입니다(역할 `account_admin` 에 `ACCOUNT:CHANGE` 가 있습니다).
  - 규칙과 서버의 판단이 어긋난 것이라 <mark>공격이라고 확정할 수 없습니다.</mark>
  - 먼저 서버가 이 요청을 거절한 이유(서버 설정 · 다른 조건)를 확인합니다.
- (다) seoyeon 의 서버 실패는 11:40 `SETTLE:QUERY` 와 18:20 `SALES:CHANGE` 두 번이라 <mark>반복 기준(3번)에 못 미쳐서</mark> 먼저 확인할 이벤트에서 빠졌습니다.
  - 놓칠 수 있는 경우: 11:40 `SETTLE:QUERY`(정산 조회)는 3과목(접근통제) 규칙으로 「권한 없음」이었습니다. 정산처럼 중요한 자원을 권한 없이 건드렸는데 <mark>횟수 기준만 보면 한 번씩이라서 놓칩니다.</mark>
  - 그래서 현업에서는 횟수 기준과 함께 민감한 행동을 따로 보는 규칙을 더합니다.

**왜**

- <mark>거절 기록을 이유별로 다시 판정하면 급한 것부터 읽을 수 있습니다.</mark> 퇴사자 계정은 정리 작업, 권한 없음은 시도 이유 확인, 규칙은 허용인데 거절은 서버 점검으로 해야 할 일이 다릅니다.

**자주 틀리는 곳**

- `isin` 에 `repeated_users` 를 그대로 넣고 `.index` 를 빼면 오류는 나지 않지만 **단계 2가 7개가 아니라 0개로 줄어듭니다.** `repeated_users` 의 값은 횟수이고 사용자 이름은 왼쪽 인덱스에 있어서, 이름을 담은 `.index` 를 넣어야 합니다.
- `.index` 뒤에 괄호를 붙여 `.index()` 라고 쓰면 `TypeError` 오류가 납니다. **`.index` 는 괄호 없이 씁니다.**
  - 실행하면 다음 오류가 납니다(<mark>`'Index' object is not callable`</mark> 이 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise6-1_run.py", line 10, in <module>
    suspicious = pick_suspicious(server_failures)                # 먼저 확인할 실패 이벤트만 골라낸다
  File "…/anomaly_detection/access_detection.py", line 41, in pick_suspicious
    repeated_names = repeated_users.index()  # 반복된 사용자의 이름들(인덱스)을 꺼낸다
TypeError: 'Index' object is not callable
```

  - 줄 번호는 사람마다 다릅니다.

**관제에서는**

- 서버가 거절한 요청을 권한 규칙으로 다시 판정하면, 그 거절이 규칙대로였는지 확인할 수 있습니다. <mark>「규칙은 허용인데 거절」이 반복되면 공격이 아니라 설정 오류일 수 있어,</mark> 점검 대상으로 따로 분류합니다.

---

## Exercise 6-2 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise6-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 함수입니다.

① `find_off_hours_logins` 안

```python
    is_business_hour = hours.between(BUSINESS_START, BUSINESS_END)  # 시가 업무 시간 안인지 구해 True 또는 False 를 만든다
    is_off_hours = ~is_business_hour                  # True 와 False 를 뒤집어 업무 시간 밖인 행을 True 로 만든다
```

② `find_new_ip_users` 안

```python
        has_usual_ip = usual_ip is not None           # 평소 IP 기록이 있는지 구한다
        is_new_ip = ip != usual_ip                    # 이번 IP 가 평소 IP 와 다른지 구한다
        if has_usual_ip and is_new_ip:                # 평소 IP 기록이 있고, 이번 IP 가 평소와 다르면 — 미리 채운 줄
            new_ip_users.append(user)                 # 리스트에 사용자를 추가한다
```

내가 채운 코드는 위의 코드입니다. <mark>줄 수가 달라도 주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같고, 업무 시간 밖 로그인은 <mark>**jiwoo**</mark>, 평소와 다른 IP 는 <mark>**jiwoo · seoyeon**</mark>, 대량 다운로드는 <mark>**seoyeon**</mark> 입니다.

```
--- 단계 1: 업무 시간 밖 로그인 1 건
                  time source   user            ip action result
0  2026-11-02 02:14:08   saas  jiwoo  203.0.113.80  login     실패
--- 단계 2: 평소와 다른 IP 로 로그인한 사용자 ['jiwoo', 'seoyeon']
--- 단계 3: 파일을 5번 이상 내려받은 사용자 ['seoyeon']
```

- (나) <mark>확정할 수 없습니다.</mark>
  - jiwoo 의 02:14 로그인은 실패였고, 같은 날 16:02 에는 평소 IP(198.51.100.52)로 성공했습니다. 다른 IP 에서 실패한 시도가 있었을 뿐이라 <mark>계정이 도용됐다는 근거가 부족합니다.</mark>
  - 더 확인할 정보의 예: 같은 IP(203.0.113.80)가 17:38 에 seoyeon 으로 로그인했으므로, 이 IP 의 다른 활동이 더 있는지 봅니다.
- (다) 제외하지 않으면 gaeun 의 로그인(198.51.100.77)이 「평소와 다른 IP」로 탐지되어 <mark>오탐 알림이 늘어납니다</mark>.
  - 제외하면 다른 사람이 gaeun 계정을 쓰고 있어도 이 규칙으로는 찾지 못하는 <mark>위험이 남습니다</mark>.
  - 그래서 평소 기록을 수집한 뒤에 규칙을 적용합니다.

**왜**

- <mark>세 규칙을 따로 찾아 두면 사용자마다 어떤 기준에 해당하는지 바로 보입니다.</mark> jiwoo 와 seoyeon 은 두 규칙에 해당하고, Unit 7의 Exercise 7-2에서 규칙마다 점수를 더하면 먼저 볼 순서가 정해집니다.

**자주 틀리는 곳**

- `~is_business_hour` 대신 `not is_business_hour` 라고 쓰면 `ValueError` 오류가 납니다. **열에는 `~` 를 씁니다.**
  - 실행하면 다음 오류가 납니다(<mark>`The truth value of a Series is ambiguous`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise6-2_run.py", line 7, in <module>
    off_hours_logins = find_off_hours_logins(logins)             # 업무 시간 밖 로그인만 골라낸다
  File "…/anomaly_detection/saas_detection.py", line 49, in find_off_hours_logins
    is_off_hours = not is_business_hour  # True 와 False 를 뒤집어 업무 시간 밖인 행을 True 로 만든다
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

  - 줄 번호는 사람마다 다릅니다.
- `ip != usual_ip` 대신 `ip == usual_ip` 라고 쓰면 오류는 나지 않지만 **평소 IP 로 로그인한 사용자가 나옵니다.** 단계 2에 junho 가 두 번 나오는 것이 이 실수의 모습입니다.

**관제에서는**

- <mark>규칙 하나마다 알림을 내면 오탐이 쌓여서 담당자가 알림을 무시하게 됩니다.</mark> 해당하는 규칙 수를 점수로 쓰면 먼저 볼 순서를 정할 수 있습니다. Unit 8에서는 오탐과 미탐을 직접 세어 봅니다.

---

## Exercise 6-3 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise6-3_run.py
python advanced_detection.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 함수입니다.

① `find_scan_ips` 안

```python
    actions = web_failures["action"]                  # action 열만 꺼낸다
    is_scanner = actions.str.contains(SCANNER_PATTERN)  # 각 행에 스캐너 경로가 들어 있는지 구해 True 또는 False 를 만든다
    scanner_rows = web_failures[is_scanner]           # True 인 행만 골라 새 표로 만든다
    scan_counts = scanner_rows["ip"].value_counts()   # IP 별로 스캐너 경로를 몇 번 요청했는지 센다
```

② `explain_scan` 안

```python
    reason = "스캐너 경로를 " + str(request_count) + "번 요청"  # 문자열을 연결해 이유 문장을 만든다
    scan_info = {"ip": ip, "reason": reason}          # IP 와 이유를 딕셔너리로 만든다
```

내가 채운 코드는 위의 코드입니다. <mark>줄 수가 달라도 주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같고, 스캔으로 본 IP 는 <mark>**198.51.100.90**</mark> 하나입니다. 이유는 「스캐너 경로를 3번 요청」입니다.

```
--- 단계 1: 웹 서버의 실패 이벤트 13 개
--- 단계 2: 스캐너 경로를 요청한 IP 와 횟수
ip
198.51.100.90    3
Name: count, dtype: int64
--- 단계 3: 스캔으로 본 IP 와 이유
{'ip': '198.51.100.90', 'reason': '스캐너 경로를 3번 요청'}
--- 단계 4: 스캐너 경로가 없어 제외한 IP
203.0.113.50
198.51.100.21
198.51.100.34
198.51.100.77
```

`advanced_detection.py` 의 출력은 다음과 같습니다.

```
판정 서버: 먼저 확인할 실패 이벤트 7 개
SaaS: 업무 시간 밖 ['jiwoo'] · 평소와 다른 IP ['jiwoo', 'seoyeon'] · 대량 다운로드 ['seoyeon']
웹 서버: 스캔으로 본 IP ['198.51.100.90']
```

- (나) 203.0.113.50 은 실패한 요청이 7번(`POST /login` 5번 · `GET /admin` · `GET /admin/users`)이지만 <mark>스캐너 경로가 하나도 없어서</mark> 제외됩니다.
  - 제외하지 않으면 경로 스캔 알림에 로그인과 관리자 화면 실패가 섞여, 담당자가 경로 스캔과 로그인 실패를 구분하기 어려워집니다.
  - 이 IP 는 Unit 4의 로그인 규칙에서 따로 다룬 대상입니다.
- (다) 198.51.100.21 의 `GET /board/99` 는 <mark>`SCANNER_PATTERN` 의 세 경로(`/.env` · `/wp-login` · `/phpmyadmin`) 중 어느 것도 아니라서</mark> `is_scanner` 가 `False` 가 되어 제외됩니다.
  - 해킹 도구가 `/backup.zip` 처럼 목록에 없는 경로를 요청하면 `str.contains` 가 `False` 라서 이 규칙은 놓칩니다. 경로 목록을 정해 두었기 때문에 생기는 한계입니다.
  - 그래서 현업에서는 경로 목록을 새 위협에 맞춰 갱신합니다.

**왜**

- <mark>해킹 도구가 자주 요청하는 경로를 요청한 IP 만 골라 알리면 오타 실패와 섞이지 않습니다.</mark> 대신 목록에 없는 경로는 놓치므로, Unit 8에서 오탐과 미탐을 세면서 확인합니다.

**자주 틀리는 곳**

- `.str.contains` 에서 `.str` 을 빼고 `actions.contains(…)` 라고 쓰면 `AttributeError` 오류가 납니다. **열의 문자열 메서드는 `.str.` 뒤에 씁니다.**
  - 실행하면 다음 오류가 납니다(<mark>`'Series' object has no attribute 'contains'`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise6-3_run.py", line 8, in <module>
    scan_ips, scan_counts = find_scan_ips(web_failures)          # 스캔 IP 와 IP 별 요청 횟수를 찾는다
  File "…/anomaly_detection/malicious_detection.py", line 36, in find_scan_ips
    is_scanner = actions.contains(SCANNER_PATTERN)  # 각 행에 스캐너 경로가 들어 있는지 구해 True 또는 False 를 만든다
AttributeError: 'Series' object has no attribute 'contains'
```

  - 줄 번호는 사람마다 다릅니다.
- 4번에서 `scanner_rows["ip"]` 대신 `web_failures["ip"]` 로 세면 오류는 나지 않지만 **스캐너 경로와 상관없이 모든 IP 가 스캔으로 나옵니다.** 203.0.113.50 이 7번으로 나오는 것이 이 실수의 모습입니다.

**관제에서는**

- 경로 스캔은 대응이 정해져 있는 편입니다(해당 IP 를 막을지 판단). <mark>조건을 정해 오탐을 줄인 알림은 담당자가 근거를 확인할 수 있습니다.</mark>

---

## 정답 마무리

- `ls` 결과에 이번 Unit의 파일들과 `config` 폴더, 이 안내 · 보고서 두 파일이 모두 보이면 됩니다.
- 보고서에 빈 `답:` 이 없으면 됩니다. 못 적은 칸은 `모름 — 막힌 곳: …` 으로 적습니다.
