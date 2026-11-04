---
id: u5-l25-tcp와-udp-개요
title: TCP와 UDP 개요
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-25.md
wiki_diagram: units/05-tcp-and-udp/lessons/01-tcp와-udp-개요/assets/diagrams/lesson-25.svg
page_metadata:
- terms:
  - 프로토콜(protocol)
  - L4
  illustrations:
  - file: assets/animations/l25-daily-bell-vs-delivered.svg
    title: "벨에 대답해도 서류가 전달됐을까?"
    alt: "나와 회사 건물이 있습니다. 안내데스크 벨을 누르면 안내데스크가 대답하지만 담당 직원이 서류를 받았는지는 물음표로 남습니다. 마지막에 담당 직원에게 전달하는 방법이 따로 있다고 표시됩니다."
    caption: "건물에 사람이 있다는 것과 담당 직원이 받았다는 것은 다릅니다."
    after_paragraph: -1
  - file: assets/animations/l25-ping-vs-program.svg
    title: "ping 응답과 프로그램 전달은 달라요"
    alt: "내 PC와 서버 컴퓨터가 있습니다. ping 요청에 서버의 ICMP 응답이 돌아오지만 웹 서버 프로그램이 요청을 받았는지는 물음표입니다. 마지막에 프로그램 사이의 전달은 TCP와 UDP가 맡는다고 표시됩니다."
    caption: "ping 응답은 서버가 응답했다는 뜻이고, 프로그램 사이의 데이터 전달은 TCP와 UDP가 맡습니다."
    after_paragraph: 4
  questions:
  - id: u7-l01-p01-q01
    kind: choice
    difficulty: easy
    prompt: "IP 주소가 데이터를 전달할 곳으로 가리키는 것은 무엇인가요?"
    choices:
    - id: a
      text: "목적지 컴퓨터"
      feedback: "IP 주소는 데이터를 받을 컴퓨터를 찾는 데 쓰입니다."
    - id: b
      text: "컴퓨터 안의 특정 프로그램"
      feedback: "프로그램을 구분하는 일은 전송 계층의 역할과 관련됩니다."
    - id: c
      text: "화면에 보이는 웹 페이지"
      feedback: "IP 주소는 웹 페이지의 내용을 가리키지 않습니다."
    - id: d
      text: "키보드와 마우스"
      feedback: "IP 주소는 네트워크에서 데이터를 받을 컴퓨터를 가리킵니다."
    - id: e
      text: "인터넷 연결 속도"
      feedback: "IP 주소는 속도를 나타내는 값이 아닙니다."
    answer: a
  - id: u7-l01-p01-q02
    kind: choice
    difficulty: easy
    prompt: "전송 계층(L4)은 주로 어떤 일을 하나요?"
    choices:
    - id: a
      text: "컴퓨터의 전원을 켭니다."
      feedback: "전송 계층은 네트워크로 오가는 데이터와 프로그램 사이의 통신을 다룹니다."
    - id: b
      text: "데이터를 받을 컴퓨터 화면을 찾습니다."
      feedback: "전송 계층은 화면이 아니라 통신 프로그램으로 데이터를 이어 줍니다."
    - id: c
      text: "네트워크 데이터를 알맞은 통신 프로그램으로 이어 줍니다."
      feedback: "전송 계층은 데이터를 받을 통신 프로그램 쪽으로 이어 주는 역할을 합니다."
    - id: d
      text: "웹 페이지의 글과 그림을 만듭니다."
      feedback: "웹 페이지 내용은 애플리케이션이 만들며, 전송 계층은 데이터 전달을 돕습니다."
    - id: e
      text: "Wi-Fi 비밀번호를 정합니다."
      feedback: "Wi-Fi 비밀번호 설정은 전송 계층의 역할이 아닙니다."
    answer: c
  - id: u7-l01-p01-q03
    kind: choice
    difficulty: easy
    prompt: "TCP와 UDP는 무엇인가요?"
    choices:
    - id: a
      text: "두 가지 IP 주소"
      feedback: "TCP와 UDP는 주소가 아니라 통신 규칙입니다."
    - id: b
      text: "전송 계층에서 사용하는 프로토콜"
      feedback: "TCP와 UDP는 L4에서 사용하는 통신 규칙, 즉 프로토콜입니다."
    - id: c
      text: "두 가지 네트워크 케이블"
      feedback: "TCP와 UDP는 물리적인 케이블이 아닙니다."
    - id: d
      text: "웹 브라우저와 메신저"
      feedback: "브라우저와 메신저는 프로그램이고, TCP와 UDP는 통신 규칙입니다."
    - id: e
      text: "두 가지 라우터"
      feedback: "TCP와 UDP는 네트워크 장비가 아닙니다."
    answer: b
  - id: u7-l01-p01-q04
    kind: choice
    difficulty: easy
    prompt: "`ping` 응답이 돌아왔을 때 확인할 수 있는 것은 무엇인가요?"
    choices:
    - id: a
      text: "웹 서버 프로그램이 요청을 처리했다"
      feedback: "`ping` 응답은 웹 서버 프로그램의 요청 처리를 확인해 주지 않습니다."
    - id: b
      text: "사진 파일이 브라우저에 모두 전달됐다"
      feedback: "`ping`은 파일의 전달 완료 여부를 확인하지 않습니다."
    - id: c
      text: "상대 IP 주소에서 응답을 받았다"
      feedback: "`ping` 응답은 해당 IP 주소에서 네트워크 응답이 돌아왔음을 보여 줍니다."
    - id: d
      text: "컴퓨터의 모든 프로그램이 정상 동작한다"
      feedback: "`ping` 응답만으로 각 프로그램의 상태를 알 수는 없습니다."
    - id: e
      text: "웹 서버가 특정 TCP 포트에서 기다리고 있다"
      feedback: "`ping`은 TCP 포트에서 프로그램이 기다리는지 확인하지 않습니다."
    answer: c
  question_placements:
  - question_id: u7-l01-p01-q01
    after_paragraph: 1
  - question_id: u7-l01-p01-q02
    after_paragraph: 2
  - question_id: u7-l01-p01-q03
    after_paragraph: 3
  - question_id: u7-l01-p01-q04
    after_paragraph: 4
