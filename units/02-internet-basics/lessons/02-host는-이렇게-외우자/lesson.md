---
id: u2-l06-host는-이렇게-외우자
title: 통신에 참여하는 기기와 역할 구분하기
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-06.md
wiki_diagram: units/02-internet-basics/lessons/02-host는-이렇게-외우자/assets/diagrams/lesson-06.svg
page_metadata:
- terms:
  - 호스트(Host)
  - 워크스테이션(Workstation)
  inline_questions_after: 1
  questions:
  - id: u2-l06-p01-q01
    kind: choice
    difficulty: easy
    prompt: 집 Wi-Fi로 동영상을 보는 스마트폰도 Host일까요?
    choices:
    - id: a
      text: 네트워크와 연결되지 않은 책상
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 네. 네트워크로 데이터를 주고받으니 Host가 될 수 있어요.
      feedback: 맞아요. 네트워크를 통해 데이터를 주고받는 스마트폰.
    - id: c
      text: 전원이 꺼진 종이 상자
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 인터넷 선을 잇는 벽
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 와이파이 이름만 적힌 메모
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: b
  - id: u2-l06-p01-q02
    kind: choice
    difficulty: medium
    prompt: 워크스테이션이라는 이름은 Host인지 판단하는 기준일까요?
    choices:
    - id: a
      text: 컴퓨터의 크기가 큰가
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 네. 워크스테이션만 Host가 될 수 있어요.
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: 사용자 손에 들 수 있는가
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 아니요. 통신의 끝에서 데이터를 주고받는지가 기준이에요.
      feedback: 맞아요. 워크스테이션이라는 이름이나 성능이 아니라 통신에서 맡는 위치로 판단해요.
    - id: e
      text: 항상 서버 역할만 하는가
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: d
  - id: u2-l06-p01-q03
    kind: short
    prompt: 네트워크 통신의 끝에서 데이터를 주고받는 장치를 가리키는 말입니다. 어떤 개념일까요? (영어 단어로 답해주세요)
    answers:
    - Host
    - host
    feedback: 정답은 Host입니다. 스마트폰과 서버는 통신의 끝 장치이므로 Host가 될 수 있습니다.
  animations:
  - file: l06-host-connected.svg
    title: 모양이 달라도 모두 호스트
    alt: 스마트폰, 태블릿, 웹 서버, 워크스테이션이 한 줄로 놓여 있다가 아래의 네트워크 띠에 선으로 연결되고, 데이터 점이 기기 사이를 오간 뒤
      네 기기 위에 모두 호스트 꼬리표가 붙는 장면입니다. 마지막에 가장 작은 스마트폰과 고성능 워크스테이션이 함께 강조됩니다.
    caption: 모양과 크기가 달라도 네트워크 통신의 끝에서 데이터를 주고받는 장치라면 호스트가 될 수 있습니다. 워크스테이션이라는 이름이나 성능이 기준은 아닙니다.
