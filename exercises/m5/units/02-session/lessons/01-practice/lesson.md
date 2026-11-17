---
id: m5-u02-l01
title: 자동 대응(SOAR) ② — 알림 보강(enrichment) · 조건 분기(branching)에 따른 처리 경로(route) 결정 · 자동 대응 안전장치(guardrail) 적용
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/118_day02_am_context_route_safety.md
  mission_id: GichanSource.m5-1110-am-context-route-safety
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 자동 대응(SOAR) ② — 알림 보강(enrichment) · 조건 분기(branching)에 따른 처리 경로(route) 결정 · 자동 대응 안전장치(guardrail) 적용

## 개요

오늘 오전은 SOAR 자동 대응의 판단 단계를 구현합니다. 2교시는 알림 보강(enrichment, 인리치먼트: 판단에 필요한 정보를 알림에 추가하는 일), 3교시는 맥락에 따른 조건 분기(branching, 브랜칭: 조건에 따라 처리 경로를 나누는 일), 4교시는 안전장치(guardrail, 가드레일: 자동 대응이 잘못 실행되어도 피해가 커지지 않도록 두는 점검 · 제한 장치)입니다.

깃허브 업로드는 오후 6교시 마지막에 합니다. 새 문법은 3교시의 **튜플 리턴과 언패킹**(두 값을 한 번에 리턴하고 한 번에 받는 문법)과 4교시의 **`startswith`**(문자열이 지정한 문자열로 시작하는지 확인하는 메서드) 둘입니다. 보고서의 🔍 질문은 <mark>내 출력 값을 근거로 사유까지</mark> 씁니다. 들여쓰기는 미리 채운 줄에 맞춥니다. 각 번호 주석 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

📎 **이전 파일**: 어제 만든 `incident.py` · `playbook_runner.py` · `incident_samples.json` · `config/playbook_registry.json` 을 씁니다. 없는 파일은 복구 안내 `day02_am_recovery_files.md` 의 순서로 만듭니다(`config/playbook_registry.json` 만 `complete_files.md` 의 1절에서 만듭니다).

## 시작하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 5과목 폴더로 들어가 어제 파일을 확인합니다. <mark>`ls` 결과에 `config` · `incident.py` · `incident_samples.json` · `playbook_runner.py` 가 보이면</mark> 됩니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. 오늘 받은 파일 두 개(`day02_am_context_route_safety.md`, `day02_am_report.md`)를 `soar_response` 폴더로 옮기고, 보고서 제목의 `이름` 을 내 이름으로 바꿉니다.
4. **[터미널]** 데이터 파일 세 개를 만들고 **[VS Code]** 에서 열어 아래 내용을 붙여 넣습니다.
   ```bash
   touch users_info.json source_ips.json trusted_ips.json
   ls
   ```

**`users_info.json`** — 계정 이름별 재직 여부(`employed`)와 VIP 계정(VIP account, 브이아이피 계정: 잠기면 업무에 미치는 영향이 큰 고중요도 계정) 여부(`vip`)를 기록한 파일입니다. `true` 는 「그렇다」, `false` 는 「아니다」입니다. 실제 조직에서는 인사 시스템과 IAM(Identity and Access Management, 아이덴티티 앤 액세스 매니지먼트: 계정과 접근 권한을 관리하는 체계)이 보유한 정보이고, 오늘은 파일로 대신합니다. `dami` 는 퇴사자(`employed` 가 `false`), `gaeun` 은 VIP 계정(`vip` 가 `true`)입니다. 2 ~ 4교시에서 읽어 사용합니다.

```
{
  "dami": {"employed": false, "vip": false},
  "seoyeon": {"employed": true, "vip": false},
  "gaeun": {"employed": true, "vip": true},
  "jiwoo": {"employed": true, "vip": false},
  "junho": {"employed": true, "vip": false},
  "hana": {"employed": true, "vip": false}
}
```

**`source_ips.json`** — 사용자 이름별로 로그인에 사용한 접속 IP(source IP, 소스 아이피: 로그인 요청이 출발한 출발지 IP)를 기록한 파일입니다. 이 파일에 이름이 없는 사용자는 접속 IP 기록이 없는 사용자입니다. 2교시에서 읽습니다.

```
{
  "seoyeon": "203.0.113.80",
  "jiwoo": "203.0.113.80",
  "gaeun": "198.51.100.77",
  "junho": "192.0.2.41"
}
```

**`trusted_ips.json`** — **신뢰 IP**(trusted IP, 트러스티드 아이피: 정상 접속의 출처로 사전에 확인해 등록한 IP) 목록입니다. 협력사 사무실 IP 한 개가 등록되어 있고, `seoyeon` 과 `jiwoo` 가 이 IP 에서 접속합니다. 2교시에서 읽습니다.

```
[
  "203.0.113.80"
]
```

5. **[터미널]** 두 가지를 확인합니다. 먼저 데이터 파일입니다. <mark>`6 4 1` 이 나와야</mark> 합니다.
   ```bash
   python -c "import json; print(len(json.load(open('users_info.json', encoding='utf-8'))), len(json.load(open('source_ips.json', encoding='utf-8'))), len(json.load(open('trusted_ips.json', encoding='utf-8'))))"
   ```
6. **[터미널]** 어제 만든 플레이북(playbook, 플레이북: 알림 유형별 대응 절차를 사전에 정의한 문서)의 등록 값을 점검합니다. 오늘 출력이 문서와 일치하려면 이 값이 <mark>아래 출력과 같아야</mark> 합니다. 다르면 `config/playbook_registry.json` 을 열어 해당 값을 같게 고칩니다(어제 내 파일은 깃허브에 올라가 있습니다).
   ```bash
   python -c "import json; print([(p['id'], p['trigger_rule'], p['min_grade'], p['approval']) for p in json.load(open('config/playbook_registry.json', encoding='utf-8'))])"
   ```
   ```
   [('PB-001', '퇴사한 계정', 'high', '자동'), ('PB-002', '대량 다운로드', 'mid', '담당자 승인 필요'), ('PB-003', '경로 스캔', 'low', '담당자 승인 필요')]
   ```

## 🆘 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError: No module named 'incident'` 는 <mark>어제 만든 `incident.py` 가 이 폴더에 없다는 뜻</mark>입니다. `day02_am_recovery_files.md` 의 3번에서 만듭니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다.

---


