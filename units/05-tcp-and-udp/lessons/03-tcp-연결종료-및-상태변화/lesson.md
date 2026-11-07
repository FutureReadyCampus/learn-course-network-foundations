---
id: u5-l27-tcp-연결종료-및-상태변화
title: TCP 연결종료 및 상태변화
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-27.md
wiki_diagram: units/05-tcp-and-udp/lessons/03-tcp-연결종료-및-상태변화/assets/diagrams/lesson-27.svg
page_metadata:
- terms:
  - FIN
  - ACK
  - 반쪽 닫기(half-close)
  illustrations:
  - file: assets/animations/l27-daily-one-side-done.svg
    title: "말을 마쳐도 상대는 남았을 수 있어요"
    alt: "두 사람이 이야기를 주고받습니다. 내가 “저는 할 말 다 했어요” 하고 알려 한 방향이 막히지만, 상대는 “아직 할 말이 남았어요” 하며 계속 말합니다. 한쪽 방향만 먼저 닫을 수 있다고 표시됩니다."
    caption: "한 사람이 말을 마쳐도 상대는 계속 말할 수 있습니다. FIN으로 한쪽 방향만 닫는 것과 같습니다."
    after_paragraph: -1
  - file: assets/animations/l27-fin-half-close.svg
    title: "FIN은 한 방향의 송신 끝"
    alt: "클라이언트와 서버가 양방향으로 데이터를 주고받습니다. 클라이언트가 FIN을 보내 자기 방향의 송신이 끝났다고 알려도 서버는 아직 보낼 데이터가 있으면 계속 보낼 수 있으며, 이렇게 한쪽 방향만 먼저 닫는 것을 half-close라고 합니다."
    caption: "FIN은 한 방향의 송신이 끝났음을 알립니다. 반대 방향은 계속 보낼 수 있습니다."
    after_paragraph: 3

  questions:
  - id: u7-l03-p01-q01
    kind: choice
    difficulty: easy
    prompt: "TCP 연결에서 데이터는 보통 어느 방향으로 오갈 수 있나요?"
    choices:
    - id: a
      text: "양쪽 방향"
      feedback: "TCP 연결은 양쪽 방향으로 데이터를 주고받을 수 있습니다."
    - id: b
      text: "한쪽 방향으로만"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "서버에서 클라이언트로만"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "클라이언트에서 서버로만"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "연결을 시작할 때만"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: a
  - id: u7-l03-p01-q02
    kind: choice
    difficulty: easy
    prompt: "전화에서 한 사람이 말을 마쳐도 상대에게 남아 있을 수 있는 것은 무엇인가요?"
    choices:
    - id: a
      text: "새 전화번호"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "답할 말"
      feedback: "한쪽이 말을 마쳐도 상대가 답할 일이 남아 있을 수 있습니다."
    - id: c
      text: "네트워크 주소"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "연결 암호"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "다른 통화"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: b
  - id: u7-l03-p01-q03
    kind: choice
    difficulty: easy
    prompt: "능동 종료 측은 무엇으로 정해지나요?"
    choices:
    - id: a
      text: "항상 클라이언트"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "항상 서버"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "먼저 FIN을 보내는 쪽"
      feedback: "능동 종료는 먼저 FIN을 보낸 쪽을 가리킵니다."
    - id: d
      text: "IP 주소가 더 작은 쪽"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "먼저 연결된 쪽"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: c
  - id: u7-l03-p01-q04
    kind: choice
    difficulty: easy
    prompt: "상대가 FIN을 보낸 뒤에도 내 쪽에서 보낼 데이터가 남았다면 어떻게 되나요?"
    choices:
    - id: a
      text: "연결이 즉시 완전히 끊긴다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "데이터가 자동으로 삭제된다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "상대가 보낸 FIN이 취소된다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "반대 방향으로 계속 보낼 수 있다"
      feedback: "FIN은 한 방향의 송신 종료를 알리므로 반대 방향은 계속 열려 있을 수 있습니다."
    - id: e
      text: "TCP가 새 연결을 만든다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: d
  question_placements:
  - question_id: u7-l03-p01-q01
    after_paragraph: 1
  - question_id: u7-l03-p01-q02
    after_paragraph: 2
  - question_id: u7-l03-p01-q03
    after_paragraph: 3
  - question_id: u7-l03-p01-q04
    after_paragraph: 4
