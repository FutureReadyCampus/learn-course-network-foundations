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
    answer: b
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
    - id: d
      text: MAC 주소만
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: 파일 이름
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 전송 계층의 포트 번호
      feedback: 맞아요. 포트 번호는 호스트 안에서 받을 통신 프로그램을 구분하는 데 쓰여요.
    answer: c
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
    - id: e
      text: IP 주소는 호스트를, 포트 번호는 그 안의 수신 통신 끝점을 구분한다
      feedback: 맞아요. IP 주소로 호스트를 찾고 포트 번호로 그 안의 수신 통신 끝점을 구분해요.
    - id: d
      text: 둘 다 웹 페이지의 파일 경로다
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
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
  - 기본 게이트웨이 (default gateway)
  - 라우터 (router)
  illustrations:
  - file: assets/animations/l14-process-host-gateway.svg
    title: "기본 게이트웨이를 거쳐 다른 네트워크로"
    alt: "내 PC의 네트워크 인터페이스에서 기본 게이트웨이 라우터를 거쳐 다른 네트워크의 서버로 이어집니다. 같은 네트워크의 장비는 직접 전달하고, 다른 네트워크의 장비는 기본 게이트웨이를 먼저 거칩니다."
    caption: "기본 게이트웨이는 다른 네트워크로 나갈 때 호스트가 처음 패킷을 맡기는 라우터입니다."
    after_paragraph: 3
  questions:
  - id: u4-l14-gateway-p03-q01
    kind: choice
    difficulty: easy
    prompt: 기본 게이트웨이란 무엇인가요?
    choices:
    - id: a
      text: 내 컴퓨터에서 실행 중인 웹 브라우저
      feedback: 브라우저는 데이터를 주고받는 프로그램이에요. 게이트웨이는 네트워크 사이에서 패킷을 전달하는 라우터예요.
    - id: b
      text: 다른 네트워크로 갈 때 호스트가 먼저 패킷을 보내는 라우터의 주소
      feedback: 맞아요. 기본 게이트웨이는 다른 네트워크로 나갈 때 처음 거치는 라우터의 주소예요.
    - id: c
      text: 인터넷에 있는 최종 서버의 주소
      feedback: 최종 서버는 목적지예요. 게이트웨이는 그곳으로 가는 길에서 먼저 거치는 라우터예요.
    - id: d
      text: 웹사이트 이름을 IP 주소로 바꾸는 DNS 서버
      feedback: DNS는 이름에 대응하는 IP 주소를 찾고, 게이트웨이는 다른 네트워크로 패킷을 전달해요.
    - id: e
      text: 같은 네트워크에 있는 L2 스위치
      feedback: 스위치는 LAN 안에서 프레임을 전달해요. 기본 게이트웨이는 다른 네트워크로 패킷을 전달하는 라우터예요.
    answer: b
  - id: u4-l14-gateway-p03-q02
    kind: choice
    difficulty: easy
    prompt: PC `192.168.0.10/24`가 다른 네트워크의 서버에 보낼 때, `192.168.0.1`이 기본 게이트웨이라면 먼저 누구에게 보내나요?
    choices:
    - id: a
      text: 목적지 서버에 직접
      feedback: 다른 네트워크의 서버에는 현재 LAN에서 직접 닿을 수 없어요. 먼저 기본 게이트웨이에 맡겨요.
    - id: c
      text: 같은 LAN의 아무 PC에나
      feedback: 다른 PC가 목적지 경로를 대신 찾아 주지는 않아요. 기본 게이트웨이에 전달해요.
    - id: d
      text: DNS 서버에 패킷 전체를
      feedback: DNS는 이름 찾기를 돕지만 다른 네트워크로 패킷을 전달하는 라우터는 아니에요.
    - id: e
      text: 인터넷의 모든 라우터에 동시에
      feedback: 호스트는 패킷을 모든 라우터에 보내지 않아요. 먼저 기본 게이트웨이에 전달해요.
    - id: b
      text: 기본 게이트웨이 `192.168.0.1`에
      feedback: 맞아요. 호스트는 목적지 서버로 가는 패킷을 먼저 기본 게이트웨이에 전달해요.
    answer: b
  - id: u4-l14-gateway-p03-q03
    kind: choice
    difficulty: medium
    prompt: PC가 다른 네트워크의 서버로 Ethernet 프레임을 보낼 때, 두 주소는 어떻게 되나요?
    choices:
    - id: a
      text: IP 목적지와 프레임 목적지 MAC 모두 최종 서버를 가리킨다
      feedback: 첫 링크에서 프레임은 같은 LAN에 있는 게이트웨이로 전달돼요. 서버는 아직 Ethernet으로 직접 닿지 않아요.
    - id: b
      text: IP 목적지는 최종 서버이고, 프레임 목적지 MAC은 기본 게이트웨이다
      feedback: 맞아요. IP 패킷은 최종 서버를 계속 가리키고, 첫 Ethernet 프레임은 다음 홉인 게이트웨이에 전달돼요.
    - id: c
      text: IP 목적지는 기본 게이트웨이로 바뀌고, 프레임 목적지 MAC은 서버를 가리킨다
      feedback: 게이트웨이는 패킷의 최종 목적지로 바뀌지 않아요. 첫 프레임만 게이트웨이의 MAC 주소를 목적지로 해요.
    - id: d
      text: 두 주소 모두 DNS 서버를 가리킨다
      feedback: DNS는 이름 찾기 역할이에요. 여기서는 최종 서버의 IP와 첫 홉 라우터의 MAC을 구분해야 해요.
    - id: e
      text: IP 목적지는 게이트웨이이고, 프레임 목적지 MAC은 최종 서버다
      feedback: IP 패킷은 최종 서버를 가리켜요. 첫 Ethernet 프레임은 게이트웨이의 MAC 주소를 목적지로 해요.
    answer: b
  question_placements:
  - question_id: u4-l14-gateway-p03-q01
    after_paragraph: 1
  - question_id: u4-l14-gateway-p03-q02
    after_paragraph: 2
  - question_id: u4-l14-gateway-p03-q03
    after_paragraph: 3
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
    answer: c
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
    - id: d
      text: DNS 이름
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: e
      text: Ethernet 트레일러
      feedback: 다시 생각해 보세요. 본문에서 각 정보와 장치의 역할을 다시 확인해 보세요.
    - id: c
      text: 기본 게이트웨이
      feedback: 맞아요. 기본 게이트웨이는 다른 네트워크로 나갈 때 패킷을 보내는 첫 라우터예요.
    answer: c
  - id: u4-l14-p03-q04
    kind: choice
    difficulty: easy
    prompt: "PC가 192.168.0.10/24이고 기본 게이트웨이가 192.168.0.1입니다. 같은 /24 네트워크의 PC 192.168.0.25로 보낼 때는 어디로 전달하나요?"
    choices:
    - id: a
      text: "기본 게이트웨이 192.168.0.1로 먼저 보낸다"
      feedback: "같은 /24 네트워크 안의 목적지라면 게이트웨이를 거칠 필요가 없어요."
    - id: b
      text: "목적지 PC로 직접 보낸다"
      feedback: "맞아요. 두 주소의 첫 24비트가 같으므로 같은 네트워크에 있어요. PC는 같은 LAN에서 목적지 PC로 직접 전달합니다."
    - id: c
      text: "DNS 서버 8.8.8.8로 보낸다"
      feedback: "DNS는 도메인 이름에 대응하는 IP 주소를 찾는 역할이에요. 같은 네트워크 안의 목적지 전달을 대신하지 않아요."
    - id: d
      text: "인터넷의 모든 라우터에 복사해 보낸다"
      feedback: "패킷을 모든 라우터에 복사하지 않아요. 같은 네트워크 안이면 목적지 장치로 직접 전달합니다."
    - id: e
      text: "전송하지 않는다"
      feedback: "두 주소의 첫 24비트가 같아 같은 네트워크에 있어요. PC는 목적지로 직접 보낼 수 있습니다."
    answer: b
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
    prompt: 예시 `203.0.113.20:443`에서 `203.0.113.20`은 무엇을 찾는 값인가요?
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
    answer: b
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
    answer: c
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
    answer: c
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
    answer: c
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

