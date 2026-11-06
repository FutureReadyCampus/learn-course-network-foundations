---
id: u5-l29-tcp-연결-이라는-착각
title: 연결은 선이 아니라 장부다 — TCP '연결'이라는 착각
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-29.md
wiki_diagram: units/05-tcp-and-udp/lessons/05-tcp-연결-이라는-착각/assets/diagrams/lesson-29.svg
page_metadata:
- terms:
  - LAN 케이블
  - TCP 연결
  - 물리 계층(L1)
  - 전송 계층(L4)
  - 소켓(Socket)
  animations:
  - file: l29-physical-vs-logical.svg
    title: 선이 끊겨도 연결 기록은 남는다
    alt: 두 컴퓨터 사이에 아래쪽 케이블과 위쪽 점선 약속선이 그려져 있고, 케이블이 끊겨도 점선은 유지되는 장면입니다.
    caption: 1층 선이 끊겨도 4층의 연결 장부는 그대로 남아 있습니다.
  questions:
  - id: u8-l03-p01-q01
    kind: choice
    difficulty: easy
    prompt: 케이블이 잠깐 끊겼을 때 TCP 연결 정보는 어떻게 될 수 있나요?
    choices:
    - id: a
      text: 케이블이 끊어지는 순간 양쪽 운영체제가 모든 연결 정보를 지웁니다
      feedback: 본문은 TCP 정보가 케이블 단절과 동시에 반드시 지워지는 것은 아니라고 설명합니다.
    - id: b
      text: 컴퓨터의 IP 주소가 자동으로 다른 주소로 바뀝니다
      feedback: 이 문항은 IP 주소 변경이 아니라 물리 링크와 TCP 연결 정보를 구분합니다.
    - id: c
      text: 케이블이 잠깐 끊겨도 양쪽 운영체제의 TCP 연결 정보가 바로 지워지지 않을 수 있습니다
      feedback: 맞아요. TCP는 양 끝에서 연결 정보를 관리하므로 물리 선이 잠깐 끊겨도 상태가 즉시 없어지지 않을 수 있습니다.
    - id: d
      text: 케이블이 끊기면 상대 프로그램이 정상 동작하는지 확인할 수 있습니다
      feedback: 케이블 상태만으로 앱의 동작을 알 수는 없습니다. 링크, TCP 상태, 앱 응답은 구분해야 합니다.
    - id: e
      text: TCP 연결 정보는 케이블 안에 저장되어 있어 끊기면 함께 사라집니다
      feedback: TCP 연결은 케이블 자체가 아니라 양 끝 운영체제가 관리하는 논리 상태입니다.
    answer: c
  - id: u8-l03-p01-q02
    kind: choice
    difficulty: medium
    prompt: 네트워크 장치에서 링크가 끊겼다고 표시되지만 운영체제에는 TCP 연결 상태가 남아 있습니다. 이 둘을 어떻게 이해해야 하나요?
    choices:
    - id: a
      text: 물리 링크 상태와 TCP 연결 상태는 서로 다를 수 있으므로 각각 확인합니다
      feedback: 맞아요. 링크는 물리 연결을, TCP 상태는 양 끝 운영체제가 관리하는 논리 연결을 나타냅니다.
    - id: b
      text: TCP 상태가 남아 있으므로 케이블도 실제로는 연결된 상태입니다
      feedback: 논리 상태가 남아 있어도 물리 링크가 끊길 수 있습니다. 두 상태를 같은 것으로 보면 안 됩니다.
    - id: c
      text: 링크가 끊겼다면 운영체제의 TCP 상태 표시는 반드시 오류입니다
      feedback: 두 상태가 다를 수 있으므로 한쪽 표시만으로 다른 쪽이 오류라고 단정할 수 없습니다.
    - id: d
      text: TCP 연결은 케이블이 끊긴 순간 반드시 정상 종료 절차를 마칩니다
      feedback: 본문은 케이블 단절과 TCP 연결 종료를 같은 사건으로 보지 말라고 설명합니다.
    - id: e
      text: 링크 상태와 TCP 연결 상태는 같은 장치에서만 확인할 수 있습니다
      feedback: 링크는 네트워크 장치에서, TCP 소켓 상태는 운영체제 도구에서 확인할 수 있습니다.
    answer: a
  question_placements:
  - question_id: u8-l03-p01-q01
    after_paragraph: 1
  - question_id: u8-l03-p01-q02
    after_paragraph: 1
