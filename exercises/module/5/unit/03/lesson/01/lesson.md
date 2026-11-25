---
id: m5-u03-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표와 오늘의 계획

Unit 2 실습 2-1 · 2-2에서는 계정 잠금과 세션 종료(세션, session: 로그인한 뒤 서버에 이어져 있는 접속 상태)를 실행하고, 조치 전 · 후 상태를 기록으로 남겼습니다. 오늘은 그 기록을 써서 두 가지를 합니다. 오탐으로 확인된 조치는 **안전하게 되돌리고**(롤백, rollback: 조치 이전 상태로 복원하는 일), 알림은 담당자가 바로 읽을 수 있는 **티켓**으로 남깁니다.

**오늘의 계획 (약 2시간 40분)**

| 순서 | 시간 | 하는 일 |
|---|---|---|
| 1. 시작 | 15분 | 앞 Unit 파일 확인, 알림 · 설정 파일 만들기 |
| 2. 결과 기록 준비 | 5분 | 핵심 실습의 실행 결과 기록 틀 만들기 |
| 3. 핵심 실습 | 약 100분 | 실습 3-1 · 3-2 |
| 4. 포트폴리오 기록 | 20분 | 문제와 해결 근거를 세 문장 글로 남기기 |
| 5. 선택 과제 | 남는 시간 | 티켓 병합 · 알림 기능 실습 |

- 시작은 이 레슨을 읽으며 합니다.
- 결과 기록 틀을 먼저 만들고, 실행 뒤 출력과 최종 상태를 붙여 넣습니다.
- 핵심 실습이 끝나면 문제를 해결한 근거를 포트폴리오 글로 남깁니다.
- 선택 과제용 함수 준비와 응용은 핵심 실습과 포트폴리오 기록을 마친 뒤 합니다.
- 하루 3시간에서 남는 20분쯤은 밀린 곳을 따라잡는 여유 시간입니다.

**오늘 다룰 것**

1. **실습 3-1**: 오탐으로 확인된 알림의 조치를 기록을 보고 되돌립니다. <mark>자동이 바꾼 것만</mark> 되돌리고, 되돌릴 수 없는 조치(세션 종료)는 따로 표시합니다(`undo_actions.py` · `rollback.py`). 직접 쓰는 곳은 `rollback.py` 의 빈칸 두 곳(① · ②)입니다.
2. **실습 3-2**: 알림 한 건으로 담당자가 바로 판단할 수 있는 **티켓을 생성**(ticketing, 티케팅: 알림을 추적 가능한 티켓으로 등록하는 일)합니다. 티켓에는 응답 기한(SLA: 알림을 받은 뒤 담당자가 몇 분 안에 응답해야 하는지 정한 시간)을 계산해 적고, 사후 검증(조치 뒤 실제 상태를 다시 조회해 확인하는 일)에 실패한 조치는 직접 확인 대상으로 따로 표시합니다(`ticketing.py`). 직접 쓰는 곳은 응답 기한을 계산하는 빈칸 두 곳(① · ②)입니다.

**응용 3-1 ~ 3-3은 여유가 되면 해 보세요.** 핵심 실습 두 개와 글쓰기를 마치고 시간이 남을 때 합니다.

| 응용 | 하는 일 |
|---|---|
| 응용 3-1 | 알림 8건을 한 번에 처리하고 근무 보고를 만든다 |
| 응용 3-2 | 같은 사건의 알림을 티켓 한 장으로 **병합**(merge)하고 티켓 상태를 바꾼다 |
| 응용 3-3 | 등급에 맞는 담당자에게 알림을 보내고, 실패하면 다시 보낸다 |

선택 과제용 병합 · 알림 함수는 핵심 실습을 마친 뒤 준비합니다. 핵심 실습은 이 선택 과제에 의존하지 않습니다.

핵심 실습에는 새 문법이 없습니다(미리 채운 줄의 `reversed` · `str()` 은 나오는 페이지에서 풀어 줍니다). 기술 결과 기록에는 실행 출력과 최종 상태를 남기고, 포트폴리오 글에는 문제를 해결한 근거와 판단을 씁니다. 코드를 쓸 때는 들여쓰기를 미리 채운 줄에 맞추고, 각 번호 주석(① · ②) 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

> **확인** — 시작 → 결과 기록 틀 → 핵심 실습 → 포트폴리오 글 → 선택 과제 순서를 말할 수 있으면 성공입니다.

## 폴더 열고 이전 파일 확인하기

