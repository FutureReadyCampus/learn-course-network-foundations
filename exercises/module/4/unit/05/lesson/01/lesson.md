---
id: m4-u05-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표: AI 요약과 pipeline.py

Unit 4까지 이상탐지 규칙을 만들고, 알림이 맞았는지 세고, 틀린 알림을 줄였습니다. 이번 Unit에서는 <mark>**Unit 3 · 7에서 만든 탐지를 한 번에 실행해 보고서 파일 하나로 남기고**</mark>, Module 4에서 만난 상황을 정리합니다. Module 4의 마지막 Unit입니다.

- **실습 5-1**: Unit 4에서 저장한 대상별 점수 파일에서 먼저 확인할 대상을 고르고, **AI** 에게 파일에 있는 사실만으로 짧은 요약문을 쓰게 합니다(`event_summary.py`).
- **도전 5-3**: 이벤트 읽기 → 연결 · 탐지 · 점수 → Gemini API 를 활용한 AI 요약 → 보고서 저장을 **`pipeline.py`**(pipeline, 파이프라인: 여러 단계를 순서대로 이어 한 번에 실행하는 프로그램) 하나로 실행합니다.
- **실습 5-2**: **Module 4 총정리.** 새로 배우는 것 없이, 상황 8개의 원인과 고치는 방법을 내 말로 정리하고 이번 Unit의 작업을 깃허브에 올립니다.

Unit 5은 실습 5-1 · 10-2 · 10-3으로 이루어져 있고, 다음 Unit부터는 Module 5(자동 대응)을 시작합니다. <mark>깃허브에 올리는 일은 실습 5-2 마지막에 합니다.</mark> 실습마다 문제는 하나입니다.

- 이번 Unit에서 쓰는 도구는 **파이썬 · 판다스 · VS Code · 터미널 · git** 이고, 실습 5-1 · 10-2에는 **LLM 호출 함수**(`llm_client.py` 의 `call_llm`)를 씁니다.
  - 이 페이지에서 말하는 **AI** 는 구글의 **Gemini API** 입니다.
  - `call_llm` 이 Gemini API 에 글을 보내고 답을 받아 옵니다.
- 이번 Unit에서 새로 배우는 문법은 실습 5-1의 문자열 이어 붙이기 `"구분 글자".join(리스트)` 와 도전 5-3의 `Series.to_dict()` 두 개입니다. 나머지는 앞에서 쓴 문법(f-문자열 · `if` · `and` · 딕셔너리 · `value_counts()` · `json.dump`)을 다시 씁니다.
- <mark>AI 가 쓰는 요약 문장은 실행할 때마다 조금씩 달라집니다.</mark> 이 페이지의 출력 예와 문장이 달라도 정상입니다. 점수와 등급과 건수는 같아야 합니다.
- [주의] <mark style="background:#ffc4d6">**무료 Gemini 키는 1분에 15번까지만 호출할 수 있습니다.**</mark> 이번 Unit에서는 실습 5-1 실행에 3번, 도전 5-3 실행마다 3번 호출합니다. `[LLM 호출 실패] 상태 코드 429` 가 나오면 <mark>1분 기다린 뒤 다시 실행</mark>합니다. 실패해도 이 프로그램은 멈추지 않도록 만듭니다.
- [주의] <mark>앞 Unit(특히 Unit 4)의 파일이 없는 사람은 아래 표를 보고, 없는 파일만 표의 안내대로 앞 Unit의 코드 상자에서 복사해 만듭니다.</mark> 이미 다 가진 사람은 건너뜁니다.
- 보고서에서 `[핵심 질문]` 표시가 붙은 질문은 이 실습에서 꼭 알아야 할 핵심 질문이고, <mark>내 출력이나 샘플 데이터의 값을 근거로 이유까지 씁니다</mark>.
- 점수 기준(high 60 이상 · mid 35 이상)과 AI 에게 요약시킬 대상 수(3명)는 **고정**하고, <mark>값을 바꿔 가며 비교하지 않습니다</mark>.

