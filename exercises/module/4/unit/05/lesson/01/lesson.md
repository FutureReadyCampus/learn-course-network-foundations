---
id: m4-u05-l01
title: 시작하기
render: markdown
---

# 시작하기

## 목표와 오늘의 계획

핵심 실습 전에 [블로그 초안 준비](__SITE__/exercises/module/4/unit/5/lesson/8/page/1)에서 이번 유닛의 글 파일을 엽니다.

Unit 5는 Module 4 **이상탐지**의 마지막 Unit입니다. 지금까지 로그를 같은 모양으로 맞추고(Unit 1), 판다스로 세어 기준을 정하고(Unit 2), 요청 급증과 반복 거절을 찾고(Unit 3), 대상마다 위험 점수를 매기고 틀린 알림을 줄였습니다(Unit 4). 이번 Unit에서는 <mark>**점수 파일의 사실만으로 AI 에게 요약을 받고**</mark>, Module 4에서 만난 상황을 원인과 해결로 정리합니다.

<h2>오늘의 계획 (약 2시간 40분)</h2>

| 순서 | 시간 | 하는 일 |
|---|---|---|
| 1. 시작 | 15분 | 이 레슨을 읽고 `requests` 설치, 파일 두 개 만들기 |
| 2. 핵심 실습 | 약 110분 | 실습 5-1, 실습 5-2 (초안에 근거 메모) |
| 3. 글쓰기 | 20분 | 「오늘의 글 쓰기」에서 블로그 글 한 편 |
| 4. 결과 기록 | 15분 | 실습 파일 확인과 저장소 반영 |

- 시작에서 만드는 두 파일은 `llm_client.py` · `unit05_risk_scores.json` 입니다. 핵심 실습 110분은 실습 5-1 약 40분, 실습 5-2 약 70분이 기준입니다.
- 초안에는 글감과 연결되는 값이 보일 때 메모합니다. 하루 3시간에서 남는 20분쯤은 밀린 곳을 따라잡는 여유 시간입니다.
- 「Gemini API 키와 .env 만들기」(선택)는 계획표에 넣지 않았습니다. 키를 만들면 20분쯤 더 걸리니 이 여유 시간에서 씁니다.

- `llm_client.py` 는 LLM(대형 언어 모델, Large Language Model · 엘엘엠: 글을 읽고 글로 답하는 AI) 호출 파일이고, `unit05_risk_scores.json` 은 점수 파일입니다.

<h2>오늘 만들 것 두 가지</h2>

1. **실습 5-1**: 점수 파일에서 먼저 확인할 대상 3명을 고르고, **AI** 에게 파일에 있는 사실만으로 짧은 요약문을 받는 `event_summary.py` 를 만듭니다. 대부분은 미리 채워 두었고, 빈칸 세 곳(① · ② · ③)만 한 줄씩 씁니다.
2. **실습 5-2**: **Module 4 총정리**입니다. 새로 배우는 것 없이, 상황 1 · 2 · 3 · 4 · 7 가운데 3개를 골라 원인과 고치는 방법을 내 말로 초안에 씁니다.

**응용 5-3은 여유가 되면 해 보세요.** 핵심 실습 두 개와 블로그 글쓰기를 마친 뒤 시간이 남을 때 Unit 3 · 4의 분석 단계를 `pipeline.py` 한 번으로 이어 실행합니다. 응용을 하지 않아도 Module 5를 따라갈 수 있습니다.

**이번 Unit에서 쓰는 것**

- 도구는 **파이썬 · VS Code · 터미널 · git** 이고, 실습 5-1에는 **LLM 호출 함수**(`llm_client.py` 의 `call_llm`)를 씁니다.
  - 이 레슨에서 말하는 **AI** 는 구글의 **Gemini API** 입니다. API(에이피아이)는 내 프로그램이 다른 회사의 프로그램에 요청을 보내 그 기능을 빌려 쓰는 창구입니다. `call_llm` 이 Gemini API 에 글을 보내고 답을 받아 옵니다.
  - `llm_client.py` 는 다음 페이지의 코드 상자를 붙여 넣어 만듭니다. 직접 쓰는 곳은 없습니다.
