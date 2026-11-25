---
id: m4-u05-l07
title: 정답
render: markdown
---

# 정답

## 정답 보는 법

글로 쓰는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

1. **핵심 실습**: 실습 5-1 · 5-2 정답입니다. 오늘 모두가 하는 실습이니 먼저 맞춰 봅니다.
2. **응용(여유가 되면)**: 응용 5-1 · 5-2 · 5-3 정답입니다. 응용을 한 사람만 봅니다.
3. 정답마다 결과, 왜, 자주 틀리는 곳, 관제에서는 순서로 읽습니다.
4. AI 요약이 나오는 실습 5-1 · 응용 5-3은 <mark>Gemini API 키가 있을 때와 없을 때 출력이 다릅니다.</mark> 두 출력을 모두 실었으니 내 경우에 맞는 쪽과 비교합니다. 키가 있을 때의 요약 문장은 한 예이고 실행할 때마다 달라집니다.

---

## 실습 5-1 정답

**터미널에 입력합니다.**

```bash
pwd
python exercise5-1_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 세 군데(① · ② · ③)입니다.

```python
    # ① "; " 에 .join(meanings) 를 붙여, 사실 문장을 이어 붙인 결과를 meaning_text 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    meaning_text = "; ".join(meanings)                  # 사실 문장들을 "; " 로 이어 붙여 문자열 하나로 만든다
```

```python
    # ② summary 가 빈 문자열("")이면   # ← 이 주석 바로 아래 줄에 씁니다 (4칸)
    if summary == "":                                   # 요약이 빈 문자열이면(호출이 실패했으면)
    # ③ FAIL_TEXT 를 summary 에 담는다   # ← 이 주석 바로 아래 줄에 씁니다 (8칸)
        summary = FAIL_TEXT                             # 대체 문장을 쓴다
