---
id: u10-l03-web-application-architecture
title: 웹 서버·WAS·DB는 어떻게 나누어 일할까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-35.md
animations_dir: units/10-web-service-structure/lessons/03-웹-서버-was-db-구조/assets/animations
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
wiki_diagram: units/10-web-service-structure/lessons/03-웹-서버-was-db-구조/assets/diagrams/lesson-35.svg
page_metadata:
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
    title: 담당 직원이 장부에 물어봐요
    alt: 손님의 신청서가 접수 창구를 거쳐 담당 직원에게 가고, 담당 직원이 회원 장부실에 이름이 있는지 물어 있음 또는 없음을 듣고, 결과를 손님에게 돌려줍니다.
    caption: 신청서는 접수 창구와 담당 직원을 거쳐 장부 확인을 마친 뒤 결과로 돌아옵니다.
    after_paragraph: -1
  - file: assets/animations/l35-was-asks-db.svg
    title: WAS가 DB에 묻고 응답을 만들어요
    alt: 브라우저의 로그인 요청이 웹 서버를 거쳐 WAS에 넘어가고, WAS가 DB의 users 표에서 계정 정보를 조회하면 DB가 계정 정보나 없음을 돌려주며, WAS가 성공 또는 실패 응답을
      만들어 웹 서버와 네트워크를 거쳐 돌려보냅니다. DB에는 비밀번호 원문이 아닌 확인값이 보관됩니다.
    caption: 웹 서버가 요청을 접수해 WAS에 넘기면 WAS가 DB에서 필요한 계정 정보를 조회하고 응답을 만듭니다. 표의 값은 예시입니다.
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
    title: 홀, 주방, 창고의 역할
    alt: 손님의 주문을 홀이 받고, 메뉴판은 홀이 바로 주지만 요리는 주방이 창고의 재료로 만들며, 작은 가게는 한 사람이 여러 일을 맡고 큰 가게는 역할마다 담당을 나눈다고 표시됩니다.
    caption: 역할을 나누는 것과 사람 수는 별개입니다. 작은 가게는 한 사람이 여러 일을 맡을 수 있습니다.
    after_paragraph: -1
  - file: assets/animations/l35-roles-vs-machines.svg
    title: 역할 구분과 장비 수는 달라요
    alt: 웹 서버는 접수와 정적 파일, WAS는 처리와 응답 만들기, DB는 자료 저장과 조회를 맡습니다. 정적 파일은 웹 서버가 바로 보내고 처리가 필요하면 WAS와 DB가 맡으며, 작은 서비스는
      한 서버에서 여러 역할을 맡고 서비스가 커지면 여러 장비나 가상 서버로 나눌 수 있습니다.
    caption: 논리적인 역할 구분과 물리적인 장비 개수는 같은 말이 아닙니다. 모든 웹 서비스가 서로 다른 컴퓨터 세 대를 쓰는 것은 아닙니다.
    after_paragraph: 2
