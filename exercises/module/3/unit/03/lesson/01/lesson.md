---
id: m3-u03-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/086_day04_am_access_review.md
  mission_id: GichanSource.m3-1029-am-access-review
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 권한 접근 점검

Unit 2까지는 권한을 **주는** 흐름(요청 → 승인 → 예외 권한 부여 → 기한 점검 → 기록 저장)을 만들었습니다. 이번 Unit에서는 반대로 이미 **부여돼 있는 권한** 가운데 필요 없어진 것을 찾는 **접근 점검**을 만듭니다.

- **실습 3-1**: 지금 누가 어떤 권한을 어떤 방법(역할 · 예외)으로 갖고 있는지 **현황 리스트**를 만든다.
- **도전 3-1**: 현황 리스트에서 **규칙**으로 필요 없어진 권한(퇴사한 사람, 만료된 예외)을 찾는다.
- **실습 3-2**: 규칙으로는 못 찾는 권한을 찾는다.

이번 Unit은 실습 3-1 · 도전 3-1 · 실습 3-2으로 이루어집니다. 실습마다 문제는 하나이고, 그 안에서 단계를 나눠 질문에 답합니다. 깃허브에 올리는 일은 Unit 3의 도전 3-3 마지막에 한 번에 합니다. 이번 Unit에서는 **찾기까지만** 하고, 찾은 권한을 실제로 회수하는 일은 Unit 4에서 합니다.

> **Unit 1 ~ Unit 1의 파일이 없다면**: Unit 1 ~ Unit 1 레슨의 코드 상자(「정답」 레슨 포함)로 아래 파일을 직접 만들면 이번 Unit을 따라올 수 있습니다.
> - 필요한 것: `rbac.py` · `exception_policy.py` · `config_loader.py` · `policy.py` 와 `config` 폴더(`users.json` · `roles.json` · `exceptions.json`).
> - 이번 Unit은 Unit 2와 Unit 2에서 만든 파일을 쓰지 않으므로, 따로 준비할 것이 없습니다.
> - 넣는 방법은 아래 「시작하기」 2번에 있습니다.

**이번 Unit에서 불러 쓰는 이전 파일** — 이번 Unit의 코드가 `import` 로 가져다 쓰는, Unit 1 ~ Unit 1에서 만든 파일입니다. 없으면 오른쪽 열의 방법으로 먼저 준비합니다.

| 파일 | 만든 Unit | 이번 Unit에서 가져다 쓰는 것 | 쓰는 실습 | 없으면 |
|---|---|---|---|---|
| `rbac.py` | Unit 1 | `USERS` · `ROLES` (`config/users.json` · `config/roles.json`) | 실습 3-1 (도전 3-1 · 실습 3-2은 `review_list.py` 를 거쳐 씀) | Unit 1 ~ Unit 1 레슨의 코드 상자 |
| `exception_policy.py` | Unit 1 | `EXCEPTIONS` · `TIME_FORMAT` (`config/exceptions.json`) | 실습 3-1 · 도전 3-1 · 실습 3-2 | Unit 1 ~ Unit 1 레슨의 코드 상자 |
| `config_loader.py` | Unit 1 | `load_json` | 실습 3-2 | Unit 1 ~ Unit 1 레슨의 코드 상자 |

- 이번 Unit에서 만드는 파일도 뒤 실습이 가져다 씁니다. 실습 3-1의 `review_list.py` 는 도전 3-1 · 실습 3-2에서, 도전 3-1의 `review_rules.py` 는 실습 3-2에서 씁니다.

## 터미널 열고 Unit 1~3 파일 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 Unit 1 ~ Unit 1에서 만든 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from rbac import USERS, ROLES; from exception_policy import EXCEPTIONS, TIME_FORMAT; from config_loader import load_json; print('이전 파일 정상', len(USERS), len(ROLES), len(EXCEPTIONS))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `이전 파일 정상 6 5 5`(사용자 6명 · 역할 5개 · 예외 5건)가 나와야 합니다.
   - 아니면 Unit 1 ~ Unit 1 레슨의 코드 상자(「정답」 레슨 포함)로 빠진 파일을 만듭니다(`config` 안의 파일은 `config` 폴더에). 그다음 마지막 줄을 다시 칩니다.
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u3.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **Unit 1 ~ Unit 1에서 만든 파일은 고치지 않습니다.** 이번 Unit에서 만드는 파일은 모두 새 파일입니다. 앞 실습 파일이 없으면 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」으로 먼저 만듭니다.

---
