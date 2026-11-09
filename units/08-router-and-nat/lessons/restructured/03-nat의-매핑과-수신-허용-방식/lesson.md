---
id: advanced-nat-mapping-filtering
title: NAT의 매핑과 수신 허용 방식
source_lesson_ids:
- u8-advanced-12-full-cone-방식과-내부-네트워크-접속-문제
- u8-advanced-13-restricted-cone-방식
- u8-advanced-14-port-restricted-cone-방식
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-12.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-13.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-14.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/03-2.md#p158-b18
- https://www.rfc-editor.org/rfc/rfc4787.html
- https://www.rfc-editor.org/rfc/rfc5128.html
- https://www.rfc-editor.org/rfc/rfc8656.html
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-12.md
page_metadata:
- page_id: advanced-nat-mapping-filtering-page-01
  questions:
  - id: u12-l03-p01-q01
    kind: choice
    difficulty: easy
    prompt: NAT 뒤의 두 기기가 인터넷에서 서로 직접 통신하기 어려울 수 있는 주된 이유는 무엇인가요?
    choices:
    - id: a
      text: 두 기기가 같은 사설 IP 주소를 항상 사용하기 때문
      feedback: 사설 주소가 겹칠 수는 있지만, 여기서 핵심은 외부에서 보낸 패킷을 어느 내부 기기로 전달할지 NAT가 알 수 있는 기록과 조건이 필요하다는 점이다.
    - id: b
      text: 외부에서 먼저 온 패킷을 어느 내부 주소로 보낼지 NAT가 모를 수 있기 때문
      feedback: 맞다. 외부에서 먼저 온 패킷은 해당 통신을 내부의 어느 기기로 연결할지 알려 주는 매핑이 없을 수 있다.
    - id: c
      text: NAT가 인터넷의 모든 패킷을 암호화하기 때문
      feedback: NAT는 주소와 포트를 변환하고 통신 기록을 관리한다. 모든 패킷을 암호화하는 장비라는 뜻은 아니다.
    - id: d
      text: P2P 프로그램은 TCP만 사용할 수 있기 때문
      feedback: P2P는 여러 전송 방식을 이용할 수 있다. 여기서는 NAT를 통과해 서로 직접 통신하는 조건을 살펴본다.
    - id: e
      text: 각 기기에 공인 IP가 직접 할당되지 않으면 P2P가 불가능하기 때문
      feedback: 공인 IP가 각 기기에 직접 할당되지 않아도 NAT 통과 조건이 맞으면 직접 통신을 시도할 수 있다. 성공 여부는 매핑과 필터링에 달려 있다.
    answer: b
    feedback: NAT의 매핑과 필터링 조건이 맞으면 직접 통신할 수 있지만, 외부에서 온 패킷을 내부로 전달할 근거가 없으면 어려울 수 있다.
  - id: u12-l03-p01-q02
    kind: choice
    difficulty: medium
    prompt: P2P 통신에 대한 설명으로 가장 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 모든 데이터가 반드시 중앙 서버를 거쳐야 하는 통신
      feedback: P2P는 피어끼리 직접 데이터를 주고받는 방식이다. 연결을 소개하거나 설정하는 서버가 함께 쓰일 수는 있다.
    - id: b
      text: NAT를 사용하지 않는 기기에서만 가능한 통신
      feedback: NAT 뒤의 기기끼리도 조건이 맞으면 직접 통신을 시도할 수 있다. 다만 성공이 보장되지는 않는다.
    - id: c
      text: 공유기가 내부 기기의 사설 주소를 인터넷에 그대로 공개하는 통신
      feedback: 사설 주소는 일반적으로 인터넷에서 직접 라우팅되지 않는다. NAT 환경에서는 외부에서 보이는 주소와 포트를 이용한다.
    - id: d
      text: 두 피어가 직접 데이터를 주고받는 통신 방식
      feedback: 맞다. 중간 서버는 상대를 소개하거나 연결 정보를 전달할 수 있지만, P2P에서는 데이터가 피어 사이를 직접 오갈 수 있다.
    - id: e
      text: 피어끼리 통신하려면 반드시 같은 공인 IP 주소를 사용해야 하는 방식
      feedback: 피어가 같은 공인 IP를 쓸 필요는 없다. 서로의 외부 주소·포트를 알아내고 NAT 조건이 맞으면 직접 통신을 시도한다.
    answer: d
    feedback: P2P는 피어 간 직접 데이터 교환을 뜻하며, 연결 설정을 돕는 서버가 있어도 데이터 경로는 직접일 수 있다.
  question_placements:
    - question_id: u12-l03-p01-q01
      after_paragraph: 1
    - question_id: u12-l03-p01-q02
      after_paragraph: 3