- terms:
  - 포트 번호(Port number)
  - 소켓(socket)
  - 클라이언트(Client)와 서버(Server)
  - PID(Process ID)
  illustrations:
  - file: assets/animations/l25-daily-counter-80.svg
    title: "3000번 번호표에서 80번 창구로"
    alt: "A동 12호의 내가 번호표 3000을 받고, 요청이 경비실과 물류센터를 지나 B동 20호의 80번 창구로 갑니다. 건물 주소와 창구 번호가 하나의 길을 만든다고 표시됩니다."
    caption: "건물 주소와 창구 번호가 함께 받는 곳을 구분합니다."
    after_paragraph: -1
  - file: assets/animations/l25-client-server-ports.svg
    title: "클라이언트의 3000번에서 서버의 80번으로"
    alt: "왼쪽의 클라이언트(192.168.0.10, 포트 3000)에서 오른쪽의 서버(192.168.1.20, 포트 80)로 요청 봉투가 스위치와 라우터를 거쳐 이동하는 장면입니다."
    caption: "각 호스트의 IP 주소와 포트 번호로 연결의 양 끝을 구분합니다. 이 예에서는 서로 다른 /24 네트워크 사이를 라우터가 연결합니다."
    after_paragraph: 3
  questions:
  - id: u7-l01-p06-q01
    kind: choice
    difficulty: easy
    prompt: 전송 계층의 포트 번호는 무엇을 구분하는 데 쓰이나요?
    choices:
    - id: a
      text: 한 호스트 안의 통신 끝점
      feedback: IP 주소가 호스트를 가리키고 포트 번호는 그 호스트 안의 통신 끝점을 구분합니다.
    - id: b
      text: 서로 다른 건물의 물리 주소
      feedback: IP 주소와 포트 번호가 구분하는 범위를 나누어 생각하세요.
    - id: c
      text: 컴퓨터의 화면 해상도
      feedback: IP 주소와 포트 번호가 구분하는 범위를 나누어 생각하세요.
    - id: d
      text: 라우터를 지난 홉 수
      feedback: IP 주소와 포트 번호가 구분하는 범위를 나누어 생각하세요.
    - id: e
      text: Ethernet 케이블 길이
      feedback: IP 주소와 포트 번호가 구분하는 범위를 나누어 생각하세요.
    answer: a
  - id: u7-l01-p06-q02
    kind: choice
    difficulty: medium
    prompt: TCP/UDP 포트 번호와 스위치의 물리 포트가 다른 점은 무엇인가요?
    choices:
    - id: a
      text: 둘 다 반드시 케이블 접속구다
      feedback: 문맥이 TCP/UDP 헤더인지 장비인지 확인하세요.
    - id: b
      text: TCP/UDP 포트는 MAC 주소다
      feedback: 문맥이 TCP/UDP 헤더인지 장비인지 확인하세요.
    - id: c
      text: TCP/UDP 포트는 헤더의 번호이고 스위치 포트는 케이블을 꽂는 접속구다
      feedback: 같은 “포트”라도 전송 계층에서는 번호, 스위치에서는 물리 접속구를 뜻할 수 있습니다.
    - id: d
      text: 물리 포트는 프로세스의 PID다
      feedback: 문맥이 TCP/UDP 헤더인지 장비인지 확인하세요.
    - id: e
      text: 두 표현은 항상 같은 뜻이다
      feedback: 문맥이 TCP/UDP 헤더인지 장비인지 확인하세요.
    answer: c
  - id: u7-l01-p06-q03
    kind: choice
    difficulty: medium
    prompt: 이 Lesson의 예에서 192.168.0.10:3000은 무엇을 뜻하나요?
    choices:
    - id: a
      text: 서버의 MAC 주소와 VLAN 번호
      feedback: 콜론 앞 IP와 뒤 포트가 각각 무엇을 가리키는지 확인하세요.
    - id: b
      text: 두 라우터의 물리 포트
      feedback: 콜론 앞 IP와 뒤 포트가 각각 무엇을 가리키는지 확인하세요.
    - id: c
      text: 웹 페이지의 파일 크기
      feedback: 콜론 앞 IP와 뒤 포트가 각각 무엇을 가리키는지 확인하세요.
    - id: d
      text: TCP의 순서 번호와 ACK 번호
      feedback: 콜론 앞 IP와 뒤 포트가 각각 무엇을 가리키는지 확인하세요.
    - id: e
      text: 클라이언트 호스트의 IP 주소와 임시 포트 번호
      feedback: IP 주소와 포트 번호를 함께 써서 호스트와 통신 끝점을 나타냅니다.
    answer: e
  question_placements:
  - question_id: u7-l01-p06-q01
    after_paragraph: 2
- terms:
  - Listen
  illustrations:
  - file: assets/animations/l25-daily-open-counter.svg
    title: "문을 연 창구만 손님을 받아요"
    alt: "가게에 80번 창구는 영업 중이고 81번 창구는 닫혀 있습니다. 손님이 80번에 가면 받아 주고, 닫힌 창구에 가면 받을 사람이 없다고 표시됩니다."
    caption: "연결을 받으려면 서버가 먼저 기다리는 상태여야 합니다."
    after_paragraph: -1
  - file: assets/animations/l25-listen-socket.svg
    title: "Listen은 연결을 기다리는 상태예요"
    alt: "서버 컴퓨터의 80번 소켓은 Listen 상태이고 8080번에는 기다리는 소켓이 없습니다. 클라이언트의 연결 요청은 80번에서는 받아지고, 기다리는 소켓이 없는 포트에서는 받을 수 없습니다. 포트 번호는 예시입니다."
    caption: "서버는 포트에서 Listen 상태로 연결을 기다립니다. 그림의 포트 번호는 예시입니다."
    after_paragraph: 0
  questions:
  - id: u7-l01-p07-q01
    kind: choice
    difficulty: easy
    prompt: 서버 프로세스가 특정 포트에서 연결을 기다리는 상태를 무엇이라고 하나요?
    choices:
    - id: a
      text: Retransmission
      feedback: 서버가 연결을 기다리는 상태 이름을 확인하세요.
    - id: b
      text: Broadcast
      feedback: 서버가 연결을 기다리는 상태 이름을 확인하세요.
    - id: c
      text: Listen
      feedback: 서버 소켓은 사용할 포트를 지정하고 Listen 상태로 연결을 기다릴 수 있습니다.
    - id: d
      text: Fragmentation
      feedback: 서버가 연결을 기다리는 상태 이름을 확인하세요.
    - id: e
      text: Loopback
      feedback: 서버가 연결을 기다리는 상태 이름을 확인하세요.
    answer: c
  - id: u7-l01-p07-q02
    kind: choice
    difficulty: medium
    prompt: 클라이언트가 서버 포트로 접속을 요청했는데 그 포트를 기다리는 서버 소켓이 없다면 어떻게 될 수 있나요?
    choices:
    - id: a
      text: 요청이 자동으로 다른 웹 사이트로 간다
      feedback: 포트 번호만 열려 있다고 응용 프로그램이 자동으로 실행되는 것은 아닙니다.
    - id: b
      text: DHCP가 새 포트를 만든다
      feedback: 포트 번호만 열려 있다고 응용 프로그램이 자동으로 실행되는 것은 아닙니다.
    - id: c
      text: 클라이언트의 IP가 서버 IP로 바뀐다
      feedback: 포트 번호만 열려 있다고 응용 프로그램이 자동으로 실행되는 것은 아닙니다.
    - id: d
      text: 모든 라우터가 Listen 상태가 된다
      feedback: 포트 번호만 열려 있다고 응용 프로그램이 자동으로 실행되는 것은 아닙니다.
    - id: e
      text: 서버의 TCP가 연결을 받을 수 없다고 응답할 수 있다
      feedback: 연결을 받을 프로세스나 소켓이 없으면 운영체제가 받을 수 없다는 응답을 처리할 수 있습니다.
    answer: e
  - id: u7-l01-p07-q03
    kind: choice
    difficulty: medium
    prompt: 서버에 접속하려는 클라이언트가 알아야 할 정보로 본문이 제시한 것은 무엇인가요?
    choices:
    - id: a
      text: 상대 프로세스의 화면 밝기와 PID
      feedback: 호스트를 찾는 정보와 그 안의 서비스 끝점을 찾는 정보를 함께 보세요.
    - id: b
      text: 상대 IP 주소와 서비스 포트 번호
      feedback: 접속하려는 쪽은 상대 IP 주소와 서비스 포트 번호를 알아야 합니다.
    - id: c
      text: 서버의 DHCP 임대 만료 시각만
      feedback: 호스트를 찾는 정보와 그 안의 서비스 끝점을 찾는 정보를 함께 보세요.
    - id: d
      text: 라우터의 모든 MAC 주소
      feedback: 호스트를 찾는 정보와 그 안의 서비스 끝점을 찾는 정보를 함께 보세요.
    - id: e
      text: 서버가 쓰는 Ethernet 케이블 길이
      feedback: 호스트를 찾는 정보와 그 안의 서비스 끝점을 찾는 정보를 함께 보세요.
    answer: b