> 📨 **오늘 들어온 일**
>
> - **상황**: 월요일에 만든 프로그램은 알림에 맞는 플레이북이 있으면 계정 잠금(account lockout, 어카운트 락아웃: 계정의 로그인을 비활성화하는 조치) 같은 조치를 즉시 실행했습니다. 오늘 샘플 알림 5건 가운데 세 건은 상황이 서로 다릅니다.
>   - `INC-001`(알림 한 건에 부여한 식별 번호): 퇴사자 `dami` 의 계정입니다. 잠가도 업무에 지장이 없습니다.
>   - `INC-003`: `gaeun` 은 직원 계정을 관리하는 계정 관리자입니다. 이 계정이 잠기면 계정 관리 업무가 중단됩니다. 이처럼 잠겼을 때 업무에 미치는 영향이 큰 고중요도 계정을 **VIP 계정**(VIP account)이라고 합니다.
>   - `INC-004`: `jiwoo` 는 협력사 사무실에서 평소와 같이 접속했을 뿐이므로 잠글 사유가 없습니다.
> - **문제**: 프로그램은 알림에 적힌 탐지 규칙 이름과 위험 등급만 참조합니다. 퇴사 여부, VIP 계정 여부, 접속 IP 의 신뢰 여부를 알지 못한 채 모든 알림에 같은 절차를 실행합니다. 월요일 샘플에서는 `INC-003` · `INC-004` 가 맞는 플레이북이 없어 조치가 실행되지 않았지만, 맞는 플레이북이 생기면 상황과 무관하게 같은 절차로 처리됩니다.
> - **부탁**: 조치를 실행하기 전에 「대상이 누구이고 어디에서 접속했는가」를 알림마다 조회해 알림에 추가해 주세요.
> - **바뀌는 점**: 「즉시 자동으로 잠글지, 담당자 승인을 받을지」를 정할 때 계정 이름이 아니라 알림에 추가된 정보(맥락)를 근거로 삼습니다. 상황과 이름은 설명을 위한 예시입니다.
> - **용어**: **인시던트**(incident, 인시던트: 조사와 대응이 필요한 보안 사건 한 건)입니다. 이 문서에서는 알림 한 건을 인시던트 한 건으로 취급합니다. `INC-001` 의 `INC` 는 incident 의 앞 세 글자입니다.

> 📖 **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 📖 2.1 보강(enrichment) — 조치 실행 전에 알림에 맥락 정보를 추가한다

알림 한 건에 `context`(맥락)라는 딕셔너리를 추가합니다. 이 일을 **보강**(enrichment, 인리치먼트: 판단에 필요한 정보를 알림에 추가로 부여하는 일)이라고 하며, SOAR 플레이북에서는 조치를 실행하기 전에 대상의 재직 상태나 접속 출처 같은 맥락을 보강으로 먼저 확인하는 단계를 둡니다. 알림이 가리키는 사용자 이름 또는 IP 를 알림 대상(entity, 엔티티)이라고 하며, 코드에서는 `entity` 라고 씁니다. `context` 는 알림 대상에 대한 정보 다섯 가지를 키로 가집니다. 아래 표의 예는 VIP 계정인 `gaeun` 의 경우입니다.

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
실행 파일       day02_2-1_run.py : 알림마다 맥락을 붙이는 함수를 호출하고 (7번), VIP 이면 (8번) VIP 알림 수를 1 늘린다 (9번)
```

> ✍️ **여기부터 문제입니다.**

## ✍️ 문제 2-1 · 알림 5건을 보강하여 재직 · VIP · 접속 IP 맥락을 추가하고 VIP 계정 알림 수 집계하기

**📍 이런 상황이 있습니다**

- **지금은**: <mark>알림 5건에는 대상 이름과 위험 등급만 있어서 퇴사자 · VIP 계정 · 신뢰 IP 에서 온 접속을 구별할 수 없습니다</mark>.
- **만드는 것**: 계정 정보 조회와 접속 IP 정보 조회(`enrichment.py`), 보강 함수 호출과 VIP 계정 알림 수 집계(`day02_2-1_run.py`).
- **실행하면**: <mark>단계 1: 불러온 개수, 단계 2: 알림마다 붙인 정보, 단계 3: VIP 계정 알림 수가 나옵니다.</mark>

**🎯 할 일**: 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 · 3 을 읽습니다.

**`enrichment.py`** — 알림에 맥락을 추가하는 보강 함수를 정의합니다. 3교시 실행 파일도 `enrich_incident` 를 가져와 사용(import)합니다. 직접 쓰는 곳은 1 ~ 6번입니다.

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

**`day02_2-1_run.py`** — 7 ~ 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 파일을 저장하지는 않습니다.

```python
from incident import load_json, INCIDENTS_PATH                 # 월요일 파일의 함수를 불러온다
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
   touch enrichment.py day02_2-1_run.py
   ls
   ```
2. **[VS Code]** `enrichment.py` 1 ~ 6번, `day02_2-1_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「2교시 한눈에」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python day02_2-1_run.py
   ```
4. 출력은 세 단계입니다. 단계 1 은 숫자가 제목 줄에 함께 나옵니다. 단계 2 는 알림 5건이 한 줄씩 나오고 한 줄에는 번호 · 대상 · 재직 · VIP · 접속 IP · 신뢰 IP 가 순서대로 있습니다. 단계 3 은 1줄입니다.
5. **[보고서]** `day02_am_report.md` 의 `## 2교시` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 재직 여부가 「퇴사」인 알림과 VIP 가 「예」인 알림의 번호, 단계 3 의 VIP 계정 알림 수를 적어 주세요.
   - (나) 🔍 INC-005 는 맥락이 모두 초기값(`False` · `None`)으로 남았습니다. 그 원인을 `lookup_account` 와 `lookup_source_ip` 의 `if` 조건을 근거로 설명해 주세요. 또 INC-005 의 `employed` 가 `True`(재직)로 판정된다면 어떤 문제가 생기는지도 적어 주세요.
   - (다) 🔍 INC-002 와 INC-004 는 접속 IP 가 같고 둘 다 「신뢰 IP: 예」입니다. 두 알림의 `reasons`(알림을 발생시킨 탐지 규칙 이름 목록)를 비교해 보세요. 접속 IP 가 같은 신뢰 IP 라는 근거만으로 두 알림을 동일하게 처리해도 되는지 적어 주세요.

## 2교시 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 딕셔너리에 그 이름(키)이 있는지 | `if entity in users_info:` |
| 딕셔너리 안의 딕셔너리 값 꺼내기 (`users_info["gaeun"]["vip"]` 는 `True`) | `users_info[entity]["employed"]` |
| 딕셔너리에 값 저장하기 | `account["vip"] = users_info[entity]["vip"]` |
| 리스트에 포함되는지 검사한 결과(`True` · `False`) 저장 | `ip_info["ip_trusted"] = source_ips[entity] in trusted_ips` |
| 함수 호출하기 | `enrich_incident(incident, users_info, source_ips, trusted_ips)` |
| 1 늘려 다시 저장하기 | `vip_count = vip_count + 1` |

---


