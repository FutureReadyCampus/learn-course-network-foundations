---
id: u5-l30-tcp-연결과-게임버그
title: TCP 연결과 게임버그
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-30.md
wiki_diagram: units/05-tcp-and-udp/lessons/06-tcp-연결과-게임버그/assets/diagrams/lesson-30.svg
page_metadata:
- terms:
  - 엔드포인트(endpoint)
  - 연결(connection)
  - SYN
  - ACK
  - 인증(authentication)
  animations:
  - file: l30-tcp-connection-judgment.svg
    title: 응답이 오면 '연결됨'이라 믿는다
    alt: 왼쪽 컴퓨터가 오른쪽 서버로 SYN 신호를 보내고 SYN+ACK 응답을 받자 연결됨 전구가 켜지지만, 오른쪽 상대의 얼굴은 물음표로 가려져 있는 장면입니다.
    caption: 규칙에 맞는 응답이 오면 내 컴퓨터는 연결되었다고 판단하지만, 상대의 얼굴은 여전히 가려져 있습니다.
  questions:
  - id: u8-l04-p01-q01
    kind: choice
    difficulty: easy
    prompt: TCP의 SYN과 ACK를 주고받았을 때 실제로 이루어지는 일은 무엇인가요?
    choices:
    - id: a
      text: 상대 사용자의 신원이 확인됩니다
      feedback: TCP 연결 수립은 상대 사용자 인증과 다른 절차입니다.
    - id: b
      text: 앱 사이에서 데이터를 주고받을 권한이 승인됩니다
      feedback: 연결 상태만으로 앱의 작업 권한이 승인되는 것은 아닙니다.
    - id: c
      text: 양 끝 사이에 TCP 통신 상태가 만들어집니다
      feedback: 맞아요. SYN과 ACK 교환은 TCP 양 끝의 통신 상태를 만듭니다.
    - id: d
      text: 통신 내용이 암호화되어 안전해집니다
      feedback: TCP 연결 자체가 데이터 암호화를 보장하지는 않습니다.
    - id: e
      text: 케이블이 물리적으로 연결되어 있음을 확인합니다
      feedback: TCP는 논리적인 통신 상태를 만들며 케이블 상태와는 다른 개념입니다.
    answer: c
  - id: u8-l04-p01-q02
    kind: choice
    difficulty: medium
    prompt: 전화가 연결되고 익숙한 목소리가 들린다는 사실만으로 부족한 확인은 무엇인가요?
    choices:
    - id: a
      text: 통화 상대가 실제로 기대한 사람인지 신원을 확인하는 일
      feedback: 맞아요. 연결된 사실과 상대의 신원을 확인하는 일은 다릅니다.
    - id: b
      text: 전화가 양쪽으로 소리를 전달할 수 있는지 확인하는 일
      feedback: 전화 연결은 소통 경로를 만들지만, 추가로 확인해야 할 것은 상대 신원입니다.
    - id: c
      text: 통신할 TCP 포트를 정하는 일
      feedback: 포트는 통신 끝점을 구분합니다. 비유에서 추가로 확인할 것은 상대 신원입니다.
    - id: d
      text: 데이터가 순서대로 도착하는지 확인하는 일
      feedback: 데이터 순서와 재전송은 TCP의 다른 기능이며, 상대 신원을 증명하지 않습니다.
    - id: e
      text: 앱 화면에 연결 표시가 켜져 있는지 확인하는 일
      feedback: 화면의 연결 표시는 신원 확인과 같지 않습니다.
    answer: a
  question_placements:
  - question_id: u8-l04-p01-q01
    after_paragraph: 1
  - question_id: u8-l04-p01-q02
    after_paragraph: 1
  illustration_after_paragraph: [-1, 0]
