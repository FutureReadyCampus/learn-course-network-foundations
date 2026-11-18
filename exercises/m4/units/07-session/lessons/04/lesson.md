---
id: m4-u07-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/108_day04_pm_correlation_risk.md
  mission_id: GichanSource.m4-1105-pm-correlation-risk
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답 보는 법

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

---

## 실습 7-1 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise7-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise7-1_run.py` 파이썬으로 실행 파일 실행

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

③ `find_chains` 안

```python
        if has_many_sources and is_close:             # 로그 종류도 충분하고 60분 이내이면 — 미리 채운 줄
            reason = "서로 다른 로그 " + str(source_count) + "종류 · " + str(span) + "분 안"  # 문자열을 연결해 이유 문장을 만든다
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
  - 하나의 사건으로 연결하지 않으면 서버의 `SETTLE:QUERY` 거절(권한 없음)과 실습 6-2에서 본 평소와 다른 IP · 대량 다운로드가 같은 사용자의 기록이라는 점을 <mark>탐지 결과에서 확인하기 어렵습니다.</mark>

**왜**

- <mark>서로 다른 로그와 짧은 시간, 두 조건이 함께 있어야 하나의 사건으로 연결합니다.</mark> 로그 종류만 보면 하루 종일 흩어진 일까지 연결되고, 시간만 보면 한 로그의 반복만 연결됩니다.

**자주 틀리는 곳**

- `pd.concat` 에 표를 쉼표로 따로 전달하면 `TypeError` 오류가 납니다. **표는 대괄호 `[ ]` 안에 넣어 리스트로 전달합니다.**
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`concat() takes 1 positional argument but 3 were given`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise7-1_run.py", line 18, in <module>
    timeline = build_timeline(server_part, saas_part, web_part)  # 세 로그를 합쳐 사용자 · 시각 순으로 정렬한다
  File "…/anomaly_detection/correlation.py", line 45, in build_timeline
    timeline = pd.concat(server_part, saas_part, web_part)  # 세 표를 위아래로 연결해 표 하나로 만든다
TypeError: concat() takes 1 positional argument but 3 were given
```

  - 줄 번호는 사람마다 다릅니다.
- 정렬 결과를 다시 담지 않고 `timeline.sort_values(["user", "time"])` 만 쓰면 오류는 나지 않지만 **정렬한 결과가 사라져서** 단계 2 의 gaeun 이벤트가 시각 순서가 아닙니다(10:14 다음에 10:12 가 아니라 서버 이벤트가 먼저 나옵니다).

**관제에서는**

- <mark>이벤트 하나씩이 아니라 사용자 단위의 사건으로 연결하면 담당자가 읽을 양이 줄어듭니다.</mark> 시간 기준 밖에 있는 이벤트는 따로 두고, 다른 사건과 섞이지 않게 합니다.

---

## 실습 7-2 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise7-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise7-2_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `score_findings` 안

```python
    points = findings_table["rule"].map(WEIGHTS)       # rule 열을 꺼내 바로 규칙마다 점수를 채운다(map)
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
  File "…/anomaly_detection/exercise7-2_run.py", line 11, in <module>
    totals = score_findings(findings)                      # 대상마다 점수를 더한다
  File "…/anomaly_detection/risk_scores.py", line 74, in score_findings
    totals = totals.sort_values(ascending=False)       # 점수가 높은 순으로 정렬한다 — 미리 채운 줄
AttributeError: 'function' object has no attribute 'sort_values'
```

  - 줄 번호는 사람마다 다릅니다.
- `make_grade` 는 **높은 기준부터 차례로 확인합니다.** high 기준을 먼저 확인하고, 아니면 mid 기준을 확인하는 순서입니다. 순서를 바꿔 mid 를 먼저 확인하면 높은 점수도 mid 가 됩니다.

**관제에서는**

- <mark>점수와 등급 기준은 정해 둔 날과 이유를 남깁니다.</mark> 기준을 바꾸면 같은 로그에서 등급이 달라지기 때문입니다. Unit 8에서는 이 등급이 맞았는지 오탐과 미탐을 직접 세어 봅니다.

---

## 정답 확인 후 점검

- (가) 예: 「`git status` 에 `.env` 와 `.venv` 는 보이지 않았다」. 보였다면 `.gitignore` 맨 아래에 한 줄을 적고 저장한 뒤 `git status` 를 다시 쳐서 사라졌는지 확인했다고 적습니다.
- 깃허브의 `anomaly_detection` 폴더에 Unit 6과 Unit 7의 파일이 보이면 됩니다.

---

## 부록 · Unit 6 파일 완성본

