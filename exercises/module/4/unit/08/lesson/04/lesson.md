---
id: m4-u08-l04
title: 실습 8-3 · 규칙 합쳐 놓친 문제 다시 세기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/110_day05_am_false_alarm_tuning.md
  mission_id: GichanSource.m4-1106-am-false-alarm-tuning
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 8-3 · 규칙 합쳐 놓친 문제 다시 세기

## 목표: 합친 알림과 평가 한 문장

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「203.0.113.50 은 로그인에 5번 실패한 뒤 성공하고 관리자 화면까지 요청했습니다. 사고 조사팀이 이것을 진짜 문제로 확인했습니다(문제 번호 `P4`, `problems.json` 에 있습니다). 그런데 이번 알림 표에는 이 IP 의 알림이 없습니다. Unit 4에서 만든 로그인 규칙은 이 IP 를 찾아 알림을 1건 냈습니다(알림 번호 `A8`, `login_alerts.json` 에 있습니다).
>
> 로그인 규칙의 알림을 합치면 놓친 문제가 몇 개 줄고 오탐은 늘지 않는지 확인해 주세요. 결과는 보고서에 한 문장으로 적을 수 있게 정리해 주세요.」
> - **왜 중요한가**: <mark>규칙을 하나 더 합치면 놓친 문제는 줄지만 오탐이 늘 수도 있어서, 합친 뒤에 다시 세어 봐야 합니다.</mark>

## 왜 규칙을 합쳐 미탐을 줄이는가

1. 규칙마다 찾는 문제가 다릅니다. 한 규칙이 놓친 문제는 다른 규칙이 찾을 수 있으므로, 알림 표를 합쳐서 한꺼번에 평가합니다.
2. 이번 실습의 질문은 하나입니다. <mark>**규칙의 알림을 합치면 놓친 문제는 몇 개 남고, 오탐은 몇 개인가?**</mark>
3. 평가 결과는 숫자 세 개(알림 수 · 오탐 수 · 놓친 문제 수)를 한 문장으로 적어 두면, 규칙을 고칠 때 전후를 비교하기 쉽습니다.

## 3.1 진짜 문제 5개를 어느 규칙이 찾는가

| 문제 | 내용 | 찾는 알림 |
|---|---|---|
| P1 | dami 가 퇴사한 계정으로 서버에 요청함 | A1 (서버 반복 거절) |
| P2 | seoyeon 이 업무와 상관없는 파일을 대량으로 내려받음 | A6 (SaaS 대량 다운로드) |
| P3 | 198.51.100.90 이 스캐너 경로를 요청함 | A7 (웹 경로 스캔) |
| P4 | 203.0.113.50 이 로그인 5번 실패 뒤 성공함 | A8 (웹 로그인 반복 실패) — **이번 실습에서 합칩니다** |
| P5 | seoyeon 이 권한 없는 정산 조회를 시도함 | **없음** |

- 오탐은 `problem` 열이 비어 있어서, 빈 값을 지우면 알림이 가리키는 문제 번호만 남습니다.
- A8 을 합치면 P4 가 잡혀서 놓친 문제가 2개에서 1개(P5)로 줄어듭니다.
- 오탐은 A8 이 진짜 문제(`real` 이 `True`)라서 늘지 않습니다. 오탐은 실습 8-2에서 줄인 2개(A2 · A3) 그대로입니다.
- <mark>P5 는 이번 실습의 규칙으로는 찾을 수 없습니다.</mark> 보고서 (다)에서 어떤 규칙이 필요한지 생각해 봅니다.

<h2>판다스 문법 상자 — 표 두 개를 이어 붙이기 <code>pd.concat</code></h2>

**<mark>`pd.concat([표1, 표2])`</mark> 는 열 이름이 같은 표 두 개를 위아래로 이어 붙여 표 하나로 만듭니다**

아래는 규칙 두 개가 낸 알림 표입니다. 두 표를 하나로 합칩니다. 표는 반드시 **대괄호 `[ ]` 안에 리스트로** 묶어 전달합니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

