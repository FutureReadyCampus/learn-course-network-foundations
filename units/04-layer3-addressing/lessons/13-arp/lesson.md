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
  questions:
  - id: u6-l03-p01-q01
    kind: choice
    difficulty: easy
    prompt: IP 주소와 MAC 주소의 역할을 바르게 구분한 것은 무엇인가요?
    choices:
    - id: a
      text: IP 주소는 네트워크 목적지를 찾고, MAC 주소는 현재 링크에서 프레임을 받을 인터페이스를 가리킨다
      feedback: IP 주소는 네트워크 목적지를, MAC 주소는 현재 링크의 프레임 수신 인터페이스를 가리킵니다.
    - id: b
      text: IP 주소는 화면을 찾고, MAC 주소는 웹 사이트 이름을 찾는다
      feedback: 두 주소가 각각 네트워크 수준과 현재 링크 수준 중 어디에 쓰이는지 구분하세요.
    - id: c
      text: 두 주소는 항상 같은 값이다
      feedback: 두 주소가 각각 네트워크 수준과 현재 링크 수준 중 어디에 쓰이는지 구분하세요.
    - id: d
      text: MAC 주소는 인터넷 전체의 라우터 경로를 나타낸다
      feedback: 두 주소가 각각 네트워크 수준과 현재 링크 수준 중 어디에 쓰이는지 구분하세요.
    - id: e
      text: IP 주소는 케이블의 종류를 나타낸다
      feedback: 두 주소가 각각 네트워크 수준과 현재 링크 수준 중 어디에 쓰이는지 구분하세요.
    answer: a
  - id: u6-l03-p01-q02
    kind: choice
    difficulty: medium
    prompt: 같은 컴퓨터에서 Wi-Fi를 집에서 카페로 바꾸면 달라질 수 있는 값은 무엇인가요?
    choices:
    - id: a
      text: 컴퓨터가 실행 중인 프로세스의 이름
      feedback: 본문은 이동과 설정에 따라 달라질 수 있는 주소를 설명합니다.
    - id: b
      text: 모든 환경에서 고정된 MAC 역할
      feedback: 본문은 이동과 설정에 따라 달라질 수 있는 주소를 설명합니다.
    - id: c
      text: 네트워크 설정에 따른 IP 주소
      feedback: IP 주소는 네트워크 설정이나 이동에 따라 달라질 수 있습니다.
    - id: d
      text: ARP라는 프로토콜의 이름
      feedback: 본문은 이동과 설정에 따라 달라질 수 있는 주소를 설명합니다.
    - id: e
      text: Ethernet 프레임의 정의
      feedback: 본문은 이동과 설정에 따라 달라질 수 있는 주소를 설명합니다.
    answer: c
  - id: u6-l03-p01-q03
    kind: choice
    difficulty: medium
    prompt: 실제 프레임을 현재 링크로 보내려면 IP 주소 외에 무엇을 알아야 하나요?
    choices:
    - id: a
      text: 웹 페이지의 제목
      feedback: IP만으로는 현재 링크에서 프레임을 누구에게 건넬지 정할 수 없습니다.
    - id: b
      text: 원격 서버의 화면 크기
      feedback: IP만으로는 현재 링크에서 프레임을 누구에게 건넬지 정할 수 없습니다.
    - id: c
      text: DHCP 임대의 남은 초
      feedback: IP만으로는 현재 링크에서 프레임을 누구에게 건넬지 정할 수 없습니다.
    - id: d
      text: 라우터의 운영체제 이름
      feedback: IP만으로는 현재 링크에서 프레임을 누구에게 건넬지 정할 수 없습니다.
    - id: e
      text: 프레임을 받을 인터페이스의 MAC 주소
      feedback: 현재 L2 링크에서 프레임을 받을 인터페이스의 MAC 주소도 필요합니다.
    answer: e
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
  questions:
  - id: u6-l03-p02-q01
    kind: choice
    difficulty: easy
    prompt: ARP가 보완하는 주소 정보는 무엇인가요?
    choices:
    - id: a
      text: 알고 있는 MAC 주소에 대응하는 도메인 이름
      feedback: ARP가 IP 주소를 다른 어떤 주소로 이어 주는지 기억하세요.
    - id: b
      text: DHCP 서버에 대응하는 포트 번호
      feedback: ARP가 IP 주소를 다른 어떤 주소로 이어 주는지 기억하세요.
    - id: c
      text: 알고 있는 IPv4 주소에 대응하는 MAC 주소
      feedback: ARP는 같은 LAN에서 알고 있는 IPv4 주소에 대응하는 MAC 주소를 알아냅니다.
    - id: d
      text: 라우터의 TTL 값에 대응하는 링크 MTU
      feedback: ARP가 IP 주소를 다른 어떤 주소로 이어 주는지 기억하세요.
    - id: e
      text: 프로세스 이름에 대응하는 IP 패킷 크기
      feedback: ARP가 IP 주소를 다른 어떤 주소로 이어 주는지 기억하세요.
    answer: c
  - id: u6-l03-p02-q02
    kind: choice
    difficulty: medium
    prompt: ARP가 주로 동작하는 범위는 어디인가요?
    choices:
    - id: a
      text: 인터넷의 모든 네트워크 전체
      feedback: ARP의 검색 범위를 인터넷 전체로 넓혀 생각하지 마세요.
    - id: b
      text: 모든 Wi-Fi 네트워크를 합친 범위
      feedback: ARP의 검색 범위를 인터넷 전체로 넓혀 생각하지 마세요.
    - id: c
      text: DNS 서버 내부
      feedback: ARP의 검색 범위를 인터넷 전체로 넓혀 생각하지 마세요.
    - id: d
      text: 컴퓨터 안의 한 프로세스만
      feedback: ARP의 검색 범위를 인터넷 전체로 넓혀 생각하지 마세요.
    - id: e
      text: 같은 LAN 안
      feedback: ARP는 같은 LAN에서 IPv4 주소에 대응하는 MAC 주소를 찾습니다.
    answer: e
  - id: u6-l03-p02-q03
    kind: choice
    difficulty: medium
    prompt: 노트북이 같은 LAN의 프린터 IP는 알지만 프린터 MAC은 모를 때 ARP가 하는 일은 무엇인가요?
    choices:
    - id: a
      text: 프린터에 새 IP 주소를 직접 배정한다
      feedback: 주소 설정과 주소 대응 관계 찾기를 구분하세요.
    - id: b
      text: 해당 IP를 쓰는 장치의 MAC 주소를 찾는다
      feedback: ARP는 알고 있는 IP 주소에 대응하는 같은 LAN 장치의 MAC을 찾습니다.
    - id: c
      text: 도메인 이름을 새로 만든다
      feedback: 주소 설정과 주소 대응 관계 찾기를 구분하세요.
    - id: d
      text: 프린터의 문서를 DNS에 저장한다
      feedback: 주소 설정과 주소 대응 관계 찾기를 구분하세요.
    - id: e
      text: 인터넷 경로의 모든 라우터를 조회한다
      feedback: 주소 설정과 주소 대응 관계 찾기를 구분하세요.
    answer: b
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
  questions:
  - id: u6-l03-p03-q01
    kind: choice
    difficulty: easy
    prompt: 이 Lesson에서 ARP의 정식 이름은 무엇인가요?
    choices:
    - id: a
      text: Automatic Router Path
      feedback: 본문에서 ARP를 풀어 쓴 이름과 주소 해석의 역할을 연결하세요.
    - id: b
      text: Address Routing Packet
      feedback: 본문에서 ARP를 풀어 쓴 이름과 주소 해석의 역할을 연결하세요.
    - id: c
      text: Application Reply Process
      feedback: 본문에서 ARP를 풀어 쓴 이름과 주소 해석의 역할을 연결하세요.
    - id: d
      text: Assigned Range Protocol
      feedback: 본문에서 ARP를 풀어 쓴 이름과 주소 해석의 역할을 연결하세요.
    - id: e
      text: Address Resolution Protocol
      feedback: ARP는 Address Resolution Protocol의 약자입니다.
    answer: e
  - id: u6-l03-p03-q02
    kind: choice
    difficulty: medium
    prompt: ARP는 어떤 두 정보를 연결해 주나요?
    choices:
    - id: a
      text: 도메인 이름과 DHCP 임대 기간
      feedback: ARP가 찾아 주는 것은 경로 비용이나 포트가 아니라 주소 대응입니다.
    - id: b
      text: 같은 LAN의 IPv4 주소와 MAC 주소
      feedback: ARP는 같은 LAN에서 IPv4 주소에 대응하는 MAC 주소를 알아냅니다.
    - id: c
      text: TCP 포트와 Ethernet MTU
      feedback: ARP가 찾아 주는 것은 경로 비용이나 포트가 아니라 주소 대응입니다.
    - id: d
      text: 서버 이름과 ICMP 응답 시간
      feedback: ARP가 찾아 주는 것은 경로 비용이나 포트가 아니라 주소 대응입니다.
    - id: e
      text: IP TTL과 라우팅 메트릭
      feedback: ARP가 찾아 주는 것은 경로 비용이나 포트가 아니라 주소 대응입니다.
    answer: b
  - id: u6-l03-p03-q03
    kind: choice
    difficulty: medium
    prompt: ARP가 특히 필요한 이유로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: IP 주소만으로 Ethernet 출발지 MAC이 자동으로 바뀌기 때문
      feedback: IP 패킷의 목적지와 현재 프레임의 수신자를 함께 생각하세요.
    - id: b
      text: ARP가 외부 도메인의 IP를 찾아 주기 때문
      feedback: IP 패킷의 목적지와 현재 프레임의 수신자를 함께 생각하세요.
    - id: c
      text: 모든 패킷을 암호화해야 하기 때문
      feedback: IP 패킷의 목적지와 현재 프레임의 수신자를 함께 생각하세요.
    - id: d
      text: IP 목적지를 알아도 현재 링크에서 프레임을 받을 MAC 주소가 필요하기 때문
      feedback: IP 목적지가 있어도 현재 링크의 프레임 수신 MAC 주소를 알아야 합니다.
    - id: e
      text: DHCP가 게이트웨이 IP를 알려 주지 않기 때문
      feedback: IP 패킷의 목적지와 현재 프레임의 수신자를 함께 생각하세요.
    answer: d
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
  questions:
  - id: u6-l03-p04-q01
    kind: choice
    difficulty: easy
    prompt: PC가 DHCP에서 기본 게이트웨이 IP를 받았더라도 추가로 알아야 할 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: 인터넷 전체 서버의 MAC 주소
      feedback: 게이트웨이의 IP를 안다는 것과 현재 링크의 MAC을 아는 것은 별개입니다.
    - id: b
      text: 그 게이트웨이 IP에 대응하는 MAC 주소
      feedback: DHCP는 게이트웨이 IP를 알려 줄 수 있지만, 대응 MAC은 ARP로 별도 확인합니다.
    - id: c
      text: 웹 서버의 파일 목록
      feedback: 게이트웨이의 IP를 안다는 것과 현재 링크의 MAC을 아는 것은 별개입니다.
    - id: d
      text: DNS 이름의 암호
      feedback: 게이트웨이의 IP를 안다는 것과 현재 링크의 MAC을 아는 것은 별개입니다.
    - id: e
      text: 라우터가 사용하는 모든 포트 번호
      feedback: 게이트웨이의 IP를 안다는 것과 현재 링크의 MAC을 아는 것은 별개입니다.
    answer: b
  - id: u6-l03-p04-q02
    kind: choice
    difficulty: medium
    prompt: 기본 게이트웨이는 어떤 상황에서 다음 전달자가 되나요?
    choices:
    - id: a
      text: 같은 컴퓨터 안에서 파일을 열 때
      feedback: 이 페이지는 같은 네트워크 안의 프린터가 아니라 외부 목적지 상황을 다룹니다.
    - id: b
      text: 도메인 이름을 입력할 때마다 DNS 역할로
      feedback: 이 페이지는 같은 네트워크 안의 프린터가 아니라 외부 목적지 상황을 다룹니다.
    - id: c
      text: MAC 주소를 저장할 때만
      feedback: 이 페이지는 같은 네트워크 안의 프린터가 아니라 외부 목적지 상황을 다룹니다.
    - id: d
      text: 다른 네트워크로 패킷을 보낼 때
      feedback: 다른 네트워크로 나갈 때 패킷은 기본 게이트웨이에 맡겨집니다.
    - id: e
      text: IP 패킷을 TCP 세그먼트로 나눌 때
      feedback: 이 페이지는 같은 네트워크 안의 프린터가 아니라 외부 목적지 상황을 다룹니다.
    answer: d
  - id: u6-l03-p04-q03
    kind: choice
    difficulty: medium
    prompt: DHCP 설정을 받은 PC가 이미 알고 있는 것과 ARP로 별도 확인하는 것을 바르게 짝지은 것은 무엇인가요?
    choices:
    - id: a
      text: 게이트웨이 IP는 DHCP에서 받고, 그 IP에 대응하는 MAC은 ARP로 알아본다
      feedback: DHCP는 게이트웨이 IP를 제공하고 ARP는 그 IP에 대응하는 MAC 주소를 찾습니다.
    - id: b
      text: 게이트웨이 MAC은 DHCP에서 받고, IP는 ARP로 알아본다
      feedback: DHCP와 ARP가 제공하는 값의 종류를 나누어 보세요.
    - id: c
      text: IP와 MAC을 모두 DNS에서 받는다
      feedback: DHCP와 ARP가 제공하는 값의 종류를 나누어 보세요.
    - id: d
      text: IP와 MAC을 모두 TTL에서 계산한다
      feedback: DHCP와 ARP가 제공하는 값의 종류를 나누어 보세요.
    - id: e
      text: 게이트웨이 주소는 필요하지 않다
      feedback: DHCP와 ARP가 제공하는 값의 종류를 나누어 보세요.
    answer: a
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
  questions:
  - id: u6-l03-p05-q01
    kind: choice
    difficulty: easy
    prompt: 외부 사이트의 목적지 IP를 알고 있을 때 현재 LAN 프레임의 목적지 MAC으로 보통 쓰는 것은 무엇인가요?
    choices:
    - id: a
      text: 인터넷 너머 사이트 서버의 MAC
      feedback: 최종 IP 목적지와 현재 구간의 다음 수신자를 구별하세요.
    - id: b
      text: PC 자신의 MAC
      feedback: 최종 IP 목적지와 현재 구간의 다음 수신자를 구별하세요.
    - id: c
      text: DNS 서버의 MAC을 항상
      feedback: 최종 IP 목적지와 현재 구간의 다음 수신자를 구별하세요.
    - id: d
      text: 같은 구간의 기본 게이트웨이 MAC
      feedback: 현재 LAN 프레임은 다음 전달자인 기본 게이트웨이 MAC을 목적지로 사용합니다.
    - id: e
      text: 브로드캐스트 MAC을 항상
      feedback: 최종 IP 목적지와 현재 구간의 다음 수신자를 구별하세요.
    answer: d
  - id: u6-l03-p05-q02
    kind: choice
    difficulty: medium
    prompt: 외부 서버로 보내는 경우 IP 패킷의 목적지와 Ethernet 프레임의 목적지가 어떻게 다른가요?
    choices:
    - id: a
      text: IP 목적지는 외부 서버이고 프레임 목적지 MAC은 현재 구간의 게이트웨이다
      feedback: IP는 최종 외부 목적지를 유지하고, 프레임은 현재 링크에서 받을 게이트웨이를 가리킵니다.
    - id: b
      text: 두 목적지는 항상 같은 주소 값이다
      feedback: 안쪽 IP 패킷과 바깥 Ethernet 프레임의 목적지를 각각 확인하세요.
    - id: c
      text: IP 목적지는 게이트웨이이고 프레임 목적지는 외부 서버 MAC이다
      feedback: 안쪽 IP 패킷과 바깥 Ethernet 프레임의 목적지를 각각 확인하세요.
    - id: d
      text: 둘 다 PC 자신의 주소다
      feedback: 안쪽 IP 패킷과 바깥 Ethernet 프레임의 목적지를 각각 확인하세요.
    - id: e
      text: 프레임에는 목적지 정보가 없다
      feedback: 안쪽 IP 패킷과 바깥 Ethernet 프레임의 목적지를 각각 확인하세요.
    answer: a
  - id: u6-l03-p05-q03
    kind: choice
    difficulty: medium
    prompt: 외부 서버의 MAC 주소를 이더넷 프레임 목적지에 직접 넣지 않는 이유는 무엇인가요?
    choices:
    - id: a
      text: 외부 서버에는 MAC 주소가 없기 때문
      feedback: 이 LAN의 프레임이 도착해야 하는 바로 다음 장치를 생각하세요.
    - id: b
      text: IP 주소가 항상 MAC 주소와 같기 때문
      feedback: 이 LAN의 프레임이 도착해야 하는 바로 다음 장치를 생각하세요.
    - id: c
      text: 현재 LAN에서 다음으로 전달받을 장치가 게이트웨이이기 때문
      feedback: 현재 링크에서 다음으로 받을 장치는 기본 게이트웨이입니다.
    - id: d
      text: DNS가 MAC 주소를 지우기 때문
      feedback: 이 LAN의 프레임이 도착해야 하는 바로 다음 장치를 생각하세요.
    - id: e
      text: 브로드캐스트는 인터넷을 통과하기 때문
      feedback: 이 LAN의 프레임이 도착해야 하는 바로 다음 장치를 생각하세요.
    answer: c
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
  questions:
  - id: u6-l03-p06-q01
    kind: choice
    difficulty: easy
    prompt: ARP Request는 같은 LAN의 장치들에게 보통 어떤 방식으로 보내나요?
    choices:
    - id: a
      text: 브로드캐스트
      feedback: ARP Request는 같은 구간에 브로드캐스트로 보내 IP 주소의 주인을 찾습니다.
    - id: b
      text: 외부 서버에만 유니캐스트
      feedback: 요청을 보내는 순간 목적 MAC을 아직 모르므로 어떤 전달 방식을 쓰는지 떠올리세요.
    - id: c
      text: DNS 쿼리
      feedback: 요청을 보내는 순간 목적 MAC을 아직 모르므로 어떤 전달 방식을 쓰는지 떠올리세요.
    - id: d
      text: DHCP 임대
      feedback: 요청을 보내는 순간 목적 MAC을 아직 모르므로 어떤 전달 방식을 쓰는지 떠올리세요.
    - id: e
      text: 루프백
      feedback: 요청을 보내는 순간 목적 MAC을 아직 모르므로 어떤 전달 방식을 쓰는지 떠올리세요.
    answer: a
  - id: u6-l03-p06-q02
    kind: choice
    difficulty: medium
    prompt: ARP Request가 “192.168.0.1을 사용하는 장치는 누구인가요?”라고 물으면 보통 누가 응답하나요?
    choices:
    - id: a
      text: 같은 LAN의 모든 장치
      feedback: 브로드캐스트를 모두 받더라도 IP 주소의 주인이 누구인지 구분하세요.
    - id: b
      text: 인터넷의 모든 라우터
      feedback: 브로드캐스트를 모두 받더라도 IP 주소의 주인이 누구인지 구분하세요.
    - id: c
      text: 해당 IP 주소를 사용하는 장치
      feedback: 요청한 IP의 주인인 게이트웨이가 ARP Reply로 응답합니다.
    - id: d
      text: DNS 서버만
      feedback: 브로드캐스트를 모두 받더라도 IP 주소의 주인이 누구인지 구분하세요.
    - id: e
      text: 요청을 보낸 PC 자신
      feedback: 브로드캐스트를 모두 받더라도 IP 주소의 주인이 누구인지 구분하세요.
    answer: c
  - id: u6-l03-p06-q03
    kind: choice
    difficulty: medium
    prompt: 다른 장치가 ARP Request를 받고도 응답하지 않는 이유로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 그 장치에는 MAC 주소가 없기 때문
      feedback: 요청의 대상 IP와 응답 장치의 IP가 일치하는지 보세요.
    - id: b
      text: 브로드캐스트는 한 장치만 받기 때문
      feedback: 요청의 대상 IP와 응답 장치의 IP가 일치하는지 보세요.
    - id: c
      text: ARP는 DHCP 서버만 사용할 수 있기 때문
      feedback: 요청의 대상 IP와 응답 장치의 IP가 일치하는지 보세요.
    - id: d
      text: 프레임에는 IP 주소가 없기 때문
      feedback: 요청의 대상 IP와 응답 장치의 IP가 일치하는지 보세요.
    - id: e
      text: 요청에 적힌 IP 주소의 주인이 아니기 때문
      feedback: 그 IP 주소의 주인이 아닌 장치는 자신을 찾는 요청이 아니므로 응답하지 않습니다.
    answer: e
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
  questions:
  - id: u6-l03-p07-q01
    kind: choice
    difficulty: easy
    prompt: 게이트웨이가 ARP Reply로 알려 주는 것은 무엇인가요?
    choices:
    - id: a
      text: 외부 서버의 모든 MAC 주소
      feedback: 응답에는 질의한 IP와 그 장치의 MAC 대응이 담깁니다.
    - id: b
      text: 클라이언트의 DNS 기록
      feedback: 응답에는 질의한 IP와 그 장치의 MAC 대응이 담깁니다.
    - id: c
      text: 자신의 IP 주소와 MAC 주소 대응
      feedback: ARP Reply는 요청한 IP 주소에 대응하는 MAC 주소를 알려 줍니다.
    - id: d
      text: 다음 DHCP 임대 시각
      feedback: 응답에는 질의한 IP와 그 장치의 MAC 대응이 담깁니다.
    - id: e
      text: 인터넷 경로의 RTT
      feedback: 응답에는 질의한 IP와 그 장치의 MAC 대응이 담깁니다.
    answer: c
  - id: u6-l03-p07-q02
    kind: choice
    difficulty: medium
    prompt: PC가 게이트웨이의 ARP 응답을 받은 뒤 할 수 있게 되는 일은 무엇인가요?
    choices:
    - id: a
      text: 외부 서버의 MAC을 직접 알아낸다
      feedback: IP 패킷은 외부 목적지를 유지하고, 프레임은 게이트웨이를 향합니다.
    - id: b
      text: 자신의 IP 주소를 게이트웨이와 같게 만든다
      feedback: IP 패킷은 외부 목적지를 유지하고, 프레임은 게이트웨이를 향합니다.
    - id: c
      text: DNS 이름을 MAC 주소로 바꾼다
      feedback: IP 패킷은 외부 목적지를 유지하고, 프레임은 게이트웨이를 향합니다.
    - id: d
      text: 모든 라우터를 거치지 않고 외부로 보낸다
      feedback: IP 패킷은 외부 목적지를 유지하고, 프레임은 게이트웨이를 향합니다.
    - id: e
      text: 현재 LAN 프레임의 목적지 MAC을 정해 외부 목적지 IP 패킷을 보낸다
      feedback: 게이트웨이 MAC을 알면 외부 목적지 IP 패킷을 실은 프레임을 게이트웨이에 보낼 수 있습니다.
    answer: e
  - id: u6-l03-p07-q03
    kind: choice
    difficulty: medium
    prompt: ARP Reply를 받아도 외부 서버와의 전체 통신이 끝난 것은 아닌 이유는 무엇인가요?
    choices:
    - id: a
      text: ARP Reply가 웹 페이지를 전송하기 때문
      feedback: 주소를 알아낸 단계와 최종 서비스 응답을 구분하세요.
    - id: b
      text: 응답은 현재 링크에서 게이트웨이의 MAC을 확인한 것이기 때문
      feedback: ARP는 현재 LAN에서 다음 전달자의 MAC을 찾는 단계일 뿐입니다.
    - id: c
      text: 게이트웨이가 외부 서버의 MAC을 대신 소유하기 때문
      feedback: 주소를 알아낸 단계와 최종 서비스 응답을 구분하세요.
    - id: d
      text: ARP가 TCP 연결을 만들기 때문
      feedback: 주소를 알아낸 단계와 최종 서비스 응답을 구분하세요.
    - id: e
      text: ARP 응답은 IP 패킷을 재조립하기 때문
      feedback: 주소를 알아낸 단계와 최종 서비스 응답을 구분하세요.
    answer: b
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
  - id: u6-l03-p08-q03
    kind: choice
    difficulty: medium
    prompt: ARP 캐시에 어떤 IP-MAC 항목이 보이지 않을 수 있는 상황은 무엇인가요?
    choices:
    - id: a
      text: 컴퓨터에 네트워크 인터페이스가 있는 경우
      feedback: 캐시에 없다고 해서 반드시 네트워크 오류라고 단정하지 마세요.
    - id: b
      text: IP 주소를 알고 있는 경우
      feedback: 캐시에 없다고 해서 반드시 네트워크 오류라고 단정하지 마세요.
    - id: c
      text: DNS 서버가 있는 경우
      feedback: 캐시에 없다고 해서 반드시 네트워크 오류라고 단정하지 마세요.
    - id: d
      text: 아직 해당 장치와 통신한 적이 없는 경우
      feedback: 통신한 지 오래됐거나 해당 장치에 말을 건 적이 없으면 항목이 없을 수 있습니다.
    - id: e
      text: 기본 게이트웨이를 설정한 경우
      feedback: 캐시에 없다고 해서 반드시 네트워크 오류라고 단정하지 마세요.
    answer: d
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
  questions:
  - id: u6-l03-p09-q01
    kind: choice
    difficulty: easy
    prompt: Windows와 macOS에서 ARP 캐시를 확인하는 명령은 무엇인가요?
    choices:
    - id: a
      text: ipconfig /all
      feedback: OS별 명령 중 ARP 항목을 표시하는 명령을 고르세요.
    - id: b
      text: arp -a
      feedback: Windows와 macOS에서는 arp -a로 ARP 캐시를 볼 수 있습니다.
    - id: c
      text: ping -c 4 127.0.0.1
      feedback: OS별 명령 중 ARP 항목을 표시하는 명령을 고르세요.
    - id: d
      text: route print
      feedback: OS별 명령 중 ARP 항목을 표시하는 명령을 고르세요.
    - id: e
      text: nslookup
      feedback: OS별 명령 중 ARP 항목을 표시하는 명령을 고르세요.
    answer: b
  - id: u6-l03-p09-q02
    kind: choice
    difficulty: medium
    prompt: Linux에서 이웃 장치의 IP와 링크 주소 정보를 확인할 때 안내된 명령은 무엇인가요?
    choices:
    - id: a
      text: arp -d
      feedback: 이 페이지의 Linux 명령은 경로 보기보다 이웃 정보 확인에 쓰입니다.
    - id: b
      text: ip route add
      feedback: 이 페이지의 Linux 명령은 경로 보기보다 이웃 정보 확인에 쓰입니다.
    - id: c
      text: ping -n 4
      feedback: 이 페이지의 Linux 명령은 경로 보기보다 이웃 정보 확인에 쓰입니다.
    - id: d
      text: ip neigh
      feedback: Linux에서는 ip neigh로 ARP 캐시와 유사한 이웃 정보를 확인할 수 있습니다.
    - id: e
      text: dhclient -r
      feedback: 이 페이지의 Linux 명령은 경로 보기보다 이웃 정보 확인에 쓰입니다.
    answer: d
  - id: u6-l03-p09-q03
    kind: choice
    difficulty: medium
    prompt: arp -a 결과에 게이트웨이 항목이 없을 때 시도할 수 있는 방법은 무엇인가요?
    choices:
    - id: a
      text: 게이트웨이와 한 번 통신한 뒤 다시 캐시를 확인한다
      feedback: 게이트웨이에 통신을 시도한 뒤 새 기록이 생기는지 확인할 수 있습니다.
    - id: b
      text: 컴퓨터를 반드시 다시 설치한다
      feedback: 아직 통신하지 않아 캐시에 없을 가능성을 먼저 고려하세요.
    - id: c
      text: 게이트웨이 MAC을 임의로 입력한다
      feedback: 아직 통신하지 않아 캐시에 없을 가능성을 먼저 고려하세요.
    - id: d
      text: DNS 서버를 삭제한다
      feedback: 아직 통신하지 않아 캐시에 없을 가능성을 먼저 고려하세요.
    - id: e
      text: TTL을 0으로 만든다
      feedback: 아직 통신하지 않아 캐시에 없을 가능성을 먼저 고려하세요.
    answer: a
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
  questions:
  - id: u6-l03-p10-q01
    kind: choice
    difficulty: easy
    prompt: Windows와 macOS에서 ARP 캐시를 확인하는 명령은 무엇인가요?
    choices:
    - id: a
      text: ipconfig /all
      feedback: ARP 항목을 표시하는 명령과 IP 설정을 표시하는 명령을 구분하세요.
    - id: b
      text: ping -c 4 127.0.0.1
      feedback: ARP 항목을 표시하는 명령과 IP 설정을 표시하는 명령을 구분하세요.
    - id: c
      text: route print
      feedback: ARP 항목을 표시하는 명령과 IP 설정을 표시하는 명령을 구분하세요.
    - id: d
      text: arp -a
      feedback: Windows와 macOS에서는 arp -a로 ARP 캐시를 볼 수 있습니다.
    - id: e
      text: nslookup
      feedback: ARP 항목을 표시하는 명령과 IP 설정을 표시하는 명령을 구분하세요.
    answer: d
  - id: u6-l03-p10-q02
    kind: choice
    difficulty: medium
    prompt: ARP 캐시에서 한 IP 주소와 MAC 주소가 한 쌍으로 보인다는 것은 무엇을 나타내나요?
    choices:
    - id: a
      text: 그 IP 주소에 대응하는 링크 주소가 기록되어 있다
      feedback: ARP 캐시는 IP 주소와 MAC 주소의 대응 관계를 기록합니다.
    - id: b
      text: 그 IP 주소가 모든 인터넷 장치에 속한다
      feedback: 캐시에 저장되는 정보가 주소 대응인지 설정 임대인지 확인하세요.
    - id: c
      text: 해당 MAC 주소가 DNS 서버라는 뜻이다
      feedback: 캐시에 저장되는 정보가 주소 대응인지 설정 임대인지 확인하세요.
    - id: d
      text: DHCP 임대가 영구적으로 고정됐다는 뜻이다
      feedback: 캐시에 저장되는 정보가 주소 대응인지 설정 임대인지 확인하세요.
    - id: e
      text: 라우터가 프레임을 재조립했다는 뜻이다
      feedback: 캐시에 저장되는 정보가 주소 대응인지 설정 임대인지 확인하세요.
    answer: a
  - id: u6-l03-p10-q03
    kind: choice
    difficulty: medium
    prompt: 통신한 적이 없는 장치가 ARP 캐시에 없을 때 적절한 설명은 무엇인가요?
    choices:
    - id: a
      text: 그 장치는 반드시 꺼져 있다
      feedback: 캐시에 없는 상황만으로 장치 상태를 단정하지 마세요.
    - id: b
      text: 컴퓨터에 ARP가 설치되지 않았다
      feedback: 캐시에 없는 상황만으로 장치 상태를 단정하지 마세요.
    - id: c
      text: 아직 그 장치에 말을 건 적이 없어 항목이 없을 수 있다
      feedback: 통신한 지 오래됐거나 아직 말을 건 적이 없다면 ARP 캐시 항목이 없을 수 있습니다.
    - id: d
      text: 게이트웨이를 삭제해야 한다
      feedback: 캐시에 없는 상황만으로 장치 상태를 단정하지 마세요.
    - id: e
      text: IP 주소가 MAC 주소와 같아졌다는 뜻이다
      feedback: 캐시에 없는 상황만으로 장치 상태를 단정하지 마세요.
    answer: c
  question_placements:
  - question_id: u6-l03-p10-q01
    after_paragraph: 1
