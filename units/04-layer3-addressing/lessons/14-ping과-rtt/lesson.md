---
id: u4-l24-ping과-rtt
title: Ping과 RTT
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-24.md
additional_sources:
  - https://studio.futurereadycampus.com/course-network/wiki/oeweo-network/lesson-24.html
  - https://www.rfc-editor.org/rfc/rfc792.html
wiki_diagram: units/04-layer3-addressing/lessons/14-ping과-rtt/assets/diagrams/lesson-24.svg
page_metadata:
- terms:
  - 동기화(Synchronization)
  - 서버(Server)
  - 지연(Latency)
- terms:
  - RTT(Round Trip Time)
  - 밀리초(ms)
  - Ping(핑)
  animations:
  - file: l24-ping-round-trip.svg
    title: 세 사람의 왕복 시간
    alt: 철수, 영희, 길동의 컴퓨터에서 각각 서버로 신호 점이 출발해 돌아오는 장면입니다. 철수의 점이 가장 먼저 돌아오고 길동의 점이 가장
      늦게 돌아오며, 마지막에 20, 25, 50ms 막대 길이가 비교됩니다.
    caption: 같은 서버를 다녀오는 데 철수는 20ms, 영희는 25ms, 길동은 50ms가 걸립니다.
- terms:
  - 응답 시간
- terms:
  - Ping 명령(Ping command)
  - 게이트웨이(Gateway)
- terms:
  - 게이트웨이 주소
- terms:
  - 왕복 시간(RTT)
  - 거리(Distance)
  - 지연(Latency)
- terms:
  - 에코(Echo)
  - ICMP(Internet Control Message Protocol)
  animations:
  - file: l24-icmp-echo.svg
    title: 보낸 그대로 돌아오는 에코
    alt: 왼쪽 PC에서 A, B, C, D가 담긴 Echo Request 봉투가 서버로 가고, 서버에서 같은 내용의 Echo Reply 봉투가
      돌아옵니다. 마지막에 Ping은 프로그램, ICMP는 약속, RTT는 값이라는 세 라벨이 나타납니다.
    caption: Ping은 A B C D를 담아 보내고, 같은 내용이 돌아오는 시간을 잽니다.
animations_dir: units/04-layer3-addressing/lessons/14-ping과-rtt/assets/animations
---

## 게임에서 느끼는 지연

온라인 게임에서는 여러 사용자가 같은 공간의 상태를 일관되게 보도록 동기화해야 한다. 철수·영희·길동이 같은 게임에 참여하는데 서로 다른 상태를 본다면 원활한 진행이 어렵다. 게임에서 ‘핑’이라고 부르는 값은 서버와 데이터를 주고받을 때의 지연을 가리킨다. 네트워크에서는 목적지까지 왕복하는 시간(RTT)으로 지연을 측정할 수 있다.

## Ping과 RTT
<!-- learn-page-id: ping-rtt -->

Ping은 프로그램의 이름이다. ICMP(Internet Control Message Protocol)를 이용해 RTT(Round Trip Time), 즉 왕복 시간을 측정한다. ICMP는 IP 통신에서 오류나 상태를 알리는 메시지를 주고받는 프로토콜이다. 앞 Lesson에서 본 TTL 만료 알림도 ICMP이고, Ping은 ICMP의 Echo 요청과 응답을 이용한다. [IPv4 헤더의 Protocol 필드](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/5/lesson/1/page/3)와 연결해 보면 ICMP가 IP 패킷 안에서 어떤 역할을 하는지 떠올릴 수 있다.

철수는 서버와 왕복하는 데 20ms, 영희는 25ms, 길동은 50ms가 걸린다고 가정하면 사용자 간에 지연 차이가 있다. 이런 차이는 게임의 화면 동기화에 중요한 문제가 된다.

## 왕복 시간을 비교하기

