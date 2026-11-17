---
id: m5-u03-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/120_day02_pm_approval_retry_flow.md
  mission_id: GichanSource.m5-1110-pm-approval-retry-flow
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 개요

Unit 2에서 알림에 맥락을 붙이고(`enrichment.py`), 처리 경로를 나누고(`routing.py`), 실행 전에 중복과 한도를 확인하는 안전장치를 만들었습니다(`safe_runner.py`). 그 결과 VIP 계정 알림은 `승인 필요` 경로로 갔고, 플레이북이 승인을 요구하는 알림은 `승인 대기` 로 멈췄습니다. 이번 Unit에서는 두 가지를 더 만듭니다.

- **Exercise 3-1**: 멈춰 있던 알림에 담당자의 결정(승인 또는 거절)을 적용합니다. 승인할 권한이 없는 사람의 승인은 막고, 모든 결정을 기록합니다.
- **Exercise 3-2**: 티켓(ticket, 티켓: 처리할 일을 한 건씩 적어 담당자에게 맡기는 요청서) 서비스 같은 외부 서비스가 잠깐 응답하지 않으면 다시 시도하고, 그래도 안 되면 담당자가 확인할 목록에 올립니다. 그리고 Unit 2부터 만든 것을 **하루 흐름**(아래 용어 설명 참고) 하나로 이어서 실행합니다.

이번 Unit에서 자주 나오는 말은 이렇습니다.

- **승인 권한**: 승인 단추를 눌러도 되는 사람입니다. 오늘 권한이 있는 사람은 `kim.sec` 과 `lee.soc` 입니다.
- **감사 기록**(audit log, 오딧 로그): 어떤 알림에 무슨 일을 했고 결과가 무엇인지 한 건씩 남긴 기록입니다. 사고가 난 뒤에 어떤 대응을 했는지 다시 확인할 때 씁니다.
- **재시도**(retry, 리트라이): 실패했을 때 같은 일을 다시 해 보는 것입니다.
- **연결 오류**(`ConnectionError`): 외부 서비스에 연결하지 못했을 때 파이썬이 내는 오류입니다.
- **연습용 시스템**(`state`): 진짜 계정 · 방화벽(firewall, 파이어월: 허용하지 않은 접속을 막는 장비나 프로그램) 대신 잠긴 계정 · 차단한 IP · 티켓을 적어 두는 연습용 딕셔너리입니다.
- **하루 흐름**: 알림 하나가 처음부터 끝까지 지나가는 전체 처리 과정입니다. Unit 2의 맥락 붙이기 · 경로 정하기 · 안전장치(이미 잠긴 계정 건너뛰기, 잠금 한도)와 이번 Unit의 승인 · 재시도를 합친 것입니다. 알림 한 건은 맥락 붙이기 → 경로 정하기를 거친 뒤, 경로에 따라 오탐 종료 · 승인 대기 · 재시도하며 실행(이때 안전장치가 함께 쓰입니다) 중 하나로 처리됩니다.

깃허브에 올리는 일은 Exercise 3-2 마지막에 합니다. 새 문법은 Exercise 3-2의 `try` / `except` 하나입니다. 보고서에서 [핵심 질문]이 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 들여쓰기는 미리 채운 줄에 맞춥니다. 각 번호 주석 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

 **이전 파일**: Exercise 3-1은 Unit 1의 `incident.py` 만 씁니다. Exercise 3-2는 Unit 2 파일(`enrichment.py` · `routing.py` · `safe_runner.py`)을 씁니다. 또 Unit 2에서 쓴 데이터 파일 `users_info.json` · `source_ips.json` · `trusted_ips.json` 도 씁니다(JSON, 제이슨: 이름과 값을 짝지어 적는 파일 형식). 여기에 Unit 1의 `incident_samples.json` · `config/playbook_registry.json` 도 씁니다. 없는 파일은 `complete_files.md` 의 해당 절에서 복사합니다.

