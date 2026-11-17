---
id: m3-u08-l03
title: 3교시 (11:00–11:50) · 승인이 필요한 회수 계획 가려내기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/090_day05_am_revoke.md
  mission_id: GichanSource.m3-1030-am-revoke
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 3교시 (11:00–11:50) · 승인이 필요한 회수 계획 가려내기

## 3교시 (11:00–11:50) · 승인이 필요한 회수 계획 가려내기

> 📨 **오늘 들어온 일**
>
> A사 관제 담당이 보낸 메시지:
> 「회수할 8건 가운데에는 데이터를 바꾸는 쓰기 권한(`CHANGE`)도 있습니다. 쓰기 권한은 잘못 없애면 영향이 크니 보안 책임자의 승인을 받고 회수하고 싶습니다. 조회 같은 일반 권한 한 건은 바로 회수해도 됩니다.
>
> 다만 퇴사한 사람의 역할을 비우면 그 사람이 역할로 받던 권한이 모두 없어집니다. 이렇게 권한이 2개 이상 사라지는 회수는 조회 권한이어도 승인을 받아 주세요. 8건 가운데 어느 것이 승인 대상인지 가려서, 계획마다 승인 상태를 적어 주세요. 보안 책임자가 승인한 것과 아직 기다리는 것도 구분해 주세요.」
> - **왜 중요한가**: 중요한 권한을 한 사람이 혼자 정하면 실수나 부정이 생길 수 있습니다. 승인 상태가 적혀 있으면 어느 회수가 승인을 받았고 어느 회수가 아직 기다리는지 바로 알 수 있습니다.

> 📖 **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「✍️ 문제」 전까지는 이 교시의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 📖 왜 필요한가

> 📖 **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 2교시의 계획은 8건 모두 같은 방식으로 다룹니다. 하지만 권한마다 중요도가 다릅니다. 데이터를 바꾸는 권한(`CHANGE`)은 잘못 없애면 그 권한으로 일하던 사람의 업무가 멈추고 실제 서비스에서는 되돌리기도 어렵습니다.
2. 그래서 승인이 필요한 경우를 둘로 정합니다. ① **민감한 권한**(sensitive · 센서티브, 잘못 없애면 피해가 큰 권한)이다 ② 한 번의 회수로 권한이 2개 이상 사라지는 경우(영향 2건 이상)다. 예를 들어 퇴사한 dami 의 역할을 비우면 dami 가 그 역할로 받던 권한 2개가 모두 없어진다. 이 경우에는 보안 책임자의 승인을 받고, 그 밖의 일반 권한 한 건은 바로 회수합니다.
3. 이 교시에서는 계획마다 승인이 필요한지, 필요하다면 승인됐는지를 **승인 상태**로 적습니다. 실제로 지우는 일은 4교시에서 합니다.

## 📖 3.1 승인이 필요한 경우와 승인 상태

> 📖 **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

- 승인이 필요한 계획은 둘 중 하나입니다.
  - ① `config/sensitive.json` 에 적힌 민감한 권한: junho 의 `SALES:CHANGE`(예외 2번), dami 의 `SALES:CHANGE`(역할 해제) 두 건입니다.
  - ② 영향(`impact`)이 2건 이상: dami 의 역할 해제 두 건(영향 2건)입니다.
  - 겹치는 것을 한 번만 세면 승인이 필요한 계획은 모두 3건입니다.
- 민감한 권한 리스트는 「자원:행위」 문자열의 리스트입니다.
  - 쓰기 권한인 `SALES:CHANGE` · `ACCOUNT:CHANGE` · `SETTLE:CHANGE` 세 개를 적었습니다.
  - `QUERY` 는 조회, `CHANGE` 는 변경(쓰기)입니다.
- 예외 1 · 2 · 4 · 5번은 만료 시각이 이미 지났습니다(어제 점검 결과에 「만료된 예외」로 나왔습니다).
  - 접근은 이미 막혀 있지만 예외 기록이 남아 있어서 회수 대상입니다.
  - 3번은 아직 유효하지만 dami 가 퇴사해서 쓸 수 없습니다.
- 승인 요청서는 따로 만들지 않고, 계획 한 건마다 `approval` 키에 **승인 상태**를 적습니다. 값은 아래 세 가지 중 하나입니다.

| `approval` 값 | 뜻 |
|---|---|
| `승인 불필요` | 승인 없이 바로 회수할 수 있는 계획 |
| `승인됨` | 승인이 필요한데 보안 책임자가 승인함 |
| `승인 대기` | 승인이 필요한데 아직 결정이 없음 |

