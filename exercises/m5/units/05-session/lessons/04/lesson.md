---
id: m5-u05-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/124_day03_pm_rollback_drill.md
  mission_id: GichanSource.m5-1111-pm-rollback-drill
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## Exercise Exercise 5-2 정답

**채운 코드** (한 예)

`undo_actions.py` 의 1 · 2번입니다.

```python
    # 1. unlock_account(record["target"], state, record["incident"], "되돌리기: " + record["reason"]) 의 결과를 리턴한다
    return unlock_account(record["target"], state, record["incident"], "되돌리기: " + record["reason"])  # 계정 해제를 실행하고 기록을 리턴한다
    # 2. unblock_ip(record["target"], state, record["incident"], "되돌리기: " + record["reason"]) 의 결과를 리턴한다
    return unblock_ip(record["target"], state, record["incident"], "되돌리기: " + record["reason"])  # IP 해제를 실행하고 기록을 리턴한다
```

`rollback.py` 의 3 ~ 8번입니다.

```python
        # 3. record 의 "incident" 가 incident_id 와 같으면 (if, ==)
        if record["incident"] == incident_id:           # 그 인시던트의 기록이면
        # 4.   found 에 record 를 추가한다 (append)
            found.append(record)                        # 모아 둔다
    # 5. record 의 "before" 와 "after" 가 같으면 (if, ==)
    if record["before"] == record["after"]:             # 조치 전과 후가 같으면
    # 6.   False 를 리턴한다 (바뀐 것이 없으니 되돌릴 것도 없다)
        return False                                    # 바뀐 것이 없으니 되돌리지 않는다
        # 7. should_undo(record) 가 참이면 (if)
        if should_undo(record):                         # 자동이 바꾼 것이고 되돌릴 수 있으면
        # 8.   undo_record(record, state) 의 결과를 records 에 추가한다 (append)
            records.append(undo_record(record, state))  # 되돌리고 해제 기록을 모은다
```

`exercise7-1_run.py` 의 9번입니다.

