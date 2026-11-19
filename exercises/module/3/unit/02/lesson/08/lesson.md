---
id: m3-u02-l08
title: 도전 2-3 · 요청 이력 저장과 상태별 건수
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/084_day03_pm_sla.md
  mission_id: GichanSource.m3-1023-pm-sla
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 도전 2-3 · 요청 이력 저장과 상태별 건수

## 목표: 저장 함수와 건수 세기

> **오늘 들어온 일**
>
> A사 관제 담당이 보낸 메시지: 「지금까지 만든 요청서는 프로그램을 끄면 사라집니다. 접수 · 승인 · 반려 · 부여를 한 번 돌리고 나면 요청서 전체를 파일로 남겨 주세요. 그리고 상태별로 몇 건인지 숫자로 보고 싶은데, 손으로 세면 시간이 걸리고 틀리기 쉽습니다.」
> - 이 실습에서 하는 일: 요청서 리스트를 `requests.json` 으로 저장하는 함수 `save_requests` 와 상태별 건수를 세는 함수 `count_by_status` 를 직접 씁니다. Unit 2와 Unit 2에서 만든 함수를 모두 이어서 한 번 돌려 봅니다. 마지막에 이번 Unit에서 만든 것을 깃허브에 올립니다.
> - 끝나면 쓰는 것: 보고서 (가)~(다) 답

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「문제」 전까지는 이 실습의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다.

## 왜 요청 이력을 파일로 남기는가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 요청서는 프로그램이 켜져 있는 동안에만 남아 있고, 프로그램이 끝나면 사라집니다. 파일로 저장해야 다음 날에도 요청서를 볼 수 있습니다. 여기서 **이력**은 요청이 어떻게 처리됐는지 남은 기록입니다.
2. 상태별 건수는 매일 아침 한눈에 보는 숫자입니다.

## 2.1 JSON 파일로 저장하기

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

- 지금까지는 JSON 파일을 **읽기**만 했습니다. 이번에는 파일에 **쓰기**를 합니다.

| 파일 열기 | 뜻 |
|---|---|
| `open(path, encoding="utf-8")` | 읽기 모드. 파일이 있어야 하고, 내용을 읽기만 한다 |
| `open(path, "w", encoding="utf-8")` | 쓰기 모드. 파일이 없으면 만들고, **있으면 내용을 지우고 새로 쓴다** |

- `json.dump(데이터, 파일, ensure_ascii=False, indent=2)` 는 데이터를 JSON 문자열로 바꿔 파일에 씁니다. `ensure_ascii=False` 는 한글을 그대로 쓰라는 뜻이고, `indent=2` 는 사람이 읽기 쉽게 줄을 나누고 2칸씩 들여 쓰라는 뜻입니다.

<figure class="page-figure"><img src="assets/f01.svg" alt="여섯 건을 접수해 처리·점검한 뒤 requests.json 에 저장하고 다시 읽어 확인한다"></figure>

**문법 상자 — 파일에 JSON 쓰기**

아래 코드는 읽기만 합니다. 따라 치지 않습니다.

**① `"w"` 로 열고 `json.dump` 로 쓰기**

```python
import json                                                         # JSON 을 다루는 모듈을 불러온다

data = [{"id": 1, "reason": "정산 확인"}]                             # 저장할 리스트
with open("demo.json", "w", encoding="utf-8") as demo_file:                 # 파일을 쓰기 모드("w")로 연다
    json.dump(data, demo_file, ensure_ascii=False, indent=2)                # 리스트를 파일에 JSON 으로 쓴다
file = open("demo.json", encoding="utf-8")                       # 파일을 연다
text = file.read()                                               # 내용을 문자열로 읽는다
print(text)                                                      # 쓴 파일을 다시 열어 내용을 출력한다
```

실행 결과:

```
[
  {
    "id": 1,
    "reason": "정산 확인"
  }
]
```