- terms:
  - 스위치(Switch)
  - 인프라(Infrastructure)
  - L2 스위치
  - 네트워크 중간 장비
  inline_questions_after: 1
  questions:
  - id: u2-l06-p02-q01
    kind: choice
    difficulty: easy
    prompt: 같은 네트워크 안에서 여러 기기를 연결하는 중간 장비는 무엇인가요?
    choices:
    - id: a
      text: L2 스위치
      feedback: 맞아요. L2 스위치는 같은 네트워크 안에서 여러 기기를 연결하는 중간 장비예요.
    - id: b
      text: 네트워크를 통해 영상을 보는 스마트폰만
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: 웹 페이지를 요청하는 브라우저만
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 네트워크를 사용하지 않는 모든 컴퓨터
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 파일을 보내는 사용자만
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: a
  - id: u2-l06-p02-q02
    kind: choice
    difficulty: medium
    prompt: 노트북과 프린터 사이에 있는 L2 스위치는 어떤 일을 하나요?
    choices:
    - id: a
      text: 같은 네트워크의 기기들이 서로 통신하도록 연결해요.
      feedback: 맞아요. L2 스위치는 같은 네트워크 안의 기기들을 연결해요.
    - id: b
      text: 웹 페이지를 요청하는 브라우저 역할을 해요.
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: 네트워크 통신의 끝에서 데이터를 주고받아요.
      feedback: 이 설명은 통신의 끝 장치에 해당해요. 스위치는 중간에서 연결을 이어 줍니다.
    - id: d
      text: 서비스를 이용하는 스마트폰 역할을 해요.
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 파일을 출력하는 프린터 역할을 해요.
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: a
  - id: u2-l06-p02-q03
    kind: short
    prompt: 같은 네트워크 안에서 노트북과 프린터를 이어 주는 장비입니다. 무엇일까요? (영어 단어로 답해주세요)
    answers:
    - switch
    - l2 switch
    feedback: 정답은 L2 Switch입니다. 같은 네트워크 안의 기기들을 연결하는 중간 장비예요.
  animations:
  - file: l06-switch-infra.svg
    title: 네트워크의 중간 장비
    alt: PC 세 대와 프린터가 먼저 보이고, 그 위에 L2 스위치 두 대가 나타나 기기들을 잇습니다. 이어서 스위치들이 라우터로 모여 인터넷과 연결되고 데이터 점이 PC에서 인터넷까지 이동합니다. 마지막에 L2 스위치와 라우터는 중간 장비, PC와 프린터는 통신의 끝 장치로 구분됩니다.
    caption: L2 스위치는 같은 네트워크 안의 기기를 연결하고, 라우터는 네트워크 사이에서 패킷의 다음 방향을 고릅니다. 장비 종류는 다르지만 둘 다 단말 사이의 통신을 이어 주는 인프라 장비입니다.
- terms:
  - 엔드포인트(End point)
  - 단말·단말기
  inline_questions_after: 1
  questions:
  - id: u2-l06-p03-q01
    kind: choice
    difficulty: easy
    prompt: 다음 중 Endpoint에 해당하는 장치는 무엇인가요?
    choices:
    - id: a
      text: 서버에 연결된 전원 케이블만
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 네트워크 선로 중간의 커넥터
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: 작동하지 않는 공유기 상자
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 서비스를 이용하는 스마트폰이나 서비스를 제공하는 서버
      feedback: 맞아요. 서비스를 이용하는 스마트폰이나 서비스를 제공하는 서버.
    - id: e
      text: 네트워크 그림의 화살표
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: d
  - id: u2-l06-p03-q02
    kind: choice
    difficulty: medium
    prompt: Endpoint를 설명한 문장으로 가장 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 사용자 손에 들린 기기만 뜻하며 서버는 포함하지 않습니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 서비스를 이용하거나 제공하는 통신의 끝단 장치입니다
      feedback: 맞아요. 서비스를 이용하거나 제공하는 통신의 끝단 장치입니다.
    - id: c
      text: 네트워크에 연결된 모든 중간 장비만 뜻합니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 오직 무선으로 연결된 기기만 가리킵니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 패킷이 지나가는 케이블만 가리킵니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: b
  - id: u2-l06-p03-q03
    kind: short
    prompt: 네트워크 연결의 끝에서 서비스를 이용하거나 제공하는 장치를 가리킵니다. 어떤 개념일까요? (영어 단어로 답해주세요)
    answers:
    - endpoint
    - end point
    feedback: 정답은 Endpoint입니다. 스마트폰과 서비스를 제공하는 서버 모두 Endpoint가 될 수 있습니다.
  animations:
  - file: l06-endpoint-ends.svg
    title: 선의 끝에 있는 엔드포인트
    alt: 노트북, 스위치, 프린터가 한 줄로 연결되어 있습니다. 노트북에서 인쇄 요청 점이 스위치를 지나 프린터로 가고 프린터에서 종이가 나옵니다. 이어서 노트북과 프린터에 엔드포인트 꼬리표가, 스위치에는 중간 전달 꼬리표가 붙고, 마지막에 스위치가 흐려지며 양 끝이 강조됩니다.
    caption: 노트북은 인쇄를 요청하고 프린터는 출력합니다. 연결의 양 끝에서 서비스를 이용하거나 제공하는 두 기기가 엔드포인트이고, 중간 스위치는 요청을 전달할 뿐입니다.