- terms:
  - Heartbeat(하트비트)
  questions:
  - id: u8-l03-p02-q01
    kind: choice
    difficulty: easy
    prompt: 운영체제에 TCP 연결 상태가 남아 있다는 사실만으로 무엇을 알 수 있나요?
    choices:
    - id: a
      text: 상대 앱이 모든 요청을 정상 처리하고 있습니다
      feedback: TCP 연결 상태만으로 앱이 요청을 처리하는지 알 수는 없습니다.
    - id: b
      text: 상대 프로그램이 반드시 실행 중이며 멈추지 않았습니다
      feedback: 프로그램이 멈췄거나 응답이 늦어도 TCP 연결 정보가 남아 있을 수 있습니다.
    - id: c
      text: 서비스 내부 세션도 아직 유효합니다
      feedback: 서비스의 세션 상태와 TCP 연결 상태는 서로 다를 수 있습니다.
    - id: d
      text: 상대 앱이 지금 정상적으로 응답한다는 보장은 없습니다
      feedback: 맞아요. TCP 상태가 남아 있어도 앱은 멈췄거나 응답을 늦게 할 수 있습니다.
    - id: e
      text: 네트워크에 데이터 손실이 전혀 없습니다
      feedback: 연결 상태만으로 데이터 손실 여부를 판단할 수는 없습니다. 앱 응답도 따로 살펴야 합니다.
    answer: d
  - id: u8-l03-p02-q02
    kind: choice
    difficulty: medium
    prompt: 앱이 일정한 신호와 응답을 주고받아 상대 앱이 살아 있는지 살핍니다. 이 방법을 TCP 연결 수립과 구분하면 무엇인가요?
    choices:
    - id: a
      text: TCP의 3-way handshake로, 앱이 주기적으로 보내는 생존 확인입니다
      feedback: 연결 수립 과정과 앱의 주기적인 상태 확인은 다른 일입니다.
    - id: b
      text: Heartbeat로, 앱 수준에서 상대의 응답 여부를 살피는 방법입니다
      feedback: 맞아요. Heartbeat는 앱 수준의 확인이며 TCP 연결을 맺는 절차와 다릅니다.
    - id: c
      text: RTO로, 앱이 상대의 작업 결과를 정기적으로 요청하는 방법입니다
      feedback: RTO는 TCP 재전송 타임아웃과 관련된 시간 기준이지 앱의 생존 신호가 아닙니다.
    - id: d
      text: 케이블 검사로, 상대 앱의 처리 상태를 직접 알려 주는 방법입니다
      feedback: 물리 링크 검사는 앱이 살아 있는지 직접 알려 주지 않습니다.
    - id: e
      text: TCP keepalive와 같은 설정으로, 두 기능은 항상 같은 목적과 동작을 합니다
      feedback: 본문은 앱의 Heartbeat와 TCP keepalive의 목적과 동작을 구분하라고 설명합니다.
    answer: b
  question_placements:
  - question_id: u8-l03-p02-q01
    after_paragraph: 1
  - question_id: u8-l03-p02-q02
    after_paragraph: 2
