---
id: m4-u09-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/112_day05_pm_docker_compose_logs.md
  mission_id: GichanSource.m4-1106-pm-docker-compose-logs
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 목표: 컴포즈로 웹 서버 로그 만들기

Unit 8에서는 샘플 알림이 맞았는지 세고, 틀린 알림을 줄였습니다. 이번 Unit에서는 Unit 10의 통합 실습에 쓸 **웹 서버 로그**를 직접 만듭니다. 서버를 켜고, 요청을 보내고, 서버가 남긴 기록(로그)에서 스캐너 요청을 찾아 파일로 저장합니다. 서버는 **도커 컴포즈**(Docker Compose: 서버 여러 대의 설정을 파일 하나에 적어 두고 한 번에 켜고 끄는 도구)로 켭니다.

- **실습 9-1**: 서버 한 대를 켜는 `docker run` 을 복습하고, 컴포즈 파일(`compose.yaml`) 하나로 서버 두 대를 한 번에 켭니다.
- **실습 9-2**: 서버를 세 대로 늘리면서 서버마다 누가 접속할 수 있는지를 컴포즈 파일에 정하고(`127.0.0.1:`), 설정을 바꿔도 바뀐 서버만 다시 켜지는 것을 확인합니다. 이어서 서버 로그를 내 폴더에 남기고 `grep` 으로 다룹니다.

Unit 9는 실습 9-1 · 9-2로 이루어져 있고, <mark>깃허브에 올리는 일은 실습 9-2 마지막에 합니다.</mark> 실습마다 문제는 하나입니다.

- 이번 Unit에서 쓰는 도구는 **도커 · 터미널 · VS Code · git** 입니다. <mark>여기서는 파이썬 · 판다스 코드를 쓰지 않고, 터미널 명령만 씁니다.</mark>
- 서버가 쓰는 포트(port, 포트: 컴퓨터로 들어오는 요청을 구분하는 번호)는 `8080` · `8081` · `8082` 로 **고정**합니다. <mark>번호를 바꾸지 않습니다.</mark>
- 보고서에서 `[핵심 질문]` 표시가 붙은 질문은 이 실습에서 꼭 알아야 할 핵심 질문이고, <mark>내 화면의 값을 근거로 이유까지 씁니다</mark>.

> [주의] **먼저 확인 — 이번 Unit에서 만드는 파일은 모두 Module 4 폴더 `anomaly_detection` 안에서 만듭니다.**
> - <mark style="background:#ffc4d6">터미널에서 `pwd` 를 쳐서 결과가 `…/anomaly_detection` 으로 끝나는지 확인한 뒤 시작합니다.</mark> 이전 Module 폴더가 아닙니다.
> - 다른 폴더에서 `docker compose` 를 치면 상위 폴더에 있는 옛 `compose.yaml` 이 켜질 수 있습니다.

**이번 Unit에서 불러 쓰는 이전 파일**: 없습니다. 여기서 만드는 파일은 `compose.yaml` · `compose.secure.yaml` 과 `logs/web_404.log` 입니다.

## Docker Desktop 켜고 폴더 준비하기

> **먼저 Docker Desktop 앱을 켭니다.** 시작 메뉴(맥북은 응용 프로그램)에서 Docker Desktop 을 열고, <mark>화면 구석에 **고래 모양 아이콘**이 보이고 움직임이 멈추면</mark> 준비된 것입니다.

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** `anomaly_detection` 폴더로 들어가 위치를 확인합니다.

   ① 폴더로 들어갑니다.

   ```bash
   cd anomaly_detection
   ```

   - 하는 일: `anomaly_detection` 폴더로 이동합니다.
   - 나오는 것: 아무것도 나오지 않습니다.

   ② 지금 위치를 확인합니다.

   ```bash
   pwd
   ```

   - 하는 일: 지금 있는 폴더의 위치를 보여 줍니다.
   - 나오는 것: <mark>`…/anomaly_detection` 으로 끝나는 글자가 나오면</mark> 됩니다.

