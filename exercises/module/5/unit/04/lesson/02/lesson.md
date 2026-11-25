---
id: m5-u04-l02
title: 실습 4-1 · 위험 점수로 조치 요청 분류하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/130_day05_am_report_gate.md
  mission_id: GichanSource.m5-1113-am-report-gate
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 4-1 · 위험 점수로 조치 요청 분류하기

## 목표: 위험 점수 승인 게이트

> **오늘 들어온 일**
>
> - **상황**: <mark style="background:#e0d4ff">Unit 1 실습 1-1 에서는 플레이북</mark>(playbook, 플레이북: 사건 종류별로 미리 정한 대응 순서)마다 승인 값을 하나(`자동` 또는 `담당자 승인 필요`)씩 정했습니다. <mark style="background:#e0d4ff">M5 Unit 1 응용 1-1에서 만든 `routing.py`</mark> 에는 「VIP(브이아이피: 막히면 업무에 큰 영향을 주는 중요한 계정) 이면 승인 필요」가 `decide_route` 함수 안의 조건문으로 들어 있습니다. 이 방식은 승인 여부를 정하는 규칙이 코드 안에 있어서, 규칙을 바꾸려면 코드를 고쳐야 합니다. 오늘은 자동 대응이 실행하려는 조치 요청 8건이 들어왔습니다.
> - **문제**: 같은 계정 잠금이라도 위험이 다릅니다. 퇴사자 한 명(`REQ-1` `dami`)을 잠그는 것과 계정 6개를 한꺼번에 잠그는 것(`REQ-6`)은 잘못 실행했을 때 업무에 미치는 피해의 범위(영향 범위)가 다릅니다. <mark style="background:#ffc4d6">그런데 승인 값은 플레이북 하나에 하나뿐이어서 요청마다 위험에 맞게 다르게 정할 수 없습니다.</mark> 또 「공유 IP(여러 계정이 함께 쓰는 IP)도 승인을 받자」처럼 기준을 바꾸려면 코드를 수정해야 합니다.
> - **부탁**: 승인 기준을 설정 파일 `config/approval_policy.json` 에 따로 두어 주세요. 그리고 요청마다 위험 점수를 더해 「자동 · 승인 필요 · 차단 금지」 가운데 하나로 나눠 주세요. 허용 목록(allowlist, 얼라우리스트: 차단 대상에서 제외하기로 미리 정한 IP 의 목록) 대상은 <mark style="background:#ffc4d6">점수와 상관없이 차단 금지</mark>입니다.
> - **바뀌는 점**: 8건이 <mark style="background:#bde3ff">자동 3건 · 승인 필요 3건 · 차단 금지 2건</mark>으로 분류되고, 결정마다 점수를 합산한 근거가 함께 출력됩니다. 상황과 숫자는 설명을 위한 예시입니다.

## 2.1 승인 게이트의 판단 순서

**승인 게이트**(approval gate, 어프루벌 게이트: 자동 대응이 조치를 실행하기 직전에, 바로 실행할지 사람의 승인을 받을지 정하는 단계)는 사람 개입 방식(human-in-the-loop, 휴먼 인 더 루프: 자동화 흐름 중간에 사람이 판단하고 승인하는 방식)을 실제로 적용하는 지점입니다. 위험이 낮은 조치는 자동으로 실행하고, 위험이 큰 조치만 사람에게 승인을 요청합니다. 판단 순서는 아래와 같습니다.

| 순서 | 확인 | 결과 |
|---|---|---|
| 1 | 대상이 허용 목록(`allowlist_ips`)에 있는가 | 있으면 점수를 보지 않고 **차단 금지** |
| 2 | 위험 점수를 합산한다 | 아래 「합산하는 점수」 표의 점수를 더한다 |
| 3 | 점수가 임계값 <mark style="background:#ffdcb0">`approval_score`(3) 이상</mark>인가 | 이상이면 **승인 필요**, 아니면 **자동** |

임계값(threshold, 쓰레숄드)은 판정이 바뀌는 기준 점수입니다.

**합산하는 점수**

| 항목 | 점수 |
|---|---|
| 등급 | <mark style="background:#ffdcb0">high 2점 · mid 1점 · low 0점</mark> |
| VIP 계정 | <mark style="background:#ffdcb0">3점</mark> |
| 함께 쓰는 IP(공유 IP) | <mark style="background:#ffdcb0">2점</mark> |
| 대상 4개 이상 | <mark style="background:#ffdcb0">2점</mark> |

