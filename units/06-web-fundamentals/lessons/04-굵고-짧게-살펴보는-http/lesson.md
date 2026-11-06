---
id: u6-l34-굵고-짧게-살펴보는-http
title: 'HTTP 요청과 응답은 어떻게 오갈까?'
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-34.md
wiki_diagram: units/06-web-fundamentals/lessons/04-굵고-짧게-살펴보는-http/assets/diagrams/lesson-34.svg
page_metadata:
- terms:
  - Stream(스트림)
  - 프로토콜(protocol)
  animations:
  - file: l34-stream-boundary.svg
    title: 끊김 없는 두루마리, 약속으로 끊어 읽기
    alt: 글자가 끊김 없이 흘러가는 긴 띠 위에서 빈 줄 약속을 만나면 가위가 두 메시지로 나누는 장면입니다.
    caption: Stream에는 칸막이가 없어서, 약속(HTTP 규칙)으로 메시지 경계를 찾습니다.
  questions:
  - id: u9-l04-p01-q01
    kind: choice
    difficulty: easy
    prompt: HTTP의 역할을 바르게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 도메인 이름을 IP 주소로 바꾸는 규칙이다
      feedback: 이 페이지에서 HTTP는 이름 조회가 아니라 웹 요청과 응답의 규칙입니다.
    - id: b
      text: 웹 자원을 요청하고 응답할 때 따르는 규칙이다
      feedback: 맞아요. HTTP는 클라이언트와 서버가 요청과 응답을 주고받는 약속입니다.
    - id: c
      text: 서버 컴퓨터의 디스크 폴더를 정하는 규칙이다
      feedback: HTTP는 디스크 폴더를 정하는 규칙이 아니라 메시지를 주고받는 규칙입니다.
    - id: d
      text: 브라우저가 화면의 글꼴을 정하는 규칙이다
      feedback: 화면 모양 대신 웹 자원의 요청과 응답을 다룹니다.
    - id: e
      text: 서버에서 브라우저로만 정보를 보내는 규칙이다
      feedback: 서버의 응답뿐 아니라 클라이언트가 보내는 요청도 포함합니다.
    answer: b
  - id: u9-l04-p01-q02
    kind: choice
    difficulty: medium
    prompt: HTTP/1.1과 TCP/IP를 함께 쓰는 예시를 이해한 설명으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: TCP가 HTML 내용을 만들고 HTTP가 전선으로 데이터를 옮긴다
      feedback: 본문은 HTTP를 메시지 규칙, TCP/IP를 네트워크 전달에 쓰는 것으로 구별합니다.
    - id: b
      text: TCP가 요청 경계를 모두 정하므로 HTTP 규칙은 필요 없다
      feedback: TCP는 이어진 흐름을 전달하므로 HTTP 규칙에 맞춰 메시지를 구분합니다.
    - id: c
      text: HTTP/1.1과 TCP/IP는 같은 규칙을 다르게 부르는 말이다
      feedback: 메시지 교환 규칙과 네트워크로 옮기는 역할은 다릅니다.
    - id: d
      text: HTTP를 쓰면 브라우저는 요청 없이 응답만 기다린다
      feedback: 브라우저가 요청하면 서버가 결과를 돌려주는 흐름입니다.
    - id: e
      text: TCP는 데이터 흐름을 전달하고 HTTP는 요청·응답을 구분하는 규칙을 제공한다
      feedback: 맞아요. 이어진 흐름을 전달하는 역할과 웹 메시지를 해석하는 규칙을 나누어 이해해야 합니다.
    answer: e
  question_placements:
  - question_id: u9-l04-p01-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l34-daily-order-promise-road.svg
    title: "주문서 약속과 배달 길"
    alt: "손님은 약속된 주문서로 분식집에 주문하고 가게는 음식으로 답합니다. 아래 배달 길은 짐을 이어진 흐름으로 나르고, 주문서 양식 덕분에 주문 1과 주문 2를 나누어 읽습니다."
    caption: "주문하는 약속과 나르는 길은 서로 다른 일입니다."
    after_paragraph: 0
  - file: assets/animations/l34-http-and-tcp-roles.svg
    title: "HTTP와 TCP/IP의 역할"
    alt: "브라우저가 HTTP 요청을 보내고 서버가 HTTP 응답을 돌려줍니다. 아래 TCP/IP는 데이터를 이어진 흐름으로 옮기고, HTTP 규칙에 맞춰 흐름 속 요청 1과 요청 2의 경계를 나눕니다."
    caption: "HTTP는 웹 자원을 주고받는 약속이고, TCP/IP는 데이터를 옮기는 데 쓰입니다."
    after_paragraph: 1
  illustration_after_paragraph: [-1, 1]
