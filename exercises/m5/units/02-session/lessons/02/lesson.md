---
id: m5-u02-l02
title: 실습 2-1 · 알림에 맥락 정보 보강하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/118_day02_am_context_route_safety.md
  mission_id: GichanSource.m5-1110-am-context-route-safety
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 2-1 · 알림에 맥락 정보 보강하기

## 이번 의뢰: 맥락 없는 자동 조치

> **오늘 들어온 일**
>
> - **상황**: Unit 1에서 만든 프로그램은 알림에 맞는 플레이북이 있으면 계정 잠금(account lockout, 어카운트 락아웃: 계정의 로그인을 비활성화하는 조치) 같은 조치를 즉시 실행했습니다. 오늘 샘플 알림 5건 가운데 세 건은 상황이 서로 다릅니다.
> - `INC-001`(알림 한 건에 부여한 식별 번호): 퇴사자 `dami` 의 계정입니다. 잠가도 업무에 지장이 없습니다.
> - `INC-003`: `gaeun` 은 직원 계정을 관리하는 계정 관리자입니다. 이 계정이 잠기면 계정 관리 업무가 중단됩니다. 이처럼 잠겼을 때 업무에 미치는 영향이 큰 고중요도 계정을 **VIP 계정**(VIP account)이라고 합니다.
> - `INC-004`: `jiwoo` 는 협력사 사무실에서 평소와 같이 접속했을 뿐이므로 잠글 사유가 없습니다.
> - **문제**: 프로그램은 알림에 적힌 탐지 규칙 이름과 위험 등급만 참조합니다. 퇴사 여부, VIP 계정 여부, 접속 IP 의 신뢰 여부를 알지 못한 채 모든 알림에 같은 절차를 실행합니다. Unit 1 샘플에서는 `INC-003` · `INC-004` 가 맞는 플레이북이 없어 조치가 실행되지 않았지만, 맞는 플레이북이 생기면 상황과 무관하게 같은 절차로 처리됩니다.
> - **부탁**: 조치를 실행하기 전에 「대상이 누구이고 어디에서 접속했는가」를 알림마다 조회해 알림에 추가해 주세요.
> - **바뀌는 점**: 「즉시 자동으로 잠글지, 담당자 승인을 받을지」를 정할 때 계정 이름이 아니라 알림에 추가된 정보(맥락)를 근거로 삼습니다. 상황과 이름은 설명을 위한 예시입니다.
> - **용어**: **인시던트**(incident, 인시던트)는 조사와 대응이 필요한 보안 사건 한 건입니다. 이 문서에서는 알림 한 건을 인시던트 한 건으로 취급합니다. `INC-001` 의 `INC` 는 incident 의 앞 세 글자입니다.

> **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 1.1 보강(enrichment) — 조치 실행 전에 알림에 맥락 정보를 추가한다

알림 한 건에 `context`(맥락)라는 딕셔너리를 추가합니다. 이 일을 **보강**(enrichment, 인리치먼트: 판단에 필요한 정보를 알림에 추가로 붙이는 일)이라고 합니다. SOAR 플레이북에서는 조치를 실행하기 전에 보강 단계를 두어, 대상의 재직 상태나 접속 출처 같은 맥락을 먼저 확인합니다.

알림이 가리키는 사용자 이름 또는 IP 를 알림 대상(entity, 엔티티)이라고 하며, 코드에서는 `entity` 라고 씁니다. `context` 에는 알림 대상에 대한 정보 다섯 가지가 키로 들어 있습니다. 아래 표의 예는 VIP 계정인 `gaeun` 의 경우입니다.

| 키(이름표) | 알려 주는 것 | `gaeun` 의 값 | 정보를 못 찾으면 |
|---|---|---|---|
| `account_known` | 계정 정보 파일에 등록된 대상인가 | `True`(있다) | `False`(IP 주소처럼 계정이 아닌 대상) |
| `employed` | 지금 재직 중인가 | `True`(재직) | `False` |
| `vip` | VIP 계정인가 | `True`(VIP 다) | `False` |
| `source_ip` | 로그인한 접속 IP | `198.51.100.77` | `None`(값이 없다) |
| `ip_trusted` | 그 IP 가 신뢰 IP 목록에 있는가 | `False`(목록에 없다) | `False` |

