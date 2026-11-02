---
id: u4-l22-인터넷-설정-자동화를-위한-dhcp
title: DHCP로 네트워크 설정을 자동으로 받기
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-22.md
additional_sources:
  - https://studio.futurereadycampus.com/course-network/wiki/oeweo-network/lesson-22.html
  - https://www.rfc-editor.org/rfc/rfc2131.html
  - https://www.rfc-editor.org/rfc/rfc2132.html
  - https://www.rfc-editor.org/rfc/rfc3927.html
wiki_diagram: units/04-layer3-addressing/lessons/12-인터넷-설정-자동화를-위한-dhcp/assets/diagrams/lesson-22.svg
page_metadata:
- terms:
  - DHCP(Dynamic Host Configuration Protocol)
  - 네트워크 설정(Network configuration)
  - 클라이언트(Client)
  - 서버(Server)
  illustrations:
  - file: assets/animations/l22-daily-welcome-card.svg
    title: "새 입주자에게 안내 카드를 채워 준다"
    alt: "새 입주자의 호수, 우리 동네 범위, 정문 위치, 안내 전화 칸이 모두 ?로 비어 있습니다. 직접 알아보는 것은 이사할 때마다 번거롭다는 표시가 나오고, 관리사무소가 입주 안내 카드의 값을 보내 칸이 채워집니다. 마지막에 카드를 받아도 길이 열려 있어야 한다고 표시됩니다."
    caption: "관리사무소가 안내 카드를 채워 주듯, 설정은 자동으로 받지만 길이 열려 있어야 합니다."
    after_paragraph: -1
  - file: assets/animations/l22-dhcp-fills-settings.svg
    title: "DHCP가 네트워크 설정을 채워 준다"
    alt: "새 노트북의 IP 주소, 서브넷 마스크, 기본 게이트웨이, DNS 서버 칸이 모두 ?로 비어 있습니다. 직접 입력하면 바꿀 때마다 번거롭다는 표시가 나오고, DHCP 서버가 설정 값을 보내 칸이 채워집니다. 마지막에 설정 전달이 자동일 뿐 회선도 동작해야 인터넷이 된다고 표시됩니다."
    caption: "‘자동’은 인터넷이 저절로 생긴다는 뜻이 아니라 필요한 설정을 받아 온다는 뜻입니다. 그림의 값은 예시예요."
    after_paragraph: 2
- terms:
  - IP 주소(IP address)
  - 서브넷 마스크(Subnet mask)
  - 기본 게이트웨이(Default gateway)
  - DNS 서버(DNS server)
  - DHCP 옵션(DHCP option)
  illustrations:
  - file: assets/animations/l22-daily-four-card-items.svg
    title: "안내 카드 네 가지는 서로 다른 일을 한다"
    alt: "왼쪽에 호수, 동네 경계, 정문, 안내 전화가 목록으로 있고, 오른쪽에 항목마다 장면이 나타납니다. 호수는 우리 집을 구별하고, 동네 경계는 같은 동네를 가르고, 정문은 다른 동네로 나가는 첫 문이며, 안내 전화는 이름을 호수로 알려 줍니다. 마지막에 관리사무소는 카드를 줄 뿐 배달과 안내는 하지 않는다고 표시됩니다."
    caption: "카드의 네 항목은 각자 다른 일을 맡습니다."
    after_paragraph: -1
  - file: assets/animations/l22-four-settings.svg
    title: "DHCP가 알려 주는 네 가지 설정"
    alt: "왼쪽에 IP 주소, 서브넷 마스크, 기본 게이트웨이, DNS 서버가 목록으로 있고, 오른쪽에 항목마다 장면이 나타납니다. IP 주소는 내 인터페이스를 구별하고, 마스크는 같은 네트워크를 가르고, 게이트웨이는 다른 네트워크로 가는 첫 라우터이며, DNS 서버는 이름을 IP 주소로 알려 줍니다. 마지막에 DHCP는 설정을 전달할 뿐 패킷 운반이나 이름 변환은 하지 않는다고 표시됩니다."
    caption: "DHCP는 설정을 전달하고, 운반은 라우팅이, 이름 변환은 DNS가 합니다. 그림의 값은 예시예요."
    after_paragraph: 1
