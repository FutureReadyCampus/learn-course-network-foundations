---
id: u4-l15-계층별-데이터-단위
title: 데이터는 Stream에서 Frame까지 어떻게 나뉘고 포장될까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-15.md
wiki_diagram: units/04-layer3-addressing/lessons/05-계층별-데이터-단위/assets/diagrams/lesson-15.svg
page_metadata:
- terms:
  - Frame(프레임)
  - Packet(패킷)
  - Segment(세그먼트)
  questions:
  - id: u4-l15-p01-q01
    kind: choice
    difficulty: easy
    prompt: 같은 정보를 여러 네트워크 계층에서 다른 이름으로 부른다는 것은 내용이 계층마다 사라진다는 뜻인가요?
    choices:
    - id: a
      text: 네. 계층을 지날 때마다 원래 데이터가 없어집니다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: 아니요. 같은 데이터가 계층별 전달 단위로 묶여 다른 이름으로 불릴 수 있습니다
      feedback: 맞아요. 계층을 지날 때 데이터에 전달 정보가 더해지고 단위 이름이 달라져도 안쪽 내용은 전달될 수 있어요.
    - id: c
      text: 네. Frame은 Packet과 전혀 관계가 없습니다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: 아니요. 모든 계층에서 이름은 항상 Frame 하나뿐입니다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: 네. Segment는 데이터가 아니라 IP 주소입니다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: b
  - id: u4-l15-p01-q02
    kind: choice
    difficulty: easy
    prompt: IP가 다루는 L3 데이터 단위의 이름은 무엇인가요?
    choices:
    - id: a
      text: Frame
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: Segment
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: Stream
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: Packet
      feedback: 맞아요. IP 계층(L3)의 데이터 단위는 Packet이에요.
    - id: e
      text: Datagram
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: d
  - id: u4-l15-p01-q03
    kind: choice
    difficulty: medium
    prompt: 계층별 데이터 단위를 바르게 연결한 것은 무엇인가요?
    choices:
    - id: a
      text: TCP=Segment, IP=Packet, Ethernet 데이터 링크=Frame
      feedback: 맞아요. TCP는 Segment, IP는 Packet, Ethernet 데이터 링크는 Frame을 다뤄요.
    - id: b
      text: TCP=L2 Frame, IP=L4 Segment, Ethernet=L3 Packet
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: TCP=Packet, IP=Frame, Ethernet=Segment
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: 물리 계층=L2 Frame, 데이터 링크=L1 bit
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: TCP=Stream, IP=Datagram, Ethernet=Packet
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: a
  - id: u4-l15-p01-q04
    kind: short
    prompt: 'TCP가 다루는 전송 계층 단위를 무엇이라고 하나요? (힌트: Segment)'
    answers:
    - segment
    - 세그먼트
    feedback: Segment(세그먼트)는 TCP가 다루는 전송 계층 단위예요.
  question_placements:
  - question_id: u4-l15-p01-q01
    after_paragraph: 1
  - question_id: u4-l15-p01-q02
    after_paragraph: 2
- terms:
  - Socket(소켓)
  - Stream(스트림)
  - User mode(사용자 모드)
  questions:
  - id: u4-l15-p02-q01
    kind: choice
    difficulty: easy
    prompt: 브라우저가 운영체제의 네트워크 기능을 요청할 때 이용하는 창구는 무엇인가요?
    choices:
    - id: a
      text: 소켓
      feedback: 맞아요. 프로그램은 소켓 인터페이스를 통해 운영체제의 네트워크 기능을 이용해요.
    - id: b
      text: MTU
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: 프레임
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: 세그먼트
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: 라우터
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: a
  - id: u4-l15-p02-q02
    kind: choice
    difficulty: easy
    prompt: TCP 소켓에서 연속해서 이어지는 데이터 흐름을 무엇이라고 하나요?
    choices:
    - id: a
      text: Frame
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: MSS
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: Stream
      feedback: 맞아요. 연속된 데이터 흐름을 Stream이라고 불러요.
    - id: d
      text: Packet
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: Datagram
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: c
  - id: u4-l15-p02-q03
    kind: choice
    difficulty: medium
    prompt: TCP Stream에 대해 바르게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 항상 1,500바이트짜리 메시지 경계로만 나뉜다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: 한 번의 읽기가 항상 한 번의 쓰기와 정확히 일치한다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: Stream은 Ethernet 프레임의 다른 이름이다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: Stream은 UDP에만 있고 TCP에는 없다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: 연속된 데이터 흐름이며, 애플리케이션이 메시지 경계를 정할 수 있다
      feedback: 맞아요. TCP Stream은 연속된 데이터 흐름이고 메시지 경계는 애플리케이션이 정할 수 있어요.
    answer: e
  - id: u4-l15-p02-q04
    kind: short
    prompt: 'TCP 소켓에서 다루는 연속된 데이터 흐름을 무엇이라고 하나요? (힌트: Stream)'
    answers:
    - stream
    - 스트림
    feedback: Stream(스트림)은 TCP 소켓에서 다루는 연속된 데이터 흐름이에요.
  question_placements:
  - question_id: u4-l15-p02-q01
    after_paragraph: 1
  - question_id: u4-l15-p02-q02
    after_paragraph: 2
