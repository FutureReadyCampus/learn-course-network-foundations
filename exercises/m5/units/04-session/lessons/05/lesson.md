---
id: m5-u04-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/122_day03_am_containment.md
  mission_id: GichanSource.m5-1111-am-containment
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답 보는 법

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## 실습 4-1 정답

**채운 코드** (한 예)

`containment_store.py` 의 1 · 2번입니다.

```python
    # 1. 키 "action"(action), "target"(target), "incident"(incident_id), "before"(before), "after"(after), "reason"(reason) 를 가진 딕셔너리를 record 에 저장한다
    record = {"action": action, "target": target, "incident": incident_id, "before": before, "after": after, "reason": reason}  # 조치 한 건의 기록을 딕셔너리로 만든다
    # 2. log 에 record 를 추가한다 (append)
    log.append(record)  # 기록 한 건을 리스트에 추가한다
```

`account_actions.py` 의 3 ~ 7번입니다.

```python
    # 3. user 가 vip_accounts 안에 있으면 (if, in)
    if user in vip_accounts:                         # VIP 계정이면
    # 4.   "VIP 계정이라 자동 조치 대상이 아님" 을 리턴한다
        return "VIP 계정이라 자동 조치 대상이 아님"  # 막는 이유를 리턴한다
    # 5. user 가 state["locked_users"] 안에 있는지(in)의 결과를 리턴한다
    return user in state["locked_users"]             # 잠긴 계정 리스트 안에 있는지 확인한 결과를 리턴한다
    # 6. state["locked_users"] 에 user 를 추가한다 (append)
    state["locked_users"].append(user)               # 잠긴 계정 리스트에 추가한다
    # 7. state["locked_users"] 에서 user 를 제거한다 (remove)
    state["locked_users"].remove(user)               # 잠긴 계정 리스트에서 제거한다
```

`exercise4-1_run.py` 의 8 · 9번입니다.