- 보안 책임자가 승인할지는 사람이 정하고, 그 결정은 `decisions` 딕셔너리로 주어집니다.
  - 예: `{"dami:SALES:QUERY": "승인"}` 처럼 키는 「사용자:권한」 문자열입니다. 여기에 없는 계획은 아직 결정하지 않은 것입니다.
  - dami 의 `SALES:QUERY` 계획은 둘(역할 해제, 예외 3번 삭제)이지만 결정 키 `dami:SALES:QUERY` 는 같습니다.
  - 이 키는 승인이 필요한 계획에서만 찾는데, 오늘은 역할 해제 쪽만 승인이 필요합니다.
- **직접 쓰는 곳은 세 함수**입니다. 판단이 필요한 함수마다 1 ~ 6줄만 쓰고, 나머지는 미리 채웠습니다.
  - `plan_key`(1번): 계획에서 「사용자:권한」 문자열을 만듭니다(승인 결정을 찾는 키).
  - `needs_approval`(2 ~ 4번): 민감한 권한이거나 영향이 2건 이상이면 `True` 를 리턴합니다.
  - `mark_approvals`(5 ~ 10번): 계획마다 승인 상태(`approval`)를 정합니다.
- **미리 채운 함수**
  - `load_sensitive`: 민감한 권한 파일을 읽습니다(판단이 없는 읽기라 미리 채움).

```
+---------------------------------------------+
| mark_approvals(plans, sensitive, decisions) |
+---------------------------------------------+
   |
   v
+---------------------------------------+
| results = []  (결과를 담을 빈 리스트) |
+---------------------------------------+
   |
   v
+------------------------------------------+
| 계획을 하나씩 꺼내 복사본(item)을 만든다 |
+------------------------------------------+
   |
   v
+--------------------------------------------------------------------------+
| 승인이 필요한가? (needs_approval: 민감한 권한이거나 영향이 2건 이상인가) |
+--------------------------------------------------------------------------+
   |
   +--> 아니다 --> item["approval"] = "승인 불필요" --> 아래 「results 에 추가한다」로
   |
   v  그렇다
+-----------------------------------------------+
| 보안 책임자의 결정(decisions)이 「승인」인가? |
+-----------------------------------------------+
   |
   +--> 그렇다 --> item["approval"] = "승인됨" --> 아래 「results 에 추가한다」로
   |
   +--> 아니다 --> item["approval"] = "승인 대기" --> 아래 「results 에 추가한다」로
   |
   v
+--------------------------------------------------+
| item 을 results 에 추가하고 다음 계획으로 (반복) |
+--------------------------------------------------+
   |
   v  모든 계획을 꺼낸 뒤
results 를 리턴한다
```

> ✍️ **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## ✍️ 문제 3-1 · 승인이 필요한 회수 계획 가려내고 승인 상태 적기

**📍 이런 상황이 있습니다**

- **지금은**: 2교시의 계획 8건이 모두 같은 리스트에 섞여 있습니다. 쓰기 권한처럼 승인이 필요한 것과 바로 회수해도 되는 것을 담당자가 눈으로 가려야 합니다.
- **그래서 만드는 것**: `mark_approvals` 입니다.
  - 승인이 필요 없는 계획은 「승인 불필요」, 승인이 필요하고 보안 책임자가 승인하기로 한 계획은 「승인됨」, 승인이 필요한데 아직 결정이 없는 계획은 「승인 대기」로 `approval` 키에 적습니다.
- **실행하면**: 단계 1은 계획 8건의 승인 상태를 출력하고, 단계 2는 승인 상태별 건수를 출력합니다.
- **현업에서는**: 접근 관리 도구도 중요한 권한의 변경은 승인자를 거치고, 승인 여부를 기록으로 남깁니다.

**🎯 할 일**

1. `config/sensitive.json` · `revoke_approve.py` · `day05_3-1_run.py` 세 파일을 만들고, `plan_key` · `needs_approval` · `mark_approvals` 에서 직접 쓰는 곳 세 군데를 씁니다.
2. 실행해서 <mark>승인 상태</mark>(단계 1: 승인 상태)와 <mark>승인 상태별 건수</mark>(단계 2: 집계)를 읽습니다.

**`config/sensitive.json`** — 그대로 붙여 넣습니다. 민감한 권한 리스트입니다. `access_control` 안의 `config` 폴더에 만듭니다.

```json
["SALES:CHANGE", "ACCOUNT:CHANGE", "SETTLE:CHANGE"]
```

**`revoke_approve.py`**