- terms:
  - MTU(Maximum Transmission Unit)
  - MSS(Maximum Segment Size)
  - Header(헤더)
  questions:
  - id: u4-l15-p03-q01
    kind: choice
    difficulty: easy
    prompt: 네트워크 링크에서 IP 패킷이 넘지 않아야 하는 최대 크기를 무엇이라고 하나요?
    choices:
    - id: a
      text: MSS
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: MTU
      feedback: 맞아요. MTU는 링크에서 전달할 수 있는 IP 패킷의 최대 크기예요.
    - id: c
      text: Segment
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: Stream
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: Socket
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: b
  - id: u4-l15-p03-q02
    kind: choice
    difficulty: easy
    prompt: 기본 Ethernet 예에서 MTU가 1,500바이트라면, 모든 패킷은 꼭 1,500바이트여야 하나요?
    choices:
    - id: a
      text: 네. 항상 정확히 1,500바이트여야 합니다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: 아니요. 1,500바이트는 포트 번호입니다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: 네. MSS도 모든 경우 1,500바이트입니다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: 아니요. 1,500바이트는 상한이므로 더 작은 패킷도 가능합니다
      feedback: 맞아요. MTU는 최대 크기 상한이므로 패킷이 그보다 작을 수 있어요.
    - id: e
      text: 네. Ethernet 프레임 전체가 언제나 정확히 그 크기입니다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: d
  - id: u4-l15-p03-q03
    kind: choice
    difficulty: medium
    prompt: IPv4/TCP 헤더가 각각 20바이트이고 옵션이 없으며 MTU가 1,500바이트일 때, 예시 MSS는 얼마인가요?
    choices:
    - id: a
      text: 1,500바이트
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: 1,480바이트
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: 1,460바이트
      feedback: 맞아요. IP와 TCP 헤더 각 20바이트를 빼면 TCP 데이터 최대 크기 예시는 1,460바이트예요.
    - id: d
      text: 1,440바이트
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: 20바이트
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: c
  - id: u4-l15-p03-q04
    kind: short
    prompt: 'TCP Segment 하나에 담을 수 있는 데이터의 최대 크기 기준은 무엇인가요? (힌트: Maximum Segment Size)'
    answers:
    - MSS
    - Maximum Segment Size
    feedback: MSS(Maximum Segment Size)는 TCP 데이터의 최대 크기 기준이에요.
  question_placements:
  - question_id: u4-l15-p03-q01
    after_paragraph: 1
  - question_id: u4-l15-p03-q02
    after_paragraph: 2
