---
id: u7-advanced-02-세-가지-네트워크-장치-구조
title: 장치가 트래픽을 다루는 세 가지 구조
source_lesson_ids:
- u7-advanced-02-세-가지-네트워크-장치-구조
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-02.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-02.md
page_metadata:
- page_id: advanced-source-02-page-01
  illustrations:
  - file: assets/diagrams/source-02.svg
    title: Inline·Out of path·Proxy · 원고 그림
    alt: Inline·Out of path·Proxy에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
  questions:
  - id: u11-l01-p01-q01
    kind: choice
    difficulty: easy
    prompt: 이 Lesson에서 장치 구조를 비교할 때 가장 먼저 살펴볼 두 가지는 무엇인가요?
    choices:
    - id: a
      text: 통신 경로에서의 위치와 처리하는 데이터 단위
      feedback: 맞아요. 장치가 경로 어디에 있고 패킷이나 소켓 Stream 중 무엇을 다루는지 보면 구조를 구분할 수 있어요.
    - id: b
      text: 장치의 제조사와 설치 연도
      feedback: 장치 이름이나 겉모습만으로 역할을 판단하지 말고 위치와 처리 단위를 함께 보세요.
    - id: c
      text: 전원 사용량과 케이블 색
      feedback: 장치 이름이나 겉모습만으로 역할을 판단하지 말고 위치와 처리 단위를 함께 보세요.
    - id: d
      text: IP 주소의 숫자와 도메인 이름
      feedback: 장치 이름이나 겉모습만으로 역할을 판단하지 말고 위치와 처리 단위를 함께 보세요.
    - id: e
      text: 운영체제와 화면 크기
      feedback: 장치 이름이나 겉모습만으로 역할을 판단하지 말고 위치와 처리 단위를 함께 보세요.
    answer: a
  - id: u11-l01-p01-q02
    kind: choice
    difficulty: medium
    prompt: 한 장치에 Inline 기능과 Proxy 기능이 함께 있을 수 있다는 설명으로 알맞은 것은?
    choices:
    - id: a
      text: 구조 이름은 서로 배타적이라 한 가지만 선택해야 한다
      feedback: 본문은 이 분류를 서로 완전히 배타적인 제품 종류로 보지 말라고 설명해요.
    - id: b
      text: 한 장치는 반드시 패킷만 처리한다
      feedback: 본문은 이 분류를 서로 완전히 배타적인 제품 종류로 보지 말라고 설명해요.
    - id: c
      text: 한 장치가 통신 경로 안에서 패킷을 다루면서 소켓 Stream 기능도 결합할 수 있다
      feedback: 맞아요. 세 구조는 장치의 연결 위치와 처리 방식에 대한 관점이어서 한 장치가 여러 특징을 가질 수 있어요.
    - id: d
      text: Proxy는 패킷을 전혀 전달하지 않는다
      feedback: 본문은 이 분류를 서로 완전히 배타적인 제품 종류로 보지 말라고 설명해요.
    - id: e
      text: Inline은 항상 Out of path와 같은 뜻이다
      feedback: 본문은 이 분류를 서로 완전히 배타적인 제품 종류로 보지 말라고 설명해요.
    answer: c