- terms:
  - 3-tier
  - 웹 서버(Web Server)
  - WAS(Web Application Server)
  - DB(데이터베이스)
  - APM(Application Performance Management)
  animations:
  - file: l36-three-tier-path.svg
    title: 요청 하나가 지나가는 세 단
    alt: 브라우저의 요청이 웹 서버, WAS, DB를 차례로 거치고 응답은 되돌아오는 길을 보여 줍니다.
    caption: 역할을 나누면 느려진 구간을 각각 살펴볼 수 있습니다.
  question_placements:
  - question_id: u10-l02-p01-q01
    after_paragraph: 2
  - question_id: u10-l02-p01-q02
    after_paragraph: 4
  questions:
  - id: u10-l02-p01-q01
    kind: choice
    difficulty: easy
    prompt: 로그인 요청을 처리하는 3-tier의 역할 분담으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 웹 서버가 계정 자료를 보관하고 DB가 브라우저 요청을 받습니다
      feedback: 웹 서버와 DB의 역할이 뒤바뀌었습니다. 웹 서버는 요청을 받고 DB는 자료를 보관합니다.
    - id: b
      text: WAS가 요청을 처음 받고 웹 서버가 프로그램을 실행하며 DB가 화면을 그립니다
      feedback: 각 역할이 섞였습니다. 웹 서버가 요청을 받고 WAS가 프로그램 처리를 하며 브라우저가 화면을 만듭니다.
    - id: c
      text: 웹 서버가 요청을 받고 WAS가 프로그램을 실행하며 DB가 자료를 보관합니다
      feedback: 맞아요. 세 역할은 요청 접수, 프로그램 처리, 자료 보관으로 나누어 볼 수 있습니다.
    - id: d
      text: DB가 요청을 받고 WAS가 자료를 보관하며 웹 서버가 로그인 규칙을 실행합니다
      feedback: DB는 자료를 보관하고, 로그인 규칙은 WAS가 실행할 수 있습니다. 요청은 웹 서버가 먼저 받습니다.
    - id: e
      text: 세 역할은 언제나 서로 다른 세 대의 컴퓨터에서만 실행됩니다
      feedback: 3-tier는 역할을 나눈 구성입니다. 작은 서비스에서는 여러 역할이 한 장비에서 함께 실행될 수 있습니다.
    answer: c
  - id: u10-l02-p01-q02
    kind: choice
    difficulty: medium
    prompt: 예시에서 네트워크 왕복은 0.1초, WAS 처리는 0.4초, DB 대기는 2.5초였습니다. 이 자료로 알 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: DB 응답을 기다린 시간이 가장 길지만, 이것만으로 원인을 확정할 수는 없습니다
      feedback: 맞아요. DB 대기 구간이 가장 길다는 관측은 조사 단서지만, 원인은 추가 자료로 확인해야 합니다.
    - id: b
      text: DB가 느린 것이 전체 지연의 확정된 원인입니다
      feedback: 측정된 DB 대기 시간이 길다는 사실만으로 근본 원인을 확정할 수는 없습니다.
    - id: c
      text: WAS가 0.4초 걸렸으므로 WAS가 병목입니다
      feedback: 예시에서 가장 긴 구간은 DB 응답 대기 2.5초입니다. 실제 원인은 관측 자료를 더 살펴야 합니다.
    - id: d
      text: APM이 DB 문제를 자동으로 고치고 결과를 보장합니다
      feedback: APM은 시간 분포와 호출 과정을 관찰할 단서를 줍니다. 문제를 자동으로 고치는 도구라고 설명하지 않습니다.
    - id: e
      text: 전체 시간이 3초라는 사실만으로 어느 구간이 느린지 알 수 있습니다
      feedback: 전체 시간만으로는 느린 구간을 구분할 수 없습니다. 예시처럼 구성요소별 시간을 살펴야 합니다.
    answer: a
  illustrations:
  - file: assets/animations/l36-daily-where-time-went.svg
    title: 주문이 늦으면 어디서 늦었는지 봐요
    alt: 손님 주문이 홀, 주방, 창고를 차례로 거치고, 구간마다 걸린 시간을 막대로 나눠 보면 이 예에서는 창고에서 재료를 기다린 시간이 가장 깁니다. 시간 기록표는 단서일 뿐 원인은 함께 확인해야
      한다고 표시됩니다.
    caption: 일을 나누면 늦어진 곳을 따로 볼 수 있습니다. 구간별 시간은 설명을 위한 가정입니다.
    after_paragraph: -1
  - file: assets/animations/l36-three-tier-time-split.svg
    title: 3초를 구간별로 나눠 보기
    alt: 브라우저의 요청이 웹 서버, WAS, DB를 차례로 거치고, 화면이 뜨기까지 3초 중 네트워크 왕복 0.1초, WAS 처리 0.4초, DB 응답 대기 2.5초로 나뉩니다. 이 예에서는
      DB 대기가 가장 길고, APM은 조사할 단서를 주며 원인은 로그와 함께 확인합니다.
    caption: 3초와 0.1초, 0.4초, 2.5초는 설명을 위한 가정입니다. 전체 시간이 길다는 사실만으로 어느 구성요소가 느린지 단정할 수는 없습니다.
    after_paragraph: 2