- terms:
  - Segmentation(분할)
  animations:
  - file: l15-segmentation.svg
    title: 긴 데이터를 MSS 조각으로 나누기
    alt: 왼쪽에서 길게 이어진 막대가 일정한 길이로 잘리고, 각 조각에 1번, 2번, 3번 번호표가 붙어 오른쪽으로 한 줄로 나가는 장면입니다. 마지막 조각만 짧습니다.
    caption: 앞서 계산한 조건의 예시 MSS 1,460바이트를 기준으로, 긴 Stream이 TCP 데이터 조각들로 나뉩니다. 마지막 조각은 더 짧습니다.
  questions:
  - id: u4-l15-p04-q01
    kind: choice
    difficulty: easy
    prompt: TCP가 MSS보다 긴 Stream을 보낼 때 하는 일은 무엇인가요?
    choices:
    - id: a
      text: Stream을 MSS 크기에 맞는 여러 조각으로 나눈다
      feedback: 맞아요. TCP는 긴 데이터를 MSS에 맞는 여러 조각으로 나눠 전송해요.
    - id: b
      text: Stream 전체를 Frame 헤더에 한꺼번에 넣는다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: 데이터를 모두 지우고 IP 주소만 보낸다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: MTU를 자동으로 무한히 크게 만든다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: 소켓을 UDP Datagram으로 바꾼다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: a
  - id: u4-l15-p04-q02
    kind: choice
    difficulty: easy
    prompt: 긴 데이터를 더 작은 Segment들로 나누는 과정을 무엇이라고 하나요?
    choices:
    - id: a
      text: Encapsulation
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: Decapsulation
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: Routing
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: Segmentation
      feedback: 맞아요. Segmentation은 연속된 데이터를 더 작은 전송 조각으로 분할하는 과정이에요.
    - id: e
      text: Translation
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: d
  - id: u4-l15-p04-q03
    kind: choice
    difficulty: medium
    prompt: 4MB 데이터 Stream이 MSS보다 훨씬 길 때 TCP의 동작으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 4MB 전체를 Segment 하나에 넣는다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: MSS와 연결 조건에 맞춰 여러 Segment로 나누어 보낸다
      feedback: 맞아요. 긴 Stream은 TCP가 MSS 기준에 맞춰 여러 Segment로 나눠 전송해요.
    - id: c
      text: 모든 바이트를 별도 IP 주소로 보낸다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: 데이터 링크 계층이 소켓 대신 분할한다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: MTU 제한을 무시하고 하나의 패킷으로 보낸다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: b
  - id: u4-l15-p04-q04
    kind: short
    prompt: '긴 Stream을 더 작은 전송 단위로 나누는 과정을 무엇이라고 하나요? (힌트: Segmentation)'
    answers:
    - segmentation
    - 세그멘테이션
    - 분할
    feedback: Segmentation(세그멘테이션)은 긴 데이터를 더 작은 단위로 분할하는 과정이에요.
  question_placements:
  - question_id: u4-l15-p04-q01
    after_paragraph: 1
  - question_id: u4-l15-p04-q02
    after_paragraph: 2
- terms:
  - Encapsulation(캡슐화)
  - FCS(Frame Check Sequence)
  animations:
  - file: l15-encapsulation.svg
    title: 세그먼트가 IP 패킷과 Ethernet 프레임에 담기는 과정
    alt: 작은 데이터 상자에 TCP 헤더, IP 헤더, Ethernet 헤더와 FCS가 차례로 붙어 크기가 달라지고, 마지막에 케이블 위로 이동하는 장면입니다.
    caption: 가정한 크기의 예에서 데이터에 TCP 헤더, IP 헤더, Ethernet 헤더와 FCS가 덧붙는 모습을 보여 줍니다.
  questions:
  - id: u4-l15-p05-q01
    kind: choice
    difficulty: easy
    prompt: TCP Segment를 담아 IP 헤더를 붙이면 어떤 단위가 되나요?
    choices:
    - id: a
      text: Stream
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: Ethernet Frame
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: IP Packet
      feedback: 맞아요. IP 계층은 Segment를 페이로드로 담아 IP Packet을 만들어요.
    - id: d
      text: MSS
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: Socket
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: c
  - id: u4-l15-p05-q02
    kind: choice
    difficulty: easy
    prompt: IP Packet을 같은 Ethernet 링크에서 보내기 위해 바깥에서 감싸는 단위는 무엇인가요?
    choices:
    - id: a
      text: Frame
      feedback: 맞아요. 데이터 링크 계층은 IP Packet을 Frame에 담아 링크로 보내요.
    - id: b
      text: Stream
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: Segment
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: MSS
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: 소켓
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: a
  - id: u4-l15-p05-q03
    kind: choice
    difficulty: medium
    prompt: MTU와 Ethernet Frame 크기의 관계를 정확히 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: MTU는 TCP Segment의 데이터만 뜻하고 Frame은 항상 1,500바이트다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: MTU와 Frame은 항상 같은 크기다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: MTU는 포트 번호의 최대값이다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: Frame에는 IP Packet이 들어갈 수 없다
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: MTU는 IP Packet의 최대 크기를 가리키며 Frame에는 링크 헤더와 트레일러도 더해질 수 있다
      feedback: 맞아요. MTU는 IP Packet의 최대 크기고 Ethernet Frame에는 링크 정보가 더해져요.
    answer: e
  - id: u4-l15-p05-q04
    kind: short
    prompt: '데이터 링크 계층(L2)에서 IP 패킷을 감싸 링크로 전달하는 단위는 무엇인가요? (힌트: Frame)'
    answers:
    - frame
    - 프레임
    feedback: Frame(프레임)은 데이터 링크 계층에서 링크로 전달할 때 사용하는 단위예요.
  question_placements:
  - question_id: u4-l15-p05-q01
    after_paragraph: 1
  - question_id: u4-l15-p05-q02
    after_paragraph: 2
