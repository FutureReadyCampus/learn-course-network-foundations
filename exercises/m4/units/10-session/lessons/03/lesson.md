---
id: m4-u10-l03
title: Exercise 10-2 · pipeline.py 로 탐지부터 보고서까지
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/114_day06_am_ai_summary_pipeline.md
  mission_id: GichanSource.m4-1109-am-ai-summary-pipeline
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# Exercise 10-2 · pipeline.py 로 탐지부터 보고서까지

## 이번에 만들 것: 한 번에 도는 pipeline.py

> **이번 Exercise에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「Unit 6 · 7에서 만든 탐지를 확인하려면 지금은 파일을 하나씩 따로 실행해야 합니다. 순서를 하나 빠뜨리면 점수가 틀리게 나오는데, 틀린 줄도 모르고 보고하게 됩니다.
>
> 명령 한 번으로 읽기부터 점수 저장, 요약, 보고서 저장까지 끝나게 해 주세요. 그리고 AI 가 응답하지 않는 날에도 점수와 등급이 담긴 보고서는 나와야 합니다.」
> - **왜 중요한가**: <mark>단계를 따로 실행하면 순서를 빠뜨리거나 앞 단계의 결과를 잘못 넘길 수 있고, AI 호출 하나가 실패해서 보고서 전체가 만들어지지 않으면 담당자가 아침에 아무것도 볼 수 없습니다.</mark>

> **읽을거리 — 문제가 아닙니다.** 이 아래부터 첫 「문제」 전까지는 이 Exercise의 배경지식입니다. 답할 질문도 따라 칠 명령도 없으니 읽고 이해만 합니다. (판다스 문법 상자의 코드는 눈으로 읽으면 됩니다.)

## 읽기 · 왜 단계 결과를 이어 붙이는가

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

1. 파이프라인은 <mark>앞 단계의 리턴값을 다음 단계에 전달해 이어 가는 구조</mark>입니다. 어느 함수에 무엇을 전달하는지가 이번 Exercise의 핵심입니다.
2. 이번 Exercise의 질문은 하나입니다. <mark>**각 단계의 결과를 다음 단계에 어떻게 넘기고, 한 단계가 실패해도 나머지 결과를 어떻게 남기는가?**</mark>

## 읽기 · 2.1 단계 연결 흐름과 앞에서 만든 파일의 자리

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문은 없습니다. 판다스 문법 상자의 코드는 눈으로 읽으면 됩니다.

```
단계 1  이벤트 읽기               normalized_events.json  →  events (표)
   ↓
단계 2  연결 · 탐지 · 점수         events  →  chains  →  findings  →  totals · reasons  →  records
   ↓                              (records 는 unit05_risk_scores.json 에도 저장)
단계 3  Gemini API 를 활용한 AI 요약                   records  →  summaries   (실패하면 대체 문장)
   ↓
단계 4  보고서 저장               events · findings · records · summaries
                                  →  anomaly_detection_report_2026-11-02.json
```

앞에서 만든 파일 가운데 파이프라인에 들어가는 것과 아직 들어가지 않은 것은 다음과 같습니다.

| 만든 날 | 파일 | 파이프라인에서 |
|---|---|---|
| Unit 2 | `normalized_events.json` | 단계 1 의 입력 |
| Unit 6 | `access_detection.py` · `saas_detection.py` · `malicious_detection.py` | 단계 2 안에서 `collect_findings` 가 호출합니다 |
| Unit 7 | `correlation.py` · `risk_scores.py` | 단계 2 |
| Exercise 10-1 | `event_summary.py` | 단계 3 |
| Unit 4 · 5 | 로그인 · 트래픽 규칙(`login_detection.py` · `traffic_detection.py` · `alerts.py`) | **넣지 않았습니다.** 알림을 `alerts.json` 에 따로 모으는 방식이라 점수 기록과 모양이 다릅니다 |
| Unit 8 | 평가 · 튜닝(`evaluation.py` · `tuning.py` · `final_check.py`) | **넣지 않았습니다.** 입력이 사람이 조사한 결과가 붙은 파일(`review_alerts.json`)이라 이벤트 표가 아닙니다 |

