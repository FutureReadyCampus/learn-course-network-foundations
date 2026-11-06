---
id: u6-l35-그림-한-장으로-외워서-끝내는-웹-서비스-구조-기본이론
title: 웹 서버·WAS·DB는 어떻게 나누어 일할까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-35.md
animations_dir: units/06-web-fundamentals/lessons/05-그림-한-장으로-외워서-끝내는-웹-서비스-구조-기본이론/assets/animations
additional_sources:
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/honja-network/05-2.md
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/honja-network/05-3.md
- https://github.com/FutureReadyCampus/course-network/blob/9acf72edc7c9e0f21fcc98cc31eb637750e26926/studio/wiki/oeweo-network/lesson-35.md
wiki_diagram: units/06-web-fundamentals/lessons/05-그림-한-장으로-외워서-끝내는-웹-서비스-구조-기본이론/assets/diagrams/lesson-35.svg
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
    title: "편지의 내용과 봉투"
    alt: "나와 가게 사이에서 로그인 화면을 달라는 편지의 내용이 먼저 쓰이고, 봉투에 담겨 우체국을 지나 가게에 도착하며, 가게가 내용을 읽고 답장을 보냅니다. 내용을 쓰는 일과 나르는 일은 다르다고 표시됩니다."
    caption: "편지의 내용과 봉투가 다르듯, HTTP 요청의 의미와 그것을 전달하는 네트워크의 역할은 서로 다른 층에 있습니다."
    after_paragraph: 1
  - file: assets/animations/l35-http-over-tcpip.svg
    title: "HTTP 요청과 TCP/IP 전달"
    alt: "브라우저가 GET /login 요청을 만들고, TCP/IP가 그 요청을 데이터로 감싸 네트워크를 지나 서버에 전달하며, 서버가 요청을 읽고 응답을 돌려보냅니다. 요청의 의미(HTTP)와 전달(TCP/IP)은 서로 다른 층이라고 표시됩니다."
    caption: "HTTP는 요청과 응답의 규칙이고 TCP/IP는 데이터를 전달합니다. 서버에 도착한 뒤의 웹 서버, WAS, DB 구조는 이어지는 페이지에서 살펴봅니다."
    after_paragraph: 3
  illustration_after_paragraph: [-1]
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
    title: "친구에게 전화하는 네 걸음"
    alt: "나와 친구 사이에서 먼저 연락처에서 친구 이름에 맞는 전화번호를 찾고, 전화를 걸어 대표번호와 내선 번호로 통로를 잇고, 필요한 말을 건네고, 친구의 대답을 듣습니다."
    caption: "연락처에서 번호를 찾고, 연결하고, 말을 건네고, 대답을 듣는 것은 웹 접속의 네 걸음과 닮았습니다."
    after_paragraph: 0
  - file: assets/animations/l35-dns-tcp-get-response.svg
    title: "이름 찾기, 연결, 요청, 응답"
    alt: "브라우저가 DNS에 shop.example의 IP 주소를 묻고 예시 주소 203.0.113.10을 받은 뒤, 웹 서버와 IP 주소와 포트로 TCP 연결을 준비하고, GET /login 요청을 보내면 서버가 상태 코드와 헤더와 HTML 본문이 담긴 응답을 돌려줍니다."
    caption: "DNS가 돌려주는 것은 서버를 찾을 주소이고, 이어서 연결 준비, 요청, 응답이 서로 다른 일로 이어집니다. 주소와 포트 번호는 예시입니다."
    after_paragraph: 3
  illustration_after_paragraph: [-1]
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
    title: "메뉴판의 내용과 모양"
    alt: "메뉴판에 음식 이름과 가격이 적혀 있고, 모양 규칙 A를 입히면 제목이 크고 빨갛게 보이며, 모양 규칙 B로 바꿔도 내용은 그대로이고, 모양만으로 없던 메뉴가 생기지는 않는다고 표시됩니다."
    caption: "같은 메뉴판 내용도 모양 규칙에 따라 다르게 보일 수 있지만, 모양만으로 없던 내용이 생기지는 않습니다."
    after_paragraph: 0
  - file: assets/animations/l35-html-content-css-style.svg
    title: "HTML은 구조, CSS는 모양"
    alt: "같은 HTML의 제목과 링크에 CSS A를 적용하면 제목이 크고 파랗게, CSS B를 적용하면 작고 검게 보입니다. 내용과 링크는 그대로이며 CSS만으로 없던 상품 정보가 생기지는 않는다고 표시됩니다."
    caption: "HTML은 문서의 구조와 내용을, CSS는 그 구조를 표현하는 모양을 맡습니다. 그림의 색과 크기는 예시입니다."
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
    title: "배달된 재료를 내 주방에서"
    alt: "재료 업체가 레시피 카드, 플레이팅 규칙, 반응 지침을 내 주방으로 보내고, 내 주방에서 레시피를 읽고 규칙대로 접시를 완성하며, 호출벨을 누르면 안내하는 반응 지침도 받은 곳이 아니라 내 주방에서 실행됩니다. 사진 같은 자원은 따로 주문할 수 있습니다."
    caption: "받은 자원을 읽고 모양을 입히고 실행하는 일은 모두 내 주방에서 일어납니다. 다운로드한 곳과 실행되는 곳은 다릅니다."
    after_paragraph: 1
  - file: assets/animations/l35-browser-render-js-runs-here.svg
    title: "브라우저가 읽고 그리고 실행해요"
    alt: "서버가 HTML, CSS, JavaScript를 보내면 브라우저가 HTML을 읽고 CSS를 적용해 화면을 그리고(렌더링), 버튼을 누르면 JavaScript가 서버가 아닌 브라우저에서 실행되어 안내 문구를 보여 줍니다. 이미지 같은 외부 자원도 브라우저가 요청합니다."
    caption: "JavaScript를 서버에서 내려받았다는 사실만으로 그 코드가 서버에서 실행되는 것은 아닙니다. 다운로드한 곳과 실행되는 곳은 구별해야 합니다."
    after_paragraph: 2
