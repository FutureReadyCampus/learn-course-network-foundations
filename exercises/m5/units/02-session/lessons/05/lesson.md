---
id: m5-u02-l05
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/118_day02_am_context_route_safety.md
  mission_id: GichanSource.m5-1110-am-context-route-safety
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## Exercise 2-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise2-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — `enrichment.py` 의 1 ~ 6번입니다.

```python
    # 1. entity 가 users_info 안에 있으면 (if, in)
    if entity in users_info:                                       # 계정 정보에 있는 대상이면
    # 2.   account 의 "employed" 에 users_info[entity]["employed"] 를 담는다
        account["employed"] = users_info[entity]["employed"]       # 재직 여부를 담는다
    # 3.   account 의 "vip" 에 users_info[entity]["vip"] 를 담는다
        account["vip"] = users_info[entity]["vip"]                 # VIP 여부를 담는다
    # 4. entity 가 source_ips 안에 있으면 (if, in)
    if entity in source_ips:                                       # 접속 IP 를 아는 대상이면
    # 5.   ip_info 의 "source_ip" 에 source_ips[entity] 를 담는다
        ip_info["source_ip"] = source_ips[entity]                  # 접속 IP 를 담는다
    # 6.   ip_info 의 "ip_trusted" 에 source_ips[entity] 가 trusted_ips 안에 있는지(in)의 결과를 담는다
        ip_info["ip_trusted"] = source_ips[entity] in trusted_ips  # 신뢰 IP 안에 있는지 확인한 결과를 담는다
```

`exercise2-1_run.py` 의 7 ~ 9번입니다.

```python
    # 7. enrich_incident(incident, users_info, source_ips, trusted_ips) 를 호출한다 (인시던트에 맥락이 붙는다)
    enrich_incident(incident, users_info, source_ips, trusted_ips)  # 맥락을 붙인다
    # 8. context 의 "vip" 가 참이면 (if)
    if context["vip"]:                                              # VIP 계정이면
    # 9.   vip_count 에 vip_count + 1 을 담는다 (1 늘린다)
        vip_count = vip_count + 1                                   # VIP 계정 알림 수를 1 늘린다
```

**결과**

- (가) 출력은 다음과 같습니다. 재직 여부가 「퇴사」인 알림은 <mark style="background:#bde3ff">**INC-001**</mark>, VIP 가 「예」인 알림은 <mark style="background:#bde3ff">**INC-003**</mark> 이고, 단계 3 의 VIP 계정 알림 수는 <mark style="background:#bde3ff">**1건**</mark>입니다.

```
--- 단계 1: 불러온 알림 5 건 · 계정 정보 6 명 · 신뢰 IP 1 개
--- 단계 2: 알림마다 붙인 정보(재직 · VIP · 접속 IP)
INC-001 dami · 재직: 퇴사 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
INC-002 seoyeon · 재직: 재직 · VIP: 아니오 · 접속 IP: 203.0.113.80 · 신뢰 IP: 예
INC-003 gaeun · 재직: 재직 · VIP: 예 · 접속 IP: 198.51.100.77 · 신뢰 IP: 아니오
INC-004 jiwoo · 재직: 재직 · VIP: 아니오 · 접속 IP: 203.0.113.80 · 신뢰 IP: 예
INC-005 198.51.100.90 · 재직: 계정 아님 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
--- 단계 3: VIP 계정 알림 수
VIP 계정 알림 1 건
```

- (나) INC-005 의 대상 `198.51.100.90` 은 <mark style="background:#bde3ff">`users_info` 에도 `source_ips` 에도 키로 없습니다.</mark>
  - 근거: `lookup_account` 의 `if entity in users_info:`(1번)와 `lookup_source_ip` 의 `if entity in source_ips:`(4번)가 모두 거짓이라 `if` 안의 2 · 3번과 5 · 6번이 실행되지 않고, 초기값(`False` · `None`)이 그대로 남습니다.
  - 문제: 확인되지 않은 대상의 `employed` 가 `True`(재직)로 판정되면 사용자 계정이 아닌 IP 를 「재직 중인 정상 사용자」로 오인하게 되어, 이후 경로 판단이 잘못됩니다. 확인되지 않은 대상은 「확인되지 않음」을 뜻하는 `False` 로 유지해야 안전합니다.
