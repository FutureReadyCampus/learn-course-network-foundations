---
id: u6-l36-was와-restful-api-그리고-jvm
title: WAS와 RESTful API 그리고 JVM
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-36.md
wiki_diagram: units/06-web-fundamentals/lessons/06-was와-restful-api-그리고-jvm/assets/diagrams/lesson-36.svg
page_metadata:
- terms:
  - Tier(티어)
  - WAS
  - DB(데이터베이스)
  animations:
  - file: l36-three-tier-path.svg
    title: 주문 한 건이 지나가는 세 단
    alt: 브라우저에서 출발한 요청 신호가 웹 서버, WAS, DB 순서로 지나가고 응답이 같은 길을 되돌아 브라우저에 도착하는 장면입니다.
    caption: 요청은 웹 서버, WAS, DB 순으로 들어가고 결과는 거꾸로 되돌아옵니다.
- terms:
  - APM
  - 응답 시간
- terms:
  - JVM
  - Java Bytecode
  - Middleware(미들웨어)
- terms:
  - 런타임(runtime)
  - 템플릿
- terms:
  - Servlet
  - Servlet Container
  - Tomcat
  - JSP
- terms:
  - 프레임워크
  - 객체(object)
  - 의존 관계
- terms:
  - 프런트엔드(front-end)
  - UI
  - GET / POST
- terms:
  - JSON
  - XML
  - React.js / Vue.js
  animations:
  - file: l36-json-to-screen.svg
    title: 자료만 보내면 화면은 기기가 만든다
    alt: 서버에서 같은 JSON 꾸러미가 휴대폰, 태블릿, PC로 전달되고 각 기기가 크기에 맞는 서로 다른 화면 배치를 그리는 장면입니다.
    caption: 같은 JSON을 받아도 휴대폰, 태블릿, PC가 각자 알맞은 화면을 그립니다.
- terms:
  - CRUD
  - 함수
- terms:
  - URI
  - 매개변수(parameter)
  - API
- terms:
  - IPS
  - SSL 가속기
  - WAF
- terms:
  - HTTPS
  - 복호화
  - SQL Injection
  animations:
  - file: l36-https-segments.svg
    title: 어디까지 잠겨서 가는가
    alt: 브라우저에서 보낸 비밀번호가 잠금 표시와 함께 SSL 장비까지 가고, 장비에서 잠금이 풀린 채 안쪽 서버로 이어지는 장면입니다.
    caption: 브라우저에서 SSL 장비까지는 암호문, 그 안쪽은 평문일 수 있습니다.
- terms:
  - Cookie(쿠키)
  - 클라이언트 검증 / 서버 검증
- terms: []
animations_dir: units/06-web-fundamentals/lessons/06-was와-restful-api-그리고-jvm/assets/animations
---

핵심 개념을 주제별로 정리했다.

## WAS와 처리 상태 관찰

웹 서비스는 웹 서버, WAS, 데이터베이스를 각각 하나의 Tier로 나누어 3-tier 구조로 구성할 수 있다. 웹 서버와 WAS를 합치면 2-tier로 설명할 수도 있다. 구성 요소가 나뉘면 각 부분이 얼마나 잘 처리하고 있는지 함께 살펴보아야 한다.

## APM · 응답 시간을 따라가기

네트워크가 빨라도 WAS의 처리가 느리거나 DB가 응답하지 않으면 전체 서비스가 느려진다. 특히 DB 질의와 응답 사이의 시간은 서비스 품질을 판단하는 중요한 값이다. WAS 상태와 DB 응답 시간을 관찰하는 시스템을 APM(Application Performance Management)이라고 한다. 이 절은 오픈소스 APM의 예로 Scouter를 소개한다. WAS를 더 이해하려면 User mode·Kernel mode·하드웨어 위에 어떤 실행 환경이 있는지도 살펴볼 필요가 있다.

## JVM · Java를 실행하는 기반

CPU라는 물리적인 기계와 소프트웨어로 구현한 가상 머신을 구별해 보자. 이 이 절은 JVM(Java Virtual Machine)을 Java를 위해 소프트웨어로 구현한 CPU에 비유한다. JVM은 Java Bytecode를 실행한다. 그 위에서 다른 프로그램이 작동하도록 돕는 소프트웨어가 Middleware다. 자기 기능만 수행하는 것보다 다른 소프트웨어가 필요한 환경과 공통 기능을 제공하는 역할로 이해할 수 있다.

## Middleware와 런타임

애플리케이션에는 TCP/IP 통신, DB 입출력, 파일 입출력 같은 공통 기능이 필요하다. 미들웨어는 이런 기능을 미리 준비해 개발자가 개별 서비스의 핵심 처리에 집중하도록 돕는다. 앞서 본 서버 측 문서 템플릿도 이러한 실행 환경과 연결된다.

## Servlet과 요청 처리

서버 측 웹 개발에는 JSP(Java Server Pages), PHP, ASP, Node.js 등 여러 방식이 있다. 여기서는 JSP를 예로 설명한다. JSP의 내용은 Servlet 형태로 변환되어 실행 환경에 들어간다. 필요한 함수 하나를 작성하면 나머지 공통 실행 부분을 환경이 맡아 주는 모습에 비유할 수 있다. Servlet을 감싸 실행과 연동을 관리하는 구성은 Servlet Container라고 부른다. 이 절은 이러한 미들웨어를 WAS와 연결해 설명하며 대표적인 예로 Tomcat을 든다.

