---
id: m3-u05-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/084_day03_pm_sla.md
  mission_id: GichanSource.m3-1023-pm-sla
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

**채운 코드** (한 예)

```python
    breached = []                                                # 기한을 초과한 요청서를 담을 빈 리스트
    for request in requests:                                     # 요청서를 하나씩 꺼낸다
        if request["status"] == "reviewing":                     # 검토 중인 것만 본다(처리가 끝난 것은 기한을 따지지 않는다)
            requested = datetime.strptime(request["requested_at"], TIME_FORMAT)   # 접수 시각 문자열을 시각으로 바꾼다
            hours = (now - requested).total_seconds() / 3600     # 지금까지 걸린 시간을 시간(hour) 단위 숫자로 구한다
            if hours > SLA_HOURS:                                # 걸린 시간이 SLA 시간보다 크면
                overdue = request.copy()                         # 요청서를 복사한다(원래 요청서는 바꾸지 않는다)
                overdue["wait_hours"] = round(hours, 1)          # 지난 시간을 소수 첫째 자리까지 반올림해 복사본에 적는다
                breached.append(overdue)                         # 기한을 초과한 리스트에 복사본을 추가한다
    return breached                                              # 기한을 초과한 요청서 리스트를 리턴한다
```

**결과**

- (가) 출력은 다음과 같고, SLA 를 초과한 요청은 **1번**(접수 08:30, 5.5시간 지남)과 **5번**(접수 07:50, 6.2시간 지남)입니다. 6번은 10:00 에 접수해 정확히 4시간이라 초과하지 않았습니다.

```
--- 단계 1: 현황 - SLA 시간 4 시간, 지금 14:00
1 seoyeon reviewing 2026-10-23 08:30
2 gaeun reviewing 2026-10-23 10:30
3 dami reviewing 2026-10-23 12:00
4 junho approved 2026-10-23 09:00
5 seoyeon reviewing 2026-10-23 07:50
6 tester reviewing 2026-10-23 10:00
--- 단계 2: 판정 - SLA 를 초과한 요청
1 seoyeon 접수 2026-10-23 08:30 -> 5.5 시간 지남
5 seoyeon 접수 2026-10-23 07:50 -> 6.2 시간 지남
```

- (나) 한 예: 기한을 초과한 요청서를 찾으면 ① 먼저 요청서를 맡은 승인자(`security_manager`)에게 알림을 보내 오늘 안에 처리하게 합니다. ② 알림 뒤에도 일정 시간(예: 2시간) 더 지나면 승인자의 윗사람이나 대리 승인자에게 넘깁니다(에스컬레이션). 처음 기한을 초과했을 때는 알림만 하고, 더 지나도 처리가 없을 때 넘기는 식으로 단계를 나눕니다. 요청자에게는 「검토가 늦어지고 있다」는 상태를 알려 메신저로 재촉해 오는 일을 줄입니다.
- (다) 4번(junho)은 접수한 지 5시간이 지났지만 이미 승인되어 처리가 끝난 요청입니다. 상태를 확인하지 않고 접수 시각만으로 세면 ① 초과 리스트에 이미 처리된 요청(4번)이 섞입니다. ② 그 리스트를 받은 담당자는 이미 끝난 일을 다시 확인하느라 시간을 쓰고, 정말 늦어진 요청을 찾기 어려워집니다. 기한은 아직 처리되지 않은 요청에만 의미가 있으므로 `reviewing` 인지 먼저 봅니다.

**왜** — 기한을 따지려면 「아직 처리되지 않았는가」와 「접수한 지 얼마나 됐는가」를 둘 다 봐야 합니다. 시각에서 시각을 빼면 걸린 시간이 나오고, 그 시간을 SLA 와 비교하는 것이 전부입니다. SLA 시간을 파일로 빼 두면 4시간을 2시간으로 줄일 때 코드를 고치지 않아도 됩니다.

**자주 틀리는 곳** — `.total_seconds()` 에서 `/ 3600` 을 빼먹는 경우가 가장 많습니다. 걸린 시간이 초 단위(예: 19800.0)라서 SLA 4 보다 항상 커지고, 검토 중인 요청서가 모두 기한 초과로 나옵니다. 실행하면 다음처럼 됩니다(정확히 4시간인 6번까지 나오는 것이 신호입니다).

```
--- 단계 2: 판정 - SLA 를 초과한 요청
1 seoyeon 접수 2026-10-23 08:30 -> 19800.0 시간 지남
2 gaeun 접수 2026-10-23 10:30 -> 12600.0 시간 지남
3 dami 접수 2026-10-23 12:00 -> 7200.0 시간 지남
5 seoyeon 접수 2026-10-23 07:50 -> 22200.0 시간 지남
6 tester 접수 2026-10-23 10:00 -> 14400.0 시간 지남
```

