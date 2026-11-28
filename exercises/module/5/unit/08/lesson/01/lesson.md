---
id: m5-u08-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/130_day05_am_report_gate.md
  mission_id: GichanSource.m5-1113-am-report-gate
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 리포트 · 승인 게이트 · 롤백

<mark style="background:#e0d4ff">Unit 7까지 조치 · 티켓 · 알림 · 에스컬레이션</mark>(escalation, 에스컬레이션: 정해진 시간 안에 처리되지 않은 사건을 상위 담당자에게 넘겨 처리하게 하는 일)을 만들었습니다. Unit 8에서는 세 가지를 만듭니다. <mark>**처리 결과를 리포트로 보고하는 부분, 자동 실행해도 되는 조치와 사람의 승인이 필요한 조치를 나누는 부분, 오탐으로 밝혀진 조치를 원래 상태로 되돌리는 부분**</mark>입니다.

- **실습 8-1**: Unit 7 근무의 티켓을 판다스(pandas, 판다스: 표 모양 데이터를 다루는 파이썬 도구) 표로 바꿔 집계(aggregation, 어그리게이션: 값을 그룹별로 모아 개수 · 평균을 구하는 일)합니다. 그다음 조치 기록과 대조(reconciliation, 레컨실리에이션: 두 기록이 서로 맞는지 맞춰 보는 일)해서 초동 대응 리포트(incident report, 인시던트 리포트: 사건의 현황과 처리 내용을 정리해 전달하는 문서) 파일을 씁니다(`report.py`).
- **실습 8-2**: 조치 요청마다 위험 점수(risk score, 리스크 스코어: 조치의 위험을 점수로 나타낸 값)를 더해 「자동 · 승인 필요 · 차단 금지」로 나누는 승인 게이트를 만듭니다. <mark style="background:#ffdcb0">승인 기준은 설정 파일에 따로 둡니다</mark>(`approval_gate.py`).
- **실습 8-3**: 오탐(false positive, 폴스 포지티브: 위협이 아닌 활동을 위협으로 잘못 판정한 알림) 신고를 받으면 먼저 영향 확인(impact assessment: 조치가 실제로 바꾼 대상을 파악하는 일)을 합니다. 그다음 <mark style="background:#e0d4ff">Unit 5의 되돌리기 함수</mark>로 롤백(rollback, 롤백: 조치 이전 상태로 되돌리는 일)합니다. 마지막으로 복구 확인(recovery verification: 실제 상태가 되돌아왔는지 다시 점검하는 일)까지 합니다(`false_positive.py`).

깃허브에 올리는 일은 Unit 9의 실습 9-2 마지막에 합니다. 새 문법은 실습 8-1의 판다스 세 가지입니다. 열(column, 컬럼: 표의 세로 줄)끼리 빼기, 그룹마다 평균 `mean`, 반올림 `round` 입니다. 보고서의 [핵심 질문] 표시가 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 들여쓰기(줄 앞의 빈칸)는 각 번호 주석과 같은 위치에서 시작합니다. 각 번호 주석 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

 **이전 파일**: <mark style="background:#e0d4ff">Unit 1의 `incident.py`</mark>(`load_json` · `save_json`)를 모든 실습에서 씁니다. 실습 8-3에서는 <mark style="background:#e0d4ff">Unit 5의 `rollback.py`</mark> 와, 그 파일이 직접 또는 다른 파일을 거쳐 가져와 사용(import)하는 `undo_actions.py` · `account_actions.py` · `ip_actions.py` · `containment_store.py` 도 씁니다. 없는 파일은 아래 시작하기의 「 이전 파일이 없을 때」 코드 상자로 만듭니다.

 **줄임말 이름 안내**: 이 문서의 코드와 파일에는 줄임말로 된 이름이 있습니다. 처음 보면 뜻을 알기 어려워서 아래에 풀어 둡니다. 이미 배포한 파일과 맞추기 위해 이름은 그대로 쓰고 뜻만 설명합니다.
  - `ack` · `acked` 는 acknowledge(확인하다) · acknowledged(확인했다)의 줄임말입니다. 담당자가 티켓을 처음 확인했다는 뜻입니다.
  - `acked_at` 은 처음 확인한 시각(분), `ack_minutes` 는 확인까지 걸린 분, `acked` 는 확인한 티켓만 남긴 표, `mean_ack_by_grade` 는 등급마다 확인까지 걸린 분의 평균을 구하는 함수입니다.
  - `sla` 는 서비스 수준 협약(SLA, Service Level Agreement)의 줄임말입니다. 이 문서에서는 응답 기한을 뜻합니다.
  - `sla_due` 는 응답해야 하는 시각입니다.

