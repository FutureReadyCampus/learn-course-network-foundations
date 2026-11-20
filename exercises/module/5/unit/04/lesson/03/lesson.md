---
id: m5-u04-l03
title: 실습 4-2 · 오탐 신고 처리와 롤백 확인
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/130_day05_am_report_gate.md
  mission_id: GichanSource.m5-1113-am-report-gate
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 4-2 · 오탐 신고 처리와 롤백 확인

## 목표: 오탐 대응 절차

> **오늘 들어온 일**
>
> - **상황**: <mark style="background:#e0d4ff">Unit 3 실습 3-1 에서 자동 조치를 원래 상태로 복원(롤백, rollback)하는 `rollback_incident` 를 만들었습니다.</mark> 오늘은 **오탐**(false positive, 폴스 포지티브: 정상 활동을 공격으로 잘못 판정한 것) 신고가 2건 들어왔습니다.
> - `INC-301`: 해외 IP 에서 로그인한 `jiwoo` 계정을 자동으로 잠그고 세션(session, 세션: 로그인한 뒤 서버가 유지하는 접속 상태)을 종료했는데, 영업팀장이 「출장 중이고 출장 등록도 했다」고 알려 왔습니다.
> - `INC-202`: 경로 스캔(서버의 여러 주소에 차례로 요청을 보내 약점을 찾는 일)으로 자동 차단한 IP `198.51.100.90` 이 회사가 계약한 점검 업체의 스캐너라고 인프라팀이 알려 왔습니다.
> - **문제**: 롤백 함수만 실행하면 오탐 대응이 끝나지 않습니다.
> - <mark style="background:#ffc4d6">영향 확인(impact assessment: 조치가 실제로 바꾼 대상을 파악하는 일)을 먼저 하지 않으면</mark> 누가 영향을 받았는지 알 수 없습니다. 신고와 상관없는 진짜 공격(정탐, true positive: 실제 공격을 정확히 탐지한 것)인 `dami` 잠금(`INC-201`)이 그대로인지도 따로 확인하기 어렵습니다.
> - 롤백한 뒤 복구 확인(recovery verification: 실제 상태가 복원됐는지 다시 점검하는 일)을 하지 않으면 해제되지 않은 계정이 남아도 알 수 없습니다. 그러면 `jiwoo` 가 계속 로그인하지 못할 수 있습니다.
> - 탐지 규칙을 조정하지 않으면 다음 출장 때도 같은 오탐 알림이 생깁니다.
> - **부탁**: 오탐 신고마다 영향 확인 → 롤백 → 복구 확인 순서로 처리하고, 신고를 접수한 뒤 <mark style="background:#ffdcb0">30분 이내</mark>에 복구했는지도 기록해 주세요. 마지막으로 담당자가 검토할 규칙 조정(튜닝, tuning: 같은 오탐이 반복되지 않도록 탐지 규칙이나 허용 목록을 고치는 일) 제안을 남겨 주세요.
> - **바뀌는 점**: 두 신고가 <mark style="background:#bde3ff">25분 · 5분</mark> 만에 복구됩니다. 롤백한 뒤에도 잠겨 있거나 차단된 대상은 <mark style="background:#bde3ff">0개</mark>입니다. <mark style="background:#ffc4d6">`jiwoo` 의 세션은 되돌릴 수 없는 조치(비가역, irreversible)라 「되돌리기 불가」로 따로 남습니다.</mark> 그래서 `jiwoo` 가 다시 로그인해야 합니다. `dami` 는 그대로 잠겨 있습니다. 상황과 이름은 설명을 위한 예시입니다.

## 3.1 오탐 대응의 네 단계

| 순서 | 하는 일 | 오늘 쓰는 함수 |
|---|---|---|
| 1. 영향 확인 | 그 인시던트의 기록 가운데 조치 전(`before`)과 조치 후(`after`)가 다른 기록만 찾는다 | `list_changes` (1 · 2번) |
| 2. 되돌리기 | 자동 조치가 바꾼 것만 조치 이전 상태로 롤백한다 | <mark style="background:#e0d4ff">Unit 3 함수 `rollback_incident`</mark> (7번) |
| 3. 복구 확인 | 롤백한 뒤에도 잠겨 있는 계정 · 차단된 IP 가 남았는지 점검한다 | `find_not_recovered` (3 · 4번) |
| 4. 규칙 조정 제안 | IP 차단이었으면 허용 목록 추가 검토, 계정이었으면 탐지 규칙 예외(exception) 검토를 담당자에게 제안한다 | `make_tuning_note` (5 · 6번) |

