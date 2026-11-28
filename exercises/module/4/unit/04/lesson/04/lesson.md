---
id: m4-u04-l04
title: 실습 4-2 · 예외 규칙으로 오탐 줄이기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/110_day05_am_false_alarm_tuning.md
  mission_id: GichanSource.m4-1106-am-false-alarm-tuning
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 4-2 · 예외 규칙으로 오탐 줄이기

## 목표: 믿는 IP 예외 규칙

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「11/2 의 알림 7건을 조사해 보니 문제가 아닌 알림이 4건이었습니다. 그중 'SaaS 평소와 다른 IP' 알림 2건(알림 번호 `A4` jiwoo · `A5` seoyeon, `review_alerts.json` 에 있습니다)은 모두 협력사 사무실 IP `203.0.113.80` 에서 로그인한 것이었습니다. 협력사 사무실은 직원이 출장이나 외근으로 자주 쓰는 곳입니다.
>
> 이 IP 에서 온 'SaaS 평소와 다른 IP' 알림만 빠지도록 규칙을 고쳐 주세요. 단, 진짜 문제까지 같이 지워지면 안 됩니다.」
> - **왜 중요한가**: <mark>같은 원인의 오탐을 규칙 하나로 줄이면 담당자가 매일 열어 보는 알림이 줄지만, 예외를 넓게 만들면 진짜 문제까지 지워질 수 있습니다.</mark>
> - **직접 쓰는 것**: 대부분은 미리 채워 두었고, 예외 조건 두 줄(① · ②)과 사용자를 모으는 한 줄(③)만 직접 씁니다.
> - **끝나면 쓰는 것**: 자기 점검 질문 (가) · (나) 답. (다)는 여유가 되면 하는 응용입니다.

## 왜 예외를 한 규칙에만 거는가

1. 문제가 아닌데 난 알림을 **오탐**(false positive, 폴스 포지티브)이라고 합니다. 오탐을 줄이는 가장 쉬운 방법은 **예외 규칙**(튜닝: 규칙을 고쳐 틀린 알림을 줄이는 일)입니다. 「이 IP 에서 온 이 규칙의 알림은 뺀다」처럼 조건을 정해 틀린 알림을 빼냅니다.
2. 이번 실습의 질문은 하나입니다. <mark>**예외 규칙 하나로 오탐을 몇 개 줄일 수 있고, 진짜 문제는 지워지지 않았는가?**</mark>
3. 예외는 **한 규칙에만** 적용합니다. 같은 IP `203.0.113.80` 에서 온 알림이라도 다른 규칙의 알림은 그대로 둡니다.

## 2.1 같은 IP 에서 온 알림 네 개

`203.0.113.80` 에서 온 알림은 A3 · A4 · A5 · A6 네 개입니다. A1 · A2 는 서버 알림이라 IP 가 없어서 이 표에서 뺐습니다. 예외 규칙은 `SaaS 평소와 다른 IP` 규칙(코드에서는 이 이름을 `IP_RULE` 에 담습니다)의 알림 중 믿는 IP 에서 온 것만 뺍니다.

| id | 규칙 | 대상 | real | 예외 규칙이 빼는가 |
|---|---|---|---|---|
| A3 | SaaS 업무 시간 밖 로그인 | jiwoo | `False` | 아니오 (다른 규칙) |
| A4 | SaaS 평소와 다른 IP | jiwoo | `False` | **예** |
| A5 | SaaS 평소와 다른 IP | seoyeon | `False` | **예** |
| A6 | SaaS 대량 다운로드 | seoyeon | `True` | 아니오 (다른 규칙) |

- A4 · A5 두 개가 빠지면 오탐은 4개에서 2개(A2 · A3)로 줄어듭니다.
- <mark>A6 은 같은 IP 에서 왔지만 진짜 문제입니다.</mark> 규칙을 가리지 않고 이 IP 의 알림을 모두 빼면 A6 까지 지워집니다.
- <mark style="background:#ffc4d6">예외에는 위험도 있습니다. 믿는 IP 에서 누군가 계정을 도용해 로그인해도, 그 규칙은 알림을 내지 않습니다.</mark>

