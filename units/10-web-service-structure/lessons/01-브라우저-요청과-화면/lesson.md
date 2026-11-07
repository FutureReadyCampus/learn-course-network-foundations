---
id: u10-l01-web-browser-and-document
title: 브라우저는 요청을 받아 어떻게 화면을 만들까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-35.md
animations_dir: units/10-web-service-structure/lessons/01-브라우저-요청과-화면/assets/animations
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
wiki_diagram: units/10-web-service-structure/lessons/01-브라우저-요청과-화면/assets/diagrams/lesson-35.svg
page_metadata:
- terms:
  - 웹 서비스(Web Service)
  - 클라이언트(Client)
  - 웹 서버(Web Server)
  - WAS(Web Application Server)
  - 데이터베이스(Database, DB)
  - 요청(Request)
  - 응답(Response)
  question_placements:
  - question_id: u10-l01-p01-q01
    after_paragraph: 2
  - question_id: u10-l01-p01-q02
    after_paragraph: 4
  questions:
  - id: u10-l01-p01-q01
    kind: choice
    difficulty: easy
    prompt: 본문에서 설명한 HTTP와 TCP/IP의 역할 구분으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: HTTP가 도메인 이름을 IP 주소로 바꿉니다
      feedback: 이름을 IP 주소로 찾는 역할은 DNS가 합니다. HTTP는 웹 요청과 응답의 규칙입니다.
    - id: b
      text: TCP/IP가 GET 요청의 의미를 결정합니다
      feedback: GET 같은 요청의 의미는 HTTP가 표현하고, TCP/IP는 데이터를 전달합니다.
    - id: c
      text: HTTP는 요청·응답 규칙이고 TCP/IP는 데이터를 전달합니다
      feedback: 맞아요. 웹 요청의 의미와 네트워크 전달은 서로 다른 역할입니다.
    - id: d
      text: HTTP가 받은 HTML을 화면으로 직접 그립니다
      feedback: HTML을 해석해 화면을 만드는 일은 브라우저가 합니다. HTTP는 요청과 응답을 주고받는 규칙입니다.
    - id: e
      text: TCP/IP가 웹 페이지의 글자와 색을 정합니다
      feedback: 글자와 색의 표현은 HTML·CSS와 브라우저가 다룹니다. TCP/IP는 데이터를 전달합니다.
    answer: c
  - id: u10-l01-p01-q02
    kind: choice
    difficulty: medium
    prompt: 서버에 도착한 로그인 요청을 처리하는 일반적인 흐름은 무엇인가요?
    choices:
    - id: a
      text: 웹 서버가 요청을 받고 WAS에 넘기며 WAS가 필요한 DB 자료를 확인합니다
      feedback: 맞아요. 웹 서버가 요청을 받아 필요한 처리를 WAS에 맡기고, WAS가 DB 자료를 이용해 응답을 만들 수 있습니다.
    - id: b
      text: DNS가 요청을 받고 DB에 로그인 자료를 직접 기록합니다
      feedback: DNS는 사이트 이름에 대응하는 IP 주소를 찾습니다. 로그인 처리는 웹 서버와 WAS가 맡을 수 있습니다.
    - id: c
      text: 브라우저가 DB를 읽고 웹 서버에 완성된 응답을 보냅니다
      feedback: 본문에서는 서버 쪽 WAS가 DB를 조회하고 응답을 만든다고 설명합니다.
    - id: d
      text: DB가 먼저 브라우저에 요청을 보내고 WAS가 이를 전달합니다
      feedback: 흐름의 시작은 브라우저의 요청입니다. 서버가 이를 받아 처리합니다.
    - id: e
      text: TCP가 로그인 여부를 확인하고 웹 서버가 화면을 저장합니다
      feedback: TCP는 데이터 전달을 담당합니다. 로그인 판단은 애플리케이션 처리와 DB 자료를 이용할 수 있습니다.
    answer: a
  illustrations:
  - file: assets/animations/l35-daily-letter-and-envelope.svg
    title: 편지의 내용과 봉투
    alt: 나와 가게 사이에서 로그인 화면을 달라는 편지의 내용이 먼저 쓰이고, 봉투에 담겨 우체국을 지나 가게에 도착하며, 가게가 내용을 읽고 답장을 보냅니다. 내용을 쓰는 일과 나르는 일은 다르다고
      표시됩니다.
    caption: 편지의 내용과 봉투가 다르듯, HTTP 요청의 의미와 그것을 전달하는 네트워크의 역할은 서로 다른 층에 있습니다.
    after_paragraph: -1
  - file: assets/animations/l35-http-over-tcpip.svg
    title: HTTP 요청과 TCP/IP 전달
    alt: 브라우저가 GET /login 요청을 만들고, TCP/IP가 그 요청을 데이터로 감싸 네트워크를 지나 서버에 전달하며, 서버가 요청을 읽고 응답을 돌려보냅니다. 요청의 의미(HTTP)와
      전달(TCP/IP)은 서로 다른 층이라고 표시됩니다.
    caption: HTTP는 요청과 응답의 규칙이고 TCP/IP는 데이터를 전달합니다. 서버에 도착한 뒤의 웹 서버, WAS, DB 구조는 이어지는 페이지에서 살펴봅니다.
    after_paragraph: 3
