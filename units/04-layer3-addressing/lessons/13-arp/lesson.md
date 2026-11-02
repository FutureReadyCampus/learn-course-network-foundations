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
  illustrations:
  - file: assets/animations/l23-daily-final-vs-leg.svg
    title: "최종 주소와 이번 구간 인수자"
    alt: "나, 접수창구, 먼 도시의 친구가 한 줄로 있습니다. 최종 주소는 전체 길에, 이번 구간 인수자는 첫 구간에 대응하며 상자에 둘이 함께 필요하다고 표시됩니다. 마지막에 인수자의 이름을 모를 수 있다는 물음표가 나타납니다."
    caption: "택배에는 최종 주소와 이번 구간 인수자가 모두 필요합니다."
    after_paragraph: -1
  - file: assets/animations/l23-ip-network-mac-link.svg
    title: "IP는 네트워크, MAC은 이번 링크"
    alt: "노트북, 공유기, 서버가 한 줄로 있습니다. IP는 전체 길의 목적지 네트워크를, MAC은 첫 링크에서 프레임을 받을 인터페이스를 가리키며 둘 다 필요합니다. 마지막에 IP는 아는데 받을 MAC은 모르는 상태가 물음표로 표시됩니다."
    caption: "IP 주소는 목적지가 있는 네트워크를, MAC 주소는 현재 링크에서 프레임을 받을 인터페이스를 가리킵니다."
    after_paragraph: 0
- terms:
  - L2 정보(Layer 2 information)
  - L3 정보(Layer 3 information)
  illustrations:
  - file: assets/animations/l23-daily-move-keep-name.svg
    title: "이사해도 이름은 그대로예요"
    alt: "옛 동네에서 주소와 이름이 있는 사람이 새 동네로 이사하면 주소는 바뀌지만 이름은 그대로입니다. 택배에는 이번 구간 인수자도 필요한데 그것은 따로 물어서 알아낸다고 표시됩니다."
    caption: "주소는 바뀌어도 이름은 사람에게 붙어 있습니다."
    after_paragraph: -1
  - file: assets/animations/l23-ip-changes-mac-stays.svg
    title: "IP는 바뀌고 MAC은 NIC에 붙어요"
    alt: "집 Wi-Fi 네트워크에서 IP와 MAC을 가진 노트북이 카페 Wi-Fi 네트워크로 옮겨 가면 IP는 바뀌지만 MAC은 같은 NIC의 것으로 그대로입니다. 프레임에는 받는 MAC이 필요한데 아직 물음표이고, 이는 ARP로 찾는다고 표시됩니다."
    caption: "IP 주소는 네트워크 설정이나 이동에 따라 달라지고 MAC 주소는 NIC에 연결된 식별자입니다. 그림의 값은 예시예요."
    after_paragraph: 0
- terms:
  - ARP
  - 게이트웨이(Gateway)
  illustrations:
  - file: assets/animations/l23-daily-ask-desk-owner.svg
    title: "책상 번호는 아는데 이름을 몰라요"
    alt: "나와 21번, 30번, 5번 책상이 있고 30번 책상 담당자의 이름을 모릅니다. 사무실에 30번 책상 담당자가 누구인지 물으면 30번 책상 담당자가 대답하고, 이제 담당자에게 상자를 건넬 수 있습니다."
    caption: "같은 사무실에 물어보면 번호의 주인을 알 수 있습니다."
    after_paragraph: -1
  - file: assets/animations/l23-know-ip-not-mac.svg
    title: "IP는 아는데 MAC을 몰라요"
    alt: "노트북과 같은 LAN의 PC, 프린터, 서버가 있고 프린터의 IP 192.168.0.30은 아는데 MAC은 모릅니다. LAN에 그 IP를 쓰는 장치가 누구인지 묻자 프린터가 자신의 MAC을 알려 주고, 이제 프린터의 MAC으로 프레임을 보낼 수 있습니다."
    caption: "ARP는 같은 LAN에서 알고 있는 IPv4 주소에 대응하는 MAC 주소를 알아냅니다. 그림의 주소와 MAC은 예시예요."
    after_paragraph: 0
