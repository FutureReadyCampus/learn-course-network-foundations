---
id: m5-u01-l05
title: 실습 1-3 · 알림에 맥락 정보 보강하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/118_day02_am_context_route_safety.md
  mission_id: GichanSource.m5-1110-am-context-route-safety
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 1-3 · 알림에 맥락 정보 보강하기

## 이번 의뢰: 맥락 없는 자동 조치

> **오늘 들어온 일**
>
> - **상황**: 실습 1-2에서 만든 실행기는 알림에 맞는 플레이북이 있으면 계정 잠금(account lockout, 어카운트 락아웃: 계정의 로그인을 비활성화하는 조치) 같은 조치를 즉시 실행했습니다. 오늘 샘플 알림 5건 가운데 세 건은 상황이 서로 다릅니다.
> - `INC-001`: 퇴사자 `dami` 의 계정입니다. 잠가도 업무에 지장이 없습니다.
> - `INC-003`: `gaeun` 은 직원 계정을 관리하는 계정 관리자입니다. 이 계정이 잠기면 계정 관리 업무가 중단됩니다. 이처럼 잠겼을 때 업무에 미치는 영향이 큰 고중요도 계정을 **VIP 계정**(VIP account)이라고 합니다.
> - `INC-004`: `jiwoo` 는 협력사 사무실에서 평소와 같이 접속했을 뿐이므로 잠글 사유가 없습니다.
> - **문제**: 프로그램은 알림에 적힌 탐지 규칙 이름과 위험 등급만 참조합니다. 퇴사 여부, VIP 계정 여부, 접속 IP 의 신뢰 여부를 알지 못한 채 모든 알림에 같은 절차를 실행합니다. 실습 1-2 실행 결과에서는 `INC-003` · `INC-004` 가 맞는 플레이북이 없어 조치가 실행되지 않았지만, 맞는 플레이북이 생기면 상황과 무관하게 같은 절차로 처리됩니다.
> - **부탁**: 조치를 실행하기 전에 「대상이 누구이고 어디에서 접속했는가」를 알림마다 조회해 알림에 추가해 주세요.
> - **바뀌는 점**: 「즉시 자동으로 잠글지, 담당자 승인을 받을지」를 정할 때 계정 이름이 아니라 알림에 추가된 정보(맥락)를 근거로 삼습니다. 상황과 이름은 설명을 위한 예시입니다.

## 3.1 보강(enrichment) — 조치 실행 전에 알림에 맥락 정보를 추가한다

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
- **`True` · `False` · `None`**: `True` 는 「참」(그렇다), `False` 는 「거짓」(아니다), `None` 은 「값 없음」입니다. JSON 파일에 적은 `true` · `false` 는 파이썬으로 읽으면 `True` · `False` 가 됩니다.
- **정보를 찾지 못했을 때**: 「확인되지 않음」을 뜻하는 초기값(`False` 또는 `None`)을 그대로 둡니다. 확인되지 않은 대상을 재직 중인 정상 사용자로 간주하면 안 되기 때문입니다.
- **주의할 점**: 계정 정보에 없는 대상의 `employed` · `vip` 가 `False` 여도 「퇴사했다」나 「VIP 가 아니다」라는 판정이 아니라, 「계정 정보에 없어 확인할 수 없다」는 뜻입니다.

함수 세 개가 각각 다른 일을 하고, 직접 쓰는 곳은 **세 군데**(① · ② · ③)입니다. 나머지 줄은 미리 채워 두었습니다.

```
enrichment.py   lookup_account   : 대상이 users_info 안에 있으면 (① 직접 씀) 재직 · VIP 를 담는다
                lookup_source_ip : 대상이 source_ips 안에 있으면 접속 IP 와 신뢰 IP 여부(② 직접 씀)를 담는다
                enrich_incident  : 두 결과를 합쳐 incident["context"] 에 붙인다 (미리 채움)
실행 파일       exercise1-3_run.py : 알림마다 맥락을 붙이는 함수를 호출하고 (③ 직접 씀), VIP 이면 VIP 알림 수를 1 늘린다 (미리 채움)
```

<h2>문법 상자 · 직접 쓰는 곳의 모양 (예시 값 · 읽기만 합니다)</h2>

```python
users_info = {"gaeun": {"employed": True, "vip": True}}   # 예시 값
trusted_ips = ["203.0.113.80"]

print("gaeun" in users_info)              # True  · 딕셔너리에 그 키가 있다
print("198.51.100.90" in users_info)      # False · 없다
print("203.0.113.80" in trusted_ips)      # True  · 리스트에 그 값이 있다

is_trusted = "203.0.113.80" in trusted_ips   # in 의 결과(True · False)를 변수에 담을 수 있다
print(is_trusted)                         # True
```