- terms:
  - 클라이언트(Client)
  - 서버(Server)
  animations:
  - file: l06-client-server.svg
    title: 요청하는 쪽, 답하는 쪽
    alt: 왼쪽의 PC에서 오른쪽의 웹 서버로 요청 화살표가 가고, 서버에서 PC로 웹 페이지가 돌아오는 장면입니다.
    caption: 브라우저가 요청을 보내면 웹 서버가 답을 돌려줍니다. 요청하는 쪽이 클라이언트, 답하는 쪽이 서버입니다.
  inline_questions_after: 1
  questions:
  - id: u2-l06-p04-q01
    kind: choice
    difficulty: easy
    prompt: 브라우저에서 웹 페이지를 열어 달라고 요청하는 쪽은 무엇인가요?
    choices:
    - id: a
      text: 라우터
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 탭 스위치
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: Client
      feedback: 맞아요. Client.
    - id: d
      text: Aggregation Switch
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 인터넷 케이블
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: c
  - id: u2-l06-p04-q02
    kind: choice
    difficulty: medium
    prompt: Client와 Server를 구분하는 기준은 무엇인가요?
    choices:
    - id: a
      text: 기기의 크기와 가격
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 기기가 항상 맡는 고정된 종류
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: 유선인지 무선인지
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 컴퓨터가 만들어진 연도
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 통신에서 누가 요청하고 누가 응답을 제공하는지
      feedback: 맞아요. 통신에서 누가 요청하고 누가 응답을 제공하는지.
    answer: e
  - id: u2-l06-p04-q03
    kind: short
    prompt: 웹 요청에 응답해 페이지를 보내 주는 쪽의 역할입니다. 무엇일까요? (영어 단어로 답해주세요)
    answers:
    - server
    feedback: 정답은 Server입니다. Client가 요청하고 Server가 그 요청에 응답해요.
- terms:
  - P2P(Peer to Peer)
  - 피어(Peer)
  - 비트토렌트(BitTorrent)
  inline_questions_after: 1
  questions:
  - id: u2-l06-p05-q01
    kind: choice
    difficulty: easy
    prompt: P2P 방식의 참여자 Peer에 대한 설명은 무엇인가요?
    choices:
    - id: a
      text: 요청을 절대 보내지 않는 서버
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 라우터에만 붙이는 이름
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: 네트워크를 관찰하는 장비
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 항상 파일을 받기만 하는 컴퓨터
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 다른 참여자와 데이터를 주고받는 참여자
      feedback: 맞아요. 다른 참여자와 데이터를 주고받는 참여자.
    answer: e
  - id: u2-l06-p05-q02
    kind: choice
    difficulty: medium
    prompt: P2P 파일 공유에서 한 컴퓨터가 할 수 있는 일은 무엇인가요?
    choices:
    - id: a
      text: 파일을 보내기만 하고 받을 수는 없습니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 조각을 받으면서 이미 가진 조각을 다른 참여자에게 보낼 수도 있습니다
      feedback: 맞아요. 조각을 받으면서 이미 가진 조각을 다른 참여자에게 보낼 수도 있습니다.
    - id: c
      text: 반드시 웹 서버처럼 고정된 한 역할만 수행합니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 네트워크와 연결을 끊어야 데이터를 주고받습니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 모든 조각을 한 번에 직접 만들기만 합니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: b
  - id: u2-l06-p05-q03
    kind: short
    prompt: P2P 통신에서 데이터를 받기도 하고 다른 참여자에게 제공하기도 하는 참여자를 가리킵니다. 어떤 개념일까요? (영어 단어로 답해주세요)
    answers:
    - peer
    feedback: 정답은 Peer입니다. Peer는 상황에 따라 받는 역할과 보내는 역할을 모두 할 수 있습니다.
  animations:
  - file: l06-p2p-peers.svg
    title: 받으면서 나눠 주는 피어
    alt: 피어 A, 나, 피어 B 세 컴퓨터 아래에 파일 조각 1부터 4까지 칸이 있습니다. 처음에는 A가 1과 2, 나는 3, B는 4만 가지고 있습니다. 나는 A에게서 조각 1을, B에게서 조각 4를 받고, 이어서 내가 가진 조각 3을 A와 B에게 보냅니다. 마지막에 세 컴퓨터 모두에 피어 꼬리표가 붙고 나에게 받기 + 주기 표시가 붙습니다.
    caption: P2P에서는 참여자끼리 파일 조각을 직접 주고받습니다. 나는 없는 조각을 받는 동시에 가진 조각을 나눠 주므로, 받는 쪽이자 주는 쪽인 피어입니다.
