---
id: m5-u10-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/134_day06_am_soar_engine.md
  mission_id: GichanSource.m5-1116-am-soar-engine
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## Unit 10에서 만들 것: 통합 엔진과 정책 점검

<mark style="background:#e0d4ff">Unit 1~9에서는 플레이북 찾기(Unit 1) · 계정 잠금과 IP 차단(Unit 4) · 티켓(Unit 6) · 승인 게이트(Unit 8)</mark>를 단계마다 따로 구현했습니다. 이번 Unit에서는 <mark>**이 모듈들을 하나의 엔진으로 연결해 알림 한 건을 처음부터 끝까지 처리하고, 4과목의 탐지 결과를 입력으로 받아 실행하고, 엔진이 정책을 지켰는지 로그로 점검하는 부분**</mark>을 구현합니다. 통합 엔진(orchestration engine, 오케스트레이션 엔진: 여러 모듈을 정해진 순서로 호출해 하나의 흐름으로 실행하는 프로그램)은 SOAR(Security Orchestration, Automation and Response, 쏘아: 보안 오케스트레이션 · 자동화 · 대응) 제품의 핵심 부분입니다.

- **Exercise 10-1**: 알림 한 건을 <mark>플레이북 찾기 → 승인 게이트 → 조치 실행 → 티켓</mark> 순서로 처리하는 엔진을 만듭니다. 알림 하나에서 오류가 나도 그 알림만 실패(failure)로 기록하고 나머지 알림을 계속 처리합니다(`soar_engine.py`).
- **Exercise 10-2**: 4과목이 저장한 탐지 결과 `unit07_risk_scores.json` 을 엔진이 읽는 알림으로 바꾸고, 파일 모양을 엔진 앞에서 점검합니다. 엔진 실행 결과는 운영 요약(operations summary: 처리 결과별 알림 수 · 티켓 수 · 실제로 실행한 조치를 한 번에 보여 주는 요약)으로 정리합니다(`engine_input.py`). 종단간(end-to-end: 처음 입력부터 마지막 결과까지 중간에 끊기지 않고 한 흐름으로 이어지는 것) 연결입니다.
- **Exercise 10-3**: 엔진이 남긴 로그로 <mark>정책 준수 점검</mark>(policy compliance check: 승인 게이트와 허용 목록 같은 통제가 실제로 지켜졌는지 확인하는 일)을 하고, Unit 1~10 전체 회고 문서 `unit10_final_retrospective.md` 를 쓴 뒤 깃허브에 올립니다(`policy_check.py`).

새 문법은 Exercise 10-1의 `except Exception as error` 하나입니다. 이번 Unit에서는 판다스를 쓰지 않습니다. 보고서의 [핵심 질문] 표시가 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 들여쓰기(줄 앞의 빈칸)는 각 번호 주석과 같은 위치에서 시작합니다. 각 번호 주석 바로 아래에 직접 쓰고(Exercise 10-2 4번만 딕셔너리라서 여러 줄), 주석은 지우지 않습니다.

 **이전 파일**: 오늘 가져와 사용(import)하는 이전 파일은 아래 표와 같습니다. 없는 파일은 시작하기 뒤의 「이전 파일이 없을 때」 코드 상자로 만듭니다.

| 파일 | 만든 날 | 가져다 쓰는 것 | 쓰는 Exercise |
|---|---|---|---|
| `incident.py` | Unit 1 | `load_json` · `save_json` · `match_playbooks` | Exercise 10-1 · Exercise 10-2 · Exercise 10-3 |
| `config/playbook_registry.json` | Unit 1 | 플레이북 3개(`actions` · 트리거 규칙 · 최소 등급) | Exercise 10-1 · Exercise 10-2 |
| `containment_store.py` · `account_actions.py` · `ip_actions.py` | Unit 4 | `new_state` · `lock_account` · `block_ip` · `count_users_on_ip` | Exercise 10-1 |
| `ip_users.json` | Unit 4 | IP 별로 그 IP 를 쓰는 계정 리스트 | Exercise 10-1 |
| `ticketing.py` · `config/escalation_rules.json` | Unit 6 | `make_ticket` · 등급별 응답 기한(`sla_minutes`) | Exercise 10-1 |
| `approval_gate.py` · `config/approval_policy.json` | Unit 8 | `decide_gate` · 승인 정책 | Exercise 10-1 · Exercise 10-3 |
| `unit07_risk_scores.json` | 4과목 Unit 7 | 대상별 점수 · 등급 · 이유 5건 | Exercise 10-2 |

