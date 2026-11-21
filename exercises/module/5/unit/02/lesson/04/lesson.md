---
id: m5-u02-l04
title: 실습 2-2 · 활성 세션 종료와 잔존 세션 점검하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/122_day03_am_containment.md
  mission_id: GichanSource.m5-1111-am-containment
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 2-2 · 활성 세션 종료와 잔존 세션 점검하기

## 목표: 세션 종료와 빈틈 점검

> **오늘 들어온 일**
>
> - **상황**: 퇴사자 `dami` 의 계정을 잠갔다고 기록했는데, 잠근 후에도 `dami` 의 서버 요청이 두 건 더 들어왔습니다. 잠금 실행 전에 이미 인증을 마친 **세션**(session, 세션: 로그인한 뒤 서버가 유지하는 접속 상태)이 두 개 남아 있었기 때문입니다.
> - **문제**: 계정을 잠그면 새 로그인(인증)만 차단되고, 이미 열려 있는 세션은 계속 유효합니다. 잠금만 하고 끝내면 퇴사자가 세션이 만료될 때까지 접속할 수 있는데, 이 상태를 점검하는 절차가 없습니다.
> - **부탁**: 계정을 잠근 후에는 열린 세션도 모두 종료해 주세요. 그리고 잠겼는데 활성 세션이 남은 계정이 있는지 점검하는 기능도 만들어 주세요.
> - **바뀌는 점**: 잠금과 세션 종료가 함께 실행되고, 조치가 누락된 계정은 점검에서 즉시 탐지됩니다. 오늘 샘플에서는 이미 잠겨 있는데 세션 하나가 열려 있는 `junho` 가 점검에서 발견됩니다. 상황은 설명을 위한 예시입니다.

## 2.1 계정 잠금은 새 로그인을 차단하고, 세션 종료는 이미 열린 접속을 종료한다

**세션**(session, 세션: 로그인한 뒤 서버가 유지하는 접속 상태)이 유효하면 서버는 비밀번호를 다시 요구하지 않습니다. 따라서 계정을 잠가도 이미 발급된 세션은 계속 사용할 수 있습니다. 예를 들어 아침에 로그인해 둔 `dami` 의 세션 `S-101` 은 계정을 잠근 후에도 서버에 요청을 보낼 수 있습니다. 세션은 서버 쪽에서 무효화(invalidate, 인밸리데이트: 그 세션을 더는 인증에 쓸 수 없게 만드는 일)해야 종료되므로, 잠금 뒤에 세션 종료 조치가 따로 필요합니다. 조치 순서도 중요합니다.

| 순서 | 결과 |
|---|---|
| 잠금 → 세션 종료 (오늘 구현) | 새 로그인이 이미 차단되어 있어서, 세션을 종료하면 더는 접속할 수 없다 |
| 세션 종료 → 잠금 | 두 조치 사이에 재로그인(re-login)이 가능해 새 세션이 생길 수 있다 |
| 잠금만 | 활성 세션으로 계속 접속할 수 있다 |

- 이 표는 오늘 연습용 시스템의 동작 규칙입니다. 실제 서비스는 시스템마다 동작이 다르므로, 계정을 잠글 때 세션이 어떻게 처리되는지 먼저 확인해야 합니다.
- 따라서 세션 종료는 **잠금이 사후 검증으로 확인된 뒤에만** 실행합니다. 잠금이 적용되지 않았거나 VIP 정책으로 차단된 계정의 세션은 종료하면 안 됩니다.
- 수업 시작 상태에서 `junho` 는 이미 잠겨 있지만 세션이 하나 열려 있습니다. 이처럼 계정은 잠겼는데 활성 세션이 잔존(residual, 레지듀얼: 조치 후에도 남아 있음)하는 상태를 이 문서에서는 **빈틈**이라 부릅니다(출력에도 「빈틈」으로 표시됩니다). 이 빈틈을 찾아내는 점검이 `find_open_sessions` 입니다.

