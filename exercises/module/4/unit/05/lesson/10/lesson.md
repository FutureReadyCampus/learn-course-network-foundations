---
id: m4-u05-l10
title: 이번 Unit 마무리
render: markdown
---

# 이번 Unit 마무리

## 이번 Unit 마무리

**지금 실습 5-2 를 막 끝냈다면, 먼저 [「오늘의 글 쓰기」](__SITE__/exercises/module/4/unit/5/lesson/5/page/1)를 마친 뒤 이 쪽으로 돌아옵니다.**

하루를 닫는 마무리입니다(15분). 실습 5-1 · 5-2와 「보고서 쓰기」 · 「오늘의 글 쓰기」를 끝낸 뒤 합니다.

**1. 오늘 한 일 확인**

1. 점수 파일의 사실만 AI 에게 보내 대상 3명의 요약을 받고, 실패하면 대체 문장을 쓰게 했다 (실습 5-1)
2. 상황 8개 중 3개 이상의 원인과 고치는 방법을 내 말로 정리해 Module 4 총정리를 썼다 (실습 5-2)
3. 보고서 `report_u5.md` 의 꼭 채울 칸(실습 5-1 (가) · (나), 실습 5-2 상황 3개와 (가) · (나), 마무리 (가))에 `답:` 뒤가 비어 있는 곳이 없다. 마무리 (가)는 다음 쪽 「깃허브에 올리기」 3번에서 채운다
4. 응용 5-1 · 5-2를 했다면 컴포즈 파일 두 개와 `logs` 폴더가 있고, 응용 5-3을 했다면 보고서 파일 `anomaly_detection_report_2026-11-02.json` 이 있다 (선택)

**2. 파일 확인** — **[터미널]** `anomaly_detection` 폴더에서 확인합니다.

```bash
pwd
ls
```

- `pwd` 결과가 `anomaly_detection` 으로 끝나야 합니다.
- 이번 Unit에서 만든 파일이 보여야 합니다. 응용 파일은 그 응용을 했을 때만 있습니다.

| 언제 | 보여야 할 파일 |
|---|---|
| 시작하기 · 실습 | `llm_client.py` · `unit05_risk_scores.json` · `event_summary.py` · `exercise5-1_run.py` · `report_u5.md` |
| 응용 5-1 · 5-2 | `compose.yaml` · `compose.secure.yaml` · `logs/` |
| 응용 5-3 | `pipeline.py` · `apply5-3_run.py` · `anomaly_detection_report_2026-11-02.json` |

- Module 4의 파일은 이렇게 둡니다. 파일을 어디에 저장했는지 헷갈리면 이 규칙과 VS Code 왼쪽 목록을 비교합니다.

| 폴더 | 두는 것 |
|---|---|
| `config/` | JSON 설정 파일(`users.json` · `roles.json`)만 |
| `anomaly_detection/` 바로 아래 | 그 밖의 파일 모두(코드 · 실행 파일 · 데이터 · 보고서 · 컴포즈 파일) |
| `logs/` | 응용 5-2에서 컴포즈가 남긴 접속 기록 |
| `__pycache__/` | 파이썬이 자동으로 만드는 임시 폴더(신경 쓰지 않음) |

- 코드는 `.py`, 실행 파일은 `exerciseN-M_run.py` · `applyN-M_run.py`, 보고서는 `report_uN.md` 입니다.

```
network-study-notes/
  .env                       ← 키를 만든 사람만 (깃허브에 올리지 않음)
  .gitignore
  access_control/            Module 3
  anomaly_detection/         Module 4
    config/
      users.json
      roles.json
    llm_client.py
    unit05_risk_scores.json
    event_summary.py
    exercise5-1_run.py
    report_u5.md
    (앞 Unit의 파일들)
    (응용을 했다면) compose.yaml · compose.secure.yaml · logs/
    (응용을 했다면) pipeline.py · apply5-3_run.py · anomaly_detection_report_2026-11-02.json
```

