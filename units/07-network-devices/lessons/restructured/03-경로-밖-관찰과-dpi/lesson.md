---
id: u7-advanced-05-out-of-path-구조와-dpi-그리고-망중립
title: 경로 밖 관찰과 DPI
source_lesson_ids:
- u7-advanced-05-out-of-path-구조와-dpi-그리고-망중립
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-05.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-05.md
page_metadata:
- page_id: advanced-source-05-page-01
  illustrations:
  - file: assets/animations/u11-oop-sensor.svg
    title: "Sensor · 경로 밖에서 관찰"
    alt: "길 옆 센서가 복사본으로 트래픽을 살피고 원래 통신은 그대로 서버에 도착하는 모습입니다."
    caption: "센서는 복사본만 보고 원래 경로는 바꾸지 않습니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p01-q01
    kind: choice
    difficulty: easy
    prompt: Out of path 센서가 주로 받는 것은 무엇인가요?
    choices:
    - id: a
      text: 원래 연결을 대신하는 소켓만
      feedback: 본문에서 센서는 별도 복사 경로로 받은 패킷을 분석합니다. 확인해 보세요.
    - id: b
      text: 서버의 소스 코드
      feedback: 본문에서 센서는 별도 복사 경로로 받은 패킷을 분석합니다. 확인해 보세요.
    - id: c
      text: 브라우저 화면 캡처
      feedback: 본문에서 센서는 별도 복사 경로로 받은 패킷을 분석합니다. 확인해 보세요.
    - id: d
      text: 복사된 패킷
      feedback: 센서는 별도 복사 경로로 받은 패킷을 분석합니다.
    - id: e
      text: DNS의 도메인 목록
      feedback: 본문에서 센서는 별도 복사 경로로 받은 패킷을 분석합니다. 확인해 보세요.
    answer: d
  - id: u11-l03-p01-q02
    kind: choice
    difficulty: medium
    prompt: Out of path의 기본 동작은 무엇인가요?
    choices:
    - id: a
      text: 원래 통신은 경로의 장치가 전달하고 센서는 복사본을 관찰한다
      feedback: 센서의 기본 역할은 경로 밖에서 복사본을 관찰하는 것입니다.
    - id: b
      text: 센서가 원래 통신을 모두 이어받는다
      feedback: 본문에서 센서의 기본 역할은 경로 밖에서 복사본을 관찰하는 것입니다. 확인해 보세요.
    - id: c
      text: 센서가 서버의 응답을 항상 차단한다
      feedback: 본문에서 센서의 기본 역할은 경로 밖에서 복사본을 관찰하는 것입니다. 확인해 보세요.
    - id: d
      text: 센서가 도메인 이름을 바꾼다
      feedback: 본문에서 센서의 기본 역할은 경로 밖에서 복사본을 관찰하는 것입니다. 확인해 보세요.
    - id: e
      text: 센서가 패킷을 만들지 않고 케이블을 바꾼다
      feedback: 본문에서 센서의 기본 역할은 경로 밖에서 복사본을 관찰하는 것입니다. 확인해 보세요.
    answer: a
- page_id: advanced-source-05-page-02
  illustrations:
  - file: assets/animations/u11-oop-mirroring.svg
    title: "Mirroring · 패킷을 복사하기"
    alt: "스위치가 원본 패킷은 서버로 보내고 같은 내용을 관찰용 포트의 분석 장치로 복사하는 모습입니다."
    caption: "포트 미러링은 복사본을 분석 장치로 보냅니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p02-q01
    kind: choice
    difficulty: easy
    prompt: 포트 미러링의 동작은 무엇인가요?
    choices:
    - id: a
      text: 원래 패킷을 반드시 삭제한다
      feedback: 본문에서 미러링은 지정한 트래픽의 복사본을 관찰 포트로 전달합니다. 확인해 보세요.
    - id: b
      text: TCP 연결을 암호화한다
      feedback: 본문에서 미러링은 지정한 트래픽의 복사본을 관찰 포트로 전달합니다. 확인해 보세요.
    - id: c
      text: 서버의 포트 번호를 자동 변경한다
      feedback: 본문에서 미러링은 지정한 트래픽의 복사본을 관찰 포트로 전달합니다. 확인해 보세요.
    - id: d
      text: 브라우저 요청을 새로 만든다
      feedback: 본문에서 미러링은 지정한 트래픽의 복사본을 관찰 포트로 전달합니다. 확인해 보세요.
    - id: e
      text: 원래 패킷을 전달하면서 관찰 포트에 복사본을 보낸다
      feedback: 미러링은 지정한 트래픽의 복사본을 관찰 포트로 전달합니다.
    answer: e
  - id: u11-l03-p02-q02
    kind: choice
    difficulty: medium
    prompt: 미러링 구성에서 고려할 요소는 무엇인가요?
    choices:
    - id: a
      text: 모든 VLAN의 복사본을 한 포트로 보내도 포트 용량은 늘지 않는다
      feedback: 복사본이 한곳에 모이면 출력 포트와 센서의 용량이 부족해질 수 있어요.
    - id: b
      text: 복사할 트래픽의 양과 출력 포트·장비의 처리 용량
      feedback: 복사본이 많으면 장비와 관찰 포트의 용량이 부족해질 수 있습니다.
    - id: c
      text: 복사 트래픽이 많아도 센서 NIC의 속도는 고려하지 않는다
      feedback: 복사본이 한곳에 모이면 출력 포트와 센서의 용량이 부족해질 수 있어요.
    - id: d
      text: 도메인 이름의 길이로 미러링 대상 포트를 정한다
      feedback: 복사본이 한곳에 모이면 출력 포트와 센서의 용량이 부족해질 수 있어요.
    - id: e
      text: 미러링은 원본 경로를 바꾸므로 경로 처리량만 확인한다
      feedback: 복사본이 한곳에 모이면 출력 포트와 센서의 용량이 부족해질 수 있어요.
    answer: b
