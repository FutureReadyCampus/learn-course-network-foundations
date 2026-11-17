---
id: m3-u04-l04
title: Exercise 4-3 · 정책 확인 후 예외 권한 부여
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/082_day03_am_request.md
  mission_id: GichanSource.m3-1023-am-request
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 4-3 · 정책 확인 후 예외 권한 부여

## 이번에 만들 것: 예외 권한 부여 함수

> **오늘 들어온 일**
>
> A사 보안 담당이 보낸 메시지: 「승인한 요청서를 제가 직접 예외 파일에 옮겨 적으면 실수가 납니다. 예외 번호를 겹치게 적거나, 만료 시각을 잘못 옮기거나, 하나를 빠뜨립니다. 승인된 요청서를 코드가 정책으로 한 번 더 확인하고, 통과한 것만 예외 권한을 부여하게 해 주세요. 어느 예외를 부여했는지도 요청서에 남겨 주세요.」
> - 이 Exercise에서 하는 일: 승인된 요청서를 Unit 1에서 만든 `check_permission` 으로 한 번 더 확인하고, 통과하면 예외를 만들어 `EXCEPTIONS` 에 추가하는 함수 `grant_request` 를 직접 씁니다. 부여 전과 후에 Unit 2의 `evaluate_access` 로 판정해 비교합니다.
> - 끝나면 쓰는 것: 보고서 (가)~(다) 답

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「문제」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 읽기 · 왜 승인 뒤에 정책으로 다시 확인하는가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 승인은 사람이 합니다. 그 뒤에 코드가 정책으로 한 번 더 확인하는 것을 **이중 검증**이라고 합니다.
2. 부여는 새 규칙을 만들지 않고, Unit 2에서 만든 **예외**(기간이 정해진 임시 권한)를 한 건 추가하는 일입니다.

## 읽기 · 3.1 부여할지 판단하는 순서

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

- 요청자를 지금 정책으로 판정한 이유(`judge_reason`)에 따라 처리가 갈립니다.
- 이 이유는 Unit 1에서 만든 `check_permission` 이 리턴하는 문자열입니다. `check_permission` 은 사용자 파일과 역할 파일만 보고 판정합니다(예외는 보지 않습니다).
- 단계 1은 Unit 2의 `evaluate_access` 로 판정해 `역할 권한` 이라고 출력하고, 단계 2는 `check_permission` 의 이유를 써서 `부여하지 않음(허용)` 이라고 출력합니다. 두 출력이 다르게 보이는 것이 정상입니다.

| 판정 결과 | 뜻 | 부여 |
|---|---|---|
| 허용 (`is_allowed` 가 `True`, 이유 「허용」) | 이미 그 권한이 있음 | 하지 않음 |
| 「권한 없음」 | 사람은 정상인데 권한만 없음 | **예외 권한 부여** |
| 「퇴사한 계정」 · 「등록되지 않은 사용자」 · 「역할이 없음」 | 사람 쪽에 문제가 있음 | 하지 않음 |

```
+------------------------+
| grant_request(request) |
+------------------------+
   |
   v
+----------------------------+
| status 가 "approved" 인가? |
+----------------------------+
   |
   +--> 아님 --> (False, "승인되지 않음")
   |
   v  맞음
+---------------------------------------------------+
| check_permission 으로 요청자를 지금 정책으로 판정 |
+---------------------------------------------------+
   |
   +--> 허용 --> (False, "부여하지 않음(허용)")   이미 가진 권한
   |
   +--> 그 밖의 이유(퇴사한 계정 · 등록되지 않은 사용자 · 역할이 없음) --> (False, "부여하지 않음(이유)")
   |
   v  권한 없음
+-----------------------------------------------------+
| 요청서로 예외 한 건을 만들어 EXCEPTIONS 에 추가한다 |
+-----------------------------------------------------+
   |
   v
+-----------------------------------------------------------------------+
| 요청서에 예외 번호(exception_id)를 적고 status 를 "granted" 로 바꾼다 |
+-----------------------------------------------------------------------+
   |
   v
(True, "부여")
```

