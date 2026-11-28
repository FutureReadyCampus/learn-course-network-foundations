---
id: m4-u03-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표와 오늘의 계획

핵심 실습 전에 [블로그 초안 준비](__SITE__/exercises/module/4/unit/3/lesson/8/page/1)에서 이번 유닛의 글 파일을 엽니다.

실습 2-3 에서는 같은 주소가 로그인에 몇 번 실패했는지 세어 알림 기준을 정했습니다. 오늘은 탐지 규칙을 두 개 더 만듭니다. 하나는 **요청이 갑자기 늘어난 때(트래픽 급증, traffic spike)** 를 찾는 규칙이고, 다른 하나는 **같은 사람이 여러 번 거절당한 기록**을 찾아 거절 이유로 순서를 정하는 규칙입니다.

<h2>오늘의 계획 (약 2시간 40분)</h2>

| 순서 | 시간 | 하는 일 |
|---|---|---|
| 1. 시작 | 15분 | 이 레슨을 읽고 오늘 쓸 파일을 만듭니다 |
| 2. 핵심 실습 | 약 110분 | 실습 3-1 · 3-2 (결과는 초안에 남김) |
| 3. 결과 확인·반영 | 15분 | 실습 3-2에서 실습 파일을 확인하고 저장소에 올리기 |
| 4. 문제 해결 기록 | 20분 | 핵심 실습에서 고민한 내용과 근거를 블로그에 기록하기 |
| 5. 선택 실습 | 여유 시간 | 응용 3-1 ~ 3-3 중 원하는 문제 해 보기 |

초안에 확인한 값을 메모하고, 핵심 실습 뒤에 그 값이 질문에 어떻게 답하는지 씁니다. 응용은 이 두 가지를 마친 다음 여유가 있을 때 선택합니다.

<h2>오늘 만들 것 두 가지</h2>

| 실습 | 직접 쓰는 것 | 하는 일 |
|---|---|---|
| **실습 3-1** | `traffic_detection.py` 의 빈칸 두 곳(① · ②) | 분마다 세어 평균의 3배 이상인 분 찾기 |
| **실습 3-2** | `access_detection.py` 의 빈칸 세 곳(① ~ ③) | 3번 이상 거절된 기록에 이유 붙이기 |

1. **실습 3-1**: 웹 서버 요청을 분마다 세고, 지난 7일 평균의 3배 이상으로 늘어난 분을 찾는 `traffic_detection.py` 를 씁니다.
2. **실습 3-2**: 판정 서버(직원이 누른 기능을 허용할지 정하는 A사 서버)가 거절한 요청 9개에서 한 사용자가 3번 이상 거절당한 기록을 고르고, Module 3 의 권한 판정 함수 `check_permission` 으로 거절 이유를 붙여 순서를 정하는 `access_detection.py` 를 씁니다.

**응용 3-1 ~ 3-3은 선택 실습입니다.** 핵심 실습과 문제 해결 기록을 마친 뒤 여유가 있을 때 합니다.

| 응용 | 하는 일 |
|---|---|
| 응용 3-1 | 로그인 실패 알림과 트래픽 급증 알림을 같은 모양으로 만들어 `alerts.json` 한 파일에 모읍니다 |
| 응용 3-2 | SaaS 로그에서 업무 시간 밖 로그인 · 평소와 다른 IP · 파일 대량 다운로드를 규칙마다 따로 찾습니다 |
| 응용 3-3 | 웹 로그에서 해킹 도구가 자주 요청하는 경로를 요청한 IP 를 찾습니다 |

다음 Unit 은 핵심 실습 3-2에서 만든 `access_detection.py` 를 여러 곳에서 불러 씁니다. 응용 3-2 · 3-3 에서 만드는 파일은 핵심 실습이나 다음 Unit의 핵심 경로에 필요하지 않습니다.

<h2>오늘 지킬 것</h2>

