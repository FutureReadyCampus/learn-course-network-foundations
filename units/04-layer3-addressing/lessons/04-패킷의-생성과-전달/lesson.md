---
id: u4-l14-패킷의-생성과-전달
title: 패킷은 어떻게 목적지 프로그램까지 전달될까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-14.md
wiki_diagram: units/04-layer3-addressing/lessons/04-패킷의-생성과-전달/assets/diagrams/lesson-14.svg
page_metadata:
- terms:
  - 패킷 (packet)
  - 페이로드 (payload)
  - 헤더 (header)
  illustrations:
  - file: assets/animations/l14-daily-parcel-with-label.svg
    title: "책에 송장을 붙여 택배로 보낸다"
    alt: "아래에 철수의 집, 물류센터, 영희의 집이 있고 위쪽에 책이 놓입니다. 책 앞에 보내는 곳과 받는 곳이 적힌 송장이 붙고, 상자가 물류센터에서 받는 곳 주소를 확인한 뒤 영희의 집에 도착합니다."
    caption: "내용물은 책이고, 겉의 송장이 어디로 보낼지 알려 줍니다."
    after_paragraph: -1
  - file: assets/animations/l14-packet-header-payload.svg
    title: "패킷은 페이로드와 헤더로 이뤄진다"
    alt: "아래에 내 PC, 라우터, 서버가 있고 위쪽에 보낼 데이터인 페이로드가 놓입니다. 앞에 출발지 IP와 목적지 IP가 든 헤더가 붙고, 패킷이 라우터에서 목적지 IP를 확인한 뒤 서버에 도착합니다."
    caption: "이 Lesson의 패킷은 주로 L3의 IP 패킷입니다. 라우터는 헤더의 목적지 IP를 보고 다음 방향을 고릅니다."
    after_paragraph: 2
  questions:
  - id: u4-l14-p01-q01
    kind: choice
    difficulty: easy
    prompt: 택배 상자 안에 들어 있는 책은 네트워크에서 무엇에 해당하나요?
    choices:
    - id: a
      text: 송장
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 전달할 데이터
      feedback: 맞아요. 책처럼 실제로 보내려는 내용이 데이터예요.
    - id: c
      text: 라우터
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 포트 번호
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 네트워크 인터페이스
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: b
  - id: u4-l14-p01-q02
    kind: choice
    difficulty: easy
    prompt: 택배 송장은 네트워크의 어떤 부분과 가장 비슷한가요?
    choices:
    - id: a
      text: 페이로드
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 케이블
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 프로세스
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 헤더
      feedback: 맞아요. 송장처럼 헤더에는 전달에 필요한 정보가 담겨요.
    - id: e
      text: 소켓
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: d
  - id: u4-l14-p01-q03
    kind: choice
    difficulty: medium
    prompt: IP 패킷의 헤더와 페이로드를 바르게 구분한 것은 무엇인가요?
    choices:
    - id: a
      text: 헤더는 실제 내용이고 페이로드는 주소 정보다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 헤더에는 전달 정보가, 페이로드에는 전달할 내용이 담긴다
      feedback: 맞아요. 헤더는 전달에 필요한 정보를, 페이로드는 전달할 내용을 담아요.
    - id: c
      text: 둘 다 물리적인 포장 상자다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 페이로드는 항상 비어 있다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 헤더는 패킷을 받는 프로그램 이름만 담는다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: a
  - id: u4-l14-p01-q04
    kind: short
    prompt: 'L3에서 헤더와 페이로드를 함께 담아 전달하는 네트워크 단위를 무엇이라고 하나요?'
    answers:
    - IP packet
    - packet
    - IP 패킷
    feedback: IP 패킷은 IP 헤더와 페이로드를 담는 네트워크 계층의 단위예요.
  question_placements:
  - question_id: u4-l14-p01-q01
    after_paragraph: 1
  - question_id: u4-l14-p01-q02
    after_paragraph: 2
