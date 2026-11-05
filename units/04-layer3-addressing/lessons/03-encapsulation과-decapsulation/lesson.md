---
id: u4-l13-encapsulation과-decapsulation
title: '캡슐화와 역캡슐화: 보낼 때 감싸고 받을 때 풀기'
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-13.md
wiki_diagram: units/04-layer3-addressing/lessons/03-encapsulation과-decapsulation/assets/diagrams/lesson-13.svg
page_metadata:
- terms:
  - Encapsulation(캡슐화)
  - 헤더(Header)
  illustrations:
  - file: assets/animations/l13-daily-box-and-label.svg
    title: "상자에 넣고 송장을 붙인다"
    alt: "가운데 책 한 권이 있습니다. 책이 상자에 들어가고 겉면에 송장이 붙어 하나의 택배 상자가 됩니다. 마지막에 눈 모양이 송장만 살피고 상자를 열지 않은 채 다음 방향으로 보내는 표시가 나타납니다."
    caption: "책을 상자에 넣고 송장을 붙이면 송장만 보고 배달할 수 있어요."
    after_paragraph: -1
  - file: assets/animations/l13-header-makes-unit.svg
    title: "캡슐화는 정보를 더해 단위로 만든다"
    alt: "가운데 ‘안녕’ 데이터가 있습니다. 데이터 앞에 헤더가 붙고 둘이 하나의 전송 단위로 묶입니다. 마지막에 눈 모양이 헤더만 살피고 다음 방향으로 보내는 표시가 나타납니다."
    caption: "캡슐화는 데이터에 헤더를 더해 하나의 전송 단위로 만드는 일이에요. 실제 네트워크의 단위는 손에 잡히는 상자가 아니라 0과 1로 된 구조입니다."
    after_paragraph: 1
  questions:
  - id: u4-l13-p01-q01
    kind: choice
    difficulty: easy
    prompt: 택배 상자를 보내기 전에 겉면에 송장을 붙이는 까닭은 무엇인가요?
    choices:
    - id: a
      text: 상자를 더 무겁게 만들기 위해
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: 받는 곳과 배송에 필요한 정보를 알리기 위해
      feedback: 맞아요. 받는 곳과 배송에 필요한 정보를 알리기 위해
    - id: c
      text: 상자 안의 물건을 암호화하기 위해
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 상자를 여러 조각으로 나누기 위해
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 택배 상자에 인터넷 주소를 넣기 위해
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: b
  - id: u4-l13-p01-q02
    kind: choice
    difficulty: easy
    prompt: 택배 비유에서 네트워크의 Header(헤더)와 가장 비슷한 것은 무엇인가요?
    choices:
    - id: a
      text: 상자 안의 책
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: 상자를 붙이는 테이프
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: 상자 겉면의 송장
      feedback: 맞아요. 상자 겉면의 송장
    - id: d
      text: 택배를 나르는 트럭
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 책을 읽는 사람
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: c
  - id: u4-l13-p01-q03
    kind: choice
    difficulty: medium
    prompt: 캡슐화를 택배 포장에 비유할 때, 비유가 잘 보여 주는 핵심은 무엇인가요?
    choices:
    - id: a
      text: 내용에 필요한 정보를 더해 하나의 전송 단위로 만든다
      feedback: 맞아요. 내용에 필요한 정보를 더해 하나의 전송 단위로 만든다
    - id: b
      text: 포장만 하면 내용이 암호화된다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: 택배 상자는 항상 같은 크기다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 받는 사람이 배송 경로를 직접 정한다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 상자 안의 내용은 네트워크에서 사라진다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: a
  - id: u4-l13-p01-q04
    kind: short
    prompt: '보낼 데이터를 필요한 정보와 함께 하나의 전송 단위로 감싸는 과정을 무엇이라고 하나요?'
    answers:
    - Encapsulation
    - 캡슐화
    feedback: Encapsulation은 데이터를 필요한 정보와 함께 하나의 전송 단위로 만드는 과정이에요.
  question_placements:
  - question_id: u4-l13-p01-q01
    after_paragraph: 1
  - question_id: u4-l13-p01-q02
    after_paragraph: 2

