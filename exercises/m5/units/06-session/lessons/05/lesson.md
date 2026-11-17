---
id: m5-u06-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/126_day04_am_ticket_notice.md
  mission_id: GichanSource.m5-1112-am-ticket-notice
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## 정답 2-1

💻 **터미널에 입력합니다.**

```bash
pwd
python day04_2-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`ticketing.py` 의 1 ~ 6번입니다.

```python
    # 1. "[" + grade + "] " + entity + " — " + rule 을 이어 붙인 문자열를 리턴한다
    return "[" + grade + "] " + entity + " — " + rule  # 등급 · 대상 · 규칙을 이어 붙인 제목을 리턴한다
    # 2. next_steps.get(status, DEFAULT_NEXT_STEP) 의 결과를 리턴한다 (키가 없으면 기본 문장)
    return next_steps.get(status, DEFAULT_NEXT_STEP)   # 상태에 맞는 다음 할 일을 리턴한다 (없으면 기본 문장)
        # 3. text 안에 "확인 실패" 가 들어 있으면 (if, in)
        if "확인 실패" in text:                        # 문장 안에 확인 실패가 있으면
            # 4. True 를 리턴한다
            return True                                # 확인 실패가 있다고 True 를 리턴한다
    # 5. sla_table[alert["grade"]] 를 sla_minutes 에 저장한다 (이 알림 등급의 응답 기한)
    sla_minutes = sla_table[alert["grade"]]            # 이 알림 등급의 응답 기한(분)을 꺼낸다
    # 6. alert["minute"] + sla_minutes 를 sla_due 에 저장한다 (응답해야 하는 시각)
    sla_due = alert["minute"] + sla_minutes            # 알림이 온 시각 + 응답 기한 = 응답해야 하는 시각
```

`day04_2-1_run.py` 의 7 ~ 9번입니다.

```python
    # 7. make_ticket(alert, ticket_no, rules, NEXT_STEPS) 의 결과를 ticket 에 저장한다
    ticket = make_ticket(alert, ticket_no, rules, NEXT_STEPS)  # 알림으로 티켓을 만든다
    # 8. tickets 리스트에 ticket 을 추가한다 (append)
    tickets.append(ticket)                                     # 티켓 리스트에 추가한다
        # 9. manual_count 에 manual_count + 1 을 저장한다 (1 늘린다)
        manual_count = manual_count + 1                        # 직접 확인이 필요한 티켓 수를 1 늘린다
```

**결과**

- (가) 출력은 다음과 같습니다. 직접 확인이 필요한 티켓은 <mark style="background:#bde3ff">**TCK-7**</mark> 한 장이고, 응답 기한 시각이 가장 이른 티켓은 <mark style="background:#bde3ff">**TCK-1**</mark>(15분)입니다.

```
--- 단계 1: 불러온 알림 11 건 · 응답 기한을 정한 등급 3 개
--- 단계 2: 알림마다 만든 티켓
TCK-1 [high] dami — 퇴사한 계정 · 만든 시각 0 분 · 기한 15 분
TCK-2 [low] 198.51.100.90 — 경로 스캔 · 만든 시각 3 분 · 기한 243 분
TCK-3 [mid] gaeun — 규칙은 허용인데 서버가 거절 · 만든 시각 8 분 · 기한 68 분
TCK-4 [mid] seoyeon — 대량 다운로드 · 만든 시각 12 분 · 기한 72 분
TCK-5 [high] dami — 퇴사한 계정 · 만든 시각 14 분 · 기한 29 분
TCK-6 [low] 198.51.100.90 — 경로 스캔 · 만든 시각 20 분 · 기한 260 분
TCK-7 [low] 203.0.113.250 — 경로 스캔 · 만든 시각 30 분 · 기한 270 분
TCK-8 [mid] hana — 업무 시간 밖 로그인 · 만든 시각 35 분 · 기한 95 분
TCK-9 [high] dami — 퇴사한 계정 · 만든 시각 40 분 · 기한 55 분
TCK-10 [high] dami — 퇴사한 계정 · 만든 시각 95 분 · 기한 110 분
TCK-11 [high] dami — 퇴사한 계정 · 만든 시각 160 분 · 기한 175 분
--- 단계 3: 티켓 본문 예 (TCK-1)
제목: [high] dami — 퇴사한 계정
조치 내역:
 - 계정 잠금: 잠기지 않음 → 잠김
 - 세션 종료: 세션 2개 → 세션 0개