<h2>판다스 문법 상자 — 같은 값을 한 번씩만 꺼내기 <code>.unique()</code></h2>

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
<StringArray>
['dami', 'gaeun', 'seoyeon']
Length: 3, dtype: str
```

- 읽는 법: 표에는 사용자가 다섯 번 나오지만, <mark style="background:#bde3ff">두 번째 출력에는 `dami` · `gaeun` · `seoyeon` 이 한 번씩만</mark> 나옵니다. 처음 나온 순서대로 나옵니다.
- 위아래의 `<StringArray>` 줄과 `Length: 3, dtype: str` 줄은 결과의 종류와 개수를 알려 주는 표시이고 읽지 않아도 됩니다. 판다스 2 에서는 이 두 줄 없이 `['dami' 'gaeun' 'seoyeon']` 처럼 쉼표 없는 한 줄로 나오는데, 내용은 같습니다.
- 실습의 실행 파일은 이 결과를 `list(…)` 로 리스트로 바꿔 출력하므로, `['jiwoo', 'seoyeon']` 처럼 쉼표가 있는 모양으로 나옵니다.

**미리 채운 줄의 `~`**

`~조건` 은 `True` 는 `False` 로, `False` 는 `True` 로 뒤집습니다. 열에는 파이썬의 `not` 대신 `~` 를 씁니다. 이번 실습에서는 `~is_real`(진짜 문제가 아닌 알림)과 `~is_removed`(빼지 않을 알림) 두 줄이 미리 채워져 있습니다.

<h2>한 장 정리</h2>

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_table` · `count_false_alarms` | 파일 경로 · 알림 표 | 표 · 오탐 수(미리 채움) |
| `apply_exception` | 알림 표 | 빼낸 알림 표와 남은 알림 표 · **① · ②** |
| `count_real_removed` | 빼낸 알림 표 | 빼낸 알림 중 진짜 문제였던 알림 수(미리 채움) |
| `find_removed_users` | 빼낸 알림 표 | 빼낸 알림에 나온 사용자(중복 없이) · **③** |

- **직접 쓰는 곳은 세 곳**(① · ② · ③)입니다. `apply_exception` 의 믿는 IP 구하기(①)와 두 조건 합치기(②), `find_removed_users` 의 `.unique()` 한 줄(③)입니다.

- 이번 실습에서 새 문법은 `.unique()` 하나입니다. `isin` 은 Unit 3 실습 3-2, `&` 는 Unit 2 실습 2-3에서 쓴 것을 다시 씁니다.

> **확인** — 문법 상자의 두 코드를 이어 실행했을 때 `['dami', 'gaeun', 'seoyeon']` 처럼 세 이름이 한 번씩 나오면 성공입니다. 판다스 2 에서는 쉼표 없이 `['dami' 'gaeun' 'seoyeon']` 한 줄로 나와도 맞습니다.
>
> 실행하는 법: 실습 4-1에서 만든 연습 파일 `try_box.py` 의 내용을 모두 지우고(없으면 `anomaly_detection` 폴더에 새로 만들고) 두 코드를 차례로 붙여 넣어 저장한 뒤, 터미널에서 `python try_box.py` 를 칩니다.

## 실습 4-2 · 예외 규칙으로 오탐 줄이기

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>협력사 사무실 IP 에서 온 'SaaS 평소와 다른 IP' 알림이 오탐으로 계속 쌓입니다</mark>.
- **그래서 만드는 것**: `tuning.py` 입니다.
  - IP 규칙의 알림 중 믿는 IP 에서 온 것을 찾아 빼냅니다.
  - 적용 전과 후의 오탐 수를 비교합니다.
  - 빼낸 알림 중 진짜 문제가 있었는지 확인합니다.
  - 빼낸 알림에 나온 사용자를 중복 없이 모읍니다.
- **실행하면**: <mark>단계 1: 적용 전 알림 수와 오탐 수, 단계 2: 빠진 알림과 그 사용자, 단계 3: 적용 후 알림 수와 오탐 수, 단계 4: 빠진 알림 중 진짜 문제였던 알림 수(0이면 진짜 문제는 지워지지 않은 것)가 나옵니다.</mark>
- **현업에서는**: 예외를 넣을 때마다 「빠진 알림 중 진짜 문제가 있는가」를 확인합니다. 예외 리스트는 근거(협력사 사무실 IP)와 함께 기록해 두어야 나중에 지울 수 있습니다.

