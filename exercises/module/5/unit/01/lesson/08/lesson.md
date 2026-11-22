---
id: m5-u01-l08
title: 정답
render: markdown
---

# 정답

## 정답을 읽는 법

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

1. **핵심 실습**: 실습 1-1 · 1-2 · 1-3 정답입니다. 오늘 모두가 하는 실습이니 먼저 맞춰 봅니다.
2. **응용(여유가 되면)**: 응용 1-1 · 1-2 정답입니다. 응용을 한 사람만 봅니다.
3. 정답마다 결과, 왜, 자주 틀리는 곳, 관제에서는 순서로 읽습니다.

---

## 실습 1-1 정답

 **터미널에 입력합니다.**

```bash
pwd
ls config
python -c "import json; print([p['id'] for p in json.load(open('config/playbook_registry.json', encoding='utf-8'))])"
python -c "import json; s = json.load(open('system_state.json', encoding='utf-8')); print(s['locked_users'], s['blocked_ips'], len(s['tickets']))"
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
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`Illegal trailing comma before end of array`</mark> 가 나오면 이 실수이고, 줄 번호는 사람마다 다릅니다). 파이썬 3.12 이하에서는 같은 실수에 `Expecting value` 로 시작하는 문구가 나옵니다.

```
json.decoder.JSONDecodeError: Illegal trailing comma before end of array: line 37 column 4 (char 873)
```

- PB-002 의 `}` 뒤에 쉼표를 빼고 PB-003 을 붙이면 같은 명령에서 다른 오류가 납니다. <mark>**플레이북과 플레이북 사이에는 쉼표가 있어야 합니다.**</mark> 줄 번호는 사람마다 다릅니다.

```
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 26 column 3 (char 581)
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

**채운 코드** (한 예) — 직접 쓰는 곳은 `playbook_runner.py` 의 `run_playbook` 안 ① · ② 두 줄입니다. 각 줄을 같은 번호 주석 바로 아래에 씁니다. ① 과 ② 사이의 `action_log.append(…)` 줄은 미리 채운 줄이라 그대로 둡니다.

```python
    # ① playbook 의 "approval" 값이 "자동" 이 아니면 (if, !=)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    if playbook["approval"] != "자동":                                              # 승인 값이 자동이 아니면
        action_log.append(make_log_entry(incident, playbook, "전체", "승인 대기"))  # 승인 대기로 기록한다 (미리 채운 줄)
        # ② False 를 리턴해 여기서 끝낸다 (액션을 실행하지 않는다)   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
        return False                                                                # 실행하지 않고 끝낸다
```

위 줄만 보면 들여쓰기가 헷갈리니, 미리 채운 줄까지 넣은 완성된 모양을 함께 봅니다.

**전체 모양 — `run_playbook`**

```python
def run_playbook(incident, playbook, state, action_log):                            # 인시던트 · 플레이북 · 시스템 상태 · 감사 기록 리스트를 받는 함수
    change_status(incident, "분류됨")                                               # 대응을 시작하기 전에 분류됨 상태로 옮긴다
    if playbook["approval"] != "자동":                                              # 승인 값이 자동이 아니면 — ① 직접 쓴 줄
        action_log.append(make_log_entry(incident, playbook, "전체", "승인 대기"))  # 승인 대기로 기록하고
        return False                                                                # 실행하지 않고 끝낸다 — ② 직접 쓴 줄
    for action in playbook["actions"]:                                              # 액션을 하나씩 꺼낸다
        result = run_action(action, incident, state)                                # 액션을 실행하고 결과 문장을 받는다
        action_log.append(make_log_entry(incident, playbook, action, result))       # 결과를 감사 기록에 추가한다
    change_status(incident, "조치됨")                                               # 실행이 끝났으니 조치됨으로 옮긴다
    return True                                                                     # 모두 실행했으니 True 를 리턴한다
```

위 코드는 한 예입니다. <mark>주석이 말한 일을 하면 맞습니다.</mark> ① · ② 말고는 모두 미리 채운 줄입니다.

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

- ② 를 빠뜨리면(① 만 쓰면) 오류는 나지 않지만 <mark>**승인이 필요한 플레이북도 바로 실행됩니다.**</mark> 승인 대기 기록은 남기고도 멈추지 않고 `for` 로 내려가기 때문입니다. 단계 3 에 `INC-002 … -> PB-002 실행 완료 (상태: 조치됨)` 가 나오고, 단계 4 에 차단한 IP 가 들어 있고, 단계 5 의 승인 대기가 0건으로 나오는 것이 이 실수의 결과입니다. 아래 출력은 PB-003 이 `IP 차단` · `티켓 생성` · `담당자 승인 필요` 인 경우입니다.

