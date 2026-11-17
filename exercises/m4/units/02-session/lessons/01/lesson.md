---
id: m4-u02-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/098_day02_am_normalize.md
  mission_id: GichanSource.m4-1103-am-normalize
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 이번 Unit 소개: 세 로그를 하나로 맞추기

Unit 1에서는 웹 서버 접속 로그 한 줄을 읽고 이상 징후를 구분하는 법을 배웠습니다. 이번 Unit에서는 **서로 다른 모양의 로그 3종류를 같은 키로 맞추는 정규화**를 합니다. SIEM(심, 로그를 모아 분석하는 보안 도구)의 네 단계(수집 → 정규화 → 탐지 → 알림 · 조사) 중 두 번째 단계입니다.

- **Exercise 2-1**: 웹 서버 로그 한 줄을 공통 이벤트(키는 2.1에서 설명)로 바꿉니다. 시각 모양을 맞추는 법을 처음 배웁니다.
- **Exercise 2-2**: 판정 서버 로그(JSON)와 SaaS 로그(CSV)를 같은 공통 이벤트로 바꿉니다.
- **Exercise 2-3**: 세 로그의 이벤트를 하나로 합쳐 시간순으로 정렬하고 `normalized_events.json` 파일로 저장합니다. 이 파일을 Unit 3에서 판다스로 읽습니다.

이번 Unit은 Exercise 2-1 · Exercise 2-2 · Exercise 2-3으로 이루어져 있고, <mark>깃허브에 올리는 일은 Unit 3의 Exercise 3-2 마지막에 합니다.</mark> Exercise마다 문제는 하나입니다.

- 이번 Unit에서 쓰는 도구는 **파이썬 · VS Code · 터미널**입니다. 판다스는 Unit 3에서 처음 씁니다.
- 새로 나오는 문법은 읽을거리의 「문법 상자」에서 코드와 실행 결과, 값이 바뀌는 모양과 함께 설명합니다.
- **이번 Unit에서 불러 쓰는 이전 파일**

| 파일 | 어디서 | 이번 Unit에서 쓰는 곳 | 없으면 |
|---|---|---|---|
| `log_parse.py` | Unit 1의 Exercise 1-1에서 만든 파일 | Exercise 2-1 `normalize_web.py` 가 안의 함수 네 개를 불러 씁니다 | 문서 맨 아래 「앞 Unit 파일 완성본」으로 만듭니다 |
| `access_sample.log` | Unit 1 시작하기에서 만든 샘플 웹 서버 로그(30줄) | Exercise 2-1과 Exercise 2-3에서 읽습니다 | 같은 곳의 완성본으로 만듭니다 |

## 폴더 열고 로그 파일 준비하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치와 Unit 1의 파일을 확인합니다(맥북은 `python3`). <mark>`pwd` 가 `…/anomaly_detection` 으로 끝나고, `ls` 결과에 `log_parse.py` 와 `access_sample.log` 가 보여야</mark> 합니다. 없으면 맨 아래 「앞 Unit 파일 완성본」으로 먼저 만듭니다. `cd` 가 「No such file or directory」 오류를 내면 `mkdir anomaly_detection` 으로 폴더부터 만들고 들어갑니다.
   ```bash
   cd anomaly_detection
   pwd
   ls
   ```
3. **이번 Unit에서 받은 파일 두 개**(Unit 2 안내, Unit 2 보고서)를 `다운로드` 폴더에서 `anomaly_detection` 폴더로 끌어다 놓습니다(안 되면 **File › Save As…**). 이미 있으면 건너뜁니다.
4. **[VS Code]** 보고서 맨 위 제목 `(이름 · 2026-11-03(화))` 의 <mark>`이름` 을 내 이름으로 바꿉니다</mark>. 안내 파일은 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다.
5. **[VS Code 또는 터미널]** `anomaly_detection` 폴더에 `server_log.jsonl` 과 `saas_events.csv` 파일을 만들어 아래 내용을 그대로 붙여 넣습니다(터미널에서는 `touch 파일이름` 후 VS Code 에서 엽니다).

**`server_log.jsonl`** — 판정 서버가 남긴 로그 샘플입니다. Module 3에서 만든 서버의 로그와 같은 모양이고, 한 줄이 요청 1개인 JSON 입니다(15줄).

