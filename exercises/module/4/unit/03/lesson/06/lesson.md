---
id: m4-u03-l06
title: 도전 3-3 · 웹 로그에서 경로를 스캔한 IP 찾기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/106_day04_am_suspicious_logs.md
  mission_id: GichanSource.m4-1105-am-suspicious-logs
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 도전 3-3 · 웹 로그에서 경로를 스캔한 IP 찾기

## 이번 의뢰: 경로 스캔 IP 찾기

> **선택입니다. 시간이 남을 때 합니다.** 핵심 실습 3-1 · 3-2와 글쓰기를 먼저 마칩니다. 이 도전에서 만드는 `malicious_detection.py` 는 다음 Unit 「제공 파일」 레슨에 완성본이 있으므로, 하지 않아도 다음 Unit 을 따라가는 데 문제가 없습니다.

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「웹 서버(우리 서비스 화면을 보여 주는 서버)의 11/2 실패 기록이 13건 있습니다. 이 중에 `/.env` · `/phpmyadmin` 처럼 일반 사용자는 열 일이 없는 경로(아래에서 설명합니다)를 요청한 IP 가 있습니다. 해킹 도구가 접근할 수 있는 곳이 있는지 경로를 차례로 요청해 본 것 같습니다.
>
> 그런데 사용자가 경로를 잘못 입력하거나 없는 게시글을 요청해도 똑같이 실패로 기록됩니다. 해킹 도구가 자주 요청하는 경로를 요청한 IP 만 가려 주세요.」
> - **왜 중요한가**: <mark>실패를 모두 알림으로 보내면 알림이 너무 많아져서, 담당자가 진짜 경로 스캔을 놓칠 수 있습니다.</mark>

## 왜 실패 중에서 스캔만 가려내는가

1. 웹 서버는 요청이 처리되지 않으면 실패로 기록합니다(없는 경로를 요청하면 404 라는 HTTP 상태 코드가 남습니다. HTTP 상태 코드는 서버가 요청을 처리한 결과를 나타내는 숫자입니다).
2. 해킹 도구는 접근할 수 있는 곳을 찾으려고 <mark>**정해진 경로를 차례로 요청**</mark>합니다. 자주 요청하는 경로는 이렇습니다.

   | 경로 | 무엇인가 |
   |---|---|
   | `/.env` | 비밀번호와 키가 든 설정 파일 |
   | `/wp-login.php` | 워드프레스 로그인 화면 |
   | `/phpmyadmin` | 데이터베이스 관리 화면 |

3. 이번 실습의 질문은 하나입니다. <mark>실패한 요청 중에 이 경로를 요청한 IP 가 있는가?</mark> 이 경로 중 하나를 요청했으면 이번 규칙의 기준에서는 스캔으로 봅니다(공격으로 확정하는 것은 아닙니다).

## 3.1 웹 실패 로그에서 스캔 찾기

샘플에서 `source` 가 `web` 이고 `result` 가 `실패` 인 이벤트는 13개입니다. IP 별로 실패한 요청을 정리하면 이렇습니다.

| IP | 실패한 요청 | 스캐너 경로를 요청했나 | 이번 규칙 결과 |
|---|---|---|---|
| 198.51.100.21 | `GET /board/99` | 아니오 | 제외 |
| 198.51.100.34 | `GET /report` | 아니오 | 제외 |
| 198.51.100.77 | `GET /admin` | 아니오 | 제외 |
| 198.51.100.90 | `GET /.env` · `GET /wp-login.php` · `GET /phpmyadmin` | **예** | **스캔** |
| 203.0.113.50 | `POST /login` 5번 · `GET /admin` · `GET /admin/users` | 아니오 | 제외 |

- `SCANNER_PATTERN` 은 `"/.env|/wp-login|/phpmyadmin"` 입니다. 따옴표 안의 `|` 는 「또는」이라는 뜻이라, <mark>셋 중 하나가 들어 있으면</mark> 해당합니다. 조건끼리 합치는 기호가 아니라, 문자열 안에 쓴 글자일 뿐입니다.
- 203.0.113.50 은 실패가 7번이지만 로그인과 관리자 화면 실패라서 스캐너 경로가 없습니다. 이 IP 는 로그인 실패 규칙에서 따로 다룹니다.

**판다스 문법 상자 — 문자열이 들어 있는지 `str.contains`**

**<mark>`열.str.contains("문자열")`</mark> 은 열의 값 안에 그 문자열이 들어 있으면 `True`, 없으면 `False` 를 줍니다**

`.str` 은 열의 각 값을 문자열로 다루겠다는 표시입니다. 문자열 안의 `|` 는 「또는」이라는 뜻입니다. 아래는 웹 서버가 받은 요청 경로이고, `/.env` 나 `/phpmyadmin` 이 들어 있는 요청을 찾습니다.

