---
id: u8-tcp-ack-재전송과-window
title: TCP의 ACK, 재전송과 Window
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-16.md
wiki_diagram: units/08-tcp-udp-details/lessons/01-tcp-ack-재전송과-window/assets/diagrams/lesson-16.svg
page_metadata:
- terms:
  - 확인 응답 (ACK, Acknowledgment)
  - 순서 번호 (Sequence Number)
  illustrations:
  - file: assets/animations/l16-daily-next-box-number.svg
    title: "다음에 받을 번호를 알려 줘요"
    alt: "보내는 사람이 1번, 2번 상자를 보내면 받는 사람 칸에 도착하고, 받는 사람이 “3번 주세요”라는 수령 문자를 돌려보냅니다. 앞은 받았으니 3번 상자가 출발합니다."
    caption: "수령 문자의 ‘3번 주세요’는 1·2번까지 연속해서 받았다는 뜻입니다. 확인을 기다리지 않고 여러 상자를 보내도 됩니다."
    after_paragraph: -1
  - file: assets/animations/l16-tcp-ack.svg
    title: "ACK는 다음에 받을 바이트 위치를 가리켜요"
    alt: "왼쪽 송신 측에서 1번과 2번 상자가 오른쪽 수신 측으로 가고, ACK 3이라고 적힌 말풍선이 돌아옵니다. 이어 3번 상자가 출발하는 단순화된 누적 확인 예시입니다."
    caption: "그림에서 ACK 3은 앞의 두 조각을 연속해서 받았다는 뜻입니다. 실제 번호는 바이트 기준이고, 송신 측은 여러 조각을 동시에 보낼 수 있습니다."
    after_paragraph: 2
- terms:
  - 수신 윈도 (Receive Window)
  - 수신 버퍼 (Receive Buffer)
  - 흐름 제어 (Flow Control)
  - 혼잡 제어 (Congestion Control)
  illustrations:
  - file: assets/animations/l16-daily-tray-free-slots.svg
    title: "트레이에 남은 자리를 알려 줘요"
    alt: "서류 트레이 8칸 중 3칸이 차 있고 남은 자리는 5칸입니다. 처리가 늦으면 6칸이 차서 남은 자리가 2칸이 되고, 처리해 가면 다시 늘어납니다. 마지막에 받는 쪽 자리와 길이 감당하는 양은 다른 문제라고 표시됩니다."
    caption: "남은 자리가 있는 만큼만 더 받을 수 있습니다. 한 칸은 설명용 단위입니다."
    after_paragraph: -1
  - file: assets/animations/l16-receive-window-free-space.svg
    title: "수신 윈도는 남은 버퍼 공간"
    alt: "수신 버퍼 8칸 중 3칸이 차 있고 윈도는 5칸입니다. 프로그램이 늦게 읽으면 윈도가 2칸으로 줄고, 읽으면 다시 늘어납니다. 흐름 제어는 받는 쪽 공간을, 혼잡 제어는 경로가 감당할 수 있는지를 살핍니다."
    caption: "수신 윈도는 더 받아 둘 수 있는 바이트 범위입니다. 한 칸은 설명용 단위이며 속도나 세그먼트 크기가 아닙니다."
    after_paragraph: 1
- terms:
  - 손실 (Loss)
  - 재전송 (Retransmission)
  - 중복 ACK (Duplicate ACK)
  - 재전송 타임아웃 (Retransmission Timeout, RTO)
  illustrations:
  - file: assets/animations/l16-daily-no-news-resend.svg
    title: "소식이 없으면 기다렸다 다시 보내요"
    alt: "1번 상자가 도중에 사라지고 받았다는 소식이 오지 않아 시간이 흐릅니다. 기다릴 시간이 지나면 같은 번호의 상자를 다시 보내 받는 집에 도착합니다."
    caption: "정해진 시간이 지나도 소식이 없으면 같은 상자를 다시 보냅니다."
    after_paragraph: -1
  - file: assets/animations/l16-rto-resend.svg
    title: "RTO가 지나면 다시 전송해요"
    alt: "순서 번호 1001~1500의 세그먼트가 도중에 사라지고 ACK가 오지 않아 RTO를 기다립니다. RTO가 만료되면 같은 순서 번호 범위를 다시 보내고, RTO는 RTT 표본 등으로 조정되며 ping 결과와 같은 값은 아닙니다."
    caption: "타임아웃은 손실 확정이 아니라 확인을 기다릴 시간이 지났다는 뜻입니다. 번호는 예시입니다."
    after_paragraph: 0