- page_id: advanced-source-05-page-03
  illustrations:
  - file: assets/animations/u11-oop-read-only.svg
    title: "Read only와 차단의 차이"
    alt: "센서가 이상한 패킷을 발견해도 원본은 서버로 가고, 차단은 경로 안 Inline 장치가 맡는 모습입니다."
    caption: "발견하는 일과 차단하는 일은 다릅니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p03-q01
    kind: choice
    difficulty: easy
    prompt: Read only 관찰의 예로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 복사된 패킷을 Wireshark로 읽어 기록한다
      feedback: 복사본 관찰은 원래 통신의 통과나 차단과 구분됩니다.
    - id: b
      text: 복사본을 읽고 원본을 반드시 버린다
      feedback: 본문에서 복사본 관찰은 원래 통신의 통과나 차단과 구분됩니다. 확인해 보세요.
    - id: c
      text: 센서가 서버 대신 신청을 승인한다
      feedback: 본문에서 복사본 관찰은 원래 통신의 통과나 차단과 구분됩니다. 확인해 보세요.
    - id: d
      text: 브라우저가 라우터 역할을 한다
      feedback: 본문에서 복사본 관찰은 원래 통신의 통과나 차단과 구분됩니다. 확인해 보세요.
    - id: e
      text: 센서가 DNS 응답을 편집한다
      feedback: 본문에서 복사본 관찰은 원래 통신의 통과나 차단과 구분됩니다. 확인해 보세요.
    answer: a
  - id: u11-l03-p03-q02
    kind: choice
    difficulty: medium
    prompt: 센서가 복사본에서 이상 징후를 찾으면 원본 패킷은 어떻게 되나요?
    choices:
    - id: a
      text: 센서가 복사본을 보는 즉시 원본도 항상 삭제된다
      feedback: 본문에서 경로 밖 관찰만으로 원본을 자동 차단하지는 않습니다. 확인해 보세요.
    - id: b
      text: 원래 패킷이 브라우저 화면으로 바뀐다
      feedback: 본문에서 경로 밖 관찰만으로 원본을 자동 차단하지는 않습니다. 확인해 보세요.
    - id: c
      text: 기본적으로 원래 경로의 전달이 계속되고, 차단에는 추가 대응이 필요하다
      feedback: 경로 밖 관찰만으로 원본을 자동 차단하지는 않습니다.
    - id: d
      text: 센서가 자동으로 서버를 종료한다
      feedback: 본문에서 경로 밖 관찰만으로 원본을 자동 차단하지는 않습니다. 확인해 보세요.
    - id: e
      text: 센서가 항상 DNS를 우회한다
      feedback: 본문에서 경로 밖 관찰만으로 원본을 자동 차단하지는 않습니다. 확인해 보세요.
    answer: c
- page_id: advanced-source-05-page-04
  illustrations:
  - file: assets/animations/u11-oop-intervene.svg
    title: "경로 밖에서 접속에 개입하기"
    alt: "센서가 연결을 감지해 이용자에게 별도 경고 응답을 보내는 능동 개입을 보여 줍니다."
    caption: "관찰 외에 별도 응답을 보내는 것은 능동 개입입니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p04-q01
    kind: choice
    difficulty: easy
    prompt: 경로 밖 센서가 원래 패킷을 직접 Drop할 수 있나요?
    choices:
    - id: a
      text: 항상 가능하다
      feedback: 본문에서 원본 전달 경로 밖에 있으므로 별도 개입 수단이 필요합니다. 확인해 보세요.
    - id: b
      text: 기본 Out of path 구조만으로는 원래 패킷을 직접 버릴 수 없다
      feedback: 원본 전달 경로 밖에 있으므로 별도 개입 수단이 필요합니다.
    - id: c
      text: DNS가 대신 버리므로 가능하다
      feedback: 본문에서 원본 전달 경로 밖에 있으므로 별도 개입 수단이 필요합니다. 확인해 보세요.
    - id: d
      text: 미러링 설정만 있으면 원본을 차단한다
      feedback: 본문에서 원본 전달 경로 밖에 있으므로 별도 개입 수단이 필요합니다. 확인해 보세요.
    - id: e
      text: 센서는 패킷 복사를 받지 않는다
      feedback: 본문에서 원본 전달 경로 밖에 있으므로 별도 개입 수단이 필요합니다. 확인해 보세요.
    answer: b
  - id: u11-l03-p04-q02
    kind: choice
    difficulty: medium
    prompt: 센서가 접속에 능동 개입하는 설명으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 복사본을 받으면 자동으로 웹사이트가 바뀐다
      feedback: 본문에서 능동 개입은 복사본 관찰과 구별되는 추가 동작입니다. 확인해 보세요.
    - id: b
      text: 모든 TCP 연결을 같은 방식으로 차단한다
      feedback: 본문에서 능동 개입은 복사본 관찰과 구별되는 추가 동작입니다. 확인해 보세요.
    - id: c
      text: 센서가 Inline 장치와 항상 동일하다
      feedback: 본문에서 능동 개입은 복사본 관찰과 구별되는 추가 동작입니다. 확인해 보세요.
    - id: d
      text: 관찰 외에 별도 응답을 보내는 조건과 방식이 추가된다
      feedback: 능동 개입은 복사본 관찰과 구별되는 추가 동작입니다.
    - id: e
      text: 포트 미러링이 곧 TLS 복호화다
      feedback: 본문에서 능동 개입은 복사본 관찰과 구별되는 추가 동작입니다. 확인해 보세요.
    answer: d
