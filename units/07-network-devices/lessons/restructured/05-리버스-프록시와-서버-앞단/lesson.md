---
id: u7-advanced-08-reverse-proxy
title: 리버스 프록시와 서버 앞단
source_lesson_ids:
- u7-advanced-08-reverse-proxy
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-08.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/07-1.md#p392-b02
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-08.md
page_metadata:
- page_id: advanced-source-08-page-01
  illustrations:
  - file: assets/animations/u11-reverse-front.svg
    title: "Client 보호와 Server 보호"
    alt: "사용자가 서비스 이름으로 접속하면 DNS가 알려 준 앞단 Proxy가 요청을 받아 안쪽 서버로 전달하는 모습입니다."
    caption: "Reverse Proxy는 서버 앞에서 요청을 먼저 받습니다."
    after_paragraph: 0
  questions:
  - id: u11-l05-p01-q01
    kind: choice
    difficulty: easy
    prompt: Reverse Proxy가 보통 놓이는 위치는 어디인가요?
    choices:
    - id: a
      text: 사용자의 브라우저 안
      feedback: 본문에서 reverse Proxy는 서버 측 앞단에서 요청을 먼저 받습니다. 확인해 보세요.
    - id: b
      text: 스위치의 복사 포트만
      feedback: 본문에서 reverse Proxy는 서버 측 앞단에서 요청을 먼저 받습니다. 확인해 보세요.
    - id: c
      text: 실제 서버의 뒤쪽 저장장치
      feedback: 본문에서 reverse Proxy는 서버 측 앞단에서 요청을 먼저 받습니다. 확인해 보세요.
    - id: d
      text: 실제 웹 서버 앞에서 요청을 받는 위치
      feedback: Reverse Proxy는 서버 측 앞단에서 요청을 먼저 받습니다.
    - id: e
      text: DNS 이름 안쪽
      feedback: 본문에서 reverse Proxy는 서버 측 앞단에서 요청을 먼저 받습니다. 확인해 보세요.
    answer: d
  - id: u11-l05-p01-q02
    kind: choice
    difficulty: medium
    prompt: Reverse Proxy가 외부 클라이언트에게 서버처럼 보이는 이유는 무엇인가요?
    choices:
    - id: a
      text: 클라이언트의 요청을 먼저 받아 내부 서버로 전달하기 때문
      feedback: 클라이언트는 앞단 주소에 접속하고 Proxy가 안쪽 서버를 대리합니다.
    - id: b
      text: 실제 서버가 항상 사라지기 때문
      feedback: 본문에서 클라이언트는 앞단 주소에 접속하고 Proxy가 안쪽 서버를 대리합니다. 확인해 보세요.
    - id: c
      text: DNS가 브라우저 화면을 보내기 때문
      feedback: 본문에서 클라이언트는 앞단 주소에 접속하고 Proxy가 안쪽 서버를 대리합니다. 확인해 보세요.
    - id: d
      text: 패킷 복사본만 관찰하기 때문
      feedback: 본문에서 클라이언트는 앞단 주소에 접속하고 Proxy가 안쪽 서버를 대리합니다. 확인해 보세요.
    - id: e
      text: 모든 서버 주소를 삭제하기 때문
      feedback: 본문에서 클라이언트는 앞단 주소에 접속하고 Proxy가 안쪽 서버를 대리합니다. 확인해 보세요.
    answer: a