- terms:
  - 캡슐화(Encapsulation)
  illustrations:
  - file: assets/animations/l13-daily-unit-boxes.svg
    title: "모양이 달라도 상자에 담으면 같은 단위"
    alt: "책, 꽃, 텐트처럼 모양이 다른 물건 세 개가 있습니다. 각각 송장이 붙은 같은 크기의 상자에 담기고, 상자들이 함께 한 줄로 이동합니다. 마지막에 상자 속 내용물이 그대로 보이고 자물쇠에 금지 표시가 붙어, 포장이 암호화가 아님을 보여 줍니다."
    caption: "포장은 다루기 쉬운 단위를 만들 뿐, 내용물을 숨기지는 않아요."
    after_paragraph: -1
  - file: assets/animations/l13-unit-not-encrypted.svg
    title: "헤더를 붙이면 같은 형식의 단위"
    alt: "문자, 사진, 영상처럼 종류가 다른 데이터 세 개가 있습니다. 각각 헤더가 붙은 같은 형식의 단위로 묶이고 함께 한 줄로 이동합니다. 마지막에 내용이 그대로 보이고 자물쇠에 금지 표시가 붙어, 캡슐화가 암호화가 아님을 보여 줍니다."
    caption: "캡슐화 자체는 내용을 숨기지 않아요. 보호하려면 암호화 같은 별도 기능이 필요합니다."
    after_paragraph: 2
  questions:
  - id: u4-l13-p02-q01
    kind: choice
    difficulty: easy
    prompt: 네트워크에서 각 계층의 헤더가 하는 일에 가까운 것은 무엇인가요?
    choices:
    - id: a
      text: 데이터를 암호화해 다른 사람이 읽지 못하게 한다
      feedback: 다시 생각해 보세요. 헤더는 정보를 숨기거나 암호화하지 않습니다.
    - id: b
      text: 다음 계층이 데이터를 처리하고 전달하는 데 필요한 정보를 제공한다
      feedback: 맞아요. 헤더에는 전달과 처리에 필요한 정보가 담깁니다.
    - id: c
      text: 네트워크 케이블
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 암호 키
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 라우터
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: b
  - id: u4-l13-p02-q02
    kind: choice
    difficulty: easy
    prompt: 헤더를 붙여 캡슐화하면 데이터가 자동으로 암호화되나요?
    choices:
    - id: a
      text: 네, 모든 헤더가 데이터를 숨겨요
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: 아니요. 캡슐화와 암호화는 다른 기능이에요
      feedback: 맞아요. 아니요. 캡슐화와 암호화는 다른 기능이에요
    - id: c
      text: 네, 단 패킷이 클 때만 그래요
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 아니요, 캡슐화하면 데이터가 삭제돼요
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 네, 라우터가 암호화해요
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: b
  - id: u4-l13-p02-q03
    kind: choice
    difficulty: medium
    prompt: 각 계층이 데이터를 캡슐화하는 이유로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 데이터를 암호화해 다른 사람이 내용을 읽지 못하게 한다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: 헤더를 더해 다음 계층이 필요한 정보를 확인하고 자기 역할을 하도록 한다
      feedback: 맞아요. 계층별 헤더가 있어 다음 계층이 필요한 처리와 전달을 할 수 있어요.
    - id: c
      text: 라우터가 목적지 컴퓨터의 화면을 직접 그리도록 한다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: IP 주소를 MAC 주소로 바꾼다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 전송 중 데이터가 손상되지 않도록 보장한다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: b
  question_placements:
  - question_id: u4-l13-p02-q01
    after_paragraph: 1
  - question_id: u4-l13-p02-q02
    after_paragraph: 2