- terms:
  - 도메인 이름(Domain Name)
  - DNS(Domain Name System)
  - IP 주소(IP Address)
  - 포트 번호(Port Number)
  - GET
  animations:
  - file: l35-browser-request-flow.svg
    title: 주소를 입력하면 일어나는 네 걸음
    alt: 브라우저가 주소 이름을 DNS에 물어 IP 주소를 받고, 서버와 TCP 선을 잇고, GET 편지를 보낸 뒤 HTML 문서를 돌려받아 화면에 표시하는 장면입니다.
    caption: 이름 찾기(DNS), 연결(TCP), 요청(GET), 응답(HTML) 순서로 문서가 도착합니다.
  question_placements:
  - question_id: u10-l01-p02-q01
    after_paragraph: 2
  - question_id: u10-l01-p02-q02
    after_paragraph: 3
  - question_id: u10-l01-p02-q03
    after_paragraph: 4
  questions:
  - id: u10-l01-p02-q01
    kind: choice
    difficulty: easy
    prompt: DNS가 도메인 이름을 조회해 돌려주는 것은 무엇인가요?
    choices:
    - id: a
      text: 요청한 웹 페이지의 HTML 내용
      feedback: DNS 조회는 페이지 내용을 가져오는 단계가 아닙니다. 서버를 찾을 IP 주소를 알아냅니다.
    - id: b
      text: 로그인에 성공했는지 나타내는 결과
      feedback: 로그인 결과는 애플리케이션이 처리합니다. DNS는 이름을 IP 주소로 찾습니다.
    - id: c
      text: 브라우저 화면의 CSS 규칙
      feedback: CSS는 웹 문서의 모양을 정합니다. DNS 응답에는 서버를 찾을 IP 주소가 담깁니다.
    - id: d
      text: 서버와 브라우저가 주고받을 GET 요청
      feedback: GET은 HTTP 요청의 한 종류입니다. DNS는 요청 전에 서버를 찾을 주소를 알아내는 데 쓰입니다.
    - id: e
      text: 사이트 서버를 찾아갈 IP 주소
      feedback: 맞아요. DNS는 이름에 대응하는 IP 주소를 찾아줍니다.
    answer: e
  - id: u10-l01-p02-q02
    kind: choice
    difficulty: medium
    prompt: 웹 접속에서 IP 주소와 포트 번호가 각각 가리키는 것은 무엇인가요?
    choices:
    - id: a
      text: IP 주소는 서비스를, 포트 번호는 컴퓨터를 가리킵니다
      feedback: 둘의 역할이 반대입니다. IP 주소는 컴퓨터를 찾고 포트 번호는 그 안의 통신 서비스를 구분합니다.
    - id: b
      text: IP 주소는 컴퓨터를, 포트 번호는 그 안의 통신 서비스를 가리킵니다
      feedback: 맞아요. 주소로 목적지 컴퓨터를 찾고 포트 번호로 그 컴퓨터의 통신 서비스를 구분합니다.
    - id: c
      text: IP 주소와 포트 번호는 모두 웹 페이지의 내용을 가리킵니다
      feedback: 두 값은 페이지 내용이 아니라 통신의 목적지를 찾고 구분하는 데 쓰입니다.
    - id: d
      text: IP 주소는 브라우저를, 포트 번호는 웹 문서의 색을 정합니다
      feedback: 브라우저 화면의 색은 CSS가 정합니다. IP 주소와 포트 번호는 목적지를 찾는 데 쓰입니다.
    - id: e
      text: IP 주소는 요청 종류를, 포트 번호는 응답 결과를 나타냅니다
      feedback: 요청 종류는 HTTP 메서드 등이 표현합니다. IP 주소와 포트 번호는 컴퓨터와 서비스를 구분합니다.
    answer: b
  - id: u10-l01-p02-q03
    kind: choice
    difficulty: medium
    prompt: 브라우저가 `GET /login` 요청에 대한 응답을 받았을 때, 그 응답에 포함될 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: 사이트 이름을 IP 주소로 바꾸는 DNS 질의만
      feedback: DNS 질의는 서버 주소를 찾는 단계입니다. HTTP 응답에는 처리 결과와 본문 등이 담길 수 있습니다.
    - id: b
      text: TCP 연결을 여는 SYN 신호만
      feedback: SYN은 TCP 연결 준비에 쓰입니다. 질문은 GET 요청 뒤 서버가 돌려주는 HTTP 응답입니다.
    - id: c
      text: 서버의 DB 테이블 전체
      feedback: 서버가 DB를 이용하더라도 전체 테이블을 응답으로 보내는 것은 아닙니다. 응답에는 상태 코드·헤더·본문이 포함될 수 있습니다.
    - id: d
      text: 상태 코드와 헤더, 화면을 구성할 HTML 본문
      feedback: 맞아요. 응답에는 상태 코드·헤더·본문이 들어갈 수 있고, 본문에 HTML 문서가 담길 수 있습니다.
    - id: e
      text: 브라우저가 화면에 그린 최종 이미지 파일
      feedback: 응답은 HTML 같은 자원을 보낼 수 있고, 브라우저가 이를 해석해 화면을 만듭니다.
    answer: d
  illustrations:
  - file: assets/animations/l35-daily-call-a-friend.svg
    title: 친구에게 전화하는 네 걸음
    alt: 나와 친구 사이에서 먼저 연락처에서 친구 이름에 맞는 전화번호를 찾고, 전화를 걸어 대표번호와 내선 번호로 통로를 잇고, 필요한 말을 건네고, 친구의 대답을 듣습니다.
    caption: 연락처에서 번호를 찾고, 연결하고, 말을 건네고, 대답을 듣는 것은 웹 접속의 네 걸음과 닮았습니다.
    after_paragraph: -1
  - file: assets/animations/l35-dns-tcp-get-response.svg
    title: 이름 찾기, 연결, 요청, 응답
    alt: 브라우저가 DNS에 shop.example의 IP 주소를 묻고 예시 주소 203.0.113.10을 받은 뒤, 웹 서버와 IP 주소와 포트로 TCP 연결을 준비하고, GET /login
      요청을 보내면 서버가 상태 코드와 헤더와 HTML 본문이 담긴 응답을 돌려줍니다.
    caption: DNS가 돌려주는 것은 서버를 찾을 주소이고, 이어서 연결 준비, 요청, 응답이 서로 다른 일로 이어집니다. 주소와 포트 번호는 예시입니다.
    after_paragraph: 3
