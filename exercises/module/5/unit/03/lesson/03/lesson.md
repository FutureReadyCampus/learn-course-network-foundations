---
id: m5-u03-l03
title: 실습 3-2 · 티켓 생성과 응답 기한 계산하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/126_day04_am_ticket_notice.md
  mission_id: GichanSource.m5-1112-am-ticket-notice
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 3-2 · 티켓 생성과 응답 기한 계산하기

## 목표: 티켓과 응답 기한

> **오늘 들어온 일**
>
> - **상황**: <mark style="background:#e0d4ff">지금까지 만든 흐름은 조치를 실행한 뒤</mark> 「조치 완료」라는 기록 한 줄만 남겼습니다. 오늘 근무 3시간 동안 알림 11건이 수신됩니다. `INC-201` 은 퇴사한 `dami` 의 계정을 잠그는 조치를 했습니다. `INC-207` 은 IP `203.0.113.250` 의 차단을 시도했습니다. 조치 뒤에 실제 상태를 다시 조회해 확인하는 일을 사후 검증이라고 합니다. <mark style="background:#ffc4d6">사후 검증에서 실제로는 차단되지 않은 것으로 확인됐습니다</mark>.
> - **문제**: 기록 한 줄만으로는 담당자가 네 가지를 알 수 없습니다. 어떤 사건인지, 이미 어떤 조치를 했는지, 이어서 무엇을 해야 하는지, 언제까지 응답해야 하는지입니다. 또한 사후 검증에 실패한 `INC-207` 이 정상 조치된 알림과 구별되지 않습니다. 그래서 후속 확인이 누락되고, 차단되지 않은 IP 가 그대로 남습니다.
> - **부탁**: 알림이 수신되면 <mark>제목 · 조치 내역 · 후속 조치 · 응답 기한(SLA)을 기재한 티켓을 자동으로 생성해 주세요</mark>. 티켓은 사건 한 건의 처리 상태를 적어 두는 기록입니다. 응답 기한(SLA)은 알림을 수신한 뒤 담당자가 몇 분 안에 응답해야 하는지 정한 기한입니다. 사후 검증에 실패한 건은 담당자가 직접 확인하도록 표시해 주세요.
> - **바뀌는 점**: 담당자는 티켓만 읽고 바로 대응을 시작할 수 있습니다. 예를 들어 `INC-201` 은 high 등급이라 티켓에 응답 기한 15분이 적힙니다. 오늘 샘플에서는 `INC-207` 한 건이 「직접 확인」 대상으로 별도 표시됩니다. 상황과 이름은 설명을 위한 예시입니다.

## 1.1 티켓은 담당자의 네 가지 질문 「사건 개요 · 이미 수행한 조치 · 후속 조치 · 응답 기한」에 답해야 한다

**티켓**(ticket)은 사건 한 건의 처리 상태 · 담당자 · 조치 이력을 추적하는 기록입니다. Unit 1 실습 1-2의 `run_action` 은 `id` · `incident` · `target` 세 가지만 담긴 간단한 티켓을 만들었습니다. 알림으로 티켓을 생성해 등록하는 일을 **티케팅**(ticketing)이라고 합니다. 오늘은 티켓에 어떤 정보를 기재할지 정합니다. 담당자는 티켓을 열면 아래 네 가지를 확인하려 합니다.

| 담당자의 질문 | 티켓의 키 | 값을 정하는 방법 | 직접 쓰는 곳 |
|---|---|---|---|
| 무슨 일인가 | `title` | 등급 · 대상 · 탐지 규칙을 이어 붙여 제목을 만든다 | |
| 이미 무엇을 했나 | `done` | 알림에 기재된 조치 내역을 그대로 복사한다 | |
| 다음에 무엇을 하나 | `next_step` | 알림 상태별로 정해 둔 후속 조치 문장을 선택한다 | |
| (검증 실패 시) | `next_step` | 직접 확인을 지시하는 문장으로 교체한다 | |
| 언제까지 응답하나 | `sla_due` | <mark style="background:#ffdcb0">알림 수신 시각 + 등급별 응답 기한</mark> | ① · ② |

예를 들어 제목은 `[high] dami — 퇴사한 계정` 모양이고, 응답 기한 시각은 0분 + 15분 = 15분처럼 계산합니다. `next_step` 은 사후 검증에 실패했을 때만 교체합니다.