- terms:
  - ACK
  - RTT
  - RTO
  - SRTT
  animations:
  - file: l29-rto-doubling.svg
    title: 확인이 없으면 기다림을 조절한다
    alt: 패킷이 중간에서 사라져 ACK가 오지 않고, 시간 간격을 두고 다시 보내는 흐름을 보여 주는 개념 예시입니다.
    caption: 확인이 없으면 다시 보내고, 다음 재시도까지 기다리는 시간을 늘릴 수 있습니다.
  questions:
  - id: u8-l03-p03-q01
    kind: choice
    difficulty: easy
    prompt: TCP가 보낸 데이터에 대한 ACK를 받지 못하고 재전송 타이머가 만료되면 무엇을 할 수 있나요?
    choices:
    - id: a
      text: 연결의 모든 상태를 즉시 지우고 다시 연결을 시작합니다
      feedback: 타임아웃은 재전송을 판단하는 기준입니다. 연결 정보를 항상 즉시 지운다는 뜻은 아닙니다.
    - id: b
      text: 상대 앱이 데이터를 읽었다고 간주하고 다음 데이터만 보냅니다
      feedback: ACK가 오지 않았으므로 상대가 데이터를 받았다고 단정할 수 없습니다.
    - id: c
      text: 해당 데이터가 더는 필요 없다고 보고 반드시 버립니다
      feedback: 본문은 타임아웃 뒤 데이터를 다시 보낼 수 있다고 설명합니다.
    - id: d
      text: 상대 앱의 Heartbeat를 자동으로 대신 보냅니다
      feedback: Heartbeat는 앱 수준의 상태 확인입니다. TCP 재전송 타이머와 다른 기능입니다.
    - id: e
      text: 데이터를 다시 보낼 수 있습니다
      feedback: 맞아요. ACK가 오지 않아 타이머가 만료되면 TCP는 재전송할 수 있습니다.
    answer: e
  - id: u8-l03-p03-q02
    kind: choice
    difficulty: medium
    prompt: ACK가 계속 오지 않아 재시도가 이어질 때, TCP의 대기 시간은 어떻게 이해해야 하나요?
    choices:
    - id: a
      text: 모든 운영체제와 연결에서 늘 같은 초 단위 값입니다
      feedback: 본문은 타임아웃이 고정된 하나의 초 단위 숫자가 아니라고 강조합니다.
    - id: b
      text: 한 번 타임아웃이 나면 이후에는 재전송을 하지 않습니다
      feedback: 타임아웃 뒤 데이터를 다시 보낼 수 있고, 확인이 계속 오지 않으면 기다림을 조절할 수 있습니다.
    - id: c
      text: RTT 측정과 계산 규칙을 바탕으로 정하고, 재시도 때 간격을 늘릴 수 있습니다
      feedback: 맞아요. 대기 시간은 RTT와 계산 규칙에 따라 달라지며 확인이 없으면 다음 재시도까지의 간격을 늘릴 수 있습니다.
    - id: d
      text: 상대 앱이 요청을 처리하는 데 걸리는 시간만으로 정합니다
      feedback: 대기 시간은 앱 처리 시간 하나로 정해지지 않습니다. TCP의 RTT 측정과 계산 규칙을 바탕으로 합니다.
    - id: e
      text: 네트워크 케이블 길이만 보고 미리 고정합니다
      feedback: 케이블 길이 하나로 고정되는 값이 아닙니다. 연결과 구현 조건에 따라 달라질 수 있습니다.
    answer: c
  question_placements:
  - question_id: u8-l03-p03-q01
    after_paragraph: 1
  - question_id: u8-l03-p03-q02
    after_paragraph: 2
