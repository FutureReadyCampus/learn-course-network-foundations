---
id: u5-l26-tcp-연결과정
title: TCP 연결과정
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-26.md
wiki_diagram: units/05-tcp-and-udp/lessons/02-tcp-연결과정/assets/diagrams/lesson-26.svg
page_metadata:
- terms:
  - 3-way handshake
  - 시간축
- terms:
  - RTT
  - ms(밀리초)
  - 포트(port)
- terms:
  - SYN
  - Payload(페이로드)
  - 순서번호
- terms:
  - ACK
- terms:
  - SYN+ACK
  animations:
  - file: l26-three-way-handshake.svg
    title: 세 번의 악수와 순서번호
    alt: 왼쪽 클라이언트와 오른쪽 서버 사이에 세 개의 화살표가 위에서 아래로 차례로 나타나며 SYN 1000, SYN+ACK 4000 확인
      1001, ACK 4001이 표시됩니다.
    caption: SYN 1000, SYN+ACK 4000/1001, ACK 4001이 시간 순서로 오가며 양쪽이 번호를 맞춥니다.
- terms:
  - MSS
  - 바이트(byte)
  questions:
  - id: u5-l26-p06-q01
    kind: choice
    difficulty: easy
    prompt: MSS는 무엇의 최대 크기인가요?
    choices:
    - id: a
      text: IP 패킷 전체
      feedback: IP 패킷 전체의 상한은 MTU예요. MSS는 그 안에서 TCP 데이터 부분만 재요.
    - id: b
      text: TCP Segment 하나에 실을 수 있는 TCP 데이터
      feedback: 맞아요. MSS는 헤더를 뺀 TCP 데이터 부분의 최대 크기예요.
    - id: c
      text: Ethernet 프레임 전체
      feedback: MSS는 헤더를 제외한 TCP 데이터만 재요. 프레임 전체를 재는 값이 아니에요.
    - id: d
      text: TCP 연결의 최대 개수
      feedback: 연결 개수와는 관계가 없어요. MSS는 Segment 하나에 담을 데이터 크기예요.
    - id: e
      text: 한 번에 보낼 수 있는 파일 크기
      feedback: 파일 전체 크기가 아니에요. 큰 파일도 MSS 이하의 여러 Segment로 나뉘어 전송돼요.
    answer: b
  - id: u5-l26-p06-q02
    kind: choice
    difficulty: medium
    prompt: IPv4/TCP 헤더가 각각 20바이트이고 옵션이 없으며 MTU가 1,500바이트일 때, 예시 MSS는 얼마인가요?
    choices:
    - id: a
      text: 1,500바이트
      feedback: 1,500은 MTU 값이에요. MSS는 여기서 IP·TCP 헤더를 빼야 해요.
    - id: b
      text: 1,480바이트
      feedback: IP 헤더 20바이트만 뺀 값이에요. TCP 헤더 20바이트도 함께 빼야 해요.
    - id: c
      text: 1,460바이트
      feedback: 맞아요. IP와 TCP 헤더 각 20바이트를 빼면 TCP 데이터 최대 크기 예시는 1,460바이트예요.
    - id: d
      text: 1,440바이트
      feedback: 헤더를 너무 많이 뺐어요. 이 예에서 빼는 값은 IP 20 + TCP 20 = 40바이트예요.
    - id: e
      text: 20바이트
      feedback: 헤더 하나의 크기예요. MSS는 MTU에서 헤더 둘을 뺀 나머지예요.
    answer: c
  question_placements:
  - question_id: u5-l26-p06-q01
    after_paragraph: 1
- terms:
  - LISTEN
  - ESTABLISHED
  - 소켓(socket)
  animations:
  - file: l26-tcp-states.svg
    title: 연결 상태가 바뀌는 순서
    alt: 클라이언트와 서버 양쪽에 상태 이름표가 있고, 메시지가 오갈 때마다 이름표가 SYN_SENT, SYN_RECEIVED, ESTABLISHED로
      바뀝니다.
    caption: 클라이언트는 SYN_SENT에서 ESTABLISHED로, 서버는 LISTEN과 SYN_RECEIVED를 거쳐 ESTABLISHED로
      갑니다.
