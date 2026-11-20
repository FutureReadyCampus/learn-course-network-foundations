---
id: m5-u04-l08
title: 도전 4-4 · 자동 조치 리스크 평가 문서 작성
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/132_day05_pm_risk_check.md
  mission_id: GichanSource.m5-1113-pm-risk-check
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 도전 4-4 · 자동 조치 리스크 평가 문서 작성

## 목표: 리스크 평가 문서

> **선택입니다. 시간이 남을 때 합니다.** 핵심 실습 4-1 · 4-2와 글쓰기를 먼저 마칩니다. 이 도전은 판다스(pandas)를 쓰고, 앞의 도전을 하지 않았어도 이 레슨의 파일만으로 진행합니다.

> **오늘 들어온 일**
>
> - **상황**: 지금까지 계정 잠금 · 세션 종료 · IP 차단 · 티켓 자동 작성 · 담당자 알림 · 상급자 에스컬레이션(escalation, 에스컬레이션: 정해진 시간 안에 처리되지 않은 사건을 상위 담당자에게 넘겨 처리하게 하는 일) 여섯 가지를 자동 조치로 구현했습니다. <mark style="background:#e0d4ff">실습 4-1 의 승인 게이트는 **요청 한 건마다** 위험을 판정했습니다.</mark> 보안팀장이 「운영에 적용하기 전에 **자동 조치 종류마다** 위험을 평가한 문서를 제출해 주세요」라고 합니다.
> - **문제**: 어떤 자동 조치가 잘못 실행됐을 때 피해가 큰지 정리한 문서가 없습니다. 그 조치에 승인 게이트나 감사 기록 같은 통제가 갖춰져 있는지 정리한 문서도 없습니다. 예를 들어 세션 종료는 되돌릴 수 없는 조치인데, <mark style="background:#ffc4d6">오늘 샘플의 통제 목록에는 세션 종료의 승인 게이트가 빠져 있습니다.</mark> 이렇게 필요한 통제와 지금 있는 통제의 차이를 통제 갭(control gap, 컨트롤 갭)이라고 합니다.
> - **부탁**: 조치마다 ① 영향도와 발생 가능성을 곱해 위험 점수를 산출하고 ② 점수 구간에 따라 높음 · 보통 · 낮음 등급으로 분류한 뒤 ③ <mark>등급별 필수 통제가 빠진 조치를 찾아</mark> `risk_assessment.md` 로 작성해 주세요.
> - **바뀌는 점**: `risk_assessment.md` 16줄이 생성됩니다. 오늘 샘플에서는 <mark style="background:#bde3ff">바로 보완할 조치가 2개</mark>(세션 종료에 승인 게이트, 담당자 알림에 감사 기록)로 산출됩니다. 상황과 숫자는 설명을 위한 예시입니다.

## 1.1 위험 점수와 통제 갭 분석

**리스크 평가**(risk assessment, 리스크 어세스먼트: 일이 잘못됐을 때의 피해와 그 일이 일어날 가능성을 따져 위험의 크기를 정하는 일)에서는 위험을 아래 두 값의 조합으로 나타냅니다. NIST SP 800-30(미국 국립표준기술연구소 NIST 가 낸 리스크 평가 지침)도 위험을 위협이 일어날 가능성과 그 결과의 영향이라는 두 요소로 설명합니다. 오늘은 두 값을 모두 <mark style="background:#ffdcb0">1 ~ 3</mark> 의 숫자 척도(scale, 스케일: 등급을 매기는 숫자 범위)로 매깁니다.

| 값 | 뜻 | 오늘의 예 |
|---|---|---|
| **영향도**(impact, 임팩트) | 자동 조치가 잘못 실행됐을 때 업무에 미치는 피해의 크기(심각도). <mark style="background:#ffdcb0">1(작음) ~ 3(큼)</mark> | 계정 잠금은 3: 오탐이면 정상 직원이 로그인하지 못해 업무가 멈춘다 |
| **발생 가능성**(likelihood, 라이클리후드) | 자동 조치가 잘못 실행될 가능성(발생 빈도). <mark style="background:#ffdcb0">1(드묾) ~ 3(잦음)</mark> | 담당자 알림은 3: 오탐 알림도 그대로 보낸다 |
| **위험 점수**(risk score, 리스크 스코어) | 영향도 × 발생 가능성. 1 ~ 9 | <mark style="background:#bde3ff">계정 잠금은 3 × 2 = 6</mark> |