## 읽기 · 3.2 요청서가 예외가 되는 방법

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

| 요청서의 키 | 예외의 키 |
|---|---|
| (없음. 새 번호) | `id` = `len(EXCEPTIONS) + 1` |
| `user` | `user` |
| `permission` | `permission` |
| `until` | `expires` |
| `reason` | `reason` |

- 예외를 만든 뒤에는 거꾸로, 예외의 `id` 를 요청서의 `exception_id` 키에 적어 둡니다. 그러면 요청서만 보고도 어느 예외를 부여했는지 찾을 수 있습니다.
- `EXCEPTIONS` 는 Unit 2의 `exception_policy.py` 가 `exceptions.json` 을 읽어 만든 리스트입니다. 오늘은 이 리스트에 한 건을 추가하기만 하고, `exceptions.json` 파일은 고치지 않습니다. 프로그램이 끝나면 추가한 예외도 사라집니다.
- Unit 2의 `find_exception` 이 같은 `EXCEPTIONS` 를 읽으므로, 추가한 예외는 바로 판정에 쓰입니다.
- Unit 2의 예외가 다섯 건이므로 새 예외의 번호는 5 + 1 = 6번입니다. 시작하기에서 본 숫자가 5가 아니면 6번이 아닌 다른 번호가 나옵니다.

**문법 상자 — 부여할지 가르는 조건과 번호 정하기**

**① `or` 로 두 조건 중 하나라도 맞는지 묻기**

```python
is_allowed = False                                                         # 허용이 아닌 판정
reason = "퇴사한 계정"                                                # 판정 이유
print(is_allowed or reason != "권한 없음")                                   # 둘 중 하나라도 참이면 참이다

reason = "권한 없음"                                                  # 이유를 바꾸면
print(is_allowed or reason != "권한 없음")                                   # 둘 다 거짓이라 거짓이다
```

실행 결과:

```
True
False
```

**② 리스트에 딕셔너리를 추가하고, 번호는 지금 개수 + 1 로 정하기**

```python
exceptions = [{"id": 1}, {"id": 2}]                                # 예외 두 건이 든 리스트

new_id = len(exceptions) + 1                                       # 번호는 지금 개수 + 1 로 정한다
new_exception = {"id": new_id}                                     # 새 예외 한 건을 만든다

exceptions.append(new_exception)                                   # 리스트 끝에 추가한다
print(exceptions)                                                  # 세 건이 되었다
```

실행 결과:

```
[{'id': 1}, {'id': 2}, {'id': 3}]
```


> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise 4-3 · 정책 확인 후 예외 권한 부여

**이런 상황이 있습니다**

- **지금은**: 승인한 요청서의 내용을 보안 담당이 예외 파일에 직접 옮겨 적습니다. 옮겨 적다 예외 번호를 겹치게 적거나, 만료 시각을 잘못 옮기거나, 하나를 빠뜨리기 쉽고 시간도 걸립니다.
- **그래서 만드는 것**: `grant_request` 입니다. 승인된 요청서를 받아서 Unit 1에서 만든 `check_permission` 으로 지금 정책을 한 번 더 확인하고, 통과한 것만 Unit 2의 **예외**로 `EXCEPTIONS` 에 추가합니다.
- **오늘 데이터**: 요청서 네 장입니다. 1번 seoyeon · 3번 dami · 4번 junho 는 승인됐고, 2번 gaeun 은 반려됐습니다.
- **실행하면**: 세 단계가 차례로 나옵니다. 단계 1은 부여하기 전의 판정, 단계 2는 부여를 시도한 결과, 단계 3은 부여한 뒤의 판정입니다. 부여 전과 후를 비교해 무엇이 달라졌는지 봅니다.
- **현업에서는**: 권한 부여 도구도 승인된 신청을 바로 부여하지 않고, 지금 정책으로 한 번 더 확인한 뒤에 부여합니다.

**할 일**

