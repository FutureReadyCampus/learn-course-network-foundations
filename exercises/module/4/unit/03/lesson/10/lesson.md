---
id: m4-u03-l10
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 두 개를 끝내고 「보고서 쓰기」 · 「오늘의 글 쓰기」까지 한 뒤에 합니다.

**1. 오늘 한 일 확인**

1. 웹 서버 요청을 분마다 세고, 평소 평균의 3배(6.0번) 이상인 분을 찾았다 (실습 3-1)
2. 판정 서버 거절 9건 중 반복된 7건을 Module 3 의 `check_permission` 으로 다시 판정하고, 이유로 순서를 정했다 (실습 3-2)
3. 보고서 `report_u3.md` 의 실습 3-1 · 3-2 칸에 `답:` 뒤가 비어 있는 질문이 없다(못 적은 칸은 `모름 — 막힌 곳: …`)

**2. 파일 확인** — **[터미널]** 작업 폴더 `network-study-notes/anomaly_detection` 에서 확인합니다.

```bash
pwd
ls
ls config
```

- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기 · `ls config` config 폴더 안 보기
- 오늘 만든 `baseline_traffic.csv` · `traffic_detection.py` · `exercise3-1_run.py` · `rbac.py` · `access_detection.py` · `exercise3-2_run.py` · `report_u3.md` 가 보여야 합니다. `normalized_events.json` 과 Unit 2 파일도 함께 보입니다.
- `config` 안에는 `users.json` · `roles.json` 이 보여야 합니다.
- `__pycache__` 폴더는 파이썬이 실행하면서 만든 임시 폴더라 있어도 됩니다.

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. <mark>결과가 `…/network-study-notes` 으로 끝나야 합니다.</mark>
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark>빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.</mark>
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - 아래 표의 이름이 보이면 VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore` 를 열어 맨 아래에 그 줄을 적고 저장합니다. `.env` · `.venv` 는 적은 뒤 `git status` 를 다시 칩니다.

   | 보이는 이름 | `.gitignore` 맨 아래에 적을 줄 |
   |---|---|
   | `.env` | `.env` |
   | `.venv` | `.venv/` |
   | `anomaly_detection/__pycache__/` | `__pycache__/` |

<!-- checklist -->
- [ ] 2번의 파일이 `anomaly_detection` 과 `anomaly_detection/config` 에 모두 있는 것을 보고, `network-study-notes` 폴더에서 `git status` 로 `.env` · `.venv` 가 올라가지 않게 했다
<!-- /checklist -->

3. **[보고서]** `report_u3.md` 의 `## 마무리` 아래 (가)를 채웁니다. <mark>올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다.</mark>
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add anomaly detection unit 3 traffic spike and repeated denial detection"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).
5. **[브라우저]** 깃허브의 내 `network-study-notes` 저장소를 새로 고쳐 `anomaly_detection` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다.

<!-- checklist -->
- [ ] `git add .` · `git commit` · `git push` 로 올리고, 깃허브의 `anomaly_detection` 폴더에서 파일을 확인했다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일까지 만든 뒤 3번의 2 ~ 4를 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**확인** — 깃허브의 `anomaly_detection` 폴더에 2번에서 본 파일이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이면 `git status` 를 다시 쳐서 빨간 목록이 남아 있는지 보고, 남아 있으면 3번의 4를 다시 합니다.

**4. 이어지는 곳**

1. 다음 Unit 4(위험 점수 매기고 오탐 줄이기)에서는 이번 Unit 의 탐지 결과를 **같은 사용자의 기록끼리 이어서 함께 보고**, 위험 점수를 매겨 등급으로 나눕니다.
2. 오늘 만든 `access_detection.py` 는 다음 Unit 에서 여러 번 불러 씁니다. 파일 이름과 함수 이름을 바꾸지 않습니다.