- terms:
  - 순서가 어긋난 데이터 (Out of order)
  illustrations:
  - file: assets/animations/l16-daily-later-box-first.svg
    title: "뒤쪽 상자가 먼저 와도 건너뛰지 않아요"
    alt: "1번 상자가 사라지고 2번 상자가 먼저 도착해 보관되지만 1번을 건너뛰어 전달하지는 못합니다. 받는 사람은 “다음은 1번이에요”를 반복해 보내고, 1번이 도착해 이어지면 한꺼번에 전달합니다."
    caption: "빈 구간이 채워져야 순서대로 전달합니다."
    after_paragraph: -1
  - file: assets/animations/l16-out-of-order-dup-ack.svg
    title: "뒤쪽 데이터가 먼저 와도 기다려요"
    alt: "1001~1500이 사라지고 1501~2000이 먼저 도착해 보관되지만 앞 구간을 건너뛰어 프로그램에 전달하지 못합니다. 수신 측은 ACK 1001을 반복하고(중복 ACK), 빠진 구간이 도착해 이어지면 ACK 2001과 함께 연속 데이터로 전달합니다."
    caption: "중복 ACK는 빠진 구간이 있을 수 있다는 단서입니다. 번호는 예시입니다."
    after_paragraph: 0
- terms:
  - 윈도 크기 (Window Size)
  - 제로 윈도 (Zero Window)
  illustrations:
  - file: assets/animations/l16-daily-cup-full-pause.svg
    title: "컵이 가득 차면 잠시 멈춰요"
    alt: "컵에 물이 많이 차 있다가 가득 차면 물 따르기를 잠시 멈추고, 마시면 자리가 생겨 다시 따릅니다. 마지막에 연결을 닫은 것이 아니라고 표시됩니다."
    caption: "컵이 가득 차면 잠시 멈추고 자리가 생기면 다시 따릅니다."
    after_paragraph: -1
  - file: assets/animations/l16-zero-window-pause.svg
    title: "제로 윈도는 잠시 멈추라는 뜻"
    alt: "수신 버퍼가 가득 차 윈도 0을 알리면 송신 측이 새 데이터를 잠시 멈추고, 프로그램이 읽어 공간이 생기면 윈도가 다시 열려 전송이 이어집니다. 연결을 닫은 것이 아닙니다."
    caption: "제로 윈도는 이 수신 측에 지금 새 데이터를 받을 공간이 없다는 알림이며 연결 종료와 다릅니다."
    after_paragraph: 0
- terms:
  - 손실 세그먼트 (Lost Segment)
  - 패킷 캡처 (Packet Capture)
  illustrations:
  - file: assets/animations/l16-daily-tracking-marks.svg
    title: "배송 조회 표식, 무엇을 물을까"
    alt: "분실이 의심돼요, 다시 배송됐어요, 순서가 뒤바뀌어 도착해요, 같은 소식이 반복돼요, 받을 자리가 가득해요의 다섯 표식이 차례로 나타나고 각각 먼저 확인할 질문이 옆에 붙습니다. 표식 하나만으로 원인을 단정하지는 않는다고 표시됩니다."
    caption: "표식마다 먼저 확인할 질문이 다릅니다."
    after_paragraph: -1
  - file: assets/animations/l16-capture-marks-questions.svg
    title: "캡처 표식마다 질문을 골라요"
    alt: "손실 세그먼트, 재전송, 순서가 어긋난 데이터, 중복 ACK, 제로 윈도의 다섯 캡처 표식이 차례로 나타나고 각각 먼저 확인할 질문이 옆에 붙습니다. 표식 하나만으로 원인을 단정하지는 않는다고 표시됩니다."
    caption: "표식 하나만으로 문제가 네트워크 경로인지 애플리케이션인지 단정할 수는 없습니다."
    after_paragraph: 1
animations_dir: units/08-tcp-udp-details/lessons/01-tcp-ack-재전송과-window/assets/animations
---

Unit 5에서는 [IP 헤더의 Protocol 필드](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/5/lesson/1/page/3)가 안쪽 데이터를 TCP·UDP·ICMP 중 무엇으로 넘길지 알려 준다는 것을 배웠다. Unit 6에서는 [ping으로 왕복 시간(RTT)](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/6/lesson/4/page/2)을 살펴봤고, Unit 7에서는 [TCP 연결을 열며 시작 순서 번호를 주고받는 과정](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/7/lesson/2/page/4)을 따라갔다. 이제 그 연결에서 데이터가 빠지거나 늦게 오고 수신 버퍼가 찰 때 TCP가 어떻게 대응하는지 본다. ping의 RTT와 TCP의 재전송 시간은 관련은 있지만 같은 측정값은 아니다.

## 확인 응답(ACK)은 다음 바이트 위치를 알린다

