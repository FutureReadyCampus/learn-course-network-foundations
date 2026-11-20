---
id: m5-u04-l04
title: 제공 파일
render: markdown
---

# 제공 파일

## `escalation.py` 만들기

TODO(assemble): `escalation.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

```python
from ticket_notice import send_with_retry, MAX_TRIES                                       # 도전 3-3에 만든 재시도 함수를 불러온다


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

## `report.py` 만들기

TODO(assemble): `report.py` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.

```python
import pandas as pd                                                                        # 표를 다루기 위해 판다스를 pd 라는 이름으로 불러온다

REPORT_TITLE = "# 초동 대응 리포트 — 2026-11-12(목) 오전 근무"                             # 리포트 맨 위 제목


def make_ticket_table(tickets):                                                            # 티켓 리스트를 받는 함수
    """티켓 리스트를 표(DataFrame)로 바꾸고, 확인까지 걸린 분(ack_minutes) 열을 더해 리턴한다.
    티켓마다 담당자가 얼마나 빨리 확인했는지를 표 하나로 계산할 때 쓴다.
    """
    table = pd.DataFrame(tickets)                                                          # 티켓 리스트를 표로 바꾼다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. table["acked_at"] - table["created_at"] 를 table["ack_minutes"] 에 저장한다 (확인까지 걸린 분)
    return table                                                                           # 열을 더한 표를 리턴한다 — 미리 채운 줄


def count_by_rule(table):                                                                  # 티켓 표를 받는 함수
    """탐지 규칙마다 티켓이 몇 장인지 세어 딕셔너리로 리턴한다.
    어떤 규칙의 사건이 많았는지 리포트 첫머리에 보여 줄 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. table["rule"].value_counts() 를 rule_counts 에 저장한다
    return rule_counts.to_dict()                                                           # 센 결과를 딕셔너리로 바꿔 리턴한다 — 미리 채운 줄


def mean_ack_by_grade(table):                                                              # 티켓 표를 받는 함수
    """확인한 티켓만 남겨 등급마다 확인까지 걸린 분의 평균을 구하고, 소수 첫째 자리까지 딕셔너리로 리턴한다.
    급한 등급일수록 빨리 확인했는지 리포트로 보여 줄 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 3. table["acked_at"] >= 0 인 행만 남겨 acked 에 저장한다 (확인한 티켓만)
    groups = acked.groupby("grade")                                                        # 등급이 같은 행끼리 묶는다 — 미리 채운 줄
    # 4. groups["ack_minutes"].mean() 을 grade_means 에 저장한다 (등급마다 평균)
    rounded = grade_means.round(1)                                                         # 소수 첫째 자리까지 반올림한다 — 미리 채운 줄
    return rounded.to_dict()                                                               # 등급별 평균을 딕셔너리로 바꿔 리턴한다 — 미리 채운 줄


def find_late_tickets(table):                                                              # 티켓 표를 받는 함수
    """응답 기한 시각(sla_due)보다 늦게 확인한 티켓을 딕셔너리 리스트로 리턴한다.
    응답 기한을 넘긴 티켓을 리포트에 이름으로 남길 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. table["acked_at"] > table["sla_due"] 인 행만 남겨 late 에 저장한다
    return late.to_dict("records")                                                         # 남은 행을 딕셔너리 리스트로 바꿔 리턴한다 — 미리 채운 줄


def find_missing_incidents(actions, tickets):                                              # 조치 기록 리스트와 티켓 리스트를 받는 함수
    """조치 기록 가운데 어느 티켓에도 들어 있지 않은 인시던트의 기록을 리스트로 리턴한다.
    조치는 했는데 티켓이 없어 리포트에서 빠지는 사건을 찾을 때 쓴다.
    """
    covered = []                                                                           # 티켓에 들어 있는 인시던트 번호를 모을 빈 리스트 — 미리 채운 줄
    for ticket in tickets:                                                                 # 티켓을 하나씩 읽는다 — 미리 채운 줄
        for incident_id in ticket["incidents"]:                                            # 티켓에 합쳐진 인시던트 번호를 하나씩 읽는다 — 미리 채운 줄
            covered.append(incident_id)                                                    # 번호를 추가한다 — 미리 채운 줄
    missing = []                                                                           # 티켓이 없는 조치 기록을 모을 빈 리스트 — 미리 채운 줄
    for action in actions:                                                                 # 조치 기록을 하나씩 읽는다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 6. action["incident"] 가 covered 안에 없으면 (if, not in)
            # 7. missing 에 action 을 추가한다 (append)
    return missing                                                                         # 티켓이 없는 조치 기록 리스트를 리턴한다 — 미리 채운 줄


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
    lines = [REPORT_TITLE, ""]                                                             # 제목과 빈 줄로 시작한다 — 미리 채운 줄
    lines.append("## 1. 티켓별 초동 대응")                                                 # 1절 제목 — 미리 채운 줄
    for ticket in tickets:                                                                 # 티켓을 하나씩 읽는다 — 미리 채운 줄
        action_count = count_actions(ticket, actions)                                      # 이 티켓의 조치 기록 수 — 미리 채운 줄
        head = "- " + ticket["id"] + " [" + ticket["grade"] + "] " + ticket["entity"] + " — " + ticket["rule"]  # 티켓 번호 · 등급 · 대상 · 규칙 — 미리 채운 줄
        lines.append(head + " · 상태 " + ticket["status"] + " · 조치 기록 " + str(action_count) + "건")  # 티켓 한 줄을 추가한다 — 미리 채운 줄
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 2. 규칙별 티켓 수")                                                   # 2절 제목 — 미리 채운 줄
    for rule in rule_counts:                                                               # 규칙 이름을 하나씩 읽는다 — 미리 채운 줄
        count = rule_counts[rule]                                                          # 그 규칙의 티켓 수 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 8. "- " + rule + ": " + str(count) + "장" 을 lines 에 추가한다 (append)
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 3. 등급별 평균 확인 시간(분)")                                        # 3절 제목 — 미리 채운 줄
    for grade in grade_means:                                                              # 등급을 하나씩 읽는다 — 미리 채운 줄
        lines.append("- " + grade + ": " + str(grade_means[grade]) + "분")                 # 등급 한 줄을 추가한다 — 미리 채운 줄
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 4. 응답 기한을 넘겨 확인한 티켓")                                     # 4절 제목 — 미리 채운 줄
    for ticket in late_tickets:                                                            # 늦게 확인한 티켓을 하나씩 읽는다 — 미리 채운 줄
        lines.append("- " + ticket["id"] + " · 기한 " + str(ticket["sla_due"]) + "분 · 확인 " + str(ticket["acked_at"]) + "분")  # 티켓 한 줄을 추가한다 — 미리 채운 줄
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 5. 티켓이 없는 조치 (사람이 티켓을 만들어야 함)")                     # 5절 제목 — 미리 채운 줄
    for action in missing:                                                                 # 티켓이 없는 조치 기록을 하나씩 읽는다 — 미리 채운 줄
        lines.append("- " + action["incident"] + " · " + action["action"] + " · " + action["target"])  # 기록 한 줄을 추가한다 — 미리 채운 줄
    lines.append("")                                                                       # 빈 줄 — 미리 채운 줄
    lines.append("## 6. 높음(high) 티켓의 처리 경위")                                      # 6절 제목 — 미리 채운 줄
    for ticket in tickets:                                                                 # 티켓을 하나씩 읽는다 — 미리 채운 줄
        if ticket["grade"] == "high":                                                      # 높음 등급 티켓이면 — 미리 채운 줄
            lines.append(make_timeline_line(ticket))                                       # 처리 경위 한 줄을 추가한다 — 미리 채운 줄
    return lines                                                                           # 완성한 줄 리스트를 리턴한다 — 미리 채운 줄
```
