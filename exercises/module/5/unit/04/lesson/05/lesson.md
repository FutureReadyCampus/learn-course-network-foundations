---
id: m5-u04-l05
title: 응용 4-1 · 기한 초과 티켓 에스컬레이션
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/128_day04_pm_escalation_metrics.md
  mission_id: GichanSource.m5-1112-pm-escalation-metrics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 응용 4-1 · 기한 초과 티켓 에스컬레이션

## 목표: 에스컬레이션 함수

> **여유가 되면 해 보세요.** 핵심 실습 4-1 · 4-2와 글쓰기를 먼저 마칩니다. 응용 4-1 ~ 4-5 가운데 하고 싶은 것만 골라 해도 됩니다. 이 응용과 응용 4-2 는 `flask` · `requests` 와 알림 서버를 쓰고, 다음 페이지 「필요한 파일 준비하기」를 먼저 합니다. 하지 않아도 다음 Unit 을 따라가는 데 문제가 없습니다.

> **오늘 들어온 일**
>
> - **상황**: Unit 3 티켓 파일에 있는 `TCK-1`(퇴사한 `dami` 계정, 등급 high)은 <mark style="background:#ffdcb0">응답 기한(SLA)이 15분입니다</mark>. 즉, 티켓이 생성된 뒤 15분 안에 담당자가 확인해야 합니다. 확인(acknowledge, 애크날리지)은 알림을 받았고 처리를 맡았다고 표시하는 일입니다. 티켓 상태 `열림`(open, 오픈)은 아직 아무도 확인하지 않은 상태입니다. 그런데 20분이 되도록 어떤 담당자도 `TCK-1` 을 확인하지 않아 `열림` 그대로라고 해 봅시다. 이때는 응답 기한을 5분 넘긴 것입니다.
> - **문제**: 두 가지입니다. 먼저 용어를 정리합니다. 에스컬레이션(escalation)은 처리되지 않는 일을 상급자에게 추가로 통보하는 일입니다.
> - 첫째, <mark style="background:#ffc4d6">티켓이 `열림` 상태로 응답 기한을 초과해도 통보 체계가 없으면 위험도가 높은 사건이 처리되지 않은 채 남습니다</mark>. `TCK-1` 은 high 등급의 퇴사자 계정 사건인데도 방치될 수 있습니다.
> - 둘째, 담당자가 이미 확인 중인 티켓까지 반복해서 에스컬레이션하면 상급자에게 알림이 지나치게 많아집니다. 그러면 상급자가 알림 피로(alert fatigue: 알림이 지나치게 많아 중요한 알림에도 반응이 둔해지는 현상)를 겪고 알림을 무시하게 됩니다.
> - **부탁**: 다음 세 가지를 만들어 주세요.
> - <mark>응답 기한이 지났는데 아직 `열림` 상태인 티켓만</mark> 상급자에게 에스컬레이션해 주세요.
> - <mark style="background:#ffdcb0">응답 기한을 초과한 시간이 길수록 더 높은 직급의 상급자에게 통보해 주세요</mark>. 기한을 넘기면 바로 팀장(`team.lead`)에게, 30분 이상 넘기면 관제 센터장(`soc.head`)에게 통보합니다. 예를 들어 5분 초과는 팀장 대상입니다.
> - 같은 에스컬레이션 단계는 한 번만 실행해 주세요.
> - **바뀌는 점**: 방치된 티켓은 초과 시간에 따라 단계적으로 상급자에게 에스컬레이션되고, 확인 중인 티켓은 대상에서 제외됩니다. 오늘 샘플은 20 · 60 · 110분에 세 번 점검합니다. 점검은 정해진 시각마다 티켓 상태를 조회하는 일입니다.
> - 20분: `TCK-1` 이 5분 초과라서 `team.lead` 에게 통보합니다. 그 뒤 25분에 `kim.sec` 이 `TCK-1` 을 확인해 상태가 `확인 중` 이 됩니다.
> - 60분: `TCK-1` 은 `확인 중` 이므로 대상에서 제외됩니다. 통보는 없습니다.
> - 110분: `TCK-3`(42분 초과)과 `TCK-4`(38분 초과)는 `soc.head` 에게, `TCK-6`(15분 초과)은 `team.lead` 에게 통보합니다.
> - 세 번의 점검에서 에스컬레이션이 실행된 횟수를 모두 합하면 4번입니다. 상황과 숫자는 설명을 위한 예시입니다.

