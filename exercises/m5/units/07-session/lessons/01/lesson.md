---
id: m5-u07-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/128_day04_pm_escalation_metrics.md
  mission_id: GichanSource.m5-1112-pm-escalation-metrics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## Unit 7에서 만들 것: 에스컬레이션과 운영 지표

Unit 6에서는 세 가지를 했습니다. 알림으로 티켓(ticket, 티켓: 처리할 일 한 건을 적어 두는 기록)을 만들었습니다. 같은 사건의 알림은 티켓 한 장으로 병합(merge: 하나로 합치기)했습니다. 그리고 담당자에게 알림을 보냈습니다(통지, notification).

이번 Unit에서는 두 가지를 만듭니다. 하나는 **에스컬레이션**(escalation, 에스컬레이션: 처리되지 않는 일을 더 높은 책임자에게 넘기는 절차)입니다. <mark>담당자가 응답 기한 안에 응답하지 않으면 상급자에게 알리는 기능</mark>입니다. 다른 하나는 **운영 지표**(operational metrics, 오퍼레이셔널 메트릭스: 팀의 대응 속도를 숫자로 나타낸 값)입니다. 근무가 끝날 때 팀의 대응 속도를 보고하려고 이 값을 계산합니다.

두 기능은 보안 관제(SOC, Security Operations Center, 소크: 보안 사건을 감시하고 대응하는 조직)가 근무 중에 하는 일입니다.

- **Exercise 7-1**: **응답 기한**(SLA, Service Level Agreement, 에스엘에이: 티켓이 생성된 뒤 담당자가 확인해야 하는 제한 시간. 원래는 「서비스 수준 협약」의 줄임말)이 지났는데도 확인(acknowledge)되지 않은 티켓을 상급자에게 에스컬레이션합니다(`escalation.py`). 예를 들어 <mark style="background:#ffdcb0">`TCK-1` 은 응답 기한이 15분이므로 15분 안에 확인되어야 합니다</mark>. 20분이 되도록 아무도 확인하지 않았다면 5분을 초과한 것입니다.
- **Exercise 7-2**: Unit 6부터 만든 기능을 근무 3시간 시뮬레이션(simulation, 시뮬레이션: 실제 근무 대신 연습용 알림 · 동작 기록으로 근무 시간을 재현하는 방식)으로 연속 실행합니다. 그 결과로 <mark>평균 확인 시간(MTTA) · 평균 해결 시간(MTTR) · 응답 기한 위반(SLA breach) 수를 계산합니다</mark>. 마지막으로 다음 근무자에게 인계(handoff)할 미해결 티켓 목록을 작성합니다(`shift_metrics.py`).

깃허브에 올리는 일은 Exercise 7-2 마지막에 합니다. 새 문법은 Exercise 7-2의 `sum()` 과 `%` 둘이고, 나눗셈 `/` 는 문법 상자에서 풀이합니다. 보고서의 [핵심 질문] 표시가 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 들여쓰기는 미리 채운 줄에 맞춥니다. 각 번호 주석 바로 아래에 한 줄을 씁니다. <mark style="background:#ffc4d6">주석은 지우지 않습니다</mark>.

 **이전 파일**: Unit 6에서 만든 `ticketing.py` · `ticket_merge.py` · `ticket_notice.py` 와 데이터 `alerts_thu.json` · `config/escalation_rules.json`, <mark style="background:#e0d4ff">Unit 1의 `incident.py`</mark>, <mark style="background:#e0d4ff">`notifier.py` · `alert_server.py`</mark> 를 씁니다. Exercise 7-1에서는 Unit 6의 Exercise 6-3에서 저장한 `tickets_unit09.json` 도 읽습니다. Exercise 7-2에서는 Exercise 7-1에서 만든 `escalation.py` 도 씁니다. 없는 파일은 `complete_files.md` 에서 복사합니다(Unit 6 파일은 6절, `escalation.py` 는 7절). `incident.py` · `notifier.py` · `alert_server.py` 는 Unit 6 안내의 시작하기에 있는 「 이전 파일이 없을 때」 코드 상자로 만듭니다.

 **줄임말 이름 안내**: 이 문서의 코드와 파일에는 줄임말로 된 이름이 있습니다. 처음 보면 뜻을 알기 어려워서 아래에 풀어 둡니다. 이미 배포한 파일과 맞추기 위해 이름은 그대로 쓰고 뜻만 설명합니다.
  - `ack` · `acked` 는 acknowledge(확인하다) · acknowledged(확인했다)의 줄임말입니다. 담당자가 티켓을 처음 확인했다는 뜻입니다.
  - `acked_at` 은 처음 확인한 시각(분), `ack_times` 는 확인까지 걸린 분 리스트, `mean_ack_minutes` 는 그 평균(평균 확인 시간)입니다.
  - `sla` 는 서비스 수준 협약(SLA, Service Level Agreement)의 줄임말입니다. 이 문서에서는 응답 기한을 뜻합니다.
  - `sla_due` 는 응답해야 하는 시각이고, `count_sla_breaches` 는 응답 기한을 넘긴 티켓 수를 세는 함수입니다.