- terms:
  - 버퍼(Buffer)
  - 애플리케이션 상태
  animations:
  - file: l29-buffer-cushion.svg
    title: 버퍼가 끊김을 가려 준다
    alt: 물탱크 모양의 버퍼에 저장된 데이터가 네트워크의 짧은 중단 동안 재생을 이어 주는 장면입니다.
    caption: 재생 버퍼는 짧은 네트워크 중단 동안 이미 받은 데이터를 사용합니다.
  questions:
  - id: u8-l03-p04-q01
    kind: choice
    difficulty: easy
    prompt: 파일을 받는 중 네트워크를 잠시 끊었다 복구하면 결과는 어떻게 될 수 있나요?
    choices:
    - id: a
      text: 전송이 잠시 멈췄다가 이어질 수도 있고, 앱에서 오류가 날 수도 있습니다
      feedback: 맞아요. 결과는 끊긴 시간과 재전송, 버퍼, 앱 정책 등에 따라 달라질 수 있습니다.
    - id: b
      text: TCP가 어떤 상황에서도 반드시 파일 전송을 이어 줍니다
      feedback: TCP가 항상 전송을 이어 준다고 보장할 수 없습니다. 환경과 타임아웃, 앱 정책이 영향을 줍니다.
    - id: c
      text: 케이블을 다시 연결하면 앱 상태와 관계없이 파일이 처음부터 다시 시작됩니다
      feedback: 본문은 환경에 따라 전송이 이어질 수도, 앱에서 오류가 날 수도 있다고 설명합니다.
    - id: d
      text: 운영체제가 항상 앱의 오류를 숨기고 다운로드를 완료합니다
      feedback: 앱에서 오류가 날 수도 있으며, 결과는 앱과 네트워크 조건에 따라 달라집니다.
    - id: e
      text: 네트워크 대역폭(속도)이 충분히 빠르면 단절 시간과 무관하게 무조건 전송이 이어집니다
      feedback: 속도가 빨라도 단절 시간이나 TCP 타임아웃, 앱 정책에 따라 오류가 발생할 수 있습니다.
    answer: a
  - id: u8-l03-p04-q02
    kind: choice
    difficulty: medium
    prompt: 영상의 재생 버퍼와 TCP 수신 버퍼를 구분한 설명은 무엇인가요?
    choices:
    - id: a
      text: 둘 다 네트워크 장비 안에만 있는 같은 공간입니다
      feedback: 재생 버퍼는 앱이 이미 받은 데이터를 저장하는 공간이며 TCP 수신 버퍼와 구분됩니다.
    - id: b
      text: 재생 버퍼는 케이블이 끊겨도 새 데이터를 계속 만들어 냅니다
      feedback: 버퍼는 이미 받은 데이터를 잠시 사용합니다. 새 데이터를 만들어 내지는 않습니다.
    - id: c
      text: 재생 버퍼는 TCP의 Window 그 자체이며 항상 같은 크기로 움직입니다
      feedback: 본문은 재생 버퍼가 TCP 수신 버퍼나 Window와 같은 공간이 아니라고 설명합니다.
    - id: d
      text: 재생 버퍼는 이미 받은 데이터를 잠시 저장해 짧은 지연 동안 화면이나 소리를 이어 줍니다
      feedback: 맞아요. 재생 버퍼는 앱이 이미 받은 데이터를 사용해 짧은 지연 동안 재생을 이어 줄 수 있습니다.
    - id: e
      text: 재생 버퍼가 가득 차면 상대 앱이 응답 중이라는 뜻입니다
      feedback: 버퍼에 데이터가 있다는 사실로 상대 앱의 현재 응답 상태를 알 수는 없습니다.
    answer: d
  question_placements:
  - question_id: u8-l03-p04-q01
    after_paragraph: 1
  - question_id: u8-l03-p04-q02
    after_paragraph: 2