**② `ensure_ascii=False` 를 빼면 한글이 `\uXXXX` 문자열로 바뀌어 사람이 읽을 수 없습니다**

```python
import json                                                         # JSON 을 다루는 모듈을 불러온다

data = [{"id": 1, "reason": "정산 확인"}]                             # 저장할 리스트
with open("demo.json", "w", encoding="utf-8") as demo_file:                 # 파일을 쓰기 모드("w")로 연다
    json.dump(data, demo_file, indent=2)                                    # ensure_ascii=False 를 빼고 쓴다
file = open("demo.json", encoding="utf-8")                       # 파일을 연다
text = file.read()                                               # 내용을 문자열로 읽는다
print(text)                                                      # 쓴 파일을 다시 열어 내용을 출력한다
```

실행 결과:

```
[
  {
    "id": 1,
    "reason": "\uc815\uc0b0 \ud655\uc778"
  }
]
```

- `as demo_file` 은 열린 파일을 `demo_file` 이라는 이름으로 부르겠다는 뜻이고, 파일은 `with` 아래에 들여쓴 줄 안에서만 열려 있습니다.
- `open(…).read()` 는 파일을 열어 내용 전체를 문자열로 읽습니다. 위 코드는 방금 쓴 파일을 확인하려고 한 번 더 읽어 출력한 것입니다.
- 세는 모양 `old_count = counts.get(키, 0)` → `counts[키] = old_count + 1` 은 Unit 1에서 쓴 것과 같습니다. `counts.get(키, 0)` 은 그 키가 있으면 값을, 없으면 0 을 꺼냅니다.

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## 도전 2-3 · 요청서 저장하고 상태별 건수 세기

**이런 상황이 있습니다**

- **지금은**: 접수 · 승인 · 부여 · 기한 점검 결과가 프로그램이 켜져 있는 동안에만 남아 있어서, 프로그램을 끄면 모두 사라집니다. 관제 담당은 상태별로 몇 건인지도 숫자로 보고 싶어 하는데, 손으로 세면 틀리기 쉽습니다.
- **그래서 만드는 것**: `save_requests`(요청서 전체를 `requests.json` 파일에 저장하고 저장한 건수를 리턴)와 `count_by_status`(상태별 건수를 딕셔너리로 리턴)입니다.
- **실행하면**: 세 단계가 나옵니다. 단계 1은 요청 여섯 건의 처리 결과, 단계 2는 상태별 건수와 SLA 초과 요청 번호, 단계 3은 저장 결과입니다. 끝나면 `requests.json` 을 열어 한글이 그대로 저장됐는지 봅니다.
- **현업에서는**: 신청 도구도 신청 기록을 지우지 않고 보관하고, 상태별 건수를 날마다 세어 보냅니다.

**할 일**

1. `request_flow.py` 와 `challenge2-3_run.py` 두 파일을 만들고, `save_requests` 와 `count_by_status` 본문을 직접 씁니다.
2. 실행해서 <mark>처리 결과</mark>(단계 1: 처리), <mark>상태별 건수와 SLA 초과</mark>(단계 2: 점검), <mark>저장 결과</mark>(단계 3: 저장)를 읽습니다. `requests.json` 파일도 열어 봅니다.

**`request_flow.py`**