- <mark style="background:#e0d4ff">Module 4 Unit 4 실습 4-2 에서는 예외 규칙으로 탐지 규칙을 고쳐(튜닝) 오탐 알림을 줄였습니다.</mark> 오늘은 오탐 때문에 **이미 실행된 자동 조치**를 원래 상태로 복원(롤백)하는 일입니다.
- `INC-301` 에는 IP `198.51.100.120` 의 차단 기록도 있지만 `before` 와 `after` 가 모두 <mark style="background:#bde3ff">「변경 없음」</mark>입니다. 바뀐 것이 없으므로 영향 확인 대상에서 제외합니다.
- `rollback_incident` 는 신고된 인시던트의 기록만 롤백합니다. 같은 기록 파일에 있는 `INC-201`(`dami`)은 <mark style="background:#ffc4d6">변경하지 않습니다.</mark>
- <mark style="background:#ffc4d6">세션 종료는 되돌릴 수 없는 조치(비가역, irreversible)입니다.</mark> 이미 종료된 세션은 재개할 수 없고, 사용자가 다시 로그인해야 새 세션이 생성되기 때문입니다. Unit 3 함수 `rollback_incident` 가 「되돌리기 불가」 기록을 남기므로, 담당자는 사용자에게 다시 로그인하라고 안내해야 합니다.
- 규칙 조정 제안은 즉시 적용하지 않습니다. 담당자가 IP 의 소유자와 용도, 예외로 둘 사용자를 검토하고 승인한 뒤에 변경합니다.
- <mark style="background:#ffdcb0">30분(`RECOVERY_LIMIT`)</mark>은 이 수업에서 정한 복구 기준 시간입니다. 지금 시각(`NOW` = 45분)에서 신고 접수 시각을 빼서 복구까지 걸린 시간을 구합니다. 예를 들어 `INC-301` 은 신고 접수 시각이 20분이라 <mark style="background:#bde3ff">45 − 20 = 25분</mark>입니다.

함수 네 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
false_positive.py   list_changes           : 바뀐 기록이면 (1번) 추가한다 (2번)
                    find_not_recovered     : 아직 잠긴 계정 (3번) · 아직 차단된 IP (4번) 를 찾는다
                    make_tuning_note       : IP 차단이면 (5번) 허용 목록 추가를 제안한다 (6번)
                    handle_false_positive  : 영향 확인 → 되돌리기 (7번) → 복구 확인 → 제안 순서로 처리한다
