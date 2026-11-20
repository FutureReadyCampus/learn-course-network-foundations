---
id: m5-u04-l10
title: 정답
render: markdown
---

# 정답

## 정답을 보는 방법

아래 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## 실습 4-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise4-1_run.py
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

`exercise4-1_run.py` 의 8 · 9번입니다.

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
  - 대상이 많으면 잘못 실행했을 때 여러 사용자의 계정이 한꺼번에 잠기므로, 영향 범위가 넓은 조치입니다. <mark style="background:#e0d4ff">Unit 1 도전 1-2 의 인사 시스템 오류(퇴사자 알림이 한꺼번에 많이 들어온 일)</mark>처럼 입력이 잘못되면 대상 수가 갑자기 늘 수 있습니다.
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

## 실습 4-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise4-2_run.py
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

`exercise4-2_run.py` 의 8 · 9번입니다.

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

## 도전 4-1 정답

> 여기부터는 **도전(선택)** 정답입니다. 선택입니다. 시간이 남을 때 합니다. 핵심 실습 정답은 앞의 실습 4-1 · 4-2 정답에 있습니다.

**터미널에 입력합니다.** 알림 서버 터미널은 켜 둔 채, 처음 쓰던 터미널에서 실행합니다.

```bash
pwd
python challenge4-1_run.py
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

`challenge4-1_run.py` 의 7 ~ 9번입니다.

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

## 도전 4-2 정답

 **터미널에 입력합니다.** 알림 서버 터미널은 켜 둔 채, 처음 쓰던 터미널에서 실행합니다.

```bash
pwd
python challenge4-2_run.py
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

`challenge4-2_run.py` 의 8 · 9번입니다.

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

## 도전 4-3 정답

 **터미널에 입력합니다.**

```bash
pwd
python challenge4-3_run.py
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

`challenge4-3_run.py` 의 9번입니다.

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

- 초동 대응 리포트는 사건 직후 정리해 전달하는 보고라서, 정해진 양식(템플릿, template)에 맞춰 자동으로 작성하는 제품도 있습니다. 보고에는 평균 확인 시간 · 평균 해결 시간 같은 지표를 함께 싣는 경우가 많습니다. <mark>전달하기 전에 「조치는 했는데 티켓이 없는 것」처럼 누락된 데이터를 먼저 점검합니다.</mark> 오늘의 절 여섯 개는 예시이고, 실제 양식은 고객사와 정한 대로 작성합니다.

---

## 도전 4-4 정답

 **터미널에 입력합니다.**

```bash
pwd
python challenge4-4_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`risk_assessment.py` 의 1 ~ 7번입니다.

```python
    # 1. table["impact"] * table["likelihood"] 를 table["score"] 에 담는다 (위험 점수)
    table["score"] = table["impact"] * table["likelihood"]       # 두 열을 곱해 위험 점수 열을 만든다
    # 2. score 가 6 이상이면 (if, >=)
    if score >= 6:                                               # 6 이상이면
        # 3. "높음" 을 리턴한다
        return "높음"                                            # 높음을 리턴한다
        # 4. control 이 controls 안에 없으면 (if, not in)
        if control not in controls:                              # 지금 있는 통제에 없으면
            # 5. missing 에 control 을 추가한다 (append)
            missing.append(control)                              # 빠진 통제를 추가한다
    # 6. table.sort_values("score", ascending=False) 를 sorted_table 에 담는다 (점수가 큰 것부터)
    sorted_table = table.sort_values("score", ascending=False)   # 점수가 큰 행부터 정렬한다
        # 7. find_missing_controls(level, row["controls"]) 의 결과를 missing 에 담는다
        missing = find_missing_controls(level, row["controls"])  # 이 등급에 빠진 통제를 찾는다
```

`challenge4-4_run.py` 의 8 · 9번입니다.

```python
# 8. assess_risks(table) 의 결과를 rows 에 담는다
rows = assess_risks(table)         # 점수가 큰 것부터 등급과 빠진 통제를 붙인다
        # 9. gap_count 에 gap_count + 1 을 담는다 (1 늘린다)
        gap_count = gap_count + 1  # 빠진 통제가 있는 조치 수를 1 늘린다
```

**결과**

- (가) 출력은 다음과 같습니다. 높음은 <mark style="background:#bde3ff">**계정 잠금 · 세션 종료 · IP 차단**</mark>이고, 바로 보완할 조치는 <mark style="background:#bde3ff">**세션 종료(승인 게이트) · 담당자 알림(감사 기록)**</mark>입니다. 이 결과는 샘플의 통제 목록을 기준으로 산출한 검토 대상이므로, 실제 운영에서는 팀이 확인한 뒤 통제를 적용합니다.