- terms:
  - 온라인 게임
  - 서버(server)와 클라이언트(client)
  - 동기화(synchronization)
  - 아이템 복제 버그
  questions:
  - id: u8-l04-p02-q01
    kind: choice
    difficulty: easy
    prompt: 온라인 게임에서 서버와 플레이어 화면의 상태는 어떻게 보일 수 있나요?
    choices:
    - id: a
      text: 모든 플레이어 화면은 언제나 서버와 정확히 동시에 바뀝니다
      feedback: 본문은 지연이나 서로 다른 시점의 표시 때문에 상태가 다를 수 있다고 설명합니다.
    - id: b
      text: 플레이어 화면만 항상 서버의 최신 상태를 결정합니다
      feedback: 게임 화면은 서버가 관리하는 상태를 받아 그립니다.
    - id: c
      text: 두 플레이어 화면은 서로 다를 수 없고 서버 상태만 바뀔 수 있습니다
      feedback: 각 화면은 서로 다른 시점의 상태를 표시할 수 있습니다.
    - id: d
      text: 한 플레이어에게 아이템이 손에 보여도 다른 화면에는 아직 바닥에 보일 수 있습니다
      feedback: 맞아요. 화면과 서버가 서로 다른 시점의 상태를 표시하면 다르게 보일 수 있습니다.
    - id: e
      text: 화면이 다르면 반드시 아이템 복제 버그가 발생한 것입니다
      feedback: 화면 불일치만으로 특정 버그나 원인을 확정할 수 없습니다.
    answer: d
  - id: u8-l04-p02-q02
    kind: choice
    difficulty: medium
    prompt: 과거 게임의 아이템 복제 일화를 읽을 때 가장 신중한 대응은 무엇인가요?
    choices:
    - id: a
      text: 일화만으로 TCP 패킷 손실이 원인이라고 확정합니다
      feedback: 본문은 세부 동작과 전송 방식이 독립적으로 확인되지 않았다고 설명합니다.
    - id: c
      text: 아이템 복제는 언제나 UDP가 만든 현상이라고 결론 내립니다
      feedback: 본문은 특정 전송 방식이 원인이라고 확인하지 않았습니다.
    - id: d
      text: 서버 화면과 플레이어 화면 중 하나는 반드시 거짓이라고 판단합니다
      feedback: 서로 다른 시점의 상태를 표시했을 수 있으므로 기록을 비교해 원인을 살펴야 합니다.
    - id: e
      text: 클라이언트 기록은 제외하고 서버 기록만 확인합니다
      feedback: 본문은 서버와 각 클라이언트의 기록을 시간 순서에 맞춰 비교하라고 설명합니다.
    - id: b
      text: 일화만으로 원인을 단정하지 않고, 서버·클라이언트 기록과 갱신 시각을 비교합니다
      feedback: 맞아요. 일화만으로 원인을 단정하지 말고 시간 순서가 있는 기록을 비교해야 합니다.
    answer: b
  question_placements:
  - question_id: u8-l04-p02-q01
    after_paragraph: 1
  - question_id: u8-l04-p02-q02
    after_paragraph: 3
  illustrations:
  - file: assets/illustrations/l30-state-mismatch.svg
    title: 플레이어 화면과 서버 상태의 차이
    alt: 철수 화면에는 아이템이 손에 있지만 서버에는 바닥에 있고, 영희 화면은 이전 상태를 보여 주는 세 칸의 개념도입니다.
    caption: 화면과 서버 상태가 어긋날 수 있음을 보여 주는 설명용 예시입니다.
    after_paragraph: 0
- terms:
  - 세션(Session)
  - SYN
  - ACK
  questions:
  - id: u8-l04-p03-q01
    kind: choice
    difficulty: easy
    prompt: 이 Lesson에서 SYN과 ACK는 각각 어떤 역할로 설명되나요?
    choices:
    - id: a
      text: SYN은 상대 앱의 신원을 증명하고 ACK는 로그인 세션을 만듭니다
      feedback: SYN과 ACK는 인증이나 앱 세션 생성이 아니라 TCP 연결과 수신 확인에 관련됩니다.
    - id: b
      text: SYN은 암호화를 시작하고 ACK는 화면을 서버 상태와 맞춥니다
      feedback: 이 두 기능은 SYN과 ACK의 역할로 설명되지 않았습니다.
    - id: c
      text: SYN은 아이템 상태를 서버에 저장하고 ACK는 클라이언트 화면을 승인합니다
      feedback: 게임 앱 상태 동기화와 TCP 신호의 역할은 서로 다릅니다.
    - id: d
      text: SYN은 데이터가 도착했음을 확인하고 ACK는 연결 시작을 요청합니다
      feedback: 역할이 반대입니다. SYN은 연결 시작 신호이고 ACK는 확인 응답입니다.
    - id: e
      text: SYN은 연결 시작을 위한 신호이고 ACK는 수신 확인을 위한 신호입니다
      feedback: 맞아요. 이 둘을 인증 성공이나 앱 작업 승인으로 해석하면 안 됩니다.
    answer: e
  - id: u8-l04-p03-q02
    kind: choice
    difficulty: medium
    prompt: TCP 연결이 만들어졌지만 사용자 신원이나 게임 화면의 최신 상태는 아직 확인되지 않았습니다. 어떻게 해석해야 하나요?
    choices:
    - id: a
      text: 연결이 만들어졌으므로 사용자는 인증되었고 화면도 서버와 일치합니다
      feedback: TCP 연결 상태만으로 인증이나 화면 동기화까지 보장하지 않습니다.
    - id: b
      text: ACK를 받았으므로 로그인 세션이 만들어졌습니다
      feedback: ACK는 수신 확인이며 애플리케이션의 로그인 세션과 다릅니다.
    - id: c
      text: TCP 연결, 신원 인증, 앱 세션, 화면 동기화는 각각 따로 확인해야 합니다
      feedback: 맞아요. TCP 연결은 이 개념들의 완료를 대신 보장하지 않습니다.
    - id: d
      text: 앱 세션이 있다면 신원 확인과 TCP 연결 상태도 항상 같은 뜻입니다
      feedback: 앱 세션과 인증, TCP 연결 상태는 서로 구분해야 합니다.
    - id: e
      text: SYN과 ACK를 다시 보내면 상대 신원과 화면 상태가 확인됩니다
      feedback: SYN과 ACK는 상대 신원이나 게임 상태를 검증하는 절차가 아닙니다.
    answer: c
  question_placements:
  - question_id: u8-l04-p03-q01
    after_paragraph: 1
  - question_id: u8-l04-p03-q02
    after_paragraph: 1