- page_id: advanced-source-02-page-02
  questions:
  - id: u11-l01-p02-q01
    kind: choice
    difficulty: easy
    prompt: Inline 장치는 통신 경로에서 어떤 일을 할 수 있나요?
    choices:
    - id: a
      text: 통신을 복사만 하고 원본 경로에는 관여하지 않는다
      feedback: 복사본만 관찰하는 Out of path와 달리, Inline은 실제 전달 경로에 놓여 있어요.
    - id: b
      text: 패킷을 규칙에 따라 전달하거나 버릴 수 있다
      feedback: 맞아요. Inline 장치는 원래 패킷이 지나는 경로 안에 있으므로 통과시키거나 차단할 수 있어요.
    - id: c
      text: 브라우저 화면만 저장한다
      feedback: 복사본만 관찰하는 Out of path와 달리, Inline은 실제 전달 경로에 놓여 있어요.
    - id: d
      text: DNS 이름만 바꾼다
      feedback: 복사본만 관찰하는 Out of path와 달리, Inline은 실제 전달 경로에 놓여 있어요.
    - id: e
      text: 항상 서버 대신 새 파일을 만든다
      feedback: 복사본만 관찰하는 Out of path와 달리, Inline은 실제 전달 경로에 놓여 있어요.
    answer: b
  - id: u11-l01-p02-q02
    kind: choice
    difficulty: medium
    prompt: 보안 규칙에서 허용된 패킷을 다음 장치로 보내고 차단 규칙에 맞는 패킷을 버리려 한다. 어떤 구조가 이 동작에 직접 관여하나요?
    choices:
    - id: a
      text: Out of path
      feedback: 경로 바깥에서 복사본을 보는 센서는 원래 패킷을 직접 전달하거나 차단하지 않아요.
    - id: b
      text: Proxy만
      feedback: 경로 바깥에서 복사본을 보는 센서는 원래 패킷을 직접 전달하거나 차단하지 않아요.
    - id: c
      text: Tapping Point만
      feedback: 경로 바깥에서 복사본을 보는 센서는 원래 패킷을 직접 전달하거나 차단하지 않아요.
    - id: d
      text: Inline
      feedback: 맞아요. 경로 안의 Inline 장치는 규칙에 따라 패킷을 전달하거나 Drop할 수 있어요.
    - id: e
      text: 소켓 Stream만
      feedback: 경로 바깥에서 복사본을 보는 센서는 원래 패킷을 직접 전달하거나 차단하지 않아요.
    answer: d
- page_id: advanced-source-02-page-03
  questions:
  - id: u11-l01-p03-q01
    kind: choice
    difficulty: easy
    prompt: Out of path 센서가 보통 분석 대상으로 받는 것은 무엇인가요?
    choices:
    - id: a
      text: 원래 통신을 대신 보내는 요청
      feedback: 원본 통신을 대신하는 구조가 아니라 복사본을 관찰하는 구조예요.
    - id: b
      text: 완성된 브라우저 화면
      feedback: 원본 통신을 대신하는 구조가 아니라 복사본을 관찰하는 구조예요.
    - id: c
      text: 네트워크에서 복사해 준 패킷
      feedback: 맞아요. Out of path 센서는 Tapping Point에서 전달된 패킷 복사본을 분석해요.
    - id: d
      text: 서버의 비밀번호 파일
      feedback: 원본 통신을 대신하는 구조가 아니라 복사본을 관찰하는 구조예요.
    - id: e
      text: 라우터의 전원 신호
      feedback: 원본 통신을 대신하는 구조가 아니라 복사본을 관찰하는 구조예요.
    answer: c
  - id: u11-l01-p03-q02
    kind: choice
    difficulty: medium
    prompt: 센서가 패킷 복사본을 분석하는 동안 원래 패킷은 누가 전달하나요?
    choices:
    - id: a
      text: 센서가 항상 원본 경로를 인수한다
      feedback: 복사본 분석과 원본 전달을 구분해야 해요.
    - id: b
      text: 브라우저가 패킷을 직접 라우팅한다
      feedback: 복사본 분석과 원본 전달을 구분해야 해요.
    - id: c
      text: DNS 서버가 파일을 다시 조립한다
      feedback: 복사본 분석과 원본 전달을 구분해야 해요.
    - id: d
      text: Tapping Point가 응답을 만들어 대신 보낸다
      feedback: 복사본 분석과 원본 전달을 구분해야 해요.
    - id: e
      text: 원래 통신 경로에 놓인 네트워크 장치들
      feedback: 맞아요. Out of path 센서는 복사본을 분석하고 원래 패킷 전달은 원래 경로의 장치들이 이어 가요.
    answer: e