```
--- 단계 4: 실행 후 연습용 시스템 상태
잠긴 계정: ['dami']
차단한 IP: ['198.51.100.90']
티켓: 3 건 · 담당자 알림: 1 건
--- 단계 5: 승인 대기 0 건
```

- ① 을 `!=` 대신 `==` 로 쓰면 반대로 동작합니다. <mark>**자동이어야 하는 PB-001 이 승인 대기로 멈추고, 승인이 필요한 플레이북이 실행됩니다.**</mark> 단계 5 에 `INC-001 dami PB-001 · 자동` 이 나오는 것이 이 실수의 결과입니다.

```
--- 단계 5: 승인 대기 1 건
INC-001 dami PB-001 · 자동
```

- ② 를 8칸이 아니라 4칸으로 쓰면 `return False` 가 `if` 밖으로 나가 <mark>**모든 플레이북이 멈춥니다.**</mark> 자동인 PB-001 도 승인 대기로 나오고, 액션은 하나도 실행되지 않습니다.

```
--- 단계 5: 승인 대기 3 건
INC-001 dami PB-001 · 자동
INC-002 seoyeon PB-002 · 담당자 승인 필요
INC-005 198.51.100.90 PB-003 · 담당자 승인 필요
```

- ① 끝의 `:` 를 빠뜨리면 실행하자마자 오류가 납니다(<mark style="background:#ffc4d6">`expected ':'`</mark>). <mark>**`if` 줄은 `:` 로 끝납니다.**</mark>

```
SyntaxError: expected ':'
```

**관제에서는**

- 자동 대응을 켤 때 가장 먼저 확인하는 것은 「허락이 필요한 일이 멈추는가」와 「한 일이 모두 기록되는가」입니다. <mark>승인 대기 목록은 담당자가 아침에 가장 먼저 보는 목록</mark>이고, 감사 기록은 사고가 난 뒤 대응을 다시 확인할 때 쓰는 자료입니다.

---

## 실습 1-3 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise1-3_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — `enrichment.py` 의 ① · ② 입니다. 각 줄을 같은 번호 주석 바로 아래에 씁니다.

```python
    # ① entity 가 users_info 안에 있으면 (if, in)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    if entity in users_info:                                         # 계정 정보에 있는 대상이면
```

```python
        # ② ip_info 의 "ip_trusted" 에 source_ips[entity] 가 trusted_ips 안에 있는지(in)의 결과를 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
        ip_info["ip_trusted"] = source_ips[entity] in trusted_ips    # 신뢰 IP 안에 있는지 확인한 결과를 담는다
```

`exercise1-3_run.py` 의 ③ 입니다.

```python
    # ③ enrich_incident(incident, users_info, source_ips, trusted_ips) 를 호출한다 (인시던트에 맥락이 붙는다)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    enrich_incident(incident, users_info, source_ips, trusted_ips)  # 맥락을 붙인다
```

**결과**

- (가) 출력은 다음과 같습니다. 재직 여부가 「퇴사」인 알림은 <mark style="background:#bde3ff">**INC-001**</mark>, VIP 가 「예」인 알림은 <mark style="background:#bde3ff">**INC-003**</mark> 이고, 단계 3 의 VIP 계정 알림 수는 <mark style="background:#bde3ff">**1건**</mark>입니다.

```
--- 단계 1: 불러온 알림 5 건 · 계정 정보 6 명 · 신뢰 IP 1 개
--- 단계 2: 알림마다 붙인 정보(재직 · VIP · 접속 IP)
INC-001 dami · 재직: 퇴사 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
INC-002 seoyeon · 재직: 재직 · VIP: 아니오 · 접속 IP: 203.0.113.80 · 신뢰 IP: 예
INC-003 gaeun · 재직: 재직 · VIP: 예 · 접속 IP: 198.51.100.77 · 신뢰 IP: 아니오
INC-004 jiwoo · 재직: 재직 · VIP: 아니오 · 접속 IP: 203.0.113.80 · 신뢰 IP: 예
INC-005 198.51.100.90 · 재직: 계정 아님 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
--- 단계 3: VIP 계정 알림 수
VIP 계정 알림 1 건
```

