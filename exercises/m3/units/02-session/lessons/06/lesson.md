---
id: m3-u02-l06
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/078_day02_am_policy.md
  mission_id: GichanSource.m3-1022-am-policy
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## Exercise 2-1 정답

 **터미널에 입력합니다.**

```bash
python exercise2-1_run.py
```

**채운 코드** (한 예)

```python
    if role not in ROLES:                                        # 역할 파일에 없는 역할이면
        return False, "없는 역할"                                 # 부여하지 않고 거부한다
    users[name] = {"role": role, "employed": True}               # 사용자 항목을 새로 만들거나 덮어쓴다
    return True, "부여"                                           # 부여했다고 알린다
```

```python
    if name not in users:                                        # 사용자 파일에 없는 이름이면
        return False, "없는 사용자"                               # 회수할 것이 없다고 알린다
    users[name]["employed"] = False                              # employed 값을 False 로 바꾼다
    return True, "회수"                                           # 회수했다고 알린다
```

- 위 코드는 `assign_role` 과 `revoke_access` 의 본문입니다. 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

**결과**

- (가) 출력은 다음과 같고, `hana` 줄은 `False` 입니다. 역할 이름 `salse` 가 `ROLES` 에 없어서 부여가 거부되고 사용자 항목도 만들어지지 않았습니다.

```
--- 인사 변경 전
minsu SALES QUERY -> False 등록되지 않은 사용자
seoyeon SALES CHANGE -> True 허용
seoyeon SETTLE QUERY -> False 권한 없음
junho SETTLE QUERY -> True 허용
--- 인사팀 통보 처리
입사 minsu (True, '부여')
입사 hana (False, '없는 역할')
hana 가 사용자에 들어갔나 False
이동 seoyeon (True, '부여')
퇴사 junho (True, '회수')
퇴사 ghost (False, '없는 사용자')
--- 인사 변경 후
minsu SALES QUERY -> True 허용
seoyeon SALES CHANGE -> False 권한 없음
seoyeon SETTLE QUERY -> True 허용
junho SETTLE QUERY -> False 퇴사한 계정
```

- (나) `SALES CHANGE` 는 **허용에서 거부**(`권한 없음`)로, `SETTLE QUERY` 는 **거부에서 허용**으로 바뀌었습니다. `seoyeon` 의 역할이 `sales` 에서 `finance` 로 바뀌었고, `finance` 에는 `SALES:QUERY` 와 `SETTLE:QUERY` 만 있고 `SALES:CHANGE` 가 없기 때문입니다. 역할 값 하나만 바꿨는데 권한 전체가 바뀐 것입니다. 이동한 사람에게 이전 역할의 권한(영업 실적 변경)이 남아 있으면 새 업무에 필요 없는 권한이 계속 쌓입니다. 계정이 도용되거나 실수가 생기면 영향받는 범위가 넓어지고, 일에 필요한 만큼만 준다는 최소권한과도 어긋납니다.
- (다) 사흘 동안 `junho` 의 사용자 항목은 아직 재직(`employed` 가 `true`)이라서 정산 조회가 계속 허용됩니다. 나간 사람이 자료를 내려받거나 변경할 수 있고, 로그에는 정상 사용자의 행동으로 남아서 나중에 가려내기 어렵습니다. 간격을 줄이는 방법은 여러 가지가 있습니다. ① 인사 시스템이 퇴사가 확정되는 즉시 보안 담당에게 알리게 한다 ② 퇴사 예정일을 미리 받아 그 시각에 맞춰 회수한다 ③ 인사 명단과 계정 리스트를 매일 대조해 어긋난 계정을 찾는다 ④ 퇴사 당일 회수 확인을 체크리스트에 넣는다. 두 가지 이상이고 핵심이 같으면 맞습니다.

**왜** — 사람이 바뀔 때마다 파일을 손으로 고치면 오타와 빠뜨림이 생깁니다. 함수로 처리하면 「없는 역할은 거부」 같은 검사가 늘 같은 순서로 들어갑니다. 역할 값 하나만 바꾸면 권한이 통째로 바뀌므로, 이동한 사람에게 이전 권한이 남지 않게 새 역할로 **바꿉니다.**(역할을 하나 더 붙이지 않습니다.) 퇴사자 항목을 삭제하지 않고 `employed` 값만 바꾸면, 거부 이유가 「퇴사한 계정」으로 남아서 처음부터 없던 계정과 구분됩니다.

