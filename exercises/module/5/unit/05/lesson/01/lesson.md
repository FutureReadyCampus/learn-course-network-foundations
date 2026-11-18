---
id: m5-u05-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/124_day03_pm_rollback_drill.md
  mission_id: GichanSource.m5-1111-pm-rollback-drill
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 되돌리기와 일괄 처리

Unit 4에서 계정 잠금 · IP 차단 · 세션 종료(세션, session: 로그인한 뒤 서버에 이어져 있는 접속 상태)를 확인하고 기록하며 만들었습니다. 이번 Unit에서는 그 조치를 **안전하게 되돌리고**, Unit 2에서 만든 맥락 · 경로 코드를 이어 써서 **알림 8건을 한 번에 처리**합니다.

- **실습 5-1**: 오탐으로 확인된 알림은 조치 기록을 보고 되돌립니다. <mark>자동이 바꾼 것만</mark> 되돌리고, 되돌릴 수 없는 조치는 따로 표시합니다(`undo_actions.py` · `rollback.py`).
- **실습 5-2**: 알림 8건을 맥락 붙이기(알림에 사용자 · IP 정보를 붙임) → 경로 정하기(어떻게 처리할지 정함) → 조치 순서로 처리합니다. 그다음 기록을 종류별로 요약해 <mark>사람이 확인할 건 목록</mark>을 만듭니다(`drill.py` · `shift_report.py`). 방화벽(firewall, 파이어월: 허용하지 않은 IP 의 접속을 막는 장치) 연결이 끊긴 상황도 한 건 들어 있습니다.

깃허브에 올리는 일은 실습 5-2 마지막에 합니다. 새 문법은 없습니다. 보고서에서 [핵심 질문]이 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 코드를 쓸 때는 들여쓰기를 미리 채운 줄에 맞추고, 각 번호 주석 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

 **이전 파일**:
- 실습 5-1은 Unit 1의 `incident.py` 와 Unit 4 파일(`containment_store.py` · `account_actions.py` · `ip_actions.py`)을 씁니다. 실습 4-3이 저장한 `containment_state.json` · `containment_log.json` 도 씁니다.
- 실습 5-2는 Unit 4 파일 전부와 Unit 4 데이터 파일(`config/vip_accounts.json` · `config/allowlist_ips.json` · `ip_users.json`)을 씁니다. Unit 1의 `incident.py` · `incident_samples.json`, Unit 2의 `enrichment.py` · `routing.py`, Unit 2 데이터(`users_info.json` · `source_ips.json` · `trusted_ips.json`)도 씁니다.
- 없는 파일은 각 Unit의 코드 상자에서 복사해 만듭니다. Unit 1 파일은 Unit 1 시작하기 · 실습 1-1 · 실습 1-2, Unit 2 파일은 Unit 2 시작하기 · 실습 2-1 · 실습 2-2, Unit 4 파일은 Unit 4 시작하기 · 실습 4-1 ~ 4-3 레슨에 있습니다. `containment_state.json` · `containment_log.json` 은 Unit 4의 실습 4-3 실행 파일을 한 번 실행하면 생깁니다.

## 이전 조치 기록 확인하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** Module 5 폴더로 들어가 파일을 확인합니다. <mark>`ls` 결과에 `containment_log.json` 과 `containment_state.json` 이 보이면</mark> 됩니다. 없으면 Unit 4의 실습 4-3 실행 파일을 한 번 실행하면 생깁니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
   - Unit 4의 실습 4-3 실행 파일: `python exercise4-3_run.py` (맥북은 `python3`)
3. 이 Unit에서 만드는 파일은 모두 각 실습 레슨의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 답을 적는 보고서 `report_u5.md` 는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. **[터미널]** 실습 4-3이 남긴 파일이 정상인지 확인합니다(맥북은 `python3`). <mark>`['junho', 'dami'] 5` 가 나와야</mark> 합니다. `['junho'] 4` 가 나오면 Unit 4의 실습 4-3 실행 파일(`exercise4-3_run.py`)을 아직 한 번도 실행하지 않은 것입니다.
   ```bash
   python -c "import json; print(json.load(open('containment_state.json', encoding='utf-8'))['locked_users'], len(json.load(open('containment_log.json', encoding='utf-8'))))"
   ```

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError` 는 <mark>앞 파일(`account_actions.py` · `ip_actions.py` · `enrichment.py` 등)이 이 폴더에 없다는 뜻</mark>입니다. 앞 Unit 레슨의 코드 상자로 다시 만듭니다. `FileNotFoundError` 는 `config/vip_accounts.json` 같은 데이터 파일이 없다는 뜻이고, Unit 4 레슨의 코드 상자로 다시 만듭니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 실습 5-1 실행 파일은 실습 4-3이 저장한 파일을 읽기만 하고 다시 저장하지 않아서, 몇 번을 실행해도 같은 결과가 나옵니다.

---
