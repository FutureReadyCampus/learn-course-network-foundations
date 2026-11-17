---
id: m5-u06-l04
title: Exercise 6-3 · 등급별 수신자에게 알림을 전파하고, 전송 간격을 제한해 알림 피로를 줄이며, 실패하면 재시도하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/126_day04_am_ticket_notice.md
  mission_id: GichanSource.m5-1112-am-ticket-notice
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 6-3 · 등급별 수신자에게 알림을 전파하고, 전송 간격을 제한해 알림 피로를 줄이며, 실패하면 재시도하기

## 개요

> **오늘 들어온 일**
>
> - **상황**: 티켓을 생성해도 담당자에게는 별도로 통지되지 않습니다. 그래서 담당자는 티켓 목록을 직접 조회하기 전에는 새 티켓이 생성된 것을 알 수 없습니다. 따라서 티켓을 생성하거나 병합할 때마다 담당자에게 알림을 보내야 합니다. 관제 팀은 알림 서버로 담당자에게 알림을 전달합니다. <mark style="background:#e0d4ff">1과목에서 만든 `notifier.py` 의 `notify` 함수가 메시지를 그 알림 서버로 전송합니다</mark>.
> - **문제**: 두 가지입니다.
> - 병합된 알림마다 메시지를 전송하면 같은 알림이 반복해서 전달됩니다. 예를 들어 퇴사한 `dami` 계정 하나 때문에 TCK-1 알림이 네 번 전달됩니다. 그러면 담당자가 알림을 무시하게 됩니다. 이를 알림 피로(alert fatigue: 알림이 너무 많아 중요한 알림에도 반응이 둔해지는 현상)라고 합니다.
> - 알림 서버가 일시적으로 응답하지 않으면 알림이 전달되지 않습니다. 이때 프로그램이 다시 전송하지 않으면, 담당자는 사건이 발생한 사실조차 알지 못합니다.
> - **부탁**: 다음 세 가지를 만들어 주세요.
> - 등급별로 수신자를 정해 주세요.
> - 같은 티켓에 새 알림이 병합됐을 때는 <mark style="background:#ffdcb0">마지막으로 알린 후 30분이 지난 경우에만 다시 알려 주세요</mark>.
> - 알림 서버 전송이 실패하면 최대 3번까지 재시도(실패한 전송을 다시 시도하는 일)해 주세요.
> - **바뀌는 점**: <mark style="background:#bde3ff">알림 11건 가운데 9건은 담당자에게 전송하고, 2건은 전송을 생략합니다</mark>(출력에서는 `건너뜀`). 생략하는 알림은 `INC-205` 와 `INC-206` 입니다. 예를 들어 `INC-205` 는 TCK-1 에 마지막으로 알린 0분에서 14분이 지났고 30분보다 짧으므로 건너뜁니다. `INC-209` 는 40분이 지나 30분 이상이므로 전송합니다. high 는 `team.lead`(팀장)까지 3명에게, low 는 `kim.sec` 한 명에게만 전달됩니다. 3번 모두 실패한 알림은 「실패」로 표시됩니다(실패 기록을 파일에 저장하는 기능은 이 수업에 없습니다). 상황과 숫자는 설명을 위한 예시입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 읽기 · 3.1 알림 전파는 「수신자 · 전송 간격 · 실패 시 재시도」를 정해야 운영할 수 있다

알림 전파에서는 세 가지를 정해야 합니다. <mark>누구에게 보낼지, 얼마나 자주 보낼지, 실패하면 어떻게 할지</mark>입니다. 오늘 적용한 정책은 아래 표와 같습니다.

| 정할 것 | 오늘 적용한 정책 | 규칙 파일의 키 |
|---|---|---|
| 누구에게 | 등급별로 수신자 리스트가 다르다. <mark style="background:#ffdcb0">high 는 `kim.sec` · `lee.soc` · `team.lead`, mid 는 `kim.sec` · `lee.soc`, low 는 `kim.sec`</mark> | `recipients` |
| 얼마나 자주 | 처음 전송하는 알림은 즉시 전송한다. 같은 티켓은 마지막 전송 후 30분이 지나야 다시 전송한다 | `send_gap_minutes` |
| 실패하면 | 실패하면 다시 보내 보며, 처음 전송을 포함해 최대 3번 시도한다. 3번 모두 실패하면 「실패」로 처리한다 | `ticket_notice.py` 의 `MAX_TRIES` |

