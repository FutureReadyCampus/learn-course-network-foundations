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

## 목표: 세 가지 상황

Unit 1에서는 사용자 → 역할 → 권한 표를 파일로 만들고, 판정 함수 `check_permission` 으로 허용 · 거부를 정했습니다. Unit 2에서는 그 정책을 현업에서 흔한 세 상황에 맞게 넓힙니다.

- **실습 2-1**: 인사팀 통보(입사 · 부서 이동 · 퇴사)에 맞춰 사용자의 역할을 부여하고 접근을 회수하는 함수를 만든다.
- **실습 2-2**: 역할에는 없지만 **정해진 시각까지만** 허용하는 예외 권한을 다루고, 끝났거나 퇴사자에게 남은 예외를 찾는다.
- **실습 2-3**: 역할 권한과 예외 권한을 합쳐 최종 판정하는 `policy.py` 를 만든다.

Unit 2는 실습 2-1 · 2-2 · 2-3으로 이루어집니다. 실습마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 깃허브에 올리는 일은 Unit 3의 실습 3-2 마지막에 한 번에 합니다.

## 폴더 열고 파일 준비하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치를 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다. Unit 1에서 만든 파일이 보이는지도 `ls` 로 봅니다.
   ```bash
   pwd
   ls
   ls config
   ```
   - `rbac.py` 와 `config` 안의 `users.json` · `roles.json` 이 보여야 합니다.
   - Unit 1의 `check_permission` 을 다 채웠는지도 `python exercise1-2_run.py`(맥북은 `python3 exercise1-2_run.py`)로 확인합니다. 아홉 줄이 나오고 `dami` 줄이 `False 퇴사한 계정` 이면 정상입니다.
   - 파일이 없거나 정상이 아니면 Unit 1 의 코드 상자(실습 1-2 의 `rbac.py` 와 「정답」 레슨, 실습 1-1 의 `users.json` · `roles.json`)로 `rbac.py` 를 `access_control` 폴더에, 두 json 파일을 `config` 폴더에 다시 만듭니다.
   - `users.json` 에는 `seoyeon` · `junho` · `gaeun` · `dami` · `batch-night` · `tester` 여섯 명과 `employed` 칸이 있어야 합니다(Unit 1의 실습 1-1). 한 명이라도 빠지면 실습 2-2 단계 2 에서 `KeyError` 가 납니다.
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u2.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **Unit 1에서 만든 `rbac.py` · `users.json` · `roles.json` 은 고치지 않습니다.** 오늘 바뀌는 설정은 새 파일에 씁니다.

---
