---
id: m3-u05-l09
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## Unit 5 마무리

하루를 닫는 마무리입니다(15분). 실습 5-1 · 5-2와 글쓰기를 끝낸 뒤 합니다.

**1. 오늘 한 일 확인**

1. 퇴사자 계정 · 만료 예외 · 부서와 역할을 점검해 통과와 실패를 가렸다 (실습 5-1)
2. 제공 파일로 점검 결과와 일주일 치 로그를 합쳐 주간 보고서 파일을 만들었다 (제공 파일)
3. 상황 3 ~ 8 중 2개 이상의 원인과 고치는 방법을 내 말로 정리해 Module 3 총정리를 썼다 (실습 5-2)
4. 보고서 `report_u5.md` 의 꼭 채울 칸(실습 5-1 (가) · (나), 실습 5-2 상황 2개 · (가))이 비어 있지 않다
5. 응용 5-1을 했다면 직접 쓴 `log_summary.py` 로 `weekly_run.py` 를 다시 돌려도 보고서가 같다 (여유가 되면)

**2. 파일 확인** — **[터미널]** `access_control` 폴더에서 확인합니다.

```bash
ls
ls config
```

- 이번 Unit에서 만든 파일 `checklist.py` · `exercise5-1_run.py` · `log_summary.py` · `weekly_report.py` · `weekly_run.py` · `week_log.jsonl` · `access_control_weekly_report_2026-11-02.md` · `report_u5.md` 가 보여야 합니다. 응용 5-1을 했다면 `apply5-1_run.py` 도 있습니다.
- `config` 안에는 이번 Unit의 `week_state.json` · `alert.json` 이 보여야 합니다. 앞 Unit에서 만든 JSON 파일도 함께 보입니다.
- Module 3의 파일은 이렇게 둡니다. 파일을 어디에 저장했는지 헷갈리면 이 규칙과 VS Code 왼쪽 목록을 비교합니다.

| 위치 | 두는 파일 |
|---|---|
| `config/` | JSON 설정 파일만(이름이 `config/…` 로 시작하는 파일) |
| `access_control/` | 그 밖의 파일 모두(폴더 바로 아래) |
| 하위 폴더 | 따로 만들지 않음 |

- 그 밖의 파일은 코드 `.py`, 실행 파일 `exerciseN-M_run.py` · `applyN-M_run.py`, 보고서 `report_uN.md`, 실행하면 생기는 파일입니다.
- `__pycache__/` 는 파이썬이 자동으로 만드는 임시 폴더라 신경 쓰지 않습니다.

```
network-study-notes/
  access_control/          Module 3
    config/
      week_state.json
      alert.json
      (앞 Unit의 JSON 파일들)
    checklist.py
    exercise5-1_run.py
    log_summary.py
    weekly_report.py
    weekly_run.py
    week_log.jsonl
    access_control_weekly_report_2026-11-02.md
    report_u5.md
    (앞 Unit의 파일들)
```

<!-- checklist -->
- [ ] `access_control` 폴더에서 `ls` · `ls config` 로 이번 Unit 파일이 모두 있는 것을 확인했다
<!-- /checklist -->

**3. 깃허브에 올리기** — 「오늘의 글 쓰기」 마지막 쪽에서 글을 올릴 때 `access_control` 폴더도 같은 저장소라서 함께 올라갑니다. 그 전에 먼저 올리고 싶으면 Unit 1 마무리의 「깃허브에 올리기」와 같은 순서(`git status` 로 `.env` 확인 → `git add .` → `git commit` → `git push`)로 올립니다.

**4. 이어지는 곳**

1. 여기까지가 Module 3입니다. 다음은 **Module 4 이상탐지**입니다.
2. Module 3은 요청이 들어오는 순간 「허용할까」를 판정했고, Module 4는 이미 쌓인 로그를 읽고 평소와 다른 일을 찾습니다.
3. 이번 Unit에서 해 본 「로그 한 줄을 읽고, 세고, 기준과 비교하는」 방식이 Module 4에서 로그를 분석할 때의 바탕이 됩니다.

**확인** — `ls` 에 위 파일들이 보이고, 「오늘 한 일 확인」의 1 ~ 4번에 모두 「했다」고 답할 수 있으면 Unit 5와 Module 3을 마친 것입니다. 빠진 파일이 있으면 그 파일을 만드는 레슨(실습 5-1 · 제공 파일 · 보고서 쓰기)으로 돌아갑니다.
