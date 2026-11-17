---
id: m3-u01-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/075_day01_pm_rbac.md
  mission_id: GichanSource.m3-1021-pm-rbac
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 개요

2과목(네트워크 · Zero Trust)을 마쳤습니다. Unit 1부터 3과목 **접근통제 자동화**를 시작합니다. 2과목에서는 요청을 점수로 판단했습니다(PDP). 3과목에서는 그 판단의 바탕이 되는 **「누가 무엇을 해도 되나」를 표로 정하고 코드로 지키는 일**을 합니다. 회사는 2과목의 **A사**를 그대로 씁니다.

- **Exercise 1-1**: 사용자 · 역할 · 권한을 표로 읽고, 사용자 파일과 역할 파일을 직접 쓴다.
- **Exercise 1-2**: 두 파일을 읽어 권한을 판정하는 함수를 직접 쓴다(코드 다섯 곳).
- **Exercise 1-3**: 2과목의 접속 기록을 그 함수로 다시 판정하고, 한 번도 안 쓰인 권한을 찾는다(코드 두 부분).

**3과목 전체 지도** — 접근통제 자동화는 사람마다 할 수 있는 일을 정하고, 그 권한을 주고 · 점검하고 · 거두는 일을 코드로 자동화합니다. 입사 · 부서 이동 · 퇴사 때마다 권한이 바뀌어서 손으로 하면 놓치기 때문입니다.

| 단계 | Unit | 하는 일 |
|---|---|---|
| ① 정하기 | Unit 1 ~ Unit 3 | 누가 무엇을 해도 되는지 표로 정함(RBAC) |
| ② 주기 | Unit 4 ~ Unit 5 | 권한 요청 → 승인 → 부여 |
| ③ 점검 | Unit 6 ~ Unit 7 | 안 쓰는 권한 · 넘치는 권한 찾기 |
| ④ 거두기 | Unit 8 ~ Unit 9 | 권한 회수 · 조건 · 예외 · 판정 서버 |
| ⑤ 보고 | Unit 10 | 한 주 점검 결과를 리포트로 |

Unit 1은 ① 정하기 단계의 시작입니다.

## 시작하기 순서

1. **[VS Code]** 왼쪽 목록의 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치를 확인합니다. 결과가 `…/security-agent-toolkit` 으로 끝나야 합니다.
   ```bash
   pwd
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치를 보여 줌
3. **[터미널]** 3과목 폴더 `access_control` 과 그 안의 설정 폴더 `config` 를 만들고, 과목 폴더로 들어갑니다. Unit 1부터 3과목의 파일은 모두 이 폴더에 둡니다.
   ```bash
   mkdir -p access_control/config
   cd access_control
   pwd
   ```
   - `mkdir -p` 는 폴더를 만들고(이미 있어도 오류 없음), 마지막 `pwd` 가 `…/security-agent-toolkit/access_control` 로 끝나면 됩니다.
   - 폴더는 이렇게 됩니다. `users.json` 과 `roles.json` 은 Exercise 1-1에서 만듭니다. Unit 1에서 받은 파일 두 개는 4번에서 옮깁니다.
     ```
     security-agent-toolkit/
       network_zt/          2과목
       access_control/      3과목 · Unit 1부터
         config/
           users.json
           roles.json
         Unit 1 안내 파일
         Unit 1 보고서
     ```
4. **Unit 1에서 받은 파일 두 개를 `access_control` 폴더에 둡니다.** `다운로드` 폴더에서 VS Code 왼쪽의 그 폴더 위로 끌어다 놓습니다.
   - Unit 1 안내 파일(지금 읽는 이 파일) — 실습 안내입니다. 읽기만 합니다.
   - Unit 1 보고서 — **답을 적는 파일입니다.** Exercise 1-1 · 1-2 · 1-3 답을 여기에 적습니다.
5. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. Unit 1 보고서는 오른쪽 클릭 › **Open to the Side** 로 옆에 엽니다.
6. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 오늘 명령은 모두 **터미널**에서 칩니다. `python` 이 없다는 오류가 나오면 `python3` 으로 칩니다(맥북은 `python3`). 오늘 나오는 이름 · 자원 · 숫자는 연습용 예시입니다. 계정과 자원은 2과목의 A사 것과 같습니다.

---
