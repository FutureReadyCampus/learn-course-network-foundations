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
> - **상황**: <mark style="background:#e0d4ff">Unit 1에서는 플레이북</mark>(playbook, 플레이북: 사건 종류별로 미리 정한 대응 순서)마다 승인 값을 하나(`자동` 또는 `담당자 승인 필요`)씩 정했습니다. <mark style="background:#e0d4ff">Unit 1에서는</mark> 「VIP(브이아이피: 막히면 업무에 큰 영향을 주는 중요한 계정) 이면 승인 필요」를 `decide_route` 함수 안의 조건문으로 작성했습니다. 이 방식은 승인 여부를 정하는 규칙이 코드 안에 있어서, 규칙을 바꾸려면 코드를 고쳐야 합니다. Unit 4에서는 자동 대응이 실행하려는 조치 요청 8건이 들어왔습니다.
> - **문제**: 같은 계정 잠금이라도 위험이 다릅니다. 퇴사자 한 명(`REQ-1` `dami`)을 잠그는 것과 계정 6개를 한꺼번에 잠그는 것(`REQ-6`)은 잘못 실행했을 때 업무에 미치는 피해의 범위(영향 범위)가 다릅니다. <mark style="background:#ffc4d6">그런데 승인 값은 플레이북 하나에 하나뿐이어서 요청마다 위험에 맞게 다르게 정할 수 없습니다.</mark> 또 「공유 IP(여러 계정이 함께 쓰는 IP)도 승인을 받자」처럼 기준을 바꾸려면 코드를 수정해야 합니다.
> - **부탁**: 승인 기준을 설정 파일 `config/approval_policy.json` 에 따로 두어 주세요. 그리고 요청마다 위험 점수를 더해 「자동 · 승인 필요 · 차단 금지」 가운데 하나로 나눠 주세요. 허용 목록(allowlist, 얼라우리스트: 차단 대상에서 제외하기로 미리 정한 IP 의 목록) 대상은 <mark style="background:#ffc4d6">점수와 상관없이 차단 금지</mark>입니다.
> - **바뀌는 점**: 8건이 <mark style="background:#bde3ff">자동 3건 · 승인 필요 3건 · 차단 금지 2건</mark>으로 분류되고, 결정마다 점수를 합산한 근거가 함께 출력됩니다. 상황과 숫자는 설명을 위한 예시입니다.

## 2.1 승인 게이트의 판단 순서

**승인 게이트**(approval gate, 어프루벌 게이트: 자동 대응이 조치를 실행하기 직전에, 바로 실행할지 사람의 승인을 받을지 정하는 단계)는 사람 개입 방식(human-in-the-loop, 휴먼 인 더 루프: 자동화 흐름 중간에 사람이 판단하고 승인하는 방식)을 실제로 적용하는 지점입니다. 위험이 낮은 조치는 자동으로 실행하고, 위험이 큰 조치만 사람에게 승인을 요청합니다. 판단 순서는 아래와 같습니다.

| 순서 | 확인 | 결과 |
|---|---|---|
| 1 | 대상이 허용 목록(`allowlist_ips`)에 있는가 | 있으면 점수를 보지 않고 **차단 금지** |
| 2 | 위험 점수를 합산한다 | 합산하는 점수: <mark style="background:#ffdcb0">등급(high 2점 · mid 1점 · low 0점), VIP 계정 3점, 함께 쓰는 IP(공유 IP) 2점, 대상 4개 이상 2점</mark> |
| 3 | 점수가 임계값(threshold, 쓰레숄드: 판정이 바뀌는 기준 점수) <mark style="background:#ffdcb0">`approval_score`(3) 이상</mark>인가 | 이상이면 **승인 필요**, 아니면 **자동** |

