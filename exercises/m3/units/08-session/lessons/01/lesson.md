---
id: m3-u08-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/090_day05_am_revoke.md
  mission_id: GichanSource.m3-1030-am-revoke
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 개요

어제 10/29(목)에는 부여돼 있는 권한을 점검해서 **회수 대상 8건**을 찾았습니다. 오늘 오전에는 그 8건을 실제로 **회수**(권한을 없애는 일)합니다. 단, 바로 지우지 않고 계획 → 승인 → 실행 순서로 합니다.

- **2교시**: 회수 대상마다 어떤 방법으로 회수할지, 몇 건의 권한이 사라지는지 **회수 계획**을 세운다(아직 지우지 않는다).
- **3교시**: 쓰기 권한 같은 **민감한 권한**은 보안 책임자의 승인이 필요합니다. 승인이 필요한 계획을 가려 **승인 상태**를 적는다.
- **4교시**: 승인 대기가 아닌 계획만 **실행**하고, 회수 전후의 판정을 비교하고, **회수 이력**을 파일로 남긴다.

오늘은 오전 2 · 3 · 4교시, 오후 5 · 6교시이고, 깃허브에 올리는 일은 6교시 마지막에 합니다. 교시마다 문제는 하나입니다. 오늘 회수는 파일 자체를 고치지 않고, 프로그램이 파일에서 읽어 둔 **메모리 안의 데이터**(`USERS` · `ROLES` · `EXCEPTIONS`)를 바꿉니다. 프로그램을 끄면 처음 상태로 돌아가고, 파일로 저장하는 것은 회수 이력뿐입니다.

> 📦 **10/29(목)에 결석했다면**: 아래 2교시 문제의 `revoke_input.py` 에서 「결석한 학생용」 코드를 붙여 넣습니다. 어제 점검 결과(회수 대상 8건)가 그대로 들어 있어서, 10/29(목) 파일이 없어도 오늘 수업을 따라올 수 있습니다.
> - 10/29(목)에 출석했다면 「결석한 학생용」 코드는 쓰지 않고 위 코드를 붙여 넣습니다.
> - 10/21(수) ~ 10/22(목) 파일이 없으면 `day02_recovery` 폴더도 필요합니다.
> - 넣는 방법은 아래 「시작하기」 2번에 있습니다.

**📎 오늘 불러 쓰는 이전 파일** — 오늘 코드가 `import` 로 가져다 쓰는 앞 수업 파일입니다. 없으면 오른쪽 열의 방법으로 먼저 준비합니다.

| 파일 | 만든 날 | 오늘 가져다 쓰는 것 | 쓰는 교시 | 없으면 |
|---|---|---|---|---|
| `rbac.py` | 10/21(수) | `USERS` · `ROLES` (`config/users.json` · `config/roles.json`) | 2 · 3 · 4교시 | `day02_recovery` 폴더(10/21(수) · 10/22(목) 파일의 완성본) |
| `exception_policy.py` | 10/22(목) | `EXCEPTIONS` · `TIME_FORMAT` (`config/exceptions.json`) | 4교시 | `day02_recovery` 폴더(10/21(수) · 10/22(목) 파일의 완성본) |
| `policy.py` | 10/22(목) | `evaluate_access` | 4교시 | `day02_recovery` 폴더(10/21(수) · 10/22(목) 파일의 완성본) |
| `config_loader.py` | 10/22(목) | `load_json` | 3 · 4교시 | `day02_recovery` 폴더(10/21(수) · 10/22(목) 파일의 완성본) |
| `review_list.py` · `review_rules.py` · `review_unused.py` · `config/access_log.json` | 10/29(목) 오전 | `build_access_list` · `find_stale` · `find_unused` | 2 · 4교시 | 2교시 문제의 「결석한 학생용」 `revoke_input.py` (10/29(목) 파일이 없어도 됨) |
| `overprivilege.py` · `report_exclude.py` · `config/exclude_list.json` | 10/29(목) 오후 | `generate_report` · `split_by_exclude` | 2 · 4교시 | 2교시 문제의 「결석한 학생용」 `revoke_input.py` (10/29(목) 파일이 없어도 됨) |

- 오늘 만드는 파일도 뒤 교시가 가져다 씁니다. 2교시 `revoke_plan.py` 는 3 · 4교시에서, 3교시 `revoke_approve.py` 는 4교시에서 씁니다.

## 시작하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 어제까지의 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from rbac import USERS, ROLES; from policy import evaluate_access; from config_loader import load_json; from exception_policy import EXCEPTIONS, TIME_FORMAT; from review_list import build_access_list; from review_rules import find_stale; from review_unused import load_last_used; from overprivilege import generate_report; from report_exclude import load_exclude_map; print('이전 파일 정상', len(build_access_list()), len(load_last_used()), len(load_exclude_map('config/exclude_list.json')))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `이전 파일 정상 14 7 3`(현황 14건 · 사용 이력 7건 · 회수 제외 3건)이 나와야 합니다.
   - 10/29(목)에 결석해서 그 파일들이 없으면 이 확인은 건너뛰고, 2교시 문제의 `revoke_input.py` 에서 「결석한 학생용」 코드를 붙여 넣습니다.
   - 파일이 있는데 숫자가 다르면 10/29(목) 오전 · 오후 문서 맨 아래 「앞 교시 파일 완성본」으로 다시 만들고, 10/21(수) · 10/22(목) 파일이 없으면 `day02_recovery` 폴더에서 넣습니다.
3. **오늘 받은 파일 두 개를 `access_control` 폴더에 둡니다.** 이미 있으면 건너뜁니다. `다운로드` 폴더에서 VS Code 왼쪽의 그 폴더 위로 끌어다 놓습니다(안 되면 파일을 열어 **File › Save As…** 로 저장).
   - `day05_am_revoke.md` (이 파일) — 오전 실습 안내. 읽기만 합니다.
   - `day05_am_report.md` — **오전 보고서.** 2 · 3 · 4교시 답을 여기에 적습니다.
4. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. 보고서 `day05_am_report.md` 는 오른쪽 클릭 › **Open to the Side** 로 옆에 열고, 맨 위 제목 `(이름 · 2026-10-30(금))` 의 `이름` 만 내 이름으로 바꿉니다.
5. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.
   - 문자열(string)은 따옴표로 감싼 글입니다. `""` 는 문자가 하나도 없는 빈 문자열입니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **어제까지의 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다. 앞 교시 파일이 없으면 문서 맨 아래 「앞 교시 파일 완성본」으로 먼저 만듭니다.

---