## 폴더 열고 파일 준비하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `soar_response` 폴더로 들어가 파일을 확인합니다. <mark>`ls` 결과에 `incident.py` 와 `rollback.py` 가 보이면</mark> 됩니다. 실습 8-3에는 Unit 4 · Unit 5의 `undo_actions.py` · `account_actions.py` · `ip_actions.py` · `containment_store.py` 도 필요합니다(없으면 아래 「이전 파일이 없을 때」 절의 코드 상자로 만듭니다).
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 답을 적는 **보고서**(`report_u8.md`)도 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. **[터미널]** 판다스를 불러올 수 있는지 확인합니다(맥북은 `python3`). <mark>`판다스 불러오기 성공` 이 나와야</mark> 합니다.
   ```bash
   python -c "import pandas; print('판다스 불러오기 성공')"
   ```
   - `No module named 'pandas'`(판다스가 설치되어 있지 않다는 뜻)가 나오면 터미널(가상환경이 켜진 상태)에서 `pip install pandas`(판다스를 설치하는 명령)를 입력한 뒤 다시 확인합니다.
5. **[VS Code]** 실습 8-1 데이터 파일 두 개 `unit10_tickets.json` · `unit10_actions.json` 을 만듭니다. 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고 파일 이름을 그대로 적은 뒤, 코드 상자의 내용을 붙여 넣고 저장합니다(`Ctrl + S`, 맥북은 `Cmd + S`).

<h2><code>unit10_tickets.json</code></h2>

Unit 7의 근무 3시간 시뮬레이션이 끝났을 때의 티켓 7장입니다.

- **무엇인가**:
  - Unit 7의 실습 7-2에서 저장한 `shift_tickets.json` 에서 리포트에 쓰는 키만 남긴 것입니다.
  - `incidents` 는 티켓 하나로 병합(merge)된 인시던트(incident, 인시던트: 탐지된 보안 사건 하나)의 번호 리스트입니다.
  - 시각을 나타내는 키는 네 개입니다.
    - `created_at`: 티켓 생성 시각입니다.
    - `sla_due`: 응답 기한 시각입니다. 담당자가 이 시각까지 확인해야 하는 마감 시각입니다. SLA 는 Service Level Agreement(에스엘에이)의 줄임말이고, 담당자가 응답해야 하는 시간을 미리 약속한 서비스 수준 협약입니다.
    - `acked_at`: 확인 시각입니다. acknowledge 는 담당자가 사건을 처음 확인했다는 뜻입니다.
    - `resolved_at`: 해결 시각입니다.
    - 네 값은 모두 근무를 시작한 때를 0분으로 놓고, 그때부터 몇 분이 지났는지를 적은 숫자입니다. <mark style="background:#ffdcb0">아직 확인하지 않았거나 해결하지 않았으면 `-1` 입니다.</mark>
- **어디에 쓰나**: 실습 8-1 리포트의 재료입니다.

```
[
  {"id": "TCK-1", "incidents": ["INC-201", "INC-205", "INC-209"], "entity": "dami", "rule": "퇴사한 계정", "grade": "high", "status": "해결", "created_at": 0, "sla_due": 15, "acked_at": 10, "resolved_at": 45},
  {"id": "TCK-2", "incidents": ["INC-202", "INC-206"], "entity": "198.51.100.90", "rule": "경로 스캔", "grade": "low", "status": "열림", "created_at": 3, "sla_due": 243, "acked_at": -1, "resolved_at": -1},
  {"id": "TCK-3", "incidents": ["INC-203"], "entity": "gaeun", "rule": "규칙은 허용인데 서버가 거절", "grade": "mid", "status": "해결", "created_at": 8, "sla_due": 68, "acked_at": 80, "resolved_at": 120},
  {"id": "TCK-4", "incidents": ["INC-204"], "entity": "seoyeon", "rule": "대량 다운로드", "grade": "mid", "status": "확인 중", "created_at": 12, "sla_due": 72, "acked_at": 140, "resolved_at": -1},
  {"id": "TCK-5", "incidents": ["INC-207"], "entity": "203.0.113.250", "rule": "경로 스캔", "grade": "low", "status": "열림", "created_at": 30, "sla_due": 270, "acked_at": -1, "resolved_at": -1},
  {"id": "TCK-6", "incidents": ["INC-208"], "entity": "hana", "rule": "업무 시간 밖 로그인", "grade": "mid", "status": "해결", "created_at": 35, "sla_due": 95, "acked_at": 90, "resolved_at": 130},
  {"id": "TCK-7", "incidents": ["INC-210", "INC-211"], "entity": "dami", "rule": "퇴사한 계정", "grade": "high", "status": "확인 중", "created_at": 95, "sla_due": 110, "acked_at": 105, "resolved_at": -1}
]
```