```python
# 9. load_json(LOG_PATH) 의 결과를 log 에 저장한다 (Exercise 5-1가 저장한 조치 기록을 읽는다)
log = load_json(LOG_PATH)  # Exercise 5-1가 저장한 조치 기록을 읽는다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 5 의 잠긴 계정은 <mark style="background:#bde3ff">**`['junho']`**</mark>, 차단한 IP 는 <mark style="background:#bde3ff">**없음(`[]`)**</mark> 입니다.

```
--- 단계 1: Exercise 5-1가 남긴 파일
잠긴 계정: ['junho', 'dami']
조치 기록: 5 건
차단한 IP: ['198.51.100.90']
--- 단계 2: INC-001 은 오탐으로 확인됨 — 되돌리기
INC-001 dami · 되돌리기 불가 · 세션 2개 → 세션 0개 · 되돌릴 수 없는 조치(세션 종료) — 사용자가 다시 로그인해야 함
INC-001 dami · 계정 해제 · 잠김 → 잠기지 않음 · 되돌리기: 퇴사한 계정의 서버 요청
--- 단계 3: INC-006 도 오탐으로 확인됨 — 되돌리기
INC-006 junho · 되돌리기 불가 · 세션 1개 → 세션 0개 · 되돌릴 수 없는 조치(세션 종료) — 사용자가 다시 로그인해야 함
--- 단계 4: INC-005 도 오탐으로 확인됨 — 되돌리기
INC-005 198.51.100.90 · IP 해제 · 차단됨 → 차단되지 않음 · 되돌리기: 경로 스캔 (120분 뒤 자동 해제)
--- 단계 5: 되돌린 뒤 상태
잠긴 계정: ['junho']
차단한 IP: []
```

- (나) Exercise 5-1 기록에서 `junho` 의 계정 잠금은 <mark style="background:#bde3ff">`잠김 → 잠김`</mark> 으로, 조치 전부터 잠겨 있던 것이라 `before` 와 `after` 가 같습니다. `before` 와 `after` 가 같으면 `should_undo` 의 5 · 6번이 `False` 를 리턴하므로 해제 대상에서 빠졌습니다.
  - 5 · 6번이 없었다면 `junho` 의 잠금도 「계정 잠금」 기록이라 해제됐을 것입니다.
  - 그러면 자동 대응과 상관없이 원래 잠겨 있던 계정이 풀려 버립니다.
- (다) `되돌리기 불가` 줄은 세션 종료가 <mark style="background:#bde3ff">`before` 와 `after` 가 다르지만(`세션 2개 → 세션 0개`) `UNDOABLE_ACTIONS` 목록(해제 한 번으로 되돌릴 수 있는 계정 잠금 · IP 차단만 적어 둔 리스트)에 없는 조치라서</mark> 나옵니다. 끊긴 세션은 사용자가 다시 로그인해야 합니다.
  - 이 사실을 기록하지 않고 「모두 원래대로」라고만 보고하면 보고와 실제 상태가 다릅니다.
  - 사용자가 다시 로그인하라는 화면을 보고 문의해도, 세션을 끊었다는 기록이 없어 관제하는 사람이 원인을 찾지 못합니다.

**왜**: <mark>자동 조치를 되돌릴 때는 자동이 바꾼 것만 풀어야 하고, 되돌릴 수 없는 것은 되돌릴 수 없다고 남겨야 합니다.</mark> 그래서 조치 전 상태를 기록해 둬야 되돌릴 수 있습니다.

**자주 틀리는 곳**

- 1 · 2번을 비워 두면 되돌리기 함수가 아무 값도 리턴하지 않습니다. 그러면 `records` 에 「값이 없다」는 뜻의 `None` 이 들어가고, 출력하다가 오류가 납니다(`TypeError`, 타입 에러: 값의 종류가 맞지 않다는 오류). 3.15 에서는 오류가 난 줄 아래에 `~~~^^^` 표시가 더 붙을 수 있습니다.

```
TypeError: 'NoneType' object is not subscriptable
```

- 3 · 4번을 비워 두면 오류는 나지 않지만 <mark>**기록을 하나도 찾지 못해 아무것도 되돌려지지 않습니다.**</mark> 단계 2 ~ 4 에 아무 줄도 없고 단계 5 에 `dami` 와 `198.51.100.90` 이 남아 있으면 이 실수 때문입니다.

```
--- 단계 2: INC-001 은 오탐으로 확인됨 — 되돌리기
--- 단계 3: INC-006 도 오탐으로 확인됨 — 되돌리기
--- 단계 4: INC-005 도 오탐으로 확인됨 — 되돌리기
--- 단계 5: 되돌린 뒤 상태
잠긴 계정: ['junho', 'dami']
차단한 IP: ['198.51.100.90']
```

- 5 · 6번을 비워 두면 <mark>**조치 전부터 잠겨 있던 `junho` 까지 해제됩니다.**</mark> 단계 3 에 `계정 해제` 가 나오고 단계 5 의 잠긴 계정이 빈 리스트가 되면 이 실수 때문입니다.

```
--- 단계 3: INC-006 도 오탐으로 확인됨 — 되돌리기
INC-006 junho · 되돌리기 불가 · 세션 1개 → 세션 0개 · 되돌릴 수 없는 조치(세션 종료) — 사용자가 다시 로그인해야 함
INC-006 junho · 계정 해제 · 잠김 → 잠기지 않음 · 되돌리기: 이미 잠겨 있어 변경 없음
…
--- 단계 5: 되돌린 뒤 상태
잠긴 계정: []
차단한 IP: []
```

- 7 · 8번을 비워 두면 <mark>**되돌릴 수 없다는 표시만 나오고 실제 되돌리기는 하지 않습니다.**</mark>

```
--- 단계 2: INC-001 은 오탐으로 확인됨 — 되돌리기
INC-001 dami · 되돌리기 불가 · 세션 2개 → 세션 0개 · 되돌릴 수 없는 조치(세션 종료) — 사용자가 다시 로그인해야 함
…
--- 단계 5: 되돌린 뒤 상태
잠긴 계정: ['junho', 'dami']
차단한 IP: ['198.51.100.90']
```

- 9번을 비워 두면 `log` 가 만들어지지 않아 오류가 납니다(`NameError`, 네임 에러: 정의하지 않은 이름을 썼다는 오류).

```
NameError: name 'log' is not defined
```

**관제에서는**: 오탐 복구는 「풀기」보다 「어디까지 풀지 정하기」가 어렵습니다. <mark>조치 전 상태를 기록해 두면 자동이 한 것만 정확히 풀 수 있고, 되돌릴 수 없는 조치는 사람이 이어서 확인할 수 있습니다.</mark>

---

## Exercise Exercise 5-2 정답

**채운 코드** (한 예)

`drill.py` 의 1 ~ 5번입니다.

```python
    # 1. incident["reasons"] 의 규칙을 하나씩 꺼낸다 (for, rule)
    for rule in incident["reasons"]:          # 탐지된 규칙을 하나씩 꺼낸다
    # 2.   rule 이 CONTAINMENT_BY_RULE 안에 있으면 (if, in)
        if rule in CONTAINMENT_BY_RULE:       # 조치 표에 있는 규칙이면
    # 3.     CONTAINMENT_BY_RULE[rule] 을 리턴한다
            return CONTAINMENT_BY_RULE[rule]  # 그 규칙에 연결된 조치 이름을 리턴한다
    # 4. route 가 "승인 필요" 이면 (if, ==)
    if route == "승인 필요":                  # VIP 계정이라 승인이 필요한 경로이면
    # 5.   "승인 대기" 와 빈 리스트 [] 를 쉼표로 이어 함께 리턴한다 (담당자가 허락하기 전에는 조치하지 않는다)
        return "승인 대기", []                # 조치하지 않고 승인 대기로 둔다