- page_id: advanced-nat-mapping-filtering-page-02
  questions:
  - id: u12-l03-p02-q01
    kind: choice
    difficulty: easy
    prompt: NAT에서 매핑(Mapping)이 답하는 질문은 무엇인가요?
    choices:
    - id: a
      text: 어느 서비스에 로그인할 수 있도록 허용할까?
      feedback: 로그인 권한은 애플리케이션의 인증 기능이다. NAT 매핑은 IP 주소와 포트를 연결한다.
    - id: b
      text: 다음 패킷을 어느 공유기 인터페이스로 내보낼까?
      feedback: 패킷을 어느 출구로 전달할지는 경로 선택에 관한 질문이다. NAT의 매핑은 내부와 외부의 통신 주소·포트를 연결한다.
    - id: c
      text: 어느 외부 출발지의 패킷을 내부로 들여보낼까?
      feedback: 이는 들어오는 패킷을 허용할 조건, 즉 필터링이 답하는 질문이다. 매핑은 내부와 외부 주소·포트를 연결한다.
    - id: d
      text: 어떤 DNS 이름을 어느 서버 IP로 바꿀까?
      feedback: DNS 이름 조회는 NAT 매핑과 다른 기능이다. 매핑은 내부·외부의 통신 주소와 포트를 짝짓는다.
    - id: e
      text: 어떤 내부 주소·포트와 어떤 외부 주소·포트를 서로 연결할까?
      feedback: 맞다. 매핑은 내부 통신의 주소·포트를 NAT 바깥에서 보이는 주소·포트와 짝짓는다.
    answer: e
    feedback: 예를 들어 내부 192.168.0.10:3000을 외부에서 보이는 203.0.113.8:42000과 연결하는 것이 매핑이다.
  - id: u12-l03-p02-q02
    kind: choice
    difficulty: medium
    prompt: 매핑과 필터링을 구분한 설명으로 옳은 것은 무엇인가요?
    choices:
    - id: a
      text: 매핑은 외부 상대를 허용하고, 필터링은 내부 포트를 정한다
      feedback: 두 개념의 역할이 뒤바뀌었다. 매핑은 내부와 외부 주소·포트의 연결이고, 필터링은 외부에서 온 패킷을 허용할 조건이다.
    - id: b
      text: 매핑과 필터링은 모두 패킷의 암호화 방식이다
      feedback: 둘 다 암호화 방식이 아니다. 주소·포트 연결과 수신 조건을 각각 설명하는 NAT 동작이다.
    - id: c
      text: 매핑은 목적지 서버의 주소이고, 필터링은 DNS 이름이다
      feedback: 매핑은 서버의 목적지 주소를 뜻하지 않고 내부·외부 통신을 연결한다. 필터링도 DNS 이름을 뜻하지 않는다.
    - id: d
      text: 매핑은 TCP에만 있고 필터링은 UDP에만 있다
      feedback: 이 Lesson의 세부 행동 유형은 주로 UDP NAT를 설명하지만, 용어의 역할을 TCP와 UDP로 나누는 것은 아니다.
    - id: e
      text: 매핑은 주소 관계, 필터링은 허용할 외부 출발지 조건을 다룬다
      feedback: 맞다. 매핑이 내부 통신을 외부 주소·포트에 연결하고, 필터링이 그 매핑으로 어떤 외부 출발지의 패킷을 받을지 정한다.
    answer: e
    feedback: 두 질문을 따로 보면 동작이 선명해진다. “어떤 외부 주소를 쓰나?”는 매핑, “어떤 외부 발신자를 받나?”는 필터링이다.
  question_placements:
    - question_id: u12-l03-p02-q01
      after_paragraph: 1
    - question_id: u12-l03-p02-q02
      after_paragraph: 3
- page_id: advanced-nat-mapping-filtering-page-03
  questions:
  - id: u12-l03-p03-q01
    kind: choice
    difficulty: easy
    prompt: Endpoint-Independent Mapping에서는 같은 내부 주소·포트가 다른 외부 상대와 통신할 때 보통 어떻게 매핑되나요?
    choices:
    - id: a
      text: 외부 상대가 바뀔 때마다 항상 다른 외부 포트를 쓴다
      feedback: 이는 목적지에 따라 매핑을 다르게 만드는 동작에 가깝다. Endpoint-Independent Mapping은 외부 상대와 관계없이 같은 외부 매핑을 유지한다.
    - id: b
      text: 외부 상대의 도메인 이름을 내부 포트로 복사한다
      feedback: 매핑은 도메인 이름을 복사하지 않는다. 내부 주소·포트에 대응하는 외부 주소·포트를 정한다.
    - id: c
      text: 같은 내부 주소·포트라면 목적지와 무관하게 같은 외부 매핑을 재사용한다
      feedback: 맞다. Endpoint-Independent Mapping(EIM)은 목적지 IP나 포트가 바뀌어도 같은 내부 endpoint에 같은 외부 매핑을 사용한다.
    - id: d
      text: 내부 포트가 같으면 외부 목적지와 관계없이 다른 외부 포트를 배정한다
      feedback: EIM은 같은 내부 endpoint에 대해 외부 목적지가 바뀌어도 같은 외부 매핑을 사용한다. 목적지마다 다른 포트를 쓰는 동작은 목적지 종속 매핑에 가깝다.
    - id: e
      text: 목적지 웹 서버의 포트 번호를 내부 포트로 복사한다
      feedback: 목적지 포트가 내부 포트로 복사되는 것은 EIM의 정의가 아니다. EIM은 내부 endpoint에 대응하는 바깥 endpoint가 목적지와 무관하게 유지되는 동작이다.
    answer: c
    feedback: EIM의 핵심은 외부 목적지가 달라져도 같은 내부 endpoint의 외부 매핑이 유지된다는 점이다.
  - id: u12-l03-p03-q02
    kind: choice
    difficulty: medium
    prompt: 같은 내부 주소·포트가 서로 다른 외부 목적지와 통신할 때 외부 매핑이 목적지에 따라 달라진다면, 무엇을 나타내는 동작인가요?
    choices:
    - id: a
      text: Endpoint-Independent Mapping
      feedback: EIM은 같은 내부 endpoint에 대해 외부 목적지와 무관하게 같은 매핑을 사용한다.
    - id: b
      text: Endpoint-Independent Filtering
      feedback: EIF는 들어오는 패킷을 어떤 외부 출발지에서 허용할지에 관한 필터링 동작이다. 매핑을 만드는 기준이 아니다.
    - id: c
      text: Address-and-Port-Dependent Filtering
      feedback: 이는 외부에서 온 패킷의 출발지 IP와 포트를 확인하는 필터링 유형이다. 질문은 외부 목적지에 따라 매핑이 달라지는 동작을 묻는다.
    - id: d
      text: Endpoint-Dependent Mapping
      feedback: 맞다. Endpoint-Dependent Mapping에서는 외부 목적지 주소 또는 목적지 endpoint가 달라질 때 다른 외부 매핑을 사용할 수 있다.
    - id: e
      text: Address-Dependent Filtering
      feedback: ADF는 외부에서 온 패킷의 출발지 IP를 확인하는 필터링 유형이다. 질문은 외부 목적지에 따라 매핑이 달라지는 동작을 묻는다.
    answer: d
    feedback: 이 동작은 목적지에 의존하는 매핑이다. 예전 Symmetric NAT라는 이름에서 핵심 차이로 다루던 부분이지만, 요즘은 매핑과 필터링을 따로 설명하는 편이 명확하다.
  question_placements:
    - question_id: u12-l03-p03-q01
      after_paragraph: 2
    - question_id: u12-l03-p03-q02
      after_paragraph: 4