- 알림이 너무 많아 담당자가 알림을 무시하게 되는 현상을 **알림 피로**(alert fatigue, 얼럿 퍼티그)라고 합니다. 이 문제를 줄이는 방법 가운데 하나가 같은 티켓에 알림을 전송하는 사이에 최소 간격을 두는 것입니다. 예를 들어 `dami` 의 알림 네 건이 TCK-1 에 병합되지만, 30분 간격 때문에 담당자에게는 <mark style="background:#bde3ff">`INC-201` · `INC-209` · `INC-210` 세 번만 전송됩니다</mark>.
- 1과목의 `notify(message, url)` 는 메시지를 알림 서버 주소(`url`)로 전송합니다. 성공하면 `True` 를 리턴합니다. 실패하면 `[알림 실패]` 와 오류 이름을 출력하고 `False` 를 리턴합니다. `ConnectionError`(연결 오류)는 서버에 연결하지 못했을 때 발생하는 오류 이름입니다.
- `notify` 는 서버에 요청을 전송하기만 하면 `True` 를 리턴합니다. <mark style="background:#ffc4d6">서버가 반환한 HTTP 응답 코드(예: 200 은 성공)는 확인하지 않습니다</mark>. 실제 제품에서는 응답 코드까지 검증합니다.
- 알림 서버는 1과목에서 만든 `alert_server.py` 입니다. 터미널 하나에서 실행해 두면, 알림이 수신될 때마다 그 터미널에 `[알림 받음]` 과 메시지가 출력됩니다. 주소는 `alert_url` 입니다. 이 서버는 요청을 수신하는 번호인 5001번 포트(port, 포트)를 사용합니다.
- 메시지는 `[등급] 대상 — 규칙 · 티켓 번호 · 알림 N건 · 기한 M분 · 수신: 이름들` 모양입니다.
- 전송이 모두 실패했을 때의 대응은 보고서 (다)에서 다룹니다.

함수 네 개와 실행 파일에서 직접 쓰는 곳은 **아홉 군데**입니다.

```
ticket_notice.py   pick_recipients     : 등급에 맞는 수신자 리스트를 고른다 (1번)
                   should_send         : 지금 알려도 되는지 정한다. 처음이거나 간격이 지났으면 True (2 ~ 4번)
                   send_with_retry     : 최대 3번 보내 보고, 성공한 시도 번호를 리턴한다. 모두 실패하면 0 (5 · 6번)
                   send_ticket_notice  : 위 세 함수로 티켓 알림을 보내고 「전송」 · 「건너뜀」 · 「실패」를 리턴한다 (미리 채움)
실행 파일          day04_4-1_run.py    : 알림마다 티켓 알림을 보내고 (7번), 보냈으면 센다 (8 · 9번)
```

> **여기부터 문제입니다.**

## Exercise Exercise 5-3 · 등급별 수신자에게 알림을 전파하고, 전송 간격을 제한해 알림 피로를 줄이며, 실패하면 재시도하기

** 이런 상황이 있습니다**

- **지금은**: <mark>티켓은 생성되지만 담당자에게 알림을 전파하는 단계가 없습니다. 그래서 담당자가 티켓 목록을 직접 조회하기 전에는 새 티켓이 생성된 것을 알 수 없습니다</mark>.
- **만드는 것**: 수신자 선택 · 전송 여부 판정 · 최대 3번 재시도 전송(`ticket_notice.py`), 알림마다 담당자에게 알림을 전파하고 집계한 결과(`day04_4-1_run.py`).
- **실행하면**: <mark>단계 1: 알림 11건의 처리와 담당자 알리기 결과, 단계 2: 전송과 건너뜀 건수 · 티켓별 알린 횟수, 단계 3: 꺼진 주소로 3번 보내 보기, 단계 4: 저장한 티켓이 나옵니다.</mark>

