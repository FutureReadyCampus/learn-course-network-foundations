---
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
  - MTU (Maximum Transmission Unit)
  questions:
  - id: u5-l01-p01-q01
    kind: choice
    difficulty: easy
    prompt: 택배 상자에서 실제 물건이 들어 있는 부분에 해당하는 IP 패킷의 부분은 무엇인가요?
    choices:
    - id: a
      text: IP 헤더
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: b
      text: 페이로드
      feedback: 맞아요. 페이로드는 IP 헤더 뒤에 실리는 실제 내용입니다.
    - id: c
      text: MTU
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: d
      text: Protocol
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: e
      text: TTL
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    answer: b
  - id: u5-l01-p01-q02
    kind: choice
    difficulty: medium
    prompt: 이더넷 MTU가 1,500바이트이고 IPv4 헤더가 기본 길이 20바이트일 때, 페이로드에 쓸 수 있는 최대 크기는 얼마인가요?
    choices:
    - id: a
      text: 1,480바이트
      feedback: 맞아요. 이 예에서는 패킷 전체 한도 1,500바이트에서 헤더 20바이트를 빼면 1,480바이트입니다.
    - id: b
      text: 1,500바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: c
      text: 1,520바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: d
      text: 1,280바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: e
      text: 20바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    answer: a
  - id: u5-l01-p01-q03
    kind: short
    prompt: IP 헤더 뒤에 놓이며, TCP나 UDP 같은 안쪽 데이터가 실리는 부분입니다. 이 개념을 영어 또는 한글로 적어 보세요.
    answers:
    - payload
    - 페이로드
    feedback: 정답은 payload(페이로드)입니다. IP 패킷에서 헤더 뒤에 실제 데이터가 실리는 부분입니다.
  question_placements:
  - question_id: u5-l01-p01-q01
    after_paragraph: 1
  - question_id: u5-l01-p01-q02
    after_paragraph: 5
  illustrations:
  - file: assets/animations/l17-daily-label-contents.svg
    title: "송장에는 받는 곳 말고도 적힌다"
    alt: "긴 상자 하나가 나타납니다. 상자의 앞쪽은 송장, 뒤쪽은 내용물로 나뉘고, 송장에서 받는 곳, 내용물 종류, 더 거칠 수 있는 횟수, 나눠 보낼 때 참고하는 정보 네 칸이 아래로 갈라져 나옵니다. 마지막에 송장과 내용물이 모여 상자 하나가 된다고 표시됩니다."
    caption: "택배 상자의 송장에는 받는 곳만 적힌 게 아니라 여러 안내가 함께 적힙니다."
    after_paragraph: -1
  - file: assets/animations/l17-header-payload-parts.svg
    title: "IP 헤더에는 전달 정보가 담긴다"
    alt: "긴 IP 패킷 하나가 나타납니다. 앞부분은 IP 헤더, 뒤쪽은 페이로드로 나뉘고, 헤더에서 목적지 주소, 다음에 올 프로토콜, 전달 범위를 제한하는 TTL, 나눠 보낼 때 참고하는 정보 네 칸이 아래로 갈라져 나옵니다. 마지막에 헤더와 페이로드가 모여 IP 패킷 하나가 된다고 표시됩니다."
    caption: "IP 헤더에는 목적지 주소 외에도 다음 프로토콜, 전달 범위 제한, 나눠 보낼 때 참고할 정보가 담깁니다."
    after_paragraph: 0
  - file: assets/diagrams/ipv4-header-map.svg
    title: "IPv4 패킷의 헤더와 페이로드"
    alt: "32비트 폭의 IPv4 헤더 구조를 보여 준다. 첫 세 행에는 Version, IHL, DS 필드, Total Length, Identification, Flags, Fragment Offset, TTL, Protocol, Header Checksum이 있다. 다음 두 행에는 출발지와 목적지 IP 주소가 있다. Options와 Padding은 선택 항목이고, 헤더 뒤에는 페이로드가 놓인다."
    caption: "이 그림은 RFC 791의 IPv4 헤더 배치를 입문용으로 다시 그린 것이다. 필드 전체를 외우기보다 지금 배울 Version·IHL·Protocol·TTL이 어디 있는지 찾아보자."
    after_paragraph: 1