- (나) INC-005 의 대상 `198.51.100.90` 은 <mark style="background:#bde3ff">`users_info` 에도 `source_ips` 에도 키로 없습니다.</mark>
  - 근거: `lookup_account` 의 `if entity in users_info:`(①)와 `lookup_source_ip` 의 `if entity in source_ips:` 가 모두 거짓이라 두 `if` 안의 줄이 실행되지 않고, 초기값(`False` · `None`)이 그대로 남습니다.
  - 문제: 확인되지 않은 대상의 `employed` 가 `True`(재직)로 판정되면 사용자 계정이 아닌 IP 를 「재직 중인 정상 사용자」로 오인하게 되어, 이후 경로 판단이 잘못됩니다. 확인되지 않은 대상은 「확인되지 않음」을 뜻하는 `False` 로 유지해야 안전합니다.
- (다) 두 알림의 `reasons` 는 다릅니다.
  - INC-002: `평소와 다른 IP` · <mark style="background:#bde3ff">**`대량 다운로드`**</mark>. INC-004: `업무 시간 밖 로그인` · `평소와 다른 IP`.
  - 신뢰 IP 라는 사실은 「IP 때문에 발생한 알림」이 정상이라는 근거가 되지만, `대량 다운로드` 는 IP 와 무관한 행위라서 신뢰 IP 가 정상이라는 근거가 되지 못합니다. IP 맥락이 같아도 <mark>동일하게 처리하면 안 됩니다.</mark> 이 차이는 응용 1-1의 조건 분기에서 반영합니다.

**왜**

- <mark>조치 실행 전에 알림을 보강하면, 프로그램이 알림의 맥락에 따라 대응을 달리할 수 있습니다.</mark> 맥락이 없으면 모든 알림이 대상 이름과 등급만 다른 동일한 알림으로 보입니다.

**자주 틀리는 곳**

- ① 의 `if` 를 쓰지 않고 그 아래 두 줄을 4칸으로 당기면 계정 정보에 없는 대상에서 오류가 납니다. <mark>**딕셔너리에서 꺼내기 전에 `in` 으로 키가 있는지 먼저 확인합니다.**</mark>
  - 실행하면 INC-004 까지 네 줄이 나온 뒤 다음 오류가 납니다(<mark style="background:#ffc4d6">`KeyError: '198.51.100.90'`</mark>, 키 에러: 딕셔너리에 없는 키를 꺼내려 할 때 나는 오류). `198.51.100.90` 은 `users_info.json` 에 없는 키입니다.

```
KeyError: '198.51.100.90'
```

- ② 를 빠뜨리면 오류는 나지 않지만 <mark>**신뢰 IP 가 모두 「아니오」로 나옵니다.**</mark> INC-002 와 INC-004 의 접속 IP 는 `203.0.113.80` 인데 신뢰 IP 가 「아니오」인 것이 이 실수의 결과입니다.

```
INC-001 dami · 재직: 퇴사 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
INC-002 seoyeon · 재직: 재직 · VIP: 아니오 · 접속 IP: 203.0.113.80 · 신뢰 IP: 아니오
INC-003 gaeun · 재직: 재직 · VIP: 예 · 접속 IP: 198.51.100.77 · 신뢰 IP: 아니오
```

- ② 에서 `in trusted_ips` 를 빼고 `source_ips[entity]` 만 담으면 오류는 나지 않지만 <mark>**접속 IP 가 있는 알림이 모두 「신뢰 IP: 예」로 나옵니다.**</mark> IP 글자가 들어 있는 값은 `if` 에서 참으로 보기 때문입니다. 신뢰 IP 목록에 없는 `198.51.100.77` 의 INC-003 이 「예」인 것이 이 실수의 결과입니다.

```
INC-003 gaeun · 재직: 재직 · VIP: 예 · 접속 IP: 198.51.100.77 · 신뢰 IP: 예
```

- 실행 파일의 ③ 을 비워 두면 맥락이 추가되지 않아 오류가 발생합니다. <mark>**보강 함수를 호출해야 `incident["context"]` 가 생성됩니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`KeyError: 'context'`</mark>).

```
KeyError: 'context'
```

**관제에서는**

