---
id: u7-advanced-05-out-of-path-구조와-dpi-그리고-망중립
title: 경로 밖 관찰과 DPI
source_lesson_ids:
- u7-advanced-05-out-of-path-구조와-dpi-그리고-망중립
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-05.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-05.md
page_metadata:
- page_id: advanced-source-05-page-01
  illustrations:
  - file: assets/diagrams/source-05.svg
    title: Sensor · 경로 밖에서 관찰 · 원고 그림
    alt: Sensor · 경로 밖에서 관찰에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
---

## Sensor · 경로 밖에서 관찰

<!-- learn-page-id: advanced-source-05-page-01 -->

동아리 사이트의 접속량과 이상 징후를 관찰하고 싶다고 하자. 원래 통신은 지나가게 두고 별도로 복사본을 받는다면, 무엇을 알아낼 수 있고 수집 과정에서는 무엇을 고려해야 할까?

Out of path 장치는 경로 밖에서 데이터를 관찰하는 Sensor로 설명한다. 분석 전에 패킷을 수집해야 하므로 수집 장치와 함께 구성한다. 한 방법은 L2 포트 미러링이다. 스위치의 A와 B가 통신하면 원래 C에는 그 내용이 전달되지 않지만, 특정 포트를 미러링 대상으로 설정하면 통신의 복사본을 센서에 전달할 수 있다.

## Mirroring · 패킷을 복사하기

<!-- learn-page-id: advanced-source-05-page-02 -->

Mirroring은 원본과 같은 내용을 복사한다는 의미다. 기존 배포 스위치의 기능을 사용할 수도 있지만 복사 자체가 부하를 일으키므로 성능을 고려해야 한다. 전문 수집 장치인 Tap 스위치는 복사에 집중한다. 예를 들어 경로를 통과하는 데이터를 관찰용 인터페이스 8개에 각각 복사해 줄 수 있다. 한 곳의 복사보다 더 큰 처리 성능이 필요하므로 이런 장비는 고성능이고 가격도 높아질 수 있다.

## Read only와 차단의 차이

<!-- learn-page-id: advanced-source-05-page-03 -->

Tap의 관찰용 포트는 청진기를 댈 지점에 비유할 수 있다. 8개 중 2개를 보안, 2개를 장애 대응, 2개를 연구, 나머지 2개를 예비 용도로 나누는 구성이 가능하다. Out of path의 목적은 복사한 데이터를 읽어 분석·탐지하는 것이다. PC와 Wireshark로도 이런 관찰을 할 수 있다. 다만 같은 수집 행위라도 권한과 절차에 따라 의미가 달라지며, 적법한 수집과 도감청의 문제를 구별해야 한다고 언급한다.

## 경로 밖에서 접속에 개입하기

<!-- learn-page-id: advanced-source-05-page-04 -->

이 절은 웹 사이트에 접속했는데 경고 화면으로 이동하는 사례를 들어, 경로 밖의 센서가 관찰 결과를 활용하는 방식을 설명한다. 예시 이름은 www.abc.com이며, ISP 쪽에서 트래픽을 모아 관찰하는 상황을 가정한다. Out of path 센서가 원래 패킷을 직접 막는 Inline 장치와는 다르더라도, 관찰 후 별도의 응답을 보내 연결에 영향을 주는 구성을 생각할 수 있다.

## TCP 응답을 이용한 개입

<!-- learn-page-id: advanced-source-05-page-05 -->

센서가 원래 서버보다 먼저 응답을 보내 브라우저가 경고 페이지로 이동하도록 하는 예를 소개한다. 이는 패킷을 경로 안에서 버리는 방식과 다른 개입이다. 여기서는 기술 구조를 설명하는 예로만 이해한다. HTTP는 L7이며 소켓에서는 Stream으로 다룬다. 네트워크로 나갈 때는 세그먼트와 패킷으로 나뉘므로, 센서가 이 내용을 보려면 패킷 안의 정보와 상위 데이터를 해석해야 한다.

## DPI · Payload까지 살펴보기

<!-- learn-page-id: advanced-source-05-page-06 -->

패킷에는 IP 헤더, TCP 헤더, 그리고 HTTP 등 상위 데이터가 들어갈 수 있다. 택배의 송장과 내용물에 비유하면 IP·TCP 헤더는 전달을 위한 바깥 정보이고, 그 안쪽은 Payload다. 이 이 절은 안쪽 내용을 깊이 살펴보는 DPI(Deep Packet Inspection)와 상대적으로 얕은 범위의 SPI(Shallow Packet Inspection)를 구별해 소개한다. 이 절은 이러한 검사 범위를 통신 비밀과 당시의 제도에 관한 논의로 연결한다.

## 망중립과 사생활의 문제

<!-- learn-page-id: advanced-source-05-page-07 -->

통신 내용을 읽거나 저장하는 것은 사생활과 통신 비밀의 문제에 연결된다. 이 절은 위험한 물건을 찾겠다는 이유로 택배사가 모든 상자를 열면, 개인의 은밀한 구매 내역까지 보게 된다는 비유를 든다. 유해 정보 차단과 특정 서비스에 대한 차별은 구별해야 한다. 한 포털은 허용하면서 특정 동영상 서비스는 차단하는 정책이 이용자와 사업자에게 어떤 영향을 주는지 생각해 보자. 기술 구조가 사생활과 망중립성 문제로 이어지는 지점이다.

## 놓치지 않고 수집하는 문제

<!-- learn-page-id: advanced-source-05-page-08 -->

기술적으로 센서에서 중요한 문제 중 하나는 데이터를 놓치지 않고 수집하는 것이다. 빠르게 유입되는 패킷을 모두 확보하는 일은 쉽지 않다.

## 저장과 분석의 부하

<!-- learn-page-id: advanced-source-05-page-09 -->

미러링된 회선에서는 원래 트래픽의 복사본이 센서로 들어온다. 센서는 이를 읽어 수집하고, 수집한 데이터를 바탕으로 분석한다. 일반 엔드포인트처럼 소켓의 최종 데이터만 읽는 구조와는 다르므로 수집 자체의 성능이 중요해진다.

## Inline과 Out of path 비교

<!-- learn-page-id: advanced-source-05-page-10 -->

1Gbps 인터페이스에 Line Rate로 트래픽이 꽉 차서 들어온다고 하자. 이를 저장한 뒤 다시 읽어 분석하려면 저장장치의 지속 쓰기 속도와 처리 능력이 충분해야 한다. 디스크 입출력이 수집의 병목이 될 수 있고 SSD로 개선하더라도 저장 과정 자체가 중요한 기술 문제라고 설명한다. ‘무손실 Line Rate 수집’을 지원하는 장비가 비싸지는 이유도 여기에 있다. 5% 또는 1% 정도를 놓쳐도 전체적인 경향만 보면 되는 용도와, 패킷 하나도 잃어서는 안 되는 용도는 요구되는 구현 수준이 다르다.

동아리 서비스의 트래픽을 복사해 관찰하는 구조를 확인했다. 다음에는 다른 호스트가 연결을 대신 맺어 주는 Proxy 구조로 시선을 옮긴다.
