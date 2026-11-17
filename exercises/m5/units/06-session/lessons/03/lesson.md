---
id: m5-u06-l03
title: Exercise 6-2 · 같은 사건의 알림을 티켓 한 장으로 병합(중복 제거)하고, 티켓 상태를 허용된 순서로 전이하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/126_day04_am_ticket_notice.md
  mission_id: GichanSource.m5-1112-am-ticket-notice
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 6-2 · 같은 사건의 알림을 티켓 한 장으로 병합(중복 제거)하고, 티켓 상태를 허용된 순서로 전이하기

## 개요

> **오늘 들어온 일**
>
> - **상황**: Exercise 6-1 방식대로 하면 알림 수만큼 티켓이 생성되므로, 알림 11건이 티켓 11장이 됩니다. 그런데 같은 사건이 반복해서 발생해 중복된 알림이 많습니다.
> - 퇴사한 `dami` 의 계정 알림이 다섯 번(`INC-201` · `INC-205` · `INC-209` · `INC-210` · `INC-211`) 수신됐습니다. 그중 네 건(`INC-201` → `INC-205` → `INC-209` → `INC-210`)은 티켓의 <mark style="background:#ffdcb0">마지막 갱신 뒤 60분 이내</mark>에 이어서 수신됐습니다. 마지막 갱신은 새 알림이 합쳐지거나 상태가 바뀌어 티켓 내용이 마지막으로 바뀐 때입니다. 예를 들어 `INC-205` 는 14분에, `INC-209` 는 40분에 수신되어 직전 알림과 각각 14분 · 26분 간격입니다.
> - `INC-211` 은 160분에 수신되어 마지막 갱신(95분)보다 65분 늦습니다. 60분을 넘으므로 이어진 알림이 아닙니다.
> - 경로 스캔(서버의 여러 주소에 차례로 요청을 보내 약점을 찾는 일) IP `198.51.100.90` 의 알림이 두 번(`INC-202` · `INC-206`) 수신됐습니다.
> - **문제**: 같은 사건의 티켓이 여러 장이면 세 가지 문제가 생깁니다. 첫째, 어느 티켓이 최신인지 알 수 없습니다. 둘째, 한 장을 처리해도 나머지는 열린 상태로 남습니다. 셋째, 티켓이 늘어나서 새로 발생한 사건을 찾기 어렵습니다.
> - **부탁**: 다음 두 가지를 만들어 주세요.
> - 첫째, 병합(merge)입니다. 병합은 새 티켓을 만들지 않고 기존 티켓에 알림을 합치는 일입니다. 같은 대상에 같은 규칙으로 수신된 알림이 티켓의 마지막 갱신 후 60분 이내에 수신되면 기존 티켓에 병합해 주세요.
> - 둘째, 상태 전이(status transition)입니다. 상태 전이는 티켓 상태를 정해진 규칙에 따라 바꾸는 일입니다. 티켓 상태는 <mark style="background:#ffdcb0">허용된 순서(열림 → 확인 중 → 해결, 또는 열림 → 해결)로만 전이하고</mark>, 누가 언제 전이했는지 기록해 주세요.
> - **바뀌는 점**: <mark style="background:#bde3ff">알림 11건이 티켓 7장으로 정리됩니다</mark>. `dami` 의 같은 알림 네 건(`INC-201` · `INC-205` · `INC-209` · `INC-210`)은 TCK-1 한 장에 「합쳐진 알림 4건」으로 집계됩니다. `INC-211` 은 새 티켓이 되고, `198.51.100.90` 의 두 건은 TCK-2 한 장에 합쳐집니다. 상황과 숫자는 설명을 위한 예시입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다. (문법 상자의 코드는 눈으로 읽으면 됩니다.)

## 읽기 · 2.1 병합 기준은 「같은 대상 · 같은 규칙 · 미해결 · 60분 이내」이다

