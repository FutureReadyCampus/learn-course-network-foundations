---
id: u6-l33-url과-uri
title: '웹 주소를 읽는 법: URI와 URL'
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-33.md
wiki_diagram: units/06-web-fundamentals/lessons/03-url과-uri/assets/diagrams/lesson-33.svg
page_metadata:
- terms:
  - URL(Uniform Resource Locator)
  - URI(Uniform Resource Identifier)
  questions:
  - id: u9-l03-p01-q01
    kind: choice
    difficulty: easy
    prompt: URI와 URL의 관계를 바르게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: URI는 URL보다 좁은 범주다
      feedback: 범위가 반대입니다. URI가 더 넓고 URL이 그 안에 포함됩니다.
    - id: b
      text: URI와 URL은 항상 같은 범위다
      feedback: 일상에서 비슷하게 쓰여도 개념의 범위는 다릅니다.
    - id: c
      text: URL은 위치와 접근 방법을 나타내는 URI다
      feedback: 맞아요. URI라는 넓은 범주 안에 위치와 접근 방법을 나타내는 URL이 있습니다.
    - id: d
      text: URL은 URI와 관계없는 형식이다
      feedback: URL은 URI에 속하는 형식입니다.
    - id: e
      text: URI는 위치를 나타내는 주소에만 붙이는 말이다
      feedback: URI는 자원 식별의 넓은 개념이고 위치와 방법을 적은 것은 URL입니다.
    answer: c
  - id: u9-l03-p01-q02
    kind: choice
    difficulty: medium
    prompt: 친구가 https://www.example.com/을 URL이라고 불렀습니다. 알맞은 설명은 무엇인가요?
    choices:
    - id: a
      text: 위치와 접근 방법을 적었으므로 URI에도 해당한다
      feedback: 맞아요. 이 주소는 URL이면서 URI라는 넓은 범주에도 포함됩니다.
    - id: b
      text: URL로 불렀으므로 URI로는 부를 수 없다
      feedback: URL은 URI의 한 종류라 두 이름이 서로 배타적이지 않습니다.
    - id: c
      text: 주소창에 넣을 수 있으므로 모든 URI가 URL이라는 뜻이다
      feedback: 이 주소가 URL인 사실로 모든 URI가 위치를 나타낸다고 일반화할 수 없습니다.
    - id: d
      text: 사이트 주소는 자원을 식별하지 않으므로 URI가 아니다
      feedback: 위치와 방법을 적은 주소도 자원을 식별하는 URI입니다.
    - id: e
      text: 웹 주소라는 일상 표현을 쓰면 URL이 아니게 된다
      feedback: 웹 주소라는 일상 표현과 URL이라는 분류는 함께 쓸 수 있습니다.
    answer: a
  question_placements:
  - question_id: u9-l03-p01-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l33-daily-name-tag-scope.svg
    title: "이름표와 위치 쪽지"
    alt: "책을 가리키는 이름표라는 큰 상자 안에, 찾아갈 위치와 방법까지 적은 쪽지라는 작은 상자가 나타나고 그 안에 도서관 쪽지 예시가 보입니다."
    caption: "위치 쪽지는 이름표의 한 종류이고, 이름표가 더 큰 범위입니다."
    after_paragraph: -1
  - file: assets/animations/l33-uri-url-scope.svg
    title: "URI와 URL의 범위"
    alt: "URI라는 큰 범주 상자 안에 URL 상자가 나타나고, 그 안에 예시 주소 https://www.test.co.kr:8080/data/index.html?search_keyword=Test#result가 보입니다. 마지막에는 URL이 URI 안에 들어간다고 표시됩니다."
    caption: "URI는 자원을 식별하는 큰 범주이고, URL은 위치와 접근 방법을 나타내는 URI입니다."
    after_paragraph: 0
- terms:
  - 자원(Resource)
  - HTML · CSS · JS
  questions:
  - id: u9-l03-p02-q01
    kind: choice
    difficulty: easy
    prompt: 웹에서 말하는 자원(Resource)의 예로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 브라우저에 보이는 HTML 문서만
      feedback: CSS, JavaScript, 사진, API 데이터도 자원입니다.
    - id: b
      text: 디스크에 저장된 이미지 파일만
      feedback: 이미지 외에 문서나 요청 시 만들어 보내는 데이터도 자원입니다.
    - id: c
      text: 사이트의 첫 화면에 들어가는 문서만
      feedback: 첫 화면에 한정하지 않고 다양한 문서와 파일을 자원으로 다룹니다.
    - id: d
      text: 서버에 미리 저장해 둔 파일만
      feedback: 서버가 요청을 처리해 그때 만든 데이터도 자원이 될 수 있습니다.
    - id: e
      text: HTML 문서와 사진, API가 보내는 데이터
      feedback: 맞아요. 파일뿐 아니라 웹에서 식별해 다루는 API 데이터도 자원에 포함됩니다.
    answer: e
  - id: u9-l03-p02-q02
    kind: choice
    difficulty: medium
    prompt: 서버가 요청을 받을 때마다 새 JSON 데이터를 만들어 보냅니다. 이 데이터도 자원인가요?
    choices:
    - id: a
      text: 아니다. 미리 저장된 파일만 자원이다
      feedback: 서버가 요청을 처리해 만든 데이터도 자원이라고 설명했습니다.
    - id: b
      text: 그렇다. 요청에 따라 만들어 보내는 데이터도 자원이다
      feedback: 맞아요. 자원은 저장된 파일에 한정되지 않아 동적으로 만든 JSON도 포함됩니다.
    - id: c
      text: 아니다. HTML 문서만 자원이다
      feedback: API가 JSON 형식으로 돌려주는 데이터도 자원입니다.
    - id: d
      text: 아니다. 사진처럼 화면에 보이는 것만 자원이다
      feedback: 자원은 눈에 보이는 사진 외에 코드와 데이터도 포함합니다.
    - id: e
      text: 그렇다. 다만 JSON을 사진 파일로 바꿔야 한다
      feedback: JSON 그대로도 자원으로 다룰 수 있어 사진으로 바꿀 필요가 없습니다.
    answer: b
  question_placements:
  - question_id: u9-l03-p02-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l33-daily-library-items.svg
    title: "도서관에서 받을 수 있는 것"
    alt: "책, 사진집, 지도, DVD가 차례로 나타나고, 사서가 그때 뽑아 만드는 대출 목록이 이어서 나타납니다. 마지막에는 필요한 것을 각각 받아 모읍니다."
    caption: "도서관에서는 책뿐 아니라 여러 가지를 따로 받아 볼 수 있습니다."
    after_paragraph: -1
  - file: assets/animations/l33-web-resources.svg
    title: "웹 자원의 여러 모습"
    alt: "HTML 문서, CSS 디자인 파일, JavaScript 코드, JPG 사진, API가 그때 만드는 JSON 데이터가 차례로 나타나고, 마지막에 브라우저가 이 자원들을 모아 화면을 만듭니다."
    caption: "문서, 파일, 이미지, API 데이터처럼 웹에서 식별해 다룰 수 있는 것이 자원입니다."
    after_paragraph: 0