- terms:
  - 헤더(header)
  questions:
  - id: u9-l04-p02-q01
    kind: choice
    difficulty: easy
    prompt: HTTP 메시지에서 헤더와 본문 사이의 빈 줄은 무엇을 알리나요?
    choices:
    - id: a
      text: 다음 줄도 계속 헤더라는 표시
      feedback: 빈 줄 뒤에는 실제 본문 내용이 시작됩니다.
    - id: b
      text: 요청이 반드시 실패했다는 표시
      feedback: 빈 줄은 구조상 경계이며 실패 결과를 뜻하지 않습니다.
    - id: c
      text: 헤더가 끝나고 실제 본문 내용이 시작되는 경계
      feedback: 맞아요. 빈 줄은 부가 정보인 헤더와 실제 내용을 나누는 표지입니다.
    - id: d
      text: HTTP 버전이 바뀐다는 표시
      feedback: 버전 정보는 첫 줄에서 읽으며 빈 줄은 헤더와 본문을 나눕니다.
    - id: e
      text: 본문을 요청 첫 줄보다 먼저 읽으라는 표시
      feedback: 메시지는 첫 줄, 헤더, 빈 줄, 본문 순서로 읽습니다.
    answer: c
  - id: u9-l04-p02-q02
    kind: choice
    difficulty: medium
    prompt: GET /example-page HTTP/1.1과 HTTP/1.1 200 OK를 읽은 설명으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 앞은 /example-page를 GET으로 요청하고 뒤는 성공 처리 결과를 알린다
      feedback: 맞아요. 요청 첫 줄은 방식과 경로를, 응답 첫 줄은 처리 결과를 요약합니다.
    - id: b
      text: 앞은 서버의 성공 응답이고 뒤는 브라우저의 요청이다
      feedback: 요청 첫 줄과 응답 첫 줄을 반대로 읽었습니다.
    - id: c
      text: 앞의 /example-page는 Host 헤더에 적힌 사이트 이름이다
      feedback: /example-page는 요청 경로이고 Host 헤더는 어느 사이트인지 알려 줍니다.
    - id: d
      text: 뒤의 200 OK는 응답 본문에 들어 있는 HTML 전체다
      feedback: 200 OK는 첫 줄의 처리 결과이며 실제 HTML 본문과 다릅니다.
    - id: e
      text: 앞의 GET은 헤더이고 뒤의 HTTP/1.1은 HTML 본문이다
      feedback: 둘 다 메시지 첫 줄에 있는 정보이며 헤더나 본문으로 읽지 않습니다.
    answer: a
  question_placements:
  - question_id: u9-l04-p02-q01
    after_paragraph: 7
  illustrations:
  - file: assets/animations/l34-daily-order-slip-lines.svg
    title: "주문서와 답을 줄마다 읽어요"
    alt: "왼쪽 주문서와 오른쪽 답에서 첫 줄, 가게 이름 같은 덧붙인 정보, 빈 줄, 떡볶이가 담긴 상자가 차례로 강조됩니다."
    caption: "첫 줄은 요약, 다음 줄들은 덧붙인 정보, 빈 줄 뒤가 실제 내용입니다."
    after_paragraph: 0
  - file: assets/animations/l34-message-parts.svg
    title: "HTTP 메시지의 모양"
    alt: "요청의 GET /example-page HTTP/1.1과 Host: www.example.com, 응답의 HTTP/1.1 200 OK와 Content-Type 헤더, 빈 줄, <h1>안녕, 웹!</h1> 본문이 차례로 강조됩니다."
    caption: "첫 줄은 요청이나 결과의 요약, 헤더는 부가 정보, 본문은 실제로 주고받는 내용입니다."
    after_paragraph: 5
- terms:
  - Request / Response
  - Method(메서드)
  animations:
  - file: l34-request-response.svg
    title: 손님 같은 클라이언트, 식당 같은 서버
    alt: 왼쪽 컴퓨터가 GET 요청 쪽지를 오른쪽 서버로 보내고, 서버가 HTML 문서를 담은 응답을 돌려보내는 장면입니다.
    caption: 클라이언트가 Request를 보내면 서버가 Response로 답합니다.
  questions:
  - id: u9-l04-p03-q01
    kind: choice
    difficulty: easy
    prompt: Request와 Response의 방향을 바르게 짝지은 것은 무엇인가요?
    choices:
    - id: a
      text: Request는 서버→클라이언트, Response는 클라이언트→서버다
      feedback: 두 방향이 반대입니다. 브라우저가 Request를 보냅니다.
    - id: b
      text: 둘 다 클라이언트→서버로만 간다
      feedback: Response는 서버에서 클라이언트로 돌아옵니다.
    - id: c
      text: 둘 다 서버→클라이언트로만 간다
      feedback: Request는 클라이언트가 서버로 보내는 메시지입니다.
    - id: d
      text: Request는 클라이언트→서버, Response는 서버→클라이언트다
      feedback: 맞아요. 클라이언트가 요청을 보내고 서버가 처리 결과를 돌려줍니다.
    - id: e
      text: 방향과 관계없이 먼저 도착한 것이 Response다
      feedback: 도착 순서 대신 보내는 역할과 메시지의 의미로 구별합니다.
    answer: d
  - id: u9-l04-p03-q02
    kind: choice
    difficulty: medium
    prompt: 페이지 하나를 열었는데 HTML, 이미지, CSS 요청이 각각 보입니다. 알맞은 판단은 무엇인가요?
    choices:
    - id: a
      text: 페이지 하나에는 요청이 하나뿐이므로 모두 중복 오류다
      feedback: 주소창에서 한 번 열어도 필요한 자원을 각각 요청할 수 있습니다.
    - id: b
      text: 페이지 구성에 필요한 자원을 각각 요청할 수 있다
      feedback: 맞아요. 한 페이지도 여러 자원으로 이루어져 요청이 여러 번 생길 수 있습니다.
    - id: c
      text: 이미지 요청은 서버가 브라우저에 보내는 Request다
      feedback: 자원을 달라는 Request는 클라이언트가 보내며 서버가 Response를 줍니다.
    - id: d
      text: CSS는 페이지가 아니므로 HTTP로 요청할 수 없다
      feedback: 본문은 CSS와 이미지, JavaScript도 각각 요청할 수 있다고 설명합니다.
    - id: e
      text: 요청이 여러 개면 서버가 HTML을 응답하지 않은 것이다
      feedback: HTML을 받은 뒤에도 다른 자원을 요청할 수 있어 응답 실패로 단정할 수 없습니다.
    answer: b
  question_placements:
  - question_id: u9-l04-p03-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l34-daily-many-orders.svg
    title: "주문하면 가게가 답해요"
    alt: "손님이 떡볶이를 주문하고 가게가 주문 완료와 함께 떡볶이를 내줍니다. 이어서 단무지, 음료, 수저도 따로 부탁하고 각각 답을 받습니다."
    caption: "한 번 방문에도 주문과 답이 여러 번 오갈 수 있습니다."
    after_paragraph: 1
  - file: assets/animations/l34-many-requests-one-page.svg
    title: "Request와 Response"
    alt: "브라우저가 GET /example-page 요청을 보내고 서버가 200 OK와 HTML로 응답합니다. 이어서 logo.png, style.css, app.js도 각각 요청하고 응답을 받습니다."
    caption: "Request는 클라이언트에서 서버로, Response는 서버에서 클라이언트로 오가며 페이지 하나에도 여러 번 생깁니다."
    after_paragraph: 1
  illustration_after_paragraph: [0]
