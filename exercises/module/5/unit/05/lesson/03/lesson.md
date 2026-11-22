---
id: m5-u05-l03
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

**실습 5-2를 시작하기 전에** 이 레슨의 파일 하나를 만듭니다. 실습 5-2는 엔진 로그 세 개를 점검하는데, 그 가운데 `risk_engine_log.json` 은 응용 5-1을 실행해야 생기는 로그입니다. 응용을 하지 않아도 실습 5-2를 똑같이 할 수 있도록, 그 실행 결과를 완성본으로 받아 씁니다.

1. 파일은 작업 폴더 `network-study-notes/soar_response` 안에 만듭니다(VS Code 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `risk_engine_log.json`).
2. 다음 페이지 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 만들 파일은 `risk_engine_log.json` 하나입니다. Module 4 탐지 결과 5건을 실습 5-1 엔진으로 처리한 로그입니다.
4. 파일을 만들었으면 아래 명령으로 확인하고 실습 5-2로 갑니다(맥북은 `python3`).
   ```bash
   python -c "import json; log = json.load(open('risk_engine_log.json', encoding='utf-8')); print('제공 파일 정상', len(log), [r['outcome'] for r in log])"
   ```
   - 아래 줄이 나오면 됩니다.
   ```
   제공 파일 정상 5 ['자동 실행', '조치 없음', '조치 없음', '조치 없음', '자동 실행']
   ```
   - `json.decoder.JSONDecodeError` 가 나오면 붙여 넣다가 일부가 빠진 것입니다. 파일 내용을 모두 지우고 다시 붙여 넣습니다.

> 응용 5-1을 이미 했다면 `risk_engine_log.json` 이 폴더에 있습니다. 새로 만들지 말고 위 확인 명령만 칩니다. 나중에 응용 5-1을 하면 `apply5-1_run.py` 가 같은 내용으로 이 파일을 다시 저장합니다.

## `risk_engine_log.json` 만들기

**`risk_engine_log.json`** — Module 4 Unit 4 실습 4-1에서 저장한 탐지 결과 5건(`unit05_risk_scores.json`)을 알림 `INC-501` ~ `INC-505` 로 바꿔, 실습 5-1 엔진(`run_all`)으로 처리한 결과 로그입니다.

- **무엇인가**:
  - 실습 5-1의 `engine_log.json` 과 같은 꼴입니다. 알림 한 건이 한 줄이고, 조치마다 `decision`(승인 게이트의 결정) · `executed`(실행했는지) · `before` · `after` 와 승인 게이트가 본 조치 요청 `request` 가 들어 있습니다.
  - 승인 게이트를 켠 채 처리한 로그입니다. 자동 실행 2건(`INC-501` 의 `dami` 계정 잠금 · `INC-505` 의 `198.51.100.90` 차단)과 조치 없음 3건이고, 티켓이 5장입니다.
- **어디에 쓰나**: 실습 5-2의 `exercise5-2_run.py` 가 점검할 로그 세 개 가운데 두 번째로 읽습니다.

<pre class="copyable"><code>[
  {"incident": "INC-501", "entity": "dami", "grade": "high", "playbook": "PB-001", "outcome": "자동 실행", "steps": [{"action": "계정 잠금", "target": "dami", "decision": "자동", "reasons": ["등급 high +2", "합계 2점"], "executed": true, "before": "잠기지 않음", "after": "잠김", "request": {"id": "INC-501", "incident": "INC-501", "action": "계정 잠금", "target": "dami", "grade": "high", "users_on_ip": 0, "target_count": 1}}], "ticket": "TCK-1", "error": ""},
  {"incident": "INC-502", "entity": "seoyeon", "grade": "mid", "playbook": "PB-002", "outcome": "조치 없음", "steps": [], "ticket": "TCK-2", "error": ""},
  {"incident": "INC-503", "entity": "gaeun", "grade": "mid", "playbook": "없음", "outcome": "조치 없음", "steps": [], "ticket": "TCK-3", "error": ""},
  {"incident": "INC-504", "entity": "jiwoo", "grade": "mid", "playbook": "없음", "outcome": "조치 없음", "steps": [], "ticket": "TCK-4", "error": ""},
  {"incident": "INC-505", "entity": "198.51.100.90", "grade": "low", "playbook": "PB-003", "outcome": "자동 실행", "steps": [{"action": "IP 차단", "target": "198.51.100.90", "decision": "자동", "reasons": ["등급 low +0", "합계 0점"], "executed": true, "before": "차단되지 않음", "after": "차단됨", "request": {"id": "INC-505", "incident": "INC-505", "action": "IP 차단", "target": "198.51.100.90", "grade": "low", "users_on_ip": 0, "target_count": 1}}], "ticket": "TCK-5", "error": ""}
]
</code></pre>

- 줄이 길어 화면에서 오른쪽이 잘려 보여도 복사 버튼은 전체를 복사합니다.
- 응용 5-1에서는 이 로그를 만드는 코드(`engine_input.py` · `apply5-1_run.py`)를 직접 씁니다.

> **확인** — 앞 페이지 4번의 확인 명령에서 `제공 파일 정상 5 ['자동 실행', '조치 없음', '조치 없음', '조치 없음', '자동 실행']` 이 나오면 성공입니다. `JSONDecodeError` 가 나오면 파일 내용을 모두 지우고 복사 버튼으로 다시 붙여 넣습니다.

<!-- checklist -->
- [ ] `soar_response` 폴더에 `risk_engine_log.json` 을 만들어 붙여 넣고 저장했다(응용 5-1을 이미 했으면 건너뛰었다)
- [ ] 앞 페이지 4번 명령으로 `risk_engine_log.json` 을 확인해 `제공 파일 정상 5` 줄이 나왔다
<!-- /checklist -->