- terms:
  - JSON
  - 식별(identify)과 특정(locate)
  questions:
  - id: u9-l03-p03-q01
    kind: choice
    difficulty: easy
    prompt: 자원을 식별한다는 말에 가장 가까운 질문은 무엇인가요?
    choices:
    - id: a
      text: 어디로 가서 가져오는가?
      feedback: 이 질문은 위치 지정에 해당하며 식별이라는 넓은 질문과 구별됩니다.
    - id: b
      text: 어떤 방법으로 가져오는가?
      feedback: 접근 방법은 위치와 함께 URL이 나타내는 정보입니다.
    - id: c
      text: 찾아갈 장소가 어디인가?
      feedback: 찾아갈 장소는 위치를 묻는 질문입니다.
    - id: d
      text: 어떤 자원인가?
      feedback: 맞아요. 식별은 어떤 대상을 가리키는지 구분하는 일입니다.
    - id: e
      text: 접근할 위치와 방법은 무엇인가?
      feedback: 이것은 위치와 접근 방법을 나타내는 URL 쪽 질문입니다.
    answer: d
  - id: u9-l03-p03-q02
    kind: choice
    difficulty: medium
    prompt: 사람의 신분 번호와 집 주소에 빗대어 URI와 URL을 이해한 설명으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 신분 번호가 집 주소보다 찾아갈 위치를 잘 알려 준다
      feedback: 신분 번호는 누구인지 구분하고 집 주소가 찾아갈 위치를 알려 줍니다.
    - id: b
      text: 집 주소는 위치를 나타내므로 식별과는 전혀 관계없다
      feedback: URL도 URI에 속합니다. 비유의 두 질문을 구별하되 완전히 무관하다고 보지 않습니다.
    - id: c
      text: 신분 번호는 식별을, 집 주소는 찾아갈 위치를 설명하는 비유다
      feedback: 맞아요. 누구인가와 어디로 가야 하는가를 나누어 생각하기 위한 비유입니다.
    - id: d
      text: 비유에 따르면 웹 자원은 사람의 신분 정보와 같은 종류다
      feedback: 본문은 이해를 위한 비유이며 같은 종류라는 뜻은 아니라고 밝혔습니다.
    - id: e
      text: 신분 번호와 집 주소는 모두 어디로 갈지만 알려 준다
      feedback: 신분 번호는 누구인가, 집 주소는 어디로 갈 것인가를 설명합니다.
    answer: c
  question_placements:
  - question_id: u9-l03-p03-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l33-daily-name-vs-address.svg
    title: "누구인지와 어디 있는지"
    alt: "민수라는 친구를 가운데 두고, 왼쪽에는 누구인지 알려 주는 이름과 신분 번호, 오른쪽에는 어디서 만날지 알려 주는 집 주소가 차례로 나타납니다."
    caption: "이름은 누구인지, 주소는 어디 있는지에 답합니다."
    after_paragraph: -1
  - file: assets/animations/l33-identify-vs-locate.svg
    title: "식별과 위치 지정"
    alt: "자원 하나를 가운데 두고, 왼쪽에는 어떤 자원인지 식별하는 URI, 오른쪽에는 어디서 어떻게 가져올지 알려 주는 URL이 차례로 나타납니다."
    caption: "자원은 대상이고, URI는 대상을 식별하며, URL은 접근할 위치를 알려 줍니다. 사람 비유는 이해를 돕기 위한 것입니다."
    after_paragraph: 0
