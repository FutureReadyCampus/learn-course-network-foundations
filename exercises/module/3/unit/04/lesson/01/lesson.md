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

## Unit 4에서 할 일: 계획, 승인, 실행으로 회수

M3 Unit 3에서는 필요 없어진 권한 후보를 찾았습니다. Unit 4의 핵심 실습에서는 먼저 회수 방법과 승인을 기록하고, 승인된 회수만 실행한 뒤 결과를 확인하고 이력을 남깁니다.

- **실습 4-1**: 계획마다 승인이 필요한지, 승인됐는지 적습니다. 아직 권한을 지우지 않습니다.
- **실습 4-2**: 승인된 계획을 실행하고, 회수 전후의 접근 판정과 이력을 확인합니다.
- **응용 4-1~4-3**: 회수 계획을 분석하고 시간·위치 조건과 판정 서버를 만듭니다. 선택 과제입니다.

핵심 실습과 고민을 마친 뒤 「문제 해결 과정을 블로그에 기록하기」에서 결과를 남깁니다. 블로그 설정이 아직 없다면 M3 Unit 1의 Jekyll/GitHub Pages 설정을 먼저 마칩니다.

> **M3 Unit 1 준비**: `rbac.py`, `exception_policy.py`, `policy.py`, `config_loader.py`와 `config` 안의 사용자·역할·예외 설정이 필요합니다. 준비되어 있지 않다면 [M3 Unit 1 시작하기](__SITE__/exercises/module/3/unit/1/lesson/1/page/1)로 돌아가 설정합니다.
>
> **회수 대상 데이터**: 핵심 실습은 M3 Unit 3 시나리오의 회수 대상 8건을 고정 입력으로 사용합니다. 다음 준비 레슨에서 `revoke_input.py`를 만들어 주므로 M3 Unit 3의 응용 문제를 하지 않아도 진행할 수 있습니다.

## 폴더 열고 이전 설정 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal**로 터미널을 엽니다.
2. **[터미널]** 위치와 M3 Unit 1 파일을 확인합니다. 결과가 `…/network-study-notes/access_control`로 끝나야 합니다.
   ```bash
   pwd
   ls config
   python - <<'PYTHON'
   from rbac import USERS, ROLES
   from exception_policy import EXCEPTIONS, TIME_FORMAT
   from policy import evaluate_access
   from config_loader import load_json

   print("Unit 1 설정 정상", len(USERS), len(ROLES), len(EXCEPTIONS))
   PYTHON
   ```
   맥북은 `python`을 `python3`로 바꿉니다. 사용자 6명 · 역할 5개 · 예외 5건이면 정상입니다. 파일이 없으면 위의 M3 Unit 1 링크에서 만듭니다.
3. **파일 만들기**: 지정한 이름의 파일을 VS Code의 **New File**로 만들고, 해당 코드 상자 내용을 붙여 넣어 저장합니다. `Ctrl + S`(맥북은 `Cmd + S`)를 누릅니다.
4. 코드는 할 일 순서대로 작성합니다. 막히면 해당 실습 바로 뒤의 「정답과 해설 보기」를 확인합니다. 이전 Unit에서 만든 파일은 수정하지 않습니다.

> 실행은 VS Code의 ▶ 단추가 아니라 터미널에서 합니다. 터미널 위치가 `access_control`인지 `pwd`로 확인한 뒤 실행합니다.

---