- page_id: advanced-source-08-page-02
  illustrations:
  - file: assets/animations/u11-reverse-ips.svg
    title: "IPS · 앞단에서의 방어"
    alt: "서버 앞 IPS가 정상 패킷은 통과시키고 공격 패턴은 차단하며, 암호화된 HTTPS 본문은 그대로 읽기 어렵다는 그림입니다."
    caption: "IPS가 볼 수 있는 정보는 위치와 암호화에 따라 달라집니다."
    after_paragraph: 0
  questions:
  - id: u11-l05-p02-q01
    kind: choice
    difficulty: easy
    prompt: IPS를 Inline으로 배치했을 때 할 수 있는 일은 무엇인가요?
    choices:
    - id: a
      text: DNS 이름을 화면으로 표시한다
      feedback: 본문에서 inline IPS는 정책에 따라 원래 경로의 통신에 영향을 줄 수 있습니다. 확인해 보세요.
    - id: b
      text: 서버 데이터를 자동 백업한다
      feedback: 본문에서 inline IPS는 정책에 따라 원래 경로의 통신에 영향을 줄 수 있습니다. 확인해 보세요.
    - id: c
      text: 모든 TLS 내용을 자동으로 복호화한다
      feedback: 본문에서 inline IPS는 정책에 따라 원래 경로의 통신에 영향을 줄 수 있습니다. 확인해 보세요.
    - id: d
      text: 웹 브라우저의 설정을 바꾼다
      feedback: 본문에서 inline IPS는 정책에 따라 원래 경로의 통신에 영향을 줄 수 있습니다. 확인해 보세요.
    - id: e
      text: 규칙에 따라 패킷을 탐지하거나 통과·차단한다
      feedback: Inline IPS는 정책에 따라 원래 경로의 통신에 영향을 줄 수 있습니다.
    answer: e
  - id: u11-l05-p02-q02
    kind: choice
    difficulty: medium
    prompt: 암호화된 HTTPS 본문을 읽기 어려운 이유는 무엇인가요?
    choices:
    - id: a
      text: HTTPS는 패킷으로 전달되지 않기 때문
      feedback: 본문에서 연결 정보가 일부 보여도 TLS Payload의 평문 내용을 읽는 것과는 다릅니다. 확인해 보세요.
    - id: b
      text: TLS를 종료하거나 검사할 구성이 없으면 Payload가 암호화되어 있기 때문
      feedback: 연결 정보가 일부 보여도 TLS Payload의 평문 내용을 읽는 것과는 다릅니다.
    - id: c
      text: IP 헤더가 반드시 암호화되기 때문
      feedback: 본문에서 연결 정보가 일부 보여도 TLS Payload의 평문 내용을 읽는 것과는 다릅니다. 확인해 보세요.
    - id: d
      text: IPS는 전원을 쓰지 않기 때문
      feedback: 본문에서 연결 정보가 일부 보여도 TLS Payload의 평문 내용을 읽는 것과는 다릅니다. 확인해 보세요.
    - id: e
      text: WAF가 DNS를 차단하기 때문
      feedback: 본문에서 연결 정보가 일부 보여도 TLS Payload의 평문 내용을 읽는 것과는 다릅니다. 확인해 보세요.
    answer: b
- page_id: advanced-source-08-page-03
  illustrations:
  - file: assets/animations/u11-reverse-tls.svg
    title: "SSL Accelerator와 복호화"
    alt: "브라우저가 앞단 Proxy와 TLS 연결을 맺고, Proxy가 내부 서버로 요청을 전달하는 모습입니다."
    caption: "TLS 종단 Proxy는 서버 대신 HTTPS 연결을 받습니다."
    after_paragraph: 0
  questions:
  - id: u11-l05-p03-q01
    kind: choice
    difficulty: easy
    prompt: TLS 종단 Proxy가 연결을 받았을 때 가능한 동작은 무엇인가요?
    choices:
    - id: a
      text: TLS를 종료해 검사하고 내부 서버로 전달할 수 있다
      feedback: 앞단에서 TLS를 종료하는 구성에서는 복호화 후 정책 검사가 가능할 수 있습니다.
    - id: b
      text: 암호화 키 없이 어떤 HTTPS도 항상 읽는다
      feedback: 본문에서 앞단에서 TLS를 종료하는 구성에서는 복호화 후 정책 검사가 가능할 수 있습니다. 확인해 보세요.
    - id: c
      text: 브라우저 대신 DNS 이름을 만든다
      feedback: 본문에서 앞단에서 TLS를 종료하는 구성에서는 복호화 후 정책 검사가 가능할 수 있습니다. 확인해 보세요.
    - id: d
      text: 서버의 IP 주소를 삭제한다
      feedback: 본문에서 앞단에서 TLS를 종료하는 구성에서는 복호화 후 정책 검사가 가능할 수 있습니다. 확인해 보세요.
    - id: e
      text: 원래 연결을 복사만 하고 종료한다
      feedback: 본문에서 앞단에서 TLS를 종료하는 구성에서는 복호화 후 정책 검사가 가능할 수 있습니다. 확인해 보세요.
    answer: a
  - id: u11-l05-p03-q02
    kind: choice
    difficulty: medium
    prompt: HTTPS 검사 구성에서 필요한 준비로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: Loopback 주소만 지정하기
      feedback: 본문에서 tLS 검사에는 별도의 적절한 인증서와 클라이언트 신뢰 구성이 필요할 수 있습니다. 확인해 보세요.
    - id: b
      text: 모든 인증서 검증 무시하기
      feedback: 본문에서 tLS 검사에는 별도의 적절한 인증서와 클라이언트 신뢰 구성이 필요할 수 있습니다. 확인해 보세요.
    - id: c
      text: 인증서와 신뢰·연결 설정 등 운영 준비
      feedback: TLS 검사에는 별도의 적절한 인증서와 클라이언트 신뢰 구성이 필요할 수 있습니다.
    - id: d
      text: DNS 서버 전원 끄기
      feedback: 본문에서 tLS 검사에는 별도의 적절한 인증서와 클라이언트 신뢰 구성이 필요할 수 있습니다. 확인해 보세요.
    - id: e
      text: 패킷 복사만 켜기
      feedback: 본문에서 tLS 검사에는 별도의 적절한 인증서와 클라이언트 신뢰 구성이 필요할 수 있습니다. 확인해 보세요.
    answer: c
