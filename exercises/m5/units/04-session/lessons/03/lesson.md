---
id: m5-u04-l03
title: Exercise 4-2 · 허용 IP 제외와 차단 자동 해제 만들기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/122_day03_am_containment.md
  mission_id: GichanSource.m5-1111-am-containment
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 4-2 · 허용 IP 제외와 차단 자동 해제 만들기

## 이번에 만들 것: 예외 IP와 차단 만료

> **오늘 들어온 일**
>
> - **상황**: 오늘 아침 경로 스캔(path scan, 패스 스캔: 서버의 여러 주소에 차례로 요청을 보내 취약점을 찾는 시도) 탐지 알림이 세 건 들어왔습니다. 하나는 외부 IP `198.51.100.90`, 하나는 자사 취약점 점검 서버(취약점 스캐너) `192.0.2.10`, 하나는 `junho` 와 `hana` 가 공유하는 사무실 IP `192.0.2.41` 입니다. IP 차단(IP block)은 해당 IP 에서 들어오는 접속을 모두 거부하는 조치입니다.
> - **문제**:
> - 세 건을 모두 자동 차단하면 점검 서버가 차단되어 점검이 중단되고, 공유 IP 를 차단하면 `junho` 와 `hana` 두 사람이 접속하지 못합니다(부수적 피해).
> - 한 번 차단하면 사람이 해제하기 전까지 유지되어, 오래된 차단이 누적되면 어떤 차단이 아직 필요한지 판단할 수 없게 됩니다.
> - **부탁**: 허용 목록(allowlist)에 있는 IP 는 차단하지 말고, 여러 계정이 공유하는 IP 는 담당자 승인을 거치게 해 주세요. 차단한 IP 는 정해진 유효 기간(TTL, 2시간)이 지나면 자동 해제해 주세요.
> - **바뀌는 점**: 세 건 중 외부 공격 IP 한 건만 차단되고, 그 차단도 2시간 뒤 자동으로 해제됩니다(오늘은 차단 함수를 직접 호출하는 수업이라, Unit 1 플레이북의 승인 값 확인은 거치지 않습니다). 점검 서버와 정상 사용자는 차단되지 않습니다. 상황과 IP 는 설명을 위한 예시입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 읽기 · 2.1 차단 전에 영향 범위를 확인하고, 차단에는 만료 시각을 정한다

차단 전에 적용하는 정책 검사(policy check) 규칙은 두 가지입니다. 영향 범위(blast radius, 블라스트 레이디어스: 한 조치가 잘못됐을 때 영향을 받는 대상의 범위)에는 정상 사용자와 필요한 서버가 포함되므로, 두 규칙은 그 범위를 먼저 확인하는 장치입니다.

| 검사 | 조건 | 결과 |
|---|---|---|
| 허용 목록 | `allowlist_ips.json` 에 있다 | 차단하지 않고 이유를 기록한다 |
| 공유 IP | 여러 사용자가 공유하는 IP 다 (그 IP 를 쓰는 계정이 `SHARED_IP_LIMIT`(2) 개 이상) | 차단하지 않고 담당자 승인이 필요하다고 기록한다 |

- 둘 다 해당하지 않으면 차단하고 **만료 시각**(expiry time, 익스파이어리 타임: 차단이 끝나는 시각)을 함께 기록합니다.
- 만료 시각은 연습용 시스템의 현재 시각(`clock`, 분)에 차단 유효 기간(`ttl`, 티티엘: Time To Live, 설정한 조치가 유효한 기간)을 더한 값입니다. 예를 들어 현재 0분이고 `ttl` 이 120분이면 만료 시각은 120분입니다. 오늘은 `ttl` 이 120분입니다.
- 차단은 일정 기간 뒤 자동 해제되는 임시 조치로 두고, 영구 차단은 사람이 사유를 확인한 뒤 결정합니다. NIST SP 800-61 Rev. 2 는 봉쇄 전략을 고르는 기준으로 두 가지를 듭니다. 하나는 서비스 가용성(service availability: 서비스를 계속 쓸 수 있는 정도)입니다. 다른 하나는 조치의 지속 기간(duration of the solution)입니다. 지속 기간의 예로는 4시간 뒤 제거하는 긴급 임시 조치, 2주 뒤 제거하는 임시 조치, 영구 조치가 있습니다.