**이번 Unit에서 불러 쓰는 이전 파일**이 있습니다. 아래 표에서 <mark>`event_summary.py` 만 이번 Unit의 실습 5-1에서 만들고, 나머지는 모두 앞 Unit에서 만들었거나 `agent_core` 폴더에서 가져오는 파일</mark>입니다. <mark>없는 파일은 표의 안내대로 앞 Unit의 코드 상자에서 복사해 만듭니다.</mark> 이미 다 가진 사람은 건너뜁니다.

| 파일 | 만든 곳 | 쓰는 곳 | 없거나 완성하지 못했을 때 |
|---|---|---|---|
| `llm_client.py` · `.env`(API 키) | `agent_core` 폴더와 `security-agent-toolkit` 폴더 | 실습 5-1 · 10-2 | 아래 시작하기 3번의 `cp` 명령으로 복사합니다. `agent_core` 에도 없으면 `agent_core` 를 만든 앞 Module 의 실습에서 먼저 만듭니다 |
| `unit05_risk_scores.json` | Unit 4의 실습 4-1 | 실습 5-1이 읽습니다 | 아래 시작하기 5번의 내용으로 파일을 만듭니다(항상 이 내용으로 덮어씁니다) |
| `normalized_events.json` · `rbac.py` · `config/users.json` · `config/roles.json` | Unit 3 「시작하기」 6번 | 도전 5-3 | Unit 3 「시작하기」 레슨 6번의 코드 상자로 파일을 만듭니다 |
| `access_detection.py` · `saas_detection.py` · `malicious_detection.py` | Unit 3의 실습 3-2 · 6-2 · 6-3 | 도전 5-3 | Unit 4 「정답」 레슨 맨 아래 「부록 · Unit 3 파일 완성본」의 코드 상자로 파일을 만듭니다 |
| `correlation.py` · `risk_scores.py` | Unit 4의 도전 4-1 · 7-2 | 도전 5-3 | Unit 4 도전 4-1 · 7-2 레슨의 코드 상자를 붙여 넣고, 「정답」 레슨의 「채운 코드」를 빈칸 자리에 넣어 파일을 완성합니다 |
| `event_summary.py` | 실습 5-1 | 도전 5-3 `pipeline.py` 가 불러옵니다 | 이 Unit 실습 5-1 레슨의 코드 칸에 「실습 5-1 정답」의 「채운 코드」를 넣어 완성합니다 |

## 폴더 열고 LLM 호출 파일 준비하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치와 앞 Unit의 파일을 확인합니다(맥북은 `python3`). <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, `ls` 결과에 위 표의 Unit 3 · 7 파일들이 보여야</mark> 합니다. 없는 파일이 있으면 위 표의 안내대로 만든 뒤 `ls` 를 다시 칩니다. <mark>자리를 바꾼 사람은 3번 전에 아래 「.env 와 API 키 다시 받기」를 먼저 합니다.</mark>
   ```bash
   cd anomaly_detection
   pwd
   ls
   ```
   - 명령 풀이: `cd 폴더이름` 그 폴더로 이동 · `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기
3. **[터미널]** `agent_core` 폴더의 LLM 호출 파일을 이 폴더로 복사하고, API 키를 읽을 수 있는지 확인합니다. <mark>마지막 명령에서 `True` 가 나오면</mark> 됩니다. 키 값은 화면에 나오지 않습니다.
   ```bash
   cp ../agent_core/llm_client.py .
   ls llm_client.py
   python -c "from llm_client import read_api_key; print(read_api_key() is not None)"
   ```
   - 명령 풀이: `cp 원본 대상` 파일 복사(`..` 은 한 단계 위 폴더, `.` 은 지금 폴더) · `ls 파일이름` 그 파일이 있는지 확인
4. **파일은 이렇게 만듭니다.** 이 페이지에 나오는 파일은 모두 이 페이지의 코드 상자에서 복사해 만들고, 따로 내려받는 파일은 없습니다. 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
   - 답을 적는 **보고서**(`report_u5.md`)도 이 Unit의 「보고서 쓰기」 레슨에서 복사해 만듭니다.
5. **[VS Code]** `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 로 `unit05_risk_scores.json` 을 만들고 아래 내용을 그대로 붙여 넣습니다. <mark>같은 이름의 파일이 이미 있으면 아래 내용으로 덮어씁니다</mark>(출력이 문서와 같아야 하기 때문입니다).

