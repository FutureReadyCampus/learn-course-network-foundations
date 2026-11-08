---
id: u8-advanced-10-공유기-작동원리-및-개요
title: 사설 주소·공인 주소와 공유기
source_lesson_ids:
- u8-advanced-10-공유기-작동원리-및-개요
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-10.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/03-2.md#p157-b10
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/03-2.md#p158-b02
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/03-2.md#p158-b11
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/03-2.md#p158-b18
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/03-2.md#p159-b03
- https://www.rfc-editor.org/rfc/rfc1918.html
- https://www.rfc-editor.org/rfc/rfc6598.html
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-10.md
page_metadata:
- page_id: advanced-source-10-page-01
  question_placements:
  - question_id: u12-l01-p01-q01
    after_paragraph: 1
  - question_id: u12-l01-p01-q02
    after_paragraph: 2
  questions:
  - id: u12-l01-p01-q01
    kind: choice
    difficulty: easy
    prompt: 집에서 휴대폰과 노트북이 보통 바깥 인터넷으로 통신할 때 함께 거치는 장치는 무엇인가요?
    choices:
    - id: a
      text: 휴대폰만의 전용 회선
      feedback: 본문의 일반적인 가정에서는 기기마다 회선을 따로 신청하지 않고 공유기를 함께 거칩니다.
    - id: b
      text: 공유기
      feedback: 맞아요. 집 안 기기들은 공유기를 거쳐 바깥 인터넷 서비스와 통신합니다.
    - id: c
      text: 노트북만의 전용 회선
      feedback: 노트북도 집 안 네트워크에 연결되어 공유기를 거치는 흐름입니다.
    - id: d
      text: 인터넷에 있는 웹사이트
      feedback: 웹사이트는 통신 상대입니다. 집 안 여러 기기의 출입구 역할은 공유기가 합니다.
    - id: e
      text: 집 안의 다른 휴대폰
      feedback: 본문에서는 다른 휴대폰이 아니라 공유기를 통해 바깥과 통신한다고 설명합니다.
    answer: b
  - id: u12-l01-p01-q02
    kind: choice
    difficulty: medium
    prompt: 공유기가 주소를 자동으로 나눠 주고 무선 접속도 제공한다면, NAT는 어떤 기능을 가리키나요?
    choices:
    - id: a
      text: 기기에 주소를 자동으로 나눠 주는 기능
      feedback: 주소 자동 할당과 NAT는 서로 다른 기능입니다. NAT는 주소를 변환합니다.
    - id: b
      text: 기기를 무선으로 연결하는 기능
      feedback: 무선 접속은 공유기가 제공할 수 있는 별도 기능입니다. NAT는 주소를 바꿉니다.
    - id: c
      text: 공유기가 제공하는 모든 기능의 이름
      feedback: 라우팅·자동 할당·무선 접속을 모두 NAT라고 부르지는 않습니다.
    - id: d
      text: 각 기기에 인터넷 회선을 따로 연결하는 기능
      feedback: 본문의 흐름은 여러 기기가 공유기를 함께 이용하는 것입니다. NAT는 그 과정의 주소 변환입니다.
    - id: e
      text: 바깥과 통신하도록 주소를 바꾸는 기능
      feedback: 맞아요. 여러 기능이 한 공유기에 들어 있어도 NAT는 네트워크 주소 변환을 뜻합니다.
    answer: e
  illustrations:
  - file: assets/diagrams/source-10.svg
    title: 사설 주소와 공인 주소 사이에서 동작하는 NAT
    alt: 집 안 기기의 사설 IP 주소가 공유기를 지나 외부에 보이는 주소로 바뀌는 흐름
    caption: 여러 기기가 공유기 하나를 거쳐 인터넷을 이용하는 큰 흐름을 살펴본다.
    after_paragraph: -1
- page_id: advanced-source-10-page-02
  question_placements:
  - question_id: u12-l01-p02-q01
    after_paragraph: 1
  - question_id: u12-l01-p02-q02
    after_paragraph: 3
  questions:
  - id: u12-l01-p02-q01
    kind: choice
    difficulty: easy
    prompt: 집 안 노트북의 사설 IP 주소는 주로 어디에서 기기를 구분하는 데 쓰이나요?
    choices:
    - id: a
      text: 그 집의 내부 네트워크
      feedback: 맞아요. 사설 IP는 내부 네트워크에서 기기를 구분하기 위한 주소입니다.
    - id: b
      text: 공용 인터넷 전체
      feedback: 사설 IP는 전 세계 목적지를 찾는 주소로 공용 인터넷에 그대로 전달되지 않습니다.
    - id: c
      text: 같은 주소를 쓰는 모든 집을 합친 네트워크
      feedback: 서로 다른 집에서 같은 사설 IP를 써도 각 집 안에서만 의미가 있습니다.
    - id: d
      text: 인터넷에 연결된 모든 웹사이트
      feedback: 노트북의 사설 IP는 집 안 기기를 구분합니다. 인터넷 전체의 웹사이트를 구분하지 않습니다.
    - id: e
      text: 인터넷 회사의 모든 고객을 합친 네트워크
      feedback: 사설 주소의 의미는 해당 내부 네트워크에 한정됩니다. 모든 고객을 하나로 구분하는 주소가 아닙니다.
    answer: a
  - id: u12-l01-p02-q02
    kind: choice
    difficulty: medium
    prompt: 어떤 기기가 공인 IP를 쓴다는 사실만 확인했습니다. 외부에서 그 기기에 접속할 수 있을까요?
    choices:
    - id: a
      text: 공인 IP이므로 누구나 바로 접속할 수 있습니다
      feedback: 본문은 공인 IP를 사용해도 누구나 접속할 수 있다는 뜻은 아니라고 설명합니다.
    - id: b
      text: 공인 IP이므로 방화벽 규칙은 접속에 영향을 주지 않습니다
      feedback: 공인 IP여도 방화벽 규칙은 실제 접속 가능성을 결정하는 조건입니다.
    - id: c
      text: 공인 IP이므로 외부 접속은 언제나 차단됩니다
      feedback: 공인이라는 말은 차단 여부를 뜻하지 않습니다. 접속 조건을 따로 확인해야 합니다.
    - id: d
      text: 주소만으로는 부족하며 라우팅·변환 기록·방화벽 조건도 봐야 합니다
      feedback: 맞아요. 공인 IP라는 사실과 실제 접속 가능성은 구별해야 합니다.
    - id: e
      text: 공인 IP이므로 그 기기는 안전하다고 판단할 수 있습니다
      feedback: 공인과 사설은 주소의 사용 범위 구분이지 안전과 위험의 등급이 아닙니다.
    answer: d
