---
id: m4-u02-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표와 오늘의 계획

핵심 실습 전에 [블로그 초안 준비](__SITE__/exercises/module/4/unit/2/lesson/8/page/1)에서 이번 유닛의 글 파일을 엽니다.

Unit 1에서는 로그를 같은 형식으로 맞추는 일(정규화)을 했습니다. 핵심 실습에서는 웹 서버 로그를, 응용에서는 판정 서버 · SaaS 로그를 맞췄습니다. 오늘은 그렇게 맞춘 이벤트를 **판다스(pandas)** 로 표처럼 읽고 셉니다. 그리고 센 숫자를 **알림 기준**과 비교해 먼저 살펴볼 주소를 찾습니다. 이렇게 규칙으로 살펴볼 일을 찾는 것을 **탐지**라고 하고, SIEM(심, 보안 로그를 모아 탐지하고 알림을 보내는 시스템)의 네 단계(수집 → 정규화 → 탐지 → 알림 · 조사) 중 세 번째 단계입니다.

**오늘의 계획 (약 2시간 40분)**

| 순서 | 시간 | 할 일 |
|---|---|---|
| 1. 시작 | 15분 | 판다스 설치와 이벤트 파일 만들기 |
| 2. 핵심 실습 | 약 110분 | 실습 2-1 ~ 2-3 (약 35 · 40 · 35분) |
| 3. 결과 확인·반영 | 15분 | 실습 2-3에서 실습 파일을 확인하고 저장소에 올리기 |
| 4. 문제 해결 기록 | 20분 | 핵심 실습에서 고민한 내용과 근거를 블로그에 기록하기 |
| 5. 선택 실습 | 여유 시간 | 응용 2-1 · 2-2 중 원하는 문제 해 보기 |

초안에 확인한 값을 메모하고, 핵심 실습 뒤에 그 값이 질문에 어떻게 답하는지 씁니다. 응용은 이 두 가지를 마친 다음 여유가 있을 때 선택합니다.

**오늘 만들 것 세 가지**

| 실습 | 직접 쓰는 것 | 하는 일 |
|---|---|---|
| **실습 2-1** | `events_basic.py` 의 빈칸 두 곳(①·②) | 실패한 이벤트를 소스별로 셈 |
| **실습 2-2** | `events_time.py` 의 빈칸 두 곳(①·②) | 실패를 묶어 세고 CSV 로 저장 |
| **실습 2-3** | `login_detection.py` 의 빈칸 두 곳(①·②) | 로그인 실패 5번 이상인 주소 찾기 |

CSV 파일은 값을 쉼표로 구분해 적은 텍스트 파일이고, 엑셀로도 열립니다. `login_detection.py` 는 다음 Unit 3 응용 3-1이 다시 불러 씁니다.

**응용 2-1 · 2-2는 여유가 되면 해 보세요.** 핵심 실습 세 개와 글쓰기를 마치고 시간이 남을 때 합니다. 응용 2-1에서는 알림 기준 5번을 지난 7일의 숫자로 직접 정해 보고, 응용 2-2에서는 이벤트마다 유형 이름을 붙여 유형별로 셉니다. 응용을 하지 않아도 다음 Unit을 따라갈 수 있습니다.

**먼저 알아 둘 말**

| 말 | 뜻 | 알아 둘 점 |
|---|---|---|
| **판다스** | 데이터를 표로 읽고 짧은 코드로 걸러 내고 셀 수 있게 해 주는 파이썬 라이브러리 | 오늘 처음 씁니다. 새 문법은 실습마다 「판다스 문법 상자」에서 코드와 실행 결과로 설명합니다 |
| **알림 기준** | 이 숫자 이상이면 담당자에게 알리기로 정한 숫자. 임계값(threshold, 쓰레숄드)이라고도 합니다 | 오늘은 「같은 주소가 하루에 로그인에 5번 이상 실패하면 알린다」를 씁니다 |
| **이상** | 평소 범위를 벗어난 일(anomaly, 애너멀리). 「먼저 살펴볼 일」이라는 뜻입니다 | 곧 공격이라는 뜻은 아닙니다 |

「5번 이상」의 이상(以上)은 「5번이거나 5번보다 많음」이라는 다른 말입니다.

