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
  animations:
  - file: l22-dhcp-client-server.svg
    title: DHCP 서버가 비어 있는 네트워크 설정을 채운다
    alt: 네트워크 설정이 비어 있는 컴퓨터가 DHCP 서버에 요청하고, IP 주소·서브넷 마스크·게이트웨이·DNS 값이 채워집니다.
    caption: DHCP 클라이언트는 설정을 요청하고, 서버는 사용할 설정을 알려 줍니다.
    after_paragraph: 2
  questions:
  - id: u6-l02-p01-q01
    kind: choice
    difficulty: easy
    prompt: 새 기기가 네트워크에 연결될 때 DHCP가 주로 하는 일은 무엇인가요?
    choices:
    - id: a
      text: 통신에 필요한 네트워크 설정을 클라이언트에 알려 준다
      feedback: DHCP는 클라이언트가 네트워크에 참여하는 데 필요한 TCP/IP 설정을 받게 합니다.
    - id: b
      text: 웹 페이지를 자동으로 만든다
      feedback: DHCP가 자동으로 제공하는 것은 인터넷 자체가 아니라 통신 설정입니다.
    - id: c
      text: 모든 네트워크 장애를 해결한다
      feedback: DHCP가 자동으로 제공하는 것은 인터넷 자체가 아니라 통신 설정입니다.
    - id: d
      text: 라우터 없이 인터넷을 만든다
      feedback: DHCP가 자동으로 제공하는 것은 인터넷 자체가 아니라 통신 설정입니다.
    - id: e
      text: 모든 패킷을 암호화한다
      feedback: DHCP가 자동으로 제공하는 것은 인터넷 자체가 아니라 통신 설정입니다.
    answer: a
  - id: u6-l02-p01-q02
    kind: choice
    difficulty: medium
    prompt: “DHCP가 설정을 자동으로 받게 한다”는 설명의 의미로 가장 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 네트워크 회선과 웹 사이트가 저절로 생긴다
      feedback: 본문은 DHCP 설정과 인터넷 연결 성공을 같은 뜻으로 보지 않습니다.
    - id: c
      text: 모든 기기의 암호가 자동으로 바뀐다
      feedback: 본문은 DHCP 설정과 인터넷 연결 성공을 같은 뜻으로 보지 않습니다.
    - id: b
      text: 통신에 필요한 주소와 관련 설정을 받을 수 있다
      feedback: DHCP는 주소와 네트워크 설정을 전달하지만 회선이나 다른 장비의 동작까지 보장하지 않습니다.
    - id: d
      text: DNS가 필요 없어지는 것
      feedback: 본문은 DHCP 설정과 인터넷 연결 성공을 같은 뜻으로 보지 않습니다.
    - id: e
      text: 컴퓨터가 꺼져 있어도 서버가 된다
      feedback: 본문은 DHCP 설정과 인터넷 연결 성공을 같은 뜻으로 보지 않습니다.
    answer: b
  - id: u6-l02-p01-q03
    kind: choice
    difficulty: medium
    prompt: DHCP에서 설정을 받으려는 쪽과 설정을 제공하는 쪽은 무엇인가요?
    choices:
    - id: b
      text: 라우터와 프레임
      feedback: DHCP 메시지 교환에서 요청하는 쪽과 답하는 쪽을 나누어 보세요.
    - id: c
      text: DNS와 포트
      feedback: DHCP 메시지 교환에서 요청하는 쪽과 답하는 쪽을 나누어 보세요.
    - id: d
      text: 스위치와 케이블
      feedback: DHCP 메시지 교환에서 요청하는 쪽과 답하는 쪽을 나누어 보세요.
    - id: e
      text: 호스트와 MTU
      feedback: DHCP 메시지 교환에서 요청하는 쪽과 답하는 쪽을 나누어 보세요.
    - id: a
      text: 클라이언트와 서버
      feedback: 클라이언트가 설정을 요청하고 서버가 설정을 제공합니다.
    answer: a
  question_placements:
  - question_id: u6-l02-p01-q01
    after_paragraph: 2
