---
id: advanced-vpn-ipsec-agreement
title: '터널을 열기 전 두 장비의 약속: IPsec'
source_lesson_ids:
- u10-advanced-20-ipsec-vpn과-터널링-개념
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-20.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p196-b15
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/03-2.md#p158-b01
- https://datatracker.ietf.org/doc/html/rfc4301
- https://datatracker.ietf.org/doc/html/rfc4302
- https://datatracker.ietf.org/doc/html/rfc4303
- https://datatracker.ietf.org/doc/html/rfc7296
- https://datatracker.ietf.org/doc/html/rfc3948
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-20.md
page_metadata:
- page_id: advanced-source-20-page-01
  questions:
  - id: u14-l03-p01-q01
    kind: choice
    difficulty: easy
    prompt: IPsec이 동작하는 계층으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 물리 계층(L1)
      feedback: L1은 신호와 케이블의 계층이다. IPsec은 IP 패킷을 다루는 L3다.
    - id: b
      text: 애플리케이션 계층(L7)
      feedback: 웹 같은 응용 프로그램 수준이 아니라 IP 계층에서 동작한다.
    - id: c
      text: 전송 계층의 TCP 포트 수준(L4)
      feedback: IPsec은 TCP 포트에 의존하지 않고 IP 패킷 전체를 보호한다.
    - id: d
      text: IP 계층(L3)
      feedback: 맞다. IPsec은 IP 패킷을 직접 보호하는 방식이라 IP 계층에서 동작한다.
    - id: e
      text: 데이터 링크 계층(L2)
      feedback: L2 터널은 따로 있다. IPsec은 L3다.
    answer: d
    feedback: IPsec은 IP 계층(L3)에서 동작한다. 그래서 IPv4와 IPv6 모두에서 쓸 수 있다.
  - id: u14-l03-p01-q02
    kind: choice
    difficulty: medium
    prompt: 도쿄 SG와 본사 SG 사이에 IPsec 터널을 한 번 만들었더니, 쇼룸에서 파일 공유, 사내 AI 웹, 화상 회의 앱을 모두 별도 설정 없이 쓴다. 이유로 알맞은 것은 무엇일까요?
    choices:
    - id: a
      text: IPsec이 앱마다 필요한 포트를 자동으로 찾아 열어 주기 때문이다
      feedback: IPsec은 포트를 열어 주는 방식이 아니라 IP 패킷을 보호하는 방식이다.
    - id: b
      text: 앱이 각자 자기 암호화를 하고 터널은 겉모양만 만들기 때문이다
      feedback: 터널이 패킷을 보호하므로 앱이 따로 암호화하지 않아도 된다.
    - id: c
      text: IPsec이 웹 브라우저 안에서 동작해 웹 기반 앱만 통과시키기 때문이다
      feedback: 그것은 SSL VPN 이야기에 가깝다. IPsec은 IP 계층이다.
    - id: d
      text: IPsec이 응용 계층에서 앱 내용을 읽어 종류별로 나눠 보내기 때문이다
      feedback: IPsec은 앱 내용을 읽지 않고 IP 패킷 단위로 보호한다.
    - id: e
      text: IPsec이 IP 계층에서 패킷을 통째로 보호해 앱 종류와 관계없기 때문이다
      feedback: 맞다. 계층의 성격을 알면 앱이 바뀌어도 같은 구조로 읽을 수 있다.
    answer: e
    feedback: IPsec은 IP 패킷을 통째로 보호하므로 그 위의 앱 종류와 관계없이 같은 터널을 지난다. 같은 구조를 알아보는 🔁 같은 모양 찾기다.
  question_placements:
  - question_id: u14-l03-p01-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/u14-l03-p1-four-pieces.svg
    title: "IPsec의 네 조각"
    alt: "터널이 안 설 때 IKE 협상(UDP 500), NAT-T(UDP 4500), 협상 내용, 상대 확인 순서로 앞에서부터 확인한다는 점검 순서입니다."
    caption: "터널이 안 서면 IKE, NAT-T, 협상 내용, 상대 확인 순으로 확인합니다."
    after_paragraph: 3
