---
id: m4-u04-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표와 오늘의 계획

Module 3 Unit 3 실습 3-2에서 만든 서버 탐지 결과에, 이번 Unit의 고정 시나리오 입력을 더해 점수를 매깁니다. 선택 응용에서 만든 코드는 필요하지 않습니다. 결과가 모두 「탐지됨」이라고만 나오면 어느 대상부터 볼지 정할 수 없고, 알림이 맞았는지도 알 수 없습니다. 오늘은 탐지된 규칙마다 **점수**를 매겨 확인할 순서를 정하고, 틀린 알림(**오탐**)을 **예외 규칙**으로 줄입니다.

**오늘의 계획 (약 2시간 40분)**

| 순서 | 시간 | 하는 일 |
|---|---|---|
| 1. 시작 | 15분 | Unit 3 핵심 파일 확인 · `risk_inputs.json` · `review_alerts.json` |
| 2. 핵심 실습 | 약 110분 | 실습 4-1 · 4-2 (보고서 핵심 질문 포함) |
| 3. 글쓰기 | 20분 | 「오늘의 글 쓰기」에서 세 문장 글 한 편 |
| 4. 결과 기록 | 15분 | 결과물 확인과 저장소 기록 |

- 하루 3시간 가운데 남는 20분은 밀린 사람을 위한 여유입니다. 핵심 실습에서 직접 쓰는 줄은 실습 4-1 두 줄, 실습 4-2 세 줄이고 나머지는 미리 채워 두었습니다. 코드와 입력을 붙여 넣을 때는 코드 상자의 복사 버튼을 사용합니다.

**실습 4-1의 핵심 입력** — Module 3 Unit 3의 서버 탐지 결과와 이 Unit의 `risk_inputs.json` 에 기록한 여섯 개 고정 시나리오 신호를 함께 점수화합니다. 각 신호에는 출처 맥락을 남기며, 이는 학습자가 선택 응용으로 생성한 결과가 아닙니다.

**오늘 만들 것 두 가지**

| 실습 | 하는 일 | 쓰는 파일 | 확인할 것 |
|---|---|---|---|
| **실습 4-1** | 탐지된 규칙마다 점수를 더해 대상(사용자 또는 IP)을 high · mid · low(높음 · 중간 · 낮음)로 나눔 | `risk_scores.py` 의 빈칸 두 곳(① · ②) | 점수 · 등급 · 이유를 `unit05_risk_scores.json` 에 저장 |
| **실습 4-2** | 알림 7개 가운데 협력사 사무실 IP 에서 온 오탐을 예외 규칙 하나로 뺌 | `tuning.py` 의 빈칸 세 곳(① · ② · ③) | 진짜 문제는 지워지지 않았는지 확인 |

**응용 4-1 ~ 4-3은 선택입니다.** 기술 결과 기록과 GitHub 블로그 글쓰기를 마치고 시간이 남을 때 합니다. 응용 4-1에서는 로그를 연결하는 `correlation.py` 를 직접 만들고, 응용 4-2 · 4-3에서는 알림의 오탐과 미탐(놓친 진짜 문제)을 세고 규칙을 합쳐 다시 셉니다. 응용을 하지 않아도 다음 Unit을 따라갈 수 있습니다.

- 점수 파일 이름 `unit05_risk_scores.json` 의 `05` 는 예전 번호라서 지금 Unit 번호와 맞지 않습니다. 그래도 이 Unit의 실습 4-1이 저장하는 이 파일을 Module 4 Unit 5와 Module 5가 같은 이름으로 읽으니, <mark>이름을 바꾸지 않고 그대로 씁니다</mark>.
- 샘플 이벤트의 날짜는 2026-11-02 입니다. 57개 중 웹 서버 28 · 판정 서버 15 · SaaS 14입니다.
- 보고서에서 `[핵심 질문]` 표시가 붙은 질문은 꼭 알아야 할 질문이고, <mark>내 화면의 값을 근거로 이유까지 씁니다</mark>.
- 아래 세 기준은 **고정**하고 <mark>값을 바꿔 가며 비교하지 않습니다</mark>.

| 기준 | 고정한 값 |
|---|---|
| 연결 기준 | 서로 다른 로그 2종류 이상 · 60분 |
| 점수 · 등급 기준 | high 60 이상 · mid 35 이상 |
| 믿는 IP | `203.0.113.80` 한 개 |

> **확인** — 오늘 만들 핵심 파일 두 개(`risk_scores.py` · `tuning.py`)와 저장될 점수 파일 이름(`unit05_risk_scores.json`)을 말할 수 있으면 성공입니다.

