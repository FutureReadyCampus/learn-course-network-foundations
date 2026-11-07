---
id: u10-l04-api-and-web-security
title: API 요청은 어떻게 보호되고 완성될까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-36.md
animations_dir: units/10-web-service-structure/lessons/04-api-요청과-웹-보안/assets/animations
additional_sources:
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/honja-network/05-2.md
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/honja-network/05-3.md
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-35.md
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-36.md
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-36.html#concept-basic-36-01
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-36.html#concept-basic-36-03
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-36.html#concept-basic-36-07
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-36.html#concept-basic-36-09
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-36.html#concept-basic-36-11
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-36.html#concept-basic-36-13
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-36.html#concept-basic-36-14
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/honja-network/07-2.md
wiki_diagram: units/10-web-service-structure/lessons/04-api-요청과-웹-보안/assets/diagrams/lesson-36.svg
page_metadata:
- terms:
  - API(Application Programming Interface)
  - URI(Uniform Resource Identifier)
  - CRUD(Create, Read, Update, Delete)
  - REST
  question_placements:
  - question_id: u10-l02-p04-q01
    after_paragraph: 2
  - question_id: u10-l02-p04-q02
    after_paragraph: 3
  - question_id: u10-l02-p04-q03
    after_paragraph: 4
  questions:
  - id: u10-l02-p04-q01
    kind: choice
    difficulty: easy
    prompt: GET /products/7에서 /products/7과 GET의 역할을 맞게 구분한 것은 무엇인가요?
    choices:
    - id: a
      text: /products/7은 응답 자료이고 GET은 서버 주소입니다
      feedback: URI와 메서드의 역할이 아닙니다. URI는 대상을 가리키고 메서드는 요청의 종류를 나타냅니다.
    - id: b
      text: /products/7은 데이터베이스이고 GET은 상품의 가격입니다
      feedback: 두 표현 모두 그 뜻이 아닙니다. 본문에서 URI는 자원을 식별하고 GET은 읽기 요청에 쓰입니다.
    - id: c
      text: /products/7은 화면의 제목이고 GET은 CSS 규칙입니다
      feedback: URI와 HTTP 메서드는 화면 스타일을 나타내지 않습니다. URI는 대상을, GET은 요청 동작을 표현합니다.
    - id: d
      text: /products/7은 상품 대상을 가리키는 URI이고 GET은 읽기 요청을 나타냅니다
      feedback: 맞아요. URI가 대상을 가리키고 HTTP 메서드가 요청의 종류를 나타냅니다.
    - id: e
      text: /products/7은 HTTP 메서드이고 GET은 상품 대상을 가리키는 URI입니다
      feedback: 둘의 역할을 서로 바꿔 썼습니다. `/products/7`은 URI이고 GET은 메서드입니다.
    answer: d
  - id: u10-l02-p04-q02
    kind: choice
    difficulty: medium
    prompt: CRUD라는 묶음은 무엇을 분류하는 데 쓰이나요?
    choices:
    - id: a
      text: 웹 서버, WAS, DB가 설치된 컴퓨터의 개수
      feedback: CRUD는 장비 수가 아니라 자료를 다루는 기본 작업을 묶어 부르는 말입니다.
    - id: b
      text: 자료를 만들기·읽기·바꾸기·삭제하기 같은 기본 작업
      feedback: 맞아요. CRUD는 Create, Read, Update, Delete의 기본 자료 작업을 가리킵니다.
    - id: c
      text: Java 코드가 바이트코드로 바뀌는 실행 단계
      feedback: 그것은 Java 실행 과정입니다. CRUD는 자료를 다루는 작업의 종류를 묶습니다.
    - id: d
      text: HTTP 연결을 암호화하고 복호화하는 순서
      feedback: 암호화는 TLS와 관련됩니다. CRUD는 자료에 수행하는 기본 작업을 뜻합니다.
    - id: e
      text: 브라우저가 화면 요소를 배치하고 색을 칠하는 과정
      feedback: 화면 표현은 프런트엔드 처리입니다. CRUD는 만들기·읽기·바꾸기·삭제하기를 분류합니다.
    answer: b
  - id: u10-l02-p04-q03
    kind: choice
    difficulty: medium
    prompt: REST 스타일의 기본 생각을 본문에 맞게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 주소에 모든 동작을 적고 HTTP 메서드는 사용하지 않습니다
      feedback: 본문은 자원을 URI로 가리키고 HTTP 메서드로 읽기나 만들기 같은 요청을 나타내는 방식을 설명합니다.
    - id: b
      text: 모든 API는 반드시 데이터베이스 테이블 이름을 URI로 써야 합니다
      feedback: 그런 규칙은 본문에 없습니다. REST의 기본 생각은 자원을 식별하고 HTTP의 표준 동작을 활용하는 것입니다.
    - id: c
      text: CRUD 작업마다 반드시 하나의 고정 HTTP 메서드만 사용할 수 있습니다
      feedback: 본문은 CRUD와 HTTP 메서드가 일대일로 고정되지 않는다고 설명합니다.
    - id: d
      text: URI 대신 JSON에 요청 대상과 동작을 모두 넣습니다
      feedback: 본문에서는 웹 API가 URI와 HTTP 메서드, 요청 자료를 사용할 수 있다고 설명합니다.
    - id: e
      text: URI로 자원을 가리키고 HTTP 메서드로 요청 동작을 표현합니다
      feedback: 맞아요. 다만 주소와 메서드만 맞춘다고 REST의 모든 원칙을 만족하는 것은 아닙니다.
    answer: e
  illustrations:
  - file: assets/animations/l36-daily-library-counter.svg
    title: 도서관 창구에서 요청하기
    alt: 손님이 도서관 창구에서 7번 서가의 책 정보를 조회하고 새 신청서를 내 새 처리를 요청합니다. 대상은 서가 번호로, 동작은 신청 종류로 나타내며 실제 처리는 도서관 안내문이 정한다고 표시됩니다.
    caption: 무엇을 대상으로 어떤 일을 할지 말하는 창구와 같이, API는 요청의 대상과 종류를 나타냅니다.
    after_paragraph: -1
  - file: assets/animations/l36-api-uri-method.svg
    title: URI는 대상, 메서드는 동작
    alt: 브라우저가 GET /products/7로 7번 상품 정보를 읽어 달라고 하고 POST /orders로 주문 자료를 보내 새 처리를 요청합니다. REST에서는 대상을 주소로, 동작을 메서드로
      나타내는 방식을 흔히 쓰고 /getProducts처럼 동작 이름을 주소에 넣는 설계도 볼 수 있으며, 실제 동작은 API 명세가 정합니다.
    caption: API는 URI와 HTTP 메서드, 요청 자료로 무엇을 요청하는지 나타냅니다. CRUD는 작업 분류이며 HTTP 메서드와 고정된 일대일 규칙은 아닙니다.
    after_paragraph: 1
