---
id: m4-u04-l02
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

**실습 4-1을 시작하기 전에** 이 레슨의 파일 세 개를 만듭니다. 실습 4-1의 `risk_scores.py` 는 SaaS · 웹 로그의 탐지 결과와 로그 연결 결과까지 모아 점수를 매기는데, 그 결과를 만드는 코드는 오늘 직접 쓰지 않고 완성본을 받아 씁니다.

| 만들 파일 | 하는 일 | 어떤 코드인가 |
|---|---|---|
| `saas_detection.py` | SaaS 로그에서 업무 시간 밖 로그인 · 평소와 다른 IP · 대량 다운로드를 찾습니다 | Unit 3 응용 3-2와 같은 코드 |
| `malicious_detection.py` | 웹 로그에서 경로 스캔 IP 를 찾습니다 | Unit 3 응용 3-3과 같은 코드 |
| `correlation.py` | 세 로그를 한 사용자 기준으로 이어 60분 안의 사건을 찾습니다 | 응용 4-1에서 직접 써 보는 코드 |

1. 파일은 모두 `anomaly_detection` 폴더 안에 만듭니다(VS Code 왼쪽 목록에서 `anomaly_detection` 폴더를 오른쪽 클릭 › **New File**).
2. 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다. 같은 이름의 파일이 이미 있으면 내용을 모두 지우고 붙여 넣습니다.
3. 만들 파일은 위 표의 세 개입니다.
   - 앞의 두 파일에는 Unit 3 응용에서만 설명한 문법(`.between` · `.str.contains` · `.dt.hour` 등)이 나옵니다. 오늘은 붙여 넣어 쓰기만 하므로, 응용을 하지 않았다면 줄 끝 주석으로 무슨 일을 하는지만 읽고 넘어가도 됩니다.
4. 시작하기 레슨의 확인에서 `Unit 3 파일 정상 57` 이 나오지 않았다면, 이 레슨 마지막 페이지의 `access_detection.py` 예비 코드도 만듭니다.
5. 다 만들었으면 아래 명령으로 확인하고 실습 4-1로 갑니다(맥북은 `python3`).
   ```bash
   python -c "from saas_detection import find_bulk_download_users; from malicious_detection import find_scan_ips; from correlation import find_chains_in_events; from access_detection import load_events, EVENTS_PATH; print('제공 파일 정상', len(find_chains_in_events(load_events(EVENTS_PATH))))"
   ```
   - 연결된 사건이 1건(gaeun)이면 마지막 숫자가 `1` 입니다.

**확인** — 5번 명령에서 `제공 파일 정상 1` 이 나오면 성공입니다. 안 나오면 오류에 나온 파일 이름(`No module named '…'`)의 페이지로 가서 그 파일을 다시 붙여 넣습니다.

> 시간이 남아 응용 4-1을 하면, `correlation.py` 를 빈칸이 있는 골격으로 바꿔 직접 써 봅니다. 그때는 다 채울 때까지 실습 4-1이 동작하지 않으니, 다 쓴 뒤 `exercise4-1_run.py` 를 다시 실행해 결과가 같은지 확인합니다.

## `saas_detection.py` 만들기

**`saas_detection.py`** 를 만들고 아래 내용을 붙여 넣습니다. SaaS 이벤트에서 세 가지 이상 사용을 찾습니다.

| 함수 | 찾는 것 | 오늘 데이터에서 나오는 것 |
|---|---|---|
| `find_off_hours_logins` | 업무 시간(8시 ~ 20시대) 밖에 시도한 로그인 | jiwoo(02:14) |
| `find_new_ip_users` | 평소 IP(`USUAL_IPS`)와 다른 IP 로 로그인한 사용자 | jiwoo · seoyeon |
| `find_bulk_download_users` | 파일을 5번 이상 내려받은 사용자 | seoyeon |

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다

EVENTS_PATH = "normalized_events.json"                # 읽을 정규화 이벤트 파일 이름
USUAL_IPS = {"seoyeon": "198.51.100.9", "junho": "192.0.2.41", "jiwoo": "198.51.100.52"}  # 사용자별 평소 IP. gaeun 은 평소 기록이 없어 넣지 않았다
BUSINESS_START = 8                                    # 업무 시간이 시작하는 시
BUSINESS_END = 20                                     # 업무 시간이 끝나는 시(20시대, 20:59 까지가 업무 시간)
DOWNLOAD_LIMIT = 5                                    # 파일을 이 횟수 이상 내려받으면 대량 다운로드로 본다