```python
import json                                                      # JSON 파일을 쓰는 모듈을 불러온다


def save_requests(requests, path):                               # 요청서 리스트와 저장할 파일 경로를 받는 함수
    """요청서 리스트를 JSON 파일로 저장한다(한글은 그대로).
    요청 처리 상태를 다음에도 이어 보려고 남길 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. path 를 쓰기 모드("w")로, encoding="utf-8" 로 열어 f 로 받는다
    # 2.   json.dump 로 requests 를 f 에 쓴다. ensure_ascii=False 와 indent=2 를 함께 쓴다
    # 3. 저장한 요청서 건수 len(requests) 를 리턴한다 (with 블록 밖, 함수 안쪽 줄에 맞춘다)


def count_by_status(requests):                                   # 요청서 리스트를 받는 함수
    """상태별 요청서 개수를 센다.
    검토 중 · 승인 · 부여가 각각 몇 개인지 현황을 볼 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. 빈 딕셔너리 counts 를 만든다
    # 2. requests 에서 request 를 하나씩 꺼낸다
    # 3.   request["status"] 를 status 에 담는다
    # 4.   counts.get(status, 0) 을 old_count 에 담는다 (없으면 0)
    # 5.   counts[status] 를 old_count + 1 로 정한다
    # 6. 반복이 끝나면 counts 를 리턴한다
```

- 본문은 모두 함수 안이라 4칸으로 쓰고, `with` 와 `for` 안쪽은 4칸 더(8칸) 들어갑니다. 각 주석 바로 아래 줄에 씁니다. `save_requests` 의 `return len(requests)` 는 `with` 와 같은 4칸입니다.
- 채우기 전에 처음 실행하면(`requests.json` 이 아직 없을 때) 단계 2의 첫 줄이 `None` 으로 나옵니다. `count_by_status` 가 아무것도 리턴하지 않기 때문입니다. 이어서 단계 3에서 `저장 함수가 리턴한 건수: None` 과 `[경고] 설정 파일 없음: requests.json` 이 나온 뒤 `IndexError` 가 납니다. `save_requests` 가 파일을 만들지 않았기 때문입니다.

**`challenge2-3_run.py`** — 그대로 붙여 넣습니다. 학생이 쓰는 줄은 없습니다. 요청 여섯 건을 접수하고 처리한 뒤, 단계 1은 승인 · 반려 · 부여 결과를 출력하고, 단계 2는 상태별 건수와 SLA 초과 요청을 출력합니다. 단계 3은 `requests.json` 으로 저장한 뒤 다시 읽어 확인합니다.

```python
from datetime import datetime                                    # 지금 시각을 만드는 데 쓴다
from config_loader import load_json                              # Unit 1에서 만든 안전한 읽기 함수를 불러온다
from req_create import REQUESTS, create_request                  # 실습 2-1에서 만든 요청서 함수와 리스트를 불러온다
from req_review import approve_request, reject_request           # 실습 2-2에서 만든 승인 · 반려 함수를 불러온다
from req_grant import grant_request                              # 도전 2-1에서 만든 부여 함수를 불러온다
from req_sla import check_sla_breach                             # 도전 2-2에서 만든 기한 점검 함수를 불러온다
from request_flow import save_requests, count_by_status          # 방금 만든 저장 · 집계 함수를 불러온다

NOW = datetime.strptime("2026-10-23 14:00", "%Y-%m-%d %H:%M")    # 이번 실습의 지금 시각(고정)

INBOX = [                                                        # 오늘 들어온 요청 여섯 건. (요청자, 자원, 행위, 희망 만료 시각, 이유, 접수 시각)
    ("seoyeon", "SETTLE", "QUERY", "2026-10-27 18:00", "정산 대조 지원", "2026-10-23 08:30"),
    ("gaeun", "SALES", "QUERY", "2026-10-28 18:00", "감사 자료 대응", "2026-10-23 10:30"),
    ("dami", "SALES", "QUERY", "2026-10-27 18:00", "인수인계 자료 확인", "2026-10-23 12:00"),
    ("junho", "SETTLE", "QUERY", "2026-10-27 18:00", "정산 확인", "2026-10-23 09:00"),
    ("seoyeon", "ACCOUNT", "QUERY", "2026-10-27 18:00", "계정 권한 점검", "2026-10-23 07:50"),
    ("tester", "SALES", "QUERY", "2026-10-27 18:00", "시험 계정 확인", "2026-10-23 10:00"),
]
for user, resource, action, until, reason, received_at in INBOX:         # 요청을 하나씩 꺼내
    create_request(user, resource, action, until, reason, received_at)   # 접수한다

print("--- 단계 1: 처리 - 승인 · 반려 · 부여")                      # 단계 1 시작을 알리는 줄
approve_request(REQUESTS[0], "security_manager")                 # 1번 승인
reject_request(REQUESTS[1], "security_manager")                  # 2번 반려
approve_request(REQUESTS[2], "security_manager")                 # 3번 승인
approve_request(REQUESTS[3], "security_manager")                 # 4번 승인
for request in REQUESTS:                                         # 요청서를 하나씩 꺼내
    is_success, result = grant_request(request)                          # 부여를 시도한다(승인된 것만 의미가 있다)
    print(request["id"], request["user"], request["status"], "->", result)   # 번호 · 요청자 · 상태 -> 결과 를 출력한다

print("--- 단계 2: 점검 - 상태별 건수와 SLA")                      # 단계 2 시작을 알리는 줄
print(count_by_status(REQUESTS))                                 # 상태별 건수를 출력한다
for request in check_sla_breach(REQUESTS, NOW):                  # 기한을 초과한 요청서를 하나씩 꺼낸다
    print("SLA 초과 요청 번호:", request["id"])                    # 요청 번호를 출력한다

print("--- 단계 3: 저장 - requests.json")                        # 단계 3 시작을 알리는 줄
count = save_requests(REQUESTS, "requests.json")                 # 요청서 리스트 전체를 파일로 저장하고 저장한 건수를 받는다
print("저장 함수가 리턴한 건수:", count)                            # 리턴한 건수를 출력한다
saved = load_json("requests.json", [])                           # 저장한 파일을 다시 읽어
print("저장한 요청서", len(saved), "건, 첫 요청서의 상태:", saved[0]["status"])   # 건수와 첫 요청서의 상태를 출력한다
```