- terms:
  - 개발자 도구(Developer Tools)
  - Network 탭
  - 경로(path)
  questions:
  - id: u9-l04-p04-q01
    kind: choice
    difficulty: easy
    prompt: 브라우저가 불러온 요청 목록을 살펴보는 개발자 도구의 탭은 무엇인가요?
    choices:
    - id: a
      text: 방문 기록 목록
      feedback: 방문 기록은 페이지 이력이며 요청별 헤더와 본문을 살피는 Network 탭과 다릅니다.
    - id: b
      text: 즐겨찾기 목록
      feedback: 즐겨찾기는 저장한 주소 목록이며 실제 요청 목록을 보여 주는 도구가 아닙니다.
    - id: c
      text: 주소 자동완성 목록
      feedback: 입력 후보는 요청의 방식과 상태 코드를 보여 주는 Network 탭과 다릅니다.
    - id: d
      text: 다운로드 파일 목록
      feedback: 파일 다운로드 이력과 페이지의 개별 요청을 살피는 Network 탭은 다릅니다.
    - id: e
      text: Network 탭
      feedback: 맞아요. Network 탭에서 요청 목록과 각 요청의 상세 정보를 확인합니다.
    answer: e
  - id: u9-l04-p04-q02
    kind: choice
    difficulty: medium
    prompt: 본인이 연 HTTPS 페이지의 요청 방식과 응답 내용을 확인하려면 어떻게 하나요?
    choices:
    - id: a
      text: 주소창의 이름만 보고 요청과 응답 헤더를 확정한다
      feedback: 주소만으로 상세 헤더와 응답 내용을 알 수 없어 요청 항목을 살펴야 합니다.
    - id: b
      text: HTTPS는 암호화되므로 자기 브라우저에서도 내용을 볼 수 없다고 판단한다
      feedback: 이동 중 암호화와 브라우저가 처리한 내용을 개발자 도구에서 보는 일은 다릅니다.
    - id: c
      text: Network 탭에서 해당 요청을 골라 상세 정보를 확인한다
      feedback: 맞아요. 개발자 도구는 브라우저가 처리한 요청의 방식, 상태, 헤더와 본문을 보여 줍니다.
    - id: d
      text: 요청 목록의 개수만 세고 응답 본문까지 확인했다고 판단한다
      feedback: 개수만으로 본문을 알 수 없으므로 요청 항목의 상세 정보를 확인해야 합니다.
    - id: e
      text: 페이지 화면만 보고 서버가 보낸 모든 헤더를 읽었다고 판단한다
      feedback: 페이지 화면과 응답 헤더는 다르므로 Network 상세 정보를 열어야 합니다.
    answer: c
  question_placements:
  - question_id: u9-l04-p04-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l34-daily-order-history.svg
    title: "내 주문 내역 살펴보기"
    alt: "앱의 내 주문 내역에서 떡볶이 주문 하나를 골라 주문 종류, 결과, 메모, 받은 것을 확인합니다. 마지막에 내 주문만 보고 남의 주문은 엿보지 않는다고 표시됩니다."
    caption: "내 주문 하나를 골라 무엇을 부탁했고 무엇을 받았는지 봅니다."
    after_paragraph: 0
  - file: assets/animations/l34-devtools-network.svg
    title: "개발자 도구의 Network 탭"
    alt: "Network 탭의 요청 목록에서 example-page를 골라 Method GET, 상태 200 OK, 요청 헤더, HTML 응답 본문을 확인합니다. 마지막에 내가 연 페이지의 요청만 본다고 표시됩니다."
    caption: "Network 탭에서 요청 하나를 고르면 브라우저가 보낸 것과 서버가 답한 것을 볼 수 있습니다."
    after_paragraph: 1
