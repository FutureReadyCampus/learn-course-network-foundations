---
id: m5-u01-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/116_day01_pm_playbook_incident.md
  mission_id: GichanSource.m5-1109-pm-playbook-incident
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답을 보는 방법

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

---

## 실습 1-1 정답

 **터미널에 입력합니다.**

```bash
pwd
ls config
python - <<'PY'
   import json
   from pathlib import Path

   playbooks = json.loads(Path("config/playbook_registry.json").read_text(encoding="utf-8"))
   print([playbook["id"] for playbook in playbooks])
   PY
python - <<'PY'
   import json
   from pathlib import Path

   state = json.loads(Path("system_state.json").read_text(encoding="utf-8"))
   print(state["locked_users"], state["blocked_ips"], len(state["tickets"]))
   PY
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls 폴더이름` 폴더 안의 파일 이름 보기

**채운 파일** (한 예)

`config/playbook_registry.json` 의 PB-003 한 건과 전체 파일은 다음과 같습니다.

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

수동 처리한 뒤의 `system_state.json` 은 다음과 같습니다(PB-003 을 `IP 차단` · `티켓 생성` 으로 쓴 경우).

```
{
  "locked_users": ["dami"],
  "blocked_ips": ["198.51.100.90"],
  "tickets": [
    {"id": "TCK-1", "incident": "INC-001", "target": "dami"},
    {"id": "TCK-2", "incident": "INC-005", "target": "198.51.100.90"}
  ],
  "notifications": []
}
```

위 파일은 한 예입니다. <mark>액션과 승인은 다르게 골라도 이유가 맞으면 맞습니다.</mark>

**결과**

- (가) PB-003 의 액션은 <mark style="background:#bde3ff">**IP 차단 · 티켓 생성**</mark>, 승인은 <mark style="background:#bde3ff">**담당자 승인 필요**</mark>입니다. 두 확인 명령의 출력은 다음과 같습니다.

```
['PB-001', 'PB-002', 'PB-003']
['dami'] ['198.51.100.90'] 2
```

- (나) 위 예에서 고친 곳은 <mark style="background:#bde3ff">**모두 4군데**</mark>입니다.
  - `locked_users` 에 `"dami"` 1군데, `blocked_ips` 에 IP 1군데, `tickets` 에 티켓 2군데입니다.
  - 알림 두 건에 이 정도이니, 알림이 100건이면 수백 군데를 고쳐야 합니다.
  - 같은 모양의 줄을 반복해 쓰다 보면 쉼표나 대괄호를 빠뜨려 파일을 읽을 때 오류가 나기 쉽습니다. 또 어떤 알림을 처리했는지 빠뜨려도 아무도 알지 못합니다.
  - 티켓 번호(`TCK-1` · `TCK-2`)를 사람이 직접 세어야 하는 것도 틀리기 쉬운 부분입니다.
- (다) 승인을 <mark style="background:#bde3ff">`담당자 승인 필요`</mark> 로 정한 이유는 대상이 IP 이기 때문입니다.
  - 사용자 계정은 한 사람의 것이지만, IP 하나는 여러 사람이 함께 쓸 수 있습니다. 그 IP 를 차단하면 경로 스캔과 상관없는 사람도 접속하지 못합니다.
  - 오늘 샘플에서 `198.51.100.90` 은 점수 30점으로 등급이 `low` 입니다. 급하게 막지 않아도 되는 등급이라, 담당자가 확인할 시간을 두는 쪽이 안전합니다.
  - 한 예로 `자동` 을 고르려면 「차단을 바로 풀 수 있다」는 전제가 있어야 합니다. 그 경우에도 `reason` 에 전제를 적어 둡니다.

**왜**

- <mark>플레이북은 「무엇을 할지」뿐 아니라 「누구의 허락을 받고 할지」까지 정해야 완성됩니다.</mark> 수동 처리를 해 보면 같은 일을 반복하는 데 시간이 들고 틀리기 쉽습니다. 그래서 실습 1-2에서는 프로그램이 대신하게 만듭니다.