- terms:
  - IP 주소(IP address)
  - 서브넷 마스크(Subnet mask)
  - 기본 게이트웨이(Default gateway)
  - DNS 서버(DNS server)
  - DHCP 옵션(DHCP option)
  questions:
  - id: u6-l02-p02-q01
    kind: choice
    difficulty: easy
    prompt: DHCP가 알려 주는 기본 게이트웨이는 어떤 일을 하나요?
    choices:
    - id: b
      text: 도메인 이름을 IP 주소로 바꾼다
      feedback: 게이트웨이와 DNS 서버가 맡는 일을 혼동하지 마세요.
    - id: c
      text: 같은 LAN의 모든 MAC 주소를 저장한다
      feedback: 게이트웨이와 DNS 서버가 맡는 일을 혼동하지 마세요.
    - id: a
      text: 다른 네트워크로 나갈 때 패킷을 맡길 첫 번째 라우터다
      feedback: 기본 게이트웨이는 다른 네트워크로 갈 때 패킷을 맡기는 첫 번째 라우터입니다.
    - id: d
      text: IP 주소의 네트워크 부분을 암호화한다
      feedback: 게이트웨이와 DNS 서버가 맡는 일을 혼동하지 마세요.
    - id: e
      text: 웹 페이지의 포트 번호를 고른다
      feedback: 게이트웨이와 DNS 서버가 맡는 일을 혼동하지 마세요.
    answer: a
  - id: u6-l02-p02-q02
    kind: choice
    difficulty: medium
    prompt: DNS 서버 주소가 필요한 이유는 무엇인가요?
    choices:
    - id: b
      text: 패킷의 TTL을 늘리기 위해
      feedback: 웹 이름을 IP 주소로 찾는 역할과 패킷 전달 역할을 구분하세요.
    - id: c
      text: DHCP 임대를 예약하기 위해
      feedback: 웹 이름을 IP 주소로 찾는 역할과 패킷 전달 역할을 구분하세요.
    - id: d
      text: Ethernet 링크 MTU를 바꾸기 위해
      feedback: 웹 이름을 IP 주소로 찾는 역할과 패킷 전달 역할을 구분하세요.
    - id: e
      text: IP 패킷을 재조립하기 위해
      feedback: 웹 이름을 IP 주소로 찾는 역할과 패킷 전달 역할을 구분하세요.
    - id: a
      text: 도메인 이름에 대응하는 IP 주소를 알아보기 위해
      feedback: DNS 서버는 도메인 이름에 대응하는 IP 주소를 알아볼 때 사용합니다.
    answer: a
  - id: u6-l02-p02-q03
    kind: choice
    difficulty: medium
    prompt: 서브넷 마스크는 어떤 구분에 도움을 주나요?
    choices:
    - id: b
      text: 어느 프로그램이 음악을 재생하는지
      feedback: 이 페이지에서 네트워크 주소와 호스트 주소 범위를 나누는 설정을 확인하세요.
    - id: a
      text: 어느 주소가 같은 네트워크에 있는지
      feedback: 서브넷 마스크는 주소가 같은 네트워크에 있는지 구분하는 데 도움을 줍니다.
    - id: c
      text: DHCP 서버가 물리적으로 어디 있는지
      feedback: 이 페이지에서 네트워크 주소와 호스트 주소 범위를 나누는 설정을 확인하세요.
    - id: d
      text: 패킷이 몇 초 동안 이동했는지
      feedback: 이 페이지에서 네트워크 주소와 호스트 주소 범위를 나누는 설정을 확인하세요.
    - id: e
      text: DNS 이름의 소유자
      feedback: 이 페이지에서 네트워크 주소와 호스트 주소 범위를 나누는 설정을 확인하세요.
    answer: a
  question_placements:
  - question_id: u6-l02-p02-q01
    after_paragraph: 1