- **값의 출처 파일**: `account_known` · `employed` · `vip` 는 `users_info.json`, `source_ip` 는 `source_ips.json` 에서 조회합니다. `ip_trusted` 는 `source_ips.json` 에서 조회한 접속 IP 가 `trusted_ips.json` 목록에 포함되면 `True`, 포함되지 않으면 `False` 입니다.
- **`True` · `False` · `None`**: `True` 는 「참」(그렇다), `False` 는 「거짓」(아니다), `None` 은 「값 없음」입니다.
- **정보를 찾지 못했을 때**: 「확인되지 않음」을 뜻하는 초기값(`False` 또는 `None`)을 그대로 둡니다. 확인되지 않은 대상을 재직 중인 정상 사용자로 간주하면 안 되기 때문입니다.
- **주의할 점**: 계정 정보에 없는 대상의 `employed` · `vip` 가 `False` 여도 「퇴사했다」나 「VIP 가 아니다」라는 판정이 아니라, 「계정 정보에 없어 확인할 수 없다」는 뜻입니다.

함수 세 개가 각각 다른 일을 하고, 직접 쓰는 곳은 **아홉 군데**입니다.

```
enrichment.py   lookup_account   : 대상이 users_info 안에 있으면 재직 · VIP 를 담는다 (1 ~ 3번)
                lookup_source_ip : 대상이 source_ips 안에 있으면 접속 IP 와 신뢰 IP 여부를 담는다 (4 ~ 6번)
                enrich_incident  : 두 결과를 합쳐 incident["context"] 에 붙인다 (미리 채움)
실행 파일       exercise2-1_run.py : 알림마다 맥락을 붙이는 함수를 호출하고 (7번), VIP 이면 (8번) VIP 알림 수를 1 늘린다 (9번)
```

> **여기부터 문제입니다.**

## 실습 2-1 · 알림 5건 보강하고 VIP 알림 수 세기

**이런 상황이 있습니다**

- **지금은**: <mark>알림 5건에는 대상 이름과 위험 등급만 있어서 퇴사자 · VIP 계정 · 신뢰 IP 에서 온 접속을 구별할 수 없습니다</mark>.
- **만드는 것**: 계정 정보 조회와 접속 IP 정보 조회(`enrichment.py`), 보강 함수 호출과 VIP 계정 알림 수 집계(`exercise2-1_run.py`).
- **실행하면**: <mark>단계 1: 불러온 개수, 단계 2: 알림마다 붙인 정보, 단계 3: VIP 계정 알림 수가 나옵니다.</mark>

**할 일**: 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 · 3 을 읽습니다.

**`enrichment.py`** — 알림에 맥락을 추가하는 보강 함수를 정의합니다. 실습 2-2 실행 파일도 `enrich_incident` 를 가져와 사용(import)합니다. 직접 쓰는 곳은 1 ~ 6번입니다.