- terms:
  - IPS(Intrusion Prevention System)
  - WAF(Web Application Firewall)
  - TLS(Transport Layer Security)
  - HTTPS
  - TLS 종료(TLS termination)
  animations:
  - file: l36-https-segments.svg
    title: HTTPS가 TLS 처리 장비에서 끝나는 한 가지 구성
    alt: 브라우저에서 보낸 비밀번호가 암호화되어 TLS 처리 장비까지 가고, 장비에서 복호화된 뒤 HTTP 평문으로 WAS에 전달되는 한 가지 구성을 보여 줍니다.
    caption: 이 그림은 브라우저에서 TLS 처리 장비까지만 암호화하고, 그 뒤에는 다시 암호화하지 않는 예입니다.
  question_placements:
  - question_id: u10-l02-p05-q01
    after_paragraph: 1
  - question_id: u10-l02-p05-q02
    after_paragraph: 3
  questions:
  - id: u10-l02-p05-q01
    kind: choice
    difficulty: easy
    prompt: IPS와 WAF의 검사 초점을 본문에 맞게 구분한 것은 무엇인가요?
    choices:
    - id: a
      text: IPS는 HTML 화면을 만들고 WAF는 계정 자료를 저장합니다
      feedback: 둘 다 본문에서 설명한 역할이 아닙니다. IPS와 WAF는 트래픽이나 웹 요청을 검사하는 보안 장비 범주입니다.
    - id: b
      text: IPS는 TLS 암호화만 하고 WAF는 도메인 이름을 IP 주소로 찾습니다
      feedback: TLS와 DNS의 역할을 IPS·WAF에 잘못 붙였습니다. 본문은 IPS의 트래픽 공격 징후 검사와 WAF의 HTTP 요청 검사 초점을 구분합니다.
    - id: c
      text: IPS는 네트워크 트래픽의 공격 징후를 살피고 WAF는 HTTP 요청 내용을 살핍니다
      feedback: 맞아요. IPS는 네트워크 트래픽을, WAF는 웹 요청 패턴과 내용을 살피는 데 초점을 둡니다.
    - id: d
      text: IPS는 Java 바이트코드를 실행하고 WAF는 Servlet을 관리합니다
      feedback: 이는 Java 실행 환경의 역할이지 보안 장비의 검사 초점이 아닙니다.
    - id: e
      text: IPS와 WAF는 항상 같은 장비에서만 동작하며 같은 내용을 검사합니다
      feedback: 본문은 장비의 종류와 배치가 구성에 따라 다를 수 있다고 설명하며, 두 검사 초점도 구분합니다.
    answer: c
  - id: u10-l02-p05-q02
    kind: choice
    difficulty: medium
    prompt: TLS 처리를 앞단 장비에서 끝내는 구성에 대한 설명으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 브라우저와 TLS 처리 지점 사이가 암호화되어도, 그 뒤 내부 구간은 별도로 암호화하지 않을 수 있습니다
      feedback: 맞아요. TLS가 어디서 처리되는지에 따라 보호 구간이 달라지므로 뒤쪽 구간도 확인해야 합니다.
    - id: b
      text: HTTPS가 주소창에 보이면 서버 내부의 모든 구간도 자동으로 암호화됩니다
      feedback: HTTPS 표시만으로 내부 전체 구간의 암호화를 보장하지 않습니다. 각 구간의 설정을 확인해야 합니다.
    - id: c
      text: TLS 처리 장비는 암호문을 복호화할 수 없으므로 요청을 전달하지 못합니다
      feedback: TLS를 처리하는 지점은 암호문을 복호화해 내용을 읽을 수 있습니다. 이후 구간의 설정은 별도로 정합니다.
    - id: d
      text: TLS 종료는 브라우저가 HTML 문서를 화면으로 바꾸는 단계입니다
      feedback: 화면 렌더링은 브라우저의 일입니다. TLS 종료는 TLS 암호화 처리를 맡는 지점과 관련됩니다.
    - id: e
      text: TLS 처리를 앞단에서 하면 WAS가 요청 내용을 절대 볼 수 없습니다
      feedback: 앞단에서 복호화한 뒤 요청이 내부로 전달될 수 있습니다. 내부 구간을 다시 암호화하는지는 구성에 달려 있습니다.
    answer: a
  illustrations:
  - file: assets/animations/l36-daily-locked-bag-route.svg
    title: 잠금 가방은 어디까지 갈까
    alt: 짐이 가방 검사대와 로비 데스크를 지나 사무실로 가고, 로비 데스크에서 가방을 열면 그 뒤는 열린 채일 수 있으며, 열고 나서 새 가방에 다시 잠그는 방법도 있습니다. 잠금 표시만으로
      모든 구간을 단정하면 안 된다고 표시됩니다.
    caption: 가방이 열리는 곳에 따라 보호되는 구간이 달라집니다.
    after_paragraph: -1
  - file: assets/animations/l36-tls-ends-where.svg
    title: TLS가 어디서 끝나는지 보기
    alt: 브라우저의 요청이 IPS·WAF 같은 보안 장비와 TLS 처리 장비를 지나 WAS로 갑니다. 구성 A는 장비까지만 TLS로 잠그고 그 뒤는 평문일 수 있으며, 구성 B는 장비에서 WAS까지
      다시 TLS로 암호화합니다. HTTPS 표시만으로 모든 내부 구간을 단정할 수 없습니다.
    caption: TLS를 처리하는 지점에 따라 보호되는 구간이 달라집니다. 장비의 종류와 배치는 제품과 네트워크 구성에 따라 다릅니다.
    after_paragraph: 2