**문법 상자 · 직접 쓰는 곳의 모양 (예시 값 · 읽기만 합니다)**

```python
sessions = {"dami": ["S-101", "S-102"]}   # 예시 값
sessions["dami"] = []                     # 키 dami 의 값을 빈 리스트로 바꾼다
print(sessions)                           # {'dami': []}
after = "잠김"                            # 예시 값
print(after == "잠김")                    # True  · 두 값이 같음 (= 하나는 저장, == 두 개는 비교)
```

| 코드 | 뜻 |
|---|---|
| `딕셔너리[키] = []` | 그 키의 값을 빈 리스트로 바꾼다 (①) |
| `if 값 == "잠김":` | 두 값이 같으면 아래 줄을 실행한다 (②) |
| `리스트.append(함수(…))` | 함수가 리턴한 값을 리스트에 더한다 (③) |

함수는 두 파일에 나뉘어 있고 실행 파일이 하나 더 있습니다. 대부분은 미리 채워 두었고, 직접 쓰는 곳은 **세 곳**(① · ② · ③)입니다.

```
session_actions.py  terminate_sessions  : 계정의 세션 리스트를 비운다 (① 세션 종료)
                    find_open_sessions  : 잠긴 계정 중 열린 세션이 남은 계정을 모은다 (미리 채움)
containment.py      contain_account     : 계정을 잠그고, 잠금이 확인되면 (②) 세션을 종료한다 (③)
실행 파일           exercise2-2_run.py    : 요청마다 contain_account 를 호출하고, 다시 점검하고, 상태를 저장한다 (미리 채움)
```

## 실습 2-2 · 활성 세션 종료와 잔존 세션 점검하기

**이런 상황이 있습니다**

- **지금은**: <mark>계정만 잠그면 활성 세션이 잔존하고, 잔존 여부를 확인하는 점검도 없습니다</mark>.
- **만드는 것**: 세션 종료와 빈틈 점검(`session_actions.py`), 잠금 → 세션 종료를 순서대로 수행하는 통합 함수(`containment.py`), 호출 · 재점검 · 저장(`exercise2-2_run.py`).
- **실행하면**: <mark>단계 1: 수업 전부터 잠겨 있는데 세션이 열려 있던 계정, 단계 2: 잠금과 세션 종료 기록, 단계 3: 조치 후 재점검, 단계 4: 저장한 파일에서 읽은 값이 나옵니다.</mark>

**할 일**

1. 아래 코드로 파일 세 개를 만들고, `# ←` 가 있는 <mark>세 곳</mark>(① · ② · ③)을 한 줄씩 채웁니다.
2. 채우기 <mark>전과 후</mark>에 한 번씩 실행해 단계 2 · 3 을 비교합니다.

**`session_actions.py`** — 세션 종료와 점검입니다. 직접 쓰는 곳은 ① 입니다.

- `state["sessions"].get(user, [])` 는 그 계정의 세션 리스트를 꺼내고, 세션 기록이 없는 계정이면 빈 리스트 `[]` 를 꺼냅니다. 그래서 `len(…)` 이 오류 없이 0 이 됩니다. `str(before_count)` 는 「제공 파일」 레슨에서 본 대로 숫자를 글자로 바꿉니다.