def load_events(path):                                # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                       # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                     # 이벤트 표를 리턴한다


def pick_saas(events):                                # 이벤트 표를 받는 함수
    """SaaS 로그의 이벤트만 골라 새 표로 만든다.
    SaaS 이상 사용을 찾기 전에 쓴다.
    """
    sources = events["source"]                        # source 열만 꺼낸다
    is_saas = sources == "saas"                       # 각 행이 SaaS 이벤트인지 비교해 True 또는 False 를 만든다
    saas = events[is_saas]                            # True 인 행만 골라 새 표로 만든다
    return saas                                       # SaaS 이벤트 표를 리턴한다


def pick_logins(saas):                                # SaaS 이벤트 표를 받는 함수
    """로그인 이벤트만 골라 새 표로 만든다.
    로그인 시각과 IP 를 살펴보기 전에 쓴다.
    """
    actions = saas["action"]                          # action 열만 꺼낸다
    is_login = actions == "login"                     # 각 행이 로그인인지 비교해 True 또는 False 를 만든다
    logins = saas[is_login]                           # True 인 행만 골라 새 표로 만든다
    return logins                                     # 로그인 이벤트 표를 리턴한다


def find_off_hours_logins(logins):                    # 로그인 표를 받는 함수
    """업무 시간 밖에 시도한 로그인만 골라 새 표로 만든다.
    새벽 로그인처럼 평소에 없는 시각을 찾을 때 쓴다.
    """
    times = pd.to_datetime(logins["time"])            # 문자열 시각을 시각 값으로 바꾼다
    hours = times.dt.hour                             # 시각 값에서 시(0~23)만 꺼낸다

    is_business_hour = hours.between(BUSINESS_START, BUSINESS_END)  # 시가 업무 시간 안인지 구해 True 또는 False 를 만든다
    is_off_hours = ~is_business_hour                  # True 와 False 를 뒤집어 업무 시간 밖인 행을 True 로 만든다
    off_hours_logins = logins[is_off_hours]           # True 인 행만 골라 새 표로 만든다
    return off_hours_logins                           # 업무 시간 밖 로그인 표를 리턴한다


def find_new_ip_users(logins):                        # 로그인 표를 받는 함수
    """평소와 다른 IP 로 로그인한 사용자를 골라 리스트로 만든다.
    계정을 다른 사람이 쓰는지 의심할 때 쓴다.
    """
    new_ip_users = []                                 # 사용자를 담을 빈 리스트
    login_list = logins.to_dict("records")            # 표를 이벤트 딕셔너리 리스트로 바꾼다
    for login in login_list:                          # 로그인을 하나씩 꺼낸다
        user = login["user"]                          # 그 로그인의 사용자
        ip = login["ip"]                              # 그 로그인의 IP
        usual_ip = USUAL_IPS.get(user)                # 그 사용자의 평소 IP(기록이 없으면 None)
        has_usual_ip = usual_ip is not None           # 평소 IP 기록이 있는지 구한다
        is_new_ip = ip != usual_ip                    # 이번 IP 가 평소 IP 와 다른지 구한다
        if has_usual_ip and is_new_ip:                # 평소 IP 기록이 있고, 이번 IP 가 평소와 다르면
            new_ip_users.append(user)                 # 리스트에 사용자를 추가한다
    return new_ip_users                               # 평소와 다른 IP 로 로그인한 사용자를 리턴한다


