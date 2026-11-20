---
id: m4-u03-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표와 오늘의 계획

실습 2-3 에서는 같은 주소가 로그인에 몇 번 실패했는지 세어 알림 기준을 정했습니다. 오늘은 탐지 규칙을 두 개 더 만듭니다. 하나는 **요청이 갑자기 늘어난 때(트래픽 급증, traffic spike)** 를 찾는 규칙이고, 다른 하나는 **같은 사람이 여러 번 거절당한 기록**을 찾아 거절 이유로 순서를 정하는 규칙입니다.

**오늘의 계획 (3시간)**

1. 시작하기 15분: 이 레슨을 읽고, 오늘 쓸 데이터 파일과 Module 3 의 권한 판정 파일을 만듭니다.
2. 실습 약 110분: 핵심 실습 두 개를 차례로 합니다.
3. 글쓰기 40분: 「보고서 쓰기」 레슨에서 핵심 실습의 질문에 답하고, 「오늘의 글 쓰기」 레슨에서 글 한 편을 씁니다.
4. 마무리 15분: 실습 3-2 끝의 「이번 Unit 마무리」에서 파일을 확인하고 깃허브에 올립니다.

**오늘 만들 것 두 가지**

1. **실습 3-1**: 웹 서버 요청을 분마다 세고, 지난 7일 평균의 3배 이상으로 늘어난 분을 찾는 `traffic_detection.py` 를 씁니다.
2. **실습 3-2**: 판정 서버가 거절한 요청 9개에서 한 사용자가 3번 이상 거절당한 기록을 고르고, Module 3 의 권한 판정 함수 `check_permission` 으로 거절 이유를 붙여 순서를 정하는 `access_detection.py` 를 씁니다.

**도전 3-1 ~ 3-3은 선택입니다.** 핵심 실습 두 개와 글쓰기를 마치고 시간이 남을 때 합니다.

- 도전 3-1: 로그인 실패 알림과 트래픽 급증 알림을 같은 모양으로 만들어 `alerts.json` 한 파일에 모읍니다.
- 도전 3-2: SaaS 로그에서 업무 시간 밖 로그인 · 평소와 다른 IP · 파일 대량 다운로드를 규칙마다 따로 찾습니다.
- 도전 3-3: 웹 로그에서 해킹 도구가 자주 요청하는 경로를 요청한 IP 를 찾습니다.

다음 Unit 은 실습 3-2 의 `access_detection.py` 를 여러 곳에서 불러 씁니다. 도전 3-2 · 3-3 의 파일은 다음 Unit 「제공 파일」 레슨에 완성본이 있으므로, 도전을 하지 않아도 다음 Unit 을 따라갈 수 있습니다.

**오늘 지킬 것**

- 쓰는 도구는 **파이썬 · 판다스 · VS Code · 터미널 · git** 입니다.
- 이번 Unit 의 기준 숫자(급증은 평균의 3배, 반복 거절은 `REPEAT_LIMIT` 3번)는 **고정**하고, 값을 바꿔 가며 비교하지 않습니다.
- 샘플 이벤트의 날짜는 모두 2026-11-02 이고, 이야기 속 「오늘」은 이 날입니다. 57개 중 웹 서버 28개 · 판정 서버 15개(`source` 가 `server`) · SaaS 14개입니다.
- 코드 줄은 판다스로 쓰는 줄과 파이썬으로 쓰는 줄이 섞여 있습니다. 표를 읽고 고르고 세는 줄이 판다스이고, 판단 · 딕셔너리 · 리스트 · 함수 호출이 파이썬입니다.
- 보고서에서 `[핵심 질문]` 표시가 붙은 질문은 그 실습에서 꼭 알아야 할 질문이고, 내 출력이나 샘플 데이터의 값을 근거로 이유까지 씁니다.

## 폴더 열고 이전 파일 확인하기

오늘 코드는 앞에서 만든 파일 몇 개를 불러 씁니다.

| 파일 | 만든 곳 | 오늘 쓰는 곳 | 없거나 안 풀렸을 때 |
|---|---|---|---|
| `normalized_events.json` | Unit 2 「시작하기」 | 모든 실습 | 다음 페이지에서 새로 만듭니다 |
| `rbac.py` | Module 3 Unit 1 실습 1-2 | 실습 3-2 | 다음 페이지에서 새로 만듭니다 |
| `config/users.json` · `config/roles.json` | Module 3 Unit 1 실습 1-1 | 실습 3-2 (`rbac.py` 가 읽음) | 다음 페이지에서 새로 만듭니다 |
| `login_detection.py` | Unit 2 실습 2-3 | 도전 3-1 만 | 아래 설명을 따릅니다 |

- Module 3 의 파일은 `access_control` 폴더에 있고 오늘 작업 폴더는 `anomaly_detection` 입니다. 그래서 `rbac.py` 와 설정 파일 두 개를 다음 페이지의 완성본으로 `anomaly_detection` 폴더에 **새로** 만듭니다. 내용은 Module 3 Unit 1 정답 레슨의 「실습 1-1 정답」 · 「실습 1-2 정답」과 같으니, Module 3 을 다 마쳤든 못 마쳤든 그대로 붙여 넣으면 됩니다.
- `login_detection.py` 는 도전 3-1 에서만 씁니다. 없으면 Unit 2 실습 2-3 레슨의 `login_detection.py` 코드 상자를 붙여 넣고, Unit 2 정답 레슨의 「실습 2-3 정답」에 있는 채운 코드를 빈칸 자리에 넣어 완성합니다.