- terms:
  - 4-way handshake
  - FIN_WAIT_1
  - FIN_WAIT_2
  illustrations:
  - file: assets/animations/l27-daily-hangup-two-pairs.svg
    title: "끊을 때도 두 쌍의 인사"
    alt: "나와 상대가 네 번 인사를 주고받습니다. 내가 “저는 다 했어요”, 상대가 “알겠어요”, 상대가 “저도 이제 끝났어요”, 내가 “알겠어요” 하고 말하며 각자 끝났다고 말하고 상대가 알겠다고 답하는 두 쌍이 됩니다."
    caption: "각자 끝났다고 말하고 상대가 알겠다고 답하는 두 쌍, 모두 네 번의 인사입니다."
    after_paragraph: -1
  - file: assets/animations/l27-tcp-four-way-close.svg
    title: "연결을 끝내는 네 번의 메시지"
    alt: "클라이언트가 FIN 1000을 보내고 서버가 ACK 1001로 답하는 첫 쌍, 서버가 FIN 5000을 보내고 클라이언트가 ACK 5001로 답하는 둘째 쌍이 차례로 오가며 두 쌍, 네 번의 메시지가 됩니다. 두 컴퓨터의 상태 이름도 단계마다 바뀝니다."
    caption: "FIN과 ACK가 이쪽에서 한 쌍, 저쪽에서 한 쌍 오가 네 번의 메시지가 됩니다."
    after_paragraph: 3

  questions:
  - id: u7-l03-p02-q01
    kind: choice
    difficulty: easy
    prompt: "먼저 FIN을 보낸 뒤 처음 들어가는 상태는 무엇인가요?"
    choices:
    - id: a
      text: "FIN_WAIT_2"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "CLOSE_WAIT"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "LAST_ACK"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "TIME_WAIT"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "FIN_WAIT_1"
      feedback: "FIN을 보낸 쪽은 먼저 FIN_WAIT_1에서 확인을 기다립니다."
    answer: e
  - id: u7-l03-p02-q02
    kind: choice
    difficulty: easy
    prompt: "FIN을 보낸 쪽은 상대의 ACK를 받은 뒤 어떤 상태에서 상대 FIN을 기다리나요?"
    choices:
    - id: a
      text: "FIN_WAIT_2"
      feedback: "ACK를 받으면 FIN_WAIT_2에서 상대가 자기 FIN을 보낼 때까지 기다립니다."
    - id: b
      text: "FIN_WAIT_1"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "CLOSE_WAIT"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "LISTEN"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "CLOSED"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: a
  - id: u7-l03-p02-q03
    kind: choice
    difficulty: easy
    prompt: "클라이언트가 FIN을 보낸 뒤에도 서버에 응답이 남아 있으면 서버는 무엇을 할 수 있나요?"
    choices:
    - id: a
      text: "즉시 전원을 끈다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "응답 데이터를 더 보낼 수 있다"
      feedback: "한쪽 FIN 뒤에도 반대 방향의 송신은 계속될 수 있습니다."
    - id: c
      text: "클라이언트의 FIN을 지운다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "새 IP 주소를 만든다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "반드시 연결을 다시 시작한다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: b
  - id: u7-l03-p02-q04
    kind: choice
    difficulty: easy
    prompt: "종료 애니메이션에 적힌 숫자는 이 Lesson에서 어떤 역할을 하나요?"
    choices:
    - id: a
      text: "모든 TCP 연결에서 정해진 고정 번호입니다."
      feedback: "숫자는 예시이며 실제 연결마다 달라질 수 있습니다."
    - id: b
      text: "패킷 크기를 정합니다."
      feedback: "여기서는 크기가 아니라 메시지 흐름을 보여 줍니다."
    - id: c
      text: "동작을 설명하기 위한 예시입니다."
      feedback: "숫자는 동작 설명용 예시이며, 순서번호 계산은 이 페이지의 목표가 아닙니다."
    - id: d
      text: "서버의 포트 번호를 뜻합니다."
      feedback: "숫자는 포트 번호가 아니라 설명용 순서번호 예시입니다."
    - id: e
      text: "먼저 닫는 쪽을 정합니다."
      feedback: "먼저 닫는 쪽은 누가 먼저 FIN을 보내는지로 정해집니다."
    answer: c
  question_placements:
  - question_id: u7-l03-p02-q01
    after_paragraph: 1
  - question_id: u7-l03-p02-q02
    after_paragraph: 2
  - question_id: u7-l03-p02-q03
    after_paragraph: 3
  - question_id: u7-l03-p02-q04
    after_paragraph: 4
- terms:
  - CLOSE_WAIT
  - LAST_ACK
  illustrations:
  - file: assets/animations/l27-daily-still-tidying.svg
    title: "끝났다는 말을 듣고도 정리가 남아요"
    alt: "상대가 “저는 끝났어요” 하고 알리면 나는 “알겠어요” 하고 답하지만 아직 남은 이야기와 정리가 있습니다. 정리를 마치면 “저도 끝났어요” 하고 알리고, 상대가 확인해 주면 통화가 끝납니다."
    caption: "상대의 말을 들은 뒤에도 내 쪽 정리가 남아 있을 수 있습니다."
    after_paragraph: -1
  - file: assets/animations/l27-close-wait-tidy.svg
    title: "CLOSE_WAIT는 정리 중인 상태"
    alt: "서버가 클라이언트의 FIN을 ACK로 확인하고 CLOSE_WAIT가 됩니다. 서버 프로그램이 남은 응답과 정리를 마치고 소켓을 닫으면 서버도 FIN을 보내 LAST_ACK가 되고, 마지막 ACK가 오면 종료 절차가 끝납니다."
    caption: "CLOSE_WAIT는 상대 FIN을 확인했지만 내 쪽 정리는 끝나지 않은 상태입니다. 오래 남을 때는 소켓을 닫았는지 로그와 함께 확인합니다."
    after_paragraph: 1

  questions:
  - id: u7-l03-p03-q01
    kind: choice
    difficulty: easy
    prompt: "상대의 FIN을 받은 쪽은 먼저 무엇을 보내 확인하나요?"
    choices:
    - id: a
      text: "SYN"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "새 FIN 두 개"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "RST만"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "ACK"
      feedback: "상대 FIN을 받으면 ACK로 확인합니다."
    - id: e
      text: "DNS 요청"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: d
  - id: u7-l03-p03-q02
    kind: choice
    difficulty: easy
    prompt: "상대 FIN을 ACK한 뒤, 내 프로그램의 송신이 아직 끝나지 않은 상태는 무엇인가요?"
    choices:
    - id: a
      text: "FIN_WAIT_1"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "FIN_WAIT_2"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "TIME_WAIT"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "LISTEN"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "CLOSE_WAIT"
      feedback: "CLOSE_WAIT는 상대 FIN은 확인했지만 내 쪽 정리는 남은 상태입니다."
    answer: e
  - id: u7-l03-p03-q03
    kind: choice
    difficulty: easy
    prompt: "내 프로그램이 남은 일을 마치고 소켓을 닫으면 이쪽은 무엇을 보내나요?"
    choices:
    - id: a
      text: "FIN"
      feedback: "남은 처리가 끝나면 자기 방향의 종료를 알리는 FIN을 보냅니다."
    - id: b
      text: "SYN"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "DNS 응답"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "새 IP 주소"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "MTU"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: a
  question_placements:
  - question_id: u7-l03-p03-q01
    after_paragraph: 1
  - question_id: u7-l03-p03-q02
    after_paragraph: 2
  - question_id: u7-l03-p03-q03
    after_paragraph: 3