- `if 값 in 딕셔너리:` 는 「그 키가 있으면」입니다. 키가 있는지 먼저 확인해야 `딕셔너리[값]` 으로 꺼낼 때 `KeyError` 가 나지 않습니다.
- 함수를 부를 때는 `함수이름(값1, 값2, …)` 처럼 이름 뒤 괄호 안에 넘길 값을 차례로 씁니다.

## 실습 1-3 · 알림 5건 보강하고 VIP 알림 수 세기

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>알림 5건에는 대상 이름과 위험 등급만 있어서 퇴사자 · VIP 계정 · 신뢰 IP 에서 온 접속을 구별할 수 없습니다</mark>.
- **만드는 것**: 계정 정보 조회와 접속 IP 정보 조회(`enrichment.py`), 보강 함수 호출과 VIP 계정 알림 수 집계(`exercise1-3_run.py`).
- **실행하면**: <mark>단계 1: 불러온 개수, 단계 2: 알림마다 붙인 정보, 단계 3: VIP 계정 알림 수가 나옵니다.</mark>

**할 일**: 두 파일을 만들어 붙여 넣고, `# ←` 가 있는 <mark>세 곳</mark>(① · ② · ③)을 한 줄씩 채웁니다. 실행해서 단계 2 · 3 을 읽습니다.

<h3><code>enrichment.py</code></h3>

알림에 맥락을 추가하는 보강 함수를 정의합니다. 응용 1-1 실행 파일도 `enrich_incident` 를 가져와 사용(import)합니다. 직접 쓰는 곳은 ① · ② 두 곳입니다.

```python
def lookup_account(entity, users_info):                              # 대상 이름과 계정 정보 딕셔너리를 받는 함수
    """계정 정보 파일에서 이 대상이 재직 중인지, VIP 계정인지 찾아 딕셔너리로 리턴한다.
    파일에 이름이 없는 대상(IP 등)은 처음 값(False)을 그대로 리턴한다.
    """
    account = {"employed": False, "vip": False}                      # 처음에는 모르는 상태로 시작한다
    # ① entity 가 users_info 안에 있으면 (if, in)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
        account["employed"] = users_info[entity]["employed"]         # 재직 여부를 담는다
        account["vip"] = users_info[entity]["vip"]                   # VIP 여부를 담는다
    return account                                                   # 계정 정보를 리턴한다


def lookup_source_ip(entity, source_ips, trusted_ips):               # 대상 이름 · 접속 IP 딕셔너리 · 신뢰 IP 리스트를 받는 함수
    """이 대상이 접속한 IP 와, 그 IP 가 신뢰 IP 목록에 있는지 찾아 딕셔너리로 리턴한다.
    접속 IP 를 모르는 대상은 처음 값(None 과 False)을 그대로 리턴한다.
    """
    ip_info = {"source_ip": None, "ip_trusted": False}               # 처음에는 모르는 상태로 시작한다
    if entity in source_ips:                                         # 접속 IP 를 아는 대상이면
        ip_info["source_ip"] = source_ips[entity]                    # 접속 IP 를 담는다
        # ② ip_info 의 "ip_trusted" 에 source_ips[entity] 가 trusted_ips 안에 있는지(in)의 결과를 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
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

<h3><code>exercise1-3_run.py</code></h3>

③ 한 곳만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 이 실행 파일은 결과를 JSON 파일로 저장하지 않고 화면에만 출력합니다.

```python
from incident import load_json, INCIDENTS_PATH                 # 실습 1-2 의 incident.py 에서 함수를 불러온다
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
    # ③ enrich_incident(incident, users_info, source_ips, trusted_ips) 를 호출한다 (인시던트에 맥락이 붙는다)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
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
    if context["vip"]:                                         # VIP 계정이면
        vip_count = vip_count + 1                              # VIP 계정 알림 수를 1 늘린다
