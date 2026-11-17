---
id: m5-u06-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/126_day04_am_ticket_notice.md
  mission_id: GichanSource.m5-1112-am-ticket-notice
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## Unit 6에서 만들 것: 티켓과 알림 전파

<mark style="background:#e0d4ff">Unit 5까지는 알림에 맞는 대응 조치를 실행하고</mark>, 롤백(rollback: 조치 이전 상태로 복원하는 일)하는 것까지 구현했습니다. 이번 Unit에서는 그 결과를 <mark>**담당자에게 인계하고 통지하는 단계**</mark>를 구현합니다. 보안 관제 조직은 티켓과 알림 메시지로 사건 처리를 인수인계하기 때문입니다. 이 단계는 인시던트 관리(incident management)의 일부에 해당합니다. 그중에서 사건 등록 · 중복 제거 · 상태 관리 · 담당자 통지를 구현합니다.

- **Exercise 6-1**: 알림 한 건으로 담당자가 즉시 판단할 수 있는 **티켓을 생성**(ticketing, 티케팅: 알림을 추적 가능한 티켓으로 등록하는 일)합니다. 티켓에는 응답 기한(SLA)을 계산해 기재합니다. 사후 검증에 실패한 조치는 수동 확인 대상으로 별도 표시합니다(`ticketing.py`).
- **Exercise 6-2**: 같은 사건의 알림을 티켓 한 장으로 **병합**(merge)합니다. 병합하면 중복 제거(deduplication: 같은 사건의 알림을 한 건으로 처리하는 일)가 됩니다. 예를 들어 `dami` 의 알림 네 건이 TCK-1 한 장에 병합됩니다. 이어서 허용된 순서로만 티켓 **상태를 전이**(status transition: 상태를 정해진 규칙에 따라 다른 값으로 바꾸는 일)합니다(`ticket_merge.py`).
- **Exercise 6-3**: 등급에 맞는 수신자에게 알림을 **전파**(notification, 노티피케이션: 사건 발생을 담당자에게 통지하는 일)합니다. 이때 `notifier.py` 의 알림 함수를 가져와 사용(import)합니다. 같은 티켓에 알림을 보내는 간격을 제한해 알림 피로(alert fatigue, 얼럿 퍼티그: 알림이 지나치게 많아 담당자가 반응하지 않게 되는 현상)를 줄입니다. 전송에 실패하면 **재시도**(retry, 리트라이: 실패한 전송을 다시 시도하는 일)합니다(`ticket_notice.py`).

깃허브에 올리는 일은 Unit 7의 Exercise 7-2 마지막에 합니다. 새 문법은 Exercise 6-2의 `return None` 과 `is None` 두 가지입니다(`None` 값 자체는 Unit 2에서 나왔습니다). 보고서의 [핵심 질문] 표시가 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 코드를 쓸 때는 들여쓰기를 미리 채운 줄에 맞추고, 각 번호 주석 바로 아래에 한 줄을 씁니다. <mark style="background:#ffc4d6">주석은 지우지 않습니다</mark>.

 **이전 파일**: 이번 Unit에서 가져와 사용(import)하는 파일은 두 묶음입니다. 하나는 <mark style="background:#e0d4ff">Unit 1에서 만든 `incident.py` 의 `load_json` · `save_json`</mark> 입니다. 다른 하나는 <mark style="background:#e0d4ff">`agent_core` 폴더의 `notifier.py` · `alert_server.py`</mark> 입니다. 없는 파일은 아래 시작하기의 「 이전 파일이 없을 때」 코드 상자로 만듭니다.

 **줄임말 이름 안내**: 이 문서의 코드와 파일에는 줄임말로 된 이름이 있습니다. 처음 보면 뜻을 알기 어려워서 아래에 풀어 둡니다. 이미 배포한 파일과 맞추기 위해 이름은 그대로 쓰고 뜻만 설명합니다.
  - `acked_at` 의 `acked` 는 acknowledged(확인했다)의 줄임말입니다. `acked_at` 은 담당자가 티켓을 처음 확인한 시각(분)입니다.
  - `sla` 는 서비스 수준 협약(SLA, Service Level Agreement)의 줄임말입니다. 이 문서에서는 응답 기한을 뜻합니다.
  - `sla_minutes` 는 응답 기한(분), `sla_table` 은 등급마다 정한 응답 기한(분) 표, `sla_due` 는 응답해야 하는 시각, `sla_count` 는 응답 기한을 정한 등급 수입니다.

