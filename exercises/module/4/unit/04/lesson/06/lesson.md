---
id: m4-u04-l06
title: 응용 4-2 · 알림의 오탐과 미탐 세기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/110_day05_am_false_alarm_tuning.md
  mission_id: GichanSource.m4-1106-am-false-alarm-tuning
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 응용 4-2 · 알림의 오탐과 미탐 세기

## 목표: 오탐과 미탐 개수

> **여유가 되면 해 보세요.** 핵심 실습 4-1 · 4-2와 글쓰기를 먼저 마칩니다. 하지 않아도 다음 Unit을 따라가는 데 문제가 없습니다.

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「지금까지 만든 탐지 규칙들이 11/2 에 알림을 7건 냈습니다. 팀원 세 명이 7건을 모두 열어 보느라 반나절이 걸렸는데, 그중에는 조사해 보니 문제가 아닌 알림이 여럿 있었습니다. 반대로 사고 조사팀이 확인한 진짜 문제는 5건인데, 알림이 난 것은 그중 3건뿐이라고 합니다.
>
> 규칙이 얼마나 맞았는지 숫자로 알려 주세요. 문제가 아닌데 난 알림이 몇 건이고, 알림이 나지 않은 진짜 문제가 몇 건인가요?」
> - **왜 중요한가**: <mark>문제가 아닌 알림이 많으면 담당자가 알림을 무시하게 되고, 알림이 나지 않은 진짜 문제는 아무도 모르고 지나갑니다.</mark> 숫자로 세어 봐야 어느 규칙을 고칠지 정할 수 있습니다.

## 왜 틀린 알림을 세어 봐야 하는가

1. 탐지 규칙은 알림을 내지만, 알림이 모두 맞는 것은 아닙니다. 사람이 조사해 보면 문제가 아닌 알림도 있고, 알림이 나지 않았는데 진짜 문제인 경우도 있습니다.
2. 이번 실습의 질문은 하나입니다. <mark>**알림 7개 중 몇 개가 틀렸고, 진짜 문제 5개 중 몇 개를 놓쳤는가?**</mark>
3. 틀리는 방식은 두 가지이고, 줄여야 하는 쪽이 다릅니다.

| | 진짜 문제였다 | 문제가 아니었다 |
|---|---|---|
| **알림이 났다** | 맞게 찾음 | **오탐** — 담당자의 확인 시간만 씀 |
| **알림이 나지 않았다** | **미탐** — 진짜 문제를 놓침 | 해당 없음 |

## 1.1 알림 7개와 진짜 문제 5개

**먼저 `problems.json` 을 만듭니다.** 사람이 조사해서 확인한 11/2 의 진짜 문제 5개입니다. `anomaly_detection` 폴더에 만들고, 같은 이름의 파일이 이미 있으면 아래 내용으로 덮어씁니다. 응용 4-3에서도 이 파일을 씁니다.

**`problems.json`**

```
[
  {"id": "P1", "who": "dami", "what": "퇴사한 계정으로 서버에 요청함"},
  {"id": "P2", "who": "seoyeon", "what": "업무와 상관없는 파일을 대량으로 내려받음"},
  {"id": "P3", "who": "198.51.100.90", "what": "스캐너 경로를 요청해 접근 가능한 곳을 찾음"},
  {"id": "P4", "who": "203.0.113.50", "what": "로그인 5번 실패 뒤 성공하고 관리자 화면을 요청함"},
  {"id": "P5", "who": "seoyeon", "what": "권한 없는 정산 조회를 시도함"}
]
```

- **[터미널]** `python -c "import pandas as pd; print(len(pd.read_json('problems.json')))"` 로 확인해 `5` 가 나오면 됩니다(맥북은 `python3`).

`review_alerts.json` 의 알림 7개입니다. `real` 열이 `True` 이면 조사해 보니 진짜 문제였습니다.

