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
  - 단위화
  - 마트료시카
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
    prompt: 택배 직원이 겉면의 송장을 보고 배송 방향을 정할 때, 주로 다루는 것은 무엇인가요?
    choices:
    - id: a
      text: 더 작은 인형
      feedback: 맞아요. 더 작은 인형
    - id: b
      text: 택배 송장
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: c
      text: 네트워크 케이블
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 암호 키
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 라우터
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    answer: a
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
    prompt: 마트료시카 비유와 실제 네트워크 캡슐화의 차이를 바르게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 마트료시카는 안쪽부터 열지만 네트워크도 받을 때 안쪽부터 처리한다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: b
      text: 마트료시카는 처음부터 겹이 있지만 네트워크는 보내는 과정에서 계층별 정보를 덧붙인다
      feedback: 맞아요. 마트료시카는 처음부터 겹이 있지만 네트워크는 보내는 과정에서 계층별 정보를 덧붙인다
    - id: c
      text: 마트료시카는 암호화되어 있지만 네트워크 헤더는 항상 암호화된다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: d
      text: 두 경우 모두 실제로 데이터가 물리적 상자 안에 들어간다
      feedback: 다시 생각해 보세요. 본문에서 이 부분의 역할을 다시 확인해 보세요.
    - id: e
      text: 네트워크에서는 바깥 계층이 안쪽 데이터보다 먼저 만들어진다
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

친구에게 책 한 권을 택배로 보낸다고 해 보자. 책을 그냥 우체국 창구에 올려놓는 대신 상자에 넣고 테이프를 붙인 뒤, 겉면에 받는 사람의 이름과 주소를 적은 송장을 붙인다. 책은 크기와 모양이 제각각이지만, 상자에 넣고 송장을 붙이면 배달하는 사람에게는 ‘주소가 적힌 짐 하나’가 된다. 이제 내용물을 직접 살피지 않고도 어디로 보낼지 판단할 수 있다.

네트워크의 캡슐화(Encapsulation, 인캡슐레이션)도 보낼 데이터에 필요한 정보를 덧붙여 하나의 전송 단위로 만드는 일이다. 데이터가 택배의 책이라면, 데이터 앞에 붙는 헤더(Header)는 송장과 비슷하다. 다만 네트워크의 상자는 손에 잡히는 물체가 아니다. 0과 1로 표현된 데이터에 헤더 정보를 붙여 만든 구조다. 이 비유는 ‘내용에 정보를 더해 한 단위로 만든다’는 점을 이해하는 데 쓸 수 있다.

다만 네트워크의 상자는 손에 잡히는 물체가 아니다. 실제 동작과 다른 점은 뒤에서 함께 확인하자.

## 캡슐화: 정보를 더해 전송 단위 만들기

택배 상자를 받은 직원은 보통 상자를 열어 책 제목부터 확인하지 않는다. 겉면의 송장을 보고 어느 방향으로 보낼지 정한다. 바깥에서 다루는 것은 내용물 하나하나가 아니라 ‘송장이 붙은 상자’라는 단위다. 캡슐화에도 여러 정보를 하나의 덩어리로 묶어 다루기 쉽게 만드는 단위화의 의미가 있다.

여기서 포장과 보안을 혼동하지 말자. 상자를 포장했다고 해서 내용물이 암호화되어 아무도 읽을 수 없게 된 것은 아니다.

네트워크에서 헤더를 붙여 캡슐화하는 일도 그 자체로 내용을 숨기거나 암호화하지 않는다. 내용을 보호하려면 암호화 같은 별도의 기능이 필요하다.

겹겹이 들어 있는 러시아 목각 인형 마트료시카도 떠올려 보자. 큰 인형 하나를 열면 작은 인형이 나오고, 그것을 열면 더 작은 인형이 나온다. 바깥에서 보면 하나의 인형처럼 다루지만 안에는 다른 단위가 들어 있다. 네트워크에서도 안쪽의 데이터를 먼저 하나의 단위로 만들고, 그 단위에 바깥 계층의 정보를 덧붙여 감싼다.

마트료시카는 처음부터 겹이 만들어져 있는 물건이다. 네트워크 데이터는 송신 과정에서 계층을 거치며 바깥쪽 정보를 차례로 붙인다는 차이가 있다.

## 프레임 안에 패킷, 패킷 안에 세그먼트
<!-- learn-page-id: u4l13-encapsulation-pdu-sequence -->

노트북에서 웹 서버로 ‘안녕’이라는 데이터를 보낸다고 해 보자. 먼저 전송 계층(L4)에서 TCP 헤더를 데이터 앞에 붙인다. TCP 헤더와 데이터가 합쳐져 하나의 단위가 되며, 이를 세그먼트(Segment)라고 한다.

다음으로 인터넷 계층(L3)에서 세그먼트 앞에 IP 헤더를 붙인다. IP 헤더에는 보내는 호스트와 받을 호스트의 IP 주소 같은 정보가 담기며, 헤더와 세그먼트를 합친 단위가 IP 패킷(IP Packet)이다.

