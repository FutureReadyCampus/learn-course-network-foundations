---
id: m4-u01-l10
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개를 끝낸 뒤 하고, 그다음 「오늘의 글 쓰기」 레슨으로 갑니다. Module 3 마지막 Unit의 `access_control` 폴더를 아직 올리지 않았다면 같은 저장소라서 오늘 함께 올라갑니다. 이미 올렸다면 `git status` 에 보이지 않는 것이 정상입니다.

**1. 오늘 한 일 확인**

1. 접속 로그 30줄을 읽어 28줄을 주소 · 방법 · 경로 · 상태 코드로 나누고, 깨진 2줄을 읽기 실패로 셌다 (실습 1-1)
2. 웹 서버 로그 한 줄을 시각 · 결과를 맞춘 공통 이벤트로 바꿨다 (실습 1-2)
3. 보고서 `report_u1.md` 의 꼭 채울 칸(실습 1-1 (가) · (다), 실습 1-2 (가) · (나))에 `답:` 뒤가 비어 있는 질문이 없다. <mark>못 적은 칸은 `모름 — 막힌 곳: …` 으로 적습니다.</mark>

**2. 파일 확인** — **[터미널]** `anomaly_detection` 폴더에서 확인합니다.

```bash
pwd
ls
```

- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
- 아래 파일이 보여야 합니다.

| 파일 | 만든 곳 |
|---|---|
| `access_sample.log` | 시작하기 |
| `log_parse.py` · `exercise1-1_run.py` | 실습 1-1 |
| `normalize_web.py` · `exercise1-2_run.py` | 실습 1-2 |
| `report_u1.md` | 「보고서 쓰기」 레슨 |

- 응용을 했다면 그 응용의 파일(`log_classify.py` · `server_log.jsonl` · `saas_events.csv` · `normalize_json_csv.py` · `normalize.py` · `apply1-1_run.py` ~ `apply1-3_run.py` · `normalized_events.json` 중 만든 것)도 보입니다. 응용 1-3의 문법 상자를 직접 돌렸다면 연습 파일 `demo_events.json` 도 보이는데, 지워도 됩니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 「2. 파일 확인」 표의 파일이 모두 있는 것을 봤다
<!-- /checklist -->

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/network-study-notes` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 위 메뉴 **Terminal › New Terminal** 로 터미널을 새로 엽니다. 새 터미널은 `network-study-notes` 에서 열립니다(이름 칸이 **bash** 인지 확인).
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄

   | 보이는 것 | 뜻 | 할 일 |
   |---|---|---|
   | `anomaly_detection/` | 오늘 만든 새 폴더 | 올리면 됨 |
   | `access_control/` 안의 파일 | Module 3 마지막 Unit의 파일을 아직 올리지 않음(이미 올렸다면 안 보이는 것이 정상) | 함께 올리면 됨 |
   | `.env` · `.venv` | 올리면 안 되는 파일 | `.gitignore` 맨 아래에 그 이름 한 줄을 적고 저장한 뒤 `git status` 를 다시 침 |
   | `anomaly_detection/__pycache__/` | 파이썬이 실행하면서 자동으로 만든 임시 폴더. 보통은 Module 3에서 만든 `.gitignore` 가 이미 걸러서 안 보임 | 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장 |

   - `.gitignore` 는 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래에 있습니다.
3. **[보고서]** `report_u1.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add anomaly detection unit 1 log parsing and web log normalization"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git add .` · `git commit` · `git push` 로 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `anomaly_detection` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다.

<!-- checklist -->
- [ ] 깃허브의 내 저장소 `anomaly_detection` 폴더에 오늘 만든 파일이 보이고 `.env` · `.venv` 가 없는 것을 봤다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**확인** — 깃허브의 `anomaly_detection` 폴더에 「2. 파일 확인」 표의 파일이 모두 보이고 `.env` · `.venv` 가 없으면 성공입니다. 안 보이면 `git status` 를 다시 쳐서 빨간 목록에 남은 파일이 있는지 보고, 「3. 깃허브에 올리기」의 4번(add · commit · push)을 다시 합니다.

**4. 이어지는 곳**

1. 다음 Unit 2(판다스로 세고 기준 정하기)는 세 로그를 합친 공통 이벤트 57개를 **판다스**로 표처럼 읽어 실패한 이벤트를 골라 세고, 사용자별 · 주소별로 묶습니다.
2. 이벤트 파일 `normalized_events.json` 은 Unit 2 시작하기에서 샘플로 만들기 때문에, 응용 1-3을 하지 않았어도 됩니다. 판다스 설치도 Unit 2 시작하기에서 합니다.