```
--- 단계 1: 불러온 자동 조치 6 개
--- 단계 2: 점수가 큰 조치부터
계정 잠금 · 점수 6 · 높음 · 빠진 통제 []
세션 종료 · 점수 6 · 높음 · 빠진 통제 ['승인 게이트']
IP 차단 · 점수 6 · 높음 · 빠진 통제 []
담당자 알림 · 점수 3 · 보통 · 빠진 통제 ['감사 기록']
티켓 자동 작성 · 점수 2 · 낮음 · 빠진 통제 []
상급자 에스컬레이션 · 점수 2 · 낮음 · 빠진 통제 []
--- 단계 3: 바로 보완할 조치 2 개 · risk_assessment.md 16 줄 저장
```

리스크 평가 문서 `risk_assessment.md` 의 내용은 다음과 같습니다.

```
# 자동 대응 리스크 평가 — 2026-11-13(금)

- 점수 = 영향도(1~3) × 발생 가능성(1~3). 6 이상 높음, 3 이상 보통, 그 밖은 낮음

| 자동 조치 | 영향도 | 발생 가능성 | 점수 | 등급 | 지금 있는 통제 | 빠진 통제 |
|---|---|---|---|---|---|---|
| 계정 잠금 | 3 | 2 | 6 | 높음 | 승인 게이트, 되돌리기, 감사 기록, VIP 예외 | 없음 |
| 세션 종료 | 3 | 2 | 6 | 높음 | 감사 기록 | 승인 게이트 |
| IP 차단 | 3 | 2 | 6 | 높음 | 허용 목록, 승인 게이트, 자동 해제, 되돌리기, 감사 기록 | 없음 |
| 담당자 알림 | 1 | 3 | 3 | 보통 | 알림 간격, 재시도 | 감사 기록 |
| 티켓 자동 작성 | 1 | 2 | 2 | 낮음 | 병합, 감사 기록 | 없음 |
| 상급자 에스컬레이션 | 2 | 1 | 2 | 낮음 | 같은 단계 한 번 | 없음 |

## 바로 보완할 조치
- 세션 종료: 승인 게이트 추가
- 담당자 알림: 감사 기록 추가
```

- (나) 세 조치 모두 영향도 3 × 발생 가능성 2 = 6점으로 높음 등급이라, 필수 통제인 승인 게이트와 감사 기록이 있어야 합니다. 계정 잠금과 IP 차단의 `controls` 에는 둘 다 있지만, 세션 종료에는 <mark style="background:#bde3ff">`감사 기록`</mark> 하나뿐이라 <mark style="background:#ffc4d6">승인 게이트가 빠진 통제 갭이 생깁니다.</mark>
  - <mark style="background:#e0d4ff">Unit 3 함수 `rollback_incident`</mark> 는 세션 종료를 「되돌리기 불가」로 남깁니다. 잘못 실행된 뒤에는 교정 통제(되돌리기)를 쓸 수 없으니, <mark>실행하기 전에 막는 예방 통제인 승인 게이트</mark>가 더 중요합니다.
- (다) 점수는 영향도 1 × 발생 가능성 3 = <mark style="background:#bde3ff">3점</mark>이라 보통 등급입니다. 보통의 기준은 <mark style="background:#ffdcb0">3 이상 6 미만</mark>입니다. 피해(영향도)는 작아도 오탐 알림을 따로 제외하는 장치가 없다고 가정하므로 발생 가능성이 높기 때문입니다.
  - 탐지 통제인 감사 기록이 없으면 사고가 난 뒤 「어느 인시던트에 · 언제 · 어떤 알림을 보냈는지」를 확인할 수 없습니다. 받는 사람까지 알려면 기록에 따로 적어야 합니다. 담당자가 알림을 받았는데 응답하지 않았는지, 알림이 아예 가지 않았는지도 <mark style="background:#ffc4d6">가릴 수 없습니다.</mark>

**왜**

- <mark>리스크 평가는 「어떤 자동 조치가 위험한지」(위험 점수)와 「그 위험을 줄이는 통제가 갖춰져 있는지」(통제 갭 분석)를 한 표로 보여 줍니다.</mark> 점수가 같아도 통제가 다르면 보완할 내용이 달라지므로, 점수와 빠진 통제를 함께 적습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 `score` 열이 없어서 6번의 정렬에서 오류가 납니다.

```
KeyError: 'score'
```

