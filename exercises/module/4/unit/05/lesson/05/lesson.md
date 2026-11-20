---
id: m4-u05-l05
title: 도전 5-2 · 서버별 접속 범위 정하고 적용하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/112_day05_pm_docker_compose_logs.md
  mission_id: GichanSource.m4-1106-pm-docker-compose-logs
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 도전 5-2 · 서버별 접속 범위 정하고 적용하기

## 목표: 서버 세 대의 접속 범위

> **선택입니다. 시간이 남을 때 합니다.** 도전 5-1에서 켠 서버 두 대(`web1` · `web2`)에 이어서 하므로 <mark>도전 5-1을 먼저 마칩니다.</mark> 하지 않아도 이번 Unit을 마무리하고 Module 5를 따라가는 데 문제가 없습니다.

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「지금 켜 둔 서버 두 대(`web1` · `web2`)는 같은 네트워크에 있는 다른 사람의 PC 에서도 들어올 수 있습니다. 그런데 앞으로 관리자만 써야 하는 서버와 접속 기록을 모아 두는 서버를 더 켤 예정입니다. 이런 서버가 다른 사람에게 열려 있으면 위험합니다.
>
> 서버를 한 대 더 늘려서 이렇게 해 주세요.
> - ① `web1` 은 지금처럼 누구나 들어올 수 있게 둡니다.
> - ② `web2` 와 `web3` 은 **내 PC 에서만** 들어올 수 있게 바꿉니다.
> - ③ `web3` 의 접속 기록은 내 폴더에 파일로 남겨 주세요.
>
> 그리고 `web1` 은 지금 쓰고 있으니 중간에 끊기면 안 됩니다.」
> - **왜 중요한가**:
> - <mark>열면 안 되는 서버를 다른 사람에게 열어 두는 실수는 보안 사고의 대표적인 원인입니다.</mark> 예를 들어 서버를 설정하는 관리 화면이 열려 있으면, 권한이 없는 사람도 들어오려고 시도할 수 있습니다.
> - <mark>설정을 바꿔도 바뀐 서버만 다시 만들고, 바뀌지 않은 `web1` 은 계속 실행합니다.</mark> 그래서 쓰고 있는 서버를 끊지 않고 고칠 수 있습니다.
> - 서버를 지우면 서버 안의 접속 기록도 같이 사라집니다. 기록을 내 폴더에 연결해 두면, 서버를 지워도 파일이 남습니다.

## 왜 서버마다 접속 범위를 정하는가

1. 이번 실습의 질문은 하나입니다. <mark>**서버마다 접속 범위(접속 범위: 어느 PC 에서 그 서버에 접속할 수 있는지)를 컴포즈 파일에 적고, 서버를 끊지 않고 바꿔 적용할 수 있는가?**</mark>
2. 도전 5-1에는 두 서버가 모두 같은 방식(`"8080:80"`)으로 열려 있었습니다. 서버가 늘면 서버마다 열 범위를 따로 정해야 합니다.
3. 컴포즈는 파일을 고치고 같은 `docker compose up -d` 를 치면, 바뀐 서버만 다시 만들고 나머지는 그대로 둡니다.

## 2.1 포트 줄에 접속 범위가 들어 있다

`127.0.0.1` 은 내 컴퓨터를 가리키는 주소입니다. 포트 줄 맨 앞에 붙이면 내 PC 에서만 접속할 수 있습니다.

| 포트 줄 | 읽는 법 | 누가 접속할 수 있나 |
|---|---|---|
| `"8080:80"` | 내 컴퓨터의 8080번 → 서버 안의 80번 | <mark>같은 네트워크의 다른 PC 도 가능</mark> (모두에게 열림) |
| `"127.0.0.1:8081:80"` | 맨 앞에 `127.0.0.1` 을 붙임 | <mark>내 PC 에서만</mark> |

