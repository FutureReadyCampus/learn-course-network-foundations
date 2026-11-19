---
id: m5-u09-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/132_day05_pm_risk_check.md
  mission_id: GichanSource.m5-1113-pm-risk-check
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 리스크 평가와 자동 점검

<mark style="background:#e0d4ff">Unit 8에서 리포트 · 승인 게이트 · 오탐 복구를 만들었습니다.</mark> Unit 9에서는 두 가지를 합니다. 하나는 **자동 조치를 운영에 적용하기 전에 위험을 평가한 문서**를 쓰는 일입니다. 다른 하나는 **Unit 8까지 만든 기능이 강의계획서의 평가 기준을 만족하는지 자동 점검으로 한 번에 확인**하는 일입니다.

- **실습 9-1**: 자동 조치 6가지마다 영향도(impact, 잘못 실행됐을 때 피해의 크기) × 발생 가능성(likelihood, 잘못 실행될 가능성)으로 위험 점수를 계산하고 등급을 나눕니다. 그다음 등급별로 필요한 통제(control, 컨트롤: 잘못된 실행을 막거나 피해를 줄이거나 나중에 확인하게 하는 장치)가 갖춰져 있는지 비교합니다. 이 비교를 **통제 갭 분석**(control gap analysis, 컨트롤 갭 애널리시스: 있어야 할 통제와 지금 있는 통제를 비교해 빠진 것을 찾는 일)이라고 합니다. 이렇게 빠진 통제를 찾아 `risk_assessment.md` 를 씁니다(`risk_assessment.py`).
- **실습 9-2**: 세 가지를 **자동 점검**(automated check, 오토메이티드 체크: 사람이 출력을 읽는 대신 프로그램이 기대한 결과와 실제 결과를 비교하는 방식)으로 한 번에 확인합니다. 세 가지는 리포트 반영, 자동 처리와 승인 요청의 분기, 오탐 복구입니다. 확인 결과로 `unit09_checklist.md` 를 쓰고(`unit09_check.py`), 이번 Unit에서 만든 것을 깃허브에 올립니다.

새 문법은 없습니다. 실습 9-1에서 판다스(pandas, 판다스: 표 모양 데이터를 다루는 파이썬 도구) 표(DataFrame, 데이터프레임)의 두 열(column, 컬럼: 표의 세로 줄) 값을 곱해 새 열을 만드는 일은, <mark style="background:#e0d4ff">Unit 8의 실습 8-1에서 두 열 값을 빼서 새 열을 만든 일</mark>과 같은 모양입니다. 정렬 `sort_values(ascending=False)` 는 <mark style="background:#e0d4ff">Module 4에서 배웠습니다</mark>. 여기서는 표(DataFrame)라서 기준이 되는 열 이름 `"score"` 를 앞에 하나 더 씁니다. 보고서의 [핵심 질문] 표시가 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 들여쓰기(줄 앞의 빈칸)는 각 번호 주석과 같은 위치에서 시작합니다. 각 번호 주석 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

 **이전 파일**: <mark style="background:#e0d4ff">실습 9-1에서는 Unit 1의 `incident.py` 만 가져와 사용(import)합니다.</mark> <mark style="background:#e0d4ff">실습 9-2에서는 Unit 8에서 만든 코드 파일 `report.py` · `approval_gate.py` · `false_positive.py` 를 가져와 사용(import)합니다.</mark> Unit 8의 데이터 파일(`unit10_tickets.json` · `unit10_actions.json` · `config/approval_policy.json` · `fp_state.json` · `fp_log.json` · `fp_reports.json`), Unit 8의 실습 8-1에서 만든 `incident_report_20261112.md` 를 씁니다. `false_positive.py` 가 부르는 Unit 5 파일(`rollback.py` 등)도 같은 폴더에 있어야 합니다.

없는 파일은 Unit 8 레슨의 코드 상자에서 복사해 만듭니다. 코드 파일(`report.py` · `approval_gate.py` · `false_positive.py`)과 실행 파일은 Unit 8 의 실습 8-1 · 8-2 · 8-3 레슨과 「정답」 레슨에, 데이터 파일은 실습 8-1 · 8-2 · 8-3 레슨에 있습니다. `incident.py` 와 Unit 5 파일은 Unit 8 의 「시작하기」 레슨에 있는 「이전 파일이 없을 때」 코드 상자로 만듭니다. 리포트 파일이 없으면 Unit 8 의 `exercise8-1_run.py` 를 한 번 실행하면 생깁니다.

## 폴더 열고 파일 준비하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `soar_response` 폴더로 들어가 Unit 8 파일을 확인합니다. <mark style="background:#bde3ff">`ls` 결과에 `report.py` · `approval_gate.py` · `false_positive.py` · `incident_report_20261112.md` 가 보이면</mark> 됩니다. `incident_report_20261112.md` 가 없으면 Unit 8 의 `exercise8-1_run.py` 를 같은 폴더에 새 파일로 붙여 넣고 실행해서 만듭니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 답을 적는 **보고서**(`report_u9.md`)도 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다. 파일은 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고 파일 이름을 그대로 적은 뒤, 코드 상자의 내용을 붙여 넣고 저장합니다(`Ctrl + S`, 맥북은 `Cmd + S`).
4. **[터미널]** Unit 8 파일을 불러올 수 있는지 확인합니다(맥북은 `python3`). <mark style="background:#bde3ff">`Unit 8 파일 불러오기 성공` 이 나와야</mark> 합니다.
   ```bash
   python -c "import report, approval_gate, false_positive; print('Unit 8 파일 불러오기 성공')"
   ```

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- <mark style="background:#ffc4d6">`ModuleNotFoundError: No module named 'report'`</mark> 처럼 Unit 8 파일 이름이 나오면 그 파일이 이 폴더에 없다는 뜻입니다. `No module named 'rollback'` 은 <mark style="background:#e0d4ff">Unit 5 파일</mark>이 없다는 뜻입니다. Unit 8 레슨의 코드 상자에서 복사하거나 Unit 8 의 「이전 파일이 없을 때」 코드 상자로 만듭니다. `No module named 'pandas'` 는 판다스(pandas, 판다스: 표 모양 데이터를 다루는 파이썬 도구)가 설치되어 있지 않다는 뜻입니다. 가상환경이 켜진 터미널에서 `pip install pandas`(판다스를 내려받아 설치하는 명령)를 입력합니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 실행할 때마다 같은 입력 파일에서 시작해 같은 결과가 나옵니다. 이런 성질을 재현성(reproducibility, 리프로듀서빌리티: 같은 조건에서 다시 실행하면 같은 결과가 나오는 성질)이라고 합니다.

---
