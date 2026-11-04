---
id: u4-l21-ttl과-단편화
title: "TTL과 단편화: 패킷의 이동 횟수와 크기 제한"
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-21.md
additional_sources:
  - https://studio.futurereadycampus.com/course-network/wiki/oeweo-network/lesson-21.html
  - https://www.rfc-editor.org/rfc/rfc791.html
  - https://www.rfc-editor.org/rfc/rfc1122.html
  - https://www.rfc-editor.org/rfc/rfc792.html
wiki_diagram: units/04-layer3-addressing/lessons/11-ttl과-단편화/assets/diagrams/lesson-21.svg
page_metadata:
- terms:
  - 라우터(Router)
  - IP 패킷(IP packet)
  - 네트워크 경로(Network path)
  questions:
  - id: u6-l01-p01-q01
    kind: choice
    difficulty: easy
    prompt: 이 Lesson에서 다루는 두 가지 전달 한계는 무엇인가요?
    choices:
    - id: b
      text: 패킷 이동 범위와 링크별 크기
      feedback: TTL은 전달 범위를, MTU는 링크에서 보낼 패킷 크기를 다룹니다.
    - id: a
      text: 패킷의 색과 주소
      feedback: 본문의 두 질문이 이동 한계와 크기 한계 중 무엇을 설명하는지 떠올려 보세요.
    - id: c
      text: 서버 수와 사용자 수
      feedback: 본문의 두 질문이 이동 한계와 크기 한계 중 무엇을 설명하는지 떠올려 보세요.
    - id: d
      text: 무선 신호와 암호 길이
      feedback: 본문의 두 질문이 이동 한계와 크기 한계 중 무엇을 설명하는지 떠올려 보세요.
    - id: e
      text: 프로세스 수와 포트 수
      feedback: 본문의 두 질문이 이동 한계와 크기 한계 중 무엇을 설명하는지 떠올려 보세요.
    answer: b
  - id: u6-l01-p01-q02
    kind: choice
    difficulty: medium
    prompt: 패킷이 출발지에서 목적지로 가는 동안 여러 라우터를 거치는 이유는 무엇인가요?
    choices:
    - id: b
      text: 라우터가 패킷 내용을 최종 사용하기 때문
      feedback: 라우터는 패킷을 소비하는 종착지가 아니라 다음 전달 지점을 고르는 장비입니다.
    - id: c
      text: 각 라우터가 패킷을 모두 저장해 두기 때문
      feedback: 라우터는 패킷을 소비하는 종착지가 아니라 다음 전달 지점을 고르는 장비입니다.
    - id: a
      text: 각 라우터가 목적지 IP를 확인해 다음 전달 방향을 정하기 때문
      feedback: 라우터는 목적지 IP와 경로 정보를 참고해 패킷을 다음 장비로 전달합니다.
    - id: d
      text: 패킷이 라우터마다 새로운 목적지를 받기 때문
      feedback: 라우터는 패킷을 소비하는 종착지가 아니라 다음 전달 지점을 고르는 장비입니다.
    - id: e
      text: 라우터가 TCP 데이터를 다시 작성하기 때문
      feedback: 라우터는 패킷을 소비하는 종착지가 아니라 다음 전달 지점을 고르는 장비입니다.
    answer: a
  - id: u6-l01-p01-q03
    kind: choice
    difficulty: medium
    prompt: IP 단편화와 TCP 세그먼트 분할에 대한 설명으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 둘 다 같은 계층에서 같은 단위로 일어난다
      feedback: 두 작업이 각각 IP 패킷과 TCP 바이트 흐름 중 무엇을 다루는지 비교하세요.
    - id: c
      text: TCP 분할은 라우터만 수행한다
      feedback: 두 작업이 각각 IP 패킷과 TCP 바이트 흐름 중 무엇을 다루는지 비교하세요.
    - id: d
      text: IP 단편화는 패킷의 목적지 주소를 없앤다
      feedback: 두 작업이 각각 IP 패킷과 TCP 바이트 흐름 중 무엇을 다루는지 비교하세요.
    - id: e
      text: 둘 다 TTL 값을 나누는 작업이다
      feedback: 두 작업이 각각 IP 패킷과 TCP 바이트 흐름 중 무엇을 다루는지 비교하세요.
    - id: b
      text: IP 단편화는 IP 패킷을, TCP 분할은 TCP의 바이트 흐름을 다룬다
      feedback: IP 단편화와 TCP 데이터 분할은 계층과 다루는 단위가 다릅니다.
    answer: b
  question_placements:
  - question_id: u6-l01-p01-q01
    after_paragraph: 2
