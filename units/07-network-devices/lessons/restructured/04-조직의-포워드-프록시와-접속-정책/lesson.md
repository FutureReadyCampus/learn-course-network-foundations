---
id: advanced-forward-proxy
title: 조직의 포워드 프록시와 접속 정책
source_lesson_ids:
- u7-advanced-06-proxy-우회
- u7-advanced-07-proxy-보호와-감시
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-06.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-07.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/07-1.md#p391-b03
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-06.md
page_metadata:
- page_id: advanced-source-06-page-01
  illustrations:
  - file: assets/animations/u11-fwd-06-01-forward-view.svg
    title: "Proxy를 사용하는 관점"
    alt: "Proxy를 사용하는 관점: 처음엔 컴퓨터마다 직접 인터넷으로 나갈 수 있어요 → 한 중계 서버를 거치게 할 수도 있어요 → 클라이언트가 고른 중계자가 대신 전달해요 → 캐시·정책·기록은 그 위에 얹는 기능이에요"
    caption: "직접 나갈까, 한 곳을 거칠까?"
    after_paragraph: 0
  questions:
  - id: u11-l04-p01-q01
    kind: choice
    difficulty: easy
    prompt: Forward Proxy의 기본 역할은 무엇인가요?
    choices:
    - id: a
      text: 패킷 복사본만 모으는 Sensor
      feedback: 본문에서 forward Proxy는 클라이언트 측 요청을 대신 전달하는 중계자입니다. 확인해 보세요.
    - id: b
      text: 서버의 데이터베이스
      feedback: 본문에서 forward Proxy는 클라이언트 측 요청을 대신 전달하는 중계자입니다. 확인해 보세요.
    - id: c
      text: 브라우저 화면을 그리는 기능
      feedback: 본문에서 forward Proxy는 클라이언트 측 요청을 대신 전달하는 중계자입니다. 확인해 보세요.
    - id: d
      text: 클라이언트 요청을 받아 다른 서버로 전달하는 중계자
      feedback: Forward Proxy는 클라이언트 측 요청을 대신 전달하는 중계자입니다.
    - id: e
      text: 케이블 신호 증폭기
      feedback: 본문에서 forward Proxy는 클라이언트 측 요청을 대신 전달하는 중계자입니다. 확인해 보세요.
    answer: d
  - id: u11-l04-p01-q02
    kind: choice
    difficulty: medium
    prompt: Proxy의 부가 기능으로 볼 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: 캐시·접근 정책·기록·검사 기능
      feedback: 부가 기능은 Proxy의 기본 중계 위에 목적에 따라 더해집니다.
    - id: b
      text: 반드시 주소를 숨기는 기능
      feedback: 본문에서 부가 기능은 Proxy의 기본 중계 위에 목적에 따라 더해집니다. 확인해 보세요.
    - id: c
      text: 반드시 바이러스를 완벽히 차단하는 기능
      feedback: 본문에서 부가 기능은 Proxy의 기본 중계 위에 목적에 따라 더해집니다. 확인해 보세요.
    - id: d
      text: 모든 네트워크의 DNS 교체
      feedback: 본문에서 부가 기능은 Proxy의 기본 중계 위에 목적에 따라 더해집니다. 확인해 보세요.
    - id: e
      text: 모든 TLS 암호화 해제
      feedback: 본문에서 부가 기능은 Proxy의 기본 중계 위에 목적에 따라 더해집니다. 확인해 보세요.
    answer: a
- page_id: advanced-source-06-page-02
  illustrations:
  - file: assets/animations/u11-fwd-06-02-direct-vs-proxy.svg
    title: "직접 가는 길과 돌아가는 길"
    alt: "직접 가는 길과 돌아가는 길: 직접 접속하면 서버는 내 쪽 주소를 봐요 → Proxy를 지정하면 먼저 Proxy에 연결해요 → 서버에는 Proxy 쪽 주소가 보일 수 있어요 → 헤더로 원래 정보가 전달될 수도 있어요"
    caption: "서버에 보이는 주소가 달라질 수 있어요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p02-q01
    kind: choice
    difficulty: easy
    prompt: 클라이언트가 Proxy를 통해 서버에 접속할 때 서버가 관찰할 수 있는 주소는 무엇인가요?
    choices:
    - id: a
      text: 항상 사용자의 집 주소만
      feedback: 본문에서 proxy가 목적지와 별도의 연결을 맺는 구성에서는 그 연결의 상대 주소가 보일 수 있습니다. 확인해 보세요.
    - id: b
      text: 항상 Loopback 주소
      feedback: 본문에서 proxy가 목적지와 별도의 연결을 맺는 구성에서는 그 연결의 상대 주소가 보일 수 있습니다. 확인해 보세요.
    - id: c
      text: 서버의 자기 주소만
      feedback: 본문에서 proxy가 목적지와 별도의 연결을 맺는 구성에서는 그 연결의 상대 주소가 보일 수 있습니다. 확인해 보세요.
    - id: d
      text: DNS 서버의 주소만
      feedback: 본문에서 proxy가 목적지와 별도의 연결을 맺는 구성에서는 그 연결의 상대 주소가 보일 수 있습니다. 확인해 보세요.
    - id: e
      text: Proxy 쪽 연결 주소가 보일 수 있다
      feedback: Proxy가 목적지와 별도의 연결을 맺는 구성에서는 그 연결의 상대 주소가 보일 수 있습니다.
    answer: e
  - id: u11-l04-p02-q02
    kind: choice
    difficulty: medium
    prompt: Proxy를 쓴다고 익명성이 보장되지 않는 이유는 무엇인가요?
    choices:
    - id: a
      text: Proxy는 서버에 연결하지 않기 때문에
      feedback: 본문에서 출구 주소가 바뀌어도 전달 정보와 Proxy 기록은 별도로 고려해야 합니다. 확인해 보세요.
    - id: b
      text: Proxy가 원래 사용자 정보를 전달하거나 접속 기록을 남길 수 있다
      feedback: 출구 주소가 바뀌어도 전달 정보와 Proxy 기록은 별도로 고려해야 합니다.
    - id: c
      text: TCP는 IP 주소를 사용하지 않기 때문에
      feedback: 본문에서 출구 주소가 바뀌어도 전달 정보와 Proxy 기록은 별도로 고려해야 합니다. 확인해 보세요.
    - id: d
      text: 브라우저는 모든 기록을 지우기 때문에
      feedback: 본문에서 출구 주소가 바뀌어도 전달 정보와 Proxy 기록은 별도로 고려해야 합니다. 확인해 보세요.
    - id: e
      text: Proxy는 반드시 암호화하지 않기 때문에
      feedback: 본문에서 출구 주소가 바뀌어도 전달 정보와 Proxy 기록은 별도로 고려해야 합니다. 확인해 보세요.
    answer: b