## 필요한 파일 준비하기

응용 4-1 과 응용 4-2 는 Unit 3 티켓 파일과 알림 서버를 씁니다. 아래 순서대로 준비합니다.

**1. Unit 3 파일**: `soar_response` 폴더에 아래 파일이 있어야 합니다. 없는 파일은 알려 준 레슨의 코드 상자로 만듭니다.

| 만드는 레슨 | 파일 |
|---|---|
| Unit 3 「시작하기」 레슨 | `alerts_thu.json` · `config/escalation_rules.json` |
| Unit 3 실습 3-2 | `ticketing.py` |
| M5 Unit 3 「선택 과제용 티켓 병합·알림 함수 준비」 레슨 | `notifier.py` · `ticket_merge.py` · `ticket_notice.py` |
| Unit 3 응용 3-3 레슨의 코드 상자 | `alert_server.py` |

응용 3-3 을 하지 않았어도 그 레슨의 `alert_server.py` 상자만 복사해 만듭니다.

**2. 티켓 파일** `tickets_unit09.json`: Unit 3 응용 3-3 을 실행했다면 그때 저장된 파일이 이미 있습니다. 없으면 아래 내용으로 만듭니다(파일 이름 속 `unit09` 는 이름을 바꾸지 않고 그대로 씁니다).

<h2><code>tickets_unit09.json</code></h2>

Unit 3 근무(알림 11건)가 끝났을 때의 티켓 7장입니다. Unit 3 응용 3-3 의 `apply3-3_run.py` 가 저장하는 파일과 내용이 같습니다. 모든 티켓이 아직 `열림` 이고 `escalation_level` 은 0 입니다.