- page_id: advanced-source-20-page-04
  questions:
  - id: u14-l03-p02-q01
    kind: choice
    difficulty: easy
    prompt: IPsec에서 두 SG가 IKE 협상을 마치고 저장해 두는 합의 결과를 무엇이라고 하나요?
    choices:
    - id: a
      text: NAT 테이블
      feedback: NAT 테이블은 주소 변환 기록이다. IKE 합의 결과가 아니다.
    - id: b
      text: MAC 주소 표
      feedback: MAC 주소 표는 스위치가 쓰는 표다.
    - id: c
      text: SA(보안 연관)
      feedback: 맞다. 알고리즘, 키, 수명 같은 합의 내용을 SA라고 하며, 보호는 방향마다 따로 있다.
    - id: d
      text: DNS 캐시
      feedback: DNS 캐시는 이름 해석 결과다.
    - id: e
      text: ARP 요청
      feedback: ARP는 같은 LAN에서 MAC 주소를 묻는 절차다.
    answer: c
    feedback: IKE의 합의 결과가 SA다. 알고리즘·키·수명을 담고, 방향마다 따로 생긴다.
  - id: u14-l03-p02-q02
    kind: choice
    difficulty: medium
    prompt: 본사 SG는 강한 암호 방식만 허용하도록, 새로 바꾼 도쿄 SG는 구형 암호 방식만 쓰도록 설정되어 있다. 터널이 올라오지 않을 때 어느 단계의 문제로 보아야 할까요?
    choices:
    - id: a
      text: 터널이 선 뒤 본사 방화벽·서버 정책에서 막히는 문제
      feedback: 터널이 아직 서지 않았다. 협상 단계가 먼저다.
    - id: b
      text: IKE 협상에서 공통 암호 조건을 찾지 못한 문제
      feedback: 맞다. 공통 조건이 없으면 협상이 실패한다. 어디서 막혔는지 단계로 나눠 보는 🧩 쪼개기다.
    - id: c
      text: AI 서버가 모델을 불러오는 동안 응답하지 못하는 문제
      feedback: 서버 문제가 아니라 두 SG의 협상 문제다.
    - id: d
      text: 쇼룸 PC의 DNS 설정이 달라 본사 이름을 못 찾는 문제
      feedback: DNS와 무관하다.
    - id: e
      text: 큰 패킷이 MTU를 넘어 터널 안에서 버려지는 문제
      feedback: MTU는 터널이 선 뒤의 큰 패킷 문제다.
    answer: b
    feedback: IPsec 문제를 협상, 상대 확인, 보호 방식, 운반으로 쪼개 보면 '공통 조건 없음'은 협상 단계다. 🧩 쪼개기다.
  question_placements:
  - question_id: u14-l03-p02-q01
    after_paragraph: 3
  illustrations:
  - file: assets/animations/u14-l03-p2-ike-sa.svg
    title: "IKE 협상과 SA"
    alt: "도쿄 SG와 서울 SG가 UDP 500으로 암호 방식·키·수명을 제안해 합의하고, 결과를 각자 SA로 기억하는 모습입니다."
    caption: "IKE는 공통 조건을 협상해 SA로 남기며, 공통 조건이 없으면 실패합니다."
    after_paragraph: 2