두 기준은 비교 방법이 다릅니다. 대상 수는 3을 **넘을 때**(`>`, 4개부터), 공유 IP 는 계정이 2 **이상**일 때(`>=`, 2개부터) 점수를 더합니다.

- 허용 목록(allowlist)은 차단 대상에서 제외하기로 미리 정해 둔 IP 의 목록입니다. 오늘은 협력사 사무실 IP `203.0.113.80` 과 점검 서버 `192.0.2.10` 이 있습니다.
- <mark>허용 목록을 점수보다 먼저 판단합니다.</mark> 차단하면 업무가 중단되는 IP 는 위험 점수와 무관하게 차단하지 않는 것이 원칙이기 때문입니다.
- 공유 IP(함께 쓰는 IP, shared IP)는 그 IP 를 쓰는 계정이 <mark style="background:#ffdcb0">2개 이상(`shared_ip_limit`)</mark>인 경우입니다. <mark style="background:#e0d4ff">Unit 2 파일 `ip_actions.py` 가 「여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요」로 처리하던 규칙</mark>을 점수로 바꾼 것입니다.
- 대상 수는 요청 하나가 한꺼번에 조치하는 대상(계정 또는 IP)의 수이고, 잘못 실행했을 때 영향이 미치는 범위(영향 범위)를 나타냅니다. <mark style="background:#e0d4ff">M5 Unit 1 응용 1-2의 `safe_runner.py`는 한 번에 3개를 넘게 잠그지 못하도록 막았습니다.</mark> 오늘은 차단하는 대신, <mark style="background:#ffdcb0">3개를 넘으면 위험 점수 2점을 더해</mark> 사람이 승인하게 바꿨습니다.
- 점수와 기준은 모두 `config/approval_policy.json` 에 있습니다. 코드에는 점수를 더하는 계산만 쓰고, <mark>더할 점수 값은 설정 파일에 따로 둡니다</mark>. 그래서 정책을 바꿀 때 코드를 수정하지 않고 설정 파일만 바꾸면 됩니다.

업계에서 자동 조치와 승인 필요 조치를 나눌 때는 <mark>가역성 · 영향 범위 · 확실성</mark> 세 가지를 봅니다.

| 기준 | 뜻 | 오늘의 위험 점수에서 |
|---|---|---|
| 가역성(reversibility) | 조치를 되돌릴 수 있는 정도 | 점수에 넣지 않음 |
| 영향 범위 | 조치가 미치는 계정 · IP 의 범위 | VIP 계정 · 공유 IP · 대상 수 |
| 확실성 | 탐지가 진짜 공격일 가능성이 얼마나 확실한지 | 허용 목록 확인: 정상임이 확실한 대상은 차단 금지 |

탐지 등급은 사건의 심각도로 점수에 더합니다. 계정 잠금과 IP 차단은 Unit 3 실습 3-1 에서 되돌리기(롤백)를 만들었습니다. 되돌릴 수 없는 세션 종료는 이 Unit 의 응용 4-4(선택) 리스크 평가에서 다룹니다. 그래서 세션 종료 요청 `REQ-7`(`hana`)이 단계 2 에서 「자동」으로 나와도 잘못된 것이 아닙니다. 오늘 위험 점수에 가역성이 들어 있지 않기 때문입니다.

함수 세 개와 실행 파일은 대부분 미리 채워 두었습니다. 직접 쓰는 곳은 `decide_gate` 의 마지막 기준 검사 **두 줄**(① · ②)입니다.

```
approval_gate.py   is_allowlisted  : 대상이 허용 목록에 있는지 리턴한다 (미리 채움)
                   risk_score      : 등급 · VIP · 함께 쓰는 IP · 대상 수 점수를 더한다 (미리 채움)
                   decide_gate     : 허용 목록이면 차단 금지, 점수를 받아 (미리 채움), 기준 이상이면 (①) 승인 필요 (②)
실행 파일          exercise4-1_run.py : 요청마다 결정을 받아 결정별로 센다 (미리 채움)
```

#### 문법 상자 · 직접 쓰는 곳의 모양 (예시 값 · 읽기만 합니다)

