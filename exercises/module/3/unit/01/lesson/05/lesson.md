---
id: m3-u01-l05
title: 제공 파일
render: markdown
---

# 제공 파일

## `exception_policy.py` 만들기

**`exception_policy.py`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.

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
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. EXCEPTIONS 에서 예외 exception 를 하나씩 꺼낸다
    # 2.   exception 의 "user" 가 user 와 같고 "permission" 이 permission 과 같으면
    # 3.     exception 의 "expires" 를 TIME_FORMAT 으로 시각으로 바꿔 expires 에 담는다
    # 4.     now 가 expires 보다 앞이면 True 와 exception 의 "id" 를 리턴한다
    # 5. 반복이 끝날 때까지 못 찾았으면 False, None 을 리턴한다
```

## `config_loader.py` 만들기

**`config_loader.py`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.

```python
import json                                                      # JSON 파일을 읽는 모듈을 불러온다


def load_json(path, default):                                    # 파일 경로와 실패했을 때 쓸 기본값을 받는 함수
    """JSON 파일을 읽어 리턴하고, 파일이 없거나 깨졌으면 경고를 출력하고 default 를 리턴한다.
    설정 파일을 읽을 때마다 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. try: 로 시작한다
    # 2.   with open(path, encoding="utf-8") as input_file: 로 path 를 열어
    # 3.     json.load 로 읽은 내용을 바로 리턴한다
    # 4. except FileNotFoundError: 로 파일이 없을 때를 받는다
    # 5.   "[경고] 설정 파일 없음:" 과 path 를 출력하고
    # 6.   default 를 리턴한다
    # 7. except json.JSONDecodeError: 로 JSON 이 깨졌을 때를 받는다
    # 8.   "[경고] 설정 파일 깨짐:" 과 path 를 출력하고
    # 9.   default 를 리턴한다
```