- page_id: advanced-source-06-page-03
  illustrations:
  - file: assets/animations/u11-fwd-06-03-proxy-settings.svg
    title: "접속 주체를 대신하기"
    alt: "접속 주체를 대신하기: 브라우저에 Proxy 주소와 포트를 입력해요 → 브라우저는 먼저 Proxy에 요청을 맡겨요 → Proxy가 목적지와 별도 연결을 맺어요 → 프로그램별 설정은 따로 확인해요"
    caption: "브라우저가 먼저 Proxy에 말을 걸어요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p03-q01
    kind: choice
    difficulty: easy
    prompt: 브라우저가 Proxy를 설정한 뒤 먼저 연결하는 대상은 누구인가요?
    choices:
    - id: a
      text: 설정된 Proxy 서버
      feedback: 브라우저는 먼저 Proxy에 요청을 맡깁니다.
    - id: b
      text: 원래 웹 서버만
      feedback: 본문에서 브라우저는 먼저 Proxy에 요청을 맡깁니다. 확인해 보세요.
    - id: c
      text: DNS의 최상위 서버
      feedback: 본문에서 브라우저는 먼저 Proxy에 요청을 맡깁니다. 확인해 보세요.
    - id: d
      text: 스위치의 관리 화면
      feedback: 본문에서 브라우저는 먼저 Proxy에 요청을 맡깁니다. 확인해 보세요.
    - id: e
      text: 동아리 데이터베이스의 디스크
      feedback: 본문에서 브라우저는 먼저 Proxy에 요청을 맡깁니다. 확인해 보세요.
    answer: a
  - id: u11-l04-p03-q02
    kind: choice
    difficulty: medium
    prompt: 브라우저의 Proxy 설정에 대한 설명으로 옳은 것은 무엇인가요?
    choices:
    - id: a
      text: 모든 컴퓨터의 연결을 자동으로 바꾼다
      feedback: 본문에서 앱별 Proxy 지원과 네트워크 정책을 확인해야 합니다. 확인해 보세요.
    - id: b
      text: 항상 모든 프로토콜을 지원한다
      feedback: 본문에서 앱별 Proxy 지원과 네트워크 정책을 확인해야 합니다. 확인해 보세요.
    - id: c
      text: 설정을 지원하거나 따르는 프로그램의 연결에 적용된다
      feedback: 앱별 Proxy 지원과 네트워크 정책을 확인해야 합니다.
    - id: d
      text: 서버의 IP 주소를 변경한다
      feedback: 본문에서 앱별 Proxy 지원과 네트워크 정책을 확인해야 합니다. 확인해 보세요.
    - id: e
      text: Proxy가 꺼져 있어도 요청을 전달한다
      feedback: 본문에서 앱별 Proxy 지원과 네트워크 정책을 확인해야 합니다. 확인해 보세요.
    answer: c
- page_id: advanced-source-06-page-04
  illustrations:
  - file: assets/animations/u11-fwd-06-04-bypass.svg
    title: "Proxy를 통한 우회"
    alt: "Proxy를 통한 우회: 한국에서 해외 Proxy를 거쳐 접속해요 → 요청이 Proxy를 지나 사이트로 가요 → 사이트에는 Proxy의 출구 주소가 보여요 → 운영자는 기록을 볼 수 있어요"
    caption: "다른 나라의 출구로 나가 봐요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p04-q01
    kind: choice
    difficulty: easy
    prompt: Proxy를 거쳐 접속하면 목적지에서 달라질 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: 웹페이지의 언어가 항상 바뀐다
      feedback: 본문에서 목적지가 보는 연결 상대가 Proxy일 경우 출구 주소가 달라질 수 있습니다. 확인해 보세요.
    - id: b
      text: TCP 연결의 출구 주소
      feedback: 목적지가 보는 연결 상대가 Proxy일 경우 출구 주소가 달라질 수 있습니다.
    - id: c
      text: 사용자 계정의 비밀번호
      feedback: 본문에서 목적지가 보는 연결 상대가 Proxy일 경우 출구 주소가 달라질 수 있습니다. 확인해 보세요.
    - id: d
      text: 서버의 운영체제
      feedback: 본문에서 목적지가 보는 연결 상대가 Proxy일 경우 출구 주소가 달라질 수 있습니다. 확인해 보세요.
    - id: e
      text: 도메인 이름의 철자
      feedback: 본문에서 목적지가 보는 연결 상대가 Proxy일 경우 출구 주소가 달라질 수 있습니다. 확인해 보세요.
    answer: b
  - id: u11-l04-p04-q02
    kind: choice
    difficulty: medium
    prompt: 주소가 달라지는 것만으로 보장되지 않는 것은 무엇인가요?
    choices:
    - id: a
      text: Proxy가 목적지에 접속한다는 사실
      feedback: 본문에서 중계는 신원을 숨기거나 정책을 항상 우회한다고 보장하지 않습니다. 확인해 보세요.
    - id: b
      text: 경로에 중계 호스트가 있다는 점
      feedback: 본문에서 중계는 신원을 숨기거나 정책을 항상 우회한다고 보장하지 않습니다. 확인해 보세요.
    - id: c
      text: 연결 상대 주소가 다를 수 있다는 점
      feedback: 본문에서 중계는 신원을 숨기거나 정책을 항상 우회한다고 보장하지 않습니다. 확인해 보세요.
    - id: d
      text: 익명성과 모든 차단 정책의 우회
      feedback: 중계는 신원을 숨기거나 정책을 항상 우회한다고 보장하지 않습니다.
    - id: e
      text: 요청이 중계될 수 있다는 점
      feedback: 본문에서 중계는 신원을 숨기거나 정책을 항상 우회한다고 보장하지 않습니다. 확인해 보세요.
    answer: d
- page_id: advanced-source-06-page-05
  illustrations:
  - file: assets/animations/u11-fwd-06-05-speed-cost.svg
    title: "우회에 따른 속도와 비용"
    alt: "우회에 따른 속도와 비용: 직접 가면 한 번에 도착해요 → Proxy를 거치면 단계가 늘어요 → Proxy가 멈추면 모두 영향을 받아요 → 잘 두면 오히려 도움이 될 수도 있어요"
    caption: "편리하지만 거치는 길이 늘어요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p05-q01
    kind: choice
    difficulty: easy
    prompt: Proxy 경유로 생길 수 있는 성능 비용은 무엇인가요?
    choices:
    - id: a
      text: IP 주소가 없어지는 것
      feedback: 본문에서 proxy까지 갔다가 목적지로 향하므로 추가 지연이 생길 수 있습니다. 확인해 보세요.
    - id: b
      text: 서버가 멈추는 것
      feedback: 본문에서 proxy까지 갔다가 목적지로 향하므로 추가 지연이 생길 수 있습니다. 확인해 보세요.
    - id: c
      text: 경로와 처리 단계가 늘어 응답 지연이 커질 수 있다
      feedback: Proxy까지 갔다가 목적지로 향하므로 추가 지연이 생길 수 있습니다.
    - id: d
      text: 모든 패킷이 자동 압축되는 것
      feedback: 본문에서 proxy까지 갔다가 목적지로 향하므로 추가 지연이 생길 수 있습니다. 확인해 보세요.
    - id: e
      text: DNS가 필요 없어지는 것
      feedback: 본문에서 proxy까지 갔다가 목적지로 향하므로 추가 지연이 생길 수 있습니다. 확인해 보세요.
    answer: c
  - id: u11-l04-p05-q02
    kind: choice
    difficulty: medium
    prompt: Proxy에 장애가 생겼을 때의 영향은 무엇인가요?
    choices:
    - id: a
      text: 모든 인터넷 연결이 자동 복구된다
      feedback: 본문에서 중계 지점의 가용성과 대체 경로를 고려해야 합니다. 확인해 보세요.
    - id: b
      text: 목적지 서버가 항상 대신 Proxy가 된다
      feedback: 본문에서 중계 지점의 가용성과 대체 경로를 고려해야 합니다. 확인해 보세요.
    - id: c
      text: 브라우저가 자동으로 캐시를 영구 삭제한다
      feedback: 본문에서 중계 지점의 가용성과 대체 경로를 고려해야 합니다. 확인해 보세요.
    - id: d
      text: TCP가 주소를 바꾼다
      feedback: 본문에서 중계 지점의 가용성과 대체 경로를 고려해야 합니다. 확인해 보세요.
    - id: e
      text: 그 Proxy에 의존하는 연결이 영향을 받을 수 있다
      feedback: 중계 지점의 가용성과 대체 경로를 고려해야 합니다.
    answer: e