- 2번을 비워 두면 3번 줄이 바로 위 줄보다 오른쪽에서 시작해서(들여쓰기가 맞지 않아) 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- 2번에서 `>=` 대신 `>` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**점수 6인 조치가 모두 보통이 됩니다.**</mark> 점수가 기준값 6 과 같을 때 어긋나는 경계 조건 오류(off-by-one error)입니다. 세션 종료의 통제 갭이 사라지고, 보완할 조치가 1개로 줄어드는 것이 이 실수의 결과입니다.

```
계정 잠금 · 점수 6 · 보통 · 빠진 통제 []
세션 종료 · 점수 6 · 보통 · 빠진 통제 []
IP 차단 · 점수 6 · 보통 · 빠진 통제 []
--- 단계 3: 바로 보완할 조치 1 개 · risk_assessment.md 15 줄 저장
```

- 3번 · 5번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. 9번을 비워도 같은 오류가 납니다(문구는 파이썬 버전마다 조금 다릅니다).

```
IndentationError: expected an indented block
```

- 4번을 비워 두면 5번 줄이 `for` 바로 아래 줄이 되어 오류 없이 <mark style="background:#ffc4d6">**있어야 하는 통제가 모두 빠진 것으로 나옵니다.**</mark> 보완할 조치가 2개가 아니라 4개로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 3: 바로 보완할 조치 4 개 · risk_assessment.md 18 줄 저장
```

- 6번을 비워 두면 `sorted_table` 이 만들어지지 않아 오류가 납니다. 7번 · 8번을 비워도 같은 꼴의 오류(`name 'missing'` · `name 'rows'`)가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'sorted_table' is not defined
```

- 6번에서 `ascending=False`(큰 값부터 정렬하라는 뜻)를 빠뜨리면 오류 없이 <mark style="background:#ffc4d6">**점수가 작은 조치부터 나옵니다.**</mark> 단계 2 의 첫 두 줄이 낮음으로 시작하는 것이 이 실수의 결과입니다.

```
티켓 자동 작성 · 점수 2 · 낮음 · 빠진 통제 []
상급자 에스컬레이션 · 점수 2 · 낮음 · 빠진 통제 []
```

**관제에서는**

- 보안 조직은 리스크 평가에서 영향도와 발생 가능성을 가로축과 세로축으로 놓고, 두 값이 만나는 곳마다 위험의 크기를 표시하는 표(**위험 매트릭스**, risk matrix, 리스크 매트릭스)를 자주 씁니다. 오늘은 같은 생각을 영향도 × 발생 가능성의 곱으로 단순하게 구현했습니다. <mark>자동 대응을 운영에 적용하기 전과 기준을 바꿀 때마다 다시 평가하고, 높음 등급 조치에는 승인 게이트(예방 통제) · 감사 기록(탐지 통제) 같은 통제를 두는 것이 일반적입니다.</mark> 통제를 적용한 뒤에도 남는 위험은 잔여 위험(residual risk)으로 따로 관리합니다. 오늘의 숫자 · 등급 기준 · 필요한 통제는 예시이고, 실제 값은 팀이 정합니다.

---

## 도전 4-5 정답

 **터미널에 입력합니다.**

```bash
pwd
python challenge4-5_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`unit09_check.py` 의 1 ~ 7번입니다.

```python
        # 1. number 가 report_text 안에 없으면 (if, not in)
        if number not in report_text:                             # 리포트에 그 번호가 없으면
            # 2. not_found 에 number 를 추가한다 (append)
            not_found.append(number)                              # 없는 번호를 추가한다
        # 3. decide_gate(case["request"], policy) 의 두 결과를 decision, reasons 에 담는다
        decision, reasons = decide_gate(case["request"], policy)  # 결정과 이유를 함께 받는다
        # 4. decision 이 case["expected"] 와 다르면 (if, !=)
        if decision != case["expected"]:                          # 기대한 결정과 다르면
        # 5. result["in_time"] 이 False 이면 (if not)
        if not result["in_time"]:                                 # 정한 시간 안에 끝나지 않았으면
        # 6. user 가 state["locked_users"] 안에 없으면 (if, not in)
        if user not in state["locked_users"]:                     # 진짜 공격 계정이 잠겨 있지 않으면
            # 7. problems 에 user + " 잠금이 풀림" 을 추가한다 (append)
            problems.append(user + " 잠금이 풀림")                # 문제를 추가한다
