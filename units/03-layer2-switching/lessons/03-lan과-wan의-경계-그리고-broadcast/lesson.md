---
id: u3-l10-lan과-wan의-경계-그리고-broadcast
title: LAN과 WAN의 경계 그리고 Broadcast
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-10.md
wiki_diagram: units/03-layer2-switching/lessons/03-lan과-wan의-경계-그리고-broadcast/assets/diagrams/lesson-10.svg
page_metadata:
- terms:
  - 유니캐스트 (Unicast)
  - 브로드캐스트 (Broadcast)
  questions:
  - id: u3-03-p01-q01
    kind: choice
    difficulty: easy
    prompt: 한 장치가 특정 수신자 한 곳을 지정해 보내는 통신 방식은 무엇인가요?
    choices:
    - id: a
      text: Jumbo Frame
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Link up
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Virtualization
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: Unicast
      feedback: 맞아요. Unicast.
    - id: e
      text: Broadcast
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p01-q02
    kind: choice
    difficulty: medium
    prompt: Broadcast에서 “모두”가 가리키는 범위는 무엇인가요?
    choices:
    - id: a
      text: 같은 제조사의 컴퓨터만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 전 세계 인터넷에 연결된 모든 장치
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 같은 스위치에 직접 꽂힌 PC만 항상
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 같은 브로드캐스트 도메인에 속한 장치들
      feedback: 맞아요. 같은 브로드캐스트 도메인에 속한 장치들.
    - id: e
      text: 같은 IP 주소를 쓰는 장치만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p01-q03
    kind: short
    prompt: 같은 네트워크 범위 안의 모든 장치에게 전달되는 통신 방식입니다. 영어로 답해주세요.
    answers:
    - Broadcast
    feedback: 정답은 Broadcast입니다.
  - id: u3-03-p01-q04
    kind: choice
    difficulty: medium
    prompt: "교실 전체 안내 방송처럼 같은 구역의 여러 장치에 한꺼번에 보내는 통신은 무엇인가요?"
    choices:
    - id: a
      text: "Broadcast"
      feedback: "맞아요. Broadcast입니다."
    - id: b
      text: "Unicast"
      feedback: "다시 본문을 확인해 보세요. Unicast."
    - id: c
      text: "Uplink"
      feedback: "다시 본문을 확인해 보세요. Uplink."
    - id: d
      text: "Link up"
      feedback: "다시 본문을 확인해 보세요. Link up."
    - id: e
      text: "Routing"
      feedback: "다시 본문을 확인해 보세요. Routing."
    answer: a
  animations:
  - file: l10-unicast-vs-broadcast.svg
    title: "Unicast와 Broadcast"
    alt: "PC 1이 점선 구역 안의 PC 2~5와 연결되어 있습니다. 먼저 파란 Unicast가 PC 4 한 대에만 가고, 이어서 주황 Broadcast가 구역 안 네 대에 한꺼번에 퍼진 뒤 네 대 모두 내용 확인 표시가 켜집니다. 마지막에 구역이 브로드캐스트 도메인으로 표시되고, 구역 밖 PC에는 닿지 않는다는 문구가 나옵니다."
    caption: "Unicast는 한 곳을 지정해 보내고, Broadcast는 같은 브로드캐스트 도메인 안의 모두에게 보냅니다. 받은 장치는 모두 내용을 확인해야 합니다."
- terms:
  - 브로드캐스트 도메인 (Broadcast Domain)
  - LAN 구역
  questions:
  - id: u3-03-p02-q01
    kind: choice
    difficulty: easy
    prompt: 브로드캐스트 범위를 미리 살펴야 하는 이유는 무엇인가요?
    choices:
    - id: a
      text: MAC 주소의 앞부분에서 제조사를 항상 확인하기 때문
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 프레임 크기를 자동으로 줄이기 때문
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 그 범위 안의 장치들이 방송을 받아 내용을 확인하기 때문
      feedback: 맞아요. 그 범위 안의 장치들이 방송을 받아 내용을 확인하기 때문.
    - id: d
      text: 각 링크의 속도가 동일해지기 때문
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 방송이 전 세계 모든 인터넷 장치에 전달되기 때문
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-03-p02-q02
    kind: choice
    difficulty: medium
    prompt: Ethernet 브로드캐스트를 받는 장치의 범위를 설명하는 것은 무엇인가요?
    choices:
    - id: a
      text: 브로드캐스트 도메인의 크기와 경계
      feedback: 맞아요. 브로드캐스트 도메인의 크기와 경계.
    - id: b
      text: 인터넷 회선의 속도만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Wi-Fi 신호가 닿는 거리와 항상 동일한 범위
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: MAC 주소의 제조사 정보
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 프레임 안의 데이터 크기만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-03-p02-q03
    kind: short
    prompt: 브로드캐스트 프레임을 받아 확인하게 되는 네트워크 구역의 이름은 무엇인가요? (영어로 답해주세요)
    answers:
    - broadcast domain
    feedback: 정답은 broadcast domain입니다.
  - id: u3-03-p02-q04
    kind: choice
    difficulty: medium
    prompt: "브로드캐스트 도메인을 가장 잘 설명한 것은 무엇인가요?"
    choices:
    - id: a
      text: "인터넷 전체의 모든 장치"
      feedback: "다시 본문을 확인해 보세요. 인터넷 전체의 모든 장치."
    - id: b
      text: "한 서버에서 실행되는 프로그램 수"
      feedback: "다시 본문을 확인해 보세요. 한 서버에서 실행되는 프로그램 수."
    - id: c
      text: "Ethernet 브로드캐스트 프레임이 전달되어 장치들이 수신하는 범위"
      feedback: "맞아요. Ethernet 브로드캐스트 프레임이 전달되어 장치들이 수신하는 범위입니다."
    - id: d
      text: "무선 신호의 속도 구간"
      feedback: "다시 본문을 확인해 보세요. 무선 신호의 속도 구간."
    - id: e
      text: "MAC 주소를 만드는 회사들의 목록"
      feedback: "다시 본문을 확인해 보세요. MAC 주소를 만드는 회사들의 목록."
    answer: c
  animations:
  - file: l10-apartment-broadcast-zone.svg
    title: "방송이 닿는 구역"
    alt: "왼쪽 아파트에서 관리실이 방송하자 연결된 여덟 세대가 모두 켜지고, 이어서 구역이 둘로 나뉘어 구역 1의 세대만 방송을 듣습니다. 오른쪽에서는 PC 1의 방송을 받은 스위치가 PC 2~4로 전달해 모두 확인하고, 그 범위가 브로드캐스트 도메인으로 묶여 표시됩니다."
    caption: "방송이 닿는 구역을 브로드캐스트 도메인이라고 합니다. 방송을 보낼 수 있는지만큼 어느 구역까지 들리게 할지가 중요합니다."
