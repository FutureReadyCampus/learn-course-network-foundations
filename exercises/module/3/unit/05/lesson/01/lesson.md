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

## 목표와 오늘의 계획

Unit 5는 Module 3 **접근통제 자동화**의 마지막 단계인 **결과 보고하기**입니다. 지금까지 권한을 정하고(Unit 1), 요청서로 주고(Unit 2), 안 쓰는 권한을 점검하고(Unit 3), 계획과 승인을 거쳐 거두었습니다(Unit 4). 이번 Unit에서는 그 결과가 **잘 지켜지고 있는지 매주 같은 기준으로 확인하고, 한 장짜리 주간 보고서로** 남깁니다. 주간 보고서는 일주일 동안 있었던 일을 숫자와 함께 한 장에 정리해, 책임자가 읽고 무엇을 처리할지 정하게 돕는 글입니다. 그리고 Module 3 전체를 상황별로 되짚어 정리합니다.

**오늘의 계획 (약 2시간 40분)**

| 단계 | 시간 | 할 일 |
|---|---|---|
| 시작 | 15분 | 이 레슨을 읽고 데이터 파일 세 개 만들기 |
| 핵심 실습 | 약 110분 | 실습 5-1 → 「제공 파일」로 주간 보고서 → 실습 5-2 |
| 글쓰기 | 20분 | 「오늘의 글 쓰기」에서 세 문장 글 한 편 |
| 마무리 | 15분 | 「Unit 5 마무리」에서 파일 확인, Module 4 준비 |

보고서는 실습 시간 안에서, 실습마다 끝에 나오는 안내에 따라 그때그때 씁니다. 글쓰기 20분은 세 문장 글에만 씁니다. 하루 3시간에서 남는 20분쯤은 밀린 곳을 따라잡는 여유 시간입니다.

**오늘 만들 것 세 가지**

| 레슨 | 만들 것 | 하는 일 |
|---|---|---|
| 실습 5-1 | `checklist.py` 의 빈칸 세 곳(① ~ ③) | 퇴사자 계정 · 만료 예외 · 부서와 역할, 세 가지 점검 |
| 제공 파일 | `log_summary.py` · `weekly_report.py` 복사, `weekly_run.py` 실행 | 점검 결과와 일주일 치 로그를 합쳐 주간 보고서 파일 만들기 |
| 실습 5-2 | **Module 3 총정리** | 새로 배우는 것 없이, Module 3에서 다룬 상황 8개 가운데 3 ~ 8번에서 2개 이상을 골라 원인과 고치는 방법을 내 말로 쓰기 |

**응용 5-1은 여유가 되면 해 보세요.** 핵심 실습 두 개와 글쓰기를 마치고 시간이 남을 때, 제공 파일로 받은 `log_summary.py` 를 빈칸이 있는 골격으로 바꿔 직접 씁니다. 응용을 하지 않아도 주간 보고서는 제공 파일로 만들어지고, Module 4를 따라가는 데도 문제가 없습니다.

**이번 Unit의 파일은 앞 Unit 파일을 불러오지 않습니다.** 필요한 데이터 세 개(점검할 데이터, 경고 기준, 일주일 치 샘플 로그)는 다음 페이지에서 붙여 넣습니다. 그래서 앞 Unit을 다 하지 못했어도 이번 Unit을 따라올 수 있습니다.

- 로그는 서버가 요청을 받을 때마다 「언제 · 누가 · 무엇을 · 허용됐나」를 한 줄씩 적어 두는 기록입니다. 건물 출입 명부와 비슷합니다.
- 샘플 로그 `week_log.jsonl` 은 응용 4-3의 판정 서버가 남기는 `server_log.jsonl` 과 **같은 모양**입니다. 응용 4-3을 하지 않았어도 괜찮습니다.
  - 그 로그는 몇 줄뿐이라 일주일 치로 쓰기에 모자라서, 같은 모양으로 40줄을 만든 샘플을 씁니다.
  - 2026-10-26부터 2026-11-01까지 일주일 동안 서버가 받은 요청이라고 생각하고 읽습니다.
- 깃허브에 올리는 일은 Module 4 첫 Unit의 실습 1-2 마지막에 한 번에 합니다. `access_control` 폴더도 같은 저장소라 그때 함께 올라갑니다.

## 폴더 열고 데이터 파일 만들기