- (다) 두 알림의 `reasons` 는 다릅니다.
  - INC-002: `평소와 다른 IP` · <mark style="background:#bde3ff">**`대량 다운로드`**</mark>. INC-004: `업무 시간 밖 로그인` · `평소와 다른 IP`.
  - 신뢰 IP 라는 사실은 「IP 때문에 발생한 알림」이 정상이라는 근거가 되지만, `대량 다운로드` 는 IP 와 무관한 행위라서 신뢰 IP 가 정상이라는 근거가 되지 못합니다. IP 맥락이 같아도 <mark>동일하게 처리하면 안 됩니다.</mark> 이 차이는 Exercise 2-2의 조건 분기에서 반영합니다.

**왜**

- <mark>조치 실행 전에 알림을 보강하면, 프로그램이 알림의 맥락에 따라 대응을 달리할 수 있습니다.</mark> 맥락이 없으면 모든 알림이 대상 이름과 등급만 다른 동일한 알림으로 보입니다.

**자주 틀리는 곳**

- 4번의 `if` 를 빼고 5 · 6번만 쓰면 `source_ips` 에 없는 대상에서 오류가 납니다. <mark>**딕셔너리에서 꺼내기 전에 `in` 으로 키가 있는지 먼저 확인합니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`KeyError: 'dami'`</mark>, 키 에러: 딕셔너리에 없는 키를 꺼내려 할 때 나는 오류). `dami` 는 `source_ips.json` 에 없는 키입니다.

```
KeyError: 'dami'
```

- 6번을 빠뜨리면 오류는 나지 않지만 <mark>**신뢰 IP 가 모두 「아니오」로 나옵니다.**</mark> INC-002 와 INC-004 의 접속 IP 는 `203.0.113.80` 인데 신뢰 IP 가 「아니오」인 것이 이 실수의 결과입니다.

```
INC-001 dami · 재직: 퇴사 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
INC-002 seoyeon · 재직: 재직 · VIP: 아니오 · 접속 IP: 203.0.113.80 · 신뢰 IP: 아니오
INC-003 gaeun · 재직: 재직 · VIP: 예 · 접속 IP: 198.51.100.77 · 신뢰 IP: 아니오
```

- 두 함수를 채우지 않고 실행하면 <mark>**오류 없이 계정 정보에 있는 대상이 모두 「퇴사」로 나오고 VIP 계정 알림이 0건입니다.**</mark> `employed` 의 초기값이 `False` 이기 때문이며, 오류가 발생하지 않아도 출력 내용이 올바른지 직접 읽고 검증해야 합니다.

```
--- 단계 2: 알림마다 붙인 정보(재직 · VIP · 접속 IP)
INC-001 dami · 재직: 퇴사 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
INC-002 seoyeon · 재직: 퇴사 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
INC-003 gaeun · 재직: 퇴사 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
INC-004 jiwoo · 재직: 퇴사 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
INC-005 198.51.100.90 · 재직: 계정 아님 · VIP: 아니오 · 접속 IP: 없음 · 신뢰 IP: 아니오
--- 단계 3: VIP 계정 알림 수
VIP 계정 알림 0 건
```

- 실행 파일의 7번을 비워 두면 맥락이 추가되지 않아 오류가 발생합니다. <mark>**보강 함수를 호출해야 `incident["context"]` 가 생성됩니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`KeyError: 'context'`</mark>).

```
KeyError: 'context'
```

- 9번에서 `vip_count + 1` 대신 `vip_count` 를 그대로 다시 저장하면 오류는 나지 않지만 <mark>**VIP 계정 알림이 항상 0건으로 나옵니다.**</mark> 센 값이 늘지 않기 때문입니다.

```
--- 단계 3: VIP 계정 알림 수
VIP 계정 알림 0 건
```

**관제에서는**

- 알림을 열었을 때 대상의 맥락이 이미 추가되어 있으면 분석 시간이 크게 단축됩니다. <mark>알림 보강은 SOAR(Security Orchestration, Automation and Response, 쏘아: 정해 둔 절차대로 대응을 자동으로 실행하는 체계)의 플레이북에서 조치를 실행하기 전에 흔히 두는 단계입니다.</mark> 오늘은 JSON 파일에서 정보를 읽었지만, 실제 환경에서는 인사 시스템이나 IAM 같은 외부 시스템에서 조회하도록 바꿔도 맥락을 추가하는 방식은 같습니다.