- terms:
  - 16진수 (Hexadecimal)
  - 브로드캐스트 MAC 주소
  animations:
  - file: l10-broadcast-mac-all-ones.svg
    title: 전구 48개가 모두 켜진 주소는 ‘모두에게’
    alt: 전구 8개가 모두 켜져 FF가 되고, 이것이 여섯 칸 이어져 FF:FF:FF:FF:FF:FF가 되어 봉투의 받는 사람 칸에 들어가는
      장면입니다.
    caption: FF는 켜진 전구 8개이고, 6칸이 모두 FF인 MAC 주소는 브로드캐스트를 뜻합니다.
  questions:
  - id: u3-03-p03-q01
    kind: choice
    difficulty: easy
    prompt: 16진수 F 한 글자를 4비트 이진수로 쓰면 무엇인가요?
    choices:
    - id: a
      text: FF:00:00:00:00:00
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 10.0.0.255
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 00:00:00:00:00:00
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: '1111'
      feedback: 맞아요. 1111.
    - id: e
      text: AA:BB:CC:11:22:33
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p03-q02
    kind: choice
    difficulty: medium
    prompt: FF:FF:FF:FF:FF:FF가 48비트 모두 1을 나타내는 이유는 무엇인가요?
    choices:
    - id: a
      text: FF 쌍이 1비트씩 여섯 번 나타난다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 콜론이 네트워크 범위를 나타내기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: F 하나가 48비트를 뜻한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 16진수 F 하나가 4개의 1이고 여섯 쌍이 48비트를 채운다
      feedback: 맞아요. 16진수 F 하나가 4개의 1이고 여섯 쌍이 48비트를 채운다.
    - id: e
      text: 각 16진수 칸은 8비트여서 모두 6비트다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p03-q03
    kind: short
    prompt: Ethernet 프레임에서 같은 브로드캐스트 구역 모두를 수신자로 지정하는 목적지 주소입니다. 영어로 답해주세요.
    answers:
    - broadcast MAC address
    feedback: 정답은 broadcast MAC address입니다.
  - id: u3-03-p03-q04
    kind: choice
    difficulty: medium
    prompt: "FF:FF:FF:FF:FF:FF가 Ethernet 브로드캐스트 MAC 주소인 이유는 무엇인가요?"
    choices:
    - id: a
      text: "IP 주소가 모두 255이기 때문이다"
      feedback: "다시 본문을 확인해 보세요. IP 주소가 모두 255이기 때문이다."
    - id: b
      text: "문자 F가 네트워크 장치를 뜻하기 때문이다"
      feedback: "다시 본문을 확인해 보세요. 문자 F가 네트워크 장치를 뜻하기 때문이다."
    - id: c
      text: "라우터가 모든 MAC 주소를 그 값으로 바꾸기 때문이다"
      feedback: "다시 본문을 확인해 보세요. 라우터가 모든 MAC 주소를 그 값으로 바꾸기 때문이다."
    - id: d
      text: "6개의 네트워크에 각각 하나씩 보내기 때문이다"
      feedback: "다시 본문을 확인해 보세요. 6개의 네트워크에 각각 하나씩 보내기 때문이다."
    - id: e
      text: "6바이트의 각 비트가 모두 1인 48비트 주소이기 때문이다"
      feedback: "맞아요. 6바이트의 각 비트가 모두 1인 48비트 주소이기 때문이다입니다."
    answer: e
- terms:
  - 프레임 (Frame)
  - 헤더 (Header)
  - 배포 스위치 (Distribution Switch)
  animations:
  - file: l10-broadcast-flood-switches.svg
    title: 방송 프레임은 스위치마다 갈라져 퍼진다
    alt: PC 1이 방송 프레임을 보내자 스위치 A, 배포 스위치 C, 스위치 B를 거쳐 모든 PC로 프레임이 복사되어 퍼지는 장면입니다.
    caption: 받는 곳이 FF:FF:FF:FF:FF:FF인 프레임은 스위치를 지날 때마다 여러 갈래로 복사됩니다.
  questions:
  - id: u3-03-p04-q01
    kind: choice
    difficulty: easy
    prompt: Ethernet 프레임 헤더에 들어가는 주소 정보 두 가지는 무엇인가요?
    choices:
    - id: a
      text: 호스트 이름과 Metric
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 출발지 IP와 목적지 URL
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 네트워크 속도와 프레임 크기
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 출발지 MAC 주소와 목적지 MAC 주소
      feedback: 맞아요. 출발지 MAC 주소와 목적지 MAC 주소.
    - id: e
      text: 전원 상태와 포트 LED 색
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p04-q02
    kind: choice
    difficulty: medium
    prompt: 브로드캐스트 프레임이 액세스 스위치에 들어왔을 때 스위치가 퍼뜨리는 방식은 무엇인가요?
    choices:
    - id: a
      text: 스위치가 프레임 내용을 새로 만들어 낸다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: L3 경계를 넘어 모든 IP 네트워크로 자동 전달한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 들어온 포트를 제외한 여러 연결 방향으로 전달한다
      feedback: 맞아요. 들어온 포트를 제외한 여러 연결 방향으로 전달한다.
    - id: d
      text: 받은 포트 하나로만 되돌려 보낸다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 목적지 MAC을 바꿔 PC 한 대에만 보낸다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-03-p04-q03
    kind: short
    prompt: Ethernet 프레임의 앞부분에서 출발지·목적지 주소 같은 전달 정보를 담는 부분입니다. 무엇일까요? (영어로 답해주세요)
    answers:
    - header
    feedback: 정답은 header입니다.
  - id: u3-03-p04-q04
    kind: choice
    difficulty: medium
    prompt: "스위치가 Ethernet 브로드캐스트 프레임을 받았을 때 일반적인 전달 방식은 무엇인가요?"
    choices:
    - id: a
      text: "들어온 포트로만 되돌려 보낸다"
      feedback: "다시 본문을 확인해 보세요. 들어온 포트로만 되돌려 보낸다."
    - id: b
      text: "들어온 포트를 제외한 같은 브로드캐스트 도메인의 포트로 전달한다"
      feedback: "맞아요. 들어온 포트를 제외한 같은 브로드캐스트 도메인의 포트로 전달한다입니다."
    - id: c
      text: "MAC 주소 테이블에 있는 한 포트에만 보낸다"
      feedback: "다시 본문을 확인해 보세요. MAC 주소 테이블에 있는 한 포트에만 보낸다."
    - id: d
      text: "다른 IP 네트워크로 라우팅한다"
      feedback: "다시 본문을 확인해 보세요. 다른 IP 네트워크로 라우팅한다."
    - id: e
      text: "프레임을 항상 폐기한다"
      feedback: "다시 본문을 확인해 보세요. 프레임을 항상 폐기한다."
    answer: b
