---
id: m4-u04-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표: 로그 연결과 위험 점수

Unit 3에서는 판정 서버 · SaaS · 웹 로그에서 먼저 확인할 것을 따로 탐지했습니다. 이번 Unit에서는 먼저 **같은 사용자의 이벤트가 서로 다른 로그에 짧은 시간 안에 나타난 경우**를 찾아 하나의 사건으로 연결합니다. 이렇게 서로 다른 로그를 같은 기준으로 연결해 분석하는 것을 상관분석(correlation, 코렐레이션)이라고 합니다. 그다음 탐지된 규칙마다 **점수**를 매겨 high · mid · low 로 나누고, 결과를 `unit05_risk_scores.json` 한 파일에 저장합니다. 파일 이름의 `unit05` 는 강의계획서가 정한 이름이라 그대로 씁니다.

- **도전 4-1**: 웹 로그에는 사용자가 없어서 SaaS 성공 로그인의 IP 로 사용자를 찾고, 서버 · SaaS · 웹 로그를 한 표로 합쳐 사용자 · 시각 순으로 놓은 뒤 60분 안에 모인 사건을 찾습니다.
- **실습 4-1**: Unit 3의 탐지와 도전 4-1 결과에서 탐지된 규칙을 모으고, 규칙마다 점수를 더해 등급과 이유를 파일로 저장합니다.

이번 Unit은 도전 4-1 · 7-2로 이루어져 있고, <mark>깃허브에 올리는 일은 실습 4-1 마지막에 합니다.</mark> 실습마다 문제는 하나입니다.

- 이번 Unit에서 쓰는 도구는 **파이썬 · 판다스 · VS Code · 터미널 · git** 입니다.
- 코드 줄은 판다스로 쓰는 줄과 파이썬으로 쓰는 줄이 섞여 있습니다. 표를 합치고 정렬하고 합계를 내는 줄이 판다스이고, 판단 · 딕셔너리 · 문자열 연결이 파이썬입니다.
- 연결 기준(서로 다른 로그 2종류 이상 · 60분)과 점수 · 등급 기준(high 60 이상 · mid 35 이상)은 **고정**하고, <mark>값을 바꿔 가며 비교하지 않습니다</mark>.
- 샘플 이벤트의 날짜는 2026-11-02 입니다. 57개 중 웹 서버 28 · 판정 서버 15 · SaaS 14입니다.
- 보고서에서 `[핵심 질문]` 표시가 붙은 질문은 이 실습에서 꼭 알아야 할 핵심 질문이고, <mark>내 화면의 값을 근거로 이유까지 서술합니다</mark>.
- **이번 Unit에서 불러 쓰는 이전 파일**이 있습니다. 아래 표에서 <mark>`correlation.py` 만 이번 Unit의 도전 4-1에서 만들고, 나머지는 모두 Unit 3에서 만든 파일</mark>입니다.

| 파일 | 만든 곳 | 쓰는 곳 | 없거나 완성하지 못했을 때 |
|---|---|---|---|
| `normalized_events.json` · `rbac.py` · `config/users.json` · `config/roles.json` | Unit 3 「시작하기」 6번 | 도전 4-1 · 7-2 | Unit 3 「시작하기」 레슨 6번의 코드 상자로 파일을 만듭니다 |
| `access_detection.py` | 실습 3-2 | 도전 4-1 · 7-2가 불러옵니다 | Unit 4 「정답」 레슨 맨 아래 「부록 · Unit 3 파일 완성본」의 코드 상자로 파일을 만듭니다 |
| `saas_detection.py` | 도전 3-2 | 도전 4-1 · 7-2가 불러옵니다 | Unit 4 「정답」 레슨 맨 아래 「부록 · Unit 3 파일 완성본」의 코드 상자로 파일을 만듭니다 |
| `malicious_detection.py` | 도전 3-3 | 도전 4-1 · 7-2가 불러옵니다 | Unit 4 「정답」 레슨 맨 아래 「부록 · Unit 3 파일 완성본」의 코드 상자로 파일을 만듭니다 |
| `correlation.py` | 도전 4-1 | 실습 4-1 `exercise4-1_run.py` 가 불러옵니다 | 이 Unit 도전 4-1 레슨의 코드 칸에 「도전 4-1 정답」의 「채운 코드」를 넣어 완성합니다 |

