---
id: m3-u05-l02
title: 실습 5-1 · 점검 체크리스트로 어긋난 곳 찾기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/094_day06_am_weekly_report.md
  mission_id: GichanSource.m3-1102-am-weekly-report
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 5-1 · 점검 체크리스트로 어긋난 곳 찾기

## 목표: 점검 체크리스트 결과

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지:
> 「앞서 회수를 마쳤는데, 시간이 지나면 다시 불안합니다. 그 사이에 퇴사 처리가 된 사람이 있는지, 만료 시각이 지났는데 남아 있는 예외가 있는지, 부서를 옮겼는데 역할은 그대로인 사람이 있는지가 궁금합니다. 저는 이것을 사용자 파일과 예외 파일을 열어 눈으로 맞춰 봅니다. 사용자가 여섯 명, 예외가 네 개뿐인데도 오래 걸립니다. 지난달에는 부서를 옮긴 사람의 역할 확인을 빠뜨려 감사팀에서 지적을 받았고, 회사가 커지면 이 방식은 쓸 수 없습니다.
>
> 퇴사자 계정 · 만료 예외 · 부서와 역할, 이 세 가지를 매주 같은 순서로 점검해서 걸린 사용자 이름이나 예외 번호를 알려 주세요. 점검은 찾기만 하고, 권한을 바로 지우지는 않습니다.」
> - **왜 중요한가**: 회수를 한 번 해도 사람은 계속 퇴사하고 부서를 옮깁니다. 눈으로 맞추면 오래 걸리고 한 명을 빠뜨릴 수 있는데, 코드가 같은 기준으로 한 번에 점검하면 걸린 대상의 이름이 바로 나옵니다. 이 결과는 응용 5-1에서 만드는 주간 보고서에 그대로 들어갑니다.

## M3 Unit 3부터 M3 Unit 4까지 흐름 복습

| Unit | 한 일 | 이번 Unit으로 이어지는 것 |
|---|---|---|
| M3 Unit 3 | 현황 리스트를 만들고, 규칙(퇴사 · 만료)과 사용 이력으로 안 쓰는 권한 후보를 찾고, 회수 제외를 가려냄 | 이번 점검 세 가지 중 퇴사자 · 만료 예외 점검의 출발 |
| M3 Unit 4 | 회수 대상을 계획 → 승인 → 실행 순서로 회수하고 이력을 남김 | 회수한 뒤에도 생기는 어긋남을 매주 다시 점검 |
| M3 Unit 4 | 업무 시간 · 접속 위치 조건을 판정에 더하고, 판정을 서버로 열어 요청마다 `server_log.jsonl` 에 한 줄씩 남김 | 응용 5-1 로그 집계의 입력. 이번에는 같은 모양의 일주일 치 샘플 40줄을 씁니다 |

## 왜 같은 기준으로 반복 점검하는가

1. 권한 점검은 한 번 하고 끝내는 일이 아니라 **주기마다 같은 기준으로 반복**하는 일입니다.
2. 반복하려면 점검할 것을 미리 정해 둡니다. 이것을 **점검 체크리스트**라고 부릅니다.
   - 점검 한 가지는 문제가 있는 사용자나 예외를 **리스트로 모읍니다.**
   - 리스트가 비어 있으면 **통과**, 하나라도 있으면 **실패**입니다.
3. 이번 실습에서는 점검 세 가지를 함수로 만듭니다. 점검할 데이터는 `config/week_state.json` 하나에 모아 두었습니다.

## 1.1 점검할 데이터와 세 가지 점검

`config/week_state.json` 은 세 부분으로 이루어집니다.

| 키 | 담긴 것 | 값의 예 |
|---|---|---|
| `users` | 사용자 이름 → 사용자 정보(부서 · 역할 · 재직 여부) | `"dami": {"dept": "영업", "role": "sales", "employed": false}` |
| `role_dept` | 역할 → 그 역할이 속해야 하는 부서 | `"finance": "재무"` |
| `exceptions` | 예외 리스트(번호 · 사용자 · 권한 · 만료 시각) | `{"id": 3, "user": "dami", "permission": "SALES:QUERY", "expires": "2026-11-03 18:00"}` |

점검 세 가지는 아래와 같습니다.

| 점검 | 문제로 보는 경우 | 모으는 것 |
|---|---|---|
| 퇴사자 계정 점검 | `employed` 가 `false`(퇴사)인데 `users` 에 계정이 남아 있다 | 사용자 이름 |
| 만료 예외 점검 | 만료 시각이 지금과 같거나 지났는데 예외가 남아 있다 | 예외 번호(`id`) |
| 부서와 역할 점검 | 사용자의 부서가 그 사용자 역할이 속해야 하는 부서와 다르다 | 사용자 이름 |

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `check_employed` | 사용자 딕셔너리 | 퇴사한(`employed` 가 `false`) 사용자 이름의 리스트 |
| `check_expired` | 예외 리스트, 지금 시각 | 만료 시각이 지금과 같거나 지난 예외 번호의 리스트 |
| `check_dept` | 사용자 딕셔너리, 역할별 부서 딕셔너리 | 부서가 역할의 부서와 다른 사용자 이름의 리스트 |
| `run_checklist` | 읽은 데이터, 지금 시각 | 점검 이름과 문제 리스트를 묶은 딕셔너리의 리스트(미리 채움) |