- terms:
  - 주소 풀(Address pool)
  - 임대(Lease)
  - 동적 할당(Dynamic allocation)
  - 예약(Reservation)
  animations:
  - file: l22-dhcp-address-pool.svg
    title: DHCP 서버는 주소 풀에서 임시로 쓸 주소를 고른다
    alt: 서버의 주소 풀에서 192.168.0.100이 선택되어 게이트웨이, DNS, 서브넷 마스크와 함께 PC에 전달됩니다.
    caption: 서버는 관리하는 주소 풀에서 사용할 주소를 빌려 주고, 필요한 네트워크 설정도 함께 제공합니다.
    after_paragraph: 3
  questions:
  - id: u6-l02-p03-q01
    kind: choice
    difficulty: easy
    prompt: DHCP 주소 풀(Address pool)은 무엇인가요?
    choices:
    - id: b
      text: 클라이언트가 저장하는 웹 사이트 목록
      feedback: 예시의 시작 주소와 끝 주소가 서버에서 어떤 목록을 이루는지 떠올리세요.
    - id: c
      text: 라우터가 보내는 패킷의 모음
      feedback: 예시의 시작 주소와 끝 주소가 서버에서 어떤 목록을 이루는지 떠올리세요.
    - id: d
      text: DNS 서버의 사용자 계정
      feedback: 예시의 시작 주소와 끝 주소가 서버에서 어떤 목록을 이루는지 떠올리세요.
    - id: e
      text: Ethernet 프레임 크기 목록
      feedback: 예시의 시작 주소와 끝 주소가 서버에서 어떤 목록을 이루는지 떠올리세요.
    - id: a
      text: DHCP 서버가 배정할 수 있도록 관리하는 주소 범위
      feedback: 주소 풀은 서버가 배정할 수 있도록 관리하는 주소들의 범위입니다.
    answer: a
  - id: u6-l02-p03-q02
    kind: choice
    difficulty: medium
    prompt: DHCP 임대(Lease)에 대한 설명으로 맞는 것은 무엇인가요?
    choices:
    - id: b
      text: 주소를 영구 소유하게 만드는 것
      feedback: 동적 할당이어도 주소가 매번 반드시 바뀌지는 않습니다.
    - id: a
      text: 정해진 기간 동안 주소를 사용할 수 있도록 허용하는 것
      feedback: 임대는 주소를 일정 기간 사용할 수 있도록 허용하며 갱신될 수 있습니다.
    - id: c
      text: 매번 컴퓨터를 켤 때 주소가 반드시 바뀌는 것
      feedback: 동적 할당이어도 주소가 매번 반드시 바뀌지는 않습니다.
    - id: d
      text: 라우터가 TTL을 정하는 것
      feedback: 동적 할당이어도 주소가 매번 반드시 바뀌지는 않습니다.
    - id: e
      text: DNS 이름을 새로 만드는 것
      feedback: 동적 할당이어도 주소가 매번 반드시 바뀌지는 않습니다.
    answer: a
  - id: u6-l02-p03-q03
    kind: choice
    difficulty: medium
    prompt: 특정 장치가 계속 같은 주소를 받도록 DHCP 서버에 설정하는 방법은 무엇인가요?
    choices:
    - id: b
      text: 단편화
      feedback: 예약도 장치가 DHCP를 통해 설정을 받는 방식입니다.
    - id: c
      text: 라우팅 루프
      feedback: 예약도 장치가 DHCP를 통해 설정을 받는 방식입니다.
    - id: d
      text: 기본 경로
      feedback: 예약도 장치가 DHCP를 통해 설정을 받는 방식입니다.
    - id: a
      text: DHCP 예약
      feedback: DHCP 예약을 사용하면 특정 장치에 같은 주소를 계속 제공할 수 있습니다.
    - id: e
      text: 링크 로컬 주소
      feedback: 예약도 장치가 DHCP를 통해 설정을 받는 방식입니다.
    answer: a
  question_placements:
  - question_id: u6-l02-p03-q01
    after_paragraph: 1
