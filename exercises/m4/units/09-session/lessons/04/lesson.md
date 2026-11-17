---
id: m4-u09-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/112_day05_pm_docker_compose_logs.md
  mission_id: GichanSource.m4-1106-pm-docker-compose-logs
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 개요

설명하는 답은 한 예이고, <mark>핵심이 같으면 맞습니다.</mark>

---

## Exercise 9-1 정답

**터미널에 입력합니다.**

```bash
docker ps --filter publish=8080 --filter publish=8081 --filter publish=8082
docker images nginx:1.28
docker pull nginx:1.28
docker run -d --rm -p 8080:80 --name web-run nginx:1.28
docker ps
docker stop web-run
touch compose.yaml
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

- 복습에서 켠 `web-run` 을 `docker stop web-run` 으로 끄지 않고 `docker compose up -d` 를 치면 <mark>**`web1` 서버가 켜지지 않습니다.**</mark> 같은 8080번 포트를 `web-run` 이 이미 쓰고 있기 때문입니다.
  - 이때 오류는 다음과 같습니다(<mark style="background:#ffc4d6">`port is already allocated`</mark> 가 나오면 이 실수입니다).

    ```
    Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint anomaly_detection-web1-1 (…): Bind for 0.0.0.0:8080 failed: port is already allocated
    ```

  - 고치는 방법: `docker stop web-run` 으로 복습 서버를 끄고, 이미 켜진 `web2` 까지 `docker compose down` 으로 정리한 뒤 `docker compose up -d` 를 다시 칩니다.
- `compose.yaml` 의 들여쓰기에 탭 문자가 들어가면 오류가 납니다. <mark>**VS Code 에서 붙여 넣으면 이 오류는 나지 않지만,**</mark> 탭 문자를 직접 넣었다면 이런 문구가 나옵니다.

    ```
    yaml: while scanning for the next token at line 3: found character that cannot start any token
    ```

  - 줄 번호는 사람마다 다릅니다.
- `docker compose up -d` 를 `compose.yaml` 이 없는 폴더에서 치면 `no configuration file provided: not found` 가 나옵니다. <mark>`pwd` 로 `anomaly_detection` 폴더인지 먼저 봅니다.</mark>

**관제에서는**

- 로그를 모으는 서버나 대응 대상 서버를 여러 대 켜야 할 때 컴포즈 파일 하나로 같은 환경을 다시 만듭니다. <mark>설정 파일을 저장소에 두면 누가 어느 PC 에서 켜도 같은 환경이 됩니다.</mark>

---

## Exercise 9-2 정답

**터미널에 입력합니다.**

```bash
docker compose ps
mkdir logs
touch compose.secure.yaml
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
- (다) `web1` 은 <mark style="background:#bde3ff">설정이 바뀌지 않아서 `Running`</mark>, `web2` 는 <mark style="background:#bde3ff">포트 줄이 바뀌어서 기존 서버를 새 설정으로 다시 만들어 `Recreated`</mark>, `web3` 은 <mark style="background:#bde3ff">새로 추가한 서버라서 `Created`</mark> 였습니다.
  - 도움이 되는 점: 설정을 바꿔도 <mark style="background:#bde3ff">바뀐 서버만 다시 켜지고 나머지는 끊기지 않습니다.</mark> 운영 중인 서비스(`web1`)를 멈추지 않고 보안 설정을 고칠 수 있습니다.

**왜**

- <mark>서버마다 접속 범위를 파일에 적어 두면 설정 실수를 검토하기 쉽고, 같은 `up -d` 로 바뀐 서버만 적용하면 운영 중인 서비스가 끊기지 않습니다.</mark> 볼륨은 서버를 지워도 접속 기록 파일을 내 폴더에 남겨 줍니다.

**자주 틀리는 곳**

- `up -d` 에 `-f compose.secure.yaml` 을 빼고 `docker compose up -d` 만 치면 <mark>**아무것도 바뀌지 않습니다.**</mark> Exercise 9-1의 `compose.yaml` 이 그대로 적용되기 때문입니다.
  - 이때 `ps` 의 PORTS 가 다음처럼 둘 다 `0.0.0.0:` 인 것이 이 실수의 모습입니다. `-f compose.secure.yaml` 을 붙여 다시 칩니다.

    ```
    SERVICE   PORTS
    web1      0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
    web2      0.0.0.0:8081->80/tcp, [::]:8081->80/tcp
    ```

- 8082번 포트를 이미 다른 서버가 쓰고 있으면 `web3` 이 켜지지 않습니다. <mark>시작하기의 포트 확인에서 `8082` 도 비어 있는지 봅니다.</mark>
  - 이때 오류는 다음과 같습니다(<mark style="background:#ffc4d6">`port is already allocated`</mark> 가 나오면 이 실수입니다).

    ```
    Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint anomaly_detection-web3-1 (…): Bind for 0.0.0.0:8082 failed: port is already allocated
    ```

- `web2` 의 포트 줄에서 `127.0.0.1:` 을 빼고 `"8081:80"` 으로 쓰면 <mark>오류는 나지 않지만 다시 모두에게 열립니다.</mark> 보안 설정은 오류가 나지 않아도 PORTS 로 확인해야 합니다.

**관제에서는**

- 서버를 새로 켤 때 「누구에게 열지」를 먼저 정하고, 열어 둔 포트는 `ps` 의 PORTS 로 확인합니다. <mark>외부에 열린 포트를 점검하는 일은 보안 점검의 첫 단계입니다.</mark>

---

## 정답 마무리

- (가) 예: 「`git status` 에 `.env` 와 `.venv` 는 보이지 않았다」. 보였다면 `.gitignore` 맨 아래에 한 줄을 적고 저장한 뒤 `git status` 를 다시 쳐서 사라졌는지 확인했다고 적습니다.
- 깃허브의 `anomaly_detection` 폴더에 Unit 8과 Unit 9의 파일(`compose.yaml` · `logs/web_404.log` 포함)이 보이면 됩니다.
