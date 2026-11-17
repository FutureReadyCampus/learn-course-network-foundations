---
id: m5-u07-l02
title: Exercise 7-1 · 응답 기한(SLA)이 초과된 미확인 티켓을 상급자에게 에스컬레이션하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/128_day04_pm_escalation_metrics.md
  mission_id: GichanSource.m5-1112-pm-escalation-metrics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 7-1 · 응답 기한(SLA)이 초과된 미확인 티켓을 상급자에게 에스컬레이션하기

## 개요

> **오늘 들어온 일**
>
> - **상황**: Unit 6에서 만든 `TCK-1`(퇴사한 `dami` 계정, 등급 high)은 <mark style="background:#ffdcb0">응답 기한(SLA)이 15분입니다</mark>. 즉, 티켓이 생성된 뒤 15분 안에 담당자가 확인해야 합니다. 확인(acknowledge, 애크날리지)은 알림을 받았고 처리를 맡았다고 표시하는 일입니다. 티켓 상태 `열림`(open, 오픈)은 아직 아무도 확인하지 않은 상태입니다. 그런데 20분이 되도록 어떤 담당자도 `TCK-1` 을 확인하지 않아 `열림` 그대로라고 해 봅시다. 이때는 응답 기한을 5분 넘긴 것입니다.
> - **문제**: 두 가지입니다. 먼저 용어를 정리합니다. 에스컬레이션(escalation)은 처리되지 않는 일을 상급자에게 추가로 통보하는 일입니다.
> - 첫째, <mark style="background:#ffc4d6">티켓이 `열림` 상태로 응답 기한을 초과해도 통보 체계가 없으면 위험도가 높은 사건이 처리되지 않은 채 남습니다</mark>. `TCK-1` 은 high 등급의 퇴사자 계정 사건인데도 방치될 수 있습니다.
> - 둘째, 담당자가 이미 확인 중인 티켓까지 반복해서 에스컬레이션하면 상급자에게 알림이 지나치게 많아집니다. 그러면 상급자가 알림 피로(alert fatigue: 알림이 지나치게 많아 중요한 알림에도 반응이 둔해지는 현상)를 겪고 알림을 무시하게 됩니다.
> - **부탁**: 다음 세 가지를 만들어 주세요.
> - <mark>응답 기한이 지났는데 아직 `열림` 상태인 티켓만</mark> 상급자에게 에스컬레이션해 주세요.
> - <mark style="background:#ffdcb0">응답 기한을 초과한 시간이 길수록 더 높은 직급의 상급자에게 통보해 주세요</mark>. 기한을 넘기면 바로 팀장(`team.lead`)에게, 30분 이상 넘기면 관제 센터장(`soc.head`)에게 통보합니다. 예를 들어 5분 초과는 팀장 대상입니다.
> - 같은 에스컬레이션 단계는 한 번만 실행해 주세요.
> - **바뀌는 점**: 방치된 티켓은 초과 시간에 따라 단계적으로 상급자에게 에스컬레이션되고, 확인 중인 티켓은 대상에서 제외됩니다. 오늘 샘플은 20 · 60 · 110분에 세 번 점검합니다. 점검은 정해진 시각마다 티켓 상태를 조회하는 일입니다.
> - 20분: `TCK-1` 이 5분 초과라서 `team.lead` 에게 통보합니다. 그 뒤 25분에 `kim.sec` 이 `TCK-1` 을 확인해 상태가 `확인 중` 이 됩니다.
> - 60분: `TCK-1` 은 `확인 중` 이므로 대상에서 제외됩니다. 통보는 없습니다.
> - 110분: `TCK-3`(42분 초과)과 `TCK-4`(38분 초과)는 `soc.head` 에게, `TCK-6`(15분 초과)은 `team.lead` 에게 통보합니다.
> - 세 번의 점검에서 에스컬레이션이 실행된 횟수를 모두 합하면 4번입니다. 상황과 숫자는 설명을 위한 예시입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 읽기 · 1.1 에스컬레이션은 「발동 시점 · 대상 티켓 · 통보 대상」을 정의한 규칙이다