```python
import pandas as pd  # 판다스를 pd 라는 짧은 이름으로 불러온다

data = {                                                                     # 표에 넣을 내용(열 이름: 값들)
    "ip": ["198.51.100.90", "192.0.2.15", "198.51.100.90", "203.0.113.50"],  # ip 열
    "path": ["/.env", "/board", "/phpmyadmin", "/board/12"],                 # path 열
}
df = pd.DataFrame(data)                                                      # 내용으로 표(DataFrame)를 만든다
print(df)                                                                    # 표를 출력한다
```

실행 결과:

```
              ip         path
0  198.51.100.90        /.env
1     192.0.2.15       /board
2  198.51.100.90  /phpmyadmin
3   203.0.113.50    /board/12
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
is_scanner = df["path"].str.contains("/.env|/phpmyadmin")  # path 에 둘 중 하나가 들어 있는지 확인한다
print(is_scanner)                                          # True · False 를 출력한다
```

실행 결과:

```
0     True
1    False
2     True
3    False
Name: path, dtype: bool
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
scanner_df = df[is_scanner]  # True 인 행만 남긴다
print(scanner_df)            # 남은 요청을 출력한다
```

실행 결과:

```
              ip         path
0  198.51.100.90        /.env
2  198.51.100.90  /phpmyadmin
```

- 읽는 법: <mark>`/.env` 가 든 0번 행과 `/phpmyadmin` 이 든 2번 행이 `True`</mark> 입니다. 세 번째 출력은 그 두 행만 남은 표입니다.
- 열의 문자열 기능은 `.str.` 을 먼저 쓰고 부릅니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `load_events` | 파일 경로 | 이벤트 표(미리 채움) |
| `pick_web_failures` | 이벤트 표 | 웹 실패 표(미리 채움) |
| `find_scan_ips` | 웹 실패 표 | 스캔 IP 리스트와 IP 별 요청 횟수 |
| `explain_scan` | IP · 요청 횟수 | 설명 딕셔너리 |

**직접 쓰는 곳은 여섯 군데**(번호 1 ~ 6)이고, 함수 두 개 안에 나뉘어 있습니다.

| 함수 | 번호 | 직접 쓰는 일 |
|---|---|---|
| `find_scan_ips` | 1 ~ 4번 | 스캐너 경로가 있는지 구하고, 그 요청만 골라 IP 별로 몇 번 요청했는지 셉니다 |
| `explain_scan` | 5 · 6번 | 요청 횟수를 문자열로 바꿔 이유 문장을 만들고, IP 와 이유를 딕셔너리로 만듭니다 |

## 도전 3-3 · 웹 로그에서 경로를 스캔한 IP 찾기

**이런 상황이 있습니다**

- **지금은**: <mark>웹 실패 로그 13개에서 사용자의 잘못된 경로 요청과 스캐너 경로 요청이 섞여 있어, 먼저 확인할 IP 를 구분하기 어렵습니다</mark>.
- **그래서 만드는 것**: `malicious_detection.py` 입니다.
  - 실패한 요청에서 스캐너가 요청하는 경로를 찾습니다.
  - 그 경로를 요청한 IP 와 횟수를 셉니다.
  - 스캔으로 본 IP 마다 이유 설명을 만듭니다.
- **실행하면**: <mark>단계 1: 웹 실패 수, 단계 2: 스캐너 경로를 요청한 IP 와 횟수, 단계 3: 스캔으로 본 IP 와 이유, 단계 4: 스캐너 경로가 없어 제외한 IP 가 나옵니다.</mark>
- **현업에서는**: 경로 스캔은 알림으로 남기고, 로그인 실패만 있는 IP 는 따로 봅니다. 제외한 IP 와 이유를 기록해 두면 이후에 규칙을 검토할 때 참고할 수 있습니다.

**할 일**

1. `malicious_detection.py` · `challenge3-3_run.py` 두 파일을 만들고, `malicious_detection.py` 의 두 함수에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>웹 실패 수</mark>(단계 1), <mark>스캐너 경로를 요청한 IP</mark>(단계 2), <mark>스캔으로 본 IP</mark>(단계 3), <mark>제외한 IP</mark>(단계 4)를 읽습니다.
3. 마지막으로 `advanced_detection.py` 를 만들어 이번 Unit의 탐지 3개를 한 번에 돌려 봅니다.

**`malicious_detection.py`**

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"                # 읽을 정규화 이벤트 파일 이름
SCANNER_PATTERN = "/.env|/wp-login|/phpmyadmin"       # 스캐너가 자주 요청하는 경로. | 는 「또는」이라는 뜻이다


def load_events(path):                                # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                       # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                     # 이벤트 표를 리턴한다


