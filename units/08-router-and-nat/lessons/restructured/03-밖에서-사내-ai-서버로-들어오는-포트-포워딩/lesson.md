---
id: u8-advanced-15-포트-포워딩
title: 포트 포워딩으로 내부 서비스 연결하기
source_lesson_ids:
- u8-advanced-15-포트-포워딩
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-15.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-15.md
page_metadata:
- page_id: advanced-source-15-page-01
  illustrations:
  - file: assets/animations/u12-fwd-auto-review.svg
    title: "자동 매핑은 안에서 시작할 때만"
    alt: "위쪽은 내 PC가 먼저 접속해 NAT Table에 자동 기록이 생기고 응답이 오는 모습, 아래쪽은 바깥에서 먼저 온 패킷이 기록이 없어 막히는 모습을 나란히 보여 줍니다."
    caption: "바깥에서 먼저 접속하려면 매핑을 직접 지정해야 합니다."
    after_paragraph: 0
- page_id: advanced-source-15-page-02
  illustrations:
  - file: assets/animations/u12-fwd-static.svg
    title: "정적 매핑을 직접 추가"
    alt: "왼쪽은 Outbound로 자동 생기는 동적 매핑, 오른쪽은 관리자가 외부 80 → 192.168.0.12:80 규칙을 직접 넣어 바깥 요청이 전달되는 정적 매핑입니다."
    caption: "직접 넣은 정적 매핑이 포트 포워딩입니다."
    after_paragraph: 0
- page_id: advanced-source-15-page-03
  illustrations:
  - file: assets/animations/u12-fwd-settings.svg
    title: "공유기의 포트 포워딩 설정"
    alt: "공유기 관리 화면에 외부 포트 80, 내부 IP 192.168.0.12, 내부 포트 80, 원격지 제한 없음 규칙이 추가되고 여러 바깥 사용자가 들어올 수 있는 모습입니다."
    caption: "포트 포워딩 규칙 한 줄로 외부 포트를 내부 서버와 잇습니다."
    after_paragraph: 0
- page_id: advanced-source-15-page-04
  illustrations:
  - file: assets/animations/u12-fwd-private-fail.svg
    title: "내부 웹 서버를 공개하는 상황"
    alt: "집 안 웹 서버 192.168.0.12:80의 주소를 친구에게 알려 줘도 바깥에서 보낸 요청이 도착하지 못하는 모습입니다."
    caption: "사설 주소만으로는 바깥에서 접속할 수 없습니다."
    after_paragraph: 0
- page_id: advanced-source-15-page-05
  illustrations:
  - file: assets/animations/u12-fwd-public-address.svg
    title: "바깥에서 접속할 주소"
    alt: "친구가 공인 주소 3.3.3.3:80으로 보낸 요청이 공유기 규칙에 따라 목적지가 192.168.0.12:80으로 바뀌어 내부 웹 서버에 도착하는 모습입니다."
    caption: "공유기는 목적지를 바꿔 내부 서버로 전달합니다."
    after_paragraph: 0
- page_id: advanced-source-15-page-06
  illustrations:
  - file: assets/animations/u12-fwd-response.svg
    title: "내부·외부 접속 결과"
    alt: "내부 웹 서버가 만든 응답이 공유기를 거쳐 친구에게 가고, 친구에게는 3.3.3.3이 답한 것처럼 보이는 모습입니다."
    caption: "응답을 만드는 주체는 내부 서버입니다."
    after_paragraph: 0
- page_id: advanced-source-15-page-07
  illustrations:
  - file: assets/animations/u12-fwd-two-homes.svg
    title: "여러 서비스와 Port를 열기"
    alt: "두 집의 공유기에 각각 30000번을 PC 1로, 40000번을 PC 2로 보내는 규칙을 넣어 P2P 통신이 이어지는 모습입니다."
    caption: "포트와 공유기마다 포워딩 규칙이 필요합니다."
    after_paragraph: 0
- page_id: advanced-source-15-page-08
  illustrations:
  - file: assets/animations/u12-fwd-manual-pain.svg
    title: "매번 설정해야 하는 불편"
    alt: "게임 방에 들어갈 때마다 메뉴 찾기, 포트 입력, 재시작을 반복해야 하는 번거로움과 이를 자동화하는 UPnP로 이어지는 흐름입니다."
    caption: "반복 설정을 자동화하는 방법으로 UPnP가 등장합니다."
    after_paragraph: 0