1. `req_grant.py` 와 `exercise4-3_run.py` 두 파일을 만들고, `grant_request` 본문을 직접 씁니다.
2. 실행해서 <mark>부여 전 판정</mark>(단계 1: 판정), <mark>부여 시도의 결과</mark>(단계 2: 부여), <mark>부여 후 판정</mark>(단계 3: 점검)을 읽습니다.

**`req_grant.py`**

```python
from rbac import check_permission                                # Unit 1에서 만든 역할 판정 함수를 불러온다
from exception_policy import EXCEPTIONS                          # Unit 2에서 만든 예외 리스트를 불러온다


def grant_request(request):                                      # 요청서를 받는 함수
    """승인된 요청서를 정책으로 한 번 더 확인하고 통과하면 예외 권한을 부여한다.
    승인 뒤 실제로 권한을 줄 때 쓰며 (성공 여부, 이유)를 리턴한다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. request["status"] 가 "approved" 가 아니면 False, "승인되지 않음" 을 리턴한다
    # 2. request 의 "user" · "resource" · "action" 을 각각 user · resource · action 에 담는다 (세 줄)
    # 3. check_permission(user, resource, action) 을 is_allowed, judge_reason 으로 나눠 받는다
    # 4. is_allowed 이거나 judge_reason 이 "권한 없음" 이 아니면 False, f"부여하지 않음({judge_reason})" 을 리턴한다
    # 5. len(EXCEPTIONS) + 1 을 exception_id 에 담는다 (다음 예외 번호)
    # 6. 예외 딕셔너리 exception 을 만든다. 키 다섯 개의 값은 이렇게 정한다:
    #    "id" 는 exception_id, "user" · "permission" · "reason" 은 request 의 같은 이름 키,
    #    "expires" 는 request["until"] (이름이 다른 것에 주의)
    # 7. EXCEPTIONS 에 exception 을 추가한다
    # 8. request["exception_id"] 를 exception["id"] 로 정한다 (어느 예외를 부여했는지 요청서에 적어 둔다)
    # 9. request["status"] 를 "granted" 로 바꾼다
    # 10. True, "부여" 를 리턴한다
```

- 본문은 모두 함수 안이라 4칸으로 쓰고, `if` 아래 `return` 은 4칸 더(8칸) 들어갑니다. 6번의 딕셔너리는 괄호 안이라 줄을 바꿔도 됩니다.
- 6번에서 딕셔너리를 변수 `exception` 에 담아 두면, 7번(`EXCEPTIONS.append(exception)`)과 8번(`exception["id"]`)에서 같은 값을 다시 쓸 수 있습니다.
- 4번의 `judge_reason` 은 `check_permission` 이 리턴하는 판정 이유 문자열입니다(요청서의 `reason`, 즉 요청 이유와는 다릅니다). 「허용」이면 이미 가진 권한이라서 부여하지 않습니다.
- 채우기 전에 실행하면 `TypeError: cannot unpack non-iterable NoneType object` 오류가 납니다. 함수가 아무것도 리턴하지 않기 때문입니다.

**`exercise4-3_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 요청서 네 장을 접수하고 1 · 3 · 4번은 승인, 2번은 반려한 뒤, 단계 1 · 2 · 3을 차례로 실행합니다. 중간의 `show` 함수는 요청서마다 Unit 2의 `evaluate_access` 로 판정해 출력하고, 단계 2 끝에서는 `exception_id` 키가 있는 요청서(`"exception_id" in request`)의 예외 번호를 출력합니다.

```python
from datetime import datetime                                    # 지금 시각을 만드는 데 쓴다
from req_create import REQUESTS, create_request                  # Exercise 4-1에서 만든 요청서 함수와 리스트를 불러온다
from req_review import approve_request, reject_request           # Exercise 4-2에서 만든 승인 · 반려 함수를 불러온다
from req_grant import grant_request                              # 방금 만든 부여 함수를 불러온다
from policy import evaluate_access                               # Unit 2에서 만든 최종 판정 함수를 불러온다

