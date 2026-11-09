---
id: advanced-l4-load-balancing
title: L4 부하 분산과 서버 상태 확인
source_lesson_ids:
- u9-advanced-17-l4-부하분산과-무정지-시스템
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-17.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-17.md
page_metadata:
- page_id: advanced-source-17-page-01
  illustrations:
  - file: assets/diagrams/source-17.svg
    title: NAT 원리에서 부하분산으로 · 원고 그림
    alt: NAT 원리에서 부하분산으로에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
---

## NAT 원리에서 부하분산으로

<!-- learn-page-id: advanced-source-17-page-01 -->

NAT에서 주소와 포트를 변환하는 원리를 알면 L4 부하분산도 이해하기 쉽다. L4 스위치는 포트 정보를 근거로 연결을 배분하며, Load Balancing에 활용한다. 다만 NAT를 한다는 이유만으로 모든 공유기를 곧바로 L4 스위치라고 부를 수 있는지는 별개의 분류 문제다. 여기서는 작동 원리의 유사성에 집중한다.

## 하나의 서비스 주소로 접속

<!-- learn-page-id: advanced-source-17-page-02 -->

여러 클라이언트가 www.abc.com을 조회해 15.15.15.15라는 주소로 접속한다고 가정한다. 외부에서는 웹 서버처럼 보이지만 실제로는 Load Balancer의 주소일 수 있다. 이 장비는 80번으로 들어온 연결을 내부의 여러 웹 서버 중 하나로 전달한다. 포트 포워딩을 확장해 생각할 수 있다.

## 여러 웹 서버에 연결 배분

<!-- learn-page-id: advanced-source-17-page-03 -->

첫 사용자 길동은 1번 서버로, 다음 사용자 영희는 2번 서버로 배분하는 식이다. 서버 1·2·3·N은 주소가 다르더라도 같은 콘텐츠를 제공해야 한다. 사용자는 어느 서버로 전달되어도 같은 서비스를 받으며, 처리할 부하는 여러 대로 나뉜다.

## 순서와 정책으로 서버 선택

<!-- learn-page-id: advanced-source-17-page-04 -->

서버를 순서대로 돌며 선택하는 방식은 Round Robin이다. 1번부터 마지막까지 갔다가 다시 1번으로 돌아온다. 그러나 순서만으로는 서버의 장애나 처리 여유를 알 수 없다. 이를 위해 Health Check가 필요하다. 그림에서는 관리 서버가 각 웹 서버의 상태를 확인하고 Load Balancer와 정보를 주고받는다.

## L4와 NAT의 관계

<!-- learn-page-id: advanced-source-17-page-05 -->

Load Balancer는 NAT Gateway처럼 연결의 대상 정보를 바꾸어 적절한 서버로 전달한다. 어느 서버를 선택할지는 상태 정보를 바탕으로 결정할 수 있다. 관리 구성은 CPU 사용량, 메모리 사용량, 디스크 여유 공간 등 정상 운영을 판단할 지표를 관찰한다. 에이전트나 네트워크 분석 등 수집 방법은 여러 가지다. 특정 지표가 기준을 넘으면 해당 서버를 여유 있는 대상으로 보지 않을 수 있다.

## 서버의 부하를 고려하기

<!-- learn-page-id: advanced-source-17-page-06 -->

현재 3번 서버가 가장 여유롭다면 새 연결을 3번으로 보내고, 다음 시점에는 2번이 여유로워 2번을 고를 수 있다. 어떤 서버의 CPU가 계속 80%를 넘으며 문제가 의심되면 새 연결 배분에서 제외할 수 있다. 나머지 서버가 서비스를 이어가는 동안 해당 장비를 점검하고, 수리 중 새 4번 서버를 넣는 구성도 가능하다. 수리에 5일이 걸리는 경우를 예로 든다.

## Health Check와 장애 서버

<!-- learn-page-id: advanced-source-17-page-07 -->

1번 서버를 빼더라도 나머지가 계속 응답하고 새 4번을 배분 대상에 추가하면, 사용자는 전체 서비스가 멈춘 것으로 느끼지 않을 수 있다. 이를 무정지 또는 Fault-tolerant 시스템이라는 관점으로 설명한다. Health Check와 WAS 관찰 등은 장애 대상을 골라내는 데 필요하다. 그러나 웹 서버가 모두 정상이어도 Load Balancer 자체가 멈추면 전체 접속에 영향을 줄 수 있다.