다음 할 일: 조치 결과가 맞는지 확인하고 계정이나 IP 상태를 점검한다
응답 기한: 15 분 (만든 시각 0 분)
--- 단계 4: 직접 확인이 필요한 티켓 1 건
TCK-7 [low] 203.0.113.250 — 경로 스캔 → 조치가 확인되지 않았다. 담당자가 직접 계정이나 IP 상태를 보고 조치한다
```

- (나) `INC-207` 의 `done` 문장이 <mark style="background:#bde3ff">`IP 차단: 차단되지 않음 → 차단되지 않음 (확인 실패)`</mark> 입니다. `has_failed_action` 이 이 문장에서 「확인 실패」를 찾아 `True` 를 리턴합니다. 그래서 후속 조치(`next_step`)가 직접 확인을 지시하는 문장으로 교체됩니다.
  - 이 표시가 없으면 `조치됨` 용 문장(「조치 결과가 맞는지 확인하고…」)만 보입니다.
  - 그러면 담당자는 IP 가 차단됐다고 판단할 수 있습니다. 그 결과 <mark style="background:#ffc4d6">차단되지 않은 공격 IP 의 접속이 계속되는 것을 놓칠 수 있습니다</mark>.
- (다) 응답 기한 시각은 **알림 수신 시각 + 등급별 응답 기한**입니다. TCK-1 은 high 라서 <mark style="background:#bde3ff">0 + 15 = 15분이고, TCK-2 는 low 라서 3 + 240 = 243분</mark>입니다.
  - 모든 티켓의 응답 기한이 240분이면 긴급한 high 알림도 늦게 확인하게 됩니다. 모든 응답 기한이 15분이면 긴급하지 않은 low 알림까지 15분 안에 확인해야 합니다.
  - 그러면 심각도에 따라 처리 우선순위를 정하기 어렵습니다.

**왜**

- <mark>티켓에 「사건 개요 · 이미 수행한 조치 · 후속 조치 · 응답 기한」이 기재되어 있으면, 담당자가 알림 원문을 다시 찾지 않고 즉시 대응에 착수할 수 있습니다.</mark> 사후 검증에 실패한 건을 별도로 표시하면, 자동 대응이 완료하지 못한 조치를 사람이 직접 확인할 수 있습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**제목이 `None` 으로 나옵니다.**</mark> 단계 2 의 줄이 이 실수의 결과입니다.

```
--- 단계 2: 알림마다 만든 티켓
TCK-1 None · 만든 시각 0 분 · 기한 15 분
TCK-2 None · 만든 시각 3 분 · 기한 243 분
```

- 2번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**다음 할 일이 `None` 으로 나옵니다.**</mark> 단계 3 의 `다음 할 일:` 줄이 이 실수의 결과입니다.

```
--- 단계 3: 티켓 본문 예 (TCK-1)
제목: [high] dami — 퇴사한 계정
조치 내역:
 - 계정 잠금: 잠기지 않음 → 잠김
 - 세션 종료: 세션 2개 → 세션 0개
다음 할 일: None
응답 기한: 15 분 (만든 시각 0 분)
```

- 3번의 `if` 를 빠뜨리고 4번만 쓰면 <mark style="background:#ffc4d6">**조치 내역이 있는 티켓이 모두 직접 확인 대상이 됩니다.**</mark> 단계 4 가 1건이 아니라 8건으로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 4: 직접 확인이 필요한 티켓 8 건
```

- 4번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. `IndentationError`(들여쓰기 오류)로 시작하는 오류입니다(문구는 파이썬 버전마다 조금 다릅니다).

```
IndentationError: expected an indented block
```

- 5번을 비워 두면 `sla_minutes` 가 만들어지지 않아 오류가 납니다. <mark style="background:#ffc4d6">**6번에서 쓰기 전에 5번에서 만들어야 합니다.**</mark> 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'sla_minutes' is not defined
```

- 6번을 비워 두면 `sla_due` 가 만들어지지 않아 티켓을 만드는 줄에서 오류가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'sla_due' is not defined
```