- 알림을 열었을 때 대상의 맥락이 이미 추가되어 있으면 분석 시간이 크게 줄어듭니다. <mark>알림 보강은 SOAR(Security Orchestration, Automation and Response, 쏘아: 정해 둔 절차대로 대응을 자동으로 실행하는 체계)의 플레이북에서 조치를 실행하기 전에 흔히 두는 단계입니다.</mark> 오늘은 JSON 파일에서 정보를 읽었지만, 실제 환경에서는 인사 시스템이나 IAM 같은 외부 시스템에서 조회하도록 바꿔도 맥락을 추가하는 방식은 같습니다.

---

## 응용 1-1 정답

> **여유가 되면 해 보세요.** 여기부터는 응용(여유가 되면) 정답입니다. 핵심 실습 정답은 앞의 실습 1-1 ~ 1-3 정답에 있습니다. 번호가 붙은 코드는 골격의 같은 번호 주석 아래에 하나씩 붙입니다. 상자 전체를 한 곳에 붙이지 않습니다.

 **터미널에 입력합니다.**

```bash
pwd
python apply1-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — `routing.py` 의 1 ~ 7번입니다.

```python
    # 1. incident["reasons"] 의 규칙을 하나씩 꺼낸다 (for, rule)
    for rule in incident["reasons"]:                                               # 탐지된 규칙을 하나씩 꺼낸다
    # 2.   rule 이 IP_RELATED_RULES 안에 없으면 (if, not in)
        if rule not in IP_RELATED_RULES:                                           # IP 관련 규칙이 아닌 것이 있으면
    # 3.     False 를 리턴한다 (IP 와 관계없는 다른 증거가 있다)
            return False                                                           # 다른 증거가 있으니 False 를 리턴한다
    # 4. context 의 "vip" 가 참이면 (if)
    if context["vip"]:                                                             # VIP 계정이면
    # 5.   "승인 필요" 와 "VIP 계정이라 담당자 승인이 필요함" 을 쉼표로 이어 함께 리턴한다
        return "승인 필요", "VIP 계정이라 담당자 승인이 필요함"                    # 경로와 이유를 함께 리턴한다
    # 6. context 의 "ip_trusted" 가 참이고(and) is_only_ip_related(incident) 가 참이면 (if)
    if context["ip_trusted"] and is_only_ip_related(incident):                     # 신뢰 IP 이고 규칙이 모두 IP 관련이면
    # 7.   "오탐 종료" 와 "신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄" 을 쉼표로 이어 함께 리턴한다
        return "오탐 종료", "신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄"  # 경로와 이유를 함께 리턴한다
```

`apply1-1_run.py` 의 8 · 9번입니다.

```python
    # 8. decide_route(incident) 가 리턴한 두 값을 route 와 reason 에 한 번에 받는다
    route, reason = decide_route(incident)         # 처리 경로와 이유를 한 번에 받는다
    # 9. route_counts[route] 에 route_counts[route] + 1 을 담는다 (그 경로의 건수를 1 늘린다)
    route_counts[route] = route_counts[route] + 1  # 그 경로의 건수를 1 늘린다
```

**결과**

- (가) 출력은 다음과 같습니다. 경로별 건수는 <mark style="background:#bde3ff">**기본 3건 · 승인 필요 1건 · 오탐 종료 1건**</mark>이고, `종료` 상태가 된 알림은 <mark style="background:#bde3ff">**INC-004**</mark> 입니다.

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-003 gaeun mid -> 승인 필요 · VIP 계정이라 담당자 승인이 필요함 (상태: 탐지됨)
INC-004 jiwoo mid -> 오탐 종료 · 신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄 (상태: 종료)
INC-005 198.51.100.90 low -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
--- 단계 2: 경로별 건수
기본 3 건
승인 필요 1 건
오탐 종료 1 건
```

- (나) INC-004 의 `reasons` 는 `업무 시간 밖 로그인` · `평소와 다른 IP` 로 <mark style="background:#bde3ff">두 규칙 모두 IP 관련 규칙</mark>이라 `is_only_ip_related` 가 `True` 이고, 신뢰 IP 이므로 6번 조건이 참입니다.
  - INC-002 의 `reasons` 에는 IP 관련이 아닌 <mark style="background:#bde3ff">`대량 다운로드`</mark> 가 있어서 `is_only_ip_related` 가 `False` 입니다. 신뢰 IP 에서 접속했어도 `대량 다운로드` 는 IP 와 상관없는 행동입니다. 그래서 정상이라고 할 수 없고, 기본 경로로 보내 분석합니다.
