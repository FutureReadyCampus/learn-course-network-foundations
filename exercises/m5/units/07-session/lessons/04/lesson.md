---
id: m5-u07-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/128_day04_pm_escalation_metrics.md
  mission_id: GichanSource.m5-1112-pm-escalation-metrics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답을 보는 방법

아래 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## 실습 7-1 정답

 **터미널에 입력합니다.** 알림 서버 터미널은 켜 둔 채, 처음 쓰던 터미널에서 실행합니다.

```bash
pwd
python exercise7-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`escalation.py` 의 1 ~ 6번입니다.

```python
    # 1. now 에서 ticket["sla_due"] 를 뺀 값을 리턴한다
    return now - ticket["sla_due"]              # 지금 시각에서 응답 기한 시각을 뺀 값을 리턴한다
    # 2. ticket 의 "status" 가 "열림" 이 아니면 (if, !=)
    if ticket["status"] != "열림":              # 이미 확인 중이거나 해결한 티켓이면
    # 3.   False 를 리턴한다
        return False                            # 올리지 않는다고 False 를 리턴한다
    # 4. overdue_minutes(ticket, now) 가 0 이상인지(>=)의 결과를 리턴한다
    return overdue_minutes(ticket, now) >= 0    # 기한이 지났는지의 결과를 리턴한다
        # 5. overdue 가 step 의 "overdue_minutes" 이상이면 (if, >=)
        if overdue >= step["overdue_minutes"]:  # 넘긴 시간이 이 단계의 기준 이상이면
            # 6. level 에 index + 1 을 저장한다
            level = index + 1                   # 이 단계 번호를 담는다 (뒤의 더 높은 단계가 덮어쓴다)
```

`exercise7-1_run.py` 의 7 ~ 9번입니다.

```python
        # 7. needs_escalation(ticket, now) 가 참이면 (if)
        if needs_escalation(ticket, now):                 # 상급자에게 올릴 티켓이면
            # 8. escalate_ticket(ticket, now, rules) 의 결과를 result 에 저장한다
            result = escalate_ticket(ticket, now, rules)  # 상급자에게 올리고 결과를 받는다
                # 9. escalated_count 에 escalated_count + 1 을 저장한다 (1 늘린다)
                escalated_count = escalated_count + 1     # 올린 횟수를 1 늘린다
```

위 줄만 보면 들여쓰기가 헷갈리니 완성된 모양을 함께 봅니다. 7번의 `if` 아래에는 8번 줄과 미리 채운 세 줄이 들어갑니다. 9번은 미리 채운 `if result == "올림":` 아래에 들어갑니다.

**전체 모양 — 점검 반복 부분**

```python
for now in [20, 60, 110]:                                           # 점검할 시각(분)을 하나씩 읽는다
    print("[" + str(now) + "분] 점검")                              # 점검 시각을 출력한다
    for ticket in tickets:                                          # 티켓을 하나씩 읽는다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        if needs_escalation(ticket, now):                           # 상급자에게 올릴 티켓이면
            result = escalate_ticket(ticket, now, rules)            # 상급자에게 올리고 결과를 받는다
            overdue = overdue_minutes(ticket, now)                  # 기한을 얼마나 넘겼는지 구한다 — 미리 채운 줄
            print(ticket["id"], ticket["title"], "→", result, "· 기한을", overdue, "분 넘김 · 올림 단계", ticket["escalation_level"])  # 결과를 출력한다 — 미리 채운 줄
            if result == "올림":                                    # 올렸으면 — 미리 채운 줄
                escalated_count = escalated_count + 1               # 올린 횟수를 1 늘린다
    if now == 20:                                                   # 20분 점검이 끝나면 — 미리 채운 줄
        change_ticket_status(tickets[0], "확인 중", 25, "kim.sec")  # 25분에 kim.sec 이 TCK-1 을 확인하기 시작한다 — 미리 채운 줄
        print("[25분] TCK-1 → 확인 중 · kim.sec")                   # 담당자의 동작을 출력한다 — 미리 채운 줄
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 3 의 올린 횟수(에스컬레이션 실행 횟수)는 <mark style="background:#bde3ff">**4번**</mark>입니다.

