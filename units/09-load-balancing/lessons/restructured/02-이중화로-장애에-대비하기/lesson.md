---
id: advanced-service-redundancy
title: 이중화로 장애에 대비하기
source_lesson_ids:
- u9-advanced-17-l4-부하분산과-무정지-시스템
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-17.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-17.md
---

## 장비를 이중으로 두기

<!-- learn-page-id: advanced-source-17-page-08 -->

Load Balancer도 두 대로 이중화할 수 있다. Active-Standby나 두 장비를 활성화하는 구성 등으로 한 장비가 실패해도 다른 장비가 역할을 이어받도록 한다. Virtual IP나 Virtual MAC 같은 논리적인 주소를 사용하는 방법도 있다. 여러 실제 장비가 외부에는 일관된 접속 대상으로 보이도록 만드는 관점이다.

## 무정지 시스템의 구성

<!-- learn-page-id: advanced-source-17-page-09 -->

장비와 관리 구성에도 Failover 대책이 필요하다. 그렇다고 모든 장애가 사라지는 것은 아니지만, 단일 장비 문제로 전체 서비스가 멈출 가능성을 줄인다. 서버가 물리 장비 대신 VM이라면 수리 대기 대신 이미지를 복원하거나 스냅샷으로 되돌리는 방법을 사용할 수 있다. 원본 이미지에 보안 패치를 적용하고 각 실행 환경을 교체하는 방식도 연결된다.

## 클라우드와 확장

<!-- learn-page-id: advanced-source-17-page-10 -->

이런 환경을 효율적으로 배포·관리하는 문제는 Docker와 Kubernetes, 클라우드의 자동화로 이어진다. 스위치와 서버의 역할도 가상 환경에서 제공받을 수 있다. 이 절은 운영을 서비스로 구매하는 흐름과 개발·배포 자동화를 DevOps라는 주제에 연결한다. 운영의 일부를 제공자에게 맡기고 개발자는 애플리케이션 배포와 관리에 집중하는 방향이다.

## VM·Container로 이어 보기

<!-- learn-page-id: advanced-source-17-page-11 -->

부하분산은 패킷의 연결 정보를 변환해 여러 서버로 나누는 기본 관점에서, VM과 Container를 관리하는 구조까지 이어진다. 이를 2022년의 흐름으로 설명하고 5G의 Network Function, 이후 6G에서도 가상화가 확대될 것이라는 전망을 덧붙인다. 이는 당시의 전망이며 현재 상황과 다를 수 있다.
