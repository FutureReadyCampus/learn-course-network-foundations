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

## 개요

오전에는 요청을 요청서로 접수하고(`req_create.py`), 승인 · 반려하고(`req_review.py`), 정책으로 확인해 예외 권한을 부여하는(`req_grant.py`) 흐름을 만들었습니다. 오후에는 그 흐름이 **정해진 시간 안에** 처리되는지 점검하고, 요청서를 **파일로 저장**해 이력(처리 기록)으로 남깁니다.

- **5교시**: 접수한 지 정해진 시간(SLA, 처리 기한)이 지났는데도 처리되지 않은 요청서를 찾는다.
- **6교시**: 요청서 전체를 `requests.json` 으로 저장하고, 상태별 건수를 센다. 마지막 10분에 오늘 만든 것을 깃허브에 올린다.

오늘 오후는 5 · 6교시이고 7교시는 없습니다. 교시마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 깃허브에 올리는 일은 6교시 마지막에 합니다.

## 시작하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 오전 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   python -c "from rbac import check_permission; from exception_policy import EXCEPTIONS; from config_loader import load_json; from req_grant import grant_request; print('오전 파일 정상')"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `오전 파일 정상` 이 나와야 합니다.
   - 아니면 오전 문서(`day03_am_request.md`) 맨 아래 「앞 교시 파일 완성본」으로 `req_create.py` · `req_review.py` · `req_grant.py` 를 만들고, `rbac.py` · `exception_policy.py` · `config_loader.py` 가 없으면 `day02_recovery` 폴더에서 넣습니다. 그다음 마지막 줄을 다시 칩니다.
3. **[VS Code]** **오후에 받은 파일 두 개를 `access_control` 폴더로 옮깁니다.** 수업 자료에서 내려받은 파일은 보통 `다운로드` 폴더에 있습니다. 파일 탐색기(맥북은 Finder)에서 `다운로드` 폴더를 열고, 두 파일을 VS Code 왼쪽 목록의 `access_control` 폴더 위로 끌어다 놓습니다. 끌어다 놓기가 안 되면 파일을 VS Code 로 열고 메뉴 **File › Save As…** 로 `access_control` 폴더에 저장합니다.
   - `day03_pm_sla.md` (이 파일) — 오후 실습 안내. 읽기만 합니다.
   - `day03_pm_report.md` — **오후 보고서.** 5 · 6교시와 마무리 답을 여기에 적습니다.
4. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. 보고서 `day03_pm_report.md` 는 오른쪽 클릭 › **Open to the Side** 로 옆에 열고, 맨 위 제목 `(이름 · 2026-10-23(금))` 의 `이름` 만 내 이름으로 바꿉니다.
5. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 **터미널**에서 합니다(VS Code 의 ▶ 단추를 쓰지 않습니다). `python` 이 없다는 오류가 나오면 `python3` 으로 칩니다(맥북은 `python3`). **오전까지 만든 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다.

---
