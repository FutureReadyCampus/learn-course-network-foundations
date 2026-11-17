---
id: m3-u02-l05
title: Exercise 2-3 · 역할 권한과 예외를 합친 정책 policy.py
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/078_day02_am_policy.md
  mission_id: GichanSource.m3-1022-am-policy
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 2-3 · 역할 권한과 예외를 합친 정책 policy.py

## 개요

> **오늘 들어온 일**
> A사 보안 담당이 보낸 메시지: 「지금은 "역할로 허용되나?"와 "예외로 허용되나?"를 따로 확인해서, 정산 포털이 어느 결과를 믿어야 할지 모르겠습니다. 요청 하나를 넣으면 "허용인지 거부인지"와 "왜 그런지"가 한 번에 나오게 해 주세요. 이미 퇴사한 사람은 예외가 남아 있어도 열리면 안 됩니다.」
> - 이 Exercise에서 하는 일: Unit 1의 `check_permission` 과 Exercise 2-2의 `find_exception` 을 불러 최종 판정 함수 `evaluate_access` 를 `policy.py` 에 직접 쓰고, 오늘 요청 아홉 건을 판정한 결과를 읽습니다.
> - 끝나면 쓰는 것: 보고서 (가)~(다) 답

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「Exercise」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 읽기 · 왜 필요한가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 판정 기준이 두 곳에 흩어져 있으면 집행하는 쪽(PEP · 피이피, 집행 지점)이 어느 것을 따를지 매번 정해야 합니다. 최종 판정을 한 함수가 하면 규칙이 한 곳에 모입니다(2과목의 판단과 집행 분리).
2. 예외는 **역할 권한이 없을 때만** 봐야 합니다. 그리고 사용자 자체가 거부 대상인 경우(없는 사용자 · 퇴사자 · 역할이 없음)는 예외가 있어도 열면 안 됩니다. 이 순서가 틀리면 Exercise 2-2 의 `dami` 처럼 퇴사자가 예외로 허용됩니다.
3. `policy.py` 는 Unit 4의 요청 · 승인 · 부여 흐름(`req_create.py` · `req_review.py` · `req_grant.py`)이 불러 쓰는 함수입니다.

## 읽기 · 3.1 판정 순서

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

```
+------------------------------------------------+
| evaluate_access(사용자, 자원, 행위, 지금 시각) |
+------------------------------------------------+
   |
   v
+----------------------------------------+
| [역할 판정] check_permission 으로 판정 |
+----------------------------------------+
   |
   +--> 허용 --> 허용: 역할 권한
   |
   +--> 거부(그 밖의 이유: 없는 사용자 · 퇴사 · 역할이 없음) --> 거부: 그 이유 그대로   (골격의 3번)
   |
   v  거부(권한 없음)일 때만 아래로
+-------------------------------------------------------+
| [예외 판정] find_exception 으로 지금 유효한 예외 찾기 |
+-------------------------------------------------------+
   |
   +--> 있음 --> 허용: 예외 N번
   |
   +--> 없음 --> 거부: 권한 없음
```

- `check_permission` 은 Unit 1에서 만든 그대로 불러 씁니다. 고치지 않습니다. 이 함수는 `(True 또는 False, 이유)` 를 리턴하고, 이유는 「권한 없음」 · 「퇴사한 계정」 · 「등록되지 않은 사용자」 · 「역할이 없음」 중 하나입니다.
- Unit 2의 `policy.py` 는 Unit 1의 역할 파일(`roles.json`)과 사용자 파일(`users.json`)을 그대로 씁니다. Exercise 2-1의 `assign_role` 과 `revoke_access` 는 메모리의 사용자 딕셔너리만 바꾸고 파일에는 저장하지 않으므로, `policy.py` 는 인사 변경 전의 사용자로 판정합니다.
- **서비스 계정**은 사람이 아니라 프로그램이 쓰는 계정입니다(`batch-night`). 사람이 로그인하지 않고, 키나 비밀번호를 설정 파일에 두고 접속하는 경우가 많습니다.
- `[역할 판정]` 에서 「권한 없음」일 때만 예외를 봅니다. 사용자 자체가 거부 대상인 경우는 예외 검사까지 가지 않습니다.