- page_id: advanced-nat-mapping-filtering-page-04
  questions:
  - id: u12-l03-p04-q01
    kind: choice
    difficulty: easy
    prompt: Address-Dependent Filtering은 어느 외부 패킷을 허용하나요?
    choices:
    - id: a
      text: 이전에 통신한 원격 IP 주소에서 온 패킷
      feedback: 맞다. 원격 IP가 이전 목적지 IP와 같으면 허용할 수 있고, 그 IP의 출발지 포트는 달라도 된다.
    - id: b
      text: 이전에 보낸 적 없는 모든 IP와 포트에서 온 패킷
      feedback: Address-Dependent Filtering은 아무 출발지나 허용하지 않는다. 이전에 통신한 원격 IP 주소를 확인한다.
    - id: c
      text: 원격 IP 주소는 같고 출발지 포트만 다른 패킷
      feedback: 이 경우는 Address-Dependent Filtering에서 허용할 수 있다. 질문의 유형은 그보다 좁게 원격 IP와 포트를 모두 확인한다.
    - id: d
      text: 원격 IP와 포트가 모두 이전 기록과 같은 패킷만
      feedback: IP와 포트 모두 확인하는 것은 Address-and-Port-Dependent Filtering이다. Address-Dependent Filtering은 IP 주소만 비교한다.
    - id: e
      text: 다른 원격 IP에서 왔지만 출발지 포트가 같은 패킷
      feedback: 포트만 같다고 허용되는 것은 아니다. Address-Dependent Filtering은 IP를, Address-and-Port-Dependent Filtering은 IP와 포트를 함께 확인한다.
    answer: a
    feedback: 원격 IP 주소가 기록과 같으면 허용하는 유형이다. 출발지 포트까지 맞아야 하는 것은 아니다.
  - id: u12-l03-p04-q02
    kind: choice
    difficulty: medium
    prompt: 내부 기기가 15.15.15.15:5555로 먼저 패킷을 보냈습니다. Address-and-Port-Dependent Filtering에서 15.15.15.15:7777의 패킷은 어떻게 처리될 수 있나요?
    choices:
    - id: a
      text: 무조건 허용된다. 같은 IP이면 포트는 확인하지 않는다
      feedback: 이 설명은 Address-Dependent Filtering에 해당한다. Address-and-Port-Dependent Filtering은 IP와 포트를 함께 확인한다.
    - id: b
      text: 출발지 IP가 같아도 포트가 다르므로 허용되지 않을 수 있다
      feedback: 맞다. 이 유형은 이전에 통신한 원격 IP와 원격 포트가 모두 맞는지 확인한다.
    - id: c
      text: 내부 기기의 포트를 7777로 바꾸어 패킷을 전달한다
      feedback: 필터링은 내부 포트를 7777로 고쳐 주는 동작이 아니다. 외부에서 온 패킷의 출발지 조건이 기록과 맞는지 검사한다.
    - id: d
      text: 같은 IP에서 왔으므로 포트와 관계없이 허용된다
      feedback: 같은 IP만 보는 것은 Address-Dependent Filtering의 기준이다. Address-and-Port-Dependent Filtering은 포트도 비교한다.
    - id: e
      text: 내부 기기가 응답 패킷을 먼저 다시 보내야만 NAT가 출발지 포트를 확인한다
      feedback: 필터링은 들어오는 패킷의 출발지 정보를 기존 허용 조건과 비교한다. 이 문제에서는 원격 IP와 포트가 다르므로 통과하지 않을 수 있다.
    answer: b
    feedback: IP는 같지만 포트가 다르다. 주소와 포트에 종속된 필터링에서는 기존 통신 상대 endpoint와 다르므로 허용되지 않을 수 있다.
  question_placements:
    - question_id: u12-l03-p04-q01
      after_paragraph: 2
    - question_id: u12-l03-p04-q02
      after_paragraph: 3
