---
id: m5-u04-l04
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

이 레슨의 두 파일은 **응용을 할 때만** 씁니다. 핵심 실습 4-1 · 4-2 에는 필요 없으니, 응용을 하지 않으면 이 레슨은 건너뜁니다.

| 파일 | 직접 써 보는 응용 | 이 파일을 불러 쓰는 응용 |
|---|---|---|
| `escalation.py` | 응용 4-1 | 응용 4-2 |
| `report.py` | 응용 4-3 | 응용 4-5 |

1. 응용 4-1 · 4-3 을 하면 그 레슨에서 이 파일을 빈칸이 있는 골격으로 만들어 직접 씁니다. 그때는 이 레슨을 건너뜁니다.
2. 응용 4-1 을 건너뛰고 응용 4-2 를 하려면 `escalation.py` 를, 응용 4-3 을 건너뛰고 응용 4-5 를 하려면 `report.py` 를 이 레슨의 완성본으로 만듭니다.
3. 파일은 `soar_response` 폴더 안에 만듭니다(VS Code 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File**). 코드 상자의 **복사** 버튼을 눌러 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
4. 다 만들었으면 아래 명령으로 확인합니다(맥북은 `python3`). 만든 파일의 줄만 칩니다.
   ```bash
   python -c "import escalation; print('escalation.py 정상')"
   python -c "import report; print('report.py 정상')"
   ```

확인할 때 오류가 나면 아래 표대로 하고 다시 확인합니다. 맥북은 `python3 -m pip` 로 칩니다.

| 오류 메시지 | 뜻 | 할 일 |
|---|---|---|
| `No module named 'ticket_notice'` | `escalation.py` 가 불러 쓰는 Unit 3 파일이 없음 | 응용 4-1 레슨의 「필요한 파일 준비하기」를 먼저 함 |
| `No module named 'requests'` | 도구가 설치되지 않음 | `python -m pip install flask requests` |
| `No module named 'pandas'` | 도구가 설치되지 않음 | `python -m pip install pandas` |

## `escalation.py` 만들기

**`escalation.py`** — 응답 기한(SLA)이 지났는데 아직 `열림` 상태인 티켓을 상급자에게 올립니다. 같은 단계는 한 번만 올립니다.

| 기한을 넘긴 시간 | 올림 단계 | 받는 사람 |
|---|---|---|
| 0분 이상 | 1단계 | `team.lead` |
| 30분 이상 | 2단계 | `soc.head` |

알림은 Unit 3 파일 `ticket_notice.py` 에 있는 `send_with_retry` 로 보냅니다.

```python
from ticket_notice import send_with_retry, MAX_TRIES                                       # Unit 3 에 있는 재시도 함수를 불러온다


def overdue_minutes(ticket, now):                                                          # 티켓과 지금 시각(분)을 받는 함수
    """응답 기한을 넘긴 시간(분)을 리턴한다. 기한이 아직 안 됐으면 음수가 나온다.
    얼마나 늦었는지 알아야 어느 상급자에게 올릴지 정할 수 있어서 쓴다.
    """
    return now - ticket["sla_due"]                                                         # 지금 시각에서 응답 기한 시각을 뺀 값을 리턴한다


def needs_escalation(ticket, now):                                                         # 티켓과 지금 시각(분)을 받는 함수
    """아직 열림 상태이고 응답 기한이 지났으면 True, 아니면 False 를 리턴한다. 담당자가 이미 확인 중이거나 해결한 티켓은 올리지 않는다.
    아무도 열어 보지 않은 티켓만 골라낼 때 쓴다.
    """
    if ticket["status"] != "열림":                                                         # 이미 확인 중이거나 해결한 티켓이면
        return False                                                                       # 올리지 않는다고 False 를 리턴한다
    return overdue_minutes(ticket, now) >= 0                                               # 기한이 지났는지의 결과를 리턴한다


def pick_level(overdue, steps):                                                            # 넘긴 시간과 올림 단계 리스트를 받는 함수
    """넘긴 시간에 해당하는 가장 높은 올림 단계 번호(1부터)를 리턴한다. 해당하는 단계가 없으면 0 을 리턴한다.
    오래 방치된 티켓일수록 더 높은 상급자에게 올릴 때 쓴다.
    """
    level = 0                                                                              # 처음에는 올릴 단계가 없다
    for index in range(len(steps)):                                                        # 단계 번호를 0 부터 하나씩 읽는다
        step = steps[index]                                                                # 그 번호의 올림 단계
        if overdue >= step["overdue_minutes"]:                                             # 넘긴 시간이 이 단계의 기준 이상이면
            level = index + 1                                                              # 이 단계 번호를 담는다 (뒤의 더 높은 단계가 덮어쓴다)
    return level                                                                           # 가장 높은 단계 번호를 리턴한다


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

- 함수 네 개의 뜻과 규칙 파일(`config/escalation_rules.json`)의 키는 응용 4-1 레슨에서 자세히 다룹니다.
- 응용 4-2 는 이 파일의 `needs_escalation` 과 `escalate_ticket` 을 불러 씁니다.

## `report.py` 만들기

**`report.py`** — 티켓 파일을 판다스 표로 바꿔 집계하고, 조치 기록과 대조해 초동 대응 리포트의 줄 리스트를 만듭니다. 리포트 파일을 실제로 쓰는 일은 응용 4-3 의 실행 파일이 합니다.

```python
import pandas as pd                                                                        # 표를 다루기 위해 판다스를 pd 라는 이름으로 불러온다