```python
score = 4                                  # 예시 값
if score >= 3:                             # 「이상」은 >= 로 묻는다. 끝에 : 를 붙인다
    print("기준 이상")                     # if 안쪽 줄은 4칸 더 들여 쓴다

def pick(score):                           # 예시 함수
    return "높음", ["합계 " + str(score)]  # 두 값을 쉼표로 이어 함께 리턴한다
```

- `>=` 는 「크거나 같으면」입니다. 기준과 같은 3점도 승인 필요에 들어가야 하므로 `>` 가 아니라 `>=` 를 씁니다.
- `return 값1, 값2` 는 두 값을 함께 돌려줍니다. 실행 파일은 `decision, reasons = decide_gate(…)` 로 나눠 받습니다.

## 실습 4-1 · 위험 점수로 조치 요청 분류하기

**이런 상황이 있습니다**

- **지금은**: <mark>승인이 필요한지는 플레이북마다 정한 값 하나로만 정해지고, 기준이 코드 안에 있습니다</mark>.
- **만드는 것**: 허용 목록 확인 · 위험 점수 · 결정(`approval_gate.py`), 요청마다 결정하고 세기(`exercise4-1_run.py`).
- **실행하면**: <mark>단계 1: 불러온 요청 수와 기준 점수, 단계 2: 요청마다 결정과 이유, 단계 3: 결정별 요청 수, 단계 4: 담당자에게 보낼 승인 요청, 단계 5: 저장한 결정 수가 나옵니다.</mark>

**할 일**

1. `soar_response` 폴더에 데이터 파일 두 개(`config/approval_policy.json` · `gate_requests.json`)와 코드 파일 두 개(`approval_gate.py` · `exercise4-1_run.py`)를 만들어 붙여 넣습니다.
2. 채우기 <mark>전에</mark> 한 번 실행해 봅니다.
3. `approval_gate.py` 에서 `# ←` 가 있는 <mark>두 곳</mark>(① · ②)을 한 줄씩 채우고 다시 실행해 단계 2 ~ 4 를 읽습니다.

**`config/approval_policy.json`** — 승인 게이트의 기준입니다. 점수 값은 위 2.1 표와 같습니다. 코드는 이 파일의 키 이름으로 읽습니다.

<pre class="copyable"><code>{
  "allowlist_ips": ["203.0.113.80", "192.0.2.10"],
  "vip_accounts": ["gaeun"],
  "grade_points": {"high": 2, "mid": 1, "low": 0},
  "vip_points": 3,
  "shared_ip_points": 2,
  "shared_ip_limit": 2,
  "many_targets_points": 2,
  "many_targets_limit": 3,
  "approval_score": 3
}
</code></pre>

**`gate_requests.json`** — 오늘 자동 대응이 실행하려는 조치 요청 8건입니다. `users_on_ip` 는 그 IP 를 쓰는 계정 수(계정 조치면 0), `target_count` 는 요청 하나가 한꺼번에 조치하는 대상 수입니다. `REQ-6` 처럼 `target` 에는 대표 계정 하나(`minsu`)만 적고, 실제로는 `target_count` 만큼(6개) 잠그는 요청도 있습니다.

<pre class="copyable"><code>[
  {"id": "REQ-1", "incident": "INC-311", "action": "계정 잠금", "target": "dami", "grade": "high", "users_on_ip": 0, "target_count": 1},
  {"id": "REQ-2", "incident": "INC-312", "action": "계정 잠금", "target": "gaeun", "grade": "mid", "users_on_ip": 0, "target_count": 1},
  {"id": "REQ-3", "incident": "INC-313", "action": "IP 차단", "target": "203.0.113.80", "grade": "high", "users_on_ip": 4, "target_count": 1},
  {"id": "REQ-4", "incident": "INC-314", "action": "IP 차단", "target": "198.51.100.45", "grade": "low", "users_on_ip": 0, "target_count": 1},
  {"id": "REQ-5", "incident": "INC-315", "action": "IP 차단", "target": "198.51.100.77", "grade": "mid", "users_on_ip": 3, "target_count": 1},
  {"id": "REQ-6", "incident": "INC-316", "action": "계정 잠금", "target": "minsu", "grade": "high", "users_on_ip": 0, "target_count": 6},
  {"id": "REQ-7", "incident": "INC-317", "action": "세션 종료", "target": "hana", "grade": "mid", "users_on_ip": 0, "target_count": 1},
  {"id": "REQ-8", "incident": "INC-318", "action": "IP 차단", "target": "192.0.2.10", "grade": "low", "users_on_ip": 1, "target_count": 1}
]
</code></pre>