- page_id: advanced-source-10-page-03
  question_placements:
  - question_id: u12-l01-p03-q01
    after_paragraph: 1
  - question_id: u12-l01-p03-q02
    after_paragraph: 3
  questions:
  - id: u12-l01-p03-q01
    kind: choice
    difficulty: easy
    prompt: 노트북의 요청이 일반적인 가정용 공유기를 지나 나갈 때, NAT는 출발지 주소를 어떻게 바꾸나요?
    choices:
    - id: a
      text: 노트북의 사설 IP를 웹사이트의 주소로 바꿉니다
      feedback: 웹사이트는 목적지입니다. 출발지에는 공유기 바깥쪽 주소가 사용됩니다.
    - id: b
      text: 공유기 바깥쪽 주소를 노트북의 사설 IP로 바꿉니다
      feedback: 이 문제는 바깥으로 나가는 요청입니다. 안쪽 사설 IP가 바깥쪽 주소로 바뀝니다.
    - id: c
      text: 노트북의 사설 IP를 공유기 바깥쪽 주소로 바꿉니다
      feedback: 맞아요. 웹사이트는 집 안 사설 IP 대신 공유기 쪽 주소를 보고 응답합니다.
    - id: d
      text: 노트북의 사설 IP를 그대로 두고 전달합니다
      feedback: 본문의 NAT 흐름에서는 요청이 나갈 때 출발지 주소가 바뀝니다.
    - id: e
      text: 노트북의 사설 IP를 다른 집 기기의 사설 IP로 바꿉니다
      feedback: 공유기는 자기 바깥쪽 주소로 바꿉니다. 다른 집의 사설 IP를 빌리는 흐름이 아닙니다.
    answer: c
  - id: u12-l01-p03-q02
    kind: choice
    difficulty: medium
    prompt: 여러 기기가 같은 바깥쪽 주소로 통신한 뒤 응답이 돌아왔습니다. 공유기는 무엇을 이용해 통신을 구별하나요?
    choices:
    - id: a
      text: 포트 번호도 사용한 변환 기록
      feedback: 맞아요. 바깥 IP가 같아도 주소와 포트를 연결한 기록으로 안쪽 통신을 구별할 수 있습니다.
    - id: b
      text: 공유기의 바깥 IP 주소 하나만
      feedback: 여러 기기가 같은 바깥 주소를 쓰므로 IP 주소 하나만으로 구별하기에는 부족합니다.
    - id: c
      text: 응답을 받은 순간 새로 고른 내부 기기
      feedback: 응답은 임의로 고른 기기가 아니라 해당 통신의 변환 기록에 맞춰 전달합니다.
    - id: d
      text: 모든 내부 기기에 똑같이 보내는 방식
      feedback: 본문에서는 변환 기록으로 어느 기기의 응답인지 알아내 전달한다고 설명합니다.
    - id: e
      text: 웹사이트가 알고 있는 각 기기의 사설 IP 목록
      feedback: 본문의 웹사이트는 공유기 쪽 주소를 봅니다. 내부 통신 구별은 공유기의 기록을 이용합니다.
    answer: a