print("VIP 계정 알림", vip_count, "건")                        # VIP 계정 알림 수를 출력한다
```

<h3>직접 쓰는 곳</h3>

| 빈칸 | 파일 · 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | `enrichment.py` · 대상이 계정 정보에 있으면 (`if`) | 4칸 |
| ② | `enrichment.py` · 신뢰 IP 인지(`in`)를 담기 | 8칸 |
| ③ | `exercise1-3_run.py` · 보강 함수 호출 | 4칸 |

- 주석 줄은 그대로 두고, **각 주석 바로 아래 줄**에 씁니다. ① 은 함수 안의 `if` 줄이라 4칸, ② 는 바로 위 `ip_info["source_ip"] = …` 줄과 같은 8칸, ③ 은 `for` 안이라 4칸에서 시작합니다.
- 채우기 전에 실행하면 `IndentationError: unexpected indent` 가 나옵니다. ① 의 `if` 가 없어서 8칸으로 들여 쓴 `account["employed"] = …` 줄이 갈 곳이 없기 때문이니 정상입니다.
- ① 확인: ① 을 쓰고 실행하면 `KeyError: 'context'` 가 나옵니다. ③ 을 아직 안 써서 알림에 맥락이 붙지 않았기 때문이니 정상입니다. 막히면: 바로 아래 `lookup_source_ip` 의 `if entity in source_ips:` 와 같은 모양이고 딕셔너리 이름만 `users_info` 입니다.
- ② 확인: ② 를 써도 ③ 전에는 같은 `KeyError: 'context'` 가 나옵니다. ③ 까지 쓴 뒤 단계 2 의 INC-002 · INC-004 줄 끝이 `신뢰 IP: 예` 이면 ② 가 맞습니다. 막히면: 위 문법 상자의 `is_trusted = "203.0.113.80" in trusted_ips` 에서 왼쪽을 `ip_info["ip_trusted"]` 로, 따옴표 IP 를 `source_ips[entity]` 로 바꿉니다.
- ③ 확인: ③ 까지 쓰고 실행하면 단계 2 에 다섯 줄, 단계 3 에 `VIP 계정 알림 1 건` 이 나와야 합니다. 막히면: 주석에 적힌 `enrich_incident(…)` 를 괄호까지 그대로 씁니다. 리턴 값은 받지 않아도 됩니다. 함수가 `incident` 에 바로 `context` 를 붙이기 때문입니다.

- `if context["source_ip"]:` 처럼 `if` 뒤에 비교 없이 값만 쓰면, 파이썬은 `None` 을 거짓으로, `"203.0.113.80"` 처럼 글자가 들어 있는 값을 참으로 봅니다. 그래서 접속 IP 를 찾은 알림만 그 IP 를 적고, 못 찾은 알림은 「없음」으로 남습니다.

<h2>순서</h2>

1. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `enrichment.py` · `exercise1-3_run.py` 두 파일을 하나씩 만들고(파일 이름 그대로), 위에서 같은 이름의 코드 상자를 붙여 넣어 저장합니다.
2. **[VS Code]** `enrichment.py` 의 ① · ②, `exercise1-3_run.py` 의 ③ 을 채웁니다. 막히면 위 「직접 쓰는 곳」의 확인과 힌트를 봅니다.

<!-- checklist -->
- [ ] `enrichment.py` 를 `soar_response` 폴더에 만들어 붙여 넣고 ① · ② 를 채워 저장했다
- [ ] `exercise1-3_run.py` 를 만들어 붙여 넣고 ③ 을 채워 저장했다
<!-- /checklist -->

3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다.
   ```bash
   python exercise1-3_run.py
   ```
4. 출력은 세 단계입니다.

   | 단계 | 나오는 것 |
   |---|---|
   | 1 | 숫자가 제목 줄에 함께 나온다 |
   | 2 | 알림 5건이 한 줄씩. 한 줄에 번호 · 대상 · 재직 · VIP · 접속 IP · 신뢰 IP 순서 |
   | 3 | 1줄 |

<!-- checklist -->
- [ ] `python exercise1-3_run.py` 를 실행해 단계 3 에 `VIP 계정 알림 1 건` 이 나왔다
<!-- /checklist -->

5. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.
   - (가) [핵심 질문] 실행한 출력을 보고, 재직 여부가 「퇴사」인 알림과 VIP 가 「예」인 알림의 번호, 단계 3 의 VIP 계정 알림 수를 적어 주세요.

**확인** — 단계 2 의 다섯 줄에서 INC-001 이 `재직: 퇴사`, INC-003 이 `VIP: 예`, INC-002 · INC-004 가 `신뢰 IP: 예` 이고, 단계 3 이 `VIP 계정 알림 1 건` 이면 성공입니다. 안 나오면 아래 실습 1-3 정답 펼침에서 출력과 한 줄씩 맞춰 보고, 다른 줄이 있으면 위 「직접 쓰는 곳」의 확인을 다시 봅니다.

## 실습 1-3 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 딕셔너리에 그 이름(키)이 있는지 (①) | `if entity in users_info:` |
| 딕셔너리 안의 딕셔너리 값 꺼내기 (`users_info["gaeun"]["vip"]` 는 `True`) | `users_info[entity]["employed"]` |
| 딕셔너리에 값 저장하기 | `account["vip"] = users_info[entity]["vip"]` |
| 리스트에 포함되는지 검사한 결과 저장 (②) | `ip_info["ip_trusted"] = source_ips[entity] in trusted_ips` |
| 함수 호출하기 (③) | `enrich_incident(incident, users_info, source_ips, trusted_ips)` |
| 1 늘려 다시 저장하기 | `vip_count = vip_count + 1` |

---

## 핵심 결과 점검과 코드 저장소 반영

핵심 실습의 코드와 결과를 확인하고 저장소에 기록합니다. 응용 실습은 이 절차에 포함되지 않습니다.

<h2>1. 오늘 한 일 확인</h2>

1. 플레이북 PB-003 을 직접 쓰고, 알림 두 건을 손으로 처리하며 고친 곳을 세었다 (실습 1-1)
2. 실행기가 알림 5건을 처리하고, 승인이 필요한 건은 멈추고, 감사 기록을 남겼다 (실습 1-2)
3. 알림마다 재직 · VIP · 접속 IP 맥락을 붙이고 VIP 계정 알림 수를 셌다 (실습 1-3)
4. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.

<h2>2. 파일 확인</h2>

**[터미널]** `soar_response` 폴더에서 확인합니다.

```bash
pwd
ls
ls config
```

- `pwd` 가 `…/soar_response` 로 끝나야 합니다.
- `ls` 에 아래 파일이 모두 보여야 합니다.

| 만든 곳 | 파일 |
|---|---|
| 시작하기 | `incident_samples.json` · `system_state.json` · `users_info.json` · `source_ips.json` · `trusted_ips.json` |
| 실습 1-2 | `incident.py` · `playbook_runner.py` · `exercise1-2_run.py` · `action_log.json`(실행하면 생김) |
| 실습 1-3 | `enrichment.py` · `exercise1-3_run.py` |

- `config` 안에는 `playbook_registry.json` 이 보여야 합니다.

<!-- checklist -->
- [ ] `soar_response` 폴더와 `config` 폴더에 2번 표의 파일이 모두 있는 것을 확인했다
<!-- /checklist -->

<h2>3. 깃허브에 올리기</h2>

Module 5 폴더를 처음 올리는 날이므로 올라가는 파일 목록을 꼭 확인합니다.

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark>`soar_response/` 가 새 폴더로 보이면</mark> 됩니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore`(깃에 올리지 않을 파일 이름을 적어 두는 파일)를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 올릴 필요가 없으므로 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.