- `docker compose ps` 의 PORTS 에서 읽을 수 있습니다. `0.0.0.0:8080` 은 모두에게 열린 것이고, `127.0.0.1:8081` 은 내 PC 에서만 열린 것입니다.
- <mark>관리 화면 · 데이터베이스처럼 밖에 열면 안 되는 서버는 `127.0.0.1:` 을 붙여 둡니다.</mark> 이것이 이번 실습 문제의 실무 의미입니다.

## 2.2 up -d 의 출력은 서버마다 다르게 읽는다

| 출력 | 뜻 | 이번 파일에서 |
|---|---|---|
| `Running` | 설정이 같아서 그대로 둠 | `web1` |
| `Recreate` → `Recreated` | 설정이 바뀌어 기존 서버(컨테이너)를 새 설정으로 다시 만듦 | `web2` (포트 줄이 바뀜) |
| `Created` | 새로 만듦 | `web3` |

- <mark>`web1` 은 설정이 바뀌지 않아서 끊기지 않습니다.</mark> 서버가 여러 대여도 바뀐 서버만 다시 켜지는 것이 컴포즈를 쓰는 이유입니다.

## 2.3 로그를 내 폴더에 남기고 다루기

- <mark>`volumes` 는 내 폴더와 서버 안 폴더를 연결하는 설정입니다.</mark> `- ./logs:/var/log/nginx` 는 서버가 로그를 쓰는 폴더(오른쪽)를 내 `logs` 폴더(왼쪽)에 연결한다는 뜻입니다.
- 연결해 두면 로그가 내 폴더의 파일로 쌓이고, 서버를 지워도(`down`) 파일은 남습니다. 서버 안에만 있는 로그는 서버와 함께 사라집니다.
- 그 파일을 다룰 때 아래 세 표시를 씁니다.

| 표시 | 하는 일 | 이번 실습에서 쓰는 곳 |
|---|---|---|
| `\|` (파이프, pipe: 앞 명령의 출력을 뒤 명령에 넘김) | 왼쪽 명령의 출력을 오른쪽 명령에 넘긴다 | `grep " 404 " logs/access.log \| wc -l` |
| `grep "글자"` (그렙: 글자가 들어 있는 줄만 남김) | 파일이나 출력에서 그 글자가 든 줄만 남긴다 | `grep " 404 " logs/access.log` |
| `> 파일이름` (리다이렉션, redirection: 출력을 화면 대신 파일에 저장) | 화면에 나올 내용을 파일에 저장한다 | `> logs/web_404.log` |

- `wc -l` 은 줄이 몇 개인지 세어 줍니다. 위 파이프 예시는 「`404` 가 든 줄이 몇 개인가」입니다.

## 도전 5-2 · 서버별 접속 범위 정하고 적용하기

> **이 문제를 내는 이유**
> - **서버마다 열 범위를 정하는 연습입니다.** 접속 범위는 보안 설정의 가장 기본이고, 컴포즈 파일의 포트 줄 하나로 정해집니다.
> - **서버를 끊지 않고 설정을 바꾸는 방법을 확인합니다.** `web1` 이 `Running` 으로 남는 것을 직접 보면 컴포즈를 왜 쓰는지 알 수 있습니다.
> - **로그를 내 폴더에 남기는 방법도 익힙니다.** `grep` 으로 다루고, 서버를 지워도 접속 기록 파일이 남는 것을 확인합니다.

**이런 상황이 있습니다**

- **지금은**: <mark>도전 5-1에서 켠 서버 두 대가 모두 같은 네트워크의 다른 PC 에서 접속할 수 있게 열려 있고, 서버를 늘리거나 접속 범위를 바꾸는 방법을 정하지 않았습니다</mark>.
- **그래서 하는 것**:
  - 새 컴포즈 파일 `compose.secure.yaml` 로 서버를 세 대로 늘립니다.
  - `web2` · `web3` 의 포트 줄에 `127.0.0.1:` 을 붙여 내 PC 에서만 접속되게 합니다.
  - `web1` 이 끊기지 않고 `Running` 으로 남는지 `up -d` 의 출력으로 확인합니다.
  - `web3` 의 로그를 내 `logs` 폴더 파일로 남기고 `grep` 으로 다룹니다.