** 할 일**: 알림 서버를 켜고, 파일 두 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 1 ~ 3 과 서버 터미널을 읽습니다.

**`ticket_notice.py`** — 담당자에게 알림을 전파합니다. 직접 쓰는 곳은 1 ~ 6번입니다. Exercise 6-2의 `ticket_merge.py` 와 1과목에서 복사한 `notifier.py` 가 같은 폴더에 있어야 합니다.

```python
from notifier import notify                                            # 1과목 notifier.py 의 알림 함수를 불러온다 (성공하면 True, 실패하면 False)

MAX_TRIES = 3                                                          # 알림을 보내 보는 최대 횟수


def pick_recipients(grade, rules):                                     # 등급과 규칙을 받는 함수
    """등급에 맞는 수신자 이름 리스트를 리턴한다.
    위험한 알림일수록 더 많은 사람에게 알려야 할 때 쓴다.
    """
    table = rules["recipients"]                                        # 등급마다 정한 수신자 표 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. table[grade] 를 리턴한다 (이 등급의 수신자 리스트)


def should_send(ticket, now, gap):                                     # 티켓 · 지금 시각(분) · 알림 간격(분)을 받는 함수
    """이 티켓의 알림을 지금 보내도 되면 True, 너무 일러서 건너뛰어야 하면 False 를 리턴한다.
    같은 티켓의 알림이 연달아 가서 사람이 알림을 무시하게 되는 일을 막을 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. ticket 의 "notified_count" 가 0 이면 (if, ==) 처음 보내는 것이다
    # 3.   True 를 리턴한다
    elapsed = now - ticket["last_notified"]                            # 마지막으로 보낸 뒤 몇 분 지났는지 — 미리 채운 줄
    # 4. elapsed 가 gap 이상인지(>=)의 결과를 리턴한다


def send_with_retry(message, url, max_tries):                          # 메시지 · 알림 주소 · 최대 횟수를 받는 함수
    """알림을 최대 max_tries 번 보내 본다. 성공한 시도 번호를, 모두 실패하면 0 을 리턴한다.
    알림 서버가 잠깐 응답하지 않을 때 바로 포기하지 않고 다시 보내 보려고 쓴다.
    """
    for attempt in range(1, max_tries + 1):                            # 시도 번호를 1 부터 최대 횟수까지 하나씩 읽는다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. notify(message, url) 의 결과가 참이면 (if)
            # 6. attempt 를 리턴한다
    return 0                                                           # 모두 실패했으면 0 을 리턴한다 — 미리 채운 줄


def send_ticket_notice(ticket, now, rules):                            # 티켓 · 지금 시각(분) · 규칙을 받는 함수
    """티켓 알림을 보낼지 정하고, 보내야 하면 수신자를 붙여 보낸다. 「전송」 · 「건너뜀」 · 「실패」 중 하나를 리턴한다.
    티켓이 만들어지거나 합쳐질 때마다 부른다.
    """
    if not should_send(ticket, now, rules["send_gap_minutes"]):        # 너무 일러서 보내면 안 되면
        return "건너뜀"                                                # 보내지 않고 「건너뜀」을 리턴한다
    recipients = pick_recipients(ticket["grade"], rules)               # 이 등급의 수신자 리스트를 구한다
    names = ""                                                         # 수신자 이름을 이어 붙일 빈 문자열
    for name in recipients:                                            # 수신자를 하나씩 읽는다
        if names != "":                                                # 이미 이름이 있으면
            names = names + ", "                                       # 쉼표를 붙이고
        names = names + name                                           # 이름을 이어 붙인다
    message = ticket["title"] + " · " + ticket["id"] + " · 알림 " + str(ticket["count"]) + "건 · 기한 " + str(ticket["sla_due"]) + "분 · 수신: " + names  # 알림 내용을 만든다
    attempt = send_with_retry(message, rules["alert_url"], MAX_TRIES)  # 최대 3번까지 보내 본다
    if attempt == 0:                                                   # 모두 실패했으면
        return "실패"                                                  # 「실패」를 리턴한다
    ticket["notified_count"] = ticket["notified_count"] + 1            # 보낸 횟수를 1 늘린다
    ticket["last_notified"] = now                                      # 마지막으로 보낸 시각을 적는다
    return "전송"                                                      # 「전송」을 리턴한다
```

