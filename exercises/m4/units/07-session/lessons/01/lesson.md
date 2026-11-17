---
id: m4-u07-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/108_day04_pm_correlation_risk.md
  mission_id: GichanSource.m4-1105-pm-correlation-risk
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 이번에 할 일: 로그 연결과 위험 점수

Unit 6에서는 판정 서버 · SaaS · 웹 로그에서 먼저 확인할 것을 따로 탐지했습니다. 이번 Unit에서는 먼저 **같은 사용자의 이벤트가 서로 다른 로그에 짧은 시간 안에 나타난 경우**를 찾아 하나의 사건으로 연결합니다. 이렇게 서로 다른 로그를 같은 기준으로 연결해 분석하는 것을 상관분석(correlation, 코렐레이션)이라고 합니다. 그다음 탐지된 규칙마다 **점수**를 매겨 high · mid · low 로 나누고, 결과를 `unit05_risk_scores.json` 한 파일에 저장합니다. 파일 이름의 `unit05` 는 강의계획서가 정한 이름이라 그대로 씁니다.

- **Exercise 7-1**: 웹 로그에는 사용자가 없어서 SaaS 성공 로그인의 IP 로 사용자를 찾고, 서버 · SaaS · 웹 로그를 한 표로 합쳐 사용자 · 시각 순으로 놓은 뒤 60분 안에 모인 사건을 찾습니다.
- **Exercise 7-2**: Unit 6의 탐지와 Exercise 7-1 결과에서 탐지된 규칙을 모으고, 규칙마다 점수를 더해 등급과 이유를 파일로 저장합니다.

이번 Unit은 Exercise 7-1 · 7-2로 이루어져 있고, <mark>깃허브에 올리는 일은 Exercise 7-2 마지막에 합니다.</mark> Exercise마다 문제는 하나입니다.

- 이번 Unit에서 쓰는 도구는 **파이썬 · 판다스 · VS Code · 터미널 · git** 입니다.
- 코드 줄은 판다스로 쓰는 줄과 파이썬으로 쓰는 줄이 섞여 있습니다. 표를 합치고 정렬하고 합계를 내는 줄이 판다스이고, 판단 · 딕셔너리 · 문자열 연결이 파이썬입니다.
- 연결 기준(서로 다른 로그 2종류 이상 · 60분)과 점수 · 등급 기준(high 60 이상 · mid 35 이상)은 **고정**하고, <mark>값을 바꿔 가며 비교하지 않습니다</mark>.
- 샘플 이벤트의 날짜는 2026-11-02 입니다. 57개 중 웹 서버 28 · 판정 서버 15 · SaaS 14입니다.
- 보고서에서 `[핵심 질문]` 표시가 붙은 질문은 이 Exercise에서 꼭 알아야 할 핵심 질문이고, <mark>내 화면의 값을 근거로 이유까지 서술합니다</mark>.
- **이번 Unit에서 불러 쓰는 이전 파일**이 있습니다. 아래 표에서 <mark>`correlation.py` 만 이번 Unit의 Exercise 7-1에서 만들고, 나머지는 모두 Unit 6에서 만든 파일</mark>입니다.

| 파일 | 만든 곳 | 쓰는 곳 | 없거나 완성하지 못했을 때 |
|---|---|---|---|
| `normalized_events.json` · `rbac.py` · `config/users.json` · `config/roles.json` | Unit 6 안내의 시작하기 6번 | Exercise 7-1 · 7-2 | 그 안내 시작하기 6번의 내용으로 파일을 만듭니다 |
| `access_detection.py` | Exercise 6-1 | Exercise 7-1 · 7-2가 불러옵니다 | 이 안내 맨 아래 「부록」의 완성본으로 파일을 만듭니다 |
| `saas_detection.py` | Exercise 6-2 | Exercise 7-1 · 7-2가 불러옵니다 | 이 안내 맨 아래 「부록」의 완성본으로 파일을 만듭니다 |
| `malicious_detection.py` | Exercise 6-3 | Exercise 7-1 · 7-2가 불러옵니다 | 이 안내 맨 아래 「부록」의 완성본으로 파일을 만듭니다 |
| `correlation.py` | Exercise 7-1 | Exercise 7-2 `exercise7-2_run.py` 가 불러옵니다 | 이 안내 Exercise 7-1 의 코드 칸에 「Exercise 7-1 정답」의 「채운 코드」를 넣어 완성합니다 |

## 폴더 열고 Unit 6 파일 확인하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치와 Unit 6 파일을 확인합니다(맥북은 `python3`). <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, `ls` 결과에 위 표의 파일들이 보여야</mark> 합니다.
   ```bash
   cd anomaly_detection
   pwd
   ls
   ```
3. **이번 Unit에서 받은 파일 두 개**(Unit 7 안내 파일과 보고서 파일)를 <mark>`다운로드` 폴더에서 `anomaly_detection` 폴더로 끌어다 놓습니다</mark>(안 되면 **File › Save As…**). 이미 있으면 건너뜁니다.
4. **[VS Code]** 보고서 맨 위의 <mark>`이름` 을 내 이름으로 바꿉니다</mark>. 안내 파일은 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다.
5. **[터미널]** Unit 6의 함수가 잘 불러와지는지 확인합니다. <mark>세 줄 모두 아무 오류도 나오지 않으면</mark> 됩니다. 오류가 나면 그 줄의 파일이 문제입니다.
   ```bash
   python -c "from access_detection import load_events, pick_server_failures, pick_suspicious, judge_failure, EVENTS_PATH"
   python -c "from saas_detection import pick_saas, pick_logins, find_off_hours_logins, find_new_ip_users, find_bulk_download_users"
   python -c "from malicious_detection import pick_web_failures, find_scan_ips"
   ```
   - `python -c "코드"` 는 파일을 만들지 않고 코드를 한 줄로 바로 실행합니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 파일 이름이 문서와 같은지 봅니다.
- `No module named 'pandas'`: <mark>가상환경이 활성화되지 않은 터미널입니다</mark>. `security-agent-toolkit` 폴더에서 가상환경을 활성화한 뒤(`source .venv/Scripts/activate`, 맥북은 `Scripts` 를 `bin` 으로, 폴더 이름이 다르면 그 이름으로) `python -m pip install pandas` 를 칩니다.
- `ImportError` · `No module named 'access_detection'`: <mark>Unit 6의 파일이 없거나 함수 이름이 문서와 다른 것입니다</mark>. 위 표의 「없거나 완성하지 못했을 때」를 따릅니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 맨 아래 「정답」을 보고</mark>, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다. 파일을 지금 위치 기준으로 찾기 때문입니다.

---