실행 파일           exercise4-2_run.py       : 신고마다 처리하고 (8번) 결과를 모은다 (9번)
```

## 실습 4-2 · 오탐 신고 처리와 롤백 확인

**이런 상황이 있습니다**

- **지금은**: <mark>롤백 함수는 있지만, 무엇이 바뀌었는지 확인하고(영향 확인), 실제로 복원됐는지 점검하고(복구 확인), 같은 오탐의 재발을 막을 규칙 조정을 제안하는 절차가 없습니다</mark>.
- **만드는 것**: 영향 확인 · 복구 확인 · 규칙 조정 제안 · 신고 한 건 처리(`false_positive.py`), 신고마다 처리하고 저장하기(`exercise4-2_run.py`).
- **실행하면**: <mark>단계 1: 신고 수와 처리 전 상태, 단계 2: 신고마다 영향 확인 · 되돌리기 · 복구 확인 · 규칙 조정 제안, 단계 3: 처리 뒤 상태, 단계 4: 저장한 파일이 나옵니다.</mark>

**할 일**: 데이터 파일 세 개와 코드 파일 두 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 · 3 을 읽습니다.

**`fp_state.json`** — 오탐을 처리하기 전 연습용 시스템 상태입니다. Unit 2 실습 2-1 의 `containment_state.json` 과 같은 모양입니다. `junho` 는 이 실습을 시작하기 전부터 잠겨 있던 계정입니다. 연습용 시스템(실제 서버를 대신하는 시스템)의 시계(`clock`)는 0 에서 움직이지 않습니다. 끝난 차단을 해제하는 `ip_actions.py` 의 함수 `expire_blocks` 도 호출하지 않습니다. 그래서 `block_expiry`(차단이 끝나는 시각)가 있어도 차단이 자동으로 풀리지 않습니다.

<pre class="copyable"><code>{"locked_users": ["junho", "dami", "jiwoo"], "blocked_ips": ["198.51.100.90"], "block_expiry": {"198.51.100.90": 120}, "clock": 0, "sessions": {"dami": [], "jiwoo": [], "junho": [], "hana": ["S-601"]}}
</code></pre>

**`fp_log.json`** — 자동 조치 기록 7건입니다. Unit 2 실습 2-1 의 `containment_log.json` 과 같은 모양입니다.

<pre class="copyable"><code>[
  {"action": "계정 잠금", "target": "dami", "incident": "INC-201", "before": "잠기지 않음", "after": "잠김", "reason": "퇴사한 계정의 서버 요청"},
  {"action": "세션 종료", "target": "dami", "incident": "INC-201", "before": "세션 2개", "after": "세션 0개", "reason": "퇴사한 계정의 서버 요청"},
  {"action": "IP 차단", "target": "198.51.100.90", "incident": "INC-202", "before": "차단되지 않음", "after": "차단됨", "reason": "경로 스캔 (120분 뒤 자동 해제)"},
  {"action": "계정 잠금", "target": "jiwoo", "incident": "INC-301", "before": "잠기지 않음", "after": "잠김", "reason": "해외 IP 에서 로그인"},
  {"action": "세션 종료", "target": "jiwoo", "incident": "INC-301", "before": "세션 1개", "after": "세션 0개", "reason": "해외 IP 에서 로그인"},
  {"action": "IP 차단", "target": "198.51.100.120", "incident": "INC-301", "before": "변경 없음", "after": "변경 없음", "reason": "여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요"},
  {"action": "계정 잠금", "target": "dami", "incident": "INC-205", "before": "잠김", "after": "잠김", "reason": "이미 잠겨 있어 변경 없음"}
]
</code></pre>

**`fp_reports.json`** — 오탐 신고 2건입니다. `reported_at` 은 신고를 받은 시각(분)입니다.

<pre class="copyable"><code>[
  {"incident": "INC-301", "reported_at": 20, "reporter": "영업팀장", "reason": "jiwoo 는 출장 중이고 출장 등록이 되어 있다"},
  {"incident": "INC-202", "reported_at": 40, "reporter": "인프라팀", "reason": "198.51.100.90 은 회사가 계약한 점검 업체의 스캐너 IP 다"}
]
</code></pre>

**`false_positive.py`** — 오탐 처리 함수 모음입니다. 도전 4-5 도 가져와 사용(import)합니다. Unit 3 파일 `rollback.py` 와 그 파일이 불러 쓰는 Unit 2 · 3 파일이 같은 폴더에 있어야 합니다(「시작하기」 레슨에서 확인). 직접 쓰는 곳은 1 ~ 7번입니다.

- 3번과 4번은 `if` 한 줄만 씁니다. 그 아래 미리 채운 `remaining.append(target)` 줄이 `if` 안쪽입니다.
- 6번의 `return` 은 5번 `if` 안쪽이라 한 단계 더 들여 씁니다. `for` 안에서 `return` 하면 그 자리에서 함수가 끝나므로, IP 차단 기록을 하나 찾으면 바로 제안을 돌려줍니다. IP 차단 기록이 하나도 없으면 `for` 를 다 돈 뒤 아래 미리 채운 줄로 내려가, 첫 번째 기록(`changes[0]`)으로 계정 예외를 제안합니다.

```python
from rollback import find_incident_records, rollback_incident                        # Unit 3 실습 3-1 의 되돌리기 함수를 불러온다

RECOVERY_LIMIT = 30                                                                  # 오탐 신고를 받은 뒤 복구를 끝내야 하는 시간(분)


def list_changes(log, incident_id):                                                  # 조치 기록 리스트와 인시던트 번호를 받는 함수
    """그 인시던트의 기록 가운데 조치 전과 조치 후가 다른 기록(자동 조치가 실제로 바꾼 것)만 리스트로 리턴한다.
    오탐 신고를 받았을 때, 무엇이 바뀌어서 누가 영향을 받았는지 먼저 확인할 때 쓴다.
    """
    changes = []                                                                     # 실제로 바뀐 기록을 모을 빈 리스트 — 미리 채운 줄
    for record in find_incident_records(log, incident_id):                           # 그 인시던트의 기록을 하나씩 읽는다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 1. record["before"] 와 record["after"] 가 다르면 (if, !=)
            # 2. changes 에 record 를 추가한다 (append)
    return changes                                                                   # 실제로 바뀐 기록 리스트를 리턴한다 — 미리 채운 줄