**에스컬레이션**(escalation, 에스컬레이션: 처리되지 않는 일을 더 높은 책임자에게 넘기는 절차)은 미리 정한 규칙에 따라 실행합니다. 규칙은 아래 세 가지, 즉 <mark>언제 시작하는지(발동 시점), 어느 티켓이 대상인지(대상 티켓), 누구에게 통보하는지(통보 대상)</mark>를 정합니다. 오늘은 담당자보다 높은 직급(팀장 · 관제 센터장)에게 넘깁니다. 이 방식은 **계층적 에스컬레이션**(hierarchical escalation, 하이어라키컬 에스컬레이션: 지휘 체계를 따라 더 높은 권한자에게 넘기는 방식)에 해당합니다. 전문성이 더 높은 기술 팀에 넘기는 방식은 기능적 에스컬레이션(functional escalation)이라고 따로 부릅니다.

| 정의할 것 | 오늘 정한 방법 | 규칙 파일의 키 |
|---|---|---|
| 발동 시점(trigger, 트리거: 에스컬레이션을 시작하는 조건) | <mark style="background:#ffdcb0">지금 시각이 응답 기한 시각(`sla_due`, due 는 마감이라는 뜻)을 지났을 때</mark> | 티켓의 `sla_due`(규칙 파일의 `sla_minutes` 로 계산) |
| 대상 티켓 | <mark style="background:#ffdcb0">상태가 `열림` 인 티켓만 해당한다</mark>. `확인 중`(담당자가 확인함)이나 `해결`(처리 완료)은 대상에서 제외한다 | |
| 통보 대상 | <mark style="background:#ffdcb0">응답 기한 초과 시간이 0분 이상 30분 미만이면 1단계로 `team.lead`(팀장)에게, 30분 이상이면 2단계로 `soc.head`(관제 센터장)에게 통보한다</mark>. 예를 들어 `TCK-1` 은 5분 초과라 1단계, `TCK-3` 은 42분 초과라 2단계다 | `escalation_steps` |

- 담당자가 티켓을 확인하면 상태가 `열림` 에서 `확인 중` 으로 변경됩니다. 출력과 코드에서는 에스컬레이션 단계를 「올림 단계」라고 표시합니다.
- 이미 실행한 에스컬레이션 단계는 반복하지 않습니다. 티켓의 `escalation_level` 에 실행한 단계를 기록합니다. 그리고 기록된 단계보다 더 높은 단계에 해당할 때만 에스컬레이션합니다. 예를 들어 `escalation_level` 이 1 인 티켓은 1단계에 해당하는 동안 다시 통보하지 않고, 초과 시간이 30분 이상이 되어 2단계에 해당할 때 통보합니다. <mark style="background:#ffc4d6">점검할 때마다 같은 티켓을 반복해서 통보하면 상급자가 알림 피로를 겪어 알림을 무시하게 됩니다</mark>.
- 등급 low 는 응답 기한이 240분입니다. 그래서 오늘 점검 시각(20 · 60 · 110분)은 모두 응답 기한 시각보다 이릅니다. 예를 들어 `TCK-2` 의 응답 기한 시각은 243분입니다. 따라서 등급 low 티켓은 에스컬레이션 대상이 아닙니다.
- 점검 시각은 20분, 60분, 110분입니다(근무 시작 시점을 0분으로 하는 상대 시각). 이처럼 정해진 주기로 상태를 반복 조회하는 방식을 폴링(polling, 폴링: 일정한 간격으로 상태를 반복해서 확인하는 방식)이라고 합니다. 실제 운영에서는 몇 분마다 자동으로 점검합니다.
- 상급자에게 통보하는 기능은 Unit 6의 Exercise 6-3의 `send_with_retry`(알림 전송에 실패하면 최대 3회까지 재시도(retry)하는 함수)를 재사용합니다. Unit 6의 Exercise 6-3 `ticket_notice.py` 를 가져와 사용(import)합니다.