<h2>할 일</h2>

1. `tuning.py` · `exercise4-2_run.py` 두 파일을 만들고, `tuning.py` 에서 `# ←` 가 있는 <mark>세 곳</mark>(① · ② · ③)을 한 줄씩 채웁니다. 나머지 줄은 미리 채워 두었습니다.
2. 실행해서 <mark>적용 전 오탐 수</mark>(단계 1), <mark>빠진 알림</mark>(단계 2), <mark>적용 후 오탐 수</mark>(단계 3), <mark>빠진 알림 중 진짜 문제였던 알림 수</mark>(단계 4)를 읽습니다.

<h3><code>tuning.py</code></h3>

```python exercise
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
    is_ip_rule = alerts["rule"] == IP_RULE            # 각 알림이 IP 규칙의 알림인지 비교한다
    # ① alerts 의 "ip" 열이 TRUSTED_IPS 안에 있는지 isin 으로 구해 is_trusted 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
#|     is_trusted = alerts["ip"].isin(TRUSTED_IPS)
    # ② is_ip_rule 과 is_trusted 가 모두 True 인 행을 & 로 구해 is_removed 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
#|     is_removed = is_ip_rule & is_trusted
    removed_alerts = alerts[is_removed]               # 빼낼 알림만 골라 새 표로 만든다
    is_kept = ~is_removed                             # 빼지 않을 알림을 True 로 만든다
    kept_alerts = alerts[is_kept]                     # True 인 행만 골라 새 표로 만든다
    return removed_alerts, kept_alerts                # 빼낸 알림 표와 남은 알림 표를 리턴한다


def count_real_removed(removed_alerts):               # 빼낸 알림 표를 받는 함수
    """빼낸 알림 중 진짜 문제였던 것이 몇 개인지 센다.
    예외 규칙이 진짜 문제를 지우지 않았는지 확인할 때 쓴다.
    """
    is_real_removed = removed_alerts["real"]          # real 열(진짜 문제이면 True)을 꺼낸다
    real_removed = removed_alerts[is_real_removed]    # True 인 행만 골라 새 표로 만든다
    real_removed_count = len(real_removed)            # 진짜 문제였던 알림이 몇 개 빠졌는지 센다
    return real_removed_count                         # 그 개수를 리턴한다


def find_removed_users(removed_alerts):               # 빼낸 알림 표를 받는 함수
    """빼낸 알림에 나온 사용자를 중복 없이 모은다.
    예외로 빠진 알림이 누구의 것인지 확인할 때 쓴다.
    """
    # ③ removed_alerts 의 "user" 열에서 같은 값은 한 번씩만 .unique() 로 꺼내 removed_users 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
#|     removed_users = removed_alerts["user"].unique()
    return removed_users                              # 중복 없는 사용자 이름을 리턴한다
```

- 주석 줄은 그대로 두고, **각 주석 바로 아래 줄**에 씁니다. ① ~ ③ 모두 함수 안이라 앞에 공백 4칸입니다.

<h3>직접 쓰는 곳</h3>

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | 믿는 IP 인지 `is_trusted` (`isin`) | 4칸 |
| ② | 두 조건을 합친 `is_removed` (`&`) | 4칸 |
| ③ | 빠진 사용자 `removed_users` (`.unique()`) | 4칸 |

- 채우기 전 확인: 그대로 실행하면 단계 1(알림 수 · 오탐 수) 다음에 `NameError: name 'is_removed' is not defined` 가 나옵니다. ② 를 아직 안 써서 나는 오류이니 정상입니다.
- ① 확인: ① 만 쓰고 실행해도 같은 `NameError: name 'is_removed' is not defined` 가 나옵니다. 이때는 ① 줄에 문법 오류가 없다는 것까지만 알 수 있고, ① 이 맞는지는 ② 까지 쓴 뒤 `빠진 알림 수: 2` 가 나오는지로 확인합니다. ① 을 `alerts["ip"] == TRUSTED_IPS` 처럼 잘못 쓰면 ① 줄에서 `ValueError` 가 납니다. 막히면: Unit 3 실습 3-2의 `isin` 처럼 `alerts["ip"].isin(…)` 괄호 안에 `TRUSTED_IPS` 를 넣습니다.
- ② 확인: ② 까지 쓰고 실행하면 단계 2에 `빠진 알림 수: 2` 와 A4 · A5 두 줄이 나온 뒤 `NameError: name 'removed_users' is not defined` 가 나옵니다. ③ 을 아직 안 써서 나는 오류입니다. 오류 끝에 `. Did you mean: 'removed_alerts'?` 처럼 꼬리가 더 붙어도 같은 오류입니다. 막히면: 두 변수 이름 사이에 `&` 를 놓고 `is_removed =` 에 담습니다.
- ③ 확인: ③ 까지 쓰고 실행하면 `빠진 알림의 사용자: ['jiwoo', 'seoyeon']` 과 마지막 줄 `진짜 문제였던 알림 수: 0` 이 나오면 성공입니다. 막히면: 문법 상자의 `df["user"].unique()` 에서 `df` 를 `removed_alerts` 로 바꿉니다.

