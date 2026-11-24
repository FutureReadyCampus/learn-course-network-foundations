---
id: m5-u04-l04
title: 실습 4-3 · 활성 세션 종료와 잔존 세션 점검하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/122_day03_am_containment.md
  mission_id: GichanSource.m5-1111-am-containment
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 4-3 · 활성 세션 종료와 잔존 세션 점검하기

## 목표: 세션 종료와 빈틈 점검

> **오늘 들어온 일**
>
> - **상황**: 퇴사자 `dami` 의 계정을 잠갔다고 기록했는데, 잠근 후에도 `dami` 의 서버 요청이 두 건 더 들어왔습니다. 잠금 실행 전에 이미 인증을 마친 **세션**(session, 세션: 로그인한 뒤 서버가 유지하는 접속 상태)이 두 개 남아 있었기 때문입니다.
> - **문제**: 계정을 잠그면 새 로그인(인증)만 차단되고, 이미 열려 있는 세션은 계속 유효합니다. 잠금만 하고 끝내면 퇴사자가 세션이 만료될 때까지 접속할 수 있는데, 이 상태를 점검하는 절차가 없습니다.
> - **부탁**: 계정을 잠근 후에는 열린 세션도 모두 종료해 주세요. 그리고 잠겼는데 활성 세션이 남은 계정이 있는지 점검하는 기능도 만들어 주세요.
> - **바뀌는 점**: 잠금과 세션 종료가 함께 실행되고, 조치가 누락된 계정은 점검에서 즉시 탐지됩니다. 오늘 샘플에서는 이미 잠겨 있는데 세션 하나가 열려 있는 `junho` 가 점검에서 발견됩니다. 상황은 설명을 위한 예시입니다.

## 3.1 계정 잠금은 새 로그인을 차단하고, 세션 종료는 이미 열린 접속을 종료한다

**세션**(session, 세션: 로그인한 뒤 서버가 유지하는 접속 상태)이 유효하면 서버는 비밀번호를 다시 요구하지 않습니다. 따라서 계정을 잠가도 이미 발급된 세션은 계속 사용할 수 있습니다. 예를 들어 아침에 로그인해 둔 `dami` 의 세션 `S-101` 은 계정을 잠근 후에도 서버에 요청을 보낼 수 있습니다. 세션은 서버 쪽에서 무효화(invalidate, 인밸리데이트: 그 세션을 더는 인증에 쓸 수 없게 만드는 일)해야 종료되므로, 잠금 뒤에 세션 종료 조치가 따로 필요합니다. 조치 순서도 중요합니다.

| 순서 | 결과 |
|---|---|
| 잠금 → 세션 종료 (오늘 구현) | 새 로그인이 이미 차단되어 있어서, 세션을 종료하면 더는 접속할 수 없다 |
| 세션 종료 → 잠금 | 두 조치 사이에 재로그인(re-login)이 가능해 새 세션이 생길 수 있다 |
| 잠금만 | 활성 세션으로 계속 접속할 수 있다 |

- 이 표는 오늘 연습용 시스템의 동작 규칙입니다. 실제 서비스는 시스템마다 동작이 다르므로, 계정을 잠글 때 세션이 어떻게 처리되는지 먼저 확인해야 합니다.
- 따라서 세션 종료는 **잠금이 사후 검증으로 확인된 뒤에만** 실행합니다. 잠금이 적용되지 않았거나 VIP 정책으로 차단된 계정의 세션은 종료하면 안 됩니다.
- 수업 시작 상태에서 `junho` 는 이미 잠겨 있지만 세션이 하나 열려 있습니다. 이처럼 계정은 잠겼는데 활성 세션이 잔존(residual, 레지듀얼: 조치 후에도 남아 있음)하는 상태를 이 문서에서는 **빈틈**이라 부릅니다(출력에도 「빈틈」으로 표시됩니다). 이 빈틈을 찾아내는 점검이 `find_open_sessions` 입니다.