Unit 6의 실습 6-1 · 6-2 · 6-3 파일이 없거나 완성하지 못했다면 아래 완성본으로 파일을 만들어 Unit 7을 이어 갑니다. Unit 6에서 직접 풀었다면 이 부분은 건너뜁니다.

**`access_detection.py`** (실습 6-1 완성본)

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다
from rbac import check_permission                     # Module 3(접근통제)에서 만든 권한 판정 함수를 불러온다

EVENTS_PATH = "normalized_events.json"                # 읽을 정규화 이벤트 파일 이름
REPEAT_LIMIT = 3                                      # 한 사용자의 실패가 이 횟수 이상이면 먼저 확인한다
PRIORITY = {"퇴사한 계정": 1, "권한 없음": 2, "허용": 3}  # 판정 이유별로 우선순위(작을수록 먼저)


def load_events(path):                                # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                       # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                     # 이벤트 표를 리턴한다


def pick_server_failures(events):                     # 이벤트 표를 받는 함수
    """판정 서버 로그에서 실패한 이벤트만 골라 새 표로 만든다.
    서버가 거절한 요청을 조사하기 전에 쓴다.
    """
    sources = events["source"]                        # source 열만 꺼낸다
    is_server = sources == "server"                   # 각 행이 판정 서버 이벤트인지 비교해 True 또는 False 를 만든다
    results = events["result"]                        # result 열만 꺼낸다
    is_fail = results == "실패"                       # 각 행이 실패인지 비교해 True 또는 False 를 만든다
    both_true = is_server & is_fail                   # 두 조건이 모두 True 인 행만 True 로 만든다
    server_failures = events[both_true]               # True 인 행만 골라 새 표로 만든다
    return server_failures                            # 서버 실패 이벤트 표를 리턴한다


def pick_suspicious(server_failures):                 # 서버 실패 표를 받는 함수
    """실패가 반복된 사용자의 이벤트만 골라 새 표로 만든다.
    같은 사용자가 여러 번 거절당했는지 볼 때 쓴다.
    """
    users = server_failures["user"]                   # user 열만 꺼낸다
    user_counts = users.value_counts()                # 사용자마다 실패가 몇 번인지 센다
    is_many = user_counts >= REPEAT_LIMIT             # 사용자마다 실패 횟수가 REPEAT_LIMIT 이상인지 비교해 True 또는 False 를 만든다
    repeated_users = user_counts[is_many]             # 반복된 사용자와 횟수만 남긴다

    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. repeated_users 의 .index 를 repeated_names 에 담는다
    repeated_names = repeated_users.index             # 반복된 사용자의 이름들(인덱스)을 꺼낸다
    # 2. users 가 repeated_names 안에 있는지 isin 으로 구해 is_repeated_user 에 담는다
    is_repeated_user = users.isin(repeated_names)     # 각 행의 사용자가 반복된 사용자 이름 안에 있는지 구해 True 또는 False 를 만든다
    # 3. server_failures 에서 is_repeated_user 가 True 인 행만 골라 suspicious 에 담는다
    suspicious = server_failures[is_repeated_user]    # True 인 행만 골라 새 표로 만든다
    return suspicious                                 # 먼저 확인할 실패 이벤트 표를 리턴한다


