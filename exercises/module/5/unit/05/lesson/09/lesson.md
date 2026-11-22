---
id: m5-u05-l09
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

**지금은 이 페이지를 건너뛰고, 「보고서 쓰기」(레슨 07)와 「오늘의 글 쓰기」(레슨 08)를 마친 뒤 돌아와서 합니다.** 하루를 닫는 마무리입니다(15분). 이번 Unit은 Module 5의 마지막이라, 오늘 올리면 Module 5에서 만든 SOAR 모듈과 엔진 · 점검 · 회고 문서가 모두 저장소에 남습니다.

**1. 오늘 한 일 확인**

1. 알림 8건을 승인 게이트를 거쳐 조치하고 티켓을 남기며, 오류가 난 알림은 실패로 격리하는 통합 엔진을 만들었다 (실습 5-1)
2. 엔진 로그 세 개를 정책 네 가지로 점검해 FAIL 2개가 `gate_off_log.json` 에서 나오는 것을 확인했다 (실습 5-2)
3. 최종 회고 문서 `unit10_final_retrospective.md` 에 `…` 가 남은 칸이 없다 (실습 5-2)
4. 보고서 `report_u5.md` 의 꼭 채울 다섯 칸(5-1 (가) · (나), 5-2 (가) · (나), 마무리 (가))에 `답:` 뒤가 비어 있지 않다

**강의계획서 평가 기준 확인**

| 기준 | 확인할 곳 |
|---|---|
| Module 4 탐지 결과부터 Module 5 대응까지 오류 없이 이어진다 | `risk_engine_log.json`: Module 4 5건 → 자동 실행 2 · 조치 없음 3 · 실패 0 (응용 5-1을 하지 않았으면 제공 파일로 결과만 확인합니다. 직접 잇는 것은 응용 5-1에서 합니다) |
| 승인 게이트가 위험도에 따라 정확히 작동한다 | 실습 5-1 단계 2 · 3, 실습 5-2 점검 ① |
| 모듈이 서로 이어져 하나의 흐름으로 동작한다 | `soar_engine.py` 의 `import` 6줄, 회고 문서 1절 |

- 첫 줄의 연결을 직접 만들어 보려면 응용 5-1(여유가 되면)을 합니다. 응용 5-1 단계 3 ~ 5 가 같은 결과를 보여 줍니다.

**2. 파일 확인** — **[터미널]** `soar_response` 폴더에서 확인합니다.

```bash
pwd
ls
```

- `pwd` 결과가 `…/soar_response` 로 끝나야 합니다.
- `ls` 결과에 아래 파일이 보여야 합니다. 응용 5-1 줄은 응용을 했을 때만 보입니다.

| 만든 곳 | 보여야 할 파일 |
|---|---|
| 시작하기 | `engine_alerts.json` |
| 실습 5-1 | `soar_engine.py` · `exercise5-1_run.py` · `engine_log.json` · `engine_tickets.json` |
| 제공 파일 | `risk_engine_log.json` |
| 실습 5-2 | `gate_off_log.json` · `policy_check.py` · `exercise5-2_run.py` · `policy_check.json` · `unit10_final_retrospective.md` |
| 보고서 쓰기 | `report_u5.md` |
| 응용 5-1(여유가 되면) | `unit05_risk_scores.json` · `engine_input.py` · `apply5-1_run.py` · `engine_summary.json` · `risk_tickets.json` |

<!-- checklist -->
- [ ] `soar_response` 폴더에서 2번 표의 파일이 모두 있는 것을 확인했다
<!-- /checklist -->

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark style="background:#ffc4d6">빨간 목록에 `.env`(API 키가 들어 있는 파일)나 `.venv`(가상환경 폴더)가 보이면 올리지 않고 멈춥니다.</mark>
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git status` 를 실행해 `.env` · `.venv` 가 목록에 없는 것을 확인했다
<!-- /checklist -->

3. **[보고서]** `report_u5.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`). 세 명령을 하나씩 칩니다.
   ```bash
   git add .
   git commit -m "Add SOAR engine, policy check and Module 5 final retrospective"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `git add .` · `git commit` · `git push` 를 차례로 실행해 깃허브에 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소 `network-study-notes` 를 새로 고쳐 `soar_response` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.
   - 깃허브에 안 보이는 파일이 있으면 그 파일이 VS Code 왼쪽 목록의 `soar_response` 폴더 안에 있는지 봅니다. 다른 폴더에 만들었다면 `soar_response` 안으로 옮긴 뒤 2번의 `git status` 부터 다시 합니다.

<!-- checklist -->
- [ ] 깃허브의 `network-study-notes` 저장소 `soar_response` 폴더에서 오늘 만든 파일이 모두 보였다
<!-- /checklist -->

- 시간이 남아 응용 5-1을 했다면 응용 파일까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**확인** — 깃허브의 `soar_response` 폴더에 2번 표의 파일(응용 줄 빼고)이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이는 파일이 있으면 `git status` 를 다시 쳐서 그 파일이 빨간 목록에 남아 있는지 보고 4번을 다시 합니다.

**4. 이어지는 곳**

1. Module 5는 여기서 끝납니다. 플레이북 · 계정과 IP 조치 · 티켓 · 승인 게이트 · 통합 엔진이 `soar_response` 폴더에 모두 들어 있습니다.
2. 캡스톤에서는 회고 문서 3절에 적은 주제 · 설정 파일 · 내 파일로 시작합니다. 회고 문서 2절에 적은 깨질 곳은 캡스톤에서 먼저 막을 일의 목록이 됩니다.
