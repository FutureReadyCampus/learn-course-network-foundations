---
id: u5-l26-tcp-연결과정
title: TCP 연결과정
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-26.md
wiki_diagram: units/05-tcp-and-udp/lessons/02-tcp-연결과정/assets/diagrams/lesson-26.svg
page_metadata:
- terms:
  - 3-way handshake
  illustrations:
  - file: assets/animations/l26-daily-hello-3-steps.svg
    title: "여보세요, 네 들려요, 네"
    alt: "나와 가게 사이에서 먼저 “여보세요?”, 이어서 “네, 들려요. 그쪽도 들리나요?”, 마지막으로 “네, 들립니다”가 차례로 오갑니다. 세 마디가 오가야 서로 들린다고 알게 된다고 표시됩니다."
    caption: "전화는 세 마디로 서로 들리는지 확인합니다. TCP의 세 메시지도 요청, 응답 겸 요청, 마지막 확인으로 이어집니다."
    after_paragraph: -1
  - file: assets/animations/l26-syn-synack-ack.svg
    title: "SYN, SYN+ACK, ACK"
    alt: "클라이언트와 서버 사이에서 SYN, SYN+ACK, ACK 세 메시지가 차례로 오가며 연결 준비가 끝납니다."
    caption: "TCP 연결 준비는 연결 요청, 요청 확인과 서버의 요청, 마지막 확인의 세 메시지로 이루어집니다."
    after_paragraph: 2
  questions:
  - id: u7-l02-p01-extra-easy-1
    kind: choice
    difficulty: easy
    prompt: "TCP 연결을 준비할 때 먼저 주고받는 것은 무엇인가요?"
    choices:
    - id: a
      text: "연결 준비 메시지"
      feedback: "먼저 연결 준비 메시지를 주고받습니다."
    - id: b
      text: "웹 페이지 파일 전체"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "새 케이블 설치 요청"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "DNS 이름 등록"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "화면 표시 설정"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  - id: u7-l02-p01-extra-easy-2
    kind: choice
    difficulty: easy
    prompt: "전화 비유에서 첫 번째 사람이 먼저 하는 말은 무엇인가요?"
    choices:
    - id: a
      text: "“네, 들립니다”"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "“통화 끝났어요”"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "“여보세요?”"
      feedback: "첫 사람이 “여보세요?”라고 부릅니다."
    - id: d
      text: "“파일을 보냈어요”"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "“번호를 바꿨어요”"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  - id: u7-l02-p01-q01
    kind: choice
    difficulty: easy
    prompt: "시간 흐름 그림에서 아래쪽으로 갈수록 무엇을 뜻하나요?"
    choices:
    - id: a
      text: "시간이 뒤로 간다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "서버가 가까워진다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "파일 크기가 커진다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "연결이 끝난다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "시간이 앞으로 흐른다"
      feedback: "그림은 위에서 아래로 시간이 흐릅니다."
    answer: e
  - id: u7-l02-p01-q02
    kind: choice
    difficulty: easy
    prompt: "그림에서 왼쪽에서 오른쪽으로 가는 화살표는 누가 보내나요?"
    choices:
    - id: a
      text: "서버가 클라이언트로"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "클라이언트가 서버로"
      feedback: "왼쪽에서 오른쪽은 클라이언트에서 서버로 가는 메시지입니다."
    - id: c
      text: "라우터가 서버로"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "DNS가 클라이언트로"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "둘 다 동시에"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: b
  - id: u7-l02-p01-q03
    kind: choice
    difficulty: easy
    prompt: "두 번째 메시지에는 무엇이 함께 들어 있나요?"
    choices:
    - id: a
      text: "파일 전체와 종료 요청"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "DNS 답과 새 IP 주소"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "클라이언트의 마지막 ACK만"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "서버의 응답과 서버 자신의 연결 요청"
      feedback: "두 번째 메시지는 응답과 서버 쪽 연결 요청을 함께 담습니다."
    - id: e
      text: "웹 페이지 처리 결과"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: d
  - id: u7-l02-p01-extra-hard
    kind: choice
    difficulty: easy
    prompt: "3-way handshake가 끝났다는 것만으로 무엇까지 알 수 있나요?"
    choices:
    - id: a
      text: "웹 페이지가 화면에 떴다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "파일이 모두 저장됐다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "애플리케이션 요청 처리는 아직 알 수 없다"
      feedback: "연결 준비가 끝나도 앱의 요청 처리 성공까지 보장하지 않습니다."
    - id: d
      text: "서버 앱이 요청을 처리했다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "인터넷이 끊겼다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  question_placements:
  - question_id: u7-l02-p01-extra-easy-1
    after_paragraph: 1
  - question_id: u7-l02-p01-extra-easy-2
    after_paragraph: 2
  - question_id: u7-l02-p01-q01
    after_paragraph: 3
  - question_id: u7-l02-p01-q02
    after_paragraph: 3
  - question_id: u7-l02-p01-q03
    after_paragraph: 4
  - question_id: u7-l02-p01-extra-hard
    after_paragraph: 4