- terms:
  - 트래픽 (Traffic)
  - 호스트 (Host)
  questions:
  - id: u3-03-p05-q01
    kind: choice
    difficulty: easy
    prompt: Broadcast 양이 커지면 네트워크에서 어떤 문제가 생길 수 있나요?
    choices:
    - id: a
      text: 링크 대역폭과 장치 처리 자원을 사용해 지연이나 성능 저하를 일으킬 수 있다
      feedback: 맞아요. 링크 대역폭과 장치 처리 자원을 사용해 지연이나 성능 저하를 일으킬 수 있다.
    - id: b
      text: 인터넷 케이블 길이가 짧아진다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: MAC 주소가 자동으로 IP 주소로 바뀐다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 각 스위치가 더 많은 포트를 갖게 된다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 모든 Unicast가 즉시 중단된다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-03-p05-q02
    kind: choice
    difficulty: medium
    prompt: Broadcast가 여러 링크와 장치의 자원을 쓰는 이유로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 프레임이 전달될 때 항상 1,000배로 커지기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 한 프레임이 전 세계 모든 케이블로 반드시 전달되기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 여러 스위치 방향으로 전달되고 범위 안 장치들이 확인하기 때문이다
      feedback: 맞아요. 여러 스위치 방향으로 전달되고 범위 안 장치들이 확인하기 때문이다.
    - id: d
      text: 브로드캐스트는 데이터 없이 LED만 켜기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 라우터가 매 프레임을 복제하기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-03-p05-q03
    kind: short
    prompt: 링크에서 일정 시간 동안 데이터를 전달할 수 있는 용량을 가리키는 말은 무엇인가요? (영어로 답해주세요)
    answers:
    - bandwidth
    feedback: 정답은 bandwidth입니다.
  - id: u3-03-p05-q04
    kind: choice
    difficulty: medium
    prompt: "브로드캐스트 트래픽이 지나치게 많아질 때 생길 수 있는 영향은 무엇인가요?"
    choices:
    - id: a
      text: "모든 유니캐스트 통신이 반드시 즉시 중단된다"
      feedback: "다시 본문을 확인해 보세요. 모든 유니캐스트 통신이 반드시 즉시 중단된다."
    - id: b
      text: "MAC 주소가 자동으로 IP 주소로 바뀐다"
      feedback: "다시 본문을 확인해 보세요. MAC 주소가 자동으로 IP 주소로 바뀐다."
    - id: c
      text: "Ethernet 프레임 크기 한계가 사라진다"
      feedback: "다시 본문을 확인해 보세요. Ethernet 프레임 크기 한계가 사라진다."
    - id: d
      text: "링크 대역폭과 장치 처리 자원을 차지해 다른 통신에 지연을 줄 수 있다"
      feedback: "맞아요. 링크 대역폭과 장치 처리 자원을 차지해 다른 통신에 지연을 줄 수 있다입니다."
    - id: e
      text: "라우터가 더 많은 링크를 자동으로 만든다"
      feedback: "다시 본문을 확인해 보세요. 라우터가 더 많은 링크를 자동으로 만든다."
    answer: d
  animations:
  - file: l10-broadcast-uses-links.svg
    title: "방송이 잦으면 자원이 줄어든다"
    alt: "스위치 A·B·C와 PC 1~6이 이어진 망에서 PC 4가 PC 5에게 파란 데이터를 계속 보냅니다. PC 1의 주황 방송이 모든 링크를 타고 모든 PC로 퍼지고, 방송이 잦아지자 왼쪽 위의 링크 대역폭·장치 처리 막대에서 주황 부분이 커지며 파란 데이터가 느려집니다. 마지막에 방송이 줄자 막대도 줄어듭니다."
    caption: "방송 하나도 여러 링크와 장치의 자원을 씁니다. 방송량이 커지면 지연이나 성능 저하가 생길 수 있으니 필요할 때만 보내고 범위를 적절히 나눕니다."
