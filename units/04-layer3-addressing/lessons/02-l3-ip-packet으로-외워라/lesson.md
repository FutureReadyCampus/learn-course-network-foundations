---
id: u4-l12-l3-ip-packet으로-외워라
title: L3 IP Packet으로 외워라
source_wiki: sources/wiki/oeweo-network/lesson-12.md
wiki_diagram: sources/wiki/oeweo-network/concepts/lesson-12.svg
page_metadata:
- terms:
  - 패킷 (Packet)
  - 데이터 (Data)
- terms:
  - IP (Internet Protocol)
  - L3 (3계층, 네트워크 계층)
  - 프레임 (Frame)
  - 프로토콜 (Protocol)
- terms:
  - MTU (Maximum Transmission Unit)
  - 바이트 (Byte)
- terms:
  - 헤더 (Header)
  - 페이로드 (Payload)
  animations:
  - file: l12-header-payload.svg
    title: 송장 붙은 상자, 헤더와 페이로드
    alt: 기다란 직사각형 상자의 앞쪽에 헤더라는 송장 부분이 붙고 나머지가 페이로드로 채워집니다. 그 페이로드가 열리면 안에 헤더와 페이로드를
      가진 작은 상자가 다시 나타납니다.
    caption: 헤더는 길을 안내하는 송장, 페이로드는 상자 속 내용물입니다. 상자 안에 다시 상자가 들어 있을 수도 있습니다.
- terms:
  - 와이어샤크 (Wireshark)
  - 16진수 (Hexadecimal)
  - Type (이더넷 타입)
  - IHL (Internet Header Length)
  animations:
  - file: l12-hex-decode.svg
    title: 16진수 숫자 줄을 헤더로 읽기
    alt: 회색 16진수 숫자들이 가로로 늘어서 있고, 앞에서부터 색깔이 입혀지며 목적지 MAC, 출발지 MAC, Type 0800, IP 45,
      출발지 IP c0 a8 00 0a라는 이름표가 차례로 붙습니다.
    caption: 16진수 숫자의 줄이 앞에서부터 이더넷 헤더, IP 헤더 순서로 의미가 붙어 갑니다.
- terms:
  - 스니퍼 (Sniffer)
  - 분석기 (Analyzer)
  - 프로토콜 디코더 (Protocol Decoder)
- terms:
  - MAC 주소 (Media Access Control address)
  - IP 주소 (Internet Protocol address)
  - 포트 번호 (Port number)
  animations:
  - file: l12-three-addresses.svg
    title: 출발지와 도착지를 나타내는 세 가지 주소
    alt: 패킷 하나의 헤더에서 계층 2의 MAC 주소, 계층 3의 IP 주소, 계층 4의 포트 번호가 차례로 켜지며 각각 출발지와 목적지를
      나타냅니다.
    caption: 헤더에서 MAC 주소, IP 주소, 포트 번호는 계층이 다를 뿐 모두 ‘어디서 어디로’를 나타냅니다.
---

핵심 개념을 주제별로 정리했다.

## Packet이라는 단위

패킷(Packet)은 하나의 단위 데이터다. 레고의 블록 하나나 여러 재료를 감싼 쌈에 비유할 수 있다. 핵심은 여러 내용을 감싸 하나의 작은 전달 단위로 만든다는 점이다.

## L3 IP Packet으로 연결하기

여기서는 패킷을 L3 IP와 연결해 기억하도록 ‘L3 IP Packet’이라는 표현을 사용한다. 패킷이라는 말을 들으면 IP 프로토콜과 OSI의 L3 네트워크 계층을 함께 떠올리면 된다. 패킷의 논리적 구조는 크게 Header와 Payload로 나뉜다. L2 프레임도 이러한 구조를 갖는다. 패킷을 다룰 때는 전체의 최대 크기도 중요하다.

## MTU와 패킷의 크기

MTU는 Maximum Transmission Unit의 약자다. 이 그림에서는 헤더의 시작부터 페이로드의 끝까지, 전달할 패킷 전체의 최대 크기를 가리킨다. 특별한 이유가 없다면 1,500바이트로 설명하며, 약 1.4x킬로바이트에 불과하다. 큰 데이터를 한 번에 모두 담기에는 작은 단위라는 점을 기억해야 한다.

## Header와 Payload

패킷은 직소 퍼즐의 조각 하나 또는 송장이 붙은 택배 상자 하나에 비유할 수 있다. Header는 송장, Payload는 그 헤더가 실어 나르는 내용물이다. 둘은 상대적인 개념으로 함께 이해한다. 이 단원의 인터넷 전달 예에서 MTU는 1,500바이트다. 작은 단위를 이용해 정보를 전달한다는 관점을 바탕으로, 실제 패킷이 어떻게 보이는지 살펴볼 수 있다.

## Wireshark에서 패킷 보기

Wireshark를 사용하면 네트워크의 패킷을 수집해 살펴보고, 파일로 저장하거나 저장한 캡처를 다시 열 수 있다. 화면 아래의 16진수 데이터는 프레임 전체를 나타낸다. Ethernet 헤더에는 목적지 MAC 주소, 출발지 MAC 주소, Type 값이 있다. 예시의 Type 0800을 보고 뒤의 데이터를 IP로 해석한다. 이어지는 분석에는 IPv4의 Version 4와 IHL 5, 출발지·목적지 IP 주소, TCP와 포트 번호 등이 표시된다. 16진수 데이터를 사람이 직접 모두 해석하지 않아도 Wireshark가 프로토콜별로 분석한 결과를 보여 준다.

## 캡처와 네트워크 관찰

Wireshark는 프로토콜 디코더, 분석기(Analyzer), 스니퍼(Sniffer)라고도 설명한다. 네트워크에서 패킷을 수집해 프로토콜을 해석하는 도구다. 의사의 청진기나 돋보기처럼, 통신을 관찰해 장애 원인을 찾고 어떤 통신이 이루어지는지 분석하며 네트워크 효율을 개선할 방법을 살펴보는 데 사용한다. 여기서 사용법 전체를 다루지는 않지만, 네트워크를 공부하며 익혀야 할 도구다.

## 헤더 속 식별자 정리

패킷을 보면 16진수 데이터와 이를 해석한 헤더 정보를 확인할 수 있다. Header와 Payload를 함께 이해하고, 최대 전송 단위인 MTU를 기억해야 한다. 헤더에서 중요한 정보는 어디에서 와서 어디로 가는지다. 계층에 따라 MAC 주소, IP 주소, 포트 번호가 출발지와 목적지를 나타내는 데 사용된다.