- page_id: u14-l03-page-03
  questions:
  - id: u14-l03-p03-q01
    kind: choice
    difficulty: easy
    prompt: 사전 공유 키(PSK)를 가장 알맞게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 양쪽 장비에 미리 같은 비밀값을 넣어 두고 서로 확인한다
      feedback: 맞다. 비밀값을 아는 장비끼리만 서로를 믿는다. 간단하지만 비밀값이 새면 위험하다.
    - id: b
      text: 인증 기관이 발급한 증명서를 양쪽 장비가 서로 보여 주는 방식
      feedback: 그것은 인증서 방식이다.
    - id: c
      text: 접속할 때마다 새로 만들어 한 번만 쓰는 일회용 비밀번호를 입력하는 방식
      feedback: PSK는 미리 정해 둔 고정 비밀값이다.
    - id: d
      text: 방화벽에 등록된 상대 주소에서 온 패킷만 통과시키는 방식
      feedback: 그것은 주소 허용 규칙이고 인증이 아니다.
    - id: e
      text: 통신사가 두 장비를 대신 확인해 주고 결과만 전달하는 방식
      feedback: 통신사가 상대를 확인해 주지 않는다. 양쪽 장비가 직접 확인한다.
    answer: a
    feedback: PSK는 미리 나눠 가진 같은 비밀값으로 서로를 확인한다. 편하지만 새면 위험하다.
  - id: u14-l03-p03-q02
    kind: choice
    difficulty: medium
    prompt: 지사 SG 설치를 맡았던 외주 업체와 계약이 끝났다. 그 업체는 설치 때 쓴 사전 공유 키를 알고 있다. 지우가 해야 할 일로 가장 알맞은 것은 무엇일까요?
    choices:
    - id: a
      text: SG를 재부팅하면 키가 새로 만들어지므로 재부팅만 한다
      feedback: 재부팅해도 설정된 키는 그대로다.
    - id: b
      text: SG 관리자 비밀번호를 바꾸면 터널 키도 함께 바뀌므로 그것만 바꾼다
      feedback: 관리자 비밀번호와 터널의 사전 공유 키는 다른 값이다.
    - id: c
      text: 계약 때 비밀유지 서약을 받았으므로 키는 그대로 둔다
      feedback: 키를 아는 사람이 남아 있어 위험하다.
    - id: d
      text: 사전 공유 키 대신 터널 암호화를 끄고 접속 주소만 허용하도록 바꾼다
      feedback: 암호화를 끄면 오히려 더 위험하다.
    - id: e
      text: 양쪽 SG의 사전 공유 키를 새로 정해 바꾸고 이전 키를 폐기한다
      feedback: 맞다. 키를 아는 사람이 있는 한 위험하다. 교체의 번거로움을 치르고 위험을 줄이는 ⚖️ 대가 따지기다.
    answer: e
    feedback: 키 교체의 번거로움과 유출 위험을 견주면 교체가 낫다. 대가를 따지는 ⚖️ 대가 따지기다.
  question_placements:
  - question_id: u14-l03-p03-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/u14-l03-p3-auth.svg
    title: "상대가 진짜 본사 SG일까"
    alt: "왼쪽은 양쪽이 같은 비밀값을 아는지로 믿는 사전 공유 키, 오른쪽은 인증 기관이 보증한 인증서를 서로 보여 주는 방식입니다."
    caption: "상대 확인은 사전 공유 키나 인증서로 하며, 암호화와는 다른 일입니다."
    after_paragraph: 1
- page_id: advanced-source-20-page-05
  questions:
  - id: u14-l03-p04-q01
    kind: choice
    difficulty: easy
    prompt: 내용을 암호화해서 기밀성을 제공하는 IPsec 방식은 무엇인가요?
    choices:
    - id: a
      text: AH
      feedback: AH는 무결성·인증을 주지만 내용을 암호화하지 않는다.
    - id: b
      text: ESP
      feedback: 맞다. ESP는 암호화로 기밀성을 주고, 무결성과 인증도 함께 켤 수 있다.
    - id: c
      text: IKE
      feedback: IKE는 협상과 키 교환을 맡는 프로토콜이다.
    - id: d
      text: SA
      feedback: SA는 협상 결과를 담은 기록이다.
    - id: e
      text: MTU
      feedback: MTU는 한 번에 보내는 패킷의 최대 크기다.
    answer: b
    feedback: 기밀성은 ESP가 준다. AH는 변조·출처 확인만 한다.
  - id: u14-l03-p04-q02
    kind: choice
    difficulty: medium
    prompt: 누군가 '변조만 막으면 되니까' 하고 AH만 켜서 고객 개인정보가 든 견적 데이터를 지사로 보내고 있다. 무엇이 문제일까요?
    choices:
    - id: a
      text: AH는 변조 확인도 못 해서 내용이 바뀌어도 알아채지 못한다
      feedback: AH는 무결성과 인증을 제공한다.
    - id: b
      text: AH는 IPv4에서만 동작해 IPv6 구간에서는 보호가 빠진다
      feedback: IPv6에서도 쓸 수 있다. 이 문제의 핵심이 아니다.
    - id: c
      text: AH는 키 교환이 없어서 상대 확인이 되지 않는다
      feedback: AH도 키가 필요하다. 핵심은 암호화가 없다는 점이다.
    - id: d
      text: 내용이 암호화되지 않아 중간에서 읽힐 수 있다
      feedback: 맞다. AH는 변조는 확인하지만 내용을 가리지 않는다. 필요한 보호를 먼저 정하는 🧩 쪼개기가 필요하다.
    - id: e
      text: AH만 켜면 개인정보 항목만 골라 자동으로 암호화해 준다
      feedback: AH는 암호화를 제공하지 않는다.
    answer: d
    feedback: 필요한 보호를 기밀성, 무결성, 인증으로 나눠 보면 AH에 기밀성이 없다는 점이 보인다. 🧩 쪼개기다.
  question_placements:
  - question_id: u14-l03-p04-q01
    after_paragraph: 3
  illustrations:
  - file: assets/animations/u14-l03-p4-esp-ah.svg
    title: "ESP와 AH는 뭘 지켜 줄까"
    alt: "기밀성, 무결성, 인증 세 가지 중 ESP는 모두, AH는 기밀성을 뺀 둘만 지켜 준다는 표 형태의 비교입니다."
    caption: "내용이 비밀인 자료는 기밀성이 있는 ESP로 맞춥니다."
    after_paragraph: 2