<h2><code>unit10_actions.json</code></h2>

근무 중 자동 대응이 남긴 조치 기록 9건에, 설명을 위해 만든 `INC-212` 1건을 더한 10건입니다.

- **무엇인가**:
  - <mark style="background:#e0d4ff">Unit 4에서 만든 조치 기록</mark>(감사 기록, audit log: 조치를 순서대로 남긴 기록)에서 `reason` 키만 뺀 모양입니다. `before` 는 조치 전 상태, `after` 는 조치 후 상태입니다.
  - `INC-212` 는 근무가 끝나기 직전에 `yuna` 계정을 잠근 기록입니다. 티켓 생성 단계가 실패해서 이 인시던트에는 티켓이 없습니다.
- **어디에 쓰나**: 실습 8-1 리포트는 티켓과 조치 기록을 대조해 티켓마다 조치 기록 수를 세고, 티켓이 없는 조치(추적 누락)를 찾습니다.

```
[
  {"incident": "INC-201", "action": "계정 잠금", "target": "dami", "before": "잠기지 않음", "after": "잠김"},
  {"incident": "INC-201", "action": "세션 종료", "target": "dami", "before": "세션 2개", "after": "세션 0개"},
  {"incident": "INC-202", "action": "IP 차단", "target": "198.51.100.90", "before": "차단되지 않음", "after": "차단됨"},
  {"incident": "INC-205", "action": "계정 잠금", "target": "dami", "before": "잠김", "after": "잠김"},
  {"incident": "INC-206", "action": "IP 차단", "target": "198.51.100.90", "before": "차단됨", "after": "차단됨"},
  {"incident": "INC-207", "action": "IP 차단", "target": "203.0.113.250", "before": "차단되지 않음", "after": "차단되지 않음 (확인 실패)"},
  {"incident": "INC-209", "action": "계정 잠금", "target": "dami", "before": "잠김", "after": "잠김"},
  {"incident": "INC-210", "action": "계정 잠금", "target": "dami", "before": "잠김", "after": "잠김"},
  {"incident": "INC-211", "action": "계정 잠금", "target": "dami", "before": "잠김", "after": "잠김"},
  {"incident": "INC-212", "action": "계정 잠금", "target": "yuna", "before": "잠기지 않음", "after": "잠김"}
]
```

6. **[터미널]** 파일이 정상인지 확인합니다(맥북은 `python3`). <mark>`7 10` 이 나와야</mark> 합니다.
   ```bash
   python -c "import json; print(len(json.load(open('unit10_tickets.json', encoding='utf-8'))), len(json.load(open('unit10_actions.json', encoding='utf-8'))))"
   ```

## 이전 파일이 없을 때 (Unit 1 · Unit 4 · Unit 5 파일)

Unit 1 · Unit 4 · Unit 5 중 하지 못한 Unit이 있거나 파일을 지운 경우에만 만듭니다. **이미 있는 파일은 건너뜁니다.** **[VS Code]** 에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 아래 여섯 파일을 하나씩 만듭니다. 파일 이름은 `incident.py` · `containment_store.py` · `account_actions.py` · `ip_actions.py` · `undo_actions.py` · `rollback.py` 입니다.

- 아래 코드 상자 여섯 개를 같은 이름의 파일에 순서대로 붙여 넣고 저장합니다. 이미 있는 파일은 새로 만들거나 붙여 넣지 않습니다. 실습 8-1 · 실습 8-2에는 `incident.py` 만 있으면 되고, 나머지 다섯 개는 실습 8-3에서 씁니다.