- 7번을 비워 두면 `ticket` 이 만들어지지 않아 오류가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'ticket' is not defined
```

- 8번을 비워 두면 티켓이 리스트에 모이지 않습니다. 단계 2 의 줄은 나오지만 번호가 모두 `TCK-1` 이고, 단계 3 에서 오류가 납니다.

```
IndexError: list index out of range
```

- 9번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. `IndentationError` 로 시작하는 오류입니다.

```
IndentationError: expected an indented block
```

**관제에서는**

- 티켓은 알림 내용과 처리 상황을 담당자가 확인하도록 남기는 기록입니다. 그래서 제목 작성 규칙과 응답 기한(SLA)을 팀이 미리 정의합니다. <mark>사후 검증에 실패한 건은 「조치 완료」와 구분해 별도로 표시하는 것이 기본입니다.</mark> <mark style="background:#ffdcb0">오늘의 15분 · 60분 · 240분은 예시이고</mark>, 실제 값은 팀과 고객사 계약마다 다릅니다.

---

## 정답 3-1

💻 **터미널에 입력합니다.**

```bash
pwd
python day04_3-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — `ticket_merge.py` 의 1 ~ 9번입니다.

```python
        # 1. ticket 의 "entity" 가 alert 의 "entity" 와 같고(and) ticket 의 "rule" 도 alert 의 "rule" 과 같으면 (if, ==)
        if ticket["entity"] == alert["entity"] and ticket["rule"] == alert["rule"]:  # 같은 대상 · 같은 규칙이면
                # 2. gap 이 window 이하이면 (if, <=)
                if gap <= window:                                                    # 합치는 시간 안이면
                    # 3. ticket 을 리턴한다
                    return ticket                                                    # 그 티켓을 리턴한다
    # 4. ticket 의 "count" 에 ticket["count"] + 1 을 저장한다 (1 늘린다)
    ticket["count"] = ticket["count"] + 1                                            # 합쳐진 알림 수를 1 늘린다
    # 5. ticket 의 "incidents" 리스트에 alert 의 "id" 를 추가한다 (append)
    ticket["incidents"].append(alert["id"])                                          # 합쳐진 알림 번호를 추가한다
    # 6. ticket 의 "updated_at" 에 alert 의 "minute" 을 저장한다
    ticket["updated_at"] = alert["minute"]                                           # 갱신 시각을 이 알림이 온 시각으로 바꾼다
    # 7. find_open_ticket(tickets, alert, window) 의 결과를 existing 에 저장한다
    existing = find_open_ticket(tickets, alert, window)                              # 합칠 티켓을 찾는다
    # 8. existing 이 None 이면 (if, is)
    if existing is None:                                                             # 합칠 티켓이 없으면
    # 9. merge_alert(existing, alert) 를 호출한다 (합칠 티켓이 있을 때만 여기까지 온다)
    merge_alert(existing, alert)                                                     # 찾은 티켓에 새 알림을 합친다
```

위 줄만 보면 들여쓰기가 헷갈리니, 두 함수의 완성된 모양을 함께 봅니다. 미리 채운 줄도 보입니다. 1번의 `if` 아래에 미리 채운 두 줄이 있고, 8번의 `if` 아래에는 미리 채운 네 줄이 있습니다. 9번은 그 `if` 가 끝난 뒤 한 단계 왼쪽에서 다시 시작합니다.

**전체 모양 — `find_open_ticket`**

```python
def find_open_ticket(tickets, alert, window):                                        # 티켓 리스트 · 알림 · 병합 시간(분)을 받는 함수
    """같은 대상 · 같은 규칙이고, 해결되지 않았고, window 분 안에 갱신된 티켓을 찾아 리턴한다. 없으면 None 을 리턴한다.
    같은 사건의 알림이 티켓 여러 장이 되는 것을 막을 때 쓴다.
    """
    for ticket in tickets:                                                           # 티켓을 하나씩 읽는다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        if ticket["entity"] == alert["entity"] and ticket["rule"] == alert["rule"]:  # 같은 대상 · 같은 규칙이면
            if ticket["status"] != "해결":                                           # 해결되지 않은 티켓이면 — 미리 채운 줄
                gap = alert["minute"] - ticket["updated_at"]                         # 마지막 갱신 뒤 몇 분 지났는지 — 미리 채운 줄
                if gap <= window:                                                    # 합치는 시간 안이면
                    return ticket                                                    # 그 티켓을 리턴한다
    return None                                                                      # 맞는 티켓이 없으면 None 을 리턴한다 — 미리 채운 줄
```

**전체 모양 — `handle_alert`**

