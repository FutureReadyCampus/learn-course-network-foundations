---
id: advanced-nat-mapping-filtering
title: NAT의 매핑과 수신 허용 방식
source_lesson_ids:
- u8-advanced-12-full-cone-방식과-내부-네트워크-접속-문제
- u8-advanced-13-restricted-cone-방식
- u8-advanced-14-port-restricted-cone-방식
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-12.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-13.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-14.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-12.md
page_metadata:
- page_id: advanced-source-12-page-01
  illustrations:
  - file: assets/diagrams/source-12.svg
    title: Symmetric NAT의 접속 제한 · 원고 그림
    alt: Symmetric NAT의 접속 제한에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
- page_id: advanced-source-13-page-01
  illustrations:
  - file: assets/diagrams/source-13.svg
    title: Full Cone에 제한을 더하기 · 원고 그림
    alt: Full Cone에 제한을 더하기에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
- page_id: advanced-source-14-page-01
  illustrations:
  - file: assets/diagrams/source-14.svg
    title: 제한을 더하면 달라지는 것 · 원고 그림
    alt: 제한을 더하면 달라지는 것에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
---

## Symmetric NAT의 접속 제한

<!-- learn-page-id: advanced-source-12-page-01 -->

Symmetric NAT는 내부에서 시작한 통신 기록을 근거로 응답을 허용하므로, 외부에서 임의로 들어오는 패킷을 제한하는 효과가 있다. 현관의 도어록처럼 내부 접근을 제한하는 모습에 비유할 수 있다. 이 예의 NAT Table은 Outbound 통신에서 만들어진다. 기록에 맞는 서버 응답은 내부로 전달하지만, 다른 외부 호스트의 요청은 같은 방식으로 처리할 수 없다.

## 바깥에서 먼저 접속하려는 경우

<!-- learn-page-id: advanced-source-12-page-02 -->

이전에 통신하지 않은 30.30.30.30:10000이 공유기의 공인 주소 3.3.3.3:23000으로 패킷을 보냈다고 하자. 공유기가 원격지 주소·포트와 매핑 정보를 검색해도 일치하는 기록이 없다. 어느 내부 PC로 복원할 근거가 없으므로 이 예에서는 패킷을 Drop한다.

## 사설 주소로 직접 접근하기 어려운 이유

<!-- learn-page-id: advanced-source-12-page-03 -->

이전에 내부에서 접속한 웹 서버의 응답은 기록에 따라 통과하지만, 통신 기록이 없는 외부 호스트는 임의로 내부에 들어올 수 없다. 사설 주소 192.168.0.10:80을 인터넷의 목적지로 직접 사용하는 방법도 해결책이 되지 않는다. 이런 제한은 내부 보호에 유리하지만, 상대끼리 직접 데이터를 주고받는 P2P 게임에는 문제가 될 수 있다. 서버를 경유하지 않고 사용자끼리 통신하려 해도 외부에서의 진입이 막히기 때문이다.

## 게임과 P2P의 연결 문제

<!-- learn-page-id: advanced-source-12-page-04 -->

게임 클라이언트가 포트를 열었더라도 공유기가 외부 연결을 통과시켜야 P2P가 된다. NAT의 제약을 해결하려는 방법을 Hole Punching이라는 주제와 연결한다. 외부 유입을 더 허용하면 연결은 쉬워질 수 있지만, 보호 범위가 줄거나 잘못된 매핑·충돌 문제를 고려해야 한다. 이 차이를 Full Cone에서 살펴본다.

## Cone NAT로 관점 바꾸기

<!-- learn-page-id: advanced-source-12-page-05 -->

내부 192.168.0.10:3000이 원격 15.15.15.15:80에 접속하고, 공유기가 공인 주소 3.3.3.3의 외부 포트 8080에 매핑했다고 가정한다. Full Cone에서는 이 내부 호스트·포트와 외부 포트의 대응 관계를 바탕으로 이후 들어오는 통신을 처리한다.

## Host·Port와 외부 Port의 매핑

<!-- learn-page-id: advanced-source-12-page-06 -->

Full Cone은 이 매핑에서 원격지의 IP와 포트를 제한하지 않는 방식으로 설명한다. 다른 서버 B가 9.9.9.9:40000에서 3.3.3.3:8080으로 보내더라도, 공유기는 8080의 매핑을 보고 내부 192.168.0.10:3000으로 전달한다. 내부 호스트가 한 번 통신해 외부 매핑이 생기면, 그 외부 주소와 포트를 아는 다른 호스트도 접근할 수 있다는 차이다.