```python
    # 8. lock_account(user, state, vip_accounts, incident_id, reason) 의 결과를 record 에 저장한다
    record = lock_account(user, state, vip_accounts, incident_id, reason)  # 계정을 잠그고 기록을 받는다
    # 9. append_log(record) 를 호출한다 (조치 기록을 파일에 남긴다)
    append_log(record)                                                     # 조치 기록을 파일에 남긴다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 4 의 잠긴 계정은 <mark style="background:#bde3ff">**`['junho']`**</mark>, 조치 기록은 <mark style="background:#bde3ff">**4건**</mark>입니다.

```
--- 단계 1: 조치 전에 잠겨 있는 계정
['junho']
--- 단계 2: 잠금 요청 3건
INC-001 dami · 잠기지 않음 → 잠김 · 퇴사한 계정의 서버 요청
INC-003 gaeun · 변경 없음 → 변경 없음 · VIP 계정이라 자동 조치 대상이 아님
INC-006 junho · 잠김 → 잠김 · 이미 잠겨 있어 변경 없음
--- 단계 3: 오탐으로 확인되어 dami 해제
INC-001 dami · 잠김 → 잠기지 않음 · 오탐으로 확인되어 해제
--- 단계 4: 파일에 저장된 값 다시 읽기
잠긴 계정: ['junho']
조치 기록: 4 건
```

- (나) 단계 2 의 INC-003 줄이 <mark style="background:#bde3ff">`변경 없음 → 변경 없음 · VIP 계정이라 자동 조치 대상이 아님`</mark> 입니다. `check_policy` 가 `gaeun` 이 `vip_accounts` 에 포함된 것을 확인하고 잠금을 차단했습니다.
  - 경로에서 이미 VIP 를 `승인 필요` 로 분기해도 조치 함수가 정책을 한 번 더 검사하는 이유: 경로 설정이 잘못될 수 있고, 경로를 거치지 않고 다른 코드가 이 함수를 직접 호출할 수도 있기 때문입니다.
  - 이처럼 통제를 한 지점에만 두지 않고 여러 지점에 중복해서 두는 설계를 심층 방어(defense in depth, 디펜스 인 뎁스: 한 통제가 실패해도 다른 통제가 보완하도록 여러 단계로 방어하는 전략)라고 합니다. 한 지점에서 누락돼도 다음 지점에서 차단해야 계정 관리자 계정이 잠기지 않습니다.
- (다) `before` 가 있으면 <mark style="background:#bde3ff">조치 전부터 잠겨 있던 계정(`junho`)과 이번 자동 대응이 잠근 계정(`dami`)을 구별</mark>할 수 있어서, 롤백할 때 자동 대응이 변경한 계정만 해제할 수 있습니다.
  - 사후 검증이 없으면 잠금 호출이 실패해도 「잠갔다」고 기록됩니다. 사후 검증이 있으면 `잠기지 않음 (확인 실패)` 로 남아 기록과 실제 상태가 일치합니다.

**왜**: <mark>조치는 실행만으로 완료되지 않습니다. 사후 검증으로 실제 상태 변경을 확인하고, 조치 전 · 후 상태를 기록해야 결과를 신뢰할 수 있고 롤백할 수 있습니다.</mark>

**자주 틀리는 곳**

- 1번을 비워 두면 기록 딕셔너리를 만들지 못해 오류가 납니다(`NameError`, 네임 에러: 정의하지 않은 이름을 썼다는 오류). 이름이 비슷한 변수가 있으면 파이썬 버전에 따라 뒤에 `Did you mean: …`(「혹시 이것을 말한 건가요?」라는 추천 문구)이 붙을 수 있습니다.

```
NameError: name 'record' is not defined
```

- 2번을 비워 두면 오류 없이 <mark>**기록이 하나도 파일에 남지 않습니다.**</mark> 단계 4 의 조치 기록이 0건으로 나옵니다.

```
--- 단계 4: 파일에 저장된 값 다시 읽기
잠긴 계정: ['junho']
조치 기록: 0 건
```

- 3 · 4번을 비워 두면 <mark>**VIP 인 `gaeun` 이 잠깁니다.**</mark> 단계 2 의 INC-003 줄이 `잠기지 않음 → 잠김` 으로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 2: 잠금 요청 3건
INC-001 dami · 잠기지 않음 → 잠김 · 퇴사한 계정의 서버 요청
INC-003 gaeun · 잠기지 않음 → 잠김 · 여러 로그 연결
INC-006 junho · 잠김 → 잠김 · 이미 잠겨 있어 변경 없음
```

- 5번을 비워 두면 확인 함수가 아무것도 리턴하지 않습니다. 그러면 잠겼는지 확인할 때마다 「잠기지 않음」으로 판단되어, <mark>**이번에 잠그려던 `dami` 가 실제로 잠겼는데도 「확인 실패」로 기록됩니다.**</mark> 원인이 확인 함수의 리턴값에 있다는 점이 6번과 다릅니다.

```
--- 단계 2: 잠금 요청 3건
INC-001 dami · 잠기지 않음 → 잠기지 않음 (확인 실패) · 퇴사한 계정의 서버 요청
INC-003 gaeun · 변경 없음 → 변경 없음 · VIP 계정이라 자동 조치 대상이 아님
INC-006 junho · 잠김 → 잠김 · 이미 잠겨 있어 변경 없음
```

- 6번을 비워 두면 오류는 나지 않지만 <mark>**잠그는 줄이 없어 실제로 잠기지 않은 `dami` 의 잠금 실패가 사후 검증에서 드러납니다.**</mark> 5번과 달리 확인 함수는 정상이고, 계정을 잠그는 줄만 빠진 경우입니다. 두 경우 모두 사후 검증이 있어서 `잠기지 않음 (확인 실패)` 로 드러납니다.

```
--- 단계 2: 잠금 요청 3건
INC-001 dami · 잠기지 않음 → 잠기지 않음 (확인 실패) · 퇴사한 계정의 서버 요청
INC-003 gaeun · 변경 없음 → 변경 없음 · VIP 계정이라 자동 조치 대상이 아님
INC-006 junho · 잠김 → 잠김 · 이미 잠겨 있어 변경 없음
```

