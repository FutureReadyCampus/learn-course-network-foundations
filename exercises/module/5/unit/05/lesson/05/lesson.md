---
id: m5-u05-l05
title: 도전 5-1 · 탐지 결과 연결과 운영 요약
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/134_day06_am_soar_engine.md
  mission_id: GichanSource.m5-1116-am-soar-engine
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 도전 5-1 · 탐지 결과 연결과 운영 요약

## 목표: 입력 점검과 운영 요약

선택입니다. 시간이 남을 때 합니다. 핵심 실습 두 개와 글쓰기를 마친 뒤에 합니다. 이 도전에서 만드는 로그 `risk_engine_log.json` 은 「제공 파일」 레슨의 파일과 같은 내용이라, 하지 않아도 실습 5-2에는 영향이 없습니다.

> **오늘 들어온 일**
>
> - **상황**: <mark style="background:#e0d4ff">Module 4 Unit 4 실습 4-1에서 `risk_scores.py` 가 대상별 점수 · 등급 · 이유를 `unit05_risk_scores.json` 에 저장했습니다.</mark> `dami`(60점 high) · `seoyeon`(45점 mid) · `gaeun`(40점 mid) · `jiwoo`(35점 mid) · `198.51.100.90`(30점 low) 5건입니다. 실습 5-1 엔진은 Unit 1 시작하기 `incident_samples.json` 과 같은 모양의 알림을 읽습니다. 이번 Unit에서 팀장이 「Module 4에서 탐지된 5건을 엔진으로 처리하고, 무엇을 실행했는지 한 장으로 보고해 달라」고 요청합니다.
> - **문제**: Module 4 파일에는 알림 번호(`id`)와 상태(`status`)가 없어서 엔진에 바로 넣을 수 없습니다. Module 4와 Module 5는 따로 만든 프로그램이라, Module 4 파일의 모양이 바뀌면(필수 키가 빠지거나 등급 이름이 늘면) 엔진 안에서 오류가 납니다. 엔진 안에서 잡힌 오류는 그 알림의 조치와 티켓이 없는 「실패」로만 남습니다(실습 5-1 `INC-402`). <mark style="background:#ffc4d6">어느 기록이 왜 못 들어갔는지 엔진 앞에서 이유와 함께 남기지 않으면 탐지된 대상이 사라집니다.</mark>
> - **부탁**: Module 4 탐지 결과를 엔진이 읽는 알림으로 바꾸되, 바꾸기 전에 모양을 점검해 문제가 있는 기록은 이유와 함께 따로 모아 주세요. 엔진을 실행한 뒤에는 처리 결과별 알림 수 · 티켓 수 · 실제로 실행한 조치를 운영 요약으로 정리해 주세요.
> - **바뀌는 점**: 5건이 알림 `INC-501` ~ `INC-505` 로 바뀌어 모두 엔진에 들어가고(거절 <mark style="background:#bde3ff">0건</mark>), <mark style="background:#bde3ff">자동 실행 2건</mark>(`dami` 잠금 · `198.51.100.90` 차단)과 <mark style="background:#bde3ff">조치 없음 3건</mark>으로 처리됩니다. 티켓 <mark style="background:#bde3ff">5장</mark>이 만들어지고, 운영 요약은 `engine_summary.json` 에, 처리 결과 로그는 `risk_engine_log.json` 에 저장됩니다. 상황과 숫자는 설명을 위한 예시입니다.

## 1.1 입력 검증과 운영 요약

| Module 4 `unit05_risk_scores.json` 의 키 | 엔진이 읽는 알림의 키 | 하는 일 |
|---|---|---|
| `entity` · `score` · `grade` · `reasons` | 같은 이름 | 값을 그대로 옮긴다 |
| (없음) | `id` | `INC-501` 부터 번호를 붙인다 (3번) |
| (없음) | `status` | 처음 상태인 `탐지됨` 을 적는다 (4번) |