- 점검하는 시각은 `2026-11-02 10:00` 으로 고정합니다.
- `for name, info in users.items():` 는 딕셔너리의 키(사용자 이름)와 값(사용자 정보)을 한꺼번에 꺼냅니다.
- JSON 의 `true` · `false` 는 파이썬으로 읽으면 `True` · `False` 가 됩니다.
- 세 함수에서 판단 기준 한 줄씩을 씁니다. ①은 퇴사 여부, ②는 예외가 만료되는 시각, ③은 역할이 속할 부서를 확인합니다.
- `load_state`가 입력을 읽고 `run_checklist`가 세 점검 결과를 모읍니다.

<figure class="page-figure"><img src="assets/f01.svg" alt="run_checklist 는 점검 세 가지를 차례로 호출해 문제 리스트로 통과와 실패를 가린다"></figure>

## 실습 5-1 · 세 점검으로 통과·실패 가리기

**이런 상황이 있습니다**

- **지금은**: 점검은 사람이 `config/week_state.json` 같은 데이터 파일을 눈으로 읽어야 합니다. 사용자가 늘면 놓치기 쉽고, 지난주와 같은 기준으로 봤는지도 알 수 없습니다.
- **그래서 만드는 것**: `checklist.py` 입니다.
  - 점검 세 가지를 함수로 만들고, 문제가 있는 사용자 이름이나 예외 번호를 리스트로 모읍니다.
  - 예를 들어 dami 는 퇴사했는데 계정이 남아 있으므로 첫째 점검에서 걸립니다.
- **실행하면**: 단계 1은 점검 대상의 수, 단계 2는 점검 세 가지의 통과와 실패, 그리고 문제 리스트를 출력합니다.
- **현업에서는**: 접근 권한 점검도 점검할 것을 정해 두고 주기마다 반복하며, 결과(통과 · 실패와 대상)를 보고서에 남깁니다.

**할 일**

1. `checklist.py`와 `exercise5-1_run.py`를 만들고 `checklist.py`의 ①·②·③을 채웁니다.
2. 실행해서 <mark>점검 대상의 수</mark>(단계 1: 점검 대상)와 <mark>점검 세 가지의 결과</mark>(단계 2: 점검 결과)를 읽습니다.

**`checklist.py`**

```python
import json
from datetime import datetime

TIME_FORMAT = "%Y-%m-%d %H:%M"


def load_state(path):
    """점검할 데이터(사용자 · 역할의 부서 · 예외)를 읽어 딕셔너리로 리턴한다.
    정기 점검을 시작할 때 쓴다.
    """
    with open(path, encoding="utf-8") as json_file:
        return json.load(json_file)


def check_employed(users):
    """퇴사했는데 계정이 남아 있는 사용자 이름 리스트를 리턴한다.
    정기 점검에서 퇴사자 계정을 찾을 때 쓴다.
    """
    problems = []
    for name, info in users.items():
        # ① False를 퇴사 여부를 확인하는 조건으로 바꿉니다.
        if False:
            problems.append(name)
    return problems


def check_expired(exceptions, now):
    """만료 시각이 지났는데 남아 있는 예외의 번호 리스트를 리턴한다.
    정기 점검에서 기간이 끝난 예외를 찾을 때 쓴다.
    """
    problems = []
    for exception in exceptions:
        expires_at = datetime.strptime(exception["expires"], TIME_FORMAT)
        # ② False를 예외가 만료됐는지 확인하는 조건으로 바꿉니다.
        if False:
            problems.append(exception["id"])
    return problems


def check_dept(users, role_dept):
    """부서가 역할의 부서와 다른 사용자 이름 리스트를 리턴한다.
    정기 점검에서 엉뚱한 부서에 역할이 남은 사람을 찾을 때 쓴다.
    """
    problems = []
    for name, info in users.items():
        # ③ 오른쪽 값을 역할에 맞는 부서를 찾는 식으로 바꿉니다.
        expected_dept = info["dept"]
        if expected_dept != info["dept"]:
            problems.append(name)
    return problems


def run_checklist(state, now):
    """점검 세 가지를 실행한다.
    점검 이름과 문제 리스트를 담은 딕셔너리의 리스트를 리턴한다.
    매주 어긋난 곳을 한 번에 찾을 때 쓴다.
    """
    users = state["users"]
    exceptions = state["exceptions"]
    role_dept = state["role_dept"]
    results = []
    results.append({"name": "퇴사자 계정 점검", "problems": check_employed(users)})
    results.append({"name": "만료 예외 점검", "problems": check_expired(exceptions, now)})
    results.append({"name": "부서와 역할 점검", "problems": check_dept(users, role_dept)})
    return results
```

