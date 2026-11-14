---
id: u8-advanced-16-upnp와-nat
title: UPnP와 자동 포트 설정
source_lesson_ids:
- u8-advanced-16-upnp와-nat
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-16.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-16.md
page_metadata:
- page_id: advanced-source-16-page-01
  illustrations:
  - file: assets/animations/u12-upnp-torrent.svg
    title: "Torrent와 P2P"
    alt: "공유기의 UPnP가 켜진 상태에서 바깥 상대의 연결이 공유기를 지나 집 PC의 Torrent까지 도착하는 모습입니다."
    caption: "UPnP가 있으면 수동 설정 없이 P2P 연결이 이어질 수 있습니다."
    after_paragraph: 0
- page_id: advanced-source-16-page-02
  illustrations:
  - file: assets/animations/u12-upnp-pnp.svg
    title: "UPnP라는 기능"
    alt: "USB 저장장치를 PC에 꽂으면 설정 없이 바로 쓰이는 모습으로 Plug and Play를 설명합니다."
    caption: "UPnP는 Plug and Play의 생각을 네트워크로 넓힌 기능입니다."
    after_paragraph: 0
- page_id: advanced-source-16-page-03
  illustrations:
  - file: assets/animations/u12-upnp-history.svg
    title: "Plug and Play의 배경"
    alt: "예전에는 프린터 드라이버를 직접 설치·설정해야 했고, PnP 이후에는 자동으로 인식·준비되는 것을 나란히 비교합니다."
    caption: "사람이 하던 설정을 자동화하는 것이 PnP와 UPnP의 공통점입니다."
    after_paragraph: 0
- page_id: advanced-source-16-page-04
  illustrations:
  - file: assets/animations/u12-upnp-coupon.svg
    title: "밖에서 집 안 프린터까지"
    alt: "홈쇼핑 쿠폰 인쇄 요청이 집으로 오지만 NAT 공유기에서 막혀 PC와 프린터에 닿지 못하는 모습입니다."
    caption: "NAT 뒤 PC로는 바깥에서 먼저 시작한 연결이 바로 들어오지 못합니다."
    after_paragraph: 0
- page_id: advanced-source-16-page-05
  illustrations:
  - file: assets/animations/u12-upnp-manual-vs-auto.svg
    title: "NAT가 가로막는 접속"
    alt: "왼쪽은 사용자가 설정 화면에 직접 입력하는 수동 포트 포워딩, 오른쪽은 프로그램이 SSDP로 공유기를 찾아 자동 설정하는 UPnP를 비교합니다."
    caption: "UPnP는 포트 포워딩 설정을 프로그램이 대신하게 합니다."
    after_paragraph: 0
- page_id: advanced-source-16-page-06
  illustrations:
  - file: assets/animations/u12-upnp-mapping-request.svg
    title: "프로그램이 매핑을 요청하기"
    alt: "Torrent가 자동 설정 서비스를 찾고 6881번 매핑을 요청하면 공유기 표에 198.51.100.25:6881 → 192.168.0.10:6881이 생기고 바깥 연결이 PC까지 들어옵니다."
    caption: "프로그램이 필요한 포트 포워딩을 공유기와 협의해 자동으로 설정합니다."
    after_paragraph: 0
- page_id: advanced-source-16-page-07
  illustrations:
  - file: assets/animations/u12-upnp-compare.svg
    title: "UPnP와 NAT를 함께 보기"
    alt: "수동 설정은 사용자가, UPnP는 프로그램이 입력한다는 비교표와 공유기 지원·설정이 전제라는 조건을 보여 줍니다."
    caption: "UPnP는 사용자의 입력 부담을 줄여 P2P 연결을 돕습니다."
    after_paragraph: 0
- page_id: advanced-source-16-page-08
  illustrations:
  - file: assets/animations/u12-upnp-dev.svg
    title: "P2P 프로그램 개발로"
    alt: "P2P 프로그램을 만들 때 서비스 발견, 매핑 요청, 주소·포트 매핑 이해를 차례로 챙기는 체크리스트입니다."
    caption: "서비스 발견과 매핑 요청은 NAT 환경 P2P 설계의 기본입니다."
    after_paragraph: 0
---

## Torrent와 P2P