def find_bulk_download_users(saas):                   # SaaS 이벤트 표를 받는 함수
    """파일을 기준 횟수 이상 내려받은 사용자를 리스트로 만든다.
    자료를 한꺼번에 빼 가는 사용자를 찾을 때 쓴다.
    """
    actions = saas["action"]                          # action 열만 꺼낸다
    is_download = actions == "file.download"          # 각 행이 다운로드인지 비교해 True 또는 False 를 만든다
    downloads = saas[is_download]                     # True 인 행만 골라 새 표로 만든다
    counts = downloads.groupby("user").size()         # user 가 같은 행끼리 그룹으로 만들고(groupby) 바로 그룹마다 행이 몇 개인지 센다(size) — 사용자별 다운로드 횟수
    is_bulk = counts >= DOWNLOAD_LIMIT                # 사용자마다 횟수가 기준 이상인지 비교해 True 또는 False 를 만든다
    bulk_counts = counts[is_bulk]                     # 기준 이상인 사용자와 횟수만 남긴다
    bulk_users = list(bulk_counts.index)              # 사용자 이름만 리스트로 만든다
    return bulk_users                                 # 대량 다운로드 사용자를 리턴한다
```

- `~` 는 `True` 와 `False` 를 뒤집는 기호입니다. `~is_business_hour` 는 「업무 시간 안이 아닌」 행을 `True` 로 만듭니다.

**확인** — VS Code 왼쪽 목록의 `anomaly_detection` 아래에 `saas_detection.py` 가 보이면 성공입니다. 실행 확인은 세 파일을 모두 만든 뒤 첫 페이지 5번 명령으로 합니다.

## `malicious_detection.py` 만들기

**`malicious_detection.py`** 를 만들고 아래 내용을 붙여 넣습니다. 웹 서버 로그의 실패 이벤트 가운데 스캐너가 자주 요청하는 경로(`/.env` · `/wp-login` · `/phpmyadmin`)를 요청한 IP 를 찾습니다.

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
    actions = web_failures["action"]                  # action 열만 꺼낸다
    is_scanner = actions.str.contains(SCANNER_PATTERN)  # 각 행에 스캐너 경로가 들어 있는지 구해 True 또는 False 를 만든다
    scanner_rows = web_failures[is_scanner]           # True 인 행만 골라 새 표로 만든다
    scan_counts = scanner_rows["ip"].value_counts()   # IP 별로 스캐너 경로를 몇 번 요청했는지 센다
    scan_ips = list(scan_counts.index)                # 스캔으로 보는 IP 이름만 리스트로 만든다
    return scan_ips, scan_counts                      # 스캔 IP 리스트와 IP 별 요청 횟수를 리턴한다


def explain_scan(ip, request_count):                  # IP 와 스캐너 경로 요청 횟수를 받는 함수
    """스캔으로 본 IP 하나를 담당자가 읽을 설명 딕셔너리로 만든다.
    왜 의심했는지 이유를 알림에 남길 때 쓴다.
    """
    reason = "스캐너 경로를 " + str(request_count) + "번 요청"  # 문자열을 연결해 이유 문장을 만든다
    scan_info = {"ip": ip, "reason": reason}          # IP 와 이유를 딕셔너리로 만든다
    return scan_info                                  # 설명 딕셔너리를 리턴한다
```

- 오늘 데이터에서는 `198.51.100.90` 한 곳이 스캐너 경로를 3번 요청해 경로 스캔으로 나옵니다.
- `explain_scan` 은 오늘 실습에서는 쓰지 않습니다. Unit 3 응용 3-3과 같은 파일을 쓰려고 그대로 두었습니다.

**확인** — VS Code 왼쪽 목록의 `anomaly_detection` 아래에 `malicious_detection.py` 가 보이면 성공입니다. 다른 폴더에 만들어졌으면 `anomaly_detection` 으로 끌어다 옮깁니다.

## `correlation.py` 만들기

**`correlation.py`** 를 만들고 아래 내용을 붙여 넣습니다. 같은 사용자의 이벤트가 서로 다른 로그에 짧은 시간 안에 나타나면 하나의 사건으로 연결합니다. 이렇게 서로 다른 로그를 같은 기준으로 연결해 분석하는 것을 **상관분석**(correlation, 코렐레이션)이라고 합니다.

1. 웹 로그에는 사용자가 없어서, SaaS 의 성공한 로그인에서 「IP → 사용자」를 찾아 웹 이벤트에 사용자를 채웁니다.
2. 서버 · SaaS · 웹 이벤트를 표 하나로 합쳐 사용자 · 시각 순으로 정렬합니다.
3. 서로 다른 로그가 2종류 이상이고, 첫 이벤트부터 마지막 이벤트까지 60분 이내인 사용자만 연결된 사건으로 봅니다.