- terms:
  - Virtual Circuit(가상 회선)
animations_dir: units/05-tcp-and-udp/lessons/02-tcp-연결과정/assets/animations
---

핵심 개념을 주제별로 정리했다.

## 3-way handshake의 의미
<!-- learn-page-id: handshake-meaning -->

TCP는 3-way handshake라는 절차를 거쳐 연결한다. 연결을 기다리는 서버에 클라이언트가 요청하고, 서로 응답을 주고받는 과정이다. 그림의 세로선은 시간축이다. 아래로 내려갈수록 시간이 흐르며, 양쪽 선 사이의 화살표는 메시지 전달을 나타낸다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 3-way handshake는 SYN, SYN-ACK, ACK를 주고받아 TCP 연결 상태를 만든다.
- **적용하기 (Apply):** 세 메시지 뒤 Client와 Server가 연결 데이터 전송을 시작하는 이유를 설명한다.
- **찾아보기 (Lookup):** 플래그 조합과 상태는 TCP 표준을 찾아본다.

## 연결 요청과 RTT

클라이언트가 192.168.0.20의 TCP 80번 서버에 접속한다고 하자. RTT를 50ms로 가정하면 설명을 위해 편도에 약 25ms가 걸린다고 볼 수 있다. 실제 처리 시간 등은 이 단순화에서 제외한다. 이 연결 과정에서도 TCP 세그먼트가 오가지만, 일반적인 파일 데이터 전송과 목적이 다르다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Handshake는 연결 전에 왕복 확인이 필요해 초기 RTT가 든다.
- **적용하기 (Apply):** 첫 데이터 지연에 TCP 설정 왕복이 더해지는 상황을 판단한다.
- **찾아보기 (Lookup):** TLS handshake와 TCP handshake 왕복은 프로토콜 캡처에서 분리한다.

## 연결 제어용 Segment
<!-- learn-page-id: syn-segment -->

연결을 관리하기 위한 예시 세그먼트에는 애플리케이션 Payload 없이 IP 헤더와 TCP 헤더가 있다. 데이터 내용보다 연결 제어 정보를 교환하는 것이다. SYN은 Synchronization의 약자다. 클라이언트는 처음 사용할 순서번호를 임의로 정한다. 여기서는 1000을 선택했다고 가정한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** SYN은 연결 요청, ACK는 상대 Sequence 번호를 확인하는 제어 정보다.
- **적용하기 (Apply):** SYN과 ACK 플래그를 데이터 본문과 혼동하지 않고 캡처에서 찾는다.
- **찾아보기 (Lookup):** 플래그 비트와 조합은 TCP Header 표에서 확인한다.

## 처음 사용할 순서번호
<!-- learn-page-id: ack-sequence -->

클라이언트는 SYN과 함께 자신의 초기 순서번호 1000을 서버에 알린다. 연결을 기다리던 서버는 이를 받았다는 의미로 1을 더한 ACK 1001을 보낸다. 서버도 자신의 초기 순서번호를 임의로 정해 함께 알려 준다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 연결마다 송신 측은 초기 Sequence number를 사용해 바이트 위치를 관리한다.
- **적용하기 (Apply):** Sequence number가 전달 데이터 순서를 확인하는 기준인 이유를 설명한다.
- **찾아보기 (Lookup):** 초기 번호 선택과 상대 번호 공간은 RFC에서 찾아본다.

## SYN과 ACK의 교환