- page_id: u14-l03-page-05
  questions:
  - id: u14-l03-p05-q01
    kind: choice
    difficulty: easy
    prompt: NAT 뒤에서 IPsec의 ESP를 UDP 4500번 포트에 한 번 더 담아 보내는 방법을 무엇이라고 하나요?
    choices:
    - id: a
      text: 포트 포워딩
      feedback: 포트 포워딩은 외부 포트의 연결을 내부 주소로 전달하는 규칙이다.
    - id: b
      text: IKE 재협상
      feedback: IKE 재협상은 수명이 끝난 키를 새로 정하는 일이다.
    - id: c
      text: NAT-T
      feedback: 맞다. UDP 4500으로 포장해 NAT가 연결을 구분하고 통과시킬 수 있게 한다.
    - id: d
      text: MTU 조정
      feedback: MTU 조정은 패킷 크기를 맞추는 일이다.
    - id: e
      text: SA 삭제
      feedback: SA를 지우면 터널이 끊긴다.
    answer: c
    feedback: NAT-T는 NAT를 건너기 위해 ESP를 UDP 4500에 한 번 더 담는 방법이다.
  - id: u14-l03-p05-q02
    kind: choice
    difficulty: medium
    prompt: 박 팀장이 집 공유기(NAT) 뒤에서 IPsec 방식 VPN을 켰다. 화면이 '연결 중'에서 멈췄다가 시간 초과가 나고, 비밀번호가 틀렸다는 안내는 없다. 집 공유기는 UDP 500만 허용하고 다른 UDP는 막는 설정이다. 가장 먼저 의심할 곳은 어디일까요?
    choices:
    - id: a
      text: NAT-T가 쓰는 UDP 4500이 막혀 협상이 인증을 마치기 전에 멈췄는지
      feedback: 맞다. NAT를 감지하면 협상이 UDP 4500으로 옮겨 가는데 공유기가 4500을 막아, 인증을 마치기 전에 멈춘 것이다. 📋 순서대로 확인하기다.
    - id: b
      text: VPN 계정 비밀번호가 틀려 인증이 거절되었는지
      feedback: 비밀번호가 틀렸다면 거절 안내가 나온다. 이 증상은 응답이 멈춘 것이다.
    - id: c
      text: 본사 방화벽이 VPN 주소 풀을 AI 서버로 허용하지 않는지
      feedback: 그것은 터널이 선 뒤의 문제다. 지금은 터널이 서지 않았다.
    - id: d
      text: SA 수명이 길게 설정되어 재협상이 늦어지는지
      feedback: 수명은 이미 선 터널의 키 교체 주기다. 처음 연결이 멈춘 원인이 아니다.
    - id: e
      text: 노트북 MTU가 커서 큰 패킷만 버려지는지
      feedback: MTU 문제는 터널이 선 뒤 큰 패킷에서 나타난다.
    answer: a
    feedback: NAT를 감지하면 협상이 UDP 4500으로 옮겨 가므로, 4500이 막히면 인증을 마치기 전에 멈춘다. 협상 단계부터 순서대로 보는 📋 순서대로 확인하기다.
  question_placements:
  - question_id: u14-l03-p05-q01
    after_paragraph: 3
  illustrations:
  - file: assets/animations/u14-l03-p5-nat-t.svg
    title: "집 공유기를 만나도 지나갈까"
    alt: "박 팀장 노트북의 ESP 패킷이 포트 번호가 없어 집 공유기(NAT)에서 막히지만, NAT-T가 UDP 4500으로 한 번 더 감싸 서울 SG까지 지나가는 모습입니다."
    caption: "NAT가 있으면 ESP를 UDP 4500으로 감싸는 NAT-T를 씁니다."
    after_paragraph: 2