first_data = {                                     # 첫 번째 규칙의 알림 내용
    "id": ["A1", "A2"],                            # id 열
    "rule": ["서버 반복 거절", "서버 반복 거절"],  # rule 열
}
first_alerts = pd.DataFrame(first_data)            # 첫 번째 알림 표를 만든다
print(first_alerts)                                # 표를 출력한다
```

실행 결과:

```
   id      rule
0  A1  서버 반복 거절
1  A2  서버 반복 거절
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
second_data = {                            # 두 번째 규칙의 알림 내용
    "id": ["A8"],                          # id 열
    "rule": ["웹 로그인 반복 실패"],       # rule 열
}
second_alerts = pd.DataFrame(second_data)  # 두 번째 알림 표를 만든다
print(second_alerts)                       # 표를 출력한다
```

실행 결과:

```
   id         rule
0  A8  웹 로그인 반복 실패
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
merged_alerts = pd.concat([first_alerts, second_alerts])  # 두 표를 대괄호 리스트로 묶어 위아래로 이어 붙인다
print(merged_alerts)                                      # 합친 표를 출력한다
```

실행 결과:

```
   id         rule
0  A1     서버 반복 거절
1  A2     서버 반복 거절
0  A8  웹 로그인 반복 실패
```

- 읽는 법: 세 번째 출력에는 알림 세 개(A1 · A2 · A8)가 모두 들어 있습니다. <mark style="background:#bde3ff">왼쪽 번호는 각 표의 번호를 그대로 가져와서 `0` 이 두 번 나오지만</mark> 내용은 모두 합쳐진 것입니다.
- 열 이름이 같아야 같은 열끼리 이어 붙습니다. 이름이 다르면 빈 값(`NaN`)이 생깁니다.

<h2>판다스 문법 상자 — 빈 값 지우기 <code>.dropna()</code></h2>

**<mark>`열.dropna()`</mark> 는 열에서 비어 있는 값(`None`)을 지우고 나머지만 남깁니다**

아래는 알림 표이고, `problem` 열은 진짜 문제를 가리키는 번호입니다. 문제가 아니었던 알림은 번호가 비어 있습니다. 번호가 있는 것만 남깁니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                  # 표에 넣을 내용(열 이름: 값들)
    "id": ["A1", "A2", "A3", "A4"],       # id 열
    "problem": ["P1", None, "P3", None],  # problem 열 (문제가 아니었으면 None)
}
df = pd.DataFrame(data)                   # 내용으로 표(DataFrame)를 만든다
print(df)                                 # 표를 출력한다
```

실행 결과:

```
   id problem
0  A1      P1
1  A2    None
2  A3      P3
3  A4    None
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
problem_ids = df["problem"].dropna()  # problem 열에서 비어 있는 값을 지운다
print(problem_ids)                    # 남은 문제 번호를 출력한다
```

실행 결과:

```
0    P1
2    P3
Name: problem, dtype: object
```

- 읽는 법: 첫 번째 출력에서 `problem` 이 비어 있는 행은 `None` 으로 보입니다. <mark style="background:#bde3ff">두 번째 출력에는 번호가 있는 0번 행(P1)과 2번 행(P3)만</mark> 남았습니다. `Name: problem, dtype: object` 줄은 몰라도 됩니다.
- `.dropna()` 는 괄호까지 써야 합니다. 괄호를 빼면 `isin` 에 넣을 때 오류가 납니다.

