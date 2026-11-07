---
id: advanced-remote-access-vpn
title: 원격 접속 VPN과 사용 시 주의
source_lesson_ids:
- u10-advanced-21-vpn과-재택근무
- u10-advanced-22-vpn-악용
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-21.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-22.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-21.md
page_metadata:
- page_id: advanced-source-21-page-01
  illustrations:
  - file: assets/diagrams/source-21.svg
    title: VPN과 재택근무의 상황 · 원고 그림
    alt: VPN과 재택근무의 상황에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
- page_id: advanced-source-22-page-01
  illustrations:
  - file: assets/diagrams/source-22.svg
    title: VPN이 바꾸는 접속 위치 · 원고 그림
    alt: VPN이 바꾸는 접속 위치에서 원고가 함께 제공한 개념 그림
    caption: 기존 원고의 그림을 참고해 구조와 용어를 확인한다.
    after_paragraph: -1
---

## VPN과 재택근무의 상황

<!-- learn-page-id: advanced-source-21-page-01 -->

앞의 예에서 서울 본사의 중요한 서버는 내부에서만 접근하도록 제한되어 있다. 부산 지사의 철수는 지사 간 VPN을 통해 사용할 수 있다. 이제 철수가 지사가 아니라 집에서 근무해야 하는 상황을 살펴본다.

## 외부 직원의 사내 접속

<!-- learn-page-id: advanced-source-21-page-02 -->

철수의 집 PC가 KT의 인터넷을 이용하며 9.9.9.9라는 주소를 받았다고 가정한다. 이 주소로 본사 DB에 직접 접속하면 보안 정책상 차단된다. 업무를 하려면 외부의 개인 PC가 허용된 방법으로 사내 네트워크에 참여해야 한다.

## VPN Client와 접속 설정

<!-- learn-page-id: advanced-source-21-page-03 -->

이때 G-to-E VPN을 사용할 수 있다. Endpoint인 집 PC에 VPN Client를 설치하고 회사의 Secure Gateway로 접속한다. 집 PC의 외부 주소를 그대로 사용해 터널의 상대 SG에 연결하는 구조다.

## Secure Gateway와 인증

<!-- learn-page-id: advanced-source-21-page-04 -->

이 단원의 철수는 부산 지사 소속이므로 부산의 SG에 VPN Client로 접속한다. SG는 VPN 사용을 위해 별도의 주소를 할당한다. 이 구간에서 접속 대상 게이트웨이의 위치를 다시 바로잡으며, 직원의 소속과 실제 터널 경로를 구별해 설명한다.

## 사내에서 사용할 주소 할당

<!-- learn-page-id: advanced-source-21-page-05 -->

할당 주소를 3.3.3.50으로 가정하면, PC에는 집에서 쓰는 주소와 VPN에서 쓰는 주소 두 개가 생긴다. 두 번째는 부산 지사의 네트워크와 연결되는 주소다. DB에 보낼 원본 패킷은 출발지 3.3.3.50, 목적지 5.5.5.100이 된다.

## 터널을 지나는 통신

<!-- learn-page-id: advanced-source-21-page-06 -->

VPN Client는 원본 패킷을 보호해 안에 넣고 바깥 헤더를 붙인다. Outer IP의 출발지는 집의 9.9.9.9, 목적지는 부산 SG의 3.3.3.1이다. 인터넷에서는 이 바깥 헤더를 근거로 SG까지 전달한다. 내부 목적지와 터널의 목적지를 구별해야 한다.

## 사내 서버까지의 경로

<!-- learn-page-id: advanced-source-21-page-07 -->

부산 SG는 외부 포장을 제거하고 복호화해 원본을 얻는다. 원본은 VPN 주소 3.3.3.50에서 본사 서버 5.5.5.100으로 가는 패킷이다. 부산에서 서울로 가는 구간에도 지사 간 VPN이 있으므로, 이번에는 그 터널의 포장을 적용한다.

## 출발지 주소와 내부 접속

<!-- learn-page-id: advanced-source-21-page-08 -->

새 Outer IP는 부산 SG 3.3.3.1에서 서울 SG 5.5.5.1로 설정한다. 안쪽 원본은 다시 암호화해 전달한다. 서울 SG에서 바깥 헤더를 제거하고 복호화하면 원래 PC와 서버의 통신이 나오며, 이를 본사 서버에 전달한다.

## 밖에서도 사내처럼 일하기

<!-- learn-page-id: advanced-source-21-page-09 -->

서버는 3.3.3.50을 상대로 응답하고, 응답도 각 터널을 거쳐 집 PC로 돌아간다. 서버 관점에서는 부산 사무실에 있는 같은 주소의 PC와 통신하는 것과 비슷하게 처리할 수 있다. 서울 소속 직원이 서울 SG로 직접 VPN 접속한다면 부산을 거칠 필요가 없어 경로가 달라질 수 있다. G-to-E와 G-to-G를 결합한 예다.

## 재택근무 구성 정리

<!-- learn-page-id: advanced-source-21-page-10 -->

전달 경로에 따라 외부 헤더를 붙이고 제거하며 암호화와 복호화를 반복한다. 집의 인터넷 주소와 VPN으로 할당받은 주소, 안쪽 통신과 바깥 터널의 주소를 구별하는 것이 핵심이다. 다만 모든 보호 대상 서버에 VPN 접근을 허용하는 것은 아니다. 회사 정책상 물리적으로 현장에 와야 하는 폐쇄망 구성도 있을 수 있다. 재택근무 허용 범위는 실제 보안 정책에 따른다.