- 7번을 비워 두면 해제 호출이 끝나도 <mark>**계정이 그대로 잠겨 있습니다.**</mark> 사후 검증이 있어서 기록에 `잠김 → 잠김 (확인 실패)` 로 나타나고, 단계 4 의 잠긴 계정에도 `dami` 가 남습니다.

```
--- 단계 3: 오탐으로 확인되어 dami 해제
INC-001 dami · 잠김 → 잠김 (확인 실패) · 오탐으로 확인되어 해제
```

- 8 · 9번을 비워 두면 `record` 가 만들어지지 않아 오류가 납니다(`NameError`).

```
NameError: name 'record' is not defined
```

**관제에서는**: 사후 검증(조치 후 확인)은 「명령은 오류 없이 종료됐지만 실제로는 적용되지 않은」 결함을 탐지하는 방법 중 하나입니다. <mark>조치 전 상태를 기록해 두면 오탐을 복구(롤백)할 때 원래 상태로 정확히 복원할 수 있습니다.</mark>

---

## 실습 4-2 정답

**채운 코드** (한 예)

`ip_actions.py` 의 1 ~ 6번입니다.

```python
    # 1. ip 가 allowlist_ips 안에 있는지(in)의 결과를 리턴한다
    return ip in allowlist_ips                                                                # 허용 목록 안에 있는지 확인한 결과를 리턴한다
    # 2. ip_users.get(ip, []) 의 개수(len)를 리턴한다 (목록에 없으면 빈 리스트로 본다)
    return len(ip_users.get(ip, []))                                                          # 그 IP 를 쓰는 계정 수를 리턴한다 (목록에 없으면 0)
    # 3. state["blocked_ips"] 에 ip 를 추가한다 (append)
    state["blocked_ips"].append(ip)                                                           # 차단한 IP 리스트에 추가한다
    # 4. state["block_expiry"][ip] 에 state["clock"] + ttl 을 저장한다 (끝나는 시각)
    state["block_expiry"][ip] = state["clock"] + ttl                                          # 차단이 끝나는 시각을 적는다
        # 5. end_time 이 state["clock"] 이하이면 (if, <=)
        if end_time <= state["clock"]:                                                        # 끝나는 시각이 지났으면
        # 6.   unblock_ip(ip, state, incident_id, "차단 시간이 끝나 자동 해제") 의 결과를 records 에 추가한다 (append)
            records.append(unblock_ip(ip, state, incident_id, "차단 시간이 끝나 자동 해제"))  # 차단을 풀고 해제 기록을 모은다
```

`exercise4-2_run.py` 의 7 ~ 9번입니다.

```python
    # 7. check_ip_policy(ip, allowlist_ips, ip_users) 의 결과를 refusal 에 저장한다
    refusal = check_ip_policy(ip, allowlist_ips, ip_users)              # 자동 차단을 막을 이유를 구한다
    # 8. refusal 이 빈 글자("")이면 (if, ==)
    if refusal == "":                                                   # 막을 이유가 없으면
    # 9.   block_ip(ip, state, incident_id, reason, DEFAULT_TTL) 의 결과를 record 에 저장한다 (실제로 차단한 기록으로 바꾼다)
        record = block_ip(ip, state, incident_id, reason, DEFAULT_TTL)  # 실제로 차단하고 기록을 받는다
```

**결과**

- (가) 출력은 다음과 같습니다. 실제로 차단된 IP 는 <mark style="background:#bde3ff">**`198.51.100.90`**</mark>, 차단하지 않은 IP 는 `192.0.2.10`(허용 목록 IP)과 `192.0.2.41`(공유 IP)입니다.

```
--- 단계 1: 차단 요청 3건
INC-005 198.51.100.90 · 차단되지 않음 → 차단됨 · 경로 스캔 (120분 뒤 자동 해제)
INC-009 192.0.2.10 · 변경 없음 → 변경 없음 · 허용 목록 IP 라서 차단하지 않음
INC-008 192.0.2.41 · 변경 없음 → 변경 없음 · 여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요
--- 단계 2: 차단 뒤 차단한 IP 와 끝나는 시각
차단한 IP: ['198.51.100.90']
차단이 끝나는 시각(분): {'198.51.100.90': 120}
--- 단계 3: 시계를 120분 뒤로 옮기고 시간이 끝난 차단 풀기
INC-005 198.51.100.90 · 차단됨 → 차단되지 않음 · 차단 시간이 끝나 자동 해제
차단한 IP: []
--- 단계 4: 파일에 저장된 값 다시 읽기
차단한 IP: []
조치 기록: 4 건
```

