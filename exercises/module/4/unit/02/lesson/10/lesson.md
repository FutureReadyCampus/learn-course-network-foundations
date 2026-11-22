---
id: m4-u02-l10
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리 · 깃허브에 올리기

하루를 닫는 마무리입니다(15분). 핵심 실습 세 개를 끝낸 뒤 합니다.

**1. 오늘 한 일 확인**

1. 이벤트 파일을 표로 읽고, 실패한 이벤트를 골라 소스별로 셌다 (실습 2-1)
2. 실패를 사용자별 · 시간대별로 묶어 세고 `failed_events.csv` 로 저장했다 (실습 2-2)
3. 같은 주소의 로그인 실패가 알림 기준(5번) 이상인 곳을 찾았다 (실습 2-3)
4. 보고서 `report_u2.md` 의 꼭 채울 칸 가운데 실습의 네 칸(2-1 (가) · 2-2 (가) · 2-3 (가) · (나))에 `답:` 뒤가 비어 있지 않다. 다섯째 칸인 마무리 (가)는 아래 3-3번에서 채웁니다

**2. 파일 확인** — **[터미널]** `anomaly_detection` 폴더에서 확인합니다.

```bash
pwd
ls
```

- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
- 아래 파일이 <mark>`report_u2.md` 까지 모두 보여야</mark> 합니다.

| 파일 | 만든 곳 |
|---|---|
| `normalized_events.json` | 시작하기 |
| `events_basic.py` · `exercise2-1_run.py` | 실습 2-1 |
| `events_time.py` · `exercise2-2_run.py` | 실습 2-2 |
| `failed_events.csv` | 실습 2-2 실행 때 생김 |
| `login_detection.py` · `exercise2-3_run.py` | 실습 2-3 |
| `report_u2.md` | 보고서 쓰기 |

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 2번 표의 파일이 `report_u2.md` 까지 모두 있는 것을 확인했다
<!-- /checklist -->

**3. 깃허브에 올리기**

1. **[터미널]** `network-study-notes` 폴더로 옮기고 위치를 확인합니다. <mark>결과가 `…/network-study-notes` 으로 끝나야</mark> 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 글씨 줄에 <mark>`.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다</mark>.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` · `.venv/` · `__pycache__/`(파이썬이 실행하면서 자동으로 만든 임시 폴더)는 Module 3 Unit 1에서 만든 `.gitignore` 에 이미 들어 있어서 보통은 보이지 않습니다. 줄을 새로 적지 않습니다.
   - 그런데도 보이면 VS Code 왼쪽 목록에서 `.gitignore` 가 `network-study-notes` 바로 아래에 있는지, 이름이 `.gitignore` 와 똑같은지 봅니다. 파일이 없거나 다른 폴더에 있으면 [Module 3 Unit 1의 `.gitignore`](__SITE__/exercises/module/3/unit/1/lesson/1/page/7) 내용으로 `network-study-notes` 바로 아래에 만들고 `git status` 를 다시 칩니다.
3. **[보고서]** `report_u2.md` 의 `## 마무리` 아래 (가)를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다. 못 적은 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add anomaly detection unit 2 pandas counting and login failure rule"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`).

<!-- checklist -->
- [ ] `git status` 에 `.env` · `.venv` 가 없는 것을 보고 `git add` · `git commit` · `git push` 를 했다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `anomaly_detection` 폴더를 열고, 2번에서 본 파일이 모두 있는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.

**확인** — 깃허브의 `anomaly_detection` 폴더에 2번 표의 파일이 모두 보이고 `.env` 가 없으면 성공입니다. 안 보이는 파일이 있으면 `git status` 를 다시 쳐서 그 파일이 빨간 목록에 남아 있는지 보고 4번을 다시 합니다.

<!-- checklist -->
- [ ] 깃허브의 내 저장소 `anomaly_detection` 폴더에서 2번 표의 파일을 모두 봤다
<!-- /checklist -->

- 시간이 남아 응용을 했다면 응용 파일(`baseline_logins.csv` · `baseline.py` · `apply2-1_run.py` · `classify.py` · `apply2-2_run.py`)까지 만든 뒤 2 ~ 4번을 한 번 더 하면 됩니다. 같은 날 여러 번 올려도 괜찮습니다.

**4. 이어지는 곳**

1. 다음 Unit 3(요청 급증과 반복 거절 찾기)은 분 단위로 요청 수를 세어 **요청이 갑자기 늘어난 때**(트래픽 급증)를 찾고, 판정 서버에서 거절이 반복된 사용자를 찾습니다.
2. 오늘 만든 `normalized_events.json` 과 `login_detection.py` 는 Unit 3 응용 3-1(알림을 한 파일로 모으기)에서 다시 불러 씁니다.
