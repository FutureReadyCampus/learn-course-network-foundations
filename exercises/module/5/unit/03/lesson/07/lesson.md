---
id: m5-u03-l07
title: 응용 3-3 · 등급별 알림 전파와 재시도 만들기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/126_day04_am_ticket_notice.md
  mission_id: GichanSource.m5-1112-am-ticket-notice
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 응용 3-3 · 등급별 알림 전파와 재시도 만들기

## 목표: 알림 전파와 재시도

> **여유가 되면 해 보세요.** 핵심 실습 3-1 · 3-2와 글쓰기를 먼저 마칩니다. 이 응용에서는 「제공 파일」 레슨에서 완성본으로 받은 `ticket_notice.py` 를 직접 써 봅니다. 알림 서버를 켜야 해서 `flask` · `requests` 도구를 설치합니다(순서 1번). 응용 3-2는 하지 않아도 되고, 그때는 제공 파일의 `ticket_merge.py` 를 씁니다.

> **오늘 들어온 일**
>
> - **상황**: 티켓을 생성해도 담당자에게는 별도로 통지되지 않습니다. 그래서 담당자는 티켓 목록을 직접 조회하기 전에는 새 티켓이 생성된 것을 알 수 없습니다. 따라서 티켓을 생성하거나 병합할 때마다 담당자에게 알림을 보내야 합니다. 관제 팀은 알림 서버로 담당자에게 알림을 전달합니다. <mark style="background:#e0d4ff">`notifier.py` 의 `notify` 함수가 메시지를 그 알림 서버로 전송합니다</mark>.
> - **문제**: 두 가지입니다.
> - 병합된 알림마다 메시지를 전송하면 같은 알림이 반복해서 전달됩니다. 예를 들어 퇴사한 `dami` 계정 하나 때문에 TCK-1 알림이 네 번 전달됩니다. 그러면 담당자가 알림을 무시하게 됩니다. 이를 알림 피로(alert fatigue: 알림이 너무 많아 중요한 알림에도 반응이 둔해지는 현상)라고 합니다.
> - 알림 서버가 일시적으로 응답하지 않으면 알림이 전달되지 않습니다. 이때 프로그램이 다시 전송하지 않으면, 담당자는 사건이 발생한 사실조차 알지 못합니다.
> - **부탁**: 다음 세 가지를 만들어 주세요.
> - 등급별로 수신자를 정해 주세요.
> - 같은 티켓에 새 알림이 병합됐을 때는 <mark style="background:#ffdcb0">마지막으로 알린 후 30분이 지난 경우에만 다시 알려 주세요</mark>.
> - 알림 서버 전송이 실패하면 최대 3번까지 재시도(실패한 전송을 다시 시도하는 일)해 주세요.
> - **바뀌는 점**: <mark style="background:#bde3ff">알림 11건 가운데 9건은 담당자에게 전송하고, 2건은 전송을 생략합니다</mark>(출력에서는 `건너뜀`). 생략하는 알림은 `INC-205` 와 `INC-206` 입니다. 예를 들어 `INC-205` 는 TCK-1 에 마지막으로 알린 0분에서 14분이 지났고 30분보다 짧으므로 건너뜁니다. `INC-209` 는 40분이 지나 30분 이상이므로 전송합니다. high 는 `team.lead`(팀장)까지 3명에게 전달되고, low 는 `kim.sec` 한 명에게만 전달됩니다. 3번 모두 실패한 알림은 「실패」로 표시됩니다. 실패 기록을 파일에 저장하는 기능은 이 수업에 없습니다. 상황과 숫자는 설명을 위한 예시입니다.

## 3.1 알림 전파는 「수신자 · 전송 간격 · 실패 시 재시도」를 정해야 운영할 수 있다

알림 전파에서는 세 가지를 정해야 합니다. <mark>누구에게 보낼지, 얼마나 자주 보낼지, 실패하면 어떻게 할지</mark>입니다. 오늘 적용한 정책은 아래 표와 같습니다.

| 정할 것 | 오늘 적용한 정책 | 규칙 파일의 키 |
|---|---|---|
| 누구에게 | 등급별로 수신자 리스트가 다르다 | `recipients` |
| 얼마나 자주 | 처음은 즉시, 같은 티켓은 마지막 전송 후 30분이 지나야 다시 | `send_gap_minutes` |
| 실패하면 | 처음 전송을 포함해 최대 3번 시도한다 | `ticket_notice.py` 의 `MAX_TRIES` |