**`unit05_risk_scores.json`** — Unit 4에서 저장한 대상별 점수 기록 5건입니다. `entity` 는 점수를 매긴 대상(사용자 또는 IP), `score` 는 점수, `grade` 는 등급, `reasons` 는 탐지된 규칙 이름입니다. 점수가 높은 순서로 저장돼 있습니다.

```
[
  {
    "entity": "dami",
    "score": 60,
    "grade": "high",
    "reasons": [
      "퇴사한 계정"
    ]
  },
  {
    "entity": "seoyeon",
    "score": 45,
    "grade": "mid",
    "reasons": [
      "평소와 다른 IP",
      "대량 다운로드"
    ]
  },
  {
    "entity": "gaeun",
    "score": 40,
    "grade": "mid",
    "reasons": [
      "규칙은 허용인데 서버가 거절",
      "여러 로그 연결"
    ]
  },
  {
    "entity": "jiwoo",
    "score": 35,
    "grade": "mid",
    "reasons": [
      "업무 시간 밖 로그인",
      "평소와 다른 IP"
    ]
  },
  {
    "entity": "198.51.100.90",
    "score": 30,
    "grade": "low",
    "reasons": [
      "경로 스캔"
    ]
  }
]
```

6. **[터미널]** 파일이 정상인지 확인합니다. <mark>`5` 가 나오고, 아래 두 줄에서 오류가 나오지 않으면</mark> 됩니다. 오류가 나면 그 줄의 파일이 없거나 이름이 다른 것이니 위 표의 안내대로 만듭니다.
   ```bash
   python -c "import json; print(len(json.load(open('unit05_risk_scores.json', encoding='utf-8'))))"
   python -c "from access_detection import load_events, EVENTS_PATH; from saas_detection import pick_saas; from malicious_detection import pick_web_failures"
   python -c "from correlation import find_chains_in_events; from risk_scores import collect_findings, save_records"
   ```

## API 키와 .env 다시 받기 (필요한 사람만)

처음부터 새로 받는 방법입니다. 키를 만들고, 키가 맞는지 확인하고, `.env` 파일에 넣고, 깃허브에 올라가지 않게 막은 뒤, 마지막으로 읽히는지 봅니다.

- **왜 다시 받나**:
  - API 키는 `.env` 파일에 들어 있고, 이 파일은 PC 마다 따로 있습니다.
  - `.env` 는 깃허브에 올리지 않으므로 다른 PC 로 따라오지 않습니다.
  - 자리를 바꾼 PC 에는 `.env` 가 없어서 이번 Unit의 실습 5-1 · 10-2에서 AI 호출이 되지 않습니다.
- **먼저 확인하기**: <mark>이미 `.env` 가 있으면 이 절은 건너뜁니다.</mark>
  - **[터미널]** `anomaly_detection` 폴더에서 한 단계 위 폴더의 파일을 숨김 파일까지 봅니다.
    ```bash
    ls -a ..
    ```
  - 명령 풀이: `ls -a` 숨김 파일(이름이 점으로 시작하는 파일)까지 보기 · `..` 한 단계 위 폴더(`security-agent-toolkit`)
  - 나오는 것: 목록에 <mark>`.env` 와 `.gitignore` 가 둘 다 보이면</mark> 됩니다. 하나라도 없으면 아래를 합니다.

**1단계 · 구글 AI Studio 에서 새 키 만들기**