3. **[Docker Desktop]** 도커 프로그램(Docker Desktop)이 켜져 있는지 확인합니다.

   ① 켜져 있는 서버를 봅니다.

   ```bash
   docker ps
   ```

   - 하는 일: 지금 켜져 있는 컨테이너(container, 컨테이너: 이미지로 실제로 켜진 서버 하나)를 보여 줍니다.
   - 나오는 것: <mark>`CONTAINER ID` 로 시작하는 머리글 줄이 나오면</mark> 도커가 켜져 있는 것입니다. 다른 서버가 없으면 머리글 줄만 나와도 됩니다. 오류가 나오면 아래 「오류가 나면」 둘째 줄을 따릅니다.

4. **[터미널]** 이번 Unit에서 쓸 포트 `8080` · `8081` · `8082` 번을 이미 켜져 있는 서버가 쓰고 있지 않은지 확인합니다. <mark>쓰고 있으면 내가 켤 서버가 켜지지 않습니다.</mark>

   ① 세 포트를 쓰는 서버가 있는지 봅니다.

   ```bash
   docker ps --filter publish=8080 --filter publish=8081 --filter publish=8082
   ```

   - 하는 일: `--filter publish=포트번호` 는 그 포트를 쓰는 서버만 보여 줍니다.
   - 나오는 것: <mark>`CONTAINER ID` 로 시작하는 머리글 줄만 나오면</mark> 아무도 쓰고 있지 않은 것이니 다음으로 갑니다.

   ```
   CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
   ```

   서버가 한 줄이라도 나오면 그 서버가 포트를 쓰고 있는 것입니다. 줄 맨 끝 `NAMES` 열의 이름을 보고, 다른 수업에서 쓰는 서버일 수 있으니 <mark>내가 켠 서버가 맞는지 확인한 뒤</mark> 아래 명령으로 끕니다.

   ② (서버가 나왔을 때만) 그 서버를 끕니다.

   ```bash
   docker stop 이름
   ```

   - 하는 일: `이름` 자리에 `NAMES` 열의 이름을 넣어 그 서버를 끕니다.
   - 나오는 것: 끈 서버의 이름이 한 줄 나옵니다. 그 뒤 ① 의 명령을 다시 쳐서 머리글 줄만 나오는지 봅니다.


5. **이번 Unit에서 받은 파일 두 개**(Unit 9 안내 파일과 보고서 파일)를 <mark>`다운로드` 폴더에서 `anomaly_detection` 폴더로 끌어다 놓습니다</mark>(안 되면 **File › Save As…**). 이미 있으면 건너뜁니다.
6. **[VS Code]** 보고서 맨 위의 <mark>`이름` 을 내 이름으로 바꿉니다</mark>. 안내 파일은 `Ctrl + Shift + V`(맥북은 `Cmd + Shift + V`)로 미리보기를 엽니다.

## 오류가 나면

- 먼저 `pwd` 가 `anomaly_detection` 으로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `Cannot connect to the Docker daemon` 처럼 도커에 연결할 수 없다는 오류(Windows 에서는 문구가 다를 수 있습니다): <mark>Docker Desktop 이 꺼져 있는 것입니다.</mark> Docker Desktop 을 실행하고, 아래쪽 상태가 초록색(Running)이 될 때까지 1분쯤 기다린 뒤 다시 칩니다.
- `toomanyrequests` 가 나오면 이미지를 너무 많이 받았다는 뜻입니다. <mark>1시간 뒤에 다시 하고,</mark> 그동안은 옆 사람이 아니라 보고서 질문부터 채웁니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). <mark>막히면 맨 아래 「정답」을 보고</mark>, 풀리지 않으면 보고서 (가)에 「모름 — 막힌 곳: …」 이라고 쓰고 넘어갑니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다.

---
