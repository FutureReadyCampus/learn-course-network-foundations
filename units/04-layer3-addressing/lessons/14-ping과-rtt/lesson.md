---
id: u4-l24-ping과-rtt
title: Ping과 RTT
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-24.md
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
  - DoS / DDoS
  - 게이트웨이(Gateway)
- terms:
  - 게이트웨이 주소
- terms: []
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

핵심 개념을 주제별로 정리했다.

## 게임에서 느끼는 지연

온라인 게임에서는 여러 사용자가 같은 공간의 상태를 일관되게 보도록 동기화해야 한다. 철수·영희·길동이 같은 게임에 참여하는데 서로 다른 상태를 본다면 원활한 진행이 어렵다. 게임에서 ‘핑’이라고 부르는 값은 서버와 데이터를 주고받을 때의 지연을 가리킨다. 네트워크에서는 목적지까지 왕복하는 시간(RTT)으로 지연을 측정할 수 있다.

## Ping과 RTT

Ping은 프로그램의 이름이다. ICMP(Internet Control Message Protocol)를 이용해 RTT(Round Trip Time), 즉 왕복 시간을 측정한다. 철수는 서버와 왕복하는 데 20ms, 영희는 25ms, 길동은 50ms가 걸린다고 가정하면 사용자 간에 지연 차이가 있다. 이런 차이는 게임의 화면 동기화에 중요한 문제가 된다.

## 왕복 시간을 비교하기

느린 사용자를 기준으로 맞출지, 다른 방법으로 동기화할지는 게임 구현의 문제다. 여기서의 핵심은 RTT로 통신의 응답 시간을 확인하고, 이를 측정하는 대표적인 도구가 Ping이라는 점이다. 따라서 ‘핑이 이상하다’는 말은 엄밀하게는 왕복 시간이 길어졌거나 응답에 문제가 있다는 상황으로 풀어 이해할 수 있다.

## 네트워크 상태를 확인하는 도구

Ping은 네트워크 상태를 확인하는 청진기 같은 도구다. 다만 불필요한 요청을 대량으로 보내 서버가 정상 서비스를 하지 못하도록 만드는 데 악용할 수도 있다. 이를 DoS·DDoS와 연결해 설명하며, 다른 사용자의 서비스를 방해하는 행위임을 강조한다. 정상적인 진단 예로는 PC 192.168.0.10에서 게이트웨이 192.168.0.1까지 응답을 확인하는 방법이 있다.

## 어느 구간의 문제인지 좁히기

인터넷이 안 될 때 게이트웨이로 Ping을 보내면 가까운 구간의 상태를 먼저 살펴볼 수 있다. 응답이 없다면 PC와 게이트웨이 사이의 연결이나 장비 상태를 조사하는 단서가 된다. 결과에는 밀리초 단위의 RTT가 표시된다. 게이트웨이는 로컬 네트워크에 가까워 1ms 이내에 응답하는 예도 있다. 더 먼 인터넷 서버와 비교하면 어느 범위에서 문제가 나타나는지 좁혀 볼 수 있다.

## 거리와 지연의 관계

서버 A와 B에 각각 Ping을 보내 RTT를 비교할 수 있다. 물리적인 거리뿐 아니라 회선 상태와 전달 속도도 함께 보아야 한다고 설명한다. 예를 들어 PC와 서버 A가 서울에 있고 서버 B가 미국에 있다면, 먼 경로에서 왕복 시간이 길어질 가능성을 생각할 수 있다. 다만 거리만으로 값을 결정할 수는 없으며 실제 경로와 연결 조건을 함께 살펴야 한다.

## ICMP Echo로 응답 확인

Ping은 ICMP Echo Request를 보내고 그에 대한 응답을 확인하는 유틸리티다. 일정 길이의 A, B, C, D 같은 데이터를 보낸 뒤 같은 내용을 되돌려 받는 에코 방식으로 왕복 시간을 측정한다. Ping 자체가 프로토콜인 것은 아니다. 프로그램은 Ping, 여기서 이용하는 프로토콜은 ICMP, 측정하는 값은 RTT라는 구분을 기억하면 된다.