- terms:
  - TIME_WAIT
  - MSL
  - 2MSL
  - 소켓(socket)
  illustrations:
  - file: assets/animations/l27-daily-hold-the-phone.svg
    title: "끊은 뒤에도 잠깐 수화기를 들고 있어요"
    alt: "내가 마지막으로 보낸 “네”가 도중에 사라지자 상대가 “끝났어요”를 다시 말하고, 아직 수화기를 들고 있던 내가 다시 “네” 하고 답합니다. 마지막에는 이전 통화의 늦은 말이 같은 번호의 새 통화에 섞이지 않게 막는다고 표시됩니다."
    caption: "먼저 끊은 쪽이 잠깐 더 기다리면 마지막 확인이 사라져도 다시 답할 수 있고, 이전 통화의 늦은 말이 섞이지 않습니다."
    after_paragraph: -1
  - file: assets/animations/l27-time-wait-reasons.svg
    title: "TIME_WAIT가 남는 두 가지 이유"
    alt: "클라이언트가 보낸 마지막 ACK가 사라지면 서버가 FIN을 다시 보내고, TIME_WAIT 상태의 클라이언트가 ACK를 한 번 더 보냅니다. 또한 이전 연결의 늦은 세그먼트가 같은 IP와 포트를 쓰는 새 연결에 섞이지 않게 막습니다."
    caption: "TIME_WAIT는 마지막 ACK가 사라졌을 때 다시 응답하고 이전 연결의 늦은 세그먼트가 새 연결에 섞이지 않게 합니다. 대기 시간은 운영체제 구현에 따라 다릅니다."
    after_paragraph: 1

  questions:
  - id: u7-l03-p04-q01
    kind: choice
    difficulty: easy
    prompt: "보통 마지막 ACK를 보낸 뒤 먼저 FIN을 보낸 쪽이 들어가는 상태는 무엇인가요?"
    choices:
    - id: a
      text: "CLOSE_WAIT"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "TIME_WAIT"
      feedback: "먼저 FIN을 보낸 쪽은 마지막 ACK 뒤 TIME_WAIT를 거치는 것이 일반적입니다."
    - id: c
      text: "LISTEN"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "ESTABLISHED"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "SYN_SENT"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: b
  - id: u7-l03-p04-q02
    kind: choice
    difficulty: easy
    prompt: "마지막 ACK가 사라져 상대 FIN이 다시 오면 TIME_WAIT 쪽은 무엇을 할 수 있나요?"
    choices:
    - id: a
      text: "새 연결을 강제로 닫는다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "FIN을 다른 포트로 옮긴다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "ACK를 다시 보낼 수 있다"
      feedback: "TIME_WAIT는 다시 도착한 FIN에 ACK를 보낼 수 있도록 남습니다."
    - id: d
      text: "상대 데이터를 삭제한다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "IP 주소를 바꾼다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: c
  - id: u7-l03-p04-q03
    kind: choice
    difficulty: easy
    prompt: "TIME_WAIT가 이전 연결의 늦은 데이터를 새 연결에 섞이지 않게 할 때 구분에 쓰이는 조합은 무엇인가요?"
    choices:
    - id: a
      text: "화면 크기와 해상도"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "케이블 색과 길이"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "사용자 이름과 암호"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "IP 주소와 포트"
      feedback: "연결의 두 끝점은 IP 주소와 포트 조합으로 구분됩니다."
    - id: e
      text: "파일 이름과 확장자"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: d
  question_placements:
  - question_id: u7-l03-p04-q01
    after_paragraph: 1
  - question_id: u7-l03-p04-q02
    after_paragraph: 2
  - question_id: u7-l03-p04-q03
    after_paragraph: 3
- terms:
  - 자원 회수
  illustrations:
  - file: assets/animations/l27-daily-hotel-room-cleaning.svg
    title: "객실은 바로 비지 않아요"
    alt: "객실 100개가 모두 찬 호텔에서 손님이 체크아웃해도 청소와 점검이 끝날 때까지 기다리고, 점검이 끝나 정리되면 다음 손님을 받아 사용 중인 객실이 99에서 다시 찹니다."
    caption: "체크아웃 뒤에도 청소와 점검이 끝나야 다음 손님을 받습니다. 객실 100개는 설명용입니다."
    after_paragraph: -1
  - file: assets/animations/l27-time-wait-socket-slot.svg
    title: "끊었다고 바로 빈칸이 되지는 않습니다"
    alt: "연결 상태 칸 100개가 모두 차 있고, 내 연결의 칸은 끊은 뒤에도 TIME_WAIT 동안 남아 있다가 CLOSED가 되면 정리되어 99가 되며 새 연결이 그 자리에 기록될 수 있습니다."
    caption: "TIME_WAIT 동안에는 연결 상태 기록이 남아 있고, 정리된 뒤에 새 연결이 그 자리를 쓸 수 있습니다. 칸 100개는 설명용 비유입니다."
    after_paragraph: 1

  questions:
  - id: u7-l03-p05-q01
    kind: choice
    difficulty: easy
    prompt: "호텔 비유에서 체크아웃한 객실을 바로 다음 손님에게 주지 않는 이유는 무엇인가요?"
    choices:
    - id: a
      text: "객실 번호를 바꾸려고"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "손님이 다시 체크인할 때까지"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "호텔 인터넷을 끄려고"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "방 크기를 늘리려고"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "청소와 점검이 남아 있어서"
      feedback: "체크아웃 뒤 정리가 끝나야 다음 손님을 받을 수 있다는 비유입니다."
    answer: e
  - id: u7-l03-p05-q02
    kind: choice
    difficulty: easy
    prompt: "애니메이션의 100칸은 무엇을 설명하는 비유인가요?"
    choices:
    - id: a
      text: "연결 관리 자원이 정리되는 시점"
      feedback: "칸의 수는 설명용이며 실제 고정 소켓 개수를 뜻하지 않습니다."
    - id: b
      text: "실제 운영체제에 고정된 소켓 100개"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "서버가 받을 수 있는 정확한 사용자 수"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "포트 번호의 최댓값"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "호텔의 실제 객실 수"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: a
  - id: u7-l03-p05-q03
    kind: choice
    difficulty: easy
    prompt: "TIME_WAIT가 보인다는 사실 하나만으로 장애라고 할 수 있나요?"
    choices:
    - id: a
      text: "그렇다. 항상 장애다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "아니다. 주변 상황도 함께 봐야 한다"
      feedback: "상태만으로 장애를 단정하지 말고 연결량, 한도, 오류와 지연을 함께 봅니다."
    - id: c
      text: "그렇다. 서버를 즉시 재부팅해야 한다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "아니다. 연결이 없다는 뜻이다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "그렇다. 인터넷이 끊겼다는 뜻이다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: b
  question_placements:
  - question_id: u7-l03-p05-q01
    after_paragraph: 1
  - question_id: u7-l03-p05-q02
    after_paragraph: 2
  - question_id: u7-l03-p05-q03
    after_paragraph: 3
