---
id: u6-l34-굵고-짧게-살펴보는-http
title: 굵고 짧게 살펴보는 HTTP
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
- terms:
  - 헤더(header)
- terms:
  - Request / Response
  - Method(메서드)
  animations:
  - file: l34-request-response.svg
    title: 손님 같은 클라이언트, 식당 같은 서버
    alt: 왼쪽 컴퓨터가 GET 요청 쪽지를 오른쪽 서버로 보내고, 서버가 HTML 문서를 담은 응답을 돌려보내는 장면입니다.
    caption: 클라이언트가 Request를 보내면 서버가 Response로 답합니다.
- terms:
  - Wireshark
  - 경로(path)
- terms:
  - User-Agent
  - Accept 계열
  - gzip
- terms:
  - Content-Length
  - Cookie(쿠키)
  - UTF-8
- terms:
  - 응답 코드(status code)
  - 404 Not Found
- terms:
  - GET / POST
  - HEAD / PUT / DELETE
- terms: []
animations_dir: units/06-web-fundamentals/lessons/04-굵고-짧게-살펴보는-http/assets/animations
---

핵심 개념을 주제별로 정리했다.

## HTTP와 TCP Stream
<!-- learn-page-id: http-definition -->

HTTP는 HTML 문서를 주고받기 위해 만들어진 L7 애플리케이션 프로토콜이다. 여기서는 TCP 소켓의 스트림(Stream) 위에서 동작하는 HTTP를 살펴본다. IP 패킷처럼 일정한 크기의 단위만 보면 내용을 해석할 수 있는 구조와 달리, Stream에서는 어디까지가 하나의 메시지인지 규칙에 따라 해석해야 한다. 여기서 다루는 HTTP 메시지는 헤더까지 문자열로 표현되어 비교적 직접 읽기 쉽다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** HTTP는 TCP Stream 위에서 메시지 경계를 규칙에 따라 해석한다.
- **적용하기 (Apply):** 연결이 바이트 스트림이어도 Request/Response 메시지 구분이 필요한 이유를 설명한다.
- **찾아보기 (Lookup):** HTTP/1.1과 HTTP/2 전송 차이는 프로토콜 문서에서 확인한다.

## HTTP 메시지를 해석하는 규칙

HTTP의 요청과 응답 헤더는 문자열로 된 항목과 값으로 구성된다. 영어와 각 필드의 의미를 알면 전송 내용을 살펴볼 수 있다. 다만 메시지의 경계와 각 헤더의 세부 규칙은 방대하다. 여기서는 기본적인 요청·응답 구조와 대표 필드만 살펴본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** HTTP 메시지는 문법과 의미를 갖는 요청·응답 단위다.
- **적용하기 (Apply):** 임의 문자열과 유효한 HTTP 요청을 start-line/헤더(header) 기준으로 구분한다.
- **찾아보기 (Lookup):** 현재 HTTP 버전의 메시지 문법은 RFC에서 찾아본다.

## Request와 Response
<!-- learn-page-id: http-request-response -->

클라이언트가 HTML 같은 자원을 Request하면 서버가 Response로 응답한다. 요청에는 어떤 작업을 원하는지 나타내는 Method가 있다. 대표적인 예는 GET과 POST다. 이 절은 GET을 자원을 달라는 다운로드 관점, POST를 클라이언트가 서버로 내용을 보내는 업로드 관점에 비유한다. 이는 용도를 처음 이해하기 위한 설명이며, 구체적인 사용 예는 뒤에서 살펴본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Request는 클라이언트(Client)가 보내고 Response는 서버(Server)가 결과와 상태를 돌려준다.
- **적용하기 (Apply):** 하나의 페이지 요청에 여러 자원 요청이 생기는 구조를 설명한다.
- **찾아보기 (Lookup):** 브라우저 DevTools에서 요청 순서·상태를 확인한다.

## 실제 HTTP 트래픽 읽기

Wireshark의 예시에서는 GET, 요청 경로, HTTP/1.1이라는 버전이 보인다. 요청이 어느 자원을 어떤 방식으로 원하는지 나타내는 것이다. 그 아래에는 User-Agent를 비롯한 여러 요청 헤더가 이어진다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Wireshark에서 HTTP 요청과 응답의 헤더·본문을 읽을 수 있다.
- **적용하기 (Apply):** 해당 환경의 허가된 평문 테스트 트래픽만 선택해 구조를 관찰한다.
- **찾아보기 (Lookup):** 암호화된 HTTPS 복호화와 캡처 설정은 보안·Wireshark 문서를 확인한다.

## 요청 Header에 담긴 정보

