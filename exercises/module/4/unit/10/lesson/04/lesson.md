---
id: m4-u10-l04
title: 실습 10-3 · 상황 8개의 원인과 해결 정리하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/114_day06_am_ai_summary_pipeline.md
  mission_id: GichanSource.m4-1109-am-ai-summary-pipeline
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 10-3 · 상황 8개의 원인과 해결 정리하기

## 목표: 상황별 원인과 해결 정리

> **이번 실습은 새로 배우는 것이 없습니다.** Module 4에서 만든 파일과 함수를 **상황별로 되짚으면서**, 각 상황의 원인과 고치는 방법을 내 말로 정리합니다. 정리한 글이 Module 4의 총정리가 되고, 보고서의 실습 10-3 칸에 씁니다.

## 상황을 풀 때 쓰는 틀

상황이 생기면 같은 네 단계로 생각합니다.

- **확인**: 로그나 평가 결과로 무슨 일인지 알아봅니다.
- **원인**: 왜 이런 일이 생겼는지 가립니다. 원인은 보통 셋 중 하나입니다.
  - 데이터 문제: 파일에 있어야 할 것이 없거나, 빠졌거나, 깨져 있습니다. 예를 들어 읽지 못한 로그 줄, 사용자 이름이 없는 로그, 합치지 않은 알림 파일이 있습니다.
  - 규칙 문제: 「무엇을 의심할지」 정해 둔 기준이 비어 있거나 현실과 맞지 않습니다(너무 느슨하거나 너무 엄격합니다). 이 과정에서 기준을 적어 둔 곳은 다섯 군데입니다.
    - `SUSPICIOUS_STATUS`: 의심으로 보는 상태 코드
    - `REPEAT_LIMIT`: 서버 거절을 몇 번부터 확인할지
    - `WINDOW_MINUTES`: 몇 분 안의 이벤트를 한 사건으로 볼지
    - `WEIGHTS`: 규칙마다 점수
    - `TRUSTED_IPS`: 예외로 믿는 IP
  - 운영 설정 문제: 서버를 켜고 접속을 허용하는 설정(`compose.yaml`)이 목적과 맞지 않습니다.
- **고치기**: 어느 파일을 열어서 어떻게 고칠지 정합니다. 방법은 셋 중 하나입니다.

| 방법 | 뜻 | Module 4에서 한 예 |
|---|---|---|
| 새로 넣는다(추가) | 없던 것을 파일에 적어 넣음 | `TRUSTED_IPS` 리스트에 `203.0.113.80` 을 넣음. `pd.concat` 으로 로그인 알림을 알림 표에 합침 |
| 값을 바꾼다(수정) | 있는 값이나 조건을 다른 것으로 고침 | 포트 `"8081:80"` 을 `"127.0.0.1:8081:80"` 으로 바꿈 |
| 지운다(삭제) | 있던 것을 뺌 | 믿는 IP 에서 온 `SaaS 평소와 다른 IP` 알림을 알림 표에서 뺌 |

- **다시 확인**: 고친 뒤에 무엇을 다시 실행하거나 어떤 출력을 보면 고쳐진 것을 알 수 있는지 정합니다.
- 알림에는 두 가지 틀린 모양이 있습니다. <mark>**오탐**은 문제가 아닌데 난 알림, **미탐**은 진짜 문제인데 나지 않은 알림</mark>입니다. 상황마다 둘 중 어느 쪽인지도 함께 생각합니다.

## 3.1 상황 8개와 읽을 핵심 코드

> 이번 실습은 코드를 실행하지 않고 읽고 글로 씁니다. 표의 파일은 Module 4에서 만든 것이고, 상황의 값은 11/2 의 샘플 데이터에서 가져온 것입니다. 앞에서 만든 파일이 없으면 문서의 코드 조각만 읽고 답합니다.