- 허용 목록(allowlist)은 차단 대상에서 제외하기로 미리 정해 둔 IP 의 목록입니다. 오늘은 협력사 사무실 IP `203.0.113.80` 과 점검 서버 `192.0.2.10` 이 있습니다.
- <mark>허용 목록을 점수보다 먼저 판단합니다.</mark> 차단하면 업무가 중단되는 IP 는 위험 점수와 무관하게 차단하지 않는 것이 원칙이기 때문입니다.
- 공유 IP(함께 쓰는 IP, shared IP)는 그 IP 를 쓰는 계정이 <mark style="background:#ffdcb0">2개 이상(`shared_ip_limit`)</mark>인 경우입니다. <mark style="background:#e0d4ff">Unit 2에서 「여러 계정이 함께 쓰는 IP 라서 담당자 승인 필요」로 처리하던 규칙</mark>을 점수로 바꾼 것입니다.
- 대상 수는 요청 하나가 한꺼번에 조치하는 대상(계정 또는 IP)의 수이고, 잘못 실행했을 때 영향이 미치는 범위(영향 범위)를 나타냅니다. <mark style="background:#e0d4ff">Unit 1의 도전 1-2에서는 한 번에 3개를 넘게 잠그지 못하도록 차단했습니다.</mark> 오늘은 차단하는 대신, <mark style="background:#ffdcb0">3개를 넘으면 위험 점수 2점을 더해</mark> 사람이 승인하게 바꿨습니다.
- 업계에서 자동 조치와 승인 필요 조치를 나눌 때는 <mark>가역성 · 영향 범위 · 확실성</mark> 세 가지를 봅니다.
  - 가역성(reversibility)은 조치를 되돌릴 수 있는 정도입니다.
  - 영향 범위는 조치가 미치는 계정 · IP 의 범위입니다.
  - 확실성은 탐지가 진짜 공격일 가능성이 얼마나 확실한지입니다.

  오늘의 위험 점수는 영향 범위를 VIP 계정 · 공유 IP · 대상 수로 나타냅니다. 확실성은 허용 목록 확인으로 나타내서, 정상임이 확실한 대상은 차단 금지로 둡니다. 탐지 등급은 사건의 심각도로 점수에 더합니다. 가역성은 점수에 넣지 않았습니다. 계정 잠금과 IP 차단은 Unit 3에서 되돌리기(롤백)를 만들었습니다. 되돌릴 수 없는 세션 종료는 Unit 4의 도전 4-4 리스크 평가에서 다룹니다.
- 점수와 기준은 모두 `config/approval_policy.json` 에 있습니다. 코드에는 점수를 더하는 계산만 쓰고, <mark>더할 점수 값은 설정 파일에 따로 둡니다</mark>. 그래서 정책을 바꿀 때 코드를 수정하지 않고 설정 파일만 바꾸면 됩니다.

함수 세 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
approval_gate.py   is_allowlisted  : 대상이 허용 목록에 있는지 리턴한다 (1번)
                   risk_score      : 등급 점수로 시작해 (2번), VIP 이면 (3번) 점수를 더한다 (4번). 함께 쓰는 IP · 대상 수는 미리 채움
                   decide_gate     : 허용 목록이면 차단 금지 (5번), 점수를 받아 (6번), 기준 이상이면 승인 필요 (7번)