- terms:
  - 호스트 (host)
  - IP 주소 (IP address)
  - 포트 번호 (port number)
  illustrations:
  - file: assets/animations/l14-daily-building-and-unit.svg
    title: "건물 주소로 찾고 호수로 받을 사람 고르기"
    alt: "택배가 건물 주소를 보고 영희네 아파트에 도착합니다. 건물 안에 101호, 102호, 103호가 나타나고, 호수 103호를 보고 영희가 선택됩니다."
    caption: "주소는 건물까지, 호수는 건물 안의 수신자까지 찾아갑니다."
    after_paragraph: -1
  - file: assets/animations/l14-ip-host-port-program.svg
    title: "IP 주소로 호스트, 포트로 프로그램"
    alt: "패킷이 IP 주소를 보고 서버에 도착합니다. 서버 안에 웹 서버, 메신저, 게임 프로그램이 나타나고, 포트 443을 보고 웹 서버가 선택됩니다. 마지막에 포트는 물리적인 구멍이 아닌 숫자 표식이라고 표시됩니다."
    caption: "IP 주소는 호스트를, 포트 번호는 호스트 안에서 데이터를 받을 프로그램을 구분합니다. 포트 번호 중 443 외에는 예시예요."
    after_paragraph: 2
  questions:
  - id: u4-l14-p02-q01
    kind: choice
    difficulty: easy
    prompt: 택배의 집 주소처럼 IP 주소는 네트워크에서 무엇을 찾나요?
    choices:
    - id: a
      text: 그 안의 특정 프로그램
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 택배 기사
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 호스트(컴퓨터나 서버)
      feedback: 맞아요. IP 주소는 데이터를 받을 호스트를 찾아요.
    - id: d
      text: 운영체제의 커널
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: Ethernet 프레임
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: c
  - id: u4-l14-p02-q02
    kind: choice
    difficulty: easy
    prompt: 한 호스트 안에서 브라우저와 메신저를 따로 구별할 때 필요한 정보는 무엇인가요?
    choices:
    - id: a
      text: 집 주소만
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 화면 크기
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 전송 계층의 포트 번호
      feedback: 맞아요. 포트 번호는 호스트 안에서 받을 통신 프로그램을 구분하는 데 쓰여요.
    - id: d
      text: MAC 주소만
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 파일 이름
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: a
  - id: u4-l14-p02-q03
    kind: choice
    difficulty: medium
    prompt: IP 주소와 포트 번호의 역할을 바르게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 둘 다 호스트 자체만 찾는다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: IP 주소는 프로그램만, 포트는 네트워크 케이블만 찾는다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 포트 번호가 집 주소이고 IP 주소가 사람 이름이다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 둘 다 웹 페이지의 파일 경로다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: IP 주소는 호스트를, 포트 번호는 그 안의 수신 통신 끝점을 구분한다
      feedback: 맞아요. IP 주소로 호스트를 찾고 포트 번호로 그 안의 수신 통신 끝점을 구분해요.
    answer: e
  - id: u4-l14-p02-q04
    kind: short
    prompt: '네트워크에서 IP 주소가 가리키는 컴퓨터나 서버를 무엇이라고 하나요?'
    answers:
    - host
    - 호스트
    feedback: Host(호스트)는 IP 주소가 가리키는 컴퓨터나 서버예요.
  question_placements:
  - question_id: u4-l14-p02-q01
    after_paragraph: 1
  - question_id: u4-l14-p02-q02
    after_paragraph: 2
