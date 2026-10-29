---
id: u4-l17-ip-헤더-형식
title: IP 헤더 형식
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-17.md
wiki_diagram: units/04-layer3-addressing/lessons/07-ip-헤더-형식/assets/diagrams/lesson-17.svg
page_metadata:
- terms:
  - 헤더 (Header)
  - 페이로드 (Payload)
  - MTU (Maximum Transmission Unit)
  animations:
  - file: l17-packet-mtu-split.svg
    title: 1,500바이트 상자의 속 나누기
    alt: 긴 막대 하나가 1,500바이트로 표시되고, 앞쪽 20바이트가 헤더, 나머지 1,480바이트가 페이로드로 나뉘는 장면입니다.
    caption: MTU 1,500바이트 안에서 헤더 20바이트를 빼면 페이로드는 1,480바이트가 남습니다.
- terms:
  - 비트 (bit)
  - 바이트 (byte)
  - 16진수 (hexadecimal)
  - IHL (Internet Header Length)
  animations:
  - file: l17-byte-45-split.svg
    title: 첫 바이트 45 쪼개 보기
    alt: 16진수 45가 8개의 켜짐·꺼짐 칸으로 풀리고, 앞 4칸은 Version 4, 뒤 4칸은 IHL 5로 나뉘며 헤더 5줄이 20바이트가
      되는 장면입니다.
    caption: 16진수 45는 8칸으로 풀면 앞 4칸은 Version 4, 뒤 4칸은 IHL 5입니다.
- terms:
  - Total Length
  - Type of Service (TOS)
- terms:
  - 단편화 (Fragmentation)
  - TTL (Time To Live)
- terms:
  - 홉 (Hop)
  - Protocol 필드
  - IANA
  animations:
  - file: l17-ttl-hops.svg
    title: 홉마다 줄어드는 TTL
    alt: 왼쪽 컴퓨터에서 TTL 128 패킷이 출발해 라우터 세 개를 지나며 127, 126, 125로 줄고, 다른 패킷은 TTL 1에서 0이
      되어 사라지는 장면입니다.
    caption: 패킷이 라우터를 하나 지날 때마다 TTL이 1씩 줄고, 0이 되면 사라집니다.
- terms:
  - 검사합 (Checksum)
- terms:
  - Wireshark
  - Identification
- terms:
  - 계층별 해석
animations_dir: units/04-layer3-addressing/lessons/07-ip-헤더-형식/assets/animations
---

핵심 개념을 주제별로 정리했다.

## IPv4 Header의 전체 모양

IP 패킷 전체의 최대 전송 크기는 MTU이며, 이 단원의 일반적인 예는 1,500바이트다. IPv4 헤더는 옵션이 없다면 20바이트이므로, 이 경우 Payload에 남는 공간은 1,480바이트다. 옵션이 있으면 헤더가 더 길어질 수 있다. IP 형식상으로는 헤더와 데이터를 합해 약 64K 크기까지 표현할 수 있다. 그림의 최대 데이터 크기 65,515는 전체 길이에서 기본 헤더 길이를 뺀 값이다. 다만 실제 전송은 보통 경로의 MTU에 맞추어 이루어진다는 점을 구별해야 한다.

## Version과 IHL

헤더 도식은 가로 한 행을 32비트, 즉 4바이트로 표현한다. 한 바이트는 8비트이고, 4비트씩 두 자리의 16진수로 나타낼 수 있다. Wireshark에서도 이러한 표기를 자주 본다. Version 필드는 4비트다. IPv4를 다루므로 값은 4다. IHL은 Internet Header Length로, 헤더의 길이를 나타낸다. 기본값 5는 도식의 다섯 행에 해당하며, 4바이트 단위로 해석한다.

## Total Length

IHL이 5라면 5×4로 계산해 헤더 길이는 20바이트다. Type of Service 필드의 세부 내용은 별도로 살펴볼 수 있다. Total Length는 헤더를 포함한 IP 패킷 전체의 길이다. 16비트 필드이므로 가장 큰 값은 65,535이며, 기본 헤더 20바이트를 빼면 데이터는 최대 65,515바이트다. 약 64K라는 형식상의 한계를 이 값과 연결해 이해한다.

## 단편화 관련 필드

도식의 두 번째 행에 있는 필드들은 단편화(Fragmentation)와 관련된다. 예를 들어 1,500바이트 패킷이 지나가려는 구간의 MTU가 1,300바이트라면, 더 작은 조각으로 나누어야 할 수 있다. 이것이 단편화다. TTL(Time To Live)은 패킷이 계속 돌아다니지 않도록 제한하는 값이다. 8비트이므로 표현 가능한 최댓값은 255이며, 0이 되면 패킷을 버린다.

## TTL과 Protocol

TTL은 패킷이 Hop을 지날 때마다 감소한다. Protocol 필드는 IP Payload의 내용을 어떤 프로토콜로 해석할지 알려 준다. IP 안에는 TCP, UDP, ICMP, IGMP 등의 데이터가 올 수 있다. 각 프로토콜에는 고유 번호가 있고, IANA의 번호 목록에서 확인할 수 있다. 수신 측은 이 값을 근거로 안쪽 데이터를 해석한다.

## Header Checksum

Header Checksum은 전송 과정에서 헤더에 손상이 생겼는지 검사하기 위한 검사합이다. 재계산할 수 있으므로 이 값 자체가 보안성을 제공하는 것은 아니다.

## Wireshark에서 필드 읽기

IPv4의 출발지와 목적지 주소는 각각 32비트다. Wireshark에서는 실제 바이트와 이를 분석한 필드를 함께 볼 수 있다. 첫 바이트가 16진수 45라면 앞의 4는 Version, 뒤의 5는 IHL이다. IHL 5는 20바이트 헤더를 뜻한다. 예시에서 TOS는 0이고, Total Length의 014B는 10진수 331로 해석된다. Identification은 단편화와 관계된 필드다. TTL 128은 이후 Hop을 거치며 감소하는 값이며, 목적지를 찾기 전에 소진되면 패킷이 사라진다. Protocol 값 6은 IP Payload를 TCP로 해석하라는 뜻이다. Wireshark가 이러한 해석을 표시해 준다.

## 출발지·목적지 주소와 교차 확인

예시 화면에서는 체크섬 검증이 Disabled로 표시되어 실제 검사를 하지 않는다. 출발지와 목적지 IP 주소는 해당 32비트씩을 해석해 표시한다. IP 다음은 Protocol 값에 따라 TCP로 해석하고, 그 뒤에는 HTTP가 나타난다. 이처럼 계층별 해석 결과와 실제 바이트를 교차해 볼 수 있다. Wireshark를 사용하려면 16진수와 2진수, 바이트 단위의 구분에 익숙해져야 한다. 헤더 형식과 실제 데이터를 함께 살펴보는 습관이 필요하다. 단편화가 발생하는 이유는 이후에 더 다룬다.