- terms:
  - Version
  - IHL (Internet Header Length)
  - Total Length
  questions:
  - id: u5-l01-p02-q01
    kind: choice
    difficulty: easy
    prompt: IPv4 첫 바이트가 0x45일 때, 앞쪽 4비트가 나타내는 값은 무엇인가요?
    choices:
    - id: a
      text: 헤더 길이
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: b
      text: Protocol 번호
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: c
      text: IP 버전
      feedback: 맞아요. 0x45의 앞 4비트 0100은 IPv4의 Version 4를 나타냅니다.
    - id: d
      text: TTL
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: e
      text: 전체 패킷 길이
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    answer: c
  - id: u5-l01-p02-q02
    kind: choice
    difficulty: medium
    prompt: IHL 값이 6이라면 IPv4 헤더 길이는 얼마인가요?
    choices:
    - id: a
      text: 6바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: b
      text: 16바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: c
      text: 20바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: d
      text: 24바이트
      feedback: 맞아요. IHL의 한 단위는 4바이트이므로 6 × 4 = 24바이트입니다.
    - id: e
      text: 32바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    answer: d
  - id: u5-l01-p02-q03
    kind: short
    prompt: IPv4 헤더의 길이를 4바이트 단위로 나타내는 필드입니다. 이 필드의 이름을 적어 보세요.
    answers:
    - ihl
    - internet header length
    - 인터넷 헤더 길이
    feedback: 정답은 IHL(Internet Header Length)입니다. 헤더 길이를 4바이트 단위로 나타내는 필드입니다.
  question_placements:
  - question_id: u5-l01-p02-q01
    after_paragraph: 2
  - question_id: u5-l01-p02-q02
    after_paragraph: 3
  illustrations:
  - file: assets/animations/l17-daily-form-code-45.svg
    title: "두 자리 번호로 송장 길이를 읽는다"
    alt: "상자에 두 자리 번호 45가 적혀 있습니다. 앞 숫자 4는 양식 번호, 뒤 숫자 5는 줄 수로 나뉩니다. 송장은 4칸짜리 줄이 다섯 개이고, 5 곱하기 4로 송장 길이는 20칸입니다."
    caption: "두 자리 번호의 앞 숫자는 양식, 뒤 숫자는 줄 수입니다. 송장 길이는 줄 수에 한 줄의 칸 수를 곱해 구해요."
    after_paragraph: -1
  - file: assets/animations/l17-version-ihl-length.svg
    title: "첫 바이트 0x45로 헤더 길이 읽기"
    alt: "첫 바이트 16진수 45가 4와 5로 나뉘고, 각각 2진수 0100과 0101로 펼쳐집니다. 앞의 네 비트는 Version 4, 뒤의 네 비트는 IHL 5입니다. IHL 5는 4바이트 단위 다섯 줄이므로 5 곱하기 4로 헤더 길이는 20바이트이고, 옵션이 없는 기본 헤더입니다."
    caption: "0x45를 4비트씩 나누면 Version 4와 IHL 5를 읽을 수 있습니다. IHL은 4바이트(32비트) 단위의 개수이고, 5이면 헤더는 20바이트입니다."
    after_paragraph: 2