**자주 틀리는 곳** — `if role in ROLES:` 로 `not` 을 빼먹어 정상 역할을 모두 거부하는 경우가 가장 많습니다. 사용자 항목을 먼저 바꾸고 역할을 검사해서, 오타 역할이 이미 들어간 뒤에 거부하는 경우도 많습니다(`hana 가 사용자에 들어갔나` 가 `True`). `False` 를 소문자 `false` 로 써서 `NameError` 가 나는 경우도 있습니다(소문자는 JSON 파일에서만 씁니다). `return` 을 빼먹으면 통보 처리 줄이 `None` 으로 나옵니다. 함수 안에서 `users = {…}` 로 새 딕셔너리를 만들어 담으면 바깥의 `USERS` 는 바뀌지 않아서, 부여 결과는 `(True, '부여')` 인데 `minsu` 와 `seoyeon` 의 변경 후 판정이 변경 전과 같습니다.

**관제에서는** — 인사 통보와 계정 상태를 정기적으로 대조합니다. 퇴사 당일에 접근을 회수하지 않으면 퇴사자 계정을 쓸 수 있는 시간이 생기고, 이동한 사람은 이전 역할의 권한이 남지 않았는지 확인합니다. 부여와 회수는 누가 언제 했는지 기록으로 남겨 감사에 대비합니다.

---

## Exercise 2-2 정답

 **터미널에 입력합니다.**

```bash
python exercise2-2_run.py
```

**`config/exceptions.json` 의 4번 · 5번 예외** (한 예)

```json
  {"id": 4, "user": "batch-night", "permission": "SALES:QUERY", "expires": "2026-10-23 09:00", "reason": "분기 집계 시험"},
  {"id": 5, "user": "gaeun", "permission": "SETTLE:QUERY", "expires": "2026-10-22 12:00", "reason": "감사 자료 대응"}
```

- `"id": 3` 줄 끝에는 쉼표가 있고, `"id": 5` 줄 뒤에는 쉼표가 없어야 합니다.

**채운 코드** (한 예)

```python
    for exception in EXCEPTIONS:                                       # 예외를 하나씩 꺼낸다
        if exception["user"] == user and exception["permission"] == permission:   # 사람과 권한이 같으면
            expires = datetime.strptime(exception["expires"], TIME_FORMAT)  # 만료 시각을 시각으로 바꾸고
            if now < expires:                                    # 아직 만료 전이면
                return True, exception["id"]                           # 유효한 예외와 그 번호를 리턴한다
    return False, None                                           # 못 찾았으면 없다고 리턴한다
```

**결과**

- (가) 출력은 다음과 같고, 회수할 것은 **2번 · 5번(만료됨)과 3번(퇴사자)** 입니다. 코드는 위의 채운 코드입니다. 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

```
seoyeon SETTLE:QUERY -> (True, 1)
junho SALES:CHANGE -> (False, None)
dami SALES:QUERY -> (True, 3)
batch-night SALES:QUERY -> (True, 4)
gaeun SETTLE:QUERY -> (False, None)
seoyeon ACCOUNT:CHANGE -> (False, None)
```

```
[유지] 1 seoyeon SETTLE:QUERY 2026-10-22 18:00
[회수] 만료됨 2 junho SALES:CHANGE 2026-10-20 18:00
[회수] 퇴사자 3 dami SALES:QUERY 2026-10-31 18:00
[유지] 4 batch-night SALES:QUERY 2026-10-23 09:00
[회수] 만료됨 5 gaeun SETTLE:QUERY 2026-10-22 12:00
```

  - 단계 1 에서 `(False, None)` 이 나온 세 건의 이유는 다음과 같습니다. `junho` 는 예외 2번이 10/20(화) 18:00 에 이미 만료됐습니다. `gaeun` 은 예외 5번이 오늘 12:00 에 만료됐고 지금은 14:00 입니다. `seoyeon` 의 `ACCOUNT:CHANGE` 는 예외 자체가 없습니다.
  - `dami` 의 예외 3번은 `(True, 3)` 으로 유효하게 나오지만 퇴사자입니다. 예외 판정은 재직 여부를 보지 않으므로, 이 결과만 보고 허용하면 안 되고 사용자 파일의 `employed` 칸을 함께 봐야 합니다(Exercise 2-3).