<h2>한 장 정리</h2>

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_table` · `apply_exception` | 파일 경로 · 알림 표 | 표 · 빼낸 알림 표와 남은 알림 표(미리 채움, 실습 8-2와 같은 코드) |
| `merge_alerts` | 알림 표 두 개 | 합친 알림 표 |
| `evaluate` | 합친 알림 표 · 진짜 문제 표 | 오탐 수와 놓친 진짜 문제 표 |
| `make_summary` | 알림 수 · 오탐 수 · 놓친 문제 수 | 한 문장 |

- **직접 쓰는 곳은 여섯 군데**(번호 1 ~ 6)이고, 함수 세 개 안에 나뉘어 있습니다.
  - `merge_alerts`(1번, 1곳): 두 표를 이어 붙입니다.
  - `evaluate`(2 ~ 5번, 4곳): 알림이 가리키는 문제 번호만 남기고(빈 값 지우기), 그 번호가 알림에 있는지 구한 뒤, 놓친 문제를 뒤집어 고릅니다.
  - `make_summary`(6번, 1곳): 숫자를 문자열로 바꿔 이어 붙여 한 문장을 만듭니다.
- 이번 실습에서 새 문법은 `.dropna()` 하나입니다. `pd.concat` 은 Unit 7에서 쓴 것이라 다시 설명합니다.

## 실습 8-3 · 규칙 합쳐 놓친 문제 다시 세기

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>예외 규칙으로 오탐은 줄였지만, 놓친 진짜 문제 2개는 그대로입니다</mark>.
- **그래서 만드는 것**: `final_check.py` 입니다.
  - 예외 규칙을 적용한 알림에 로그인 규칙의 알림을 합칩니다.
  - 합친 알림의 오탐 수와 놓친 문제를 다시 구합니다.
  - 결과를 한 문장으로 만듭니다.
- **실행하면**: <mark>단계 1: 예외 규칙으로 빠진 알림과 남은 알림, 단계 2: 합친 알림 수, 단계 3: 오탐 수, 단계 4: 아직 놓친 문제, 단계 5: 한 문장 요약이 나옵니다.</mark>
- **현업에서는**: 규칙을 고치거나 더할 때마다 오탐과 미탐을 다시 세어 전후 숫자를 보고서에 남깁니다.

<h2>할 일</h2>

1. `final_check.py` · `exercise8-3_run.py` 두 파일을 만들고, `final_check.py` 의 세 함수에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>합친 알림 수</mark>(단계 2), <mark>오탐 수</mark>(단계 3), <mark>아직 놓친 문제</mark>(단계 4), <mark>한 문장 요약</mark>(단계 5)을 읽습니다.
3. 마지막으로 이번 Unit의 작업 파일이 모두 있는지 확인합니다.

<h3><code>final_check.py</code></h3>

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다

ALERTS_PATH = "review_alerts.json"                    # 읽을 알림 파일 이름
LOGIN_ALERTS_PATH = "login_alerts.json"               # 읽을 로그인 규칙 알림 파일 이름
PROBLEMS_PATH = "problems.json"                       # 읽을 진짜 문제 파일 이름
IP_RULE = "SaaS 평소와 다른 IP"                       # 예외를 적용할 규칙 이름
TRUSTED_IPS = ["203.0.113.80"]                        # 믿는 IP 리스트 : 협력사 사무실 IP 한 개


def load_table(path):                                 # 파일 경로를 받는 함수
    """JSON 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    table = pd.read_json(path)                        # 파일 속 내용을 표 한 개로 읽는다
    return table                                      # 표를 리턴한다


def apply_exception(alerts):                          # 알림 표를 받는 함수
    """IP 규칙 알림 중 믿는 IP 에서 온 것만 빼낸다.
    실습 8-2에서 만든 예외 규칙을 다시 적용할 때 쓴다.
    """
    is_ip_rule = alerts["rule"] == IP_RULE            # 각 알림이 IP 규칙의 알림인지 비교한다
    is_trusted = alerts["ip"].isin(TRUSTED_IPS)       # 각 알림의 IP 가 믿는 IP 리스트에 있는지 구한다
    is_removed = is_ip_rule & is_trusted              # IP 규칙의 알림이면서 믿는 IP 에서 온 것만 True 로 만든다
    removed_alerts = alerts[is_removed]               # 빼낼 알림만 골라 새 표로 만든다
    is_kept = ~is_removed                             # 빼지 않을 알림을 True 로 만든다
    kept_alerts = alerts[is_kept]                     # True 인 행만 골라 새 표로 만든다
    return removed_alerts, kept_alerts                # 빼낸 알림 표와 남은 알림 표를 리턴한다


def merge_alerts(alerts, login_alerts):               # 알림 표 두 개를 받는 함수
    """두 규칙 묶음의 알림 표를 위아래로 이어 하나로 만든다.
    새 규칙의 알림까지 한꺼번에 평가할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. pd.concat 에 두 표를 대괄호 리스트로 묶어 전달하고, 합친 표를 all_alerts 에 담는다 (모양: pd.concat([표1, 표2]))
    return all_alerts                                 # 합친 알림 표를 리턴한다


def evaluate(all_alerts, problems):                   # 알림 표와 진짜 문제 표를 받는 함수
    """합친 알림에서 오탐 수와 놓친 문제를 구한다.
    튜닝을 마친 뒤 결과를 마지막으로 평가할 때 쓴다.
    """
    is_real = all_alerts["real"]                      # real 열(진짜 문제이면 True)을 꺼낸다
    is_false = ~is_real                               # 문제가 아니었던 알림을 True 로 만든다
    false_alarms = all_alerts[is_false]               # True 인 행만 골라 새 표로 만든다
    false_alarm_count = len(false_alarms)             # 오탐이 몇 개인지 센다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. all_alerts 의 "problem" 열에서 빈 값을 .dropna() 로 지워 caught_ids 에 담는다
    # 3. problems 의 "id" 열이 caught_ids 안에 있는지 isin 으로 구해 is_caught 에 담는다
    # 4. is_caught 를 ~ 로 뒤집어 is_missed 에 담는다
    # 5. problems 에서 is_missed 가 True 인 행만 골라 missed_problems 에 담는다
    return false_alarm_count, missed_problems         # 오탐 수와 놓친 문제 표를 리턴한다


def make_summary(alert_count, false_alarm_count, missed_count):  # 세 개수를 받는 함수
    """알림 수 · 오탐 수 · 놓친 문제 수를 한 문장으로 만든다.
    평가 결과를 보고서에 한 줄로 적을 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 6. "알림 " 과 알림 수, "개 중 오탐 " 과 오탐 수, "개 · 놓친 문제 " 와 놓친 문제 수, "개" 를 + 로 이어 summary 에 담는다 (숫자는 str() 로 문자열로 바꿔서 이어 붙인다)
    return summary                                    # 한 문장을 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 6번은 모두 함수 안이라 앞에 공백 4개입니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.**
- 채우기 전에 실행하면 `NameError: name 'all_alerts' is not defined` 오류가 납니다. 1번을 아직 안 썼기 때문입니다.

<h3><code>exercise8-3_run.py</code></h3>

그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다.

```python
from final_check import load_table, apply_exception, merge_alerts, evaluate, make_summary, ALERTS_PATH, LOGIN_ALERTS_PATH, PROBLEMS_PATH  # 방금 만든 함수를 불러온다