REPORT_TITLE = "# 초동 대응 리포트 — 2026-11-12(목) 오전 근무"                             # 리포트 맨 위 제목


def make_ticket_table(tickets):                                                            # 티켓 리스트를 받는 함수
    """티켓 리스트를 표(DataFrame)로 바꾸고, 확인까지 걸린 분(ack_minutes) 열을 더해 리턴한다.
    티켓마다 담당자가 얼마나 빨리 확인했는지를 표 하나로 계산할 때 쓴다.
    """
    table = pd.DataFrame(tickets)                                                          # 티켓 리스트를 표로 바꾼다
    table["ack_minutes"] = table["acked_at"] - table["created_at"]                         # 두 열을 빼서 확인까지 걸린 분 열을 만든다
    return table                                                                           # 열을 더한 표를 리턴한다


def count_by_rule(table):                                                                  # 티켓 표를 받는 함수
    """탐지 규칙마다 티켓이 몇 장인지 세어 딕셔너리로 리턴한다.
    어떤 규칙의 사건이 많았는지 리포트 첫머리에 보여 줄 때 쓴다.
    """
    rule_counts = table["rule"].value_counts()                                             # 규칙 열에서 값마다 개수를 센다
    return rule_counts.to_dict()                                                           # 센 결과를 딕셔너리로 바꿔 리턴한다


def mean_ack_by_grade(table):                                                              # 티켓 표를 받는 함수
    """확인한 티켓만 남겨 등급마다 확인까지 걸린 분의 평균을 구하고, 소수 첫째 자리까지 딕셔너리로 리턴한다.
    급한 등급일수록 빨리 확인했는지 리포트로 보여 줄 때 쓴다.
    """
    acked = table[table["acked_at"] >= 0]                                                  # 확인한 티켓(acked_at 이 0 이상)만 남긴다
    groups = acked.groupby("grade")                                                        # 등급이 같은 행끼리 묶는다
    grade_means = groups["ack_minutes"].mean()                                             # 등급마다 확인까지 걸린 분의 평균을 구한다
    rounded = grade_means.round(1)                                                         # 소수 첫째 자리까지 반올림한다
    return rounded.to_dict()                                                               # 등급별 평균을 딕셔너리로 바꿔 리턴한다


def find_late_tickets(table):                                                              # 티켓 표를 받는 함수
    """응답 기한 시각(sla_due)보다 늦게 확인한 티켓을 딕셔너리 리스트로 리턴한다.
    응답 기한을 넘긴 티켓을 리포트에 이름으로 남길 때 쓴다.
    """
    late = table[table["acked_at"] > table["sla_due"]]                                     # 응답 기한 시각보다 늦게 확인한 행만 남긴다
    return late.to_dict("records")                                                         # 남은 행을 딕셔너리 리스트로 바꿔 리턴한다


def find_missing_incidents(actions, tickets):                                              # 조치 기록 리스트와 티켓 리스트를 받는 함수
    """조치 기록 가운데 어느 티켓에도 들어 있지 않은 인시던트의 기록을 리스트로 리턴한다.
    조치는 했는데 티켓이 없어 리포트에서 빠지는 사건을 찾을 때 쓴다.
    """
    covered = []                                                                           # 티켓에 들어 있는 인시던트 번호를 모을 빈 리스트
    for ticket in tickets:                                                                 # 티켓을 하나씩 읽는다
        for incident_id in ticket["incidents"]:                                            # 티켓에 합쳐진 인시던트 번호를 하나씩 읽는다
            covered.append(incident_id)                                                    # 번호를 추가한다
    missing = []                                                                           # 티켓이 없는 조치 기록을 모을 빈 리스트
    for action in actions:                                                                 # 조치 기록을 하나씩 읽는다
        if action["incident"] not in covered:                                              # 티켓에 없는 인시던트이면
            missing.append(action)                                                         # 그 조치 기록을 추가한다
    return missing                                                                         # 티켓이 없는 조치 기록 리스트를 리턴한다


def count_actions(ticket, actions):                                                        # 티켓 한 장과 조치 기록 리스트를 받는 함수
    """티켓에 합쳐진 인시던트의 조치 기록이 몇 건인지 세어 리턴한다.
    리포트의 티켓 줄에 조치 기록 수를 함께 적을 때 쓴다.
    """
    count = 0                                                                              # 조치 기록 수 : 처음에는 0
    for action in actions:                                                                 # 조치 기록을 하나씩 읽는다
        if action["incident"] in ticket["incidents"]:                                      # 이 티켓의 인시던트 기록이면
            count = count + 1                                                              # 1 늘린다
    return count                                                                           # 센 수를 리턴한다


