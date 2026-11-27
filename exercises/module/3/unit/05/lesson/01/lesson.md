---
id: m3-u05-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/094_day06_am_weekly_report.md
  mission_id: GichanSource.m3-1102-am-weekly-report
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## Unit 5에서 할 일: 점검, 집계, 총정리

M3 Unit 4까지 권한을 점검하고, 회수하고, 요청마다 조건을 확인하는 서버를 만들었습니다. 이번 Unit에서는 그 결과가 **잘 지켜지고 있는지 매주 같은 기준으로 확인하고 한 장으로 보고**합니다. Module 3의 마지막 Unit입니다.

- **실습 5-1**: 퇴사자, 만료된 예외, 부서와 역할이 맞는지, 세 가지를 **점검 체크리스트**로 살펴 통과와 실패를 가립니다.
- **응용 5-1**: 서버가 남기는 **요청 로그**를 모아 허용과 거부 건수, 거부율, 거부 사유를 구하고 **경고 기준**과 비교합니다. 그다음 실습 5-1 점검 결과와 합쳐 **주간 보고서** 파일을 만듭니다.
- **실습 5-2**: **Module 3 총정리.** 새로 배우는 것 없이, 상황 8개마다 원인과 고치는 방법을 내 말로 정리합니다.

핵심 실습은 실습 5-1과 실습 5-2입니다. 응용 5-1은 선택 과제입니다. 핵심 실습을 마친 뒤, Module 3에서 실제로 고민하고 확인한 과정을 GitHub 블로그 글로 남깁니다. 다음 Unit부터는 Module 4(이상탐지)를 시작합니다.

이번 Unit의 핵심 실습은 이전 Unit의 파일을 불러오지 않습니다. 점검할 데이터, 경고 기준, 일주일 치 샘플 로그를 아래에서 새 파일로 만듭니다. 이전 Unit을 건너뛰었어도 진행할 수 있습니다.

- 샘플 로그(`week_log.jsonl`)는 M3 Unit 4에서 서버가 남긴 `server_log.jsonl` 과 **같은 모양**입니다.
  - M3 Unit 4의 로그는 8줄뿐이라 일주일 치로 쓰기에 모자라서, 같은 모양으로 40줄을 만든 샘플을 씁니다.
  - 2026-10-26부터 2026-11-01까지 일주일 동안 서버가 받은 요청이라고 생각하고 읽습니다.

## 폴더 열고 Module 3 파일 확인하기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치를 확인합니다. 결과가 `…/network-study-notes/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python --version
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. `config` 폴더가 없어서 `ls config` 가 오류를 내도 괜찮습니다(5번에서 `config` 폴더와 JSON을 만듭니다).
3. **파일은 이렇게 만듭니다.** 파일 이름이 안내되면 VS Code에서 새 파일을 만들고, 아래 코드 상자 내용을 붙여 넣습니다:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 두 핵심 실습을 마치면 [실습 결과와 문제 해결 과정을 기록하기](__SITE__/exercises/module/3/unit/5/lesson/7/page/1)에서 근거와 판단을 블로그 글로 남깁니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 각 실습 바로 뒤의 「정답과 해설 보기」를 엽니다.
5. **[VS Code]** `access_control/config`에 `week_state.json`을 만들고 아래 내용을 붙여 넣습니다. `config` 폴더가 없으면 먼저 만듭니다.

**`config/week_state.json`** — 점검할 데이터입니다. 사용자 여섯 명 · 역할별 부서 · 예외 네 개가 들어 있습니다.

<pre class="copyable"><code>{
  "users": {
    "seoyeon": {"dept": "영업", "role": "sales", "employed": true},
    "junho": {"dept": "영업", "role": "finance", "employed": true},
    "gaeun": {"dept": "IT", "role": "account_admin", "employed": true},
    "dami": {"dept": "영업", "role": "sales", "employed": false},
    "batch-night": {"dept": "시스템", "role": "batch", "employed": true},
    "tester": {"dept": "인턴", "role": "intern", "employed": true}
  },
  "role_dept": {
    "sales": "영업",
    "finance": "재무",
    "account_admin": "IT",
    "batch": "시스템",
    "intern": "인턴"
  },
  "exceptions": [
    {"id": 3, "user": "dami", "permission": "SALES:QUERY", "expires": "2026-11-03 18:00"},
    {"id": 6, "user": "seoyeon", "permission": "SETTLE:QUERY", "expires": "2026-11-06 18:00"},
    {"id": 7, "user": "tester", "permission": "SALES:QUERY", "expires": "2026-11-04 09:00"},
    {"id": 8, "user": "gaeun", "permission": "SETTLE:QUERY", "expires": "2026-11-13 12:00"}
  ]
}
</code></pre>

6. **[터미널]** `python -m json.tool config/week_state.json`으로 점검 데이터의 형식을 확인합니다. macOS에서는 `python3`를 씁니다. 내용이 다시 출력되면 정상입니다.

## 오류가 나면

- 먼저 `pwd` 가 `access_control` 로 끝나는지, `ls` 로 파일 이름이 문서와 같은지 봅니다.
  - `ModuleNotFoundError` · `FileNotFoundError`: 위치나 파일 이름이 틀렸습니다.
  - `JSONDecodeError`: 붙여 넣다가 쉼표나 괄호가 빠졌습니다. `python -m json.tool 파일이름` 으로 어느 줄인지 봅니다.
  - `IndentationError` · `NameError`: 직접 쓴 줄의 들여쓰기가 틀렸거나 빠뜨린 줄이 있습니다.
- AI 에게 물을 때는 운영체제와 터미널(예: Windows Git Bash), 친 명령 한 줄, 오류 전체를 함께 붙여 넣습니다. `.env` 내용이나 API 키가 보이면 지우고 붙여 넣습니다.
- AI 가 알려 준 명령은 뜻을 읽고 치고, `rm` · `del` 처럼 지우는 명령은 뜻을 되물은 뒤에 칩니다. 풀리지 않으면 어디까지 해 봤는지와 다음에 확인할 내용을 블로그 글의 초안에 메모합니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **M3 Unit 4까지 만든 파일은 고치지 않습니다.** 핵심 실습에 필요한 데이터는 이 페이지에서 만들고, 코드는 실습에서 작성합니다.

---
