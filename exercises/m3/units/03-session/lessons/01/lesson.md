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

## 개요

오전에는 역할 부여와 회수, 기간이 정해진 예외, 최종 판정 함수 `evaluate_access`(`policy.py`)를 만들었습니다. 오후에는 그 정책을 **믿을 수 있게** 만듭니다.

- **5교시**: 설정 파일이 없거나 깨져도 프로그램이 멈추지 않고 **빈 설정으로 이어지게** 한다(그 설정이면 모든 요청이 거부됩니다).
- **6교시**: 정책이 정한 대로 움직이는지 **테스트 케이스**를 직접 설계해 자동으로 확인하고, 마지막 10분에 오늘 만든 것을 올린다.

오늘 오후는 5 · 6교시이고 7교시는 없습니다. 교시마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 깃허브에 올리는 일은 6교시 마지막에 합니다.

## 시작하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 오전 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   ```
   - `rbac.py` · `role_admin.py` · `exception_policy.py` · `policy.py` · `day02_2-1_run.py` · `day02_3-1_run.py` · `day02_4-1_run.py` 가 보여야 하고, `config` 안에는 `users.json` · `roles.json` · `exceptions.json` 이 보여야 합니다. 없으면 오전 문서(`day02_am_policy.md`)의 정답으로 먼저 만듭니다.
3. **[VS Code]** **오후에 받은 파일 두 개를 `access_control` 폴더로 옮깁니다.** 수업 자료에서 내려받은 파일은 보통 `다운로드` 폴더에 있습니다. 파일 탐색기(맥북은 Finder)에서 `다운로드` 폴더를 열고, 두 파일을 VS Code 왼쪽 목록의 `access_control` 폴더 위로 끌어다 놓습니다. 끌어다 놓기가 안 되면 파일을 VS Code 로 열고 메뉴 **File › Save As…** 로 `access_control` 폴더에 저장합니다.
   - `day02_pm_tests.md` (이 파일) — 오후 실습 안내. 읽기만 합니다.
   - `day02_pm_report.md` — **오후 보고서.** 5 · 6교시와 마무리 답을 여기에 적습니다.
4. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. 보고서 `day02_pm_report.md` 는 오른쪽 클릭 › **Open to the Side** 로 옆에 열고, 맨 위 제목 `(이름 · 2026-10-22(목))` 의 `이름` 만 내 이름으로 바꿉니다.
5. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 **터미널**에서 합니다(VS Code 의 ▶ 단추를 쓰지 않습니다). `python` 이 없다는 오류가 나오면 `python3` 으로 칩니다(맥북은 `python3`). **오전까지 만든 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다.

---
