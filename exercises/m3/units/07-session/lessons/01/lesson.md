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

## 개요

Unit 6에서는 부여돼 있는 권한의 **현황 리스트**를 만들고, 거기서 필요 없어진 권한을 **규칙**(퇴사 · 만료)과 **사용 이력**(90일 넘게 안 씀)으로 찾았습니다. 이번 Unit에서는 그 결과들을 한 장의 **과다권한 리포트**로 합치고, 회수하지 않을 권한을 가려냅니다.

- **Exercise 7-1**: 규칙으로 찾은 것과 사용 이력으로 찾은 것을 합쳐 **리포트**를 만든다(후보마다 이유 리스트).
- **Exercise 7-2**: 후보 가운데 평소에 안 써도 되는 권한을 **회수 제외 리스트**로 가려내 「회수 대상」과 「회수 제외」로 나눈다. 마지막 10분에 이번 Unit에서 만든 것을 깃허브에 올립니다.

이번 Unit도 **찾기와 기록까지만** 하고, 실제로 회수하는 일은 Unit 8에서 합니다. Exercise마다 문제는 하나입니다.

> **앞 Unit의 파일이 없다면**: Unit 6 문서 맨 위의 안내처럼 수업 자료의 `unit03_recovery` 폴더(Unit 1 ~ Unit 3 파일의 완성본)로 먼저 준비하고, Unit 6의 파일은 Unit 6 문서 맨 아래 「앞 Exercise 파일 완성본」으로 만듭니다. 넣는 방법은 아래 「시작하기」 2번에 있습니다.

**이번 Unit에서 불러 쓰는 이전 파일** — 이번 Unit의 코드가 `import` 로 가져다 쓰는 앞 Unit의 파일입니다. 없으면 오른쪽 열의 방법으로 먼저 준비합니다.

| 파일 | 만든 Unit | 이번 Unit에서 가져다 쓰는 것 | 쓰는 Exercise | 없으면 |
|---|---|---|---|---|
| `review_list.py` | Unit 6의 Exercise 6-1 | `build_access_list` | Exercise 7-1 · Exercise 7-2 | Unit 6 문서 맨 아래 「앞 Exercise 파일 완성본」 |
| `review_rules.py` | Unit 6의 Exercise 6-2 | `find_stale` | Exercise 7-1 · Exercise 7-2 | Unit 6 문서 맨 아래 「앞 Exercise 파일 완성본」 |
| `review_unused.py` · `config/access_log.json` | Unit 6의 Exercise 6-3 | `load_last_used` · `find_unused` (사용 이력) | Exercise 7-1 · Exercise 7-2 | Unit 6 문서 맨 아래 「앞 Exercise 파일 완성본」 |
| `config_loader.py` | Unit 3 | `load_json` | Exercise 7-2 | `unit03_recovery` 폴더 |

- Unit 6의 파일(`review_list.py` 등)이 Unit 1 ~ Unit 3의 `rbac.py` · `exception_policy.py` · `config_loader.py` 를 다시 가져다 쓰므로, 그 파일들도 있어야 합니다.
  - 없으면 `unit03_recovery` 폴더를 씁니다.
- 이번 Unit에서 만드는 파일도 뒤 Exercise가 가져다 씁니다. Exercise 7-1의 `overprivilege.py` 는 Exercise 7-2에서 씁니다.

## 개요

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치와 Unit 6의 파일을 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python -c "from review_list import build_access_list; from review_rules import find_stale; from review_unused import load_last_used, find_unused; print('Unit 6 파일 정상', len(build_access_list()), len(load_last_used()))"
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. 마지막 줄에 `Unit 6 파일 정상 14 7`(현황 14건 · 사용 이력 7건)이 나와야 합니다.
   - 아니면 Unit 6 문서 맨 아래 「앞 Exercise 파일 완성본」으로 `review_list.py` · `review_rules.py` · `review_unused.py` 와 `config/access_log.json` 을 만들고, Unit 1 ~ Unit 3 파일이 없으면 `unit03_recovery` 폴더에서 넣습니다.
3. **이번 Unit에서 받은 파일 두 개를 `access_control` 폴더에 둡니다.** 이미 있으면 건너뜁니다. `다운로드` 폴더에서 VS Code 왼쪽의 그 폴더 위로 끌어다 놓습니다(안 되면 파일을 열어 **File › Save As…** 로 저장).
   - Unit 7 (이 파일) — 실습 안내. 읽기만 합니다.
   - Unit 7 — **보고서.** Exercise 7-1 · Exercise 7-2 답과 마무리 칸을 여기에 적습니다.
4. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. 보고서 Unit 7 는 오른쪽 클릭 › **Open to the Side** 로 옆에 열고, 맨 위 제목 `(이름 · Unit 7)` 의 `이름` 만 내 이름으로 바꿉니다.
5. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.

> 실행은 **터미널**에서 합니다(VS Code 의 ▶ 단추를 쓰지 않습니다). `python` 이 없다는 오류가 나오면 `python3` 으로 칩니다(맥북은 `python3`). **Unit 6까지 만든 파일은 고치지 않습니다.** 이번 Unit에서 만드는 파일은 모두 새 파일입니다. 앞 Exercise 파일이 없으면 문서 맨 아래 「앞 Exercise 파일 완성본」(Exercise 7-1 · Exercise 7-2 파일)과 Unit 6 문서의 완성본으로 먼저 만듭니다.

---
