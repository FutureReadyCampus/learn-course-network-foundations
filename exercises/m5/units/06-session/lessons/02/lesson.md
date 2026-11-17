---
id: m5-u06-l02
title: 실습 6-1 · 티켓 생성과 응답 기한 계산하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/126_day04_am_ticket_notice.md
  mission_id: GichanSource.m5-1112-am-ticket-notice
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 6-1 · 티켓 생성과 응답 기한 계산하기

## 목표: 티켓과 응답 기한

> **오늘 들어온 일**
>
> - **상황**: <mark style="background:#e0d4ff">Unit 5까지 만든 흐름은 조치를 실행한 뒤</mark> 「조치 완료」라는 기록 한 줄만 남겼습니다. 이번 Unit의 근무 3시간 동안 알림 11건이 수신됩니다. `INC-201` 은 퇴사한 `dami` 의 계정을 잠그는 조치를 했습니다. `INC-207` 은 IP `203.0.113.250` 의 차단을 시도했습니다. 조치 뒤에 실제 상태를 다시 조회해 확인하는 일을 사후 검증이라고 합니다. <mark style="background:#ffc4d6">사후 검증에서 실제로는 차단되지 않은 것으로 확인됐습니다</mark>.
> - **문제**: 기록 한 줄만으로는 담당자가 네 가지를 알 수 없습니다. 어떤 사건인지, 이미 어떤 조치를 했는지, 이어서 무엇을 해야 하는지, 언제까지 응답해야 하는지입니다. 또한 사후 검증에 실패한 `INC-207` 이 정상 조치된 알림과 구별되지 않습니다. 그래서 후속 확인이 누락되고, 차단되지 않은 IP 가 그대로 남습니다.
> - **부탁**: 알림이 수신되면 <mark>제목 · 조치 내역 · 후속 조치 · 응답 기한(SLA)을 기재한 티켓을 자동으로 생성해 주세요</mark>. 티켓은 사건 한 건의 처리 상태를 적어 두는 기록입니다. 응답 기한(SLA)은 알림을 수신한 뒤 담당자가 몇 분 안에 응답해야 하는지 정한 기한입니다. 사후 검증에 실패한 건은 담당자가 직접 확인하도록 표시해 주세요.
> - **바뀌는 점**: 담당자는 티켓만 읽고 바로 대응을 시작할 수 있습니다. 예를 들어 `INC-201` 은 high 등급이라 티켓에 응답 기한 15분이 적힙니다. 오늘 샘플에서는 `INC-207` 한 건이 「직접 확인」 대상으로 별도 표시됩니다. 상황과 이름은 설명을 위한 예시입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 1.1 티켓은 담당자의 네 가지 질문 「사건 개요 · 이미 수행한 조치 · 후속 조치 · 응답 기한」에 답해야 한다

**티켓**(ticket)은 사건 한 건의 처리 상태 · 담당자 · 조치 이력을 추적하는 기록입니다. Unit 1에서는 `id` · `incident` · `target` 세 가지만 담긴 간단한 티켓을 만들었습니다. 알림으로 티켓을 생성해 등록하는 일을 **티케팅**(ticketing)이라고 합니다. 오늘은 티켓에 어떤 정보를 기재할지 정합니다. 담당자는 티켓을 열면 아래 네 가지를 확인하려 합니다.

| 담당자의 질문 | 티켓의 키 | 값을 정하는 방법 |
|---|---|---|
| 무슨 일인가 | `title` | 등급 · 대상 · 탐지 규칙을 이어 붙여 제목을 만든다 (1번). 예: `[high] dami — 퇴사한 계정` |
| 이미 무엇을 했나 | `done` | 알림에 기재된 조치 내역을 그대로 복사한다 |
| 다음에 무엇을 하나 | `next_step` | 알림 상태별로 정해 둔 후속 조치 문장을 선택한다 (2번). 사후 검증에 실패했으면 직접 확인을 지시하는 문장으로 교체한다 (3 · 4번) |
| 언제까지 응답하나 | `sla_due` | <mark style="background:#ffdcb0">알림 수신 시각 + 등급별 응답 기한</mark> (5 · 6번). 예: 0분 + 15분 = 15분 |