```

4 · 5번은 `if` 만 쓰고 `if` 안에 들어가는 줄은 미리 채운 줄이니, 완성된 모양을 함께 봅니다.

**전체 모양 — `check_gate`**

```python
def check_gate(cases, policy):                                    # 시험 사례 리스트와 승인 정책을 받는 함수
    """시험 사례마다 승인 게이트를 실행해, 결정이 기대한 결정과 다른 사례의 이름을 리스트로 리턴한다.
    승인 기준을 바꾼 뒤에도 자동 · 승인 필요 · 차단 금지가 맞게 나뉘는지 확인할 때 쓴다.
    """
    wrong = []                                                    # 기대와 다른 사례를 모을 빈 리스트 — 미리 채운 줄
    for case in cases:                                            # 시험 사례를 하나씩 꺼낸다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        decision, reasons = decide_gate(case["request"], policy)  # 결정과 이유를 함께 받는다
        if decision != case["expected"]:                          # 기대한 결정과 다르면
            wrong.append(case["case"] + " (기대 " + case["expected"] + ", 결과 " + decision + ")")  # 사례 이름과 두 결정을 추가한다 — 미리 채운 줄
    return wrong                                                  # 기대와 다른 사례 리스트를 리턴한다 — 미리 채운 줄
```

**전체 모양 — `check_recovery`**

```python
def check_recovery(results, state, true_positive_users):         # 오탐 처리 결과 · 처리 뒤 상태 · 진짜 공격 계정 리스트를 받는 함수
    """오탐 처리 결과에서 남은 대상 · 시간 초과를 찾고, 진짜 공격 계정이 풀렸는지도 확인해 문제 문장 리스트를 리턴한다.
    오탐 복구가 신속하고 완전했는지, 진짜 공격의 조치는 그대로인지 확인할 때 쓴다.
    """
    problems = []                                                # 문제 문장을 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                       # 오탐 처리 결과를 하나씩 꺼낸다 — 미리 채운 줄
        if result["remaining"] != []:                            # 아직 복구되지 않은 대상이 있으면 — 미리 채운 줄
            problems.append(result["incident"] + " 복구 안 됨")  # 문제를 추가한다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        if not result["in_time"]:                                # 정한 시간 안에 끝나지 않았으면
            problems.append(result["incident"] + " 30분 넘음")   # 문제를 추가한다 — 미리 채운 줄
    for user in true_positive_users:                             # 진짜 공격 계정을 하나씩 꺼낸다 — 미리 채운 줄
        if user not in state["locked_users"]:                    # 진짜 공격 계정이 잠겨 있지 않으면
            problems.append(user + " 잠금이 풀림")               # 문제를 추가한다
    return problems                                              # 문제 문장 리스트를 리턴한다 — 미리 채운 줄
```

`challenge4-5_run.py` 의 8 · 9번입니다.

```python
# 8. check_report(report_text, tickets, actions) 의 결과를 report_problems 에 담는다
report_problems = check_report(report_text, tickets, actions)            # 리포트에 빠진 번호를 찾는다
# 9. check_recovery(results, state, TRUE_POSITIVE_USERS) 의 결과를 recovery_problems 에 담는다
recovery_problems = check_recovery(results, state, TRUE_POSITIVE_USERS)  # 오탐 복구의 문제를 찾는다
```

**결과**

- (가) 출력은 다음과 같습니다. 세 기준 모두 <mark style="background:#bde3ff">**통과**</mark>이고, `unit09_checklist.md` 는 <mark style="background:#bde3ff">**5줄**</mark>입니다.

```
--- 단계 1: 점검 재료 · 티켓 7 장 · 조치 기록 10 건 · 시험 사례 7 개
--- 단계 2: Unit 4 점검 목록
[통과] ① 근무 데이터가 리포트에 빠짐없이 들어갔다 · 문제 0 개
[통과] ② 위험 점수에 따라 자동 · 승인 필요 · 차단 금지가 맞게 나뉜다 · 문제 0 개
[통과] ③ 오탐 복구가 30분 안에 빠짐없이 끝났고 진짜 공격의 잠금은 그대로다 · 문제 0 개
--- 단계 3: unit09_checklist.md 5 줄 저장
```

점검 목록 `unit09_checklist.md` 의 내용은 다음과 같습니다.

```
# Unit 4 마무리 점검 — 2026-11-13(금)