<!-- learn-page-id: advanced-source-16-page-01 -->

Torrent 같은 P2P 프로그램이 공유기의 수동 설정 없이 통신하는 이유를 UPnP와 연결해 살펴본다. 자료의 ipTIME 화면에는 UPnP가 실행 중인 상태로 표시된다. 여기서는 공유기가 해당 기능을 지원하고 사용할 수 있도록 설정되어 있다는 예를 전제로 한다.

## UPnP라는 기능

<!-- learn-page-id: advanced-source-16-page-02 -->

UPnP는 Universal Plug and Play다. 먼저 PnP는 장치를 꽂으면 사용할 수 있도록 설정을 돕는 개념이다. 이 절은 Windows 98 시절과 USB의 보급을 예로 설명한다. USB 저장장치를 연결하고 분리할 때 사용자가 매번 복잡한 설정을 할 필요가 줄어든 모습과 연결된다.

## Plug and Play의 배경

<!-- learn-page-id: advanced-source-16-page-03 -->

과거 프린터를 병렬 포트 등에 연결할 때는 드라이버 설치와 설정이 필요했다. PnP 환경에서는 장치를 인식하고 필요한 드라이버를 준비해 사용 가능한 상태로 만드는 작업이 자동화된다. 별도 설치가 필요한 장치도 있지만 공통적인 사용 부담이 줄었다는 설명이다. UPnP도 여러 장치의 연결과 설정을 자동화하는 관점으로 이해할 수 있다. 이를 홈쇼핑의 쿠폰 인쇄 예로 확장한다.

## P2P가 여러 상대와 만나는 구조

<!-- learn-page-id: advanced-source-16-page-04 -->

홈쇼핑을 보던 사용자가 버튼을 눌러 집의 프린터에서 쿠폰을 인쇄한다고 가정해 보자. 외부 서비스의 요청이 집 안 PC에 도달하고, PC가 연결된 프린터에 명령을 전달해야 한다. 하지만 집의 PC가 NAT 공유기 뒤에 있다면 외부에서 바로 들어오는 연결이 제한된다. 단순히 버튼을 누르는 사용 흐름 안에서 이 문제를 해결해야 한다.

## NAT가 가로막는 접속

<!-- learn-page-id: advanced-source-16-page-05 -->

사용자에게 공유기 설정 화면을 열어 포트 포워딩을 직접 지정하라고 요구하기는 어렵다. 이 과정을 자동화하는 기능을 UPnP와 연결해 설명한다. 서비스 발견 프로토콜인 SSDP(Simple Service Discovery Protocol)를 소개하며, 이를 지원하는 Torrent 프로그램과 공유기의 상호작용을 예로 든다.

## 프로그램이 매핑을 요청하기

<!-- learn-page-id: advanced-source-16-page-06 -->

P2P 프로그램은 네트워크에서 자동 설정을 도와줄 서비스를 찾고, 공유기가 응답하면 사용할 포트에 대한 매핑을 요청하는 흐름이다. 쉽게 말해 프로그램이 필요한 포트 포워딩을 공유기와 협의해 자동으로 설정하는 것이다.

## UPnP와 NAT를 함께 살펴보기

<!-- learn-page-id: advanced-source-16-page-07 -->

이 동작을 이해하려면 UPnP와 SSDP, 그에 연결된 서비스 규격을 살펴보면 된다. 핵심은 사용자가 직접 외부 포트와 내부 대상을 입력하는 부담을 줄여 P2P 연결을 돕는다는 점이다. 공유기의 지원 여부와 실제 설정이 전제다. 이 절은 당시 국내 공유기의 지원 사례를 들어 이 자동화가 널리 활용되는 배경을 설명한다.

## P2P 프로그램 개발로 이어 보기

<!-- learn-page-id: advanced-source-16-page-08 -->

P2P 프로그램을 개발한다면 서비스 발견과 매핑 요청을 어떻게 처리할지 함께 설계해야 한다. UPnP와 SSDP를 알아두면 NAT 환경의 연결 문제를 이해하는 데 도움이 된다. 이로써 공유기의 기본 원리와 외부 접속 문제를 살펴보았다. 다음 기술도 이 주소·포트 매핑을 바탕으로 이해하므로 필요하다면 앞의 내용을 복습하면 좋다.
