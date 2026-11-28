---
id: m4-u09-l02
title: 실습 9-1 · 컴포즈로 서버 두 대 한 번에 켜기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/112_day05_pm_docker_compose_logs.md
  mission_id: GichanSource.m4-1106-pm-docker-compose-logs
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 실습 9-1 · 컴포즈로 서버 두 대 한 번에 켜기

## 목표: compose.yaml 로 서버 두 대

> **이번 실습에 들어온 일**
>
> A사 보안 팀장이 보낸 메시지입니다:
> 「Unit 10에서 지금까지 만든 탐지를 한꺼번에 돌려 볼 예정입니다. 쓸 웹 서버 로그가 필요해서 서버를 두 대 켜려고 합니다. 그런데 서버 한 대를 켜는 `docker run` 명령이 옵션이 길어서, 두 대를 켜려면 긴 명령을 두 번 쳐야 하고 한 군데만 틀려도 서버가 다르게 켜집니다.
>
> 서버 설정을 파일 하나에 적어 두고, 명령 한 줄로 두 대를 켤 수 있을까요?」
> - **왜 중요한가**: <mark>설정을 파일로 적어 두면 누가 켜도 같은 서버가 켜지고, 파일을 저장소에 올려 두면 설정 기록도 남습니다.</mark>

## 왜 서버 설정을 파일에 적는가

1. 서버(server, 서버: 요청을 받아 응답을 돌려주는 프로그램)를 켜는 방법을 `docker run` 으로 배웠습니다. 서버 한 대를 켤 때도 옵션을 여러 개 씁니다.
2. 서버가 두 대가 되면 같은 명령을 두 번 쳐야 합니다. <mark>설정을 `compose.yaml` 파일에 적어 두면 `docker compose up -d` 한 줄로 두 대를 한 번에 켭니다.</mark>
3. 이번 실습의 질문은 하나입니다. <mark>**서버 두 대를 명령 한 줄로 켤 수 있는가?**</mark>

## 1.1 docker run 옵션은 compose.yaml 의 어디에 적을까

| `docker run` 에서 | `compose.yaml` 에서 | 뜻 |
|---|---|---|
| `--name web-run` | `web1:` · `web2:` (서비스 이름) | 서버를 구분하는 이름. 컴포즈에서는 서비스(service, 서비스: 컴포즈 파일에 적은 서버 한 대의 설정)라고 부릅니다 |
| `nginx:1.28` | `image: nginx:1.28` | 서버를 켜는 데 쓰는 이미지(image, 이미지: 서버 프로그램과 설정을 묶어 둔 파일) |
| `-p 8080:80` | `ports:` 아래 `- "8080:80"` | 내 컴퓨터의 8080번 포트로 온 요청을 서버의 80번 포트로 보냄 |
| `-d` | `docker compose up -d` 의 `-d` | 백그라운드(background, 백그라운드: 터미널 화면을 차지하지 않고 안에서 계속 실행되는 방식)에서 실행함 |

- `nginx`(엔진엑스)는 웹 서버 프로그램입니다. 서버를 켜면 컨테이너가 하나 생깁니다.
- 컴포즈 파일은 YAML(야믈) 형식으로 씁니다. YAML 은 바로 아래 1.2 에서 설명합니다.

## 1.2 YAML(야믈) 파일이란

1. **정의**: YAML(야믈)은 설정 내용을 사람이 읽기 쉽게 글로 적는 파일 형식입니다. 파일 이름이 `.yaml` 이나 `.yml` 로 끝나고, 이번 Unit에서 쓰는 `compose.yaml` 이 이 형식입니다. 처음 보는 형식이지만 아래 네 가지 모양만 알면 읽을 수 있습니다.

| 모양 | 뜻 | `compose.yaml` 에서 |
|---|---|---|
| `이름: 값` | 이름과 값을 짝으로 적음 (콜론 뒤에 공백 한 칸) | `image: nginx:1.28` |
| 줄 앞의 공백 (들여쓰기) | 그 줄이 어느 이름 아래에 속하는지 나타냄 | `web1:` 아래에 `image:` 와 `ports:` 가 속함 |
| `- 값` | 값이 여러 개일 때 한 줄에 하나씩 적음 | `ports:` 아래의 `- "8080:80"` |
| `#` 뒤의 글 | 사람이 읽는 설명 (실행에는 영향이 없음) | 각 줄 끝의 설명 |

