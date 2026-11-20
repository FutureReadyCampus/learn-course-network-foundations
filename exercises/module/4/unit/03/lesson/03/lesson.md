---
id: m4-u03-l03
title: 실습 3-2 · 반복 거절 찾고 이유별 순서 정하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/106_day04_am_suspicious_logs.md
  mission_id: GichanSource.m4-1105-am-suspicious-logs
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 3-2 · 반복 거절 찾고 이유별 순서 정하기

## 이번 의뢰: 반복 거절과 거절 이유

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「11/2 에 판정 서버가 요청을 거절한 기록이 9건 있습니다. 판정 서버는 사용자가 누른 기능을 허용할지 정하는 서버입니다. 로그에는 `실패` 라고만 적혀 있어서 왜 거절했는지 알 수 없고, 9건을 하나씩 열어 볼 시간도 없습니다.
>
> 같은 사람이 여러 번 거절당한 기록부터 확인하고 싶습니다. Module 3에서 만든 권한 규칙으로 거절 이유도 붙여 주세요. 퇴사한 사람의 계정이면 가장 먼저 알려 주세요. 거절이 전부 문제는 아니니 공격이라고 단정하지는 말아 주세요.」
> - **왜 중요한가**: <mark>거절 이유를 알아야 퇴사한 계정을 정리할지, 서버 설정을 확인할지 정할 수 있습니다.</mark>

## 왜 거절 이유로 순서를 정하는가

1. 판정 서버는 요청을 거절할 때마다 `실패` 로 기록합니다. 실습 2-3 에서는 웹 서버의 로그인 실패를 확인했습니다. 이번 실습에서는 **판정 서버 로그**의 거절 기록을 확인합니다.
2. 이번 실습에서 먼저 확인할 거절은 <mark>**한 사용자가 3번 이상 거절당한 기록**</mark>입니다. 질문은 이것 하나입니다.
3. Module 3의 권한 규칙(`check_permission`)으로 같은 요청을 다시 판정하면 **거절 이유**가 나옵니다. <mark>이유에 따라 할 일이 다릅니다.</mark>

| 거절 이유 | 뜻 | 할 일 | 순서 |
|---|---|---|---|
| 퇴사한 계정 | 퇴사했는데 계정이 남아 있음 | 계정 정리 | **1** |
| 권한 없음 | 그 역할에 허용되지 않은 행동을 요청함 | 요청한 이유 확인 | 2 |
| 허용 | 규칙으로는 허용인데 서버가 거절함 | 서버 설정 확인(공격이라고 확정할 수 없음) | 3 |

## 1.1 먼저 확인할 거절

판정 서버 로그의 실패 9개입니다(샘플에서 `source` 가 `server` 이고 `result` 가 `실패` 인 이벤트).

**먼저 확인할 질문은 하나입니다.**

| 질문 | 「예」가 되는 때 |
|---|---|
| 그 사용자의 실패가 3번 이상인가? | 그날 그 사용자의 판정 서버 실패가 3번 이상입니다(`REPEAT_LIMIT` = 3). 행동의 종류와 상관없이 실패 횟수만 셉니다. |

- <mark>**「예」이면 먼저 확인합니다.**</mark> 「아니오」이면 이번에는 뺍니다.

| 시각 | 사용자 | 행동 | 그 사용자의 실패 횟수 | 먼저 확인 |
|---|---|---|---|---|
| 10:05 | gaeun | `ACCOUNT:CHANGE` | 3번 | **예** |
| 10:09 | gaeun | `ACCOUNT:CHANGE` | 3번 | **예** |
| 10:14 | gaeun | `ACCOUNT:CHANGE` | 3번 | **예** |
| 11:02 | dami | `SALES:QUERY` | 4번 | **예** |
| 11:03 | dami | `SALES:QUERY` | 4번 | **예** |
| 11:05 | dami | `SALES:CHANGE` | 4번 | **예** |
| 11:08 | dami | `SALES:QUERY` | 4번 | **예** |
| 11:40 | seoyeon | `SETTLE:QUERY` | 2번 | 아니오 |
| 18:20 | seoyeon | `SALES:CHANGE` | 2번 | 아니오 |