animations_dir: units/05-tcp-and-udp/lessons/06-tcp-연결과-게임버그/assets/animations
---
TCP가 연결되었다는 신호를 주고받으면 양쪽은 TCP 연결 상태에 들어간다. 하지만 그 사실만으로 상대가 우리가 기대한 사람인지, 앱의 상태가 서로 일치하는지 확인되는 것은 아니다. 이 Lesson에서는 연결 상태와 신원 확인, 앱의 동기화 문제를 나누어 본다.

## 연결됨은 상대 신원 확인이 아니다

TCP는 연결 시작 신호(SYN, Synchronize)와 확인 응답(ACK, Acknowledgement)을 주고받아 연결 상태를 만든다. 이 절차는 데이터를 주고받을 TCP 양 끝을 정하는 절차이지, 상대 사용자의 신원이나 데이터의 보안을 모두 보장하는 인증(authentication) 절차가 아니다. 전화번호로 통화가 연결되고 익숙한 목소리가 들려도 통화 상대의 신원을 별도로 확인해야 하는 것과 비슷하다. 화면의 애니메이션처럼 “연결됨” 신호가 켜져도 상대의 얼굴은 확인되지 않은 채 남을 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP 연결은 통신 상태를 나타내며 상대 신원 확인과는 다르다.
- **적용하기 (Apply):** 연결 수립 응답만으로 상대 사용자나 앱을 인증했다고 말하지 않는다.
- **찾아보기 (Lookup):** 인증과 보호 방법은 TLS 등 보안 관련 Lesson에서 확인한다.

## 읽을거리 · 게임 화면과 서버 상태가 어긋날 때

온라인 게임의 각 화면은 서버가 관리하는 상태를 받아 그린다. 네트워크가 잠시 지연되거나 서버와 클라이언트가 서로 다른 시점의 상태를 표시하면, 한 플레이어에게는 아이템이 손에 있고 다른 화면에는 아직 바닥에 있는 것처럼 보일 수 있다. 아래 그림은 이런 상태 불일치를 단순화한 예다. 이는 게임 사례의 원인이 확인되었다는 뜻이 아니라, 화면과 서버 상태가 어긋날 수 있다는 설명을 돕는 그림이다.

짧은 일시 중단 뒤 연결이 복구되더라도 서버와 화면의 상태가 자동으로 같아진다고 보장되지는 않는다. 게임은 서버의 권위 있는 상태, 클라이언트가 보낸 요청, 확인 응답과 동기화 규칙을 함께 다루어야 한다. 네트워크 연결만을 원인으로 단정하기보다 서버 기록과 각 클라이언트의 기록을 시간 순서에 맞춰 비교해야 한다.

과거 게임의 아이템 복제 문제를 다룬 일화가 있지만, 세부 동작과 전송 방식이 독립적으로 확인된 것은 아니다. 이를 검증된 장애 분석으로 받아들이기보다, 연결 상태·상대 확인·화면 동기화가 서로 다르다는 점을 보여 주는 읽을거리 예시로 보자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 클라이언트 화면은 서버 상태와 다를 수 있다.
- **적용하기 (Apply):** 화면 불일치를 곧바로 패킷 손실이나 TCP 오류 하나로 단정하지 않는다.
- **찾아보기 (Lookup):** 원인을 좁힐 때 서버와 클라이언트 로그, 상태 갱신 시각을 비교한다.

## 정리 · 연결, 응답, 신뢰를 구분하기

TCP의 연결 상태는 상대 신원을 확인하지 않고, 한 사용자의 화면이 서버의 최신 상태와 같다는 것도 보장하지 않는다. SYN은 연결 시작을 위한 신호이고, ACK는 수신 확인을 위한 신호다. 앱의 로그인 상태를 이어 관리하는 세션(Session)은 TCP 연결과 다른 개념이다. 기밀성·무결성·가용성은 Unit 14에서 다시 다룬다. 무엇을 확인했는지에 맞게 결론을 내리자.

- **기억하기 (Recall):** 연결 상태, 신원 인증, 앱 세션과 화면 동기화는 구분해야 한다.
- **적용하기 (Apply):** SYN·ACK를 인증 성공이나 앱 작업 승인으로 해석하지 않는다.
- **찾아보기 (Lookup):** 앱 세션은 애플리케이션 자료에서, 인증은 TLS와 보안 자료에서 확인한다.