| 위험 등급 | 점수 | 반드시 있어야 하는 통제 |
|---|---|---|
| 높음 | 6 이상 | 승인 게이트 · 감사 기록 |
| 보통 | 3 이상 6 미만 | 감사 기록 |
| 낮음 | 3 미만 | 따로 정하지 않는다 |

- **통제**(control, 컨트롤)는 위험을 줄이는 장치이고, 기능에 따라 세 종류로 나눕니다. **예방 통제**(preventive control, 프리벤티브 컨트롤)는 잘못 실행되기 전에 막습니다(예: 승인 게이트). **교정 통제**(corrective control, 코렉티브 컨트롤)는 잘못 실행된 뒤 피해를 줄이고 원래 상태로 복구합니다(예: 되돌리기). **탐지 통제**(detective control, 디텍티브 컨트롤)는 일어난 일을 나중에 확인할 수 있게 합니다(예: 감사 기록). <mark style="background:#e0d4ff">지금까지 만든 승인 게이트(실습 4-1) · 되돌리기(Unit 3) · 허용 목록(Unit 2) · 감사 기록(Unit 1) · 알림 간격(Unit 3)</mark>이 모두 통제입니다.
- 세션 종료는 되돌릴 수 없어서 교정 통제(되돌리기)를 쓸 수 없습니다. 그래서 <mark>잘못 실행되기 전에 막는 예방 통제(승인 게이트)가 더 중요합니다.</mark>
- 영향도와 발생 가능성의 숫자, 그리고 <mark style="background:#ffdcb0">등급 기준(6 이상 높음, 3 이상 보통)</mark>은 팀이 위험 허용 수준(risk tolerance, 리스크 톨러런스: 조직이 받아들일 수 있다고 정한 위험의 크기)에 맞춰 회의로 정합니다. 오늘 파일의 숫자와 통제 목록은 예시입니다. 통제를 적용한 뒤에도 남는 위험을 잔여 위험(residual risk, 레지듀얼 리스크)이라고 하는데, 오늘 코드는 잔여 위험을 계산하지 않고 필수 통제가 빠졌는지만 비교합니다.

새 문법은 없습니다. 두 열을 곱해 새 열을 만드는 일(1번)은 도전 4-3 의 두 열 빼기와 같은 모양이고, 정렬 `sort_values(ascending=False)`(6번)는 <mark style="background:#e0d4ff">Module 4 Unit 2 실습 2-2 에서 배웠습니다</mark>. 여기서는 표(DataFrame)를 정렬하므로 기준이 되는 열 이름 `"score"` 를 앞에 하나 더 씁니다.

함수 다섯 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
risk_assessment.py   make_risk_table        : 표로 바꾸고 위험 점수 열을 더한다 (1번)
                     risk_level             : 6 이상이면 (2번) 높음을 리턴한다 (3번). 보통 · 낮음은 미리 채움
                     find_missing_controls  : 있어야 하는 통제가 없으면 (4번) 추가한다 (5번)
                     assess_risks           : 점수가 큰 것부터 정렬하고 (6번), 조치마다 빠진 통제를 찾는다 (7번)
                     make_assessment_lines  : 리스크 평가 문서의 줄 리스트를 만든다 (미리 채움)
