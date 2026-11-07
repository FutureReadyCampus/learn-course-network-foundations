---
id: advanced-intrusion-and-logs
title: 침입 탐지·차단과 보안 로그 분석
source_lesson_ids:
- u10-advanced-23-네트워크-보안-솔루션-종류
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-23.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-23.md
---

## IPS와 NIDS

<!-- learn-page-id: advanced-source-23-page-14 -->

이보다 더 안쪽의 Payload와 상위 내용까지 살피는 DPI 기반 탐지로 확장할 수 있다. 대표적인 장치는 Inline의 IPS와 Out of path의 NIDS다. IPS는 탐지 후 차단할 수 있고, NIDS는 경로 밖에서 탐지를 수행한다. IP·포트·상태 외에 내용의 패턴까지 판단하므로 탐지 Rule이 중요해진다.

## DPI와 Signature 검사

<!-- learn-page-id: advanced-source-23-page-15 -->

Signature 검사는 Payload 안에 특정 패턴이 있는지 찾는 방식이다. 그러나 이것만으로 알려지지 않은 파일형 악성코드를 모두 막기는 어렵다. Sandbox는 가상 환경에서 의심 파일을 실행하고 이상 행동을 관찰하는 방식으로 소개한다. 이 절은 이를 MPS라는 악성코드 방지 체계와 연결하지만, 이것도 완벽한 해결책은 아니라고 설명한다. 이후 클라우드의 추가 분석·평판 정보와 결합하는 방향으로 이어진다.

## Reputation · 평판을 활용

<!-- learn-page-id: advanced-source-23-page-16 -->

Reputation 시스템은 파일이나 대상이 알려진 악성 항목인지, 신뢰할 만한지에 관한 평판 정보를 참조한다. 장비 자체 분석과 외부 정보를 함께 활용할 수 있다. 다양한 탐지 Rule이 작동하면 정탐·오탐의 판단과 함께 많은 로그가 발생한다. 여러 보안 장비의 기록과 상태를 관리하는 체계가 필요해진다.

## ESM · 로그를 모아 분석

<!-- learn-page-id: advanced-source-23-page-17 -->

ESM(Enterprise Security Management)은 여러 보안 장비의 관리와 로그·상태 관찰을 통합하는 개념으로 설명한다. 로그가 방대해지면 모아서 분석하고 사건을 따라 추적할 필요가 있다. SIEM(Security Information and Event Management)은 이런 통합 분석과 연결된다. 예시에서 앞뒤로 혼재한 약어는 여기서 각각의 역할에 맞춰 구분했다.

## NIDS 탐지 규칙 읽기

<!-- learn-page-id: advanced-source-23-page-18 -->

NIDS Rule의 예에는 Alert라는 동작, TCP라는 프로토콜, 출발지·목적지 IP와 포트 조건, 검사할 Content가 있다. 출발지를 제한하지 않고 목적지 포트 80을 보는 예라면 웹 통신을 대상으로 이해할 수 있다. Payload 안에 ‘테스트’라는 문자열이 있으면 ‘테스트어택’이라는 로그를 내는 식이다. 이 문자열이 Signature가 된다. Rule에는 식별자와 수정 버전(Revision) 등의 정보도 있다. 기본은 조건과 패턴의 조합이다. 어느 범위의 어떤 데이터를 검사해 어떤 동작을 할지 읽을 수 있어야 한다.

## 여러 보안 기능의 결합

<!-- learn-page-id: advanced-source-23-page-19 -->

네트워크에는 라우터와 일반 스위치뿐 아니라 보안 스위치와 탐지 장치도 함께 작동한다. IPS나 NIDS의 Rule을 바꾼 뒤 이전에 없던 장애나 이상 현상이 나타날 수 있다. 따라서 각 장치가 어디에 있고 무엇을 검사하는지 알아야 네트워크 문제의 원인도 살펴볼 수 있다.

## 구조별 역할 정리

<!-- learn-page-id: advanced-source-23-page-20 -->

보안 솔루션을 만났을 때 Inline·Out of path·Proxy 중 어떤 구조인지, 다루는 데이터가 Packet인지 Stream인지 먼저 구별하면 된다. 기초편과 응용편은 여러 기술의 큰 흐름을 연결해 설명하는 과정이다. 각 주제를 더 깊이 이해하려면 이후 별도의 자료와 실습으로 보충하면 좋다.