| id | 규칙 | 대상 | real | 조사 메모 |
|---|---|---|---|---|
| A1 | 서버 반복 거절 | dami | `True` | 퇴사한 계정이 서버에 4번 요청함 |
| A2 | 서버 반복 거절 | gaeun | `False` | 서버 설정 오류로 확인됨 — 공격 아님 |
| A3 | SaaS 업무 시간 밖 로그인 | jiwoo | `False` | 출장 중 협력사 사무실에서 비밀번호를 잘못 입력함 |
| A4 | SaaS 평소와 다른 IP | jiwoo | `False` | 출장 중 협력사 사무실에서 접속함 |
| A5 | SaaS 평소와 다른 IP | seoyeon | `False` | 외근 중 협력사 사무실에서 접속함 |
| A6 | SaaS 대량 다운로드 | seoyeon | `True` | 업무와 상관없는 파일 6개를 한꺼번에 내려받음 |
| A7 | 웹 경로 스캔 | 198.51.100.90 | `True` | 스캐너 경로 3개를 연속으로 요청함 |

- 진짜 문제였던 알림은 A1 · A6 · A7 세 개이고, <mark>나머지 네 개(A2 · A3 · A4 · A5)가 오탐</mark>입니다.
- `problems.json` 의 진짜 문제 P1 ~ P5 중 알림이 나온 것은 P1 · P2 · P3 이고, <mark>P4 · P5 는 알림이 나지 않았습니다(미탐)</mark>.
- 오탐이라고 해서 알림을 만든 규칙이 잘못 작동한 것은 아닙니다. 규칙대로 찾았지만 조사해 보니 문제가 아니었다는 뜻입니다.

**판다스 문법 상자 — 리스트에 없는 것 찾기 `~열.isin(리스트)`**

**<mark>`~열.isin(리스트)`</mark> 는 열의 값이 리스트 안에 없으면 `True`, 있으면 `False` 를 줍니다**

아래는 알림이 난 사용자 기록입니다. 이미 확인을 끝낸 사용자 리스트(`checked_users`)에 **없는** 기록만 찾습니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                          # 표에 넣을 내용(열 이름: 값들)
    "user": ["gaeun", "dami", "seoyeon", "junho", "dami"],        # user 열
    "action": ["login", "download", "login", "upload", "login"],  # action 열
}
df = pd.DataFrame(data)                                           # 내용으로 표(DataFrame)를 만든다
print(df)                                                         # 표를 출력한다
```

실행 결과:

```
      user    action
0    gaeun     login
1     dami  download
2  seoyeon     login
3    junho    upload
4     dami     login
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
checked_users = ["gaeun", "seoyeon"]         # 확인을 끝낸 사용자 두 명을 리스트에 담는다
is_checked = df["user"].isin(checked_users)  # user 열의 각 값이 그 리스트 안에 있는지 확인한다
print(is_checked)                            # True · False 를 출력한다
```

실행 결과:

```
0     True
1    False
2     True
3    False
4    False
Name: user, dtype: bool
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
is_unchecked = ~is_checked  # True 와 False 를 서로 뒤집는다 (리스트에 없으면 True)
print(is_unchecked)         # 뒤집은 결과를 출력한다
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
unchecked_df = df[is_unchecked]  # True 인 행만 남긴다
print(unchecked_df)              # 아직 확인하지 않은 사용자의 기록을 출력한다
```

실행 결과:

```
    user    action