- terms:
  - L3 (Layer 3)
  - 라우팅 (Routing)
  - LAN 구역
  animations:
  - file: l10-l3-boundary-blocks-broadcast.svg
    title: 라우터는 L2 브로드캐스트를 전달하지 않는다
    alt: 서로 다른 IP 네트워크 사이에 있는 라우터가 왼쪽 네트워크에서 온 L2 브로드캐스트 프레임을 오른쪽으로 전달하지 않는 장면입니다.
    caption: Ethernet 브로드캐스트 프레임은 라우터를 지나 다른 IP 네트워크로 전달되지 않습니다.
  questions:
  - id: u3-03-p06-q01
    kind: choice
    difficulty: easy
    prompt: 일반적인 Ethernet 브로드캐스트 프레임이 다른 IP 네트워크로 그대로 넘어가지 않게 하는 L3 장비는 무엇인가요?
    choices:
    - id: a
      text: Ethernet frame
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Router
      feedback: 맞아요. Router.
    - id: c
      text: NIC
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: Access switch만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: Host
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-03-p06-q02
    kind: choice
    difficulty: medium
    prompt: 브로드캐스트가 L3 경계를 넘어야 할 때 사용할 수 있는 별도 기능의 예는 무엇인가요?
    choices:
    - id: a
      text: Unicast flooding
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Link up LED
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Jumbo Frame
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: DHCP relay
      feedback: 맞아요. DHCP relay.
    - id: e
      text: MAC address table aging
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p06-q03
    kind: short
    prompt: Ethernet 방송이 다른 IP 네트워크로 그대로 넘어가지 않게 구역을 나누는 경계를 가리키는 말은 무엇일까요? (영어로 답해주세요)
    answers:
    - L3 boundary
    feedback: 정답은 L3 boundary입니다.
  - id: u3-03-p06-q04
    kind: choice
    difficulty: medium
    prompt: "일반적인 Ethernet 브로드캐스트가 다른 IP 네트워크에 그대로 전달되지 않도록 경계를 만드는 장비와, 필요할 때 사용할 수 있는 보조 기능의 조합은 무엇인가요?"
    choices:
    - id: a
      text: "라우터와 DHCP relay"
      feedback: "맞아요. 라우터와 DHCP relay입니다."
    - id: b
      text: "액세스 스위치와 MAC learning"
      feedback: "다시 본문을 확인해 보세요. 액세스 스위치와 MAC learning."
    - id: c
      text: "NIC와 Link up"
      feedback: "다시 본문을 확인해 보세요. NIC와 Link up."
    - id: d
      text: "DNS 서버와 Unicast"
      feedback: "다시 본문을 확인해 보세요. DNS 서버와 Unicast."
    - id: e
      text: "광섬유와 FCS"
      feedback: "다시 본문을 확인해 보세요. 광섬유와 FCS."
    answer: a
- terms:
  - MAC 주소
  - IP 주소
  questions:
  - id: u3-03-p07-q01
    kind: choice
    difficulty: easy
    prompt: 라우터를 지나 다음 링크 구간으로 갈 때 보통 달라지는 정보는 무엇인가요?
    choices:
    - id: a
      text: HTTP 내용이 반드시 MAC 주소로 바뀐다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: LAN이 WAN으로 이름만 바뀌면 패킷이 폐기된다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 출발지·목적지 IP 주소가 매 링크마다 반드시 새로 바뀐다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 전송 데이터 전체가 매 홉마다 사라진다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 프레임과 MAC 주소
      feedback: 맞아요. 프레임과 MAC 주소.
    answer: e
  - id: u3-03-p07-q02
    kind: choice
    difficulty: medium
    prompt: LAN과 WAN을 물리 네트워크와 논리 네트워크에 대응시키는 그림은 어떻게 이해해야 하나요?
    choices:
    - id: a
      text: 처음 구조를 그리는 데 도움이 되는 요령이지 엄밀한 정의는 아니다
      feedback: 맞아요. 처음 구조를 그리는 데 도움이 되는 요령이지 엄밀한 정의는 아니다.
    - id: b
      text: 두 이름은 프레임과 패킷의 크기를 뜻한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: LAN에는 IP를 쓸 수 없고 WAN에만 쓸 수 있다는 뜻이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: WAN은 장비 없이 소프트웨어만 있다는 의미다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: LAN은 언제나 물리적이고 WAN은 언제나 논리적이라는 정의다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-03-p07-q03
    kind: short
    prompt: 라우터를 지나도 보통 그대로 유지되는 네트워크 계층 주소입니다. 영어로 무엇일까요?
    answers:
    - IP address
    feedback: 정답은 IP address입니다.
  - id: u3-03-p07-q04
    kind: choice
    difficulty: medium
    prompt: "일반적인 라우터 전달에서 여러 링크를 지날 때 주소가 바뀌거나 유지되는 방식으로 맞는 것은 무엇인가요?"
    choices:
    - id: a
      text: "MAC 주소와 목적지 IP가 항상 함께 바뀐다"
      feedback: "다시 본문을 확인해 보세요. MAC 주소와 목적지 IP가 항상 함께 바뀐다."
    - id: b
      text: "목적지 IP는 매 링크마다 다음 스위치 주소로 바뀐다"
      feedback: "다시 본문을 확인해 보세요. 목적지 IP는 매 링크마다 다음 스위치 주소로 바뀐다."
    - id: c
      text: "링크별 MAC 주소는 다음 프레임 수신자에 맞게 바뀔 수 있고, 목적지 IP는 최종 목적지를 가리킨다"
      feedback: "맞아요. 링크별 MAC 주소는 다음 프레임 수신자에 맞게 바뀔 수 있고, 목적지 IP는 최종 목적지를 가리킨다입니다."
    - id: d
      text: "출발지와 목적지 MAC은 인터넷 끝까지 고정된다"
      feedback: "다시 본문을 확인해 보세요. 출발지와 목적지 MAC은 인터넷 끝까지 고정된다."
    - id: e
      text: "라우터는 MAC 주소만 보고 네트워크 사이 경로를 정한다"
      feedback: "다시 본문을 확인해 보세요. 라우터는 MAC 주소만 보고 네트워크 사이 경로를 정한다."
    answer: c
  animations:
  - file: l10-mac-changes-ip-stays.svg
    title: "MAC은 링크마다, IP는 끝까지"
    alt: "왼쪽에 물리 매체부터 HTTP까지 계층이 쌓여 있고, Ethernet 칸에는 목적지 MAC, IP 칸에는 목적지 IP가 표시됩니다. 오른쪽에서 PC가 라우터를 거쳐 서버로 보낼 때, 링크 1의 프레임은 목적지 MAC이 라우터이고 링크 2의 새 프레임은 목적지 MAC이 서버로 바뀌지만 목적지 IP는 두 프레임 모두 서버입니다. 마지막에 LAN=물리, WAN=논리라는 그림은 외우기 요령일 뿐이라는 안내가 나옵니다."
    caption: "L2 Ethernet은 같은 링크에서 목적지 MAC을, L3 IP는 네트워크 사이에서 목적지 IP를 봅니다. 라우터를 지나면 프레임과 MAC은 새로 바뀌고 IP는 보통 그대로입니다."