- **응답 기한**(SLA, Service Level Agreement, 에스엘에이: 서비스 수준 협약)은 알림을 수신한 뒤 담당자가 응답해야 하는 시간의 약속입니다. `escalation_rules.json` 의 `sla_minutes` 에 등급별로 정의되어 있으며, <mark style="background:#ffdcb0">high 는 15분, mid 는 60분, low 는 240분</mark>입니다. 응답 기한은 시간의 길이입니다. 티켓의 `sla_due` 에 적는 **응답 기한 시각**은 알림 수신 시각에 응답 기한을 더한 값입니다.
  - 예를 들어 `INC-201` 은 0분에 수신된 high 알림이라 15분 안에 응답해야 합니다. 그래서 TCK-1 의 응답 기한 시각은 0 + 15 = 15분입니다.
  - `INC-202` 는 3분에 수신된 low 알림이라, TCK-2 의 응답 기한 시각은 3 + 240 = 243분입니다.
- 알림 상태(`status`)는 `조치됨`(자동 조치 완료) · `승인 대기`(담당자의 승인을 기다리는 중) · `조치 없음`(자동 조치 대상 아님) 세 가지입니다. 상태별로 담당자가 수행할 후속 조치가 다르므로, 후속 조치 문장(`next_step`)도 상태별로 따로 정의합니다.
- `done` 문장 끝에 「(확인 실패)」가 붙은 조치가 있습니다. 조치는 실행했지만, 사후 검증에서 실제 상태가 바뀌지 않은 것으로 확인된 조치라는 뜻입니다. 예를 들어 `INC-207` 의 `IP 차단: 차단되지 않음 → 차단되지 않음 (확인 실패)` 가 그렇습니다. <mark style="background:#e0d4ff">Unit 4에서 구현한 조치 후 확인(사후 검증)</mark>이 이 결과를 기록합니다. 이런 조치는 담당자가 수동 검증(manual verification: 사람이 실제 상태를 직접 조회해 확인하는 일)으로 직접 확인해야 하므로, 티켓에 별도로 표시합니다.
- 정의되지 않은 상태가 입력될 수 있습니다. 그래도 프로그램이 중단되지 않도록, 딕셔너리에서 키가 없을 때 기본값을 리턴하는 `.get(키, 기본값)` 을 사용합니다(Unit 4에서 배웠습니다).

함수 네 개와 실행 파일에서 직접 쓰는 곳은 **아홉 군데**입니다.

```
ticketing.py   make_title         : 등급 · 대상 · 규칙으로 티켓 제목을 만든다 (1번)
               find_next_step     : 알림 상태에 맞는 다음 할 일 문장을 고른다 (2번)
               has_failed_action  : 조치 내역에 「확인 실패」가 있는지 확인한다 (3 · 4번)
               make_ticket        : 응답 기한을 계산해 티켓 한 장을 만든다 (5 · 6번)
실행 파일      exercise6-1_run.py   : 알림마다 티켓을 만들고 (7번), 리스트에 모으고 (8번), 직접 확인이 필요한 티켓 수를 센다 (9번)
```

> **여기부터 문제입니다.**

## 실습 6-1 · 티켓 생성과 응답 기한 계산하기

**이런 상황이 있습니다**

- **지금은**: <mark>알림 11건에는 조치 기록만 있고, 담당자의 후속 조치와 응답 기한이 기재되어 있지 않습니다</mark>.
- **만드는 것**: 제목 · 후속 조치 · 수동 확인 표시 · 응답 기한(SLA)을 기재한 티켓을 생성하는 코드(`ticketing.py`)와, 알림마다 티켓을 생성해 리스트에 저장하는 코드(`exercise6-1_run.py`)입니다.
- **실행하면**: <mark>단계 1: 불러온 알림 수, 단계 2: 알림마다 만든 티켓, 단계 3: 티켓 본문 예, 단계 4: 직접 확인이 필요한 티켓이 나옵니다.</mark>