함수는 한 파일에 있고, 직접 쓰는 곳은 **아홉 군데**입니다.

```
ip_actions.py     is_in_allowlist    : 허용 목록에 있는지 확인한다 (1번)
                  count_users_on_ip  : 그 IP 를 쓰는 계정 수를 센다 (2번)
                  check_ip_policy    : 허용 목록 IP · 함께 쓰는 IP 이면 차단을 막는 이유를 리턴한다 (미리 채움)
                  block_ip           : 차단하고 (3번) 끝나는 시각을 적는다 (4번)
                  expire_blocks      : 끝나는 시각이 지난 차단을 찾아 (5번) 풀고 기록한다 (6번)
실행 파일         exercise4-2_run.py   : 막을 이유를 구하고 (7번), 이유가 없으면 (8번) 차단한다 (9번)
```

> **여기부터 문제입니다.**

## Exercise 4-2 · 허용 IP 제외와 차단 자동 해제 만들기

**이런 상황이 있습니다**

- **지금은**: <mark>경로 스캔 알림 세 건을 모두 차단하면 점검 서버와 정상 사용자가 차단되고, 차단이 해제되지 않고 계속 유지됩니다</mark>.
- **만드는 것**: 허용 목록 조회 · 사용 계정 수 집계 · 차단 · 만료된 차단 해제(`ip_actions.py`), 정책 검사와 차단 호출(`exercise4-2_run.py`).
- **실행하면**: <mark>단계 1: 요청 3건의 처리 결과, 단계 2: 차단 뒤 상태, 단계 3: 120분 뒤 자동 해제, 단계 4: 저장한 파일에서 읽은 값이 나옵니다.</mark>

**할 일**: 파일 두 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 1 ~ 3 을 읽습니다.

**`ip_actions.py`** — IP 차단과 만료된 차단의 자동 해제를 구현합니다. Unit 5에서도 이 파일의 함수를 불러와 사용합니다. 직접 쓰는 곳은 1 ~ 6번입니다.