- 이번 파이프라인은 점수 기록 쪽만 이어 붙였습니다. Unit 4 · 5의 알림이나 Unit 8의 평가를 더하려면 입력과 출력의 모양을 맞추는 단계가 필요하고, 현업에서도 이 단계를 따로 만들어 이어 붙입니다.
- 보고서 파일 `anomaly_detection_report_2026-11-02.json` 에 들어가는 키는 다음과 같습니다. 파일 이름의 날짜 `2026-11-02` 는 샘플 이벤트의 날짜입니다.

| 키 | 값 |
|---|---|
| `date` | 샘플 이벤트의 날짜 |
| `event_count` | 읽은 이벤트 수 |
| `source_event_counts` | 로그 종류(`web` · `server` · `saas`)마다 이벤트 수 |
| `finding_count` | 탐지된 규칙 건수 |
| `records` | 대상별 점수 · 등급 · 이유 기록 |
| `summaries` | 대상별 Gemini API 를 활용한 AI 요약(실패하면 대체 문장) |

- 단계 3 이 실패해도 단계 4 가 이어지도록 <mark>요약 함수는 오류를 내지 않고 `FAIL_TEXT` 를 리턴</mark>합니다. 그래서 점수와 등급은 항상 보고서에 들어갑니다.

**판다스 문법 상자 — 시리즈를 딕셔너리로 바꾸기 `시리즈.to_dict()`**

**<mark>`시리즈.to_dict()`</mark> 는 시리즈의 이름(인덱스)을 키로, 값을 값으로 하는 딕셔너리를 만듭니다**

보고서는 JSON 파일로 저장하는데, 판다스의 시리즈는 JSON 으로 바로 저장되지 않습니다. 센 결과(`value_counts()`)를 딕셔너리로 바꿔야 합니다. 과일 이름 다섯 개를 센 예로 익힙니다.

```python
import pandas as pd                                       # 판다스를 pd 라는 짧은 이름으로 불러온다

fruits = pd.Series(["사과", "사과", "배", "사과", "귤"])  # 과일 이름 다섯 개로 시리즈를 만든다
fruit_counts = fruits.value_counts()                      # 이름마다 몇 개인지 센다
print(fruit_counts)                                       # 센 결과를 출력한다
```

실행 결과:

```
사과    3
배     1
귤     1
Name: count, dtype: int64
```

위 코드에 이어서 실행하는 다음 코드입니다.

```python
fruit_count_dict = fruit_counts.to_dict()  # 시리즈를 딕셔너리로 바꾼다
print(fruit_count_dict)                    # 딕셔너리를 출력한다
```

실행 결과:

```
{'사과': 3, '배': 1, '귤': 1}
```

- **읽는 법**:
  - <mark style="background:#bde3ff">`사과` · `배` · `귤` 이 키이고 3 · 1 · 1 이 값</mark>인 딕셔너리가 됩니다.
  - 이 딕셔너리는 `json.dump` 로 저장할 수 있습니다.
- **이번 Exercise에서는**:
  - 과일 이름 대신 로그 종류(`web` · `server` · `saas`)마다 센 이벤트 수에 씁니다.
- **주의**:
  - <mark style="background:#ffc4d6">`json.dump` 에 시리즈를 그대로 전달하면 `TypeError` 오류가 납니다.</mark>
  - `.to_dict()` 는 괄호까지 써야 합니다.

**한 장 정리**

| 함수 | 받는 것 | 리턴하는 것 |
|---|---|---|
| `analyze_events` | 이벤트 표 | 탐지된 규칙 리스트 · 점수 기록 리스트 |
| `summarize_records` | 점수 기록 리스트 | 요약 리스트(미리 채움) |
| `count_failed` | 요약 리스트 | 실패한 요약 수(미리 채움) |
| `build_report` | 이벤트 표 · 탐지된 규칙 · 점수 기록 · 요약 | 보고서 딕셔너리 |
| `save_report` | 보고서 · 파일 경로 | 없음(파일에 저장, 미리 채움) |
| `run_pipeline` | 없음 | 없음(단계마다 결과를 출력, 미리 채움) |

- **직접 쓰는 곳은 일곱 군데**(번호 1 ~ 7)이고, 함수 두 개 안에 나뉘어 있습니다.
  - `analyze_events`(1 ~ 4번): 함수 네 개를 차례로 호출하면서, 앞 함수의 리턴값을 다음 함수에 전달합니다.
  - `build_report`(5 ~ 7번): 로그 종류마다 이벤트 수를 세고(`value_counts`), 딕셔너리로 바꾸고(`to_dict`), 보고서 딕셔너리로 모읍니다.