- 쓰는 도구는 **파이썬 · 판다스 · VS Code · 터미널 · git** 입니다.
- 이번 Unit 의 기준 숫자(급증은 평균의 3배, 반복 거절은 `REPEAT_LIMIT` 3번)는 **고정**하고, 값을 바꿔 가며 비교하지 않습니다.
- 샘플 이벤트의 날짜는 모두 2026-11-02 이고, 이야기 속 「오늘」은 이 날입니다. 57개 중 웹 서버 28개 · 판정 서버 15개(`source` 가 `server`) · SaaS 14개입니다.
- 코드 줄은 판다스로 쓰는 줄과 파이썬으로 쓰는 줄이 섞여 있습니다. 표를 읽고 고르고 세는 줄이 판다스이고, 판단 · 딕셔너리 · 리스트 · 함수 호출이 파이썬입니다.
- 초안에는 핵심 실습의 실행 결과와 확인 근거를 남깁니다. 문제를 이해하고 해결한 과정은 핵심 실습 뒤 GitHub 블로그에 기록합니다.

## 폴더 열고 이전 파일 확인하기

오늘 코드는 앞에서 만든 파일 몇 개를 불러 씁니다.

| 파일 | 만든 곳 | 오늘 쓰는 곳 | 없거나 안 풀렸을 때 |
|---|---|---|---|
| `normalized_events.json` | Unit 2 「시작하기」 | 모든 실습 | 다음 페이지에서 새로 만듭니다 |
| `rbac.py` | Module 3 Unit 1 실습 1-2 | 실습 3-2 | 다음 페이지에서 새로 만듭니다 |
| `config/users.json` · `config/roles.json` | Module 3 Unit 1 실습 1-1 | 실습 3-2 (`rbac.py` 가 읽음) | 다음 페이지에서 새로 만듭니다 |
| `login_detection.py` | Unit 2 실습 2-3 | 응용 3-1 만 | 아래 설명을 따릅니다 |

- Module 3 의 파일은 `network-study-notes/access_control` 폴더에 있고 오늘 작업 폴더는 `network-study-notes/anomaly_detection` 입니다. 따라서 필요한 `rbac.py` 와 두 설정 JSON 은 이 레슨에서 `anomaly_detection` 안에 별도로 만듭니다. `access_control` 폴더의 파일은 그대로 둡니다. 두 JSON 값은 [M3 Unit 1 실습 1-1의 정답 접기](__SITE__/exercises/module/3/unit/1/lesson/2/page/7), `rbac.py` 의 빈칸은 [M3 Unit 1 실습 1-2의 정답 접기](__SITE__/exercises/module/3/unit/1/lesson/3/page/4)에서 확인합니다. Module 3 Unit 1을 다 마치지 않았어도 필요한 내용을 이 레슨에서 다시 준비할 수 있습니다.
- `login_detection.py` 는 선택 실습 3-1에서만 씁니다. 만들 때는 [M4 Unit 2 실습 2-3의 코드와 정답 접기](__SITE__/exercises/module/4/unit/2/lesson/4/page/4)를 참고합니다.

<h2>순서</h2>

1. **[VS Code]** `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다. 터미널 오른쪽 위 이름 칸에 **bash** 가 보이는지 확인합니다. `powershell` 이면 `+` 옆의 **∨** 를 눌러 **Git Bash** 를 고릅니다. 새 터미널은 저장소 맨 위 폴더(`…/network-study-notes`)에서 열립니다(Module 3 Unit 1 시작하기에서 한 방법과 같습니다).
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치를 확인하고, 판다스가 설치돼 있는지 봅니다. <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, 마지막에 버전 번호(예: `2.3.3` 또는 `3.1.1`)가 나오면</mark> 됩니다. 판다스 3(`3.` 으로 시작)이면 일부 출력의 `dtype` 이름이 문서와 조금 다르게 나오고, 그 자리마다 따로 적어 두었습니다. `No module named 'pandas'` 가 나오면 이 레슨의 「오류가 나면」 둘째 줄을 따릅니다.
   ```bash
   cd anomaly_detection
   pwd
   python - <<'PY'
   import pandas

   print(pandas.__version__)
   PY
   ls
   ```
   - 명령 풀이: `cd` 폴더 안으로 들어감 · `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
   - `ls` 결과에 `login_detection.py` 와 `normalized_events.json` 이 보이면 Unit 2 파일이 있는 것입니다.

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 터미널을 열고 `anomaly_detection` 폴더로 들어가, 판다스 버전 번호가 나오는 것을 봤다
<!-- /checklist -->