```

`shift_report.py` 의 6 ~ 8번입니다.

```python
    # 6. "확인 실패" 가 record 의 "after" 안에 있는지(in)의 결과를 리턴한다
    return "확인 실패" in record["after"]       # 조치 후 상태에 확인 실패가 들어 있는지 확인한 결과를 리턴한다
    # 7. record 의 "before" 와 "after" 가 같은지(==)의 결과를 리턴한다
    return record["before"] == record["after"]  # 조치 전과 후가 같은지의 결과를 리턴한다
        # 8. counts[kind] 에 counts[kind] + 1 을 담는다 (그 종류의 건수를 1 늘린다)
        counts[kind] = counts[kind] + 1         # 그 종류의 건수를 1 늘린다
```

`exercise7-2_run.py` 의 9번입니다.

```python
    # 9. handle_incident(incident, state, refs) 가 리턴한 두 값을 status 와 records 에 한 번에 받는다
    status, records = handle_incident(incident, state, refs)  # 처리 결과 문장과 조치 기록을 한 번에 받는다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 3 의 요약은 <mark style="background:#bde3ff">**변경됨 2 · 변경 없음 2 · 확인 실패 1**</mark>이고, 단계 4 는 <mark style="background:#bde3ff">**4건**</mark>입니다.

```
--- 단계 1: 알림 8건 처리
INC-001 dami -> 조치함 (조치 기록 2건)
INC-002 seoyeon -> 조치하지 않음 (조치 기록 0건)
INC-003 gaeun -> 승인 대기 (조치 기록 0건)
INC-004 jiwoo -> 오탐 종료 (조치 기록 0건)
INC-005 198.51.100.90 -> 조치 실패 (조치 기록 1건)
INC-008 192.0.2.41 -> 승인 대기 (조치 기록 1건)
INC-009 192.0.2.10 -> 조치하지 않음 (조치 기록 1건)
INC-010 gaeun -> 승인 대기 (조치 기록 0건)
--- 단계 2: 조치 기록
INC-001 dami · 계정 잠금 · 잠기지 않음 → 잠김 · 퇴사한 계정
INC-001 dami · 세션 종료 · 세션 2개 → 세션 0개 · 퇴사한 계정
INC-005 198.51.100.90 · IP 차단 · 차단되지 않음 → 차단되지 않음 (확인 실패) · 방화벽 연결 실패
INC-008 192.0.2.41 · IP 차단 · 변경 없음 → 변경 없음 · 여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요
INC-009 192.0.2.10 · IP 차단 · 변경 없음 → 변경 없음 · 허용 목록 IP 라서 차단하지 않음
--- 단계 3: 근무 보고 요약
{'변경됨': 2, '변경 없음': 2, '확인 실패': 1}
잠긴 계정: ['junho', 'dami']
차단한 IP: []
--- 단계 4: 담당자 확인이 필요한 건
INC-003 gaeun : VIP 계정이라 담당자 승인이 필요함
INC-010 gaeun : VIP 계정이라 담당자 승인이 필요함
INC-005 198.51.100.90 : 조치 후 확인 실패 — 방화벽 연결 실패
INC-008 192.0.2.41 : 여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요
```

- (나) INC-005 는 `FIREWALL_DOWN_FOR` 에 들어 있어 방화벽 연결이 끊긴 상황으로 처리됩니다. 단계 2 의 줄이 <mark style="background:#bde3ff">`차단되지 않음 → 차단되지 않음 (확인 실패) · 방화벽 연결 실패`</mark> 라서 `is_failure` 가 참이 되어 `확인 실패` 로 셉니다.
  - 6번이 없으면 `is_failure` 는 값을 리턴하지 않습니다(`None`, 조건에서는 거짓으로 취급됩니다). 그러면 조치 전과 후의 글자가 달라서 「변경됨」으로 세어집니다. 그래서 <mark style="background:#bde3ff">차단되지 않은 건이 조치된 것처럼 보고에 들어갑니다.</mark>