- terms:
  - HTTP 메서드(Method)
  - GET
  - POST
  - 요청(Request)
  - 응답(Response)
  question_placements:
  - question_id: u10-l01-p05-q01
    after_paragraph: 2
  - question_id: u10-l01-p05-q02
    after_paragraph: 3
  questions:
  - id: u10-l01-p05-q01
    kind: choice
    difficulty: easy
    prompt: 본문에서 GET과 POST의 흔한 용도를 어떻게 구분하나요?
    choices:
    - id: a
      text: GET은 보통 자료를 제출하고 POST는 정보를 가져옵니다
      feedback: 두 메서드의 흔한 용도를 서로 바꿔 쓴 설명입니다. GET은 정보를 가져오고 POST는 자료 제출이나 처리를 요청할 때 자주 씁니다.
    - id: b
      text: GET은 로그인 상태를 저장하고 POST는 DNS를 조회합니다
      feedback: 두 메서드의 용도는 로그인 상태 저장이나 이름 조회가 아니라 자원에 대한 요청 동작입니다.
    - id: c
      text: GET은 정보를 가져올 때, POST는 자료를 제출하거나 처리를 요청할 때 흔히 씁니다
      feedback: 맞아요. GET은 정보를 가져올 때, POST는 입력 자료를 제출하거나 처리를 요청할 때 자주 쓰입니다.
    - id: d
      text: GET은 자원 주소를 정하고 POST는 서버 포트를 정합니다
      feedback: 주소와 포트는 목적지를 구분하는 정보입니다. GET과 POST는 요청 메서드입니다.
    - id: e
      text: GET과 POST는 서버가 처리한 뒤 보내는 응답의 종류입니다
      feedback: GET과 POST는 응답 종류가 아니라 브라우저가 보내는 HTTP 요청 메서드입니다.
    answer: c
  - id: u10-l01-p05-q02
    kind: choice
    difficulty: medium
    prompt: POST 요청을 받았을 때 서버 안에서 실제로 어떤 처리를 할지는 무엇이 정하나요?
    choices:
    - id: a
      text: POST는 항상 새 계정이나 새 주문을 저장하도록 정합니다
      feedback: POST는 흔히 자료를 제출하지만, 실제 처리는 서비스마다 다릅니다.
    - id: b
      text: POST는 모든 사이트에서 로그인 확인만 실행하도록 정합니다
      feedback: POST를 로그인에 쓸 수 있지만 주문이나 댓글 등 다른 처리를 할 수도 있습니다.
    - id: c
      text: POST는 기존 자료를 항상 수정하도록 정합니다
      feedback: POST가 어떤 결과를 만드는지는 서버가 구현한 처리에 달려 있습니다.
    - id: d
      text: 포트 번호가 POST 요청의 로그인·주문 처리를 선택합니다
      feedback: 포트 번호는 통신 서비스를 찾습니다. 요청을 어떤 업무로 처리할지는 서비스의 서버가 정합니다.
    - id: e
      text: 사이트의 서버가 POST 요청을 어떻게 처리하도록 만들었는지가 정합니다
      feedback: 맞아요. POST는 흔한 요청 방식이고, 로그인 확인이나 주문 저장처럼 구체적인 처리는 서버가 정합니다.
    answer: e
  illustrations:
  - file: assets/animations/l35-daily-two-counters.svg
    title: "조회 창구와 접수 창구"
    alt: "나는 조회 창구에서 목록을 보여 달라고 하여 서류를 받고, 접수 창구에서는 내가 쓴 서류를 내면 우체국이 확인해 처리한 뒤 승인 또는 반려를 알려 줍니다."
    caption: "목록을 보는 일과 내가 쓴 서류를 내서 처리하는 일은 다르며, 어떻게 처리할지는 받는 쪽이 정합니다."
    after_paragraph: 0
  - file: assets/animations/l35-get-vs-post.svg
    title: "GET은 가져오기, POST는 제출"
    alt: "브라우저가 GET /items로 문서를 가져오고, POST /login으로 입력 내용을 제출하면 서버가 입력을 확인해 처리한 뒤 성공 화면이나 오류 안내를 응답합니다."
    caption: "GET은 자료를 가져올 때, POST는 자료를 제출하거나 처리를 요청할 때 흔히 쓰이며 정확한 동작은 서버가 정합니다."
    after_paragraph: 2