- 새로 배우는 문법은 실습 5-1의 문자열 이어 붙이기 `"구분 글자".join(리스트)` 하나입니다. 빈칸의 나머지는 앞에서 쓴 `if` 와 `==` 입니다.
- 점수 기준(high 60 이상 · mid 35 이상)과 AI 에게 요약시킬 대상 수(3명)는 **고정**하고, <mark>값을 바꿔 가며 비교하지 않습니다</mark>.
- 실습에서 `[핵심 질문]` 표시가 붙은 질문은 이 실습에서 꼭 알아야 할 핵심 질문이고, <mark>내 출력이나 샘플 데이터의 값을 근거로 이유까지 씁니다</mark>.

**API 키가 없어도 끝까지 할 수 있습니다**

- 진짜 AI 요약을 받으려면 **Gemini API 키**가 저장소 폴더 `network-study-notes` 바로 아래(`anomaly_detection` 의 바깥)의 `.env` 파일에 있어야 합니다. API 키는 구글에 「내가 누구인지」 알리는 비밀 글자라서 비밀번호처럼 다룹니다. `.env` 는 이런 비밀 값을 적어 두는 파일이고, 깃허브에 올리지 않습니다. 키를 만드는 방법은 이 레슨의 「Gemini API 키와 .env 만들기」에 있습니다.
- <mark>키가 없으면 `call_llm` 이 `[LLM 호출 실패] API 키 없음` 을 출력하고 빈 문자열을 돌려주고, 요약 자리에는 대체 문장 `(요약 실패 — 점수와 이유를 직접 확인)` 이 들어갑니다.</mark> 프로그램은 멈추지 않고 끝까지 실행됩니다.
- [주의] <mark style="background:#ffc4d6">**키가 없을 때는 출력과 보고서 답이 실습 5-1 정답 펼침의 「키가 있을 때」 예와 다릅니다.**</mark> 실습 5-1 의 출력은 단계 1 ~ 4 로 나뉘는데, 단계 1 ~ 3과 점수 · 등급 · 대상은 같고, 단계 4 의 요약만 대체 문장으로 바뀝니다. 이때는 실습 5-1 정답 펼침의 「키가 없을 때」 출력과 맞춰 보고, AI 요약 문장을 읽어야 하는 보고서 질문은 실습 5-1 정답 펼침에 실린 요약 예시로 답합니다.
- AI 가 쓰는 요약 문장은 실행할 때마다 조금씩 달라집니다. 키가 있는 사람도 문장은 해당 실습의 정답 펼침과 달라도 정상이고, 점수 · 등급 · 건수는 같아야 합니다.
- **무료 Gemini 키는 1분에 부를 수 있는 횟수에 한도가 있습니다**(이 문서를 쓸 때는 15번이었고, 숫자는 구글이 바꿀 수 있습니다). 실습 5-1은 한 번 실행에 3번 호출합니다. `[LLM 호출 실패] 상태 코드 429` 가 나오면 <mark>1분 기다린 뒤 다시 실행</mark>합니다.

> **확인** — 오늘 할 네 가지(시작 · 핵심 실습 · 글쓰기 · 마무리)를 순서대로 말할 수 있고, 키가 없어도 실습 5-1을 끝까지 할 수 있다는 것을 알면 성공입니다. 헷갈리면 위 「오늘의 계획」 표를 한 번 더 봅니다.

## 폴더 열고 LLM 호출 파일 준비하기