- terms:
  - Datagram(데이터그램)
  - Packet(패킷)
  - Segment(세그먼트)
  questions:
  - id: u4-l15-p06-q01
    kind: choice
    difficulty: easy
    prompt: TCP가 연속된 데이터 흐름을 나누어 전달할 때 L4 단위로 부르는 이름은 무엇인가요?
    choices:
    - id: a
      text: Datagram
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: Packet
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: Frame
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: Segment
      feedback: 맞아요. TCP의 전송 계층 데이터 단위는 Segment예요.
    - id: e
      text: Stream
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: d
  - id: u4-l15-p06-q02
    kind: choice
    difficulty: easy
    prompt: UDP가 전송하는 하나의 데이터 덩어리를 무엇이라고 하나요?
    choices:
    - id: a
      text: Socket
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: Datagram
      feedback: 맞아요. UDP의 전송 계층 데이터 단위는 Datagram이에요.
    - id: c
      text: MSS
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: Stream
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: Ethernet Frame
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    answer: b
  - id: u4-l15-p06-q03
    kind: choice
    difficulty: medium
    prompt: TCP와 UDP의 전송 계층 단위를 바르게 짝지은 것은 무엇인가요?
    choices:
    - id: a
      text: TCP=Datagram, UDP=Segment
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: b
      text: TCP=Frame, UDP=Stream
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: c
      text: TCP=Packet, UDP=Socket
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: d
      text: TCP=MTU, UDP=MSS
      feedback: 다시 생각해 보세요. 본문에서 이 계층 또는 데이터 단위의 역할을 확인해 보세요.
    - id: e
      text: TCP=Segment, UDP=Datagram
      feedback: 맞아요. TCP는 Segment, UDP는 Datagram을 전송 계층 단위로 사용해요.
    answer: e
  - prompt: 'UDP가 전송하는 하나의 데이터 덩어리를 무엇이라고 하나요? (힌트: Datagram)'
    answers:
    - datagram
    - 데이터그램
    feedback: Datagram(데이터그램)은 UDP가 전송하는 하나의 데이터 덩어리예요.
    id: u4-l15-p06-q04
    kind: short
  question_placements:
  - question_id: u4-l15-p06-q01
    after_paragraph: 1
  - question_id: u4-l15-p06-q02
    after_paragraph: 2
animations_dir: units/04-layer3-addressing/lessons/05-계층별-데이터-단위/assets/animations
additional_sources:
- https://github.com/physical-spark/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/01-3.md
- https://github.com/physical-spark/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/03-1.md
---
핵심 개념을 주제별로 정리했다.

## 계층마다 달라지는 데이터 이름

택배로 책을 보낼 때 책은 내용물이지만, 상자에 담기면 운반 단위로 다뤄진다. 네트워크에서도 같은 정보가 계층을 지날 때마다 전달에 맞는 단위로 묶이고 이름이 달라진다.

TCP/IP 통신에서는 TCP가 다루는 단위를 Segment(세그먼트), IP가 다루는 단위를 Packet(패킷), 데이터 링크 계층(L2)이 다루는 단위를 Frame(프레임)이라고 한다. 예를 들어 IP 패킷은 L3에서 하나의 단위이고, Ethernet 프레임 안에서는 페이로드로 실린다.

물리 계층(L1)은 프레임을 새 단위로 다루는 계층이 아니라, L2 프레임을 비트와 신호로 실제 매체에 전달한다. 따라서 여기서는 L1은 비트, L2는 프레임이라고 구별하고, 계층별 이름은 같은 데이터의 전달 단위가 어디에서 어떻게 보이는지를 나타낸다고 기억하자.

## Socket과 Stream

브라우저 같은 애플리케이션은 운영체제의 네트워크 기능을 소켓(Socket) 인터페이스로 이용한다. 프로그램이 소켓을 통해 TCP에 데이터를 전달하면, 애플리케이션은 보통 이를 처음부터 고정된 크기의 메시지 조각으로만 다루지 않는다.

TCP 소켓에서 프로그램이 주고받는 연속된 데이터 흐름을 Stream(스트림)이라고 한다. 물이 이어져 흐르는 모습처럼 데이터가 이어진다는 뜻이다. 어디까지가 한 번의 메시지인지 애플리케이션이 약속을 정할 수 있고, 한 번의 읽기 동작이 보낸 한 번의 쓰기와 항상 정확히 일치한다고 가정해서는 안 된다.