- ①은 `info["employed"]`와 `not`으로 퇴사 여부를 확인합니다.
- ②는 `expires_at`을 `now`와 비교합니다. 만료 시각과 같은 순간도 만료이므로 `<=`를 씁니다.
- ③은 `info["role"]`을 키로 `role_dept`에서 그 역할의 부서를 꺼냅니다.
- 세 곳을 다 채운 뒤 출력에서 **퇴사자 dami**, **부서와 역할이 맞지 않는 junho**, **만료 예외 점검 통과**를 확인합니다. 시작 코드의 자리 표시 값으로는 점검 결과를 판단할 수 없습니다.

**`exercise5-1_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 데이터 파일을 읽고 점검을 실행해 결과를 출력합니다.

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from checklist import TIME_FORMAT, load_state, run_checklist     # 방금 만든 점검 함수를 불러온다

NOW = datetime.strptime("2026-11-02 10:00", TIME_FORMAT)         # 점검하는 시각을 2026-11-02 10:00 으로 고정한다
state = load_state("config/week_state.json")                     # 점검할 데이터 파일을 읽는다
users = state["users"]                                           # 사용자 딕셔너리를 꺼낸다
exceptions = state["exceptions"]                                 # 예외 리스트를 꺼낸다

user_count = len(users)                                          # 사용자가 몇 명인지 센다
exception_count = len(exceptions)                                # 예외가 몇 개인지 센다
print("--- 단계 1: 점검 대상 - 사용자", user_count, "명 · 예외", exception_count, "개")  # 단계 1 시작을 알리는 줄
results = run_checklist(state, NOW)                              # 점검 세 가지를 실행한다
print("--- 단계 2: 점검 결과")                                      # 단계 2 시작을 알리는 줄
for result in results:                                           # 점검 결과를 하나씩 꺼낸다
    name = result["name"]                                        # 점검 이름을 꺼낸다
    problems = result["problems"]                                # 문제가 있는 사용자 · 예외 리스트를 꺼낸다
    if len(problems) == 0:                                       # 문제가 하나도 없으면
        status = "통과"                                           # 통과라고 적는다
    else:                                                        # 문제가 있으면
        status = "실패"                                           # 실패라고 적는다
    print(name, "|", status, "|", problems)                      # 점검 이름 | 결과 | 문제 리스트를 출력한다
```

**순서**

1. **[VS Code]** 파일 `checklist.py` · `exercise5-1_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `checklist.py` 에서 ①·②·③을 채웁니다. 1.1의 표와 그림을 참고합니다.
3. **[터미널]** `pwd` 의 결과가 `access_control` 로 끝나는지 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise5-1_run.py
   ```
4. 출력은 두 단계입니다. 단계 1은 한 줄, 단계 2는 점검 이름 세 줄입니다.
5. 출력과 실패한 항목을 확인합니다. 실습 5-2까지 마친 뒤 [실습 결과와 문제 해결 과정을 기록하기](__SITE__/exercises/module/3/unit/5/lesson/7/page/1)에서 이 결과를 판단 근거로 사용할 수 있습니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 통과한 점검과 실패한 점검, 실패한 점검에서 나온 사용자 이름이나 예외 번호를 적어 주세요.
   - (나) [핵심 질문] 만료 예외 점검은 「통과」인데, 예외 3번은 퇴사한 dami 의 예외입니다. 「통과」를 「문제 없음」으로만 읽으면 안 되는 이유와, 이 예외를 볼 때 함께 읽어야 하는 다른 점검을 적어 주세요.
   - (다) [핵심 질문] 점검은 junho 가 영업 부서인데 역할은 `finance` 라고 알려 줍니다. 점검 코드가 알려 주는 것과 알려 주지 못하는 것을 구분해 주세요. 그리고 이 결과를 받은 담당자가 무엇을 확인해야 하는지, 코드가 바로 권한을 회수하면 안 되는 이유가 무엇인지 적어 주세요.

<!-- answer: 06|실습 5-1 정답 -->

## 실습 5-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 점검할 데이터 읽기 | `state = load_state("config/week_state.json")` (미리 채움) |
| 사용자 이름과 정보 꺼내기 | `for name, info in users.items():` (미리 채움) |
| 퇴사자 찾기 | `if not info["employed"]:` → `problems.append(name)` |
| 만료 예외 찾기 | `datetime.strptime(exception["expires"], TIME_FORMAT)` → `if expires_at <= now:` → `problems.append(exception["id"])` |
| 부서가 다른 사용자 찾기 | `role_dept[info["role"]]` → `if expected_dept != info["dept"]:` → `problems.append(name)` |
| 통과 · 실패 | 문제 리스트가 비었으면 통과, 아니면 실패 |

---