- (나) 만료 시각이 없는 예외는 아무도 회수하지 않아서 계속 열린 채로 쌓입니다. 1년 뒤에는 누가 왜 받았는지 아는 사람이 없고, 이동 · 퇴사한 사람에게도 남아서 감사에서 「과다권한」 · 「회수 누락」을 지적받습니다. 규칙 예: 만료 시각이 비어 있으면 접수하지 않는다, 최대 기간(예: 30일)을 정하고 넘기려면 다시 승인받는다, 만료가 가까워지면 알림을 보낸다.
- (다) 확인할 것: 이 일이 정말 프로그램이 하는 집계 작업인지, 사람이 자기 일을 서비스 계정으로 대신하려는 것인지, 요청자와 승인자가 누구인지, 연장하려는 기간과 권한이 얼마나 되는지. 서비스 계정은 로그인한 사람이 없어서 누가 썼는지 추적하기 어렵고 키가 새면 피해가 크므로, 사람이 쓰려는 것이면 연장하지 않고 사람 계정에 기간을 정해 주도록 제안하는 것이 안전합니다. 프로그램의 집계 작업이 맞다면 기간을 짧게(작업이 끝나는 날까지), 권한은 조회만, 사용 기록을 따로 감시, 만료 시 자동 회수의 조건을 붙여 연장할 수 있습니다. 연장 또는 거절 어느 쪽이든 판단 근거가 있으면 맞습니다.

**왜** — 예외는 사람 · 권한 · 시각이 모두 맞아야 유효합니다. 시각을 시각으로 바꿔 비교하면 「언제까지」를 코드가 확인합니다. 코드가 만료된 예외를 거부하더라도 리스트에 남은 예외는 점검을 어렵게 하므로, 퇴사자의 예외는 만료 시각과 상관없이 바로 회수합니다.

**자주 틀리는 곳** — `return False, None` 을 `for` 안에 넣어 첫 예외만 보고 끝나는 경우가 가장 많습니다(`seoyeon` 말고는 모두 `False` 가 됩니다). 형식에서 `%m` 과 `%M` 을 헷갈리면 `ValueError` 가 납니다(`%m` 은 월, `%M` 은 분). `now <= expires` 로 쓰면 18:00 정각이 허용됩니다. 4 · 5번 예외를 빼먹거나 3번 줄 끝 쉼표를 빼먹으면 `json.decoder.JSONDecodeError` 가 납니다.

**관제에서는** — 만료 시각이 지난 예외로 들어온 요청이 거부된 기록은 「예외가 끝난 것을 모르고 계속 시도」한 신호라서 담당자에게 알립니다. 회수 리스트는 매일 만들고, 회수한 예외는 지우지 않고 「회수 시각 · 회수 이유」를 남겨 감사 기록으로 둡니다(3과목 Unit 8 권한 회수).

---

## Exercise 2-3 정답

 **터미널에 입력합니다.**

```bash
python exercise2-3_run.py
```

**채운 코드** (한 예)

```python
    is_allowed, reason = check_permission(user, resource, action)        # 역할 판정을 먼저 한다
    if is_allowed:                                                       # 역할로 허용되면
        return True, "역할 권한"                                   # 역할 권한으로 허용한다
    if reason != "권한 없음":                                     # 사용자 자체가 거부 대상이면(없음 · 퇴사 · 역할이 없음)
        return False, reason                                     # 예외를 보지 않고 그 이유로 거부한다
    found, found_exception_id = find_exception(user, f"{resource}:{action}", now)   # 유효한 예외를 찾는다
    if found:                                                    # 있으면
        return True, f"예외 {found_exception_id}번"                            # 예외 번호와 함께 허용한다
    return False, "권한 없음"                                      # 둘 다 없으면 거부한다
```

**결과**

- (가) 출력은 다음과 같습니다. 코드는 위의 채운 코드이고, 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

```
09:10 seoyeon SETTLE QUERY -> True 예외 1번
10:00 dami SALES QUERY -> False 퇴사한 계정
11:40 gaeun SETTLE QUERY -> True 예외 5번
12:30 gaeun SETTLE QUERY -> False 권한 없음
[만료 뒤 시도] 12:30 gaeun SETTLE QUERY - 만료된 예외 5 2026-10-22 12:00
13:00 junho SETTLE QUERY -> True 역할 권한
14:00 batch-night SALES QUERY -> True 예외 4번
15:00 junho SALES CHANGE -> False 권한 없음
[만료 뒤 시도] 15:00 junho SALES CHANGE - 만료된 예외 2 2026-10-20 18:00
16:20 seoyeon SETTLE QUERY -> True 예외 1번
18:05 seoyeon SETTLE QUERY -> False 권한 없음
[만료 뒤 시도] 18:05 seoyeon SETTLE QUERY - 만료된 예외 1 2026-10-22 18:00
{'예외로 허용': 4, '거부': 4, '역할로 허용': 1}
예외 사용 {'예외 1번': 2, '예외 5번': 1, '예외 4번': 1}
```

  `[만료 뒤 시도]` 세 건은 다음과 같고, 「예외 사용」 줄에서 예외 1번은 **2번** 쓰였습니다.
  - 12:30 `gaeun` 의 정산 조회: 예외 5번이 12:00 에 끝난 뒤의 시도.
  - 15:00 `junho` 의 영업 실적 변경: 예외 2번이 10/20(화) 18:00 에 끝난 뒤의 시도.
  - 18:05 `seoyeon` 의 정산 조회: 예외 1번이 18:00 에 끝난 뒤의 시도.
  `dami` 10:00 요청은 `[역할 판정]` 에서 「퇴사한 계정」으로 거부되어 「권한 없음」이 아니므로 예외 리스트를 보지 않습니다. 사람 자체가 거부 대상이라 예외가 남아 있어도 만료 뒤 시도로 보지 않습니다.