**이 시간에 나오는 말** (이미 배운 방법입니다)

- `from rbac import check_permission` · `from exception_policy import find_exception` 처럼 두 파일의 함수를 함께 불러옵니다(Unit 1).
- `값 != "권한 없음"` 은 이유 문자열이 「권한 없음」이 아닌지 검사합니다.
- `f"예외 {found_exception_id}번"` 처럼 f-문자열로 이유를 만듭니다(앞선 실습).

## 읽기 · 3.2 허용 방식별로 세기

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

- 판정 결과는 세 갈래로 셉니다: **역할로 허용**(이유가 「역할 권한」) · **예외로 허용**(이유가 「예외 N번」) · **거부**.
- 허용을 둘로 나눠 세는 이유는 **예외로 열린 일이 얼마나 되는지** 숫자로 보기 위해서입니다. 예외가 많아지면 역할 설계가 실제 업무와 맞지 않는다는 신호입니다. 현업에서는 예외 허용 건수를 따로 세어 매주 보고합니다.
- 세는 모양은 Unit 1의 Exercise 1-3 과 같습니다: `old_count = counts.get(키, 0)` → `counts[키] = old_count + 1`.
- 요청마다 시각이 다르면 `"2026-10-22 " + 시각` 으로 날짜 문자열과 시각 문자열을 이어 붙인 뒤 `strptime` 으로 시각을 만듭니다(2.2).
- **만료 뒤 시도**: 거부 이유가 「권한 없음」인데 같은 사람 · 같은 권한의 예외가 예외 리스트에 있으면, 예외가 끝난 뒤에도 다시 시도한 것입니다. 퇴사자(`dami`)처럼 사람이 거부 대상인 경우는 예외가 남아 있어도 만료 뒤 시도로 보지 않습니다.
- 순서는 「역할 권한으로 허용」을 먼저 검사하고, 그다음 「그 밖의 허용」(예외)을 검사합니다. 거꾸로 하면 역할로 허용된 요청이 예외로 세어집니다.

## 읽기 · 3.3 파일 사이의 흐름을 그림으로 그리기

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

- 파일이 여러 개가 되면 「어느 파일이 어느 파일의 무엇을 호출하는가」를 머릿속에만 두기 어렵습니다. 글자로 그림을 그리면 한 곳이 고장 났을 때 어느 화살표에서 멈추는지 바로 보입니다.
- 그림 규칙은 다음과 같습니다.
  - 파일은 상자(`+---+` 와 `| 파일 이름 |`)로 그리고, 시작 파일을 맨 위에 둡니다.
  - 상자 아래로 `|` 와 `v` 로 이어 가고, `+-->` 옆에 **호출하는 함수 이름**을 씁니다.
  - 파일이 읽는 설정 파일은 `읽음` 아래에 적습니다.
  - 그림에는 파일 이름 · 호출하는 함수 · 읽는 설정 파일만 넣습니다. 그 밖의 가져오기(`datetime` 등)는 그리지 않습니다.
  - 오른쪽 선이 한글 때문에 조금 안 맞아도 괜찮습니다.
- **파일 맨 위에서 설정 파일을 읽는 줄(`with open(…)`)은 그 파일을 불러오는(`import`) 순간 실행됩니다.** 그래서 설정 파일이 깨져 있으면 함수를 부르기도 전에, 그 파일을 불러오는 화살표에서 멈춥니다.
- 아래는 Exercise 2-1의 파일들로 그린 본보기입니다. Exercise 2-3에서는 이 Exercise의 파일들로 직접 그립니다.