## 알림 데이터와 설정 파일 만들기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** Module 5 폴더로 들어가 파일을 확인합니다. <mark style="background:#bde3ff">`ls` 결과에 `config` 와 `incident.py` 가 보이면</mark> 됩니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. 이번 Unit에서 받은 파일 두 개(Unit 6 안내 문서, Unit 6 보고서)를 `soar_response` 폴더로 옮기고, 보고서 제목의 `이름` 을 내 이름으로 바꿉니다.
4. **[터미널]** 데이터 파일과 설정 파일을 만들고 **[VS Code]** 에서 열어 아래 내용을 붙여 넣습니다.
   ```bash
   mkdir -p config
   touch alerts_thu.json config/escalation_rules.json
   ls config
   ```

**`alerts_thu.json`** — 이번 Unit의 근무 3시간 동안 들어온 알림 11건입니다.

- **무엇인가**:
  - 알림 한 건은 `id`(알림 번호), `minute`(알림 수신 시각), `entity`(대상: 사용자 이름 또는 IP), `rule`(탐지 규칙), `grade`(심각도 등급, severity)로 구성됩니다.
  - 알림에는 처리 정보도 들어 있습니다. `status` 는 알림 처리 상태입니다. `playbook` 은 실행한 플레이북(playbook: 알림 유형별로 정해 둔 대응 절차)입니다. `done` 은 이미 수행한 조치 내역을 문장으로 적은 리스트입니다.
  - `minute` 은 근무를 시작한 때를 0분으로 센 분 단위 숫자입니다. `INC-201` 은 0분, `INC-211` 은 160분에 왔습니다.
- **어디에 쓰나**: Exercise 6-1 · Exercise 6-2 · Exercise 6-3 실행 파일이 이 파일을 읽어 알림을 하나씩 처리합니다.

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

**`config/escalation_rules.json`** — 티켓 생성 · 병합 · 알림 전파에 적용하는 정책 설정(policy configuration, 폴리시 컨피규레이션: 코드를 수정하지 않고 값만 바꿔 동작을 조정하는 설정 파일)입니다.

- **무엇인가**:
  - `sla_minutes` 는 등급별 응답 기한(SLA, 서비스 수준 협약)입니다. 알림을 수신한 뒤 담당자가 응답해야 하는 시간이며, 단위는 분입니다.
  - `recipients` 는 등급별 알림 수신자(recipient, 리서피언트: 알림을 받는 사람)입니다.
  - `merge_window_minutes` 는 병합 시간 범위(merge window, 머지 윈도우: 이 시간 안에 수신된 같은 사건의 알림만 병합하는 기준)이며 단위는 분입니다. 이번 Unit의 값은 60이므로, 티켓이 마지막으로 갱신된 뒤 60분 이내에 수신된 같은 사건의 알림만 그 티켓에 병합합니다.
  - `send_gap_minutes` 는 같은 티켓에 알림을 다시 전송하기까지 두는 최소 간격이며 단위는 분입니다. 이번 Unit의 값은 30이므로, <mark style="background:#ffdcb0">마지막으로 알린 뒤 30분이 지나야</mark> 같은 티켓에 다시 전송합니다.
  - `alert_url` 은 알림 서버 주소입니다. 알림 서버는 Exercise 6-3 순서에서 두 번째 터미널로 켭니다.
  - `escalation_steps` 는 응답 기한이 지난 티켓을 상급자에게 올리는 에스컬레이션(escalation, 에스컬레이션: 미처리 사건을 상위 담당자에게 넘기는 일) 단계로, Unit 7에서 사용합니다.
- **어디에 쓰나**: 코드를 바꾸지 않고 이 파일만 고쳐도 응답 시간과 수신자(알림을 받는 사람)가 바뀝니다.

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

5. **[터미널]** `agent_core` 폴더의 알림 파일 두 개를 이 폴더로 복사합니다.
   ```bash
   cp ../agent_core/notifier.py .
   cp ../agent_core/alert_server.py .
   ls
   ```
   - 명령 풀이: `cp 원본 복사본` 파일 복사하기(`.` 은 지금 폴더)
   - `No such file` 이 나오면 `ls ..` 로 `agent_core` 폴더 이름이 맞는지 봅니다. 그래도 없으면 아래 「 이전 파일이 없을 때」의 `notifier.py` · `alert_server.py` 코드 상자를 같은 이름의 파일로 붙여 넣습니다.