## 폴더 열고 Unit 3 파일 확인하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치와 Unit 3 파일을 확인합니다(맥북은 `python3`). <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, `ls` 결과에 위 표의 파일들이 보여야</mark> 합니다.
   ```bash
   cd anomaly_detection
   pwd
   ls
   ```
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
4. 답을 적는 **보고서**(`report_u4.md`)도 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
5. **[터미널]** Unit 3의 함수가 잘 불러와지는지 확인합니다. <mark>세 줄 모두 아무 오류도 나오지 않으면</mark> 됩니다. 오류가 나면 그 줄의 파일이 문제입니다.
   ```bash
   python -c "from access_detection import load_events, pick_server_failures, pick_suspicious, judge_failure, EVENTS_PATH"
   python -c "from saas_detection import pick_saas, pick_logins, find_off_hours_logins, find_new_ip_users, find_bulk_download_users"
   python -c "from malicious_detection import pick_web_failures, find_scan_ips"
   ```
   - `python -c "코드"` 는 파일을 만들지 않고 코드를 한 줄로 바로 실행합니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 파일 이름이 문서와 같은지 봅니다.
- `No module named 'pandas'`: <mark>가상환경이 활성화되지 않은 터미널입니다</mark>. `security-agent-toolkit` 폴더에서 가상환경을 활성화한 뒤(`source .venv/Scripts/activate`, 맥북은 `Scripts` 를 `bin` 으로, 폴더 이름이 다르면 그 이름으로) `python -m pip install pandas` 를 칩니다.
- `ImportError` · `No module named 'access_detection'`: <mark>Unit 3의 파일이 없거나 함수 이름이 문서와 다른 것입니다</mark>. 위 표의 「없거나 완성하지 못했을 때」를 따릅니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 맨 아래 「정답」을 보고</mark>, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

---

## 목표: 알림 평가와 오탐 줄이기

<!-- REVIEW: 옛 Unit 4 시작하기에서 가져온 쪽입니다. 새 Unit 시작하기에 맞게 합치거나 지우세요 -->

Unit 3과 Unit 4에서 만든 탐지 규칙은 알림을 냈지만, **그 알림이 맞았는지**는 아직 세어 보지 않았습니다. 이번 Unit에서는 <mark>**알림이 맞았는지 세고(평가), 틀린 알림을 줄이는(튜닝)**</mark> 일을 합니다. 세어 보지 않으면 틀린 알림이 쌓여 담당자가 알림을 무시하게 되고, 놓친 문제는 아무도 모른 채 남습니다. 이번 Unit은 <mark>한 실습에 질문 하나씩만</mark> 봅니다.

- **도전 4-2**: 알림 7개와 사람이 조사한 정답(진짜 문제 5개)을 비교해 **오탐**(false positive, 폴스 포지티브: 문제가 아닌데 난 알림)과 **미탐**(false negative, 폴스 네거티브: 진짜 문제인데 알림이 나지 않은 것)을 셉니다.
- **실습 4-2**: 오탐 4개 중 같은 원인 2개를 **예외 규칙**(튜닝: 규칙을 고쳐 틀린 알림을 줄이는 일) 하나로 줄이고, 진짜 문제를 지우지 않았는지 확인합니다.
- **도전 4-3**: 로그인 규칙의 알림을 합쳐 놓친 문제가 줄었는지 확인하고, 평가 결과를 한 문장으로 만듭니다.

이번 Unit은 도전 4-2 · 8-2 · 8-3으로 이루어져 있고, Unit 5에서는 도커 컴포즈를 합니다. <mark>깃허브에 올리는 일은 Unit 5의 도전 5-2 마지막에 합니다.</mark> 실습마다 문제는 하나입니다.

- 이번 Unit에서 쓰는 도구는 **파이썬 · 판다스 · VS Code · 터미널**입니다.
- 이번 Unit에서 새로 배우는 판다스 문법은 `.unique()` 와 `.dropna()` 두 개입니다. `.sum()` 은 Unit 4에서 쓴 것을 `True` 개수 세기에 다시 쓰고, 나머지도 Unit 3과 Unit 4에서 쓴 문법(`isin` · `~` · `&` · `value_counts()` · `pd.concat`)을 다시 씁니다.
- 보고서에서 `[핵심 질문]` 표시가 붙은 질문은 이 실습에서 꼭 알아야 할 핵심 질문이고, <mark>내 출력이나 샘플 데이터의 값을 근거로 이유까지 서술합니다</mark>.
- 알림 번호(`A1` ~ `A8`)와 진짜 문제 번호(`P1` ~ `P5`)는 아래 시작하기의 JSON 파일(`review_alerts.json` · `problems.json` · `login_alerts.json`)에 들어 있습니다. 번호는 구분하려고 붙인 이름입니다.
- 이번 Unit에서 정하는 기준(예외로 믿는 IP `203.0.113.80` 한 개)은 **고정**하고, <mark>값을 바꿔 가며 비교하지 않습니다</mark>.