- terms:
  - 클라이언트 검증(client-side validation)
  - 서버 검증(server-side validation)
  - SQL Injection(SQL 삽입 공격)
  question_placements:
  - question_id: u10-l02-p06-q01
    after_paragraph: 2
  - question_id: u10-l02-p06-q02
    after_paragraph: 3
  questions:
  - id: u10-l02-p06-q01
    kind: choice
    difficulty: easy
    prompt: 브라우저 입력 검증과 서버 검증을 함께 하는 이유로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 브라우저 검증만 통과하면 서버는 값을 다시 확인할 필요가 없습니다
      feedback: 브라우저의 코드는 사용자가 바꾸거나 우회할 수 있으므로 서버도 받은 값을 직접 검사해야 합니다.
    - id: b
      text: 서버 검증은 화면의 글자 색을 바꾸고 브라우저 검증은 DB를 수정합니다
      feedback: 두 검증의 역할이 아닙니다. 브라우저 검사는 입력 편의, 서버 검증은 처리할 값의 확인을 맡습니다.
    - id: c
      text: 서버는 브라우저에서 보내온 요청을 항상 신뢰해야 합니다
      feedback: 본문은 요청을 직접 만들거나 브라우저 코드를 바꿀 수 있으므로 서버가 입력을 확인해야 한다고 설명합니다.
    - id: d
      text: 브라우저 검증과 서버 검증은 같은 위치에서 같은 일을 합니다
      feedback: 두 검증은 위치와 역할이 다릅니다. 브라우저 검사는 사용을 돕고 서버 검증은 실제 처리를 지킵니다.
    - id: e
      text: 브라우저 검사는 입력 오류를 빨리 알려 주고 서버는 받은 값을 직접 검사합니다
      feedback: 맞아요. 브라우저 검사는 편의를 주지만 서버가 최종 입력값을 직접 확인해야 합니다.
    answer: e
  - id: u10-l02-p06-q02
    kind: choice
    difficulty: medium
    prompt: SQL Injection 위험을 줄이는 입력 처리 방식으로 본문이 권하는 것은 무엇인가요?
    choices:
    - id: a
      text: 입력값을 SQL 명령문에 그대로 이어 붙여 실행합니다
      feedback: 입력이 명령의 일부로 해석될 수 있어 위험한 방식이라고 본문에서 설명합니다.
    - id: b
      text: 입력값을 형식에 맞게 확인하고 자료와 SQL 명령을 분리해 전달합니다
      feedback: 맞아요. 입력을 검사하고 자료와 명령을 구분해 전달하는 안전한 방식을 사용해야 합니다.
    - id: c
      text: 입력값을 브라우저에서만 검사하고 서버에는 그대로 전달합니다
      feedback: 브라우저 검사는 우회될 수 있습니다. 서버가 직접 확인하고 질의에서 입력 자료를 명령과 분리해야 합니다.
    - id: d
      text: 모든 입력값을 DNS 서버에 저장한 뒤 데이터베이스를 조회합니다
      feedback: DNS는 이름을 IP 주소로 찾습니다. SQL Injection 대응은 입력값과 DB 명령을 안전하게 분리하는 문제입니다.
    - id: e
      text: 작은따옴표만 지우면 모든 입력값을 검사하지 않아도 됩니다
      feedback: 본문은 특수 기호 하나보다 입력을 명령과 구분하지 않고 처리하는 방식이 문제라고 설명합니다.
    answer: b
  illustrations:
  - file: assets/animations/l36-daily-reception-and-review.svg
    title: 접수 안내와 심사실
    alt: 접수 안내 창구는 빈 칸이나 글자 수를 바로 알려 주고, 창구를 거치지 않고 직접 낸 서류도 올 수 있어 심사실이 직접 확인합니다. 양식 칸과 쓴 내용을 섞지 않고 따로 다루며, 보관증
      번호도 심사실이 장부와 대조합니다.
    caption: 안내 창구는 편의를, 심사실은 처리를 지키는 최종 확인을 맡습니다.
    after_paragraph: -1
  - file: assets/animations/l36-browser-and-server-checks.svg
    title: 브라우저 검사와 서버 검증
    alt: 브라우저는 이름 길이와 나이 범위를 확인해 틀린 입력을 바로 알려 주지만, 직접 만든 요청도 서버에 올 수 있어 서버가 길이와 범위와 필수 항목을 다시 검사합니다. SQL은 명령과 입력
      자료를 분리해 다루고 이어 붙이지 않으며, 쿠키 값도 입력이라 서버가 세션 정보와 대조합니다.
    caption: 브라우저 검사는 사용을 편하게 하고 서버 검증은 실제 처리를 지킵니다.
    after_paragraph: 2