- **응답 기한**(SLA, Service Level Agreement, 에스엘에이: 서비스 수준 협약)은 알림을 수신한 뒤 담당자가 응답해야 하는 시간의 약속입니다. `escalation_rules.json` 의 `sla_minutes` 에 등급별로 정의되어 있으며, <mark style="background:#ffdcb0">high 는 15분, mid 는 60분, low 는 240분</mark>입니다. 응답 기한은 시간의 길이입니다. 티켓의 `sla_due` 에 적는 **응답 기한 시각**은 알림 수신 시각에 응답 기한을 더한 값입니다.
  - 예를 들어 `INC-201` 은 0분에 수신된 high 알림이라 15분 안에 응답해야 합니다. 그래서 TCK-1 의 응답 기한 시각은 0 + 15 = 15분입니다.
  - `INC-202` 는 3분에 수신된 low 알림이라, TCK-2 의 응답 기한 시각은 3 + 240 = 243분입니다.
- 알림 상태(`status`)는 아래 표의 세 가지입니다. 상태별로 담당자가 수행할 후속 조치가 다르므로, 후속 조치 문장(`next_step`)도 상태별로 따로 정의합니다.

| 알림 상태 | 뜻 |
|---|---|
| `조치됨` | 자동 조치 완료 |
| `승인 대기` | 담당자의 승인을 기다리는 중 |
| `조치 없음` | 자동 조치 대상 아님 |

- `done` 문장 끝에 「(확인 실패)」가 붙은 조치가 있습니다. 조치는 실행했지만, 사후 검증에서 실제 상태가 바뀌지 않은 것으로 확인된 조치라는 뜻입니다. 예를 들어 `INC-207` 의 `IP 차단: 차단되지 않음 → 차단되지 않음 (확인 실패)` 가 그렇습니다. <mark style="background:#e0d4ff">Unit 2 실습 2-1에서 본 조치 후 확인(사후 검증)처럼, 이 결과는 알림 파일 `alerts_thu.json` 에 이미 적혀 있습니다</mark>. 이런 조치는 담당자가 수동 검증(manual verification: 사람이 실제 상태를 직접 조회해 확인하는 일)으로 직접 확인해야 하므로, 티켓에 별도로 표시합니다.
- 정의되지 않은 상태가 입력될 수 있습니다. 그래도 프로그램이 중단되지 않도록, 딕셔너리에서 키가 없을 때 기본값을 리턴하는 `.get(키, 기본값)` 을 사용합니다(Unit 2 실습 2-2의 `state["sessions"].get(user, [])` 와 같은 모양입니다).
- 미리 채운 `"TCK-" + str(ticket_no)` 의 `str()` 은 숫자를 문자열로 바꿉니다. 숫자는 `+` 로 문자열과 바로 이어 붙일 수 없어서, `1` 을 `"1"` 로 바꾼 뒤 이어 붙여 `"TCK-1"` 을 만듭니다.

<h2>줄임말 이름 안내</h2>

코드에는 줄임말로 된 키 이름이 있습니다. 다른 Unit 파일과 맞추기 위해 이름은 그대로 쓰고 뜻만 풀어 둡니다.

- `sla` 는 서비스 수준 협약(SLA, Service Level Agreement)의 줄임말입니다. 이 문서에서는 응답 기한을 뜻합니다.
- `acked_at` 의 `acked` 는 acknowledged(확인했다)의 줄임말입니다.

| 이름 | 뜻 |
|---|---|
| `sla_minutes` | 응답 기한(분) |
| `sla_table` | 등급마다 정한 응답 기한(분) 표 |
| `sla_due` | 응답해야 하는 시각 |
| `sla_count` | 응답 기한을 정한 등급 수 |
| `acked_at` | 담당자가 티켓을 처음 확인한 시각(분) |

`acked_at` 은 오늘은 `-1`(아직 없음)로 두고, 응용 3-2에서 상태를 바꿀 때 채웁니다. 티켓 딕셔너리 아래쪽의 `count` · `incidents` · `notified_count` · `last_notified` · `resolved_at` · `escalation_level` · `comments` 도 응용 3-2 · 3-3과 Unit 4에서 씁니다. 오늘은 읽기만 합니다.

**직접 쓰는 곳은 두 군데**(① · ②)입니다. 응답 기한 시각을 계산하는 `make_ticket` 의 두 줄이고, 나머지는 모두 미리 채워 두었습니다.