- terms:
  - HTML(HyperText Markup Language)
  - CSS(Cascading Style Sheets)
  - 태그(Tag)
  question_placements:
  - question_id: u10-l01-p03-q01
    after_paragraph: 2
  - question_id: u10-l01-p03-q02
    after_paragraph: 3
  questions:
  - id: u10-l01-p03-q01
    kind: choice
    difficulty: easy
    prompt: HTML에서 `<h1>상품 목록</h1>`이 하는 일은 무엇인가요?
    choices:
    - id: a
      text: 문서에서 상품 목록을 제목으로 표시합니다
      feedback: 맞아요. HTML 태그는 문서 구조와 의미를 표시하며 h1은 제목입니다.
    - id: b
      text: 상품 보기라는 링크를 만듭니다
      feedback: 링크를 만드는 예는 a 태그입니다. h1 태그는 문서의 제목을 표시합니다.
    - id: c
      text: 본문 문단을 표시합니다
      feedback: 본문 문단을 나타내는 태그는 p입니다. h1은 제목을 표시합니다.
    - id: d
      text: 문서 안에 이미지를 넣습니다
      feedback: 이미지를 넣는 태그는 img입니다. h1은 제목을 표시하는 HTML 태그입니다.
    - id: e
      text: 사용자가 정보를 입력할 칸을 만듭니다
      feedback: 입력 칸은 input 같은 태그로 표시합니다. h1은 문서의 제목을 나타냅니다.
    answer: a
  - id: u10-l01-p03-q02
    kind: choice
    difficulty: medium
    prompt: 같은 HTML 문서에 다른 CSS를 적용하면 본문 설명대로 어떤 변화가 가능한가요?
    choices:
    - id: a
      text: CSS를 바꾸면 HTML 문장의 글자가 자동으로 바뀝니다
      feedback: CSS는 HTML의 글자 내용을 바꾸지 않습니다. 색·크기·간격 같은 모양을 정합니다.
    - id: b
      text: CSS를 바꾸면 링크가 가리키는 주소도 자동으로 바뀝니다
      feedback: 링크 주소는 HTML의 href에 담깁니다. CSS는 링크의 모양을 바꿀 수 있지만 목적지를 바꾸지는 않습니다.
    - id: c
      text: CSS 규칙이 바뀌면 h1 제목 태그가 p 문단 태그로 바뀝니다
      feedback: CSS는 HTML 태그의 의미나 구조를 바꾸지 않고, 그 구조를 표현하는 모양을 정합니다.
    - id: d
      text: 사이트의 IP 주소와 포트 번호가 달라집니다
      feedback: CSS는 네트워크 목적지를 바꾸지 않습니다. 브라우저의 문서 표현을 정합니다.
    - id: e
      text: 내용과 링크는 두고 색·크기·간격 같은 모양을 바꿀 수 있습니다
      feedback: 맞아요. CSS는 HTML 구조를 어떤 색·크기·간격·배치로 보여 줄지 정합니다.
    answer: e
  illustrations:
  - file: assets/animations/l35-daily-menu-content-style.svg
    title: 메뉴판의 내용과 모양
    alt: 메뉴판에 음식 이름과 가격이 적혀 있고, 모양 규칙 A를 입히면 제목이 크고 빨갛게 보이며, 모양 규칙 B로 바꿔도 내용은 그대로이고, 모양만으로 없던 메뉴가 생기지는 않는다고 표시됩니다.
    caption: 같은 메뉴판 내용도 모양 규칙에 따라 다르게 보일 수 있지만, 모양만으로 없던 내용이 생기지는 않습니다.
    after_paragraph: -1
  - file: assets/animations/l35-html-content-css-style.svg
    title: HTML은 구조, CSS는 모양
    alt: 같은 HTML의 제목과 링크에 CSS A를 적용하면 제목이 크고 파랗게, CSS B를 적용하면 작고 검게 보입니다. 내용과 링크는 그대로이며 CSS만으로 없던 상품 정보가 생기지는 않는다고
      표시됩니다.
    caption: HTML은 문서의 구조와 내용을, CSS는 그 구조를 표현하는 모양을 맡습니다. 그림의 색과 크기는 예시입니다.
    after_paragraph: 2