- terms:
  - 세그먼트(Segment)
  - 패킷(Packet)
  - 프레임(Frame)
  - Payload(페이로드)
  illustrations:
  - file: assets/animations/l13-daily-boxes-nesting.svg
    title: "안쪽 상자부터 차례로 감싼다"
    alt: "가운데 책에서 시작해 작은 상자, 중간 상자, 큰 상자가 차례로 바깥을 감쌉니다. 상자마다 송장이 붙고, 가장 바깥 큰 상자에는 봉인 테이프도 붙습니다."
    caption: "안쪽부터 바깥으로 감싸고, 한 겹이 끝날 때마다 하나의 상자가 완성돼요."
    after_paragraph: -1
  - file: assets/animations/l13-frame-packet-segment.svg
    title: "프레임 안에 패킷, 패킷 안에 세그먼트"
    alt: "가운데 ‘안녕’ 데이터에서 시작해 TCP 헤더가 붙은 세그먼트, IP 헤더가 붙은 IP 패킷, 프레임 헤더와 FCS가 붙은 프레임이 차례로 바깥을 감쌉니다."
    caption: "L4에서 세그먼트, L3에서 IP 패킷, L2에서 프레임이 완성됩니다. 실제 필드와 크기는 프로토콜마다 달라요."
    after_paragraph: 2
  questions:
  - id: u4-l13-p03-q01
    kind: choice
    difficulty: easy
    prompt: TCP 헤더와 데이터가 합쳐져 전송 계층에서 하나의 단위가 되면 무엇이라고 부르나요?
    choices:
    - id: a
      text: 프레임
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: 패킷
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: 세그먼트
      feedback: 맞아요. 세그먼트
    - id: d
      text: 송장
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 라우트
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: c
  - id: u4-l13-p03-q02
    kind: choice
    difficulty: easy
    prompt: IP 헤더를 세그먼트에 붙이면 어떤 단위가 만들어지나요?
    choices:
    - id: a
      text: IP 패킷
      feedback: 맞아요. IP 패킷
    - id: b
      text: Ethernet 프레임
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: FCS
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 스트림
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: MAC 주소
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: a
  - id: u4-l13-p03-q03
    kind: choice
    difficulty: medium
    prompt: 보내는 쪽에서 데이터를 감싸는 순서를 바르게 나열한 것은 무엇인가요?
    choices:
    - id: a
      text: 프레임 → 패킷 → 세그먼트 → 데이터
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: 데이터 → 세그먼트 → 패킷 → 프레임
      feedback: 맞아요. 데이터 → 세그먼트 → 패킷 → 프레임
    - id: c
      text: 패킷 → 데이터 → 프레임 → 세그먼트
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 세그먼트 → 프레임 → 데이터 → 패킷
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 데이터 → 프레임 → 세그먼트 → 패킷
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: b
  - id: u4-l13-p03-q04
    kind: short
    prompt: 'TCP 헤더와 데이터를 합친 전송 계층의 단위를 무엇이라고 하나요?'
    answers:
    - Segment
    - 세그먼트
    feedback: Segment(세그먼트)는 TCP 헤더와 데이터로 이루어진 전송 계층의 단위예요.
  question_placements:
  - question_id: u4-l13-p03-q01
    after_paragraph: 1
  - question_id: u4-l13-p03-q02
    after_paragraph: 2
  page_id: u4l13-encapsulation-pdu-sequence
  video:
    video_id: Coxcs47ZQjE
    title: '[CCNA 입문 3-2강] OSI 7계층 vs TCP/IP 모델 완벽 비교｜데이터 캡슐화·PDU·역캡슐화 원리'
    creator: Network History
    duration_seconds: 629

