---
id: m3-u09-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/092_day05_pm_conditions.md
  mission_id: GichanSource.m3-1030-pm-conditions
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## 정답 5-1

💻 **터미널에 입력합니다.**

```bash
pwd
python day05_5-1_run.py
```

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수입니다.

① `is_work_time` 안

```python
    start_hour, end_hour = rule["hours"]                                   # 허용 시작 시와 끝 시를 꺼낸다
    hour = now.hour                                              # 요청 시각의 시를 꺼낸다
    return start_hour <= hour < end_hour                                   # 시작 시 이상이고 끝 시 미만인지(True 또는 False)를 리턴한다
```

② `is_allowed_network` 안

```python
    allowed_networks = rule["networks"]                          # 허용된 접속 위치 리스트를 꺼낸다
    return network in allowed_networks                           # 그 리스트에 들어 있는지(True 또는 False)를 리턴한다
```

③ `evaluate_conditional` 안(미리 채운 `if rule["permission"] == permission:` 아래)

```python
            if not is_work_time(rule, now):                      # 업무 시간 안이 아니면
                return False, "업무 시간 밖"                       # 거부한다
            if not is_allowed_network(rule, network):            # 허용된 접속 위치가 아니면
                return False, "허용되지 않은 접속 위치"            # 거부한다
```

**결과**

- (가) 출력은 다음과 같고, 허용은 **3건**(1 · 2 · 6번), 거부는 **5건**입니다.
  - 조건 때문에 거부된 요청은 **4건**(3 · 4 · 5 · 7번)이고, 8번은 기본 판정에서 퇴사한 계정으로 거부됐습니다.

```
--- 단계 1: 판정 - 요청 8 건
1 seoyeon SALES:QUERY office 10:00 -> 허용(역할 권한)
2 seoyeon SALES:CHANGE office 09:00 -> 허용(역할 권한)
3 seoyeon SALES:CHANGE office 18:00 -> 거부(업무 시간 밖)
4 seoyeon SALES:CHANGE external 10:00 -> 거부(허용되지 않은 접속 위치)
5 seoyeon SALES:CHANGE external 22:00 -> 거부(업무 시간 밖)
6 junho SETTLE:QUERY vpn 19:30 -> 허용(역할 권한)
7 gaeun ACCOUNT:CHANGE vpn 10:00 -> 거부(허용되지 않은 접속 위치)
8 dami SALES:QUERY office 10:00 -> 거부(퇴사한 계정)
--- 단계 2: 확인 - 조건 파일에 적힌 조건
SALES:CHANGE | 9시부터 18시 전까지 | office, vpn
SETTLE:QUERY | 8시부터 20시 전까지 | office, vpn
ACCOUNT:CHANGE | 9시부터 18시 전까지 | office
```

- (나) 정상 사용자에게는 어긋난 조건을 모두 알려 주는 쪽이 낫습니다.
  - 한 번에 무엇을 고쳐야 하는지 알 수 있기 때문입니다.
  - 계정을 가로챈 사람에게는 이유를 하나만 알려 주는 쪽이 낫습니다.
  - 어떤 조건이 걸려 있는지 덜 알려 주기 때문입니다.
  - 두 경우가 서로 반대라서, 실제 서비스에서는 요청한 사람에게 보내는 응답에는 이유를 줄이고 서버 로그에는 어긋난 조건을 모두 남기는 방법을 많이 씁니다.
  - 관제 담당자에게는 어긋난 조건을 **모두** 아는 쪽이 낫습니다.
  - 어긋난 조건이 여러 개인 요청이 몇 건인지 세면 평소와 다른 접속이 얼마나 되는지 볼 수 있기 때문입니다.
  - 오늘 만든 코드는 첫 번째 이유만 리턴하므로, 모두 알리려면 코드를 바꿔야 합니다.