- terms:
  - 라우터(Router)
  - IPS
  - 공유기
  inline_questions_after: 1
  questions:
  - id: u2-l06-p06-q01
    kind: choice
    difficulty: easy
    prompt: 서로 다른 네트워크 사이에서 패킷이 다음에 갈 방향을 정하는 장비는 무엇인가요?
    choices:
    - id: a
      text: 클라이언트
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 웹 서버
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: 라우터
      feedback: 맞아요. 라우터.
    - id: d
      text: 프린터
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 워크스테이션
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: c
  - id: u2-l06-p06-q02
    kind: choice
    difficulty: medium
    prompt: 라우터가 패킷을 전달할 때 본문에서 설명한 기준은 무엇인가요?
    choices:
    - id: a
      text: 목적지 IP 주소와 라우팅 정보
      feedback: 맞아요. 목적지 IP 주소와 라우팅 정보.
    - id: b
      text: 사용자의 키보드 종류
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: 파일 이름의 알파벳 순서
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 컴퓨터 화면의 크기
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 브라우저의 테마 색상
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: a
  - id: u2-l06-p06-q03
    kind: short
    prompt: 목적지 IP 주소를 보고 네트워크 사이에서 패킷이 다음으로 갈 방향을 정하는 장비입니다. 어떤 개념일까요? (영어 단어로 답해주세요)
    answers:
    - router
    feedback: 정답은 Router입니다. 라우터는 라우팅 정보에 따라 패킷의 다음 방향을 선택합니다.
  animations:
  - file: l06-router-next-hop.svg
    title: 다음 길을 고르는 라우터
    alt: 노트북에서 목적지 203.0.113.5가 적힌 패킷이 라우터로 갑니다. 라우터 아래 라우팅 정보 표에서 203.0.113.x는 B망이라는 줄이 강조되고, 패킷은 A망, B망, C망 세 갈래 중 B망 쪽 연결로 나가 B망에 도착합니다. 마지막에 라우터 위에 L3 장비 꼬리표가 붙습니다.
    caption: 라우터는 패킷의 목적지 IP를 라우팅 정보와 맞춰 보고 다음에 보낼 연결을 고릅니다. IP가 L3 정보이므로 라우터를 대표적인 L3 장비라고 부릅니다.
