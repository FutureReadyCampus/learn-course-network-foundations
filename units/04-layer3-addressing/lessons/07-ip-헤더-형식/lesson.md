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
    caption: 이 그림은 RFC 791의 IPv4 헤더 배치를 입문용으로 다시 그린 것이다. 필드 전체를 외우기보다 지금 배울 Version·IHL·Total Length·TTL·Protocol이 어디 있는지 찾아보자.
    after_paragraph: 1
- terms:
  - Version
  - IHL (Internet Header Length)
  - Total Length
  - MTU (Maximum Transmission Unit)
  animations:
  - file: l17-byte-45-split.svg
    title: 첫 바이트 45에서 Version과 IHL 읽기
    alt: 16진수 45가 8비트로 펼쳐진다. 앞의 네 비트 0100은 Version 4, 뒤의 네 비트 0101은 IHL 5이며, IHL 5는 4바이트 단위 다섯 개, 즉 20바이트 헤더를 뜻한다.
    caption: 0x45를 4비트씩 나누면 Version 4와 IHL 5를 읽을 수 있다. IHL은 32비트 단위의 헤더 길이다.
    after_paragraph: 2
  - file: l17-packet-mtu-split.svg
    title: MTU 1,500바이트 안의 헤더와 페이로드
    alt: 일반적인 MTU 1,500바이트 안에 IPv4 기본 헤더 20바이트와 페이로드 최대 1,480바이트가 함께 들어가는 모습을 보여 준다.
    caption: MTU는 링크가 한 번에 나를 수 있는 IP 패킷의 크기 상한이다. 이 예에서는 헤더 20바이트와 페이로드 1,480바이트를 합쳐 1,500바이트가 된다. 모든 링크의 MTU가 1,500바이트로 고정된 것은 아니다.
    after_paragraph: 4
- terms:
  - TTL (Time To Live)
  - Protocol
  - Header Checksum
  animations:
  - file: l17-ttl-hops.svg
    title: 라우터를 지날 때마다 줄어드는 TTL
    alt: TTL 128인 패킷이 라우터를 통과할 때 값이 하나씩 줄어든다. TTL 1인 패킷은 다음 라우터에서 0이 되어 버려진다.
    caption: TTL은 패킷이 네트워크를 끝없이 돌지 않게 제한한다. 실제로는 라우터를 거칠 때마다 적어도 1씩 줄고, 0이 되면 폐기된다.
    after_paragraph: 1
- terms:
  - Wireshark
  - 출발지 IP 주소
  - 목적지 IP 주소
  - Identification
  - Flags
  - Fragment Offset
animations_dir: units/04-layer3-addressing/lessons/07-ip-헤더-형식/assets/animations
---
## IP 패킷의 앞부분에는 전달 정보가 담긴다

택배 상자에 받는 곳과 배송에 필요한 표시를 적듯이, IP 패킷의 앞부분에는 목적지까지 전달하는 데 필요한 정보가 담긴다. 이 앞부분이 **IP 헤더**이고, 뒤에 실린 상위 계층의 데이터가 **페이로드(Payload)**다. 헤더와 페이로드를 합쳐 하나의 IP 패킷을 이룬다.

IP 헤더는 단순한 주소표 하나가 아니다. 패킷의 길이, 다음에 어떤 프로토콜 데이터가 오는지, 전달 중 얼마나 더 이동할 수 있는지 같은 정보도 있다. 그림은 IPv4 헤더가 실제로 배치되는 순서를 보여 준다. 한 줄은 32비트, 즉 4바이트다.

IP 헤더의 모든 칸을 지금 외울 필요는 없다. 우선 버전과 헤더 길이를 읽는 법, 전체 길이와 MTU의 차이, TTL과 Protocol의 역할을 익히자. 다른 칸은 그림에서 위치를 알아보고 필요할 때 다시 찾아보면 된다.

## Version과 IHL로 헤더의 길이를 읽는다

IPv4 헤더의 첫 바이트에는 **Version**과 **IHL**이 각각 4비트씩 들어간다. Version은 어떤 IP 형식인지 나타낸다. 이 Lesson에서 다루는 IPv4라면 값은 4다. IHL은 Internet Header Length의 약자로, 헤더가 몇 개의 32비트 단위로 이루어졌는지 나타낸다.

Wireshark에서 첫 바이트가 `45`로 보인다고 하자. 이는 16진수 `0x45`이며, 2진수로 펼치면 `0100 0101`이다. 앞의 네 비트 `0100`은 4, 뒤의 네 비트 `0101`은 5이므로 Version은 4, IHL은 5다. 16진수 한 자리마다 4비트라는 점은 Unit 1에서 본 진법 설명과 연결된다.

IHL의 단위는 바이트가 아니라 32비트, 즉 4바이트다. 그래서 IHL이 5이면 헤더 길이는 `5 × 4 = 20바이트`다. 옵션이 들어간 헤더는 이보다 길어질 수 있으며, 그런 경우 IHL 값도 커진다. `45` 예시는 옵션이 없는 기본 길이의 IPv4 헤더를 뜻한다.