실행 파일            challenge4-4_run.py       : 평가 결과를 받아 (8번), 빠진 통제가 있는 조치를 센다 (9번)
```

## 도전 4-4 · 자동 조치 리스크 평가 문서 작성

**이런 상황이 있습니다**

- **지금은**: <mark>자동 조치마다 위험이 얼마나 큰지, 필요한 통제가 갖춰져 있는지 정리한 리스크 평가 문서가 없습니다</mark>.
- **만드는 것**: 위험 점수 산출 · 등급 분류 · 통제 갭 분석 · 위험도순 정렬(`risk_assessment.py`), 평가 결과 출력과 리스크 평가 문서 저장(`challenge4-4_run.py`).
- **실행하면**: <mark style="background:#bde3ff">단계 1: 불러온 자동 조치 수, 단계 2: 점수가 큰 조치부터 등급과 빠진 통제, 단계 3: 바로 보완할 조치 수와 저장한 문서가 나옵니다.</mark>

**할 일**: 데이터 파일 하나와 코드 파일 두 개를 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 실행한 뒤 문서 파일을 열어 읽습니다.

**`config/automation_risks.json`** — 자동 조치 6가지의 영향도 · 발생 가능성 · 지금 있는 통제(existing control, 이그지스팅 컨트롤: 이미 적용된 통제)를 적은 입력 데이터입니다.

<pre class="copyable"><code>[
  {"action": "계정 잠금", "impact": 3, "likelihood": 2, "controls": ["승인 게이트", "되돌리기", "감사 기록", "VIP 예외"]},
  {"action": "세션 종료", "impact": 3, "likelihood": 2, "controls": ["감사 기록"]},
  {"action": "IP 차단", "impact": 3, "likelihood": 2, "controls": ["허용 목록", "승인 게이트", "자동 해제", "되돌리기", "감사 기록"]},
  {"action": "티켓 자동 작성", "impact": 1, "likelihood": 2, "controls": ["병합", "감사 기록"]},
  {"action": "담당자 알림", "impact": 1, "likelihood": 3, "controls": ["알림 간격", "재시도"]},
  {"action": "상급자 에스컬레이션", "impact": 2, "likelihood": 1, "controls": ["같은 단계 한 번"]}
]
</code></pre>

**`risk_assessment.py`** — 리스크 평가 함수 모음입니다. 직접 쓰는 곳은 1 ~ 7번입니다.

- 2번과 3번은 `if` 한 줄과 그 안의 `return` 한 줄입니다. 그 아래 미리 채운 `if score >= 3:` 은 2번과 같은 들여쓰기입니다.

```python
import pandas as pd                                                         # 표를 다루기 위해 판다스를 pd 라는 이름으로 불러온다

REQUIRED_CONTROLS = {                                                       # 위험 등급마다 반드시 있어야 하는 통제
    "높음": ["승인 게이트", "감사 기록"],                                   # 잘못되면 피해가 큰 조치
    "보통": ["감사 기록"],                                                  # 나중에 확인할 수 있어야 하는 조치
    "낮음": [],                                                             # 따로 요구하지 않는다
}


def make_risk_table(risks):                                                 # 자동 조치마다 적은 위험 리스트를 받는 함수
    """위험 리스트를 표(DataFrame)로 바꾸고, 영향도 × 발생 가능성으로 위험 점수(score) 열을 더해 리턴한다.
    자동 조치마다 위험이 얼마나 큰지 숫자 하나로 비교할 때 쓴다.
    """
    table = pd.DataFrame(risks)                                             # 위험 리스트를 표로 바꾼다 — 미리 채운 줄
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. table["impact"] * table["likelihood"] 를 table["score"] 에 담는다 (위험 점수)
    return table                                                            # 점수 열을 더한 표를 리턴한다 — 미리 채운 줄


def risk_level(score):                                                      # 위험 점수를 받는 함수
    """위험 점수가 6 이상이면 「높음」, 3 이상이면 「보통」, 그보다 낮으면 「낮음」을 리턴한다.
    점수를 사람이 읽기 쉬운 등급으로 바꿀 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. score 가 6 이상이면 (if, >=)
        # 3. "높음" 을 리턴한다
    if score >= 3:                                                          # 3 이상이면 — 미리 채운 줄
        return "보통"                                                       # 보통을 리턴한다 — 미리 채운 줄
    return "낮음"                                                           # 그보다 낮으면 낮음을 리턴한다 — 미리 채운 줄


def find_missing_controls(level, controls):                                 # 위험 등급과 지금 있는 통제 리스트를 받는 함수
    """그 등급에 반드시 있어야 하는 통제 가운데 지금 없는 것을 리스트로 리턴한다.
    위험이 큰 자동 조치에 승인이나 되돌리기 같은 통제가 빠졌는지 찾을 때 쓴다.
    """
    missing = []                                                            # 빠진 통제를 모을 빈 리스트 — 미리 채운 줄
    required = REQUIRED_CONTROLS[level]                                     # 이 등급에 반드시 있어야 하는 통제 — 미리 채운 줄
    for control in required:                                                # 있어야 하는 통제를 하나씩 꺼낸다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 4. control 이 controls 안에 없으면 (if, not in)
            # 5. missing 에 control 을 추가한다 (append)
    return missing                                                          # 빠진 통제 리스트를 리턴한다 — 미리 채운 줄


def assess_risks(table):                                                    # 점수 열이 있는 위험 표를 받는 함수
    """점수가 큰 조치부터 정렬하고, 조치마다 등급과 빠진 통제를 붙인 딕셔너리 리스트를 리턴한다.
    리스크 평가 문서에 위험이 큰 조치부터 적을 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 6. table.sort_values("score", ascending=False) 를 sorted_table 에 담는다 (점수가 큰 것부터)
    rows = []                                                               # 평가 결과를 모을 빈 리스트 — 미리 채운 줄
    for row in sorted_table.to_dict("records"):                             # 표를 딕셔너리 리스트로 바꿔 하나씩 꺼낸다 — 미리 채운 줄
        level = risk_level(row["score"])                                    # 점수로 등급을 정한다 — 미리 채운 줄
        # 7. find_missing_controls(level, row["controls"]) 의 결과를 missing 에 담는다
        row["level"] = level                                                # 등급을 딕셔너리에 넣는다 — 미리 채운 줄
        row["missing"] = missing                                            # 빠진 통제를 딕셔너리에 넣는다 — 미리 채운 줄
        rows.append(row)                                                    # 평가 결과를 추가한다 — 미리 채운 줄
    return rows                                                             # 평가 결과 리스트를 리턴한다 — 미리 채운 줄