## 폴더 열고 이전 파일 확인하기

오늘 코드는 Unit 3 파일을 `import` 로 불러 씁니다. 오늘의 작업 폴더는 저장소 폴더 `network-study-notes` 안의 `anomaly_detection` 입니다(`network-study-notes/anomaly_detection`). 이 Unit 에서 만드는 파일은 모두 이 폴더 바로 아래에 두고, 파일 이름은 이 폴더 기준으로 적습니다. 먼저 `anomaly_detection` 폴더에 아래 파일이 있는지 봅니다.

| 파일 | 만든 곳 | 없을 때 |
|---|---|---|
| `normalized_events.json` · `rbac.py` · `config/users.json` · `config/roles.json` | Unit 3 시작하기 레슨 | Unit 3 시작하기 레슨의 코드 상자로 다시 만듭니다 |
| `access_detection.py` | Unit 3 실습 3-2 | 이 Unit의 「위험 점수 실습 입력 준비」 레슨 마지막 절에 있는 예비 코드로 만듭니다 |

**순서**

1. **[VS Code]** `network-study-notes` 폴더를 연 창에서 메뉴 **Terminal › New Terminal** 로 터미널을 엽니다. 새 터미널은 저장소 맨 위 폴더(`…/network-study-notes`)에서 열립니다.
   - 터미널 오른쪽 위 이름 칸이 **bash** 인지 봅니다. `powershell` 이면 `+` 옆의 **∨** 를 눌러 **Git Bash** 를 고릅니다(Module 3 Unit 1과 같은 방법). 이 과정의 명령은 모두 Git Bash 기준이라, PowerShell 에서는 `source .venv/Scripts/activate` 같은 명령이 동작하지 않습니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치와 파일을 확인합니다. <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, `ls` 결과에 위 표의 파일들이 보여야</mark> 합니다.
   ```bash
   cd anomaly_detection
   pwd
   ls
   python - <<'PY'
   from access_detection import EVENTS_PATH, load_events

   events = load_events(EVENTS_PATH)
   print("Unit 3 파일 정상", len(events))
   PY
   ```
   - 마지막 줄에 `Unit 3 파일 정상 57` 이 나오면 됩니다.
   - `No module named 'access_detection'` 이나 `ImportError` 가 나오면 「위험 점수 실습 입력 준비」 레슨 마지막 절의 `access_detection.py` 예비 코드를 만듭니다. `FileNotFoundError` 나 `No module named 'rbac'` 이 나오면 Unit 3 시작하기 레슨의 코드 상자로 빠진 파일을 만듭니다.

<!-- checklist -->
- [ ] 터미널에서 `anomaly_detection` 폴더로 들어가 2번 명령을 실행했고, `Unit 3 파일 정상 57` 이 나왔다(안 나오면 위 표의 「없을 때」대로 빠진 파일을 만들었다)
<!-- /checklist -->

3. **파일은 이렇게 만듭니다.** 따로 내려받는 파일은 없고, 모두 코드 상자에서 복사해 만듭니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S` 로 저장합니다.
   - 점수·등급·오탐 비교 결과를 남기는 기술 기록 `report_u4.md` 는 「실습 결과 기록 준비」 레슨의 틀로 만듭니다.
4. 다음 페이지에서 `review_alerts.json` 을 만들고, 「위험 점수 실습 입력 준비」 레슨에서 `risk_inputs.json` 을 준비한 뒤 기술 결과 기록 틀을 만들고 실습 4-1로 갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다. **Unit 3 파일은 고치지 않습니다.**

**확인** — 2번의 마지막 줄에 `Unit 3 파일 정상 57` 이 나오면 성공입니다. 안 나오면 다음 페이지 뒤의 「오류가 나면」 표에서 나온 오류 이름을 찾아 고칩니다.

## 알림 파일 만들기

실습 4-2는 지난 11/2 하루 동안 탐지 규칙(서버 반복 거절 · SaaS 세 규칙 · 웹 경로 스캔)이 낸 알림 7개로 시작합니다. 사람이 하나씩 조사한 결과가 붙어 있는 파일입니다.

1. **[VS Code]** `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 로 `review_alerts.json` 파일을 만들어 아래 내용을 붙여 넣고 저장합니다. <mark>같은 이름의 파일이 이미 있으면 아래 내용으로 덮어씁니다</mark>(출력이 문서와 같아야 하기 때문입니다).
   - `real` 은 조사해 보니 진짜 문제였으면 `true`, 아니면 `false` 입니다(판다스로 읽으면 파이썬의 `True` · `False` 가 됩니다). `problem` 은 그 진짜 문제의 번호, `memo` 는 조사 메모입니다.
   - `null` 은 그 값이 없다는 뜻입니다. 서버 알림에는 IP 가 없고, 웹 알림에는 사용자가 없습니다.
   - 알림 번호(`A1` ~ `A7`)와 문제 번호(`P1` …)는 구분하려고 붙인 이름입니다.