- terms:
  - 요청(Request)
  - 응답(Response)
  - 웹 서버(Web Server)
  - WAS(Web Application Server)
  - 데이터베이스(Database, DB)
  question_placements:
  - question_id: u10-l02-p07-q01
    after_paragraph: 1
  - question_id: u10-l02-p07-q02
    after_paragraph: 1
  questions:
  - id: u10-l02-p07-q01
    kind: choice
    difficulty: easy
    prompt: 로그인 규칙을 실행하는 서버 쪽 구성요소는 무엇인가요?
    choices:
    - id: a
      text: WAS
      feedback: 맞아요. WAS가 로그인 규칙 같은 프로그램 처리를 실행합니다.
    - id: b
      text: DNS
      feedback: DNS는 도메인 이름으로 서버의 IP 주소를 찾습니다. 로그인 규칙은 WAS가 실행합니다.
    - id: c
      text: DB
      feedback: DB는 계정 자료를 보관하거나 조회할 수 있습니다. 로그인 규칙의 실행은 WAS가 맡습니다.
    - id: d
      text: 웹 서버
      feedback: 웹 서버는 요청을 받고 필요한 프로그램 처리를 WAS에 넘길 수 있습니다.
    - id: e
      text: 브라우저
      feedback: 브라우저는 요청을 보내고 응답을 화면에 표시합니다. 서버 쪽 로그인 규칙은 WAS가 실행합니다.
    answer: a
  - id: u10-l02-p07-q02
    kind: choice
    difficulty: medium
    prompt: 로그인 요청이 처리되어 화면에 돌아오는 흐름으로 본문에 가장 잘 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 브라우저 → DB → 웹 서버 → DNS → WAS → 브라우저
      feedback: 브라우저는 DB에 직접 요청하지 않습니다. 웹 서버가 요청을 받고 WAS가 필요한 자료를 DB에서 조회합니다.
    - id: b
      text: 브라우저 → WAS → DB → DNS → 웹 서버 → 브라우저
      feedback: 본문에서는 웹 서버가 요청을 먼저 받고 필요한 프로그램 처리를 WAS에 넘깁니다.
    - id: c
      text: 브라우저 → 웹 서버 → DB → WAS → DNS → 브라우저
      feedback: 흐름의 역할 순서가 맞지 않습니다. WAS가 요청 처리를 맡고 필요한 DB 자료를 확인합니다.
    - id: d
      text: 브라우저 → DNS로 주소 확인 → 네트워크 → 웹 서버 → WAS → DB 조회 → 응답 반환
      feedback: 맞아요. 이름과 연결을 준비한 뒤 웹 서버가 요청을 받고 WAS가 DB 자료를 확인해 응답을 만듭니다.
    - id: e
      text: 브라우저 → DNS로 주소 확인 → DB → 웹 서버 → WAS → 응답 반환
      feedback: DNS는 서버 주소를 찾고 브라우저는 네트워크를 통해 웹 서버에 요청합니다. DB는 WAS가 필요한 자료를 조회할 때 사용합니다.
    answer: d
  illustrations:
  - file: assets/animations/l36-daily-reservation-call.svg
    title: 식당 예약 전화로 이어 보기
    alt: 손님이 전화번호부에서 식당 번호를 찾아 전화를 연결해 주문을 전하고, 홀이 받아 주방이 만들며 창고에서 재료를 꺼내 확인하고, 완성된 요리가 손님 식탁으로 돌아옵니다. 잠금 가방이 어디서
      열리는지에 따라 보호 구간이 달라질 수 있다고 표시됩니다.
    caption: 로그인 한 번이 식당 예약 전화와 같은 길을 지납니다. 홀은 웹 서버, 주방은 WAS, 창고는 DB에 빗댈 수 있습니다.
    after_paragraph: -1
  - file: assets/animations/l36-login-end-to-end.svg
    title: 로그인 요청 하나로 전체 흐름 잇기
    alt: 브라우저가 DNS로 서버의 IP 주소를 찾고, TCP/IP로 연결해 HTTP 요청을 보내면, 웹 서버가 받고 WAS가 입력을 확인해 DB에서 자료를 조회한 뒤, 응답으로 HTML 또는
      JSON이 돌아와 브라우저가 화면을 만듭니다. HTTPS여도 TLS를 처리하는 지점에 따라 보호 구간이 달라집니다.
    caption: 로그인 요청 하나에 DNS, TCP/IP, HTTP, 웹 서버, WAS, DB, 응답과 화면까지의 흐름이 이어집니다.
    after_paragraph: 1