```
--- 단계 1: 불러온 티켓 7 장 · 올림 단계 2 개
--- 단계 2: 점검 시각마다 상급자에게 올릴 티켓 찾기
[20분] 점검
TCK-1 [high] dami — 퇴사한 계정 → 올림 · 기한을 5 분 넘김 · 올림 단계 1
[25분] TCK-1 → 확인 중 · kim.sec
[60분] 점검
[110분] 점검
TCK-3 [mid] gaeun — 규칙은 허용인데 서버가 거절 → 올림 · 기한을 42 분 넘김 · 올림 단계 2
TCK-4 [mid] seoyeon — 대량 다운로드 → 올림 · 기한을 38 분 넘김 · 올림 단계 2
TCK-6 [mid] hana — 업무 시간 밖 로그인 → 올림 · 기한을 15 분 넘김 · 올림 단계 1
--- 단계 3: 올린 결과 요약 (올린 횟수 4 번)
TCK-1 올림 단계 1 · 상태 확인 중
TCK-3 올림 단계 2 · 상태 열림
TCK-4 올림 단계 2 · 상태 열림
TCK-6 올림 단계 1 · 상태 열림
```

알림 서버 터미널에는 `[알림 받음]` 줄이 <mark style="background:#bde3ff">**4개**</mark> 찍힙니다.

```
[알림 받음] [올림 1단계] TCK-1 [high] dami — 퇴사한 계정 · 기한을 5분 넘김 · 받는 사람: team.lead
[알림 받음] [올림 2단계] TCK-3 [mid] gaeun — 규칙은 허용인데 서버가 거절 · 기한을 42분 넘김 · 받는 사람: soc.head
[알림 받음] [올림 2단계] TCK-4 [mid] seoyeon — 대량 다운로드 · 기한을 38분 넘김 · 받는 사람: soc.head
[알림 받음] [올림 1단계] TCK-6 [mid] hana — 업무 시간 밖 로그인 · 기한을 15분 넘김 · 받는 사람: team.lead
```

- (나) `TCK-1` 은 응답 기한(15분)이 지난 20분 점검에서 5분을 초과했으므로 1단계로 에스컬레이션되었습니다. 그 뒤 25분에 `kim.sec` 이 상태를 `확인 중` 으로 변경했습니다.
  - 60분 점검에서 `TCK-1` 의 상태는 `확인 중` 입니다. `needs_escalation` 은 상태가 `열림` 이 아니면 `False` 를 리턴하므로 <mark style="background:#bde3ff">에스컬레이션하지 않았습니다.</mark>
  - 이 조건이 없으면 담당자가 이미 확인 중인 티켓도 점검할 때마다 상급자에게 통보됩니다. 그러면 불필요한 알림이 늘어나고, 상급자가 알림 피로를 겪어 알림을 무시하게 됩니다.
- (다) 110분 점검에서 `TCK-3` 은 응답 기한 시각이 68분이므로 110 − 68 = 42분을 초과하여 <mark style="background:#bde3ff">2단계</mark>로 에스컬레이션되었습니다. `TCK-6` 은 응답 기한 시각이 95분이므로 110 − 95 = 15분을 초과하여 <mark style="background:#bde3ff">1단계</mark>로 에스컬레이션되었습니다.
  - <mark style="background:#ffdcb0">응답 기한 초과 시간이 30분 이상이면 2단계(`soc.head`, 관제 센터장), 0분 이상 30분 미만이면 1단계(`team.lead`, 팀장)</mark>입니다. <mark style="background:#bde3ff">42분은 30분 이상이므로 2단계이고, 15분은 30분 미만이므로 1단계입니다</mark>.
  - `TCK-2` 는 등급 low 이므로 응답 기한 시각이 243분입니다. 110분은 그보다 이르므로 초과 시간이 110 − 243 = −133분으로 음수입니다. 응답 기한이 아직 지나지 않았으므로 에스컬레이션 대상이 아닙니다.

**왜**