<!-- checklist -->
- [ ] `git status` 에서 `.env` · `.venv` 가 올라갈 목록에 없는 것을 확인했다(있으면 `.gitignore` 에 적었다)
<!-- /checklist -->

3. 실행 결과에서 선택한 글감의 근거를 찾아 초안의 ‘검증 결과’에 메모합니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add SOAR unit 1 playbook runner, enrichment and report"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git add .` · `git commit` · `git push` 로 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소 `network-study-notes` 를 새로 고쳐 `soar_response` 폴더를 열고, 2번에서 확인한 파일이 모두 있는지 봅니다. `__pycache__` 폴더는 없어도 됩니다.

<!-- checklist -->
- [ ] 깃허브의 `network-study-notes` 저장소에서 `soar_response` 폴더의 파일을 확인했다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 이 「3. 깃허브에 올리기」의 1 ~ 4번(`cd ..` 부터 `git push` 까지, 그림의 3 ~ 5)을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

<h2>4. 이어지는 곳</h2>

| 다시 쓰는 곳 | 오늘 만든 것 |
|---|---|
| Module 5 끝까지 | `config/playbook_registry.json` · `incident.py` · `incident_samples.json` 을 그대로 불러 쓴다 |
| Unit 2 응용 2-2 · Unit 3 응용 3-1 | `enrichment.py` 의 `enrich_incident` 와 `users_info.json` · `source_ips.json` · `trusted_ips.json` (알림에 맥락을 붙일 때) |
| Unit 2 응용 2-2 · Unit 3 응용 3-1 | 응용 준비 레슨의 `routing.py` |
| Unit 2 응용 2-2 | 응용 준비 레슨의 `safe_runner.py` |

- Unit 2 는 연습용 시스템에 적기만 하던 `계정 잠금` 을 실행한 뒤 정말 잠겼는지 다시 확인하고, 조치 전 · 후 상태를 기록으로 남깁니다.

**확인** — 깃허브의 `soar_response` 폴더에 2번 표의 파일이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이는 파일이 있으면 `git status` 를 다시 쳐서 그 파일이 빨간 목록에 남아 있는지 보고 3번의 4단계(`git add .` 부터)를 다시 합니다.

---

<!-- answer: 08|실습 1-3 정답 -->

<!-- learn:answers -->