- terms:
  - Protocol
  - TTL (Time To Live)
  - 홉 (Hop)
  - 포트 번호 (Port number)
  questions:
  - id: u5-l01-p03-q01
    kind: choice
    difficulty: easy
    prompt: IP 헤더의 Protocol 필드는 무엇을 알려 주나요?
    choices:
    - id: a
      text: 패킷이 이동할 수 있는 라우터 수
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: b
      text: IP 페이로드 안에 어떤 프로토콜 데이터가 있는지
      feedback: 맞아요. Protocol은 페이로드 안에 TCP, UDP, ICMP 중 어떤 프로토콜 데이터가 있는지 가리킵니다.
    - id: c
      text: 목적지의 포트 번호
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: d
      text: 이더넷 링크의 최대 크기
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: e
      text: 패킷의 전체 바이트 수
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    answer: b
  - id: u5-l01-p03-q02
    kind: choice
    difficulty: medium
    prompt: TTL이 2인 패킷이 라우터를 두 번 거쳤고 그때까지 목적지에 도착하지 않았다면 어떻게 되나요?
    choices:
    - id: a
      text: TTL이 2로 유지되어 계속 전달된다
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: c
      text: Protocol이 UDP로 바뀐다
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: d
      text: 포트 번호가 0이 된다
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: e
      text: IP 헤더가 페이로드로 바뀐다
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: b
      text: TTL이 0이 되어 더 전달되지 않고 폐기된다
      feedback: 맞아요. 라우터를 지날 때 TTL이 줄며 0이 되면 패킷은 더 전달되지 않습니다.
    answer: b
  - id: u5-l01-p03-q03
    kind: short
    prompt: 라우터를 지날 때 값이 줄어들며, 0이 되면 패킷을 더 전달하지 않도록 하는 IP 헤더 필드입니다. 이 필드의 이름을 적어 보세요.
    answers:
    - ttl
    - time to live
    feedback: 정답은 TTL(Time To Live)입니다. 라우터를 지날 때 줄어드는 전달 제한값입니다.
  question_placements:
  - question_id: u5-l01-p03-q01
    after_paragraph: 1
  - question_id: u5-l01-p03-q02
    after_paragraph: 3
  illustrations:
  - file: assets/animations/l17-daily-kind-and-limit.svg
    title: "송장의 종류 표시와 이동 한도"
    alt: "위쪽에서는 상자의 송장에 내용물 종류 표시가 있고, 식품 창구, 서류 창구, 의류 창구 중 맞는 식품 창구가 켜집니다. 아래쪽에서는 출발 집에서 환승센터 세 곳을 지나며 이동 한도가 3, 2, 1로 줄고, 세 번째 환승센터에서 0이 되어 상자가 버려집니다."
    caption: "송장의 종류 표시는 맞는 창구를 고르고, 이동 한도는 환승할 때마다 줄어 0이 되면 상자가 버려집니다. 한도 값은 예시예요."
    after_paragraph: -1
  - file: assets/animations/l17-protocol-ttl.svg
    title: "Protocol과 TTL의 역할"
    alt: "위쪽에서는 IP 헤더의 Protocol 값 6이 TCP 칸과 이어져 켜지고, UDP는 17, ICMP는 1입니다. 아래쪽에서는 PC에서 라우터 세 대를 지나며 TTL이 3, 2, 1로 줄고, 세 번째 라우터에서 0이 되어 패킷이 폐기됩니다."
    caption: "Protocol은 다음에 해석할 프로토콜을 가리키고, 포트 번호와는 다릅니다. TTL은 라우터를 지날 때마다 줄고 0이 되면 폐기돼요. 그림의 TTL 값은 예시입니다."
    after_paragraph: 1
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
  questions:
  - id: u5-l01-p04-q01
    kind: choice
    difficulty: easy
    prompt: Wireshark에서 패킷의 원시 바이트와 함께 해석된 필드 목록을 볼 수 있습니다. 해석된 목록은 무엇을 보여 주나요?
    choices:
    - id: a
      text: 원시 바이트를 규칙에 따라 읽어 낸 필드 값
      feedback: 맞아요. Wireshark는 원시 바이트를 프로토콜 규칙에 따라 해석해 필드로 보여 줍니다.
    - id: b
      text: 패킷을 보낸 사람의 비밀번호
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: c
      text: 네트워크 케이블의 물리 길이
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: d
      text: 컴퓨터에 설치된 모든 프로그램
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: e
      text: 이더넷 스위치의 포트 개수
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    answer: a
  - id: u5-l01-p04-q02
    kind: choice
    difficulty: medium
    prompt: IP 헤더가 20바이트이고 Total Length가 331바이트라면 IP 페이로드 크기는 얼마인가요?
    choices:
    - id: a
      text: 20바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: b
      text: 311바이트
      feedback: 맞아요. Total Length에는 헤더가 포함되므로 331에서 20을 빼면 페이로드는 311바이트입니다.
    - id: c
      text: 331바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: d
      text: 351바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    - id: e
      text: 1,480바이트
      feedback: 다시 본문에서 해당 필드가 답하는 질문과 역할을 확인해 보세요.
    answer: b
  - id: u5-l01-p04-q03
    kind: short
    prompt: IP 헤더와 페이로드를 합친 IP 패킷 전체의 바이트 수를 나타내는 필드입니다. 이 필드의 이름을 적어 보세요.
    answers:
    - total length
    - 전체 길이
    feedback: 정답은 Total Length입니다. 헤더와 페이로드를 합친 IP 패킷 전체 길이를 나타냅니다.
  question_placements:
  - question_id: u5-l01-p04-q01
    after_paragraph: 1
  - question_id: u5-l01-p04-q02
    after_paragraph: 3
  illustrations:
  - file: assets/animations/l17-daily-lookup-screen.svg
    title: "송장 조회 화면에서 칸 찾기"
    alt: "위쪽에는 송장 조회 화면의 풀이 줄 일곱 개(양식, 송장 길이, 전체 크기, 종류, 이동 한도, 보낸 곳, 받는 곳)가, 아래쪽에는 원래 번호 20칸이 있습니다. 첫 칸 45에서 양식과 줄 수를, 이어서 종류, 이동 한도, 보낸 곳, 받는 곳 칸을 찾고, 마지막으로 전체 크기 331에서 송장 20칸을 빼면 내용물 311이 남습니다."
    caption: "조회 화면은 풀어 쓴 칸과 원래 번호를 함께 보여 줍니다. 번호와 크기 값은 설명용 예시예요."
    after_paragraph: -1
  - file: assets/animations/l17-wireshark-ip-fields.svg
    title: "Wireshark에서 핵심 필드 찾기"
    alt: "위쪽에는 Version, Header Length, Total Length, Protocol, TTL, Source, Destination 필드 일곱 줄이, 아래쪽에는 원시 바이트 20개가 있습니다. 첫 바이트 45에서 Version과 IHL을, 이어서 TTL, Protocol, 출발지와 목적지 주소 바이트를 찾고, 마지막으로 Total Length 331에서 헤더 20바이트를 빼면 페이로드 311바이트가 남습니다."
    caption: "Wireshark는 원시 바이트와 해석된 필드를 함께 보여 줍니다. 그림의 바이트, 주소, TTL 값은 설명용 예시예요."
    after_paragraph: 2