- page_id: http-stateless
  terms:
  - 무상태(Stateless)
  - 쿠키(Cookie)
  - Set-Cookie
  - Cookie 헤더
  question_placements:
  - question_id: u10-l01-p06-q01
    after_paragraph: 2
  - question_id: u10-l01-p06-q02
    after_paragraph: 3
  - question_id: u10-l01-p06-q03
    after_paragraph: 6
  questions:
  - id: u10-l01-p06-q01
    kind: choice
    difficulty: easy
    prompt: HTTP가 무상태(stateless)라는 설명은 무엇을 뜻하나요?
    choices:
    - id: a
      text: 웹 서버는 어떤 정보도 저장할 수 없습니다
      feedback: 무상태는 서버가 저장을 못 한다는 뜻이 아닙니다. HTTP 요청에 이전 대화가 자동으로 이어지지 않는다는 뜻입니다.
    - id: b
      text: 각 HTTP 요청에 앞선 요청의 대화 내용이 자동으로 붙지 않습니다
      feedback: 맞아요. HTTP 요청 하나가 끝나면 다음 요청이 앞서 주고받은 내용을 자동으로 기억하지 않습니다.
    - id: c
      text: 브라우저는 한 번에 요청을 하나만 보낼 수 있습니다
      feedback: 무상태는 요청 개수 제한이 아닙니다. 각 요청에 앞서 주고받은 내용이 자동으로 붙지 않는다는 성질입니다.
    - id: d
      text: TCP 연결이 끊기면 서버의 데이터베이스도 지워집니다
      feedback: HTTP의 무상태와 TCP 연결 상태, DB 저장은 서로 다른 개념입니다.
    - id: e
      text: 모든 HTTP 응답에는 로그인 정보가 들어 있습니다
      feedback: 무상태는 로그인 정보를 자동으로 포함한다는 뜻이 아닙니다. 서버가 별도 방법으로 상태를 이어갈 수 있습니다.
    answer: b
  - id: u10-l01-p06-q02
    kind: choice
    difficulty: medium
    prompt: TCP 연결이 유지될 때 HTTP 요청의 사용자 로그인 상태는 어떻게 되나요?
    choices:
    - id: a
      text: TCP가 로그인 상태를 자동으로 기억합니다
      feedback: TCP는 바이트 전달을 맡습니다. 로그인 상태는 애플리케이션이 별도 방법으로 이어야 합니다.
    - id: b
      text: HTTP는 이전 요청을 모두 TCP 연결 안에서 자동 저장합니다
      feedback: TCP 연결이 유지되어도 HTTP가 앞선 요청의 내용을 자동으로 기억하지는 않습니다.
    - id: c
      text: 로그인 상태는 IP 주소만으로 항상 복원됩니다
      feedback: 본문은 IP 주소가 아니라 서버와 브라우저가 쿠키·세션 같은 별도 방법을 쓸 수 있다고 설명합니다.
    - id: d
      text: 자동으로 기억되지는 않으며 서버와 브라우저가 별도 방법을 사용할 수 있습니다
      feedback: 맞아요. TCP 연결 유지와 HTTP의 로그인 상태는 서로 다른 층의 문제입니다.
    - id: e
      text: TCP 연결이 유지되는 동안에는 서버가 아무 정보도 저장할 수 없습니다
      feedback: 서버는 로그인 상태를 별도로 보관할 수 있습니다. 무상태는 앞선 HTTP 요청의 내용이 자동으로 이어지지 않는다는 뜻입니다.
    answer: d
  - id: u10-l01-p06-q03
    kind: choice
    difficulty: medium
    prompt: 브라우저와 서버가 쿠키를 주고받는 방식에 맞는 설명은 무엇인가요?
    choices:
    - id: a
      text: 서버 응답은 Set-Cookie를 보낼 수 있고, 브라우저는 다음 요청에 Cookie를 실을 수 있습니다
      feedback: 맞아요. 서버가 응답으로 쿠키를 설정하면 브라우저는 조건에 맞는 다음 요청에 Cookie 값을 보낼 수 있습니다.
    - id: b
      text: 브라우저 응답은 Set-Cookie를 보내고, 서버 요청은 Cookie를 보냅니다
      feedback: 방향이 반대입니다. Set-Cookie는 서버 응답에, Cookie는 브라우저의 후속 요청에 실릴 수 있습니다.
    - id: c
      text: 쿠키는 서버의 데이터베이스에만 저장되고 브라우저에는 오지 않습니다
      feedback: 본문에서는 브라우저가 쿠키를 보관하고 조건에 맞는 요청에 다시 보낼 수 있다고 설명합니다.
    - id: d
      text: Cookie 헤더는 HTML의 제목과 색을 정합니다
      feedback: 제목 구조는 HTML, 색은 CSS가 다룹니다. Cookie 헤더는 요청에 쿠키 값을 전달할 수 있습니다.
    - id: e
      text: Set-Cookie는 DNS가 주소를 찾을 때 보내는 응답입니다
      feedback: DNS는 도메인 이름을 IP 주소로 찾습니다. Set-Cookie는 HTTP 응답에서 쿠키를 설정할 수 있습니다.
    answer: a
  illustrations:
  - file: assets/animations/l35-daily-shop-keeps-no-record.svg
    title: "기록하지 않는 가게"
    alt: "손님이 처음 방문해 로그인했다고 말해도 가게는 기록을 남기지 않아 다음 방문에서는 알아보지 못합니다. 가게가 보관증을 건네고 손님이 보관해 두었다가 보여 주면 손님을 구별할 수 있습니다."
    caption: "기록을 남기지 않는 가게는 손님을 알아보지 못하지만, 보관증이 있으면 구별할 수 있습니다."
    after_paragraph: 0
  - file: assets/animations/l35-stateless-then-cookie.svg
    title: "HTTP는 요청을 자동으로 기억하지 않아요"
    alt: "브라우저가 POST /login으로 로그인하고 서버가 확인하지만, 다음 GET /next 요청에는 앞의 내용이 자동으로 붙지 않아 서버가 요청을 구별하지 못합니다. TCP 연결이 이어져 있어도 HTTP가 기억하는 것은 아닙니다. 서버가 Set-Cookie로 식별 표식을 저장하라고 하면 브라우저가 보관했다가 이후 요청의 Cookie 헤더에 실어 보냅니다."
    caption: "HTTP는 요청 사이의 기억을 자동으로 보존하지 않으며, 쿠키는 브라우저가 저장해 요청에 실어 보내는 표식입니다."
    after_paragraph: 4
