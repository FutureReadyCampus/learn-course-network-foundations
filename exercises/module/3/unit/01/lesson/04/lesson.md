---
id: m3-u01-l04
title: 예외 판정 준비
render: markdown
---

# 예외 판정 준비

## 예외 판정에 필요한 준비

실습 1-3에서는 기본 역할에 없는 권한이라도, 기간을 정해 허용한 예외가 있는지 확인합니다. 이 레슨에서는 예외 목록과 예외를 찾는 함수를 준비합니다. 다음 Unit에서 사용할 설정 읽기 함수도 함께 만듭니다. 아래 내용을 복사해 저장하면 실습 1-3을 이어서 진행할 수 있습니다.

**예외**는 「이번 주 금요일까지만 과학실 열쇠를 빌려주기」처럼, 역할에는 없는 권한을 한 사람에게만 기간을 정해 잠깐 주는 것입니다.

1. 파일은 모두 작업 폴더 `access_control` 안에 만듭니다. `exception_policy.py` · `config_loader.py` 는 `access_control` 폴더 바로 아래에(VS Code 왼쪽 목록에서 `access_control` 폴더를 고르고 **새 파일** 아이콘, 실습 1-2와 같은 방법), `exceptions.json` 은 `access_control` 폴더 안의 `config` 폴더에(`config` 폴더를 오른쪽 클릭 › **New File**) 만듭니다.
2. 아래 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 만들 파일은 세 개입니다.

   | 파일 | 담긴 것 | 쓰는 때 |
   |---|---|---|
   | `config/exceptions.json` | 사용자 한 명에게 기간을 정해 따로 허용한 권한(예외) 다섯 건 | 실습 1-3 |
   | `exception_policy.py` | 지금 시각에 유효한 예외가 있는지 찾는 함수 `find_exception` | 실습 1-3 |
   | `config_loader.py` | 설정 파일이 없거나 깨져도 멈추지 않고 빈 설정을 돌려주는 함수 `load_json` | 다음 Unit에서 설정을 읽을 때 |

4. 세 파일을 다 만든 뒤 마지막 쪽(「`config_loader.py` 만들기」) 끝에서 터미널로 한꺼번에 확인하고 실습 1-3으로 돌아갑니다.


## `config/exceptions.json` 만들기

`access_control` 폴더 안의 `config` 폴더를 오른쪽 클릭 › **New File** 로 `exceptions.json` 을 만들고(경로 `config/exceptions.json`) 아래 내용을 붙여 넣습니다. 한 줄이 예외 한 건이고, 누구에게 · 어떤 권한을 · 언제까지(`expires`) · 왜 주었는지 적혀 있습니다.

<pre class="copyable"><code>[
  {"id": 1, "user": "seoyeon", "permission": "SETTLE:QUERY", "expires": "2026-10-22 18:00", "reason": "월말 정산 대조 지원"},
  {"id": 2, "user": "junho", "permission": "SALES:CHANGE", "expires": "2026-10-20 18:00", "reason": "영업 실적 정정"},
  {"id": 3, "user": "dami", "permission": "SALES:QUERY", "expires": "2026-10-31 18:00", "reason": "인수인계"},
  {"id": 4, "user": "batch-night", "permission": "SALES:QUERY", "expires": "2026-10-23 09:00", "reason": "분기 집계 시험"},
  {"id": 5, "user": "gaeun", "permission": "SETTLE:QUERY", "expires": "2026-10-22 12:00", "reason": "감사 자료 대응"}
]
</code></pre>

- `reason` 칸의 「월말 정산 대조」는 한 달 동안 오간 돈의 기록이 서로 맞는지 맞춰 보는 일이고, 「인수인계」는 떠나는 사람이 맡던 일을 다음 사람에게 넘겨주는 일입니다.

<!-- checklist -->
- [ ] `config/exceptions.json` 을 만들어 붙여 넣고 저장했다
<!-- /checklist -->

- 저장한 뒤 터미널에서 JSON 규칙에 맞는지 확인합니다. 다섯 건이 다시 정리되어 나오면 성공입니다. `Expecting …` 나 `Unterminated string …` 같은 오류 문구가 나오면 복사가 덜 된 것이니 내용을 지우고 다시 붙여 넣습니다.
  ```bash
  python -m json.tool config/exceptions.json
  ```
  - 명령 풀이: `python -m json.tool` 파이썬의 JSON 검사 도구를 실행 · `config/exceptions.json` 검사할 파일. 한글이 `\uXXXX` 로 보여도 정상입니다

<!-- checklist -->
- [ ] `python -m json.tool config/exceptions.json` 으로 다섯 건이 오류 없이 나왔다
<!-- /checklist -->

## `exception_policy.py` 만들기