animations_dir: units/04-layer3-addressing/lessons/07-ip-헤더-형식/assets/animations
---
## IPv4 패킷의 앞부분에는 전달 안내가 담긴다

택배 상자를 떠올려 보자. 겉의 송장에는 받는 곳과 보낼 때 참고할 안내가 있고, 상자 안에는 실제 물건이 있다. IPv4 패킷도 앞부분의 **IP 헤더(IP header)**가 전달 안내를 맡고, 그 뒤의 **페이로드(payload)**가 실제 내용을 싣는다. 둘을 합친 것이 IP 패킷이다. 택배 송장은 비유일 뿐이다. 실제 헤더는 상자 바깥 종이가 아니라 패킷 안에서 페이로드보다 앞에 놓인 바이트들이다.

IP 헤더는 목적지 주소만 적는 칸이 아니다. 받는 컴퓨터의 IP 주소, 안쪽 데이터가 TCP인지 UDP인지, 패킷이 라우터를 얼마나 더 거칠 수 있는지, 단편화가 일어났다면 조각을 식별하는 정보 등이 함께 들어간다. 그래서 헤더를 읽으면 “어디로 가는가?”, “안쪽 내용을 어떤 프로토콜이 해석하는가?”, “전달 중 어떤 제한을 지켜야 하는가?”를 알 수 있다.

그림의 IPv4 헤더는 한 줄이 32비트, 즉 4바이트인 표로 그려져 있다. 이 표는 실제 헤더 바이트를 읽기 쉽게 배열한 것이다. 앞쪽에는 Version, IHL, Total Length 같은 형식과 크기 정보가 있고, 가운데에는 단편화 관련 정보와 TTL, Protocol, Header Checksum이 있으며, 뒤쪽에는 출발지와 목적지 IPv4 주소가 있다. 선택적으로 Options와 Padding이 뒤에 붙을 수도 있다.