```python
from containment_store import make_record                  # 기록 한 건을 만드는 함수를 불러온다


def terminate_sessions(user, state, incident_id, reason):  # 계정 · 상태 · 인시던트 번호 · 이유를 받는 함수
    """계정에 열려 있는 로그인 세션을 모두 종료하고, 조치 전과 후의 세션 수를 기록 한 건으로 리턴한다.
    계정을 잠가도 이미 로그인한 세션은 남기 때문에, 잠근 뒤에 이어서 쓴다.
    """
    before_count = len(state["sessions"].get(user, []))    # 조치 전 세션 수
    # ① state["sessions"][user] 에 빈 리스트를 저장한다 (세션을 모두 종료한다)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    after_count = len(state["sessions"].get(user, []))     # 조치 뒤 세션 수를 다시 구한다
    return make_record("세션 종료", user, incident_id, "세션 " + str(before_count) + "개", "세션 " + str(after_count) + "개", reason)  # 조치 전 · 후 세션 수와 함께 기록한다


def find_open_sessions(state):                             # 연습용 시스템 상태를 받는 함수
    """잠겨 있는데도 열린 세션이 남아 있는 계정의 리스트를 리턴한다.
    잠금만 하고 세션을 끝내지 않아 생긴 빈틈을 점검할 때 쓴다.
    """
    gaps = []                                              # 빈틈이 있는 계정을 저장할 빈 리스트
    for user in state["locked_users"]:                     # 잠긴 계정을 하나씩 꺼낸다
        open_count = len(state["sessions"].get(user, []))  # 그 계정에 열린 세션 수
        if open_count > 0:                                 # 열린 세션이 남아 있으면
            gaps.append(user)                              # 빈틈이 있는 계정으로 모은다
    return gaps                                            # 빈틈이 있는 계정 리스트를 리턴한다
```

**`containment.py`** — 잠금과 세션 종료를 한 함수에서 순서대로 수행합니다. Unit 3 응용 3-1 도 이 파일의 함수를 불러와 사용합니다. 직접 쓰는 곳은 ② · ③ 입니다.

```python
from account_actions import lock_account                              # 실습 2-1에 만든 계정 잠금 함수를 불러온다
from session_actions import terminate_sessions                        # 방금 만든 세션 종료 함수를 불러온다


def contain_account(user, state, vip_accounts, incident_id, reason):  # 계정 · 상태 · VIP 리스트 · 인시던트 번호 · 이유를 받는 함수
    """계정을 먼저 잠그고, 잠겼다고 확인되면 이어서 열린 세션을 종료한 뒤, 조치 기록 리스트를 리턴한다.
    잠금과 세션 종료를 따로 하다가 생기는 빈틈을 막고 싶을 때 쓴다.
    """
    records = []                                                      # 조치 기록을 저장할 빈 리스트
    lock_record = lock_account(user, state, vip_accounts, incident_id, reason)  # 계정을 먼저 잠그고 기록을 받는다
    records.append(lock_record)                                       # 잠금 기록을 리스트에 추가한다
    # ② lock_record 의 "after" 가 "잠김" 이면 (if, ==)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    # ③ terminate_sessions(user, state, incident_id, reason) 의 결과를 records 에 추가한다 (append)   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
    return records                                                    # 조치 기록 리스트를 리턴한다
```

**`exercise2-2_run.py`** — 직접 쓰는 곳 없이 그대로 붙여 넣습니다. 실습 2-1의 `containment_store.py` 와 `account_actions.py` 가 같은 폴더에 있어야 합니다.

