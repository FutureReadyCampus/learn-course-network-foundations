---
id: m5-u02-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/122_day03_am_containment.md
  mission_id: GichanSource.m5-1111-am-containment
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표와 오늘의 계획

Unit 1 은 알림을 플레이북으로 처리하고 알림에 맥락을 붙이는 판단 단계였습니다. 오늘은 판단한 대응 조치를 연습용 시스템(실제 서버 대신 연습용으로 만든 시뮬레이션 환경)에서 **실행하고, 사후 검증하고, 감사 기록으로 남깁니다**. 사후 검증(post-action verification)은 조치 후 실제 상태를 다시 확인하는 일이고, 감사 기록(audit log)은 조치를 순서대로 남긴 기록입니다. 침해 사고 대응에서 이 단계는 봉쇄(containment, 컨테인먼트: 피해가 더 확산되기 전에 사고를 차단하는 단계)에 해당합니다. 미국 국립표준기술연구원(NIST)이 낸 침해 사고 대응 안내서 NIST SP 800-61 Rev. 2 는 봉쇄를 「봉쇄 · 제거 · 복구」(Containment, Eradication, and Recovery) 단계 안에 둡니다.

**오늘의 계획 (3시간)**

1. 시작하기 15분: 이 레슨을 읽고 Unit 1 파일을 확인한 뒤, 설정 파일 세 개를 만듭니다.
2. 실습 약 110분: 핵심 실습 두 개를 차례로 합니다. 실습 2-1 을 마친 뒤 「제공 파일」 레슨의 파일 세 개를 복사해 만듭니다.
3. 글쓰기 40분: 「보고서 쓰기」 레슨에서 핵심 실습의 질문에 답하고, 「오늘의 글 쓰기」 레슨에서 글 한 편을 씁니다.
4. 마무리 15분: 실습 2-2 끝의 「이번 Unit 마무리 · 깃허브에 올리기」에서 파일을 확인하고 깃허브에 올립니다.

**오늘 만들 것 두 가지**

1. **실습 2-1**: 계정 잠금(account lockout, 어카운트 락아웃: 계정의 로그인을 비활성화하는 조치)을 실행하고 <mark>잠금 상태를 사후 검증</mark>하며, 조치 전 · 후 상태를 감사 기록으로 남깁니다(`containment_store.py` · `account_actions.py`).
2. **실습 2-2**: 계정을 잠가도 <mark>이미 발급된 세션(session, 세션: 로그인한 뒤 서버가 유지하는 접속 상태)이 활성 상태(active, 액티브: 아직 유효한 상태)로 남는 문제</mark>를 세션 종료(session termination)로 해소하고, 잠긴 계정에 활성 세션이 잔존하는지 점검합니다(`session_actions.py` · `containment.py`). 실행하면 상태 파일 `containment_state.json` · `containment_log.json` 이 생기고, Unit 3 실습 3-1 이 이 두 파일을 읽습니다.

**오늘 받아 쓰는 것** — 「제공 파일」 레슨의 완성 코드 세 개입니다. 오늘 핵심 실습에서는 쓰지 않지만, 도전과 Unit 3 이 불러 씁니다.

1. `ip_actions.py`: 허용 목록 IP 와 공유 IP 를 가려 차단하고, 유효 기간이 지나면 자동 해제하는 함수
2. `audit.py` · `approvals.py`: 감사 기록 한 건을 만들고, 담당자의 승인 · 거절을 권한 확인 뒤 적용하는 함수

**도전 2-1 ~ 2-3은 선택입니다.** 핵심 실습 두 개와 글쓰기를 마치고 시간이 남을 때 합니다. 도전 2-1 · 2-3 에서는 제공 파일 `approvals.py` · `ip_actions.py` 를 빈칸이 있는 골격으로 직접 써 보고, 도전 2-2 에서는 연결 오류가 나면 다시 시도하는 하루 흐름을 만듭니다. 도전을 하지 않아도 Unit 3 을 따라갈 수 있습니다.

새 문법은 실습 2-1 의 `리스트.remove()` 하나입니다. 보고서에서 [핵심 질문]이 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 코드를 쓸 때는 들여쓰기를 미리 채운 줄에 맞추고, 각 번호 주석 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

## 이전 파일 확인하고 설정 파일 세 개 만들기