- **실행하면**: <mark>`up -d` 에서 `web1` 은 `Running`, `web2` 는 `Recreated`, `web3` 은 `Created` 로 나오고, `ps` 의 PORTS 에 `web2` · `web3` 은 `127.0.0.1:` 이 붙습니다.</mark>
- **현업에서는**: 서버마다 공개 범위를 컴포즈 파일에 적어 두고, 설정을 바꿀 때는 파일을 고쳐 같은 `docker compose up -d` 로 적용합니다. 설정이 바뀐 서버만 다시 만들어지고 바뀌지 않은 서버는 계속 실행됩니다. 이번 실습에서는 설정이 그대로인 `web1` 이 계속 실행되는 것을 확인합니다.

**할 일**

1. 도전 5-1 서버의 접속 범위(PORTS)를 확인하고, 새 파일을 만들어 붙여 넣고 읽습니다.
2. `compose.secure.yaml` 로 적용하고, `web1` · `web2` · `web3` 의 출력과 PORTS 가 서로 다른 것을 읽습니다.
3. `web3` 의 로그 파일을 읽고 `404` 요청을 세어 저장합니다.

**순서**

1. **[터미널]** 도전 5-1에서 켠 서버의 접속 범위를 확인합니다. 이 출력은 보고서 (가)에 붙여 넣습니다.

   ① 서버 상태를 봅니다.

   ```bash
   docker compose ps
   ```

   - 하는 일: 컴포즈로 켠 서버의 상태를 보여 줍니다.
   - 나오는 것: <mark>`web1` · `web2` 가 `Up` 이고, PORTS 가 둘 다 `0.0.0.0:` 으로 시작하면</mark> 됩니다. 켜져 있지 않으면 `docker compose up -d` 를 먼저 칩니다.

   ```
   NAME                       IMAGE        COMMAND                  SERVICE   CREATED                  STATUS                  PORTS
   anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      Less than a second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
   anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      Less than a second ago   Up Less than a second   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp
   ```