앞 Lesson 2와 3에서는 데이터가 헤더와 함께 IP 패킷으로 전달되는 모양을 살펴봤다. 이제는 그 패킷이 **보내는 프로그램에서 출발해 받는 프로그램까지 어떻게 전달되는지** 따라가 보자.

친구에게 책을 보낼 때, 보내는 사람이 택배 트럭을 몰고 여러 도시의 길을 직접 찾아다니지는 않는다. 주소를 적은 상자를 택배사에 맡기면 물류센터와 배송 담당자가 각자 맡은 구간을 이어서 운반한다. 네트워크에서도 프로그램은 데이터를 운영체제의 네트워크 기능에 맡기고, 컴퓨터와 중간 장비가 각자 맡은 전달 작업을 한다.

이 Lesson에서 패킷이라고 부를 때는 주로 인터넷 계층(L3)의 **IP 패킷**을 뜻한다. IP 헤더에는 출발지와 최종 목적지의 IP 주소가 담기며, 라우터는 목적지 주소를 보고 다음에 보낼 방향을 고른다. 택배의 주소가 전체 목적지를 알려 주는 것과 비슷하다. 이후 페이지에서 목적지 컴퓨터 안의 수신 프로그램을 찾는 방법까지 이어서 살펴본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 보내는 프로그램은 네트워크 경로를 직접 운전하지 않고 운영체제의 네트워크 기능에 전달을 맡긴다.
- **적용하기 (Apply):** IP 패킷의 목적지 주소를 보고 라우터가 다음 방향을 고르는 이유를 설명한다.
- **찾아보기 (Lookup):** IP 주소와 포트가 수신 프로그램까지 이어지는 흐름은 다음 페이지에서 확인한다.