- terms:
  - Decapsulation(디캡슐레이션, 역캡슐화)
  illustrations:
  - file: assets/animations/l13-daily-unwrapping.svg
    title: "바깥 상자부터 차례로 푼다"
    alt: "큰 상자가 도착해 송장과 봉인 테이프가 확인됩니다. 큰 상자가 사라지고 중간 상자의 송장이 확인되고, 다시 작은 상자의 송장이 확인된 뒤 책만 남아 전달됩니다."
    caption: "받는 쪽은 바깥 상자부터 풀고, 상자마다 자기 겉면의 송장만 확인해요."
    after_paragraph: -1
  - file: assets/animations/l13-decapsulation-order.svg
    title: "바깥 헤더부터 처리해 안쪽을 꺼낸다"
    alt: "프레임이 도착해 헤더와 FCS가 확인됩니다. 프레임이 벗겨지고 IP 헤더가 확인되고, 이어 세그먼트의 TCP 헤더가 확인된 뒤 데이터만 남아 전달됩니다."
    caption: "각 계층은 자기 계층의 헤더만 읽고 안쪽 단위를 다음 계층에 넘겨요."
    after_paragraph: 3
  questions:
  - id: u4-l13-p04-q01
    kind: choice
    difficulty: easy
    prompt: 프레임이 받는 쪽 네트워크 인터페이스에 도착하면 먼저 어느 쪽 정보부터 처리하나요?
    choices:
    - id: a
      text: 프레임의 바깥쪽 정보
      feedback: 맞아요. 프레임의 바깥쪽 정보
    - id: b
      text: 사용자 화면의 글자
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: TCP 데이터의 마지막 문장
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 파일 이름
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 웹페이지의 색상
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: a
  - id: u4-l13-p04-q02
    kind: choice
    difficulty: easy
    prompt: IP 계층이 목적지 IP 주소를 확인한 뒤 안쪽에서 다음으로 넘기는 것은 무엇인가요?
    choices:
    - id: a
      text: 프레임 트레일러만
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: TCP 세그먼트
      feedback: 맞아요. TCP 세그먼트
    - id: c
      text: 택배 송장
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: Wi-Fi 비밀번호
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 화면 픽셀
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: b
  - id: u4-l13-p04-q03
    kind: choice
    difficulty: medium
    prompt: 수신 측이 바깥 헤더를 처리하고 안쪽 데이터를 꺼내는 과정을 무엇이라고 하나요?
    choices:
    - id: a
      text: 캡슐화
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: 암호화
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: 역캡슐화
      feedback: 맞아요. 역캡슐화
    - id: d
      text: 단편화
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 주소 변환
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: c
  - id: u4-l13-p04-q04
    kind: short
    prompt: '받는 쪽에서 바깥 정보를 처리하며 안쪽 데이터를 꺼내는 과정의 이름은 무엇인가요?'
    answers:
    - Decapsulation
    - 역캡슐화
    - 디캡슐레이션
    feedback: Decapsulation(역캡슐화)은 바깥 정보를 처리하며 안쪽 단위를 꺼내는 과정이에요.
  question_placements:
  - question_id: u4-l13-p04-q01
    after_paragraph: 1
  - question_id: u4-l13-p04-q02
    after_paragraph: 2