> 📨 **오늘 들어온 일**
>
> - **상황**: 지난주 협력사 사무실(`203.0.113.80`)에서 온 `평소와 다른 IP` 알림이 12건 있었습니다. 분석팀이 한 건씩 열어 분석(triage, 트리아지: 알림의 진위와 우선순위를 판정하는 초기 분류)했고 12건 모두 정상 업무로 판정되었습니다. 12건을 분석하는 데 1시간이 소요되었습니다(한 건당 5분).
> - **문제**:
>   - 그 1시간 동안 다른 알림을 확인하는 일이 늦어졌습니다.
>   - 반대로 계정 관리자 `gaeun`(VIP 계정)의 알림이 플레이북에 맞으면 지금은 일반 계정과 같은 절차로 처리됩니다. 이 계정이 잘못 잠기면 직원 계정 관리 업무가 중단됩니다.
> - **부탁**: 협력사의 정상 접속 알림은 종료 사유를 기록하고 자동으로 종료(close)해 주세요. 이처럼 실제로는 위협이 아닌데 위협으로 탐지된 알림을 **오탐**(false positive, 폴스 포지티브)이라고 합니다. VIP 계정은 담당자가 승인한 뒤에만 조치해 주세요.
> - **바뀌는 점**: 분석팀은 절감한 1시간을 위험도가 높은 알림 분석에 씁니다. VIP 계정은 담당자가 승인하기 전에는 조치되지 않습니다. 오늘 샘플에서는 5건 가운데 `INC-004` 한 건이 자동 종료되고 `INC-003` 한 건이 담당자 승인 경로로 분기됩니다. 12건과 5분은 설명을 위한 예시 숫자입니다.

> 📖 **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 📖 3.1 조건 분기(branching) — 맥락에 따라 알림을 서로 다른 처리 경로로 분기한다

알림을 조건에 따라 세 가지 처리 경로(route) 가운데 하나로 분류해 보냅니다. 이처럼 조건에 따라 실행 경로를 나누는 일을 **조건 분기**(branching, 브랜칭)라고 하며, SOAR 플레이북에서는 알림의 맥락이나 신뢰도에 따라 자동 실행과 분석가 검토 중 하나를 선택하는 데 씁니다.

| 경로 | 보내는 조건 | 하는 일 | 오늘 샘플 |
|---|---|---|---|
| `승인 필요` | 대상이 VIP 계정이다 | 담당자가 확인하기 전에는 조치하지 않는다 | `INC-003`(`gaeun`) |
| `오탐 종료` | 접속 IP 가 신뢰 IP 이고, 탐지된 규칙이 **모두** IP 관련 규칙이다 | 상태(status: 알림의 처리 진행 단계를 나타내는 값)를 `분류됨` 으로, 이어서 `종료` 로 변경하고 종료 사유를 기록한다 | `INC-004`(`jiwoo`) |
| `기본` | 위 두 경우가 아니다 | 어제 만든 플레이북 절차대로 처리한다 | `INC-001` · `INC-002` · `INC-005` |

- **탐지 규칙**(detection rule, 디텍션 룰: 알림을 발생시키는 조건): 알림에는 `reasons` 라는 리스트가 있고, 이 알림을 발생시킨 탐지 규칙의 이름이 요소로 저장되어 있습니다. 예를 들어 `INC-002` 는 `["평소와 다른 IP", "대량 다운로드"]` 입니다.
- **IP 관련 규칙**: 접속 IP 를 보고 낸 규칙입니다. 오늘은 `평소와 다른 IP` 와 `업무 시간 밖 로그인` 두 가지입니다.

- **상태**는 알림을 어디까지 처리했는지 나타내는 값이고, `탐지됨` → `분류됨` → `조치됨` 또는 `종료` 순서로 바뀝니다.
- <mark>VIP 를 먼저 확인합니다.</mark> VIP 계정의 알림이 신뢰 IP 에서 접속했다는 이유만으로 자동으로 닫히면 안 되기 때문입니다.
- <mark>탐지 규칙이 **모두** IP 관련일 때만 종료합니다.</mark> 신뢰 IP 에서 접속했어도 `대량 다운로드` 처럼 IP 와 무관한 규칙이 함께 탐지되었다면, 그 다운로드가 정상이라는 근거는 되지 못하기 때문입니다. `INC-002` 가 이에 해당합니다.

**🐍 문법 상자 — 튜플 리턴과 언패킹(tuple unpacking): 두 값을 한 번에 리턴하고 한 번에 받는다**

```python
def check(score):
    if score >= 60:
        return "높음", "바로 확인"
    return "낮음", "나중에 확인"

level, action = check(70)
print(level)
print(action)
```

| 코드 | 뜻 |
|---|---|
| `return "높음", "바로 확인"` | 값 두 개를 쉼표로 이어 함께 리턴한다. 이렇게 쉼표로 이은 값 묶음을 **튜플**(tuple)이라고 한다 |
| `level, action = check(70)` | 튜플로 온 두 값을 순서대로 변수 두 개에 하나씩 저장한다. 이렇게 묶음을 풀어 변수에 저장하는 것을 **언패킹**(unpacking)이라고 한다 |
| 위 코드의 출력 | `높음` 과 `바로 확인` 이 한 줄씩 나온다 |

- 리턴하는 값의 개수와 받는 변수의 개수가 다르면 `ValueError`(밸류 에러: 값의 개수나 형태가 맞지 않을 때 나는 오류)가 납니다.

직접 쓰는 곳은 함수와 실행 파일을 합쳐 **아홉 군데**입니다.

```
routing.py   is_only_ip_related : 규칙을 하나씩 꺼내 IP 관련이 아닌 것이 있으면 False 를 리턴한다 (1 ~ 3번)
             decide_route       : VIP 이면 「승인 필요」 (4 · 5번) / 신뢰 IP 이고 규칙이 모두 IP 관련이면 「오탐 종료」 (6 · 7번) / 아니면 「기본」 (미리 채움)
             apply_route        : 오탐 종료이면 상태를 종료로 옮기고 이유를 기록한다 (미리 채움)
실행 파일    day02_3-1_run.py   : decide_route 가 리턴한 두 값을 언패킹으로 받고 (8번), 경로별 건수를 센다 (9번)
```

> ✍️ **여기부터 문제입니다.**

## ✍️ 문제 3-1 · VIP 계정은 승인 경로로 분기하고, 신뢰 IP 의 IP 관련 알림은 오탐으로 종료하며 경로별 건수 집계하기

**📍 이런 상황이 있습니다**

- **지금은**: <mark>알림을 규칙 이름과 등급만 보고 처리하므로 계정 관리자(VIP)의 알림과 협력사의 정상 접속 알림을 따로 다룰 수 없습니다</mark>.
- **만드는 것**: 규칙이 모두 IP 관련인지 판별하는 함수와 처리 경로를 결정하는 함수(`routing.py`), 경로 수신과 경로별 건수 집계(`day02_3-1_run.py`). 경로를 결정할 때마다 판정 사유도 문장으로 함께 리턴합니다.
- **실행하면**: <mark>단계 1: 알림마다 경로 · 이유 · 상태, 단계 2: 경로별 건수가 나옵니다.</mark>

**🎯 할 일**: 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 1 · 2 를 읽습니다.

**`routing.py`** — 맥락을 보고 처리 경로를 정합니다. 이 파일이 정한 경로(`승인 필요` · `오탐 종료` · `기본`)를 오후 5교시 이후에도 씁니다. 직접 쓰는 곳은 1 ~ 7번입니다.

