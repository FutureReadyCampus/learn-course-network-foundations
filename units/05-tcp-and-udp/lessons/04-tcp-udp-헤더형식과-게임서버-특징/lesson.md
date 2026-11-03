---
id: u5-l28-tcp-udp-헤더형식과-게임서버-특징
title: TCP, UDP 헤더형식과 게임서버 특징
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-28.md
wiki_diagram: units/05-tcp-and-udp/lessons/04-tcp-udp-헤더형식과-게임서버-특징/assets/diagrams/lesson-28.svg
page_metadata:
- terms:
  - 포트 번호 (Port Number)
  - Well-known Port
  animations:
  - file: l28-port-apartment.svg
    title: IP는 건물, 포트는 호수
    alt: 데이터 상자가 건물 모양 컴퓨터에 도착한 뒤, 목적지 포트 80이 적힌 호수의 문으로 들어가는 장면입니다.
    caption: 도착한 데이터는 IP로 컴퓨터를 찾고, 포트 번호로 알맞은 프로그램을 찾아갑니다.
- terms:
  - Sequence Number
  - ACK (Acknowledgement)
  - Data Offset
- terms:
  - 제어 플래그 (Control Flag)
  - RST (Reset)
- terms:
  - Window Size
  - Zero Window
  - Checksum (검사합)
  animations:
  - file: l28-window-buffer.svg
    title: 받을 자리를 알리는 Window
    alt: 수신 버퍼 칸이 데이터로 차오르며 Window 숫자가 줄어 0이 되는 장면입니다.
    caption: 프로그램이 데이터를 가져가는 속도가 느리면 수신 버퍼가 차고 Window는 0이 됩니다.
- terms:
  - UDP (User Datagram Protocol)
  - 흐름 제어 (Flow Control)
  - 혼잡 제어 (Congestion Control)
- terms:
  - 동기화
  - 지연 (Latency)
  animations:
  - file: l28-udp-game-latest.svg
    title: 기다리는 TCP, 건너뛰는 UDP
    alt: 위아래 두 줄에서 TCP 줄은 사라진 3번 때문에 멈추고 UDP 줄은 3번을 건너뛰어 최신 위치가 보이는 장면입니다.
    caption: 위치 3번이 사라졌을 때 TCP는 기다리고 UDP는 최신 5번으로 넘어갑니다.
- terms:
  - HTTP/3
animations_dir: units/05-tcp-and-udp/lessons/04-tcp-udp-헤더형식과-게임서버-특징/assets/animations
---

핵심 개념을 주제별로 정리했다.

## Port · 송수신 프로세스 식별

TCP 헤더 도식은 가로 32비트를 기준으로 표현한다. 출발지와 목적지 포트 번호는 각각 16비트이므로 표현 범위는 0~65,535다. 예시에는 양 끝값을 제외한 사용 가능 개수 설명도 있지만, 해당 설명은 별도 확인이 필요하다. 서비스별로 정해 둔 Well-known Port가 있다. 예를 들어 이 단원의 HTTP 웹 서비스는 TCP 80번을 기본으로 사용하므로 브라우저 주소에 :80을 생략할 수 있다. 기본값과 다른 포트를 쓰면 명시한다. FTP나 Telnet에도 정해진 포트가 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Port 번호는 같은 Host에서 통신할 프로세스를 구분하는 값이다.
- **적용하기 (Apply):** IP가 같은 서버에서 Port가 다른 서비스 연결을 구별한다.
- **찾아보기 (Lookup):** 등록 포트와 동적 포트 범위는 IANA 및 OS 설정에서 확인한다.

## Sequence와 Acknowledgement

Sequence Number는 전송한 데이터의 바이트 수에 따라 증가한다. 100바이트를 보내면 100, 1,000바이트면 1,000, 1,460바이트면 1,460만큼 진행하는 식이다. Acknowledgement Number 필드에는 앞 Lesson에서 본 ACK 값, 곧 수신 측이 다음에 기대하는 바이트 위치가 담긴다. Data Offset은 TCP Payload가 시작하는 위치를 해석하는 데 필요한 값이다. 옵션 유무에 따라 헤더 길이가 달라질 수 있다는 점에서 IP의 IHL과 연결해 이해할 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Sequence는 송신 바이트 위치, Acknowledgment는 다음 기대 위치를 나타낸다.
- **적용하기 (Apply):** 데이터 길이와 ACK 증가량을 이용해 바이트 진행을 계산한다.
- **찾아보기 (Lookup):** 재전송과 누적 ACK 예시는 Wireshark에서 확인한다.

## 제어 플래그