- terms:
  - 주소 풀(Address pool)
  - 임대(Lease)
  - 동적 할당(Dynamic allocation)
  - 예약(Reservation)
  illustrations:
  - file: assets/animations/l22-daily-room-lease.svg
    title: "객실을 빌려 주고 기간을 관리한다"
    alt: "객실 100호부터 200호까지의 방 목록이 있고, 손님 A와 B가 방을 하나씩 숙박 기간만큼 빌립니다. 기간이 끝나기 전에 연장하면 같은 방을 계속 쓰고, 마지막에 직원이 따로 쓰는 방을 손님에게 빌려 주면 충돌한다고 표시됩니다."
    caption: "방을 빌리듯 주소도 기간을 두고 빌리며, 따로 쓰는 방은 빌려 주는 목록에서 뺍니다."
    after_paragraph: -1
  - file: assets/animations/l22-address-pool-lease.svg
    title: "주소 풀에서 주소를 임대한다"
    alt: "주소 풀 192.168.0.100부터 200까지의 칸이 한 줄로 있고, 노트북 A와 B가 주소를 하나씩 임대받으며 임대 기간 막대가 생깁니다. 갱신하면 같은 주소를 계속 쓰고, 마지막에 풀 안의 주소를 장치에 수동으로 설정하면 충돌한다고 표시됩니다."
    caption: "풀의 범위와 값은 구조를 보여 주는 예시이고, 실제 범위는 네트워크마다 다릅니다."
    after_paragraph: 2
- terms:
  - DHCP Discover
  - 브로드캐스트(Broadcast)
  - 브로드캐스트 도메인(Broadcast domain)
  - 0.0.0.0
  - 255.255.255.255
  illustrations:
  - file: assets/animations/l22-daily-shout-in-floor.svg
    title: "처음 온 사람은 모두에게 물어본다"
    alt: "새 입주자는 호수도 안내 데스크 위치도 모릅니다. ‘받는 사람: 모두’로 층 방송을 하면 방송 장치를 거쳐 같은 층의 이웃과 안내 데스크에 모두 들리고, 층 사이 문은 방송을 다른 층으로 넘기지 않습니다."
    caption: "방송은 같은 층 안에서만 퍼집니다."
    after_paragraph: -1
  - file: assets/animations/l22-discover-broadcast.svg
    title: "Discover는 모두에게 방송한다"
    alt: "새 PC는 출발지 IP가 0.0.0.0이고, 목적지 IP 255.255.255.255와 목적지 MAC FF:FF:FF:FF:FF:FF로 Discover를 보냅니다. 스위치가 같은 범위의 PC 2와 DHCP 서버, 라우터 쪽으로 복사해 전달하고, 라우터는 다른 네트워크로 넘기지 않는다고 표시됩니다."
    caption: "IP 브로드캐스트와 MAC 브로드캐스트는 서로 다른 계층의 주소이며 함께 쓰일 수 있습니다. 라우터는 기본적으로 브로드캐스트를 넘기지 않아요."
    after_paragraph: 1
- terms:
  - DORA
  - DHCP Offer
  - DHCP Request
  - DHCP ACK
  - UDP(User Datagram Protocol)
  illustrations:
  - file: assets/animations/l22-daily-hotel-booking.svg
    title: "호텔 방 배정은 네 번 오가요"
    alt: "손님과 프런트 사이에 문의, 제안, 선택, 확인이 차례로 화살표로 나타납니다. 손님이 빈방을 묻고, 프런트가 방을 제안하고, 손님이 그 방을 고르고, 프런트가 배정을 확인합니다."
    caption: "문의, 제안, 선택, 확인이 DORA와 같은 순서입니다."
    after_paragraph: -1
  - file: assets/animations/l22-dora-messages.svg
    title: "DORA 네 메시지로 주소를 확정한다"
    alt: "클라이언트와 DHCP 서버 사이에 Discover, Offer, Request, ACK가 차례로 화살표로 나타납니다. 클라이언트가 서버를 찾고, 서버가 주소를 제안하고, 클라이언트가 그 제안을 선택하고, 서버가 확인하면 임대가 시작됩니다. 마지막에 DHCP의 ACK는 TCP의 ACK와 다른 메시지라고 표시됩니다."
    caption: "Discover와 Offer만으로 주소가 확정되지 않고 Request와 ACK까지 거칩니다. DHCP ACK와 TCP ACK는 이름만 같아요."
    after_paragraph: 1