2. 새 파일을 만들 준비를 합니다. ①은 **[터미널]**, ②는 **[VS Code]** 에서 합니다.

   ① **[터미널]** 로그를 남길 폴더를 만듭니다.

   ```bash
   mkdir logs
   ```

   - 하는 일: `logs` 폴더를 만듭니다.
   - 나오는 것: 아무것도 나오지 않습니다.

   ② **[VS Code]** 왼쪽 목록에서 `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 파일 이름 `compose.secure.yaml` 을 그대로 적고 Enter 를 칩니다. 내용은 다음 3번에서 붙여 넣으니 지금은 비워 둡니다. 도전 5-1의 `compose.yaml` 은 그대로 둡니다.

3. **[VS Code]** `compose.secure.yaml` 을 열어 아래 내용을 그대로 붙여 넣고 저장합니다. <mark>주석을 읽으면서 도전 5-1 파일과 다른 곳 세 군데를 찾아봅니다.</mark>

<pre class="copyable"><code>services:                      # 켤 서버들을 적는 곳이 여기서 시작된다
  web1:                        # 일반 서버 : 같은 네트워크의 다른 PC 도 접속할 수 있다
    image: nginx:1.28          # 도전 5-1과 같은 프로그램
    ports:                     # 접속 범위를 정하는 곳
      - "8080:80"              # 주소를 적지 않으면 모두에게 열린다 (도전 5-1과 같다)
    restart: unless-stopped    # 서버가 저절로 꺼지면 다시 켠다 (도전 5-1과 같다)
  web2:                        # 관리용 서버 : 내 PC 에서만 접속한다
    image: nginx:1.28          # 도전 5-1과 같은 프로그램
    ports:                     # 접속 범위를 정하는 곳
      - "127.0.0.1:8081:80"    # 맨 앞의 127.0.0.1 은 「내 PC 에서만」이라는 뜻이다 (바뀐 줄)
    restart: unless-stopped    # 서버가 저절로 꺼지면 다시 켠다
  web3:                        # 로그 서버 : 내 PC 에서만 접속하고, 로그를 내 폴더에 남긴다 (새로 추가한 서버)
    image: nginx:1.28          # 같은 nginx 웹 서버
    ports:                     # 접속 범위를 정하는 곳
      - "127.0.0.1:8082:80"    # web2 와 같이 내 PC 에서만 접속한다 (포트는 8082)
    restart: unless-stopped    # 서버가 저절로 꺼지면 다시 켠다
    volumes:                   # 내 폴더와 서버 안 폴더를 연결하는 곳
      - ./logs:/var/log/nginx  # 서버가 로그를 쓰는 폴더를 내 logs 폴더에 연결한다 (왼쪽 내 폴더, 오른쪽 서버 안)
</code></pre>

   - `web1`: 도전 5-1과 같습니다. <mark>바뀌지 않은 서버입니다.</mark>
   - `web2`: 포트 줄 맨 앞에 `127.0.0.1:` 이 붙었습니다. <mark>바뀐 서버입니다.</mark>
   - `web3`: 새로 추가한 서버이고, 로그를 내 폴더에 남기는 `volumes` 줄이 있습니다.
   - <mark style="background:#ffc4d6">`web1` · `web2` · `web3` 의 포트 번호(8080 · 8081 · 8082)를 바꾸지 않습니다.</mark>

4. **[터미널]** 새 파일로 적용합니다. <mark>도전 5-1의 서버를 끄지 않고 바로 칩니다.</mark> 이 출력을 서버마다 읽는 것이 이번 실습 문제의 핵심입니다.

   ① 새 파일로 적용합니다.

   ```bash
   docker compose -f compose.secure.yaml up -d
   ```

   - 하는 일: `-f 파일이름` 은 사용할 컴포즈 파일을 정합니다. 적용하는 방식은 도전 5-1과 같습니다.
   - 나오는 것: <mark>`web1-1 Running`, `web2-1 Recreated`, `web3-1 Created` 세 줄이 보이면</mark> 됩니다. `Creating` · `Starting` 은 준비 과정이니 2.2 의 표로 위 세 줄만 읽습니다.

   ```
    Container anomaly_detection-web1-1 Running
    Container anomaly_detection-web3-1 Creating
    Container anomaly_detection-web2-1 Recreate
    Container anomaly_detection-web3-1 Created
    Container anomaly_detection-web2-1 Recreated
    Container anomaly_detection-web3-1 Starting
    Container anomaly_detection-web2-1 Starting
    Container anomaly_detection-web2-1 Started
    Container anomaly_detection-web3-1 Started
   ```

5. **[터미널]** 접속 범위가 바뀐 것을 확인합니다. 이 출력도 보고서 (가)에 붙여 넣습니다.

   ① 적용 뒤 서버 상태를 봅니다.

   ```bash
   docker compose -f compose.secure.yaml ps
   ```

   - 하는 일: 새 파일의 서버 상태를 보여 줍니다. 앞에서 친 1번의 출력과 PORTS 를 비교합니다.
   - 나오는 것: <mark>`web1` 은 `0.0.0.0:8080` 그대로이고, `web2` · `web3` 은 `127.0.0.1:` 으로 시작하면</mark> 됩니다.

   ```
   NAME                       IMAGE        COMMAND                  SERVICE   CREATED        STATUS                  PORTS
   anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      1 second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
   anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      1 second ago   Up Less than a second   127.0.0.1:8081->80/tcp
   anomaly_detection-web3-1   nginx:1.28   "/docker-entrypoint.…"   web3      1 second ago   Up Less than a second   127.0.0.1:8082->80/tcp
   ```

6. **[터미널]** 내 PC 에서는 세 서버가 모두 열려 있는지 확인합니다. `127.0.0.1` 로 제한한 서버도 **내 PC 에서는** 접속됩니다. 막히는 것은 다른 PC 에서 들어오는 요청입니다.

   ① `web1` 에 요청합니다.

   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
   ```

   - 하는 일: 8080번 서버에 요청을 보내고 결과 번호만 보여 줍니다.
   - 나오는 것: <mark>결과 번호가 `200` 이면</mark> 됩니다.

   ```
   200
   ```

   ② `web2` 에 요청합니다.

   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
   ```

   - 하는 일: 8081번 서버(내 PC 에서만 열린 서버)에 요청합니다.
   - 나오는 것: <mark>결과 번호가 `200` 이면</mark> 됩니다.

   ```
   200
   ```

   ③ `web3` 에 요청합니다.

   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8082
   ```

   - 하는 일: 8082번 서버(내 PC 에서만 열린 서버)에 요청합니다.
   - 나오는 것: <mark>결과 번호가 `200` 이면</mark> 됩니다.

   ```
   200
   ```