- terms:
  - RTT
  - 포트(port)
  illustrations:
  - file: assets/animations/l26-daily-call-round-trip.svg
    title: "말을 건네고 대답이 오기까지"
    alt: "나와 가게가 있습니다. 가게 번호와 내선 80번으로 걸면 내 목소리가 가는 데 25ms, 대답이 돌아오는 데 25ms가 걸리고 전체가 왕복 시간 50ms라고 표시됩니다."
    caption: "말을 건네고 대답을 들을 때까지가 왕복 시간입니다. 25ms씩이라는 값은 예시입니다."
    after_paragraph: -1
  - file: assets/animations/l26-rtt-50ms.svg
    title: "RTT는 왕복 시간이에요"
    alt: "노트북이 192.168.0.20의 포트 80으로 연결을 요청합니다. 서버로 가는 데 25ms, 돌아오는 데 25ms가 걸려 RTT는 50ms이고, 서버 처리 시간은 0으로 둔 단순한 예시입니다."
    caption: "RTT는 요청을 보내고 응답이 돌아오기까지의 왕복 시간입니다. 25ms씩 나눈 것은 이 예를 위한 단순화입니다."
    after_paragraph: 2
  questions:
  - id: u7-l02-p02-extra-easy-1
    kind: choice
    difficulty: easy
    prompt: "컴퓨터 안에서 통신할 프로그램의 접점을 구분하는 번호는 무엇인가요?"
    choices:
    - id: a
      text: "MAC 주소"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "순서번호"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "MSS"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "RTT"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "포트 번호"
      feedback: "포트 번호는 컴퓨터 안의 통신 프로그램 접점을 구분합니다."
    answer: e
  - id: u7-l02-p02-extra-easy-2
    kind: choice
    difficulty: easy
    prompt: "요청을 보내고 응답이 돌아오기까지 걸리는 시간은 무엇인가요?"
    choices:
    - id: a
      text: "MSS"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "RTT"
      feedback: "RTT는 요청과 응답 사이의 왕복 시간입니다."
    - id: c
      text: "ACK"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "SYN"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "LISTEN"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: b
  - id: u7-l02-p02-q01
    kind: choice
    difficulty: easy
    prompt: "본문의 예시에서 RTT 50ms는 몇 초인가요?"
    choices:
    - id: a
      text: "0.5초"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "5초"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "0.005초"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "0.05초"
      feedback: "50ms는 0.05초입니다."
    - id: e
      text: "50초"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: d
  - id: u7-l02-p02-q02
    kind: choice
    difficulty: easy
    prompt: "단순한 그림에서 RTT 50ms를 양쪽 방향에 똑같이 나누면 한 방향은 얼마인가요?"
    choices:
    - id: a
      text: "25ms"
      feedback: "예시에서는 50ms를 가는 데 25ms, 오는 데 25ms로 나눕니다."
    - id: b
      text: "50ms"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "100ms"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "5ms"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "0ms"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  - id: u7-l02-p02-q03
    kind: choice
    difficulty: easy
    prompt: "실제 RTT를 항상 정확히 반으로 나눌 수 없는 이유는 무엇인가요?"
    choices:
    - id: a
      text: "TCP에는 응답이 없어서"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "포트가 두 개라서"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "MSS가 달라서"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "모든 연결이 50ms라서"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "양쪽 경로 시간과 서버 처리 시간이 달라질 수 있어서"
      feedback: "실제 경로와 서버 처리 시간은 서로 다를 수 있습니다."
    answer: e
  - id: u7-l02-p02-extra-hard
    kind: choice
    difficulty: easy
    prompt: "연결을 준비하는 동안 오가는 세그먼트의 주된 목적은 무엇인가요?"
    choices:
    - id: a
      text: "사진 파일 전송"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "화면 해상도 변경"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "DNS 등록"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "연결에 필요한 정보 교환"
      feedback: "연결 준비 세그먼트는 연결에 필요한 정보를 주고받습니다."
    - id: e
      text: "파일 저장"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: d
  question_placements:
  - question_id: u7-l02-p02-extra-easy-1
    after_paragraph: 1
  - question_id: u7-l02-p02-extra-easy-2
    after_paragraph: 2
  - question_id: u7-l02-p02-q01
    after_paragraph: 2
  - question_id: u7-l02-p02-q02
    after_paragraph: 3
  - question_id: u7-l02-p02-q03
    after_paragraph: 3
  - question_id: u7-l02-p02-extra-hard
    after_paragraph: 4
- terms:
  - SYN
  - Payload(페이로드)
  - 순서번호
  illustrations:
  - file: assets/animations/l26-daily-note-without-body.svg
    title: "용건 없는 첫 마디"
    alt: "쪽지 한 장에 받는 곳·보내는 곳, 말머리, 용건 칸이 있습니다. 말머리에서 연결을 시작한다는 표시와 내 시작 번호 1000이 켜지고 용건 칸은 비어 있어 연결 준비만 한다고 표시됩니다."
    caption: "첫 “여보세요?”에는 용건이 들어 있지 않고 연결 준비만 합니다. 1000은 예시 번호입니다."
    after_paragraph: -1
  - file: assets/animations/l26-syn-segment-no-payload.svg
    title: "연결 요청도 세그먼트예요"
    alt: "TCP 세그먼트가 IP 헤더, TCP 헤더, Payload로 나뉘어 있습니다. TCP 헤더의 SYN 표시가 켜지고 초기 순서번호 1000이 담기며 Payload는 비어 있습니다."
    caption: "SYN 세그먼트는 연결 준비만 하며 Payload가 없습니다. 초기 순서번호 1000은 예시입니다."
    after_paragraph: 1
  questions:
  - id: u7-l02-p03-extra-easy-1
    kind: choice
    difficulty: easy
    prompt: "TCP 연결 요청은 무엇에 담겨 전달되나요?"
    choices:
    - id: a
      text: "포트 번호 자체"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "DNS 레코드"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "TCP 세그먼트"
      feedback: "TCP 연결 요청도 TCP 세그먼트에 담깁니다."
    - id: d
      text: "파일 이름"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "화면 픽셀"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  - id: u7-l02-p03-extra-easy-2
    kind: choice
    difficulty: easy
    prompt: "이 페이지의 첫 SYN 예시에는 애플리케이션 파일 내용이 들어 있나요?"
    choices:
    - id: a
      text: "항상 들어 있다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "들어 있지 않다"
      feedback: "예시의 SYN에는 애플리케이션 Payload가 없습니다."
    - id: c
      text: "라우터가 넣는다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "MSS만큼 들어 있다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "ACK 번호로 바뀐다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: b
  - id: u7-l02-p03-q01
    kind: choice
    difficulty: easy
    prompt: "SYN은 무엇을 알리는 표시인가요?"
    choices:
    - id: a
      text: "연결 시작"
      feedback: "SYN은 연결을 시작하자는 제어 표시입니다."
    - id: b
      text: "파일 전송 완료"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "서버 종료"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "IP 주소 변경"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "RTT 측정 완료"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  - id: u7-l02-p03-q02
    kind: choice
    difficulty: easy
    prompt: "SYN에는 보내는 쪽의 어떤 번호가 함께 담기나요?"
    choices:
    - id: a
      text: "초기 순서번호"
      feedback: "SYN은 보내는 쪽의 초기 순서번호를 알립니다."
    - id: b
      text: "포트 번호"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "RTT 값"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "파일 크기"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "DNS 번호"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  - id: u7-l02-p03-q03
    kind: choice
    difficulty: easy
    prompt: "본문에서 클라이언트의 초기 순서번호로 든 1000은 어떤 값인가요?"
    choices:
    - id: a
      text: "모든 연결에서 고정된 값"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "서버 포트 번호"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "계산을 위한 예시 값"
      feedback: "1000은 이해를 돕기 위한 예시 번호입니다."
    - id: d
      text: "RTT 값"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "파일 크기"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  - id: u7-l02-p03-extra-hard
    kind: choice
    difficulty: easy
    prompt: "예시의 첫 SYN에 웹 요청 본문이나 파일 바이트가 있나요?"
    choices:
    - id: a
      text: "예, 파일 전체가 있다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "라우터가 채워 넣는다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "항상 1000바이트가 있다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "DNS가 대신 보낸다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "아니요, 연결 준비 정보만 있다"
      feedback: "첫 SYN은 연결 준비용이며 웹 요청 본문이나 파일 바이트를 담지 않습니다."
    answer: e
  question_placements:
  - question_id: u7-l02-p03-extra-easy-1
    after_paragraph: 1
  - question_id: u7-l02-p03-extra-easy-2
    after_paragraph: 1
  - question_id: u7-l02-p03-q01
    after_paragraph: 2
  - question_id: u7-l02-p03-q02
    after_paragraph: 2
  - question_id: u7-l02-p03-q03
    after_paragraph: 3
  - question_id: u7-l02-p03-extra-hard
    after_paragraph: 4