- terms:
  - DHCP 릴레이(DHCP relay)
  - IP 주소 충돌(IP address conflict)
  - 링크 로컬 주소(Link-local address)
  illustrations:
  - file: assets/animations/l22-daily-branch-receptionist.svg
    title: "지점 접수원이 본사에 전달한다"
    alt: "왼쪽 우리 지점의 새 직원이 외치는 소리가 지점 안에서만 퍼지고 밖으로 넘어가지 않습니다. 접수원이 대신 본사 안내센터로 전달하고, 본사의 답도 접수원이 가져와 새 직원에게 돌려줍니다."
    caption: "접수원이 대신 전달해 주기 때문에 다른 건물의 안내센터를 쓸 수 있습니다."
    after_paragraph: -1
  - file: assets/animations/l22-dhcp-relay.svg
    title: "릴레이가 다른 네트워크 서버에 잇는다"
    alt: "왼쪽 클라이언트 네트워크의 새 PC가 Discover를 브로드캐스트하면 같은 네트워크 안에서만 퍼지고 라우터를 넘지 못합니다. 라우터에 설정된 DHCP 릴레이가 이를 받아 설정된 서버 네트워크의 DHCP 서버로 전달하고, 서버의 응답도 릴레이가 클라이언트 쪽으로 가져옵니다."
    caption: "클라이언트가 직접 먼 서버를 브로드캐스트하는 것이 아니라, 관리자가 설정한 릴레이가 연결합니다."
    after_paragraph: 1
- terms:
  - DHCP 서버 주소(DHCP server address)
  - 임대 기간(Lease time)
  - "`ipconfig /all`"
  - "`ipconfig getpacket`"
  - "`nmcli`"
  illustrations:
  - file: assets/animations/l22-daily-read-guide.svg
    title: "안내서에서 받은 값을 찾아 읽기"
    alt: "안내서 세 장 가운데 쓰는 것을 먼저 고릅니다. 호수, 동네, 정문 항목을 찾고, 배정해 준 곳과 계약 기간을 찾고, 안내 전화 항목까지 차례로 확인합니다. 마지막에 스스로 붙인 임시 번호는 관리사무소가 준 것이 아니라고 표시됩니다."
    caption: "여러 장의 안내서가 있을 때는 지금 쓰는 것부터 찾습니다."
    after_paragraph: -1
  - file: assets/animations/l22-find-dhcp-settings.svg
    title: "내 컴퓨터에서 DHCP 설정 찾기"
    alt: "왼쪽에 Wi-Fi, Ethernet, 가상 어댑터가 있고 오른쪽에 ipconfig /all 출력 예시가 있습니다. 연결된 어댑터를 먼저 고르고, IPv4 주소와 서브넷 마스크와 기본 게이트웨이, 다음으로 DHCP 서버와 임대 시작·만료, 마지막으로 DNS 서버를 차례로 찾습니다. 마지막에 169.254.x.x는 DHCP가 준 주소가 아니라고 표시됩니다."
    caption: "Windows 출력의 예시이고 운영체제마다 명령과 표기가 다릅니다. 그림의 주소 값은 예시예요."
    after_paragraph: 3