1   dami  download
3  junho    upload
4   dami     login
```

- 읽는 법: 두 번째 출력은 `isin` 의 결과이고, <mark style="background:#bde3ff">gaeun · seoyeon 의 행이 `True`</mark> 입니다. 세 번째 출력은 그 결과를 `~` 로 뒤집은 것이라 <mark style="background:#bde3ff">dami · junho 의 행이 `True`</mark> 입니다. 네 번째 출력은 그 `True` 인 세 행만 남은 표입니다.
- `~is_checked` 는 「리스트에 없다」는 뜻입니다. 이번 실습에서는 이 방식으로 「알림이 하나도 나지 않은 진짜 문제」를 찾습니다.

**판다스 문법 상자 — `True` 개수 세기에 쓰는 `.sum()` (복습)**

**<mark>`열.sum()`</mark> 은 열의 값을 모두 더합니다. `True · False` 열에 쓰면 `True` 의 개수를 셉니다(`True` 는 1, `False` 는 0)**

실습 4-1에서 그룹마다 점수를 더할 때 쓴 `.sum()` 입니다. 아래는 `is_blocked` 열이 차단된 기록이면 `True` 인 표이고, 차단된 기록이 몇 개인지 셉니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                    # 표에 넣을 내용(열 이름: 값들)
    "user": ["gaeun", "dami", "seoyeon", "junho", "dami"],  # user 열
    "is_blocked": [False, True, False, False, True],        # is_blocked 열 (차단된 기록이면 True)
}
df = pd.DataFrame(data)                                     # 내용으로 표(DataFrame)를 만든다
blocked_count = df["is_blocked"].sum()                      # is_blocked 열에서 True 가 몇 개인지 더해서 센다
print(blocked_count)                                        # 차단된 기록 수를 출력한다
```

실행 결과:

```
2
```