`hours > SLA_HOURS` 를 `>=` 로 쓰면 정확히 4시간인 6번도 초과로 나옵니다. `datetime.strptime` 에 형식 문자열 대신 다른 값을 넣으면 `ValueError` 가 납니다.

**관제에서는** — 기한을 초과한 요청 건수는 승인이 밀리는 곳을 보는 숫자입니다. 같은 승인자에게 계속 쌓이면 승인자를 늘리거나 대리 승인자를 정합니다. 오래 방치된 요청이 갑자기 승인되는 경우는 요청 당시와 상황이 달라졌는지 다시 확인합니다.

---

## Exercise 5-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise5-2_run.py
```

**채운 코드** (한 예)

```python
    with open(path, "w", encoding="utf-8") as output_file:                 # 파일을 쓰기 모드("w")로 연다
        json.dump(requests, output_file, ensure_ascii=False, indent=2)     # 리스트를 파일에 JSON 으로 쓴다
    return len(requests)                                         # 저장한 요청서 건수를 리턴한다
```

```python
    counts = {}                                                  # 상태 → 건수를 담을 빈 딕셔너리
    for request in requests:                                     # 요청서를 하나씩 꺼낸다
        status = request["status"]                               # 그 요청서의 상태를 꺼낸다
        old_count = counts.get(status, 0)                        # 그 키의 지금까지 센 수(처음이면 0)
        counts[status] = old_count + 1                           # 1 늘려서 다시 적는다
    return counts                                                # 상태별 건수를 리턴한다