<pre class="copyable"><code>[
  {"id": "TCK-1", "title": "[high] dami — 퇴사한 계정", "entity": "dami", "rule": "퇴사한 계정", "grade": "high", "playbook": "PB-001", "done": ["계정 잠금: 잠기지 않음 → 잠김", "세션 종료: 세션 2개 → 세션 0개", "계정 잠금: 잠김 → 잠김 (이미 잠겨 있어 변경 없음)", "계정 잠금: 잠김 → 잠김 (이미 잠겨 있어 변경 없음)", "계정 잠금: 잠김 → 잠김 (이미 잠겨 있어 변경 없음)"], "status": "열림", "next_step": "조치 결과가 맞는지 확인하고 계정이나 IP 상태를 점검한다", "needs_manual": false, "created_at": 0, "updated_at": 95, "sla_due": 15, "count": 4, "incidents": ["INC-201", "INC-205", "INC-209", "INC-210"], "notified_count": 3, "last_notified": 95, "acked_at": -1, "resolved_at": -1, "escalation_level": 0, "comments": []},
  {"id": "TCK-2", "title": "[low] 198.51.100.90 — 경로 스캔", "entity": "198.51.100.90", "rule": "경로 스캔", "grade": "low", "playbook": "PB-003", "done": ["IP 차단: 차단되지 않음 → 차단됨", "IP 차단: 차단됨 → 차단됨 (이미 차단되어 변경 없음)"], "status": "열림", "next_step": "조치 결과가 맞는지 확인하고 계정이나 IP 상태를 점검한다", "needs_manual": false, "created_at": 3, "updated_at": 20, "sla_due": 243, "count": 2, "incidents": ["INC-202", "INC-206"], "notified_count": 1, "last_notified": 3, "acked_at": -1, "resolved_at": -1, "escalation_level": 0, "comments": []},
  {"id": "TCK-3", "title": "[mid] gaeun — 규칙은 허용인데 서버가 거절", "entity": "gaeun", "rule": "규칙은 허용인데 서버가 거절", "grade": "mid", "playbook": "VIP 확인", "done": [], "status": "열림", "next_step": "승인할지 거절할지 정하고 정한 사람의 이름을 남긴다", "needs_manual": false, "created_at": 8, "updated_at": 8, "sla_due": 68, "count": 1, "incidents": ["INC-203"], "notified_count": 1, "last_notified": 8, "acked_at": -1, "resolved_at": -1, "escalation_level": 0, "comments": []},
  {"id": "TCK-4", "title": "[mid] seoyeon — 대량 다운로드", "entity": "seoyeon", "rule": "대량 다운로드", "grade": "mid", "playbook": "PB-002", "done": [], "status": "열림", "next_step": "승인할지 거절할지 정하고 정한 사람의 이름을 남긴다", "needs_manual": false, "created_at": 12, "updated_at": 12, "sla_due": 72, "count": 1, "incidents": ["INC-204"], "notified_count": 1, "last_notified": 12, "acked_at": -1, "resolved_at": -1, "escalation_level": 0, "comments": []},
  {"id": "TCK-5", "title": "[low] 203.0.113.250 — 경로 스캔", "entity": "203.0.113.250", "rule": "경로 스캔", "grade": "low", "playbook": "PB-003", "done": ["IP 차단: 차단되지 않음 → 차단되지 않음 (확인 실패)"], "status": "열림", "next_step": "조치가 확인되지 않았다. 담당자가 직접 계정이나 IP 상태를 보고 조치한다", "needs_manual": true, "created_at": 30, "updated_at": 30, "sla_due": 270, "count": 1, "incidents": ["INC-207"], "notified_count": 1, "last_notified": 30, "acked_at": -1, "resolved_at": -1, "escalation_level": 0, "comments": []},
  {"id": "TCK-6", "title": "[mid] hana — 업무 시간 밖 로그인", "entity": "hana", "rule": "업무 시간 밖 로그인", "grade": "mid", "playbook": "없음", "done": [], "status": "열림", "next_step": "자동 조치가 없는 알림이니 직접 보고 조치가 필요한지 정한다", "needs_manual": false, "created_at": 35, "updated_at": 35, "sla_due": 95, "count": 1, "incidents": ["INC-208"], "notified_count": 1, "last_notified": 35, "acked_at": -1, "resolved_at": -1, "escalation_level": 0, "comments": []},
  {"id": "TCK-7", "title": "[high] dami — 퇴사한 계정", "entity": "dami", "rule": "퇴사한 계정", "grade": "high", "playbook": "PB-001", "done": ["계정 잠금: 잠김 → 잠김 (이미 잠겨 있어 변경 없음)"], "status": "열림", "next_step": "조치 결과가 맞는지 확인하고 계정이나 IP 상태를 점검한다", "needs_manual": false, "created_at": 160, "updated_at": 160, "sla_due": 175, "count": 1, "incidents": ["INC-211"], "notified_count": 1, "last_notified": 160, "acked_at": -1, "resolved_at": -1, "escalation_level": 0, "comments": []}
]
</code></pre>

<!-- checklist optional -->
- [ ] 1번 표의 Unit 3 파일과 `tickets_unit09.json` 가운데 없던 파일을 `soar_response` 폴더에 만들고 저장했다
<!-- /checklist -->

<h2>순서</h2>

1. **[터미널]** 서버와 알림 전송에 쓰는 도구를 설치합니다. 이미 설치했다면 바로 다음 줄로 갑니다.
   ```bash
   python -m pip install flask requests
   ```
   - 가상환경을 쓴다면 먼저 켭니다(`source ../.venv/Scripts/activate`). 터미널 맨 앞에 `(.venv)` 가 보이면 켜진 것입니다. 가상환경을 쓰지 않으면 건너뜁니다.
2. **[터미널]** 파일을 확인합니다. <mark style="background:#bde3ff">`응용 준비 정상 7` 이 나와야</mark> 합니다.
   ```bash
   pwd
   python - <<'PY'
import ticketing
import ticket_merge
import ticket_notice
import notifier
import alert_server
from incident import load_json

print('응용 준비 정상', len(load_json('tickets_unit09.json')))
PY
   ```
   - `No module named '…'` 가 나오면 1번 목록에서 그 이름의 파일을 찾아 만듭니다. `No module named 'requests'` 는 1번 설치를 다시 합니다.