함수는 두 파일에 나뉘어 있고, 직접 쓰는 곳은 **아홉 군데**입니다.

```
session_actions.py  terminate_sessions  : 계정의 세션 리스트를 비운다 (1번)
                    find_open_sessions  : 잠긴 계정 중 열린 세션이 남은 계정을 모은다 (2 · 3번)
containment.py      contain_account     : 계정을 잠그고 (4번), 잠금이 확인되면 (5번) 세션을 종료한다 (6번)
실행 파일           exercise4-3_run.py    : 요청마다 contain_account 를 호출하고 (7번), 다시 점검하고 (8번), 상태를 저장한다 (9번)
```

## 실습 4-3 · 활성 세션 종료와 잔존 세션 점검하기

**이런 상황이 있습니다**

- **지금은**: <mark>계정만 잠그면 활성 세션이 잔존하고, 잔존 여부를 확인하는 점검도 없습니다</mark>.
- **만드는 것**: 세션 종료와 빈틈 점검(`session_actions.py`), 잠금 → 세션 종료를 순서대로 수행하는 통합 함수(`containment.py`), 호출 · 재점검 · 저장(`exercise4-3_run.py`).
- **실행하면**: <mark>단계 1: 수업 전부터 잠겨 있는데 세션이 열려 있던 계정, 단계 2: 잠금과 세션 종료 기록, 단계 3: 조치 후 재점검, 단계 4: 저장한 파일에서 읽은 값이 나옵니다.</mark>

**할 일**: 파일 세 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 1 ~ 3 을 읽습니다.

**`session_actions.py`** — 세션 종료와 점검입니다. 직접 쓰는 곳은 1 ~ 3번입니다.

```python
from containment_store import make_record  # 기록 한 건을 만드는 함수를 불러온다


def terminate_sessions(user, state, incident_id, reason):  # 계정 · 상태 · 인시던트 번호 · 이유를 받는 함수
    """계정에 열려 있는 로그인 세션을 모두 종료하고, 조치 전과 후의 세션 수를 기록 한 건으로 리턴한다.
    계정을 잠가도 이미 로그인한 세션은 남기 때문에, 잠근 뒤에 이어서 쓴다.
    """
    before_count = len(state["sessions"].get(user, []))  # 조치 전 세션 수 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. state["sessions"][user] 에 빈 리스트를 저장한다 (세션을 모두 종료한다)
    after_count = len(state["sessions"].get(user, []))  # 조치 뒤 세션 수를 다시 구한다 — 미리 채운 줄
    return make_record(
        "세션 종료",
        user,
        incident_id,
        "세션 " + str(before_count) + "개",
        "세션 " + str(after_count) + "개",
        reason,
    )  # 조치 전 · 후 세션 수와 함께 기록한다 — 미리 채운 줄


def find_open_sessions(state):  # 연습용 시스템 상태를 받는 함수
    """잠겨 있는데도 열린 세션이 남아 있는 계정의 리스트를 리턴한다.
    잠금만 하고 세션을 끝내지 않아 생긴 빈틈을 점검할 때 쓴다.
    """
    gaps = []  # 빈틈이 있는 계정을 저장할 빈 리스트
    for user in state["locked_users"]:  # 잠긴 계정을 하나씩 꺼낸다
        open_count = len(state["sessions"].get(user, []))  # 그 계정에 열린 세션 수 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 2. open_count 가 0 보다 크면 (if, >)
        # 3.   gaps 에 user 를 추가한다 (append)
    return gaps  # 빈틈이 있는 계정 리스트를 리턴한다
```
**`containment.py`** — 잠금과 세션 종료를 한 함수에서 순서대로 수행합니다. Unit 5에서도 이 파일의 함수를 불러와 사용합니다. 직접 쓰는 곳은 4 ~ 6번입니다.