- terms:
  - Scheme(스킴)
  - Authority · Path · Query · Fragment
  animations:
  - file: l33-uri-parts.svg
    title: 주소 한 줄은 칸이 나뉜 운송장
    alt: 한 줄로 쓰인 웹 주소가 방식, 호스트, 포트, 경로, 쿼리 다섯 조각으로 색이 나뉘며 택배 운송장의 칸으로 옮겨 가는 장면입니다.
    caption: https://www.test.co.kr:8080/data/index.html?search_keyword=Test 는 방식,
      호스트, 포트, 경로, 쿼리 칸으로 나뉩니다.
  questions:
  - id: u9-l03-p04-q01
    kind: choice
    difficulty: easy
    prompt: 주소에서 query와 fragment를 시작하는 기호를 순서대로 고르면 무엇인가요?
    choices:
    - id: a
      text: '?와 #'
      feedback: 맞아요. 물음표는 query, 샵 기호는 fragment를 나누는 표지입니다.
    - id: b
      text: '#와 ?'
      feedback: '순서가 반대입니다. query는 ?, fragment는 #로 구분합니다.'
    - id: c
      text: /와 ?
      feedback: '슬래시는 경로에 쓰이며 fragment를 시작하는 기호는 #입니다.'
    - id: d
      text: :와 /
      feedback: '콜론과 슬래시 대신 query는 ?, fragment는 #를 확인해야 합니다.'
    - id: e
      text: '?와 :'
      feedback: 'query는 맞지만 fragment를 시작하는 것은 콜론이 아니라 #입니다.'
    answer: a
  - id: u9-l03-p04-q02
    kind: choice
    difficulty: medium
    prompt: https://shop.example/items?sort=new#list를 부분별로 읽은 설명 중 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 경로는 sort=new, query는 /items, fragment는 list다
      feedback: 경로와 query가 바뀌었습니다. /items는 경로입니다.
    - id: b
      text: scheme은 shop.example이고 authority는 https다
      feedback: scheme과 authority가 바뀌었습니다. https가 방식입니다.
    - id: c
      text: fragment는 sort=new이고 query는 list다
      feedback: '? 뒤 query와 # 뒤 fragment를 반대로 읽었습니다.'
    - id: d
      text: 포트가 없으므로 여러 부분으로 나눌 수 없는 주소다
      feedback: 모든 주소에 포트를 명시할 필요는 없고 나머지 부분도 구분할 수 있습니다.
    - id: e
      text: 경로는 /items, query는 sort=new, fragment는 list다
      feedback: '맞아요. 슬래시 뒤 경로, ? 뒤 조건, # 뒤 문서 내 위치를 구별한 설명입니다.'
    answer: e
  question_placements:
  - question_id: u9-l03-p04-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l33-daily-note-cells.svg
    title: "도서관 쪽지를 칸으로 나눠요"
    alt: "도서관 쪽지 한 줄을 방법, 건물, 창구, 서가와 책, 조건, 책 속 위치 칸으로 나누고, 마지막에 창구 번호와 책 속 위치가 빠질 수 있다고 표시합니다."
    caption: "한 줄을 통째로 외우지 않고 칸마다 나누어 읽습니다."
    after_paragraph: -1
  - file: assets/animations/l33-url-part-split.svg
    title: "주소를 부분으로 나누어 읽기"
    alt: "예시 주소 https://www.test.co.kr:8080/data/index.html?search_keyword=Test#result에서 구분 기호를 찾고, scheme, host와 port를 묶은 authority, path, query, fragment로 나눕니다. 마지막에 port와 fragment가 생략될 수 있다고 표시됩니다."
    caption: "구분 기호를 따라 scheme·authority·path·query·fragment로 나누어 읽습니다."
    after_paragraph: 0
- terms:
  - 프로토콜(protocol)
  - 호스트(host)
  - 포트 번호(port number)
  questions:
  - id: u9-l03-p05-q01
    kind: choice
    difficulty: easy
    prompt: URL에서 Host와 Port를 바르게 구별한 것은 무엇인가요?
    choices:
    - id: a
      text: Host는 서비스 번호, Port는 서버 이름이다
      feedback: 역할이 반대입니다. Host는 서버 이름이고 Port는 번호입니다.
    - id: b
      text: Host는 서버 이름, Port는 서비스 연결점 번호다
      feedback: 맞아요. 호스트는 어느 서버인지, 포트는 그 컴퓨터의 어떤 서비스에 연결할지 구별합니다.
    - id: c
      text: Host는 요청 경로, Port는 서버 이름이다
      feedback: Host는 서버를 가리키며 경로는 그 서버의 요청 자원을 가리킵니다.
    - id: d
      text: Host와 Port는 모두 요청할 파일 경로다
      feedback: 서버 이름과 서비스 번호는 파일 경로와 다른 정보입니다.
    - id: e
      text: Host와 Port는 모두 요청 방식을 뜻한다
      feedback: 요청 방식은 scheme 자리에 나타나며 Host와 Port와 구별됩니다.
    answer: b
  - id: u9-l03-p05-q02
    kind: choice
    difficulty: medium
    prompt: https://shop.example:8443/news에서 서버 이름과 서비스 번호, 요청 경로를 바르게 고른 것은 무엇인가요?
    choices:
    - id: a
      text: https / 8443 / shop.example
      feedback: https는 방식이고 shop.example이 서버 이름입니다.
    - id: b
      text: shop.example / 443 / /news
      feedback: 이 주소에는 기본값 대신 8443이 명시되어 있습니다.
    - id: c
      text: shop.example / /news / 8443
      feedback: 서비스 번호와 요청 경로를 바꾸어 읽었습니다.
    - id: d
      text: shop.example / 8443 / /news
      feedback: 맞아요. 호스트 뒤 콜론의 번호가 포트이고 그 뒤 /news가 요청 경로입니다.
    - id: e
      text: shop.example:8443 / 80 / /news
      feedback: 호스트 이름과 포트를 나누어 읽어야 하며 명시된 번호는 8443입니다.
    answer: d
  question_placements:
  - question_id: u9-l03-p05-q01
    after_paragraph: 5
  illustrations:
  - file: assets/animations/l33-daily-method-building-desk.svg
    title: "방법, 건물, 창구"
    alt: "도서관 쪽지에서 빌리기라는 방법, 한빛도서관이라는 건물, 8번 창구가 차례로 강조되고, 기본 창구라면 번호를 빼고 적는다고 표시됩니다."
    caption: "어떻게 요청할지, 어느 곳에 갈지, 어느 창구에서 볼지를 나누어 봅니다."
    after_paragraph: -1
  - file: assets/animations/l33-scheme-host-port.svg
    title: "Scheme, Host, Port"
    alt: "예시 주소에서 scheme https, host www.test.co.kr, port 8080이 차례로 강조되며 각각 요청 방식, 서버 이름, 서비스 번호로 설명됩니다. 마지막에 HTTPS 기본 포트 443이면 생략한다고 표시됩니다."
    caption: "Host는 서버 이름, Port는 서비스 번호, Path는 요청할 자원을 가리킵니다."
    after_paragraph: 0