- <mark>에스컬레이션은 「확인되지 않은 티켓이 방치되어 응답 기한을 위반하는 일」을 막는 절차입니다.</mark> `열림` 상태인 티켓만 에스컬레이션하고 같은 단계는 한 번만 실행해야 불필요한 알림이 늘어나지 않습니다. 그래야 알림 피로 없이 상급자가 실제로 필요한 알림에 반응할 수 있습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 `None`(값이 없다는 뜻의 파이썬 값)이 리턴되어 기한을 비교하는 줄에서 오류가 납니다.

```
TypeError: '>=' not supported between instances of 'NoneType' and 'int'
```

- 2 · 3번을 비워 두면 <mark style="background:#ffc4d6">**확인 중인 티켓도 반복해서 에스컬레이션됩니다.**</mark> 아래 출력이 그 결과입니다. 60분 점검에서 `TCK-1` 이 2단계로 에스컬레이션되고, 110분 점검에서도 `TCK-1` 의 출력 줄이 나옵니다.

```
[60분] 점검
TCK-1 [high] dami — 퇴사한 계정 → 올림 · 기한을 45 분 넘김 · 올림 단계 2
[110분] 점검
TCK-1 [high] dami — 퇴사한 계정 → 그대로 · 기한을 95 분 넘김 · 올림 단계 2
```

- 3번만 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. `IndentationError`(들여쓰기가 맞지 않다는 오류)로 시작하는 오류입니다(문구는 파이썬 버전마다 조금 다릅니다).

```
IndentationError: expected an indented block
```

- 4번을 비워 두면 `needs_escalation` 이 값을 리턴하지 않아(`None`) <mark style="background:#ffc4d6">**에스컬레이션이 한 건도 실행되지 않습니다.**</mark> 단계 3 의 올린 횟수가 0번으로 출력되는 것이 이 실수의 결과입니다.

```
--- 단계 3: 올린 결과 요약 (올린 횟수 0 번)
```

- 5번을 비워 두면 6번의 줄이 `if` 없이 들여쓰기만 남아 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- 6번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다.

```
IndentationError: expected an indented block
```

- 7번을 비워 두면 <mark style="background:#ffc4d6">**기한 이전의 티켓도 모두 처리 대상이 됩니다.**</mark> 응답 기한에 도달하지 않은 티켓의 줄이 음수의 초과 시간과 함께 출력되는 것이 이 실수의 결과입니다.

```
[20분] 점검
TCK-1 [high] dami — 퇴사한 계정 → 올림 · 기한을 5 분 넘김 · 올림 단계 1
TCK-2 [low] 198.51.100.90 — 경로 스캔 → 그대로 · 기한을 -223 분 넘김 · 올림 단계 0
```

- 8번을 비워 두면 `result` 가 만들어지지 않아 오류가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'result' is not defined
```

- 9번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다.

```
IndentationError: expected an indented block
```

- 알림 서버를 켜지 않고 실행하면 코드는 정상이어도 <mark style="background:#ffc4d6">**상급자에게 통보하지 못합니다.**</mark> 단계 2 의 시작이 이렇게 출력되면 알림 서버가 실행 중이 아닌 것입니다.

```
--- 단계 2: 점검 시각마다 상급자에게 올릴 티켓 찾기
[20분] 점검
[알림 실패] ConnectionError
[알림 실패] ConnectionError
[알림 실패] ConnectionError
```

**관제에서는**

- 에스컬레이션 규칙(escalation policy, 에스컬레이션 폴리시: 어느 시점에 누구에게 통보할지 정한 규칙)은 「응답 기한 초과 시간이 몇 분이면 누구에게 통보하는가」를 표로 정의해 둡니다. 이 표가 있으면 사람이 판단하지 않아도 윗단계에 자동으로 통보하도록 설정할 수 있습니다.
- <mark>이미 담당자가 확인 중인 티켓은 에스컬레이션하지 않는 것</mark>이 기본 설계입니다. 이렇게 하면 알림이 불필요하게 늘어 상급자가 알림을 무시하게 되는 일(알림 피로)을 줄일 수 있습니다. <mark style="background:#ffdcb0">오늘의 0분 · 30분 기준은 예시입니다</mark>.

---

## 실습 7-2 정답

 **터미널에 입력합니다.** 알림 서버 터미널은 켜 둔 채, 처음 쓰던 터미널에서 실행합니다.

```bash
pwd
python exercise7-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`shift_metrics.py` 의 1 ~ 7번입니다.

