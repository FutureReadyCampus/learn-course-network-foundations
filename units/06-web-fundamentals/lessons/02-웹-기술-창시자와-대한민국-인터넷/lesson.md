---
id: u6-l32-웹-기술-창시자와-대한민국-인터넷
title: 웹과 인터넷은 어떻게 시작되었을까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-32.md
wiki_diagram: units/06-web-fundamentals/lessons/02-웹-기술-창시자와-대한민국-인터넷/assets/diagrams/lesson-32.svg
page_metadata:
- terms:
  - 웹
  - 인터넷
  questions:
  - id: u9-l02-p01-q01
    kind: choice
    difficulty: easy
    prompt: 링크를 따라 여러 문서를 읽는 서비스는 무엇인가요?
    choices:
    - id: a
      text: 웹
      feedback: 맞아요. 웹은 문서를 읽고 링크로 다른 문서를 찾아가는 서비스입니다.
    - id: b
      text: 인터넷 자체
      feedback: 인터넷은 여러 서비스를 이용하도록 연결을 제공하는 기반입니다.
    - id: c
      text: 이메일
      feedback: 이메일도 인터넷을 이용하지만 여기서는 문서와 링크를 이용하는 웹을 설명합니다.
    - id: d
      text: 온라인 게임
      feedback: 온라인 게임도 인터넷을 이용하지만 문서와 링크를 읽는 서비스와는 다릅니다.
    - id: e
      text: 네트워크 연결 기반 전체
      feedback: 문서 서비스인 웹과 이를 포함한 여러 서비스의 연결 기반을 구분하세요.
    answer: a
  - id: u9-l02-p01-q02
    kind: choice
    difficulty: medium
    prompt: 친구가 “인터넷은 웹을 볼 때만 쓰는 것”이라고 말했습니다. 알맞은 설명은 무엇인가요?
    choices:
    - id: a
      text: 웹과 인터넷은 정확히 같은 뜻이다
      feedback: 웹은 인터넷을 이용하는 여러 서비스 중 하나입니다.
    - id: b
      text: 웹이 이메일을 포함한 모든 서비스를 뜻한다
      feedback: 웹은 문서와 링크를 이용하는 서비스이며 이메일과 구분됩니다.
    - id: c
      text: 웹 외에 이메일과 온라인 게임도 인터넷을 이용한다
      feedback: 맞아요. 인터넷이라는 기반 위에서 여러 서비스가 동작합니다.
    - id: d
      text: 이메일은 인터넷과 관계없이 동작한다
      feedback: 본문은 이메일도 인터넷을 이용하는 서비스로 설명합니다.
    - id: e
      text: 온라인 게임도 모두 웹 문서를 읽는 서비스다
      feedback: 인터넷을 이용한다고 모든 서비스가 웹이 되는 것은 아닙니다.
    answer: c
  question_placements:
  - question_id: u9-l02-p01-q01
    after_paragraph: 1
  illustrations:
  - file: assets/animations/l32-daily-road-and-vehicles.svg
    title: "도로와 그 위를 달리는 차"
    alt: "도로가 먼저 강조되고, 그 위에 도서관 버스, 우편차, 놀이 버스가 차례로 나타납니다. 마지막에는 도로는 기반이고 버스는 그 위의 한 가지라고 표시됩니다."
    caption: "도로는 여러 차가 함께 쓰는 기반이고, 차마다 하는 일이 다릅니다."
    after_paragraph: 1
  - file: assets/animations/l32-web-on-internet.svg
    title: "웹은 인터넷 위의 서비스"
    alt: "인터넷 연결 기반이 먼저 강조되고, 그 위에 웹, 이메일, 온라인 게임이 차례로 나타납니다. 마지막에는 웹이 인터넷을 이용하는 여러 서비스 중 하나라고 표시됩니다."
    caption: "인터넷은 연결 기반이고, 웹은 그 위에서 문서와 링크를 주고받는 서비스입니다."
    after_paragraph: 1
  illustration_after_paragraph: [-1]
- terms:
  - CERN
  - 참고문헌
  questions: []
  illustrations:
  - file: assets/animations/l32-daily-reference-note.svg
    title: "참고한 책을 바로 찾고 싶어요"
    alt: "보고서의 참고 표시를 보고 책장 여기저기를 다니며 책 B를 찾다가, 보고서에 책 B로 바로 가는 쪽지를 붙입니다. 마지막에는 누구나 쪽지를 따라 바로 찾는다고 표시됩니다."
    caption: "책과 책을 이어 두면 찾기와 나누기가 쉬워집니다."
    after_paragraph: 0
  - file: assets/animations/l32-cern-linked-papers.svg
    title: "CERN에서 시작된 문서 연결"
    alt: "CERN 연구자가 논문 A의 참고문헌을 보고 다른 논문을 직접 찾아다니다가, 문서를 서로 연결하자는 제안으로 논문 B까지 바로 이어집니다. 마지막에는 연결된 자료를 함께 찾고 공유한다고 표시됩니다."
    caption: "연구 자료를 연결하고 공유하려는 필요가 초기 웹의 출발점이 되었습니다."
    after_paragraph: 1