- terms:
  - DHCP Discover
  - 브로드캐스트(Broadcast)
  - 브로드캐스트 도메인(Broadcast domain)
  - 0.0.0.0
  - 255.255.255.255
  animations:
  - file: l22-dhcp-discover-broadcast.svg
    title: 서버 주소를 모를 때 Discover를 같은 범위에 방송한다
    alt: IP 주소가 아직 없는 PC가 보낸 DHCP Discover가 스위치를 통해 같은 브로드캐스트 범위로 퍼지고, DHCP 서버가 응답을 준비합니다.
    caption: DHCP 서버 주소를 모르는 클라이언트는 Discover를 브로드캐스트해 같은 범위의 서버를 찾습니다.
    after_paragraph: 2
  questions:
  - id: u6-l02-p04-q01
    kind: choice
    difficulty: easy
    prompt: DHCP 서버 주소를 아직 모르는 새 클라이언트가 처음 서버를 찾을 때 보내는 메시지는 무엇인가요?
    choices:
    - id: b
      text: DHCP ACK
      feedback: 서버 주소를 모르는 상태에서 시작하는 DHCP 메시지를 찾으세요.
    - id: a
      text: DHCP Discover
      feedback: 클라이언트는 DHCP Discover를 보내 서버를 찾기 시작합니다.
    - id: c
      text: DNS Reply
      feedback: 서버 주소를 모르는 상태에서 시작하는 DHCP 메시지를 찾으세요.
    - id: d
      text: TCP ACK
      feedback: 서버 주소를 모르는 상태에서 시작하는 DHCP 메시지를 찾으세요.
    - id: e
      text: ARP Reply
      feedback: 서버 주소를 모르는 상태에서 시작하는 DHCP 메시지를 찾으세요.
    answer: a
  - id: u6-l02-p04-q02
    kind: choice
    difficulty: medium
    prompt: 아직 IPv4 주소를 받지 못한 DHCP 클라이언트가 Discover를 보낼 때 사용할 수 있는 출발지 IP는 무엇인가요?
    choices:
    - id: b
      text: 127.0.0.1
      feedback: 본문에서 출발지 IP와 브로드캐스트 목적지 IP를 따로 확인하세요.
    - id: c
      text: 255.255.255.255
      feedback: 본문에서 출발지 IP와 브로드캐스트 목적지 IP를 따로 확인하세요.
    - id: d
      text: 192.168.0.1
      feedback: 본문에서 출발지 IP와 브로드캐스트 목적지 IP를 따로 확인하세요.
    - id: a
      text: 0.0.0.0
      feedback: 주소를 아직 받지 못한 클라이언트는 출발지 IP에 0.0.0.0을 쓸 수 있습니다.
    - id: e
      text: 224.0.0.1
      feedback: 본문에서 출발지 IP와 브로드캐스트 목적지 IP를 따로 확인하세요.
    answer: a
  - id: u6-l02-p04-q03
    kind: choice
    difficulty: medium
    prompt: DHCP Discover가 브로드캐스트로 전송되는 이유는 무엇인가요?
    choices:
    - id: a
      text: 클라이언트가 DHCP 서버 주소를 아직 모르기 때문
      feedback: 서버 주소를 모르는 클라이언트는 같은 범위의 서버를 찾도록 브로드캐스트할 수 있습니다.
    - id: b
      text: 클라이언트가 모든 인터넷 기기에서 답을 받아야 하기 때문
      feedback: 브로드캐스트 범위와 인터넷 전체를 같은 범위로 생각하지 마세요.
    - id: c
      text: DHCP 서버가 항상 원격지에 있기 때문
      feedback: 브로드캐스트 범위와 인터넷 전체를 같은 범위로 생각하지 마세요.
    - id: d
      text: 브로드캐스트는 라우터를 반드시 통과하기 때문
      feedback: 브로드캐스트 범위와 인터넷 전체를 같은 범위로 생각하지 마세요.
    - id: e
      text: IP 주소가 이미 확정되었기 때문
      feedback: 브로드캐스트 범위와 인터넷 전체를 같은 범위로 생각하지 마세요.
    answer: a
  question_placements:
  - question_id: u6-l02-p04-q01
    after_paragraph: 1
