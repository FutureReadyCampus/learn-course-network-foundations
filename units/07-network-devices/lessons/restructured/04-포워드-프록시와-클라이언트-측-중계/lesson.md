---
id: advanced-forward-proxy
title: 포워드 프록시와 클라이언트 측 중계
source_lesson_ids:
- u7-advanced-06-proxy-우회
- u7-advanced-07-proxy-보호와-감시
- u7-advanced-09-pc에-설치하는-proxy
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-06.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-07.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-09.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-06.md
page_metadata:
- page_id: advanced-source-06-page-01
  illustrations:
  - file: assets/diagrams/source-06.svg
    title: Proxy를 사용하는 관점 · 원고 그림
    alt: Proxy를 사용하는 관점에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
- page_id: advanced-source-07-page-01
  illustrations:
  - file: assets/diagrams/source-07.svg
    title: 회사에서 직접 접속을 제한하기 · 원고 그림
    alt: 회사에서 직접 접속을 제한하기에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
- page_id: advanced-source-09-page-01
  illustrations:
  - file: assets/diagrams/source-09.svg
    title: 암호화된 패킷을 보는 한계 · 원고 그림
    alt: 암호화된 패킷을 보는 한계에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
---

## Proxy를 사용하는 관점

<!-- learn-page-id: advanced-source-06-page-01 -->

동아리원이 외부 웹사이트에 직접 연결하는 대신 중간 서버를 거쳐 접속한다고 생각해 보자. 어느 호스트가 누구와 연결하는지 따라가면 Proxy의 대리 역할이 보인다.

Proxy는 목적에 따라 여러 형태로 사용된다. 먼저 다른 호스트를 거쳐 접속하는 우회 목적의 Proxy 서버를 살펴본다. Proxy는 소켓 수준에서 Stream을 다룬다는 점을 기본으로 기억하면 된다.

## 직접 가는 경로와 돌아가는 경로

<!-- learn-page-id: advanced-source-06-page-02 -->

한국의 사용자가 미국의 웹 서버에 직접 TCP/IP로 접속하면 서버는 접속한 쪽의 IP 주소를 볼 수 있다. 자료에서는 한국 쪽 주소를 설명용으로 192.118.10.10이라고 가정한다. 사용자가 직접 접속하는 대신 다른 접속 주체를 중간에 두고 싶다면 Proxy 구성을 생각할 수 있다. 그림의 NAT Gateway는 이후에 따로 다룬다.

## 접속 주체를 대신하기

<!-- learn-page-id: advanced-source-06-page-03 -->

브라우저에는 Proxy 서버 설정이 있다. 여기에 중국에 있는 Proxy 서버를 지정했다고 가정하면, 브라우저가 원래 목적지에 바로 접속하는 대신 해당 서버에 요청을 전달한다. Proxy는 사용자 대신 외부 서버에 접속하는 대리자 역할을 한다.

## Proxy를 통한 우회

<!-- learn-page-id: advanced-source-06-page-04 -->

미국 서버에는 중국의 Proxy가 접속한 것으로 보일 수 있다. Proxy를 독일의 서버로 바꾸면 이번에는 독일 쪽 주소에서 접속하는 형태가 된다. 사용자는 한국에 그대로 있어도 목적지에서 보이는 직접 접속 주소가 달라지는 것이다. 접속 경로에 따른 차단이나 주소 노출 문제를 이러한 우회 방식과 연결해 설명한다.

## 우회에 따른 속도와 비용

<!-- learn-page-id: advanced-source-06-page-05 -->

Proxy를 거치면 직접 가는 것보다 경로가 길어져 속도가 떨어질 수 있다. 또한 Proxy까지의 접속이 막히면 이 경로도 사용할 수 없다. 핵심은 Proxy가 대리 접속으로 원래 목적지까지 중계한다는 것이다. Proxy를 통한 우회 가능성은 차단 방식과 네트워크 환경에 따라 달라진다. 모든 환경에서 우회가 보장되는 것은 아니다.

## 두 Socket 사이의 중계

<!-- learn-page-id: advanced-source-06-page-06 -->

