---
id: m3-u02-l02
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/082_day03_am_request.md
  mission_id: GichanSource.m3-1023-am-request
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 요청서 접수·승인·부여

Unit 2는 Module 3의 두 번째 단계인 **권한 주기**입니다. Unit 1 실습에서는 사용자 파일과 역할 파일을 읽어 허용 · 거부를 판정하는 `check_permission`(`rbac.py`)과, 기간을 정해 따로 허용한 예외까지 보는 최종 판정 함수 `evaluate_access`(`policy.py`)를 만들었습니다. 이번 Unit에서는 직원이 권한을 달라고 하는 **요청**을 요청서로 받아 기록으로 남기고, 보안 담당이 승인하거나 반려(받아들이지 않고 돌려보냄)하는 흐름을 만듭니다.

**오늘의 계획 (3시간)**

1. 시작하기 15분: 이 레슨을 읽고 Unit 1 파일이 있는지 확인합니다. 자리를 옮겼다면 그 전에 앞의 「준비 · 새 자리에서 내 깃허브 연결하기」 레슨으로 내 폴더를 받아 둡니다.
2. 실습 약 110분: 핵심 실습 두 개를 차례로 합니다. 실습 2-2를 마치면 「제공 파일」 `req_grant.py` 를 복사해 만듭니다.
3. 글쓰기 40분: 「보고서 쓰기」 레슨에서 핵심 실습의 질문에 답하고, 「오늘의 글 쓰기」 레슨에서 글 한 편을 씁니다.
4. 마무리 15분: 실습 2-2 끝의 「이번 Unit 마무리」에서 파일을 확인하고 깃허브에 올립니다.

**오늘 만들 것 두 가지**

1. **실습 2-1**: 요청 하나를 요청서 한 장(딕셔너리)으로 적어 리스트에 모으는 함수 `create_request` 를 `req_create.py` 에 직접 씁니다. 접수할 수 없는 요청은 이유와 함께 걸러 냅니다.
2. **실습 2-2**: 보안 담당이 요청서를 승인하거나 반려하는 함수 `approve_request` · `reject_request` 를 `req_review.py` 에 직접 씁니다. 이미 처리한 요청서와 본인 요청은 막습니다.

「제공 파일」 `req_grant.py` 는 승인된 요청서를 정책으로 한 번 더 확인하고, 통과한 것만 예외 권한을 주는 함수 `grant_request` 입니다. 직접 쓰지 않고 완성본을 복사해 둡니다.

**도전 2-1 ~ 2-3은 선택입니다.** 핵심 실습 두 개와 글쓰기를 마치고 시간이 남을 때 합니다. 도전 2-1은 `grant_request` 를 직접 써 보고, 도전 2-2는 처리 기한(SLA · 에스엘에이, 정해 둔 시간 안에 처리하겠다는 약속)을 넘긴 요청서를 찾고, 도전 2-3은 요청서 전체를 파일로 저장합니다. 도전을 하지 않아도 다음 Unit을 따라가는 데 문제가 없습니다.

## 터미널 열고 앞에서 만든 파일 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from datetime import datetime; from policy import evaluate_access; from exception_policy import EXCEPTIONS; print('이전 파일 정상', len(EXCEPTIONS)); print(evaluate_access('dami', 'SALES', 'QUERY', datetime(2026, 10, 23, 10, 0)))"
   ```
   - 명령 풀이: `python -c "…"` 따옴표 안의 파이썬 코드를 파일로 만들지 않고 바로 실행함. 여기서는 Unit 1 파일을 불러와 예외 수를 세고, `dami` 의 영업 실적 조회를 판정해 봅니다.
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 두 줄에 `이전 파일 정상 5` 와 `(False, '퇴사한 계정')` 이 나와야 합니다. `dami` 는 Unit 1 사용자 파일에서 퇴사로 적힌 계정이라 거부가 맞습니다.
3. 오늘 코드는 아래 파일을 불러 씁니다. `ls` 와 `ls config` 에 모두 보여야 합니다.
   1. `config/users.json` · `config/roles.json`: 사용자 파일과 역할 파일. 없으면 Unit 1 정답 레슨의 실습 1-1 정답에서 복사해 만듭니다.
   2. `rbac.py`: 사용자 딕셔너리 `USERS` 와 역할 판정 함수 `check_permission`. 없으면 Unit 1 실습 1-2 레슨의 `rbac.py` 코드 상자를 붙여 넣고, 빈칸을 Unit 1 정답 레슨의 실습 1-2 채운 코드로 채웁니다.
   3. `config/exceptions.json` · `exception_policy.py` · `config_loader.py`: 예외 파일, 예외 리스트 `EXCEPTIONS` 와 시각 형식 `TIME_FORMAT`, 안전한 읽기 함수 `load_json`. 없으면 Unit 1 「제공 파일」 레슨에서 복사해 만듭니다.
   4. `policy.py`: 최종 판정 함수 `evaluate_access`. 없으면 Unit 1 실습 1-3 레슨의 `policy.py` 코드 상자를 붙여 넣고, 빈칸을 Unit 1 정답 레슨의 실습 1-3 채운 코드로 채웁니다.
   - `config` 안의 파일은 `config` 폴더에 만듭니다. 만든 뒤 2번의 마지막 줄을 다시 칩니다.
4. **파일은 이렇게 만듭니다.** 이 Unit의 파일은 모두 레슨의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u2.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
5. 실습은 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 이 Unit 뒤쪽의 정답을 봅니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). 3번의 파일은 오늘 고치지 않고 불러 쓰기만 합니다. 오늘 만드는 파일은 모두 새 파일입니다.

---
