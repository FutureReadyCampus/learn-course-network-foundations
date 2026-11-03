---
id: u4-l24-ping과-rtt
title: Ping과 RTT
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-24.md
additional_sources:
  - https://studio.futurereadycampus.com/course-network/wiki/oeweo-network/lesson-24.html
  - https://www.rfc-editor.org/rfc/rfc792.html
wiki_diagram: units/04-layer3-addressing/lessons/14-ping과-rtt/assets/diagrams/lesson-24.svg
page_metadata:
- terms:
  - 동기화(Synchronization)
  - 서버(Server)
  - 지연(Latency)
  questions:
  - id: u6-l04-p01-q01
    kind: choice
    difficulty: easy
    prompt: 온라인 게임에서 “핑이 높다”고 말할 때 주로 걱정하는 것은 무엇인가요?
    choices:
    - id: a
      text: 서버와 데이터를 주고받는 왕복 지연이 큰 것
      feedback: 게임에서 말하는 핑은 서버와 주고받는 지연을 가리키며 RTT로 잴 수 있습니다.
    - id: b
      text: 컴퓨터 화면의 해상도가 높은 것
      feedback: 게임의 상태 동기화와 서버까지 다녀오는 시간의 관계를 생각하세요.
    - id: c
      text: DHCP 주소 풀의 크기
      feedback: 게임의 상태 동기화와 서버까지 다녀오는 시간의 관계를 생각하세요.
    - id: d
      text: 라우터 포트 수
      feedback: 게임의 상태 동기화와 서버까지 다녀오는 시간의 관계를 생각하세요.
    - id: e
      text: 프레임의 색상 수
      feedback: 게임의 상태 동기화와 서버까지 다녀오는 시간의 관계를 생각하세요.
    answer: a
  - id: u6-l04-p01-q02
    kind: choice
    difficulty: medium
    prompt: RTT는 어떤 시간을 뜻하나요?
    choices:
    - id: a
      text: 패킷이 라우터 한 대를 지나는 시간만
      feedback: 단방향이 아니라 요청과 응답이 오가는 전체 시간을 말합니다.
    - id: b
      text: DHCP 주소를 임대하는 기간
      feedback: 단방향이 아니라 요청과 응답이 오가는 전체 시간을 말합니다.
    - id: c
      text: 목적지까지 갔다가 응답이 돌아오는 왕복 시간
      feedback: RTT는 Round Trip Time, 즉 왕복 시간입니다.
    - id: d
      text: 한 Ethernet 프레임의 전송 속도
      feedback: 단방향이 아니라 요청과 응답이 오가는 전체 시간을 말합니다.
    - id: e
      text: DNS 이름의 길이
      feedback: 단방향이 아니라 요청과 응답이 오가는 전체 시간을 말합니다.
    answer: c
  - id: u6-l04-p01-q03
    kind: choice
    difficulty: medium
    prompt: 같은 서버에 왕복 시간이 철수 20ms, 영희 25ms, 길동 50ms라면 가장 짧은 RTT는 누구인가요?
    choices:
    - id: a
      text: 영희
      feedback: 밀리초 수치가 작을수록 이 예에서는 왕복 시간이 짧습니다.
    - id: b
      text: 길동
      feedback: 밀리초 수치가 작을수록 이 예에서는 왕복 시간이 짧습니다.
    - id: c
      text: 세 명 모두 같다
      feedback: 밀리초 수치가 작을수록 이 예에서는 왕복 시간이 짧습니다.
    - id: d
      text: 주어진 값으로 비교할 수 없다
      feedback: 밀리초 수치가 작을수록 이 예에서는 왕복 시간이 짧습니다.
    - id: e
      text: 철수
      feedback: 20ms가 가장 작으므로 철수의 RTT가 가장 짧습니다.
    answer: e