- terms:
  - DHCP 자동 구성
  - 브로드캐스트 전달
  - IP 주소 갱신
  illustrations:
  - file: assets/animations/l22-daily-card-vs-road.svg
    title: "안내 카드가 있어도 길이 막히면 안 돼요"
    alt: "안내 카드를 받은 뒤 복도, 정문, 안내 전화, 가게로 이어지는 길이 나타납니다. 복도가 끊기거나 정문이나 안내 전화가 막히면 가게에 갈 수 없다고 표시되고, 마지막에 안내 카드와 문패 확인은 서로 다른 일이라는 두 카드가 나타납니다."
    caption: "카드를 받은 것과 실제로 갈 수 있는 것은 다릅니다."
    after_paragraph: -1
  - file: assets/animations/l22-dhcp-limits.svg
    title: "DHCP가 해결하는 일, 못 하는 일"
    alt: "DHCP 설정을 받은 뒤 Wi-Fi 회선, 기본 게이트웨이, DNS 서버, 웹 사이트로 이어지는 길이 나타납니다. Wi-Fi가 끊기거나 게이트웨이나 DNS가 막히면 웹 사이트가 열리지 않는다고 표시되고, 마지막에 IP 설정은 DHCP가, 같은 LAN에서 MAC을 찾는 일은 ARP가 맡는다는 두 카드가 나타납니다."
    caption: "IP 주소를 받았다는 것과 인터넷 통신이 모두 성공했다는 것은 다릅니다. ARP는 다음 Lesson에서 이어집니다."
    after_paragraph: 1
animations_dir: units/04-layer3-addressing/lessons/12-인터넷-설정-자동화를-위한-dhcp/assets/animations
---

## 네트워크에 연결하면 설정은 어디서 올까?

새 노트북을 집 Wi-Fi에 연결했다고 하자. 인터넷을 쓰려면 노트북에는 IP 주소뿐 아니라 서브넷 마스크, 기본 게이트웨이, DNS 서버 같은 정보도 필요하다. 이 값을 사용자가 매번 직접 입력해야 한다면 기기를 바꾸거나 다른 네트워크로 이동할 때마다 설정을 다시 해야 한다. 네트워크는 어떻게 이 일을 자동으로 해 줄까?

그 역할을 하는 프로토콜이 **DHCP(Dynamic Host Configuration Protocol)**다. DHCP는 클라이언트가 네트워크에 참여할 때 사용할 TCP/IP 설정을 서버에서 받아오게 한다. 이번 Lesson에서는 DHCP가 알려 주는 값, 주소가 임대되는 방식, 서버를 찾는 브로드캐스트, 그리고 실제 컴퓨터에서 받은 값을 확인하는 순서로 살펴본다.

여기서 말하는 ‘자동’은 인터넷 자체가 자동으로 생긴다는 뜻이 아니다. DHCP가 네트워크 통신에 필요한 설정을 알려 주는 것이다. 그 설정이 올바르고 네트워크 회선도 동작해야 인터넷에 연결된다.

## DHCP 서버는 컴퓨터가 쓸 네트워크 설정을 알려 준다

DHCP에는 설정을 받으려는 **클라이언트**와 설정을 제공하는 **서버**가 있다. 클라이언트는 보통 내 컴퓨터의 운영체제 안에서 동작하고, 서버는 필요한 설정 정보를 준비해 두었다가 요청에 답한다. 집에서는 공유기가 DHCP 서버 역할을 함께 맡는 경우가 흔하지만, 서버는 특정한 모양의 장비를 뜻하지 않는다. 다른 네트워크에서는 전용 서버나 중앙 관리 시스템이 담당할 수 있다.

서버가 알려 주는 대표적인 값은 네 가지다. **IP 주소**는 내 네트워크 인터페이스를 식별하고, **서브넷 마스크**는 어느 주소가 같은 네트워크에 있는지 구분하는 데 도움을 준다. **기본 게이트웨이**는 다른 네트워크로 나갈 때 패킷을 맡길 첫 번째 라우터이고, **DNS 서버 주소**는 도메인 이름에 대응하는 IP 주소를 알아볼 때 사용한다. [Unit 5 Lesson 2의 서브넷 경계](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/5/lesson/2/page/1), [Unit 5 Lesson 3의 브로드캐스트 범위](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/5/lesson/3/page/1)와 [Unit 4에서 본 라우터의 전달](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/4/lesson/1/page/7)를 다시 떠올리면, DHCP가 알려 주는 값이 각기 다른 일을 맡는다는 점이 보인다.

