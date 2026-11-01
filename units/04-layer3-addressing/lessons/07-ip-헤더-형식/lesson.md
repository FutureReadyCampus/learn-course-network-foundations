---
id: u4-l17-ip-헤더-형식
title: IP 헤더 형식
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-17.md
additional_sources:
- https://github.com/FutureReadyCampus/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/03-1.md
- https://www.rfc-editor.org/rfc/rfc791.html
page_metadata:
- terms:
  - IP 헤더 (IP header)
  - 페이로드 (Payload)
  illustrations:
  - file: assets/diagrams/ipv4-header-map.svg
    title: IPv4 패킷의 헤더와 페이로드
    alt: 32비트 폭의 IPv4 헤더 구조를 보여 준다. 첫 세 행에는 Version, IHL, DS 필드, Total Length, Identification, Flags, Fragment Offset, TTL, Protocol, Header Checksum이 있다. 다음 두 행에는 출발지와 목적지 IP 주소가 있다. Options와 Padding은 선택 항목이고, 헤더 뒤에는 페이로드가 놓인다.
    caption: 이 그림은 RFC 791의 IPv4 헤더 배치를 입문용으로 다시 그린 것이다. 필드 전체를 외우기보다 지금 배울 Version·IHL·Protocol·TTL이 어디 있는지 찾아보자.
    after_paragraph: 1
- terms:
  - Version
  - IHL (Internet Header Length)
  animations:
  - file: l17-byte-45-split.svg
    title: 첫 바이트 45에서 Version과 IHL 읽기
    alt: 16진수 45가 8비트로 펼쳐진다. 앞의 네 비트 0100은 Version 4, 뒤의 네 비트 0101은 IHL 5이며, IHL 5는 4바이트 단위 다섯 개, 즉 20바이트 헤더를 뜻한다.
    caption: 0x45를 4비트씩 나누면 Version 4와 IHL 5를 읽을 수 있다. IHL은 32비트 단위의 헤더 길이다.
    after_paragraph: 2
- terms:
  - Protocol
  - TTL (Time To Live)
  animations:
  - file: l17-ttl-hops.svg
    title: 라우터를 지날 때마다 줄어드는 TTL
    alt: TTL 128인 패킷이 라우터를 통과할 때 값이 하나씩 줄어든다. TTL 1인 패킷은 다음 라우터에서 0이 되어 버려진다.
    caption: TTL은 패킷이 네트워크를 끝없이 돌지 않게 제한한다. 라우터를 거칠 때마다 적어도 1씩 줄고, 0이 되면 폐기된다.
    after_paragraph: 2
- terms:
  - Wireshark
  - Total Length
  - 출발지 IP 주소
  - 목적지 IP 주소
  - Identification
  - Flags
  - Fragment Offset
  - DSCP/ECN
  - Header Checksum
animations_dir: units/04-layer3-addressing/lessons/07-ip-헤더-형식/assets/animations
---
## IP 패킷의 앞부분에는 전달 정보가 담긴다

택배 상자에 받는 곳과 배송에 필요한 표시를 적듯이, IP 패킷의 앞부분에는 목적지까지 전달하는 데 필요한 정보가 담긴다. 이 앞부분이 **IP 헤더**이고, 뒤에 실린 상위 계층의 데이터가 **페이로드(Payload)**다. 헤더와 페이로드를 합쳐 하나의 IP 패킷을 이룬다.

IP 헤더는 단순한 주소표 하나가 아니다. 목적지 주소 외에도 다음에 어떤 프로토콜 데이터가 오는지, 전달 중 얼마나 더 이동할 수 있는지, IPv4 패킷을 나누어 보낼 때 어떤 정보를 참고하는지가 담긴다. 그림은 IPv4 헤더가 실제로 배치되는 순서를 보여 준다. 한 줄은 32비트, 즉 4바이트다. 패킷을 나누는 상황은 Unit 6 Lesson 1 「TTL과 단편화」에서 자세히 살펴본다.

IP 헤더의 모든 칸을 지금 외울 필요는 없다. 이 Lesson에서는 첫 바이트에서 Version과 IHL을 읽고, Protocol과 TTL이 어떤 역할을 하는지 살펴본다. 나머지 필드는 Wireshark에서 이름과 위치를 찾아보면 된다.

## Version과 IHL로 헤더의 길이를 읽는다

IPv4 헤더의 첫 바이트에는 **Version**과 **IHL**이 각각 4비트씩 들어간다. Version은 어떤 IP 형식인지 나타낸다. 이 Lesson에서 다루는 IPv4라면 값은 4다. IHL은 Internet Header Length의 약자로, 헤더가 몇 개의 32비트 단위로 이루어졌는지 나타낸다.

Wireshark에서 첫 바이트가 `45`로 보인다고 하자. 이는 16진수 `0x45`이며, 2진수로 펼치면 `0100 0101`이다. 앞의 네 비트 `0100`은 4, 뒤의 네 비트 `0101`은 5이므로 Version은 4, IHL은 5다. 16진수 한 자리마다 4비트라는 점은 Unit 1에서 본 진법 설명과 연결된다.