- terms:
  - RTT(Round Trip Time)
  - 밀리초(ms)
  - Ping(핑)
  animations:
  - file: l24-ping-round-trip.svg
    title: 세 사람의 왕복 시간
    alt: 철수, 영희, 길동의 컴퓨터에서 각각 서버로 신호 점이 출발해 돌아오는 장면입니다. 철수의 점이 가장 먼저 돌아오고 길동의 점이 가장
      늦게 돌아오며, 마지막에 20, 25, 50ms 막대 길이가 비교됩니다.
    caption: 같은 서버를 다녀오는 데 철수는 20ms, 영희는 25ms, 길동은 50ms가 걸립니다.
  questions:
  - id: u6-l04-p02-q01
    kind: choice
    difficulty: easy
    prompt: Ping은 무엇인가요?
    choices:
    - id: a
      text: IP 주소에 MAC 주소를 배정하는 프로토콜
      feedback: Ping 프로그램, ICMP 프로토콜, RTT 측정값을 구분하세요.
    - id: b
      text: 라우터의 하드웨어 주소
      feedback: Ping 프로그램, ICMP 프로토콜, RTT 측정값을 구분하세요.
    - id: c
      text: 네트워크 응답을 확인하고 RTT를 측정하는 프로그램
      feedback: Ping은 ICMP Echo를 이용해 응답과 RTT를 확인하는 프로그램입니다.
    - id: d
      text: DHCP 임대 메시지
      feedback: Ping 프로그램, ICMP 프로토콜, RTT 측정값을 구분하세요.
    - id: e
      text: Ethernet 링크의 최대 크기
      feedback: Ping 프로그램, ICMP 프로토콜, RTT 측정값을 구분하세요.
    answer: c
  - id: u6-l04-p02-q02
    kind: choice
    difficulty: medium
    prompt: Ping이 왕복 시간을 측정할 때 사용하는 메시지 방식은 무엇인가요?
    choices:
    - id: a
      text: DHCP Discover와 Offer
      feedback: ICMP 안에서도 TTL 만료 알림과 Ping의 Echo는 목적이 다릅니다.
    - id: b
      text: ARP Request와 DNS Reply
      feedback: ICMP 안에서도 TTL 만료 알림과 Ping의 Echo는 목적이 다릅니다.
    - id: c
      text: TCP FIN과 ACK
      feedback: ICMP 안에서도 TTL 만료 알림과 Ping의 Echo는 목적이 다릅니다.
    - id: d
      text: Ethernet 프레임의 브로드캐스트만
      feedback: ICMP 안에서도 TTL 만료 알림과 Ping의 Echo는 목적이 다릅니다.
    - id: e
      text: ICMP Echo 요청과 응답
      feedback: Ping은 ICMP Echo 요청과 그 응답을 이용합니다.
    answer: e
  - id: u6-l04-p02-q03
    kind: choice
    difficulty: medium
    prompt: ICMP에 대한 설명으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 도메인 이름을 등록하는 시스템
      feedback: Ping은 ICMP를 이용하지만 Ping 자체가 프로토콜인 것은 아닙니다.
    - id: b
      text: IP 통신에서 오류나 상태를 알리는 메시지를 주고받는 프로토콜
      feedback: ICMP는 IP 통신에서 오류나 상태를 알리는 메시지에 사용됩니다.
    - id: c
      text: Ethernet MAC 주소를 배정하는 서버
      feedback: Ping은 ICMP를 이용하지만 Ping 자체가 프로토콜인 것은 아닙니다.
    - id: d
      text: TCP 연결을 암호화하는 프로그램
      feedback: Ping은 ICMP를 이용하지만 Ping 자체가 프로토콜인 것은 아닙니다.
    - id: e
      text: 네트워크 케이블 규격
      feedback: Ping은 ICMP를 이용하지만 Ping 자체가 프로토콜인 것은 아닙니다.
    answer: b
  question_placements:
  - question_id: u6-l04-p02-q01
    after_paragraph: 1