- page_id: advanced-source-10-page-04
  question_placements:
  - question_id: u12-l01-p04-q01
    after_paragraph: 1
  - question_id: u12-l01-p04-q02
    after_paragraph: 3
  questions:
  - id: u12-l01-p04-q01
    kind: choice
    difficulty: easy
    prompt: 흔한 가정용 NAT에 기존 변환 기록과 맞지 않는 외부 패킷이 도착하면 어떤 일이 생길 수 있나요?
    choices:
    - id: a
      text: 모든 내부 기기에 자동으로 복사됩니다
      feedback: 본문의 NAT는 기록에 맞지 않는 패킷을 모든 내부 기기에 보내지 않습니다.
    - id: b
      text: 항상 내부의 첫 번째 기기에 전달됩니다
      feedback: 어느 기기로 보낼지는 통신 기록과 규칙이 필요합니다. 첫 기기로 무조건 보내지 않습니다.
    - id: c
      text: 외부에서 왔으므로 항상 전달됩니다
      feedback: 외부 패킷이라고 자동으로 허용되는 것은 아닙니다. 기록과 수신 조건이 필요합니다.
    - id: d
      text: 사설 IP를 쓰므로 안전한 패킷으로 인정됩니다
      feedback: 사설 주소라는 사실만으로 패킷의 안전성을 판단할 수 없습니다.
    - id: e
      text: 어느 내부 기기로 보낼지 몰라 전달되지 않을 수 있습니다
      feedback: 맞아요. 기록에 맞지 않는 패킷을 전달하지 않아 외부 접속이 막히는 효과가 생길 수 있습니다.
    answer: e
  - id: u12-l01-p04-q02
    kind: choice
    difficulty: medium
    prompt: 게임 연결을 위해 공유기에 외부에서 들어오는 길을 설정했습니다. NAT와 방화벽에 대한 올바른 판단은 무엇인가요?
    choices:
    - id: a
      text: NAT가 있으므로 공유기와 PC의 방화벽은 필요 없습니다
      feedback: NAT의 목적은 주소 변환입니다. 공유기와 PC의 방화벽 규칙은 별도로 존재할 수 있습니다.
    - id: b
      text: NAT와 별개로 방화벽의 허용·차단 규칙을 확인해야 합니다
      feedback: 맞아요. 주소 변환과 보안 규칙은 별개이며, 외부 수신 경로가 생길 수도 있습니다.
    - id: c
      text: 사설 주소를 쓰므로 설정 후에도 무조건 안전합니다
      feedback: 본문은 사설 주소를 쓴다는 이유로 무조건 안전하다고 결론 내릴 수 없다고 설명합니다.
    - id: d
      text: NAT는 외부 통신을 전부 차단하므로 설정은 의미가 없습니다
      feedback: 포트 포워딩이나 UPnP로 외부에서 들어오는 길을 설정할 수 있습니다.
    - id: e
      text: NAT와 방화벽은 같은 기능이므로 하나만 확인하면 됩니다
      feedback: NAT는 주소 변환, 방화벽은 보안 규칙에 따른 허용·차단을 담당합니다.
    answer: b
- page_id: advanced-source-10-page-05
  question_placements:
  - question_id: u12-l01-p05-q01
    after_paragraph: 1
  - question_id: u12-l01-p05-q02
    after_paragraph: 2
  questions:
  - id: u12-l01-p05-q01
    kind: choice
    difficulty: easy
    prompt: 외부에서 시작된 패킷을 받아들이는 조건은 모든 NAT 장비에서 같을까요?
    choices:
    - id: a
      text: NAT를 사용하면 항상 같은 조건입니다
      feedback: NAT라는 공통 이름만으로 모든 장비의 수신 조건이 같다고 볼 수 없습니다.
    - id: b
      text: 내부 기기가 같으면 설정과 무관하게 같습니다
      feedback: 본문은 장비와 설정에 따라 외부 패킷 허용 조건이 달라진다고 설명합니다.
    - id: c
      text: 통신 상대나 포트가 바뀌어도 언제나 같습니다
      feedback: 상대나 포트가 달라지면 다른 기록을 만들 수도 있습니다. 언제나 같다고 단정할 수 없습니다.
    - id: d
      text: 장비와 설정에 따라 달라질 수 있습니다
      feedback: 맞아요. 변환 기록을 만드는 방식과 외부 패킷을 허용하는 조건은 장비·설정에 따라 다를 수 있습니다.
    - id: e
      text: NAT는 외부에서 시작된 패킷을 모두 허용합니다
      feedback: 어떤 외부 패킷을 허용하는지는 별도의 조건으로 살펴봐야 합니다.
    answer: d
  - id: u12-l01-p05-q02
    kind: choice
    difficulty: medium
    prompt: NAT 이름만으로 동작을 판단하기 어렵다면, 어떤 두 기준을 나누어 살펴봐야 하나요?
    choices:
    - id: a
      text: 예전 NAT 유형의 이름과 그 이름으로 추정한 보안 정도
      feedback: 예전 NAT 이름만으로 실제 동작이나 보안 정도를 판단하기 어렵다고 설명합니다.
    - id: b
      text: 사설 주소의 첫 숫자와 기기 수
      feedback: 이 페이지의 비교 기준은 바깥 주소·포트 결정 방식과 외부 패킷 허용 조건입니다.
    - id: c
      text: 바깥 주소·포트를 정하는 방식과 외부 패킷 허용 조건
      feedback: 맞아요. 주소·포트 연결 방식과 외부 수신 조건을 나누어 봐야 실제 동작을 이해할 수 있습니다.
    - id: d
      text: 외부 패킷 허용 조건만 두 번 비교
      feedback: 주소·포트를 어떻게 정하는지도 별개로 살펴봐야 합니다. 수신 조건만으로는 부족합니다.
    - id: e
      text: 바깥 주소를 정하는 방식만 두 번 비교
      feedback: 바깥 주소 결정과 어떤 외부 패킷을 받아들이는가는 서로 구분할 기준입니다.
    answer: c