7. **[터미널]** 접속 범위와 재생성 확인이 끝난 뒤에 하는 로그 실습입니다. 서버를 지워도 접속 기록 파일이 내 `logs` 폴더에 남는 것을 확인합니다. 6번에서 `web3` 에 보낸 요청 한 건이 `logs/access.log` 첫 줄에 기록되어 있으니, 요청 두 개를 더 보냅니다.

   ① 없는 주소 `/.env` 를 요청합니다.

   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8082/.env
   ```

   - 하는 일: 스캐너가 자주 찾는 설정 파일 주소를 요청합니다.
   - 나오는 것: 결과 번호가 `404` 이면 됩니다.

   ```
   404
   ```

   ② 없는 주소 `/phpmyadmin` 을 요청합니다.

   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8082/phpmyadmin
   ```

   - 하는 일: 스캐너가 자주 찾는 관리 화면 주소를 요청합니다.
   - 나오는 것: 결과 번호가 `404` 이면 됩니다.

   ```
   404
   ```

   ③ 로그 파일을 읽습니다.

   ```bash
   cat logs/access.log
   ```

   - 하는 일: `web3` 이 내 `logs` 폴더에 남긴 접속 기록을 보여 줍니다.
   - 나오는 것: <mark>요청 3줄(`200` 하나, `404` 둘)이 보이면</mark> 됩니다. IP 와 시각은 사람마다 다릅니다.
     - IP 가 내 PC 의 주소가 아니라 `172.18.0.1` 같은 값인 것은, 내 PC 에서 보낸 요청이 도커 안의 네트워크를 거쳐 서버에 들어가기 때문입니다.
     - 시각 뒤의 `+0000` 은 세계 표준시라는 뜻이라서, 우리나라 시각보다 9시간 이르게 적힙니다.

   ```
   172.18.0.1 - - [06/Nov/2026:03:37:43 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/8.7.1" "-"
   172.18.0.1 - - [06/Nov/2026:03:37:43 +0000] "GET /.env HTTP/1.1" 404 153 "-" "curl/8.7.1" "-"
   172.18.0.1 - - [06/Nov/2026:03:37:43 +0000] "GET /phpmyadmin HTTP/1.1" 404 153 "-" "curl/8.7.1" "-"
   ```

   ④ `404` 요청이 몇 개인지 셉니다.

   ```bash
   grep " 404 " logs/access.log | wc -l
   ```

   - 하는 일: `grep` 이 `404` 가 든 줄만 남기고, `|` 가 그 줄들을 `wc -l` 에 넘겨 줄 수를 셉니다. `404` 앞뒤의 공백까지 따옴표 안에 씁니다.
   - 나오는 것: <mark>`2` 가 나오면</mark> 됩니다. 맥북에서는 숫자 앞에 공백이 붙어 `       2` 처럼 보여도 같은 결과입니다.

   ```
   2
   ```

   ⑤ `404` 요청만 파일로 저장합니다.

   ```bash
   grep " 404 " logs/access.log > logs/web_404.log
   ```

   - 하는 일: ④ 와 같은 `grep` 인데 끝에 `> logs/web_404.log` 를 붙였습니다. `>` 는 화면에 나올 내용을 파일에 저장합니다.
   - 나오는 것: 화면에는 아무것도 나오지 않습니다. 내용이 파일로 들어갔기 때문입니다.