<h2><code>incident.py</code></h2>

Unit 1 파일에서 오늘 쓰는 두 함수(`load_json` · `save_json`)만 담았습니다. Unit 1 파일 전체가 있으면 그것을 그대로 씁니다.

```python
import json                                                  # JSON 파일을 읽고 쓰기 위해 json 을 불러온다


def load_json(path):                                         # 파일 경로를 받는 함수
    """JSON 파일을 읽어 리스트나 딕셔너리로 리턴한다.
    인시던트와 플레이북 등록 파일을 읽을 때 쓴다.
    """
    with open(path, encoding="utf-8") as file:               # 파일을 읽기 모드로 연다
        data = json.load(file)                               # JSON 글자를 파이썬 값으로 바꾼다
    return data                                              # 읽은 값을 리턴한다


def save_json(data, path):                                   # 저장할 값과 파일 경로를 받는 함수
    """값을 JSON 파일로 저장한다.
    실행 결과 상태와 감사 기록을 남길 때 쓴다.
    """
    with open(path, "w", encoding="utf-8") as file:          # 파일을 쓰기 모드로 연다
        json.dump(data, file, ensure_ascii=False, indent=2)  # 한글은 그대로, 줄을 나눠 저장한다
```

<h2><code>containment_store.py</code></h2>

Unit 4 파일입니다. 조치 기록 한 건을 만들고 조치 상태를 파일로 저장하고 읽습니다.

```python
import copy                                                           # 처음 상태를 복사해 쓰기 위해 copy 를 불러온다
from incident import load_json, save_json                             # Unit 1 파일의 파일 읽기 · 쓰기 함수를 불러온다

STATE_PATH = "containment_state.json"                                 # 연습용 시스템 상태를 저장할 파일 이름
LOG_PATH = "containment_log.json"                                     # 조치 기록을 저장할 파일 이름
INITIAL_STATE = {                                                     # 수업을 시작할 때의 연습용 시스템 상태
    "locked_users": ["junho"],                                        # 이미 잠겨 있는 계정 : junho 는 수업 전부터 잠겨 있다
    "blocked_ips": [],                                                # 차단한 IP 리스트 : 처음에는 비어 있다
    "block_expiry": {},                                               # IP 별 차단이 끝나는 시각(분) : 처음에는 비어 있다
    "clock": 0,                                                       # 연습용 시스템의 시계(분) : 0 에서 시작한다
    "sessions": {"dami": ["S-101", "S-102"], "seoyeon": ["S-201"], "gaeun": ["S-301"], "jiwoo": ["S-401"], "junho": ["S-501"], "hana": ["S-601"]},  # 계정별로 열려 있는 로그인 세션
}


def new_state():                                                      # 인자가 없는 함수
    """처음 상태를 복사해 새 연습용 시스템 상태를 리턴한다.
    실행할 때마다 같은 상태에서 시작해 결과를 비교할 때 쓴다.
    """
    return copy.deepcopy(INITIAL_STATE)                               # 처음 상태의 복사본을 리턴한다


def save_state(state):                                                # 연습용 시스템 상태를 받는 함수
    """상태를 파일에 저장한다.
    다음 프로그램이 이어서 읽을 수 있게 할 때 쓴다.
    """
    save_json(state, STATE_PATH)                                      # 상태를 JSON 파일로 저장한다


def load_state():                                                     # 인자가 없는 함수
    """저장해 둔 상태 파일을 읽어 리턴한다.
    저장이 제대로 됐는지 확인하거나 이어서 일할 때 쓴다.
    """
    return load_json(STATE_PATH)                                      # 상태 파일을 읽어 리턴한다


def reset_log():                                                      # 인자가 없는 함수
    """조치 기록 파일을 빈 리스트로 비운다.
    실행할 때마다 기록을 처음부터 쌓을 때 쓴다.
    """
    save_json([], LOG_PATH)                                           # 빈 리스트를 기록 파일로 저장한다


def make_record(action, target, incident_id, before, after, reason):  # 조치 이름 · 대상 · 인시던트 번호 · 조치 전 · 조치 후 · 이유를 받는 함수
    """조치 한 건(무엇을 · 누구에게 · 조치 전 · 조치 후 · 이유)의 기록을 딕셔너리로 만들어 리턴한다.
    조치 전과 후 상태를 함께 남겨 두고 싶을 때 쓴다.
    """
    record = {"action": action, "target": target, "incident": incident_id, "before": before, "after": after, "reason": reason}  # 조치 한 건의 기록을 딕셔너리로 만든다
    return record                                                     # 기록 한 건을 리턴한다


def append_log(record):                                               # 기록 한 건을 받는 함수
    """기록 파일을 읽어 기록 한 건을 더하고 다시 저장한다. 파일이 아직 없으면 빈 리스트로 시작한다.
    조치할 때마다 기록을 한 건씩 쌓아 둘 때 쓴다.
    """
    try:                                                              # 파일 읽기를 시도한다 — 미리 채운 줄
        log = load_json(LOG_PATH)                                     # 기록 파일을 읽는다 — 미리 채운 줄
    except FileNotFoundError:                                         # 파일이 없으면 — 미리 채운 줄
        log = []                                                      # 빈 리스트로 시작한다 — 미리 채운 줄
    log.append(record)                                                # 기록 한 건을 리스트에 추가한다
    save_json(log, LOG_PATH)                                          # 기록 파일로 다시 저장한다
```