- terms:
  - 하이퍼텍스트(Hypertext)
  - 링크(Link)
  animations:
  - file: l32-hypertext-link.svg
    title: 링크는 문서와 문서를 잇는 길
    alt: 문서 A 카드 안의 파란 링크 글자를 누르면 점선이 이어지며 문서 B 카드가 나타나고, 이어서 B에서 C로 이어지는 모습입니다.
    caption: 링크를 누르면 문서 A에서 문서 B로 곧장 건너갑니다.
  questions:
  - id: u9-l02-p03-q01
    kind: choice
    difficulty: easy
    prompt: 문서 A의 글을 누르자 문서 B로 이동했습니다. 누른 연결 지점은 무엇인가요?
    choices:
    - id: a
      text: 하이퍼텍스트 전체
      feedback: 하이퍼텍스트는 문서가 연결된 구조이며 누른 연결 지점은 링크입니다.
    - id: b
      text: 문서를 읽는 고정 순서
      feedback: 링크는 정해진 앞뒤 순서 외에도 다른 문서로 이동하게 합니다.
    - id: c
      text: 문서의 모든 본문
      feedback: 본문 전체가 아니라 다른 자료로 이어지는 연결 지점을 눌렀습니다.
    - id: d
      text: 링크
      feedback: 맞아요. 링크는 다른 문서나 자료로 이동하는 연결 지점입니다.
    - id: e
      text: 문서 사이의 연결이 없는 상태
      feedback: 다른 문서로 이동했으므로 문서 사이에 연결이 있습니다.
    answer: d
  - id: u9-l02-p03-q02
    kind: choice
    difficulty: medium
    prompt: A에서 B로, B에서 C로 링크를 따라 읽었습니다. 하이퍼텍스트와 링크의 관계는 무엇인가요?
    choices:
    - id: a
      text: 하이퍼텍스트는 연결 구조이고 링크는 이동할 연결 지점이다
      feedback: 맞아요. 연결된 문서의 구조와 실제로 따라가는 연결을 구분합니다.
    - id: b
      text: 하이퍼텍스트는 연결 지점이고 링크는 문서 구조 전체다
      feedback: 두 역할이 뒤바뀌었습니다. 링크가 실제 연결 지점입니다.
    - id: c
      text: 하이퍼텍스트는 순서대로만 읽고 링크도 앞뒤로만 간다
      feedback: 링크를 따라 다른 문서로 바로 이동할 수 있습니다.
    - id: d
      text: 하이퍼텍스트에는 다른 자료로 가는 연결이 없다
      feedback: 다른 문서나 자료로 이어지는 연결이 핵심입니다.
    - id: e
      text: 링크는 다른 문서로 이동하지 않고 글만 꾸민다
      feedback: 링크의 핵심 역할은 다른 자료로 이동하는 연결입니다.
    answer: a
  question_placements:
  - question_id: u9-l02-p03-q01
    after_paragraph: 1
  page_id: html-definition
  illustrations:
  - file: assets/animations/l32-daily-book-jump.svg
    title: "표시를 따라 다른 책으로"
    alt: "과학책을 앞에서 뒤로 읽다가, 책 속 표시를 따라 용어 사전으로, 다시 사전 속 표시를 따라 동물 도감으로 건너갑니다. 마지막에는 표시로 이어진 책 묶음과 표시 하나가 구분되어 표시됩니다."
    caption: "표시로 이어진 묶음 전체와 건너갈 지점 하나를 구분합니다."
    after_paragraph: 1
  - file: assets/animations/l32-hypertext-structure.svg
    title: "하이퍼텍스트와 링크"
    alt: "문서 A를 위에서 아래로 읽다가 링크를 눌러 문서 B로, 다시 B의 링크를 따라 문서 C로 이동합니다. 마지막에는 전체 연결 구조가 하이퍼텍스트, 누르는 지점이 링크라고 표시됩니다."
    caption: "하이퍼텍스트는 링크로 이어진 문서 구조이고, 링크는 다른 자료로 이동하는 연결 지점입니다."
    after_paragraph: 1
  illustration_after_paragraph: [0]