- (나) `ip_users.json` 에서 `192.0.2.41` 을 쓰는 계정은 <mark style="background:#bde3ff">`junho` 와 `hana` 두 명</mark>이라서 임계값(threshold, 쓰레숄드: 판정 기준이 되는 값) `SHARED_IP_LIMIT`(2) 명 이상에 해당합니다.
  - 그대로 차단했다면 두 사람이 모두 접속하지 못했을 것입니다.
  - 공격으로 의심된 접속이 한 사람의 것이었더라도 다른 사람의 업무가 함께 중단됩니다(부수적 피해).
  - 그래서 자동 차단하지 않고 담당자 승인을 받게 합니다.
- (다) 단계 2 의 만료 시각이 <mark style="background:#bde3ff">120</mark> 이고 단계 3 에서 시계를 120분 뒤로 옮겼습니다. 그러면 시계가 120이 되어 만료 시각 120과 같아집니다. 그래서 `end_time <= clock` 조건이 참이 되었고, 차단이 해제되었습니다.
  - 유효 기간이 있는 임시 차단은 사람의 해제 작업 없이 만료되므로 오래된 차단이 누적되지 않고, 필요하면 다시 차단하면 됩니다. 영구 차단은 사람이 사유를 확인한 뒤에 결정합니다.

**왜**: <mark>차단은 정상 사용자와 필요한 서버의 가용성(availability, 어베일러빌리티: 서비스를 필요할 때 쓸 수 있는 상태)까지 해칠 수 있으므로, 차단 전에 영향 범위를 확인하고 만료 시각을 함께 정해야 안전합니다.</mark>

**자주 틀리는 곳**

- 1번을 비워 두면 허용 목록 확인 함수가 아무것도 리턴하지 않아, 허용 목록에 없는 것으로 판단되어 <mark>**회사의 점검 서버 `192.0.2.10` 이 차단됩니다.**</mark> 단계 1 의 INC-009 줄이 `차단됨` 으로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 1: 차단 요청 3건
INC-005 198.51.100.90 · 차단되지 않음 → 차단됨 · 경로 스캔 (120분 뒤 자동 해제)
INC-009 192.0.2.10 · 차단되지 않음 → 차단됨 · 경로 스캔 (120분 뒤 자동 해제)
INC-008 192.0.2.41 · 변경 없음 → 변경 없음 · 여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요
```

- 2번을 비워 두면 사용 계정 수를 구하지 못해 비교에서 오류가 납니다.

```
TypeError: '>=' not supported between instances of 'NoneType' and 'int'
```

- 3번을 비워 두면 오류는 나지 않지만 <mark>**차단 실패가 사후 검증에서 드러납니다.**</mark> `차단되지 않음 (확인 실패)` 로 기록됩니다.

```
INC-005 198.51.100.90 · 차단되지 않음 → 차단되지 않음 (확인 실패) · 경로 스캔 (120분 뒤 자동 해제)
```

- 4번을 비워 두면 만료 시각이 없어 시간이 끝난 차단을 푸는 단계에서 오류가 납니다(`KeyError`, 키 에러: 딕셔너리에 없는 키를 꺼냈다는 오류).

```
KeyError: '198.51.100.90'
```

- 5 · 6번을 비워 두면 <mark>**차단이 만료되지 않고 계속 유지됩니다.**</mark> 단계 3 에서 시계가 120분을 가리키는데도 차단한 IP 가 남아 있는 것이 이 실수의 결과입니다.

```
--- 단계 3: 시계를 120분 뒤로 옮기고 시간이 끝난 차단 풀기
차단한 IP: ['198.51.100.90']
```

- 7번을 비워 두면 `refusal` 이 만들어지지 않아 오류가 납니다(`NameError`).

```
NameError: name 'refusal' is not defined
```

- 8 · 9번을 비워 두면 <mark>**아무것도 차단되지 않고 첫 줄의 이유가 빈 문자열로 나옵니다.**</mark>

```
--- 단계 1: 차단 요청 3건
INC-005 198.51.100.90 · 변경 없음 → 변경 없음 ·
INC-009 192.0.2.10 · 변경 없음 → 변경 없음 · 허용 목록 IP 라서 차단하지 않음
INC-008 192.0.2.41 · 변경 없음 → 변경 없음 · 여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요
```

**관제에서는**: 차단 규칙에는 허용 목록(allowlist) 검사와 공유 IP 여부 검사를 함께 둡니다. 두 검사는 차단이 정상 업무에 미치는 영향 범위를 줄입니다. <mark>임시 차단에 만료 시각을 두면 자동 대응이 만든 차단이 계속 늘어나 아무도 관리하지 않게 되는 일을 방지합니다.</mark>

---

## 실습 4-3 정답

**채운 코드** (한 예)

`session_actions.py` 의 1 ~ 3번입니다.

```python
    # 1. state["sessions"][user] 에 빈 리스트를 저장한다 (세션을 모두 종료한다)
    state["sessions"][user] = []  # 그 계정의 세션 리스트를 비운다
        # 2. open_count 가 0 보다 크면 (if, >)
        if open_count > 0:        # 열린 세션이 남아 있으면
        # 3.   gaps 에 user 를 추가한다 (append)
            gaps.append(user)     # 빈틈이 있는 계정으로 모은다