1. **[VS Code]** `network-study-notes` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
   - 터미널 이름 칸에 **bash** 가 보이는지 봅니다. `powershell` 이 보이면 터미널 오른쪽 위 `+` 옆의 **∨** › **Git Bash** 로 새 터미널을 엽니다. 이 레슨의 명령은 모두 Git Bash 기준입니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치를 확인하고, `llm_client.py` 가 쓰는 `requests` 를 설치합니다. <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나면</mark> 됩니다. Unit 2 에서 가상환경을 켜고 판다스를 설치했다면 <mark>첫 줄로 `network-study-notes` 폴더에서 같은 가상환경을 먼저 켭니다.</mark> 가상환경을 쓰지 않는 사람은 첫 줄을 건너뜁니다. 켜지 않고 설치하면 `requests` 와 판다스가 서로 다른 파이썬에 깔립니다.
   ```bash
   # 이 명령은 전체를 복사해 Git Bash에 붙여 넣어 실행하세요.
   source .venv/Scripts/activate   # 가상환경을 쓰는 사람만 (network-study-notes 에서)
   cd anomaly_detection
   pwd
   ls
   python -m pip install requests
   python - <<'PY'
   import requests

   print(requests.__version__)
   PY
   ```
   - 명령 풀이: `cd 폴더이름` 그 폴더로 이동 · `pwd` 지금 있는 폴더의 위치 확인 · `ls` 폴더 안의 파일 이름 보기 · `python -m pip install requests` 인터넷으로 요청을 보내는 도구 `requests` 설치 · 마지막 Python 블록에서 설치한 `requests` 의 버전 출력
   - 설치가 끝나면 <mark>`Successfully installed …` 또는 `Requirement already satisfied` 가 나옵니다.</mark> 마지막에 `WARNING: You are using pip version …` 이 나와도 무시합니다.
   - <mark>마지막 명령에서 점이 든 숫자(예: `2.34.2`)가 나오면</mark> `requests` 를 쓸 수 있습니다. 숫자는 설치한 때에 따라 다릅니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에서 `python -m pip install requests` 로 `requests` 를 설치하고 버전 숫자가 나왔다
<!-- /checklist -->

3. **파일은 이렇게 만듭니다.** 이 레슨에 나오는 파일은 모두 코드 상자에서 복사해 만들고, 「`파일이름` 파일을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 붙여 넣고, `Ctrl + S` 로 저장합니다.
   - 핵심 실습 전에 [블로그 초안 준비](__SITE__/exercises/module/4/unit/5/lesson/8/page/1)에서 이번 유닛의 글 파일을 엽니다.
4. **[VS Code]** `anomaly_detection` 폴더 바로 아래에 `llm_client.py` 파일을 만들어 아래 `llm_client.py` 코드 상자의 내용을 붙여 넣습니다. <mark>같은 이름의 파일이 이미 있어도 아래 내용으로 덮어씁니다.</mark> 키가 없을 때도 멈추지 않고 빈 문자열을 돌려주도록 만든 파일이라, 출력이 이 Unit의 문서와 같아집니다.

<h2><code>llm_client.py</code></h2>

Gemini API 를 부르는 함수 세 개입니다.

| 함수 | 하는 일 | 돌려주는 값 |
| --- | --- | --- |
| `find_env` | 지금 폴더부터 위쪽으로 `.env` 를 찾음 | `.env` 경로, 없으면 `None` |
| `read_api_key` | `.env` 에서 키를 읽음 | 키 값, 없으면 `None` |
| `call_llm` | 질문을 Gemini API 에 보냄 | 답 문장 |

키가 없거나 호출이 실패하면 `call_llm` 은 `[LLM 호출 실패] …` 를 출력하고 빈 문자열 `""` 을 돌려줍니다.

