---
id: u10-l02-login-and-session-state
title: 로그인 요청은 어떻게 서버와 이어질까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-35.md
animations_dir: units/10-web-service-structure/lessons/02-로그인-요청과-세션/assets/animations
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
wiki_diagram: units/10-web-service-structure/lessons/02-로그인-요청과-세션/assets/diagrams/lesson-35.svg
page_metadata:
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
    title: 조회 창구와 접수 창구
    alt: 나는 조회 창구에서 목록을 보여 달라고 하여 서류를 받고, 접수 창구에서는 내가 쓴 서류를 내면 우체국이 확인해 처리한 뒤 승인 또는 반려를 알려 줍니다.
    caption: 목록을 보는 일과 내가 쓴 서류를 내서 처리하는 일은 다르며, 어떻게 처리할지는 받는 쪽이 정합니다.
    after_paragraph: -1
  - file: assets/animations/l35-get-vs-post.svg
    title: GET은 가져오기, POST는 제출
    alt: 브라우저가 GET /items로 문서를 가져오고, POST /login으로 입력 내용을 제출하면 서버가 입력을 확인해 처리한 뒤 성공 화면이나 오류 안내를 응답합니다.
    caption: GET은 자료를 가져올 때, POST는 자료를 제출하거나 처리를 요청할 때 흔히 쓰이며 정확한 동작은 서버가 정합니다.
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
    title: 기록하지 않는 가게
    alt: 손님이 처음 방문해 로그인했다고 말해도 가게는 기록을 남기지 않아 다음 방문에서는 알아보지 못합니다. 가게가 보관증을 건네고 손님이 보관해 두었다가 보여 주면 손님을 구별할 수 있습니다.
    caption: 기록을 남기지 않는 가게는 손님을 알아보지 못하지만, 보관증이 있으면 구별할 수 있습니다.
    after_paragraph: -1
  - file: assets/animations/l35-stateless-then-cookie.svg
    title: HTTP는 요청을 자동으로 기억하지 않아요
    alt: 브라우저가 POST /login으로 로그인하고 서버가 확인하지만, 다음 GET /next 요청에는 앞의 내용이 자동으로 붙지 않아 서버가 요청을 구별하지 못합니다. TCP 연결이 이어져
      있어도 HTTP가 기억하는 것은 아닙니다. 서버가 Set-Cookie로 식별 표식을 저장하라고 하면 브라우저가 보관했다가 이후 요청의 Cookie 헤더에 실어 보냅니다.
    caption: HTTP는 요청 사이의 기억을 자동으로 보존하지 않으며, 쿠키는 브라우저가 저장해 요청에 실어 보내는 표식입니다.
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
    title: 번호표와 회원 장부
    alt: 손님이 로그인하면 가게가 자격을 확인하고 장부에 기록한 뒤 번호표를 건네며, 다음에 손님이 번호표를 보여 주면 가게가 번호표로 회원 장부를 찾아 확인합니다. 번호표는 손님이 가진 표식이고
      장부는 가게가 보관하는 기록입니다.
    caption: 번호표는 손님이 가진 표식이고 장부는 가게가 보관하는 기록이라는 점에서 쿠키와 세션에 대응합니다.
    after_paragraph: -1
  - file: assets/animations/l35-session-id-cookie.svg
    title: 세션 ID로 로그인 상태 잇기
    alt: 로그인 요청이 오면 서버가 자격을 확인해 세션을 만들고 세션 ID를 Set-Cookie로 전달하며, 브라우저가 이후 요청의 Cookie에 세션 ID를 실어 보내면 서버가 ID로 자신이
      보관한 세션을 찾아 응답합니다. 쿠키는 브라우저가 보내는 표식이고 세션은 서버가 보관하는 상태입니다. 세션 ID a1b2c3은 예시입니다.
    caption: 쿠키는 브라우저가 보내는 표식이고, 세션은 서버가 보관하는 로그인 상태입니다. 세션 ID 값은 예시입니다.
    after_paragraph: 1
---


핵심 개념을 주제별로 정리했다.

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