> **여기부터 문제입니다.** 위는 읽을거리였고, 아래에서 직접 합니다.

## Exercise 10-2 · pipeline.py 로 탐지부터 보고서까지

**이런 상황이 있습니다**

- **지금은**: <mark>탐지를 확인하려면 파일을 따로따로 실행해야 하고, AI 호출이 실패하면 결과를 한 번에 남길 방법이 없습니다</mark>.
- **그래서 만드는 것**: `pipeline.py` 입니다.
  - 이벤트를 읽고 연결 · 탐지 · 점수까지 한 함수에서 이어 실행합니다.
  - 점수 기록을 파일에 저장하고, 대상마다 Gemini API 를 활용한 AI 요약을 받습니다.
  - 모든 결과를 보고서 파일 하나로 저장합니다.
- **실행하면**: <mark>단계 1: 읽은 이벤트 수, 단계 2: 탐지된 규칙과 점수 기록 수, 단계 3: Gemini API 를 활용한 AI 요약, 단계 4: 보고서 저장, 단계 5: 확인할 순서가 나옵니다.</mark>
- **현업에서는**: 파이프라인을 정해진 시각에 자동으로 실행하고 보고서 파일을 담당자에게 보냅니다. 자동 실행은 AI 가 없는 날에도 멈추지 않아야 해서 실패한 단계를 대체 값으로 넘깁니다.

**할 일**

1. `pipeline.py` · `exercise10-2_run.py` 두 파일을 만들고, `pipeline.py` 의 두 함수에서 직접 쓰는 곳을 씁니다.
2. 실행해서 <mark>읽은 이벤트 수</mark>(단계 1), <mark>탐지된 규칙과 점수 기록 수</mark>(단계 2), <mark>Gemini API 를 활용한 AI 요약</mark>(단계 3), <mark>보고서 저장</mark>(단계 4), <mark>확인할 순서</mark>(단계 5)를 읽고, 새로 생긴 `anomaly_detection_report_2026-11-02.json` 을 VS Code 에서 열어 봅니다.

`summarize_records` · `count_failed` · `save_report` · `run_pipeline` 은 읽기만 하는 미리 채운 함수입니다. Exercise 10-1에서 쓴 방식과 같아서 직접 쓰는 곳이 없습니다.

**`pipeline.py`**