- terms:
  - DHCP(Dynamic Host Configuration Protocol)
  illustrations:
  - file: assets/animations/l23-daily-gate-guard-name.svg
    title: "정문 위치는 알아도 경비는 몰라요"
    alt: "입주 안내 카드에 내 호수와 정문 위치는 적혀 있지만 정문 경비의 이름은 없습니다. 밖으로 나가려면 먼저 정문으로 가야 하는데 카드에는 이름이 없어서 따로 알아내야 한다고 표시됩니다."
    caption: "안내 카드에는 위치만 있고 이름은 없어서 따로 알아내야 합니다."
    after_paragraph: -1
  - file: assets/animations/l23-gateway-mac-needed.svg
    title: "게이트웨이 MAC은 따로 알아내요"
    alt: "DHCP로 받은 설정에 내 IP 192.168.0.100과 게이트웨이 IP 192.168.0.1은 있지만 게이트웨이 MAC은 물음표입니다. 인터넷으로 나가려면 먼저 게이트웨이로 보내야 하는데 DHCP는 IP까지만 알려 주므로, MAC은 ARP로 따로 알아내야 한다고 표시됩니다."
    caption: "DHCP는 게이트웨이의 IP 주소는 알려 주지만 그 IP에 대응하는 MAC 주소까지 알려 주지는 않습니다."
    after_paragraph: 0
- terms:
  - 목적지 IP 주소(Destination IP address)
  - 기본 게이트웨이(Default gateway)
  illustrations:
  - file: assets/animations/l23-daily-far-friend-desk.svg
    title: "먼 친구에게는 접수창구에 맡겨요"
    alt: "나, 접수창구, 여러 구간, 먼 도시 친구가 한 줄로 있습니다. 먼저 접수창구에 맡기고, 필요한 인수자는 친구가 아니라 접수창구 담당이며, 그다음은 접수창구가 이어서 보냅니다."
    caption: "내 구간에서 필요한 인수자는 접수창구 담당입니다."
    after_paragraph: -1
  - file: assets/animations/l23-outside-site-gateway.svg
    title: "외부 사이트는 게이트웨이 MAC이 필요"
    alt: "내 PC, 게이트웨이, 여러 구간, 목적지 IP 3.3.3.3인 외부 서버가 한 줄로 있습니다. PC는 먼저 게이트웨이로 프레임을 보내며, 필요한 MAC은 서버가 아니라 게이트웨이의 것이고, 그다음 경로는 게이트웨이가 정합니다."
    caption: "외부 사이트의 IP는 설명용 예시입니다. 같은 구간에서 필요한 MAC은 다음으로 패킷을 받을 게이트웨이의 것이에요."
    after_paragraph: 0
- terms:
  - 브로드캐스트
  illustrations:
  - file: assets/animations/l23-daily-call-out-desk.svg
    title: "책상 번호를 방 전체에 묻는다"
    alt: "나, 층 방송 장치, 1번 책상이 있고 2번·3번 책상이 아래에 있습니다. ‘1번 책상 담당자 누구세요?’를 모두에게 방송하면 같은 층 모두에게 전달되고, 다른 책상은 자기 번호가 아니라 대답하지 않으며, 1번 책상 담당자는 자신을 찾는 줄 압니다."
    caption: "방송은 같은 층에만 들리고, 번호의 주인만 알아챕니다."
    after_paragraph: -1
  - file: assets/animations/l23-arp-request-broadcast.svg
    title: "ARP Request는 모두에게 묻는다"
    alt: "내 PC, 스위치, 게이트웨이가 있고 PC 2와 프린터가 아래에 있습니다. PC가 목적지 MAC FF:FF:FF:FF:FF:FF로 ‘192.168.0.1은 누구?’를 보내면 스위치가 같은 범위로 전달하고, 주인이 아닌 호스트는 응답하지 않으며 게이트웨이는 자신을 찾는 요청임을 알아챕니다."
    caption: "ARP Request는 브로드캐스트로 보내고, 해당 IP의 주인만 응답합니다. 그림의 주소는 예시예요."
    after_paragraph: 0
- terms:
  - ARP 응답(ARP Reply)
  illustrations:
  - file: assets/animations/l23-daily-owner-raises-hand.svg
    title: "담당자만 손들고 대답한다"
    alt: "1번 책상 담당자가 자기 번호임을 알아채고, 손을 들고 번호와 이름을 나에게만 알려 줍니다. 나는 ‘1번 책상 = 김철수’를 알게 되어 이제 상자의 인수자를 정할 수 있습니다."
    caption: "대답은 물어본 나에게만 갑니다."
    after_paragraph: -1
  - file: assets/animations/l23-arp-reply.svg
    title: "ARP Reply로 MAC을 알려 준다"
    alt: "게이트웨이가 자신의 IP를 찾는 요청을 알아채고 ARP Reply로 자신의 IP와 MAC을 PC에게 알려 줍니다. PC는 192.168.0.1의 MAC을 알게 되어 프레임의 받는 MAC을 정할 수 있습니다."
    caption: "ARP Reply는 물어본 PC에게 보내집니다. 그림의 MAC은 48비트 주소의 예시예요."
    after_paragraph: 0