- terms:
  - 연결 지향(Connection-oriented)
  - Virtual Circuit(가상 회선)
  - 상태(State)
  illustrations:
  - file: assets/animations/l25-daily-call-vs-postcard.svg
    title: "연결 있는 전화, 연결 없는 엽서"
    alt: "왼쪽 전화 통화 칸에서는 두 전화기가 연결되어 서로 기억하고 ‘들려요’가 돌아옵니다. 오른쪽 엽서 칸에서는 연결 없이 엽서가 한 방향으로 가고 돌아오는 대답이 없습니다."
    caption: "전화는 연결을 기억하고, 엽서에는 연결이 없습니다."
    after_paragraph: -1
  - file: assets/animations/l25-tcp-connection-vs-udp.svg
    title: "연결이 있는 TCP, 연결이 없는 UDP"
    alt: "화면 왼쪽에서는 두 컴퓨터 사이에 점선 통로가 생기고 확인 신호가 오갑니다. 오른쪽에서는 두 컴퓨터 사이에 아무 통로 없이 엽서 모양 짐이 한 방향으로 날아갑니다."
    caption: "TCP는 먼저 연결을 맺고 확인을 주고받으며, UDP는 연결 없이 그냥 보냅니다."
    after_paragraph: 3
  questions:
  - id: u7-l01-p04-q01
    kind: choice
    difficulty: easy
    prompt: TCP를 연결 지향 프로토콜이라고 하는 이유는 무엇인가요?
    choices:
    - id: a
      text: 인터넷에 전용 전선을 깔기 때문이다
      feedback: 논리적 상태 관리와 물리적 전용 회선을 혼동하지 마세요.
    - id: b
      text: 통신 전에 양 끝 TCP가 연결 상태와 관련 정보를 관리한다
      feedback: TCP는 데이터를 주고받기 전에 연결을 만들고 양쪽 상태를 관리합니다.
    - id: c
      text: 모든 경로의 라우터를 독점하기 때문이다
      feedback: 논리적 상태 관리와 물리적 전용 회선을 혼동하지 마세요.
    - id: d
      text: 서버와 클라이언트가 같은 컴퓨터여야 하기 때문이다
      feedback: 논리적 상태 관리와 물리적 전용 회선을 혼동하지 마세요.
    - id: e
      text: UDP보다 항상 빠르기 때문이다
      feedback: 논리적 상태 관리와 물리적 전용 회선을 혼동하지 마세요.
    answer: b
  - id: u7-l01-p04-q02
    kind: choice
    difficulty: medium
    prompt: TCP 연결에 대한 설명으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 두 컴퓨터 사이에 전용 케이블을 새로 설치한다
      feedback: 본문에서 TCP 연결이 의미하지 않는 것으로 전용 전선과 경로 독점을 설명합니다.
    - id: b
      text: 중간 라우터가 연결 상태를 모두 관리한다
      feedback: 본문에서 TCP 연결이 의미하지 않는 것으로 전용 전선과 경로 독점을 설명합니다.
    - id: c
      text: 연결 중에는 IP 주소가 필요 없다
      feedback: 본문에서 TCP 연결이 의미하지 않는 것으로 전용 전선과 경로 독점을 설명합니다.
    - id: d
      text: 양 끝 TCP가 관리하는 논리적 연결이며 인터넷 경로를 독점하지 않는다
      feedback: TCP 연결은 양 끝 TCP가 상대와의 상태를 관리하는 논리적 약속입니다.
    - id: e
      text: TCP 연결은 UDP에도 같은 절차로 적용된다
      feedback: 본문에서 TCP 연결이 의미하지 않는 것으로 전용 전선과 경로 독점을 설명합니다.
    answer: d
  - id: u7-l01-p04-q03
    kind: choice
    difficulty: medium
    prompt: TCP가 연결 상태를 관리하면 도움이 되는 이유는 무엇인가요?
    choices:
    - id: a
      text: 보낸 범위, 받은 범위, 연결 진행 상태를 추적할 수 있다
      feedback: TCP는 어떤 바이트를 보내고 확인받았는지 등 통신 상태를 관리합니다.
    - id: b
      text: 인터넷 경로의 모든 장치를 끌 수 있다
      feedback: ACK와 흐름 제어가 연결 상태와 어떻게 이어지는지 생각하세요.
    - id: c
      text: 포트 번호가 필요 없어 진다
      feedback: ACK와 흐름 제어가 연결 상태와 어떻게 이어지는지 생각하세요.
    - id: d
      text: 데이터그램 경계를 보존한다
      feedback: ACK와 흐름 제어가 연결 상태와 어떻게 이어지는지 생각하세요.
    - id: e
      text: 모든 응용 프로그램이 같은 PID를 쓰게 된다
      feedback: ACK와 흐름 제어가 연결 상태와 어떻게 이어지는지 생각하세요.
    answer: a
  question_placements:
  - question_id: u7-l01-p04-q01
    after_paragraph: 1
- terms:
  - Frame · Packet · Segment · Datagram
  - Stream
  illustrations:
  - file: assets/animations/l25-daily-address-layers.svg
    title: "겹겹이 붙는 주소"
    alt: "보낼 내용에 책상 번호, 건물 주소, 이번 구간 인수자가 차례로 겹겹이 붙습니다. 겹이 늘 때마다 해당 행이 강조됩니다."
    caption: "같은 내용도 어떤 겹을 붙였는지에 따라 이름이 달라집니다."
    after_paragraph: -1
  - file: assets/animations/l25-layers-data-units.svg
    title: "층을 지날 때마다 이름이 바뀌는 데이터"
    alt: "작은 데이터 상자에 먼저 포트 봉투, 다음 IP 봉투, 마지막으로 MAC 봉투가 차례로 씌워지고, 각 단계마다 Segment, Packet, Frame 이름표가 붙습니다."
    caption: "같은 데이터가 포트, IP, MAC 순으로 겹겹이 감싸지며 Segment, Packet, Frame이 됩니다."
    after_paragraph: 0
  questions:
  - id: u5-l25-p05-q01
    kind: choice
    difficulty: easy
    prompt: TCP가 Stream을 나누어 보내는 전송 단위는 무엇인가요?
    choices:
    - id: a
      text: Frame
      feedback: Frame은 Ethernet(L2)이 쓰는 데이터 단위예요. TCP가 Stream을 나눈 조각의 이름이 아니에요.
    - id: b
      text: Datagram
      feedback: Datagram은 UDP의 데이터 단위예요. 이 문제는 TCP를 묻고 있어요.
    - id: c
      text: Segment
      feedback: 맞아요. TCP는 Stream을 나눈 조각에 TCP 헤더를 붙여 Segment로 보내요.
    - id: d
      text: 포트 번호
      feedback: 포트 번호는 데이터 조각이 아니라 L4에서 프로그램을 구분하는 식별자예요.
    - id: e
      text: MAC 주소
      feedback: MAC 주소는 L2에서 장치를 구분하는 식별자예요. 데이터 조각의 이름이 아니에요.
    answer: c
  - id: u5-l25-p05-q02
    kind: choice
    difficulty: medium
    prompt: Stream이 MSS보다 길고 길이가 MSS로 나누어 떨어지지 않을 때 TCP의 동작으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: Segment 하나에 Stream 전체를 넣는다
      feedback: MSS보다 긴 Stream은 Segment 하나에 담을 수 없어요. TCP는 MSS에 맞춰 나눠 보내요.
    - id: b
      text: 모든 Segment를 같은 크기로 맞추려고 데이터를 버린다
      feedback: TCP는 데이터를 버리지 않아요. 남은 만큼을 짧은 마지막 조각으로 보내요.
    - id: c
      text: 마지막 조각은 보내지 않고 기다린다
      feedback: 마지막 조각도 그대로 보내요. 앞 조각과 같은 크기가 될 때까지 기다리지 않아요.
    - id: d
      text: MSS 크기로 나누고, 마지막 Segment는 더 짧을 수 있다
      feedback: 맞아요. TCP는 MSS 기준으로 나누고 마지막 조각은 앞 조각보다 짧을 수 있어요.
    - id: e
      text: Stream을 Datagram으로 바꿔 보낸다
      feedback: Datagram은 UDP의 단위예요. TCP는 Stream을 Segment로 나눠요.
    answer: d
  - id: u7-l01-p05-q03
    kind: choice
    difficulty: medium
    prompt: TCP Segment를 받은 쪽 TCP가 데이터를 애플리케이션에 제공할 때 어떤 형태로 볼 수 있나요?
    choices:
    - id: a
      text: 항상 송신자가 나눈 메시지 경계 그대로
      feedback: TCP Stream의 읽기 경계가 송신 요청 경계와 항상 같지는 않습니다.
    - id: b
      text: Ethernet Frame의 목록만
      feedback: TCP Stream의 읽기 경계가 송신 요청 경계와 항상 같지는 않습니다.
    - id: c
      text: 순서가 이어진 바이트 Stream
      feedback: TCP 수신 측은 Segment를 순서대로 이어 애플리케이션에 Stream으로 제공합니다.
    - id: d
      text: MAC 주소 문자열
      feedback: TCP Stream의 읽기 경계가 송신 요청 경계와 항상 같지는 않습니다.
    - id: e
      text: DHCP 옵션 목록
      feedback: TCP Stream의 읽기 경계가 송신 요청 경계와 항상 같지는 않습니다.
    answer: c
  question_placements:
  - question_id: u5-l25-p05-q01
    after_paragraph: 1