6. **[터미널]** 파일이 정상인지 확인합니다. 먼저 데이터 파일입니다(맥북은 `python3`). <mark style="background:#bde3ff">`11 6` 이 나와야</mark> 합니다(알림이 11건, 규칙 파일의 키가 6개라는 뜻입니다).
   ```bash
   python -c "import json; print(len(json.load(open('alerts_thu.json', encoding='utf-8'))), len(json.load(open('config/escalation_rules.json', encoding='utf-8'))))"
   ```
7. **[터미널]** 알림 함수를 불러올 수 있는지 확인합니다(맥북은 `python3`). <mark style="background:#bde3ff">`notifier 불러오기 성공` 이 나와야</mark> 합니다.
   ```bash
   python -c "import notifier; print('notifier 불러오기 성공')"
   ```

## 이전 파일이 없을 때 (Unit 1 · 알림 파일)

Unit 1을 하지 못했거나 파일을 지운 경우에만 만듭니다. **이미 있는 파일은 건너뜁니다.** 먼저 **[터미널]** 에서 빈 파일을 만듭니다. 이미 있는 파일은 `touch` 가 그대로 둡니다.

```bash
touch incident.py notifier.py alert_server.py
ls
```

- 명령 풀이: `touch 파일이름들` 빈 파일 만들기 · `ls` 폴더 안의 파일 이름 보기
- 아래 코드 상자 세 개를 **[VS Code]** 에서 같은 이름의 파일에 붙여 넣고 저장합니다. 이미 있는 파일은 붙여 넣지 않습니다.

**`incident.py`** — Unit 1 파일에서 이번 Unit에서 쓰는 두 함수(`load_json` · `save_json`)만 담았습니다. Unit 1 파일 전체가 있으면 그것을 그대로 씁니다.

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

**`notifier.py`** — 알림 함수 `notify` 입니다. 메시지를 알림 서버로 보냅니다.

```python
import requests                                                # 인터넷으로 요청을 보내는 도구 (9/30)


def notify(message, url):                                      # 메시지를 알림 서버로 보내는 함수
    try:                                                       # 아래 줄을 해 본다
        requests.post(url, json={"text": message}, timeout=5)  # 메시지를 POST 한다 — 5초만 기다린다
        return True                                            # 보냈다
    except Exception as e:                                     # 에러가 나면 e 에 담아 여기로 온다
        print("[알림 실패]", type(e).__name__)                 # 에러 이름을 알린다 — 숨기지 않는다
        return False                                           # 못 보냈다 — 부른 쪽은 계속 간다
```

**`alert_server.py`** — 알림 서버입니다. Exercise 6-3과 Unit 7의 Exercise 7-1에서 알림을 받는 쪽입니다.

```python
from flask import Flask, request        # 10/2 에 쓴 웹 서버 도구

app = Flask(__name__)                   # 서버를 하나 만든다


@app.route("/alert", methods=["POST"])  # /alert 로 POST 가 오면 아래 함수가 받는다
def alert():                            # 알림을 받는 함수
    data = request.get_json()           # 보낸 JSON 을 딕셔너리로 꺼낸다
    print("[알림 받음]", data["text"])  # 터미널에 알림 내용을 보여 준다
    return {"ok": True}                 # 받았다고 답한다 (상태 코드 200)


app.run(port=5001)                      # 5001 번 포트에서 기다린다
```

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError: No module named 'incident'` 는 <mark style="background:#ffc4d6">Unit 1에서 만든 `incident.py` 가 이 폴더에 없다는 뜻</mark>입니다. `No module named 'notifier'` 는 5번 복사를 하지 않았다는 뜻입니다. 둘 다 위 「 이전 파일이 없을 때」의 코드 상자로 만듭니다. `No module named 'requests'` 나 `No module named 'flask'` 가 나오면, 터미널(가상환경이 켜진 상태)에서 `pip install requests` 또는 `pip install flask` 를 입력합니다.
- 오류 전체와 입력한 명령을 AI 에게 붙여 넣어 물어봅니다. 이때 <mark style="background:#ffc4d6">`.env` 와 API 키는 지웁니다</mark>. 그래도 막히면 맨 아래 「정답」을 봅니다. 그래도 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 실행할 때마다 처음 상태에서 시작해 같은 결과가 나옵니다.

---