- terms:
  - 프로세스 (process)
  - 게이트웨이 (gateway)
  - 인터페이스 (interface)
  illustrations:
  - file: assets/animations/l14-daily-house-and-exit.svg
    title: "집 안의 철수에서 동네 밖으로"
    alt: "철수가 사는 집 안에서 현관문과 접수창구를 거쳐 다른 동네의 영희 집으로 이어지는 길이 있습니다. 집, 현관문, 처음 맡기는 곳이 차례로 강조되고, 같은 동네 이웃에게는 직접, 다른 동네에는 출구를 거쳐 간다고 표시됩니다."
    caption: "철수는 프로세스, 집은 호스트, 현관문은 인터페이스, 처음 맡기는 곳은 기본 게이트웨이에 해당합니다."
    after_paragraph: -1
  - file: assets/animations/l14-process-host-gateway.svg
    title: "프로세스에서 기본 게이트웨이까지"
    alt: "내 PC 안의 브라우저에서 네트워크 인터페이스를 거쳐 기본 게이트웨이와 다른 네트워크의 서버로 이어지는 길이 있습니다. 호스트, 인터페이스, 기본 게이트웨이가 차례로 강조되고, 같은 네트워크 장비에는 직접, 다른 네트워크에는 게이트웨이를 거쳐 간다고 표시됩니다."
    caption: "같은 네트워크 안의 목적지는 게이트웨이 없이 직접 전달되고, 다른 네트워크로 갈 때는 기본 게이트웨이로 먼저 보냅니다."
    after_paragraph: 3
  questions:
  - id: u4-l14-p03-q01
    kind: choice
    difficulty: easy
    prompt: 데이터를 만들거나 받아서 통신에 참여하는 브라우저 같은 프로그램은 무엇이라고 하나요?
    choices:
    - id: a
      text: 라우터
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 프레임
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 게이트웨이
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 프로세스
      feedback: 맞아요. 프로세스는 데이터를 만들거나 받는 실행 중인 프로그램이에요.
    - id: e
      text: 인터페이스
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: d
  - id: u4-l14-p03-q02
    kind: choice
    difficulty: easy
    prompt: 컴퓨터가 유선 또는 무선 네트워크에 실제로 연결되는 지점은 무엇인가요?
    choices:
    - id: a
      text: 기본 게이트웨이
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 포트 번호
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 네트워크 인터페이스
      feedback: 맞아요. 네트워크 인터페이스가 호스트를 유선 또는 무선 네트워크에 연결해요.
    - id: d
      text: IP 페이로드
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 수신 프로세스
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: a
  - id: u4-l14-p03-q03
    kind: choice
    difficulty: medium
    prompt: 목적지가 다른 네트워크에 있을 때 호스트가 패킷을 처음 보내는 라우터는 무엇인가요?
    choices:
    - id: a
      text: 목적지 호스트
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 수신 프로세스
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 기본 게이트웨이
      feedback: 맞아요. 기본 게이트웨이는 다른 네트워크로 나갈 때 패킷을 보내는 첫 라우터예요.
    - id: d
      text: DNS 이름
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: Ethernet 트레일러
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: c
  - id: u4-l14-p03-q04
    kind: short
    prompt: '다른 네트워크로 나갈 때 호스트가 패킷을 처음 보내는 라우터를 무엇이라고 하나요?'
    answers:
    - gateway
    - 기본 게이트웨이
    - 게이트웨이
    feedback: 기본 게이트웨이는 목적지가 다른 네트워크일 때 호스트가 패킷을 처음 보내는 라우터예요.
  question_placements:
  - question_id: u4-l14-p03-q01
    after_paragraph: 1
  - question_id: u4-l14-p03-q02
    after_paragraph: 2
- terms:
  - IP 주소 (IP address)
  - 임시 포트 (ephemeral port)
  illustrations:
  - file: assets/animations/l14-daily-record-both-ends.svg
    title: "접수 기록을 양쪽 끝으로 읽기"
    alt: "접수 기록 한 줄에 ‘철수 집 : 번호표 7’과 ‘영희 집 : 101호’가 화살표로 이어져 있습니다. 내 쪽은 집 주소와 번호표, 받는 쪽은 집 주소와 호수라고 강조되고, 마지막에는 번호표만 8로 바뀝니다."
    caption: "연결의 양쪽 끝은 각각 주소와 번호로 구별됩니다. 내 쪽 번호는 연결마다 달라질 수 있어요."
    after_paragraph: -1
  - file: assets/animations/l14-ip-port-both-ends.svg
    title: "IP 주소:포트 번호를 양쪽 끝으로 읽기"
    alt: "연결 목록 한 줄에 ‘192.0.2.15 : 51707’과 ‘203.0.113.20 : 443’이 화살표로 이어져 있습니다. 내 컴퓨터 쪽은 주소와 임시 포트, 서버 쪽은 주소와 보통 HTTPS를 뜻하는 443이라고 강조되고, 마지막에는 임시 포트만 51722로 바뀝니다."
    caption: "왼쪽은 내 컴퓨터, 오른쪽은 원격 호스트의 주소와 포트입니다. 숫자는 설명용 예시예요."
    after_paragraph: 2
  questions:
  - id: u4-l14-p04-q01
    kind: choice
    difficulty: easy
    prompt: 예시 `203.0.113.20:80`에서 `203.0.113.20`은 무엇을 찾는 값인가요?
    choices:
    - id: a
      text: 프레임 안의 위치
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 브라우저 탭
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 호스트
      feedback: 맞아요. 콜론 앞의 IP 주소는 데이터를 받을 호스트를 찾아요.
    - id: d
      text: 케이블
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 프로세스의 파일 이름
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: c
  - id: u4-l14-p04-q02
    kind: choice
    difficulty: easy
    prompt: 웹 연결에서 서버가 HTTPS 요청을 받을 때 흔히 쓰는 포트 번호는 무엇인가요?
    choices:
    - id: a
      text: '21'
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: '53'
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: '80'
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: '51707'
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: '443'
      feedback: 맞아요. HTTPS는 흔히 포트 443을 사용해요.
    answer: e
  - id: u4-l14-p04-q03
    kind: choice
    difficulty: medium
    prompt: 연결 목록 `192.0.2.15:51707 → 203.0.113.20:443`에서 원격 서버 끝점은 무엇인가요?
    choices:
    - id: a
      text: 192.0.2.15:51707
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 203.0.113.20:443
      feedback: 맞아요. 화살표 오른쪽의 IP와 포트가 원격 서버 쪽 끝점이에요.
    - id: c
      text: 51707만
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 192.0.2.15만
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 두 IP 주소를 더한 값
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: a
  question_placements:
  - question_id: u4-l14-p04-q01
    after_paragraph: 1
  - question_id: u4-l14-p04-q02
    after_paragraph: 2