| 파일 | 함수 | 직접 쓰는 곳 | 하는 일 |
|---|---|---|---|
| `ticketing.py` | `make_title` | 없음 | 등급 · 대상 · 규칙으로 티켓 제목을 만든다 |
| `ticketing.py` | `find_next_step` | 없음 | 알림 상태에 맞는 다음 할 일 문장을 고른다 |
| `ticketing.py` | `has_failed_action` | 없음 | 조치 내역에 「확인 실패」가 있는지 확인한다 |
| `ticketing.py` | `make_ticket` | ① · ② | 응답 기한을 계산해 티켓 한 장을 만든다 |
| `exercise3-2_run.py` | (실행 파일) | 없음 | 알림마다 티켓을 만들어 모으고, 직접 확인할 수를 센다 |

<h3>문법 상자 · 직접 쓰는 곳의 모양 (예시 값 · 읽기만 합니다)</h3>

```python
sla_table = {"high": 15, "mid": 60, "low": 240}   # 등급 → 응답 기한(분) 딕셔너리
alert = {"minute": 3, "grade": "low"}              # 예시 알림 (3분에 온 low 알림)

print(alert["grade"])                              # low
print(sla_table[alert["grade"]])                   # 240  · 대괄호 안에 또 대괄호: 알림 등급으로 기한을 꺼낸다
print(alert["minute"] + 240)                       # 243  · 숫자끼리 + 는 더하기
```

- `변수 = 값` 은 오른쪽 값을 왼쪽 이름에 저장합니다. ① · ② 모두 이 모양입니다.
- `sla_table[alert["grade"]]` 는 안쪽 `alert["grade"]`(예: `"low"`)를 먼저 읽고, 그 값으로 `sla_table["low"]` 를 꺼냅니다.

## 실습 3-2 · 티켓 생성과 응답 기한 계산하기

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>알림 11건에는 조치 기록만 있고, 담당자의 후속 조치와 응답 기한이 기재되어 있지 않습니다</mark>.
- **만드는 것**: 제목 · 후속 조치 · 수동 확인 표시 · 응답 기한(SLA)을 기재한 티켓을 생성하는 코드(`ticketing.py`)와, 알림마다 티켓을 생성해 리스트에 저장하는 코드(`exercise3-2_run.py`)입니다.
- **실행하면**: <mark>단계 1: 불러온 알림 수, 단계 2: 알림마다 만든 티켓, 단계 3: 티켓 본문 예, 단계 4: 직접 확인이 필요한 티켓이 나옵니다.</mark>

<h2>할 일</h2>

1. `soar_response` 폴더에 `ticketing.py` · `exercise3-2_run.py` 두 파일을 만들어 아래 코드를 붙여 넣습니다.
2. `ticketing.py` 의 `# ←` 가 있는 <mark>두 곳</mark>(① · ②)을 한 줄씩 채웁니다.
3. 실행해서 단계 2 ~ 4 를 읽습니다.

<h3><code>ticketing.py</code></h3>

알림으로 티켓을 생성합니다. 이 파일은 나중에 「선택 과제용 티켓 병합·알림 함수 준비」 레슨의 `ticket_merge.py` 와 Unit 5 실습 5-1이 가져다 씁니다(import). 직접 쓰는 곳은 `make_ticket` 의 ① · ② 입니다.