- terms:
  - ACK
  illustrations:
  - file: assets/animations/l26-daily-bookmark-next-page.svg
    title: "다음에 펼칠 쪽을 알려 줘요"
    alt: "쪽번호 999부터 1003이 한 줄로 있습니다. 내 시작은 1000쪽이고 그 신호도 한 쪽을 차지하며, 상대는 방금 읽은 쪽이 아니라 다음에 펼칠 1001쪽을 알려 줍니다."
    caption: "책갈피는 방금 읽은 쪽이 아니라 다음에 펼칠 쪽에 꽂습니다. 번호는 예시입니다."
    after_paragraph: -1
  - file: assets/animations/l26-ack-next-number.svg
    title: "ACK 번호는 다음 순서번호"
    alt: "순서번호 999부터 1003이 한 줄로 있습니다. 클라이언트가 SYN 1000을 보내면 SYN이 한 자리를 차지하고, 서버는 다음에 받고 싶은 1001을 ACK로 알려 줍니다."
    caption: "ACK 번호는 방금 받은 번호가 아니라 다음에 받고 싶은 순서번호입니다. 번호는 예시입니다."
    after_paragraph: 1
  questions:
  - id: u7-l02-p04-extra-easy-1
    kind: choice
    difficulty: easy
    prompt: "ACK 번호는 무엇을 알려 주나요?"
    choices:
    - id: a
      text: "서버의 포트 번호"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "다음에 받고 싶은 순서번호"
      feedback: "ACK 번호는 다음에 받고 싶은 순서번호를 가리킵니다."
    - id: c
      text: "왕복 시간"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "파일 전체 크기"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "연결을 닫는 시각"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: b
  - id: u7-l02-p04-extra-easy-2
    kind: choice
    difficulty: easy
    prompt: "클라이언트가 SYN 번호 1000을 보내면 서버는 예시에서 어떤 ACK 번호를 보내나요?"
    choices:
    - id: a
      text: "1000"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "999"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "4000"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "1001"
      feedback: "SYN이 한 자리를 차지하므로 다음 번호 1001을 확인합니다."
    - id: e
      text: "1500"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: d
  - id: u7-l02-p04-q01
    kind: choice
    difficulty: easy
    prompt: "순서번호는 통신의 어느 방향에 있나요?"
    choices:
    - id: a
      text: "서버에서만 사용한다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "클라이언트에서만 사용한다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "두 방향에 각각 있다"
      feedback: "클라이언트와 서버가 각자 자기 방향의 시작 번호를 정합니다."
    - id: d
      text: "라우터에서만 사용한다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "파일을 저장할 때만 있다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  - id: u7-l02-p04-q02
    kind: choice
    difficulty: easy
    prompt: "서버는 자신의 시작 번호를 언제 알리나요?"
    choices:
    - id: a
      text: "첫 메시지 전에 별도 전화로"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "연결을 닫은 뒤"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "DNS 응답에서"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "파일을 다 받은 뒤"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "SYN+ACK 메시지에서"
      feedback: "서버는 SYN+ACK에 자신의 시작 번호를 함께 알립니다."
    answer: e
  - id: u7-l02-p04-q03
    kind: choice
    difficulty: easy
    prompt: "ACK 표시가 켜져 있다는 것은 무엇을 뜻하나요?"
    choices:
    - id: a
      text: "파일이 저장됐다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "헤더의 확인 번호를 사용한다"
      feedback: "ACK 표시가 켜지면 헤더의 확인 번호를 사용합니다."
    - id: c
      text: "RTT가 0이다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "서버가 종료됐다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "MSS가 바뀌었다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: b
  - id: u7-l02-p04-extra-hard
    kind: choice
    difficulty: easy
    prompt: "ACK 번호는 방금 받은 위치와 다음에 받고 싶은 위치 중 무엇을 가리키나요?"
    choices:
    - id: a
      text: "방금 받은 위치"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "파일의 끝"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "서버 포트"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "다음에 받고 싶은 위치"
      feedback: "ACK 번호는 다음에 받고 싶은 위치를 가리킵니다."
    - id: e
      text: "RTT의 절반"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: d
  question_placements:
  - question_id: u7-l02-p04-extra-easy-1
    after_paragraph: 1
  - question_id: u7-l02-p04-extra-easy-2
    after_paragraph: 2
  - question_id: u7-l02-p04-q01
    after_paragraph: 3
  - question_id: u7-l02-p04-q02
    after_paragraph: 3
  - question_id: u7-l02-p04-q03
    after_paragraph: 4
  - question_id: u7-l02-p04-extra-hard
    after_paragraph: 4
- terms:
  - SYN+ACK
  illustrations:
  - file: assets/animations/l26-daily-numbers-call.svg
    title: "여보세요, 번호를 서로 알려 줘요"
    alt: "나와 가게가 번호를 주고받습니다. 내가 번호 1000을 말하고, 가게가 1001을 기다리며 자기 번호 4000을 알리고, 내가 4000을 잘 들었다며 다음 4001을 말하면 양쪽이 서로의 번호를 알게 됩니다."
    caption: "세 마디가 오가면 양쪽이 서로의 시작 번호를 알고 확인합니다. 1000과 4000은 예시입니다."
    after_paragraph: -1
  - file: assets/animations/l26-three-way-handshake.svg
    title: "SYN, SYN+ACK, ACK로 시작하는 TCP 연결"
    alt: "클라이언트가 SYN과 순서번호 1000을 보내고, 서버가 SYN+ACK로 순서번호 4000과 확인 번호 1001을 돌려주며, 클라이언트가 확인 번호 4001의 ACK를 보내 양쪽이 서로의 시작 번호를 확인하는 과정입니다."
    caption: "첫 메시지는 연결을 요청하고, 두 번째는 요청을 확인하면서 서버의 시작 번호를 알리며, 세 번째는 그 번호를 확인합니다."
    after_paragraph: 3
  questions:
  - id: u7-l02-p05-extra-easy-1
    kind: choice
    difficulty: easy
    prompt: "예시에서 서버의 시작 순서번호로 쓰인 값은 무엇인가요?"
    choices:
    - id: a
      text: "4000"
      feedback: "이 페이지 예시에서는 서버의 시작 번호를 4000으로 둡니다."
    - id: b
      text: "1000"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "1001"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "4001"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "1460"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  - id: u7-l02-p05-extra-easy-2
    kind: choice
    difficulty: easy
    prompt: "첫 번째 메시지는 누가 누구에게 보내나요?"
    choices:
    - id: a
      text: "서버가 클라이언트에게 SYN+ACK"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "서버가 클라이언트에게 ACK"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "클라이언트가 서버에게 FIN"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "라우터가 양쪽에게 ACK"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "클라이언트가 서버에게 SYN"
      feedback: "첫 메시지는 클라이언트가 서버로 보내는 SYN입니다."
    answer: e
  - id: u7-l02-p05-q01
    kind: choice
    difficulty: easy
    prompt: "두 번째 메시지 SYN+ACK에는 어떤 확인 번호가 있나요?"
    choices:
    - id: a
      text: "1000"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "4000"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "4001"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "1001"
      feedback: "서버는 클라이언트의 SYN 1000 다음 번호인 1001을 확인합니다."
    - id: e
      text: "1460"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: d
  - id: u7-l02-p05-q02
    kind: choice
    difficulty: easy
    prompt: "서버가 SYN 순서번호 4000을 보내면 클라이언트의 확인 번호는 얼마인가요?"
    choices:
    - id: a
      text: "4000"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "1001"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "4001"
      feedback: "서버의 SYN도 한 자리를 차지하므로 클라이언트는 4001을 확인합니다."
    - id: d
      text: "1000"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "1500"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  - id: u7-l02-p05-q03
    kind: choice
    difficulty: easy
    prompt: "이 설명에서 서버는 언제 연결 준비가 완료된 상태가 되나요?"
    choices:
    - id: a
      text: "첫 SYN을 보내기 전"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "마지막 ACK가 도착한 뒤"
      feedback: "서버는 마지막 ACK를 받은 뒤 연결 준비 완료 상태가 됩니다."
    - id: c
      text: "SYN을 받자마자"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "클라이언트가 포트를 열 때"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "RTT가 0이 될 때"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: b
  - id: u7-l02-p05-extra-hard
    kind: choice
    difficulty: easy
    prompt: "단순 예시에서 SYN+ACK가 약 50ms에 도착한 뒤, 마지막 ACK가 서버에 가는 데 더 걸리는 시간은 얼마인가요?"
    choices:
    - id: a
      text: "25ms"
      feedback: "왕복 50ms를 반으로 나눈 예시라 마지막 편도에 약 25ms가 더 걸립니다."
    - id: b
      text: "50ms"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "75ms"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "100ms"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "0ms"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  question_placements:
  - question_id: u7-l02-p05-extra-easy-1
    after_paragraph: 1
  - question_id: u7-l02-p05-extra-easy-2
    after_paragraph: 2
  - question_id: u7-l02-p05-q01
    after_paragraph: 2
  - question_id: u7-l02-p05-q02
    after_paragraph: 2
  - question_id: u7-l02-p05-q03
    after_paragraph: 3
  - question_id: u7-l02-p05-extra-hard
    after_paragraph: 4