def find_not_recovered(changes, state):                                              # 바뀐 기록 리스트와 연습용 시스템 상태를 받는 함수
    """되돌린 뒤에도 아직 잠겨 있는 계정이나 차단된 IP 를 리스트로 리턴한다. 빈 리스트이면 복구가 끝난 것이다.
    되돌리기 함수를 실행한 뒤, 실제 상태가 원래대로 돌아왔는지 확인할 때 쓴다.
    """
    remaining = []                                                                   # 아직 복구되지 않은 대상을 모을 빈 리스트 — 미리 채운 줄
    for record in changes:                                                           # 바뀐 기록을 하나씩 읽는다 — 미리 채운 줄
        target = record["target"]                                                    # 조치 대상(계정 또는 IP) — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. record["action"] 이 "계정 잠금" 이고(and) target 이 state["locked_users"] 안에 있으면 (if, ==, in)
            remaining.append(target)                                                 # 아직 잠겨 있는 계정을 추가한다 — 미리 채운 줄
        # 4. record["action"] 이 "IP 차단" 이고(and) target 이 state["blocked_ips"] 안에 있으면 (if, ==, in)
            remaining.append(target)                                                 # 아직 차단된 IP 를 추가한다 — 미리 채운 줄
    return remaining                                                                 # 복구되지 않은 대상 리스트를 리턴한다 — 미리 채운 줄


def make_tuning_note(changes):                                                       # 바뀐 기록 리스트를 받는 함수
    """같은 오탐이 다시 나지 않도록 규칙을 어떻게 고칠지 제안 문장을 만들어 리턴한다.
    복구한 뒤, 탐지 규칙이나 허용 목록을 고치자고 담당자에게 남길 때 쓴다.
    """
    for record in changes:                                                           # 바뀐 기록을 하나씩 읽는다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. record["action"] 이 "IP 차단" 이면 (if, ==)
            # 6. "허용 목록에 추가 검토: " + record["target"] 을 리턴한다
    first = changes[0]                                                               # 첫 번째 바뀐 기록 — 미리 채운 줄
    return "탐지 규칙 예외 검토: " + first["target"] + " (" + first["reason"] + ")"  # 계정이면 규칙 예외를 제안한다 — 미리 채운 줄


def handle_false_positive(report, log, state, now):                                  # 오탐 신고 한 건 · 조치 기록 · 상태 · 지금 시각(분)을 받는 함수
    """오탐 신고 한 건을 영향 확인 → 되돌리기 → 복구 확인 순서로 처리하고, 규칙 조정 제안을 함께 담은 결과 딕셔너리를 리턴한다.
    오탐으로 잘못 잠그거나 차단한 것을 빠르고 빠짐없이 원래대로 돌릴 때 쓴다.
    """
    incident_id = report["incident"]                                                 # 오탐으로 신고된 인시던트 번호 — 미리 채운 줄
    changes = list_changes(log, incident_id)                                         # 영향 확인: 자동 조치가 실제로 바꾼 기록 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. rollback_incident(incident_id, log, state) 의 결과를 undo_records 에 저장한다 (되돌리기)
    remaining = find_not_recovered(changes, state)                                   # 복구 확인: 아직 남은 대상 — 미리 채운 줄
    changed = []                                                                     # 영향 받은 대상과 조치를 모을 빈 리스트 — 미리 채운 줄
    for record in changes:                                                           # 바뀐 기록을 하나씩 읽는다 — 미리 채운 줄
        changed.append(record["action"] + " " + record["target"])                    # 「조치 대상」 꼴로 추가한다 — 미리 채운 줄
    undone = []                                                                      # 되돌린 일을 모을 빈 리스트 — 미리 채운 줄
    for record in undo_records:                                                      # 되돌리기 기록을 하나씩 읽는다 — 미리 채운 줄
        undone.append(record["action"] + " " + record["target"])                     # 「조치 대상」 꼴로 추가한다 — 미리 채운 줄
    minutes = now - report["reported_at"]                                            # 신고를 받은 뒤 걸린 시간(분) — 미리 채운 줄
    result = {                                                                       # 처리 결과 한 건 — 미리 채운 줄
        "incident": incident_id,                                                     # 인시던트 번호
        "changed": changed,                                                          # 영향 받은 대상과 조치
        "undone": undone,                                                            # 되돌린 일
        "remaining": remaining,                                                      # 아직 복구되지 않은 대상
        "minutes": minutes,                                                          # 걸린 시간(분)
        "in_time": minutes <= RECOVERY_LIMIT,                                        # 정한 시간 안에 끝났는지
        "tuning": make_tuning_note(changes),                                         # 규칙 조정 제안
    }
    return result                                                                    # 처리 결과를 리턴한다 — 미리 채운 줄