- page_id: cookie-session
  terms:
  - 세션(Session)
  - 세션 ID(Session ID)
  - 쿠키(Cookie)
  question_placements:
  - question_id: u10-l01-p07-q01
    after_paragraph: 1
  - question_id: u10-l01-p07-q02
    after_paragraph: 3
  - question_id: u10-l01-p07-q03
    after_paragraph: 4
  questions:
  - id: u10-l01-p07-q01
    kind: choice
    difficulty: easy
    prompt: 세션 정보를 보관하는 곳은 어디인가요?
    choices:
    - id: a
      text: 브라우저가 보관하는 쿠키
      feedback: 쿠키는 브라우저가 보관해 요청에 실어 보내는 표식입니다. 세션 정보 자체는 보통 서버 쪽에 보관합니다.
    - id: b
      text: DNS 서버의 도메인 이름 기록
      feedback: DNS는 도메인 이름에 대응하는 IP 주소를 찾습니다. 로그인 세션 정보는 보통 서버 쪽에 보관합니다.
    - id: c
      text: TCP의 송신 버퍼
      feedback: TCP 송신 버퍼는 보낼 바이트를 잠시 보관합니다. 세션은 사용자의 로그인 상태를 서버 쪽에 보관합니다.
    - id: d
      text: 브라우저가 받은 HTML 문서
      feedback: HTML 문서는 웹 페이지의 구조를 담습니다. 로그인 세션 정보는 보통 서버 쪽에 보관합니다.
    - id: e
      text: 서버 쪽 저장 공간
      feedback: 맞아요. 서버는 세션 정보를 보관하고 세션 ID로 해당 정보를 구별할 수 있습니다.
    answer: e
  - id: u10-l01-p07-q02
    kind: choice
    difficulty: medium
    prompt: 쿠키와 세션의 역할을 본문에 맞게 구분한 것은 무엇인가요?
    choices:
    - id: a
      text: 쿠키는 서버의 로그인 상태이고 세션은 브라우저의 CSS 설정입니다
      feedback: 역할이 바뀌었습니다. 쿠키는 브라우저와 서버 사이에 오가는 값이고, 세션은 서버가 이어 기억하는 상태입니다.
    - id: b
      text: 쿠키와 세션은 같은 값의 서로 다른 이름입니다
      feedback: 본문은 두 용어를 구별합니다. 쿠키는 전달 수단이고 세션은 서버가 여러 요청을 잇는 상태입니다.
    - id: c
      text: 쿠키는 브라우저와 서버 사이에 오가는 값이고 세션은 서버가 보관하는 로그인 상태입니다
      feedback: 맞아요. 세션 ID를 쿠키로 전달할 수 있지만 쿠키와 세션 자체는 같은 것이 아닙니다.
    - id: d
      text: 쿠키는 IP 주소이고 세션은 TCP 포트 번호입니다
      feedback: IP와 포트는 네트워크 목적지를 구분합니다. 쿠키와 세션은 웹 로그인 상태를 이어 가는 데 쓰일 수 있습니다.
    - id: e
      text: 쿠키는 WAS 프로그램이고 세션은 데이터베이스 테이블입니다
      feedback: 본문에서 쿠키는 전달되는 값, 세션은 서버가 보관하는 로그인 상태로 설명합니다.
    answer: c
  - id: u10-l01-p07-q03
    kind: choice
    difficulty: medium
    prompt: 세션이 TCP 연결과 다른 점은 무엇인가요?
    choices:
    - id: a
      text: 세션은 바이트를 전달하고 TCP는 로그인 상태를 보관합니다
      feedback: 역할이 반대입니다. TCP는 데이터 전달 통로이고 세션은 로그인 같은 애플리케이션 상태입니다.
    - id: b
      text: TCP는 데이터 전달 통로이고 세션은 여러 HTTP 요청에 로그인 상태를 이어 줍니다
      feedback: 맞아요. 두 개념은 서로 다른 층의 역할을 합니다.
    - id: c
      text: 세션과 TCP 연결은 항상 같은 순간에 열리고 닫힙니다
      feedback: 본문은 두 개념을 구분합니다. TCP 연결 상태와 세션의 로그인 상태를 동일시할 수 없습니다.
    - id: d
      text: 세션은 한 요청만 기억하고 TCP는 로그인 상태를 이어 갑니다
      feedback: HTTP 로그인 상태를 여러 요청에 잇는 것은 세션입니다. TCP는 데이터 전달을 맡습니다.
    - id: e
      text: TCP는 세션 ID를 정하고 세션은 순서 번호를 관리합니다
      feedback: 세션 ID는 세션을 구분하고 순서 번호는 TCP 바이트 위치를 가리킵니다. 둘은 다른 역할입니다.
    answer: b
  illustrations:
  - file: assets/animations/l35-daily-ticket-and-ledger.svg
    title: "번호표와 회원 장부"
    alt: "손님이 로그인하면 가게가 자격을 확인하고 장부에 기록한 뒤 번호표를 건네며, 다음에 손님이 번호표를 보여 주면 가게가 번호표로 회원 장부를 찾아 확인합니다. 번호표는 손님이 가진 표식이고 장부는 가게가 보관하는 기록입니다."
    caption: "번호표는 손님이 가진 표식이고 장부는 가게가 보관하는 기록이라는 점에서 쿠키와 세션에 대응합니다."
    after_paragraph: 0
  - file: assets/animations/l35-session-id-cookie.svg
    title: "세션 ID로 로그인 상태 잇기"
    alt: "로그인 요청이 오면 서버가 자격을 확인해 세션을 만들고 세션 ID를 Set-Cookie로 전달하며, 브라우저가 이후 요청의 Cookie에 세션 ID를 실어 보내면 서버가 ID로 자신이 보관한 세션을 찾아 응답합니다. 쿠키는 브라우저가 보내는 표식이고 세션은 서버가 보관하는 상태입니다. 세션 ID a1b2c3은 예시입니다."
    caption: "쿠키는 브라우저가 보내는 표식이고, 세션은 서버가 보관하는 로그인 상태입니다. 세션 ID 값은 예시입니다."
    after_paragraph: 1