## IP 주소로 호스트를 찾고 포트 번호로 프로그램을 구별한다
<!-- learn-page-id: port-definition -->

택배가 영희의 집에 도착했다고 해 보자. **집 주소만으로는 집 안에서 누가 받을 물건인지 알 수 없다.** 컴퓨터도 마찬가지다. IP 주소로 데이터를 받을 호스트(host), 즉 컴퓨터나 서버를 찾더라도 그 안에는 브라우저, 메신저, 게임처럼 네트워크를 사용하는 프로그램이 여럿 실행될 수 있다.

그래서 TCP나 UDP는 헤더에 **포트 번호(port number)**를 담아 목적지 호스트 안의 통신 끝점을 구분하는 데 사용한다. 운영체제는 목적지 IP 주소와 전송 계층의 포트 정보를 함께 보고 알맞은 통신에 데이터를 전달한다. 여러 프로그램이 같은 컴퓨터에서 통신하더라도 각 연결은 자기 통신 정보에 따라 구분된다.

택배 비유로 보면 IP 주소는 건물 주소이고 포트 번호는 건물 안에서 받을 곳을 가리키는 표식에 가깝다. 다만 실제 포트 번호는 사람 이름이나 방 번호가 아니라, TCP/UDP 통신을 구분하기 위해 쓰이는 숫자다. 스위치에 케이블을 꽂는 물리 포트와도 다르다. 포트 번호 하나만으로 모든 통신이 구별되는 것은 아니며, 운영체제는 IP 주소와 TCP/UDP 같은 프로토콜 정보도 함께 사용한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** IP 주소는 받을 호스트를, TCP/UDP 포트 정보는 그 호스트 안의 통신 끝점을 찾는 데 쓰인다.
- **적용하기 (Apply):** 한 컴퓨터에서 브라우저와 메신저가 통신할 때 왜 목적지 IP 정보만으로는 충분하지 않은지 설명한다.
- **찾아보기 (Lookup):** 등록 포트 번호와 예외 사용은 IANA 목록에서 찾아본다.

## 기본 게이트웨이는 다른 네트워크로 나가는 첫 라우터다
<!-- learn-page-id: default-gateway-definition -->

**게이트웨이(gateway)**는 서로 다른 네트워크 사이에서 데이터를 전달하는 출입구 역할을 하는 장치나 연결 지점을 말한다. 컴퓨터의 네트워크 설정에서 말하는 **기본 게이트웨이(default gateway)**는 더 구체적으로, 목적지가 내 네트워크 바깥에 있을 때 컴퓨터가 먼저 패킷을 보내도록 설정된 라우터의 주소다. 가정에서는 흔히 공유기의 LAN 쪽 주소가 기본 게이트웨이로 설정된다.

컴퓨터는 자기 IP 주소와 `/24` 같은 네트워크 경계를 이용해 목적지가 같은 네트워크 안에 있는지 살핀다. 여기서 ‘직접 전달’은 **라우터나 기본 게이트웨이를 거치지 않는다**는 뜻이다. Ethernet 프레임은 여전히 스위치나 Wi-Fi 공유기를 거쳐 목적지 장치까지 갈 수 있다.

예를 들어 IP 주소가 `192.168.0.10/24`인 PC가 `192.168.0.25` 또는 다른 네트워크의 서버로 데이터를 보낸다고 하자.

