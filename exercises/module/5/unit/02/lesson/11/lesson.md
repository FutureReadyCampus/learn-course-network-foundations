---
id: m5-u02-l11
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개와 보고서의 [핵심 질문], 글쓰기(「오늘의 글 쓰기」 세 문장 글)를 마친 뒤 이 페이지로 돌아와 합니다. 응용을 하지 않았어도 이대로 마무리합니다.

- 「오늘의 글 쓰기」 마지막 페이지에서 이미 `git push` 까지 했다면 파일은 깃허브에 올라가 있습니다. 그래도 아래 「1. 오늘 한 일 확인」 · 「2. 파일 확인」을 하고, 「3. 깃허브에 올리기」로 보고서 `## 마무리` (가)까지 채워 한 번 더 올립니다. 같은 날 여러 번 올려도 괜찮습니다.

**1. 오늘 한 일 확인**

1. 계정 잠금을 실행하고 사후 검증했으며, 조치 전 · 후 상태를 감사 기록으로 남겼다 (실습 2-1)
2. 잠금 뒤 활성 세션을 종료하고, 빈틈(잔존 세션)이 남았는지 다시 점검했다 (실습 2-2)
3. 「제공 파일」 레슨의 `ip_actions.py` · `audit.py` · `approvals.py` 를 만들고 `제공 파일 정상` 을 확인했다
4. 보고서 `report_u2.md` 의 꼭 채울 칸(2-1 (가) · (다), 2-2 (가) · (다))에 `답:` 뒤가 비어 있지 않다

**2. 파일 확인** — **[터미널]** `soar_response` 폴더에서 확인합니다.

```bash
ls
ls config
python -c "import json; print(json.load(open('containment_state.json', encoding='utf-8'))['locked_users'], len(json.load(open('containment_log.json', encoding='utf-8'))))"
```

- `containment_store.py` · `account_actions.py` · `exercise2-1_run.py` · `session_actions.py` · `containment.py` · `exercise2-2_run.py` · `ip_actions.py` · `audit.py` · `approvals.py` · `ip_users.json` · `containment_state.json` · `containment_log.json` · `report_u2.md` 가 보여야 합니다.
- `config` 안에는 `vip_accounts.json` · `allowlist_ips.json` 이 새로 보여야 합니다.
- 마지막 줄은 <mark>`['junho', 'dami'] 5`</mark> 여야 합니다. 실습 2-2 가 저장한 상태(잠긴 계정 두 개 · 조치 기록 5건)이고, Unit 3 실습 3-1 이 이 상태에서 시작합니다.
  - 다른 값이 나오면(예: 응용 2-3 을 실습 2-2 뒤에 실행해 `['junho'] 4` 가 나옴) `python exercise2-2_run.py` 를 한 번 더 실행하고 다시 확인합니다. 응용 실행 파일도 같은 두 파일에 결과를 저장하기 때문입니다.
- 응용 2-3 을 하다가 다 채우지 못했거나 출력이 「정답」과 다르면, `ip_actions.py` 의 내용을 모두 지우고 「제공 파일」 레슨의 완성본을 다시 붙여 넣은 뒤 「제공 파일」 레슨 첫 페이지 4번 명령을 다시 칩니다. Unit 3 이 이 파일을 불러 쓰기 때문입니다.

<!-- checklist -->
- [ ] `soar_response` 폴더에서 파일 확인 명령을 쳐 마지막 줄에 `['junho', 'dami'] 5` 가 나왔다
<!-- /checklist -->

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env`(API 키가 들어 있는 파일)나 `.venv`(내 PC 에서만 쓰는 가상환경 폴더)가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore`(깃이 올리지 않을 파일 이름을 적어 두는 파일)를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.
   - `soar_response/containment_state.json` · `soar_response/containment_log.json` 은 실습 2-2 에서 프로그램이 저장한 상태 파일입니다. 이것도 올라갑니다.
3. **[보고서]** `report_u2.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add SOAR unit 2 account lockout, session termination and provided files"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase --no-edit` 로 받아 와 합친 뒤 `git push` 를 다시 합니다. `--no-edit` 는 합친 기록의 설명을 기본값 그대로 써서 편집기 화면이 뜨지 않게 합니다.

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git status` 로 `.env` · `.venv` 가 목록에 없는 것을 본 뒤 `git add .` · `git commit` · `git push` 로 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소 `network-study-notes` 를 새로 고쳐 `soar_response` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.

<!-- checklist -->
- [ ] 깃허브의 `network-study-notes` 저장소 `soar_response` 폴더에 2번에서 본 파일이 모두 보였다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다. 올리기 전에 2번의 마지막 줄이 `['junho', 'dami'] 5` 인지 다시 봅니다.

**확인** — 2번 마지막 줄이 `['junho', 'dami'] 5` 이고, 깃허브의 `soar_response` 폴더에 2번에서 본 파일이 모두 보이면 성공입니다. 안 보이면 3번의 `git status` 부터 다시 합니다.

**4. 이어지는 곳**

1. 다음 Unit 3(되돌리고 티켓 남기기)의 실습 3-1 에서는 오늘 저장한 `containment_state.json` · `containment_log.json` 의 기록만 근거로 자동 조치를 **되돌립니다**(조치 전부터 잠겨 있던 `junho` 는 그대로 둡니다).
2. 실습 3-1 은 오늘 만든 `containment_store.py` · `account_actions.py` 와 제공 파일 `ip_actions.py` 를 불러 씁니다. 실습 3-2 에서는 처리할 일을 티켓으로 만들고 응답 기한을 계산합니다.