아래 함수 네 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
escalation.py   overdue_minutes   : 응답 기한을 넘긴 시간(분)을 구한다 (1번)
                needs_escalation  : 열림 상태이고 기한이 지났으면 True 를 리턴한다 (2 ~ 4번)
                pick_level        : 넘긴 시간에 해당하는 가장 높은 올림 단계를 고른다 (5 · 6번)
                escalate_ticket   : 그 단계의 상급자에게 알리고 올린 단계를 적는다 (미리 채움)
실행 파일       exercise7-1_run.py  : 점검 시각마다 올릴 티켓을 찾고 (7번), 올리고 (8번), 올린 횟수를 센다 (9번)
```

> **여기부터 문제입니다.**

## Exercise 7-1 · 응답 기한이 초과된 열림 상태 티켓을 초과 시간에 맞는 단계로 에스컬레이션하기

**이런 상황이 있습니다**

- **지금은**: <mark>티켓이 확인되지 않은 채 응답 기한을 초과해도 상급자에게 에스컬레이션되지 않습니다</mark>.
- **만드는 것**: 두 파일을 만듭니다. `escalation.py` 는 응답 기한 초과 시간을 구하고, 에스컬레이션 대상 티켓을 가려내고, 에스컬레이션 단계를 고릅니다. `exercise7-1_run.py` 는 점검 시각마다 대상 티켓을 에스컬레이션하고 실행 횟수를 셉니다. 상급자에게 통보하는 함수는 미리 채워져 있습니다.
- **실행하면**: <mark>출력은 세 단계입니다. 단계 1 은 불러온 티켓 수와 올림 단계 수입니다. 단계 2 는 점검 시각마다 올린 티켓입니다. 단계 3 은 올린 결과 요약입니다.</mark>

**할 일**: 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 알림 서버를 실행한 상태에서 프로그램을 실행합니다. 그리고 단계 2 · 3 의 출력과 서버 터미널의 수신 로그를 해석합니다.

**`escalation.py`** — 응답 기한이 지난 티켓을 상급자에게 올립니다. Exercise 7-2에서도 이 파일을 가져와 사용(import)합니다. 직접 쓰는 곳은 1 ~ 6번입니다. 5번 아래에는 `if` 한 줄을, 6번 아래에는 한 단계 더 들여쓴 줄을 씁니다.

```python
from ticket_notice import send_with_retry, MAX_TRIES                                       # Exercise 6-3에 만든 재시도 함수를 불러온다


def overdue_minutes(ticket, now):                                                          # 티켓과 지금 시각(분)을 받는 함수
    """응답 기한을 넘긴 시간(분)을 리턴한다. 기한이 아직 안 됐으면 음수가 나온다.
    얼마나 늦었는지 알아야 어느 상급자에게 올릴지 정할 수 있어서 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. now 에서 ticket["sla_due"] 를 뺀 값을 리턴한다


def needs_escalation(ticket, now):                                                         # 티켓과 지금 시각(분)을 받는 함수
    """아직 열림 상태이고 응답 기한이 지났으면 True, 아니면 False 를 리턴한다. 담당자가 이미 확인 중이거나 해결한 티켓은 올리지 않는다.
    아무도 열어 보지 않은 티켓만 골라낼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. ticket 의 "status" 가 "열림" 이 아니면 (if, !=)
    # 3.   False 를 리턴한다
    # 4. overdue_minutes(ticket, now) 가 0 이상인지(>=)의 결과를 리턴한다


def pick_level(overdue, steps):                                                            # 넘긴 시간과 올림 단계 리스트를 받는 함수
    """넘긴 시간에 해당하는 가장 높은 올림 단계 번호(1부터)를 리턴한다. 해당하는 단계가 없으면 0 을 리턴한다.
    오래 방치된 티켓일수록 더 높은 상급자에게 올릴 때 쓴다.
    """
    level = 0                                                                              # 처음에는 올릴 단계가 없다 — 미리 채운 줄
    for index in range(len(steps)):                                                        # 단계 번호를 0 부터 하나씩 읽는다 — 미리 채운 줄
        step = steps[index]                                                                # 그 번호의 올림 단계 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. overdue 가 step 의 "overdue_minutes" 이상이면 (if, >=)
            # 6. level 에 index + 1 을 저장한다
    return level                                                                           # 가장 높은 단계 번호를 리턴한다 — 미리 채운 줄