animations_dir: units/04-layer3-addressing/lessons/13-arp/assets/animations
---

## IP 주소와 MAC 주소 복습

ARP를 이해하려면 먼저 IP 주소와 MAC 주소가 맡는 범위를 떠올리면 된다. [앞에서 본 IP 주소와 MAC 주소의 역할](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/4/lesson/1/page/1)에서처럼 IP 주소는 목적지가 있는 네트워크를 찾고, MAC 주소는 현재 연결된 링크에서 프레임을 받을 인터페이스를 가리킨다. 이번 Lesson은 알고 있는 IP 주소에 대응하는 MAC 주소를 같은 LAN에서 찾는 과정을 다룬다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** IP는 네트워크 간 목적지를, MAC은 같은 링크에서 프레임 수신자를 찾는다.
- **적용하기 (Apply):** 원격 서버에 보낼 IP Packet과 게이트웨이에 보낼 Frame 주소를 분리한다.
- **찾아보기 (Lookup):** MAC/IP 주소 역할은 주소·ARP Page를 다시 참조한다.

## 바뀔 수 있는 주소와 식별자

IP 주소와 MAC 주소는 같은 장치에 설정되어 함께 쓰이지만, 역할과 바뀌는 조건은 다르다. IP 주소는 네트워크 설정이나 이동에 따라 달라질 수 있고, MAC 주소는 네트워크 인터페이스(NIC)에 연결된 식별자다. 실제 프레임을 보낼 때는 IP 주소만으로는 부족하다. 지금 연결된 L2 링크에서 어느 인터페이스에 프레임을 건넬지도 알아야 한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** IP 주소는 설정에 따라 바뀔 수 있고 MAC은 인터페이스 식별에 쓰인다.
- **적용하기 (Apply):** 노트북이 다른 Wi-Fi로 이동해도 같은 NIC와 다른 IP를 가질 수 있음을 설명한다.
- **찾아보기 (Lookup):** MAC randomization과 DHCP lease의 실제 설정은 기기에서 확인한다.