- terms:
  - User-Agent
  - Accept 계열
  - gzip
  questions:
  - id: u9-l04-p05-q01
    kind: choice
    difficulty: easy
    prompt: 'Accept: text/html 요청 헤더의 뜻은 무엇인가요?'
    choices:
    - id: a
      text: HTML 형식의 응답을 받을 수 있음을 알린다
      feedback: 맞아요. Accept는 클라이언트가 받을 수 있는 응답 형식을 알리는 부가 정보입니다.
    - id: b
      text: 서버가 이미 보낸 본문이 HTML임을 알린다
      feedback: 요청의 Accept는 응답을 받기 전 선호·지원 형식을 알리는 정보입니다.
    - id: c
      text: 요청할 파일 경로가 text/html이라고 알린다
      feedback: 헤더의 형식 정보와 요청 경로는 다릅니다.
    - id: d
      text: 브라우저가 보내는 본문 전체가 HTML이라는 뜻이다
      feedback: Accept는 본문 자체가 아니라 받을 수 있는 응답 형식에 대한 설명입니다.
    - id: e
      text: HTML 대신 gzip 압축만 받을 수 있다는 뜻이다
      feedback: gzip 처리 가능 여부는 Accept-Encoding으로 알립니다.
    answer: a
  - id: u9-l04-p05-q02
    kind: choice
    difficulty: medium
    prompt: '요청에 Accept-Language: ko와 Accept-Encoding: gzip이 있습니다. 바르게 읽은 것은 무엇인가요?'
    choices:
    - id: a
      text: 한국어 응답을 반드시 보장하고 요청 경로를 gzip으로 바꾼다
      feedback: 선호를 알리는 것과 보장은 다르며 압축 헤더는 경로 변경이 아닙니다.
    - id: b
      text: gzip 언어를 선호하고 ko 압축을 처리한다
      feedback: 언어와 압축 방식의 역할을 반대로 읽었습니다.
    - id: c
      text: 두 줄은 헤더가 아니라 서버가 보낸 실제 본문이다
      feedback: 이 이름과 값은 요청에 덧붙이는 헤더 정보입니다.
    - id: d
      text: 한국어 응답을 선호하고 gzip 압축 응답을 처리할 수 있다고 알린다
      feedback: 맞아요. 언어 선호와 압축 처리 가능 여부를 서로 다른 헤더로 전달합니다.
    - id: e
      text: 두 줄은 요청을 보낸 프로그램의 이름만 설명한다
      feedback: 프로그램 정보는 User-Agent에 담을 수 있으며 이 두 줄은 언어와 압축 정보입니다.
    answer: d
  question_placements:
  - question_id: u9-l04-p05-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l34-daily-order-memo.svg
    title: "주문서에 붙이는 메모"
    alt: "주문서의 받을 형태, 원하는 말, 눌러 담기 메모가 차례로 강조되고, 마지막에 주문 기기와 가려진 회원 카드 번호가 표시됩니다."
    caption: "메모는 주문에 덧붙인 설명이고, 민감한 번호는 가립니다."
    after_paragraph: 0
  - file: assets/animations/l34-request-headers.svg
    title: "요청 Header"
    alt: "요청 헤더 Accept: text/html, Accept-Language: ko, Accept-Encoding: gzip이 차례로 강조되고, 마지막에 User-Agent와 값이 가려진 Cookie가 표시됩니다."
    caption: "요청 헤더는 원하는 응답 형식과 요청에 필요한 부가 정보를 전달합니다. 민감한 값은 가립니다."
    after_paragraph: 1
- terms:
  - Content-Length
  - Cookie(쿠키)
  - UTF-8
  questions:
  - id: u9-l04-p06-q01
    kind: choice
    difficulty: easy
    prompt: '응답의 Content-Type: text/html; charset=utf-8은 무엇을 설명하나요?'
    choices:
    - id: a
      text: 본문을 요청한 클라이언트의 프로그램 이름
      feedback: 프로그램 정보를 담을 수 있는 User-Agent와 본문 형식 헤더는 다릅니다.
    - id: b
      text: 뒤에 올 본문의 종류와 문자 인코딩
      feedback: 맞아요. HTML 내용 자체가 아니라 본문을 어떻게 해석할지 알려 주는 헤더입니다.
    - id: c
      text: 본문이 담긴 서버의 실제 디스크 경로
      feedback: Content-Type은 파일 경로가 아니라 내용의 종류를 설명합니다.
    - id: d
      text: 본문 데이터의 바이트 수만
      feedback: 바이트 단위 크기는 Content-Length가 알려 줍니다.
    - id: e
      text: 쿠키를 저장하라는 명령만
      feedback: 쿠키 저장은 Set-Cookie로 알릴 수 있고 Content-Type은 형식 정보입니다.
    answer: b
  - id: u9-l04-p06-q02
    kind: choice
    difficulty: medium
    prompt: '응답에 Content-Length: 120과 Set-Cookie가 있습니다. 역할을 바르게 읽은 것은 무엇인가요?'
    choices:
    - id: a
      text: 앞은 글자 수, 뒤는 HTML 본문의 시작이다
      feedback: 크기는 글자 수가 아닌 바이트 단위이고 Set-Cookie는 본문 시작 표시가 아닙니다.
    - id: b
      text: 앞은 HTTP 상태 코드, 뒤는 요청 경로다
      feedback: 상태 코드는 응답 첫 줄에 있으며 두 헤더의 역할은 크기와 쿠키 안내입니다.
    - id: c
      text: 앞은 쿠키 저장 안내, 뒤는 본문의 바이트 크기다
      feedback: 두 헤더의 역할을 반대로 읽었습니다.
    - id: d
      text: 앞은 HTML 본문 전체이고 뒤는 그 문서 제목이다
      feedback: 둘 다 본문을 설명하거나 처리에 쓰는 헤더이며 실제 HTML 내용과 다릅니다.
    - id: e
      text: 앞은 본문의 바이트 크기, 뒤는 쿠키 저장 안내다
      feedback: 맞아요. Content-Length는 크기를 알려 주고 Set-Cookie는 브라우저에 쿠키 저장을 알릴 수 있습니다.
    answer: e
  question_placements:
  - question_id: u9-l04-p06-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l34-daily-box-label.svg
    title: "음식 상자에 붙은 라벨"
    alt: "음식 상자 라벨의 내용물, 무게, 적립 도장 안내가 차례로 강조되고, 손님이 라벨을 보고 음식을 알맞게 다룹니다."
    caption: "라벨은 내용물이 무엇인지와 어떻게 다룰지 알려 줍니다."
    after_paragraph: 0
  - file: assets/animations/l34-response-headers.svg
    title: "응답 Header"
    alt: "응답 헤더 Content-Type이 본문은 HTML이라고, Content-Length가 본문 크기를 알려 주고, Set-Cookie가 브라우저에 쿠키 저장을 알립니다. 마지막에 브라우저가 헤더를 참고해 응답을 처리합니다."
    caption: "응답 헤더는 본문이 어떤 내용인지와 브라우저가 어떻게 다룰지 설명합니다."
    after_paragraph: 1
