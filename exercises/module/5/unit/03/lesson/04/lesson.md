---
id: m5-u03-l04
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

이 레슨의 파일은 **실습 3-2를 마친 뒤**, 실습 3-2 끝의 「이번 Unit 마무리 · 깃허브에 올리기」 2번에서 만듭니다. 오늘 핵심 실습에는 쓰지 않지만, 도전 3-2 · 3-3과 Unit 4 도전 4-1 · 4-2가 이 파일을 가져와 사용(import)합니다. 도전을 하지 않아도 완성본을 받아 두면 다음 Unit을 따라갈 수 있습니다.

만들 파일은 세 개입니다.

| 파일 | 담긴 함수 | 하는 일 |
|---|---|---|
| `ticket_merge.py` | `handle_alert` | 같은 사건의 알림을 티켓 한 장으로 병합한다 |
| `ticket_merge.py` | `change_ticket_status` | 티켓 상태를 바꾼다 |
| `notifier.py` | `notify` | 메시지를 알림 서버로 보낸다 |
| `ticket_notice.py` | `send_ticket_notice` | 등급에 맞는 수신자에게 티켓 알림을 보낸다 |
| `ticket_notice.py` | `send_with_retry` | 실패하면 최대 3번까지 다시 보낸다 |

`ticket_merge.py` 는 실습 3-2의 `ticketing.py` 를 가져와 씁니다. `notifier.py` 는 `agent_core` 폴더에 이미 있으면 복사해 씁니다.

1. 파일은 모두 `soar_response` 폴더 안에 만듭니다(VS Code 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File**).
2. 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. `ticket_merge.py` 를 만들었으면 아래 명령으로 확인합니다(맥북은 `python3`). `제공 파일 정상 7` 이 나오면 됩니다(알림 11건이 티켓 7장으로 병합된다는 뜻입니다).
   ```bash
   python -c "from incident import load_json; from ticket_merge import handle_alert; rules = load_json('config/escalation_rules.json'); tickets = []; [handle_alert(a, tickets, rules) for a in load_json('alerts_thu.json')]; print('제공 파일 정상', len(tickets))"
   ```
   - 명령 풀이: 알림 파일의 알림을 하나씩 `handle_alert` 로 처리한 뒤, 만들어진 티켓 수를 출력합니다. 길지만 그대로 복사해 붙여 넣으면 됩니다.
   - `No module named 'ticketing'` 이 나오면 실습 3-2의 `ticketing.py` 가 이 폴더에 없는 것입니다.
   - `notifier.py` 와 `ticket_notice.py` 는 `requests` 도구가 있어야 불러올 수 있어서 여기서는 확인하지 않습니다. 도전 3-3 순서 1번에서 도구를 설치한 뒤 확인합니다.

> 시간이 남아 도전 3-2 · 3-3을 하면, `ticket_merge.py` · `ticket_notice.py` 를 빈칸이 있는 골격으로 바꿔 직접 써 봅니다. 다 쓴 뒤에는 도전의 실행 결과가 정답과 같은지 확인합니다. 결과가 다르면 이 레슨의 완성본을 다시 붙여 넣으면 다음 Unit에 지장이 없습니다.

## `ticket_merge.py` 만들기

**`ticket_merge.py`** 를 만들고 아래 내용을 붙여 넣습니다. 알림이 올 때마다 `handle_alert` 가 합칠 티켓을 찾아, 있으면 그 티켓에 병합하고 없으면 새 티켓을 만듭니다.

병합 조건은 네 가지입니다.

| 조건 | 보는 키 |
|---|---|
| 같은 대상 | `entity` |
| 같은 규칙 | `rule` |
| 해결되지 않은 티켓 | `status` |
| 마지막 갱신 뒤 60분 이내에 온 알림 | `updated_at` · `merge_window_minutes` |

- `change_ticket_status` 는 허용된 이동(열림 → 확인 중 → 해결, 또는 열림 → 해결)일 때만 상태를 바꾸고, 바꾼 사람과 시각을 댓글(`comments`)로 남깁니다.
- 병합 기준과 상태 이동은 도전 3-2 레슨에서 자세히 다룹니다.