- terms:
  - HTML 문서
  - HTTP
  - TCP/IP
  animations:
  - file: l32-html-http-internet.svg
    title: 문서·배달 규칙·길, 세 겹의 웹
    alt: 맨 위 층에 HTML 문서, 가운데 층에 HTTP 포장, 아래 층에 인터넷 도로가 쌓여 있고 문서가 위에서 아래로 포장되어 도로를 달려 오른쪽 브라우저에 도착하는 장면입니다.
    caption: HTML 문서는 HTTP 규칙으로 포장되어 인터넷이라는 길을 달립니다.
  questions:
  - id: u9-l02-p04-q01
    kind: choice
    difficulty: easy
    prompt: 웹 문서의 제목·문단·링크 같은 구조를 표시하는 언어는 무엇인가요?
    choices:
    - id: a
      text: HTTP
      feedback: HTTP는 문서 구조가 아니라 요청과 응답을 주고받는 규칙입니다.
    - id: b
      text: TCP/IP
      feedback: TCP/IP는 문서 구조를 표시하는 언어가 아니라 데이터 전달을 돕습니다.
    - id: c
      text: HTML
      feedback: 맞아요. HTML은 브라우저가 보여 줄 문서의 구조를 나타냅니다.
    - id: d
      text: 인터넷
      feedback: 인터넷은 문서 구조를 적는 언어가 아니라 연결 기반입니다.
    - id: e
      text: 브라우저
      feedback: 브라우저는 문서를 보여 주는 프로그램이며 구조를 표시하는 언어는 HTML입니다.
    answer: c
  - id: u9-l02-p04-q02
    kind: choice
    difficulty: medium
    prompt: 브라우저가 웹 문서를 요청해 받는 일을 역할별로 나눈 설명은 무엇인가요?
    choices:
    - id: a
      text: HTML은 요청 규칙, HTTP는 연결 기반, 인터넷은 문서 구조다
      feedback: HTML이 문서 구조, HTTP가 요청·응답 규칙이라는 기준을 다시 보세요.
    - id: b
      text: HTML은 문서 구조, HTTP는 요청·응답 규칙, 인터넷은 연결 기반이다
      feedback: 맞아요. 문서와 주고받는 약속, 데이터가 이동할 기반이 함께 작동합니다.
    - id: c
      text: HTML은 연결 기반, HTTP는 문서 구조, 인터넷은 요청 규칙이다
      feedback: 문서 구조는 HTML이며 연결 기반은 인터넷입니다.
    - id: d
      text: HTML과 HTTP는 모두 문서 구조만 표시한다
      feedback: HTTP는 브라우저와 서버 사이의 요청·응답 규칙입니다.
    - id: e
      text: 인터넷이 문서를 구성하므로 HTML과 HTTP는 필요 없다
      feedback: 연결 기반 외에도 문서 구조와 요청·응답 규칙의 역할이 필요합니다.
    answer: b
  question_placements:
  - question_id: u9-l02-p04-q01
    after_paragraph: 1
  illustrations:
  - file: assets/animations/l32-daily-letter-promise-road.svg
    title: "편지 내용, 약속, 그리고 길"
    alt: "나는 도서관에 소개 편지를 부탁하고, 도서관은 제목·문단·다른 글 안내를 갖춘 편지를 씁니다. 답장은 길을 따라 나에게 오고, 마지막에는 내용, 주고받는 약속, 길이 따로 표시됩니다."
    caption: "편지의 내용과 주고받는 약속, 편지가 다니는 길은 각자 다른 일입니다."
    after_paragraph: 1
  - file: assets/animations/l32-html-http-roles.svg
    title: "HTML, HTTP, 인터넷의 역할"
    alt: "브라우저가 HTTP 요청 GET /index.html을 보내고, 서버에는 제목·문단·링크 구조를 표시한 HTML 문서가 있습니다. HTTP 응답이 인터넷(TCP/IP)을 따라 브라우저에 오고, 마지막에는 HTML, HTTP, 전달 기반이 따로 표시됩니다."
    caption: "HTML은 문서 구조, HTTP는 요청·응답 규칙, 인터넷은 데이터가 이동할 기반입니다."
    after_paragraph: 1
  illustration_after_paragraph: [0]