```python
def lookup_account(entity, users_info):                              # 대상 이름과 계정 정보 딕셔너리를 받는 함수
    """계정 정보 파일에서 이 대상이 재직 중인지, VIP 계정인지 찾아 딕셔너리로 리턴한다.
    파일에 이름이 없는 대상(IP 등)은 처음 값(False)을 그대로 리턴한다.
    """
    account = {"employed": False, "vip": False}                      # 처음에는 모르는 상태로 시작한다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. entity 가 users_info 안에 있으면 (if, in)
    # 2.   account 의 "employed" 에 users_info[entity]["employed"] 를 담는다
    # 3.   account 의 "vip" 에 users_info[entity]["vip"] 를 담는다
    return account                                                   # 계정 정보를 리턴한다


def lookup_source_ip(entity, source_ips, trusted_ips):               # 대상 이름 · 접속 IP 딕셔너리 · 신뢰 IP 리스트를 받는 함수
    """이 대상이 접속한 IP 와, 그 IP 가 신뢰 IP 목록에 있는지 찾아 딕셔너리로 리턴한다.
    접속 IP 를 모르는 대상은 처음 값(None 과 False)을 그대로 리턴한다.
    """
    ip_info = {"source_ip": None, "ip_trusted": False}               # 처음에는 모르는 상태로 시작한다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. entity 가 source_ips 안에 있으면 (if, in)
    # 5.   ip_info 의 "source_ip" 에 source_ips[entity] 를 담는다
    # 6.   ip_info 의 "ip_trusted" 에 source_ips[entity] 가 trusted_ips 안에 있는지(in)의 결과를 담는다
    return ip_info                                                   # 접속 IP 정보를 리턴한다


def enrich_incident(incident, users_info, source_ips, trusted_ips):  # 인시던트 · 계정 정보 · 접속 IP 딕셔너리 · 신뢰 IP 리스트를 받는 함수
    """위 두 함수가 찾은 정보를 모아 알림에 context 라는 이름으로 붙이고, 붙인 알림을 리턴한다.
    붙이고 나면 알림만 봐도 퇴사 · VIP · 접속 IP 를 알 수 있어서, 조치하기 전에 확인할 때 쓴다.
    """
    entity = incident["entity"]                                      # 대응할 대상(사용자 이름 또는 IP)
    account = lookup_account(entity, users_info)                     # 계정 정보를 찾는다
    ip_info = lookup_source_ip(entity, source_ips, trusted_ips)      # 접속 IP 정보를 찾는다
    account_known = entity in users_info                             # 계정 정보에 있는 대상인지 구한다
    context = {"account_known": account_known, "employed": account["employed"], "vip": account["vip"], "source_ip": ip_info["source_ip"], "ip_trusted": ip_info["ip_trusted"]}  # 다섯 가지 맥락을 합친다
    incident["context"] = context                                    # 인시던트에 맥락을 붙인다
    return incident                                                  # 맥락이 붙은 인시던트를 리턴한다
```

**`exercise2-1_run.py`** — 7 ~ 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 파일을 저장하지는 않습니다.

```python
from incident import load_json, INCIDENTS_PATH                 # Unit 1 파일의 함수를 불러온다
from enrichment import enrich_incident                         # 방금 만든 함수를 불러온다

incidents = load_json(INCIDENTS_PATH)                          # 인시던트 파일을 리스트로 읽는다
users_info = load_json("users_info.json")                      # 계정 정보 파일을 딕셔너리로 읽는다
source_ips = load_json("source_ips.json")                      # 알림이 난 접속의 IP 파일을 딕셔너리로 읽는다
trusted_ips = load_json("trusted_ips.json")                    # 신뢰 IP 파일을 리스트로 읽는다
incident_count = len(incidents)                                # 인시던트가 몇 건인지 센다
user_count = len(users_info)                                   # 계정 정보가 몇 명인지 센다
trusted_count = len(trusted_ips)                               # 신뢰 IP 가 몇 개인지 센다
print("--- 단계 1: 불러온 알림", incident_count, "건 · 계정 정보", user_count, "명 · 신뢰 IP", trusted_count, "개")  # 단계 1 시작을 알리는 줄

print("--- 단계 2: 알림마다 붙인 정보(재직 · VIP · 접속 IP)")  # 단계 2 시작을 알리는 줄
for incident in incidents:                                     # 인시던트를 하나씩 꺼낸다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 7. enrich_incident(incident, users_info, source_ips, trusted_ips) 를 호출한다 (인시던트에 맥락이 붙는다)
    context = incident["context"]                              # 붙은 맥락을 꺼낸다
    if context["account_known"]:                               # 계정 정보가 있으면
        if context["employed"]:                                # 재직 중이면
            employed_text = "재직"                             # 재직이라고 적는다
        else:                                                  # 아니면
            employed_text = "퇴사"                             # 퇴사라고 적는다
    else:                                                      # 계정 정보가 없으면
        employed_text = "계정 아님"                            # 계정이 아니라고 적는다
    vip_text = "아니오"                                        # 처음에는 아니오로 적는다
    if context["vip"]:                                         # VIP 이면
        vip_text = "예"                                        # 예라고 적는다
    ip_text = "없음"                                           # 처음에는 없음으로 적는다
    if context["source_ip"]:                                   # 접속 IP 가 있으면
        ip_text = context["source_ip"]                         # 그 IP 를 적는다
    trusted_text = "아니오"                                    # 처음에는 아니오로 적는다
    if context["ip_trusted"]:                                  # 신뢰 IP 이면
        trusted_text = "예"                                    # 예라고 적는다
    print(incident["id"], incident["entity"], "· 재직:", employed_text, "· VIP:", vip_text, "· 접속 IP:", ip_text, "· 신뢰 IP:", trusted_text)  # 한 줄로 출력한다

print("--- 단계 3: VIP 계정 알림 수")                          # 단계 3 시작을 알리는 줄
vip_count = 0                                                  # VIP 계정 알림 수 : 처음에는 0 이다
for incident in incidents:                                     # 인시던트를 하나씩 꺼낸다
    context = incident["context"]                              # 붙은 맥락을 꺼낸다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 8. context 의 "vip" 가 참이면 (if)
    # 9.   vip_count 에 vip_count + 1 을 담는다 (1 늘린다)
print("VIP 계정 알림", vip_count, "건")                        # VIP 계정 알림 수를 출력한다
```