alerts = load_table(ALERTS_PATH)                      # 알림 파일을 표로 읽는다
login_alerts = load_table(LOGIN_ALERTS_PATH)          # 로그인 규칙 알림 파일을 표로 읽는다
problems = load_table(PROBLEMS_PATH)                  # 진짜 문제 파일을 표로 읽는다

removed_alerts, kept_alerts = apply_exception(alerts)  # 믿는 IP 예외 규칙을 적용한다
removed_count = len(removed_alerts)                   # 빠진 알림이 몇 개인지 센다
kept_count = len(kept_alerts)                         # 남은 알림이 몇 개인지 센다
print("--- 단계 1: 믿는 IP 예외 규칙 적용 ---")       # 단계 1 제목
print("빠진 알림 수:", removed_count)                 # 빠진 알림 수를 출력한다
print("남은 알림 수:", kept_count)                    # 남은 알림 수를 출력한다

all_alerts = merge_alerts(kept_alerts, login_alerts)  # 로그인 규칙의 알림을 합친다
all_count = len(all_alerts)                           # 합친 알림이 몇 개인지 센다
print("--- 단계 2: 로그인 규칙의 알림 합치기 ---")    # 단계 2 제목
print("합친 뒤 알림 수:", all_count)                  # 합친 알림 수를 출력한다

false_alarm_count, missed_problems = evaluate(all_alerts, problems)  # 오탐 수와 놓친 문제를 구한다
print("--- 단계 3: 합친 알림의 오탐 ---")             # 단계 3 제목
print("오탐 수:", false_alarm_count)                  # 오탐 수를 출력한다

missed_count = len(missed_problems)                   # 놓친 문제가 몇 개인지 센다
print("--- 단계 4: 아직 놓친 진짜 문제 ---")          # 단계 4 제목
print("미탐 수:", missed_count)                       # 미탐 수를 출력한다
missed_list = missed_problems.to_dict("records")      # 표를 문제 딕셔너리 리스트로 바꾼다
for problem in missed_list:                           # 놓친 문제를 하나씩 꺼낸다
    print("놓친 문제:", problem["id"], problem["who"], problem["what"])  # 문제 번호 · 대상 · 내용을 출력한다