- terms:
  - 전달(Forwarding)
  - 홉(Hop)
  - 다음 홉(Next hop)
  animations:
  - file: l21-router-forwarding.svg
    title: 라우터는 패킷을 다음 장비로 전달한다
    alt: PC에서 출발한 IP 패킷이 라우터를 차례로 지나 서버에 도착합니다. 각 라우터는 목적지 주소를 확인해 다음 라우터로 넘깁니다.
    caption: 라우터는 패킷을 최종 소비하지 않고 목적지 IP를 보고 다음 홉으로 전달합니다.
    after_paragraph: 2
  questions:
  - id: u6-l01-p02-q01
    kind: choice
    difficulty: easy
    prompt: 라우터에서 다음 라우터로 한 번 넘어가는 이동을 무엇이라고 하나요?
    choices:
    - id: a
      text: 세션
      feedback: 경로 전체가 아니라 라우터 사이 한 번의 이동을 가리키는 용어를 찾으세요.
    - id: c
      text: 임대
      feedback: 경로 전체가 아니라 라우터 사이 한 번의 이동을 가리키는 용어를 찾으세요.
    - id: b
      text: 홉(Hop)
      feedback: 라우터에서 다음 라우터로 한 번 이동하는 것을 홉이라고 합니다.
    - id: d
      text: 단편
      feedback: 경로 전체가 아니라 라우터 사이 한 번의 이동을 가리키는 용어를 찾으세요.
    - id: e
      text: 포트
      feedback: 경로 전체가 아니라 라우터 사이 한 번의 이동을 가리키는 용어를 찾으세요.
    answer: b
  - id: u6-l01-p02-q02
    kind: choice
    difficulty: medium
    prompt: 라우터가 패킷을 다음 방향으로 넘길 때 주로 확인하는 정보는 무엇인가요?
    choices:
    - id: b
      text: 웹 페이지의 글꼴
      feedback: 본문의 라우터 동작 순서에서 목적지 주소와 함께 참고하는 표를 확인하세요.
    - id: c
      text: 클라이언트의 화면 크기
      feedback: 본문의 라우터 동작 순서에서 목적지 주소와 함께 참고하는 표를 확인하세요.
    - id: d
      text: 패킷 안의 파일 이름만
      feedback: 본문의 라우터 동작 순서에서 목적지 주소와 함께 참고하는 표를 확인하세요.
    - id: e
      text: Wi-Fi 비밀번호
      feedback: 본문의 라우터 동작 순서에서 목적지 주소와 함께 참고하는 표를 확인하세요.
    - id: a
      text: 목적지 IP 주소와 라우팅 테이블
      feedback: 라우터는 목적지 IP를 확인하고 라우팅 테이블을 참고해 전달 방향을 정합니다.
    answer: a
  - id: u6-l01-p02-q03
    kind: choice
    difficulty: medium
    prompt: 패킷의 최종 목적지가 라우터 자신이 아니라면 라우터는 보통 무엇을 하나요?
    choices:
    - id: a
      text: 패킷 내용을 사용자에게 보여 준다
      feedback: 중간 물류센터 비유에서 라우터가 상자를 어떻게 처리하는지 떠올려 보세요.
    - id: b
      text: 패킷을 다음 장비로 전달한다
      feedback: 라우터는 최종 목적지가 아니라면 패킷을 다음 장비로 전달합니다.
    - id: c
      text: 패킷을 영구 보관한다
      feedback: 중간 물류센터 비유에서 라우터가 상자를 어떻게 처리하는지 떠올려 보세요.
    - id: d
      text: 패킷의 IP 주소를 지운다
      feedback: 중간 물류센터 비유에서 라우터가 상자를 어떻게 처리하는지 떠올려 보세요.
    - id: e
      text: 패킷을 항상 폐기한다
      feedback: 중간 물류센터 비유에서 라우터가 상자를 어떻게 처리하는지 떠올려 보세요.
    answer: b
  question_placements:
  - question_id: u6-l01-p02-q01
    after_paragraph: 1
- terms:
  - TTL(Time To Live)
  - IP 헤더(IP header)
  - 라우팅 루프(Routing loop)
  animations:
  - file: l21-ttl-countdown.svg
    title: 라우터를 지날 때마다 줄어드는 TTL
    alt: 패킷의 TTL이 128에서 127, 126으로 줄어듭니다. 값이 소진되면 라우터가 패킷을 더 전달하지 않고 버립니다.
    caption: TTL은 패킷이 경로에서 끝없이 돌지 않도록 전달 가능 범위를 제한합니다.
    after_paragraph: 2
  questions:
  - id: u6-l01-p03-q01
    kind: choice
    difficulty: easy
    prompt: TTL은 IPv4 패킷에서 어떤 역할을 하나요?
    choices:
    - id: b
      text: 한 링크의 최대 패킷 크기를 정한다
      feedback: 이 페이지에서 TTL을 초시계 시간보다 어떤 한도로 설명하는지 떠올려 보세요.
    - id: c
      text: 도메인 이름을 IP 주소로 바꾼다
      feedback: 이 페이지에서 TTL을 초시계 시간보다 어떤 한도로 설명하는지 떠올려 보세요.
    - id: d
      text: 패킷을 암호화한다
      feedback: 이 페이지에서 TTL을 초시계 시간보다 어떤 한도로 설명하는지 떠올려 보세요.
    - id: e
      text: 서버의 포트 번호를 고른다
      feedback: 이 페이지에서 TTL을 초시계 시간보다 어떤 한도로 설명하는지 떠올려 보세요.
    - id: a
      text: 패킷이 라우터를 거쳐 전달될 수 있는 범위를 제한한다
      feedback: TTL은 전달이 끝없이 이어지지 않도록 패킷의 전달 범위를 제한합니다.
    answer: a
  - id: u6-l01-p03-q02
    kind: choice
    difficulty: medium
    prompt: IPv4를 전달할 때 TTL 값은 보통 어떻게 되나요?
    choices:
    - id: b
      text: 라우터를 지날 때마다 커진다
      feedback: 자유 이용권의 도장 비유처럼 전달할 때마다 값이 줄어듭니다.
    - id: a
      text: 라우터를 지날 때마다 줄어든다
      feedback: 라우터는 패킷을 전달할 때 TTL을 적어도 1 줄입니다.
    - id: c
      text: 목적지 이름으로 바뀐다
      feedback: 자유 이용권의 도장 비유처럼 전달할 때마다 값이 줄어듭니다.
    - id: d
      text: 링크 MTU와 같아진다
      feedback: 자유 이용권의 도장 비유처럼 전달할 때마다 값이 줄어듭니다.
    - id: e
      text: 항상 255로 다시 설정된다
      feedback: 자유 이용권의 도장 비유처럼 전달할 때마다 값이 줄어듭니다.
    answer: a
  - id: u6-l01-p03-q03
    kind: choice
    difficulty: medium
    prompt: TTL이라는 이름에 “시간”이 들어가지만, 일반적인 IPv4 전달에서 기억할 핵심은 무엇인가요?
    choices:
    - id: a
      text: 실제 초 단위 시간을 매번 재는 값이다
      feedback: 본문은 이름의 뜻과 실제로 학습할 동작을 구분합니다.
    - id: c
      text: DNS 응답을 기다리는 시간이다
      feedback: 본문은 이름의 뜻과 실제로 학습할 동작을 구분합니다.
    - id: d
      text: 링크가 유지되는 시간이다
      feedback: 본문은 이름의 뜻과 실제로 학습할 동작을 구분합니다.
    - id: b
      text: 라우터 전달 때마다 감소하는 한도다
      feedback: 이 Lesson에서는 TTL을 실제 초시계보다 홉마다 줄어드는 전달 한도로 이해합니다.
    - id: e
      text: DHCP 임대 기간이다
      feedback: 본문은 이름의 뜻과 실제로 학습할 동작을 구분합니다.
    answer: b
  question_placements:
  - question_id: u6-l01-p03-q01
    after_paragraph: 1