하지만 링크가 한 번에 전달할 수 있는 패킷에는 최대 크기가 있다. 그래서 긴 Stream은 네트워크에서 전달할 수 있는 더 작은 단위들로 나뉘어 전송된다.

## MSS와 MTU

네트워크 링크가 한 번에 전달할 수 있는 IP 패킷의 최대 크기를 MTU(Maximum Transmission Unit)라고 한다. 이 단원의 기본 Ethernet 예에서는 MTU를 1,500바이트로 둔다. 이는 패킷이 반드시 1,500바이트라는 뜻이 아니라, 이보다 커지지 않아야 한다는 상한이다.

TCP에는 하나의 Segment에 실을 수 있는 데이터 크기의 기준인 MSS(Maximum Segment Size)가 있다. MSS는 TCP 데이터의 최대 크기이고, MTU는 IP 패킷 전체의 최대 크기이므로 둘은 같은 값이 아니다.

기본 IPv4와 TCP 헤더가 각각 20바이트이고 옵션이 없는 예라면 `1,500 - 20 - 20 = 1,460`바이트가 MSS가 된다. 실제 헤더 옵션이나 IP 버전 등 조건에 따라 달라질 수 있지만, 우선은 MTU가 바깥 IP 패킷의 상한이고 MSS가 TCP 데이터 조각의 상한이라는 점을 구별하자.

## Stream을 Segment로 나누기

하나의 Stream이 MSS보다 길면 TCP는 전달할 데이터를 MSS에 맞는 여러 조각으로 나눈다. 길이가 딱 나누어 떨어지지 않으면 마지막 조각은 앞의 조각보다 짧을 수 있다.

긴 Stream을 작은 조각들로 분할하는 과정을 Segmentation(세그멘테이션, 분할)이라고 한다. TCP가 이 과정을 거치면 각각의 조각에 TCP 헤더가 더해져 Segment가 된다.

예를 들어 파일 데이터가 4MB라고 해서 TCP가 이를 Segment 하나에 모두 넣지는 않는다. 링크의 MTU와 해당 연결의 MSS에 맞추어 여러 Segment로 나누어 보낸다. 수신 측 TCP는 이를 처리해 애플리케이션에 연속된 Stream으로 제공한다.

## Packet과 Frame으로 보내기

TCP Segment에는 TCP 헤더가 붙고, IP 계층은 그 전체를 페이로드로 담아 IP 헤더를 더해 Packet을 만든다. Ethernet 데이터 링크 계층은 IP 패킷을 페이로드로 받아 프레임 헤더와 오류 확인용 정보를 더해 Frame으로 감싼다.

MTU는 기본 예에서 IP 패킷의 최대 크기다. Ethernet 프레임에는 IP 패킷 바깥의 링크 헤더와 트레일러가 더해지므로, 프레임 전체 크기와 MTU를 같은 값으로 보면 안 된다. IP 패킷이 실제 링크로 나갈 때에는 그 링크에서 쓸 프레임에 담긴다.

TCP를 쓰는 예의 흐름은 `Stream → Segment → IP Packet → Ethernet Frame`이다. 계층 이름으로 기억하면 소켓은 Stream, TCP는 Segment와 MSS, IP는 Packet과 MTU, Ethernet 데이터 링크는 Frame을 다룬다. 물리 계층은 그 프레임을 비트와 신호로 전달한다.

## UDP Datagram과 용어 구별

TCP 소켓에서 다루는 Stream은 연속된 바이트 흐름이고, Segment는 TCP가 그 흐름을 나누어 전송하는 단위다. 애플리케이션이 다루는 메시지의 경계와 Segment의 경계는 항상 같지는 않다.

UDP는 TCP처럼 연결된 Stream을 제공하지 않는다. UDP에서 전송하는 하나의 데이터 덩어리는 Datagram(데이터그램)이라고 부른다. 계층별 단위를 정확히 말할 때 TCP의 L4 단위는 Segment, UDP의 L4 단위는 Datagram, IP의 L3 단위는 Packet이다.

실무나 대화에서는 세그먼트나 데이터그램을 포함해 전달 단위를 넓게 ‘패킷’이라고 부르는 경우도 있다. 하지만 계층의 역할을 설명하거나 TCP와 UDP를 비교할 때는 이름을 구별하면 혼동이 줄어든다. UDP 데이터그램도 IP 패킷의 페이로드에 담겨 전달된다.