<!-- checklist optional -->
- [ ] `python -m pip install flask requests` 로 설치하고, 2번 명령에서 `응용 준비 정상 7` 이 나왔다
<!-- /checklist -->

3. **[터미널]** 알림 서버를 켭니다. VS Code 터미널 창 오른쪽 위의 `+` 로 **새 터미널**을 하나 더 열고, `soar_response` 폴더에서 서버를 실행합니다. <mark style="background:#bde3ff">`Running on http://127.0.0.1:5001` 이 보이면</mark> 됩니다.
   ```bash
   cd soar_response
   python alert_server.py
   ```
   - 새 터미널은 `network-study-notes` 폴더에서 열리므로 `cd soar_response` 를 먼저 칩니다. 가상환경을 쓴다면 `cd soar_response` 전에 새 터미널에서도 `source .venv/Scripts/activate` 로 켭니다(맨 앞에 `(.venv)` 가 보이면 됨).
   - 이 터미널(서버 터미널)은 응용 4-1 · 4-2 를 마칠 때까지 켜 둡니다. 다른 명령은 처음 쓰던 터미널에서 칩니다.
   - `Address already in use` 가 나오면 이미 켜진 서버가 있는 것입니다. 그 서버를 그대로 쓰거나, 서버를 켠 터미널에서 `Ctrl + C` 로 끄고 다시 켭니다.

<!-- checklist optional -->
- [ ] 새 터미널에서 `python alert_server.py` 를 실행해 `Running on http://127.0.0.1:5001` 이 보였다
<!-- /checklist -->

## 1.1 에스컬레이션 규칙의 세 요소

**에스컬레이션**(escalation, 에스컬레이션: 처리되지 않는 일을 더 높은 책임자에게 넘기는 절차)은 미리 정한 규칙에 따라 실행합니다. 규칙은 아래 세 가지, 즉 <mark>언제 시작하는지(발동 시점), 어느 티켓이 대상인지(대상 티켓), 누구에게 통보하는지(통보 대상)</mark>를 정합니다. 오늘은 담당자보다 높은 직급(팀장 · 관제 센터장)에게 넘깁니다. 이 방식은 **계층적 에스컬레이션**(hierarchical escalation, 하이어라키컬 에스컬레이션: 지휘 체계를 따라 더 높은 권한자에게 넘기는 방식)에 해당합니다. 전문성이 더 높은 기술 팀에 넘기는 방식은 기능적 에스컬레이션(functional escalation)이라고 따로 부릅니다.

| 정의할 것 | 오늘 정한 방법 | 규칙 파일의 키 |
|---|---|---|
| 발동 시점(trigger) | <mark style="background:#ffdcb0">지금 시각이 응답 기한 시각(`sla_due`)을 지났을 때</mark> | 티켓의 `sla_due`(규칙 파일의 `sla_minutes` 로 계산) |
| 대상 티켓 | <mark style="background:#ffdcb0">상태가 `열림` 인 티켓만 해당한다</mark> | |
| 통보 대상 | <mark style="background:#ffdcb0">초과 시간에 따라 단계별로 통보한다</mark>(아래 표) | `escalation_steps` |

- 트리거(trigger)는 에스컬레이션을 시작하는 조건입니다. `sla_due` 의 due 는 마감이라는 뜻입니다.
- `확인 중`(담당자가 확인함)이나 `해결`(처리 완료)인 티켓은 대상에서 제외합니다.

| 응답 기한 초과 시간 | 단계 | 통보 대상 | 오늘의 예 |
|---|---|---|---|
| <mark style="background:#ffdcb0">0분 이상 30분 미만</mark> | 1단계 | `team.lead`(팀장) | `TCK-1` 5분 초과 |
| <mark style="background:#ffdcb0">30분 이상</mark> | 2단계 | `soc.head`(관제 센터장) | `TCK-3` 42분 초과 |

