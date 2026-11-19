---
id: m5-u07-l03
title: 실습 7-2 · 근무 시뮬레이션과 대응 지표 산출
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/128_day04_pm_escalation_metrics.md
  mission_id: GichanSource.m5-1112-pm-escalation-metrics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 7-2 · 근무 시뮬레이션과 대응 지표 산출

## 목표: 근무 시뮬레이션과 지표

> **오늘 들어온 일**
>
> - **상황**: 근무 교대(shift handoff, 시프트 핸드오프: 근무 시간이 끝나 다음 근무자에게 업무를 넘기는 일) 직전에 팀장이 요청합니다. 요청 내용은 「이번 Unit의 근무 3시간 동안 팀의 대응 속도를 지표로 보고해 주세요」입니다. 이 3시간 동안 알림이 11건 수신되었고, 담당자가 티켓 상태를 변경한 동작 기록(이력)은 8건입니다. 예를 들어 `TCK-1` 은 0분에 생성되어, 10분에 `확인 중` 으로, 45분에 `해결` 로 바뀌었습니다.
> - **문제**: 티켓마다 상태와 시각이 따로 기록되어 있습니다. 그래서 <mark style="background:#ffc4d6">대응 속도를 나타내는 집계 값(여러 기록을 합쳐 낸 숫자)이 없습니다</mark>. 응답 기한 위반 티켓(확인 시각이 응답 기한 시각보다 늦은 티켓. 아직 확인하지 않은 티켓은 현재 시각을 확인 시각으로 봅니다)도 사람이 하나씩 세어야 합니다. 인계할 미해결 티켓도 하나씩 확인해서 골라야 합니다. 그러면 보고가 늦어지고 세다가 틀릴 수 있습니다.
> - **부탁**: 근무 3시간 시뮬레이션(연습용 알림 · 동작 기록으로 근무 시간을 재현하는 방식)을 처음부터 끝까지 연속 실행한 뒤, 다음 세 가지를 구해 주세요. 그리고 해결되지 않은 티켓은 다음 근무자에게 인계할 목록으로 출력해 주세요.
> - 평균 확인 시간(MTTA): 티켓이 생성된 때부터 담당자가 처음 확인하기까지 걸린 시간의 평균
> - 평균 해결 시간(MTTR): 티켓이 생성된 때부터 해결되기까지 걸린 시간의 평균
> - 응답 기한 위반 티켓 수
> - **바뀌는 점**: 지표 세 개와 인계 목록(handoff list, 핸드오프 리스트: 다음 근무자에게 넘길 미해결 티켓 목록)으로 보고합니다. 오늘 샘플에서는 확인한 티켓 5장으로 구한 평균 확인 시간이 55.0분이고, 해결한 티켓 3장으로 구한 평균 해결 시간이 84.0분이며, 응답 기한 위반은 2장입니다. 인계 목록은 미해결 티켓 4장(`TCK-2` · `TCK-4` · `TCK-5` · `TCK-7`)입니다. 상황과 숫자는 설명을 위한 예시입니다.

## 2.1 MTTA · MTTR · 기한 위반 수의 뜻

| 지표 | 정의 | 계산 방법 |
|---|---|---|
| **평균 확인 시간**(MTTA, Mean Time To Acknowledge) | 티켓이 생성된 시점부터 담당자가 처음 확인(acknowledge)하기까지 걸린 시간의 평균 | <mark style="background:#ffdcb0">(확인 시각 − 생성 시각)의 평균</mark> |
| **평균 해결 시간**(MTTR, Mean Time To Resolve) | 티켓이 생성된 시점부터 해결(resolve)되기까지 걸린 시간의 평균 | <mark style="background:#ffdcb0">(해결 시각 − 생성 시각)의 평균</mark> |
| 응답 기한 위반(SLA breach, 에스엘에이 브리치: 약속한 응답 기한을 지키지 못한 것) | 응답 기한 시각보다 늦게 확인된 티켓 | <mark style="background:#ffdcb0">확인 시각 > `sla_due`</mark> |