## 시작하기 순서

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 5과목 폴더로 들어가 파일을 확인합니다. <mark>`ls` 결과에 `config` · `incident.py` · `incident_samples.json` · `enrichment.py` · `routing.py` · `safe_runner.py` · `users_info.json` · `source_ips.json` · `trusted_ips.json` 이 보이면</mark> 됩니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. 오늘 받은 파일 두 개(안내 파일과 보고서)를 `soar_response` 폴더로 옮기고, 보고서 제목의 `이름` 을 내 이름으로 바꿉니다.
4. **[터미널]** 데이터 파일 두 개를 만들고 **[VS Code]** 에서 열어 아래 내용을 붙여 넣습니다.
   ```bash
   touch pending.json decisions.json
   ls
   ```

**`pending.json`** — 승인을 기다리는 건 3건입니다(Unit 2에서 `승인 필요` 경로로 간 VIP 알림 1건과, 플레이북이 승인을 요구해 멈춘 2건). `INC-002` 같은 번호는 **인시던트**(incident, 보안 알림 가운데 사람이 확인하고 대응해야 하는 사건 한 건)에 붙인 관리 번호입니다. 각 건에는 어떤 플레이북(playbook, 플레이북: 알림 종류별로 어떤 대응을 할지 적어 둔 절차) 때문에 멈췄는지, 승인되면 어떤 액션을 실행하는지, 왜 승인이 필요한지가 적혀 있습니다. Exercise 3-1은 이 파일을 읽어서 씁니다. Exercise 3-2 하루 흐름은 이 파일을 읽지 않고, 코드가 같은 내용을 직접 만듭니다.

```
[
  {"id": "INC-002", "entity": "seoyeon", "playbook": "PB-002", "actions": ["담당자 알림", "티켓 생성"], "why": "플레이북 승인 값이 담당자 승인 필요", "status": "분류됨"},
  {"id": "INC-003", "entity": "gaeun", "playbook": "VIP 확인", "actions": ["담당자 알림", "티켓 생성"], "why": "VIP 계정이라 경로가 승인 필요", "status": "분류됨"},
  {"id": "INC-005", "entity": "198.51.100.90", "playbook": "PB-003", "actions": ["IP 차단", "티켓 생성"], "why": "플레이북 승인 값이 담당자 승인 필요", "status": "분류됨"}
]
```

**`decisions.json`** — 담당자가 메신저에서 누른 승인 · 거절 결과를 파일로 흉내 낸 것입니다. 건마다 적힌 것은 세 가지입니다. 누가 눌렀는지(`approver`), 승인과 거절 중 무엇을 눌렀는지(`result`), 남긴 말(`comment`)입니다. 권한이 있는 담당자는 `kim.sec` · `lee.soc` 이고 `intern01` 은 권한이 없습니다. Exercise 3-1과 Exercise 3-2가 읽습니다.

```
{
  "INC-002": {"approver": "kim.sec", "result": "승인", "comment": "대량 다운로드 사유를 확인해야 함"},
  "INC-003": {"approver": "kim.sec", "result": "거절", "comment": "계정 관리자의 정상 작업으로 확인됨"},
  "INC-005": {"approver": "intern01", "result": "승인", "comment": "IP 차단 진행"}
}
```

5. **[터미널]** 파일이 정상인지 확인합니다(맥북은 `python3`). <mark>`3 3` 이 나와야</mark> 합니다.
   ```bash
   python -c "import json; print(len(json.load(open('pending.json', encoding='utf-8'))), len(json.load(open('decisions.json', encoding='utf-8'))))"
   ```

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError` 는 <mark>`incident.py` · `enrichment.py` 같은 앞 파일이 이 폴더에 없다는 뜻</mark>입니다. `complete_files.md` 에서 복사합니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env`(API 키를 적어 둔 파일) · API 키(외부 서비스를 쓸 수 있게 확인하는 비밀 문자열)는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다.

---