User-Agent에는 예시의 Mozilla 5.0, Windows NT 6.1, WOW64, Gecko 등 클라이언트 환경과 관련된 문자열이 있다. Accept에는 HTML, XML, XHTML 등 처리할 수 있는 형식이, Accept-Language에는 언어가 표시된다. Accept-Encoding의 gzip과 deflate는 압축된 응답을 해석할 수 있다는 뜻이다. 예시에는 Google의 링크를 따라 현재 페이지로 왔음을 나타내는 정보도 있다. HTTP 헤더를 통해 요청 환경과 이동 경로에 관한 정보를 전달할 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Request Header는 호스트(Host)·Accept·쿠키(Cookie) 같은 요청 부가 정보를 담는다.
- **적용하기 (Apply):** 브라우저가 원하는 형식이나 인증 관련 정보를 보내는 위치를 찾는다.
- **찾아보기 (Lookup):** Header별 의미와 보안 영향은 HTTP 표준에서 확인한다.

## 응답 Header와 Cookie

응답의 200 OK는 처리 결과를 나타낸다. 응답 헤더에는 HTML이라는 내용 형식, UTF-8 같은 문자 집합, gzip 같은 압축 방식, 날짜와 쿠키(Cookie) 등의 정보가 올 수 있다. Content-Length는 뒤에 오는 내용의 바이트 길이를 해석하는 데 사용한다. 클라이언트는 이런 정보를 바탕으로 응답을 나누고 내용을 처리한다. 직접 구현하려면 파싱 규칙을 따라야 하지만, 보통은 이미 구현된 서버와 라이브러리를 활용한다. Cookie는 이후 구조 설명에서 다시 다룬다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Response Header는 Content-Type·Cache-Control·Set-Cookie 등을 전달할 수 있다.
- **적용하기 (Apply):** 응답의 본문 형식과 브라우저 저장 지시를 Header에서 찾는다.
- **찾아보기 (Lookup):** 쿠키 보안 속성은 MDN 및 HTTP cookie 표준을 참조한다.

## HTTP 응답 코드
<!-- learn-page-id: status-code-definition -->

HTTP 응답 코드 200은 정상 처리를 나타낸다. 404 Not Found는 요청한 자원을 찾지 못했다는 뜻이다. 예를 들어 문서가 a.jpg를 표시하려고 요청했는데 서버에 그 파일이 없으면 이미지가 표시되지 않을 수 있다. 500번대 응답은 서버 측의 오류를 나타낸다. 데이터베이스 처리나 SQL 실행 등의 내부 문제가 생긴 경우를 예로 든다. 정확한 원인은 응답 코드와 서버 내부 기록을 함께 살펴보아야 한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** HTTP 상태 코드(status code)는 요청 처리 결과를 세 자리 숫자로 나타낸다.
- **적용하기 (Apply):** 2xx·3xx·4xx·5xx 응답을 결과 범주로 구분한다.
- **찾아보기 (Lookup):** 특정 상태 코드의 의미와 사용은 IANA registry에서 확인한다.

## GET·POST 등 Method

GET은 자원을 요청할 때, POST는 파일 업로드나 로그인 정보를 서버로 전달하는 등의 상황에서 사용한다. HEAD는 본문을 받지 않고 관련 응답 정보를 확인하는 방식이다. PUT과 DELETE처럼 자원을 올리거나 지우는 작업과 연결되는 메서드도 있다. 여기서 GET과 POST를 중심으로 다루고 나머지 메서드는 별도 학습 대상으로 둔다. 서버의 자원을 변경하는 기능은 허용 범위와 접근을 고려해야 한다는 취지로 설명한다. 문자열이라는 점에서 읽기는 쉬워도 HTTP 전체를 제대로 이해하려면 각 메서드와 헤더의 규칙을 더 공부해야 한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** GET·POST 등 Method는 요청 의도와 처리 의미를 표현한다.
- **적용하기 (Apply):** 조회와 데이터 제출에 적절한 Method를 구분한다.
- **찾아보기 (Lookup):** 멱등성·캐시 가능 여부는 HTTP method 정의에서 확인한다.

## 웹 서비스 구조로 이어가기

다음 여기서는 개별 프로토콜을 넘어 웹 서비스의 전체 구조를 살펴본다. 앞서 본 HTML, HTTP, TCP/IP와 클라이언트·서버를 하나의 동작 과정으로 연결하는 단계다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** HTTP Request가 WAS·API로 이어지는 흐름은 다음 Unit의 웹 서비스 구조로 연결된다.
- **적용하기 (Apply):** 클라이언트(Client) 요청에서 웹 서버(Server)와 애플리케이션 처리 단계를 그린다.
- **찾아보기 (Lookup):** WAS와 API의 역할·경계는 Unit 10에서 다시 확인한다.