- page_id: advanced-source-06-page-06
  illustrations:
  - file: assets/animations/u11-fwd-06-06-two-sockets.svg
    title: "두 Socket 사이의 중계"
    alt: "두 Socket 사이의 중계: 클라이언트와 이야기하는 연결 하나 → 서버와 이야기하는 연결 하나 → 한쪽에서 받은 흐름을 다른 쪽에 이어 줘요 → 한쪽이 끊기면 Proxy가 처리해요"
    caption: "Proxy에는 연결이 두 개 생겨요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p06-q01
    kind: choice
    difficulty: easy
    prompt: Forward Proxy가 일반적으로 사용할 수 있는 연결 구성은 무엇인가요?
    choices:
    - id: a
      text: 클라이언트와 서버 사이의 연결 하나만 있고 Proxy는 연결되지 않는다
      feedback: 본문에서 proxy가 각 연결을 맺고 그 사이에서 데이터를 전달할 수 있습니다. 확인해 보세요.
    - id: b
      text: 두 개의 DNS 응답만
      feedback: 본문에서 proxy가 각 연결을 맺고 그 사이에서 데이터를 전달할 수 있습니다. 확인해 보세요.
    - id: c
      text: 하나의 소켓을 모든 호스트가 공유한다
      feedback: 본문에서 proxy가 각 연결을 맺고 그 사이에서 데이터를 전달할 수 있습니다. 확인해 보세요.
    - id: d
      text: 클라이언트와 Proxy, Proxy와 서버 사이의 별도 연결 두 개
      feedback: Proxy가 각 연결을 맺고 그 사이에서 데이터를 전달할 수 있습니다.
    - id: e
      text: 패킷 복사본만 있고 연결은 없다
      feedback: 본문에서 proxy가 각 연결을 맺고 그 사이에서 데이터를 전달할 수 있습니다. 확인해 보세요.
    answer: d
  - id: u11-l04-p06-q02
    kind: choice
    difficulty: medium
    prompt: Proxy 프로그램이 두 연결을 이어 줄 때 하는 일은 무엇인가요?
    choices:
    - id: a
      text: 한쪽 요청을 받아 다른 쪽으로 전달하고 응답을 되돌린다
      feedback: 소켓 연결 사이에서 요청과 응답을 중계하는 것이 기본 역할입니다.
    - id: b
      text: IP 주소를 파일로 저장한다
      feedback: 본문에서 소켓 연결 사이에서 요청과 응답을 중계하는 것이 기본 역할입니다. 확인해 보세요.
    - id: c
      text: 패킷을 반드시 모두 폐기한다
      feedback: 본문에서 소켓 연결 사이에서 요청과 응답을 중계하는 것이 기본 역할입니다. 확인해 보세요.
    - id: d
      text: 클라이언트의 화면을 렌더링한다
      feedback: 본문에서 소켓 연결 사이에서 요청과 응답을 중계하는 것이 기본 역할입니다. 확인해 보세요.
    - id: e
      text: 전원 신호를 변환한다
      feedback: 본문에서 소켓 연결 사이에서 요청과 응답을 중계하는 것이 기본 역할입니다. 확인해 보세요.
    answer: a
- page_id: advanced-source-06-page-07
  illustrations:
  - file: assets/animations/u11-fwd-06-07-bypass-summary.svg
    title: "우회 목적의 Proxy 정리"
    alt: "우회 목적의 Proxy 정리: Proxy는 요청을 받아 다른 서버에 접속해요 → 무엇을 전달·기록하는지에 따라 달라져요 → 그래서 대리 접속이 익명성을 보장하진 않아요 → 같은 구조를 여러 목적에 응용해요"
    caption: "핵심은 요청을 대신 전달한다는 점이에요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p07-q01
    kind: choice
    difficulty: easy
    prompt: Proxy 활용 사례가 달라도 공통으로 나타나는 원리는 무엇인가요?
    choices:
    - id: a
      text: 모든 트래픽을 암호 해제하는 것
      feedback: 본문에서 활용 목적과 관계없이 중계 연결이 기본 구조입니다. 확인해 보세요.
    - id: b
      text: 항상 다른 국가에서 나가는 것
      feedback: 본문에서 활용 목적과 관계없이 중계 연결이 기본 구조입니다. 확인해 보세요.
    - id: c
      text: 서버의 디스크를 복사하는 것
      feedback: 본문에서 활용 목적과 관계없이 중계 연결이 기본 구조입니다. 확인해 보세요.
    - id: d
      text: 원본 패킷만 수집하는 것
      feedback: 본문에서 활용 목적과 관계없이 중계 연결이 기본 구조입니다. 확인해 보세요.
    - id: e
      text: 요청을 받아 다른 연결로 전달하는 중계
      feedback: 활용 목적과 관계없이 중계 연결이 기본 구조입니다.
    answer: e
  - id: u11-l04-p07-q02
    kind: choice
    difficulty: medium
    prompt: Proxy의 익명성과 보안을 판단할 때 확인할 것은 무엇인가요?
    choices:
    - id: a
      text: 제품 이름만
      feedback: 본문에서 이름만으로 정보 노출이나 안전성을 단정할 수 없습니다. 확인해 보세요.
    - id: b
      text: 배치, 전달 정보, 기록 정책과 운영 주체
      feedback: 이름만으로 정보 노출이나 안전성을 단정할 수 없습니다.
    - id: c
      text: 장비 외관 색깔
      feedback: 본문에서 이름만으로 정보 노출이나 안전성을 단정할 수 없습니다. 확인해 보세요.
    - id: d
      text: 브라우저 글꼴
      feedback: 본문에서 이름만으로 정보 노출이나 안전성을 단정할 수 없습니다. 확인해 보세요.
    - id: e
      text: 도메인의 철자 수
      feedback: 본문에서 이름만으로 정보 노출이나 안전성을 단정할 수 없습니다. 확인해 보세요.
    answer: b
