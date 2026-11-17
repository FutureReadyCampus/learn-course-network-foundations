---
id: m3-u10-l02
title: Exercise 10-1 · 점검 체크리스트로 어긋난 곳 찾기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/094_day06_am_weekly_report.md
  mission_id: GichanSource.m3-1102-am-weekly-report
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 10-1 · 점검 체크리스트로 어긋난 곳 찾기

## 개요

> **오늘 들어온 일**
>
> A사 보안 팀장이 보낸 메시지:
> 「금요일에 회수를 마쳤는데, 월요일 아침이 되면 다시 불안합니다. 주말 사이에 퇴사 처리가 된 사람이 있는지, 만료 시각이 지났는데 남아 있는 예외가 있는지, 부서를 옮겼는데 역할은 그대로인 사람이 있는지를 저는 사용자 파일과 예외 파일을 열어 눈으로 맞춰 봅니다. 사용자가 여섯 명, 예외가 네 개뿐인데도 오래 걸립니다. 지난달에는 부서를 옮긴 사람의 역할 확인을 빠뜨려 감사팀에서 지적을 받았고, 회사가 커지면 이 방식은 쓸 수 없습니다.
>
> 퇴사자 계정 · 만료 예외 · 부서와 역할, 이 세 가지를 매주 같은 순서로 점검해서 걸린 사용자 이름이나 예외 번호를 알려 주세요. 점검은 찾기만 하고, 권한을 바로 지우지는 않습니다.」
> - **왜 중요한가**: 회수를 한 번 해도 사람은 계속 퇴사하고 부서를 옮깁니다. 눈으로 맞추면 오래 걸리고 한 명을 빠뜨릴 수 있는데, 코드가 같은 기준으로 한 번에 점검하면 걸린 대상의 이름이 바로 나옵니다. 이 결과는 Exercise 10-2에서 만드는 주간 보고서에 그대로 들어갑니다.

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「 문제」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 읽기 · 앞 수업 흐름 복습

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

| 날짜 | 한 일 | 오늘 이어지는 것 |
|---|---|---|
| 10/29(목) | 현황 리스트를 만들고, 규칙(퇴사 · 만료)과 사용 이력으로 안 쓰는 권한 후보를 찾고, 회수 제외를 가려냄 | 오늘 점검 세 가지 중 퇴사자 · 만료 예외 점검의 출발 |
| 10/30(금) 오전 | 회수 대상을 계획 → 승인 → 실행 순서로 회수하고 이력을 남김 | 회수한 뒤에도 생기는 어긋남을 매주 다시 점검 |
| 10/30(금) 오후 | 업무 시간 · 접속 위치 조건을 판정에 더하고, 판정을 서버로 열어 요청마다 `server_log.jsonl` 에 한 줄씩 남김 | Exercise 10-2 로그 집계의 입력. 오늘은 같은 모양의 일주일 치 샘플 40줄을 씁니다 |

## 읽기 · 왜 필요한가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 권한 점검은 한 번 하고 끝내는 일이 아니라 **주기마다 같은 기준으로 반복**하는 일입니다.
2. 반복하려면 점검할 것을 미리 정해 둡니다. 이것을 **점검 체크리스트**라고 부릅니다.
   - 점검 한 가지는 문제가 있는 사용자나 예외를 **리스트로 모읍니다.**
   - 리스트가 비어 있으면 **통과**, 하나라도 있으면 **실패**입니다.
3. 오늘은 점검 세 가지를 함수로 만듭니다. 점검할 데이터는 `config/week_state.json` 하나에 모아 두었습니다.

## 읽기 · 1.1 점검할 데이터와 세 가지 점검

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

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
- **직접 쓰는 곳은 세 함수**(번호 1 ~ 8)입니다. 함수마다 2 ~ 3줄만 쓰고, 나머지는 미리 채웠습니다.
  - `check_employed`(1 · 2번): 퇴사한 사용자의 이름을 모읍니다.
  - `check_expired`(3 ~ 5번): 만료된 예외의 번호를 모읍니다.
  - `check_dept`(6 ~ 8번): 부서가 다른 사용자의 이름을 모읍니다.
- **미리 채운 것**: `load_state`(파일 읽기)와 `run_checklist`(세 점검을 묶기)입니다.