모든 칸을 한 번에 외우기보다, 먼저 역할을 묶어 기억하자. **주소는 출발지와 목적지를, Protocol은 다음 해석 대상을, TTL은 전달 범위를, 단편화 관련 필드는 나뉜 패킷을 식별하는 데 필요한 정보를 알려 준다.**

여기서 MTU도 함께 구분하자. **MTU(Maximum Transmission Unit)**는 한 링크에서 실어 나를 수 있는 IP 패킷 하나의 최대 크기다. 흔한 Ethernet 예에서는 1,500바이트이며, 이 크기에는 IP 헤더도 포함된다. 옵션이 없는 20바이트 헤더라면 같은 조건에서 페이로드에 쓸 수 있는 크기는 최대 1,480바이트다. 실제로 한 번에 보낼 수 있는 크기는 연결 경로의 링크와 설정에 따라 달라질 수 있다. MTU는 길에서 통과할 수 있는 상자 크기이고, Total Length는 그 상자의 실제 전체 길이를 패킷 안에 기록한 값이라고 구별하면 된다.

이 Lesson에서는 Version과 IHL을 직접 읽고, Protocol·TTL을 실제 전달 흐름에 연결한 뒤, 나머지는 Wireshark에서 찾아본다. 단편화의 자세한 동작은 Unit 6 Lesson 1 「TTL과 단편화」에서 배운다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** IPv4 Header에는 주소와 패킷 처리에 필요한 필드가 들어 있다.
- **적용하기 (Apply):** Wireshark에서 IPv4 헤더와 Ethernet 헤더를 분리해 읽는다.
- **찾아보기 (Lookup):** Header 필드 순서와 길이는 IPv4 표준 문서에서 확인한다.

## Version과 IHL로 헤더의 길이를 읽는다

IPv4 헤더의 맨 앞 1바이트는 **Version**과 **IHL(Internet Header Length)** 두 값으로 나뉜다. 바이트는 8비트이고, 이 바이트의 앞 4비트가 Version, 뒤 4비트가 IHL이다. IPv4에서 Version 값은 4다. IP 헤더 그림에서 첫 줄이 32비트 단위로 그려져 있다는 점을 기억하면, “한 바이트의 위쪽 절반과 아래쪽 절반을 따로 읽는다”고 이해할 수 있다.

Wireshark의 원시 바이트에서 첫 값이 `45`로 보인다고 하자. 이 값은 16진수 `0x45`다. 16진수 한 자리는 4비트를 나타내므로 `4`는 `0100`, `5`는 `0101`이다. 따라서 `0100 0101`의 앞 절반 `0100`은 Version 4, 뒤 절반 `0101`은 IHL 5를 뜻한다. 여기서 첫 번째 4는 IP 버전이고, IHL의 단위가 되는 4바이트와는 서로 다른 의미다.

IHL은 헤더 길이를 바이트로 직접 쓰는 값이 아니라, **32비트(4바이트) 단위가 몇 개 있는지**를 표시한다. 그러므로 IHL이 5라면 `5 × 4 = 20바이트`다. 옵션이 없는 IPv4 헤더는 보통 이 기본 길이를 사용한다. 옵션이 있으면 헤더가 더 길어지고 IHL도 커진다. 헤더 길이를 4바이트 단위로 맞추기 위해 필요한 패딩이 붙을 수도 있다.

`0x45`를 읽는 순서를 다시 적으면 이렇다. 먼저 16진수 두 자리를 각각 4비트로 바꾸고, 앞 4비트에서 Version을, 뒤 4비트에서 IHL을 읽는다. 그다음 IHL에 4바이트를 곱해 헤더 길이를 구한다. 이 바이트 하나만 읽어도 “IPv4이며, 헤더는 기본 길이인 20바이트”라는 정보를 얻을 수 있다.