- page_id: advanced-source-07-page-01
  illustrations:
  - file: assets/animations/u11-fwd-07-01-limit-direct.svg
    title: "회사에서 직접 접속 제한"
    alt: "회사에서 직접 접속 제한: 공용 PC가 바로 인터넷으로 나가지 못하게 해요 → PC는 먼저 내부 Proxy로 요청해요 → Proxy가 외부 서버에 접속해요 → 관리자는 한 지점에서 정책을 적용해요"
    caption: "내부 Proxy를 거쳐서만 나가요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p08-q01
    kind: choice
    difficulty: easy
    prompt: 조직이 내부 Proxy를 두는 목적에 가까운 것은 무엇인가요?
    choices:
    - id: a
      text: 내부 사용자의 외부 접속에 정책을 적용하고 운영한다
      feedback: 내부 Proxy는 관리하는 네트워크의 접속 통제 지점이 될 수 있습니다.
    - id: b
      text: 다른 나라의 위치를 흉내 낸다
      feedback: 본문에서 내부 Proxy는 관리하는 네트워크의 접속 통제 지점이 될 수 있습니다. 확인해 보세요.
    - id: c
      text: 원본 트래픽 복사본만 수집한다
      feedback: 본문에서 내부 Proxy는 관리하는 네트워크의 접속 통제 지점이 될 수 있습니다. 확인해 보세요.
    - id: d
      text: 웹 서버 대신 신청을 승인한다
      feedback: 본문에서 내부 Proxy는 관리하는 네트워크의 접속 통제 지점이 될 수 있습니다. 확인해 보세요.
    - id: e
      text: 케이블을 무선으로 바꾼다
      feedback: 본문에서 내부 Proxy는 관리하는 네트워크의 접속 통제 지점이 될 수 있습니다. 확인해 보세요.
    answer: a
  - id: u11-l04-p08-q02
    kind: choice
    difficulty: medium
    prompt: 내부 Proxy만 사용하도록 구성하려면 무엇이 함께 필요할 수 있나요?
    choices:
    - id: a
      text: 모든 PC에서 방화벽을 끄는 것
      feedback: 본문에서 브라우저 설정과 네트워크의 허용 정책을 함께 맞춰야 우회 연결을 제한할 수 있습니다. 확인해 보세요.
    - id: b
      text: DNS 기록을 삭제하는 것
      feedback: 본문에서 브라우저 설정과 네트워크의 허용 정책을 함께 맞춰야 우회 연결을 제한할 수 있습니다. 확인해 보세요.
    - id: c
      text: 직접 외부 연결을 제한하는 네트워크 정책
      feedback: 브라우저 설정과 네트워크의 허용 정책을 함께 맞춰야 우회 연결을 제한할 수 있습니다.
    - id: d
      text: 사이트의 서버를 끄는 것
      feedback: 본문에서 브라우저 설정과 네트워크의 허용 정책을 함께 맞춰야 우회 연결을 제한할 수 있습니다. 확인해 보세요.
    - id: e
      text: Loopback을 공인 IP로 바꾸는 것
      feedback: 본문에서 브라우저 설정과 네트워크의 허용 정책을 함께 맞춰야 우회 연결을 제한할 수 있습니다. 확인해 보세요.
    answer: c
- page_id: advanced-source-07-page-02
  illustrations:
  - file: assets/animations/u11-fwd-07-02-firewall-rule.svg
    title: "Proxy를 통한 외부 접속"
    alt: "Proxy를 통한 외부 접속: 공용 PC의 직접 외부 연결은 차단해요 → Proxy가 시작한 연결만 허용해요 → 접속이 한곳으로 모여 관리하기 쉬워요 → Proxy 자체의 보안·용량도 챙겨요"
    caption: "직접 연결은 막고 Proxy만 열어요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p09-q01
    kind: choice
    difficulty: easy
    prompt: 내부 Proxy 경유 정책의 예로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 모든 연결을 항상 허용한다
      feedback: 본문에서 proxy를 정책 지점으로 만들려면 네트워크 규칙이 함께 적용되어야 합니다. 확인해 보세요.
    - id: b
      text: PC의 직접 외부 연결은 제한하고 Proxy의 허용된 외부 연결은 통과시킨다
      feedback: Proxy를 정책 지점으로 만들려면 네트워크 규칙이 함께 적용되어야 합니다.
    - id: c
      text: Proxy 서버도 외부와 연결하지 못하게 한다
      feedback: 본문에서 proxy를 정책 지점으로 만들려면 네트워크 규칙이 함께 적용되어야 합니다. 확인해 보세요.
    - id: d
      text: DNS 요청만 브라우저로 바꾼다
      feedback: 본문에서 proxy를 정책 지점으로 만들려면 네트워크 규칙이 함께 적용되어야 합니다. 확인해 보세요.
    - id: e
      text: 허용 여부와 관계없이 모든 패킷을 복사한다
      feedback: 본문에서 proxy를 정책 지점으로 만들려면 네트워크 규칙이 함께 적용되어야 합니다. 확인해 보세요.
    answer: b
  - id: u11-l04-p09-q02
    kind: choice
    difficulty: medium
    prompt: 내부 Proxy를 중앙 지점으로 만들 때 생길 수 있는 부담은 무엇인가요?
    choices:
    - id: a
      text: 포트 번호가 사라진다
      feedback: 본문에서 중앙 중계 지점의 성능과 안정성을 계획해야 합니다. 확인해 보세요.
    - id: b
      text: 웹 요청이 필요 없어 진다
      feedback: 본문에서 중앙 중계 지점의 성능과 안정성을 계획해야 합니다. 확인해 보세요.
    - id: c
      text: TLS가 자동 해제된다
      feedback: 본문에서 중앙 중계 지점의 성능과 안정성을 계획해야 합니다. 확인해 보세요.
    - id: d
      text: 장애·보안 위험과 처리 용량이 한곳에 집중될 수 있다
      feedback: 중앙 중계 지점의 성능과 안정성을 계획해야 합니다.
    - id: e
      text: 모든 PC의 NIC가 제거된다
      feedback: 본문에서 중앙 중계 지점의 성능과 안정성을 계획해야 합니다. 확인해 보세요.
    answer: d
- page_id: advanced-source-07-page-03
  illustrations:
  - file: assets/animations/u11-fwd-07-03-proxy-log.svg
    title: "중간에서 알 수 있는 것"
    alt: "중간에서 알 수 있는 것: PC의 요청이 Proxy를 거쳐 가요 → 누가 언제 어디로 갔는지 알 수 있어요 → 암호화된 내용은 설정 없이는 읽지 못해요 → 기록하기 전에 목적과 범위를 정해요"
    caption: "Proxy는 접속 기록을 남길 수 있어요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p10-q01
    kind: choice
    difficulty: easy
    prompt: 내부 Proxy가 관찰할 수 있는 정보는 무엇인가요?
    choices:
    - id: a
      text: 항상 모든 암호화 본문
      feedback: 본문에서 기록 가능 범위는 설정, 프로토콜과 TLS 처리 여부에 달려 있습니다. 확인해 보세요.
    - id: b
      text: 사용자의 화면 모든 픽셀
      feedback: 본문에서 기록 가능 범위는 설정, 프로토콜과 TLS 처리 여부에 달려 있습니다. 확인해 보세요.
    - id: c
      text: 클라이언트와 접속 시각·목적지 정보 등 설정된 범위의 기록
      feedback: 기록 가능 범위는 설정, 프로토콜과 TLS 처리 여부에 달려 있습니다.
    - id: d
      text: 네트워크에 없는 파일
      feedback: 본문에서 기록 가능 범위는 설정, 프로토콜과 TLS 처리 여부에 달려 있습니다. 확인해 보세요.
    - id: e
      text: 모든 앱의 비밀번호 평문
      feedback: 본문에서 기록 가능 범위는 설정, 프로토콜과 TLS 처리 여부에 달려 있습니다. 확인해 보세요.
    answer: c
  - id: u11-l04-p10-q02
    kind: choice
    difficulty: medium
    prompt: 접속 기록을 운영할 때 고려할 점은 무엇인가요?
    choices:
    - id: a
      text: 가능한 모든 내용을 무기한 저장한다
      feedback: 본문에서 필요한 정보만 적절히 관리하는 정책이 중요합니다. 확인해 보세요.
    - id: b
      text: Proxy 이름만 공개한다
      feedback: 본문에서 필요한 정보만 적절히 관리하는 정책이 중요합니다. 확인해 보세요.
    - id: c
      text: 기록을 누구나 보게 한다
      feedback: 본문에서 필요한 정보만 적절히 관리하는 정책이 중요합니다. 확인해 보세요.
    - id: d
      text: 기록 목적은 고려하지 않는다
      feedback: 본문에서 필요한 정보만 적절히 관리하는 정책이 중요합니다. 확인해 보세요.
    - id: e
      text: 필요한 범위, 접근 권한과 보관 기간
      feedback: 필요한 정보만 적절히 관리하는 정책이 중요합니다.
    answer: e