- terms:
  - 탭 스위치(Tap Switch)
  - 애그리게이션 스위치(Aggregation Switch)
  - 관리 목적
  inline_questions_after: 1
  questions:
  - id: u2-l06-p07-q01
    kind: choice
    difficulty: easy
    prompt: 네트워크 문제를 살펴볼 때 Tap Switch가 분석 장비에 보내는 것은 무엇인가요?
    choices:
    - id: a
      text: 사용자 대신 웹 페이지를 작성하기 위해
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 보안·분석 장비가 네트워크 흐름을 관찰하도록 하기 위해
      feedback: 맞아요. 보안·분석 장비가 네트워크 흐름을 관찰하도록 하기 위해.
    - id: c
      text: IP 주소를 모두 지우기 위해
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 컴퓨터의 화면을 공유하기 위해
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: 모든 연결을 무선으로 바꾸기 위해
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: b
  - id: u2-l06-p07-q02
    kind: choice
    difficulty: medium
    prompt: Tap Switch와 Aggregation Switch의 역할을 바르게 짝지은 것은 무엇인가요?
    choices:
    - id: a
      text: 탭은 여러 연결을 모으고, 애그리게이션은 트래픽을 복사해 관찰합니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 둘 다 웹 요청을 시작하는 클라이언트입니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: 둘 다 네트워크에 연결된 스마트폰입니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: 탭은 관찰할 트래픽을 복사하고, 애그리게이션은 여러 연결을 모읍니다
      feedback: 맞아요. 탭은 관찰할 트래픽을 복사하고, 애그리게이션은 여러 연결을 모읍니다.
    - id: e
      text: 탭은 IP 목적지를 정하고, 애그리게이션은 응답을 작성합니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: d
  - id: u2-l06-p07-q03
    kind: choice
    difficulty: medium
    prompt: 이 페이지의 특수 장비에서 우선 기억할 내용은 무엇인가요?
    choices:
    - id: a
      text: 장비 모델과 세부 설정값을 모두 외우기
      feedback: 지금은 세부 설정을 외울 필요가 없어요. 장비가 어떤 일을 하는지 연결해 보세요.
    - id: b
      text: Tap은 관찰할 트래픽을 복사하고, Aggregation은 여러 연결을 모아요.
      feedback: 맞아요. 각 장비의 용도를 알아두고, 세부 내용은 필요할 때 찾아보면 됩니다.
    - id: c
      text: 두 장비 모두 웹 페이지 요청을 시작해요.
      feedback: 다시 살펴보세요. 이 장비들은 사용자 요청을 보내는 Client가 아니에요.
    - id: d
      text: Tap은 IP 주소를 정하고, Aggregation은 응답을 보내요.
      feedback: 다시 살펴보세요. 두 장비의 용도와 맞지 않아요.
    - id: e
      text: 두 장비의 이름만 외우면 역할은 몰라도 돼요.
      feedback: 이름만 외우기보다 각각 무엇을 하는지 알아두세요.
    answer: b
  animations:
  - file: l06-tap-aggregation.svg
    title: 탭은 복사, 애그리게이션은 모으기
    alt: 화면 왼쪽에서는 PC와 라우터 사이의 흐름이 탭을 지나가고, 탭에서 복사본 점이 아래 분석 장비로 내려갑니다. 오른쪽에서는 1층, 2층, 3층 스위치의 연결이 애그리게이션 스위치로 모인 뒤 상위 장비로 올라갑니다. 마지막에 왼쪽에는 관찰용 흐름 복사, 오른쪽에는 여러 연결 모으기 꼬리표가 붙습니다.
    caption: 탭 스위치는 지나가는 트래픽의 복사본을 보안·분석 장비로 보내 흐름을 관찰하게 하고, 애그리게이션 스위치는 여러 구간의 연결을 모아 상위 장비로 잇습니다. 둘 다 인프라 쪽 장비입니다.