- 읽는 법: 출력 <mark style="background:#bde3ff">`2`</mark> 는 `True` 가 두 개(dami 의 행 두 개)라는 뜻입니다. `.sum()` 은 괄호까지 써야 합니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_table` · `pick_real_alerts` | 파일 경로 · 알림 표 | 표 · 진짜 문제였던 알림 표(미리 채움) |
| `find_false_alarms` | 알림 표 | 오탐 표와 규칙별 오탐 개수 |
| `find_missed` | 진짜 문제 표 · 진짜 알림 표 | 놓친 진짜 문제 표 |
| `count_real_alerts` | 알림 표 | 진짜 문제였던 알림 수 |

- **직접 쓰는 곳은 일곱 군데**(번호 1 ~ 7)이고, 함수 세 개 안에 나뉘어 있습니다.

| 함수 | 번호 | 직접 쓰는 일 |
|---|---|---|
| `find_false_alarms` | 1 ~ 3번(3곳) | 진짜가 아닌 알림을 뒤집어 고르고, 규칙별로 셉니다 |
| `find_missed` | 4 ~ 6번(3곳) | 알림이 가리키는 문제 번호를 꺼내고, 알림이 나지 않은 문제를 뒤집어 고릅니다 |
| `count_real_alerts` | 7번(1곳) | `True` 가 몇 개인지 `.sum()` 으로 셉니다 |

- 이번 실습에서 새 문법은 없습니다. `.sum()` 은 실습 4-1에서 쓴 것을 `True` 개수 세기에 다시 쓰고, `isin` · `~` · `value_counts()` 도 다시 씁니다.

## 응용 4-2 · 알림의 오탐과 미탐 세기

**이런 상황이 있습니다**

- **지금은**: <mark>실습 4-2에서 오탐 수는 셌지만, 알림이 나지 않은 진짜 문제(미탐)가 몇 개인지는 세어 보지 않았습니다</mark>.
- **그래서 만드는 것**: `evaluation.py` 입니다.
  - 진짜 문제였던 알림을 골라 셉니다.
  - 문제가 아니었던 알림(오탐)을 골라 규칙별로 셉니다.
  - 알림이 나지 않은 진짜 문제(미탐)를 찾습니다.
- **실행하면**: <mark>단계 1: 알림 수, 단계 2: 진짜 문제였던 알림 수, 단계 3: 오탐 수와 규칙별 개수, 단계 4: 놓친 진짜 문제가 나옵니다.</mark>
- **현업에서는**: 알림을 낸 규칙마다 오탐 수를 세어 두면 어느 규칙부터 고칠지 정할 수 있고, 미탐은 새 규칙이 필요하다는 신호입니다.

**할 일**

1. `evaluation.py` · `apply4-2_run.py` 두 파일을 만들고, `evaluation.py` 의 세 함수에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>알림 수</mark>(단계 1), <mark>진짜 문제였던 알림 수</mark>(단계 2), <mark>오탐</mark>(단계 3), <mark>미탐</mark>(단계 4)을 읽습니다.

**`evaluation.py`**

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다

ALERTS_PATH = "review_alerts.json"                    # 읽을 알림 파일 이름
PROBLEMS_PATH = "problems.json"                       # 읽을 진짜 문제 파일 이름


def load_table(path):                                 # 파일 경로를 받는 함수
    """JSON 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    table = pd.read_json(path)                        # 파일 속 내용을 표 한 개로 읽는다
    return table                                      # 표를 리턴한다


def pick_real_alerts(alerts):                         # 알림 표를 받는 함수
    """알림 중 조사해 보니 진짜 문제였던 것만 골라 새 표로 만든다.
    맞게 찾은 알림을 셀 때 쓴다.
    """
    is_real = alerts["real"]                          # real 열(진짜 문제이면 True)을 꺼낸다
    real_alerts = alerts[is_real]                     # True 인 행만 골라 새 표로 만든다
    return real_alerts                                # 진짜 문제였던 알림 표를 리턴한다


def find_false_alarms(alerts):                        # 알림 표를 받는 함수
    """진짜 문제가 아니었는데 난 알림(오탐)을 골라 규칙별로 센다.
    어느 규칙이 오탐을 많이 내는지 볼 때 쓴다.
    """
    is_real = alerts["real"]                          # real 열(진짜 문제이면 True)을 꺼낸다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. is_real 을 ~ 로 뒤집어 is_false 에 담는다
    # 2. alerts 에서 is_false 가 True 인 행만 골라 false_alarms 에 담는다
    # 3. false_alarms 의 "rule" 열에서 값별 개수를 value_counts() 로 세어 false_alarm_rule_counts 에 담는다
    return false_alarms, false_alarm_rule_counts      # 오탐 표와 규칙별 오탐 개수를 리턴한다


def find_missed(problems, real_alerts):               # 진짜 문제 표와 진짜 알림 표를 받는 함수
    """알림이 하나도 나지 않은 진짜 문제(미탐)를 골라 새 표로 만든다.
    놓친 문제를 찾을 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. real_alerts 의 "problem" 열을 꺼내 caught_ids 에 담는다
    is_caught = problems["id"].isin(caught_ids)       # 각 문제 번호가 그 안에 있는지 구한다
    # 5. is_caught 를 ~ 로 뒤집어 is_missed 에 담는다
    # 6. problems 에서 is_missed 가 True 인 행만 골라 missed_problems 에 담는다
    return missed_problems                            # 놓친 문제 표를 리턴한다


def count_real_alerts(alerts):                        # 알림 표를 받는 함수
    """진짜 문제였던 알림이 몇 개인지 센다.
    알림이 얼마나 맞았는지 숫자 하나로 볼 때 쓴다.
    """
    is_real = alerts["real"]                          # real 열(진짜 문제이면 True)을 꺼낸다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. is_real 의 True 개수를 .sum() 으로 세어 real_alert_count 에 담는다
    return real_alert_count                           # 진짜 문제였던 알림 수를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 7번은 모두 함수 안이라 앞에 공백 4개입니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.**
- 채우기 전에 실행하면 `NameError: name 'real_alert_count' is not defined` 오류가 납니다. 7번을 아직 안 썼기 때문입니다.

**`apply4-2_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. `len(표)` 는 표의 행 수입니다.