- page_id: u7-tcp-delivery-confirmation
  terms:
  - 확인 응답(ACK)
  - 재전송(Retransmission)
  illustrations:
  - file: assets/animations/l25-daily-parcel-receipt-resend.svg
    title: "받았다는 소식이 돌아와요"
    alt: "판매자가 택배를 보내면 집에서 받았다는 문자가 돌아옵니다. 다음 택배는 도중에 사라지고 소식이 오지 않아 판매자가 같은 물건을 다시 보내고 집에 도착합니다."
    caption: "받았다는 소식이 없으면 같은 물건을 다시 보낼 수 있습니다."
    after_paragraph: -1
  - file: assets/animations/l25-ack-and-retransmit.svg
    title: "ACK는 받은 범위를 알려 줘요"
    alt: "서버가 PC로 데이터를 보내면 PC의 TCP가 받은 범위를 ACK로 돌려보냅니다. 다음 데이터는 도중에 사라져 확인이 오지 않고, 서버가 확인되지 않은 데이터를 다시 보내 PC에 도착합니다."
    caption: "ACK는 상대 TCP가 받은 범위를 알리고, 확인되지 않은 데이터는 재전송할 수 있습니다."
    after_paragraph: 3
  - file: assets/diagrams/tcp-receipt.svg
    title: "데이터를 보내는 방향과 확인 응답이 돌아오는 방향"
    alt: "서버에서 PC의 TCP로 사진 데이터가 가고, 반대 방향으로 TCP 확인 응답이 돌아온다. PC의 TCP 수신과 브라우저가 읽는 단계는 별도로 표시되어 있다."
    caption: "ACK는 상대 TCP가 받은 범위를 알려 준다. 브라우저가 사진을 읽거나 저장했다는 확인은 아니다."
    after_paragraph: 3
  questions:
  - id: u7-l01-p02-q01
    kind: choice
    difficulty: easy
    prompt: IP 패킷을 목적지로 보냈다는 사실만으로 알 수 없는 것은 무엇인가요?
    choices:
    - id: a
      text: IP 패킷에 목적지 주소가 있었는지
      feedback: IP의 전달과 수신 데이터 확인은 같은 일인지 생각해 보세요.
    - id: b
      text: IP가 전달을 시도했는지
      feedback: IP의 전달과 수신 데이터 확인은 같은 일인지 생각해 보세요.
    - id: c
      text: 상대 프로그램이 사진의 모든 바이트를 받았는지
      feedback: IP 자체는 상대가 어디까지 받았는지 확인하거나 누락 데이터를 다시 보내지 않습니다.
    - id: d
      text: 패킷을 보낼 출발지가 있었는지
      feedback: IP의 전달과 수신 데이터 확인은 같은 일인지 생각해 보세요.
    - id: e
      text: 네트워크 계층이 사용되었는지
      feedback: IP의 전달과 수신 데이터 확인은 같은 일인지 생각해 보세요.
    answer: c
  - id: u7-l01-p02-q02
    kind: choice
    difficulty: medium
    prompt: TCP의 ACK가 알려 주는 것은 무엇인가요?
    choices:
    - id: a
      text: 브라우저가 사진을 화면에 띄웠는지
      feedback: ACK가 확인하는 주체는 브라우저가 아니라 상대 TCP입니다.
    - id: b
      text: 사용자가 파일을 열었는지
      feedback: ACK가 확인하는 주체는 브라우저가 아니라 상대 TCP입니다.
    - id: c
      text: 서버가 전원을 껐는지
      feedback: ACK가 확인하는 주체는 브라우저가 아니라 상대 TCP입니다.
    - id: d
      text: DNS가 도메인을 등록했는지
      feedback: ACK가 확인하는 주체는 브라우저가 아니라 상대 TCP입니다.
    - id: e
      text: 수신 측 TCP가 어디까지 빠짐없이 받았는지
      feedback: ACK는 수신 측 TCP가 받은 범위를 송신 측 TCP에 알립니다.
    answer: e
  - id: u7-l01-p02-q03
    kind: choice
    difficulty: medium
    prompt: TCP가 보낸 데이터 중 확인받지 못한 부분에 문제가 있다고 판단하면 할 수 있는 일은 무엇인가요?
    choices:
    - id: a
      text: 수신 버퍼를 강제로 지운다
      feedback: 재전송은 새 데이터를 만드는 것이 아니라 확인받지 못한 데이터를 다시 보내는 동작입니다.
    - id: b
      text: 해당 바이트를 다시 전송한다
      feedback: TCP는 확인되지 않은 데이터를 재전송할 수 있습니다.
    - id: c
      text: IP 주소를 MAC 주소로 바꾼다
      feedback: 재전송은 새 데이터를 만드는 것이 아니라 확인받지 못한 데이터를 다시 보내는 동작입니다.
    - id: d
      text: 모든 데이터를 UDP로 바꾼다
      feedback: 재전송은 새 데이터를 만드는 것이 아니라 확인받지 못한 데이터를 다시 보내는 동작입니다.
    - id: e
      text: 서버의 웹 페이지를 삭제한다
      feedback: 재전송은 새 데이터를 만드는 것이 아니라 확인받지 못한 데이터를 다시 보내는 동작입니다.
    answer: b
  question_placements:
  - question_id: u7-l01-p02-q01
    after_paragraph: 6