- 먼저 확인할 기록은 **7개**(gaeun 3 + dami 4)이고, seoyeon 의 2건만 빠집니다.
- 7개를 Module 3 규칙으로 판정하면 dami 는 「퇴사한 계정」으로 1순위, gaeun 은 「허용」으로 3순위입니다.
- 이 판정은 거절이 규칙대로였는지 확인하는 것이고, **공격이라고 확정하는 것이 아닙니다.**

**판다스 문법 상자 — 목록에 있는 사용자인지 `isin`**

**<mark>`열.isin(리스트)`</mark> 는 열의 값이 리스트 안에 있으면 `True`, 없으면 `False` 를 줍니다**

아래는 로그인 기록입니다. 퇴사한 사용자를 차단 목록(`blocked_users`)에 적어 두었습니다. 이 목록에 있는 사용자의 기록만 찾아봅니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                    # 표에 넣을 내용(열 이름: 값들)
    "user": ["gaeun", "dami", "seoyeon", "junho", "dami"],  # user 열
    "result": ["성공", "실패", "성공", "실패", "실패"],     # result 열
}
df = pd.DataFrame(data)                                     # 내용으로 표(DataFrame)를 만든다
print(df)                                                   # 표를 출력한다
```

실행 결과:

```
      user result
0    gaeun     성공
1     dami     실패
2  seoyeon     성공
3    junho     실패
4     dami     실패
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
blocked_users = ["dami", "junho"]            # 차단한 사용자 두 명을 리스트에 담는다
is_blocked = df["user"].isin(blocked_users)  # user 열의 각 값이 차단 목록에 있는지 확인한다
print(is_blocked)                            # True · False 를 출력한다
```

실행 결과:

```
0    False
1     True
2    False
3     True
4     True
Name: user, dtype: bool
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
blocked_df = df[is_blocked]  # True 인 행만 남긴다
print(blocked_df)            # 차단된 사용자의 기록을 출력한다
```

실행 결과:

```
    user result
1   dami     실패
3  junho     실패
4   dami     실패
```

- 읽는 법: 첫 번째 출력은 입력 표입니다. <mark>두 번째 출력에서 1번 행(dami) · 3번 행(junho) · 4번 행(dami)이 `True`</mark> 입니다. 세 번째 출력은 그 세 기록만 남은 표입니다. `Name: user, dtype: bool` 줄은 몰라도 됩니다.

**판다스 문법 상자 — 센 결과에서 이름만 꺼내기 `.index`**

**<mark>`센 결과.index`</mark> 는 `value_counts()` 로 센 결과에서 왼쪽에 나오는 이름들(인덱스)을 꺼냅니다. 사용자별로 센 결과라면 사용자 이름이 나옵니다**

아래는 로그인에 실패한 기록입니다. 사용자별 실패 횟수를 센 뒤, 2번 이상 실패한 사용자의 이름만 꺼냅니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                            # 표에 넣을 내용(열 이름: 값들)
    "user": ["dami", "gaeun", "dami", "seoyeon", "dami", "gaeun"],  # user 열
    "result": ["실패", "실패", "실패", "실패", "실패", "실패"],     # result 열
}
df = pd.DataFrame(data)                                             # 내용으로 표(DataFrame)를 만든다
print(df)                                                           # 표를 출력한다
```

실행 결과:

```
      user result
0     dami     실패
1    gaeun     실패
2     dami     실패
3  seoyeon     실패
4     dami     실패
5    gaeun     실패
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
counts = df["user"].value_counts()  # 같은 사용자가 몇 번 나왔는지 센다
print(counts)                       # 사용자(인덱스)와 실패 횟수를 출력한다
```

실행 결과:

```
user
dami       3
gaeun      2
seoyeon    1
Name: count, dtype: int64
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
many = counts[counts >= 2]  # 2번 이상인 사용자만 남긴다
names = list(many.index)    # 남은 결과의 인덱스(사용자 이름)만 꺼내 리스트로 만든다
print(names)                # 이름 리스트를 출력한다
```

실행 결과:

```
['dami', 'gaeun']
```

- 읽는 법: 첫 번째 출력은 입력 표입니다. 두 번째 출력은 사용자별 실패 횟수입니다(dami 3번 · gaeun 2번 · seoyeon 1번). <mark>세 번째 출력은 2번 이상 실패한 사용자 이름만 담은 리스트</mark>입니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_events` | 파일 경로 | 이벤트 표(미리 채움) |
| `pick_server_failures` | 이벤트 표 | 판정 서버 실패 이벤트 표(미리 채움) |
| `pick_suspicious` | 서버 실패 표 | 실패가 반복된 사용자의 이벤트 표 |
| `judge_failure` | 사용자 · 행동 | 판정 이유와 우선순위 |

- **직접 쓰는 곳은 여섯 군데**(번호 1 ~ 6)이고, 함수 두 개 안에 나뉘어 있습니다.
  - `pick_suspicious`(1 ~ 3번): 반복된 사용자의 이름을 꺼내고, `isin` 으로 그 사용자의 행을 골라 이벤트 표를 만듭니다. 사용자별 실패 횟수를 세는 줄은 미리 채웠습니다.
  - `judge_failure`(4 ~ 6번): 행동을 자원과 행위로 나누고, Module 3 `check_permission` 으로 판정하고, 이유에서 우선순위를 꺼냅니다.

## 실습 3-2 · 반복 거절 찾고 이유별 순서 정하기

**이런 상황이 있습니다**

- **지금은**: <mark>판정 서버의 거절 9건을 하나씩 읽어야 하고, 어느 것이 급한지 알 수 없습니다</mark>.
- **그래서 만드는 것**: `access_detection.py` 입니다.
  - 실패가 3번 이상 반복된 사용자의 이벤트를 고릅니다.
  - 고른 이벤트를 Module 3 `check_permission` 으로 다시 판정해 이유를 알아냅니다.
  - 이유로 순서를 정합니다.
- **실행하면**: <mark>단계 1: 서버 실패 이벤트 수, 단계 2: 먼저 확인할 이벤트 수, 단계 3: 순서대로 이벤트가 한 줄씩 나옵니다.</mark>
- **현업에서는**: 같은 계정의 요청이 반복해서 거절되면 먼저 확인할 근거가 됩니다. 이유별로 순서를 정해 두면 퇴사자 계정처럼 급한 것을 빠뜨리지 않고, 서버 설정 문제는 따로 점검합니다.

**할 일**

1. `access_detection.py` · `exercise3-2_run.py` 두 파일을 만들고, `access_detection.py` 의 두 함수에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>서버 실패 수</mark>(단계 1), <mark>먼저 확인할 이벤트 수</mark>(단계 2), <mark>이유별 순서</mark>(단계 3)를 읽습니다.

**`access_detection.py`**

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다
from rbac import check_permission                     # Module 3에서 만든 권한 판정 함수를 불러온다

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
    # 2. users 가 repeated_names 안에 있는지 isin 으로 구해 is_repeated_user 에 담는다
    # 3. server_failures 에서 is_repeated_user 가 True 인 행만 골라 suspicious 에 담는다
    return suspicious                                 # 먼저 확인할 실패 이벤트 표를 리턴한다


def judge_failure(user, action):                      # 사용자와 행동을 받는 함수
    """서버가 거절한 요청을 Module 3 권한 규칙으로 다시 판정해 이유와 우선순위를 리턴한다.
    거절이 규칙대로인지 확인할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. action 을 ":" 기준으로 나눠 parts 에 담는다 (예: "SALES:QUERY" → ["SALES", "QUERY"]. 앞 조각이 자원, 뒤 조각이 행위)
    resource = parts[0]                               # 첫 번째 조각이 자원이다
    permission_action = parts[1]                      # 두 번째 조각이 행위이다

    # 5. check_permission 에 user, resource, permission_action 을 전달하고, 결과를 is_allowed 와 reason 에 나눠 담는다 (모양: is_allowed, reason = check_permission(...). is_allowed 는 이 문제에서 쓰지 않는다)
    # 6. PRIORITY 에서 reason 의 순서를 꺼내 priority 에 담는다 (딕셔너리에 없는 이유이면 4 — .get(reason, 4))
    return reason, priority                           # 판정 이유와 우선순위를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 6번은 모두 함수 안이라 앞에 공백 4개입니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.**
- 채우기 전에 실행하면 `NameError: name 'suspicious' is not defined` 오류가 납니다. 1 ~ 3번을 아직 안 썼기 때문입니다.

**`exercise3-2_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. `len(표)` 는 표의 행 수입니다.