- terms:
  - JavaScript
  - 브라우저(Browser)
  - 렌더링(Rendering)
  question_placements:
  - question_id: u10-l01-p04-q01
    after_paragraph: 1
  - question_id: u10-l01-p04-q02
    after_paragraph: 3
  questions:
  - id: u10-l01-p04-q01
    kind: choice
    difficulty: easy
    prompt: 웹 페이지에 클릭이나 입력에 반응하는 동작을 더할 때 본문에서 든 기술은 무엇인가요?
    choices:
    - id: a
      text: CSS
      feedback: CSS는 색·크기·간격·배치 같은 모양을 정합니다. 클릭 반응은 JavaScript가 더할 수 있습니다.
    - id: b
      text: DNS
      feedback: DNS는 도메인 이름으로 IP 주소를 찾습니다. 화면 동작은 JavaScript가 더할 수 있습니다.
    - id: c
      text: HTTP
      feedback: HTTP는 요청과 응답을 주고받는 규칙입니다. 화면의 클릭 동작을 작성하는 기술은 JavaScript입니다.
    - id: d
      text: JavaScript
      feedback: 맞아요. JavaScript는 클릭이나 입력에 반응하는 동작을 더할 수 있습니다.
    - id: e
      text: SQL
      feedback: SQL은 데이터베이스에 자료를 질의할 때 쓰입니다. 브라우저 동작은 JavaScript가 더할 수 있습니다.
    answer: d
  - id: u10-l01-p04-q02
    kind: choice
    difficulty: medium
    prompt: 서버에서 JavaScript 파일을 내려받았다는 사실만으로 알 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: JavaScript가 반드시 서버에서 실행됐다는 것
      feedback: 내려받은 곳과 실행되는 곳은 다를 수 있습니다. 이 Lesson의 예에서는 브라우저가 JavaScript를 실행합니다.
    - id: b
      text: JavaScript가 브라우저에서 실행될 수 있으며, 다운로드 장소만으로 실행 장소를 단정할 수 없다는 것
      feedback: 맞아요. 파일을 받은 곳과 코드를 실행하는 곳은 구별해야 합니다.
    - id: c
      text: 서버가 브라우저의 HTML을 대신 렌더링했다는 것
      feedback: 브라우저는 HTML을 읽고 CSS를 적용해 화면을 배치합니다. 다운로드만으로 서버 렌더링을 단정할 수 없습니다.
    - id: d
      text: JavaScript가 데이터베이스에 저장된 계정 정보를 읽었다는 것
      feedback: 파일을 받았다는 사실만으로 DB 조회 여부는 알 수 없습니다. 본문은 실행 장소와 다운로드 장소를 구분합니다.
    - id: e
      text: HTML과 CSS가 더는 필요하지 않다는 것
      feedback: 본문은 HTML 구조와 CSS 모양에 JavaScript 동작이 더해질 수 있다고 설명합니다.
    answer: b
  illustrations:
  - file: assets/animations/l35-daily-kitchen-delivery.svg
    title: 배달된 재료를 내 주방에서
    alt: 재료 업체가 레시피 카드, 플레이팅 규칙, 반응 지침을 내 주방으로 보내고, 내 주방에서 레시피를 읽고 규칙대로 접시를 완성하며, 호출벨을 누르면 안내하는 반응 지침도 받은 곳이 아니라
      내 주방에서 실행됩니다. 사진 같은 자원은 따로 주문할 수 있습니다.
    caption: 받은 자원을 읽고 모양을 입히고 실행하는 일은 모두 내 주방에서 일어납니다. 다운로드한 곳과 실행되는 곳은 다릅니다.
    after_paragraph: -1
  - file: assets/animations/l35-browser-render-js-runs-here.svg
    title: 브라우저가 읽고 그리고 실행해요
    alt: 서버가 HTML, CSS, JavaScript를 보내면 브라우저가 HTML을 읽고 CSS를 적용해 화면을 그리고(렌더링), 버튼을 누르면 JavaScript가 서버가 아닌 브라우저에서
      실행되어 안내 문구를 보여 줍니다. 이미지 같은 외부 자원도 브라우저가 요청합니다.
    caption: JavaScript를 서버에서 내려받았다는 사실만으로 그 코드가 서버에서 실행되는 것은 아닙니다. 다운로드한 곳과 실행되는 곳은 구별해야 합니다.
    after_paragraph: 1