```python
from account_actions import lock_account  # 실습 4-1에 만든 계정 잠금 함수를 불러온다
from session_actions import terminate_sessions  # 방금 만든 세션 종료 함수를 불러온다


def contain_account(user, state, vip_accounts, incident_id, reason):  # 계정 · 상태 · VIP 리스트 · 인시던트 번호 · 이유를 받는 함수
    """계정을 먼저 잠그고, 잠겼다고 확인되면 이어서 열린 세션을 종료한 뒤, 조치 기록 리스트를 리턴한다.
    잠금과 세션 종료를 따로 하다가 생기는 빈틈을 막고 싶을 때 쓴다.
    """
    records = []  # 조치 기록을 저장할 빈 리스트
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. lock_account(user, state, vip_accounts, incident_id, reason) 의 결과를 lock_record 에 저장한다
    records.append(lock_record)  # 잠금 기록을 리스트에 추가한다 — 미리 채운 줄
    # 5. lock_record 의 "after" 가 "잠김" 이면 (if, ==)
    # 6.   terminate_sessions(user, state, incident_id, reason) 의 결과를 records 에 추가한다 (append)
    return records  # 조치 기록 리스트를 리턴한다
```
**`exercise4-3_run.py`** — 7 ~ 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 실습 4-1의 `containment_store.py` 와 `account_actions.py` 가 같은 폴더에 있어야 합니다.

```python
from incident import load_json  # Unit 1 파일의 함수를 불러온다
from containment_store import new_state, save_state, load_state, reset_log, append_log  # 상태 · 기록 함수를 불러온다
from session_actions import find_open_sessions  # 방금 만든 세션 점검 함수를 불러온다
from containment import contain_account  # 방금 만든 통합 조치 함수를 불러온다

vip_accounts = load_json("config/vip_accounts.json")  # VIP 계정 리스트를 읽는다
requests = [
    ("INC-001", "dami", "퇴사한 계정의 서버 요청"),
    ("INC-003", "gaeun", "여러 로그 연결"),
    ("INC-006", "junho", "퇴사 처리 확인"),
]  # 조치 요청 3건 : (인시던트 번호, 계정, 이유)
state = new_state()  # 처음 상태에서 시작한다
reset_log()  # 기록 파일을 비운다

print("--- 단계 1: 점검 — 잠겼는데 세션이 열려 있는 계정")  # 단계 1 시작을 알리는 줄
print(find_open_sessions(state))  # 수업 전부터 있는 빈틈을 출력한다

print("--- 단계 2: 잠금 → 세션 종료")  # 단계 2 시작을 알리는 줄
for incident_id, user, reason in requests:  # 요청을 하나씩 꺼낸다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. contain_account(user, state, vip_accounts, incident_id, reason) 의 결과를 records 에 저장한다
    for record in records:  # 조치 기록을 하나씩 꺼낸다
        append_log(record)  # 조치 기록을 파일에 남긴다
        print(record["incident"], record["target"], "·", record["before"], "→", record["after"], "·", record["reason"])  # 기록 한 건을 출력한다

print("--- 단계 3: 조치 뒤 다시 점검")  # 단계 3 시작을 알리는 줄
# ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
# 8. find_open_sessions(state) 의 결과를 gaps_after 에 저장한다
print("빈틈이 남은 계정:", gaps_after)  # 점검 결과를 출력한다
print("잠긴 계정:", state["locked_users"])  # 잠긴 계정을 출력한다

# 9. save_state(state) 를 호출한다 (상태를 파일에 저장한다)
print("--- 단계 4: 파일에 저장된 값 다시 읽기")  # 단계 4 시작을 알리는 줄
print("잠긴 계정:", load_state()["locked_users"])  # 저장된 잠긴 계정을 출력한다
print("조치 기록:", len(load_json("containment_log.json")), "건")  # 저장된 기록 수를 출력한다
```
**순서**