- terms: []
  questions:
  - id: u8-l03-p05-q01
    kind: choice
    difficulty: easy
    prompt: 이 Lesson에서 구분해 살펴보자고 한 세 가지 상태는 무엇인가요?
    choices:
    - id: a
      text: 장치 IP 주소, 통신 포트 번호, 저장된 파일 이름
      feedback: 이 항목들은 데이터나 프로그램을 식별할 때 쓰이며, Lesson의 세 가지 상태가 아닙니다.
    - id: b
      text: 물리 링크, TCP 연결 상태, 애플리케이션의 응답 상태
      feedback: 맞아요. 선의 연결, TCP의 논리 상태, 앱의 응답 여부는 서로 다릅니다.
    - id: c
      text: ACK, RTO, SRTT
      feedback: 이 용어들은 재전송과 시간 계산에 관련됩니다. 정리 페이지가 구분하는 세 상태는 아닙니다.
    - id: d
      text: 요청 클라이언트, 처리 서버, 중계 라우터
      feedback: 네트워크 역할 이름이지, 이 Lesson에서 구분하는 세 가지 상태는 아닙니다.
    - id: e
      text: 케이블, 스위치, 포트 번호
      feedback: 연결과 장비에 관련된 말이지만 TCP 상태와 앱 응답 상태를 포함하지 않습니다.
    answer: b
  - id: u8-l03-p05-q02
    kind: choice
    difficulty: medium
    prompt: 케이블을 다시 연결한 뒤 다운로드가 이어졌습니다. 이 결과를 가장 바르게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 이어졌다는 사실은 상대 앱이 중단 내내 정상 처리했다는 뜻입니다
      feedback: 연결 상태와 앱 응답 상태는 다릅니다. 다운로드 결과만으로 앱이 내내 정상 처리했다고 단정할 수 없습니다.
    - id: b
      text: 케이블이 돌아왔으므로 TCP의 재전송과 타임아웃은 관여하지 않았습니다
      feedback: 전송이 이어질지는 TCP의 타임아웃과 재전송에도 달려 있습니다.
    - id: c
      text: TCP 연결은 물리 선과 같은 것이므로 케이블이 복구되면 상태가 자동으로 완전히 초기화됩니다
      feedback: TCP 연결은 선이 아니라 양 끝이 관리하는 논리 상태입니다.
    - id: d
      text: 재생 버퍼와 TCP 수신 Window는 같은 공간이므로 앱의 버퍼만 확인하면 됩니다
      feedback: 재생 버퍼와 TCP 수신 버퍼·Window는 구분해야 합니다. 상황에 따라 관련 로그를 함께 살펴야 합니다.
    - id: e
      text: 링크 복구만으로 결과를 단정할 수 없으며 TCP의 타임아웃·재전송과 버퍼, 앱 상태를 함께 살펴야 합니다
      feedback: 맞아요. 케이블 복구는 전체 결과의 한 부분입니다. TCP 동작과 버퍼, 앱 정책과 상태도 영향을 줍니다.
    answer: e
  question_placements:
  - question_id: u8-l03-p05-q01
    after_paragraph: 1
  - question_id: u8-l03-p05-q02
    after_paragraph: 1
animations_dir: units/05-tcp-and-udp/lessons/05-tcp-연결-이라는-착각/assets/animations
---
Unit 7 Lesson 2에서는 “이미 있는 네트워크 위에서 양쪽이 연결 상태를 관리한다”고 배웠다. 그 Lesson의 비유대로 TCP 연결은 선 자체가 아니라 양 끝이 기록한 장부, 즉 논리 상태다. 이 Lesson에서 말하는 ‘착각’은 연결이 존재한다는 사실이 아니다. 연결됨을 “케이블이 이어져 있고 상대 앱도 지금 응답한다”와 같은 뜻으로 여기는 오해다.

## 물리 연결(L1)과 논리 연결(L4) · 선과 장부

TCP 연결을 시작하면 양쪽 운영체제는 상대 주소와 포트, 순서 번호 같은 통신 정보를 관리한다. 이 기록은 물리적인 케이블 그 자체가 아니다. 아래 애니메이션의 1층 선과 4층 장부처럼, 선이 잠깐 끊겨도 양 끝의 TCP가 즉시 모든 연결 정보를 지우는 것은 아니다. 그래서 물리 링크 상태와 TCP 연결 상태는 서로 다를 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP 연결은 양 끝이 관리하는 논리 상태다.
- **적용하기 (Apply):** 케이블 단절과 TCP 연결 종료를 같은 사건으로 보지 않는다.
- **찾아보기 (Lookup):** 링크 상태와 소켓 상태는 각기 네트워크 장치와 운영체제 도구에서 확인한다.

## 연결 상태와 앱의 응답은 또 다르다

TCP 상태가 남아 있다고 상대 프로그램이 정상적으로 작업하고 있다는 뜻은 아니다. 상대 앱이 멈췄거나, 요청을 처리하는 데 오래 걸리거나, 서비스 내부의 세션이 끝났을 수도 있다. 따라서 “연결되어 있음”과 “앱이 지금 응답함”도 나눠 보아야 한다.

앱이 일정한 신호와 응답을 주고받아 상대가 살아 있는지 살피는 방법을 Heartbeat(하트비트)라고 한다. 이는 TCP 연결 수립과는 다른 앱 수준의 확인 방법이다. 신호에 응답이 없다는 사실만으로 원인을 하나로 단정할 수는 없다. 앱의 상태 확인과 TCP keepalive의 동작도 같지 않으므로 설정과 목적을 구분한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP 연결 상태와 애플리케이션의 응답 상태는 다르다.
- **적용하기 (Apply):** 연결이 남아 있어도 앱이 응답하지 않을 수 있음을 고려한다.
- **찾아보기 (Lookup):** Heartbeat와 TCP keepalive의 차이는 운영체제와 서비스 문서에서 확인한다.