```
{"time": "2026-11-02T09:40", "user": "seoyeon", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-11-02T09:52", "user": "junho", "permission": "SALES:CHANGE", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-11-02T10:05", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "vpn", "allowed": false, "reason": "허용되지 않은 접속 위치"}
{"time": "2026-11-02T10:09", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "vpn", "allowed": false, "reason": "허용되지 않은 접속 위치"}
{"time": "2026-11-02T10:14", "user": "gaeun", "permission": "ACCOUNT:CHANGE", "network": "vpn", "allowed": false, "reason": "허용되지 않은 접속 위치"}
{"time": "2026-11-02T11:02", "user": "dami", "permission": "SALES:QUERY", "network": "office", "allowed": false, "reason": "퇴사한 계정"}
{"time": "2026-11-02T11:03", "user": "dami", "permission": "SALES:QUERY", "network": "office", "allowed": false, "reason": "퇴사한 계정"}
{"time": "2026-11-02T11:05", "user": "dami", "permission": "SALES:CHANGE", "network": "office", "allowed": false, "reason": "퇴사한 계정"}
{"time": "2026-11-02T11:08", "user": "dami", "permission": "SALES:QUERY", "network": "office", "allowed": false, "reason": "퇴사한 계정"}
{"time": "2026-11-02T11:40", "user": "seoyeon", "permission": "SETTLE:QUERY", "network": "office", "allowed": false, "reason": "권한 없음"}
{"time": "2026-11-02T13:15", "user": "junho", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-11-02T14:30", "user": "seoyeon", "permission": "SALES:CHANGE", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-11-02T15:05", "user": "junho", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-11-02T16:10", "user": "gaeun", "permission": "SALES:QUERY", "network": "office", "allowed": true, "reason": "역할 권한"}
{"time": "2026-11-02T18:20", "user": "seoyeon", "permission": "SALES:CHANGE", "network": "vpn", "allowed": false, "reason": "업무 시간 밖"}
```

**`saas_events.csv`** — SaaS 서비스가 내보낸 로그 샘플입니다. 첫 줄은 열 이름이고, 둘째 줄부터 한 줄이 이벤트 1개이며 값은 쉼표로 나뉩니다(첫 줄이 열 이름이라 이벤트는 14개이고, 파일은 15줄입니다). 시각은 내보낼 때 한국 시간으로 설정되어 있습니다.

```
time,account,event,ip_address,outcome
2026-11-02 02:14:08,jiwoo@a-corp.example,login,203.0.113.80,failure
2026-11-02 09:05:30,seoyeon@a-corp.example,login,198.51.100.9,success
2026-11-02 09:30:12,junho@a-corp.example,login,192.0.2.41,success
2026-11-02 10:12:55,gaeun@a-corp.example,login,198.51.100.77,success
2026-11-02 11:25:40,seoyeon@a-corp.example,file.download,198.51.100.9,success
2026-11-02 13:50:21,junho@a-corp.example,file.upload,192.0.2.41,success
2026-11-02 15:20:03,junho@a-corp.example,login,192.0.2.41,success
2026-11-02 16:02:18,jiwoo@a-corp.example,login,198.51.100.52,success
2026-11-02 17:38:10,seoyeon@a-corp.example,login,203.0.113.80,success
2026-11-02 17:40:02,seoyeon@a-corp.example,file.download,203.0.113.80,success
2026-11-02 17:40:31,seoyeon@a-corp.example,file.download,203.0.113.80,success
2026-11-02 17:41:05,seoyeon@a-corp.example,file.download,203.0.113.80,success
2026-11-02 17:41:48,seoyeon@a-corp.example,file.download,203.0.113.80,success
2026-11-02 17:42:20,seoyeon@a-corp.example,file.download,203.0.113.80,success
```

6. **[터미널]** 세 파일의 줄 수를 확인합니다.
   ```bash
   python -c "print(len(open('access_sample.log', encoding='utf-8').read().splitlines()))"
   python -c "print(len(open('server_log.jsonl', encoding='utf-8').read().splitlines()))"
   python -c "print(len(open('saas_events.csv', encoding='utf-8').read().splitlines()))"
   ```
   - <mark>순서대로 `30` · `15` · `15` 가 나와야</mark> 합니다. 다르면 줄이 빠졌거나 빈 줄이 끼어든 것이니 다시 붙여 넣습니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `No module named 'log_parse'`: Unit 1의 `log_parse.py` 가 이 폴더에 없는 것입니다. 맨 아래 「앞 Unit 파일 완성본」으로 만듭니다.
- `IndentationError` · `NameError`: 직접 쓴 줄의 들여쓰기가 틀렸거나 빠뜨린 줄이 있습니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 그 질문의 `답:` 에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 **터미널**에서 합니다(맥북은 `python3`).

---
