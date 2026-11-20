---
id: m5-u01-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표와 전체 지도

이번 Unit 1로 Module 5 **자동 대응**을 시작합니다. Module 4에서는 로그를 읽어 **위험한 대상을 찾아 점수와 등급을 매겼습니다.** Module 5는 그 **알림이 난 뒤에 하는 일**을 다룹니다. 계정을 잠그고, **티켓**(ticket, 티켓: 처리할 일 한 건을 적어 두고 누가 맡았는지와 처리됐는지를 추적하는 기록)을 만들고, 담당자에게 알리는 일을 정해 둔 절차대로 프로그램이 실행하게 만듭니다. 회사는 이번에도 **A사**입니다.

**오늘의 계획 (3시간)**

1. 시작하기 15분: 이 레슨을 읽고 작업 폴더와 데이터 파일을 만듭니다.
2. 실습 약 110분: 핵심 실습 세 개를 차례로 합니다. 실습 1-3 앞에서 「제공 파일」 두 개를 복사해 만듭니다.
3. 글쓰기 40분: 「보고서 쓰기」 레슨에서 핵심 실습의 질문에 답하고, 「오늘의 글 쓰기」 레슨에서 글 한 편을 씁니다.
4. 마무리 15분: 실습 1-3 끝의 「이번 Unit 마무리」에서 파일을 확인하고 깃허브에 올립니다.

**오늘 만들 것 세 가지**

1. **실습 1-1**: **플레이북**(playbook, 플레이북: 「이런 알림이 오면 이렇게 대응한다」를 미리 적어 둔 대응 절차서) 한 건을 직접 쓰고, 알림 두 건을 프로그램 없이 손으로 처리해 봅니다.
2. **실습 1-2**: 같은 일을 프로그램(`playbook_runner.py`)이 하게 만듭니다. 한 번 실행하면 알림 5건이 처리되고, 사람의 승인이 필요한 건은 멈추고, 무엇을 했는지 기록이 남습니다.
3. **실습 1-3**: 조치하기 전에 「대상이 누구이고 어디에서 접속했는가」를 알림마다 조회해 붙이는 `enrichment.py` 를 만듭니다.

**도전 1-1 · 1-2는 선택입니다.** 핵심 실습 세 개와 글쓰기를 마치고 시간이 남을 때 합니다. 도전에서 직접 쓰는 `routing.py` · `safe_runner.py` 는 「제공 파일」에서 완성본으로 미리 만들어 두므로, 도전을 하지 않아도 다음 Unit을 따라갈 수 있습니다.

**Module 5 전체 지도** — 알림이 오면 보안 담당자는 알림을 분류하고, 조치하고, 기록을 남기고, 잘못된 조치를 되돌립니다. Module 5에서는 이 일을 다섯 단계로 나눠 코드로 자동화합니다.

1. **플레이북으로 알림 처리하기 (Unit 1)**: 대응 절차를 플레이북 파일에 적고, 실행기가 알림 5건을 처리하며 감사 기록을 남깁니다. 조치 전에 알림에 맥락 정보를 붙입니다.
2. **계정 잠그고 세션 끊기 (Unit 2)**: 계정 잠금과 세션 종료를 실행한 뒤 정말 바뀌었는지 다시 확인하고, 조치 전 · 후 상태를 기록합니다.
3. **되돌리고 티켓 남기기 (Unit 3)**: 오탐으로 확인된 알림의 자동 조치를 되돌리고, 티켓을 만들어 응답 기한을 계산합니다.
4. **승인 게이트와 오탐 되돌리기 (Unit 4)**: 위험 점수로 조치 요청을 자동 실행 · 승인 필요로 나누고, 오탐 신고가 오면 조치를 되돌립니다.
5. **통합 엔진과 최종 회고 (Unit 5)**: 지금까지 만든 것을 엔진 하나로 이어 실행하고, 정책을 지켰는지 점검해 회고 문서를 씁니다.

- 오늘 쓰는 도구는 **파이썬 · VS Code · 터미널 · git** 입니다. 판다스와 Gemini API 는 쓰지 않습니다.
- 핵심 실습은 지금까지 쓴 문법(딕셔너리 · 리스트 · `in` · `not in` · `if` · `for` · `append` · `json`)만 씁니다. 도전 1-1에는 **튜플 리턴과 언패킹**, 도전 1-2에는 **`startswith`** 가 새로 나옵니다.
- 새로 나오는 용어가 많은 날입니다. 처음 나올 때 한 번씩 풀어 쓰니, 문제를 풀 때는 실습 1-1의 1.2 표와 실습 1-2의 2.1 표를 보면서 풉니다.

