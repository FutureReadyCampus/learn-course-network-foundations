---
id: m5-u08-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/130_day05_am_report_gate.md
  mission_id: GichanSource.m5-1113-am-report-gate
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

아래 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## Exercise 8-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise8-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`report.py` 의 1 ~ 8번입니다.

```python
    # 1. table["acked_at"] - table["created_at"] 를 table["ack_minutes"] 에 저장한다 (확인까지 걸린 분)
    table["ack_minutes"] = table["acked_at"] - table["created_at"]  # 두 열을 빼서 확인까지 걸린 분 열을 만든다
    # 2. table["rule"].value_counts() 를 rule_counts 에 저장한다
    rule_counts = table["rule"].value_counts()                      # 규칙 열에서 값마다 개수를 센다
    # 3. table["acked_at"] >= 0 인 행만 남겨 acked 에 저장한다 (확인한 티켓만)
    acked = table[table["acked_at"] >= 0]                           # 확인한 티켓(acked_at 이 0 이상)만 남긴다
    # 4. groups["ack_minutes"].mean() 을 grade_means 에 저장한다 (등급마다 평균)
    grade_means = groups["ack_minutes"].mean()                      # 등급마다 확인까지 걸린 분의 평균을 구한다
    # 5. table["acked_at"] > table["sla_due"] 인 행만 남겨 late 에 저장한다
    late = table[table["acked_at"] > table["sla_due"]]              # 응답 기한 시각보다 늦게 확인한 행만 남긴다
        # 6. action["incident"] 가 covered 안에 없으면 (if, not in)
        if action["incident"] not in covered:                       # 티켓에 없는 인시던트이면
            # 7. missing 에 action 을 추가한다 (append)
            missing.append(action)                                  # 그 조치 기록을 추가한다
        # 8. "- " + rule + ": " + str(count) + "장" 을 lines 에 추가한다 (append)
        lines.append("- " + rule + ": " + str(count) + "장")        # 규칙 한 줄을 추가한다
```

`exercise8-1_run.py` 의 9번입니다.

```python
# 9. make_ticket_table(tickets) 의 결과를 table 에 저장한다
table = make_ticket_table(tickets)  # 티켓 리스트를 표로 바꾸고 확인까지 걸린 분 열을 더한다
```

**결과**

- (가) 출력은 다음과 같습니다. 티켓이 가장 많은 규칙은 <mark style="background:#bde3ff">**퇴사한 계정 · 경로 스캔**</mark>(각 2장)이고, 리포트 파일은 <mark style="background:#bde3ff">**32줄**</mark>입니다.

```
--- 단계 1: 불러온 티켓 7 장 · 조치 기록 10 건
--- 단계 2: 규칙별 티켓 수
퇴사한 계정 : 2 장
경로 스캔 : 2 장
규칙은 허용인데 서버가 거절 : 1 장
대량 다운로드 : 1 장
업무 시간 밖 로그인 : 1 장
--- 단계 3: 등급별 평균 확인 시간(분)
high : 10.0 분
mid : 85.0 분
--- 단계 4: 응답 기한을 넘겨 확인한 티켓 2 장 · 티켓이 없는 조치 1 건
TCK-3 기한 68 분 · 확인 80 분
TCK-4 기한 72 분 · 확인 140 분
INC-212 계정 잠금 yuna → 티켓 없음
--- 단계 5: 리포트 파일 incident_report_20261112.md · 32 줄 저장
```

리포트 파일 `incident_report_20261112.md` 의 내용은 다음과 같습니다.