같은 사건의 알림이 새 티켓을 만들지 않고 기존 티켓에 합쳐지는 것을 **병합**(merge)이라고 합니다. 병합은 중복 제거의 한 방식이고, 실행 결과에도 `병합` 으로 나옵니다. 예를 들어 `INC-205` 는 14분에 수신되어 새 티켓 대신 TCK-1 에 병합되고, TCK-1 의 합쳐진 알림이 2건이 됩니다. 병합할지는 아래 <mark style="background:#ffdcb0">네 가지 조건을 모두 확인해 판정합니다</mark>.

| 확인 | 충족하는 경우 |
|---|---|
| 같은 대상 | 티켓의 `entity` 가 알림의 `entity` 와 같다 |
| 같은 규칙 | 티켓의 `rule` 이 알림의 `rule` 과 같다 |
| 끝나지 않음 | 티켓 상태가 `해결` 이 아니다 (<mark style="background:#ffdcb0">해결된 티켓에는 병합하지 않고 새 티켓을 생성한다</mark>) |
| 60분 안 | 알림 수신 시각에서 티켓의 마지막 갱신 시각을 뺀 값(경과 시간, 분)이 <mark style="background:#ffdcb0">`merge_window_minutes`(60) 이하다</mark> |

- <mark>경과 시간은 티켓 생성 시각이 아니라 마지막 갱신 시각을 기준으로 계산합니다.</mark> `INC-209`(40분)가 병합되면 티켓의 마지막 갱신 시각이 40분이 됩니다. `INC-210`(95분)은 마지막 갱신 시각 40분보다 55분 뒤에 수신되므로 병합됩니다. 병합되면 갱신 시각이 95분으로 바뀝니다. `INC-211`(160분)은 마지막 갱신 시각 95분보다 <mark style="background:#bde3ff">65분 뒤에 수신되어 60분을 넘으므로, 새 티켓이 생성됩니다</mark>.
- 상태 전이도 갱신으로 간주합니다. 따라서 상태를 전이하면 갱신 시각이 바뀝니다.
- 같은 대상 · 규칙인데 등급이 다른 알림이 수신되어도, 오늘은 기존 티켓의 등급과 응답 기한을 변경하지 않습니다. 더 높은 등급의 알림이 병합될 때 티켓의 등급을 상향 조정할지는 팀마다 정책으로 정하기도 합니다.
- 시간 범위 기준이 없으면 <mark style="background:#ffc4d6">하루 전에 수신된 알림과 오늘 수신된 알림이 티켓 한 장으로 병합됩니다</mark>. 그러면 오늘 새로 발생한 사건을 식별하기 어렵습니다.
- 해결된 티켓에 새 알림이 병합되면, 상태가 「해결」 그대로여서 아무도 그 티켓을 다시 확인하지 않습니다. 그래서 <mark style="background:#ffc4d6">새로 수신된 알림이 누락됩니다</mark>.
- 티켓 상태 전이(status transition, 스테이터스 트랜지션: 티켓 상태가 한 값에서 다른 값으로 바뀌는 일)는 <mark style="background:#e0d4ff">월요일에 알림 상태를 바꾸던 방식과 같습니다</mark>. 티켓이 생성부터 종료까지 거치는 상태의 흐름을 티켓 수명주기(lifecycle, 라이프사이클)라고 합니다. 오늘은 아래 표에 정의한 전이만 허용합니다.
- 티켓 상태는 세 가지이며, 티켓 도구에서 흔히 쓰는 이름과 뜻이 같습니다. 열림(open, 오픈)은 새로 생성되어 아직 아무도 확인하지 않은 상태입니다. 확인 중(acknowledged, 애크날리지드)은 담당자가 확인하고 처리하기 시작한 상태입니다. 해결(resolved, 리졸브드)은 조치가 끝나 사건이 해소된 상태입니다. 예를 들어 TCK-1 은 생성될 때 열림이고, 단계 3 에서 `kim.sec` 이 50분에 확인 중으로 바꿉니다.
- 상태를 전이할 때 최초 확인 시각(`acked_at`)과 해결 시각(`resolved_at`)도 기록합니다. 오후에 평균 확인 시간과 평균 해결 시간을 계산할 때 사용합니다.