- 규칙 파일의 `escalation_steps` 는 단계마다 기준 시간(`overdue_minutes`, 넘긴 분)과 받는 사람(`notify`)을 적은 리스트입니다. 오늘은 `{"overdue_minutes": 0, "notify": "team.lead"}` 와 `{"overdue_minutes": 30, "notify": "soc.head"}` 두 단계가 이 순서로 들어 있습니다.
- 담당자가 티켓을 확인하면 상태가 `열림` 에서 `확인 중` 으로 변경됩니다. 출력과 코드에서는 에스컬레이션 단계를 「올림 단계」라고 표시합니다.
- 이미 실행한 에스컬레이션 단계는 반복하지 않습니다. 티켓의 `escalation_level` 에 실행한 단계를 기록합니다. 그리고 기록된 단계보다 더 높은 단계에 해당할 때만 에스컬레이션합니다. 예를 들어 `escalation_level` 이 1 인 티켓은 1단계에 해당하는 동안 다시 통보하지 않고, 초과 시간이 30분 이상이 되어 2단계에 해당할 때 통보합니다. <mark style="background:#ffc4d6">점검할 때마다 같은 티켓을 반복해서 통보하면 상급자가 알림 피로를 겪어 알림을 무시하게 됩니다</mark>.
- 등급 low 는 응답 기한이 240분입니다. 그래서 오늘 점검 시각(20 · 60 · 110분)은 모두 응답 기한 시각보다 이릅니다. 예를 들어 `TCK-2` 의 응답 기한 시각은 243분입니다. 따라서 등급 low 티켓은 에스컬레이션 대상이 아닙니다.
- 점검 시각은 20분, 60분, 110분입니다(근무 시작 시점을 0분으로 하는 상대 시각). 이처럼 정해진 주기로 상태를 반복 조회하는 방식을 폴링(polling, 폴링: 일정한 간격으로 상태를 반복해서 확인하는 방식)이라고 합니다. 실제 운영에서는 몇 분마다 자동으로 점검합니다.
- 상급자에게 통보하는 기능은 `send_with_retry`(알림 전송에 실패하면 최대 3회까지 재시도(retry)하는 함수)를 재사용합니다. 이 함수가 든 `ticket_notice.py` 는 M5 Unit 3 「선택 과제용 티켓 병합·알림 함수 준비」 레슨의 파일입니다(Unit 3 응용 3-3 에서 직접 써 보는 파일).

아래 함수 네 개와 실행 파일 가운데 직접 쓰는 곳은 **아홉 군데**입니다.

```
escalation.py   overdue_minutes   : 응답 기한을 넘긴 시간(분)을 구한다 (1번)
                needs_escalation  : 열림 상태이고 기한이 지났으면 True 를 리턴한다 (2 ~ 4번)
                pick_level        : 넘긴 시간에 해당하는 가장 높은 올림 단계를 고른다 (5 · 6번)
                escalate_ticket   : 그 단계의 상급자에게 알리고 올린 단계를 적는다 (미리 채움)
실행 파일       apply4-1_run.py  : 점검 시각마다 올릴 티켓을 찾고 (7번), 올리고 (8번), 올린 횟수를 센다 (9번)
```

## 응용 4-1 · 기한 초과 티켓 에스컬레이션

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>티켓이 확인되지 않은 채 응답 기한을 초과해도 상급자에게 에스컬레이션되지 않습니다</mark>.
- **만드는 것**: 두 파일을 만듭니다. `escalation.py` 는 응답 기한 초과 시간을 구하고, 에스컬레이션 대상 티켓을 가려내고, 에스컬레이션 단계를 고릅니다. `apply4-1_run.py` 는 점검 시각마다 대상 티켓을 에스컬레이션하고 실행 횟수를 셉니다. 상급자에게 통보하는 함수는 미리 채워져 있습니다.
- **실행하면**: <mark>출력은 세 단계입니다. 단계 1 은 불러온 티켓 수와 올림 단계 수입니다. 단계 2 는 점검 시각마다 올린 티켓입니다. 단계 3 은 올린 결과 요약입니다.</mark>