- page_id: advanced-source-02-page-04
  questions:
  - id: u11-l01-p04-q01
    kind: choice
    difficulty: easy
    prompt: 소켓 Stream을 가장 잘 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 라우터 사이에 케이블을 연결하는 물리 장치
      feedback: 패킷은 네트워크의 전달 단위이고, Stream은 프로그램이 소켓에서 읽는 연속된 흐름이에요.
    - id: b
      text: IP 주소를 한 개의 패킷으로 바꾸는 규칙
      feedback: 패킷은 네트워크의 전달 단위이고, Stream은 프로그램이 소켓에서 읽는 연속된 흐름이에요.
    - id: c
      text: 브라우저가 만든 화면 이미지
      feedback: 패킷은 네트워크의 전달 단위이고, Stream은 프로그램이 소켓에서 읽는 연속된 흐름이에요.
    - id: d
      text: 운영체제가 TCP 데이터를 바이트의 연속된 흐름으로 애플리케이션에 건네주는 방식
      feedback: 맞아요. 소켓 Stream은 애플리케이션이 TCP 데이터를 연속된 바이트 흐름으로 읽는 방식이에요.
    - id: e
      text: 패킷 복사본을 모으는 별도 저장소
      feedback: 패킷은 네트워크의 전달 단위이고, Stream은 프로그램이 소켓에서 읽는 연속된 흐름이에요.
    answer: d
  - id: u11-l01-p04-q02
    kind: choice
    difficulty: medium
    prompt: 프록시가 파일 내용을 검사할 때 소켓 Stream을 다루는 이점은 무엇인가요?
    choices:
    - id: a
      text: TCP가 전달한 애플리케이션 바이트 흐름을 패킷 경계에만 의존하지 않고 살펴볼 수 있다
      feedback: 맞아요. 프록시는 소켓에서 애플리케이션 바이트 흐름을 읽어 내용 처리에 활용할 수 있어요.
    - id: b
      text: 항상 파일 전체를 한 번에 메모리에 저장한다
      feedback: Stream 처리의 이점은 애플리케이션 데이터 흐름을 다룬다는 점이지, 파일 전체나 암호 내용을 언제나 자동으로 얻는다는 뜻은 아니에요.
    - id: c
      text: IP 헤더를 제거하면 파일이 자동으로 완성된다
      feedback: Stream 처리의 이점은 애플리케이션 데이터 흐름을 다룬다는 점이지, 파일 전체나 암호 내용을 언제나 자동으로 얻는다는 뜻은 아니에요.
    - id: d
      text: 네트워크 경로를 통과하지 않아도 된다
      feedback: Stream 처리의 이점은 애플리케이션 데이터 흐름을 다룬다는 점이지, 파일 전체나 암호 내용을 언제나 자동으로 얻는다는 뜻은 아니에요.
    - id: e
      text: 모든 암호화된 내용을 자동으로 읽을 수 있다
      feedback: Stream 처리의 이점은 애플리케이션 데이터 흐름을 다룬다는 점이지, 파일 전체나 암호 내용을 언제나 자동으로 얻는다는 뜻은 아니에요.
    answer: a