```

`containment.py` 의 4 ~ 6번입니다.

```python
    # 4. lock_account(user, state, vip_accounts, incident_id, reason) 의 결과를 lock_record 에 저장한다
    lock_record = lock_account(user, state, vip_accounts, incident_id, reason)  # 계정을 먼저 잠그고 기록을 받는다
    # 5. lock_record 의 "after" 가 "잠김" 이면 (if, ==)
    if lock_record["after"] == "잠김":                                          # 잠금이 확인됐으면
    # 6.   terminate_sessions(user, state, incident_id, reason) 의 결과를 records 에 추가한다 (append)
        records.append(terminate_sessions(user, state, incident_id, reason))    # 이어서 세션을 종료하고 기록을 모은다
```

`exercise4-3_run.py` 의 7 ~ 9번입니다.

```python
    # 7. contain_account(user, state, vip_accounts, incident_id, reason) 의 결과를 records 에 저장한다
    records = contain_account(user, state, vip_accounts, incident_id, reason)  # 잠금 → 세션 종료를 하고 기록 리스트를 받는다
# 8. find_open_sessions(state) 의 결과를 gaps_after 에 저장한다
gaps_after = find_open_sessions(state)                                         # 조치 뒤 다시 점검한다
# 9. save_state(state) 를 호출한다 (상태를 파일에 저장한다)
save_state(state)                                                              # 상태를 파일에 저장한다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 3 에서 빈틈이 남은 계정은 <mark style="background:#bde3ff">**없음(`[]`)**</mark>, 단계 4 의 잠긴 계정은 <mark style="background:#bde3ff">**`['junho', 'dami']`**</mark> 입니다.

```
--- 단계 1: 점검 — 잠겼는데 세션이 열려 있는 계정
['junho']
--- 단계 2: 잠금 → 세션 종료
INC-001 dami · 잠기지 않음 → 잠김 · 퇴사한 계정의 서버 요청
INC-001 dami · 세션 2개 → 세션 0개 · 퇴사한 계정의 서버 요청
INC-003 gaeun · 변경 없음 → 변경 없음 · VIP 계정이라 자동 조치 대상이 아님
INC-006 junho · 잠김 → 잠김 · 이미 잠겨 있어 변경 없음
INC-006 junho · 세션 1개 → 세션 0개 · 퇴사 처리 확인
--- 단계 3: 조치 뒤 다시 점검
빈틈이 남은 계정: []
잠긴 계정: ['junho', 'dami']
--- 단계 4: 파일에 저장된 값 다시 읽기
잠긴 계정: ['junho', 'dami']
조치 기록: 5 건
```