```python
from incident import change_status                                          # 월요일 파일의 상태 바꾸기 함수를 불러온다

IP_RELATED_RULES = ["평소와 다른 IP", "업무 시간 밖 로그인"]                # 접속 IP 만 보고 낸 알림의 규칙 이름


def is_only_ip_related(incident):                                           # 인시던트 하나를 받는 함수
    """알림이 난 이유(규칙)가 모두 IP 와 관련된 것이면 True, 하나라도 다른 이유가 있으면 False 를 리턴한다.
    IP 때문에만 난 알림인지, 다른 증거도 있는 알림인지 구별할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. incident["reasons"] 의 규칙을 하나씩 꺼낸다 (for, rule)
    # 2.   rule 이 IP_RELATED_RULES 안에 없으면 (if, not in)
    # 3.     False 를 리턴한다 (IP 와 관계없는 다른 증거가 있다)
    return True                                                             # 모두 IP 관련이면 True 를 리턴한다 — 미리 채운 줄


def decide_route(incident):                                                 # 맥락이 붙은 인시던트를 받는 함수
    """붙어 있는 맥락을 보고 이 알림을 어느 경로(승인 필요 · 오탐 종료 · 기본)로 보낼지 정해, 이유 문장과 함께 리턴한다.
    같은 플레이북이어도 누구의 알림이냐에 따라 처리를 다르게 하고 싶을 때 쓴다.
    """
    context = incident["context"]                                           # 붙어 있는 맥락
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 4. context 의 "vip" 가 참이면 (if)
    # 5.   "승인 필요" 와 "VIP 계정이라 담당자 승인이 필요함" 을 쉼표로 이어 함께 리턴한다
    # 6. context 의 "ip_trusted" 가 참이고(and) is_only_ip_related(incident) 가 참이면 (if)
    # 7.   "오탐 종료" 와 "신뢰 IP 에서 온 IP 관련 규칙뿐이라 정상 접속으로 봄" 을 쉼표로 이어 함께 리턴한다
    return "기본", "플레이북 기본 절차대로 처리함"                          # 어느 경우도 아니면 기본 경로로 보낸다


def apply_route(incident, route, reason, incident_log):                     # 인시던트 · 경로 · 이유 · 기록 리스트를 받는 함수
    """정한 경로를 알림에 적용한다. 오탐 종료이면 상태를 분류됨을 거쳐 종료로 바꾸고, 경로와 이유를 기록에 남긴다.
    나중에 「왜 이 알림을 이렇게 처리했나」에 답할 수 있게 하려고 쓴다.
    """
    if route == "오탐 종료":                                                # 오탐 종료이면
        change_status(incident, "분류됨")                                   # 먼저 분류됨으로 옮기고
        change_status(incident, "종료")                                     # 종료로 옮긴다
    entry = {"incident": incident["id"], "route": route, "reason": reason}  # 기록 한 건을 만든다
    incident_log.append(entry)                                              # 기록 리스트에 추가한다
```

**`day02_3-1_run.py`** — 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 2교시의 `enrichment.py` 가 같은 폴더에 있어야 합니다.

```python
from incident import load_json, INCIDENTS_PATH                      # 월요일 파일의 함수를 불러온다
from enrichment import enrich_incident                              # 2교시에 만든 함수를 불러온다
from routing import decide_route, apply_route                       # 방금 만든 함수를 불러온다

incidents = load_json(INCIDENTS_PATH)                               # 인시던트 파일을 리스트로 읽는다
users_info = load_json("users_info.json")                           # 계정 정보 파일을 읽는다
source_ips = load_json("source_ips.json")                           # 알림이 난 접속의 IP 파일을 읽는다
trusted_ips = load_json("trusted_ips.json")                         # 신뢰 IP 파일을 읽는다
incident_log = []                                                   # 경로 기록을 담을 빈 리스트
route_counts = {"기본": 0, "승인 필요": 0, "오탐 종료": 0}          # 경로마다 몇 건인지 셀 딕셔너리

print("--- 단계 1: 알림마다 정한 처리 경로 · 이유 · 상태")          # 단계 1 시작을 알리는 줄
for incident in incidents:                                          # 인시던트를 하나씩 꺼낸다
    enrich_incident(incident, users_info, source_ips, trusted_ips)  # 맥락을 붙인다
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 8. decide_route(incident) 가 리턴한 두 값을 route 와 reason 에 한 번에 받는다
    apply_route(incident, route, reason, incident_log)              # 경로를 적용하고 기록한다
    # 9. route_counts[route] 에 route_counts[route] + 1 을 담는다 (그 경로의 건수를 1 늘린다)
    print(incident["id"], incident["entity"], incident["grade"], "->", route, "·", reason, "(상태: " + incident["status"] + ")")  # 한 줄로 출력한다

print("--- 단계 2: 경로별 건수")                                    # 단계 2 시작을 알리는 줄
for route in route_counts:                                          # 경로를 하나씩 꺼낸다
    print(route, route_counts[route], "건")                         # 경로와 건수를 출력한다
```

**순서**

1. **[터미널]** 파일 두 개를 만들고 붙여 넣습니다.
   ```bash
   pwd
   touch routing.py day02_3-1_run.py
   ls
   ```
2. **[VS Code]** `routing.py` 1 ~ 7번, `day02_3-1_run.py` 8 · 9번을 씁니다. 막히면 아래 「3교시 한눈에」를 봅니다.
3. **[터미널]** 실행합니다(맥북은 `python3`).
   ```bash
   python day02_3-1_run.py
   ```
4. 출력은 두 단계입니다. 단계 1 은 알림 5건이 한 줄씩 나오고 한 줄에는 번호, 대상, 등급이 나오고 `->` 뒤에 경로, 사유, 괄호 안에 상태가 순서대로 나옵니다. 단계 2 는 경로마다 한 줄씩 3줄입니다.
5. **[보고서]** `day02_am_report.md` 의 `## 3교시` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 경로별 건수와 `종료` 상태가 된 알림의 번호를 적어 주세요.
   - (나) 🔍 INC-002 와 INC-004 는 둘 다 신뢰 IP 에서 접속했는데 INC-002 는 `기본`, INC-004 는 `오탐 종료` 입니다. 두 알림의 `reasons` 를 근거로 경로가 달라진 사유를 적어 주세요.
   - (다) 🔍 6번 조건보다 4번 VIP 판정을 먼저 두었습니다. VIP 계정이 신뢰 IP 에서 접속했고 `평소와 다른 IP` 규칙 하나만 탐지되었다고 가정해 보세요. 이 알림이 어느 경로로 분기되는지 적어 주세요. 그리고 4번과 6번 조건의 순서를 바꾸면 무엇이 달라지는지 적어 주세요.