- terms:
  - MSS
  - 바이트(byte)
  illustrations:
  - file: assets/animations/l26-daily-text-length-limit.svg
    title: "한 통에 보낼 수 있는 길이"
    alt: "나와 친구가 각자 “나한테는 한 통에 70자 이하로”, “나한테는 60자 이하로” 하고 알립니다. 긴 내용은 상대가 정한 길이에 맞춰 나눠 보내며 방향마다 길이가 달라도 됩니다."
    caption: "문자는 상대가 알린 길이에 맞춰 나눠 보냅니다. 70자와 60자는 예시입니다."
    after_paragraph: -1
  - file: assets/animations/l26-mss-exchange.svg
    title: "MSS는 한 세그먼트의 데이터 크기"
    alt: "클라이언트가 SYN에 MSS 1460을, 서버가 SYN+ACK에 MSS 1400을 담아 알립니다. 각자 상대가 알린 MSS 이하로 데이터를 나눠 보내며 방향마다 값이 달라도 됩니다."
    caption: "MSS는 한 TCP 세그먼트에 실을 수 있는 TCP 데이터의 최대 크기입니다. 1460과 1400은 예시입니다."
    after_paragraph: 1
  questions:
  - id: u7-l02-p06-extra-easy-1
    kind: choice
    difficulty: easy
    prompt: "MSS가 나타내는 크기는 무엇인가요?"
    choices:
    - id: a
      text: "한 세그먼트의 TCP 데이터 최대 크기"
      feedback: "MSS는 한 TCP 세그먼트에 실을 TCP 데이터의 최대 크기입니다."
    - id: b
      text: "IP 패킷 전체의 크기"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "Ethernet 주소 길이"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "왕복 시간"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "파일 전체 크기"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  - id: u7-l02-p06-extra-easy-2
    kind: choice
    difficulty: easy
    prompt: "MSS 크기에 TCP 헤더와 IP 헤더도 포함되나요?"
    choices:
    - id: a
      text: "둘 다 포함된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "TCP 헤더만 포함된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "포함되지 않는다"
      feedback: "MSS는 TCP 데이터 크기를 나타내므로 IP·TCP 헤더는 포함하지 않습니다."
    - id: d
      text: "IP 헤더만 포함된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "헤더 수에 따라 RTT가 된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  - id: u5-l26-p06-q01
    kind: choice
    difficulty: easy
    prompt: "클라이언트가 MSS 1460을 알리면 그 값은 어느 방향 전송의 기준인가요?"
    choices:
    - id: a
      text: "클라이언트에서 서버로 보내는 데이터"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "양방향 모두 고정"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "라우터끼리 보내는 데이터"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "DNS 응답 크기"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "서버에서 클라이언트로 보내는 데이터"
      feedback: "클라이언트의 광고 값은 서버가 클라이언트에게 보낼 때의 기준입니다."
    answer: e
  - id: u5-l26-p06-q02
    kind: choice
    difficulty: easy
    prompt: "양쪽이 광고한 MSS 값은 꼭 같아야 하나요?"
    choices:
    - id: a
      text: "항상 같다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "서로 다를 수 있다"
      feedback: "두 방향에서 광고하는 MSS 값은 서로 다를 수 있습니다."
    - id: c
      text: "서버만 광고할 수 있다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "둘 다 1500이어야 한다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "MSS는 숫자가 아니다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: b
  - id: u7-l02-p06-q03
    kind: choice
    difficulty: easy
    prompt: "1500 − 20 − 20은 얼마인가요?"
    choices:
    - id: a
      text: "1480"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "1500"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "1400"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "1460"
      feedback: "예시에서는 1500에서 IP 헤더 20과 TCP 헤더 20을 빼 1460바이트가 됩니다."
    - id: e
      text: "20"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: d
  - id: u7-l02-p06-extra-hard
    kind: choice
    difficulty: easy
    prompt: "파일이 MSS보다 크면 보통 어떻게 나누어 보낼 수 있나요?"
    choices:
    - id: a
      text: "한 세그먼트에 무조건 모두 담는다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "RTT로 바꾼다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "여러 세그먼트로 나눈다"
      feedback: "MSS보다 큰 데이터는 여러 세그먼트로 나누어 보낼 수 있습니다."
    - id: d
      text: "포트 번호로 바꾼다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "연결을 자동으로 끝낸다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  question_placements:
  - question_id: u7-l02-p06-extra-easy-1
    after_paragraph: 1
  - question_id: u7-l02-p06-extra-easy-2
    after_paragraph: 1
  - question_id: u5-l26-p06-q01
    after_paragraph: 2
  - question_id: u5-l26-p06-q02
    after_paragraph: 2
  - question_id: u7-l02-p06-q03
    after_paragraph: 3
  - question_id: u7-l02-p06-extra-hard
    after_paragraph: 4