3번 모두 실패하면 「실패」로 처리합니다. 등급별 수신자는 아래와 같습니다.

| 등급 | 수신자 |
|---|---|
| high | <mark style="background:#ffdcb0">`kim.sec` · `lee.soc` · `team.lead`</mark> |
| mid | <mark style="background:#ffdcb0">`kim.sec` · `lee.soc`</mark> |
| low | <mark style="background:#ffdcb0">`kim.sec`</mark> |

- 알림이 너무 많아 담당자가 알림을 무시하게 되는 현상을 **알림 피로**(alert fatigue, 얼럿 퍼티그)라고 합니다. 이 문제를 줄이는 방법 가운데 하나가 같은 티켓에 알림을 전송하는 사이에 최소 간격을 두는 것입니다. 예를 들어 `dami` 의 알림 네 건이 TCK-1 에 병합되지만, 30분 간격 때문에 담당자에게는 <mark style="background:#bde3ff">`INC-201` · `INC-209` · `INC-210` 세 번만 전송됩니다</mark>.
- `notify(message, url)` 는 메시지를 알림 서버 주소(`url`)로 전송합니다. 성공하면 `True` 를 리턴합니다. 실패하면 `[알림 실패]` 와 오류 이름을 출력하고 `False` 를 리턴합니다. `ConnectionError`(연결 오류)는 서버에 연결하지 못했을 때 발생하는 오류 이름입니다.
- `notify` 는 서버에 요청을 전송하기만 하면 `True` 를 리턴합니다. <mark style="background:#ffc4d6">서버가 반환한 HTTP 응답 코드(예: 200 은 성공)는 확인하지 않습니다</mark>. 실제 제품에서는 응답 코드까지 검증합니다.
- 알림 서버는 `alert_server.py` 입니다. 터미널 하나에서 실행해 두면, 알림이 수신될 때마다 그 터미널에 `[알림 받음]` 과 메시지가 출력됩니다. 주소는 `alert_url` 입니다. 이 서버는 요청을 수신하는 번호인 5001번 포트(port, 포트)를 사용합니다.
- 메시지는 `[등급] 대상 — 규칙 · 티켓 번호 · 알림 N건 · 기한 M분 · 수신: 이름들` 모양입니다.
- 전송이 모두 실패했을 때의 대응은 보고서 (다)에서 다룹니다.

**직접 쓰는 곳은 아홉 군데**입니다.

| 파일 | 함수 | 번호 | 하는 일 |
|---|---|---|---|
| `ticket_notice.py` | `pick_recipients` | 1번 | 등급에 맞는 수신자 리스트를 고른다 |
| `ticket_notice.py` | `should_send` | 2 ~ 4번 | 처음이거나 간격이 지났으면 `True` 를 리턴한다 |
| `ticket_notice.py` | `send_with_retry` | 5 · 6번 | 최대 3번 보내 보고, 성공한 시도 번호를 리턴한다 |
| `ticket_notice.py` | `send_ticket_notice` | 미리 채움 | 위 세 함수로 티켓 알림을 보낸다 |
| `apply3-3_run.py` | (실행 파일) | 7번 | 알림마다 티켓 알림을 보낸다 |
| `apply3-3_run.py` | (실행 파일) | 8 · 9번 | 보냈으면 센다 |

- `should_send` 는 지금 알려도 되는지 정합니다. `send_with_retry` 는 모두 실패하면 0 을 리턴합니다.
- `send_ticket_notice` 는 「전송」 · 「건너뜀」 · 「실패」 중 하나를 리턴합니다.

## 응용 3-3 · 등급별 알림 전파와 재시도 만들기

**이런 상황이 있습니다**

- **지금은**: <mark>티켓은 생성되지만 담당자에게 알림을 전파하는 단계가 없습니다. 그래서 담당자가 티켓 목록을 직접 조회하기 전에는 새 티켓이 생성된 것을 알 수 없습니다</mark>.
- **만드는 것**: 수신자 선택 · 전송 여부 판정 · 최대 3번 재시도 전송(`ticket_notice.py`), 알림마다 담당자에게 알림을 전파하고 집계한 결과(`apply3-3_run.py`).
- **실행하면**: <mark>단계 1: 알림 11건의 처리와 담당자 알리기 결과, 단계 2: 전송과 건너뜀 건수 · 티켓별 알린 횟수, 단계 3: 꺼진 주소로 3번 보내 보기, 단계 4: 저장한 티켓이 나옵니다.</mark>

**할 일**: 도구를 설치하고 알림 서버를 켠 뒤, 파일 두 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 1 ~ 4 와 서버 터미널을 읽습니다.