3. **파일은 이렇게 만듭니다.** 모두 코드 상자에서 복사해 직접 만듭니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S` 로 저장합니다.
   - 핵심 실습 전에 [블로그 초안 준비](__SITE__/exercises/module/4/unit/3/lesson/8/page/1)에서 이번 유닛의 글 파일을 엽니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 이 Unit 뒤쪽의 정답을 봅니다.

**확인** — `pwd` 가 `…/anomaly_detection` 으로 끝나고 판다스 버전 번호가 나오면 성공입니다. 안 나오면 이 레슨의 「오류가 나면」 페이지를 봅니다.

## 오늘 쓸 파일 만들기

이 페이지의 파일 다섯 개를 모두 만든 뒤 맨 아래 3번으로 확인합니다.

1. **[터미널]** `anomaly_detection` 폴더에서, Module 3 설정 파일을 넣을 `config` 폴더(`anomaly_detection/config`)를 만듭니다. 이미 `config` 폴더가 있으면 건너뜁니다.
   ```bash
   mkdir config
   ls
   ```
   - 명령 풀이: `mkdir config` 폴더 만들기 · `ls` 폴더 안의 파일 이름 보기
2. **[VS Code]** 왼쪽 목록에서 `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 로 `normalized_events.json` · `baseline_traffic.csv` · `rbac.py` 를 만들고, `anomaly_detection` 폴더 안의 `config` 폴더를 오른쪽 클릭 › **New File** 로 `users.json` · `roles.json` 을 만들어 아래 내용을 그대로 붙여 넣습니다. `rbac.py` 는 `access_control` 이 아니라 `anomaly_detection` 바로 아래(`anomaly_detection/rbac.py`)에 둡니다.

<h2><code>normalized_events.json</code></h2>

Unit 2 시작하기에서 만든 것과 같은 이벤트 샘플 57개입니다. 실습 3-1 · 3-2 와 응용이 모두 읽습니다. <mark>같은 이름의 파일이 이미 있어도 아래 내용으로 덮어씁니다</mark>(출력이 문서와 같아야 하기 때문입니다). `null` 은 그 값이 로그에 없다는 뜻입니다.

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
- [ ] `anomaly_detection` 폴더에 `normalized_events.json` 을 만들어 붙여 넣고 저장했다
<!-- /checklist -->

<h2><code>baseline_traffic.csv</code></h2>

실습 3-1 에서 씁니다. 지난 7일 동안 오전 9시대에 웹 서버로 들어온 요청이 **1분에 평균 몇 번**이었는지 적은 연습용 숫자입니다. 첫 줄은 헤더(열 이름이 적힌 줄)이고, 둘째 줄부터 한 줄이 하루입니다. 샘플의 웹 서버 이벤트도 모두 9시대입니다.

```
date,requests_per_minute
2026-10-26,2
2026-10-27,2
2026-10-28,3
2026-10-29,2
2026-10-30,1
2026-10-31,2
2026-11-01,2
```

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 `baseline_traffic.csv` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

<h2><code>rbac.py</code></h2>

실습 3-2 에서 씁니다. Module 3 Unit 1 실습 1-2 에서 만든 권한 판정 파일의 완성본입니다. `check_permission(사용자, 자원, 행위)` 가 `(허용 여부, 이유)` 를 리턴합니다.

