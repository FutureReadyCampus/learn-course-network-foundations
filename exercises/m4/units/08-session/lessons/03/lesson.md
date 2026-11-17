---
id: m4-u08-l03
title: 3교시 (11:00–11:50) · 예외 규칙 하나로 오탐 줄이기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/110_day05_am_false_alarm_tuning.md
  mission_id: GichanSource.m4-1106-am-false-alarm-tuning
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 3교시 (11:00–11:50) · 예외 규칙 하나로 오탐 줄이기

## 3교시 (11:00–11:50) · 예외 규칙 하나로 오탐 줄이기

> 📨 **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「오탐 4건 중 'SaaS 평소와 다른 IP' 알림 2건(알림 번호 `A4` jiwoo · `A5` seoyeon, `review_alerts.json` 에 있습니다)은 모두 협력사 사무실 IP `203.0.113.80` 에서 로그인한 것이었습니다. 협력사 사무실은 직원이 출장이나 외근으로 자주 쓰는 곳입니다.
>
> 이 IP 에서 온 'SaaS 평소와 다른 IP' 알림만 빠지도록 규칙을 고쳐 주세요. 단, 진짜 문제까지 같이 지워지면 안 됩니다.」
> - **왜 중요한가**: <mark>같은 원인의 오탐을 규칙 하나로 줄이면 담당자가 매일 열어 보는 알림이 줄지만, 예외를 넓게 만들면 진짜 문제까지 지워질 수 있습니다.</mark>

> 📖 **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「✍️ 문제」 전까지는 이 교시의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다. (판다스 문법 상자의 코드는 눈으로 읽으면 됩니다.)

## 📖 왜 필요한가

> 📖 **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 오탐을 줄이는 가장 쉬운 방법은 **예외 규칙**입니다. 「이 IP 에서 온 이 규칙의 알림은 뺀다」처럼 조건을 정해 틀린 알림을 빼냅니다.
2. 오늘 질문은 하나입니다. <mark>**예외 규칙 하나로 오탐을 몇 개 줄일 수 있고, 진짜 문제는 지워지지 않았는가?**</mark>
3. 예외는 **한 규칙에만** 적용합니다. 같은 IP `203.0.113.80` 에서 온 알림이라도 다른 규칙의 알림은 그대로 둡니다.

## 📖 3.1 같은 IP 에서 온 알림 네 개

> 📖 **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

`203.0.113.80` 에서 온 알림은 A3 · A4 · A5 · A6 네 개입니다. A1 · A2 는 서버 알림이라 IP 가 없어서 이 표에서 뺐습니다. 예외 규칙은 `IP_RULE`(SaaS 평소와 다른 IP)의 알림 중 믿는 IP 에서 온 것만 뺍니다.

| id | 규칙 | 대상 | real | 예외 규칙이 빼는가 |
|---|---|---|---|---|
| A3 | SaaS 업무 시간 밖 로그인 | jiwoo | `False` | 아니오 (다른 규칙) |
| A4 | SaaS 평소와 다른 IP | jiwoo | `False` | **예** |
| A5 | SaaS 평소와 다른 IP | seoyeon | `False` | **예** |
| A6 | SaaS 대량 다운로드 | seoyeon | `True` | 아니오 (다른 규칙) |

- A4 · A5 두 개가 빠지면 오탐은 4개에서 2개(A2 · A3)로 줄어듭니다.
- <mark>A6 은 같은 IP 에서 왔지만 진짜 문제입니다.</mark> 규칙을 가리지 않고 이 IP 의 알림을 모두 빼면 A6 까지 지워집니다.
- <mark style="background:#ffc4d6">예외에는 위험도 있습니다. 믿는 IP 에서 누군가 계정을 도용해 로그인해도, 그 규칙은 알림을 내지 않습니다.</mark>

**🐼 판다스 문법 상자 — 같은 값을 한 번씩만 꺼내기 `.unique()`**

**<mark>`열.unique()`</mark> 는 열에서 같은 값을 한 번씩만 모아 줍니다**