- page_id: db-role
  terms:
  - WAS(Web Application Server)
  - 데이터베이스(Database, DB)
  - 테이블(Table)
  - SQL(Structured Query Language)
  question_placements:
  - question_id: u10-l01-p08-q01
    after_paragraph: 1
  - question_id: u10-l01-p08-q02
    after_paragraph: 3
  - question_id: u10-l01-p08-q03
    after_paragraph: 4
  questions:
  - id: u10-l01-p08-q01
    kind: choice
    difficulty: easy
    prompt: 로그인 요청에서 DB에 저장될 수 있는 자료의 예로 가장 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 계정 자료처럼 나중에도 보존하고 다시 찾을 정보
      feedback: 맞아요. 계정 정보는 DB에 보관하고 로그인 처리에서 조회할 수 있습니다.
    - id: b
      text: 브라우저가 HTML을 화면으로 배치하는 과정
      feedback: 화면 배치는 브라우저가 합니다. DB에는 계정처럼 보존할 자료를 저장할 수 있습니다.
    - id: c
      text: 서버가 입력값을 받아 로그인 응답을 만드는 처리 과정
      feedback: 응답을 만드는 처리는 WAS가 맡을 수 있습니다. DB는 처리에 필요한 자료를 저장하고 조회합니다.
    - id: d
      text: TCP가 보내는 바이트의 순서 번호
      feedback: 순서 번호는 TCP의 전달 과정에 쓰입니다. DB에는 계정 같은 서비스 자료를 저장할 수 있습니다.
    - id: e
      text: 웹 페이지의 제목 색과 글자 간격
      feedback: 제목 색과 간격은 CSS가 정합니다. DB에는 로그인에 필요한 계정 자료를 저장할 수 있습니다.
    answer: a
  - id: u10-l01-p08-q02
    kind: choice
    difficulty: medium
    prompt: 로그인 요청에서 WAS와 DB는 어떤 방식으로 협력하나요?
    choices:
    - id: a
      text: DB가 요청을 받아 WAS의 로그인 화면을 직접 그립니다
      feedback: 브라우저가 화면을 그립니다. WAS는 처리를 맡고 DB는 필요한 자료를 제공합니다.
    - id: b
      text: WAS는 자료를 보관하고 DB는 로그인 처리 결과를 화면에 표시합니다
      feedback: 역할이 바뀌었습니다. DB는 자료를 저장하고 WAS는 요청을 처리해 응답을 만듭니다.
    - id: c
      text: WAS와 DB는 모두 브라우저 안에서 실행됩니다
      feedback: 본문은 WAS와 DB를 서버 쪽 구성요소로 설명합니다.
    - id: d
      text: WAS가 입력을 처리하고 DB에서 계정을 조회해 결과에 맞는 응답을 만듭니다
      feedback: 맞아요. WAS가 애플리케이션 처리를 맡고 DB에서 필요한 계정 자료를 확인할 수 있습니다.
    - id: e
      text: DB가 DNS를 대신해 로그인 요청의 도메인 이름을 찾습니다
      feedback: DNS는 도메인 이름을 IP 주소로 찾습니다. 로그인 처리는 WAS가 DB 자료를 이용해 수행할 수 있습니다.
    answer: d
  - id: u10-l01-p08-q03
    kind: choice
    difficulty: medium
    prompt: 사용자 입력값으로 DB를 조회할 때 본문에서 권장하는 방법은 무엇인가요?
    choices:
    - id: a
      text: 입력한 글자를 SQL 명령문에 그대로 이어 붙입니다
      feedback: 본문은 입력 문자를 명령문에 그대로 이어 붙이는 방식이 위험할 수 있다고 설명합니다.
    - id: b
      text: 사용자가 입력한 값을 웹 페이지의 제목으로 바꿉니다
      feedback: 페이지 제목 변경은 DB 조회 안전 방법이 아닙니다. 값과 명령을 분리해 전달해야 합니다.
    - id: c
      text: 입력값과 DB 명령을 분리해 전달합니다
      feedback: 맞아요. 본문은 입력값과 명령을 분리해 전달하는 방법을 권합니다.
    - id: d
      text: 로그인 입력을 모두 DNS 서버에 저장합니다
      feedback: DNS는 이름과 IP 주소를 찾는 역할입니다. DB 질의에서는 입력값을 명령과 분리해 다룹니다.
    - id: e
      text: 브라우저가 DB 테이블 전체를 내려받게 합니다
      feedback: DB 자료 전체를 내려받는 것이 아니라 필요한 계정 자료를 서버가 조회합니다.
    answer: c
  illustrations:
  - file: assets/animations/l35-daily-clerk-asks-ledger.svg
    title: "담당 직원이 장부에 물어봐요"
    alt: "손님의 신청서가 접수 창구를 거쳐 담당 직원에게 가고, 담당 직원이 회원 장부실에 이름이 있는지 물어 있음 또는 없음을 듣고, 결과를 손님에게 돌려줍니다."
    caption: "신청서는 접수 창구와 담당 직원을 거쳐 장부 확인을 마친 뒤 결과로 돌아옵니다."
    after_paragraph: 2
  - file: assets/animations/l35-was-asks-db.svg
    title: "WAS가 DB에 묻고 응답을 만들어요"
    alt: "브라우저의 로그인 요청이 웹 서버를 거쳐 WAS에 넘어가고, WAS가 DB의 users 표에서 계정 정보를 조회하면 DB가 계정 정보나 없음을 돌려주며, WAS가 성공 또는 실패 응답을 만들어 웹 서버와 네트워크를 거쳐 돌려보냅니다. DB에는 비밀번호 원문이 아닌 확인값이 보관됩니다."
    caption: "웹 서버가 요청을 접수해 WAS에 넘기면 WAS가 DB에서 필요한 계정 정보를 조회하고 응답을 만듭니다. 표의 값은 예시입니다."
    after_paragraph: 2
