---
id: m4-u01-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/096_day01_pm_log_basics.md
  mission_id: GichanSource.m4-1102-pm-log-basics
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 로그 읽기와 작은 규칙

이번 Unit부터 **Module 4 이상탐지**입니다. 이상탐지는 로그에서 **평소와 다른 것을 찾는 일**입니다. 첫 Unit에서는 찾기 전에 먼저 **로그가 무엇이고 한 줄에 무엇이 들어 있는지** 읽고, 아주 작은 탐지 규칙을 직접 만들어 봅니다.

- **실습 1-1**: 먼저 Module 4가 무엇을 하는 Module인지, 그리고 이 Module 내내 나오는 도구 **SIEM(심)** 이 무엇이고 현업에서 어떻게 쓰는지 읽습니다. 이어서 웹서버 접속 로그 한 줄을 프로그램이 읽을 수 있게 **조각으로 나눕니다.**
- **실습 1-2**: 읽은 로그 줄을 **정상 · 오류 · 의심**으로 가르고, 작은 회사라면 어떤 심 방식이 맞을지 고릅니다.

이번 Unit은 실습 1-1과 실습 1-2로 이루어져 있고, 깃허브에 올리는 일은 실습 1-2 마지막에 합니다. 실습마다 문제는 하나입니다.

- 이번 Unit에서 쓰는 도구는 Module 3과 같습니다. **파이썬 · VS Code · 터미널 · git** 입니다.
  - 도커와 판다스는 이번 Unit에서 쓰지 않습니다. 도커는 Unit 9에서, 판다스는 Unit 3의 실습 3-1부터 씁니다. 판다스 설치는 이번 Unit 마무리 뒤에 미리 해 둘 수 있습니다(「이번 Unit 마무리」 아래 「다음 Unit 준비」).
- 로그는 문서에 붙여 넣는 **샘플 파일**(`access_sample.log`) 하나만 씁니다. 30줄이고, 정상 접속 · 로그인 실패 · 없는 주소 탐색 · 깨진 줄 2개가 섞여 있습니다. Module 3에서 만든 파일은 불러오지 않습니다.
  - 실습 1-2 파일은 실습 1-1에서 만든 `log_parse.py` 를 불러 씁니다(문서 맨 아래 「앞 실습 파일 완성본」에 있습니다).

## 폴더 만들고 샘플 로그 준비하기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** Module 4 폴더를 만들고 들어갑니다(맥북은 `python` 을 `python3` 로). <mark>마지막 `pwd` 가 `…/anomaly_detection` 으로 끝나야</mark> 합니다. `mkdir` 가 「이미 있다」고 하면 그대로 `cd` 합니다. 앞으로 Module 4 파일은 모두 이 폴더에 만듭니다.
   ```bash
   mkdir anomaly_detection
   cd anomaly_detection
   pwd
   python --version
   ```
3. **이번 Unit에서 받은 파일 두 개**(Unit 1 안내, Unit 1 보고서)를 `다운로드` 폴더에서 `anomaly_detection` 폴더로 끌어다 놓습니다(안 되면 **File › Save As…**). 이미 있으면 건너뜁니다.
4. **[VS Code]** 보고서 맨 위 제목 `(이름 · 2026-11-02(월))` 의 `이름` 을 내 이름으로 바꿉니다. 안내 파일은 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다.
5. **[VS Code 또는 터미널]** `anomaly_detection` 폴더에 `access_sample.log` 파일을 만들어 아래 내용을 그대로 붙여 넣습니다(터미널에서는 `touch access_sample.log` 후 VS Code 에서 엽니다).

**`access_sample.log`** — 웹서버(nginx) 접속 로그 샘플입니다. 한 줄이 요청 한 개입니다. 일부 줄은 일부러 깨뜨려 두었습니다(실제 로그에도 끝이 잘린 줄이 섞입니다). <mark>마지막 줄의 `-` 도 일부러 넣은 깨진 줄이니 지우지 않습니다.</mark>

