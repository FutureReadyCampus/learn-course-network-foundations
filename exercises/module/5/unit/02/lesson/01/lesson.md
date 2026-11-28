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

핵심 실습 전에 [블로그 초안 준비](__SITE__/exercises/module/5/unit/2/lesson/9/page/1)에서 이번 유닛의 글 파일을 엽니다.

Unit 1 은 알림을 플레이북으로 처리하고 알림에 맥락을 붙이는 판단 단계였습니다. 오늘은 판단한 대응 조치를 연습용 시스템(실제 서버 대신 연습용으로 만든 시뮬레이션 환경)에서 **실행하고, 사후 검증하고, 감사 기록으로 남깁니다**. 사후 검증(post-action verification)은 조치 후 실제 상태를 다시 확인하는 일이고, 감사 기록(audit log)은 조치를 순서대로 남긴 기록입니다. 침해 사고 대응에서 이 단계는 봉쇄(containment, 컨테인먼트: 피해가 더 확산되기 전에 사고를 차단하는 단계)에 해당합니다. 미국 국립표준기술연구원(NIST)이 낸 침해 사고 대응 안내서 NIST SP 800-61 Rev. 2 는 봉쇄를 「봉쇄 · 제거 · 복구」(Containment, Eradication, and Recovery) 단계 안에 둡니다.

<h2>오늘의 계획 (약 2시간 45분)</h2>

| 순서 | 시간 | 하는 일 |
|---|---|---|
| 1. 시작 | 15분 | Unit 1 파일을 확인하고 설정 파일 세 개를 만든다 |
| 2. 블로그 초안 준비 | 5분 | 「블로그 초안 준비」에서 블로그 초안을 만든다 |
| 3. 핵심 실습 | 약 110분 | 실습 2-1 → 실습 2-2, 초안에 핵심 결과 작성 |
| 4. 핵심 결과 점검과 코드 저장소 반영 | 15분 | 실습 2-2 끝의 점검 절차를 마친다 |
| 5. 포트폴리오 기록 | 20분 | 「문제 해결 기록을 포트폴리오에 남기기」에서 초안을 다듬고 올린다 |

실습 중에는 초안에 근거를 메모하고 글쓰기 시간에 같은 파일을 다듬습니다. 오늘의 핵심 실습에는 `audit.py` · `approvals.py` · `ip_actions.py` 가 필요하지 않습니다. 핵심 결과를 확인하고 포트폴리오 기록을 남긴 뒤, 선택 응용이나 Unit 3을 위해 필요한 함수 준비 레슨으로 이동합니다.

<h2>오늘 만들 것 두 가지</h2>

1. **실습 2-1**: 계정 잠금(account lockout, 어카운트 락아웃: 계정의 로그인을 비활성화하는 조치)을 실행하고 <mark>잠금 상태를 사후 검증</mark>하며, 조치 전 · 후 상태를 감사 기록으로 남깁니다(`containment_store.py` · `account_actions.py`). 직접 쓰는 곳은 빈칸 세 곳(① · ② · ③)입니다.
2. **실습 2-2**: 계정을 잠가도 <mark>이미 발급된 세션(session, 세션: 로그인한 뒤 서버가 유지하는 접속 상태)이 활성 상태(active, 액티브: 아직 유효한 상태)로 남는 문제</mark>를 세션 종료(session termination)로 해소하고, 잠긴 계정에 활성 세션이 잔존하는지 점검합니다(`session_actions.py` · `containment.py`). 직접 쓰는 곳은 빈칸 세 곳(① · ② · ③)입니다. 실행하면 상태 파일 `containment_state.json` · `containment_log.json` 이 생기고, Unit 3 실습 3-1 이 이 두 파일을 읽습니다.

**다음 단계에서 쓰는 함수** — `audit.py` · `approvals.py` 는 선택 응용 2-1 · 2-2에서, `ip_actions.py` 는 선택 응용 2-3과 Unit 3에서 사용합니다. 핵심 실습에 이 함수들은 필요하지 않으며, 포트폴리오 기록 뒤의 함수 준비 레슨에서 각 목적과 준비 순서를 확인합니다.