TCP 제어 플래그에는 앞서 본 SYN, FIN, ACK가 있다. 연결 요청과 종료, 응답을 나타낼 때 사용하는 정보다. RST는 문제가 생긴 연결을 리셋하거나 비정상적으로 종료하는 상황과 연결된다. PSH를 버퍼링에 지체하지 않고 데이터를 전달하라는 취지로 소개한다. 각 플래그의 정교한 동작과 혼잡 제어 관련 내용은 여기서 깊이 다루지 않는다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** SYN·ACK·FIN·RST 등 TCP flag는 연결 제어 상태를 표시한다.
- **적용하기 (Apply):** 연결 수립·종료·강제 초기화 패킷의 flag를 비교한다.
- **찾아보기 (Lookup):** flag 조합과 reserved bit는 TCP Header 사양을 찾아본다.

## 윈도(Window) · 수신 버퍼의 여유

윈도 크기(Window Size) 필드에는 앞 Lesson에서 본 수신 윈도우, 곧 수신 버퍼의 여유 공간이 담긴다. 이 값이 0이면 제로 윈도(Zero Window)다. 윈도에 맞춰 보내는 양을 조절하는 것이 흐름 제어라면, 앞 Lesson의 Loss, Retransmission, Duplicate ACK 같은 신호를 바탕으로 네트워크 상황에 맞춰 전송량을 조절하는 것은 혼잡 제어와 연결된다. 세부 제어 알고리즘은 이 과정의 범위를 벗어난다. Checksum은 전송한 데이터에 손상이 있는지 확인하는 검사합이다. TCP의 세부 제어는 복잡하므로 여기서는 헤더의 전체 구성을 익힌다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Window 값은 수신 측이 받아들일 수 있는 데이터 여유를 송신 측에 알린다.
- **적용하기 (Apply):** Window가 작아질 때 송신 속도가 제한될 수 있음을 판단한다.
- **찾아보기 (Lookup):** Window scale option과 실제 바이트 단위 값은 캡처에서 확인한다.

## 간결한 UDP Header

UDP 헤더는 TCP보다 간결하다. 출발지·목적지 포트, 길이, Checksum을 중심으로 구성된다. UDP 자체는 TCP와 같은 혼잡 제어나 수신 버퍼의 여유 공간을 확인하는 흐름 제어를 제공하지 않는다. 이러한 차이를 앞서 상대의 상태를 고려하는 방식의 차이로 설명했다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** UDP Header는 Source/Destination Port, Length, Checksum 등으로 간결하다.
- **적용하기 (Apply):** UDP Header 필드가 TCP보다 적다는 것이 앱 수준 보장을 뜻하지 않음을 설명한다.
- **찾아보기 (Lookup):** IPv4/IPv6별 checksum 규칙은 UDP 표준에서 확인한다.

## 게임 서버와 UDP

영상 송출 서버에 여러 사용자가 접속하고, 각 사용자의 회선이 서로 다르다고 하자. 가장 느린 한 사람 때문에 모든 사람의 송출을 느리게 하는 것이 적절하지 않을 수 있다. 이를 UDP를 활용할 이유로 설명한다. 게임에서도 상태 동기화와 지연 처리가 중요하다. TCP는 중간 데이터가 빠지면 이를 다시 받으려 하므로, 순서를 기다리는 동안 처리가 지연될 수 있다. 실시간 게임에서는 일부 중간 상태를 건너뛰고 최신 상태를 전달하는 편이 더 적절한 경우가 있다. 화면에서 캐릭터가 순간 이동하듯 보이는 현상과 연결해 생각할 수 있다. UDP를 사용하면 개발자가 필요한 혼잡 제어와 동기화 로직을 애플리케이션에 직접 설계할 수 있다. 모든 중간 데이터를 반드시 복구할지, 오래된 상태는 버릴지 선택할 수 있다는 점이다. 이런 이유로 게임과 멀티미디어 전송에서 UDP가 사용된다고 설명한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 게임은 지연과 실시간성을 위해 UDP 위에 앱별 처리 규칙을 만들 수 있다.
- **적용하기 (Apply):** 손실·순서 보장 대신 앱이 최신 상태를 우선하는 상황을 구별한다.
- **찾아보기 (Lookup):** 특정 게임의 전송 방식을 일반화하지 말고 캡처나 개발 문서를 확인한다.

## HTTP/3 등 확장되는 활용

HTTP/3에서도 UDP를 활용한다. 여기서는 이를 TCP가 제공하는 처리 전체에 의존하기보다 필요한 제어를 다른 계층에서 구성하는 방향과 연결해 소개한다. 여기서는 TCP와 UDP 헤더의 복잡도와 기능 차이를 이해하면 된다. 혼잡 제어의 구체적인 알고리즘은 별도의 자료에서 더 깊이 살펴보아야 한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** HTTP/3는 QUIC 위에서 동작하며 QUIC은 UDP를 기반으로 한다.
- **적용하기 (Apply):** HTTP/3와 TCP 기반 HTTP/2를 Transport 층에서 구분한다.
- **찾아보기 (Lookup):** 현재 브라우저가 협상한 HTTP 버전은 개발자 도구나 네트워크 캡처에서 확인한다.