실행 파일          exercise4-1_run.py : 요청마다 결정을 받아 (8번) 결정별로 센다 (9번)
```

## 실습 4-1 · 위험 점수로 조치 요청 분류하기

**이런 상황이 있습니다**

- **지금은**: <mark>승인이 필요한지는 플레이북마다 정한 값 하나로만 정해지고, 기준이 코드 안에 있습니다</mark>.
- **만드는 것**: 허용 목록 확인 · 위험 점수 · 결정(`approval_gate.py`), 요청마다 결정하고 세기(`exercise4-1_run.py`).
- **실행하면**: <mark>단계 1: 불러온 요청 수와 기준 점수, 단계 2: 요청마다 결정과 이유, 단계 3: 결정별 요청 수, 단계 4: 담당자에게 보낼 승인 요청, 단계 5: 저장한 결정 수가 나옵니다.</mark>

**할 일**: 데이터 파일 두 개와 코드 파일 두 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 2 ~ 4 를 읽습니다.

**`config/approval_policy.json`** — 승인 게이트의 기준입니다. 점수 값은 위 2.1 표와 같습니다. 코드는 이 파일의 키 이름으로 읽습니다.

```
{
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
```

**`gate_requests.json`** — Unit 4에서 자동 대응이 실행하려는 조치 요청 8건입니다. `users_on_ip` 는 그 IP 를 쓰는 계정 수(계정 조치면 0), `target_count` 는 요청 하나가 한꺼번에 조치하는 대상 수입니다.

```
[
  {"id": "REQ-1", "incident": "INC-311", "action": "계정 잠금", "target": "dami", "grade": "high", "users_on_ip": 0, "target_count": 1},
  {"id": "REQ-2", "incident": "INC-312", "action": "계정 잠금", "target": "gaeun", "grade": "mid", "users_on_ip": 0, "target_count": 1},
  {"id": "REQ-3", "incident": "INC-313", "action": "IP 차단", "target": "203.0.113.80", "grade": "high", "users_on_ip": 4, "target_count": 1},
  {"id": "REQ-4", "incident": "INC-314", "action": "IP 차단", "target": "198.51.100.45", "grade": "low", "users_on_ip": 0, "target_count": 1},
  {"id": "REQ-5", "incident": "INC-315", "action": "IP 차단", "target": "198.51.100.77", "grade": "mid", "users_on_ip": 3, "target_count": 1},
  {"id": "REQ-6", "incident": "INC-316", "action": "계정 잠금", "target": "minsu", "grade": "high", "users_on_ip": 0, "target_count": 6},
  {"id": "REQ-7", "incident": "INC-317", "action": "세션 종료", "target": "hana", "grade": "mid", "users_on_ip": 0, "target_count": 1},
  {"id": "REQ-8", "incident": "INC-318", "action": "IP 차단", "target": "192.0.2.10", "grade": "low", "users_on_ip": 1, "target_count": 1}
]
```

**`approval_gate.py`** — 승인 게이트 함수 모음입니다. 도전 4-5도 가져와 사용(import)합니다. 직접 쓰는 곳은 1 ~ 7번입니다.

- 3번 아래에는 `if` 한 줄을 씁니다. 그 아래 미리 채운 `reasons.append(…)` 줄은 4번과 함께 `if` 안쪽입니다.
- 5번과 7번도 `if` 한 줄만 씁니다. 그 아래 미리 채운 `return` 줄이 `if` 안쪽입니다.

```python
def is_allowlisted(request, policy):                                        # 조치 요청 한 건과 승인 정책을 받는 함수
    """조치 대상이 허용 목록에 있으면 True, 없으면 False 를 리턴한다.
    협력사 사무실이나 점검 서버처럼 지금 정책에서 차단하지 않기로 등록한 대상을 먼저 가려낼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. request["target"] 이 policy["allowlist_ips"] 안에 있는지(in)의 결과를 리턴한다


def risk_score(request, policy):                                            # 조치 요청 한 건과 승인 정책을 받는 함수
    """등급 · VIP · 함께 쓰는 IP · 대상 수로 위험 점수를 더하고, 점수와 이유 리스트를 함께 리턴한다.
    자동으로 실행해도 되는 요청인지 숫자로 판단할 때 쓴다.
    """
    grade_table = policy["grade_points"]                                    # 등급마다 정한 점수 표 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. grade_table[request["grade"]] 를 score 에 저장한다 (등급 점수로 시작한다)
    reasons = ["등급 " + request["grade"] + " +" + str(score)]              # 점수를 더한 이유 리스트 — 미리 채운 줄
    # 3. request["target"] 이 policy["vip_accounts"] 안에 있으면 (if, in)
        # 4. score 에 score + policy["vip_points"] 를 저장한다 (VIP 점수를 더한다)
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
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. is_allowlisted(request, policy) 가 참이면 (if)
        return "차단 금지", ["허용 목록 대상"]                              # 결정과 이유를 함께 리턴한다 — 미리 채운 줄
    # 6. risk_score(request, policy) 의 두 결과를 score, reasons 에 저장한다
    reasons.append("합계 " + str(score) + "점")                             # 합계 점수를 이유에 추가한다 — 미리 채운 줄
    # 7. score 가 policy["approval_score"] 이상이면 (if, >=)
        return "승인 필요", reasons                                         # 결정과 이유를 함께 리턴한다 — 미리 채운 줄
    return "자동", reasons                                                  # 기준보다 낮으면 자동으로 실행한다 — 미리 채운 줄
```

**`exercise4-1_run.py`** — 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다.

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
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 8. decide_gate(request, policy) 의 두 결과를 decision, reasons 에 저장한다
    # 9. counts[decision] 에 counts[decision] + 1 을 저장한다 (1 늘린다)
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

**순서**

1. **[터미널]** `config` 폴더가 없으면 만듭니다.
   ```bash
   pwd
   mkdir -p config
   ls
   ```
   - 명령 풀이: `mkdir -p config` 는 `config` 폴더가 없을 때만 만듭니다(이미 있으면 그대로 둡니다).
   - **[VS Code]** 파일 네 개를 만듭니다. `config` 폴더를 오른쪽 클릭 › **New File** 로 `approval_policy.json` 을, `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `gate_requests.json` · `approval_gate.py` · `exercise4-1_run.py` 를 만들고, 각각 코드 상자의 내용을 붙여 넣고 저장합니다.
2. **[VS Code]** `approval_gate.py` 1 ~ 7번, `exercise4-1_run.py` 8 · 9번을 씁니다. 막히면 아래 「실습 4-1 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python exercise4-1_run.py
   ```
4. 출력은 다섯 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 과 단계 5 는 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 8줄, 단계 3 은 3줄, 단계 4 는 3줄입니다.
5. **[보고서]** `report_u4.md` 의 `## 실습 4-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 결정별 요청 수를 적고, 승인 필요인 요청 번호도 적어 주세요.
   - (나) [핵심 질문] `REQ-1`(`dami`)과 `REQ-6`(`minsu`)은 둘 다 high 등급의 계정 잠금인데 결정이 다릅니다. 단계 2 의 이유를 근거로 결정이 달라진 이유를 적어 주세요. 그리고 대상 수(영향 범위)를 위험 점수에 반영해야 하는 이유도 적어 주세요.
   - (다) [핵심 질문] `REQ-3` 은 high 등급이고 함께 쓰는 IP 인데 차단 금지입니다. `decide_gate` 가 허용 목록을 점수보다 먼저 확인하는 이유를 적고, 승인 기준(임계값)을 코드가 아니라 설정 파일로 분리하면 무엇이 좋은지 적어 주세요.

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
