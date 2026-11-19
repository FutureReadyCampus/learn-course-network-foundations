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

Unit 3과 Unit 3에서는 부여돼 있는 권한을 점검해서 **회수 대상 8건**을 찾았습니다. 이번 Unit에서는 그 8건을 실제로 **회수**(권한을 없애는 일)합니다. 단, 바로 지우지 않고 계획 → 승인 → 실행 순서로 합니다.

- **도전 4-1**: 회수 대상마다 어떤 방법으로 회수할지, 몇 건의 권한이 사라지는지 **회수 계획**을 세운다(아직 지우지 않는다).
- **실습 4-1**: 쓰기 권한 같은 **민감한 권한**은 보안 책임자의 승인이 필요합니다. 승인이 필요한 계획을 가려 **승인 상태**를 적는다.
- **실습 4-2**: 승인 대기가 아닌 계획만 **실행**하고, 회수 전후의 판정을 비교하고, **회수 이력**을 파일로 남긴다.

이번 Unit은 도전 4-1 · 실습 4-1 · 실습 4-2으로 이루어지고, 깃허브에 올리는 일은 Unit 4의 도전 4-3 마지막에 합니다. 실습마다 문제는 하나입니다.

이번 Unit의 회수는 파일 자체를 고치지 않습니다. 프로그램이 파일에서 읽어 둔 **메모리 안의 데이터**(`USERS` · `ROLES` · `EXCEPTIONS`)를 바꿉니다. 프로그램을 끄면 처음 상태로 돌아가고, 파일로 저장하는 것은 회수 이력뿐입니다.

> **Unit 3 · Unit 3의 파일이 없다면**: 아래 도전 4-1 문제의 `revoke_input.py` 에서 「Unit 3 · 7 파일이 없을 때용」 코드를 붙여 넣습니다. Unit 3의 점검 결과(회수 대상 8건)가 그대로 들어 있어서, Unit 3 · Unit 3의 파일이 없어도 이번 Unit을 따라올 수 있습니다.
> - Unit 3 · Unit 3의 파일이 있다면 「Unit 3 · 7 파일이 없을 때용」 코드는 쓰지 않고 위 코드를 붙여 넣습니다.
> - Unit 1 ~ Unit 1 파일이 없으면 그 레슨의 코드 상자로 먼저 만듭니다.
> - 넣는 방법은 아래 「시작하기」 2번에 있습니다.

**이번 Unit에서 불러 쓰는 이전 파일** — 이번 Unit의 코드가 `import` 로 가져다 쓰는, 앞서 만든 파일입니다. 없으면 오른쪽 열의 방법으로 먼저 준비합니다.

| 파일 | 만든 Unit | 이번 Unit에서 가져다 쓰는 것 | 쓰는 실습 | 없으면 |
|---|---|---|---|---|
| `rbac.py` | Unit 1 | `USERS` · `ROLES` (`config/users.json` · `config/roles.json`) | 도전 4-1 · 실습 4-1 · 실습 4-2 | Unit 1 ~ Unit 1 레슨의 코드 상자 |
| `exception_policy.py` | Unit 1 | `EXCEPTIONS` · `TIME_FORMAT` (`config/exceptions.json`) | 실습 4-2 | Unit 1 ~ Unit 1 레슨의 코드 상자 |
| `policy.py` | Unit 1 | `evaluate_access` | 실습 4-2 | Unit 1 ~ Unit 1 레슨의 코드 상자 |
| `config_loader.py` | Unit 1 | `load_json` | 실습 4-1 · 실습 4-2 | Unit 1 ~ Unit 1 레슨의 코드 상자 |
| `review_list.py` · `review_rules.py` · `review_unused.py` · `config/access_log.json` | Unit 3 | `build_access_list` · `find_stale` · `find_unused` | 도전 4-1 · 실습 4-1 · 실습 4-2 | 도전 4-1 문제의 「Unit 3 · 7 파일이 없을 때용」 `revoke_input.py` (Unit 3 · Unit 3 파일이 없어도 됨) |
| `overprivilege.py` · `report_exclude.py` · `config/exclude_list.json` | Unit 3 | `generate_report` · `split_by_exclude` | 도전 4-1 · 실습 4-1 · 실습 4-2 | 도전 4-1 문제의 「Unit 3 · 7 파일이 없을 때용」 `revoke_input.py` (Unit 3 · Unit 3 파일이 없어도 됨) |

- 이번 Unit에서 만드는 파일도 뒤 실습이 가져다 씁니다. 도전 4-1의 `revoke_plan.py` 는 실습 4-1 · 실습 4-2에서, 실습 4-1의 `revoke_approve.py` 는 실습 4-2에서 씁니다.

## 폴더 열고 Unit 3 · 7 파일 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 앞서 만든 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from rbac import USERS, ROLES; from policy import evaluate_access; from config_loader import load_json; from exception_policy import EXCEPTIONS, TIME_FORMAT; from review_list import build_access_list; from review_rules import find_stale; from review_unused import load_last_used; from overprivilege import generate_report; from report_exclude import load_exclude_map; print('이전 파일 정상', len(build_access_list()), len(load_last_used()), len(load_exclude_map('config/exclude_list.json')))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `이전 파일 정상 14 7 3`(현황 14건 · 사용 이력 7건 · 회수 제외 3건)이 나와야 합니다.
   - Unit 3 · Unit 3의 파일들이 없으면 이 확인은 건너뛰고, 도전 4-1 문제의 `revoke_input.py` 에서 「Unit 3 · 7 파일이 없을 때용」 코드를 붙여 넣습니다.
   - 파일이 있는데 숫자가 다르면 Unit 3 · Unit 3 의 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」으로 다시 만들고, Unit 1 ~ Unit 1 파일이 없으면 그 레슨의 코드 상자로 만듭니다.
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u4.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.
   - 문자열(string)은 따옴표로 감싼 글입니다. `""` 는 문자가 하나도 없는 빈 문자열입니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **앞서 만든 파일은 고치지 않습니다.** 이번 Unit에서 만드는 파일은 모두 새 파일입니다. 앞 실습 파일이 없으면 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」으로 먼저 만듭니다.

---