**할 일**: `soar_response` 폴더에 `escalation.py` · `apply4-1_run.py` 두 파일을 만들어 붙여 넣고 번호 주석 바로 아래에 직접 코드를 씁니다. 알림 서버를 실행한 상태에서 프로그램을 실행합니다. 그리고 단계 2 · 3 의 출력과 서버 터미널의 수신 로그를 해석합니다.

<h3><code>escalation.py</code></h3>

응답 기한이 지난 티켓을 상급자에게 올립니다. 응용 4-2에서도 이 파일을 가져와 사용(import)합니다. 「선택 과제용 에스컬레이션·리포트 함수 준비」 레슨에서 완성본을 만들어 두었다면 그 파일을 아래 골격으로 바꿔 직접 써 봅니다. 직접 쓰는 곳은 1 ~ 6번입니다. 5번 아래에는 `if` 한 줄을, 6번 아래에는 한 단계 더 들여쓴 줄을 씁니다.

- 2번 아래에는 `if` 한 줄을 씁니다. 3번은 그 `if` 안쪽이라 주석 위치보다 한 단계(공백 4개) 더 들여 씁니다. 주석 `# 3.` 뒤의 빈칸이 그 표시입니다.
- 미리 채운 `for index in range(len(steps)):` 는 0 부터 (단계 수 − 1) 까지의 번호를 차례로 꺼냅니다. `range(숫자)` 는 0 부터 그 숫자 바로 앞까지의 번호를 만듭니다. 리스트 번호는 0 부터 세므로 사람이 읽는 단계 번호는 `index + 1` 입니다.

```python exercise
from ticket_notice import send_with_retry, MAX_TRIES                                       # Unit 3 에 있는 재시도 함수를 불러온다


def overdue_minutes(ticket, now):                                                          # 티켓과 지금 시각(분)을 받는 함수
    """응답 기한을 넘긴 시간(분)을 리턴한다. 기한이 아직 안 됐으면 음수가 나온다.
    얼마나 늦었는지 알아야 어느 상급자에게 올릴지 정할 수 있어서 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. now 에서 ticket["sla_due"] 를 뺀 값을 리턴한다
#|     return now - ticket["sla_due"]


def needs_escalation(ticket, now):                                                         # 티켓과 지금 시각(분)을 받는 함수
    """아직 열림 상태이고 응답 기한이 지났으면 True, 아니면 False 를 리턴한다. 담당자가 이미 확인 중이거나 해결한 티켓은 올리지 않는다.
    아무도 열어 보지 않은 티켓만 골라낼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 2. ticket 의 "status" 가 "열림" 이 아니면 (if, !=)
#|     if ticket["status"] != "열림":
    # 3.   False 를 리턴한다
#|         return False
    # 4. overdue_minutes(ticket, now) 가 0 이상인지(>=)의 결과를 리턴한다
#|     return overdue_minutes(ticket, now) >= 0


def pick_level(overdue, steps):                                                            # 넘긴 시간과 올림 단계 리스트를 받는 함수
    """넘긴 시간에 해당하는 가장 높은 올림 단계 번호(1부터)를 리턴한다. 해당하는 단계가 없으면 0 을 리턴한다.
    오래 방치된 티켓일수록 더 높은 상급자에게 올릴 때 쓴다.
    """
    level = 0                                                                              # 처음에는 올릴 단계가 없다 — 미리 채운 줄
    for index in range(len(steps)):                                                        # 단계 번호를 0 부터 하나씩 읽는다 — 미리 채운 줄
        step = steps[index]                                                                # 그 번호의 올림 단계 — 미리 채운 줄
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 5. overdue 가 step 의 "overdue_minutes" 이상이면 (if, >=)
#|         if overdue >= step["overdue_minutes"]:
            # 6. level 에 index + 1 을 저장한다
#|             level = index + 1
    return level                                                                           # 가장 높은 단계 번호를 리턴한다 — 미리 채운 줄


def escalate_ticket(ticket, now, rules):                                                   # 티켓 · 지금 시각(분) · 규칙을 받는 함수
    """티켓을 상급자에게 올린다. 이미 올린 단계이거나 올릴 때가 아니면 「그대로」, 올렸으면 「올림」, 알림이 모두 실패했으면 「실패」를 리턴한다.
    응답 기한이 지나도 아무도 확인하지 않은 티켓을 놓치지 않을 때 쓴다.
    """
    overdue = overdue_minutes(ticket, now)                                                 # 기한을 얼마나 넘겼는지
    steps = rules["escalation_steps"]                                                      # 규칙 파일의 올림 단계 리스트
    level = pick_level(overdue, steps)                                                     # 지금 해당하는 올림 단계
    if level <= ticket["escalation_level"]:                                                # 이미 올린 단계이거나 아직 올릴 때가 아니면
        return "그대로"                                                                    # 아무것도 하지 않는다
    step = steps[level - 1]                                                                # 그 단계의 규칙(받는 사람)
    message = "[올림 " + str(level) + "단계] " + ticket["id"] + " " + ticket["title"] + " · 기한을 " + str(overdue) + "분 넘김 · 받는 사람: " + step["notify"]  # 알림 내용을 만든다
    attempt = send_with_retry(message, rules["alert_url"], MAX_TRIES)                      # 최대 3번까지 보내 본다
    if attempt == 0:                                                                       # 모두 실패했으면
        return "실패"                                                                      # 올리지 못했다고 「실패」를 리턴한다
    ticket["escalation_level"] = level                                                     # 올린 단계를 적는다
    comment = str(now) + "분 · " + str(level) + "단계로 " + step["notify"] + " 에게 올림"  # 댓글 내용을 만든다
    ticket["comments"].append(comment)                                                     # 댓글 리스트에 추가한다
    return "올림"                                                                          # 「올림」을 리턴한다
```