**`review_alerts.json`**

```
[
  {"id": "A1", "rule": "서버 반복 거절", "user": "dami", "ip": null, "real": true, "problem": "P1", "memo": "퇴사한 계정이 서버에 4번 요청함"},
  {"id": "A2", "rule": "서버 반복 거절", "user": "gaeun", "ip": null, "real": false, "problem": null, "memo": "서버 설정 오류로 확인됨 — 공격 아님"},
  {"id": "A3", "rule": "SaaS 업무 시간 밖 로그인", "user": "jiwoo", "ip": "203.0.113.80", "real": false, "problem": null, "memo": "출장 중 협력사 사무실에서 비밀번호를 잘못 입력함"},
  {"id": "A4", "rule": "SaaS 평소와 다른 IP", "user": "jiwoo", "ip": "203.0.113.80", "real": false, "problem": null, "memo": "출장 중 협력사 사무실에서 접속함"},
  {"id": "A5", "rule": "SaaS 평소와 다른 IP", "user": "seoyeon", "ip": "203.0.113.80", "real": false, "problem": null, "memo": "외근 중 협력사 사무실에서 접속함"},
  {"id": "A6", "rule": "SaaS 대량 다운로드", "user": "seoyeon", "ip": "203.0.113.80", "real": true, "problem": "P2", "memo": "업무와 상관없는 파일 6개를 한꺼번에 내려받음"},
  {"id": "A7", "rule": "웹 경로 스캔", "user": null, "ip": "198.51.100.90", "real": true, "problem": "P3", "memo": "스캐너 경로 3개를 연속으로 요청함"}
]
```

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 `review_alerts.json` 을 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
<!-- /checklist -->

2. **[터미널]** <mark>파일이 정상인지 확인합니다</mark>.
   ```bash
   python - <<'PY'
   import pandas as pd

   alerts = pd.read_json("review_alerts.json")
   print(len(alerts))
   PY
   ```
   - <mark>`7` 이 나와야</mark> 합니다. 다르면 파일 내용이나 위치(`anomaly_detection` 폴더 안인지)를 다시 확인합니다.
   - 응용 4-2 · 4-3에서 쓰는 `problems.json` · `login_alerts.json` 은 그 응용 레슨에서 만듭니다.

**확인** — 확인 명령이 `7` 을 출력하면 성공입니다. `ValueError` 가 나오면 붙여 넣은 내용의 첫 줄 `[` 와 마지막 줄 `]` 가 빠지지 않았는지 봅니다.

<!-- checklist -->
- [ ] 2번 확인 명령을 실행해 `7` 이 나왔다
<!-- /checklist -->

## 오류가 나면

먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.

| 오류 | 원인 | 고치는 법 |
|---|---|---|
| `No module named 'pandas'` | <mark>판다스가 설치되지 않은 터미널입니다</mark> | `python -m pip install pandas` 를 칩니다 |
| `ImportError` · `No module named 'access_detection'` | <mark>Unit 3 실습 3-2 파일이 없거나 함수 이름이 문서와 다른 것입니다</mark> | 「위험 점수 실습 입력 준비」 레슨 마지막 절의 예비 코드로 `access_detection.py` 를 만듭니다 |
| `FileNotFoundError` · `ValueError` | 파일 위치가 다르거나 JSON 이 깨졌습니다 | <mark>파일이 `anomaly_detection` 폴더 바로 아래에 있는지</mark> `ls` 로 보고, 붙여 넣은 JSON 에 쉼표 · 대괄호가 빠졌는지 봅니다 |

- 판다스를 설치할 때 가상환경을 쓴다면 먼저 `network-study-notes` 폴더에서 가상환경을 켠 뒤(`source .venv/Scripts/activate`) 칩니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 실습 아래의 정답 펼침을 보고</mark>, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

**확인** — 고친 뒤 시작하기의 두 확인 명령에서 `Unit 3 파일 정상 57` 과 `7` 이 나오면 성공입니다. 그래도 안 되면 위 표에 없는 오류이니 오류 전체를 AI 에게 묻습니다.

---