- terms:
  - 절대 경로(absolute path)
  - 상대 경로(relative path)
  questions:
  - id: u9-l03-p06-q01
    kind: choice
    difficulty: easy
    prompt: 상대 경로를 읽을 때 기준으로 삼는 것은 무엇인가요?
    choices:
    - id: a
      text: 항상 웹사이트의 기준점
      feedback: 사이트 기준점에서 시작하는 / 경로와 상대 경로를 구별해야 합니다.
    - id: b
      text: 항상 컴퓨터 디스크 전체의 시작점
      feedback: 상대 경로는 현재 문서 위치를 기준으로 읽습니다.
    - id: c
      text: 현재 문서의 위치
      feedback: 맞아요. 상대 경로는 현재 문서가 있는 위치를 기준으로 목적지를 적습니다.
    - id: d
      text: 항상 바로 위 폴더
      feedback: 위 폴더 이동은 .. 기호가 있을 때 적용하며 기준 자체는 현재 위치입니다.
    - id: e
      text: 링크가 가리키는 목적지 폴더
      feedback: 목적지가 아니라 링크를 읽는 현재 문서 위치가 기준입니다.
    answer: c
  - id: u9-l03-p06-q02
    kind: choice
    difficulty: medium
    prompt: 현재 문서가 /data/index.html입니다. ../images/logo.png와 /images/logo.png를 읽은 설명으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 앞 경로는 한 단계 위로 이동하고 뒤 경로는 사이트 기준점에서 시작한다
      feedback: 맞아요. ..은 위 폴더 이동이고 맨 앞 /는 사이트 기준점에서 시작한다는 뜻입니다.
    - id: b
      text: 두 경로 모두 data 폴더 아래 images에서 시작한다
      feedback: ..은 data보다 위로 이동하며 맨 앞 /도 data를 기준으로 하지 않습니다.
    - id: c
      text: 앞 경로는 사이트 기준점, 뒤 경로는 현재 위치에서 시작한다
      feedback: 상대 경로와 /로 시작하는 절대 경로의 기준을 반대로 설명했습니다.
    - id: d
      text: 앞 경로의 ..은 두 단계 위로 이동한다
      feedback: .. 하나는 한 단계 위 폴더를 뜻합니다.
    - id: e
      text: 뒤 경로는 서버 디스크 전체의 시작점에서 찾는다
      feedback: 웹의 / 경로는 사이트 기준점을 뜻하며 디스크 전체 시작점이 아닙니다.
    answer: a
  question_placements:
  - question_id: u9-l03-p06-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l33-daily-shelf-route.svg
    title: "지금 자리에서, 또는 입구에서"
    alt: "과학 서가의 공룡책 앞에서 한 단계 위로 나간 뒤 사진 서가의 지도책으로 찾아가고, 마지막에는 도서관 입구부터 같은 지도책까지 가는 길이 표시됩니다."
    caption: "지금 위치에서 출발하는 길과 입구에서 출발하는 길을 구분합니다."
    after_paragraph: -1
  - file: assets/animations/l33-relative-absolute-path.svg
    title: "상대 경로와 절대 경로"
    alt: "/data/index.html에서 ../로 한 단계 위 폴더로 간 뒤 images/logo.png를 찾아가고, 마지막에는 /images/logo.png처럼 사이트 기준점에서 바로 출발하는 경로가 표시됩니다."
    caption: "상대 경로는 현재 위치를 기준으로, /로 시작하는 웹 경로는 사이트 기준점에서 시작합니다."
    after_paragraph: 1
- terms:
  - 웹 루트(web root)
  - 기본 문서(default document)
  animations:
  - file: l33-web-root-path.svg
    title: 주소의 / 는 서버가 열어 둔 로비
    alt: 서버 디스크의 폴더 그림에서 C 드라이브와 web 폴더 부분은 흐려지고, 웹 루트부터 data 폴더와 index.html까지 이어지는
      경로가 브라우저 주소창의 /data/index.html과 연결되는 장면입니다.
    caption: 브라우저 주소의 경로는 디스크 전체가 아니라 웹 루트에서 시작합니다.
  questions:
  - id: u9-l03-p07-q01
    kind: choice
    difficulty: easy
    prompt: 웹 서버의 문서 루트는 무엇인가요?
    choices:
    - id: a
      text: 서버 디스크에 있는 모든 폴더
      feedback: 웹 루트는 공개하도록 정한 범위이며 디스크 전체와 같지 않습니다.
    - id: b
      text: 브라우저가 설치된 폴더
      feedback: 문서 루트는 브라우저가 아니라 웹 서버가 공개하는 시작 폴더입니다.
    - id: c
      text: 사용자가 마지막으로 방문한 문서
      feedback: 문서 루트는 방문 기록이 아니라 공개 폴더의 기준점입니다.
    - id: d
      text: 어느 서버에서나 고정된 index.html 파일
      feedback: 루트는 시작 폴더이고 기본 문서 파일과 구별됩니다.
    - id: e
      text: 웹에서 공개하도록 정한 시작 폴더
      feedback: 맞아요. 브라우저의 경로는 서버가 공개한 문서 루트 안에서 해석될 수 있습니다.
    answer: e
  - id: u9-l03-p07-q02
    kind: choice
    difficulty: medium
    prompt: 어떤 서버에서 / 요청에 index.html이 돌아왔습니다. 다른 서버의 / 요청도 반드시 같을까요?
    choices:
    - id: a
      text: 그렇다. /는 언제나 index.html이라는 고정 파일 이름이다
      feedback: /는 index.html 자체의 고정 이름이 아니며 기본 문서는 설정에 따릅니다.
    - id: b
      text: 아니다. 기본 문서는 각 서버 설정에 따라 달라질 수 있다
      feedback: 맞아요. 경로가 없거나 /인 요청에 어떤 문서를 돌려줄지는 서버 설정에 달려 있습니다.
    - id: c
      text: 그렇다. 브라우저가 모든 서버의 기본 문서를 정한다
      feedback: 어떤 기본 문서를 쓸지는 웹 서버 설정이 정합니다.
    - id: d
      text: 아니다. /는 언제나 서버 디스크 전체 목록을 반환한다
      feedback: /는 공개한 웹 루트 기준이며 디스크 전체 목록을 뜻하지 않습니다.
    - id: e
      text: 아니다. / 요청은 어떤 서버에서도 문서를 돌려줄 수 없다
      feedback: 설정에 따라 index.html 같은 기본 문서를 돌려줄 수 있습니다.
    answer: b
  question_placements:
  - question_id: u9-l03-p07-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l33-daily-open-reading-room.svg
    title: "공개된 열람실 안에서 찾아요"
    alt: "도서관 건물 안에서 직원실은 닫혀 있고 열람실만 공개됩니다. 과학 서가/공룡책 요청은 열람실 안에서 찾고, 그냥 온 손님에게는 도서관이 정한 안내 책자를 줍니다."
    caption: "손님의 요청은 공개된 열람실 안에서 찾습니다."
    after_paragraph: -1
  - file: assets/animations/l33-document-root-default.svg
    title: "웹 서버의 문서 루트"
    alt: "서버 디스크 전체 가운데 비공개 파일은 닫혀 있고 문서 루트만 공개됩니다. /data/index.html 요청은 루트 아래 data 폴더에서 찾고, / 요청에는 서버 설정이 정한 기본 문서 index.html을 줍니다."
    caption: "브라우저 경로는 서버가 공개한 웹 루트에서 시작하고, / 요청의 기본 문서는 서버가 정합니다."
    after_paragraph: 0