## ARP · IP로 MAC을 알아내기
<!-- learn-page-id: arp-definition -->

ARP(Address Resolution Protocol)는 같은 LAN에서 목적지 IPv4 주소에 대응하는 MAC 주소를 알아낼 때 쓰인다. 예를 들어 노트북이 같은 LAN의 프린터 `192.168.0.30`에 인쇄 데이터를 보내려는데 프린터의 MAC 주소를 모른다면, “`192.168.0.30`을 사용하는 장치가 누구인가?”라고 LAN에 물어볼 수 있다. IP는 알지만 프레임의 받는 사람은 모르는 상황을 ARP가 이어 준다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** ARP는 같은 LAN에서 목표 IPv4 주소에 대응하는 MAC을 알아낸다.
- **적용하기 (Apply):** 같은 서브넷 프린터에 보낼 때 Request와 Reply를 연결한다.
- **찾아보기 (Lookup):** ARP packet opcode와 형식은 표준 문서나 캡처에서 확인한다.

## Gateway의 MAC이 필요한 이유

이 Ethernet 예에서 인터넷으로 나가려면 게이트웨이의 MAC 주소를 알아야 한다. 게이트웨이를 192.168.0.1, 부팅 후 DHCP로 설정을 받은 PC를 192.168.0.100이라고 하자. PC는 DHCP 설정을 통해 자신의 게이트웨이가 192.168.0.1이라는 사실은 알고 있다. 그러나 이 IP에 대응하는 MAC 주소는 별도로 알아내야 한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 원격 목적지에 보낼 때 PC는 서버 MAC이 아니라 게이트웨이 MAC을 사용한다.
- **적용하기 (Apply):** IP 목적지는 원격 서버로 유지되고 Ethernet 목적지는 게이트웨이인 이유를 말한다.
- **찾아보기 (Lookup):** 기본 게이트웨이의 IP·MAC 관계는 ARP cache에서 확인한다.