`access_control` 폴더 바로 아래에 **`exception_policy.py`** 를 만들고 아래 내용을 붙여 넣습니다. 다른 파일이 `import` 로 이 파일을 불러오면, 맨 위 줄들이 `config/exceptions.json` 을 한 번 읽어 `EXCEPTIONS` 에 담습니다. `find_exception` 은 그 안에서 사람과 권한이 같고 아직 만료 시각이 지나지 않은 예외를 찾습니다.

- `datetime.strptime(문자열, 형식)` 은 `"2026-10-22 18:00"` 같은 글자를 시각 값으로 바꿉니다. 시각 값으로 바꿔야 `now < expires` 처럼 지금 시각과 「더 이른가」를 비교할 수 있습니다.

```python
import json                                                      # JSON 파일을 읽는 모듈을 불러온다
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다

with open("config/exceptions.json", encoding="utf-8") as exceptions_file:      # 예외 파일을 연다
    EXCEPTIONS = json.load(exceptions_file)                                    # 예외 딕셔너리들의 리스트로 읽는다

TIME_FORMAT = "%Y-%m-%d %H:%M"                                   # 만료 시각 문자열의 형식


def find_exception(user, permission, now):                       # 사용자 · "자원:행위" · 지금 시각을 받는 함수
    """now 시각에 유효한 예외가 있으면 (True, 예외 번호)를 리턴한다.
    없으면 (False, None)을 리턴한다.
    역할에 없는 권한을 임시로 허용해도 되는지 확인할 때 쓴다.
    """
    for exception in EXCEPTIONS:                                       # 예외를 하나씩 꺼낸다
        if exception["user"] == user and exception["permission"] == permission:   # 사람과 권한이 같으면
            expires = datetime.strptime(exception["expires"], TIME_FORMAT)  # 만료 시각을 시각으로 바꾸고
            if now < expires:                                    # 아직 만료 전이면
                return True, exception["id"]                           # 유효한 예외와 그 번호를 리턴한다
    return False, None                                           # 못 찾았으면 없다고 리턴한다
```

<!-- checklist -->
- [ ] `access_control` 폴더 바로 아래에 `exception_policy.py` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

## `config_loader.py` 만들기

`access_control` 폴더 바로 아래에 **`config_loader.py`** 를 만들고 아래 내용을 붙여 넣습니다. 오늘 실습에서는 불러 쓰지 않지만, 다음 Unit부터 설정 파일을 읽을 때 이 함수를 씁니다. 미리 만들어 둡니다. 코드의 `try:` 는 「아래를 해 보다가 오류가 나면 `except` 아래로 넘어가라」는 뜻입니다.

```python
import json                                                      # JSON 파일을 읽는 모듈을 불러온다


def load_json(path, default):                                    # 파일 경로와 실패했을 때 쓸 기본값을 받는 함수
    """JSON 파일을 읽어 리턴하고, 파일이 없거나 깨졌으면 경고를 출력하고 default 를 리턴한다.
    설정 파일을 읽을 때마다 쓴다.
    """
    try:                                                         # 아래를 시도한다
        with open(path, encoding="utf-8") as input_file:                  # 파일을 연다
            return json.load(input_file)                                  # 읽은 내용을 바로 리턴한다
    except FileNotFoundError:                                    # 파일이 없으면
        print("[경고] 설정 파일 없음:", path)                      # 경고를 남기고
        return default                                           # 기본값을 리턴한다
    except json.JSONDecodeError:                                 # JSON 이 깨졌으면
        print("[경고] 설정 파일 깨짐:", path)                      # 경고를 남기고
        return default                                           # 기본값을 리턴한다
```

<!-- checklist -->
- [ ] `access_control` 폴더 바로 아래에 `config_loader.py` 를 만들어 붙여 넣고 저장했다
<!-- /checklist -->

- 세 파일을 모두 만들었으면 터미널(`…/access_control` 위치)에서 확인합니다. `ls` 에 `exception_policy.py` · `config_loader.py` 가, `ls config` 에 `exceptions.json` 이 보이고, 마지막 줄에 `준비 완료`가 나오면 성공이고 실습 1-3으로 갑니다. 파일이 안 보이면 다른 폴더에 만든 것이니 VS Code 왼쪽 목록에서 그 파일을 `access_control` 폴더로 끌어 옮깁니다.
  ```bash
  ls
  ls config
  # 이 명령은 전체를 복사해 Git Bash에 붙여 넣어 실행하세요.
  python -c "
  import exception_policy, config_loader
  print('준비 완료')
  "
  ```
  - 명령 풀이: `ls` · `ls config` 폴더 안의 파일 이름을 보여 줌 · `python -c "…"` 따옴표 안의 파이썬을 바로 실행해 두 파일을 불러 와 봄

<!-- checklist -->
- [ ] `python -c "import exception_policy, config_loader; print('준비 완료')"` 를 실행해 `준비 완료`가 나왔다
<!-- /checklist -->