| # | 상황 (이렇게 알게 됐습니다) | 읽을 핵심 코드 |
|---|---|---|
| 1 | 198.51.100.90 이 `/.env` · `/wp-login.php` · `/phpmyadmin` 을 1초 간격으로 요청했는데, 분류 결과가 세 줄 모두 「오류」이고 「의심」 목록에는 없다 | `log_classify.py` 의 `is_suspicious` · `is_error` |
| 2 | 웹 서버 로그 파일은 30줄인데 `normalized_events.json` 의 웹 서버 이벤트(`source` 가 `web`)는 28개이다. 담당자가 「로그 2줄이 사라졌다」고 보고했다 | `normalize_web` 의 깨진 줄 검사 |
| 3 | 웹 서버 로그의 실패 요청 13개 중 어느 사용자의 요청인지 알 수 있는 것은 1개뿐이다. 203.0.113.50 의 로그인 실패 5번은 누구의 일인지 모른다 | `correlation.py` 의 `make_ip_user_map` · `attach_user_to_web` |
| 4 | seoyeon 은 SaaS 로그와 서버 로그에 모두 나오는데 연결된 사건에 없고, gaeun 은 연결됐다 | `correlation.py` 의 `find_chains` |
| 5 | 알림 7개 중 4개가 오탐인데, 그중 2개는 협력사 사무실 IP 203.0.113.80 에서 온 접속이다 **(예시)** | `tuning.py` 의 `apply_exception` |
| 6 | 로그인 5번 실패 뒤 성공한 203.0.113.50 의 일(P4)이 평가에서 놓친 문제로 나온다. 로그인 규칙은 알림을 이미 냈다 **(예시)** | `final_check.py` 의 `merge_alerts`, `login_alerts.json` |
| 7 | seoyeon 이 권한 없는 정산 조회를 시도했는데(P5) 알림이 나지 않는다 | `access_detection.py` 의 `pick_suspicious`, `REPEAT_LIMIT` |
| 8 | 컴포즈로 켠 `web2` 에 같은 사무실 네트워크의 다른 PC 에서도 접속할 수 있다. 서버를 지우면 서버 안의 접속 기록도 사라진다 | `compose.yaml` · `compose.secure.yaml` 의 `ports` · `volumes` |

- 파일들은 서로의 함수를 호출합니다. 상황 3 · 4는 같은 이벤트 표에서 이어지고, 상황 5 · 6 · 7은 평가 결과에서 이어집니다.
  - 상황 3 → 4: 웹 로그의 요청에 사용자를 붙이는 `attach_user_to_web` 의 결과가 `build_timeline` 을 거쳐 `find_chains` 로 들어갑니다.
  - 상황 5 → 6 → 7: 알림을 센 결과(오탐 · 미탐)가 예외 규칙(`apply_exception`), 알림 합치기(`merge_alerts`), 새 규칙이 필요한 미탐으로 이어집니다.

아래는 상황마다 관련된 코드입니다. 각 코드 앞의 문장은 **이 코드를 왜 읽는지**를 알려 줍니다. 답을 알려 주는 것은 아니고, 코드에서 어디를 볼지만 짚어 줍니다. 읽고 나서 보고서의 실습 10-3 상황 정리를 쓸 때 참고합니다.

#### 상황 1 · 설정 파일 주소를 연달아 요청했는데 「의심」이 아니라 「오류」로 분류됨

요청 하나를 「의심」으로 보는 조건이 무엇인지 읽습니다. 아래 세 줄은 11/2 에 분류한 결과 가운데 「오류」로 나온 요청입니다.

```
198.51.100.90 GET /.env 404
198.51.100.90 GET /wp-login.php 404
198.51.100.90 GET /phpmyadmin 404
```

`log_classify.py` 의 `is_suspicious` 와 `is_error` 입니다. 의심 조건이 상태 코드와 `/admin` 만 보는지 읽습니다.

```python
SUSPICIOUS_STATUS = (401, 403)                         # 의심으로 보는 상태 코드(로그인 실패 · 접근 거부)


def is_suspicious(entry):                              # 읽은 요청 딕셔너리를 받는 함수
    bad_status = entry["status"] in SUSPICIOUS_STATUS  # 상태 코드가 401 이나 403 인지
    admin_path = "/admin" in entry["path"]             # 경로에 /admin 이 들어 있는지
    return bad_status or admin_path                    # 둘 중 하나라도 참이면 True 를 리턴한다


def is_error(entry):                                   # 읽은 요청 딕셔너리를 받는 함수
    return entry["status"] >= 400                      # 400 이상이면 True 를 리턴한다
```

#### 상황 2 · 로그 30줄이 이벤트 28개가 됨

줄 수를 비교한 표입니다. 같은 샘플 로그를 정규화하기 전과 후의 숫자입니다.

| 단계 | 개수 |
|---|---|
| 정규화 전: 웹 서버 로그 파일의 줄 | 30 |
| 정규화 후: `source` 가 `web` 인 이벤트 | 28 |

