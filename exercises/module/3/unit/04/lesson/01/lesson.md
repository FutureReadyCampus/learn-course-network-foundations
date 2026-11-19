---
id: m3-u04-l01
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

Unit 2와 Unit 3에서는 역할 부여와 회수, 기간이 정해진 예외, 최종 판정 함수 `evaluate_access`(`policy.py`)를 만들었습니다. 이번 Unit에서는 직원이 권한을 달라고 하는 **요청**을 기록으로 남기고, 승인하고, 정책으로 한 번 더 확인해서 Unit 2의 예외 권한을 부여하는 흐름을 만듭니다.

- **실습 4-1**: 요청을 요청서 한 장(딕셔너리)으로 적어 리스트에 모으고, 접수할 수 없는 요청을 걸러 낸다.
- **실습 4-2**: 보안 담당이 요청서를 승인하거나 반려하고, 이미 처리한 요청서는 다시 처리하지 못하게 막는다.
- **실습 4-3**: 승인된 요청서를 정책으로 한 번 더 확인하고, 통과한 것만 예외 권한을 부여한다.

이번 Unit은 실습 4-1 · 4-2 · 4-3으로 이루어집니다. 실습마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 깃허브에 올리는 일은 Unit 5의 실습 5-2 마지막에 한 번에 합니다.

## 터미널 열고 Unit 3 파일 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 Unit 3까지 만든 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from datetime import datetime; from policy import evaluate_access; from exception_policy import EXCEPTIONS; print('이전 파일 정상', len(EXCEPTIONS)); print(evaluate_access('dami', 'SALES', 'QUERY', datetime(2026, 10, 23, 10, 0)))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 두 줄에 `이전 파일 정상 5` 와 `(False, '퇴사한 계정')` 이 나와야 합니다.
   - 파일이 없거나 결과가 다르면 Unit 1 ~ Unit 3 레슨의 코드 상자(「정답」 레슨 포함)로 빠진 파일을 만듭니다(`config` 안의 파일은 `config` 폴더에). 그다음 마지막 줄을 다시 칩니다.
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u4.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **Unit 3까지 만든 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다. 앞 실습 파일이 없으면 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」으로 먼저 만듭니다.

---