- terms:
  - 소켓 (socket)
  illustrations:
  - file: assets/animations/l14-daily-service-windows.svg
    title: "접수 창구가 손님과 작업장을 잇는다"
    alt: "손님 가와 손님 나가 각자 창구 1, 창구 2를 통해 우체국 작업장과 트럭 출구에 이어져 있습니다. 손님이 트럭을 직접 다루지 못한다는 표시가 나오고, 짐이 창구를 거쳐 작업장에서 트럭으로 나갑니다. 답이 오면 짐이 손님 가의 창구로만 돌아옵니다."
    caption: "창구를 통해서만 작업장과 트럭을 쓰고, 돌아오는 짐은 맞는 창구로 갑니다."
    after_paragraph: -1
  - file: assets/animations/l14-socket-window.svg
    title: "소켓은 프로그램과 운영체제를 잇는 창구"
    alt: "브라우저와 메신저가 각자 소켓을 통해 운영체제와 네트워크 장치에 이어져 있습니다. 프로그램이 장치를 직접 다루지 못한다는 표시가 나오고, 요청이 소켓을 거쳐 커널의 TCP/IP 처리를 지나 장치로 나갑니다. 응답이 오면 브라우저의 소켓으로만 돌아옵니다."
    caption: "소켓은 포트 번호 자체가 아니라, 프로그램이 운영체제의 네트워크 기능을 쓰는 통신 창구입니다."
    after_paragraph: 2
  questions:
  - id: u4-l14-p05-q01
    kind: choice
    difficulty: easy
    prompt: 브라우저가 운영체제의 네트워크 기능을 이용해 데이터를 보내고 받는 창구는 무엇인가요?
    choices:
    - id: a
      text: 포트 번호
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 라우터
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 프레임
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 소켓
      feedback: 맞아요. 소켓은 프로그램과 운영체제의 네트워크 기능을 잇는 통신 창구예요.
    - id: e
      text: 게이트웨이
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: d
  - id: u4-l14-p05-q02
    kind: choice
    difficulty: easy
    prompt: 소켓에 대한 설명으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 소켓은 케이블의 다른 이름이다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 소켓은 포트 번호 하나만을 뜻한다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 소켓은 프로그램이 운영체제에 네트워크 입출력을 요청하는 인터페이스다
      feedback: 맞아요. 소켓은 프로그램이 운영체제의 네트워크 입출력을 이용하는 인터페이스예요.
    - id: d
      text: 소켓은 데이터를 암호화하는 알고리즘이다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 소켓은 라우터의 물리 포트다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: a
  - id: u4-l14-p05-q03
    kind: choice
    difficulty: medium
    prompt: 브라우저가 소켓으로 데이터를 넘긴 뒤 TCP/IP와 장치 처리를 맡는 운영체제의 핵심 부분은 무엇인가요?
    choices:
    - id: a
      text: 스위치
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 모니터
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 웹 페이지
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 임시 포트
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 커널
      feedback: 맞아요. 운영체제의 커널이 TCP/IP와 네트워크 장치 처리를 맡아요.
    answer: e
  - id: u4-l14-p05-q04
    kind: short
    prompt: '프로그램이 운영체제의 네트워크 입출력을 이용하는 통신 창구를 무엇이라고 하나요?'
    answers:
    - socket
    - 소켓
    feedback: Socket(소켓)은 프로그램과 운영체제의 네트워크 기능을 잇는 인터페이스예요.
  question_placements:
  - question_id: u4-l14-p05-q01
    after_paragraph: 1
  - question_id: u4-l14-p05-q02
    after_paragraph: 2