- page_id: u14-l03-page-06
  questions:
  - id: u14-l03-p06-q01
    kind: choice
    difficulty: easy
    prompt: SSL/TLS VPN이 호텔 와이파이처럼 제한된 환경에서도 비교적 잘 통과하는 이유로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: UDP 500과 4500을 숨겨서 방화벽이 포트를 볼 수 없게 하기 때문이다
      feedback: 포트를 숨겨 우회한다는 뜻이 아니라 웹이 쓰는 통로를 쓰는 것이다.
    - id: b
      text: IP 헤더를 한 번 더 씌워서 NAT가 주소를 바꾸지 못하게 하기 때문이다
      feedback: 그런 방식이 아니다. TLS 위에서 동작한다.
    - id: c
      text: 웹(HTTPS)과 같은 TLS·443 통로를 쓰기 때문이다
      feedback: 맞다. 웹이 열린 환경이면 같은 통로로 통과하기 쉽다.
    - id: d
      text: 암호화를 생략해 처리가 가벼워 제한 장비가 검사하지 않기 때문이다
      feedback: SSL/TLS VPN도 암호화한다.
    - id: e
      text: 호텔 와이파이가 보안을 위해 VPN 트래픽만 따로 열어 두기 때문이다
      feedback: 호텔은 오히려 웹 외의 포트를 막는 경우가 많다.
    answer: c
    feedback: SSL/TLS VPN은 웹(HTTPS)과 같은 TLS·443 통로를 써서 제한된 환경을 통과하기 쉽다.
  - id: u14-l03-p06-q02
    kind: choice
    difficulty: medium
    prompt: 외주 3D 렌더링 작업자에게 사내 도면 열람 웹 한 곳만 2주간 열어 주어야 한다. 대가가 가장 작은 방식은 무엇일까요?
    choices:
    - id: a
      text: 그 웹 앱만 열어 주는 SSL VPN 포털을 쓴다
      feedback: 맞다. 접근 범위를 앱 하나로 좁힐 수 있어 노출이 작다. 범위와 부담을 견주는 ⚖️ 대가 따지기다.
    - id: b
      text: 지사급 IPsec 사이트 간 터널을 새로 만든다
      feedback: 망 전체를 잇는 방식은 2주짜리 외주에 과하다.
    - id: c
      text: 방화벽에서 도면 서버 포트를 인터넷에 연다
      feedback: 서버를 인터넷에 여는 것은 위험이 크다.
    - id: d
      text: 외주 업체에 본사 LAN 전체를 열어 준다
      feedback: 필요한 것은 웹 하나다. 범위가 너무 넓다.
    - id: e
      text: 외주 작업자 PC에 사내 관리자 계정을 준다
      feedback: 권한이 너무 크다.
    answer: a
    feedback: 필요한 범위만 열어 주는 방식을 고르면 대가가 작다. 비용과 노출을 견주는 ⚖️ 대가 따지기다.
  question_placements:
  - question_id: u14-l03-p06-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/u14-l03-p6-ssl-vpn.svg
    title: "브라우저로 붙는 SSL VPN"
    alt: "호텔 와이파이에서 IPsec의 UDP 500·4500은 막히고 TLS 기반 SSL VPN은 TCP 443으로 본사 SG까지 지나가는 모습입니다."
    caption: "웹만 열린 환경에서는 TCP 443을 쓰는 SSL VPN이 대개 통과합니다."
    after_paragraph: 1
---

## VPN 만드는 방법은 하나뿐일까?

<!-- learn-page-id: advanced-source-20-page-01 -->

도쿄 쇼룸 SG를 교체하는 날, 지우가 새 장비 설정 화면을 열었다. IKE, SA, ESP, NAT-T 같은 낯선 단어가 가득하다. 앞 Lesson에서 "두 SG가 이미 약속을 마쳤다"고 넘어갔던 그 약속이 바로 이 화면 안에 있다. 이 Lesson은 그 약속을 하나씩 풀어 본다.

VPN을 만드는 방법은 여러 가지다. 도로를 잇는 방법에 다리와 터널이 있는 것과 같다. 이 과정의 대표 예는 **IPsec**이다. IPsec은 IP 계층(L3)에서 패킷을 통째로 보호한다. 그래서 그 위에서 파일 공유를 쓰든 사내 AI 웹을 쓰든 같은 터널을 지나고, 앱마다 따로 설정할 필요가 없다. 지사끼리 망 전체를 잇는 데 흔하게 쓰인다.