- terms:
  - 응답 시간
  questions:
  - id: u6-l04-p03-q01
    kind: choice
    difficulty: easy
    prompt: RTT 값으로 직접 확인하려는 것은 무엇인가요?
    choices:
    - id: a
      text: 서버의 물리적 거리만
      feedback: 거리나 장치 정보와 시간을 혼동하지 마세요.
    - id: b
      text: 패킷 안의 데이터 크기
      feedback: 거리나 장치 정보와 시간을 혼동하지 마세요.
    - id: c
      text: DHCP 임대가 끝나는 시각
      feedback: 거리나 장치 정보와 시간을 혼동하지 마세요.
    - id: d
      text: 라우터의 MAC 주소
      feedback: 거리나 장치 정보와 시간을 혼동하지 마세요.
    - id: e
      text: 요청을 보내고 응답이 돌아올 때까지의 시간
      feedback: RTT는 왕복 응답 시간을 나타냅니다.
    answer: e
  - id: u6-l04-p03-q02
    kind: choice
    difficulty: medium
    prompt: 어떤 사용자에게 20ms, 다른 사용자에게 50ms의 RTT가 측정됐다면 알 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: 50ms인 사용자는 반드시 서버에서 더 멀다
      feedback: RTT 수치가 보여 주는 사실과 그 원인에 대한 추측을 나누세요.
    - id: b
      text: 두 사용자의 왕복 응답 시간에 차이가 있다
      feedback: 측정값은 응답 시간 차이를 보여 주며, 그 원인이나 게임 구현을 모두 결정하지는 않습니다.
    - id: c
      text: 20ms인 사용자는 항상 게임에서 이긴다
      feedback: RTT 수치가 보여 주는 사실과 그 원인에 대한 추측을 나누세요.
    - id: d
      text: 두 사용자의 인터넷 속도는 정확히 2.5배 차이다
      feedback: RTT 수치가 보여 주는 사실과 그 원인에 대한 추측을 나누세요.
    - id: e
      text: RTT만으로 게임 구현 방식을 알 수 있다
      feedback: RTT 수치가 보여 주는 사실과 그 원인에 대한 추측을 나누세요.
    answer: b
  - id: u6-l04-p03-q03
    kind: choice
    difficulty: medium
    prompt: 느린 사용자를 기준으로 게임을 동기화할지는 무엇에 해당하나요?
    choices:
    - id: a
      text: RTT 측정 자체의 정의
      feedback: 네트워크 측정과 그 값을 이용하는 응용 프로그램의 설계를 구분하세요.
    - id: b
      text: DHCP 주소 할당 방식
      feedback: 네트워크 측정과 그 값을 이용하는 응용 프로그램의 설계를 구분하세요.
    - id: c
      text: ICMP의 이름
      feedback: 네트워크 측정과 그 값을 이용하는 응용 프로그램의 설계를 구분하세요.
    - id: d
      text: 게임 구현의 선택
      feedback: 느린 사용자를 기준으로 맞출지는 게임 구현의 문제입니다.
    - id: e
      text: 기본 게이트웨이의 주소
      feedback: 네트워크 측정과 그 값을 이용하는 응용 프로그램의 설계를 구분하세요.
    answer: d
