---
id: m5-u01-l01
title: 시작하기
render: markdown
---

# 시작하기

## Module 5 소개와 이번 Unit에서 만들 것

앞서 Module 4를 마쳤습니다. Module 4에서는 로그를 읽어 **위험한 대상을 찾아 점수와 등급을 매겼습니다.** 이번 Unit부터 시작하는 Module 5는 그 **알림이 난 뒤에 하는 일**을 다룹니다. 계정을 잠그고, **티켓**(ticket, 티켓: 처리할 일 한 건을 적어 두고 누가 맡았는지와 처리됐는지를 추적하는 기록)을 만들고, 담당자에게 알리는 일을 정해 둔 절차대로 프로그램이 실행하게 만드는 Module입니다.

오늘은 <mark>**연습용 시스템**(실제 서버와 계정 대신 파일로 흉내 낸 시스템)에서 대응이 실제로 일어나는 것</mark>을 봅니다. 실제 서버와 계정은 건드리지 않습니다.

- **실습 1-1**: SOAR 가 무엇인지 읽고, **플레이북**(playbook, 플레이북: 「이런 알림이 오면 이렇게 대응한다」를 미리 적어 둔 대응 절차서) 한 건을 직접 씁니다. 그리고 알림 두 건을 **수동 처리**(프로그램 없이 사람이 직접 하는 처리)해 봅니다. 여기서는 VS Code 로 `system_state.json` 을 열어 값을 직접 타이핑해 넣고 저장합니다. 이 과정에서 얼마나 번거로운지 겪습니다.
- **실습 1-2**: 같은 일을 프로그램(`playbook_runner.py`)이 하게 만듭니다. <mark>한 번 실행하면 알림 5건이 처리되고, 사람의 승인이 필요한 건은 멈추고, 무엇을 했는지 기록이 남습니다.</mark>

이번 Unit은 실습 1-1과 실습 1-2로 이루어져 있고, <mark>깃허브에 올리는 일은 실습 1-2 마지막에 합니다.</mark> 실습마다 문제는 하나입니다.

- 오늘 쓰는 도구는 **파이썬 · VS Code · 터미널 · git** 입니다. 판다스와 Gemini API 는 쓰지 않으므로 호출 한도(1분에 15번)는 신경 쓰지 않아도 됩니다.
- 오늘 새로 배우는 문법은 없습니다. 지금까지 쓴 문법(딕셔너리 · 리스트 · `in` · `not in` · `if` · `for` · `append` · `json`)을 다시 씁니다.
- 새로 나오는 용어가 많은 날입니다. <mark>처음 나올 때 한 번씩 풀어 쓰고, 문제를 풀 때는 1.2 와 2.1 의 표를 보면서 풉니다.</mark>
- 보고서에서 [핵심 질문]이 붙은 질문은 이 실습에서 꼭 알아야 할 핵심 질문이고, <mark>내 출력이나 샘플 데이터의 값을 근거로 이유까지 서술합니다</mark>.

 **오늘 불러 쓰는 이전 파일**: 없습니다. 오늘 쓰는 데이터(`incident_samples.json`)는 Module 4의 점수 파일과 같은 내용입니다. 이 내용을 아래에 예시 데이터로 적어 두었으니 붙여 넣어 만듭니다. 그래서 Module 4 파일이 없어도 그대로 따라 할 수 있습니다. 실습 1-2는 실습 1-1에서 만드는 `config/playbook_registry.json` 을 읽습니다(없으면 실습 1-1 의 「정답」 레슨 완성본으로 만듭니다).