## 3교시 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 리스트의 요소를 하나씩 반복 | `for rule in incident["reasons"]:` |
| 리스트 안에 없으면 | `if rule not in IP_RELATED_RULES:` |
| 참이면 | `if context["vip"]:` |
| 두 조건이 모두 참이면 | `if context["ip_trusted"] and is_only_ip_related(incident):` |
| 값 두 개를 함께 리턴 | `return "승인 필요", "VIP 계정이라 담당자 승인이 필요함"` |
| 리턴된 값 두 개를 한 번에 받기(언패킹) | `route, reason = decide_route(incident)` |
| 1 늘려 다시 저장하기 | `route_counts[route] = route_counts[route] + 1` |

---


> 📨 **오늘 들어온 일**
>
> - **상황**: 월요일에 만든 실행기(playbook runner, 플레이북 러너: 플레이북의 액션을 실제로 실행하는 프로그램)는 같은 알림 파일을 두 번 처리하면 `dami` 계정을 두 번 잠그고 티켓(ticket, 티켓: 담당자에게 일을 맡기려고 만드는 작업 요청 기록)을 두 번 생성합니다. 더 큰 위험은 인사 시스템의 오류입니다. 직원 전체가 퇴사자로 잘못 표시되면 퇴사자 알림이 대량으로 유입됩니다. 오늘 샘플에서는 이런 알림 7건(계정 6개)이 한꺼번에 유입됩니다.
> - **문제**: 실행기는 알림 수만큼 계정을 모두 잠급니다. 7건이 유입되면 서로 다른 계정 6개가 잠기고(`dami` 알림이 두 건이라 잠긴 계정 리스트에는 `dami` 가 두 번 기록됩니다), 100건이 유입되면 100개가 잠깁니다. 이 샘플에서 실제 퇴사자는 `dami` 한 명뿐입니다.
> - **부탁**: 이미 끝난 인시던트는 다시 처리하지 말고, 이미 잠긴 계정은 다시 잠그지 마세요. 또 한 번 실행할 때 잠글 수 있는 계정은 최대 3개로 제한해 주세요.
> - **바뀌는 점**: 같은 알림을 두 번 처리해도 `dami` 는 한 번만 잠기고, 알림이 몰려도 잠기는 계정이 3개를 넘지 않습니다. 그 사이에 담당자가 확인할 시간이 생깁니다.

> 📖 **읽을거리 — 문제가 아닙니다.** 읽고 이해만 합니다.

## 📖 4.1 안전장치(guardrail) 두 가지 — 중복 실행 방지와 영향 범위 제한

**안전장치**(guardrail, 가드레일: 자동 대응이 잘못 실행되어도 피해가 커지지 않도록 두는 사전 점검 · 제한 장치)는 실행기가 액션(계정 잠금처럼 대응으로 하는 동작 하나)을 실행하기 전에 「이 액션을 지금 실행해도 되는가」를 한 번 더 점검하는 장치입니다. 위험도가 높은 자동 조치는 신뢰도나 담당자 승인 같은 조건을 통과한 뒤에만 실행하도록 제한하는 것이 일반적인 설계 방식입니다. 코드에 나오는 용어는 다음과 같습니다.

- **`state`**: 연습용 시스템(실제 서버를 대신하는 연습용 시스템)의 현재 상태입니다. 잠긴 계정(`locked_users`) · 차단한 IP · 티켓을 저장한 딕셔너리입니다.
- **`DONE_STATUSES`**: 대응이 이미 끝난 상태 `조치됨` · `보고됨` · `종료` 를 모은 리스트입니다.
- **`MAX_LOCKS_PER_RUN`**: 한 번 실행에서 잠글 수 있는 계정의 최대 수이고 값은 3입니다.

| 안전장치 | 방지하는 일 | 오늘 수업에서 |
|---|---|---|
| **중복 실행 방지**(멱등성, idempotency, 아이뎀포턴시: 같은 조치를 여러 번 실행해도 한 번 실행한 것과 결과가 같도록 하는 성질) | 같은 알림이 두 번 와서 같은 대응을 두 번 하는 일 | 이미 끝난 인시던트는 실행하지 않고(미리 채움), 이미 잠긴 계정은 다시 잠그지 않는다 (1 · 2번) |
| **영향 범위 제한**(blast radius limit, 블라스트 레이디어스 리밋: 조치가 잘못됐을 때 영향을 받는 대상의 범위에 상한을 두는 것) | 잘못된 입력으로 계정이 대량으로 잠기는 일 | 한 번 실행에서 잠글 수 있는 계정을 `MAX_LOCKS_PER_RUN`(3개)까지만 허용한다 (3 · 4번) |

- 중복 실행 방지의 예: `dami` 를 잠그라는 요청이 두 번 들어와도 잠금은 한 번만 실행됩니다. 영향 범위 제한의 예: 알림이 100건 들어와도 이번 실행에서 잠기는 계정은 3개까지입니다.
- 한도는 **잘못된 알림을 식별하지는 못합니다.** 잘못된 알림이 유입되어도 잠기는 계정이 3개를 넘지 않게 제한할 뿐이며, 한도를 넘은 건은 「담당자 확인 필요」라고 기록합니다.
- 오늘 `bulk_incidents.json` 은 인사 오류로 몰린 퇴사자 알림 7건(계정 6개, `dami` 알림이 두 건)입니다. `users_info.json` 의 `employed` 를 보면 <mark>실제 퇴사자는 `dami` 한 명뿐입니다.</mark>

**🐍 문법 상자 — `startswith` 는 문자열이 지정한 문자열로 시작하는지 확인한다**

```python
result_text = "건너뜀: 이미 잠겨 있음"
print(result_text.startswith("건너뜀"))
print(result_text.startswith("실행"))
```

| 코드 | 결과 | 뜻 |
|---|---|---|
| `result_text.startswith("건너뜀")` | `True` | 글자가 「건너뜀」으로 시작한다 |
| `result_text.startswith("실행")` | `False` | 「실행」으로 시작하지 않는다 |

직접 쓰는 곳은 함수와 실행 파일을 합쳐 **아홉 군데**입니다.

```
safe_runner.py   find_skip_reason : 이미 잠긴 계정이면 (1 · 2번), 잠근 계정 수가 한도 이상이면 (3 · 4번) 건너뛸 이유를 리턴한다
                 safe_run_action  : 이유가 있으면 그 이유를 리턴하고 (5 · 6번), 없으면 어제의 run_action 으로 실행한다 (7번)
                 run_playbook_safe · process_safe : 결과를 이미 처리됨 · 승인 대기 · 일부 건너뜀 · 실행 완료로 나누고, 결과마다 몇 건인지 센다 (미리 채움)
실행 파일        day02_4-1_run.py : 기록에서 「건너뜀」으로 시작하는 결과만 골라 출력한다 (8 · 9번)
```

> ✍️ **여기부터 문제입니다.**

## ✍️ 문제 4-1 · 중복 실행을 방지하고 1회 실행당 잠글 수 있는 계정을 3개로 제한하기

**📍 이런 상황이 있습니다**