---

## Exercise 2-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise2-2_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — `routing.py` 의 1 ~ 7번입니다.

```python
    # 1. incident["reasons"] 의 규칙을 하나씩 꺼낸다 (for, rule)
    for rule in incident["reasons"]:                                               # 탐지된 규칙을 하나씩 꺼낸다
    # 2.   rule 이 IP_RELATED_RULES 안에 없으면 (if, not in)
        if rule not in IP_RELATED_RULES:                                           # IP 관련 규칙이 아닌 것이 있으면
    # 3.     False 를 리턴한다 (IP 와 관계없는 다른 증거가 있다)
            return False                                                           # 다른 증거가 있으니 False 를 리턴한다
    # 4. context 의 "vip" 가 참이면 (if)
    if context["vip"]:                                                             # VIP 계정이면
    # 5.   "승인 필요" 와 "VIP 계정이라 담당자 승인이 필요함" 을 쉼표로 이어 함께 리턴한다
        return "승인 필요", "VIP 계정이라 담당자 승인이 필요함"                    # 경로와 이유를 함께 리턴한다
    # 6. context 의 "ip_trusted" 가 참이고(and) is_only_ip_related(incident) 가 참이면 (if)
    if context["ip_trusted"] and is_only_ip_related(incident):                     # 신뢰 IP 이고 규칙이 모두 IP 관련이면
    # 7.   "오탐 종료" 와 "신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄" 을 쉼표로 이어 함께 리턴한다
        return "오탐 종료", "신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄"  # 경로와 이유를 함께 리턴한다
```

`exercise2-2_run.py` 의 8 · 9번입니다.

```python
    # 8. decide_route(incident) 가 리턴한 두 값을 route 와 reason 에 한 번에 받는다
    route, reason = decide_route(incident)         # 처리 경로와 이유를 한 번에 받는다
    # 9. route_counts[route] 에 route_counts[route] + 1 을 담는다 (그 경로의 건수를 1 늘린다)
    route_counts[route] = route_counts[route] + 1  # 그 경로의 건수를 1 늘린다
```

**결과**

- (가) 출력은 다음과 같습니다. 경로별 건수는 <mark style="background:#bde3ff">**기본 3건 · 승인 필요 1건 · 오탐 종료 1건**</mark>이고, `종료` 상태가 된 알림은 <mark style="background:#bde3ff">**INC-004**</mark> 입니다.

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-003 gaeun mid -> 승인 필요 · VIP 계정이라 담당자 승인이 필요함 (상태: 탐지됨)
INC-004 jiwoo mid -> 오탐 종료 · 신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄 (상태: 종료)
INC-005 198.51.100.90 low -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
--- 단계 2: 경로별 건수
기본 3 건
승인 필요 1 건
오탐 종료 1 건
```

- (나) INC-004 의 `reasons` 는 `업무 시간 밖 로그인` · `평소와 다른 IP` 로 <mark style="background:#bde3ff">두 규칙 모두 IP 관련 규칙</mark>이라 `is_only_ip_related` 가 `True` 이고, 신뢰 IP 이므로 6번 조건이 참입니다.
  - INC-002 의 `reasons` 에는 IP 관련이 아닌 <mark style="background:#bde3ff">`대량 다운로드`</mark> 가 있어서 `is_only_ip_related` 가 `False` 입니다. 신뢰 IP 에서 접속했어도 `대량 다운로드` 는 IP 와 상관없는 행동입니다. 그래서 정상이라고 할 수 없고, 기본 경로로 보내 분석합니다.
- (다) 한 예: 그 VIP 계정은 <mark style="background:#bde3ff">`승인 필요`</mark> 경로로 갑니다.
  - 4번이 먼저라서 VIP 이면 6번까지 가지 않고 바로 리턴합니다.
  - 순서를 바꾸면 6번 조건이 먼저 검사됩니다. 이 VIP 알림은 「신뢰 IP 이고 규칙이 모두 IP 관련」이라서 `오탐 종료` 로 종료됩니다. 중요한 계정의 알림이 담당자 검토 없이 종료되는 결과이므로, <mark>위험이 더 큰 조건을 먼저 판정합니다.</mark>

**왜**

- <mark>맥락에 따라 경로를 분기하면 중요한 알림은 담당자 검토로 넘기고, 정상임이 분명한 알림은 자동으로 종료할 수 있습니다.</mark> 종료 사유를 함께 기록해야 나중에 「이 알림을 왜 분석하지 않았는가」라는 질문에 감사(audit) 근거로 답할 수 있습니다.

**자주 틀리는 곳**

- 1 ~ 3번을 빠뜨리면 `is_only_ip_related` 가 항상 `True` 를 리턴해서 오류는 나지 않지만 <mark>**INC-002 가 오탐으로 종료됩니다.**</mark> 6번에서 `and is_only_ip_related(incident)` 를 빼도 같은 결과가 나옵니다. 이 실수가 가장 위험합니다. 대량 다운로드가 탐지된 알림이 아무도 검토하지 않은 채 종료되기 때문입니다. 이처럼 실제 위협을 정상으로 판정해 놓치는 것을 미탐(false negative, 폴스 네거티브)이라고 합니다.

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 오탐 종료 · 신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄 (상태: 종료)
```