```
198.51.100.21 - - [02/Nov/2026:09:01:05 +0900] "GET / HTTP/1.1" 200 1204 "-" "Mozilla/5.0"
198.51.100.21 - - [02/Nov/2026:09:01:06 +0900] "GET /static/app.css HTTP/1.1" 200 3120 "-" "Mozilla/5.0"
198.51.100.34 - - [02/Nov/2026:09:03:47 +0900] "GET /login HTTP/1.1" 200 1830 "-" "Mozilla/5.0"
198.51.100.34 - - [02/Nov/2026:09:03:59 +0900] "POST /login HTTP/1.1" 302 0 "-" "Mozilla/5.0"
198.51.100.34 - - [02/Nov/2026:09:04:00 +0900] "GET /board HTTP/1.1" 200 5410 "-" "Mozilla/5.0"
192.0.2.15 - - [02/Nov/2026:09:05:21 +0900] "GET /board?page=2 HTTP/1.1" 200 5322 "-" "Mozilla/5.0"
192.0.2.15 - - [02/Nov/2026:09:05:40 +0900] "GET /board/12 HTTP/1.1" 200 2210 "-" "Mozilla/5.0"
203.0.113.50 - - [02/Nov/2026:09:12:01 +0900] "GET /login HTTP/1.1" 200 1830 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:03 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:06 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:09 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:12 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:15 +0900] "POST /login HTTP/1.1" 401 312 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:18 +0900] "POST /login HTTP/1.1" 302 0 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:25 +0900] "GET /admin HTTP/1.1" 403 287 "-" "python-requests/2.31.0"
203.0.113.50 - - [02/Nov/2026:09:12:27 +0900] "GET /admin/users HTTP/1.1" 403 287 "-" "python-requests/2.31.0"
198.51.100.90 - - [02/Nov/2026:09:20:10 +0900] "GET /.env HTTP/1.1" 404 153 "-" "curl/8.4.0"
198.51.100.90 - - [02/Nov/2026:09:20:11 +0900] "GET /wp-login.php HTTP/1.1" 404 153 "-" "curl/8.4.0"
198.51.100.90 - - [02/Nov/2026:09:20:12 +0900] "GET /phpmyadmin HTTP/1.1" 404 153 "-" "curl/8.4.0"
198.51.100.21 - - [02/Nov/2026:09:22:30 +0900] "GET /board/99 HTTP/1.1" 404 153 "-" "Mozilla/5.0"
198.51.100.34 - - [02/Nov/2026:09:25:02 +0900] "GET /report HTTP/1.1" 500 177 "-" "Mozilla/5.0"
192.0.2.15 - - [02/Nov/2026:09:26:44 +0900] "GET /search?q=network HTTP/1.1" 200 4010 "-" "Mozilla/5.0"
192.0.2.88 - - [02/Nov/2026:09:28:13 +0900] "GET / HTTP/1.1" 200 1204 "-" "Mozilla/5.0"
192.0.2.88 - - [02/Nov/2026:09:28:20 +0900] "GET /board HTTP/1.1" 200 5410 "-" "Mozilla/5.0"
198.51.100.21 - - [02/Nov/2026:09:31:15 +0900] "GET /board HTTP/1.1" 301 169 "-" "Mozilla/5.0"
198.51.100.21 - - [02/Nov/2026:09:31:40 +0900] "GET /board/5 HTTP/1.1
198.51.100.77 - - [02/Nov/2026:09:33:51 +0900] "GET /admin HTTP/1.1" 403 287 "-" "Mozilla/5.0"
192.0.2.88 - - [02/Nov/2026:09:35:02 +0900] "GET /logout HTTP/1.1" 302 0 "-" "Mozilla/5.0"
198.51.100.21 - - [02/Nov/2026:09:36:10 +0900] "GET /board/12 HTTP/1.1" 200 2210 "-" "Mozilla/5.0"
-
```

6. **[터미널]** 파일이 30줄인지 확인합니다(맥북은 `python3`).
   ```bash
   python -c "print(len(open('access_sample.log', encoding='utf-8').read().splitlines()))"
   ```
   - <mark>`30` 이 나와야</mark> 합니다. 다르면 줄이 빠졌거나 빈 줄이 끼어든 것이니 다시 붙여 넣습니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `IndentationError` · `NameError`: 직접 쓴 줄의 들여쓰기가 틀렸거나 빠뜨린 줄이 있습니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다(맥북은 `python3`). 앞 실습 파일이 없으면 문서 맨 아래 「앞 실습 파일 완성본」으로 먼저 만듭니다.

---