def escalate_ticket(ticket, now, rules):                                                   # 티켓 · 지금 시각(분) · 규칙을 받는 함수
    """티켓을 상급자에게 올린다. 이미 올린 단계이거나 올릴 때가 아니면 「그대로」, 올렸으면 「올림」, 알림이 모두 실패했으면 「실패」를 리턴한다.
    응답 기한이 지나도 아무도 확인하지 않은 티켓을 놓치지 않을 때 쓴다.
    """
    overdue = overdue_minutes(ticket, now)                                                 # 기한을 얼마나 넘겼는지
    steps = rules["escalation_steps"]                                                      # 규칙 파일의 올림 단계 리스트
    level = pick_level(overdue, steps)                                                     # 지금 해당하는 올림 단계
    if level <= ticket["escalation_level"]:                                                # 이미 올린 단계이거나 아직 올릴 때가 아니면
        return "그대로"                                                                    # 아무것도 하지 않는다
    step = steps[level - 1]                                                                # 그 단계의 규칙(받는 사람)
    message = "[올림 " + str(level) + "단계] " + ticket["id"] + " " + ticket["title"] + " · 기한을 " + str(overdue) + "분 넘김 · 받는 사람: " + step["notify"]  # 알림 내용을 만든다
    attempt = send_with_retry(message, rules["alert_url"], MAX_TRIES)                      # 최대 3번까지 보내 본다
    if attempt == 0:                                                                       # 모두 실패했으면
        return "실패"                                                                      # 올리지 못했다고 「실패」를 리턴한다
    ticket["escalation_level"] = level                                                     # 올린 단계를 적는다
    comment = str(now) + "분 · " + str(level) + "단계로 " + step["notify"] + " 에게 올림"  # 댓글 내용을 만든다
    ticket["comments"].append(comment)                                                     # 댓글 리스트에 추가한다
    return "올림"                                                                          # 「올림」을 리턴한다
```

**`exercise7-1_run.py`** — 7 ~ 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 7번 아래에는 `if` 한 줄을, 8번 아래에는 한 단계 더 들여쓴 줄을, 9번 아래에는 또 한 단계 들여쓴 줄을 씁니다. 그 사이의 미리 채운 줄은 그대로 둡니다.

```python
from incident import load_json                                                       # Unit 1 파일의 JSON 읽기 함수를 불러온다
from ticket_merge import change_ticket_status                                        # Exercise 6-2에 만든 상태 바꾸기 함수를 불러온다
from escalation import overdue_minutes, needs_escalation, escalate_ticket            # 방금 만든 함수를 불러온다

tickets = load_json("tickets_unit09.json")                                             # Unit 6의 Exercise 6-3에서 저장한 티켓을 읽는다
rules = load_json("config/escalation_rules.json")                                    # 규칙 파일을 읽는다
steps_count = len(rules["escalation_steps"])                                         # 올림 단계가 몇 개인지 센다
print("--- 단계 1: 불러온 티켓", len(tickets), "장 · 올림 단계", steps_count, "개")  # 단계 1 시작을 알리는 줄
escalated_count = 0                                                                  # 상급자에게 올린 횟수 : 처음에는 0