```python
import json                                                      # JSON 파일을 읽는 모듈을 불러온다

with open("config/roles.json", encoding="utf-8") as roles_file:  # 역할 파일을 연다
    ROLES = json.load(roles_file)                                # 역할 → 권한 리스트 딕셔너리로 읽는다
with open("config/users.json", encoding="utf-8") as users_file:  # 사용자 파일을 연다
    USERS = json.load(users_file)                                # 사용자 → 정보 딕셔너리로 읽는다


def check_permission(user, resource, action):                    # 사용자 · 자원 · 행위를 받는 함수
    """요청을 허용할지 (허용 여부, 이유)로 리턴한다. 요청이 들어올 때 가장 먼저 쓰는 판정이고, 허용 리스트에 없으면 모두 거부한다."""
    if user not in USERS:                                        # 사용자 파일에 없는 계정이면
        return False, "등록되지 않은 사용자"                     # 바로 거부하고 함수를 끝낸다
    if not USERS[user]["employed"]:                              # 재직 중이 아니면
        return False, "퇴사한 계정"                              # 거부하고 함수를 끝낸다
    role = USERS[user]["role"]                                   # 이 사용자의 역할을 꺼낸다
    if role not in ROLES:                                        # 역할 파일에 없는 역할이면
        return False, "역할이 없음"                              # 거부하고 함수를 끝낸다
    permission = f"{resource}:{action}"                          # "자원:행위" 모양 문자열로 합친다
    if permission not in ROLES[role]:                            # 그 역할의 권한 리스트에 없으면
        return False, "권한 없음"                                # 거부하고 함수를 끝낸다
    return True, "허용"                                          # 모든 검사를 지나면 허용한다
```

읽는 법: 자원은 다루는 대상이고, 행위는 그 대상에 하는 일입니다.

| 이름 | 종류 | 뜻 |
|---|---|---|
| `SALES` | 자원 | 영업 실적 |
| `SETTLE` | 자원 | 정산 내역 |
| `ACCOUNT` | 자원 | 계정 |
| `QUERY` | 행위 | 조회 |
| `CHANGE` | 행위 | 변경 |

함수는 아래 검사를 차례로 보고, 처음 걸린 곳의 이유를 돌려줍니다.

| 순서 | 검사 | 걸리면 돌려주는 이유 |
|---|---|---|
| 1 | 등록된 사용자인가 | 등록되지 않은 사용자 |
| 2 | 재직 중인가 | 퇴사한 계정 |
| 3 | 역할이 있는가 | 역할이 없음 |
| 4 | 그 역할에 「자원:행위」 권한이 있는가 | 권한 없음 |
| 끝 | 네 검사를 모두 지났는가 | 허용 |

- 예를 들어 dami 는 `users.json` 에서 `employed` 가 `false` 라서 둘째 검사에서 「퇴사한 계정」이 됩니다.
- 이 파일은 불러오는(`import`) 순간 `config/roles.json` · `config/users.json` 을 지금 터미널 위치 기준으로 읽습니다. 그래서 `config` 폴더가 `anomaly_detection` 안에 있어야 하고, 실행도 그 폴더에서 합니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 `rbac.py` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

<h2><code>config/users.json</code></h2>

Module 3 Unit 1 실습 1-1 의 사용자 파일입니다. 사용자마다 역할과 재직 여부(`employed`)가 있습니다.

```
{
  "seoyeon": {"role": "sales", "employed": true},
  "junho": {"role": "finance", "employed": true},
  "gaeun": {"role": "account_admin", "employed": true},
  "dami": {"role": "sales", "employed": false},
  "batch-night": {"role": "batch", "employed": true},
  "tester": {"role": "intern", "employed": true}
}
```

<h2><code>config/roles.json</code></h2>