- page_id: advanced-source-05-page-05
  illustrations:
  - file: assets/animations/u11-oop-tcp-reply.svg
    title: "TCP 응답을 이용한 개입"
    alt: "센서가 TCP 연결의 한쪽인 척 패킷을 보내도 번호가 맞지 않으면 단말이 무시할 수 있음을 보여 줍니다."
    caption: "TCP 응답 개입은 연결 상태가 맞아야 통합니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p05-q01
    kind: choice
    difficulty: easy
    prompt: TCP 연결에 별도 응답을 보내 개입하려면 무엇이 중요한가요?
    choices:
    - id: a
      text: 응답의 목적지 주소를 몰라도 된다
      feedback: 본문에서 tCP 상태와 단말의 수용 여부 때문에 별도 응답이 항상 성공하는 것은 아닙니다. 확인해 보세요.
    - id: b
      text: 모든 패킷에 같은 순서 번호를 쓴다
      feedback: 본문에서 tCP 상태와 단말의 수용 여부 때문에 별도 응답이 항상 성공하는 것은 아닙니다. 확인해 보세요.
    - id: c
      text: 연결 상태를 파악하고 단말이 받아들일 응답을 보내야 한다
      feedback: TCP 상태와 단말의 수용 여부 때문에 별도 응답이 항상 성공하는 것은 아닙니다.
    - id: d
      text: 센서는 원본 경로와 항상 같은 장치다
      feedback: 본문에서 tCP 상태와 단말의 수용 여부 때문에 별도 응답이 항상 성공하는 것은 아닙니다. 확인해 보세요.
    - id: e
      text: TCP는 연결 상태를 확인하지 않는다
      feedback: 본문에서 tCP 상태와 단말의 수용 여부 때문에 별도 응답이 항상 성공하는 것은 아닙니다. 확인해 보세요.
    answer: c
  - id: u11-l03-p05-q02
    kind: choice
    difficulty: medium
    prompt: 능동 개입과 단순 관찰의 차이는 무엇인가요?
    choices:
    - id: a
      text: 둘은 모두 원본을 차단한다
      feedback: 본문에서 관찰과 연결에 영향을 주는 대응 기능을 구분해야 합니다. 확인해 보세요.
    - id: b
      text: 관찰은 항상 서버가 되며 개입은 센서가 된다
      feedback: 본문에서 관찰과 연결에 영향을 주는 대응 기능을 구분해야 합니다. 확인해 보세요.
    - id: c
      text: 관찰은 DPI이고 개입은 DNS다
      feedback: 본문에서 관찰과 연결에 영향을 주는 대응 기능을 구분해야 합니다. 확인해 보세요.
    - id: d
      text: 둘은 처리 위치가 같은 뜻이다
      feedback: 본문에서 관찰과 연결에 영향을 주는 대응 기능을 구분해야 합니다. 확인해 보세요.
    - id: e
      text: 능동 개입은 복사본을 읽는 데서 더 나아가 별도 동작으로 연결에 영향을 준다
      feedback: 관찰과 연결에 영향을 주는 대응 기능을 구분해야 합니다.
    answer: e
  - id: u11-l03-p05-q03
    kind: choice
    difficulty: medium
    prompt: Out of path 센서의 능동 개입이 Inline 정책 적용보다 덜 직접적인 이유는 무엇인가요?
    choices:
    - id: a
      text: 센서는 원본 통신을 항상 먼저 차단한 다음 복사본을 만든다
      feedback: Out of path는 원본 경로 밖에서 복사본을 관찰하는 구조이며, 원본을 직접 차단하는 것이 기본은 아닙니다.
    - id: b
      text: 경로 밖 센서는 연결 상태에 맞는 별도 응답을 보내고, 단말이 받아들여야 한다
      feedback: 경로 밖 센서는 원본 연결을 직접 이어받지 않으므로, 연결 상태와 단말의 수용 여부가 중요합니다.
    - id: c
      text: Inline 장치는 복사본만 보고 연결에 별도 응답을 보낸다
      feedback: 본문은 Inline 정책 적용과 경로 밖 센서의 별도 응답을 서로 다른 방식으로 설명합니다.
    - id: d
      text: TCP 연결에는 주소나 상태 정보가 사용되지 않는다
      feedback: 본문은 TCP의 연결 상태와 주소를 알아야 단말이 받아들일 응답을 보낼 수 있다고 설명합니다.
    - id: e
      text: 두 구조는 모두 원본 경로에 직접 들어가야만 동작한다
      feedback: Out of path 센서는 원래 경로 밖에 있으며, 별도 응답을 보내는 방식으로 개입할 수 있습니다.
    answer: b
- page_id: advanced-source-05-page-06
  illustrations:
  - file: assets/animations/u11-oop-dpi.svg
    title: "DPI · Payload까지 살펴보기"
    alt: "패킷을 송장(헤더)과 내용물(Payload)로 나누어 헤더만 보는 SPI와 안쪽까지 보는 DPI를 비교합니다."
    caption: "DPI는 헤더를 넘어 Payload까지 검사합니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p06-q01
    kind: choice
    difficulty: easy
    prompt: DPI는 어떤 검사를 가리키나요?
    choices:
    - id: a
      text: 케이블의 전압만 재는 검사
      feedback: 본문에서 dPI는 상위 데이터까지 살펴보는 깊은 패킷 검사를 뜻합니다. 확인해 보세요.
    - id: b
      text: 원본 패킷을 복사하지 않는 기능
      feedback: 본문에서 dPI는 상위 데이터까지 살펴보는 깊은 패킷 검사를 뜻합니다. 확인해 보세요.
    - id: c
      text: 도메인 이름을 IP 주소로 바꾸는 기능
      feedback: 본문에서 dPI는 상위 데이터까지 살펴보는 깊은 패킷 검사를 뜻합니다. 확인해 보세요.
    - id: d
      text: 기본 헤더를 넘어 상위 프로토콜이나 Payload까지 분석하는 방식
      feedback: DPI는 상위 데이터까지 살펴보는 깊은 패킷 검사를 뜻합니다.
    - id: e
      text: 서버의 디스크 상태만 보는 검사
      feedback: 본문에서 dPI는 상위 데이터까지 살펴보는 깊은 패킷 검사를 뜻합니다. 확인해 보세요.
    answer: d
  - id: u11-l03-p06-q02
    kind: choice
    difficulty: medium
    prompt: TLS로 암호화된 웹 내용에 대한 설명으로 옳은 것은 무엇인가요?
    choices:
    - id: a
      text: 복호화할 구성이나 권한이 없으면 복사 패킷만으로 평문 내용을 읽을 수 없다
      feedback: 암호화된 Payload와 관찰 가능한 헤더 정보를 구별해야 합니다.
    - id: b
      text: 모든 DPI 장치가 내용을 자동 복호화한다
      feedback: 본문에서 암호화된 Payload와 관찰 가능한 헤더 정보를 구별해야 합니다. 확인해 보세요.
    - id: c
      text: 암호화되어도 Payload는 항상 공개된다
      feedback: 본문에서 암호화된 Payload와 관찰 가능한 헤더 정보를 구별해야 합니다. 확인해 보세요.
    - id: d
      text: TLS는 IP 헤더를 숨긴다
      feedback: 본문에서 암호화된 Payload와 관찰 가능한 헤더 정보를 구별해야 합니다. 확인해 보세요.
    - id: e
      text: 스위치 미러링이 곧 암호 해제다
      feedback: 본문에서 암호화된 Payload와 관찰 가능한 헤더 정보를 구별해야 합니다. 확인해 보세요.
    answer: a