- terms:
  - 폐기(Drop)
  - ICMP Time Exceeded
  - ICMP(Internet Control Message Protocol)
  questions:
  - id: u6-l01-p04-q01
    kind: choice
    difficulty: easy
    prompt: TTL이 라우터에서 줄어 0이 되면 라우터는 보통 어떻게 하나요?
    choices:
    - id: b
      text: TTL을 255로 바꾸어 계속 보낸다
      feedback: TTL이 다 된 패킷을 계속 보내면 어떤 문제가 생기는지 생각해 보세요.
    - id: a
      text: 패킷을 더 전달하지 않고 폐기한다
      feedback: TTL이 0이 되면 라우터는 패킷을 더 전달하지 않고 폐기합니다.
    - id: c
      text: 패킷을 DHCP 서버로 보낸다
      feedback: TTL이 다 된 패킷을 계속 보내면 어떤 문제가 생기는지 생각해 보세요.
    - id: d
      text: 패킷을 항상 재조립한다
      feedback: TTL이 다 된 패킷을 계속 보내면 어떤 문제가 생기는지 생각해 보세요.
    - id: e
      text: 목적지 MAC 주소를 새로 만든다
      feedback: TTL이 다 된 패킷을 계속 보내면 어떤 문제가 생기는지 생각해 보세요.
    answer: a
  - id: u6-l01-p04-q02
    kind: choice
    difficulty: medium
    prompt: TTL이 만료된 패킷을 폐기한 라우터가 출발지에 보낼 수 있는 안내 메시지는 무엇인가요?
    choices:
    - id: a
      text: DHCP Offer
      feedback: 이 페이지에서 TTL 만료 상황과 연결한 ICMP 메시지 이름을 확인하세요.
    - id: c
      text: DNS Query
      feedback: 이 페이지에서 TTL 만료 상황과 연결한 ICMP 메시지 이름을 확인하세요.
    - id: d
      text: TCP ACK
      feedback: 이 페이지에서 TTL 만료 상황과 연결한 ICMP 메시지 이름을 확인하세요.
    - id: b
      text: ICMP Time Exceeded
      feedback: 가능한 경우 ICMP Time Exceeded로 TTL 만료를 알릴 수 있습니다.
    - id: e
      text: ARP Reply
      feedback: 이 페이지에서 TTL 만료 상황과 연결한 ICMP 메시지 이름을 확인하세요.
    answer: b
  - id: u6-l01-p04-q03
    kind: choice
    difficulty: medium
    prompt: TTL 만료 안내 응답이 보이지 않을 때 알맞은 해석은 무엇인가요?
    choices:
    - id: b
      text: 라우터나 방화벽이 안내 메시지를 보내지 않았을 수도 있다
      feedback: 라우터나 방화벽 설정에 따라 ICMP 안내를 보내지 않을 수 있습니다.
    - id: a
      text: 패킷이 반드시 목적지에 도착했다
      feedback: 응답이 없다는 사실만으로 패킷의 도착 여부를 단정하지 마세요.
    - id: c
      text: TTL 기능이 항상 꺼져 있다
      feedback: 응답이 없다는 사실만으로 패킷의 도착 여부를 단정하지 마세요.
    - id: d
      text: MTU가 0이라는 뜻이다
      feedback: 응답이 없다는 사실만으로 패킷의 도착 여부를 단정하지 마세요.
    - id: e
      text: DHCP 임대가 만료되었다
      feedback: 응답이 없다는 사실만으로 패킷의 도착 여부를 단정하지 마세요.
    answer: b
  question_placements:
  - question_id: u6-l01-p04-q01
    after_paragraph: 1
