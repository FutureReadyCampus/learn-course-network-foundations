---
id: "u4-l15-계층별-데이터-단위"
title: "계층별 데이터 단위"
source_wiki: "sources/wiki/oeweo-network/lesson-15.md"
beginner_guide: "sources/wiki/oeweo-network/newbie/specs/lesson-15.json"
wiki_diagram: "sources/wiki/oeweo-network/concepts/lesson-15.svg"
illustrated_pages: [4, 5]
---

핵심 개념을 주제별로 정리했다.

## 계층마다 달라지는 데이터 이름

Chrome 같은 브라우저는 소켓 인터페이스를 이용해 데이터를 송수신한다. 이 데이터는 계층을 내려가며 서로 다른 단위로 다뤄진다. L1~L2에서 사용하는 단위는 Frame, IP 수준의 단위는 Packet, TCP 수준의 단위는 Segment다. 계층별 이름을 구별해 기억해야 한다.

## Socket과 Stream

User mode 애플리케이션이 소켓에서 다루는 데이터는 Stream이다. 스트리밍 서비스에서 사용하는 Stream과 같은 단어로, 연속해서 이어지는 데이터를 뜻한다. 운영체제 입장에서는 시작은 있지만 전체 크기나 끝을 미리 확정하기 어려운 데이터다. 어디까지를 하나의 내용으로 볼지는 애플리케이션 수준에서 정한다. 프로세스는 이를 소켓에 write한다. 그러나 인터넷에서 전달하는 패킷에는 MTU라는 최대 크기 제한이 있다.

## MSS와 MTU

TCP에는 MSS(Maximum Segment Size)라는 크기 기준이 있다. 이 단원의 예에서 MTU는 1,500바이트, MSS는 특별한 이유가 없다면 약 1,460바이트다. Stream 전체가 4MB라면 한 세그먼트나 패킷에 담을 수 있는 크기를 넘는다. 따라서 큰 데이터를 작은 단위로 나누어야 한다.

## Stream을 Segment로 나누기

TCP는 연속된 Stream을 MSS에 맞는 단위로 분할한다. 이 과정을 Segmentation이라고 한다. 애플리케이션의 긴 데이터를 인터넷에서 전달 가능한 단위로 바꾸는 단계다.

## Packet과 Frame으로 보내기

분할한 데이터는 헤더를 붙여 MTU에 맞는 패킷으로 전달하고, 더 아래에서는 프레임으로 감싼다. 소켓은 Stream, TCP는 Segment와 MSS, IP는 Packet과 MTU를 연결해 기억하면 된다. 이 단원의 기본 예에서 MTU는 1,500바이트다. L1~L2의 전달 단위는 Frame이다.

## UDP Datagram과 용어 구별

Stream은 정해진 크기의 한 조각이라기보다 연속된 데이터 전체를 가리킨다. 크기가 정해진 전달 단위로 나뉘면 Segment, Packet, Frame이라는 이름을 사용한다. UDP에는 Datagram이라는 단위가 있다. 여기서는 정해진 데이터 덩어리라는 점에서 패킷과 비슷하게 이해하고, UDP를 다룰 때 다시 살펴본다. 실제 설명에서는 세그먼트까지 넓게 ‘패킷’이라고 부르기도 한다. 다만 정확히 구별해야 할 때를 위해 계층별 단위의 차이를 알고 있어야 한다.
