---
id: "u8-advanced-13-restricted-cone-방식"
title: "Restricted Cone 방식"
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-13.md
wiki_diagram: units/08-router-and-nat/lessons/04-restricted-cone-방식/assets/diagrams/lesson-13.svg
---

핵심 개념을 주제별로 정리했다.

## Full Cone에 제한을 더하기

Full Cone이 외부 유입을 폭넓게 허용한다면 Restricted Cone은 여기에 제한을 더한다. 제한 기준은 IP 주소나 포트가 될 수 있다. 별도로 Port를 명시하지 않은 Restricted Cone은 여기서 원격 IP 주소를 제한하는 방식으로 설명한다.

## 외부 포트를 열었을 때의 문제

내부 192.168.0.10:3000을 공유기의 3.3.3.3:8080에 매핑했다고 하자. Full Cone에서는 원격지가 누구인지와 관계없이 이 외부 포트로 들어오는 패킷을 전달할 수 있었다. 그러나 전혀 통신한 적 없는 호스트도 주소와 포트를 알면 접근할 수 있으므로, 원격지 정보에도 조건을 두려는 것이다.

## Remote IP 주소를 확인

Restricted Cone은 외부 포트뿐 아니라 이전에 통신한 원격지 IP 주소도 확인한다. 예를 들어 기록에 15.15.15.15가 있는데 9.9.9.9에서 패킷이 오면 해당 원격지와의 기록이 없으므로 허용하지 않는다. Full Cone과 달리 응답이나 접속을 보낸 호스트가 누구인지 제한하는 방식이다.

## 기록이 없는 Host는 차단

조건에 맞는 매핑을 찾을 수 없으면 내부 주소로 변환하지 못하고 패킷을 Drop한다. 다만 원격지의 포트 번호까지 일치해야 하는 것은 아니다.

## 같은 Host의 다른 Port

한 번 통신한 15.15.15.15라면 출발지 포트가 달라도 유입을 허용하는 예다. 내부 3000번이 상대 5555번과 통신한 기록이 있어도, 같은 상대 IP에서 다른 포트로 보내는 통신을 허용할 수 있다. 이처럼 상대 호스트는 확인하되 그 호스트의 포트는 제한하지 않는다. 관계없는 외부 호스트가 외부 매핑 정보만 알고 접근하는 경우는 막을 수 있다.

## Restricted Cone 정리

Restricted Cone은 Full Cone에 원격 IP 조건을 더한 방식이다. 외부 주소와 포트만 확인하는 것보다 접근 범위가 좁아진다. Symmetric처럼 세션별 정보를 더 세밀하게 구별하는 방식과는 별도로, 원격지 제한의 기준을 이해하는 것이 중요하다.