- page_id: advanced-source-10-page-06
  question_placements:
  - question_id: u12-l01-p06-q01
    after_paragraph: 1
  - question_id: u12-l01-p06-q02
    after_paragraph: 3
  questions:
  - id: u12-l01-p06-q01
    kind: choice
    difficulty: easy
    prompt: 집 안 기기가 연결되는 쪽과 ISP 쪽을 공유기 기준으로 각각 무엇이라고 하나요?
    choices:
    - id: a
      text: 집 안은 WAN, ISP 쪽은 LAN
      feedback: 두 방향이 바뀌었습니다. 본문에서는 집 안이 LAN, ISP 쪽이 WAN입니다.
    - id: b
      text: 집 안은 LAN, ISP 쪽은 WAN
      feedback: 맞아요. LAN과 WAN은 공유기를 기준으로 어느 쪽 연결인지 나타냅니다.
    - id: c
      text: 양쪽 모두 LAN
      feedback: 공유기 안쪽 LAN과 ISP로 이어지는 바깥쪽 WAN을 구분합니다.
    - id: d
      text: 양쪽 모두 WAN
      feedback: 집 안 기기가 연결되는 쪽은 LAN이라고 합니다.
    - id: e
      text: 안전한 쪽은 LAN, 위험한 쪽은 WAN
      feedback: LAN과 WAN은 좋고 나쁜 쪽이 아니라 연결 위치를 나타냅니다.
    answer: b
  - id: u12-l01-p06-q02
    kind: choice
    difficulty: medium
    prompt: 집 안 노트북의 주소가 바뀌었습니다. 공유기의 바깥 주소에 대해 옳은 설명은 무엇인가요?
    choices:
    - id: a
      text: 안쪽 주소와 똑같은 값으로 반드시 바뀝니다
      feedback: 안쪽과 바깥쪽 주소를 같은 것으로 보면 안 됩니다. 한쪽 변화가 다른 쪽 변화로 반드시 이어지지 않습니다.
    - id: b
      text: 노트북 주소가 바뀔 때마다 반드시 바뀝니다
      feedback: 본문은 안쪽 주소가 바뀌어도 바깥 주소가 반드시 함께 바뀌지는 않는다고 설명합니다.
    - id: c
      text: WAN이 사라지고 LAN만 남습니다
      feedback: 기기 주소 변경과 LAN·WAN의 연결 위치 구분은 다른 문제입니다.
    - id: d
      text: 공유기가 있는 동안 바깥 주소는 절대 바뀌지 않습니다
      feedback: 반드시 함께 바뀌지 않는다는 말은 영원히 고정된다는 뜻이 아닙니다. 구성과 할당 조건을 봐야 합니다.
    - id: e
      text: 바깥 주소가 반드시 함께 바뀌는 것은 아닙니다
      feedback: 맞아요. 안쪽과 바깥쪽은 다른 네트워크이며, 주소 할당과 NAT 구성에 따라 달라집니다.
    answer: e
- page_id: advanced-source-10-page-07
  question_placements:
  - question_id: u12-l01-p07-q01
    after_paragraph: 2
  - question_id: u12-l01-p07-q02
    after_paragraph: 3
  questions:
  - id: u12-l01-p07-q01
    kind: choice
    difficulty: easy
    prompt: 표에 있는 세 사설 IPv4 범위 중 하나에 속하는 주소는 무엇인가요?
    choices:
    - id: a
      text: 192.167.3.25
      feedback: 192로 시작하는 주소가 모두 사설은 아닙니다. 표의 해당 범위는 192.168입니다.
    - id: b
      text: 172.15.1.9
      feedback: 172로 시작하는 사설 범위는 두 번째 숫자가 16부터 31까지입니다.
    - id: c
      text: 192.168.3.25
      feedback: 맞아요. 192.168.0.0부터 192.168.255.255까지의 범위에 속합니다.
    - id: d
      text: 172.32.1.9
      feedback: 172.32는 표의 상한인 172.31을 벗어납니다.
    - id: e
      text: 11.4.2.8
      feedback: 표의 첫 범위는 10.0.0.0부터 10.255.255.255입니다. 11로 시작하면 그 범위가 아닙니다.
    answer: c
  - id: u12-l01-p07-q02
    kind: choice
    difficulty: medium
    prompt: 친구가 “172로 시작하면 모두 사설 IP야”라고 말합니다. 표를 기준으로 어떻게 고치면 될까요?
    choices:
    - id: a
      text: 172.16.0.0부터 172.31.255.255까지가 사설 범위입니다
      feedback: 맞아요. 첫 숫자 172만 보지 말고 정해진 시작과 끝 범위 안에 있는지 확인해야 합니다.
    - id: b
      text: 172.0.0.0부터 172.255.255.255까지가 사설 범위입니다
      feedback: 172 전체가 아닙니다. 두 번째 숫자가 16부터 31인 범위입니다.
    - id: c
      text: 172.16.0.0부터 172.16.255.255까지만 사설 범위입니다
      feedback: 시작 부분만 본 것입니다. 표의 범위는 172.31.255.255까지 이어집니다.
    - id: d
      text: 172.16.0.0부터 172.32.255.255까지가 사설 범위입니다
      feedback: 두 번째 숫자 32는 포함되지 않습니다. 상한은 172.31.255.255입니다.
    - id: e
      text: 172.0.0.0부터 172.15.255.255까지가 사설 범위입니다
      feedback: 표의 사설 범위는 172.16부터 시작합니다. 제시한 범위는 그보다 앞에 있습니다.
    answer: a