```python
from containment_store import make_record                                              # 기록 한 건을 만드는 함수를 불러온다

SHARED_IP_LIMIT = 2                                                                    # 한 IP 를 쓰는 계정이 이 수 이상이면 공유 IP 로 본다
DEFAULT_TTL = 120                                                                      # 차단을 유지하는 시간(분)


def is_in_allowlist(ip, allowlist_ips):                                                # IP 와 허용 목록을 받는 함수
    """IP 가 허용 목록에 있으면 True, 없으면 False 를 리턴한다.
    협력사 사무실처럼 차단하면 안 되는 IP 를 찾아낼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. ip 가 allowlist_ips 안에 있는지(in)의 결과를 리턴한다


def count_users_on_ip(ip, ip_users):                                                   # IP 와 IP 별 사용 계정 딕셔너리를 받는 함수
    """그 IP 를 쓰는 계정이 몇 개인지 리턴한다. ip_users.json 에 없는 IP 는 0 을 리턴한다.
    차단하면 정상 사용자가 몇 명 영향을 받는지 확인할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. ip_users.get(ip, []) 의 개수(len)를 리턴한다 (목록에 없으면 빈 리스트로 본다)


def check_ip_policy(ip, allowlist_ips, ip_users):                                      # IP · 허용 목록 · 사용 계정 딕셔너리를 받는 함수
    """자동으로 차단하면 안 되는 IP 이면 그 이유 문장을, 아니면 빈 글자("")를 리턴한다.
    허용 목록 IP 이거나 여러 계정이 함께 쓰는 IP 를 차단하기 전에 가려낼 때 쓴다.
    """
    if is_in_allowlist(ip, allowlist_ips):                                             # 허용 목록 IP 이면 — 미리 채운 줄
        return "허용 목록 IP 라서 차단하지 않음"                                       # 이유를 리턴한다 — 미리 채운 줄
    if count_users_on_ip(ip, ip_users) >= SHARED_IP_LIMIT:                             # 여러 계정이 함께 쓰는 IP 이면 — 미리 채운 줄
        return "여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요"                        # 이유를 리턴한다 — 미리 채운 줄
    return ""                                                                          # 막을 이유가 없으면 빈 글자를 리턴한다 — 미리 채운 줄


def block_ip(ip, state, incident_id, reason, ttl):                                     # IP · 상태 · 인시던트 번호 · 이유 · 유지 시간을 받는 함수
    """IP 를 차단하고 끝나는 시각을 적은 뒤, 실제로 차단됐는지 확인해 기록 한 건을 리턴한다.
    영구 차단 대신, 시간이 지나면 자동으로 풀리는 임시 차단을 만들 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 3. state["blocked_ips"] 에 ip 를 추가한다 (append)
    # 4. state["block_expiry"][ip] 에 state["clock"] + ttl 을 저장한다 (끝나는 시각)
    after = "차단됨"                                                                   # 조치 뒤 상태 : 일단 차단됐다고 적고 — 미리 채운 줄
    if ip not in state["blocked_ips"]:                                                 # 실제로 확인해 차단되지 않았으면 — 미리 채운 줄
        after = "차단되지 않음 (확인 실패)"                                            # 확인 실패라고 고쳐 적는다 — 미리 채운 줄
    return make_record("IP 차단", ip, incident_id, "차단되지 않음", after, reason + " (" + str(ttl) + "분 뒤 자동 해제)")  # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄


def unblock_ip(ip, state, incident_id, reason):                                        # IP · 상태 · 인시던트 번호 · 이유를 받는 함수
    """차단한 IP 를 풀고 끝나는 시각 기록도 지운 뒤 기록 한 건을 리턴한다.
    시간이 끝나서 풀거나 오탐으로 풀 때 쓴다.
    """
    state["blocked_ips"].remove(ip)                                                    # 차단 리스트에서 제거한다 — 미리 채운 줄
    state["block_expiry"].pop(ip)                                                      # 끝나는 시각 기록도 지운다 — 미리 채운 줄
    return make_record("IP 해제", ip, incident_id, "차단됨", "차단되지 않음", reason)  # 조치 전 · 후 상태와 함께 기록한다 — 미리 채운 줄


def expire_blocks(state, incident_id):                                                 # 상태와 인시던트 번호를 받는 함수
    """끝나는 시각이 지난 차단을 모두 풀고 해제 기록 리스트를 리턴한다.
    임시 차단이 사람 손 없이 풀리게 할 때 쓴다.
    """
    records = []                                                                       # 해제 기록을 저장할 빈 리스트
    for ip in list(state["blocked_ips"]):                                              # 차단 리스트의 복사본에서 IP 를 하나씩 꺼낸다 (원본을 바꾸며 돌면 안 되기 때문이다)
        end_time = state["block_expiry"][ip]                                           # 그 IP 의 차단이 끝나는 시각 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. end_time 이 state["clock"] 이하이면 (if, <=)
        # 6.   unblock_ip(ip, state, incident_id, "차단 시간이 끝나 자동 해제") 의 결과를 records 에 추가한다 (append)
    return records                                                                     # 해제 기록 리스트를 리턴한다
```

**`exercise4-2_run.py`** — 7 ~ 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 7번 아래에는 막을 이유를 저장하는 `refusal = …`(`refusal` 은 영어로 「거절」이고, 막을 이유가 있으면 그 문장이 저장됩니다)을, 8번 아래에는 `if … :` 를, 9번 아래에는 한 단계 들여쓴 `record = …` 를 씁니다. 그 사이의 미리 채운 줄은 그대로 둡니다. Exercise 4-1의 `containment_store.py` 가 같은 폴더에 있어야 합니다.