```python
def handle_alert(alert, tickets, rules):                           # 알림 · 티켓 리스트 · 규칙을 받는 함수
    """알림 한 건을 처리한다. 합칠 티켓이 있으면 합치고, 없으면 새 티켓을 만든다. 처리한 티켓과 「새 티켓」 또는 「병합」을 함께 리턴한다.
    알림이 올 때마다 부른다.
    """
    window = rules["merge_window_minutes"]                         # 같은 사건으로 보는 시간(분) — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    existing = find_open_ticket(tickets, alert, window)            # 합칠 티켓을 찾는다
    if existing is None:                                           # 합칠 티켓이 없으면
        ticket_no = len(tickets) + 1                               # 새 티켓 번호 — 미리 채운 줄
        ticket = make_ticket(alert, ticket_no, rules, NEXT_STEPS)  # 새 티켓을 만들고 — 미리 채운 줄
        tickets.append(ticket)                                     # 티켓 리스트에 추가한다 — 미리 채운 줄
        return ticket, "새 티켓"                                   # 티켓과 「새 티켓」을 함께 리턴하고 끝낸다 — 미리 채운 줄
    merge_alert(existing, alert)                                   # 찾은 티켓에 새 알림을 합친다
    return existing, "병합"                                        # 티켓과 「병합」을 함께 리턴한다 — 미리 채운 줄
```

**결과**

- (가) 출력은 다음과 같습니다. 티켓은 <mark style="background:#bde3ff">**7장**</mark>이고, TCK-1 에 병합된 알림은 <mark style="background:#bde3ff">**INC-201 · INC-205 · INC-209 · INC-210**</mark> 입니다.

```
--- 단계 1: 알림 11 건 처리 (합치는 시간 60 분)
INC-201 -> TCK-1 새 티켓 · 합쳐진 알림 1 건
INC-202 -> TCK-2 새 티켓 · 합쳐진 알림 1 건
INC-203 -> TCK-3 새 티켓 · 합쳐진 알림 1 건
INC-204 -> TCK-4 새 티켓 · 합쳐진 알림 1 건
INC-205 -> TCK-1 병합 · 합쳐진 알림 2 건
INC-206 -> TCK-2 병합 · 합쳐진 알림 2 건
INC-207 -> TCK-5 새 티켓 · 합쳐진 알림 1 건
INC-208 -> TCK-6 새 티켓 · 합쳐진 알림 1 건
INC-209 -> TCK-1 병합 · 합쳐진 알림 3 건
INC-210 -> TCK-1 병합 · 합쳐진 알림 4 건
INC-211 -> TCK-7 새 티켓 · 합쳐진 알림 1 건
--- 단계 2: 알림 11 건 → 티켓 7 장
TCK-1 [high] dami — 퇴사한 계정 · 알림 ['INC-201', 'INC-205', 'INC-209', 'INC-210'] · 상태 열림
TCK-2 [low] 198.51.100.90 — 경로 스캔 · 알림 ['INC-202', 'INC-206'] · 상태 열림
TCK-3 [mid] gaeun — 규칙은 허용인데 서버가 거절 · 알림 ['INC-203'] · 상태 열림
TCK-4 [mid] seoyeon — 대량 다운로드 · 알림 ['INC-204'] · 상태 열림
TCK-5 [low] 203.0.113.250 — 경로 스캔 · 알림 ['INC-207'] · 상태 열림
TCK-6 [mid] hana — 업무 시간 밖 로그인 · 알림 ['INC-208'] · 상태 열림
TCK-7 [high] dami — 퇴사한 계정 · 알림 ['INC-211'] · 상태 열림
--- 단계 3: TCK-1 상태 바꾸기
TCK-1 → 확인 중 · 바꾼 사람 kim.sec
TCK-1 → 해결 · 바꾼 사람 kim.sec
TCK-1 → 열림 · 거절됨 · 해결에서는 갈 수 없음
댓글 기록:
 - kim.sec · 50분 · 열림 → 확인 중
 - kim.sec · 65분 · 확인 중 → 해결
```

- (나) TCK-1 의 마지막 갱신 시각은 `INC-209` 가 병합된 40분입니다.
  - `INC-210` 은 95분에 수신됐으니 95 − 40 = 55분이라 60분 이하여서 <mark style="background:#bde3ff">병합됐습니다.</mark>
  - 병합되면서 마지막 갱신 시각이 95분이 되고, `INC-211` 은 160분에 수신되어 160 − 95 = 65분이 되어 <mark style="background:#bde3ff">새 티켓(TCK-7)</mark> 이 됐습니다.
  - 티켓 생성 시각(0분)부터 계산하면 `INC-209`(40분)는 병합되지만 `INC-210`(95분)은 60분을 넘어 새 티켓이 됩니다. 그러면 티켓이 8장이 되고 TCK-1 의 알림은 3건뿐입니다.