TCP 순서 번호(Sequence Number)는 세그먼트에 붙인 조각 번호가 아니라 데이터 바이트의 위치를 가리킨다. Unit 7 Lesson 2에서 연결을 열 때 시작 번호를 주고받았고, 여기서는 그 번호가 데이터에 어떻게 이어지는지 살펴본다.

예를 들어 A가 연결 요청(SYN, 연결을 시작하자는 신호)에 시작 번호 1000을 사용했다면, SYN 신호도 순서 번호 하나를 사용하므로 첫 데이터 바이트는 1001부터다. A가 1001~1500을 보내고 이어 1501~2000도 보냈다고 하자. B가 두 범위를 빠짐없이 이어서 받으면 `ACK=2001`을 보낼 수 있다.

`ACK=2001`은 “2001번 세그먼트를 보내라”가 아니라 “2000번 바이트까지 이어서 받았고, 다음에는 2001번 바이트를 기다린다”는 뜻이다. ACK는 도착한 바이트 범위를 누적해 확인한다. 그림의 `ACK 3`은 조각 순서를 보여 주는 단순한 표기이고, 실제 ACK 번호는 세그먼트 개수가 아니라 바이트 위치를 가리킨다. 송신 측은 매번 확인 응답 하나를 기다린 뒤에만 다음 데이터를 보내는 것이 아니라, 여러 바이트를 전송 중인 상태로 둘 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** ACK 번호는 연속해서 받은 마지막 바이트 다음 위치를 가리킨다.
- **적용하기 (Apply):** 1001~2000바이트를 받았을 때 `ACK=2001`인 이유를 설명한다.
- **찾아보기 (Lookup):** 선택 확인 응답(SACK) 옵션의 자세한 형식은 TCP 문서에서 확인한다.

## 수신 윈도는 더 받을 공간을 알린다

Unit 4 Lesson 6에서 본 수신 소켓 버퍼는 TCP가 받은 바이트를 애플리케이션이 읽기 전까지 잠시 보관하는 곳이다. 애플리케이션이 바이트를 읽으면 공간이 생기고, 수신 측 TCP는 수신 윈도(receive window)로 상대에게 더 받아 둘 수 있는 양을 알린다. 윈도는 한 세그먼트의 크기나 초당 전송 속도가 아니라, 더 받을 수 있다고 알리는 바이트 범위다.

이 정보를 바탕으로 송신 측이 받는 쪽의 버퍼 용량을 넘지 않도록 조절하는 것이 흐름 제어다. 네트워크 경로가 혼잡할 때 전송량을 조절하는 혼잡 제어와는 다른 문제를 다룬다. 둘 다 전송량을 줄일 수 있지만, 흐름 제어는 “받는 쪽이 받아 둘 공간이 있는가?”, 혼잡 제어는 “경로가 감당할 수 있는가?”를 살핀다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 수신 윈도는 상대가 더 받아 둘 수 있다고 알리는 바이트 범위다.
- **적용하기 (Apply):** 애플리케이션이 늦게 읽으면 윈도가 줄 수 있는 이유를 말한다.
- **찾아보기 (Lookup):** 프로그램별 소켓 버퍼 상태는 운영체제 진단 도구에서 확인한다.

## 확인되지 않은 데이터는 다시 전송한다

세그먼트가 사라졌거나 확인 응답(ACK)이 늦으면, 송신 측은 데이터가 도착했는지 아직 확인하지 못한다. 확인 응답이 오지 않은 채 재전송 타임아웃(RTO)이 만료되면 TCP는 해당 데이터를 다시 보낼 수 있다. 타임아웃은 손실을 확정하는 신호라기보다, 확인을 기다릴 시간이 지났다는 뜻이다. 뒤쪽 바이트가 먼저 도착해 같은 ACK가 반복되는 경우도 있지만, 그 상황은 다음 페이지에서 살펴본다.

TCP는 RTT(왕복 시간) 표본 등을 바탕으로 재전송을 기다릴 시간을 조정하며, 모든 연결에 같은 고정 시간을 쓰지 않는다. Unit 6의 ping도 RTT를 측정하지만 ICMP 메시지를 이용한다. 따라서 ping 결과는 지연을 이해하는 단서이지, 특정 TCP 연결의 재전송 타이머 값과 같지는 않다. 통신 기록을 남기는 패킷 캡처 도구에서 재전송이 보여도, 기록한 위치와 지연 같은 상황을 함께 살펴야 원인을 좁힐 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 확인되지 않은 데이터는 조건에 따라 다시 전송될 수 있다.
- **적용하기 (Apply):** 캡처에서 같은 순서 번호 범위가 다시 전송됐는지 찾는다.
- **찾아보기 (Lookup):** 빠른 재전송과 타임아웃 기준은 TCP 표준·문서에서 확인한다.

## 뒤쪽 데이터가 먼저 도착하면(Out of order)