- terms:
  - DORA
  - DHCP Offer
  - DHCP Request
  - DHCP ACK
  - UDP(User Datagram Protocol)
  questions:
  - id: u6-l02-p05-q01
    kind: choice
    difficulty: easy
    prompt: 새 IP 주소를 받는 대표 DHCP 메시지 순서는 무엇인가요?
    choices:
    - id: b
      text: Offer → ACK → Discover → Request
      feedback: 클라이언트의 발견과 요청, 서버의 제안과 확인 순서를 본문 표와 맞춰 보세요.
    - id: c
      text: Request → Discover → ACK → Offer
      feedback: 클라이언트의 발견과 요청, 서버의 제안과 확인 순서를 본문 표와 맞춰 보세요.
    - id: d
      text: ACK → Discover → Offer → Request
      feedback: 클라이언트의 발견과 요청, 서버의 제안과 확인 순서를 본문 표와 맞춰 보세요.
    - id: a
      text: Discover → Offer → Request → ACK
      feedback: 대표적인 DHCP 새 주소 할당 흐름은 Discover, Offer, Request, ACK 순서입니다.
    - id: e
      text: Discover → Request → Offer → ACK
      feedback: 클라이언트의 발견과 요청, 서버의 제안과 확인 순서를 본문 표와 맞춰 보세요.
    answer: a
  - id: u6-l02-p05-q02
    kind: choice
    difficulty: medium
    prompt: DHCP Offer 다음에 클라이언트가 보내는 메시지는 무엇인가요?
    choices:
    - id: a
      text: DHCP Request
      feedback: 클라이언트는 사용할 제안을 선택해 DHCP Request를 보냅니다.
    - id: b
      text: DHCP Discover
      feedback: Offer는 서버의 제안이고, 그 제안을 선택하는 클라이언트 메시지를 찾으세요.
    - id: c
      text: DHCP ACK
      feedback: Offer는 서버의 제안이고, 그 제안을 선택하는 클라이언트 메시지를 찾으세요.
    - id: d
      text: ICMP Time Exceeded
      feedback: Offer는 서버의 제안이고, 그 제안을 선택하는 클라이언트 메시지를 찾으세요.
    - id: e
      text: ARP Reply
      feedback: Offer는 서버의 제안이고, 그 제안을 선택하는 클라이언트 메시지를 찾으세요.
    answer: a
  - id: u6-l02-p05-q03
    kind: choice
    difficulty: medium
    prompt: DHCP ACK는 이 Lesson에서 어떤 의미인가요?
    choices:
    - id: b
      text: TCP가 연결 종료를 알리는 메시지
      feedback: 이름이 같아도 DHCP ACK와 TCP ACK를 같은 메시지로 보지 마세요.
    - id: c
      text: DNS가 이름을 해석하는 메시지
      feedback: 이름이 같아도 DHCP ACK와 TCP ACK를 같은 메시지로 보지 마세요.
    - id: a
      text: 서버가 DHCP 요청을 확인하고 설정 임대를 시작하라고 알리는 메시지
      feedback: DHCP ACK는 DHCP 요청을 확인하는 메시지이며 TCP ACK와는 다른 프로토콜의 메시지입니다.
    - id: d
      text: 라우터가 TTL 만료를 알리는 메시지
      feedback: 이름이 같아도 DHCP ACK와 TCP ACK를 같은 메시지로 보지 마세요.
    - id: e
      text: 클라이언트가 처음 서버를 찾는 메시지
      feedback: 이름이 같아도 DHCP ACK와 TCP ACK를 같은 메시지로 보지 마세요.
    answer: a
  question_placements:
  - question_id: u6-l02-p05-q01
    after_paragraph: 1
