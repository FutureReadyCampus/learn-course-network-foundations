---
id: m3-u06-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/086_day04_am_access_review.md
  mission_id: GichanSource.m3-1029-am-access-review
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 개요

지난 10/23(금)까지는 권한을 **주는** 흐름(요청 → 승인 → 예외 권한 부여 → 기한 점검 → 기록 저장)을 만들었습니다. 오늘 오전에는 반대로 이미 **부여돼 있는 권한** 가운데 필요 없어진 것을 찾는 **접근 점검**을 만듭니다.

- **Exercise 6-1**: 지금 누가 어떤 권한을 어떤 방법(역할 · 예외)으로 갖고 있는지 **현황 리스트**를 만든다.
- **Exercise 6-2**: 현황 리스트에서 **규칙**으로 필요 없어진 권한(퇴사한 사람, 만료된 예외)을 찾는다.
- **Exercise 6-3**: 규칙으로는 못 찾는 권한을 찾는다.

오늘은 오전 2 · 3 · Exercise 6-3, 오후 5 · Exercise 5-2이고, 깃허브에 올리는 일은 Exercise 5-2 마지막에 한 번에 합니다. Exercise마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 오늘은 **찾기까지만** 하고, 찾은 권한을 실제로 회수하는 일은 내일(10/30(금)) 합니다.

> **앞 수업에 결석했거나 파일이 없다면**: 수업 자료의 `unit03_recovery` 폴더는 10/21(수) ~ 10/22(목)에 만든 파일의 완성본입니다. 이 폴더로 오늘 수업을 따라올 수 있습니다.
> - 들어 있는 것: `rbac.py` · `exception_policy.py` · `config_loader.py` · `policy.py` 와 `config` 폴더(`users.json` · `roles.json` · `exceptions.json`).
> - 오늘은 10/23(금)에 만든 파일을 쓰지 않으므로, 10/23(금)에 결석했어도 따로 준비할 것이 없습니다.
> - 넣는 방법은 아래 「시작하기」 2번에 있습니다.

** 오늘 불러 쓰는 이전 파일** — 오늘 코드가 `import` 로 가져다 쓰는 앞 수업 파일입니다. 없으면 오른쪽 열의 방법으로 먼저 준비합니다.

| 파일 | 만든 날 | 오늘 가져다 쓰는 것 | 쓰는 Exercise | 없으면 |
|---|---|---|---|---|
| `rbac.py` | 10/21(수) | `USERS` · `ROLES` (`config/users.json` · `config/roles.json`) | Exercise 6-1 (3 · Exercise 6-3는 `review_list.py` 를 거쳐 씀) | `unit03_recovery` 폴더 |
| `exception_policy.py` | 10/22(목) | `EXCEPTIONS` · `TIME_FORMAT` (`config/exceptions.json`) | 2 · 3 · Exercise 6-3 | `unit03_recovery` 폴더 |
| `config_loader.py` | 10/22(목) | `load_json` | Exercise 6-3 | `unit03_recovery` 폴더 |

- 오늘 만드는 파일도 뒤 Exercise가 가져다 씁니다. Exercise 6-1 `review_list.py` 는 3 · Exercise 6-3에서, Exercise 6-2 `review_rules.py` 는 Exercise 6-3에서 씁니다.

## 개요

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 이전 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from rbac import USERS, ROLES; from exception_policy import EXCEPTIONS, TIME_FORMAT; from config_loader import load_json; print('이전 파일 정상', len(USERS), len(ROLES), len(EXCEPTIONS))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `이전 파일 정상 6 5 5`(사용자 6명 · 역할 5개 · 예외 5건)가 나와야 합니다.
   - 아니면 수업 자료의 `unit03_recovery` 폴더 파일을 `access_control` 폴더에 넣고(`config` 안의 파일은 `config` 폴더에) 마지막 줄을 다시 칩니다.
3. **오늘 받은 파일 두 개를 `access_control` 폴더에 둡니다.** 이미 있으면 건너뜁니다. `다운로드` 폴더에서 VS Code 왼쪽의 그 폴더 위로 끌어다 놓습니다(안 되면 파일을 열어 **File › Save As…** 로 저장).
   - Unit 6 (이 파일) — 오전 실습 안내. 읽기만 합니다.
   - Unit 6 — **오전 보고서.** 2 · 3 · Exercise 6-3 답을 여기에 적습니다.
4. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. 보고서 Unit 6 는 오른쪽 클릭 › **Open to the Side** 로 옆에 열고, 맨 위 제목 `(이름 · 2026-10-29(목))` 의 `이름` 만 내 이름으로 바꿉니다.
5. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **이전 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다. 앞 Exercise 파일이 없으면 문서 맨 아래 「앞 Exercise 파일 완성본」으로 먼저 만듭니다.

---