```

<mark>주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 점수 기록은 <mark style="background:#bde3ff">**5건**</mark>, 요약할 대상은 <mark style="background:#bde3ff">**3명**</mark>(dami · seoyeon · gaeun)입니다. `(요약 실패 …)` 가 나온 대상은 키가 있을 때 0명, 키가 없을 때 3명입니다.

**키가 있을 때** — 단계 4 의 문장은 AI 가 쓴 한 예이고 사람마다 다릅니다.

```
--- 단계 1: 불러온 점수 기록 5 건
--- 단계 2: 요약할 대상 3 명 (최대 3 명)
high dami 60
mid seoyeon 45
mid gaeun 40
--- 단계 3: AI 에게 보내는 글 (seoyeon)
당신은 보안 관제 담당자를 돕는 도우미입니다. 아래 [사실]만 사용해 한국어 두 문장 이하로 요약하세요. [사실]에 없는 내용은 지어내지 말고, 공격이라고 단정하지 마세요. 먼저 확인할 것을 한 가지 제안하세요.
[사실] 대상: seoyeon / 등급: mid / 점수: 45점 / 탐지된 내용: 평소와 다른 IP 에서 SaaS 에 접속함; SaaS 에서 파일을 한꺼번에 많이 내려받음
--- 단계 4: Gemini API 를 활용한 AI 요약
dami : 퇴사한 사람의 계정으로 서버에 요청한 기록이 있습니다. 먼저 이 계정이 비활성화되어 있는지 확인하세요.
seoyeon : 평소와 다른 IP 에서 접속하고 파일을 한꺼번에 많이 내려받은 기록이 있습니다. 먼저 내려받은 파일 목록을 확인하세요.
gaeun : 규칙으로는 허용되는 요청을 서버가 거절했고, 서로 다른 로그에서 짧은 시간 안에 이벤트가 확인되었습니다. 먼저 거절된 요청의 서버 설정을 확인하세요.
```

**키가 없을 때** — 단계 1 ~ 3은 같고, 단계 4 에서 호출마다 `[LLM 호출 실패] API 키 없음` 이 나온 뒤 대체 문장이 들어갑니다. 키가 있어도 한도를 넘으면 그 자리에 `[LLM 호출 실패] 상태 코드 429` 가 나옵니다.

```
--- 단계 4: Gemini API 를 활용한 AI 요약
[LLM 호출 실패] API 키 없음
dami : (요약 실패 — 점수와 이유를 직접 확인)
[LLM 호출 실패] API 키 없음
seoyeon : (요약 실패 — 점수와 이유를 직접 확인)
[LLM 호출 실패] API 키 없음
gaeun : (요약 실패 — 점수와 이유를 직접 확인)
```

- 키가 없으면 (가)에는 이 출력을 붙이고 「요약한 대상 3명, 요약 실패 3명」이라고 적습니다. (다)는 위 「키가 있을 때」의 요약 하나를 골라 비교해 씁니다.

- (나) 지시문이 하지 말라고 한 것은 <mark style="background:#bde3ff">**[사실]에 없는 내용을 지어내는 것**</mark>과 <mark style="background:#bde3ff">**공격이라고 단정하는 것**</mark> 두 가지입니다.
  - 지어내는 것이 위험한 이유: 점수 파일에 없는 사고를 AI 가 쓰면 담당자가 없는 일을 조사하게 되고, 실제로 확인할 대상은 뒤로 밀립니다.
  - 단정하는 것이 위험한 이유: 점수와 등급은 먼저 확인할 순서를 뜻할 뿐 공격이라는 판정이 아닙니다. 예를 들어 dami 는 `퇴사한 계정` 한 가지로 high 이지만, 파일에는 어떤 사고가 있었다는 내용이 없습니다. 「공격이 있었다」고 쓰면 파일에 없는 판단을 사실처럼 말하는 것입니다.
- (다) 한 예: seoyeon 의 요약이 「평소와 다른 IP 에서 접속하고 파일을 많이 내려받았습니다. 먼저 내려받은 파일의 목록을 확인하세요.」라면 <mark style="background:#bde3ff">표에 없는 내용이 없고, 탐지된 규칙 두 개(평소와 다른 IP · 대량 다운로드)가 모두 들어 있습니다.</mark>
  - 만약 요약에 「계정이 해킹당했습니다」 같은 문장이 있다면 표에 없는 단정입니다. 이 경우에는 지시문의 「공격이라고 단정하지 마세요」 앞에 「[사실]에 적힌 것만 말하세요」를 한 번 더 적고 다시 실행해 문장이 사라지는지 확인합니다.
  - 탐지된 규칙이 하나 빠졌다면 [사실]에는 두 규칙이 모두 있는데 AI 가 한 가지만 쓴 것입니다. 지시문에 「탐지된 내용을 모두 포함하세요」를 더하는 방법이 있습니다.

**왜**

- <mark>점수와 등급은 코드가 정하고, AI 는 코드가 정한 값을 문장으로 풀어 쓰기만 합니다.</mark> AI 의 문장은 실행마다 달라지지만 확인할 순서는 바뀌지 않습니다. 그리고 보내는 글에 값을 그대로 넣었기 때문에 담당자가 [사실]과 요약을 나란히 보고 틀린 곳을 찾을 수 있습니다.

**자주 틀리는 곳**

- ① 에서 `.join` 을 쓰지 않고 `meaning_text = meanings` 로 쓰면 오류는 나지 않지만 <mark>**[사실]의 탐지된 내용에 대괄호와 따옴표가 그대로 나옵니다.**</mark> 단계 3 의 마지막 줄이 이 실수의 모습입니다.

```
--- 단계 3: AI 에게 보내는 글 (seoyeon)
당신은 보안 관제 담당자를 돕는 도우미입니다. 아래 [사실]만 사용해 한국어 두 문장 이하로 요약하세요. [사실]에 없는 내용은 지어내지 말고, 공격이라고 단정하지 마세요. 먼저 확인할 것을 한 가지 제안하세요.
[사실] 대상: seoyeon / 등급: mid / 점수: 45점 / 탐지된 내용: ['평소와 다른 IP 에서 SaaS 에 접속함', 'SaaS 에서 파일을 한꺼번에 많이 내려받음']
```

- ② 에서 `==` 대신 `=` 를 하나만 써서 `if summary = "":` 로 쓰면 실행하자마자 `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?` 가 납니다(파이썬 버전에 따라 뒷부분 문구가 다를 수 있습니다). <mark>**같은지 비교할 때는 `==` 입니다.**</mark>
- ③ 을 8칸이 아니라 4칸에서 시작하면 `IndentationError: expected an indented block after 'if' statement` 가 납니다. ③ 은 ② 의 `if` 안쪽 줄이라 한 단계 더 들여 씁니다.
- ② · ③ 을 빠뜨리면 평소에는 문제가 없다가 <mark>**AI 호출이 실패했을 때 요약 자리가 빈칸으로 나옵니다.**</mark> 키가 없을 때나, 무료 키의 한도(1분에 15번)를 넘어 `429` 가 나는 때가 그렇습니다. 오류가 아니라서 눈에 띄지 않는 것이 문제입니다. 아래는 키가 없을 때의 모습이고, 한도를 넘었으면 `API 키 없음` 자리에 `상태 코드 429` 가 나옵니다.

```
[LLM 호출 실패] API 키 없음
dami :
[LLM 호출 실패] API 키 없음
seoyeon :
[LLM 호출 실패] API 키 없음
gaeun :
```

**관제에서는**

- Gemini API 를 활용한 AI 요약은 담당자가 점수와 이유를 읽는 시간을 줄이는 도구입니다. <mark>값은 규칙이 정하고 AI 는 설명만 하게 하면, AI 가 틀려도 확인할 순서는 안 틀립니다.</mark>

---

## 실습 5-2 정답

**용어 풀이**

| 용어 | 뜻 |
|---|---|
| 데이터 문제 | 로그나 알림 같은 <mark>자료</mark>에 있어야 할 것이 없거나, 빠졌거나, 깨져 있는 경우 |
| 규칙 문제 | 「무엇을 의심할지」 정해 둔 <mark>기준</mark>이 없거나 현실과 맞지 않는 경우 |
| 운영 설정 문제 | 서버를 켜고 접속을 허용하는 <mark>설정</mark>이 목적과 맞지 않는 경우 |

아래 답은 한 예이고, 상황마다 원인이 겹치면 겹치는 대로 쓰면 맞습니다. 3개 이상 썼으면 됩니다.

#### 상황 1 · 설정 파일 주소를 연달아 요청했는데 「의심」이 아니라 「오류」로 분류됨

- 원인: <mark style="background:#bde3ff">규칙 문제</mark>입니다.
  - `is_suspicious` 는 요청 하나의 상태 코드가 401 · 403 이거나 경로에 `/admin` 이 있을 때만 「의심」으로 가릅니다.
  - 198.51.100.90 의 세 요청은 상태 코드가 모두 404 이고 경로에 `/admin` 이 없어서 의심 조건에 맞지 않습니다. 400 이상이라는 `is_error` 조건에만 맞아서 「오류」가 됩니다.
  - 한 줄씩은 흔한 404 이지만, 설정 파일 · 관리 화면 주소를 1초 간격으로 연달아 요청한 것은 탐색입니다. 이 규칙은 경로 이름도 같은 주소의 반복도 보지 않습니다.
- 고칠 파일: `log_classify.py`(Unit 1 응용 1-1 의 파일입니다. 응용을 하지 않아 파일이 없어도, 고칠 곳은 실습 5-2 레슨에 실린 `is_suspicious` 조각으로 정합니다)
- 어떻게 고치나요:
  - 케이스 A: <mark style="background:#bde3ff">값을 바꿉니다.</mark> `is_suspicious` 에 「경로에 `/.env` · `/wp-login` · `/phpmyadmin` 중 하나가 들어 있다」는 조건을 하나 더하고 `or` 로 잇습니다.
  - 케이스 B: 경로 목록만 늘리면 목록에 없는 새 주소는 또 놓칩니다. 그래서 같은 IP 가 없는 주소를 연달아 요청하는 횟수를 세는 규칙을 <mark style="background:#bde3ff">새로 넣습니다.</mark> 이런 규칙은 Unit 3 응용 3-3 의 `find_scan_ips` 로 이미 만들었습니다.
- 고친 뒤 확인: 같은 로그를 다시 분류해서 198.51.100.90 의 세 줄이 「의심」 목록에 나오는지 봅니다. 분류별 개수는 정상 15 · 오류 5 · 의심 8 에서 정상 15 · 오류 2 · 의심 11 로 바뀝니다.
- 담당자가 가장 먼저 할 일: 198.51.100.90 의 같은 시간대 요청이 더 있었는지, 성공(200)한 요청이 있었는지 접속 기록에서 확인합니다.

#### 상황 2 · 로그 30줄이 이벤트 28개가 됨

- 원인: <mark style="background:#bde3ff">데이터 문제</mark>입니다.
  - 원본 로그 30줄 가운데 2줄은 `GET /board/5 HTTP/1.1` 에서 잘려 있거나 `-` 하나만 있어서 큰따옴표가 두 개보다 적습니다.
  - `normalize_web` 은 이런 줄을 읽지 않고 `None` 을 리턴하므로 이벤트가 되지 못합니다. 그래서 웹 서버 이벤트가 30개가 아니라 28개입니다.
  - 줄이 사라진 것이 아니라 읽기 실패로 센 것입니다. Unit 1 실습 1-2 실행 파일의 단계 1 에 `읽기 실패 2 줄` 로 나옵니다.
- 고칠 파일: 고칠 코드는 없습니다. 정규화 코드(`normalize_web.py`)는 의도한 대로 동작했고, 문제는 원본 로그의 두 줄입니다.
- 어떻게 고치나요:
  - 케이스 A: 코드를 바꾸지 않고 <mark style="background:#bde3ff">확인합니다.</mark> 읽기 성공 28 + 읽기 실패 2 = 전체 30 이 맞는지 계산해 보고서에 적어 둡니다.
  - 케이스 B: 로그를 만드는 서버에서 줄이 끊기는 원인을 찾아 고칩니다. 이 과정에서는 서버 설정을 바꾸지 않았습니다.
- 고친 뒤 확인: 정규화한 이벤트 수와 읽기 실패 줄 수를 더해 원본 줄 수 30 과 같은지 봅니다. 같으면 사라진 줄 없이 모두 설명됩니다.
- 담당자가 가장 먼저 할 일: 읽지 못한 2줄의 원문을 원본 로그에서 찾아, 서버가 로그를 쓰는 도중 끊긴 것인지 확인합니다.

#### 상황 3 · 웹 서버 로그에서 사용자를 알 수 있는 요청이 1개뿐

- 원인: <mark style="background:#bde3ff">데이터 문제</mark>입니다.
  - 웹 서버 로그에는 사용자 이름이 없고 IP 주소만 있어서 이벤트의 `user` 가 `None` 입니다.
  - 사용자를 알려면 SaaS 에서 로그인에 성공한 IP 를 찾아 연결해야 합니다(`make_ip_user_map`). 웹 서버 실패 요청 13개 중 이렇게 사용자를 알 수 있는 것은 198.51.100.77(gaeun)의 `/admin` 1개뿐입니다.
  - 203.0.113.50 은 SaaS 로그와 판정 서버 로그에 기록이 없어서 누구의 일인지 알 수 없습니다.
- 고칠 파일: 케이스 A 는 웹 서버의 로그 설정, 케이스 B 는 `risk_scores.py` 입니다.
- 어떻게 고치나요:
  - 케이스 A: <mark style="background:#bde3ff">새로 넣습니다.</mark> 웹 서버가 로그인한 사용자의 이름도 로그 한 줄에 남기도록 설정을 바꿉니다. 이 과정에서는 서버 설정을 바꾸지 않았습니다.
  - 케이스 B: 사용자를 모르는 요청은 사용자가 아니라 IP 를 대상으로 점수를 매깁니다. 경로 스캔 198.51.100.90 을 IP 로 점수를 매긴 것이 이 방식입니다.
- 고친 뒤 확인: 케이스 A 는 다시 실행해 「IP 로 사용자를 알 수 있는 웹 실패 이벤트」 수가 1개보다 늘었는지 봅니다. 케이스 B 는 점수 파일의 `entity` 에 IP(198.51.100.90)가 나오는지 봅니다.
- 담당자가 가장 먼저 할 일: 203.0.113.50 으로 로그인한 기록이 다른 로그에 있는지 검색해 계정을 찾습니다.

#### 상황 4 · 두 로그에 나오는 seoyeon 이 연결되지 않음

- 원인: <mark style="background:#bde3ff">규칙 문제</mark>입니다.
  - `find_chains` 는 사용자의 하루 첫 이벤트부터 마지막 이벤트까지 걸린 시간(`span`)이 `WINDOW_MINUTES`(60분) 이내여야 연결합니다.
  - seoyeon 의 이벤트는 09:05 부터 18:20 까지 흩어져 있어서 `span` 이 555분이고 연결되지 않습니다. 17:38 의 로그인부터 18:20 의 서버 거절까지는 42분인데, 하루 전체로 계산해서 놓칩니다.
  - gaeun 은 이벤트 3종류가 41분 안에 있어서 연결됩니다.
- 고칠 파일: `correlation.py`
- 어떻게 고치나요:
  - 케이스 A: <mark style="background:#bde3ff">값을 바꿉니다.</mark> `WINDOW_MINUTES` 를 600 으로 올리면 이 샘플에서는 seoyeon 이 `서로 다른 로그 2종류 · 555분 안` 으로 연결됩니다. 하지만 하루 전체가 한 사건이 되어 「짧은 시간 안에 모였다」는 뜻이 약해집니다.
  - 케이스 B: `find_chains` 의 계산 방식을 <mark style="background:#bde3ff">바꿉니다.</mark> 첫 이벤트와 마지막 이벤트의 차이 대신, 이웃한 이벤트 사이가 60분 이내로 이어지는 이벤트끼리만 한 사건으로 묶습니다.
- 고친 뒤 확인: 다시 실행해 seoyeon 이 연결된 사건에 나오는지, 연결 이유에 적힌 분이 어떻게 달라졌는지 봅니다. 케이스 A 에서는 이유에 `555분 안` 이 나옵니다.
- 담당자가 가장 먼저 할 일: seoyeon 의 17:38 로그인부터 18:20 서버 거절까지를 시간순으로 읽습니다.

#### 상황 7 · 정산 조회 시도에는 알림이 나지 않음

- 원인: <mark style="background:#bde3ff">규칙 문제</mark>입니다(그 일을 잡는 규칙이 없습니다).
  - 서버 거절 규칙(`pick_suspicious`)은 한 사용자의 서버 실패가 `REPEAT_LIMIT`(3번) 이상일 때만 먼저 확인합니다.
  - seoyeon 의 서버 실패는 11:40 의 `SETTLE:QUERY` 와 18:20 의 `SALES:CHANGE` 두 번뿐이라 기준에 못 미칩니다. 그래서 P5 는 알림 대상이 아닙니다.
  - 횟수만 보는 규칙은 정산처럼 중요한 권한을 권한 없이 한 번 건드린 일을 놓칩니다.
- 고칠 파일: `access_detection.py`
- 어떻게 고치나요: <mark style="background:#bde3ff">새로 넣습니다.</mark>
  - 중요한 권한 목록(예: `SETTLE:QUERY`)을 정하고, 서버 실패 이벤트의 행동이 그 목록에 있으면 횟수와 상관없이 확인 대상에 넣는 함수를 `pick_suspicious` 옆에 더합니다.
  - 이 규칙은 업무상 실수로 한 번 건드린 사용자까지 알려서 오탐이 늘 수 있습니다.
- 고친 뒤 확인: 같은 이벤트로 다시 실행해 P5 가 알림 대상에 나오는지 보고, Unit 4 응용 4-2 처럼 오탐과 미탐을 다시 세어 오탐이 얼마나 늘었는지 봅니다.
- 담당자가 가장 먼저 할 일: seoyeon 에게 11:40 의 정산 조회가 업무 요청이었는지 확인합니다.

## 응용 5-1 정답

> **여유가 되면 해 보세요.** 여기부터는 응용 정답입니다. 응용을 한 사람만 봅니다. 응용 5-1 · 5-2는 Docker Desktop 이 있어야 합니다.

**터미널에 입력합니다.**

```bash
docker ps --filter publish=8080 --filter publish=8081 --filter publish=8082
docker images nginx:1.28
docker pull nginx:1.28
docker run -d --rm -p 8080:80 --name web-run nginx:1.28
docker ps
docker stop web-run
ls
docker compose up -d
docker compose ps
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
```
- 명령 풀이: `docker ps --filter publish=포트번호` 그 포트를 쓰는 서버 확인(줄이 나오면 `docker stop 이름` 으로 끔) · `docker images 이름:버전` 받아 둔 이미지 확인(있으면 `docker pull` 은 건너뜀) · `docker compose up -d` 컴포즈 파일의 서버를 모두 백그라운드에서 켬 · `docker compose ps` 컴포즈로 켠 서버의 상태 보기 · `curl 주소` 그 주소에 요청을 보내 결과 번호 보기

**결과**

- (가) 서버 켜기 · 확인 명령과 결과를 친 순서대로 붙인 예입니다. 서비스 이름은 <mark style="background:#bde3ff">**`web1` · `web2`**</mark>, 포트는 <mark style="background:#bde3ff">**8080 · 8081**</mark>입니다.

  ```
  $ docker images nginx:1.28
  IMAGE        ID             DISK USAGE   CONTENT SIZE   EXTRA
  nginx:1.28   146adea4768b        258MB         64.1MB   U
  $ docker run -d --rm -p 8080:80 --name web-run nginx:1.28
  e1a2ad01c5441866eae9a81e97aa28caabf3a1efdd4c12bf66817887c63237a4
  $ docker ps
  CONTAINER ID   IMAGE        COMMAND                  CREATED                  STATUS                  PORTS                                     NAMES
  e1a2ad01c544   nginx:1.28   "/docker-entrypoint.…"   Less than a second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web-run
  $ docker stop web-run
  web-run
  $ docker compose up -d
   Network anomaly_detection_default Creating
   Network anomaly_detection_default Created
   Container anomaly_detection-web1-1 Creating
   Container anomaly_detection-web2-1 Creating
   Container anomaly_detection-web1-1 Created
   Container anomaly_detection-web2-1 Created
   Container anomaly_detection-web2-1 Starting
   Container anomaly_detection-web1-1 Starting
   Container anomaly_detection-web2-1 Started
   Container anomaly_detection-web1-1 Started
  $ docker compose ps
  NAME                       IMAGE        COMMAND                  SERVICE   CREATED                  STATUS                  PORTS
  anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      Less than a second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
  anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      Less than a second ago   Up Less than a second   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp
  $ curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
  200
  $ curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
  200
  ```

  - 이미지가 없어서 `docker pull` 을 했다면 그 결과도 맨 앞에 붙입니다. 컨테이너 번호(긴 글자)와 시각은 사람마다 다릅니다.

- (나) 컴포즈가 더 나은 점의 예:
  - <mark style="background:#bde3ff">긴 옵션을 파일에 적어 두어서 누가 켜도 같은 서버가 켜집니다.</mark>
  - 명령 한 줄(`docker compose up -d`)로 서버 두 대를 한 번에 켜고 끌 수 있습니다.
  - 파일을 저장소에 올려 두면 서버 설정이 기록으로 남습니다.
- (다) 두 팀의 차이:
  - `docker run` 팀은 <mark style="background:#bde3ff">명령을 기억하지 못하면 포트 · 이름 · 이미지 버전을 알 수 없어서 같은 구성을 다시 켤 수 없고,</mark> 켠 기록도 남아 있지 않습니다.
  - 컴포즈 팀은 `compose.yaml` 과 깃허브 기록이 있어서 <mark style="background:#bde3ff">`docker compose up -d` 한 줄로 같은 구성을 다시 켤 수 있습니다.</mark>
  - 버전을 적어 두는 것이 중요한 이유: `nginx:1.28` 처럼 적어 두면 <mark style="background:#bde3ff">몇 주 뒤에도 같은 버전의 이미지로 켜서</mark> 사고 당시와 같은 환경이 됩니다. 이름만 적으면(`nginx`) 가장 최신 버전을 받아 와서 동작이 달라질 수 있어, 재현한 결과를 믿기 어렵습니다.
- (라) 바꿀 줄:
  - `web2` 의 <mark style="background:#bde3ff">`- "8081:80"` 에서 왼쪽 숫자만</mark> 다른 프로그램이 쓰지 않는 번호로 바꿉니다. 예: `- "8082:80"`
  - 서버 안이 그대로 `80` 인 이유: 콜론 <mark style="background:#bde3ff">왼쪽은 내 컴퓨터의 포트이고, 오른쪽은 서버(컨테이너) 안의 포트이기 때문입니다.</mark> 내 컴퓨터 쪽 번호만 바꿨으므로 서버 안은 달라지지 않습니다.
  - `curl` 이 달라지는 점: 요청 주소의 포트를 <mark style="background:#bde3ff">왼쪽 숫자로 바꿔서</mark> `curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8082` 로 칩니다. 다른 팀원은 그대로 `8081` 입니다.

**왜**

- <mark>서버 설정을 파일에 적어 두면 사람이 옵션을 외우거나 두 번 치지 않아도 되어서 실수가 줄고, 서버가 늘어도 명령은 그대로입니다.</mark>

**자주 틀리는 곳**

- 1 ~ 2번에서 켠 `web-run` 을 `docker stop web-run` 으로 끄지 않고 `docker compose up -d` 를 치면 <mark>**`web1` 서버가 켜지지 않습니다.**</mark> 같은 8080번 포트를 `web-run` 이 이미 쓰고 있기 때문입니다.
  - 이때 오류는 다음과 같습니다(<mark style="background:#ffc4d6">`port is already allocated`</mark> 가 나오면 이 실수입니다).

    ```
    Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint anomaly_detection-web1-1 (…): Bind for 0.0.0.0:8080 failed: port is already allocated
    ```

  - 고치는 방법: `docker stop web-run` 으로 한 대짜리 서버를 끄고, 이미 켜진 `web2` 까지 `docker compose down` 으로 정리한 뒤 `docker compose up -d` 를 다시 칩니다.
- `compose.yaml` 의 들여쓰기에 탭 문자가 들어가면 오류가 납니다. <mark>**VS Code 에서 붙여 넣으면 이 오류는 나지 않지만,**</mark> 탭 문자를 직접 넣었다면 이런 문구가 나옵니다.

    ```
    yaml: while scanning for the next token at line 3: found character that cannot start any token
    ```

  - 줄 번호는 사람마다 다릅니다.
- `docker compose up -d` 를 `compose.yaml` 이 없는 폴더에서 치면 `no configuration file provided: not found` 가 나옵니다. <mark>`pwd` 로 `anomaly_detection` 폴더인지 먼저 봅니다.</mark>

**관제에서는**

- 로그를 모으는 서버나 대응 대상 서버를 여러 대 켜야 할 때 컴포즈 파일 하나로 같은 환경을 다시 만듭니다. <mark>설정 파일을 저장소에 두면 누가 어느 PC 에서 켜도 같은 환경이 됩니다.</mark>

---

## 응용 5-2 정답

**터미널에 입력합니다.**

```bash
docker compose ps
mkdir logs
docker compose -f compose.secure.yaml up -d
docker compose -f compose.secure.yaml ps
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8082
cat logs/access.log
grep " 404 " logs/access.log | wc -l
grep " 404 " logs/access.log > logs/web_404.log
docker compose -f compose.secure.yaml down
ls logs
```
- 명령 풀이: `-f 파일이름` 사용할 컴포즈 파일 지정 · `127.0.0.1:` 포트 줄 앞에 붙여 내 PC 에서만 접속 · `grep "글자" 파일` 그 글자가 든 줄만 남김 · `wc -l` 줄 수 세기 · `>` 출력을 파일에 저장

**결과**

- (가) 1번 출력은 두 서버 모두 `0.0.0.0:` 으로 시작하고, 5번 출력은 다음과 같습니다. 접속 범위가 바뀐 서비스는 <mark style="background:#bde3ff">**`web2`**</mark> 이고, 새로 생긴 서비스는 <mark style="background:#bde3ff">**`web3`**</mark> 입니다.

  ```
  NAME                       IMAGE        COMMAND                  SERVICE   CREATED        STATUS                  PORTS
  anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      1 second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
  anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      1 second ago   Up Less than a second   127.0.0.1:8081->80/tcp
  anomaly_detection-web3-1   nginx:1.28   "/docker-entrypoint.…"   web3      1 second ago   Up Less than a second   127.0.0.1:8082->80/tcp
  ```

- (나) `"8081:80"` 은 <mark style="background:#bde3ff">같은 네트워크의 다른 PC 에서도 접속할 수 있고</mark>, `"127.0.0.1:8081:80"` 은 <mark style="background:#bde3ff">내 PC 에서만 접속할 수 있습니다.</mark>
  - 이유: 관리 화면이나 데이터베이스는 필요한 사람만 쓰는 서버입니다. 밖에 열어 두면 스캐너가 `/phpmyadmin` 같은 주소를 찾아 들어올 수 있으므로 <mark style="background:#bde3ff">꼭 열어야 하는 서버만 열고 나머지는 `127.0.0.1:` 으로 제한합니다.</mark>
- (다) 서버마다 출력이 다른 이유는 다음과 같습니다.

  | 서버 | 출력 | 이유 |
  |---|---|---|
  | `web1` | `Running` | <mark style="background:#bde3ff">설정이 바뀌지 않아서</mark> |
  | `web2` | `Recreated` | <mark style="background:#bde3ff">포트 줄이 바뀌어서 기존 서버를 새 설정으로 다시 만들어서</mark> |
  | `web3` | `Created` | <mark style="background:#bde3ff">새로 추가한 서버라서</mark> |

  - 도움이 되는 점: 설정을 바꿔도 <mark style="background:#bde3ff">바뀐 서버만 다시 켜지고 나머지는 끊기지 않습니다.</mark> 운영 중인 서비스(`web1`)를 멈추지 않고 보안 설정을 고칠 수 있습니다.

**왜**

- <mark>서버마다 접속 범위를 파일에 적어 두면 설정 실수를 검토하기 쉽고, 같은 `up -d` 로 바뀐 서버만 적용하면 운영 중인 서비스가 끊기지 않습니다.</mark> `volumes` 로 연결해 두면 서버를 지워도 접속 기록 파일을 내 폴더에 남겨 줍니다.

**자주 틀리는 곳**

- `up -d` 에 `-f compose.secure.yaml` 을 빼고 `docker compose up -d` 만 치면 <mark>**아무것도 바뀌지 않습니다.**</mark> 응용 5-1의 `compose.yaml` 이 그대로 적용되기 때문입니다.
  - 이때 `ps` 의 PORTS 가 다음처럼 둘 다 `0.0.0.0:` 인 것이 이 실수의 모습입니다. `-f compose.secure.yaml` 을 붙여 다시 칩니다.

    ```
    SERVICE   PORTS
    web1      0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
    web2      0.0.0.0:8081->80/tcp, [::]:8081->80/tcp
    ```

- 8082번 포트를 이미 다른 서버가 쓰고 있으면 `web3` 이 켜지지 않습니다. <mark>응용 5-1 레슨의 「Docker Desktop 켜고 포트 확인하기」에서 `8082` 도 비어 있는지 봅니다.</mark>
  - 이때 오류는 다음과 같습니다(<mark style="background:#ffc4d6">`port is already allocated`</mark> 가 나오면 이 실수입니다).

    ```
    Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint anomaly_detection-web3-1 (…): Bind for 0.0.0.0:8082 failed: port is already allocated
    ```

- `web2` 의 포트 줄에서 `127.0.0.1:` 을 빼고 `"8081:80"` 으로 쓰면 <mark>오류는 나지 않지만 다시 모두에게 열립니다.</mark> 보안 설정은 오류가 나지 않아도 PORTS 로 확인해야 합니다.

**관제에서는**

- 서버를 새로 켤 때 「누구에게 열지」를 먼저 정하고, 열어 둔 포트는 `ps` 의 PORTS 로 확인합니다. <mark>외부에 열린 포트를 점검하는 일은 보안 점검의 첫 단계입니다.</mark>

---

## 응용 5-3 정답

**터미널에 입력합니다.**

```bash
pwd
python apply5-3_run.py
```
- 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `python 파일이름` 파이썬으로 실행 파일 실행

**채운 코드** (한 예) — 직접 쓰는 곳은 두 함수입니다.

① `analyze_events` 안

```python
    chains = find_chains_in_events(events)       # 이벤트에서 서로 다른 로그로 연결된 사건을 구한다
    findings = collect_findings(events, chains)  # 이벤트와 연결된 사건에서 탐지된 규칙을 모은다
    totals = score_findings(findings)            # 탐지된 규칙으로 대상별 점수를 더한다
    reasons = collect_reasons(findings)          # 대상마다 탐지된 규칙 이름을 모은다