2. **같은 내용을 JSON 과 비교하면**: Unit 8에서 쓴 JSON 파일과 같은 정보를 담지만 모양이 다릅니다. 아래 둘은 같은 내용입니다.

```
JSON : {"services": {"web1": {"image": "nginx:1.28"}}}
```

```
YAML :
services:
  web1:
    image: nginx:1.28
```

3. **장점**
   - <mark>읽기 쉽습니다.</mark> 중괄호(`{ }`)와 따옴표가 거의 없어서 위에서 아래로 읽으면 구조가 보입니다.
   - <mark>설명(주석)을 적을 수 있습니다.</mark> JSON 은 주석을 쓸 수 없지만, YAML 은 `#` 로 「왜 이 값인지」를 파일에 남길 수 있습니다.
   - <mark>여러 도구가 같은 형식을 씁니다.</mark> Docker Compose 외에도 GitHub Actions(깃허브에서 작업을 자동으로 실행하는 설정), Kubernetes(쿠버네티스: 서버 여러 대를 관리하는 도구), Ansible(앤서블: 서버 설정을 자동화하는 도구)의 설정 파일이 YAML 입니다. 이번 실습에서 읽는 방법을 그대로 쓸 수 있습니다.
4. **주의할 점**
   - <mark style="background:#ffc4d6">들여쓰기는 공백으로 합니다. 탭 문자를 넣으면 오류가 납니다.</mark> VS Code 에서 붙여 넣으면 공백으로 들어가서 괜찮습니다.
   - <mark style="background:#ffc4d6">같은 단계의 줄은 공백 수가 같아야 합니다.</mark> 이 파일은 한 단계 안쪽마다 공백 2칸입니다. 공백이 어긋나면 다른 이름 아래에 속하는 것으로 읽혀서 오류가 나거나 다른 뜻이 됩니다.
   - `이름: 값` 에서 콜론 뒤에 공백 한 칸을 씁니다.

## 실습 9-1 · 컴포즈로 서버 두 대 한 번에 켜기

<h2>이런 상황이 있습니다</h2>

- **지금은**: <mark>서버를 켤 때마다 긴 `docker run` 명령을 쳐야 하고, 서버가 늘수록 틀리기 쉽습니다</mark>.
- **그래서 하는 것**:
  - `docker run` 으로 서버 한 대를 켜고 끄는 것을 복습합니다.
  - `compose.yaml` 을 읽고, 서버 두 대를 한 번에 켭니다.
  - 두 서버가 모두 응답하는지 확인합니다.
- **실행하면**: <mark>`docker compose ps` 에 서버 두 개(`web1` · `web2`)가 `Up` 으로 나오고, 8080번과 8081번 모두 결과 번호 `200` 이 나옵니다.</mark>
- **현업에서는**: 서버가 늘수록 설정 파일 하나로 관리하는 방식을 씁니다. 파일에 포트와 이미지 버전이 적혀 있어서 누가 켜도 같은 결과가 나옵니다.

<h2>할 일</h2>

1. 서버 한 대를 `docker run` 으로 켜고 확인한 뒤 끕니다.
2. `compose.yaml` 파일을 만들어 붙여 넣고 읽습니다.
3. `docker compose up -d` 로 서버 두 대를 켜고, 두 서버가 응답하는지 확인합니다.

<h2>순서</h2>

1. **[터미널]** 서버를 켜는 데 쓸 이미지가 내 PC 에 이미 있는지 먼저 확인합니다. <mark>이미 있으면 다시 받지 않아도 됩니다.</mark>

   ① 이미지가 있는지 봅니다.

   ```bash
   docker images nginx:1.28
   ```

   - 하는 일: 내 PC 에 받아 둔 이미지 중 `nginx:1.28` 을 보여 줍니다.
   - 나오는 것: <mark>`nginx:1.28` 이 적힌 줄이 있으면</mark> 이미 받은 것이니 ② 는 건너뛰고 2번으로 갑니다. 머리글 줄만 나오면 아직 없는 것입니다. 도커 버전에 따라 머리글의 글자는 다를 수 있습니다.

   ```
   IMAGE        ID             DISK USAGE   CONTENT SIZE   EXTRA
   nginx:1.28   146adea4768b        258MB         64.1MB   U
   ```

   ② (없을 때만) 이미지를 받습니다.

   ```bash
   docker pull nginx:1.28
   ```

   - 하는 일: `nginx:1.28` 이미지를 인터넷에서 내려받습니다.
   - 나오는 것: 마지막에 `Status: Downloaded newer image` 가 나오면 됩니다.

