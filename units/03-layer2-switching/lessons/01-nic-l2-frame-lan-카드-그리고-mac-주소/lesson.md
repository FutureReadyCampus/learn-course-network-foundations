---
id: "u3-l08-nic-l2-frame-lan-카드-그리고-mac-주소"
title: "NIC, L2 Frame, LAN 카드 그리고 MAC 주소"
source_wiki: "sources/wiki/oeweo-network/lesson-08.md"
beginner_guide: "sources/wiki/oeweo-network/newbie/specs/lesson-08.json"
wiki_diagram: "sources/wiki/oeweo-network/concepts/lesson-08.svg"
illustrated_pages: [2, 4, 7]
---

핵심 개념을 주제별로 정리했다.

## NIC와 LAN 카드

LAN 카드는 NIC(Network Interface Card), 또는 네트워크 인터페이스라고도 부른다. 이후 여기서는 NIC와 인터페이스라는 표현을 사용하므로 같은 대상을 가리키는 말로 연결해 두면 된다. 예를 들어 ‘리얼텍 LAN 카드’ 대신 ‘리얼텍 네트워크 인터페이스’라고 표현할 수 있다.

## Host와 네트워크 인터페이스

네트워크 도식에서는 호스트를 네모로 그리고, 인터페이스를 진한 점으로 표시하기도 한다. PC에 점이 두 개 그려져 있다면 네트워크 인터페이스가 두 개 있다는 의미로 읽을 수 있다. 한 호스트가 여러 인터페이스를 갖는 일은 흔하다. 무선 NIC가 있는 노트북에 USB 유선 NIC를 추가하면 인터페이스가 두 개가 된다. 무선 인터페이스는 액세스 포인트에 연결하고, 다른 인터페이스는 유선으로 연결할 수 있다. LAN은 Local Area Network의 약자다.

## LAN과 네트워크 규모

LAN, MAN, WAN은 네트워크의 규모를 설명하는 표현이다. 여기서는 작은 범위의 LAN, 도시 규모의 MAN(Metropolitan Area Network), 더 넓은 범위의 WAN(Wide Area Network)으로 연결해 설명한다. 가정의 공유기에 태블릿, 스마트폰, 유선 PC, IPTV 수신기 등이 연결된 홈 네트워크를 하나의 LAN으로 생각할 수 있다. NIC는 이러한 네트워크에 연결하는 하드웨어이며, MAC 주소를 갖는다.

## MAC 주소 · NIC의 식별자

MAC(Media Access Control) 주소는 하드웨어 주소 또는 Physical Address라고도 한다. NIC에 부여되며, 네트워크 인터페이스를 식별하는 값이다.

## 유선·무선 NIC 살펴보기

자료에는 다나와에서 가져온 ipTIME NIC 이미지가 있다. 본체를 열고 메인보드에 직접 장착하는 유선 NIC도 있고, USB 인터페이스에 연결한 뒤 LAN 케이블을 꽂는 유선 NIC도 있다. USB 방식의 무선 NIC를 장착해 무선 네트워크에 연결할 수도 있다. NIC를 도식으로 그릴 때는 네트워크 연결 부분을 인터페이스로 표현한다. 이 장치가 다루는 L2 수준의 데이터 단위는 프레임(Frame)이다. 앞서 등장한 패킷과 구분해 두어야 한다.

## L2 Frame의 크기

프레임은 L2 네트워크에서 전달되는 데이터 단위다. 자료에는 10Base-T와 802.3, 802.5, 802.11 등의 규격 표기가 등장하며, 자세한 규격은 별도로 참고할 수 있다. 여기서는 일반적인 Ethernet 프레임의 크기를 약 1,514바이트로 설명한다. Jumbo Frame은 10K에 조금 못 미치는 크기로 소개한다. 이 설명의 이 구간은 바이트와 kb 표기가 섞여 있으므로 단위 표기는 원문 확인이 필요하다. NIC 사양에는 프레임 크기뿐 아니라 1Gbps 같은 전송 속도도 표시된다.

## bps와 바이트 단위 구별

bps는 초당 비트 수를 나타낸다. 소문자 b는 비트, 대문자 B는 바이트이므로 표기를 구별해야 한다. 8비트가 1바이트이기 때문에 1Gbps와 초당 1GB는 같은 속도가 아니다. 대문자 B로 잘못 쓰면 8배의 차이가 생긴다. 1Gbps NIC는 기가비트 NIC 또는 기가비트 네트워크라는 표현과 연결된다. 더 빠른 사양으로는 10Gbps도 있다.

## 내 컴퓨터의 인터페이스 확인

10Gbps는 1Gbps의 10배에 해당하는 속도다. 이러한 연결에서 구리선 단자 대신 광섬유 케이블을 사용하는 예도 소개한다. NIC라는 이름의 Card는 슬롯에 꽂는 카드 형태의 장치에서 나온 표현이다. LAN은 네트워크의 규모를, NIC는 연결 하드웨어를 가리킨다. MAC 주소는 NIC에 붙으며, 호스트 하나가 NIC를 여러 개 가질 수 있다는 점을 기억하면 된다.