<h2><code>account_actions.py</code></h2>

Unit 4 파일입니다. 계정을 잠그고 해제합니다.

```python
from containment_store import make_record                                             # 기록 한 건을 만드는 함수를 불러온다


def check_policy(user, vip_accounts):                                                 # 계정 이름과 VIP 계정 리스트를 받는 함수
    """자동으로 조치하면 안 되는 계정(VIP)이면 그 이유 문장을, 아니면 빈 글자("")를 리턴한다.
    경로에서 이미 걸렀어도 조치 함수가 마지막으로 한 번 더 막고 싶을 때 쓴다.
    """
    if user in vip_accounts:                                                          # VIP 계정이면
        return "VIP 계정이라 자동 조치 대상이 아님"                                   # 막는 이유를 리턴한다
    return ""                                                                         # 막을 이유가 없으면 빈 글자를 리턴한다 — 미리 채운 줄


def verify_locked(user, state):                                                       # 계정 이름과 연습용 시스템 상태를 받는 함수
    """계정이 잠긴 계정 리스트에 들어 있으면 True, 없으면 False 를 리턴한다.
    잠그라고 호출한 것과 실제로 잠긴 것이 같은지 조치 뒤에 확인할 때 쓴다.
    """
    return user in state["locked_users"]                                              # 잠긴 계정 리스트 안에 있는지 확인한 결과를 리턴한다


def lock_account(user, state, vip_accounts, incident_id, reason):                     # 계정 · 상태 · VIP 리스트 · 인시던트 번호 · 이유를 받는 함수
    """VIP 인지 먼저 확인하고 계정을 잠근 뒤, 실제로 잠겼는지 다시 확인해 조치 기록 한 건을 리턴한다.
    VIP 이거나 이미 잠겨 있으면 잠그지 않고 그 이유를 기록에 남긴다.
    """
    blocked = check_policy(user, vip_accounts)                                        # 자동 조치를 막을 이유를 구한다 — 미리 채운 줄
    if blocked != "":                                                                 # 막을 이유가 있으면 — 미리 채운 줄
        return make_record("계정 잠금", user, incident_id, "변경 없음", "변경 없음", blocked)  # 바꾸지 않고 이유를 기록한다 — 미리 채운 줄
    if user in state["locked_users"]:                                                 # 이미 잠겨 있으면 — 미리 채운 줄
        return make_record("계정 잠금", user, incident_id, "잠김", "잠김", "이미 잠겨 있어 변경 없음")  # 바꾸지 않고 기록한다 — 미리 채운 줄
    state["locked_users"].append(user)                                                # 잠긴 계정 리스트에 추가한다
    after = "잠김"                                                                    # 조치 뒤 상태 : 일단 잠겼다고 적고 — 미리 채운 줄
    if not verify_locked(user, state):                                                # 실제로 확인해 잠기지 않았으면 — 미리 채운 줄
        after = "잠기지 않음 (확인 실패)"                                             # 확인 실패라고 고쳐 적는다 — 미리 채운 줄
    return make_record("계정 잠금", user, incident_id, "잠기지 않음", after, reason)  # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄


def unlock_account(user, state, incident_id, reason):                                 # 계정 · 상태 · 인시던트 번호 · 이유를 받는 함수
    """잠긴 계정을 해제하고 실제로 해제됐는지 확인해 조치 기록 한 건을 리턴한다.
    오탐으로 확인된 계정을 되돌릴 때 쓴다.
    """
    if user not in state["locked_users"]:                                             # 잠겨 있지 않으면 — 미리 채운 줄
        return make_record("계정 해제", user, incident_id, "잠기지 않음", "잠기지 않음", "잠겨 있지 않아 변경 없음")  # 바꾸지 않고 기록한다 — 미리 채운 줄
    state["locked_users"].remove(user)                                                # 잠긴 계정 리스트에서 제거한다
    after = "잠기지 않음"                                                             # 조치 뒤 상태 : 일단 해제됐다고 적고 — 미리 채운 줄
    if verify_locked(user, state):                                                    # 실제로 확인해 아직 잠겨 있으면 — 미리 채운 줄
        after = "잠김 (확인 실패)"                                                    # 확인 실패라고 고쳐 적는다 — 미리 채운 줄
    return make_record("계정 해제", user, incident_id, "잠김", after, reason)         # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄
```

