---
id: advanced-network-access-control
title: NAC와 네트워크 접근 통제
source_lesson_ids:
- u10-advanced-23-네트워크-보안-솔루션-종류
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-23.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-23.md
---

## NAC · 네트워크 접근통제

<!-- learn-page-id: advanced-source-23-page-06 -->

IP는 Packet과 IP 주소, L2는 Frame과 MAC 주소, 소켓 위 애플리케이션은 Stream과 연결한다. 보안 솔루션마다 패킷 헤더를 볼지, 상위 Stream을 볼지가 다르다. 이 절은 L2~L3 수준에서 IP·MAC의 대응을 관찰해 네트워크 접근을 통제하는 NAC 형태를 소개한다. 표준적인 인증 구성과의 차이는 뒤에서 다시 설명한다.

## ARP를 이용한 접근 유도

<!-- learn-page-id: advanced-source-23-page-07 -->

IP와 MAC 주소를 쌍으로 관리하고 허용되지 않은 호스트를 발견하면 접근을 막는 방식이 있다. 스위치 포트를 내려 물리적인 Link를 끊거나, ARP 관련 정보를 이용해 게이트웨이 접근을 방해하는 방식 등을 예시에서 비교한다. ARP를 이용한 방식은 네트워크 장애를 일으킬 수 있다. LAN을 특정 계층과 연결한 설명은 개념을 구분하기 위한 관점이며 엄밀한 정의와는 구별한다.

## HTTP Redirect 방식

<!-- learn-page-id: advanced-source-23-page-08 -->

Probe가 트래픽을 관찰하고 허용되지 않은 사용자의 HTTP 접속을 안내 페이지 등으로 Redirect하는 구성이 있다. 로컬 네트워크에서 빠르게 반응할 수 있다는 설명이다. 또 다른 방식은 스위치와 인증 서버가 연동해 접근을 허용하는 것이다. RADIUS 같은 인증 체계를 이용해 인증된 대상만 네트워크에 접속하게 한다. 이 절은 이를 인증 기반 NAC의 기본 형태로 설명한다.

## 무선·단말 접근통제

<!-- learn-page-id: advanced-source-23-page-09 -->

무선에서는 WIPS 같은 접근 탐지·차단 체계도 생각할 수 있다. 보안상 무선 사용을 금지한 조직에서 몰래 사용하는 무선 NIC나 정보 유출 경로를 찾아 제한하려는 목적이다. 무선 접속도 RADIUS나 TACACS 등의 인증 체계와 연결될 수 있다. 인증 후 접속을 허용하는 구성과, 허가되지 않은 무선 사용 자체를 찾아 막는 목적을 구별하면 된다. 원문에 혼재한 약어 표기는 자료와 대조해 읽을 필요가 있다.