오늘 코드는 앞 Unit 파일을 `import` 로 불러 씁니다. 먼저 `soar_response` 폴더에 아래 파일이 있는지 봅니다.

| 파일 | 만든 곳 | 담긴 것 |
|---|---|---|
| `incident.py` | Unit 1 실습 1-2 | `load_json` · `save_json` |
| `containment_store.py` | Unit 2 실습 2-1 | `load_state` · `make_record` · `LOG_PATH` |
| `account_actions.py` | Unit 2 실습 2-1 | `unlock_account` |
| `audit.py` | M5 Unit 2 「응용과 Unit 3에 필요한 처리 함수 준비」 | `ip_actions.py` 가 조치 결과를 기록할 때 사용하는 `log_line` |
| `ip_actions.py` | M5 Unit 2 「응용과 Unit 3에 필요한 처리 함수 준비」 | `block_ip` · `unblock_ip` · `DEFAULT_TTL` |
| `containment_state.json` | 실습 2-2 실행 결과 | 잠긴 계정 같은 연습용 시스템 상태 |
| `containment_log.json` | 실습 2-2 실행 결과 | 조치 기록 5건 |

실습 3-1이 실습 2-2 결과 파일 두 개를 읽습니다.

**순서**

1. **[VS Code]** 왼쪽 목록의 `network-study-notes` 안에 있는 `soar_response` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다. 이렇게 열면 터미널이 처음부터 `soar_response` 에 있습니다.
2. **[터미널]** `soar_response` 폴더에 있는지 보고 파일을 확인합니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. **[터미널]** 앞 Unit 파일을 불러올 수 있는지 확인합니다. <mark>`앞 Unit 파일 정상` 이 나와야</mark> 합니다.
   ```bash
   python - <<'PY'
from incident import load_json, save_json
from containment_store import load_state, make_record, LOG_PATH
from account_actions import unlock_account
from ip_actions import block_ip, unblock_ip, DEFAULT_TTL

print('앞 Unit 파일 정상')
PY
   ```
   - `ModuleNotFoundError` 나 `ImportError` 가 나오면 다음 페이지 「이전 파일이 없을 때」를 봅니다.

<!-- checklist -->
- [ ] `soar_response` 폴더에서 3번 명령을 실행해 `앞 Unit 파일 정상` 이 나왔다
<!-- /checklist -->

4. **[터미널]** 실습 2-2 결과 파일이 맞는지 확인합니다. <mark>`['junho', 'dami'] 5` 가 나와야</mark> 합니다.
   ```bash
   python - <<'PY'
import json

with open('containment_state.json', encoding='utf-8') as file:
    state = json.load(file)
with open('containment_log.json', encoding='utf-8') as file:
    log = json.load(file)
print(state['locked_users'], len(log))
PY
   ```
   - `['junho'] 4` 가 나오면 실습 2-1만 실행하고 실습 2-2 실행 파일은 아직 실행하지 않았거나, Unit 2 실습 2-2 실행 파일을 아직 실행하지 않은 것입니다. `python exercise2-2_run.py` 를 한 번 실행한 뒤 다시 확인합니다.
   - `FileNotFoundError` 가 나오면 다음 페이지 「이전 파일이 없을 때」의 두 상자로 파일을 만듭니다.

<!-- checklist -->
- [ ] 4번 명령을 실행해 `['junho', 'dami'] 5` 가 나왔다
<!-- /checklist -->

5. **코드는 각 실습의 코드 상자에서 작성합니다.**
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S` 로 저장합니다.
   - 기술 실행 결과 기록 `report_u3.md` 는 「핵심 실습 결과 기록 준비」 레슨의 틀을 복사해 만듭니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. **앞 Unit 파일은 고치지 않습니다.** 실습 3-1 실행 파일은 두 결과 파일을 읽기만 하고 다시 저장하지 않아서, 몇 번을 실행해도 같은 결과가 나옵니다.

> **확인** — 3번에서 `앞 Unit 파일 정상`, 4번에서 `['junho', 'dami'] 5` 가 나오면 성공입니다. 안 나오면 다음 페이지 「이전 파일이 없을 때」를 봅니다.

## 이전 파일이 없을 때

앞 페이지의 확인에서 오류가 난 파일만 만듭니다. **이미 있는 파일은 건너뜁니다.**

**파이썬 파일** — 앞 Unit 레슨의 코드 상자로 만들고, 빈칸은 그 Unit 해당 실습 아래의 정답 펼침의 채운 코드로 채웁니다.

| 파일 | 만드는 레슨 |
|---|---|
| `containment_store.py` · `account_actions.py` | Unit 2 실습 2-1 레슨 |
| `audit.py` · `ip_actions.py` | M5 Unit 2 「응용과 Unit 3에 필요한 처리 함수 준비」 |
| `incident.py` | Unit 1 실습 1-2 레슨 |

Unit 1 파일이 아예 없으면 `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `incident.py` 를 만들고, 오늘 쓰는 두 함수만 담은 아래 상자를 붙여 넣어도 핵심 실습 두 개를 할 수 있습니다. 선택 과제 3-1은 Unit 1 파일 전체가 있어야 합니다.

