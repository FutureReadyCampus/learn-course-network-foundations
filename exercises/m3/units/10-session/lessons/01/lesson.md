---
id: m3-u10-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/094_day06_am_weekly_report.md
  mission_id: GichanSource.m3-1102-am-weekly-report
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 개요

지난 금요일(10/30(금))까지 권한을 점검하고, 회수하고, 요청마다 조건을 확인하는 서버를 만들었습니다. 오늘 오전에는 그 결과가 **잘 지켜지고 있는지 매주 같은 기준으로 확인하고 한 장으로 보고**합니다. 3과목의 마지막 수업입니다.

- **Exercise 10-1**: 퇴사자 · 만료 예외 · 부서와 역할, 세 가지를 **점검 체크리스트**로 점검해 통과와 실패를 가린다.
- **Exercise 10-2**: 서버가 남기는 **요청 로그**를 집계해 허용과 거부, 거부율, 거부 사유를 구하고 **경고 기준**과 비교한 뒤, Exercise 10-1 점검 결과와 합친 **주간 보고서** 파일을 만듭니다.
- **Exercise 10-3**: **3과목 총정리.** 새로 배우는 것 없이, 상황 8개마다 원인과 고치는 방법을 내 말로 정리합니다.

오늘은 오전 2 · 3 · Exercise 10-3이고, 오후부터는 4과목(이상탐지)을 시작합니다. 깃허브에 올리는 일은 오후 Exercise 9-2 마지막에 한 번에 합니다. Exercise마다 문제는 하나입니다.

오늘 파일은 앞 수업 파일을 불러오지 않습니다. 필요한 데이터 세 개(점검할 데이터 · 경고 기준 · 일주일 치 샘플 로그)는 아래 「시작하기」에서 붙여 넣습니다. 그래서 앞 날에 결석했어도 오늘 수업을 따라올 수 있습니다.

- 샘플 로그(`week_log.jsonl`)는 금요일 서버가 남긴 `server_log.jsonl` 과 **같은 모양**입니다.
  - 금요일 로그는 8줄뿐이라 일주일 치로 쓰기에 모자라서, 같은 모양으로 40줄을 만든 샘플을 씁니다.
  - 10/26(월)부터 11/1(일)까지 서버가 받은 요청이라고 생각하고 읽습니다.

