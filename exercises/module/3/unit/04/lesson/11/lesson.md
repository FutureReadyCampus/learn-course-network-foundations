---
id: m3-u04-l11
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개와 「오늘의 글 쓰기」를 마친 뒤 합니다.

**1. 오늘 한 일 확인**

1. 민감한 권한이거나 영향이 2건 이상인 계획을 가려 승인 상태를 적었다 (실습 4-1)
2. 승인 대기가 아닌 계획만 실행하고, 회수 전후의 판정을 비교했다 (실습 4-2)
3. 회수 이력 `revocation_log.json` 을 저장하고 다시 읽어 건수를 확인했다 (실습 4-2)
4. 보고서 `report_u4.md` 의 실습 4-1 · 4-2 칸에 `답:` 뒤가 비어 있는 질문이 없다

**2. 파일 확인** — **[터미널]** `access_control` 폴더에서 확인합니다.

```bash
ls
ls config
```

- `revoke_input.py` · `revoke_plan.py` · `revoke_approve.py` · `revoke.py` · `exercise4-1_run.py` · `exercise4-2_run.py` · `revocation_log.json` · `report_u4.md` 가 보여야 합니다.
- `config` 안에는 `sensitive.json` 이 새로 보여야 합니다.

<!-- checklist -->
- [ ] 「2. 파일 확인」에서 오늘 만든 파일과 `config/sensitive.json` 이 모두 보였다
<!-- /checklist -->

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다. 이미 `pwd` 가 `…/network-study-notes` 로 끝나면 `cd ..` 는 건너뜁니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 도 같은 방법으로 합니다.
   - `access_control/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.
   - `access_control/revocation_log.json` 은 실습 4-2에서 프로그램이 만든 회수 이력입니다. 이것도 올라갑니다.
3. **[보고서]** `report_u4.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add access control unit 4 revocation approval, execution and log"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git status` 로 `.env` · `.venv` 가 없는 것을 확인하고 `git add` · `git commit` · `git push` 로 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `access_control` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다.

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.
- 올린 뒤 응용을 하러 가면 먼저 `cd access_control` 로 작업 폴더에 돌아옵니다.

> **확인** — 깃허브의 `access_control` 폴더에 `revoke_approve.py` · `revoke.py` · `revocation_log.json` · `report_u4.md` 가 보이면 성공입니다. 안 보이면 `git status` 를 다시 쳐서 빨간 목록이 남았는지 보고, 남았으면 4번을 다시 합니다.

<!-- checklist -->
- [ ] 깃허브의 `access_control` 폴더에서 `revoke_approve.py` · `revoke.py` · `revocation_log.json` · `report_u4.md` 를 확인했다
<!-- /checklist -->

**4. 이어지는 곳**

1. 다음 Unit 5(결과 보고하기)에서는 점검 체크리스트로 어긋난 곳을 찾고, 상황별 원인과 해결법을 정리합니다.
2. 오늘 만든 `revoke_approve.py` · `revoke.py` 와 `revocation_log.json` 은 Unit 5 실습 5-2(상황별 원인과 해결법)에서 다시 봅니다.