- **지금은**: <mark>같은 알림을 두 번 처리하면 계정이 두 번 잠기고, 인사 오류 알림이 몰리면 모든 계정이 잠깁니다</mark>.
- **만드는 것**: 건너뛰는 사유 판정과 안전장치를 적용한 액션 실행(`safe_runner.py`), 건너뛴 액션 선별 출력(`day02_4-1_run.py`).
- **실행하면**: <mark>단계 1 ~ 2: 어제 방식의 결과, 단계 3 ~ 4: 안전한 방식의 결과, 마지막에 건너뛴 액션과 이유가 나옵니다.</mark>

**🎯 할 일**: 파일 세 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 어제 방식과 안전한 방식의 차이를 읽습니다.

**`bulk_incidents.json`** — 인사 시스템 오류로 몰린 퇴사자 알림 7건입니다(모두 `퇴사한 계정` · `high`). `INC-B01` 과 `INC-B02` 는 같은 계정 `dami` 의 알림으로, 번호가 다른 알림 두 건이 같은 계정을 가리키는 경우를 일부러 만들어 둔 것입니다.

```
[
  {"id": "INC-B01", "entity": "dami", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B02", "entity": "dami", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B03", "entity": "seoyeon", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B04", "entity": "gaeun", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B05", "entity": "jiwoo", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B06", "entity": "junho", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"},
  {"id": "INC-B07", "entity": "hana", "grade": "high", "score": 60, "reasons": ["퇴사한 계정"], "status": "탐지됨"}
]
```

**`safe_runner.py`** — 안전장치를 건 실행기입니다. 오후 6교시에서 실패 처리를 더합니다. 직접 쓰는 곳은 1 ~ 7번입니다.

```python
from incident import change_status, match_playbooks, run_action, make_log_entry     # 월요일 파일의 함수를 불러온다

DONE_STATUSES = ["조치됨", "보고됨", "종료"]                                        # 이미 대응이 끝난 상태들
MAX_LOCKS_PER_RUN = 3                                                               # 한 번 실행에서 잠글 수 있는 계정의 최대 수


def find_skip_reason(action, entity, state):                                        # 액션 · 대상 · 연습용 시스템을 받는 함수
    """이 액션을 건너뛰어야 하면 그 이유 문장을, 건너뛸 필요가 없으면 빈 글자("")를 리턴한다.
    계정을 잠그기 전에 이미 잠긴 계정인지, 한 번에 잠글 수 있는 수를 넘었는지 확인할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. action 이 "계정 잠금" 이고(and) entity 가 state["locked_users"] 안에 있으면 (if, in)
    # 2.   "건너뜀: 이미 잠겨 있음" 을 리턴한다
    # 3. action 이 "계정 잠금" 이고(and) state["locked_users"] 의 개수(len)가 MAX_LOCKS_PER_RUN 이상이면 (if, >=)
    # 4.   "건너뜀: 한 번에 잠글 수 있는 계정 수를 넘음 (담당자 확인 필요)" 를 리턴한다
    return ""                                                                       # 건너뛸 이유가 없으면 빈 글자를 리턴한다 — 미리 채운 줄


def safe_run_action(action, incident, state):                                       # 액션 · 인시던트 · 연습용 시스템을 받는 함수
    """액션을 실행하기 전에 건너뛸 이유가 있는지 먼저 확인한다. 이유가 있으면 실행하지 않고 그 이유를, 없으면 월요일의 run_action 으로 실행한 결과를 리턴한다.
    같은 일을 두 번 하거나 너무 많이 하는 것을 막고 싶을 때 쓴다.
    """
    entity = incident["entity"]                                                     # 대응할 대상
    skip_reason = find_skip_reason(action, entity, state)                           # 건너뛸 이유를 구한다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. skip_reason 이 빈 글자("")가 아니면 (if, !=)
    # 6.   skip_reason 을 리턴한다
    # 7. run_action(action, incident, state) 의 결과를 리턴한다 (건너뛸 이유가 없으면 원래대로 실행한다)


def run_playbook_safe(incident, playbook, state, action_log):                       # 인시던트 · 플레이북 · 연습용 시스템 · 기록 리스트를 받는 함수
    """알림 한 건을 안전하게 처리한다. 이미 끝난 알림이면 건너뛰고, 승인이 필요하면 멈추고, 아니면 액션을 실행한다.
    처리 결과를 「실행 완료」 · 「승인 대기」 · 「이미 처리됨」 · 「일부 건너뜀」 중 하나로 리턴한다.
    """
    if incident["status"] in DONE_STATUSES:                                         # 이미 대응이 끝난 인시던트이면
        entry = make_log_entry(incident, playbook, "전체", "이미 처리됨 — 건너뜀")  # 건너뛴 기록을 만들고
        action_log.append(entry)                                                    # 기록 리스트에 추가한다
        return "이미 처리됨"                                                        # 이미 처리됨을 리턴한다
    change_status(incident, "분류됨")                                               # 대응을 시작하기 전에 분류됨 상태로 옮긴다
    if playbook["approval"] != "자동":                                              # 승인이 필요하면
        entry = make_log_entry(incident, playbook, "전체", "승인 대기")             # 승인 대기 기록을 만들고
        action_log.append(entry)                                                    # 기록 리스트에 추가한다
        return "승인 대기"                                                          # 승인 대기를 리턴한다
    skipped = False                                                                 # 건너뛴 액션이 있는지 : 처음에는 없다
    for action in playbook["actions"]:                                              # 액션을 하나씩 꺼낸다
        result = safe_run_action(action, incident, state)                           # 안전한 방식으로 실행한다
        if result.startswith("건너뜀"):                                             # 결과 문장이 「건너뜀」으로 시작하면
            skipped = True                                                          # 건너뛴 액션이 있다고 적는다
        entry = make_log_entry(incident, playbook, action, result)                  # 기록을 만들고
        action_log.append(entry)                                                    # 기록 리스트에 추가한다
    if skipped:                                                                     # 건너뛴 액션이 있으면
        return "일부 건너뜀"                                                        # 조치됨으로 옮기지 않고 일부 건너뜀을 리턴한다
    change_status(incident, "조치됨")                                               # 모두 실행했으니 조치됨으로 옮긴다
    return "실행 완료"                                                              # 실행 완료를 리턴한다


def process_safe(incidents, registry, state, action_log):                           # 인시던트 리스트 · 플레이북 리스트 · 연습용 시스템 · 기록 리스트를 받는 함수
    """알림을 하나씩 맞는 플레이북으로 안전하게 처리하고, 결과를 한 줄씩 출력한다.
    결과마다 몇 건인지 센 딕셔너리를 리턴한다.
    """
    counts = {}                                                                     # 실행 결과마다 몇 건인지 셀 딕셔너리
    for incident in incidents:                                                      # 인시던트를 하나씩 꺼낸다
        playbooks = match_playbooks(incident, registry)                             # 맞는 플레이북을 찾는다
        result_text = "맞는 플레이북 없음"                                          # 처음에는 없다고 적어 둔다
        for playbook in playbooks:                                                  # 맞는 플레이북을 하나씩 꺼낸다
            result_text = run_playbook_safe(incident, playbook, state, action_log)  # 안전하게 실행한다
        counts[result_text] = counts.get(result_text, 0) + 1                        # 그 결과의 건수를 1 늘린다
        print(incident["id"], incident["entity"], "->", result_text, "(상태: " + incident["status"] + ")")  # 한 줄로 출력한다
    return counts                                                                   # 결과별 건수를 리턴한다
```