```
# 초동 대응 리포트 — 2026-11-12(목) 오전 근무

## 1. 티켓별 초동 대응
- TCK-1 [high] dami — 퇴사한 계정 · 상태 해결 · 조치 기록 4건
- TCK-2 [low] 198.51.100.90 — 경로 스캔 · 상태 열림 · 조치 기록 2건
- TCK-3 [mid] gaeun — 규칙은 허용인데 서버가 거절 · 상태 해결 · 조치 기록 0건
- TCK-4 [mid] seoyeon — 대량 다운로드 · 상태 확인 중 · 조치 기록 0건
- TCK-5 [low] 203.0.113.250 — 경로 스캔 · 상태 열림 · 조치 기록 1건
- TCK-6 [mid] hana — 업무 시간 밖 로그인 · 상태 해결 · 조치 기록 0건
- TCK-7 [high] dami — 퇴사한 계정 · 상태 확인 중 · 조치 기록 2건

## 2. 규칙별 티켓 수
- 퇴사한 계정: 2장
- 경로 스캔: 2장
- 규칙은 허용인데 서버가 거절: 1장
- 대량 다운로드: 1장
- 업무 시간 밖 로그인: 1장

## 3. 등급별 평균 확인 시간(분)
- high: 10.0분
- mid: 85.0분

## 4. 응답 기한을 넘겨 확인한 티켓
- TCK-3 · 기한 68분 · 확인 80분
- TCK-4 · 기한 72분 · 확인 140분

## 5. 티켓이 없는 조치 (사람이 티켓을 만들어야 함)
- INC-212 · 계정 잠금 · yuna

## 6. 높음(high) 티켓의 처리 경위
- TCK-1 · dami: 0분 티켓 생성 → 10분 담당자 확인 → 45분 해결
- TCK-7 · dami: 95분 티켓 생성 → 105분 담당자 확인
```

- (나) `TCK-2` 와 `TCK-5` 는 `acked_at` 이 <mark style="background:#bde3ff">`-1`</mark>(아직 확인하지 않음)입니다. 3번에서 `acked_at` 이 0 이상인 행만 필터링하므로 low 티켓이 하나도 남지 않아, 단계 3 의 평균 확인 시간 집계에 low 가 나오지 않습니다.
  - 3번에서 확인한 티켓만 필터링하지 않으면 low 의 평균이 ((−1 − 3) + (−1 − 30)) ÷ 2 = <mark style="background:#ffc4d6">**−17.5분**</mark>으로 나옵니다. 확인하지 않은 티켓을 「빨리 확인했다」고 잘못 보고하게 되고, 평균 확인 시간 지표가 실제와 다르게 나옵니다.
- (다) `covered` 에는 티켓 7장에 병합된 인시던트 번호(`INC-201` ~ `INC-211`)만 들어 있습니다. `INC-212` 는 어느 티켓에도 없어서 `not in covered` 가 참이 되므로 `missing` 에 추가됩니다(추적 누락 탐지).
  - <mark style="background:#ffc4d6">이 절이 없으면 `yuna` 계정을 잠근 조치가 리포트에서 누락됩니다.</mark> 고객사는 `yuna` 가 왜 로그인하지 못하는지 알 수 없고, 담당자도 이 사건을 확인하지 않습니다.

**왜**

- <mark>리포트에 「티켓에 적힌 것」만 옮기면 누락되는 사건이 생깁니다.</mark> 조치 기록과 티켓을 대조(reconciliation)해 티켓이 없는 조치를 따로 적으면, 조치는 실행됐는데 리포트에 없는 사건을 찾을 수 있습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 `ack_minutes` 열이 없어서 4번에서 오류가 납니다. <mark style="background:#ffc4d6">**열을 만든 뒤에 그 열로 평균을 구해야 합니다.**</mark>

```
KeyError: 'Column not found: ack_minutes'
```

- 2번을 비워 두면 `rule_counts` 가 만들어지지 않아 오류가 납니다. 3 · 4 · 5번을 비워도 같은 종류의 오류(`name 'acked'` · `name 'grade_means'` · `name 'late'`)가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'rule_counts' is not defined
```

- 3번에서 확인한 티켓만 남기지 않고 `acked = table` 로 쓰면 오류 없이 <mark style="background:#ffc4d6">**low 의 평균이 음수로 나옵니다.**</mark> 단계 3 의 `low : -17.5 분` 줄이 이 실수의 결과입니다.

```
--- 단계 3: 등급별 평균 확인 시간(분)
high : 10.0 분
low : -17.5 분
mid : 85.0 분
```

- 6번을 비워 두면 7번 줄이 `for` 바로 아래 줄이 되어 오류 없이 <mark style="background:#ffc4d6">**모든 조치 기록이 「티켓 없음」으로 나옵니다.**</mark> 단계 4 의 제목 줄이 1건이 아니라 10건으로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 4: 응답 기한을 넘겨 확인한 티켓 2 장 · 티켓이 없는 조치 10 건
```