- page_id: advanced-source-10-page-08
  question_placements:
  - question_id: u12-l01-p08-q01
    after_paragraph: 1
  - question_id: u12-l01-p08-q02
    after_paragraph: 3
  questions:
  - id: u12-l01-p08-q01
    kind: choice
    difficulty: easy
    prompt: 통신사급 NAT인 CGNAT는 이 페이지에서 어떤 구성으로 설명하나요?
    choices:
    - id: a
      text: 집 공유기가 무선 접속 기능만 제공하는 구성
      feedback: CGNAT는 무선 접속의 이름이 아니라 인터넷 회사 쪽의 추가 주소 변환을 뜻합니다.
    - id: b
      text: 집 안 모든 기기에 공인 주소를 하나씩 주는 구성
      feedback: 본문의 CGNAT는 여러 고객이 공인 주소를 함께 사용하도록 추가 NAT를 두는 경우입니다.
    - id: c
      text: 집 공유기를 제거하고 사설 주소를 그대로 인터넷에 보내는 구성
      feedback: CGNAT가 있으면 집 공유기와 인터넷 회사 장비에서 각각 주소 변환이 일어날 수 있습니다.
    - id: d
      text: 인터넷 회사가 여러 고객의 공인 주소 공유를 위해 추가 NAT를 두는 구성
      feedback: 맞아요. 집 공유기 외에 인터넷 회사 쪽에서 주소를 한 번 더 변환할 수 있습니다.
    - id: e
      text: 인터넷 회사가 모든 주소 변환을 없애는 구성
      feedback: CGNAT는 변환을 없애는 것이 아니라 인터넷 회사 쪽 NAT를 추가하는 구성입니다.
    answer: d
  - id: u12-l01-p08-q02
    kind: choice
    difficulty: medium
    prompt: WAN 주소가 100.64.0.0/10 범위인 집 공유기에 포트 포워딩을 설정했지만 외부 접속이 안 됩니다. 본문에 맞는 판단은 무엇인가요?
    choices:
    - id: a
      text: 공유기 WAN이므로 반드시 공인 주소이고 통신사 NAT는 무관합니다
      feedback: WAN 주소가 항상 공인 주소는 아닙니다. 본문은 이 범위를 통신사 네트워크의 공유용 대역으로 설명합니다.
    - id: b
      text: 통신사 NAT 쪽 수신 경로도 필요할 수 있으며 다른 조건도 살펴봅니다
      feedback: 맞아요. 이 공유용 대역에서는 통신사 NAT를 고려해야 하지만 주소 하나로 모든 문제를 설명할 수는 없습니다.
    - id: c
      text: 이 범위는 집 안 RFC 1918 사설 범위이므로 통신사 NAT와 무관합니다
      feedback: 100.64.0.0/10은 집 안에서 쓰는 RFC 1918 사설 범위와 별개의 공유용 대역입니다.
    - id: d
      text: 집 공유기 설정만 완료되면 외부 접속은 반드시 됩니다
      feedback: 통신사 NAT에도 외부에서 들어오는 길이 필요할 수 있어 집 공유기 설정만으로 충분하지 않을 수 있습니다.
    - id: e
      text: 이 주소가 보이면 모든 인터넷 연결 문제의 원인이 확정됩니다
      feedback: 본문은 주소 대역 하나만으로 모든 인터넷 연결 문제를 설명할 수는 없다고 덧붙입니다.
    answer: b
- page_id: advanced-source-10-page-09
  question_placements:
  - question_id: u12-l01-p09-q01
    after_paragraph: 1
  - question_id: u12-l01-p09-q02
    after_paragraph: 3
  questions:
  - id: u12-l01-p09-q01
    kind: choice
    difficulty: easy
    prompt: 노트북이 보낸 웹 요청의 응답이 공유기로 돌아오면, 공유기는 무엇에 따라 노트북으로 전달하나요?
    choices:
    - id: a
      text: 해당 통신 기록
      feedback: 맞아요. 공유기는 요청과 연결된 통신 기록에 따라 응답을 내부 기기로 전달합니다.
    - id: b
      text: 공유기에 마지막으로 연결한 기기
      feedback: 최근 연결한 기기가 응답의 주인은 아닙니다. 해당 요청과 응답을 연결하는 통신 기록을 이용합니다.
    - id: c
      text: 그때 켜져 있는 기기 전체
      feedback: 본문에서는 모든 기기가 아니라 해당 통신의 노트북으로 응답을 전달합니다.
    - id: d
      text: 웹사이트가 새로 지정한 사설 IP
      feedback: 본문의 흐름에서는 공유기가 해당 통신 기록으로 내부 노트북에 응답을 돌려줍니다.
    - id: e
      text: 공유기 바깥 주소만 보고 임의로 고른 기기
      feedback: 응답을 임의로 나누지 않습니다. 안쪽 기기와 연결된 통신 기록을 이용합니다.
    answer: a
  - id: u12-l01-p09-q02
    kind: choice
    difficulty: medium
    prompt: 공유기 한 상자가 패킷 전달과 주소 변환을 함께 수행합니다. 두 역할을 어떻게 구별하면 좋을까요?
    choices:
    - id: a
      text: 공유기는 주소만 변환하고 NAT가 장치로서 패킷을 전달합니다
      feedback: 장치와 기능의 역할이 뒤바뀌었습니다. 공유기가 전달하고 NAT는 주소 변환 기능입니다.
    - id: b
      text: 공유기와 NAT는 같은 뜻이므로 구별할 필요가 없습니다
      feedback: 본문은 한 상자에 여러 기능이 있어도 개념을 각각 구분해서 이해해야 한다고 설명합니다.
    - id: c
      text: 공유기는 네트워크 사이에서 전달하고 NAT는 주소를 변환합니다
      feedback: 맞아요. 한 장치에서 함께 수행해도 패킷 전달을 맡는 장치와 주소 변환 기능을 구분합니다.
    - id: d
      text: 공유기는 사설 IP의 다른 이름이고 NAT는 공인 IP의 다른 이름입니다
      feedback: 주소의 종류와 장치·기능을 섞은 설명입니다. 사설·공인은 주소이고 공유기·NAT는 장치와 기능입니다.
    - id: e
      text: 공유기는 집 안 주소만 쓰고 NAT를 써도 주소는 바뀌지 않습니다
      feedback: 본문의 공유기는 서로 다른 네트워크 사이에서 전달하며 NAT는 그 과정의 주소 정보를 바꿉니다.
    answer: c
---

## 공유기는 여러 기기의 인터넷 출입구다

<!-- learn-page-id: advanced-source-10-page-01 -->