| 목적지 | IP 패킷의 목적지 IP | 첫 Ethernet 프레임의 목적지 MAC | 첫 구간에서 하는 일 |
|---|---|---|---|
| 같은 `/24` 네트워크의 PC | `192.168.0.25` | 받는 PC의 MAC 주소 | 스위치나 Wi-Fi 장비가 로컬 네트워크 안에서 전달한다. |
| 다른 네트워크의 서버 | 서버의 IP 주소 | 기본 게이트웨이 `192.168.0.1`의 MAC 주소 | 라우터가 패킷을 받아 다음 네트워크 쪽으로 전달한다. |

여기서 **첫 경유지와 최종 목적지를 구분**해야 한다. 원격 서버로 보내는 경우에도 IP 패킷의 목적지 IP는 서버를 가리킨다. 첫 Ethernet 프레임의 목적지 MAC만 같은 LAN에 있는 기본 게이트웨이의 MAC으로 설정한다. 게이트웨이는 목적지 서버가 아니라, 서버를 향해 다음 구간으로 보내 주는 라우터다.

기본 게이트웨이는 마법처럼 인터넷 전체를 해결하는 장치가 아니다. 호스트가 목적지 네트워크로 가는 더 구체적인 경로를 갖고 있지 않을 때 사용하는 기본 출구다. DHCP를 사용하면 컴퓨터는 IP 주소와 함께 기본 게이트웨이 주소도 자동으로 받을 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 기본 게이트웨이는 목적지가 로컬 네트워크 밖일 때 먼저 패킷을 맡기는 라우터다.
- **적용하기 (Apply):** 로컬 주소와 원격 주소를 비교해 게이트웨이가 필요한 경우를 판별한다.
- **찾아보기 (Lookup):** 게이트웨이 주소를 찾는 방법은 OS 네트워크 설정에서 확인한다.

## 프로그램에서 네트워크 인터페이스까지 이어지는 역할

여러 개념을 한 컴퓨터 안팎의 역할로 정리해 보자.

| 요소 | 네트워크에서 하는 일 | 예 |
|---|---|---|
| 프로세스 | 데이터를 만들거나 받아 사용하는 실행 중인 프로그램 | 브라우저, 메신저 |
| 호스트 | 프로세스와 네트워크 기능이 동작하는 컴퓨터나 서버 | 노트북, 웹 서버 |
| 네트워크 인터페이스 | 호스트를 특정 유선·무선 링크에 연결하는 장치 | Wi-Fi 어댑터, Ethernet 어댑터 |
| 기본 게이트웨이 | 다른 네트워크로 나갈 때 호스트가 처음 패킷을 맡기는 라우터 | 가정용 공유기의 LAN 쪽 주소 |

이 요소들은 서로 같은 종류의 주소나 장치가 아니다. 한 호스트에는 Wi-Fi와 유선 Ethernet처럼 여러 네트워크 인터페이스가 있을 수 있고, 각 인터페이스는 자기 MAC 주소와 네트워크 설정에 따른 IP 주소를 가진다. 그래서 ‘호스트의 IP 주소’라고 간단히 말하더라도, 실제 설정에서는 IP 주소가 특정 인터페이스에 구성되는 경우가 일반적이다.

보내는 프로그램은 데이터를 운영체제의 네트워크 기능에 맡긴다. 운영체제는 목적지에 맞는 인터페이스와 다음 전달 지점을 정하고, 네트워크 인터페이스가 프레임을 링크로 내보낸다. 원격 네트워크로 향하는 첫 구간에서는 기본 게이트웨이가 다음 담당자다. 이 Page는 역할 지도를 보여 주며, 소켓·포장·라우터의 세부 동작은 뒤 페이지에서 이어서 본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 프로세스는 프로그램, 호스트는 컴퓨터, 네트워크 인터페이스는 그 컴퓨터의 연결 지점이다.
- **적용하기 (Apply):** Wi-Fi와 Ethernet을 모두 쓰는 노트북에서 인터페이스가 둘일 수 있는 이유를 설명한다.
- **찾아보기 (Lookup):** 운영체제가 보낼 인터페이스와 다음 경유지를 고르는 흐름은 뒤 페이지에서 확인한다.

## IP 주소와 포트 번호를 함께 읽기

