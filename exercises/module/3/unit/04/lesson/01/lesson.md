---
id: m3-u04-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/090_day05_am_revoke.md
  mission_id: GichanSource.m3-1030-am-revoke
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표와 오늘의 계획

Unit 3 점검에서는 이미 부여돼 있는 권한을 살펴 **회수 대상 8건**을 찾았습니다. 오늘은 그 8건을 실제로 **회수**(권한을 없애는 일)합니다. 다만 바로 지우지 않고 **계획 → 승인 → 실행** 순서로 합니다.

**오늘의 계획 (3시간)**

1. 시작하기 15분: 이 레슨을 읽고 앞 Unit 파일을 확인한 뒤, 「제공 파일」 레슨의 파일 두 개를 만듭니다.
2. 실습 약 110분: 핵심 실습 두 개를 차례로 합니다.
3. 글쓰기 40분: 「보고서 쓰기」 레슨에서 핵심 실습의 질문에 답하고, 「오늘의 글 쓰기」 레슨에서 글 한 편을 씁니다.
4. 마무리 15분: 실습 4-2 끝의 「이번 Unit 마무리」에서 파일을 확인하고 깃허브에 올립니다.

**오늘 먼저 받아 쓰는 것** — 「제공 파일」 레슨의 완성 코드 두 개입니다.

1. `revoke_input.py`: Unit 3 점검을 다시 해서 회수 대상 8건을 리스트로 돌려주는 함수 `load_to_revoke`
2. `revoke_plan.py`: 회수 대상마다 회수 방법(예외 삭제 · 역할 해제 · 역할에서 권한 빼기)과 영향(사라지는 권한 수)을 적은 **회수 계획**을 만드는 함수 `plan_revocation`. 계획만 세우고 실제로는 아무것도 지우지 않습니다.

**오늘 만들 것 두 가지**

1. **실습 4-1**: 쓰기 권한처럼 **민감한 권한**이거나 한 번에 권한이 여러 개 사라지는 계획을 가려, 계획마다 **승인 상태**를 적는 함수 `mark_approvals` 를 `revoke_approve.py` 에 씁니다.
2. **실습 4-2**: 승인 대기가 아닌 계획만 **실행**하는 함수 `execute_revocation` 을 `revoke.py` 에 쓰고, 회수 전후의 판정을 비교하고, **회수 이력**을 파일로 남깁니다.

**도전 4-1 ~ 4-3은 선택입니다.** 핵심 실습 두 개와 글쓰기를 마치고 시간이 남을 때 합니다. 도전 4-1에서는 제공 파일 `revoke_plan.py` 를 직접 써 보고, 도전 4-2 · 4-3에서는 업무 시간 · 접속 위치 조건으로 판정하는 함수와 그 판정을 주소로 묻는 서버를 만듭니다. 도전을 하지 않아도 다음 Unit을 따라갈 수 있습니다.

오늘의 회수는 설정 파일 자체를 고치지 않습니다. 프로그램이 파일에서 읽어 둔 **메모리 안의 데이터**(`USERS` · `ROLES` · `EXCEPTIONS`)를 바꿉니다. 프로그램을 끝내면 처음 상태로 돌아가고, 파일로 저장하는 것은 회수 이력뿐입니다.

## 폴더 열고 이전 파일 확인하기

오늘 코드는 앞 Unit 파일을 `import` 로 불러 씁니다. 먼저 `access_control` 폴더에 아래 파일이 있는지 봅니다.

1. **Unit 1 파일**(꼭 있어야 합니다)
   1. 실습 1-1의 `config/users.json` · `config/roles.json`
   2. 실습 1-2의 `rbac.py`(`USERS` · `ROLES`)
   3. 실습 1-3의 `policy.py`(`evaluate_access`)
   4. Unit 1 제공 파일의 `exception_policy.py` · `config_loader.py` · `config/exceptions.json`
2. **Unit 3 파일**(있으면 씁니다)
   1. 실습 3-1의 `review_list.py`, 실습 3-2의 `review_unused.py` · `config/access_log.json`
   2. Unit 3 제공 파일의 `review_rules.py` · `overprivilege.py` · `report_exclude.py`
   3. 회수 제외 리스트 `config/exclude_list.json`(Unit 3 「제공 파일」 레슨에서 만듭니다)

**순서**

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 Unit 1 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from rbac import USERS, ROLES; from policy import evaluate_access; from config_loader import load_json; from exception_policy import EXCEPTIONS, TIME_FORMAT; print('Unit 1 파일 정상', len(USERS), len(ROLES), len(EXCEPTIONS))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `Unit 1 파일 정상 6 5 5`(사용자 6명 · 역할 5개 · 예외 5건)가 나와야 합니다.
   - 아니면 Module 3 Unit 1 레슨(실습 1-1 ~ 1-3, 제공 파일, 정답)의 코드 상자로 빠진 파일을 만들고 다시 칩니다.
3. **[터미널]** Unit 3 파일을 확인합니다.
   ```bash
   python -c "from review_list import build_access_list; from review_rules import find_stale; from review_unused import load_last_used; from overprivilege import generate_report; from report_exclude import load_exclude_map; print('Unit 3 파일 정상', len(build_access_list()), len(load_last_used()), len(load_exclude_map('config/exclude_list.json')))"
   ```
   - 마지막 줄에 `Unit 3 파일 정상 14 7 3`(현황 14건 · 사용 이력 7건 · 회수 제외 3건)이 나오면 「제공 파일」 레슨의 `revoke_input.py` 에서 **Unit 3 파일이 있을 때** 코드를 씁니다.
   - 오류가 나거나 숫자가 다르면 **Unit 3 파일이 없을 때** 코드를 씁니다. 회수 대상 8건이 코드 안에 그대로 들어 있어서 Unit 3 파일 없이도 오늘 실습이 똑같이 돌아갑니다.
4. **[VS Code]** 「제공 파일」 레슨으로 가서 `revoke_input.py` 와 `revoke_plan.py` 를 만들고 실습 4-1로 돌아옵니다.
5. **파일은 이렇게 만듭니다.** 따로 내려받는 파일은 없고, 모두 코드 상자에서 복사해 만듭니다.
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u4.md` 는 「보고서 쓰기」 레슨의 틀을 복사해 만듭니다.
6. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 이 Unit 뒤쪽의 정답을 봅니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **앞 Unit 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다.

---
