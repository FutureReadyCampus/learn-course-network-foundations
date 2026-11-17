---
id: m5-u09-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/132_day05_pm_risk_check.md
  mission_id: GichanSource.m5-1113-pm-risk-check
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

아래 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark> 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.

---

## Exercise 9-1 정답

 **터미널에 입력합니다.**

```bash
pwd
python day05_5-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`risk_assessment.py` 의 1 ~ 7번입니다.

```python
    # 1. table["impact"] * table["likelihood"] 를 table["score"] 에 담는다 (위험 점수)
    table["score"] = table["impact"] * table["likelihood"]       # 두 열을 곱해 위험 점수 열을 만든다
    # 2. score 가 6 이상이면 (if, >=)
    if score >= 6:                                               # 6 이상이면
        # 3. "높음" 을 리턴한다
        return "높음"                                            # 높음을 리턴한다
        # 4. control 이 controls 안에 없으면 (if, not in)
        if control not in controls:                              # 지금 있는 통제에 없으면
            # 5. missing 에 control 을 추가한다 (append)
            missing.append(control)                              # 빠진 통제를 추가한다
    # 6. table.sort_values("score", ascending=False) 를 sorted_table 에 담는다 (점수가 큰 것부터)
    sorted_table = table.sort_values("score", ascending=False)   # 점수가 큰 행부터 정렬한다
        # 7. find_missing_controls(level, row["controls"]) 의 결과를 missing 에 담는다
        missing = find_missing_controls(level, row["controls"])  # 이 등급에 빠진 통제를 찾는다
```

`day05_5-1_run.py` 의 8 · 9번입니다.

```python
# 8. assess_risks(table) 의 결과를 rows 에 담는다
rows = assess_risks(table)         # 점수가 큰 것부터 등급과 빠진 통제를 붙인다
        # 9. gap_count 에 gap_count + 1 을 담는다 (1 늘린다)
        gap_count = gap_count + 1  # 빠진 통제가 있는 조치 수를 1 늘린다
```

**결과**

- (가) 출력은 다음과 같습니다. 높음은 <mark style="background:#bde3ff">**계정 잠금 · 세션 종료 · IP 차단**</mark>이고, 바로 보완할 조치는 <mark style="background:#bde3ff">**세션 종료(승인 게이트) · 담당자 알림(감사 기록)**</mark>입니다. 이 결과는 샘플의 통제 목록을 기준으로 산출한 검토 대상이므로, 실제 운영에서는 팀이 확인한 뒤 통제를 적용합니다.

```
--- 단계 1: 불러온 자동 조치 6 개
--- 단계 2: 점수가 큰 조치부터
계정 잠금 · 점수 6 · 높음 · 빠진 통제 []
세션 종료 · 점수 6 · 높음 · 빠진 통제 ['승인 게이트']
IP 차단 · 점수 6 · 높음 · 빠진 통제 []
담당자 알림 · 점수 3 · 보통 · 빠진 통제 ['감사 기록']
티켓 자동 작성 · 점수 2 · 낮음 · 빠진 통제 []
상급자 에스컬레이션 · 점수 2 · 낮음 · 빠진 통제 []
--- 단계 3: 바로 보완할 조치 2 개 · risk_assessment.md 16 줄 저장
```

리스크 평가 문서 `risk_assessment.md` 의 내용은 다음과 같습니다.

```
# 자동 대응 리스크 평가 — 2026-11-13(금)

- 점수 = 영향도(1~3) × 발생 가능성(1~3). 6 이상 높음, 3 이상 보통, 그 밖은 낮음

| 자동 조치 | 영향도 | 발생 가능성 | 점수 | 등급 | 지금 있는 통제 | 빠진 통제 |
|---|---|---|---|---|---|---|
| 계정 잠금 | 3 | 2 | 6 | 높음 | 승인 게이트, 되돌리기, 감사 기록, VIP 예외 | 없음 |
| 세션 종료 | 3 | 2 | 6 | 높음 | 감사 기록 | 승인 게이트 |
| IP 차단 | 3 | 2 | 6 | 높음 | 허용 목록, 승인 게이트, 자동 해제, 되돌리기, 감사 기록 | 없음 |
| 담당자 알림 | 1 | 3 | 3 | 보통 | 알림 간격, 재시도 | 감사 기록 |
| 티켓 자동 작성 | 1 | 2 | 2 | 낮음 | 병합, 감사 기록 | 없음 |
| 상급자 에스컬레이션 | 2 | 1 | 2 | 낮음 | 같은 단계 한 번 | 없음 |

