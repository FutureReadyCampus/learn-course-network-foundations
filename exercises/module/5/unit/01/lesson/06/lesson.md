---
id: m5-u01-l06
title: 응용 1-1 · 맥락에 따라 처리 경로 나누기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/118_day02_am_context_route_safety.md
  mission_id: GichanSource.m5-1110-am-context-route-safety
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 응용 1-1 · 맥락에 따라 처리 경로 나누기

## 이번 의뢰: 오탐과 VIP 계정 구분

> **여유가 되면 해 보세요.** 핵심 실습 1-1 ~ 1-3과 글쓰기를 먼저 마칩니다. 이 응용을 하지 않아도 다음 Unit을 따라가는 데 문제가 없습니다.

> **오늘 들어온 일**
>
> - **상황**: 지난주 협력사 사무실(`203.0.113.80`)에서 온 `평소와 다른 IP` 알림이 12건 있었습니다. 분석팀이 한 건씩 열어 분석(triage, 트리아지: 알림의 진위와 우선순위를 판정하는 초기 분류)했고 12건 모두 정상 업무로 판정되었습니다. 12건을 분석하는 데 1시간이 걸렸습니다(한 건당 5분).
> - **문제**:
> - 그 1시간 동안 다른 알림을 확인하는 일이 늦어졌습니다.
> - 반대로 계정 관리자 `gaeun`(VIP 계정)의 알림이 플레이북에 맞으면 지금은 일반 계정과 같은 절차로 처리됩니다. 이 계정이 잘못 잠기면 직원 계정 관리 업무가 중단됩니다.
> - **부탁**: 협력사의 정상 접속 알림은 종료 사유를 기록하고 자동으로 종료(close)해 주세요. 이처럼 실제로는 위협이 아닌데 위협으로 탐지된 알림을 **오탐**(false positive, 폴스 포지티브)이라고 합니다. VIP 계정은 담당자가 승인한 뒤에만 조치해 주세요.
> - **바뀌는 점**: 분석팀은 아낀 1시간을 위험도가 높은 알림 분석에 씁니다. VIP 계정은 담당자가 승인하기 전에는 조치되지 않습니다. 오늘 샘플에서는 5건 가운데 `INC-004` 한 건이 자동 종료되고 `INC-003` 한 건이 담당자 승인 경로로 분기됩니다. 12건과 5분은 설명을 위한 예시 숫자입니다.

## 2.1 조건 분기(branching) — 맥락에 따라 알림을 서로 다른 처리 경로로 분기한다

알림을 조건에 따라 세 가지 처리 경로(route) 가운데 하나로 분류해 보냅니다. 이처럼 조건에 따라 실행 경로를 나누는 일을 **조건 분기**(branching, 브랜칭)라고 하며, SOAR 플레이북에서는 알림의 맥락이나 신뢰도에 따라 자동 실행과 분석가 검토 중 하나를 선택하는 데 씁니다.

| 경로 | 보내는 조건 | 하는 일 | 오늘 샘플 |
|---|---|---|---|
| `승인 필요` | 대상이 VIP 계정이다 | 담당자가 확인하기 전에는 조치하지 않는다 | `INC-003`(`gaeun`) |
| `오탐 종료` | 접속 IP 가 신뢰 IP 이고, 탐지된 규칙이 **모두** IP 관련 규칙이다 | 상태를 `분류됨` 으로, 이어서 `종료` 로 바꾸고 종료 사유를 기록한다 | `INC-004`(`jiwoo`) |
| `기본` | 위 두 경우가 아니다 | 실습 1-2의 실행기가 플레이북 절차대로 처리한다 | `INC-001` · `INC-002` · `INC-005` |

- **탐지 규칙**(detection rule, 디텍션 룰: 알림을 발생시키는 조건): 알림에는 `reasons` 라는 리스트가 있고, 이 알림을 발생시킨 탐지 규칙의 이름이 들어 있습니다. 예를 들어 `INC-002` 는 `["평소와 다른 IP", "대량 다운로드"]` 입니다.
- **IP 관련 규칙**: 접속 IP 를 보고 낸 규칙입니다. 오늘은 `평소와 다른 IP` 와 `업무 시간 밖 로그인` 두 가지입니다.

- **상태**(status)는 알림을 어디까지 처리했는지 나타내는 값(처리 진행 단계)이고, `탐지됨` → `분류됨` → `조치됨` 또는 `종료` 순서로 바뀝니다.
- <mark>VIP 를 먼저 확인합니다.</mark> VIP 계정의 알림이 신뢰 IP 에서 접속했다는 이유만으로 자동으로 닫히면 안 되기 때문입니다.
- <mark>탐지 규칙이 **모두** IP 관련일 때만 종료합니다.</mark> 신뢰 IP 에서 접속했어도 `대량 다운로드` 처럼 IP 와 무관한 규칙이 함께 탐지되었다면, 그 다운로드가 정상이라는 근거는 되지 못하기 때문입니다. `INC-002` 가 이에 해당합니다.

**문법 상자 — 튜플 리턴과 언패킹(tuple unpacking): 두 값을 한 번에 리턴하고 한 번에 받는다**

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
| `return "높음", "바로 확인"` | 값 두 개를 쉼표로 이어 함께 리턴한다 |
| `level, action = check(70)` | 함께 온 두 값을 순서대로 변수 두 개에 하나씩 저장한다 |
| 위 코드의 출력 | `높음` 과 `바로 확인` 이 한 줄씩 나온다 |