- terms:
  - 웹 서버(Web Server)
  - WAS(Web Application Server)
  - 데이터베이스(Database, DB)
  - 정적 파일(Static File)
  - 동적 응답(Dynamic Response)
  animations:
  - file: l35-web-was-db-flow.svg
    title: 로그인 한 번이 웹 서버, WAS, DB를 지나는 길
    alt: 브라우저에서 보낸 아이디 tester가 웹 서버, 처리 서버, DB로 차례로 이동하고, 처리 서버가 빈칸 문서에 tester를 채워 만든 문서가 되돌아와 브라우저에 표시되는 장면입니다.
    caption: 입력이 웹 서버와 WAS를 거쳐 DB에서 확인되고, tester님 안녕하세요라는 문서로 돌아옵니다.
  question_placements:
  - question_id: u10-l01-p09-q01
    after_paragraph: 1
  - question_id: u10-l01-p09-q02
    after_paragraph: 3
  - question_id: u10-l01-p09-q03
    after_paragraph: 4
  questions:
  - id: u10-l01-p09-q01
    kind: choice
    difficulty: easy
    prompt: 웹 서버가 할 수 있는 일로 본문에서 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 사용자의 로그인 상태 전체를 항상 쿠키에 저장합니다
      feedback: 쿠키는 브라우저와 서버 사이에 오가는 표식입니다. 웹 서버는 정적 파일을 보내거나 요청을 전달할 수 있습니다.
    - id: b
      text: 모든 데이터베이스 질의를 직접 실행하고 결과를 보관합니다
      feedback: 본문은 WAS가 DB 자료를 조회해 사이트별 처리를 한다고 구분합니다.
    - id: c
      text: 브라우저에서 HTML과 CSS를 렌더링합니다
      feedback: 브라우저가 HTML을 읽고 CSS를 적용해 화면을 만듭니다. 웹 서버는 자원을 보낼 수 있습니다.
    - id: d
      text: 도메인 이름을 IP 주소로 변환합니다
      feedback: 도메인 이름에서 IP 주소를 찾는 역할은 DNS가 합니다.
    - id: e
      text: 정적 파일을 보내거나 처리가 필요한 요청을 다른 구성요소에 전달합니다
      feedback: 맞아요. 웹 서버는 정적 파일을 보낼 수 있고, 필요한 처리를 WAS 같은 구성요소에 넘길 수 있습니다.
    answer: e
  - id: u10-l01-p09-q02
    kind: choice
    difficulty: medium
    prompt: 웹 서버·WAS·DB를 역할별로 구분했다면 반드시 서로 다른 컴퓨터 세 대에서 실행해야 하나요?
    choices:
    - id: a
      text: 네. 역할이 세 가지면 컴퓨터도 반드시 세 대입니다
      feedback: 본문은 역할 구분과 물리적인 장비 수가 같은 말이 아니라고 설명합니다.
    - id: b
      text: 네. DB는 항상 웹 서버와 다른 건물에 있어야 합니다
      feedback: DB의 물리적 위치는 여기서 정한 규칙이 아닙니다. 여러 역할은 한 서버에서도 함께 실행될 수 있습니다.
    - id: c
      text: 아니요. 역할은 나누어도 작은 서비스에서는 한 서버에서 함께 실행할 수 있습니다
      feedback: 맞아요. 역할별 구분은 설계상의 지도이며, 반드시 장비 세 대를 뜻하지 않습니다.
    - id: d
      text: 아니요. 웹 서버와 DB는 같은 역할이므로 항상 하나로 합쳐야 합니다
      feedback: 두 구성요소의 역할은 다릅니다. 다만 실제 배치는 서비스에 따라 같은 서버에 둘 수도 있습니다.
    - id: e
      text: 네. 브라우저가 서버 역할을 대신할 수 없기 때문입니다
      feedback: 브라우저가 서버 역할을 대신한다는 뜻이 아닙니다. 서버 역할들이 한 장비에 함께 실행될 수 있다는 설명입니다.
    answer: c
  - id: u10-l01-p09-q03
    kind: choice
    difficulty: medium
    prompt: 로그인 요청이 DB 자료 확인을 거쳐 브라우저 응답으로 돌아오는 흐름으로 가장 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 브라우저 → WAS → 웹 서버 → DB 확인 → 웹 서버 → 브라우저
      feedback: 본문에서는 웹 서버가 요청을 먼저 받고, 필요한 처리를 WAS에 맡긴 뒤 DB 자료를 확인한다고 설명합니다.
    - id: b
      text: 브라우저 → 웹 서버 → DB 확인 → WAS → 웹 서버 → 브라우저
      feedback: 이 흐름은 DB 확인이 WAS의 처리보다 앞섭니다. 본문에서는 WAS가 필요한 DB 자료를 조회해 응답을 만듭니다.
    - id: c
      text: 브라우저 → DB 확인 → 웹 서버 → WAS → 브라우저
      feedback: 브라우저가 DB에 직접 요청을 보내는 흐름은 아닙니다. 서버 쪽 WAS가 DB 자료를 확인합니다.
    - id: d
      text: 브라우저 → 웹 서버 → WAS → DB 확인 → WAS 응답 → 웹 서버 → 브라우저
      feedback: 맞아요. 요청은 웹 서버와 WAS를 거쳐 DB 자료를 확인하고, 처리된 응답은 브라우저로 돌아옵니다.
    - id: e
      text: 브라우저 → 웹 서버 → WAS → 브라우저 → DB 확인 → 웹 서버
      feedback: DB 확인은 브라우저에 응답을 돌려준 뒤가 아닙니다. WAS가 필요한 자료를 확인한 다음 응답을 만듭니다.
    answer: d
  illustrations:
  - file: assets/animations/l35-daily-hall-kitchen-storage.svg
    title: "홀, 주방, 창고의 역할"
    alt: "손님의 주문을 홀이 받고, 메뉴판은 홀이 바로 주지만 요리는 주방이 창고의 재료로 만들며, 작은 가게는 한 사람이 여러 일을 맡고 큰 가게는 역할마다 담당을 나눈다고 표시됩니다."
    caption: "역할을 나누는 것과 사람 수는 별개입니다. 작은 가게는 한 사람이 여러 일을 맡을 수 있습니다."
    after_paragraph: 2
  - file: assets/animations/l35-roles-vs-machines.svg
    title: "역할 구분과 장비 수는 달라요"
    alt: "웹 서버는 접수와 정적 파일, WAS는 처리와 응답 만들기, DB는 자료 저장과 조회를 맡습니다. 정적 파일은 웹 서버가 바로 보내고 처리가 필요하면 WAS와 DB가 맡으며, 작은 서비스는 한 서버에서 여러 역할을 맡고 서비스가 커지면 여러 장비나 가상 서버로 나눌 수 있습니다."
    caption: "논리적인 역할 구분과 물리적인 장비 개수는 같은 말이 아닙니다. 모든 웹 서비스가 서로 다른 컴퓨터 세 대를 쓰는 것은 아닙니다."
    after_paragraph: 2
  illustration_after_paragraph: [1]
---

## 웹 접속 한 번, 네트워크부터 서버까지 되짚기

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

## 받기만으로는 부족하다: POST로 보내기

상품 목록을 보기만 할 때 브라우저는 서버에서 문서를 받아오면 된다. 하지만 로그인처럼 사용자가 아이디와 비밀번호를 입력하면 그 값을 서버에 전달해야 한다. 브라우저에서 서버로 보내는 요청도 웹 서비스의 기본 흐름에 포함된다.

HTTP 메서드(Method)는 요청이 자원에 대해 어떤 동작을 하려는지 나타낸다. `GET`은 보통 정보를 가져오는 요청에, `POST`는 입력한 자료를 서버에 제출하거나 처리를 요청하는 경우에 자주 사용한다. 로그인 폼의 제출은 POST의 흔한 예다. GET이나 POST는 요청의 종류를 나타내지만, 서버 안에서 어떤 처리를 할지까지 정해 주지는 않는다. 예를 들어 POST 요청은 사이트에 따라 로그인 확인, 주문 저장, 댓글 등록으로 이어질 수 있다.