IHL의 단위는 바이트가 아니라 32비트, 즉 4바이트다. 그래서 IHL이 5이면 헤더 길이는 `5 × 4 = 20바이트`다. 옵션이 들어간 헤더는 이보다 길어질 수 있으며, 그런 경우 IHL 값도 커진다. `45` 예시는 옵션이 없는 기본 길이의 IPv4 헤더를 뜻한다.

**Total Length**는 헤더와 페이로드를 합친 IP 패킷 전체 길이다. 실제 값은 마지막 페이지의 Wireshark에서 확인하고, 여기서는 `0x45`로 헤더 길이를 읽는 데 집중하자.

## Protocol과 TTL은 전달 중의 역할을 알려 준다

IP 패킷이 목적지에 도착하면 IP 헤더의 **Protocol** 필드가 페이로드를 다음에 어떤 프로토콜로 해석할지 알려 준다. 예를 들어 값 6은 TCP, 17은 UDP, 1은 ICMP를 가리킨다. 값 1인 ICMP는 `ping` 같은 진단 도구에서도 만난다. Protocol 값은 ‘어느 프로그램인가’를 뜻하는 포트 번호와 다르다. ICMP가 네트워크 진단에 어떻게 쓰이는지는 Unit 6 Lesson 4 「ping과 RTT」에서 살펴본다.

**TTL(Time To Live)**은 패킷이 네트워크를 끝없이 맴돌지 않도록 수명을 제한하는 값이다. 라우터는 패킷을 전달할 때 TTL을 적어도 1 줄인다. 전달 도중 값이 0이 되면 라우터는 그 패킷을 폐기한다. 이름에는 ‘시간’이 들어가지만, 일반적인 학습에서는 라우터를 몇 번 거칠 수 있는지를 제한하는 값으로 이해하면 된다.

첫 페이지의 그림에서 Protocol과 TTL의 위치를 확인해 보자. TTL이 0이 된 패킷에 대한 알림과 단편화가 필요한 경우는 Unit 6 Lesson 1 「TTL과 단편화」에서 다룬다. 여기서는 Protocol이 다음 처리 프로토콜을 가리키고 TTL이 전달 범위를 제한한다는 역할을 기억하면 된다.

## Wireshark에서 핵심 필드를 찾아본다

Wireshark에서 패킷 하나를 선택하고 **Internet Protocol Version 4** 항목을 펼치면, 아래쪽의 원시 바이트와 위쪽의 해석된 필드가 함께 보인다. 먼저 Version이 4인지, Header Length가 20바이트인지, Total Length가 얼마인지 확인해 보자. 원시 첫 바이트가 `45`라면 2페이지에서 본 것처럼 Version 4와 IHL 5를 읽는다.

그다음 Protocol, TTL, Source Address, Destination Address를 찾는다. Protocol이 6이면 그 뒤의 IP 페이로드를 TCP로 해석하고, TTL은 전달 범위를 제한하는 값이다. 주소 두 개는 출발지와 목적지를 보여 준다. 패킷마다 주소와 수치는 달라질 수 있으므로 예시 값을 외우기보다 필드 이름과 역할을 연결하자.

Total Length는 헤더와 페이로드를 합친 패킷 전체 길이를 바이트 단위로 보여 준다. Wireshark가 예를 들어 331바이트라고 표시하면, 2페이지에서 구한 20바이트 헤더를 빼 나머지가 페이로드임을 알 수 있다. 출발지와 목적지 주소는 각각 32비트이며 패킷의 양 끝을 나타낸다. Identification, Flags, Fragment Offset은 단편화와 관련되며 세부 동작은 Unit 6 Lesson 1에서 배운다. Type of Service로 알려졌던 칸은 현재 DSCP와 ECN으로 나누어 쓰고, Header Checksum은 IP 헤더 오류를 확인하는 값이다. 옵션과 패딩은 필요한 경우에만 들어간다. 세부 값이나 전체 필드 목록은 외우지 않고 분석할 때 그림·Wireshark·RFC에서 찾아보면 된다.

### 이 Lesson에서 가져갈 것

- **회상할 핵심:** IP 헤더에는 목적지 전달 정보가 담기고, 페이로드는 그 뒤에 실린 데이터다. Protocol은 다음에 해석할 프로토콜을 가리키며 TTL은 패킷이 전달될 수 있는 범위를 제한한다.
- **사례에 적용할 것:** 첫 바이트 `0x45`에서 Version 4와 IHL 5를 나누어 읽고, 기본 헤더 길이가 20바이트임을 설명해 보자. Wireshark에서 Protocol과 TTL이 뜻하는 바도 찾아보자.
- **필요할 때 찾아볼 것:** Total Length, Identification·Flags·Fragment Offset, DSCP/ECN, Header Checksum의 뜻과 Protocol 번호 목록은 그림·Wireshark·RFC/IANA 목록에서 확인한다. 다음 Lesson에서는 IP 주소의 네트워크 부분을 CIDR로 구분하는 법을 배운다.