---


핵심 개념을 주제별로 정리했다.

## API는 기능을 요청하는 약속된 창구다

쇼핑몰 화면에서 상품 목록을 열거나 주문을 저장할 때 브라우저는 서버에 요청을 보낸다. 프로그램이 다른 프로그램에 기능이나 자료를 요청하는 데 사용하는 약속된 접점을 API(Application Programming Interface)라고 한다. 웹 API는 보통 URI와 HTTP 메서드, 요청 자료를 사용해 무엇을 요청하는지 나타내고, 서버는 정해 둔 규칙에 따라 응답한다.

URI(Uniform Resource Identifier)는 웹에서 자원이나 기능 대상을 식별하는 이름이다. 예를 들어 `/products/7`은 7번 상품을 가리키는 URI로 정할 수 있다. 같은 주소라도 메서드와 요청 내용이 다르면 서버가 다르게 처리할 수 있다. `GET /products/7`은 그 상품 정보를 읽어 달라는 요청, `POST /orders`는 주문 자료를 보내 새 주문 처리를 요청하는 사례가 될 수 있다. 실제 동작은 각 서비스가 정한 API 명세에 따라 달라진다.

자료를 다루는 기본 작업은 CRUD로 묶어 부르기도 한다. Create는 만들기, Read는 읽기, Update는 바꾸기, Delete는 삭제하기다. 화면의 상품 조회는 Read, 주문 등록은 Create에 가까운 예다. CRUD는 데이터 작업을 분류하는 말이고, HTTP 메서드와 반드시 일대일로 고정되는 규칙은 아니다. 어떤 요청을 어떤 메서드로 처리할지는 API 설계가 정한다.