```
+------------------+
| exercise2-1_run.py |
+------------------+
   |
   +--> 1. check_permission() 호출
   |       |
   |       v
   |    +---------+
   |    | rbac.py |
   |    +---------+
   |       |  읽음 (rbac.py 를 불러올 때 한 번)
   |       v
   |    config/users.json · config/roles.json
   |
   +--> 2. assign_role() · revoke_access() 호출  (USERS 를 넘김)
           |
           v
        +---------------+
        | role_admin.py |
        +---------------+
           |  가져옴
           v
        rbac.py 의 ROLES
```

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise 2-3 · 최종 판정 함수 evaluate_access 만들고, 오늘 요청 아홉 건의 결과와 만료 뒤 시도 읽기

**이런 상황이 있습니다**

- 지금은 역할을 확인하는 함수(`check_permission`)와 예외를 확인하는 함수(`find_exception`)가 따로 있습니다. 정산 포털 개발팀은 요청 하나를 넣으면 「허용인지 거부인지」와 「이유」가 한 번에 나오는 함수 하나를 원합니다. 두 확인을 3.1 의 순서대로 합칩니다.
- 보안 담당은 하루가 끝나면 세 가지를 알고 싶어 합니다. 오늘 예외로 허용된 요청이 몇 건인지, 예외 번호마다 몇 번 쓰였는지, 이미 끝난 예외로 다시 시도한 요청이 있는지입니다. 오늘 요청 아홉 건을 그 시각대로 판정하면서 이 숫자를 셉니다.
- 현업에서는 이 집계를 하루가 끝날 때 자동으로 만들어 보안 담당에게 보냅니다. 또 접근통제 제품에는 이렇게 여러 규칙을 정해진 순서로 합쳐 결과 하나를 내는 부분(PDP · 피디피, 판단 지점)이 따로 있습니다.

**할 일**

1. `policy.py` 를 만들고 `evaluate_access` 본문을 직접 씁니다.
2. `exercise2-3_run.py` 를 실행해서 <mark>아홉 건의 결과</mark>, <mark>만료 뒤 시도</mark>, <mark>예외 번호별 사용 건수</mark>를 읽습니다.

**`policy.py`**

```python
from rbac import check_permission                                # Unit 1에서 만든 역할 판정 함수를 불러온다
from exception_policy import find_exception                      # Exercise 2-2에 만든 예외 판정 함수를 불러온다


def evaluate_access(user, resource, action, now):                # 사용자 · 자원 · 행위 · 지금 시각을 받는 함수
    """(허용 여부, 이유)를 리턴한다.
    역할 권한 → 유효한 예외 → 거부 순서로 보며, 임시 예외까지 포함해 요청을 판정할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. check_permission 으로 판정해 is_allowed, reason 으로 나눠 받는다
    # 2. is_allowed 이면 True, "역할 권한" 을 리턴한다
    # 3. reason 이 "권한 없음" 이 아니면 False 와 그 reason 을 그대로 리턴한다
    # 4. find_exception 에 user, "자원:행위" 문자열(f"{resource}:{action}"), now 를 넣어 found, found_exception_id 로 나눠 받는다
    # 5. found 이면 True, f"예외 {found_exception_id}번" 을 리턴한다
    # 6. 여기까지 왔으면 False, "권한 없음" 을 리턴한다
```

**`exercise2-3_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 이 파일은 오늘 요청 아홉 건을 그 시각대로 `evaluate_access` 로 판정합니다. 그리고 3.2 의 순서로 방식별 건수와 예외 번호별 사용 건수를 세고, 예외가 끝난 뒤의 시도를 알립니다.

```python
from datetime import datetime                                    # 요청 시각을 만드는 데 쓴다
from policy import evaluate_access                               # 방금 만든 최종 판정 함수를 불러온다
from exception_policy import EXCEPTIONS                          # 예외 리스트를 불러온다