- page_id: advanced-nat-mapping-filtering-page-05
  questions:
  - id: u12-l03-p05-q01
    kind: choice
    difficulty: easy
    prompt: 전통적인 Cone NAT 분류에서 Port Restricted Cone을 이해하는 핵심은 무엇인가요?
    choices:
    - id: a
      text: 외부에서 오는 패킷의 출발지 IP와 포트 조건을 모두 확인한다
      feedback: 맞다. 전통적 설명에서 Port Restricted Cone은 이전에 통신한 외부 IP뿐 아니라 포트도 확인한다.
    - id: b
      text: 패킷의 출발지 IP와 포트를 전혀 확인하지 않는다
      feedback: 이는 Full Cone의 전통적 설명에 가깝다. Port Restricted Cone은 외부 출발지 IP와 포트를 함께 제한한다.
    - id: c
      text: 이전에 통신한 원격 IP 주소만 확인하고 포트는 무시한다
      feedback: 이는 Address-Dependent Filtering의 설명이다. Port Restricted Cone의 전통적 설명은 원격 IP와 포트를 함께 확인한다.
    - id: d
      text: 내부 포트마다 별도의 공인 IP 주소를 새로 신청한다
      feedback: 이 분류는 공인 IP 신청 절차를 뜻하지 않는다. NAT 매핑과 외부 출발지 허용 조건을 설명한다.
    - id: e
      text: 내부에서 시작한 모든 통신을 외부 상대와 상관없이 같은 기준으로 받아들인다
      feedback: 외부 상대와 무관하게 받아들이는 설명은 Full Cone의 전통적 필터링 특성에 가깝다. Port Restricted Cone은 IP와 포트를 확인한다.
    answer: a
    feedback: 전통적 용어에서는 외부에서 온 출발지 IP와 포트가 이전에 통신한 상대와 맞는지 확인한다.
  - id: u12-l03-p05-q02
    kind: choice
    difficulty: medium
    prompt: Full Cone, Restricted Cone, Port Restricted Cone이라는 이름을 오늘날 NAT 동작을 설명할 때 다루는 방법으로 가장 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 세 이름만 알면 모든 공유기 동작을 정확히 예측할 수 있다
      feedback: 실제 구현은 다양하며 이름만으로 모든 동작을 예측할 수 없다. 매핑과 필터링을 따로 보는 편이 더 분명하다.
    - id: b
      text: 이 세 이름만으로 매핑과 필터링 동작을 각각 정확히 구분할 수 있다
      feedback: 세 이름은 여러 동작을 한데 묶은 전통적 분류다. 정확히 비교하려면 매핑과 필터링을 각각 확인해야 한다.
    - id: c
      text: 오늘날의 모든 NAT 표준에서 이 세 이름을 필수로 사용한다
      feedback: 현재의 행동 요구사항은 매핑과 필터링 기준을 구분해 기술한다. Cone 용어는 오래된 통합 분류로 다룬다.
    - id: d
      text: 매핑과 필터링의 차이를 익힌 뒤 과거 분류와 연결해 읽는다
      feedback: 맞다. 이 이름은 두 동작 기준을 함께 묶어 설명한 전통적 분류로 소개하고, 모든 장비에 그대로 적용하지 않는다.
    - id: e
      text: 포트 포워딩과 같은 관리자의 고정 전달 규칙을 뜻한다
      feedback: Cone 이름은 NAT의 매핑·필터링 동작을 설명하던 분류다. 관리자가 만든 포트 포워딩 규칙과는 다른 개념이다.
    answer: d
    feedback: Cone 이름을 외우는 것보다 매핑과 필터링이 각각 어떤 기준으로 동작하는지 이해하는 것이 중요하다.
  question_placements:
    - question_id: u12-l03-p05-q01
      after_paragraph: 2
    - question_id: u12-l03-p05-q02
      after_paragraph: 3