아래는 알림이 난 기록이고, 같은 사용자가 여러 번 나옵니다. 어떤 사용자가 나왔는지만 한 번씩 봅니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                          # 표에 넣을 내용(열 이름: 값들)
    "user": ["dami", "gaeun", "dami", "seoyeon", "dami"],         # user 열
    "action": ["login", "login", "download", "login", "upload"],  # action 열
}
df = pd.DataFrame(data)                                           # 내용으로 표(DataFrame)를 만든다
print(df)                                                         # 표를 출력한다
```

실행 결과:

```
      user    action
0     dami     login
1    gaeun     login
2     dami  download
3  seoyeon     login
4     dami    upload
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
users = df["user"].unique()  # user 열에서 같은 값을 한 번씩만 꺼낸다
print(users)                 # 사용자 이름을 출력한다
```

실행 결과:

```
['dami' 'gaeun' 'seoyeon']
```

- 읽는 법: 표에는 사용자가 다섯 번 나오지만, <mark style="background:#bde3ff">두 번째 출력에는 `dami` · `gaeun` · `seoyeon` 이 한 번씩만</mark> 나옵니다. 처음 나온 순서대로 나옵니다.
- 출력의 `[` `]` 안에 따옴표로 묶인 이름이 공백으로 이어지는 모양은 정상입니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_table` · `count_false_alarms` | 파일 경로 · 알림 표 | 표 · 오탐 수(미리 채움) |
| `apply_exception` | 알림 표 | 빼낸 알림 표와 남은 알림 표 |
| `count_real_removed` | 빼낸 알림 표 | 빼낸 알림 중 진짜 문제였던 알림 수 |
| `find_removed_users` | 빼낸 알림 표 | 빼낸 알림에 나온 사용자(중복 없이) |

- **직접 쓰는 곳은 일곱 군데**(번호 1 ~ 7)이고, 함수 세 개 안에 나뉘어 있습니다.
  - `apply_exception`(1 ~ 4번, 4곳): 알림의 규칙이 IP 규칙인지 비교하고, 믿는 IP 인지 구하고, 둘을 합쳐 빼낼 알림을 정한 뒤, 남은 알림을 고릅니다.
  - `count_real_removed`(5 · 6번, 2곳): 빼낸 알림 중 진짜 문제였던 것을 고릅니다.
  - `find_removed_users`(7번, 1곳): 빼낸 알림에 나온 사용자를 중복 없이 꺼냅니다.
- 오늘 새 문법은 `.unique()` 하나입니다. 이번 주에 쓴 `isin` · `&` 와 2교시의 `~` 는 다시 씁니다.

> ✍️ **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## ✍️ 문제 3-1 · 믿는 IP 예외 규칙으로 오탐 줄이기

**📍 이런 상황이 있습니다**

- **지금은**: <mark>협력사 사무실 IP 에서 온 'SaaS 평소와 다른 IP' 알림이 오탐으로 계속 쌓입니다</mark>.
- **그래서 만드는 것**: `tuning.py` 입니다.
  - IP 규칙의 알림 중 믿는 IP 에서 온 것을 찾아 빼냅니다.
  - 적용 전과 후의 오탐 수를 비교합니다.
  - 빼낸 알림 중 진짜 문제가 있었는지 확인합니다.
  - 빼낸 알림에 나온 사용자를 중복 없이 모읍니다.
- **실행하면**: <mark>단계 1: 적용 전 알림 수와 오탐 수, 단계 2: 빠진 알림과 그 사용자, 단계 3: 적용 후 알림 수와 오탐 수, 단계 4: 빠진 알림 중 진짜 문제였던 알림 수(0이면 진짜 문제는 지워지지 않은 것)가 나옵니다.</mark>
- **현업에서는**: 예외를 넣을 때마다 「빠진 알림 중 진짜 문제가 있는가」를 확인합니다. 예외 리스트는 근거(협력사 사무실 IP)와 함께 기록해 두어야 나중에 지울 수 있습니다.

**🎯 할 일**

1. `tuning.py` · `day05_3-1_run.py` 두 파일을 만들고, `tuning.py` 의 세 함수에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>적용 전 오탐 수</mark>(단계 1), <mark>빠진 알림</mark>(단계 2), <mark>적용 후 오탐 수</mark>(단계 3), <mark>빠진 알림 중 진짜 문제였던 알림 수</mark>(단계 4)를 읽습니다.