- (다) 한 예: 그 VIP 계정은 <mark style="background:#bde3ff">`승인 필요`</mark> 경로로 갑니다.
  - 4번이 먼저라서 VIP 이면 6번까지 가지 않고 바로 리턴합니다.
  - 순서를 바꾸면 6번 조건이 먼저 검사됩니다. 이 VIP 알림은 「신뢰 IP 이고 규칙이 모두 IP 관련」이라서 `오탐 종료` 로 종료됩니다. 중요한 계정의 알림이 담당자 검토 없이 종료되는 결과이므로, <mark>위험이 더 큰 조건을 먼저 판정합니다.</mark>

**왜**

- <mark>맥락에 따라 경로를 분기하면 중요한 알림은 담당자 검토로 넘기고, 정상임이 분명한 알림은 자동으로 종료할 수 있습니다.</mark> 종료 사유를 함께 기록해야 나중에 「이 알림을 왜 분석하지 않았는가」라는 질문에 감사(audit) 근거로 답할 수 있습니다.

**자주 틀리는 곳**

- 1 ~ 3번을 빠뜨리면 `is_only_ip_related` 가 항상 `True` 를 리턴해서 오류는 나지 않지만 <mark>**INC-002 가 오탐으로 종료됩니다.**</mark> 6번에서 `and is_only_ip_related(incident)` 를 빼도 같은 결과가 나옵니다. 이 실수가 가장 위험합니다. 대량 다운로드가 탐지된 알림이 아무도 검토하지 않은 채 종료되기 때문입니다. 이처럼 실제 위협을 정상으로 판정해 놓치는 것을 미탐(false negative, 폴스 네거티브)이라고 합니다.

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 오탐 종료 · 신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄 (상태: 종료)
```

- 4 · 5번을 빠뜨리면 <mark>**VIP 인 `gaeun`(INC-003) 이 `기본` 경로로 갑니다.**</mark> 중요한 계정이 담당자 승인 없이 기본 절차대로 처리되는 것이 이 실수의 결과입니다.

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-003 gaeun mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
```

- 5번에서 값을 하나만 리턴하면 실행 파일의 `route, reason = decide_route(incident)` 에서 오류가 납니다. <mark>**리턴하는 값의 개수와 받는 변수의 개수가 같아야 합니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`too many values to unpack (expected 2)`</mark>). INC-003 에서 멈추는 것이 이 실수의 결과입니다.

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
ValueError: too many values to unpack (expected 2)
```

- 두 함수만 채우지 않고 실행하면 <mark>**오류 없이 5건이 모두 `기본` 으로 나옵니다.**</mark>

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-003 gaeun mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-004 jiwoo mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-005 198.51.100.90 low -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
--- 단계 2: 경로별 건수
기본 5 건
승인 필요 0 건
오탐 종료 0 건
```

- 실행 파일의 8번을 비워 두면 `route` 가 만들어지지 않아 오류가 납니다. <mark>**리턴된 두 값을 변수에 받아야 아래에서 쓸 수 있습니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`name 'route' is not defined`</mark>, `route` 라는 이름의 변수가 아직 만들어지지 않았다는 뜻입니다). 파이썬 버전에 따라 뒤에 `Did you mean: …`(혹시 이걸 말한 것인가요?라는 추천 문구)이 더 붙을 수 있습니다.

```
NameError: name 'route' is not defined
```

**관제에서는**

- 오탐으로 종료하는 규칙은 <mark>「모든 조건을 충족할 때만 종료한다」처럼 조건을 엄격하게 정의하는 것</mark>이 원칙입니다. 종료한 알림도 사유와 함께 목록으로 보관하고, 주기적으로 일부를 표본 추출(sampling, 샘플링: 전체에서 일부를 골라 검토하는 방식)해 잘못 종료한 건이 없는지 검토합니다. (이 수업 코드에는 없는 운영 절차입니다.)

---

## 응용 1-2 정답

> **여유가 되면 해 보세요.** 응용 1-2를 한 사람만 봅니다.

 **터미널에 입력합니다.**