- 4 · 5번을 빠뜨리면 <mark>**VIP 인 `gaeun`(INC-003) 이 `기본` 경로로 갑니다.**</mark> 중요한 계정이 담당자 승인 없이 기본 절차대로 처리되는 것이 이 실수의 결과입니다.

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-003 gaeun mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
```

- 5번에서 값을 하나만 리턴하면 실행 파일의 `route, reason = decide_route(incident)` 에서 오류가 납니다. <mark>**리턴하는 값의 개수와 받는 변수의 개수가 같아야 합니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`too many values to unpack (expected 2)`</mark>). INC-003 에서 멈추는 것이 이 실수의 결과입니다.

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
ValueError: too many values to unpack (expected 2)
```

- 두 함수만 채우지 않고 실행하면 <mark>**오류 없이 5건이 모두 `기본` 으로 나옵니다.**</mark>

```
--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태
INC-001 dami high -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-002 seoyeon mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-003 gaeun mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-004 jiwoo mid -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
INC-005 198.51.100.90 low -> 기본 · 플레이북 기본 절차대로 처리함 (상태: 탐지됨)
--- 단계 2: 경로별 건수
기본 5 건
승인 필요 0 건
오탐 종료 0 건
```

- 실행 파일의 8번을 비워 두면 `route` 가 만들어지지 않아 오류가 납니다. <mark>**리턴된 두 값을 변수에 받아야 아래에서 쓸 수 있습니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`name 'route' is not defined`</mark>, `route` 라는 이름의 변수가 아직 만들어지지 않았다는 뜻입니다). 파이썬 버전에 따라 뒤에 `Did you mean: …`(혹시 이걸 말한 것인가요?라는 추천 문구)이 더 붙을 수 있습니다.

```
NameError: name 'route' is not defined
```

**관제에서는**

- 오탐으로 종료하는 규칙은 <mark>「모든 조건을 충족할 때만 종료한다」처럼 조건을 엄격하게 정의하는 것</mark>이 원칙입니다. 종료한 알림도 사유와 함께 목록으로 보관하고, 주기적으로 일부를 표본 추출(sampling, 샘플링: 전체에서 일부를 골라 검토하는 방식)해 잘못 종료한 건이 없는지 검토합니다. (이 수업 코드에는 없는 운영 절차입니다.)

---

## Exercise 2-3 정답

 **터미널에 입력합니다.**

```bash
pwd
python exercise2-3_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — `safe_runner.py` 의 1 ~ 7번입니다.

```python
    # 1. action 이 "계정 잠금" 이고(and) entity 가 state["locked_users"] 안에 있으면 (if, in)
    if action == "계정 잠금" and entity in state["locked_users"]:                  # 계정 잠금인데 이미 잠긴 계정이면
    # 2.   "건너뜀: 이미 잠겨 있음" 을 리턴한다
        return "건너뜀: 이미 잠겨 있음"                                            # 건너뛸 이유를 리턴한다
    # 3. action 이 "계정 잠금" 이고(and) state["locked_users"] 의 개수(len)가 MAX_LOCKS_PER_RUN 이상이면 (if, >=)
    if action == "계정 잠금" and len(state["locked_users"]) >= MAX_LOCKS_PER_RUN:  # 잠근 계정이 한도 이상이면
    # 4.   "건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)" 를 리턴한다
        return "건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)"    # 건너뛸 이유를 리턴한다
    # 5. skip_reason 이 빈 글자("")가 아니면 (if, !=)
    if skip_reason != "":                                                          # 건너뛸 이유가 있으면
    # 6.   skip_reason 을 리턴한다
        return skip_reason                                                         # 실행하지 않고 이유를 리턴한다
    # 7. run_action(action, incident, state) 의 결과를 리턴한다 (건너뛸 이유가 없으면 원래대로 실행한다)
    return run_action(action, incident, state)                                     # 이유가 없으면 Unit 1의 방식대로 실행한 결과를 리턴한다