DHCP는 IP 설정을 마련해 주는 응용 계층 프로토콜이며 UDP/IP를 이용해 클라이언트와 서버가 메시지를 주고받는다. 즉 DHCP가 직접 패킷을 목적지까지 운반하거나 도메인 이름을 IP 주소로 바꾸는 것은 아니다. DHCP는 그 통신을 시작할 수 있도록 필요한 설정을 전달한다.

## 주소 풀에서 주소를 임대하고 사용 기간을 관리한다

DHCP 서버는 배정할 수 있는 주소들의 목록을 관리한다. 이를 **주소 풀(Address pool)**이라고 한다. 예를 들어 `192.168.0.100`부터 `192.168.0.200`까지를 풀로 정했다면, 서버는 그 범위에서 현재 다른 장치에 빌려 주지 않은 주소를 골라 클라이언트에게 제공한다. 실제 범위는 네트워크마다 다르므로 이 숫자는 구조를 설명하기 위한 예시다.

주소는 보통 영구 소유권을 주기보다 **임대(Lease)**한다. 서버는 “이 주소를 일정 기간 사용할 수 있다”고 허용하고, 클라이언트는 사용 기간이 끝나기 전에 임대를 갱신하려고 한다. 갱신이 성공하면 같은 주소를 계속 쓰는 경우도 많다. 따라서 동적 할당이라고 해서 컴퓨터를 다시 켤 때마다 주소가 반드시 바뀌는 것은 아니다.

주소 풀을 관리하면 DHCP 서버가 자신이 관리하는 임대를 바탕으로 같은 주소를 여러 클라이언트에 중복으로 주지 않게 할 수 있다. 하지만 풀에 포함된 주소를 다른 장치에 수동으로 똑같이 설정하면 충돌이 생길 수 있다. 서버의 풀을 네트워크에서 고정으로 쓰는 주소와 겹치지 않게 구성하는 이유다. 서버에서 특정 기기에 같은 주소를 계속 주도록 설정하는 DHCP 예약도 가능하지만, 그 경우에도 기기는 DHCP를 통해 설정을 받는다.

## Discover 브로드캐스트로 DHCP 서버를 찾는다

네트워크에 처음 연결한 기기는 자기 IP 주소도 DHCP 서버의 주소도 모를 수 있다. 주소를 모르는 서버에게 바로 유니캐스트로 요청할 수 없으므로, 클라이언트는 **DHCP Discover** 메시지를 보낸다. IPv4 주소를 아직 받지 못한 DHCP 클라이언트는 출발지 IP에 `0.0.0.0`을 쓰고, IPv4 제한 브로드캐스트 주소 `255.255.255.255`로 메시지를 보낼 수 있다. 이때 이더넷 프레임의 목적지 MAC 주소도 `FF:FF:FF:FF:FF:FF` 브로드캐스트가 된다.

Unit 3에서 본 액세스 스위치는 이 프레임을 같은 브로드캐스트 범위의 포트들로 전달한다. 여기서 IP 브로드캐스트 주소와 MAC 브로드캐스트 주소는 서로 다른 계층의 주소지만, Discover를 같은 LAN에 전달하는 과정에서 함께 사용될 수 있다. [Unit 5 Lesson 3의 비교표](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/5/lesson/3/page/1)를 떠올리면, IP의 목적지와 프레임의 목적지가 둘 다 브로드캐스트라고 불리는 이유를 구분할 수 있다.