- page_id: u7-tcp-receive-capacity
  terms:
  - 수신 윈도(Receive Window)
  - 흐름 제어(Flow Control)
  illustrations:
  - file: assets/animations/l25-daily-locker-slots.svg
    title: "보관함에 남은 자리를 알려 줘요"
    alt: "8칸 보관함에 택배 6칸이 차 있고 남은 자리는 2칸입니다. 주인이 2칸을 꺼내 가면 택배는 4칸, 남은 자리는 4칸이 되고 이 소식을 판매자에게 알립니다."
    caption: "주인이 꺼내 가면 남은 자리가 늘어납니다. 한 칸은 설명용 단위입니다."
    after_paragraph: -1
  - file: assets/animations/l25-receive-window-slots.svg
    title: "수신 윈도는 남은 버퍼 공간이에요"
    alt: "수신 버퍼 8칸 중 읽지 않은 데이터가 6칸이고 수신 윈도는 2칸입니다. 브라우저가 2칸을 읽으면 데이터는 4칸, 수신 윈도는 4칸이 되어 서버에 알립니다."
    caption: "수신 윈도는 더 받아 둘 수 있는 바이트 범위입니다. 한 칸은 예시로 1,000바이트입니다."
    after_paragraph: 2
  - file: assets/diagrams/receive-capacity.svg
    title: "프로그램이 읽으면 수신 버퍼의 여유가 늘어난다"
    alt: "8칸의 수신 버퍼에 데이터 6칸과 빈칸 2칸이 있다. 브라우저가 2칸을 읽은 뒤에는 데이터 4칸과 빈칸 4칸이 된다. 한 칸은 예시로 1,000바이트를 뜻한다."
    caption: "수신 윈도는 더 받아 둘 수 있는 바이트 범위를 알린다. 그림은 수신 버퍼의 용량과 읽기의 관계를 단순화한 예시이며, 회선 속도나 세그먼트 하나의 크기를 뜻하지 않는다."
    after_paragraph: 3
  questions:
  - id: u7-l01-p03-q01
    kind: choice
    difficulty: easy
    prompt: 수신 버퍼는 어떤 역할을 하나요?
    choices:
    - id: a
      text: 도메인 이름과 IP 주소를 영구 저장한다
      feedback: 데이터 도착과 프로그램이 데이터를 읽는 시점은 다를 수 있습니다.
    - id: b
      text: 인터넷 경로를 독점한다
      feedback: 데이터 도착과 프로그램이 데이터를 읽는 시점은 다를 수 있습니다.
    - id: c
      text: 모든 Ethernet 프레임을 암호화한다
      feedback: 데이터 도착과 프로그램이 데이터를 읽는 시점은 다를 수 있습니다.
    - id: d
      text: 송신자의 DHCP 임대를 연장한다
      feedback: 데이터 도착과 프로그램이 데이터를 읽는 시점은 다를 수 있습니다.
    - id: e
      text: TCP가 받은 바이트를 애플리케이션이 읽기 전까지 잠시 보관한다
      feedback: 수신 버퍼는 받은 바이트를 프로그램이 읽기 전까지 보관합니다.
    answer: e
  - id: u7-l01-p03-q02
    kind: choice
    difficulty: medium
    prompt: 수신 윈도(Receive Window)는 주로 어떤 정보를 알려 주나요?
    choices:
    - id: a
      text: 이미 화면에 표시한 사진의 크기
      feedback: 받은 범위(ACK)와 추가로 받을 공간(수신 윈도)을 나누어 생각하세요.
    - id: b
      text: 수신 측이 앞으로 더 받아 둘 수 있는 바이트 범위
      feedback: 수신 윈도는 수신 측이 더 받아 둘 수 있는 공간을 송신 측에 알립니다.
    - id: c
      text: 초당 인터넷 전송 속도
      feedback: 받은 범위(ACK)와 추가로 받을 공간(수신 윈도)을 나누어 생각하세요.
    - id: d
      text: 세그먼트 하나의 최대 크기만
      feedback: 받은 범위(ACK)와 추가로 받을 공간(수신 윈도)을 나누어 생각하세요.
    - id: e
      text: 라우터까지의 거리
      feedback: 받은 범위(ACK)와 추가로 받을 공간(수신 윈도)을 나누어 생각하세요.
    answer: b
  - id: u7-l01-p03-q03
    kind: choice
    difficulty: medium
    prompt: 수신 윈도가 2,000바이트라는 말의 뜻은 무엇인가요?
    choices:
    - id: a
      text: 초당 2,000바이트로만 전송한다는 뜻
      feedback: 용량, 속도, 세그먼트 크기를 구별하세요.
    - id: b
      text: MSS가 정확히 2,000바이트라는 뜻
      feedback: 용량, 속도, 세그먼트 크기를 구별하세요.
    - id: c
      text: 이미 2,000바이트를 브라우저가 화면에 표시했다는 뜻
      feedback: 용량, 속도, 세그먼트 크기를 구별하세요.
    - id: d
      text: 더 받아 둘 수 있는 바이트 범위가 2,000바이트라는 뜻이지 초당 속도가 아니다
      feedback: 수신 윈도는 추가 수용 공간이지 전송 속도나 MSS를 뜻하지 않습니다.
    - id: e
      text: 패킷이 2,000개의 라우터를 지난다는 뜻
      feedback: 용량, 속도, 세그먼트 크기를 구별하세요.
    answer: d
  question_placements:
  - question_id: u7-l01-p03-q01
    after_paragraph: 3
- terms: []
  illustrations:
  - file: assets/animations/l25-daily-postcards-separate.svg
    title: "엽서는 따로따로 가요"
    alt: "내가 엽서 A와 B를 연결 없이 차례로 보냅니다. A는 도중에 사라지고 B만 친구에게 도착하지만 A가 어떻게 됐는지는 아무도 알려 주지 않습니다. 필요하면 보내는 사람이 직접 확인해야 한다고 표시됩니다."
    caption: "엽서는 따로 가며 보낸 뒤 확인해 주는 사람이 없습니다."
    after_paragraph: -1
  - file: assets/animations/l25-udp-datagrams.svg
    title: "UDP는 데이터그램을 따로 보내요"
    alt: "송신 프로그램이 데이터그램 1과 2를 연결 없이 차례로 보냅니다. 데이터그램 1은 도중에 사라지고 2만 수신 프로그램에 도착하지만 1에 대한 알림은 없습니다. 확인, 재전송, 윈도가 없으므로 필요하면 프로그램이 마련해야 합니다."
    caption: "UDP 자체에는 수신 확인, 재전송, 수신 윈도 흐름 제어가 없습니다."
    after_paragraph: 0
  questions:
  - id: u7-l01-p08-q01
    kind: choice
    difficulty: easy
    prompt: UDP가 TCP와 다른 점으로 본문에 맞는 설명은 무엇인가요?
    choices:
    - id: a
      text: 항상 연결을 맺고 바이트 Stream으로 보낸다
      feedback: 연결 유무와 데이터 단위를 함께 비교하세요.
    - id: b
      text: 데이터 도착과 순서를 자체적으로 보장한다
      feedback: 연결 유무와 데이터 단위를 함께 비교하세요.
    - id: c
      text: 포트 번호를 사용할 수 없다
      feedback: 연결 유무와 데이터 단위를 함께 비교하세요.
    - id: d
      text: 데이터를 IP 패킷에 넣지 않는다
      feedback: 연결 유무와 데이터 단위를 함께 비교하세요.
    - id: e
      text: TCP와 같은 연결 절차 없이 데이터그램 단위로 보낸다
      feedback: UDP는 TCP와 같은 연결 절차 없이 데이터그램 단위로 보냅니다.
    answer: e
  - id: u7-l01-p08-q02
    kind: choice
    difficulty: medium
    prompt: UDP로 두 개의 데이터그램을 보내면 수신 프로그램에서 어떤 점이 유지되나요?
    choices:
    - id: a
      text: 두 데이터그램이 항상 하나의 TCP Stream이 된다
      feedback: UDP의 메시지 경계 유지와 전달 보장은 서로 다른 속성입니다.
    - id: b
      text: 각 데이터그램이 별개의 메시지 경계로 다뤄진다
      feedback: UDP는 프로그램이 보낸 데이터그램의 경계를 유지합니다.
    - id: c
      text: 각 데이터그램은 반드시 순서가 보장된다
      feedback: UDP의 메시지 경계 유지와 전달 보장은 서로 다른 속성입니다.
    - id: d
      text: 첫 데이터그램만 전달된다
      feedback: UDP의 메시지 경계 유지와 전달 보장은 서로 다른 속성입니다.
    - id: e
      text: 수신 측 포트가 사라진다
      feedback: UDP의 메시지 경계 유지와 전달 보장은 서로 다른 속성입니다.
    answer: b
  - id: u7-l01-p08-q03
    kind: choice
    difficulty: medium
    prompt: UDP 자체가 보장하지 않는 것은 무엇인가요?
    choices:
    - id: a
      text: 포트 번호의 사용
      feedback: UDP 자체의 보장과 애플리케이션이 별도로 마련할 수 있는 기능을 구분하세요.
    - id: b
      text: 데이터그램 단위로 보낸다는 점
      feedback: UDP 자체의 보장과 애플리케이션이 별도로 마련할 수 있는 기능을 구분하세요.
    - id: c
      text: 소켓을 통한 사용
      feedback: UDP 자체의 보장과 애플리케이션이 별도로 마련할 수 있는 기능을 구분하세요.
    - id: d
      text: 데이터그램의 도착과 순서
      feedback: UDP 자체는 데이터그램의 도착이나 순서를 보장하지 않습니다.
    - id: e
      text: IP 위에서 동작한다는 점
      feedback: UDP 자체의 보장과 애플리케이션이 별도로 마련할 수 있는 기능을 구분하세요.
    answer: d
  question_placements:
  - question_id: u7-l01-p08-q01
    after_paragraph: 1