```python
from incident import load_json                                                          # Unit 1 파일의 함수를 불러온다
from containment_store import new_state, save_state, load_state, reset_log, append_log  # 상태 · 기록 함수를 불러온다
from session_actions import find_open_sessions                                          # 방금 만든 세션 점검 함수를 불러온다
from containment import contain_account                                                 # 방금 만든 통합 조치 함수를 불러온다

vip_accounts = load_json("config/vip_accounts.json")                                    # VIP 계정 리스트를 읽는다
requests = [("INC-001", "dami", "퇴사한 계정의 서버 요청"), ("INC-003", "gaeun", "여러 로그 연결"), ("INC-006", "junho", "퇴사 처리 확인")]  # 조치 요청 3건 : (인시던트 번호, 계정, 이유)
state = new_state()                                                                     # 처음 상태에서 시작한다
reset_log()                                                                             # 기록 파일을 비운다

print("--- 단계 1: 점검 — 잠겼는데 세션이 열려 있는 계정")                              # 단계 1 시작을 알리는 줄
print(find_open_sessions(state))                                                        # 수업 전부터 있는 빈틈을 출력한다

print("--- 단계 2: 잠금 → 세션 종료")                                                   # 단계 2 시작을 알리는 줄
for incident_id, user, reason in requests:                                              # 요청을 하나씩 꺼낸다
    records = contain_account(user, state, vip_accounts, incident_id, reason)           # 잠금 → 세션 종료를 하고 기록 리스트를 받는다
    for record in records:                                                              # 조치 기록을 하나씩 꺼낸다
        append_log(record)                                                              # 조치 기록을 파일에 남긴다
        print(record["incident"], record["target"], "·", record["before"], "→", record["after"], "·", record["reason"])  # 기록 한 건을 출력한다

print("--- 단계 3: 조치 뒤 다시 점검")                                                  # 단계 3 시작을 알리는 줄
gaps_after = find_open_sessions(state)                                                  # 조치 뒤 다시 점검한다
print("빈틈이 남은 계정:", gaps_after)                                                  # 점검 결과를 출력한다
print("잠긴 계정:", state["locked_users"])                                              # 잠긴 계정을 출력한다

save_state(state)                                                                       # 상태를 파일에 저장한다
print("--- 단계 4: 파일에 저장된 값 다시 읽기")                                         # 단계 4 시작을 알리는 줄
print("잠긴 계정:", load_state()["locked_users"])                                       # 저장된 잠긴 계정을 출력한다
print("조치 기록:", len(load_json("containment_log.json")), "건")                       # 저장된 기록 수를 출력한다
```

- 주석 줄은 그대로 두고, **각 주석 바로 아래 줄**에 씁니다. ① · ② 는 4칸, ③ 은 ② 의 `if` 안쪽 줄이라 8칸에서 시작합니다.

**직접 쓰는 곳**

| 빈칸 | 파일 · 함수 | 쓰는 줄 | 들여쓰기 |
|---|---|---|---|
| ① | `session_actions.py` · `terminate_sessions` | 세션 리스트를 빈 리스트로 (`= []`) | 4칸 |
| ② | `containment.py` · `contain_account` | 잠금이 확인됐으면 (`if … ==`) | 4칸 |
| ③ | `containment.py` · `contain_account` | 세션 종료 기록을 더하기 (`append`) | 8칸 |

- **채우기 전에 실행하면**: 오류 없이 돌아가지만 단계 2 에 잠금 세 줄만 나오고 「세션 종료」 줄이 없습니다. 단계 3 은 `빈틈이 남은 계정: ['junho', 'dami']`, 단계 4 는 `조치 기록: 3 건` 입니다. 잠금만 하면 빈틈이 오히려 늘어난다는 것을 보여 주는 결과입니다.
- ① 확인: ① 만 채우고 실행하면 출력이 채우기 전과 **같습니다**. ① 이 들어 있는 `terminate_sessions` 를 ③ 에서 부르기 때문이니 정상입니다. 막히면: 문법 상자의 `sessions["dami"] = []` 에서 `sessions` 자리에 `state["sessions"]`, `"dami"` 자리에 `user` 를 넣습니다.
- ② 확인: ② 만 쓰고 실행하면 `IndentationError: expected an indented block after 'if' statement` 가 나옵니다. ③ 을 아직 안 써서 나는 오류이니 정상입니다. 막히면: 문법 상자의 `after == "잠김"` 에서 `after` 자리에 `lock_record["after"]` 를 넣고, 앞에 `if`, 끝에 `:` 를 붙입니다.
- ③ 확인: ③ 까지 쓰고 실행하면 단계 2 에 `INC-001 dami · 세션 2개 → 세션 0개 · 퇴사한 계정의 서버 요청` 이 나와야 합니다. `세션 2개 → 세션 2개` 면 ① 을, `gaeun` 의 세션 종료 줄이 나오면 ② 의 조건을 봅니다. 막히면: 바로 위 미리 채운 `records.append(lock_record)` 와 같은 모양이고, 괄호 안이 `terminate_sessions(user, state, incident_id, reason)` 입니다.