`normalize_web` 의 앞부분입니다. 줄을 읽기 전에 무엇을 검사하는지 읽습니다.

```python
def normalize_web(line):  # 로그 한 줄을 받는 함수
    if line.count('"') < 2:                                  # 큰따옴표가 두 개보다 적은 깨진 줄이면
        return None       # 읽지 않고 None 을 리턴한다
```

#### 상황 3 · 웹 서버 로그에서 사용자를 알 수 있는 요청이 1개뿐

웹 서버 로그의 이벤트 한 개입니다. `user` 값이 어떤지 읽습니다.

```
{'time': '2026-11-02 09:12:09', 'source': 'web', 'user': None, 'ip': '203.0.113.50', 'action': 'POST /login', 'result': '실패'}
```

`correlation.py` 의 `make_ip_user_map` 입니다. 사용자를 어디에서 알아내는지 읽습니다.

```python
def make_ip_user_map(logins):                     # SaaS 로그인 표를 받는 함수
    ip_user = {}                                  # IP → 사용자 딕셔너리
    login_list = logins.to_dict("records")        # 표를 이벤트 딕셔너리 리스트로 바꾼다
    for login in login_list:                      # 로그인을 하나씩 꺼낸다
        if login["result"] == "성공":             # 성공한 로그인이면
            ip_user[login["ip"]] = login["user"]  # 그 IP 의 사용자를 딕셔너리에 담는다
    return ip_user                                # IP → 사용자 딕셔너리를 리턴한다
```

Unit 6에서 이 함수로 만든 딕셔너리에는 IP 가 다섯 개 있었고, 203.0.113.50 은 그 안에 없었습니다.

#### 상황 4 · 두 로그에 나오는 seoyeon 이 연결되지 않음

`find_chains` 의 두 조건입니다. 「처음부터 마지막까지」가 어느 범위인지 읽습니다.

```python
MIN_SOURCES = 2                            # 서로 다른 로그 종류가 이 개수 이상이어야 연결한다
WINDOW_MINUTES = 60                        # 한 사용자의 이벤트가 이 분 안에 모여 있어야 연결한다

# find_chains 안에서 사용자마다
latest = grouped["minute_of_day"].max()    # 그 사용자의 가장 늦은 시각(분)
earliest = grouped["minute_of_day"].min()  # 그 사용자의 가장 이른 시각(분)
spans = latest - earliest                  # 처음부터 마지막까지 몇 분인지
is_close = span <= WINDOW_MINUTES          # 시간 간격이 기준 이내인지
```

seoyeon 의 이벤트를 시각순으로 놓은 표입니다. Unit 7에서 단계 4 로 나온 결과는 `{'user': 'seoyeon', 'source_count': 2, 'span_minutes': 555}` 이고, gaeun 은 `서로 다른 로그 3종류 · 41분 안` 으로 연결됐습니다.

| 시각 | 로그 | 행동 | 결과 |
|---|---|---|---|
| 09:05:30 | saas | login | 성공 |
| 11:25:40 | saas | file.download | 성공 |
| 11:40:00 | server | SETTLE:QUERY | 실패 |
| 17:38:10 | saas | login | 성공 |
| 17:40:02 ~ 17:42:20 | saas | file.download 5번 | 성공 |
| 18:20:00 | server | SALES:CHANGE | 실패 |

#### 상황 5 · 협력사 사무실에서 접속한 정상 접속에 알림이 남 (예시)

Unit 8의 알림 가운데 `SaaS 평소와 다른 IP` 규칙에서 난 세 건입니다. 조사 메모를 읽습니다.

| id | 규칙 | 대상 | IP | 진짜 문제? | 조사 메모 |
|---|---|---|---|---|---|
| A4 | SaaS 평소와 다른 IP | jiwoo | 203.0.113.80 | 아니오 | 출장 중 협력사 사무실에서 접속함 |
| A5 | SaaS 평소와 다른 IP | seoyeon | 203.0.113.80 | 아니오 | 외근 중 협력사 사무실에서 접속함 |
| A6 | SaaS 대량 다운로드 | seoyeon | 203.0.113.80 | 예 | 업무와 상관없는 파일 6개를 한꺼번에 내려받음 |

`tuning.py` 의 `apply_exception` 입니다. 어떤 조건의 알림만 빼는지 읽습니다.