| 파일 | 들어 있는 함수 |
|---|---|
| `ip_actions.py` | 허용 목록 IP 와 공유 IP 를 가려 차단하고, 유효 기간이 지나면 자동 해제하는 함수 |
| `audit.py` · `approvals.py` | 감사 기록 한 건을 만들고, 담당자의 승인 · 거절을 권한 확인 뒤 적용하는 함수 |

**응용 2-1 ~ 2-3은 선택입니다.** 핵심 실습과 문제 해결 기록을 마친 뒤 진행합니다. 응용에 필요한 함수와 이전 Unit의 준비 여부는 각 응용에서 안내합니다. 선택 응용을 건너뛰어도 오늘의 핵심 학습은 완료할 수 있습니다.

새로 배울 문법은 없습니다. 미리 채운 줄에 처음 보는 `copy.deepcopy()` 가 있고, 전에 본 튜플(Module 4 Unit 1)과 `리스트.remove()`(Module 3 Unit 4)도 나옵니다. 셋 다 실습 2-1 에서 읽는 법을 설명합니다. 실습 기록의 [핵심 질문]에는 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 코드를 쓸 때는 들여쓰기를 미리 채운 줄에 맞추고, 각 번호 주석 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

## 이전 파일 확인하고 설정 파일 세 개 만들기

오늘 핵심 실습은 Unit 1 실습 1-2 레슨에서 만든 `incident.py` 의 `load_json` · `save_json` 만 씁니다. 먼저 이 파일이 있는지 봅니다.

1. **[VS Code]** `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다. 터미널 이름 칸이 **bash** 가 아니면 터미널 오른쪽 위 `+` 옆의 **∨** 를 눌러 **Git Bash** 를 고릅니다.
2. **[터미널]** Module 5 폴더 `soar_response` 로 들어가 Unit 1 파일을 확인합니다.
   ```bash
   pwd
   cd soar_response
   ls
   python - <<'PY'
from incident import load_json, save_json

print('Unit 1 파일 정상')
PY
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
   - 마지막 줄에 <mark>`Unit 1 파일 정상`</mark> 이 나오면 됩니다. 오류가 나면 Unit 1 실습 1-2 레슨의 `incident.py` 코드 상자로 파일을 만들고 다시 칩니다.

<!-- checklist -->
- [ ] `soar_response` 폴더에서 Unit 1 확인 명령을 쳐 `Unit 1 파일 정상` 이 나왔다
<!-- /checklist -->