- 7번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. `IndentationError`(들여쓰기 오류: 줄 앞의 빈칸이 맞지 않다는 뜻)로 시작하는 오류입니다(문구는 파이썬 버전마다 조금 다릅니다).

```
IndentationError: expected an indented block
```

- 8번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**리포트 2절이 제목만 남고 비어 있습니다.**</mark> 단계 5 의 줄 수가 32줄이 아니라 27줄로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 5: 리포트 파일 incident_report_20261112.md · 27 줄 저장
```

- 9번을 비워 두면 `table` 이 만들어지지 않아 오류가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'table' is not defined
```

**관제에서는**

- 초동 대응 리포트는 사건 직후 정리해 전달하는 보고라서, 정해진 양식(템플릿, template)에 맞춰 자동으로 작성하는 제품도 있습니다. 보고에는 평균 확인 시간 · 평균 해결 시간 같은 지표를 함께 싣는 경우가 많습니다. <mark>전달하기 전에 「조치는 했는데 티켓이 없는 것」처럼 누락된 데이터를 먼저 점검합니다.</mark> 오늘의 절 다섯 개는 예시이고, 실제 양식은 고객사와 정한 대로 작성합니다.

---

## Exercise 8-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise8-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`approval_gate.py` 의 1 ~ 7번입니다.

```python
    # 1. request["target"] 이 policy["allowlist_ips"] 안에 있는지(in)의 결과를 리턴한다
    return request["target"] in policy["allowlist_ips"]  # 대상이 허용 목록에 있는지의 결과를 리턴한다
    # 2. grade_table[request["grade"]] 를 score 에 저장한다 (등급 점수로 시작한다)
    score = grade_table[request["grade"]]                # 이 요청 등급의 점수로 시작한다
    # 3. request["target"] 이 policy["vip_accounts"] 안에 있으면 (if, in)
    if request["target"] in policy["vip_accounts"]:      # 대상이 VIP 계정이면
        # 4. score 에 score + policy["vip_points"] 를 저장한다 (VIP 점수를 더한다)
        score = score + policy["vip_points"]             # VIP 점수를 더한다
    # 5. is_allowlisted(request, policy) 가 참이면 (if)
    if is_allowlisted(request, policy):                  # 허용 목록 대상이면
    # 6. risk_score(request, policy) 의 두 결과를 score, reasons 에 저장한다
    score, reasons = risk_score(request, policy)         # 위험 점수와 이유 리스트를 함께 받는다
    # 7. score 가 policy["approval_score"] 이상이면 (if, >=)
    if score >= policy["approval_score"]:                # 승인 기준 점수 이상이면
```

위 줄만으로는 `if` 안에 들어가는 줄이 어느 것인지 알기 어려우니, 미리 채운 줄까지 넣은 두 함수의 완성된 모양을 함께 봅니다.

**전체 모양 — `risk_score`**