**`day02_4-1_run.py`** — 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 어제 `playbook_runner.py` 의 완성된 `run_playbook` 이 필요합니다.

```python
from incident import load_json, match_playbooks, INCIDENTS_PATH, REGISTRY_PATH           # 월요일 파일의 함수를 불러온다
from playbook_runner import run_playbook                                                 # 월요일에 만든 실행기를 불러온다
from safe_runner import process_safe, MAX_LOCKS_PER_RUN                                  # 방금 만든 안전한 실행기를 불러온다

BULK_PATH = "bulk_incidents.json"                                                        # 인사 시스템 오류로 퇴사자 알림이 몰린 상황의 알림 파일 이름


def new_state():                                                                         # 인자가 없는 함수
    """잠긴 계정 · 차단한 IP · 티켓이 모두 비어 있는 연습용 시스템 상태를 새로 만들어 리턴한다.
    실험마다 깨끗한 상태에서 시작하고 싶을 때 쓴다.
    """
    state = {"locked_users": [], "blocked_ips": [], "tickets": [], "notifications": []}  # 비어 있는 상태 딕셔너리
    return state                                                                         # 상태를 리턴한다


def run_monday_way(incidents, registry, state, action_log):                              # 월요일 방식으로 처리하는 함수
    """월요일에 만든 run_playbook 으로 알림을 모두 처리한다. 오늘 만든 안전장치는 쓰지 않는다.
    안전장치가 없으면 어떤 일이 생기는지 보고 싶을 때 쓴다.
    """
    for incident in incidents:                                                           # 인시던트를 하나씩 꺼낸다
        playbooks = match_playbooks(incident, registry)                                  # 맞는 플레이북을 찾는다
        for playbook in playbooks:                                                       # 맞는 플레이북을 하나씩 꺼낸다
            run_playbook(incident, playbook, state, action_log)                          # 월요일 방식으로 실행한다


registry = load_json(REGISTRY_PATH)                                                      # 플레이북 등록 파일을 읽는다

print("--- 단계 1: 어제 방식(안전장치 없음)으로 같은 알림 5건을 두 번 처리")             # 단계 1 시작을 알리는 줄
incidents = load_json(INCIDENTS_PATH)                                                    # 알림 5건을 읽는다
state = new_state()                                                                      # 깨끗한 상태로 시작한다
action_log = []                                                                          # 기록 리스트를 만든다
run_monday_way(incidents, registry, state, action_log)                                   # 첫 번째 처리
run_monday_way(incidents, registry, state, action_log)                                   # 같은 알림을 한 번 더 처리한다
print("잠긴 계정:", state["locked_users"])                                               # 잠긴 계정을 출력한다
print("티켓:", len(state["tickets"]), "건")                                              # 티켓 수를 출력한다

print("--- 단계 2: 어제 방식(안전장치 없음)으로 인사 오류 알림 7건 처리")                # 단계 2 시작을 알리는 줄
bulk_incidents = load_json(BULK_PATH)                                                    # 인사 오류 알림 7건을 읽는다
state = new_state()                                                                      # 깨끗한 상태로 시작한다
action_log = []                                                                          # 기록 리스트를 만든다
run_monday_way(bulk_incidents, registry, state, action_log)                              # 월요일 방식으로 처리한다
locked_count = len(state["locked_users"])                                                # 잠긴 계정이 몇 개인지 센다
print("잠긴 계정", locked_count, "개:", state["locked_users"])                           # 잠긴 계정 수와 이름을 출력한다

print("--- 단계 3: 안전한 방식으로 같은 알림 5건을 두 번 처리")                          # 단계 3 시작을 알리는 줄
incidents = load_json(INCIDENTS_PATH)                                                    # 알림 5건을 다시 읽는다
state = new_state()                                                                      # 깨끗한 상태로 시작한다
action_log = []                                                                          # 기록 리스트를 만든다
print("첫 번째 처리")                                                                    # 첫 번째 처리임을 알리는 줄
process_safe(incidents, registry, state, action_log)                                     # 안전한 방식으로 처리한다
print("두 번째 처리")                                                                    # 두 번째 처리임을 알리는 줄
process_safe(incidents, registry, state, action_log)                                     # 같은 알림을 한 번 더 처리한다
print("잠긴 계정:", state["locked_users"])                                               # 잠긴 계정을 출력한다
print("티켓:", len(state["tickets"]), "건")                                              # 티켓 수를 출력한다

print("--- 단계 4: 안전한 방식으로 인사 오류 알림 7건 처리 (한 번에 최대", MAX_LOCKS_PER_RUN, "개)")  # 단계 4 시작을 알리는 줄
bulk_incidents = load_json(BULK_PATH)                                                    # 인사 오류 알림 7건을 다시 읽는다
state = new_state()                                                                      # 깨끗한 상태로 시작한다
action_log = []                                                                          # 기록 리스트를 만든다
counts = process_safe(bulk_incidents, registry, state, action_log)                       # 안전한 방식으로 처리한다
locked_count = len(state["locked_users"])                                                # 잠긴 계정이 몇 개인지 센다
print("잠긴 계정", locked_count, "개:", state["locked_users"])                           # 잠긴 계정 수와 이름을 출력한다
print("결과별 건수:", counts)                                                            # 결과별 건수를 출력한다
print("티켓:", len(state["tickets"]), "건")                                              # 만든 티켓 수를 출력한다
print("건너뛴 액션과 이유:")                                                             # 건너뛴 액션을 모아 보여 주는 제목 줄
for entry in action_log:                                                                 # 기록을 하나씩 꺼낸다
    result_text = entry["result"]                                                        # 기록의 결과 문장
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 8. result_text 가 "건너뜀" 으로 시작하면 (if, startswith)
    # 9.   entry["incident"] · entry["action"] · "->" · result_text 를 출력한다 (print)
```

**순서**

1. **[터미널]** 파일 세 개를 만들고 붙여 넣습니다.
   ```bash
   pwd
   touch bulk_incidents.json safe_runner.py day02_4-1_run.py
   ls
   ```
2. **[VS Code]** `safe_runner.py` 1 ~ 7번, `day02_4-1_run.py` 8 · 9번을 씁니다. 막히면 아래 「4교시 한눈에」를 봅니다.
3. **[터미널]** 실행합니다(맥북은 `python3`).
   ```bash
   python day02_4-1_run.py
   ```