- (나) `junho` 는 수업 전부터 <mark style="background:#bde3ff">잠겨 있지만 세션 `S-501` 이 열려 있어</mark> 점검에서 탐지됐습니다. `dami` 는 단계 2 에서 `계정 잠금` 과 `세션 종료`(세션 2개 → 0개) 두 가지를 받았습니다.
  - 잠금만 했다면 `dami` 의 세션 `S-101` · `S-102` 가 유효한 채 남아, 잠금 뒤에도 그 세션으로 서버에 요청할 수 있었을 것입니다.
- (다) `gaeun` 은 `lock_account` 의 기록이 <mark style="background:#bde3ff">`변경 없음 → 변경 없음`</mark> 이라 5번의 `lock_record["after"] == "잠김"` 이 거짓이 되어 세션 종료를 실행하지 않습니다.
  - 잠기지 않은 계정의 세션을 종료하면 정상 사용자의 접속만 중단됩니다. 계정은 잠기지 않았으므로 다시 로그인할 수 있어서, 접속을 차단하는 효과는 없습니다.
  - 특히 VIP 계정은 승인 전에 접속이 종료되면 업무가 중단됩니다.

**왜**: <mark>잠금은 새 로그인만 차단하므로, 이미 열린 세션을 종료하고 잔존 세션(빈틈)이 없는지 재점검해야 봉쇄 조치가 완료됩니다.</mark>

**자주 틀리는 곳**

- 1번을 비워 두면 오류는 나지 않지만 <mark>**세션이 그대로 남습니다.**</mark> 기록이 `세션 2개 → 세션 2개` 로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 2: 잠금 → 세션 종료
INC-001 dami · 잠기지 않음 → 잠김 · 퇴사한 계정의 서버 요청
INC-001 dami · 세션 2개 → 세션 2개 · 퇴사한 계정의 서버 요청
INC-003 gaeun · 변경 없음 → 변경 없음 · VIP 계정이라 자동 조치 대상이 아님
INC-006 junho · 잠김 → 잠김 · 이미 잠겨 있어 변경 없음
INC-006 junho · 세션 1개 → 세션 1개 · 퇴사 처리 확인
```

- 2 · 3번을 비워 두면 점검이 항상 빈 리스트를 리턴해서 <mark>**`junho` 의 빈틈을 탐지하지 못합니다.**</mark>

```
--- 단계 1: 점검 — 잠겼는데 세션이 열려 있는 계정
[]
```

- 5 · 6번을 모두 비워 두면 <mark>**잠금만 하고 세션을 종료하지 않아 빈틈이 남습니다.**</mark> 단계 3 의 재점검에서 `dami` 와 `junho` 가 나오는 것이 이 실수의 결과입니다.

```
--- 단계 1: 점검 — 잠겼는데 세션이 열려 있는 계정
['junho']
…
--- 단계 3: 조치 뒤 다시 점검
빈틈이 남은 계정: ['junho', 'dami']
잠긴 계정: ['junho', 'dami']
```

- 4번을 비워 두면 `lock_record` 가 만들어지지 않아 오류가 납니다(`NameError`).

```
NameError: name 'lock_record' is not defined
```

- 7번을 비워 두면 `records` 가 만들어지지 않아 오류가 납니다(`NameError`).

```
NameError: name 'records' is not defined
```

- 9번을 비워 두면 상태가 저장되지 않아 단계 4 가 이전 실행에서 저장된 파일을 읽거나, 처음 실행이면 파일이 없다는 오류(`FileNotFoundError`)가 납니다.

**관제에서는**: 계정 잠금 뒤에는 열린 세션을 종료하는 것까지가 하나의 봉쇄 조치입니다. <mark>잠긴 계정에 활성 세션이 남았는지 정기적으로 점검하는 것</mark>은 자동 대응의 누락을 탐지하는 방법 중 하나입니다.