- terms:
  - LISTEN
  - ESTABLISHED
  - 소켓(socket)
  illustrations:
  - file: assets/animations/l26-daily-call-states.svg
    title: "전화 상태가 바뀌어요"
    alt: "가게는 벨 기다림 상태이고, 내가 걸면 나는 거는 중, 가게는 벨 울림이 됩니다. “들려요”를 받은 내가 먼저 통화 중이 되고 마지막 대답이 닿으면 가게도 통화 중이 됩니다."
    caption: "받는 쪽은 마지막 대답이 닿은 뒤에 통화 중이 됩니다."
    after_paragraph: -1
  - file: assets/animations/l26-tcp-states.svg
    title: "연결 상태가 바뀌는 순서"
    alt: "서버는 LISTEN에서 시작하고, 클라이언트가 SYN을 보내면 SYN_SENT, 서버는 SYN_RECEIVED가 됩니다. 클라이언트는 SYN+ACK를 받고 먼저 ESTABLISHED가 되며 서버는 마지막 ACK가 닿은 뒤 ESTABLISHED가 됩니다."
    caption: "클라이언트는 SYN_SENT에서 ESTABLISHED로, 서버는 LISTEN과 SYN_RECEIVED를 거쳐 ESTABLISHED로 바뀝니다."
    after_paragraph: 2
  questions:
  - id: u7-l02-p07-extra-easy-1
    kind: choice
    difficulty: easy
    prompt: "TCP의 상태 이름은 무엇을 기록하나요?"
    choices:
    - id: a
      text: "컴퓨터 전체의 전원 상태"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "화면 밝기"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "파일 이름"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "라우터의 위치"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "특정 TCP 연결의 진행 상태"
      feedback: "상태는 특정 TCP 연결이 어디까지 진행됐는지 기록합니다."
    answer: e
  - id: u7-l02-p07-extra-easy-2
    kind: choice
    difficulty: easy
    prompt: "서버가 새 연결 요청을 기다리는 상태는 무엇인가요?"
    choices:
    - id: a
      text: "SYN_SENT"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "LISTEN"
      feedback: "LISTEN은 서버가 연결 요청을 기다리는 상태입니다."
    - id: c
      text: "ESTABLISHED"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "SYN_RECEIVED"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "CLOSED"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: b
  - id: u7-l02-p07-q01
    kind: choice
    difficulty: easy
    prompt: "클라이언트가 SYN을 보낸 직후의 상태는 무엇인가요?"
    choices:
    - id: a
      text: "LISTEN"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "ESTABLISHED"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "CLOSED"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "SYN_SENT"
      feedback: "클라이언트는 SYN을 보낸 뒤 SYN_SENT 상태가 됩니다."
    - id: e
      text: "TIME_WAIT"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: d
  - id: u7-l02-p07-q02
    kind: choice
    difficulty: easy
    prompt: "서버가 SYN을 받은 뒤의 상태는 무엇인가요?"
    choices:
    - id: a
      text: "SYN_RECEIVED"
      feedback: "서버는 SYN을 받으면 SYN_RECEIVED 상태가 됩니다."
    - id: b
      text: "LISTEN만 유지"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "CLOSED"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "ESTABLISHED 이전에 종료"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "TIME_WAIT"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  - id: u7-l02-p07-q03
    kind: choice
    difficulty: easy
    prompt: "클라이언트는 서버의 SYN+ACK를 받은 뒤 어떤 상태가 될 수 있나요?"
    choices:
    - id: a
      text: "LISTEN"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "SYN_SENT"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "CLOSED"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "SYN_RECEIVED"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "ESTABLISHED"
      feedback: "클라이언트는 SYN+ACK를 받고 마지막 ACK를 보내며 ESTABLISHED가 됩니다."
    answer: e
  - id: u7-l02-p07-extra-hard
    kind: choice
    difficulty: easy
    prompt: "서버가 LISTEN 상태에서 연결 하나를 받아들여도 무엇이 가능한가요?"
    choices:
    - id: a
      text: "서버는 즉시 종료된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "모든 포트가 사라진다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "다른 연결은 모두 실패한다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "다른 새 연결 요청도 계속 기다릴 수 있다"
      feedback: "LISTEN 소켓은 새 요청을 기다리고, 연결마다 별도 상태를 관리할 수 있습니다."
    - id: e
      text: "클라이언트가 서버 상태를 지운다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: d
  question_placements:
  - question_id: u7-l02-p07-extra-easy-1
    after_paragraph: 1
  - question_id: u7-l02-p07-extra-easy-2
    after_paragraph: 2
  - question_id: u7-l02-p07-q01
    after_paragraph: 2
  - question_id: u7-l02-p07-q02
    after_paragraph: 2
  - question_id: u7-l02-p07-q03
    after_paragraph: 3
  - question_id: u7-l02-p07-extra-hard
    after_paragraph: 4