**`approval_gate.py`** — 승인 게이트 함수 모음입니다. Unit 5 와 응용 4-5 도 가져와 사용(import)합니다. 직접 쓰는 곳은 `decide_gate` 의 ① · ② 두 줄이고, 나머지는 미리 채운 줄입니다.

- 미리 채운 줄의 `str(score)` 는 숫자를 문자열(글자로 된 값)로 바꿉니다. 숫자는 `+` 로 문자열과 바로 이어 붙일 수 없어서 먼저 바꿉니다.

```python
def is_allowlisted(request, policy):                                        # 조치 요청 한 건과 승인 정책을 받는 함수
    """조치 대상이 허용 목록에 있으면 True, 없으면 False 를 리턴한다.
    협력사 사무실이나 점검 서버처럼 지금 정책에서 차단하지 않기로 등록한 대상을 먼저 가려낼 때 쓴다.
    """
    return request["target"] in policy["allowlist_ips"]                     # 대상이 허용 목록에 있는지의 결과를 리턴한다 — 미리 채운 줄


def risk_score(request, policy):                                            # 조치 요청 한 건과 승인 정책을 받는 함수
    """등급 · VIP · 함께 쓰는 IP · 대상 수로 위험 점수를 더하고, 점수와 이유 리스트를 함께 리턴한다.
    자동으로 실행해도 되는 요청인지 숫자로 판단할 때 쓴다.
    """
    grade_table = policy["grade_points"]                                    # 등급마다 정한 점수 표 — 미리 채운 줄
    score = grade_table[request["grade"]]                                   # 이 요청 등급의 점수로 시작한다 — 미리 채운 줄
    reasons = ["등급 " + request["grade"] + " +" + str(score)]              # 점수를 더한 이유 리스트 — 미리 채운 줄
    if request["target"] in policy["vip_accounts"]:                         # 대상이 VIP 계정이면 — 미리 채운 줄
        score = score + policy["vip_points"]                                # VIP 점수를 더한다 — 미리 채운 줄
        reasons.append("VIP 계정 +" + str(policy["vip_points"]))            # 이유를 추가한다 — 미리 채운 줄
    if request["users_on_ip"] >= policy["shared_ip_limit"]:                 # 여러 계정이 함께 쓰는 IP 이면 — 미리 채운 줄
        score = score + policy["shared_ip_points"]                          # 함께 쓰는 IP 점수를 더한다 — 미리 채운 줄
        reasons.append("함께 쓰는 IP +" + str(policy["shared_ip_points"]))  # 이유를 추가한다 — 미리 채운 줄
    if request["target_count"] > policy["many_targets_limit"]:              # 한 번에 조치할 대상이 많으면 — 미리 채운 줄
        score = score + policy["many_targets_points"]                       # 대상 수 점수를 더한다 — 미리 채운 줄
        reasons.append("대상 " + str(request["target_count"]) + "개 +" + str(policy["many_targets_points"]))  # 이유를 추가한다 — 미리 채운 줄
    return score, reasons                                                   # 점수와 이유 리스트를 함께 리턴한다 — 미리 채운 줄


def decide_gate(request, policy):                                           # 조치 요청 한 건과 승인 정책을 받는 함수
    """조치 요청 한 건을 「차단 금지」 · 「승인 필요」 · 「자동」 가운데 하나로 정하고, 결정과 이유 리스트를 함께 리턴한다.
    자동 대응이 조치를 실행하기 직전에, 사람의 승인이 필요한지 정할 때 쓴다.
    """
    if is_allowlisted(request, policy):                                     # 허용 목록 대상이면 — 미리 채운 줄
        return "차단 금지", ["허용 목록 대상"]                              # 결정과 이유를 함께 리턴한다 — 미리 채운 줄
    score, reasons = risk_score(request, policy)                            # 위험 점수와 이유 리스트를 함께 받는다 — 미리 채운 줄
    reasons.append("합계 " + str(score) + "점")                             # 합계 점수를 이유에 추가한다 — 미리 채운 줄
    # ① score 가 policy["approval_score"] 이상이면 (if, >=)   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    # ② "승인 필요" 와 reasons 를 함께 리턴한다   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)

    return "자동", reasons                                                  # 기준보다 낮으면 자동으로 실행한다 — 미리 채운 줄
```