## 외부에서 내부로 들어오는 통신

<!-- learn-page-id: advanced-source-12-page-07 -->

P2P에서는 Rendezvous 서버가 내부 PC와 먼저 통신하면서 외부에 보이는 3.3.3.3:8080이라는 정보를 얻고, 이를 다른 PC에 알려 주는 구성을 생각할 수 있다. 다른 PC는 알려 받은 외부 주소와 포트로 접속해 내부 PC와 통신한다. 이를 Full Cone에서 P2P 연결이 쉬워지는 이유로 설명한다.

## Full Cone의 편의와 보안

<!-- learn-page-id: advanced-source-12-page-08 -->

외부에서 들어올 수 있는 범위가 넓으므로 연결 편의와 보안상 제한을 함께 고려해야 한다. 잘못된 매핑과 충돌 가능성도 언급한다. 공유기의 제조사나 모델에 따라 방식이 다를 수 있다. 이 절은 Symmetric을 제한이 중요한 기업 구성과, Full Cone을 게임 등의 연결 편의가 중요한 구성과 비교해 설명한다. 어느 한 방식이 모든 용도에서 더 낫다는 뜻은 아니다.

## 두 방식의 차이 정리

<!-- learn-page-id: advanced-source-12-page-09 -->

Cone의 핵심은 내부 IP·포트를 외부 포트에 매핑한다는 점이다. Full Cone은 매핑이 있는 공인 주소와 외부 포트로 들어오는 상대의 IP·포트를 제한하지 않는다. 이는 P2P의 연결 편의를 높이는 동시에 외부 접근을 더 넓게 허용한다는 특징이다.

## Full Cone에 제한을 더하기

<!-- learn-page-id: advanced-source-13-page-01 -->

Full Cone이 외부 유입을 폭넓게 허용한다면 Restricted Cone은 여기에 제한을 더한다. 제한 기준은 IP 주소나 포트가 될 수 있다. 별도로 Port를 명시하지 않은 Restricted Cone은 여기서 원격 IP 주소를 제한하는 방식으로 설명한다.

## 외부 포트를 열었을 때의 문제

<!-- learn-page-id: advanced-source-13-page-02 -->

내부 192.168.0.10:3000을 공유기의 3.3.3.3:8080에 매핑했다고 하자. Full Cone에서는 원격지가 누구인지와 관계없이 이 외부 포트로 들어오는 패킷을 전달할 수 있었다. 그러나 전혀 통신한 적 없는 호스트도 주소와 포트를 알면 접근할 수 있으므로, 원격지 정보에도 조건을 두려는 것이다.

## Remote IP 주소를 확인

<!-- learn-page-id: advanced-source-13-page-03 -->

Restricted Cone은 외부 포트뿐 아니라 이전에 통신한 원격지 IP 주소도 확인한다. 예를 들어 기록에 15.15.15.15가 있는데 9.9.9.9에서 패킷이 오면 해당 원격지와의 기록이 없으므로 허용하지 않는다. Full Cone과 달리 응답이나 접속을 보낸 호스트가 누구인지 제한하는 방식이다.

## 기록이 없는 Host는 차단

<!-- learn-page-id: advanced-source-13-page-04 -->

조건에 맞는 매핑을 찾을 수 없으면 내부 주소로 변환하지 못하고 패킷을 Drop한다. 다만 원격지의 포트 번호까지 일치해야 하는 것은 아니다.

## 같은 Host의 다른 Port

<!-- learn-page-id: advanced-source-13-page-05 -->

한 번 통신한 15.15.15.15라면 출발지 포트가 달라도 유입을 허용하는 예다. 내부 3000번이 상대 5555번과 통신한 기록이 있어도, 같은 상대 IP에서 다른 포트로 보내는 통신을 허용할 수 있다. 이처럼 상대 호스트는 확인하되 그 호스트의 포트는 제한하지 않는다. 관계없는 외부 호스트가 외부 매핑 정보만 알고 접근하는 경우는 막을 수 있다.

## Restricted Cone 정리

<!-- learn-page-id: advanced-source-13-page-06 -->

Restricted Cone은 Full Cone에 원격 IP 조건을 더한 방식이다. 외부 주소와 포트만 확인하는 것보다 접근 범위가 좁아진다. Symmetric처럼 세션별 정보를 더 세밀하게 구별하는 방식과는 별도로, 원격지 제한의 기준을 이해하는 것이 중요하다.

## 제한을 더하면 달라지는 것

<!-- learn-page-id: advanced-source-14-page-01 -->