**Total Length**는 뒤에서 볼 또 다른 길이 값이다. IHL이 헤더 길이를 알려 준다면 Total Length는 헤더와 페이로드를 합친 IP 패킷 전체 길이를 알려 준다. 둘을 같은 값으로 착각하지 말자. 마지막 페이지의 Wireshark 예시에서 두 길이를 실제로 비교한다. 패킷이 링크에서 통과할 수 있는 MTU보다 크다면 전달 과정에서 단편화가 필요할 수 있지만, 그 판단과 조각을 처리하는 방법은 Unit 6 Lesson 1에서 배운다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Version은 IPv4를 표시하고 IHL은 헤더 길이를 32비트 단위로 나타낸다.
- **적용하기 (Apply):** 옵션 유무에 따라 IPv4 헤더 길이가 달라질 수 있음을 계산한다.
- **찾아보기 (Lookup):** IHL 값의 최소·최대 범위는 IPv4 형식표에서 찾아본다.

## Protocol과 TTL은 전달 중의 역할을 알려 준다

IP 패킷이 도착하면 수신 측은 먼저 IP 헤더를 읽는다. 그중 **Protocol** 필드는 IP 페이로드 안에 어떤 프로토콜의 데이터가 들어 있는지 알려 준다. 대표적인 값은 `6`이 TCP, `17`이 UDP, `1`이 ICMP다. IP는 이 값으로 안쪽 데이터를 다음에 어느 프로토콜이 해석해야 하는지 구분한다.

Protocol 번호와 **포트 번호**는 서로 다른 질문에 답한다. Protocol은 “IP 패킷 안쪽에 TCP·UDP·ICMP 중 무엇이 들어 있는가?”를 가리킨다. 포트는 TCP나 UDP가 선택된 다음 “그 호스트에서 어느 통신 끝점으로 전달할 것인가?”를 구분한다. 예를 들어 Protocol 값 6은 TCP 처리를 뜻하지만, 웹 서버의 포트 443을 뜻하지는 않는다. ICMP는 포트를 쓰지 않는 프로토콜이며, `ping` 같은 진단에서도 만난다. ICMP와 ping의 관계는 Unit 6 Lesson 4 「ping과 RTT」에서 살펴본다.

**TTL(Time To Live)**은 패킷이 길을 잘못 들어 네트워크를 계속 맴돌지 않도록 전달 범위를 제한한다. 이름만 보면 초 단위 시간처럼 느껴지지만, 여기서는 라우터를 지날 때 줄어드는 제한값으로 이해하면 된다. 한 번의 라우터 전달을 **홉(hop)**이라고 부르며, 라우터는 패킷을 다음 구간으로 넘길 때 TTL을 적어도 1 줄인다. 가령 TTL이 4인 패킷은 라우터를 지날 때 3, 2, 1로 줄어든다. 목적지에 닿기 전에 0이 되면 더 전달하지 않고 폐기한다.

TTL이 없다고 상상해 보자. 잘못된 경로 정보 때문에 패킷이 라우터 사이를 빙빙 돌면, 계속 네트워크 자원을 차지할 수 있다. TTL은 이런 패킷이 무한히 남지 않게 하는 안전장치다. TTL이 0이 된 사실을 보낸 쪽에 알리는 방식과 실제 라우팅 상황은 Unit 6 Lesson 1에서 이어서 다룬다.

첫 페이지의 헤더 그림에서 Protocol과 TTL의 위치를 다시 찾아보자. **Protocol은 안쪽 데이터의 해석 담당을, TTL은 전달 가능한 범위를 알려 준다.** 이 둘의 역할을 구분해 기억하면, 나머지 필드를 Wireshark에서 볼 때도 헤더가 단순한 숫자 나열이 아니라 전달을 위한 안내라는 점이 보인다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Protocol은 상위 프로토콜 종류, TTL은 전달 가능한 홉 제한을 나타낸다.
- **적용하기 (Apply):** Protocol 번호와 TTL 값을 구분해 패킷의 상위 데이터와 남은 전달 수를 읽는다.
- **찾아보기 (Lookup):** Protocol 번호 할당 목록은 IANA에서 조회한다.

## Wireshark에서 핵심 필드를 찾아본다

Wireshark는 네트워크 패킷을 캡처하고, 그 안의 바이트를 프로토콜 규칙에 따라 해석해 보여 주는 분석 프로그램이다. 캡처 목록에서 패킷 하나를 선택한 다음 세부 정보에서 **Internet Protocol Version 4** 항목을 펼쳐 보자. 한쪽에는 실제 16진수 바이트가, 다른 쪽에는 Wireshark가 읽어 낸 Version, Header Length, Protocol, TTL, 출발지·목적지 주소 같은 필드가 보인다. 실제 바이트가 원문이라면 해석된 필드 목록은 그 원문을 읽기 쉽게 풀어 쓴 결과다.