- terms:
  - DHCP 릴레이(DHCP relay)
  - IP 주소 충돌(IP address conflict)
  - 링크 로컬 주소(Link-local address)
  questions:
  - id: u6-l02-p06-q01
    kind: choice
    difficulty: easy
    prompt: DHCP 서버와 클라이언트가 서로 다른 서브넷에 있을 때 필요한 기능은 무엇인가요?
    choices:
    - id: a
      text: DHCP 릴레이
      feedback: 다른 서브넷의 서버를 쓰려면 요청을 전달할 DHCP 릴레이가 필요할 수 있습니다.
    - id: b
      text: DHCP 예약
      feedback: 브로드캐스트가 라우터를 넘어가지 않는 상황을 떠올리세요.
    - id: c
      text: IP 단편화
      feedback: 브로드캐스트가 라우터를 넘어가지 않는 상황을 떠올리세요.
    - id: d
      text: DNS 캐시
      feedback: 브로드캐스트가 라우터를 넘어가지 않는 상황을 떠올리세요.
    - id: e
      text: 루프백
      feedback: 브로드캐스트가 라우터를 넘어가지 않는 상황을 떠올리세요.
    answer: a
  - id: u6-l02-p06-q02
    kind: choice
    difficulty: medium
    prompt: DHCP 릴레이는 어떤 일을 하나요?
    choices:
    - id: b
      text: IP 주소를 영구 소유권으로 바꾼다
      feedback: 릴레이는 브로드캐스트를 인터넷 전체로 보내는 기능이 아닙니다.
    - id: c
      text: DNS 이름을 웹 페이지로 바꾼다
      feedback: 릴레이는 브로드캐스트를 인터넷 전체로 보내는 기능이 아닙니다.
    - id: a
      text: 클라이언트의 브로드캐스트 요청을 설정된 서버로 전달하고 응답을 되돌린다
      feedback: 릴레이는 클라이언트의 요청과 서버의 응답이 다른 서브넷 사이를 오가도록 전달합니다.
    - id: d
      text: 모든 브로드캐스트를 인터넷에 전달한다
      feedback: 릴레이는 브로드캐스트를 인터넷 전체로 보내는 기능이 아닙니다.
    - id: e
      text: 각 패킷의 TTL을 원래 값으로 만든다
      feedback: 릴레이는 브로드캐스트를 인터넷 전체로 보내는 기능이 아닙니다.
    answer: a
  - id: u6-l02-p06-q03
    kind: choice
    difficulty: medium
    prompt: DHCP 서버가 다른 네트워크에 있는데 릴레이가 없다면 어떤 일이 생길 수 있나요?
    choices:
    - id: b
      text: 클라이언트가 자동으로 서버 주소를 알아낸다
      feedback: 다른 서브넷에서 중앙 DHCP 서버를 쓰려면 어떤 연결 역할이 필요한지 생각하세요.
    - id: c
      text: DHCP Discover가 모든 라우터를 통과한다
      feedback: 다른 서브넷에서 중앙 DHCP 서버를 쓰려면 어떤 연결 역할이 필요한지 생각하세요.
    - id: d
      text: 임대가 영구 주소로 바뀐다
      feedback: 다른 서브넷에서 중앙 DHCP 서버를 쓰려면 어떤 연결 역할이 필요한지 생각하세요.
    - id: e
      text: 서브넷 마스크가 DNS 서버가 된다
      feedback: 다른 서브넷에서 중앙 DHCP 서버를 쓰려면 어떤 연결 역할이 필요한지 생각하세요.
    - id: a
      text: 클라이언트 Discover가 라우터를 넘어 서버까지 저절로 전달되지 않는다
      feedback: 라우터는 기본적으로 브로드캐스트를 다른 네트워크로 그대로 전달하지 않습니다.
    answer: a
  question_placements:
  - question_id: u6-l02-p06-q01
    after_paragraph: 1