Module 3 Unit 1 실습 1-1 의 역할 파일입니다. 역할마다 허용된 권한 리스트가 있습니다.

```
{
  "sales": ["SALES:QUERY", "SALES:CHANGE"],
  "account_admin": ["ACCOUNT:QUERY", "ACCOUNT:CHANGE"],
  "finance": ["SALES:QUERY", "SETTLE:QUERY"],
  "batch": ["SETTLE:QUERY"],
  "auditor": ["SALES:QUERY", "SETTLE:QUERY", "ACCOUNT:QUERY"]
}
```

<!-- checklist -->
- [ ] `config` 폴더를 만들고 그 안에 `config/users.json` · `config/roles.json` 을 만들어 붙여 넣고 저장했다
<!-- /checklist -->

3. **[터미널]** <mark>파일이 정상인지 확인합니다</mark>.
   ```bash
   python - <<'PY'
   import json
   from pathlib import Path
   from rbac import check_permission

   with open("normalized_events.json", encoding="utf-8") as events_file:
       print(len(json.load(events_file)))

   traffic_lines = Path("baseline_traffic.csv").read_text(encoding="utf-8").splitlines()
   print(len(traffic_lines))
   print(check_permission("dami", "SALES", "QUERY"))
   PY
   ```
   - <mark>순서대로 `57`, `8`(헤더 줄 포함), `(False, '퇴사한 계정')` 이 나와야</mark> 합니다.

   | 다르게 나온 것 | 원인 · 고치는 법 |
   |---|---|
   | 둘째 줄이 `8` 이 아님 | `baseline_traffic.csv` 에 줄이 빠졌거나 빈 줄이 들어간 것이니 다시 붙여 넣습니다 |
   | 셋째 줄이 다름 | `rbac.py` 내용이나 두 JSON 파일의 위치(`config` 폴더 안인지)를 다시 봅니다 |

**확인** — 세 명령이 차례로 `57`, `8`, `(False, '퇴사한 계정')` 을 내면 성공입니다. 안 나오면 위 표에서 다르게 나온 줄을 찾아 고친 뒤 세 명령을 다시 칩니다.

<!-- checklist -->
- [ ] 확인 명령 세 개가 차례로 `57`, `8`, `(False, '퇴사한 계정')` 을 냈다
<!-- /checklist -->

## 오류가 나면

먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.

| 오류 | 원인 | 고치는 법 |
|---|---|---|
| `No module named 'pandas'` | <mark>판다스가 설치되지 않은 터미널입니다</mark> | `python -m pip install pandas` 를 칩니다 |
| `FileNotFoundError: … 'config/roles.json'` · `No module named 'rbac'` | 파일 위치가 다릅니다 | <mark>`config` 폴더 안에 두 JSON 파일이 있는지</mark>, `rbac.py` 가 `anomaly_detection` 폴더 바로 아래에 있는지 `ls` 와 `ls config` 로 봅니다 |
| `No module named 'login_detection'`(응용 3-1) | Unit 2 실습 2-3 의 `login_detection.py` 가 없습니다 | 「폴더 열고 이전 파일 확인하기」 페이지의 표 아래 설명대로 만듭니다 |

- 가상환경을 쓴다면 판다스를 설치하기 전에 `network-study-notes` 폴더에서 가상환경을 켭니다(`source .venv/Scripts/activate`).
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 각 실습 아래 정답 접기를 보고, 풀리지 않으면 초안에 오류와 막힌 지점을 남깁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다. **앞 Unit 과 Module 3 의 파일은 고치지 않습니다.**

**확인** — 위 표대로 고친 뒤 「오늘 쓸 파일 만들기」 페이지의 확인 코드가 `57`, `8`, `(False, '퇴사한 계정')` 을 내면 성공입니다. 그래도 안 되면 오류와 막힌 지점을 초안에 남기고 실습 3-1 로 넘어갑니다.

---