animations_dir: units/05-tcp-and-udp/lessons/01-tcp와-udp-개요/assets/animations
additional_sources:
- https://github.com/FutureReadyCampus/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/04-1.md
- https://github.com/FutureReadyCampus/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/04-2.md
- https://github.com/FutureReadyCampus/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/04-3.md
source_snapshot: sources/wiki/tcp-delivery-intro.json
---

## TCP와 UDP는 프로그램 사이에서 어떤 일을 할까?
<!-- learn-page-id: tcp-udp-overview -->

회사 안내데스크가 벨에 대답해도 서류가 담당 직원에게 전달됐다고는 알 수 없습니다. 네트워크에서도 목적지 컴퓨터가 응답했다는 것과 그 안의 웹 브라우저나 서버 프로그램이 데이터를 받았다는 것은 다릅니다. IP 주소는 데이터를 받을 컴퓨터를 찾는 데 쓰이지만, 그 컴퓨터 안의 프로그램까지 전달하는 규칙은 따로 필요합니다.

이 일을 맡는 계층을 전송 계층(Transport layer), 또는 L4라고 부릅니다. 같은 컴퓨터에서 브라우저, 메신저, 게임처럼 여러 프로그램이 네트워크를 사용할 수 있으므로, 전송 계층은 데이터를 알맞은 통신 프로그램으로 이어 주는 역할을 합니다. 어떤 프로그램 쪽인지 구분하는 포트 번호는 다음 페이지에서 살펴봅니다.

TCP와 UDP는 전송 계층에서 사용하는 두 가지 프로토콜입니다. 프로토콜은 서로 통신할 때 따르는 규칙을 뜻합니다. 두 이름은 모두 L4에 속하지만, 데이터를 주고받는 방식에는 차이가 있습니다. 이 페이지에서는 우선 두 프로토콜이 어디에서 어떤 역할을 하는지 익히고, 다음 페이지부터 차이를 하나씩 살펴봅니다.

`ping` 응답이 돌아오면 상대 IP 주소에서 응답을 받을 수 있었다는 점을 확인할 수 있습니다. 하지만 그것만으로 웹 서버 프로그램이 요청을 받았거나 사진의 모든 내용이 브라우저까지 전달됐다고 확인할 수는 없습니다. 컴퓨터까지 닿는 일과 그 안의 프로그램에 데이터를 전달하는 일은 구분해서 봐야 합니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP와 UDP는 프로그램 사이의 데이터 전달에 쓰이는 전송 계층 프로토콜이다.
- **적용하기 (Apply):** 컴퓨터에 도착한 것과 그 안의 프로그램이 데이터를 받은 것을 구분한다.
- **찾아보기 (Lookup):** 내 컴퓨터의 프로그램이 사용하는 프로토콜과 포트는 네트워크 도구에서 확인한다.

## 포트와 소켓으로 클라이언트와 서버를 연결한다

Unit 4에서 소켓은 프로그램과 운영체제의 네트워크 기능을 잇는 창구라고 배웠다. 프로그램은 이 창구를 통해 TCP와 UDP를 사용한다. IP 주소가 데이터를 받을 컴퓨터를 가리킨다면 포트 번호는 그 컴퓨터 안에서 어느 통신 끝점으로 건넬지 구분한다. 한 컴퓨터에서 웹 서버와 다른 네트워크 프로그램이 각자 포트를 사용할 수 있다. 포트 번호는 프로세스의 PID와 같은 값이 아니며, 운영체제는 소켓과 포트 정보를 이용해 받은 데이터를 알맞은 통신 끝점에 연결한다.

‘포트’라는 말은 스위치의 케이블 접속구 같은 물리 인터페이스에도 쓰인다. 여기서 다루는 TCP·UDP 포트는 헤더에 적히는 번호다. 컴퓨터 주소가 건물 주소라면 포트 번호는 그 건물 안에서 어느 안내 창구로 데이터를 보낼지 가리키는 표시와 비슷하다. 같은 단어라도 장비의 접속구인지, 전송 계층의 번호인지 문맥을 확인하자.

TCP 연결을 먼저 시도하는 쪽은 클라이언트, 연결을 기다렸다 받아 주는 쪽은 서버다. 두 쪽 모두 프로세스이며 소켓을 사용한다. 예를 들어 192.168.0.10의 클라이언트가 임시 포트 3000을 사용해 192.168.1.20의 서버 포트 80으로 연결할 수 있다. 80은 이 예에서 HTTP 요청을 기다리는 포트다. 클라이언트의 포트는 운영체제가 사용 가능한 번호 중에서 배정할 수 있다.

이 예에서 양쪽의 프리픽스 길이는 /24다. 클라이언트는 192.168.0.0/24, 서버는 192.168.1.0/24에 있으므로 라우터를 거쳐 전달한다. 애니메이션에서는 이 경로와 함께 출발지·목적지의 IP 주소와 포트 번호 짝을 살펴보자. 중간 장비는 전달을 맡고, 양 끝의 TCP는 해당 연결의 상태를 관리한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Port는 Host 안의 통신 종점, Socket은 앱이 통신을 이용하는 인터페이스다.
- **적용하기 (Apply):** 같은 서버의 서로 다른 포트에 여러 Client가 연결되는 상황을 읽는다.
- **찾아보기 (Lookup):** 소켓 식별자와 4-tuple은 TCP API 문서에서 확인한다.

## Listen · 연결을 기다리기

서버 프로세스는 사용할 포트를 지정하고 소켓을 Listen 상태로 두어 연결을 기다린다. 가게가 안내 창구를 열고 손님을 기다리는 것처럼, Listen은 연결을 받을 준비를 한 상태다. 아직 특정 클라이언트와 연결됐다는 뜻은 아니다. 예를 들어 웹 서버가 포트 80에서 기다리면, 클라이언트는 서버의 IP 주소와 80번 포트를 지정해 접속을 시도한다. 연결을 받을 프로세스나 소켓이 없는데 요청이 오면, 서버의 TCP 구현이 연결을 받을 수 없다는 응답을 처리한다. 이러한 동작은 운영체제 수준에서 이루어진다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Listen은 서버 프로세스가 새 TCP 연결을 받아들일 준비를 하는 상태다.
- **적용하기 (Apply):** Client 요청이 도착하기 전 대기 중인 Port와 연결된 소켓을 구분한다.
- **찾아보기 (Lookup):** 운영체제에서 Listening socket을 확인하는 명령은 도움말을 참조한다.

## TCP 연결은 양쪽이 통신 상태를 관리하는 약속이다
<!-- learn-page-id: tcp-session-definition -->

서버가 포트에서 연결을 기다리고 있으면 클라이언트가 그곳에 접속을 시도할 수 있다. TCP는 데이터 통신을 시작하기 전에 양쪽이 연결 상태를 만드는 연결 지향(Connection-oriented) 프로토콜이다. UDP에는 TCP와 같은 연결 수립 절차가 없다.