- terms:
  - 개방된 표준
  - 상호운용성
  questions:
  - id: u9-l02-p05-q01
    kind: choice
    difficulty: easy
    prompt: 서로 다른 기기와 프로그램이 웹 문서를 주고받을 수 있는 성질은 무엇인가요?
    choices:
    - id: a
      text: 특정 회사의 기기만 허용하는 성질
      feedback: 상호운용성은 회사나 기기가 달라도 함께 동작할 수 있는 성질입니다.
    - id: b
      text: 서버마다 규칙을 숨겨야 하는 성질
      feedback: 공개된 공통 규칙이 서로 이해하는 데 도움을 줍니다.
    - id: c
      text: 브라우저마다 문서를 교환하지 못하는 성질
      feedback: 문서를 주고받을 수 있다는 점이 상호운용성의 핵심입니다.
    - id: d
      text: 모든 기기를 한 제품으로 바꾸는 성질
      feedback: 같은 제품으로 통일하지 않아도 공통 표준으로 함께 동작할 수 있습니다.
    - id: e
      text: 상호운용성
      feedback: 맞아요. 공통 표준을 따르면 서로 다른 프로그램도 함께 동작할 수 있습니다.
    answer: e
  - id: u9-l02-p05-q02
    kind: choice
    difficulty: medium
    prompt: 서로 다른 회사의 브라우저와 서버가 함께 웹을 쓰려면 어떤 방식이 알맞나요?
    choices:
    - id: a
      text: 각 회사만 아는 비밀 규칙만 사용한다
      feedback: 상대가 이해할 수 없는 규칙은 함께 동작하는 데 방해가 됩니다.
    - id: b
      text: 어떤 규칙도 정하지 않고 문서를 보낸다
      feedback: 개방성은 규칙이 없다는 뜻이 아니라 공개된 규칙을 함께 쓴다는 뜻입니다.
    - id: c
      text: 브라우저와 서버를 반드시 한 회사가 만든다
      feedback: 공통 표준은 회사가 달라도 함께 동작하도록 돕습니다.
    - id: d
      text: HTML·HTTP 같은 공개된 공통 표준을 따른다
      feedback: 맞아요. 공개된 규칙을 함께 이해하면 회사가 달라도 문서를 주고받을 수 있습니다.
    - id: e
      text: 회사별로 다른 규칙을 쓰고 서로 공유하지 않는다
      feedback: 서로 이해할 수 있도록 공개된 공통 규칙을 사용하는 것이 핵심입니다.
    answer: d
  question_placements:
  - question_id: u9-l02-p05-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l32-daily-common-plug.svg
    title: "누구나 맞는 공통 규격"
    alt: "A사 휴대폰의 회사 전용 플러그는 충전기에 맞지 않다가, 모두가 볼 수 있는 공통 규격이 공개됩니다. 규격을 따르자 A, B, C사 휴대폰이 모두 충전기에 연결됩니다."
    caption: "규칙이 없는 것이 아니라 모두가 아는 공개 규칙이 있어서 함께 쓸 수 있습니다."
    after_paragraph: 0
  - file: assets/animations/l32-open-standard-interop.svg
    title: "공개 표준과 상호운용성"
    alt: "A사 브라우저의 회사 전용 비밀 규칙은 웹 서버가 알아듣지 못하다가, HTML·HTTP 같은 공개 표준을 함께 쓰자 A, B, C사 브라우저가 모두 웹 서버와 연결됩니다. 마지막에는 상호운용성이 표시됩니다."
    caption: "공개된 표준을 따르면 회사가 다른 브라우저와 서버도 함께 동작합니다."
    after_paragraph: 1
- terms:
  - 튜링상
  questions: []
  illustrations:
  - file: assets/animations/l32-daily-idea-to-award.svg
    title: "아이디어에서 상까지"
    alt: "책 나눔함 아이디어, 직접 만들어 시험하기, 친구들이 함께 쓰며 고치기, 상 받기가 차례로 나타납니다. 마지막에는 상이 기여를 인정할 뿐 혼자 다 만들었다는 뜻은 아니라고 표시됩니다."
    caption: "아이디어만으로는 완성되지 않고, 만들고 고치는 과정이 이어져야 합니다."
    after_paragraph: 0
  - file: assets/animations/l32-turing-award-path.svg
    title: "웹의 발전과 튜링상"
    alt: "웹 제안, 초기 웹 구현, 여러 사람의 발전, 튜링상이 차례로 나타납니다. 마지막에는 상이 기여를 인정할 뿐 혼자 다 만들었다는 뜻은 아니라고 표시됩니다."
    caption: "튜링상은 컴퓨터 과학에 큰 공헌을 한 사람의 기여를 인정합니다."
    after_paragraph: 1
- terms:
  - 전길남
  - 인터넷 명예의 전당
  questions: []
  illustrations:
  - file: assets/animations/l32-daily-road-vs-library.svg
    title: "길을 놓은 사람, 도서관을 만든 사람"
    alt: "왼쪽에는 마을과 마을을 잇는 길, 오른쪽에는 그 길 위를 다니는 이동 도서관의 책들이 차례로 나타납니다. 마지막에는 둘 다 상을 받았지만 역할은 다르다고 표시됩니다."
    caption: "함께 상을 받아도 길 놓기와 도서관 만들기는 서로 다른 일입니다."
    after_paragraph: 1
  - file: assets/animations/l32-two-contributions.svg
    title: "전길남과 팀 버너스리"
    alt: "왼쪽에는 전길남의 서울과 구미 사이 연결 기반, 오른쪽에는 팀 버너스리의 링크로 이어진 웹 문서가 차례로 나타납니다. 마지막에는 두 사람이 인터넷 명예의 전당에 함께 언급되지만 역할은 다르다고 표시됩니다."
    caption: "인터넷 연결 기반의 구축과 웹 문서 서비스의 발전은 서로 다른 기여입니다."
    after_paragraph: 1