- 이벤트 데이터는 이 레슨에서 붙여 넣는 **샘플 파일**(`normalized_events.json`) 하나만 씁니다. 이벤트 57개이고, Unit 1 정규화 결과와 같은 키로 되어 있습니다. Unit 1 파일이 없어도 오늘 실습을 모두 할 수 있습니다.

> **확인** — 시작과 핵심 실습을 마친 뒤 결과를 확인·반영하고 블로그 기록을 남긴 다음 응용을 선택한다는 순서를 말할 수 있으면 성공입니다.

## 폴더 열고 판다스 준비하기

이번 Unit 의 작업 폴더는 `network-study-notes/anomaly_detection` 입니다. VS Code 로 저장소 폴더 `network-study-notes` 를 열고, 터미널에서 `anomaly_detection` 폴더로 들어가 작업합니다. 이 Unit 의 파일 이름은 모두 `anomaly_detection` 폴더 기준입니다.

1. **[VS Code]** `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 가상환경은 **선택**입니다. 가상환경은 프로젝트마다 따로 패키지(판다스 같은 라이브러리)를 설치해 두는 파이썬 실행 환경입니다. <mark>쓰지 않으면 3번으로 바로 갑니다.</mark> 터미널 줄 맨 앞에 `(.venv)` 처럼 가상환경 이름이 이미 보여도 3번으로 갑니다.
   - 가상환경을 쓰고 싶으면 `network-study-notes` 폴더에서 아래 두 줄을 칩니다. 첫 줄이 `.venv` 폴더를 만들고, 둘째 줄이 가상환경을 켭니다. `.venv` 폴더가 이미 있으면 둘째 줄만 칩니다.
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```
   - 가상환경을 켜서 판다스를 설치했다면, 터미널을 새로 열 때마다 둘째 줄을 다시 쳐야 판다스를 쓸 수 있습니다. 새 터미널이 `anomaly_detection` 폴더에서 열렸다면 한 단계 위를 가리키도록 `source ../.venv/Scripts/activate` 로 칩니다.
3. **[터미널]** `anomaly_detection` 폴더로 들어가 위치를 확인하고 판다스를 설치합니다.
   ```bash
   cd anomaly_detection
   pwd
   python -m pip install pandas
   python - <<'PY'
   import pandas

   print(pandas.__version__)
   PY
   ```
   - <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나야</mark> 합니다. `cd anomaly_detection` 이 안 되면 `ls` 로 폴더 이름을 확인하고, 없으면 `mkdir anomaly_detection` 으로 만든 뒤 들어갑니다.
   - 설치가 끝나면 <mark>`Successfully installed …` 또는 `Requirement already satisfied` 가 나옵니다.</mark> 마지막에 `WARNING: You are using pip version …` 이 나와도 무시합니다.
   - <mark>마지막 명령에서 점이 든 숫자(예: `3.1.1`)가 나오면</mark> 판다스를 쓸 수 있습니다. 숫자는 설치한 때에 따라 다릅니다.
   - 판다스 버전에 따라 표 아래의 `dtype` 표시(`object` 또는 `str`), 시각 종류(`datetime64[ns]` 또는 `[us]`), `<StringArray>` 줄, 빈 값이 `None` 이나 `NaN` 으로 보이는 것 같은 **종류 표시만** 조금 다르게 나올 수 있습니다. 숫자와 이름이 레슨의 결과와 같으면 정상입니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에서 판다스를 설치하고 버전 숫자가 나온 것을 봤다