print("--- 단계 2: 점검 시각마다 상급자에게 올릴 티켓 찾기")                         # 단계 2 시작을 알리는 줄
for now in [20, 60, 110]:                                                            # 점검할 시각(분)을 하나씩 읽는다
    print("[" + str(now) + "분] 점검")                                               # 점검 시각을 출력한다
    for ticket in tickets:                                                           # 티켓을 하나씩 읽는다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 7. needs_escalation(ticket, now) 가 참이면 (if)
            # 8. escalate_ticket(ticket, now, rules) 의 결과를 result 에 저장한다
            overdue = overdue_minutes(ticket, now)                                   # 기한을 얼마나 넘겼는지 구한다 — 미리 채운 줄
            print(ticket["id"], ticket["title"], "→", result, "· 기한을", overdue, "분 넘김 · 올림 단계", ticket["escalation_level"])  # 결과를 출력한다 — 미리 채운 줄
            if result == "올림":                                                     # 올렸으면 — 미리 채운 줄
                # 9. escalated_count 에 escalated_count + 1 을 저장한다 (1 늘린다)
    if now == 20:                                                                    # 20분 점검이 끝나면 — 미리 채운 줄
        change_ticket_status(tickets[0], "확인 중", 25, "kim.sec")                   # 25분에 kim.sec 이 TCK-1 을 확인하기 시작한다 — 미리 채운 줄
        print("[25분] TCK-1 → 확인 중 · kim.sec")                                    # 담당자의 동작을 출력한다 — 미리 채운 줄

print("--- 단계 3: 올린 결과 요약 (올린 횟수", escalated_count, "번)")               # 단계 3 시작을 알리는 줄과 횟수
for ticket in tickets:                                                               # 티켓을 하나씩 읽는다
    if ticket["escalation_level"] > 0:                                               # 상급자에게 올린 티켓이면
        print(ticket["id"], "올림 단계", ticket["escalation_level"], "· 상태", ticket["status"])  # 올림 단계와 지금 상태를 출력한다
```

**순서**

1. **[터미널]** 처음 쓰던 터미널에서 파일 두 개를 만들고 **[VS Code]** 에서 열어 붙여 넣습니다.
   ```bash
   pwd
   touch escalation.py exercise7-1_run.py
   ls
   ```
2. **[VS Code]** `escalation.py` 1 ~ 6번, `exercise7-1_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「Exercise 7-1 한눈에」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`). 알림 서버 터미널은 켜 둡니다.
   ```bash
   python exercise7-1_run.py
   ```
4. 출력은 세 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 제목 줄 하나만 나옵니다(숫자가 제목 줄 안에 함께 나옵니다). 단계 2 는 제목 아래 8줄입니다. 단계 3 은 제목 아래 4줄입니다(올린 횟수는 제목 줄 안에 있습니다). <mark>알림 서버 터미널에는 `[알림 받음]` 줄이 4개 찍힙니다.</mark>
5. **[보고서]** Unit 7 의 `## Exercise 7-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣어 주세요. 그리고 알림 서버 터미널에 출력된 `[알림 받음]` 줄 수와 단계 3 의 올린 횟수(에스컬레이션 실행 횟수)를 적어 주세요.
   - (나) [핵심 질문] `TCK-1` 은 20분 점검에서 1단계로 에스컬레이션되었지만, 60분 점검에서는 에스컬레이션되지 않았습니다. 그 이유를 설명해 주세요. 이때 25분에 변경된 상태와 `needs_escalation` 의 조건을 근거로 쓰고, 이 조건이 없을 때 발생하는 문제도 함께 설명해 주세요.
   - (다) [핵심 질문] 110분 점검에서 `TCK-3` 은 2단계로, `TCK-6` 은 1단계로 에스컬레이션되었습니다. 두 티켓의 응답 기한과 초과 시간을 근거로 단계가 달라진 이유를 설명해 주세요. 또한 등급 low 인 `TCK-2` 가 에스컬레이션되지 않은 이유도 설명해 주세요.

## Exercise 7-1 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 빼서 리턴 | `return now - ticket["sla_due"]` |
| 같지 않으면 | `if ticket["status"] != "열림":` |
| 이상인지의 결과 리턴 | `return overdue_minutes(ticket, now) >= 0` |
| 이상이면 | `if overdue >= step["overdue_minutes"]:` |
| 번호에 1 더해 저장 | `level = index + 1` |
| 함수 결과가 참이면 | `if needs_escalation(ticket, now):` |
| 함수 결과를 변수에 저장 | `result = escalate_ticket(ticket, now, rules)` |
| 1 늘려 다시 저장 | `escalated_count = escalated_count + 1` |

---