집에서 휴대폰과 노트북으로 같은 인터넷을 쓸 때, 두 기기가 각자 인터넷 회사에 회선을 신청하지는 않는다. 보통 두 기기는 공유기 안쪽의 집 네트워크(LAN)에 연결되고, 공유기의 바깥쪽(WAN)은 인터넷 서비스 제공자(ISP) 쪽으로 이어진다. 공유기는 두 네트워크 사이에서 패킷이 갈 길을 안내하는 라우터 역할을 한다. 집에서 쓰는 한 상자 안에는 이 라우팅에 더해 주소 변환(NAT), 주소 자동 할당(DHCP), 무선 접속점(Wi-Fi) 같은 기능이 함께 들어 있는 경우가 많다.

LAN과 WAN은 안전한 쪽과 위험한 쪽의 이름이 아니라 공유기를 기준으로 한 안쪽과 바깥쪽이다. 많은 가정용 IPv4 네트워크는 LAN의 기기에 사설 IP 주소를 쓰고, NAT(Network Address Translation, 네트워크 주소 변환)가 바깥 통신에 맞는 주소로 바꾼다. 여기서는 한 집에 공유기가 하나 있고 인터넷 회사가 공유기에 IPv4 주소를 주는 경우를 먼저 살펴본다.

**기억할 점:** 기기 여러 대가 인터넷을 함께 쓰는 큰 흐름의 중심에는 공유기가 있고, NAT는 그중 주소를 바꾸는 기능이다.

## 공인 IP와 사설 IP는 쓰이는 범위가 다르다

<!-- learn-page-id: advanced-source-10-page-02 -->

공인 IP 주소(Public IP address)는 인터넷에서 네트워크와 목적지를 구분하고 패킷을 전달하는 데 쓰이는 주소다. 사설 IP 주소(Private IP address)는 집이나 회사처럼 내부 네트워크에서 기기를 구분하기 위해 마련된 주소다. 예를 들어 집 안 노트북에 `192.168.0.25`가 설정되어 있다면, 이 주소는 그 집 네트워크 안에서 노트북을 찾는 데 쓰인다.

사설 IP 주소는 공용 인터넷에서 전 세계 목적지를 찾는 주소로 그대로 전달되지 않는다. 서로 떨어진 두 집에서 같은 `192.168.0.25`를 사용해도 괜찮은 이유가 여기에 있다. 두 주소는 각자 자기 집 네트워크 안에서만 의미가 있기 때문이다. 반면 외부 서비스로 가는 통신은 집 안 주소만으로는 목적지까지 이어지지 않으므로, 공유기 바깥에서 쓸 주소와 연결해야 한다.

공인과 사설은 주소가 안전한지, 위험한지를 나타내는 말이 아니다. 또 공인 IP를 사용한다고 누구나 그 기기에 접속할 수 있다는 뜻도 아니다. 실제 접속 가능성은 라우팅, NAT의 변환 기록, 방화벽 규칙 같은 조건에 따라 달라진다.

**기억할 점:** 사설 IP는 내부에서 기기를 찾는 주소이고, 공인 IP는 공용 인터넷과 통신할 때 사용하는 주소다.

## NAT는 사설 주소를 바꾸어 외부 통신을 이어 준다

<!-- learn-page-id: advanced-source-10-page-03 -->

노트북이 웹사이트에 요청을 보낼 때 요청 패킷의 출발지 주소는 노트북의 사설 IP다. 이 패킷이 공유기를 지나 인터넷으로 나갈 때 공유기는 출발지 주소를 자기 바깥쪽 주소로 바꾸어 전달한다. 여기서는 인터넷 회사가 추가로 NAT를 하지 않는 경우를 생각한다. 바깥의 웹사이트는 집 안 노트북의 사설 IP가 아니라 공유기 쪽 주소를 보고 응답을 보낸다.

응답이 공유기로 돌아오면 공유기는 어느 안쪽 기기의 통신에 대한 응답인지 알아내 사설 네트워크로 전달해야 한다. 예를 들어 노트북과 휴대폰이 같은 웹사이트에 동시에 접속하면 두 요청의 목적지 주소가 같을 수 있다. 공유기 바깥 주소 하나만 기록하면 돌아온 응답을 어느 기기로 보낼지 구별하기 어렵다. 그래서 공유기는 TCP나 UDP 통신을 구분하는 포트 번호도 주소와 함께 기록하고, 각 안쪽 통신과 바깥 통신을 연결한다. 이 주소·포트 연결 기록의 한 줄 한 줄을 다음 Lesson에서 따라가 본다.

NAT는 Network Address Translation의 줄임말이며, 말 그대로 네트워크 주소를 변환하는 기술이다. 공유기는 요청이 나갈 때 패킷의 주소 정보를 바꾸고, 응답이 돌아오면 변환 기록을 이용해 안쪽 기기로 전달한다. 인터넷에서 쓰는 주소를 집 안 기기마다 따로 하나씩 두는 대신, 여러 기기가 공유기 바깥 주소를 함께 사용할 수 있다.

**기억할 점:** 공유기는 바깥으로 나가는 주소를 바꾸고, 돌아오는 응답은 통신 기록에 맞춰 안쪽 기기로 전달한다.

## NAT가 있다고 방화벽이 필요 없는 것은 아니다

<!-- learn-page-id: advanced-source-10-page-04 -->

외부에서 먼저 시작한 통신이 공유기에 도착하면, 공유기는 어느 내부 기기로 보내야 하는지 모를 수 있다. 흔한 가정용 NAT는 통신을 시작할 때 만든 변환 기록과 맞지 않는 패킷을 안쪽 기기로 전달하지 않는다. 그 결과 원치 않는 외부 접속이 막히는 효과가 생기기도 한다.