- terms:
  - Virtual Circuit(가상 회선)
  illustrations:
  - file: assets/animations/l26-daily-no-new-wire.svg
    title: "통화 중은 새 전선이 아니에요"
    alt: "나와 친구 사이에 여러 기지국이 있습니다. 양쪽이 통화 중이라고 기록하지만 새 전용선은 깔리지 않고 목소리는 이미 있는 통신망을 지나가며, 통화 중이라는 것이 용건 처리를 뜻하지는 않는다고 표시됩니다."
    caption: "통화 중은 새 전선이 아니라 양쪽이 기록해 둔 상태입니다."
    after_paragraph: -1
  - file: assets/animations/l26-virtual-circuit.svg
    title: "TCP 연결은 논리적인 관계예요"
    alt: "클라이언트와 서버 사이에 여러 라우터가 있습니다. 양 끝은 ESTABLISHED 상태와 상대 주소·포트, 순서번호, MSS를 기록하지만 새 케이블이나 전용선은 생기지 않고, 데이터는 기존 네트워크로 갑니다. 연결 수립이 앱의 처리 성공을 뜻하지는 않습니다."
    caption: "TCP 연결은 양 끝이 상태를 기록해 둔 논리적 관계입니다. 연결이 수립되었다고 앱이 데이터를 처리했다는 뜻은 아닙니다."
    after_paragraph: 1
  questions:
  - id: u7-l02-p08-extra-easy-1
    kind: choice
    difficulty: easy
    prompt: "세 메시지를 주고받은 뒤 TCP 양 끝은 무엇을 하기 시작하나요?"
    choices:
    - id: a
      text: "새 전용 케이블을 설치한다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "웹 앱의 처리를 보장한다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "연결 상태를 관리한다"
      feedback: "양 끝 TCP는 서로의 연결 정보를 알고 연결 상태를 관리합니다."
    - id: d
      text: "라우터를 끈다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "IP 주소를 지운다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  - id: u7-l02-p08-extra-easy-2
    kind: choice
    difficulty: easy
    prompt: "TCP 연결이 생기면 컴퓨터 사이에 새 전용 케이블이 설치되나요?"
    choices:
    - id: a
      text: "예, 항상 설치된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "아니요, 새 전용 케이블이 생기는 것은 아니다"
      feedback: "TCP 연결은 새 물리 케이블을 설치한다는 뜻이 아닙니다."
    - id: c
      text: "서버에만 설치된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "라우터마다 한 개씩 설치된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "파일 크기에 따라 설치된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: b
  - id: u7-l02-p08-q01
    kind: choice
    difficulty: easy
    prompt: "TCP 연결이 “논리적인 관계”라는 설명은 무엇을 뜻하나요?"
    choices:
    - id: a
      text: "양 끝이 통신 상태를 기록해 관리한다"
      feedback: "논리적 연결은 양 끝 TCP가 통신 상태를 기록해 관리하는 관계입니다."
    - id: b
      text: "통신 전용 선로가 새로 깔린다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "라우터가 앱 데이터를 처리한다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "IP 패킷이 더는 필요 없다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "서버가 파일을 모두 전송했다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  - id: u7-l02-p08-q02
    kind: choice
    difficulty: easy
    prompt: "전화의 “통화 중” 비유에서 실제로 새로 생기지 않는 것은 무엇인가요?"
    choices:
    - id: a
      text: "전용 케이블"
      feedback: "통화 중이어도 두 전화기 사이에 전용 케이블이 새로 깔리지는 않습니다."
    - id: b
      text: "통화 상태"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "서로 통신한다는 사실"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "양 끝의 기록"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "기존 통신망 사용"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: a
  - id: u7-l02-p08-q03
    kind: choice
    difficulty: easy
    prompt: "TCP 데이터는 연결이 된 뒤에도 무엇을 통해 네트워크를 지나가나요?"
    choices:
    - id: a
      text: "새 전용 케이블만"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "DNS 이름만"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "IP 패킷과 링크 프레임"
      feedback: "연결 뒤 데이터도 IP 패킷과 링크 프레임으로 네트워크를 통과합니다."
    - id: d
      text: "MSS 숫자만"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "LISTEN 상태만"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    answer: c
  - id: u7-l02-p08-extra-hard
    kind: choice
    difficulty: easy
    prompt: "TCP 연결이 수립되면 서버 애플리케이션이 요청을 처리했다고 확정되나요?"
    choices:
    - id: a
      text: "예, 반드시 처리했다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: b
      text: "서버가 자동으로 파일을 저장한다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: c
      text: "연결이 바로 종료된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: d
      text: "RTT가 0이 된다"
      feedback: "바로 앞 문단의 설명에서 이 부분을 다시 확인해 보세요."
    - id: e
      text: "아니요, 앱의 처리 성공과는 별개다"
      feedback: "연결 수립은 애플리케이션의 요청 처리 성공을 뜻하지 않습니다."
    answer: e
  question_placements:
  - question_id: u7-l02-p08-extra-easy-1
    after_paragraph: 1
  - question_id: u7-l02-p08-extra-easy-2
    after_paragraph: 1
  - question_id: u7-l02-p08-q01
    after_paragraph: 2
  - question_id: u7-l02-p08-q02
    after_paragraph: 3
  - question_id: u7-l02-p08-q03
    after_paragraph: 3
  - question_id: u7-l02-p08-extra-hard
    after_paragraph: 4
animations_dir: units/05-tcp-and-udp/lessons/02-tcp-연결과정/assets/animations
additional_sources:
- https://studio.futurereadycampus.com/course-network/wiki/oeweo-network/lesson-26.html
- https://github.com/FutureReadyCampus/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/04-2.md
- https://www.rfc-editor.org/rfc/rfc9293.html
---
앞 Lesson에서 TCP와 UDP의 역할을 비교했다. 이번 Lesson에서는 웹 서버에 접속하는 예를 따라가며 TCP 연결이 어떤 메시지로 시작되는지 살펴본다. 먼저 세 메시지 전체를 보고, 이어서 RTT·순서번호·MSS·연결 상태를 차례로 읽는다.

## 3-way handshake의 의미
<!-- learn-page-id: handshake-meaning -->

TCP 연결을 준비할 때는 바로 파일이나 웹 요청부터 보내지 않는다. 먼저 양쪽 TCP가 서로 메시지를 주고받을 수 있는지 확인하고, 각자 사용할 시작 번호 같은 정보를 알린다. 이 준비 과정을 3-way handshake(쓰리웨이 핸드셰이크)라고 부른다. 세 개의 메시지가 오가기 때문에 ‘세 번의 악수’라고 기억하면 된다.

전화 통화를 떠올려 보자. 한쪽이 “여보세요?”라고 부르고, 상대가 “네, 들려요. 그쪽도 들리나요?”라고 답한 다음, 첫 번째 사람이 “네, 들립니다”라고 확인한다. TCP의 세 메시지도 요청, 응답 겸 요청, 마지막 확인으로 이어진다. 전화 비유는 서로 확인을 주고받는다는 점에만 해당하며, TCP가 실제 음성을 듣는 것은 아니다.

두 컴퓨터를 세로선으로 그린 그림에서는 위에서 아래로 시간이 흐른다. 화살표가 왼쪽에서 오른쪽으로 가면 클라이언트가 서버로 보내는 메시지이고, 오른쪽에서 왼쪽으로 오면 서버가 답하는 메시지다. 다음 페이지부터 각 화살표에 어떤 정보가 담기는지 살펴본다.

세 번인 이유는 양쪽이 각자의 시작 번호를 알리고, 상대의 번호를 받았다는 확인도 돌려주기 때문이다. 두 번째 메시지에는 서버의 응답과 서버 자신의 연결 요청이 함께 담긴다. 세 번째 메시지는 그 서버 요청이 클라이언트에 도착했음을 서버에 알려 준다. 이 절차가 끝나도 웹 서버가 요청을 처리했거나 파일 전송이 성공했다는 뜻은 아니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP는 데이터를 보내기 전에 SYN, SYN+ACK, ACK 세 메시지로 연결 준비를 확인한다.
- **적용하기 (Apply):** 시간축 그림에서 누가 먼저 연결을 요청했는지와 각 메시지 방향을 설명한다.
- **찾아보기 (Lookup):** 세 메시지에 담긴 구체적인 정보는 다음 페이지부터 따라간다.

## 연결 요청과 RTT
이제 예를 하나 정해 전체 절차를 따라가 보자. 노트북에서 `192.168.0.20` 주소를 가진 일반 HTTP 웹 서버의 TCP 80번 포트에 연결을 요청한다고 하자. IP 주소가 목적지 컴퓨터를 가리킨다면, 포트 번호는 그 컴퓨터 안에서 통신할 프로그램의 접점을 구분한다. 포트는 케이블을 꽂는 장비의 물리 포트와 다른 개념이다. 포트가 어느 프로그램을 가리키는지에 대한 복습은 [앞 Lesson의 포트 설명](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/7/lesson/1/page/2)에서 확인할 수 있다.