- terms:
  - 세그먼트 (segment)
  - 패킷 (packet)
  - 프레임 (frame)
  - 페이로드 (payload)
  illustrations:
  - file: assets/animations/l14-daily-layered-labels.svg
    title: "책에 겹겹이 정보를 붙여 간다"
    alt: "책 하나에서 시작해 호수 라벨이 붙은 작은 상자, 건물 주소가 붙은 중간 상자, 구간 라벨과 봉인 테이프가 붙은 큰 상자가 차례로 만들어집니다."
    caption: "겉으로 나올수록 정보가 더해져 더 큰 단위가 됩니다."
    after_paragraph: -1
  - file: assets/animations/l14-data-to-frame.svg
    title: "데이터에서 프레임까지 차례로 만든다"
    alt: "요청 데이터에서 시작해 TCP 헤더의 포트가 붙은 세그먼트, IP 주소가 붙은 IP 패킷, MAC 주소와 FCS가 붙은 프레임이 차례로 만들어집니다."
    caption: "TCP를 쓰는 예입니다. 한 계층에서 완성된 단위는 바깥 계층의 페이로드로 실려 갑니다."
    after_paragraph: 3
  questions:
  - id: u4-l14-p06-q01
    kind: choice
    difficulty: easy
    prompt: TCP가 포트 번호 같은 정보를 데이터에 붙여 만든 전송 계층 단위는 무엇인가요?
    choices:
    - id: a
      text: 프레임
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: IP 주소
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 게이트웨이
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 소켓
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 세그먼트
      feedback: 맞아요. TCP 헤더와 데이터가 합쳐져 세그먼트가 돼요.
    answer: e
  - id: u4-l14-p06-q02
    kind: choice
    difficulty: easy
    prompt: IP 헤더를 더해 만든 네트워크 계층 단위는 무엇인가요?
    choices:
    - id: a
      text: Ethernet 프레임
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 포트 번호
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: IP 패킷
      feedback: 맞아요. IP 헤더와 페이로드를 묶은 단위가 IP 패킷이에요.
    - id: d
      text: 네트워크 인터페이스
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 커널
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: b
  - id: u4-l14-p06-q03
    kind: choice
    difficulty: medium
    prompt: TCP를 쓰고 Ethernet 링크로 보낼 때의 캡슐화 순서는 무엇인가요?
    choices:
    - id: a
      text: 프레임 → 패킷 → 세그먼트 → 데이터
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 데이터 → 프레임 → 세그먼트 → IP 패킷
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: IP 패킷 → 데이터 → 프레임 → 세그먼트
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 데이터 → 세그먼트 → IP 패킷 → Ethernet 프레임
      feedback: 맞아요. 데이터에 TCP, IP, Ethernet 정보를 차례로 더해 세그먼트, 패킷, 프레임이 돼요.
    - id: e
      text: 세그먼트 → 프레임 → 데이터 → 패킷
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: d
  - id: u4-l14-p06-q04
    kind: short
    prompt: 'Ethernet 링크에서 같은 링크 안으로 전달할 때 사용하는 데이터 단위는 무엇인가요?'
    answers:
    - frame
    - 프레임
    feedback: Frame(프레임)은 데이터 링크에서 전달할 때 사용하는 단위예요.
  question_placements:
  - question_id: u4-l14-p06-q01
    after_paragraph: 2
  - question_id: u4-l14-p06-q02
    after_paragraph: 3