<h3><code>apply4-1_run.py</code></h3>

7 ~ 9번만 직접 쓰고 나머지는 그대로 붙여 넣습니다. 7번 아래에는 `if` 한 줄을, 8번 아래에는 한 단계 더 들여쓴 줄을, 9번 아래에는 또 한 단계 들여쓴 줄을 씁니다. 그 사이의 미리 채운 줄은 그대로 둡니다.

```python exercise
from incident import load_json                                                       # Unit 1 파일의 JSON 읽기 함수를 불러온다
from ticket_merge import change_ticket_status                                        # Unit 3 에 있는 상태 바꾸기 함수를 불러온다
from escalation import overdue_minutes, needs_escalation, escalate_ticket            # 방금 만든 함수를 불러온다

tickets = load_json("tickets_unit09.json")                                           # Unit 3 근무가 끝났을 때의 티켓을 읽는다
rules = load_json("config/escalation_rules.json")                                    # 규칙 파일을 읽는다
steps_count = len(rules["escalation_steps"])                                         # 올림 단계가 몇 개인지 센다
print("--- 단계 1: 불러온 티켓", len(tickets), "장 · 올림 단계", steps_count, "개")  # 단계 1 시작을 알리는 줄
escalated_count = 0                                                                  # 상급자에게 올린 횟수 : 처음에는 0

print("--- 단계 2: 점검 시각마다 상급자에게 올릴 티켓 찾기")                         # 단계 2 시작을 알리는 줄
for now in [20, 60, 110]:                                                            # 점검할 시각(분)을 하나씩 읽는다
    print("[" + str(now) + "분] 점검")                                               # 점검 시각을 출력한다
    for ticket in tickets:                                                           # 티켓을 하나씩 읽는다
        # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
        # 7. needs_escalation(ticket, now) 가 참이면 (if)
#|         if needs_escalation(ticket, now):
            # 8. escalate_ticket(ticket, now, rules) 의 결과를 result 에 저장한다
#|             result = escalate_ticket(ticket, now, rules)
            overdue = overdue_minutes(ticket, now)                                   # 기한을 얼마나 넘겼는지 구한다 — 미리 채운 줄
            print(ticket["id"], ticket["title"], "→", result, "· 기한을", overdue, "분 넘김 · 올림 단계", ticket["escalation_level"])  # 결과를 출력한다 — 미리 채운 줄
            if result == "올림":                                                     # 올렸으면 — 미리 채운 줄
                # 9. escalated_count 에 escalated_count + 1 을 저장한다 (1 늘린다)
#|                 escalated_count = escalated_count + 1
    if now == 20:                                                                    # 20분 점검이 끝나면 — 미리 채운 줄
        change_ticket_status(tickets[0], "확인 중", 25, "kim.sec")                   # 25분에 kim.sec 이 TCK-1 을 확인하기 시작한다 — 미리 채운 줄
        print("[25분] TCK-1 → 확인 중 · kim.sec")                                    # 담당자의 동작을 출력한다 — 미리 채운 줄

print("--- 단계 3: 올린 결과 요약 (올린 횟수", escalated_count, "번)")               # 단계 3 시작을 알리는 줄과 횟수
for ticket in tickets:                                                               # 티켓을 하나씩 읽는다
    if ticket["escalation_level"] > 0:                                               # 상급자에게 올린 티켓이면
        print(ticket["id"], "올림 단계", ticket["escalation_level"], "· 상태", ticket["status"])  # 올림 단계와 지금 상태를 출력한다
```