- Module 4의 출력과 Module 5의 입력이 같은 키 이름과 모양을 쓰기로 정한 약속을 공통 스키마(common schema, 커먼 스키마: 프로그램끼리 주고받는 데이터의 키 이름과 모양을 미리 정한 약속)라고 합니다. 오늘 엔진의 공통 스키마는 <mark style="background:#e0d4ff">Unit 1 시작하기 `incident_samples.json` 의 알림 모양</mark>입니다.
- 입력 검증(input validation, 인풋 밸리데이션: 데이터를 처리하기 전에 필수 키와 값의 범위가 맞는지 확인하는 일)에서는 <mark>필수 키가 있는지(1번), 등급 이름을 엔진이 아는지(2번)</mark> 점검합니다. 탐지된 규칙 이름이 비어 있는 기록도 거절합니다.
- 문제가 있는 기록은 버리지 않고 이유와 함께 거절 리스트(`rejected`)에 모읍니다. 거절 리스트가 있으면 Module 4 파일을 고쳐야 하는지 알 수 있습니다.
- 방어는 두 겹입니다. 엔진 앞의 입력 검증은 <mark>알려진 문제를 이유와 함께 걸러 내고</mark>, 실습 5-1의 오류 격리는 <mark>걸러 내지 못한 문제가 다른 알림으로 번지지 않게</mark> 합니다.
- 운영 요약은 근무를 인계하거나 보고할 때 한 번에 보여 주는 정리입니다. 오늘은 처리 결과별 알림 수(7번), 티켓 수, 실제로 실행한 조치(8번)를 담습니다. <mark>실제로 실행한 조치는 `executed` 가 참인 조치만 모읍니다.</mark>
- Module 4의 등급은 아래 표처럼 점수로 정해지고, 엔진은 이 등급을 그대로 승인 게이트의 `grade` 로 씁니다.

| 점수 | 등급 |
|---|---|
| 60점 이상 | high |
| 35점 이상 | mid |
| 그 아래 | low |

함수 네 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
engine_input.py   find_schema_problem  : 필수 키가 없으면 (1번) · 모르는 등급이면 (2번) 이유를 리턴한다
                  make_alert           : 알림 번호를 만들고 (3번) Module 4 기록을 알림 딕셔너리로 바꾼다 (4번)
                  split_records        : 기록마다 점검하고 (5번) 문제가 없으면 (6번) 알림 리스트에 넣는다
                  summarize            : 처리 결과별 알림 수를 세고 (7번) 실행한 조치만 (8번) 모은다
실행 파일         challenge5-1_run.py     : 엔진을 실행한다 (9번)
```

## 도전 5-1 · 탐지 결과 연결과 운영 요약

**이런 상황이 있습니다**

- **지금은**: <mark>Module 4 탐지 결과 파일은 있지만 엔진이 읽는 알림 모양이 아니고, 엔진을 실행한 결과를 한눈에 보고할 요약이 없습니다</mark>.
- **만드는 것**: 모양 점검 · 알림으로 바꾸기 · 기록 나누기 · 운영 요약(`engine_input.py`), 엔진 실행과 출력(`challenge5-1_run.py`).
- **실행하면**: <mark>단계 1: Module 4 탐지 결과 수, 단계 2: 일부러 틀리게 만든 기록 두 건의 점검 결과, 단계 3: 엔진에 넣을 알림, 단계 4: 알림마다 엔진 처리 결과, 단계 5: 운영 요약, 단계 6: 저장한 파일이 나옵니다.</mark>

**할 일**: 데이터 파일 한 개와 코드 파일 두 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행해서 단계 3 ~ 5 를 읽습니다.

**`unit05_risk_scores.json`** — Module 4 Unit 4 실습 4-1 파일입니다. Module 4 폴더(`anomaly_detection`)에 이 파일이 있으면 **[터미널]** 에서 `cp ../anomaly_detection/unit05_risk_scores.json .` 으로 복사하고, 없으면 `soar_response` 폴더에 같은 이름의 파일을 만들어 아래 내용을 붙여 넣습니다. 두 방법 모두 내용이 같습니다.

| 키 | 뜻 |
|---|---|
| `entity`(대상) | 계정 이름 또는 IP |
| `score`(점수) | 탐지된 규칙의 점수를 더한 값 |
| `grade`(등급) | 점수로 정한 high · mid · low |
| `reasons`(이유) | 탐지된 규칙 이름 리스트 |

<pre class="copyable"><code>[
  {
    "entity": "dami",
    "score": 60,
    "grade": "high",
    "reasons": [
      "퇴사한 계정"
    ]
  },
  {
    "entity": "seoyeon",
    "score": 45,
    "grade": "mid",
    "reasons": [
      "평소와 다른 IP",
      "대량 다운로드"
    ]
  },
  {
    "entity": "gaeun",
    "score": 40,
    "grade": "mid",
    "reasons": [
      "규칙은 허용인데 서버가 거절",
      "여러 로그 연결"
    ]
  },
  {
    "entity": "jiwoo",
    "score": 35,
    "grade": "mid",
    "reasons": [
      "업무 시간 밖 로그인",
      "평소와 다른 IP"
    ]
  },
  {
    "entity": "198.51.100.90",
    "score": 30,
    "grade": "low",
    "reasons": [
      "경로 스캔"
    ]
  }
]
</code></pre>

**`engine_input.py`** — Module 4 연결 함수 모음입니다. 실습 5-2에서는 가져오지 않습니다. 직접 쓰는 곳은 1 ~ 8번입니다.

| 번호 | 쓰는 것 |
|---|---|
| 1번 · 2번 · 6번 · 8번 | `if` 한 줄(그 아래 미리 채운 줄이 `if` 안쪽) |
| 7번 | 한 줄 |
| 4번 | 딕셔너리라서 줄을 나눠 씀 |

```python
REQUIRED_KEYS = ["entity", "score", "grade", "reasons"]              # Module 4 결과 기록에 반드시 있어야 하는 키
GRADES = ["high", "mid", "low"]                                      # 엔진이 읽을 수 있는 등급 이름
FIRST_NUMBER = 501                                                   # 엔진이 붙이는 알림 번호의 시작 (INC-501 부터)