## 폴더 열고 파일 준비하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 지금 위치를 확인합니다. <mark>`pwd` 결과가 `…/security-agent-toolkit` 으로 끝나고, `ls` 결과에 `anomaly_detection` 폴더가 보이면</mark> 됩니다. 결과가 다르면 `security-agent-toolkit` 폴더에서 터미널을 새로 엽니다.
   ```bash
   pwd
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
3. **[터미널]** Module 5 폴더를 만들고 그 안으로 들어갑니다. Module 5의 모든 파일은 <mark>`soar_response` 폴더 안</mark>에 둡니다. 폴더 이름은 강의계획서가 정한 이름 그대로입니다.
   ```bash
   mkdir soar_response
   cd soar_response
   mkdir config
   ls
   ```
   - 명령 풀이: `mkdir 폴더이름` 새 폴더 만들기 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 이름 보기
   - <mark>`config` 폴더가 보이면</mark> 됩니다. `config` 에는 JSON 설정 파일만 둡니다.
4. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 확장자까지 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서**(`report_u1.md`)도 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
5. **[VS Code]** 오늘 쓸 파일 두 개 `incident_samples.json` · `system_state.json` 을 `soar_response` 폴더에 만들고, 아래 각 파일의 코드 상자 내용을 그대로 붙여 넣습니다. 폴더는 이렇게 됩니다. 나머지 파일은 실습 때 만듭니다.
   ```
   soar_response/
     config/
       playbook_registry.json   실습 1-1에서 만듦
     incident_samples.json      지금 만듦
     system_state.json          지금 만듦
     incident.py                실습 1-2에서 만듦
     playbook_runner.py         실습 1-2에서 만듦
     exercise1-2_run.py         실습 1-2에서 만듦
     report_u1.md               「보고서 쓰기」에서 만듦
   ```

**`incident_samples.json`** — 오늘 처리할 알림 5건의 목록입니다.

- **무엇인가**:
  - Module 4에서 저장한 대상별 점수 기록 5건에 인시던트 번호(`id`)와 처음 상태(`status`)를 붙인 것입니다.
  - **인시던트**(incident, 인시던트): 알림 가운데 사람이 확인하고 대응해야 하는 일 한 건입니다. 예를 들어 「퇴사한 `dami` 의 계정으로 서버에 요청이 왔다」는 알림에 `INC-001` 이라는 번호를 붙이면 인시던트 한 건이 되고, 대응이 끝날 때까지 이 번호로 추적합니다. 알림과 어떻게 다른지는 실습 1-1 읽을거리의 「인시던트는 무엇인가」에서 자세히 설명합니다.
  - `entity` 는 점수를 매긴 대상(사용자 또는 IP), `grade` 는 등급, `reasons` 는 탐지된 규칙 이름입니다. <mark>처음 상태는 모두 `탐지됨` 입니다.</mark>
- **어디에 쓰나**:
  - 실습 1-1: 어떤 알림을 처리할지 볼 때 읽습니다.
  - 실습 1-2: 실행기(`playbook_runner.py`)가 이 파일을 읽어 알림을 하나씩 처리합니다.

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
  - 실습 1-1: 알림 두 건을 수동 처리하면서 VS Code 로 이 파일을 열어 값을 직접 입력하고 저장합니다.
  - 실습 1-2: 실행기가 대응 결과를 이 파일에 새로 저장합니다. 실행하면 직접 입력한 내용은 덮어씁니다.

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

## 목표: 보강·분기·안전장치

<!-- REVIEW: 옛 Unit 1 시작하기에서 가져온 쪽입니다. 새 Unit 시작하기에 맞게 합치거나 지우세요 -->

이번 Unit은 SOAR 자동 대응의 판단 단계를 구현합니다. 실습 1-3은 알림 보강(enrichment, 인리치먼트: 판단에 필요한 정보를 알림에 추가하는 일)을 다룹니다. 도전 1-1는 맥락에 따른 조건 분기(branching, 브랜칭: 조건에 따라 처리 경로를 나누는 일)를 다룹니다. 도전 1-2은 안전장치(guardrail, 가드레일: 자동 대응이 잘못 실행되어도 피해가 커지지 않도록 미리 두는 점검과 제한)를 다룹니다.

깃허브 업로드는 Unit 2의 도전 2-2 마지막에 합니다. 새 문법은 도전 1-1의 **튜플 리턴과 언패킹**(두 값을 한 번에 리턴하고 한 번에 받는 문법)과 도전 1-2의 **`startswith`**(문자열이 지정한 문자열로 시작하는지 확인하는 메서드) 둘입니다. 보고서에서 [핵심 질문]이 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 들여쓰기는 미리 채운 줄에 맞춥니다. 각 번호 주석 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

 **이전 파일**: Unit 1에서 만든 `incident.py` · `playbook_runner.py` · `incident_samples.json` · `config/playbook_registry.json` 을 씁니다. 없는 파일은 Unit 1의 코드 상자로 만듭니다(`incident_samples.json` 은 Unit 1 「시작하기」, `config/playbook_registry.json` 은 실습 1-1, `incident.py` · `playbook_runner.py` 는 실습 1-2 레슨).

## Unit 1 파일 확인하고 데이터 파일 만들기

<!-- REVIEW: 옛 Unit 1 시작하기에서 가져온 쪽입니다. 새 Unit 시작하기에 맞게 합치거나 지우세요 -->

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** Module 5 폴더로 들어가 Unit 1 파일을 확인합니다. <mark>`ls` 결과에 `config` · `incident.py` · `incident_samples.json` · `playbook_runner.py` 가 보이면</mark> 됩니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. **[VS Code]** 왼쪽 목록에서 `soar_response` 폴더를 오른쪽 클릭 › **New File** 을 누르고, **파일 이름을 확장자까지 그대로** 적고 Enter 를 친 뒤, 내용을 붙여 넣고 `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다. 답을 적는 보고서(`report_u1.md`)는 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
4. **[VS Code]** 데이터 파일 세 개 `users_info.json` · `source_ips.json` · `trusted_ips.json` 을 `soar_response` 폴더에 만들고, 아래 각 파일의 코드 상자 내용을 붙여 넣습니다.