- terms:
  - 응답 코드(status code)
  - 404 Not Found
  questions:
  - id: u9-l04-p07-q01
    kind: choice
    difficulty: easy
    prompt: 200 OK와 404 Not Found의 뜻을 바르게 짝지은 것은 무엇인가요?
    choices:
    - id: a
      text: 200은 자원 없음, 404는 성공 처리다
      feedback: 뜻이 반대입니다. 200은 성공이고 404는 자원을 찾지 못한 경우입니다.
    - id: b
      text: 200은 성공 처리, 404는 모든 네트워크가 끊김이다
      feedback: 404는 요청 자원을 찾지 못했다는 단서이며 전체 네트워크 단절을 뜻하지 않습니다.
    - id: c
      text: 200은 성공 처리, 404는 요청한 자원을 찾지 못함이다
      feedback: 맞아요. 둘 다 응답 첫 줄에서 요청 처리 결과를 요약하는 상태 코드입니다.
    - id: d
      text: 200은 로그인 실패, 404는 서버가 정상 처리함이다
      feedback: 본문에서 200은 성공, 404는 자원을 찾지 못함으로 설명합니다.
    - id: e
      text: 200과 404는 모두 응답 본문의 바이트 수다
      feedback: 상태 코드는 크기가 아니라 처리 결과를 나타냅니다.
    answer: c
  - id: u9-l04-p07-q02
    kind: choice
    difficulty: medium
    prompt: 삭제된 이미지 요청에서 404를, 다른 요청에서 5xx를 보았습니다. 알맞은 판단은 무엇인가요?
    choices:
    - id: a
      text: 앞은 자원을 못 찾았다는 뜻이고 뒤는 서버 처리 문제의 단서다
      feedback: 맞아요. 404와 5xx는 각각 결과의 단서를 주며 정확한 원인까지 모두 확정하지는 않습니다.
    - id: b
      text: 앞은 서버 처리 성공이고 뒤는 이미지 파일의 크기다
      feedback: 404는 성공이 아니며 5xx는 파일 크기가 아니라 상태 코드 계열입니다.
    - id: c
      text: 두 코드만 보면 모든 문제의 정확한 원인이 확정된다
      feedback: 본문은 코드를 단서로 보며 모든 원인을 설명하는 진단서는 아니라고 강조합니다.
    - id: d
      text: 404는 반드시 브라우저 고장이고 5xx는 반드시 주소 오타다
      feedback: 그렇게 단정할 수 없습니다. 404는 자원 없음, 5xx는 서버 처리 문제의 단서입니다.
    - id: e
      text: 4xx와 5xx는 모두 서버가 자원을 성공 처리했다는 뜻이다
      feedback: 성공은 200의 예이며 4xx와 5xx는 문제를 나타내는 경우가 많습니다.
    answer: a
  question_placements:
  - question_id: u9-l04-p07-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l34-daily-order-result.svg
    title: "주문 결과 한마디"
    alt: "떡볶이 주문에는 주문 완료, 메뉴 이름 오타에는 그런 메뉴는 없다는 답, 주방 고장에는 만들 수 없다는 답이 차례로 나타납니다."
    caption: "가게의 첫마디는 결과의 단서일 뿐 원인을 모두 말하지는 않습니다."
    after_paragraph: 0
  - file: assets/animations/l34-status-codes.svg
    title: "상태 코드"
    alt: "GET /example-page에는 200 OK, 오타가 난 GET /exmaple-page에는 404 Not Found, 서버 처리 문제에는 500 Internal Server Error가 차례로 돌아옵니다."
    caption: "200은 성공, 404는 자원을 찾지 못함, 5xx는 서버 처리 문제의 단서입니다."
    after_paragraph: 1