def find_schema_problem(record):                                     # Module 4 결과 기록 한 건을 받는 함수
    """엔진이 읽을 수 없는 기록이면 그 이유 문장을, 문제가 없으면 빈 문자열("")를 리턴한다. Module 4 파일의 모양이 바뀌었을 때 엔진이 오류를 내기 전에 걸러 낼 때 쓴다."""
    for key in REQUIRED_KEYS:                                        # 필수 키를 하나씩 꺼낸다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 1. key 가 record 안에 없으면 (if, not in)
            return "필수 키 없음: " + key                            # 어떤 키가 없는지 이유로 리턴한다 — 미리 채운 줄
    # 2. record["grade"] 가 GRADES 안에 없으면 (if, not in)
        return "알 수 없는 등급: " + record["grade"]                 # 등급 이름을 이유로 리턴한다 — 미리 채운 줄
    if record["reasons"] == []:                                      # 탐지된 규칙 리스트가 비어 있으면 — 미리 채운 줄
        return "탐지된 규칙이 없음"                                  # 이유를 리턴한다 — 미리 채운 줄
    return ""                                                        # 문제가 없으면 빈 문자열를 리턴한다 — 미리 채운 줄


def make_alert(record, number):                                      # Module 4 결과 기록 한 건과 알림 번호 숫자를 받는 함수
    """Module 4 결과 기록(대상 · 점수 · 등급 · 이유)에 알림 번호와 상태를 붙여 Unit 1 인시던트 모양의 딕셔너리로 리턴한다. Module 4 파일의 기록을 엔진의 입력으로 바꿀 때 쓴다."""
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 3. "INC-" 뒤에 str(number) 를 이어 붙여 alert_id 에 저장한다
    # 4. 키 "id"(alert_id) · "entity" · "grade" · "score" · "reasons"(record 의 같은 이름 키의 값), "status"("탐지됨") 를 가진 딕셔너리를 alert 에 저장한다
    return alert                                                     # 엔진이 읽을 알림을 리턴한다 — 미리 채운 줄


def split_records(records):                                          # Module 4 결과 기록 리스트를 받는 함수
    """기록마다 모양을 점검해 엔진에 넣을 알림 리스트와 거절한 기록 리스트를 만들고 두 리스트를 함께 리턴한다. 거절한 기록을 이유와 함께 남겨 기록 없이 빠지지 않게 할 때 쓴다."""
    alerts = []                                                      # 엔진에 넣을 알림을 모을 빈 리스트 — 미리 채운 줄
    rejected = []                                                    # 거절한 기록과 이유를 모을 빈 리스트 — 미리 채운 줄
    number = FIRST_NUMBER                                            # 다음에 붙일 알림 번호 — 미리 채운 줄
    for record in records:                                           # 기록을 하나씩 꺼낸다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. find_schema_problem(record) 의 결과를 problem 에 저장한다
        # 6. problem 이 "" 이면 (if, ==)
            alert = make_alert(record, number)                       # 알림 모양으로 바꾼다 — 미리 채운 줄
            alerts.append(alert)                                     # 알림 리스트에 추가한다 — 미리 채운 줄
            number = number + 1                                      # 다음 번호로 넘어간다 — 미리 채운 줄
        else:                                                        # 문제가 있으면 — 미리 채운 줄
            rejected.append({"record": record, "problem": problem})  # 기록과 이유를 거절 리스트에 추가한다 — 미리 채운 줄
    return alerts, rejected                                          # 두 리스트를 함께 리턴한다 — 미리 채운 줄


