---
id: u2-l05-osi-7-layer와-식별자
title: OSI 7 layer와 식별자
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-05.md
wiki_diagram: units/02-internet-basics/lessons/01-osi-7-layer와-식별자/assets/diagrams/lesson-05.svg
page_metadata:
- terms:
  - OSI 7 layer
  animations:
  - file: l05-osi-layer-stack.svg
    title: 일곱 층으로 나눠 보는 통신
    alt: 아래에서 위로 일곱 개의 가로 막대가 쌓이고 각 층의 이름이 붙은 뒤, 맨 위에서 작은 상자가 한 층씩 아래로 내려갑니다.
    caption: 통신을 일곱 층으로 쌓아 놓고, 위에서 만든 데이터가 한 층씩 내려가는 모습입니다.
- terms:
  - 장치 드라이버(Device driver)
  - L2 / L3 / L4
- terms:
  - 식별자(Identifier)
- terms:
  - MAC 주소(MAC address)
  - NIC / 네트워크 인터페이스
  - 16진수
  animations:
  - file: l05-mac-per-nic.svg
    title: MAC 주소는 NIC마다 하나
    alt: 컴퓨터 한 대의 아래쪽에 NIC가 하나씩 늘어 세 개가 되고, NIC마다 서로 다른 MAC 주소 표찰이 붙습니다.
    caption: 컴퓨터는 한 대여도 NIC가 3개면 MAC 주소도 3개입니다.
- terms:
  - IP 주소(IP address)
  - 호스트(Host)
- terms:
  - 포트 번호(Port number)
  - 포트(Port)
  - 프로세스(Process)
- terms:
  - 명령 프롬프트 / 터미널
  - ipconfig / ifconfig
- terms:
  - DoD 분류
  - 액세스 단(Access)
- terms:
  - 세 가지 식별자
  animations:
  - file: l05-three-identifiers.svg
    title: 세 식별자는 무엇을 가리킬까
    alt: 건물 모양의 호스트에 출입문 세 개가 나타나 MAC 주소 표찰이 붙고, 지붕에 IP 주소가 붙으며, 안쪽 방에 포트 번호가 켜지는
      장면입니다.
    caption: 문마다 MAC, 건물 전체에 IP, 사무실 호수에 포트 번호가 붙습니다.
animations_dir: units/02-internet-basics/lessons/01-osi-7-layer와-식별자/assets/animations
---

핵심 개념을 주제별로 정리했다.

## OSI 계층을 훑어보기

OSI 7 layer는 네트워크 통신에 필요한 일을 일곱 역할로 나누어 설명하는 모델이다. 아래부터 물리, 데이터 링크, 네트워크, 전송, 세션, 표현, 응용 계층 순서로 놓인다. 처음에는 계층 이름과 순서만 익히면 된다. 각 계층에서 실제로 어떤 일이 일어나는지는 관련 개념을 만날 때 연결해 보자.

## 계층을 실제 구성요소에 연결하기

계층을 실제 구성 요소에 연결하면 아래에는 NIC와 장치 드라이버가 있고, 그 위에 IP와 TCP를 구현한 소프트웨어가 있다. User mode에는 HTTP를 사용하는 Chrome 같은 브라우저가 놓인다. 그림에서 IP는 L3, TCP는 L4에 해당한다. L2는 드라이버와 하드웨어에 걸쳐 표현된다. 이 절은 아래쪽 구성 요소부터 위쪽으로 올라가며 핵심 내용을 살펴보는 방식으로 진행한다.

## 식별자는 무엇을 구별할까

식별자는 어떤 대상을 구별하는 근거가 되는 정보다. 사람의 이름, 학생의 학번이나 반 번호, 대한민국 국민의 주민등록번호를 예로 들 수 있다. 네트워크에서도 계층마다 어떤 대상을 무엇으로 식별하는지 구분하는 것이 중요하다.

## MAC 주소 · 인터페이스

L2 Ethernet에서 중요한 식별자는 MAC 주소다. 하드웨어 주소 또는 Physical Address라고도 부른다. MAC 주소가 식별하는 대상은 NIC, 즉 네트워크 인터페이스다. 컴퓨터 자체에 하나씩 붙는 식별자로 생각해서는 안 된다. 이 단원의 예에서 컴퓨터에 NIC가 3개 있으면 MAC 주소도 3개, NIC가 5개 있으면 MAC 주소도 5개다.

## IP 주소 · 호스트

L3 네트워크 계층에서 중요한 식별자는 IP 주소다. IP에는 버전 4와 6이 있으며, 이 과정에서는 IPv4만 다룬다.

## 포트 번호 · 관점에 따른 의미

IP 주소는 인터넷을 사용하는 컴퓨터인 호스트를 식별한다. L4에서 중요한 식별자는 포트 번호다. 다만 ‘포트’라는 말은 업무와 관점에 따라 다른 대상을 가리킬 수 있다. 케이블을 연결하는 L2 장비를 다루는 관점에서는 물리적인 포트, 즉 인터페이스를 뜻한다. 네트워크 관리 관점에서는 웹 서비스를 위해 포트를 개방한다는 식으로 서비스 식별자라고 설명한다. PC나 서버의 소프트웨어를 개발·관리하는 관점에서는 프로세스를 식별하는 값으로 설명한다. 따라서 포트라는 표현이 나올 때는 물리 인터페이스를 말하는지, 서비스나 프로세스와 연결된 포트 번호를 말하는지 문맥을 구별해야 한다. 컴퓨터의 네트워크 정보를 확인하는 명령으로는 Windows의 ipconfig가 있다.

## 내 컴퓨터의 식별자 확인

Windows 명령 프롬프트에서 ipconfig /all을 실행하면 네트워크 인터페이스 정보를 확인할 수 있다. 출력의 ‘물리적 주소’가 MAC 주소다. 예시 화면에서는 88, 36, 6C 등의 16진수로 표현되며, 전체 길이는 48비트다. 같은 출력에서 IPv4 주소도 확인할 수 있다. 직접 명령을 실행해 MAC 주소와 IP 주소가 어떻게 표시되는지 살펴보면 좋다. Linux에서 확인하는 명령으로 ifconfig를 소개한다. 각 정보의 자세한 의미는 해당 주제를 다룰 때 다시 설명한다.

## DoD 분류와 계층 묶기

계층을 나누는 방법이 OSI만 있는 것은 아니다. 미국 국방부의 DoD 분류는 네 계층으로 묶는다. OSI의 L1과 L2를 Network Access 계층으로, L3를 Internet 계층으로, L4를 Host to Host 계층으로 설명하고, 상위 계층은 Application으로 묶는다. ‘액세스 계층’이나 ‘액세스 단’이라는 표현은 하드웨어와 가까운 관점의 설명에서 등장한다. Host는 컴퓨터라는 뜻으로 이해하면 된다. OSI 분류와 함께 이러한 묶음 방식도 알아두면 네트워크 설명을 읽는 데 도움이 된다.

## 세 가지 식별자 정리

여기서 기억할 핵심은 식별 대상이다. MAC 주소는 NIC를, IP 주소는 호스트를 식별한다. 포트라는 말은 L2 인터페이스를 뜻할 수도 있고, 포트 번호를 통해 서비스나 프로세스를 가리킬 수도 있다. 구체적인 의미는 이후 여기서 문맥에 맞추어 다시 다룬다.