- page_id: advanced-source-07-page-04
  illustrations:
  - file: assets/animations/u11-fwd-07-04-file-scan.svg
    title: "악성 파일 검사"
    alt: "악성 파일 검사: 자료 사이트에서 PDF를 내려받아요 → 파일이 Proxy를 지나가요 → 구성에 따라 검사 시스템이 확인해요 → 문제가 있으면 전달하지 않아요"
    caption: "내려받는 파일을 Proxy에서 살펴봐요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p11-q01
    kind: choice
    difficulty: easy
    prompt: Proxy를 파일 검사 지점으로 활용하는 이유는 무엇인가요?
    choices:
    - id: a
      text: Proxy가 파일을 자동으로 안전하다고 보장하기 때문
      feedback: 본문에서 중계 지점이 데이터를 검사 시스템에 전달하도록 구성할 수 있습니다. 확인해 보세요.
    - id: b
      text: DNS가 파일을 분석하기 때문
      feedback: 본문에서 중계 지점이 데이터를 검사 시스템에 전달하도록 구성할 수 있습니다. 확인해 보세요.
    - id: c
      text: 브라우저가 다운로드를 중지하기 때문
      feedback: 본문에서 중계 지점이 데이터를 검사 시스템에 전달하도록 구성할 수 있습니다. 확인해 보세요.
    - id: d
      text: 다운로드 데이터가 중계 지점을 통과할 수 있기 때문
      feedback: 중계 지점이 데이터를 검사 시스템에 전달하도록 구성할 수 있습니다.
    - id: e
      text: 패킷에 파일이 실리지 않기 때문
      feedback: 본문에서 중계 지점이 데이터를 검사 시스템에 전달하도록 구성할 수 있습니다. 확인해 보세요.
    answer: d
  - id: u11-l04-p11-q02
    kind: choice
    difficulty: medium
    prompt: 다운로드 검사의 범위에 영향을 주는 것은 무엇인가요?
    choices:
    - id: a
      text: TLS 처리, 지원 파일 형식과 암호화·압축 여부
      feedback: 복호화와 형식 지원 등에 따라 검사할 수 있는 데이터가 달라집니다.
    - id: b
      text: 파일 확장자 이름만 보기
      feedback: 확장자만으로 암호화 여부나 실제 파일 내용을 모두 검사할 수 있는 것은 아닙니다.
    - id: c
      text: 다운로드 속도 수치만 보기
      feedback: 전송 속도만으로 TLS 복호화 여부나 검사할 수 있는 파일 형식이 달라지지는 않습니다.
    - id: d
      text: 접속한 도메인의 이름만 보기
      feedback: 도메인만으로 파일 내용까지 검사할 수 있는 것은 아닙니다. TLS 처리와 파일 형식 지원도 확인해야 합니다.
    - id: e
      text: 파일 크기와 접속 시각만 보기
      feedback: 파일 크기와 접속 시각은 메타데이터이며, 그 자체로 내용 검사 범위를 결정하지 않습니다.
    answer: a
- page_id: advanced-source-07-page-05
  illustrations:
  - file: assets/animations/u11-fwd-07-05-virus-wall.svg
    title: "Virus Wall과 내부 보호"
    alt: "Virus Wall과 내부 보호: 밖에서 파일 두 개가 들어와요 → 안전한 파일은 안으로 전달돼요 → 위험한 파일은 벽에서 멈춰요 → IPS와 Proxy는 역할이 겹칠 수 있어요"
    caption: "웹 통신을 중계하며 파일을 걸러요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p12-q01
    kind: choice
    difficulty: easy
    prompt: Proxy와 IPS의 처리에 관한 설명으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: IPS는 언제나 패킷만 보고 Proxy는 언제나 모든 파일을 읽는다
      feedback: 본문에서 기능을 단정하지 말고 실제 장비의 처리 경로와 설정을 확인합니다. 확인해 보세요.
    - id: b
      text: 두 장치는 항상 같은 구조로만 동작한다
      feedback: 본문에서 기능을 단정하지 말고 실제 장비의 처리 경로와 설정을 확인합니다. 확인해 보세요.
    - id: c
      text: Proxy는 보안 기능을 가질 수 없다
      feedback: 본문에서 기능을 단정하지 말고 실제 장비의 처리 경로와 설정을 확인합니다. 확인해 보세요.
    - id: d
      text: IPS는 어떤 트래픽도 차단할 수 없다
      feedback: 본문에서 기능을 단정하지 말고 실제 장비의 처리 경로와 설정을 확인합니다. 확인해 보세요.
    - id: e
      text: 서로 다른 방식이 많지만 기능은 제품·배치에 따라 겹칠 수 있다
      feedback: 기능을 단정하지 말고 실제 장비의 처리 경로와 설정을 확인합니다.
    answer: e
  - id: u11-l04-p12-q02
    kind: choice
    difficulty: medium
    prompt: Virus Wall 사례의 중심은 무엇인가요?
    choices:
    - id: a
      text: 내부 PC의 화면을 녹화하는 기능
      feedback: 본문에서 proxy와 파일 검사를 결합해 유입을 관리하는 예입니다. 확인해 보세요.
    - id: b
      text: 웹 중계 지점에서 들어오는 파일을 검사하는 구성
      feedback: Proxy와 파일 검사를 결합해 유입을 관리하는 예입니다.
    - id: c
      text: 라우터가 도메인 이름을 만드는 기능
      feedback: 본문에서 proxy와 파일 검사를 결합해 유입을 관리하는 예입니다. 확인해 보세요.
    - id: d
      text: 패킷을 복사하지 않는 Wi-Fi
      feedback: 본문에서 proxy와 파일 검사를 결합해 유입을 관리하는 예입니다. 확인해 보세요.
    - id: e
      text: 서버의 데이터베이스 복제
      feedback: 본문에서 proxy와 파일 검사를 결합해 유입을 관리하는 예입니다. 확인해 보세요.
    answer: b