기본적으로 라우터는 이런 브로드캐스트를 다른 네트워크로 그대로 전달하지 않는다. 그래서 DHCP 서버가 같은 브로드캐스트 도메인에 있으면 바로 발견할 수 있지만, 다른 네트워크에 서버가 있다면 릴레이 기능이 필요하다. 다음 페이지에서 그 과정을 보자.

## DORA 네 메시지가 주소를 요청하고 확정한다

새 주소를 받는 대표 흐름은 메시지 이름의 첫 글자를 따 **DORA**라고 부른다. Discover와 Offer만으로 주소가 확정되는 것은 아니다. 클라이언트가 어떤 제안을 사용할지 요청하고, 서버가 최종 확인을 보내는 단계가 이어진다.

| 순서 | 메시지 | 누가 보내나 | 쉽게 풀면 |
|---|---|---|---|
| 1 | Discover | 클라이언트 → 같은 범위의 서버들 | “DHCP 서버가 있나요? 설정을 받고 싶어요.” |
| 2 | Offer | 서버 → 클라이언트 | “이 주소와 설정을 사용할 수 있어요.” |
| 3 | Request | 클라이언트 → 서버 | “이 제안을 선택해 사용할게요.” |
| 4 | ACK | 서버 → 클라이언트 | “요청을 확인했어요. 이 설정으로 임대를 시작하세요.” |

이 흐름을 호텔 방 배정에 빗대면, 손님이 빈방을 문의하고(Discover), 프런트가 방을 제안하고(Offer), 손님이 그 방을 선택하고(Request), 프런트가 배정을 확인하는(ACK) 순서다. 여기서 DHCP ACK는 DHCP 요청에 대한 확인 메시지다. Unit 7에서 배우는 TCP의 ACK와 이름은 같지만, 이 표에서 같은 프로토콜이나 같은 데이터를 확인하는 것은 아니다.

## 다른 네트워크의 서버는 DHCP 릴레이가 연결한다

브로드캐스트는 기본적으로 라우터를 넘어가지 않는다. 따라서 클라이언트와 DHCP 서버가 다른 서브넷에 있다면, 클라이언트의 Discover가 서버까지 저절로 전달되지 않는다. 이때 라우터나 L3 스위치에 **DHCP 릴레이(DHCP relay)**를 설정할 수 있다.

릴레이는 클라이언트가 보낸 브로드캐스트 요청을 받아 설정된 DHCP 서버로 전달하고, 서버의 응답을 다시 클라이언트 네트워크로 가져온다. 클라이언트가 인터넷 너머의 서버를 직접 브로드캐스트로 부르는 것은 아니다. 네트워크 관리자가 릴레이와 서버를 연결해 두었기 때문에 다른 서브넷의 서버를 사용할 수 있는 것이다.

따라서 “DHCP 서버는 반드시 같은 LAN에 있어야 한다”는 말은 릴레이가 없는 단순한 구성에서만 맞다. 작은 집 네트워크에서는 공유기가 같은 LAN의 요청에 응답하는 구성이 흔하고, 큰 조직에서는 여러 네트워크가 중앙 DHCP 서버와 릴레이를 함께 쓸 수 있다. Unit 3의 브로드캐스트 도메인과 Unit 4의 라우터 역할이 여기서 만난다.

## 내 컴퓨터에서 DHCP 설정을 확인한다

직접 받은 설정을 확인하면 DHCP가 무엇을 전달했는지 알 수 있다. 먼저 실제로 연결된 네트워크 어댑터를 찾아야 한다. 컴퓨터에 Wi-Fi, 유선 LAN, 가상 어댑터가 여럿 있으면 각각 다른 주소나 DHCP 설정이 보일 수 있다.