**자주 틀리는 곳**

- 등록 파일의 마지막 플레이북 뒤에 쉼표를 남기면 확인 명령에서 `JSONDecodeError` 가 납니다. <mark>**마지막 플레이북 뒤에는 쉼표를 붙이지 않습니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`Expecting value`</mark> 로 시작하면 이 실수이고, 줄 번호는 사람마다 다릅니다).

```
json.decoder.JSONDecodeError: Expecting value: line 38 column 1 (char 875)
```

- PB-002 의 `}` 뒤에 쉼표를 빼고 PB-003 을 붙이면 같은 명령에서 다른 오류가 납니다. <mark>**플레이북과 플레이북 사이에는 쉼표가 있어야 합니다.**</mark>

```
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 14 column 3 (char 298)
```

- `actions` 를 `"IP 차단", "티켓 생성"` 처럼 대괄호 없이 쓰면 JSON 문법에 맞지 않아 오류가 납니다. <mark>**`actions` 의 값은 `[ ]` 로 감싼 리스트입니다.**</mark>
- 알림의 대상이 IP 인데 액션에 `계정 잠금` 을 고르면 대상과 맞지 않는 액션입니다. 이 알림은 IP 가 대상이므로 1.2 의 표에서 「대상」이 IP 인 액션을 골라야 합니다. 실습 1-2 실행기는 이런 액션을 실행하지 않고 「건너뜀」으로 기록합니다.

**관제에서는**

- 플레이북은 새 담당자가 와도 같은 순서로 대응하게 하는 문서이고, 승인 값은 자동화를 안전하게 쓰는 기준입니다. <mark>처음에는 사람의 승인을 넣어 두고, 같은 알림을 여러 번 처리해도 잘못된 대응이 없었다고 확인되면 `자동` 으로 바꾸는 방식이 흔합니다.</mark>

---

## 실습 1-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise1-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 `run_playbook` 한 함수입니다.

```python
    if playbook["approval"] != "자동":                                              # 승인 값이 자동이 아니면
        action_log.append(make_log_entry(incident, playbook, "전체", "승인 대기"))  # 승인 대기로 기록하고
        return False                                                                # 실행하지 않고 끝낸다
    for action in playbook["actions"]:                                              # 액션을 하나씩 꺼낸다
        result = run_action(action, incident, state)                                # 액션을 실행하고 결과 문장을 받는다
        action_log.append(make_log_entry(incident, playbook, action, result))       # 결과를 감사 기록에 추가한다
    change_status(incident, "조치됨")                                               # 실행이 끝났으니 조치됨으로 옮긴다
```

위 코드는 한 예입니다. <mark>줄 수가 달라도 주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같습니다(PB-003 이 `담당자 승인 필요` 인 경우). 실행 후 잠긴 계정은 <mark style="background:#bde3ff">**`dami` 1개**</mark>, 차단한 IP는 <mark style="background:#bde3ff">**0개**</mark>, 티켓은 <mark style="background:#bde3ff">**1건**</mark>, 승인 대기는 <mark style="background:#bde3ff">**2건**</mark>(INC-002 · INC-005)입니다.