<h2><code>ip_actions.py</code></h2>

Unit 4 파일입니다. IP 를 차단하고 해제합니다.

```python
from containment_store import make_record                                                     # 기록 한 건을 만드는 함수를 불러온다

SHARED_IP_LIMIT = 2                                                                           # 한 IP 를 쓰는 계정이 이 수 이상이면 공유 IP 로 본다
DEFAULT_TTL = 120                                                                             # 차단을 유지하는 시간(분)


def is_in_allowlist(ip, allowlist_ips):                                                       # IP 와 허용 목록을 받는 함수
    """IP 가 허용 목록에 있으면 True, 없으면 False 를 리턴한다.
    협력사 사무실처럼 차단하면 안 되는 IP 를 걸러낼 때 쓴다.
    """
    return ip in allowlist_ips                                                                # 허용 목록 안에 있는지 확인한 결과를 리턴한다


def count_users_on_ip(ip, ip_users):                                                          # IP 와 IP 별 사용 계정 딕셔너리를 받는 함수
    """그 IP 를 쓰는 계정이 몇 개인지 리턴한다. ip_users.json 에 없는 IP 는 0 을 리턴한다.
    차단하면 정상 사용자가 몇 명 영향을 받는지 확인할 때 쓴다.
    """
    return len(ip_users.get(ip, []))                                                          # 그 IP 를 쓰는 계정 수를 리턴한다 (목록에 없으면 0)


def check_ip_policy(ip, allowlist_ips, ip_users):                                             # IP · 허용 목록 · 사용 계정 딕셔너리를 받는 함수
    """자동으로 차단하면 안 되는 IP 이면 그 이유 문장을, 아니면 빈 글자("")를 리턴한다.
    허용 목록 IP 이거나 여러 계정이 함께 쓰는 IP 를 차단하기 전에 가려낼 때 쓴다.
    """
    if is_in_allowlist(ip, allowlist_ips):                                                    # 허용 목록 IP 이면 — 미리 채운 줄
        return "허용 목록 IP 라서 차단하지 않음"                                              # 이유를 리턴한다 — 미리 채운 줄
    if count_users_on_ip(ip, ip_users) >= SHARED_IP_LIMIT:                                    # 여러 계정이 함께 쓰는 IP 이면 — 미리 채운 줄
        return "여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요"                               # 이유를 리턴한다 — 미리 채운 줄
    return ""                                                                                 # 막을 이유가 없으면 빈 글자를 리턴한다 — 미리 채운 줄


def block_ip(ip, state, incident_id, reason, ttl):                                            # IP · 상태 · 인시던트 번호 · 이유 · 유지 시간을 받는 함수
    """IP 를 차단하고 끝나는 시각을 적은 뒤, 실제로 차단됐는지 확인해 기록 한 건을 리턴한다.
    영구 차단 대신, 시간이 지나면 자동으로 풀리는 임시 차단을 만들 때 쓴다.
    """
    state["blocked_ips"].append(ip)                                                           # 차단한 IP 리스트에 추가한다
    state["block_expiry"][ip] = state["clock"] + ttl                                          # 차단이 끝나는 시각을 적는다
    after = "차단됨"                                                                          # 조치 뒤 상태 : 일단 차단됐다고 적고 — 미리 채운 줄
    if ip not in state["blocked_ips"]:                                                        # 실제로 확인해 차단되지 않았으면 — 미리 채운 줄
        after = "차단되지 않음 (확인 실패)"                                                   # 확인 실패라고 고쳐 적는다 — 미리 채운 줄
    return make_record("IP 차단", ip, incident_id, "차단되지 않음", after, reason + " (" + str(ttl) + "분 뒤 자동 해제)")  # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄


def unblock_ip(ip, state, incident_id, reason):                                               # IP · 상태 · 인시던트 번호 · 이유를 받는 함수
    """차단한 IP 를 풀고 끝나는 시각 기록도 지운 뒤 기록 한 건을 리턴한다.
    시간이 끝나서 풀거나 오탐으로 풀 때 쓴다.
    """
    state["blocked_ips"].remove(ip)                                                           # 차단 리스트에서 제거한다 — 미리 채운 줄
    state["block_expiry"].pop(ip)                                                             # 끝나는 시각 기록도 지운다 — 미리 채운 줄
    return make_record("IP 해제", ip, incident_id, "차단됨", "차단되지 않음", reason)         # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄


def expire_blocks(state, incident_id):                                                        # 상태와 인시던트 번호를 받는 함수
    """끝나는 시각이 지난 차단을 모두 풀고 해제 기록 리스트를 리턴한다.
    임시 차단이 사람 손 없이 풀리게 할 때 쓴다.
    """
    records = []                                                                              # 해제 기록을 담을 빈 리스트
    for ip in list(state["blocked_ips"]):                                                     # 차단 리스트의 복사본에서 IP 를 하나씩 꺼낸다 (원본을 바꾸며 돌면 안 되기 때문이다)
        end_time = state["block_expiry"][ip]                                                  # 그 IP 의 차단이 끝나는 시각 — 미리 채운 줄
        if end_time <= state["clock"]:                                                        # 끝나는 시각이 지났으면
            records.append(unblock_ip(ip, state, incident_id, "차단 시간이 끝나 자동 해제"))  # 차단을 풀고 해제 기록을 모은다
    return records                                                                            # 해제 기록 리스트를 리턴한다
```