**확인** — `ls` 에 `llm_client.py` · `unit05_risk_scores.json` · `event_summary.py` · `exercise5-1_run.py` · `report_u5.md` 다섯 개가 모두 보이면 성공입니다. 빠진 것이 있으면 VS Code 왼쪽 목록에서 다른 폴더에 만들어졌는지 보고 `anomaly_detection` 으로 끌어다 옮깁니다.

## 마무리 · 깃허브에 올리기

**「오늘의 글 쓰기」를 아직 안 했다면, [「오늘의 글 쓰기」](__SITE__/exercises/module/4/unit/5/lesson/5/page/1)를 마친 뒤 이 쪽으로 돌아옵니다.**

<mark>Module 4 작업을 저장소에 올리는 마무리입니다.</mark> 보고서와 글쓰기를 마친 뒤에 올려야 빈칸 없이 올라갑니다. 어느 터미널을 써도 되고, `pwd` 로 위치를 먼저 확인한 뒤 결과가 `anomaly_detection` 으로 끝나면 아래 1번의 `cd ..` 를 칩니다.

**이런 상황이 있습니다**

- **지금은**: <mark>팀장이 「Module 4에서 만든 파일과 보고서 파일을 저장소에 남겨 달라」고 합니다</mark>.
- **그래서 하는 것**: `git status` 로 올라갈 파일을 확인한 뒤(`.env` 같은 비밀 키 파일이 섞이면 안 됩니다) `git add` → `git commit` → `git push` 순서로 올립니다.
- **끝나면**: 깃허브 저장소의 `anomaly_detection` 폴더에 이번 Unit에서 만든 `event_summary.py` · `exercise5-1_run.py` · `report_u5.md` 가 보입니다. 응용을 했다면 그 파일도 함께 보입니다.

**순서**

1. **[터미널]** `network-study-notes` 폴더로 옮깁니다. 앞 페이지의 `pwd` 결과가 `anomaly_detection` 으로 끝날 때만 `cd ..` 를 칩니다. 이미 `…/network-study-notes` 으로 끝나면 `cd ..` 는 건너뛰고 `pwd` 만 칩니다.

   ① 한 단계 위 폴더로 이동합니다.

   ```bash
   cd ..
   ```

   - 하는 일: 한 단계 위 폴더로 이동합니다.
   - 나오는 것: 아무것도 나오지 않습니다.

   ② 지금 위치를 확인합니다.

   ```bash
   pwd
   ```

   - 하는 일: 지금 있는 폴더의 위치를 보여 줍니다.
   - 나오는 것: <mark>`…/network-study-notes` 으로 끝나면</mark> 됩니다. 결과가 다르면 VS Code 왼쪽 목록에서 `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다.

2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. <mark>빨간 글씨 줄에 `.env` 나 `.venv` 가 보이면 올리지 말고,</mark> 아래 안내대로 `.gitignore` 를 고친 뒤 `git status` 를 다시 봅니다.

   ```bash
   git status
   ```

   - 하는 일: 올릴 파일의 상태를 보여 줍니다.
   - 나오는 것: 바뀐 파일의 이름이 나옵니다.
   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `network-study-notes` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다.
     - `.venv` 는 `.venv/` 한 줄을 같은 방법으로 적습니다.
   - `anomaly_detection/__pycache__/` (파이썬이 실행하면서 자동으로 만드는 임시 폴더)가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 봅니다.
   - `anomaly_detection/llm_client.py` 는 API 키가 들어 있지 않은 코드 파일이라 올라가도 됩니다. 키는 `.env` 에만 있습니다.

<!-- checklist -->
- [ ] `network-study-notes` 폴더에서 `git status` 를 쳐서 목록에 `.env` · `.venv` 가 없는 것을 확인했다
<!-- /checklist -->

3. **[보고서]** `report_u5.md` 의 `## 마무리` 아래를 채웁니다.
   - (가) `git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.
   - <mark>실습 5-1 · 5-2에서 못 적은 보고서 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다.</mark> 올린 뒤에 이어서 적어 다시 올려도 됩니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`). 세 명령을 순서대로 하나씩 칩니다.

   ① 바뀐 파일을 모두 담습니다.

   ```bash
   git add .
   ```

   - 하는 일: 바뀐 파일을 올릴 대상에 담습니다.
   - 나오는 것: 아무것도 나오지 않습니다.

   ② 기록으로 저장합니다.

   ```bash
   git commit -m "Add AI summary and Module 4 review for anomaly detection"
   ```

   - 하는 일: 따옴표 안의 설명을 붙여 기록으로 저장합니다.
   - 나오는 것: 바뀐 파일 수가 적힌 줄이 나옵니다.

   ③ 깃허브로 올립니다.

   ```bash
   git push
   ```

   - 하는 일: 저장한 기록을 깃허브로 올립니다.
   - 나오는 것: 올라간 내용이 몇 줄 나옵니다.
   - `git push` 가 거절(`rejected`)되면 `git pull --no-rebase` 로 받아 와 합친 뒤 `git push` 를 다시 합니다(터미널에 편집기 화면이 뜨면 `Esc` → `:wq` → `Enter`, VS Code 에 새 탭이 열리면 그 탭을 그대로 닫습니다).

