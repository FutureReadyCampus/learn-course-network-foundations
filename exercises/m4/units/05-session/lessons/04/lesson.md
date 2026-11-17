---
id: m4-u05-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/104_day03_pm_traffic_alerts.md
  mission_id: GichanSource.m4-1104-pm-traffic-alerts
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## Exercise 5-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise5-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise5-1_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 네 함수입니다.

① `add_minute_column` 안

```python
    minutes = times.dt.floor("min")  # 시각에서 초를 버린다 (09:12:03 → 09:12:00)
```

② `count_web_per_minute` 안

```python
    is_web = events["source"] == "web"  # 행마다 웹 서버 이벤트인지 비교해 True 또는 False 를 만든다
    web_events = events[is_web]         # True 인 행만 골라 웹 서버 이벤트의 표를 만든다
```

③ `make_traffic_limit` 안

```python
    limit = average * multiple  # 평소 평균에 3 을 곱한 값이 급증 기준이다
```

④ `pick_spike_minutes` 안

```python
    is_spike = minute_request_counts >= limit        # 분마다 「기준 이상인가?」를 비교해 True 또는 False 를 만든다
    spike_minutes = minute_request_counts[is_spike]  # True 인 분만 남긴다
```

**결과**

- (가) 출력은 다음과 같고, 급증 기준은 <mark>**6.0번 이상**</mark>, 요청이 급증한 분은 <mark>**09:12(요청 9개)**</mark> 한 분입니다.

```
--- 단계 1: time 열과 minute 열의 처음 3개 비교
0    2026-11-02 02:14:08
1    2026-11-02 09:01:05
2    2026-11-02 09:01:06
Name: time, dtype: object
0   2026-11-02 02:14:00
1   2026-11-02 09:01:00
2   2026-11-02 09:01:00
Name: minute, dtype: datetime64[ns]
--- 단계 2: 웹 서버의 분당 요청 수
minute
2026-11-02 09:01:00    2
2026-11-02 09:03:00    2
2026-11-02 09:04:00    1
2026-11-02 09:05:00    2
2026-11-02 09:12:00    9
2026-11-02 09:20:00    3
2026-11-02 09:22:00    1
2026-11-02 09:25:00    1
2026-11-02 09:26:00    1
2026-11-02 09:28:00    2
2026-11-02 09:31:00    1
2026-11-02 09:33:00    1
2026-11-02 09:35:00    1
2026-11-02 09:36:00    1
dtype: int64
--- 단계 3: 급증 기준(평소 평균의 3 배) 6.0 번 이상
--- 단계 4: 요청이 급증한 분
minute
2026-11-02 09:12:00    9
dtype: int64
```

- (나) 09:12 에 들어온 요청 9개는 모두 **203.0.113.50** 이 보낸 것입니다. 이 분의 이벤트는 다음과 같습니다.

| 시각 | 주소 | 행동 | 결과 |
|---|---|---|---|
| 09:12:01 | 203.0.113.50 | `GET /login` | 성공 |
| 09:12:03 | 203.0.113.50 | `POST /login` | 실패 |
| 09:12:06 | 203.0.113.50 | `POST /login` | 실패 |
| 09:12:09 | 203.0.113.50 | `POST /login` | 실패 |
| 09:12:12 | 203.0.113.50 | `POST /login` | 실패 |
| 09:12:15 | 203.0.113.50 | `POST /login` | 실패 |
| 09:12:18 | 203.0.113.50 | `POST /login` | 성공 |
| 09:12:25 | 203.0.113.50 | `GET /admin` | 실패 |
| 09:12:27 | 203.0.113.50 | `GET /admin/users` | 실패 |

  - 로그인 화면을 열고(`GET /login`), 로그인 정보를 6번 보냈고(`POST /login`, 5번 실패 뒤 1번 성공), 관리자 경로를 2번 요청했습니다(`/admin`, `/admin/users`).
  - <mark>이 급증이 공격이라고 확정할 수는 없습니다.</mark> 하지만 <mark>Exercise 4-2에서 로그인 실패 5번으로 알림 대상이 된 주소와 같은 IP 주소입니다.</mark> 한 주소가 1분도 안 되는 사이에 로그인을 반복하다 성공했고, 이어서 관리자 경로까지 요청했습니다. 이것은 먼저 살펴볼 일입니다.
  - 확정하려면 이 주소가 회사 직원의 주소인지, 성공한 계정이 누구인지 <mark>판정 서버 · SaaS 로그와 시각을 맞춰 봐야 합니다.</mark>