- terms: []
  illustrations:
  - file: assets/animations/l27-daily-who-hangs-up-first.svg
    title: "누가 먼저 끊어도 괜찮아요"
    alt: "왼쪽 칸에서는 내가 먼저 끊고 내가 잠깐 더 수화기를 들고 있고, 오른쪽 칸에서는 상대가 먼저 끊고 상대가 잠깐 더 들고 있습니다. 먼저 끊은 쪽이 마지막에 기다린다고 표시됩니다."
    caption: "먼저 끊은 쪽이 마지막에 잠깐 기다립니다. 누가 먼저 끊을지는 정해져 있지 않습니다."
    after_paragraph: -1
  - file: assets/animations/l27-who-closes-first.svg
    title: "먼저 닫는 쪽은 정해져 있지 않아요"
    alt: "왼쪽 칸에서는 클라이언트가 먼저 FIN을 보내 클라이언트가 TIME_WAIT를 거치고, 오른쪽 칸에서는 서버가 먼저 FIN을 보내 서버가 TIME_WAIT를 거칩니다. 먼저 FIN을 보낸 쪽이 TIME_WAIT를 거친다고 표시됩니다."
    caption: "능동 종료와 수동 종료는 클라이언트·서버의 고정된 역할이 아니라 누가 먼저 FIN을 보냈는지로 정해집니다."
    after_paragraph: 0

  questions:
  - id: u7-l03-p06-q01
    kind: choice
    difficulty: easy
    prompt: "능동 종료 측은 클라이언트와 서버 중 누구로 고정되나요?"
    choices:
    - id: c
      text: "고정되지 않는다"
      feedback: "누가 먼저 FIN을 보냈는지에 따라 능동 종료 측이 정해집니다."
    - id: a
      text: "항상 클라이언트"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "항상 서버"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "항상 라우터"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "항상 웹 브라우저"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: c
  - id: u7-l03-p06-q02
    kind: choice
    difficulty: easy
    prompt: "직접 통신 규칙을 설계할 때 종료 시점을 정하는 이유는 무엇인가요?"
    choices:
    - id: a
      text: "항상 클라이언트만 종료하게 하려고"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "포트 번호를 없애려고"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "IP 주소를 새로 받으려고"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "양쪽이 데이터를 마친 뒤 정리하도록 하려고"
      feedback: "프로토콜은 대화 순서와 종료 조건을 정해 양쪽이 안전하게 정리하도록 합니다."
    - id: e
      text: "응답 데이터를 건너뛰려고"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: d
  question_placements:
  - question_id: u7-l03-p06-q01
    after_paragraph: 1
  - question_id: u7-l03-p06-q02
    after_paragraph: 2
- terms: []
  illustrations:
  - file: assets/animations/l27-daily-three-groups-call.svg
    title: "전화 상태는 세 무리로 읽어요"
    alt: "전화 상태를 세 무리로 묶습니다. 전화를 내려놓거나 벨을 기다리는 무리, 거는 중·벨 울림·통화 중인 무리, 끝났다고 알리고 기다리며 정리하는 끊는 중 무리입니다."
    caption: "하나하나 외우기보다 어느 무리인지 읽습니다."
    after_paragraph: -1
  - file: assets/animations/l27-state-three-groups.svg
    title: "TCP 상태는 세 무리로 읽어요"
    alt: "TCP 상태를 세 무리로 묶습니다. CLOSED와 LISTEN의 연결 전·기다림 무리, SYN_SENT·SYN_RECEIVED·ESTABLISHED의 시작·통신 무리, FIN_WAIT_1·FIN_WAIT_2·CLOSE_WAIT·LAST_ACK·TIME_WAIT·CLOSING의 정리 중 무리입니다."
    caption: "이름 전체보다 어느 단계의 역할인지 기억합니다. 자세한 전이는 상태도에서 찾아봅니다."
    after_paragraph: 1

  questions:
  - id: u7-l03-p07-q01
    kind: choice
    difficulty: easy
    prompt: "TCP 상태를 크게 묶어 볼 때 연결 전이나 대기 중의 예는 무엇인가요?"
    choices:
    - id: a
      text: "FIN_WAIT_1과 FIN_WAIT_2"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "CLOSE_WAIT와 LAST_ACK"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "TIME_WAIT와 CLOSING"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "ESTABLISHED와 TIME_WAIT"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "CLOSED와 LISTEN"
      feedback: "CLOSED와 LISTEN은 아직 연결되지 않았거나 연결 요청을 기다리는 큰 무리에 속합니다."
    answer: e
  - id: u7-l03-p07-q02
    kind: choice
    difficulty: easy
    prompt: "ESTABLISHED는 어떤 단계의 상태인가요?"
    choices:
    - id: a
      text: "연결이 수립되어 통신하는 단계"
      feedback: "ESTABLISHED는 연결이 수립된 상태입니다."
    - id: b
      text: "연결 전 대기 단계"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "종료 뒤 자원 정리 단계"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "네트워크 주소를 찾는 단계"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "케이블 연결을 검사하는 단계"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: a
  - id: u7-l03-p07-q03
    kind: choice
    difficulty: easy
    prompt: "낯선 TCP 상태 이름을 만났을 때 이 Lesson의 쉬운 방법은 무엇인가요?"
    choices:
    - id: a
      text: "이름을 전부 외우기 전에는 넘어가지 않는다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "먼저 큰 연결 단계 중 어디에 속하는지 본다"
      feedback: "먼저 연결 전, 통신 중, 종료 중 어느 큰 단계인지 살펴봅니다."
    - id: c
      text: "항상 서버 오류라고 판단한다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "상태 이름을 포트 번호로 바꾼다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "FIN과 ACK를 무시한다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: b
  question_placements:
  - question_id: u7-l03-p07-q01
    after_paragraph: 2
  - question_id: u7-l03-p07-q02
    after_paragraph: 3
  - question_id: u7-l03-p07-q03
    after_paragraph: 3