## Module 4 결과와 오늘 쓰는 알림

오늘 처리할 알림 5건은 **Module 4 Unit 4 「위험 점수 매기고 오탐 줄이기」의 실습 4-1**에서 저장한 점수 파일 `unit05_risk_scores.json` 의 내용과 같습니다. 그 파일에는 대상별 점수 기록 5건(대상 · 점수 · 등급 · 이유)이 들어 있습니다.

| Module 4 점수 파일의 키 | 뜻 | 예 (`dami`) |
|---|---|---|
| `entity` | 점수를 매긴 대상(사용자 이름 또는 IP) | `"dami"` |
| `score` | 탐지된 규칙의 점수를 더한 값 | `60` |
| `grade` | 점수로 정한 등급(`high` · `mid` · `low`) | `"high"` |
| `reasons` | 탐지된 규칙 이름의 리스트 | `["퇴사한 계정"]` |

오늘은 이 기록 한 건마다 두 가지를 더 붙여 `incident_samples.json` 으로 씁니다.

1. `id`: `INC-001` 같은 인시던트 번호입니다. **인시던트**(incident, 인시던트)는 알림 가운데 사람이 확인하고 대응해야 하는 일 한 건입니다. 번호를 붙이면 대응이 끝날 때까지 이 번호로 추적합니다(실습 1-1에서 자세히 설명합니다).
2. `status`: 처리 상태입니다. 처음 상태는 모두 `탐지됨` 입니다.

- **Module 4 파일이 없어도 됩니다.** 다음 페이지에 `incident_samples.json` 의 내용을 그대로 적어 두었으니 붙여 넣어 만듭니다. Module 4 폴더(`anomaly_detection`)의 파일은 오늘 불러 쓰지 않습니다.
- 내 `unit05_risk_scores.json` 과 비교해 보고 싶으면 VS Code 에서 `anomaly_detection/unit05_risk_scores.json` 을 열어 봅니다. 대상 5개와 점수(60 · 45 · 40 · 35 · 30)가 같으면 됩니다.

## 폴더 열고 파일 준비하기