```python
import os                                                            # 폴더 · 파일 위치를 다루는 도구
import requests                                                      # 인터넷으로 요청을 보내는 도구

URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"  # Gemini API 에 글을 보낼 주소
MODEL = "gemini-3.5-flash-lite"                                      # 쓸 모델 이름


def find_env():                                                      # .env 파일을 찾는 함수
    """지금 폴더부터 다섯 단계 위 폴더까지 .env 를 찾아 경로를 리턴한다. 없으면 None."""
    folder = os.getcwd()                                             # 지금 폴더에서 시작한다
    for step in range(5):                                            # 다섯 단계 위까지 찾는다
        path = os.path.join(folder, ".env")                          # 그 폴더 안의 .env 경로를 만든다
        if os.path.exists(path):                                     # 그 파일이 있으면
            return path                                              # 찾은 경로를 리턴한다
        folder = os.path.dirname(folder)                             # 한 단계 위 폴더로 간다
    return None                                                      # 끝까지 없으면 None 을 리턴한다


def read_api_key():                                                  # .env 에서 키를 읽는 함수
    """.env 의 GEMINI_API_KEY 값을 리턴한다. .env 나 키가 없으면 None."""
    path = find_env()                                                # .env 위치를 찾는다
    if path is None:                                                 # .env 가 없으면
        return None                                                  # 키도 없다
    api_key = None                                                   # 키를 못 찾으면 None 으로 남는다
    with open(path, encoding="utf-8") as file:                       # .env 를 읽기 모드로 연다
        for line in file:                                            # 한 줄씩 꺼낸다
            parts = line.strip().split("=", 1)                       # 줄 끝 공백을 지우고 = 에서 둘로 나눈다
            if parts[0] == "GEMINI_API_KEY" and len(parts) == 2 and parts[1] != "":  # 키 이름이 맞고 값이 있으면
                api_key = parts[1]                                   # = 뒷부분이 키 값이다
    return api_key                                                   # 읽은 키를 리턴한다


def call_llm(question):                                              # 질문 글을 받는 함수
    """Gemini API 에 질문을 보내 답 문장을 리턴한다. 키가 없거나 호출이 실패하면 빈 문자열("")."""
    api_key = read_api_key()                                         # .env 에서 키를 읽는다
    if api_key is None:                                              # 키가 없으면
        print("[LLM 호출 실패] API 키 없음")                         # 호출하지 않고 알린다
        return ""                                                    # 빈 문자열을 리턴한다
    headers = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}  # 키와 본문 형식을 적은 머리글
    body = {"model": MODEL, "temperature": 0, "messages": [{"role": "user", "content": question}]}  # 보낼 본문
    try:                                                             # 아래 요청을 해 본다
        response = requests.post(URL, headers=headers, json=body, timeout=30)  # Gemini API 에 POST 요청을 보낸다
    except requests.RequestException:                                # 인터넷이 끊기는 등 요청 자체가 실패하면
        print("[LLM 호출 실패] 인터넷 연결 오류")                    # 실패를 알린다
        return ""                                                    # 빈 문자열을 리턴한다
    if response.status_code != 200:                                  # 200(성공)이 아니면
        print("[LLM 호출 실패] 상태 코드", response.status_code)     # 429 면 1분 기다린 뒤 다시 실행한다
        return ""                                                    # 빈 문자열을 리턴한다
    data = response.json()                                           # 응답(JSON 글자)을 딕셔너리로 바꾼다
    return data["choices"][0]["message"]["content"]                  # 답 문장만 리턴한다
```

- 키 값은 이 파일에 적지 않습니다. 키는 `.env` 에만 있고, 이 파일은 깃허브에 올라가도 됩니다.
- `try:` · `except` 는 「해 보고, 이 오류가 나면 멈추지 않고 아래 줄을 실행한다」는 뜻입니다. 이 파일에서만 쓰고, 직접 쓰지는 않습니다.
- `call_llm` 은 `requests.post` 로 Gemini API 주소에 POST 요청을 보냅니다. 머리글(`headers`)에는 API 키를 담고, 본문(`body`)에는 쓸 모델(구글이 만든 여러 AI 가운데 하나의 이름)과 질문 글을 담습니다. `temperature` 를 0 으로 두면 답 문장이 덜 흔들립니다.
- 답이 오면 상태 코드가 200(성공)인지 먼저 보고, 응답 안에 여러 겹으로 들어 있는 답 문장만 꺼내 돌려줍니다.

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 `llm_client.py` 를 만들어 코드 상자 내용을 붙여 넣고 저장했다
<!-- /checklist -->

5. **[VS Code]** `anomaly_detection` 폴더 바로 아래에 `unit05_risk_scores.json` 파일을 만들어 아래 `unit05_risk_scores.json` 상자의 내용을 그대로 붙여 넣습니다. Unit 4 실습 4-1 이 저장한 점수 파일과 같은 내용입니다. <mark>이미 있으면 아래 내용으로 덮어씁니다</mark>(출력이 문서와 같아야 하기 때문입니다). Module 4 Unit 5와 Module 5가 이 이름으로 읽으니 이름을 바꾸지 않고 그대로 씁니다.