```

② `build_report` 안

```python
    source_event_counts = events["source"].value_counts()                                  # 로그 종류마다 이벤트가 몇 개인지 센다
    source_count_dict = source_event_counts.to_dict()                                      # 센 결과를 JSON 에 저장할 수 있는 딕셔너리로 바꾼다
    report = {"date": REPORT_DATE, "event_count": len(events), "source_event_counts": source_count_dict,
              "finding_count": len(findings), "records": records, "summaries": summaries}  # 보고서 딕셔너리로 모은다
```

<mark>주석이 말한 일을 하면 맞습니다.</mark>

**결과**

- (가) 출력은 다음과 같고, 이벤트는 <mark style="background:#bde3ff">**57개**</mark>, 탐지된 규칙은 <mark style="background:#bde3ff">**8건**</mark>, 점수 기록은 <mark style="background:#bde3ff">**5건**</mark>, Gemini API 를 활용한 AI 요약은 <mark style="background:#bde3ff">**3건**</mark>(키가 있을 때 실패 0건, 키가 없을 때 실패 3건)입니다.

**키가 있을 때** — 단계 3 의 문장은 AI 가 쓴 한 예이고 사람마다 다릅니다.

```
--- 단계 1: 읽은 이벤트 57 개
--- 단계 2: 탐지된 규칙 8 건 → 점수 기록 5 건을 unit05_risk_scores.json 에 저장
--- 단계 3: Gemini API 를 활용한 AI 요약 3 건 (실패 0 건)
dami : 퇴사한 사람의 계정으로 서버에 요청한 기록이 있습니다. 먼저 이 계정이 비활성화되어 있는지 확인하세요.
seoyeon : 평소와 다른 IP 에서 접속하고 파일을 한꺼번에 많이 내려받은 기록이 있습니다. 먼저 내려받은 파일 목록을 확인하세요.
gaeun : 규칙으로는 허용되는 요청을 서버가 거절했고, 서로 다른 로그에서 짧은 시간 안에 이벤트가 확인되었습니다. 먼저 거절된 요청의 서버 설정을 확인하세요.
--- 단계 4: 보고서를 anomaly_detection_report_2026-11-02.json 에 저장
--- 단계 5: 확인할 순서
high dami 60
mid seoyeon 45
mid gaeun 40
mid jiwoo 35
low 198.51.100.90 30
```

- 보고서 파일 `anomaly_detection_report_2026-11-02.json` 의 값은 이렇습니다.

| 키 | 값 |
|---|---|
| `date` | `2026-11-02` |
| `event_count` | 57 |
| `source_event_counts` | 웹 서버 28 · 판정 서버 15 · SaaS 14 |
| `finding_count` | 8 |
| `records` | 5건 |
| `summaries` | 3건 |

- 파일의 앞부분은 다음과 같습니다.

```
{
  "date": "2026-11-02",
  "event_count": 57,
  "source_event_counts": {
    "web": 28,
    "server": 15,
    "saas": 14
  },
  "finding_count": 8,
  "records": [
    {
      "entity": "dami",
      "score": 60,
      "grade": "high",
      "reasons": [
        "퇴사한 계정"
      ]
    },
    …
  ],
  "summaries": [
    …
  ]
}
```

- (나) 점수와 등급을 코드가 정하는 이유는 <mark style="background:#bde3ff">같은 입력이면 항상 같은 결과가 나와야 확인할 순서가 흔들리지 않기 때문</mark>입니다.
  - 단계 5 의 확인할 순서(dami → seoyeon → gaeun → jiwoo → 198.51.100.90)는 Gemini API 를 활용한 AI 요약이 어떻게 나와도 같습니다. 점수는 `risk_scores.py` 의 `WEIGHTS` 와 등급 기준으로 정해지기 때문입니다.
  - 단계 3 의 요약 문장은 실행할 때마다 다르게 나올 수 있습니다. 순서를 AI 가 정하면 같은 로그로 실행해도 오늘과 내일의 순서가 달라질 수 있습니다.
  - AI 는 값을 풀어 쓰기만 해서, 요약이 틀려도 점수와 등급은 그대로입니다.
- (다) AI 호출이 실패해도 멈추지 않게 만든 이유는 <mark style="background:#bde3ff">AI 하나가 실패했다고 점수와 등급이 담긴 보고서까지 못 만들면 담당자가 아침에 아무것도 볼 수 없기 때문</mark>입니다.
  - 실패한 요약은 `(요약 실패 — 점수와 이유를 직접 확인)` 이라는 문장으로 채워지고, 단계 3 의 제목 줄에 실패 건수가 나옵니다.
  - 대체 문장이 들어간 대상은 담당자가 `records` 의 점수와 이유(`reasons`)를 직접 읽고 판단합니다. 1분 뒤에 다시 실행해 요약을 받을 수도 있습니다.
  - 실패했을 때의 출력은 다음과 같습니다(**키가 없을 때**, 3번 모두 실패한 경우). 키가 있는데 한도를 넘어 실패하면 `API 키 없음` 자리에 `상태 코드 429` 가 나옵니다. 보고서 파일의 `summaries` 에도 세 건 모두 대체 문장이 들어가고, `records` 는 키가 있을 때와 같습니다.

```
--- 단계 1: 읽은 이벤트 57 개
--- 단계 2: 탐지된 규칙 8 건 → 점수 기록 5 건을 unit05_risk_scores.json 에 저장
[LLM 호출 실패] API 키 없음
[LLM 호출 실패] API 키 없음
[LLM 호출 실패] API 키 없음
--- 단계 3: Gemini API 를 활용한 AI 요약 3 건 (실패 3 건)
dami : (요약 실패 — 점수와 이유를 직접 확인)
seoyeon : (요약 실패 — 점수와 이유를 직접 확인)
gaeun : (요약 실패 — 점수와 이유를 직접 확인)
--- 단계 4: 보고서를 anomaly_detection_report_2026-11-02.json 에 저장
--- 단계 5: 확인할 순서
high dami 60
mid seoyeon 45
mid gaeun 40
mid jiwoo 35
low 198.51.100.90 30
```

**왜**

- <mark>단계를 이어 실행할 때는 앞 단계의 결과를 다음 단계에 정확히 전달하고, 바깥 서비스(AI)처럼 실패할 수 있는 단계는 대체 값으로 이어 가게 만듭니다.</mark> 그래야 한 번 실행한 결과를 믿고 보고서로 보낼 수 있습니다.

**자주 틀리는 곳**

- 2번에서 `collect_findings(events, chains)` 의 순서를 바꿔 `collect_findings(chains, events)` 로 쓰면 `TypeError` 오류가 납니다. <mark>**함수에 전달하는 순서는 정의한 순서(이벤트 표, 연결된 사건)입니다.**</mark>
  - 실행하면 다음 오류가 납니다(<mark style="background:#ffc4d6">`list indices must be integers or slices, not str`</mark> 가 나오면 이 실수입니다).

```
Traceback (most recent call last):
  File "…/anomaly_detection/apply5-3_run.py", line 3, in <module>
  File "…/anomaly_detection/pipeline.py", line 75, in run_pipeline
  File "…/anomaly_detection/pipeline.py", line 17, in analyze_events
  File "…/anomaly_detection/risk_scores.py", line 31, in collect_findings
  File "…/anomaly_detection/access_detection.py", line 21, in pick_server_failures