독일 Proxy의 주소를 설명용으로 70.70.70.70이라고 가정하자. Proxy는 외부 사용자의 연결을 받는 서버 측 소켓과, 목적지로 접속하는 클라이언트 측 소켓을 사용한다. 한국의 클라이언트는 Proxy에 접속해 www.abc.com 같은 목적지를 요청하고, Proxy는 별도의 소켓으로 그 서버에 접속한다. 두 연결 사이에서 데이터를 중계하는 구조다.

## 우회 목적의 Proxy 정리

<!-- learn-page-id: advanced-source-06-page-07 -->

이 예에서 Proxy가 원래 사용자의 정보를 전달하거나 기록하지 않는다면 목적지 서버는 자신에게 직접 연결한 Proxy를 접속 주체로 인식한다. 다만 이는 설명이 제시한 조건이 있는 설명이다. 우회가 유일한 사용 목적은 아니다. 다른 호스트를 거쳐 접속하고 두 소켓 사이를 중계한다는 기본 구조를 다음 사례에도 적용할 수 있다.

여기서는 다른 경로로 접속하는 상황에서 두 연결 사이의 중계를 살펴봤다. 다음에는 같은 대리 구조를 동아리 내부의 접속 관리에 활용하는 경우를 살펴본다.

## 회사에서 직접 접속을 제한하기

<!-- learn-page-id: advanced-source-07-page-01 -->

동아리에서 함께 사용하는 PC의 외부 접속을 관리한다고 하자. 접속을 Proxy 한곳으로 모으면 어떤 정보를 확인하고 어떤 처리를 맡길 수 있을까?

Proxy는 우회 외에 보호와 감시에도 사용한다. 기업에서 내부 PC의 직접 인터넷 접속을 보안 장비로 막고, 내부 Proxy를 통해서만 접속하도록 구성하는 예가 있다. 사용자는 브라우저에 회사의 Proxy 주소를 설정한다. 이 경우 목적은 외부 Proxy로 돌아가는 것보다 내부 접속 경로를 통제하는 데 있다.

## Proxy를 통한 외부 접속

<!-- learn-page-id: advanced-source-07-page-02 -->

보안 정책은 PC가 외부 웹 서버로 직접 나가는 것은 차단하고, 내부 Proxy의 외부 접속은 허용한다. PC는 Proxy를 거쳐 외부 서비스를 사용한다. 우회 예에서는 Proxy가 외부에 있었지만, 여기서는 관리하는 내부 네트워크에 놓인다는 차이가 있다.

## 중간에서 내용을 볼 수 있는 이유

<!-- learn-page-id: advanced-source-07-page-03 -->

중간의 Proxy는 어느 내부 PC가 언제 어떤 외부 주소에 접속했는지 알 수 있다. 이를 접속 기록과 감시에 활용할 수 있다. 이 절은 근무 시간에 회사 PC로 증권 사이트를 이용하는 사례를 들어 내부 사용자의 접속을 관찰할 수 있다고 설명한다. 접속 기록을 업무상 어떻게 해석할지는 별개의 정책 문제다.

## 악성 파일 검사

<!-- learn-page-id: advanced-source-07-page-04 -->

외부에서 내려받는 DOC나 PDF 파일에 악성코드가 있는지 검사할 수도 있다. 파일이 Proxy를 지나므로, 내용을 확인한 뒤 문제가 없으면 내부 PC로 전달하는 식이다. 이는 내부 사용자를 보는 것과 함께 외부에서 들어오는 데이터를 감시하는 용도다.

## Virus Wall과 내부 보호

<!-- learn-page-id: advanced-source-07-page-05 -->

악성코드의 유입을 막는 구성을 Virus Wall이라고 설명한다. 이 예에서는 HTTP 접속을 Proxy로 제한해 파일 검사 지점을 만든다. IPS는 패킷 단위에서 정보를 처리하지만 Proxy는 HTTP Stream을 볼 수 있으므로, 파일 전체를 추출해 검사하는 데 유리하다. 같은 보호 목적이라도 다루는 데이터 수준이 다르다.

## 보호 기능을 함께 두기

<!-- learn-page-id: advanced-source-07-page-06 -->

Application Proxy 기능을 IPS 장비에 함께 설치하는 등 여러 기능을 결합할 수도 있다. 구조의 핵심은 PC가 다른 호스트를 거쳐 접속한다는 점이다. 그 중계 장치를 내부에 두고 관리하면 보호·감시에, 외부에 두면 다른 경로로 접속하는 데 활용할 수 있다. 목적에 따라 배치와 정책을 함께 살펴보아야 한다.

