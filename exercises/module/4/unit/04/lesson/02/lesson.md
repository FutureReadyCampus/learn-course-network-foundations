---
id: m4-u04-l02
title: 위험 점수 실습 입력 준비
render: markdown
---

# 위험 점수 실습 입력 준비

## 핵심 실습에 필요한 입력

실습 4-1은 서버 로그에서 Module 3 Unit 3 실습 3-2의 탐지 결과를 가져오고, 아래 여섯 신호를 고정 시나리오 입력으로 함께 점수화합니다. 이 여섯 신호는 선택 응용에서 생성하는 결과가 아닙니다. 지정된 시나리오 행을 입력으로 미리 정리한 것으로, 각 행에 근거 위치를 설명해 두었습니다.

`anomaly_detection` 폴더에 **`risk_inputs.json`** 파일을 만들고 아래 내용을 붙여 넣습니다. `entity` 와 `rule` 은 점수 계산에 쓰고, `origin` 과 `evidence` 는 시나리오 입력의 출처를 이해하기 위한 설명입니다.

```json
[
  {
    "entity": "jiwoo",
    "rule": "업무 시간 밖 로그인",
    "origin": "SaaS 로그인 시나리오 행",
    "evidence": "02:14 로그인 시도"
  },
  {
    "entity": "jiwoo",
    "rule": "평소와 다른 IP",
    "origin": "SaaS 로그인 시나리오 행",
    "evidence": "평소 IP와 다른 주소에서 로그인 시도"
  },
  {
    "entity": "seoyeon",
    "rule": "평소와 다른 IP",
    "origin": "SaaS 로그인 시나리오 행",
    "evidence": "평소 IP와 다른 주소에서 로그인"
  },
  {
    "entity": "seoyeon",
    "rule": "대량 다운로드",
    "origin": "SaaS 파일 활동 시나리오 행",
    "evidence": "짧은 시간에 파일 5개 이상 다운로드"
  },
  {
    "entity": "198.51.100.90",
    "rule": "경로 스캔",
    "origin": "웹 요청 시나리오 행",
    "evidence": "민감 경로를 연속 요청"
  },
  {
    "entity": "gaeun",
    "rule": "여러 로그 연결",
    "origin": "서버·SaaS·웹 시나리오 행의 고정 요약",
    "evidence": "서로 다른 로그 3종류가 41분 안에 나타남"
  }
]
```

**확인** — 파일을 저장한 뒤 JSON 문법 오류 표시가 없고, 여섯 개 객체가 보이면 준비됐습니다. 실습 4-1에서 이 입력을 서버 로그의 핵심 탐지 결과와 합칩니다. SaaS·웹 탐지기나 로그 연결 코드를 직접 작성하는 선택 응용은 필요하지 않습니다.

<!-- checklist -->
- [ ] `anomaly_detection/risk_inputs.json` 에 위 여섯 시나리오 입력을 저장했다
<!-- /checklist -->

## Unit 3 파일이 없을 때 `access_detection.py`

시작하기 레슨의 확인에서 `Unit 3 파일 정상 57` 이 나왔다면 **이 페이지는 건너뜁니다.** Unit 3 실습 3-2에서 직접 만든 파일을 그대로 씁니다.

`No module named 'access_detection'` 이나 `ImportError` 가 나왔다면 `anomaly_detection` 폴더에 **`access_detection.py`** 를 만들고 아래 내용을 붙여 넣습니다. Unit 3 실습 3-2의 완성본입니다. 판정 서버가 거절한 요청 가운데 3번 이상 반복된 사용자를 고르고, Module 3에서 만든 권한 판정 `check_permission` 으로 다시 판정해 이유를 붙입니다.