- page_id: advanced-nat-mapping-filtering-page-06
  questions:
  - id: u12-l03-p06-q01
    kind: choice
    difficulty: easy
    prompt: UDP 홀 펀칭이 시도하는 일은 무엇인가요?
    choices:
    - id: a
      text: 두 피어가 서로의 사설 주소만 사용해 인터넷 라우터를 우회한다
      feedback: 사설 주소는 보통 인터넷에서 직접 찾아갈 수 없다. 피어들은 외부에서 보이는 주소와 포트를 교환해 연결을 시도한다.
    - id: b
      text: 두 피어가 서로에게 먼저 UDP 패킷을 보내 NAT에 매핑을 만들고, 그 매핑을 이용해 직접 통신을 시도한다
      feedback: 맞다. 양쪽이 먼저 바깥으로 패킷을 보내면 NAT에 매핑이 생기고, 필터링 조건도 허용할 때 직접 통신을 시도할 수 있다.
    - id: c
      text: STUN 서버가 게임 영상 전체를 대신 전송한다
      feedback: STUN은 외부에서 관찰되는 주소 정보를 알아내는 데 도움을 준다. 데이터를 계속 전달하는 중계는 TURN 같은 별도 역할이다.
    - id: d
      text: 각 피어가 소개 서버에만 패킷을 보내고 상대에게는 패킷을 보내지 않는다
      feedback: 소개 서버와 통신하는 것만으로 직접 P2P 경로가 생기지는 않는다. 각 피어가 상대의 외부 주소·포트로도 패킷을 보내야 한다.
    - id: e
      text: 연결 시도 뒤에도 상대가 바깥에서 보이는 주소를 알 필요가 없다
      feedback: 피어가 서로의 외부 주소·포트를 알아야 해당 주소로 패킷을 보낼 수 있다. 홀 펀칭은 이 정보와 NAT 상태를 이용한다.
    answer: b
    feedback: 양쪽이 외부 주소로 패킷을 보내고 응답을 주고받아 직접 경로를 만들 수 있는지 확인한다. 성공이 항상 보장되지는 않는다.
  - id: u12-l03-p06-q02
    kind: choice
    difficulty: medium
    prompt: P2P 연결을 소개하거나 외부에서 보이는 주소를 알려 주는 서버가 있다고 해서, 그 서버가 항상 데이터도 중계한다고 볼 수 있나요?
    choices:
    - id: a
      text: 그렇다. 주소를 알려 주는 서버는 반드시 영상과 음성도 모두 전달한다
      feedback: 연결 정보를 알려 주는 역할과 실제 데이터를 중계하는 역할은 다를 수 있다. 직접 연결에 성공하면 데이터는 피어 사이로 흐를 수 있다.
    - id: b
      text: 그렇다. NAT가 있으면 어떤 방식에서도 직접 통신할 수 없다
      feedback: NAT가 있어도 조건이 맞으면 직접 통신을 시도할 수 있다. 단, 실패할 수 있으므로 중계 대안도 준비할 수 있다.
    - id: c
      text: 아니다. 소개 서버와 데이터 중계 서버는 역할이 다르며, 연결이 직접 되면 데이터는 피어 사이로 흐를 수 있다
      feedback: 맞다. Rendezvous/signaling 서버는 상대와 연결 정보를 교환하도록 돕고, TURN 서버는 직접 경로가 안 될 때 데이터를 릴레이한다.
    - id: d
      text: 아니다. 소개 서버와 데이터 경로가 분리되면 피어는 연결 정보를 교환하고 직접 데이터를 보낼 수 있다
      feedback: 이 설명이 맞다. 소개 서버가 연결 정보를 전달해도 실제 데이터가 항상 그 서버를 지나는 것은 아니다.
    - id: e
      text: 아니다. Rendezvous 서버는 연결 정보를 전달할 수 있지만, 직접 연결이 안 되면 별도의 중계가 필요할 수 있다
      feedback: 역할을 잘 구분했다. 소개 서버는 피어를 연결하도록 돕고, 직접 연결이 실패하면 TURN 같은 서버가 실제 데이터를 전달할 수 있다.
    answer: c
    feedback: 소개·주소 확인과 실제 데이터 전달은 다른 역할이다. 이 차이를 알아야 P2P와 TURN 중계를 구분할 수 있다.
  question_placements:
    - question_id: u12-l03-p06-q01
      after_paragraph: 6
    - question_id: u12-l03-p06-q02
      after_paragraph: 7
- page_id: advanced-nat-mapping-filtering-page-07
  questions:
  - id: u12-l03-p07-q01
    kind: choice
    difficulty: easy
    prompt: 홀 펀칭을 시도해도 직접 P2P 연결이 되지 않을 때 데이터를 전달할 대안은 무엇인가요?
    choices:
    - id: a
      text: TURN 같은 중계 서버
      feedback: 맞다. TURN은 직접 통신 경로를 만들기 어려울 때 서버가 피어 사이의 데이터를 중계하도록 한다.
    - id: b
      text: DHCP 서버
      feedback: DHCP는 네트워크 기기에 주소 설정을 제공한다. 피어 사이의 데이터를 이어 주는 중계 서버가 아니다.
    - id: c
      text: STUN 서버
      feedback: STUN은 외부에서 보이는 주소를 알아내는 데 도움을 주지만, 일반적으로 직접 연결 실패 뒤 데이터를 대신 전달하는 역할은 TURN이 맡는다.
    - id: d
      text: 포트 포워딩 규칙
      feedback: 포트 포워딩은 관리자가 특정 외부 포트를 내부 주소·포트에 연결하는 설정이다. 서로 다른 NAT 환경의 피어 데이터를 중계하는 서버는 아니다.
    - id: e
      text: UPnP 요청
      feedback: UPnP는 프로그램이 공유기에 포트 설정을 요청할 수 있게 돕지만, 여러 NAT를 건너 피어 사이 데이터를 전달하는 중계 서버는 아니다.
    answer: a
    feedback: TURN은 중계 주소를 제공해 직접 연결이 어려운 두 피어의 트래픽을 이어 준다.
  - id: u12-l03-p07-q02
    kind: choice
    difficulty: medium
    prompt: 홀 펀칭과 TURN에 대한 설명으로 옳은 것은 무엇인가요?
    choices:
    - id: a
      text: 둘 다 모든 NAT 구성에서 직접 통신을 보장한다
      feedback: 홀 펀칭은 매핑과 필터링, 네트워크 구성에 따라 실패할 수 있다. TURN은 실패한 경우 데이터를 중계하는 대안이다.
    - id: b
      text: TURN은 외부 주소를 알려 주기만 하고 데이터를 전달하지 않는다
      feedback: 외부 주소를 알아내는 역할과 달리 TURN은 실제 피어 간 데이터를 릴레이한다.
    - id: c
      text: 직접 연결이 실패하면 TURN이 데이터를 중계할 수 있지만 서버 자원이 더 든다
      feedback: 맞다. 중계는 연결 가능성을 높이는 대안이지만 서버가 트래픽을 전달하므로 전송량과 자원이 든다.
    - id: d
      text: 홀 펀칭은 포트 포워딩과 같은 수동 설정이다
      feedback: 홀 펀칭은 애플리케이션이 통신을 시도해 NAT의 동적 상태를 활용한다. 포트 포워딩은 관리자가 규칙을 직접 등록한다.
    - id: e
      text: TURN은 NAT의 매핑이나 필터링과 관계없는 암호화 방식이다
      feedback: TURN은 NAT traversal을 위한 중계 프로토콜이다. 데이터 암호화 방식 자체를 뜻하지 않는다.
    answer: c
    feedback: 직접 경로를 우선 시도하고, 만들 수 없으면 TURN 중계로 전환할 수 있다. 어느 방식도 네트워크 조건을 무시하지는 않는다.
  question_placements:
    - question_id: u12-l03-p07-q01
      after_paragraph: 2
    - question_id: u12-l03-p07-q02
      after_paragraph: 3