- **Windows:** 명령 프롬프트에서 `ipconfig /all`을 실행한다. 현재 Wi-Fi 또는 Ethernet 어댑터에서 `DHCP 사용`, `IPv4 주소`, `서브넷 마스크`, `기본 게이트웨이`, `DHCP 서버`, `임대 시작/만료`, `DNS 서버`를 찾아본다.
- **macOS:** 터미널에서 `ipconfig getpacket en0`을 실행한다. `en0`이 사용 중인 인터페이스인지 먼저 확인한다. 출력에서 DHCP 서버 식별자, 임대 시간, 서브넷 마스크, 라우터, DNS 서버 값을 살펴본다. 그래픽 화면의 네트워크 설정에서도 IP 주소·서브넷 마스크·라우터를 확인할 수 있다.
- **Linux:** `ip addr show`에서 인터페이스의 주소와 프리픽스를, `ip route`에서 `default via` 뒤의 기본 게이트웨이를 확인한다. NetworkManager를 쓴다면 `nmcli device show`에서 DHCP 옵션과 서버 정보가 표시되는지 볼 수 있다. DNS는 배포판의 네트워크 설정 또는 `resolvectl status`에서 확인할 수 있다.

내 컴퓨터의 주소가 예시와 다르더라도 이상하지 않다. DHCP 서버와 네트워크마다 주소 풀과 게이트웨이가 다르기 때문이다. 반대로 DHCP 서버나 릴레이에 도달하지 못하면 필요한 설정을 받지 못할 수 있다. 일부 운영체제는 이런 때 `169.254.x.x` 링크 로컬 주소를 스스로 설정할 수 있지만, 이는 DHCP 서버가 준 주소가 아니며 보통 같은 링크의 장치끼리만 통신할 때 쓴다. 링크 로컬 주소 하나만 보인다고 인터넷 접속이 되는 것은 아니다.

## DHCP가 해결하는 일과 해결하지 않는 일

DHCP는 컴퓨터가 네트워크에서 통신을 시작할 수 있도록 주소와 몇 가지 설정을 전달한다. 하지만 DHCP가 모든 네트워크 문제를 해결하는 것은 아니다. 예를 들어 DHCP 서버에서 주소를 받았더라도 Wi-Fi 신호가 끊겼거나, 게이트웨이가 동작하지 않거나, DNS 서버에 도달할 수 없다면 웹 사이트가 열리지 않을 수 있다.

또한 DHCP가 알려 주는 IP 주소와 같은 LAN에서 실제 프레임을 보낼 때 필요한 MAC 주소는 서로 다른 정보다. DHCP는 IP 주소와 게이트웨이 같은 설정을 알려 주고, 같은 네트워크 안에서 목적지 IP에 대응하는 MAC 주소를 찾는 일은 ARP가 맡는다. [다음 Lesson의 ARP 설명](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/6/lesson/3/page/1)에서 두 역할을 이어서 살펴보자.

정리하면 DHCP는 네트워크에 참여할 때 필요한 설정을 자동으로 받게 해 주는 출발점이다. 설정을 받은 뒤에는 ARP가 같은 LAN의 다음 전달 대상을 찾고, 라우터와 DNS가 각자의 역할을 수행한다. 이 역할들을 구분하면 “IP 주소를 받았다”와 “인터넷 통신이 모두 성공했다”가 같은 뜻이 아니라는 점을 이해할 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** DHCP는 클라이언트가 IP 주소·서브넷 마스크·기본 게이트웨이·DNS 등의 네트워크 설정을 받게 한다. 임대 주소는 갱신될 수 있어 매번 바뀌는 것은 아니다. 새 주소를 받는 대표 메시지 흐름은 Discover → Offer → Request → ACK다.
- **적용하기 (Apply):** 컴퓨터의 네트워크 정보에서 DHCP 서버와 임대 정보를 찾아보고, Discover가 브로드캐스트되는 이유와 다른 서브넷에서는 릴레이가 필요한 이유를 설명한다.
- **찾아보기 (Lookup):** 정확한 임대 갱신 시점, DHCP 옵션 전체 목록, 주소 풀·예약·릴레이 설정은 네트워크와 운영체제의 관리 화면 또는 DHCP 문서를 확인한다. 다음 Lesson에서는 ARP가 같은 LAN 안에서 목적지 IP에 대응하는 MAC 주소를 알아내는 과정을 살펴본다.