- terms:
  - Ping 명령(Ping command)
  - 게이트웨이(Gateway)
  questions:
  - id: u6-l04-p04-q01
    kind: choice
    difficulty: easy
    prompt: Ping을 간단한 네트워크 진단 도구로 사용하는 목적은 무엇인가요?
    choices:
    - id: a
      text: 웹 서버의 모든 페이지 내용을 확인한다
      feedback: Ping은 제한된 진단 정보를 주며 모든 장애를 고치지는 않습니다.
    - id: b
      text: 대상까지 요청과 응답이 오가는지 살펴본다
      feedback: Ping은 네트워크 연결을 살펴보는 간단한 진단 도구입니다.
    - id: c
      text: DHCP 주소 풀을 수정한다
      feedback: Ping은 제한된 진단 정보를 주며 모든 장애를 고치지는 않습니다.
    - id: d
      text: MAC 주소의 제조사를 반드시 찾는다
      feedback: Ping은 제한된 진단 정보를 주며 모든 장애를 고치지는 않습니다.
    - id: e
      text: 모든 네트워크 문제를 자동 복구한다
      feedback: Ping은 제한된 진단 정보를 주며 모든 장애를 고치지는 않습니다.
    answer: b
  - id: u6-l04-p04-q02
    kind: choice
    difficulty: medium
    prompt: 내 컴퓨터와 가까운 네트워크 구간을 확인하려고 Ping할 수 있는 대상은 무엇인가요?
    choices:
    - id: a
      text: 인터넷의 모든 IP 주소를 동시에
      feedback: 첫 확인 대상은 실제 설정에 표시된 로컬 게이트웨이입니다.
    - id: b
      text: 임의의 이웃 Wi-Fi 장치
      feedback: 첫 확인 대상은 실제 설정에 표시된 로컬 게이트웨이입니다.
    - id: c
      text: 내 컴퓨터의 파일 경로
      feedback: 첫 확인 대상은 실제 설정에 표시된 로컬 게이트웨이입니다.
    - id: d
      text: 현재 설정에 표시된 기본 게이트웨이
      feedback: 기본 게이트웨이로 Ping을 보내 가까운 네트워크 구간을 살펴볼 수 있습니다.
    - id: e
      text: DHCP 주소 풀 전체
      feedback: 첫 확인 대상은 실제 설정에 표시된 로컬 게이트웨이입니다.
    answer: d
  - id: u6-l04-p04-q03
    kind: choice
    difficulty: medium
    prompt: 진단 목적으로 Ping을 보낼 때 알맞은 태도는 무엇인가요?
    choices:
    - id: a
      text: 필요한 횟수만 요청하고 허가 없는 서버에 과도하게 보내지 않는다
      feedback: 필요한 횟수만 요청하고 허가받지 않은 서버에 과도하게 요청하지 않습니다.
    - id: b
      text: 대상 서버에 가능한 한 많은 요청을 계속 보낸다
      feedback: 본문의 진단 예는 제한된 요청 횟수를 사용합니다.
    - id: c
      text: 응답을 보장하려고 라우터를 우회한다
      feedback: 본문의 진단 예는 제한된 요청 횟수를 사용합니다.
    - id: d
      text: 모든 외부 주소를 자동 검색한다
      feedback: 본문의 진단 예는 제한된 요청 횟수를 사용합니다.
    - id: e
      text: Ping을 항상 무한 반복한다
      feedback: 본문의 진단 예는 제한된 요청 횟수를 사용합니다.
    answer: a
- terms:
  - 게이트웨이 주소
  questions:
  - id: u6-l04-p05-q01
    kind: choice
    difficulty: easy
    prompt: Ping 결과의 time 값은 무엇을 나타내나요?
    choices:
    - id: a
      text: 남은 DHCP 임대 시간
      feedback: time과 TTL은 서로 다른 출력 항목입니다.
    - id: b
      text: 패킷 크기(byte)
      feedback: time과 TTL은 서로 다른 출력 항목입니다.
    - id: c
      text: 라우터까지의 정확한 거리
      feedback: time과 TTL은 서로 다른 출력 항목입니다.
    - id: d
      text: 왕복 시간(ms)
      feedback: Ping 응답의 time 값은 왕복 시간이며 밀리초로 표시됩니다.
    - id: e
      text: MAC 주소 수
      feedback: time과 TTL은 서로 다른 출력 항목입니다.
    answer: d
  - id: u6-l04-p05-q02
    kind: choice
    difficulty: medium
    prompt: Ping 응답의 TTL 값을 어떻게 해석해야 하나요?
    choices:
    - id: a
      text: 돌아온 응답 패킷의 남은 전달 한도이며 정확한 거리나 RTT가 아니다
      feedback: 응답의 TTL은 전달 한도와 관련되며 RTT나 정확한 거리 값은 아닙니다.
    - id: b
      text: 요청의 왕복 시간을 밀리초로 나타낸다
      feedback: 출력에서 time, TTL, 손실률의 의미를 구분하세요.
    - id: c
      text: 서버와의 물리적 거리를 정확히 나타낸다
      feedback: 출력에서 time, TTL, 손실률의 의미를 구분하세요.
    - id: d
      text: DHCP 임대 기간을 나타낸다
      feedback: 출력에서 time, TTL, 손실률의 의미를 구분하세요.
    - id: e
      text: 응답 손실률을 나타낸다
      feedback: 출력에서 time, TTL, 손실률의 의미를 구분하세요.
    answer: a
  - id: u6-l04-p05-q03
    kind: choice
    difficulty: medium
    prompt: Ping 요약의 손실률은 무엇의 비율인가요?
    choices:
    - id: a
      text: 손실된 파일의 크기
      feedback: 응답 시간과 응답이 아예 없었던 비율은 다른 지표입니다.
    - id: b
      text: 라우터를 거친 홉의 비율
      feedback: 응답 시간과 응답이 아예 없었던 비율은 다른 지표입니다.
    - id: c
      text: 응답하지 않은 요청의 비율
      feedback: 손실률은 보낸 요청 가운데 응답하지 않은 요청의 비율입니다.
    - id: d
      text: DHCP Offer 중 실패한 비율
      feedback: 응답 시간과 응답이 아예 없었던 비율은 다른 지표입니다.
    - id: e
      text: MAC 주소가 없는 장치의 비율
      feedback: 응답 시간과 응답이 아예 없었던 비율은 다른 지표입니다.
    answer: c
  question_placements:
  - question_id: u6-l04-p05-q01
    after_paragraph: 1