- terms:
  - GET / POST
  - HEAD / PUT / DELETE
  questions:
  - id: u9-l04-p08-q01
    kind: choice
    difficulty: easy
    prompt: GET과 POST의 주된 쓰임을 바르게 고른 것은 무엇인가요?
    choices:
    - id: a
      text: GET은 정보 제출, POST는 자원 조회에만 쓴다
      feedback: 주된 쓰임을 반대로 읽었으며 실제 동작은 서버와 표준 규칙도 함께 봐야 합니다.
    - id: b
      text: GET은 로그인 전용, POST는 이미지 조회 전용이다
      feedback: 특정 화면에만 한정되지 않으며 주로 조회와 제출의 의도로 구별합니다.
    - id: c
      text: GET과 POST는 모두 응답 상태 코드다
      feedback: 메서드는 요청 작업의 종류이고 상태 코드는 응답 처리 결과입니다.
    - id: d
      text: GET은 자원 조회, POST는 정보 제출에 흔히 쓴다
      feedback: 맞아요. 메서드는 원하는 작업의 종류를 나타내며 이 구별이 기본적인 쓰임입니다.
    - id: e
      text: GET과 POST는 모두 요청할 서버 이름이다
      feedback: 서버 이름이 아니라 요청의 의도를 나타내는 메서드입니다.
    answer: d
  - id: u9-l04-p08-q02
    kind: choice
    difficulty: medium
    prompt: 본인이 사용하는 서비스에서 상품 목록을 조회하고 회원가입 양식을 제출합니다. 본문에 맞는 설명은 무엇인가요?
    choices:
    - id: a
      text: 조회에는 POST만, 양식 제출에는 GET만 써야 한다
      feedback: 본문의 일반적인 쓰임은 GET 조회, POST 제출입니다.
    - id: b
      text: 조회에는 GET, 양식 제출에는 POST를 흔히 쓰며 실제 서버 동작도 확인한다
      feedback: 맞아요. 조회와 제출을 구별하되 메서드 의미는 서버 동작과 표준 규칙 안에서 이해합니다.
    - id: c
      text: 회원가입은 파일 업로드가 아니므로 POST를 쓸 수 없다
      feedback: POST를 업로드로만 외우면 정보 제출 같은 실제 쓰임을 놓칩니다.
    - id: d
      text: 상품 목록은 파일 다운로드가 아니므로 GET을 쓸 수 없다
      feedback: GET은 파일 다운로드에 한정하지 않고 자원 조회에 주로 씁니다.
    - id: e
      text: 어떤 서버든 메서드 이름만 같으면 내부 동작까지 모두 같다
      feedback: 실제 동작은 서버와 표준 규칙 안에서 정해지므로 이름만으로 내부 동작을 모두 단정하지 않습니다.
    answer: b
  question_placements:
  - question_id: u9-l04-p08-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l34-daily-kinds-of-asks.svg
    title: "부탁의 종류"
    alt: "메뉴판 보기, 회원 가입서 제출, 가격만 묻기, 주문 바꾸기·취소 부탁이 차례로 나타나고, 마지막에 남의 가게 주문을 함부로 바꾸지 않는다고 표시됩니다."
    caption: "부탁마다 원하는 일이 다르고, 가능한 일은 가게가 정해 둡니다."
    after_paragraph: 0
  - file: assets/animations/l34-http-methods.svg
    title: "HTTP Method"
    alt: "GET은 자원 조회, POST는 로그인 양식 같은 정보 제출, HEAD는 본문 없이 헤더만, PUT과 DELETE는 만들기·바꾸기와 삭제를 나타내며 차례로 나타납니다."
    caption: "GET은 주로 조회, POST는 주로 제출에 쓰이며, Method는 요청의 의도를 나타내는 표준 이름입니다."
    after_paragraph: 2
- terms: []
  questions:
  - id: u9-l04-p09-q01
    kind: choice
    difficulty: easy
    prompt: URL을 입력한 뒤 본문의 예시에서 이어지는 순서는 무엇인가요?
    choices:
    - id: a
      text: HTTP 응답 → DNS가 IP 찾기 → TCP 연결 → 결과 표시
      feedback: 예시에서는 목적지 주소와 연결을 준비한 뒤 HTTP 요청과 응답이 오갑니다.
    - id: b
      text: TCP 연결 → 결과 표시 → DNS가 IP 찾기 → HTTP 요청
      feedback: 주소를 먼저 찾고 연결한 뒤 요청과 응답을 거쳐 결과를 표시합니다.
    - id: c
      text: DNS가 IP 찾기 → 결과 표시 → HTTP 요청·응답 → TCP 연결
      feedback: 화면 표시 전에 연결과 요청·응답 단계가 필요합니다.
    - id: d
      text: HTTP 요청 → 결과 표시 → TCP 연결 → DNS가 IP 찾기
      feedback: 본문의 예시는 DNS와 TCP 단계를 거친 뒤 HTTP로 요청합니다.
    - id: e
      text: DNS가 IP 찾기 → TCP 연결 → HTTP 요청·응답 → 결과 표시
      feedback: 맞아요. 본문의 흐름은 주소 조회와 연결을 거쳐 웹 메시지를 주고받고 화면을 표시합니다.
    answer: e
  - id: u9-l04-p09-q02
    kind: choice
    difficulty: medium
    prompt: DNS로 IP를 찾고 TCP 연결도 만들었습니다. 이제 GET /example-page를 보내는 단계의 역할은 무엇인가요?
    choices:
    - id: a
      text: DNS 규칙으로 서버 IP 주소를 처음 알아낸다
      feedback: 상황에서 IP 주소는 이미 DNS로 찾았으며 GET은 HTTP 요청입니다.
    - id: b
      text: URL을 다시 정해야만 TCP 연결을 시작할 수 있다
      feedback: 주어진 상황은 이미 연결을 만든 뒤 요청을 보내는 단계입니다.
    - id: c
      text: HTTP 규칙으로 자원을 요청하고 서버의 처리 결과를 받는다
      feedback: 맞아요. 주소를 찾는 DNS와 연결을 만드는 TCP를 거쳐 HTTP 요청·응답 단계로 이어집니다.
    - id: d
      text: TCP가 HTML 내용을 직접 만들어 브라우저로 응답한다
      feedback: HTML 응답은 서버가 요청을 처리해 보내며 TCP 자체가 내용을 만드는 것이 아닙니다.
    - id: e
      text: 서버 응답 없이 브라우저가 요청한 문서를 확정해 표시한다
      feedback: 본문의 예시는 서버가 HTML을 응답한 뒤 브라우저가 그 문서를 표시합니다.
    answer: c
  question_placements:
  - question_id: u9-l04-p09-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l34-daily-name-to-meal.svg
    title: "가게 이름에서 음식까지"
    alt: "가게 이름으로 지도 앱에서 위치를 찾고, 가게까지 길을 잇고, 떡볶이를 주문해 받은 뒤 먹는 단계가 차례로 나타납니다."
    caption: "찾기, 가기, 주문, 받기는 단계마다 하는 일이 다릅니다."
    after_paragraph: 0
  - file: assets/animations/l34-url-to-response-flow.svg
    title: "URL에서 응답까지"
    alt: "URL과 DNS가 www.example.com의 예시 IP 주소를 찾고, TCP 연결을 만든 뒤, HTTP로 GET /example-page를 보내 200 OK와 HTML을 받고, 브라우저가 화면에 표시합니다."
    caption: "URL 선택 → DNS가 IP 찾기 → TCP 연결 → HTTP 요청·응답 → 브라우저 표시. IP 주소는 예시입니다."
    after_paragraph: 1