- terms:
  - 프런트엔드(frontend)
  - JSON
  - XML
  - JavaScript
  animations:
  - file: l36-json-to-screen.svg
    title: 자료를 받아 화면을 그리는 기기
    alt: 서버에서 같은 JSON 자료를 휴대폰과 PC에 보내고 각 기기가 화면을 그리는 장면입니다.
    caption: 서버가 자료를 보내면 브라우저가 화면을 만들 수 있습니다.
  question_placements:
  - question_id: u10-l02-p03-q01
    after_paragraph: 2
  - question_id: u10-l02-p03-q02
    after_paragraph: 4
  questions:
  - id: u10-l02-p03-q01
    kind: choice
    difficulty: easy
    prompt: 본문에서 JSON은 어떤 역할을 하는 자료인가요?
    choices:
    - id: a
      text: 프로그램 사이에서 상품 이름과 가격 같은 자료를 표현하는 형식입니다
      feedback: 맞아요. JSON은 프로그램 사이에 자료를 주고받기 쉬운 텍스트 표현 형식입니다.
    - id: b
      text: 웹 페이지의 글자 크기와 색을 지정하는 스타일 규칙입니다
      feedback: 글자 모양과 색은 CSS가 다룹니다. JSON은 자료를 표현합니다.
    - id: c
      text: 브라우저와 서버 사이의 네트워크 연결을 암호화하는 방식입니다
      feedback: 통신 암호화는 TLS가 맡습니다. JSON은 상품 이름이나 가격 같은 자료 형식입니다.
    - id: d
      text: 서버 안에서만 실행되는 Java 프로그램입니다
      feedback: JSON 자체는 실행 프로그램이 아니라 자료를 표현하는 텍스트 형식입니다.
    - id: e
      text: 휴대폰과 PC의 화면 배치를 자동으로 결정하는 프런트엔드 도구입니다
      feedback: 화면 배치는 브라우저의 코드와 스타일이 정합니다. JSON은 화면에 쓸 수 있는 자료를 담습니다.
    answer: a
  - id: u10-l02-p03-q02
    kind: choice
    difficulty: medium
    prompt: 같은 상품 JSON을 받은 휴대폰과 PC에서 화면 배치가 달라질 수 있는 이유는 무엇인가요?
    choices:
    - id: a
      text: JSON이 각 기기의 화면을 완성해 보내기 때문입니다
      feedback: JSON은 자료를 표현합니다. 화면을 구성하는 단계는 각 기기의 브라우저에서 일어날 수 있습니다.
    - id: b
      text: 서버가 기기마다 상품 가격을 반드시 다르게 저장하기 때문입니다
      feedback: 화면 배치가 다르다고 서버의 실제 상품 가격까지 달라지는 것은 아닙니다.
    - id: c
      text: 브라우저의 JavaScript와 CSS가 각 기기에서 자료를 읽고 화면을 구성할 수 있기 때문입니다
      feedback: 맞아요. 같은 자료를 받아도 각 기기의 브라우저가 화면을 만들고 배치할 수 있습니다.
    - id: d
      text: XML이 휴대폰의 화면을 그리고 JSON이 PC의 화면을 그리기 때문입니다
      feedback: JSON과 XML은 모두 자료 표현 형식입니다. 화면은 브라우저가 구성할 수 있습니다.
    - id: e
      text: HTTP가 화면 크기에 맞춰 상품 자료의 글자 크기를 바꾸기 때문입니다
      feedback: HTTP는 요청과 응답 규칙입니다. 본문은 브라우저가 자료를 화면으로 만드는 방식을 설명합니다.
    answer: c
  illustrations:
  - file: assets/animations/l36-daily-meal-kit-delivery.svg
    title: 완성품 배달과 밀키트 배달
    alt: 재료 업체가 완성된 요리를 보내면 내 주방에서 그대로 차리고, 재료와 조리법을 보내면 내 식탁에서 조립합니다. 두 방법 모두 널리 쓰이며, 내 식탁에서 바꿔도 업체의 실제 가격은 그대로입니다.
    caption: 누가 마지막 조립을 하는지가 다른 두 방식입니다. 둘 다 널리 쓰입니다.
    after_paragraph: -1
  - file: assets/animations/l36-html-vs-json-screen.svg
    title: HTML을 받거나 JSON을 받거나
    alt: 서버가 완성한 HTML 문서를 보내면 브라우저가 그대로 그리고, 서버가 JSON 자료를 보내면 브라우저의 JavaScript가 화면을 조립합니다. 두 방식 모두 널리 쓰이며 화면의 가격을
      바꿔도 서버의 실제 가격은 그대로입니다.
    caption: JSON을 받는다고 해서 특정 프레임워크가 반드시 필요한 것은 아닙니다. 서버가 HTML을 완성해 보내는 사이트도 널리 쓰입니다.
    after_paragraph: 2