- terms:
  - 논리적 (Logical)
  questions:
  - id: u3-03-p08-q01
    kind: choice
    difficulty: easy
    prompt: IP 네트워크가 케이블 그 자체와 같은 물건이 아닌 이유는 무엇인가요?
    choices:
    - id: a
      text: 모니터 포인터와 같이 화면에만 그려지기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: IP 네트워크는 실제 장비 없이 마법처럼 통신하기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 케이블이 있으면 IP 주소를 사용할 수 없기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 논리 네트워크는 반드시 WAN에서만 쓰기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 물리 링크 위에서 주소와 규칙으로 구성된 연결을 설명하는 추상화이기 때문이다
      feedback: 맞아요. 물리 링크 위에서 주소와 규칙으로 구성된 연결을 설명하는 추상화이기 때문이다.
    answer: e
  - id: u3-03-p08-q02
    kind: choice
    difficulty: medium
    prompt: 네트워크 그림에서 인터넷을 구름으로 표현할 때 주로 뜻하는 것은 무엇인가요?
    choices:
    - id: a
      text: 모든 데이터가 무선 구간만 통과한다는 뜻
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: IP 네트워크가 프레임을 사용하지 않는다는 뜻
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 세부 물리 경로를 펼치지 않고 그 너머 네트워크와 통신한다는 표현
      feedback: 맞아요. 세부 물리 경로를 펼치지 않고 그 너머 네트워크와 통신한다는 표현.
    - id: d
      text: 인터넷이 날씨에 따라 통신한다는 뜻
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 인터넷에는 물리 장비와 케이블이 없다는 사실
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-03-p08-q03
    kind: short
    prompt: 물리 링크 위에서 주소와 규칙으로 구성한 연결을 별도 관점으로 다루는 성질입니다. 영어로 무엇일까요?
    answers:
    - abstraction
    feedback: 정답은 abstraction입니다.
  - id: u3-03-p08-q04
    kind: choice
    difficulty: medium
    prompt: "IP 네트워크를 논리적 연결이라고 부르는 설명으로 맞는 것은 무엇인가요?"
    choices:
    - id: a
      text: "논리적 네트워크에는 실제 케이블이나 장비가 없다"
      feedback: "다시 본문을 확인해 보세요. 논리적 네트워크에는 실제 케이블이나 장비가 없다."
    - id: b
      text: "인터넷 구름 그림은 케이블이 존재하지 않는다는 뜻이다"
      feedback: "다시 본문을 확인해 보세요. 인터넷 구름 그림은 케이블이 존재하지 않는다는 뜻이다."
    - id: c
      text: "논리 네트워크는 항상 하나의 컴퓨터 안에만 있다"
      feedback: "다시 본문을 확인해 보세요. 논리 네트워크는 항상 하나의 컴퓨터 안에만 있다."
    - id: d
      text: "IP 주소가 있으면 물리 연결이 필요 없다"
      feedback: "다시 본문을 확인해 보세요. IP 주소가 있으면 물리 연결이 필요 없다."
    - id: e
      text: "물리 링크와 장비 위에서 주소와 규칙으로 구성한 연결을 따로 표현한다"
      feedback: "맞아요. 물리 링크와 장비 위에서 주소와 규칙으로 구성한 연결을 따로 표현한다입니다."
    answer: e
  animations:
  - file: l10-cloud-over-cables.svg
    title: "포인터와 구름: 논리적이라는 말"
    alt: "왼쪽 모니터에서 마우스를 움직이면 화면의 포인터가 따라 움직이지만 책상 위에는 화살표가 없고, OS가 위치를 기억해 그린다는 표시가 붙습니다. 오른쪽에서는 PC와 서버 사이가 인터넷 구름으로 그려졌다가, 구름이 흐려지며 광섬유·해저 케이블·무선 구간과 라우터가 드러나고, 그 장비들 위로 PC에서 서버까지 가는 파란 경로가 표시되며 그 위의 주소·경로를 보는 관점이라는 문구가 나옵니다."
    caption: "IP 네트워크는 물리 링크 위에서 주소와 규칙으로 구성된 연결을 보는 추상화입니다. 논리적이라는 말은 장비가 없다는 뜻이 아닙니다."
- terms:
  - 가상화 (Virtualization)
  - 가상 머신 (Virtual Machine)
  questions:
  - id: u3-03-p09-q01
    kind: choice
    difficulty: easy
    prompt: 실제 서버 한 대가 여러 독립된 가상 머신 환경을 제공할 수 있게 하는 것은 무엇 덕분인가요?
    choices:
    - id: a
      text: 한 서버에 네트워크 인터페이스가 하나뿐이기 때문
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 각 가상 머신이 서로 다른 물리 서버를 반드시 사용하기 때문
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 모든 VM에 같은 메모리와 저장 공간을 복사하기 때문
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 소프트웨어가 물리 자원을 나누어 제공하기 때문
      feedback: 맞아요. 소프트웨어가 물리 자원을 나누어 제공하기 때문.
    - id: e
      text: 물리 네트워크가 없어도 되기 때문
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p09-q02
    kind: choice
    difficulty: medium
    prompt: “논리적” 또는 “가상” 네트워크라는 말의 의미로 가장 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 물리 장비가 전혀 없어서 실제 통신을 하지 않는다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 모든 VM이 서로 같은 네트워크 주소를 써야 한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: LAN은 반드시 가상이고 WAN은 반드시 물리적이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 물리 자원 위에 다른 규칙과 경계를 만들어 표현하고 관리한다
      feedback: 맞아요. 물리 자원 위에 다른 규칙과 경계를 만들어 표현하고 관리한다.
    - id: e
      text: 가짜 주소만 쓰고 실제 네트워크와 연결되지 않는다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p09-q03
    kind: short
    prompt: 실제 컴퓨터 자원을 소프트웨어로 나누어 여러 가상 머신처럼 제공하는 기술입니다. 영어로 답해주세요.
    answers:
    - virtualization
    feedback: 정답은 virtualization입니다.
  - id: u3-03-p09-q04
    kind: choice
    difficulty: medium
    prompt: "가상화가 한 대의 실제 서버에서 여러 가상 머신을 제공할 수 있게 하는 방식으로 가장 알맞은 것은 무엇인가요?"
    choices:
    - id: a
      text: "서버 안에 같은 수의 물리 컴퓨터를 추가 설치한다"
      feedback: "다시 본문을 확인해 보세요. 서버 안에 같은 수의 물리 컴퓨터를 추가 설치한다."
    - id: b
      text: "소프트웨어가 실제 컴퓨터 자원을 나누어 각 가상 머신에 제공한다"
      feedback: "맞아요. 소프트웨어가 실제 컴퓨터 자원을 나누어 각 가상 머신에 제공한다입니다."
    - id: c
      text: "각 가상 머신이 별도의 인터넷을 물리적으로 만든다"
      feedback: "다시 본문을 확인해 보세요. 각 가상 머신이 별도의 인터넷을 물리적으로 만든다."
    - id: d
      text: "MAC 주소를 모두 같게 설정한다"
      feedback: "다시 본문을 확인해 보세요. MAC 주소를 모두 같게 설정한다."
    - id: e
      text: "가상 머신은 네트워크 인터페이스를 사용할 수 없다"
      feedback: "다시 본문을 확인해 보세요. 가상 머신은 네트워크 인터페이스를 사용할 수 없다."
    answer: b
  animations:
  - file: l10-one-server-many-vms.svg
    title: "한 대를 여러 대처럼: 가상화"
    alt: "왼쪽에 CPU 시간·메모리·저장 공간·네트워크를 가진 실제 서버 한 대가 있고, 그 위에 가상화 소프트웨어가 놓인 뒤 자원이 세 색으로 나뉘어 VM 1~3에 배정됩니다. 오른쪽에서는 PC 네 대가 실제 스위치 하나에 케이블로 연결된 채 가상 네트워크 A와 B로 묶이고, 마지막에 실제 장비 위의 다른 규칙·경계라는 표시가 나옵니다."
    caption: "가상화는 소프트웨어가 실제 자원을 나눠 여러 대처럼 쓰게 하는 기술입니다. 가상 네트워크도 실제 케이블과 스위치 위에서 동작하며, 다른 규칙과 경계로 관리합니다."
