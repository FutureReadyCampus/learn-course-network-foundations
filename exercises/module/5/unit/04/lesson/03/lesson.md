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
> - `INC-202`: 경로 스캔(서버의 여러 주소에 차례로 요청을 보내 약점을 찾는 일)으로 자동 차단한 IP `198.51.100.90` 이 회사가 계약한 점검 업체의 스캐너(scanner: 약점을 찾으려고 서버에 자동으로 요청을 보내는 점검 도구)라고 인프라팀(서버 · 네트워크를 관리하는 팀)이 알려 왔습니다.
> - **문제**: 롤백 함수만 실행하면 오탐 대응이 끝나지 않습니다.
> - <mark style="background:#ffc4d6">영향 확인(impact assessment: 조치가 실제로 바꾼 대상을 파악하는 일)을 먼저 하지 않으면</mark> 누가 영향을 받았는지 알 수 없습니다. 신고와 상관없는 진짜 공격(정탐, true positive: 실제 공격을 정확히 탐지한 것)인 `dami` 잠금(`INC-201`)이 그대로인지도 따로 확인하기 어렵습니다.
> - 롤백한 뒤 복구 확인(recovery verification: 실제 상태가 복원됐는지 다시 점검하는 일)을 하지 않으면 해제되지 않은 계정이 남아도 알 수 없습니다. 그러면 `jiwoo` 가 계속 로그인하지 못할 수 있습니다.
> - 탐지 규칙을 조정하지 않으면 다음 출장 때도 같은 오탐 알림이 생깁니다.
> - **부탁**: 오탐 신고마다 영향 확인 → 롤백 → 복구 확인 순서로 처리하고, 신고를 접수한 뒤 <mark style="background:#ffdcb0">30분 이내</mark>에 복구했는지도 기록해 주세요. 마지막으로 담당자가 검토할 규칙 조정(튜닝, tuning: 같은 오탐이 반복되지 않도록 탐지 규칙이나 허용 목록을 고치는 일) 제안을 남겨 주세요.
> - **바뀌는 점**: 두 신고가 <mark style="background:#bde3ff">25분 · 5분</mark> 만에 복구됩니다. 롤백한 뒤에도 잠겨 있거나 차단된 대상은 <mark style="background:#bde3ff">0개</mark>입니다. <mark style="background:#ffc4d6">`jiwoo` 의 세션은 되돌릴 수 없는 조치(비가역, irreversible)라 「되돌리기 불가」로 따로 남습니다.</mark> 그래서 `jiwoo` 가 다시 로그인해야 합니다. `dami` 는 그대로 잠겨 있습니다. 상황과 이름은 설명을 위한 예시입니다.

## 3.1 오탐 대응의 네 단계

| 순서 | 하는 일 | 오늘 쓰는 함수 |
|---|---|---|
| 1. 영향 확인 | 그 인시던트의 기록 가운데 조치 전(`before`)과 조치 후(`after`)가 다른 기록만 찾는다 | `list_changes` (① · ② 직접 씀) |
| 2. 되돌리기 | 자동 조치가 바꾼 것만 조치 이전 상태로 롤백한다 | <mark style="background:#e0d4ff">Unit 3 함수 `rollback_incident`</mark> (미리 채움) |
| 3. 복구 확인 | 롤백한 뒤에도 잠겨 있는 계정 · 차단된 IP 가 남았는지 점검한다 | `find_not_recovered` (미리 채움) |
| 4. 규칙 조정 제안 | 같은 오탐을 막을 규칙 조정을 담당자에게 제안한다 | `make_tuning_note` (미리 채움) |

규칙 조정 제안은 조치 종류에 따라 다릅니다. IP 차단이었으면 허용 목록 추가 검토, 계정이었으면 탐지 규칙 예외(exception) 검토를 제안합니다.