2. **[터미널]** 복습입니다. 서버 한 대를 켜고, 확인하고, 끕니다. 아래 세 명령을 <mark>하나씩 쳐서</mark> 결과를 봅니다.

   ① 서버를 켭니다.

   ```bash
   docker run -d --rm -p 8080:80 --name web-run nginx:1.28
   ```

   - 하는 일: 서버 한 대를 켭니다. 옵션은 이렇습니다.
     - `-d`: 백그라운드에서 켬 (터미널을 계속 쓸 수 있음)
     - `--rm`: 서버를 끄면 그 서버(컨테이너)를 자동으로 지움
     - `-p 8080:80`: 내 컴퓨터의 8080번 포트를 서버의 80번 포트에 연결
     - `--name web-run`: 서버 이름을 `web-run` 으로 정함
   - 나오는 것: 서버의 고유 번호(긴 글자)가 한 줄 나옵니다.

   ② 켜졌는지 봅니다.

   ```bash
   docker ps
   ```

   - 하는 일: 켜져 있는 서버를 보여 줍니다.
   - 나오는 것: <mark>`web-run` 이 `Up` 으로 보이고, PORTS 에 `0.0.0.0:8080->80/tcp` 가 있으면</mark> 됩니다.

   ```
   CONTAINER ID   IMAGE        COMMAND                  CREATED                  STATUS                  PORTS                                     NAMES
   e1a2ad01c544   nginx:1.28   "/docker-entrypoint.…"   Less than a second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web-run
   ```

   ③ 서버를 끕니다.

   ```bash
   docker stop web-run
   ```

   - 하는 일: `web-run` 서버를 끕니다.
   - 나오는 것: `web-run` 이 한 줄 나옵니다. <mark>이어서 `docker ps` 를 쳤을 때 `web-run` 이 없으면</mark> 정상입니다. `--rm` 때문에 끄면 서버가 지워집니다.

3. **[VS Code]** 왼쪽 목록에서 `anomaly_detection` 폴더를 오른쪽 클릭 › **New File** 을 누르고, 파일 이름 `compose.yaml` 을 그대로 적고 Enter 를 칩니다. 내용은 다음 4번에서 붙여 넣으니 지금은 비워 둡니다.

   이어서 **[터미널]** 에서 파일이 생겼는지 봅니다.

   ```bash
   ls
   ```

   - 하는 일: 폴더 안의 파일 이름을 보여 줍니다.
   - 나오는 것: <mark>`compose.yaml` 이 보이면</mark> 됩니다.

4. **[VS Code]** `compose.yaml` 을 열어 아래 내용을 그대로 붙여 넣고 저장합니다. <mark>각 줄의 `#` 뒤 설명을 읽으면서 붙여 넣습니다.</mark>

   ```yaml
   services:                      # 켤 서버들을 적는 곳이 여기서 시작된다
     web1:                        # 첫 번째 서버의 이름 (명령에서 이 이름으로 부른다)
       image: nginx:1.28          # 사용할 프로그램 : nginx 웹 서버 1.28 버전
       ports:                     # 내 컴퓨터와 서버를 이어 주는 포트를 적는 곳
         - "8080:80"              # 내 컴퓨터의 8080번으로 보낸 요청이 서버의 80번으로 들어간다
       restart: unless-stopped    # 서버가 저절로 꺼지면 다시 켠다 (내가 직접 끈 경우는 그대로 둔다)
     web2:                        # 두 번째 서버의 이름
       image: nginx:1.28          # 같은 nginx 웹 서버를 하나 더 켠다
       ports:                     # 내 컴퓨터와 서버를 이어 주는 포트를 적는 곳
         - "8081:80"              # 두 번째 서버는 8081번으로 받는다 (8080번과 겹치면 안 된다)
       restart: unless-stopped    # 서버가 저절로 꺼지면 다시 켠다
   ```

   - `restart: unless-stopped` 는 서버가 저절로 꺼지면 다시 켜라는 설정입니다. 내가 직접 끈 서버는 다시 켜지 않습니다.
   - <mark style="background:#ffc4d6">`web1` 은 8080번, `web2` 는 8081번입니다. 두 서버가 같은 번호를 쓰면 한쪽이 켜지지 않습니다.</mark>