def pick_web_failures(events):                        # 이벤트 표를 받는 함수
    """웹 서버 로그에서 실패한 이벤트만 골라 새 표로 만든다.
    경로 스캔 요청을 찾기 전에 쓴다.
    """
    sources = events["source"]                        # source 열만 꺼낸다
    is_web = sources == "web"                         # 각 행이 웹 서버 이벤트인지 비교해 True 또는 False 를 만든다
    results = events["result"]                        # result 열만 꺼낸다
    is_fail = results == "실패"                       # 각 행이 실패인지 비교해 True 또는 False 를 만든다
    both_true = is_web & is_fail                      # 두 조건이 모두 True 인 행만 True 로 만든다
    web_failures = events[both_true]                  # True 인 행만 골라 새 표로 만든다
    return web_failures                               # 웹 실패 이벤트 표를 리턴한다


def find_scan_ips(web_failures):                      # 웹 실패 표를 받는 함수
    """스캐너가 요청하는 경로를 요청한 IP 와 요청 횟수를 찾는다.
    한 번의 오타 요청이나 로그인 실패만 있는 IP 를 거르고 경로 스캔만 가려낼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. web_failures 의 "action" 열을 꺼내 actions 에 담는다
    # 2. actions 에 .str.contains(SCANNER_PATTERN) 을 붙여 스캐너 경로가 들어 있는지 구해 is_scanner 에 담는다
    # 3. web_failures 에서 is_scanner 가 True 인 행만 골라 scanner_rows 에 담는다
    # 4. scanner_rows 의 "ip" 열에 .value_counts() 를 붙여 IP 별로 몇 번 요청했는지 세어 scan_counts 에 담는다
    scan_ips = list(scan_counts.index)                # 스캔으로 보는 IP 이름만 리스트로 만든다
    return scan_ips, scan_counts                      # 스캔 IP 리스트와 IP 별 요청 횟수를 리턴한다


def explain_scan(ip, request_count):                  # IP 와 스캐너 경로 요청 횟수를 받는 함수
    """스캔으로 본 IP 하나를 담당자가 읽을 설명 딕셔너리로 만든다.
    왜 의심했는지 이유를 알림에 남길 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. "스캐너 경로를 " 와 str(request_count) 와 "번 요청" 을 + 로 연결해 reason 에 담는다 (문구는 복사해 붙여도 된다)
    # 6. 키 "ip" 에 ip, 키 "reason" 에 reason 을 담은 딕셔너리를 scan_info 에 담는다
    return scan_info                                  # 설명 딕셔너리를 리턴한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 6번은 모두 함수 안이라 앞에 공백 4개입니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.**
- 채우기 전에 실행하면 `NameError: name 'scan_counts' is not defined` 오류가 납니다. 1 ~ 4번을 아직 안 썼기 때문입니다.

**`challenge3-3_run.py`** — 그대로 붙여 넣습니다. 직접 쓰는 줄은 없습니다. `scan_counts[ip]` 는 센 결과에서 그 IP 의 횟수를 꺼내고, `.unique()` 는 열의 값을 중복 없이 한 번씩만 모읍니다.

```python
from malicious_detection import load_events, pick_web_failures, find_scan_ips, explain_scan, EVENTS_PATH  # 방금 만든 함수를 불러온다

events = load_events(EVENTS_PATH)                            # 이벤트 파일을 표로 읽는다
web_failures = pick_web_failures(events)                     # 웹 서버의 실패 이벤트만 골라낸다
web_failure_count = len(web_failures)                        # 웹 실패가 모두 몇 개인지 센다
print("--- 단계 1: 웹 서버의 실패 이벤트", web_failure_count, "개")  # 단계 1 시작을 알리는 줄과 개수

scan_ips, scan_counts = find_scan_ips(web_failures)          # 스캔 IP 와 IP 별 요청 횟수를 찾는다
print("--- 단계 2: 스캐너 경로를 요청한 IP 와 횟수")          # 단계 2 시작을 알리는 줄
print(scan_counts)                                           # IP 와 요청 횟수를 출력한다

print("--- 단계 3: 스캔으로 본 IP 와 이유")                   # 단계 3 시작을 알리는 줄
for ip in scan_ips:                                          # 스캔 IP 를 하나씩 꺼낸다
    request_count = scan_counts[ip]                          # 그 IP 의 요청 횟수를 꺼낸다
    scan_info = explain_scan(ip, request_count)              # 이유 설명을 만든다
    print(scan_info)                                         # 설명을 출력한다

print("--- 단계 4: 스캐너 경로가 없어 제외한 IP")              # 단계 4 시작을 알리는 줄
all_ips = web_failures["ip"].unique()                        # 웹 실패 이벤트에 나온 IP 를 중복 없이 모은다
for ip in all_ips:                                           # IP 를 하나씩 꺼낸다
    if ip not in scan_ips:                                   # 스캔 IP 에 없으면
        print(ip)                                            # 제외한 IP 를 출력한다
```

