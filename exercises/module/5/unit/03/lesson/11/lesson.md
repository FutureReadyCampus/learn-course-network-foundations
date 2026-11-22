---
id: m5-u03-l11
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(25분). 핵심 실습 두 개를 끝낸 뒤 합니다.

**1. 오늘 한 일 확인**

1. 조치 기록을 거꾸로 읽어 자동이 바꾼 것만 되돌리고, 되돌릴 수 없는 세션 종료는 따로 표시했다 (실습 3-1)
2. 알림 11건으로 티켓을 만들고 응답 기한(SLA)을 계산했으며, 조치 확인에 실패한 건을 직접 확인 대상으로 표시했다 (실습 3-2)
3. 보고서 `report_u3.md` 의 [핵심 질문] 칸(실습 3-1 (가) · (나), 실습 3-2 (가) · (다))에 `답:` 뒤가 비어 있는 곳이 없다

**2. 제공 파일 만들기** — 「제공 파일」 레슨으로 가서 `ticket_merge.py` · `notifier.py` · `ticket_notice.py` 를 만들고 확인 명령까지 친 뒤 이 페이지로 돌아옵니다. 오늘 핵심 실습에는 쓰지 않지만, 응용 3-2 · 3-3과 Unit 4 응용에서 씁니다.

<!-- checklist -->
- [ ] 「제공 파일」 레슨에서 `ticket_merge.py` · `notifier.py` · `ticket_notice.py` 를 만들고 `제공 파일 정상 7` 을 확인했다
<!-- /checklist -->

**3. 파일 확인** — **[터미널]** `soar_response` 폴더에서 확인합니다.

```bash
pwd
ls
ls config
```

- `undo_actions.py` · `rollback.py` · `exercise3-1_run.py` · `ticketing.py` · `exercise3-2_run.py` · `ticket_merge.py` · `notifier.py` · `ticket_notice.py` · `alerts_thu.json` · `report_u3.md` 가 보여야 합니다.
- `config` 안에는 `escalation_rules.json` 이 새로 보여야 합니다.

**4. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 위쪽 메뉴 **Terminal › New Terminal** 로 터미널을 새로 엽니다. 새 터미널은 작업 폴더 `network-study-notes` 에서 열리므로 `cd` 는 필요 없습니다. 다시 `pwd` 로 확인합니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.
3. **[보고서]** `report_u3.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add SOAR unit 3 rollback and ticketing"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git status` 로 `.env` · `.venv` 가 없는 것을 보고 `git add` · `git commit` · `git push` 를 했다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소 `network-study-notes` 를 새로 고쳐 `soar_response` 폴더를 열고, 3번에서 본 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.

<!-- checklist -->
- [ ] 깃허브의 `network-study-notes` 저장소 `soar_response` 폴더에서 3번의 파일을 모두 확인했다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 3-3 끝의 「응용 파일 올리기」를 따라 한 번 더 올립니다. 같은 날 여러 번 올려도 괜찮습니다.

**5. 이어지는 곳**

1. 다음 Unit 4(승인 게이트와 오탐 되돌리기)의 실습 4-2는 오늘 만든 `rollback.py` 의 `rollback_incident` 로 오탐 신고를 처리합니다.
2. 오늘 만든 `ticketing.py` 의 `make_ticket` 은 Unit 5 실습 5-1 통합 엔진에서 티켓을 만들 때 다시 씁니다.
3. 오늘은 연습용 시스템에서 실행했습니다. <mark>실제 제품에서는 `account_actions.py` · `ip_actions.py` 안의 상태를 바꾸는 줄이 계정 · 방화벽 시스템에 실제로 명령을 보내는 코드로 바뀝니다.</mark> 기록을 남기고, 되돌릴지 정하고, 티켓을 만드는 코드는 그대로 씁니다.

> **확인** — 깃허브의 내 저장소 `soar_response` 폴더에 3번에서 본 파일이 모두 보이고 `.env` 는 보이지 않으면 성공입니다. 파일이 빠졌으면 4번 2의 `git status` 부터 다시 합니다.