---

## NAT 뒤에서 피어끼리 만나기 어려운 이유

<!-- learn-page-id: advanced-nat-mapping-filtering-page-01 -->

Unit 12 Lesson 2에서는 내부 기기가 먼저 통신을 시작하면 NAT가 안쪽 주소·포트와 바깥에서 보이는 주소·포트를 연결해 기록하는 과정을 살펴봤다. 웹처럼 기기가 서버에 먼저 요청하는 통신은 이 기록을 이용해 응답을 되돌릴 수 있다. 그런데 두 기기가 서로 데이터를 주고받는 P2P(peer-to-peer, 피어 간 통신)에서는 한쪽이 보낸 첫 패킷을 상대의 NAT가 받아들일지 문제가 된다.

P2P는 중앙 서버가 모든 데이터를 전달하는 대신, 두 피어가 직접 데이터를 주고받는 방식이다. 게임의 상태 정보나 음성·영상처럼 양쪽이 자주 데이터를 교환하는 서비스에서 직접 경로를 만들면 중계 서버의 부담을 줄일 수 있다. 다만 연결을 시작할 때 상대를 소개하거나 주소 정보를 알려 주는 서버를 함께 사용할 수 있으며, 그런 서버가 있다고 해서 모든 데이터가 반드시 그 서버를 지난다는 뜻은 아니다.

각 피어는 보통 공유기나 NAT 뒤에 있어 내부 사설 주소만으로는 인터넷의 상대가 바로 찾아오기 어렵다. NAT는 안쪽에서 먼저 만들어진 통신 기록을 보고 응답을 되돌릴 수 있지만, 외부에서 갑자기 도착한 패킷은 어느 내부 기기로 보내야 할지 모를 수 있다. 이때 패킷을 받아들이는 기준은 공유기마다 다를 수 있다. NAT는 주소 변환 기능이며, 그 존재만으로 내부 네트워크의 안전이 보장되는 것은 아니다.

**기억할 점:** NAT 뒤의 피어끼리 직접 통신하려면 외부 주소·포트의 매핑과 외부 패킷을 허용하는 조건이 모두 맞아야 한다.

## 매핑과 필터링은 서로 다른 질문이다

<!-- learn-page-id: advanced-nat-mapping-filtering-page-02 -->

NAT의 동작을 이해할 때는 먼저 두 질문을 분리한다. **매핑(mapping)**은 내부 기기의 주소·포트에 바깥에서 보이는 어떤 주소·포트를 짝지을지 정한다. **필터링(filtering)**은 그 바깥 주소·포트로 들어온 패킷 가운데 어떤 외부 출발지에서 온 것을 통과시킬지 정한다. Lesson 2에서 변환표의 한 행을 읽었다면, 이제 그 행을 어떻게 만들고 어떤 응답을 받아들이는지 따로 보는 것이다.

예를 들어 내부 `192.168.0.10:3000`이 외부 서버 `15.15.15.15:5555`로 UDP 패킷을 보냈고 NAT가 이를 `203.0.113.8:42000`으로 내보냈다고 하자. 매핑을 보면 안쪽 endpoint와 바깥 endpoint가 어떻게 연결됐는지 알 수 있다. 필터링을 보면 `203.0.113.8:42000`으로 돌아오는 패킷을 `15.15.15.15`에서만 받을지, 그 IP의 `5555` 포트까지 맞아야 받을지 판단할 수 있다.

| 구분 | 답하는 질문 | 이 예에서 보는 것 |
|---|---|---|
| 매핑 | 안쪽 통신을 바깥에서 어떤 주소·포트로 보이게 할까? | `192.168.0.10:3000` ↔ `203.0.113.8:42000` |
| 필터링 | 바깥에서 어떤 출발지의 패킷을 받아들일까? | `15.15.15.15`인지, 그중 `:5555`까지 같은지 |

**기억할 점:** 매핑은 “어떤 바깥 주소로 나가나?”, 필터링은 “누가 보낸 패킷을 받나?”에 답한다. 둘을 하나의 NAT 종류 이름으로 뭉뚱그리면 실제 차이를 놓치기 쉽다.

## 매핑은 외부 상대에 따라 달라질 수 있다

<!-- learn-page-id: advanced-nat-mapping-filtering-page-03 -->

**endpoint**는 IP 주소와 포트의 한 쌍을 말한다. 내부 기기의 같은 UDP endpoint가 외부 목적지를 바꾸어 통신할 때 NAT가 같은 바깥 endpoint를 계속 쓸 수도 있고, 목적지에 따라 다른 바깥 endpoint를 배정할 수도 있다. 이처럼 내부 endpoint를 바깥 endpoint에 연결하는 기준을 매핑 동작이라고 한다.