```python
from config_loader import load_json                              # 10/22(목)에 만든 안전한 읽기 함수를 불러온다


def load_sensitive(path):                                        # 민감한 권한 파일 경로를 받는 함수
    """민감한 권한 파일을 읽어 「자원:행위」 리스트로 리턴하고, 없거나 깨졌으면 빈 리스트를 리턴한다.
    승인이 필요한 회수를 가릴 때 쓴다.
    """
    return load_json(path, [])                                   # 안전하게 읽어 그대로 리턴한다


def plan_key(plan):                                              # 계획 한 건을 받는 함수
    """「사용자:권한」 문자열(예: "dami:SALES:CHANGE")을 리턴한다.
    계획에 맞는 승인 결정을 찾는 키로 쓴다.
    """
    user = plan["user"]                                          # 계획의 사용자
    permission = plan["permission"]                              # 계획의 권한
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. f"{user}:{permission}" 을 리턴한다 (사용자와 권한을 : 로 이어 붙인 문자열)


def needs_approval(plan, sensitive):                             # 계획 한 건과 민감한 권한 리스트를 받는 함수
    """민감한 권한이거나 영향이 2개 이상이면 True, 아니면 False 를 리턴한다.
    승인이 필요한 회수를 가려낼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. plan["permission"] 이 sensitive 안에 있는지(in)를 is_sensitive 에 담는다
    # 3. plan["impact"] 가 2 이상인지(>=)를 is_big_impact 에 담는다
    # 4. is_sensitive 이거나 is_big_impact 이면 True 가 되도록 리턴한다 (or)


def mark_approvals(plans, sensitive, decisions):                 # 계획 리스트 · 민감한 권한 리스트 · 승인 결정 딕셔너리를 받는 함수
    """계획마다 "approval" 키(승인 불필요 · 승인됨 · 승인 대기)를 적은 복사본 리스트를 리턴한다.
    어떤 회수가 보안 책임자의 승인을 기다려야 하는지 가를 때 쓴다.
    """
    results = []                                                 # 결과를 담을 빈 리스트
    for plan in plans:                                           # 계획을 하나씩 꺼낸다
        item = plan.copy()                                       # 원래 계획은 바꾸지 않고 복사한다
        key = plan_key(plan)                                     # 승인 결정을 찾는 「사용자:권한」 문자열을 만든다
        decision = decisions.get(key)                            # 보안 책임자의 결정을 꺼낸다(결정이 없으면 None)
        needs = needs_approval(plan, sensitive)                  # 승인이 필요한 계획인지 알아본다(True 또는 False)
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. needs 가 거짓이면 (not)
        # 6.   item["approval"] 을 "승인 불필요" 로 정한다
        # 7. 그렇지 않고 decision 이 "승인" 이면 (elif)
        # 8.   item["approval"] 을 "승인됨" 으로 정한다
        # 9. 그렇지 않으면 (else)
        # 10.  item["approval"] 을 "승인 대기" 로 정한다
        results.append(item)                                     # 승인 상태를 적은 복사본을 결과 리스트에 추가한다
    return results                                               # 결과 리스트를 리턴한다

```

- 직접 쓰는 곳은 세 함수이고, 모두 함수 안이라 앞에 공백 4개를 기본으로 넣습니다(Tab 키 한 번).
  - `plan_key` · `needs_approval` 안: 1 ~ 4번은 모두 4개입니다.
  - `mark_approvals` 안: 미리 채운 `for` 안쪽이라 `if` · `elif` · `else` 는 8개이고, 그 안쪽 `item["approval"] = …` 는 4개 더(12개)입니다. 위의 `key` · `decision` · `needs` 는 미리 채운 줄입니다.
  - 나머지 줄은 미리 채워 두었으니 그대로 둡니다.
- 5번의 `not needs` 는 「승인이 필요하지 않으면」입니다(`needs` 는 승인이 필요한지의 참 · 거짓). `not` 은 참과 거짓을 뒤집습니다.
- 채우기 전에 실행하면 `KeyError: 'approval'` 오류가 납니다. 승인 상태(`approval`)를 아직 적지 않았기 때문입니다.

**`day05_3-1_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 2교시의 계획을 만든 뒤 `mark_approvals` 로 승인 상태를 정하고 두 단계로 출력합니다.

```python
from rbac import USERS, ROLES                                    # 10/21(수)에 만든 사용자 · 역할 딕셔너리를 불러온다
from revoke_input import load_to_revoke                          # 어제 점검 결과(회수 대상)를 만드는 함수를 불러온다
from revoke_plan import plan_revocation                          # 2교시에 만든 회수 계획 함수를 불러온다
from revoke_approve import load_sensitive, mark_approvals        # 방금 만든 승인 함수를 불러온다

DECISIONS = {"dami:SALES:QUERY": "승인", "dami:SALES:CHANGE": "승인"}  # 보안 책임자의 결정. 여기 없는 계획은 아직 결정하지 않은 것이다