## 폴더 열고 파일 준비하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `soar_response` 폴더로 들어가 파일을 확인합니다. <mark style="background:#bde3ff">`ls` 결과에 `ticketing.py` · `ticket_merge.py` · `ticket_notice.py` · `tickets_unit09.json` 이 보이면</mark> 됩니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다. `cd` 가 안 되면 `ls` 로 `soar_response` 폴더가 보이는지 확인합니다.
   - `tickets_unit09.json` 이 없으면 먼저 아래 6번(알림 서버 켜기)을 합니다. 그다음 이 터미널에서 Unit 6의 Exercise 6-3 실행 파일(`exercise6-3_run.py`)을 한 번 실행하면 `tickets_unit09.json` 이 생깁니다. 실행 파일이 없으면 Unit 6의 Exercise 6-3 안내 문서의 `exercise6-3_run.py` 코드로 파일을 만들어 실행합니다. `ticketing.py` 같은 Unit 6 코드 파일은 `complete_files.md` 6절에서 복사합니다. 이 경우 서버 터미널에 Unit 6의 Exercise 6-3의 `[알림 받음]` 9줄이 먼저 나오므로, Exercise 7-1의 4줄은 그 아래부터 셉니다.
3. Unit 7에서 받은 파일 두 개(Unit 7 안내 문서, Unit 7 보고서)를 `soar_response` 폴더로 옮기고, 보고서 제목의 `이름` 을 내 이름으로 바꿉니다.
4. **[터미널]** 담당자 동작 파일을 만들고 **[VS Code]** 에서 열어 아래 내용을 붙여 넣습니다.
   ```bash
   touch status_events.json
   ls
   ```

**`status_events.json`** — Exercise 7-2 근무 시뮬레이션 3시간 동안 담당자가 티켓 상태를 변경한 기록입니다.

- **구성**: 담당자 동작 한 건은 `minute`(변경 시각, 분), `ticket`(티켓 번호), `status`(변경 후 상태), `who`(변경한 담당자)로 이루어집니다.
- **용도**: Exercise 7-2 실행 파일이 이 기록에 따라 티켓 상태를 변경합니다. Exercise 7-1에서는 사용하지 않습니다.

```
[
  {"minute": 10, "ticket": "TCK-1", "status": "확인 중", "who": "kim.sec"},
  {"minute": 45, "ticket": "TCK-1", "status": "해결", "who": "kim.sec"},
  {"minute": 80, "ticket": "TCK-3", "status": "확인 중", "who": "lee.soc"},
  {"minute": 90, "ticket": "TCK-6", "status": "확인 중", "who": "kim.sec"},
  {"minute": 105, "ticket": "TCK-7", "status": "확인 중", "who": "kim.sec"},
  {"minute": 120, "ticket": "TCK-3", "status": "해결", "who": "lee.soc"},
  {"minute": 130, "ticket": "TCK-6", "status": "해결", "who": "kim.sec"},
  {"minute": 140, "ticket": "TCK-4", "status": "확인 중", "who": "lee.soc"}
]
```

5. **[터미널]** 파일이 정상인지 확인합니다(맥북은 `python3`). <mark style="background:#bde3ff">`7 8` 이 나와야</mark> 합니다.
   ```bash
   python -c "import json; print(len(json.load(open('tickets_unit09.json', encoding='utf-8'))), len(json.load(open('status_events.json', encoding='utf-8'))))"
   ```
6. **[터미널]** 알림 서버를 시작합니다. VS Code 터미널 창 오른쪽 위의 `+` 로 **새 터미널**을 하나 더 열고 서버를 실행합니다(맥북은 `python3`). <mark style="background:#bde3ff">`Running on http://127.0.0.1:5001` 이 보이면</mark> 됩니다. 이 터미널은 이번 Unit 내내 그대로 둡니다.
   ```bash
   pwd
   python alert_server.py
   ```

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError` 는 <mark style="background:#ffc4d6">Unit 6 파일이나 `incident.py` · `notifier.py` 가 이 폴더에 없다는 뜻</mark>입니다. `complete_files.md` 에서 복사합니다.
- 출력에 `[알림 실패] ConnectionError`(연결 오류)가 나오면 <mark style="background:#ffc4d6">알림 서버가 실행 중이 아니라는 뜻</mark>입니다. 6번을 다시 실행합니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. Exercise 7-1 실행 파일은 `tickets_unit09.json` 을 읽기만 하고 다시 저장하지 않아서, 몇 번을 실행해도 같은 결과가 나옵니다.

---