```
+------------------------------------------------+
| load_state 가 config/week_state.json 을 읽는다 |
+------------------------------------------------+
   |
   v
+-----------------------------------------------------+
| run_checklist 가 점검 세 가지를 차례로 호출한다     |
+-----------------------------------------------------+
   |
   +--> check_employed(users)          --> 퇴사한 사용자 이름 리스트
   |
   +--> check_expired(exceptions, now) --> 만료된 예외 번호 리스트
   |
   +--> check_dept(users, role_dept)   --> 부서가 다른 사용자 이름 리스트
   |
   v
+------------------------------------------------------------+
| 점검마다 {"name": 점검 이름, "problems": 리스트} 로 묶는다 |
+------------------------------------------------------------+
   |
   v
+----------------------------------------------+
| 리스트가 비었으면 통과, 하나라도 있으면 실패 |
+----------------------------------------------+
```

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise 10-1 · 퇴사자 · 만료 예외 · 부서와 역할을 점검해 통과와 실패 가리기

** 이런 상황이 있습니다**

- **지금은**: 점검은 사람이 `config/week_state.json` 같은 데이터 파일을 눈으로 읽어야 합니다. 사용자가 늘면 놓치기 쉽고, 지난주와 같은 기준으로 봤는지도 알 수 없습니다.
- **그래서 만드는 것**: `checklist.py` 입니다.
  - 점검 세 가지를 함수로 만들고, 문제가 있는 사용자 이름이나 예외 번호를 리스트로 모읍니다.
  - 예를 들어 dami 는 퇴사했는데 계정이 남아 있으므로 첫째 점검에서 걸립니다.
- **실행하면**: 단계 1은 점검 대상의 수, 단계 2는 점검 세 가지의 통과와 실패, 그리고 문제 리스트를 출력합니다.
- **현업에서는**: 접근 권한 점검도 점검할 것을 정해 두고 주기마다 반복하며, 결과(통과 · 실패와 대상)를 보고서에 남깁니다.

** 할 일**

1. `checklist.py` · `exercise10-1_run.py` 두 파일을 만들고, `checklist.py` 의 `check_employed` · `check_expired` · `check_dept` 에서 직접 쓰는 곳 세 군데를 씁니다.
2. 실행해서 <mark>점검 대상의 수</mark>(단계 1: 점검 대상)와 <mark>점검 세 가지의 결과</mark>(단계 2: 점검 결과)를 읽습니다.

**`checklist.py`**

```python
import json                                                      # JSON 파일을 읽는 모듈을 불러온다
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다

TIME_FORMAT = "%Y-%m-%d %H:%M"                                   # 만료 시각 문자열의 형식 (예: 2026-11-03 18:00)


def load_state(path):                                            # 파일 경로를 받는 함수
    """점검할 데이터(사용자 · 역할의 부서 · 예외)를 읽어 딕셔너리로 리턴한다.
    정기 점검을 시작할 때 쓴다.
    """
    with open(path, encoding="utf-8") as json_file:                      # 파일을 연다
        return json.load(json_file)                                      # 읽은 내용을 바로 리턴한다


def check_employed(users):                                       # 사용자 딕셔너리를 받는 함수
    """퇴사했는데 계정이 남아 있는 사용자 이름 리스트를 리턴한다.
    정기 점검에서 퇴사자 계정을 찾을 때 쓴다.
    """
    problems = []                                                # 문제가 있는 사용자 이름을 모을 리스트
    for name, info in users.items():                             # 사용자 이름과 사용자 정보을 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 1. info["employed"] 가 거짓이면 (if not …)
        # 2.   name 을 problems 에 추가한다
    return problems                                              # 문제가 있는 사용자 이름을 리턴한다


def check_expired(exceptions, now):                              # 예외 리스트와 지금 시각(datetime)을 받는 함수
    """만료 시각이 지났는데 남아 있는 예외의 번호 리스트를 리턴한다.
    정기 점검에서 기간이 끝난 예외를 찾을 때 쓴다.
    """
    problems = []                                                # 문제가 있는 예외 번호를 모을 리스트
    for exception in exceptions:                                       # 예외를 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. exception["expires"] 를 TIME_FORMAT 으로 읽어 시각 expires_at 에 담는다 (datetime.strptime)
        # 4. expires_at 이 now 보다 이르거나 같으면 (<=)
        # 5.   exception["id"] 를 problems 에 추가한다
    return problems                                              # 문제가 있는 예외 번호를 리턴한다


def check_dept(users, role_dept):                                # 사용자 딕셔너리와 역할별 부서 딕셔너리를 받는 함수
    """부서가 역할의 부서와 다른 사용자 이름 리스트를 리턴한다.
    정기 점검에서 엉뚱한 부서에 역할이 남은 사람을 찾을 때 쓴다.
    """
    problems = []                                                # 문제가 있는 사용자 이름을 모을 리스트
    for name, info in users.items():                             # 사용자 이름과 사용자 정보을 하나씩 꺼낸다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 6. role_dept 에서 info["role"] 의 부서를 찾아 expected_dept 에 담는다
        # 7. expected_dept 가 info["dept"] 와 다르면 (!=)
        # 8.   name 을 problems 에 추가한다
    return problems                                              # 문제가 있는 사용자 이름을 리턴한다


def run_checklist(state, now):                                   # 읽은 데이터와 지금 시각을 받는 함수
    """점검 세 가지를 실행한다.
    점검 이름과 문제 리스트를 담은 딕셔너리의 리스트를 리턴한다.
    매주 어긋난 곳을 한 번에 찾을 때 쓴다.
    """
    users = state["users"]                                       # 사용자 딕셔너리를 꺼낸다
    exceptions = state["exceptions"]                             # 예외 리스트를 꺼낸다
    role_dept = state["role_dept"]                               # 역할별 부서 딕셔너리를 꺼낸다
    results = []                                                 # 점검 결과를 모을 리스트
    results.append({"name": "퇴사자 계정 점검", "problems": check_employed(users)})            # 첫째 점검 결과를 추가한다
    results.append({"name": "만료 예외 점검", "problems": check_expired(exceptions, now)})     # 둘째 점검 결과를 추가한다
    results.append({"name": "부서와 역할 점검", "problems": check_dept(users, role_dept)})     # 셋째 점검 결과를 추가한다
    return results                                               # 점검 결과 리스트를 리턴한다
```