앞의 예처럼 1001~1500바이트가 아직 도착하지 않았는데 1501~2000바이트가 먼저 도착했다고 하자. 이런 도착 순서와 TCP 바이트 순서가 다른 상황을 순서가 어긋난 상태(Out of order)라고 한다. 수신 TCP는 뒤쪽 바이트를 잠시 보관할 수 있지만, 빠진 구간을 건너뛰어 애플리케이션에 전달할 수는 없다. 앞 구간이 채워져 순서가 이어진 뒤에야 연속된 데이터로 전달한다.

이때 수신 측은 여전히 1001부터 이어지는 데이터를 기다린다는 ACK를 반복해 보낼 수 있다. 같은 ACK가 반복되는 현상을 중복 ACK(Duplicate ACK)라고 하며, 빠진 구간이 있을 가능성을 보여 주는 단서다. 빠진 데이터가 도착하면 그 뒤에 먼저 받아 보관한 데이터와 이어진다. 패킷 캡처 도구의 Out of order 표시는 실제 도착 순서가 바이트 순서와 달랐다는 기록이다. 앞 구간이 채워질 때까지 뒤쪽 데이터도 애플리케이션에 전달되지 않을 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 뒤쪽 바이트가 먼저 와도 앞의 빈 구간을 건너뛰어 전달하지 않는다.
- **적용하기 (Apply):** 순서 번호와 도착 순서를 비교해 빠진 구간을 짚는다.
- **찾아보기 (Lookup):** 캡처 도구의 순서 어긋남 표시는 해당 도구의 도움말에서 확인한다.

## 받을 공간이 0이면(Zero Window)

애플리케이션이 데이터를 늦게 읽어 수신 소켓 버퍼가 가득 차면, 수신 TCP는 수신 윈도 크기가 0이라고 알릴 수 있다. 이 제로 윈도(Zero Window)는 인터넷 전체가 멈췄거나 TCP 연결이 닫혔다는 뜻이 아니라, 이 연결의 수신 측이 지금은 새 데이터를 더 받아 둘 공간이 없다는 뜻이다.

송신 측은 새 데이터를 잠시 멈추고 수신 윈도가 다시 열렸는지 확인할 수 있다. 애플리케이션이 버퍼를 비우면 수신 측은 새로 생긴 공간을 알리고 데이터 전송이 이어질 수 있다. 캡처에서 제로 윈도가 보이면 수신 프로그램이 소켓을 읽는 속도와 버퍼 상태를 살펴보자. 이것만으로 컴퓨터의 부하나 원인을 단정할 수는 없다. 제로 윈도는 Unit 7에서 본 연결 종료(FIN)와 달리 연결을 닫았다는 뜻이 아니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 제로 윈도는 해당 수신 측에 새 데이터를 받을 공간이 없다는 알림이다.
- **적용하기 (Apply):** 제로 윈도와 연결 종료를 구분한다.
- **찾아보기 (Lookup):** 윈도 확인용 탐침(Window Probe)과 유지 타이머(Persist Timer)는 TCP 문서에서 확인한다.

## 송수신 구조와 장애 원인 정리

Unit 4에서 배운 송신 버퍼에서 수신 버퍼까지의 흐름에 Unit 5의 IP 주소·Protocol, Unit 6의 왕복 지연 관찰, Unit 7의 TCP 연결과 시작 번호가 더해졌다. 이제 캡처 표식을 보면 다음처럼 질문을 좁혀 볼 수 있다.

| 캡처에서 보이는 표식 | 먼저 확인할 질문 |
| --- | --- |
| 손실 세그먼트(Lost Segment) | 어떤 바이트 범위가 아직 확인되지 않았나? |
| 재전송(Retransmission) | 같은 순서 번호 범위가 다시 전송됐나? |
| 순서가 어긋난 데이터(Out of order) | 도착 순서와 바이트 순서가 어디서 달라졌나? |
| 중복 ACK(Duplicate ACK) | 수신 측은 다음에 어떤 바이트를 기다리고 있나? |
| 제로 윈도(Zero Window) | 수신 측이 더 받을 공간이 없다고 알렸나? |

표식 하나만으로 문제가 네트워크 경로인지 애플리케이션인지 단정할 수는 없다. 다음 Lesson에서는 TCP 헤더에서 순서 번호, 확인 번호, 윈도 값이 어느 자리에 담기는지 살펴본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** ACK는 받은 바이트를 확인하고, 수신 윈도는 더 받을 공간을 알린다.
- **적용하기 (Apply):** 캡처 표식마다 다음에 확인할 질문을 고른다.
- **찾아보기 (Lookup):** TCP 헤더 필드와 혼잡 제어의 세부 사항은 다음 Lesson과 TCP 문서에서 확인한다.