**할 일**: 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 ~ 4 를 읽습니다.

**`ticketing.py`** — 알림으로 티켓을 생성합니다. 실습 6-2 · 실습 6-3도 가져와 사용(import)합니다. 직접 쓰는 곳은 1 ~ 6번입니다.

```python
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
    grade = alert["grade"]                                                              # 알림 등급 — 미리 채운 줄
    entity = alert["entity"]                                                            # 알림 대상(사용자 이름 또는 IP) — 미리 채운 줄
    rule = alert["rule"]                                                                # 탐지된 규칙 이름 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. "[" + grade + "] " + entity + " — " + rule 을 이어 붙인 문자열를 리턴한다


def find_next_step(alert, next_steps):                                                  # 알림 한 건과 다음 할 일 딕셔너리를 받는 함수
    """알림 상태에 맞는 다음 할 일 문장을 리턴한다. 정해 둔 문장이 없으면 기본 문장을 리턴한다.
    담당자가 티켓을 열자마자 무엇부터 할지 알게 할 때 쓴다.
    """
    status = alert["status"]                                                            # 알림 상태(조치됨 · 승인 대기 · 조치 없음) — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. next_steps.get(status, DEFAULT_NEXT_STEP) 의 결과를 리턴한다 (키가 없으면 기본 문장)


def has_failed_action(done_list):                                                       # 조치 내역 문장 리스트를 받는 함수
    """조치 내역에 「확인 실패」가 들어 있는 문장이 하나라도 있으면 True, 없으면 False 를 리턴한다.
    조치했다고 했지만 실제로 바뀌지 않은 알림을 사람이 직접 보게 할 때 쓴다.
    """
    for text in done_list:                                                              # 조치 내역 문장을 하나씩 읽는다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 3. text 안에 "확인 실패" 가 들어 있으면 (if, in)
            # 4. True 를 리턴한다
    return False                                                                        # 하나도 없으면 False 를 리턴한다 — 미리 채운 줄


def make_ticket(alert, ticket_no, rules, next_steps):                                   # 알림 · 티켓 번호 · 규칙 · 다음 할 일 딕셔너리를 받는 함수
    """알림 한 건으로 티켓 한 장(딕셔너리)을 만들어 리턴한다. 만든 시각과 응답 기한(SLA)을 함께 적는다.
    알림이 오면 바로 담당자가 읽을 수 있는 티켓을 만들 때 쓴다.
    """
    sla_table = rules["sla_minutes"]                                                    # 등급마다 정한 응답 기한(분) 표 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. sla_table[alert["grade"]] 를 sla_minutes 에 저장한다 (이 알림 등급의 응답 기한)
    # 6. alert["minute"] + sla_minutes 를 sla_due 에 저장한다 (응답해야 하는 시각)
    needs_manual = has_failed_action(alert["done"])                                     # 조치 확인에 실패한 내역이 있는지 — 미리 채운 줄
    next_step = find_next_step(alert, next_steps)                                       # 다음 할 일 문장 — 미리 채운 줄
    if needs_manual:                                                                    # 확인 실패가 있으면 — 미리 채운 줄
        next_step = MANUAL_STEP                                                         # 직접 확인하라는 문장으로 바꾼다 — 미리 채운 줄
    ticket = {                                                                          # 티켓 한 장 — 미리 채운 줄
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

**`exercise6-1_run.py`** — 7 ~ 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. Unit 1의 `incident.py` 가 같은 폴더에 있어야 합니다.

```python
from incident import load_json                                                                # Unit 1 파일의 JSON 읽기 함수를 불러온다
from ticketing import make_ticket, NEXT_STEPS                                                 # 방금 만든 티켓 함수를 불러온다