이 Lesson은 IPsec을 네 조각으로 쪼개 본다. 터널이 안 뜰 때 읽는 눈이 빨라지도록, 막혔을 때 앞에서부터 확인하는 순서와 증상을 먼저 표로 잡아 두자. 지금은 모르는 단어가 많아도 괜찮다. 뒤의 Page들이 한 줄씩 풀어 준다.

| 확인 순서 | 조각 | 막히면 보이는 증상 | 의심할 곳 |
| --- | --- | --- | --- |
| 1 | 협상 시작(IKE) | '협상 실패'에서 시작도 못 한다 | 두 SG 사이 UDP 500 |
| 2 | NAT 통과(NAT-T) | 공유기 뒤에서 '연결 중'만 반복한다 | NAT-T 설정, UDP 4500 |
| 3 | 협상 내용(암호 방식·수명·ESP 또는 AH) | 협상 실패 메시지가 뜬다 | 양쪽 제안에 공통 조건이 있는가 |
| 4 | 상대 확인 | 인증 실패 메시지가 뜬다 | 사전 공유 키·인증서가 같은가 |

공유기(NAT)가 중간에 있으면 2번이 3·4번보다 먼저 막힌다. 협상이 UDP 4500으로 옮겨 가기 때문이다. 마지막에는 브라우저 기반으로 동작하는 SSL VPN과 비교한다.

## 처음 만난 두 장비는 뭘부터 정할까?

<!-- learn-page-id: advanced-source-20-page-04 -->

도쿄 쇼룸 SG를 새 장비로 바꿨더니 터널이 '협상 실패'에서 멈춘다. 두 장비가 서로 연결되어 있다는 것은 확인했다. 처음 만난 두 사람이 계약서를 쓰려면 사용할 언어, 서명 방식, 유효 기간부터 맞춰야 하는 것과 비슷한 일이 막혔을 가능성이 크다.

IPsec에서 이 일을 맡는 것이 **IKE(Internet Key Exchange)**다. IKE는 두 SG가 쓸 암호 알고리즘과 키, 보호 방식(ESP 또는 AH), 그리고 키를 얼마 뒤에 바꿀지(수명)를 합의한다. 협상은 보통 UDP 500번 포트로 시작하므로, 두 SG 사이 방화벽에서 UDP 500이 막혀 있어도 협상이 실패한다. 상대가 맞는지 확인하는 단계도 이 협상 안에서 이뤄진다.

합의가 끝나면 그 결과를 **SA(Security Association, 보안 연관)**라는 '합의 결과 메모'로 각자 기억해 둔다. "이 방향의 트래픽은 이 알고리즘과 이 키로 보호한다"는 기록이다. 데이터를 보호하는 SA는 방향마다 따로 생겨서, 도쿄에서 서울로 가는 것과 서울에서 도쿄로 오는 것이 각각 있다.

SA에는 수명이 있다. 같은 키를 너무 오래 쓰면 해독 위험이 커지므로, 수명이 끝나면 다시 협상해 새 키로 바꾼다. 대가는 재협상하는 순간의 부하와, 두 장비의 수명 설정을 맞춰 관리해야 하는 번거로움이다.

그래서 '협상 실패'를 만나면 지우는 두 SG의 제안이 서로 맞는지부터 대조한다. 한쪽이 허용하는 암호 방식을 다른 쪽이 허용하지 않거나, 수명이 어긋나거나, UDP 500이 막혀 있는 경우가 흔하다. 협상은 "공통으로 허용하는 조건을 하나 찾는 일"이라서, 공통 조건이 없으면 실패한다.

## 상대가 진짜 우리 본사 SG일까?

<!-- learn-page-id: u14-l03-page-03 -->

서 이사가 이렇게 묻는다. "그런데 누가 본사 SG인 척하면 어쩌죠?" 날카로운 질문이다. 암호화한 터널이라도 끝에 있는 상대가 가짜라면 소용이 없다. 가짜 가게에 계약서를 안전하게 전달하는 셈이기 때문이다. IKE 협상에는 이 문제를 막는 **상대 확인(인증)**이 들어 있다.