- terms: []
  animations:
  - file: l06-host-roles.svg
    title: Host, Endpoint, Client/Server
    alt: 노트북과 웹 서버는 통신의 끝 장치로, 가운데 공유기는 패킷을 전달하는 라우터로 표시됩니다. 노트북에는 Host와 Endpoint, 요청을 시작하는 Client 꼬리표가 붙고, 서버에는 Host와 Endpoint, 응답을 제공하는 Server 꼬리표가 붙습니다.
    caption: Host는 통신의 끝에 있는 장치이고, Endpoint는 특정 통신의 한쪽 끝을 가리킵니다. Client와 Server는 그 통신에서 요청을 시작하고 응답을 제공하는 역할입니다. 가운데 라우터는 패킷을 다음 네트워크로 전달합니다.
  inline_questions_after: 1
  questions:
  - id: u2-l06-p08-q01
    kind: choice
    difficulty: easy
    prompt: 노트북에서 웹 사이트를 열 때 노트북에 붙을 수 있는 이름은 무엇인가요?
    choices:
    - id: a
      text: Client만 해당하고 Host나 Endpoint는 아닙니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: Router와 Tap Switch
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: Server와 Aggregation Switch
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: d
      text: Host이지만 통신 역할은 맡지 않습니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: Host이자 Endpoint이며 요청을 보내는 Client
      feedback: 맞아요. Host이자 Endpoint이며 요청을 보내는 Client.
    answer: e
  - id: u2-l06-p08-q02
    kind: choice
    difficulty: medium
    prompt: 한 기기에 Host, Endpoint, Client 같은 이름이 함께 붙어도 모순이 아닌 이유는 무엇인가요?
    choices:
    - id: a
      text: 기기가 여러 대로 복제되기 때문입니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: b
      text: 그 이름들이 같은 기준으로 같은 일을 뜻하기 때문입니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: c
      text: Host는 장치 종류, Endpoint는 특정 통신의 끝, Client는 요청 역할을 가리키기 때문입니다
      feedback: 맞아요. Host는 장치 종류, Endpoint는 특정 통신의 끝, Client/Server는 그 통신의 요청·응답 역할을 가리켜요.
    - id: d
      text: 기기는 항상 네트워크 장비이기 때문입니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    - id: e
      text: Host라는 이름은 컴퓨터의 성능만 나타내기 때문입니다
      feedback: 다시 생각해 보세요. 본문에서 설명한 기준을 확인해 보세요.
    answer: c
  - id: u2-l06-p08-q03
    kind: short
    prompt: 웹 사이트를 보던 노트북이 다른 기기에 파일을 제공한다면, 새 통신에서 맡을 수 있는 역할은 무엇인가요? (영어 단어로 답해주세요)
    answers:
    - server
    feedback: 정답은 Server입니다. Client와 Server는 기기에 고정된 이름이 아니라 통신에서 맡는 역할이에요.
animations_dir: units/02-internet-basics/lessons/02-host는-이렇게-외우자/assets/animations
---
통신에 참여하는 기기를 부르는 말과, 기기가 통신에서 맡는 역할을 구분해 봅니다.

## Host · 통신의 끝에서 데이터를 주고받는 장치

Host(호스트)는 네트워크 통신의 끝에서 데이터를 보내거나 받는 장치입니다. 스마트폰으로 동영상을 보거나 서버에서 파일을 내려받을 때, 스마트폰과 서버 모두 Host가 될 수 있습니다. 컴퓨터의 크기나 성능, ‘워크스테이션’ 같은 이름으로 정하지 않습니다.

**기억할 말:** Host는 통신의 끝 장치입니다. 노트북과 웹 서버는 통신의 양 끝에 있으므로 둘 다 Host가 될 수 있습니다.

## Switch · 같은 네트워크의 기기를 연결하는 장비

L2 스위치는 같은 네트워크 안에서 노트북, 프린터 같은 기기들이 서로 통신하도록 연결합니다. 스위치는 통신의 끝에서 서비스를 이용하는 기기가 아니라, 중간에서 연결을 이어 주는 장비입니다.

스위치와 라우터를 구분해 보세요. 스위치는 같은 네트워크 안의 기기들을 연결하고, 라우터는 서로 다른 네트워크 사이에서 패킷이 다음에 갈 방향을 고릅니다. 둘 다 중간에서 통신을 돕는 인프라 장비입니다.

## Endpoint · 특정 통신의 한쪽 끝

Endpoint(엔드포인트)는 특정 통신의 한쪽 끝에 있는 장치입니다. 노트북에서 네트워크 프린터로 인쇄를 요청하면 노트북과 프린터가 각각 Endpoint이고, 사이의 스위치는 Endpoint가 아닙니다.

Host는 통신의 끝 장치를 가리키고, Endpoint는 특정 통신에서 어느 쪽 끝에 있는지를 가리킵니다. 웹 서버도 서비스를 제공하는 통신의 한쪽 끝이므로 Endpoint가 될 수 있습니다. **기억할 말:** Endpoint는 특정 통신의 한쪽 끝입니다.