TypeError: list indices must be integers or slices, not str
```

  - 줄 번호는 사람마다 다릅니다.
- 1번을 빠뜨리면 2번 줄에서 `NameError` 가 납니다. <mark>**앞 단계의 결과 `chains` 가 만들어지지 않았기 때문입니다.**</mark>

```
Traceback (most recent call last):
  File "…/anomaly_detection/apply5-3_run.py", line 3, in <module>
  File "…/anomaly_detection/pipeline.py", line 74, in run_pipeline
  File "…/anomaly_detection/pipeline.py", line 16, in analyze_events
NameError: name 'chains' is not defined
```

- 6번에서 `.to_dict` 의 괄호를 빼거나, 6번을 통째로 쓰지 않고 시리즈(pandas 의 열 하나)를 그대로 보고서에 넣으면 `TypeError` 가 납니다. <mark>**`.to_dict()` 는 괄호까지 써야 합니다.**</mark> 보고서를 저장하는 단계에서 오류가 나고, 단계 4 의 제목 줄 앞까지는 정상으로 출력됩니다.
  - 괄호를 빼면 다음 오류가 납니다(<mark style="background:#ffc4d6">`Object of type method is not JSON serializable`</mark>).

```
Traceback (most recent call last):
  File "…/anomaly_detection/apply5-3_run.py", line 3, in <module>
  File "…/anomaly_detection/pipeline.py", line 86, in run_pipeline
  File "…/anomaly_detection/pipeline.py", line 65, in save_report
TypeError: Object of type method is not JSON serializable
```

  - `.to_dict()` 를 쓰지 않고 시리즈를 그대로 넣으면 `Object of type Series is not JSON serializable` 오류가 납니다.
- 7번의 딕셔너리에서 키와 값 묶음 사이의 쉼표를 빼면 실행하기 전에 `SyntaxError` 가 납니다(오류 문구는 파이썬 버전마다 조금 다릅니다).

```
  File "…/anomaly_detection/pipeline.py", line 56
    "finding_count": len(findings), "records": records, "summaries": summaries}
    ^
SyntaxError: invalid syntax
```

**관제에서는**

- 여러 단계를 한 번에 실행하는 프로그램은 어느 단계가 어떤 결과를 냈는지 단계마다 한 줄씩 출력해 둡니다. <mark>그래야 결과가 이상할 때 어느 단계에서 틀어졌는지 바로 찾을 수 있습니다.</mark>

---