- terms: []
  illustrations:
  - file: assets/animations/l27-daily-hangup-step-by-step.svg
    title: "끊는 순서를 처음부터 끝까지"
    alt: "내가 먼저 “저는 다 했어요”, 상대가 “알겠어요”, 상대가 “저도 끝났어요”, 내가 “알겠어요” 하고 말하는 네 마디가 오가며 양쪽 상태가 바뀌고, 마지막에는 내가 잠깐 더 들고 있다가 정리됩니다."
    caption: "내가 먼저 끊는 흔한 예에서 네 마디가 오가며 상태가 바뀝니다."
    after_paragraph: -1
  - file: assets/animations/l27-fin-ack-steps.svg
    title: "FIN과 ACK 네 단계"
    alt: "클라이언트가 FIN을 보내 FIN_WAIT_1, 서버가 ACK를 보내 CLOSE_WAIT, 서버가 FIN을 보내 LAST_ACK, 클라이언트가 ACK를 보내 서버가 CLOSED가 되는 순서입니다. 클라이언트는 TIME_WAIT 대기 뒤 CLOSED가 됩니다."
    caption: "흔한 종료 순서입니다. 실제로는 ACK와 FIN이 한 세그먼트에 함께 실릴 수도 있습니다."
    after_paragraph: 4

  questions:
  - id: u7-l03-p08-q01
    kind: choice
    difficulty: easy
    prompt: "흔한 종료 과정에서 클라이언트가 첫 FIN을 보내는 뜻은 무엇인가요?"
    choices:
    - id: a
      text: "클라이언트가 보낼 데이터가 끝났다고 알립니다"
      feedback: "FIN은 보내는 쪽이 자기 방향의 데이터 전송을 마쳤다고 알립니다."
    - id: b
      text: "서버가 보낼 데이터까지 모두 끝났다고 알립니다"
      feedback: "첫 FIN은 보낸 쪽의 송신이 끝났다는 뜻입니다. 서버는 자기 데이터를 더 보낼 수 있습니다."
    - id: c
      text: "서버가 보낸 FIN을 받았다고 확인합니다"
      feedback: "FIN은 송신 종료를 알리고, ACK는 받은 것을 확인합니다."
    - id: d
      text: "TCP 연결 상태를 즉시 모두 지웁니다"
      feedback: "FIN을 보내도 연결 정리 상태가 바로 사라지는 것은 아닙니다."
    - id: e
      text: "서버가 모든 데이터를 받았다고 확인합니다"
      feedback: "FIN은 받았다는 확인이 아니라, 보내는 쪽의 송신 종료 알림입니다."
    answer: a
  - id: u7-l03-p08-q02
    kind: choice
    difficulty: easy
    prompt: "클라이언트의 FIN을 확인한 뒤 서버에 보낼 데이터가 남아 있으면 어떻게 하나요?"
    choices:
    - id: a
      text: "남은 데이터를 버리고 바로 종료합니다"
      feedback: "클라이언트의 FIN은 클라이언트 쪽 송신 종료를 알립니다."
    - id: b
      text: "클라이언트가 서버의 데이터를 대신 보냅니다"
      feedback: "각 컴퓨터는 자기 쪽에서 보낼 데이터를 직접 보냅니다."
    - id: c
      text: "라우터가 서버의 남은 응답을 만들어 보냅니다"
      feedback: "라우터는 서버의 응답 내용을 대신 만들지 않습니다."
    - id: d
      text: "서버는 남은 데이터를 계속 보낼 수 있습니다"
      feedback: "첫 FIN은 클라이언트 쪽 송신만 끝냈다는 뜻입니다."
    - id: e
      text: "양쪽이 곧바로 CLOSED가 됩니다"
      feedback: "서버가 더 보낼 데이터가 있다면 종료는 아직 끝나지 않았습니다."
    answer: d
  - id: u7-l03-p08-q03
    kind: choice
    difficulty: easy
    prompt: "클라이언트가 마지막 ACK를 보내 서버가 이를 받은 뒤, 양쪽 연결 상태는 어떻게 정리되나요?"
    choices:
    - id: c
      text: "서버는 ACK 뒤 CLOSED, 클라이언트는 TIME_WAIT 뒤 CLOSED가 됩니다"
      feedback: "마지막 ACK를 받은 서버는 종료하고, 클라이언트는 TIME_WAIT 대기 뒤 정리됩니다."
    - id: a
      text: "서버가 TIME_WAIT를 거치고 클라이언트는 바로 CLOSED가 됩니다"
      feedback: "이 흔한 예에서는 먼저 FIN을 보낸 클라이언트 쪽에 TIME_WAIT가 남습니다."
    - id: b
      text: "양쪽 모두 마지막 ACK 직후 바로 CLOSED가 됩니다"
      feedback: "클라이언트는 마지막 ACK를 보낸 뒤에도 TIME_WAIT를 거칩니다."
    - id: d
      text: "클라이언트는 ESTABLISHED에 남고 서버는 CLOSED가 됩니다"
      feedback: "이 예에서는 클라이언트가 TIME_WAIT를 거친 뒤 CLOSED로 정리됩니다."
    - id: e
      text: "서버는 새 연결이 올 때까지 LAST_ACK에 남습니다"
      feedback: "서버가 마지막 ACK를 받으면 종료 절차를 마치고 CLOSED로 갑니다."
    answer: c
  question_placements:
  - question_id: u7-l03-p08-q01
    after_paragraph: 1
  - question_id: u7-l03-p08-q02
    after_paragraph: 2
  - question_id: u7-l03-p08-q03
    after_paragraph: 4
- terms: []
  illustrations:
  - file: assets/animations/l27-daily-three-to-remember.svg
    title: "끊는 일에서 기억할 세 가지"
    alt: "카드 세 장이 차례로 나타납니다. 한쪽이 먼저 끝내고, 상대도 남은 말을 마치고 끝내며, 먼저 끝낸 쪽이 마지막에 잠깐 기다린다는 내용입니다."
    caption: "먼저 끊은 쪽이 마지막에 잠깐 기다립니다."
    after_paragraph: -1
  - file: assets/animations/l27-close-three-points.svg
    title: "연결 종료에서 기억할 세 가지"
    alt: "카드 세 장이 차례로 나타납니다. 한쪽이 FIN으로 자기 송신을 끝내고, 상대가 남은 송신을 마친 뒤 자기 FIN을 보내며, 먼저 FIN을 보낸 쪽이 TIME_WAIT에서 기다린다는 내용입니다."
    caption: "TIME_WAIT는 먼저 FIN을 보낸 쪽에 남습니다. 서버가 먼저 FIN을 보냈다면 서버 쪽입니다."
    after_paragraph: 2
  questions:
  - id: u7-l03-p09-q01
    kind: choice
    difficulty: easy
    prompt: "보통 TIME_WAIT를 거치는 쪽은 누구인가요?"
    choices:
    - id: a
      text: "먼저 FIN을 보낸 쪽"
      feedback: "흔한 종료 흐름에서는 능동 종료 측, 즉 먼저 FIN을 보낸 쪽이 TIME_WAIT를 거칩니다."
    - id: b
      text: "항상 서버"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "항상 클라이언트"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "마지막 데이터를 받은 쪽"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "IP 주소가 큰 쪽"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: a
  - id: u7-l03-p09-q02
    kind: choice
    difficulty: easy
    prompt: "서버가 먼저 FIN을 보냈다면 TIME_WAIT는 어느 쪽에 생길 수 있나요?"
    choices:
    - id: a
      text: "항상 클라이언트 쪽"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: c
      text: "라우터 쪽"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "DNS 서버 쪽"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "서버 쪽"
      feedback: "누가 먼저 FIN을 보냈는지에 따라 서버도 TIME_WAIT를 거칠 수 있습니다."
    - id: e
      text: "양쪽 모두 반드시 같은 시간 동안"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: b
  - id: u7-l03-p09-q03
    kind: choice
    difficulty: easy
    prompt: "전체 종료 흐름을 가장 잘 요약한 것은 무엇인가요?"
    choices:
    - id: c
      text: "각자 FIN으로 송신을 끝내고 상대가 ACK로 확인한다"
      feedback: "각 방향의 송신은 FIN으로 끝을 알리고 상대의 ACK로 확인합니다."
    - id: a
      text: "클라이언트가 서버의 모든 데이터를 삭제한다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: b
      text: "서버만 FIN을 보내면 양쪽이 즉시 끝난다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: d
      text: "먼저 FIN을 보낸 쪽은 기다리지 않는다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    - id: e
      text: "ACK는 연결 시작에만 사용된다"
      feedback: "바로 앞 문단의 설명을 다시 확인해 보세요."
    answer: c
  question_placements:
  - question_id: u7-l03-p09-q01
    after_paragraph: 1
  - question_id: u7-l03-p09-q02
    after_paragraph: 2
  - question_id: u7-l03-p09-q03
    after_paragraph: 3