```
--- 단계 1: 불러온 인시던트 5 건 · 등록된 플레이북 3 개
--- 단계 2: 실행 전 연습용 시스템 상태
잠긴 계정: []
차단한 IP: []
티켓: 0 건 · 담당자 알림: 0 건
--- 단계 3: 인시던트마다 플레이북 실행
INC-001 dami high -> PB-001 실행 완료 (상태: 조치됨)
INC-002 seoyeon mid -> PB-002 승인 대기 (상태: 분류됨)
INC-003 gaeun mid -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-004 jiwoo mid -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-005 198.51.100.90 low -> PB-003 승인 대기 (상태: 분류됨)
--- 단계 4: 실행 후 연습용 시스템 상태
잠긴 계정: ['dami']
차단한 IP: []
티켓: 1 건 · 담당자 알림: 0 건
--- 단계 5: 승인 대기 2 건
INC-002 seoyeon PB-002 · 담당자 승인 필요
INC-005 198.51.100.90 PB-003 · 담당자 승인 필요
--- 단계 6: 감사 기록 4 건을 action_log.json 에 저장
INC-001 PB-001 계정 잠금 : 계정 dami 잠금 완료
INC-001 PB-001 티켓 생성 : 티켓 TCK-1 생성
INC-002 PB-002 전체 : 승인 대기
INC-005 PB-003 전체 : 승인 대기
```

- (나) 실습 1-1에서는 INC-005 를 처리한다고 가정하고 `198.51.100.90` 을 차단했지만, <mark style="background:#bde3ff">실행기는 INC-005 를 처리하지 않고 승인 대기로 멈췄습니다.</mark>
  - 근거: 단계 3 에 `INC-005 … -> PB-003 승인 대기 (상태: 분류됨)`, 단계 4 에 `차단한 IP: []`, 단계 5 에 `INC-005 … PB-003 · 담당자 승인 필요` 가 나옵니다.
  - 이유: `run_playbook` 이 플레이북의 `approval` 이 `자동` 이 아니면 액션을 실행하지 않기 때문입니다. 수동 처리할 때는 이 확인을 사람이 기억해야 했지만, 실행기는 매번 확인합니다.
  - PB-003 의 승인 값을 `자동` 으로 쓴 경우에는 단계 4 의 `차단한 IP` 에 `198.51.100.90` 이 들어갑니다. 또 INC-005 가 `실행 완료 (상태: 조치됨)` 로 나옵니다. 승인 값 하나가 실제 결과를 바꿉니다.
- (다) INC-002 의 기록 한 줄은 `INC-002 PB-002 전체 : 승인 대기` 입니다.
  - 일어난 일: 플레이북 PB-002 가 인시던트 INC-002 에 맞아서 시작됐고, 승인이 필요해 승인 대기로 기록됐습니다.
  - 일어나지 않은 일: 담당자 알림도 티켓 생성도 실행하지 않았습니다. 이 인시던트의 상태는 `분류됨` 입니다.
  - 필요한 이유: 사고가 난 뒤 「그때 왜 조치하지 않았나」를 물으면 이 기록으로 「승인을 기다리고 있었다」고 설명할 수 있습니다. 기록이 없으면 실행하지 않은 일은 아무 흔적도 남지 않습니다.

PB-003 을 `자동` 으로 쓴 경우의 단계 3 ~ 6 은 다음과 같습니다.

```
--- 단계 3: 인시던트마다 플레이북 실행
INC-001 dami high -> PB-001 실행 완료 (상태: 조치됨)
INC-002 seoyeon mid -> PB-002 승인 대기 (상태: 분류됨)
INC-003 gaeun mid -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-004 jiwoo mid -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-005 198.51.100.90 low -> PB-003 실행 완료 (상태: 조치됨)
--- 단계 4: 실행 후 연습용 시스템 상태
잠긴 계정: ['dami']
차단한 IP: ['198.51.100.90']
티켓: 2 건 · 담당자 알림: 0 건
--- 단계 5: 승인 대기 1 건
INC-002 seoyeon PB-002 · 담당자 승인 필요
--- 단계 6: 감사 기록 5 건을 action_log.json 에 저장
INC-001 PB-001 계정 잠금 : 계정 dami 잠금 완료
INC-001 PB-001 티켓 생성 : 티켓 TCK-1 생성
INC-002 PB-002 전체 : 승인 대기
INC-005 PB-003 IP 차단 : IP 198.51.100.90 차단 완료
INC-005 PB-003 티켓 생성 : 티켓 TCK-2 생성
```

