---
id: advanced-security-placement
title: 보안 장치의 배치와 역할
source_lesson_ids:
- u10-advanced-23-네트워크-보안-솔루션-종류
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-23.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-23.md
page_metadata:
- page_id: advanced-source-23-page-01
  illustrations:
  - file: assets/diagrams/source-23.svg
    title: 보안 장치를 세 가지 구조로 보기 · 원고 그림
    alt: 보안 장치를 세 가지 구조로 보기에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
---

## 보안 장치를 세 가지 구조로 보기

<!-- learn-page-id: advanced-source-23-page-01 -->

네트워크 보안 장치도 먼저 Inline, Out of path, Proxy 중 어떤 구조인지 살펴보면 이해하기 쉽다. Inline과 Out of path는 패킷을 다루고, User mode 애플리케이션인 Proxy는 소켓 수준에서 조립된 Stream을 다룬다. 앞서 본 세 구조를 보안 솔루션에 적용해 보는 복습이다.

## PC 방화벽과 NAC

<!-- learn-page-id: advanced-source-23-page-02 -->

PC 방화벽은 개별 PC에서 작동하는 예다. NAC(Network Access Control)는 네트워크 접근을 통제하는 체계다. 이 절은 인증 기반의 표준적인 구성과, PC 방화벽·Probe 센서 등을 결합한 구성을 구별한다. 이 차이는 이후 접근통제 방법을 비교할 때 다시 살펴본다.

## 방화벽·IPS·망분리의 배치

<!-- learn-page-id: advanced-source-23-page-03 -->

패킷 필터링 방화벽과 IPS는 기본적으로 Inline, NIDS는 Out of path의 탐지 구조로 설명한다. VPN은 경로상의 게이트웨이로, SSL 가속기와 WAF는 Proxy로 구성되는 예가 있다. UTM은 여러 보안 기능을 한 장비에 결합한다. 망분리와 망연계도 등장하지만 방화벽이나 VPN과 완전히 같은 개념은 아니다. 이름보다 어디에 놓여 어떤 데이터를 처리하는지 살펴보아야 한다.

## NIDS와 Proxy 기반 보호

<!-- learn-page-id: advanced-source-23-page-04 -->

앞단 IPS에서 패킷을 통과시키거나 차단하고, SSL 처리 뒤 평문이 된 요청을 WAF가 검사하는 구성을 생각할 수 있다. Out of path의 NIDS는 경로를 직접 통과시키는 대신 복사본으로 추가 관찰을 한다. 여러 검사가 서로 다른 위치에서 서버를 보호하는 구조다.

## OSI 계층에 장치를 놓아 보기

<!-- learn-page-id: advanced-source-23-page-05 -->

OSI 그림에는 아래의 Ethernet과 IP, L4의 TCP·UDP, 상위의 SSL과 HTTP를 연결해 볼 수 있다. TCP의 데이터 단위는 Segment, L4에서 중요한 식별자는 포트 번호다. 보안 장치가 어느 계층의 정보를 보는지 파악하는 기준이 된다.