<h2><code>unit05_risk_scores.json</code></h2>

대상별 점수 기록 5건이고, 점수가 높은 순서로 저장돼 있습니다.

| 키 | 뜻 |
| --- | --- |
| `entity` | 점수를 매긴 대상(사용자 또는 IP) |
| `score` | 점수 |
| `grade` | 등급 |
| `reasons` | 탐지된 규칙 이름 |

<pre class="copyable"><code>[
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
</code></pre>

<!-- checklist -->
- [ ] `anomaly_detection` 폴더에 `unit05_risk_scores.json` 을 만들어 상자 내용을 붙여 넣고 저장했다
<!-- /checklist -->

6. **[터미널]** 두 파일이 정상인지 확인합니다.
   ```bash
   # 이 명령은 전체를 복사해 Git Bash에 붙여 넣어 실행하세요.
   python - <<'PY'
   import json

   with open("unit05_risk_scores.json", encoding="utf-8") as file:
       print(len(json.load(file)))
   PY
   python - <<'PY'
   from llm_client import read_api_key

   print(read_api_key() is not None)
   PY
   ```
   - 첫 줄은 <mark>`5` 가 나오면</mark> 됩니다.
   - 둘째 줄은 `.env` 에서 키를 읽었는지 알려 줍니다. 키 값은 화면에 나오지 않습니다.
     - `True`: 키가 있습니다. 실습 5-1에서 진짜 AI 요약을 받습니다.
     - `False`: 키가 없습니다. <mark>그대로 실습 5-1로 가도 됩니다.</mark> 요약 자리에 대체 문장이 나옵니다. 키를 만들고 싶으면 다음 페이지 「Gemini API 키와 .env 만들기」를 먼저 합니다.

> **확인** — 첫 줄에서 `5` 가 나오고, 둘째 줄에서 `True` 나 `False` 가 나오면(오류 글자 없이) 성공입니다. `ModuleNotFoundError` 나 `FileNotFoundError` 가 나오면 이 레슨 마지막 페이지 「오류가 나면」의 표를 봅니다.

<!-- checklist -->
- [ ] 6번 확인 명령 두 줄을 쳐서 `5` 와 `True` 또는 `False` 가 나왔다
<!-- /checklist -->

## Gemini API 키와 .env 만들기 (키를 쓸 사람만)

진짜 AI 요약을 받고 싶은 사람만 합니다. 키를 만들고, 키가 맞는지 확인하고, `.env` 파일에 넣고, 깃허브에 올라가지 않게 막은 뒤, 마지막으로 읽히는지 봅니다. <mark>하지 않아도 실습 5-1은 대체 문장으로 끝까지 됩니다.</mark>

- **왜 PC 마다 해야 하나**:
  - API 키는 `.env` 파일에 들어 있고, 이 파일은 PC 마다 따로 있습니다.
  - `.env` 는 깃허브에 올리지 않으므로 다른 PC 로 따라오지 않습니다. 자리를 바꿨다면 그 PC 에서 다시 만듭니다.
- **먼저 확인하기**: <mark>시작하기 6번에서 `True` 가 나왔으면 이 절은 건너뜁니다.</mark>
  - **[터미널]** `anomaly_detection` 폴더에서 한 단계 위 폴더의 파일을 숨김 파일까지 봅니다.
    ```bash
    ls -a ..
    ```
  - 명령 풀이: `ls -a` 숨김 파일(이름이 점으로 시작하는 파일)까지 보기 · `..` 한 단계 위 폴더(`network-study-notes`)
  - 나오는 것: 목록에 `.env` 와 `.gitignore` 가 있는지 봅니다. 없는 것은 아래 3단계에서 만듭니다.

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
- 나오는 것: <mark>`"models"` 가 든 긴 목록이 나오면</mark> 키가 맞습니다. `UNAUTHENTICATED` 나 `API key not valid` 같은 오류 글자가 나오면 키를 다시 복사합니다.
- 같은 명령을 여러 번 반복하지 않습니다. 호출 횟수에 한도가 있습니다.
- 이렇게 직접 친 명령은 키까지 Git Bash 의 명령 기록에 남습니다. 공용 PC 라면 확인한 뒤 `history -c` 를 쳐서 기록을 지웁니다.

<!-- checklist optional -->
- [ ] 구글 AI Studio 에서 키를 만들고 `curl` 로 `"models"` 목록이 나오는 것을 확인했다
<!-- /checklist -->

**3단계 · `.env` 파일 만들기**

- **[VS Code]** 왼쪽 목록에서 `network-study-notes` 폴더(`anomaly_detection` 의 바깥)를 오른쪽 클릭 › **New File** 을 누르고 `.env` 를, 같은 방법으로 `.gitignore` 를 만듭니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다. 파일 이름 뒤에 `.txt` 같은 것이 붙지 않아야 합니다.
- `.env` 를 `anomaly_detection` 바깥에 두어도 되는 이유: `llm_client.py` 의 `find_env` 가 지금 폴더부터 한 단계씩 위쪽 폴더로 올라가며 찾기 때문입니다. 그래서 `anomaly_detection` 에서 실행해도 바깥의 `.env` 가 읽힙니다.
- **[VS Code]** 왼쪽 파일 목록에서 `network-study-notes` 바로 아래의 `.env` 를 열고 아래 한 줄만 적습니다. <mark>등호 앞뒤에 빈칸을 넣지 않고, 따옴표도 넣지 않습니다.</mark>

<pre class="copyable"><code>GEMINI_API_KEY=여기에_복사한_키를_붙여넣습니다
</code></pre>

- 탭 이름 옆에 점(●)이 없으면 저장된 것입니다. 이 한 줄 말고 다른 글자는 넣지 않습니다.

<!-- checklist optional -->
- [ ] `network-study-notes` 바로 아래(`anomaly_detection` 의 바깥)에 `.env` 를 만들어 `GEMINI_API_KEY=키` 한 줄을 적고 저장했다
<!-- /checklist -->

**4단계 · 깃허브에 키가 올라가지 않게 막기**

- **[VS Code]** `network-study-notes` 바로 아래의 `.gitignore` 를 엽니다. 맨 아래에 `.env` 한 줄이 있는지 보고, 없으면 적습니다.

<pre class="copyable"><code>.env
</code></pre>

- **[터미널]** 막혔는지 확인합니다. <mark>목록에 `.env` 가 보이지 않으면</mark> 막힌 것입니다.
  ```bash
  git status
  ```
  - 나오는 것: 바뀐 파일 목록에 `.env` 가 있으면 아직 막히지 않은 것입니다. `.gitignore` 의 `.env` 줄이 맞는지 다시 봅니다. 깃허브에 올리기 전에는 항상 이 확인을 합니다.

<!-- checklist optional -->
- [ ] `network-study-notes` 바로 아래의 `.gitignore` 에 `.env` 줄을 두고, `git status` 에 `.env` 가 보이지 않았다
<!-- /checklist -->

**5단계 · 이번 Unit에서 쓸 폴더에서 읽히는지 확인하기**

- **[터미널]** `anomaly_detection` 폴더에서 시작하기 6번의 둘째 명령을 다시 칩니다. <mark>`True` 가 나오면</mark> 됩니다. 키 값은 화면에 나오지 않습니다.
  ```bash
  # 이 명령은 전체를 복사해 Git Bash에 붙여 넣어 실행하세요.
  pwd
  python - <<'PY'
  from llm_client import read_api_key

  print(read_api_key() is not None)
  PY
  ```
  - 명령 풀이: 여러 줄 Python 블록에서 점검 코드를 바로 실행

<!-- checklist optional -->
- [ ] `anomaly_detection` 폴더에서 5단계 명령을 쳐서 `True` 가 나왔다
<!-- /checklist -->

**막혔을 때**

- `.env.txt` 처럼 이름이 다르게 만들어졌다면, `network-study-notes` 폴더에서 `mv .env.txt .env` 를 칩니다(`mv 이전이름 새이름` 은 이름 바꾸기).
- `False` 가 나오면 `GEMINI_API_KEY=` 글자가 틀렸거나, 등호 뒤가 비어 있거나, 등호 앞에 빈칸이 있는 것입니다. 3단계를 다시 봅니다.
- 키가 맞는데(2단계는 성공) `상태 코드 429` 가 1분을 기다려도 계속 나오면, 구글이 그 계정의 무료 호출 한도를 0 으로 둔 경우가 구글 포럼에 보고되어 있습니다. 초안에 「막힘: 429 가 계속 나옴」이라고 적고 넘어갑니다. 요약 자리에는 대체 문장이 나오고 프로그램은 멈추지 않습니다.

**키를 다룰 때 지킬 것**

- 단톡방이나 메신저에 키를 올리지 않습니다.
- 화면을 공유할 때 `.env` 를 열어 두지 않습니다.
- 깃허브에 웹으로 파일을 올릴 때 `.env` 를 끌어다 놓지 않습니다. `.gitignore` 는 웹 업로드를 막아 주지 않습니다.
- 키가 노출됐다면 구글 AI Studio 의 키 목록에서 그 키를 삭제하고 새로 만듭니다. 쓰지 않는 예전 키도 같은 곳에서 삭제해 둡니다.

> **확인** — 5단계에서 `True` 가 나오고, `git status` 목록에 `.env` 가 보이지 않으면 성공입니다. `False` 가 나오면 위 「막혔을 때」를 봅니다.

## 오류가 나면

먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.

파이썬 오류는 이렇게 고칩니다.

| 오류 | 뜻 | 고치는 법 |
| --- | --- | --- |
| `No module named 'llm_client'` | <mark>`llm_client.py` 가 `anomaly_detection` 폴더 바로 아래에 없다는 뜻</mark> | 시작하기 4번의 코드 상자로 만듦 |
| `No module named 'requests'` | 이 터미널의 파이썬에 `requests` 가 없음 | 시작하기 2번의 설치 명령을 침(가상환경을 쓰면 먼저 켬) |
| `FileNotFoundError` | `unit05_risk_scores.json` 이 없거나 이름이 다름 | 시작하기 5번의 코드 상자로 만듦 |

- 앞의 두 오류는 `ModuleNotFoundError: …` 로 시작합니다. 설치 명령은 `python -m pip install requests` 입니다.

`[LLM 호출 실패]` 뒤에 나오는 글자로 원인을 봅니다.

| 뒤의 글자 | 뜻 | 고치는 법 |
| --- | --- | --- |
| `API 키 없음` | `.env` 를 못 찾았거나 키 줄이 없음 | 키를 쓰려면 「Gemini API 키와 .env 만들기」 |
| `상태 코드 400` · `401` · `403` | 키가 틀림 | 2단계로 키를 확인하고 `.env` 에 다시 붙여 넣음 |
| `상태 코드 404` | 모델 이름(`MODEL`)을 구글이 바꾸거나 없앰 | 해당 실습의 정답 펼침과 과정 공지에서 새 모델 이름을 확인 |
| `상태 코드 429` | 1분 호출 한도를 넘음 | <mark>1분 기다린 뒤 다시 실행</mark> |
| `인터넷 연결 오류` | 인터넷이 끊겼거나 30초 안에 답이 없음 | 연결을 확인하고 다시 실행 |

- `API 키 없음` 은 <mark>오류가 아니라, 키 없이 대체 문장으로 진행하는 정상 동작</mark>입니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 이 Unit의 해당 실습의 정답 펼침을 보고</mark>, 풀리지 않으면 초안에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

> **확인** — 오류 글자를 위 두 표에서 찾아 고친 뒤 같은 명령을 다시 쳐서 오류가 사라지면 성공입니다. 표에 없는 오류이면 해당 실습의 정답 펼침을 보고, 그래도 안 되면 초안에 막힌 곳을 적고 넘어갑니다.

---