**`exercise4-1_run.py`** — 직접 쓰는 줄이 없습니다. 그대로 붙여 넣습니다. 단계 3 의 `for decision in counts:` 처럼 딕셔너리를 `for` 로 돌리면 키(여기서는 결정 이름)가 하나씩 나옵니다.

```python
from incident import load_json, save_json                           # Unit 1 파일의 JSON 읽기 · 쓰기 함수를 불러온다
from approval_gate import decide_gate                               # 방금 만든 승인 게이트 함수를 불러온다

policy = load_json("config/approval_policy.json")                   # 승인 정책 파일을 딕셔너리로 읽는다
requests = load_json("gate_requests.json")                          # 오늘 들어온 조치 요청 파일을 리스트로 읽는다
print("--- 단계 1: 불러온 조치 요청", len(requests), "건 · 승인 기준", policy["approval_score"], "점")  # 단계 1 시작을 알리는 줄

counts = {"자동": 0, "승인 필요": 0, "차단 금지": 0}                # 결정마다 요청 수 : 처음에는 모두 0
results = []                                                        # 요청마다 결정을 저장할 빈 리스트
print("--- 단계 2: 요청마다 결정과 이유")                           # 단계 2 시작을 알리는 줄
for request in requests:                                            # 조치 요청을 하나씩 읽는다
    decision, reasons = decide_gate(request, policy)                # 결정과 이유 리스트를 함께 받는다
    counts[decision] = counts[decision] + 1                         # 이 결정의 요청 수를 1 늘린다
    reason_text = ", ".join(reasons)                                # 이유 리스트를 쉼표로 이어 한 문자열로 만든다
    print(request["id"], request["action"], request["target"], "→", decision, "·", reason_text)  # 요청과 결정을 출력한다
    results.append({"id": request["id"], "incident": request["incident"], "action": request["action"], "target": request["target"], "decision": decision})  # 결정을 추가한다

print("--- 단계 3: 결정별 요청 수")                                 # 단계 3 시작을 알리는 줄
for decision in counts:                                             # 결정 이름을 하나씩 읽는다
    print(decision, ":", counts[decision], "건")                    # 결정과 요청 수를 출력한다

print("--- 단계 4: 담당자에게 보낼 승인 요청")                      # 단계 4 시작을 알리는 줄
for result in results:                                              # 결정을 하나씩 읽는다
    if result["decision"] == "승인 필요":                           # 사람의 승인이 필요하면
        print(result["id"], result["incident"], result["action"], result["target"], "→ 담당자 승인을 기다림")  # 승인 요청을 출력한다

save_json(results, "gate_results.json")                             # 결정 리스트를 파일에 저장한다
print("--- 단계 5: gate_results.json 에", len(results), "건 저장")  # 단계 5 시작을 알리는 줄과 저장한 수
```

- 주석 줄은 그대로 두고, **각 주석 바로 아래 줄**에 씁니다. ① 은 `if` 줄이라 4칸, ② 는 그 `if` 안쪽의 `return` 줄이라 8칸에서 시작합니다.
- 바로 위의 미리 채운 `if is_allowlisted(request, policy):` 와 그 아래 `return "차단 금지", …` 가 ① · ② 와 같은 모양입니다.

**직접 쓰는 곳**

| 빈칸 | 쓰는 줄 | 들여쓰기 |
|---|---|---|
| ① | `score` 가 기준 이상이면 (`if`, `>=`) | 4칸 |
| ② | 「승인 필요」와 `reasons` 를 리턴 (`return`) | 8칸 |

- ① 확인: ① 만 쓰고 실행하면 `IndentationError: expected an indented block after 'if' statement` 가 나옵니다. ② 를 아직 안 써서 나는 오류이니 정상입니다. 막히면: 문법 상자의 `if score >= 3:` 에서 `3` 자리에 `policy["approval_score"]` 를 넣습니다. `3` 을 직접 쓰면 지금 출력은 같아도, 설정 파일의 기준을 바꿨을 때 반영되지 않습니다.
- ② 확인: ② 까지 쓰고 실행하면 `REQ-2 계정 잠금 gaeun → 승인 필요 · 등급 mid +1, VIP 계정 +3, 합계 4점` 이 나오면 성공입니다. 막히면: 맨 아래 미리 채운 `return "자동", reasons` 와 같은 모양이고 `"자동"` 만 `"승인 필요"` 로 바뀝니다.
- 채우기 전에 실행해도 오류 없이 돌아갑니다. 다만 허용 목록 대상 두 건 말고는 모두 「자동」이라 단계 3 이 `자동 : 6 건` · `승인 필요 : 0 건` 이고, 단계 4 에는 줄이 하나도 없습니다. VIP 계정 잠금(`REQ-2`)과 계정 6개 잠금(`REQ-6`)도 사람의 승인 없이 실행된다는 것을 보여 주는 결과입니다.