- (다) 권한이 있어도 계정을 다른 사람이 가로챘다면 그 요청은 정상 사용자가 보낸 것이 아닙니다.
  - 로그인할 때 한 번만 확인하면 가로챈 계정이 새벽 2시에 외부에서 들어와도 막지 못하고, 쓰기 권한이 있는 데이터까지 바꿀 수 있습니다.
  - 요청마다 시간과 접속 위치를 확인하면(서버가 그 값을 직접 알아낼 수 있을 때) 평소와 다른 접속을 바로 막을 수 있습니다.

**왜**

- 권한이 있다는 것만으로 모든 요청을 믿지 않고, 요청마다 조건을 함께 봅니다.
  - 기본 판정이 거부이면 조건을 볼 필요가 없어서 먼저 확인하고 바로 끝냅니다.
  - 조건은 파일에 두어서 업무 시간이 바뀌어도 코드를 고치지 않습니다.

**자주 틀리는 곳**

- `is_work_time` 의 끝 시각 비교를 `hour < end` 대신 `hour <= end` 로 쓰면 18시 정각 요청도 허용됩니다.
  - 오류는 나지 않고 결과만 달라집니다.
  - 실행하면 다음처럼 됩니다(3번 줄 18:00 요청이 허용으로 나오면 이 실수입니다).

```
--- 단계 1: 판정 - 요청 8 건
1 seoyeon SALES:QUERY office 10:00 -> 허용(역할 권한)
2 seoyeon SALES:CHANGE office 09:00 -> 허용(역할 권한)
3 seoyeon SALES:CHANGE office 18:00 -> 허용(역할 권한)
…
```

**관제에서는**

- 접근 제어 서비스는 사용자를 확인한 뒤에도 접속 시간, 위치, 기기 상태를 요청마다 다시 확인하고, 평소와 다른 요청은 한 번 더 확인하거나 막습니다.
  - 오늘 단순화한 부분은 두 가지입니다.
  - 첫째, 실습에서는 접속 위치(`network`)와 시각(`time`)을 요청하는 쪽이 적어 보내지만, 실제 서비스는 서버에 접속해 온 쪽의 주소(IP)와 서버 시계로 직접 알아냅니다.
  - 둘째, 조건 파일을 읽지 못하면 오늘 코드는 조건 없이 모두 허용하는데, 실제 서비스는 읽지 못하면 서버를 켜지 않거나 모두 거부하는 쪽으로 만듭니다.

---

## 정답 6-1

💻 **터미널에 입력합니다.**

터미널 1:

```bash
pwd
python access_server.py
```

터미널 2:

```bash
cd access_control
pwd
python send_checks.py
```

**채운 코드** (한 예) — 직접 쓰는 곳은 세 함수의 다섯 군데입니다.

① `parse_time` 안(미리 채운 `try` 아래)

```python
        return datetime.strptime(text, TIME_FORMAT)              # 문자열을 시각으로 바꿔 리턴한다
```

② `parse_time` 안(미리 채운 `except` 아래)

```python
        return None                                              # 모양이 틀렸으면 없다고 알린다
```

③ `write_log` 안(`with` 위)

```python
    mode = "a"                                                   # 파일을 여는 모드: 덧붙이기("a")
```

④ `check` 안(미리 채운 400 처리 아래)

```python
    allowed, reason = evaluate_conditional(user, resource, action, network, now, RULES)   # 조건까지 판정한다
```

⑤ `check` 안(미리 채운 `write_log` 줄 아래)

```python
    if allowed:                                                  # 허용이면
        return {"allowed": True, "reason": reason}, 200          # 상태 코드 200 으로 답한다
    return {"allowed": False, "reason": reason}, 403             # 거부이면 상태 코드 403 으로 답한다
```

**결과**

- (가) 출력은 다음과 같고, 상태 코드는 200 이 **3건**(1 · 4 · 5번), 403 이 **5건**(2 · 3 · 6 · 7 · 8번), 400 이 **1건**(9번)입니다.
  - 서버가 남긴 로그는 **8줄**입니다(400 요청은 기록하지 않습니다).