1. **[VS Code]** 왼쪽 목록의 `access_control` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 위치를 확인합니다. 결과가 `…/network-study-notes/access_control` 로 끝나야 합니다.
   ```bash
   pwd
   ls
   ls config
   python --version
   ```
   - 맥북은 `python` 을 `python3` 로 바꿔 칩니다. `config` 폴더가 없어서 `ls config` 가 오류를 내도 괜찮습니다(이번 Unit에서 쓸 json 파일은 5번에서 만듭니다).
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u5.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 코드는 `# ←` 가 있는 번호 빈칸(① · ② …)만 한 줄씩 채우고, 막히면 빈칸마다 있는 힌트를 본 뒤 이 Unit 뒤쪽의 정답 레슨을 봅니다.
5. **[VS Code]** 이번 Unit에서 쓸 데이터 파일 세 개를 만들어 아래 내용을 그대로 붙여 넣습니다. `access_control` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 아래 굵은 글씨의 **파일 이름을 그대로** 적습니다. `config/week_state.json` 처럼 `config/` 가 붙은 이름을 적으면 `config` 폴더 안에 만들어집니다(`config` 폴더가 없으면 함께 만들어집니다).

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

**`config/alert.json`** — 경고 기준입니다. 거부율은 전체 요청 가운데 거부된 요청의 비율입니다. 거부율이 0.3(30%) 이상이면 경고이고, 사용자 한 명이 4번 이상 거부되면 눈여겨봅니다.

<pre class="copyable"><code>{"deny_rate_limit": 0.3, "user_denied_limit": 4}
</code></pre>

**`week_log.jsonl`** — 일주일 치 샘플 로그입니다. 한 줄이 요청 한 개이고 JSON 한 줄입니다. 이름 끝의 `.jsonl` 은 이렇게 한 줄에 JSON 한 건씩 적은 파일이라는 뜻입니다(JSON Lines · 제이슨 라인즈). `access_control` 폴더 바로 아래에 만듭니다.

<pre class="copyable"><code>{"time": "2026-10-26T09:10", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
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
</code></pre>

6. **[터미널]** 세 파일이 정상인지 확인합니다. `pwd` 결과가 `access_control` 로 끝나야 합니다(맥북은 `python3`).
   ```bash
   python -m json.tool config/week_state.json
   python -m json.tool config/alert.json
   python -c "print(len(open('week_log.jsonl', encoding='utf-8').read().splitlines()))"
   ```
   - 앞의 두 명령은 내용이 다시 출력되면 정상입니다(한글이 `\uc601…` 로 보여도 정상).
   - `python -c "…"` 는 따옴표 안의 파이썬 코드를 파일로 만들지 않고 바로 실행합니다. 여기서는 `week_log.jsonl` 의 줄 수를 셉니다. 마지막은 `40` 이 나와야 합니다. 다르면 줄이 빠졌거나 빈 줄이 끼어든 것이니 위 내용과 비교해 다시 셉니다.

**확인** — 앞의 두 명령이 내용을 다시 출력하고 마지막 명령이 `40` 을 내면 성공입니다. 안 나오면 다음 페이지 「오류가 나면」의 표에서 오류 이름을 찾습니다.

## 오류가 나면

먼저 `pwd` 가 `access_control` 로 끝나는지, `ls` 로 파일 이름이 문서와 같은지 봅니다.

| 오류 | 원인 | 확인할 곳 |
|---|---|---|
| `ModuleNotFoundError` · `FileNotFoundError` | 위치나 파일 이름이 틀림 | `pwd` · `ls` 결과 |
| `JSONDecodeError` | 붙여 넣다가 쉼표나 괄호가 빠짐 | `python -m json.tool 파일이름` 으로 어느 줄인지 봄 |
| `IndentationError` · `NameError` | 들여쓰기가 틀렸거나 빠뜨린 줄이 있음 | 직접 쓴 줄 |

`week_log.jsonl` 은 JSON 이 여러 줄이라 `python -m json.tool` 이 늘 오류를 내니, 위 내용과 한 줄씩 비교합니다.

- AI 에게 물을 때는 운영체제와 터미널(예: Windows Git Bash), 친 명령 한 줄, 오류 전체를 함께 붙여 넣습니다. `.env` 내용이나 API 키가 보이면 지우고 붙여 넣습니다.
- AI 가 알려 준 명령은 뜻을 읽고 치고, `rm` · `del` 처럼 지우는 명령은 뜻을 되물은 뒤에 칩니다. 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`). 앞 Unit에서 만든 파일은 고치지 않습니다. 이번 Unit에서 만드는 파일은 모두 새 파일입니다.

---
