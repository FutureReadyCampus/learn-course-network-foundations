---
id: m3-u07-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/088_day04_pm_overprivilege.md
  mission_id: GichanSource.m3-1029-pm-overprivilege
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## Unit 7에서 할 일: 리포트 합치기와 회수 제외

Unit 6에서는 부여돼 있는 권한의 **현황 리스트**를 만들고, 거기서 필요 없어진 권한을 **규칙**(퇴사 · 만료)과 **사용 이력**(90일 넘게 안 씀)으로 찾았습니다. 이번 Unit에서는 그 결과들을 한 장의 **과다권한 리포트**로 합치고, 회수하지 않을 권한을 가려냅니다.

- **실습 7-1**: 규칙으로 찾은 것과 사용 이력으로 찾은 것을 합쳐 **리포트**를 만든다(후보마다 이유 리스트).
- **실습 7-2**: 후보 가운데 평소에 안 써도 되는 권한을 **회수 제외 리스트**로 가려내 「회수 대상」과 「회수 제외」로 나눈다. 마지막에 이번 Unit에서 만든 것을 깃허브에 올립니다.

이번 Unit도 **찾기와 기록까지만** 하고, 실제로 회수하는 일은 Unit 8에서 합니다. 실습마다 문제는 하나입니다.

> **Unit 6의 파일이 없다면**: Unit 6 첫 레슨의 안내처럼 Unit 1 ~ Unit 3 레슨의 코드 상자로 그 파일들을 먼저 만들고, Unit 6의 파일은 Unit 6 의 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」으로 만듭니다. 넣는 방법은 아래 「시작하기」 2번에 있습니다.

**이번 Unit에서 불러 쓰는 이전 파일** — 이번 Unit의 코드가 `import` 로 가져다 쓰는, 앞서 만든 파일입니다. 없으면 오른쪽 열의 방법으로 먼저 준비합니다.

| 파일 | 만든 Unit | 이번 Unit에서 가져다 쓰는 것 | 쓰는 실습 | 없으면 |
|---|---|---|---|---|
| `review_list.py` | Unit 6의 실습 6-1 | `build_access_list` | 실습 7-1 · 실습 7-2 | Unit 6 의 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」 |
| `review_rules.py` | Unit 6의 실습 6-2 | `find_stale` | 실습 7-1 · 실습 7-2 | Unit 6 의 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」 |
| `review_unused.py` · `config/access_log.json` | Unit 6의 실습 6-3 | `load_last_used` · `find_unused` (사용 이력) | 실습 7-1 · 실습 7-2 | Unit 6 의 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」 |
| `config_loader.py` | Unit 3 | `load_json` | 실습 7-2 | Unit 1 ~ Unit 3 레슨의 코드 상자 |

- Unit 6의 파일(`review_list.py` 등)이 Unit 1 ~ Unit 3의 `rbac.py` · `exception_policy.py` · `config_loader.py` 를 다시 가져다 쓰므로, 그 파일들도 있어야 합니다.
  - 없으면 Unit 1 ~ Unit 3 레슨의 코드 상자로 만듭니다.
- 이번 Unit에서 만드는 파일도 뒤 실습이 가져다 씁니다. 실습 7-1의 `overprivilege.py` 는 실습 7-2에서 씁니다.

## 폴더 열고 Unit 6 파일 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 Unit 6의 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from review_list import build_access_list; from review_rules import find_stale; from review_unused import load_last_used, find_unused; print('Unit 6 파일 정상', len(build_access_list()), len(load_last_used()))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `Unit 6 파일 정상 14 7`(현황 14건 · 사용 이력 7건)이 나와야 합니다.
   - 아니면 Unit 6 의 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」으로 `review_list.py` · `review_rules.py` · `review_unused.py` 와 `config/access_log.json` 을 만들고, Unit 1 ~ Unit 3 파일이 없으면 그 레슨의 코드 상자로 만듭니다.
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u7.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 **터미널**에서 합니다(VS Code 의 ▶ 단추를 쓰지 않습니다). `python` 이 없다는 오류가 나오면 `python3` 으로 칩니다(맥북은 `python3`). **Unit 6까지 만든 파일은 고치지 않습니다.** 이번 Unit에서 만드는 파일은 모두 새 파일입니다. 앞 실습 파일이 없으면 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」(실습 7-1 · 실습 7-2 파일)과 Unit 6 의 완성본으로 먼저 만듭니다.

---
