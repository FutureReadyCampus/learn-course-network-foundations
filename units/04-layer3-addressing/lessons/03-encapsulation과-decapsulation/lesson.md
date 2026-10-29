---
id: "u4-l13-encapsulation과-decapsulation"
title: "Encapsulation과 Decapsulation"
source_wiki: "sources/wiki/oeweo-network/lesson-13.md"
beginner_guide: "sources/wiki/oeweo-network/newbie/specs/lesson-13.json"
wiki_diagram: "sources/wiki/oeweo-network/concepts/lesson-13.svg"
illustrated_pages: [3, 4]
---

핵심 개념을 주제별로 정리했다.

## 택배 포장으로 이해하기

Encapsulation은 어떤 내용을 다른 단위 안에 담는 캡슐화다. 택배를 보낼 물건을 상자 안에 넣고 포장해 하나의 배송 단위로 만드는 것에 비유할 수 있다. 핵심은 내용을 감싸 하나의 단위로 만든다는 점이다.

## Encapsulation · 단위 안에 담기

상자에 책이나 음식을 넣으면 바깥에서는 내용물 대신 상자라는 단위를 보게 된다. 이처럼 캡슐화에는 단위화와 포장의 의미가 있다. 보안 관점의 가림 효과도 언급하지만, 실제로 내용이 보이지 않게 되는 것과 완전히 같은 뜻은 아니라는 제한을 둔다. 러시아 목각 인형인 마트료시카도 좋은 비유다. 인형 안에 더 작은 인형이 들어 있어 바깥에서는 하나로 보이고, 열면 그 안의 다른 단위가 나온다.

## Frame 안의 Packet과 Segment

네트워크에서는 L2 프레임 안에 L3 IP 패킷을 담는다. 이때 IP 패킷 전체가 L2 프레임의 Payload가 된다. 각 계층에서 하나의 단위였던 것이 바깥 계층의 내용물로 들어가는 구조다.

## Decapsulation · 겉에서부터 꺼내기

수신할 때 바깥 헤더를 제거하면 안쪽의 데이터가 나온다. L2 헤더를 제거하면 IP 패킷이 나오고, L3의 Payload 안에는 TCP 헤더와 데이터로 이루어진 L4 세그먼트가 들어 있다. TCP 위의 데이터는 Stream이라는 다른 관점으로 다룬다. L5·L6·L7마다 같은 방식으로 헤더가 하나씩 중첩된다고만 생각하면 전체 동작을 이해하기 어렵다. 이 부분은 뒤에서 종합적으로 설명한다.

## Header와 Payload의 관계 정리

어떤 데이터에 헤더를 붙여 하나의 단위로 만들고, 이를 다시 다른 계층의 Payload로 담는 과정이 Encapsulation이다. 반대로 바깥 헤더를 제거하며 안의 내용을 꺼내는 과정이 Decapsulation이다. 마트료시카처럼 안에 넣고 바깥부터 꺼내는 관계를 먼저 기억하면 된다. 이후 약 30~40분의 종합 설명에서 전체 구조를 다시 연결해 다룬다.