**순서**

1. **[VS Code]** 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 파일 이름 `session_actions.py` · `containment.py` · `exercise2-2_run.py` 를 하나씩 그대로 적어 세 개의 파일을 만듭니다. 각 파일에 이 페이지의 코드 상자를 복사해 붙여 넣고 저장합니다(`Ctrl + S`, 맥북은 `Cmd + S`).
2. **[터미널]** **채우기 전에** 한 번 실행해 단계 2 · 3 을 봅니다(맥북은 `python3`).
   ```bash
   python exercise2-2_run.py
   ```
3. **[VS Code]** `session_actions.py` 의 ①, `containment.py` 의 ② · ③ 을 씁니다. 위 「직접 쓰는 곳」의 확인과 맞춰 봅니다.
4. **[터미널]** 다시 실행합니다. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 1줄, 단계 2 는 5줄, 단계 3 은 2줄, 단계 4 는 2줄입니다. 실행하면 `containment_state.json` 과 `containment_log.json` 이 이번 실행의 결과로 바뀝니다. <mark>Unit 3 실습 3-1 이 이 두 파일을 읽으니 지우지 않습니다.</mark>
   ```bash
   python exercise2-2_run.py
   ```
5. **[보고서]** `report_u2.md` 의 `## 실습 2-2` 아래를 채웁니다.
   - (가) [핵심 질문] 실행한 출력 전체를 붙여 넣고, 단계 3 에서 빈틈이 남은 계정과 단계 4 의 잠긴 계정을 적어 주세요.
   - (나) [응용] 단계 1 에서 `junho` 가 점검에서 발견된 이유를 적어 주세요. 그리고 `dami` 가 단계 2 에서 받은 두 가지 조치와, 잠금만 했다면 유효하게 남았을 접속(세션)을 적어 주세요.
   - (다) [핵심 질문] `gaeun` 은 잠금도 세션 종료도 받지 않았습니다. `containment.py` ② 의 `if` 조건과 단계 2 의 출력 줄을 근거로 그 이유를 적어 주세요. 그리고 잠금이 적용되지 않은 계정의 세션을 종료하면 안 되는 이유도 적어 주세요.

**확인** — 단계 2 가 다섯 줄(`dami` 잠금 · 세션 종료, `gaeun` 변경 없음, `junho` 잠김 → 잠김 · 세션 종료)이고, 단계 3 이 `빈틈이 남은 계정: []`, 단계 4 가 `잠긴 계정: ['junho', 'dami']` · `조치 기록: 5 건` 이면 성공입니다. 안 나오면 「정답」 레슨의 실습 2-2 출력과 한 줄씩 맞춰 보고, 다른 줄이 있으면 위 「직접 쓰는 곳」의 확인을 다시 봅니다.

## 실습 2-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 딕셔너리에 값 저장하기 (①) | `state["sessions"][user] = []` |
| 보다 크면 | `if open_count > 0:` |
| 리스트에 추가 (③) | `records.append(terminate_sessions(...))` |
| 함수 결과를 변수에 저장하기 | `lock_record = lock_account(...)` |
| 같으면 (②) | `if lock_record["after"] == "잠김":` |
| 함수 호출만 하기 | `save_state(state)` |

---

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개와 보고서의 [핵심 질문], 글쓰기(「오늘의 글 쓰기」 세 문장 글)를 마친 뒤 합니다. 응용을 하지 않았어도 이대로 마무리합니다.

**1. 오늘 한 일 확인**