- [통과] ① 근무 데이터가 리포트에 빠짐없이 들어갔다
- [통과] ② 위험 점수에 따라 자동 · 승인 필요 · 차단 금지가 맞게 나뉜다
- [통과] ③ 오탐 복구가 30분 안에 빠짐없이 끝났고 진짜 공격의 잠금은 그대로다
```

- (나) 「대상 3개」는 등급 `mid`(중간)가 주는 1점만 있어 <mark style="background:#bde3ff">1점 · 자동</mark>이고, 「대상 4개」는 mid 1점 + 대상 수 2점으로 <mark style="background:#bde3ff">3점 · 승인 필요</mark>입니다.
  - <mark style="background:#ffdcb0">기준이 「3개 넘음(`>`)」</mark>인데 코드가 「3개 이상(`>=`)」으로 바뀌면(경계 조건 오류), 대상 3개 사례가 승인 필요로 바뀌어 <mark style="background:#ffc4d6">점검이 바로 「확인 필요」를 냅니다.</mark> 경계값의 양쪽(안쪽과 바깥쪽)을 함께 포함해야 이런 실수를 검출합니다.
- (다) <mark style="background:#e0d4ff">`rollback_incident`</mark> 가 신고된 인시던트가 아닌 기록까지 되돌리면 <mark style="background:#ffc4d6">정탐(진짜 공격)인 `dami` 의 잠금이 풀릴 수 있습니다.</mark> 남은 대상과 시간만 확인하면 오탐 복구가 「통과」로 보일 수 있으므로, 정탐 계정의 잠금이 그대로인지도 따로 확인해야 이 실수를 놓치지 않습니다.

**왜**

- <mark>자동 점검은 「기대한 결과」를 미리 적어 두고 실제 결과와 비교합니다.</mark> 기준 숫자나 코드를 바꾼 뒤 한 번 실행하면(회귀 시험), 사람이 출력을 다시 읽지 않아도 어디가 잘못됐는지 알 수 있습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 2번 줄이 `for` 바로 아래 줄이 되어 오류 없이 <mark style="background:#ffc4d6">**있어야 할 번호가 모두 「없음」으로 나옵니다.**</mark> ① 이 「확인 필요 · 문제 8 개」로 나오는 것이 이 실수의 결과입니다(아래는 앞 세 줄).

```
[확인 필요] ① 근무 데이터가 리포트에 빠짐없이 들어갔다 · 문제 8 개
   - TCK-1
   - TCK-2
```

- 2번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. 7번을 비워도 같은 오류가 납니다(문구는 파이썬 버전마다 조금 다릅니다).

```
IndentationError: expected an indented block
```

- 3번을 비워 두면 `decision` 이 만들어지지 않아 오류가 납니다. 8번 · 9번을 비워도 같은 꼴의 오류(`name 'report_problems'` · `name 'recovery_problems'`)가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'decision' is not defined
```

- 4번을 비워 두면 미리 채운 `wrong.append(…)` 줄이 바로 위 줄보다 오른쪽에서 시작해서(들여쓰기가 맞지 않아) 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- 4번에서 `!=` 대신 `==` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**맞게 나온 사례가 모두 문제로 나옵니다.**</mark> ② 가 「확인 필요 · 문제 7 개」로 나오는 것이 이 실수의 결과입니다(아래는 앞 두 줄).

```
[확인 필요] ② 위험 점수에 따라 자동 · 승인 필요 · 차단 금지가 맞게 나뉜다 · 문제 7 개
   - high 등급 한 명 (기대 자동, 결과 자동)
```

- 5번을 비워 두면 오류는 나지 않고 출력도 정답과 같습니다. 아래 `problems.append(…)` 줄이 위 `if` 안으로 들어가서, <mark style="background:#ffc4d6">**30분을 넘긴 복구를 찾지 못합니다.**</mark> 오늘 샘플은 두 신고 모두 30분 안이라 차이가 보이지 않으니, 출력이 맞아도 코드를 다시 읽어 확인합니다.
- 6번을 비워 두면 7번 줄이 `for` 바로 아래 줄이 되어 오류 없이 <mark style="background:#ffc4d6">**잠겨 있는 `dami` 도 「잠금이 풀림」으로 나옵니다.**</mark>

```
[확인 필요] ③ 오탐 복구가 30분 안에 빠짐없이 끝났고 진짜 공격의 잠금은 그대로다 · 문제 1 개
   - dami 잠금이 풀림
```

**관제에서는**

- 대응 절차와 자동 대응 규칙은 바꿀 때마다 시험 사례를 다시 실행해(회귀 시험) 확인합니다. <mark>기대한 결과를 적은 시험 사례를 경계값까지 포함해 계속 추가해 두면, 기준을 바꾼 뒤 무엇이 달라졌는지 바로 알 수 있습니다.</mark> 오늘의 사례 7개와 점검 세 가지는 예시입니다.