---


핵심 개념을 주제별로 정리했다.

## 웹 접속 한 번, 아래층부터 되짚기

브라우저에서 `https://shop.example/login`을 열었다고 하자. 브라우저가 서버의 IP 주소를 알아내고 TCP 연결을 준비한 뒤 HTTP 요청을 보내는 흐름은 앞 단원에서 배웠다. 이 Lesson은 그 요청이 서버에 도착한 뒤 어떤 구성요소를 만나고, 응답이 어떻게 화면으로 이어지는지에 초점을 둔다.

하이퍼텍스트 전송 프로토콜(HTTP)은 브라우저와 웹 서버가 요청과 응답을 주고받는 규칙이다. 이 규칙이 TCP/IP 전달을 대신하는 것은 아니다. 편지를 쓸 때 내용과 봉투를 구별하듯, HTTP 요청의 의미와 그것을 전달하는 네트워크의 역할은 서로 다른 층에 있다. ([HTTP 요청·응답](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/9/lesson/4/page/1))

웹 페이지는 하나의 파일만으로 끝나지 않을 수 있다. HTML 문서가 CSS, JavaScript, 이미지 같은 다른 자원을 가리키면 브라우저는 그 자원도 요청한다. 그러므로 브라우저 화면은 서버에서 온 한 장의 완성된 사진이 아니라, 받은 문서와 자원을 브라우저가 해석해 만든 결과일 수 있다.

