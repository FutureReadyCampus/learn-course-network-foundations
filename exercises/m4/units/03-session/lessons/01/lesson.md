---
id: m4-u03-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/100_day02_pm_pandas_basics.md
  mission_id: GichanSource.m4-1103-pm-pandas-basics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 개요

오전에는 웹 서버 · 판정 서버 · SaaS 로그 3종류를 같은 형식(정규화)으로 맞췄습니다. 오후에는 그렇게 맞춘 이벤트를 **판다스(pandas)** 로 표처럼 읽고 세는 법을 배웁니다. 이벤트를 세고 묶는 일은 SIEM(심)의 다음 단계인 탐지를 하기 위한 준비입니다.

- **5교시**: 정규화된 이벤트 파일을 표로 읽고, 실패한 이벤트만 골라 소스별로 셉니다.
- **6교시**: 실패를 사용자별 · 시간대별로 묶어 세고, 실패한 이벤트를 CSV 파일로 저장합니다.

오늘은 오후 5 · 6교시이고, 깃허브에 올리는 일은 6교시 마지막에 합니다. 교시마다 문제는 하나입니다.

- 오늘 쓰는 도구는 **파이썬 · VS Code · 터미널 · git** 이고, 판다스를 처음 씁니다. 도커는 11/6(금) 오후에 씁니다.
- 새로 나오는 판다스 문법은 읽을거리의 「판다스 문법 상자」에서 코드와 실행 결과, 표가 바뀌는 모양과 함께 설명합니다.
- 이벤트 데이터는 문서에 붙여 넣는 **샘플 파일**(`normalized_events.json`) 하나만 씁니다. 57개이고, 오전에 정규화한 결과와 같은 키로 되어 있습니다.
  - 📎 오늘 불러 쓰는 이전 파일은 없습니다. 오전 파일이 없어도 풀 수 있습니다.

## 시작하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 터미널 줄 맨 앞에 `(.venv)` 처럼 가상환경 이름이 보이는지 봅니다. 보이면 3번으로 가고, 안 보이면 아래를 칩니다(맥북은 `Scripts` 를 `bin` 으로, 가상환경 폴더 이름이 다르면 그 이름으로). 가상환경은 프로젝트마다 따로 패키지(판다스 같은 라이브러리)를 설치해 두는 파이썬 실행 환경입니다.
   ```bash
   source .venv/Scripts/activate
   ```
3. **[터미널]** `anomaly_detection` 폴더로 들어가 위치를 확인하고 판다스를 설치합니다(맥북은 `python3`).
   ```bash
   cd anomaly_detection
   pwd
   python -m pip install pandas
   python -c "import pandas; print(pandas.__version__)"
   ```
   - <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나야</mark> 합니다.
   - 설치가 끝나면 <mark>`Successfully installed …` 또는 `Requirement already satisfied` 가 나옵니다.</mark> 마지막에 `WARNING: You are using pip version …` 이 나와도 무시합니다.
   - <mark>마지막 명령에서 점이 든 숫자(예: `2.3.3`)가 나오면</mark> 판다스를 쓸 수 있습니다.
4. **오늘 받은 파일 두 개**(`day02_pm_pandas_basics.md`, `day02_pm_report.md`)를 `다운로드` 폴더에서 `anomaly_detection` 폴더로 끌어다 놓습니다(안 되면 **File › Save As…**). 이미 있으면 건너뜁니다.
5. **[VS Code]** 보고서 맨 위 제목 `(이름 · 2026-11-03(화))` 의 `이름` 을 내 이름으로 바꿉니다. 안내 파일은 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다.
6. **[VS Code 또는 터미널]** `anomaly_detection` 폴더에 `normalized_events.json` 파일을 만들어 아래 내용을 그대로 붙여 넣습니다(터미널에서는 `touch normalized_events.json` 후 VS Code 에서 엽니다).

**`normalized_events.json`** — 정규화된 이벤트 샘플입니다. 한 줄이 이벤트 1개이고, 시간순으로 정렬되어 있습니다. `raw`(원래 로그 한 줄 전체)는 길어서 이 파일에서 뺐습니다. `null` 은 그 값이 로그에 없다는 뜻입니다.

```
[
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
```

7. **[터미널]** 이벤트가 57개인지 확인합니다(맥북은 `python3`).
   ```bash
   python -c "import json; print(len(json.load(open('normalized_events.json', encoding='utf-8'))))"
   ```
   - <mark>`57` 이 나와야</mark> 합니다. 아니면 붙여 넣다가 줄이 빠졌거나 `[` `]` 가 빠진 것입니다. 다시 붙여 넣습니다.

## 🆘 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `No module named 'pandas'`: 판다스가 설치되지 않았거나 가상환경이 꺼진 터미널입니다. 위 2 · 3번을 같은 터미널에서 다시 합니다.
- `FileNotFoundError` · `ValueError`: 위치나 파일 이름이 틀렸거나, 붙여 넣은 JSON 의 `[` `]` · 쉼표가 틀렸습니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다(맥북은 `python3`).

---