<!-- checklist -->
- [ ] `git add .` → `git commit` → `git push` 를 차례로 쳐서 올렸다
<!-- /checklist -->

5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `anomaly_detection` 폴더를 열고, VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 있는 파일들이 깃허브에도 보이는지 확인합니다. <mark>`.env` 와 `__pycache__` 폴더는 없어야 합니다</mark>.
   - 빠진 이름이 있으면 VS Code 왼쪽 목록의 `anomaly_detection` 폴더에 내 PC 에도 있는지 봅니다.
     - 없으면 다른 폴더에 만든 것이니 `anomaly_detection` 안으로 옮기고, 2번의 `git status` 부터 다시 합니다.

**확인** — 깃허브의 `anomaly_detection` 폴더에 `event_summary.py` · `report_u5.md` 가 보이고 `.env` 가 없으면 성공입니다. 파일이 안 보이면 `git push` 의 출력에 `rejected` 나 `error` 가 있었는지 보고, 위 4번 ③ 의 안내대로 다시 올립니다.

<!-- checklist -->
- [ ] 깃허브의 `anomaly_detection` 폴더에서 `event_summary.py` · `report_u5.md` 를 보고 `.env` 가 없는 것을 확인했다
<!-- /checklist -->

## 마무리 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 파일 확인 | `anomaly_detection` 에서 `pwd` · `ls` |
| 올릴 파일 확인 | `git status` (`.env` · `.venv` 가 보이면 멈춤) |
| 올리기 | `git add .` → `git commit -m "…"` → `git push` |
| 올린 뒤 | 브라우저에서 `anomaly_detection` 폴더와 파일이 있는지 확인 |

**이어지는 곳**

1. 여기까지가 Module 4입니다. 다음은 **Module 5 자동 대응**입니다.
2. Module 4는 쌓인 로그를 읽어 평소와 다른 일을 찾고, 대상마다 점수와 등급을 매겼습니다. Module 5는 <mark>등급이 `high` 인 대상을 만났을 때 사람이 하던 일(계정 잠그기, 티켓 남기기, 담당자에게 알리기)을 프로그램이 대신하게</mark> 합니다.
3. 보고서 실습 5-2 상황 정리의 마지막 칸(담당자가 가장 먼저 할 일)이 그때 대응 목록을 만드는 참고 자료가 됩니다. Module 5는 새 폴더 `soar_response` 에서 작업하고, 그 폴더는 Module 5의 시작하기에서 만듭니다.