- page_id: advanced-source-07-page-06
  illustrations:
  - file: assets/animations/u11-fwd-07-06-combined-box.svg
    title: "보호 기능을 함께 두기"
    alt: "보호 기능을 함께 두기: 물리적으로는 한 장비예요 → 어떤 기능은 패킷을 경로에서 검사하고 → 어떤 기능은 연결을 받아 중계해요 → 경로를 도식으로 그려 보면 정확해요"
    caption: "한 장비 안에 여러 기능이 들어가요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p13-q01
    kind: choice
    difficulty: easy
    prompt: 한 물리 장비에 여러 네트워크 기능이 함께 있을 수 있나요?
    choices:
    - id: a
      text: 그렇다. 패킷 처리와 Proxy 중계 기능이 결합될 수 있다
      feedback: 물리적 장비 수와 논리적 기능 수는 같지 않을 수 있습니다.
    - id: b
      text: 아니다. 장비는 한 기능만 가질 수 있다
      feedback: 본문에서 물리적 장비 수와 논리적 기능 수는 같지 않을 수 있습니다. 확인해 보세요.
    - id: c
      text: 아니다. 소프트웨어는 네트워크에 쓰이지 않는다
      feedback: 본문에서 물리적 장비 수와 논리적 기능 수는 같지 않을 수 있습니다. 확인해 보세요.
    - id: d
      text: 그렇다. 그러면 모든 연결이 자동 암호 해제된다
      feedback: 본문에서 물리적 장비 수와 논리적 기능 수는 같지 않을 수 있습니다. 확인해 보세요.
    - id: e
      text: 그렇다. 그러면 정책 설정이 필요 없다
      feedback: 본문에서 물리적 장비 수와 논리적 기능 수는 같지 않을 수 있습니다. 확인해 보세요.
    answer: a
  - id: u11-l04-p13-q02
    kind: choice
    difficulty: medium
    prompt: 복합 장비를 그릴 때 우선 살펴볼 것은 무엇인가요?
    choices:
    - id: a
      text: 장비 상자의 외관 색상
      feedback: 본문에서 역할과 데이터 흐름을 기능별로 확인해야 합니다. 확인해 보세요.
    - id: b
      text: 운영자의 키보드 종류
      feedback: 본문에서 역할과 데이터 흐름을 기능별로 확인해야 합니다. 확인해 보세요.
    - id: c
      text: 데이터의 진입·처리 경로와 기능별 역할
      feedback: 역할과 데이터 흐름을 기능별로 확인해야 합니다.
    - id: d
      text: 제품 화면의 글꼴
      feedback: 본문에서 역할과 데이터 흐름을 기능별로 확인해야 합니다. 확인해 보세요.
    - id: e
      text: 랜선의 길이만
      feedback: 본문에서 역할과 데이터 흐름을 기능별로 확인해야 합니다. 확인해 보세요.
    answer: c
- page_id: advanced-source-07-page-07
  illustrations:
  - file: assets/animations/u11-fwd-07-07-monitoring.svg
    title: "내부 사용자의 통신 감시"
    alt: "내부 사용자의 통신 감시: 모든 요청이 내부 Proxy로 모여요 → 운영자는 접속 흐름을 점검할 수 있어요 → 하지만 개인 검색까지 남으면 사생활 문제예요 → 목적·범위·안내를 함께 정해요"
    caption: "점검과 감시는 한 끗 차이예요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p14-q01
    kind: choice
    difficulty: easy
    prompt: 내부 Proxy에서 웹 내용을 검사하는 구성에 필요한 것은 무엇인가요?
    choices:
    - id: a
      text: 브라우저 화면 크기만
      feedback: 본문에서 hTTPS 내용을 검사하려면 적절한 승인과 별도 TLS 구성이 필요합니다. 확인해 보세요.
    - id: b
      text: 목적과 권한에 맞는 TLS 검사 설정 등 추가 운영 절차
      feedback: HTTPS 내용을 검사하려면 적절한 승인과 별도 TLS 구성이 필요합니다.
    - id: c
      text: 서버 주소를 삭제하는 것
      feedback: 본문에서 hTTPS 내용을 검사하려면 적절한 승인과 별도 TLS 구성이 필요합니다. 확인해 보세요.
    - id: d
      text: 모든 인증서를 무시하는 것
      feedback: 본문에서 hTTPS 내용을 검사하려면 적절한 승인과 별도 TLS 구성이 필요합니다. 확인해 보세요.
    - id: e
      text: 패킷 복사만 켜는 것
      feedback: 본문에서 hTTPS 내용을 검사하려면 적절한 승인과 별도 TLS 구성이 필요합니다. 확인해 보세요.
    answer: b
  - id: u11-l04-p14-q02
    kind: choice
    difficulty: medium
    prompt: Proxy 기록에 대해 옳은 설명은 무엇인가요?
    choices:
    - id: a
      text: 기록이 가능하면 무제한 감시가 정당하다
      feedback: 본문에서 기술적 가능성과 수집의 적절성은 구분해야 합니다. 확인해 보세요.
    - id: b
      text: 기록은 암호화된 모든 내용을 자동 수집한다
      feedback: 본문에서 기술적 가능성과 수집의 적절성은 구분해야 합니다. 확인해 보세요.
    - id: c
      text: Proxy는 개인정보와 관계가 없다
      feedback: 본문에서 기술적 가능성과 수집의 적절성은 구분해야 합니다. 확인해 보세요.
    - id: d
      text: 기록 지점이 생기므로 사생활과 접근 권한도 고려해야 한다
      feedback: 기술적 가능성과 수집의 적절성은 구분해야 합니다.
    - id: e
      text: 기록 보관 기간은 중요하지 않다
      feedback: 본문에서 기술적 가능성과 수집의 적절성은 구분해야 합니다. 확인해 보세요.
    answer: d
---
## Proxy를 사용하는 관점

<!-- learn-page-id: advanced-source-06-page-01 -->

동아리원이 행사 신청 페이지뿐 아니라 외부 자료 사이트에도 접속해야 합니다. 모든 컴퓨터가 제각각 인터넷으로 나가게 둘지, 한 중계 서버를 거치게 할지 운영자가 고민합니다. 클라이언트가 선택하거나 설정한 중계자가 요청을 받아 다른 서버로 전달할 때 이를 **Forward Proxy(포워드 프록시)**라고 합니다.

프록시는 단순히 케이블처럼 데이터를 통과시키는 장치가 아닙니다. 한쪽 연결의 요청을 받아 목적지에 새 연결을 만들고, 응답도 다시 요청한 쪽으로 전달할 수 있습니다. 그래서 클라이언트 관점에서 프록시는 다른 서버와의 대화를 대신해 주는 대리자입니다. 캐시, 접근 정책, 기록, 콘텐츠 검사 등은 이 기본 중계 구조 위에 추가되는 기능입니다.

이 Lesson에서는 먼저 외부 경로를 이용하는 사례를 살핀 뒤, 조직이 내부 사용자의 접속을 관리하는 경우를 봅니다. 두 사례 모두 클라이언트 측 연결을 중계하지만 운영 목적과 신뢰 관계는 다릅니다.

## 직접 가는 경로와 돌아가는 경로

<!-- learn-page-id: advanced-source-06-page-02 -->

브라우저가 신청 사이트에 직접 접속하면, 사이트는 자신과 TCP 연결을 맺은 상대의 네트워크 주소를 관찰할 수 있습니다. 다른 네트워크를 거쳐 접속하고 싶다면 클라이언트가 중간 서버를 지정할 수 있습니다. 이때 브라우저는 원래 웹 서버 대신 먼저 Proxy에 연결합니다.

목적지 서버가 네트워크 연결의 상대 주소를 보는 상황이라면, 서버에는 Proxy 쪽의 연결 주소가 보일 수 있습니다. 하지만 Proxy가 요청 헤더나 다른 식별 정보를 추가해 원래 사용자 정보를 전달할 수도 있습니다. 따라서 목적지에서 Proxy의 IP가 보일 수 있다는 사실은 사용자의 신원이나 활동이 항상 감춰진다는 보장이 아닙니다.

그림에서 보이는 IP 주소는 설명을 위한 예시입니다. 실제로 어느 주소가 보이는지는 연결 방식, Proxy 설정, 전달 헤더와 목적지의 처리에 따라 달라집니다. 다음에는 클라이언트가 Proxy 주소를 설정해 요청을 전달하는 순서를 따라가 보겠습니다.

## 접속 주체를 대신하기

<!-- learn-page-id: advanced-source-06-page-03 -->