- terms:
  - 런타임(runtime)
  - JVM(Java Virtual Machine)
  - Java 바이트코드(Java bytecode)
  - 미들웨어(middleware)
  - Servlet
  - Servlet 컨테이너(Servlet container)
  - Tomcat
  question_placements:
  - question_id: u10-l02-p02-q01
    after_paragraph: 2
  - question_id: u10-l02-p02-q02
    after_paragraph: 4
  - question_id: u10-l02-p02-q03
    after_paragraph: 7
  questions:
  - id: u10-l02-p02-q01
    kind: choice
    difficulty: easy
    prompt: Java 프로그램이 실행되는 과정에 대한 설명으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: JVM이 Java 코드를 HTML과 CSS로 바꾸어 브라우저에 보냅니다
      feedback: JVM의 역할은 Java 바이트코드를 실행하는 것입니다. 화면 문서를 만들어 보내는 역할과는 다릅니다.
    - id: b
      text: Java 코드는 바이트코드로 바뀌고 JVM이 그 바이트코드를 실행합니다
      feedback: 맞아요. JVM은 Java 바이트코드를 실행하는 소프트웨어 환경입니다.
    - id: c
      text: CPU가 JVM을 실행하고 JVM은 컴퓨터의 모든 부품을 가상으로 만듭니다
      feedback: JVM은 컴퓨터 전체를 흉내 내는 것이 아니라 Java 프로그램 실행에 초점을 둡니다.
    - id: d
      text: Servlet 컨테이너가 Java 코드를 바이트코드로 바꾸고 JVM이 요청을 받습니다
      feedback: 역할이 섞였습니다. 본문에서는 코드가 바이트코드로 바뀌고 JVM이 이를 실행한다고 설명합니다.
    - id: e
      text: Tomcat이 운영체제 대신 CPU 명령을 모두 실행합니다
      feedback: Tomcat은 Servlet 컨테이너 기능을 제공하는 소프트웨어의 한 예이지 운영체제나 CPU가 아닙니다.
    answer: b
  - id: u10-l02-p02-q02
    kind: choice
    difficulty: medium
    prompt: Java 웹 환경에서 Servlet 컨테이너가 맡는 일은 무엇인가요?
    choices:
    - id: a
      text: 브라우저가 화면에 적용할 CSS 색상을 정합니다
      feedback: CSS 표현은 브라우저 화면 쪽의 일입니다. Servlet 컨테이너는 서버에서 Servlet 실행을 관리합니다.
    - id: b
      text: 데이터베이스 계정 자료를 영구 보관합니다
      feedback: 자료 보관은 DB의 역할입니다. 컨테이너는 Servlet을 시작하고 요청에 맞춰 실행하는 과정을 관리합니다.
    - id: c
      text: 도메인 이름을 서버 IP 주소로 바꿉니다
      feedback: 이름을 IP 주소로 찾는 일은 DNS가 합니다. Servlet 컨테이너는 Java 웹 요청의 실행을 관리합니다.
    - id: d
      text: Servlet을 시작하고 요청에 맞춰 실행하며 종료 과정을 관리합니다
      feedback: 맞아요. Servlet 컨테이너는 Servlet의 실행과 생명주기를 관리합니다.
    - id: e
      text: Java 바이트코드를 CPU 없이 직접 전송합니다
      feedback: 컨테이너의 설명된 역할은 Servlet 실행 관리입니다. 바이트코드 실행은 JVM이 맡습니다.
    answer: d
  - id: u10-l02-p02-q03
    kind: choice
    difficulty: medium
    prompt: WAS, JVM, Servlet 컨테이너의 관계를 본문에 맞게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 세 용어는 모두 Java 바이트코드만을 가리키는 같은 이름입니다
      feedback: 본문은 세 용어를 구분합니다. WAS는 요청 처리 환경, JVM은 Java 실행 기반, 컨테이너는 Servlet 실행 관리입니다.
    - id: b
      text: JVM은 요청을 WAS에 전달하고 WAS는 Servlet의 생명주기만 관리합니다
      feedback: 역할이 뒤섞였습니다. JVM은 바이트코드를 실행하고 Servlet 컨테이너가 Servlet 실행을 관리합니다.
    - id: c
      text: Servlet 컨테이너는 Java 프로그램을 실행하는 CPU 부품입니다
      feedback: Servlet 컨테이너는 소프트웨어 구성요소입니다. CPU는 실제 부품이며 두 개념은 다릅니다.
    - id: d
      text: WAS는 Java에서만 쓰는 이름이고 JVM은 모든 언어의 공통 실행 환경입니다
      feedback: 본문은 WAS를 서버 측 처리 환경의 넓은 역할 이름으로 소개하고, JVM을 Java 바이트코드 실행 기반으로 구분합니다.
    - id: e
      text: WAS는 요청 처리 환경, JVM은 바이트코드 실행 기반, Servlet 컨테이너는 Servlet 실행 관리자입니다
      feedback: 맞아요. 서로 관련되어 함께 구성될 수 있지만, 가리키는 역할은 다릅니다.
    answer: e
  illustrations:
  - file: assets/animations/l36-daily-theater-backstage.svg
    title: 극장의 배우와 무대 뒤 운영자
    alt: 공연장 안에서 악보는 연주자를 거쳐 소리가 되고, 무대 뒤 운영자는 배우가 언제 무대에 올라오고 장면마다 연기하고 내려오는지를 관리합니다. 공연장, 연주자, 운영자는 같은 말이 아니라고
      표시됩니다.
    caption: 배우는 맡은 장면을 연기하고, 운영자는 그 시작부터 끝까지를 관리합니다. 실제 무대는 프로그램 실행 환경을 뜻합니다.
    after_paragraph: -1
  - file: assets/animations/l36-was-jvm-container.svg
    title: WAS, JVM, Servlet 컨테이너
    alt: WAS는 요청을 처리하는 서버 쪽 환경이고, 그 안에서 Java 코드가 바이트코드가 되어 JVM에서 실행되며, Servlet 컨테이너는 Servlet의 시작, 요청마다 실행, 종료를 관리합니다.
      WAS, JVM, 컨테이너는 서로 다른 역할이라고 표시됩니다.
    caption: WAS는 요청 처리 환경, JVM은 Java 실행 기반, Servlet 컨테이너는 Java 웹 요청과 Servlet을 이어 주는 관리자입니다. 제품에 따라 한 프로그램에 함께 들어갈
      수 있습니다.
    after_paragraph: 3