하지만 이를 NAT 자체가 방화벽이라는 뜻으로 받아들이면 안 된다. NAT의 목적은 주소 변환이고, 방화벽의 목적은 정해 둔 보안 규칙에 따라 통신을 허용하거나 차단하는 것이다. 공유기와 PC에는 각각 별도의 방화벽 규칙이 있을 수 있다. 포트 포워딩은 바깥의 특정 포트로 온 통신을 안쪽 기기와 연결하도록 설정하는 기능이다. 일부 공유기는 UPnP(Universal Plug and Play)를 이용해 프로그램이 이런 포트 연결을 자동으로 요청하도록 지원한다. 둘 다 필요한 연결을 허용하는 설정이므로, 무엇을 열었는지 확인해야 한다. “사설 주소를 쓰면 무조건 안전하다”거나 “NAT가 있으니 방화벽은 필요 없다”고 결론 내릴 수 없다.

외부에서 기기로 직접 연결해야 하는 게임·화상 통화·P2P 프로그램은 NAT의 변환 방식 때문에 연결에 어려움을 겪을 수 있다. 이것은 NAT가 무조건 통신을 차단하기 때문이 아니라, 상대가 먼저 보낸 패킷을 어느 내부 기기에 연결할지 정하는 규칙과 기록이 필요하기 때문이다. 다음 Lesson들에서 변환표와 수신 허용 조건을 살펴보면 이 차이를 더 정확히 볼 수 있다.

**기억할 점:** NAT는 주소를 바꾸고, 방화벽은 규칙에 따라 통신을 허용하거나 막는다.

## NAT의 동작 방식은 한 가지가 아니다

<!-- learn-page-id: advanced-source-10-page-05 -->

공유기는 내부 기기의 통신을 바깥 주소와 연결할 때 변환 기록을 만든다. 이 동작에는 서로 다른 두 질문이 있다. 첫째, 내부 기기의 주소와 포트를 바깥에서 어떤 주소·포트로 나타낼까? 둘째, 외부에서 시작한 패킷이 왔을 때 어떤 조건을 만족하면 안쪽으로 들여보낼까? 예를 들어 바깥쪽 포트를 새 통신마다 다르게 배정할 수 있고, 응답은 먼저 안에서 통신을 시작한 상대에게서만 받아들이도록 제한할 수 있다. 주소·포트 배정 방식과 외부 패킷 허용 조건은 관련은 있지만 같은 기준은 아니다.

예전 설명 자료에는 Full Cone, Restricted Cone, Port Restricted Cone, Symmetric 같은 NAT 이름이 자주 나온다. 이 이름들은 두 질문에 대한 조합을 과거의 몇 가지 유형으로 나눠 설명한 것이다. 다만 실제 공유기의 동작은 장비와 설정에 따라 달라질 수 있어 이름 하나만으로 동작이나 보안 수준을 단정하기 어렵다. 이 Lesson에서 기억할 것은 유형 이름이 아니라, “바깥 주소·포트를 어떻게 배정하는가”와 “어떤 외부 패킷을 받아들이는가”라는 두 가지 확인 기준이다. 다음 Lesson에서는 변환표를 보고 주소와 포트가 연결되는 모습을, 그 다음 Lesson에서는 배정 방식과 수신 조건의 차이를 구체적으로 살펴본다.

이 페이지에서는 그 두 기준의 이름과 세부 차이를 외우지 않는다. 다음 Lesson에서 먼저 변환표 한 줄이 통신을 어떻게 이어 주는지 확인한 뒤, 그 다음 Lesson에서 매핑과 수신 필터링을 나누어 비교한다.

**기억할 점:** NAT를 이해할 때는 바깥 주소를 만드는 방식과 외부 패킷을 허용하는 조건을 구분한다.

## 공유기 안쪽과 바깥쪽은 다른 네트워크다

<!-- learn-page-id: advanced-source-10-page-06 -->

첫 페이지에서 본 LAN은 공유기 안쪽의 집 네트워크이고 WAN은 인터넷 회사 쪽 연결이다. 공유기 뒷면에서 집 안 기기를 꽂는 포트와 인터넷 회선을 꽂는 포트를 구별할 때도 이 이름을 볼 수 있다. 실제 장비에서는 무선 LAN처럼 케이블을 꽂지 않는 연결도 LAN에 포함될 수 있으므로, LAN을 단순히 “랜선 구멍”이라고만 생각하지 않는다.

일반적인 가정용 IPv4 구성에서는 LAN 쪽 기기가 사설 주소를 사용하고, WAN 쪽에는 인터넷 회사가 제공한 주소가 설정된다. 공유기는 두 쪽 사이에서 패킷을 전달하면서 NAT를 적용할 수 있다. 그림을 볼 때 “이 주소는 공유기 안쪽 기기의 주소인가, 공유기 바깥쪽 인터페이스의 주소인가?”를 먼저 물으면 각 주소가 어디에서 쓰이는지 정리하기 쉽다.

안쪽 주소가 바뀌어도 바깥 주소가 반드시 함께 바뀌는 것은 아니다. 주소를 누가 할당하는지, 어느 구간에서 NAT를 하는지는 네트워크 구성에 따라 다르다. 가정용 공유기에서는 내부 기기가 주소를 자동으로 받는 경우가 흔하지만, 큰 조직에서는 다른 장비나 서버가 주소를 관리할 수도 있다.