- 들여쓰기는 미리 채운 줄에 맞춥니다.
  - 세 함수 모두 `for` 안쪽이라 `if` · 변수 줄은 앞에 공백 8개이고, `if` 안쪽 `problems.append(…)` 는 4개 더(12개)입니다.
  - 나머지 줄은 미리 채워 두었으니 그대로 둡니다.
- 3번은 `datetime.strptime(문자열, TIME_FORMAT)` 으로 문자열을 시각으로 바꿉니다. 10/22(목)에 예외의 만료 시각을 읽을 때와 같은 방법입니다.
- 4번의 `<=` 는 「같거나 이전」입니다. 만료 시각 정각도 만료로 봅니다.
- 6번의 `role_dept[info["role"]]` 는 키가 `info["role"]` 인 값을 찾습니다. 사용자의 역할이 `finance` 이면 `"재무"` 가 나옵니다.
- 채우기 전에 실행하면 `IndentationError: expected an indented block` 오류가 납니다(파이썬 버전에 따라 뒤에 `after 'for' statement on line …` 가 붙습니다). `for` 아래에 실행할 줄이 아직 없기 때문입니다.

**`exercise10-1_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 데이터 파일을 읽고 점검을 실행해 결과를 출력합니다.

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

1. **[VS Code 또는 터미널]** 파일 `checklist.py` · `exercise10-1_run.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `checklist.py` 에서 직접 쓰는 곳 세 군데를 씁니다. 1.1 의 표와 그림을 보고 씁니다.
3. **[터미널]** `pwd` 의 결과가 `access_control` 로 끝나는지 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python exercise10-1_run.py
   ```
4. 출력은 두 단계입니다. 단계 1은 한 줄, 단계 2는 점검 이름 세 줄입니다.
5. **[보고서]** Unit 10 의 `## Exercise 10-1` › `### Exercise 10-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 통과한 점검과 실패한 점검, 실패한 점검에서 나온 사용자 이름이나 예외 번호를 적어 주세요.
   - (나) [핵심 질문] 만료 예외 점검은 「통과」인데, 예외 3번은 퇴사한 dami 의 예외입니다. 「통과」를 「문제 없음」으로만 읽으면 안 되는 이유와, 이 예외를 볼 때 함께 읽어야 하는 다른 점검을 적어 주세요.
   - (다) [핵심 질문] 점검은 junho 가 영업 부서인데 역할은 `finance` 라고 알려 줍니다. 점검 코드가 알려 주는 것과 알려 주지 못하는 것을 구분하고, 이 결과를 받은 담당자가 무엇을 확인해야 하는지, 코드가 바로 권한을 회수하면 안 되는 이유가 무엇인지 적어 주세요.

## Exercise 10-1 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 점검할 데이터 읽기 | `state = load_state("config/week_state.json")` (미리 채움) |
| 사용자 이름과 정보 꺼내기 | `for name, info in users.items():` (미리 채움) |
| 퇴사자 찾기 | `if not info["employed"]:` → `problems.append(name)` |
| 만료 예외 찾기 | `datetime.strptime(exception["expires"], TIME_FORMAT)` → `if expires_at <= now:` → `problems.append(exception["id"])` |
| 부서가 다른 사용자 찾기 | `role_dept[info["role"]]` → `if expected_dept != info["dept"]:` → `problems.append(name)` |
| 통과 · 실패 | 문제 리스트가 비었으면 통과, 아니면 실패 |

---