```python exercise
DEFAULT_NEXT_STEP = "담당자가 알림 내용을 읽고 필요한 일을 정한다"                      # 알림 상태를 모를 때 쓰는 다음 할 일
MANUAL_STEP = "조치가 확인되지 않았다. 담당자가 직접 계정이나 IP 상태를 보고 조치한다"  # 조치 확인에 실패한 티켓의 다음 할 일
NEXT_STEPS = {                                                                          # 알림 상태마다 담당자가 할 다음 일
    "조치됨": "조치 결과가 맞는지 확인하고 계정이나 IP 상태를 점검한다",                # 자동 조치가 끝난 알림
    "승인 대기": "승인할지 거절할지 정하고 정한 사람의 이름을 남긴다",                  # 승인을 기다리는 알림
    "조치 없음": "자동 조치가 없는 알림이니 직접 보고 조치가 필요한지 정한다",          # 자동 조치 대상이 아닌 알림
}


def make_title(alert):                                                                  # 알림 한 건을 받는 함수
    """티켓 제목(등급 · 대상 · 규칙)을 문자열로 만들어 리턴한다.
    티켓 목록에서 제목만 봐도 무슨 일인지 알 수 있게 할 때 쓴다.
    """
    grade = alert["grade"]                                                              # 알림 등급
    entity = alert["entity"]                                                            # 알림 대상(사용자 이름 또는 IP)
    rule = alert["rule"]                                                                # 탐지된 규칙 이름
    return "[" + grade + "] " + entity + " — " + rule                                   # 등급 · 대상 · 규칙을 이어 붙인 제목을 리턴한다


def find_next_step(alert, next_steps):                                                  # 알림 한 건과 다음 할 일 딕셔너리를 받는 함수
    """알림 상태에 맞는 다음 할 일 문장을 리턴한다. 정해 둔 문장이 없으면 기본 문장을 리턴한다.
    담당자가 티켓을 열자마자 무엇부터 할지 알게 할 때 쓴다.
    """
    status = alert["status"]                                                            # 알림 상태(조치됨 · 승인 대기 · 조치 없음)
    return next_steps.get(status, DEFAULT_NEXT_STEP)                                    # 상태에 맞는 다음 할 일을 리턴한다 (없으면 기본 문장)


def has_failed_action(done_list):                                                       # 조치 내역 문장 리스트를 받는 함수
    """조치 내역에 「확인 실패」가 들어 있는 문장이 하나라도 있으면 True, 없으면 False 를 리턴한다.
    조치했다고 했지만 실제로 바뀌지 않은 알림을 사람이 직접 보게 할 때 쓴다.
    """
    for text in done_list:                                                              # 조치 내역 문장을 하나씩 읽는다
        if "확인 실패" in text:                                                         # 문장 안에 확인 실패가 있으면
            return True                                                                 # 확인 실패가 있다고 True 를 리턴한다
    return False                                                                        # 하나도 없으면 False 를 리턴한다


def make_ticket(alert, ticket_no, rules, next_steps):                                   # 알림 · 티켓 번호 · 규칙 · 다음 할 일 딕셔너리를 받는 함수
    """알림 한 건으로 티켓 한 장(딕셔너리)을 만들어 리턴한다. 만든 시각과 응답 기한(SLA)을 함께 적는다.
    알림이 오면 바로 담당자가 읽을 수 있는 티켓을 만들 때 쓴다.
    """
    sla_table = rules["sla_minutes"]                                                    # 등급마다 정한 응답 기한(분) 표
    # ① sla_table[alert["grade"]] 를 sla_minutes 에 저장한다 (이 알림 등급의 응답 기한)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
#|     sla_minutes = sla_table[alert["grade"]]
    # ② alert["minute"] + sla_minutes 를 sla_due 에 저장한다 (응답해야 하는 시각)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
#|     sla_due = alert["minute"] + sla_minutes
    needs_manual = has_failed_action(alert["done"])                                     # 조치 확인에 실패한 내역이 있는지
    next_step = find_next_step(alert, next_steps)                                       # 다음 할 일 문장
    if needs_manual:                                                                    # 확인 실패가 있으면
        next_step = MANUAL_STEP                                                         # 직접 확인하라는 문장으로 바꾼다
    ticket = {                                                                          # 티켓 한 장
        "id": "TCK-" + str(ticket_no),                                                  # 티켓 번호
        "title": make_title(alert),                                                     # 제목
        "entity": alert["entity"],                                                      # 대상
        "rule": alert["rule"],                                                          # 규칙
        "grade": alert["grade"],                                                        # 등급
        "playbook": alert["playbook"],                                                  # 실행한 플레이북
        "done": alert["done"],                                                          # 조치 내역
        "status": "열림",                                                               # 티켓 상태 : 처음에는 열림
        "next_step": next_step,                                                         # 다음 할 일
        "needs_manual": needs_manual,                                                   # 직접 확인이 필요한지
        "created_at": alert["minute"],                                                  # 만든 시각(분)
        "updated_at": alert["minute"],                                                  # 마지막으로 갱신한 시각(분)
        "sla_due": sla_due,                                                             # 응답 기한 시각(분)
        "count": 1,                                                                     # 합쳐진 알림 수 : 처음에는 1
        "incidents": [alert["id"]],                                                     # 합쳐진 알림 번호
        "notified_count": 0,                                                            # 알림을 보낸 횟수
        "last_notified": -1,                                                            # 마지막으로 알림을 보낸 시각(분) : 아직 없음
        "acked_at": -1,                                                                 # 담당자가 처음 확인한 시각(분) : 아직 없음
        "resolved_at": -1,                                                              # 해결한 시각(분) : 아직 없음
        "escalation_level": 0,                                                          # 상급자에게 올린 단계 : 아직 없음
        "comments": [],                                                                 # 상태를 바꾼 기록
    }
    return ticket                                                                       # 만든 티켓을 리턴한다
```