- page_id: advanced-source-08-page-04
  illustrations:
  - file: assets/animations/u11-reverse-waf.svg
    title: "WAF · 웹 요청을 검사"
    alt: "WAF가 정상 요청은 서버로 전달하고 웹 공격 패턴은 차단하지만 모든 공격을 찾지는 못한다는 그림입니다."
    caption: "WAF는 웹 요청의 내용을 보고 허용하거나 차단합니다."
    after_paragraph: 0
  questions:
  - id: u11-l05-p04-q01
    kind: choice
    difficulty: easy
    prompt: WAF가 주로 검사하는 대상은 무엇인가요?
    choices:
    - id: a
      text: 랜선의 색상
      feedback: 본문에서 wAF는 웹 요청에 나타나는 애플리케이션 공격 패턴을 검사합니다. 확인해 보세요.
    - id: b
      text: 웹 애플리케이션 요청
      feedback: WAF는 웹 요청에 나타나는 애플리케이션 공격 패턴을 검사합니다.
    - id: c
      text: 모니터 밝기
      feedback: 본문에서 wAF는 웹 요청에 나타나는 애플리케이션 공격 패턴을 검사합니다. 확인해 보세요.
    - id: d
      text: 전원 공급 장치의 전압만
      feedback: 본문에서 wAF는 웹 요청에 나타나는 애플리케이션 공격 패턴을 검사합니다. 확인해 보세요.
    - id: e
      text: DNS 서버의 운영체제만
      feedback: 본문에서 wAF는 웹 요청에 나타나는 애플리케이션 공격 패턴을 검사합니다. 확인해 보세요.
    answer: b
  - id: u11-l05-p04-q02
    kind: choice
    difficulty: medium
    prompt: WAF 규칙의 한계에 대한 설명으로 옳은 것은 무엇인가요?
    choices:
    - id: a
      text: 규칙은 모든 공격을 완벽히 차단한다
      feedback: 본문에서 규칙은 애플리케이션에 맞춰 관리해야 하며 완벽한 방어를 보장하지 않습니다. 확인해 보세요.
    - id: b
      text: WAF는 서버 요청을 전달하지 않는다
      feedback: 본문에서 규칙은 애플리케이션에 맞춰 관리해야 하며 완벽한 방어를 보장하지 않습니다. 확인해 보세요.
    - id: c
      text: WAF는 IP 주소를 사용하지 않는다
      feedback: 본문에서 규칙은 애플리케이션에 맞춰 관리해야 하며 완벽한 방어를 보장하지 않습니다. 확인해 보세요.
    - id: d
      text: 정상 요청을 막거나 공격을 놓칠 수 있어 설정과 점검이 필요하다
      feedback: 규칙은 애플리케이션에 맞춰 관리해야 하며 완벽한 방어를 보장하지 않습니다.
    - id: e
      text: WAF는 HTTPS와 관계없이 평문을 본다
      feedback: 본문에서 규칙은 애플리케이션에 맞춰 관리해야 하며 완벽한 방어를 보장하지 않습니다. 확인해 보세요.
    answer: d