alerts = load_json("alerts_thu.json")                                                         # 이번 Unit의 알림 파일을 리스트로 읽는다
rules = load_json("config/escalation_rules.json")                                             # 응답 기한 규칙 파일을 딕셔너리로 읽는다
sla_count = len(rules["sla_minutes"])                                                         # 응답 기한을 정한 등급이 몇 개인지 센다
print("--- 단계 1: 불러온 알림", len(alerts), "건 · 응답 기한을 정한 등급", sla_count, "개")  # 단계 1 시작을 알리는 줄

tickets = []                                                                                  # 만든 티켓을 저장할 빈 리스트
manual_count = 0                                                                              # 직접 확인이 필요한 티켓 수 : 처음에는 0
print("--- 단계 2: 알림마다 만든 티켓")                                                       # 단계 2 시작을 알리는 줄
for alert in alerts:                                                                          # 알림을 하나씩 읽는다
    ticket_no = len(tickets) + 1                                                              # 티켓 번호는 지금까지 만든 수 + 1
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. make_ticket(alert, ticket_no, rules, NEXT_STEPS) 의 결과를 ticket 에 저장한다
    # 8. tickets 리스트에 ticket 을 추가한다 (append)
    print(ticket["id"], ticket["title"], "· 만든 시각", ticket["created_at"], "분 · 기한", ticket["sla_due"], "분")  # 티켓 한 줄을 출력한다
    if ticket["needs_manual"]:                                                                # 직접 확인이 필요하면
        # 9. manual_count 에 manual_count + 1 을 저장한다 (1 늘린다)

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

**순서**

1. **[터미널]** 파일 두 개를 만들고 **[VS Code]** 에서 열어 붙여 넣습니다.
   ```bash
   pwd
   touch ticketing.py exercise6-1_run.py
   ls
   ```
2. **[VS Code]** `ticketing.py` 1 ~ 6번, `exercise6-1_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「실습 6-1 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise6-1_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다. 단계 2 는 11줄, 단계 3 은 6줄, 단계 4 는 숫자가 제목 줄에 함께 나오고 그 아래 1줄입니다.
5. **[보고서]** Unit 6 의 `## 실습 6-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣어 주세요. 그리고 단계 4 에 나온 직접 확인이 필요한 티켓 번호를 적어 주세요. 마지막으로 응답 기한 시각(담당자가 응답해야 하는 시각)이 가장 이른 티켓 번호를 적어 주세요.
   - (나) [핵심 질문] `INC-207` 은 상태가 `조치됨` 인데, 티켓의 후속 조치(`next_step`)는 「조치됨」용 문장이 아닙니다. `done` 의 문장을 근거로 그 사유를 적어 주세요. 그다음 이 표시가 없으면 담당자가 무엇을 놓칠 수 있는지 적어 주세요.
   - (다) [핵심 질문] TCK-1 의 응답 기한 시각은 15분이고 TCK-2 는 243분입니다. 두 티켓의 등급과 만든 시각을 근거로 응답 기한 시각을 계산하는 방법을 적어 주세요. 그다음 모든 티켓에 같은 응답 기한을 적용하면 어떤 문제가 생기는지 적어 주세요.

## 실습 6-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 문자열 이어 붙이기 | `"[" + grade + "] " + entity` |
| 키가 없으면 기본값을 주며 읽기 | `next_steps.get(status, DEFAULT_NEXT_STEP)` |
| 문자열 안에 있으면 | `if "확인 실패" in text:` |
| 딕셔너리에서 값을 읽어 변수에 저장 | `sla_minutes = sla_table[alert["grade"]]` |
| 더해서 변수에 저장 | `sla_due = alert["minute"] + sla_minutes` |
| 함수 결과를 변수에 저장 | `ticket = make_ticket(alert, ticket_no, rules, NEXT_STEPS)` |
| 1 늘려 다시 저장 | `manual_count = manual_count + 1` |

---