```python
import pandas as pd                                   # 판다스를 pd 라는 짧은 이름으로 불러온다
from rbac import check_permission                     # Module 3(접근통제)에서 만든 권한 판정 함수를 불러온다

EVENTS_PATH = "normalized_events.json"                # 읽을 정규화 이벤트 파일 이름
REPEAT_LIMIT = 3                                      # 한 사용자의 실패가 이 횟수 이상이면 먼저 확인한다
PRIORITY = {"퇴사한 계정": 1, "권한 없음": 2, "허용": 3}  # 판정 이유별로 우선순위(작을수록 먼저)


def load_events(path):                                # 파일 경로를 받는 함수
    """이벤트 파일을 표로 읽는다.
    분석을 시작할 때 맨 먼저 쓴다.
    """
    events = pd.read_json(path)                       # 파일 속 이벤트를 표 한 개로 읽는다
    return events                                     # 이벤트 표를 리턴한다


def pick_server_failures(events):                     # 이벤트 표를 받는 함수
    """판정 서버 로그에서 실패한 이벤트만 골라 새 표로 만든다.
    서버가 거절한 요청을 조사하기 전에 쓴다.
    """
    sources = events["source"]                        # source 열만 꺼낸다
    is_server = sources == "server"                   # 각 행이 판정 서버 이벤트인지 비교해 True 또는 False 를 만든다
    results = events["result"]                        # result 열만 꺼낸다
    is_fail = results == "실패"                       # 각 행이 실패인지 비교해 True 또는 False 를 만든다
    both_true = is_server & is_fail                   # 두 조건이 모두 True 인 행만 True 로 만든다
    server_failures = events[both_true]               # True 인 행만 골라 새 표로 만든다
    return server_failures                            # 서버 실패 이벤트 표를 리턴한다


def pick_suspicious(server_failures):                 # 서버 실패 표를 받는 함수
    """실패가 반복된 사용자의 이벤트만 골라 새 표로 만든다.
    같은 사용자가 여러 번 거절당했는지 볼 때 쓴다.
    """
    users = server_failures["user"]                   # user 열만 꺼낸다
    user_counts = users.value_counts()                # 사용자마다 실패가 몇 번인지 센다
    is_many = user_counts >= REPEAT_LIMIT             # 사용자마다 실패 횟수가 REPEAT_LIMIT 이상인지 비교해 True 또는 False 를 만든다
    repeated_users = user_counts[is_many]             # 반복된 사용자와 횟수만 남긴다

    repeated_names = repeated_users.index             # 반복된 사용자의 이름들(인덱스)을 꺼낸다
    is_repeated_user = users.isin(repeated_names)     # 각 행의 사용자가 반복된 사용자 이름 안에 있는지 구해 True 또는 False 를 만든다
    suspicious = server_failures[is_repeated_user]    # True 인 행만 골라 새 표로 만든다
    return suspicious                                 # 먼저 확인할 실패 이벤트 표를 리턴한다


def judge_failure(user, action):                      # 사용자와 행동을 받는 함수
    """서버가 거절한 요청을 Module 3(접근통제) 권한 규칙으로 다시 판정해 이유와 우선순위를 리턴한다.
    거절이 규칙대로인지 확인할 때 쓴다.
    """
    parts = action.split(":")                         # ":" 로 나눠 두 조각의 리스트로 만든다
    resource = parts[0]                               # 첫 번째 조각이 자원이다
    permission_action = parts[1]                      # 두 번째 조각이 행위이다

    is_allowed, reason = check_permission(user, resource, permission_action)  # Module 3(접근통제) 판정 결과를 허용 여부와 이유로 나눠 받는다
    priority = PRIORITY.get(reason, 4)                # 이유의 우선순위를 꺼낸다(없으면 4)
    return reason, priority                           # 판정 이유와 우선순위를 리턴한다
```

- 이 파일은 `rbac.py` 와 `normalized_events.json` · `config/users.json` · `config/roles.json` 이 있어야 동작합니다. 없으면 Unit 3 시작하기 레슨의 코드 상자로 먼저 만듭니다.

**확인** — 시작하기 레슨의 확인 명령을 다시 쳐서 `Unit 3 파일 정상 57` 이 나오면 성공입니다. `No module named 'rbac'` 이 나오면 Unit 3 시작하기 레슨의 코드 상자로 `rbac.py` 를 먼저 만듭니다.

<!-- checklist -->
- [ ] `Unit 3 파일 정상 57` 이 이미 나왔거나, `anomaly_detection` 폴더에 `access_detection.py` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

---