```
--- 단계 1: 응답 - 요청 9 건
1 seoyeon SALES:CHANGE -> 200 역할 권한
2 seoyeon SALES:CHANGE -> 403 업무 시간 밖
3 seoyeon SALES:CHANGE -> 403 허용되지 않은 접속 위치
4 seoyeon SALES:QUERY -> 200 역할 권한
5 junho SETTLE:QUERY -> 200 역할 권한
6 junho SETTLE:QUERY -> 403 허용되지 않은 접속 위치
7 gaeun ACCOUNT:CHANGE -> 403 허용되지 않은 접속 위치
8 dami SALES:QUERY -> 403 퇴사한 계정
9 seoyeon SALES:CHANGE -> 400 입력이 잘못됨
--- 단계 2: 로그 - 서버가 남긴 8 줄
seoyeon SALES:CHANGE office 2026-10-30T09:00 -> True 역할 권한
seoyeon SALES:CHANGE office 2026-10-30T18:00 -> False 업무 시간 밖
seoyeon SALES:CHANGE external 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
seoyeon SALES:QUERY external 2026-10-30T23:00 -> True 역할 권한
junho SETTLE:QUERY vpn 2026-10-30T19:30 -> True 역할 권한
junho SETTLE:QUERY external 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
gaeun ACCOUNT:CHANGE vpn 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
dami SALES:QUERY office 2026-10-30T10:00 -> False 퇴사한 계정
--- 단계 3: 대조 - 판정까지 간 응답과 로그
판정까지 간 응답 8 건 / 로그에 남은 줄 8 줄
```

- (나) 403 은 요청이 제대로 도착했고 서버가 판정(인가)까지 마친 뒤 거부했다는 뜻이라, 같은 요청을 다시 보내도 결과가 같습니다.
  - 400 은 요청 자체가 잘못됐다는 뜻이라, 값을 고쳐 다시 보내면 결과가 달라질 수 있습니다.
  - 요청을 보내는 쪽이 둘을 구별하면 400 이면 자기 프로그램의 오류로 보고 고치고, 403 이면 접근 거부로 처리할 수 있습니다.
  - 구별하지 않으면 거부를 입력 오류로 오해해 같은 요청을 계속 다시 보내거나, 입력 오류를 거부로 오해해 방치하게 됩니다.
- (다) `"w"` 로 열면 요청이 올 때마다 파일이 새로 써져서 앞의 기록이 지워지고 마지막 한 건만 남습니다.
  - 한 달 뒤에 지난주 거부 기록을 찾으면 그 기록은 이미 없습니다.
  - 로그는 시간이 지나도 앞의 기록이 남아 있어야 하므로 끝에 덧붙이는 `"a"` 방식이 알맞습니다.
  - 한 줄에 한 건씩 쓰면 파일이 아무리 커져도 한 줄씩 읽어 처리할 수 있습니다.

**왜**

- 판정을 서버로 만들어 주소로 요청하게 하면 여러 프로그램이 같은 규칙으로 물을 수 있습니다.
  - 상태 코드로 허용(200) · 거부(403) · 잘못된 요청(400)을 숫자로 구별해 알려 주고, 요청마다 한 줄씩 로그를 남겨 나중에 볼 수 있게 합니다.
  - 응답과 서버 로그를 세어 맞춰 보면 판정까지 간 요청이 빠짐없이 로그에 남았는지 알 수 있습니다.
  - 입력 오류(400)가 로그에 없다는 점도 이 대조로 알 수 있습니다.

**자주 틀리는 곳**

- 거부 응답의 상태 코드를 `403` 대신 `200` 으로 쓰면 화면에 보이는 내용은 같아서 알아채기 어렵습니다.
  - 하지만 상태 코드만 보는 프로그램은 거부를 허용으로 오해합니다.
  - 실행하면 다음처럼 됩니다(거부 요청인데 `->` 뒤 숫자가 `200` 이면 이 실수입니다).