```python
    # 1. numbers 의 개수(len)가 0 이면 (if, ==)
    if len(numbers) == 0:                                            # 숫자가 하나도 없으면
    # 2.   0 을 리턴한다 (비어 있으면 나눌 수 없다)
        return 0                                                     # 0 을 리턴한다
    # 3. sum(numbers) / len(numbers) 를 리턴한다 (합계를 개수로 나눈다)
    return sum(numbers) / len(numbers)                               # 합계를 개수로 나눈 평균을 리턴한다
        # 4. ticket 의 "acked_at" 이 -1 이 아니면 (if, !=)
        if ticket["acked_at"] != -1:                                 # 담당자가 확인한 티켓이면
            # 5. times 리스트에 ticket["acked_at"] - ticket["created_at"] 을 추가한다 (append)
            times.append(ticket["acked_at"] - ticket["created_at"])  # 확인까지 걸린 시간을 추가한다
        # 6. checked_time 이 ticket 의 "sla_due" 보다 크면 (if, >)
        if checked_time > ticket["sla_due"]:                         # 확인한 시각이 응답 기한 시각보다 늦으면
            # 7. late 에 late + 1 을 저장한다 (1 늘린다)
            late = late + 1                                          # 기한을 넘긴 티켓 수를 1 늘린다
```

`exercise7-2_run.py` 의 8 · 9번입니다.

```python
# 8. collect_response_times(tickets) 의 결과를 ack_times 에 저장한다
ack_times = collect_response_times(tickets)  # 확인까지 걸린 시간 리스트를 만든다
# 9. average(ack_times) 의 결과를 mean_ack_minutes 에 저장한다
mean_ack_minutes = average(ack_times)        # 평균 확인 시간(MTTA)을 구한다
```

**결과**

- (가) 출력은 다음과 같습니다. 평균 확인 시간(MTTA)은 <mark style="background:#bde3ff">**55.0분**</mark>, 평균 해결 시간(MTTR)은 <mark style="background:#bde3ff">**84.0분**</mark>, 응답 기한을 넘긴 티켓(응답 기한 위반)은 <mark style="background:#bde3ff">**2장**</mark>입니다.

```
--- 단계 1: 가상 근무 0분부터 180분까지 (알림 11 건 · 담당자 동작 8 건)
[0분] INC-201 → TCK-1 새 티켓 · 알리기 전송
[3분] INC-202 → TCK-2 새 티켓 · 알리기 전송
[8분] INC-203 → TCK-3 새 티켓 · 알리기 전송
[10분] TCK-1 → 확인 중 · kim.sec
[12분] INC-204 → TCK-4 새 티켓 · 알리기 전송
[14분] INC-205 → TCK-1 병합 · 알리기 건너뜀
[20분] INC-206 → TCK-2 병합 · 알리기 건너뜀
[30분] INC-207 → TCK-5 새 티켓 · 알리기 전송
[35분] INC-208 → TCK-6 새 티켓 · 알리기 전송
[40분] INC-209 → TCK-1 병합 · 알리기 전송
[45분] TCK-1 → 해결 · kim.sec
[70분] TCK-3 상급자에게 올림 · 올림 단계 1
[80분] TCK-3 → 확인 중 · lee.soc
[80분] TCK-4 상급자에게 올림 · 올림 단계 1
[90분] TCK-6 → 확인 중 · kim.sec
[95분] INC-210 → TCK-7 새 티켓 · 알리기 전송
[105분] TCK-7 → 확인 중 · kim.sec
[110분] TCK-4 상급자에게 올림 · 올림 단계 2
[120분] TCK-3 → 해결 · lee.soc
[130분] TCK-6 → 해결 · kim.sec
[140분] TCK-4 → 확인 중 · lee.soc
[160분] INC-211 → TCK-7 병합 · 알리기 전송
--- 단계 2: 근무 지표
티켓 7 장 · 확인한 티켓 5 장 · 해결한 티켓 3 장
평균 확인 시간(MTTA): 55.0 분
평균 해결 시간(MTTR): 84.0 분
응답 기한을 넘긴 티켓: 2 장
--- 단계 3: 다음 근무자에게 넘길 티켓 (해결되지 않은 티켓)
TCK-2 [low] 198.51.100.90 — 경로 스캔 · 상태 열림 · 조치 결과가 맞는지 확인하고 계정이나 IP 상태를 점검한다
TCK-4 [mid] seoyeon — 대량 다운로드 · 상태 확인 중 · 승인할지 거절할지 정하고 정한 사람의 이름을 남긴다
TCK-5 [low] 203.0.113.250 — 경로 스캔 · 상태 열림 · 조치가 확인되지 않았다. 담당자가 직접 계정이나 IP 상태를 보고 조치한다
TCK-7 [high] dami — 퇴사한 계정 · 상태 확인 중 · 조치 결과가 맞는지 확인하고 계정이나 IP 상태를 점검한다
--- 단계 4: 파일에 저장된 티켓 7 장
```