- 쉼표로 이은 값 묶음을 **튜플**(tuple)이라고 하고, 그 묶음을 풀어 변수에 저장하는 것을 **언패킹**(unpacking)이라고 합니다.
- 리턴하는 값의 개수와 받는 변수의 개수가 다르면 `ValueError`(밸류 에러: 값의 개수나 형태가 맞지 않을 때 나는 오류)가 납니다.

직접 쓰는 곳은 함수와 실행 파일을 합쳐 **아홉 군데**입니다.

```
routing.py   is_only_ip_related : 규칙을 하나씩 꺼내 IP 관련이 아닌 것이 있으면 False 를 리턴한다 (1 ~ 3번)
             decide_route       : VIP 이면 「승인 필요」 (4 · 5번) / 신뢰 IP 이고 규칙이 모두 IP 관련이면 「오탐 종료」 (6 · 7번) / 아니면 「기본」 (미리 채움)
             apply_route        : 오탐 종료이면 상태를 종료로 옮기고 이유를 기록한다 (미리 채움)
실행 파일    apply1-1_run.py   : decide_route 가 리턴한 두 값을 언패킹으로 받고 (8번), 경로별 건수를 센다 (9번)
```

## 응용 1-1 · 경로 분기하고 경로별 건수 세기

**이런 상황이 있습니다**

- **지금은**: <mark>알림을 규칙 이름과 등급만 보고 처리하므로 계정 관리자(VIP)의 알림과 협력사의 정상 접속 알림을 따로 다룰 수 없습니다</mark>.
- **만드는 것**: 규칙이 모두 IP 관련인지 판별하는 함수와 처리 경로를 결정하는 함수(`routing.py`), 경로를 받아 적용하는 부분과 경로별 건수 집계(`apply1-1_run.py`). 경로를 결정할 때마다 판정 이유도 문장으로 함께 리턴합니다.
- **실행하면**: <mark>단계 1: 알림마다 경로 · 이유 · 상태, 단계 2: 경로별 건수가 나옵니다.</mark>

**할 일**: 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 1 · 2 를 읽습니다.

**`routing.py`** — 맥락을 보고 처리 경로를 정합니다. 이 파일이 정한 경로(`승인 필요` · `오탐 종료` · `기본`)를 Unit 2 응용 2-2 와 Unit 3 응용 3-1 에서도 씁니다. 직접 쓰는 곳은 1 ~ 7번입니다.

**제공 파일과의 관계** — `routing.py` 는 「제공 파일」 레슨에서 이미 완성본으로 만들었습니다. 이 응용에서는 그 내용을 아래 골격으로 **바꿔서(덮어써서)** 직접 써 봅니다. 다음 Unit에서도 이 파일을 쓰므로, 다 쓴 뒤 실행 결과가 「정답」과 같은지 확인하고, 막히면 「제공 파일」의 완성본을 다시 붙여 넣습니다.

```python
from incident import change_status                                          # 실습 1-2 의 incident.py 에서 상태 바꾸기 함수를 불러온다

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

**`apply1-1_run.py`** — 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 실습 1-3의 `enrichment.py` 가 같은 폴더에 있어야 합니다.

```python
from incident import load_json, INCIDENTS_PATH                      # 실습 1-2 의 incident.py 에서 함수를 불러온다
from enrichment import enrich_incident                              # 실습 1-3에서 만든 함수를 불러온다
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

1. **[VS Code]** `routing.py` 를 열어 내용을 모두 지우고 위 골격을 붙여 넣습니다. `apply1-1_run.py` 는 `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 새로 만들어(파일 이름 그대로) 붙여 넣고 저장합니다.
2. **[VS Code]** `routing.py` 1 ~ 7번, `apply1-1_run.py` 8 · 9번을 씁니다. 막히면 아래 「응용 1-1 정리」를 봅니다.
3. **[터미널]** 실행합니다(맥북은 `python3`).
   ```bash
   python apply1-1_run.py
   ```
4. 출력은 두 단계입니다.

   | 단계 | 나오는 것 |
   |---|---|
   | 1 | 알림 5건이 한 줄씩. 번호 · 대상 · 등급, `->` 뒤에 경로 · 이유, 괄호 안에 상태 |
   | 2 | 경로마다 한 줄씩 3줄 |

5. **[보고서]** `report_u1.md` 의 `## 응용 1-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 경로별 건수와 `종료` 상태가 된 알림의 번호를 적어 주세요.
   - (나) [핵심 질문] INC-002 와 INC-004 는 둘 다 신뢰 IP 에서 접속했는데 INC-002 는 `기본`, INC-004 는 `오탐 종료` 입니다. 두 알림의 `reasons` 를 근거로 경로가 달라진 이유를 적어 주세요.
   - (다) [핵심 질문] 6번 조건보다 4번 VIP 판정을 먼저 두었습니다. VIP 계정이 신뢰 IP 에서 접속했고 `평소와 다른 IP` 규칙 하나만 탐지되었다고 가정해 보세요. 이 알림이 어느 경로로 분기되는지 적어 주세요. 그리고 4번과 6번 조건의 순서를 바꾸면 무엇이 달라지는지 적어 주세요.

## 응용 1-1 정리

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