```python
IP_RULE = "SaaS 평소와 다른 IP"                  # 예외를 적용할 규칙 이름
TRUSTED_IPS = ["203.0.113.80"]                   # 믿는 IP 리스트 : 협력사 사무실 IP 한 개


def apply_exception(alerts):                     # 알림 표를 받는 함수
    is_ip_rule = alerts["rule"] == IP_RULE       # 규칙이 IP 규칙인지
    is_trusted = alerts["ip"].isin(TRUSTED_IPS)  # IP 가 믿는 IP 안에 있는지
    is_removed = is_ip_rule & is_trusted         # 둘 다 참인 행을 뺄 알림으로 본다
    removed_alerts = alerts[is_removed]          # 빼낼 알림
    is_kept = ~is_removed                        # 빼지 않을 알림
    kept_alerts = alerts[is_kept]                # 남은 알림
    return removed_alerts, kept_alerts           # 빼낸 알림과 남은 알림을 리턴한다
```

#### 상황 6 · 로그인 규칙이 낸 알림이 평가에서 빠짐 (예시)

Unit 8의 실습 8-1의 마지막 단계입니다. 알림 7개로 센 결과입니다.

```
--- 단계 4: 미탐 (알림이 나지 않은 진짜 문제) ---
미탐 수: 2
놓친 문제: P4 203.0.113.50 로그인 5번 실패 뒤 성공하고 관리자 화면을 요청함
놓친 문제: P5 seoyeon 권한 없는 정산 조회를 시도함
```

로그인 규칙(`LOGIN_LIMIT = 5`)이 만든 알림 `login_alerts.json` 입니다. 이 알림이 어느 문제를 가리키는지 읽습니다.

```
[
  {"id": "A8", "rule": "웹 로그인 반복 실패", "user": null, "ip": "203.0.113.50", "real": true, "problem": "P4", "memo": "로그인 5번 실패 뒤 성공, 이어서 관리자 화면을 요청함"}
]
```

`final_check.py` 의 `merge_alerts` 입니다. 두 알림 표를 어떻게 다루는지 읽습니다.

```python
def merge_alerts(alerts, login_alerts):             # 알림 표 두 개를 받는 함수
    all_alerts = pd.concat([alerts, login_alerts])  # 두 알림 표를 위아래로 이어 붙인다
    return all_alerts                               # 합친 알림 표를 리턴한다
```

#### 상황 7 · 정산 조회 시도에는 알림이 나지 않음

`access_detection.py` 의 `pick_suspicious` 입니다. 서버 거절이 몇 번이어야 먼저 확인할 대상이 되는지 읽습니다.

```python
REPEAT_LIMIT = 3                           # 한 사용자의 실패가 이 횟수 이상이면 먼저 확인한다


def pick_suspicious(server_failures):      # 서버 실패 표를 받는 함수
    users = server_failures["user"]        # user 열만 꺼낸다
    user_counts = users.value_counts()     # 사용자마다 실패가 몇 번인지 센다
    is_many = user_counts >= REPEAT_LIMIT  # 실패 횟수가 REPEAT_LIMIT 이상인지 비교한다
```

서버 로그에서 seoyeon 의 요청 가운데 실패한 두 건입니다. 진짜 문제 P5 는 `권한 없는 정산 조회를 시도함` 입니다.

| 시각 | 행동 | 결과 |
|---|---|---|
| 11:40:00 | SETTLE:QUERY | 실패 |
| 18:20:00 | SALES:CHANGE | 실패 |

#### 상황 8 · 서버가 같은 네트워크에 열려 있고, 지우면 접속 기록도 사라짐

Unit 9의 실습 9-1에서 쓴 `compose.yaml` 로 켠 `web2` 의 상태입니다. PORTS 에 `0.0.0.0` 이 보입니다.

```
anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2   Up   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp
```

`compose.secure.yaml` 의 `web2` 와 `web3` 입니다. 접속 범위를 정하는 `ports` 와 기록을 내 폴더에 연결하는 `volumes` 를 읽습니다. Unit 9의 실습 9-1에서 쓴 `compose.yaml` 의 `web2` 는 `"8081:80"` 으로 적혀 있었습니다.

