---
id: m3-u01-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/075_day01_pm_rbac.md
  mission_id: GichanSource.m3-1021-pm-rbac
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답을 읽는 법

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## Exercise 1-1 정답

 **`config/users.json` 입니다.**

```json
{
  "seoyeon": {"role": "sales", "employed": true},
  "junho": {"role": "finance", "employed": true},
  "gaeun": {"role": "account_admin", "employed": true},
  "dami": {"role": "sales", "employed": false},
  "batch-night": {"role": "batch", "employed": true},
  "tester": {"role": "intern", "employed": true}
}
```

 **`config/roles.json` 입니다.**

```json
{
  "sales": ["SALES:QUERY", "SALES:CHANGE"],
  "account_admin": ["ACCOUNT:QUERY", "ACCOUNT:CHANGE"],
  "finance": ["SALES:QUERY", "SETTLE:QUERY"],
  "batch": ["SETTLE:QUERY"],
  "auditor": ["SALES:QUERY", "SETTLE:QUERY", "ACCOUNT:QUERY"]
}
```

 **터미널에 입력합니다.**

```bash
python -m json.tool config/users.json
python -m json.tool config/roles.json
```

**결과**


- (가) ① 허용 · ② 거부 · ③ 허용 · ④ 거부 · ⑤ 거부 · ⑥ 허용입니다. 요청 ② 는 **인가**에서 막힙니다. seoyeon 은 비밀번호로 본인임을 확인받았으므로(인증 통과) 누구인지는 맞습니다. 그러나 `sales` 역할에는 `SETTLE:QUERY` 칸에 ○ 가 없어 「이 일을 해도 되나」에서 거부됩니다. Module 2의 사건은 인증만 있고 인가를 확인하는 곳이 없어서 같은 요청이 통과했습니다.
- (나) 한 예: `finance` 의 `SALES:QUERY`. 재무는 정산을 맡고 영업 실적 조회는 하는 일에 꼭 필요하다는 근거가 없습니다. 이 ○ 가 남아 있으면 재무 계정이 도용됐을 때 영업 실적까지 노출됩니다. `auditor` 의 `ACCOUNT:QUERY` 처럼 감사 목적이 분명하면 남길 수 있다고 답해도 맞습니다. 이유가 「하는 일에 필요한가」로 설명되면 됩니다.
- (다) **거부**되어야 합니다. 역할 `intern` 에 어떤 권한을 줄지 아무도 정하지 않았으므로, 정하지 않은 것은 허용하지 않는 기본 거부 원칙에 따라 막습니다. 이유는 「역할이 없음」처럼 따로 남겨, 역할 파일에 빠진 역할이 있다는 것을 담당자가 알 수 있게 합니다.

**왜** — 인증은 「누구」, 인가는 「무엇을」입니다. RBAC 는 인가를 역할 단위로 관리해서, 사람이 바뀌어도 표는 그대로 둡니다. 설정을 파일로 나누면 코드를 고치지 않고 사람만 바꿀 수 있고, JSON 규칙이 하나만 틀려도 프로그램이 파일을 못 읽으므로 먼저 검사합니다. 매트릭스와 설정 파일이 같아야 코드가 표대로 판정하고, 표에 없는 역할은 권한이 없는 것으로 다룹니다.

**자주 틀리는 곳** — ⑤ 를 「계정 관리자는 높은 권한이니 허용」으로 판정하는 경우가 많습니다. 매트릭스에 ○ 가 없으면 직급과 상관없이 거부입니다. 인증과 인가를 같은 말로 쓰는 경우도 많습니다. `true` 를 파이썬처럼 `True` 로 쓰는 실수가 가장 많고(JSON 오류), 마지막 줄 뒤 쉼표, 작은따옴표(`'sales'`) 사용, `batch-night` 를 `batch_night` 로 쓰는 오타도 많습니다. `"account_admin"` 줄 끝에 쉼표를 안 붙여 JSON 오류가 나는 경우, `auditor` 에 `ACCOUNT:CHANGE` 까지 넣는 실수도 있습니다(매트릭스의 ○ 는 `ACCOUNT:QUERY` 하나입니다).

**관제에서는** — 「로그인은 정상인데 맡지 않은 자원에 접근」한 기록은 인가 쪽 문제로 분류하고 매트릭스와 대조합니다. 퇴사자 계정이 살아 있는 것은 감사에서 가장 자주 지적되는 항목이라 인사 리스트와 계정 리스트를 정기적으로 대조하고, 역할 파일에 없는 역할을 가진 사용자는 설정 누락의 신호입니다.

---

## Exercise 1-2 정답

 **터미널에 입력합니다.**

```bash
python exercise1-2_run.py
```