## 바로 보완할 조치
- 세션 종료: 승인 게이트 추가
- 담당자 알림: 감사 기록 추가
```

- (나) 세 조치 모두 영향도 3 × 발생 가능성 2 = 6점으로 높음 등급이라, 필수 통제인 승인 게이트와 감사 기록이 있어야 합니다. 계정 잠금과 IP 차단의 `controls` 에는 둘 다 있지만, 세션 종료에는 <mark style="background:#bde3ff">`감사 기록`</mark> 하나뿐이라 <mark style="background:#ffc4d6">승인 게이트가 빠진 통제 갭이 생깁니다.</mark>
  - <mark style="background:#e0d4ff">수요일의 `rollback_incident`</mark> 는 세션 종료를 「되돌리기 불가」로 남깁니다. 잘못 실행된 뒤에는 교정 통제(되돌리기)를 쓸 수 없으니, <mark>실행하기 전에 막는 예방 통제인 승인 게이트</mark>가 더 중요합니다.
- (다) 점수는 영향도 1 × 발생 가능성 3 = <mark style="background:#bde3ff">3점</mark>이라 보통 등급입니다. 보통의 기준은 <mark style="background:#ffdcb0">3 이상 6 미만</mark>입니다. 피해(영향도)는 작아도 오탐 알림을 따로 제외하는 장치가 없다고 가정하므로 발생 가능성이 높기 때문입니다.
  - 탐지 통제인 감사 기록이 없으면 사고가 난 뒤 「어느 인시던트에 · 언제 · 어떤 알림을 보냈는지」를 확인할 수 없습니다. 받는 사람까지 알려면 기록에 따로 적어야 합니다. 담당자가 알림을 받았는데 응답하지 않았는지, 알림이 아예 가지 않았는지도 <mark style="background:#ffc4d6">가릴 수 없습니다.</mark>

**왜**

- <mark>리스크 평가는 「어떤 자동 조치가 위험한지」(위험 점수)와 「그 위험을 줄이는 통제가 갖춰져 있는지」(통제 갭 분석)를 한 표로 보여 줍니다.</mark> 점수가 같아도 통제가 다르면 보완할 내용이 달라지므로, 점수와 빠진 통제를 함께 적습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 `score` 열이 없어서 6번의 정렬에서 오류가 납니다.

```
KeyError: 'score'
```

- 2번을 비워 두면 3번 줄이 바로 위 줄보다 오른쪽에서 시작해서(들여쓰기가 맞지 않아) 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- 2번에서 `>=` 대신 `>` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**점수 6인 조치가 모두 보통이 됩니다.**</mark> 점수가 기준값 6 과 같을 때 어긋나는 경계 조건 오류(off-by-one error)입니다. 세션 종료의 통제 갭이 사라지고, 보완할 조치가 1개로 줄어드는 것이 이 실수의 결과입니다.

```
계정 잠금 · 점수 6 · 보통 · 빠진 통제 []
세션 종료 · 점수 6 · 보통 · 빠진 통제 []
IP 차단 · 점수 6 · 보통 · 빠진 통제 []
--- 단계 3: 바로 보완할 조치 1 개 · risk_assessment.md 15 줄 저장
```

- 3번 · 5번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. 9번을 비워도 같은 오류가 납니다(문구는 파이썬 버전마다 조금 다릅니다).

```
IndentationError: expected an indented block
```

- 4번을 비워 두면 5번 줄이 `for` 바로 아래 줄이 되어 오류 없이 <mark style="background:#ffc4d6">**있어야 하는 통제가 모두 빠진 것으로 나옵니다.**</mark> 보완할 조치가 2개가 아니라 4개로 나오는 것이 이 실수의 결과입니다.

```
--- 단계 3: 바로 보완할 조치 4 개 · risk_assessment.md 18 줄 저장
```

- 6번을 비워 두면 `sorted_table` 이 만들어지지 않아 오류가 납니다. 7번 · 8번을 비워도 같은 꼴의 오류(`name 'missing'` · `name 'rows'`)가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'sorted_table' is not defined
```