- terms:
  - Encapsulation(캡슐화)
  - Decapsulation(역캡슐화)
  - Header(헤더)
  - Payload(페이로드)
  illustrations:
  - file: assets/animations/l13-daily-view-and-order.svg
    title: "누가 보느냐에 따라 달라지는 내용물"
    alt: "송장과 내용물로 이뤄진 중간 상자가 보입니다. 큰 상자의 송장과 봉인 테이프가 둘러싸면 중간 상자 전체가 큰 상자의 내용물이 됩니다. 이어 책에서 큰 상자까지 감싸는 순서와, 큰 상자에서 책까지 푸는 순서가 차례로 나타납니다."
    caption: "같은 상자도 보는 쪽에 따라 송장이 붙은 단위이거나 다른 상자의 내용물이 됩니다."
    after_paragraph: -1
  - file: assets/animations/l13-header-payload-by-layer.svg
    title: "헤더와 페이로드는 계층에 따라 달라진다"
    alt: "IP 헤더와 페이로드로 이뤄진 IP 패킷이 보입니다. 프레임 헤더와 FCS가 둘러싸면 IP 패킷 전체가 프레임의 페이로드가 됩니다. 이어 보낼 때는 데이터, 세그먼트, 패킷, 프레임 순서로, 받을 때는 그 반대 순서로 처리한다고 나타납니다."
    caption: "IP 패킷은 L3에서는 헤더와 페이로드를 가진 패킷이고, L2 프레임 안에서는 페이로드예요."
    after_paragraph: 2
  questions:
  - id: u4-l13-p05-q01
    kind: choice
    difficulty: easy
    prompt: 보내는 쪽은 데이터에 계층별 정보를 덧붙여 안쪽부터 바깥으로 감쌉니다. 이 과정을 무엇이라고 하나요?
    choices:
    - id: a
      text: 역캡슐화
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: 암호 해독
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: 캡슐화
      feedback: 맞아요. 캡슐화
    - id: d
      text: 응답 확인
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 주소 검색
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: c
  - id: u4-l13-p05-q02
    kind: choice
    difficulty: easy
    prompt: 한 계층에서 완성된 단위가 바깥 계층에서 실리는 자리가 될 수 있습니다. 그 자리를 무엇이라 하나요?
    choices:
    - id: a
      text: Payload(페이로드)
      feedback: 맞아요. Payload(페이로드)
    - id: b
      text: Header(헤더)
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: FCS
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 포트
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 라우팅 테이블
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: a
  - id: u4-l13-p05-q03
    kind: choice
    difficulty: medium
    prompt: IP 패킷은 L3와 L2에서 각각 어떤 역할로 볼 수 있나요?
    choices:
    - id: a
      text: L3에서는 프레임, L2에서는 세그먼트
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: L3에서는 패킷, L2에서는 프레임 헤더
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: L3에서는 완성된 패킷, L2 프레임 안에서는 Payload
      feedback: 맞아요. L3에서는 완성된 패킷, L2 프레임 안에서는 Payload
    - id: d
      text: 두 계층 모두에서 TCP 헤더
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: L3에서는 Payload, L2에서는 IP 헤더
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: c
  - id: u4-l13-p05-q04
    kind: short
    prompt: '바깥 계층의 단위 안에 실려 가는 내용을 부르는 말은 무엇인가요?'
    answers:
    - Payload
    - 페이로드
    feedback: Payload(페이로드)는 바깥 단위에 실려 가는 내용이에요.
  question_placements:
  - question_id: u4-l13-p05-q01
    after_paragraph: 1
  - question_id: u4-l13-p05-q02
    after_paragraph: 2

animations_dir: units/04-layer3-addressing/lessons/03-encapsulation과-decapsulation/assets/animations
additional_sources:
- https://github.com/physical-spark/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/01-3.md
---

보내는 쪽에서는 계층별 정보를 덧붙여 데이터를 감싸고, 받는 쪽에서는 바깥 정보를 확인하며 안쪽 데이터를 꺼낸다. 택배 포장과 마트료시카를 떠올리며 세그먼트, 패킷, 프레임이 어떻게 안팎으로 이어지는지 살펴보자.

## 택배 포장으로 이해하기

앞 Lesson에서는 IP 패킷이 전달 정보인 헤더와 실어 나르는 내용인 페이로드로 이루어진다는 점을 살펴봤다. 이번에는 그 패킷이 만들어져 링크를 건너기까지, 데이터에 바깥쪽 정보가 차례로 더해지는 과정을 본다.

책을 친구에게 보낼 때 책을 상자에 넣고 주소가 적힌 송장을 붙이면, 배달하는 사람은 책을 펼쳐 보지 않고도 어디로 보낼지 알 수 있다. 네트워크에서도 각 계층이 자기 역할에 필요한 헤더를 데이터 앞에 더해 다음 계층이 다룰 단위로 만든다. 이처럼 데이터를 계층별 정보로 감싸 전송 단위를 만드는 과정을 **캡슐화(Encapsulation)**라고 한다.

택배 상자는 실제 물건이지만 네트워크의 ‘상자’는 0과 1로 표현된 데이터 구조다. 다음 페이지부터 송신 측에서 각 헤더가 더해지는 순서를 하나씩 따라가 보자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 캡슐화는 각 계층이 필요한 헤더를 더해 전송 단위를 만드는 과정이다.
- **적용하기 (Apply):** 다음 페이지에서 각 헤더가 어떤 단위에 더해지는지 찾아본다.
- **찾아보기 (Lookup):** 각 계층의 PDU 명칭과 헤더는 이어지는 Page에서 확인한다.