- <mark style="background:#e0d4ff">Module 4 Unit 4 실습 4-2 에서는 예외 규칙으로 탐지 규칙을 고쳐(튜닝) 오탐 알림을 줄였습니다.</mark> 오늘은 오탐 때문에 **이미 실행된 자동 조치**를 원래 상태로 복원(롤백)하는 일입니다.
- `INC-301` 에는 IP `198.51.100.120` 의 차단 기록도 있지만 `before` 와 `after` 가 모두 <mark style="background:#bde3ff">「변경 없음」</mark>입니다. 바뀐 것이 없으므로 영향 확인 대상에서 제외합니다.
- `rollback_incident` 는 신고된 인시던트의 기록만 롤백합니다. 같은 기록 파일에 있는 `INC-201`(`dami`)은 <mark style="background:#ffc4d6">변경하지 않습니다.</mark>
- <mark style="background:#ffc4d6">세션 종료는 되돌릴 수 없는 조치(비가역, irreversible)입니다.</mark> 이미 종료된 세션은 재개할 수 없고, 사용자가 다시 로그인해야 새 세션이 생성되기 때문입니다. Unit 3 함수 `rollback_incident` 가 「되돌리기 불가」 기록을 남기므로, 담당자는 사용자에게 다시 로그인하라고 안내해야 합니다.
- 규칙 조정 제안은 즉시 적용하지 않습니다. 담당자가 IP 의 소유자와 용도, 예외로 둘 사용자를 검토하고 승인한 뒤에 변경합니다.
- <mark style="background:#ffdcb0">30분(`RECOVERY_LIMIT`)</mark>은 이 수업에서 정한 복구 기준 시간입니다. 지금 시각(`NOW` = 45분)에서 신고 접수 시각을 빼서 복구까지 걸린 시간을 구합니다. 예를 들어 `INC-301` 은 신고 접수 시각이 20분이라 <mark style="background:#bde3ff">45 − 20 = 25분</mark>입니다.

함수 네 개와 실행 파일은 대부분 미리 채워 두었습니다. 직접 쓰는 곳은 첫 단계인 영향 확인 `list_changes` 의 **두 줄**(① · ②)입니다.

```
false_positive.py   list_changes           : 바뀐 기록이면 (①) 추가한다 (②)
                    find_not_recovered     : 아직 잠긴 계정 · 아직 차단된 IP 를 찾는다 (미리 채움)
                    make_tuning_note       : IP 차단이면 허용 목록 추가를 제안한다 (미리 채움)
                    handle_false_positive  : 영향 확인 → 되돌리기 → 복구 확인 → 제안 순서로 처리한다 (미리 채움)
실행 파일           exercise4-2_run.py       : 신고마다 처리하고 결과를 모은다 (미리 채움)
```

<h2>문법 상자 · 직접 쓰는 곳의 모양 (예시 값 · 읽기만 합니다)</h2>

```python
record = {"before": "잠기지 않음", "after": "잠김"}   # 예시 값
found = []                                          # 예시 리스트

if record["before"] != record["after"]:             # 「다르면」은 != 로 묻는다. 끝에 : 를 붙인다
    found.append(record)                            # if 안쪽 줄은 4칸 더 들여 쓴다
print(len(found))                                   # 1
```

- `!=` 는 「같지 않으면」입니다. `before` 와 `after` 가 다르다는 것은 자동 조치가 실제로 무언가를 바꿨다는 뜻입니다.
- `리스트.append(값)` 은 리스트 끝에 값을 하나 더합니다.

## 실습 4-2 · 오탐 신고 처리와 롤백 확인

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>롤백 함수는 있지만, 무엇이 바뀌었는지 확인하고(영향 확인), 실제로 복원됐는지 점검하고(복구 확인), 같은 오탐의 재발을 막을 규칙 조정을 제안하는 절차가 없습니다</mark>.
- **만드는 것**: 영향 확인 · 복구 확인 · 규칙 조정 제안 · 신고 한 건 처리(`false_positive.py`), 신고마다 처리하고 저장하기(`exercise4-2_run.py`).
- **실행하면**: <mark>단계 1: 신고 수와 처리 전 상태, 단계 2: 신고마다 영향 확인 · 되돌리기 · 복구 확인 · 규칙 조정 제안, 단계 3: 처리 뒤 상태, 단계 4: 저장한 파일이 나옵니다.</mark>

<h2>할 일</h2>

1. `soar_response` 폴더에 데이터 파일 세 개(`fp_state.json` · `fp_log.json` · `fp_reports.json`)와 코드 파일 두 개(`false_positive.py` · `exercise4-2_run.py`)를 만들어 붙여 넣습니다.
2. `false_positive.py` 에서 `# ←` 가 있는 <mark>두 곳</mark>(① · ②)을 한 줄씩 채웁니다.
3. 실행해서 단계 2 · 3 을 읽습니다.

<h3><code>fp_state.json</code></h3>