**순서**

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치를 확인하고, 판다스가 설치돼 있는지 봅니다(맥북은 `python3`). <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, 마지막에 버전 번호(예: `2.3.3`)가 나오면</mark> 됩니다. `No module named 'pandas'` 가 나오면 이 레슨의 「오류가 나면」 둘째 줄을 따릅니다.
   ```bash
   cd anomaly_detection
   pwd
   python -c "import pandas; print(pandas.__version__)"
   ls
   ```
   - 명령 풀이: `cd` 폴더 안으로 들어감 · `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
   - `ls` 결과에 `login_detection.py` 와 `normalized_events.json` 이 보이면 Unit 2 파일이 있는 것입니다.
3. **파일은 이렇게 만듭니다.** 따로 내려받는 파일은 없고, 모두 코드 상자에서 복사해 만듭니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u3.md` 는 「보고서 쓰기」 레슨의 틀을 복사해 만듭니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 이 Unit 뒤쪽의 정답을 봅니다.

## 오늘 쓸 파일 만들기

이 페이지의 파일 다섯 개를 모두 만든 뒤 맨 아래 3번으로 확인합니다.

1. **[터미널]** Module 3 설정 파일을 넣을 `config` 폴더를 만듭니다. 이미 `config` 폴더가 있으면 건너뜁니다.
   ```bash
   mkdir config
   ls
   ```
   - 명령 풀이: `mkdir config` 폴더 만들기 · `ls` 폴더 안의 파일 이름 보기
2. **[VS Code]** `anomaly_detection` 폴더에 `normalized_events.json` · `baseline_traffic.csv` · `rbac.py` 를, 그 안의 `config` 폴더에 `users.json` · `roles.json` 을 만들어 아래 내용을 그대로 붙여 넣습니다.

**`normalized_events.json`** — Unit 2 시작하기에서 만든 것과 같은 이벤트 샘플 57개입니다. 실습 3-1 · 3-2 와 도전이 모두 읽습니다. <mark>같은 이름의 파일이 이미 있어도 아래 내용으로 덮어씁니다</mark>(출력이 문서와 같아야 하기 때문입니다). `null` 은 그 값이 로그에 없다는 뜻입니다.

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

**`baseline_traffic.csv`** — 실습 3-1 에서 씁니다. 지난 7일 동안 오전 9시대에 웹 서버로 들어온 요청이 **1분에 평균 몇 번**이었는지 적은 연습용 숫자입니다. 첫 줄은 헤더(열 이름이 적힌 줄)이고, 둘째 줄부터 한 줄이 하루입니다. 샘플의 웹 서버 이벤트도 모두 9시대입니다.

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

**`rbac.py`** — 실습 3-2 에서 씁니다. Module 3 Unit 1 실습 1-2 에서 만든 권한 판정 파일의 완성본입니다. `check_permission(사용자, 자원, 행위)` 가 `(허용 여부, 이유)` 를 리턴합니다.

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

**`config/users.json`** — Module 3 Unit 1 실습 1-1 의 사용자 파일입니다. 사용자마다 역할과 재직 여부(`employed`)가 있습니다.

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

**`config/roles.json`** — Module 3 Unit 1 실습 1-1 의 역할 파일입니다. 역할마다 허용된 권한 리스트가 있습니다.

```
{
  "sales": ["SALES:QUERY", "SALES:CHANGE"],
  "account_admin": ["ACCOUNT:QUERY", "ACCOUNT:CHANGE"],
  "finance": ["SALES:QUERY", "SETTLE:QUERY"],
  "batch": ["SETTLE:QUERY"],
  "auditor": ["SALES:QUERY", "SETTLE:QUERY", "ACCOUNT:QUERY"]
}
```

3. **[터미널]** <mark>파일이 정상인지 확인합니다</mark>(맥북은 `python3`).
   ```bash
   python -c "import json; print(len(json.load(open('normalized_events.json', encoding='utf-8'))))"
   python -c "print(len(open('baseline_traffic.csv', encoding='utf-8').read().splitlines()))"
   python -c "from rbac import check_permission; print(check_permission('dami', 'SALES', 'QUERY'))"
   ```
   - <mark>순서대로 `57`, `8`(헤더 줄 포함), `(False, '퇴사한 계정')` 이 나와야</mark> 합니다.
   - `8` 이 아니면 `baseline_traffic.csv` 에 줄이 빠졌거나 빈 줄이 들어간 것이니 다시 붙여 넣습니다. 셋째 줄이 다르면 `rbac.py` 내용이나 두 JSON 파일의 위치(`config` 폴더 안인지)를 다시 봅니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `No module named 'pandas'`: <mark>가상환경이 활성화되지 않은 터미널입니다</mark>. `security-agent-toolkit` 폴더에서 가상환경을 활성화한 뒤(`source .venv/Scripts/activate`, 맥북은 `Scripts` 를 `bin` 으로, 폴더 이름이 다르면 그 이름으로) `python -m pip install pandas` 를 칩니다.
- `FileNotFoundError: … 'config/roles.json'` · `No module named 'rbac'`: <mark>`config` 폴더 안에 두 JSON 파일이 있는지</mark>, `rbac.py` 가 `anomaly_detection` 폴더 바로 아래에 있는지 `ls` 와 `ls config` 로 봅니다.
- `No module named 'login_detection'`(도전 3-1): Unit 2 실습 2-3 의 `login_detection.py` 가 없는 것입니다. 「폴더 열고 이전 파일 확인하기」 페이지의 표 아래 설명대로 만듭니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 이 Unit 뒤쪽의 「정답」을 보고</mark>, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다. **앞 Unit 과 Module 3 의 파일은 고치지 않습니다.**

---