REST(Representational State Transfer)는 웹 자원을 식별하고 HTTP의 표준 동작을 활용하는 설계 방식이다. 예를 들어 `GET /products`처럼 주소에 상품이라는 대상을 두고, `GET`으로 읽기를 요청할 수 있다. `/getProducts`처럼 주소에 동작 이름을 넣는 설계도 볼 수 있지만, REST 스타일에서는 자원을 주소로 가리키고 HTTP 메서드로 읽기·만들기 같은 동작을 나타내는 방식을 흔히 사용한다. 주소와 메서드만 이렇게 정했다고 해서 REST의 모든 원칙을 지킨 것은 아니다. 여기서는 이 기본 생각만 기억하고 더 자세한 설계 조건은 찾아보기로 남긴다.

한 줄로 기억하면, **API는 프로그램이 요청하고 응답받는 접점이고, URI는 대상을 가리키며 메서드는 요청의 종류를 나타낸다.**

## 보안 장비와 HTTPS는 어느 구간을 보호할까?
<!-- learn-page-id: https-section -->

브라우저가 보낸 요청은 서버에 도착하기 전에 여러 장비를 지날 수 있다. IPS(Intrusion Prevention System, 침입 방지 시스템)는 네트워크 트래픽에서 알려진 공격 징후를 살펴 차단하는 장비 범주다. WAF(Web Application Firewall, 웹 애플리케이션 방화벽)는 HTTP 요청의 내용과 웹 요청 패턴을 검사하는 데 초점을 둔다. 장비의 배치와 기능은 제품과 네트워크 구성에 따라 다르다.

