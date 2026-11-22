---
id: m4-u04-l11
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개를 끝낸 뒤 합니다. 응용을 하지 않았어도 이 순서대로 마무리하면 됩니다.

**1. 오늘 한 일 확인**

1. 탐지된 규칙 8건((대상, 규칙) 쌍)에 점수를 더해 대상 5개를 high · mid · low 로 나누고, 점수 · 등급 · 이유를 `unit05_risk_scores.json` 에 저장했다 (실습 4-1)
2. 믿는 IP 예외 규칙으로 오탐을 4개에서 2개로 줄이고, 빠진 알림 중 진짜 문제가 0개임을 확인했다 (실습 4-2)
3. 보고서 `report_u4.md` 의 실습 칸 네 개(실습 4-1 (가) · (나), 실습 4-2 (가) · (나))에 `답:` 뒤가 비어 있지 않다. 다섯 번째 꼭 채울 칸인 마무리 (가)는 아래 「3. 깃허브에 올리기」의 3번에서 채웁니다

**2. 파일 확인** — **[터미널]** `anomaly_detection` 폴더에서 확인합니다.

```bash
pwd
ls
```

- `pwd` 의 결과가 `anomaly_detection` 으로 끝나야 합니다.
- `ls` 결과에 아래 파일이 보여야 합니다.

| 만든 곳 | 파일 |
|---|---|
| 제공 파일 | `saas_detection.py` · `malicious_detection.py` · `correlation.py` |
| 실습 4-1 | `risk_scores.py` · `exercise4-1_run.py` · `unit05_risk_scores.json` |
| 실습 4-2 | `review_alerts.json` · `tuning.py` · `exercise4-2_run.py` |
| 보고서 | `report_u4.md` |

- `unit05_risk_scores.json` 은 실습 4-1에서 프로그램이 만든 점수 파일입니다. 이것도 올라갑니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에서 `ls` 로 「2. 파일 확인」 표의 파일이 모두 있는 것을 확인했다
<!-- /checklist -->

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 메뉴 **Terminal › New Terminal** 로 터미널을 새로 엽니다(이름 칸이 **bash** 인지 봅니다). 새 터미널은 `…/network-study-notes` 에서 열립니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `anomaly_detection/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git status` 를 보고, `.env` · `.venv` 가 올라가지 않게 했다
<!-- /checklist -->

3. **[보고서]** `report_u4.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add anomaly detection unit 4 risk scores and false alarm tuning"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `git add .` · `git commit` · `git push` 로 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소 `network-study-notes` 를 새로 고쳐 `anomaly_detection` 폴더를 열고, 「2. 파일 확인」 표의 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.

<!-- checklist -->
- [ ] 깃허브의 `network-study-notes` 저장소 `anomaly_detection` 폴더에서 「2. 파일 확인」 표의 파일을 확인했다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 「2. 파일 확인」부터 「3. 깃허브에 올리기」의 4번(`git add .` · `git commit` · `git push`)까지를 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**확인** — 깃허브의 `anomaly_detection` 폴더에 「2. 파일 확인」 표의 파일이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이는 파일이 있으면 `git status` 를 다시 쳐서 그 파일이 빨간 목록에 남아 있는지 보고 「3. 깃허브에 올리기」의 4번을 다시 합니다.

**4. 이어지는 곳**

1. 다음 Unit 5(AI 요약과 총정리)에서는 오늘 저장한 점수 파일의 사실만 골라 AI 에게 요약을 받고, 상황별 원인과 해결법을 정리합니다.
2. Unit 5 시작하기 레슨에서 `unit05_risk_scores.json` 을 같은 내용으로 다시 만들기 때문에, 오늘 파일이 달라도 다음 Unit은 그대로 따라갈 수 있습니다.