- terms:
  - MTU(Maximum Transmission Unit)
  - 링크(Link)
  - 패킷 크기
  questions:
  - id: u6-l01-p05-q01
    kind: choice
    difficulty: easy
    prompt: MTU가 제한하는 것은 무엇인가요?
    choices:
    - id: b
      text: 패킷이 지날 수 있는 라우터의 수
      feedback: TTL과 비교할 때 MTU는 전달 횟수가 아니라 무엇의 한계인지 확인하세요.
    - id: c
      text: 한 호스트의 프로세스 수
      feedback: TTL과 비교할 때 MTU는 전달 횟수가 아니라 무엇의 한계인지 확인하세요.
    - id: d
      text: DNS 이름의 글자 수
      feedback: TTL과 비교할 때 MTU는 전달 횟수가 아니라 무엇의 한계인지 확인하세요.
    - id: a
      text: 한 링크에서 한 번에 보낼 수 있는 IP 패킷의 크기
      feedback: MTU는 링크 하나에서 보낼 수 있는 IP 패킷 크기의 상한입니다.
    - id: e
      text: DHCP 임대 기간
      feedback: TTL과 비교할 때 MTU는 전달 횟수가 아니라 무엇의 한계인지 확인하세요.
    answer: a
  - id: u6-l01-p05-q02
    kind: choice
    difficulty: medium
    prompt: 한 경로 중간에 MTU 1,400바이트인 링크가 있다면 1,500바이트 IP 패킷에 어떤 문제가 생기나요?
    choices:
    - id: a
      text: 그 링크에 그대로 실을 수 없다
      feedback: 1,500바이트 패킷은 MTU 1,400바이트 링크에 그대로 실을 수 없습니다.
    - id: b
      text: TTL이 자동으로 1,400이 된다
      feedback: MTU는 경로 전체의 평균이 아니라 각 링크의 크기 한도입니다.
    - id: c
      text: 목적지 IP가 지워진다
      feedback: MTU는 경로 전체의 평균이 아니라 각 링크의 크기 한도입니다.
    - id: d
      text: 패킷은 무조건 더 작아진다
      feedback: MTU는 경로 전체의 평균이 아니라 각 링크의 크기 한도입니다.
    - id: e
      text: 라우터가 이를 웹 페이지로 바꾼다
      feedback: MTU는 경로 전체의 평균이 아니라 각 링크의 크기 한도입니다.
    answer: a
  - id: u6-l01-p05-q03
    kind: choice
    difficulty: medium
    prompt: 이 Lesson에서 말하는 MTU의 패킷 크기에는 무엇이 포함되나요?
    choices:
    - id: b
      text: 데이터 부분만
      feedback: MTU 한도를 데이터 부분만의 크기로 오해하지 않도록 본문 설명을 떠올리세요.
    - id: c
      text: Ethernet 케이블 길이
      feedback: MTU 한도를 데이터 부분만의 크기로 오해하지 않도록 본문 설명을 떠올리세요.
    - id: a
      text: IP 헤더와 데이터(페이로드)를 합친 전체 IP 패킷
      feedback: MTU는 IP 헤더와 데이터가 포함된 IP 패킷 전체의 크기를 제한합니다.
    - id: d
      text: IP 주소의 글자 수
      feedback: MTU 한도를 데이터 부분만의 크기로 오해하지 않도록 본문 설명을 떠올리세요.
    - id: e
      text: TCP 포트 번호만
      feedback: MTU 한도를 데이터 부분만의 크기로 오해하지 않도록 본문 설명을 떠올리세요.
    answer: a
  question_placements:
  - question_id: u6-l01-p05-q01
    after_paragraph: 1