```python
from access_detection import load_events, pick_server_failures, pick_suspicious, judge_failure, EVENTS_PATH  # 방금 만든 함수를 불러온다

LABELS = {"퇴사한 계정": "퇴사한 계정", "권한 없음": "권한 없음", "허용": "규칙은 허용인데 서버가 거절"}  # 판정 이유를 담당자가 읽는 말로 바꾼다

events = load_events(EVENTS_PATH)                            # 이벤트 파일을 표로 읽는다
server_failures = pick_server_failures(events)               # 판정 서버의 실패 이벤트만 골라낸다
failure_count = len(server_failures)                         # 서버 실패가 모두 몇 개인지 센다
print("--- 단계 1: 판정 서버의 실패 이벤트", failure_count, "개")  # 단계 1 시작을 알리는 줄과 개수

suspicious = pick_suspicious(server_failures)                # 먼저 확인할 실패 이벤트만 골라낸다
suspicious_count = len(suspicious)                           # 먼저 확인할 이벤트가 몇 개인지 센다
print("--- 단계 2: 먼저 확인할 실패 이벤트", suspicious_count, "개")  # 단계 2 시작을 알리는 줄과 개수

suspicious_list = suspicious.to_dict("records")              # 표를 이벤트 딕셔너리 리스트로 바꾼다
judged_list = []                                             # 판정 결과를 담을 빈 리스트
for event in suspicious_list:                                # 이벤트를 하나씩 꺼낸다
    reason, priority = judge_failure(event["user"], event["action"])  # Module 3 규칙으로 다시 판정한다
    judged = {"priority": priority, "reason": reason, "event": event}  # 순서 · 이유 · 이벤트를 딕셔너리로 만든다
    judged_list.append(judged)                               # 판정 결과를 리스트에 추가한다

print("--- 단계 3: 우선순위")                            # 단계 3 시작을 알리는 줄
for priority in [1, 2, 3]:                                   # 우선순위대로 꺼낸다
    for judged in judged_list:                               # 판정 결과를 하나씩 꺼낸다
        if judged["priority"] == priority:                   # 지금 순서의 결과이면
            event = judged["event"]                          # 그 이벤트를 꺼낸다
            label = LABELS.get(judged["reason"], judged["reason"])  # 담당자가 읽는 말로 바꾼다
            print(priority, label, event["user"], event["action"], event["time"])  # 순서 · 이유 · 사용자 · 행동 · 시각을 출력한다
```

**순서**