```yaml
  web2:                          # 관리용 서버
    image: nginx:1.28            # 같은 nginx 웹 서버
    ports:                       # 접속 범위를 정하는 곳
      - "127.0.0.1:8081:80"      # 맨 앞의 127.0.0.1 은 「내 PC 에서만」이라는 뜻이다
  web3:                          # 로그 서버
    image: nginx:1.28            # 같은 nginx 웹 서버
    ports:                       # 접속 범위를 정하는 곳
      - "127.0.0.1:8082:80"      # web2 와 같이 내 PC 에서만 접속한다
    volumes:                     # 내 폴더와 서버 안 폴더를 연결하는 곳
      - ./logs:/var/log/nginx    # 서버가 로그를 쓰는 폴더를 내 logs 폴더에 연결한다
```

Unit 9에서 `logs/access.log` 에 남은 한 줄의 모양입니다. Unit 9에서 이 폴더를 만들었다면 `cat logs/access.log` 로 내 파일의 줄과 비교해 읽습니다.

```
172.18.0.1 - - [06/Nov/2026:03:37:43 +0000] "GET /.env HTTP/1.1" 404 153 "-" "curl/8.7.1" "-"
```

## 실습 10-3 · 상황 8개의 원인과 해결 정리하기

**이런 상황이 있습니다**

- **지금은**: Module 4에서 파일과 함수를 하나씩 만들었지만, 상황이 생겼을 때 「무엇이 문제이고 어디를 어떻게 고치는지」를 한 번에 말하기는 어렵습니다.
- **그래서 하는 것**: 상황 8개마다 원인, 고칠 파일, 어떻게 고치는지, 고친 뒤 확인, 담당자가 가장 먼저 할 일을 내 말로 정리합니다.
  - 상황 5 · 6 은 예시가 있습니다. 먼저 읽고, 나머지 여섯 개(1 · 2 · 3 · 4 · 7 · 8) 중에서 내가 약하다고 느끼는 것부터 **4개 이상** 씁니다. 다 쓰고 싶으면 다 써도 됩니다.
  - 분량은 정하지 않습니다. 짧게 써도 되고, 더 공부하고 싶으면 깊게 써도 됩니다.
- **끝나면**: 보고서의 실습 10-3 상황 정리가 Module 4 총정리가 됩니다.
- **현업에서는**: 인수인계 문서는 「이런 일이 생기면 여기를 이렇게 고친다」를 상황별로 적어 둡니다. 마지막 칸에 적은 「담당자가 가장 먼저 할 일」은 다음 Unit의 Module 5에서 자동 대응을 만들 때 대응 목록의 출발점이 됩니다.

**할 일**

1. `report_u10.md` 의 `## 실습 10-3` 아래 「상황 정리」 틀을 엽니다. 상황 5 · 6 은 예시라 이미 적혀 있습니다.
2. 상황 1 · 2 · 3 · 4 · 7 · 8 중 4개 이상을 골라 `-` 뒤를 채웁니다. Module 4에서 만든 내 파일을 열어 보면서 써도 됩니다.

- 칸마다 무엇을 쓰는지
  - **원인**: 데이터 문제인지, 규칙 문제인지, 운영 설정 문제인지 고르고 이유를 씁니다.
  - **고칠 파일**: 어느 파일을 열어서 고치는지 씁니다.
  - **어떻게 고치나요**: 새로 넣는지, 값을 바꾸는지, 지우는지 고르고, 정확히 무엇을 넣거나 바꾸거나 지우는지 씁니다.
  - **고친 뒤 확인**: 무엇을 다시 실행하거나 어떤 출력을 보면 고쳐진 것을 알 수 있는지 씁니다.
  - **담당자가 가장 먼저 할 일(선택)**: 이 상황의 알림이 났을 때 사람이 가장 먼저 확인하거나 하는 일 한 가지를 씁니다.
- 상황 하나에서 답이 여러 개일 수 있습니다(예: 상황 8은 접속 범위와 접속 기록 두 가지입니다). 떠오르는 대로 모두 씁니다. 같은 칸에 케이스 A · B 를 쓸 때는 줄을 나눠 「케이스 A: …」 처럼 적습니다.

**순서**