```python
def risk_score(request, policy):                                            # 조치 요청 한 건과 승인 정책을 받는 함수
    """등급 · VIP · 함께 쓰는 IP · 대상 수로 위험 점수를 더하고, 점수와 이유 리스트를 함께 리턴한다.
    자동으로 실행해도 되는 요청인지 숫자로 판단할 때 쓴다.
    """
    grade_table = policy["grade_points"]                                    # 등급마다 정한 점수 표 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    score = grade_table[request["grade"]]                                   # 이 요청 등급의 점수로 시작한다
    reasons = ["등급 " + request["grade"] + " +" + str(score)]              # 점수를 더한 이유 리스트 — 미리 채운 줄
    if request["target"] in policy["vip_accounts"]:                         # 대상이 VIP 계정이면
        score = score + policy["vip_points"]                                # VIP 점수를 더한다
        reasons.append("VIP 계정 +" + str(policy["vip_points"]))            # 이유를 추가한다 — 미리 채운 줄
    if request["users_on_ip"] >= policy["shared_ip_limit"]:                 # 여러 계정이 함께 쓰는 IP 이면 — 미리 채운 줄
        score = score + policy["shared_ip_points"]                          # 함께 쓰는 IP 점수를 더한다 — 미리 채운 줄
        reasons.append("함께 쓰는 IP +" + str(policy["shared_ip_points"]))  # 이유를 추가한다 — 미리 채운 줄
    if request["target_count"] > policy["many_targets_limit"]:              # 한 번에 조치할 대상이 많으면 — 미리 채운 줄
        score = score + policy["many_targets_points"]                       # 대상 수 점수를 더한다 — 미리 채운 줄
        reasons.append("대상 " + str(request["target_count"]) + "개 +" + str(policy["many_targets_points"]))  # 이유를 추가한다 — 미리 채운 줄
    return score, reasons                                                   # 점수와 이유 리스트를 함께 리턴한다 — 미리 채운 줄
```

**전체 모양 — `decide_gate`**

```python
def decide_gate(request, policy):                 # 조치 요청 한 건과 승인 정책을 받는 함수
    """조치 요청 한 건을 「차단 금지」 · 「승인 필요」 · 「자동」 가운데 하나로 정하고, 결정과 이유 리스트를 함께 리턴한다.
    자동 대응이 조치를 실행하기 직전에, 사람의 승인이 필요한지 정할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    if is_allowlisted(request, policy):           # 허용 목록 대상이면
        return "차단 금지", ["허용 목록 대상"]    # 결정과 이유를 함께 리턴한다 — 미리 채운 줄
    score, reasons = risk_score(request, policy)  # 위험 점수와 이유 리스트를 함께 받는다
    reasons.append("합계 " + str(score) + "점")   # 합계 점수를 이유에 추가한다 — 미리 채운 줄
    if score >= policy["approval_score"]:         # 승인 기준 점수 이상이면
        return "승인 필요", reasons               # 결정과 이유를 함께 리턴한다 — 미리 채운 줄
    return "자동", reasons                        # 기준보다 낮으면 자동으로 실행한다 — 미리 채운 줄
```

`exercise8-2_run.py` 의 8 · 9번입니다.

```python
    # 8. decide_gate(request, policy) 의 두 결과를 decision, reasons 에 저장한다
    decision, reasons = decide_gate(request, policy)  # 결정과 이유 리스트를 함께 받는다
    # 9. counts[decision] 에 counts[decision] + 1 을 저장한다 (1 늘린다)
    counts[decision] = counts[decision] + 1           # 이 결정의 요청 수를 1 늘린다
```

**결과**

- (가) 출력은 다음과 같습니다. 자동 <mark style="background:#bde3ff">**3건**</mark> · 승인 필요 <mark style="background:#bde3ff">**3건**</mark> · 차단 금지 <mark style="background:#bde3ff">**2건**</mark>이고, 승인 필요는 `REQ-2` · `REQ-5` · `REQ-6` 입니다.

```
--- 단계 1: 불러온 조치 요청 8 건 · 승인 기준 3 점
--- 단계 2: 요청마다 결정과 이유
REQ-1 계정 잠금 dami → 자동 · 등급 high +2, 합계 2점
REQ-2 계정 잠금 gaeun → 승인 필요 · 등급 mid +1, VIP 계정 +3, 합계 4점
REQ-3 IP 차단 203.0.113.80 → 차단 금지 · 허용 목록 대상
REQ-4 IP 차단 198.51.100.45 → 자동 · 등급 low +0, 합계 0점
REQ-5 IP 차단 198.51.100.77 → 승인 필요 · 등급 mid +1, 함께 쓰는 IP +2, 합계 3점
REQ-6 계정 잠금 minsu → 승인 필요 · 등급 high +2, 대상 6개 +2, 합계 4점
REQ-7 세션 종료 hana → 자동 · 등급 mid +1, 합계 1점
REQ-8 IP 차단 192.0.2.10 → 차단 금지 · 허용 목록 대상
--- 단계 3: 결정별 요청 수
자동 : 3 건
승인 필요 : 3 건
차단 금지 : 2 건
--- 단계 4: 담당자에게 보낼 승인 요청
REQ-2 INC-312 계정 잠금 gaeun → 담당자 승인을 기다림
REQ-5 INC-315 IP 차단 198.51.100.77 → 담당자 승인을 기다림
REQ-6 INC-316 계정 잠금 minsu → 담당자 승인을 기다림
--- 단계 5: gate_results.json 에 8 건 저장
```