- page_id: advanced-source-05-page-07
  illustrations:
  - file: assets/animations/u11-oop-privacy.svg
    title: "망중립과 사생활의 문제"
    alt: "통신 내용을 열어 보면 악성 단서와 사적 정보가 함께 보이므로 목적·범위·기간·권한을 정해야 한다는 그림입니다."
    caption: "검사 범위는 목적과 권한에 맞춰 정해야 합니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p07-q01
    kind: choice
    difficulty: easy
    prompt: 망중립성에서 함께 살펴볼 쟁점은 무엇인가요?
    choices:
    - id: a
      text: 특정 서비스의 응답 시간이 다른 서비스보다 짧은지
      feedback: 응답 시간은 성능 비교에 해당하며, 본문은 특정 트래픽을 차별·제한하는 기준과 영향을 묻습니다.
    - id: b
      text: 트래픽이 유선이나 무선 중 어떤 매체를 통과하는지
      feedback: 전송 매체만으로 망중립성 쟁점을 설명할 수는 없습니다. 본문은 트래픽을 차별하거나 제한하는 기준을 다룹니다.
    - id: c
      text: 센서가 전용 장비인지 범용 컴퓨터인지
      feedback: 장비 구현 방식과 트래픽에 대한 차별·제한의 쟁점은 서로 다른 질문입니다.
    - id: d
      text: 패킷이 어느 저장 장치에 기록되는지
      feedback: 저장 위치는 운영 설계의 문제이고, 망중립성은 트래픽을 어떤 기준으로 차별·제한하는지 살핍니다.
    - id: e
      text: 특정 서비스·콘텐츠 트래픽을 어떤 기준으로 차별하거나 제한하는가
      feedback: 망중립성은 트래픽에 대한 차별·제한의 기준과 영향을 따집니다.
    answer: e
  - id: u11-l03-p07-q02
    kind: choice
    difficulty: medium
    prompt: 기술적으로 내용을 검사할 수 있다는 사실은 무엇을 보장하나요?
    choices:
    - id: a
      text: 모든 데이터가 안전하다는 뜻이다
      feedback: 본문에서 가능성과 적절성은 다른 질문이며 목적·권한·절차를 따져야 합니다. 확인해 보세요.
    - id: b
      text: 수집과 저장이 언제나 허용된다는 뜻은 아니다
      feedback: 가능성과 적절성은 다른 질문이며 목적·권한·절차를 따져야 합니다.
    - id: c
      text: 법과 정책 검토가 필요 없다는 뜻이다
      feedback: 본문에서 가능성과 적절성은 다른 질문이며 목적·권한·절차를 따져야 합니다. 확인해 보세요.
    - id: d
      text: 개인정보가 포함되지 않는다는 뜻이다
      feedback: 본문에서 가능성과 적절성은 다른 질문이며 목적·권한·절차를 따져야 합니다. 확인해 보세요.
    - id: e
      text: 검사 범위가 자동으로 최소화된다는 뜻이다
      feedback: 본문에서 가능성과 적절성은 다른 질문이며 목적·권한·절차를 따져야 합니다. 확인해 보세요.
    answer: b
  - id: u11-l03-p07-q03
    kind: choice
    difficulty: medium
    prompt: 센서가 이용자 데이터를 관찰하도록 설계할 때, 운영자가 미리 정해야 할 항목은 무엇인가요?
    choices:
    - id: a
      text: 모든 트래픽을 가능한 한 오래 보관하는 기준
      feedback: 본문은 필요한 범위와 보관 기간을 정하고 접근 권한을 관리하도록 설명합니다.
    - id: b
      text: 특정 서비스만 검사하고 그 이유는 기록하지 않는 방식
      feedback: 무엇을 왜 검사하고 누구에게 어떤 영향을 주는지 함께 따져야 합니다.
    - id: c
      text: 법률 검토 없이 기술적으로 가능한 데이터 전부를 저장하는 방식
      feedback: 기술적으로 식별할 수 있다는 사실만으로 수집·저장이 정당화되지는 않습니다.
    - id: d
      text: 목적, 필요한 데이터 범위, 보관 기간과 접근 권한
      feedback: 센서 설계에서는 목적과 필요한 범위, 보관 기간, 접근 권한을 함께 정해야 합니다.
    - id: e
      text: 패킷 속도만 정하고 기록 내용과 접근자는 따로 보지 않는 방식
      feedback: 성능과 별개로 수집할 데이터의 범위와 보관·접근 조건도 정해야 합니다.
    answer: d