**순서**

0. **[터미널]** 도전 2-2 파일이 정상인지 먼저 확인합니다. 마지막 줄에 `도전 2-2 파일 정상` 이 나와야 합니다(맥북은 `python3 -c "…"`). 아니면 「정답」 레슨 맨 아래 「앞 실습 파일 완성본」으로 `req_sla.py` 와 `config/sla.json` 을 먼저 만듭니다.
   ```bash
   python -c "from req_sla import check_sla_breach; print('도전 2-2 파일 정상')"
   ```
1. **[VS Code]** 파일을 만들고 각각 붙여 넣습니다. 파일마다 아래 세 가지 방법 중 **하나만** 고릅니다.
   - **VS Code 에서 만들기**: 파일마다 아래 네 가지를 반복합니다.
     1. VS Code 왼쪽 목록에서 `access_control` 폴더를 클릭해 선택합니다(선택하지 않으면 다른 폴더에 만들어집니다).
     2. 목록 위쪽의 **새 파일**(New File, 파일 모양에 `+`) 아이콘을 누릅니다.
     3. 이름 칸에 파일 이름을 입력하고 Enter 를 누릅니다. 이름은 차례로 `request_flow.py` · `challenge2-3_run.py` 입니다.
     4. 열린 파일에 위 코드 상자의 내용을 복사해 붙여 넣고 저장합니다.
2. **[VS Code]** `request_flow.py` 의 두 함수 본문을 직접 씁니다. 2.1 의 표와 문법 상자를 보고 씁니다.
3. **[터미널]** 위치가 `…/access_control` 인지 확인하고 실행합니다.
   ```bash
   pwd
   python challenge2-3_run.py
   ```
   - 명령 풀이: `pwd` 지금 위치 확인 · `python` 파이썬으로 파일을 실행 · `challenge2-3_run.py` 실행할 파일
   - 맥북은 `python3 challenge2-3_run.py` 로 칩니다.