- page_id: advanced-source-02-page-05
  questions:
  - id: u11-l01-p05-q01
    kind: choice
    difficulty: easy
    prompt: Application Proxy가 보통 살펴보는 정보와 가장 가까운 것은 무엇인가요?
    choices:
    - id: a
      text: 전원 케이블의 전압만
      feedback: 본문에서 L7과 연결한 것은 애플리케이션이 이해하는 HTTP 요청이에요.
    - id: b
      text: 스위치 포트의 물리적 위치만
      feedback: 본문에서 L7과 연결한 것은 애플리케이션이 이해하는 HTTP 요청이에요.
    - id: c
      text: 파일 이름만 기록한 목록
      feedback: 본문에서 L7과 연결한 것은 애플리케이션이 이해하는 HTTP 요청이에요.
    - id: d
      text: 모든 장치의 제조 번호
      feedback: 본문에서 L7과 연결한 것은 애플리케이션이 이해하는 HTTP 요청이에요.
    - id: e
      text: HTTP 요청처럼 애플리케이션이 이해하는 데이터
      feedback: 맞아요. Application Proxy는 HTTP처럼 애플리케이션 계층의 내용을 다룰 수 있어요.
    answer: e
  - id: u11-l01-p05-q02
    kind: choice
    difficulty: medium
    prompt: Application Proxy가 L5~L7과 연결된다는 말을 어떻게 이해해야 하나요?
    choices:
    - id: a
      text: 모든 프록시가 언제나 L5, L6, L7의 모든 내용을 해석한다
      feedback: 계층 이름은 기준을 보여 줄 뿐, 모든 제품의 기능을 보장하지는 않아요.
    - id: b
      text: 애플리케이션 수준 정보를 다루는 경우가 많다는 참고 구분이며 제품마다 기능은 다를 수 있다
      feedback: 맞아요. 계층 표기는 처리 수준을 가늠하는 참고이며 모든 제품이 동일하게 동작한다는 뜻은 아니에요.
    - id: c
      text: 프록시는 네트워크 계층을 사용하지 않는다
      feedback: 계층 이름은 기준을 보여 줄 뿐, 모든 제품의 기능을 보장하지는 않아요.
    - id: d
      text: Proxy와 OSI 계층은 서로 같은 이름이다
      feedback: 계층 이름은 기준을 보여 줄 뿐, 모든 제품의 기능을 보장하지는 않아요.
    - id: e
      text: 프록시는 항상 L2 프레임만 처리한다
      feedback: 계층 이름은 기준을 보여 줄 뿐, 모든 제품의 기능을 보장하지는 않아요.
    answer: b
- page_id: advanced-source-02-page-06
  questions:
  - id: u11-l01-p06-q01
    kind: choice
    difficulty: easy
    prompt: 패킷 수준 장치가 HTTP 내용을 분석하는 것은 가능한가요?
    choices:
    - id: a
      text: 가능할 수 있지만 여러 패킷을 모아 내용을 해석하는 추가 과정이 필요하다
      feedback: 맞아요. 패킷을 모아 조립하고 해석하면 가능할 수 있지만 추가 과정이 필요해요.
    - id: b
      text: 불가능하다. HTTP는 패킷에 실리지 않는다
      feedback: 본문은 패킷 수준 분석이 불가능하다고 하지 않고, 필요한 추가 작업이 있다고 설명해요.
    - id: c
      text: 가능하려면 반드시 DNS가 패킷을 삭제해야 한다
      feedback: 본문은 패킷 수준 분석이 불가능하다고 하지 않고, 필요한 추가 작업이 있다고 설명해요.
    - id: d
      text: 불가능하다. HTTP는 파일 이름과 같은 뜻이다
      feedback: 본문은 패킷 수준 분석이 불가능하다고 하지 않고, 필요한 추가 작업이 있다고 설명해요.
    - id: e
      text: 가능하려면 모든 패킷을 한 개로 바꾸어야 한다
      feedback: 본문은 패킷 수준 분석이 불가능하다고 하지 않고, 필요한 추가 작업이 있다고 설명해요.
    answer: a
  - id: u11-l01-p06-q02
    kind: choice
    difficulty: medium
    prompt: 새 네트워크 장치를 분류할 때 가장 좋은 질문 조합은 무엇인가요?
    choices:
    - id: a
      text: 장치가 비싼지 싼지, 오래됐는지 새것인지
      feedback: 본문이 제시한 분류 기준 두 가지를 함께 적용해 보세요.
    - id: b
      text: IP 주소가 짧은지 긴지, 화면이 큰지 작은지
      feedback: 본문이 제시한 분류 기준 두 가지를 함께 적용해 보세요.
    - id: c
      text: 장치가 경로 안인지 복사본 관찰인지, 그리고 패킷인지 소켓 Stream인지
      feedback: 맞아요. 경로에서의 위치와 처리 데이터 단위를 함께 살펴보면 복합 기능도 설명할 수 있어요.
    - id: d
      text: 제품 이름에 보안이라는 말이 있는지
      feedback: 본문이 제시한 분류 기준 두 가지를 함께 적용해 보세요.
    - id: e
      text: 회사 로고가 어느 색인지
      feedback: 본문이 제시한 분류 기준 두 가지를 함께 적용해 보세요.
    answer: c