```python
import pandas as pd                                    # 판다스를 pd 라는 짧은 이름으로 불러온다
from access_detection import load_events, pick_server_failures, EVENTS_PATH  # 실습 3-2 함수를 불러온다
from saas_detection import pick_saas, pick_logins      # saas_detection.py 의 함수를 불러온다
from malicious_detection import pick_web_failures      # malicious_detection.py 의 함수를 불러온다

MIN_SOURCES = 2                                        # 서로 다른 로그(source)가 이 개수 이상이면 연결된 것으로 본다
WINDOW_MINUTES = 60                                    # 한 사용자의 이벤트가 이 분 안에 모여 있어야 연결된 것으로 본다


def make_ip_user_map(logins):                          # SaaS 로그인 표를 받는 함수
    """성공한 SaaS 로그인에서 IP 마다 사용자를 찾아 딕셔너리로 만든다.
    웹 서버 로그에는 사용자가 없어서 IP 로 사용자를 찾을 때 쓴다.
    """
    ip_user = {}                                       # IP → 사용자 딕셔너리
    login_list = logins.to_dict("records")             # 표를 이벤트 딕셔너리 리스트로 바꾼다
    for login in login_list:                           # 로그인을 하나씩 꺼낸다
        if login["result"] == "성공":                  # 성공한 로그인이면
            ip_user[login["ip"]] = login["user"]       # 그 IP 의 사용자를 딕셔너리에 담는다
    return ip_user                                     # IP → 사용자 딕셔너리를 리턴한다


def attach_user_to_web(web_failures, ip_user):         # 웹 실패 표와 IP → 사용자 딕셔너리를 받는 함수
    """IP 로 사용자를 알 수 있는 웹 실패 이벤트에 user 열을 붙인다.
    웹 로그를 서버 · SaaS 로그와 같은 사용자 기준으로 연결해 분석할 때 쓴다.
    """
    ips = web_failures["ip"]                           # ip 열만 꺼낸다
    known_ips = list(ip_user)                          # 딕셔너리의 키(IP)만 리스트로 만든다
    is_known = ips.isin(known_ips)                     # 행마다 사용자를 아는 IP 인지 구해 True 또는 False 를 만든다
    known_web = web_failures[is_known]                 # True 인 행만 골라 새 표를 만든다
    web_part = known_web.copy()                        # 원본을 바꾸지 않도록 복사한다

    users = web_part["ip"].map(ip_user)                # ip 열을 꺼내 바로 IP 마다 사용자를 찾아 채운다(map)
    web_part["user"] = users                           # 표에 user 열을 붙인다
    return web_part                                    # user 열이 붙은 웹 이벤트 표를 리턴한다


def build_timeline(server_part, saas_part, web_part):  # 세 로그의 표를 받는 함수
    """세 로그의 표를 하나로 합쳐 사용자 · 시각 순으로 정렬하고, 하루 중 몇 분인지 열을 붙인다.
    사용자마다 서로 다른 로그의 이벤트를 시간순으로 놓고 볼 때 쓴다.
    """
    timeline = pd.concat([server_part, saas_part, web_part])  # 세 표를 위아래로 연결해 표 하나로 만든다
    timeline = timeline.sort_values(["user", "time"])  # user 순으로, 같은 user 는 time 순으로 정렬한다
    times = pd.to_datetime(timeline["time"])           # 문자열 시각을 시각 값으로 바꾼다
    hours = times.dt.hour                              # 시각 값에서 시(0~23)만 꺼낸다
    minutes = times.dt.minute                          # 시각 값에서 분(0~59)만 꺼낸다
    timeline["minute_of_day"] = hours * 60 + minutes   # 자정부터 몇 분이 지났는지 열을 붙인다
    return timeline                                    # 정렬된 이벤트 표를 리턴한다


def find_chains(timeline):                             # 정렬된 이벤트 표를 받는 함수
    """서로 다른 로그가 짧은 시간 안에 한 사용자에게 모여 있는 사건을 찾는다.
    이벤트 하나씩이 아니라 한 사용자의 사건으로 연결해 분석할 때 쓴다.
    """
    grouped = timeline.groupby("user")                 # user 가 같은 행끼리 그룹으로 만든다
    source_counts = grouped["source"].nunique()        # 그룹마다 서로 다른 로그(source)가 몇 종류인지 센다
    latest = grouped["minute_of_day"].max()            # 그룹마다 가장 늦은 시각(분)을 구한다
    earliest = grouped["minute_of_day"].min()          # 그룹마다 가장 이른 시각(분)을 구한다
    spans = latest - earliest                          # 그룹마다 처음부터 마지막까지 몇 분인지 구한다

    chains = []                                        # 연결된 사건을 담을 빈 리스트
    not_chained = []                                   # 로그 종류는 여럿이지만 시간 차가 60분을 초과해 연결되지 않은 사용자 정보
    for user in source_counts.index:                   # 사용자를 하나씩 꺼낸다
        source_count = source_counts[user]             # 그 사용자의 로그 종류 수
        span = spans[user]                             # 그 사용자의 처음부터 마지막까지 분
        has_many_sources = source_count >= MIN_SOURCES  # 로그 종류가 기준 이상인지 구한다
        is_close = span <= WINDOW_MINUTES              # 시간 간격이 기준 이내인지 구한다
        if has_many_sources and is_close:              # 로그 종류도 충분하고 60분 이내이면
            reason = "서로 다른 로그 " + str(source_count) + "종류 · " + str(span) + "분 안"  # 문자열을 연결해 이유 문장을 만든다
            chains.append({"user": user, "reason": reason})  # 연결된 사건에 사용자와 이유를 추가한다
        if has_many_sources and not is_close:          # 로그 종류는 여럿인데 시간 차가 60분을 초과하면
            not_chained.append({"user": user, "source_count": int(source_count), "span_minutes": int(span)})  # 연결되지 않은 사용자와 두 숫자를 추가한다
    return chains, not_chained                         # 연결된 사건과 연결되지 않은 사용자를 리턴한다


def find_chains_in_events(events):                     # 이벤트 표를 받는 함수
    """이벤트 표 하나로 위 함수를 차례로 불러 연결된 사건 리스트를 만든다.
    실습 4-1에서 점수를 매기기 전에 한 번에 쓴다.
    """
    server_failures = pick_server_failures(events)     # 판정 서버 실패 이벤트를 고른다
    server_part = server_failures                      # 서버 실패 이벤트 전체를 쓴다
    saas_part = pick_saas(events)                      # SaaS 이벤트를 고른다
    logins = pick_logins(saas_part)                    # 로그인 이벤트를 고른다
    ip_user = make_ip_user_map(logins)                 # IP → 사용자 딕셔너리를 만든다
    web_failures = pick_web_failures(events)           # 웹 실패 이벤트를 고른다
    web_part = attach_user_to_web(web_failures, ip_user)  # 사용자를 아는 웹 이벤트에 user 열을 붙인다
    timeline = build_timeline(server_part, saas_part, web_part)  # 세 로그를 합쳐 정렬한다
    chains, not_chained = find_chains(timeline)        # 연결된 사건을 찾는다
    return chains                                      # 연결된 사건 리스트를 리턴한다
```