## 장애 원인과 실행 상태 추적

Spring 같은 프레임워크의 컨테이너는 객체의 생성과 소멸, 의존 관계 등 실행에 필요한 관리를 담당한다. 요청에 따라 필요한 코드가 실행되는 구조다. 이런 환경에서 장애를 찾으려면 실제 실행 상태를 추적해야 한다. APM은 DB 응답 시간뿐 아니라 JVM의 상태도 관찰하고, 이상 현상을 그래프와 지표로 표시한다. 서버 관리자는 이를 통해 어느 처리에서 문제가 생기는지 살펴본다.

## 다양한 화면과 프런트엔드

사용자의 요청은 특정 기능을 실행하는 계기가 된다. 그러나 결과를 표시할 클라이언트 환경은 iPhone, Galaxy Fold, 태블릿, PC처럼 다양하다. 서버가 모든 환경의 UI를 직접 만들어 보내면 관리가 복잡해질 수 있다. 따라서 UI와 데이터를 더 분리하는 구성을 생각할 수 있다. 요청 방식은 GET·POST 등을 사용하되, 서버 응답에는 완성된 화면 대신 자료를 전달한다.

## JSON·XML로 데이터 전달

응답 자료는 XML이나 JSON 같은 형식으로 보낼 수 있다. 클라이언트의 JavaScript가 이를 받아 HTML을 만들고, 기기 환경에 맞는 화면을 구성한다. 이 이 절은 React.js와 Vue.js를 이러한 클라이언트 측 구성의 예로 소개한다. 서버가 완성된 문서 전체를 만들어 보내는 방식과 데이터를 보내 클라이언트에서 화면을 만드는 방식을 구별하면 된다.

## CRUD와 API

요청을 작업으로 나누면 생성(Create), 읽기(Read), 수정(Update), 삭제(Delete)라는 CRUD로 설명할 수 있다. 데이터를 올리거나 가져오거나 바꾸는 처리다. 서버는 이를 함수나 객체의 기능 단위로 구현하고, 클라이언트의 요청으로 해당 처리를 실행한다. 요청을 어떤 기능을 호출하는 행위로 이해하는 관점이다.

## 함수와 URI의 연결

URI로 서버의 처리 대상을 지정하고 매개변수를 전달하면 기능을 호출하는 인터페이스로 사용할 수 있다. API는 Application Programming Interface의 약자다. 이 절은 이를 RESTful API라는 주제와 연결해 소개한다. API로 자료를 받아 클라이언트에서 화면을 생성하는 웹 구조를 큰 틀에서 이해하기 위한 설명이다.

## 보안 장비가 놓이는 경로

서버 앞에는 보안 장비도 배치된다. 그림의 예에는 1차 방어를 맡는 IPS(침입 방지 시스템), SSL 처리를 담당하는 가속기, 웹 요청을 검사하는 WAF(웹 애플리케이션 방화벽)가 있다. WAF의 위치는 구성에 따라 달라질 수 있다. 웹 서버 앞에 둘 수도 있고, 웹 서버를 바깥에 두고 그 뒤의 처리 구간을 보호하는 형태로 설명할 수도 있다.

## HTTPS 구간과 복호화

중간 장비가 SSL 처리를 맡는 구성에서는 클라이언트부터 그 장비까지 HTTPS로 암호화하고, 복호화한 뒤 안쪽을 HTTP 평문으로 전달할 수 있다. 모든 구간이 자동으로 같은 보호를 받는 것은 아니므로 구간을 구별해야 한다. 서버로 들어오는 매개변수는 원격지 사용자 입력이므로 신뢰하지 않고 검증해야 한다. 이 절은 입력에 SQL 관련 내용이 포함되는 SQL Injection 문제를 예로 들어 보안 검사 필요성을 설명한다.

## 입력 검증은 서버에서

이름을 받는 곳에 숫자 10만 자를 보내는 등 정상 범위를 벗어난 입력도 검증 대상이다. 서버가 입력 형식과 범위를 확인해야 안정적으로 처리할 수 있다. Cookie는 Key와 Value 형태로 구성된다는 점도 함께 알아둔다. JavaScript 코드는 서버에서 내려받더라도 이 예에서는 클라이언트에서 실행된다. 따라서 특수문자를 막는 등의 클라이언트 검사는 사용자의 입력을 돕는 기능으로 볼 수 있지만, 조작을 막는 최종 보안 검증으로 신뢰해서는 안 된다. 필요한 검증은 서버에서도 수행해야 한다.

## 전체 구조와 과정 정리

웹 서비스의 큰 구조에는 브라우저, 웹 서버, WAS, DB와 그 사이의 네트워크·보안 장비가 함께 들어간다. 개별 기술과 함께 요청이 어디로 가고 어떤 처리를 거쳐 응답하는지 전체를 연결해 보면 좋다. 이로써 기초 과정의 웹 설명을 마친다. 응용 과정에서는 VPN 등 앞에서 다루지 못한 네트워크 구조를 더 살펴본다.