느린 사용자를 기준으로 맞출지, 다른 방법으로 동기화할지는 게임 구현의 문제다. 여기서의 핵심은 RTT로 통신의 응답 시간을 확인하고, 이를 측정하는 대표적인 도구가 Ping이라는 점이다. 따라서 ‘핑이 이상하다’는 말은 엄밀하게는 왕복 시간이 길어졌거나 응답에 문제가 있다는 상황으로 풀어 이해할 수 있다.

## 네트워크 상태를 확인하는 도구

Ping은 네트워크 연결을 살펴보는 간단한 진단 도구다. 예를 들어 PC에서 기본 게이트웨이의 IP 주소로 요청을 보내면 내 컴퓨터와 가까운 네트워크 구간을 확인할 수 있다. 진단 목적에 필요한 횟수만 요청하고, 허가받지 않은 서버에 과도하게 요청을 보내지 않는다.

## 어느 구간의 문제인지 좁히기

인터넷이 안 될 때 먼저 실제 네트워크 설정에 표시된 기본 게이트웨이 주소로 Ping을 보낼 수 있다. Windows에서는 `ping -n 4 192.168.0.1`, macOS와 Linux에서는 `ping -c 4 192.168.0.1`처럼 네 번 요청한다. 주소는 내 환경의 게이트웨이 값으로 바꿔야 한다. 응답 줄의 `time`은 왕복 시간(ms), `TTL`은 돌아온 응답 패킷의 남은 전달 한도이며, 마지막 통계의 손실률은 응답하지 않은 요청의 비율이다. Ping 결과의 TTL은 왕복 시간이나 정확한 거리 값이 아니며, 앞 Lesson에서 본 IP TTL과 연결되는 필드다.

게이트웨이는 로컬 네트워크에 가까워 1ms 이내에 응답하는 예도 있다. 더 먼 인터넷 서버와 비교하면 어느 범위에서 문제가 나타나는지 좁혀 볼 수 있다.

## 거리와 지연의 관계

서버 A와 B에 각각 Ping을 보내 RTT를 비교할 수 있다. 물리적인 거리뿐 아니라 회선 상태와 전달 속도도 함께 보아야 한다고 설명한다. 예를 들어 PC와 서버 A가 서울에 있고 서버 B가 미국에 있다면, 먼 경로에서 왕복 시간이 길어질 가능성을 생각할 수 있다. 다만 거리만으로 값을 결정할 수는 없으며 실제 경로와 연결 조건을 함께 살펴야 한다.

## ICMP Echo로 응답 확인
<!-- learn-page-id: icmp-echo -->

Ping은 ICMP Echo Request를 보내고 그에 대한 응답을 확인하는 유틸리티다. 일정 길이의 A, B, C, D 같은 데이터를 보낸 뒤 같은 내용을 되돌려 받는 에코 방식으로 왕복 시간을 측정한다. Ping 자체가 프로토콜인 것은 아니다. 프로그램은 Ping, 여기서 이용하는 프로토콜은 ICMP, 측정하는 값은 RTT라는 구분을 기억하면 된다.

Ping 응답은 ICMP 요청과 응답이 오갈 수 있었고 왕복 시간이 얼마였는지 알려 준다. 응답이 없다고 해서 대상 장치가 반드시 꺼졌다고 단정할 수는 없다. 방화벽이나 장치 설정이 ICMP를 막을 수 있기 때문이다. 반대로 응답이 왔다고 웹 서버 프로그램이 요청을 받았거나 사진의 모든 바이트가 전달됐다는 뜻도 아니다. 다음 Unit 7에서는 프로그램 사이의 통신을 맡는 TCP와 UDP를 알아보고, TCP가 수신 확인과 재전송을 제공하는 이유를 살펴본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Ping은 ICMP Echo 요청과 응답을 이용해 왕복 시간(RTT)을 잰다.
- **적용하기 (Apply):** 게이트웨이와 외부 서버의 응답 시간·손실률을 비교하되, 무응답만으로 장애 위치를 단정하지 않는다.
- **찾아보기 (Lookup):** 운영체제별 명령 옵션과 요약 통계는 필요할 때 터미널에서 확인한다.