```
--- 단계 1: 응답 - 요청 9 건
1 seoyeon SALES:CHANGE -> 200 역할 권한
2 seoyeon SALES:CHANGE -> 200 업무 시간 밖
3 seoyeon SALES:CHANGE -> 200 허용되지 않은 접속 위치
4 seoyeon SALES:QUERY -> 200 역할 권한
5 junho SETTLE:QUERY -> 200 역할 권한
6 junho SETTLE:QUERY -> 200 허용되지 않은 접속 위치
7 gaeun ACCOUNT:CHANGE -> 200 허용되지 않은 접속 위치
8 dami SALES:QUERY -> 200 퇴사한 계정
9 seoyeon SALES:CHANGE -> 400 입력이 잘못됨
--- 단계 2: 로그 - 서버가 남긴 8 줄
seoyeon SALES:CHANGE office 2026-10-30T09:00 -> True 역할 권한
seoyeon SALES:CHANGE office 2026-10-30T18:00 -> False 업무 시간 밖
seoyeon SALES:CHANGE external 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
seoyeon SALES:QUERY external 2026-10-30T23:00 -> True 역할 권한
junho SETTLE:QUERY vpn 2026-10-30T19:30 -> True 역할 권한
junho SETTLE:QUERY external 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
gaeun ACCOUNT:CHANGE vpn 2026-10-30T10:00 -> False 허용되지 않은 접속 위치
dami SALES:QUERY office 2026-10-30T10:00 -> False 퇴사한 계정
--- 단계 3: 대조 - 판정까지 간 응답과 로그
판정까지 간 응답 8 건 / 로그에 남은 줄 8 줄
```

**관제에서는**

- 판정 서버는 요청 로그를 지우지 않고 보관하고, 거부(403)가 갑자기 늘면 담당자에게 알립니다.
  - 400 도 따로 기록해 두어야 많아졌는지 알 수 있습니다.
  - 서버가 요청을 받은 시각은 서버가 직접 적어야 하고(지금은 요청한 쪽이 보낸 `time` 을 그대로 씁니다), 입력 오류 요청도 따로 기록해서 공격 시도를 찾는 데 씁니다.

---

## 정답 마무리

💻 **터미널에 입력합니다.**

```bash
cd ..
pwd
git status
```

`.env` 나 `.venv` 가 없는 것을 확인한 뒤에 아래를 칩니다.

```bash
git add .
git commit -m "Add access control day 5 revocation, conditional policy and check server"
git push
```

**결과**

- (가) 한 예: 「줄이 열아홉 개였고(`.py` 열한 개 + `.json` 세 개 + `server_log.jsonl` 한 개 + `.md` 네 개), `.env` · `.venv` 는 없었다」. 이 숫자는 어제(10/29(목))까지 올렸고 `__pycache__` 가 보이지 않을 때의 숫자이며, 줄 수와 이름은 학생마다 다를 수 있습니다.
  - `.env` 나 `.venv` 가 보였다면 `.gitignore` 에 한 줄을 적고 `git status` 를 다시 쳤다고 적습니다.

**왜**

- 올리기 전에 올라갈 파일을 확인해야 비밀 키가 섞이지 않습니다.
  - 코드와 오늘 서버가 남긴 `server_log.jsonl` 이 함께 올라가야 11/2(월) 수업이 같은 로그에서 시작합니다.

**자주 틀리는 곳**

- `.env` 가 보이는데 그대로 `git add .` 를 하는 실수가 가장 위험합니다.
  - `cd ..` 를 두 번 쳐서 `security-agent-toolkit` 바깥으로 나가는 경우도 있습니다.
  - `pwd` 로 확인합니다.

**관제에서는**

- 서버 코드와 그 서버가 남긴 로그는 같은 커밋에 함께 올려, 어느 코드로 어떤 요청을 처리했는지 이력으로 남깁니다.

---

## 앞 교시 파일 완성본

앞 교시 파일이 없거나 잘 안 될 때 이 코드로 만듭니다.

**`config/conditions.json`** (5교시 완성본)