```python
from evaluation import load_table, pick_real_alerts, find_false_alarms, find_missed, count_real_alerts, ALERTS_PATH, PROBLEMS_PATH  # 방금 만든 함수를 불러온다

alerts = load_table(ALERTS_PATH)                      # 알림 파일을 표로 읽는다
problems = load_table(PROBLEMS_PATH)                  # 진짜 문제 파일을 표로 읽는다
alert_count = len(alerts)                             # 알림이 모두 몇 개인지 센다
print("--- 단계 1: 알림 전체 ---")                    # 단계 1 제목
print("알림 수:", alert_count)                        # 알림 수를 출력한다

real_alerts = pick_real_alerts(alerts)                # 진짜 문제였던 알림만 골라낸다
real_alert_count = count_real_alerts(alerts)          # 진짜 문제였던 알림이 몇 개인지 센다
print("--- 단계 2: 진짜 문제였던 알림 (맞게 찾은 알림) ---")  # 단계 2 제목
print("진짜 문제였던 알림 수:", real_alert_count)     # 맞게 찾은 알림 수를 출력한다

false_alarms, false_alarm_rule_counts = find_false_alarms(alerts)  # 오탐과 규칙별 오탐 개수를 구한다
false_alarm_count = len(false_alarms)                 # 오탐이 몇 개인지 센다
print("--- 단계 3: 오탐 (문제가 아닌데 난 알림) ---")  # 단계 3 제목
print("오탐 수:", false_alarm_count)                  # 오탐 수를 출력한다
print("오탐이 난 규칙과 오탐 수:")                    # 아래 표가 무엇인지 알리는 줄
print(false_alarm_rule_counts)                        # 규칙마다 오탐이 몇 개인지 출력한다

missed_problems = find_missed(problems, real_alerts)  # 알림이 나지 않은 진짜 문제를 찾는다
missed_count = len(missed_problems)                   # 놓친 문제가 몇 개인지 센다
print("--- 단계 4: 미탐 (알림이 나지 않은 진짜 문제) ---")  # 단계 4 제목
print("미탐 수:", missed_count)                       # 미탐 수를 출력한다
missed_list = missed_problems.to_dict("records")      # 표를 문제 딕셔너리 리스트로 바꾼다
for problem in missed_list:                           # 놓친 문제를 하나씩 꺼낸다
    print("놓친 문제:", problem["id"], problem["who"], problem["what"])  # 문제 번호 · 대상 · 내용을 출력한다
```

**순서**

1. **[VS Code]** 파일 `evaluation.py` · `apply4-2_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `evaluation.py` 에서 <mark>직접 쓰는 곳 일곱 군데를 씁니다</mark>. 위 판다스 문법 상자와 1.1 의 표를 참고해 씁니다. 막히면 아래 「응용 4-2 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python apply4-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python apply4-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1과 단계 2는 각각 1줄, 단계 3은 7줄(오탐 수 1줄 · 안내 1줄 · 규칙별 개수 표 5줄), 단계 4는 3줄(미탐 수 1줄 · 놓친 문제 2줄)입니다. 개수가 같은 규칙의 순서는 달라도 됩니다.
5. **[보고서]** `report_u4.md` 의 `## 응용 4-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 알림 수와 오탐 수와 미탐 수를 적어 주세요.
   - (나) [핵심 질문] A2(gaeun)는 조사해 보니 서버 설정 오류여서 오탐으로 셌습니다. 이 알림이 오탐인 이유와, 그래도 한 번은 확인해야 했던 이유를 적어 주세요.
   - (다) [핵심 질문] 미탐인 P5(seoyeon 의 권한 없는 정산 조회 시도)는 왜 알림이 나지 않았을까요? 그 문제를 찾으려면 어떤 규칙이 필요한지도 적어 주세요.

## 응용 4-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 조건 뒤집기 | `is_false = ~is_real` |
| 조건에 맞는 행만 | `false_alarms = alerts[is_false]` |
| 이름별 개수 | `false_alarm_rule_counts = false_alarms["rule"].value_counts()` |
| 열 하나 꺼내기 | `caught_ids = real_alerts["problem"]` |
| 리스트에 없는 것 | `is_missed = ~is_caught` |
| `True` 개수 세기 | `real_alert_count = is_real.sum()` |

---