def judge_failure(user, action):                      # 사용자와 행동을 받는 함수
    """서버가 거절한 요청을 Module 3(접근통제) 권한 규칙으로 다시 판정해 이유와 우선순위를 리턴한다.
    거절이 규칙대로인지 확인할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. action 을 ":" 기준으로 나눠 parts 에 담는다 (예: "SALES:QUERY" → ["SALES", "QUERY"]. 앞 조각이 자원, 뒤 조각이 행위)
    parts = action.split(":")                         # ":" 로 나눠 두 조각의 리스트로 만든다
    resource = parts[0]                               # 첫 번째 조각이 자원이다
    permission_action = parts[1]                      # 두 번째 조각이 행위이다

    # 5. check_permission 에 user, resource, permission_action 을 전달하고, 결과를 is_allowed 와 reason 에 나눠 담는다 (모양: is_allowed, reason = check_permission(...). is_allowed 는 이 문제에서 쓰지 않는다)
    is_allowed, reason = check_permission(user, resource, permission_action)  # Module 3(접근통제) 판정 결과를 허용 여부와 이유로 나눠 받는다
    # 6. PRIORITY 에서 reason 의 순서를 꺼내 priority 에 담는다 (딕셔너리에 없는 이유이면 4 — .get(reason, 4))
    priority = PRIORITY.get(reason, 4)                # 이유의 우선순위를 꺼낸다(없으면 4)
    return reason, priority                           # 판정 이유와 우선순위를 리턴한다
```

**`saas_detection.py`** (실습 6-2 완성본)

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"                # 읽을 정규화 이벤트 파일 이름
USUAL_IPS = {"seoyeon": "198.51.100.9", "junho": "192.0.2.41", "jiwoo": "198.51.100.52"}  # 사용자별 평소 IP. gaeun 은 평소 기록이 없어 넣지 않았다
BUSINESS_START = 8                                    # 업무 시간이 시작하는 시
BUSINESS_END = 20                                     # 업무 시간이 끝나는 시(20시대, 20:59 까지가 업무 시간)
DOWNLOAD_LIMIT = 5                                    # 파일을 이 횟수 이상 내려받으면 대량 다운로드로 본다


def load_events(path):                                # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                       # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                     # 이벤트 표를 리턴한다


def pick_saas(events):                                # 이벤트 표를 받는 함수
    """SaaS 로그의 이벤트만 골라 새 표로 만든다.
    SaaS 이상 사용을 찾기 전에 쓴다.
    """
    sources = events["source"]                        # source 열만 꺼낸다
    is_saas = sources == "saas"                       # 각 행이 SaaS 이벤트인지 비교해 True 또는 False 를 만든다
    saas = events[is_saas]                            # True 인 행만 골라 새 표로 만든다
    return saas                                       # SaaS 이벤트 표를 리턴한다


def pick_logins(saas):                                # SaaS 이벤트 표를 받는 함수
    """로그인 이벤트만 골라 새 표로 만든다.
    로그인 시각과 IP 를 살펴보기 전에 쓴다.
    """
    actions = saas["action"]                          # action 열만 꺼낸다
    is_login = actions == "login"                     # 각 행이 로그인인지 비교해 True 또는 False 를 만든다
    logins = saas[is_login]                           # True 인 행만 골라 새 표로 만든다
    return logins                                     # 로그인 이벤트 표를 리턴한다


def find_off_hours_logins(logins):                    # 로그인 표를 받는 함수
    """업무 시간 밖에 시도한 로그인만 골라 새 표로 만든다.
    새벽 로그인처럼 평소에 없는 시각을 찾을 때 쓴다.
    """
    times = pd.to_datetime(logins["time"])            # 문자열 시각을 시각 값으로 바꾼다 — 미리 채운 줄
    hours = times.dt.hour                             # 시각 값에서 시(0~23)만 꺼낸다 — 미리 채운 줄

    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. hours 가 BUSINESS_START 이상 BUSINESS_END 이하인지 between 으로 구해 is_business_hour 에 담는다
    is_business_hour = hours.between(BUSINESS_START, BUSINESS_END)  # 시가 업무 시간 안인지 구해 True 또는 False 를 만든다
    # 2. is_business_hour 의 반대를 ~ 로 구해 is_off_hours 에 담는다
    is_off_hours = ~is_business_hour                  # True 와 False 를 뒤집어 업무 시간 밖인 행을 True 로 만든다
    off_hours_logins = logins[is_off_hours]           # True 인 행만 골라 새 표로 만든다
    return off_hours_logins                           # 업무 시간 밖 로그인 표를 리턴한다


def find_new_ip_users(logins):                        # 로그인 표를 받는 함수
    """평소와 다른 IP 로 로그인한 사용자를 골라 리스트로 만든다.
    계정을 다른 사람이 쓰는지 의심할 때 쓴다.
    """
    new_ip_users = []                                 # 사용자를 담을 빈 리스트
    login_list = logins.to_dict("records")            # 표를 이벤트 딕셔너리 리스트로 바꾼다
    for login in login_list:                          # 로그인을 하나씩 꺼낸다
        user = login["user"]                          # 그 로그인의 사용자
        ip = login["ip"]                              # 그 로그인의 IP
        usual_ip = USUAL_IPS.get(user)                # 그 사용자의 평소 IP(기록이 없으면 None)
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. usual_ip 가 None 이 아닌지 구해 has_usual_ip 에 담는다 (None 인지는 is None, 아닌지는 is not None)
        has_usual_ip = usual_ip is not None           # 평소 IP 기록이 있는지 구한다
        # 4. ip 가 usual_ip 와 다른지 != 로 구해 is_new_ip 에 담는다 (같은지는 ==, 다른지는 !=)
        is_new_ip = ip != usual_ip                    # 이번 IP 가 평소 IP 와 다른지 구한다
        if has_usual_ip and is_new_ip:                # 평소 IP 기록이 있고, 이번 IP 가 평소와 다르면
            # 5. new_ip_users 에 user 를 추가한다
            new_ip_users.append(user)                 # 리스트에 사용자를 추가한다
    return new_ip_users                               # 평소와 다른 IP 로 로그인한 사용자를 리턴한다


def find_bulk_download_users(saas):                   # SaaS 이벤트 표를 받는 함수
    """파일을 기준 횟수 이상 내려받은 사용자를 리스트로 만든다.
    자료를 한꺼번에 빼 가는 사용자를 찾을 때 쓴다.
    """
    actions = saas["action"]                          # action 열만 꺼낸다
    is_download = actions == "file.download"          # 각 행이 다운로드인지 비교해 True 또는 False 를 만든다
    downloads = saas[is_download]                     # True 인 행만 골라 새 표로 만든다
    counts = downloads.groupby("user").size()         # user 가 같은 행끼리 그룹으로 만들고(groupby) 바로 그룹마다 행이 몇 개인지 센다(size) — 사용자별 다운로드 횟수
    is_bulk = counts >= DOWNLOAD_LIMIT                # 사용자마다 횟수가 기준 이상인지 비교해 True 또는 False 를 만든다
    bulk_counts = counts[is_bulk]                     # 기준 이상인 사용자와 횟수만 남긴다
    bulk_users = list(bulk_counts.index)              # 사용자 이름만 리스트로 만든다
    return bulk_users                                 # 대량 다운로드 사용자를 리턴한다
```

**`malicious_detection.py`** (실습 6-3 완성본)

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"                # 읽을 정규화 이벤트 파일 이름
SCANNER_PATTERN = "/.env|/wp-login|/phpmyadmin"       # 스캐너가 자주 요청하는 경로. | 는 「또는」이라는 뜻이다


def load_events(path):                                # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                       # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                     # 이벤트 표를 리턴한다


def pick_web_failures(events):                        # 이벤트 표를 받는 함수
    """웹 서버 로그에서 실패한 이벤트만 골라 새 표로 만든다.
    경로 스캔 요청을 찾기 전에 쓴다.
    """
    sources = events["source"]                        # source 열만 꺼낸다
    is_web = sources == "web"                         # 각 행이 웹 서버 이벤트인지 비교해 True 또는 False 를 만든다
    results = events["result"]                        # result 열만 꺼낸다
    is_fail = results == "실패"                       # 각 행이 실패인지 비교해 True 또는 False 를 만든다
    both_true = is_web & is_fail                      # 두 조건이 모두 True 인 행만 True 로 만든다
    web_failures = events[both_true]                  # True 인 행만 골라 새 표로 만든다
    return web_failures                               # 웹 실패 이벤트 표를 리턴한다


def find_scan_ips(web_failures):                      # 웹 실패 표를 받는 함수
    """스캐너가 요청하는 경로를 요청한 IP 와 요청 횟수를 찾는다.
    한 번의 오타 요청이나 로그인 실패만 있는 IP 를 거르고 경로 스캔만 가려낼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. web_failures 의 "action" 열을 꺼내 actions 에 담는다
    actions = web_failures["action"]                  # action 열만 꺼낸다
    # 2. actions 에 .str.contains(SCANNER_PATTERN) 을 붙여 스캐너 경로가 들어 있는지 구해 is_scanner 에 담는다
    is_scanner = actions.str.contains(SCANNER_PATTERN)  # 각 행에 스캐너 경로가 들어 있는지 구해 True 또는 False 를 만든다
    # 3. web_failures 에서 is_scanner 가 True 인 행만 골라 scanner_rows 에 담는다
    scanner_rows = web_failures[is_scanner]           # True 인 행만 골라 새 표로 만든다
    # 4. scanner_rows 의 "ip" 열에 .value_counts() 를 붙여 IP 별로 몇 번 요청했는지 세어 scan_counts 에 담는다
    scan_counts = scanner_rows["ip"].value_counts()   # IP 별로 스캐너 경로를 몇 번 요청했는지 센다
    scan_ips = list(scan_counts.index)                # 스캔으로 보는 IP 이름만 리스트로 만든다
    return scan_ips, scan_counts                      # 스캔 IP 리스트와 IP 별 요청 횟수를 리턴한다


def explain_scan(ip, request_count):                  # IP 와 스캐너 경로 요청 횟수를 받는 함수
    """스캔으로 본 IP 하나를 담당자가 읽을 설명 딕셔너리로 만든다.
    왜 의심했는지 이유를 알림에 남길 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. "스캐너 경로를 " 와 str(request_count) 와 "번 요청" 을 + 로 연결해 reason 에 담는다 (문구는 복사해 붙여도 된다)
    reason = "스캐너 경로를 " + str(request_count) + "번 요청"  # 문자열을 연결해 이유 문장을 만든다
    # 6. 키 "ip" 에 ip, 키 "reason" 에 reason 을 담은 딕셔너리를 scan_info 에 담는다
    scan_info = {"ip": ip, "reason": reason}          # IP 와 이유를 딕셔너리로 만든다
    return scan_info                                  # 설명 딕셔너리를 리턴한다
```