TCP 연결은 전화를 걸고 상대가 응답한 뒤 서로 통화 중임을 기억하는 상황에 비유할 수 있다. 다만 실제 전화선처럼 두 컴퓨터 사이에 전용 전선을 새로 깔거나 인터넷 경로를 독점하는 것은 아니다. 양 끝 TCP가 상대 주소·포트와 현재 통신 상태를 기억하는 논리적인 연결이며, 이 관계를 TCP 세션(TCP session)이라고도 한다. UDP는 엽서를 우체통에 넣듯 연결 절차 없이 데이터그램을 보낸다. 실제 TCP 패킷과 UDP 데이터그램은 모두 기존 네트워크 경로를 다른 통신과 함께 이용한다.

예를 들어 서버는 어느 통신 끝점과 연결되어 있는지, 연결이 어떤 상태인지 기억한다. PC 쪽 TCP도 같은 연결에 관한 상태를 관리한다. 이처럼 연결은 눈에 보이는 전용 통로가 아니라 양 끝이 함께 유지하는 통신 관계다. TCP가 데이터의 순서와 받은 범위를 어떻게 표시하는지는 다음 Lesson과 Unit 8에서 더 자세히 살펴본다.

연결에는 상태 변화도 있다. 전화를 기다리는 때, 통화 중인 때, 통화를 끝내는 때를 구별하듯 TCP도 연결을 기다리거나 연결된 상태 등을 구별한다. 이 페이지의 애니메이션에서는 TCP 쪽의 연결과 확인 신호, UDP 쪽의 연결 절차 없는 전송을 비교하자. 점선은 설명용 표시이며 실제 전용 통로는 아니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP 연결은 양 끝이 상대 통신 끝점과 현재 상태를 기억하는 논리적 관계다.
- **적용하기 (Apply):** 케이블이 연결된 상태와 TCP 연결 상태가 다를 수 있음을 사례에 적용한다.
- **찾아보기 (Lookup):** TCP 상태 이름과 전이는 상태도에서 찾아본다.

## TCP/IP 계층과 데이터 단위
<!-- learn-page-id: segmentation-stream -->

계층별 식별자는 L2의 MAC 주소, L3의 IP 주소, L4의 포트 번호다. 전송 계층의 포트 번호를 논한다면 L4 수준의 정보를 다루는 것이다. 데이터 단위는 Ethernet의 Frame, IP의 Packet, TCP의 Segment, UDP의 Datagram으로 구분한다. TCP 소켓을 사용하는 애플리케이션은 Stream, 즉 연속된 바이트 흐름을 다룬다. 예를 들어 프로그램이 `사진`과 `끝`을 나누어 보내더라도, TCP는 두 번의 전송 요청 경계를 상대 프로그램에 그대로 보존한다고 약속하지 않는다. 받는 프로그램은 `사진끝`처럼 이어진 바이트를 읽을 수도 있으므로, 메시지의 시작과 끝은 애플리케이션 프로토콜이 정한다. TCP 연결이 끝났다는 사실과 사진 한 장의 경계도 구별해야 한다. 웹 통신과의 연결은 뒤의 웹 Unit에서 살펴본다.

TCP는 이 Stream을 한 번에 보내지 않고 MSS(Maximum Segment Size)에 맞춰 여러 Segment로 나눈다. 예를 들어 4MB 파일이라면 수많은 Segment가 된다. 길이가 MSS로 나누어 떨어지지 않으면 마지막 조각은 앞의 조각보다 짧을 수 있다. 수신 측 TCP는 도착한 Segment를 순서대로 다시 이어 애플리케이션에 연속된 Stream으로 넘겨 준다. MSS가 어떤 크기이고 어떻게 정해지는지는 다음 Lesson의 연결 과정에서 이어서 본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP/IP 계층마다 애플리케이션 데이터가 다른 전달 단위로 처리된다.
- **적용하기 (Apply):** 데이터가 Segment에서 Packet과 Frame으로 포장되는 순서를 설명한다.
- **찾아보기 (Lookup):** 각 PDU와 Header 필드는 계층 구조표에서 찾아본다.

## 보냈다는 것과 받았다는 것은 같을까?
<!-- learn-page-id: u7-tcp-delivery-confirmation -->

처음의 사진 다운로드를 이어서 생각해 보자. Unit 4 마지막 Lesson에서는 소켓, 송신 버퍼, 세그먼트, 패킷, 프레임, 수신 버퍼를 거쳐 브라우저가 읽는 전체 흐름을 살펴보았다. 그때는 데이터가 빠짐없이 순서대로 도착한다고 가정했다. 이제는 그 가정을 잠시 내려놓고 ‘보낸 데이터가 도중에 사라지면 어떻게 알까?’를 생각해 보자. 예를 들어 중간 장비에 처리할 데이터가 너무 몰리면 일부 패킷이 버려질 수 있다.

택배를 발송한 판매자에게는 ‘물건을 접수했다’는 사실과 ‘상대가 받았다’는 사실이 다르다. 접수한 물건이 아직 이동 중일 수도 있고, 배송 중 문제가 생겼을 수도 있다. 네트워크에서도 프로그램이 전송을 요청하거나 서버가 데이터를 내보냈다는 것만으로 상대가 받았다고 확정할 수는 없다.

IP는 패킷을 목적지 쪽으로 전달하려고 최선을 다하지만, 데이터가 반드시 도착하거나 순서대로 도착한다고 보장하지는 않는다. IP 자체에는 상대가 어디까지 받았는지 확인하거나, 빠진 데이터를 다시 보내는 기능도 없다. 따라서 IP 패킷에 목적지 주소를 잘 적어 보냈더라도, 송신 측은 그것만으로 사진의 모든 바이트가 도착했는지 알 수 없다.

이 간격을 메우는 TCP의 기능 중 하나가 **확인 응답, ACK(Acknowledgement)**다. 수신 측 TCP는 어디까지 빠짐없이 받았는지 송신 측 TCP에 알려 준다. 택배 수령 문자가 발송자에게 돌아오는 것처럼, 데이터가 가는 방향과 받은 범위를 알리는 응답이 돌아오는 방향을 함께 생각하면 된다.

### ACK는 누가 무엇을 확인하는가?

사진을 받는 브라우저와 PC의 TCP는 역할이 다르다. ACK는 브라우저가 ‘사진을 화면에 띄웠다’고 보내는 메시지가 아니다. **수신 측 TCP가 데이터를 받은 범위에 대한 확인**이다. 아직 브라우저가 소켓에서 읽지 않아 수신 버퍼에 기다리는 바이트도 TCP에서는 이미 받았다고 확인할 수 있다.

그래서 ‘ACK를 받았다’와 ‘상대 프로그램이 처리를 끝냈다’를 구별해야 한다. 예를 들어 사진의 바이트가 PC의 수신 버퍼까지 도착했지만 브라우저는 다른 작업 중일 수 있다. 서버는 TCP 수신 확인을 받았더라도 사진 표시나 저장까지 끝났다고 판단할 수 없다. 애플리케이션의 처리 완료를 알아야 한다면 그 목적에 맞는 애플리케이션 차원의 응답이 필요하다.

ACK는 세그먼트 하나마다 꼭 하나씩 돌아오는 영수증이라고 생각하지 말자. TCP는 받은 바이트의 범위를 확인한다. 여기서는 구체적인 번호를 계산하지 않고 **‘어디까지 받았는지 상대 TCP가 알려 준다’**는 역할을 이해하면 된다. 번호가 어떤 규칙으로 표현되는지는 Unit 8에서 배운다.

### 확인되지 않은 데이터는 다시 보낼 수 있다

송신 측 TCP는 보낸 데이터 중 아직 확인받지 못한 부분을 관리한다. 전달에 문제가 있다고 판단하면 그 바이트를 다시 보낼 수 있다. 이 동작을 **재전송(Retransmission)**이라고 한다. 택배를 보냈는데 수령 여부가 확인되지 않아 같은 물건을 다시 보내는 상황과 닮았다.