마지막으로 링크 계층(L2)에서 IP 패킷을 실을 프레임을 만든다. Ethernet 환경에서는 프레임 헤더가 앞에 붙고, 프레임 끝에는 오류를 확인하기 위한 FCS 같은 트레일러 정보도 붙는다. 이때 IP 패킷 전체가 프레임의 페이로드(Payload), 즉 프레임에 실려 가는 내용물이다. 따라서 한 계층에서 완성한 단위가 바깥 계층에서는 Payload가 될 수 있다. IP 패킷은 L3에서 완성된 단위이지만 L2에서 바라보면 프레임 안에 실리는 내용물이다.

위 애니메이션의 흐름을 글자로 펼쳐 보면 `프레임 헤더 | IP 헤더 | TCP 헤더 | 안녕 데이터 | 프레임 트레일러`처럼 생각할 수 있다. 실제 필드와 크기는 프로토콜에 따라 달라지므로, 이 모양은 각 계층의 관계를 이해하기 위한 간단한 그림이다.

아래 영상은 **[참고용]**으로 가볍게 시청해 보자. OSI와 TCP/IP 모델 비교도 함께 다루므로, 여기서는 데이터·세그먼트·패킷·프레임이 안팎으로 이어지는 흐름만 살펴보면 된다.

## 역캡슐화: 겉에서부터 정보를 처리하기

위 애니메이션처럼, 받는 쪽의 네트워크 인터페이스에 프레임이 도착하면 바깥에서 안쪽으로 확인한다. 먼저 링크 계층이 프레임의 정보를 살펴보고, Ethernet 프레임이라면 FCS로 전송 중 오류가 있었는지도 확인한다. 프레임 헤더와 트레일러를 처리하면 그 안에 실려 온 IP 패킷이 다음 계층으로 전달된다.

인터넷 계층은 IP 헤더를 읽어 목적지 IP 주소 등 자기 계층의 정보를 확인한 뒤, IP 패킷의 Payload인 TCP 세그먼트를 전송 계층에 넘긴다.

전송 계층은 TCP 헤더를 확인하고 그 뒤의 데이터를 꺼내 적절한 통신 상대에게 전달한다. 우체국 직원이 송장을 확인해 다음 목적지를 정하는 것처럼 각 계층은 자기 계층의 헤더를 읽는다. 링크 계층이 TCP 내용을 해석하거나 전송 계층이 프레임의 FCS를 확인하는 식은 아니다.

이처럼 바깥 정보를 처리한 뒤 안쪽 단위를 꺼내는 과정을 역캡슐화(Decapsulation, 디캡슐레이션)이라고 한다. 택배는 보통 상자를 열어야 책을 볼 수 있고, 네트워크도 바깥 계층의 정보를 처리해야 안쪽의 데이터에 도달한다.

한 가지 범위도 구분해 두자. TCP 데이터가 이어지는 흐름(Stream)처럼 다뤄지는 관점은 이 Unit의 Lesson 5에서 다시 살펴본다. 또한 실제 네트워크에서 OSI 5·6·7계층마다 똑같은 헤더를 하나씩 붙이는 것은 아니다. 지금은 여기서 본 L2 프레임, L3 패킷, L4 세그먼트가 바깥에서 안쪽으로 이어지는 흐름을 먼저 익히면 된다.

## 헤더와 페이로드는 계층에 따라 달라진다

보내는 쪽은 데이터를 가장 안쪽에 두고, 각 계층을 지날 때 자기 계층의 헤더를 붙여 바깥 단위로 감싼다. ‘안녕’ 데이터에 TCP 헤더를 붙이면 세그먼트가 되고, 세그먼트에 IP 헤더를 붙이면 패킷이 되며, IP 패킷을 프레임에 실으면 링크를 통해 보낼 수 있다. 이것이 Encapsulation이다.

받는 쪽은 반대 방향으로 처리한다. 프레임의 정보를 확인해 안의 IP 패킷을 꺼내고, IP 정보를 확인해 세그먼트를 꺼낸 뒤, TCP 정보를 확인해 데이터를 전달한다. 이것이 Decapsulation이다. 마트료시카처럼 보낼 때는 안쪽부터 바깥으로 감싸고, 받을 때는 바깥부터 안쪽으로 풀어 간다고 기억하면 된다.

Header와 Payload는 고정된 두 종류의 데이터가 아니라, 어느 계층에서 보느냐에 따라 달라지는 관계다. 한 계층에서 헤더와 Payload를 합쳐 완성한 단위가 바깥 계층으로 가면 통째로 Payload가 될 수 있다. 그래서 IP 패킷은 L3에서는 하나의 패킷이고, L2 프레임 안에서는 Payload다. 보낼 때는 `데이터 → 세그먼트 → 패킷 → 프레임` 순서로 감싼다.

받을 때는 `프레임 → 패킷 → 세그먼트 → 데이터` 순서로 꺼낸다는 두 방향을 함께 기억하자. 세부 필드는 각 프로토콜을 배우는 페이지에서 다시 살펴본다.
