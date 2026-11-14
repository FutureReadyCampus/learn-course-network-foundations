---
id: advanced-stateful-firewall
title: 방화벽과 연결 상태 추적
source_lesson_ids:
- u10-advanced-23-네트워크-보안-솔루션-종류
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-23.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-23.md
---

## Packet Filtering과 방화벽

<!-- learn-page-id: advanced-source-23-page-10 -->

Packet Filtering Firewall은 IP 주소와 포트 번호 등을 보고 허용과 차단을 결정하는 Inline 장치다. NAT가 다루는 정보 범위와도 연결해 생각할 수 있다. 상위 애플리케이션에서 Proxy로 구현하는 방화벽도 있으며 두 방식을 결합하면 Hybrid라는 표현을 사용한다. Stateful Inspection은 TCP 연결의 상태 변화를 추적해 판단하는 것과 연결된다. 연결 전·중·후의 전이를 보고 비정상적인 상황을 인지하려면 세션을 추적할 수 있어야 한다.

## 세션 관리와 Hybrid 방화벽

<!-- learn-page-id: advanced-source-23-page-11 -->

동시에 관리할 수 있는 세션 수는 이런 장비의 성능을 설명하는 기준 중 하나다. WAF처럼 소켓 Stream의 HTTP를 보는 장치와 패킷 헤더를 보는 장치는 관찰 수준이 다르다. G-to-G VPN은 Inline Gateway 형태의 보안 기능과 연결된다. 패킷 필터링, NAT, 라우팅, VPN, 웹 방화벽 등을 한 장비에 결합할 수도 있다.

## VPN·SSL VPN

<!-- learn-page-id: advanced-source-23-page-12 -->

여러 위협 대응 기능을 통합한 장비를 UTM(Unified Threat Management)이라고 부른다. 한 대로 여러 기능을 제공하는 편의가 있지만, 고성능 개별 장비와 비교한 처리 성능도 고려해야 한다. 이 절은 중소 규모 환경의 통합 구성 예로 소개한다. SSL VPN은 애플리케이션 수준의 VPN이라는 관점으로 설명한다. 특정 웹 서비스를 Proxy 방식으로 제공하는 예를 들며 앞서 본 IPsec 기반 Gateway 구성과 비교한다.

## 기본 필터링에서 능동적 탐지로

<!-- learn-page-id: advanced-source-23-page-13 -->

Screening Router는 ACL(Access Control List) 규칙으로 간단한 허용·차단을 할 수 있다. 패킷 필터링 방화벽의 일부 기능과 비슷한 관점이다. 이 절은 이런 정책 기반 체계를 철조망 같은 보안 인프라에 비유한다. 무엇을 허용하고 막을지 정하는 Policy가 중요한 단계다.