브라우저는 입력 내용을 요청에 담아 서버로 보내고, 서버는 아이디·비밀번호 같은 로그인 정보를 확인한 결과를 응답한다. 성공하면 환영 화면이나 다음 페이지가 오고, 실패하면 오류 안내가 올 수 있다. 우리는 입력 내용이 브라우저 화면에 보이는 일과 서버가 그 내용을 받아 처리하는 일을 구별해서 보아야 한다.

로그인 정보는 민감한 입력이다. HTTPS는 브라우저와 연결된 서버 사이의 통신을 전송 계층 보안(TLS)으로 보호할 수 있지만, 암호화가 모든 보안 문제를 해결하거나 서버에서의 안전한 저장을 보장하지는 않는다. 보안 장비와 입력 검증은 뒤에서 다루므로 여기서는 “입력도 HTTP 요청으로 서버에 전달된다”는 흐름을 잡는다.

**기억할 흐름:** GET은 자료를 가져올 때, POST는 자료를 제출하거나 처리를 요청할 때 흔히 쓰인다. 정확한 동작은 서버가 정한다.

## HTTP는 요청 사이의 기억을 자동으로 보존하지 않는다
<!-- learn-page-id: http-stateless -->

로그인 페이지에서 아이디와 비밀번호를 확인한 뒤, 다음 페이지로 이동했다고 하자. 브라우저는 새 HTTP 요청을 보내지만 HTTP 요청 하나가 끝난 뒤 다음 요청이 자동으로 이전 요청의 대화 내용을 기억해 주지는 않는다. 마치 손님 기록을 따로 남기지 않는 가게가 다음 방문 때 손님을 알아보지 못하는 것과 비슷하다. 이런 성질을 무상태(Stateless)라고 한다.

무상태라는 말은 웹 서버가 영원히 아무것도 저장하지 못한다는 뜻이 아니다. HTTP 자체의 각 요청에 앞서 주고받은 내용이 자동으로 붙지 않는다는 뜻이다. 서버 애플리케이션은 로그인 상태를 별도로 보관하고, 후속 요청이 누구의 것인지 구별하는 방법을 마련할 수 있다.

TCP 연결 상태와 HTTP의 무상태도 서로 다른 층의 이야기다. TCP는 연결을 통해 바이트를 전달하고, HTTP는 요청과 응답의 의미를 정한다. TCP 연결이 유지된다고 해서 HTTP가 사용자의 로그인 상태를 자동 기억하는 것은 아니다. ([HTTP의 무상태 복습](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/9/lesson/4/page/1))

사이트가 매 요청마다 비밀번호를 다시 묻지 않도록, 서버와 브라우저는 쿠키(Cookie)와 세션(Session) 같은 방법을 함께 사용할 수 있다. 두 용어는 같은 것이 아니다. 이어지는 두 페이지에서 브라우저가 보내는 표식과 서버가 기억하는 로그인 상태를 나누어 살펴본다.


서버가 로그인 성공을 확인했다고 하자. 서버는 브라우저에 쿠키를 저장하라는 응답을 보낼 수 있고, 브라우저는 이후 조건에 맞는 요청에 그 쿠키를 다시 포함한다. 쿠키는 브라우저가 보관하고 요청과 함께 보내는 작은 데이터다. 서버가 그 값을 어떻게 해석할지는 서비스가 정한다.
쿠키는 응답의 `Set-Cookie` 헤더로 설정될 수 있고, 브라우저는 이후 요청의 `Cookie` 헤더에 값을 실어 보낼 수 있다. 예를 들어 브라우저가 `theme=dark`처럼 화면 설정값을 저장했다가 같은 사이트에 다음 요청을 보낸다고 해 보자. 다음 페이지에서 볼 로그인 확인 번호도 쿠키에 담을 수 있지만, 아이디나 비밀번호를 그대로 넣어야 한다는 뜻은 아니다. 보통은 의미가 드러나지 않는 식별 표식을 저장하고 서버가 이를 확인한다.

쿠키에는 적용할 도메인·경로·만료 시간 같은 조건과, 브라우저가 다루는 방식을 제한하는 속성이 붙을 수 있다. 초보 단계에서는 “브라우저가 보관하고, 다음 요청 때 조건에 따라 다시 보내는 값”으로 기억하자. 쿠키에 무엇을 담을지와 어떻게 보호할지는 별도의 보안 고려가 필요하다. ([쿠키 동작 복습](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/9/lesson/4/page/1))

우체국 보관증처럼 쿠키는 서버가 요청을 구별할 때 참고할 수 있는 표식이다. 보관증 자체가 창고 안의 물건 전부를 의미하지 않듯, 쿠키 값과 서버가 보관하는 로그인 정보는 구분해야 한다. 다음 페이지에서 서버 쪽에 놓이는 세션을 살펴본다.

**구별하기:** 쿠키는 브라우저가 저장해 요청에 실어 보내는 데이터다. 로그인 상태의 전체 내용이 쿠키에 들어 있다고 단정하지 않는다.

## 세션 ID로 로그인 요청을 이어 보기
<!-- learn-page-id: cookie-session -->

세션(Session)은 여러 요청을 한 번의 로그인 상태로 이어 보려고 서버가 정보를 보관하는 방식이다. 로그인 예에서는 “이 브라우저는 로그인 확인을 마쳤다”라는 표시를 서버 쪽에 보관할 수 있다. 서버는 각 사용자의 정보를 구별하기 위해 세션 ID(Session ID)라는 식별 값을 사용한다.

로그인 요청이 성공하면 서버는 세션을 만들고, 그 세션을 찾을 수 있는 ID를 쿠키로 브라우저에 전달할 수 있다. 브라우저가 다음 요청에 쿠키를 보내면 서버는 ID를 확인해 자신이 보관한 세션 정보를 찾는다. 흐름은 **로그인 요청 → 서버의 자격 확인 → 세션 생성 → ID를 쿠키로 전달 → 후속 요청에서 ID 전송 → 서버가 세션 확인** 순서다.