1. **[VS Code]** 프로젝트 폴더 `security-agent-toolkit` 을 열고, 왼쪽 목록에서 그 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 지금 위치를 확인합니다. <mark>`pwd` 결과가 `…/security-agent-toolkit` 으로 끝나면</mark> 됩니다. 결과가 다르면 `security-agent-toolkit` 폴더에서 터미널을 새로 엽니다.
   ```bash
   pwd
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인
3. **[터미널]** Module 5의 작업 폴더 `soar_response` 와 그 안의 설정 폴더 `config` 를 만들고, `soar_response` 폴더로 들어갑니다. Module 5의 파일은 모두 이 폴더에 둡니다.
   ```bash
   mkdir -p soar_response/config
   cd soar_response
   pwd
   ```
   - `mkdir -p` 는 폴더를 만들고(이미 있어도 오류 없음), 마지막 `pwd` 가 `…/security-agent-toolkit/soar_response` 로 끝나면 됩니다. `config` 에는 JSON 설정 파일만 둡니다.
4. **파일은 이렇게 만듭니다.** 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 확장자까지 그대로** 적고 Enter 를 칩니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서**(`report_u1.md`)는 「보고서 쓰기」 레슨의 틀을 복사해 만듭니다.
5. **[VS Code]** 오늘 쓸 데이터 파일 다섯 개를 `soar_response` 폴더에 만들고, 아래 각 파일의 코드 상자 내용을 그대로 붙여 넣습니다. 폴더는 이렇게 됩니다. 나머지 파일은 실습 때 만듭니다.
   ```
   soar_response/
     config/
       playbook_registry.json   실습 1-1에서 만듦
     incident_samples.json      지금 만듦
     system_state.json          지금 만듦
     users_info.json            지금 만듦
     source_ips.json            지금 만듦
     trusted_ips.json           지금 만듦
   ```

**`incident_samples.json`** — 오늘 처리할 알림 5건입니다. 앞 페이지의 점수 기록 5건에 `id` 와 `status` 를 붙였습니다. 실습 1-2의 실행기와 실습 1-3의 보강 프로그램이 이 파일을 읽습니다.

<pre class="copyable"><code>[
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
</code></pre>

**`system_state.json`** — 연습용 시스템(실제 서버와 계정 대신 파일로 흉내 낸 시스템)의 상태입니다. 잠긴 계정(`locked_users`) · 차단한 IP(`blocked_ips`) · 티켓(`tickets`) · 담당자 알림(`notifications`) 네 가지를 적고, 처음에는 모두 비어 있습니다. 실습 1-1에서는 이 파일을 직접 고치고, 실습 1-2에서는 실행기가 결과를 덮어써 저장합니다.

<pre class="copyable"><code>{
  "locked_users": [],
  "blocked_ips": [],
  "tickets": [],
  "notifications": []
}
</code></pre>

**`users_info.json`** — 계정 이름별 재직 여부(`employed`)와 **VIP 계정**(VIP account, 브이아이피 계정: 잠기면 업무에 미치는 영향이 큰 중요한 계정) 여부(`vip`)입니다. `true` 는 「그렇다」, `false` 는 「아니다」입니다. 실제 조직에서는 인사 시스템과 IAM(Identity and Access Management, 아이덴티티 앤 액세스 매니지먼트: 계정과 접근 권한을 관리하는 체계)이 가진 정보이고, 오늘은 파일로 대신합니다. `dami` 는 퇴사자, `gaeun` 은 VIP 계정입니다. 실습 1-3에서 읽습니다.

<pre class="copyable"><code>{
  "dami": {"employed": false, "vip": false},
  "seoyeon": {"employed": true, "vip": false},
  "gaeun": {"employed": true, "vip": true},
  "jiwoo": {"employed": true, "vip": false},
  "junho": {"employed": true, "vip": false},
  "hana": {"employed": true, "vip": false}
}
</code></pre>

**`source_ips.json`** — 사용자 이름별로 로그인에 쓴 접속 IP(source IP, 소스 아이피: 로그인 요청이 출발한 IP)입니다. 이 파일에 이름이 없는 사용자는 접속 IP 기록이 없는 사용자입니다. 실습 1-3에서 읽습니다.

<pre class="copyable"><code>{
  "seoyeon": "203.0.113.80",
  "jiwoo": "203.0.113.80",
  "gaeun": "198.51.100.77",
  "junho": "192.0.2.41"
}
</code></pre>

**`trusted_ips.json`** — **신뢰 IP**(trusted IP, 트러스티드 아이피: 정상 접속의 출처로 미리 확인해 등록한 IP) 목록입니다. 협력사 사무실 IP 한 개가 있고, `seoyeon` 과 `jiwoo` 가 이 IP 에서 접속합니다. 실습 1-3에서 읽습니다.

<pre class="copyable"><code>[
  "203.0.113.80"
]
</code></pre>

6. **[터미널]** 파일이 정상인지 확인합니다. <mark>`5 6 4 1` 이 나와야</mark> 합니다. 다르면 붙여 넣은 내용이나 파일 위치(`soar_response` 폴더 안인지)를 다시 확인합니다(맥북은 `python3`).
   ```bash
   python -c "import json; print(*[len(json.load(open(f, encoding='utf-8'))) for f in ['incident_samples.json', 'users_info.json', 'source_ips.json', 'trusted_ips.json']])"
   ```
   - 명령 풀이: 네 파일을 차례로 읽어 각각 몇 건인지(알림 5건 · 계정 6명 · 접속 IP 4개 · 신뢰 IP 1개) 한 줄로 출력합니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다. 각 실습은 **「할 일」을 위에서부터 차례로** 따라 하고, 코드를 채울 때는 코드 안 `#` 설명이 시키는 일을 합니다. 막히면 이 Unit 뒤쪽의 정답을 봅니다.

## 오류가 나면

- 먼저 `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `FileNotFoundError` 가 나오면 <mark>파일이 `soar_response` 폴더 바로 아래(또는 `config` 폴더 안)에 있는지</mark> `ls` 로 봅니다. `config/playbook_registry.json` 은 `config` 폴더 안에 있어야 합니다.
- `json.decoder.JSONDecodeError` 가 나오면 <mark>JSON 파일의 쉼표나 대괄호 · 중괄호가 빠졌거나 남은 것</mark>입니다. 오류에 적힌 줄 번호의 앞뒤 줄을 봅니다.
- `python` 이 없다는 오류가 나오면 `python3` 으로 칩니다(맥북은 `python3`).
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 이 Unit 뒤쪽의 정답을 보고, 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.