서버까지 온 요청도 곧바로 DB에 가는 것은 아니다. 앞단의 웹 서버가 요청을 받고, 애플리케이션 처리가 필요하면 WAS에 넘기며, WAS가 필요한 데이터를 DB에서 읽거나 기록한 뒤 응답을 만든다. 작은 서비스는 이 역할을 한 프로그램이나 한 장비가 함께 맡을 수도 있다. 구분은 역할을 이해하기 위한 지도다.

**기억할 흐름:** 브라우저가 요청을 만들고, 네트워크가 나르고, 서버의 프로그램이 처리해, 응답을 브라우저가 화면으로 만든다.

## 주소를 입력하면 일어나는 네 걸음

친구에게 전화하려면 먼저 연락처에서 번호를 찾고, 전화를 연결한 다음 말을 건넨다. 웹 접속에도 비슷하게 구분되는 단계가 있다. 주소창에 도메인 이름을 입력했다고 해서 그 문서가 즉시 화면에 나타나는 것은 아니다.

첫째, 브라우저는 도메인 이름 시스템(DNS)에 사이트 이름을 물어 인터넷 프로토콜(IP) 주소를 찾는다. 주소록에서 사람 이름에 연결된 전화번호를 찾는 것과 비슷하다. DNS가 돌려주는 것은 서버를 찾을 주소이며, 웹 페이지 내용 그 자체는 아니다. ([DNS 복습](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/9/lesson/1/page/1))

둘째, 브라우저는 서버와 전송 제어 프로토콜(TCP) 연결을 준비한다. IP 주소는 어느 컴퓨터로 보낼지 알려 주고, 포트 번호는 그 컴퓨터 안에서 어떤 통신 서비스를 찾아갈지 구분한다. 실제 연결 과정은 앞선 TCP 단원에서 다뤘으므로 여기서는 요청을 주고받을 통로를 마련한다고 이해하면 된다. ([TCP와 포트 복습](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/7/lesson/1/page/2))

셋째, 브라우저는 HTTP 요청을 보낸다. 예를 들어 로그인 화면을 가져올 때는 `GET /login`처럼 요청할 자원과 동작을 표시한다. 넷째, 서버는 처리 결과를 HTTP 응답으로 돌려준다. 응답에는 상태 코드, 헤더, 본문이 포함될 수 있고, 본문에는 화면을 구성할 HTML 문서가 담길 수 있다. ([URL·URI 복습](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/9/lesson/3/page/1), [HTTP 복습](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/9/lesson/4/page/1))

이 네 걸음은 설명을 위한 큰 흐름이다. 브라우저가 이미 주소를 알고 있거나 TCP 연결을 재사용하면 DNS 조회나 연결 준비를 매번 새로 하지 않을 수 있다. 핵심은 이름 찾기, 전달 통로 마련, 요청 보내기, 응답 받기를 서로 다른 일로 구별하는 것이다.

## 내용과 모양을 나누기: HTML과 CSS

웹 문서를 식당 메뉴판에 비유해 보자. 음식 이름과 가격처럼 무엇이 적혀 있는지가 내용이고, 글자 크기와 간격, 색처럼 어떻게 보이는지가 표현이다. 내용을 바꾸지 않고도 메뉴판의 글꼴이나 배치를 바꿀 수 있듯, 웹에서도 문서의 구조와 화면 표현을 나누어 관리할 수 있다.

하이퍼텍스트 마크업 언어(HTML)는 제목, 문단, 링크, 입력 칸처럼 문서의 구조와 의미를 태그로 표시한다. 예를 들어 `<h1>상품 목록</h1>`은 제목을 표시한다. `h1`은 가장 큰 제목을 나타내는 태그 이름이다. `<a href="/items/7">상품 보기</a>`에서 `a` 태그는 링크를 만들고, `href`에는 이동할 주소가 들어간다. HTML 태그는 화면의 픽셀을 직접 그리는 명령이라기보다 브라우저가 문서 구조를 이해하도록 붙이는 표지다.

캐스케이딩 스타일 시트(CSS)는 그 구조를 어떤 색·크기·간격·배치로 보여 줄지 정하는 규칙이다. 같은 HTML 문서에 다른 CSS를 적용하면 내용과 링크는 그대로 두고도 화면을 바꿀 수 있다. 반대로 CSS만으로 문서에 없던 상품 정보나 링크 목적지가 자동으로 생기지는 않는다.