## 개요

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치를 확인합니다. 결과가 `…/security-agent-toolkit/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python --version
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. `config` 폴더가 없어서 `ls config` 가 오류를 내도 괜찮습니다(오늘 쓸 json 파일은 6번에서 만듭니다).
3. **오늘 받은 파일 두 개를 `access_control` 폴더에 둡니다.** 이미 있으면 건너뜁니다. `다운로드` 폴더에서 VS Code 왼쪽의 그 폴더 위로 끌어다 놓습니다(안 되면 파일을 열어 **File › Save As…** 로 저장).
   - Unit 10 (이 파일) — 오전 실습 안내. 읽기만 합니다.
   - Unit 10 — **오전 보고서.** 2 · 3 · Exercise 10-3 답을 여기에 적습니다.
4. **[VS Code]** 안내 파일을 열고 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다. 보고서 Unit 10 는 오른쪽 클릭 › **Open to the Side** 로 옆에 열고, 맨 위 제목 `(이름 · 2026-11-02(월))` 의 `이름` 만 내 이름으로 바꿉니다.
5. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드를 채울 때는 주석이 말하는 일을 하면 몇 줄이든 맞고, 막히면 맨 아래 「정답」을 봅니다.
6. **[VS Code 또는 터미널]** 오늘 쓸 데이터 파일 세 개를 만들어 아래 내용을 그대로 붙여 넣습니다. VS Code 에서는 `access_control` 폴더를 선택해 **새 파일**(New File)을 누르고(`config/…` 이름은 `config` 폴더 안에 만들어집니다. 이미 `config` 폴더가 있으면 그 안에 만듭니다), 터미널에서는 `config` 폴더가 없으면 `mkdir config` 후 `touch 이름` 으로 만들어 VS Code 에서 열어 붙여 넣습니다.

**`config/week_state.json`** — 점검할 데이터입니다. 사용자 여섯 명 · 역할별 부서 · 예외 네 개가 들어 있습니다.

```json
{
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
```

**`config/alert.json`** — 경고 기준입니다. 거부율이 0.3(30%) 이상이면 경고이고, 사용자 한 명이 4번 이상 거부되면 눈여겨봅니다.

```json
{"deny_rate_limit": 0.3, "user_denied_limit": 4}
```

**`week_log.jsonl`** — 일주일 치 샘플 로그입니다. 한 줄이 요청 한 개이고 JSON 한 줄입니다. `access_control` 폴더 바로 아래에 만듭니다.

```
{"time": "2026-10-26T09:10", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-26T09:40", "user": "seoyeon", "permission": "SALES:CHANGE", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-26T10:05", "user": "junho", "permission": "SETTLE:QUERY", "network": "vpn", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-26T10:30", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-26T14:20", "user": "tester", "permission": "SALES:QUERY", "network": "office", "allowed": false, "reason": "역할이 없음"}
{"time": "2026-10-26T23:10", "user": "seoyeon", "permission": "SALES:CHANGE", "network": "external", "allowed": false, "reason": "업무 시간 밖"}
{"time": "2026-10-27T09:05", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-27T10:15", "user": "junho", "permission": "SETTLE:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-27T11:00", "user": "dami", "permission": "SALES:QUERY", "network": "office", "allowed": false, "reason": "퇴사한 계정"}
{"time": "2026-10-27T13:45", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "vpn", "allowed": false, "reason": "허용되지 않은 접속 위치"}
{"time": "2026-10-27T15:30", "user": "batch-night", "permission": "SETTLE:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-27T22:40", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "external", "allowed": false, "reason": "업무 시간 밖"}
{"time": "2026-10-28T09:20", "user": "seoyeon", "permission": "SALES:CHANGE", "network": "vpn", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-28T10:00", "user": "junho", "permission": "SETTLE:QUERY", "network": "vpn", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-28T10:50", "user": "dami", "permission": "SALES:QUERY", "network": "vpn", "allowed": false, "reason": "퇴사한 계정"}
{"time": "2026-10-28T14:10", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-28T16:25", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-28T20:30", "user": "junho", "permission": "SETTLE:QUERY", "network": "vpn", "allowed": false, "reason": "업무 시간 밖"}
{"time": "2026-10-29T09:00", "user": "seoyeon", "permission": "SALES:CHANGE", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-29T09:35", "user": "junho", "permission": "SETTLE:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-29T10:20", "user": "dami", "permission": "SALES:QUERY", "network": "external", "allowed": false, "reason": "퇴사한 계정"}
{"time": "2026-10-29T11:10", "user": "tester", "permission": "SETTLE:QUERY", "network": "office", "allowed": false, "reason": "역할이 없음"}
{"time": "2026-10-29T13:00", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "vpn", "allowed": false, "reason": "허용되지 않은 접속 위치"}
{"time": "2026-10-29T15:45", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-29T18:00", "user": "seoyeon", "permission": "SALES:CHANGE", "network": "office", "allowed": false, "reason": "업무 시간 밖"}
{"time": "2026-10-30T09:15", "user": "junho", "permission": "SETTLE:QUERY", "network": "vpn", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-30T10:00", "user": "seoyeon", "permission": "SALES:CHANGE", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-30T10:30", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "external", "allowed": false, "reason": "허용되지 않은 접속 위치"}
{"time": "2026-10-30T11:20", "user": "batch-night", "permission": "SETTLE:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-30T14:00", "user": "dami", "permission": "SALES:QUERY", "network": "office", "allowed": false, "reason": "퇴사한 계정"}
{"time": "2026-10-30T19:30", "user": "junho", "permission": "SETTLE:QUERY", "network": "vpn", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-31T09:10", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-31T09:50", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-31T10:40", "user": "junho", "permission": "SETTLE:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-31T13:15", "user": "tester", "permission": "SALES:QUERY", "network": "office", "allowed": false, "reason": "역할이 없음"}
{"time": "2026-10-31T15:00", "user": "seoyeon", "permission": "SALES:CHANGE", "network": "external", "allowed": false, "reason": "허용되지 않은 접속 위치"}
{"time": "2026-10-31T17:20", "user": "batch-night", "permission": "SETTLE:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-10-31T19:50", "user": "junho", "permission": "SETTLE:QUERY", "network": "vpn", "allowed": true, "reason": "역할 권한"}
{"time": "2026-11-01T09:30", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-11-01T10:10", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "vpn", "allowed": false, "reason": "허용되지 않은 접속 위치"}
```

7. **[터미널]** 세 파일이 정상인지 확인합니다. `pwd` 결과가 `access_control` 로 끝나야 합니다(맥북은 `python3`).
   ```bash
   python -m json.tool config/week_state.json
   python -m json.tool config/alert.json
   python -c "print(len(open('week_log.jsonl', encoding='utf-8').read().splitlines()))"
   ```
   - 앞의 두 명령은 내용이 다시 출력되면 정상입니다(한글이 `\uc601…` 로 보여도 정상). 마지막은 `40` 이 나와야 합니다. 다르면 줄이 빠졌거나 빈 줄이 끼어든 것이니 위 내용과 비교해 다시 셉니다.

## 오류가 나면

- 먼저 `pwd` 가 `access_control` 로 끝나는지, `ls` 로 파일 이름이 문서와 같은지 봅니다.
  - `ModuleNotFoundError` · `FileNotFoundError`: 위치나 파일 이름이 틀렸습니다.
  - `JSONDecodeError`: 붙여 넣다가 쉼표나 괄호가 빠졌습니다. `python -m json.tool 파일이름` 으로 어느 줄인지 봅니다.
  - `IndentationError` · `NameError`: 직접 쓴 줄의 들여쓰기가 틀렸거나 빠뜨린 줄이 있습니다.
- AI 에게 물을 때는 운영체제와 터미널(예: Windows Git Bash), 친 명령 한 줄, 오류 전체를 함께 붙여 넣습니다. `.env` 내용이나 API 키가 보이면 지우고 붙여 넣습니다.
- AI 가 알려 준 명령은 뜻을 읽고 치고, `rm` · `del` 처럼 지우는 명령은 뜻을 되물은 뒤에 칩니다. 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). **앞 수업의 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다. 앞 Exercise 파일이 없으면 문서 맨 아래 「앞 Exercise 파일 완성본」으로 먼저 만듭니다.

---