animations_dir: units/05-tcp-and-udp/lessons/03-tcp-연결종료-및-상태변화/assets/animations
additional_sources:
- https://studio.futurereadycampus.com/course-network/wiki/oeweo-network/lesson-27.html
- https://github.com/FutureReadyCampus/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/04-2.md
- https://www.rfc-editor.org/rfc/rfc9293.html
---
앞 Lesson에서는 SYN, SYN+ACK, ACK로 TCP 연결을 시작하는 과정을 살펴봤다. 이번에는 데이터 송수신을 마친 뒤 양쪽이 어떻게 각자 보낼 일을 끝내고 연결 상태를 정리하는지 따라간다. 먼저 끊자고 한 쪽과 요청을 받은 쪽의 역할은 클라이언트·서버라는 이름으로 고정되지 않는다.

## FIN · 연결을 끝내자는 요청
<!-- learn-page-id: fin-definition -->

TCP 연결은 양방향으로 데이터를 주고받는다. 한쪽 프로그램이 보낼 데이터를 다 보냈다고 해서 상대편도 동시에 보낼 일을 마쳤다고 단정할 수는 없다. 그래서 TCP에서는 각 방향의 송신이 끝났다는 사실을 따로 알리고, 양쪽이 차례로 정리한다.

전화 통화를 떠올려 보자. 한 사람이 “저는 할 말을 다 했어요”라고 말해도 상대가 답할 일이 남아 있을 수 있다. 상대가 자기 말을 마친 뒤 “저도 이제 끝났어요”라고 알려야 통화가 정리된다. TCP의 FIN(Finish)은 “내가 이 방향으로 보낼 데이터는 여기까지”라는 알림이고, ACK(Acknowledgment)는 “그 알림을 받았다”는 확인이다.

이 Lesson에서는 클라이언트가 먼저 FIN을 보내는 흔한 예를 따라간다. FIN을 먼저 보내는 쪽을 능동 종료 측, FIN을 받아 나중에 자기 FIN을 보내는 쪽을 수동 종료 측이라고 부른다. 이 이름은 누가 먼저 요청했는지를 뜻한다. 서버가 먼저 FIN을 보내면 역할도 반대로 바뀐다.

FIN은 한 방향의 송신이 끝났음을 알린다. 따라서 상대가 FIN을 보냈더라도, 내 쪽에서 아직 보낼 데이터가 남았다면 그 방향으로 계속 보낼 수 있다. 이처럼 한쪽 방향만 먼저 닫는 것을 half-close(절반 종료)라고 한다. 전화처럼 한 사람이 끊자마자 양쪽 통화가 모두 끝나는 것과 다른 점이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** FIN은 “내가 보낼 데이터는 여기까지”라고 알리는 신호다.
- **적용하기 (Apply):** 한쪽이 FIN을 보낸 뒤에도 반대 방향으로 데이터가 오갈 수 있는 이유를 말한다.
- **찾아보기 (Lookup):** FIN과 ACK의 헤더 표시는 TCP 헤더 설명에서 확인한다.

## FIN_WAIT 상태

먼저 FIN을 보낸 쪽은 자기 FIN이 확인되고 상대의 송신도 끝날 때까지 기다린다. FIN을 보내면 FIN_WAIT_1에 들어간다. 상대가 ACK를 보내면 FIN_WAIT_2로 이동해, 상대편이 자기 FIN을 보낼 때까지 기다린다. 이름의 1과 2를 외우기보다 “내 FIN의 확인을 기다리는 단계”와 “상대 FIN을 기다리는 단계”로 읽으면 된다.

예를 들어 클라이언트가 FIN을 보내고 서버가 ACK를 돌려주어도, 서버 프로그램에 보낼 응답이 남았다면 서버는 그 데이터를 마저 보낼 수 있다. 그동안 클라이언트는 FIN_WAIT_2에서 기다린다. 서버가 보낼 일을 마치면 자기 FIN을 보내고, 클라이언트가 ACK를 보내면서 두 번째 방향의 종료도 진행된다.

두 쌍이라는 말은 한쪽 방향의 FIN과 그 확인 ACK가 한 쌍, 반대 방향의 FIN과 확인 ACK가 또 한 쌍이라는 뜻이다. 그래서 보통 네 메시지를 주고받는 4-way 종료라고 부른다. 실제 전송에서는 ACK와 FIN이 한 세그먼트에 함께 실릴 수 있어 메시지 수가 그림의 단순한 네 단계와 달라 보일 때도 있다.

아래 종료 애니메이션에서 두 방향의 FIN과 ACK가 오가는 순서를 따라가 보자. 숫자 표시는 동작을 설명하기 위한 예시이며, 여기서는 순서번호 계산을 학습 목표로 삼지 않는다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** FIN_WAIT_1은 내 FIN 확인을, FIN_WAIT_2는 상대 FIN을 기다리는 단계다.
- **적용하기 (Apply):** 상대가 ACK만 보낸 뒤에도 데이터를 더 보낼 수 있는 상황을 설명한다.
- **찾아보기 (Lookup):** 동시에 종료를 시작하는 경우 등 다른 상태 이동은 TCP 상태도에서 확인한다.