<h2><code>undo_actions.py</code></h2>

Unit 5 파일입니다. 조치 기록 한 건을 거꾸로 되돌립니다.

```python
from account_actions import unlock_account  # 실습 8-1에 만든 계정 해제 함수를 불러온다
from ip_actions import unblock_ip           # 실습 8-2에 만든 IP 해제 함수를 불러온다


def undo_account(record, state):            # 되돌릴 조치 기록과 연습용 시스템 상태를 받는 함수
    """계정 잠금 기록 한 건을 되돌려 계정을 해제하고, 해제 기록을 리턴한다.
    자동으로 잠근 계정을 오탐이 확인된 뒤에 원래대로 풀 때 쓴다.
    """
    return unlock_account(record["target"], state, record["incident"], "되돌리기: " + record["reason"])  # 계정 해제를 실행하고 기록을 리턴한다


def undo_ip(record, state):                 # 되돌릴 조치 기록과 연습용 시스템 상태를 받는 함수
    """IP 차단 기록 한 건을 되돌려 IP 차단을 풀고, 해제 기록을 리턴한다.
    자동으로 차단한 IP 를 오탐이 확인된 뒤에 원래대로 풀 때 쓴다.
    """
    return unblock_ip(record["target"], state, record["incident"], "되돌리기: " + record["reason"])  # IP 해제를 실행하고 기록을 리턴한다


def undo_record(record, state):             # 되돌릴 조치 기록과 연습용 시스템 상태를 받는 함수
    """조치 종류(계정 잠금 · IP 차단)에 맞는 되돌리기 함수를 골라 불러서, 해제 기록을 리턴한다.
    기록 한 건을 받아 알맞은 방법으로 되돌릴 때 쓴다.
    """
    if record["action"] == "계정 잠금":     # 계정 잠금 기록이면 — 미리 채운 줄
        return undo_account(record, state)  # 계정을 해제한다 — 미리 채운 줄
    return undo_ip(record, state)           # 아니면 IP 차단 기록이므로 IP 를 해제한다 — 미리 채운 줄
```