- terms:
  - DHCP 서버 주소(DHCP server address)
  - 임대 기간(Lease time)
  - "`ipconfig /all`"
  - "`ipconfig getpacket`"
  - "`nmcli`"
  questions:
  - id: u6-l02-p07-q01
    kind: choice
    difficulty: easy
    prompt: 여러 네트워크 어댑터가 있는 컴퓨터에서 DHCP 설정을 확인할 때 먼저 할 일은 무엇인가요?
    choices:
    - id: b
      text: 모든 어댑터의 설정이 같다고 가정한다
      feedback: 본문에서 명령 출력 해석 전에 확인하라고 한 대상을 찾아보세요.
    - id: c
      text: 브라우저 캐시를 지운다
      feedback: 본문에서 명령 출력 해석 전에 확인하라고 한 대상을 찾아보세요.
    - id: a
      text: 실제로 연결해 쓰는 어댑터를 찾는다
      feedback: Wi-Fi, Ethernet, 가상 어댑터는 각기 다른 설정을 가질 수 있어 사용 중인 어댑터를 확인해야 합니다.
    - id: d
      text: TTL을 255로 바꾼다
      feedback: 본문에서 명령 출력 해석 전에 확인하라고 한 대상을 찾아보세요.
    - id: e
      text: 웹 서버를 설치한다
      feedback: 본문에서 명령 출력 해석 전에 확인하라고 한 대상을 찾아보세요.
    answer: a
  - id: u6-l02-p07-q02
    kind: choice
    difficulty: medium
    prompt: Windows에서 DHCP와 주소 등 상세 네트워크 정보를 보는 명령은 무엇인가요?
    choices:
    - id: b
      text: ping 127.0.0.1
      feedback: Windows 명령과 macOS 또는 Linux에서 소개한 명령을 구분하세요.
    - id: c
      text: route print
      feedback: Windows 명령과 macOS 또는 Linux에서 소개한 명령을 구분하세요.
    - id: d
      text: nslookup localhost
      feedback: Windows 명령과 macOS 또는 Linux에서 소개한 명령을 구분하세요.
    - id: e
      text: arp -d
      feedback: Windows 명령과 macOS 또는 Linux에서 소개한 명령을 구분하세요.
    - id: a
      text: ipconfig /all
      feedback: Windows 명령 프롬프트에서 ipconfig /all로 상세 어댑터 설정을 확인할 수 있습니다.
    answer: a
  - id: u6-l02-p07-q03
    kind: choice
    difficulty: medium
    prompt: Linux에서 기본 게이트웨이 정보를 확인할 때 본문에서 안내한 명령은 무엇인가요?
    choices:
    - id: b
      text: ipconfig /all
      feedback: 주소 확인 명령과 경로 정보를 확인하는 명령을 구분하세요.
    - id: a
      text: ip route
      feedback: Linux에서는 ip route 출력의 default via에서 기본 게이트웨이를 확인할 수 있습니다.
    - id: c
      text: ping -c 4 127.0.0.1
      feedback: 주소 확인 명령과 경로 정보를 확인하는 명령을 구분하세요.
    - id: d
      text: dhcp offer
      feedback: 주소 확인 명령과 경로 정보를 확인하는 명령을 구분하세요.
    - id: e
      text: route add
      feedback: 주소 확인 명령과 경로 정보를 확인하는 명령을 구분하세요.
    answer: a
  question_placements:
  - question_id: u6-l02-p07-q01
    after_paragraph: 1