1. **[VS Code]** 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 파일 이름 `session_actions.py` · `containment.py` · `exercise4-3_run.py` 을(를) 하나씩 그대로 적어 세 개의 파일을 만듭니다. 각 파일에 이 페이지의 코드 상자를 복사해 붙여 넣고 저장합니다(`Ctrl + S`, 맥북은 `Cmd + S`).
2. **[VS Code]** `session_actions.py` 1 ~ 3번, `containment.py` 4 ~ 6번, `exercise4-3_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「실습 4-3 정리」를 봅니다.
3. **[터미널]** 실행합니다(맥북은 `python3`).
   ```bash
   python exercise4-3_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 1줄, 단계 2 는 5줄, 단계 3 은 2줄, 단계 4 는 2줄입니다.
5. **[실습 결과 기록]** `report_u4.md` 의 `## 실습 4-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 단계 3 에서 빈틈이 남은 계정과 단계 4 의 잠긴 계정을 적어 주세요.
   - (나) [핵심 질문] 단계 1 에서 `junho` 가 점검에서 발견된 이유를 적어 주세요. 그리고 `dami` 가 단계 2 에서 받은 두 가지 조치와, 잠금만 했다면 유효하게 남았을 접속(세션)을 적어 주세요.
   - (다) [핵심 질문] `gaeun` 은 잠금도 세션 종료도 받지 않았습니다. `containment.py` 5번의 `if` 조건과 단계 2 의 출력 줄을 근거로 그 이유를 적어 주세요. 그리고 잠금이 적용되지 않은 계정의 세션을 종료하면 안 되는 이유도 적어 주세요.

## 실습 4-3 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 딕셔너리에 값 저장하기 | `state["sessions"][user] = []` |
| 보다 크면 | `if open_count > 0:` |
| 리스트에 추가 | `gaps.append(user)` |
| 함수 결과를 변수에 저장하기 | `lock_record = lock_account(...)` |
| 같으면 | `if lock_record["after"] == "잠김":` |
| 함수 호출만 하기 | `save_state(state)` |

<!-- answer: 05|실습 4-3 정답 -->

---

## 문제 해결 기록 남기기

이번 Unit에서는 계정 잠금과 IP 차단을 실행하고, 상태를 다시 확인한 뒤, 계정에 남아 있는 세션까지 종료했습니다. 실습 결과 기록에 적은 출력과 근거를 바탕으로 GitHub 블로그에 어떤 정책을 확인했고, 조치 전후에 무엇이 달라졌는지 남깁니다. 블로그와 GitHub Pages를 처음 설정한다면 [M3 Unit 1의 Jekyll 및 GitHub Pages 설정](__SITE__/exercises/module/3/unit/1/lesson/1/page/4)을 먼저 진행하세요. 이미 설정했다면 `network-study-notes` 저장소의 `_posts` 폴더에 `YYYY-MM-DD-m5-u4-containment.md` 형식의 글을 만듭니다.

기록에는 다음 내용을 담습니다.

- **계정 잠금의 근거:** VIP 계정이 제외된 이유, 이미 잠긴 계정의 `before` 값, 잠금 뒤 사후 검증이 필요한 이유
- **IP 차단의 영향 범위:** 허용 목록과 공유 IP를 확인한 결과, 실제 차단한 IP와 120분 뒤 만료된 시점
- **세션 종료의 순서:** 잠금이 확인된 뒤 세션을 종료한 이유, `junho`에게 남아 있던 세션 빈틈을 확인한 방법
- **남은 한계와 다음 확인:** 연습용 상태에서 확인한 사실과 실제 서비스에서 추가로 확인해야 할 항목

실습 출력으로 확인한 사실과 추정한 설명을 구분합니다. 차단이나 세션 종료가 막은 문제와 정책이 보호한 계정을 함께 적습니다. 글을 저장하고 `network-study-notes` 저장소에 커밋한 뒤 `git push` 합니다. GitHub Pages에서 게시된 글과 링크를 확인하세요.

M5 Unit 5에서는 감사 기록을 근거로 실행한 조치를 롤백하고, 여러 알림의 처리 결과를 한 흐름으로 묶습니다.

---

<!-- learn:answers -->