IPv4 주소는 뒤에 콜론과 포트 번호를 붙여 `IP 주소:포트 번호`처럼 적을 수 있다. 아래 애니메이션의 `203.0.113.20:443`은 문서와 예시에 쓰도록 따로 마련된 서버 주소와 포트의 조합이다. `443`은 HTTPS를 제공할 때 흔히 사용하는 포트 번호다.

일반 웹(HTTP)은 흔히 `80`번 포트, 암호화된 웹(HTTPS)은 흔히 `443`번 포트에서 제공된다. `80`과 `443`은 널리 쓰이는 기본 약속이지, 포트 번호가 프로토콜을 강제로 결정하는 것은 아니다. 서버 관리자는 다른 포트 번호를 설정할 수도 있다.

예를 들어 `192.0.2.15:51707 → 203.0.113.20:443`은 내 컴퓨터에서 서버로 향하는 한 연결을 나타낸다. `192.0.2.15`도 문서용 예시 주소이며, 브라우저 같은 클라이언트는 연결을 시작할 때 운영체제가 정한 **임시 포트(ephemeral port)**를 사용할 수 있다. 여기서는 `51707`이 그 값이고, 서버 쪽 `443`은 흔히 HTTPS에 사용하는 포트다. 서버가 답장을 보낼 때는 방향이 반대가 되어 `203.0.113.20:443 → 192.0.2.15:51707`로 돌아온다. 실제 숫자는 연결마다 달라질 수 있다.

Windows에서는 리소스 모니터의 **네트워크** 탭에서 프로세스별 연결을 살펴볼 수 있다. `로컬 주소`와 `로컬 포트`는 내 컴퓨터 쪽, `원격 주소`와 `원격 포트`는 상대 서버 쪽 정보다. 이 예시의 화살표 방향과 연결 목록의 로컬·원격 구분을 함께 읽어 보자.

여기서는 IPv4 표기만 사용했다. IPv6 주소에는 콜론이 이미 들어가므로 보통 `[2001:db8::1]:443`처럼 대괄호로 주소와 포트를 구분한다. 지금은 IPv4 예시에서 주소와 포트가 함께 한쪽 통신 끝을 나타낸다는 점에 집중하자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** `IP:Port`는 한 통신의 주소와 포트를 함께 적는 IPv4 표기다.
- **적용하기 (Apply):** 연결 예에서 로컬/원격 주소·포트와 요청/응답 방향을 구분한다.
- **찾아보기 (Lookup):** 80·443은 흔한 기본값이지만 서버 설정을 실제 환경에서 확인한다.

## 소켓은 프로그램과 운영체제를 잇는 통신 창구다

브라우저가 웹 요청을 보내려면 네트워크 장치의 세부 동작을 직접 처리하는 대신 운영체제에 네트워크 입출력을 요청한다.

이때 프로그램이 운영체제의 네트워크 기능을 이용하는 인터페이스가 **소켓(socket)**이다. 소켓은 포트 번호 그 자체도, 케이블이나 택배 상자도 아니다. 프로그램이 데이터를 보내고 받을 수 있도록 운영체제가 제공하는 통신 창구다.

예를 들어 브라우저가 소켓을 통해 요청 데이터를 운영체제(Windows, macOS, Linux 등)에 넘기면, 운영체제의 핵심부인 **커널(kernel)**이 TCP/IP 규칙에 맞게 처리하고 네트워크 장치에 전달한다. 응답이 돌아오면 운영체제는 연결 정보와 맞는 소켓을 통해 데이터를 브라우저에 전달한다. 같은 컴퓨터에서 브라우저와 메신저가 동시에 통신해도 운영체제가 각각의 소켓과 주소·포트 정보를 이용해 알맞은 통신으로 나눌 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Socket은 프로그램이 운영체제 네트워크 기능을 사용하는 인터페이스다.
- **적용하기 (Apply):** 브라우저가 소켓으로 요청을 보내는 흐름과 Port 자체를 구분한다.
- **찾아보기 (Lookup):** 소켓 API 사용법은 사용하는 언어와 OS 문서에서 찾아본다.

## 포트·IP·MAC 정보는 각 계층 헤더에 담긴다

브라우저가 원격 웹 서버로 TCP 요청을 보낸다고 하자. 앞 페이지에서 본 `192.0.2.15:51707 → 203.0.113.20:443` 연결의 데이터가 소켓에 전달되면, 운영체제는 각 계층에서 필요한 주소 정보를 헤더에 담는다.