HTML과 CSS를 따로 두면 내용 편집과 디자인 수정이 서로 덜 얽힌다. 예를 들어 제목 문구를 바꾸는 일과 모든 페이지의 제목 색을 바꾸는 일을 다른 파일에서 할 수 있다. 실제로 한 파일 안에 함께 작성할 수도 있지만, 이 Lesson에서는 각 기술의 역할 차이를 중심으로 기억한다.

**구별하기:** HTML은 문서의 구조와 내용, CSS는 그 구조를 표현하는 모양을 맡는다.

## 브라우저가 문서를 읽고 동작을 그리기

HTML과 CSS가 화면의 구조와 모양을 설명한다면, 자바스크립트(JavaScript)는 클릭이나 입력에 반응하는 동작을 더할 수 있다. 로그인 버튼을 눌렀을 때 입력값을 확인하고 서버에 요청을 보내거나, 검색창에 글자를 입력하는 동안 결과를 바꾸는 동작이 그 예다.

브라우저는 서버가 보낸 HTML을 읽어 태그의 구조를 파악하고 CSS 규칙을 적용해 화면을 배치한다. 마치 조리법을 읽고 재료를 순서대로 놓아 완성된 음식을 내듯, 문서와 모양 규칙을 읽어 화면을 그려 내는 과정을 렌더링(Rendering)이라고 한다. 브라우저는 이미지 같은 외부 자원도 요청해 페이지에 함께 표시할 수 있다.

JavaScript는 브라우저가 실행하는 코드다. 예를 들어 버튼을 눌렀을 때 화면에 안내 문구를 보여 주는 동작은 브라우저 안에서 일어날 수 있다. 서버에서 JavaScript 파일을 내려받았다는 사실만으로 그 코드가 서버에서 실행된다는 뜻은 아니다. **다운로드한 곳과 실행되는 곳은 구별해야 한다.**

간단히 정리하면, 서버는 HTML·CSS·JavaScript 같은 자원을 보낼 수 있고 브라우저는 문서를 읽고, 모양을 입히고, 코드를 실행해 화면과 동작을 만든다. 브라우저 구성요소의 내부 이름이나 실행 최적화는 찾아보기로 남기고, 지금은 HTML·CSS·JavaScript의 역할을 구분하자.

## 서버는 자료를 보내고 브라우저가 화면을 만들 수 있다

앞 Lesson에서는 서버가 완성한 HTML 문서를 보내고 브라우저가 화면에 그리는 방식을 보았다. 다른 방식에서는 서버가 자료를 보내고 각 기기의 브라우저가 화면을 만들기도 한다. 휴대폰과 PC에서 같은 쇼핑몰을 열어도 화면 배치는 다를 수 있다. 두 방식은 모두 쓰이며, 모든 웹 사이트가 같은 방법을 택하는 것은 아니다.

예를 들어 서버는 `{ "상품명": "사과", "가격": 1000 }`처럼 상품 이름과 가격을 JSON(JavaScript Object Notation)으로 보낼 수 있다. 중괄호 안에서 이름과 값이 짝을 이룬다. JSON은 프로그램 사이에서 자료를 주고받기 쉬운 텍스트 형식이다. XML(Extensible Markup Language)도 자료를 구조화해 표현하는 다른 형식이다. 둘은 자료를 나타내는 방법이지, 화면 모양이나 네트워크 연결 방식 자체는 아니다.

브라우저에서 실행되는 JavaScript는 응답 자료를 읽어 HTML 요소를 만들거나 바꾸고, CSS를 적용해 화면을 표시할 수 있다. React나 Vue 같은 프런트엔드 도구는 화면의 여러 부분을 구성하고 갱신하는 데 쓰일 수 있다. 하지만 JSON을 받은 모든 페이지에 특정 프레임워크가 필요한 것은 아니며, 서버가 HTML 문서를 완성해 보내는 웹 사이트도 지금 널리 사용된다.

여기서 프런트엔드(frontend)는 사용자의 기기에서 보이고 조작되는 화면 쪽의 코드와 자원을 가리킨다. WAS가 자료를 준비해 보냈다는 것과 브라우저가 그 자료를 화면으로 만들었다는 것은 서로 다른 단계다. 화면에서 보이는 가격을 바꿔도 서버의 실제 상품 가격이 자동으로 바뀌지는 않는다.

한 줄로 기억하면, **JSON과 XML은 자료를 표현하고, HTML·CSS·JavaScript는 브라우저 화면을 구성하고 움직이는 데 쓰일 수 있다.**