- terms:
  - 초기 인터넷 연결
  - 라우터
  animations:
  - file: l32-router-crossroad.svg
    title: 라우터는 교차로의 안내원
    alt: 서울대 쪽 길에서 온 상자가 가운데 라우터 교차로에 도착해, 라벨의 목적지를 읽고 구미 방향 길로 나가는 장면입니다.
    caption: 라우터는 도착지를 보고 상자를 알맞은 길로 보내 줍니다.
  questions:
  - id: u9-l02-p08-q01
    kind: choice
    difficulty: easy
    prompt: 서로 다른 네트워크 사이에서 데이터가 갈 길을 골라 전달하는 장비는 무엇인가요?
    choices:
    - id: a
      text: HTML 문서
      feedback: HTML 문서는 보여 줄 내용의 구조이며 경로를 고르는 장비가 아닙니다.
    - id: b
      text: 참고문헌
      feedback: 참고문헌은 관련 자료를 가리키며 데이터를 전달하는 장비가 아닙니다.
    - id: c
      text: 웹페이지의 링크
      feedback: 링크는 문서 사이의 이동 연결이며 네트워크 사이의 전달 장비와 다릅니다.
    - id: d
      text: 라우터
      feedback: 맞아요. 라우터는 다음 목적지로 가도록 길을 골라 데이터를 전달합니다.
    - id: e
      text: 연구 논문
      feedback: 연구 논문은 자료이며 네트워크 사이에서 길을 고르는 장비가 아닙니다.
    answer: d
  - id: u9-l02-p08-q02
    kind: choice
    difficulty: medium
    prompt: 전용 라우터 장비가 없더라도 다른 네트워크로 데이터를 전달할 수 있었던 이유는 무엇인가요?
    choices:
    - id: a
      text: DNS가 라우터 대신 패킷의 경로를 모두 결정하기 때문입니다
      feedback: DNS는 이름을 IP 주소로 찾는 데 쓰이며, 라우터의 전달 기능을 대신하지 않습니다.
    - id: b
      text: 스위치가 항상 서로 다른 네트워크 사이의 경로를 고르기 때문입니다
      feedback: 스위치는 주로 같은 네트워크 안에서 장치를 연결하며, 서로 다른 네트워크 사이의 전달은 라우팅 기능과 관련됩니다.
    - id: c
      text: 데이터가 네트워크를 지날 때 경로 선택이 필요하지 않기 때문입니다
      feedback: 다른 네트워크로 데이터를 보내려면 목적지에 맞는 경로를 선택해야 합니다.
    - id: d
      text: IP 주소가 없어도 라우터가 목적지를 자동으로 알기 때문입니다
      feedback: 라우터는 목적지 정보를 확인해 전달할 방향을 판단합니다.
    - id: e
      text: 라우터의 경로 선택과 전달 기능을 소프트웨어로 구현할 수 있기 때문입니다
      feedback: 맞아요. 라우터는 전용 장비로만 가능한 것이 아니라, 필요한 경로 선택과 전달 기능을 소프트웨어로 구현할 수도 있습니다.
    answer: e
  question_placements:
  - question_id: u9-l02-p08-q01
    after_paragraph: 1
  - question_id: u9-l02-p08-q02
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l32-daily-handmade-sign.svg
    title: "안내판을 직접 만들어 길을 이어요"
    alt: "두 마을 사이를 이으려는데 갈림길 안내판을 구하기 어려워서, 직접 만든 안내판을 세우고 짐을 마을 A에서 마을 B로 보냅니다. 마지막에는 길이 생긴 것과 모두가 버스를 타는 것은 다르다고 표시됩니다."
    caption: "필요한 장비가 없으면 직접 만들어 길을 잇기도 합니다."
    after_paragraph: 1
  - file: assets/animations/l32-1982-software-router.svg
    title: "1982년 서울대–구미 연구망"
    alt: "서울대학교와 구미 전자기술연구소를 이으려는데 라우터 장비를 구하기 어려워서, 소프트웨어로 만든 라우터가 길을 골라 데이터를 보냅니다. 마지막에는 초기 연구망과 대중 인터넷 서비스가 다르다고 표시됩니다."
    caption: "1982년 연구망은 라우터 기능을 소프트웨어로 구현한 국내 초기 네트워크 구축 사례입니다."
    after_paragraph: 1
  illustration_after_paragraph: [0]
