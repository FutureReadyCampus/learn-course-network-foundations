---
id: u4-l23-arp
title: ARP
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-23.md
additional_sources:
  - https://studio.futurereadycampus.com/course-network/wiki/oeweo-network/lesson-23.html
  - https://www.rfc-editor.org/rfc/rfc826.html
wiki_diagram: units/04-layer3-addressing/lessons/13-arp/assets/diagrams/lesson-23.svg
page_metadata:
- terms:
  - IP 주소
  - MAC 주소
  - NIC
- terms:
  - L2 정보(Layer 2 information)
  - L3 정보(Layer 3 information)
- terms:
  - ARP
  - 게이트웨이(Gateway)
- terms:
  - DHCP(Dynamic Host Configuration Protocol)
- terms:
  - 목적지 IP 주소(Destination IP address)
  - 기본 게이트웨이(Default gateway)
- terms:
  - 브로드캐스트
  animations:
  - file: l23-arp-broadcast.svg
    title: ARP 요청은 모두에게, 대답은 주인만
    alt: PC에서 나온 질문 신호가 같은 구간의 장치 세 대로 퍼지고, 192.168.0.1인 게이트웨이만 불이 켜집니다.
    caption: PC가 같은 구간 모두에게 '192.168.0.1 누구?'라고 묻습니다.
- terms:
  - ARP 응답(ARP Reply)
- terms:
  - 패킷(Packet)
  - 프레임(Frame)
  questions:
  - id: u4-l23-p08-q01
    kind: choice
    difficulty: easy
    prompt: "PC가 ARP로 기본 게이트웨이의 MAC 주소를 알아낸 뒤, 외부 서버 3.3.3.3으로 IP 패킷을 보냅니다. 그 IP 패킷을 담은 Ethernet 프레임의 목적지 MAC 주소는 무엇인가요?"
    choices:
    - id: a
      text: "외부 서버 3.3.3.3의 MAC 주소"
      feedback: "인터넷 너머 서버의 MAC 주소를 이 LAN에서 직접 쓰지는 않아요. 현재 구간에서 다음으로 받을 장치의 MAC이 필요해요."
    - id: b
      text: "기본 게이트웨이의 MAC 주소"
      feedback: "맞아요. IP 패킷은 3.3.3.3을 목적지로 유지하고, 현재 LAN의 프레임은 다음 전달자인 게이트웨이의 MAC을 목적지로 사용해요."
    - id: c
      text: "PC 자신의 MAC 주소"
      feedback: "PC 자신의 MAC 주소는 프레임의 출발지에 사용돼요. 목적지에는 현재 구간에서 다음으로 받을 장치의 MAC이 들어가요."
    - id: d
      text: "DNS 서버의 MAC 주소"
      feedback: "DNS는 도메인 이름에 대응하는 IP 주소를 찾는 데 쓰여요. 이 예에서 프레임은 게이트웨이로 전달돼요."
    - id: e
      text: "ARP 요청의 브로드캐스트 MAC 주소"
      feedback: "ARP 요청은 브로드캐스트지만, 여기서 묻는 것은 ARP 응답을 받은 뒤 IP 패킷을 담아 보내는 프레임이에요."
    answer: b
  - id: u4-l23-p08-q02
    kind: choice
    difficulty: easy
    prompt: "PC가 같은 LAN의 게이트웨이 192.168.0.1에 대한 MAC 주소를 모를 때, ARP Request로 무엇을 묻나요?"
    choices:
    - id: a
      text: "외부 서버 3.3.3.3의 MAC 주소가 무엇인지"
      feedback: "ARP는 현재 LAN에서 도달할 수 있는 IP의 MAC 주소를 찾는 데 써요. 외부 서버의 MAC을 이 LAN에서 묻지 않아요."
    - id: b
      text: "192.168.0.1을 사용하는 장치의 MAC 주소가 무엇인지"
      feedback: "맞아요. ARP Request는 같은 LAN에 ‘192.168.0.1을 쓰는 장치는 자신의 MAC 주소를 알려 달라’고 브로드캐스트해요."
    - id: c
      text: "PC의 IP 주소를 어떤 값으로 바꿔야 하는지"
      feedback: "ARP는 IP 설정을 바꾸지 않아요. 이미 알고 있는 IP 주소에 대응하는 MAC 주소를 찾습니다."
    - id: d
      text: "도메인 이름에 어떤 IP 주소가 대응하는지"
      feedback: "그 역할은 DNS예요. ARP는 같은 LAN에서 IP 주소에 대응하는 MAC 주소를 찾습니다."
    - id: e
      text: "인터넷의 모든 장치가 가진 MAC 주소 목록이 무엇인지"
      feedback: "ARP는 전 세계 MAC 목록을 조회하지 않아요. 현재 LAN 안에서 요청한 IP를 사용하는 장치를 찾습니다."
    answer: b
  animations:
  - file: l23-packet-in-frame.svg
    title: IP 패킷을 프레임에 담기
    alt: IP 패킷 상자가 이더넷 프레임이라는 더 큰 상자에 담기고, 바깥 상자의 받는 사람이 게이트웨이로 적힙니다.
    caption: 안쪽 송장은 3.3.3.3, 바깥 송장은 게이트웨이입니다.
- terms:
  - ARP 캐시
- terms:
  - arp -a
  - ip neigh
animations_dir: units/04-layer3-addressing/lessons/13-arp/assets/animations
---

## IP 주소와 MAC 주소 복습

