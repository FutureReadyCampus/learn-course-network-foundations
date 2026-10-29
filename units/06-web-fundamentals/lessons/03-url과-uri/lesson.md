---
id: u6-l33-url과-uri
title: URL과 URI
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-33.md
wiki_diagram: units/06-web-fundamentals/lessons/03-url과-uri/assets/diagrams/lesson-33.svg
page_metadata:
- terms:
  - URL(Uniform Resource Locator)
  - URI(Uniform Resource Identifier)
- terms:
  - 자원(Resource)
  - HTML · CSS · JS
- terms:
  - JSON
  - 식별(identify)과 특정(locate)
- terms:
  - Scheme(스킴)
  - Authority · Path · Query · Fragment
  animations:
  - file: l33-uri-parts.svg
    title: 주소 한 줄은 칸이 나뉜 운송장
    alt: 한 줄로 쓰인 웹 주소가 방식, 호스트, 포트, 경로, 쿼리 다섯 조각으로 색이 나뉘며 택배 운송장의 칸으로 옮겨 가는 장면입니다.
    caption: https://www.test.co.kr:8080/data/index.html?search_keyword=Test 는 방식,
      호스트, 포트, 경로, 쿼리 칸으로 나뉩니다.
- terms:
  - 프로토콜(protocol)
  - 호스트(host)
- terms:
  - 절대 경로(absolute path)
  - 상대 경로(relative path)
- terms:
  - 웹 루트(web root)
  - 기본 문서(default document)
  animations:
  - file: l33-web-root-path.svg
    title: 주소의 / 는 서버가 열어 둔 로비
    alt: 서버 디스크의 폴더 그림에서 C 드라이브와 web 폴더 부분은 흐려지고, 웹 루트부터 data 폴더와 index.html까지 이어지는
      경로가 브라우저 주소창의 /data/index.html과 연결되는 장면입니다.
    caption: 브라우저 주소의 경로는 디스크 전체가 아니라 웹 루트에서 시작합니다.
- terms:
  - 동적 처리
  - 클라이언트(client)
- terms:
  - Query(쿼리)
  - 매개변수(Parameter)와 값(Value)
- terms:
  - 포트 번호(port number)
  - 기본 포트
animations_dir: units/06-web-fundamentals/lessons/03-url과-uri/assets/animations
---

핵심 개념을 주제별로 정리했다.

## URL과 URI의 이름

웹을 이해하려면 URL과 URI를 구별해야 한다. 앞서 www.naver.com에서 www를 호스트 이름, naver.com을 도메인 이름으로 나누어 보았다. URL과 URI의 앞부분은 Uniform Resource이며, 끝의 L은 Locator, I는 Identifier를 뜻한다. 위치를 나타내는 것과 대상을 식별하는 것의 차이를 보기 전에 Resource가 무엇인지 살펴보자.

## Resource · 문서와 파일

이 이 절은 웹의 기본 자원을 파일로 설명한다. HTML 문서뿐 아니라 CSS 스타일시트, JPG 이미지, JS 파일 등도 웹에서 전달하는 자원이 될 수 있다. MS Word 문서처럼 저장된 파일의 위치를 지정한다고 생각하면 Resource Locator라는 표현을 이해하기 쉽다.

## 자원을 식별하고 특정하기

JSON을 비롯해 자원의 형태는 다양하다. URL은 URI라는 더 큰 범주에 포함되는 개념이다. URI는 자원을 식별한다는 넓은 의미이고, URL은 그 위치를 지정하는 방식으로 이해할 수 있다. 일상적으로 www.naver.com을 URL 주소라고 부르기도 하지만, 이후 설명에서는 이름과 경로, 자원을 함께 살펴보는 것이 중요하다.

## URI의 문법

URI에는 Scheme, Authority, Path, Query, Fragment 등을 기술하는 문법이 있다. 콜론과 슬래시 등으로 각 부분을 구분한다. 웹에서는 흔히 http:// 다음에 호스트 이름과 필요할 경우 포트 번호, 경로를 적고 그 뒤에 Query나 Fragment를 붙이는 형태를 본다. 사용자 정보 등 모든 구성 요소가 항상 나타나는 것은 아니다.

## Protocol·Host·Port

처음 부분의 http, https, ftp 등은 사용할 방식 또는 프로토콜과 연결된다. 그 뒤에는 호스트와 도메인 이름이 온다. 호스트를 찾은 다음에는 나머지 경로 등을 이용해 그 안에서 요청할 자원을 구별한다.

## 절대 경로와 상대 경로

Path는 파일 경로에 비유할 수 있다. 예를 들어 C 드라이브의 Program Files 아래 data 폴더에 a.txt가 있다면, 드라이브부터 전부 적은 경로는 절대 경로다. Program Files를 기준으로 data/a.txt처럼 적으면 그 기준점에 대한 상대 경로다. 절대 위치를 적는지, 어떤 기준에 상대적인 위치를 적는지 구별하면 된다.

## 웹 서버의 루트와 기본 문서

설명용 주소 www.test.co.kr에 접속하는 상황을 생각해 보자. 경로를 생략하면 서버의 기본 문서인 index.html을 요청할 수 있다. 서버 내부에 C 드라이브와 웹 루트, data 폴더가 있더라도 브라우저 주소에 디스크의 실제 경로를 전부 적지는 않는다. 서버가 정한 웹 루트를 기준으로 상대적인 위치를 적는다. data 폴더 아래 문서를 요청하는 예는 /data/index.html이다.

## 파일 경로와 동적 처리

주소가 항상 저장된 파일을 그대로 가리키는 것은 아니다. .do 같은 경로는 서버의 처리를 요청하는 용도로 사용되기도 한다. 그 처리 결과로 HTML이나 JSON을 만들어 응답할 수 있다. 클라이언트는 미리 저장된 파일을 받든 서버가 생성한 결과를 받든, 요청한 주소에서 응답 데이터를 받는 구조로 동작한다.

## Query · 매개변수와 값

Query는 물음표 뒤에 적으며, 여러 매개변수는 &로 구분한다. 예시의 search_keyword는 매개변수 이름이고 Test는 그 값이다. 이처럼 주소에 Parameter와 Value를 실어 서버에 전달할 수 있다.

## 포트 번호와 주소 표기

포트 번호는 호스트 이름 뒤에 콜론으로 적는다. 여기서 설명하는 기본 HTTP는 TCP 80번을 사용하므로 생략할 수 있고, 8080처럼 다른 포트라면 www.blahblah.co.kr:8080과 같이 표시한다. 포트의 기본값은 사용하는 프로토콜의 문맥과 함께 이해해야 한다. 자원을 식별하는 URI, 그 위치를 나타내는 URL, 호스트 이름과 경로를 연결해 기억하면 된다.