- terms: []
  questions:
  - id: u9-l02-p09-q01
    kind: choice
    difficulty: easy
    prompt: 웹페이지 안의 링크를 누르면 어떤 과정이 다시 시작되나요?
    choices:
    - id: a
      text: 인터넷 전체를 새로 구축하는 과정
      feedback: 링크를 눌러도 연결 기반을 매번 새로 만드는 것은 아닙니다.
    - id: b
      text: HTTP를 문서 구조 언어로 바꾸는 과정
      feedback: HTTP의 역할은 계속 요청과 응답을 주고받는 규칙입니다.
    - id: c
      text: 다른 문서를 요청하는 과정
      feedback: 맞아요. 링크를 누르면 연결된 다른 문서를 요청하는 과정으로 이어집니다.
    - id: d
      text: HTML을 데이터 전달 장비로 바꾸는 과정
      feedback: HTML은 계속 문서의 구조를 나타냅니다.
    - id: e
      text: 서버의 응답 없이 모든 문서를 만드는 과정
      feedback: 본문은 브라우저가 서버에 요청하고 응답받는 흐름을 설명합니다.
    answer: c
  - id: u9-l02-p09-q02
    kind: choice
    difficulty: medium
    prompt: 웹페이지를 여는 전체 흐름을 정리한 것으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: HTML로 경로를 고르고 HTTP 내용을 보며 인터넷이 문단을 정한다
      feedback: HTML은 문서 구조이며 경로를 고르는 역할로 설명되지 않습니다.
    - id: b
      text: HTTP로 요청·응답을 주고받고 HTML 내용을 보며 인터넷 기반으로 데이터를 전달한다
      feedback: 맞아요. 요청 규칙, 문서 구조, 연결 기반이 각자의 역할을 맡아 함께 작동합니다.
    - id: c
      text: 인터넷으로 문단을 정하고 HTML이 응답 규칙을 맡는다
      feedback: 문단 구조는 HTML, 요청·응답 규칙은 HTTP의 역할입니다.
    - id: d
      text: HTTP만 있으면 데이터가 이동할 연결 기반은 필요 없다
      feedback: HTTP 규칙을 따르는 데이터도 인터넷과 TCP/IP 기반으로 오갑니다.
    - id: e
      text: HTML과 HTTP는 이름만 다를 뿐 모두 연결 기반이다
      feedback: HTML은 문서 구조, HTTP는 요청·응답 규칙이며 연결 기반과 구분됩니다.
    answer: b
  question_placements:
  - question_id: u9-l02-p09-q01
    after_paragraph: 1
  illustrations:
  - file: assets/animations/l32-daily-book-order-loop.svg
    title: "책 내용, 신청 약속, 배달 길"
    alt: "나는 신청서로 도서관에 책을 부탁하고, 도서관은 약속대로 책을 보냅니다. 책은 배달 길을 따라 오고, 책 속 다른 책 표시를 보면 다시 신청합니다."
    caption: "책 내용, 신청 약속, 배달 길은 각자 다른 역할을 맡습니다."
    after_paragraph: 0
  - file: assets/animations/l32-web-page-flow.svg
    title: "문서·규칙·연결로 나누어 보기"
    alt: "브라우저가 HTTP 요청을 보내고, 서버가 HTML 문서를 HTTP 응답으로 돌려줍니다. 데이터는 인터넷과 TCP/IP를 통해 오가고, 문서 속 링크를 누르면 다시 요청이 시작됩니다."
    caption: "HTML이 문서를 만들고, HTTP가 주고받으며, 인터넷이 연결을 제공합니다."
    after_paragraph: 1
animations_dir: units/06-web-fundamentals/lessons/02-웹-기술-창시자와-대한민국-인터넷/assets/animations
---
## 웹은 인터넷을 이용하는 문서 서비스다

친구와 함께 학교 게시판을 본다고 상상해 봅시다. 게시판에는 글과 그림이 있고, 글 안의 링크를 누르면 다른 글로 이동할 수 있습니다. 이처럼 문서를 읽고 링크로 다른 문서를 찾아가는 서비스가 웹(World Wide Web)입니다.

인터넷은 컴퓨터와 네트워크가 서로 데이터를 주고받도록 이어진 기반이고, 웹은 그 기반을 이용하는 여러 서비스 중 하나입니다. 웹과 인터넷은 자주 함께 쓰이지만 같은 뜻은 아닙니다. 인터넷으로 웹뿐 아니라 이메일, 온라인 게임 같은 다른 서비스도 이용합니다.

