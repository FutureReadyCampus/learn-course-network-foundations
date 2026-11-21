---
id: m3-u05-l03
title: 제공 파일
render: markdown
---

# 제공 파일

## 제공 파일 쓰는 법

**실습 5-1을 마친 뒤, 실습 5-2를 시작하기 전에** 이 레슨의 파일 세 개를 만들고 주간 보고서를 한 번 만들어 봅니다. 로그를 집계하는 함수는 도전 5-1에서 직접 쓰는 것이라, 오늘은 완성본을 받아 씁니다.

1. 파일은 모두 `access_control` 폴더 바로 아래에 만듭니다. 만드는 방법은 실습 5-1과 같습니다(VS Code 왼쪽 목록에서 `access_control` 폴더를 오른쪽 클릭 › **New File**).
2. 아래 코드 상자의 **복사** 버튼을 눌러 내용을 그대로 붙여 넣고 저장합니다. 고칠 곳은 없습니다.
3. 만들 파일은 세 개입니다.

   | 파일 | 들어 있는 것 | 하는 일 |
   |---|---|---|
   | `log_summary.py` | 함수 다섯 개 | 로그를 읽고, 거부된 요청을 모으고, 값별로 세고, 거부율을 구함 |
   | `weekly_report.py` | 함수 두 개 | 점검 결과와 로그 집계를 합쳐 보고서 문자열을 만들고 파일로 저장함 |
   | `weekly_run.py` | 실행 파일 | 위 두 파일과 실습 5-1의 `checklist.py` 를 불러 주간 보고서를 만듦 |

4. `weekly_run.py` 는 실습 5-1의 `checklist.py` 를 불러옵니다. `python exercise5-1_run.py` 가 정답 레슨 「실습 5-1 정답」의 출력과 같은 출력을 내는지 먼저 확인합니다. 아직 안 되면 정답 레슨의 「실습 5-1 정답」에 있는 채운 코드를 넣어 `checklist.py` 를 완성합니다.
5. 데이터 파일 `config/week_state.json` · `config/alert.json` · `week_log.jsonl` 은 시작하기 레슨에서 만든 것을 그대로 씁니다.

> 시간이 남아 도전 5-1을 하면, `log_summary.py` 를 빈칸이 있는 골격으로 바꿔 직접 써 봅니다. 그때는 다 채울 때까지 `weekly_run.py` 가 동작하지 않으니, 다 쓴 뒤 `weekly_run.py` 를 다시 실행해 보고서가 같은지 확인합니다.

## `log_summary.py` 만들기

**`log_summary.py`** 를 만들고 아래 내용을 붙여 넣습니다. 서버 로그를 읽고 세는 함수 다섯 개가 들어 있습니다.

```python
import json                                                      # JSON 문자열을 딕셔너리로 바꾸는 모듈을 불러온다


def read_log(path):                                              # 로그 파일 경로를 받는 함수
    """서버 로그 파일을 한 줄씩 읽어 요청 딕셔너리 리스트로 만든다.
    주간 로그를 집계하기 전에 파일을 읽을 때 쓴다.
    """
    entries = []                                                 # 요청 딕셔너리를 모을 리스트
    with open(path, encoding="utf-8") as log_file:                      # 파일을 연다
        for line in log_file:                                           # 파일에서 한 줄씩 꺼낸다
            entry = json.loads(line)                             # JSON 한 줄을 딕셔너리로 바꾼다
            entries.append(entry)                                # 요청 리스트에 추가한다
    return entries                                               # 요청 리스트를 리턴한다


def count_by(entries, key):                                      # 요청 리스트와 센 기준(키 이름)을 받는 함수
    """요청을 key 의 값별로 세어 {값: 횟수} 딕셔너리를 리턴한다.
    사용자별 · 이유별로 몇 번인지 알고 싶을 때 쓴다.
    예: count_by(entries, "user")
    """
    counts = {}                                                  # 값별 횟수를 담을 딕셔너리
    for entry in entries:                                        # 요청을 하나씩 꺼낸다
        value = entry[key]                                       # 이 요청의 기준 값을 꺼낸다
        old_count = counts.get(value, 0)                         # 지금까지 센 횟수를 꺼낸다(처음이면 0)
        counts[value] = old_count + 1                            # 횟수를 1 늘려 넣는다
    return counts                                                # 값별 횟수를 리턴한다


def filter_denied(entries):                                      # 요청 리스트를 받는 함수
    """거부된 요청만 모아 리스트로 리턴한다.
    거부 사유와 사용자를 따로 볼 때 쓴다.
    """
    denied = []                                                  # 거부된 요청을 모을 리스트
    for entry in entries:                                        # 요청을 하나씩 꺼낸다
        if not entry["allowed"]:                                 # 거부된 요청이면
            denied.append(entry)                                 # 거부 리스트에 추가한다
    return denied                                                # 거부된 요청 리스트를 리턴한다


def deny_rate(entries):                                          # 요청 리스트를 받는 함수
    """전체 요청 중 거부된 요청의 비율(0 ~ 1)을 리턴한다.
    주간 보고서에서 거부율을 구할 때 쓰며, 요청이 없으면 0.0 이다.
    """
    total = len(entries)                                         # 전체 요청 수
    if total == 0:                                               # 요청이 하나도 없으면
        return 0.0                                               # 0.0 을 리턴한다(0 으로 나누지 않는다)
    denied_entries = filter_denied(entries)                      # 거부된 요청 리스트
    denied = len(denied_entries)                                 # 거부된 요청 수
    return denied / total                                        # 거부 수를 전체 수로 나눈 비율을 리턴한다


def find_heavy_users(denied_counts, limit):                      # 사용자별 거부 횟수 딕셔너리와 기준 횟수를 받는 함수
    """거부 횟수가 limit 이상인 사용자 이름 리스트를 리턴한다.
    거부가 한 사람에게 몰렸는지 확인할 때 쓴다.
    """
    heavy = []                                                   # 기준에 걸린 사용자 이름을 모을 리스트
    for user, count in denied_counts.items():                    # 사용자 이름과 거부 횟수를 하나씩 꺼낸다
        if count >= limit:                                       # 거부 횟수가 기준 이상이면
            heavy.append(user)                                   # 사용자 이름을 추가한다
    return heavy                                                 # 기준에 걸린 사용자 이름을 리턴한다
```