## 재전송 타이머와 타임아웃

송신한 데이터에 대한 확인 응답(ACK, Acknowledgement)이 오지 않으면 TCP는 재전송 여부를 판단한다. 이때 쓰는 시간 기준을 재전송 타임아웃(RTO, Retransmission Timeout)이라고 한다. 이를 위해 재전송 타이머를 두고, 타이머가 만료된 상황을 타임아웃이라고 부른다. 타임아웃이 발생하면 데이터를 다시 보낼 수 있다. 대기 시간은 왕초보가 외울 하나의 고정된 초 단위 숫자가 아니다. 왕복 시간(RTT, Round-Trip Time)의 측정과 프로토콜의 계산 규칙을 바탕으로 정하며, 확인이 계속 오지 않으면 다음 재시도까지의 간격을 늘릴 수 있다.

애니메이션의 간격 표시는 이런 증가를 보여 주는 개념 예시다. 실제 간격은 연결과 구현 조건에 따라 달라진다. 이 Lesson에서는 정확한 초 수나 RFC·SRTT·RTO의 계산식을 외우기보다, “확인이 없으면 타임아웃 뒤 다시 보내고 기다림을 조절한다”는 흐름을 잡는다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** ACK가 오지 않으면 재전송 타이머가 만료된 뒤 다시 보낼 수 있다.
- **적용하기 (Apply):** 타임아웃 값은 고정 상수가 아니므로 숫자 하나만으로 동작을 설명하지 않는다.
- **찾아보기 (Lookup):** RTO 계산과 재시도 제한은 TCP 표준 및 운영체제 자료에서 확인한다.

## 케이블 단절을 관찰하는 실험

파일을 내려받는 동안 네트워크를 잠시 끊었다가 복구하면, 전송이 일시 정지한 뒤 이어질 수도 있고 앱에서 오류가 날 수도 있다. 결과는 끊긴 시간, 재전송과 타임아웃, 버퍼, 서버와 클라이언트 앱의 정책에 따라 달라진다. 같은 실험에서도 운영체제와 네트워크 환경이 다르면 결과가 같지 않을 수 있다.

재생 버퍼(Buffer)는 이미 받은 데이터를 잠시 저장해 화면이나 소리를 이어 주는 앱의 공간이다. 예를 들어 몇 초 분량을 미리 받아 두면 짧은 네트워크 지연 동안 재생을 계속할 수 있지만, 이는 TCP 수신 버퍼나 Window와 같은 공간을 뜻하지 않는다. 재생 버퍼가 비면 사용자는 멈춤을 볼 수 있고, 데이터 전송이 복구되면 다시 채워질 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 물리 링크, TCP 연결 상태, 앱의 처리 상태는 서로 다르다.
- **적용하기 (Apply):** 짧은 단절 뒤 이어진 전송을 TCP가 모든 상황에서 보장한다고 확대하지 않는다.
- **찾아보기 (Lookup):** 실험 로그와 패킷 캡처, 앱의 timeout 기록을 함께 비교한다.

## 정리 · 연결됨과 통함은 다르다

TCP 연결은 물리 선이 아니라 양 끝이 관리하는 논리 상태다. 물리 연결이 돌아와도 전송이 이어질지는 타임아웃과 재전송 등 TCP 동작에 달려 있고, 연결 상태가 남아 있어도 상대 앱이 응답한다는 보장은 없다. 선, TCP 상태, 앱 응답이라는 세 가지를 따로 확인하자.

- **기억하기 (Recall):** 선(L1)·TCP 연결 상태(L4)·앱 응답은 서로 다른 상태다.
- **적용하기 (Apply):** 케이블 단절 뒤 전송이 멈추거나 이어지는 이유를 세 층으로 나누어 설명한다.
- **찾아보기 (Lookup):** RTT, RTO, SRTT, OS별 재시도 동작은 표준과 구현 자료에서 찾아본다.