- terms:
  - LAN (Local Area Network)
  - WAN (Wide Area Network)
  questions:
  - id: u3-03-p10-q01
    kind: choice
    difficulty: easy
    prompt: LAN과 WAN을 구분할 때 기본적으로 설명하는 기준은 무엇인가요?
    choices:
    - id: a
      text: MAC 주소 길이
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 네트워크가 걸쳐 있는 지리적 범위
      feedback: 맞아요. 네트워크가 걸쳐 있는 지리적 범위.
    - id: c
      text: 물리 대 논리만으로 정해지는 구분
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 장치의 운영체제 종류
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 프레임의 Ethernet 크기
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-03-p10-q02
    kind: choice
    difficulty: medium
    prompt: LAN과 WAN에 관한 설명으로 정확한 것은 무엇인가요?
    choices:
    - id: a
      text: LAN은 반드시 물리 연결이고 WAN은 반드시 논리 연결이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: LAN도 논리적으로 나뉠 수 있고 WAN도 물리 장비 위에서 구현된다
      feedback: 맞아요. LAN도 논리적으로 나뉠 수 있고 WAN도 물리 장비 위에서 구현된다.
    - id: c
      text: LAN은 MAC 주소를 쓰고 WAN은 IP 주소를 쓰지 않는다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: LAN과 WAN은 각각 하나의 고정 거리로만 구분된다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: WAN에는 케이블이나 라우터가 필요 없다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-03-p10-q03
    kind: short
    prompt: 제한된 지역보다 더 넓은 범위를 잇는 네트워크를 가리키는 영어 약어입니다. 무엇일까요?
    answers:
    - WAN
    feedback: 정답은 WAN입니다.
  - id: u3-03-p10-q04
    kind: choice
    difficulty: medium
    prompt: "LAN과 WAN을 구분하는 기본 관점에 대한 설명으로 가장 정확한 것은 무엇인가요?"
    choices:
    - id: a
      text: "LAN은 항상 물리적이고 WAN은 항상 논리적이다"
      feedback: "다시 본문을 확인해 보세요. LAN은 항상 물리적이고 WAN은 항상 논리적이다."
    - id: b
      text: "WAN은 반드시 광섬유를 써야 한다"
      feedback: "다시 본문을 확인해 보세요. WAN은 반드시 광섬유를 써야 한다."
    - id: c
      text: "LAN은 유선만, WAN은 무선만 사용한다"
      feedback: "다시 본문을 확인해 보세요. LAN은 유선만, WAN은 무선만 사용한다."
    - id: d
      text: "주로 네트워크가 아우르는 범위를 설명하며, 물리적·논리적 여부만으로 구분하지 않는다"
      feedback: "맞아요. 주로 네트워크가 아우르는 범위를 설명하며, 물리적·논리적 여부만으로 구분하지 않는다입니다."
    - id: e
      text: "LAN과 WAN은 속도 순위를 나타낸다"
      feedback: "다시 본문을 확인해 보세요. LAN과 WAN은 속도 순위를 나타낸다."
    answer: d

  animations:
  - file: l10-lan-wan-summary.svg
    title: "LAN·WAN 한 장으로 정리"
    alt: "왼쪽 구역의 PC는 케이블로, 노트북은 Wi-Fi로 스위치에 연결되어 있고 그 링크 위로 파란 프레임이 오갑니다. 주황 방송은 왼쪽 구역 안에만 퍼지고 라우터에서 멈추며, 민트 IP 패킷은 라우터 두 개를 지나 오른쪽 구역의 PC까지 갑니다. 이어서 두 구역이 LAN, 전체가 WAN으로 묶이고, 마지막에 오른쪽 LAN의 VLAN 구분과 WAN의 광섬유·무선 구간, 범위·기술·운영 주체라는 판단 기준이 나타납니다."
    caption: "링크 위로 MAC 프레임이 오가고, 그 위에서 IP 패킷이 네트워크 사이를 이동합니다. LAN과 WAN은 물리·논리만으로 나뉘지 않으니 범위·기술·운영 주체 같은 문맥으로 판단합니다."
animations_dir: units/03-layer2-switching/lessons/03-lan과-wan의-경계-그리고-broadcast/assets/animations
---
네트워크에서 “모두에게 알려야 하는 말”은 어떻게 전달될까? 그리고 그 말은 어디까지 퍼져도 괜찮을까? 아파트 안내 방송과 택배 송장, 손에 잡히지 않는 마우스 포인터를 떠올리며 Broadcast와 LAN·WAN의 관계를 살펴보자.

