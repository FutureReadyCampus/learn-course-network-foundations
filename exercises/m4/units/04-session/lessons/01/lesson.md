---
id: m4-u04-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/102_day03_am_baseline_login.md
  mission_id: GichanSource.m4-1104-am-baseline-login
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 개요

어제는 로그를 표로 읽고 세는 법을 배웠습니다. 오늘 오전에는 두 가지를 합니다. 첫째, **「평소」가 얼마인지 정합니다.** 둘째, **평소보다 많은 일을 찾는 규칙**을 만듭니다. 이렇게 규칙으로 일을 찾는 것을 **탐지**라고 하며, SIEM(심, 보안 로그를 모아 탐지 · 알림하는 시스템)의 네 단계(수집 → 정규화 → 탐지 → 알림) 중 세 번째입니다.

- **2교시**: 지난 7일의 로그인 실패 횟수로 **평소 기준**을 정하고, 알림을 보낼 기준 숫자(임계값, threshold, 쓰레숄드)를 정합니다.
- **3교시**: 같은 주소의 로그인 실패가 알림 기준(5번) 이상인 곳을 찾아 알림 대상으로 추출합니다.
- **4교시**: 이벤트마다 **유형 이름**을 정하고 유형별 개수를 셉니다.

오늘은 오전 2 · 3 · 4교시이고, <mark>깃허브에 올리는 일은 오후 6교시 마지막에 합니다.</mark> 교시마다 문제는 하나입니다.

- 오늘 오전에 쓰는 도구는 **파이썬 · 판다스 · VS Code · 터미널**입니다. 판다스는 어제 설치했고, 안 했다면 아래 「🆘」를 봅니다.
- **이상(anomaly, 애너멀리)** 은 <mark>평소 범위를 벗어난 일입니다.</mark> 예를 들어 지난 7일 동안 하루 최대 4번이던 로그인 실패가 한 주소에서 5번이 되는 것입니다. 이상은 **먼저 살펴볼 일**이라는 뜻입니다.
- 「5번 이상」의 이상(以上)은 「5번이거나 5번보다 많음」이라는 다른 뜻입니다.
- 보고서에서 🔍 가 붙은 질문은 이 교시에서 꼭 알아야 할 핵심 질문이고, 내 출력이나 샘플 데이터의 값을 근거로 이유까지 서술합니다.
- 알림 기준(임계값)은 **평소 기준에서 정한 숫자로 고정**하고, <mark>값을 바꿔 가며 비교하지 않습니다.</mark>
- 📎 **오늘 불러 쓰는 이전 파일**은 없습니다. 어제 파일이 없어도 풀 수 있습니다.

## 시작하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치를 확인하고, 판다스가 설치돼 있는지 봅니다(맥북은 `python3`). <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, 마지막에 버전 번호(예: `2.3.3`)가 나오면</mark> 됩니다. `No module named 'pandas'` 가 나오면 아래 「🆘」 첫 줄을 따릅니다.
   ```bash
   cd anomaly_detection
   pwd
   python -c "import pandas; print(pandas.__version__)"
   ```
3. **오늘 받은 파일 두 개**(`day03_am_baseline_login.md`, `day03_am_report.md`)를 `다운로드` 폴더에서 `anomaly_detection` 폴더로 끌어다 놓습니다(안 되면 **File › Save As…**). 이미 있으면 건너뜁니다.
4. **[VS Code]** 보고서 맨 위 제목 `(이름 · 2026-11-04(수))` 의 `이름` 을 내 이름으로 바꿉니다. 안내 파일은 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다.
5. **[VS Code 또는 터미널]** `anomaly_detection` 폴더에 `normalized_events.json` 과 `baseline_logins.csv` 파일을 만들어 아래 내용을 그대로 붙여 넣습니다(터미널에서는 `touch 파일이름` 후 VS Code 에서 엽니다). 두 파일을 모두 붙인 뒤 아래 6번으로 이어 갑니다.

**`normalized_events.json`** — 어제 오후에 만든 이벤트 샘플 57개입니다. 어제 만든 파일이 있어도 열이 6개가 아니거나 아래 6번에서 `57` 이 나오지 않으면 **아래 내용으로 덮어씁니다.** 이벤트 날짜는 모두 2026-11-02 입니다. `null` 은 그 값이 로그에 없다는 뜻입니다.

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

**`baseline_logins.csv`** — 하루마다 **로그인에 가장 많이 실패한 주소 한 곳의 실패 횟수**를 적은 연습용 숫자 7개입니다. CSV 는 값을 쉼표로 구분해 적은 텍스트 파일입니다. 첫 줄은 **헤더(header)** 로, 열 이름이 적힌 줄입니다. 둘째 줄부터 한 줄이 하루입니다.

```
date,failed_logins
2026-10-26,2
2026-10-27,3
2026-10-28,1
2026-10-29,4
2026-10-30,2
2026-10-31,3
2026-11-01,2
```

6. **[터미널]** 두 파일이 정상인지 확인합니다(맥북은 `python3`).
   ```bash
   python -c "import json; print(len(json.load(open('normalized_events.json', encoding='utf-8'))))"
   python -c "print(len(open('baseline_logins.csv', encoding='utf-8').read().splitlines()))"
   ```
   - `python -c "코드"` 는 파일을 만들지 않고 코드를 한 줄로 바로 실행합니다. <mark>순서대로 `57`(이벤트 개수)과 `8`(헤더 줄 포함)이 나와야</mark> 합니다. 다르면 줄이 누락됐거나 빈 줄이 들어간 것이니 다시 붙여 넣습니다.

## 🆘 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다. `cd anomaly_detection` 이 안 되면 `ls` 로 폴더 이름을 확인하고, 없으면 `mkdir anomaly_detection` 으로 만든 뒤 들어갑니다.
- `No module named 'pandas'`: 가상환경이 활성화되지 않은 터미널입니다. `security-agent-toolkit` 폴더에서 가상환경을 활성화한 뒤(`source .venv/Scripts/activate`, 맥북은 `Scripts` 를 `bin` 으로, 폴더 이름이 다르면 그 이름으로) `python -m pip install pandas` 를 칩니다.
- `FileNotFoundError` · `ValueError`: 위치나 파일 이름이 틀렸거나 붙여 넣은 내용이 틀렸습니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

---