5. **[터미널]** 서버 두 대를 한 번에 켜고 상태를 봅니다. <mark>컴포즈 파일이 있는 폴더(`anomaly_detection`)에서 칩니다.</mark>

   ① 서버 두 대를 한 번에 켭니다.

   ```bash
   docker compose up -d
   ```

   - 하는 일: 컴포즈 파일의 서버를 모두 백그라운드에서 켭니다.
   - 나오는 것: 서버마다 `Created`, `Started` 줄이 차례로 나옵니다.

   ```
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
   ```

   ② 켜진 상태를 봅니다.

   ```bash
   docker compose ps
   ```

   - 하는 일: 컴포즈로 켠 서버의 상태를 보여 줍니다.
   - 나오는 것: <mark>`web1` 과 `web2` 가 모두 `Up` 이고, PORTS 에 `8080` 과 `8081` 이 보이면</mark> 됩니다. 서버 이름 앞의 `anomaly_detection` 은 컴포즈 파일이 있는 폴더 이름이고, 끝의 `-1` 은 컴포즈가 자동으로 붙이는 번호입니다.

   ```
   NAME                       IMAGE        COMMAND                  SERVICE   CREATED                  STATUS                  PORTS
   anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      Less than a second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
   anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      Less than a second ago   Up Less than a second   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp
   ```

6. **[터미널]** 두 서버가 모두 응답하는지 확인합니다. 명령 끝의 `-s -o /dev/null -w "%{http_code}\n"` 는 HTML 을 화면에 안 보이고 결과 번호만 보여 주는 설정이라 외우지 않아도 됩니다. 결과 번호 `200` 은 요청이 성공했다는 뜻입니다.

   ① 8080번 서버(`web1`)를 확인합니다.

   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
   ```

   - 하는 일: 그 주소에 요청을 보내고 결과 번호만 보여 줍니다.
   - 나오는 것: <mark>결과 번호가 `200` 이면</mark> 됩니다.

   ```
   200
   ```

   ② 8081번 서버(`web2`)를 확인합니다.

   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
   ```

   - 하는 일: 같은 방법으로 두 번째 서버를 확인합니다.
   - 나오는 것: <mark>결과 번호가 `200` 이면</mark> 됩니다.

   ```
   200
   ```


7. **[보고서]** `report_u9.md` 의 `## 실습 9-1` 아래를 채웁니다.
   - (가) 실습 9-1의 서버 켜기 · 확인 명령(`docker images` 부터 `curl` 까지)과 그 결과를 친 순서대로 붙여 넣고, 서비스 이름 두 개와 각 서비스의 포트를 적어 주세요.
   - (나) [핵심 질문] 서버 두 대를 `docker run` 으로 켜는 것과 `compose.yaml` 과 `docker compose up -d` 로 켜는 것을 비교해, 컴포즈가 더 나은 점을 두 가지 적어 주세요.
   - (다) [핵심 질문] 보안 사고가 난 뒤 감사팀이 「사고 당시와 같은 구성으로 서버를 다시 켜 보라」고 요청했습니다. 팀원 한 명은 3주 전에 긴 `docker run` 명령을 직접 쳐서 서버를 켰는데 그 명령을 기억하지 못합니다. 다른 팀은 `compose.yaml` 을 깃허브에 올려 두었습니다. 두 팀이 같은 구성을 다시 켤 수 있는지 비교하고, 파일에 `nginx:1.28` 처럼 버전을 적어 두는 것이 이런 재현에 왜 중요한지 적어 주세요.
   - (라) [핵심 질문] 팀원 세 명이 같은 `compose.yaml` 로 서버를 켰는데 한 명의 PC 에서만 `8081` 번 포트를 다른 프로그램이 쓰고 있어서 `web2` 가 켜지지 않았습니다. 이 사람이 파일의 어느 줄을 어떻게 바꾸면 되는지 적고, 바꿔도 서버 안에서는 여전히 `80` 번 포트로 동작하는 이유를 적어 주세요. 이 사람이 `curl` 로 확인할 때 달라지는 점도 적어 주세요.

## 실습 9-1 정리

| 하려는 일 | 명령 |
|---|---|
| 서버 한 대 켜기 · 확인 · 끄기 | `docker run -d --rm -p 8080:80 --name web-run nginx:1.28` → `docker ps` → `docker stop web-run` |
| 서버 두 대 한 번에 켜기 | `docker compose up -d` |
| 켜진 서버 상태 보기 | `docker compose ps` |
| 응답 확인 | `curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080` |

---