---

## Inline·Out of path·Proxy

<!-- learn-page-id: advanced-source-02-page-01 -->

네트워크 장치를 처음 접하면 먼저 Inline, Out of path, Proxy 중 어떤 구조인지 살펴보는 것이 좋다. 한 장치가 여러 구조를 함께 가질 수도 있으므로 하나만 고집해 분류할 필요는 없다. Inline과 Out of path는 패킷 단위로, Proxy는 소켓의 Stream 수준으로 데이터를 다룬다는 차이가 있다.


이 세 이름은 장치가 통신 경로의 어디에 연결되는지, 그리고 어떤 단위로 데이터를 살펴보는지 설명하는 기준이다. **패킷**은 네트워크를 지나가도록 IP 정보 등이 붙은 전달 단위다. **소켓 Stream**은 TCP가 받은 바이트를 순서대로 애플리케이션에 건네는 연속된 흐름이다. 같은 데이터도 네트워크에서는 여러 패킷으로 오가고, 프로그램은 소켓에서 이어진 바이트 흐름으로 읽을 수 있다. 세 구조는 서로 완전히 배타적인 제품 종류가 아니므로 한 장치에 여러 특징이 함께 나타날 수도 있다.
## Inline · 통과와 차단

<!-- learn-page-id: advanced-source-02-page-02 -->

Inline 장치는 패킷이 통과하는 경로에 놓인다. 공기가 필터를 통과하는 모습에 비유할 수 있다. 장치는 패킷을 통과(Bypass)시키거나 버려(Drop) 차단할 수 있다. 출력 인터페이스(랜선이 연결된 출구 포트)가 여러 개라면 어느 방향으로 내보낼지도 선택한다. 라우터가 대표적인 Inline 장치다. Out of path도 패킷을 보지만, 직접 경로에서 통과·차단을 결정하는 대신 읽고 인지하는 것을 주목적으로 한다.


Inline은 필터가 길 한가운데 놓인 것과 같다. 통신이 이 장치를 지나가므로 장치는 규칙에 따라 패킷을 다음 장치로 전달(Bypass)하거나 버려(Drop) 통신을 막을 수 있다. 예를 들어 허용된 연결은 통과시키고 차단 규칙에 맞는 패킷은 버릴 수 있다. 여기서 Bypass는 패킷이 통과한다는 뜻으로 쓰며, 특정 제품의 장애 시 우회 기능과는 문맥에 따라 구별해야 한다.
## Out of path · 관찰과 수집

<!-- learn-page-id: advanced-source-02-page-03 -->

보안 문제를 알아내는 장치라면 보안 센서, 장애를 알아내는 장치라면 장애 대응 센서로 볼 수 있다. 이러한 센서는 보통 Out of path 구조로 연결한다. Tap 스위치 등으로 패킷을 복사받는 지점을 Tapping Point라고 하며, 복사한 데이터를 분석해 결과를 알린다. 반면 MP3, JPG, DOC 같은 파일 수준의 내용을 보려면 패킷 여러 개를 다시 조립해야 한다. 약 1MB에 패킷 1,000개, 10MB에 약 1만 개가 필요한 규모의 예를 든다. 이런 상위 데이터를 처리할 때 소켓의 Stream을 사용하는 Proxy가 유리하다. Proxy 역시 중간에서 데이터를 허용하거나 걸러낼 수 있다.