4. 출력은 세 단계입니다. 단계 1은 요청 여섯 건의 처리 결과(여섯 줄), 단계 2는 상태별 건수와 SLA 초과 요청 번호, 단계 3은 저장 함수가 리턴한 건수와 저장 결과입니다.
   - 도전 2-2에서는 SLA 초과가 1번과 5번이었지만 여기서는 5번만 나옵니다. 이 실행에서는 1번이 승인 · 부여까지 끝나 더 이상 `reviewing` 이 아니기 때문입니다.
5. **[VS Code]** 왼쪽 목록에 새로 생긴 `requests.json` 을 열어 요청서가 한글 그대로 저장됐는지 봅니다.
6. **[보고서]** `report_u2.md` 의 `## 도전 2-3` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, `requests.json` 에 저장된 요청서가 몇 건인지와 상태별 건수를 적어 주세요.
   - (나) [핵심 질문] 반려된 요청서(`rejected`)나 승인은 됐지만 부여하지 않은 요청서(`approved`)도 지우지 않고 `requests.json` 에 남기는 이유는 무엇인가요?
   - (다) [핵심 질문] 상태별 건수가 `granted` 1 · `rejected` 1 · `approved` 2 · `reviewing` 2 로 나왔습니다. 이 숫자를 매일 아침 보면 처리 흐름의 어디가 막혀 있는지 어떻게 알 수 있나요?

## 도전 2-3 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 파일에 쓰기 | `with open(path, "w", encoding="utf-8") as output_file:` |
| 리스트를 JSON 으로 | `json.dump(requests, f, ensure_ascii=False, indent=2)` |
| 상태별 건수 | `old_count = counts.get(status, 0)` → `counts[status] = old_count + 1` |
| 저장한 건수 알리기 | `return len(requests)` |
| 저장했는지 확인 | `load_json("requests.json", [])` 로 다시 읽는다 |

---

## 마무리 · 이번 Unit에서 만든 것을 깃허브에 올리기

문제가 아니라 오늘 한 일을 저장소에 올리는 마무리입니다. 도전 2-3를 끝낸 뒤 마지막에 합니다.

- **지금은**: 팀장이 「오늘 만든 요청 처리 코드를 저장소에 남겨 달라」고 합니다.
- **그래서 하는 것**: 올라갈 파일을 `git status` 로 먼저 확인하고(비밀 키 파일 `.env` 가 섞이면 안 됩니다), `git add` → `git commit` → `git push` 로 올립니다.
- **끝나면**: 깃허브 저장소의 `access_control` 폴더에서 오늘 만든 파일이 모두 보입니다.

**순서**

1. **[터미널]** `security-agent-toolkit` 폴더로 옮기고 위치를 확인합니다. 결과가 `…/security-agent-toolkit` 으로 끝나야 합니다.
   ```bash
   cd ..
   pwd
   ```
   - 명령 풀이: `cd ..` 한 단계 위 폴더로 이동 · `pwd` 지금 위치 확인
   - 결과가 다르면 VS Code 왼쪽 목록에서 `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 새로 엽니다. 새로 연 뒤 `pwd` 를 한 번 더 쳐서 확인합니다.
2. **[터미널]** 무엇이 바뀌었는지 먼저 봅니다. 빨간 목록에 `.env` 나 `.venv` 가 보이면 올리지 않고 멈춥니다.
   ```bash
   git status
   ```
   - 명령 풀이: `git status` 올릴 파일의 상태를 봄
   - `.env` 가 보이면: VS Code 왼쪽 목록에서 `security-agent-toolkit` 바로 아래의 `.gitignore` 를 열어 맨 아래에 `.env` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. `.venv` 도 같은 방법으로 합니다.
   - Unit 1에서 `access_control` 을 이미 올렸다면 오늘 새로 만든 파일이 `access_control/req_create.py` 처럼 한 줄씩 보입니다. Unit 1에서 올리지 않았다면 `access_control/` 한 줄로 보일 수 있습니다. 어느 쪽이든 `Untracked files:` 아래에 보이는 줄을 센 그대로 적습니다.
   - `access_control/requests.json` 은 도전 2-3에서 프로그램이 만든 이력 파일입니다. 이것도 올라갑니다.
   - `access_control/__pycache__/` 가 보이면 `.gitignore` 맨 아래에 `__pycache__/` 한 줄을 적고 저장한 뒤 `git status` 를 다시 칩니다. 줄 수는 그 뒤에 다시 셉니다.
3. **[보고서]** `report_u2.md` 의 `## 마무리` 아래를 채웁니다. 올리기 전에 채워야 깃허브에 빈칸 없이 올라갑니다.
   - (가) `git status` 를 쳤을 때 `Untracked files:` 아래에 줄이 몇 개 보였는지, 그중에 `.env` 나 `.venv` 가 있었는지 적어 주세요.
   - 앞 실습에서 못 적은 보고서 칸이 있으면 `모름 — 막힌 곳: …` 으로 적고 올립니다. 올린 뒤에 이어서 적어 다시 올려도 됩니다.