## 내부 사용자의 통신 감시

<!-- learn-page-id: advanced-source-07-page-07 -->

회사가 통신 내용을 읽는 구성은 회사 자산 보호와 개인의 사생활 사이의 문제를 함께 갖는다. 이 절은 여러 법적 쟁점이 있지만 여기서는 자세히 다루지 않는다. 여기서는 보호·감시 목적의 Proxy가 실제 기업 네트워크 구성에 등장하며, 소켓 Stream을 다루는 구조라는 점을 이해하면 된다.

이번에는 내부 사용자가 외부로 나가는 접속을 대신하는 구조를 살펴봤다. 다음에는 방향을 바꿔, 동아리 신청 사이트 앞에서 서버를 대신해 요청을 받는 Reverse Proxy를 살펴본다.

## 암호화된 패킷을 보는 한계

<!-- learn-page-id: advanced-source-09-page-01 -->

동아리 사이트의 요청과 응답을 분석하려고 운영자의 PC에 Proxy 프로그램을 설치했다고 하자. 브라우저와 분석 프로그램, 실제 서버 사이에 각각 어떤 연결이 생기는지 따라가 보자.

HTTPS는 내용을 암호화하므로, PC에 Wireshark를 설치해 자신의 웹 접속을 캡처해도 내용을 바로 읽기 어려울 수 있다. 분석하려면 복호화할 수 있는 별도 구성이 필요하다. 이때 PC 안에서 Proxy를 사용하는 방법이 있다.

## PC에 설치하는 Proxy

<!-- learn-page-id: advanced-source-09-page-02 -->

Fiddler는 로컬 Proxy 방식으로 웹 트래픽을 분석하는 도구의 예다. 이 절은 Burp Suite도 관련 도구로 언급한다. 여기서는 Chrome과 분석 프로그램을 같은 PC에서 실행하는 상황을 가정한다.

## Loopback에 Proxy 설정

<!-- learn-page-id: advanced-source-09-page-03 -->

브라우저의 Proxy를 자기 호스트인 127.0.0.1로 지정하고, 포트를 예를 들어 8080으로 설정한다. 분석 프로그램은 그 포트에서 연결을 받는 소켓을 연다. 브라우저는 외부 서버에 직접 가는 대신 로컬 분석 프로그램에 접속한다. 프로그램은 별도의 소켓으로 실제 목적지에 연결한다.

## 로컬 Proxy를 통과하는 경로

<!-- learn-page-id: advanced-source-09-page-04 -->

브라우저와 로컬 Proxy, 로컬 Proxy와 외부 서버 사이에 각각 연결이 생긴다. 양쪽 모두 HTTPS로 통신하더라도 필요한 분석 설정을 갖춘 Proxy 내부에서는 복호화한 내용을 다룰 수 있다. SSL의 세부 설정 절차는 여기서 다루지 않는다.

## Stream 수준의 해석과 분석

<!-- learn-page-id: advanced-source-09-page-05 -->

Proxy는 패킷별 조각보다 소켓 Stream 수준에서 내용을 처리하므로 분석하기 편리하다. 여러 호스트를 거치는 대신 같은 호스트 안에서 프로세스를 나누어 중계하는 방식이다. 직접 접속보다 단계가 늘지만, 학습·분석이나 보안 목적에 맞는 관찰 지점을 만들 수 있다. Fiddler 같은 도구를 이러한 구조의 예로 기억하면 된다.

## Fiddler와 Proxy 활용 정리

<!-- learn-page-id: advanced-source-09-page-06 -->

지금까지 본 Proxy의 목적은 외부 서버로 우회하기, 내부 사용자의 접속을 감시하거나 악성 파일을 차단하기, Reverse Proxy로 서버를 보호하기, 로컬에서 HTTPS 트래픽을 분석하기다. 배치와 목적은 달라도 소켓 연결 사이에서 Stream을 대리 처리한다는 기본 구조는 같다.

이제 우리 서비스 안팎에서 장치가 통신을 전달하고 관찰하고 대리하는 방식을 구별할 수 있다. 다음 Unit에서는 공유기를 지날 때 주소와 포트가 어떻게 바뀌고 연결되는지 살펴본다.
