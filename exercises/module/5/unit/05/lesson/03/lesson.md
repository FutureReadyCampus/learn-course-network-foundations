---
id: m5-u05-l03
title: 실습 5-2 핵심 입력 · Module 4 탐지 로그
render: markdown
---

# 실습 5-2 핵심 입력 · Module 4 탐지 로그

## 입력 데이터의 출처와 사용 목적

실습 5-2는 서로 다른 상황을 기록한 엔진 로그 세 개를 정책으로 점검합니다. 이 중 `risk_engine_log.json` 은 M5 Unit 4의 여덟 알림이 아니라, M4 Unit 4의 탐지 결과 다섯 건을 M5 엔진으로 처리한 **고정 시나리오 입력**입니다. 응용 5-1을 하지 않아도 핵심 실습을 진행할 수 있도록 그 시나리오의 처리 결과를 이 레슨에 둡니다. 이 데이터는 선택 과제에서 만든 결과라고 가정하지 않습니다.

1. 파일은 작업 폴더 `network-study-notes/soar_response` 안에 만듭니다(VS Code 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `risk_engine_log.json`).
2. 다음 페이지 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 만들 파일은 `risk_engine_log.json` 하나입니다. Module 4 탐지 결과 5건을 실습 5-1 엔진으로 처리한 로그입니다.
4. 파일을 만들었으면 아래 명령으로 확인하고 실습 5-2로 갑니다.
   ```bash
   python - <<'PY'
import json

with open("risk_engine_log.json", encoding="utf-8") as file:
    log = json.load(file)

print("엔진 로그 확인", len(log), [record["outcome"] for record in log])
PY
   ```
   - 아래 줄이 나오면 됩니다.
   ```
   엔진 로그 확인 5 ['자동 실행', '조치 없음', '조치 없음', '조치 없음', '자동 실행']
   ```
   - `json.decoder.JSONDecodeError` 가 나오면 붙여 넣다가 일부가 빠진 것입니다. 파일 내용을 모두 지우고 다시 붙여 넣습니다.

> 응용 5-1을 이미 했다면 `risk_engine_log.json` 이 폴더에 있습니다. 새로 만들지 말고 위 확인 명령만 칩니다. 선택 과제 실행기는 이 파일에 같은 시나리오 결과를 다시 저장합니다.

## `risk_engine_log.json` 만들기

<h2><code>risk_engine_log.json</code></h2>

Module 4 Unit 4 실습 4-1에서 저장한 탐지 결과 5건(`unit05_risk_scores.json`)을 알림 `INC-501` ~ `INC-505` 로 바꿔, 실습 5-1 엔진(`run_all`)으로 처리한 결과 로그입니다.

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
- 응용 5-1에서는 M4 탐지 결과를 이 로그로 변환하는 코드(`engine_input.py` · `apply5-1_run.py`)를 직접 씁니다. 핵심 실습에서 사용하는 이 파일은 선택 과제 실행 여부와 독립된 고정 입력입니다.

> **확인** — 앞 페이지 4번의 확인 명령에서 `엔진 로그 확인 5 ['자동 실행', '조치 없음', '조치 없음', '조치 없음', '자동 실행']` 이 나오면 성공입니다. `JSONDecodeError` 가 나오면 파일 내용을 모두 지우고 복사 버튼으로 다시 붙여 넣습니다.

<!-- checklist -->
- [ ] `soar_response` 폴더에 `risk_engine_log.json` 을 만들어 붙여 넣고 저장했다(응용 5-1을 이미 했으면 건너뛰었다)
- [ ] 앞 페이지 4번 명령으로 `risk_engine_log.json` 을 확인해 `엔진 로그 확인 5` 줄이 나왔다
<!-- /checklist -->