- terms:
  - 패킷(Packet)
  - 프레임(Frame)
  illustrations:
  - file: assets/animations/l23-daily-box-and-truck.svg
    title: "상자 주소와 트럭 인수자는 달라요"
    alt: "송장 붙은 상자에 보내는 곳 서울과 받는 곳 부산이 있고, 상자 겉에 이번 구간 인수자와 봉인이 붙습니다. 최종 도착지와 이번 구간 인수자는 다른 질문이며, 상자는 먼저 접수창구에 맡겨져 이어서 보내집니다."
    caption: "상자의 주소는 끝까지 같고 인수자는 구간마다 달라집니다."
    after_paragraph: -1
  - file: assets/animations/l23-packet-in-frame-pair.svg
    title: "IP 패킷을 프레임에 담는다"
    alt: "출발 IP 192.168.0.100, 목적 IP 3.3.3.3, 데이터로 이뤄진 IP 패킷에 받는 MAC과 출발 MAC, FCS가 붙어 프레임이 됩니다. IP 목적지는 최종적으로 누구에게 보낼지, MAC 목적지는 이번 LAN에서 누구에게 맡길지에 답하며, 프레임은 먼저 게이트웨이로 갑니다."
    caption: "IP 목적지와 프레임의 목적지 MAC은 서로 다른 질문에 답합니다. IP 주소는 설명용 예시예요."
    after_paragraph: 0
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
- terms:
  - ARP 캐시
  illustrations:
  - file: assets/animations/l23-daily-memo-pad.svg
    title: "알아낸 이름을 메모해 둔다"
    alt: "처음에는 번호를 방송해서 물어보고, 알아낸 번호와 이름을 메모장에 한 줄 적습니다. 다음에는 메모를 보고 다시 묻지 않고 바로 건네며, 메모는 오래되면 지워질 수 있습니다."
    caption: "알아낸 대응은 잠깐 적어 두어 매번 다시 묻지 않도록 합니다."
    after_paragraph: -1
  - file: assets/animations/l23-arp-cache.svg
    title: "ARP 캐시에 대응 관계를 남긴다"
    alt: "PC가 게이트웨이에 ARP로 묻고 대답을 받으면 IP 192.168.0.1과 MAC의 한 쌍이 ARP 캐시에 저장됩니다. 다음 통신에서는 다시 묻지 않고 바로 보내며, 캐시는 잠시 저장이라 오래되면 사라질 수 있습니다."
    caption: "ARP 캐시는 알아낸 IP와 MAC의 대응을 잠시 저장합니다. 그림의 주소와 MAC은 예시예요."
    after_paragraph: 0
- terms:
  - arp -a
  - ip neigh
  illustrations:
  - file: assets/animations/l23-daily-read-memo.svg
    title: "메모장에서 이름 쌍을 찾아본다"
    alt: "메모장을 열면 번호와 이름이 한 쌍씩 적혀 있고, 정문 번호가 있는지 살펴봅니다. 아직 적힌 게 없으면 1번 책상에 말을 한 번 걸고 다시 보면 새 메모가 생깁니다."
    caption: "메모가 비어 있으면 한 번 말을 걸어 본 뒤 다시 확인합니다."
    after_paragraph: -1
  - file: assets/animations/l23-arp-a-command.svg
    title: "arp -a로 ARP 캐시 확인하기"
    alt: "왼쪽에 arp -a(Windows·macOS)와 ip neigh(Linux) 명령이 있고 오른쪽에 IP 주소와 MAC 주소가 한 쌍씩 표시된 출력 예시가 있습니다. IP와 MAC의 짝을 보고 게이트웨이 주소가 있는지 찾으며, 항목이 없으면 게이트웨이에 통신을 한 번 시도한 뒤 다시 확인하면 새 기록이 생깁니다."
    caption: "운영체제마다 표시 모양이 다릅니다. 그림의 주소와 MAC은 예시예요."
    after_paragraph: 0
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