def make_timeline_line(ticket):                                                            # 티켓 한 장을 받는 함수
    """티켓 한 장의 생성 · 확인 · 해결 시각을 시간순으로 이은 한 줄을 리턴한다.
    높음 등급 사건이 어떤 순서로 처리됐는지 리포트에 처리 경위로 남길 때 쓴다.
    """
    steps = [str(ticket["created_at"]) + "분 티켓 생성"]                                   # 생성 시각으로 시작한다
    if ticket["acked_at"] >= 0:                                                            # 확인했으면 (확인 전이면 -1)
        steps.append(str(ticket["acked_at"]) + "분 담당자 확인")                           # 확인 시각을 추가한다
    if ticket["resolved_at"] >= 0:                                                         # 해결했으면 (해결 전이면 -1)
        steps.append(str(ticket["resolved_at"]) + "분 해결")                               # 해결 시각을 추가한다
    return "- " + ticket["id"] + " · " + ticket["entity"] + ": " + " → ".join(steps)       # 시각을 화살표로 이어 한 줄로 리턴한다


def make_report_lines(tickets, actions, rule_counts, grade_means, late_tickets, missing):  # 리포트에 넣을 재료를 받는 함수
    """리포트에 넣을 재료로 마크다운 문서의 줄 리스트를 만들어 리턴한다.
    근무가 끝난 뒤 사람이 읽을 초동 대응 리포트를 자동으로 쓸 때 쓴다.
    """
    lines = [REPORT_TITLE, ""]                                                             # 제목과 빈 줄로 시작한다
    lines.append("## 1. 티켓별 초동 대응")                                                 # 1절 제목
    for ticket in tickets:                                                                 # 티켓을 하나씩 읽는다
        action_count = count_actions(ticket, actions)                                      # 이 티켓의 조치 기록 수
        head = "- " + ticket["id"] + " [" + ticket["grade"] + "] " + ticket["entity"] + " — " + ticket["rule"]  # 티켓 번호 · 등급 · 대상 · 규칙
        lines.append(head + " · 상태 " + ticket["status"] + " · 조치 기록 " + str(action_count) + "건")  # 티켓 한 줄을 추가한다
    lines.append("")                                                                       # 빈 줄
    lines.append("## 2. 규칙별 티켓 수")                                                   # 2절 제목
    for rule in rule_counts:                                                               # 규칙 이름을 하나씩 읽는다
        count = rule_counts[rule]                                                          # 그 규칙의 티켓 수
        lines.append("- " + rule + ": " + str(count) + "장")                               # 규칙 한 줄을 추가한다
    lines.append("")                                                                       # 빈 줄
    lines.append("## 3. 등급별 평균 확인 시간(분)")                                        # 3절 제목
    for grade in grade_means:                                                              # 등급을 하나씩 읽는다
        lines.append("- " + grade + ": " + str(grade_means[grade]) + "분")                 # 등급 한 줄을 추가한다
    lines.append("")                                                                       # 빈 줄
    lines.append("## 4. 응답 기한을 넘겨 확인한 티켓")                                     # 4절 제목
    for ticket in late_tickets:                                                            # 늦게 확인한 티켓을 하나씩 읽는다
        lines.append("- " + ticket["id"] + " · 기한 " + str(ticket["sla_due"]) + "분 · 확인 " + str(ticket["acked_at"]) + "분")  # 티켓 한 줄을 추가한다
    lines.append("")                                                                       # 빈 줄
    lines.append("## 5. 티켓이 없는 조치 (사람이 티켓을 만들어야 함)")                     # 5절 제목
    for action in missing:                                                                 # 티켓이 없는 조치 기록을 하나씩 읽는다
        lines.append("- " + action["incident"] + " · " + action["action"] + " · " + action["target"])  # 기록 한 줄을 추가한다
    lines.append("")                                                                       # 빈 줄
    lines.append("## 6. 높음(high) 티켓의 처리 경위")                                      # 6절 제목
    for ticket in tickets:                                                                 # 티켓을 하나씩 읽는다
        if ticket["grade"] == "high":                                                      # 높음 등급 티켓이면
            lines.append(make_timeline_line(ticket))                                       # 처리 경위 한 줄을 추가한다
    return lines                                                                           # 완성한 줄 리스트를 리턴한다
```

- 함수마다 하는 일과 판다스 문법은 응용 4-3 레슨에서 자세히 다룹니다.
- 응용 4-5 는 이 파일의 `find_missing_incidents` 를 불러 씁니다. 응용 4-5 가 읽는 리포트 파일 `incident_report_20261112.md` 는 응용 4-5 레슨에서 만드는 방법을 알려 줍니다.
