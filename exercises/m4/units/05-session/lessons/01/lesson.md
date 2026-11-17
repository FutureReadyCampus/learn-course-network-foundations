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

## 개요

오전에는 로그인 실패 규칙과 이벤트 유형 규칙을 만들었습니다. 오후에는 **요청이 갑자기 늘어난 때(트래픽 급증, traffic spike, 트래픽 스파이크)** 를 찾는 규칙을 하나 더 만들고, 오전과 오후의 탐지 결과를 **알림 한 파일**로 모읍니다. SIEM(심, 보안 로그를 모아 탐지 · 알림하는 시스템)의 네 단계 중 탐지를 마무리하고 마지막 단계인 **알림**을 처음 해 보는 날입니다.

- **Exercise 5-1**: 웹 서버 요청을 분마다 세고, 지난 7일 평균의 3배 이상으로 늘어난 분을 찾습니다.
- **Exercise 5-2**: 로그인 실패 알림과 트래픽 급증 알림을 같은 모양으로 만들어 `alerts.json` 한 파일에 저장합니다.

오늘은 오후 5 · Exercise 5-2이고, <mark>깃허브에 올리는 일은 Exercise 5-2 마지막에 합니다.</mark> Exercise마다 문제는 하나입니다.

- 오늘 쓰는 도구는 **파이썬 · 판다스 · VS Code · 터미널 · git** 입니다.
- 급증 기준은 **지난 7일 평균의 3배로 고정**하고, 값을 바꿔 가며 비교하지 않습니다.
- 샘플 이벤트의 날짜는 2026-11-02 이고, 이야기 속 「오늘」은 이 샘플을 기준으로 합니다. `baseline_traffic.csv` 의 숫자는 오전 9시대 값이고, 웹 서버 이벤트도 모두 9시대입니다(57개 중 웹 서버 28 · 판정 서버 15(`source` 가 `server`) · SaaS 14).
- 보고서에서 [핵심 질문] 가 붙은 질문은 이 Exercise에서 꼭 알아야 할 핵심 질문이고, 내 화면의 값을 근거로 이유까지 서술합니다.
- **오늘 불러 쓰는 이전 파일**이 있습니다. 모두 오늘 오전에 만든 파일입니다.

| 파일 | 만든 곳 | 쓰는 곳 | 없거나 안 풀렸을 때 |
|---|---|---|---|
| `normalized_events.json` | 오전 안내(`day03_am_baseline_login.md`) 시작하기 5번 | 5 · Exercise 5-2 | 그 안내 시작하기 5번의 내용으로 파일을 만듭니다 |
| `login_detection.py` | 오전 Exercise 4-2 Exercise Exercise 4-3 | Exercise 5-2 `day03_6-1_run.py` 가 불러옵니다 | 오전 안내 Exercise Exercise 4-3 의 `login_detection.py` 코드 칸을 붙여 넣고, 「Exercise Exercise 4-3 정답」의 「채운 코드」를 빈칸 자리에 넣어 파일을 완성합니다. `pick_alert_ips` 는 주소와 횟수를 담은 결과(`Series`)를 리턴해야 합니다 |

## 개요

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치와 오전 파일을 확인합니다. <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, `ls` 결과에 `login_detection.py` 와 `normalized_events.json` 이 보여야</mark> 합니다.
   ```bash
   cd anomaly_detection
   pwd
   ls
   ```
3. **오늘 받은 파일 두 개**(`day03_pm_traffic_alerts.md`, `day03_pm_report.md`)를 `다운로드` 폴더에서 `anomaly_detection` 폴더로 끌어다 놓습니다(안 되면 **File › Save As…**). 이미 있으면 건너뜁니다.
4. **[VS Code]** 보고서 맨 위 제목 `(이름 · 2026-11-04(수))` 의 `이름` 을 내 이름으로 바꿉니다. 안내 파일은 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다.
5. **[VS Code 또는 터미널]** `anomaly_detection` 폴더에 `baseline_traffic.csv` 파일을 만들어 아래 내용을 그대로 붙여 넣습니다(터미널에서는 `touch baseline_traffic.csv` 후 VS Code 에서 엽니다).

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
   python -c "print(len(open('baseline_traffic.csv', encoding='utf-8').read().splitlines()))"
   ```
   - <mark>`8`(헤더 줄 포함)이 나와야</mark> 합니다. 다르면 줄이 누락됐거나 빈 줄이 들어간 것이니 다시 붙여 넣습니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `No module named 'pandas'`: 가상환경이 활성화되지 않은 터미널입니다. `security-agent-toolkit` 폴더에서 `source .venv/Scripts/activate` 로 활성화한 뒤 `python -m pip install pandas` 를 입력합니다(맥북은 `Scripts` 를 `bin` 으로, 폴더 이름이 `.venv` 가 아니면 그 이름으로).
- `ImportError` · `No module named 'login_detection'`: 오전 `login_detection.py` 가 없거나 함수 이름이 문서와 다른 것입니다. 위 표의 「없거나 안 풀렸을 때」를 따릅니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

---