**채운 코드** (한 예)

```python
    if not USERS[user]["employed"]:                              # 재직 중이 아니면
        return False, "퇴사한 계정"                                # 거부하고 함수를 끝낸다
    role = USERS[user]["role"]                                   # 이 사용자의 역할을 꺼낸다
    if role not in ROLES:                                        # 역할 파일에 없는 역할이면
        return False, "역할이 없음"                                # 거부하고 함수를 끝낸다
    permission = f"{resource}:{action}"                          # "자원:행위" 모양 문자열로 합친다
    if permission not in ROLES[role]:                            # 그 역할의 권한 리스트에 없으면
        return False, "권한 없음"                                  # 거부하고 함수를 끝낸다
```

**결과**

- 채우기 전 출력은 다음과 같습니다(`minsu` 만 거부).

```
seoyeon SALES QUERY -> True 허용
seoyeon SETTLE QUERY -> True 허용
junho SETTLE QUERY -> True 허용
junho SALES CHANGE -> True 허용
dami SALES QUERY -> True 허용
minsu SALES QUERY -> False 등록되지 않은 사용자
gaeun ACCOUNT CHANGE -> True 허용
batch-night SETTLE QUERY -> True 허용
tester SALES QUERY -> True 허용
```

  내가 채운 코드는 위의 코드입니다. 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.


- (가) 채운 뒤의 출력입니다.

```
seoyeon SALES QUERY -> True 허용
seoyeon SETTLE QUERY -> False 권한 없음
junho SETTLE QUERY -> True 허용
junho SALES CHANGE -> False 권한 없음
dami SALES QUERY -> False 퇴사한 계정
minsu SALES QUERY -> False 등록되지 않은 사용자
gaeun ACCOUNT CHANGE -> True 허용
batch-night SETTLE QUERY -> True 허용
tester SALES QUERY -> False 역할이 없음
```

  - `minsu` 는 [1](사용자 없음), `dami` 는 [2](퇴사), `tester` 는 [3](역할 없음), `seoyeon` 의 정산 조회와 `junho` 의 영업 실적 변경은 [4](권한 없음)에서 걸렸습니다.
- (나) 허용되면 안 되는 요청은 네 건입니다: `seoyeon` 의 정산 조회(영업에는 정산 권한이 없음), `junho` 의 영업 실적 변경(재무에는 변경 권한이 없음), `dami` 의 영업 실적 조회(퇴사자), `tester` 의 영업 실적 조회(역할 `intern` 이 역할 파일에 없음). 검사가 [1] 하나뿐이면 [2] ~ [4] 의 경우가 모두 마지막 `return True` 까지 내려가 허용됩니다. Module 2의 사건(영업 계정의 정산 조회)도 다시 통과합니다. Module 2의 **열림 기본 값(fail-open)** 과 같은 문제입니다. 확인하지 못한 경우를 통과시키면 그 틈이 그대로 공격 경로가 됩니다.
- (다) 판정은 둘 다 거부지만 **이유가 달라집니다.** 지금 순서([2] → [3])면 「퇴사한 계정」으로 남습니다. 순서를 바꾸면([3] → [2]) 역할 `none` 이 역할 파일에 없어서 [3] 에서 먼저 걸려 「역할이 없음」으로 남고, 퇴사자라는 진짜 이유가 기록에서 사라집니다. 사람 자체를 먼저 확인하고(있나 · 재직 중인가) 그다음 역할 · 권한을 보는 순서가 이유를 정확하게 남깁니다.

**왜** — 접근통제 함수는 「허용할 조건을 모두 확인한 뒤에만 허용」해야 합니다. 맨 끝의 `return True` 앞에 빠진 검사가 있으면 그 경우는 모두 허용됩니다.

**자주 틀리는 곳** — `return` 을 빼고 `False, "퇴사한 계정"` 만 써서 검사가 아무 일도 안 하는 경우가 많습니다. `f"{resource}:{action}"` 에서 `f` 를 빼면 글자 그대로 `{resource}:{action}` 이 되어 모두 「권한 없음」이 됩니다. `role` 을 담기 전에 `role not in ROLES` 를 써서 `NameError` 가 나는 경우도 있습니다. 들여쓰기가 `if` 와 맞지 않으면 `IndentationError` 가 납니다.

**관제에서는** — 거부 이유가 구분돼 있으면 「권한 없음」이 몰리는 계정(사건 신호)과 「역할이 없음」이 몰리는 계정(설정 누락)을 나눠 볼 수 있습니다.

---

## Exercise 1-3 정답

 **터미널에 입력합니다.**

```bash
python exercise1-3_audit.py
```

**채운 코드** (한 예)

단계 1:

```python
for log_id, time, user, resource, action in LOG:                 # 기록을 하나씩 꺼낸다
    is_allowed, reason = check_permission(user, resource, action)        # 판정 결과와 이유를 받는다
    if is_allowed:                                                       # 허용이면
        allowed = allowed + 1                                    # 허용 건수를 1 늘리고
        count_key = user + " 허용"                                 # 세는 기준이 되는 키
        old_count = counts.get(count_key, 0)                     # 그 키의 지금까지 센 수(처음이면 0)
        counts[count_key] = old_count + 1                        # 1 늘려서 다시 적는다
        role = USERS[user]["role"]                               # 그 사용자의 역할을 꺼내고
        if role not in used:                                     # 이 역할이 처음이면
            used[role] = []                                      # 빈 리스트를 만든 뒤
        used[role].append(f"{resource}:{action}")                # 쓴 권한을 리스트에 추가한다
    else:                                                        # 거부면 (쓴 권한으로 모으지 않는다)
        denied = denied + 1                                      # 거부 건수를 1 늘리고
        print("[거부]", log_id, time, user, resource, action, "-", reason)   # 거부된 기록을 출력하고
        count_key = user + " 거부"                                 # 세는 기준이 되는 키
        old_count = counts.get(count_key, 0)                     # 그 키의 지금까지 센 수(처음이면 0)
        counts[count_key] = old_count + 1                        # 1 늘려서 다시 적는다
```

단계 2:

```python
for role, permissions in ROLES.items():                          # 역할과 권한 리스트를 하나씩 꺼낸다
    for permission in permissions:                               # 권한을 하나씩 꺼내
        if permission not in used.get(role, []):                 # 실제로 쓴 리스트에 없으면
            print("쓰이지 않음", role, permission)                 # 쓰이지 않은 권한으로 출력한다
```

**결과**

- 출력은 다음과 같습니다(역할 순서는 `roles.json` 의 순서를 따릅니다).

```
[거부] 3 02:14 seoyeon SETTLE QUERY - 권한 없음
[거부] 4 02:15 seoyeon SETTLE QUERY - 권한 없음
[거부] 5 02:15 seoyeon SETTLE QUERY - 권한 없음
[거부] 12 13:40 seoyeon SETTLE QUERY - 권한 없음
[거부] 14 14:10 seoyeon SETTLE QUERY - 권한 없음
[거부] 15 14:35 seoyeon SETTLE QUERY - 권한 없음
[거부] 16 15:00 seoyeon SETTLE QUERY - 권한 없음
[거부] 17 15:25 seoyeon SETTLE QUERY - 권한 없음
허용 7 거부 8
{'batch-night 허용': 1, 'seoyeon 거부': 8, 'junho 허용': 3, 'seoyeon 허용': 3}
쓰이지 않음 sales SALES:CHANGE
쓰이지 않음 account_admin ACCOUNT:QUERY
쓰이지 않음 account_admin ACCOUNT:CHANGE
쓰이지 않음 finance SALES:QUERY
쓰이지 않음 auditor SALES:QUERY
쓰이지 않음 auditor SETTLE:QUERY
쓰이지 않음 auditor ACCOUNT:QUERY
```

- (가) 허용 7건 · 거부 8건이고, 거부된 번호는 3 · 4 · 5 · 12 · 14 · 15 · 16 · 17번입니다(모두 `seoyeon` 의 `SETTLE:QUERY`). 한 예: 점수 판단은 기기 · 시각 · 국가 · 건수 같은 **상황**을 보고 위험 점수를 매깁니다. 낮의 12 · 14 ~ 17번은 등록 기기 · 낮 시간 · 적은 건수라 점수가 낮아 허용됐습니다. RBAC 는 **역할이 그 자원에 그 행위를 해도 되는지**만 봅니다. 상황이 정상이어도 영업 역할에는 정산 조회 권한이 없으므로 시각과 상관없이 모두 막습니다. 둘은 서로 다른 것을 보므로 함께 써야 합니다.
- (나) **말할 수 없습니다.** 확인되는 것은 「이 하루 기록의 조회 15건에서 seoyeon 의 정산 조회 8건만 거부됐고, 재무 · 서비스 계정 · 영업의 영업 실적 조회는 막히지 않았다」입니다. 확인되지 않는 것은 다른 날 · 다른 직원의 업무, 기록에 없는 변경(`CHANGE`) 요청, 그리고 seoyeon 이 정산 조회를 해야 하는 정당한 업무가 있었는지입니다. 하루치 기록의 한계도 있습니다. 월말 정산, 분기 감사, 계정 변경처럼 가끔 하는 업무가 빠지므로 「쓰이지 않음」을 바로 지우면 정상 업무가 막힙니다. 현업에서는 보통 **90일** 같은 긴 기간을 정해 한 번도 쓰이지 않은 권한을 후보로 뽑고 담당자 확인을 거칩니다(Unit 6의 과다권한 탐지).
- (다) 한 예: Exercise 1-1 에서 `finance` 의 `SALES:QUERY` 를 필요 이상이라고 골랐다면 이 기록에서도 `쓰이지 않음 finance SALES:QUERY` 로 나와 두 근거가 일치합니다. **줄일 것은 `finance` 의 `SALES:QUERY`** 입니다. 재무의 일(정산)에 필요하다는 근거가 없고 기록에도 쓰이지 않았습니다. **남길 것은 `account_admin` 의 `ACCOUNT:CHANGE`** 입니다. 계정 관리자는 이 일을 맡은 역할이고, 하루 기록에 계정 변경이 없었을 뿐입니다. `sales` 의 `SALES:CHANGE` 는 영업이 실적을 고쳐야 하는지 영업팀에 확인한 뒤 정한다고 답해도 맞습니다. 참고로 `auditor` 역할은 사용자가 한 명도 없어서 모든 권한이 「쓰이지 않음」으로 나옵니다. 지금 당장 위험은 없지만 나중에 누군가에게 잘못 붙으면 넓은 조회 권한이 생기므로, 감사가 실제로 필요한 때 기간을 정해 주는 쪽으로 처리합니다.