TODAY_LOG = [                                                    # 오늘 정산 포털 요청 기록. (시각, 사용자, 자원, 행위)
    ("09:10", "seoyeon", "SETTLE", "QUERY"),                     # 예외 1번 기간 안
    ("10:00", "dami", "SALES", "QUERY"),                         # 퇴사자(예외 3번이 남아 있음)
    ("11:40", "gaeun", "SETTLE", "QUERY"),                       # 예외 5번 기간 안
    ("12:30", "gaeun", "SETTLE", "QUERY"),                       # 예외 5번이 12:00 에 끝난 뒤
    ("13:00", "junho", "SETTLE", "QUERY"),                       # 역할 권한으로 허용되는 요청
    ("14:00", "batch-night", "SALES", "QUERY"),                  # 예외 4번 기간 안
    ("15:00", "junho", "SALES", "CHANGE"),                       # 예외 2번은 10/20(화) 에 끝남
    ("16:20", "seoyeon", "SETTLE", "QUERY"),                     # 예외 1번 기간 안
    ("18:05", "seoyeon", "SETTLE", "QUERY"),                     # 예외 1번이 18:00 에 끝난 뒤
]

counts = {}                                                      # "역할로 허용" · "예외로 허용" · "거부" → 건수
used = {}                                                        # "예외 N번" → 오늘 쓰인 건수

for time, user, resource, action in TODAY_LOG:                   # 기록을 하나씩 꺼낸다
    now = datetime.strptime("2026-10-22 " + time, "%Y-%m-%d %H:%M")   # 오늘 날짜와 그 요청의 시각을 시각으로 바꾼다
    is_allowed, reason = evaluate_access(user, resource, action, now)    # 그 시각으로 최종 판정을 받는다
    print(time, user, resource, action, "->", is_allowed, reason)        # 결과를 출력한다
    if is_allowed and reason == "역할 권한":                               # 역할로 허용이면
        count_key = "역할로 허용"                                     # 세는 기준이 되는 키
        old_count = counts.get(count_key, 0)                     # 그 키의 지금까지 센 수(처음이면 0)
        counts[count_key] = old_count + 1                        # 1 늘려서 다시 적는다
    elif is_allowed:                                                     # 그 밖의 허용은 예외로 허용
        count_key = "예외로 허용"                                     # 세는 기준이 되는 키
        old_count = counts.get(count_key, 0)                     # 그 키의 지금까지 센 수(처음이면 0)
        counts[count_key] = old_count + 1                        # 1 늘려서 다시 적는다
        old_count = used.get(reason, 0)                          # 그 키의 지금까지 센 수(처음이면 0)
        used[reason] = old_count + 1                             # 1 늘려서 다시 적는다
    else:                                                        # 거부면
        count_key = "거부"                                         # 세는 기준이 되는 키
        old_count = counts.get(count_key, 0)                     # 그 키의 지금까지 센 수(처음이면 0)
        counts[count_key] = old_count + 1                        # 1 늘려서 다시 적는다
        if reason == "권한 없음":                                 # 거부 이유가 「권한 없음」일 때만
            permission = resource + ":" + action                 # "자원:행위" 모양 권한 문자열을 만든다
            for exception in EXCEPTIONS:                               # 예외 리스트를 하나씩 꺼낸다
                if exception["user"] == user and exception["permission"] == permission:   # 같은 사람 · 같은 권한의 예외가 있으면
                    print("[만료 뒤 시도]", time, user, resource, action, "- 만료된 예외", exception["id"], exception["expires"])   # 만료 뒤 시도로 알린다