브라우저 설정에 Proxy의 주소와 포트를 입력했다고 합시다. 사용자가 `example.net`을 열면 브라우저는 먼저 그 Proxy에 연결해 목적지와 요청을 전달합니다. Proxy는 요청을 받아 목적지 서버와 별도 연결을 맺고 응답을 다시 브라우저에 돌려줍니다.

이때 클라이언트가 접속하도록 선택한 중계 서버와, 브라우저가 원래 열려던 서버는 서로 다릅니다. 브라우저는 Proxy에 요청을 맡기고, Proxy가 그 요청의 다음 단계를 수행합니다. 회사 네트워크에서 중앙 Proxy 주소를 배포하는 것처럼, 관리자가 사용자의 브라우저 설정을 정책으로 지정하는 환경도 있습니다.

Proxy 설정만으로 모든 애플리케이션의 연결이 자동으로 Proxy를 거치는 것은 아닙니다. 프로그램별 설정과 프로토콜 지원, 네트워크 정책을 확인해야 합니다. 다음 Page에서는 중간 서버를 거쳤을 때 목적지에서 보이는 출구 주소가 달라질 수 있는 이유를 살펴봅니다.

## Proxy를 통한 우회

<!-- learn-page-id: advanced-source-06-page-04 -->

사용자가 한국에서 해외 Proxy를 거쳐 동아리 자료 사이트에 접속한다고 합시다. 사이트와 맺은 연결의 상대가 Proxy라면 사이트는 그 Proxy의 출구 주소를 관찰할 수 있습니다. Proxy의 위치나 출구가 바뀌면 목적지에서 보이는 연결 주소도 달라질 수 있습니다. 이를 다른 네트워크 경로를 이용하는 우회와 연결해 설명할 수 있습니다.

다만 주소가 달라진다고 해서 모든 차단 정책을 피할 수 있거나 익명성이 보장되는 것은 아닙니다. Proxy 운영자는 연결 시각과 요청 내용을 볼 수 있고, 목적지에 사용자를 식별할 정보를 전달할 수도 있습니다. 학교나 회사의 정책, 서비스 이용 조건에도 따라야 합니다.

따라서 Proxy는 “흔적을 없애는 장치”라기보다 “요청을 다른 호스트가 대신 전달하는 구조”로 이해해야 합니다. 다음에는 그 대리 접속에 어떤 성능 비용과 운영상 의존성이 생기는지 보겠습니다.

## 우회에 따른 속도와 비용

<!-- learn-page-id: advanced-source-06-page-05 -->

Proxy를 쓰면 클라이언트에서 목적지까지 한 번에 가는 대신, 먼저 Proxy에 도착하고 거기서 목적지로 다시 이동합니다. 경로와 처리 단계가 늘어나므로 응답 지연이 커질 수 있습니다. Proxy의 용량이 부족하거나 장애가 나면 그 Proxy에 의존하는 사용자들의 접속이 영향을 받습니다.

반대로 Proxy가 가까운 곳에 있고 응답을 캐시하거나 정책을 중앙 관리한다면 특정 운영 목적에 도움이 될 수 있습니다. 이점은 구성과 사용 방식에 달려 있습니다. Proxy를 설치했다는 사실만으로 네트워크가 항상 빨라지거나 안전해지는 것은 아닙니다.

서비스 운영자는 Proxy의 가용성, 연결 용량, 기록 정책과 장애 시 대안을 함께 살펴야 합니다. 다음에는 한 Proxy가 두 연결을 맺는다는 말을 소켓 관점에서 구체적으로 설명하겠습니다.

## 두 Socket 사이의 중계

<!-- learn-page-id: advanced-source-06-page-06 -->

Proxy는 브라우저에서 오는 연결을 받는 소켓과 목적지 서버로 나가는 별도 연결을 만드는 소켓을 사용할 수 있습니다. 쉽게 말해 프록시에는 클라이언트와 이야기하는 연결 하나, 서버와 이야기하는 연결 하나가 생깁니다. 두 연결은 같은 TCP 연결이 아니라 서로 독립적으로 맺어진 연결입니다.

클라이언트는 목적지를 요청하고 Proxy는 그 요청을 읽어 서버로 전달합니다. 서버의 응답이 오면 Proxy가 다시 클라이언트에게 보냅니다. Proxy 프로그램은 한 소켓에서 받은 데이터 흐름을 다른 소켓에 이어 주면서 정책 적용이나 애플리케이션 수준 처리를 할 수 있습니다.

이런 중계는 데이터의 전달 주체를 나누고 관찰 지점을 만들어 주지만, 양쪽 연결을 관리할 책임도 생깁니다. 서버가 응답하지 않거나 한쪽 연결이 끊기면 Proxy가 그 상태를 처리해야 합니다. 다음에는 Proxy가 우회뿐 아니라 내부 접속 정책에 쓰이는 사례로 바꾸어 보겠습니다.

## 우회 목적의 Proxy 정리

<!-- learn-page-id: advanced-source-06-page-07 -->

지금까지 본 우회 사례에서 핵심은 Proxy가 클라이언트의 요청을 받아 다른 서버에 접속한다는 것입니다. Proxy가 어느 정보를 목적지에 전달하는지, 어떤 기록을 보관하는지에 따라 서버와 운영자에게 드러나는 정보가 달라집니다. 따라서 대리 접속은 익명성을 자동으로 보장하지 않습니다.

그렇더라도 이 연결 구조는 여러 목적으로 유용합니다. 중계 서버가 클라이언트와 목적지 사이에서 요청을 전달한다는 기본 원리는 캐시, 접근 통제, 악성 파일 검사, 개발 중 트래픽 분석에 응용할 수 있습니다. 어디에 설치하고 누가 관리하는지가 목적을 크게 바꿉니다.

외부에 있는 Proxy는 다른 출구를 통해 목적지에 연결하는 데 이용될 수 있습니다. 이제 동아리 공용 PC의 외부 접속을 내부 운영자가 관리하는 상황을 보며, 내부 Proxy가 어떤 정책 지점이 되는지 살펴보겠습니다.

## 회사에서 직접 접속을 제한하기

<!-- learn-page-id: advanced-source-07-page-01 -->

동아리 공용 PC에서 외부 웹사이트에 접속할 때 악성 파일이 내려오거나 업무와 무관한 사이트에 접속하는 일이 걱정된다고 합시다. 운영자는 PC들이 인터넷으로 직접 나가지 못하게 하고, 내부 Proxy를 거쳐서만 접속하도록 설계할 수 있습니다. 여기서 Proxy는 다른 나라의 출구가 아니라 조직이 직접 관리하는 내부 중계자입니다.

PC에서 외부 서버로 가는 직접 연결은 방화벽 정책으로 제한하고, 내부 Proxy의 외부 연결은 허용합니다. 브라우저는 Proxy로 요청을 보내고 Proxy가 외부 서버에 접속합니다. 관리자는 하나의 중계 지점에서 정책 적용과 운영 기록을 수행할 수 있습니다.

모든 프로그램이 브라우저의 Proxy 설정을 따르는 것은 아니므로, 실제로는 애플리케이션 지원과 방화벽 정책을 맞춰야 합니다. 이 구조를 어떻게 운영하느냐가 다음 단계의 핵심입니다. 다음 Page에서는 직접 연결을 막고 Proxy 연결만 통과시키는 규칙을 구분해 보겠습니다.

## Proxy를 통한 외부 접속

<!-- learn-page-id: advanced-source-07-page-02 -->