- terms:
  - DHCP 자동 구성
  - 브로드캐스트 전달
  - IP 주소 갱신
  questions:
  - id: u6-l02-p08-q01
    kind: choice
    difficulty: easy
    prompt: DHCP에서 주소를 받았다는 사실만으로 인터넷이 반드시 된다고 할 수 없는 이유는 무엇인가요?
    choices:
    - id: b
      text: DHCP는 IP 주소를 주지 않기 때문
      feedback: “IP 주소를 받았다”와 “전체 통신이 성공했다”를 구분하세요.
    - id: c
      text: DHCP가 웹 브라우저를 막기 때문
      feedback: “IP 주소를 받았다”와 “전체 통신이 성공했다”를 구분하세요.
    - id: d
      text: 모든 DHCP 주소는 루프백이기 때문
      feedback: “IP 주소를 받았다”와 “전체 통신이 성공했다”를 구분하세요.
    - id: e
      text: IP 패킷에는 목적지가 없기 때문
      feedback: “IP 주소를 받았다”와 “전체 통신이 성공했다”를 구분하세요.
    - id: a
      text: 게이트웨이, DNS, Wi-Fi 등 다른 부분도 동작해야 하기 때문
      feedback: DHCP 설정을 받는 것은 출발점이며 다른 네트워크 요소도 동작해야 인터넷을 쓸 수 있습니다.
    answer: a
  - id: u6-l02-p08-q02
    kind: choice
    difficulty: medium
    prompt: 같은 LAN에서 목적지 IP에 대응하는 MAC 주소를 찾는 일은 무엇이 맡나요?
    choices:
    - id: b
      text: DHCP
      feedback: DHCP가 설정을 주는 일과 ARP가 다음 전달 대상을 찾는 일을 구분하세요.
    - id: a
      text: ARP
      feedback: ARP는 같은 LAN에서 목적지 IP에 대응하는 MAC 주소를 찾는 일을 맡습니다.
    - id: c
      text: DNS
      feedback: DHCP가 설정을 주는 일과 ARP가 다음 전달 대상을 찾는 일을 구분하세요.
    - id: d
      text: TTL
      feedback: DHCP가 설정을 주는 일과 ARP가 다음 전달 대상을 찾는 일을 구분하세요.
    - id: e
      text: MTU
      feedback: DHCP가 설정을 주는 일과 ARP가 다음 전달 대상을 찾는 일을 구분하세요.
    answer: a
  - id: u6-l02-p08-q03
    kind: choice
    difficulty: medium
    prompt: DHCP 서버에서 주소를 받지 못했을 때 보일 수 있는 169.254.x.x 주소에 대한 설명으로 맞는 것은 무엇인가요?
    choices:
    - id: b
      text: 인터넷 전체에서 쓰는 공인 주소다
      feedback: 링크 로컬 주소가 있다고 해서 인터넷 접속이 된다고 단정하지 마세요.
    - id: c
      text: 항상 기본 게이트웨이 주소다
      feedback: 링크 로컬 주소가 있다고 해서 인터넷 접속이 된다고 단정하지 마세요.
    - id: d
      text: DHCP Offer 메시지의 이름이다
      feedback: 링크 로컬 주소가 있다고 해서 인터넷 접속이 된다고 단정하지 마세요.
    - id: a
      text: 운영체제가 설정할 수 있는 링크 로컬 주소이며 DHCP 서버가 준 주소는 아니다
      feedback: 일부 운영체제는 DHCP 실패 시 링크 로컬 주소를 설정할 수 있으며, 이는 DHCP 서버가 준 주소가 아닙니다.
    - id: e
      text: 127.0.0.1과 같은 루프백 주소다
      feedback: 링크 로컬 주소가 있다고 해서 인터넷 접속이 된다고 단정하지 마세요.
    answer: a
  question_placements:
  - question_id: u6-l02-p08-q01
    after_paragraph: 1
animations_dir: units/04-layer3-addressing/lessons/12-인터넷-설정-자동화를-위한-dhcp/assets/animations
---

## 네트워크에 연결하면 설정은 어디서 올까?

새 노트북을 집 Wi-Fi에 연결했다고 하자. 인터넷을 쓰려면 노트북에는 IP 주소뿐 아니라 서브넷 마스크, 기본 게이트웨이, DNS 서버 같은 정보도 필요하다. 이 값을 사용자가 매번 직접 입력해야 한다면 기기를 바꾸거나 다른 네트워크로 이동할 때마다 설정을 다시 해야 한다. 네트워크는 어떻게 이 일을 자동으로 해 줄까?

그 역할을 하는 프로토콜이 **DHCP(Dynamic Host Configuration Protocol)**다. DHCP는 클라이언트가 네트워크에 참여할 때 사용할 TCP/IP 설정을 서버에서 받아오게 한다. 이번 Lesson에서는 DHCP가 알려 주는 값, 주소가 임대되는 방식, 서버를 찾는 브로드캐스트, 그리고 실제 컴퓨터에서 받은 값을 확인하는 순서로 살펴본다.

여기서 말하는 ‘자동’은 인터넷 자체가 자동으로 생긴다는 뜻이 아니다. DHCP가 네트워크 통신에 필요한 설정을 알려 주는 것이다. 그 설정이 올바르고 네트워크 회선도 동작해야 인터넷에 연결된다.

## DHCP 서버는 컴퓨터가 쓸 네트워크 설정을 알려 준다
<!-- learn-page-id: dhcp-role -->

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
