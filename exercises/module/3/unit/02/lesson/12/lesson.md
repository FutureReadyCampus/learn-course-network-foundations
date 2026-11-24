---
id: m3-u02-l12
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 권한 부여 준비를 마치고 기록을 마친 뒤 합니다. 응용은 하지 않아도 됩니다.

**1. 오늘 한 일 확인**

1. 요청을 요청서(딕셔너리)로 접수하고, 접수할 수 없는 요청 세 건을 이유와 함께 걸러 냈다 (실습 2-1)
2. 승인 · 반려가 검토 중인 요청서에만 되고, 본인 요청과 두 번째 처리는 막힌다 (실습 2-2)
3. 승인된 요청서에 예외 권한을 주는 `req_grant.py` 를 「권한 부여 준비」에서 복사해 두었다
4. 문제 해결 기록 `report_u2.md` 의 꼭 채울 네 칸 가운데 2-1 (가), 2-2 (가) · (나)에 `답:` 뒤가 비어 있지 않다(남은 마무리 (가)는 아래 3번에서 채웁니다)

**2. 파일 확인** — **[터미널]** `access_control` 폴더에서 확인합니다(`pwd` 가 `…/access_control` 로 끝나지 않으면 `cd access_control` 부터 칩니다).

```bash
ls
ls config
```

오늘 만든 아래 파일이 보여야 합니다.

| 파일 | 만든 곳 |
|---|---|
| `req_create.py` · `exercise2-1_run.py` | 실습 2-1 |
| `req_review.py` · `exercise2-2_run.py` | 실습 2-2 |
| `req_grant.py` | 「권한 부여 준비」 레슨 |
| `report_u2.md` | 「문제 해결 기록 쓰기」 레슨 |

- `req_grant.py` 가 없으면 「권한 부여 준비」 레슨에서 먼저 만듭니다.
- `config` 안은 Unit 1을 마쳤을 때와 같습니다(`users.json` · `roles.json` · `exceptions.json`). Unit 1 응용 1-4를 했다면 `users_broken.json` 도 보입니다. 오늘 핵심 실습에서는 `config` 에 새 파일을 만들지 않았습니다.

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
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

   | 이것이 보이면 | 할 일 |
   |---|---|
   | `.env` | `.gitignore` 맨 아래에 `.env` 한 줄, 저장 후 `git status` 다시 |
   | `.venv` | `.env` 와 같은 방법으로 `.venv` 한 줄 |
   | `access_control/__pycache__/` | `.gitignore` 맨 아래에 `__pycache__/` 한 줄, 저장 후 `git status` 다시 |

   - `.venv` 는 파이썬 가상환경(이 프로젝트용 파이썬 도구를 담은 폴더), `__pycache__` 는 파이썬이 실행할 때 저절로 만드는 임시 폴더라 올리지 않습니다.
   - `.gitignore` 는 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래에 있습니다.
   - 오늘 새로 만든 파일은 `Untracked files:` 아래에 `access_control/req_create.py` 처럼 한 줄씩 보입니다.
3. **[문제 해결 기록]** `report_u2.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 먼저 Unit 1 마무리처럼 공개 전 점검 스크립트 `python check_publish.py` 를 돌려 마지막 줄이 `요약: 오류 0건, 주의 0건` 인지 봅니다. `access_control` 코드도 공개 사이트에 함께 올라가기 때문입니다. `[오류]` · `[주의]` 줄이 나오면 그 줄이 가리키는 파일을 고치고 다시 돌립니다. 그다음 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add access control unit 2 request, review, grant and report"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git status` 로 `.env` · `.venv` 가 없는 것을, `python check_publish.py` 로 `오류 0건` 을 본 뒤 `git add .` · `git commit` · `git push` 로 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `access_control` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다.

<!-- checklist -->
- [ ] 깃허브 내 저장소의 `access_control` 폴더에서 2번 표의 파일을 모두 확인했다
<!-- /checklist -->

- 여유가 되어 응용을 했다면 응용 파일까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**4. 이어지는 곳**

1. `req_create.py` 의 요청서 모양(`id` · `user` · `permission` · `status` …)과 상태 이름(`reviewing` · `approved` · `rejected` · `granted`)은 Module 3 끝까지 같은 뜻으로 씁니다.
2. 다음 Unit 3(권한 점검하기)에서는 이렇게 준 권한 가운데 오래 쓰이지 않는 것을 찾습니다.

**확인** — 깃허브의 `access_control` 폴더에 2번 표의 파일이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이는 파일이 있으면 `git status` 를 다시 쳐서 그 파일이 빨간 목록에 남아 있는지 보고 4번을 다시 합니다.

---

<!-- learn:answers -->