**Endpoint-Independent Mapping(EIM, 목적지 독립 매핑)**에서는 같은 내부 IP·포트가 같은 외부 IP·포트에 연결된다. 목적지가 `15.15.15.15:5555`에서 `9.9.9.9:40000`으로 바뀌어도 같은 외부 매핑을 재사용할 수 있다. 반대로 **Endpoint-Dependent Mapping(목적지 종속 매핑)**에서는 목적지 IP 또는 IP와 포트 조합에 따라 다른 외부 매핑을 쓸 수 있다. “외부 서버가 바뀌면 항상 포트가 바뀐다”는 뜻은 아니며, NAT가 매핑을 정하는 동작을 구분하는 말이다.

이 차이는 P2P 연결 시도에 영향을 준다. 피어가 중계·소개 서버와 통신할 때 얻은 외부 주소가 다른 피어에게 보낼 때도 그대로 유효하면 직접 연결을 시도하기 쉽다. 목적지가 바뀌면 외부 매핑도 달라지는 장비에서는 소개 서버가 관찰한 주소를 다른 피어에게 그대로 알려도 맞지 않을 수 있다.

RFC 4787은 UDP NAT 동작을 설명하며 목적지와 무관한 매핑을 요구사항으로 둔다. 실제 장비와 네트워크 설정은 서로 다를 수 있으므로, 오래된 Cone 분류의 이름만 보고 지금 사용하는 공유기의 동작을 단정하지 않는다. 이 Lesson의 매핑·필터링 표는 UDP 통신을 이해하기 위한 기준이다.

**기억할 점:** 매핑을 비교할 때는 “같은 내부 통신이 다른 외부 상대와 통신해도 같은 바깥 주소·포트를 쓰는가?”를 묻는다.

## 필터링은 허용할 외부 출발지를 정한다

<!-- learn-page-id: advanced-nat-mapping-filtering-page-04 -->

필터링은 NAT의 외부 주소·포트로 들어온 패킷을 어느 원격 출발지에서 받게 할지 정한다. 세 가지 대표 동작을 같은 예로 비교해 보자. 내부 `192.168.0.10:3000`이 `15.15.15.15:5555`에 먼저 UDP 패킷을 보냈고, 나중에 외부 주소 `203.0.113.8:42000`에 패킷이 도착했다고 가정한다.

| 필터링 동작 | 들어오는 패킷의 허용 기준 | 예: `15.15.15.15:7777`에서 도착 |
|---|---|---|
| Endpoint-Independent Filtering (EIF) | 원격 IP·포트와 관계없이 매핑으로 향하는 패킷 허용 | 허용할 수 있음 |
| Address-Dependent Filtering (ADF) | 이전에 통신한 원격 IP가 같으면 허용, 포트는 달라도 됨 | 허용할 수 있음 |
| Address-and-Port-Dependent Filtering (APDF) | 이전에 통신한 원격 IP와 포트가 모두 같아야 허용 | 허용되지 않을 수 있음 |

이 표에서 중요한 비교는 마지막 두 줄이다. 두 패킷은 모두 `15.15.15.15`에서 왔지만 출발지 포트가 다르다. ADF는 IP 주소만 비교하므로 허용할 수 있지만, APDF는 포트까지 확인하므로 통과시키지 않을 수 있다. `9.9.9.9:40000`처럼 다른 IP에서 온 패킷은 ADF와 APDF 모두 이전 조건과 맞지 않는다.

이들은 NAT의 수신 허용 동작을 설명하는 기준이지, 전체 방화벽 정책이나 앱의 로그인 여부를 설명하는 것은 아니다. 또한 필터링 기준과 매핑 기준은 독립적으로 조합될 수 있다. 특정 장비가 실제로 어떤 동작을 하는지는 표준 이름 하나만 보고 추측하지 말고 구현과 설정을 확인해야 한다.

**기억할 점:** 필터링 조건은 원격 출발지를 얼마나 자세히 비교하는가에 따라 “누구든지”, “같은 IP”, “같은 IP와 포트”로 좁아진다.

## 전통적인 Cone 이름은 두 기준을 묶어 부른다

<!-- learn-page-id: advanced-nat-mapping-filtering-page-05 -->

예전 자료에서 자주 보이는 Full Cone, Restricted Cone, Port Restricted Cone, Symmetric NAT는 매핑과 필터링의 동작을 함께 묶어 설명한 분류다. 이 이름은 NAT의 모든 구현을 빠짐없이 구별하는 현재의 공통 표준 분류로 외우기보다, 오래된 설명에서 어떤 기준을 뜻했는지 읽는 데 사용한다. 요즘 동작을 비교할 때는 앞 페이지처럼 매핑과 필터링을 나누어 말하는 편이 정확하다.

| 전통적인 이름 | 전통적 설명에서의 매핑 | 전통적 설명에서의 필터링 |
|---|---|---|
| Full Cone | 보통 목적지 독립적으로 설명 | 매핑된 외부 주소·포트로 들어오는 모든 원격 출발지를 허용 |
| Restricted Cone | 보통 목적지 독립적으로 설명 | 이전에 통신한 원격 IP 주소를 확인 |
| Port Restricted Cone | 보통 목적지 독립적으로 설명 | 이전에 통신한 원격 IP와 포트를 함께 확인 |
| Symmetric NAT | 목적지 endpoint에 따라 매핑이 달라질 수 있음 | 보통 목적지 endpoint와 연관된 허용 조건으로 설명 |