summary = make_summary(all_count, false_alarm_count, missed_count)  # 결과를 한 문장으로 만든다
print("--- 단계 5: 한 문장 요약 ---")                 # 단계 5 제목
print(summary)                                        # 요약 문장을 출력한다
```

<h2>순서</h2>

1. **[VS Code]** 파일 `final_check.py` · `exercise8-3_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `final_check.py` 에서 <mark>직접 쓰는 곳 여섯 군데를 씁니다</mark>. 위 판다스 문법 상자와 3.1 의 표를 참고해 씁니다. 막히면 아래 「실습 8-3 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise8-3_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise8-3_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **다섯 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1은 2줄(빠진 알림 수 · 남은 알림 수), 단계 2와 단계 3은 각각 1줄, 단계 4는 2줄(미탐 수 · 놓친 문제), 단계 5는 1줄입니다.
5. **[보고서]** `report_u8.md` 의 `## 실습 8-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 한 문장 요약을 적어 주세요.
   - (나) [핵심 질문] 로그인 규칙의 알림을 합치자 놓친 문제가 몇 개에서 몇 개로 줄었나요? P4 가 잡힌 이유와, 오탐이 늘지 않은 이유를 함께 적어 주세요.
   - (다) [핵심 질문] 아직 놓친 P5(seoyeon 의 권한 없는 정산 조회 시도)를 찾으려면 어떤 규칙이 필요하고, 그 규칙을 더하면 오탐이 늘 수 있는 이유는 무엇인지 적어 주세요.

## 실습 8-3 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 표 두 개를 위아래로 이어 붙이기 | `all_alerts = pd.concat([alerts, login_alerts])` |
| 빈 값 지우기 | `caught_ids = all_alerts["problem"].dropna()` |
| 리스트 안에 있는지 | `is_caught = problems["id"].isin(caught_ids)` |
| 조건 뒤집기 | `is_missed = ~is_caught` |
| 숫자를 문자열로 바꿔 이어 붙이기 | `"알림 " + str(alert_count) + "개 중 …"` |

---

## 마무리 · 이번 Unit 작업 확인하기

이번 Unit의 작업을 깃허브에 올리는 일은 Unit 9의 실습 9-2 마지막에 한 번에 합니다. <mark>이번 Unit에서는 파일이 모두 있는지만 확인합니다</mark>.

<h2>순서</h2>

1. **[터미널]** `anomaly_detection` 폴더에서 <mark>이번 Unit에서 만든 파일이 있는지 확인합니다.</mark>
   ```bash
   pwd
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
   - `evaluation.py` · `tuning.py` · `final_check.py` · `exercise8-1_run.py` · `exercise8-2_run.py` · `exercise8-3_run.py` · `review_alerts.json` · `problems.json` · `login_alerts.json` 과 `report_u8.md` 가 보여야 합니다.
2. **[보고서]** `report_u8.md` 의 실습 8-1 · 8-2 · 8-3 칸에서 <mark>`답:` 뒤가 비어 있는 질문이 없는지</mark> 봅니다. 못 적은 칸은 `모름 — 막힌 곳: …` 으로 적습니다.

---

## 이번 Unit 마무리

| 확인 | 문제 |
|---|---|
| 알림 7개 중 오탐 4개, 진짜 문제 5개 중 미탐 2개를 세었다 | 실습 8-1 |
| 믿는 IP 예외 규칙으로 오탐을 4개에서 2개로 줄이고, 진짜 문제가 지워지지 않았음을 확인했다 | 실습 8-2 |
| 로그인 규칙의 알림을 합쳐 놓친 문제를 2개에서 1개로 줄이고 한 문장으로 요약했다 | 실습 8-3 |

Unit 9에서는 도커 컴포즈로 서버를 켜고, <mark>정상 요청과 스캐너 요청을 보내 로그를 만든 뒤</mark> Unit 10의 통합 실습에 쓸 로그를 저장합니다.

---

<!-- learn:answers -->