to_revoke = load_to_revoke()                                     # 어제 점검한 회수 대상을 만든다
plans = plan_revocation(to_revoke, USERS, ROLES)                 # 2교시와 같은 방법으로 회수 계획을 세운다
sensitive = load_sensitive("config/sensitive.json")              # 민감한 권한 리스트를 읽는다
results = mark_approvals(plans, sensitive, DECISIONS)            # 계획마다 승인 상태를 적는다

print("--- 단계 1: 승인 상태 - 계획 8건")                        # 단계 1 시작을 알리는 줄
for item in results:                                             # 결과를 하나씩 꺼낸다
    print(item["user"], item["permission"], "<-", item["source"], "|", item["method"], "| 영향", item["impact"], "건 |", item["approval"])  # 사용자 · 권한 <- 출처 | 방법 | 영향 | 승인 상태를 출력한다

print("--- 단계 2: 집계 - 승인 상태별 건수")                     # 단계 2 시작을 알리는 줄
counts = {}                                                      # 승인 상태 → 건수를 담을 빈 딕셔너리
for item in results:                                             # 결과를 하나씩 꺼낸다
    count_key = item["approval"]                                 # 세는 기준이 되는 키
    old_count = counts.get(count_key, 0)                         # 그 키의 지금까지 센 수(처음이면 0)
    counts[count_key] = old_count + 1                            # 1 늘려서 다시 적는다
print(counts)                                                    # 승인 상태별 건수를 출력한다
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `config/sensitive.json` · `revoke_approve.py` · `day05_3-1_run.py` 를 만들어 위 코드를 붙여 넣습니다. 만드는 법은 둘 중 하나를 고릅니다.
   - VS Code: `access_control` 폴더를 선택하고 **새 파일**(New File) 아이콘을 눌러 이름을 입력합니다(`config/…` 이름은 이 폴더를 선택한 채 입력하면 `config` 폴더 안에 만들어집니다).
   - 터미널: `pwd` 로 `access_control` 인지 확인하고 `touch 이름` 으로 만든 뒤 VS Code 에서 열어 붙여 넣습니다(`vim 이름` → `i` → 붙여넣기 → `Esc` → `:wq` 도 됩니다).
2. **[터미널]** `ls config` 로 `sensitive.json` 이 `users.json` 과 같은 `config` 폴더에 있는지 보고, `python -m json.tool config/sensitive.json`(맥북은 `python3`)로 내용이 정상인지 확인합니다.
   - 깨진 채 두면 민감한 권한 리스트를 읽지 못해 junho 의 `SALES:CHANGE` 가 「승인 불필요」로 나오고, 승인이 필요한 계획이 3건에서 2건으로 줄어듭니다.
3. **[VS Code]** `revoke_approve.py` 에서 `plan_key` · `needs_approval` · `mark_approvals` 에서 직접 쓰는 곳 세 군데를 씁니다. 3.1 의 표와 그림을 보고 씁니다.
4. **[터미널]** `pwd` 의 결과가 `access_control` 로 끝나는지 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python day05_3-1_run.py
   ```
5. 출력은 두 단계입니다. 단계 1은 `계획 8건` 제목 줄과 계획 여덟 줄(줄마다 승인 상태), 단계 2는 승인 상태별 건수 딕셔너리 한 줄입니다.
6. **[보고서]** `day05_am_report.md` 의 `## 3교시` › `### 문제 3-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 「승인 불필요」 · 「승인됨」 · 「승인 대기」가 각각 몇 건인지, 승인 대기인 계획이 무엇인지 적어 주세요.
   - (나) 🔍 권한을 없애는 일인데 왜 쓰기 권한 같은 민감한 권한은 승인을 받게 할까요? 조회 같은 일반 권한 한 건은 바로 회수해도 되는 이유도 적어 주세요.
   - (다) 🔍 junho 의 `SALES:CHANGE`(예외 2번) 계획은 승인 대기입니다. 4교시에서 이 계획은 어떻게 처리될지 예상해서 적고, 승인이 오래 나지 않으면 어떤 문제가 생길지도 적어 주세요.

## 3교시 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 결정을 찾는 키 | `return f"{user}:{permission}"` (`plan_key` 안) |
| 승인이 필요한지 | `is_sensitive = plan["permission"] in sensitive` · `is_big_impact = plan["impact"] >= 2` → `return is_sensitive or is_big_impact` (`needs_approval` 안) |
| 승인이 필요 없을 때 | `if not needs:` → `item["approval"] = "승인 불필요"` |
| 결정이 「승인」인지 | `elif decision == "승인":` → `item["approval"] = "승인됨"` |
| 그 밖(결정 없음) | `else:` → `item["approval"] = "승인 대기"` |

---