<h3><code>exercise3-2_run.py</code></h3>

직접 쓰는 곳이 없으니 그대로 붙여 넣습니다. Unit 1 `incident.py` 가 같은 폴더에 있어야 합니다.

```python
from incident import load_json                                                                # Unit 1 파일의 JSON 읽기 함수를 불러온다
from ticketing import make_ticket, NEXT_STEPS                                                 # 방금 만든 티켓 함수를 불러온다

alerts = load_json("alerts_thu.json")                                                         # 오늘의 알림 파일을 리스트로 읽는다
rules = load_json("config/escalation_rules.json")                                             # 응답 기한 규칙 파일을 딕셔너리로 읽는다
sla_count = len(rules["sla_minutes"])                                                         # 응답 기한을 정한 등급이 몇 개인지 센다
print("--- 단계 1: 불러온 알림", len(alerts), "건 · 응답 기한을 정한 등급", sla_count, "개")  # 단계 1 시작을 알리는 줄

tickets = []                                                                                  # 만든 티켓을 저장할 빈 리스트
manual_count = 0                                                                              # 직접 확인이 필요한 티켓 수 : 처음에는 0
print("--- 단계 2: 알림마다 만든 티켓")                                                       # 단계 2 시작을 알리는 줄
for alert in alerts:                                                                          # 알림을 하나씩 읽는다
    ticket_no = len(tickets) + 1                                                              # 티켓 번호는 지금까지 만든 수 + 1
    ticket = make_ticket(alert, ticket_no, rules, NEXT_STEPS)                                 # 알림으로 티켓을 만든다
    tickets.append(ticket)                                                                    # 티켓 리스트에 추가한다
    print(ticket["id"], ticket["title"], "· 만든 시각", ticket["created_at"], "분 · 기한", ticket["sla_due"], "분")  # 티켓 한 줄을 출력한다
    if ticket["needs_manual"]:                                                                # 직접 확인이 필요하면
        manual_count = manual_count + 1                                                       # 직접 확인이 필요한 티켓 수를 1 늘린다

print("--- 단계 3: 티켓 본문 예 (TCK-1)")                                                     # 단계 3 시작을 알리는 줄
first = tickets[0]                                                                            # 첫 번째 티켓을 꺼낸다
print("제목:", first["title"])                                                                # 제목을 출력한다
print("조치 내역:")                                                                           # 조치 내역 제목을 출력한다
for text in first["done"]:                                                                    # 조치 내역 문장을 하나씩 읽는다
    print(" -", text)                                                                         # 문장 앞에 - 를 붙여 출력한다
print("다음 할 일:", first["next_step"])                                                      # 다음 할 일을 출력한다
print("응답 기한:", first["sla_due"], "분 (만든 시각", first["created_at"], "분)")            # 응답 기한을 출력한다

print("--- 단계 4: 직접 확인이 필요한 티켓", manual_count, "건")                              # 단계 4 시작을 알리는 줄과 건수
for ticket in tickets:                                                                        # 티켓을 하나씩 읽는다
    if ticket["needs_manual"]:                                                                # 직접 확인이 필요하면
        print(ticket["id"], ticket["title"], "→", ticket["next_step"])                        # 티켓과 다음 할 일을 출력한다
```

- 주석 줄은 그대로 두고, **각 주석 바로 아래 줄**에 씁니다. ① · ② 모두 함수 안의 저장 줄이라, 위아래 미리 채운 줄과 같이 4칸에서 시작합니다.
- ① 에서 만든 `sla_minutes` 를 ② 에서 씁니다. 그래서 ① 을 먼저 씁니다.

<h3>직접 쓰는 곳</h3>

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | 등급의 응답 기한을 `sla_minutes` 에 저장 | 4칸 |
| ② | 수신 시각 + 응답 기한을 `sla_due` 에 저장 | 4칸 |

