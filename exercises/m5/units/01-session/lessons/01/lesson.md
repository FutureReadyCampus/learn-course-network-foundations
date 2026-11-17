---
id: m5-u01-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/116_day01_pm_playbook_incident.md
  mission_id: GichanSource.m5-1109-pm-playbook-incident
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 개요

오전에 4과목을 마쳤습니다. 4과목에서는 로그를 읽어 **위험한 대상을 찾아 점수와 등급을 매겼습니다.** 오늘 오후부터 시작하는 5과목은 그 **알림이 난 뒤에 하는 일**을 다룹니다. 계정을 잠그고, **티켓**(ticket, 티켓: 처리할 일 한 건을 적어 두고 누가 맡았는지와 처리됐는지를 추적하는 기록)을 만들고, 담당자에게 알리는 일을 정해 둔 절차대로 프로그램이 실행하게 만드는 과목입니다.

오늘은 <mark>**연습용 시스템**(실제 서버와 계정 대신 파일로 흉내 낸 시스템)에서 대응이 실제로 일어나는 것</mark>을 봅니다. 실제 서버와 계정은 건드리지 않습니다.

- **Exercise 1-1**: SOAR 가 무엇인지 읽고, **플레이북**(playbook, 플레이북: 「이런 알림이 오면 이렇게 대응한다」를 미리 적어 둔 대응 절차서) 한 건을 직접 씁니다. 그리고 알림 두 건을 **수동 처리**(수동: 프로그램 없이 사람이 직접 하는 처리입니다. 여기서는 VS Code 로 `system_state.json` 을 열어 값을 직접 타이핑해 넣고 저장하는 처리)해 보면서 얼마나 번거로운지 겪습니다.
- **Exercise 1-2**: 같은 일을 프로그램(`playbook_runner.py`)이 하게 만듭니다. <mark>한 번 실행하면 알림 5건이 처리되고, 사람의 승인이 필요한 건은 멈추고, 무엇을 했는지 기록이 남습니다.</mark>

오늘은 오후 5 · Exercise 1-2이고, <mark>깃허브에 올리는 일은 Exercise 1-2 마지막에 합니다.</mark> Exercise마다 문제는 하나입니다.

- 오늘 쓰는 도구는 **파이썬 · VS Code · 터미널 · git** 입니다. 판다스와 Gemini API 는 쓰지 않으므로 호출 한도(1분에 15번)는 신경 쓰지 않아도 됩니다.
- 오늘 새로 배우는 문법은 없습니다. 이번 주에 쓴 문법(딕셔너리 · 리스트 · `in` · `not in` · `if` · `for` · `append` · `json`)을 다시 씁니다.
- 새로 나오는 용어가 많은 날입니다. <mark>처음 나올 때 한 번씩 풀어 쓰고, 문제를 풀 때는 1.2 와 2.1 의 표를 보면서 풉니다.</mark>
- 보고서에서 [핵심 질문] 가 붙은 질문은 이 Exercise에서 꼭 알아야 할 핵심 질문이고, <mark>내 출력이나 샘플 데이터의 값을 근거로 이유까지 서술합니다</mark>.

 **오늘 불러 쓰는 이전 파일**: 없습니다. 오늘 쓰는 데이터(`incident_samples.json`)는 오전 4과목의 점수 파일과 같은 내용을 오늘 수업용 예시 데이터로 아래 시작하기에 적어 두었고, 그것을 붙여 넣어 만듭니다. 그래서 오전 파일이 없어도 그대로 따라 할 수 있습니다. Exercise 1-2는 Exercise 1-1에서 만드는 `config/playbook_registry.json` 을 읽습니다(없으면 `complete_files.md` 의 1절이나 Exercise 1-1 의 「Exercise 1-1 정답」 완성본으로 만듭니다).