## 캡슐화: 정보를 더해 전송 단위 만들기
<!-- learn-page-id: encapsulation-definition -->

택배 송장은 배달원이 상자를 어디로 보낼지 알려 준다. 네트워크 헤더도 각 계층에 필요한 처리·전달 정보를 담아, 다음 장치나 계층이 자기 역할을 할 수 있게 한다. 각 계층은 안쪽 데이터를 모두 해석하지 않고도 자기 헤더를 읽어 전송 단위로 다룰 수 있다.

여기서 포장은 보안과 다르다. 헤더를 붙였다고 내용이 숨겨지거나 암호화되는 것은 아니다. 헤더는 전달과 처리에 필요한 정보이고, 내용을 읽지 못하게 보호하려면 암호화 같은 별도 기능이 필요하다.

따라서 캡슐화의 핵심은 단순히 ‘상자 안에 넣기’가 아니다. **각 계층의 정보가 데이터에 차례로 더해져, 다음 계층이 자기 규칙에 따라 다룰 수 있는 단위가 된다**는 점이다. 다음 페이지에서 TCP·IP·Ethernet이 각자 어떤 헤더를 붙이는지 구체적으로 따라가 보자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 헤더는 각 계층이 데이터를 처리하고 전달하는 데 필요한 정보다.
- **적용하기 (Apply):** 헤더 추가와 암호화가 서로 다른 목적임을 구분한다.
- **찾아보기 (Lookup):** 계층별 헤더 필드와 길이는 해당 프로토콜 형식에서 찾아본다.

## 프레임 안에 패킷, 패킷 안에 세그먼트
<!-- learn-page-id: u4l13-encapsulation-pdu-sequence -->

노트북에서 웹 서버로 ‘안녕’이라는 데이터를 보낸다고 해 보자. 먼저 전송 계층(L4)에서 TCP 헤더를 데이터 앞에 붙인다. TCP 헤더와 데이터가 합쳐져 하나의 단위가 되며, 이를 세그먼트(Segment)라고 한다.

다음으로 인터넷 계층(L3)에서 세그먼트 앞에 IP 헤더를 붙인다. IP 헤더에는 보내는 호스트와 받을 호스트의 IP 주소 같은 정보가 담기며, 헤더와 세그먼트를 합친 단위가 IP 패킷(IP Packet)이다.

마지막으로 링크 계층(L2)에서 IP 패킷을 실을 프레임을 만든다. Ethernet 프레임에는 앞쪽 헤더와 뒤쪽의 **FCS(Frame Check Sequence, 오류 확인 값)**가 있고, 그 사이에 실린 IP 패킷 전체가 프레임의 페이로드(Payload)다. 즉, 바깥 프레임에서 보면 IP 헤더까지 포함한 IP 패킷이 통째로 내용물이다. 한 계층에서 완성된 단위가 바깥 계층에서는 페이로드가 될 수 있다.

위 애니메이션의 흐름을 글자로 펼쳐 보면 `프레임 헤더 | [IP 헤더 | TCP 헤더 | 안녕 데이터] | FCS`와 같다. 대괄호 안의 IP 패킷 전체가 Ethernet 프레임의 페이로드다. 실제 필드와 크기는 프로토콜에 따라 달라지므로, 이 모양은 각 계층의 포함 관계를 이해하기 위한 간단한 그림이다.

아래 영상은 **[참고용]**으로 가볍게 시청해 보자. OSI와 TCP/IP 모델 비교도 함께 다루므로, 여기서는 데이터·세그먼트·패킷·프레임이 안팎으로 이어지는 흐름만 살펴보면 된다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP Segment는 IP Packet 안에, IP Packet 전체는 Ethernet Frame의 Payload에 실린다.
- **적용하기 (Apply):** 송신 측 데이터를 Segment→Packet→Frame 순서로 구성해 본다.
- **찾아보기 (Lookup):** UDP를 쓸 때 달라지는 상위 단위 명칭은 Datagram Page에서 확인한다.

## 역캡슐화: 겉에서부터 정보를 처리하기
<!-- learn-page-id: decapsulation-definition -->