```

`exercise2-3_run.py` 의 8 · 9번입니다.

```python
    # 8. result_text 가 "건너뜀" 으로 시작하면 (if, startswith)
    if result_text.startswith("건너뜀"):                              # 결과 문장이 「건너뜀」으로 시작하면
    # 9.   entry["incident"] · entry["action"] · "->" · result_text 를 출력한다 (print)
        print(entry["incident"], entry["action"], "->", result_text)  # 인시던트 · 액션 · 이유를 출력한다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 1 의 잠긴 계정은 <mark style="background:#bde3ff">**`['dami', 'dami']`, 티켓 2건**</mark>, 단계 3 은 <mark style="background:#bde3ff">**`['dami']`, 티켓 1건**</mark>, 단계 4 는 <mark style="background:#bde3ff">**3개(`dami` · `seoyeon` · `gaeun`), 티켓 7건**</mark> 입니다.

```
--- 단계 1: Unit 1 방식(안전장치 없음)으로 같은 알림 5건을 두 번 처리
잠긴 계정: ['dami', 'dami']
티켓: 2 건
--- 단계 2: Unit 1 방식(안전장치 없음)으로 인사 오류 알림 7건 처리
잠긴 계정 7 개: ['dami', 'dami', 'seoyeon', 'gaeun', 'jiwoo', 'junho', 'hana']
--- 단계 3: 안전한 방식으로 같은 알림 5건을 두 번 처리
첫 번째 처리
INC-001 dami -> 실행 완료 (상태: 조치됨)
INC-002 seoyeon -> 승인 대기 (상태: 분류됨)
INC-003 gaeun -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-004 jiwoo -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-005 198.51.100.90 -> 승인 대기 (상태: 분류됨)
두 번째 처리
INC-001 dami -> 이미 처리됨 (상태: 조치됨)
INC-002 seoyeon -> 승인 대기 (상태: 분류됨)
INC-003 gaeun -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-004 jiwoo -> 맞는 플레이북 없음 (상태: 탐지됨)
INC-005 198.51.100.90 -> 승인 대기 (상태: 분류됨)
잠긴 계정: ['dami']
티켓: 1 건
--- 단계 4: 안전한 방식으로 인사 오류 알림 7건 처리 (한 번에 최대 3 개)
INC-B01 dami -> 실행 완료 (상태: 조치됨)
INC-B02 dami -> 일부 건너뜀 (상태: 분류됨)
INC-B03 seoyeon -> 실행 완료 (상태: 조치됨)
INC-B04 gaeun -> 실행 완료 (상태: 조치됨)
INC-B05 jiwoo -> 일부 건너뜀 (상태: 분류됨)
INC-B06 junho -> 일부 건너뜀 (상태: 분류됨)
INC-B07 hana -> 일부 건너뜀 (상태: 분류됨)
잠긴 계정 3 개: ['dami', 'seoyeon', 'gaeun']
결과별 건수: {'실행 완료': 3, '일부 건너뜀': 4}
티켓: 7 건
건너뛴 액션과 이유:
INC-B02 계정 잠금 -> 건너뜀: 이미 잠겨 있음
INC-B05 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B06 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B07 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
```

- (나) 단계 3 의 「두 번째 처리」에서 INC-001 이 <mark style="background:#bde3ff">`이미 처리됨 (상태: 조치됨)`</mark> 으로 나옵니다.
  - 장치: 중복 실행 방지(idempotency)입니다. `run_playbook_safe` 의 첫 `if` 가 인시던트 상태를 점검해서, `조치됨` · `보고됨` · `종료` 이면 실행하지 않고 건너뜁니다. 첫 번째 처리에서 INC-001 이 `조치됨` 이 되었기 때문입니다.
  - Unit 1 방식에는 이 확인이 없어서 두 번째 처리에서 `dami` 를 다시 잠그고 티켓을 또 만들었습니다.