- (다) `해결 → 열림` 전이를 허용하면 기록이 서로 어긋납니다. 댓글(상태 전이 이력)에는 누가 언제 「해결」했다고 기록되어 있는데, <mark style="background:#ffc4d6">현재 상태는 「열림」이 됩니다</mark>. 또한 해결한 사건이 재발한 것인지, 새 사건인지 구별할 수 없습니다.
  - `해결` 확인이 없으면 해결 후에 수신된 같은 알림이 해결된 티켓에 병합됩니다.
  - 상태가 `해결` 그대로여서 아무도 새 알림이 수신된 것을 확인하지 못합니다.

**왜**

- <mark>같은 사건의 알림을 티켓 한 장으로 병합(중복 제거)하면 담당자가 새로 발생한 사건을 더 쉽게 식별해 처리할 수 있습니다.</mark> 다만 <mark>마지막 갱신 후 경과 시간과 해결 여부를 함께 확인해야 합니다</mark>. 그래야 오래전 알림이 병합되거나 이미 해결된 티켓에 잘못 병합되는 일이 없습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**대상과 규칙을 비교하지 않아 서로 다른 사건이 한 장으로 합쳐집니다.**</mark> 단계 1 에서 `INC-202` 가 `dami` 의 TCK-1 에 합쳐지는 것이 이 실수의 결과입니다.

```
--- 단계 1: 알림 11 건 처리 (합치는 시간 60 분)
INC-201 -> TCK-1 새 티켓 · 합쳐진 알림 1 건
INC-202 -> TCK-1 병합 · 합쳐진 알림 2 건
INC-203 -> TCK-1 병합 · 합쳐진 알림 3 건
INC-204 -> TCK-1 병합 · 합쳐진 알림 4 건
INC-205 -> TCK-1 병합 · 합쳐진 알림 5 건
INC-206 -> TCK-1 병합 · 합쳐진 알림 6 건
```

- 2 · 3번을 비워 두면 합칠 티켓을 찾지 못해 <mark style="background:#ffc4d6">**티켓이 알림 수만큼 만들어집니다.**</mark> 단계 2 의 제목 줄이 이 실수의 결과입니다.

```
--- 단계 2: 알림 11 건 → 티켓 11 장
```

- 2번에서 `<=` 대신 `>=` 를 쓰면 <mark style="background:#ffc4d6">**60분 안의 알림은 합치지 않고 60분이 지난 알림만 합칩니다.**</mark> 티켓 수가 7장이 아니게 됩니다.

```
--- 단계 2: 알림 11 건 → 티켓 9 장
```

- 4번을 비워 두면 합쳐도 <mark style="background:#ffc4d6">**합쳐진 알림 수가 늘지 않습니다.**</mark> 단계 1 에서 `병합` 인데 1건으로 나오는 것이 이 실수의 결과입니다.

```
INC-205 -> TCK-1 병합 · 합쳐진 알림 1 건
INC-206 -> TCK-2 병합 · 합쳐진 알림 1 건
```

- 5번을 비워 두면 <mark style="background:#ffc4d6">**합쳐진 알림 번호가 티켓에 남지 않습니다.**</mark> 단계 2 의 TCK-1 줄에 `INC-201` 한 건만 나오는 것이 이 실수의 결과입니다.

```
TCK-1 [high] dami — 퇴사한 계정 · 알림 ['INC-201'] · 상태 열림
```

- 6번을 비워 두면 갱신 시각이 바뀌지 않아 <mark style="background:#ffc4d6">**60분 기준이 처음 만든 시각부터 재어집니다.**</mark> 티켓이 7장이 아니라 8장이 됩니다.

```
--- 단계 2: 알림 11 건 → 티켓 8 장
TCK-1 [high] dami — 퇴사한 계정 · 알림 ['INC-201', 'INC-205', 'INC-209'] · 상태 열림
TCK-2 [low] 198.51.100.90 — 경로 스캔 · 알림 ['INC-202', 'INC-206'] · 상태 열림
TCK-3 [mid] gaeun — 규칙은 허용인데 서버가 거절 · 알림 ['INC-203'] · 상태 열림
TCK-4 [mid] seoyeon — 대량 다운로드 · 알림 ['INC-204'] · 상태 열림
TCK-5 [low] 203.0.113.250 — 경로 스캔 · 알림 ['INC-207'] · 상태 열림
TCK-6 [mid] hana — 업무 시간 밖 로그인 · 알림 ['INC-208'] · 상태 열림
TCK-7 [high] dami — 퇴사한 계정 · 알림 ['INC-210'] · 상태 열림
TCK-8 [high] dami — 퇴사한 계정 · 알림 ['INC-211'] · 상태 열림
```