**`alert_server.py`** — 알림 서버입니다. Flask(플라스크)는 파이썬으로 작은 웹 서버를 만드는 도구이고, `requests` 는 그런 서버에 요청을 보내는 도구입니다. `/alert` 로 알림이 오면 터미널에 `[알림 받음]` 과 내용을 보여 줍니다. 쓰는 줄이 없습니다. 이미 있으면 다시 만들지 않습니다(`agent_core` 폴더에 있으면 `cp ../agent_core/alert_server.py .` 로 복사해도 됩니다). Unit 4 응용 4-1 · 4-2에서도 이 서버를 켭니다.

```python
from flask import Flask, request        # 웹 서버를 만드는 Flask 와 요청 정보를 담은 request 를 불러온다

app = Flask(__name__)                   # 서버를 하나 만든다


@app.route("/alert", methods=["POST"])  # /alert 로 POST 가 오면 아래 함수가 받는다
def alert():                            # 알림을 받는 함수
    data = request.get_json()           # 보낸 JSON 을 딕셔너리로 꺼낸다
    print("[알림 받음]", data["text"])  # 터미널에 알림 내용을 보여 준다
    return {"ok": True}                 # 받았다고 답한다 (상태 코드 200)


app.run(port=5001)                      # 5001 번 포트에서 기다린다
```

**`ticket_notice.py`** — 담당자에게 알림을 전파합니다. 직접 쓰는 곳은 1 ~ 6번입니다. 3번은 2번에서 쓴 `if` 의 안쪽이라 주석보다 한 단계 더 오른쪽에, 6번은 이미 한 단계 들어가 있는 주석과 같은 위치에 씁니다. 「제공 파일」 레슨의 `ticket_merge.py`(응용 3-2를 했다면 직접 쓴 파일)와 `notifier.py` 가 같은 폴더에 있어야 합니다. 제공 파일의 완성본이 있으면 그 파일의 내용을 모두 지우고 아래 골격을 붙여 넣은 뒤 씁니다.

```python
from notifier import notify                                            # notifier.py 의 알림 함수를 불러온다 (성공하면 True, 실패하면 False)

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

**`apply3-3_run.py`** — 7 ~ 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 7번 아래에는 `result = …` 를 씁니다. 8번 아래에는 `if … :` 를 씁니다. 9번 아래에는 한 단계 들여쓴 줄을 씁니다.

```python
from incident import load_json, save_json                                             # Unit 1 파일의 JSON 읽기 · 저장 함수를 불러온다
from ticket_merge import handle_alert                                                 # 제공 파일(응용 3-2)의 알림 처리 함수를 불러온다
from ticket_notice import send_ticket_notice, send_with_retry, MAX_TRIES              # 방금 만든 알림 함수를 불러온다

alerts = load_json("alerts_thu.json")                                                 # 오늘의 알림 파일을 읽는다
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

save_json(tickets, "tickets_unit09.json")                                               # 티켓을 파일에 저장한다
saved = load_json("tickets_unit09.json")                                                # 저장한 파일을 다시 읽는다
print("--- 단계 4: 파일에 저장된 티켓", len(saved), "장")                             # 단계 4 시작을 알리는 줄과 장수
```

**순서**

1. **[터미널]** 먼저 알림 서버와 알림 보내기에 쓰는 도구를 설치합니다(맥북은 `python3`). 이미 설치했다면 바로 다음 번호로 갑니다.
   ```bash
   python -m pip install flask requests
   ```
   - 설치 뒤 `python -c "import ticket_notice; print('불러오기 성공')"` 를 치면 `불러오기 성공` 이 나와야 합니다. 「제공 파일」 레슨의 `ticket_notice.py` 와 `notifier.py` 를 확인하는 명령입니다.
2. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `alert_server.py` 를 만들고(이미 있으면 건너뜁니다) 위 코드 상자를 붙여 넣고 저장합니다.
3. **[터미널]** 알림 서버를 켭니다. VS Code 터미널 창 오른쪽 위의 `+` 로 **새 터미널**을 하나 더 엽니다. 그 터미널에서 위치를 확인한 뒤 서버를 켭니다. <mark style="background:#bde3ff">`Running on http://127.0.0.1:5001` 이 보이면</mark> 됩니다. 이 터미널은 그대로 두고 쓰지 않습니다.
   ```bash
   pwd
   python alert_server.py
   ```
   - `pwd` 결과가 `soar_response` 로 끝나지 않으면 `cd soar_response` 를 먼저 입력합니다. 새 터미널이 다른 폴더에서 열릴 수 있습니다.
   - `No module named 'flask'` 가 나오면 새 터미널에서 가상환경이 켜져 있는지 보고, 1번 설치를 이 터미널에서 다시 합니다.
   - `Address already in use` 가 나오면 이미 켜진 서버가 있는 것이니, 그 터미널에서 `Ctrl + C` 로 끄고 다시 켭니다.