**순서**

핵심 실습 결과를 기록할 `report_u4.md` 가 아직 없으면 [「핵심 실습 결과 기록 준비」 레슨](__SITE__/exercises/module/5/unit/4/lesson/11/page/1)에서 먼저 만듭니다.

1. **[터미널]** `config` 폴더가 없으면 만듭니다.
   ```bash
   pwd
   mkdir -p config
   ls
   ```
   - 명령 풀이: `mkdir -p config` 는 `config` 폴더가 없을 때만 만듭니다(이미 있으면 그대로 둡니다).
   - **[VS Code]** 파일 네 개를 만듭니다. `soar_response` 폴더 안의 `config` 폴더를 오른쪽 클릭 › **New File** 로 `approval_policy.json` 을, `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `gate_requests.json` · `approval_gate.py` · `exercise4-1_run.py` 를 만들고, 각각 코드 상자의 내용을 붙여 넣고 저장합니다.

<!-- checklist -->
- [ ] `soar_response` 폴더 안의 `config` 폴더에 `approval_policy.json` 을, `soar_response` 폴더에 `gate_requests.json` 을 만들고 붙여 넣은 뒤 저장했다
- [ ] `soar_response` 폴더에 `approval_gate.py` · `exercise4-1_run.py` 를 만들고 붙여 넣은 뒤 저장했다
<!-- /checklist -->

2. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고, **채우기 전에** 한 번 실행합니다. 단계 3 이 `승인 필요 : 0 건` 인지 봅니다.
   ```bash
   python exercise4-1_run.py
   ```
3. **[VS Code]** `approval_gate.py` 의 `# ←` 두 곳(① · ②)을 채웁니다. 2.1 의 판단 순서 표 3번 줄을 보고 씁니다.

<!-- checklist -->
- [ ] `approval_gate.py` 의 빈칸 ① · ② 를 채우고 저장했다
<!-- /checklist -->

4. **[터미널]** 다시 실행합니다.
   ```bash
   python exercise4-1_run.py
   ```
5. 출력은 다섯 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 과 단계 5 는 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 8줄, 단계 3 은 3줄, 단계 4 는 3줄입니다.

<!-- checklist -->
- [ ] `python exercise4-1_run.py` 를 다시 실행해 단계 3 이 `자동 : 3 건` · `승인 필요 : 3 건` · `차단 금지 : 2 건` 으로 나왔다
<!-- /checklist -->

6. **[실습 결과 기록]** `report_u4.md` 의 「실습 4-1 · 조치 요청 분류」에 실행 출력과 결정별 요청 수, 승인 기준 파일을 기록합니다. 틀이 없으면 「핵심 실습 결과 기록 준비」 레슨을 엽니다.

<!-- answer: 10|실습 4-1 정답 -->

**확인** — 단계 3 이 `자동 : 3 건` · `승인 필요 : 3 건` · `차단 금지 : 2 건` 이고, 단계 4 에 `REQ-2` · `REQ-5` · `REQ-6` 세 줄이 나오면 성공입니다. 출력이 다르면 이 실습 바로 아래의 정답 펼침과 비교합니다.

## 실습 4-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 리스트 안에 있는지의 결과 리턴 | `return request["target"] in policy["allowlist_ips"]` |
| 딕셔너리에서 값을 읽어 변수에 저장하기 | `score = grade_table[request["grade"]]` |
| 리스트 안에 있으면 | `if request["target"] in policy["vip_accounts"]:` |
| 더해서 다시 저장하기 | `score = score + policy["vip_points"]` |
| 함수 결과가 참이면 | `if is_allowlisted(request, policy):` |
| 두 결과를 함께 받기 | `score, reasons = risk_score(request, policy)` |
| 기준 이상이면 | `if score >= policy["approval_score"]:` |
| 1 늘려 다시 저장하기 | `counts[decision] = counts[decision] + 1` |

---