def make_assessment_lines(rows):                                            # 평가 결과 리스트를 받는 함수
    """평가 결과로 리스크 평가 문서(마크다운)의 줄 리스트를 만들어 리턴한다.
    자동 조치를 운영에 넣기 전에 팀이 함께 읽을 문서를 쓸 때 쓴다.
    """
    lines = ["# 자동 대응 리스크 평가 — 2026-11-13(금)", ""]                # 제목과 빈 줄로 시작한다
    lines.append("- 점수 = 영향도(1~3) × 발생 가능성(1~3). 6 이상 높음, 3 이상 보통, 그 밖은 낮음")  # 기준을 적는다
    lines.append("")                                                        # 빈 줄
    lines.append("| 자동 조치 | 영향도 | 발생 가능성 | 점수 | 등급 | 지금 있는 통제 | 빠진 통제 |")  # 표의 제목 줄
    lines.append("|---|---|---|---|---|---|---|")                           # 표의 구분 줄
    for row in rows:                                                        # 평가 결과를 하나씩 꺼낸다
        controls_text = ", ".join(row["controls"])                          # 지금 있는 통제를 쉼표로 잇는다
        missing_text = ", ".join(row["missing"])                            # 빠진 통제를 쉼표로 잇는다
        if missing_text == "":                                              # 빠진 통제가 없으면
            missing_text = "없음"                                           # 없음이라고 적는다
        numbers = str(row["impact"]) + " | " + str(row["likelihood"]) + " | " + str(row["score"])  # 영향도 · 발생 가능성 · 점수를 표 모양으로 잇는다
        lines.append("| " + row["action"] + " | " + numbers + " | " + row["level"] + " | " + controls_text + " | " + missing_text + " |")  # 표의 한 줄
    lines.append("")                                                        # 빈 줄
    lines.append("## 바로 보완할 조치")                                     # 보완할 조치 절의 제목
    for row in rows:                                                        # 평가 결과를 하나씩 꺼낸다
        if row["missing"] != []:                                            # 빠진 통제가 있으면
            gap_text = ", ".join(row["missing"])                            # 빠진 통제를 쉼표로 잇는다
            lines.append("- " + row["action"] + ": " + gap_text + " 추가")  # 보완할 내용을 적는다
    return lines                                                            # 완성한 줄 리스트를 리턴한다
```

**`challenge4-4_run.py`** — 8 · 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다.

```python
from incident import load_json                                                             # Unit 1 파일의 JSON 읽기 함수를 불러온다
from risk_assessment import make_risk_table, assess_risks, make_assessment_lines           # 방금 만든 리스크 평가 함수를 불러온다

DOC_PATH = "risk_assessment.md"                                                            # 리스크 평가 문서를 저장할 파일 이름

risks = load_json("config/automation_risks.json")                                          # 자동 조치마다 적은 위험 파일을 리스트로 읽는다
print("--- 단계 1: 불러온 자동 조치", len(risks), "개")                                    # 단계 1 시작을 알리는 줄

table = make_risk_table(risks)                                                             # 표로 바꾸고 점수 열을 더한다
# ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
# 8. assess_risks(table) 의 결과를 rows 에 담는다
print("--- 단계 2: 점수가 큰 조치부터")                                                    # 단계 2 시작을 알리는 줄
gap_count = 0                                                                              # 빠진 통제가 있는 조치 수 : 처음에는 0
for row in rows:                                                                           # 평가 결과를 하나씩 꺼낸다
    print(row["action"], "· 점수", row["score"], "·", row["level"], "· 빠진 통제", row["missing"])  # 조치 한 줄을 출력한다
    if row["missing"] != []:                                                               # 빠진 통제가 있으면
        # 9. gap_count 에 gap_count + 1 을 담는다 (1 늘린다)