1. **[VS Code]** `report_u10.md` 의 `## 실습 10-3` 아래 「상황 정리」 를 엽니다. 예시(상황 5 · 6)를 먼저 읽습니다.
2. **[VS Code]** 3.1 의 상황 표와 코드를 보면서 상황 1 · 2 · 3 · 4 · 7 · 8 중 4개 이상의 `-` 뒤를 채웁니다. 막히면 Module 4에서 만든 내 파일을 열어서 읽습니다.
3. **[보고서]** `report_u10.md` 의 `## 실습 10-3` 아래의 질문을 채웁니다.
   - (가) 내가 쓴 상황 번호를 적어 주세요. 쓰지 못한 상황이 있으면 막힌 곳도 적어 주세요.
   - (나) [핵심 질문] 상황 8개를 「데이터 문제」 · 「규칙 문제」 · 「운영 설정 문제」로 나누면 각각 어떤 상황인가요? 어느 쪽에서 실수하면 더 위험한지 이유와 함께 적어 주세요.
   - (다) [핵심 질문] Module 4에서 가장 헷갈렸던 로직 하나와, 어떻게 이해했는지 적어 주세요.

## 실습 10-3 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 상황이 생기면 | 확인 → 원인 → 고치기(추가 · 수정 · 삭제) → 다시 확인 |
| 원인 | 데이터 문제 · 규칙 문제 · 운영 설정 문제 |
| 틀린 알림 | 오탐(문제가 아닌데 난 알림) · 미탐(진짜 문제인데 나지 않은 알림) |
| 데이터를 고치는 곳 | 로그 줄 · `normalized_events.json` · 알림 파일(`review_alerts.json` · `login_alerts.json`) |
| 규칙을 고치는 곳 | `SUSPICIOUS_STATUS` · `REPEAT_LIMIT` · `WINDOW_MINUTES` · `WEIGHTS` · `TRUSTED_IPS` |
| 운영 설정을 고치는 곳 | `compose.yaml` 의 `ports` · `volumes` |

---

## 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기

<mark>Module 4 작업을 저장소에 올리는 마무리입니다.</mark> 실습 10-3 마지막 약 10분에 합니다. 어느 터미널을 써도 되고, `pwd` 로 위치를 먼저 확인한 뒤 결과가 `anomaly_detection` 으로 끝나면 아래 1번의 `cd ..` 를 칩니다.

**이런 상황이 있습니다**

- **지금은**: <mark>팀장이 「Module 4에서 만든 파일과 보고서 파일을 저장소에 남겨 달라」고 합니다</mark>.
- **그래서 하는 것**: `git status` 로 올라갈 파일을 확인한 뒤(`.env` 같은 비밀 키 파일이 섞이면 안 됩니다) `git add` → `git commit` → `git push` 순서로 올립니다.
- **끝나면**: 깃허브 저장소의 `anomaly_detection` 폴더에 Unit 10에서 만든 `event_summary.py` · `pipeline.py` · `anomaly_detection_report_2026-11-02.json` 이 보입니다.

**순서**

0. **[터미널]** Unit 10에서 만든 파일이 있는지 `anomaly_detection` 폴더에서 확인합니다. 두 명령을 하나씩 칩니다. `report_u10.md` 의 실습 10-1 · 10-2 · 10-3 칸에서 `답:` 뒤와 코드 상자가 비어 있는 질문이 없는지도 봅니다(마무리 (가)는 3번에서 채웁니다).

   ① 지금 위치를 확인합니다.

   ```bash
   pwd
   ```

   - 하는 일: 지금 있는 폴더의 위치를 보여 줍니다.
   - 나오는 것: <mark>`anomaly_detection` 으로 끝나야</mark> 합니다.

   ② 폴더 안의 파일을 봅니다.

   ```bash
   ls
   ```

   - 하는 일: 폴더 안의 파일 이름을 보여 줍니다.
   - 나오는 것: `event_summary.py` · `pipeline.py` · `anomaly_detection_report_2026-11-02.json` 이 보이면 됩니다.

1. **[터미널]** `security-agent-toolkit` 폴더로 옮깁니다. 0번의 `pwd` 결과가 `anomaly_detection` 으로 끝날 때만 `cd ..` 를 칩니다. 이미 `…/security-agent-toolkit` 으로 끝나면 `cd ..` 는 건너뛰고 `pwd` 만 칩니다.

   ① 한 단계 위 폴더로 이동합니다.

   ```bash
   cd ..
   ```

   - 하는 일: 한 단계 위 폴더로 이동합니다.
   - 나오는 것: 아무것도 나오지 않습니다.

   ② 지금 위치를 확인합니다.

   ```bash
   pwd
   ```

   - 하는 일: 지금 있는 폴더의 위치를 보여 줍니다.
   - 나오는 것: <mark>`…/security-agent-toolkit` 으로 끝나면</mark> 됩니다. 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.