```python
from ticketing import make_ticket, has_failed_action, NEXT_STEPS, MANUAL_STEP  # 실습 3-2에 만든 함수와 문장을 불러온다

ALLOWED_MOVES = {                                                              # 티켓 상태마다 옮겨 갈 수 있는 상태의 리스트
    "열림": ["확인 중", "해결"],                                               # 열림에서는 확인 중이나 해결로 갈 수 있다
    "확인 중": ["해결"],                                                       # 확인 중에서는 해결로만 갈 수 있다
    "해결": [],                                                                # 해결에서는 어디로도 갈 수 없다
}


def find_open_ticket(tickets, alert, window):                                  # 티켓 리스트 · 알림 · 병합 시간(분)을 받는 함수
    """같은 대상 · 같은 규칙이고, 해결되지 않았고, window 분 안에 갱신된 티켓을 찾아 리턴한다. 없으면 None 을 리턴한다.
    같은 사건의 알림이 티켓 여러 장이 되는 것을 막을 때 쓴다.
    """
    for ticket in tickets:                                                     # 티켓을 하나씩 읽는다
        if ticket["entity"] == alert["entity"] and ticket["rule"] == alert["rule"]:  # 같은 대상 · 같은 규칙이면
            if ticket["status"] != "해결":                                     # 해결되지 않은 티켓이면
                gap = alert["minute"] - ticket["updated_at"]                   # 마지막 갱신 뒤 몇 분 지났는지
                if gap <= window:                                              # 합치는 시간 안이면
                    return ticket                                              # 그 티켓을 리턴한다
    return None                                                                # 맞는 티켓이 없으면 None 을 리턴한다


def merge_alert(ticket, alert):                                                # 티켓과 새 알림을 받는 함수
    """이미 있는 티켓에 새 알림을 합친다. 합친 알림 수를 1 늘리고, 알림 번호를 더하고, 갱신 시각을 알림이 온 시각으로 바꾼다.
    같은 사건이 되풀이될 때 새 티켓 대신 기존 티켓에 기록을 더할 때 쓴다.
    """
    ticket["count"] = ticket["count"] + 1                                      # 합쳐진 알림 수를 1 늘린다
    ticket["incidents"].append(alert["id"])                                    # 합쳐진 알림 번호를 추가한다
    ticket["updated_at"] = alert["minute"]                                     # 갱신 시각을 이 알림이 온 시각으로 바꾼다
    ticket["done"] = ticket["done"] + alert["done"]                            # 새 알림의 조치 내역을 티켓의 조치 내역 뒤에 이어 붙인다
    if has_failed_action(alert["done"]):                                       # 새 알림의 조치 확인이 실패했으면
        ticket["needs_manual"] = True                                          # 직접 확인이 필요하다고 표시하고
        ticket["next_step"] = MANUAL_STEP                                      # 다음 할 일도 직접 확인하라는 문장으로 바꾼다


def handle_alert(alert, tickets, rules):                                       # 알림 · 티켓 리스트 · 규칙을 받는 함수
    """알림 한 건을 처리한다. 합칠 티켓이 있으면 합치고, 없으면 새 티켓을 만든다. 처리한 티켓과 「새 티켓」 또는 「병합」을 함께 리턴한다.
    알림이 올 때마다 부른다.
    """
    window = rules["merge_window_minutes"]                                     # 같은 사건으로 보는 시간(분)
    existing = find_open_ticket(tickets, alert, window)                        # 합칠 티켓을 찾는다
    if existing is None:                                                       # 합칠 티켓이 없으면
        ticket_no = len(tickets) + 1                                           # 새 티켓 번호
        ticket = make_ticket(alert, ticket_no, rules, NEXT_STEPS)              # 새 티켓을 만들고
        tickets.append(ticket)                                                 # 티켓 리스트에 추가한다
        return ticket, "새 티켓"                                               # 티켓과 「새 티켓」을 함께 리턴하고 끝낸다
    merge_alert(existing, alert)                                               # 찾은 티켓에 새 알림을 합친다
    return existing, "병합"                                                    # 티켓과 「병합」을 함께 리턴한다


def change_ticket_status(ticket, new_status, minute, who):                     # 티켓 · 바꿀 상태 · 시각(분) · 바꾼 사람을 받는 함수
    """허용된 이동이면 티켓 상태를 바꾸고 True, 아니면 바꾸지 않고 False 를 리턴한다. 바꾼 사람과 시각을 댓글로 남긴다.
    담당자가 티켓을 확인하기 시작했는지 끝냈는지 추적할 때 쓴다.
    """
    old_status = ticket["status"]                                              # 지금 상태
    if new_status not in ALLOWED_MOVES[old_status]:                            # 갈 수 없는 이동이면
        return False                                                           # 바꾸지 않고 False 를 리턴한다
    ticket["status"] = new_status                                              # 상태를 바꾼다
    if ticket["acked_at"] == -1:                                               # 처음 확인하는 것이면
        ticket["acked_at"] = minute                                            # 확인한 시각을 적는다
    if new_status == "해결":                                                   # 해결로 바꾸는 것이면
        ticket["resolved_at"] = minute                                         # 해결한 시각을 적는다
    ticket["updated_at"] = minute                                              # 갱신 시각을 적는다
    comment = who + " · " + str(minute) + "분 · " + old_status + " → " + new_status  # 누가 언제 무엇을 했는지 문자열로 만든다
    ticket["comments"].append(comment)                                         # 댓글 리스트에 추가한다
    return True                                                                # 바꿨다고 True 를 리턴한다
```