- page_id: advanced-source-05-page-08
  illustrations:
  - file: assets/animations/u11-oop-dropped.svg
    title: "놓치지 않고 수집하는 문제"
    alt: "몰리는 패킷을 센서가 못 따라가면 일부가 누락될 수 있음을 보여 줍니다."
    caption: "복사본이 전부 수집된다고 보장되지는 않습니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p08-q01
    kind: choice
    difficulty: easy
    prompt: 센서가 복사 패킷 일부를 놓칠 수 있는 이유는 무엇인가요?
    choices:
    - id: a
      text: 복사 지점이나 수신 센서의 처리 용량이 트래픽을 감당하지 못할 수 있다
      feedback: 복사 포트, NIC, 메모리와 프로그램 처리 용량을 점검해야 합니다.
    - id: b
      text: 패킷에는 주소가 없기 때문에
      feedback: 본문에서 복사 포트, NIC, 메모리와 프로그램 처리 용량을 점검해야 합니다. 확인해 보세요.
    - id: c
      text: 패킷은 항상 한 번만 전달되기 때문에
      feedback: 본문에서 복사 포트, NIC, 메모리와 프로그램 처리 용량을 점검해야 합니다. 확인해 보세요.
    - id: d
      text: 브라우저가 미러링을 끄기 때문에
      feedback: 본문에서 복사 포트, NIC, 메모리와 프로그램 처리 용량을 점검해야 합니다. 확인해 보세요.
    - id: e
      text: DNS가 센서에 응답하지 않기 때문에
      feedback: 본문에서 복사 포트, NIC, 메모리와 프로그램 처리 용량을 점검해야 합니다. 확인해 보세요.
    answer: a
  - id: u11-l03-p08-q02
    kind: choice
    difficulty: medium
    prompt: 모든 패킷을 빠짐없이 관찰해야 하는지 어떻게 정하나요?
    choices:
    - id: a
      text: 모든 용도에 동일한 누락률을 적용한다
      feedback: 본문에서 허용 가능한 누락률은 관찰의 목적과 요구 정확도에 따라 달라집니다. 확인해 보세요.
    - id: b
      text: 장치 가격만 보고 정한다
      feedback: 본문에서 허용 가능한 누락률은 관찰의 목적과 요구 정확도에 따라 달라집니다. 확인해 보세요.
    - id: c
      text: 접속 추세 분석인지 사고의 개별 패킷 추적인지 용도에 따라 정한다
      feedback: 허용 가능한 누락률은 관찰의 목적과 요구 정확도에 따라 달라집니다.
    - id: d
      text: 패킷 크기만 보고 정한다
      feedback: 본문에서 허용 가능한 누락률은 관찰의 목적과 요구 정확도에 따라 달라집니다. 확인해 보세요.
    - id: e
      text: 항상 5%를 놓쳐도 충분하다
      feedback: 본문에서 허용 가능한 누락률은 관찰의 목적과 요구 정확도에 따라 달라집니다. 확인해 보세요.
    answer: c
  - id: u11-l03-p08-q03
    kind: choice
    difficulty: medium
    prompt: 사고 분석에서 개별 패킷까지 확인해야 하는데 복사 지점의 출력 용량이 부족하다면, 어떤 판단이 적절한가요?
    choices:
    - id: a
      text: 미러링 설정이 켜져 있으니 기록이 완전하다고 간주한다
      feedback: 미러링을 켠 것만으로 모든 복사본이 센서에 도착한다고 보장되지는 않습니다.
    - id: b
      text: 누락된 기록은 원본 통신에도 반드시 같은 손실이 있었다고 뜻한다
      feedback: 관찰 복사본의 누락은 수집 문제일 수 있어 원본 통신에서 같은 손실이 있었다고 단정할 수 없어요.
    - id: c
      text: 추세 분석과 사고 추적은 요구 정확도가 같다고 본다
      feedback: 본문은 대략적인 추세와 개별 패킷 추적에 서로 다른 누락 허용 수준이 필요하다고 설명합니다.
    - id: d
      text: 센서의 저장 공간만 늘리고 입력 포트와 NIC는 확인하지 않는다
      feedback: 누락은 저장 전 복사 지점이나 센서 NIC·메모리·캡처 프로그램에서도 생길 수 있습니다.
    - id: e
      text: 복사 경로·센서 용량과 드롭을 확인한 뒤 기록을 해석한다
      feedback: 복사 포트와 센서가 속도를 감당하는지, 드롭 카운터 등에 누락이 있는지 점검해야 합니다.
    answer: e
- page_id: advanced-source-05-page-09
  illustrations:
  - file: assets/animations/u11-oop-storage.svg
    title: "저장과 분석의 부하"
    alt: "받기, 분석, 저장 세 단계 중 어느 단계든 느리면 누락이 생기고 1Gbps는 초당 약 125MB라는 점을 보여 줍니다."
    caption: "수집·분석·저장 전체 처리 용량을 봐야 합니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p09-q01
    kind: choice
    difficulty: easy
    prompt: 1Gbps 입력을 저장할 때의 대략적인 초당 데이터량은 얼마인가요?
    choices:
    - id: a
      text: 약 1.25MB
      feedback: 본문에서 비트 단위 속도를 바이트로 바꾸려면 8로 나눕니다. 실제 저장량은 오버헤드에 따라 달라집니다. 확인해 보세요.
    - id: b
      text: 약 125MB
      feedback: 비트 단위 속도를 바이트로 바꾸려면 8로 나눕니다. 실제 저장량은 오버헤드에 따라 달라집니다.
    - id: c
      text: 약 8MB
      feedback: 본문에서 비트 단위 속도를 바이트로 바꾸려면 8로 나눕니다. 실제 저장량은 오버헤드에 따라 달라집니다. 확인해 보세요.
    - id: d
      text: 약 1GB
      feedback: 본문에서 비트 단위 속도를 바이트로 바꾸려면 8로 나눕니다. 실제 저장량은 오버헤드에 따라 달라집니다. 확인해 보세요.
    - id: e
      text: 약 125KB
      feedback: 본문에서 비트 단위 속도를 바이트로 바꾸려면 8로 나눕니다. 실제 저장량은 오버헤드에 따라 달라집니다. 확인해 보세요.
    answer: b
  - id: u11-l03-p09-q02
    kind: choice
    difficulty: medium
    prompt: 센서가 충분히 빠른 네트워크 카드가 있어도 데이터가 누락될 수 있는 이유는 무엇인가요?
    choices:
    - id: a
      text: 센서는 저장할 수 없기 때문에
      feedback: 본문에서 수집 이후의 분석과 기록 단계도 병목이 될 수 있습니다. 확인해 보세요.
    - id: b
      text: TCP는 패킷을 암호화하기 때문에
      feedback: 본문에서 수집 이후의 분석과 기록 단계도 병목이 될 수 있습니다. 확인해 보세요.
    - id: c
      text: 미러링은 복사본을 만들지 않기 때문에
      feedback: 본문에서 수집 이후의 분석과 기록 단계도 병목이 될 수 있습니다. 확인해 보세요.
    - id: d
      text: 메모리·CPU·저장 장치가 입력 속도를 따라가지 못할 수 있다
      feedback: 수집 이후의 분석과 기록 단계도 병목이 될 수 있습니다.
    - id: e
      text: IP 헤더가 디스크를 막기 때문에
      feedback: 본문에서 수집 이후의 분석과 기록 단계도 병목이 될 수 있습니다. 확인해 보세요.
    answer: d