## Broadcast · 모두에게 보내기

친구 한 명에게 쪽지를 건네는 것과 교실 전체에 안내 방송을 하는 것을 비교해 보자. 한 사람을 지정해 보내는 통신이 Unicast이고, 같은 범위에 있는 여러 장치에게 한꺼번에 알리는 통신이 Broadcast다. Broadcast는 “누군지 모르겠으니 이 범위 안의 모두에게 물어볼게”처럼 쓸모가 있다. 하지만 안내 방송이 잦으면 자기와 상관없는 학생도 듣느라 수업을 멈춰야 한다. 네트워크의 장치도 Broadcast를 받으면 내용을 확인해야 하므로, 필요하지 않은 방송이 많아질수록 다른 통신이 쓸 자원과 장치의 처리 시간이 줄어든다.

여기서 중요한 말은 ‘모두’의 범위다. 전 세계 모든 장치가 아니라, 같은 브로드캐스트 도메인에 속한 장치들이다. 그 범위를 이해하면 스위치가 방송을 퍼뜨리는 이유와 L3 경계가 필요한 이유가 함께 보인다.

## 브로드캐스트 도메인

아파트 관리실에서 “입주민 여러분, 정전 점검이 있습니다”라고 방송하면 그 방송은 한 집에만 전달되지 않는다. 같은 방송 장비에 연결된 세대 모두가 들을 수 있다. 이때 방송이 닿는 구역을 브로드캐스트 도메인이라고 생각하면 된다. 한 동 전체가 한 구역일 수도 있고, 관리 방식에 따라 여러 구역으로 나뉠 수도 있다.

네트워크에서도 Broadcast는 필요한 기능이지만, 한 번의 방송을 받은 스위치가 연결된 여러 방향으로 전달하면 범위 안의 장치들이 모두 확인하게 된다. 그래서 “방송을 보낼 수 있나?”만큼 “어느 구역까지 들리게 할까?”가 중요하다. Ethernet에서 브로드캐스트를 표시하는 특별한 목적지 MAC 주소는 48비트가 모두 1인 값이다. IP 브로드캐스트 주소는 주소 범위와 함께 뒤에서 따로 살펴본다.

## 브로드캐스트 MAC 주소

택배 상자에 받는 사람 주소가 적혀 있으면 특정 집으로 간다. 그런데 송장에 “이 구역의 모든 집”이라고 표시되어 있다면 배달 방식이 달라질 것이다. Ethernet 프레임에도 받는 곳을 적는 목적지 MAC 주소가 있고, 그 자리에 브로드캐스트 주소를 쓰면 “이 브로드캐스트 도메인 안의 모두가 확인해 주세요”라는 뜻이 된다.

그 주소를 2진수로 보면 48개의 자리가 전부 1이다. MAC 주소를 보기 좋게 16진수 여섯 칸으로 적으므로 `FF:FF:FF:FF:FF:FF`가 된다. F 하나는 2진수 `1111`, FF는 `11111111`이다. 즉 F 두 개가 8비트 한 칸을 채우고, 그런 칸 여섯 개가 모여 48비트 전체를 채운다. 외울 때는 “여섯 칸의 FF, 받는 사람은 구역 안의 모두”라고 연결하면 된다. 모든 비트가 1인 값이 언제나 Broadcast라는 뜻은 아니며, 여기서는 Ethernet 목적지 MAC 주소라는 자리와 문맥이 함께 특별한 의미를 만든다.

## 스위치에서 전파되는 과정

L2에서 주고받는 데이터 단위는 프레임이다. 프레임은 택배 상자, 헤더는 겉면의 송장이라고 떠올려 보자. 송장에는 보내는 곳과 받는 곳이 있어야 하듯 프레임 헤더에도 출발지 MAC 주소와 목적지 MAC 주소가 들어간다. Ethernet MAC 주소 하나는 48비트이고, 헤더에는 주소들뿐 아니라 상위에 어떤 프로토콜 데이터가 실렸는지를 나타내는 Type 같은 정보도 담긴다.

PC 1이 `FF:FF:FF:FF:FF:FF`를 목적지로 적은 프레임을 액세스 스위치 A에 보냈다고 하자. 특정 한 곳에 배달할 송장이 아니므로 스위치는 받은 포트 하나를 제외한 여러 포트로 프레임을 내보낸다. 배포 스위치 C도 이 프레임을 받으면 자신이 관리하는 다른 연결 방향으로 전달하고, 반대편 액세스 스위치 B도 연결된 PC들에게 퍼뜨린다. 하나의 방송이 스위치 연결을 따라 갈래를 만들며 전파되는 셈이다. 스위치가 내용을 새로 만들어 내는 것이 아니라, 목적지 주소가 “이 구역의 모두”라고 지정했기 때문에 전달한다.

## 트래픽이 불어나는 문제

교실 한쪽에서 안내 방송을 한 번 하면 모두가 듣는다. 방송이 계속 반복되면 학생마다 듣는 시간은 짧아도 교실 전체의 시간이 조금씩 쓰인다. 네트워크에서도 PC 1의 방송 하나가 스위치들을 따라 전달되면서 여러 링크와 장치의 자원을 사용한다. PC 4가 PC 5에게 필요한 데이터를 보내는 중에도 장치들은 들어온 방송 프레임을 받고 확인해야 한다. Broadcast가 곧바로 모든 Unicast를 멈춘다는 뜻은 아니지만, 방송량이 커지면 링크 대역폭과 장치의 처리 자원을 함께 차지해 지연이나 성능 저하를 일으킬 수 있다. 그래서 필요한 발견·안내에는 Broadcast를 쓰되, 불필요하게 자주 보내지 않고 범위를 적절히 나누는 것이 운영의 요령이다.

## L3 경계와 브로드캐스트

아파트 방송을 동별로 나눠 한 동의 안내가 다른 동에 자동으로 울리지 않게 하는 모습을 생각해 보자. 네트워크도 L3 라우터 경계를 두면 일반적인 Ethernet 브로드캐스트 프레임을 다른 IP 네트워크로 그대로 전달하지 않는다. 예를 들어 PC 1~3이 있는 쪽에서 나온 방송은 그 구역에 머물고, PC 4~6이 있는 다른 쪽에는 닿지 않게 설계할 수 있다. 이 경계는 방송의 범위를 제한해 불필요한 영향을 줄인다.