- ① 확인: ① 만 쓰고 실행하면 여전히 `NameError: name 'sla_due' is not defined` 가 나옵니다. `sla_due` 는 ② 에서 만드니 정상입니다. 다른 오류(`KeyError` 등)가 나오면 ① 을 다시 봅니다. 막히면: 위 문법 상자의 `sla_table[alert["grade"]]` 를 그대로 쓰고, 앞에 `sla_minutes = ` 를 붙입니다.
- ② 확인: ② 까지 쓰고 실행하면 단계 2 첫 줄이 `TCK-1 [high] dami — 퇴사한 계정 · 만든 시각 0 분 · 기한 15 분` 이면 성공입니다. 막히면: 문법 상자의 `alert["minute"] + 240` 에서 `240` 자리에 ① 의 `sla_minutes` 를 넣고, 앞에 `sla_due = ` 를 붙입니다.
- 채우기 전에 실행하면 단계 1 과 단계 2 제목 줄까지 나온 뒤 `NameError: name 'sla_due' is not defined` 로 멈춥니다. 티켓에 적을 응답 기한 시각이 아직 없어서, 티켓을 한 장도 만들지 못한다는 뜻입니다.

<h2>순서</h2>

1. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `ticketing.py` 와 `exercise3-2_run.py` 를 이름 그대로 만들고, 위 코드 상자를 복사해 붙여 넣고 저장합니다.

<!-- checklist -->
- [ ] `ticketing.py` 를 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
- [ ] `exercise3-2_run.py` 를 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
<!-- /checklist -->

2. **[VS Code]** `ticketing.py` 의 `# ←` 두 곳(① · ②)을 채웁니다. 1.1 의 예 「0분 + 15분 = 15분」을 보고 씁니다. 막히면 아래 「실습 3-2 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다.
   ```bash
   python exercise3-2_run.py
   ```
   - 명령 풀이: `python` 파이썬으로 파일을 실행 · `exercise3-2_run.py` 실행할 파일

<!-- checklist -->
- [ ] `ticketing.py` 의 ① · ② 를 채우고 `python exercise3-2_run.py` 를 실행해 TCK-1 의 기한 `15 분` 이 나왔다
<!-- /checklist -->

4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다. 단계 2 는 11줄, 단계 3 은 6줄, 단계 4 는 숫자가 제목 줄에 함께 나오고 그 아래 1줄입니다.
5. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.

<!-- answer: 08|실습 3-2 정답 -->

**확인** — 단계 2 에 티켓 11줄이 나오고 TCK-1 의 기한이 `15 분`, TCK-2 의 기한이 `243 분` 이며, 단계 4 가 `직접 확인이 필요한 티켓 1 건` 과 TCK-7 한 줄이면 성공입니다. 출력이 다르면 이 실습 바로 하단 바의 ‘정답 보기’와 비교합니다.

## 실습 3-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 등급의 기한을 읽어 저장 (①) | `sla_minutes = sla_table[alert["grade"]]` |
| 더해서 저장 (②) | `sla_due = alert["minute"] + sla_minutes` |
| 문자열 이어 붙이기 | `"[" + grade + "] " + entity` |
| 키가 없으면 기본값을 주며 읽기 | `next_steps.get(status, DEFAULT_NEXT_STEP)` |
| 문자열 안에 있으면 | `if "확인 실패" in text:` |
| 함수 결과를 변수에 저장 | `ticket = make_ticket(alert, ticket_no, rules, NEXT_STEPS)` |
| 1 늘려 다시 저장 | `manual_count = manual_count + 1` |

---

## 핵심 코드와 결과를 저장소에 반영하기

핵심 실습에서 만든 코드와 입력 데이터를 저장소에 남깁니다. 선택 과제용 함수는 이 단계에서 만들지 않습니다.

1. **[터미널]** `soar_response` 폴더에서 핵심 파일과 입력 데이터를 확인합니다.
   ```bash
   pwd
   ls
   ls config
   ```
   `undo_actions.py` · `rollback.py` · `exercise3-1_run.py` · `ticketing.py` · `exercise3-2_run.py` · `alerts_thu.json` 와 `config/escalation_rules.json` 이 있어야 합니다.
2. 저장소 루트 `network-study-notes` 로 이동하고, 올릴 변경 목록을 확인합니다.
   ```bash
   cd ..
   git status
   ```
   `.env` 나 실제 비밀값이 보이면 올리지 말고 `.gitignore` 를 먼저 확인합니다.
3. 실행 출력과 최종 상태를 확인한 뒤, 저장소에 반영합니다.
   ```bash
   git add soar_response
   git commit -m "Add SOAR unit 3 core rollback and ticketing"
   git push
   ```

<!-- checklist -->
- [ ] 핵심 코드와 입력 데이터, 실행 결과 기록을 저장소에 올렸다
<!-- /checklist -->