**Total Length**는 헤더만의 길이가 아니라 헤더와 페이로드를 합친 IP 패킷 전체 길이다. 예를 들어 Wireshark가 Total Length를 331바이트로 보여 주고 IHL이 5라면, 전체 331바이트 중 헤더가 20바이트이고 나머지 311바이트가 페이로드다. `331`은 한 패킷의 관측값이지 외울 숫자는 아니다.

앞서 본 MTU는 한 링크가 한 번에 나를 수 있는 IP 패킷 크기의 상한이다. 흔히 쓰는 1,500바이트 MTU 예에서는 IPv4 기본 헤더 20바이트도 그 안에 들어가므로 페이로드 자리는 최대 1,480바이트다. Total Length의 형식상 최댓값 65,535바이트와 실제 링크의 MTU는 서로 다른 기준이다. 한 링크의 MTU를 넘는 패킷을 어떻게 처리하는지는 Unit 6 Lesson 1의 단편화에서 이어서 살펴본다.

## Protocol과 TTL은 전달 중의 역할을 알려 준다

IP 패킷이 목적지에 도착하면 IP 헤더의 **Protocol** 필드가 페이로드를 다음에 어떤 프로토콜로 해석할지 알려 준다. 예를 들어 값 6은 TCP, 17은 UDP, 1은 ICMP를 가리킨다. 그러면 수신 측은 IP 페이로드의 시작부터 해당 프로토콜의 형식에 따라 처리한다. Protocol 값은 ‘어느 프로그램인가’를 뜻하는 포트 번호와 다르다. 다음 프로토콜의 번호는 필요할 때 IANA 목록에서 확인할 수 있다.

**TTL(Time To Live)**은 패킷이 네트워크를 끝없이 맴돌지 않도록 수명을 제한하는 값이다. 라우터는 패킷을 전달할 때 TTL을 적어도 1 줄인다. 전달 도중 값이 0이 되면 라우터는 그 패킷을 폐기한다. 이름에는 ‘시간’이 들어가지만, 일반적인 학습에서는 라우터를 몇 번 거칠 수 있는지를 제한하는 값으로 이해하면 된다.

헤더에는 **Header Checksum**도 있다. 이 값은 IP 헤더의 오류를 확인하며 페이로드 데이터의 무결성을 확인하는 값은 아니다. TTL처럼 라우터에서 바뀌는 헤더 정보가 있으므로, 라우터는 헤더 체크섬을 다시 계산한다. 체크섬은 암호화나 보안용 인증 코드와도 다르다.

출발지 IP 주소와 목적지 IP 주소는 각각 32비트이며, IP 패킷이 어디서 왔고 어디로 향하는지 나타낸다. 앞 페이지의 그림에서 Protocol·TTL과 함께 위치를 확인해 보자. 나머지 식별자와 플래그, 단편화 오프셋은 패킷을 나누고 다시 처리하는 상황에서 쓰이며, 세부 동작은 Unit 6에서 배운다.

## Wireshark에서 핵심 필드를 찾아본다

Wireshark에서 패킷 하나를 선택하고 **Internet Protocol Version 4** 항목을 펼치면, 아래쪽의 원시 바이트와 위쪽의 해석된 필드가 함께 보인다. 먼저 Version이 4인지, Header Length가 20바이트인지, Total Length가 얼마인지 확인해 보자. 원시 첫 바이트가 `45`라면 앞 페이지처럼 Version 4와 IHL 5를 읽는다.

그다음 Protocol, TTL, Source Address, Destination Address를 찾는다. Protocol이 6이면 그 뒤의 IP 페이로드를 TCP로 해석하고, TTL은 라우터를 지날수록 줄어든다. 주소 두 개는 출발지와 목적지를 보여 준다. 패킷마다 주소와 수치는 달라질 수 있으므로 예시 값을 외우기보다 필드 이름과 역할을 연결하자.

Identification, Flags, Fragment Offset은 단편화와 관련된 필드다. Type of Service로 알려졌던 칸은 현재 DSCP와 ECN으로 나누어 쓰며, 옵션과 패딩은 필요한 경우에만 들어간다. 세부 값이나 전체 필드 목록을 암기할 필요는 없다. 분석할 때는 그림에서 위치를 확인하고, Wireshark가 보여 주는 이름과 RFC의 설명을 함께 참고하면 된다.

### 이 Lesson에서 가져갈 것

- **회상할 핵심:** IP 헤더는 전달 정보, 페이로드는 그 뒤에 실린 데이터다. IHL은 32비트 단위의 헤더 길이이고 Total Length는 헤더를 포함한 IP 패킷 전체 길이다. Protocol은 다음 프로토콜을, TTL은 전달 가능한 범위를 알려 준다.
- **사례에 적용할 것:** 첫 바이트 `0x45`에서 Version 4와 IHL 5를 나누어 읽고, 기본 헤더 길이가 20바이트임을 설명해 보자. Wireshark에서 Protocol과 TTL이 뜻하는 바도 찾아보자.
- **필요할 때 찾아볼 것:** Identification·Flags·Fragment Offset·DSCP/ECN·Header Checksum의 세부 형식과 Protocol 번호 목록은 필요할 때 그림과 RFC/IANA 목록에서 확인한다. 다음 Lesson에서는 IP 주소의 네트워크 부분을 CIDR로 구분하는 법을 배운다.