예시의 첫 바이트가 `45`, 다음 바이트가 `00`, 그다음 두 바이트가 `01 4B`라고 하자. `45`는 앞에서 본 대로 Version 4와 IHL 5다. IHL 5이므로 헤더는 20바이트다. `01 4B`는 **Total Length** 필드다. IPv4의 여러 바이트 값은 큰 자리부터 기록되므로 `0x014B`는 `1 × 256 + 4 × 16 + 11 = 331`이다. 즉 이 예시의 IP 패킷 전체는 331바이트다.

Total Length는 페이로드만의 크기가 아니다. IP 헤더 20바이트를 포함한 전체 길이다. 따라서 이 예시에서 IPv4 헤더 뒤의 IP 페이로드는 `331 - 20 = 311바이트`다. 이 311바이트 안에는 보통 TCP 헤더와 그 뒤의 데이터가 함께 들어 있다. 애플리케이션이 보낸 내용만 세는 값으로 혼동하지 말자. Total Length 필드는 16비트이므로 형식상 패킷 전체 길이를 최대 65,535바이트까지 나타낼 수 있다. 기본 헤더 20바이트를 빼면 이론상 IP 페이로드는 최대 65,515바이트다. 이는 IPv4 필드가 표현할 수 있는 크기이고, Ethernet MTU 1,500바이트 같은 실제 링크의 한도와는 다른 값이다.

계속해서 헤더의 TTL과 Protocol을 찾는다. 예시에서 TTL 바이트 `80`은 16진수이며 10진수로 128이다. Protocol 바이트 `06`은 TCP를 가리킨다. 출발지·목적지 주소는 각각 4바이트씩 읽는다. 예를 들어 바이트 `C0 A8 00 0A`는 네 부분을 10진수로 바꿔 `192.168.0.10`으로 표현한다. 이렇게 바이트와 풀이된 필드를 짝지으면 주소나 숫자를 무작정 외우지 않고 구조를 확인할 수 있다.

헤더 그림의 다른 필드도 살펴보자. **Identification, Flags, Fragment Offset**은 IPv4 패킷이 단편화될 때 조각들이 같은 원본에서 왔는지, 더 조각이 있는지, 원래 데이터의 어느 위치인지 확인하는 데 쓰인다. 여기서는 그 이름과 목적만 연결하고 계산·재조립 과정은 Unit 6 Lesson 1에 맡긴다. 예전에 Type of Service(TOS)라고 불리던 8비트 영역은 오늘날 DSCP와 ECN으로 나뉘어 서비스 처리와 혼잡 표시 등에 사용된다.

**Header Checksum**은 IPv4 헤더의 오류를 확인하는 검사값이다. 데이터 페이로드 전체의 무결성을 보장하거나 변조를 막는 보안 기능은 아니다. TTL처럼 전달 중 헤더 값이 바뀌면 헤더 체크섬도 다시 계산해야 한다. Wireshark에서 체크섬 검증이 비활성화되어 있다면 “오류가 없다고 확인됐다”는 뜻이 아니라, 해당 검사를 수행하지 않았다는 뜻이다.

이제 헤더 그림을 보며 필드 이름을 찾고, Wireshark에서는 실제 값과 맞춰 보자. **회상할 것은 헤더의 큰 역할, 적용할 것은 `0x45`와 Protocol·TTL 읽기, 필요할 때 찾아볼 것은 단편화 필드와 체크섬의 세부 규칙**이다. 다음 Lesson에서는 IP 주소 안에서 네트워크 부분과 호스트 부분을 어떻게 나누는지 배운다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Wireshark 패킷 세부 정보에서 Version·TTL·Protocol·주소를 찾는다.
- **적용하기 (Apply):** 캡처 한 건의 필드를 펼쳐 이름과 값을 직접 대응한다.
- **찾아보기 (Lookup):** Display filter 문법과 필드 전체 목록은 Wireshark 문서를 참조한다.