| 지금 상태 | 갈 수 있는 상태 |
|---|---|
| 열림 | 확인 중 · 해결 |
| 확인 중 | 해결 |
| 해결 | 없음 (재개하지 않고 새 티켓을 생성한다) |

** 문법 상자 — `None` 은 「없다」는 값이고, `is None` 으로 확인한다**

```python
def find_name(names, target):
    for name in names:
        if name == target:
            return name
    return None

found = find_name(["dami", "hana"], "gaeun")
print(found)
print(found is None)
```

| 코드 | 뜻 |
|---|---|
| `return None` | 「찾는 것이 없다」는 값을 리턴한다 |
| `found is None` | `found` 가 `None` 이면 `True`, 아니면 `False` 다. `None` 인지 확인할 때는 `==` 대신 `is` 를 쓴다 |
| 위 코드의 출력 | `None` 다음 줄에 `True` |

함수 세 개에서 직접 쓰는 곳은 **아홉 군데**이고 모두 `ticket_merge.py` 안에 있습니다.

```
ticket_merge.py   find_open_ticket     : 합칠 수 있는 티켓을 찾는다 (1 ~ 3번). 없으면 None 을 리턴한다
                  merge_alert          : 찾은 티켓에 알림을 합친다 (4 ~ 6번). 새 알림의 조치 내역과 확인 실패 표시도 옮긴다 (미리 채움)
                  handle_alert         : 합칠 티켓을 찾아 (7번), 없으면 (8번) 새 티켓을 만들고, 있으면 합친다 (9번)
                  change_ticket_status : 허용된 이동일 때만 상태를 바꾸고, 확인 · 해결 시각과 댓글을 남긴다 (미리 채움)
실행 파일         exercise8-2_run.py     : 알림 11건을 처리하고 (미리 채움), TCK-1 의 상태를 바꿔 본다
```

> **여기부터 문제입니다.**

## Exercise Exercise 5-3 · 같은 사건의 알림을 티켓 한 장으로 병합(중복 제거)하고, 티켓 상태를 허용된 순서로 전이하기

** 이런 상황이 있습니다**

- **지금은**: <mark>알림 수만큼 티켓이 생성되므로 같은 사건의 티켓이 여러 장입니다. 또한 티켓 상태를 전이하는 방법도 없습니다</mark>.
- **만드는 것**: 병합할 티켓 찾기 · 병합 · 알림 한 건 처리(`ticket_merge.py`). 상태 전이와 실행 파일은 미리 채워져 있습니다.
- **실행하면**: <mark>단계 1: 알림 11건의 처리 결과, 단계 2: 알림 수와 티켓 수 · 티켓 목록, 단계 3: TCK-1 의 상태 바꾸기와 댓글이 나옵니다.</mark>

** 할 일**: 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행 파일은 그대로 붙여 넣습니다. 실행해서 단계 1 ~ 3 을 읽습니다.

**`ticket_merge.py`** — 같은 사건의 알림을 티켓 한 장으로 병합합니다. Exercise 6-3도 가져와 사용(import)합니다. Exercise 6-1의 `ticketing.py` 가 같은 폴더에 있어야 합니다. 직접 쓰는 곳은 1 ~ 9번입니다.

- 1번 아래에는 `if` 한 줄을 씁니다.
- 2번 아래에는 `if` 한 줄을 씁니다. 1번 아래에 쓰는 `if` 안쪽에는 미리 채운 `if` 가 이미 한 단계 들어가 있습니다. 그래서 2번은 1번보다 두 단계 오른쪽에서 시작합니다.
- 3번 아래에는 2번보다 한 단계 오른쪽에 `return` 한 줄을 씁니다.
- 8번도 `if` 한 줄만 씁니다. 그 아래 미리 채운 줄들이 `if` 안쪽입니다.