PB-003 의 액션에 `계정 잠금` 을 골랐고 승인을 `자동` 으로 쓴 경우의 단계 3 과 단계 6 은 다음과 같습니다. 대상이 IP 라서 실행하지 않고 건너뜁니다.

```
--- 단계 3: 인시던트마다 플레이북 실행
INC-001 dami high -> PB-001 실행 완료 (상태: 조치됨)
INC-002 seoyeon mid -> PB-002 승인 대기 (상태: 분류됨)
INC-003 gaeun mid -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-004 jiwoo mid -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-005 198.51.100.90 low -> PB-003 실행 완료 (상태: 조치됨)
…
--- 단계 6: 감사 기록 5 건을 action_log.json 에 저장
INC-001 PB-001 계정 잠금 : 계정 dami 잠금 완료
INC-001 PB-001 티켓 생성 : 티켓 TCK-1 생성
INC-002 PB-002 전체 : 승인 대기
INC-005 PB-003 계정 잠금 : 건너뜀: 대상이 IP 라서 계정 잠금을 할 수 없습니다
INC-005 PB-003 티켓 생성 : 티켓 TCK-2 생성
```

**왜**

- <mark>승인 값을 코드가 매번 확인해 멈추게 하면, 사람이 기억하지 않아도 허락 없이 실행되는 일이 막힙니다.</mark> 그리고 실행한 일과 멈춘 일을 모두 기록하면 나중에 설명할 수 있습니다.

**자주 틀리는 곳**

- 1 ~ 3번을 빠뜨리면 오류는 나지 않지만 <mark>**승인이 필요한 플레이북도 바로 실행됩니다.**</mark> 단계 4 에 차단한 IP 가 들어 있고 단계 5 의 승인 대기가 0건으로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 4: 실행 후 연습용 시스템 상태
잠긴 계정: ['dami']
차단한 IP: ['198.51.100.90']
티켓: 3 건 · 담당자 알림: 1 건
--- 단계 5: 승인 대기 0 건
```

- 1번을 `!=` 대신 `==` 로 쓰면 반대로 동작합니다. <mark>**자동이어야 하는 PB-001 이 승인 대기로 멈추고, 승인이 필요한 플레이북이 실행됩니다.**</mark> 단계 5 에 `INC-001 dami PB-001 · 자동` 이 나오는 것이 이 실수의 결과입니다.

```
--- 단계 5: 승인 대기 1 건
INC-001 dami PB-001 · 자동
```

- 4번을 빠뜨리고 5번에서 `result` 를 쓰면 오류가 납니다. <mark>**`result` 는 4번에서 만들어야 쓸 수 있습니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`name 'result' is not defined`</mark>).

```
NameError: name 'result' is not defined
```

- 6번을 빠뜨리면 오류는 나지 않지만 <mark>**실행을 마친 인시던트의 상태가 `조치됨` 이 아니라 `분류됨` 으로 남습니다.**</mark> 단계 3 의 INC-001 줄 끝이 이 실수의 결과입니다.

```
INC-001 dami high -> PB-001 실행 완료 (상태: 분류됨)
```

**관제에서는**

- 자동 대응을 켤 때 가장 먼저 확인하는 것은 「허락이 필요한 일이 멈추는가」와 「한 일이 모두 기록되는가」입니다. <mark>승인 대기 목록은 담당자가 아침에 가장 먼저 보는 목록</mark>이고, 감사 기록은 사고가 난 뒤 대응을 다시 확인할 때 쓰는 자료입니다.

---

## 정답 마무리

- (가) 한 예: <mark>`git status` 에서 `.env` 와 `.venv` 가 보이지 않았습니다.</mark> `__pycache__` 가 보여서 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 다시 확인했습니다.
- 깃허브에 `soar_response` 폴더가 생기고 `config` 폴더와 `incident.py` · `playbook_runner.py` · `action_log.json` 이 보이면 됩니다.