```

**`exercise4-2_run.py`** — 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 두 번째 줄은 함수뿐 아니라 파일 맨 위에 적은 변수 `RECOVERY_LIMIT` 도 같은 `import` 로 불러옵니다.

```python
from incident import load_json, save_json                                                   # Unit 1 파일의 JSON 읽기 · 쓰기 함수를 불러온다
from false_positive import handle_false_positive, RECOVERY_LIMIT                            # 방금 만든 오탐 처리 함수를 불러온다

NOW = 45                                                                                    # 오탐 신고를 처리하는 지금 시각(분)

state = load_json("fp_state.json")                                                          # 오탐 처리 전 연습용 시스템 상태를 읽는다
log = load_json("fp_log.json")                                                              # 자동 조치 기록을 리스트로 읽는다
reports = load_json("fp_reports.json")                                                      # 오탐 신고 파일을 리스트로 읽는다
print("--- 단계 1: 오탐 신고", len(reports), "건 · 조치 기록", len(log), "건 · 지금", NOW, "분")  # 단계 1 시작을 알리는 줄
print("처리 전 잠긴 계정:", state["locked_users"], "· 차단된 IP:", state["blocked_ips"])    # 처리 전 상태를 출력한다

results = []                                                                                # 신고마다 처리 결과를 저장할 빈 리스트
print("--- 단계 2: 신고마다 영향 확인 · 되돌리기 · 복구 확인 · 규칙 조정 제안")             # 단계 2 시작을 알리는 줄
for report in reports:                                                                      # 오탐 신고를 하나씩 읽는다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 8. handle_false_positive(report, log, state, NOW) 의 결과를 result 에 저장한다
    # 9. results 에 result 를 추가한다 (append)
    print("[" + result["incident"] + "] 신고:", report["reporter"], "—", report["reason"])  # 신고 내용을 출력한다
    print(" - 영향 확인:", result["changed"])                                               # 자동 조치가 바꾼 것을 출력한다
    print(" - 되돌리기:", result["undone"])                                                 # 되돌린 일을 출력한다
    print(" - 복구 확인: 아직 잠기거나 차단된 대상", result["remaining"], "· 걸린 시간", result["minutes"], "분 · 기준", RECOVERY_LIMIT, "분 안", result["in_time"])  # 복구 확인 결과를 출력한다
    print(" - 규칙 조정 제안:", result["tuning"])                                           # 규칙 조정 제안을 출력한다

print("--- 단계 3: 처리 뒤 상태 (오탐이 아닌 계정은 그대로인지)")                           # 단계 3 시작을 알리는 줄
print("잠긴 계정:", state["locked_users"], "· 차단된 IP:", state["blocked_ips"])            # 처리 뒤 상태를 출력한다
print("dami 는 아직 잠김:", "dami" in state["locked_users"])                                # 진짜 공격(퇴사한 계정)은 그대로 잠겨 있는지 출력한다