```python
from ticketing import make_ticket, has_failed_action, NEXT_STEPS, MANUAL_STEP        # Exercise 6-1에 만든 함수와 문장을 불러온다

ALLOWED_MOVES = {                                                                    # 티켓 상태마다 옮겨 갈 수 있는 상태의 리스트
    "열림": ["확인 중", "해결"],                                                     # 열림에서는 확인 중이나 해결로 갈 수 있다
    "확인 중": ["해결"],                                                             # 확인 중에서는 해결로만 갈 수 있다
    "해결": [],                                                                      # 해결에서는 어디로도 갈 수 없다
}


def find_open_ticket(tickets, alert, window):                                        # 티켓 리스트 · 알림 · 병합 시간(분)을 받는 함수
    """같은 대상 · 같은 규칙이고, 해결되지 않았고, window 분 안에 갱신된 티켓을 찾아 리턴한다. 없으면 None 을 리턴한다.
    같은 사건의 알림이 티켓 여러 장이 되는 것을 막을 때 쓴다.
    """
    for ticket in tickets:                                                           # 티켓을 하나씩 읽는다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 1. ticket 의 "entity" 가 alert 의 "entity" 와 같고(and) ticket 의 "rule" 도 alert 의 "rule" 과 같으면 (if, ==)
            if ticket["status"] != "해결":                                           # 해결되지 않은 티켓이면 — 미리 채운 줄
                gap = alert["minute"] - ticket["updated_at"]                         # 마지막 갱신 뒤 몇 분 지났는지 — 미리 채운 줄
                # 2. gap 이 window 이하이면 (if, <=)
                    # 3. ticket 을 리턴한다
    return None                                                                      # 맞는 티켓이 없으면 None 을 리턴한다 — 미리 채운 줄


def merge_alert(ticket, alert):                                                      # 티켓과 새 알림을 받는 함수
    """이미 있는 티켓에 새 알림을 합친다. 합친 알림 수를 1 늘리고, 알림 번호를 더하고, 갱신 시각을 알림이 온 시각으로 바꾼다.
    같은 사건이 되풀이될 때 새 티켓 대신 기존 티켓에 기록을 더할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. ticket 의 "count" 에 ticket["count"] + 1 을 저장한다 (1 늘린다)
    # 5. ticket 의 "incidents" 리스트에 alert 의 "id" 를 추가한다 (append)
    # 6. ticket 의 "updated_at" 에 alert 의 "minute" 을 저장한다
    ticket["done"] = ticket["done"] + alert["done"]                                  # 새 알림의 조치 내역을 티켓의 조치 내역 뒤에 이어 붙인다 — 미리 채운 줄
    if has_failed_action(alert["done"]):                                             # 새 알림의 조치 확인이 실패했으면 — 미리 채운 줄
        ticket["needs_manual"] = True                                                # 직접 확인이 필요하다고 표시하고 — 미리 채운 줄
        ticket["next_step"] = MANUAL_STEP                                            # 다음 할 일도 직접 확인하라는 문장으로 바꾼다 — 미리 채운 줄


def handle_alert(alert, tickets, rules):                                             # 알림 · 티켓 리스트 · 규칙을 받는 함수
    """알림 한 건을 처리한다. 합칠 티켓이 있으면 합치고, 없으면 새 티켓을 만든다. 처리한 티켓과 「새 티켓」 또는 「병합」을 함께 리턴한다.
    알림이 올 때마다 부른다.
    """
    window = rules["merge_window_minutes"]                                           # 같은 사건으로 보는 시간(분) — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. find_open_ticket(tickets, alert, window) 의 결과를 existing 에 저장한다
    # 8. existing 이 None 이면 (if, is)
        ticket_no = len(tickets) + 1                                                 # 새 티켓 번호 — 미리 채운 줄
        ticket = make_ticket(alert, ticket_no, rules, NEXT_STEPS)                    # 새 티켓을 만들고 — 미리 채운 줄
        tickets.append(ticket)                                                       # 티켓 리스트에 추가한다 — 미리 채운 줄
        return ticket, "새 티켓"                                                     # 티켓과 「새 티켓」을 함께 리턴하고 끝낸다 — 미리 채운 줄
    # 9. merge_alert(existing, alert) 를 호출한다 (합칠 티켓이 있을 때만 여기까지 온다)
    return existing, "병합"                                                          # 티켓과 「병합」을 함께 리턴한다 — 미리 채운 줄


def change_ticket_status(ticket, new_status, minute, who):                           # 티켓 · 바꿀 상태 · 시각(분) · 바꾼 사람을 받는 함수
    """허용된 이동이면 티켓 상태를 바꾸고 True, 아니면 바꾸지 않고 False 를 리턴한다. 바꾼 사람과 시각을 댓글로 남긴다.
    담당자가 티켓을 확인하기 시작했는지 끝냈는지 추적할 때 쓴다.
    """
    old_status = ticket["status"]                                                    # 지금 상태
    if new_status not in ALLOWED_MOVES[old_status]:                                  # 갈 수 없는 이동이면
        return False                                                                 # 바꾸지 않고 False 를 리턴한다
    ticket["status"] = new_status                                                    # 상태를 바꾼다
    if ticket["acked_at"] == -1:                                                     # 처음 확인하는 것이면
        ticket["acked_at"] = minute                                                  # 확인한 시각을 적는다
    if new_status == "해결":                                                         # 해결로 바꾸는 것이면
        ticket["resolved_at"] = minute                                               # 해결한 시각을 적는다
    ticket["updated_at"] = minute                                                    # 갱신 시각을 적는다
    comment = who + " · " + str(minute) + "분 · " + old_status + " → " + new_status  # 누가 언제 무엇을 했는지 문자열로 만든다
    ticket["comments"].append(comment)                                               # 댓글 리스트에 추가한다
    return True                                                                      # 바꿨다고 True 를 리턴한다
```

