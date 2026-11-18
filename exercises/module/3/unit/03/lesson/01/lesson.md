---
id: m3-u03-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/080_day02_pm_tests.md
  mission_id: GichanSource.m3-1022-pm-tests
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 믿을 수 있는 정책

Unit 2에서는 역할 부여와 회수, 기간이 정해진 예외, 최종 판정 함수 `evaluate_access`(`policy.py`)를 만들었습니다. Unit 3에서는 그 정책을 **믿을 수 있게** 만듭니다.

- **실습 3-1**: 설정 파일이 없거나 깨져도 프로그램이 멈추지 않고 **빈 설정으로 이어지게** 한다(그 설정이면 모든 요청이 거부됩니다).
- **실습 3-2**: 정책이 정한 대로 움직이는지 **테스트 케이스**를 직접 설계해 자동으로 확인하고, 마지막에 오늘 만든 것을 올린다.

Unit 3은 실습 3-1 · 3-2로 이루어집니다. 실습마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 깃허브에 올리는 일은 실습 3-2 마지막에 합니다.

## 폴더 열고 Unit 2 파일 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 Unit 2의 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   ```
   - `rbac.py` · `role_admin.py` · `exception_policy.py` · `policy.py` · `exercise2-1_run.py` · `exercise2-2_run.py` · `exercise2-3_run.py` 가 보여야 하고, `config` 안에는 `users.json` · `roles.json` · `exceptions.json` 이 보여야 합니다. 없으면 Unit 2 의 「정답」 레슨 코드 상자로 먼저 만듭니다.
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u3.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 **터미널**에서 합니다(VS Code 의 ▶ 단추를 쓰지 않습니다). `python` 이 없다는 오류가 나오면 `python3` 으로 칩니다(맥북은 `python3`). **Unit 2까지 만든 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다.

---