- 7번을 비워 두면 `existing` 이 만들어지지 않아 오류가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'existing' is not defined
```

- 8번을 비워 두면 그 아래 미리 채운 줄들이 `if` 없이 들여쓰기만 남아 실행하기 전에 멈춥니다. `IndentationError` 로 시작하는 오류입니다.

```
IndentationError: unexpected indent
```

- 9번을 비워 두면 찾기만 하고 합치지 않아 <mark style="background:#ffc4d6">**「병합」이라고 나오는데 알림 수가 늘지 않습니다.**</mark> 단계 1 의 `병합` 줄이 이 실수의 결과입니다.

```
INC-205 -> TCK-1 병합 · 합쳐진 알림 1 건
INC-206 -> TCK-2 병합 · 합쳐진 알림 1 건
```

**관제에서는**

- 티켓 도구는 같은 사건의 알림을 병합하는 기능(중복 제거, deduplication: 디듀플리케이션)을 갖고 있는 경우가 많습니다. <mark>병합 기준은 도구마다 다르고, 대상 · 규칙(또는 별칭) 같은 식별 값을 쓰는 경우가 많습니다. 해결된 티켓에 병합할지도 도구와 팀마다 정합니다.</mark> 오늘의 60분은 예시입니다.

---

## 정답 4-1

💻 **터미널에 입력합니다.** 알림 서버를 켠 터미널은 그대로 두고, 처음 쓰던 터미널에서 실행합니다.

```bash
pwd
python day04_4-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`ticket_notice.py` 의 1 ~ 6번입니다.

```python
    # 1. table[grade] 를 리턴한다 (이 등급의 수신자 리스트)
    return table[grade]                # 이 등급의 수신자 리스트를 리턴한다
    # 2. ticket 의 "notified_count" 가 0 이면 (if, ==) 처음 보내는 것이다
    if ticket["notified_count"] == 0:  # 처음 보내는 것이면
    # 3.   True 를 리턴한다
        return True                    # 바로 보내도 된다고 True 를 리턴한다
    # 4. elapsed 가 gap 이상인지(>=)의 결과를 리턴한다
    return elapsed >= gap              # 알림 간격 이상 지났는지의 결과를 리턴한다
        # 5. notify(message, url) 의 결과가 참이면 (if)
        if notify(message, url):       # 알림을 보냈으면
            # 6. attempt 를 리턴한다
            return attempt             # 성공한 시도 번호를 리턴한다
```

`day04_4-1_run.py` 의 7 ~ 9번입니다.