<!-- /checklist -->
4. **파일은 이렇게 만듭니다.** 모두 코드 상자에서 복사해 직접 만듭니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S` 로 저장합니다.
   - 핵심 실습 전에 [블로그 초안 준비](__SITE__/exercises/module/4/unit/2/lesson/8/page/1)에서 이번 유닛의 글 파일을 엽니다.
5. **[VS Code]** `anomaly_detection` 폴더에 `normalized_events.json` 파일을 만들어 아래 내용을 그대로 붙여 넣습니다. <mark>같은 이름의 파일이 이미 있어도 아래 내용으로 덮어씁니다</mark>(출력이 문서와 같아야 하기 때문입니다). Unit 1 응용 1-3 을 한 사람은 같은 이름의 파일이 이미 있는데, 그 파일에는 `raw` 키가 더 있어서 판다스로 읽은 표의 열(키 하나의 값을 세로로 모은 줄, 실습 2-1에서 배웁니다)이 7개가 되고 실습 2-1 · 2-2 의 출력이 문서와 달라집니다.

**`normalized_events.json`** — 정규화된 이벤트 샘플입니다. 한 줄이 이벤트 1개이고, 시간순으로 정렬되어 있습니다. `raw`(원래 로그 한 줄 전체)는 길어서 이 파일에서 뺐습니다. `null` 은 그 값이 로그에 없다는 뜻입니다.

아래 상자의 **복사**를 누르고 VS Code에서 `normalized_events.json` 파일을 엽니다. 편집 영역을 클릭해 전체 선택(`Ctrl + A`) 후 붙여넣고(`Ctrl + V`) 저장합니다(`Ctrl + S`).

<pre class="copyable"><code>[
  {"time": "2026-11-02 02:14:08", "source": "saas", "user": "jiwoo", "ip": "203.0.113.80", "action": "login", "result": "실패"},
  {"time": "2026-11-02 09:01:05", "source": "web", "user": null, "ip": "198.51.100.21", "action": "GET /", "result": "성공"},
  {"time": "2026-11-02 09:01:06", "source": "web", "user": null, "ip": "198.51.100.21", "action": "GET /static/app.css", "result": "성공"},
  {"time": "2026-11-02 09:03:47", "source": "web", "user": null, "ip": "198.51.100.34", "action": "GET /login", "result": "성공"},
  {"time": "2026-11-02 09:03:59", "source": "web", "user": null, "ip": "198.51.100.34", "action": "POST /login", "result": "성공"},
  {"time": "2026-11-02 09:04:00", "source": "web", "user": null, "ip": "198.51.100.34", "action": "GET /board", "result": "성공"},
  {"time": "2026-11-02 09:05:21", "source": "web", "user": null, "ip": "192.0.2.15", "action": "GET /board?page=2", "result": "성공"},
  {"time": "2026-11-02 09:05:30", "source": "saas", "user": "seoyeon", "ip": "198.51.100.9", "action": "login", "result": "성공"},
  {"time": "2026-11-02 09:05:40", "source": "web", "user": null, "ip": "192.0.2.15", "action": "GET /board/12", "result": "성공"},
  {"time": "2026-11-02 09:12:01", "source": "web", "user": null, "ip": "203.0.113.50", "action": "GET /login", "result": "성공"},
  {"time": "2026-11-02 09:12:03", "source": "web", "user": null, "ip": "203.0.113.50", "action": "POST /login", "result": "실패"},
  {"time": "2026-11-02 09:12:06", "source": "web", "user": null, "ip": "203.0.113.50", "action": "POST /login", "result": "실패"},
  {"time": "2026-11-02 09:12:09", "source": "web", "user": null, "ip": "203.0.113.50", "action": "POST /login", "result": "실패"},
  {"time": "2026-11-02 09:12:12", "source": "web", "user": null, "ip": "203.0.113.50", "action": "POST /login", "result": "실패"},
  {"time": "2026-11-02 09:12:15", "source": "web", "user": null, "ip": "203.0.113.50", "action": "POST /login", "result": "실패"},
  {"time": "2026-11-02 09:12:18", "source": "web", "user": null, "ip": "203.0.113.50", "action": "POST /login", "result": "성공"},
  {"time": "2026-11-02 09:12:25", "source": "web", "user": null, "ip": "203.0.113.50", "action": "GET /admin", "result": "실패"},
  {"time": "2026-11-02 09:12:27", "source": "web", "user": null, "ip": "203.0.113.50", "action": "GET /admin/users", "result": "실패"},
  {"time": "2026-11-02 09:20:10", "source": "web", "user": null, "ip": "198.51.100.90", "action": "GET /.env", "result": "실패"},
  {"time": "2026-11-02 09:20:11", "source": "web", "user": null, "ip": "198.51.100.90", "action": "GET /wp-login.php", "result": "실패"},
  {"time": "2026-11-02 09:20:12", "source": "web", "user": null, "ip": "198.51.100.90", "action": "GET /phpmyadmin", "result": "실패"},
  {"time": "2026-11-02 09:22:30", "source": "web", "user": null, "ip": "198.51.100.21", "action": "GET /board/99", "result": "실패"},
  {"time": "2026-11-02 09:25:02", "source": "web", "user": null, "ip": "198.51.100.34", "action": "GET /report", "result": "실패"},
  {"time": "2026-11-02 09:26:44", "source": "web", "user": null, "ip": "192.0.2.15", "action": "GET /search?q=network", "result": "성공"},
  {"time": "2026-11-02 09:28:13", "source": "web", "user": null, "ip": "192.0.2.88", "action": "GET /", "result": "성공"},
  {"time": "2026-11-02 09:28:20", "source": "web", "user": null, "ip": "192.0.2.88", "action": "GET /board", "result": "성공"},
  {"time": "2026-11-02 09:30:12", "source": "saas", "user": "junho", "ip": "192.0.2.41", "action": "login", "result": "성공"},
  {"time": "2026-11-02 09:31:15", "source": "web", "user": null, "ip": "198.51.100.21", "action": "GET /board", "result": "성공"},
  {"time": "2026-11-02 09:33:51", "source": "web", "user": null, "ip": "198.51.100.77", "action": "GET /admin", "result": "실패"},
  {"time": "2026-11-02 09:35:02", "source": "web", "user": null, "ip": "192.0.2.88", "action": "GET /logout", "result": "성공"},
  {"time": "2026-11-02 09:36:10", "source": "web", "user": null, "ip": "198.51.100.21", "action": "GET /board/12", "result": "성공"},
  {"time": "2026-11-02 09:40:00", "source": "server", "user": "seoyeon", "ip": null, "action": "SALES:QUERY", "result": "성공"},
  {"time": "2026-11-02 09:52:00", "source": "server", "user": "junho", "ip": null, "action": "SALES:CHANGE", "result": "성공"},
  {"time": "2026-11-02 10:05:00", "source": "server", "user": "gaeun", "ip": null, "action": "ACCOUNT:CHANGE", "result": "실패"},
  {"time": "2026-11-02 10:09:00", "source": "server", "user": "gaeun", "ip": null, "action": "ACCOUNT:CHANGE", "result": "실패"},
  {"time": "2026-11-02 10:12:55", "source": "saas", "user": "gaeun", "ip": "198.51.100.77", "action": "login", "result": "성공"},
  {"time": "2026-11-02 10:14:00", "source": "server", "user": "gaeun", "ip": null, "action": "ACCOUNT:CHANGE", "result": "실패"},
  {"time": "2026-11-02 11:02:00", "source": "server", "user": "dami", "ip": null, "action": "SALES:QUERY", "result": "실패"},
  {"time": "2026-11-02 11:03:00", "source": "server", "user": "dami", "ip": null, "action": "SALES:QUERY", "result": "실패"},
  {"time": "2026-11-02 11:05:00", "source": "server", "user": "dami", "ip": null, "action": "SALES:CHANGE", "result": "실패"},
  {"time": "2026-11-02 11:08:00", "source": "server", "user": "dami", "ip": null, "action": "SALES:QUERY", "result": "실패"},
  {"time": "2026-11-02 11:25:40", "source": "saas", "user": "seoyeon", "ip": "198.51.100.9", "action": "file.download", "result": "성공"},
  {"time": "2026-11-02 11:40:00", "source": "server", "user": "seoyeon", "ip": null, "action": "SETTLE:QUERY", "result": "실패"},
  {"time": "2026-11-02 13:15:00", "source": "server", "user": "junho", "ip": null, "action": "SALES:QUERY", "result": "성공"},
  {"time": "2026-11-02 13:50:21", "source": "saas", "user": "junho", "ip": "192.0.2.41", "action": "file.upload", "result": "성공"},
  {"time": "2026-11-02 14:30:00", "source": "server", "user": "seoyeon", "ip": null, "action": "SALES:CHANGE", "result": "성공"},
  {"time": "2026-11-02 15:05:00", "source": "server", "user": "junho", "ip": null, "action": "SALES:QUERY", "result": "성공"},
  {"time": "2026-11-02 15:20:03", "source": "saas", "user": "junho", "ip": "192.0.2.41", "action": "login", "result": "성공"},
  {"time": "2026-11-02 16:02:18", "source": "saas", "user": "jiwoo", "ip": "198.51.100.52", "action": "login", "result": "성공"},
  {"time": "2026-11-02 16:10:00", "source": "server", "user": "gaeun", "ip": null, "action": "SALES:QUERY", "result": "성공"},
  {"time": "2026-11-02 17:38:10", "source": "saas", "user": "seoyeon", "ip": "203.0.113.80", "action": "login", "result": "성공"},
  {"time": "2026-11-02 17:40:02", "source": "saas", "user": "seoyeon", "ip": "203.0.113.80", "action": "file.download", "result": "성공"},
  {"time": "2026-11-02 17:40:31", "source": "saas", "user": "seoyeon", "ip": "203.0.113.80", "action": "file.download", "result": "성공"},
  {"time": "2026-11-02 17:41:05", "source": "saas", "user": "seoyeon", "ip": "203.0.113.80", "action": "file.download", "result": "성공"},
  {"time": "2026-11-02 17:41:48", "source": "saas", "user": "seoyeon", "ip": "203.0.113.80", "action": "file.download", "result": "성공"},
  {"time": "2026-11-02 17:42:20", "source": "saas", "user": "seoyeon", "ip": "203.0.113.80", "action": "file.download", "result": "성공"},
  {"time": "2026-11-02 18:20:00", "source": "server", "user": "seoyeon", "ip": null, "action": "SALES:CHANGE", "result": "실패"}
]
</code></pre>

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 `normalized_events.json` 을 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
<!-- /checklist -->

6. **[터미널]** 이벤트가 57개인지 확인합니다.
   ```bash
   python - <<'PY'
   import json

   with open("normalized_events.json", encoding="utf-8") as events_file:
       events = json.load(events_file)

   print(len(events))
   PY
   ```
   - 위 코드는 여러 줄을 한꺼번에 복사해 실행하는 방식입니다. <mark>`57` 이 나와야</mark> 합니다. 아니면 붙여 넣다가 줄이 빠졌거나 `[` `]` 가 빠진 것입니다. 다시 붙여 넣습니다.

<!-- checklist -->
- [ ] 6번의 확인 명령을 실행해 `57` 이 나왔다
<!-- /checklist -->

7. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 직접 쓰는 곳은 실습마다 `# ←` 가 붙은 두 곳(① · ②)이고, 각 주석 바로 아래에 한 줄씩 씁니다. 막히면 각 실습 안의 정답 접기를 봅니다.
   - 판다스 문법 상자와 「알아 둘 것」의 코드는 **읽기만** 합니다. 실행 결과가 함께 적혀 있으니 따로 파일을 만들어 돌려 보지 않아도 됩니다. 직접 만들어 실행하는 파일은 실습마다 굵은 파일 이름이 붙은 두 코드 상자(예: `events_basic.py` · `exercise2-1_run.py`)뿐입니다.