<h2><code>rollback.py</code></h2>

Unit 5 파일입니다. 인시던트 한 건의 조치 기록을 찾아 되돌립니다.

```python
from containment_store import make_record                                    # 기록 한 건을 만드는 함수를 불러온다
from undo_actions import undo_record                                         # 방금 만든 되돌리기 함수를 불러온다

UNDOABLE_ACTIONS = ["계정 잠금", "IP 차단"]                                  # 해제로 되돌릴 수 있는 조치 이름


def find_incident_records(log, incident_id):                                 # 기록 리스트와 인시던트 번호를 받는 함수
    """기록 중 그 인시던트(알림 한 건)의 기록만 모은 뒤, 나중에 한 일이 먼저 오도록 순서를 뒤집어 리턴한다.
    조치를 거꾸로 되돌릴 때 쓴다.
    """
    found = []                                                               # 그 인시던트의 기록을 담을 빈 리스트
    for record in log:                                                       # 기록을 하나씩 꺼낸다
        action_name = record["action"]                                       # 기록의 조치 이름 — 미리 채운 줄
        if record["incident"] == incident_id:                                # 그 인시던트의 기록이면
            found.append(record)                                             # 모아 둔다
    return list(reversed(found))                                             # 순서를 뒤집어 리턴한다 — 미리 채운 줄


def should_undo(record):                                                     # 기록 한 건을 받는 함수
    """자동 조치가 실제로 바꾼 것이고 해제로 되돌릴 수 있으면 True, 아니면 False 를 리턴한다.
    조치 전부터 그 상태였던 것과 확인에 실패한 조치는 되돌리지 않으려고 쓴다.
    """
    if record["before"] == record["after"]:                                  # 조치 전과 후가 같으면
        return False                                                         # 바뀐 것이 없으니 되돌리지 않는다
    if "확인 실패" in record["after"]:                                       # 확인에 실패한 조치이면 — 미리 채운 줄
        return False                                                         # 실제로 바뀌지 않았으니 되돌리지 않는다 — 미리 채운 줄
    return record["action"] in UNDOABLE_ACTIONS                              # 해제로 되돌릴 수 있는 조치 종류인지의 결과를 리턴한다 — 미리 채운 줄


def rollback_incident(incident_id, log, state):                              # 인시던트 번호 · 기록 리스트 · 연습용 시스템 상태를 받는 함수
    """인시던트의 기록을 거꾸로 훑으며 자동이 바꾼 것만 되돌리고, 되돌릴 수 없는 조치는 따로 기록해 리턴한다.
    조치 전부터 있던 상태를 건드리지 않고 오탐을 복구할 때 쓴다.
    """
    records = []                                                             # 되돌리기 기록을 담을 빈 리스트
    for record in find_incident_records(log, incident_id):                   # 그 인시던트의 기록을 하나씩 꺼낸다
        if should_undo(record):                                              # 자동이 바꾼 것이고 되돌릴 수 있으면
            records.append(undo_record(record, state))                       # 되돌리고 해제 기록을 모은다
        if record["before"] != record["after"] and not should_undo(record):  # 바뀌었는데 되돌릴 수 없는 조치이면 — 미리 채운 줄
            note = "되돌릴 수 없는 조치(" + record["action"] + ") — 사용자가 다시 로그인해야 함"  # 이유 문장을 만들고 — 미리 채운 줄
            records.append(make_record("되돌리기 불가", record["target"], incident_id, record["before"], record["after"], note))  # 기록으로 남긴다 — 미리 채운 줄
    return records                                                           # 되돌리기 기록 리스트를 리턴한다
```

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError: No module named 'incident'` 는 <mark style="background:#ffc4d6">Unit 1에서 만든 `incident.py` 가 이 폴더에 없다는 뜻</mark>입니다. `No module named 'rollback'` 은 Unit 5 파일이 없다는 뜻입니다. 둘 다 위 「 이전 파일이 없을 때」의 코드 상자로 만듭니다.
- 먼저 오류 전체와 내가 친 명령을 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 그래도 막히면 맨 아래 「정답」을 봅니다. 그래도 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark style="background:#ffc4d6">**터미널**에서</mark> 합니다. 실행할 때마다 같은 입력 파일에서 시작해 같은 결과가 나옵니다.

---