**`tuning.py`**

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다

ALERTS_PATH = "review_alerts.json"                    # 읽을 알림 파일 이름
IP_RULE = "SaaS 평소와 다른 IP"                       # 예외를 적용할 규칙 이름
TRUSTED_IPS = ["203.0.113.80"]                        # 믿는 IP 리스트 : 협력사 사무실 IP 한 개


def load_table(path):                                 # 파일 경로를 받는 함수
    """JSON 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    table = pd.read_json(path)                        # 파일 속 내용을 표 한 개로 읽는다
    return table                                      # 표를 리턴한다


def count_false_alarms(alerts):                       # 알림 표를 받는 함수
    """진짜 문제가 아니었는데 난 알림(오탐)이 몇 개인지 센다.
    튜닝 전과 후를 비교할 때 쓴다.
    """
    is_real = alerts["real"]                          # real 열(진짜 문제이면 True)을 꺼낸다
    is_false = ~is_real                               # 문제가 아니었던 알림을 True 로 만든다
    false_alarms = alerts[is_false]                   # True 인 행만 골라 새 표로 만든다
    false_alarm_count = len(false_alarms)             # 오탐이 몇 개인지 센다
    return false_alarm_count                          # 오탐 개수를 리턴한다


def apply_exception(alerts):                          # 알림 표를 받는 함수
    """IP 규칙 알림 중 믿는 IP 에서 온 것만 빼낸다.
    오탐을 줄이는 예외 규칙을 적용할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. alerts 의 "rule" 열이 IP_RULE 과 같은지 비교해 is_ip_rule 에 담는다
    # 2. alerts 의 "ip" 열이 TRUSTED_IPS 안에 있는지 isin 으로 구해 is_trusted 에 담는다
    # 3. is_ip_rule 과 is_trusted 가 모두 True 인 행을 & 로 구해 is_removed 에 담는다
    removed_alerts = alerts[is_removed]               # 빼낼 알림만 골라 새 표로 만든다
    is_kept = ~is_removed                             # 빼지 않을 알림을 True 로 만든다
    # 4. alerts 에서 is_kept 가 True 인 행만 골라 kept_alerts 에 담는다
    return removed_alerts, kept_alerts                # 빼낸 알림 표와 남은 알림 표를 리턴한다


def count_real_removed(removed_alerts):               # 빼낸 알림 표를 받는 함수
    """빼낸 알림 중 진짜 문제였던 것이 몇 개인지 센다.
    예외 규칙이 진짜 문제를 지우지 않았는지 확인할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. removed_alerts 의 "real" 열을 꺼내 is_real_removed 에 담는다
    # 6. removed_alerts 에서 is_real_removed 가 True 인 행만 골라 real_removed 에 담는다
    real_removed_count = len(real_removed)            # 진짜 문제였던 알림이 몇 개 빠졌는지 센다
    return real_removed_count                         # 그 개수를 리턴한다


def find_removed_users(removed_alerts):               # 빼낸 알림 표를 받는 함수
    """빼낸 알림에 나온 사용자를 중복 없이 모은다.
    예외로 빠진 알림이 누구의 것인지 확인할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. removed_alerts 의 "user" 열에서 같은 값은 한 번씩만 .unique() 로 꺼내 removed_users 에 담는다
    return removed_users                              # 중복 없는 사용자 이름을 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 7번은 모두 함수 안이라 앞에 공백 4개입니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.**
- 채우기 전에 실행하면 `NameError: name 'is_removed' is not defined` 오류가 납니다. 3번을 아직 안 썼기 때문입니다.

**`day05_3-1_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다.

```python
from tuning import load_table, count_false_alarms, apply_exception, count_real_removed, find_removed_users, ALERTS_PATH  # 방금 만든 함수를 불러온다