- 예를 들어 `TCK-1` 은 0분에 생성되어 10분에 확인되었으므로 확인 시간이 10 − 0 = 10분입니다. `TCK-3` 은 8분에 생성되어 80분에 확인되었으므로 80 − 8 = 72분입니다. 평균 확인 시간은 이런 확인 시간을 모두 더해 확인한 티켓 수로 나눈 값입니다.
- 평균 해결 시간도 같은 방식으로 구합니다. 오늘 샘플에서 해결한 티켓 3장의 해결 시간은 `TCK-1` 45분, `TCK-3` 112분, `TCK-6` 95분입니다. 합계 252분을 3으로 나누면 평균 해결 시간은 84.0분입니다.
- <mark style="background:#ffdcb0">미확인 티켓과 미해결 티켓은 해당 시간 값이 아직 없으므로 평균 계산에서 제외합니다</mark>.
- MTTR 의 R 은 이 문서에서는 해결(Resolve)을 뜻합니다. 그러나 도구와 조직에 따라 <mark style="background:#ffc4d6">복구(Recovery) · 수리(Repair) 같은 다른 뜻으로도 정의합니다</mark>. 그래서 보고할 때는 측정 구간, 즉 어느 시점부터 어느 시점까지 잰 값인지를 함께 적습니다.
- 응답 기한 위반은 아직 확인되지 않은 티켓도 집계합니다. 확인되지 않았는데 이미 기한 시각이 지났다면 위반이기 때문입니다. 판정 방법은 다음과 같습니다. <mark style="background:#ffdcb0">미확인 티켓은 「지금 시각에 확인된 것」으로 봅니다</mark>. 그리고 지금 시각이 기한 시각을 넘었는지 비교합니다.
- 예를 들어 `TCK-2` 는 근무 종료 시각 180분까지 확인되지 않았지만, 응답 기한 시각이 243분이어서 아직 기한 안이므로 위반이 아닙니다.
- 평균은 표본 크기(sample size, 샘플 사이즈: 평균을 계산한 티켓 수)와 함께 보고합니다. 티켓 5장으로 낸 평균보다 50장으로 낸 평균을 더 믿을 수 있기 때문입니다. 오늘 평균 확인 시간은 티켓 5장으로, 평균 해결 시간은 티켓 3장으로 계산한 평균입니다.
- 근무 시뮬레이션에서도 Unit 6의 실습 6-2의 병합 규칙을 그대로 적용합니다. 이 규칙에서는 <mark style="background:#ffdcb0">해결된 티켓에 새 알림을 병합하지 않습니다</mark>. `TCK-1` 은 45분에 해결되었으므로, 95분에 같은 `dami` 알림(`INC-210`)이 수신되면 새 티켓 `TCK-7` 이 생성됩니다.

**문법 상자 — `sum()` 은 리스트의 합계를, `%`(나머지 연산자, modulo operator) 는 나눗셈의 나머지를 구한다**

```python
times = [10, 70, 40]
print(sum(times))
print(sum(times) / len(times))
print(25 % 10)
print(30 % 10 == 0)
```

| 코드 | 결과 | 뜻 |
|---|---|---|
| `sum(times)` | `120` | 리스트의 숫자를 모두 더한다 |
| `sum(times) / len(times)` | `40.0` | 합계를 개수로 나눈 평균이다. `/` 의 결과는 소수점이 있는 숫자다 |
| `25 % 10` | `5` | 25 를 10 으로 나눈 나머지다 |
| `30 % 10 == 0` | `True` | 나머지가 0 이면 나누어떨어진다. <mark style="background:#ffdcb0">수업에서는 `now % 10 == 0` 으로 10분마다 점검한다</mark> |

아래 함수 네 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
shift_metrics.py   average                 : 숫자 리스트의 평균을 구한다. 비어 있으면 0 (1 ~ 3번)
                   collect_response_times  : 확인한 티켓마다 (확인한 시각 − 만든 시각)을 모은다 (4 · 5번)
                   collect_resolve_times   : 해결한 티켓마다 (해결한 시각 − 만든 시각)을 모은다 (미리 채움)
                   count_sla_breaches      : 응답 기한을 넘겨 확인한 티켓 수를 센다 (6 · 7번)