**`day04_4-1_run.py`** — 7 ~ 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 7번 아래에는 `result = …` 를 씁니다. 8번 아래에는 `if … :` 를 씁니다. 9번 아래에는 한 단계 들여쓴 줄을 씁니다.

```python
from incident import load_json, save_json                                             # 월요일 파일의 JSON 읽기 · 저장 함수를 불러온다
from ticket_merge import handle_alert                                                 # Exercise 6-2에 만든 알림 처리 함수를 불러온다
from ticket_notice import send_ticket_notice, send_with_retry, MAX_TRIES              # 방금 만든 알림 함수를 불러온다

alerts = load_json("alerts_thu.json")                                                 # 오늘 오전 알림 파일을 읽는다
rules = load_json("config/escalation_rules.json")                                     # 규칙 파일을 읽는다
tickets = []                                                                          # 만든 티켓을 저장할 빈 리스트
sent_count = 0                                                                        # 알림을 보낸 수 : 처음에는 0
skipped_count = 0                                                                     # 건너뛴 수 : 처음에는 0

print("--- 단계 1: 알림", len(alerts), "건 처리와 담당자 알리기")                     # 단계 1 시작을 알리는 줄과 개수
for alert in alerts:                                                                  # 알림을 하나씩 읽는다
    ticket, action = handle_alert(alert, tickets, rules)                              # 알림을 처리하고 티켓과 처리 방식을 받는다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. send_ticket_notice(ticket, alert["minute"], rules) 의 결과를 result 에 저장한다
    print(alert["id"], "->", ticket["id"], action, "· 담당자 알리기:", result)        # 알림 한 건의 결과를 출력한다
    # 8. result 가 "전송" 이면 (if, ==)
        # 9. sent_count 에 sent_count + 1 을 저장한다 (1 늘린다)
    if result == "건너뜀":                                                            # 건너뛰었으면 — 미리 채운 줄
        skipped_count = skipped_count + 1                                             # 건너뛴 수를 1 늘린다 — 미리 채운 줄

print("--- 단계 2: 담당자에게 전송", sent_count, "건 · 건너뜀", skipped_count, "건")  # 단계 2 시작을 알리는 줄과 건수
for ticket in tickets:                                                                # 티켓을 하나씩 읽는다
    print(ticket["id"], "담당자에게 알린 횟수", ticket["notified_count"], "번 · 마지막으로 알린 시각", ticket["last_notified"], "분")  # 티켓별 전송 횟수를 출력한다

url_off = "http://127.0.0.1:5999/alert"                                               # 아무 서버도 없는 주소 — 알림 서버가 꺼진 상황
print("--- 단계 3: 꺼진 주소로 최대", MAX_TRIES, "번 보내 보기")                      # 단계 3 시작을 알리는 줄
attempt = send_with_retry("[테스트] 꺼진 알림 서버", url_off, MAX_TRIES)              # 꺼진 주소로 보내 본다
print("성공한 시도 번호:", attempt, "(0 은 모두 실패)")                               # 시도 결과를 출력한다

save_json(tickets, "tickets_day4.json")                                               # 티켓을 파일에 저장한다
saved = load_json("tickets_day4.json")                                                # 저장한 파일을 다시 읽는다
print("--- 단계 4: 파일에 저장된 티켓", len(saved), "장")                             # 단계 4 시작을 알리는 줄과 장수
```

**순서**

1. **[터미널]** 알림 서버를 켭니다. 먼저 VS Code 터미널 창 오른쪽 위의 `+` 로 **새 터미널**을 하나 더 엽니다. 그 터미널에서 위치를 확인한 뒤 서버를 켭니다(맥북은 `python3`). <mark style="background:#bde3ff">`Running on http://127.0.0.1:5001` 이 보이면</mark> 됩니다. 이 터미널은 그대로 두고 쓰지 않습니다.
   ```bash
   pwd
   python alert_server.py
   ```
   - `pwd` 결과가 `soar_response` 로 끝나지 않으면 `cd soar_response` 를 먼저 입력합니다. 새 터미널이 다른 폴더에서 열릴 수 있습니다.