## CLOSE_WAIT와 종료 지연

상대의 FIN을 받은 쪽은 그 FIN을 ACK로 확인한 뒤 CLOSE_WAIT에 들어간다. 이 말은 “상대는 이 방향으로 보낼 일을 끝냈고, 나는 아직 내 쪽 정리를 마치지 않았다”는 뜻이다. 상대 FIN이 왔다고 내 프로그램의 송신도 자동으로 끝나는 것은 아니다.

수신 프로그램이 남은 응답이나 정리 작업을 마치고 소켓을 닫으면, 이쪽도 FIN을 보낸다. 자기 FIN의 확인을 기다리는 마지막 단계가 LAST_ACK다. 상대 ACK가 도착하면 이 연결의 종료 절차가 끝난다.

CLOSE_WAIT가 오래 남는다면 애플리케이션이 상대의 종료 알림을 받은 뒤에도 자기 소켓을 닫지 않고 있는지 확인할 단서가 된다. 다만 상태 이름만으로 프로그램 오류라고 단정할 수는 없다. 애플리케이션이 데이터를 마무리하는 동안 잠시 이 상태에 있을 수 있고, 실제 원인은 로그와 연결 흐름을 함께 보고 판단해야 한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** CLOSE_WAIT는 상대 FIN을 확인했지만 내 쪽 종료는 아직 진행 중인 상태다.
- **적용하기 (Apply):** CLOSE_WAIT가 오래 이어질 때 애플리케이션의 종료 처리를 살펴볼 이유를 설명한다.
- **찾아보기 (Lookup):** 어느 프로세스가 연결을 보유하는지는 OS 네트워크 도구와 애플리케이션 로그에서 확인한다.

## TIME_WAIT

보통 먼저 FIN을 보낸 쪽은 상대의 FIN을 받은 뒤 마지막 ACK를 보내고 TIME_WAIT에 들어간다. 이름만 보면 “시간을 기다린다”는 상태다. 바로 CLOSED로 끝내지 않고 잠시 남아 있는 데에는 두 가지 이유가 있다.

첫째, 마지막 ACK가 네트워크에서 사라질 수 있다. 그러면 상대는 FIN을 다시 보낼 수 있다. TIME_WAIT로 남아 있으면 다시 온 FIN을 확인해 ACK를 한 번 더 보낼 수 있다. 둘째, 이전 연결에서 늦게 도착한 세그먼트가 같은 두 끝점(IP 주소와 포트 조합)을 사용하는 새 연결의 데이터로 잘못 섞이는 일을 줄인다.

TCP 표준은 이 대기 시간을 2 MSL(Maximum Segment Lifetime, 세그먼트가 네트워크에 남을 수 있는 최대 시간)로 설명한다. 실제 대기 시간의 구체적인 값과 표시 방식은 운영체제 구현에 따라 다를 수 있으므로, 여기서는 “마지막 확인에 대응하고 이전 연결의 흔적이 사라질 시간을 둔다”는 목적을 기억하자. 대기가 끝나면 연결 상태가 CLOSED로 정리된다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TIME_WAIT는 마지막 ACK 재전송과 이전 연결의 늦은 세그먼트에 대비하는 대기 상태다.
- **적용하기 (Apply):** TIME_WAIT가 단순한 지연이 아니라 연결을 안전하게 정리하는 과정임을 설명한다.
- **찾아보기 (Lookup):** 구체적인 대기 시간과 재사용 동작은 운영체제 문서에서 확인한다.

## 소켓 자원의 회수

소켓 자원을 호텔 객실에 비유해 보자. 손님이 체크아웃했어도 객실 청소와 점검이 끝나기 전까지는 다음 손님을 받지 않는다. TCP도 종료 메시지를 주고받은 직후 모든 연결 관리 기록을 바로 지우지 않는다. 특히 TIME_WAIT가 끝날 때까지는 연결 상태를 확인하기 위한 정보가 남는다.

애니메이션의 “100칸에서 99칸으로 줄어든다”는 그림은 연결 관리 자원이 회수되는 시점을 보여 주는 단순한 비유다. 실제 운영체제가 소켓 파일 기술자 100개를 고정된 칸에 보관한다는 뜻은 아니다. 애플리케이션이 소켓을 닫은 뒤에도 커널이 TIME_WAIT 상태를 유지할 수 있으므로, “프로그램이 닫은 소켓”과 “커널이 정리 중인 TCP 연결 상태”를 구별해야 한다.

서버처럼 연결을 많이 처리하는 컴퓨터에서는 짧은 시간에 종료된 연결이 많이 생길 수 있다. 그렇다고 TIME_WAIT가 보인다는 이유만으로 장애라고 단정할 수는 없다. 연결 요청량, 실제 자원 한도, 오류와 지연 같은 주변 상황을 함께 확인해야 한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 애플리케이션이 닫기를 요청한 뒤에도 커널의 TCP 상태가 잠시 남을 수 있다.
- **적용하기 (Apply):** 애니메이션의 100칸을 실제 고정 소켓 개수로 오해하지 않고 자원 회수 시점으로 읽는다.
- **찾아보기 (Lookup):** 상태별 연결 수와 자원 사용은 운영체제 네트워크 도구에서 확인한다.

## 어느 쪽이 먼저 닫을까

능동 종료와 수동 종료는 클라이언트·서버의 고정된 역할이 아니라 누가 먼저 FIN을 보냈는지로 정해진다. 웹 서버가 먼저 응답을 끝내고 연결을 닫을 수도 있고, 클라이언트가 먼저 닫을 수도 있다. 먼저 FIN을 보낸 쪽은 보통 TIME_WAIT를 거치므로 연결이 많은 서버에서는 자원 사용을 살펴볼 필요가 있지만, 이 사실만으로 “항상 클라이언트가 먼저 닫아야 한다”는 규칙이 생기지는 않는다.

