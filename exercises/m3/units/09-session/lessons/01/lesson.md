---
id: m3-u09-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/092_day05_pm_conditions.md
  mission_id: GichanSource.m3-1030-pm-conditions
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## Unit 9에서 할 일: 조건 판정과 서버

Unit 8에서는 점검에서 찾은 권한을 계획 → 승인 → 실행 순서로 회수했습니다. 이번 Unit에서는 회수하고도 남은 권한을 **요청이 올 때마다 조건을 확인해서** 판정하고, 그 판정을 **서버**로 만들어 다른 프로그램이 주소로 요청해 판정을 받을 수 있게 합니다.

- **Exercise 9-1**: 기본 판정이 허용이어도 업무 시간과 접속 위치 조건에 어긋나면 거부하는 **조건기반 정책**을 만든다.
- **Exercise 9-2**: 판정을 `.py` **서버**로 만들어 다른 프로그램이 주소로 요청해 판정을 받을 수 있게 하고, 요청마다 로그를 한 줄씩 남긴다.
  - 요청을 보내 응답과 서버 로그를 대조하고, 마지막에 이번 Unit에서 만든 것을 깃허브에 올립니다.

Exercise마다 문제는 하나입니다. 이번 Unit은 Unit 8의 회수 결과를 쓰지 않고, Unit 2에서 만든 판정 함수 `evaluate_access` 만 씁니다.

**이번 Unit에서 불러 쓰는 이전 파일** — 이번 Unit의 코드가 `import` 로 가져다 쓰는, 앞서 만든 파일입니다. 없으면 오른쪽 열의 방법으로 먼저 준비합니다.

| 파일 | 만든 Unit | 이번 Unit에서 가져다 쓰는 것 | 쓰는 Exercise | 없으면 |
|---|---|---|---|---|
| `policy.py` | Unit 2 | `evaluate_access` (이 함수가 `rbac.py` · `exception_policy.py` 와 `config` 의 json 3개를 다시 가져다 씁니다) | Exercise 9-1 | `unit03_recovery` 폴더(Unit 1 ~ Unit 3 파일의 완성본) |
| `config_loader.py` | Unit 3 | `load_json` | Exercise 9-1 | `unit03_recovery` 폴더(Unit 1 ~ Unit 3 파일의 완성본) |

- Unit 8의 회수 결과와 Unit 4 ~ Unit 7의 파일은 이번 Unit에서 쓰지 않습니다. 앞의 Unit을 건너뛰었어도 위 `unit03_recovery` 폴더만 있으면 됩니다.
- 이번 Unit에서 만드는 파일도 뒤 Exercise가 가져다 씁니다. Exercise 9-1의 `conditional.py` 는 Exercise 9-2에서 씁니다.

## 폴더 열고 Unit 2 판정 함수 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 이전 파일, 설치한 도구(flask · requests)를 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from datetime import datetime; from rbac import USERS; from policy import evaluate_access; from config_loader import load_json; import flask, requests; print('이전 파일 · flask · requests 정상', len(USERS), evaluate_access('seoyeon', 'SALES', 'QUERY', datetime(2026, 10, 30, 10, 0)))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다(`NotOpenSSLWarning` 경고는 무시합니다). 마지막 줄에 `이전 파일 · flask · requests 정상 6 (True, '역할 권한')` 이 나와야 합니다.
   - 파일이 없거나 결과가 다르면 수업 자료의 `unit03_recovery` 폴더 파일을 `access_control` 폴더에 넣고(`config` 안의 파일은 `config` 폴더에) 마지막 줄을 다시 칩니다. `No module named 'flask'` 나 `'requests'` 가 나오면 `pip install flask requests`(맥북은 `pip3`)를 칩니다.
3. **이번 Unit에서 받은 파일 두 개를 `access_control` 폴더에 둡니다.** 이미 있으면 건너뜁니다. `다운로드` 폴더에서 VS Code 왼쪽의 그 폴더 위로 끌어다 놓습니다(안 되면 파일을 열어 **File › Save As…** 로 저장).
   - Unit 9 (이 파일) — 실습 안내. 읽기만 합니다.
   - Unit 9 — **보고서.** Exercise 9-1 · Exercise 9-2 답과 마무리 칸을 여기에 적습니다.
4. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. 보고서 Unit 9 는 오른쪽 클릭 › **Open to the Side** 로 옆에 열고, 맨 위 제목 `(이름 · Unit 9)` 의 `이름` 만 내 이름으로 바꿉니다.
5. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.
   - 문자열(string)은 따옴표로 감싼 글입니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **앞서 만든 파일은 고치지 않습니다.** 이번 Unit에서 만드는 파일은 모두 새 파일입니다. 앞 Exercise 파일이 없으면 문서 맨 아래 「앞 Exercise 파일 완성본」으로 먼저 만듭니다.

---