- terms:
  - 왕복 시간(RTT)
  - 거리(Distance)
  - 지연(Latency)
  questions:
  - id: u6-l04-p06-q01
    kind: choice
    difficulty: easy
    prompt: 서버 A와 B의 RTT를 비교할 때 고려해야 할 것은 무엇인가요?
    choices:
    - id: a
      text: 거리뿐 아니라 실제 경로와 연결 상태도 함께 본다
      feedback: 물리적 거리 외에도 실제 경로와 회선 상태가 RTT에 영향을 줍니다.
    - id: b
      text: 물리적 거리만으로 RTT를 정확히 계산한다
      feedback: 거리는 가능성을 생각하게 하지만 결과를 단독으로 결정하지 않습니다.
    - id: c
      text: 도메인 이름의 글자 수만 본다
      feedback: 거리는 가능성을 생각하게 하지만 결과를 단독으로 결정하지 않습니다.
    - id: d
      text: 두 서버의 MAC 주소를 비교한다
      feedback: 거리는 가능성을 생각하게 하지만 결과를 단독으로 결정하지 않습니다.
    - id: e
      text: 응답이 빠른 서버는 반드시 더 가까운 나라에 있다
      feedback: 거리는 가능성을 생각하게 하지만 결과를 단독으로 결정하지 않습니다.
    answer: a
  - id: u6-l04-p06-q02
    kind: choice
    difficulty: medium
    prompt: 먼 곳의 서버가 가까운 서버보다 항상 느리다고 단정할 수 없는 이유는 무엇인가요?
    choices:
    - id: a
      text: RTT는 네트워크와 관계가 없기 때문
      feedback: 물리적 거리와 네트워크가 실제로 거치는 경로를 함께 생각하세요.
    - id: b
      text: 모든 서버는 같은 위치에 있기 때문
      feedback: 물리적 거리와 네트워크가 실제로 거치는 경로를 함께 생각하세요.
    - id: c
      text: 실제 네트워크 경로와 연결 조건이 다를 수 있기 때문
      feedback: 실제 경로와 연결 조건도 왕복 시간에 영향을 줍니다.
    - id: d
      text: Ping은 거리만 측정하기 때문
      feedback: 물리적 거리와 네트워크가 실제로 거치는 경로를 함께 생각하세요.
    - id: e
      text: 먼 서버에는 IP 주소가 없기 때문
      feedback: 물리적 거리와 네트워크가 실제로 거치는 경로를 함께 생각하세요.
    answer: c
  - id: u6-l04-p06-q03
    kind: choice
    difficulty: medium
    prompt: RTT 비교 결과만으로 확실하게 말하기 어려운 것은 무엇인가요?
    choices:
    - id: a
      text: 측정한 두 응답 시간에 차이가 있다는 것
      feedback: 측정된 사실과 원인에 관한 설명을 구별하세요.
    - id: b
      text: 주어진 수치 중 더 작은 값이 무엇인지
      feedback: 측정된 사실과 원인에 관한 설명을 구별하세요.
    - id: c
      text: 시간이 ms로 표시되었다는 것
      feedback: 측정된 사실과 원인에 관한 설명을 구별하세요.
    - id: d
      text: Ping 응답이 돌아왔다는 것
      feedback: 측정된 사실과 원인에 관한 설명을 구별하세요.
    - id: e
      text: 물리적 거리가 RTT 차이의 유일한 원인이라고 단정하는 것
      feedback: 거리만으로 RTT가 결정되지는 않아 단일 원인으로 단정하기 어렵습니다.
    answer: e