HTTPS는 HTTP를 TLS(Transport Layer Security)로 보호해 전송하는 방식이다. TLS는 통신 구간에서 내용을 암호화하고 통신 상대를 확인하는 데 쓰인다. 브라우저와 서버 사이에 전달 장비가 있어도, 어느 지점에서 TLS를 처리하는지에 따라 실제 보호 구간이 달라질 수 있다.

예를 들어 앞단의 부하 분산 장비나 프록시가 TLS 처리를 맡으면 그 지점에서 암호문을 복호화(암호화된 내용을 읽을 수 있는 형태로 되돌림)할 수 있다. 이후 서버까지 다시 TLS로 암호화할 수도 있고, 내부 구간에서 별도 암호화를 하지 않을 수도 있다. 그러므로 브라우저 주소창에 HTTPS가 보인다는 사실만으로 모든 내부 구간이 같은 방식으로 암호화되어 있다고 단정할 수 없다. 전체 경로와 각 구간의 설정을 확인해야 한다.

IPS·WAF·TLS 처리를 맡는 장비의 종류와 배치 원리는 보안 심화 과정에서 더 살펴본다. 여기서는 **보안 장비가 어디에 있고 TLS가 어디서 끝나는지에 따라 보호 범위를 따로 확인해야 한다**는 점을 기억하자.

## 입력은 브라우저와 서버에서 각각 확인한다

회원 가입 화면이 이름과 나이를 받는다고 해 보자. 브라우저에서 글자 수나 입력 형식을 확인하면 사용자가 잘못 입력했을 때 바로 알려 줄 수 있다. 이런 클라이언트 검증은 편리하지만, 입력을 최종적으로 믿어도 된다는 뜻은 아니다.

브라우저에서 실행되는 JavaScript는 사용자의 기기에서 동작한다. 사용자는 화면을 거치지 않고 요청을 직접 만들거나, 브라우저 안의 코드를 바꿀 수 있다. 따라서 서버는 이름 길이, 나이 범위, 필수 항목 여부 등을 요청을 받을 때 직접 검사해야 한다. 브라우저 검사는 입력을 돕고, 서버 검증은 서버가 처리할 값을 판단하는 경계다.