def summarize(results):                                              # 엔진 결과 기록 리스트를 받는 함수
    """결과 기록을 모아 처리 결과별 알림 수 · 만든 티켓 수 · 실제로 실행한 조치 문장 리스트를 담은 요약 딕셔너리를 리턴한다. 운영 담당자가 한 번에 볼 요약이 필요할 때 쓴다."""
    outcome_counts = {"자동 실행": 0, "승인 대기": 0, "차단 금지": 0, "조치 없음": 0, "실패": 0}  # 처리 결과마다 알림 수 : 처음에는 모두 0 — 미리 채운 줄
    ticket_count = 0                                                 # 만든 티켓 수 : 처음에는 0 — 미리 채운 줄
    executed_actions = []                                            # 실제로 실행한 조치 문장을 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                           # 결과 기록을 하나씩 꺼낸다 — 미리 채운 줄
        outcome = result["outcome"]                                  # 이 알림의 처리 결과 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 7. outcome_counts[outcome] 에 outcome_counts[outcome] + 1 을 저장한다 (1 늘린다)
        if result["ticket"] != "":                                   # 티켓이 있으면 — 미리 채운 줄
            ticket_count = ticket_count + 1                          # 티켓 수를 1 늘린다 — 미리 채운 줄
        for step in result["steps"]:                                 # 조치 결과를 하나씩 꺼낸다 — 미리 채운 줄
            # 8. step["executed"] 가 참이면 (if)
                action_text = result["incident"] + " " + step["action"] + " " + step["target"] + ": " + step["before"] + " → " + step["after"]  # 알림 · 조치 · 대상 · 전 · 후 상태를 한 문장으로 만든다 — 미리 채운 줄
                executed_actions.append(action_text)                 # 문장을 추가한다 — 미리 채운 줄
    summary = {"outcome_counts": outcome_counts, "ticket_count": ticket_count, "executed_actions": executed_actions}  # 요약 딕셔너리 — 미리 채운 줄
    return summary                                                   # 요약을 리턴한다 — 미리 채운 줄
```

**`challenge5-1_run.py`** — 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다.

```python
from incident import load_json, save_json                                                    # Unit 1 파일의 JSON 읽기 · 쓰기 함수를 불러온다
from soar_engine import load_context, run_all                                                # 실습 5-1에 만든 엔진 함수를 불러온다
from engine_input import find_schema_problem, split_records, summarize                       # 방금 만든 연결 함수를 불러온다

TEST_RECORDS = [                                                                             # 모양을 일부러 틀리게 만든 시험 기록 두 건
    {"entity": "hana", "score": 40, "reasons": ["업무 시간 밖 로그인"]},                     # grade 키가 없다
    {"entity": "minsu", "score": 90, "grade": "critical", "reasons": ["퇴사한 계정"]},       # 엔진이 모르는 등급 이름이다
]

records = load_json("unit05_risk_scores.json")                                                # Module 4가 저장한 탐지 결과 파일을 리스트로 읽는다
print("--- 단계 1: Module 4 탐지 결과", len(records), "건")                                     # 단계 1 시작을 알리는 줄과 건수

print("--- 단계 2: 모양 점검 시험 (일부러 틀린 기록)")                                       # 단계 2 시작을 알리는 줄
for test_record in TEST_RECORDS:                                                             # 시험 기록을 하나씩 꺼낸다
    test_problem = find_schema_problem(test_record)                                          # 모양 점검 결과를 받는다
    print(test_record["entity"], "→", test_problem)                                          # 대상과 점검 결과를 출력한다

alerts, rejected = split_records(records)                                                    # 기록을 엔진에 넣을 알림과 거절한 기록으로 나눈다
print("--- 단계 3: 엔진에 넣을 알림", len(alerts), "건 · 거절한 기록", len(rejected), "건")  # 단계 3 시작을 알리는 줄과 건수
for alert in alerts:                                                                         # 알림을 하나씩 꺼낸다
    print(alert["id"], alert["entity"], alert["grade"], alert["score"], alert["reasons"])    # 알림 번호 · 대상 · 등급 · 점수 · 이유를 출력한다