기억할 한 줄: **인터넷은 연결된 네트워크의 기반이고, 웹은 그 위에서 문서와 링크를 주고받는 서비스다.**

<!-- source: 외워서네트워크 lesson-32.md, 웹 기술의 출발; 혼자공부하는네트워크 05장 웹 기초 -->

## 연구 자료를 잇기 위해 CERN에서 웹을 제안했다

유럽 입자물리연구소 CERN에서는 연구자가 논문을 읽다가 참고문헌을 찾아 다른 논문으로 옮겨 가는 일이 많았습니다. 한 문서에서 다른 문서로 쉽게 이어 갈 방법이 있으면 자료를 찾고 공유하기 편해집니다.

Tim Berners-Lee(팀 버너스리)는 CERN에서 일하며 문서와 정보를 서로 연결하는 방법을 제안하고 초기 웹을 만드는 데 핵심 역할을 했습니다. 웹의 탄생은 한 사람이 혼자 모든 것을 만든 이야기라기보다, 연구 자료를 연결하려는 필요와 이를 구현하고 발전시킨 사람들의 일이 함께한 결과입니다.

기억할 한 줄: **CERN에서 연구 자료를 연결하고 공유하려는 필요가 초기 웹의 중요한 출발점이 되었다.**

<!-- source: 외워서네트워크 lesson-32.md, Tim Berners-Lee와 CERN -->

## 하이퍼텍스트는 링크로 이어진 문서다
<!-- learn-page-id: html-definition -->

종이책은 보통 앞에서 뒤로 읽지만, 온라인 문서에서는 글 안의 링크를 눌러 다른 문서로 바로 이동할 수 있습니다. 글자뿐 아니라 다른 문서나 자료로 이어지는 연결을 담은 문서를 하이퍼텍스트(Hypertext)라고 합니다.

링크는 문서 사이에 놓인 이동 경로입니다. 링크를 누르면 문서 A에서 문서 B로 이동하고, B의 링크를 따라 문서 C로 갈 수도 있습니다. 여기서 하이퍼텍스트는 연결 구조를 가리키고, 링크는 실제로 누르거나 따라가는 연결 지점이라는 차이를 기억하세요.

기억할 한 줄: **하이퍼텍스트는 문서가 링크로 이어진 구조이고, 링크는 다른 자료로 이동하는 연결이다.**

<!-- source: 외워서네트워크 lesson-32.md, Hypertext와 링크 -->

## HTML은 문서, HTTP는 주고받는 규칙이다

웹페이지는 제목과 문장, 그림처럼 브라우저가 보여 줄 내용을 담은 문서입니다. HTML은 이 문서의 제목·문단·링크 같은 구조를 표시하는 언어입니다. 브라우저가 웹페이지를 요청하면 서버가 내용을 돌려주는데, 이 요청과 응답을 어떤 모양과 순서로 주고받을지 정한 규칙이 HTTP입니다.

HTML과 HTTP는 역할이 다릅니다. HTML은 전달할 문서의 구조를 나타내고, HTTP는 브라우저와 서버가 요청과 응답을 주고받는 약속입니다. 그 아래에서는 TCP/IP와 인터넷이 데이터를 목적지까지 전달하는 일을 돕습니다. 우편으로 비유하면 HTML은 편지의 내용, HTTP는 편지를 부탁하고 돌려받는 약속, 인터넷은 편지가 이동하는 길에 가깝습니다.

기억할 한 줄: **HTML은 문서를 구성하고, HTTP는 그 문서를 요청·응답으로 주고받으며, 인터넷은 데이터가 이동할 기반이다.**

<!-- source: 외워서네트워크 lesson-32.md, HTML을 전달하는 HTTP; 혼자공부하는네트워크 05장 웹 기초 -->

## 열린 표준 덕분에 여러 브라우저가 웹을 함께 쓴다

학교 게시판을 모두가 볼 수 있으려면 특정 학생의 컴퓨터에서만 통하는 비밀 규칙이 아니라, 여러 사람이 이해할 수 있는 약속이 필요합니다. 웹도 브라우저와 서버를 만든 회사가 달라도 서로 이해할 수 있도록 HTML이나 HTTP 같은 공개된 표준을 사용합니다.

공통 표준을 따르면 서로 다른 기기와 프로그램이 웹 문서를 주고받을 수 있습니다. 이를 상호운용성이라고 합니다. 웹의 개방성은 아무 규칙도 없다는 뜻이 아니라, 함께 사용할 수 있는 공개된 규칙을 바탕으로 다양한 사람이 만들고 이용할 수 있다는 뜻입니다.

기억할 한 줄: **공개된 표준은 서로 다른 브라우저와 서버가 웹을 함께 이해하도록 돕는다.**