서버가 사용자 입력을 데이터베이스 명령문에 그대로 이어 붙이면 SQL Injection(SQL 삽입 공격)이 생길 수 있다. 예를 들어 입력값의 작은따옴표가 데이터베이스 명령의 경계를 바꾸도록 문자열을 이어 붙이면, 입력 자료가 명령의 일부로 해석될 수 있다. 문제는 특수 기호 자체가 아니라 입력을 명령과 구분하지 않고 처리하는 데 있다. 입력값을 길이와 형식에 맞게 검사하고, 데이터베이스 질의에서는 입력 자료와 명령을 분리하는 안전한 방식을 사용해야 한다.

쿠키 값도 사용자의 브라우저에서 요청과 함께 올 수 있으므로 서버가 확인해야 하는 입력이다. 페이지 앞에서 본 로그인 예에서는 브라우저에 저장된 값만으로 로그인 권한을 결정하지 않고, 서버가 자신이 관리하는 세션 정보와 요청을 확인한다.

한 줄로 기억하면, **브라우저 검사는 사용을 편하게 하고 서버 검증은 실제 처리를 지킨다.**

## 로그인 요청으로 기본편의 흐름을 연결하기

이제 로그인 요청 하나를 전체 과정에 놓아 보자. 사용자는 URL을 입력하고, 브라우저는 DNS로 서버의 IP 주소를 알아낸 뒤 네트워크 연결을 준비한다. HTTP 요청은 TCP/IP를 통해 서버에 전달된다. 웹 서버는 요청을 받고, 프로그램 처리가 필요하면 WAS에 넘긴다. WAS는 입력을 검증하고 필요한 자료를 DB에서 조회한 뒤 응답을 만든다. 응답이 브라우저에 돌아오면 브라우저는 HTML을 읽고 필요한 화면을 표시한다.

클라이언트와 서버는 요청을 주고받는 양 끝이고, 링크와 IP는 데이터를 네트워크를 통해 옮긴다. TCP와 UDP는 프로그램 사이에서 데이터를 전달하며, URL·DNS·HTTP는 웹 요청의 주소와 이름 찾기, 메시지 규칙을 다룬다. 그리고 이번 웹 서비스 단원에서는 요청이 서버 안의 역할을 거쳐 결과가 되는 과정을 연결했다. 서버는 HTML 문서를 돌려줄 수도 있고, JSON 같은 자료를 보내 브라우저가 화면을 만들도록 할 수도 있다. HTTPS를 사용해도 TLS를 처리하는 지점에 따라 보호되는 구간이 달라질 수 있다. 더 살펴보고 싶다면 [패킷 전달](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/4/lesson/4/page/1), [TCP와 포트](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/7/lesson/1/page/2), [DNS](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/9/lesson/1/page/1), [URL·URI](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/9/lesson/3/page/1), [HTTP](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/9/lesson/4/page/1) 페이지를 다시 볼 수 있다.

**기억하기 (Recall)**

- 웹 서버는 요청을 접수하고, WAS는 프로그램 처리를 실행하며, DB는 자료를 보관한다.
- API 요청은 URI로 대상을 가리키고 HTTP 메서드와 자료로 동작을 표현할 수 있다.
- 브라우저 검증과 서버 검증은 역할이 다르며, 서버는 받은 값을 직접 확인해야 한다.

**적용하기 (Apply)**

- 로그인 화면에서 입력한 값이 브라우저, 네트워크, 웹 서버, WAS, DB를 거쳐 응답으로 돌아오는 순서를 그려 본다.
- 화면이 늦을 때 APM 관측 자료로 네트워크, WAS 처리, DB 대기 중 어디의 시간이 긴지 살펴본다.

**찾아보기 (Lookup)**

- 실제 서비스의 웹 서버·WAS·DB 배치와 API 동작은 해당 서비스의 구성도와 API 문서를 확인한다.
- JVM과 Servlet 컨테이너의 구체적 실행 설정은 제품 문서에서 찾아본다. VPN과 네트워크 보안 솔루션을 다루는 심화 과정에서는 보안 장비의 배치와 역할을 더 살펴본다.