4. 출력은 네 단계와 건너뛴 이유입니다. 단계 1 은 2줄, 단계 2 는 1줄, 단계 3 은 14줄(「첫 번째 처리」 · 「두 번째 처리」 제목 2줄과 결과 10줄, 마지막의 잠긴 계정 · 티켓 2줄), 단계 4 는 알림 7건의 결과 7줄과 요약 3줄(잠긴 계정 · 결과별 건수 · 티켓)입니다. 마지막 `건너뛴 액션과 이유:` 아래는 건너뛴 액션만큼 줄이 나옵니다.
5. **[보고서]** `day02_am_report.md` 의 `## 4교시` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 단계 1 · 3 · 4 의 잠긴 계정과 티켓 수를 적어 주세요.
   - (나) 🔍 단계 1(어제 방식)에서는 `dami` 가 두 번 잠기고 티켓이 2건 생성되었는데, 단계 3(안전한 방식)에서는 1건입니다. 단계 3 의 「두 번째 처리」 줄을 근거로 어떤 안전장치가 두 번째 실행을 차단했는지 적어 주세요.
   - (다) 🔍 단계 4 에서 잠긴 계정 3개 가운데 `users_info.json` 의 `employed` 값으로 볼 때 잘못 잠긴 계정이 있는지 적고, 한도가 없을 때와 비교해 잘못 잠긴 계정이 몇 개 감소했는지 적어 주세요. 한도로 방지하지 못하는 문제가 무엇인지도 적어 주세요. 마지막으로, 2교시의 맥락(보강)과 3교시의 경로 분기 중 무엇을 적용하면 잘못 잠긴 계정을 줄일 수 있는지 적어 주세요.

## 4교시 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 두 조건이 모두 참이면 | `if action == "계정 잠금" and entity in state["locked_users"]:` |
| 리스트의 개수 | `len(state["locked_users"])` |
| 이상이면 | `>=` |
| 같지 않으면 | `if skip_reason != "":` |
| 다른 함수의 결과를 그대로 리턴 | `return run_action(action, incident, state)` |
| 글자가 어떤 말로 시작하면 | `if result_text.startswith("건너뜀"):` |

---

## 오늘 오전 마무리

| 확인 | 문제 |
|---|---|
| 알림 보강으로 재직 · VIP · 접속 IP 맥락을 추가했다 | 오전 2-1 |
| 맥락에 따라 승인 필요 · 오탐 종료 · 기본 경로로 분기하고 판정 사유를 기록했다 | 오전 3-1 |
| 중복 실행을 방지하고 1회 실행당 잠글 수 있는 계정 수를 제한했다 | 오전 4-1 |

오전에 구현한 보강 · 경로 분기 · 안전장치는 하나의 흐름으로 이어집니다. <mark>오후에는 두 가지를 구현합니다. 첫째, 3교시에서 `승인 필요` 경로로 분기된 알림을 담당자가 승인하거나 거절하는 승인 처리입니다. 둘째, 4교시의 실행기에서 액션이 실패했을 때의 실패 처리입니다. 그리고 보강 · 경로 분기 · 안전장치 적용 실행을 하나의 흐름으로 연결해 한 번에 실행합니다.</mark> 4교시 마지막에 확인한 「한도 안에서도 잘못 잠긴 계정」 문제는, 오후 하루 흐름에서 VIP 경로와 신뢰 IP 판단을 함께 적용하면 일부 감소합니다.

---

---

<!-- learn:answers -->


설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## 정답 2-1

💻 **터미널에 입력합니다.**

```bash
pwd
python day02_2-1_run.py
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

`day02_2-1_run.py` 의 7 ~ 9번입니다.

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
  - 신뢰 IP 라는 사실은 「IP 때문에 발생한 알림」이 정상이라는 근거가 되지만, `대량 다운로드` 는 IP 와 무관한 행위라서 신뢰 IP 가 정상이라는 근거가 되지 못합니다. IP 맥락이 같아도 <mark>동일하게 처리하면 안 됩니다.</mark> 이 차이는 3교시의 조건 분기에서 반영합니다.

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

## 정답 3-1

💻 **터미널에 입력합니다.**

```bash
pwd
python day02_3-1_run.py
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

`day02_3-1_run.py` 의 8 · 9번입니다.

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

## 정답 4-1

💻 **터미널에 입력합니다.**

```bash
pwd
python day02_4-1_run.py
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
    return run_action(action, incident, state)                                     # 이유가 없으면 어제의 방식대로 실행한 결과를 리턴한다
```

`day02_4-1_run.py` 의 8 · 9번입니다.

```python
    # 8. result_text 가 "건너뜀" 으로 시작하면 (if, startswith)
    if result_text.startswith("건너뜀"):                              # 결과 문장이 「건너뜀」으로 시작하면
    # 9.   entry["incident"] · entry["action"] · "->" · result_text 를 출력한다 (print)
        print(entry["incident"], entry["action"], "->", result_text)  # 인시던트 · 액션 · 이유를 출력한다
```

**결과**

- (가) 출력은 다음과 같습니다. 단계 1 의 잠긴 계정은 <mark style="background:#bde3ff">**`['dami', 'dami']`, 티켓 2건**</mark>, 단계 3 은 <mark style="background:#bde3ff">**`['dami']`, 티켓 1건**</mark>, 단계 4 는 <mark style="background:#bde3ff">**3개(`dami` · `seoyeon` · `gaeun`), 티켓 7건**</mark> 입니다.

```
--- 단계 1: 어제 방식(안전장치 없음)으로 같은 알림 5건을 두 번 처리
잠긴 계정: ['dami', 'dami']
티켓: 2 건
--- 단계 2: 어제 방식(안전장치 없음)으로 인사 오류 알림 7건 처리
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
  - 월요일 방식에는 이 확인이 없어서 두 번째 처리에서 `dami` 를 다시 잠그고 티켓을 또 만들었습니다.
- (다) 잠긴 3개 가운데 <mark style="background:#bde3ff">`seoyeon` 과 `gaeun` 은 `employed` 가 `true` 인 재직자라 잘못 잠긴 계정</mark>입니다. 실제 퇴사자는 `dami` 한 명입니다.
  - 한도가 없고 중복 방지만 있다면 서로 다른 계정 6개가 모두 잠깁니다. 이 가운데 실제 퇴사자는 `dami` 한 명이라 5명이 잘못 잠깁니다(`dami` 는 알림이 두 건이라도 한 번만 잠깁니다). 한도 3개로 잘못 잠긴 계정이 5명에서 2명으로 줄었습니다.
  - 한도가 방지하지 못하는 문제: 한도 안에서는 잘못된 알림도 그대로 실행됩니다. 한도는 영향 범위(잠기는 계정 수)를 제한할 뿐, 잘못된 알림을 식별하지는 못합니다.
  - 줄이는 방법: 2교시에서 보강한 `employed` 맥락을 잠금 실행 전에 점검하면 `seoyeon` 과 `gaeun` 은 재직 중이라 잠금 대상에서 제외됩니다. `gaeun` 은 VIP 계정이라 3교시의 `승인 필요` 경로에서도 자동 잠금 대상에서 제외됩니다. 오후 6교시 하루 흐름은 이 가운데 VIP 경로와 신뢰 IP 오탐 판단을 하나의 흐름으로 연결합니다(재직 여부 점검은 연결하지 않습니다).
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