<!-- source: 외워서네트워크 lesson-32.md, 웹의 개방성과 활동 -->

## 튜링상은 컴퓨터 과학에 기여한 일을 인정한다

새로운 기술은 한 번의 아이디어만으로 완성되지 않습니다. 아이디어를 시험하고, 다른 사람이 사용할 수 있도록 구현하고, 오랜 시간 발전시켜야 널리 쓰이는 기술이 됩니다. 팀 버너스리는 웹을 만들고 발전시키는 데 기여한 공로로 튜링상(Turing Award)을 받았습니다.

튜링상은 컴퓨터 과학 분야에서 중요한 공헌을 한 사람에게 주는 상입니다. 상을 받았다는 사실은 기술이 한 사람의 생각만으로 생겼다는 뜻이 아니라, 그 사람의 기여가 공동체와 사회에 큰 영향을 주었다는 점을 인정받았다는 의미로 이해하면 됩니다.

기억할 한 줄: **기술의 역사를 볼 때는 발명자의 역할과 함께 구현·발전에 기여한 사람들도 살펴본다.**

<!-- source: 외워서네트워크 lesson-32.md, 튜링상과 기술의 공로 -->

## 전길남은 대한민국 인터넷 초기 연구에 기여했다

한 나라에서 인터넷을 쓰려면 컴퓨터를 연결하는 연구와 통신 기반을 마련하는 일이 필요합니다. 대한민국 인터넷 역사를 이야기할 때 전길남 박사는 초기 컴퓨터 네트워크 연구와 연결 구축에 기여한 연구자로 소개됩니다.

웹을 만든 팀 버너스리와 한국의 인터넷 연결에 기여한 전길남은 서로 다른 분야와 맥락에서 활동했습니다. 웹의 문서 서비스와 인터넷의 연결 기반을 같은 일로 섞지 않고, 각각 누가 어떤 역할을 했는지 구분해 보면 역사가 더 분명해집니다. 두 사람은 인터넷 명예의 전당에 이름을 올린 인물로도 함께 언급됩니다.

기억할 한 줄: **웹의 발전과 대한민국 인터넷 기반의 구축은 연결되어 있지만 서로 다른 기여의 역사다.**

<!-- source: 외워서네트워크 lesson-32.md, 전길남과 대한민국 인터넷 -->

## 1982년 연구망 연결은 국내 네트워크 구축의 사례다

전화선을 새로 놓고 길을 연결하듯, 컴퓨터가 서로 데이터를 주고받으려면 연결 장비와 통신 규칙이 필요합니다. 라우터는 서로 다른 네트워크 사이에서 데이터가 다음 목적지로 가도록 길을 골라 전달하는 장비입니다.

1982년 서울대학교와 구미의 전자기술연구소를 잇는 연결은 국내 초기 네트워크 구축의 한 사례입니다. 당시에는 필요한 라우터를 구하기 어려워, 네트워크에서 라우터가 하던 기능을 소프트웨어로 직접 구현해 연결했습니다. 이 연구망 연결은 오늘날 누구나 쓰는 대중 인터넷 서비스와 같은 사건은 아니지만, 국내 네트워크 기반을 넓혀 간 중요한 사례입니다.

기억할 한 줄: **초기 연구망은 인터넷 기반을 만드는 과정이고, 대중 웹 서비스의 확산은 그 뒤 이어진 별도의 과정이다.**

<!-- source: 외워서네트워크 lesson-32.md, 초기 인터넷 구축과 서비스 -->

## 웹페이지를 볼 때 문서·규칙·연결을 나누어 본다

브라우저에서 웹페이지를 열면 HTML 문서에 담긴 내용을 보게 됩니다. 브라우저는 HTTP 규칙으로 서버에 요청하고 응답을 받습니다. 그 데이터는 인터넷과 TCP/IP 기반을 통해 오갑니다. 페이지 안의 링크를 누르면 다른 문서를 요청하는 과정이 다시 시작됩니다.

웹 기술과 인터넷 기술은 함께 움직이지만 역할이 다릅니다. HTML은 웹 문서의 구조, HTTP는 문서를 요청하고 응답하는 규칙, 인터넷과 TCP/IP는 컴퓨터 사이 데이터 전달을 맡습니다. 다음 Lesson에서는 브라우저 주소에 적힌 URL과 URI가 각각 무엇을 가리키는지 살펴봅니다.

기억할 한 줄: **HTML이 문서를 만들고, HTTP가 주고받으며, 인터넷이 연결을 제공한다.**

<!-- source: 외워서네트워크 lesson-32.md, HTML·HTTP·인터넷의 관계 정리; 혼자공부하는네트워크 05장 웹 기초 -->
