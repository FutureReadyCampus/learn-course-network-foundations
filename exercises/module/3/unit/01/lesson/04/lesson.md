---
id: m3-u01-l04
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

**실습 1-3을 시작하기 전에** 이 레슨의 파일 세 개를 만듭니다. 실습 1-3의 `policy.py` 가 예외 판정 함수 `find_exception` 을 불러 쓰는데, 그 함수와 예외 파일은 도전 1-3에서 만드는 것이라 오늘은 완성본을 받아 씁니다.

1. 파일은 모두 `access_control` 폴더 안에 만듭니다. 만드는 방법은 실습 1-2와 같습니다(VS Code 왼쪽 목록에서 `access_control` 폴더를 고르고 **새 파일** 아이콘).
2. 아래 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 만들 파일은 세 개입니다.
   1. `config/exceptions.json`: 사용자 한 명에게 기간을 정해 따로 허용한 권한(예외) 다섯 건
   2. `exception_policy.py`: 지금 시각에 유효한 예외가 있는지 찾는 함수 `find_exception`
   3. `config_loader.py`: 설정 파일이 없거나 깨져도 멈추지 않고 빈 설정을 돌려주는 함수 `load_json` (오늘 실습에서는 쓰지 않고, 다음 Unit부터 씁니다)
4. 세 파일을 다 만들었으면 터미널에서 `ls` 와 `ls config` 로 파일 이름이 보이는지 확인하고 실습 1-3으로 돌아갑니다.

> 시간이 남아 도전 1-3이나 도전 1-4를 하면, 이 파일들을 빈칸이 있는 골격으로 바꿔 직접 써 봅니다. 그때는 본문을 다 채울 때까지 실습 1-3이 동작하지 않으니, 다 쓴 뒤 `exercise1-3_run.py` 를 다시 실행해 결과가 같은지 확인합니다.

## `config/exceptions.json` 만들기

**`config/exceptions.json`** 을 만들고 아래 내용을 붙여 넣습니다. 한 줄이 예외 한 건이고, 누구에게 · 어떤 권한을 · 언제까지(`expires`) · 왜 주었는지 적혀 있습니다.

<pre class="copyable"><code>[
  {"id": 1, "user": "seoyeon", "permission": "SETTLE:QUERY", "expires": "2026-10-22 18:00", "reason": "월말 정산 대조 지원"},
  {"id": 2, "user": "junho", "permission": "SALES:CHANGE", "expires": "2026-10-20 18:00", "reason": "영업 실적 정정"},
  {"id": 3, "user": "dami", "permission": "SALES:QUERY", "expires": "2026-10-31 18:00", "reason": "인수인계"},
  {"id": 4, "user": "batch-night", "permission": "SALES:QUERY", "expires": "2026-10-23 09:00", "reason": "분기 집계 시험"},
  {"id": 5, "user": "gaeun", "permission": "SETTLE:QUERY", "expires": "2026-10-22 12:00", "reason": "감사 자료 대응"}
]
</code></pre>

- 저장한 뒤 터미널에서 JSON 규칙에 맞는지 확인합니다. 다섯 건이 다시 정리되어 나오면 됩니다.
  ```bash
  python -m json.tool config/exceptions.json
  ```
  - 명령 풀이: `python -m json.tool` 파이썬의 JSON 검사 도구를 실행 · `config/exceptions.json` 검사할 파일 (맥북은 `python3`)

## `exception_policy.py` 만들기

**`exception_policy.py`** 를 만들고 아래 내용을 붙여 넣습니다. 다른 파일이 `import` 로 이 파일을 불러올 때 `config/exceptions.json` 을 한 번 읽어 `EXCEPTIONS` 에 담고, `find_exception` 은 사람과 권한이 같고 지금 시각이 만료 시각보다 앞인 예외를 찾습니다.

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

## `config_loader.py` 만들기

**`config_loader.py`** 를 만들고 아래 내용을 붙여 넣습니다. 오늘 실습에서는 불러 쓰지 않지만, 다음 Unit부터 설정 파일을 읽을 때 이 함수를 씁니다. 미리 만들어 둡니다.

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

- 모두 만들었으면 터미널에서 확인합니다. `exception_policy.py` · `config_loader.py` 와 `config` 안의 `exceptions.json` 이 보이면 실습 1-3으로 갑니다.
  ```bash
  ls
  ls config
  ```
