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

## 개요

어제(10/22(목))에는 역할 부여와 회수, 기간이 정해진 예외, 최종 판정 함수 `evaluate_access`(`policy.py`)를 만들었습니다. 오늘 오전에는 직원이 권한을 달라고 하는 **요청**을 기록으로 남기고, 승인하고, 정책으로 한 번 더 확인해서 어제의 예외 권한을 부여하는 흐름을 만듭니다.

- **2교시**: 요청을 요청서 한 장(딕셔너리)으로 적어 리스트에 모으고, 접수할 수 없는 요청을 걸러 낸다.
- **3교시**: 보안 담당이 요청서를 승인하거나 반려하고, 이미 처리한 요청서는 다시 처리하지 못하게 막는다.
- **4교시**: 승인된 요청서를 정책으로 한 번 더 확인하고, 통과한 것만 예외 권한을 부여한다.

오늘 수업은 오전 2 · 3 · 4교시와 오후 5 · 6교시이고 7교시는 없습니다. 교시마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 깃허브에 올리는 일은 오후 6교시 마지막에 한 번에 합니다.

## 시작하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 어제 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from datetime import datetime; from policy import evaluate_access; from exception_policy import EXCEPTIONS; print('어제 파일 정상', len(EXCEPTIONS)); print(evaluate_access('dami', 'SALES', 'QUERY', datetime(2026, 10, 23, 10, 0)))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 두 줄에 `어제 파일 정상 5` 와 `(False, '퇴사한 계정')` 이 나와야 합니다.
   - 파일이 없거나 결과가 다르면 수업 자료의 `day02_recovery` 폴더 파일을 `access_control` 폴더에 넣고(`config` 안의 파일은 `config` 폴더에) 마지막 줄을 다시 칩니다.
3. **오늘 받은 파일 두 개를 `access_control` 폴더에 둡니다.** 이미 있으면 건너뜁니다. `다운로드` 폴더에서 VS Code 왼쪽의 그 폴더 위로 끌어다 놓습니다(안 되면 파일을 열어 **File › Save As…** 로 저장).
   - `day03_am_request.md` (이 파일) — 오전 실습 안내. 읽기만 합니다.
   - `day03_am_report.md` — **오전 보고서.** 2 · 3 · 4교시 답을 여기에 적습니다.
4. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. 보고서 `day03_am_report.md` 는 오른쪽 클릭 › **Open to the Side** 로 옆에 열고, 맨 위 제목 `(이름 · 2026-10-23(금))` 의 `이름` 만 내 이름으로 바꿉니다.
5. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **어제까지 만든 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다. 앞 교시 파일이 없으면 문서 맨 아래 「앞 교시 파일 완성본」으로 먼저 만듭니다.

---