```json
[
  {"permission": "SALES:CHANGE", "hours": [9, 18], "networks": ["office", "vpn"]},
  {"permission": "SETTLE:QUERY", "hours": [8, 20], "networks": ["office", "vpn"]},
  {"permission": "ACCOUNT:CHANGE", "hours": [9, 18], "networks": ["office"]}
]
```

**`conditional.py`** (5교시 완성본)

```python
from config_loader import load_json                              # 10/22(목)에 만든 안전한 읽기 함수를 불러온다
from policy import evaluate_access                               # 10/22(목)에 만든 기본 판정 함수를 불러온다


def load_rules(path):                                            # 조건 파일 경로를 받는 함수
    """조건 파일을 읽어 조건 딕셔너리 리스트를 리턴하고, 파일이 없거나 깨졌으면 빈 리스트를 리턴한다.
    판정 서버가 시작할 때 업무 시간 · 접속 위치 조건을 불러오는 데 쓴다.
    """
    return load_json(path, [])                                   # 안전하게 읽는다(못 읽으면 두 번째 값인 빈 리스트를 리턴한다)


def is_work_time(rule, now):                                     # 조건 한 건과 요청 시각(datetime)을 받는 함수
    """요청 시각의 시가 허용 시간대 안이면 True, 밖이면 False 를 리턴한다.
    끝 시각은 포함하지 않는다.
    업무 시간 밖의 요청을 막을 때 쓴다.
    """
    start_hour, end_hour = rule["hours"]                                   # 허용 시작 시와 끝 시를 꺼낸다
    hour = now.hour                                              # 요청 시각의 시를 꺼낸다
    return start_hour <= hour < end_hour                                   # 시작 시 이상이고 끝 시 미만인지(True 또는 False)를 리턴한다


def is_allowed_network(rule, network):                           # 조건 한 건과 접속 위치를 받는 함수
    """접속 위치가 조건의 허용 위치에 들어 있으면 True, 아니면 False 를 리턴한다.
    사내망 · VPN 에서 온 요청만 허용할 때 쓴다.
    """
    allowed_networks = rule["networks"]                          # 허용된 접속 위치 리스트를 꺼낸다
    return network in allowed_networks                           # 그 리스트에 들어 있는지(True 또는 False)를 리턴한다


def evaluate_conditional(user, resource, action, network, now, rules):   # 사용자 · 자원 · 행위 · 접속 위치 · 요청 시각(datetime) · 조건 리스트를 받는 함수
    """(허용 여부, 이유)를 리턴한다.
    기본 판정이 허용이어도 업무 시간 · 접속 위치 조건에 어긋나면 거부한다.
    새벽 · 외부 접속을 막을 때 쓴다.
    """
    is_allowed, reason = evaluate_access(user, resource, action, now)    # 먼저 10/22(목)의 기본 판정을 한다
    if not is_allowed:                                                   # 기본 판정이 거부이면
        return False, reason                                     # 그 이유로 바로 거부한다
    permission = f"{resource}:{action}"                          # "자원:행위" 모양 문자열로 합친다
    for rule in rules:                                           # 조건을 하나씩 꺼낸다
        if rule["permission"] == permission:                     # 이 권한에 걸린 조건이면
            if not is_work_time(rule, now):                      # 업무 시간 안이 아니면
                return False, "업무 시간 밖"                       # 거부한다
            if not is_allowed_network(rule, network):            # 허용된 접속 위치가 아니면
                return False, "허용되지 않은 접속 위치"            # 거부한다
    return True, reason                                          # 어긋나는 조건이 없으면 기본 판정의 이유로 허용한다
```

**`access_server.py`** (6교시 완성본)