**`users_info.json`** — 계정 이름별 재직 여부(`employed`)와 VIP 계정(VIP account, 브이아이피 계정: 잠기면 업무에 미치는 영향이 큰 중요도가 높은 계정) 여부(`vip`)를 기록한 파일입니다. `true` 는 「그렇다」, `false` 는 「아니다」입니다. 실제 조직에서는 인사 시스템과 IAM(Identity and Access Management, 아이덴티티 앤 액세스 매니지먼트: 계정과 접근 권한을 관리하는 체계)이 보유한 정보이고, 오늘은 파일로 대신합니다. `dami` 는 퇴사자(`employed` 가 `false`), `gaeun` 은 VIP 계정(`vip` 가 `true`)입니다. 실습 1-3 ~ 도전 1-2에서 읽어 사용합니다.

```
{
  "dami": {"employed": false, "vip": false},
  "seoyeon": {"employed": true, "vip": false},
  "gaeun": {"employed": true, "vip": true},
  "jiwoo": {"employed": true, "vip": false},
  "junho": {"employed": true, "vip": false},
  "hana": {"employed": true, "vip": false}
}
```

**`source_ips.json`** — 사용자 이름별로 로그인에 사용한 접속 IP(source IP, 소스 아이피: 로그인 요청이 출발한 출발지 IP)를 기록한 파일입니다. 이 파일에 이름이 없는 사용자는 접속 IP 기록이 없는 사용자입니다. 실습 1-3에서 읽습니다.

```
{
  "seoyeon": "203.0.113.80",
  "jiwoo": "203.0.113.80",
  "gaeun": "198.51.100.77",
  "junho": "192.0.2.41"
}
```

**`trusted_ips.json`** — **신뢰 IP**(trusted IP, 트러스티드 아이피: 정상 접속의 출처로 사전에 확인해 등록한 IP) 목록입니다. 협력사 사무실 IP 한 개가 등록되어 있고, `seoyeon` 과 `jiwoo` 가 이 IP 에서 접속합니다. 실습 1-3에서 읽습니다.

```
[
  "203.0.113.80"
]
```

5. **[터미널]** 두 가지를 확인합니다. 먼저 데이터 파일입니다. <mark>`6 4 1` 이 나와야</mark> 합니다.
   ```bash
   python -c "import json; print(len(json.load(open('users_info.json', encoding='utf-8'))), len(json.load(open('source_ips.json', encoding='utf-8'))), len(json.load(open('trusted_ips.json', encoding='utf-8'))))"
   ```
6. **[터미널]** Unit 1에서 만든 플레이북(playbook, 플레이북: 알림 유형별 대응 절차를 사전에 정의한 문서)의 등록 값을 점검합니다. 오늘 출력이 문서와 일치하려면 이 값이 <mark>아래 출력과 같아야</mark> 합니다. 다르면 `config/playbook_registry.json` 을 열어 해당 값을 같게 고칩니다(Unit 1에서 만든 내 파일은 깃허브에 올라가 있습니다).
   ```bash
   python -c "import json; print([(p['id'], p['trigger_rule'], p['min_grade'], p['approval']) for p in json.load(open('config/playbook_registry.json', encoding='utf-8'))])"
   ```
   ```
   [('PB-001', '퇴사한 계정', 'high', '자동'), ('PB-002', '대량 다운로드', 'mid', '담당자 승인 필요'), ('PB-003', '경로 스캔', 'low', '담당자 승인 필요')]
   ```

## 오류가 나면

<!-- REVIEW: 옛 Unit 1 시작하기에서 가져온 쪽입니다. 새 Unit 시작하기에 맞게 합치거나 지우세요 -->

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError: No module named 'incident'` 는 <mark>Unit 1에서 만든 `incident.py` 가 이 폴더에 없다는 뜻</mark>입니다. Unit 1 실습 1-2 레슨의 `incident.py` 코드 상자로 만듭니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다.

---