- (나) **허용**됩니다. `dami` 는 `[역할 판정]` 에서 「퇴사한 계정」으로 거부되지만, 골격의 3번 주석(`# 3. …`)이 없으면 바로 `[예외 판정]` 으로 가서 예외 3번(10/31(토) 까지)을 찾아 「예외 3번」으로 허용됩니다. 현업에서는 퇴사자가 남은 예외로 영업 자료를 조회하고, 로그에는 정상 허용으로 남아 아무도 눈치채지 못하는 사고로 이어질 수 있습니다. 감사에서는 퇴사자 계정이 사용된 기록으로 지적됩니다.
- (다) 그림은 다음과 같고, 핵심(누가 누구를 호출하는가)이 같으면 맞습니다. `config/exceptions.json` 이 깨지면 `policy.py` 가 `exception_policy.py` 를 불러오는 맨 위의 `import` 에서 멈추고(`JSONDecodeError`), `exercise2-3_run.py` 는 요청을 한 건도 판정하기 전에 끝납니다.

```
+------------------+
| exercise2-3_run.py |
+------------------+
   |
   +--> evaluate_access(user, resource, action, now) 호출
   |       |
   |       v
   |    +-------------------------------+
   |    | policy.py : evaluate_access() |
   |    +-------------------------------+
   |       |
   |       +--> 1. check_permission() 호출
   |       |       |
   |       |       v
   |       |    +---------+
   |       |    | rbac.py |
   |       |    +---------+
   |       |       |  읽음
   |       |       v
   |       |    config/users.json · config/roles.json
   |       |    (허용이면 「역할 권한」 으로 끝 / 「권한 없음」 이 아닌 이유면 그 이유로 거부하고 끝)
   |       |
   |       +--> 2. find_exception() 호출
   |       |       |
   |       |       v
   |       |    +---------------------+
   |       |    | exception_policy.py |
   |       |    +---------------------+
   |       |       |  읽음 (파일을 불러올 때 한 번)
   |       |       v
   |       |    config/exceptions.json
   |       |
   |       v
   |    (허용 여부, 이유) 를 리턴
   |       |
   |       v
   |    exercise2-3_run.py 가 건수를 세고 출력  (EXCEPTIONS 도 exception_policy.py 에서 가져옴)
```

**왜** — 여러 규칙을 합칠 때는 「사람이 유효한가」를 먼저 보고, 그다음 「무엇으로 허용하나」를 봅니다. 예외는 역할 권한을 보충할 뿐 사람 검사를 건너뛰게 하면 안 됩니다. 허용을 「역할」과 「예외」로 나눠 세고 예외 번호별로 쓰인 횟수를 세면, 예외로 열리는 일이 얼마나 되는지 숫자로 보입니다.

**자주 틀리는 곳** — `find_exception` 에 `resource` 만 넣어 항상 `(False, None)` 이 나오는 경우가 많습니다. 예외 파일은 `"SETTLE:QUERY"` 처럼 「자원:행위」 문자열로 적혀 있습니다. 3번을 `if reason == "권한 없음"` 으로 뒤집어 써서 반대로 동작하는 경우도 있습니다. `return` 을 빼먹으면 실행할 때 `TypeError: cannot unpack non-iterable NoneType object` 가 납니다.

**관제에서는** — 판정 이유에 「역할 권한」 · 「예외 N번」 · 거부 이유가 남아 있으면, 감사 때 「왜 열렸나」를 예외 번호로 바로 찾아갈 수 있습니다. 거부된 요청이 끝난 예외와 같은 사람 · 같은 권한이면 만료 뒤 시도로 따로 모아 담당자에게 알리고, 같은 예외가 계속 쓰이면 역할을 새로 만들지, 예외를 끝낼지 판단합니다.