```python
import json                                                      # JSON 문자열을 만드는 모듈을 불러온다
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from flask import Flask, request                                 # 서버를 만드는 Flask 와 요청 정보를 담은 request 를 불러온다
from conditional import load_rules, evaluate_conditional         # 5교시에 만든 조건 판정 함수를 불러온다

app = Flask(__name__)                                            # 서버 프로그램을 만든다
app.json.ensure_ascii = False                                    # 응답의 한글이 \uXXXX 로 깨지지 않게 한다
RULES = load_rules("config/conditions.json")                     # 조건 파일을 서버를 켤 때 한 번 읽는다
LOG_PATH = "server_log.jsonl"                                    # 요청 로그를 남길 파일 이름
TIME_FORMAT = "%Y-%m-%dT%H:%M"                                   # 주소로 받는 시각 문자열의 형식(예: 2026-10-30T10:00)


def parse_time(text):                                            # 시각 문자열을 받는 함수
    """2026-10-30T10:00 모양 문자열을 시각으로 바꾼다.
    없거나 모양이 틀리면 None 을 리턴한다.
    판정 서버가 요청 시각을 읽을 때 쓴다.
    """
    if text is None:                                             # 시각 문자열이 아예 없으면
        return None                                              # 없다고 알린다
    try:                                                         # 아래를 시도한다
        return datetime.strptime(text, TIME_FORMAT)              # 문자열을 시각으로 바꿔 리턴한다
    except ValueError:                                           # 모양이 틀렸으면
        return None                                              # 없다고 알린다


def write_log(entry):                                            # 로그에 쓸 딕셔너리를 받는 함수
    """딕셔너리 한 개를 JSON 한 줄로 만들어 로그 파일 끝에 덧붙인다.
    판정 서버가 요청마다 기록을 남길 때 쓴다.
    """
    mode = "a"                                                   # 파일을 여는 모드: 덧붙이기("a")
    with open(LOG_PATH, mode, encoding="utf-8") as log_file:            # 파일을 mode(덧붙이기 모드)로 연다
        text = json.dumps(entry, ensure_ascii=False)             # 딕셔너리를 JSON 문자열로 만든다(한글은 그대로)
        log_file.write(text + "\n")                                     # 한 줄로 파일 끝에 쓴다


@app.route("/check")                                             # 주소 /check 로 오는 요청을 아래 함수가 받는다
def check():                                                     # 요청 한 건을 처리하는 함수
    """주소의 값으로 판정해 허용이면 200, 거부이면 403, 값이 빠졌으면 400 으로 답한다.
    판정 서버가 요청을 받을 때마다 쓴다.
    """
    user = request.args.get("user")                              # 요청 주소에서 user 값을 꺼낸다(주소에 없으면 None)
    resource = request.args.get("resource")                      # 요청 주소에서 resource 값을 꺼낸다
    action = request.args.get("action")                          # 요청 주소에서 action 값을 꺼낸다
    network = request.args.get("network")                        # 요청 주소에서 network 값을 꺼낸다
    time_text = request.args.get("time")                         # 요청 주소에서 time 값을 꺼낸다(없으면 None)
    now = parse_time(time_text)                                  # 시각으로 바꾼다(없거나 모양이 틀리면 None)
    if None in (user, resource, action, network, now):           # 빠졌거나 모양이 틀린 값이 하나라도 있으면
        return {"allowed": False, "reason": "입력이 잘못됨"}, 400   # 요청이 잘못됐다는 상태 코드 400 으로 답한다
    allowed, reason = evaluate_conditional(user, resource, action, network, now, RULES)   # 조건까지 판정한다
    log_entry = {                                                 # 로그 한 줄에 담을 값을 묶는다(여러 줄)
        "time": request.args.get("time"),                        # 시각
        "user": user,                                            # 사용자
        "permission": f"{resource}:{action}",                    # 권한
        "network": network,                                      # 접속 위치
        "allowed": allowed,                                      # 허용 여부
        "reason": reason,                                        # 이유
    }
    write_log(log_entry)                                         # 요청 로그를 한 줄 덧붙인다
    if allowed:                                                  # 허용이면
        return {"allowed": True, "reason": reason}, 200          # 상태 코드 200 으로 답한다
    return {"allowed": False, "reason": reason}, 403             # 거부이면 상태 코드 403 으로 답한다

if __name__ == "__main__":                                       # 이 파일을 직접 실행했을 때만
    app.run(port=5001)                                           # 5001번 포트로 서버를 켠다
```
