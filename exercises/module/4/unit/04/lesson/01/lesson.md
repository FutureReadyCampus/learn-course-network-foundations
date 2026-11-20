---
id: m4-u04-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표와 오늘의 계획

Unit 3 실습 3-2에서는 판정 서버 로그에서 반복 거절을 찾았습니다. SaaS · 웹 로그를 살피는 탐지 규칙은 Unit 3 도전 3-2 · 3-3에서 다뤘고, 도전을 하지 않았어도 오늘 「제공 파일」 레슨에서 완성본을 받아 씁니다. 그런데 결과가 모두 「탐지됨」이라고만 나오면 어느 대상부터 볼지 정할 수 없고, 알림이 맞았는지도 알 수 없습니다. 오늘은 탐지된 규칙마다 **점수**를 매겨 확인할 순서를 정하고, 틀린 알림(**오탐**)을 **예외 규칙**으로 줄입니다.

**오늘의 계획 (3시간)**

1. 시작하기 15분: 이 레슨을 읽고 Unit 3 파일을 확인한 뒤, 알림 파일 `review_alerts.json` 과 「제공 파일」 레슨의 파일 세 개를 만듭니다.
2. 실습 약 110분: 핵심 실습 두 개를 차례로 합니다.
3. 글쓰기 40분: 「보고서 쓰기」 레슨에서 핵심 실습의 질문에 답하고, 「오늘의 글 쓰기」 레슨에서 글 한 편을 씁니다.
4. 마무리 15분: 실습 4-2 끝의 「이번 Unit 마무리」에서 파일을 확인하고 깃허브에 올립니다.

**오늘 먼저 받아 쓰는 것** — 「제공 파일」 레슨의 완성 코드 세 개입니다.

1. `saas_detection.py`: SaaS 로그에서 업무 시간 밖 로그인 · 평소와 다른 IP · 대량 다운로드를 찾는 함수
2. `malicious_detection.py`: 웹 로그에서 스캐너 경로를 요청한 IP(경로 스캔)를 찾는 함수
3. `correlation.py`: 서버 · SaaS · 웹 로그를 한 사용자 기준으로 이어, 60분 안에 서로 다른 로그가 모인 사건을 찾는 함수 `find_chains_in_events`

**오늘 만들 것 두 가지**

1. **실습 4-1**: 탐지된 규칙마다 점수를 더해 대상(사용자 또는 IP)을 high · mid · low(높음 · 중간 · 낮음) 세 등급으로 나누고, 점수 · 등급 · 이유를 `unit05_risk_scores.json` 에 저장하는 `risk_scores.py` 를 씁니다.
2. **실습 4-2**: 알림 7개 가운데 협력사 사무실 IP 에서 온 오탐을 예외 규칙 하나로 빼고, 진짜 문제는 지워지지 않았는지 확인하는 `tuning.py` 를 씁니다.

**도전 4-1 ~ 4-3은 선택입니다.** 핵심 실습 두 개와 글쓰기를 마치고 시간이 남을 때 합니다. 도전 4-1에서는 제공 파일 `correlation.py` 를 직접 써 보고, 도전 4-2 · 4-3에서는 알림의 오탐과 미탐(놓친 진짜 문제)을 세고 규칙을 합쳐 다시 셉니다. 도전을 하지 않아도 다음 Unit을 따라갈 수 있습니다.

- 점수 파일 이름 `unit05_risk_scores.json` 의 `05` 는 예전 번호라서 지금 Unit 번호와 맞지 않습니다. 그래도 이 Unit의 실습 4-1이 저장하는 이 파일을 Module 4 Unit 5와 Module 5가 같은 이름으로 읽으니, <mark>이름을 바꾸지 않고 그대로 씁니다</mark>.
- 연결 기준(서로 다른 로그 2종류 이상 · 60분), 점수 · 등급 기준(high 60 이상 · mid 35 이상), 믿는 IP(`203.0.113.80` 한 개)는 **고정**하고 <mark>값을 바꿔 가며 비교하지 않습니다</mark>.
- 샘플 이벤트의 날짜는 2026-11-02 입니다. 57개 중 웹 서버 28 · 판정 서버 15 · SaaS 14입니다.
- 보고서에서 `[핵심 질문]` 표시가 붙은 질문은 꼭 알아야 할 질문이고, <mark>내 화면의 값을 근거로 이유까지 씁니다</mark>.