쿠키와 세션은 서로 경쟁하는 두 방식이 아니다. 쿠키는 브라우저와 서버 사이에 오가는 저장·전달 수단이고, 세션은 서버가 여러 요청을 연결해 기억하는 방식이다. 세션 ID를 쿠키로 전달하는 설계가 흔하지만, 세션을 구현하는 세부 방법은 서비스에 따라 달라질 수 있다.

세션은 TCP 연결과도 다르다. TCP 연결은 두 끝점 사이의 데이터 전달 통로이고, 세션은 로그인 같은 애플리케이션 상태를 여러 HTTP 요청에 이어 붙이는 개념이다. 사용자가 로그아웃하거나 일정 시간이 지나면 서버가 세션을 끝낼 수 있다.

**한 줄 정리:** 쿠키는 브라우저가 보내는 표식이고, 세션은 서버가 보관하는 로그인 상태다.

## WAS가 DB에 묻고 결과를 돌려주기
<!-- learn-page-id: db-role -->

로그인 요청을 받은 서버는 아이디에 해당하는 계정 정보가 있는지 확인할 수 있다. 이 정보가 저장된 곳이 데이터베이스(Database, DB)다. 웹 서비스에서 DB는 계정, 상품, 주문처럼 나중에도 보존하고 다시 찾아야 하는 자료를 저장하는 역할을 맡는다.

간단한 관계형 데이터베이스(Relational Database)는 표와 비슷한 테이블에 자료를 행과 열로 담는다. 예를 들어 `users` 테이블에는 사용자 ID와 비밀번호 해시, 계정 상태 같은 열이 있을 수 있다. 실제 서비스는 비밀번호를 읽을 수 있는 원문 그대로 저장하지 않는다. 대신 원래 비밀번호를 바로 되살리기 어렵게 바꾼 확인값을 보관한다. 여기서는 DB 조회가 로그인 처리의 한 단계라는 점에 집중한다.

웹 애플리케이션 서버(WAS)는 로그인처럼 사이트마다 달라지는 처리를 맡는 서버 쪽 프로그램 실행 환경이다. 웹 서버가 요청을 접수해 WAS에 넘기면, WAS는 로그인 입력을 확인하고 DB에서 해당 계정을 조회해 성공 또는 실패 응답을 만든다. 웹 서버는 정적 파일을 보내는 일도 맡을 수 있다. 두 역할을 나누는 이유와 전체 흐름은 마지막 페이지에서 다시 묶어 본다.

예를 들어 데이터베이스 질의 언어(SQL)로 “users 표에서 입력한 아이디와 일치하는 사용자를 찾아 달라”고 요청할 수 있다. 입력한 글자를 명령문에 그대로 이어 붙이는 방식은 위험할 수 있으므로, 값과 명령을 분리해 전달하는 방법을 사용한다. 입력값을 안전하게 다루는 방법은 다음 Lesson에서 다시 다룬다.

응답은 처리 결과를 담아 WAS에서 웹 서버와 네트워크를 거쳐 브라우저로 돌아간다. 브라우저가 응답을 받았다는 사실과 로그인 상태가 안전하게 유지되는지는 다른 문제다. 이제 마지막 페이지에서 요청을 받은 여러 서버 역할을 하나의 구조로 묶어 보자.

## 웹 서버·WAS·DB가 역할을 나누는 이유
<!-- learn-page-id: was-role -->

웹 서버(Web Server)는 브라우저의 HTTP 요청을 받고 정적 파일을 보내거나, 필요한 처리를 다른 구성요소에 전달할 수 있다. 정적 파일은 요청마다 내용이 달라지지 않는 CSS, 이미지, 미리 만들어 둔 HTML 파일 같은 자료다. WAS는 로그인 여부처럼 요청을 처리해 결과를 만드는 일을 맡고, DB는 필요한 자료를 저장하고 조회한다.

로그인 흐름을 다시 보자. 브라우저가 요청을 보내면 웹 서버가 받고, 애플리케이션 처리가 필요하면 WAS가 입력을 확인한다. WAS는 DB에서 계정 자료를 찾아 결과를 판단하고 응답을 만든다. 응답은 웹 서버를 거쳐 브라우저로 돌아와 화면이 된다. 요청 방향과 응답 방향을 함께 따라가면 각 요소의 역할이 더 분명해진다.

웹 서버, WAS, DB를 나누는 것은 역할별로 관리·확장·관찰하기 쉽게 만드는 한 가지 설계다. 모든 웹 서비스가 반드시 서로 다른 컴퓨터 세 대를 사용하는 것은 아니다. 소규모 서비스에서는 여러 역할이 한 서버에서 실행될 수 있고, 서비스가 커지면 여러 장비나 가상 서버로 나눌 수 있다. 논리적인 역할 구분과 물리적인 장비 개수는 같은 말이 아니다.

앞에서 본 HTML·CSS·JavaScript는 브라우저가 화면과 동작을 구성하는 자원이고, 서버는 그 자원이나 데이터 응답을 제공할 수 있다. 로그인 예에서는 Cookie가 브라우저와 서버 사이를 오가는 표식이고 Session은 WAS 쪽에서 이어지는 상태이며 DB는 계정 자료를 저장한다. 이제 “웹 페이지가 뜬다”를 하나의 기계가 모두 처리한다고 보지 않고, 요청·처리·저장·응답의 협력으로 설명할 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** DNS가 이름을 찾고, HTTP가 요청·응답을 표현하며, 웹 서버는 요청을 받고, WAS는 필요한 처리를 하며, DB는 자료를 저장한다.
- **적용하기 (Apply):** 로그인 요청을 브라우저 → 웹 서버 → WAS → DB → 응답 순으로 그려 보고, Cookie와 Session이 각각 어디서 쓰이는지 말한다.
- **찾아보기 (Lookup):** 실제 배포 구성, TLS 보호 범위, Cookie 속성, DB·WAS 구현 기술은 해당 서비스의 설계·보안 문서에서 확인한다.