2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark>빨간 글씨 줄에 `.env` 나 `.venv` 가 보이면 올리지 말고,</mark> 아래 안내대로 `.gitignore` 를 고친 뒤 `git status` 를 다시 봅니다.

   ① 올릴 파일의 상태를 봅니다.

   ```bash
   git status
   ```

   - 하는 일: 올릴 파일의 상태를 보여 줍니다.
   - 나오는 것: 바뀐 파일의 이름이 나옵니다.

   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `anomaly_detection/__pycache__/` (파이썬이 실행하면서 자동으로 만드는 임시 폴더)가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 봅니다.
   - `anomaly_detection/llm_client.py` 는 API 키가 들어 있지 않은 코드 파일이라 올라가도 됩니다. 키는 `.env` 에만 있습니다.

3. **[보고서]** `report_u10.md` 의 `## 마무리` 아래를 채웁니다. <mark>올리기 전에 채워야</mark> 깃허브에 빈칸 없이 올라갑니다.
   - (가) `git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.
   - <mark>실습 10-1 · 10-2 · 10-3에서 못 적은 보고서 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.</mark> 올린 뒤에 이어서 적어 다시 올려도 됩니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`). 세 명령을 순서대로 하나씩 칩니다.

   ① 바뀐 파일을 모두 담습니다.

   ```bash
   git add .
   ```

   - 하는 일: 바뀐 파일을 올릴 대상에 담습니다.
   - 나오는 것: 아무것도 나오지 않습니다.

   ② 기록으로 저장합니다.

   ```bash
   git commit -m "Add Gemini API summary and pipeline for anomaly detection"
   ```

   - 하는 일: 따옴표 안의 설명을 붙여 기록으로 저장합니다.
   - 나오는 것: 바뀐 파일 수가 적힌 줄이 나옵니다.

   ③ 깃허브로 올립니다.

   ```bash
   git push
   ```

   - 하는 일: 저장한 기록을 깃허브로 올립니다.
   - 나오는 것: 올라간 내용이 몇 줄 나옵니다.

   - <mark>`git push` 가 거절(`rejected`)되면 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다.</mark> `git pull` 을 입력해 받아 온 뒤 `git push` 를 다시 합니다.
   - `git pull` 뒤에 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다.

5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `anomaly_detection` 폴더를 열고, VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 있는 파일들이 깃허브에도 보이는지 확인합니다. <mark>`__pycache__` 폴더는 없어도 됩니다</mark>.
   - 빠진 이름이 있으면 VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 내 PC 에도 있는지 봅니다.
     - 없으면 다른 폴더에 만든 것이니 `anomaly_detection` 안으로 옮기고, `pwd` 로 위치를 확인한 뒤 2번의 `git status` 부터 다시 합니다.

## 마무리 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 올릴 파일 확인 | `git status` (`.env` · `.venv` 가 보이면 멈춤) |
| 올리기 | `git add .` → `git commit -m "…"` → `git push` |
| 올린 뒤 | 브라우저에서 `anomaly_detection` 폴더와 파일이 있는지 확인 |

---

## 이번 Unit 마무리

| 확인 | 문제 |
|---|---|
| 점수 파일의 사실만 AI 에게 보내 대상 3명의 요약을 받고, 실패하면 대체 문장을 쓰게 했다 | 실습 10-1 |
| 이벤트 읽기부터 연결 · 탐지 · 점수 · Gemini API 를 활용한 AI 요약 · 보고서 저장까지 `pipeline.py` 한 번으로 실행했다 | 실습 10-2 |
| 상황 8개의 원인과 고치는 방법을 내 말로 정리해 보고서에 Module 4 총정리를 썼다 | 실습 10-3 |
| Module 4 작업과 보고서를 깃허브에 올렸다 | 마무리 |

다음 Unit에서는 Module 5(자동 대응)을 시작합니다. <mark>점수 기록에서 등급이 `high` 인 대상을 만났을 때 사람이 하던 일을 프로그램이 대신하는 것이 Module 5의 출발점</mark>입니다. 보고서 실습 10-3 상황 정리의 마지막 칸(담당자가 가장 먼저 할 일)이 그때 참고 자료가 됩니다. Module 5의 첫 실습에서 새 폴더 `soar_response` 를 만듭니다.

---

<!-- learn:answers -->