- (다) INC-008 은 `ip_users.json` 을 보면 `junho` 와 `hana` 가 같은 IP 를 함께 씁니다. 그래서 `여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요` 이유로 <mark style="background:#bde3ff">승인 대기</mark> 입니다. INC-009 는 허용 목록의 점검 서버라서 `허용 목록 IP 라서 차단하지 않음` 이유로 <mark style="background:#bde3ff">조치하지 않음</mark> 입니다.
  - INC-003 과 INC-010 은 `gaeun` 이 VIP 라서 경로가 `승인 필요` 가 되고 4 · 5번에서 `승인 대기` 가 됩니다.
  - 그대로 자동 처리했다면 이런 영향이 생길 수 있었습니다. INC-008 은 `junho` 와 `hana` 가 접속하지 못합니다. INC-009 는 회사 점검 서버가 보내는 접속이 막혀 점검이 멈춥니다. INC-003 · INC-010 은 계정 관리 업무를 하는 VIP 계정 `gaeun` 의 알림이라 담당자 확인 없이 처리하면 안 됩니다(오전에 만든 조치 함수는 VIP 계정을 한 번 더 막아서 INC-010 에서는 `변경 없음` 으로 남깁니다).

**왜**: <mark>알림마다 판단 → 조치 → 기록을 이어서 자동으로 하면 사람이 알림을 하나씩 열어 보지 않아도 되고, 요약이 있으면 사람이 봐야 할 건만 남습니다.</mark> 실패를 숨기지 않고 따로 세는 것이 핵심입니다.

**자주 틀리는 곳**

- 1 ~ 3번을 비워 두면 <mark>**아무것도 조치하지 않습니다.**</mark> 퇴사자 `dami` 도 `조치하지 않음` 으로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 1: 알림 8건 처리
INC-001 dami -> 조치하지 않음 (조치 기록 0건)
INC-002 seoyeon -> 조치하지 않음 (조치 기록 0건)
INC-003 gaeun -> 승인 대기 (조치 기록 0건)
INC-004 jiwoo -> 오탐 종료 (조치 기록 0건)
INC-005 198.51.100.90 -> 조치하지 않음 (조치 기록 0건)
INC-008 192.0.2.41 -> 조치하지 않음 (조치 기록 0건)
INC-009 192.0.2.10 -> 조치하지 않음 (조치 기록 0건)
INC-010 gaeun -> 승인 대기 (조치 기록 0건)
```

- 4 · 5번을 비워 두면 VIP 계정의 `INC-010` 이 조치 함수를 호출하게 되어 <mark>**승인 대기가 아니라 「조치함」으로 표시됩니다.**</mark> 오전에 만든 함수는 VIP 계정을 잠그지 않고 `변경 없음` 기록만 남깁니다. 그런데 승인 대기로 두는 코드가 없어서 단계 4 의 확인 목록에 나오지 않습니다. `INC-003` 은 연결된 규칙이 없어 `조치하지 않음` 으로 나옵니다. 아래는 이 실수일 때 INC-010 에서 나오는 출력입니다.

```
INC-010 gaeun -> 조치함 (조치 기록 1건)
…
INC-010 gaeun · 계정 잠금 · 변경 없음 → 변경 없음 · VIP 계정이라 자동 조치 대상이 아님
```

- 6번을 비워 두면 오류는 나지 않지만 <mark>**확인 실패가 0 으로 나오고 단계 4 에서 INC-005 가 빠집니다.**</mark>

```
{'변경됨': 3, '변경 없음': 2, '확인 실패': 0}
…
--- 단계 4: 담당자 확인이 필요한 건
INC-003 gaeun : VIP 계정이라 담당자 승인이 필요함
INC-010 gaeun : VIP 계정이라 담당자 승인이 필요함
INC-008 192.0.2.41 : 여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요
```

- 7번을 비워 두면 「변경 없음」이 0 으로 나옵니다.

```
{'변경됨': 4, '변경 없음': 0, '확인 실패': 1}
```

- 8번을 비워 두면 모든 종류가 0 으로 나옵니다.

```
{'변경됨': 0, '변경 없음': 0, '확인 실패': 0}
```

- 9번을 비워 두면 `status` 가 만들어지지 않아 오류가 납니다(`NameError`). 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 붙을 수 있습니다.

```
NameError: name 'status' is not defined
```

**관제에서는**: 근무 교대에서 가장 중요한 것은 「자동이 한 일」이 아니라 「사람이 이어서 해야 할 일」입니다. <mark>확인 실패와 승인 대기를 따로 세어 목록으로 넘기면</mark> 실패한 조치가 아무도 모르게 넘어가지 않습니다.

---

## 정답 마무리

- (가) 한 예: <mark>`git status` 에서 `.env` 와 `.venv` 가 보이지 않았습니다.</mark> `__pycache__` 가 보여서 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 다시 확인했습니다.
- 깃허브 `soar_response` 폴더에 오늘 만든 `.py` 파일이 보이면 됩니다.