**이번 Unit에서 불러 쓰는 이전 파일**: 없습니다. 이번 Unit은 아래 시작하기에서 만드는 JSON 파일 세 개로 시작하므로, 앞 Unit의 파일을 만들지 못했어도 그대로 따라 하면 됩니다.

## 폴더 열고 JSON 파일 준비하기

<!-- REVIEW: 옛 Unit 4 시작하기에서 가져온 쪽입니다. 새 Unit 시작하기에 맞게 합치거나 지우세요 -->

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치를 확인하고, 판다스가 설치돼 있는지 봅니다(맥북은 `python3`). <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, 마지막에 버전 번호(예: `2.3.3`)가 나오면</mark> 됩니다. `No module named 'pandas'` 가 나오면 아래 「오류가 나면」 둘째 줄을 따릅니다.
   ```bash
   cd anomaly_detection
   pwd
   python -c "import pandas; print(pandas.__version__)"
   ```
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
4. 답을 적는 **보고서**(`report_u4.md`)도 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
5. **[VS Code]** `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 로 이번 Unit에서 쓸 JSON 파일 세 개 `review_alerts.json` · `problems.json` · `login_alerts.json` 을 만듭니다. 같은 이름의 파일이 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
6. **[VS Code]** 세 파일에 아래 내용을 그대로 붙여 넣습니다(<mark>파일 세 개를 모두 붙인 뒤 맨 아래 7번으로 확인합니다</mark>). <mark>같은 이름의 파일이 이미 있으면 아래 내용으로 덮어씁니다</mark>(출력이 문서와 같아야 하기 때문입니다). `null` 은 그 값이 없다는 뜻입니다.

**`review_alerts.json`** — Unit 3과 Unit 4의 탐지 규칙이 11/2 에 낸 알림 7개이고, 사람이 조사한 결과가 붙어 있습니다. `real` 은 조사해 보니 진짜 문제였으면 `true`, `problem` 은 그 진짜 문제의 번호(`problems.json` 의 `id`), `memo` 는 조사 메모입니다.

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

**`problems.json`** — 사람이 조사해서 확인한 11/2 의 진짜 문제 5개입니다.

```
[
  {"id": "P1", "who": "dami", "what": "퇴사한 계정으로 서버에 요청함"},
  {"id": "P2", "who": "seoyeon", "what": "업무와 상관없는 파일을 대량으로 내려받음"},
  {"id": "P3", "who": "198.51.100.90", "what": "스캐너 경로를 요청해 접근 가능한 곳을 찾음"},
  {"id": "P4", "who": "203.0.113.50", "what": "로그인 5번 실패 뒤 성공하고 관리자 화면을 요청함"},
  {"id": "P5", "who": "seoyeon", "what": "권한 없는 정산 조회를 시도함"}
]
```

**`login_alerts.json`** — 로그인 규칙(웹 로그인 반복 실패)이 낸 알림 1개입니다. 도전 4-3에서 씁니다.

```
[
  {"id": "A8", "rule": "웹 로그인 반복 실패", "user": null, "ip": "203.0.113.50", "real": true, "problem": "P4", "memo": "로그인 5번 실패 뒤 성공, 이어서 관리자 화면을 요청함"}
]
```

7. **[터미널]** <mark>파일이 정상인지 확인합니다</mark>(맥북은 `python3`).
   ```bash
   python -c "import pandas as pd; print(len(pd.read_json('review_alerts.json')), len(pd.read_json('problems.json')), len(pd.read_json('login_alerts.json')))"
   ```
   - <mark>`7 5 1` 이 나와야</mark> 합니다. 다르면 파일 내용이나 위치(`anomaly_detection` 폴더 안인지)를 다시 확인합니다.

## 오류가 나면

<!-- REVIEW: 옛 Unit 4 시작하기에서 가져온 쪽입니다. 새 Unit 시작하기에 맞게 합치거나 지우세요 -->

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `No module named 'pandas'`: <mark>가상환경이 활성화되지 않은 터미널입니다</mark>. `security-agent-toolkit` 폴더에서 가상환경을 활성화한 뒤(`source .venv/Scripts/activate`, 맥북은 `Scripts` 를 `bin` 으로, 폴더 이름이 다르면 그 이름으로) `python -m pip install pandas` 를 칩니다.
- `FileNotFoundError` 나 `ValueError` 가 나오면 <mark>JSON 파일 세 개가 `anomaly_detection` 폴더 바로 아래에 있는지</mark> `ls` 로 보고, 붙여 넣은 내용에 쉼표나 대괄호가 빠지지 않았는지 봅니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 맨 아래 「정답」을 보고</mark>, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

---