**`incident.py`** — Unit 1 파일에서 오늘 쓰는 두 함수(`load_json` · `save_json`)만 담았습니다. Unit 1 파일 전체가 있으면 그것을 그대로 씁니다.

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

**실습 2-2 결과 파일** — Unit 2 파일이 있으면 `python exercise2-2_run.py` 를 한 번 실행하는 것이 가장 쉽습니다. 실습 2-2를 하지 못했다면 `soar_response` 폴더에 `containment_state.json` 과 `containment_log.json` 을 만들고 아래 두 상자를 하나씩 붙여 넣고 저장합니다. 실습 2-2 실행 파일이 저장하는 내용과 같습니다.

**`containment_state.json`** — 실습 2-2가 끝난 뒤의 연습용 시스템 상태입니다. `junho` 는 수업 전부터, `dami` 는 실습 2-2에서 잠겼고, 두 계정의 세션은 모두 종료됐습니다.

```
{"locked_users": ["junho", "dami"], "blocked_ips": [], "block_expiry": {}, "clock": 0, "sessions": {"dami": [], "seoyeon": ["S-201"], "gaeun": ["S-301"], "jiwoo": ["S-401"], "junho": [], "hana": ["S-601"]}}
```

**`containment_log.json`** — 실습 2-2가 남긴 조치 기록 5건입니다. 기록마다 조치 전(`before`)과 조치 후(`after`) 상태가 들어 있습니다.

```
[
  {"action": "계정 잠금", "target": "dami", "incident": "INC-001", "before": "잠기지 않음", "after": "잠김", "reason": "퇴사한 계정의 서버 요청"},
  {"action": "세션 종료", "target": "dami", "incident": "INC-001", "before": "세션 2개", "after": "세션 0개", "reason": "퇴사한 계정의 서버 요청"},
  {"action": "계정 잠금", "target": "gaeun", "incident": "INC-003", "before": "변경 없음", "after": "변경 없음", "reason": "VIP 계정이라 자동 조치 대상이 아님"},
  {"action": "계정 잠금", "target": "junho", "incident": "INC-006", "before": "잠김", "after": "잠김", "reason": "이미 잠겨 있어 변경 없음"},
  {"action": "세션 종료", "target": "junho", "incident": "INC-006", "before": "세션 1개", "after": "세션 0개", "reason": "퇴사 처리 확인"}
]
```

<!-- checklist -->
- [ ] 앞 페이지 확인에서 오류가 난 파일만 `soar_response` 폴더에 만들었다(오류가 없었으면 건너뛰고 체크)
<!-- /checklist -->

다 만들었으면 앞 페이지의 3 · 4번 확인을 다시 합니다.

> **확인** — 앞 페이지 3번에서 `앞 Unit 파일 정상`, 4번에서 `['junho', 'dami'] 5` 가 나오면 성공입니다. 그래도 오류가 나면 마지막 페이지 「오류가 나면」의 표에서 같은 오류 줄을 찾습니다.

<!-- checklist -->
- [ ] 앞 페이지 3 · 4번 확인을 다시 해 두 줄이 모두 그대로 나왔다
<!-- /checklist -->

## 알림 데이터와 설정 파일 만들기

실습 3-2가 읽는 데이터 파일 두 개를 만듭니다. 응용 3-2 · 3-3도 같은 파일을 읽습니다.

1. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `alerts_thu.json` 을, `soar_response` 폴더 안의 `config` 폴더를 오른쪽 클릭 › **New File** 로 `escalation_rules.json`(`config/escalation_rules.json`)을 만들고, 아래 두 상자를 하나씩 붙여 넣고 저장합니다.
   - `config` 폴더가 없으면 `soar_response` 폴더의 터미널에서 `mkdir -p config` 로 만듭니다.