```python
    # 7. send_ticket_notice(ticket, alert["minute"], rules) 의 결과를 result 에 저장한다
    result = send_ticket_notice(ticket, alert["minute"], rules)  # 티켓 알림을 보내고 결과를 받는다
    # 8. result 가 "전송" 이면 (if, ==)
    if result == "전송":                                         # 알림을 보냈으면
        # 9. sent_count 에 sent_count + 1 을 저장한다 (1 늘린다)
        sent_count = sent_count + 1                              # 보낸 수를 1 늘린다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 2 의 전송은 <mark style="background:#bde3ff">**9건**</mark>, 건너뜀은 <mark style="background:#bde3ff">**2건**</mark>입니다.

```
--- 단계 1: 알림 11 건 처리와 담당자 알리기
INC-201 -> TCK-1 새 티켓 · 담당자 알리기: 전송
INC-202 -> TCK-2 새 티켓 · 담당자 알리기: 전송
INC-203 -> TCK-3 새 티켓 · 담당자 알리기: 전송
INC-204 -> TCK-4 새 티켓 · 담당자 알리기: 전송
INC-205 -> TCK-1 병합 · 담당자 알리기: 건너뜀
INC-206 -> TCK-2 병합 · 담당자 알리기: 건너뜀
INC-207 -> TCK-5 새 티켓 · 담당자 알리기: 전송
INC-208 -> TCK-6 새 티켓 · 담당자 알리기: 전송
INC-209 -> TCK-1 병합 · 담당자 알리기: 전송
INC-210 -> TCK-1 병합 · 담당자 알리기: 전송
INC-211 -> TCK-7 새 티켓 · 담당자 알리기: 전송
--- 단계 2: 담당자에게 전송 9 건 · 건너뜀 2 건
TCK-1 담당자에게 알린 횟수 3 번 · 마지막으로 알린 시각 95 분
TCK-2 담당자에게 알린 횟수 1 번 · 마지막으로 알린 시각 3 분
TCK-3 담당자에게 알린 횟수 1 번 · 마지막으로 알린 시각 8 분
TCK-4 담당자에게 알린 횟수 1 번 · 마지막으로 알린 시각 12 분
TCK-5 담당자에게 알린 횟수 1 번 · 마지막으로 알린 시각 30 분
TCK-6 담당자에게 알린 횟수 1 번 · 마지막으로 알린 시각 35 분
TCK-7 담당자에게 알린 횟수 1 번 · 마지막으로 알린 시각 160 분
--- 단계 3: 꺼진 주소로 최대 3 번 보내 보기
[알림 실패] ConnectionError
[알림 실패] ConnectionError
[알림 실패] ConnectionError
성공한 시도 번호: 0 (0 은 모두 실패)
--- 단계 4: 파일에 저장된 티켓 7 장
```

알림 서버 터미널에는 `[알림 받음]` 줄이 <mark style="background:#bde3ff">**9개**</mark> 찍힙니다.

```
[알림 받음] [high] dami — 퇴사한 계정 · TCK-1 · 알림 1건 · 기한 15분 · 수신: kim.sec, lee.soc, team.lead
[알림 받음] [low] 198.51.100.90 — 경로 스캔 · TCK-2 · 알림 1건 · 기한 243분 · 수신: kim.sec
[알림 받음] [mid] gaeun — 규칙은 허용인데 서버가 거절 · TCK-3 · 알림 1건 · 기한 68분 · 수신: kim.sec, lee.soc
[알림 받음] [mid] seoyeon — 대량 다운로드 · TCK-4 · 알림 1건 · 기한 72분 · 수신: kim.sec, lee.soc
[알림 받음] [low] 203.0.113.250 — 경로 스캔 · TCK-5 · 알림 1건 · 기한 270분 · 수신: kim.sec
[알림 받음] [mid] hana — 업무 시간 밖 로그인 · TCK-6 · 알림 1건 · 기한 95분 · 수신: kim.sec, lee.soc
[알림 받음] [high] dami — 퇴사한 계정 · TCK-1 · 알림 3건 · 기한 15분 · 수신: kim.sec, lee.soc, team.lead
[알림 받음] [high] dami — 퇴사한 계정 · TCK-1 · 알림 4건 · 기한 15분 · 수신: kim.sec, lee.soc, team.lead
[알림 받음] [high] dami — 퇴사한 계정 · TCK-7 · 알림 1건 · 기한 175분 · 수신: kim.sec, lee.soc, team.lead
```

- (나) 전송을 생략할지 전송할지는 <mark style="background:#ffdcb0">마지막 전송 시각과 최소 간격(30분)</mark>으로 결정됩니다.
  - `INC-205`(14분): TCK-1 은 0분에 전송했고 14분이 지나 30분보다 짧아서 <mark style="background:#bde3ff">전송을 생략합니다.</mark>
  - `INC-206`(20분): TCK-2 는 3분에 전송했고 17분이 지나 30분보다 짧아 전송을 생략합니다.
  - `INC-209`(40분): TCK-1 은 0분에 전송했고 40분이 지나 30분 이상이라 <mark style="background:#bde3ff">전송합니다.</mark>
  - `INC-210`(95분): TCK-1 은 40분에 마지막으로 전송했고 55분이 지나 30분 이상이므로 전송합니다.
  - 전송을 생략하지 않으면 `dami` 의 같은 알림 4건이 모두 담당자에게 전달되어, 알림 피로로 담당자가 알림을 무시하게 됩니다.
- (다) 꺼진 주소(5999번 포트)에는 알림 서버가 없습니다. 그래서 전송할 때마다 연결 오류(`ConnectionError`)가 발생합니다. `notify` 는 `[알림 실패]` 를 출력한 뒤 `False` 를 리턴합니다. `send_with_retry` 가 최대 3번 시도했으므로 이 줄이 3번 출력됩니다. 3번 모두 실패했으므로 `send_with_retry` 는 0 을 리턴했습니다.
  - <mark style="background:#ffc4d6">이 코드는 3번 모두 실패한 알림을 저장하지 않습니다</mark>. 실제 관제에서는 전송에 실패한 알림의 목록을 별도로 보관합니다.
  - 전화나 메일 같은 대체 채널(fallback channel, 폴백 채널: 기본 수단이 실패했을 때 쓰는 다른 전달 수단)로도 통지해야 합니다. 또한 다음 근무자에게 인수인계(handover)해야 합니다.
  - 이 수업 코드에는 없는 운영 절차입니다.

**왜**

- <mark>알림은 전송하는 것만큼 담당자가 실제로 확인하게 하는 것이 중요합니다.</mark> 수신자를 등급에 맞추고 전송 간격을 두면 알림이 무시되지 않습니다. 알림 서버가 일시적으로 멈춘 것이라면 재시도하는 동안 성공할 수 있습니다. <mark style="background:#ffc4d6">이 코드는 시도 사이에 기다리지 않습니다</mark>. 실제 제품은 재시도 사이에 몇 초의 대기 시간(백오프, backoff)을 둔 뒤 다시 전송합니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 수신자 리스트가 `None` 이 되어 이름을 이어 붙이는 줄에서 오류가 납니다.

```
TypeError: 'NoneType' object is not iterable
```

- 2 · 3번을 비워 두면 <mark style="background:#ffc4d6">**처음 보내는 알림도 간격 계산에서 너무 이르다고 나와 건너뜁니다.**</mark> 단계 1 의 첫 줄부터 `건너뜀` 으로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 1: 알림 11 건 처리와 담당자 알리기
INC-201 -> TCK-1 새 티켓 · 담당자 알리기: 건너뜀
INC-202 -> TCK-2 새 티켓 · 담당자 알리기: 건너뜀
INC-203 -> TCK-3 새 티켓 · 담당자 알리기: 건너뜀
```