**`advanced_detection.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 실습 3-2 · 도전 3-2 · 도전 3-3 에서 만든 함수를 모두 불러 한 번에 돌립니다. `list(열)` 은 열의 값을 리스트로 만듭니다. 도전 3-2 의 `saas_detection.py` 를 만들지 않았다면 이 파일은 건너뜁니다(`No module named 'saas_detection'` 오류가 납니다).

```python
from access_detection import load_events, pick_server_failures, pick_suspicious, EVENTS_PATH  # 실습 3-2 함수를 불러온다
from saas_detection import pick_saas, pick_logins, find_off_hours_logins, find_new_ip_users, find_bulk_download_users  # 도전 3-2 함수를 불러온다
from malicious_detection import pick_web_failures, find_scan_ips  # 도전 3-3 함수를 불러온다

events = load_events(EVENTS_PATH)                            # 이벤트 파일을 표로 읽는다

server_failures = pick_server_failures(events)               # 판정 서버 실패 이벤트를 고른다
suspicious = pick_suspicious(server_failures)                # 실패가 반복된 사용자의 이벤트를 고른다
suspicious_count = len(suspicious)                           # 그 이벤트가 몇 개인지 센다
print("판정 서버: 먼저 확인할 실패 이벤트", suspicious_count, "개")  # 판정 서버 탐지 결과를 출력한다

saas = pick_saas(events)                                     # SaaS 이벤트를 고른다
logins = pick_logins(saas)                                   # 로그인 이벤트를 고른다
off_hours_logins = find_off_hours_logins(logins)             # 업무 시간 밖 로그인을 찾는다
off_hours_users = list(off_hours_logins["user"])             # 그 로그인의 사용자 이름만 리스트로 만든다
new_ip_users = find_new_ip_users(logins)                     # 평소와 다른 IP 로 로그인한 사용자를 찾는다
bulk_users = find_bulk_download_users(saas)                  # 대량 다운로드 사용자를 찾는다
print("SaaS: 업무 시간 밖", off_hours_users, "· 평소와 다른 IP", new_ip_users, "· 대량 다운로드", bulk_users)  # SaaS 탐지 결과를 출력한다

web_failures = pick_web_failures(events)                     # 웹 서버 실패 이벤트를 고른다
scan_ips, scan_counts = find_scan_ips(web_failures)          # 스캔으로 본 IP 를 찾는다
print("웹 서버: 스캔으로 본 IP", scan_ips)                   # 웹 탐지 결과를 출력한다
```

**순서**

1. **[VS Code]** 파일 `malicious_detection.py` · `challenge3-3_run.py` · `advanced_detection.py` 를 만들어 위 코드를 붙여 넣습니다.
2. **[VS Code]** `malicious_detection.py` 에서 <mark>직접 쓰는 곳 여섯 군데를 씁니다</mark>. 3.1 의 판다스 문법 상자와 표를 보고 씁니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   pwd
   python challenge3-3_run.py
   python advanced_detection.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행
4. 출력은 **두 번** 나옵니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다.

   | 출력 | 줄 수 |
   |---|---|
   | `challenge3-3_run.py` 단계 1 | 0줄(숫자가 제목 줄에 함께 나옴) |
   | `challenge3-3_run.py` 단계 2 | 3줄 |
   | `challenge3-3_run.py` 단계 3 | 1줄 |
   | `challenge3-3_run.py` 단계 4 | 4줄 |
   | `advanced_detection.py` | 3줄 |
5. **[보고서]** `report_u3.md` 의 `## 도전 3-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 스캔으로 본 IP 와 이유를 적어 주세요.
   - (나) [핵심 질문] 203.0.113.50 은 실패한 요청이 7번 있지만 스캔에서 제외됐습니다. 제외된 이유와, 제외하지 않으면 담당자에게 어떤 일이 생기는지 적어 주세요.
   - (다) [핵심 질문] 198.51.100.21 의 `GET /board/99` 실패 1건은 이 규칙에서 어떤 조건 때문에 제외되나요? 그리고 해킹 도구가 `SCANNER_PATTERN` 에 없는 경로(예: `/backup.zip`)를 요청하면 이 규칙이 탐지하지 못한다는 점을 설명해 주세요.

## 도전 3-3 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 문자열이 들어 있는지 | `is_scanner = actions.str.contains(SCANNER_PATTERN)` |
| 조건에 맞는 행만 | `scanner_rows = web_failures[is_scanner]` |
| 이름별 개수 | `scan_counts = scanner_rows["ip"].value_counts()` |
| 문자열 연결 | `reason = "스캐너 경로를 " + str(request_count) + "번 요청"` |

---
