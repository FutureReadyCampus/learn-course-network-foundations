---
id: m3-u03-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/086_day04_am_access_review.md
  mission_id: GichanSource.m3-1029-am-access-review
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 권한 접근 점검

Unit 2까지는 권한을 **주는** 흐름(요청 → 승인 → 예외 권한 부여 → 기한 점검 → 기록 저장)을 만들었습니다. 이번 Unit에서는 반대로 이미 **부여돼 있는 권한** 가운데 필요 없어진 것을 찾는 **접근 점검**을 만듭니다.

1. **실습 3-1**에서 역할과 예외로 받은 권한을 한 목록으로 모읍니다.
2. **핵심 실습 점검 함수 준비**에서 퇴사한 계정과 만료된 예외를 가려내는 `review_rules.py`를 만듭니다.
3. **실습 3-2**에서 남은 권한 중 90일 넘게 안 썼거나 사용 이력이 없는 권한을 찾습니다.
4. [문제 해결 과정을 블로그에 기록하기](__SITE__/exercises/module/3/unit/3/lesson/9/page/1)에서 결과와 판단 근거를 한 편의 글로 남깁니다. 응용은 글을 쓴 뒤 여유가 되면 진행합니다.

이번 Unit에서는 후보를 찾는 데까지 진행합니다. 실제 권한 회수는 Unit 4에서 다룹니다.

**Unit 1에서 준비한 코드와 설정**을 같은 `access_control` 폴더에서 불러옵니다. 빠진 항목은 아래 레슨에서 채웁니다.

| 필요한 것 | 지금 쓰는 곳 | 준비하는 곳 |
|---|---|---|
| `config/users.json` · `config/roles.json` | 실습 3-1의 사용자와 역할 | [M3 Unit 1 실습 1-1](__SITE__/exercises/module/3/unit/1/lesson/2/page/7) |
| `rbac.py` | 실습 3-1의 `USERS` · `ROLES` | [M3 Unit 1 실습 1-2](__SITE__/exercises/module/3/unit/1/lesson/3/page/4) |
| `config/exceptions.json` · `exception_policy.py` · `config_loader.py` | 실습 3-1의 예외 목록과 실습 3-2의 시각 형식 및 사용 이력 읽기 | [M3 Unit 1 예외 판정 준비](__SITE__/exercises/module/3/unit/1/lesson/4/page/1) |

## M3 Unit 1 파일과 작업 폴더 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 M3 Unit 1에서 만든 파일을 확인합니다. `pwd` 결과가 `…/network-study-notes/access_control`로 끝나야 합니다.
   Windows에서는 VS Code 터미널 프로필에서 **Git Bash**를 선택합니다. 아래 블록은 통째로 복사해서 실행합니다.

   ```bash
   # 이 명령은 전체를 복사해 Git Bash에 붙여 넣어 실행하세요.
   pwd
   ls
   ls config
   python - <<'PYTHON'
   from rbac import USERS, ROLES
   from exception_policy import EXCEPTIONS, TIME_FORMAT
   from config_loader import load_json

   print("이전 파일 정상", len(USERS), len(ROLES), len(EXCEPTIONS))
   PYTHON
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `이전 파일 정상 6 5 5`(사용자 6명 · 역할 5개 · 예외 5건)가 나와야 합니다.
   - 오류가 나면 위 표에서 빠진 파일을 만드는 레슨을 찾습니다. 같은 폴더에 저장한 뒤 블록 전체를 다시 실행합니다.
3. **코드 파일은 이렇게 만듭니다.** 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 실습 결과는 핵심 작업을 마친 뒤 「문제 해결 과정을 블로그에 기록하기」에서 한 편의 글로 정리합니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 실습 코드에서 ①·②를 찾아 채웁니다. 막히면 해당 실습 아래의 「정답과 해설 보기」를 엽니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **M3 Unit 1에서 만든 파일은 고치지 않습니다.** 이번 Unit에서 만드는 파일은 모두 새 파일입니다. 앞 실습에서 만든 파일은 같은 폴더에 둡니다.

---