- page_id: advanced-source-05-page-10
  illustrations:
  - file: assets/animations/u11-oop-compare.svg
    title: "Inline과 Out of path 비교"
    alt: "Inline은 실시간 차단에, Out of path는 영향 없는 사후 분석에 알맞다는 비교입니다."
    caption: "목적에 따라 알맞은 구조가 다릅니다."
    after_paragraph: 0
  questions:
  - id: u11-l03-p10-q01
    kind: choice
    difficulty: easy
    prompt: 원본 통신에 즉시 전달·차단 영향을 주는 배치는 무엇인가요?
    choices:
    - id: a
      text: Out of path
      feedback: 본문에서 inline 장치는 원래 패킷이 지나는 경로 안에서 처리합니다. 확인해 보세요.
    - id: b
      text: Tapping Point만
      feedback: 본문에서 inline 장치는 원래 패킷이 지나는 경로 안에서 처리합니다. 확인해 보세요.
    - id: c
      text: Inline
      feedback: Inline 장치는 원래 패킷이 지나는 경로 안에서 처리합니다.
    - id: d
      text: Read only
      feedback: 본문에서 inline 장치는 원래 패킷이 지나는 경로 안에서 처리합니다. 확인해 보세요.
    - id: e
      text: Wireshark만
      feedback: 본문에서 inline 장치는 원래 패킷이 지나는 경로 안에서 처리합니다. 확인해 보세요.
    answer: c
  - id: u11-l03-p10-q02
    kind: choice
    difficulty: medium
    prompt: 두 구조를 선택할 때 함께 고려할 기준으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 장치의 설치 위치와 제조 방식만
      feedback: 설치 위치와 구현 방식만으로는 통신 개입 필요성, 누락 허용도와 개인정보 보호 요구를 판단할 수 없습니다.
    - id: b
      text: 필요한 로그 형식과 운영체제 종류만
      feedback: 로그 형식과 운영체제 외에도 기능, 처리량, 정확도와 데이터 보호를 함께 고려해야 합니다.
    - id: c
      text: 관찰 장치의 구매 가격만
      feedback: 비용은 고려 요소지만, 구조가 목적에 맞는지와 처리 성능·개인정보 보호도 살펴야 합니다.
    - id: d
      text: 운영자의 선호와 제품 이름만
      feedback: 제품 이름과 선호만으로 구조의 개입 방식, 누락 허용도와 데이터 보호 수준을 판단할 수 없습니다.
    - id: e
      text: 통신 개입 필요성, 누락 허용도, 처리량과 개인정보 보호
      feedback: 구조 선택은 기능, 성능, 정확도와 데이터 보호를 함께 고려해야 합니다.
    answer: e
---

## Sensor · 경로 밖에서 관찰

<!-- learn-page-id: advanced-source-05-page-01 -->

동아리 신청 서버가 느려졌다는 연락이 왔습니다. 운영자는 신청자가 실제로 얼마나 접속하는지 알고 싶지만, 모든 요청이 지나가는 장치를 바꾸면 서비스에 영향을 줄까 걱정됩니다. 원래 통신은 경로에서 그대로 이어 가고, 별도 장치가 복사본을 받는 배치를 **Out of path(경로 밖)**라고 합니다.

복사본을 받아 관찰하는 장치를 Sensor(센서)라고 부릅니다. 센서는 트래픽의 양이나 패턴을 살피고 이상 징후를 찾는 데 활용할 수 있습니다. 다만 분석하려면 먼저 관찰할 패킷이 센서까지 전달되어야 합니다. 스위치의 포트 미러링이나 별도 TAP 장치가 이 복사 경로를 만들 수 있습니다.

센서는 원래 통신의 전달 경로를 이어 주는 장치가 아닙니다. 이 점이 경로에 들어와 전달·차단하는 Inline과 다릅니다. 다음 Page에서는 스위치가 어느 포트로 패킷 복사본을 보내는지 살펴보겠습니다.

## Mirroring · 패킷을 복사하기

<!-- learn-page-id: advanced-source-05-page-02 -->

신청 페이지 앞의 스위치가 사용자와 서버 사이의 패킷을 전달하고 있습니다. 운영자가 특정 포트를 복사 대상으로 지정하면 스위치는 원본 패킷을 원래 목적지로 보내는 동시에, 같은 내용을 관찰용 포트에도 복사할 수 있습니다. 이 기능을 **Port mirroring(포트 미러링)**이라고 합니다.

예를 들어 서버로 향하는 포트와 사용자가 연결된 포트의 트래픽을 별도 분석 포트로 복사할 수 있습니다. 여러 링크를 모으거나 복사본을 여러 분석 장치에 나눌 때에는 TAP 스위치 같은 전용 수집 장비를 활용하기도 합니다. “복사”는 공짜 작업이 아닙니다. 복사할 트래픽이 많으면 스위치나 TAP의 포트 용량과 복사 처리 능력을 고려해야 합니다.

복사본을 여러 곳에 보내면 운영, 장애 분석, 보안 관찰을 병렬로 수행할 수 있지만 필요한 대역폭도 커집니다. 관찰 장치가 충분히 빠르지 않으면 복사 과정이나 수신 과정에서 일부가 누락될 수 있습니다. 다음 Page에서는 복사본 분석과 원래 패킷의 통과·차단을 구분하겠습니다.

## Read only와 차단의 차이

<!-- learn-page-id: advanced-source-05-page-03 -->