알림 서버 터미널에는 `[알림 받음]` 줄이 <mark style="background:#bde3ff">**12개**</mark> 찍힙니다(담당자에게 알린 9개와 상급자에게 올린 3개).

```
[알림 받음] [high] dami — 퇴사한 계정 · TCK-1 · 알림 1건 · 기한 15분 · 수신: kim.sec, lee.soc, team.lead
[알림 받음] [low] 198.51.100.90 — 경로 스캔 · TCK-2 · 알림 1건 · 기한 243분 · 수신: kim.sec
[알림 받음] [mid] gaeun — 규칙은 허용인데 서버가 거절 · TCK-3 · 알림 1건 · 기한 68분 · 수신: kim.sec, lee.soc
[알림 받음] [mid] seoyeon — 대량 다운로드 · TCK-4 · 알림 1건 · 기한 72분 · 수신: kim.sec, lee.soc
[알림 받음] [low] 203.0.113.250 — 경로 스캔 · TCK-5 · 알림 1건 · 기한 270분 · 수신: kim.sec
[알림 받음] [mid] hana — 업무 시간 밖 로그인 · TCK-6 · 알림 1건 · 기한 95분 · 수신: kim.sec, lee.soc
[알림 받음] [high] dami — 퇴사한 계정 · TCK-1 · 알림 3건 · 기한 15분 · 수신: kim.sec, lee.soc, team.lead
[알림 받음] [올림 1단계] TCK-3 [mid] gaeun — 규칙은 허용인데 서버가 거절 · 기한을 2분 넘김 · 받는 사람: team.lead
[알림 받음] [올림 1단계] TCK-4 [mid] seoyeon — 대량 다운로드 · 기한을 8분 넘김 · 받는 사람: team.lead
[알림 받음] [high] dami — 퇴사한 계정 · TCK-7 · 알림 1건 · 기한 110분 · 수신: kim.sec, lee.soc, team.lead
[알림 받음] [올림 2단계] TCK-4 [mid] seoyeon — 대량 다운로드 · 기한을 38분 넘김 · 받는 사람: soc.head
[알림 받음] [high] dami — 퇴사한 계정 · TCK-7 · 알림 2건 · 기한 110분 · 수신: kim.sec, lee.soc, team.lead
```

- (나) 확인한 티켓 5장의 확인 시간은 다음과 같습니다.
  - `TCK-1` 10 − 0 = 10분, `TCK-3` 80 − 8 = 72분, `TCK-4` 140 − 12 = 128분, `TCK-6` 90 − 35 = 55분, `TCK-7` 105 − 95 = 10분입니다.
  - 합계 275분을 5로 나누면 <mark style="background:#bde3ff">55.0분</mark>입니다.
  - `TCK-2` 와 `TCK-5` 는 아직 확인되지 않아 확인 시간 값이 없습니다(결측값, missing value: 아직 측정되지 않은 값). 이 값을 0분으로 넣으면 평균 확인 시간이 실제보다 낮아져 대응이 빠른 것처럼 잘못 보입니다.