- 실습 4-1은 마지막 함수 `find_chains_in_events` 하나만 불러 씁니다. 오늘 데이터에서는 gaeun 한 명이 「서로 다른 로그 3종류 · 41분 안」으로 연결됩니다.
- 이 파일은 `access_detection` · `saas_detection` · `malicious_detection` 을 불러 쓰므로 세 파일이 먼저 있어야 합니다.
- 함수마다 무엇을 하는지는 응용 4-1 레슨에서 자세히 다룹니다.

**확인** — 첫 페이지 5번 명령에서 `제공 파일 정상 1` 이 나오면 성공입니다. `No module named 'saas_detection'` 이 나오면 앞 페이지의 파일을 먼저 만듭니다.

## Unit 3 파일이 없을 때 `access_detection.py`

시작하기 레슨의 확인에서 `Unit 3 파일 정상 57` 이 나왔다면 **이 페이지는 건너뜁니다.** Unit 3 실습 3-2에서 직접 만든 파일을 그대로 씁니다.

`No module named 'access_detection'` 이나 `ImportError` 가 나왔다면 **`access_detection.py`** 를 만들고 아래 내용을 붙여 넣습니다. Unit 3 실습 3-2의 완성본입니다. 판정 서버가 거절한 요청 가운데 3번 이상 반복된 사용자를 고르고, Module 3에서 만든 권한 판정 `check_permission` 으로 다시 판정해 이유를 붙입니다.

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다
from rbac import check_permission                     # Module 3(접근통제)에서 만든 권한 판정 함수를 불러온다