받는 쪽에서는 송신할 때의 순서를 거꾸로 따라간다. 이 예에서는 Ethernet 프레임 안에 IPv4 패킷이 있고, 그 패킷 안에 TCP 세그먼트가 있다고 하자.

| 받는 계층 | 확인하는 것 | 확인한 뒤 넘기는 것 |
|---|---|---|
| 링크 계층(L2) | 프레임 헤더와 FCS(오류 확인 값) | 프레임 바깥 정보를 처리하고 안의 IP 패킷을 넘긴다. |
| 인터넷 계층(L3) | IP 헤더의 목적지 주소와 다음에 처리할 프로토콜 정보(TCP 등) | IP 패킷 바깥을 처리하고 TCP 세그먼트를 넘긴다. |
| 전송 계층(L4) | TCP 헤더의 포트 등 연결 정보 | 해당 통신에 속한 데이터를 받을 프로그램 쪽으로 전달한다. |

FCS는 Ethernet 프레임의 비트가 구간에서 손상됐는지 확인하는 값이다. 손상된 프레임은 버려질 수 있지만, FCS가 내용을 고치거나 다시 보내 주지는 않는다. 각 계층은 자기 헤더를 처리하고 안쪽 단위를 다음 계층에 맡긴다. 링크 계층이 TCP 내용을 해석하거나 TCP가 프레임의 FCS를 확인하지는 않는다. 이처럼 수신 측에서 바깥 정보를 처리해 안쪽 데이터에 도달하는 과정을 **역캡슐화(Decapsulation)**라고 한다.

TCP가 전달한 데이터가 프로그램에서 어떤 순서와 크기로 읽히는지는 이 Unit의 Lesson 5에서 살펴본다. 여기서는 `프레임 → IP 패킷 → TCP 세그먼트 → 데이터` 순서로 바깥 포장을 처리한다는 점을 기억하자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 역캡슐화는 수신 측이 L2 프레임부터 L3 패킷, L4 세그먼트 순으로 처리하는 과정이다.
- **적용하기 (Apply):** 각 계층이 확인하는 정보와 다음 계층에 넘기는 단위를 말해 본다.
- **찾아보기 (Lookup):** 오류 확인과 헤더 제거 위치는 Ethernet/IP 처리 문서를 찾아본다.

## 헤더와 페이로드는 계층에 따라 달라진다

Header와 Payload는 데이터 종류가 늘 고정되어 있다는 뜻이 아니다. **어느 계층에서 바라보느냐에 따라, 안쪽 단위 전체가 바깥 계층의 Payload가 된다.** TCP over IPv4 over Ethernet이라는 이 Lesson의 예를 표로 정리해 보자.

| 계층 | 더하는 정보와 만드는 단위 | 그 계층에서 Payload가 되는 것 |
|---|---|---|
| 전송 계층(L4) | TCP 헤더 + 애플리케이션 데이터 = TCP 세그먼트 | 애플리케이션 데이터 |
| 인터넷 계층(L3) | IP 헤더 + TCP 세그먼트 = IP 패킷 | TCP 세그먼트 전체 |
| 링크 계층(L2) | 프레임 헤더 + IP 패킷 + FCS 트레일러 = Ethernet 프레임 | IP 패킷 전체 |

따라서 IP 패킷은 L3에서 보면 완성된 전달 단위이고, L2 프레임 안에 들어가면 페이로드다. 보낼 때는 `데이터 → 세그먼트 → 패킷 → 프레임`으로 감싸고, 받을 때는 `프레임 → 패킷 → 세그먼트 → 데이터` 순서로 각 계층이 자기 정보를 처리한다. 이번 Lesson의 핵심은 각 이름만 외우는 것이 아니라 이 안팎의 관계를 함께 보는 것이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP 세그먼트는 IP 패킷의 Payload이고, IP 패킷은 Ethernet 프레임의 Payload다.
- **적용하기 (Apply):** 표에서 특정 계층의 Payload가 무엇인지 가리킨다.
- **찾아보기 (Lookup):** 특정 계층의 Header/Payload 구분은 캡처 화면에서 확인한다.
