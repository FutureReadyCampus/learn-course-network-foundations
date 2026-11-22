---
id: m3-u01-l14
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 세 개를 끝낸 뒤 합니다.

**1. 오늘 한 일 확인**

1. 인증과 인가를 구분하고, 매트릭스로 요청을 판정했다 (실습 1-1)
2. `config/users.json` 과 `config/roles.json` 을 직접 쓰고 JSON 규칙을 확인했다 (실습 1-1)
3. `check_permission` 이 모든 실패 경로를 서로 다른 이유로 거부한다 (실습 1-2)
4. `evaluate_access` 가 역할 권한을 먼저 보고, 「권한 없음」일 때만 예외를 본다 (실습 1-3)
5. 보고서 `report_u1.md` 의 실습 1-1 ~ 1-3 칸에 `답:` 뒤가 비어 있는 질문이 없다

**2. 파일 확인** — **[터미널]** `access_control` 폴더에서 확인합니다.

```bash
ls
ls config
```

아래 파일이 모두 보여야 합니다. `config/` 가 붙은 파일은 `ls config` 에서 보입니다.

| 파일 | 만든 곳 |
|---|---|
| `rbac.py` · `exercise1-2_run.py` | 실습 1-2 |
| `exception_policy.py` · `config_loader.py` | 「제공 파일」 |
| `policy.py` · `exercise1-3_run.py` | 실습 1-3 |
| `report_u1.md` | 「보고서 쓰기」 |
| `config/users.json` · `config/roles.json` | 실습 1-1 |
| `config/exceptions.json` | 「제공 파일」 |

**3. 깃허브에 올리기**

저장소 `network-study-notes` 는 「시작하기」 3쪽에서 내려받았고 7쪽에서 처음 올려 두었습니다. 작업 폴더 `access_control` 은 그 저장소 루트 바로 아래에 있으므로, 저장소 루트(`..`)로 올라가 올리면 오늘 만든 파일이 함께 올라갑니다. 이 저장소는 Public 이므로 `access_control` 의 파일도 누구나 볼 수 있습니다.

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 메뉴 **Terminal › New Terminal** 로 터미널을 새로 엽니다. 새 터미널은 저장소 맨 위 폴더(`…/network-study-notes`)에서 열리므로 `cd ..` 없이 `pwd` 만 다시 칩니다. 터미널 이름 칸이 **bash** 가 아니면 시작하기 3쪽처럼 **Git Bash** 를 고릅니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env`(비밀번호 · 키를 적어 두는 파일)나 `.venv`(파이썬이 쓰는 가상 환경 폴더)가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   git status -u
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄 · `git status -u` 아직 안 올린 새 파일을 폴더로 접지 않고 파일 하나하나로 풀어 보여 줌
   - 오늘 처음 올리는 `access_control` 폴더는 `git status` 에서 안의 파일이 하나씩 나오지 않고 **`access_control/` 한 줄로 접혀** 나옵니다. 그 밖에는 시작하기 12쪽에서 만든 `check_publish.py` 처럼 아직 올리지 않은 새 파일이 한 줄씩 나옵니다. 예를 들면 빨간 목록이 `access_control/` · `check_publish.py` 두 줄입니다.
   - 그래서 `access_control` 안에 `.env` 가 없는지는 `git status` 만으로는 안 보입니다. `git status -u` 로 풀어 본 목록(`access_control/rbac.py` · `access_control/config/users.json` …)에 `.env` · `.venv` 가 없으면 됩니다. `.gitignore` 에 적힌 파일은 `-u` 로 풀어도 나오지 않습니다.
   - 시작하기 7쪽에서 만든 `.gitignore` 에 `.env` · `.venv/` · `__pycache__/`(파이썬이 실행하면서 자동으로 만든 임시 폴더)가 들어 있어 보통은 보이지 않습니다. 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래에 `.gitignore` 가 있는지 보고, 그 파일 맨 아래에 보인 이름(예: `.env`)을 한 줄 적고 저장한 뒤 `git status` 를 다시 칩니다.
3. **[보고서]** `report_u1.md` 의 `## 마무리` 아래 (가)를 채웁니다. 2번의 `git status` 빨간 목록 줄과, `git status -u` 에서 `.env` · `.venv` 가 있었는지를 적습니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 저장소 루트에서 공개 전 점검 스크립트를 돌립니다. 시작하기 12쪽에서 만든 `check_publish.py` 이고, 올리기 전에는 매번 이렇게 한 번 돌립니다.
   ```bash
   python check_publish.py
   ```
   - 명령 풀이: `python check_publish.py` 저장소 안의 모든 파일에 비밀 값 · 개인 정보가 없는지 점검
   - 마지막 줄에 `요약: 오류 0건, 주의 0건` 이 나오면 5번으로 갑니다. `[오류]` · `[주의]` 줄이 나오면 그 줄이 가리키는 파일을 고치고 다시 돌립니다.
5. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add access control unit 1 roles, checker, policy and report"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다. 그때 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다. 이 화면은 git 이 두 기록을 합친 기록에 붙일 메시지를 확인하라고 여는 편집기(vim)라서, 메시지는 고치지 않고 저장하고 닫기만 하면 됩니다.

<!-- checklist -->
- [ ] 저장소 루트에서 `git status` · `git status -u` 로 `.env` 가 없는 것을 보고, `python check_publish.py` 가 `오류 0건` 인 것을 확인한 뒤 `git add` · `git commit` · `git push` 로 올렸다
<!-- /checklist -->

6. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `access_control` 폴더를 열고, 위 「2. 파일 확인」 표의 파일이 모두 있는지 확인합니다.

<!-- checklist -->
- [ ] GitHub 저장소의 `access_control` 폴더에서 「2. 파일 확인」 표의 파일을 모두 보았다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 이 「3. 깃허브에 올리기」의 2 ~ 5번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**확인** — 깃허브의 `access_control` 폴더에 「2. 파일 확인」 표의 파일이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이는 파일이 있으면 `git status` 를 다시 쳐서 그 파일이 빨간 목록에 남아 있는지 보고 5번을 다시 합니다.

**4. 이어지는 곳**

| 파일 · 함수 | 다음에 쓰는 곳 |
|---|---|
| `users.json` · `roles.json` · `rbac.py` | Module 3 끝까지 그대로 불러 씀 |
| `policy.py` 의 `evaluate_access` | 다음 Unit 2(권한 주기)에서 요청으로 권한을 주기 전과 준 뒤의 판정을 비교할 때 |
| `config_loader.py` 의 `load_json` | Unit 2부터 설정 파일을 읽을 때 |