대신 경계를 건너야 하는 발견이나 요청이 있다면 라우터의 DHCP relay 같은 별도 기능이나 애플리케이션의 다른 전달 방식을 써야 할 수 있다. 범위를 작게 나누는 데에는 관리와 설정이 더 필요하다는 점도 함께 기억하자. 여기서 말하는 것은 L2 Ethernet 브로드캐스트의 일반적인 전달 범위이며, 모든 IP 패킷이나 모든 멀티캐스트가 똑같이 막힌다는 뜻은 아니다. IP 브로드캐스트 주소와 서브넷의 관계는 뒤의 IP 주소 단원에서 이어서 배운다.

## LAN과 WAN을 보는 관점

계층 그림에서는 아래쪽에 전기 신호·무선 신호 같은 물리 매체와 Ethernet, 그 위에 IP, TCP·UDP, TLS, HTTP처럼 서로 다른 역할의 규칙이 놓인다. 이때 L2 Ethernet이 같은 링크에서 프레임을 전달할 때 목적지 MAC 주소를 보고, L3 IP가 네트워크 사이에서 패킷을 전달할 때 IP 주소를 본다고 연결해 두면 좋다. 편의상 MAC을 가까운 링크의 배달 주소, IP를 목적지 네트워크를 찾는 주소처럼 비유할 수 있지만, 두 주소가 맡는 일과 수명은 다르다. 라우터를 지나도 보통 출발지·목적지 IP는 그대로 유지되는 한편, 각 링크에서 프레임은 새로 만들어지고 MAC 주소는 다음 구간의 이웃에 맞게 달라진다.

LAN과 WAN을 외울 때 물리 네트워크와 논리 네트워크를 연결하는 학습용 그림을 쓰기도 한다. 이 연결은 처음 구조를 그려 보는 데 도움을 주는 요령이지, LAN은 무조건 물리적이고 WAN은 무조건 논리적이라는 정의는 아니다.

## 물리 네트워크와 논리 네트워크

모니터 위의 마우스 포인터는 화면에서 분명 움직이지만, 책상 위에 작은 화살표 조각이 실제로 놓여 있는 것은 아니다. 운영체제가 위치를 기억하고 화면에 그려 주기 때문에 논리적으로 존재한다. IP 네트워크도 케이블 그 자체와 같은 물건은 아니며, 물리 링크 위에서 주소와 규칙으로 구성된 연결을 설명하는 추상화다. 그래서 인터넷을 그릴 때 실제 전 세계 케이블 대신 구름 모양을 그리곤 한다. 구름 아이콘은 “내가 지금 모든 케이블 경로를 펼쳐 보이지 않아도, 그 너머의 네트워크와 통신한다”는 약속처럼 쓰인다.

다만 실제 인터넷에는 해저 케이블, 광섬유, 무선 구간, 라우터 같은 물리 장비가 있다. ‘논리적’이라는 말은 기반 장비가 없다는 뜻이 아니라, 그 위의 주소·경로·연결을 별도의 관점으로 다룬다는 뜻이다.

## 가상 네트워크라는 표현

손으로 마우스를 움직이면 화면 속 포인터가 따라오지만, 포인터를 밀고 있는 작은 물체가 화면 안에 있는 것은 아니다. 그 포인터는 컴퓨터가 상태를 관리하고 그려 주는 논리적인 대상이다. 비슷하게, 한 대의 실제 서버 안에 여러 대처럼 보이는 가상 머신을 만들 수 있다. 소프트웨어가 CPU 시간, 메모리, 저장 공간과 네트워크 인터페이스를 나눠 각 가상 머신에 제공하기 때문이다. 물리적인 기계를 소프트웨어로 나누어 쓰거나 흉내 내는 기술을 가상화라고 한다.

네트워크에서도 가상 LAN이나 가상 네트워크처럼 논리적으로 구분한 연결을 만들 수 있다. 이런 연결은 실제 케이블과 스위치 위에서 동작하지만, 구성과 정책을 소프트웨어로 관리할 수 있다. 그러니 ‘논리적’과 ‘가상’은 눈에 보이지 않으니 가짜라는 뜻이 아니라, 물리 자원을 다른 규칙과 경계로 표현하고 관리한다는 쪽에 가깝다.

## LAN·WAN의 구별 정리

이제 처음 질문으로 돌아가자. LAN 케이블이 꽂혀 있거나 Wi-Fi 신호가 닿는지는 지금 연결된 링크와 매체의 문제다. 그 링크를 통해 MAC 주소가 있는 프레임이 오가고, 그 위에서 IP 주소를 사용해 서로 다른 네트워크 사이로 패킷이 이동한다. 건물 안내 방송 비유로는, 같은 방송 구역 안의 전달이 L2 브로드캐스트의 감각을 잡게 해 준다. 라우터는 방송이 다른 구역까지 저절로 번지는 일을 막는 경계에 가깝다.

LAN은 보통 제한된 지역의 네트워크를 가리키고, WAN은 더 넓은 지역을 잇는 네트워크를 가리킨다. 초보 단계에서는 “가까운 물리 연결을 바탕으로, 그 위에 더 넓은 IP 연결을 구성한다”고 그려 보면 도움이 된다. 하지만 LAN과 WAN은 오직 물리와 논리만으로 나뉘지 않는다. LAN도 VLAN처럼 논리적으로 나뉠 수 있고, WAN도 케이블·광섬유·무선 장비 위에서 실제로 구현된다. 그러므로 이 비유는 네트워크를 머릿속에 그리는 출발점으로 쓰고, 정식 구분은 범위·기술·운영 주체 같은 문맥을 함께 보며 판단하자.

**한 문장으로 기억하기:** `FF:FF:FF:FF:FF:FF`는 같은 브로드캐스트 구역 모두에게 보내는 Ethernet 프레임의 목적지이고, 스위치는 그 구역 안으로 퍼뜨리며, 라우터는 그 L2 방송이 다른 IP 네트워크로 그대로 넘어가지 않게 경계를 만든다.