오탐을 처리하기 전 연습용 시스템 상태입니다. Unit 2 실습 2-1 의 `containment_state.json` 과 같은 모양입니다. `junho` 는 이 실습을 시작하기 전부터 잠겨 있던 계정입니다. 연습용 시스템(실제 서버를 대신하는 시스템)의 시계(`clock`)는 0 에서 움직이지 않습니다. 끝난 차단을 해제하는 `ip_actions.py` 의 함수 `expire_blocks` 도 호출하지 않습니다. 그래서 `block_expiry`(차단이 끝나는 시각)가 있어도 차단이 자동으로 풀리지 않습니다.

<pre class="copyable"><code>{"locked_users": ["junho", "dami", "jiwoo"], "blocked_ips": ["198.51.100.90"], "block_expiry": {"198.51.100.90": 120}, "clock": 0, "sessions": {"dami": [], "jiwoo": [], "junho": [], "hana": ["S-601"]}}
</code></pre>

<h3><code>fp_log.json</code></h3>

자동 조치 기록 7건입니다. Unit 2 실습 2-1 의 `containment_log.json` 과 같은 모양입니다. 마지막 줄(`INC-205`)은 다른 인시던트의 기록이라 오늘 신고와 무관합니다(`find_incident_records` 가 신고된 인시던트의 기록만 골라 냅니다).

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

<h3><code>fp_reports.json</code></h3>

오탐 신고 2건입니다. `reported_at` 은 신고를 받은 시각(분)입니다.

<pre class="copyable"><code>[
  {"incident": "INC-301", "reported_at": 20, "reporter": "영업팀장", "reason": "jiwoo 는 출장 중이고 출장 등록이 되어 있다"},
  {"incident": "INC-202", "reported_at": 40, "reporter": "인프라팀", "reason": "198.51.100.90 은 회사가 계약한 점검 업체의 스캐너 IP 다"}
]
</code></pre>

<h3><code>false_positive.py</code></h3>

오탐 처리 함수 모음입니다. 응용 4-5 도 가져와 사용(import)합니다. Unit 3 파일 `rollback.py` 와 그 파일이 불러 쓰는 Unit 2 · 3 파일이 같은 폴더에 있어야 합니다(「시작하기」 레슨에서 확인). 직접 쓰는 곳은 `list_changes` 의 ① · ② 두 줄이고, 나머지는 미리 채운 줄입니다.

- `make_tuning_note` 는 `for` 안에서 `return` 합니다. `return` 하면 그 자리에서 함수가 끝나므로, IP 차단 기록을 하나 찾으면 바로 제안을 돌려줍니다. IP 차단 기록이 하나도 없으면 `for` 를 다 돈 뒤 아래 줄로 내려가, 첫 번째 기록(`changes[0]`)으로 계정 예외를 제안합니다.