```python
import json                                                                                # 보고서를 JSON 파일로 저장하기 위해 json 을 불러온다
from access_detection import load_events, EVENTS_PATH                                      # Unit 6 : 이벤트 파일을 읽는 함수를 불러온다
from correlation import find_chains_in_events                                              # Unit 7 : 서로 다른 로그를 연결하는 함수를 불러온다
from risk_scores import collect_findings, score_findings, collect_reasons, make_records, save_records, RISK_PATH  # Unit 7 : 탐지 · 점수 함수를 불러온다
from event_summary import pick_records_to_summarize, summarize_record, FAIL_TEXT           # Exercise 10-1 : Gemini API 를 활용한 AI 요약 함수를 불러온다

REPORT_DATE = "2026-11-02"                                                                 # 샘플 이벤트의 날짜
REPORT_PATH = "anomaly_detection_report_" + REPORT_DATE + ".json"                          # 보고서를 저장할 파일 이름


def analyze_events(events):                                                                # 이벤트 표를 받는 함수
    """이벤트에서 연결된 사건을 찾고, 탐지된 규칙을 모아 대상별 점수 기록을 만든다.
    Unit 7에서 하나씩 실행한 단계를 한 함수에서 이어 쓸 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. events 를 find_chains_in_events 에 전달해 연결된 사건을 구해 chains 에 담는다
    # 2. events 와 chains 를 collect_findings 에 전달해 탐지된 규칙 리스트를 구해 findings 에 담는다
    # 3. findings 를 score_findings 에 전달해 대상별 점수를 구해 totals 에 담는다
    # 4. findings 를 collect_reasons 에 전달해 대상별 규칙 이름을 구해 reasons 에 담는다
    records = make_records(totals, reasons)                                                # 점수 · 등급 · 이유 기록을 만든다 — 미리 채운 줄
    return findings, records                                                               # 탐지된 규칙 리스트와 기록을 리턴한다


def summarize_records(records):                                                            # 점수 기록 리스트를 받는 함수
    """요약할 대상을 고르고 대상마다 Gemini API 를 활용한 AI 요약을 받아 리스트로 모은다.
    요약에 실패한 대상은 FAIL_TEXT 가 들어가서 나머지 결과가 그대로 이어지게 할 때 쓴다.
    """
    picked = pick_records_to_summarize(records)                                            # 요약할 대상을 고른다
    summaries = []                                                                         # 요약을 담을 빈 리스트
    for record in picked:                                                                  # 대상을 하나씩 꺼낸다
        summary = summarize_record(record)                                                 # AI 에게 요약을 시킨다
        item = {"entity": record["entity"], "grade": record["grade"], "summary": summary}  # 대상 · 등급 · 요약을 딕셔너리로 만든다
        summaries.append(item)                                                             # 요약 리스트에 추가한다
    return summaries                                                                       # 요약 리스트를 리턴한다


def count_failed(summaries):                                                               # 요약 리스트를 받는 함수
    """요약 가운데 AI 호출이 실패한 것이 몇 개인지 센다.
    실패가 있으면 담당자가 그 대상은 점수와 이유를 직접 읽어야 하므로 알릴 때 쓴다.
    """
    failed = 0                                                                             # 실패한 개수를 0 으로 시작한다
    for item in summaries:                                                                 # 요약을 하나씩 꺼낸다
        if item["summary"] == FAIL_TEXT:                                                   # 실패 문장이면
            failed = failed + 1                                                            # 실패 개수를 1 늘린다
    return failed                                                                          # 실패한 개수를 리턴한다


def build_report(events, findings, records, summaries):                                    # 이벤트 표 · 탐지된 규칙 · 점수 기록 · 요약을 받는 함수
    """분석 결과를 담당자가 읽는 보고서 딕셔너리 하나로 모은다.
    분석 결과를 파일 하나로 전달할 때 쓴다.
    """
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 5. events 의 "source" 열을 꺼내 .value_counts() 를 붙여 로그 종류마다 이벤트 수를 구해 source_event_counts 에 담는다
    # 6. source_event_counts 에 .to_dict() 를 붙여 JSON 에 저장할 수 있는 딕셔너리로 바꿔 source_count_dict 에 담는다
    # 7. 키 "date" 에 REPORT_DATE, "event_count" 에 len(events), "source_event_counts" 에 source_count_dict, "finding_count" 에 len(findings), "records" 에 records, "summaries" 에 summaries 를 담은 딕셔너리를 report 에 담는다
    return report                                                                          # 보고서 딕셔너리를 리턴한다


def save_report(report, path):                                                             # 보고서 딕셔너리와 파일 경로를 받는 함수
    """보고서를 JSON 파일로 저장한다.
    담당자와 다른 프로그램이 같은 파일을 읽게 할 때 쓴다.
    """
    with open(path, "w", encoding="utf-8") as file:                                        # path 파일을 쓰기 모드로 연다
        json.dump(report, file, ensure_ascii=False, indent=2)                              # 한글은 그대로, 줄을 나눠 저장한다


def run_pipeline():                                                                        # 인자가 없는 함수
    """읽기 → 분석 → 점수 저장 → Gemini API 를 활용한 AI 요약 → 보고서 저장을 차례로 실행하고 단계마다 결과를 출력한다.
    탐지부터 보고서까지 한 번에 돌릴 때 쓴다.
    """
    events = load_events(EVENTS_PATH)                                                      # 이벤트 파일을 표로 읽는다
    print("--- 단계 1: 읽은 이벤트", len(events), "개")                                    # 단계 1 : 읽은 이벤트 수

    findings, records = analyze_events(events)                                             # 연결 · 탐지 · 점수를 한 번에 실행한다
    saved_count = save_records(records, RISK_PATH)                                         # 점수 기록을 파일에 저장한다
    print("--- 단계 2: 탐지된 규칙", len(findings), "건 → 점수 기록", saved_count, "건을", RISK_PATH, "에 저장")  # 단계 2 : 탐지 · 점수

    summaries = summarize_records(records)                                                 # 대상마다 Gemini API 를 활용한 AI 요약을 받는다
    failed_count = count_failed(summaries)                                                 # 요약에 실패한 것이 몇 개인지 센다
    print("--- 단계 3: Gemini API 를 활용한 AI 요약", len(summaries), "건 (실패", failed_count, "건)")  # 단계 3 : Gemini API 를 활용한 AI 요약
    for item in summaries:                                                                 # 요약을 하나씩 꺼낸다
        print(item["entity"], ":", item["summary"])                                        # 대상과 요약 문장을 출력한다

    report = build_report(events, findings, records, summaries)                            # 보고서 딕셔너리를 만든다
    save_report(report, REPORT_PATH)                                                       # 보고서를 파일에 저장한다
    print("--- 단계 4: 보고서를", REPORT_PATH, "에 저장")                                  # 단계 4 : 보고서 저장

    print("--- 단계 5: 확인할 순서")                                                       # 단계 5 : 담당자가 볼 순서
    for record in records:                                                                 # 점수 기록을 하나씩 꺼낸다
        print(record["grade"], record["entity"], record["score"])                          # 등급 · 대상 · 점수를 출력한다
```