<h3><code>exercise4-2_run.py</code></h3>

그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다.

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
print("빠진 알림의 사용자:", list(removed_users))     # 사용자 이름을 리스트로 바꿔 출력한다

kept_count = len(kept_alerts)                         # 남은 알림이 몇 개인지 센다
false_alarm_count_after = count_false_alarms(kept_alerts)  # 적용 후의 오탐 수를 센다
print("--- 단계 3: 예외 규칙을 적용한 뒤 ---")        # 단계 3 제목
print("알림 수:", kept_count)                         # 적용 후 알림 수를 출력한다
print("오탐 수:", false_alarm_count_after)            # 적용 후 오탐 수를 출력한다

real_removed_count = count_real_removed(removed_alerts)  # 빠진 알림 중 진짜 문제였던 것을 센다
print("--- 단계 4: 빠진 알림 중 진짜 문제였던 것 ---")  # 단계 4 제목
print("진짜 문제였던 알림 수:", real_removed_count)   # 0 이면 진짜 문제는 지워지지 않은 것이다
```

<h2>순서</h2>

1. **[VS Code]** `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 로 `tuning.py` 와 `exercise4-2_run.py` 를 만들어 위 코드를 각각 붙여 넣고 저장합니다.
2. **[VS Code]** `tuning.py` 의 <mark>`# ←` 세 곳(① · ② · ③)을 채웁니다</mark>. 위 판다스 문법 상자와 「같은 IP 에서 온 알림 네 개」 쪽의 표를 참고해 씁니다. 막히면 위 「직접 쓰는 곳」의 힌트와 아래 「실습 4-2 정리」를 봅니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 `tuning.py` 를 만들어 붙여 넣고, 빈칸 ① · ② · ③ 을 채워 저장했다
- [ ] `anomaly_detection` 폴더에 `exercise4-2_run.py` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다.
   ```bash
   pwd
   python exercise4-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise4-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **네 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1은 2줄(알림 수 · 오탐 수), 단계 2는 4줄(빠진 알림 수 1줄 · 빠진 알림 2줄 · 사용자 1줄), 단계 3은 2줄, 단계 4는 1줄입니다.

<!-- checklist -->
- [ ] `python exercise4-2_run.py` 를 실행해 단계 3이 `알림 수: 5` · `오탐 수: 2`, 마지막 줄이 `진짜 문제였던 알림 수: 0` 으로 나왔다
<!-- /checklist -->

5. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.
   - (가) [핵심 질문] 실행한 출력을 보고, 적용 전후의 오탐 수와 빠진 알림을 적어 주세요.
   - (나) [핵심 질문] 예외 규칙을 적용한 뒤 오탐이 몇 개에서 몇 개로 줄었나요? A3(jiwoo 의 업무 시간 밖 로그인)은 같은 IP 인데 왜 줄어들지 않았는지도 적어 주세요.
   - (다) [응용] `SaaS 평소와 다른 IP` 규칙에서 `203.0.113.80` 을 믿는 IP 로 두면, 이 IP 에서 오는 진짜 공격을 그 규칙으로는 놓칠 수 있습니다. 어떤 경우인지 한 가지 적어 주세요.

**확인** — 단계 3이 `알림 수: 5` · `오탐 수: 2` 이고 마지막 줄이 `진짜 문제였던 알림 수: 0` 이면 성공입니다. 안 나오면 실습 4-2 하단 바의 ‘정답 보기’로 연 해설의 출력과 한 줄씩 맞춰 보고, `빠진 알림 수: 4` 가 나오면 ② 에 `is_ip_rule &` 가 빠졌는지 봅니다.

## 실습 4-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 값이 같은지 비교(미리 채움) | `is_ip_rule = alerts["rule"] == IP_RULE` |
| ① 리스트 안에 있는지 | `is_trusted = alerts["ip"].isin(TRUSTED_IPS)` |
| ② 두 조건이 모두 맞는 행 | `is_removed = is_ip_rule & is_trusted` |
| 조건에 맞는 행만(미리 채움) | `kept_alerts = alerts[is_kept]` |
| ③ 같은 값을 한 번씩만 | `removed_users = removed_alerts["user"].unique()` |

---

## 작업물 점검 및 GitHub 반영

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개를 끝낸 뒤 합니다. 응용을 하지 않았어도 이 순서대로 마무리하면 됩니다.

<h2>1. 오늘 한 일 확인</h2>

1. 탐지된 규칙 8건((대상, 규칙) 쌍)에 점수를 더해 대상 5개를 high · mid · low 로 나누고, 점수 · 등급 · 이유를 `unit05_risk_scores.json` 에 저장했다 (실습 4-1)
2. 믿는 IP 예외 규칙으로 오탐을 4개에서 2개로 줄이고, 빠진 알림 중 진짜 문제가 0개임을 확인했다 (실습 4-2)
3. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.

<h2>2. 파일 확인</h2>

**[터미널]** `anomaly_detection` 폴더에서 확인합니다.

```bash
pwd
ls
```

- `pwd` 의 결과가 `anomaly_detection` 으로 끝나야 합니다.
- `ls` 결과에 아래 파일이 보여야 합니다.

| 만든 곳 | 파일 |
|---|---|
| 핵심 입력 | `risk_inputs.json` |
| 실습 4-1 | `risk_scores.py` · `exercise4-1_run.py` · `unit05_risk_scores.json` |
| 실습 4-2 | `review_alerts.json` · `tuning.py` · `exercise4-2_run.py` |

- `unit05_risk_scores.json` 은 실습 4-1에서 프로그램이 만든 점수 파일입니다. 이것도 올라갑니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에서 `ls` 로 「2. 파일 확인」 표의 파일이 모두 있는 것을 확인했다
<!-- /checklist -->

<h2>3. 깃허브에 올리기</h2>

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 메뉴 **Terminal › New Terminal** 로 터미널을 새로 엽니다(이름 칸이 **bash** 인지 봅니다). 새 터미널은 `…/network-study-notes` 에서 열립니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `anomaly_detection/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git status` 를 보고, `.env` · `.venv` 가 올라가지 않게 했다
<!-- /checklist -->

4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add anomaly detection unit 4 risk scores and false alarm tuning"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `git add .` · `git commit` · `git push` 로 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소 `network-study-notes` 를 새로 고쳐 `anomaly_detection` 폴더를 열고, 「2. 파일 확인」 표의 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.

<!-- checklist -->
- [ ] 깃허브의 `network-study-notes` 저장소 `anomaly_detection` 폴더에서 「2. 파일 확인」 표의 파일을 확인했다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 「2. 파일 확인」부터 「3. 깃허브에 올리기」의 4번(`git add .` · `git commit` · `git push`)까지를 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**확인** — 깃허브의 `anomaly_detection` 폴더에 「2. 파일 확인」 표의 파일이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이는 파일이 있으면 `git status` 를 다시 쳐서 그 파일이 빨간 목록에 남아 있는지 보고 「3. 깃허브에 올리기」의 4번을 다시 합니다.

<h2>4. 이어지는 곳</h2>

1. 다음 Unit 5(AI 요약과 총정리)에서는 오늘 저장한 점수 파일의 사실만 골라 AI 에게 요약을 받고, 상황별 원인과 해결법을 정리합니다.
2. Unit 5 시작하기 레슨에서 `unit05_risk_scores.json` 을 같은 내용으로 다시 만들기 때문에, 오늘 파일이 달라도 다음 Unit은 그대로 따라갈 수 있습니다.

---

<!-- learn:answers -->
<!-- answer: 08|실습 4-2 정답 -->