```python
from incident import load_json                                                           # Unit 1 파일의 함수를 불러온다
from containment_store import new_state, save_state, load_state, reset_log, append_log, make_record  # 상태 · 기록 함수를 불러온다
from ip_actions import check_ip_policy, block_ip, expire_blocks, DEFAULT_TTL             # 방금 만든 IP 조치 함수를 불러온다

allowlist_ips = load_json("config/allowlist_ips.json")                                   # 허용 목록을 읽는다
ip_users = load_json("ip_users.json")                                                    # IP 별 사용 계정을 읽는다
requests = [("INC-005", "198.51.100.90", "경로 스캔"), ("INC-009", "192.0.2.10", "경로 스캔"), ("INC-008", "192.0.2.41", "경로 스캔")]  # 차단 요청 3건 : (인시던트 번호, IP, 이유)
state = new_state()                                                                      # 처음 상태에서 시작한다
reset_log()                                                                              # 기록 파일을 비운다

print("--- 단계 1: 차단 요청 3건")                                                       # 단계 1 시작을 알리는 줄
for incident_id, ip, reason in requests:                                                 # 요청을 하나씩 꺼낸다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. check_ip_policy(ip, allowlist_ips, ip_users) 의 결과를 refusal 에 저장한다
    record = make_record("IP 차단", ip, incident_id, "변경 없음", "변경 없음", refusal)  # 먼저 「바꾸지 않음」 기록을 만들어 두고 — 미리 채운 줄
    # 8. refusal 이 빈 글자("")이면 (if, ==)
    # 9.   block_ip(ip, state, incident_id, reason, DEFAULT_TTL) 의 결과를 record 에 저장한다 (실제로 차단한 기록으로 바꾼다)
    append_log(record)                                                                   # 조치 기록을 파일에 남긴다
    print(record["incident"], record["target"], "·", record["before"], "→", record["after"], "·", record["reason"])  # 기록 한 건을 출력한다

print("--- 단계 2: 차단 뒤 차단한 IP 와 끝나는 시각")                                    # 단계 2 시작을 알리는 줄
print("차단한 IP:", state["blocked_ips"])                                                # 차단한 IP 를 출력한다
print("차단이 끝나는 시각(분):", state["block_expiry"])                                  # 끝나는 시각을 출력한다

print("--- 단계 3: 시계를 120분 뒤로 옮기고 시간이 끝난 차단 풀기")                      # 단계 3 시작을 알리는 줄
state["clock"] = state["clock"] + 120                                                    # 연습용 시스템의 시계를 120분 뒤로 옮긴다
for record in expire_blocks(state, "INC-005"):                                           # 끝난 차단의 해제 기록을 하나씩 꺼낸다
    append_log(record)                                                                   # 해제 기록도 남긴다
    print(record["incident"], record["target"], "·", record["before"], "→", record["after"], "·", record["reason"])  # 기록 한 건을 출력한다
print("차단한 IP:", state["blocked_ips"])                                                # 해제 뒤 차단한 IP 를 출력한다

save_state(state)                                                                        # 상태를 파일에 저장한다
print("--- 단계 4: 파일에 저장된 값 다시 읽기")                                          # 단계 4 시작을 알리는 줄
print("차단한 IP:", load_state()["blocked_ips"])                                         # 저장된 차단 IP 를 출력한다
print("조치 기록:", len(load_json("containment_log.json")), "건")                        # 저장된 기록 수를 출력한다
```

**순서**

1. **[터미널]** 파일 두 개를 만들고 붙여 넣습니다.
   ```bash
   pwd
   touch ip_actions.py exercise4-2_run.py
   ls
   ```
2. **[VS Code]** `ip_actions.py` 1 ~ 6번, `exercise4-2_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「Exercise 4-2 한눈에」를 봅니다.
3. **[터미널]** 실행합니다(맥북은 `python3`).
   ```bash
   python exercise4-2_run.py
   ```
4. 출력은 네 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 3줄, 단계 2 는 2줄, 단계 3 은 2줄, 단계 4 는 2줄입니다.
5. **[보고서]** Unit 4 의 `## Exercise 4-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣어 주세요. 그리고 단계 1 에서 실제로 차단된 IP 와, 차단하지 않은 IP 와 그 이유를 적어 주세요.
   - (나) [핵심 질문] INC-008 의 `192.0.2.41` 은 차단되지 않았습니다. `ip_users.json` 의 값을 근거로 차단하지 않은 이유를 적고, 그대로 차단했다면 영향을 받았을 사용자와 그 영향을 적어 주세요.
   - (다) [핵심 질문] 단계 2 의 만료 시각(120)과 단계 3 의 시계(120)를 근거로 `198.51.100.90` 이 자동 해제된 이유를 적어 주세요. 그리고 유효 기간이 있는 임시 차단이 영구 차단보다 나은 점도 적어 주세요.

## Exercise 4-2 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 리스트 안에 있는지 확인한 결과 리턴 | `return ip in allowlist_ips` |
| 키가 없어도 기본값을 주며 꺼내기 | `ip_users.get(ip, [])` |
| 리스트의 개수 | `len(ip_users.get(ip, []))` |
| 딕셔너리에 값 저장하기 | `state["block_expiry"][ip] = state["clock"] + ttl` |
| 이하이면 | `if end_time <= state["clock"]:` |
| 빈 문자열과 같으면 | `if refusal == "":` |

---