Out of path 센서는 원래 통신을 대신 처리하지 않고, 네트워크 장비가 복사해 준 패킷을 받아 살펴본다. 이 복사 지점을 Tapping Point(탭 지점)라고 부른다. TAP 장비나 스위치의 포트 미러링 기능을 이용해 복사본을 보낼 수 있다. 따라서 센서가 분석을 위해 원래 패킷의 전달 경로를 직접 이어받는 것은 아니다.

파일 크기와 패킷 수의 관계는 대략적인 감을 잡기 위한 계산이다. 1MB를 약 1,000KB, 패킷 하나에 실리는 데이터를 약 1KB로 단순화하면 약 1,000개의 패킷이 된다. 실제 패킷 크기와 헤더, 파일 크기에 따라 개수는 달라진다. 큰 파일 내용을 패킷 단위에서 확인하려면 관련 패킷을 모아 순서와 내용을 해석해야 한다.
## Proxy · Socket Stream 처리

<!-- learn-page-id: advanced-source-02-page-04 -->

Proxy는 대리자다. 애플리케이션의 Stream이 대리자를 지나가므로 전체 내용을 관찰하고 처리할 수 있다. 여기서는 User mode, Application, Proxy, Socket, Stream을 한 묶음으로 연결해 이해한다. TCP를 추상화한 소켓을 사용하는 애플리케이션 수준의 장치라는 뜻이다.


프록시(Proxy)는 한쪽 프로그램의 요청을 받아 상대편에 전달하고 응답을 되돌려 주는 중계 프로그램이다. 양쪽 연결을 각각 맺어 중계할 수 있으며, 소켓에서 TCP의 바이트 Stream을 읽는다. 이 덕분에 프록시는 HTTP 같은 애플리케이션 데이터를 패킷 경계에만 의존하지 않고 살펴볼 수 있다.

다만 Stream을 읽는다고 해서 언제나 파일 전체가 한꺼번에 준비되는 것은 아니다. 데이터가 도착하는 동안 일부씩 읽어 처리할 수도 있다. 핵심 차이는 프록시가 소켓을 통해 애플리케이션 데이터의 연속된 흐름을 다룬다는 점이다.
## 장치를 구조로 분류하기

<!-- learn-page-id: advanced-source-02-page-05 -->

이 관점에서 Application Proxy는 OSI의 L5~L7 수준과 연결된다. L7인 HTTP를 분석하려면 소켓 Stream을 직접 다루는 Proxy 구조가 편리하다. 장치 이름보다 어떤 단위의 데이터를 어느 위치에서 처리하는지 먼저 살펴보면 역할을 파악하기 쉽다.


OSI 계층 이름은 어느 수준의 정보를 다루는지 가늠하는 참고표다. Application Proxy는 보통 애플리케이션 계층(L7)의 HTTP 요청처럼 프로그램이 이해하는 내용을 살펴본다. 이는 프록시가 L5~L7과 연결된다는 뜻이지, 모든 프록시가 항상 모든 계층의 내용을 해석한다는 뜻은 아니다.
## 여러 구조가 결합되는 경우

<!-- learn-page-id: advanced-source-02-page-06 -->

패킷 수준에서 HTTP를 분석하는 것도 불가능한 것은 아니지만, 패킷 조립과 해석 등 추가 과정이 필요하다. 따라서 Inline·Out of path는 Packet과, User mode의 Application Proxy는 Socket·Stream과 연결해 기억하면 된다. 이후에는 각 구조의 구체적인 동작을 살펴본다. L2 프레임만을 다루는 특수한 사례는 이 과정에서 거의 다루지 않는다.


따라서 장치를 볼 때는 이름 하나로 단정하지 말고 두 질문을 해 보자. 장치가 원래 통신 경로 안에 있는가, 아니면 복사본을 받아 관찰하는가? 그리고 패킷을 보는가, 소켓 Stream의 애플리케이션 데이터를 보는가? 이 기준을 함께 적용하면 한 장치가 여러 기능을 결합한 경우도 구별할 수 있다.