- **[브라우저]** `https://aistudio.google.com` 에 들어갑니다. 바로 키 화면으로 가려면 `https://aistudio.google.com/app/apikey` 를 씁니다.
- **로그인**: 개인 gmail 계정으로 로그인합니다. 학교나 회사 계정은 관리자가 막아 두었을 수 있습니다. 처음이면 약관 동의 화면이 나오고 **동의**를 누릅니다.
- **키 만들기**: 왼쪽 메뉴의 **Get API key** 를 누르고, **Create API key** 를 누릅니다.
  - 이미 만든 키가 있는 사람도 새 키를 만들어도 됩니다.
  - 프로젝트(구글이 키를 묶어 두는 이름)를 고르거나 만들라는 창이 나오면, 제안하는 기본 프로젝트를 고르거나 새로 만들고 계속합니다.
- **키 복사**: 목록에 새 키가 나오면 복사 단추를 눌러 복사합니다. 영문자와 숫자가 섞인 긴 글자이고, 보통 `AIza` 로 시작합니다. <mark>복사한 글자 앞뒤에 빈칸이 끼지 않게</mark> 합니다.
- <mark style="background:#ffc4d6">카드 번호나 결제 정보는 넣지 않습니다.</mark> 결제를 요구하는 화면이 나오면 닫습니다.
- 화면의 글자는 구글이 바꿀 수 있습니다. 이름이 조금 달라도 「API 키를 만든다」는 뜻의 단추를 찾으면 됩니다.
- 「접속할 수 없다」는 화면이 나오면 구글 계정에 생년월일이 등록되어 있는지(`https://myaccount.google.com` › 개인 정보) 확인합니다.

**2단계 · 키가 맞는지 먼저 확인하기**

- **[터미널]** 아래 명령의 `여기에_내_키` 를 복사한 키로 바꿔서 칩니다. 키는 따옴표 안에 그대로 붙여 넣습니다. 화면을 공유하는 중이면 하지 않습니다.
  ```bash
  curl -H "x-goog-api-key: 여기에_내_키" "https://generativelanguage.googleapis.com/v1beta/models"
  ```
  - 명령 풀이: `curl 주소` 주소로 요청을 보내 답을 받아 오기 · `-H "이름: 값"` 요청에 붙이는 머리글(여기서는 키)
- 나오는 것: <mark>`"models"` 로 시작하는 긴 목록이 나오면</mark> 키가 맞습니다. 키의 마지막 글자를 하나 지우고 치면 `UNAUTHENTICATED` 가 나옵니다. 오류 글자가 나오면 키를 다시 복사합니다.
- 같은 명령을 여러 번 반복하지 않습니다. 호출 횟수에 한도가 있습니다.

**3단계 · `.env` 파일 만들기**

- **[VS Code]** 왼쪽 목록에서 `security-agent-toolkit` 폴더(`anomaly_detection` 의 바깥)를 오른쪽 클릭 › **New File** 을 누르고 `.env` 를, 같은 방법으로 `.gitignore` 를 만듭니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다. 파일 이름 뒤에 `.txt` 같은 것이 붙지 않아야 합니다.
- **[VS Code]** 왼쪽 파일 목록에서 `security-agent-toolkit` 바로 아래의 `.env` 를 열고 아래 한 줄만 적습니다. <mark>등호 앞뒤에 빈칸을 넣지 않고, 따옴표도 넣지 않습니다.</mark>
  ```
  GEMINI_API_KEY=여기에_복사한_키를_붙여넣습니다
  ```
  - 탭 이름 옆에 점(●)이 없으면 저장된 것입니다. 이 한 줄 말고 다른 글자는 넣지 않습니다.

**4단계 · 깃허브에 키가 올라가지 않게 막기**

- **[VS Code]** `security-agent-toolkit` 바로 아래의 `.gitignore` 를 엽니다. 맨 아래에 `.env` 한 줄이 있는지 보고, 없으면 적습니다.
  ```
  .env
  ```
