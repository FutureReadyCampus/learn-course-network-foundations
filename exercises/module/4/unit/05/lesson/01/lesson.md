---
id: m4-u05-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/104_day03_pm_traffic_alerts.md
  mission_id: GichanSource.m4-1104-pm-traffic-alerts
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표와 쓸 도구

Unit 4에서는 로그인 실패 규칙과 이벤트 유형 규칙을 만들었습니다. 이번 Unit에서는 **요청이 갑자기 늘어난 때(트래픽 급증, traffic spike, 트래픽 스파이크)** 를 찾는 규칙을 하나 더 만들고, Unit 4와 이번 Unit의 탐지 결과를 **알림 한 파일**로 모읍니다. SIEM(심, 보안 로그를 모아 탐지하고 알림을 보내는 시스템)의 네 단계 중 탐지를 마무리하고, 마지막 단계인 **알림**을 처음 해 봅니다.

- **실습 5-1**: 웹 서버 요청을 분마다 세고, 지난 7일 평균의 3배 이상으로 늘어난 분을 찾습니다.
- **실습 5-2**: 로그인 실패 알림과 트래픽 급증 알림을 같은 모양으로 만들어 `alerts.json` 한 파일에 저장합니다.

이번 Unit은 실습 5-1과 실습 5-2로 이루어져 있고, <mark>깃허브에 올리는 일은 실습 5-2 마지막에 합니다.</mark> 실습마다 문제는 하나입니다.

- 이번 Unit에서 쓰는 도구는 **파이썬 · 판다스 · VS Code · 터미널 · git** 입니다.
- 급증 기준은 **지난 7일 평균의 3배로 고정**하고, 값을 바꿔 가며 비교하지 않습니다.
- 샘플 이벤트의 날짜는 2026-11-02 이고, 이야기 속 「오늘」은 이 샘플을 기준으로 합니다. `baseline_traffic.csv` 의 숫자는 오전 9시대 값이고, 웹 서버 이벤트도 모두 9시대입니다(57개 중 웹 서버 28 · 판정 서버 15(`source` 가 `server`) · SaaS 14).
- 실습 결과 기록에서 [핵심 질문] 표시가 붙은 질문은 이 실습에서 꼭 알아야 할 핵심 질문이고, 내 화면의 값을 근거로 이유까지 서술합니다.
- **이번 Unit에서 불러 쓰는 이전 파일**이 있습니다. 모두 Unit 4에서 만든 파일입니다.

| 파일 | 만든 곳 | 쓰는 곳 | 없거나 안 풀렸을 때 |
|---|---|---|---|
| `normalized_events.json` | Unit 4 「시작하기」 5번 | 실습 5-2 | Unit 4 「시작하기」 레슨 5번의 코드 상자로 파일을 만듭니다 |
| `login_detection.py` | 실습 4-2 | 실습 5-2 `exercise5-2_run.py` 가 불러옵니다 | Unit 4 실습 4-2 레슨의 `login_detection.py` 코드 칸을 붙여 넣고, [M4 Unit 4 실습 4-2](__SITE__/exercises/module/4/unit/4/lesson/3/page/4)에서 「정답과 해설 보기」를 열어 채운 코드를 확인한 뒤 빈칸에 넣어 파일을 완성합니다. `pick_alert_ips` 는 주소와 횟수를 담은 결과(`Series`)를 리턴해야 합니다 |

## 폴더 열고 평소 요청 수 파일 준비하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치와 Unit 4의 파일을 확인합니다. <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, `ls` 결과에 `login_detection.py` 와 `normalized_events.json` 이 보여야</mark> 합니다.
   ```bash
   cd anomaly_detection
   pwd
   ls
   ```
3. **파일을 만드는 방법:** 「`파일이름`을 만들어 아래 내용을 붙여 넣습니다」라고 하면:
   1. **[VS Code]** 왼쪽 목록에서 알려 준 폴더를 오른쪽 클릭 › **New File** 을 누르고, 알려 준 **파일 이름을 그대로** 적고 Enter 를 칩니다. 이미 있으면 새로 만들지 않고 그 파일을 엽니다.
   2. 코드 상자의 복사 버튼으로 내용을 복사해 새 파일에 붙여 넣고, `Ctrl + S`(맥북은 `Cmd + S`)로 저장합니다.
4. 실행 출력과 판단 근거를 기록할 `report_u5.md` 도 이 Unit의 「실습 결과 기록 준비」에서 틀을 복사해 만듭니다.
5. **[VS Code]** `anomaly_detection` 폴더에 `baseline_traffic.csv` 파일을 만들어 아래 내용을 그대로 붙여 넣습니다.

**`baseline_traffic.csv`** — 지난 7일 동안 오전 9시대에 웹 서버로 들어온 요청이 **1분에 평균 몇 번**이었는지 적은 연습용 숫자입니다. 첫 줄은 헤더(열 이름이 적힌 줄)이고, 둘째 줄부터 한 줄이 하루입니다.

```
date,requests_per_minute
2026-10-26,2
2026-10-27,2
2026-10-28,3
2026-10-29,2
2026-10-30,1
2026-10-31,2
2026-11-01,2
```

6. **[터미널]** 파일이 정상인지 확인합니다(맥북은 `python3`).
   ```bash
   python - <<'PY'
   from pathlib import Path

   lines = Path("baseline_traffic.csv").read_text(encoding="utf-8").splitlines()
   print("CSV 줄 수(헤더 포함):", len(lines))
   PY
   ```
   - <mark>`CSV 줄 수(헤더 포함): 8` 이 나와야</mark> 합니다. 다르면 줄이 누락됐거나 빈 줄이 들어간 것이니 다시 붙여 넣습니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `No module named 'pandas'`: 가상환경이 활성화되지 않은 터미널입니다. `security-agent-toolkit` 폴더에서 `source .venv/Scripts/activate` 로 활성화한 뒤 `python -m pip install pandas` 를 입력합니다(맥북은 `Scripts` 를 `bin` 으로, 폴더 이름이 `.venv` 가 아니면 그 이름으로).
- `ImportError` · `No module named 'login_detection'`: Unit 4의 `login_detection.py` 가 없거나 함수 이름이 문서와 다른 것입니다. 위 표의 「없거나 안 풀렸을 때」를 따릅니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 각 실습 뒤의 「정답과 해설 보기」를 참고하고, 풀리지 않으면 실습 결과 기록의 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

---