| 함수 | 하는 일 |
|---|---|
| `read_log` | 로그 파일의 JSON 한 줄을 딕셔너리 하나로 바꿔 리스트에 모음 |
| `count_by` | `count_by(entries, "user")` 처럼 키 이름을 주면 그 값별로 몇 번인지 셈 |
| `filter_denied` | 거부된 요청만 모음 |
| `deny_rate` | 거부율을 구함. 요청이 하나도 없으면 0 으로 나누지 않고 `0.0` 을 돌려줌 |
| `find_heavy_users` | 거부 횟수가 기준 이상인 사용자 이름을 모음 |

- 파일 전체를 읽는 `json.load` 와 달리, `json.loads` 는 문자열 하나(여기서는 한 줄)를 받아 딕셔너리로 바꿉니다. 끝의 `s` 는 문자열(string)의 `s` 입니다.
- `count_by` 의 세는 두 줄(`counts.get(value, 0)` 으로 지금까지 센 수를 꺼내고, 1 늘려 다시 넣기)은 Unit 1에서 읽은 모양과 같습니다.

## `weekly_report.py` 만들기

**`weekly_report.py`** 를 만들고 아래 내용을 붙여 넣습니다. 점검 결과와 로그 집계를 합쳐 네 절(`## ` 로 시작하는 제목 하나와 그 아래 줄들)의 보고서 문자열을 만들고, 날짜가 들어간 `.md` 파일로 저장합니다.