- terms:
  - 동적 처리
  - 클라이언트(client)
  questions:
  - id: u9-l03-p08-q01
    kind: choice
    difficulty: easy
    prompt: 클라이언트가 보내는 URL 경로에 대한 설명으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 반드시 디스크의 같은 이름 파일을 가리킨다
      feedback: 주소의 경로가 디스크 파일 이름과 항상 일치하는 것은 아닙니다.
    - id: b
      text: 반드시 프로그램이 만든 JSON만 요청한다
      feedback: 서버는 JSON 외에 HTML을 만들거나 저장된 파일을 보낼 수도 있습니다.
    - id: c
      text: 파일 확장자가 없으면 요청할 수 없다
      feedback: /products/17처럼 확장자 없는 동적 처리 경로도 가능합니다.
    - id: d
      text: 저장 파일을 가리키거나 서버의 동적 처리를 요청할 수 있다
      feedback: 맞아요. 경로는 요청 주소이며 파일 전달과 프로그램이 만든 응답 모두 가능합니다.
    - id: e
      text: 클라이언트가 서버 디스크 위치를 직접 정한다
      feedback: 클라이언트는 경로로 요청하며 서버가 파일이나 처리 결과를 돌려줍니다.
    answer: d
  - id: u9-l03-p08-q02
    kind: choice
    difficulty: medium
    prompt: 주소 /products/17에서 상품 정보가 표시됩니다. 이 주소만으로 알 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: 서버 디스크에 이름이 17인 파일이 반드시 있다
      feedback: 경로는 서버의 동적 처리에 연결될 수도 있어 파일이 있다고 단정할 수 없습니다.
    - id: b
      text: 파일 확장자가 없으므로 서버가 응답하지 못한다
      feedback: 서버는 확장자 없는 경로에도 요청을 처리해 응답할 수 있습니다.
    - id: c
      text: 요청 경로는 알지만 실제 파일의 존재 여부는 단정할 수 없다
      feedback: 맞아요. 서버가 상품 정보를 찾아 응답을 만들 수도 있으므로 경로와 실제 파일을 동일시하지 않습니다.
    - id: d
      text: 상품 정보이므로 HTML 응답은 만들 수 없다
      feedback: 서버는 요청을 처리해 HTML이나 JSON 응답을 만들 수 있습니다.
    - id: e
      text: 이 경로는 저장 파일을 보내는 방식으로만 처리한다
      feedback: 주소 모양만으로 저장 파일 전달인지 동적 처리인지 확정할 수 없습니다.
    answer: c
  question_placements:
  - question_id: u9-l03-p08-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l33-daily-fetch-or-make.svg
    title: "꺼내 주기와 만들어 주기"
    alt: "사진집을 부탁하면 서가에 꽂힌 것을 그대로 건네주고, 17번 회원 목록을 부탁하면 꽂힌 책이 없어서 사서가 그때 목록을 만들어 건네줍니다."
    caption: "부탁하는 말이 늘 꽂혀 있는 책 이름과 같지는 않습니다."
    after_paragraph: -1
  - file: assets/animations/l33-path-not-file.svg
    title: "URL 경로와 실제 파일"
    alt: "클라이언트가 /images/logo.png를 요청하면 서버가 저장된 파일을 그대로 보내고, /products/17을 요청하면 같은 이름의 파일 없이 프로그램이 HTML이나 JSON 응답을 만들어 보냅니다."
    caption: "URL의 경로는 요청 주소이고, 서버가 파일을 보내거나 프로그램으로 결과를 만들 수 있습니다."
    after_paragraph: 0