```bash
pwd
python apply1-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — `safe_runner.py` 의 1 ~ 7번입니다.

```python
    # 1. action 이 "계정 잠금" 이고(and) entity 가 state["locked_users"] 안에 있으면 (if, in)
    if action == "계정 잠금" and entity in state["locked_users"]:                  # 계정 잠금인데 이미 잠긴 계정이면
    # 2.   "건너뜀: 이미 잠겨 있음" 을 리턴한다
        return "건너뜀: 이미 잠겨 있음"                                            # 건너뛸 이유를 리턴한다
    # 3. action 이 "계정 잠금" 이고(and) state["locked_users"] 의 개수(len)가 MAX_LOCKS_PER_RUN 이상이면 (if, >=)
    if action == "계정 잠금" and len(state["locked_users"]) >= MAX_LOCKS_PER_RUN:  # 잠근 계정이 한도 이상이면
    # 4.   "건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)" 를 리턴한다
        return "건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)"    # 건너뛸 이유를 리턴한다
    # 5. skip_reason 이 빈 글자("")가 아니면 (if, !=)
    if skip_reason != "":                                                          # 건너뛸 이유가 있으면
    # 6.   skip_reason 을 리턴한다
        return skip_reason                                                         # 실행하지 않고 이유를 리턴한다
    # 7. run_action(action, incident, state) 의 결과를 리턴한다 (건너뛸 이유가 없으면 원래대로 실행한다)
    return run_action(action, incident, state)                                     # 이유가 없으면 원래 run_action 으로 실행한 결과를 리턴한다
```

`apply1-2_run.py` 의 8 · 9번입니다.

```python
    # 8. result_text 가 "건너뜀" 으로 시작하면 (if, startswith)
    if result_text.startswith("건너뜀"):                              # 결과 문장이 「건너뜀」으로 시작하면
    # 9.   entry["incident"] · entry["action"] · "->" · result_text 를 출력한다 (print)
        print(entry["incident"], entry["action"], "->", result_text)  # 인시던트 · 액션 · 이유를 출력한다