NOW = datetime.strptime("2026-10-23 10:00", "%Y-%m-%d %H:%M")    # 오늘 실습의 지금 시각(고정)

INBOX = [                                                        # 접수에 성공하는 요청 네 건. (요청자, 자원, 행위, 희망 만료 시각, 이유, 접수 시각)
    ("seoyeon", "SETTLE", "QUERY", "2026-10-27 18:00", "정산 대조 지원", "2026-10-23 08:30"),
    ("gaeun", "SALES", "QUERY", "2026-10-28 18:00", "감사 자료 대응", "2026-10-23 08:40"),
    ("dami", "SALES", "QUERY", "2026-10-27 18:00", "인수인계 자료 확인", "2026-10-23 08:50"),
    ("junho", "SETTLE", "QUERY", "2026-10-27 18:00", "정산 확인", "2026-10-23 09:00"),
]
for user, resource, action, until, reason, received_at in INBOX:         # 요청을 하나씩 꺼내
    create_request(user, resource, action, until, reason, received_at)   # 접수한다
for number in [1, 3, 4]:                                         # 보안 담당이 1 · 3 · 4번을 승인하고
    approve_request(REQUESTS[number - 1], "security_manager")    # 승인 처리한다
reject_request(REQUESTS[1], "security_manager")                  # 2번은 반려한다


def show(title):                                                 # 제목을 받아 요청서마다 지금 판정을 출력하는 함수
    """요청서마다 지금의 최종 판정을 출력한다.
    승인과 부여 전후에 판정이 어떻게 달라지는지 볼 때 쓴다.
    """
    print("---", title)                                          # 제목 줄을 출력한다
    for request in REQUESTS:                                     # 요청서를 하나씩 꺼낸다
        user = request["user"]                                   # 요청자
        resource = request["resource"]                           # 자원
        action = request["action"]                               # 행위
        is_allowed, reason = evaluate_access(user, resource, action, NOW)   # 22일의 최종 판정을 받는다
        print(request["id"], request["user"], request["permission"], "->", is_allowed, reason)   # 요청 번호 · 요청자 · 권한 -> 판정 을 출력한다


show("단계 1: 판정 - 부여 전")                                     # 부여하기 전의 판정을 본다

print("--- 단계 2: 부여 - 요청서마다 부여를 시도한다")                # 단계 2 시작을 알리는 줄
for request in REQUESTS:                                         # 요청서를 하나씩 꺼낸다
    is_allowed, result = grant_request(request)                          # 부여를 시도한다
    print(request["id"], request["user"], request["status"], "->", is_allowed, result)   # 요청 번호 · 요청자 · 상태 -> 결과 를 출력한다

for request in REQUESTS:                                         # 요청서를 하나씩 꺼낸다
    if "exception_id" in request:                                # exception_id 키가 있는 요청서(부여된 것)만
        print("부여된 예외 번호:", request["exception_id"])         # 그 예외 번호를 출력한다

