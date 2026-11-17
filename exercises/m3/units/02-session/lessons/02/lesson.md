---
id: m3-u02-l02
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/078_day02_am_policy.md
  mission_id: GichanSource.m3-1022-am-policy
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 이번 Unit에서 할 일: 세 가지 상황

Unit 1에서는 사용자 → 역할 → 권한 표를 파일로 만들고, 판정 함수 `check_permission` 으로 허용 · 거부를 정했습니다. Unit 2에서는 그 정책을 현업에서 흔한 세 상황에 맞게 넓힙니다.

- **Exercise 2-1**: 인사팀 통보(입사 · 부서 이동 · 퇴사)에 맞춰 사용자의 역할을 부여하고 접근을 회수하는 함수를 만든다.
- **Exercise 2-2**: 역할에는 없지만 **정해진 시각까지만** 허용하는 예외 권한을 다루고, 끝났거나 퇴사자에게 남은 예외를 찾는다.
- **Exercise 2-3**: 역할 권한과 예외 권한을 합쳐 최종 판정하는 `policy.py` 를 만든다.

Unit 2는 Exercise 2-1 · 2-2 · 2-3으로 이루어집니다. Exercise마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 깃허브에 올리는 일은 Unit 3의 Exercise 3-2 마지막에 한 번에 합니다.

## 폴더 열고 받은 파일 준비하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치를 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다. Unit 1에서 만든 파일이 보이는지도 `ls` 로 봅니다.
   ```bash
   pwd
   ls
   ls config
   ```
   - `rbac.py` 와 `config` 안의 `users.json` · `roles.json` 이 보여야 합니다.
   - Unit 1의 `check_permission` 을 다 채웠는지도 `python exercise1-2_run.py`(맥북은 `python3 exercise1-2_run.py`)로 확인합니다. 아홉 줄이 나오고 `dami` 줄이 `False 퇴사한 계정` 이면 정상입니다.
   - 파일이 없거나 정상이 아니면 수업 자료로 받은 `rbac_recovery` 폴더 안의 `rbac.py` 를 `access_control` 폴더에 넣고, `config` 안의 두 파일을 `config` 폴더에 넣습니다.
   - `users.json` 에는 `seoyeon` · `junho` · `gaeun` · `dami` · `batch-night` · `tester` 여섯 명과 `employed` 칸이 있어야 합니다(Unit 1의 Exercise 1-1). 한 명이라도 빠지면 Exercise 2-2 단계 2 에서 `KeyError` 가 납니다.
3. **Unit 2에서 받은 파일 두 개를 `access_control` 폴더에 둡니다.** 이미 있으면 건너뜁니다. `다운로드` 폴더에서 VS Code 왼쪽의 그 폴더 위로 끌어다 놓습니다(안 되면 파일을 열어 **File › Save As…** 로 저장).
   - Unit 2 안내 파일(지금 읽는 이 파일) — 실습 안내입니다. 읽기만 합니다.
   - Unit 2 보고서 — **답을 적는 파일입니다.** Exercise 2-1 · 2-2 · 2-3 답을 여기에 적습니다.
4. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. Unit 2 보고서는 오른쪽 클릭 › **Open to the Side** 로 옆에 열고, 맨 위 제목 `(이름 · 2026-10-22(목))` 의 `이름` 만 내 이름으로 바꿉니다.
5. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **Unit 1에서 만든 `rbac.py` · `users.json` · `roles.json` 은 고치지 않습니다.** 오늘 바뀌는 설정은 새 파일에 씁니다.

---
