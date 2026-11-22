---
id: m5-u04-l13
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개와 「보고서 쓰기」 · 「오늘의 글 쓰기」를 끝낸 뒤 합니다. 응용을 하지 않았어도 이것으로 이 Unit 이 끝납니다.

**1. 오늘 한 일 확인**

1. 조치 요청 8건을 위험 점수로 자동 · 승인 필요 · 차단 금지로 나눴다 (실습 4-1)
2. 오탐 신고 2건을 영향 확인 · 롤백 · 복구 확인 · 규칙 조정 제안까지 처리했다 (실습 4-2)
3. 보고서 `report_u4.md` 의 꼭 채울 세 칸(실습 4-1 (가) · 실습 4-2 (가) · 마무리 (가))에 `답:` 뒤가 비어 있지 않다

**2. 파일 확인** — **[터미널]** `soar_response` 폴더에서 확인합니다.

```bash
pwd
ls
ls config
```

아래 파일이 보여야 합니다.

| 어디에 | 종류 | 파일 |
|---|---|---|
| `soar_response` | 직접 만든 파일 | `approval_gate.py` · `exercise4-1_run.py` · `gate_requests.json` · `false_positive.py` · `exercise4-2_run.py` · `fp_state.json` · `fp_log.json` · `fp_reports.json` · `report_u4.md` |
| `soar_response` | 실행할 때 프로그램이 만든 결과 파일 | `gate_results.json` · `fp_results.json` · `fp_state_after.json` |
| `config` | 새로 만든 파일 | `approval_policy.json` |

결과 파일도 깃허브에 올라갑니다.

<!-- checklist optional -->
- [ ] `soar_response` 폴더에서 `ls` · `ls config` 로 표의 파일이 모두 있는 것을 확인했다
<!-- /checklist -->

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 메뉴 **Terminal › New Terminal** 로 터미널을 새로 엽니다(새 터미널은 `network-study-notes` 에서 열립니다. 이름 칸이 **bash** 가 아니면 오른쪽 위 **∨** 에서 **Git Bash** 를 고릅니다).
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark style="background:#ffc4d6">빨간 목록에 `.env`(API 키가 들어 있는 파일)나 `.venv`(가상환경 폴더)가 보이면 올리지 않고 멈춥니다.</mark>
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.

<!-- checklist optional -->
- [ ] `network-study-notes` 폴더에서 `git status` 를 쳐서 `.env` · `.venv` 가 없는 것을 확인했다
<!-- /checklist -->

3. **[보고서]** `report_u4.md` 의 `## 마무리` 아래 (가)를 채웁니다. 질문: 「`git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.」 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add approval gate and false positive rollback"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist optional -->
- [ ] `git add .` · `git commit` · `git push` 로 깃허브에 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소 `network-study-notes` 를 새로 고쳐 `soar_response` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.

<!-- checklist optional -->
- [ ] 깃허브 저장소의 `soar_response` 폴더에서 `approval_gate.py` · `false_positive.py` 를 확인했다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**4. 이어지는 곳**

1. 다음 Unit 5(통합 엔진과 최종 회고)에서는 지금까지 만든 플레이북 · 조치 · 티켓 · 승인 게이트를 엔진 하나로 연결합니다.
2. 오늘 만든 `approval_gate.py` 와 `config/approval_policy.json` 은 Unit 5 실습 5-1 · 5-2 에서 그대로 가져와 씁니다.

**확인** — 깃허브 저장소의 `soar_response` 폴더에 `approval_gate.py` 와 `false_positive.py` 가 보이고 `git status` 가 `nothing to commit` 으로 끝나면 성공입니다. 안 보이면 위 3번의 `git push` 출력에 `rejected` 나 오류가 있었는지 보고, 있으면 그 줄의 안내대로 다시 올립니다.