- (나) `REQ-1` 은 등급 high 2점뿐이라 <mark style="background:#bde3ff">합계 2점</mark>으로 <mark style="background:#ffdcb0">임계값(3점)</mark>보다 낮아 자동입니다. `REQ-6` 은 등급 2점에 대상 6개 2점을 더해 <mark style="background:#bde3ff">합계 4점</mark>이라 승인 필요입니다.
  - 대상이 많으면 잘못 실행했을 때 여러 사용자의 계정이 한꺼번에 잠기므로, 영향 범위가 넓은 조치입니다. <mark style="background:#e0d4ff">Unit 2의 인사 시스템 오류(퇴사자 알림이 한꺼번에 많이 들어온 일)</mark>처럼 입력이 잘못되면 대상 수가 갑자기 늘 수 있습니다.
- (다) 허용 목록 대상은 차단하면 업무가 중단되는 대상이라, <mark>점수와 무관하게 차단하지 않아야 합니다.</mark> 점수부터 판단하면 `REQ-3`(4점)처럼 점수가 높은 요청이 「승인 필요」가 되고, 담당자가 실수로 승인하면 협력사 사무실 IP 가 차단됩니다.
  - 기준을 설정 파일에 따로 두면 코드를 고치지 않고 숫자만 바꿔 정책을 조정할 수 있습니다. 또 설정 파일을 깃(git)으로 관리하면 누가 언제 기준을 바꿨는지 변경 이력(change history)으로 남습니다.

**왜**

- <mark>승인 게이트는 「먼저 실행하면 안 되는 대상을 제외하고, 그다음 위험이 큰 조치만 사람에게 승인을 요청하는」 순서입니다.</mark> 모든 요청에 승인을 요구하면 요청이 너무 많아져서 담당자가 내용을 자세히 보지 않고 승인하게 됩니다. 반대로 모든 요청을 자동으로 실행하면 큰 실수를 막지 못합니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 `is_allowlisted` 가 아무것도 리턴하지 않아 <mark style="background:#ffc4d6">**허용 목록 대상도 점수로 정해집니다.**</mark> 점검 서버 `192.0.2.10` 이 「자동」으로 차단되는 것이 이 실수의 결과입니다.

```
REQ-3 IP 차단 203.0.113.80 → 승인 필요 · 등급 high +2, 함께 쓰는 IP +2, 합계 4점
REQ-8 IP 차단 192.0.2.10 → 자동 · 등급 low +0, 합계 0점
```

- 2번을 비워 두면 `score` 를 만들기 전에 쓰게 되어 오류가 납니다. 파이썬 3.11 부터는 같은 오류가 `cannot access local variable 'score' …` 문구로 나옵니다.

```
UnboundLocalError: local variable 'score' referenced before assignment
```

- 3번을 비워 두면 4번 줄이 앞줄보다 안쪽으로 들어가 있어 실행하기 전에 멈춥니다. 5번과 7번을 비워도 같은 오류가 납니다.

```
IndentationError: unexpected indent
```

- 4번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**이유에는 「VIP 계정 +3」이 있는데 점수에는 더해지지 않습니다.**</mark> `REQ-2` 가 합계 1점으로 「자동」이 되는 것이 이 실수의 결과입니다.

```
REQ-2 계정 잠금 gaeun → 자동 · 등급 mid +1, VIP 계정 +3, 합계 1점
```

- 6번을 비워 두면 `reasons` 가 만들어지지 않아 오류가 납니다.

```
NameError: name 'reasons' is not defined
```