4. **[터미널]** 바뀐 파일을 모두 담고(`add`), 기록하고(`commit`), 올립니다(`push`).
   ```bash
   git add .
   git commit -m "Add access control day 3 request, approval, grant, SLA and history"
   git push
   ```
   - 명령 풀이: `git add .` 바뀐 파일을 올릴 목록에 담음 · `git commit -m "…"` 따옴표 안의 설명을 붙여 기록으로 저장 · `git push` 깃허브로 올림
   - `git push` 가 거절(`rejected`)되면 깃허브에 내 PC 에 없는 기록이 있다는 뜻입니다. `git pull` 을 입력해 받아 온 뒤 `git push` 를 다시 합니다
   - `git pull` 뒤에 편집기 화면이 뜨면 `Esc` 를 누르고 `:wq` 를 입력한 뒤 `Enter` 를 누릅니다
5. **[브라우저]** 깃허브의 내 저장소를 새로 고쳐 `access_control` 폴더를 열고, 터미널에서 `ls access_control` 로 본 파일들이 깃허브에도 보이는지 확인합니다. `__pycache__` 폴더는 없어도 됩니다.
   - 빠진 이름이 있으면 터미널에서 `ls access_control` 로 내 PC 에 있는지 봅니다. 없으면 다른 폴더에 만든 것이니 `access_control` 안으로 옮기고 1 ~ 4번을 다시 합니다.

## 마무리 정리

| 하려는 일 | 코드 · 말 |
|---|---|
| 올릴 파일 확인 | `git status` (`.env` · `.venv` 가 보이면 멈춤) |
| 올리기 | `git add .` → `git commit -m "…"` → `git push` |
| 올린 뒤 | 브라우저에서 파일이 모두 있는지 확인 |

---

## 이번 Unit 마무리

| 확인 | 문제 |
|---|---|
| 요청을 요청서로 접수하고 접수 못 할 요청을 걸러 냈다 | 실습 2-1 |
| 승인 · 반려가 검토 중인 요청서에만 되게 했다 | 실습 2-2 |
| 승인된 요청서를 정책으로 확인하고 예외 권한을 부여했다 | 도전 2-1 |
| 처리 기한을 초과한 요청서를 시간 계산으로 찾았다 | 도전 2-2 |
| 요청서 전체를 `requests.json` 으로 저장하고 상태별 건수를 셌다 | 도전 2-3 |
| 오늘 만든 파일과 보고서를 깃허브에 올렸다 | 마무리 |

다음 Unit(Unit 3)에서는 부여된 권한 가운데 쓰이지 않는 것 · 넘치는 것을 찾는 과다권한 탐지를 합니다. 오늘 만든 `requests.json` 이 그때 「누가 어떤 권한을 요청해 받았나」를 보는 자료입니다.

---

<!-- learn:answers -->