- terms:
  - 에코(Echo)
  - ICMP(Internet Control Message Protocol)
  animations:
  - file: l24-icmp-echo.svg
    title: 보낸 그대로 돌아오는 에코
    alt: 왼쪽 PC에서 A, B, C, D가 담긴 Echo Request 봉투가 서버로 가고, 서버에서 같은 내용의 Echo Reply 봉투가
      돌아옵니다. 마지막에 Ping은 프로그램, ICMP는 약속, RTT는 값이라는 세 라벨이 나타납니다.
    caption: Ping은 A B C D를 담아 보내고, 같은 내용이 돌아오는 시간을 잽니다.
  questions:
  - id: u6-l04-p07-q01
    kind: choice
    difficulty: easy
    prompt: Ping 프로그램, ICMP, RTT의 관계를 바르게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: Ping은 프로토콜, ICMP는 거리, RTT는 서버다
      feedback: 세 용어를 도구·약속·측정값으로 나누어 기억하세요.
    - id: b
      text: Ping과 ICMP는 같은 장치이고 RTT는 주소다
      feedback: 세 용어를 도구·약속·측정값으로 나누어 기억하세요.
    - id: c
      text: Ping은 프로그램, ICMP는 이용하는 프로토콜, RTT는 측정하는 값이다
      feedback: Ping은 프로그램, ICMP는 프로토콜, RTT는 왕복 시간 값입니다.
    - id: d
      text: ICMP는 프로그램, Ping은 IP 주소다
      feedback: 세 용어를 도구·약속·측정값으로 나누어 기억하세요.
    - id: e
      text: 세 용어는 모두 같은 뜻이다
      feedback: 세 용어를 도구·약속·측정값으로 나누어 기억하세요.
    answer: c
  - id: u6-l04-p07-q02
    kind: choice
    difficulty: medium
    prompt: Ping 응답이 없을 때 대상 장치가 반드시 꺼져 있다고 할 수 없는 이유는 무엇인가요?
    choices:
    - id: a
      text: Ping은 인터넷을 사용하지 않기 때문
      feedback: 측정 도구가 응답을 받지 못한 것과 장치 자체가 꺼진 것을 구분하세요.
    - id: b
      text: 대상 장치에는 항상 MAC 주소가 없기 때문
      feedback: 측정 도구가 응답을 받지 못한 것과 장치 자체가 꺼진 것을 구분하세요.
    - id: c
      text: RTT가 0이면 응답이 사라지기 때문
      feedback: 측정 도구가 응답을 받지 못한 것과 장치 자체가 꺼진 것을 구분하세요.
    - id: d
      text: DHCP는 응답을 금지하기 때문
      feedback: 측정 도구가 응답을 받지 못한 것과 장치 자체가 꺼진 것을 구분하세요.
    - id: e
      text: 방화벽이나 장치 설정이 ICMP를 막을 수 있기 때문
      feedback: 방화벽이나 장치 설정이 ICMP를 막을 수 있어 무응답만으로 장치가 꺼졌다고 단정할 수 없습니다.
    answer: e
  - id: u6-l04-p07-q03
    kind: choice
    difficulty: medium
    prompt: Ping 응답이 왔을 때도 확실히 알 수 없는 것은 무엇인가요?
    choices:
    - id: a
      text: ICMP 요청과 응답이 오갈 수 있었다는 것
      feedback: 네트워크 진단 응답과 특정 응용 프로그램의 성공을 구분하세요.
    - id: b
      text: 웹 서버 프로그램이 요청을 받았거나 파일 전체가 전달되었다는 것
      feedback: Ping 응답은 ICMP Echo 응답과 RTT를 보여 줄 뿐 웹 서비스 동작이나 파일 전달을 증명하지 않습니다.
    - id: c
      text: 왕복 시간이 얼마였는지
      feedback: 네트워크 진단 응답과 특정 응용 프로그램의 성공을 구분하세요.
    - id: d
      text: Ping 대상이 응답했다는 것
      feedback: 네트워크 진단 응답과 특정 응용 프로그램의 성공을 구분하세요.
    - id: e
      text: Echo 응답이 돌아왔다는 것
      feedback: 네트워크 진단 응답과 특정 응용 프로그램의 성공을 구분하세요.
    answer: b
  question_placements:
  - question_id: u6-l04-p07-q01
    after_paragraph: 1