## VPN이 바꾸는 접속 위치

<!-- learn-page-id: advanced-source-22-page-01 -->

VPN은 사설망을 확장하거나 여러 네트워크를 연결하는 데 사용한다. 같은 중계와 주소 특성이 원래 목적과 다르게 악용되는 경우도 있다. 설명을 위해 철수가 중국으로 출장 가서 9.9.9.9라는 주소로 인터넷을 쓰고, 업무상 VPN Client로 회사 서버에 접속하는 상황을 가정한다.

## 서버가 보는 접속 IP

<!-- learn-page-id: advanced-source-22-page-02 -->

VPN을 끈 상태에서 한국의 게임 서버에 접속하면 서버는 외부에 보이는 IP를 바탕으로 중국 지역 접속이라고 판단할 수 있다. 지역별 서버를 운영하는 게임이라면 다른 지역 서버로 안내할 수 있다. 여기서는 서버가 보는 접속 주소와 사용자의 실제 위치 관계를 설명하는 예다.

## 지역에 따른 접근 차이

<!-- learn-page-id: advanced-source-22-page-03 -->

기존 게임 기록이 한국 서버에 있는 사용자는 다른 지역 서버를 이용하기 불편할 수 있다. 이 상황에서 VPN을 켜면 서버가 보는 접속 경로가 달라질 수 있다고 설명한다. 그림에는 VPN 쪽 주소 3.3.3.40과 게임 서버 7.7.7.7이 등장한다. 이는 통신 구조를 위한 예시 값이다.

## 다른 출구로 트래픽 보내기

<!-- learn-page-id: advanced-source-22-page-04 -->

터널의 바깥 패킷은 출장지에서 SG로 전달되고, SG는 원본을 꺼내 다른 경로로 내보낸다. 그 결과 원격 서버가 사용자의 실제 출장지보다 VPN의 출구 쪽을 접속 위치로 판단할 수 있다. 이 절은 이를 실제 접속 위치를 감추는 효과와 연결해 설명한다. 특정 서비스에서 언제나 같은 결과가 난다는 보장은 아니다.

## 우회의 문제점

<!-- learn-page-id: advanced-source-22-page-05 -->

접속 지역만으로 사용 범위를 제한하는 서비스에서는 이러한 경로 변경이 정책 우회 문제가 될 수 있다. 게임뿐 아니라 스팸·마케팅 용도의 주소 변경도 악용 사례로 언급한다. 일부 서비스가 사용 이력이 적은 ‘클린 IP’를 홍보하는 현상도 이 맥락에서 설명한다.

## IP에 대한 판단과 평판

<!-- learn-page-id: advanced-source-22-page-06 -->

탐지 체계가 악성 행위에 사용된 주소를 차단하면, 공격자가 다른 주소로 바꾸어 다시 시도하는 문제가 생길 수 있다. 이 예시에는 3.3.3.40에서 14.14.4.4 같은 다른 주소로 바꾸는 예가 나온다. 따라서 IP의 평판과 차단만으로 행위 주체를 완전히 구별하기는 어렵다는 취지다.

## 여러 경로로 이어지는 통신

<!-- learn-page-id: advanced-source-22-page-07 -->

이 절은 IPsec 외에 PPTP VPN도 소개한다. 일부 공유기가 VPN 서버 기능을 제공하므로 공유기의 관리자 접근과 보안 패치 상태도 중요하다는 설명으로 이어진다. 이 단원의 예는 VPN 기능이 있는 공유기를 전제로 한다.

## 장악된 PC와 악용

<!-- learn-page-id: advanced-source-22-page-08 -->

공유기 관리 권한이 탈취되면 공격자가 그 장비를 외부 통신의 중계 지점으로 악용할 수 있다. 원격 서비스의 기록에는 피해자의 공유기가 사용하는 공인 주소가 남을 수 있어 실제 행위자와 주소 명의자가 달라진다. 이 경우 공유기 소유자도 침해 피해자일 수 있다. 접속 IP만 보고 주체를 단정하기 어려운 이유다.

## 제한을 우회하려는 사례

<!-- learn-page-id: advanced-source-22-page-09 -->

학교의 접속 제한을 집의 VPN으로 우회하려는 사례와 여러 중계 지점을 거치는 공격을 함께 언급한다. 경로가 복잡해지거나 중간 기록이 끊기면 역추적이 어려워질 수 있다. 이는 우회를 권하는 사용 안내가 아니라 VPN이 정상 목적과 다르게 사용될 수 있다는 문제 설명이다.

## 접속 IP만으로 판단하는 한계

<!-- learn-page-id: advanced-source-22-page-10 -->

접속 IP는 네트워크상의 관찰 지점이며 실제 사람의 위치나 신원을 그대로 증명하는 정보는 아니다. VPN 출구와 여러 중계 경로를 고려해야 한다. 공유기 보안 관리와 탐지·추적의 한계를 이해하고 대응을 설계하는 것이 이 사례의 목적이다. 이 사례는 보안 관리와 추적의 한계를 이해하고 대응을 설계하기 위한 것이다.