Address Restricted Cone이 외부에서 들어오는 패킷의 출발지 IP를 확인한다면, Port Restricted Cone은 출발지 포트도 함께 확인한다. 이 단원의 동적 NAT 매핑은 기본적으로 Outbound에서 만들어진다. Inbound는 기록의 조건에 맞는 통신인지 보고 내부로 변환한다.

## IP와 Port를 함께 확인

<!-- learn-page-id: advanced-source-14-page-02 -->

내부 192.168.0.10:3000이 원격 15.15.15.15:5555와 통신하고 외부 포트에 매핑된 상황을 생각해 보자. Port Restricted Cone에서는 같은 외부 포트로 패킷이 들어와도 원격지 IP와 포트가 기록과 맞는지 함께 검사한다. 이후 다른 로컬 포트와 원격 포트를 사용하는 연결을 추가해 비교한다.

## 다른 Port에서 온 통신

<!-- learn-page-id: advanced-source-14-page-03 -->

설명에는 로컬 포트 3001, 상대 포트 7777, 외부 포트 8080 같은 값이 등장한다. 외부 포트를 재사용하더라도 다른 식별 정보를 함께 보면 어느 내부 통신에 해당하는지 구별하는 구성을 설명한다. 도식의 로컬 포트는 3001이다. 원격지 IP와 포트 조건을 함께 살펴 어느 내부 연결인지 구별한다.

## Port와 서비스의 관계

<!-- learn-page-id: advanced-source-14-page-04 -->

같은 호스트에서도 포트가 다르면 다른 프로세스나 서비스를 뜻할 수 있다. 따라서 상대 IP만으로 통신을 구별하는 것과 포트까지 보는 것은 차이가 있다. 이 절은 Cone 계열을 가능한 한 기존 외부 포트의 대응을 유지하려는 관점으로 설명한다. 예측 가능성과 주소 공유의 편의가 생길 수 있지만, NAT가 P2P 연결을 방해하는 문제도 함께 고려해야 한다.

## P2P를 가로막는 NAT

<!-- learn-page-id: advanced-source-14-page-05 -->

NAT의 제한을 해결해 P2P를 성립시키려는 여러 방법이 있다. Port Restricted Cone도 제한과 연결 편의 사이에서 이해할 수 있는 방식이다. IP와 포트를 함께 본다는 점만 보면 Symmetric과 비슷해 보일 수 있으므로, 외부 포트를 어떤 기준으로 새로 매핑하는지 함께 비교해야 한다.

## 연결을 성립시키려는 방법

<!-- learn-page-id: advanced-source-14-page-06 -->

이 단원의 비교에서 Symmetric은 상대와의 세션 정보가 달라지면 외부 포트도 새로 지정한다. 내부의 다른 연결에 23000번대의 별도 포트를 배정하는 식이다. Cone 쪽은 기존 대응을 가능한 한 유지하려는 관점, Symmetric은 연결 조합에 따라 외부 매핑을 더 세분화하는 관점으로 설명한다.

## Symmetric NAT와 비교

<!-- learn-page-id: advanced-source-14-page-07 -->

외부 포트를 23000, 23001, 23002처럼 이어 지정하면 다음 값을 예측할 여지가 있다. 이를 40000처럼 바꾸거나 시작점·증가분을 예측하기 어렵게 구성하는 경우도 있다. 이런 Symmetric NAT에서는 외부에서 필요한 매핑을 예측하기 어려워 P2P 통신이 더 제한될 수 있다. 외부 유입을 제한하는 특성과 직접 연결의 편의를 함께 보아야 한다.

## 실시간 통신과 중계의 비용

<!-- learn-page-id: advanced-source-14-page-08 -->

P2P는 게임에만 필요한 것이 아니다. 화상통신과 WebRTC 같은 기술에서도 직접 연결을 활용할 수 있다. 영상 트래픽이 모두 중계 서버를 지나면 서버의 전송량과 성능 부담이 커질 수 있기 때문이다. NAT가 있어도 연결할 수 있도록 하는 해결 방법들이 있으며, 다음 내용에서 관련 구성을 살펴본다.

## NAT 방식 정리

<!-- learn-page-id: advanced-source-14-page-09 -->

Full Cone, Restricted Cone, Port Restricted Cone, Symmetric의 차이는 외부 매핑을 만드는 기준과 유입을 허용하는 조건을 나누어 보면 이해하기 쉽다. 어느 IP와 포트로 나갔고, 돌아오는 패킷에서 무엇을 확인하는지 도식과 함께 따라가면 된다.