- terms:
  - L2 스위치 (L2 switch)
  - 라우터 (router)
  - 다음 홉 (next hop)
  - NAT (network address translation)
  illustrations:
  - file: assets/animations/l14-daily-whole-trip.svg
    title: "접수소와 물류센터를 거쳐 영희에게"
    alt: "철수의 집에서 동네 접수소와 물류센터를 지나 영희네 아파트에 도착하는 길이 있습니다. 접수소는 이번 구간 인수자를, 물류센터는 건물 주소를 확인하고, 아파트에 도착하면 호수에 맞는 창구로 영희에게 전달됩니다."
    caption: "각 곳은 자기가 맡은 정보만 확인하고, 건물 주소는 끝까지 그대로입니다."
    after_paragraph: -1
  - file: assets/animations/l14-whole-delivery.svg
    title: "스위치와 라우터를 거쳐 웹 서버까지"
    alt: "내 PC에서 스위치와 라우터를 지나 서버에 도착하는 길이 있습니다. 스위치는 목적지 MAC을, 라우터는 목적지 IP를 확인하고, 서버에서는 IP로 호스트를 찾은 뒤 포트와 소켓 정보로 웹 서버 프로세스에 전달됩니다."
    caption: "NAT가 없는 일반적인 예입니다. 목적지 IP는 그대로이고, 프레임과 MAC은 구간마다 새로 정해집니다."
    after_paragraph: 2
  questions:
  - id: u4-l14-p07-q01
    kind: choice
    difficulty: easy
    prompt: 현재 LAN 안에서 프레임의 목적지 MAC 주소를 보고 전달 방향을 정하는 장치는 무엇인가요?
    choices:
    - id: a
      text: 기본 게이트웨이
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 브라우저
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 커널
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: L2 스위치
      feedback: 맞아요. L2 스위치는 MAC 주소를 보고 현재 LAN 안에서 프레임을 전달해요.
    - id: e
      text: 수신 포트
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: d
  - id: u4-l14-p07-q02
    kind: choice
    difficulty: easy
    prompt: 다른 네트워크로 IP 패킷을 넘길 때 라우터가 고르는 다음 전달 경로의 다음 장비를 무엇이라고 하나요?
    choices:
    - id: a
      text: 페이로드
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 프로세스
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 다음 홉
      feedback: 맞아요. 라우터는 패킷을 넘길 다음 장비, 즉 다음 홉을 골라요.
    - id: d
      text: 임시 포트
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 소켓
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    answer: a
  - id: u4-l14-p07-q03
    kind: choice
    difficulty: medium
    prompt: NAT가 없을 때 라우터가 다음 링크로 전달하면서 바꿀 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: 모든 데이터의 내용을 지운다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: b
      text: 목적지 프로세스를 라우터의 프로세스로 바꾼다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: IP 패킷을 항상 Ethernet 프레임 하나에 영구 저장한다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: d
      text: 웹 페이지의 주소를 포트 번호로 바꾼다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 최종 목적지 IP 주소는 그대로 두고 다음 링크의 프레임과 MAC 주소를 바꾼다
      feedback: 맞아요. 각 링크의 프레임과 MAC 주소는 달라질 수 있지만, NAT가 없으면 최종 IP 목적지는 유지돼요.
    answer: e
  - id: u4-l14-p07-q04
    kind: short
    prompt: '사설 주소와 공인 주소 사이에서 IP 주소를 변환하는 기능을 무엇이라고 하나요?'
    answers:
    - NAT
    - network address translation
    - 네트워크 주소 변환
    feedback: NAT는 Network Address Translation, 즉 네트워크 주소 변환이에요.
  question_placements:
  - question_id: u4-l14-p07-q01
    after_paragraph: 1
  - question_id: u4-l14-p07-q02
    after_paragraph: 2
animations_dir: units/04-layer3-addressing/lessons/04-패킷의-생성과-전달/assets/animations
additional_sources:
- https://github.com/physical-spark/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/01-3.md
- https://github.com/physical-spark/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/04-1.md
---

웹 브라우저에서 사이트를 열면 요청은 브라우저 프로그램에서 출발해 서버 컴퓨터까지 가고, 그 안의 웹 서비스 프로그램에 도착해야 한다. IP 주소와 포트 번호는 각각 어디까지 찾는지 다르고, 소켓과 네트워크 계층은 프로그램의 데이터를 실제 링크로 내보내는 일을 이어 준다. 이 Lesson에서는 한 번의 웹 요청을 따라가며 데이터가 프로그램에서 프로그램까지 전달되는 과정을 살펴본다.

## 데이터와 전달 정보가 패킷에 담긴다

철수가 영희에게 책을 택배로 보낸다고 해 보자. 책은 상자 안에 들어가는 내용물이다. 네트워크에서 책에 해당하는 것은 실제로 보내려는 데이터다.

받는 주소와 보내는 주소는 겉에 붙이는 송장에 적는다. 네트워크에서도 데이터에 전달에 필요한 정보를 더한다. 계층 안에서 전달되는 실제 내용은 **페이로드(payload)**, 이를 어디로 어떻게 보낼지 해당 계층에 필요한 정보를 담은 부분은 **헤더(header)**라고 한다.