## 외부 사이트로 접속하는 경로

네이버의 IP 주소를 설명용으로 3.3.3.3이라고 가정한다. 실제 주소라는 뜻은 아니다. 여기서는 목적지 IP를 이미 알고 있다고 가정하며, 도메인 이름에서 IP 주소를 찾는 과정은 뒤의 Unit 9에서 다룬다. 외부 사이트에 접속할 때 PC가 알아야 하는 MAC 주소는 인터넷 너머 서버의 것이 아니라 같은 구간에서 다음으로 패킷을 받을 게이트웨이의 것이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 외부 사이트로 향하는 Frame은 목적지 IP와 목적지 MAC이 다를 수 있다.
- **적용하기 (Apply):** DNS로 목적지 IP를 알아낸 뒤 다음 홉 MAC을 구하는 순서를 설명한다.
- **찾아보기 (Lookup):** 실제 DNS 질의와 ARP 교환은 패킷 캡처에서 찾아본다.

## 브로드캐스트로 MAC 질의

PC는 ARP Request를 브로드캐스트로 보내 ‘192.168.0.1을 사용하는 호스트’를 찾는다. 다른 호스트들은 그 주소의 주인이 아니므로 응답하지 않는다. 해당 IP 주소를 사용하는 게이트웨이는 자신을 찾는 요청이라는 사실을 알 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** ARP Request는 같은 브로드캐스트 도메인에 IP 소유자를 묻는다.
- **적용하기 (Apply):** 요청을 받은 여러 Host 중 대상 주소의 장치가 응답할 조건을 판별한다.
- **찾아보기 (Lookup):** ARP broadcast 주소와 cache 상태는 `arp -a`/`ip neigh`로 확인한다.