오늘 핵심 실습은 Unit 1 실습 1-2 레슨에서 만든 `incident.py` 의 `load_json` · `save_json` 만 씁니다. 먼저 이 파일이 있는지 봅니다.

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** Module 5 폴더 `soar_response` 로 들어가 Unit 1 파일을 확인합니다(맥북은 `python3`).
   ```bash
   pwd
   cd soar_response
   ls
   python -c "from incident import load_json, save_json; print('Unit 1 파일 정상')"
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
   - 마지막 줄에 <mark>`Unit 1 파일 정상`</mark> 이 나오면 됩니다. 오류가 나면 Unit 1 실습 1-2 레슨의 `incident.py` 코드 상자로 파일을 만들고 다시 칩니다.
3. **파일은 이렇게 만듭니다.** 따로 내려받는 파일은 없고, 모두 코드 상자에서 복사해 만듭니다.
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서** `report_u2.md` 는 「보고서 쓰기」 레슨의 틀을 복사해 만듭니다.
4. **[VS Code]** 설정 · 데이터 파일 세 개를 만듭니다.
   - `config` 폴더를 오른쪽 클릭 › **New File** 으로 `vip_accounts.json` 과 `allowlist_ips.json` 을 하나씩 만듭니다.
   - `soar_response` 폴더를 오른쪽 클릭 › **New File** 으로 `ip_users.json` 을 만듭니다.

**`config/vip_accounts.json`** — 자동 조치 대상에서 제외하는 **VIP 계정**(고중요도 계정: 자동 조치로 잠기면 업무 영향이 큰 계정) 리스트입니다. `gaeun` 은 계정 관리자이므로 포함했습니다. 실습 2-1 · 실습 2-2 가 읽습니다.

<pre class="copyable"><code>["gaeun"]
</code></pre>

**`config/allowlist_ips.json`** — **허용 목록**(allowlist, 얼라우리스트: 정상 접속이 발생하는 출처라서 차단 대상에서 제외하기로 미리 정한 IP 의 목록)입니다. 협력사 사무실 `203.0.113.80` 과 자사 취약점(vulnerability, 벌너러빌리티: 공격에 이용될 수 있는 보안상의 약점) 점검 서버 `192.0.2.10` 이 들어 있습니다. 점검 서버(취약점 스캐너)는 취약점을 찾기 위해 경로 스캔(path scan, 패스 스캔: 서버의 여러 주소에 차례로 요청을 보내 확인하는 일) 같은 요청을 보내므로 탐지 알림이 발생합니다. 그러나 자사가 의도적으로 수행하는 점검이므로 차단하면 안 됩니다. 제공 파일 `ip_actions.py` 를 쓰는 도전 2-3 과 Unit 3 이 읽습니다.

<pre class="copyable"><code>["203.0.113.80", "192.0.2.10"]
</code></pre>

**`ip_users.json`** — IP 별로 해당 IP 를 사용하는 계정의 리스트입니다. 여러 사용자가 함께 쓰는 IP(공유 IP, shared IP, 셰어드 아이피: 사무실 공용 회선처럼 한 주소를 여러 사람이 함께 쓰는 IP)를 차단하면 정상 사용자까지 접속하지 못하는 부수적 피해(collateral damage, 콜래터럴 대미지: 의도하지 않은 대상까지 영향을 받는 일)가 생깁니다. 그래서 `ip_actions.py` 가 IP 별 사용 계정 수를 셉니다. 도전 2-3 과 Unit 3 이 읽습니다.

<pre class="copyable"><code>{"203.0.113.80": ["seoyeon", "jiwoo"], "192.0.2.41": ["junho", "hana"]}
</code></pre>

5. **[터미널]** 파일이 정상인지 확인합니다(맥북은 `python3`). <mark>`1 2 2` 가 나와야</mark> 합니다(VIP 계정 1개 · 허용 목록 IP 2개 · `ip_users.json` 에 적은 IP 2개를 센 값).
   ```bash
   python -c "import json; print(len(json.load(open('config/vip_accounts.json', encoding='utf-8'))), len(json.load(open('config/allowlist_ips.json', encoding='utf-8'))), len(json.load(open('ip_users.json', encoding='utf-8'))))"
   ```
6. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 막히면 이 Unit 뒤쪽의 정답을 봅니다.

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError: No module named 'incident'` 는 <mark>`incident.py` 가 이 폴더에 없다는 뜻</mark>입니다. Unit 1 실습 1-2 레슨의 코드 상자로 다시 만듭니다.
- `FileNotFoundError` 는 JSON 파일이 없거나 다른 폴더에 있다는 뜻입니다. `vip_accounts.json` · `allowlist_ips.json` 은 `config` 폴더 안에, `ip_users.json` 은 `soar_response` 폴더 바로 아래에 있어야 합니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 이 Unit 뒤쪽의 정답을 보고, 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 실행 파일은 실행할 때마다 처음 상태에서 시작해 같은 결과가 나옵니다. **Unit 1 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다.

---