- 6번에서 `ascending=False`(큰 값부터 정렬하라는 뜻)를 빠뜨리면 오류 없이 <mark style="background:#ffc4d6">**점수가 작은 조치부터 나옵니다.**</mark> 단계 2 의 첫 두 줄이 낮음으로 시작하는 것이 이 실수의 결과입니다.

```
티켓 자동 작성 · 점수 2 · 낮음 · 빠진 통제 []
상급자 에스컬레이션 · 점수 2 · 낮음 · 빠진 통제 []
```

**관제에서는**

- 보안 조직은 리스크 평가에서 영향도와 발생 가능성을 가로축과 세로축으로 놓고, 두 값이 만나는 곳마다 위험의 크기를 표시하는 표(**위험 매트릭스**, risk matrix, 리스크 매트릭스)를 자주 씁니다. 오늘은 같은 생각을 영향도 × 발생 가능성의 곱으로 단순하게 구현했습니다. <mark>자동 대응을 운영에 적용하기 전과 기준을 바꿀 때마다 다시 평가하고, 높음 등급 조치에는 승인 게이트(예방 통제) · 감사 기록(탐지 통제) 같은 통제를 두는 것이 일반적입니다.</mark> 통제를 적용한 뒤에도 남는 위험은 잔여 위험(residual risk)으로 따로 관리합니다. 오늘의 숫자 · 등급 기준 · 필요한 통제는 예시이고, 실제 값은 팀이 정합니다.

---

## Exercise 9-2 정답

 **터미널에 입력합니다.**

```bash
pwd
python day05_6-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예)

`day4_check.py` 의 1 ~ 7번입니다.

```python
        # 1. number 가 report_text 안에 없으면 (if, not in)
        if number not in report_text:                             # 리포트에 그 번호가 없으면
            # 2. not_found 에 number 를 추가한다 (append)
            not_found.append(number)                              # 없는 번호를 추가한다
        # 3. decide_gate(case["request"], policy) 의 두 결과를 decision, reasons 에 담는다
        decision, reasons = decide_gate(case["request"], policy)  # 결정과 이유를 함께 받는다
        # 4. decision 이 case["expected"] 와 다르면 (if, !=)
        if decision != case["expected"]:                          # 기대한 결정과 다르면
        # 5. result["in_time"] 이 False 이면 (if not)
        if not result["in_time"]:                                 # 정한 시간 안에 끝나지 않았으면
        # 6. user 가 state["locked_users"] 안에 없으면 (if, not in)
        if user not in state["locked_users"]:                     # 진짜 공격 계정이 잠겨 있지 않으면
            # 7. problems 에 user + " 잠금이 풀림" 을 추가한다 (append)
            problems.append(user + " 잠금이 풀림")                # 문제를 추가한다
```

4 · 5번은 `if` 만 쓰고 `if` 안에 들어가는 줄은 미리 채운 줄이니, 완성된 모양을 함께 봅니다.

**전체 모양 — `check_gate`**

```python
def check_gate(cases, policy):                                    # 시험 사례 리스트와 승인 정책을 받는 함수
    """시험 사례마다 승인 게이트를 실행해, 결정이 기대한 결정과 다른 사례의 이름을 리스트로 리턴한다.
    승인 기준을 바꾼 뒤에도 자동 · 승인 필요 · 차단 금지가 맞게 나뉘는지 확인할 때 쓴다.
    """
    wrong = []                                                    # 기대와 다른 사례를 모을 빈 리스트 — 미리 채운 줄
    for case in cases:                                            # 시험 사례를 하나씩 꺼낸다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        decision, reasons = decide_gate(case["request"], policy)  # 결정과 이유를 함께 받는다
        if decision != case["expected"]:                          # 기대한 결정과 다르면
            wrong.append(case["case"] + " (기대 " + case["expected"] + ", 결과 " + decision + ")")  # 사례 이름과 두 결정을 추가한다 — 미리 채운 줄
    return wrong                                                  # 기대와 다른 사례 리스트를 리턴한다 — 미리 채운 줄