- (다) 잠긴 3개 가운데 <mark style="background:#bde3ff">`seoyeon` 과 `gaeun` 은 `employed` 가 `true` 인 재직자라 잘못 잠긴 계정</mark>입니다. 실제 퇴사자는 `dami` 한 명입니다.
  - 한도가 없고 중복 방지만 있다면 서로 다른 계정 6개가 모두 잠깁니다. 이 가운데 실제 퇴사자는 `dami` 한 명이라 5명이 잘못 잠깁니다(`dami` 는 알림이 두 건이라도 한 번만 잠깁니다). 한도 3개로 잘못 잠긴 계정이 5명에서 2명으로 줄었습니다.
  - 한도가 방지하지 못하는 문제: 한도 안에서는 잘못된 알림도 그대로 실행됩니다. 한도는 영향 범위(잠기는 계정 수)를 제한할 뿐, 잘못된 알림을 식별하지는 못합니다.
  - 줄이는 방법: Exercise 2-1에서 보강한 `employed` 맥락을 잠금 실행 전에 점검하면 `seoyeon` 과 `gaeun` 은 재직 중이라 잠금 대상에서 제외됩니다. `gaeun` 은 VIP 계정이라 Exercise 2-2의 `승인 필요` 경로에서도 자동 잠금 대상에서 제외됩니다. Unit 3의 Exercise 3-2 하루 흐름은 이 가운데 VIP 경로와 신뢰 IP 오탐 판단을 하나의 흐름으로 연결합니다(재직 여부 점검은 연결하지 않습니다).
  - 계정 잠금을 건너뛴 알림에도 티켓은 만들어집니다(티켓 7건). 건너뛰는 것이 알림 전체가 아니라 계정 잠금 액션 하나뿐이기 때문이며, 담당자가 티켓을 보고 이어서 확인합니다.

**왜**

- <mark>자동 대응의 더 큰 위험은 한 번의 오판이 아니라, 잘못된 판단이 짧은 시간에 대량으로 반복 실행되는 것입니다. 예를 들어 잘못된 알림 100건이 유입되면 계정 100개가 몇 초 만에 잠길 수 있습니다.</mark> 중복 실행 방지(같은 조치를 두 번 실행하지 않게 하는 장치)와 영향 범위 제한(피해가 미치는 범위를 제한하는 장치)을 두면, 잘못된 알림이 유입되어도 피해가 확대되지 않습니다.

**자주 틀리는 곳**

- 1 · 2번을 빠뜨리면 오류는 나지 않지만 <mark>**같은 계정의 두 번째 알림(INC-B02)이 `dami` 를 다시 잠급니다.**</mark> 잠긴 계정 리스트에 `dami` 가 두 번 들어가서 한도 3개 가운데 2개를 쓰기 때문에, `gaeun` 은 잠기지 않습니다. 단계 4 의 `잠긴 계정` 줄이 이 실수의 결과입니다.

```
INC-B04 gaeun -> 일부 건너뜀 (상태: 분류됨)
INC-B05 jiwoo -> 일부 건너뜀 (상태: 분류됨)
INC-B06 junho -> 일부 건너뜀 (상태: 분류됨)
INC-B07 hana -> 일부 건너뜀 (상태: 분류됨)
잠긴 계정 3 개: ['dami', 'dami', 'seoyeon']
결과별 건수: {'실행 완료': 3, '일부 건너뜀': 4}
티켓: 7 건
건너뛴 액션과 이유:
INC-B04 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B05 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B06 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B07 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
```

- 3 · 4번을 빠뜨리면 <mark>**한도가 없어져 재직자까지 모두 잠깁니다.**</mark> 단계 4 의 잠긴 계정이 6개로 나오는 것이 이 실수의 결과입니다.