이 Lesson에서 패킷이라고 부를 때는 주로 인터넷 계층(L3)의 IP 패킷을 뜻한다. IP 패킷에는 전달할 페이로드와 출발지·목적지 IP 주소 등이 담긴 헤더가 있다. 보내는 컴퓨터는 최종 목적지의 IP 주소를 지정하고, 중간에 있는 라우터는 그 주소를 보고 다음 전달 방향을 고른다. 택배 송장이 최종 목적지를 알려 주는 것과 비슷하지만, 실제 네트워크 장비가 택배 기사처럼 움직인다는 뜻은 아니다.

## IP 주소로 호스트를 찾고 포트 번호로 프로그램을 구별한다

영희의 집에 도착한 택배가 있다고 해 보자. 집 주소는 택배가 어느 집으로 가야 하는지 알려 준다.

네트워크에서 IP 주소는 데이터를 받을 **호스트(host)**, 즉 컴퓨터나 서버를 찾는다. 하지만 한 호스트에는 웹 브라우저, 메신저, 게임처럼 여러 네트워크 프로그램이 함께 실행될 수 있다.

그 호스트 안에서 데이터를 받을 애플리케이션을 구분하는 데 TCP나 UDP의 **포트 번호(port number)**가 쓰인다. 택배 비유로 보면 IP 주소는 건물 주소이고, 포트 번호는 그 건물 안에서 전달할 수신자를 가리키는 표식에 가깝다. 포트는 컴퓨터에 난 물리적인 구멍도, 프로그램이 실행되는 방 번호도 아니다. 전송 계층 헤더에 기록되는 숫자이며, 운영체제는 주소와 포트 등의 정보를 이용해 알맞은 통신 끝점으로 데이터를 전달한다.

## 프로그램에서 네트워크 인터페이스까지 이어지는 역할

택배 비유의 요소를 네트워크에서 하는 일에 대응해 보자.

택배를 보내는 철수와 받는 영희처럼 **프로세스**는 데이터를 만들고 받는 프로그램이다. 택배 상자 속 책에 해당하는 것은 프로그램이 보내려는 **데이터**다.

택배를 받을 집처럼 **호스트**는 IP 주소가 가리키는 컴퓨터나 서버다. 집과 바깥길이 이어지는 지점처럼 **네트워크 인터페이스**는 호스트가 유선이나 무선 네트워크에 연결되는 지점이다.

다른 동네로 나갈 때 처음 맡기는 곳에 해당하는 **기본 게이트웨이**는 목적지가 다른 네트워크에 있을 때 호스트가 패킷을 보내는 첫 라우터다.

예를 들어 영희의 서버가 다른 네트워크에 있다면, 철수의 컴퓨터는 그 서버에 직접 닿는 대신 먼저 기본 게이트웨이로 패킷을 보낸다. 게이트웨이는 최종 목적지가 아니라 다음 네트워크로 나가는 출구다. 목적지가 같은 네트워크 안에 있으면 기본 게이트웨이를 거치지 않고, 같은 네트워크의 장비를 통해 전달된다. 택배 요소와 네트워크 역할은 이해를 돕기 위한 대응이며, 실제 주소 처리 방식이 택배와 같지는 않다.

## IP 주소와 포트 번호를 함께 읽기

IP 주소 뒤에 콜론과 포트 번호를 붙여 `IP 주소:포트 번호`처럼 적을 수 있다. 아래 애니메이션에서 `203.0.113.20`은 호스트를 찾는 IP 주소이고, `80`은 그 호스트에서 일반 웹(HTTP) 요청을 받을 프로그램을 가리킬 때 흔히 쓰는 포트 번호다.

암호화된 웹(HTTPS)을 받는 프로그램은 흔히 `443`번 포트를 사용한다. 이 번호들은 널리 쓰이는 약속이지만, 설정에 따라 다른 번호를 사용할 수도 있다.

예를 들어 연결 목록에 `192.0.2.15:51707 → 203.0.113.20:443`이 보인다면, 왼쪽은 내 컴퓨터 쪽 주소와 포트, 오른쪽은 원격 호스트의 주소와 포트다. 웹 브라우저 같은 클라이언트에는 통신할 때 임시 포트가 배정될 수 있고, 서버 쪽 `443`은 보통 HTTPS 서비스를 가리킨다. 이 숫자들이 모든 브라우저나 연결에서 늘 같다는 뜻은 아니다.