- 7번에서 `>=` 대신 `>` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**기준과 같은 3점이 「자동」이 됩니다.**</mark> `REQ-5` 가 자동으로 나오는 것이 이 실수의 결과입니다.

```
REQ-5 IP 차단 198.51.100.77 → 자동 · 등급 mid +1, 함께 쓰는 IP +2, 합계 3점
```

- 8번을 비워 두면 `decision` 이 만들어지지 않아 9번 줄에서 오류가 납니다.

```
NameError: name 'decision' is not defined
```

- 9번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**결정별 요청 수가 모두 0건으로 나옵니다.**</mark>

```
--- 단계 3: 결정별 요청 수
자동 : 0 건
승인 필요 : 0 건
차단 금지 : 0 건
```

**관제에서는**

- SOAR(Security Orchestration, Automation and Response, 쏘아: 보안 오케스트레이션 · 자동화 · 대응) 제품의 플레이북에는 조치 직전에 사람의 승인을 받는 단계(휴먼 인 더 루프)를 넣을 수 있습니다. 어떤 조치를 승인 없이 실행할지는 팀이 정합니다. 위험이 낮은 조치는 자동으로, 업무에 영향을 줄 수 있는 조치는 분석가의 승인을 받는 방식이 일반적입니다.
- <mark>점수와 임계값을 설정 파일에 따로 두면, 운영하면서 오탐 · 사고 기록을 보고 승인 기준을 조정하기 쉽습니다.</mark> 오늘의 점수와 3점 임계값은 예시입니다.

---

## Exercise 8-3 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise8-3_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`false_positive.py` 의 1 ~ 7번입니다.

```python
        # 1. record["before"] 와 record["after"] 가 다르면 (if, !=)
        if record["before"] != record["after"]:                                  # 조치 전과 조치 후가 다르면
            # 2. changes 에 record 를 추가한다 (append)
            changes.append(record)                                               # 실제로 바뀐 기록을 추가한다
        # 3. record["action"] 이 "계정 잠금" 이고(and) target 이 state["locked_users"] 안에 있으면 (if, ==, in)
        if record["action"] == "계정 잠금" and target in state["locked_users"]:  # 잠금 기록인데 아직 잠겨 있으면
        # 4. record["action"] 이 "IP 차단" 이고(and) target 이 state["blocked_ips"] 안에 있으면 (if, ==, in)
        if record["action"] == "IP 차단" and target in state["blocked_ips"]:     # 차단 기록인데 아직 차단되어 있으면
        # 5. record["action"] 이 "IP 차단" 이면 (if, ==)
        if record["action"] == "IP 차단":                                        # IP 차단 기록이면
            # 6. "허용 목록에 추가 검토: " + record["target"] 을 리턴한다
            return "허용 목록에 추가 검토: " + record["target"]                  # 허용 목록에 넣자고 제안한다
    # 7. rollback_incident(incident_id, log, state) 의 결과를 undo_records 에 저장한다 (되돌리기)
    undo_records = rollback_incident(incident_id, log, state)                    # 자동 조치가 바꾼 것만 거꾸로 되돌린다
```

3 · 4번은 `if` 만 쓰고 `if` 안에 들어가는 줄은 미리 채운 줄이니, 완성된 모양을 함께 봅니다.

**전체 모양 — `find_not_recovered`**

```python
def find_not_recovered(changes, state):                                          # 바뀐 기록 리스트와 연습용 시스템 상태를 받는 함수
    """되돌린 뒤에도 아직 잠겨 있는 계정이나 차단된 IP 를 리스트로 리턴한다. 빈 리스트이면 복구가 끝난 것이다.
    되돌리기 함수를 실행한 뒤, 실제 상태가 원래대로 돌아왔는지 확인할 때 쓴다.
    """
    remaining = []                                                               # 아직 복구되지 않은 대상을 모을 빈 리스트 — 미리 채운 줄
    for record in changes:                                                       # 바뀐 기록을 하나씩 읽는다 — 미리 채운 줄
        target = record["target"]                                                # 조치 대상(계정 또는 IP) — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        if record["action"] == "계정 잠금" and target in state["locked_users"]:  # 잠금 기록인데 아직 잠겨 있으면
            remaining.append(target)                                             # 아직 잠겨 있는 계정을 추가한다 — 미리 채운 줄
        if record["action"] == "IP 차단" and target in state["blocked_ips"]:     # 차단 기록인데 아직 차단되어 있으면
            remaining.append(target)                                             # 아직 차단된 IP 를 추가한다 — 미리 채운 줄
    return remaining                                                             # 복구되지 않은 대상 리스트를 리턴한다 — 미리 채운 줄
```