센서의 관찰 포트에 노트북을 연결하고 Wireshark로 패킷을 확인한다고 해 봅시다. 이 노트북은 원래 통신을 중계하지 않고, 복사된 패킷을 읽어 기록하는 **Read only(읽기 전용) 관찰**을 합니다. 심장 소리를 듣는 청진기가 환자의 혈액 흐름을 직접 조절하지 않는 것과 비슷합니다.

센서가 이상한 패킷을 발견했다고 해도 복사본을 보는 것만으로 원본 패킷이 자동으로 차단되지는 않습니다. 차단하려면 Inline 장치에 규칙을 적용하거나, 별도의 대응 절차를 호출하는 등 추가 동작이 필요합니다. 경로 밖에서 발견하는 기능과 경로 안에서 통신을 바꾸는 기능을 구별하면 센서의 역할을 정확히 설명할 수 있습니다.

네트워크 트래픽에는 로그인 정보, 검색 기록, 사적인 대화처럼 민감한 데이터가 포함될 수 있습니다. 합법적인 운영 목적과 적절한 권한·절차를 갖춘 관찰인지 함께 따져야 합니다. 다음 Page에서는 센서가 원래 통신을 통과시키지 않으면서도 접속에 영향을 주는 사례가 어떤 별도 조건을 요구하는지 보겠습니다.

## 경로 밖에서 접속에 개입하기

<!-- learn-page-id: advanced-source-05-page-04 -->

인터넷 사업자가 특정 웹 주소의 접속을 감지해 이용자에게 경고를 보여 주려는 상황을 생각해 봅시다. 센서가 통신을 복사해 분석하는 기본 Out of path 구조만으로는 원래 패킷을 중간에서 버릴 수 없습니다. 따라서 “관찰 장치가 경고 화면을 보여 줬다”는 결과에는 관찰 외의 대응 방식이 추가되어야 합니다.

가능한 설계 중 하나는 센서나 별도의 대응 장치가 관찰한 연결을 토대로 클라이언트에 별도 응답을 보내는 것입니다. 하지만 센서는 원래 경로에 있지 않으므로 원본의 송수신 양쪽 연결을 직접 이어받아 응답하는 것이 아닙니다. 어떤 패킷을 볼 수 있는지, 연결의 주소와 상태를 얼마나 빨리 알아내는지, 클라이언트가 어떤 응답을 받아들이는지에 따라 결과가 달라집니다.

이런 동작은 기본적인 수동 관찰과 구분해 ‘능동 개입’으로 설명해야 합니다. 센서가 복사본을 받는다는 사실만으로 임의의 사이트를 차단하거나 안전하게 다른 페이지로 바꿀 수 있다고 보면 안 됩니다. 다음 Page에서는 TCP 연결을 대상으로 별도의 응답이 영향을 줄 수 있는 이유와 한계를 살펴보겠습니다.

## TCP 응답을 이용한 개입

<!-- learn-page-id: advanced-source-05-page-05 -->

웹 서버로 가는 TCP 연결을 센서가 관찰한다고 하겠습니다. 네트워크에 연결된 별도 장치가 클라이언트 또는 서버처럼 보이는 패킷을 추가로 보내면, 단말이 그 패킷을 유효한 연결의 응답으로 받아들일 가능성이 있습니다. 이를 이용해 접속을 끊거나 다른 안내로 유도하는 능동 대응을 설계할 수 있지만, 단순한 복사 관찰과는 다른 기능입니다.

TCP는 연결의 상태와 순서 번호 등을 확인하므로, 임의의 패킷 하나를 보낸다고 항상 연결이 원하는 대로 바뀌는 것은 아닙니다. 센서가 통신의 양 끝과 상태를 정확히 알아야 하고, 단말이 받아들일 수 있는 응답이어야 합니다. 차단이 목적이라면 Inline 장치의 정책 적용이 더 직접적인 방법일 수 있습니다. 경로 밖 개입에는 정확성과 오작동 위험을 따져야 합니다.

또한 HTTP 응답이 브라우저에 경고 페이지를 보여 주려면 연결이 해당 응답을 수용하는 방식이어야 합니다. HTTPS라면 암호화와 인증 때문에 임의의 응답이 웹사이트 콘텐츠인 것처럼 보이게 만들기는 더 어렵습니다. 다음 Page에서는 패킷의 헤더와 안쪽 데이터, 그리고 DPI가 무엇을 검사하는지 구분합니다.

## DPI · Payload까지 살펴보기

<!-- learn-page-id: advanced-source-05-page-06 -->

신청 요청을 실은 패킷에는 목적지를 찾는 데 쓰이는 IP 헤더, TCP 연결을 구분하는 정보, 그리고 그 안에 실린 상위 데이터가 들어갈 수 있습니다. 택배 상자에 비유하면 헤더는 운송에 필요한 송장, 안쪽 데이터는 전달할 내용물에 가깝습니다. 패킷 안에서 실제 전달하는 상위 계층 데이터를 **Payload(페이로드)**라고 합니다.

**DPI(Deep Packet Inspection)**는 주소와 포트 같은 기본 헤더만 확인하는 것을 넘어, 패킷 안의 상위 프로토콜이나 Payload까지 분석하는 검사 방식입니다. 상대적으로 얕은 헤더 중심 검사를 SPI(Shallow Packet Inspection)라고 부르기도 합니다. 다만 DPI라는 이름만으로 검사 범위가 하나로 정해지지는 않습니다. 제품과 설정, 암호화 여부에 따라 실제로 확인할 수 있는 데이터가 달라집니다.

HTTPS/TLS로 암호화된 내용은 그 세션을 복호화할 수 있는 구성이나 권한이 없으면 패킷 복사본만으로 평문처럼 읽을 수 없습니다. 주소·포트·일부 연결 정보와 암호화된 Payload를 구별해야 합니다. 내용을 더 깊게 볼수록 사생활과 통신 비밀의 문제가 커집니다. 다음 Page에서는 기술적으로 가능한 검사와 사회적으로 허용할 검사를 구분해 봅니다.

## 망중립과 사생활의 문제

<!-- learn-page-id: advanced-source-05-page-07 -->