- **[터미널]** 막혔는지 확인합니다. <mark>목록에 `.env` 가 보이지 않으면</mark> 막힌 것입니다.
  ```bash
  git status
  ```
  - 나오는 것: 바뀐 파일 목록에 `.env` 가 있으면 아직 막히지 않은 것입니다. `.gitignore` 의 `.env` 줄이 맞는지 다시 봅니다. 깃허브에 올리기 전에는 항상 이 확인을 합니다.

**5단계 · 이번 Unit에서 쓸 폴더에서 읽히는지 확인하기**

- **[터미널]** `anomaly_detection` 폴더로 돌아와 시작하기 3번의 마지막 명령을 칩니다. <mark>`True` 가 나오면</mark> 됩니다. 키 값은 화면에 나오지 않습니다.
  ```bash
  cd anomaly_detection
  pwd
  python -c "from llm_client import read_api_key; print(read_api_key() is not None)"
  ```
  - 명령 풀이: `python -c "코드"` 적은 코드를 바로 실행(맥북은 `python3`)

**막혔을 때**

- `.env.txt` 처럼 이름이 다르게 만들어졌다면, `security-agent-toolkit` 폴더에서 `mv .env.txt .env` 를 칩니다(`mv 이전이름 새이름` 은 이름 바꾸기).
- `False` 가 나오면 `.env` 를 `anomaly_detection` 폴더 안에 만들었거나, `GEMINI_API_KEY=` 글자가 틀렸거나, 등호 앞뒤에 빈칸이 있는 것입니다. 3단계를 다시 봅니다.
- 키가 맞는데(2단계는 성공) 이번 실행에서 `상태 코드 429` 가 1분을 기다려도 계속 나오면, 구글이 그 계정의 무료 호출 한도를 0 으로 둔 경우가 구글 포럼에 보고되어 있습니다. 보고서 (가)에 「막힘: 429 가 계속 나옴」이라고 적고 넘어갑니다. 요약 자리에는 대체 문장이 나오고 프로그램은 멈추지 않습니다.

**키를 다룰 때 지킬 것**

- 단톡방이나 메신저에 키를 올리지 않습니다.
- 화면을 공유할 때 `.env` 를 열어 두지 않습니다.
- 깃허브에 웹으로 파일을 올릴 때 `.env` 를 끌어다 놓지 않습니다. `.gitignore` 는 웹 업로드를 막아 주지 않습니다.
- 키가 노출됐다면 구글 AI Studio 의 키 목록에서 그 키를 삭제하고 새로 만듭니다. 쓰지 않는 예전 키도 같은 곳에서 삭제해 둡니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError: No module named 'llm_client'`(또는 `correlation` · `risk_scores` · `access_detection` 등): <mark>그 파일이 `anomaly_detection` 폴더 바로 아래에 없다는 뜻</mark>입니다. 위 표의 「없거나 완성하지 못했을 때」를 따라 그 파일을 만듭니다.
- `TypeError: expected str, bytes or os.PathLike object, not NoneType`: <mark>`llm_client.py` 가 `.env` 파일을 찾지 못한 것</mark>입니다. 위 「.env 와 API 키 다시 받기」를 따릅니다. API 키는 화면이나 AI 질문에 붙여 넣지 않습니다.
- `ModuleNotFoundError: No module named 'requests'`: 새 PC 의 가상환경에 `requests` 가 없는 것입니다. 가상환경을 활성화한 뒤 `python -m pip install requests` 를 칩니다.
- `[LLM 호출 실패] 상태 코드 429`: 1분에 15번을 넘었다는 뜻입니다. <mark>1분 기다린 뒤 다시 실행</mark>합니다. 요약 자리에 `(요약 실패 — 점수와 이유를 직접 확인)` 이 나와도 이 프로그램이 일부러 그렇게 만든 것이라 정상입니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 맨 아래 「정답」을 보고</mark>, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

---