animations_dir: units/06-web-fundamentals/lessons/04-굵고-짧게-살펴보는-http/assets/animations
---

브라우저에서 웹페이지를 열면 브라우저와 서버가 HTTP 규칙에 따라 요청과 응답을 주고받습니다. 먼저 한 번의 요청을 읽고, 마지막에 DNS·TCP·HTTP가 이어지는 흐름으로 묶어 봅니다.

## HTTP는 웹 요청과 응답의 약속이다
<!-- learn-page-id: http-definition -->
<!-- Source: Wiki lesson-34, “HTTP와 TCP Stream”; TCP stream details are intentionally kept brief here. -->

HTTP(Hypertext Transfer Protocol)는 브라우저와 웹 서버가 웹 자원을 요청하고 응답할 때 따르는 규칙입니다. 브라우저는 클라이언트(Client), 요청을 받아 처리하는 프로그램은 서버(Server)입니다. 예를 들어 브라우저가 페이지를 달라고 요청하면 서버가 결과를 돌려줍니다.

이 예시에서 HTTP/1.1은 메시지를 주고받는 규칙이고, TCP/IP는 데이터를 네트워크로 옮기는 데 쓰입니다. TCP는 데이터를 이어진 흐름(stream)으로 전달하므로 HTTP 규칙에 맞춰 요청과 응답을 구분합니다. 여기서는 TCP의 세부 동작은 다루지 않습니다.

**기억할 한 줄:** HTTP는 웹 자원을 주고받는 약속이고, 클라이언트가 요청하면 서버가 응답합니다.


## 요청과 응답은 첫 줄과 헤더, 본문으로 읽는다
<!-- Source: Wiki lesson-34, “HTTP 메시지를 해석하는 규칙”; request/response lines are simplified examples. -->

HTTP 메시지는 보통 첫 줄(start-line), 헤더(header), 빈 줄, 본문(body) 순서로 읽습니다. 다음은 페이지를 달라는 요청 예입니다.

```http
GET /example-page HTTP/1.1
Host: www.example.com
```

첫 줄은 GET 방식으로 `/example-page`를 요청한다고 말합니다. `Host` 헤더는 어느 사이트를 요청하는지 알려 줍니다. 서버 응답은 다음처럼 생길 수 있습니다.

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
  <body><h1>안녕, 웹!</h1></body>