- (다) 09:20 의 요청 3개는 <mark>급증 기준(6.0번 이상)보다 적어서 탐지되지 않았습니다.</mark>
  - 그 3개는 모두 198.51.100.90 이 09:20:10 ~ 09:20:12 에 보낸 `GET /.env` · `GET /wp-login.php` · `GET /phpmyadmin` 이고 모두 실패했습니다. 서로 다른 경로를 차례로 요청한 모양입니다.
  - 급증 규칙은 요청의 **수**만 보기 때문에, <mark>수가 적으면 요청의 내용과 상관없이 알리지 못합니다.</mark> 이런 경로 스캔(취약한 경로를 하나씩 찾아보는 시도)은 Unit 6에서 다른 규칙으로 찾습니다.

**왜**

- <mark>「짧은 시간에 늘어난 요청」은 시간을 일정한 구간(여기서는 1분)으로 나눠 구간마다 세어야 보입니다.</mark> 구간 길이를 정하는 일이 초를 버리는 일입니다.

**자주 틀리는 곳**

- `times.dt.floor("min")` 에서 **`.dt` 를 빠뜨리고 `times.floor("min")` 으로 쓰면 오류가 납니다.**
  - 실행하면 다음 오류가 납니다(<mark>`'Series' object has no attribute 'floor'`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise5-1_run.py", line 4, in <module>
    events = add_minute_column(events)  # 시각에서 초를 버린 minute 열을 붙인다
  File "…/anomaly_detection/traffic_detection.py", line 23, in add_minute_column
    minutes = times.floor("min")  # .dt 를 빼먹었다
AttributeError: 'Series' object has no attribute 'floor'
```

  - 줄 번호는 사람마다 다릅니다.
- <mark>요청이 하나도 없던 분은 결과에 나오지 않습니다.</mark> 분당 요청 수 14줄은 요청이 있던 분만 센 것입니다.

**관제에서는**

- <mark>급증 기준은 요일 · 시간대마다 평소가 다르므로 시간대별 평소 평균을 따로 둡니다.</mark> 이 문서의 `baseline_traffic.csv`(지난 7일, 오전 9시대)는 연습용 하나뿐입니다.

---

## Exercise 5-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise5-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise5-2_run.py` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 네 함수입니다.

① `make_alert` 안

```python
    alert = {"type": alert_type, "target": target, "count": count, "note": note, "status": "확인 필요"}  # 알림 한 건의 키 다섯 개
```

② `make_login_alerts` 안

```python
        alert = make_alert("비정상 로그인", ip_address, count, note)  # 로그인 실패 알림 한 건을 만든다
```

③ `make_traffic_alerts` 안

```python
        target = str(minute)                                    # 시각 값을 문자열로 바꾼다 — JSON 에는 시각 값을 그대로 쓸 수 없다
        alert = make_alert("트래픽 급증", target, count, note)  # 트래픽 급증 알림 한 건을 만든다
```

④ `save_alerts` 안

```python
    with open(path, "w", encoding="utf-8") as file:            # 파일을 쓰기 위해 열고 file 변수로 쓴다
        json.dump(alerts, file, ensure_ascii=False, indent=2)  # 한글은 그대로, 들여쓰기를 해서 파일에 쓴다
```

**결과**

- (가) 출력은 다음과 같고, 알림은 모두 <mark>**2건**</mark>(로그인 실패 1건 + 트래픽 급증 1건)입니다.

```
--- 단계 1: 로그인 실패 알림 1 건
--- 단계 2: 트래픽 급증 알림 1 건
--- 단계 3: alerts.json 에 알림 2 건 저장
--- 단계 4: 저장된 알림
{'type': '비정상 로그인', 'target': '203.0.113.50', 'count': 5, 'note': '로그인 실패가 기준 이상 — 공격 확정이 아니라 먼저 살펴볼 곳', 'status': '확인 필요'}
{'type': '트래픽 급증', 'target': '2026-11-02 09:12:00', 'count': 9, 'note': '요청이 평소의 3배 이상으로 늘어남 — 공격 확정이 아니라 먼저 살펴볼 곳', 'status': '확인 필요'}
```

  - `alerts.json` 의 내용은 다음과 같습니다.

```
[
  {
    "type": "비정상 로그인",
    "target": "203.0.113.50",
    "count": 5,
    "note": "로그인 실패가 기준 이상 — 공격 확정이 아니라 먼저 살펴볼 곳",
    "status": "확인 필요"
  },
  {
    "type": "트래픽 급증",
    "target": "2026-11-02 09:12:00",
    "count": 9,
    "note": "요청이 평소의 3배 이상으로 늘어남 — 공격 확정이 아니라 먼저 살펴볼 곳",
    "status": "확인 필요"
  }
]
```

- (나) <mark>두 알림은 같은 일과 관련이 있어 보입니다.</mark>
  - 겹치는 단서: 로그인 실패 알림의 주소 `203.0.113.50` 이 09:12:03 ~ 09:12:15 에 로그인(`POST /login`)을 5번 실패했고, 트래픽 급증 알림의 분 `09:12` 에 들어온 요청 9개도 모두 이 주소의 것입니다.
  - 다루는 법: <mark>알림 두 건을 따로 처리하지 않고 「203.0.113.50 이 09:12 에 로그인을 반복한 한 사건」으로 통합해 한 번에 조사합니다.</mark> 성공한 로그인 계정과 뒤이은 관리자 경로 요청까지 함께 봅니다.
- (다) <mark>`status` 를 「조사 완료」로 바꾸고,</mark> `note` 에 「직원이 비밀번호를 잊어 반복 입력함」과 확인한 사람 · 날짜를 적습니다.
  - 알림을 지우지 않고 남겨 두면, 같은 주소에서 다시 알림이 났을 때 <mark>이전 조사 결과를 보고 빨리 판단할 수 있습니다.</mark> 같은 일이 자주 생기면 알림 기준을 고칠 근거도 됩니다.
  - 알림이 있어도 공격으로 확정된 것이 아니므로 <mark>조사 결과가 정상이든 공격이든 처리 상태는 「조사 완료」이고</mark>, 정상인지 대응이 필요한지는 `note` 에 적습니다.

**왜**

- <mark>알림의 모양을 하나로 맞추면 탐지 규칙이 늘어도 담당자의 처리 방법과 알림을 보내는 코드가 그대로입니다.</mark> `make_login_alerts` · `make_traffic_alerts` 처럼 규칙마다 알림을 만드는 함수 하나만 더 만들면 됩니다.

**자주 틀리는 곳**

- `target = str(minute)` 대신 **`target = minute` 으로 두면 `json.dump` 에서 오류가 납니다.** 판다스의 시각 값은 JSON 에 쓸 수 없습니다.
  - 실행하면 다음 오류가 납니다(<mark>`Object of type Timestamp is not JSON serializable`</mark> 이 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/exercise5-2_run.py", line 23, in <module>
    saved_count = save_alerts(all_alerts, ALERTS_PATH)  # 모은 알림을 파일에 저장하고 저장한 건수를 받는다
  File "…/anomaly_detection/alerts.py", line 54, in save_alerts
    json.dump(alerts, file, ensure_ascii=False, indent=2)  # 한글은 그대로, 들여쓰기를 해서 파일에 쓴다
TypeError: Object of type Timestamp is not JSON serializable
```

  - 줄 번호는 사람마다 다릅니다.
- `json.dump` 에서 `ensure_ascii=False` 를 빼면 한글이 `\ube44\uc815\uc0c1` 같은 코드(「비정상」을 코드로 쓴 모양)로 저장됩니다. <mark>오류는 나지 않지만 파일을 열어 보면 알림 내용을 알아볼 수 없습니다.</mark>
- `with` 줄 아래의 6번 코드는 **공백 8개로 씁니다.** 4개로 쓰면 `IndentationError` 오류가 납니다. `with` 줄 끝의 `:` 도 빠뜨리지 않습니다.

**관제에서는**

- 알림 파일에는 처리 상태 키(`status`)가 있어서, 담당자가 「확인 필요」 → 「조사 중」 → 「조사 완료」처럼 바꿔 가며 <mark>어디까지 봤는지 남깁니다.</mark>

---

## 정답 마무리

 **터미널에 입력합니다.**

```bash
cd ..
pwd
git status
```
- 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 있는 폴더의 위치 확인 · `git status` 올릴 파일의 상태를 봄

<mark>`.env` 나 `.venv` 가 없는 것을 확인한 뒤에 아래를 칩니다.</mark>

```bash
git add .
git commit -m "Add anomaly detection unit 4 and unit 5 baseline and alerts"
git push
```
- 명령 풀이: `git add .` 바뀐 파일을 올릴 대상에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림

**결과**

- (가) 한 예: 「`.env` · `.venv` 는 보이지 않았다」. 보였다면 `.gitignore` 에 `.env`(또는 `.venv`) 한 줄을 적고 저장한 뒤 `git status` 를 다시 쳤다고 적습니다.

**왜**

- <mark>올리기 전에 올라갈 파일을 확인해야 비밀 키가 섞이지 않습니다.</mark>

**자주 틀리는 곳**

- <mark>`.env` 가 보이는데 그대로 `git add .` 를 하는 실수가 가장 위험합니다.</mark>
  - `cd ..` 를 두 번 쳐서 `security-agent-toolkit` 바깥으로 나가는 경우도 있습니다. `pwd` 로 확인합니다.