**기억할 점:** LAN은 공유기 안쪽, WAN은 공유기 바깥쪽 연결을 가리킨다.

## 사설 IPv4 주소는 세 범위로 정해져 있다

<!-- learn-page-id: advanced-source-10-page-07 -->

사설 주소는 아무 IPv4 주소나 골라 쓰는 것이 아니다. 사설 네트워크에서 사용할 수 있도록 RFC 1918이라는 인터넷 표준 문서에 정해 둔 세 범위가 있다. 아래 표의 `/8`, `/12`, `/16`은 주소 범위를 나타내는 접두사 표기다. 범위 계산을 이 페이지에서 다시 하지 않아도 된다. 특히 `172`로 시작하는 주소가 전부 사설인 것은 아니다. 사설 범위는 `172.16`부터 `172.31`까지다.

| 사설 주소 범위 | 주소가 시작하고 끝나는 곳 | 예 |
| --- | --- | --- |
| `10.0.0.0/8` | `10.0.0.0`–`10.255.255.255` | `10.4.2.8` |
| `172.16.0.0/12` | `172.16.0.0`–`172.31.255.255` | `172.20.1.9` |
| `192.168.0.0/16` | `192.168.0.0`–`192.168.255.255` | `192.168.0.25` |

공유기 관리 화면이나 기기 네트워크 설정에서 이 범위의 주소를 자주 보게 된다. 주소를 보았을 때 첫 숫자만 보고 판단하지 말고, 표에 적힌 범위 안에 있는지 확인하자. 이 세 범위는 IPv4 사설 주소를 나누는 기준이며, 예전 A·B·C 클래스의 구분으로 외울 필요는 없다.

**기억할 점:** 자주 보이는 사설 IPv4 대역은 `10/8`, `172.16/12`, `192.168/16` 세 가지다.

## 인터넷 회사가 주소를 한 번 더 바꿀 수도 있다

<!-- learn-page-id: advanced-source-10-page-08 -->

앞의 기본 그림에서는 인터넷 회사가 집 공유기에 공인 IPv4 주소를 바로 준다고 가정했다. 하지만 기숙사나 원룸처럼 여러 집이 건물 출입구 하나를 함께 쓰는 것처럼, 인터넷 회사도 여러 고객이 공인 주소를 함께 사용하도록 중간에 추가 NAT를 둘 수 있다. 이를 통신사급 NAT(Carrier-Grade NAT, CGNAT)라고 한다.

CGNAT가 있으면 주소 변환이 두 번 일어날 수 있다. 첫 번째로 집 공유기가 집 안 사설 주소와 자기 WAN 주소 사이를 변환한다. 두 번째로 인터넷 회사의 장비가 그 WAN 주소를 인터넷에서 사용할 공인 주소와 연결한다. 인터넷 회사와 연결된 공유기의 WAN 주소가 `100.64.0.0/10` 범위라면, 이는 일반적인 공인 주소가 아니라 통신사 네트워크에서 공유용으로 쓰는 주소 대역이다. 이 대역은 앞 페이지 표에 나온 집 안 사설 주소 범위와는 별개다.

이런 구성에서는 집 공유기에서 포트 포워딩을 설정하는 것만으로 외부 접속이 되지 않을 수 있다. 인터넷 회사 쪽 NAT에도 외부에서 들어오는 길이 필요하기 때문이다. 포트 포워딩이나 게임 연결 문제를 살펴볼 때 공유기의 WAN 주소가 공인 주소인지 확인하는 이유가 여기에 있다. 다만 주소 대역 하나만으로 모든 인터넷 연결 문제를 설명할 수 있는 것은 아니다.

**기억할 점:** 집 공유기 뒤에 인터넷 회사의 NAT가 한 겹 더 있을 수 있으므로, 공유기의 WAN 주소가 항상 공인 IP인 것은 아니다.

## 공유기와 NAT의 역할을 구분해 정리하자

<!-- learn-page-id: advanced-source-10-page-09 -->

한 집의 노트북이 `192.168.0.25`라는 사설 IP로 웹사이트에 요청을 보낸다고 하자. 공유기는 안쪽에서 바깥쪽으로 패킷을 전달하고 NAT로 주소 정보를 바꾼다. 웹사이트의 응답이 돌아오면 공유기는 해당 통신 기록에 따라 노트북으로 응답을 전달한다. 인터넷 회사 쪽에 CGNAT가 있으면 공유기와 인터넷 회사의 장비가 각각 주소 변환을 수행할 수도 있다.

핵심 용어를 다시 구별해 보자. **사설 IP**는 내부 네트워크에서 기기를 구분하는 주소다. **공인 IP**는 공용 인터넷에서 네트워크를 구분하고 통신을 이어 가는 데 쓰인다. **공유기**는 서로 다른 네트워크 사이에서 패킷을 전달하는 장치이며, **NAT**는 전달 과정에서 주소를 변환하는 기능이다. 가정용 공유기에는 여러 기능이 한 상자에 함께 들어갈 수 있지만, 개념은 각각 구분해서 이해해야 한다.

이 페이지에서는 흔한 가정용 IPv4 흐름을 살펴봤다. 실제 서비스에서는 IPv6, 통신사 NAT, 방화벽 설정 등에 따라 주소와 연결 방법이 달라질 수 있다. 다음 Lesson에서는 한 통신의 요청과 응답을 변환표로 따라가며, 주소뿐 아니라 포트가 왜 필요한지도 구체적으로 확인한다.

**한 줄 정리:** 사설 주소가 공유기와 NAT를 거쳐 외부 통신에 쓰이고, 응답은 그 통신 기록을 따라 내부 기기로 돌아온다.