애플리케이션 프로토콜은 프로그램끼리 어떤 순서로 요청과 응답을 주고받고 언제 끝낼지를 정한 약속이다. 이미 HTTP 같은 표준을 사용하는 서비스는 그 표준의 동작을 따라야 한다. 직접 통신 규칙을 설계한다면 어느 쪽이 어떤 조건에서 종료를 시작하는지 분명히 정해야 한다. 핵심은 자원을 한쪽에 떠넘기는 것이 아니라, 서비스가 정한 대화 순서에 맞춰 양쪽이 데이터를 다 보낸 뒤 정리하도록 하는 것이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 능동 종료는 먼저 FIN을 보낸 쪽이며 클라이언트로 고정되지 않는다.
- **적용하기 (Apply):** 서버가 먼저 FIN을 보내는 경우에도 같은 종료 절차가 역할만 바뀌어 진행됨을 판단한다.
- **찾아보기 (Lookup):** 서비스가 연결을 닫는 시점은 애플리케이션 프로토콜과 구현 문서에서 확인한다.

## TCP 상태는 세 무리로 읽자
<!-- learn-page-id: tcp-state-definition -->

상태 이름이 많아 보여도 연결의 큰 흐름으로 묶으면 읽기 쉽다. 아래 표는 상태도를 대신하는 전체 그림이 아니라, 이름을 세 단계로 분류해 기억하기 위한 요약이다.

| 연결 단계 | 대표 상태 | 쉬운 말로 읽으면 |
| --- | --- | --- |
| 아직 연결되지 않았거나 기다리는 중 | `CLOSED`, `LISTEN` | 연결이 없거나 서버가 요청을 기다린다 |
| 연결을 시작하고 데이터를 주고받는 중 | `SYN_SENT`, `SYN_RECEIVED`, `ESTABLISHED` | 연결 메시지를 확인하고 통신을 시작한다 |
| 한쪽 또는 양쪽이 연결을 정리하는 중 | `FIN_WAIT_1`, `FIN_WAIT_2`, `CLOSE_WAIT`, `LAST_ACK`, `TIME_WAIT`, `CLOSING` | FIN과 ACK를 주고받고 남은 상태를 정리한다 |

여기서 자세히 기억할 것은 이름 전체가 아니라 역할이다. 앞 Lesson에서 본 LISTEN은 서버가 연결을 기다리는 상태이고, ESTABLISHED는 연결이 수립된 상태다. 이번 Lesson에서는 FIN_WAIT, CLOSE_WAIT, TIME_WAIT가 어떤 정리 단계를 가리키는지 살펴봤다. CLOSING은 양쪽이 거의 동시에 종료를 시작하는 등 일반적인 네 메시지 순서와 다른 경우에 등장할 수 있으므로, 우선 상태표에서 찾아볼 수 있으면 충분하다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP 상태는 연결 전, 연결 수립·통신 중, 종료 중의 큰 단계로 묶어 볼 수 있다.
- **적용하기 (Apply):** 상태 이름이 낯설 때 표에서 어느 단계에 속하는지 찾는다.
- **찾아보기 (Lookup):** 각 상태의 세부 전이 조건은 TCP 상태도와 표준에서 확인한다.

## FIN과 ACK 순서로 종료 따라가기

이제 흔한 종료 순서를 처음부터 끝까지 한 번 더 따라가 보자. 이 예에서는 클라이언트가 먼저 끝내자고 한다.

1. **클라이언트가 FIN을 보낸다.** “내가 보낼 데이터는 여기까지”라고 알리고 FIN_WAIT_1에서 확인을 기다린다.
2. **서버가 ACK를 보낸다.** 클라이언트의 FIN을 받았다고 확인하고 CLOSE_WAIT에서 자기 쪽 정리를 한다. 서버는 아직 보낼 데이터가 남았다면 마저 보낼 수 있다.
3. **서버도 FIN을 보낸다.** 보낼 일을 마친 서버가 자기 방향도 끝내겠다고 알리고 LAST_ACK에서 확인을 기다린다. 클라이언트는 서버의 FIN을 확인하고 TIME_WAIT에 들어간다.
4. **클라이언트가 보낸 마지막 ACK를 서버가 받는다.** 서버는 종료를 마치고 CLOSED로 가며, 클라이언트는 TIME_WAIT 대기가 끝난 뒤 CLOSED로 정리된다.

세 번째 단계에서 서버의 ACK와 FIN은 실제로 한 세그먼트에 함께 실릴 수도 있다. 네 단계는 양쪽 송신을 각각 끝내는 논리를 설명하는 기본 모형이다. 그림의 네 화살표만 외우기보다 “각자 자기 FIN을 보내고, 상대가 확인한다”는 원리를 잡자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 종료의 네 단계는 양쪽이 각각 FIN을 보내고 상대가 ACK로 확인하는 흐름이다.
- **적용하기 (Apply):** 서버가 아직 보낼 데이터가 있으면 첫 FIN 뒤에도 연결의 반대 방향이 열려 있음을 설명한다.
- **찾아보기 (Lookup):** ACK·FIN 결합이나 재전송은 실제 TCP 캡처에서 확인한다.

## 연결 종료에서 기억할 세 가지

흔한 종료 예에서 TIME_WAIT는 먼저 FIN을 보낸 능동 종료 측에 남는다. 예에서 클라이언트가 먼저 FIN을 보냈기 때문에 클라이언트가 TIME_WAIT를 거친다. 서버가 먼저 FIN을 보냈다면 서버 쪽이 그 역할을 맡는다. 따라서 “클라이언트 상태”나 “서버 상태”로 외우지 말고, “먼저 FIN을 보낸 쪽의 대기”로 기억하자.

양쪽이 거의 동시에 FIN을 보내면 표준 상태도에 CLOSING 같은 다른 경로가 나타날 수 있다. 이런 경우도 결국 서로의 종료 메시지를 확인하고 정리하는 과정이다. 이 Lesson에서는 흔한 순서를 먼저 이해하고, 드문 상태 이름과 모든 전이 조건은 필요할 때 상태표에서 찾아보면 된다.

전체를 한 문장으로 묶으면 이렇다. **한쪽이 FIN으로 자기 송신을 끝내고, 상대가 남은 송신을 마친 뒤 자기 FIN을 보낸다. 먼저 FIN을 보낸 쪽은 마지막 확인과 늦게 도착할 데이터에 대비해 TIME_WAIT에서 잠시 기다린다.**

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 보통 먼저 FIN을 보낸 쪽이 마지막 ACK 뒤 TIME_WAIT를 거친다.
- **적용하기 (Apply):** 서버가 먼저 FIN을 보내면 TIME_WAIT도 서버 쪽에 생길 수 있음을 설명한다.
- **찾아보기 (Lookup):** 동시에 종료를 시작하는 CLOSING 경로는 전체 TCP 상태도에서 확인한다.