</html>
```

헤더와 본문 사이에는 빈 줄이 있어 여기서부터 실제 응답 내용이 시작된다고 알립니다. `200 OK`는 요청을 성공적으로 처리했다는 뜻입니다.

**기억할 한 줄:** 첫 줄은 요청이나 결과의 요약, 헤더는 부가 정보, 본문은 실제로 주고받는 내용입니다.


## 브라우저가 Request를 보내면 서버가 Response를 돌려준다
<!-- learn-page-id: http-request-response -->
<!-- Source: Wiki lesson-34, “Request와 Response”. -->

Request(요청)는 클라이언트가 보내는 메시지이고 Response(응답)는 서버가 돌려주는 메시지입니다. 웹페이지의 HTML을 요청할 때 브라우저는 예를 들어 `GET /example-page HTTP/1.1`을 보냅니다. 서버는 요청을 처리한 뒤 `HTTP/1.1 200 OK`와 HTML 문서를 응답할 수 있습니다.

페이지 하나를 보더라도 HTML, 이미지, CSS, JavaScript를 각각 요청할 수 있어 요청이 여러 번 생길 수 있습니다. 주소창에서 페이지를 한 번 열었다고 HTTP 메시지가 딱 하나만 오가는 것은 아닙니다.

**기억할 한 줄:** Request는 클라이언트에서 서버로, Response는 서버에서 클라이언트로 돌아옵니다.


## 개발자 도구에서 내 브라우저의 요청을 살펴본다
<!-- Source: Supplemental course guidance: inspect a learner-owned browser request in Developer Tools Network panel. -->

브라우저 개발자 도구(Developer Tools)의 Network 탭은 페이지가 불러온 요청 목록을 보여 줍니다. 항목을 누르면 요청 주소, 방식(Method), 상태 코드, 요청·응답 헤더와 본문을 확인할 수 있습니다. 처음에는 이 도구에서 본인이 직접 연 페이지의 한 요청을 골라 살펴보세요.

브라우저와 서버 사이의 HTTPS 내용은 암호화되어 이동합니다. 개발자 도구는 브라우저가 처리한 요청을 보여 주므로 학습자가 헤더와 응답을 이해하기 좋습니다. 다른 사람의 통신을 몰래 가로채어 보는 방식은 사용하지 않습니다.

**기억할 한 줄:** Network 탭에서 요청 하나를 고르면 브라우저가 무엇을 보냈고 서버가 무엇을 답했는지 볼 수 있습니다.


## 요청 Header에는 원하는 형식과 환경을 담을 수 있다
<!-- Source: Wiki lesson-34, “요청 Header에 담긴 정보”. -->

요청 헤더(header)는 첫 줄 아래에 붙는 이름과 값의 정보입니다. `Accept: text/html`은 HTML 형식의 응답을 받을 수 있음을 알리고, `Accept-Language: ko`는 한국어 응답을 선호한다고 알릴 수 있습니다. `Accept-Encoding: gzip`은 gzip 방식으로 압축된 응답을 처리할 수 있음을 알립니다. `User-Agent`는 요청을 보낸 프로그램에 관한 정보를 담을 수 있습니다.

헤더는 요청에 덧붙이는 설명이고, 요청 경로나 본문과 같은 것은 아닙니다. 쿠키처럼 로그인 상태와 관련된 값도 요청 헤더로 보내질 수 있으므로 공개 화면이나 공유 자료에 민감한 값이 보이지 않도록 주의합니다.

**기억할 한 줄:** 요청 헤더는 브라우저가 어떤 응답을 원하는지와 요청에 필요한 부가 정보를 전달합니다.


## 응답 Header는 본문의 형식과 처리 방법을 알려 준다
<!-- Source: Wiki lesson-34, “응답 Header와 Cookie”. -->

응답 헤더에는 본문이 어떤 종류인지 알려 주는 `Content-Type: text/html; charset=utf-8` 같은 정보가 올 수 있습니다. `Content-Length`는 본문의 데이터 크기를 바이트 단위로 알려 줍니다. 서버는 `Set-Cookie`로 브라우저에 쿠키를 저장하라고 알릴 수도 있습니다. 압축이나 캐시와 관련된 헤더도 사용할 수 있습니다.

헤더는 응답 본문과 구별됩니다. 예를 들어 `Content-Type`은 뒤에 올 내용이 HTML이라고 설명하고, 본문에는 실제 HTML이 들어갑니다. 브라우저는 이 정보를 참고해 응답을 처리합니다.

**기억할 한 줄:** 응답 헤더는 본문이 어떤 내용인지와 브라우저가 어떻게 다룰지 설명합니다.


## 상태 코드는 서버가 요청을 어떻게 처리했는지 보여 준다
<!-- learn-page-id: status-code-definition -->
<!-- Source: Wiki lesson-34, “HTTP 응답 코드”. -->

상태 코드(status code)는 응답 첫 줄에 있는 세 자리 숫자로, 요청 처리 결과를 요약합니다. `200 OK`는 요청이 성공적으로 처리되었음을 뜻합니다. `404 Not Found`는 서버가 요청한 자원을 찾지 못했음을 알려 줍니다. 예를 들어 주소에 오타가 있거나 서버에서 삭제된 이미지 경로를 요청하면 404 응답이 올 수 있습니다.

`4xx`는 요청 쪽에서 해결할 문제가 있음을 나타내는 경우가 많고, `5xx`는 서버가 요청을 처리하는 중 문제를 만났음을 나타내는 경우가 많습니다. 코드는 단서이지, 원인을 모두 설명하는 진단서는 아닙니다.

**기억할 한 줄:** 200은 성공, 404는 요청한 자원을 찾지 못함, 5xx는 서버 처리 문제의 단서입니다.


## Method는 요청이 원하는 일을 나타낸다
<!-- Source: Wiki lesson-34, “GET·POST 등 Method”. -->

Method(메서드)는 요청이 어떤 종류의 작업을 원하는지 나타냅니다. `GET`은 자원을 조회할 때 주로 쓰고, `POST`는 서버에 정보를 제출할 때 흔히 씁니다. 예를 들어 아이디와 비밀번호를 입력해 로그인하거나 회원가입 양식을 보낼 때 POST를 쓸 수 있습니다.

GET을 단순히 “다운로드”, POST를 “업로드”로만 외우면 실제 쓰임을 놓칠 수 있습니다. Method의 정확한 의미는 서버가 정한 동작과 표준 규칙 안에서 이해해야 합니다. 다른 사람의 서버에 데이터를 바꾸는 요청을 함부로 보내면 안 됩니다.

`HEAD`는 본문 없이 응답 헤더를 요청하고, `PUT`과 `DELETE`는 각각 자원을 만들거나 바꾸기, 삭제하기를 요청할 때 쓰일 수 있습니다. 실제 동작은 서버와 표준 규칙에 따라 정해집니다.

**기억할 한 줄:** GET은 주로 조회, POST는 주로 제출에 쓰이지만, Method는 요청의 의도를 나타내는 표준 이름입니다.


## URL에서 응답까지 이어지는 흐름을 한 번에 본다
<!-- Source: Supplemental course synthesis connecting Units 7, 9 and 10. -->

브라우저에 URL을 입력하면 먼저 DNS가 도메인 이름에 맞는 IP 주소를 찾습니다. 브라우저는 그 서버와 TCP 연결을 만들고, HTTP 규칙으로 `GET /example-page` 요청을 보냅니다. 서버는 요청을 처리해 `200 OK`와 HTML을 응답할 수 있고, 브라우저는 그 문서를 화면에 표시합니다.

각 단계의 질문은 다릅니다. URL은 어느 자원을 요청할지, DNS는 서버의 IP 주소가 무엇인지, TCP는 서버와 데이터를 주고받을 연결을, HTTP는 요청과 응답의 형식을 다룹니다. 다음 Unit에서는 이 요청이 웹 서버와 애플리케이션 안에서 어떻게 처리되는지 살펴봅니다.

**기억할 한 줄:** URL 선택 → DNS가 IP 찾기 → TCP 연결 → HTTP 요청·응답 → 브라우저가 결과 표시.