print(counts)                                                    # 방식별 건수를 출력한다
print("예외 사용", used)                                          # 예외 번호별 사용 건수를 출력한다
```
- `evaluate_access` 의 들여쓰기: 본문은 모두 함수 안이라 4칸으로 쓰고, 2번 `if` 아래 `return` 과 3번 `if` 아래 `return` 은 4칸 더(8칸) 들어갑니다. 5번 `if` 아래 `return` 도 8칸입니다.
- `evaluate_access` 를 채우기 전에 실행하면 `TypeError: cannot unpack non-iterable NoneType object` 오류가 납니다. 함수가 아무것도 리턴하지 않아 `is_allowed, reason` 으로 나눠 받지 못하기 때문입니다. 본문을 채운 뒤에 실행합니다.

**순서**

1. **[VS Code 또는 터미널]** 두 파일을 만들고 각각 붙여 넣습니다.
   - 만드는 방법은 Exercise 2-1 의 순서 1번과 같습니다(VS Code 새 파일 아이콘 · `touch` · `vim` 중 하나). 만들 파일 이름은 차례로 `policy.py` · `exercise2-3_run.py` 입니다. 붙여 넣을 내용은 위 코드 상자입니다.
2. **[VS Code]** `policy.py` 의 `evaluate_access` 본문을 직접 씁니다. 3.1 의 그림을 보고 씁니다.
3. **[터미널]** 실행합니다.
   ```bash
   python exercise2-3_run.py
   ```
   - 명령 풀이: `python` 파이썬으로 파일을 실행 · `exercise2-3_run.py` 실행할 파일
   맥북: `python3 exercise2-3_run.py`
4. 요청 아홉 건의 결과 사이에 `[만료 뒤 시도]` 줄이 섞여 나오고, 마지막 두 줄이 방식별 건수와 예외 번호별 사용 건수입니다.
5. **[보고서]** Unit 2 의 `## Exercise 2-3` › `### Exercise 2-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, `[만료 뒤 시도]` 로 출력된 세 건의 사용자와 끝난 예외 번호, 마지막 줄 「예외 사용」에서 예외 1번이 쓰인 횟수를 적어 주세요.
   - (나) [핵심 질문] 역할 판정에서 「권한 없음」이 아닌 이유(퇴사 · 없는 사용자 · 역할이 없음)로 거부되면 예외를 보지 않게 했습니다. 골격의 3번 주석(`# 3. …`)이 없다고 가정하면 퇴사자 `dami` 의 영업 실적 조회는 어떻게 판정되나요? 코드를 지우지 말고 생각해서 답합니다. 3.1 의 그림으로 설명하고, 현업에서 이런 허점이 어떤 사고로 이어질 수 있는지 적어 주세요.
   - (다) [핵심 질문] 오늘 Exercise 2-3까지 만든 파일들이 서로 어떻게 이어지는지 그려 보세요. `exercise2-3_run.py` 에서 출발해, 파일 이름 · 함수 이름 · 읽는 설정 파일을 상자와 화살표(`+---+` · `|` · `v` · `+-->`)로 이어 글자로 그립니다(3.3 의 본보기를 참고). 그린 뒤, `config/exceptions.json` 이 깨졌을 때 이 그림의 어느 화살표에서 멈추는지 적어 주세요.

## Exercise 2-3 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 역할 판정 먼저 | `is_allowed, reason = check_permission(user, resource, action)` |
| 사람이 막히면 예외도 안 봄 | `if reason != "권한 없음": return False, reason` |
| 예외 찾기 | `found, found_exception_id = find_exception(user, f"{resource}:{action}", now)` |
| 이유 남기기 | `"역할 권한"` · `f"예외 {found_exception_id}번"` · 거부 이유 |
| 방식별로 세기 | 「역할 권한」 허용 → 역할로 · 그 밖의 허용 → 예외로 · 거부 |
| 만료 뒤 시도 | 거부 이유가 「권한 없음」이고 같은 사람 · 같은 권한의 예외가 리스트에 있음 |

---

## Unit 2 마무리 — 보고서 Exercise 2-1 · 2-2 · 2-3 칸 확인

Unit 2 의 Exercise 2-1 · 2-2 · 2-3 칸에서 `답:` 뒤가 비어 있는 질문이 없는지 봅니다. `access_control` 폴더에 오늘 만든 파일이 있는지 확인합니다.

```bash
ls
ls config
```

- `role_admin.py` · `exception_policy.py` · `policy.py` · `exercise2-1_run.py` · `exercise2-2_run.py` · `exercise2-3_run.py` 가 보여야 합니다. `config` 안에는 `exceptions.json` 이 새로 보여야 합니다(`users.json` · `roles.json` 은 Unit 1 그대로입니다).

다음 Unit(Unit 3)에서는 설정 파일이 없거나 깨졌을 때도 안전하게 거부하도록 만들고, 오늘 만든 정책을 테스트 네 가지로 검증합니다. 올리기(git)는 Unit 3의 Exercise 3-2 마지막에 한 번에 합니다.

---

<!-- learn:answers -->
