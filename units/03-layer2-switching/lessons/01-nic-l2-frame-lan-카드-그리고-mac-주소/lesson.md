---
id: u3-l08-nic-l2-frame-lan-카드-그리고-mac-주소
title: NIC, L2 Frame, LAN 카드 그리고 MAC 주소
source_wiki: sources/wiki/oeweo-network/lesson-08.md
wiki_diagram: sources/wiki/oeweo-network/concepts/lesson-08.svg
page_metadata:
- terms:
  - NIC (Network Interface Card)
  - 인터페이스 (Interface)
  - 리얼텍 (Realtek)
- terms:
  - 호스트 (Host)
  - 액세스 포인트 (Access Point)
  - LAN (Local Area Network)
  - 인터페이스와 케이블 구멍
  animations:
  - file: l08-host-two-nics.svg
    title: 호스트 하나, 인터페이스 둘
    alt: 노트북 모양의 네모 하나에 진한 점이 처음엔 하나, 나중엔 둘로 늘어납니다. 점 하나는 무선으로 액세스 포인트에, 다른 하나는 선으로
      이어집니다. 마지막 장면에서도 점은 둘로 유지되고 ‘점 2개 = 인터페이스 2개’ 문구가 나옵니다.
    caption: 노트북 한 대에 무선 NIC와 USB 유선 NIC가 달리면 문이 두 개가 됩니다. 진한 점 하나가 인터페이스 하나이므로 점
      두 개는 인터페이스 두 개입니다.
- terms:
  - LAN (Local Area Network)
  - MAN (Metropolitan Area Network)
  - WAN (Wide Area Network)
- terms:
  - MAC 주소 (Media Access Control address)
  - 식별자 (identifier)
  - 16진수 (hexadecimal)
  - 임시 MAC 주소
  animations:
  - file: l08-mac-address-label.svg
    title: NIC에 붙는 문패, MAC 주소
    alt: NIC 모양의 작은 카드에 여섯 덩어리의 MAC 주소 라벨이 붙습니다. 호스트에 NIC가 하나 더 붙으면 다른 값의 라벨이 하나 더
      생깁니다. 공장에서 새긴 주소만 앞 세 덩어리를 회사로 읽을 수 있고, 임시 주소는 그렇게 읽지 않는다는 점도 함께 보입니다.
    caption: 공장에서 NIC마다 서로 다른 MAC 주소가 새겨지고, 한 호스트의 NIC가 둘이면 주소도 둘입니다. 무선 연결에서는 개인정보
      보호를 위한 임시 주소가 대신 보이기도 합니다.
- terms:
  - 프레임 (Frame)
  - L2 (Layer 2, 계층 2)
  - 패킷 (Packet)
  - 메인보드 (Mainboard)
- terms:
  - Ethernet
  - Jumbo Frame
  - 바이트 (Byte)
- terms:
  - 비트 (bit)
  - 바이트 (Byte)
  - bps (bits per second)
  - 기가비트 (Gigabit)
  animations:
  - file: l08-bit-vs-byte-speed.svg
    title: 소문자 b와 대문자 B, 8배의 차이
    alt: 작은 물방울 8개가 모여 병 하나가 되고, 그 아래 b와 B 글자가 나란히 놓입니다. 이어서 1Gbps 눈금이 약 125MB/s 눈금으로
      환산됩니다.
    caption: 8비트가 1바이트이므로 1Gbps는 초당 1GB가 아니라 약 0.125GB입니다.
- terms:
  - 광섬유 케이블
  - 슬롯 (Slot)
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