alerts = load_table(ALERTS_PATH)                      # 알림 파일을 표로 읽는다
alert_count = len(alerts)                             # 알림이 모두 몇 개인지 센다
false_alarm_count_before = count_false_alarms(alerts)  # 예외 규칙을 적용하기 전의 오탐 수를 센다
print("--- 단계 1: 예외 규칙을 적용하기 전 ---")      # 단계 1 제목
print("알림 수:", alert_count)                        # 적용 전 알림 수를 출력한다
print("오탐 수:", false_alarm_count_before)           # 적용 전 오탐 수를 출력한다

removed_alerts, kept_alerts = apply_exception(alerts)  # 믿는 IP 에서 온 IP 규칙 알림을 빼낸다
removed_count = len(removed_alerts)                   # 빠진 알림이 몇 개인지 센다
print("--- 단계 2: 예외 규칙으로 빠진 알림 ---")      # 단계 2 제목
print("빠진 알림 수:", removed_count)                 # 빠진 알림 수를 출력한다
removed_list = removed_alerts.to_dict("records")      # 표를 알림 딕셔너리 리스트로 바꾼다
for alert in removed_list:                            # 빠진 알림을 하나씩 꺼낸다
    print("빠진 알림:", alert["id"], alert["rule"], alert["user"], alert["ip"])  # 번호 · 규칙 · 사용자 · IP 를 출력한다
removed_users = find_removed_users(removed_alerts)    # 빠진 알림에 나온 사용자를 중복 없이 모은다
print("빠진 알림의 사용자:", removed_users)           # 사용자 이름을 출력한다

kept_count = len(kept_alerts)                         # 남은 알림이 몇 개인지 센다
false_alarm_count_after = count_false_alarms(kept_alerts)  # 적용 후의 오탐 수를 센다
print("--- 단계 3: 예외 규칙을 적용한 뒤 ---")        # 단계 3 제목
print("알림 수:", kept_count)                         # 적용 후 알림 수를 출력한다
print("오탐 수:", false_alarm_count_after)            # 적용 후 오탐 수를 출력한다

real_removed_count = count_real_removed(removed_alerts)  # 빠진 알림 중 진짜 문제였던 것을 센다
print("--- 단계 4: 빠진 알림 중 진짜 문제였던 것 ---")  # 단계 4 제목
print("진짜 문제였던 알림 수:", real_removed_count)   # 0 이면 진짜 문제는 지워지지 않은 것이다
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `tuning.py` · `day05_3-1_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `tuning.py` 에서 <mark>직접 쓰는 곳 일곱 군데를 씁니다</mark>. 2교시에서 쓴 방식과 위 판다스 문법 상자, 3.1 의 표를 참고해 씁니다. 막히면 아래 「3교시 한눈에」를 봅니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python day05_3-1_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python day05_3-1_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1은 2줄(알림 수 · 오탐 수), 단계 2는 4줄(빠진 알림 수 1줄 · 빠진 알림 2줄 · 사용자 1줄), 단계 3은 2줄, 단계 4는 1줄입니다.
5. **[보고서]** `day05_am_report.md` 의 `## 3교시` › `### 문제 3-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 적용 전후의 오탐 수와 빠진 알림을 적어 주세요.
   - (나) 🔍 예외 규칙을 적용한 뒤 오탐이 몇 개에서 몇 개로 줄었나요? A3(jiwoo 의 업무 시간 밖 로그인)은 같은 IP 인데 왜 줄어들지 않았는지도 적어 주세요.
   - (다) 🔍 `SaaS 평소와 다른 IP` 규칙에서 `203.0.113.80` 을 믿는 IP 로 두면, 이 IP 에서 오는 진짜 공격을 그 규칙으로는 놓칠 수 있습니다. 어떤 경우인지 한 가지 적어 주세요.

## 3교시 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 값이 같은지 비교 | `is_ip_rule = alerts["rule"] == IP_RULE` |
| 리스트 안에 있는지 | `is_trusted = alerts["ip"].isin(TRUSTED_IPS)` |
| 두 조건이 모두 맞는 행 | `is_removed = is_ip_rule & is_trusted` |
| 조건에 맞는 행만 | `kept_alerts = alerts[is_kept]` |
| 같은 값을 한 번씩만 | `removed_users = removed_alerts["user"].unique()` |

---