```

**전체 모양 — `check_recovery`**

```python
def check_recovery(results, state, true_positive_users):         # 오탐 처리 결과 · 처리 뒤 상태 · 진짜 공격 계정 리스트를 받는 함수
    """오탐 처리 결과에서 남은 대상 · 시간 초과를 찾고, 진짜 공격 계정이 풀렸는지도 확인해 문제 문장 리스트를 리턴한다.
    오탐 복구가 신속하고 완전했는지, 진짜 공격의 조치는 그대로인지 확인할 때 쓴다.
    """
    problems = []                                                # 문제 문장을 모을 빈 리스트 — 미리 채운 줄
    for result in results:                                       # 오탐 처리 결과를 하나씩 꺼낸다 — 미리 채운 줄
        if result["remaining"] != []:                            # 아직 복구되지 않은 대상이 있으면 — 미리 채운 줄
            problems.append(result["incident"] + " 복구 안 됨")  # 문제를 추가한다 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        if not result["in_time"]:                                # 정한 시간 안에 끝나지 않았으면
            problems.append(result["incident"] + " 30분 넘음")   # 문제를 추가한다 — 미리 채운 줄
    for user in true_positive_users:                             # 진짜 공격 계정을 하나씩 꺼낸다 — 미리 채운 줄
        if user not in state["locked_users"]:                    # 진짜 공격 계정이 잠겨 있지 않으면
            problems.append(user + " 잠금이 풀림")               # 문제를 추가한다
    return problems                                              # 문제 문장 리스트를 리턴한다 — 미리 채운 줄
```

`day05_6-1_run.py` 의 8 · 9번입니다.

```python
# 8. check_report(report_text, tickets, actions) 의 결과를 report_problems 에 담는다
report_problems = check_report(report_text, tickets, actions)            # 리포트에 빠진 번호를 찾는다
# 9. check_recovery(results, state, TRUE_POSITIVE_USERS) 의 결과를 recovery_problems 에 담는다
recovery_problems = check_recovery(results, state, TRUE_POSITIVE_USERS)  # 오탐 복구의 문제를 찾는다
```

**결과**

- (가) 출력은 다음과 같습니다. 세 기준 모두 <mark style="background:#bde3ff">**통과**</mark>이고, `day4_checklist.md` 는 <mark style="background:#bde3ff">**5줄**</mark>입니다.

```
--- 단계 1: 점검 재료 · 티켓 7 장 · 조치 기록 10 건 · 시험 사례 7 개
--- 단계 2: Unit 9 점검 목록
[통과] ① 2 · 3일 차 데이터가 리포트에 빠짐없이 들어갔다 · 문제 0 개
[통과] ② 위험 점수에 따라 자동 · 승인 필요 · 차단 금지가 맞게 나뉜다 · 문제 0 개
[통과] ③ 오탐 복구가 30분 안에 빠짐없이 끝났고 진짜 공격의 잠금은 그대로다 · 문제 0 개
--- 단계 3: day4_checklist.md 5 줄 저장
```

점검 목록 `day4_checklist.md` 의 내용은 다음과 같습니다.

```
# Unit 9 마무리 점검 — 2026-11-13(금)