- 4번을 비워 두면 `should_send` 가 아무것도 리턴하지 않아 <mark style="background:#ffc4d6">**처음이 아닌 알림은 모두 건너뜁니다.**</mark> 전송이 9건이 아니라 7건으로 나옵니다.

```
--- 단계 2: 담당자에게 전송 7 건 · 건너뜀 4 건
```

- 5번의 `if` 를 빠뜨리고 6번만 쓰면 <mark style="background:#ffc4d6">**알림 서버로 보내지도 않고 성공으로 처리됩니다.**</mark> 단계 1 은 모두 `전송` 으로 나오지만 알림 서버 터미널에는 `[알림 받음]` 이 하나도 찍히지 않습니다.

```
--- 단계 1: 알림 11 건 처리와 담당자 알리기
INC-201 -> TCK-1 새 티켓 · 담당자 알리기: 전송
INC-202 -> TCK-2 새 티켓 · 담당자 알리기: 전송
```

- 6번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. `IndentationError` 로 시작하는 오류입니다.

```
IndentationError: expected an indented block
```

- 7번을 비워 두면 `result` 가 만들어지지 않아 오류가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'result' is not defined
```

- 8 · 9번을 비워 두면 알림은 가지만 <mark style="background:#ffc4d6">**센 값이 늘지 않아 전송이 0건으로 나옵니다.**</mark> 단계 2 의 제목 줄이 이 실수의 결과입니다.

```
--- 단계 2: 담당자에게 전송 0 건 · 건너뜀 2 건
```

- 알림 서버를 켜지 않고 실행하면 코드는 정상이어도 <mark style="background:#ffc4d6">**모든 알림이 3번씩 실패합니다.**</mark> 단계 1 의 시작이 이렇게 나오면 서버 터미널이 꺼져 있는 것입니다(알림 11건이 모두 `실패` 가 되어 `[알림 실패]` 가 33번 나옵니다).

```
--- 단계 1: 알림 11 건 처리와 담당자 알리기
[알림 실패] ConnectionError
[알림 실패] ConnectionError
[알림 실패] ConnectionError
INC-201 -> TCK-1 새 티켓 · 담당자 알리기: 실패
```

**관제에서는**

- 알림 전파는 「수신자 · 전송 간격 · 실패 시 대응」을 먼저 정합니다. <mark>같은 사건은 병합해 한 번만 통지하고, 긴급한 알림만 상급자에게 에스컬레이션하는 것</mark>이 알림 피로를 줄이는 기본입니다. 이 수업에서는 알림 서버를 사용합니다. 실제 관제에서는 그 자리에 메신저나 호출 도구(pager, 페이저: 호출 메시지를 받는 기기나 앱) 같은 도구를 사용하며, 달라지는 것은 주로 전송 방법입니다.