## 해당 장치의 응답

게이트웨이는 ARP Reply로 자신의 IP 주소와 MAC 주소를 알려 준다. PC는 192.168.0.1에 대응하는 48비트 MAC 주소를 얻는다. 이제 외부 사이트에 접속하기 위해 만든 IP 패킷을 어떤 L2 목적지로 보낼지 결정할 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** ARP Reply는 요청된 IP에 대응하는 인터페이스 MAC을 알려 준다.
- **적용하기 (Apply):** 응답에서 얻은 주소가 Ethernet Frame 목적지가 되는 과정을 말한다.
- **찾아보기 (Lookup):** gratuitous ARP와 중복 주소 감지는 관련 장비 문서에서 찾아본다.

## IP Packet을 Frame에 담기

IP 패킷의 출발지는 PC인 192.168.0.100, 목적지는 외부 사이트를 가정한 3.3.3.3이다. 이를 담은 Ethernet 프레임의 출발지 MAC은 PC의 NIC 주소, 목적지 MAC은 게이트웨이의 주소다. IP 목적지는 “최종적으로 누구에게 보낼까?”, 프레임의 목적지 MAC은 “이번 LAN에서 누구에게 맡길까?”에 답한다. [Unit 4 Lesson 1의 주소 역할 설명](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/4/lesson/1/page/1)과 이어서 기억하자. 프레임은 먼저 게이트웨이에 전달하고, 게이트웨이가 IP 헤더의 목적지를 보고 다음 경로로 라우팅한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Ethernet Frame의 MAC 목적지는 이번 링크의 다음 수신자다.
- **적용하기 (Apply):** 원격 Packet을 게이트웨이 Frame에 넣어 최종 IP와 구간 MAC을 구분한다.
- **찾아보기 (Lookup):** 스위치에서 Frame 헤더 값은 Wireshark 캡처로 확인한다.