방법은 두 가지다. 첫째는 **사전 공유 키(PSK)**다. 양쪽 장비에 미리 같은 비밀값을 넣어 두고, 서로 그 값을 아는지로 상대를 믿는다. 두 사람이 미리 정한 암구호와 같다. 둘째는 **인증서**다. 신뢰할 수 있는 인증 기관(CA)이 "이 장비는 한결디자인 본사 SG가 맞다"고 보증한 증명서를 서로 보여 준다. 신분증과 같은 방식이다.

| 방식 | 장점 | 대가 |
| --- | --- | --- |
| 사전 공유 키(PSK) | 설정이 간단하다 | 새면 해당 터널이 위험하고, 바꾸려면 양쪽을 맞춰야 한다 |
| 인증서 | 장비마다 신원을 확인할 수 있어 관리 규모가 커질수록 유리하다 | 발급과 갱신, 폐기 관리가 필요하다 |

PSK는 지사가 한두 곳일 때 간단하지만, 비밀값이 한 번 새면 같은 값을 쓰는 모든 터널을 바꿔야 한다. 지사가 많아질수록 부담이 커진다. 인증서는 처음 준비가 번거롭지만 장비별로 취소할 수 있다. 어느 쪽이 낫다고 단정할 수 없고, 지사 수와 관리 인력을 보고 정한다.

어떤 방식이든 "상대 확인"과 "암호화"는 다른 일이다. 인증은 상대가 맞는지, 암호화는 내용을 가리는지의 문제다. 지우의 점검표에는 터널을 열기 전에 "상대를 어떻게 믿는가"가 한 줄 들어간다.

## ESP와 AH는 뭘 지켜 줄까?

<!-- learn-page-id: advanced-source-20-page-05 -->

SG 설정 화면에서 보호 방식을 고르라고 한다. 선택지는 ESP와 AH 두 가지다. 지우는 앞에서 정리한 세 가지 보호, 즉 기밀성, 무결성, 인증을 떠올리며 각각이 어디에 해당하는지 확인한다.

**ESP(Encapsulating Security Payload)**는 암호화로 기밀성을 주고, 무결성과 인증도 함께 켤 수 있다. 불투명한 봉투에 밀봉까지 한 셈이다. 실무의 지사 VPN은 거의 ESP를 쓴다.

**AH(Authentication Header)**는 무결성과 출처 인증만 주고 내용은 암호화하지 않는다. 투명한 봉투에 밀봉 스티커만 붙인 것과 같아서, 열면 티가 나지만 안은 보인다. 게다가 IP 헤더까지 검증해서 NAT를 만나면 쓸 수 없다(다음 Page).

이 선택도 앞 Page의 협상에 들어 있다. 한쪽 SG는 ESP만, 다른 쪽은 AH만 허용하도록 설정했다면 공통 조건이 없어 협상이 실패한다. 그래서 고객 도면과 견적서처럼 내용이 비밀인 자료는 양쪽 모두 ESP로 맞춘다. "변조만 막으면 되겠지" 하고 AH만 켜면 내용이 그대로 읽힌다. 어떤 보호가 필요한지를 먼저 정하고 그에 맞는 방식을 고르는 순서다.

## 집 공유기를 만나도 터널은 지나갈 수 있을까?

<!-- learn-page-id: u14-l03-page-05 -->

박 팀장이 집에서 IPsec 방식 VPN을 켰다. 노트북은 집 공유기가 준 사설 주소 `192.168.0.20`을 쓰고, 인터넷에는 공유기의 공인 주소 `192.0.2.123`으로 나간다. 그런데 연결 화면이 '연결 중'에서 한참 멈췄다가 시간 초과가 난다. 두 장비 사이에 공유기, 곧 NAT가 끼면 무슨 일이 생길까?

NAT는 패킷을 통과시킬 때 IP 주소를 바꿔 쓴다(Unit 12). AH는 주소가 바뀌면 변조로 보고 버리므로 NAT 뒤에서는 ESP로 가야 한다. 그런데 ESP에는 TCP나 UDP 같은 포트 번호가 없다. NAT는 포트 번호로 여러 연결을 구분하는데, ESP에는 그 구분표가 없어서 안쪽에서 여러 장비가 나가면 어느 응답이 누구 것인지 가리지 못한다.

해결책이 **NAT-T(NAT Traversal, NAT 통과)**다. IKE가 협상 중에 중간의 NAT를 감지하면, ESP를 UDP 4500번 포트로 한 번 더 포장하고 협상도 500번에서 4500번으로 옮겨 간다. UDP는 포트가 있으니 NAT가 구분할 수 있다. NAT-T는 ESP를 감싸는 방법이라 AH를 구제하지는 않는다.