> **확인** — `pwd` 가 `…/anomaly_detection` 으로 끝나고, 판다스 버전 숫자와 이벤트 수 `57` 이 나오면 성공입니다. 안 나오면 다음 페이지 「오류가 나면」의 표에서 내 오류와 같은 줄을 찾습니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.

| 오류 | 원인 | 고치는 법 |
|---|---|---|
| `No module named 'pandas'` | 판다스가 설치되지 않은 터미널입니다. 가상환경을 쓴다면 가상환경이 꺼져 있을 수 있습니다 | 위 2 · 3번을 같은 터미널에서 다시 합니다 |
| `FileNotFoundError` · `ValueError` | 위치나 파일 이름이 틀렸거나, 붙여 넣은 JSON 의 `[` `]` · 쉼표가 틀렸습니다 | `pwd` · `ls` 로 위치와 이름을 보고, 5번의 내용을 다시 붙여 넣습니다 |

- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 각 실습 안의 정답 접기를 보고, 풀리지 않으면 초안에 막힌 지점과 확인한 내용을 남깁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

> **확인** — 앞 페이지 6번의 명령이 오류 없이 `57` 을 보여 주면 성공입니다. 표의 고치는 법으로도 풀리지 않으면 오류 마지막 줄을 그대로 AI 에게 붙여 넣어 묻습니다.

---