**왜** — 새 규칙을 과거 기록에 먼저 적용하면 켜는 날 정상 업무가 갑자기 막히는 일과 막아야 할 것을 놓치는 일을 미리 줄일 수 있습니다. 최소권한은 「준 권한」과 「쓴 권한」을 맞춰 볼 때 실제로 확인되고, 쓰이지 않는 권한은 사고가 나면 피해 범위만 넓힙니다.

**자주 틀리는 곳** — `for` 에서 다섯 값을 받지 않고 `for user, resource, action in LOG` 처럼 세 개만 받아 `ValueError: too many values to unpack` 이 나는 경우가 가장 많습니다. `old_count = counts[키]` 처럼 `.get` 없이 꺼내 처음 보는 키에서 `KeyError` 가 나는 경우도 많으니 `.get(키, 0)` 을 씁니다. 거부된 기록까지 `used` 에 모아서 `sales` 가 `SETTLE:QUERY` 를 「쓴」 것처럼 되는 경우도 많습니다. 거부는 쓴 것이 아닙니다. `used[role]` 을 만들기 전에 `append` 해서 `KeyError` 가 나는 경우, 단계 2 에서 `used[role]` 로 바로 꺼내 기록에 없는 역할(`auditor`)에서 `KeyError` 가 나는 경우도 있으니 `used.get(role, [])` 를 씁니다. 출력만 보고 「정상 업무는 막히지 않는다」고 단정하거나 「쓰이지 않음」을 모두 바로 지우자고 결론 내는 것도 흔한 실수입니다.

**관제에서는** — 규칙을 바꾸기 전과 후의 판정 차이를 숫자로 남겨 두면 켠 뒤 문의가 들어왔을 때 원인이 규칙 변경인지 바로 알 수 있습니다. 미사용 권한 리스트는 정기 권한 점검의 첫 자료이고, 그대로 회수하지 않고 역할 담당자 확인을 거쳐 회수 이력을 남깁니다.

---

## 정답 마무리

 **터미널에 입력합니다.**

```bash
cd ..
pwd
git status
git add .
git commit -m "Add access control day 1 RBAC config, checker and report"
git push
```

**결과**

- (가) 한 예: 「줄이 1개였고(`access_control/`), `.env` · `.venv` 는 없었다」. Module 2 파일을 올린 뒤 바로 했다면 `access_control/` 한 줄만 보입니다. 줄 수와 이름은 학생마다 다를 수 있습니다. `.env` 나 `.venv` 가 보였다면 `.gitignore` 에 한 줄을 적고 `git status` 를 다시 쳤다고 적습니다.

**왜** — 올리기 전에 올라갈 파일을 확인해야 비밀 키가 섞이지 않습니다. Module 3 설정 파일과 판정 코드는 Unit 2 · Unit 4 · 캡스톤에서 다시 씁니다.

**자주 틀리는 곳** — `.env` 가 보이는데 그대로 `git add .` 를 하는 실수가 가장 위험합니다. `cd ..` 를 두 번 쳐서 `security-agent-toolkit` 바깥으로 나가는 경우도 있습니다. `pwd` 로 확인합니다.

**관제에서는** — 접근통제 설정 파일은 바뀔 때마다 저장소에 남겨, 누가 언제 어떤 권한을 바꿨는지 추적할 수 있게 합니다.