---


핵심 개념을 주제별로 정리했다.

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

## 세 단으로 나누면 느린 곳을 찾기 쉽다

브라우저에서 로그인 버튼을 눌렀다고 해 보자. 요청은 먼저 웹 서버에 도착한다. 웹 서버는 요청을 받아 기본적인 파일을 전달하거나, 프로그램 실행이 필요한 요청을 WAS(Web Application Server, 웹 애플리케이션 서버)에 넘길 수 있다. WAS는 로그인 규칙을 실행하고, 계정 정보가 필요하면 데이터베이스(DB)에 조회를 요청한다. 결과는 DB에서 WAS로, 웹 서버와 네트워크를 거쳐 브라우저로 돌아온다.

이렇게 웹 서버, WAS, DB가 맡은 일을 세 단으로 나누어 보는 구성을 3-tier(3계층)라고 한다. 여기서 tier는 역할을 구분해 설명하는 층이다. 반드시 서로 다른 세 대의 컴퓨터를 뜻하지 않는다. 작은 서비스에서는 웹 서버와 WAS가 한 장비에서 함께 실행될 수 있고, 큰 서비스에서는 각 역할을 여러 장비로 나누기도 한다.

역할을 나누면 요청이 늦어진 지점을 찾아보기 쉽다. 예를 들어 화면이 뜨기까지 3초가 걸리고, 그중 네트워크 왕복에 0.1초, WAS 처리에 0.4초, DB 응답 대기에 2.5초가 들었다고 해 보자. 이 예에서는 DB를 기다리는 시간이 가장 길다. 숫자는 설명을 위한 가정이며, 실제 원인은 측정 자료로 확인해야 한다. 전체 시간이 길다는 사실만으로 어느 구성요소가 느린지 단정할 수는 없다.