2. **[터미널]** 처음 쓰던 터미널로 돌아와 파일 두 개를 만들고 **[VS Code]** 에서 열어 붙여 넣습니다.
   ```bash
   pwd
   touch ticket_notice.py day04_4-1_run.py
   ls
   ```
3. **[VS Code]** `ticket_notice.py` 1 ~ 6번, `day04_4-1_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「Exercise 6-3 한눈에」를 봅니다.
4. **[터미널]** 처음 쓰던 터미널에서 <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python day04_4-1_run.py
   ```
5. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 11줄, 단계 2 는 숫자가 제목 줄에 함께 나오고 그 아래 티켓 7줄, 단계 3 은 `[알림 실패] ConnectionError` 3줄과 결과 1줄(재시도를 확인하는 시험입니다), 단계 4 는 숫자가 제목 줄에 함께 나오고 그 아래 줄이 없습니다. <mark style="background:#bde3ff">알림 서버 터미널에는 `[알림 받음]` 줄이 9개 출력됩니다.</mark>
6. **[터미널]** 알림 서버 터미널을 `Ctrl + C` 로 끕니다.
7. **[보고서]** `day04_am_report.md` 의 `## Exercise 6-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 알림 서버 터미널에 출력된 `[알림 받음]` 줄 수와, 단계 2 의 전송 건수 · 건너뜀 건수를 적어 주세요.
   - (나) [핵심 질문] `INC-205` 와 `INC-206` 은 전송을 생략했고 `INC-209` 와 `INC-210` 은 전송했습니다. 각각 전송을 생략한 사유와 전송한 사유를 적어 주세요. 근거는 각 알림이 수신된 시각과 해당 티켓의 마지막 전송 시각입니다. 그다음 전송 간격을 제한하지 않으면 담당자에게 어떤 일이 생기는지 적어 주세요.
   - (다) [핵심 질문] 단계 3 에서 꺼진 주소로 3번 전송을 시도했고 모두 실패했습니다. `[알림 실패] ConnectionError`(연결 오류: 서버에 연결하지 못했을 때 발생하는 오류 이름)가 3번 출력된 사유를 적어 주세요. 그다음 3번 모두 실패한 알림이 누락되지 않게 하려면, 실제 관제에서 무엇을 추가로 해야 하는지 적어 주세요.

## Exercise 6-3 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 딕셔너리에서 값을 읽어 리턴 | `return table[grade]` |
| 같으면 | `if ticket["notified_count"] == 0:` |
| 이상인지의 결과 리턴 | `return elapsed >= gap` |
| 함수 결과가 참이면 | `if notify(message, url):` |
| 번호를 1 부터 하나씩 읽기 | `for attempt in range(1, max_tries + 1):` |
| 함수 결과를 변수에 저장 | `result = send_ticket_notice(ticket, alert["minute"], rules)` |
| 1 늘려 다시 저장 | `sent_count = sent_count + 1` |

---

## 오늘 오전 마무리

| 확인 | 문제 |
|---|---|
| 알림으로 티켓을 생성하고 응답 기한(SLA)을 계산했으며, 조치 확인에 실패한 건을 수동 확인 대상으로 표시했다 | 오전 Exercise 6-1 |
| 같은 사건의 알림을 티켓 한 장으로 병합(중복 제거)하고 허용된 순서로 상태를 전이했다 | 오전 Exercise 6-2 |
| 등급별 수신자에게 알림을 전파하고, 전송 간격을 제한했으며, 실패하면 최대 3번 재시도했다 | 오전 Exercise 6-3 |

오전에 구현한 티켓 생성 · 병합 · 알림 전파는 오후로 이어집니다. <mark>오후에는 응답 기한이 지나도 아무도 확인하지 않은 티켓을 상급자에게 올리는 에스컬레이션(escalation)을 구현합니다. 그리고 오전부터 만든 것을 가상 근무 시간 동안 한 번에 실행합니다.</mark>

---

---

<!-- learn:answers -->