3. **파일은 이렇게 만듭니다.** 코드 상자에서 내용을 복사해 새 파일로 저장합니다.
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S` 로 저장합니다.
   - 핵심 실습 전에 [블로그 초안 준비](__SITE__/exercises/module/5/unit/2/lesson/9/page/1)에서 이번 유닛의 글 파일을 엽니다.
4. **[VS Code]** 설정 · 데이터 파일 세 개를 만듭니다. 경로는 모두 작업 폴더 `network-study-notes/soar_response` 기준입니다.
   - `soar_response` 폴더 안의 `config` 폴더를 오른쪽 클릭 › **New File** 으로 `vip_accounts.json` 과 `allowlist_ips.json` 을 하나씩 만듭니다(`config/vip_accounts.json` · `config/allowlist_ips.json`).
   - `soar_response` 폴더를 오른쪽 클릭 › **New File** 으로 `ip_users.json` 을 만듭니다.

**`config/vip_accounts.json`** — 자동 조치 대상에서 제외하는 **VIP 계정**(고중요도 계정: 자동 조치로 잠기면 업무 영향이 큰 계정) 리스트입니다. `gaeun` 은 계정 관리자이므로 포함했습니다. 실습 2-1 · 실습 2-2 가 읽습니다.

<pre class="copyable"><code>["gaeun"]
</code></pre>

**`config/allowlist_ips.json`** — **허용 목록**(allowlist, 얼라우리스트: 정상 접속이 발생하는 출처라서 차단 대상에서 제외하기로 미리 정한 IP 의 목록)입니다. 협력사 사무실 `203.0.113.80` 과 자사 취약점(vulnerability, 벌너러빌리티: 공격에 이용될 수 있는 보안상의 약점) 점검 서버 `192.0.2.10` 이 들어 있습니다. 점검 서버(취약점 스캐너)는 취약점을 찾기 위해 경로 스캔(path scan, 패스 스캔: 서버의 여러 주소에 차례로 요청을 보내 확인하는 일) 같은 요청을 보내므로 탐지 알림이 발생합니다. 그러나 자사가 의도적으로 수행하는 점검이므로 차단하면 안 됩니다. 처리 함수 준비 레슨의 `ip_actions.py` 를 쓰는 응용 2-3 과 Unit 3 이 읽습니다.

<pre class="copyable"><code>["203.0.113.80", "192.0.2.10"]
</code></pre>

**`ip_users.json`** — IP 별로 해당 IP 를 사용하는 계정의 리스트입니다. 여러 사용자가 함께 쓰는 IP(공유 IP, shared IP, 셰어드 아이피: 사무실 공용 회선처럼 한 주소를 여러 사람이 함께 쓰는 IP)를 차단하면 정상 사용자까지 접속하지 못하는 부수적 피해(collateral damage, 콜래터럴 대미지: 의도하지 않은 대상까지 영향을 받는 일)가 생깁니다. 그래서 `ip_actions.py` 가 IP 별 사용 계정 수를 셉니다. 응용 2-3 과 Unit 3 이 읽습니다.

<pre class="copyable"><code>{"203.0.113.80": ["seoyeon", "jiwoo"], "192.0.2.41": ["junho", "hana"]}
</code></pre>

<!-- checklist -->
- [ ] `config/vip_accounts.json` 을 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
- [ ] `config/allowlist_ips.json` 을 만들고 코드 상자 내용을 붙여 넣은 뒤 저장했다
- [ ] `ip_users.json` 을 `soar_response` 폴더 바로 아래에 만들고 붙여 넣은 뒤 저장했다
<!-- /checklist -->

5. **[터미널]** 파일이 정상인지 확인합니다. <mark>`1 2 2` 가 나와야</mark> 합니다(VIP 계정 1개 · 허용 목록 IP 2개 · `ip_users.json` 에 적은 IP 2개를 센 값).
   ```bash
   python - <<'PY'
import json

paths = [
    'config/vip_accounts.json',
    'config/allowlist_ips.json',
    'ip_users.json',
]
for path in paths:
    with open(path, encoding='utf-8') as file:
        print(path, len(json.load(file)))
PY
   ```

<!-- checklist -->
- [ ] 5번 확인 명령을 쳐 `1 2 2` 가 나왔다
<!-- /checklist -->

6. 문제는 **할 일 → 순서**대로 하고, `[창 이름]` 이 지금 쓸 창입니다. 막히면 이 Unit 뒤쪽의 정답을 봅니다.

**확인** — 2번의 마지막 줄에 `Unit 1 파일 정상`, 5번에 `1 2 2` 가 나오면 성공입니다. 안 나오면 다음 페이지 「오류가 나면」의 표에서 오류 이름을 찾습니다.

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.

| 오류 | 뜻 | 고치는 법 |
|---|---|---|
| `ModuleNotFoundError: No module named 'incident'` | <mark>`incident.py` 가 이 폴더에 없다</mark> | Unit 1 실습 1-2 레슨의 코드 상자로 다시 만든다 |
| `FileNotFoundError` | JSON 파일이 없거나 다른 폴더에 있다 | 아래 위치에 파일을 둔다 |

- `vip_accounts.json` · `allowlist_ips.json` 은 `config` 폴더 안에, `ip_users.json` 은 `soar_response` 폴더 바로 아래에 있어야 합니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 해당 실습 아래의 정답 펼침을 보고, 풀리지 않으면 초안에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 실행 파일은 실행할 때마다 처음 상태에서 시작해 같은 결과가 나옵니다. **Unit 1 파일은 고치지 않습니다.** 오늘 만드는 파일은 모두 새 파일입니다.

**확인** — 앞 페이지의 두 명령을 다시 쳐서 `Unit 1 파일 정상` 과 `1 2 2` 가 나오면 성공입니다. 그래도 오류가 나면 오류 전체를 초안에 붙여 두고 실습 2-1 로 넘어가지 않습니다.

---