내부 Proxy를 제대로 사용하려면 PC가 Proxy를 건너뛰어 외부로 직접 연결하지 못하게 하는 정책이 필요할 수 있습니다. 예를 들어 방화벽은 공용 PC의 직접 외부 연결을 차단하고, Proxy 서버에서 시작한 외부 연결은 필요한 대상과 포트에 한해 허용합니다. 사용자는 내부 Proxy를 통해 외부 웹서비스를 이용합니다.

이렇게 하면 접속이 한곳으로 모여 정책을 적용하기 쉬워질 수 있습니다. 하지만 Proxy 서버 자체의 보안, 용량, 장애 대응을 잘못 관리하면 중앙의 한 지점이 위험이나 병목이 됩니다. 직접 연결을 막았다고 모든 위협이 사라지는 것도 아닙니다.

정책은 브라우저의 설정뿐 아니라 네트워크 장비의 허용 규칙과 일치해야 합니다. 다음에는 Proxy가 중간에서 어떤 접속 정보를 알 수 있는지, 기록과 감시가 왜 별도 관리 문제인지 살펴보겠습니다.

## 중간에서 내용을 볼 수 있는 이유

<!-- learn-page-id: advanced-source-07-page-03 -->

Proxy가 요청을 받아 외부 서버와 새 연결을 맺으면, Proxy는 어느 클라이언트가 언제 어떤 목적지에 요청했는지 관찰할 수 있습니다. 운영자는 이 정보를 장애를 찾거나 보안 정책을 점검하는 데 사용할 수 있습니다. 요청의 종류와 기록 범위는 Proxy의 기능과 설정에 따라 다릅니다.

접속 주소만 기록하는 것과 요청의 구체적인 내용을 저장하는 것은 개인정보 영향이 다릅니다. 특히 HTTPS 내용은 적절한 TLS 종료·검사 구성이 없다면 Proxy도 암호화된 Payload를 그대로 읽을 수 없습니다. 기록을 활용하려면 어떤 정보가 필요한지 먼저 정하고, 접근 권한과 보관 기간을 제한해야 합니다.

기록이 가능하다는 사실은 무제한 감시가 바람직하거나 허용된다는 뜻이 아닙니다. 보안 목적과 개인의 사생활을 함께 고려해야 합니다. 다음 Page에서는 외부에서 내려받은 문서를 검사하는 과정을 보며, Proxy가 파일 검사 지점이 되는 이유를 살펴보겠습니다.

## 악성 파일 검사

<!-- learn-page-id: advanced-source-07-page-04 -->

동아리원이 외부 자료 사이트에서 신청 안내용 PDF를 내려받는다고 합시다. 다운로드가 Proxy를 지나면, 구성에 따라 파일 데이터를 검사 시스템에 전달해 악성코드가 알려진 패턴과 일치하는지 확인할 수 있습니다. 문제가 발견되면 정책에 따라 전송을 차단하거나 운영자에게 알릴 수 있습니다.

파일을 검사하려면 Proxy 또는 연동한 보안 기능이 파일 데이터를 사용할 수 있어야 합니다. HTTPS라면 TLS가 어디서 종료되는지, 파일이 지원되는 형식인지, 압축 파일이나 암호화 파일을 어떻게 처리하는지에 따라 검사 범위가 달라집니다. 모든 파일을 완벽히 판별한다고 보장할 수는 없습니다.

따라서 Proxy를 통과시킨다는 것과 모든 악성 파일을 막는다는 것은 다른 주장입니다. 검사 방식과 예외 처리, 차단 시 안내가 함께 필요합니다. 다음 Page에서는 이런 HTTP 기반 보호 구성을 Virus Wall이라고 부르는 맥락과 IPS의 패킷 분석을 비교합니다.

## Virus Wall과 내부 보호

<!-- learn-page-id: advanced-source-07-page-05 -->

외부에서 안으로 들어오는 웹 다운로드를 Proxy에서 검사하고, 위험한 파일을 내부 PC에 전달하지 않도록 하는 구성을 이 자료는 **Virus Wall** 사례로 소개합니다. 이름처럼 내부망의 파일 유입을 막는 보호 지점으로 생각할 수 있습니다. 핵심은 웹 통신을 중계하는 곳에 파일 검사 기능을 결합한다는 점입니다.

IPS도 네트워크 트래픽의 이상 패턴을 탐지하거나 차단할 수 있습니다. 많은 IPS는 경로에서 패킷과 프로토콜 정보를 처리하며, Proxy는 연결을 중계해 소켓 Stream과 애플리케이션 데이터를 다룰 수 있습니다. 그러나 제품 기능은 서로 겹칠 수 있고 실제 검사 범위는 배치와 설정에 달려 있습니다. 한쪽이 언제나 패킷만 보고 다른 쪽이 언제나 파일 전체를 읽는다고 단정하지 않습니다.

검사 지점을 만들면 보안 기능을 적용할 기회가 늘지만 처리 지연과 용량 부담도 생깁니다. 다음 Page에서는 여러 보안 기능이 한 장비에 결합될 때에도 역할과 경로를 각각 살펴야 한다는 점을 확인하겠습니다.

## 보호 기능을 함께 두기

<!-- learn-page-id: advanced-source-07-page-06 -->

실제 네트워크 장비에는 IPS와 Proxy 같은 여러 기능이 한 상자 안에 함께 들어갈 수 있습니다. 물리적으로 한 장비라고 해서 논리적 동작도 하나인 것은 아닙니다. 어떤 기능은 패킷을 경로에서 검사하고, 다른 기능은 애플리케이션 연결을 받아 중계할 수 있습니다.

동아리 공용 PC의 웹 요청을 한 장비가 받아 보안 규칙을 적용하고 외부 서버로 전달하는 구성을 생각해 보세요. 이 장비는 정책에 따라 허용·차단하는 기능과 Proxy 연결을 동시에 가질 수 있습니다. 장애 대응과 성능 계획에서는 각 기능의 처리 경로와 상태를 따로 확인해야 합니다.

장비 이름이나 외관보다 데이터가 어디로 들어오고 어떤 기능을 거쳐 나가는지 도식으로 그려 보는 것이 더 정확합니다. 다음 Page에서는 내부 Proxy의 기록 기능이 사용자 감시와 사생활 쟁점을 함께 만드는 이유를 다룹니다.

## 내부 사용자의 통신 감시

<!-- learn-page-id: advanced-source-07-page-07 -->

관리되는 공용 PC의 트래픽은 내부 Proxy에 집중되므로, 운영자는 접속 흐름과 정책 위반을 점검할 수 있습니다. 하지만 같은 지점이 직원이나 동아리원의 개인적인 검색 내용까지 기록할 수 있다면 사생활 문제가 생깁니다. 정보보호와 감시는 수집 목적과 범위, 이용자에게 알리는 방식까지 함께 다뤄야 합니다.

특히 요청 본문이나 응답 내용을 검사하는 구성은 단순히 목적지 주소만 기록하는 것보다 민감도가 높습니다. TLS 검사를 적용하려면 조직의 승인과 적절한 인증서·단말 설정 등 별도의 운영 절차가 필요합니다. 기술적인 가능성과 조직의 권한·정책은 구별해야 합니다.

여기서는 법률 결론을 내리기보다 Proxy가 기록 지점이 되는 구조와 그 책임을 살펴봅니다. 이제 시선을 공용 PC에서 운영자의 개인 PC로 옮겨, 개발·분석을 위해 로컬 Proxy를 사용하는 경우를 보겠습니다.