대가는 포장 한 겹만큼 패킷이 커지는 것과, 경로의 방화벽·공유기에서 UDP 500과 4500이 열려 있어야 한다는 점이다. 4500이 막히면 협상이 인증을 마치기 전에 멈춘다. 그래서 NAT가 있다면 이 Lesson 첫 Page 표의 2번을 1번 바로 다음에 확인한다.

## 브라우저로 붙는 SSL VPN은 뭐가 다를까?

<!-- learn-page-id: u14-l03-page-06 -->

서 이사가 출장지 호텔의 와이파이에서 IPsec VPN을 쓰지 못한다. 웹사이트는 잘 열린다. 호텔이나 카페의 공용 와이파이는 웹 말고는 대부분 막아 두는 경우가 있고, UDP 500이나 4500도 그 대상이 된다. 이런 환경에서도 잘 붙는 방식이 **SSL/TLS VPN**이다.

SSL/TLS VPN은 HTTPS와 같은 TLS 위에서 보통 443번 포트로 동작한다. 호텔이 웹을 허용하면 이 방식도 대개 통과한다. 건물 정문이 닫힌 날에도 직원용 출입문은 열려 있는 것과 비슷하다. 형태는 두 가지다. 브라우저의 웹 포털로 특정 앱만 열어 주는 방식과, 클라이언트를 설치해 사내망에 폭넓게 붙는 방식이다.

IPsec은 IP 계층에서 망 전체를 잇는 데 강하다. 지사끼리 연결하는 사이트 간 VPN에 흔한 이유다. 반면 SSL VPN은 사용자 한 명이 필요한 앱 몇 개에 붙는 경우에 어울린다. 클라이언트 설치 부담이 적고 앱별로 접근을 정할 수 있기 때문이다.

| 항목 | IPsec | SSL/TLS VPN |
| --- | --- | --- |
| 동작 계층 | IP 계층(L3) | TLS 위, 응용에 가깝다 |
| 주로 쓰는 포트 | UDP 500·4500 | TCP 443 |
| 주 용도 | 지사 간 연결, 망 전체 접속 | 재택·출장, 특정 앱 접속 |
| 설치 부담 | 장비·클라이언트 설정이 필요하다 | 웹 포털은 설치가 거의 없다 |
| 통제 범위 | 망 전체 | 앱별로 좁게 가능 |

그래서 지사는 IPsec, 재택·출장은 SSL VPN으로 나눠 함께 쓰는 구성도 흔하다. 어느 쪽이 항상 낫다는 정답은 없고, 연결 대상과 통로의 환경으로 고른다. 지우는 이 표를 장비 견적서 옆에 붙여 두기로 했다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** IPsec은 IKE로 알고리즘·키·수명을 협상해 SA를 만들고(UDP 500), 상대 확인은 사전 공유 키나 인증서로 한다. ESP는 암호화(+무결성), AH는 무결성·인증만 주고 NAT를 지나지 못한다. NAT 뒤에서는 ESP를 NAT-T(UDP 4500)로 감싼다.
- **적용하기 (Apply):** 터널이 안 서면 UDP 500 도달, NAT가 있으면 NAT-T·UDP 4500, 암호·수명·ESP 제안 일치, 상대 확인 순으로 확인하고, 호텔처럼 웹만 열린 환경에서는 TLS 기반 SSL VPN을 고려한다.
- **찾아보기 (Lookup):** SG나 VPN 장비 화면에서 IKE 암호 방식·SA 수명, 인증 방식(PSK/인증서), NAT-T 사용 여부가 어디에 있는지 찾아본다.

### 🧠 이번에 쓴 생각법

- 🧩 **쪼개기:** "터널이 안 뜬다"를 협상(IKE), 상대 확인, 보호 방식(ESP/AH), 운반(NAT-T)으로 나눠 어느 칸이 막혔는지 찾았다.
- ⚖️ **대가 따지기:** ESP 대 AH, PSK 대 인증서, IPsec 대 SSL VPN을 보호 범위와 관리·설치 부담으로 견주었다.
- 📋 **순서대로 확인하기:** 터널이 안 뜰 때 UDP 500 도달, NAT-T·UDP 4500, 협상 내용, 상대 확인 순서로 앞쪽부터 확인했다.