```python exercise
from rollback import find_incident_records, rollback_incident                        # Unit 3 실습 3-1 의 되돌리기 함수를 불러온다

RECOVERY_LIMIT = 30                                                                  # 오탐 신고를 받은 뒤 복구를 끝내야 하는 시간(분)


def list_changes(log, incident_id):                                                  # 조치 기록 리스트와 인시던트 번호를 받는 함수
    """그 인시던트의 기록 가운데 조치 전과 조치 후가 다른 기록(자동 조치가 실제로 바꾼 것)만 리스트로 리턴한다.
    오탐 신고를 받았을 때, 무엇이 바뀌어서 누가 영향을 받았는지 먼저 확인할 때 쓴다.
    """
    changes = []                                                                     # 실제로 바뀐 기록을 모을 빈 리스트 — 미리 채운 줄
    for record in find_incident_records(log, incident_id):                           # 그 인시던트의 기록을 하나씩 읽는다 — 미리 채운 줄
        # ① record["before"] 와 record["after"] 가 다르면 (if, !=)   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
#|         if record["before"] != record["after"]:
        # ② changes 에 record 를 추가한다 (append)   # ← 이 주석 바로 아래 줄에 씁니다 (12칸)
#|             changes.append(record)

    return changes                                                                   # 실제로 바뀐 기록 리스트를 리턴한다 — 미리 채운 줄


def find_not_recovered(changes, state):                                              # 바뀐 기록 리스트와 연습용 시스템 상태를 받는 함수
    """되돌린 뒤에도 아직 잠겨 있는 계정이나 차단된 IP 를 리스트로 리턴한다. 빈 리스트이면 복구가 끝난 것이다.
    되돌리기 함수를 실행한 뒤, 실제 상태가 원래대로 돌아왔는지 확인할 때 쓴다.
    """
    remaining = []                                                                   # 아직 복구되지 않은 대상을 모을 빈 리스트 — 미리 채운 줄
    for record in changes:                                                           # 바뀐 기록을 하나씩 읽는다 — 미리 채운 줄
        target = record["target"]                                                    # 조치 대상(계정 또는 IP) — 미리 채운 줄
        if record["action"] == "계정 잠금" and target in state["locked_users"]:      # 잠금 기록인데 아직 잠겨 있으면 — 미리 채운 줄
            remaining.append(target)                                                 # 아직 잠겨 있는 계정을 추가한다 — 미리 채운 줄
        if record["action"] == "IP 차단" and target in state["blocked_ips"]:         # 차단 기록인데 아직 차단되어 있으면 — 미리 채운 줄
            remaining.append(target)                                                 # 아직 차단된 IP 를 추가한다 — 미리 채운 줄
    return remaining                                                                 # 복구되지 않은 대상 리스트를 리턴한다 — 미리 채운 줄


def make_tuning_note(changes):                                                       # 바뀐 기록 리스트를 받는 함수
    """같은 오탐이 다시 나지 않도록 규칙을 어떻게 고칠지 제안 문장을 만들어 리턴한다.
    복구한 뒤, 탐지 규칙이나 허용 목록을 고치자고 담당자에게 남길 때 쓴다.
    """
    for record in changes:                                                           # 바뀐 기록을 하나씩 읽는다 — 미리 채운 줄
        if record["action"] == "IP 차단":                                            # IP 차단 기록이면 — 미리 채운 줄
            return "허용 목록에 추가 검토: " + record["target"]                      # 허용 목록에 넣자고 제안한다 — 미리 채운 줄
    first = changes[0]                                                               # 첫 번째 바뀐 기록 — 미리 채운 줄
    return "탐지 규칙 예외 검토: " + first["target"] + " (" + first["reason"] + ")"  # 계정이면 규칙 예외를 제안한다 — 미리 채운 줄


def handle_false_positive(report, log, state, now):                                  # 오탐 신고 한 건 · 조치 기록 · 상태 · 지금 시각(분)을 받는 함수
    """오탐 신고 한 건을 영향 확인 → 되돌리기 → 복구 확인 순서로 처리하고, 규칙 조정 제안을 함께 담은 결과 딕셔너리를 리턴한다.
    오탐으로 잘못 잠그거나 차단한 것을 빠르고 빠짐없이 원래대로 돌릴 때 쓴다.
    """
    incident_id = report["incident"]                                                 # 오탐으로 신고된 인시던트 번호 — 미리 채운 줄
    changes = list_changes(log, incident_id)                                         # 영향 확인: 자동 조치가 실제로 바꾼 기록 — 미리 채운 줄
    undo_records = rollback_incident(incident_id, log, state)                        # 되돌리기: 자동 조치가 바꾼 것만 거꾸로 되돌린다 — 미리 채운 줄
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

<h3><code>exercise4-2_run.py</code></h3>

직접 쓰는 줄이 없습니다. 그대로 붙여 넣습니다. 두 번째 줄은 함수뿐 아니라 파일 맨 위에 적은 변수 `RECOVERY_LIMIT` 도 같은 `import` 로 불러옵니다.

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
    result = handle_false_positive(report, log, state, NOW)                                 # 신고 한 건을 처리하고 결과를 받는다
    results.append(result)                                                                  # 처리 결과를 추가한다
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

- 주석 줄은 그대로 두고, **각 주석 바로 아래 줄**에 씁니다. ① 은 `for` 안쪽의 `if` 줄이라 8칸, ② 는 그 `if` 안쪽 줄이라 12칸에서 시작합니다.
- 바로 아래 `find_not_recovered` 의 미리 채운 `if …:` 와 `remaining.append(target)` 두 줄이 ① · ② 와 같은 모양입니다.

<h3>직접 쓰는 곳</h3>

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | `before` 와 `after` 가 다르면 (`if`, `!=`) | 8칸 |
| ② | `changes` 에 `record` 를 추가 (`append`) | 12칸 |

- 순서에는 없지만, 채우기 전에 실행하면 `IndentationError: expected an indented block after 'for' statement` 가 나옵니다. `for` 안쪽 줄(① · ②)이 아직 비어 있어서 나는 오류이니 정상입니다. 오류의 `^^^^^^` 표시가 `return changes` 줄을 가리켜도, 고칠 곳은 그 위 ① · ② 입니다.
- ① 확인: ① 만 쓰고 실행하면 `IndentationError: expected an indented block after 'if' statement` 가 나옵니다. ② 를 아직 안 써서 나는 오류이니 정상입니다. 막히면: 문법 상자의 `if record["before"] != record["after"]:` 를 그대로 8칸에 씁니다.
- ② 확인: ② 까지 쓰고 실행하면 `INC-301` 의 영향 확인이 ` - 영향 확인: ['세션 종료 jiwoo', '계정 잠금 jiwoo']` 로 나오면 성공입니다. `IP 차단 198.51.100.120` 이 섞여 나오면 ① 의 `if` 줄을 썼는지, `!=` 인지 봅니다. 막히면: 문법 상자의 `found.append(record)` 에서 `found` 자리에 `changes` 를 씁니다.

<h2>순서</h2>

1. **[VS Code]** 파일 다섯 개 `fp_state.json` · `fp_log.json` · `fp_reports.json` · `false_positive.py` · `exercise4-2_run.py` 를 만듭니다. 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고 파일 이름을 그대로 적은 뒤, 코드 상자의 내용을 붙여 넣고 저장합니다(`Ctrl + S`).

<!-- checklist -->
- [ ] `soar_response` 폴더에 `fp_state.json` · `fp_log.json` · `fp_reports.json` 을 만들고 붙여 넣은 뒤 저장했다
- [ ] `soar_response` 폴더에 `false_positive.py` · `exercise4-2_run.py` 를 만들고 붙여 넣은 뒤 저장했다
<!-- /checklist -->

2. **[VS Code]** `false_positive.py` 의 `# ←` 두 곳(① · ②)을 채웁니다. 3.1 표의 1번 줄 「조치 전과 조치 후가 다른 기록만 찾는다」를 보고 씁니다.