메시지를 보내고 응답이 돌아올 때까지 걸리는 시간을 RTT(Round Trip Time), 즉 왕복 시간이라고 한다. RTT가 50ms라면 1초의 1000분의 50, 다시 말해 0.05초다. [Unit 6 Lesson 4에서 배운 ping과 RTT](https://futurereadycampus.github.io/learn-course-network-foundations/m2-network/unit/6/lesson/4/page/2)는 네트워크 왕복 시간을 확인하는 예다.

이 Lesson의 그림에서는 계산을 쉽게 하려고 RTT 50ms를 가는 데 25ms, 돌아오는 데 25ms로 나누고 서버 처리 시간은 0으로 둔다. 실제 경로는 양방향 시간이 다를 수 있고 서버 처리 시간도 들기 때문에, 25ms씩이라는 값은 이 예를 위한 단순화다. 현실의 왕복 시간을 항상 반으로 나눌 수 있는 것은 아니다.

TCP 연결을 준비하는 동안에도 TCP 세그먼트가 오간다. 다만 이때 세그먼트의 주된 목적은 파일 내용을 전달하는 것이 아니라 연결에 필요한 정보를 주고받는 것이다. 왕복 시간이 길수록 이 준비를 기다리는 시간도 길어질 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** RTT는 요청을 보내고 응답이 돌아오기까지의 왕복 시간이다.
- **적용하기 (Apply):** 연결 준비에도 네트워크 지연이 들어감을 예시의 50ms에 적용한다.
- **찾아보기 (Lookup):** 실제 왕복 시간은 Unit 6 Lesson 4의 ping과 RTT에서 확인한다.

## 연결 제어용 Segment
<!-- learn-page-id: syn-segment -->

TCP는 연결 요청도 TCP 세그먼트에 담아 보낸다. 여기서 다루는 단순한 예에서는 세그먼트에 IP 헤더와 TCP 헤더가 있고, 애플리케이션이 보낼 파일 내용인 Payload(페이로드)는 없다. 세그먼트가 오가지만, 이 메시지는 사진이나 웹 페이지를 나르는 대신 연결을 준비하는 정보 전달에 쓰인다.

첫 번째 메시지에서 TCP 헤더의 SYN 표시를 켠다. SYN은 순서번호를 서로 맞추기 시작하자는 제어 표시다. “연결을 시작하고 싶다”는 요청과 함께 보내는 쪽은 자신이 사용할 초기 순서번호를 알린다. SYN은 연결 절차를 나타내는 표지이면서 순서번호 흐름에서 한 자리를 차지한다. 그래서 다음 페이지의 확인 번호가 같은 숫자로 돌아오지 않는다.

이 예에서는 클라이언트가 초기 순서번호를 1000이라고 정했다고 하자. 실제 시작 번호가 항상 1000인 것은 아니며, 1000은 계산을 쉽게 따라가기 위한 예시다. 책의 쪽번호처럼 순서를 가리키는 정보라고 생각하면 된다. TCP가 데이터 바이트의 위치를 번호로 다루는 방법은 Unit 8에서 더 자세히 살펴본다.

따라서 첫 SYN을 짧게 읽으면 “연결을 시작하고, 내 시작 번호는 1000이다”가 된다. 이 예에서 요청 세그먼트에는 웹 요청 본문이나 파일 바이트가 담기지 않는다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** SYN은 TCP 연결 시작을 알리는 제어 표시이고, Payload는 애플리케이션 데이터다.
- **적용하기 (Apply):** 연결 제어 메시지와 파일 데이터가 담긴 세그먼트를 구분한다.
- **찾아보기 (Lookup):** TCP 헤더의 제어 비트는 TCP 표준과 헤더 설명에서 확인한다.

## 처음 사용할 순서번호
<!-- learn-page-id: ack-sequence -->

클라이언트가 SYN과 초기 순서번호 1000을 보냈으니, 서버는 그 번호를 받았다는 표시를 돌려준다. 이때 쓰는 ACK(Acknowledgment, 확인 응답)는 단순히 “받았다”라고만 말하는 표지가 아니다. ACK 번호는 다음에 받고 싶은 순서번호를 가리킨다.

클라이언트가 SYN 1000을 보냈을 때 서버가 ACK 1001을 보내는 이유는 SYN 자체가 번호 흐름에서 한 자리를 차지하기 때문이다. 세그먼트에 애플리케이션 데이터가 없어도 연결 요청을 나타내는 SYN에는 순서번호가 배정된다. 따라서 1000 다음에 기대하는 번호는 1001이다. 책갈피에 방금 읽은 쪽이 아니라 다음에 펼칠 쪽을 적는 모습과 비슷하다.

번호는 두 방향에 각각 있다. 클라이언트가 시작 번호를 정하듯 서버도 자기 쪽에서 사용할 시작 번호를 정한다. 서버는 클라이언트의 시작 번호를 확인하면서 자신의 번호도 다음 메시지에 함께 알린다.

여기서 필요한 구분은 ACK 표시와 ACK 번호다. ACK 표시가 켜졌다는 것은 헤더의 확인 번호를 사용한다는 뜻이고, 그 번호는 상대에게서 다음으로 받고 싶은 위치를 가리킨다. 이후 데이터가 오갈 때의 번호 계산은 이 페이지에서 외우지 않고 Unit 8에서 다룬다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** ACK 번호는 상대가 다음으로 받을 순서번호를 나타낸다.
- **적용하기 (Apply):** SYN 1000 뒤에 확인 번호 1001이 오는 이유를 말한다.
- **찾아보기 (Lookup):** 데이터 바이트의 순서번호 계산은 Unit 8에서 확인한다.

## SYN과 ACK의 교환
이제 서버의 시작 번호를 4000이라고 두고 세 메시지를 차례로 읽어 보자. 숫자는 설명을 위한 예시이며 실제 연결마다 다르다.

1. **클라이언트 → 서버: SYN, 순서번호 1000.** “연결을 시작하고 싶습니다. 제 시작 번호는 1000입니다.”
2. **서버 → 클라이언트: SYN+ACK, 순서번호 4000, 확인 번호 1001.** “1000을 받았습니다. 다음 번호 1001을 기다립니다. 제 시작 번호는 4000입니다.” 서버의 SYN과 클라이언트 요청에 대한 ACK가 한 세그먼트에 함께 들어 있다.
3. **클라이언트 → 서버: ACK, 확인 번호 4001.** “서버의 시작 번호 4000을 받았습니다. 다음에는 4001을 기대합니다.”

세 번째 메시지가 서버에 도착하면 서버도 자신이 보낸 SYN이 클라이언트에 도착했다는 사실을 확인한다. 클라이언트는 SYN+ACK를 받은 뒤 연결이 준비되었다고 판단할 수 있고, 서버는 마지막 ACK를 받아야 같은 상태에 도달한다. 따라서 양 끝에서 연결 완료를 판단하는 시점은 정확히 같지 않다.

앞 페이지의 단순한 RTT 예시를 그대로 적용하면 클라이언트는 첫 메시지를 보낸 뒤 약 50ms에 서버의 SYN+ACK를 받는다. 마지막 ACK가 서버에 도착하는 시점은 그 뒤 편도 시간인 약 25ms 후다. 실제 지연과 서버 처리 시간은 다를 수 있으므로, 이 계산은 양쪽의 판단 시점이 다를 수 있다는 점을 보여 주는 예시다.

정리하면 두 번째 메시지는 “상대 요청 확인”과 “내 연결 요청”을 한 번에 수행하고, 세 번째 메시지는 그 요청을 다시 확인한다. 그래서 세 메시지로 양쪽의 시작 번호 교환과 확인이 이루어진다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** SYN+ACK는 상대의 SYN을 확인하면서 자기 쪽 SYN도 함께 보낸다.
- **적용하기 (Apply):** 예시 값 1000과 4000으로 세 메시지의 역할을 차례로 설명한다.
- **찾아보기 (Lookup):** 실제 연결 캡처의 필드 값은 패킷 분석 도구에서 확인한다.

## MSS 등 통신 조건 교환
<!-- learn-page-id: mss-exchange -->

연결을 시작할 때 각 TCP는 자기 쪽의 시작 번호뿐 아니라 데이터를 받을 때 지킬 수 있는 조건도 알릴 수 있다. 대표적인 값이 MSS(Maximum Segment Size, 최대 세그먼트 크기)다. MSS는 한 TCP 세그먼트에 실을 수 있는 **TCP 데이터의 최대 크기**를 바이트로 나타낸다. TCP 헤더와 IP 헤더는 이 데이터 크기에 포함되지 않는다.

SYN에서 MSS를 알린 쪽은 “상대가 나에게 보낼 때 TCP 데이터는 이 크기 이하로 해 달라”고 알려 준다. 따라서 클라이언트가 MSS 1460을 광고하면 서버가 클라이언트로 보낼 데이터 크기의 기준이 되고, 서버가 MSS 1400을 광고하면 클라이언트가 서버로 보낼 데이터 크기의 기준이 된다. 양방향 값은 서로 다를 수 있다.

익숙한 예로 MTU가 1500바이트인 IPv4 링크를 생각해 보자. 기본 IPv4 헤더 20바이트와 옵션 없는 TCP 헤더 20바이트를 가정하면 `1500 − 20 − 20 = 1460`바이트가 TCP 데이터 크기의 한 예가 된다. 이 숫자는 조건을 단순화한 예다. 헤더 옵션이나 경로의 MTU에 따라 실제로 보낼 수 있는 크기는 더 작아질 수 있다.

파일이 1460바이트보다 크면 한 세그먼트에 모두 넣는 대신 여러 세그먼트로 나눌 수 있다. MSS는 파일 전체의 최대 크기도, 초당 전송 속도도 아니다. 상대가 받을 수 있다고 알린 크기와 경로 조건에 맞춰 송신 측이 한 세그먼트의 데이터 양을 조절할 때 쓰는 기준이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** MSS는 한 TCP 세그먼트에서 받을 수 있는 데이터의 최대 크기를 알리는 값이다.
- **적용하기 (Apply):** 각 방향의 송신자는 상대가 광고한 MSS를 기준으로 데이터 크기를 조절한다.
- **찾아보기 (Lookup):** MSS 옵션과 경로 크기 조정은 TCP 표준과 패킷 캡처에서 확인한다.

## 연결 과정의 상태 변화
TCP는 연결 절차가 어디까지 진행되었는지 상태 이름으로 기록한다. 여기서 상태는 컴퓨터 전체의 상태가 아니라 특정 TCP 연결을 관리하는 TCP의 진행 표지다. `netstat` 같은 도구에서 보이는 ESTABLISHED는 연결이 수립된 상태를 나타내는 이름이다.

서버 프로그램은 먼저 소켓을 열어 연결을 기다린다. 이 대기 상태가 LISTEN이다. 클라이언트가 연결을 요청해 SYN을 보내면 클라이언트 쪽은 SYN_SENT가 된다. 서버는 SYN을 받으면 SYN_RECEIVED로 바뀌고, SYN+ACK를 보낸 뒤 마지막 ACK를 기다린다.

클라이언트는 서버의 SYN+ACK를 받고 마지막 ACK를 보내면 ESTABLISHED(연결이 수립된 상태)가 된다. 서버는 그 마지막 ACK가 도착한 뒤 ESTABLISHED가 된다. `l26-tcp-states.svg`에서 두 컴퓨터의 상태 이름표가 메시지 교환에 따라 바뀌는 모습을 이 순서와 함께 보자. 모든 상태 이름을 외우기보다 LISTEN은 기다림, ESTABLISHED는 연결 수립 완료라는 큰 차이를 우선 기억하면 된다.

서버에서 LISTEN 중인 소켓과 연결을 마친 소켓도 구분해야 한다. 서버는 LISTEN 상태로 새로운 요청을 계속 기다릴 수 있고, 연결을 수락한 뒤에는 그 클라이언트와 통신할 별도의 연결 상태를 관리한다. 따라서 연결 하나가 ESTABLISHED가 되었다고 서버가 다른 연결을 더 받을 수 없다는 뜻은 아니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** LISTEN은 연결을 기다리는 상태이고 ESTABLISHED는 연결이 수립된 상태다.
- **적용하기 (Apply):** 클라이언트와 서버가 서로 다른 순서로 상태를 바꾸는 까닭을 설명한다.
- **찾아보기 (Lookup):** SYN_SENT와 SYN_RECEIVED의 전체 전이는 상태도나 운영체제 도구에서 확인한다.

## 연결의 의미 정리
<!-- learn-page-id: virtual-circuit-definition -->
세 번의 메시지를 주고받으면 TCP 양 끝은 서로의 연결 시작 번호를 알고, 연결 상태를 관리하기 시작한다. 이때 “연결되었다”는 말은 두 컴퓨터 사이에 새 케이블을 연결하거나 통신 전용 선로를 예약했다는 뜻이 아니다.

TCP 연결은 이미 있는 네트워크를 통해 두 끝점이 통신에 필요한 상태를 기록해 두는 논리적인 관계다. 양쪽 운영체제의 TCP가 상대 주소와 포트, 순서번호와 협의한 전송 조건 등을 연결 상태로 관리한다. 이처럼 물리적인 전선이 아니라 양 끝의 규칙과 기록으로 성립하는 연결을 Virtual Circuit(가상 회선) 또는 논리적 연결이라고 부르기도 한다.

전화의 “통화 중” 표시를 떠올리면 이해하기 쉽다. 통화가 시작되어도 두 전화기 사이에 전용 케이블이 새로 깔리는 것은 아니다. 다만 이 비유는 통신 중이라는 상태가 있다는 점에만 해당한다. 실제 TCP 데이터는 연결 후에도 IP 패킷과 링크 프레임으로 네트워크를 통과한다.

이번 Lesson은 연결 준비에 집중했다. 다음 Lesson에서는 연결을 어떻게 끝내고 상태를 정리하는지 살펴본다. 연결이 수립되었다는 사실은 애플리케이션이 데이터를 성공적으로 처리했다는 확인과 다르며, 데이터 전달 중의 확인·재전송·수신 여유 공간은 Unit 8에서 자세히 다룬다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TCP 연결은 물리 전용선이 아니라 양 끝의 TCP가 관리하는 논리적 관계다.
- **적용하기 (Apply):** 연결 수립과 애플리케이션 데이터 처리 성공을 구별한다.
- **찾아보기 (Lookup):** 연결 종료 과정은 다음 Lesson, 데이터 전달의 세부 동작은 Unit 8에서 살펴본다.