lines = make_assessment_lines(rows)                                                        # 문서의 줄 리스트를 만든다
text = "\n".join(lines) + "\n"                                                             # 줄 리스트를 줄바꿈으로 이어 한 문자열로 만든다
with open(DOC_PATH, "w", encoding="utf-8") as doc_file:                                    # 문서 파일을 쓰기 모드("w")로 연다
    doc_file.write(text)                                                                   # 문서 문자열을 파일에 쓴다
print("--- 단계 3: 바로 보완할 조치", gap_count, "개 ·", DOC_PATH, len(lines), "줄 저장")  # 단계 3 시작을 알리는 줄
```

**순서**

1. **[터미널]** 판다스를 설치합니다(맥북은 `python3`). 이미 설치했다면 바로 다음 줄로 갑니다.
   ```bash
   python -m pip install pandas
   ```
   - 터미널 맨 앞에 가상환경 이름(예: `(.venv)`)이 보이는 상태에서 칩니다. 도전 4-3 에서 설치했다면 건너뜁니다.
2. **[VS Code]** 파일 세 개를 만듭니다. `config` 폴더를 오른쪽 클릭 › **New File** 로 `automation_risks.json` 을, `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `risk_assessment.py` · `challenge4-4_run.py` 를 만들고, 각각 코드 상자의 내용을 붙여 넣고 저장합니다.
3. **[VS Code]** `risk_assessment.py` 1 ~ 7번, `challenge4-4_run.py` 8 · 9번을 씁니다. 막히면 아래 「도전 4-4 정리」를 봅니다.
4. **[터미널]** <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python challenge4-4_run.py
   ```
5. 출력은 세 단계입니다. 제목 줄은 줄 수에 넣지 않습니다.
   - 단계 1 과 단계 3 은 숫자가 제목 줄에 함께 나와 그 아래 줄이 없습니다.
   - 단계 2 는 조치 6개가 한 줄씩, 모두 6줄입니다.
6. **[VS Code]** 왼쪽 목록에서 `risk_assessment.md` 를 열고 `Ctrl+Shift+V`(맥북은 `Cmd+Shift+V`)로 마크다운 미리보기에서 표 모양을 확인합니다. <mark style="background:#bde3ff">표 한 개와 「바로 보완할 조치」 절이 보이면</mark> 됩니다.
7. **[보고서]** `report_u4.md` 의 `## 도전 4-4` 아래를 채웁니다(보고서 파일은 「보고서 쓰기」 레슨에서 만듭니다).
   - (가) 실행한 출력 전체를 붙여 넣고, 등급이 높음인 조치와 바로 보완할 조치 2개를 적어 주세요.
   - (나) [핵심 질문] 계정 잠금 · 세션 종료 · IP 차단은 점수가 모두 6(높음)인데, 세션 종료만 통제 갭이 있습니다. `config/automation_risks.json` 의 `controls` 를 근거로 그 이유를 적고, 세션 종료에 예방 통제인 승인 게이트가 특히 필요한 이유를 Unit 3 에 있는 되돌리기(교정 통제)와 연결해 적어 주세요.
   - (다) [핵심 질문] 담당자 알림은 영향도가 1인데 등급이 보통입니다. 점수 계산을 근거로 그 이유를 적고, 탐지 통제인 감사 기록이 없으면 사고가 난 뒤 무엇을 확인할 수 없는지 적어 주세요.

## 도전 4-4 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 두 열을 곱해 위험 점수 열 만들기 | `table["score"] = table["impact"] * table["likelihood"]` |
| 점수가 기준 이상이면 등급 문자열 리턴 | `if score >= 6:` → `return "높음"` |
| 필수 통제가 없으면 빠진 통제 리스트에 추가 | `if control not in controls:` → `missing.append(control)` |
| 위험 점수가 큰 순서로 정렬 | `sorted_table = table.sort_values("score", ascending=False)` |
| 함수 결과를 변수에 저장하기 | `missing = find_missing_controls(level, row["controls"])` |
| 빠진 통제가 있는 조치 수를 1 늘리기 | `gap_count = gap_count + 1` |

---