- terms:
  - Query(쿼리)
  - 매개변수(Parameter)와 값(Value)
  questions:
  - id: u9-l03-p09-q01
    kind: choice
    difficulty: easy
    prompt: ?keyword=dns에서 매개변수 이름과 값을 바르게 고른 것은 무엇인가요?
    choices:
    - id: a
      text: 이름은 keyword, 값은 dns다
      feedback: 맞아요. 이름=값 쌍에서 등호 앞이 매개변수 이름이고 뒤가 값입니다.
    - id: b
      text: 이름은 dns, 값은 keyword다
      feedback: 이름과 값이 반대입니다. 등호 앞 keyword가 이름입니다.
    - id: c
      text: 이름은 ?, 값은 keyword다
      feedback: ?는 query를 시작하는 기호이며 매개변수 이름이 아닙니다.
    - id: d
      text: 이름은 keyword=dns, 값은 없다
      feedback: keyword=dns 전체가 한 쌍이며 dns라는 값이 있습니다.
    - id: e
      text: 이름은 없고 keyword와 dns가 모두 값이다
      feedback: 등호 앞 keyword는 조건을 구분하는 매개변수 이름입니다.
    answer: a
  - id: u9-l03-p09-q02
    kind: choice
    difficulty: medium
    prompt: 검색 경로 /search에 검색어 dns와 페이지 번호 2를 함께 전달하려 합니다. 알맞은 주소는 무엇인가요?
    choices:
    - id: a
      text: /search?keyword=dns?page=2
      feedback: 조건을 추가할 때는 ?를 반복하지 않고 &로 이어야 합니다.
    - id: b
      text: /search?dns=keyword&2=page
      feedback: 이름과 값을 뒤집었습니다. keyword와 page가 매개변수 이름입니다.
    - id: c
      text: /search/keyword=dns/page=2
      feedback: 이는 조건을 query 대신 경로에 넣은 형태입니다. 본문의 query 형식은 ? 뒤에 씁니다.
    - id: d
      text: /search?keyword=dns&page
      feedback: 페이지 번호를 값으로 전달하려면 page=2처럼 이름과 값을 적어야 합니다.
    - id: e
      text: /search?keyword=dns&page=2
      feedback: 맞아요. ?로 query를 시작하고 &로 두 이름=값 조건을 이었습니다.
    answer: e
  question_placements:
  - question_id: u9-l03-p09-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l33-daily-search-condition.svg
    title: "물음표 뒤에 조건을 적어요"
    alt: "쪽지의 ?검색어=공룡에서 검색어는 이름, 공룡은 값으로 나뉘고, &쪽=2가 이어 붙습니다. 마지막에 사서가 서가 위치와 따로 두 조건을 받습니다."
    caption: "? 뒤에는 이름=값 모양으로 원하는 조건을 적습니다."
    after_paragraph: -1
  - file: assets/animations/l33-query-name-value.svg
    title: "Query: 물음표 뒤의 조건"
    alt: "예시 주소의 ?search_keyword=Test에서 search_keyword는 매개변수, Test는 값으로 나뉘고, &page=2가 이어 붙습니다. 마지막에 서버가 path와 따로 두 조건을 받습니다."
    caption: "? 뒤는 Query이고, 이름=값 쌍으로 서버에 조건을 전달합니다."
    after_paragraph: 0
- terms:
  - Fragment(프래그먼트)
  - 문서 내 위치
  questions:
  - id: u9-l03-p10-q01
    kind: choice
    difficulty: easy
    prompt: '주소의 #result는 이 페이지에서 어떤 뜻으로 설명했나요?'
    choices:
    - id: a
      text: 서버에 있는 result 파일을 반드시 여는 표시
      feedback: fragment 값이 항상 서버 파일 이름인 것은 아닙니다.
    - id: b
      text: 문서 안의 result 위치를 가리키는 표시
      feedback: 맞아요. fragment는 문서 안에서 보여 줄 위치를 가리킬 수 있습니다.
    - id: c
      text: 서버에 보낼 result라는 검색 조건
      feedback: '검색 조건을 담는 query와 # 뒤 fragment는 구별됩니다.'
    - id: d
      text: 새 서버 result로 접속하는 호스트 이름
      feedback: fragment는 서버 이름이 아니라 문서 안 위치를 나타낼 수 있습니다.
    - id: e
      text: 문서를 받기 전에 찾을 디스크 폴더 이름
      feedback: 보통 브라우저가 문서를 받은 뒤 그 안의 위치를 찾는 데 씁니다.
    answer: b
  - id: u9-l03-p10-q02
    kind: choice
    difficulty: medium
    prompt: '브라우저가 https://example.com/guide#tips를 열었습니다. #tips를 해석하는 설명으로 알맞은 것은 무엇인가요?'
    choices:
    - id: a
      text: 서버는 반드시 tips라는 파일을 따로 보내야 한다
      feedback: '# 뒤 값이 항상 서버 파일 이름인 것은 아닙니다.'
    - id: b
      text: 요청 경로는 /guide#tips라는 디스크 경로가 된다
      feedback: fragment는 서버에 보낼 path와 구분되는 부분입니다.
    - id: c
      text: tips는 서버에 전달하는 query의 매개변수 이름이다
      feedback: 'query와 fragment를 혼동했습니다. 이 주소의 tips는 # 뒤에 있습니다.'
    - id: d
      text: 보통 문서를 받은 뒤 문서 안의 tips 위치를 찾는다
      feedback: 맞아요. fragment는 보통 브라우저가 받은 문서 안에서 위치를 찾는 데 사용합니다.
    - id: e
      text: tips라는 이름의 다른 서버로 접속한다
      feedback: 서버를 나타내는 부분과 달리 fragment는 문서 안 위치를 가리킬 수 있습니다.
    answer: d
  question_placements:
  - question_id: u9-l03-p10-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l33-daily-open-chapter.svg
    title: "빌린 책에서 3장을 펼쳐요"
    alt: "쪽지의 #3장이 강조되고, 사서에게는 공룡책만 빌려 달라고 합니다. 책을 받은 뒤 내가 책 안의 3장을 펼칩니다."
    caption: "책 속 위치는 책을 받은 뒤 내가 찾습니다."
    after_paragraph: -1
  - file: assets/animations/l33-fragment-in-page.svg
    title: "Fragment: 문서 안의 위치"
    alt: "예시 주소의 #result가 강조되고, 서버에는 /data/index.html?search_keyword=Test로 문서를 요청합니다. 문서를 받은 뒤 브라우저가 문서 안의 result 위치로 이동합니다."
    caption: "# 뒤의 fragment는 문서 안의 위치를 가리킬 수 있습니다."
    after_paragraph: 0