`exercise8-3_run.py` 의 8 · 9번입니다.

```python
    # 8. handle_false_positive(report, log, state, NOW) 의 결과를 result 에 저장한다
    result = handle_false_positive(report, log, state, NOW)  # 신고 한 건을 처리하고 결과를 받는다
    # 9. results 에 result 를 추가한다 (append)
    results.append(result)                                   # 처리 결과를 추가한다
```

**결과**

- (가) 출력은 다음과 같습니다. 걸린 시간은 `INC-301` 이 <mark style="background:#bde3ff">**25분**</mark>, `INC-202` 가 <mark style="background:#bde3ff">**5분**</mark>이고 둘 다 30분 안입니다. 처리 뒤 잠긴 계정은 <mark style="background:#bde3ff">`junho` · `dami`</mark> 입니다.

```
--- 단계 1: 오탐 신고 2 건 · 조치 기록 7 건 · 지금 45 분
처리 전 잠긴 계정: ['junho', 'dami', 'jiwoo'] · 차단된 IP: ['198.51.100.90']
--- 단계 2: 신고마다 영향 확인 · 되돌리기 · 복구 확인 · 규칙 조정 제안
[INC-301] 신고: 영업팀장 — jiwoo 는 출장 중이고 출장 등록이 되어 있다
 - 영향 확인: ['세션 종료 jiwoo', '계정 잠금 jiwoo']
 - 되돌리기: ['되돌리기 불가 jiwoo', '계정 해제 jiwoo']
 - 복구 확인: 아직 잠기거나 차단된 대상 [] · 걸린 시간 25 분 · 기준 30 분 안 True
 - 규칙 조정 제안: 탐지 규칙 예외 검토: jiwoo (해외 IP 에서 로그인)
[INC-202] 신고: 인프라팀 — 198.51.100.90 은 회사가 계약한 점검 업체의 스캐너 IP 다
 - 영향 확인: ['IP 차단 198.51.100.90']
 - 되돌리기: ['IP 해제 198.51.100.90']
 - 복구 확인: 아직 잠기거나 차단된 대상 [] · 걸린 시간 5 분 · 기준 30 분 안 True
 - 규칙 조정 제안: 허용 목록에 추가 검토: 198.51.100.90
--- 단계 3: 처리 뒤 상태 (오탐이 아닌 계정은 그대로인지)
잠긴 계정: ['junho', 'dami'] · 차단된 IP: []
dami 는 아직 잠김: True
--- 단계 4: fp_results.json 에 2 건 · fp_state_after.json 저장 · 기준 30 분
```

- (나) 그 기록은 `before` 와 `after` 가 모두 <mark style="background:#bde3ff">「변경 없음」</mark>입니다. 함께 쓰는 IP 라서 담당자 승인을 기다리느라 차단하지 않았으므로, 자동 조치가 바꾼 것이 없어 영향 확인 대상에서 제외됩니다.
  - 1번의 `if` 가 없으면 이 기록도 영향 확인에 들어가고, 규칙 조정 제안이 「허용 목록에 추가 검토: 198.51.100.120」으로 바뀝니다. 여러 계정이 함께 쓰는 IP(`fp_log.json` 의 사유)를 <mark style="background:#ffc4d6">허용 목록에 넣자는 잘못된 제안</mark>입니다.