ARP를 이해하려면 먼저 IP 주소와 MAC 주소가 맡는 범위를 떠올리면 된다. [앞에서 본 IP 주소와 MAC 주소의 역할](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/4/lesson/1/page/1)에서처럼 IP 주소는 목적지가 있는 네트워크를 찾고, MAC 주소는 현재 연결된 링크에서 프레임을 받을 인터페이스를 가리킨다. 이번 Lesson은 알고 있는 IP 주소에 대응하는 MAC 주소를 같은 LAN에서 찾는 과정을 다룬다.

## 바뀔 수 있는 주소와 식별자

IP 주소와 MAC 주소는 같은 장치에 설정되어 함께 쓰이지만, 역할과 바뀌는 조건은 다르다. IP 주소는 네트워크 설정이나 이동에 따라 달라질 수 있고, MAC 주소는 네트워크 인터페이스(NIC)에 연결된 식별자다. 실제 프레임을 보낼 때는 IP 주소만으로는 부족하다. 지금 연결된 L2 링크에서 어느 인터페이스에 프레임을 건넬지도 알아야 한다.

## ARP · IP로 MAC을 알아내기
<!-- learn-page-id: arp-definition -->

ARP(Address Resolution Protocol)는 같은 LAN에서 목적지 IPv4 주소에 대응하는 MAC 주소를 알아낼 때 쓰인다. 예를 들어 노트북이 같은 LAN의 프린터 `192.168.0.30`에 인쇄 데이터를 보내려는데 프린터의 MAC 주소를 모른다면, “`192.168.0.30`을 사용하는 장치가 누구인가?”라고 LAN에 물어볼 수 있다. IP는 알지만 프레임의 받는 사람은 모르는 상황을 ARP가 이어 준다.

## Gateway의 MAC이 필요한 이유

이 Ethernet 예에서 인터넷으로 나가려면 게이트웨이의 MAC 주소를 알아야 한다. 게이트웨이를 192.168.0.1, 부팅 후 DHCP로 설정을 받은 PC를 192.168.0.100이라고 하자. PC는 DHCP 설정을 통해 자신의 게이트웨이가 192.168.0.1이라는 사실은 알고 있다. 그러나 이 IP에 대응하는 MAC 주소는 별도로 알아내야 한다.

## 외부 사이트로 접속하는 경로

네이버의 IP 주소를 설명용으로 3.3.3.3이라고 가정한다. 실제 주소라는 뜻은 아니다. 여기서는 목적지 IP를 이미 알고 있다고 가정하며, 도메인 이름에서 IP 주소를 찾는 과정은 뒤의 Unit 9에서 다룬다. 외부 사이트에 접속할 때 PC가 알아야 하는 MAC 주소는 인터넷 너머 서버의 것이 아니라 같은 구간에서 다음으로 패킷을 받을 게이트웨이의 것이다.

## 브로드캐스트로 MAC 질의

PC는 ARP Request를 브로드캐스트로 보내 ‘192.168.0.1을 사용하는 호스트’를 찾는다. 다른 호스트들은 그 주소의 주인이 아니므로 응답하지 않는다. 해당 IP 주소를 사용하는 게이트웨이는 자신을 찾는 요청이라는 사실을 알 수 있다.

## 해당 장치의 응답

게이트웨이는 ARP Reply로 자신의 IP 주소와 MAC 주소를 알려 준다. PC는 192.168.0.1에 대응하는 48비트 MAC 주소를 얻는다. 이제 외부 사이트에 접속하기 위해 만든 IP 패킷을 어떤 L2 목적지로 보낼지 결정할 수 있다.

## IP Packet을 Frame에 담기

IP 패킷의 출발지는 PC인 192.168.0.100, 목적지는 외부 사이트를 가정한 3.3.3.3이다. 이를 담은 Ethernet 프레임의 출발지 MAC은 PC의 NIC 주소, 목적지 MAC은 게이트웨이의 주소다. IP 목적지는 “최종적으로 누구에게 보낼까?”, 프레임의 목적지 MAC은 “이번 LAN에서 누구에게 맡길까?”에 답한다. [Unit 4 Lesson 1의 주소 역할 설명](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/4/lesson/1/page/1)과 이어서 기억하자. 프레임은 먼저 게이트웨이에 전달하고, 게이트웨이가 IP 헤더의 목적지를 보고 다음 경로로 라우팅한다.

## ARP Cache에 남기는 정보

DHCP는 게이트웨이의 IP 주소를 알려 주지만, 그 IP에 대응하는 MAC 주소까지 알려 주지는 않는다. 따라서 PC는 통신이 필요할 때 ARP로 해당 IP의 MAC 주소를 구한다. 이렇게 알아낸 대응 관계는 **ARP 캐시(ARP cache)**에 잠시 저장되어, 다음 통신에서 매번 다시 물어보지 않도록 돕는다.

## arp -a로 확인하기

Windows와 macOS에서는 `arp -a`, Linux에서는 `ip neigh` 명령으로 현재 ARP 캐시를 볼 수 있다. 출력에서 IP 주소와 MAC 주소가 한 쌍으로 표시되는지, 게이트웨이 주소가 있는지 살펴보자. 통신한 지 오래됐거나 아직 해당 장치에 말을 건 적이 없다면 항목이 없을 수 있다. 이때는 게이트웨이에 한 번 통신을 시도한 뒤 다시 확인하면 새 기록이 생기는지 볼 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** ARP는 같은 LAN에서 알고 있는 IPv4 주소에 대응하는 MAC 주소를 찾는다.
- **적용하기 (Apply):** 외부 IP로 보내는 프레임의 목적지 MAC은 보통 현재 LAN의 기본 게이트웨이라는 점을 설명한다.
- **찾아보기 (Lookup):** 내 컴퓨터의 ARP 캐시는 Windows·macOS에서 `arp -a`, Linux에서 `ip neigh`로 확인한다.