```

**결과**

- (가) 출력은 다음과 같고(단계 3 첫 줄 `저장 함수가 리턴한 건수` 는 `save_requests` 의 마지막 줄 `return len(requests)` 가 만든 값입니다), `requests.json` 에 저장된 요청서는 **6건**이며 상태별 건수는 `granted` 1건 · `rejected` 1건 · `approved` 2건 · `reviewing` 2건입니다.

```
--- 단계 1: 처리 - 승인 · 반려 · 부여
1 seoyeon granted -> 부여
2 gaeun rejected -> 승인되지 않음
3 dami approved -> 부여하지 않음(퇴사한 계정)
4 junho approved -> 부여하지 않음(허용)
5 seoyeon reviewing -> 승인되지 않음
6 tester reviewing -> 승인되지 않음
--- 단계 2: 점검 - 상태별 건수와 SLA
{'granted': 1, 'rejected': 1, 'approved': 2, 'reviewing': 2}
SLA 초과 요청 번호: 5
--- 단계 3: 저장 - requests.json
저장 함수가 리턴한 건수: 6
저장한 요청서 6 건, 첫 요청서의 상태: granted
```

- (나) 반려되거나 부여되지 않은 요청서도 「그런 요청이 있었고 이렇게 처리됐다」는 사실이기 때문입니다. 지우면 나중에 같은 사람이 같은 요청을 반복하는지, 승인자가 어떤 요청을 반려했는지, 퇴사한 사람의 요청이 승인까지 갔는지를 알 수 없습니다. 감사에서는 처리된 것뿐 아니라 거절된 것도 증빙이 됩니다.
- (다) 숫자가 말하는 막힌 곳은 두 군데입니다. ① `reviewing` 2건은 승인자가 아직 처리하지 않은 요청입니다(그중 5번은 4시간을 초과했습니다). ② `approved` 2건은 승인은 됐지만 정책 확인에서 부여되지 않은 요청입니다(퇴사한 계정 · 이미 허용된 권한). 막힌 곳이 다르므로 ①은 승인자에게 처리를 재촉하고, ②는 요청자에게 부여되지 않은 이유를 알려 요청을 정리합니다. 막힌 곳과 조치가 이어져 있으면 맞습니다.

**왜** — 프로그램 안의 요청서는 프로그램이 끝나면 사라지므로, 이력은 파일로 남겨야 합니다. `"w"` 로 열면 파일 내용이 새로 쓰여서 항상 가장 최근의 전체 리스트가 저장됩니다. 상태별 건수는 처리가 어디에서 막히는지 보여 주는 가장 간단한 숫자입니다.

**자주 틀리는 곳** — `json.dump` 에서 `ensure_ascii=False` 를 빼먹는 경우가 가장 많습니다. 파일은 만들어지지만 한글이 `\uXXXX` 문자열로 저장되어 사람이 읽을 수 없습니다. 실행한 뒤 `requests.json` 의 앞부분이 다음처럼 보이면 그 실수입니다.

```
[
  {
    "id": 1,
    "user": "seoyeon",
    "resource": "SETTLE",
    "action": "QUERY",
    "permission": "SETTLE:QUERY",
    "until": "2026-10-27 18:00",
    "reason": "\uc815\uc0b0 \ub300\uc870 \uc9c0\uc6d0",
    "requested_at": "2026-10-23 08:30",
```

파일을 `"w"` 대신 읽기 모드(`"r"`)로 열면 `io.UnsupportedOperation: not writable` 오류가 납니다. `with` 줄 아래를 들여쓰지 않으면 `IndentationError: expected an indented block` 오류가 납니다.

**관제에서는** — 요청 이력 파일은 과다권한 점검의 입력이 됩니다. 「누가 어떤 권한을 받았고 아직 쓰이는가」를 이력과 접속 기록을 맞춰 봅니다. 실무에서는 이력을 날짜별 파일로 나눠 남기고(오늘은 가장 최근 리스트 하나만 저장합니다), 파일 자체도 접근 권한을 제한합니다.

---

## 정답 마무리

 **터미널에 입력합니다.**

```bash
cd ..
pwd
git status
git add .
git commit -m "Add access control day 3 request, approval, grant, SLA and history"
git push
```

**결과**

- (가) 한 예: 「줄이 열여섯 개였고(`.py` 열 개 + `config/sla.json` 한 개 + `requests.json` 한 개 + `.md` 네 개), `.env` · `.venv` 는 없었다」. 이 16줄은 `__pycache__` 가 보이지 않을 때의 숫자이고, 줄 수와 이름은 학생마다 다를 수 있습니다. `.env` 나 `.venv` 가 보였다면 `.gitignore` 에 한 줄을 적고 `git status` 를 다시 쳤다고 적습니다.

**왜** — 올리기 전에 올라갈 파일을 확인해야 비밀 키가 섞이지 않습니다. 요청 처리 코드와 이력 파일이 함께 올라가야 다음에 누가 보아도 같은 흐름을 따라갈 수 있습니다.

**자주 틀리는 곳** — `.env` 가 보이는데 그대로 `git add .` 를 하는 실수가 가장 위험합니다. `cd ..` 를 두 번 쳐서 `security-agent-toolkit` 바깥으로 나가는 경우도 있습니다. `pwd` 로 확인합니다.

**관제에서는** — 접근통제 코드와 요청 이력은 같은 커밋에 함께 올려, 어느 요청이 어느 코드로 처리됐는지 이력으로 남깁니다.

---

## 앞 Exercise 파일 완성본

Exercise 5-1 파일을 못 만들고 Exercise 5-2로 넘어가야 할 때 그대로 만들어 씁니다. 정답 본문을 머리말과 합친 전체 파일입니다.

**`config/sla.json`**

```json
{"hours": 4}
```

**`req_sla.py`** (Exercise 5-1 완성본)

```python
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from config_loader import load_json                              # Unit 3에서 만든 안전한 읽기 함수를 불러온다
from exception_policy import TIME_FORMAT                         # 시각 문자열의 형식("%Y-%m-%d %H:%M")을 불러온다

SLA_HOURS = load_json("config/sla.json", {"hours": 4})["hours"]  # 처리 기한(시간). 파일이 없거나 깨졌으면 기본값 4


def check_sla_breach(requests, now):                             # 요청서 리스트와 지금 시각(datetime)을 받는 함수
    """처리 기한(SLA_HOURS)을 넘긴 검토 중 요청서 리스트를 리턴한다.
    오래 방치된 요청을 담당자에게 알릴 때 쓴다.
    """
    breached = []                                                # 기한을 초과한 요청서를 담을 빈 리스트
    for request in requests:                                     # 요청서를 하나씩 꺼낸다
        if request["status"] == "reviewing":                     # 검토 중인 것만 본다(처리가 끝난 것은 기한을 따지지 않는다)
            requested = datetime.strptime(request["requested_at"], TIME_FORMAT)   # 접수 시각 문자열을 시각으로 바꾼다
            hours = (now - requested).total_seconds() / 3600     # 지금까지 걸린 시간을 시간(hour) 단위 숫자로 구한다
            if hours > SLA_HOURS:                                # 걸린 시간이 SLA 시간보다 크면
                overdue = request.copy()                         # 요청서를 복사한다(원래 요청서는 바꾸지 않는다)
                overdue["wait_hours"] = round(hours, 1)          # 지난 시간을 소수 첫째 자리까지 반올림해 복사본에 적는다
                breached.append(overdue)                         # 기한을 초과한 리스트에 복사본을 추가한다
    return breached                                              # 기한을 초과한 요청서 리스트를 리턴한다
```