animations_dir: units/06-web-fundamentals/lessons/03-url과-uri/assets/animations
---
웹 주소를 읽을 때는 먼저 무엇을 가리키는지, 어느 서버에 요청하는지, 서버 안에서 어떤 자원을 찾는지 나누어 보면 됩니다. 아래에서는 한 가지 예시 주소를 여러 조각으로 나누어 읽습니다.

## URI는 자원을 식별하고 URL은 위치를 알려 준다
<!-- learn-page-id: uri-definition -->
<!-- Source: Wiki lesson-33, “URL과 URI의 이름”; beginner phrasing added for this course. -->

URI(Uniform Resource Identifier)는 웹에서 다루는 자원을 식별하는 형식입니다. URL(Uniform Resource Locator)은 그 자원에 접근할 위치와 방법을 나타내는 URI입니다. 주소창에 적는 `https://www.example.com/`은 흔히 URL이라고 부르는 예입니다.

개념의 크기로 보면 URI가 더 넓은 범주의 이름이고, 그중에서 실제로 찾아갈 위치와 방법을 적은 주소를 URL이라고 부릅니다. 일상 대화에서는 URL을 “웹 주소”라고 많이 부르지만 둘은 같은 범위의 말이 아닙니다.

**기억할 한 줄:** URI는 자원을 식별하는 큰 범주이고, URL은 그 자원의 위치와 접근 방법을 나타냅니다.


## 자원(Resource)은 웹에서 찾거나 받는 대상이다
<!-- Source: Wiki lesson-33, “Resource · 문서와 파일”. -->

자원(Resource)은 주소를 붙여 찾거나 서버에서 받아 볼 수 있는 대상입니다. 웹페이지의 HTML 문서뿐 아니라 글의 모양을 꾸미는 디자인 파일(CSS), 동작을 만드는 코드(JavaScript), 사진(JPG)도 자원입니다. 프로그램끼리 데이터를 주고받는 창구(API)가 JSON 형식으로 돌려주는 데이터도 자원으로 다룰 수 있습니다.

예를 들어 웹페이지 안의 글과 사진은 서로 다른 자원일 수 있고, 브라우저는 각 자원을 요청해 화면을 만듭니다. 자원은 저장된 파일만 뜻하지 않습니다. 서버가 요청을 처리해 그때 만들어 보내는 데이터도 자원이 될 수 있습니다.

**기억할 한 줄:** 문서, 이미지, 파일, API 데이터처럼 웹에서 식별해 다룰 수 있는 것이 자원입니다.


## 식별과 위치 지정은 서로 다른 질문이다
<!-- learn-page-id: url-definition -->
<!-- Source: Wiki lesson-33, “자원을 식별하고 특정하기”; the identity/location example is an added analogy. -->

“어떤 자원인가?”는 식별에 관한 질문이고, “어디로 가서 어떻게 가져오나?”는 위치 지정에 관한 질문입니다. URI는 첫 질문에 답하는 식별자라는 넓은 말이며, URL은 두 번째 질문에 답하도록 위치와 접근 방법을 나타냅니다.

사람으로 비유하면 이름이나 신분 번호는 “누구인가”를 식별하고, 집 주소는 “어디로 가야 만날 수 있는가”를 알려 줍니다. 웹에서도 자원을 가리키는 URI라는 넓은 개념이 있고, 그 자원에 접근할 위치와 방법을 적은 URL이 있습니다. 이 비유는 이해를 돕기 위한 것이며 웹 자원과 사람의 신분 정보가 같은 종류라는 뜻은 아닙니다.

**기억할 한 줄:** 자원은 대상이고, URI는 대상을 식별하며, URL은 그 대상에 접근할 위치를 알려 줍니다.


## 주소는 구분 기호를 따라 여러 부분으로 읽는다
<!-- Source: Wiki lesson-33, “URI의 문법”; aligned with the existing l33-uri-parts diagram. -->

예시 주소 `https://www.test.co.kr:8080/data/index.html?search_keyword=Test#result`를 봅시다. `https`는 방식(scheme), `www.test.co.kr:8080`은 서버를 나타내는 authority, `/data/index.html`은 경로(path), `?search_keyword=Test`는 질의(query), `#result`는 문서 안의 위치(fragment)입니다. 포트 `8080`은 예시용으로 명시한 번호입니다.

콜론, 슬래시, 물음표, 샵 기호가 부분을 나누는 표지입니다. 모든 주소에 모든 부분이 꼭 있는 것은 아닙니다. 예를 들어 포트나 fragment는 생략될 수 있습니다.

**기억할 한 줄:** 주소를 한 덩어리로 외우지 말고 구분 기호를 따라 scheme·authority·path·query·fragment로 나눕니다.


## Scheme은 접근 방법, Host는 서버 이름을 가리킨다
<!-- Source: Wiki lesson-33, “Protocol·Host·Port”. -->

주소 맨 앞의 `https`는 브라우저가 어떤 방식으로 요청할지 알려 주는 scheme입니다. 이 방식을 통신 규약, 즉 프로토콜(protocol)이라고도 하며 URL 문법에서는 scheme 자리에 적습니다. `www.test.co.kr`은 요청을 보낼 서버를 찾을 때 쓰는 호스트 이름(host)입니다. 포트 번호는 바로 아래에서 살펴보고, 경로(`/data/index.html`)는 다음 페이지에서 이어서 봅니다.

호스트 이름은 경로와 다릅니다. 호스트는 어느 서버에 갈지 알려 주고, 경로는 그 서버에서 어떤 자원을 요청할지 알려 줍니다. 같은 호스트에서 `/news`와 `/images/logo.png`처럼 서로 다른 자원을 요청할 수 있습니다.