8. **[터미널]** 확인이 끝났으므로 세 서버를 모두 종료합니다. 서버를 지워도 `logs` 폴더의 기록이 남는지 봅니다.

   ① 서버를 모두 끄고 지웁니다.

   ```bash
   docker compose -f compose.secure.yaml down
   ```

   - 하는 일: 새 파일의 서버를 모두 끄고 지웁니다.
   - 나오는 것: `Stopped`, `Removed` 줄이 차례로 나옵니다.

   ```
    Container anomaly_detection-web1-1 Stopping
    Container anomaly_detection-web3-1 Stopping
    Container anomaly_detection-web2-1 Stopping
    Container anomaly_detection-web1-1 Stopped
    Container anomaly_detection-web1-1 Removing
    Container anomaly_detection-web1-1 Removed
    Container anomaly_detection-web2-1 Stopped
    Container anomaly_detection-web2-1 Removing
    Container anomaly_detection-web2-1 Removed
    Container anomaly_detection-web3-1 Stopped
    Container anomaly_detection-web3-1 Removing
    Container anomaly_detection-web3-1 Removed
    Network anomaly_detection_default Removing
    Network anomaly_detection_default Removed
   ```

   ② 로그 파일이 남았는지 봅니다.

   ```bash
   ls logs
   ```

   - 하는 일: `logs` 폴더 안의 파일 이름을 보여 줍니다.
   - 나오는 것: <mark>서버를 지웠는데도 `access.log` · `web_404.log` 가 보이면</mark> 됩니다. 이것이 로그를 내 폴더에 연결해 남기는 이유입니다. 함께 보이는 `error.log` 는 nginx 가 오류를 적는 파일이라 저절로 생깁니다.

   ```
   access.log
   error.log
   web_404.log
   ```

9. **[보고서]** `report_u5.md` 의 `## 도전 5-2` 아래를 채웁니다.
   - (가) 1번과 5번의 `docker compose ps` 출력을 붙여 넣고, 접속 범위가 바뀐 기존 서비스와 새로 추가된 서비스를 따로 적어 주세요.
   - (나) [핵심 질문] `"8081:80"` 과 `"127.0.0.1:8081:80"` 은 누가 접속할 수 있는지가 어떻게 다른가요? 관리 화면이나 데이터베이스 서버를 이렇게 설정하는 이유도 적어 주세요.
   - (다) [핵심 질문] `up -d` 의 출력에서 `web1` 은 `Running`, `web2` 는 `Recreated`, `web3` 은 `Created` 였습니다. 서버마다 출력이 다른 이유와, 운영 중인 서비스의 설정을 바꿀 때 이것이 왜 도움이 되는지 적어 주세요.

## 도전 5-2 정리

| 하려는 일 | 명령 · 설정 |
|---|---|
| 서버를 내 PC 에서만 접속하게 | `ports:` 줄 앞에 `127.0.0.1:` → `"127.0.0.1:8081:80"` |
| 다른 컴포즈 파일로 적용 | `docker compose -f compose.secure.yaml up -d` |
| 접속 범위 읽기 | `docker compose -f compose.secure.yaml ps` 의 PORTS |
| 로그를 내 폴더에 연결 | `volumes: - ./logs:/var/log/nginx` |
| 찾고 세기 · 저장 | `grep " 404 " logs/access.log \| wc -l` · `… > logs/web_404.log` |
| 모두 끄고 지우기 | `docker compose -f compose.secure.yaml down` |


---