context = load_context()                                                                     # 엔진이 쓰는 재료를 읽는다
# ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
# 9. run_all(alerts, context) 의 결과를 results 에 저장한다
print("--- 단계 4: 엔진 처리 결과")                                                          # 단계 4 시작을 알리는 줄
for result in results:                                                                       # 결과 기록을 하나씩 꺼낸다
    print(result["incident"], result["entity"], "→", result["outcome"], "·", result["playbook"], "· 티켓", result["ticket"])  # 알림 · 대상 · 처리 결과 · 플레이북 · 티켓을 출력한다

summary = summarize(results)                                                                 # 결과를 모아 운영 요약을 만든다
counts = summary["outcome_counts"]                                                           # 처리 결과별 알림 수 딕셔너리
print("--- 단계 5: 운영 요약")                                                               # 단계 5 시작을 알리는 줄
print("자동 실행", counts["자동 실행"], "건 · 승인 대기", counts["승인 대기"], "건 · 차단 금지", counts["차단 금지"], "건 · 조치 없음", counts["조치 없음"], "건 · 실패", counts["실패"], "건")  # 처리 결과별 알림 수를 한 줄로 출력한다
print("티켓", summary["ticket_count"], "건 · 실제로 실행한 조치", len(summary["executed_actions"]), "건")  # 티켓 수와 실행한 조치 수를 출력한다
for action_text in summary["executed_actions"]:                                              # 실행한 조치 문장을 하나씩 꺼낸다
    print(action_text)                                                                       # 문장을 출력한다

save_json(results, "risk_engine_log.json")                                                   # 결과 기록 리스트를 파일에 저장한다
save_json(summary, "engine_summary.json")                                                    # 운영 요약을 파일에 저장한다
save_json(context["tickets"], "risk_tickets.json")                                           # 만든 티켓 리스트를 파일에 저장한다
print("--- 단계 6: risk_engine_log.json · engine_summary.json · risk_tickets.json 저장")     # 단계 6 시작을 알리는 줄
```

**순서**

1. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `unit05_risk_scores.json` · `engine_input.py` · `challenge5-1_run.py` 파일을 만들어 이 페이지의 코드 상자를 붙여 넣고 저장합니다. Module 4 파일을 복사해 왔으면 `unit05_risk_scores.json` 은 만들지 않습니다.
2. **[VS Code]** `engine_input.py` 1 ~ 8번, `challenge5-1_run.py` 9번을 씁니다. 막히면 아래 「도전 5-1 정리」를 봅니다.
3. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python challenge5-1_run.py
   ```
4. 출력은 여섯 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 과 단계 6 은 숫자나 파일 이름이 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 2줄, 단계 3 은 제목 줄에 건수가 나오고 그 아래 5줄입니다. 단계 4 는 5줄입니다.
   - 단계 5 는 제목 줄 아래 2줄에 실행한 조치 줄이 더 붙습니다.
5. 단계 6 에서 `risk_engine_log.json` 이 다시 저장됩니다. 「제공 파일」 레슨에서 만든 파일이 있었다면 같은 내용으로 덮어쓰므로 실습 5-2 결과는 그대로입니다.
6. **[보고서]** `report_u5.md` 의 `## 도전 5-1` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 단계 5 의 처리 결과별 알림 수와 실제로 실행한 조치 두 개를 적어 주세요.
   - (나) [핵심 질문] `seoyeon` · `gaeun` · `jiwoo` 는 모두 「조치 없음」인데 티켓은 만들어졌습니다. 단계 4 에서 알림 뒤에 나오는 플레이북 번호를 근거로 세 알림에 조치가 없는 이유를 적고, 티켓이 없다면 이 세 알림이 어떻게 되는지 적어 주세요.
   - (다) [핵심 질문] 단계 2 의 `minsu` 기록은 등급이 `critical` 입니다. `find_schema_problem` 이 이 기록을 엔진 앞에서 거절하는 이유를 적고, 거절 없이 엔진에 넣으면 어떤 오류가 나고 그 알림이 어떻게 기록되는지 실습 5-1 `INC-402` 와 연결해 적어 주세요.

## 도전 5-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 리스트 안에 없으면 | `if key not in record:` · `if record["grade"] not in GRADES:` |
| 문자열을 이어 붙여 저장하기 | `alert_id = "INC-" + str(number)` |
| 키와 값을 짝지어 딕셔너리 만들기 | `alert = {"id": alert_id, "entity": record["entity"], …}` |
| 함수 결과를 변수에 저장하기 | `problem = find_schema_problem(record)` |
| 같으면 | `if problem == "":` |
| 1 늘려 다시 저장하기 | `outcome_counts[outcome] = outcome_counts[outcome] + 1` |
| 참이면 | `if step["executed"]:` |
---
