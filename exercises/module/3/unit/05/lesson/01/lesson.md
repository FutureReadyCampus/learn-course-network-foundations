---
id: m3-u05-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/084_day03_pm_sla.md
  mission_id: GichanSource.m3-1023-pm-sla
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 기한 점검과 기록 저장

Unit 4에서는 요청을 요청서로 접수하고(`req_create.py`), 승인 · 반려하고(`req_review.py`), 정책으로 확인해 예외 권한을 부여하는(`req_grant.py`) 흐름을 만들었습니다. 이번 Unit에서는 그 흐름이 **정해진 시간 안에** 처리되는지 점검하고, 요청서를 **파일로 저장**해 이력(처리 기록)으로 남깁니다.

- **실습 5-1**: 접수한 지 정해진 시간(SLA, 처리 기한)이 지났는데도 처리되지 않은 요청서를 찾는다.
- **실습 5-2**: 요청서 전체를 `requests.json` 으로 저장하고, 상태별 건수를 센다. 마지막에 이번 Unit에서 만든 것을 깃허브에 올린다.

이번 Unit은 실습 5-1 · 5-2로 이루어집니다. 실습마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 깃허브에 올리는 일은 실습 5-2 마지막에 합니다.

## 터미널 열고 Unit 4 파일 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 Unit 4의 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   python -c "from rbac import check_permission; from exception_policy import EXCEPTIONS; from config_loader import load_json; from req_grant import grant_request; print('Unit 4 파일 정상')"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `Unit 4 파일 정상` 이 나와야 합니다.
   - 아니면 Unit 4 의 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」으로 `req_create.py` · `req_review.py` · `req_grant.py` 를 만들고, `rbac.py` · `exception_policy.py` · `config_loader.py` 가 없으면 Unit 1 ~ Unit 3 레슨의 코드 상자로 만듭니다. 그다음 마지막 줄을 다시 칩니다.
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u5.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 **터미널**에서 합니다(VS Code 의 ▶ 단추를 쓰지 않습니다). `python` 이 없다는 오류가 나오면 `python3` 으로 칩니다(맥북은 `python3`). **Unit 4까지 만든 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다.

---