실행 파일          exercise7-2_run.py        : 가상 근무 3시간을 실행하고 (미리 채움), 확인까지 걸린 시간 리스트를 만들어 (8번) 평균을 구한다 (9번)
```

## 실습 7-2 · 근무 시뮬레이션과 대응 지표 산출

**이런 상황이 있습니다**

- **지금은**: <mark>티켓 생성 · 병합 · 통지 · 에스컬레이션이 개별 기능으로만 있고, 근무 3시간을 연속 실행해 지표로 보고하는 코드가 없습니다</mark>.
- **만드는 것**: 두 파일을 만듭니다. `shift_metrics.py` 는 평균을 계산하고, 확인 시간을 모으고, 응답 기한 위반 티켓 수를 셉니다. `exercise7-2_run.py` 는 확인까지 걸린 시간 리스트를 만들고 그 평균(평균 확인 시간)을 구합니다. 근무 3시간을 시뮬레이션하는 부분은 미리 채워져 있습니다.
- **실행하면**: <mark>출력은 네 단계입니다. 단계 1 은 0분부터 180분까지 발생한 이벤트(알림 처리 · 담당자 동작 · 에스컬레이션)입니다. 단계 2 는 근무 지표(평균 확인 시간 · 평균 해결 시간 · 응답 기한 위반 수)입니다. 단계 3 은 다음 근무자에게 인계할 미해결 티켓입니다. 단계 4 는 파일에 저장한 티켓 수입니다.</mark>

**할 일**: 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 알림 서버를 실행한 상태에서 프로그램을 실행합니다. 그리고 단계 1 ~ 3 의 출력을 해석합니다.

**`shift_metrics.py`** — 근무 지표를 계산합니다. 직접 쓰는 곳은 1 ~ 7번입니다. 4번 아래에는 `if` 한 줄을, 5번 아래에는 한 단계 더 들여쓴 줄을 씁니다. 6번과 7번도 같은 모양입니다.

```python
def average(numbers):                                                   # 숫자 리스트를 받는 함수
    """숫자 리스트의 평균을 리턴한다. 리스트가 비어 있으면 0 을 리턴한다.
    평균 확인 시간과 평균 해결 시간을 계산할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. numbers 의 개수(len)가 0 이면 (if, ==)
    # 2.   0 을 리턴한다 (비어 있으면 나눌 수 없다)
    # 3. sum(numbers) / len(numbers) 를 리턴한다 (합계를 개수로 나눈다)


def collect_response_times(tickets):                                    # 티켓 리스트를 받는 함수
    """담당자가 처음 확인한 티켓마다 (확인한 시각 − 만든 시각)을 모아 리스트로 리턴한다. 아직 확인하지 않은 티켓은 뺀다.
    평균 확인 시간(MTTA)을 구할 재료를 만들 때 쓴다.
    """
    times = []                                                          # 걸린 시간(분)을 저장할 빈 리스트 — 미리 채운 줄
    for ticket in tickets:                                              # 티켓을 하나씩 읽는다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 4. ticket 의 "acked_at" 이 -1 이 아니면 (if, !=)
            # 5. times 리스트에 ticket["acked_at"] - ticket["created_at"] 을 추가한다 (append)
    return times                                                        # 걸린 시간 리스트를 리턴한다 — 미리 채운 줄


def collect_resolve_times(tickets):                                     # 티켓 리스트를 받는 함수
    """해결한 티켓마다 (해결한 시각 − 만든 시각)을 모아 리스트로 리턴한다. 아직 해결하지 않은 티켓은 뺀다.
    평균 해결 시간(MTTR)을 구할 재료를 만들 때 쓴다.
    """
    times = []                                                          # 걸린 시간(분)을 저장할 빈 리스트
    for ticket in tickets:                                              # 티켓을 하나씩 읽는다
        if ticket["resolved_at"] != -1:                                 # 해결한 티켓이면
            times.append(ticket["resolved_at"] - ticket["created_at"])  # 걸린 시간을 추가한다
    return times                                                        # 걸린 시간 리스트를 리턴한다


def count_sla_breaches(tickets, now):                                   # 티켓 리스트와 지금 시각(분)을 받는 함수
    """응답 기한을 넘긴 티켓 수를 리턴한다. 아직 확인하지 않은 티켓은 지금 시각에 확인한 것으로 본다.
    응답 기한(SLA)을 얼마나 지켰는지 보고할 때 쓴다.
    """
    late = 0                                                            # 기한을 넘긴 티켓 수 : 처음에는 0 — 미리 채운 줄
    for ticket in tickets:                                              # 티켓을 하나씩 읽는다 — 미리 채운 줄
        checked_time = ticket["acked_at"]                               # 확인한 시각 — 미리 채운 줄
        if checked_time == -1:                                          # 아직 확인하지 않았으면 — 미리 채운 줄
            checked_time = now                                          # 지금 시각에 확인한 것으로 본다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 6. checked_time 이 ticket 의 "sla_due" 보다 크면 (if, >)
            # 7. late 에 late + 1 을 저장한다 (1 늘린다)
    return late                                                         # 기한을 넘긴 티켓 수를 리턴한다 — 미리 채운 줄
```

**`exercise7-2_run.py`** — 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. Unit 6의 `ticket_merge.py` · `ticket_notice.py` 와 실습 7-1의 `escalation.py` 가 같은 폴더에 있어야 합니다.

```python
from incident import load_json, save_json                                             # Unit 1 파일의 JSON 읽기 · 저장 함수를 불러온다
from ticket_merge import handle_alert, change_ticket_status                           # 실습 6-2에 만든 함수를 불러온다
from ticket_notice import send_ticket_notice                                          # 실습 6-3에 만든 알리기 함수를 불러온다
from escalation import needs_escalation, escalate_ticket                              # 실습 7-1에 만든 올리기 함수를 불러온다
from shift_metrics import average, collect_response_times, collect_resolve_times, count_sla_breaches  # 방금 만든 계산 함수를 불러온다

alerts = load_json("alerts_thu.json")                                                 # 이번 Unit의 알림 파일을 읽는다
events = load_json("status_events.json")                                              # 담당자의 동작 기록을 읽는다
rules = load_json("config/escalation_rules.json")                                     # 규칙 파일을 읽는다
tickets = []                                                                          # 만든 티켓을 저장할 빈 리스트

print("--- 단계 1: 가상 근무 0분부터 180분까지 (알림", len(alerts), "건 · 담당자 동작", len(events), "건)")  # 단계 1 시작을 알리는 줄
for now in range(0, 181):                                                             # 지금 시각을 0 분부터 180 분까지 1분씩 꺼낸다
    for alert in alerts:                                                              # 알림을 하나씩 읽는다
        if alert["minute"] == now:                                                    # 이 시각에 온 알림이면
            ticket, action = handle_alert(alert, tickets, rules)                      # 알림을 처리하고 티켓과 처리 방식을 받는다
            result = send_ticket_notice(ticket, now, rules)                           # 담당자에게 알린다
            print("[" + str(now) + "분]", alert["id"], "→", ticket["id"], action, "· 알리기", result)  # 알림 처리 결과를 출력한다
    for event in events:                                                              # 담당자의 동작을 하나씩 읽는다
        if event["minute"] == now:                                                    # 이 시각에 한 동작이면
            for ticket in tickets:                                                    # 티켓을 하나씩 읽는다
                if ticket["id"] == event["ticket"]:                                   # 동작 대상 티켓이면
                    change_ticket_status(ticket, event["status"], now, event["who"])  # 상태를 바꾼다
                    print("[" + str(now) + "분]", ticket["id"], "→", event["status"], "·", event["who"])  # 담당자의 동작을 출력한다
    if now % 10 == 0:                                                                 # 10분마다 (10 으로 나눈 나머지가 0 이면)
        for ticket in tickets:                                                        # 티켓을 하나씩 읽는다
            if needs_escalation(ticket, now):                                         # 상급자에게 올릴 티켓이면
                result = escalate_ticket(ticket, now, rules)                          # 상급자에게 올린다
                if result != "그대로":                                                # 새로 올렸거나 실패했으면
                    print("[" + str(now) + "분]", ticket["id"], "상급자에게", result, "· 올림 단계", ticket["escalation_level"])  # 올린 결과를 출력한다

print("--- 단계 2: 근무 지표")                                                        # 단계 2 시작을 알리는 줄
# ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
# 8. collect_response_times(tickets) 의 결과를 ack_times 에 저장한다
# 9. average(ack_times) 의 결과를 mean_ack_minutes 에 저장한다
resolve_times = collect_resolve_times(tickets)                                        # 해결한 티켓의 걸린 시간 리스트 — 미리 채운 줄
mean_resolve_minutes = average(resolve_times)                                         # 평균 해결 시간(MTTR) — 미리 채운 줄
late_count = count_sla_breaches(tickets, 180)                                         # 응답 기한을 넘긴 티켓 수 — 미리 채운 줄
print("티켓", len(tickets), "장 · 확인한 티켓", len(ack_times), "장 · 해결한 티켓", len(resolve_times), "장")  # 티켓 수를 출력한다
print("평균 확인 시간(MTTA):", mean_ack_minutes, "분")                                # 평균 확인 시간을 출력한다
print("평균 해결 시간(MTTR):", mean_resolve_minutes, "분")                            # 평균 해결 시간을 출력한다
print("응답 기한을 넘긴 티켓:", late_count, "장")                                     # 응답 기한을 넘긴 티켓 수를 출력한다

print("--- 단계 3: 다음 근무자에게 넘길 티켓 (해결되지 않은 티켓)")                   # 단계 3 시작을 알리는 줄
for ticket in tickets:                                                                # 티켓을 하나씩 읽는다
    if ticket["status"] != "해결":                                                    # 해결되지 않은 티켓이면
        print(ticket["id"], ticket["title"], "· 상태", ticket["status"], "·", ticket["next_step"])  # 티켓과 다음 할 일을 출력한다

save_json(tickets, "shift_tickets.json")                                              # 근무가 끝난 티켓을 파일에 저장한다
saved = load_json("shift_tickets.json")                                               # 저장한 파일을 다시 읽는다
print("--- 단계 4: 파일에 저장된 티켓", len(saved), "장")                             # 단계 4 시작을 알리는 줄과 장수
```

**순서**

1. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `shift_metrics.py` 와 `exercise7-2_run.py` 를 이름 그대로 만들고, 위 코드 상자를 복사해 붙여 넣고 저장합니다.
2. **[VS Code]** `shift_metrics.py` 1 ~ 7번, `exercise7-2_run.py` 8 · 9번을 씁니다. 막히면 아래 「실습 7-2 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`). 알림 서버 터미널은 켜 둡니다.
   ```bash
   python exercise7-2_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 22줄(알림 11줄 · 담당자 동작 8줄 · 상급자에게 올림 3줄), 단계 2 는 4줄, 단계 3 은 4줄(해결되지 않은 티켓 4장)입니다. 단계 4 는 제목 줄 하나뿐이고 저장한 티켓 수가 그 줄 안에 있습니다. <mark style="background:#bde3ff">실습 7-2를 실행하면 알림 서버 터미널에 새로 출력되는 `[알림 받음]` 줄이 12개입니다.</mark> 실습 7-1의 4줄 아래에 이어서 나오므로 터미널 전체로는 16줄입니다.
5. **[보고서]** `report_u7.md` 의 `## 실습 7-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣어 주세요. 그리고 그 출력에서 평균 확인 시간(MTTA) · 평균 해결 시간(MTTR) · 응답 기한을 넘긴 티켓 수(응답 기한 위반 수)를 찾아 적어 주세요.
   - (나) [핵심 질문] 확인된 티켓 `TCK-1` · `TCK-3` · `TCK-4` · `TCK-6` · `TCK-7` 의 확인 시간(확인 시각 − 생성 시각)을 각각 계산하고, 그 평균인 평균 확인 시간(MTTA)을 직접 계산해 적어 주세요. 또한 미확인 티켓인 `TCK-2` · `TCK-5` 를 평균에서 제외하는 이유도 설명해 주세요.
   - (다) [핵심 질문] 응답 기한을 위반한 티켓 2장이 어느 티켓인지 적어 주세요. 이때 각 티켓의 `sla_due` 와 확인 시각을 근거로 씁니다. 그리고 단계 1 의 70분 · 80분 · 110분에 출력된 줄(상급자에게 올림 · 확인 중)이 이 두 티켓과 어떤 관계인지 설명해 주세요.

## 실습 7-2 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 개수가 0 이면 | `if len(numbers) == 0:` |
| 합계를 개수로 나누기 | `return sum(numbers) / len(numbers)` |
| 값이 -1 이 아니면 | `if ticket["acked_at"] != -1:` |
| 리스트에 추가 | `times.append(ticket["acked_at"] - ticket["created_at"])` |
| 보다 늦으면 | `if checked_time > ticket["sla_due"]:` |
| 1 늘려 다시 저장 | `late = late + 1` |
| 함수 결과를 변수에 저장 | `mean_ack_minutes = average(ack_times)` |

---

## 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기

<mark>문제가 아닙니다. 오늘 구현한 코드를 원격 저장소(remote repository, 리모트 리포지토리: 깃허브에 있는 저장소)에 반영하는 마무리입니다.</mark> 실습 7-2 마지막 약 10분에 진행합니다. 알림 서버를 켜지 않은, 처음 쓰던 터미널에서 진행합니다. 먼저 `pwd` 로 위치를 확인하고, 결과가 `soar_response` 로 끝나면 아래 1번의 `cd ..` 를 실행합니다.

**이런 상황이 있습니다**

- **지금은**: <mark>팀장이 「오늘 구현한 티켓 생성 · 병합 · 통지 · 에스컬레이션 · 지표 산출 코드를 저장소에 보관해 달라」고 요청합니다</mark>.
- **진행 내용**: 먼저 `git status` 로 반영할 파일을 점검합니다. `.env` 같은 비밀 키(API 키) 파일이 포함되면 누구나 볼 수 있게 공개되어 보안 사고가 되므로 반드시 제외합니다. 점검한 뒤 `git add` → `git commit` → `git push` 순서로 반영합니다.
- **끝나면**: 깃허브 저장소의 `soar_response` 폴더에 `ticketing.py` · `ticket_merge.py` · `ticket_notice.py` · `escalation.py` · `shift_metrics.py` 가 보입니다.

**순서**

0. **[터미널]** 오늘 구현한 파일이 있는지 `soar_response` 폴더에서 점검합니다. 두 명령을 하나씩 실행합니다. 이 단계에서 보고서(`report_u6.md` · `report_u7.md`)도 점검합니다. Unit 6과 Unit 7의 모든 질문에서 `답:` 뒤와 코드 상자가 모두 작성되었는지 확인합니다(마무리 (가)는 3번에서 작성합니다).

   ① 지금 위치를 확인합니다.

   ```bash
   pwd
   ```

   - 하는 일: 지금 있는 폴더의 위치를 보여 줍니다.
   - 나오는 것: <mark>`soar_response` 로 끝나야</mark> 합니다.

   ② 폴더 안의 파일을 봅니다.

   ```bash
   ls
   ```

   - 하는 일: 폴더 안의 파일 이름을 보여 줍니다.
   - 나오는 것: `ticketing.py` · `ticket_merge.py` · `ticket_notice.py` · `escalation.py` · `shift_metrics.py` · `report_u7.md` · `config` 가 보이면 됩니다.

1. **[터미널]** `security-agent-toolkit` 폴더로 옮깁니다. 0번의 `pwd` 결과가 `soar_response` 로 끝날 때만 `cd ..` 를 칩니다. 이미 `…/security-agent-toolkit` 으로 끝나면 `cd ..` 는 건너뛰고 `pwd` 만 칩니다.

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

2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark style="background:#ffc4d6">빨간 글씨 줄에 `.env` 나 `.venv` 가 보이면 올리지 않습니다.</mark> `.env` 는 API 키가 들어 있어 공개되면 안 되는 파일이고, `.venv` 는 크기가 커서 올릴 필요가 없는 가상환경 폴더입니다. 이때 아래 안내대로 `.gitignore`(깃이 올리지 않을 파일 이름을 적어 두는 파일)를 고친 뒤 `git status` 를 다시 봅니다.

   ① 올릴 파일의 상태를 봅니다.

   ```bash
   git status
   ```

   - 하는 일: 올릴 파일의 상태를 보여 줍니다.
   - 나오는 것: 바뀐 파일의 이름이 나옵니다. `soar_response/` 아래의 새 파일들이 보이면 됩니다.

   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` (파이썬이 실행하면서 자동으로 만드는 임시 폴더)가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 봅니다.

3. **[보고서]** `report_u7.md` 의 `## 마무리` 아래를 작성합니다. <mark>반영하기 전에 작성해야</mark> 깃허브에 빈 답이 없는 상태로 올라갑니다.
   - (가) `git status` 를 실행했을 때 `.env` 나 `.venv` 가 목록에 표시되었는지, 표시되었다면 어떤 조치를 했는지 적어 주세요.
   - <mark>Unit 6 · Unit 7에서 앞서 풀면서 답하지 못한 보고서 질문이 있으면 `모름 — 막힌 곳: …` 으로 적고 push 합니다.</mark> push 한 뒤에 이어서 작성하여 다시 push 해도 됩니다.
4. **[터미널]** 바뀐 파일을 올릴 목록에 추가하고(`add`), 설명을 붙여 저장하고(`commit`), 깃허브로 올립니다(`push`). 세 명령을 순서대로 하나씩 칩니다.

   ① 바뀐 파일을 모두 올릴 목록에 추가합니다.

   ```bash
   git add .
   ```

   - 하는 일: 바뀐 파일을 이번에 올릴 목록에 추가합니다.
   - 나오는 것: 아무것도 나오지 않습니다.

   ② 기록으로 저장합니다.

   ```bash
   git commit -m "Add ticketing, escalation and shift metrics"
   ```

   - 하는 일: 따옴표 안의 설명을 붙여 기록으로 저장합니다.
   - 나오는 것: 바뀐 파일 수가 적힌 줄이 나옵니다.

   ③ 깃허브로 올립니다.

   ```bash
   git push
   ```

   - 하는 일: 저장한 기록을 깃허브로 올립니다.
   - 나오는 것: 올라간 내용이 몇 줄 나옵니다.

   - <mark style="background:#ffc4d6">`git push` 가 거절(`rejected`)되면 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다.</mark> `git pull --no-rebase`(깃허브의 새 기록을 내 PC 로 받아 와 합치는 명령)를 입력한 뒤 `git push` 를 다시 합니다.
   - 편집기 화면이 뜨면 `Esc` → `:wq`(저장하고 나가기) → `Enter` 를 합니다.
   - `git pull` 만 입력했을 때 `fatal: Need to specify how to reconcile divergent branches` 가 나오면, 내 기록과 깃허브 기록이 갈라졌다는 뜻이므로 `git pull --no-rebase` 를 입력합니다.

5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `soar_response` 폴더를 열고, VS Code 왼쪽 목록의 `soar_response` 폴더에 있는 파일들이 깃허브에도 보이는지 확인합니다. <mark>`__pycache__` 폴더는 없어도 됩니다</mark>.
   - 깃허브에 안 보이는 파일이 있으면, 먼저 VS Code 왼쪽 목록의 `soar_response` 폴더 안에 그 파일이 있는지 봅니다.
     - 없으면 다른 폴더에 만든 것이니 `soar_response` 안으로 옮기고, `pwd` 로 위치를 확인한 뒤 2번의 `git status` 부터 다시 합니다.
6. **[터미널]** 알림 서버 터미널을 `Ctrl + C` 로 끕니다.

## 마무리 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 올릴 파일 확인 | `git status` (`.env` · `.venv` 가 보이면 멈춤) |
| 올리기 | `git add .` → `git commit -m "…"` → `git push` |
| 올린 뒤 | 브라우저에서 `soar_response` 폴더와 파일이 있는지 확인 |

---

## 이번 Unit 마무리

| 달성 기준 | 문제 |
|---|---|
| 응답 기한이 초과된 열림 상태 티켓을 초과 시간에 맞는 단계로 에스컬레이션했다 | 실습 7-1 |
| 근무 3시간 시뮬레이션을 실행하고 평균 확인 시간 · 평균 해결 시간 · 응답 기한 위반 수를 산출했다 | 실습 7-2 |
| 오늘 구현한 파일과 보고서를 깃허브에 반영했다 | 마무리 |

**강의계획서 평가 기준 확인**

| 기준 | 확인할 곳 |
|---|---|
| 티켓 생성 시 플레이북(playbook, 플레이북: 사건 종류별로 정해 둔 대응 순서) · 조치 내역이 자동으로 반영된다 | Unit 6의 실습 6-1 단계 3 (TCK-1 의 조치 내역), 티켓의 `playbook` · `done` |
| 에스컬레이션이 응답 기한(SLA) 기준에 따라 해당 단계의 상급자에게 통보된다 | 실습 7-1 단계 2 · 3 (기한을 넘긴 시간과 올림 단계), 실습 7-2 단계 1 의 70분 · 80분 · 110분 줄 |
| 알림 함수가 재사용되었다 | Unit 6의 실습 6-3 `ticket_notice.py` 의 `notify` (`notifier.py`), 알림 서버 터미널의 `[알림 받음]` |

오늘은 알림 서버(연습용 시스템)로 검증했습니다. <mark>실제 제품에서는 `notify` 가 알림 서버가 아니라 메신저 · 호출기(pager, 페이저: 담당자를 호출하는 알림 장치) · 티켓 관리 도구로 통지를 전송하는 경우가 많습니다.</mark> 응답 기한 계산, 에스컬레이션 단계, 평균 확인 시간 · 평균 해결 시간 계산 방식은 그대로 적용됩니다.

---

<!-- learn:answers -->