**`exercise8-2_run.py`** — 쓰는 줄이 없습니다. 그대로 붙여 넣습니다.

```python
from incident import load_json                                                              # 월요일 파일의 JSON 읽기 함수를 불러온다
from ticket_merge import handle_alert, change_ticket_status                                 # 방금 만든 함수를 불러온다

alerts = load_json("alerts_thu.json")                                                       # 오늘 오전 알림 파일을 읽는다
rules = load_json("config/escalation_rules.json")                                           # 규칙 파일을 읽는다
tickets = []                                                                                # 만든 티켓을 저장할 빈 리스트

window = rules["merge_window_minutes"]                                                      # 같은 사건으로 보는 시간(분)을 꺼낸다
print("--- 단계 1: 알림", len(alerts), "건 처리 (합치는 시간", window, "분)")               # 단계 1 시작을 알리는 줄과 개수
for alert in alerts:                                                                        # 알림을 하나씩 읽는다
    ticket, action = handle_alert(alert, tickets, rules)                                    # 알림을 처리하고 티켓과 처리 방식을 함께 받는다
    print(alert["id"], "->", ticket["id"], action, "· 합쳐진 알림", ticket["count"], "건")  # 알림 한 건의 결과를 출력한다

print("--- 단계 2: 알림", len(alerts), "건 → 티켓", len(tickets), "장")                     # 단계 2 시작을 알리는 줄과 개수
for ticket in tickets:                                                                      # 티켓을 하나씩 읽는다
    print(ticket["id"], ticket["title"], "· 알림", ticket["incidents"], "· 상태", ticket["status"])  # 티켓 한 줄을 출력한다

print("--- 단계 3: TCK-1 상태 바꾸기")                                                      # 단계 3 시작을 알리는 줄
first = tickets[0]                                                                          # 첫 번째 티켓을 꺼낸다
moves = [("확인 중", "kim.sec", 50), ("해결", "kim.sec", 65), ("열림", "lee.soc", 70)]      # 바꿀 상태 · 바꾼 사람 · 시각을 모은 리스트
for new_status, who, minute in moves:                                                       # 세 값을 한 번에 받아 하나씩 읽는다
    changed = change_ticket_status(first, new_status, minute, who)                          # 상태를 바꿔 본다
    if changed:                                                                             # 바뀌었으면
        print(first["id"], "→", new_status, "· 바꾼 사람", who)                             # 바뀐 상태를 출력한다
    else:                                                                                   # 안 바뀌었으면
        reason = first["status"] + "에서는 갈 수 없음"                                      # 거절한 이유를 문자열로 만든다
        print(first["id"], "→", new_status, "· 거절됨 ·", reason)                           # 거절한 이유를 출력한다
print("댓글 기록:")                                                                         # 댓글 제목을 출력한다
for comment in first["comments"]:                                                           # 댓글을 하나씩 읽는다
    print(" -", comment)                                                                    # 댓글을 출력한다
```