2. **[터미널]** 아래 두 상자를 파일로 저장한 뒤, 파일이 정상인지 확인합니다. <mark>`11 6` 이 나와야</mark> 합니다(알림이 11건, 규칙 파일의 키가 6개라는 뜻입니다).
   ```bash
   python - <<'PY'
import json

with open('alerts_thu.json', encoding='utf-8') as file:
    alerts = json.load(file)
with open('config/escalation_rules.json', encoding='utf-8') as file:
    rules = json.load(file)
print(len(alerts), len(rules))
PY
   ```

**`alerts_thu.json`** — 오늘 근무 3시간 동안 들어온 알림 11건입니다.

- **어디에 쓰나**: 실습 3-2 · 응용 3-2 · 응용 3-3 실행 파일이 이 파일을 읽어 알림을 하나씩 처리합니다.

알림 한 건의 키는 아래와 같습니다. 위 다섯 개는 알림 정보이고, 아래 세 개는 처리 정보입니다.

| 키 | 뜻 |
|---|---|
| `id` | 알림 번호 |
| `minute` | 알림 수신 시각 |
| `entity` | 대상(사용자 이름 또는 IP) |
| `rule` | 탐지 규칙 |
| `grade` | 심각도 등급(severity) |
| `status` | 알림 처리 상태 |
| `playbook` | 실행한 플레이북(playbook: 알림 유형별로 정해 둔 대응 절차) |
| `done` | 이미 수행한 조치 내역을 문장으로 적은 리스트 |

`minute` 은 근무를 시작한 때를 0분으로 센 분 단위 숫자입니다. `INC-201` 은 0분, `INC-211` 은 160분에 왔습니다.

```
[
  {"id": "INC-201", "minute": 0, "entity": "dami", "rule": "퇴사한 계정", "grade": "high", "status": "조치됨", "playbook": "PB-001", "done": ["계정 잠금: 잠기지 않음 → 잠김", "세션 종료: 세션 2개 → 세션 0개"]},
  {"id": "INC-202", "minute": 3, "entity": "198.51.100.90", "rule": "경로 스캔", "grade": "low", "status": "조치됨", "playbook": "PB-003", "done": ["IP 차단: 차단되지 않음 → 차단됨"]},
  {"id": "INC-203", "minute": 8, "entity": "gaeun", "rule": "규칙은 허용인데 서버가 거절", "grade": "mid", "status": "승인 대기", "playbook": "VIP 확인", "done": []},
  {"id": "INC-204", "minute": 12, "entity": "seoyeon", "rule": "대량 다운로드", "grade": "mid", "status": "승인 대기", "playbook": "PB-002", "done": []},
  {"id": "INC-205", "minute": 14, "entity": "dami", "rule": "퇴사한 계정", "grade": "high", "status": "조치됨", "playbook": "PB-001", "done": ["계정 잠금: 잠김 → 잠김 (이미 잠겨 있어 변경 없음)"]},
  {"id": "INC-206", "minute": 20, "entity": "198.51.100.90", "rule": "경로 스캔", "grade": "low", "status": "조치됨", "playbook": "PB-003", "done": ["IP 차단: 차단됨 → 차단됨 (이미 차단되어 변경 없음)"]},
  {"id": "INC-207", "minute": 30, "entity": "203.0.113.250", "rule": "경로 스캔", "grade": "low", "status": "조치됨", "playbook": "PB-003", "done": ["IP 차단: 차단되지 않음 → 차단되지 않음 (확인 실패)"]},
  {"id": "INC-208", "minute": 35, "entity": "hana", "rule": "업무 시간 밖 로그인", "grade": "mid", "status": "조치 없음", "playbook": "없음", "done": []},
  {"id": "INC-209", "minute": 40, "entity": "dami", "rule": "퇴사한 계정", "grade": "high", "status": "조치됨", "playbook": "PB-001", "done": ["계정 잠금: 잠김 → 잠김 (이미 잠겨 있어 변경 없음)"]},
  {"id": "INC-210", "minute": 95, "entity": "dami", "rule": "퇴사한 계정", "grade": "high", "status": "조치됨", "playbook": "PB-001", "done": ["계정 잠금: 잠김 → 잠김 (이미 잠겨 있어 변경 없음)"]},
  {"id": "INC-211", "minute": 160, "entity": "dami", "rule": "퇴사한 계정", "grade": "high", "status": "조치됨", "playbook": "PB-001", "done": ["계정 잠금: 잠김 → 잠김 (이미 잠겨 있어 변경 없음)"]}
]
```

<!-- checklist -->
- [ ] `alerts_thu.json` 을 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
<!-- /checklist -->