- [통과] ① 2 · 3일 차 데이터가 리포트에 빠짐없이 들어갔다
- [통과] ② 위험 점수에 따라 자동 · 승인 필요 · 차단 금지가 맞게 나뉜다
- [통과] ③ 오탐 복구가 30분 안에 빠짐없이 끝났고 진짜 공격의 잠금은 그대로다
```

- (나) 「대상 3개」는 등급 `mid`(중간)가 주는 1점만 있어 <mark style="background:#bde3ff">1점 · 자동</mark>이고, 「대상 4개」는 mid 1점 + 대상 수 2점으로 <mark style="background:#bde3ff">3점 · 승인 필요</mark>입니다.
  - <mark style="background:#ffdcb0">기준이 「3개 넘음(`>`)」</mark>인데 코드가 「3개 이상(`>=`)」으로 바뀌면(경계 조건 오류), 대상 3개 사례가 승인 필요로 바뀌어 <mark style="background:#ffc4d6">점검이 바로 「확인 필요」를 냅니다.</mark> 경계값의 양쪽(안쪽과 바깥쪽)을 함께 포함해야 이런 실수를 검출합니다.
- (다) <mark style="background:#e0d4ff">`rollback_incident`</mark> 가 신고된 인시던트가 아닌 기록까지 되돌리면 <mark style="background:#ffc4d6">정탐(진짜 공격)인 `dami` 의 잠금이 풀릴 수 있습니다.</mark> 남은 대상과 시간만 확인하면 오탐 복구가 「통과」로 보일 수 있으므로, 정탐 계정의 잠금이 그대로인지도 따로 확인해야 이 실수를 놓치지 않습니다.

**왜**

- <mark>자동 점검은 「기대한 결과」를 미리 적어 두고 실제 결과와 비교합니다.</mark> 기준 숫자나 코드를 바꾼 뒤 한 번 실행하면(회귀 시험), 사람이 출력을 다시 읽지 않아도 어디가 잘못됐는지 알 수 있습니다.

**자주 틀리는 곳**

아래 결과는 해당 번호의 줄을 지우고 실행한 것입니다.

- 1번을 비워 두면 2번 줄이 `for` 바로 아래 줄이 되어 오류 없이 <mark style="background:#ffc4d6">**있어야 할 번호가 모두 「없음」으로 나옵니다.**</mark> ① 이 「확인 필요 · 문제 8 개」로 나오는 것이 이 실수의 결과입니다(아래는 앞 세 줄).

```
[확인 필요] ① 2 · 3일 차 데이터가 리포트에 빠짐없이 들어갔다 · 문제 8 개
   - TCK-1
   - TCK-2
```

- 2번을 비워 두면 `if` 아래에 실행할 줄이 없어 실행하기 전에 멈춥니다. 7번을 비워도 같은 오류가 납니다(문구는 파이썬 버전마다 조금 다릅니다).

```
IndentationError: expected an indented block
```

- 3번을 비워 두면 `decision` 이 만들어지지 않아 오류가 납니다. 8번 · 9번을 비워도 같은 꼴의 오류(`name 'report_problems'` · `name 'recovery_problems'`)가 납니다. 파이썬 버전에 따라 뒤에 `Did you mean: …` 이 더 붙을 수 있습니다.

```
NameError: name 'decision' is not defined
```

- 4번을 비워 두면 미리 채운 `wrong.append(…)` 줄이 바로 위 줄보다 오른쪽에서 시작해서(들여쓰기가 맞지 않아) 실행하기 전에 멈춥니다.

```
IndentationError: unexpected indent
```

- 4번에서 `!=` 대신 `==` 를 쓰면 오류 없이 <mark style="background:#ffc4d6">**맞게 나온 사례가 모두 문제로 나옵니다.**</mark> ② 가 「확인 필요 · 문제 7 개」로 나오는 것이 이 실수의 결과입니다(아래는 앞 두 줄).

```
[확인 필요] ② 위험 점수에 따라 자동 · 승인 필요 · 차단 금지가 맞게 나뉜다 · 문제 7 개
   - high 등급 한 명 (기대 자동, 결과 자동)
```

- 5번을 비워 두면 오류는 나지 않고 출력도 정답과 같습니다. 아래 `problems.append(…)` 줄이 위 `if` 안으로 들어가서, <mark style="background:#ffc4d6">**30분을 넘긴 복구를 찾지 못합니다.**</mark> 오늘 샘플은 두 신고 모두 30분 안이라 차이가 보이지 않으니, 출력이 맞아도 코드를 다시 읽어 확인합니다.
- 6번을 비워 두면 7번 줄이 `for` 바로 아래 줄이 되어 오류 없이 <mark style="background:#ffc4d6">**잠겨 있는 `dami` 도 「잠금이 풀림」으로 나옵니다.**</mark>

```
[확인 필요] ③ 오탐 복구가 30분 안에 빠짐없이 끝났고 진짜 공격의 잠금은 그대로다 · 문제 1 개
   - dami 잠금이 풀림
```

**관제에서는**

- 대응 절차와 자동 대응 규칙은 바꿀 때마다 시험 사례를 다시 실행해(회귀 시험) 확인합니다. <mark>기대한 결과를 적은 시험 사례를 경계값까지 포함해 계속 추가해 두면, 기준을 바꾼 뒤 무엇이 달라졌는지 바로 알 수 있습니다.</mark> 오늘의 사례 7개와 점검 세 가지는 예시입니다.