```

**결과**

- (가) 단계 1 · 3 · 4 의 잠긴 계정과 티켓 수는 다음과 같습니다. 출력 전체는 그 아래에 있습니다.

| 단계 | 잠긴 계정 | 티켓 |
|---|---|---|
| 1 | <mark style="background:#bde3ff">**`['dami', 'dami']`**</mark> | <mark style="background:#bde3ff">**2건**</mark> |
| 3 | <mark style="background:#bde3ff">**`['dami']`**</mark> | <mark style="background:#bde3ff">**1건**</mark> |
| 4 | <mark style="background:#bde3ff">**3개(`dami` · `seoyeon` · `gaeun`)**</mark> | <mark style="background:#bde3ff">**7건**</mark> |

```
--- 단계 1: 실습 1-2 방식(안전장치 없음)으로 같은 알림 5건을 두 번 처리
잠긴 계정: ['dami', 'dami']
티켓: 2 건
--- 단계 2: 실습 1-2 방식(안전장치 없음)으로 인사 오류 알림 7건 처리
잠긴 계정 7 개: ['dami', 'dami', 'seoyeon', 'gaeun', 'jiwoo', 'junho', 'hana']
--- 단계 3: 안전한 방식으로 같은 알림 5건을 두 번 처리
첫 번째 처리
INC-001 dami -> 실행 완료 (상태: 조치됨)
INC-002 seoyeon -> 승인 대기 (상태: 분류됨)
INC-003 gaeun -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-004 jiwoo -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-005 198.51.100.90 -> 승인 대기 (상태: 분류됨)
두 번째 처리
INC-001 dami -> 이미 처리됨 (상태: 조치됨)
INC-002 seoyeon -> 승인 대기 (상태: 분류됨)
INC-003 gaeun -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-004 jiwoo -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-005 198.51.100.90 -> 승인 대기 (상태: 분류됨)
잠긴 계정: ['dami']
티켓: 1 건
--- 단계 4: 안전한 방식으로 인사 오류 알림 7건 처리 (한 번에 최대 3 개)
INC-B01 dami -> 실행 완료 (상태: 조치됨)
INC-B02 dami -> 일부 건너뜀 (상태: 분류됨)
INC-B03 seoyeon -> 실행 완료 (상태: 조치됨)
INC-B04 gaeun -> 실행 완료 (상태: 조치됨)
INC-B05 jiwoo -> 일부 건너뜀 (상태: 분류됨)
INC-B06 junho -> 일부 건너뜀 (상태: 분류됨)
INC-B07 hana -> 일부 건너뜀 (상태: 분류됨)
잠긴 계정 3 개: ['dami', 'seoyeon', 'gaeun']
결과별 건수: {'실행 완료': 3, '일부 건너뜀': 4}
티켓: 7 건
건너뛴 액션과 이유:
INC-B02 계정 잠금 -> 건너뜀: 이미 잠겨 있음
INC-B05 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B06 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B07 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
```

- (나) 단계 3 의 「두 번째 처리」에서 INC-001 이 <mark style="background:#bde3ff">`이미 처리됨 (상태: 조치됨)`</mark> 으로 나옵니다.
  - 장치: 중복 실행 방지(idempotency)입니다. `run_playbook_safe` 의 첫 `if` 가 인시던트 상태를 점검해서, `조치됨` · `보고됨` · `종료` 이면 실행하지 않고 건너뜁니다. 첫 번째 처리에서 INC-001 이 `조치됨` 이 되었기 때문입니다.
  - 실습 1-2 방식에는 이 확인이 없어서 두 번째 처리에서 `dami` 를 다시 잠그고 티켓을 또 만들었습니다.
- (다) 잠긴 3개 가운데 <mark style="background:#bde3ff">`seoyeon` 과 `gaeun` 은 `employed` 가 `true` 인 재직자라 잘못 잠긴 계정</mark>입니다. 실제 퇴사자는 `dami` 한 명입니다.
  - 한도가 없고 중복 방지만 있다면 서로 다른 계정 6개가 모두 잠깁니다. 이 가운데 실제 퇴사자는 `dami` 한 명이라 5명이 잘못 잠깁니다(`dami` 는 알림이 두 건이라도 한 번만 잠깁니다). 한도 3개로 잘못 잠긴 계정이 5명에서 2명으로 줄었습니다.
  - 한도가 방지하지 못하는 문제: 한도 안에서는 잘못된 알림도 그대로 실행됩니다. 한도는 영향 범위(잠기는 계정 수)를 제한할 뿐, 잘못된 알림을 알아내지는 못합니다.
  - 줄이는 방법: 실습 1-3에서 보강한 `employed` 맥락을 잠금 실행 전에 점검하면 `seoyeon` 과 `gaeun` 은 재직 중이라 잠금 대상에서 제외됩니다. `gaeun` 은 VIP 계정이라 응용 1-1의 `승인 필요` 경로에서도 자동 잠금 대상에서 제외됩니다. Unit 2 응용 2-2 의 하루 흐름은 이 가운데 VIP 경로와 신뢰 IP 오탐 판단을 하나의 흐름으로 연결합니다. 재직 여부 점검은 연결하지 않습니다.
  - 계정 잠금을 건너뛴 알림에도 티켓은 만들어집니다(티켓 7건). 건너뛰는 것이 알림 전체가 아니라 계정 잠금 액션 하나뿐이기 때문이며, 담당자가 티켓을 보고 이어서 확인합니다.

**왜**

- <mark>자동 대응의 더 큰 위험은 한 번의 오판이 아니라, 잘못된 판단이 짧은 시간에 대량으로 반복 실행되는 것입니다. 예를 들어 잘못된 알림 100건이 들어오면 계정 100개가 몇 초 만에 잠길 수 있습니다.</mark> 중복 실행 방지(같은 조치를 두 번 실행하지 않게 하는 장치)와 영향 범위 제한(피해가 미치는 범위를 제한하는 장치)을 두면, 잘못된 알림이 들어와도 피해가 커지지 않습니다.

**자주 틀리는 곳**

- 1 · 2번을 빠뜨리면 오류는 나지 않지만 <mark>**같은 계정의 두 번째 알림(INC-B02)이 `dami` 를 다시 잠급니다.**</mark> 잠긴 계정 리스트에 `dami` 가 두 번 들어가서 한도 3개 가운데 2개를 쓰기 때문에, `gaeun` 은 잠기지 않습니다. 단계 4 의 `잠긴 계정` 줄이 이 실수의 결과입니다.

```
INC-B04 gaeun -> 일부 건너뜀 (상태: 분류됨)
INC-B05 jiwoo -> 일부 건너뜀 (상태: 분류됨)
INC-B06 junho -> 일부 건너뜀 (상태: 분류됨)
INC-B07 hana -> 일부 건너뜀 (상태: 분류됨)
잠긴 계정 3 개: ['dami', 'dami', 'seoyeon']
결과별 건수: {'실행 완료': 3, '일부 건너뜀': 4}
티켓: 7 건
건너뛴 액션과 이유:
INC-B04 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B05 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B06 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B07 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
```

- 3 · 4번을 빠뜨리면 <mark>**한도가 없어져 재직자까지 모두 잠깁니다.**</mark> 단계 4 의 잠긴 계정이 6개로 나오는 것이 이 실수의 결과입니다.

```
INC-B01 dami -> 실행 완료 (상태: 조치됨)
INC-B02 dami -> 일부 건너뜀 (상태: 분류됨)
INC-B03 seoyeon -> 실행 완료 (상태: 조치됨)
INC-B04 gaeun -> 실행 완료 (상태: 조치됨)
INC-B05 jiwoo -> 실행 완료 (상태: 조치됨)
INC-B06 junho -> 실행 완료 (상태: 조치됨)
INC-B07 hana -> 실행 완료 (상태: 조치됨)
잠긴 계정 6 개: ['dami', 'seoyeon', 'gaeun', 'jiwoo', 'junho', 'hana']
결과별 건수: {'실행 완료': 6, '일부 건너뜀': 1}
티켓: 7 건
건너뛴 액션과 이유:
INC-B02 계정 잠금 -> 건너뜀: 이미 잠겨 있음
```

- 3번에서 `>=` 대신 `>` 를 쓰면 <mark>**한도 3개가 아니라 4개까지 잠깁니다.**</mark> 이처럼 경계값을 하나 잘못 포함하거나 빠뜨리는 오류를 경계 조건 오류(off-by-one error, 오프 바이 원 에러)라고 합니다. 「3개 이상이면 건너뛴다」와 「3개를 초과하면 건너뛴다」는 다릅니다.

```
INC-B03 seoyeon -> 실행 완료 (상태: 조치됨)
INC-B04 gaeun -> 실행 완료 (상태: 조치됨)
INC-B05 jiwoo -> 실행 완료 (상태: 조치됨)
INC-B06 junho -> 일부 건너뜀 (상태: 분류됨)
INC-B07 hana -> 일부 건너뜀 (상태: 분류됨)
잠긴 계정 4 개: ['dami', 'seoyeon', 'gaeun', 'jiwoo']
결과별 건수: {'실행 완료': 4, '일부 건너뜀': 3}
티켓: 7 건
건너뛴 액션과 이유:
INC-B02 계정 잠금 -> 건너뜀: 이미 잠겨 있음
INC-B06 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B07 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
```

- 5 · 6번을 빠뜨리면 <mark>**건너뛸 이유를 판정해 놓고도 적용하지 않아 한도와 중복 방지가 모두 무시됩니다.**</mark> 단계 4 의 잠긴 계정이 7개로 나오고 `dami` 가 두 번 들어 있는 것이 이 실수의 결과입니다.

```
--- 단계 4: 안전한 방식으로 인사 오류 알림 7건 처리 (한 번에 최대 3 개)
INC-B01 dami -> 실행 완료 (상태: 조치됨)
INC-B02 dami -> 실행 완료 (상태: 조치됨)
INC-B03 seoyeon -> 실행 완료 (상태: 조치됨)
INC-B04 gaeun -> 실행 완료 (상태: 조치됨)
INC-B05 jiwoo -> 실행 완료 (상태: 조치됨)
INC-B06 junho -> 실행 완료 (상태: 조치됨)
INC-B07 hana -> 실행 완료 (상태: 조치됨)
잠긴 계정 7 개: ['dami', 'dami', 'seoyeon', 'gaeun', 'jiwoo', 'junho', 'hana']
결과별 건수: {'실행 완료': 7}
티켓: 7 건
건너뛴 액션과 이유:
```

- 7번을 빠뜨리면 `safe_run_action` 이 값을 리턴하지 않아 오류가 납니다. <mark>**건너뛸 이유가 없을 때 실행하는 줄이 있어야 합니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`'NoneType' object has no attribute 'startswith'`</mark>, 값이 없다는 뜻의 `None` 에 `startswith` 를 쓰려 해서 난 오류).

```
AttributeError: 'NoneType' object has no attribute 'startswith'
```

**관제에서는**

- 자동 대응을 켤 때는 <mark>「1회에 최대 몇 건까지 자동 실행하고, 초과하면 담당자에게 넘긴다」</mark>를 먼저 정합니다. 한도에 도달한 건이 나왔다면 잘못된 알림이 대량으로 들어오는 사고가 났다는 신호일 수 있으므로, 담당자에게 별도로 통보하는 에스컬레이션(escalation, 에스컬레이션: 상위 담당자나 다른 팀에 판단을 넘기는 일)을 하기도 합니다. 이 통보 기능은 이번 수업 코드에는 없고, 실제 운영에서 쓰는 절차입니다. 같은 알림이 여러 번 들어와도 결과가 같게 설계하는 것(멱등성)이 기본입니다.