animations_dir: units/04-layer3-addressing/lessons/14-ping과-rtt/assets/animations
---

## 게임에서 느끼는 지연

온라인 게임에서는 여러 사용자가 같은 공간의 상태를 일관되게 보도록 동기화해야 한다. 철수·영희·길동이 같은 게임에 참여하는데 서로 다른 상태를 본다면 원활한 진행이 어렵다. 게임에서 ‘핑’이라고 부르는 값은 서버와 데이터를 주고받을 때의 지연을 가리킨다. 네트워크에서는 목적지까지 왕복하는 시간(RTT)으로 지연을 측정할 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 온라인 게임의 지연은 양 끝에서 데이터가 오가는 시간과 처리 상황에 영향을 받는다.
- **적용하기 (Apply):** 게임에서 느껴지는 ping과 통신 왕복 응답을 구분해 생각한다.
- **찾아보기 (Lookup):** 게임의 서버 tick·보간은 네트워크 RTT와 별개로 개발 문서를 본다.

## Ping과 RTT
<!-- learn-page-id: ping-rtt -->

Ping은 프로그램의 이름이다. ICMP(Internet Control Message Protocol)를 이용해 RTT(Round Trip Time), 즉 왕복 시간을 측정한다. ICMP는 IP 통신에서 오류나 상태를 알리는 메시지를 주고받는 프로토콜이다. 앞 Lesson에서 본 TTL 만료 알림도 ICMP이고, Ping은 ICMP의 Echo 요청과 응답을 이용한다. [IPv4 헤더의 Protocol 필드](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/5/lesson/1/page/3)와 연결해 보면 ICMP가 IP 패킷 안에서 어떤 역할을 하는지 떠올릴 수 있다.

철수는 서버와 왕복하는 데 20ms, 영희는 25ms, 길동은 50ms가 걸린다고 가정하면 사용자 간에 지연 차이가 있다. 이런 차이는 게임의 화면 동기화에 중요한 문제가 된다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Ping은 ICMP를 이용해 RTT를 측정하는 프로그램이고 ICMP는 프로토콜이다.
- **적용하기 (Apply):** Ping 도구·ICMP 메시지·측정값 RTT를 각각 이름 붙인다.
- **찾아보기 (Lookup):** Echo 요청/응답 형식은 ICMP 표준에서 찾아본다.

## 왕복 시간을 비교하기

느린 사용자를 기준으로 맞출지, 다른 방법으로 동기화할지는 게임 구현의 문제다. 여기서의 핵심은 RTT로 통신의 응답 시간을 확인하고, 이를 측정하는 대표적인 도구가 Ping이라는 점이다. 따라서 ‘핑이 이상하다’는 말은 엄밀하게는 왕복 시간이 길어졌거나 응답에 문제가 있다는 상황으로 풀어 이해할 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** RTT가 큰 두 서버를 비교할 때 경로·혼잡·거리 조건을 함께 고려한다.
- **적용하기 (Apply):** 여러 번 측정한 평균과 변동을 보고 단일 응답으로 결론 내리지 않는다.
- **찾아보기 (Lookup):** 손실률과 지연 통계는 Ping 출력과 별도 도구로 확인한다.

## 네트워크 상태를 확인하는 도구

Ping은 네트워크 연결을 살펴보는 간단한 진단 도구다. 예를 들어 PC에서 기본 게이트웨이의 IP 주소로 요청을 보내면 내 컴퓨터와 가까운 네트워크 구간을 확인할 수 있다. 진단 목적에 필요한 횟수만 요청하고, 허가받지 않은 서버에 과도하게 요청을 보내지 않는다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Ping은 목적지까지 ICMP 요청과 응답이 오가는지 확인하는 진단 도구다.
- **적용하기 (Apply):** 내 게이트웨이에 제한된 횟수로 Ping을 보내 로컬 구간을 확인한다.
- **찾아보기 (Lookup):** 방화벽이 Echo를 차단하는 경우는 대상 정책과 OS 설정을 확인한다.