## ARP Cache에 남기는 정보

DHCP는 게이트웨이의 IP 주소를 알려 주지만, 그 IP에 대응하는 MAC 주소까지 알려 주지는 않는다. 따라서 PC는 통신이 필요할 때 ARP로 해당 IP의 MAC 주소를 구한다. 이렇게 알아낸 대응 관계는 **ARP 캐시(ARP cache)**에 잠시 저장되어, 다음 통신에서 매번 다시 물어보지 않도록 돕는다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** ARP cache는 IP-MAC 대응을 잠시 저장해 반복 질의를 줄인다.
- **적용하기 (Apply):** 통신 직후 cache entry가 생기고 시간이 지나 사라질 수 있음을 설명한다.
- **찾아보기 (Lookup):** cache 만료 시간은 OS와 네트워크 장비에서 확인한다.

## arp -a로 확인하기

Windows와 macOS에서는 `arp -a`, Linux에서는 `ip neigh` 명령으로 현재 ARP 캐시를 볼 수 있다. 출력에서 IP 주소와 MAC 주소가 한 쌍으로 표시되는지, 게이트웨이 주소가 있는지 살펴보자. 통신한 지 오래됐거나 아직 해당 장치에 말을 건 적이 없다면 항목이 없을 수 있다. 이때는 게이트웨이에 한 번 통신을 시도한 뒤 다시 확인하면 새 기록이 생기는지 볼 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** `arp -a` 또는 `ip neigh`로 최근에 학습한 IP-MAC 관계를 확인한다.
- **적용하기 (Apply):** 게이트웨이와 통신한 전후에 cache 항목이 달라지는지 비교한다.
- **찾아보기 (Lookup):** OS별 상태·삭제 옵션은 명령 도움말에서 확인한다.