1. 계정 잠금을 실행하고 사후 검증했으며, 조치 전 · 후 상태를 감사 기록으로 남겼다 (실습 2-1)
2. 잠금 뒤 활성 세션을 종료하고, 빈틈(잔존 세션)이 남았는지 다시 점검했다 (실습 2-2)
3. 「제공 파일」 레슨의 `ip_actions.py` · `audit.py` · `approvals.py` 를 만들고 `제공 파일 정상` 을 확인했다
4. 보고서 `report_u2.md` 의 꼭 채울 칸(2-1 (가) · (다), 2-2 (가) · (다))에 `답:` 뒤가 비어 있지 않다

**2. 파일 확인** — **[터미널]** `soar_response` 폴더에서 확인합니다(맥북은 `python3`).

```bash
ls
ls config
python -c "import json; print(json.load(open('containment_state.json', encoding='utf-8'))['locked_users'], len(json.load(open('containment_log.json', encoding='utf-8'))))"
```

- `containment_store.py` · `account_actions.py` · `exercise2-1_run.py` · `session_actions.py` · `containment.py` · `exercise2-2_run.py` · `ip_actions.py` · `audit.py` · `approvals.py` · `ip_users.json` · `containment_state.json` · `containment_log.json` · `report_u2.md` 가 보여야 합니다.
- `config` 안에는 `vip_accounts.json` · `allowlist_ips.json` 이 새로 보여야 합니다.
- 마지막 줄은 <mark>`['junho', 'dami'] 5`</mark> 여야 합니다. 실습 2-2 가 저장한 상태(잠긴 계정 두 개 · 조치 기록 5건)이고, Unit 3 실습 3-1 이 이 상태에서 시작합니다.
  - 다른 값이 나오면(예: 응용 2-3 을 실습 2-2 뒤에 실행해 `['junho'] 4` 가 나옴) `python exercise2-2_run.py` 를 한 번 더 실행하고 다시 확인합니다. 응용 실행 파일도 같은 두 파일에 결과를 저장하기 때문입니다.

**3. 깃허브에 올리기**

1. **[터미널]** `security-agent-toolkit` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/security-agent-toolkit` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env`(API 키가 들어 있는 파일)나 `.venv`(내 PC 에서만 쓰는 가상환경 폴더)가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore`(깃이 올리지 않을 파일 이름을 적어 두는 파일)를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.
   - `soar_response/containment_state.json` · `soar_response/containment_log.json` 은 실습 2-2 에서 프로그램이 저장한 상태 파일입니다. 이것도 올라갑니다.
3. **[보고서]** `report_u2.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add SOAR unit 2 account lockout, session termination and provided files"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다. `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다. 그때 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다. 이 화면은 git 이 두 기록을 합친 기록에 붙일 메시지를 확인하라고 여는 편집기(vim)라서, 메시지는 고치지 않고 저장하고 닫기만 하면 됩니다.
5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `soar_response` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다. 올리기 전에 2번의 마지막 줄이 `['junho', 'dami'] 5` 인지 다시 봅니다.

**확인** — 2번 마지막 줄이 `['junho', 'dami'] 5` 이고, 깃허브의 `soar_response` 폴더에 2번에서 본 파일이 모두 보이면 성공입니다. 안 보이면 3번의 `git status` 부터 다시 합니다.

**4. 이어지는 곳**

1. 다음 Unit 3(되돌리고 티켓 남기기)의 실습 3-1 에서는 오늘 저장한 `containment_state.json` · `containment_log.json` 의 기록만 근거로 자동 조치를 **되돌립니다**(조치 전부터 잠겨 있던 `junho` 는 그대로 둡니다).
2. 실습 3-1 은 오늘 만든 `containment_store.py` · `account_actions.py` 와 제공 파일 `ip_actions.py` 를 불러 씁니다. 실습 3-2 에서는 처리할 일을 티켓으로 만들고 응답 기한을 계산합니다.

---

<!-- learn:answers -->