## 어느 구간의 문제인지 좁히기

인터넷이 안 될 때 먼저 실제 네트워크 설정에 표시된 기본 게이트웨이 주소로 Ping을 보낼 수 있다. Windows에서는 `ping -n 4 192.168.0.1`, macOS와 Linux에서는 `ping -c 4 192.168.0.1`처럼 네 번 요청한다. 주소는 내 환경의 게이트웨이 값으로 바꿔야 한다. 응답 줄의 `time`은 왕복 시간(ms), `TTL`은 돌아온 응답 패킷의 남은 전달 한도이며, 마지막 통계의 손실률은 응답하지 않은 요청의 비율이다. Ping 결과의 TTL은 왕복 시간이나 정확한 거리 값이 아니며, 앞 Lesson에서 본 IP TTL과 연결되는 필드다.

게이트웨이는 로컬 네트워크에 가까워 1ms 이내에 응답하는 예도 있다. 더 먼 인터넷 서버와 비교하면 어느 범위에서 문제가 나타나는지 좁혀 볼 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 게이트웨이 응답과 원격 서버 응답을 비교하면 장애 구간을 좁힐 수 있다.
- **적용하기 (Apply):** 첫 홉은 응답하지만 외부 주소는 실패하는 결과를 해석한다.
- **찾아보기 (Lookup):** 경로별 홉 확인은 `traceroute`/`tracert` 도움말을 참조한다.

## 거리와 지연의 관계

서버 A와 B에 각각 Ping을 보내 RTT를 비교할 수 있다. 물리적인 거리뿐 아니라 회선 상태와 전달 속도도 함께 보아야 한다고 설명한다. 예를 들어 PC와 서버 A가 서울에 있고 서버 B가 미국에 있다면, 먼 경로에서 왕복 시간이 길어질 가능성을 생각할 수 있다. 다만 거리만으로 값을 결정할 수는 없으며 실제 경로와 연결 조건을 함께 살펴야 한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** RTT는 거리뿐 아니라 경로·혼잡·장비 처리 영향을 함께 받는다.
- **적용하기 (Apply):** 가까운 서버라도 혼잡하면 멀리 있는 서버보다 느릴 수 있음을 판단한다.
- **찾아보기 (Lookup):** 시간대별 지연 기록과 네트워크 경로는 진단 로그를 찾아본다.

## ICMP Echo로 응답 확인
<!-- learn-page-id: icmp-echo -->

Ping은 ICMP Echo Request를 보내고 그에 대한 응답을 확인하는 유틸리티다. 일정 길이의 A, B, C, D 같은 데이터를 보낸 뒤 같은 내용을 되돌려 받는 에코 방식으로 왕복 시간을 측정한다. Ping 자체가 프로토콜인 것은 아니다. 프로그램은 Ping, 여기서 이용하는 프로토콜은 ICMP, 측정하는 값은 RTT라는 구분을 기억하면 된다.

Ping 응답은 ICMP 요청과 응답이 오갈 수 있었고 왕복 시간이 얼마였는지 알려 준다. 응답이 없다고 해서 대상 장치가 반드시 꺼졌다고 단정할 수는 없다. 방화벽이나 장치 설정이 ICMP를 막을 수 있기 때문이다. 반대로 응답이 왔다고 웹 서버 프로그램이 요청을 받았거나 사진의 모든 바이트가 전달됐다는 뜻도 아니다. 다음 Unit 7에서는 프로그램 사이의 통신을 맡는 TCP와 UDP를 알아보고, TCP가 수신 확인과 재전송을 제공하는 이유를 살펴본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Ping은 ICMP Echo Request를 보내고 Echo Reply를 기다린다.
- **적용하기 (Apply):** Echo data와 sequence·time 응답을 읽어 왕복을 확인한다.
- **찾아보기 (Lookup):** ICMP type/code 값은 RFC와 패킷 캡처에서 확인한다.