4. **[VS Code]** `ticket_notice.py` 와 `apply3-3_run.py` 를 이름 그대로 만들고(이미 있는 `ticket_notice.py` 는 내용을 지우고), 위 코드 상자를 복사해 붙여 넣고 저장합니다.
5. **[VS Code]** `ticket_notice.py` 1 ~ 6번, `apply3-3_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「응용 3-3 정리」를 봅니다.
6. **[터미널]** 처음 쓰던 터미널에서 <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python apply3-3_run.py
   ```
7. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 11줄, 단계 2 는 숫자가 제목 줄에 함께 나오고 그 아래 티켓 7줄, 단계 3 은 `[알림 실패] ConnectionError` 3줄과 결과 1줄(재시도를 확인하는 시험입니다), 단계 4 는 숫자가 제목 줄에 함께 나오고 그 아래 줄이 없습니다. <mark style="background:#bde3ff">알림 서버 터미널에는 `[알림 받음]` 줄이 9개 출력됩니다.</mark>
8. **[터미널]** 알림 서버 터미널을 `Ctrl + C` 로 끕니다.
9. **[보고서]** `report_u3.md` 의 `## 응용 3-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 알림 서버 터미널에 출력된 `[알림 받음]` 줄 수와, 단계 2 의 전송 건수 · 건너뜀 건수를 적어 주세요.
   - (나) [핵심 질문] `INC-205` 와 `INC-206` 은 전송을 생략했고 `INC-209` 와 `INC-210` 은 전송했습니다. 각각 전송을 생략한 사유와 전송한 사유를 적어 주세요. 근거는 각 알림이 수신된 시각과 해당 티켓의 마지막 전송 시각입니다. 그다음 전송 간격을 제한하지 않으면 담당자에게 어떤 일이 생기는지 적어 주세요.
   - (다) [핵심 질문] 단계 3 에서 꺼진 주소로 3번 전송을 시도했고 모두 실패했습니다. `[알림 실패] ConnectionError`(연결 오류: 서버에 연결하지 못했을 때 발생하는 오류 이름)가 3번 출력된 사유를 적어 주세요. 그다음 3번 모두 실패한 알림이 누락되지 않게 하려면, 실제 관제에서 무엇을 추가로 해야 하는지 적어 주세요.

## 응용 3-3 정리

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

## 응용 파일 올리기

응용 3-1 ~ 3-3 가운데 하나라도 했다면 그 파일도 깃허브에 올립니다. 알림 서버는 `Ctrl + C` 로 끈 뒤에 합니다.

1. **[보고서]** 올리기 전에 `report_u3.md` 의 내가 한 응용 칸을 먼저 채웁니다.
2. **[터미널]** 실습 3-2 끝 「이번 Unit 마무리 · 깃허브에 올리기」의 **4. 깃허브에 올리기** 1 ~ 4번을 한 번 더 합니다. 기록 설명은 아래처럼 바꿔 씁니다.
   ```bash
   git add .
   git commit -m "Add SOAR unit 3 apply tasks: shift drill, ticket merge and notice"
   git push
   ```
3. 그 2번에서 `git status` 를 치면 내가 한 응용의 파일이 보입니다.
   1. 응용 3-1: `drill.py` · `shift_report.py` · `apply3-1_run.py` 와 실행이 만든 근무 기록 `shift_log.json`
   2. 응용 3-2: `apply3-2_run.py`(직접 쓴 `ticket_merge.py` 는 바뀐 파일로 보입니다)
   3. 응용 3-3: `alert_server.py` · `apply3-3_run.py` 와 실행이 저장한 티켓 `tickets_unit09.json`(직접 쓴 `ticket_notice.py` 는 바뀐 파일로 보입니다)
4. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `soar_response` 폴더에 위 파일이 보이는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.

다음 Unit 4 응용 4-1은 응용 3-3이 저장한 `tickets_unit09.json` 을 읽습니다. 이 응용을 하지 않았다면 Unit 4 응용 4-1 레슨의 상자로 같은 파일을 만들 수 있습니다.

---