## 폴더 열고 이전 파일 확인하기

오늘 코드는 Unit 3 파일을 `import` 로 불러 씁니다. 먼저 `anomaly_detection` 폴더에 아래 파일이 있는지 봅니다.

| 파일 | 만든 곳 | 없을 때 |
|---|---|---|
| `normalized_events.json` · `rbac.py` · `config/users.json` · `config/roles.json` | Unit 3 시작하기 레슨 | Unit 3 시작하기 레슨의 코드 상자로 다시 만듭니다 |
| `access_detection.py` | Unit 3 실습 3-2 | 이 Unit 「제공 파일」 레슨 마지막 페이지의 예비 코드로 만듭니다 |

**순서**

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치와 파일을 확인합니다(맥북은 `python3`). <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, `ls` 결과에 위 표의 파일들이 보여야</mark> 합니다.
   ```bash
   cd anomaly_detection
   pwd
   ls
   python -c "from access_detection import load_events, pick_server_failures, pick_suspicious, judge_failure, EVENTS_PATH; print('Unit 3 파일 정상', len(load_events(EVENTS_PATH)))"
   ```
   - `python -c "코드"` 는 파일을 만들지 않고 코드를 한 줄로 바로 실행합니다.
   - 마지막 줄에 `Unit 3 파일 정상 57` 이 나오면 됩니다.
   - `No module named 'access_detection'` 이나 `ImportError` 가 나오면 「제공 파일」 레슨에서 `access_detection.py` 예비 코드까지 만듭니다. `FileNotFoundError` 나 `No module named 'rbac'` 이 나오면 Unit 3 시작하기 레슨의 코드 상자로 빠진 파일을 만듭니다.
3. **파일은 이렇게 만듭니다.** 따로 내려받는 파일은 없고, 모두 코드 상자에서 복사해 만듭니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u4.md` 는 「보고서 쓰기」 레슨의 틀을 복사해 만듭니다.
4. 다음 페이지에서 알림 파일을 만들고, 「제공 파일」 레슨으로 가서 파일 세 개를 만든 뒤 실습 4-1로 갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다. **Unit 3 파일은 고치지 않습니다.**

## 알림 파일 만들기

실습 4-2는 지난 11/2 하루 동안 탐지 규칙(서버 반복 거절 · SaaS 세 규칙 · 웹 경로 스캔)이 낸 알림 7개로 시작합니다. 사람이 하나씩 조사한 결과가 붙어 있는 파일입니다.

1. **[VS Code]** `anomaly_detection` 폴더에 `review_alerts.json` 파일을 만들어 아래 내용을 붙여 넣습니다. <mark>같은 이름의 파일이 이미 있으면 아래 내용으로 덮어씁니다</mark>(출력이 문서와 같아야 하기 때문입니다).
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

2. **[터미널]** <mark>파일이 정상인지 확인합니다</mark>(맥북은 `python3`).
   ```bash
   python -c "import pandas as pd; print(len(pd.read_json('review_alerts.json')))"
   ```
   - <mark>`7` 이 나와야</mark> 합니다. 다르면 파일 내용이나 위치(`anomaly_detection` 폴더 안인지)를 다시 확인합니다.
   - 도전 4-2 · 4-3에서 쓰는 `problems.json` · `login_alerts.json` 은 그 도전 레슨에서 만듭니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `No module named 'pandas'`: <mark>판다스가 설치되지 않은 터미널입니다</mark>. `python -m pip install pandas` 를 칩니다(맥북은 `python3`). 가상환경을 쓴다면 먼저 `security-agent-toolkit` 폴더에서 가상환경을 켠 뒤(`source .venv/Scripts/activate`, 맥북은 `Scripts` 를 `bin` 으로) 칩니다.
- `ImportError` · `No module named 'access_detection'`: <mark>Unit 3 실습 3-2 파일이 없거나 함수 이름이 문서와 다른 것입니다</mark>. 「제공 파일」 레슨 마지막 페이지의 예비 코드로 `access_detection.py` 를 만듭니다.
- `FileNotFoundError` 나 `ValueError`: <mark>파일이 `anomaly_detection` 폴더 바로 아래에 있는지</mark> `ls` 로 보고, 붙여 넣은 JSON 에 쉼표나 대괄호가 빠지지 않았는지 봅니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 이 Unit 뒤쪽의 정답을 보고</mark>, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

---