APM(Application Performance Management, 애플리케이션 성능 관리)은 요청 처리 시간과 WAS·DB 같은 구성요소의 상태를 관찰하는 도구 범주다. APM은 느린 요청의 시간 분포나 호출 과정을 보여 주어 조사할 단서를 준다. 다만 그래프를 보여 주는 것만으로 원인을 자동 확정하는 것은 아니다. 관측 결과를 로그와 함께 살펴 원인을 좁힌다. Scouter(스카우터)는 APM 도구의 한 예이며, 기능은 제품별 문서에서 확인할 수 있다.

식당에 빗대면 홀 직원이 손님을 맞고(웹 서버), 주방에서 음식을 만들며(WAS), 창고에서 재료를 꺼내듯(DB) 각 역할이 이어진다. 그림의 주문이 지나가는 길은 로그인 요청에도 같은 방식으로 적용된다.

한 줄로 기억하면, **웹 서버는 요청을 받고, WAS는 프로그램을 실행하고, DB는 자료를 보관한다. 역할을 나누면 느린 구간도 나누어 살펴볼 수 있다.**

## WAS 안에서 Java 웹 요청은 어떻게 실행될까?

WAS는 프로그램 처리를 실행할 수 있는 서버 측 환경이다. 모든 WAS가 같은 언어나 기술을 쓰는 것은 아니다. 여기서는 한 가지 대표 사례로 Java 기반 서버를 살펴본다. Java 기술의 이름을 다른 언어의 웹 서비스 전체에 그대로 적용하면 안 된다.

개발자가 Java로 작성한 코드는 실행 과정에서 Java 바이트코드(bytecode)로 바뀐다. JVM(Java Virtual Machine, 자바 가상 머신)은 이 바이트코드를 실행하는 소프트웨어다. CPU는 컴퓨터 안의 실제 부품이지만, JVM은 Java 프로그램이 실행될 수 있도록 마련한 소프트웨어 환경이다. 악보를 여러 연주자가 읽는 것처럼, Java 프로그램은 운영체제에 맞는 JVM을 통해 실행될 수 있다. 다만 JVM이 컴퓨터 전체를 흉내 낸다는 뜻은 아니다. Java 프로그램을 실행하는 역할에 초점을 둔 설명이다.

애플리케이션이 요청을 받거나 응답을 만드는 데 필요한 공통 기능을 대신 제공하는 중간 소프트웨어를 미들웨어(middleware)라고 한다. 미들웨어를 사용하면 각 서비스가 반복해서 만드는 일을 줄이고, 핵심 기능에 집중할 수 있다.

Java 웹 환경에서는 Servlet(서블릿)이 요청을 받아 응답을 만드는 프로그램 단위다. Servlet 컨테이너는 이 Servlet을 시작하고 요청에 맞춰 실행하며, 종료할 때 정리하는 과정을 관리한다. 이 시작부터 끝까지의 과정을 프로그램의 생명주기라고 부른다.

Tomcat(톰캣)은 Servlet 컨테이너 기능을 제공하는 소프트웨어의 한 예다. JSP는 HTML 안에 Java 기반 내용을 섞어 동적 페이지를 만드는 기술로, 서버에서 실행될 때 Servlet과 연결되는 처리 과정을 거친다.

극장에 빗대면 Servlet은 맡은 장면을 연기하는 배우이고, Servlet 컨테이너는 배우가 언제 무대에 올라와 어떤 대본을 받을지 관리하는 무대 뒤 운영자와 비슷하다. 이 비유에서 실제 무대는 프로그램 실행 환경이며, 배우가 사람처럼 생각한다는 뜻은 아니다.

따라서 WAS, JVM, Servlet 컨테이너는 같은 말이 아니다. WAS는 애플리케이션 요청을 실행하는 서버 측 환경을 가리키는 넓은 역할 이름이고, JVM은 Java 바이트코드를 실행하는 기반이며, Servlet 컨테이너는 Java 웹 요청을 Servlet에 연결해 실행한다. 사용하는 제품과 구성에 따라 이 역할들이 한 프로그램이나 한 장비에 함께 들어갈 수 있다.

한 줄로 기억하면, **WAS는 요청 처리 환경, JVM은 Java 실행 기반, Servlet 컨테이너는 Java 웹 요청과 Servlet을 이어 주는 관리자다.**