save_json(results, "fp_results.json")                                                       # 처리 결과를 파일에 저장한다
save_json(state, "fp_state_after.json")                                                     # 처리 뒤 상태를 다른 파일에 저장한다
print("--- 단계 4: fp_results.json 에", len(results), "건 · fp_state_after.json 저장 · 기준", RECOVERY_LIMIT, "분")  # 단계 4 시작을 알리는 줄
```

**순서**

1. **[VS Code]** 파일 다섯 개 `fp_state.json` · `fp_log.json` · `fp_reports.json` · `false_positive.py` · `exercise4-2_run.py` 를 만듭니다. 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고 파일 이름을 그대로 적은 뒤, 코드 상자의 내용을 붙여 넣고 저장합니다(`Ctrl + S`, 맥북은 `Cmd + S`).
2. **[VS Code]** `false_positive.py` 1 ~ 7번, `exercise4-2_run.py` 8 · 9번을 씁니다. 막히면 아래 「실습 4-2 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise4-2_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 은 숫자가 제목 줄에 함께 나오고 그 아래 1줄입니다.
   - 단계 2 는 10줄(신고 한 건에 5줄씩), 단계 3 은 2줄입니다.
   - 단계 4 는 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
5. **[보고서]** `report_u4.md` 의 `## 실습 4-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 신고마다 걸린 시간과 처리 뒤 잠긴 계정을 적어 주세요.
   - (나) [핵심 질문] `INC-301` 의 영향 확인에 `IP 차단 198.51.100.120` 이 없습니다. `fp_log.json` 에서 `198.51.100.120` 의 IP 차단 기록이 가진 `before` · `after` 를 근거로 그 이유를 적고, `false_positive.py` 1번의 `if` 줄이 없으면 규칙 조정 제안이 어떻게 잘못되는지 적어 주세요.
   - (다) [핵심 질문] `INC-301` 의 되돌리기에 `되돌리기 불가 jiwoo` 가 있습니다. 무엇을 되돌릴 수 없는지(비가역 조치)와 담당자가 `jiwoo` 에게 따로 안내해야 할 것을 적어 주세요. 그리고 `dami` 가 처리 뒤에도 잠겨 있어야 하는 이유를 따로 적어 주세요.

## 실습 4-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 두 값이 다르면 | `if record["before"] != record["after"]:` |
| 리스트에 추가 | `changes.append(record)` |
| 두 조건을 함께 | `if record["action"] == "계정 잠금" and target in state["locked_users"]:` |
| 같으면 | `if record["action"] == "IP 차단":` |
| 문자열을 이어 붙여 리턴 | `return "허용 목록에 추가 검토: " + record["target"]` |
| 함수 결과를 변수에 저장하기 | `undo_records = rollback_incident(incident_id, log, state)` |

---


## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개와 「보고서 쓰기」 · 「오늘의 글 쓰기」를 끝낸 뒤 합니다. 도전을 하지 않았어도 이것으로 이 Unit 이 끝납니다.

**1. 오늘 한 일 확인**

1. 조치 요청 8건을 위험 점수로 자동 · 승인 필요 · 차단 금지로 나눴다 (실습 4-1)
2. 오탐 신고 2건을 영향 확인 · 롤백 · 복구 확인 · 규칙 조정 제안까지 처리했다 (실습 4-2)
3. 보고서 `report_u4.md` 의 실습 4-1 · 4-2 칸에 `답:` 뒤가 비어 있는 질문이 없다

**2. 파일 확인** — **[터미널]** `soar_response` 폴더에서 확인합니다.

```bash
pwd
ls
ls config
```

- `approval_gate.py` · `exercise4-1_run.py` · `gate_requests.json` · `gate_results.json` · `false_positive.py` · `exercise4-2_run.py` · `fp_state.json` · `fp_log.json` · `fp_reports.json` · `fp_results.json` · `fp_state_after.json` · `report_u4.md` 가 보여야 합니다.
- `config` 안에는 `approval_policy.json` 이 새로 보여야 합니다.
- `gate_results.json` · `fp_results.json` · `fp_state_after.json` 은 실행할 때 프로그램이 만든 결과 파일입니다. 이것도 올라갑니다.

**3. 깃허브에 올리기**

1. **[터미널]** `security-agent-toolkit` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/security-agent-toolkit` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark style="background:#ffc4d6">빨간 목록에 `.env`(API 키가 들어 있는 파일)나 `.venv`(가상환경 폴더)가 보이면 올리지 않고 멈춥니다.</mark>
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.
3. **[보고서]** `report_u4.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add approval gate and false positive rollback"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - <mark style="background:#ffc4d6">`git push` 가 거절(`rejected`)되면</mark> 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다. `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다. 그때 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다. 이 화면은 git 이 두 기록을 합친 기록에 붙일 메시지를 확인하라고 여는 편집기(vim)라서, 메시지는 고치지 않고 저장하고 닫기만 하면 됩니다.
5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `soar_response` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.

- 시간이 남아 도전을 했다면 도전 파일까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**4. 이어지는 곳**

1. 다음 Unit 5(통합 엔진과 최종 회고)에서는 지금까지 만든 플레이북 · 조치 · 티켓 · 승인 게이트를 엔진 하나로 연결합니다.
2. 오늘 만든 `approval_gate.py` 와 `config/approval_policy.json` 은 Unit 5 실습 5-1 · 5-2 에서 그대로 가져와 씁니다.

---

<!-- learn:answers -->