```python
from log_summary import count_by, filter_denied, deny_rate, find_heavy_users   # 제공 파일 log_summary.py 의 집계 함수를 불러온다


def build_report(results, entries, alert, today):                # 점검 결과 · 요청 리스트 · 경고 기준 · 날짜 문자열을 받는 함수
    """점검 결과와 로그 집계를 합쳐 주간 보고서 문자열을 만든다.
    매주 정기 보고서를 만들 때 쓴다.
    """
    denied = filter_denied(entries)                              # 거부된 요청만 모은다
    total = len(entries)                                         # 전체 요청 수
    denied_count = len(denied)                                   # 거부된 요청 수
    allowed_count = total - denied_count                         # 허용된 요청 수
    rate = deny_rate(entries)                                    # 거부율(0 ~ 1)을 구한다
    percent = round(rate * 100)                                  # 거부율을 퍼센트 숫자로 바꾼다
    limit = alert["deny_rate_limit"]                             # 거부율 경고 기준(0 ~ 1)
    limit_percent = round(limit * 100)                           # 경고 기준을 퍼센트 숫자로 바꾼다
    status = "경고 없음"                                          # 먼저 경고 없음으로 둔다
    if rate >= limit:                                            # 거부율이 기준 이상이면
        status = "경고"                                           # 경고로 바꾼다
    user_limit = alert["user_denied_limit"]                      # 사용자별 거부 횟수 기준
    user_counts = count_by(denied, "user")                       # 거부된 요청을 사용자별로 센다
    heavy = find_heavy_users(user_counts, user_limit)            # 기준 이상 거부된 사용자를 찾는다

    lines = [f"# 접근통제 주간 보고서 ({today})", ""]            # 보고서 줄을 모을 리스트(제목과 빈 줄로 시작)
    lines.append("## 1. 요청 현황")                                # 첫째 절 제목
    lines.append(f"- 전체 요청: {total}건 (허용 {allowed_count}건 · 거부 {denied_count}건)")   # 요청 수
    lines.append(f"- 거부율: {percent}% (경고 기준 {limit_percent}%) -> {status}")             # 거부율과 경고 여부
    lines.append("")                                             # 빈 줄
    lines.append("## 2. 거부 사유")                                # 둘째 절 제목
    reason_counts = count_by(denied, "reason")                   # 거부된 요청을 사유별로 센다
    for reason, count in reason_counts.items():                  # 사유와 횟수를 하나씩 꺼낸다
        lines.append(f"- {reason}: {count}건")                    # 사유별 횟수를 추가한다
    lines.append("")                                             # 빈 줄
    lines.append("## 3. 점검 결과")                                # 셋째 절 제목
    for result in results:                                       # 점검 결과를 하나씩 꺼낸다
        name = result["name"]                                    # 점검 이름
        problems = result["problems"]                            # 문제가 있는 사용자 · 예외 리스트
        if len(problems) == 0:                                   # 문제가 없으면
            lines.append(f"- {name}: 통과")                       # 통과라고 추가한다
        else:                                                    # 문제가 있으면
            lines.append(f"- {name}: 실패 {problems}")            # 실패와 문제 리스트를 추가한다
    lines.append("")                                             # 빈 줄
    lines.append("## 4. 조치가 필요한 것")                          # 넷째 절 제목
    lines.append(f"- 거부 {user_limit}번 이상 사용자: {heavy}")     # 기준 이상 거부된 사용자
    for result in results:                                       # 점검 결과를 하나씩 꺼낸다
        name = result["name"]                                    # 점검 이름
        problems = result["problems"]                            # 문제가 있는 사용자 · 예외 리스트
        if len(problems) > 0:                                    # 문제가 있으면
            lines.append(f"- 확인: {name} -> {problems}")         # 확인할 것을 추가한다
    return "\n".join(lines) + "\n"                               # 줄들을 줄바꿈으로 이어 붙인 문자열을 리턴한다


def save_report(text, today):                                    # 보고서 문자열과 날짜 문자열을 받는 함수
    """보고서를 날짜가 들어간 .md 파일로 저장하고 파일 이름을 리턴한다.
    주간 보고서를 파일로 남길 때 쓴다.
    """
    file_name = f"access_control_weekly_report_{today}.md"       # 날짜가 들어간 파일 이름을 만든다
    with open(file_name, "w", encoding="utf-8") as report_file:            # 파일을 쓰기 모드("w")로 연다
        report_file.write(text)                                            # 보고서 문자열을 파일에 쓴다
    return file_name                                             # 저장한 파일 이름을 리턴한다
```

읽어 둘 곳은 세 곳입니다.

1. `if rate >= limit:` 는 거부율이 경고 기준 이상인지 보는 비교입니다. 거부율은 0 ~ 1 사이 소수이고, 경고 기준도 같은 소수입니다. 퍼센트(`round(rate * 100)`)는 보여 줄 때만 씁니다. `round(숫자)` 는 가장 가까운 정수로 반올림합니다(0.4 × 100 → 40).
2. 보고서 줄은 `lines.append(…)` 로 하나씩 모으고, 마지막에 `"\n".join(lines)` 로 줄바꿈을 넣어 한 문자열로 만듭니다.
3. `save_report` 는 파일을 `"w"`(새로 쓰기)로 엽니다. 로그처럼 계속 덧붙이는 파일은 `"a"` 로 열지만, 매주 새로 만드는 보고서는 `"w"` 입니다. 파일 이름에는 `f"…{today}.md"` 로 날짜를 넣습니다.

## 주간 보고서 만들기

**`weekly_run.py`** 를 만들고 아래 내용을 붙여 넣습니다. 실습 5-1의 점검 결과와 일주일 치 로그를 모아 보고서를 만들고 저장합니다.