## `ticket_notice.py` 만들기

`ticket_notice.py` 는 `notifier.py` 의 `notify` 를 불러 쓰므로 `notifier.py` 를 먼저 만듭니다.

1. **[터미널]** `agent_core` 폴더에 `notifier.py` 가 있으면 이 폴더로 복사합니다.
   ```bash
   cp ../agent_core/notifier.py .
   ls
   ```
   - 명령 풀이: `cp 원본 복사본` 파일 복사하기(`.` 은 지금 폴더)
   - `No such file` 이 나오면 `ls ..` 로 `agent_core` 폴더 이름이 맞는지 봅니다. 그래도 없으면 아래 `notifier.py` 상자를 같은 이름의 파일에 붙여 넣습니다.
2. **[VS Code]** `ticket_notice.py` 를 만들고 맨 아래 `ticket_notice.py` 상자를 붙여 넣습니다.

**`notifier.py`** — 알림 함수 `notify` 입니다. 메시지를 알림 서버로 보내고, 보내면 `True`, 실패하면 `[알림 실패]` 와 오류 이름을 출력하고 `False` 를 리턴합니다.

```python
import requests                                                # 인터넷으로 요청을 보내는 도구


def notify(message, url):                                      # 메시지를 알림 서버로 보내는 함수
    try:                                                       # 아래 줄을 해 본다
        requests.post(url, json={"text": message}, timeout=5)  # 메시지를 POST 한다 — 5초만 기다린다
        return True                                            # 보냈다
    except Exception as e:                                     # 에러가 나면 e 에 담아 여기로 온다
        print("[알림 실패]", type(e).__name__)                 # 에러 이름을 알린다 — 숨기지 않는다
        return False                                           # 못 보냈다 — 부른 쪽은 계속 간다
```

**`ticket_notice.py`** — 티켓 알림을 보낼지 정하고 보냅니다.

| 함수 | 하는 일 |
|---|---|
| `pick_recipients` | `config/escalation_rules.json` 의 `recipients` 에서 등급별 수신자를 고른다 |
| `should_send` | 처음 보내는 티켓은 바로, 같은 티켓은 `send_gap_minutes`(30분)가 지나야 다시 보낸다 |
| `send_with_retry` | 실패하면 최대 `MAX_TRIES`(3)번까지 다시 보내 본다 |

- `send_with_retry` 는 성공한 시도 번호를, 모두 실패하면 0 을 리턴합니다. `should_send` 의 30분은 마지막으로 보낸 뒤부터 잽니다.
- 보낼지 정하는 방법과 재시도는 도전 3-3 레슨에서 자세히 다룹니다.

```python
from notifier import notify                                            # notifier.py 의 알림 함수를 불러온다 (성공하면 True, 실패하면 False)

MAX_TRIES = 3                                                          # 알림을 보내 보는 최대 횟수


def pick_recipients(grade, rules):                                     # 등급과 규칙을 받는 함수
    """등급에 맞는 수신자 이름 리스트를 리턴한다.
    위험한 알림일수록 더 많은 사람에게 알려야 할 때 쓴다.
    """
    table = rules["recipients"]                                        # 등급마다 정한 수신자 표
    return table[grade]                                                # 이 등급의 수신자 리스트를 리턴한다


def should_send(ticket, now, gap):                                     # 티켓 · 지금 시각(분) · 알림 간격(분)을 받는 함수
    """이 티켓의 알림을 지금 보내도 되면 True, 너무 일러서 건너뛰어야 하면 False 를 리턴한다.
    같은 티켓의 알림이 연달아 가서 사람이 알림을 무시하게 되는 일을 막을 때 쓴다.
    """
    if ticket["notified_count"] == 0:                                  # 처음 보내는 것이면
        return True                                                    # 바로 보내도 된다고 True 를 리턴한다
    elapsed = now - ticket["last_notified"]                            # 마지막으로 보낸 뒤 몇 분 지났는지
    return elapsed >= gap                                              # 알림 간격 이상 지났는지의 결과를 리턴한다


def send_with_retry(message, url, max_tries):                          # 메시지 · 알림 주소 · 최대 횟수를 받는 함수
    """알림을 최대 max_tries 번 보내 본다. 성공한 시도 번호를, 모두 실패하면 0 을 리턴한다.
    알림 서버가 잠깐 응답하지 않을 때 바로 포기하지 않고 다시 보내 보려고 쓴다.
    """
    for attempt in range(1, max_tries + 1):                            # 시도 번호를 1 부터 최대 횟수까지 하나씩 읽는다
        if notify(message, url):                                       # 알림을 보냈으면
            return attempt                                             # 성공한 시도 번호를 리턴한다
    return 0                                                           # 모두 실패했으면 0 을 리턴한다


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
