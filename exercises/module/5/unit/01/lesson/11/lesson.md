---
id: m5-u01-l11
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 세 개와 「제공 파일」을 끝낸 뒤 합니다. 응용은 하지 않아도 됩니다.

**1. 오늘 한 일 확인**

1. 플레이북 PB-003 을 직접 쓰고, 알림 두 건을 손으로 처리하며 고친 곳을 세었다 (실습 1-1)
2. 실행기가 알림 5건을 처리하고, 승인이 필요한 건은 멈추고, 감사 기록을 남겼다 (실습 1-2)
3. 알림마다 재직 · VIP · 접속 IP 맥락을 붙이고 VIP 계정 알림 수를 셌다 (실습 1-3)
4. 「제공 파일」의 `routing.py` · `safe_runner.py` 를 만들었다
5. 보고서 `report_u1.md` 에서 꼭 채울 다섯 칸(1-1 (가) · (나), 1-2 (가), 1-3 (가), 마무리 (가))의 `답:` 뒤가 비어 있지 않다

**2. 파일 확인** — **[터미널]** `soar_response` 폴더에서 확인합니다.

```bash
pwd
ls
ls config
```

- `pwd` 가 `…/soar_response` 로 끝나야 합니다.
- `ls` 에 아래 파일이 모두 보여야 합니다.

| 만든 곳 | 파일 |
|---|---|
| 시작하기 | `incident_samples.json` · `system_state.json` · `users_info.json` · `source_ips.json` · `trusted_ips.json` |
| 실습 1-2 | `incident.py` · `playbook_runner.py` · `exercise1-2_run.py` · `action_log.json`(실행하면 생김) |
| 제공 파일 | `routing.py` · `safe_runner.py` |
| 실습 1-3 | `enrichment.py` · `exercise1-3_run.py` |
| 보고서 쓰기 | `report_u1.md` |

- `config` 안에는 `playbook_registry.json` 이 보여야 합니다.

<!-- checklist -->
- [ ] `soar_response` 폴더와 `config` 폴더에 2번 표의 파일이 모두 있는 것을 확인했다
<!-- /checklist -->

**3. 깃허브에 올리기** — Module 5 폴더를 처음 올리는 날이므로 올라가는 파일 목록을 꼭 확인합니다.

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark>`soar_response/` 가 새 폴더로 보이면</mark> 됩니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore`(깃에 올리지 않을 파일 이름을 적어 두는 파일)를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `soar_response/__pycache__/` 는 파이썬이 실행하면서 자동으로 만든 임시 폴더입니다. 올릴 필요가 없으므로 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장합니다.

<!-- checklist -->
- [ ] `git status` 에서 `.env` · `.venv` 가 올라갈 목록에 없는 것을 확인했다(있으면 `.gitignore` 에 적었다)
<!-- /checklist -->

3. **[보고서]** `soar_response/report_u1.md` 의 `## 마무리` 아래 (가)를 채웁니다. <mark>올리기 전에 채워야</mark> 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add SOAR unit 1 playbook runner, enrichment and report"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git add .` · `git commit` · `git push` 로 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소 `network-study-notes` 를 새로 고쳐 `soar_response` 폴더를 열고, 2번에서 확인한 파일이 모두 있는지 봅니다. `__pycache__` 폴더는 없어도 됩니다.

<!-- checklist -->
- [ ] 깃허브의 `network-study-notes` 저장소에서 `soar_response` 폴더의 파일을 확인했다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 이 「3. 깃허브에 올리기」의 1 ~ 4번(`cd ..` 부터 `git push` 까지, 그림의 3 ~ 5)을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**4. 이어지는 곳**

| 다시 쓰는 곳 | 오늘 만든 것 |
|---|---|
| Module 5 끝까지 | `config/playbook_registry.json` · `incident.py` · `incident_samples.json` 을 그대로 불러 쓴다 |
| Unit 2 응용 2-2 · Unit 3 응용 3-1 | `enrichment.py` 의 `enrich_incident` 와 `users_info.json` · `source_ips.json` · `trusted_ips.json` (알림에 맥락을 붙일 때) |
| Unit 2 응용 2-2 · Unit 3 응용 3-1 | 「제공 파일」의 `routing.py` |
| Unit 2 응용 2-2 | 「제공 파일」의 `safe_runner.py` |

- Unit 2 는 연습용 시스템에 적기만 하던 `계정 잠금` 을 실행한 뒤 정말 잠겼는지 다시 확인하고, 조치 전 · 후 상태를 기록으로 남깁니다.

**확인** — 깃허브의 `soar_response` 폴더에 2번 표의 파일이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이는 파일이 있으면 `git status` 를 다시 쳐서 그 파일이 빨간 목록에 남아 있는지 보고 3번의 4단계(`git add .` 부터)를 다시 합니다.