## Client와 Server · 요청하는 쪽과 응답하는 쪽

노트북에서 웹 페이지를 열면 브라우저가 페이지를 요청합니다. 요청하는 쪽이 Client(클라이언트), 요청을 받아 페이지를 제공하는 쪽이 Server(서버)입니다.

이 이름은 기기의 종류가 아니라 통신에서 맡는 역할입니다. 같은 노트북도 웹 사이트를 볼 때는 Client이고, 다른 기기에 파일을 제공할 때는 Server가 될 수 있습니다.

**기억할 말:** Client는 요청하고 Server는 응답합니다. 어떤 기기인지보다 이번 통신에서 누가 요청하고 응답하는지 살펴보세요.

## Peer · 받으면서 나누는 참여자

P2P(Peer to Peer) 파일 공유에서는 참여자끼리 파일 조각을 직접 주고받습니다. 내 컴퓨터가 없는 조각을 내려받는 동시에, 이미 가진 조각을 다른 참여자에게 보낼 수 있습니다. 이렇게 보내기도 하고 받기도 하는 참여자를 Peer(피어)라고 합니다.

웹 접속에서는 보통 Client가 요청하고 Server가 응답하지만, P2P에서는 한 참여자가 상황에 따라 받는 쪽도, 보내는 쪽도 될 수 있습니다. 모든 참여자가 항상 같은 양을 주고받는다는 뜻은 아닙니다. **기억할 말:** Peer는 P2P에서 데이터를 주고받는 참여자입니다.

## Router · 네트워크 사이에서 다음 방향을 고르는 장비

Router(라우터)는 목적지 IP 주소와 경로 정보를 보고 패킷을 어느 네트워크 쪽으로 보낼지 고릅니다. L2 스위치가 같은 네트워크 안을 연결한다면, 라우터는 서로 다른 네트워크를 잇습니다.

집에서 쓰는 공유기는 보통 Wi-Fi 연결과 라우터 기능을 한 장비에 함께 담습니다. 지금은 라우팅 표나 경로를 계산하는 세부 방법보다, **라우터는 네트워크 사이에서 다음 방향을 고른다**는 점을 기억하세요. 자세한 라우팅은 뒤에서 다시 배웁니다.

## 특수 장비 · 지금은 용도만 알아두기

Tap Switch와 Aggregation Switch는 모두 네트워크 인프라 장비입니다. 세부 모델이나 설정을 외우기보다, 무엇을 하는지 연결해 두세요.

Tap Switch는 지나가는 트래픽의 복사본을 분석 장비에 보내 관찰하게 합니다. Aggregation Switch는 여러 네트워크 연결을 모아 상위 장비로 이어 줍니다. 장애나 보안 문제를 살필 때 Tap의 용도를, 여러 연결을 모을 때 Aggregation의 용도를 찾아보면 됩니다.

## 한 기기에 여러 이름이 붙는 이유

노트북으로 웹 사이트를 열면 노트북은 통신의 끝 장치인 Host이고, 해당 통신의 한쪽 끝인 Endpoint입니다. 요청을 보내는 동안에는 Client 역할을 합니다. 웹 서버도 Host이자 Endpoint이며, 응답을 제공하는 Server 역할을 합니다. 두 장비 사이의 스위치와 라우터는 통신을 잇는 중간 장비입니다.

각 이름은 서로 다른 질문에 답합니다.

- **Host:** 통신의 끝에서 데이터를 주고받는 장치인가?
- **Endpoint:** 특정 통신의 어느 한쪽 끝인가?
- **Client / Server:** 누가 요청하고 누가 응답하는가?
- **Peer:** P2P에서 데이터를 주고받는 참여자인가?

기기 하나에 여러 이름이 붙어도 괜찮습니다. 노트북은 Host이면서 Endpoint이고, 웹 페이지를 요청할 때 Client입니다. 같은 노트북이 파일을 제공하는 다른 통신에서는 Server 역할도 할 수 있습니다.