응답이 안 왔다고 언제나 데이터 자체가 사라졌다는 뜻은 아니다. 데이터는 도착했지만 확인 응답이 돌아오는 중에 늦어지거나 사라질 수도 있다. 따라서 지금은 ‘ACK가 안 오면 무조건 상대가 못 받았다’고 외우기보다, TCP가 확인되지 않은 데이터를 추적하고 필요하면 재전송해 전달을 이어 간다고 이해하자. TCP도 연결을 복구할 수 없으면 전송 실패를 알릴 수 있으므로 무한히 성공을 보장하는 마법은 아니다.

이 페이지에서 연결할 세 가지는 간단하다. **IP는 목적지로 전달을 시도하고, ACK는 TCP가 받은 범위를 알리며, 재전송은 확인되지 않은 데이터를 다시 보내는 동작이다.** 재전송을 결정하는 구체적인 기준과 번호 계산은 뒤로 두고, 다음 페이지에서는 데이터가 도착한 뒤에도 받을 공간이 부족할 수 있다는 문제를 살펴보자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 송신 완료는 상대 애플리케이션 수신이나 처리 완료를 자동으로 보장하지 않는다.
- **적용하기 (Apply):** 전송 성공·TCP 확인 응답·앱 처리 확인을 서로 다른 단계로 구분한다.
- **찾아보기 (Lookup):** 앱 수준의 처리 완료 보장은 API 응답 설계를 찾아본다.

## 도착했는데 프로그램이 아직 읽지 않았다면?
<!-- learn-page-id: u7-tcp-receive-capacity -->

택배가 집 앞 보관함에 도착했다고 주인이 곧바로 꺼내 쓰는 것은 아니다. 배송 담당자는 계속 물건을 넣고, 주인은 시간이 날 때 꺼내 간다. Unit 4에서 본 수신 소켓 버퍼도 이 보관함처럼, TCP가 받은 바이트를 애플리케이션이 읽기 전까지 잠시 보관하는 메모리 공간이다.

사진 다운로드에서는 PC의 TCP가 수신 버퍼에 데이터를 준비하고, 브라우저가 소켓에서 읽어 자신의 메모리로 가져간다. 데이터가 들어오는 일과 브라우저가 읽는 일은 서로 다른 속도로 진행될 수 있다. 네트워크가 아무리 빨리 데이터를 전달하더라도 브라우저가 읽는 속도가 더 느리면, 수신 버퍼에는 아직 읽지 않은 바이트가 쌓인다.

보관함이 가득 찬 집에 택배를 계속 밀어 넣을 수는 없다. 데이터를 더 보내려는 서버도 PC가 추가로 받아 둘 공간이 있는지 알아야 한다. 이를 알려 주는 것이 **수신 윈도(Receive Window)**다. 수신 측 TCP가 송신 측 TCP에 ‘현재 이 범위의 바이트를 더 받아 둘 수 있다’고 알리는 값이라고 이해하자.

예를 들어 수신 버퍼의 용량을 8,000바이트로 단순화하고, 아직 읽지 않은 데이터가 6,000바이트 있다고 하자. 남은 공간은 2,000바이트다. 브라우저가 2,000바이트를 읽어 가면 기다리는 데이터는 4,000바이트가 되고, 비어 있는 공간도 4,000바이트로 늘어난다. 그림에서 한 칸은 1,000바이트이며, 채워진 칸과 빈칸의 변화를 따라가면 된다.

### 받은 범위와 받을 공간은 다른 정보다

앞 페이지의 ACK는 ‘어디까지 받았는가’를 알렸다. 수신 윈도는 ‘앞으로 더 받아 둘 수 있는 양’을 알린다. 택배 수령 문자에 ‘이번 물건은 받았고, 보관함에는 이만큼 더 들어간다’는 소식을 함께 적는 것과 비슷하다. **이미 받았다는 확인과 추가로 받을 공간은 따로 구별해야 한다.**

TCP는 ACK를 보내는 세그먼트에 수신 윈도 정보도 함께 담아 상대에게 알릴 수 있다. 송신 측은 상대가 알린 수신 윈도의 범위를 고려해 전송량을 조절한다. 프로그램이 데이터를 읽어 여유가 생기면, 수신 측은 달라진 받을 공간을 다시 알릴 수 있다. 이렇게 받는 쪽이 받아 둘 수 있는 양을 고려하는 기능을 **흐름 제어(Flow Control)**라고 부른다.

수신 윈도가 2,000바이트라고 해서 ‘초당 2,000바이트로 보낸다’는 뜻은 아니다. 초당 얼마나 보낼 수 있는가는 속도이고, 수신 윈도는 추가로 받아 둘 수 있는 바이트 범위다. 또한 세그먼트 하나에 담을 수 있는 데이터 크기인 MSS와도 다르다. 배송 상자 하나의 크기와 도착지 보관함에 남은 전체 공간을 나누어 생각하면 된다.

그러므로 ‘길이 빠른데 다운로드가 왜 기다릴까?’라는 질문에는 여러 단계를 살펴볼 필요가 있다. 이 페이지의 예처럼 받는 프로그램이 아직 충분히 읽지 못했을 수도 있다. 수신 윈도가 전송에 영향을 주는 이유는 도로의 속도만 보지 않고 **받는 쪽의 수용 능력도 함께 고려해야 하기 때문**이다.

TCP는 받은 범위를 확인하고, 확인되지 않은 데이터를 다시 보내며, 수신 측이 더 받을 공간을 고려한다. UDP 자체에는 이와 같은 수신 확인·재전송·수신 윈도에 따른 흐름 제어가 없다. UDP를 사용하는 프로그램에 이런 기능이 필요하다면 애플리케이션이나 상위 프로토콜에서 마련해야 한다. UDP의 데이터그램 경계와 사용 방식은 마지막 페이지에서 함께 정리한다.

이제 받은 범위와 더 받을 공간을 구별했다. 마지막으로 UDP는 이 두 TCP 기능을 어떻게 다루는지, 데이터그램 단위와 함께 비교해 보자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP 수신 완료 뒤에도 애플리케이션이 Buffer에서 데이터를 읽기 전까지 대기할 수 있다.
- **적용하기 (Apply):** 네트워크 전달과 프로그램 소비 속도가 다를 때 수신 Buffer 상태를 설명한다.
- **찾아보기 (Lookup):** 소켓 Buffer와 수신 창은 OS·TCP 진단 자료에서 확인한다.

## UDP의 사용 방식 정리

UDP도 소켓과 포트 번호를 사용하지만 TCP의 연결 절차는 없다. 이런 성질을 비연결형(connectionless)이라고 한다. UDP에서는 프로그램이 보낸 데이터그램의 경계가 유지된다. 예를 들어 두 번에 나누어 보낸 두 데이터그램은 각각 별개의 메시지로 다뤄진다. TCP에서는 두 번의 전송 요청이 상대의 두 번 읽기와 일치한다고 보장하지 않는다는 점과 비교하자. UDP 자체는 데이터그램의 도착이나 순서를 보장하지 않는다. 실시간 음성이나 일부 게임 통신에서는 늦게 도착한 오래된 데이터보다 최신 상태가 더 유용할 수 있어 UDP를 선택하기도 한다. 그렇다고 UDP가 언제나 더 빠르거나 손실을 해결해 주는 것은 아니다. 필요한 확인·순서 맞추기·재전송은 사용하는 애플리케이션이나 그 위의 프로토콜이 맡아야 한다. 프로그램이 사용할 포트 번호를 지정할지, 사용 가능한 번호를 운영체제에서 배정받을지는 구성에 따라 달라진다. 연결 유무와 수신 측을 고려하는 방식의 차이를 기본으로 기억하고, 이후 TCP의 연결 과정을 살펴본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** UDP는 연결 설정과 전달 보장을 TCP와 같은 방식으로 제공하지 않는다.
- **적용하기 (Apply):** 지연을 줄이는 실시간 전송에서 손실 처리 책임이 어디 있는지 구분한다.
- **찾아보기 (Lookup):** UDP 사용 앱의 재전송·순서 보장은 앱 프로토콜 문서에서 확인한다.