**순서**

1. **[터미널]** 파일 두 개를 만들고 **[VS Code]** 에서 열어 붙여 넣습니다.
   ```bash
   pwd
   touch enrichment.py exercise2-1_run.py
   ls
   ```
2. **[VS Code]** `enrichment.py` 1 ~ 6번, `exercise2-1_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「실습 2-1 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise2-1_run.py
   ```
4. 출력은 세 단계입니다. 단계 1 은 숫자가 제목 줄에 함께 나옵니다. 단계 2 는 알림 5건이 한 줄씩 나오고 한 줄에는 번호 · 대상 · 재직 · VIP · 접속 IP · 신뢰 IP 가 순서대로 있습니다. 단계 3 은 1줄입니다.
5. **[보고서]** Unit 2 의 `## 실습 2-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 재직 여부가 「퇴사」인 알림과 VIP 가 「예」인 알림의 번호, 단계 3 의 VIP 계정 알림 수를 적어 주세요.
   - (나) [핵심 질문] INC-005 는 맥락이 모두 초기값(`False` · `None`)으로 남았습니다. 그 원인을 `lookup_account` 와 `lookup_source_ip` 의 `if` 조건을 근거로 설명해 주세요. 또 INC-005 의 `employed` 가 `True`(재직)로 판정된다면 어떤 문제가 생기는지도 적어 주세요.
   - (다) [핵심 질문] INC-002 와 INC-004 는 접속 IP 가 같고 둘 다 「신뢰 IP: 예」입니다. 두 알림의 `reasons`(알림을 발생시킨 탐지 규칙 이름 목록)를 비교해 보세요. 접속 IP 가 같은 신뢰 IP 라는 근거만으로 두 알림을 동일하게 처리해도 되는지 적어 주세요.

## 실습 2-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 딕셔너리에 그 이름(키)이 있는지 | `if entity in users_info:` |
| 딕셔너리 안의 딕셔너리 값 꺼내기 (`users_info["gaeun"]["vip"]` 는 `True`) | `users_info[entity]["employed"]` |
| 딕셔너리에 값 저장하기 | `account["vip"] = users_info[entity]["vip"]` |
| 리스트에 포함되는지 검사한 결과(`True` · `False`) 저장 | `ip_info["ip_trusted"] = source_ips[entity] in trusted_ips` |
| 함수 호출하기 | `enrich_incident(incident, users_info, source_ips, trusted_ips)` |
| 1 늘려 다시 저장하기 | `vip_count = vip_count + 1` |

---