show("단계 3: 점검 - 부여 후")                                     # 부여한 뒤의 판정을 다시 본다
```

**순서**

1. **[VS Code 또는 터미널]** 파일을 만들고 각각 붙여 넣습니다. 파일마다 아래 세 가지 방법 중 **하나만** 고릅니다.
   - **방법 1 · VS Code 에서 만들기**: 파일마다 아래 네 가지를 반복합니다.
     1. VS Code 왼쪽 목록에서 `access_control` 폴더를 클릭해 선택합니다(선택하지 않으면 다른 폴더에 만들어집니다).
     2. 목록 위쪽의 **새 파일**(New File, 파일 모양에 `+`) 아이콘을 누릅니다.
     3. 이름 칸에 파일 이름을 입력하고 Enter 를 누릅니다. 이름은 차례로 `req_grant.py` · `exercise4-3_run.py` 입니다.
     4. 열린 파일에 위 코드 상자의 내용을 복사해 붙여 넣고 저장합니다.
   - **방법 2 · touch 로 만들기**: 터미널에서 파일마다 한 줄씩 치고, 각각 VS Code 에서 열어 붙여넣기: `touch req_grant.py` → `touch exercise4-3_run.py`
   - **방법 3 · vim 으로 만들기**: 파일마다 한 번씩 합니다: `vim req_grant.py` → `vim exercise4-3_run.py` (각각 `i` → 붙여넣기 → `Esc` → `:wq` Enter. 줄 앞 공백이 줄마다 밀려 있으면 `Esc` → `:q!` 로 나와서 방법 1 이나 방법 2 로 다시 만듭니다)
2. **[VS Code]** `req_grant.py` 의 `grant_request` 본문을 직접 씁니다. 3.1 의 표와 그림을 보고 씁니다.
3. **[터미널]** `pwd` 를 쳐서 마지막 폴더가 `access_control` 인지 확인한 뒤 실행합니다.
   ```bash
   python exercise4-3_run.py
   ```
   - 명령 풀이: `python` 파이썬으로 파일을 실행 · `exercise4-3_run.py` 실행할 파일
   - 맥북은 `python3 exercise4-3_run.py` 로 칩니다.
4. 출력은 세 단계입니다. 단계 1은 부여 전 판정(네 줄), 단계 2는 부여 시도의 결과(네 줄)와 `부여된 예외 번호:` 한 줄, 단계 3은 부여 후 판정(네 줄)입니다. 부여 전과 후에 달라진 줄이 하나 있습니다.
5. **[보고서]** Unit 4 의 `## Exercise 4-3` › `### Exercise 4-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 부여를 시도한 네 건이 각각 어떻게 됐는지 적어 주세요.
   - (나) [핵심 질문] 승인자가 승인한 3번 요청(`dami`)을 코드가 부여하지 않았습니다. 코드의 이 확인이 없었다면 어떤 일이 생겼을까요? 승인자가 이 문제를 미리 막기 어려운 이유도 적어 주세요.
   - (다) [핵심 질문] 부여한 예외의 만료 시각에는 요청서의 희망 만료 시각을 그대로 썼습니다. 그 시각이 지나면 이 예외는 어떻게 될까요? 만료된 예외를 정리하는 점검은 누가 얼마나 자주 하면 좋을까요?

## Exercise 4-3 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 승인된 것만 부여 | `if request["status"] != "approved": return False, "승인되지 않음"` |
| 정책으로 한 번 더 판정 | `is_allowed, judge_reason = check_permission(user, resource, action)` |
| 부여하지 않는 경우 | `if is_allowed or judge_reason != "권한 없음": return False, f"부여하지 않음({judge_reason})"` |
| 예외 권한 부여 | `exception_id = len(EXCEPTIONS) + 1` → `exception = {"id": exception_id, …}` → `EXCEPTIONS.append(exception)` |
| 어느 예외인지 적기 | `request["exception_id"] = exception["id"]` |
| 부여 끝 표시 | `request["status"] = "granted"` |

---

## Unit 4 마무리 — 보고서 Exercise 4-1 · 4-2 · 4-3 칸 확인

Unit 4 의 Exercise 4-1 · 4-2 · 4-3 칸에서 `답:` 뒤가 비어 있는 질문이 없는지 봅니다. `access_control` 폴더에 오늘 만든 파일이 있는지 확인합니다.

```bash
ls
ls config
```

- `req_create.py` · `req_review.py` · `req_grant.py` · `exercise4-1_run.py` · `exercise4-2_run.py` · `exercise4-3_run.py` 가 보여야 합니다. `config` 안은 Unit 3을 마쳤을 때와 같아야 합니다(오늘은 `config` 에 새 파일을 만들지 않았습니다).

다음 Unit(Unit 5)에서는 접수한 지 오래된 요청서를 시간으로 찾아내고(SLA · 처리 기한), 요청서 이력을 파일로 저장합니다. 올리기(git)는 Unit 5의 Exercise 5-2 마지막에 한 번에 합니다.

---

<!-- learn:answers -->