```
INC-B01 dami -> 실행 완료 (상태: 조치됨)
INC-B02 dami -> 일부 건너뜀 (상태: 분류됨)
INC-B03 seoyeon -> 실행 완료 (상태: 조치됨)
INC-B04 gaeun -> 실행 완료 (상태: 조치됨)
INC-B05 jiwoo -> 실행 완료 (상태: 조치됨)
INC-B06 junho -> 실행 완료 (상태: 조치됨)
INC-B07 hana -> 실행 완료 (상태: 조치됨)
잠긴 계정 6 개: ['dami', 'seoyeon', 'gaeun', 'jiwoo', 'junho', 'hana']
결과별 건수: {'실행 완료': 6, '일부 건너뜀': 1}
티켓: 7 건
건너뛴 액션과 이유:
INC-B02 계정 잠금 -> 건너뜀: 이미 잠겨 있음
```

- 3번에서 `>=` 대신 `>` 를 쓰면 <mark>**한도 3개가 아니라 4개까지 잠깁니다.**</mark> 이처럼 경계값을 하나 잘못 포함하거나 빠뜨리는 오류를 경계 조건 오류(off-by-one error, 오프 바이 원 에러)라고 합니다. 「3개 이상이면 건너뛴다」와 「3개를 초과하면 건너뛴다」는 다릅니다.

```
INC-B03 seoyeon -> 실행 완료 (상태: 조치됨)
INC-B04 gaeun -> 실행 완료 (상태: 조치됨)
INC-B05 jiwoo -> 실행 완료 (상태: 조치됨)
INC-B06 junho -> 일부 건너뜀 (상태: 분류됨)
INC-B07 hana -> 일부 건너뜀 (상태: 분류됨)
잠긴 계정 4 개: ['dami', 'seoyeon', 'gaeun', 'jiwoo']
결과별 건수: {'실행 완료': 4, '일부 건너뜀': 3}
티켓: 7 건
건너뛴 액션과 이유:
INC-B02 계정 잠금 -> 건너뜀: 이미 잠겨 있음
INC-B06 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
INC-B07 계정 잠금 -> 건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)
```

- 5 · 6번을 빠뜨리면 <mark>**건너뛸 사유를 판정해 놓고도 적용하지 않아 한도와 중복 방지가 모두 무시됩니다.**</mark> 단계 4 의 잠긴 계정이 7개로 나오고 `dami` 가 두 번 들어 있는 것이 이 실수의 결과입니다.

```
--- 단계 4: 안전한 방식으로 인사 오류 알림 7건 처리 (한 번에 최대 3 개)
INC-B01 dami -> 실행 완료 (상태: 조치됨)
INC-B02 dami -> 실행 완료 (상태: 조치됨)
INC-B03 seoyeon -> 실행 완료 (상태: 조치됨)
INC-B04 gaeun -> 실행 완료 (상태: 조치됨)
INC-B05 jiwoo -> 실행 완료 (상태: 조치됨)
INC-B06 junho -> 실행 완료 (상태: 조치됨)
INC-B07 hana -> 실행 완료 (상태: 조치됨)
잠긴 계정 7 개: ['dami', 'dami', 'seoyeon', 'gaeun', 'jiwoo', 'junho', 'hana']
결과별 건수: {'실행 완료': 7}
티켓: 7 건
건너뛴 액션과 이유:
```

- 7번을 빠뜨리면 `safe_run_action` 이 값을 리턴하지 않아 오류가 납니다. <mark>**건너뛸 이유가 없을 때 실행하는 줄이 있어야 합니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`'NoneType' object has no attribute 'startswith'`</mark>, 값이 없다는 뜻의 `None` 에 `startswith` 를 쓰려 해서 난 오류).

```
AttributeError: 'NoneType' object has no attribute 'startswith'
```

**관제에서는**

- 자동 대응을 활성화할 때는 <mark>「1회에 최대 몇 건까지 자동 실행하고, 초과하면 담당자에게 이관한다」</mark>를 먼저 정합니다. 한도에 도달한 건이 나왔다면 잘못된 알림이 대량 유입되는 사고가 발생했다는 신호일 수 있으므로, 담당자에게 별도로 통보하는 에스컬레이션(escalation, 에스컬레이션: 상위 담당자나 다른 팀에 판단을 넘기는 일)을 하기도 합니다. 이 통보 기능은 이번 수업 코드에는 없고, 실제 운영에서 쓰는 절차입니다. 같은 알림이 여러 번 들어와도 결과가 같게 설계하는 것(멱등성)이 기본입니다.