## 개요

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 지금 위치를 확인합니다. <mark>`pwd` 결과가 `…/security-agent-toolkit` 으로 끝나고, `ls` 결과에 `anomaly_detection` 폴더가 보이면</mark> 됩니다. 결과가 다르면 `security-agent-toolkit` 폴더에서 터미널을 새로 엽니다.
   ```bash
   pwd
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
3. **[터미널]** 5과목 폴더를 만들고 그 안으로 들어갑니다. 5과목의 모든 파일은 <mark>`soar_response` 폴더 안</mark>에 둡니다. 폴더 이름은 강의계획서가 정한 이름 그대로입니다.
   ```bash
   mkdir soar_response
   cd soar_response
   mkdir config
   ls
   ```
   - 명령 풀이: `mkdir 폴더이름` 새 폴더 만들기 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 이름 보기
   - <mark>`config` 폴더가 보이면</mark> 됩니다. `config` 에는 JSON 설정 파일만 둡니다.
4. **오늘 받은 파일 두 개**(`day01_pm_playbook_incident.md`, `day01_pm_report.md`)를 <mark>`다운로드` 폴더에서 `soar_response` 폴더로 끌어다 놓습니다</mark>(안 되면 **File › Save As…**). 그리고 **[VS Code]** 보고서 맨 위 제목 `(이름 · 2026-11-09(월))` 의 <mark>`이름` 을 내 이름으로 바꿉니다</mark>. 안내 파일은 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다.
5. **[터미널]** 오늘 쓸 파일 두 개를 만들고 **[VS Code]** 에서 열어 아래 내용을 그대로 붙여 넣습니다.
   ```bash
   touch incident_samples.json system_state.json
   ls
   ```
   - 명령 풀이: `touch 파일이름들` 빈 파일 만들기 · `ls` 폴더 안의 이름 보기

**`incident_samples.json`** — 오늘 처리할 알림 5건의 목록입니다.

- **무엇인가**:
  - 오전 4과목에서 저장한 대상별 점수 기록 5건에 인시던트 번호(`id`)와 처음 상태(`status`)를 붙인 것입니다.
  - **인시던트**(incident, 인시던트): 알림 가운데 사람이 확인하고 대응해야 하는 일 한 건입니다. 예를 들어 「퇴사한 `dami` 의 계정으로 서버에 요청이 왔다」는 알림에 `INC-001` 이라는 번호를 붙이면 인시던트 한 건이 되고, 대응이 끝날 때까지 이 번호로 추적합니다. 알림과 어떻게 다른지는 Exercise 1-1 읽을거리의 「인시던트는 무엇인가」에서 자세히 설명합니다.
  - `entity` 는 점수를 매긴 대상(사용자 또는 IP), `grade` 는 등급, `reasons` 는 탐지된 규칙 이름입니다. <mark>처음 상태는 모두 `탐지됨` 입니다.</mark>
- **어디에 쓰나**:
  - Exercise 1-1: 어떤 알림을 처리할지 볼 때 읽습니다.
  - Exercise 1-2: 실행기(`playbook_runner.py`)가 이 파일을 읽어 알림을 하나씩 처리합니다.

```
[
  {
    "id": "INC-001",
    "entity": "dami",
    "grade": "high",
    "score": 60,
    "reasons": [
      "퇴사한 계정"
    ],
    "status": "탐지됨"
  },
  {
    "id": "INC-002",
    "entity": "seoyeon",
    "grade": "mid",
    "score": 45,
    "reasons": [
      "평소와 다른 IP",
      "대량 다운로드"
    ],
    "status": "탐지됨"
  },
  {
    "id": "INC-003",
    "entity": "gaeun",
    "grade": "mid",
    "score": 40,
    "reasons": [
      "규칙은 허용인데 서버가 거절",
      "여러 로그 연결"
    ],
    "status": "탐지됨"
  },
  {
    "id": "INC-004",
    "entity": "jiwoo",
    "grade": "mid",
    "score": 35,
    "reasons": [
      "업무 시간 밖 로그인",
      "평소와 다른 IP"
    ],
    "status": "탐지됨"
  },
  {
    "id": "INC-005",
    "entity": "198.51.100.90",
    "grade": "low",
    "score": 30,
    "reasons": [
      "경로 스캔"
    ],
    "status": "탐지됨"
  }
]
```

**`system_state.json`** — 연습용 시스템의 상태를 적는 파일입니다.

- **무엇인가**:
  - 대응을 하면 바뀌는 것 네 가지를 적습니다. 잠긴 계정(`locked_users`) · 차단한 IP(`blocked_ips`) · 티켓(`tickets`) · 담당자 알림(`notifications`)입니다.
  - 처음에는 모두 비어 있습니다.
- **어디에 쓰나**:
  - Exercise 1-1: 알림 두 건을 수동 처리하면서 VS Code 로 이 파일을 열어 값을 직접 입력하고 저장합니다.
  - Exercise 1-2: 실행기가 대응 결과를 이 파일에 새로 저장합니다. 실행하면 직접 입력한 내용은 덮어씁니다.

```
{
  "locked_users": [],
  "blocked_ips": [],
  "tickets": [],
  "notifications": []
}
```

6. **[터미널]** 파일이 정상인지 확인합니다. <mark>`5` 가 나와야</mark> 합니다. 다르면 붙여 넣은 내용이나 파일 위치(`soar_response` 폴더 안인지)를 다시 확인합니다(맥북은 `python3`).
   ```bash
   python -c "import json; print(len(json.load(open('incident_samples.json', encoding='utf-8'))))"
   ```

## 오류가 나면

- 먼저 `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `FileNotFoundError` 가 나오면 <mark>파일이 `soar_response` 폴더 바로 아래(또는 `config` 폴더 안)에 있는지</mark> `ls` 로 봅니다. `config/playbook_registry.json` 은 `config` 폴더 안에 있어야 합니다.
- `json.decoder.JSONDecodeError` 가 나오면 <mark>JSON 파일의 쉼표나 대괄호 · 중괄호가 빠졌거나 남은 것</mark>입니다. 오류에 적힌 줄 번호의 앞뒤 줄을 봅니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 맨 아래 「정답」을 보고</mark>, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

---