운영자가 신청 서비스의 보안을 위해 모든 접속을 자세히 분석하고 싶어도, 네트워크를 지나는 데이터에는 이용자의 사적인 정보가 포함될 수 있습니다. 파일 검사 때문에 택배 상자를 열어 보듯 통신 내용을 검사하면 악성 데이터의 단서를 찾을 수 있지만, 동시에 이용자가 주고받은 민감한 내용까지 볼 수 있습니다.

**망중립성** 논의에서는 네트워크 사업자나 관리자가 특정 서비스·콘텐츠의 트래픽을 어떤 기준으로 차별하거나 제한하는 것이 타당한지 따집니다. 보안 위협을 막기 위한 조치와 특정 서비스에 불리한 정책은 같은 질문이 아닙니다. 어떤 트래픽을 왜 검사하고, 누구에게 어떤 영향을 주는지 따져야 합니다. 기술적으로 식별할 수 있다는 사실이 그 내용을 항상 수집·저장해도 된다는 뜻은 아닙니다.

따라서 센서를 설계할 때는 수집 목적, 필요한 데이터 범위, 보관 기간, 접근 권한을 함께 정해야 합니다. 법과 정책은 적용 지역과 시점, 운영 주체에 따라 다를 수 있으므로 이 Page는 법률 자문 대신 기술 구조가 만든 쟁점을 소개합니다. 다음 Page에서는 정책과 별개로 센서가 관찰 데이터를 놓칠 수 있는 성능 문제를 살펴보겠습니다.

## 놓치지 않고 수집하는 문제

<!-- learn-page-id: advanced-source-05-page-08 -->

행사 신청이 시작되자 수만 개의 패킷이 짧은 시간에 몰립니다. 스위치가 원본 트래픽을 복사해도 센서가 그 속도로 데이터를 받아 처리하지 못하면 일부 패킷은 관찰 기록에 남지 않을 수 있습니다. 경로 밖 센서의 분석 결과는 실제 회선에서 오간 모든 패킷을 완벽히 반영한다고 자동으로 보장되지는 않습니다.

복사 지점의 출력 포트가 복수 회선의 합산 트래픽보다 느리면 그 지점에서 이미 복사본이 누락될 수 있습니다. 센서의 NIC, 메모리, 캡처 프로그램도 데이터 속도를 감당해야 합니다. 네트워크 처리량 외에도 시스템 부하와 버퍼 크기가 영향을 줍니다. 따라서 “미러링을 켰다”는 설정만 확인하지 말고 포트 속도와 드롭 카운터 등을 함께 점검해야 합니다.

용도에 따라 허용 가능한 누락률은 다릅니다. 대략적인 접속 추세를 파악하는 목적과 보안 사고의 패킷 한 개까지 추적해야 하는 목적은 요구 수준이 다릅니다. 다음 Page에서는 수집 이후의 저장과 분석 과정도 별도의 병목이 될 수 있음을 살펴보겠습니다.

## 저장과 분석의 부하

<!-- learn-page-id: advanced-source-05-page-09 -->

복사본을 센서에 전달한 뒤에는 데이터를 받아 저장하고 분석해야 합니다. 패킷을 메모리에서 읽어 가공하는 데 CPU가 필요하고, 기록을 남기면 디스크 쓰기 성능도 영향을 줍니다. 센서가 네트워크에서 데이터를 받는 속도가 충분해도 저장 장치가 따라오지 못하면 수집 중 데이터가 누락될 수 있습니다.

예를 들어 1Gbps를 바이트 단위로 환산하면 이론상 초당 약 125MB(메가바이트)의 전송량에 해당합니다(1Gbps ÷ 8). 실제 저장량은 링크와 패킷 헤더, 메타데이터, 파일 시스템 오버헤드 등에 따라 달라지지만, 트래픽을 장시간 기록하려면 큰 저장 용량과 지속 쓰기 성능이 필요하다는 감을 줍니다. 저장 전에 필요한 항목만 필터링하거나 요약하면 부담을 줄일 수 있지만, 나중에 분석할 정보도 함께 줄어들 수 있습니다.

따라서 장비를 고를 때는 입력 포트 속도만 볼 것이 아니라 수집, 분석, 기록의 전체 파이프라인을 살펴야 합니다. “센서가 빠른가?”는 네트워크 카드의 숫자 하나가 아니라 여러 처리 단계의 용량을 묻는 질문입니다. 다음에는 Inline과 Out of path를 같은 상황에 놓고 무엇이 다른지 정리하겠습니다.

## Inline과 Out of path 비교

<!-- learn-page-id: advanced-source-05-page-10 -->

동아리 운영자는 신청 요청을 검사해 즉시 차단할지, 별도 복사본을 모아 나중에 분석할지 선택해야 합니다. **Inline**은 원본 패킷이 지나가는 경로 안에서 처리하므로 전달·차단 결정이 통신에 바로 영향을 줄 수 있습니다. **Out of path**는 경로 밖 센서가 복사본을 받아 분석하므로 원래 전달을 직접 맡지 않는 것이 기본입니다.

두 구조의 요구 성능도 다릅니다. Inline 장치는 실제 트래픽을 계속 전달하면서 정책 처리를 마쳐야 합니다. Out of path는 복사본을 놓치지 않고 수집하고 분석하는 용량이 중요합니다. 1Gbps 회선을 꽉 채운 복사본을 저장한다면 초당 약 125MB 수준의 입력을 감당해야 하므로, 장시간 무손실 기록은 네트워크·메모리·CPU·저장장치 모두에 부담을 줍니다.

목표가 실시간 차단이면 Inline 배치가 알맞을 수 있고, 서비스에 영향을 주지 않으면서 사후 분석하려면 경로 밖 관찰이 적합할 수 있습니다. 어느 방식이 더 좋다고 일괄 판단하기보다 통신 개입 필요성, 허용 가능한 누락, 처리량과 개인정보 보호를 함께 따져야 합니다. 다음 Lesson에서는 클라이언트나 서버를 대신해 연결을 맺는 Proxy 구조로 넘어갑니다.