서버의 초기 순서번호를 4000이라고 하면, 클라이언트는 이를 받고 ACK 4001로 응답한다. 이 SYN, SYN+ACK, ACK 교환이 연결 절차의 큰 흐름이다. 양쪽이 연결 완료를 판단하는 시점에는 차이가 있다. 클라이언트는 서버의 SYN+ACK를 받은 시점에 연결된 것으로 판단하지만, 서버는 마지막 ACK를 받아야 연결 완료로 판단한다. 앞의 단순화된 예에서는 그 사이에 편도 약 25ms의 차이가 있다. 이 과정의 중요한 목적은 서로의 순서번호를 교환하는 것이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** SYN과 ACK는 양쪽의 연결 요청·수락과 번호 동기화에 쓰인다.
- **적용하기 (Apply):** 세 번의 메시지에서 각 방향이 확인한 번호를 표로 정리한다.
- **찾아보기 (Lookup):** SYN flood 완화와 backlog 처리는 OS 설정에서 찾아본다.

## MSS 등 통신 조건 교환
<!-- learn-page-id: mss-exchange -->

연결 과정에서는 순서번호 외에도 통신 조건을 교환한다. 대표적인 값은 MSS(Maximum Segment Size)다. 클라이언트와 서버가 모두 1,460을 사용한다면 그 조건으로 통신한다. 상대가 1,400까지만 받을 수 있다고 알리면 그 크기에 맞추어야 한다. 연결은 서로의 조건을 알고 전송 방식을 정하는 과정으로 이해할 수 있다.

MSS와 MTU는 재는 범위가 다르다. MTU는 IP 패킷 전체의 상한이고, MSS는 그 안에서 TCP 데이터 부분만의 상한이다. 기본 IPv4 헤더 20바이트와 옵션이 없는 TCP 헤더 20바이트를 MTU 1,500바이트에서 빼면 `1,500 − 20 − 20 = 1,460`바이트가 MSS가 된다. 옵션이나 IP 버전에 따라 헤더 크기가 달라지면 MSS도 달라질 수 있다. 앞에서 본 Stream은 이렇게 정해진 MSS에 맞춰 여러 Segment로 나뉘어 전송된다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 양쪽은 MSS 등 데이터 전달에 적용할 조건을 handshake에서 교환할 수 있다.
- **적용하기 (Apply):** 양방향 MSS가 다를 수 있음을 큰 파일 전송에 적용한다.
- **찾아보기 (Lookup):** TCP option 종류와 실제 값은 SYN 캡처에서 확인한다.

## 연결 과정의 상태 변화

클라이언트는 SYN을 보내 SYN_SENT 상태가 된 뒤 서버의 응답을 받아 ESTABLISHED로 간다. 서버는 LISTEN 상태에서 SYN을 받아 SYN_RECEIVED로 바뀌고, 마지막 ACK를 받아 ESTABLISHED로 간다. 이처럼 연결은 메시지 교환과 함께 상태 변화로 표현된다. 소켓 생성과 개방은 그 전에 이루어진다는 전제다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 연결 과정은 SYN-SENT, SYN-RECEIVED를 거쳐 ESTABLISHED로 이어진다.
- **적용하기 (Apply):** 연결 요청을 보낸 쪽과 받은 쪽에서 상태가 다르게 움직임을 추적한다.
- **찾아보기 (Lookup):** 구현별 TCP 상태 명칭은 OS 진단 문서에서 확인한다.

## 연결의 의미 정리

TCP 연결은 프로토콜이 정한 관리 정보를 주고받는 과정이다. 초기 순서번호, MSS 등 이후 통신에 필요한 조건이 포함된다. 이 연결은 Virtual Circuit, 즉 논리적인 연결이다. 클라이언트와 서버 사이에 새 전선을 직접 연결하는 것이 아니라 이미 있는 네트워크 위에서 양쪽이 연결 상태를 관리한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Handshake는 전달 보장 자체가 아니라 TCP 상태를 맞추고 시작 조건을 교환한다.
- **적용하기 (Apply):** 연결 수립 성공과 애플리케이션 데이터 전달 성공을 구분한다.
- **찾아보기 (Lookup):** Handshake 뒤 재전송·흐름제어는 후속 TCP Lesson에서 찾아본다.