```python
import json                                                      # 경고 기준 파일을 읽는 데 쓴다
from datetime import datetime                                    # 문자열을 시각으로 바꾸는 데 쓴다
from checklist import TIME_FORMAT, load_state, run_checklist     # 실습 5-1에서 만든 점검 함수를 불러온다
from log_summary import read_log                                 # 제공 파일의 로그 읽기 함수를 불러온다
from weekly_report import build_report, save_report             # 제공 파일의 보고서 함수를 불러온다

TODAY = "2026-11-02"                                             # 보고서 날짜
NOW = datetime.strptime(TODAY + " 10:00", TIME_FORMAT)           # 점검하는 시각
with open("config/alert.json", encoding="utf-8") as alert_file:           # 경고 기준 파일을 연다
    ALERT = json.load(alert_file)                                         # 경고 기준 딕셔너리로 읽는다

print("--- 단계 1: 모으기 - 점검 결과와 요청 로그")                    # 단계 1 시작을 알리는 줄
state = load_state("config/week_state.json")                     # 점검할 데이터 파일을 읽는다
results = run_checklist(state, NOW)                              # 점검 세 가지를 실행한다
entries = read_log("week_log.jsonl")                             # 요청 로그를 읽는다
result_count = len(results)                                      # 점검이 몇 가지인지 센다
entry_count = len(entries)                                       # 요청이 몇 건인지 센다
print("점검", result_count, "가지 · 요청", entry_count, "건")    # 모은 양을 출력한다
print("--- 단계 2: 보고서 만들기와 저장")                              # 단계 2 시작을 알리는 줄
text = build_report(results, entries, ALERT, TODAY)              # 보고서 문자열을 만든다
file_name = save_report(text, TODAY)                             # 파일로 저장한다
print("저장한 파일:", file_name)                                    # 저장한 파일 이름을 출력한다
print("--- 단계 3: 저장한 보고서 내용")                                # 단계 3 시작을 알리는 줄
print(text)                                                      # 보고서 내용을 출력한다
```

1. **[터미널]** `pwd` 의 결과가 `access_control` 로 끝나는지 확인하고 실행합니다(맥북은 `python3`).
   ```bash
   python weekly_run.py
   ls
   ```
2. 출력은 세 단계입니다. 단계 3에 보고서가 네 절로 나오고, `ls` 에 `access_control_weekly_report_2026-11-02.md` 가 보이면 됩니다.

실행 결과:

```
--- 단계 1: 모으기 - 점검 결과와 요청 로그
점검 3 가지 · 요청 40 건
--- 단계 2: 보고서 만들기와 저장
저장한 파일: access_control_weekly_report_2026-11-02.md
--- 단계 3: 저장한 보고서 내용
# 접근통제 주간 보고서 (2026-11-02)

## 1. 요청 현황
- 전체 요청: 40건 (허용 24건 · 거부 16건)
- 거부율: 40% (경고 기준 30%) -> 경고

## 2. 거부 사유
- 역할이 없음: 3건
- 업무 시간 밖: 4건
- 퇴사한 계정: 4건
- 허용되지 않은 접속 위치: 5건

## 3. 점검 결과
- 퇴사자 계정 점검: 실패 ['dami']
- 만료 예외 점검: 통과
- 부서와 역할 점검: 실패 ['junho']

## 4. 조치가 필요한 것
- 거부 4번 이상 사용자: ['dami', 'gaeun']
- 확인: 퇴사자 계정 점검 -> ['dami']
- 확인: 부서와 역할 점검 -> ['junho']
```

| 절 | 담긴 것 |
|---|---|
| 1절 | 일주일 동안의 요청 수와 거부율 |
| 2절 | 거부 사유별 횟수 |
| 3절 | 실습 5-1의 점검 결과 |
| 4절 | 담당자가 먼저 볼 것 |

- 거부율 40% 는 거부 16건 ÷ 전체 40건 = 0.4 이고, 경고 기준 0.3 이상이라 「경고」입니다.
- 4절의 `['dami', 'gaeun']` 은 거부가 `alert.json` 의 기준 4번 이상인 사람입니다(dami 4번, gaeun 5번).
- VS Code 왼쪽 목록에서 `access_control_weekly_report_2026-11-02.md` 를 열면 같은 내용이 파일로 저장된 것을 볼 수 있습니다.

오류가 나면 아래 표를 봅니다.

| 오류 | 원인 |
|---|---|
| `ModuleNotFoundError: No module named 'checklist'` | `checklist.py` 가 같은 폴더에 없음 |
| `IndentationError` | `checklist.py` 의 직접 쓰는 곳이 아직 비어 있음 |

- 이 보고서는 실습 5-2의 상황 8에서 다시 읽습니다. 숫자가 어떻게 나왔는지 직접 세어 보고 싶으면 도전 5-1을 합니다.