## 폴더 열고 파일 준비하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 5과목 폴더로 들어가 파일을 확인합니다. <mark>`ls` 결과에 `incident.py` · `approval_gate.py` · `ticketing.py` · `ip_users.json` 과 `config` 가 보이고, `ls config` 결과에 `playbook_registry.json` · `approval_policy.json` · `escalation_rules.json` 이 보이면</mark> 됩니다. Unit 4 파일 세 개(`containment_store.py` · `account_actions.py` · `ip_actions.py`)도 필요합니다. 없는 파일은 아래 「이전 파일이 없을 때」에서 만듭니다.
   ```bash
   pwd
   cd soar_response
   ls
   ls config
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. 이번 Unit에서 받은 파일 두 개(Unit 10 안내 문서, Unit 10 보고서)를 `soar_response` 폴더로 옮기고, 보고서 제목의 `이름` 을 내 이름으로 바꿉니다.
4. **[터미널]** Unit 1의 플레이북 등록 값을 점검합니다(맥북은 `python3`). 엔진은 이 파일의 `actions` · 트리거 규칙 · 최소 등급을 읽으므로, <mark>아래 출력과 같아야</mark> 이번 Unit의 출력이 문서와 일치합니다. 다르면 아래 「이전 파일이 없을 때」의 `config/playbook_registry.json` 으로 덮어씁니다.
   ```bash
   python -c "import json; print([(p['id'], p['trigger_rule'], p['min_grade'], p['actions']) for p in json.load(open('config/playbook_registry.json', encoding='utf-8'))])"
   ```
   ```
   [('PB-001', '퇴사한 계정', 'high', ['계정 잠금', '티켓 생성']), ('PB-002', '대량 다운로드', 'mid', ['담당자 알림', '티켓 생성']), ('PB-003', '경로 스캔', 'low', ['IP 차단', '티켓 생성'])]
   ```
5. **[터미널]** Exercise 10-1 데이터 파일을 만들고 **[VS Code]** 에서 열어 아래 내용을 붙여 넣습니다.
   ```bash
   touch engine_alerts.json
   ls
   ```

**`engine_alerts.json`** — 이번 Unit에서 들어온 알림 8건입니다.

- **무엇인가**:
  - Unit 1의 `incident_samples.json` 과 같은 알림 모양입니다. 키는 `id`(알림 번호) · `entity`(대상 계정 또는 IP) · `grade`(등급) · `score`(점수) · `reasons`(탐지된 규칙 이름 리스트) · `status`(상태)입니다.
  - 알림마다 다른 처리 경로를 지나도록 만든 시험용 데이터입니다. `INC-402` 는 `grade` 키가 없는 알림입니다.
  - `203.0.113.80` 은 허용 목록(allowlist, 얼라우리스트: 차단 대상에서 제외하기로 미리 정한 IP 의 목록)에 있는 협력사 사무실 IP 이고, `192.0.2.41` 은 `junho` 와 `hana` 가 함께 쓰는 IP 이며, `gaeun` 은 VIP 계정입니다.
- **어디에 쓰나**: Exercise 10-1 엔진이 알림을 하나씩 처리합니다.

```
[
  {"id": "INC-401", "entity": "dami", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-402", "entity": "hana", "score": 40, "reasons": ["업무 시간 밖 로그인"], "status": "탐지됨"},
  {"id": "INC-403", "entity": "198.51.100.45", "grade": "low", "score": 30, "reasons": ["경로 스캔"], "status": "탐지됨"},
  {"id": "INC-404", "entity": "203.0.113.80", "grade": "high", "score": 65, "reasons": ["경로 스캔"], "status": "탐지됨"},
  {"id": "INC-405", "entity": "192.0.2.41", "grade": "mid", "score": 35, "reasons": ["경로 스캔"], "status": "탐지됨"},
  {"id": "INC-406", "entity": "gaeun", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-407", "entity": "seoyeon", "grade": "mid", "score": 45, "reasons": ["대량 다운로드"], "status": "탐지됨"},
  {"id": "INC-408", "entity": "jiwoo", "grade": "mid", "score": 35, "reasons": ["업무 시간 밖 로그인"], "status": "탐지됨"}
]
```

6. **[터미널]** 파일이 정상인지 확인합니다(맥북은 `python3`). <mark>`8` 이 나와야</mark> 합니다.
   ```bash
   python -c "import json; print(len(json.load(open('engine_alerts.json', encoding='utf-8'))))"
   ```

## 이전 파일이 없을 때 (Unit 1 · 4 · 6 · 8 파일)

해당 요일에 결석했거나 파일을 지운 경우에만 만듭니다. **이미 있는 파일은 건너뜁니다.** 먼저 **[터미널]** 에서 빈 파일을 만듭니다. 이미 있는 파일은 `touch` 가 그대로 두고, `config` 폴더가 이미 있으면 `mkdir -p` 도 그대로 둡니다.

```bash
mkdir -p config
touch incident.py containment_store.py account_actions.py ip_actions.py ticketing.py approval_gate.py
touch ip_users.json config/playbook_registry.json config/approval_policy.json config/escalation_rules.json
ls
```

- 명령 풀이: `mkdir -p 폴더이름` 폴더가 없을 때만 만들기 · `touch 파일이름들` 빈 파일 만들기 · `ls` 폴더 안의 파일 이름 보기
- 아래 코드 상자를 **[VS Code]** 에서 같은 이름의 파일에 붙여 넣고 저장합니다. 이미 있는 파일은 붙여 넣지 않습니다(플레이북 등록 파일만 4번 점검 결과가 다를 때 덮어씁니다).

**`incident.py`** — Unit 1 파일에서 이번 Unit에서 쓰는 부분(`load_json` · `save_json` · `match_playbooks` 와 그 함수가 쓰는 `is_grade_enough`)만 담았습니다. Unit 1 파일 전체가 있으면 그것을 그대로 씁니다.

```python
import json                                                                   # JSON 파일을 읽고 쓰기 위해 json 을 불러온다

GRADE_ORDER = {"low": 1, "mid": 2, "high": 3}                                 # 등급을 크기를 비교할 수 있는 숫자로 바꾸는 딕셔너리


def load_json(path):                                                          # 파일 경로를 받는 함수
    """JSON 파일을 읽어 리스트나 딕셔너리로 리턴한다.
    인시던트와 플레이북 등록 파일을 읽을 때 쓴다.
    """
    with open(path, encoding="utf-8") as file:                                # 파일을 읽기 모드로 연다
        data = json.load(file)                                                # JSON 글자를 파이썬 값으로 바꾼다
    return data                                                               # 읽은 값을 리턴한다


def save_json(data, path):                                                    # 저장할 값과 파일 경로를 받는 함수
    """값을 JSON 파일로 저장한다.
    실행 결과 상태와 감사 기록을 남길 때 쓴다.
    """
    with open(path, "w", encoding="utf-8") as file:                           # 파일을 쓰기 모드로 연다
        json.dump(data, file, ensure_ascii=False, indent=2)                   # 한글은 그대로, 줄을 나눠 저장한다


def is_grade_enough(incident_grade, min_grade):                               # 인시던트 등급과 플레이북의 최소 등급을 받는 함수
    """인시던트 등급이 최소 등급 이상이면 True, 아니면 False 를 리턴한다.
    등급이 낮은 인시던트에 무거운 대응이 실행되지 않게 할 때 쓴다.
    """
    return GRADE_ORDER[incident_grade] >= GRADE_ORDER[min_grade]              # 등급을 숫자로 바꿔 비교한 결과를 리턴한다


def match_playbooks(incident, registry):                                      # 인시던트와 플레이북 리스트를 받는 함수
    """트리거 규칙과 조건 등급이 모두 맞는 플레이북을 리스트로 리턴한다.
    알림이 올 때 어떤 대응 절차를 쓸지 찾을 때 쓴다.
    """
    matched = []                                                              # 맞는 플레이북을 담을 빈 리스트
    for playbook in registry:                                                 # 플레이북을 하나씩 꺼낸다
        has_rule = playbook["trigger_rule"] in incident["reasons"]            # 트리거 규칙이 탐지된 규칙 리스트 안에 있는지 구한다
        grade_ok = is_grade_enough(incident["grade"], playbook["min_grade"])  # 인시던트 등급이 최소 등급 이상인지 구한다
        if has_rule and grade_ok:                                             # 트리거와 조건이 모두 맞으면
            matched.append(playbook)                                          # 맞는 플레이북을 리스트에 추가한다
    return matched                                                            # 맞는 플레이북 리스트를 리턴한다
```

**`config/playbook_registry.json`** — Unit 1의 플레이북 3개입니다. 이번 Unit의 엔진은 `trigger_rule` · `min_grade` · `actions` 만 읽습니다.

```
[
  {
    "id": "PB-001",
    "name": "퇴사한 계정의 서버 요청",
    "trigger_rule": "퇴사한 계정",
    "min_grade": "high",
    "actions": [
      "계정 잠금",
      "티켓 생성"
    ],
    "approval": "자동",
    "reason": "퇴사한 사람의 계정으로 서버에 요청이 오면 그 계정이 아직 사용할 수 있는 상태라는 뜻입니다. 퇴사한 사람이 쓰는 계정이 없으므로 잠가도 막히는 업무가 없습니다."
  },
  {
    "id": "PB-002",
    "name": "대량 다운로드",
    "trigger_rule": "대량 다운로드",
    "min_grade": "mid",
    "actions": [
      "담당자 알림",
      "티켓 생성"
    ],
    "approval": "담당자 승인 필요",
    "reason": "파일을 많이 내려받은 것은 업무 때문일 수도 있습니다. 사람이 확인하기 전에는 정상인지 알 수 없으므로 담당자가 허락한 뒤에 실행합니다."
  },
  {
    "id": "PB-003",
    "name": "경로 스캔",
    "trigger_rule": "경로 스캔",
    "min_grade": "low",
    "actions": [
      "IP 차단",
      "티켓 생성"
    ],
    "approval": "담당자 승인 필요",
    "reason": "경로 스캔의 대상은 사용자가 아니라 IP 입니다. 같은 IP 를 여러 사람이 쓰고 있으면 차단했을 때 정상 사용자의 업무도 막히므로, 담당자가 확인한 뒤에 차단합니다."
  }
]
```

**`containment_store.py`** — Unit 4 파일에서 이번 Unit에서 쓰는 부분(`new_state` · `make_record`)만 담았습니다. 조치 기록 한 건을 만들고 연습용 시스템의 처음 상태를 만듭니다. Unit 4 파일 전체가 있으면 그것을 그대로 씁니다.

```python
import copy                                                           # 처음 상태를 복사해 쓰기 위해 copy 를 불러온다

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


def make_record(action, target, incident_id, before, after, reason):  # 조치 이름 · 대상 · 인시던트 번호 · 조치 전 · 조치 후 · 이유를 받는 함수
    """조치 한 건(무엇을 · 누구에게 · 조치 전 · 조치 후 · 이유)의 기록을 딕셔너리로 만들어 리턴한다.
    조치 전과 후 상태를 함께 남겨 두고 싶을 때 쓴다.
    """
    record = {"action": action, "target": target, "incident": incident_id, "before": before, "after": after, "reason": reason}  # 조치 한 건의 기록을 딕셔너리로 만든다
    return record                                                     # 기록 한 건을 리턴한다
```

**`account_actions.py`** — Unit 4 파일에서 이번 Unit에서 쓰는 부분(`lock_account` 와 그 함수가 쓰는 `check_policy` · `verify_locked`)만 담았습니다. VIP 이면 잠그지 않고, 아니면 계정을 잠급니다.

```python
from containment_store import make_record                                             # 기록 한 건을 만드는 함수를 불러온다


def check_policy(user, vip_accounts):                                                 # 계정 이름과 VIP 계정 리스트를 받는 함수
    """자동으로 조치하면 안 되는 계정(VIP)이면 그 이유 문장을, 아니면 빈 글자("")를 리턴한다.
    경로에서 이미 `승인 필요` 로 보냈어도 조치 함수가 마지막으로 한 번 더 막고 싶을 때 쓴다.
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
```

**`ip_actions.py`** — Unit 4 파일에서 이번 Unit에서 쓰는 부분(`block_ip` · `count_users_on_ip` · `DEFAULT_TTL`)만 담았습니다. IP 를 차단하고, 그 IP 를 쓰는 계정 수를 셉니다.

```python
from containment_store import make_record             # 기록 한 건을 만드는 함수를 불러온다

DEFAULT_TTL = 120                                     # 차단을 유지하는 시간(분)


def count_users_on_ip(ip, ip_users):                  # IP 와 IP 별 사용 계정 딕셔너리를 받는 함수
    """그 IP 를 쓰는 계정이 몇 개인지 리턴한다. ip_users.json 에 없는 IP 는 0 을 리턴한다.
    차단하면 정상 사용자가 몇 명 영향을 받는지 확인할 때 쓴다.
    """
    return len(ip_users.get(ip, []))                  # 그 IP 를 쓰는 계정 수를 리턴한다 (목록에 없으면 0)


def block_ip(ip, state, incident_id, reason, ttl):    # IP · 상태 · 인시던트 번호 · 이유 · 유지 시간을 받는 함수
    """IP 를 차단하고 끝나는 시각을 적은 뒤, 실제로 차단됐는지 확인해 기록 한 건을 리턴한다.
    영구 차단 대신, 시간이 지나면 자동으로 풀리는 임시 차단을 만들 때 쓴다.
    """
    state["blocked_ips"].append(ip)                   # 차단한 IP 리스트에 추가한다
    state["block_expiry"][ip] = state["clock"] + ttl  # 차단이 끝나는 시각을 적는다
    after = "차단됨"                                  # 조치 뒤 상태 : 일단 차단됐다고 적고 — 미리 채운 줄
    if ip not in state["blocked_ips"]:                # 실제로 확인해 차단되지 않았으면 — 미리 채운 줄
        after = "차단되지 않음 (확인 실패)"           # 확인 실패라고 고쳐 적는다 — 미리 채운 줄
    return make_record("IP 차단", ip, incident_id, "차단되지 않음", after, reason + " (" + str(ttl) + "분 뒤 자동 해제)")  # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄
```

**`ip_users.json`** — Unit 4 파일입니다. IP 별로 그 IP 를 쓰는 계정 리스트입니다.

```
{"203.0.113.80": ["seoyeon", "jiwoo"], "192.0.2.41": ["junho", "hana"]}
```

**`ticketing.py`** — Unit 6 파일입니다. 알림 한 건으로 티켓 한 장을 만듭니다.

```python
DEFAULT_NEXT_STEP = "담당자가 알림 내용을 읽고 필요한 일을 정한다"                      # 알림 상태를 모를 때 쓰는 다음 할 일
MANUAL_STEP = "조치가 확인되지 않았다. 담당자가 직접 계정이나 IP 상태를 보고 조치한다"  # 조치 확인에 실패한 티켓의 다음 할 일
NEXT_STEPS = {                                                                          # 알림 상태마다 담당자가 할 다음 일
    "조치됨": "조치 결과가 맞는지 확인하고 계정이나 IP 상태를 점검한다",                # 자동 조치가 끝난 알림
    "승인 대기": "승인할지 거절할지 정하고 정한 사람의 이름을 남긴다",                  # 승인을 기다리는 알림
    "조치 없음": "자동 조치가 없는 알림이니 직접 보고 조치가 필요한지 정한다",          # 자동 조치 대상이 아닌 알림
}


def make_title(alert):                                                                  # 알림 한 건을 받는 함수
    """티켓 제목(등급 · 대상 · 규칙)을 문자열로 만들어 리턴한다.
    티켓 목록에서 제목만 봐도 무슨 일인지 알 수 있게 할 때 쓴다.
    """
    grade = alert["grade"]                                                              # 알림 등급 — 미리 채운 줄
    entity = alert["entity"]                                                            # 알림 대상(사용자 이름 또는 IP) — 미리 채운 줄
    rule = alert["rule"]                                                                # 탐지된 규칙 이름 — 미리 채운 줄
    return "[" + grade + "] " + entity + " — " + rule                                   # 등급 · 대상 · 규칙을 이어 붙인 제목을 리턴한다


def find_next_step(alert, next_steps):                                                  # 알림 한 건과 다음 할 일 딕셔너리를 받는 함수
    """알림 상태에 맞는 다음 할 일 문장을 리턴한다. 정해 둔 문장이 없으면 기본 문장을 리턴한다.
    담당자가 티켓을 열자마자 무엇부터 할지 알게 할 때 쓴다.
    """
    status = alert["status"]                                                            # 알림 상태(조치됨 · 승인 대기 · 조치 없음) — 미리 채운 줄
    return next_steps.get(status, DEFAULT_NEXT_STEP)                                    # 상태에 맞는 다음 할 일을 리턴한다 (없으면 기본 문장)


def has_failed_action(done_list):                                                       # 조치 내역 문장 리스트를 받는 함수
    """조치 내역에 「확인 실패」가 들어 있는 문장이 하나라도 있으면 True, 없으면 False 를 리턴한다.
    조치했다고 했지만 실제로 바뀌지 않은 알림을 사람이 직접 보게 할 때 쓴다.
    """
    for text in done_list:                                                              # 조치 내역 문장을 하나씩 읽는다 — 미리 채운 줄
        if "확인 실패" in text:                                                         # 문장 안에 확인 실패가 있으면
            return True                                                                 # 확인 실패가 있다고 True 를 리턴한다
    return False                                                                        # 하나도 없으면 False 를 리턴한다 — 미리 채운 줄


def make_ticket(alert, ticket_no, rules, next_steps):                                   # 알림 · 티켓 번호 · 규칙 · 다음 할 일 딕셔너리를 받는 함수
    """알림 한 건으로 티켓 한 장(딕셔너리)을 만들어 리턴한다. 만든 시각과 응답 기한(SLA)을 함께 적는다.
    알림이 오면 바로 담당자가 읽을 수 있는 티켓을 만들 때 쓴다.
    """
    sla_table = rules["sla_minutes"]                                                    # 등급마다 정한 응답 기한(분) 표 — 미리 채운 줄
    sla_minutes = sla_table[alert["grade"]]                                             # 이 알림 등급의 응답 기한(분)을 꺼낸다
    sla_due = alert["minute"] + sla_minutes                                             # 알림이 온 시각 + 응답 기한 = 응답해야 하는 시각
    needs_manual = has_failed_action(alert["done"])                                     # 조치 확인에 실패한 내역이 있는지 — 미리 채운 줄
    next_step = find_next_step(alert, next_steps)                                       # 다음 할 일 문장 — 미리 채운 줄
    if needs_manual:                                                                    # 확인 실패가 있으면 — 미리 채운 줄
        next_step = MANUAL_STEP                                                         # 직접 확인하라는 문장으로 바꾼다 — 미리 채운 줄
    ticket = {                                                                          # 티켓 한 장 — 미리 채운 줄
        "id": "TCK-" + str(ticket_no),                                                  # 티켓 번호
        "title": make_title(alert),                                                     # 제목
        "entity": alert["entity"],                                                      # 대상
        "rule": alert["rule"],                                                          # 규칙
        "grade": alert["grade"],                                                        # 등급
        "playbook": alert["playbook"],                                                  # 실행한 플레이북
        "done": alert["done"],                                                          # 조치 내역
        "status": "열림",                                                               # 티켓 상태 : 처음에는 열림
        "next_step": next_step,                                                         # 다음 할 일
        "needs_manual": needs_manual,                                                   # 직접 확인이 필요한지
        "created_at": alert["minute"],                                                  # 만든 시각(분)
        "updated_at": alert["minute"],                                                  # 마지막으로 갱신한 시각(분)
        "sla_due": sla_due,                                                             # 응답 기한 시각(분)
        "count": 1,                                                                     # 합쳐진 알림 수 : 처음에는 1
        "incidents": [alert["id"]],                                                     # 합쳐진 알림 번호
        "notified_count": 0,                                                            # 알림을 보낸 횟수
        "last_notified": -1,                                                            # 마지막으로 알림을 보낸 시각(분) : 아직 없음
        "acked_at": -1,                                                                 # 담당자가 처음 확인한 시각(분) : 아직 없음
        "resolved_at": -1,                                                              # 해결한 시각(분) : 아직 없음
        "escalation_level": 0,                                                          # 상급자에게 올린 단계 : 아직 없음
        "comments": [],                                                                 # 상태를 바꾼 기록
    }
    return ticket                                                                       # 만든 티켓을 리턴한다
```

**`config/escalation_rules.json`** — Unit 6 파일입니다. 이번 Unit에서는 등급별 응답 기한(`sla_minutes`)만 읽습니다.

```
{
  "sla_minutes": {"high": 15, "mid": 60, "low": 240},
  "recipients": {
    "high": ["kim.sec", "lee.soc", "team.lead"],
    "mid": ["kim.sec", "lee.soc"],
    "low": ["kim.sec"]
  },
  "merge_window_minutes": 60,
  "send_gap_minutes": 30,
  "alert_url": "http://127.0.0.1:5001/alert",
  "escalation_steps": [
    {"overdue_minutes": 0, "notify": "team.lead"},
    {"overdue_minutes": 30, "notify": "soc.head"}
  ]
}
```

**`approval_gate.py`** — Unit 8 파일입니다. 조치 요청 한 건을 자동 · 승인 필요 · 차단 금지로 정합니다.

```python
def is_allowlisted(request, policy):                                        # 조치 요청 한 건과 승인 정책을 받는 함수
    """조치 대상이 허용 목록에 있으면 True, 없으면 False 를 리턴한다.
    협력사 사무실이나 점검 서버처럼 지금 정책에서 차단하지 않기로 등록한 대상을 먼저 가려낼 때 쓴다.
    """
    return request["target"] in policy["allowlist_ips"]                     # 대상이 허용 목록에 있는지의 결과를 리턴한다


def risk_score(request, policy):                                            # 조치 요청 한 건과 승인 정책을 받는 함수
    """등급 · VIP · 함께 쓰는 IP · 대상 수로 위험 점수를 더하고, 점수와 이유 리스트를 함께 리턴한다.
    자동으로 실행해도 되는 요청인지 숫자로 판단할 때 쓴다.
    """
    grade_table = policy["grade_points"]                                    # 등급마다 정한 점수 표 — 미리 채운 줄
    score = grade_table[request["grade"]]                                   # 이 요청 등급의 점수로 시작한다
    reasons = ["등급 " + request["grade"] + " +" + str(score)]              # 점수를 더한 이유 리스트 — 미리 채운 줄
    if request["target"] in policy["vip_accounts"]:                         # 대상이 VIP 계정이면
        score = score + policy["vip_points"]                                # VIP 점수를 더한다
        reasons.append("VIP 계정 +" + str(policy["vip_points"]))            # 이유를 추가한다 — 미리 채운 줄
    if request["users_on_ip"] >= policy["shared_ip_limit"]:                 # 여러 계정이 함께 쓰는 IP 이면 — 미리 채운 줄
        score = score + policy["shared_ip_points"]                          # 함께 쓰는 IP 점수를 더한다 — 미리 채운 줄
        reasons.append("함께 쓰는 IP +" + str(policy["shared_ip_points"]))  # 이유를 추가한다 — 미리 채운 줄
    if request["target_count"] > policy["many_targets_limit"]:              # 한 번에 조치할 대상이 많으면 — 미리 채운 줄
        score = score + policy["many_targets_points"]                       # 대상 수 점수를 더한다 — 미리 채운 줄
        reasons.append("대상 " + str(request["target_count"]) + "개 +" + str(policy["many_targets_points"]))  # 이유를 추가한다 — 미리 채운 줄
    return score, reasons                                                   # 점수와 이유 리스트를 함께 리턴한다 — 미리 채운 줄


def decide_gate(request, policy):                                           # 조치 요청 한 건과 승인 정책을 받는 함수
    """조치 요청 한 건을 「차단 금지」 · 「승인 필요」 · 「자동」 가운데 하나로 정하고, 결정과 이유 리스트를 함께 리턴한다.
    자동 대응이 조치를 실행하기 직전에, 사람의 승인이 필요한지 정할 때 쓴다.
    """
    if is_allowlisted(request, policy):                                     # 허용 목록 대상이면
        return "차단 금지", ["허용 목록 대상"]                              # 결정과 이유를 함께 리턴한다 — 미리 채운 줄
    score, reasons = risk_score(request, policy)                            # 위험 점수와 이유 리스트를 함께 받는다
    reasons.append("합계 " + str(score) + "점")                             # 합계 점수를 이유에 추가한다 — 미리 채운 줄
    if score >= policy["approval_score"]:                                   # 승인 기준 점수 이상이면
        return "승인 필요", reasons                                         # 결정과 이유를 함께 리턴한다 — 미리 채운 줄
    return "자동", reasons                                                  # 기준보다 낮으면 자동으로 실행한다 — 미리 채운 줄
```

**`config/approval_policy.json`** — Unit 8 파일입니다. 승인 게이트의 점수 기준입니다.

```
{
  "allowlist_ips": ["203.0.113.80", "192.0.2.10"],
  "vip_accounts": ["gaeun"],
  "grade_points": {"high": 2, "mid": 1, "low": 0},
  "vip_points": 3,
  "shared_ip_points": 2,
  "shared_ip_limit": 2,
  "many_targets_points": 2,
  "many_targets_limit": 3,
  "approval_score": 3
}
```

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError: No module named 'approval_gate'` 처럼 `No module named` 이 나오면 <mark style="background:#ffc4d6">그 이름의 파일이 이 폴더에 없다는 뜻</mark>입니다. 위 「이전 파일이 없을 때」의 코드 상자로 만듭니다.
- `FileNotFoundError` 가 나오면 오류 문장에 적힌 파일(`ip_users.json` · `config/playbook_registry.json` · `config/approval_policy.json` · `config/escalation_rules.json`)이 그 위치에 없는 것입니다. `ls` 와 `ls config` 로 확인한 뒤 위 「이전 파일이 없을 때」의 코드 상자로 만듭니다.
- `json.decoder.JSONDecodeError` 가 나오면 붙여 넣은 JSON 파일에서 쉼표나 괄호가 빠졌거나 남은 것입니다. 오류 문장의 `line` 숫자 근처를 확인하고, 모르겠으면 파일 내용을 모두 지운 뒤 문서의 코드 상자를 다시 붙여 넣습니다.
- 먼저 오류 전체와 내가 친 명령을 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 그래도 막히면 맨 아래 「정답」을 봅니다. 그래도 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark style="background:#ffc4d6">**터미널**에서</mark> 합니다. 실행할 때마다 같은 입력 파일에서 시작해 같은 결과가 나옵니다.
---