- page_id: advanced-source-08-page-05
  illustrations:
  - file: assets/animations/u11-reverse-compare.svg
    title: "Reverse Proxy로 서버 보호"
    alt: "Forward Proxy는 클라이언트를 대신하고 Reverse Proxy는 서버를 대신하며, 이번 Unit의 세 가지 구조를 정리하는 표입니다."
    caption: "Forward와 Reverse는 대신하는 방향이 다릅니다."
    after_paragraph: 0
  questions:
  - id: u11-l05-p05-q01
    kind: choice
    difficulty: easy
    prompt: Forward Proxy와 Reverse Proxy의 주요 구분 기준은 무엇인가요?
    choices:
    - id: a
      text: 장비의 외관 색상
      feedback: 본문에서 두 용어는 대리하는 방향과 배치 관점이 다릅니다. 확인해 보세요.
    - id: b
      text: 장비 제조 국가
      feedback: 본문에서 두 용어는 대리하는 방향과 배치 관점이 다릅니다. 확인해 보세요.
    - id: c
      text: 클라이언트 측 요청을 대리하는지 서버 앞에서 요청을 받는지
      feedback: 두 용어는 대리하는 방향과 배치 관점이 다릅니다.
    - id: d
      text: 서버 파일의 크기
      feedback: 본문에서 두 용어는 대리하는 방향과 배치 관점이 다릅니다. 확인해 보세요.
    - id: e
      text: DNS 이름 글자 수
      feedback: 본문에서 두 용어는 대리하는 방향과 배치 관점이 다릅니다. 확인해 보세요.
    answer: c
  - id: u11-l05-p05-q02
    kind: choice
    difficulty: medium
    prompt: 서비스 앞단 Proxy 하나가 해결하지 않는 것은 무엇인가요?
    choices:
    - id: a
      text: 요청을 내부 서버로 전달하는 기능
      feedback: 본문에서 reverse Proxy는 여러 운영 문제를 자동으로 모두 해결하지 않습니다. 확인해 보세요.
    - id: b
      text: 앞단 주소가 접속 대상이 되는 구조
      feedback: 본문에서 reverse Proxy는 여러 운영 문제를 자동으로 모두 해결하지 않습니다. 확인해 보세요.
    - id: c
      text: TLS 종료 기능이 결합될 가능성
      feedback: 본문에서 reverse Proxy는 여러 운영 문제를 자동으로 모두 해결하지 않습니다. 확인해 보세요.
    - id: d
      text: 요청의 중계 역할
      feedback: 본문에서 reverse Proxy는 여러 운영 문제를 자동으로 모두 해결하지 않습니다. 확인해 보세요.
    - id: e
      text: DNS·서버·분산·보안 구성을 함께 맞춰야 하는 운영 문제 전체
      feedback: Reverse Proxy는 여러 운영 문제를 자동으로 모두 해결하지 않습니다.
    answer: e
---

## Client 보호와 Server 보호

<!-- learn-page-id: advanced-source-08-page-01 -->

동아리 행사 신청이 알려지자 접속자가 늘고, 운영자는 실제 웹 서버를 인터넷에 바로 공개하는 것이 걱정됩니다. 사용자가 먼저 만나는 주소와 요청을 실제로 처리하는 서버를 분리할 수 있습니다. 클라이언트 쪽 요청을 대신 전달하는 Forward Proxy와 반대로, **Reverse Proxy(리버스 프록시)**는 서버 앞에서 요청을 먼저 받습니다.

사용자는 `event.example` 같은 서비스 이름으로 접속하지만, DNS가 가리키는 주소는 실제 애플리케이션 서버가 아니라 앞단 Reverse Proxy일 수 있습니다. 클라이언트 입장에서는 Proxy가 요청을 받아 주는 서버처럼 보이고, Proxy는 내부의 실제 서버에 요청을 전달합니다. 여러 서버를 내부에 둘 수도 있습니다.

서버를 감추거나 요청을 검사하는 기능을 더할 수 있지만, 이 구조 하나가 보안과 성능을 자동으로 보장하지는 않습니다. 장치마다 맡은 역할과 처리 가능한 데이터가 다릅니다. 다음에는 서버 앞단에 IPS를 두었을 때 확인할 수 있는 정보와 HTTPS의 제약을 살펴보겠습니다.

## IPS · 앞단에서의 방어

<!-- learn-page-id: advanced-source-08-page-02 -->

외부에서 들어오는 신청 요청이 실제 웹 서버에 닿기 전에, 앞단에 IPS를 배치할 수 있습니다. IPS는 설정된 규칙이나 알려진 공격 패턴을 바탕으로 통신을 탐지하거나 차단하도록 구성됩니다. Inline으로 놓이면 정책에 맞는 패킷을 통과시키거나 차단해 원래 연결에 영향을 줄 수 있습니다.

검사 장치가 패킷 헤더와 프로토콜 정보를 보는 것과 웹 요청의 본문까지 이해하는 것은 다릅니다. HTTP 내용이 TLS로 암호화된 HTTPS라면, TLS를 종료하거나 검사할 수 있는 별도 구성이 없는 장치는 암호화된 Payload를 평문 요청처럼 분석하기 어렵습니다. 주소나 일부 연결 정보가 보이더라도 웹 본문을 읽는 것과 같지 않습니다.

IPS의 탐지 범위와 대응 방식은 장비의 기능, 위치, 규칙에 따라 달라집니다. 서버 공격을 검사하려면 어느 구간에서 어떤 데이터가 보이는지부터 확인해야 합니다. 다음에는 서버 대신 TLS 처리를 맡는 앞단 Proxy가 검사 기능과 어떻게 결합되는지 보겠습니다.