1. **[VS Code]** 파일 `access_detection.py` · `exercise3-2_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `access_detection.py` 에서 <mark>직접 쓰는 곳 여섯 군데를 씁니다</mark>. 위 판다스 문법 상자와 1.1 의 표를 참고해 씁니다. 막히면 아래 「실습 3-2 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise3-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise3-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **세 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1과 단계 2는 숫자가 제목 줄에 함께 나오므로 그 아래 줄이 없고, 단계 3은 7줄입니다.
5. **[보고서]** `report_u3.md` 의 `## 실습 3-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 서버 실패 수와 먼저 확인할 이벤트 수, 1순위 사용자를 적어 주세요.
   - (나) [핵심 질문] ① dami 의 실패 4개는 Module 3 규칙으로 어떤 이유로 판정됐고, 왜 1순위일까요? ② gaeun 의 실패 3개는 규칙으로는 「허용」인데 서버가 거절했습니다. 공격이라고 확정할 수 있는지 적고, 먼저 무엇을 확인해야 하는지 적어 주세요.
   - (다) [핵심 질문] seoyeon 의 서버 실패 2건(11:40 `SETTLE:QUERY` · 18:20 `SALES:CHANGE`)은 먼저 확인할 이벤트에 들어가지 않았습니다. 들어가지 않은 이유를 이번 실습의 규칙(실패 3번 이상)으로 설명하고, 이 규칙 때문에 놓칠 수 있는 경우를 한 가지 적어 주세요.

## 실습 3-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 센 결과의 왼쪽 이름(인덱스) | `repeated_names = repeated_users.index` |
| 리스트 안에 있는지 | `is_repeated_user = users.isin(repeated_names)` |
| Module 3 규칙으로 판정 | `is_allowed, reason = check_permission(user, resource, permission_action)` |
| 순서 | `priority = PRIORITY.get(reason, 4)` |

---

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개를 끝내고 「보고서 쓰기」 · 「오늘의 글 쓰기」까지 한 뒤에 합니다.

**1. 오늘 한 일 확인**

1. 웹 서버 요청을 분마다 세고, 평소 평균의 3배(6.0번) 이상인 분을 찾았다 (실습 3-1)
2. 판정 서버 거절 9건 중 반복된 7건을 Module 3 의 `check_permission` 으로 다시 판정하고, 이유로 순서를 정했다 (실습 3-2)
3. 보고서 `report_u3.md` 의 실습 3-1 · 3-2 칸에 `답:` 뒤가 비어 있는 질문이 없다(못 적은 칸은 `모름 — 막힌 곳: …`)

**2. 파일 확인** — **[터미널]** `anomaly_detection` 폴더에서 확인합니다.

```bash
pwd
ls
ls config
```

- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기 · `ls config` config 폴더 안 보기
- 오늘 만든 `baseline_traffic.csv` · `traffic_detection.py` · `exercise3-1_run.py` · `rbac.py` · `access_detection.py` · `exercise3-2_run.py` · `report_u3.md` 가 보여야 합니다. `normalized_events.json` 과 Unit 2 파일도 함께 보입니다.
- `config` 안에는 `users.json` · `roles.json` 이 보여야 합니다.
- `__pycache__` 폴더는 파이썬이 실행하면서 만든 임시 폴더라 있어도 됩니다.

**3. 깃허브에 올리기**

1. **[터미널]** `security-agent-toolkit` 폴더로 옮기고 위치를 확인합니다. <mark>결과가 `…/security-agent-toolkit` 으로 끝나야 합니다.</mark>
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark>빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.</mark>
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `anomaly_detection/__pycache__/` 가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.
3. **[보고서]** `report_u3.md` 의 `## 마무리` 아래 (가)를 채웁니다. <mark>올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다.</mark>
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add anomaly detection unit 3 traffic spike and repeated denial detection"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - <mark>`git push` 가 거절(`rejected`)되면</mark> 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다. `git pull` 로 받아 온 뒤 `git push` 를 다시 합니다. 그때 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다.
5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `anomaly_detection` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다.

- 시간이 남아 도전을 했다면 도전 파일까지 만든 뒤 3번의 2 ~ 4를 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**4. 이어지는 곳**

1. 다음 Unit 4(위험 점수 매기고 오탐 줄이기)에서는 이번 Unit 의 탐지 결과를 **같은 사용자의 기록끼리 이어서 함께 보고**, 위험 점수를 매겨 등급으로 나눕니다.
2. 오늘 만든 `access_detection.py` 는 다음 Unit 에서 여러 번 불러 씁니다. 파일 이름과 함수 이름을 바꾸지 않습니다.

---

<!-- learn:answers -->