- 들여쓰기는 **미리 채운 줄에 맞춥니다.** 1 ~ 7번은 모두 함수 안이라 앞에 공백 4개입니다.
- 각 번호 주석 바로 아래에 새 줄을 만들어 그 번호의 코드를 한 줄 씁니다. **주석은 지우지 않습니다.** 7번의 딕셔너리는 한 줄이 길어서 중괄호 안에서 줄을 나눠도 됩니다.
- 함수에 전달하는 순서는 주석에 적힌 순서입니다. <mark>2번은 `events` 다음에 `chains` 입니다.</mark>
- 채우기 전에 실행하면 `NameError: name 'totals' is not defined` 오류가 납니다. `totals` 를 만드는 3번을 아직 안 썼기 때문입니다.

**`exercise10-2_run.py`** — 그대로 붙여 넣습니다. 직접 쓰는 줄은 없습니다.

```python
from pipeline import run_pipeline  # 방금 만든 파이프라인 함수를 불러온다

run_pipeline()                     # 읽기부터 보고서 저장까지 한 번에 실행한다
```

**순서**

1. **[VS Code 또는 터미널]** 파일 `pipeline.py` · `exercise10-2_run.py` 를 `anomaly_detection` 폴더에 만들어 위 코드를 붙여 넣습니다.
   ```bash
   pwd
   touch pipeline.py exercise10-2_run.py
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `touch 파일이름` 빈 파일 만들기 · `ls` 폴더 안의 파일 이름 보기
2. **[VS Code]** `pipeline.py` 에서 <mark>직접 쓰는 곳 일곱 군데를 씁니다</mark>. 위 판다스 문법 상자와 2.1 의 그림을 참고해 씁니다. 막히면 아래 「Exercise 10-2 한눈에」를 봅니다.
3. **[터미널]** <mark>`pwd` 의 결과가 `anomaly_detection` 으로 끝나는지</mark> 확인하고 실행합니다(맥북은 `python3`). Gemini API 를 3번 호출합니다.
   ```bash
   pwd
   python exercise10-2_run.py
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python exercise10-2_run.py` 파이썬으로 실행 파일 실행
4. 출력은 **다섯 단계**입니다. 제목 줄(`--- 단계 …`)은 줄 수에 넣지 않습니다. 단계 1과 2와 4는 숫자나 파일 이름이 제목 줄에 함께 나와서 그 아래 줄이 없습니다. 단계 3은 제목 아래에 대상마다 요약 1줄씩 3줄이 나오고, 단계 5는 대상마다 등급 · 대상 · 점수 1줄씩 5줄이 나옵니다. <mark>AI 호출이 실패하면 `[LLM 호출 실패]` 줄이 단계 3 제목 줄 위에 나옵니다.</mark>
5. **[VS Code]** 새로 생긴 `anomaly_detection_report_2026-11-02.json` 을 열어 `event_count` · `records` · `summaries` 를 확인합니다.
6. **[보고서]** Unit 10 의 `## Exercise 10-2` › `#### Exercise 10-2` 아래를 채웁니다.
   - (가) 실행한 출력 전체를 붙여 넣고, 보고서 파일의 `event_count` · `finding_count` 값과 `records` · `summaries` 의 건수를 적어 주세요.
   - (나) [핵심 질문] 점수와 등급은 코드가 정하고 AI 에게는 요약만 시킨 이유를 적어 주세요. 단계 5 의 확인할 순서와 단계 3 의 요약을 근거로 쓰세요.
   - (다) [핵심 질문] AI 호출이 실패해도 파이프라인이 멈추지 않고 대체 문장을 쓰게 만든 이유를 적어 주세요. 대체 문장이 들어간 대상을 담당자가 어떻게 처리해야 하는지도 적어 주세요.