---

## NAT Table의 자동 매핑 복습

<!-- learn-page-id: advanced-source-15-page-01 -->

NAT는 어떤 기록을 테이블에 추가하고, 들어오는 패킷의 무엇을 비교해 변환하는지에 따라 방식이 달라진다. 앞의 기본 예는 내부 클라이언트가 외부에 접속하는 상황이다. 반대로 외부에서 내부 서버로 먼저 접속해야 한다면 별도의 대응 관계가 필요하다. 이를 위해 NAT Table에 매핑을 직접 지정할 수 있다.

## 정적 매핑을 직접 추가

<!-- learn-page-id: advanced-source-15-page-02 -->

동적 매핑이 Outbound에 의해 자동으로 만들어진다면, 관리자가 필요한 매핑을 직접 추가하는 방식이 포트 포워딩(Port Forwarding)이다. 외부의 어느 포트로 온 통신을 내부 어느 호스트의 어느 포트로 전달할지 지정한다.

## 공유기의 포트 포워딩 설정

<!-- learn-page-id: advanced-source-15-page-03 -->

ipTIME 설정 화면의 예에는 ‘포트 포워딩 설정’과 규칙(Rule)이 있다. Rule이라는 말은 방화벽에서도 같은 의미로 사용한다. 예시 규칙은 외부 80번으로 온 통신을 내부 192.168.0.12의 80번으로 전달한다. 원격지 IP·포트는 제한하지 않는 형태로 소개하며, Full Cone처럼 외부 유입을 넓게 허용하는 효과와 연결한다.

## 내부 웹 서버를 공개하는 상황

<!-- learn-page-id: advanced-source-15-page-04 -->

내부 PC에 웹 서버를 설치하고 TCP 80번을 열어 외부 친구에게 확인을 부탁하는 상황을 생각해 보자. 공유기 뒤에 있다는 사실을 모르면 내부 사설 주소를 그대로 알려 줄 수 있지만, 그 주소만으로는 외부 인터넷에서 접속할 수 없다.

## 바깥에서 접속할 주소

<!-- learn-page-id: advanced-source-15-page-05 -->

외부 사용자가 192.168.0.12로 직접 접속하는 대신 공유기의 공인 주소 3.3.3.3을 사용해야 한다. 공유기에는 외부 80번을 내부 192.168.0.12:80으로 전달하는 규칙을 넣는다. 공유기 자체에서 웹 서버가 실행되는 것은 아니다. 해당 패킷의 목적지를 내부 서버로 바꾸어 보내 주는 것이다. 여기서는 기본 HTTP 포트 80을 사용하는 예다.

## 내부·외부 접속 결과

<!-- learn-page-id: advanced-source-15-page-06 -->

내부 웹 서버의 응답도 공유기를 거쳐 외부 사용자에게 돌아간다. 외부에서는 공인 주소로 접속하지만 실제 응답을 만드는 주체는 내부 서버다. 동적 NAT와 달리 미리 정한 포워딩 규칙으로 외부 유입을 허용한다. 양쪽이 각각 NAT 뒤에 있는 P2P에서도 필요한 포트를 내부 PC로 전달하도록 구성하면 직접 통신을 위한 조건을 만들 수 있다.

## 여러 서비스와 Port를 열기

<!-- learn-page-id: advanced-source-15-page-07 -->

PC 1이 30000번을 사용하고 PC 2가 40000번을 사용한다면, 각 공유기에 해당 외부 포트를 자기 PC로 포워딩하는 규칙을 지정하는 예를 생각할 수 있다. 다만 프로그램을 사용할 때마다 공유기의 제조사별 설정을 찾아 입력하고 재시작하는 방식은 번거롭다.

## 매번 설정해야 하는 불편

<!-- learn-page-id: advanced-source-15-page-08 -->

게임의 방에 들어갈 때마다 사용자가 포트 포워딩을 직접 설정하기는 어렵다. 따라서 이 요청과 설정을 자동화하는 방법이 필요하다. 다음 여기서는 그와 연결되는 UPnP를 살펴본다.