## SSL Accelerator와 복호화

<!-- learn-page-id: advanced-source-08-page-03 -->

웹 서버 대신 앞단 Proxy가 HTTPS 연결을 받도록 구성할 수 있습니다. 예를 들어 `event.example`의 DNS가 실제 서버 주소가 아니라 Proxy의 주소를 알려 주면, 브라우저는 먼저 Proxy와 TLS 연결을 맺습니다. Proxy는 서버를 대신해 연결을 처리하고 내부 서버로 요청을 전달합니다. TLS 처리를 앞단에 모으는 장치를 SSL Accelerator 또는 TLS 종단 Proxy라고 부르기도 합니다.

TLS가 Proxy에서 종료되면, Proxy는 복호화된 요청을 정책에 따라 검사한 뒤 내부의 다른 연결로 전달할 수 있습니다. 이 구간을 다시 암호화할지 내부망에서 평문으로 보낼지는 별도 구성의 선택이며, 보안 요건과 네트워크 경계를 고려해야 합니다. 복호화 기능과 부하 분산, WAF 같은 기능이 한 장치에 결합되기도 합니다.

HTTPS 내용을 검사하려면 인증서와 개인 키, 클라이언트가 신뢰하는 연결 구성 등 운영 준비가 필요합니다. 인증서 신뢰를 무시하거나 허가 없이 통신을 복호화하는 것과는 구분해야 합니다. 다음에는 복호화된 웹 요청을 검사하는 WAF가 어떤 역할을 하는지 살펴보겠습니다.

## WAF · 웹 요청을 검사

<!-- learn-page-id: advanced-source-08-page-04 -->

앞단 Proxy가 HTTPS 요청을 받아 TLS를 종료하면, 구성에 따라 **WAF(Web Application Firewall)**가 웹 요청을 검사할 수 있습니다. WAF는 SQL 삽입이나 사이트 간 스크립팅처럼 웹 애플리케이션을 겨냥한 요청 패턴을 찾아 정책에 따라 허용하거나 차단하도록 설계됩니다. IP 주소와 포트만 보는 정책보다 웹 요청의 경로·매개변수·본문 같은 애플리케이션 정보를 활용할 수 있습니다.

WAF는 요청을 받아 내부 웹 서버에 전달하고, 응답을 다시 클라이언트에 돌려줄 수 있습니다. 사용자는 외부 주소로 접속하지만 실제 처리는 내부 서버에서 이뤄집니다. 검사 규칙이 모든 공격을 찾아내는 것은 아니며, 애플리케이션에 맞지 않는 규칙은 정상 요청을 막거나 공격을 놓칠 수 있습니다.

웹 서비스 앞단에서 요청을 대리하고 검사하는 구조를 보면, Proxy가 서버 보호와 결합되는 이유가 드러납니다. 다음 Page에서 이 구조를 Reverse Proxy로 정리하고 Forward Proxy와 관점 차이를 다시 비교하겠습니다.

## Reverse Proxy로 서버 보호

<!-- learn-page-id: advanced-source-08-page-05 -->

Reverse Proxy는 실제 서버 앞에서 요청을 받아 내부의 한 서버 또는 여러 서버로 전달하는 중개자입니다. 외부 클라이언트에게는 서비스의 접속 대상처럼 보이고, 안쪽에서는 오리진 서버를 대신해 연결을 이어 줍니다. 요청을 어느 서버로 보낼지 정하거나, TLS를 종료하거나, 캐시와 WAF를 결합하는 구성도 가능합니다.

Forward Proxy와 Reverse Proxy는 대리하는 방향과 관리 관점이 다릅니다. Forward Proxy는 클라이언트가 외부 서버에 보낼 요청을 대신 전달하는 쪽이고, Reverse Proxy는 서비스 운영자가 서버 앞에 두어 외부 요청을 받아 내부 서버로 전달하는 쪽입니다. 실제 용어는 제품과 문맥에서 겹쳐 쓰일 수 있으므로, 장치가 누굴 대신하고 어느 쪽 연결을 받는지 확인하는 것이 명확합니다.

우리 서비스가 성장하면 앞단 장치 하나만으로 모든 문제를 해결하기보다 DNS, 서버 구성, 부하 분산, 보안 정책이 함께 맞아야 합니다. 이번 Unit에서 배운 세 가지 구조—원본 경로 안에서 처리하기, 복사본을 경로 밖에서 관찰하기, 연결을 대신 중계하기—를 구별할 수 있습니다. 다음 Unit에서는 공유기와 NAT가 주소·포트를 어떻게 연결하는지 살펴봅니다.