## Exercise 10-2 한눈에

| 하려는 일 | 코드 · 말 |
|---|---|
| 앞 결과를 다음 함수에 전달 | `findings = collect_findings(events, chains)` |
| 점수 합계 | `totals = score_findings(findings)` |
| 로그 종류마다 개수 | `source_event_counts = events["source"].value_counts()` |
| 시리즈를 딕셔너리로 | `source_count_dict = source_event_counts.to_dict()` |
| 보고서 딕셔너리 | `report = {"date": REPORT_DATE, … "summaries": summaries}` |

## Module 4 폴더 구조 한눈에 보기

> **읽을거리 — 읽기만 합니다.** 문제가 아닙니다. 답할 질문도, 따라 칠 명령도 없습니다.

Module 4가 끝나면 `anomaly_detection` 폴더에 Unit별로 아래 파일이 있어야 합니다. 파일을 어디에 저장했는지 헷갈리면 내 VS Code 왼쪽 목록과 비교합니다.

- **`config/` 안에는 JSON 설정 파일만** 둡니다. Unit 6에서 만든 `users.json` · `roles.json` 입니다.
- **그 밖의 파일은 모두 `anomaly_detection/` 바로 아래**에 둡니다. 코드(`.py`), 실행 파일(`exerciseU-n_…_run.py`), 데이터, 안내와 보고서(`.md`), 컴포즈 파일이 해당합니다. `logs/` 는 Unit 9에서 컴포즈로 만든 접속 기록 폴더입니다.
- 터미널은 항상 `…/anomaly_detection` 에서 실행합니다(`pwd` 로 확인).

```
security-agent-toolkit/
  .env
  .gitignore
  agent_core/
  network_zt/
  access_control/                   Module 3
  anomaly_detection/                Module 4   ← 여기서 작업
    config/                         ← JSON 설정만
      roles.json
      users.json
    logs/                           ← Unit 9에서 컴포즈가 남긴 접속 기록
      access.log
      error.log
      web_404.log
    __pycache__/                    ← 파이썬이 자동으로 만듦
    ── Unit 1 ──
    access_sample.log
    log_parse.py
    log_classify.py
    exercise1-1_run.py
    exercise1-2_run.py
    ── Unit 2 · 3 ──
    server_log.jsonl
    saas_events.csv
    normalize_web.py
    normalize_json_csv.py
    normalize.py
    normalized_events.json
    events_basic.py
    events_time.py
    exercise2-1_run.py  ~  exercise3-2_run.py
    ── Unit 4 · 5 ──
    baseline_logins.csv
    baseline_traffic.csv
    baseline.py
    login_detection.py
    classify.py
    traffic_detection.py
    alerts.py
    alerts.json
    exercise4-1_run.py  ~  exercise5-2_run.py
    ── Unit 6 · 7 ──
    rbac.py
    access_detection.py
    saas_detection.py
    malicious_detection.py
    advanced_detection.py
    correlation.py
    risk_scores.py
    unit05_risk_scores.json
    exercise6-1_run.py  ~  exercise7-2_run.py
    ── Unit 8 · 9 ──
    review_alerts.json
    problems.json
    login_alerts.json
    evaluation.py
    tuning.py
    final_check.py
    exercise8-1_run.py  ~  exercise8-3_run.py
    compose.yaml
    compose.secure.yaml
    ── Unit 10 (이번 Unit) ──
    llm_client.py
    event_summary.py
    pipeline.py
    exercise10-1_run.py
    exercise10-2_run.py
    anomaly_detection_report_2026-11-02.json
    ── Unit마다 받은 안내와 보고서 ──
    unit01_pm_*.md  unit03_am_*.md  unit03_pm_*.md  unit05_am_*.md  unit05_pm_*.md
    unit07_am_*.md  unit07_pm_*.md  unit09_am_*.md  unit09_pm_*.md  unit10_am_*.md
```

- `__pycache__/` 는 파이썬이 자동으로 만드는 임시 폴더라서 신경 쓰지 않고 깃허브에도 올리지 않습니다.

---