- (다) <mark style="background:#ffc4d6">종료한 세션은 되돌릴 수 없는 조치(비가역)입니다.</mark> 담당자는 `jiwoo` 에게 「계정은 해제했으니 다시 로그인하면 된다」고 안내해야 합니다.
  - `dami` 는 퇴사한 계정이라 정탐(true positive)인 진짜 공격(`INC-201`)이고 오탐 신고가 없었습니다. <mark>오탐 처리는 신고된 인시던트만 롤백해야 하므로</mark>, `dami` 는 그대로 잠겨 있어야 합니다.

**왜**

- <mark>오탐 복구는 세 가지를 모두 충족해야 완료됩니다. 정한 시간 안에 복구하고, 바뀐 것을 빠짐없이 롤백하고, 진짜 공격에 한 조치는 그대로 유지합니다.</mark>
- 롤백한 뒤 실제 상태를 다시 점검하고(복구 확인) 규칙 조정 제안까지 남겨야, 같은 오탐 알림이 반복되지 않습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 2번 줄이 `for` 바로 아래 줄이 되어 오류 없이 <mark style="background:#ffc4d6">**바뀌지 않은 기록까지 영향 확인에 들어갑니다.**</mark> 아래 두 줄(영향 확인 · 규칙 조정 제안)이 이 실수의 결과입니다.

```
 - 영향 확인: ['IP 차단 198.51.100.120', '세션 종료 jiwoo', '계정 잠금 jiwoo']
 - 규칙 조정 제안: 허용 목록에 추가 검토: 198.51.100.120
```

- 2번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. 6번을 비워도 같은 오류가 납니다(문구는 파이썬 버전마다 조금 다릅니다).

```
IndentationError: expected an indented block
```

- 3번을 비워 두면 미리 채운 `remaining.append(target)` 줄이 앞줄보다 들여써져 있어 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- 3번에서 `and target in state["locked_users"]` 를 빠뜨리면 오류 없이 <mark style="background:#ffc4d6">**이미 해제된 `jiwoo` 가 「아직 잠기거나 차단된 대상」으로 나옵니다.**</mark> 잠금 기록이 있다는 것만 보고 지금 상태를 보지 않았기 때문입니다.

```
 - 복구 확인: 아직 잠기거나 차단된 대상 ['jiwoo'] · 걸린 시간 25 분 · 기준 30 분 안 True
```

- 4번을 비워 두면 오류는 나지 않고 출력도 정답과 같습니다. 아래 `remaining.append(target)` 줄이 3번 `if` 안으로 들어가서, <mark style="background:#ffc4d6">**IP 차단이 풀리지 않아도 찾지 못합니다.**</mark> 오늘 샘플은 IP 차단이 모두 풀려서 4번을 비워도 출력이 같으니, 출력이 맞아도 코드를 다시 읽어 확인합니다.
- 5번을 비워 두면 6번 줄이 `for` 바로 아래 줄이 되어 오류 없이 <mark style="background:#ffc4d6">**계정 오탐에도 「허용 목록에 추가」를 제안합니다.**</mark>

```
 - 규칙 조정 제안: 허용 목록에 추가 검토: jiwoo
```

- 7번을 비워 두면 `undo_records` 가 만들어지지 않아 오류가 납니다. 되돌리기도 실행되지 않습니다.

```
NameError: name 'undo_records' is not defined
```

- 8번을 비워 두면 `result` 가 만들어지지 않아 9번 줄에서 오류가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'result' is not defined
```

- 9번을 비워 두면 오류 없이 <mark style="background:#ffc4d6">**결과 파일에 0건이 저장됩니다.**</mark> 화면에는 결과가 나오지만 기록이 남지 않습니다.

```
--- 단계 4: fp_results.json 에 0 건 · fp_state_after.json 저장 · 기준 30 분
```

**관제에서는**

- 오탐으로 확인되면 자동 조치를 롤백하고, 사용자에게 알리고, 탐지 규칙이나 허용 목록을 조정(튜닝)하자는 검토 요청을 남깁니다. 규칙 조정은 승인을 받은 뒤에 적용합니다. <mark>롤백한 뒤 실제 상태를 다시 점검하는 복구 확인 단계를 생략하지 않는 것이 중요합니다.</mark> 오늘의 30분 기준은 예시이고, 실제 기준은 팀과 고객사 계약마다 다릅니다.