- (다) 응답 기한을 위반한 티켓은 <mark style="background:#bde3ff">`TCK-3`</mark>(응답 기한 시각 68분, 80분에 확인)과 <mark style="background:#bde3ff">`TCK-4`</mark>(응답 기한 시각 72분, 140분에 확인)입니다. 각각 12분, 68분 늦게 확인되었습니다.
  - `TCK-3` 은 70분 점검에서 1단계로 에스컬레이션되었고, 80분에 `lee.soc` 이 확인했습니다.
  - `TCK-4` 는 80분에 1단계, 110분에 2단계로 에스컬레이션되었고, 140분에야 확인되었습니다.
  - 오늘 샘플에서는 에스컬레이션된 티켓(`TCK-3` · `TCK-4`)과 응답 기한 위반 티켓이 같습니다. 그러나 두 집합은 항상 같지는 않습니다. 에스컬레이션 대상은 응답 기한을 초과한 뒤 점검 시각까지 `열림` 으로 남은 티켓입니다. 응답 기한 위반은 확인 시각이 기한 시각보다 늦은 티켓입니다. 예를 들어 기한을 넘긴 뒤 다음 점검 전에 확인된 티켓은 에스컬레이션되지 않지만 위반으로는 셉니다.

**왜**

- <mark>평균 확인 시간 · 평균 해결 시간 · 응답 기한 위반 수는 「팀이 얼마나 빨리 대응했는가」를 숫자로 보여 줍니다.</mark> 지표가 있으면 두 가지를 근거를 가지고 판단할 수 있습니다. 하나는 어느 시간대에 인력이 부족한지이고, 다른 하나는 정한 응답 기한이 너무 짧거나 길지 않은지입니다.
- 비어 있는 리스트로 평균을 구하면 0 으로 나누는 오류(`ZeroDivisionError`)가 발생합니다. 확인된 티켓이 하나도 없는 날이 있을 수 있으므로 `average` 가 먼저 개수를 검사합니다. 이처럼 예외 상황을 미리 대비하는 작성 방식을 방어적 프로그래밍(defensive programming)이라고 합니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1 · 2번을 비워 두면 오늘 샘플에서는 오류가 나지 않습니다. 하지만 숫자가 하나도 없는 리스트로 평균을 구하는 날에는 `ZeroDivisionError`(0 으로 나누었다는 오류)가 납니다.
- 3번을 비워 두면 평균이 `None` 으로 나옵니다.

```
평균 확인 시간(MTTA): None 분
평균 해결 시간(MTTR): None 분
```

- 4번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**미확인 티켓까지 평균에 포함됩니다.**</mark> 그 결과 확인한 티켓이 5장이 아니라 7장으로 계산되고 평균도 달라집니다.

```
티켓 7 장 · 확인한 티켓 7 장 · 해결한 티켓 3 장
평균 확인 시간(MTTA): 34.285714285714285 분
```

- 5번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. `IndentationError` 로 시작하는 오류입니다.

```
IndentationError: expected an indented block
```

- 6 · 7번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**응답 기한 위반이 0장으로 집계됩니다.**</mark>

```
응답 기한을 넘긴 티켓: 0 장
```

- 7번만 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다.

```
IndentationError: expected an indented block
```

- 8번을 비워 두면 `ack_times` 가 만들어지지 않아 오류가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'ack_times' is not defined
```

- 9번을 비워 두면 `mean_ack_minutes` 가 만들어지지 않아 오류가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'mean_ack_minutes' is not defined
```

**관제에서는**

- 근무 교대 인계(shift handoff) 보고에는 보통 두 가지를 포함합니다. 하나는 평균 확인 시간 · 평균 해결 시간 · 응답 기한 위반 수이고, 다른 하나는 <mark>다음 근무자에게 인계할 미해결 티켓 목록</mark>(티켓마다 현재 상태와 다음 조치)입니다. 평균은 표본 크기(티켓 수)와 함께 보고합니다. 오늘의 숫자는 근무 3시간 시뮬레이션의 예시입니다.