**순서**

1. **[터미널]** 파일 두 개를 만들고 붙여 넣습니다.
   ```bash
   pwd
   touch ticket_merge.py exercise8-2_run.py
   ls
   ```
2. **[VS Code]** `ticket_merge.py` 1 ~ 9번을 씁니다. 막히면 아래 「Exercise 6-2 한눈에」를 봅니다.
3. **[터미널]** 실행합니다(맥북은 `python3`).
   ```bash
   python exercise8-2_run.py
   ```
4. 출력은 세 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 11줄, 단계 2 는 티켓 목록 7줄, 단계 3 은 상태 바꾸기 3줄과 `댓글 기록:` 줄, 댓글 2줄입니다. 단계 3 은 알림 처리와 별개입니다. TCK-1 에 대해 담당자가 50분과 65분에 상태를 바꾸는 동작을 했다고 가정하고, 상태 전이만 보여 줍니다.
5. **[보고서]** Unit 6 의 `## Exercise 6-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣어 주세요. 그리고 단계 2 의 티켓 수와 TCK-1 에 병합된 알림 번호를 적어 주세요.
   - (나) [핵심 질문] `INC-210` 은 TCK-1 에 병합됐고 `INC-211` 은 새 티켓이 생성됐습니다. 각각 그렇게 처리된 사유를 적어 주세요. 근거는 두 알림이 수신된 시각과 TCK-1 의 마지막 갱신 시각입니다. 그다음 60분을 티켓 생성 시각(0분)부터 계산한다면 `INC-210` 이 어떻게 처리될지 적어 주세요.
   - (다) [핵심 질문] 단계 3 에서 `해결 → 열림` 전이가 거절됐습니다. 이 전이를 허용하면 어떤 문제가 생기는지 적어 주세요. 그다음 병합 조건에서 `해결` 확인을 제외한다고 가정합니다. 이때 해결 후에 수신된 같은 알림이 어떻게 처리되는지 적어 주세요.

## Exercise 6-2 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 두 조건이 모두 맞으면 | `if ticket["entity"] == alert["entity"] and ticket["rule"] == alert["rule"]:` |
| 이하이면 | `if gap <= window:` |
| 딕셔너리의 숫자를 1 늘리기 | `ticket["count"] = ticket["count"] + 1` |
| 딕셔너리 안의 리스트에 추가 | `ticket["incidents"].append(alert["id"])` |
| 함수 결과를 변수에 저장 | `existing = find_open_ticket(tickets, alert, window)` |
| 없는 값인지 | `if existing is None:` |
| 함수 호출만 하기 | `merge_alert(existing, alert)` |

---