Windows에서는 리소스 모니터의 **네트워크** 탭에서 프로세스별 연결과 로컬·원격 주소 및 포트를 살펴볼 수 있다. 목록을 볼 때는 IP 주소가 호스트를, 그 뒤의 포트 번호가 해당 연결의 양쪽 끝점을 어떻게 구별하는지 찾아보자.

## 소켓은 프로그램과 운영체제를 잇는 통신 창구다

브라우저가 웹 요청을 보내려면 네트워크 장치의 세부 동작을 직접 처리하는 대신 운영체제에 네트워크 입출력을 요청한다.

이때 프로그램이 운영체제의 네트워크 기능을 이용하는 인터페이스가 **소켓(socket)**이다. 소켓은 포트 번호 그 자체도, 케이블이나 택배 상자도 아니다. 프로그램이 데이터를 보내고 받을 수 있도록 운영체제가 제공하는 통신 창구다.

예를 들어 브라우저가 소켓으로 요청 데이터를 운영체제에 넘기면, 운영체제의 핵심 제어부인 커널(kernel)이 TCP/IP와 네트워크 장치에 필요한 처리를 맡긴다. 응답이 돌아오면 운영체제는 연결 정보에 맞는 소켓을 통해 데이터를 브라우저에 전달한다. 같은 컴퓨터에서 브라우저와 메신저가 동시에 통신해도 각각의 연결을 구분할 수 있는 것은 소켓과 주소·포트 정보가 함께 쓰이기 때문이다.

## 데이터를 세그먼트와 패킷, 프레임으로 만들기

TCP를 사용하는 예에서 프로그램이 보낼 데이터를 소켓에 넘기면, 운영체제는 계층을 거치며 전달에 필요한 정보를 덧붙인다.

TCP는 포트 번호 등의 정보를 담은 헤더와 데이터를 묶어 **세그먼트(segment)**를 만든다. 인터넷 계층은 IP 주소 등을 담은 헤더를 더해 **IP 패킷(packet)**을 만든다.

Ethernet 링크를 사용하는 데이터 링크 계층은 같은 링크 안에서 전달하기 위한 헤더와 오류 확인용 트레일러를 더해 **프레임(frame)**을 만든다.

아래 애니메이션처럼 한 계층에서 완성된 단위 전체는 바깥 계층의 페이로드로 실릴 수 있다. 보낼 때의 순서는 `데이터 → 세그먼트 → IP 패킷 → Ethernet 프레임`이다. 받은 쪽은 바깥 프레임의 정보를 먼저 처리하고 안쪽 단위로 올라가며 데이터를 꺼낸다. 캡슐화와 역캡슐화의 자세한 원리는 앞 Lesson에서 살펴본 내용이다.

## 스위치와 라우터를 거쳐 목적지에 도착하기

이더넷 LAN을 지나는 예에서 프레임은 먼저 L2 스위치에 도착한다. 스위치는 프레임의 목적지 MAC 주소를 보고 현재 LAN 안에서 어느 쪽으로 전달할지 정한다.

목적지 호스트가 다른 네트워크에 있으면 라우터가 IP 패킷의 목적지 IP 주소를 확인해 패킷을 넘길 다음 경로, 즉 다음 홉(next hop)을 고른다.

라우터는 들어온 링크의 프레임 정보를 처리하고, 다음 링크에서 사용할 새 프레임에 IP 패킷을 다시 담아 보낸다. 사설 IP 주소와 공인 IP 주소처럼 주소를 바꾸는 NAT(네트워크 주소 변환)가 없는 일반적인 예에서는 최종 목적지 IP 주소는 유지되지만, 각 링크에서 쓰는 프레임과 그 MAC 주소는 다음 구간에 맞게 달라진다. 받는 호스트에 도착하면 IP 주소로 호스트를 찾고, 포트 번호와 소켓 정보에 따라 웹 서버 프로세스에 데이터를 전달한다.

전체 흐름을 연결하면 `브라우저 프로세스 → 소켓 → TCP 세그먼트 → IP 패킷 → Ethernet 프레임 → 스위치와 라우터 → 목적지 호스트 → 수신 소켓 → 웹 서버 프로세스`다. 요점은 IP 주소가 목적지 호스트를 찾고, 포트 번호는 그 호스트 안에서 데이터를 받을 통신 끝점을 구분하며, 각 네트워크 장비와 계층이 데이터를 다음 단계로 넘긴다는 것이다.