| 계층과 단위 | 헤더에 담는 주소 정보 | 이 예에서 가리키는 것 |
|---|---|---|
| TCP · 세그먼트 | 출발지 포트와 목적지 포트 | 내 컴퓨터의 통신 끝점 `51707`에서 서버의 통신 끝점 `443`으로 |
| IP · 패킷 | 출발지 IP와 목적지 IP | 내 컴퓨터 `192.0.2.15`에서 최종 서버 `203.0.113.20`으로 |
| Ethernet · 프레임 | 현재 링크의 출발지 MAC과 목적지 MAC | 내 네트워크 인터페이스에서 첫 라우터인 기본 게이트웨이로 |

이 예에서 목적지는 원격 서버이므로 첫 프레임의 목적지 MAC은 서버가 아니라 기본 게이트웨이의 MAC이다. 그 프레임의 페이로드에는 IP 패킷 전체가 들어간다. TCP 세그먼트와 IP 패킷, Ethernet 프레임은 모두 같은 데이터 전달 과정의 서로 다른 계층 단위다.

다음 페이지에서는 이 프레임이 스위치와 라우터를 거치며 어떻게 전달되는지 본다. IP 패킷은 최종 서버를 향하지만, MAC 주소는 각 링크에서 다음 장치로 보내도록 사용된다는 차이를 확인하자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 포트는 TCP 헤더, IP 주소는 IP 헤더, MAC 주소는 Ethernet 헤더에 담긴다.
- **적용하기 (Apply):** 원격 서버에 보낼 때 IP 목적지와 첫 프레임의 MAC 목적지가 왜 다른지 설명한다.
- **찾아보기 (Lookup):** 각 단위의 필드 내용은 해당 계층 헤더 표에서 확인한다.

## 스위치와 라우터를 거쳐 목적지에 도착하기

같은 LAN의 스위치와 다른 네트워크로 보내는 라우터는 서로 다른 정보를 보고 전달한다.

| 장비 | 주로 확인하는 정보 | 맡은 범위 | 전달할 때 하는 일 |
|---|---|---|---|
| L2 스위치 | Ethernet 프레임의 목적지 MAC 주소 | 같은 LAN 안 | MAC 주소를 바꾸지 않고 받은 프레임을 목적지 장치 쪽으로 전달한다. |
| 라우터 | IP 패킷의 목적지 IP 주소 | 네트워크와 네트워크 사이 | 다음에 보낼 방향을 고르고, 다음 링크용 새 프레임에 IP 패킷을 담는다. |

라우터가 고르는 다음 전달 지점을 **다음 홉(next hop)**이라고 한다. 이는 경로에서 바로 다음에 만나는 라우터일 수도 있고, 마지막 구간에서는 목적지 호스트일 수도 있다. NAT(Network Address Translation, 네트워크 주소 변환)처럼 주소를 바꾸는 설정이 없는 일반적인 예에서는 IP 패킷의 최종 목적지 IP 주소가 계속 서버를 가리킨다. 각 링크의 Ethernet 프레임과 그 MAC 주소는 다음 구간에 맞게 새로 만들어진다. IP 헤더의 다른 값은 전달 과정에서 바뀔 수 있으므로, ‘IP 주소가 유지된다’는 말은 패킷의 모든 값이 그대로라는 뜻이 아니다.

목적지 호스트에 도착하면 해당 호스트의 네트워크 기능이 IP와 포트 정보를 처리해 연결된 수신 소켓과 프로세스에 데이터를 넘긴다.

전체 흐름을 연결하면 `브라우저 프로세스 → 소켓 → TCP 세그먼트 → IP 패킷 → Ethernet 프레임 → 스위치와 라우터 → 목적지 호스트 → 수신 소켓 → 웹 서버 프로세스`다. 요점은 IP 주소가 목적지 호스트를 찾고, 포트 번호는 그 호스트 안에서 데이터를 받을 통신 끝점을 구분하며, 각 네트워크 장비와 계층이 데이터를 다음 단계로 넘긴다는 것이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 스위치는 MAC으로 같은 LAN 안에서 전달하고, 라우터는 목적지 IP로 다음 홉을 고른다.
- **적용하기 (Apply):** 원격 서버의 최종 IP와 첫 프레임의 목적지 MAC을 구분해 추적한다.
- **찾아보기 (Lookup):** 라우팅 뒤 새 링크에서 프레임 주소가 바뀌는 과정은 ARP Lesson에서 본다.