**`config/escalation_rules.json`** — 티켓 생성 · 병합 · 알림 전파에 적용하는 정책 설정(policy configuration, 폴리시 컨피규레이션: 코드를 수정하지 않고 값만 바꿔 동작을 조정하는 설정 파일)입니다.

- **어디에 쓰나**: 코드를 바꾸지 않고 이 파일만 고쳐도 응답 기한과 수신자가 바뀝니다.

| 키 | 뜻 | 쓰는 곳 |
|---|---|---|
| `sla_minutes` | 등급별 응답 기한(SLA, 서비스 수준 협약, 분) | 실습 3-2 |
| `recipients` | 등급별 알림 수신자(recipient, 리서피언트: 알림을 받는 사람) | 응용 3-3 |
| `merge_window_minutes` | 병합 시간 범위(merge window, 머지 윈도우, 분) | 응용 3-2 |
| `send_gap_minutes` | 같은 티켓에 알림을 다시 보내기까지의 최소 간격(분) | 응용 3-3 |
| `alert_url` | 알림 서버 주소 | 응용 3-3 |
| `escalation_steps` | 응답 기한이 지난 티켓을 상급자에게 올리는 단계 | Unit 4 응용 4-1 |

- 응답 기한(`sla_minutes`)은 알림을 수신한 뒤 담당자가 응답해야 하는 시간입니다.
- 병합 시간 범위는 이 시간 안에 수신된 같은 사건의 알림만 병합하는 기준입니다. 값이 60이므로, 티켓이 마지막으로 갱신된 뒤 60분 이내에 수신된 같은 사건의 알림만 그 티켓에 병합합니다.
- `send_gap_minutes` 는 값이 30이므로, <mark>마지막으로 알린 뒤 30분이 지나야</mark> 같은 티켓에 다시 전송합니다.
- 알림 서버는 응용 3-3에서 두 번째 터미널로 켭니다.
- 에스컬레이션(escalation, 에스컬레이션)은 미처리 사건을 상위 담당자에게 넘기는 일입니다.

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

<!-- checklist -->
- [ ] `config/escalation_rules.json` 을 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
<!-- /checklist -->

> **확인** — 2번 확인 명령에서 `11 6` 이 나오면 성공입니다. `FileNotFoundError` 나 `JSONDecodeError` 가 나오면 마지막 페이지 「오류가 나면」의 표를 봅니다.

<!-- checklist -->
- [ ] 2번 확인 명령을 실행해 `11 6` 이 나왔다
<!-- /checklist -->

## 오류가 나면

먼저 `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.

| 오류 | 뜻 | 고치는 법 |
|---|---|---|
| `No module named 'incident'` | <mark>Unit 1 `incident.py` 가 이 폴더에 없다는 뜻</mark> | 「이전 파일이 없을 때」 페이지를 보고 만든다 |
| `No module named 'ip_actions'` | Unit 2 파일이 없다(`'containment_store'` · `'account_actions'` 도 같다) | 「이전 파일이 없을 때」 페이지를 보고 만든다 |
| `cannot import name 'unblock_ip'` | 파일은 있지만 그 함수가 빠졌다 | `ip_actions.py` 를 Unit 2 M5 Unit 2 「응용과 Unit 3에 필요한 처리 함수 준비」 레슨의 코드를 붙여 넣는다 |
| `FileNotFoundError` | `containment_state.json` 이나 `alerts_thu.json` 같은 데이터 파일이 없다 | 이름과 폴더를 확인하고 이 레슨의 코드 상자로 다시 만든다 |
| `JSONDecodeError` | 붙여 넣을 때 괄호나 따옴표가 빠졌다 | 파일 내용을 지우고 복사 버튼으로 다시 붙여 넣는다 |

- 앞 두 줄은 `ModuleNotFoundError: No module named …`, 셋째 줄은 `ImportError: cannot import name …` 모양으로 나옵니다. `JSONDecodeError` 의 전체 이름은 `json.decoder.JSONDecodeError` 입니다.
- `config/` 로 시작하는 파일은 `config` 폴더에 있어야 합니다.
- 오류 전체와 입력한 명령을 AI 에게 붙여 넣어 물어봅니다. 이때 <mark>`.env` 와 API 키는 지웁니다</mark>. 그래도 막히면 각 실습 바로 아래의 정답 펼침을 봅니다. 그래도 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> **확인** — 고친 뒤 앞 페이지들의 확인 명령(`앞 Unit 파일 정상` · `['junho', 'dami'] 5` · `11 6`)이 모두 그대로 나오면 성공입니다. 하나라도 다르면 그 명령이 있는 페이지로 돌아갑니다.

---