<h2>순서</h2>

1. **[터미널]** 「필요한 파일 준비하기」의 서버 터미널에 `Running on http://127.0.0.1:5001` 이 떠 있는지 봅니다. 꺼져 있으면 그 페이지의 3번으로 다시 켭니다.
2. **[VS Code]** `soar_response` 폴더를 오른쪽 클릭 › **New File** 로 `escalation.py` 와 `apply4-1_run.py` 를 이름 그대로 만들고, 위 코드 상자를 복사해 붙여 넣고 저장합니다.

<!-- checklist optional -->
- [ ] `soar_response` 폴더에 `escalation.py` · `apply4-1_run.py` 를 만들고 붙여 넣은 뒤 저장했다
<!-- /checklist -->

3. **[VS Code]** `escalation.py` 1 ~ 6번, `apply4-1_run.py` 7 ~ 9번을 씁니다. 막히면 아래 「응용 4-1 정리」를 봅니다.

<!-- checklist optional -->
- [ ] `escalation.py` 1 ~ 6번과 `apply4-1_run.py` 7 ~ 9번을 쓰고 저장했다
<!-- /checklist -->

4. **[터미널]** 처음 쓰던 터미널에서 <mark>`pwd` 가 `soar_response` 로 끝나는지</mark> 확인하고 실행합니다.
   ```bash
   python apply4-1_run.py
   ```
5. 출력은 세 단계입니다. 제목 줄은 줄 수에 넣지 않습니다. 단계 1 은 제목 줄 하나만 나옵니다(숫자가 제목 줄 안에 함께 나옵니다). 단계 2 는 제목 아래 8줄입니다. 단계 3 은 제목 아래 4줄입니다(올린 횟수는 제목 줄 안에 있습니다). <mark>알림 서버 터미널에는 `[알림 받음]` 줄이 4개 찍힙니다.</mark> 같은 서버로 Unit 3 응용 3-3 을 먼저 실행했다면 그 줄 아래부터 셉니다.
   - `apply4-1_run.py` 는 `tickets_unit09.json` 을 읽기만 하고 다시 저장하지 않아서, 몇 번을 실행해도 같은 결과가 나옵니다(서버 터미널의 줄은 실행할 때마다 4줄씩 늘어납니다).

<!-- checklist optional -->
- [ ] `python apply4-1_run.py` 를 실행하고, 서버 터미널에 `[알림 받음]` 줄이 4개 새로 찍힌 것을 확인했다
<!-- /checklist -->

<!-- answer: 10|응용 4-1 정답 -->

## 응용 4-1 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 빼서 리턴 | `return now - ticket["sla_due"]` |
| 같지 않으면 | `if ticket["status"] != "열림":` |
| 이상인지의 결과 리턴 | `return overdue_minutes(ticket, now) >= 0` |
| 이상이면 | `if overdue >= step["overdue_minutes"]:` |
| 번호에 1 더해 저장 | `level = index + 1` |
| 함수 결과가 참이면 | `if needs_escalation(ticket, now):` |
| 함수 결과를 변수에 저장 | `result = escalate_ticket(ticket, now, rules)` |
| 1 늘려 다시 저장 | `escalated_count = escalated_count + 1` |

---