- terms:
  - IPv4 단편화(IPv4 fragmentation)
  - 페이로드(Payload)
  - DF(Don't Fragment)
  animations:
  - file: l21-fragmentation.svg
    title: MTU보다 큰 IPv4 패킷을 더 작은 조각으로 나눈다
    alt: 1,500바이트 IP 패킷이 MTU 1,400바이트인 좁은 구간을 만나 페이로드 조각 두 개를 담은 더 작은 IPv4 패킷들로 나뉩니다.
    caption: IPv4 단편화에서는 페이로드를 나누고 각 조각에 IP 헤더를 붙여 다음 링크의 MTU에 맞춥니다.
    after_paragraph: 3
  questions:
  - id: u6-l01-p06-q01
    kind: choice
    difficulty: easy
    prompt: IPv4 단편화는 어떤 작업인가요?
    choices:
    - id: a
      text: MTU보다 큰 IPv4 패킷을 더 작은 IP 패킷 조각들로 나누는 일
      feedback: IPv4 단편화는 큰 패킷의 페이로드를 나누고 각 조각에 IP 헤더를 붙입니다.
    - id: b
      text: TTL을 여러 값으로 복사하는 일
      feedback: 단편화가 다루는 단위가 IP 패킷이라는 점을 확인하세요.
    - id: c
      text: TCP 연결을 여러 서버로 나누는 일
      feedback: 단편화가 다루는 단위가 IP 패킷이라는 점을 확인하세요.
    - id: d
      text: IP 주소를 MAC 주소로 바꾸는 일
      feedback: 단편화가 다루는 단위가 IP 패킷이라는 점을 확인하세요.
    - id: e
      text: 라우터 경로를 암호화하는 일
      feedback: 단편화가 다루는 단위가 IP 패킷이라는 점을 확인하세요.
    answer: a
  - id: u6-l01-p06-q02
    kind: choice
    difficulty: medium
    prompt: 단편화된 각 조각에 IP 헤더를 붙이는 이유는 무엇인가요?
    choices:
    - id: b
      text: 조각마다 새 웹 사이트를 만들기 위해
      feedback: 본문에서 조각마다 반복해 붙는 정보가 무엇인지 살펴보세요.
    - id: c
      text: TTL을 제거하기 위해
      feedback: 본문에서 조각마다 반복해 붙는 정보가 무엇인지 살펴보세요.
    - id: a
      text: 각 조각이 링크를 통해 전달될 수 있도록 패킷 정보가 필요하기 때문
      feedback: 각 조각은 IP 헤더를 갖고 다음 링크의 MTU 안에 들어가도록 전달됩니다.
    - id: d
      text: MAC 주소를 인터넷 주소로 바꾸기 위해
      feedback: 본문에서 조각마다 반복해 붙는 정보가 무엇인지 살펴보세요.
    - id: e
      text: DHCP 임대를 갱신하기 위해
      feedback: 본문에서 조각마다 반복해 붙는 정보가 무엇인지 살펴보세요.
    answer: a
  - id: u6-l01-p06-q03
    kind: choice
    difficulty: medium
    prompt: DF(Don’t Fragment) 표시가 “켜져” 단편화가 금지된 패킷이 더 작은 MTU 링크를 만나면 어떻게 되나요?
    choices:
    - id: b
      text: 라우터가 항상 두 배 크기로 만든다
      feedback: DF는 이름 그대로 조각내지 말라는 표시입니다.
    - id: c
      text: 클라이언트가 새 DHCP 주소를 받는다
      feedback: DF는 이름 그대로 조각내지 말라는 표시입니다.
    - id: d
      text: TTL이 자동으로 늘어난다
      feedback: DF는 이름 그대로 조각내지 말라는 표시입니다.
    - id: e
      text: 패킷은 제한 없이 그대로 전달된다
      feedback: DF는 이름 그대로 조각내지 말라는 표시입니다.
    - id: a
      text: 라우터가 임의로 단편화하지 않고 전달하지 못할 수 있다
      feedback: DF가 단편화를 금지하면 라우터가 임의로 조각내지 못해 패킷이 폐기될 수 있습니다.
    answer: a
  question_placements:
  - question_id: u6-l01-p06-q01
    after_paragraph: 1
- terms:
  - Identification(식별 값)
  - Flags(플래그)
  - Fragment Offset(단편 오프셋)
  - IP 재조립(IP reassembly)
  questions:
  - id: u6-l01-p07-q01
    kind: choice
    difficulty: easy
    prompt: 보통 IP 조각을 다시 모아 원래 패킷을 복원하는 곳은 어디인가요?
    choices:
    - id: a
      text: 각 중간 라우터
      feedback: 중간 라우터가 매 구간마다 조각을 합치는 동작은 기본이 아닙니다.
    - id: c
      text: 첫 번째 스위치
      feedback: 중간 라우터가 매 구간마다 조각을 합치는 동작은 기본이 아닙니다.
    - id: b
      text: 최종 수신 호스트
      feedback: IP 조각의 재조립은 보통 최종 수신 호스트에서 이뤄집니다.
    - id: d
      text: DNS 서버
      feedback: 중간 라우터가 매 구간마다 조각을 합치는 동작은 기본이 아닙니다.
    - id: e
      text: DHCP 릴레이
      feedback: 중간 라우터가 매 구간마다 조각을 합치는 동작은 기본이 아닙니다.
    answer: b
  - id: u6-l01-p07-q02
    kind: choice
    difficulty: medium
    prompt: IP 단편 중 하나가 목적지에 도착하지 않으면 어떤 일이 생길 수 있나요?
    choices:
    - id: b
      text: 라우터가 자동으로 누락 조각을 다시 요청한다
      feedback: IP 자체가 빠진 조각을 다시 요청하는 기능을 한다고 본문에서 설명했는지 확인하세요.
    - id: c
      text: 누락된 조각을 DHCP가 만들어 준다
      feedback: IP 자체가 빠진 조각을 다시 요청하는 기능을 한다고 본문에서 설명했는지 확인하세요.
    - id: d
      text: TTL이 원래 값으로 돌아온다
      feedback: IP 자체가 빠진 조각을 다시 요청하는 기능을 한다고 본문에서 설명했는지 확인하세요.
    - id: e
      text: 다른 조각이 자동으로 두 배 크기가 된다
      feedback: IP 자체가 빠진 조각을 다시 요청하는 기능을 한다고 본문에서 설명했는지 확인하세요.
    - id: a
      text: 수신 호스트가 원래 IP 패킷을 완성하지 못한다
      feedback: 한 조각이라도 빠지면 수신 측은 원래 IP 패킷을 완성하지 못할 수 있습니다.
    answer: a
  - id: u6-l01-p07-q03
    kind: choice
    difficulty: medium
    prompt: IP 패킷이 복원된 뒤 그 안에 들어 있던 TCP 세그먼트는 어떻게 되나요?
    choices:
    - id: b
      text: 다시 Ethernet 프레임으로 바뀌어 라우터에서 재조립된다
      feedback: IP 재조립과 TCP가 데이터를 다루는 순서를 연결해 보세요.
    - id: a
      text: 상위 계층으로 전달되어 TCP가 별도 규칙을 처리한다
      feedback: IP 패킷 복원과 TCP 바이트 흐름 처리는 계층이 다른 작업입니다.
    - id: c
      text: DHCP 서버로 전달된다
      feedback: IP 재조립과 TCP가 데이터를 다루는 순서를 연결해 보세요.
    - id: d
      text: TTL 값으로 바뀐다
      feedback: IP 재조립과 TCP가 데이터를 다루는 순서를 연결해 보세요.
    - id: e
      text: 폐기되어 응용 프로그램과 무관해진다
      feedback: IP 재조립과 TCP가 데이터를 다루는 순서를 연결해 보세요.
    answer: a
  question_placements:
  - question_id: u6-l01-p07-q01
    after_paragraph: 1
- terms:
  - TCP 세그먼트(TCP segment)
  - IP 단편(IP fragment)
  - 터널링(Tunneling)
  - VPN(Virtual Private Network)
  questions:
  - id: u6-l01-p08-q01
    kind: choice
    difficulty: easy
    prompt: TTL과 MTU의 차이를 바르게 설명한 것은 무엇인가요?
    choices:
    - id: b
      text: TTL은 패킷 크기, MTU는 DNS 시간을 다룬다
      feedback: 두 값이 각각 이동 한계와 크기 한계 중 무엇을 나타내는지 구분하세요.
    - id: c
      text: 둘 다 IP 주소를 자동 배정한다
      feedback: 두 값이 각각 이동 한계와 크기 한계 중 무엇을 나타내는지 구분하세요.
    - id: d
      text: TTL은 링크 종류, MTU는 라우터 개수를 센다
      feedback: 두 값이 각각 이동 한계와 크기 한계 중 무엇을 나타내는지 구분하세요.
    - id: e
      text: 두 값은 서로 바꾸어 쓸 수 있다
      feedback: 두 값이 각각 이동 한계와 크기 한계 중 무엇을 나타내는지 구분하세요.
    - id: a
      text: TTL은 전달 범위, MTU는 링크별 패킷 크기 한계를 다룬다
      feedback: TTL은 전달이 끝없이 이어지는 일을, MTU는 한 링크의 크기 초과를 다룹니다.
    answer: a
  - id: u6-l01-p08-q02
    kind: choice
    difficulty: medium
    prompt: TTL이 남아 있어도 패킷이 전달되지 않을 수 있는 상황은 무엇인가요?
    choices:
    - id: b
      text: IP 패킷에 목적지 주소가 있는 경우
      feedback: 전달 횟수 한도와 링크 크기 한도는 독립적으로 확인해야 합니다.
    - id: a
      text: 패킷이 경로 링크의 MTU보다 크고 처리 가능한 방법이 없는 경우
      feedback: TTL과 별개로 링크의 MTU보다 패킷이 크면 그 구간에서 처리할 방법이 필요합니다.
    - id: c
      text: 라우터가 다음 홉을 아는 경우
      feedback: 전달 횟수 한도와 링크 크기 한도는 독립적으로 확인해야 합니다.
    - id: d
      text: 패킷 크기가 링크 MTU 안에 들어가는 경우
      feedback: 전달 횟수 한도와 링크 크기 한도는 독립적으로 확인해야 합니다.
    - id: e
      text: 목적지가 네트워크에 연결된 경우
      feedback: 전달 횟수 한도와 링크 크기 한도는 독립적으로 확인해야 합니다.
    answer: a
  - id: u6-l01-p08-q03
    kind: choice
    difficulty: medium
    prompt: MTU보다 큰 IPv4 패킷이 링크를 만나면 어떤 설명이 맞나요?
    choices:
    - id: b
      text: 항상 그대로 전달된다
      feedback: 본문의 DF와 단편화 설명을 함께 떠올려 보세요.
    - id: c
      text: TTL이 자동으로 늘어나 전달된다
      feedback: 본문의 DF와 단편화 설명을 함께 떠올려 보세요.
    - id: d
      text: DHCP가 패킷을 나누어 준다
      feedback: 본문의 DF와 단편화 설명을 함께 떠올려 보세요.
    - id: a
      text: 단편화가 허용되면 조각으로 나눌 수 있고, 금지되면 전달되지 않을 수 있다
      feedback: IPv4 단편화 허용 여부에 따라 조각을 만들거나 전달하지 못할 수 있습니다.
    - id: e
      text: 모든 라우터가 반드시 조각을 재조립한다
      feedback: 본문의 DF와 단편화 설명을 함께 떠올려 보세요.
    answer: a
  question_placements:
  - question_id: u6-l01-p08-q01
    after_paragraph: 1
- terms:
  - 홉 수(Hop count)
  - MTU
  - 단편화(Fragmentation)
  - 재조립(Reassembly)
animations_dir: units/04-layer3-addressing/lessons/11-ttl과-단편화/assets/animations
---
## 패킷은 경로를 따라 이동하고, 크기에도 한계가 있다

웹 페이지를 열면 IP 패킷은 내 컴퓨터에서 출발해 여러 라우터를 거쳐 서버로 간다. 이때 패킷은 목적지에 도착하기 전까지 무한히 떠돌아서는 안 되고, 지나가는 링크마다 한 번에 실을 수 있는 크기도 다를 수 있다. 이 Lesson에서는 두 질문을 따라간다. **패킷은 경로에서 얼마나 오래 전달될 수 있을까?** 그리고 **중간 구간이 패킷을 다 실을 수 없으면 어떻게 될까?**

먼저 큰 흐름을 보자. 라우터를 지나는 횟수는 Hop으로 세고, IP 헤더의 TTL은 전달이 끝없이 이어지지 않게 한다. MTU는 링크마다 보낼 수 있는 IP 패킷 크기를 제한한다. IPv4에서는 조건에 따라 큰 패킷을 작은 조각으로 나눌 수 있지만, 이 조각 나누기는 Unit 4 Lesson 5에서 본 TCP의 바이트 흐름 분할과 다른 일이다.

아래 지도는 이번 Lesson의 순서다. 먼저 라우터와 Hop을 보고 TTL의 역할을 익힌 뒤, 링크별 MTU와 IPv4 단편화, 수신 측 재조립을 살펴본다. TCP 연결이나 재전송 절차를 다시 배우는 Lesson은 아니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 이 Lesson은 라우터의 홉 제한 TTL과 링크별 MTU가 패킷에 주는 영향을 함께 다룬다.
- **적용하기 (Apply):** 장거리 경로와 용량이 작은 링크에서 각각 어떤 제한을 만나는지 예상한다.
- **찾아보기 (Lookup):** 홉 처리와 크기 한도는 다음 Page의 TTL·MTU 설명에서 나누어 본다.

## 라우터가 패킷을 다음 홉으로 전달한다
<!-- learn-page-id: hop-count -->

라우터는 자신에게 도착한 패킷을 읽고 목적지 IP 주소를 확인한다. 그리고 라우팅 테이블을 참고해 그 패킷을 어느 방향으로 넘길지 결정한다. 패킷의 최종 목적지가 라우터 자신이 아니라면, 라우터는 내용을 사용하지 않고 다음 장비로 전달한다. 이 동작을 **전달(Forwarding)**이라고 한다.

택배를 예로 들면, 중간 물류센터는 상자를 열어 물건을 쓰는 곳이 아니다. 송장의 목적지를 확인해 다음 물류센터로 보내는 곳이다. 다만 실제 라우터는 물건을 며칠씩 보관하는 창고가 아니라, 패킷을 매우 짧은 시간 동안 처리해 다음 경로로 넘기는 네트워크 장비다.

라우터에서 다음 라우터로 한 번 넘어가는 이동을 **홉(Hop)**이라고 한다. PC에서 라우터 A, 라우터 B를 거쳐 서버로 갔다면 라우터를 두 번 거친 경로라고 셀 수 있다. 목적지까지 이어지는 전체 경로가 몇 Hop인지는 중간에 어떤 라우터를 거치는지에 따라 달라진다. [Unit 2 Lesson 3에서 본 다음 홉과 라우팅 테이블](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/2/lesson/3/page/4)을 떠올리면, 라우터가 한 번에 전체 경로를 외워서 달리는 것이 아니라 다음 전달 지점을 선택한다는 점이 연결된다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 라우터는 패킷을 목적지까지 직접 운반하기보다 다음 홉으로 전달한다.
- **적용하기 (Apply):** 라우팅 표의 다음 홉을 따라 패킷이 여러 라우터를 지나가는 경로를 설명한다.
- **찾아보기 (Lookup):** 각 라우터 처리 뒤 TTL이 바뀌는 과정은 TTL Page에서 확인한다.

## TTL은 패킷이 끝없이 돌지 않도록 한다
<!-- learn-page-id: ttl-definition -->

라우터들이 경로 정보를 잘못 배워 패킷을 라우터 A에서 B로, 다시 B에서 A로 보내는 상황을 생각해 보자. 이런 **라우팅 루프**가 생기면 패킷이 목적지에 도착하지 못한 채 네트워크 안을 계속 돌 수 있다. 그래서 IPv4 패킷에는 이동을 제한하는 값인 **TTL(Time To Live)**이 있다.

TTL은 IP 헤더에 담기는 8비트 값이다. 이름에는 ‘시간(Time)’이 들어 있지만, 일반적인 IPv4 전달에서는 실제 초시계처럼 시간을 재기보다 라우터가 전달할 때마다 값이 줄어드는 한도로 이해하면 된다. 라우터는 패킷을 전달할 때 TTL을 적어도 1 줄인다. 실제 처음 값은 운영체제나 장비 설정에 따라 다르므로, `64`, `128`, `255` 중 하나를 외우기보다 경로를 따라 감소한다는 원리를 기억하자.

놀이공원 자유 이용권에 정해진 횟수의 도장이 있다고 생각해 보자. 놀이기구를 한 번 탈 때마다 도장 하나를 쓰고, 다 쓰면 더는 입장하지 못한다. TTL도 이와 비슷하게 패킷이 라우터를 거쳐 전달될 수 있는 범위를 제한한다. 비유와 달리 실제 패킷에 사람이 도장을 찍는 것은 아니다. 라우터가 IP 헤더 값을 처리한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TTL은 라우팅 루프에서 패킷이 끝없이 순환하지 않도록 홉마다 줄어든다.
- **적용하기 (Apply):** 초기 TTL과 경유 라우터 수를 보고 남은 TTL을 계산한다.
- **찾아보기 (Lookup):** 운영체제가 보내는 초기 TTL은 환경에 따라 달라져 캡처에서 확인한다.

## TTL이 0이 되면 라우터는 패킷을 폐기한다

TTL이 라우터에서 줄어 0이 되면 그 라우터는 패킷을 더 전달하지 않고 **폐기(Drop)**한다. 그래야 경로를 잘못 돈 패킷이 네트워크 자원을 계속 차지하지 않는다. 예를 들어 TTL이 3인 패킷은 첫 라우터에서 2, 둘째에서 1로 줄고, 셋째 라우터에서 0이 되므로 그 자리에서 폐기된다.

폐기한 라우터가 출발지에 이유를 알려 주기도 한다. 이때 사용하는 안내 메시지의 한 종류가 **ICMP Time Exceeded**다. ICMP는 IP 통신에서 오류나 상태를 알리는 데 쓰이는 프로토콜이다. 다만 라우터나 방화벽 설정에 따라 안내 메시지를 보내지 않을 수도 있으므로, 응답이 없다고 해서 반드시 패킷이 목적지에 도착했다고 볼 수는 없다.

이 메시지는 Unit 5 Lesson 1에서 IP 헤더의 Protocol 칸을 읽을 때 본 ICMP와 연결된다. 뒤의 Ping Lesson에서 다룰 Echo 요청·응답과는 목적이 다른 ICMP 메시지다. 하나는 시간이 다 된 패킷을 알리고, 다른 하나는 왕복 응답을 확인하는 데 쓰인다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TTL이 0이 되면 라우터는 패킷 전달을 멈추고 폐기한다.
- **적용하기 (Apply):** TTL 만료가 목적지 미도달과 ICMP 안내로 이어지는 과정을 말한다.
- **찾아보기 (Lookup):** ICMP Time Exceeded 형식과 정책은 RFC와 장비 설정을 찾아본다.

## MTU는 링크마다 한 번에 보낼 IP 패킷 크기를 제한한다

TTL이 이동 횟수의 한도라면, **MTU(Maximum Transmission Unit)**는 한 링크가 한 번에 실을 수 있는 IP 패킷 크기의 상한이다. Unit 4에서 본 이더넷 MTU 1,500바이트는 익숙한 예다. 이는 링크 하나의 한도이므로 경로의 다른 링크에서 값이 더 작을 수도 있다.

예를 들어 출발지에서 1,500바이트까지 전달할 수 있어도, 경로 중간에 MTU가 1,400바이트인 링크가 있다면 1,500바이트 패킷을 그 링크에 그대로 실을 수 없다. 여기서 MTU는 IP 헤더와 데이터를 합친 패킷 전체를 가리키므로 데이터 부분만 1,400바이트까지 보내도 된다는 뜻이 아니다. 경로를 따라 통과하는 한도가 달라질 수 있다는 점이 중요하다.

택배 트럭의 적재 상한이 도로 구간마다 다르다고 생각해 보자. 큰 트럭이 출발할 수 있어도 중간에 작은 터널이 있으면 그 구간에 맞는 방법을 찾아야 한다. 네트워크에서는 더 작은 MTU를 가진 구간이 패킷 전달을 제한한다. 이 Lesson에서는 1,500과 1,400바이트를 크기 관계를 이해하는 예로만 사용한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** MTU는 링크 하나에서 전달 가능한 IP Packet 크기 상한이다.
- **적용하기 (Apply):** 경로 중 더 작은 MTU 링크를 만나면 어떤 처리가 필요한지 판단한다.
- **찾아보기 (Lookup):** Path MTU discovery 동작은 IPv4·IPv6 환경별 문서에서 확인한다.

## IPv4 단편화는 큰 패킷의 페이로드를 나누는 일이다
<!-- learn-page-id: fragmentation-definition -->

**IPv4 단편화(Fragmentation)**는 MTU보다 큰 IPv4 패킷을 더 작은 IP 패킷 조각들로 나누는 일이다. 위 예에서 1,500바이트 패킷이 MTU 1,400바이트인 링크에 도착하면, IPv4 라우터는 단편화가 허용된 경우 원래 패킷의 페이로드를 여러 부분으로 나누고 각 부분에 새 IP 헤더를 붙여 보낼 수 있다.

원래 패킷의 IP 헤더는 조각마다 반복해서 붙는다. 그 결과 각 조각의 전체 크기는 해당 링크의 MTU 안에 들어간다. 단편화가 금지된 패킷이라면 라우터가 임의로 나누지 않고 패킷을 폐기하며, 가능한 경우 출발지에 MTU 문제를 알린다. IP 헤더의 DF(Don't Fragment) 표시는 “조각내지 말라”는 뜻이다.

여기서 나누는 대상은 **IP 패킷의 페이로드**다. Unit 4 Lesson 5에서 본 TCP 세그먼트 분할은 TCP가 바이트 흐름을 다루는 별도 작업이다. 두 경우 모두 ‘나눈다’고 말하지만, 계층과 단위가 다르다. U5L1에서 이름을 본 Identification, Flags, Fragment Offset은 IP 조각들이 같은 원래 패킷에 속하는지와 원래 데이터의 어느 부분인지 표시하는 칸이다. 이 Lesson에서는 역할만 연결하고 오프셋 계산은 요구하지 않는다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** IPv4 fragmentation은 큰 Packet의 Payload를 여러 조각으로 나눈다.
- **적용하기 (Apply):** MTU가 더 작은 링크에서 Fragment offset과 길이 값의 역할을 설명한다.
- **찾아보기 (Lookup):** DF·MF flag와 offset 계산은 IPv4 헤더 문서를 찾아본다.

## 수신 호스트가 IP 조각을 재조립한다

각 IP 조각은 네트워크를 거쳐 목적지로 전달되고, 보통 **최종 수신 호스트**의 IP 기능이 조각을 다시 모아 원래 IP 패킷을 복원한다. 라우터가 조각들을 매 구간마다 합쳤다가 다시 나누는 것은 기본 동작이 아니다. 한 조각이라도 도착하지 않으면 수신 측은 원래 IP 패킷을 완성할 수 없고, IP 자체가 그 조각을 다시 요청해 주는 것도 아니다.

IP 패킷이 복원된 다음에는 그 안의 TCP 세그먼트가 상위 계층으로 전달된다. TCP는 별도의 바이트 흐름 규칙을 다룬다. 따라서 **IP 조각의 재조립**과 **TCP 데이터 흐름의 처리**를 같은 ‘합치기’로 뭉뚱그리지 말자.

가능하면 경로에 맞는 크기의 패킷을 처음부터 보내 단편화를 줄이는 편이 낫다. VPN처럼 기존 패킷을 새 포장으로 감싸는 터널 구간에서는 추가 헤더가 자리를 차지해, 한 링크에 넣을 수 있는 원래 데이터가 줄어들 수 있다. 자세한 터널 설정이나 경로 MTU 찾기 절차는 여기서 외우지 않고, MTU가 예상보다 작아질 수 있는 사례로만 기억한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 보통 최종 수신 Host가 IP Fragment를 재조립한다.
- **적용하기 (Apply):** 조각 하나가 누락되면 원래 IP Packet을 완성할 수 없는 이유를 설명한다.
- **찾아보기 (Lookup):** 재조립 제한과 타이머는 OS·프로토콜 자료에서 확인한다.

## TTL과 MTU는 서로 다른 한계를 다룬다

TTL과 MTU는 모두 패킷 전달의 한계를 나타내지만 서로 바꿔 쓸 수 있는 값이 아니다. **TTL은 패킷이 라우터를 거쳐 전달될 수 있는 범위**를 제한하고, **MTU는 한 링크가 한 번에 실을 수 있는 IP 패킷의 크기**를 제한한다. 하나는 이동 과정의 횟수 쪽, 다른 하나는 한 구간의 크기 쪽 문제다.

예를 들어 패킷이 목적지까지 가는 중 TTL이 먼저 0이 되면, 링크의 MTU가 충분해도 라우터는 패킷을 더 전달하지 않는다. 반대로 TTL이 남아 있어도 어떤 링크의 MTU보다 패킷이 크면, 해당 링크에서 처리할 방법이 필요하다. IPv4에서 단편화가 허용된 경우에는 조각을 만들 수 있고, 금지된 경우에는 전달되지 않을 수 있다.

이 Lesson의 순서를 한 번 더 이어 보자. 라우터는 다음 홉으로 패킷을 넘기고, TTL은 전달이 끝없이 계속되는 일을 막는다. 각 링크의 MTU는 패킷 크기를 제한하며, 필요한 경우 IPv4가 페이로드를 조각내고 최종 수신 호스트가 다시 모은다. TCP 세그먼트 분할은 이 IP 단편화와 다른 계층의 작업이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TTL은 이동 홉 수, MTU는 링크별 Packet 크기 한도를 제한한다.
- **적용하기 (Apply):** 경로가 너무 길 때와 패킷이 너무 클 때의 증상을 구별한다.
- **찾아보기 (Lookup):** 단편화 없는 경로 크기 확인은 `tracepath` 등 OS 도구 도움말을 본다.