Cone 세 이름은 매핑이 어떻게 만들어지는지보다 외부 패킷을 누구에게서 받을지 차례로 제한하는 모습을 강조한다. 반면 옛 Symmetric NAT 설명은 매핑이 외부 목적지에 따라 달라질 수 있다는 점도 함께 강조한다. 따라서 “Symmetric은 필터링이 가장 강한 한 종류”라고 외우면 매핑 차이를 놓치게 된다.

이 표는 용어를 읽기 위한 전통적 요약이며 모든 공유기의 실제 동작을 보장하지 않는다. 특히 Symmetric이라는 단어가 어떤 문서에서 쓰였는지 확인하고, 그 문서가 매핑을 말하는지 필터링을 말하는지 따로 읽는다.

**기억할 점:** Cone 이름은 옛 분류로 이해하고, 실제 동작은 매핑 기준과 필터링 기준을 따로 확인한다.

## UDP 홀 펀칭으로 직접 연결을 시도한다

<!-- learn-page-id: advanced-nat-mapping-filtering-page-06 -->

게임이나 음성·영상 앱은 중앙 서버가 두 피어를 소개하되, 이후 데이터는 직접 주고받고 싶을 수 있다. 이때 소개 서버(signaling 또는 rendezvous server)가 양쪽 피어가 서로를 찾도록 연결 정보를 전달한다. STUN 서버는 각 피어가 NAT 바깥에서 어떤 IP·포트로 관찰되는지 알아내는 데 도움을 준다. 소개 서버와 STUN 서버는 역할이 겹칠 수 있지만, 이름만으로 같은 기능이라고 단정하지 않는다.

간단한 UDP 홀 펀칭 흐름은 다음과 같다.

1. 피어 A와 B가 각각 소개·주소 확인 서버에 UDP 패킷을 보낸다.
2. 서버는 각 피어의 바깥에서 보이는 주소·포트를 관찰해 상대에게 알려 준다.
3. A와 B는 서로의 바깥 주소·포트로 UDP 패킷을 보낸다. 이 바깥 방향 패킷이 각 NAT에 매핑을 만든다.
4. 각 NAT의 필터링 조건이 상대 패킷을 허용하면, 두 피어가 직접 데이터를 주고받을 수 있다.

“구멍을 뚫는다”는 표현은 장비에 영구 구멍을 내거나 모든 보안 규칙을 끄는 뜻이 아니다. 양쪽이 보낸 패킷으로 생긴 매핑과 필터링 상태를 이용해 응답 경로를 열 수 있는지 시도하는 비유다. 외부 주소를 얻었다고 해서 연결이 반드시 성공하는 것은 아니다.

**기억할 점:** 홀 펀칭은 두 피어의 바깥 주소를 알려 주고 양쪽에서 먼저 패킷을 보내 직접 경로를 시도한다.

## 직접 연결이 안 되면 중계 경로를 쓴다

<!-- learn-page-id: advanced-nat-mapping-filtering-page-07 -->

홀 펀칭은 NAT의 매핑 동작과 필터링 조건, 양쪽 네트워크의 정책에 따라 실패할 수 있다. 예를 들어 목적지에 따라 매핑이 달라지는 NAT에서는 소개 서버에서 관찰한 바깥 주소를 피어 통신에도 재사용하지 못할 수 있다. 회사·학교 방화벽이 직접 UDP 통신을 막거나 NAT가 여러 겹인 경우도 연결을 어렵게 한다. 그러므로 “Full Cone이면 항상 연결되고 Symmetric이면 절대 연결되지 않는다”처럼 단정하지 않는다.

직접 경로를 만들 수 없으면 TURN 같은 중계 서버가 데이터를 대신 전달할 수 있다. 이때 두 피어의 데이터가 중계 서버를 지나므로 서버의 네트워크 사용량과 운영 비용이 늘지만, 직접 경로가 막힌 환경에서도 통신을 이어갈 가능성이 생긴다. STUN은 바깥에서 보이는 주소를 알아내는 데 도움을 주고, TURN은 실제 데이터를 릴레이한다는 역할 차이를 기억한다.

Lesson 4에서 배울 포트 포워딩은 관리자가 외부 포트를 내부 서비스로 연결하는 규칙을 직접 등록하는 방식이다. 홀 펀칭은 앱이 패킷을 먼저 보내 동적 매핑을 이용해 피어 간 경로를 시도한다. 둘 다 외부에서 내부로 이어지는 길과 관련 있지만, 설정 주체와 동작 방식이 다르다.

| 연결 방법 | 누가 설정을 시작하나? | 핵심 역할 |
|---|---|---|
| 홀 펀칭 | 통신하는 앱과 피어 | NAT 매핑·필터링 상태를 이용해 직접 경로를 시도 |
| 포트 포워딩 | 공유기 관리자 | 정해 둔 외부 포트를 내부 주소·포트로 전달 |
| TURN 중계 | 앱과 중계 서버 | 직접 연결이 어려울 때 중계 서버가 데이터를 전달 |

**기억할 점:** 매핑은 바깥 주소를 정하고, 필터링은 받을 상대를 정한다. 두 피어의 조건이 맞으면 직접 연결을 시도하고, 실패하면 TURN 같은 중계를 사용할 수 있다.
