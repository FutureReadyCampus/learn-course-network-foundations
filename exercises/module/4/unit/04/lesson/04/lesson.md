---
id: m4-u04-l04
title: 제공 파일
render: markdown
---

# 제공 파일

## `saas_detection.py` 만들기

TODO(assemble): `saas_detection.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

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
    times = pd.to_datetime(logins["time"])            # 문자열 시각을 시각 값으로 바꾼다 — 미리 채운 줄
    hours = times.dt.hour                             # 시각 값에서 시(0~23)만 꺼낸다 — 미리 채운 줄

    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. hours 가 BUSINESS_START 이상 BUSINESS_END 이하인지 between 으로 구해 is_business_hour 에 담는다
    is_business_hour = hours.between(BUSINESS_START, BUSINESS_END)  # 시가 업무 시간 안인지 구해 True 또는 False 를 만든다
    # 2. is_business_hour 의 반대를 ~ 로 구해 is_off_hours 에 담는다
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
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. usual_ip 가 None 이 아닌지 구해 has_usual_ip 에 담는다 (None 인지는 is None, 아닌지는 is not None)
        has_usual_ip = usual_ip is not None           # 평소 IP 기록이 있는지 구한다
        # 4. ip 가 usual_ip 와 다른지 != 로 구해 is_new_ip 에 담는다 (같은지는 ==, 다른지는 !=)
        is_new_ip = ip != usual_ip                    # 이번 IP 가 평소 IP 와 다른지 구한다
        if has_usual_ip and is_new_ip:                # 평소 IP 기록이 있고, 이번 IP 가 평소와 다르면
            # 5. new_ip_users 에 user 를 추가한다
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

## `malicious_detection.py` 만들기

TODO(assemble): `malicious_detection.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

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
    actions = web_failures["action"]                  # action 열만 꺼낸다
    # 2. actions 에 .str.contains(SCANNER_PATTERN) 을 붙여 스캐너 경로가 들어 있는지 구해 is_scanner 에 담는다
    is_scanner = actions.str.contains(SCANNER_PATTERN)  # 각 행에 스캐너 경로가 들어 있는지 구해 True 또는 False 를 만든다
    # 3. web_failures 에서 is_scanner 가 True 인 행만 골라 scanner_rows 에 담는다
    scanner_rows = web_failures[is_scanner]           # True 인 행만 골라 새 표로 만든다
    # 4. scanner_rows 의 "ip" 열에 .value_counts() 를 붙여 IP 별로 몇 번 요청했는지 세어 scan_counts 에 담는다
    scan_counts = scanner_rows["ip"].value_counts()   # IP 별로 스캐너 경로를 몇 번 요청했는지 센다
    scan_ips = list(scan_counts.index)                # 스캔으로 보는 IP 이름만 리스트로 만든다
    return scan_ips, scan_counts                      # 스캔 IP 리스트와 IP 별 요청 횟수를 리턴한다


def explain_scan(ip, request_count):                  # IP 와 스캐너 경로 요청 횟수를 받는 함수
    """스캔으로 본 IP 하나를 담당자가 읽을 설명 딕셔너리로 만든다.
    왜 의심했는지 이유를 알림에 남길 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. "스캐너 경로를 " 와 str(request_count) 와 "번 요청" 을 + 로 연결해 reason 에 담는다 (문구는 복사해 붙여도 된다)
    reason = "스캐너 경로를 " + str(request_count) + "번 요청"  # 문자열을 연결해 이유 문장을 만든다
    # 6. 키 "ip" 에 ip, 키 "reason" 에 reason 을 담은 딕셔너리를 scan_info 에 담는다
    scan_info = {"ip": ip, "reason": reason}          # IP 와 이유를 딕셔너리로 만든다
    return scan_info                                  # 설명 딕셔너리를 리턴한다
```

## `correlation.py` 만들기

TODO(assemble): `correlation.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

```python
import pandas as pd                                    # 판다스를 pd 라는 짧은 이름으로 불러온다
from access_detection import load_events, pick_server_failures, EVENTS_PATH  # 실습 3-2 함수를 불러온다
from saas_detection import pick_saas, pick_logins      # 도전 3-2 함수를 불러온다
from malicious_detection import pick_web_failures      # 도전 3-3 함수를 불러온다

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
    web_part = known_web.copy()                        # 원본을 바꾸지 않도록 복사한다 — 미리 채운 줄

    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. web_part 의 "ip" 열을 꺼내 .map(ip_user) 를 붙여 IP 마다 사용자를 구해 users 에 담는다
    web_part["user"] = users                           # 표에 user 열을 붙인다 — 미리 채운 줄
    return web_part                                    # user 열이 붙은 웹 이벤트 표를 리턴한다


def build_timeline(server_part, saas_part, web_part):  # 세 로그의 표를 받는 함수
    """세 로그의 표를 하나로 합쳐 사용자 · 시각 순으로 정렬하고, 하루 중 몇 분인지 열을 붙인다.
    사용자마다 서로 다른 로그의 이벤트를 시간순으로 놓고 볼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. pd.concat 에 [server_part, saas_part, web_part] 리스트를 전달해 timeline 에 담는다
    # 3. timeline 에 .sort_values 를 붙이고 ["user", "time"] 리스트를 전달해 사용자 순, 같은 사용자는 시각 순으로 정렬한 결과를 timeline 에 담는다
    times = pd.to_datetime(timeline["time"])           # 문자열 시각을 시각 값으로 바꾼다
    hours = times.dt.hour                              # 시각 값에서 시(0~23)만 꺼낸다
    minutes = times.dt.minute                          # 시각 값에서 분(0~59)만 꺼낸다
    timeline["minute_of_day"] = hours * 60 + minutes   # 자정부터 몇 분이 지났는지 열을 붙인다 — 미리 채운 줄
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
        if has_many_sources and is_close:              # 로그 종류도 충분하고 60분 이내이면 — 미리 채운 줄
            # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
            # 4. "서로 다른 로그 " 와 str(source_count) 와 "종류 · " 와 str(span) 과 "분 안" 을 + 로 연결해 reason 에 담는다
            # 5. chains 에 키 "user" 에 user, 키 "reason" 에 reason 을 담은 딕셔너리를 추가한다
        if has_many_sources and not is_close:          # 로그 종류는 여럿인데 시간 차가 60분을 초과하면 — 미리 채운 줄
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