<!-- checklist -->
- [ ] `false_positive.py` 의 빈칸 ① · ② 를 채우고 저장했다
<!-- /checklist -->

3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다.
   ```bash
   python exercise4-2_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 은 숫자가 제목 줄에 함께 나오고 그 아래 1줄입니다.
   - 단계 2 는 10줄(신고 한 건에 5줄씩), 단계 3 은 2줄입니다.
   - 단계 4 는 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.

<!-- checklist -->
- [ ] `python exercise4-2_run.py` 를 실행해 걸린 시간 `25 분` · `5 분` 과 `dami 는 아직 잠김: True` 가 나왔다
<!-- /checklist -->

5. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.

<!-- answer: 10|실습 4-2 정답 -->

**확인** — 단계 2 에 두 신고 처리 결과가, 단계 3 에 처리 뒤 상태가 나오고 단계 4 에 두 건이 저장되면 성공입니다. 출력이 다르면 이 실습 바로 하단 바의 ‘정답 보기’와 비교합니다.

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


## 핵심 코드와 결과를 저장소에 반영하기

핵심 실습에서 만든 코드와 입력 데이터를 저장소에 남깁니다. 선택 과제용 헬퍼는 이 단계에서 만들지 않습니다.

1. **[터미널]** `soar_response` 폴더에서 핵심 파일과 입력 데이터를 확인합니다.
   ```bash
   pwd
   ls
   ls config
   ```
   `approval_gate.py` · `exercise4-1_run.py` · `gate_requests.json` · `false_positive.py` · `exercise4-2_run.py` · `fp_state.json` · `fp_log.json` · `fp_reports.json` 와 `config/approval_policy.json` 이 있어야 합니다.
2. 저장소 루트 `network-study-notes` 로 이동하고 변경 목록을 확인합니다.
   ```bash
   cd ..
   git status
   ```
   `.env` 나 비밀키가 포함된 파일은 올리지 말고 `.gitignore` 를 확인합니다.
3. 핵심 실습의 실행 결과와 복구 상태를 기록에 반영한 뒤 저장소에 올립니다.
   ```bash
   git add soar_response
   git commit -m "Add M5 Unit 4 approval and recovery exercises"
   git push
   ```

<!-- checklist -->
- [ ] 핵심 코드와 입력 데이터를 저장소에 올렸다
<!-- /checklist -->