EVENTS_PATH = "normalized_events.json"                # 읽을 정규화 이벤트 파일 이름
REPEAT_LIMIT = 3                                      # 한 사용자의 실패가 이 횟수 이상이면 먼저 확인한다
PRIORITY = {"퇴사한 계정": 1, "권한 없음": 2, "허용": 3}  # 판정 이유별로 우선순위(작을수록 먼저)


def load_events(path):                                # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                       # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                     # 이벤트 표를 리턴한다


def pick_server_failures(events):                     # 이벤트 표를 받는 함수
    """판정 서버 로그에서 실패한 이벤트만 골라 새 표로 만든다.
    서버가 거절한 요청을 조사하기 전에 쓴다.
    """
    sources = events["source"]                        # source 열만 꺼낸다
    is_server = sources == "server"                   # 각 행이 판정 서버 이벤트인지 비교해 True 또는 False 를 만든다
    results = events["result"]                        # result 열만 꺼낸다
    is_fail = results == "실패"                       # 각 행이 실패인지 비교해 True 또는 False 를 만든다
    both_true = is_server & is_fail                   # 두 조건이 모두 True 인 행만 True 로 만든다
    server_failures = events[both_true]               # True 인 행만 골라 새 표로 만든다
    return server_failures                            # 서버 실패 이벤트 표를 리턴한다


def pick_suspicious(server_failures):                 # 서버 실패 표를 받는 함수
    """실패가 반복된 사용자의 이벤트만 골라 새 표로 만든다.
    같은 사용자가 여러 번 거절당했는지 볼 때 쓴다.
    """
    users = server_failures["user"]                   # user 열만 꺼낸다
    user_counts = users.value_counts()                # 사용자마다 실패가 몇 번인지 센다
    is_many = user_counts >= REPEAT_LIMIT             # 사용자마다 실패 횟수가 REPEAT_LIMIT 이상인지 비교해 True 또는 False 를 만든다
    repeated_users = user_counts[is_many]             # 반복된 사용자와 횟수만 남긴다

    repeated_names = repeated_users.index             # 반복된 사용자의 이름들(인덱스)을 꺼낸다
    is_repeated_user = users.isin(repeated_names)     # 각 행의 사용자가 반복된 사용자 이름 안에 있는지 구해 True 또는 False 를 만든다
    suspicious = server_failures[is_repeated_user]    # True 인 행만 골라 새 표로 만든다
    return suspicious                                 # 먼저 확인할 실패 이벤트 표를 리턴한다


def judge_failure(user, action):                      # 사용자와 행동을 받는 함수
    """서버가 거절한 요청을 Module 3(접근통제) 권한 규칙으로 다시 판정해 이유와 우선순위를 리턴한다.
    거절이 규칙대로인지 확인할 때 쓴다.
    """
    parts = action.split(":")                         # ":" 로 나눠 두 조각의 리스트로 만든다
    resource = parts[0]                               # 첫 번째 조각이 자원이다
    permission_action = parts[1]                      # 두 번째 조각이 행위이다

    is_allowed, reason = check_permission(user, resource, permission_action)  # Module 3(접근통제) 판정 결과를 허용 여부와 이유로 나눠 받는다
    priority = PRIORITY.get(reason, 4)                # 이유의 우선순위를 꺼낸다(없으면 4)
    return reason, priority                           # 판정 이유와 우선순위를 리턴한다
```

- 이 파일은 `rbac.py` 와 `normalized_events.json` · `config/users.json` · `config/roles.json` 이 있어야 동작합니다. 없으면 Unit 3 시작하기 레슨의 코드 상자로 먼저 만듭니다.

**확인** — 시작하기 레슨의 확인 명령을 다시 쳐서 `Unit 3 파일 정상 57` 이 나오면 성공입니다. `No module named 'rbac'` 이 나오면 Unit 3 시작하기 레슨의 코드 상자로 `rbac.py` 를 먼저 만듭니다.

---