### Port는 Host 바로 뒤에서 서비스 연결점을 고른다

Port(포트)는 한 컴퓨터에서 어떤 네트워크 서비스를 연결할지 구분하는 번호입니다. URL에서는 호스트 뒤에 콜론과 번호를 붙여 표시합니다. 기준 주소의 `www.test.co.kr:8080`에서 `8080`이 포트 번호입니다.

HTTP의 기본 포트는 80이고 HTTPS의 기본 포트는 443이라 주소에서 생략하는 경우가 흔합니다. 기본값이 아닌 포트를 쓰면 `:8080`처럼 적습니다. 포트는 서버 이름이나 요청 경로와 다른 정보입니다.

**기억할 한 줄:** Host는 서버 이름, Port는 서비스 번호, Path는 요청할 자원을 가리킵니다.



## 절대 경로는 기준점부터, 상대 경로는 현재 위치부터 쓴다
<!-- Source: Wiki lesson-33, “절대 경로와 상대 경로”. -->

절대 경로(absolute path)는 정해진 기준점부터 목적지까지 적은 경로이고, 상대 경로(relative path)는 현재 문서의 위치를 기준으로 목적지를 적은 경로입니다. 컴퓨터 폴더에서 `images/logo.png`를 현재 폴더 기준으로 찾는 상황을 떠올리면 쉽습니다.

`..`은 “현재 위치보다 한 단계 위 폴더”를 뜻하는 약속된 기호입니다. 기준 주소의 `/data/index.html`에서 `../images/logo.png`를 가리키면 한 단계 위 폴더로 간 뒤 `images/logo.png`를 찾습니다. 반면 `/images/logo.png`처럼 맨 앞에 `/`가 있으면 웹사이트 경로의 기준점에서 시작하는 절대 경로입니다.

**기억할 한 줄:** 상대 경로는 현재 위치를 기준으로 움직이고, `/`로 시작하는 웹 경로는 사이트 기준점에서 시작합니다.


## 웹 서버는 공개한 루트 안에서 경로를 찾는다
<!-- Source: Wiki lesson-33, “웹 서버의 루트와 기본 문서”; aligned with the existing l33-web-root-path diagram. -->

웹 서버의 문서 루트(document root)는 웹에서 공개하도록 정한 시작 폴더입니다. 주소의 `/data/index.html`은 그 루트 아래의 `data` 폴더에 있는 문서를 가리킬 수 있습니다. 서버 컴퓨터의 디스크 경로 전체를 브라우저에 적는 것은 아닙니다.

주소에 경로가 없거나 `/`만 있으면 서버 설정에 따라 `index.html` 같은 기본 문서를 돌려줄 수 있습니다. 어떤 기본 문서를 쓸지는 웹 서버 설정에 달려 있습니다.

**기억할 한 줄:** 브라우저 경로는 보통 서버가 공개한 웹 루트에서 시작하고, `/` 요청의 기본 문서는 서버가 정합니다.


## URL 모양의 경로가 실제 파일과 같지는 않다
<!-- Source: Wiki lesson-33, “파일 경로와 동적 처리”. -->

웹 문서를 요청하는 브라우저 같은 프로그램을 클라이언트(client)라고 부릅니다. 클라이언트가 보내는 주소의 경로가 항상 디스크에 있는 파일 이름과 일치하는 것은 아닙니다. 예를 들어 `/products/17`은 서버가 상품 정보를 찾아 만들어 내는 동적 처리 경로일 수 있습니다. 서버는 요청을 처리해 HTML이나 JSON 응답을 만들 수 있습니다.

반대로 `/images/logo.png`처럼 저장된 이미지 파일을 그대로 보내는 경우도 있습니다. 주소만 보고 파일이 실제로 있는지 단정하지 말고, 서버가 요청을 처리한 결과를 본다고 이해하세요.

**기억할 한 줄:** URL의 경로는 요청 주소이고, 서버가 파일을 보내거나 프로그램으로 결과를 만들 수 있습니다.


## Query는 물음표 뒤에 검색 조건을 담는다
<!-- Source: Wiki lesson-33, “Query · 매개변수와 값”. -->

Query(질의)는 기준 주소의 `?search_keyword=Test`처럼 물음표 뒤에 붙는 추가 정보입니다. `search_keyword=Test`에서 `search_keyword`라는 이름은 매개변수(parameter), `Test`는 값(value)입니다. 조건을 더 붙이고 싶으면 `&`로 이어 `?search_keyword=Test&page=2`처럼 쓸 수 있습니다.

이 정보는 서버에 검색어나 페이지 번호 같은 조건을 전달할 때 쓰입니다. Query는 경로와 다른 부분입니다. `/search`는 요청 경로이고, `?keyword=dns`는 그 요청에 붙인 조건입니다.

**기억할 한 줄:** `?` 뒤는 Query이고, `이름=값` 쌍으로 서버에 조건을 전달합니다.


## Fragment는 문서 안에서 보여 줄 위치를 가리킬 수 있다
<!-- Source: The fragment explanation is supplemental clarification for the URI components introduced in Wiki lesson-33. -->

Fragment(프래그먼트)는 주소의 `#` 뒤에 적으며, 문서 안에서 보여 줄 위치를 가리킬 수 있습니다. 기준 주소의 `#result`는 문서의 `result` 위치로 이동하라는 표시입니다.

Fragment는 서버에 보낼 경로(path)나 query와 구분됩니다. 보통 브라우저가 문서를 받은 뒤 해당 문서 안에서 위치를 찾는 데 쓰며, `#` 뒤의 값이 항상 서버 파일 이름이라는 뜻은 아닙니다.

**기억할 한 줄:** `#` 뒤의 fragment는 문서 안의 위치를 가리킬 수 있습니다.
