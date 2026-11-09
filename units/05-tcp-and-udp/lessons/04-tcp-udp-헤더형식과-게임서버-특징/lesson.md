---
id: u5-l28-tcp-udp-헤더형식과-게임서버-특징
title: TCP와 UDP 헤더는 무엇이 다르고, 게임은 왜 UDP를 쓸까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-28.md
wiki_diagram: units/05-tcp-and-udp/lessons/04-tcp-udp-헤더형식과-게임서버-특징/assets/diagrams/lesson-28.svg
page_metadata:
- terms: []
  question_placements:
  - question_id: u8-l02-p01-q01
    after_paragraph: 1
  - question_id: u8-l02-p01-q02
    after_paragraph: 2
  questions:
  - id: u8-l02-p01-q01
    kind: choice
    difficulty: easy
    prompt: TCP나 UDP 헤더는 전송할 데이터와 어떤 관계인가요?
    choices:
    - id: a
      text: 헤더는 내용 앞에 붙는 안내 정보이고, 사진이나 문서 내용 자체는 따로 있습니다
      feedback: 맞아요. 헤더는 전달에 필요한 정보를 담고 사진·문서 같은 내용 그 자체와 구분됩니다.
    - id: b
      text: 헤더는 사진이나 문서의 내용을 압축해 저장한 부분입니다
      feedback: 본문은 헤더를 압축된 내용이 아니라 전달에 필요한 안내 정보로 설명합니다.
    - id: c
      text: 헤더는 데이터가 도착한 뒤 수신 프로그램이 새로 붙이는 표시입니다
      feedback: 헤더는 전송할 데이터 앞에 붙어 함께 전달됩니다. 도착한 뒤 수신 프로그램이 만드는 정보가 아닙니다.
    - id: d
      text: 헤더와 데이터는 같은 내용을 두 번 적어 둔 것입니다
      feedback: 둘은 같은 내용을 반복하지 않습니다. 헤더는 전달 정보를, 데이터는 실제 내용을 담습니다.
    - id: e
      text: 헤더는 목적지 컴퓨터의 화면에 표시되는 제목입니다
      feedback: 헤더는 화면 제목이 아니라 통신에 필요한 정보를 담는 부분입니다.
    answer: a
  - id: u8-l02-p01-q02
    kind: choice
    difficulty: medium
    prompt: 헤더의 각 정보가 답하는 질문을 올바르게 연결한 것은 무엇인가요?
    choices:
    - id: a
      text: 포트 번호는 바이트의 순서를, 순서 번호와 ACK는 받을 프로그램을 가리킵니다
      feedback: 두 역할이 뒤바뀌었습니다. 포트는 통신 프로그램을 구분하고 순서 번호·ACK는 바이트 흐름을 나타냅니다.
    - id: b
      text: 포트 번호는 내용의 종류를, 순서 번호는 목적지 컴퓨터를 가리킵니다
      feedback: 본문은 포트 번호를 받을 프로그램과 연결하고, 순서 번호를 바이트 흐름의 진행과 연결합니다.
    - id: c
      text: 순서 번호는 사진 파일의 이름을, ACK는 데이터의 암호화 여부를 나타냅니다
      feedback: 본문에서 순서 번호와 ACK는 TCP 바이트 흐름의 위치와 다음에 기대하는 위치를 나타냅니다.
    - id: d
      text: 포트 번호는 받을 프로그램을, 순서 번호와 ACK는 바이트 흐름의 진행을 나타냅니다
      feedback: 맞아요. 뒤 페이지에서 이 안내 정보들이 포트와 TCP 바이트 순서에서 어떻게 쓰이는지 살펴봅니다.
    - id: e
      text: 포트와 순서 번호는 모두 데이터가 손상됐는지만 확인합니다
      feedback: 손상 확인은 Checksum의 역할입니다. 포트는 프로그램을 찾고 순서 번호·ACK는 바이트 진행을 나타냅니다.
    answer: d
  illustrations:
  - file: assets/illustrations/tcp-udp-header-overview.svg
    title: TCP와 UDP 헤더의 정보 비교
    alt: TCP는 포트, 순서 번호, 확인 응답, 제어 플래그, Window와 검사합 등을 담고, UDP는 출발지 포트·목적지 포트·길이·검사합을 담는 구조 비교 그림입니다.
    caption: TCP와 UDP 헤더를 나란히 보고, 각 필드가 답하는 질문을 뒤 페이지에서 하나씩 살펴봅니다.
    after_paragraph: 0
  - file: assets/animations/l28-daily-waybill-fields.svg
    title: "송장은 상자 겉에 붙는 안내예요"
    alt: "상자 속 물건과 겉에 붙는 송장이 구분되고, 송장의 받는 곳, 접수·수령 번호, 보관함 여유, 파손 점검 스티커 칸이 각각 누구에게 가는지, 어디까지 받았는지, 얼마나 더 받을 수 있는지, 가다가 상했는지에 답한다고 표시됩니다."
    caption: "송장은 상자 속 내용이 아니라 겉에 붙는 안내입니다. 칸마다 하나의 질문에 답하며 모든 칸을 외우는 표가 아닙니다."
    after_paragraph: 1
  - file: assets/animations/l28-header-fields-questions.svg
    title: "헤더 칸은 질문에 답해요"
    alt: "내용 앞에 붙는 헤더의 칸을 포트 번호, 순서 번호·ACK, Window, Checksum 순서로 보며 각각 어느 프로그램으로 가는지, 바이트 흐름이 어디까지인지, 얼마나 더 받을 수 있는지, 전송 중 손상됐는지에 답하는 칸으로 연결합니다."
    caption: "헤더는 외울 표가 아니라 전송에 필요한 안내 정보를 찾아 읽는 지도입니다. 어떤 질문에 답하는 칸인지 알면 됩니다."
    after_paragraph: 1
  illustration_after_paragraph: [-1]
- terms:
  - 포트 번호 (Port Number)
  - Well-known Port
  animations:
  - file: l28-port-apartment.svg
    title: IP는 건물, 포트는 호수
    alt: 데이터 상자가 건물 모양 컴퓨터에 도착한 뒤, 목적지 포트 80이 적힌 호수의 문으로 들어가는 장면입니다.
    caption: IP 주소가 컴퓨터를 찾으면 포트 번호가 그 컴퓨터 안에서 받을 프로그램을 구분합니다.
  question_placements:
  - question_id: u8-l02-p02-q01
    after_paragraph: 1
  - question_id: u8-l02-p02-q02
    after_paragraph: 3
  questions:
  - id: u8-l02-p02-q01
    kind: choice
    difficulty: easy
    prompt: IP 주소가 컴퓨터에 도착한 뒤 포트 번호는 무엇을 찾는 데 쓰이나요?
    choices:
    - id: a
      text: 컴퓨터가 연결된 건물의 실제 위치
      feedback: 네트워크에서 컴퓨터를 찾는 데는 IP 주소를 씁니다. 포트 번호는 그 컴퓨터 안의 통신 프로그램을 구분합니다.
    - id: b
      text: 그 컴퓨터에서 데이터를 받을 통신 프로그램
      feedback: 맞아요. IP 주소가 컴퓨터를 찾으면 포트 번호가 그 안에서 받을 프로그램을 구분합니다.
    - id: c
      text: 데이터가 바이트 흐름에서 차지하는 순서
      feedback: 바이트의 위치는 TCP 순서 번호와 관련됩니다. 포트 번호는 받을 프로그램을 찾습니다.
    - id: d
      text: 네트워크 경로가 현재 붐비는 정도
      feedback: 경로의 혼잡은 혼잡 제어가 살피는 문제입니다. 포트 번호는 통신 프로그램을 구분합니다.
    - id: e
      text: 데이터 내용이 전송 중 바뀌었는지 여부
      feedback: 데이터 손상 확인에는 Checksum이 쓰입니다. 포트 번호는 컴퓨터 안에서 프로그램을 구분합니다.
    answer: b
  - id: u8-l02-p02-q02
    kind: choice
    difficulty: medium
    prompt: 브라우저가 임시 포트 51514에서 HTTPS 서버 포트 443으로 요청을 보냈다면, 응답의 목적지 포트는 보통 무엇이 되나요?
    choices:
    - id: a
      text: 응답에서도 서버의 목적지였던 443입니다
      feedback: 응답을 보낼 때 양 끝의 역할이 반대로 보입니다. 응답의 목적지는 요청을 보낸 브라우저 쪽 포트입니다.
    - id: b
      text: 출발지와 목적지 포트가 모두 443입니다
      feedback: 응답은 브라우저의 통신 포트로 돌아가므로 두 포트가 모두 443이 되는 것은 아닙니다.
    - id: c
      text: 매번 고정되는 HTTP 포트 80입니다
      feedback: 포트 80은 HTTP에서 흔히 쓰는 기본값입니다. 이 사례의 HTTPS 응답은 브라우저가 사용한 포트로 돌아갑니다.
    - id: d
      text: 포트 번호가 필요하지 않으므로 값이 없습니다
      feedback: 포트는 컴퓨터 안의 통신 프로그램을 구분합니다. 응답도 요청을 보낸 프로그램에 전달되어야 합니다.
    - id: e
      text: 요청에서 브라우저가 사용한 51514입니다
      feedback: 맞아요. 요청에서 출발지였던 브라우저 포트가 응답에서는 목적지가 됩니다.
    answer: e
  illustrations:
  - file: assets/animations/l28-daily-apartment-reply.svg
    title: "답장에서는 보낸 호수와 받는 호수가 바뀌어요"
    alt: "건물은 컴퓨터를, 호수는 그 안의 프로그램을 가리킵니다. 요청은 우리 집 1203호에서 가게 502호로 가고, 답장에서는 가게 502호가 보낸 곳, 1203호가 받는 곳이 됩니다. 대표 호수는 약속이라 다른 번호를 쓸 수도 있습니다."
    caption: "IP 주소는 컴퓨터를, 포트 번호는 그 안의 프로그램을 찾습니다. 호수 번호는 예시입니다."
    after_paragraph: 2
  - file: assets/animations/l28-ports-swap-on-reply.svg
    title: "응답에서는 출발지와 목적지 포트가 바뀌어요"
    alt: "클라이언트의 포트 51514에서 웹 서버의 포트 443으로 요청이 가고, 응답에서는 443이 출발지, 51514가 목적지가 됩니다. 80과 443은 HTTP와 HTTPS의 흔한 기본 포트이고 다른 번호도 설정할 수 있다고 표시됩니다."
    caption: "응답에서는 요청의 출발지 포트가 목적지 포트가 됩니다. 포트 51514와 443은 예시입니다."
    after_paragraph: 2
  illustration_after_paragraph: [0]
- terms:
  - Sequence Number
  - ACK (Acknowledgement)
  - Data Offset
  - 제어 플래그 (Control Flag)
  - RST (Reset)
  - Checksum (검사합)
  question_placements:
  - question_id: u8-l02-p03-q01
    after_paragraph: 1
  - question_id: u8-l02-p03-q02
    after_paragraph: 2
  - question_id: u8-l02-p03-q03
    after_paragraph: 3
  questions:
  - id: u8-l02-p03-q01
    kind: choice
    difficulty: easy
    prompt: TCP 헤더의 순서 번호(Sequence Number)는 무엇을 나타내나요?
    choices:
    - id: a
      text: 다음에 데이터를 받을 프로그램의 포트
      feedback: 받을 프로그램은 포트 번호로 구분합니다. 순서 번호는 보낸 바이트 흐름의 위치를 나타냅니다.
    - id: b
      text: 전체 데이터가 상대에게 도착할 때까지 걸린 시간
      feedback: 순서 번호는 시간을 나타내지 않습니다. 바이트 흐름에서 데이터가 시작하는 위치를 나타냅니다.
    - id: c
      text: 보낸 데이터가 바이트 흐름에서 시작하는 위치
      feedback: 맞아요. 순서 번호는 보낸 데이터가 바이트 흐름의 어디에서 시작하는지 나타냅니다.
    - id: d
      text: 수신 버퍼에 남아 있는 빈 공간의 양
      feedback: 수신 버퍼의 여유는 Window 값으로 알립니다. 순서 번호는 바이트 흐름의 위치를 나타냅니다.
    - id: e
      text: 데이터가 전송 중 손상됐는지 확인한 결과
      feedback: 손상 확인에는 Checksum을 씁니다. 순서 번호는 바이트 흐름의 위치를 나타냅니다.
    answer: c
  - id: u8-l02-p03-q02
    kind: choice
    difficulty: medium
    prompt: 설명을 위해 1000번 바이트부터 100바이트를 보냈습니다. 모두 받았다는 TCP ACK는 다음에 기대하는 몇 번 바이트를 가리킬 수 있나요?
    choices:
    - id: a
      text: 1100번
      feedback: 맞아요. 1000번부터 1099번까지 받았으므로 다음에 기대하는 바이트는 1100번입니다.
    - id: b
      text: 1000번
      feedback: 1000번은 이 데이터의 첫 바이트입니다. 모두 받았다면 다음에 기대하는 위치는 1100번입니다.
    - id: c
      text: 1099번
      feedback: 1099번은 받은 범위의 마지막 바이트입니다. ACK는 그다음에 기대하는 1100번을 가리킬 수 있습니다.
    - id: d
      text: 100번
      feedback: 100은 보낸 바이트 수입니다. ACK는 길이가 아니라 다음에 기대하는 바이트 위치를 나타냅니다.
    - id: e
      text: ACK에는 순서 위치가 아니라 포트 번호만 들어갑니다
      feedback: ACK 번호는 다음에 기대하는 바이트 위치를 나타냅니다. 포트 번호와는 다른 헤더 정보입니다.
    answer: a
  - id: u8-l02-p03-q03
    kind: choice
    difficulty: medium
    prompt: TCP Checksum(검사합)이 확인하는 범위에 대해 맞는 설명은 무엇인가요?
    choices:
    - id: a
      text: 확인 응답을 받았으므로 데이터가 상대 앱에서 올바르게 처리됐는지 보장합니다
      feedback: Checksum은 손상 확인에 쓰이며, 상대 앱이 데이터를 올바르게 처리했는지까지 보장하지는 않습니다.
    - id: b
      text: 데이터가 목적지에 반드시 도착했는지 확인합니다
      feedback: 도착 자체를 보장하지 않습니다. Checksum은 전송 중 손상 여부를 확인하는 데 쓰입니다.
    - id: c
      text: 바이트의 순서와 다음에 기대하는 위치를 정합니다
      feedback: 바이트 위치는 순서 번호와 ACK가 나타냅니다. Checksum은 손상 확인에 쓰입니다.
    - id: d
      text: 헤더와 데이터가 전송 중 손상됐는지 확인하는 데 쓰입니다
      feedback: 맞아요. Checksum은 손상 여부를 확인하는 데 쓰이지만 도착이나 의미까지 보장하지는 않습니다.
    - id: e
      text: 수신 버퍼에 남은 공간을 송신 측에 알립니다
      feedback: 수신 버퍼 여유는 Window가 알립니다. Checksum은 헤더와 데이터의 손상 확인에 쓰입니다.
    answer: d
  illustrations:
  - file: assets/animations/l28-daily-page-numbers-signals.svg
    title: "쪽번호와 신호 카드"
    alt: "원고 1000쪽부터 100쪽을 보내면 다음에 받을 쪽은 1100쪽이고, 신호 카드로 시작, 마침, 확인, 처음부터 다시를 알립니다. 안내문이 끝나는 곳을 표시하는 표지와 파손 점검 스티커가 있지만 스티커는 도착을 보장하지 않습니다."
    caption: "1000쪽부터 100쪽을 보내면 모두 받았다는 확인은 다음 쪽인 1100을 가리킵니다. 숫자는 예시입니다."
    after_paragraph: 0
  - file: assets/animations/l28-seq-ack-flags-checksum.svg
    title: "순서 번호, ACK, 제어 플래그"
    alt: "1000번 바이트부터 100바이트를 보내면 1000~1099를 차지하고 모두 받았다는 ACK는 다음 위치인 1100을 가리킵니다. 이어 SYN, FIN, ACK, RST 제어 플래그와, 헤더가 끝나는 곳을 알리는 Data Offset, 손상을 점검하지만 도착이나 의미를 보장하지 않는 Checksum이 나옵니다."
    caption: "순서 번호는 바이트의 위치, ACK는 다음에 기대하는 위치를 나타냅니다. 숫자는 설명을 위한 예시입니다."
    after_paragraph: 2
- terms:
  - 흐름 제어 (Flow Control)
  - 수신 윈도 (Receive Window)
  - Zero Window
  animations:
  - file: l28-window-buffer.svg
    title: 받을 자리를 알리는 Window
    alt: 수신 버퍼 칸이 데이터로 차오르며 Window 숫자가 줄어 0이 되는 장면입니다.
    caption: 프로그램이 데이터를 가져가는 속도보다 도착이 빠르면 수신 버퍼가 차고 알릴 수 있는 Window가 줄어듭니다.
  question_placements:
  - question_id: u8-l02-p04-q01
    after_paragraph: 1
  - question_id: u8-l02-p04-q02
    after_paragraph: 2
  questions:
  - id: u8-l02-p04-q01
    kind: choice
    difficulty: easy
    prompt: 흐름 제어(Flow Control)는 주로 무엇의 여유를 살피나요?
    choices:
    - id: a
      text: 인터넷 경로에 동시에 지나가는 장치의 수
      feedback: 경로가 붐비는지는 혼잡 제어가 살핍니다. 흐름 제어는 받는 쪽의 수신 버퍼 여유를 살핍니다.
    - id: b
      text: 받는 컴퓨터의 수신 버퍼에 데이터를 받아 둘 공간
      feedback: 맞아요. 흐름 제어는 받는 쪽의 여유를 보내는 쪽에 알려 버퍼가 넘치지 않게 돕습니다.
    - id: c
      text: 송신 프로그램이 사용할 수 있는 목적지 포트
      feedback: 포트 번호는 통신 프로그램을 구분합니다. 흐름 제어는 수신 버퍼의 여유를 살핍니다.
    - id: d
      text: TCP 헤더에 옵션이 추가될 수 있는 공간
      feedback: 헤더 옵션과 길이는 Data Offset과 관련됩니다. 흐름 제어는 받는 쪽의 버퍼 여유를 다룹니다.
    - id: e
      text: 데이터가 수신 컴퓨터에 도착하기까지의 시간
      feedback: 도착까지 걸리는 시간은 지연입니다. 흐름 제어는 수신 버퍼의 여유를 살핍니다.
    answer: b
  - id: u8-l02-p04-q02
    kind: choice
    difficulty: medium
    prompt: 수신 측이 Zero Window를 알렸다면 어떤 상황을 뜻하나요?
    choices:
    - id: a
      text: 네트워크 경로에 혼잡이 전혀 없다는 뜻입니다
      feedback: Zero Window는 네트워크 경로가 아니라 수신 측이 알릴 수 있는 버퍼 여유와 관련됩니다.
    - id: b
      text: 수신 측에서 더는 데이터를 받을 수 없도록 연결을 영구 종료했다는 뜻입니다
      feedback: Zero Window는 연결 종료 신호가 아닙니다. 수신 버퍼 여유가 없어 새 데이터 전송을 조절해야 한다는 뜻입니다.
    - id: c
      text: 송신 측 포트 번호가 0으로 바뀌었다는 뜻입니다
      feedback: 포트 번호와 Window 값은 다른 정보입니다. Zero Window는 수신 측 버퍼 여유가 없음을 알립니다.
    - id: d
      text: TCP가 데이터를 모두 받아 앱에 전달했다는 뜻입니다
      feedback: 데이터 완료를 뜻하는 신호가 아닙니다. 수신 버퍼에 공간이 없는 동안 송신 측은 전송을 조절합니다.
    - id: e
      text: 수신 버퍼 여유가 없어 송신 측이 새 데이터 전송을 조절해야 한다는 뜻입니다
      feedback: 맞아요. 송신 측은 수신 측에 공간이 생기는지 살피며 전송을 조절할 수 있습니다.
    answer: e
  illustrations:
  - file: assets/animations/l28-daily-serving-counter-space.svg
    title: "서빙대에 접시를 둘 자리가 있을까"
    alt: "서빙대에 빈자리가 많으면 접시를 계속 내고, 빈자리가 줄면 알리는 여유도 작아지며, 자리가 없으면 새 접시 내기를 멈췄다가 자리가 나면 알리고 다시 냅니다."
    caption: "받는 쪽의 여유에 맞춰 접시를 냅니다. 칸 수는 설명용입니다."
    after_paragraph: 0
  - file: assets/animations/l28-window-shrinks-to-zero.svg
    title: "수신 윈도가 줄어 0이 되는 과정"
    alt: "수신 버퍼에 여유가 많으면 윈도가 크고, 버퍼가 차면 알리는 윈도 값이 작아지며, 가득 차면 Zero Window로 새 데이터를 멈추게 합니다. 프로그램이 읽어 공간이 생기면 알리고 전송을 이어 갑니다."
    caption: "흐름 제어는 받는 쪽이 데이터를 받아 둘 여유를 살핍니다. 칸 수는 설명용입니다."
    after_paragraph: 1
  illustration_after_paragraph: [1]
- terms:
  - 혼잡 제어 (Congestion Control)
  question_placements:
  - question_id: u8-l02-p05-q01
    after_paragraph: 1
  - question_id: u8-l02-p05-q02
    after_paragraph: 2
  questions:
  - id: u8-l02-p05-q01
    kind: choice
    difficulty: easy
    prompt: 흐름 제어와 혼잡 제어가 각각 살피는 곳을 바르게 구분한 것은 무엇인가요?
    choices:
    - id: a
      text: 흐름 제어는 네트워크 경로를, 혼잡 제어는 수신 버퍼를 살핍니다
      feedback: 두 역할이 뒤바뀌었습니다. 흐름 제어는 받는 쪽을, 혼잡 제어는 네트워크 경로를 살핍니다.
    - id: b
      text: 둘 다 수신 프로그램의 버퍼만 살핍니다
      feedback: 흐름 제어는 수신 버퍼를 살피지만, 혼잡 제어는 네트워크 경로의 붐빔을 살핍니다.
    - id: c
      text: 흐름 제어는 받는 쪽의 여유를, 혼잡 제어는 네트워크 경로의 붐빔을 살핍니다
      feedback: 맞아요. 둘 다 보내는 양을 조절하지만 살피는 대상이 다릅니다.
    - id: d
      text: 흐름 제어는 포트 번호를, 혼잡 제어는 데이터 내용을 살핍니다
      feedback: 포트는 프로그램을 구분합니다. 이 페이지는 흐름 제어의 수신 여유와 혼잡 제어의 경로 상태를 구분합니다.
    - id: e
      text: 흐름 제어는 데이터 손상을, 혼잡 제어는 바이트 순서를 살핍니다
      feedback: 데이터 손상과 바이트 순서를 살피는 구분이 아닙니다. 흐름 제어는 받는 쪽, 혼잡 제어는 경로를 살핍니다.
    answer: c
  - id: u8-l02-p05-q02
    kind: choice
    difficulty: medium
    prompt: 패킷 하나가 늦거나 사라졌다면 그 이유를 곧바로 네트워크 혼잡이라고 판단해도 될까요?
    choices:
    - id: a
      text: 아니요. 여러 원인이 있을 수 있어 그 사실만으로 혼잡을 확정할 수 없습니다
      feedback: 맞아요. 손실이나 지연은 여러 원인으로 생길 수 있어 혼잡이라고 단정할 수 없습니다.
    - id: b
      text: 네. 패킷이 하나라도 늦으면 경로가 반드시 가득 찬 것입니다
      feedback: 지연만으로 경로가 혼잡하다고 확정할 수 없습니다. 다른 원인도 살펴야 합니다.
    - id: c
      text: 네. 수신 버퍼가 비어 있으면 경로가 혼잡하다는 뜻입니다
      feedback: 수신 버퍼 여유는 흐름 제어의 대상입니다. 경로 혼잡과 같은 뜻이 아닙니다.
    - id: d
      text: 아니요. TCP는 손실이나 지연을 감지할 수 없습니다
      feedback: 본문은 송신 측이 혼잡 신호를 바탕으로 양을 조절한다고 설명합니다. 다만 단일 지연·손실만으로 원인을 확정하지 않습니다.
    - id: e
      text: 네. 포트 번호가 바뀌면 혼잡이 발생했다고 볼 수 있습니다
      feedback: 포트 번호 변화는 경로 혼잡을 증명하지 않습니다. 지연이나 손실도 여러 원인에서 생길 수 있습니다.
    answer: a
  illustrations:
  - file: assets/animations/l28-daily-counter-vs-road.svg
    title: "받는 쪽 자리와 도로의 붐빔은 달라요"
    alt: "주방에서 서빙대로 가는 길에서 서빙대의 빈자리는 받는 쪽의 여유이고 좁은 도로의 붐빔은 길의 상태입니다. 둘 다 내는 양을 조절하지만 하나는 받는 쪽을, 하나는 함께 쓰는 길을 보호하며 접시 하나가 늦었다고 길이 막혔다고 단정하지는 않습니다."
    caption: "받는 쪽의 자리와 길의 붐빔은 서로 다른 문제입니다."
    after_paragraph: 0
  - file: assets/animations/l28-flow-vs-congestion.svg
    title: "흐름 제어와 혼잡 제어"
    alt: "송신 측에서 수신 측으로 가는 길에서 흐름 제어는 받는 쪽 수신 버퍼의 여유를, 혼잡 제어는 데이터가 지나는 네트워크 경로의 혼잡을 살핍니다. 각각 받는 프로그램과 컴퓨터, 공유하는 경로를 보호하며 패킷 하나가 늦었다고 혼잡이라고 단정할 수는 없습니다."
    caption: "흐름 제어는 받는 쪽, 혼잡 제어는 네트워크 경로를 살핍니다. 혼잡 제어의 구체적 알고리즘은 이 Lesson의 범위가 아닙니다."
    after_paragraph: 1
- terms:
  - TCP 헤더 (TCP Header)
  - UDP 헤더 (UDP Header)
  question_placements:
  - question_id: u8-l02-p06-q01
    after_paragraph: 1
  - question_id: u8-l02-p06-q02
    after_paragraph: 2
  questions:
  - id: u8-l02-p06-q01
    kind: choice
    difficulty: easy
    prompt: TCP 옵션이 없을 때와 UDP 헤더의 크기를 바르게 비교한 것은 무엇인가요?
    choices:
    - id: a
      text: TCP는 8바이트이고 UDP는 최소 20바이트입니다
      feedback: 크기를 서로 바꿔 썼습니다. TCP는 옵션이 없어도 최소 20바이트이고 UDP는 8바이트입니다.
    - id: b
      text: TCP와 UDP 헤더는 모두 항상 20바이트입니다
      feedback: UDP 헤더는 8바이트이며, TCP는 옵션이 없을 때도 최소 20바이트입니다.
    - id: c
      text: TCP는 항상 20바이트로 고정되고 UDP는 옵션에 따라 더 길어집니다
      feedback: TCP 헤더는 옵션이 있으면 더 길어질 수 있습니다. UDP 헤더는 이 페이지에서 8바이트로 설명합니다.
    - id: d
      text: TCP는 옵션이 없어도 최소 20바이트이고 UDP는 8바이트입니다
      feedback: 맞아요. TCP는 옵션이 붙으면 더 길어질 수 있고 UDP 헤더는 네 칸, 8바이트입니다.
    - id: e
      text: UDP는 20바이트이고 TCP는 데이터 크기에 따라 8바이트입니다
      feedback: TCP 헤더의 최소 크기와 UDP 헤더 크기가 뒤바뀌고 데이터 크기와도 혼동했습니다.
    answer: d
  - id: u8-l02-p06-q02
    kind: choice
    difficulty: medium
    prompt: UDP 헤더가 TCP 헤더보다 짧다는 사실만으로 내 상황에서 UDP가 더 낫다고 결론 내릴 수 있나요?
    choices:
    - id: a
      text: 네. 헤더가 짧으면 모든 앱에서 항상 더 빠르고 좋습니다
      feedback: 헤더 길이만으로 모든 상황의 성능이나 적합성을 결론 내릴 수 없습니다. 필요한 전달 기능도 봐야 합니다.
    - id: b
      text: 아니요. 필요한 순서·재전송 같은 기능과 앱이 맡을 동작을 함께 따져야 합니다
      feedback: 맞아요. TCP와 UDP 선택은 헤더 길이뿐 아니라 필요한 전달 기능과 앱의 책임을 함께 고려해야 합니다.
    - id: c
      text: 네. UDP는 기본적으로 모든 데이터를 확인하고 다시 전송합니다
      feedback: UDP 자체는 데이터그램의 도착이나 순서를 보장하지 않습니다. 필요한 동작은 앱이나 그 위의 프로토콜이 정합니다.
    - id: d
      text: 아니요. UDP는 헤더가 짧아서 포트 번호를 사용할 수 없습니다
      feedback: UDP 헤더에도 출발지·목적지 포트가 있습니다. 선택할 때는 포트 유무가 아니라 필요한 전달 기능을 봅니다.
    - id: e
      text: 네. TCP의 순서 있는 바이트 흐름은 어떤 앱에도 도움이 되지 않습니다
      feedback: 파일처럼 순서와 재전송이 필요한 경우 TCP 기능이 도움이 될 수 있습니다. 앱의 요구를 고려해야 합니다.
    answer: b
  illustrations:
  - file: assets/animations/l28-daily-short-vs-detailed-waybill.svg
    title: "같은 물건에 붙는 송장 길이"
    alt: "같은 크기의 물건에 짧은 송장은 보낸 호수, 받는 호수, 크기, 파손 점검의 네 칸만 있고, 상세 송장은 확인과 순서 칸이 더해져 더 깁니다. 송장 길이만으로 좋고 나쁨을 정하지 않는다고 표시됩니다."
    caption: "짧은 송장과 상세 송장은 해 주는 일이 다릅니다. 길이만으로 판단하지 않습니다."
    after_paragraph: 0
  - file: assets/animations/l28-udp-8-tcp-20-header-size.svg
    title: "UDP 헤더 8바이트, TCP 헤더 20바이트 이상"
    alt: "같은 크기의 데이터 앞에 UDP 헤더는 출발지 포트, 목적지 포트, 길이, Checksum 네 칸의 8바이트이고 TCP 헤더는 옵션이 없어도 최소 20바이트이며 옵션이 붙으면 더 깁니다. 헤더 길이만이 아니라 필요한 전달 기능을 함께 봐야 합니다."
    caption: "헤더가 짧다고 모든 상황에서 UDP가 더 빠르거나 좋은 것은 아닙니다. 필요한 전달 기능을 함께 봅니다."
    after_paragraph: 1
- terms:
  - UDP (User Datagram Protocol)
  - 동기화
  - 지연 (Latency)
  animations:
  - file: l28-udp-game-latest.svg
    title: 기다리는 TCP, 최신 상태를 고르는 UDP 앱
    alt: 위치 데이터 하나가 빠졌을 때 TCP의 바이트 흐름은 빠진 데이터를 기다리고, UDP를 쓰는 앱은 새 위치를 적용하는 장면입니다.
    caption: UDP 자체가 빠진 데이터를 건너뛰는 것은 아닙니다. 앱이 오래된 위치 대신 최신 상태를 고를 수 있습니다.
  question_placements:
  - question_id: u8-l02-p07-q01
    after_paragraph: 1
  - question_id: u8-l02-p07-q02
    after_paragraph: 2
  - question_id: u8-l02-p07-q03
    after_paragraph: 3
  questions:
  - id: u8-l02-p07-q01
    kind: choice
    difficulty: easy
    prompt: TCP에서 중간 바이트가 빠졌을 때 뒤의 데이터가 앱에 바로 전달되지 않을 수 있는 이유는 무엇인가요?
    choices:
    - id: a
      text: TCP 헤더가 UDP보다 짧아서 뒤 데이터를 보관할 공간이 없습니다
      feedback: 헤더 길이가 이유가 아닙니다. TCP는 바이트를 순서 있는 흐름으로 제공하므로 빠진 부분을 기다릴 수 있습니다.
    - id: b
      text: 서버가 모든 오래된 위치 업데이트를 의도적으로 버리기 때문입니다
      feedback: 이 페이지는 앱의 최신 위치 선택과 TCP의 순서 있는 바이트 전달을 구분합니다.
    - id: c
      text: 위치 업데이트에는 TCP에서 사용할 순서 번호가 없기 때문입니다
      feedback: TCP 순서 번호는 바이트 흐름의 위치를 나타냅니다. 지연은 빠진 바이트를 기다리는 특성에서 생길 수 있습니다.
    - id: d
      text: UDP가 TCP 연결을 종료해 버리기 때문입니다
      feedback: UDP가 TCP 연결을 종료하지 않습니다. TCP 자체의 순서 있는 바이트 흐름 때문에 기다릴 수 있습니다.
    - id: e
      text: TCP는 바이트를 순서 있는 흐름으로 제공하므로 빠진 부분을 기다릴 수 있습니다
      feedback: 맞아요. 빠진 바이트를 기다리는 동안 뒤의 바이트가 앱에 전달되기 전 지연될 수 있습니다.
    answer: e
  - id: u8-l02-p07-q02
    kind: choice
    difficulty: medium
    prompt: 위치 갱신을 UDP로 보낼 때, 늦게 도착한 오래된 값 대신 최신 값만 사용하려면 어떻게 해야 하나요?
    choices:
    - id: a
      text: 빠진 3번 데이터를 만들어 5번보다 먼저 전달합니다
      feedback: UDP가 빠진 데이터를 만들지는 않습니다. 앱이 번호나 시간을 이용해 어떤 값을 쓸지 정할 수 있습니다.
    - id: b
      text: 오래된 3번을 반드시 받은 뒤에만 5번을 앱에 전달합니다
      feedback: 순서 있는 바이트 흐름으로 기다리는 동작은 TCP의 특성입니다. UDP는 데이터그램 순서를 보장하지 않습니다.
    - id: c
      text: UDP는 자동으로 골라주지 않으므로 앱이 업데이트 번호나 시간을 확인해 최신 값만 적용합니다
      feedback: 맞아요. UDP는 최신 값 선택을 대신하지 않으며 앱이 오래된 값을 버리고 새 값을 적용할 수 있습니다.
    - id: d
      text: 위치 값을 재전송해 게임 화면을 이전 상태로 되돌립니다
      feedback: UDP 자체가 손실된 위치를 재전송하거나 화면을 되돌리지는 않습니다. 그런 동작은 앱이 정해야 합니다.
    - id: e
      text: 목적지 포트를 바꾸어 오래된 위치를 제거합니다
      feedback: 포트 번호는 프로그램을 구분합니다. 오래된 업데이트를 적용할지는 앱의 규칙으로 정합니다.
    answer: c
  - id: u8-l02-p07-q03
    kind: choice
    difficulty: medium
    prompt: 게임에서 위치는 최신 값이 중요하고 중요한 행동은 확인이 필요하다면, 본문에 맞는 설계는 무엇인가요?
    choices:
    - id: a
      text: 위치 갱신에는 UDP와 앱의 최신 값 선택을 쓰고, 중요한 행동은 확인받도록 설계할 수 있습니다
      feedback: 맞아요. 데이터의 성격에 따라 최신 상태를 택하거나 확인을 요구하도록 앱이 규칙을 정할 수 있습니다.
    - id: b
      text: 모든 데이터를 UDP로 보내면 UDP가 위치와 중요한 행동을 자동 확인합니다
      feedback: UDP는 도착이나 순서를 보장하지 않습니다. 중요한 행동의 확인이 필요하면 앱이 그 동작을 구현해야 합니다.
    - id: c
      text: 모든 위치 값을 TCP로 보내면 과거 위치를 기다리지 않고 최신 값만 자동 전달합니다
      feedback: TCP는 순서 있는 바이트 흐름을 제공하므로 빠진 부분을 기다릴 수 있습니다. 최신 값만 고르는 기능은 앱이 정합니다.
    - id: d
      text: UDP는 손실이 없으므로 앱은 위치 번호를 확인할 필요가 없습니다
      feedback: UDP는 손실이나 순서를 보장하지 않습니다. 앱이 번호나 시간을 이용해 최신 값을 고를 수 있습니다.
    - id: e
      text: TCP와 UDP는 같은 방식으로 모든 데이터의 도착과 순서를 보장합니다
      feedback: 두 방식의 전달 특성이 다릅니다. TCP는 순서 있는 바이트 흐름을 제공하고 UDP는 도착·순서를 보장하지 않습니다.
    answer: a
  illustrations:
  - file: assets/animations/l28-daily-latest-position-alert.svg
    title: "늦은 옛 위치보다 제때 온 새 위치"
    alt: "배달 기사 위치 알림 3, 4, 5번이 가다가 3번이 늦거나 사라집니다. 한쪽은 3번을 기다리며 보여 주고 다른 쪽은 5번을 바로 보여 주며, 어느 방식이 맞는지는 앱이 정하는 규칙이라고 표시됩니다."
    caption: "늦은 옛 정보보다 제때 온 새 정보를 택할 수 있지만 그 선택은 앱이 합니다."
    after_paragraph: 0
  - file: assets/animations/l28-lost-update-wait-or-latest.svg
    title: "위치 갱신 3번이 사라졌을 때"
    alt: "위치 갱신 3, 4, 5번을 보내다 3번이 늦거나 사라지면, 순서를 지키는 흐름은 4, 5번도 앱에 전달되기 전에 3번을 기다릴 수 있고, 앱이 번호를 보고 낡은 값을 버리면 최신 5번을 바로 반영할 수 있습니다. UDP가 스스로 고르는 것이 아니라 앱이 규칙을 정합니다."
    caption: "UDP는 도착과 순서를 보장하지 않으며, 최신 값을 고르거나 중요한 행동을 확인받는 규칙은 앱이 정합니다. 모든 게임이 UDP만 쓰는 것은 아닙니다."
    after_paragraph: 2
  illustration_after_paragraph: [1]
- terms:
  - HTTP/3
  - QUIC
  question_placements:
  - question_id: u8-l02-p08-q01
    after_paragraph: 1
  - question_id: u8-l02-p08-q02
    after_paragraph: 2
  questions:
  - id: u8-l02-p08-q01
    kind: choice
    difficulty: easy
    prompt: TCP와 UDP 중 어떤 방식이 맞는지는 무엇을 보고 판단해야 하나요?
    choices:
    - id: a
      text: 언제나 헤더가 더 짧은 쪽을 고릅니다
      feedback: 헤더 길이만으로 고르지 않습니다. 모든 바이트가 필요한지 최신 상태를 제때 처리하는 일이 중요한지 살펴야 합니다.
    - id: b
      text: 게임이나 웹 같은 앱 이름만 보고 항상 같은 방식을 고릅니다
      feedback: 앱 이름만으로 결정되지 않습니다. 해당 데이터에 필요한 전달 특성을 따져야 합니다.
    - id: c
      text: 목적지 컴퓨터가 더 가까워 보이는 쪽을 고릅니다
      feedback: 목적지 거리만으로 TCP와 UDP의 적합성이 정해지지 않습니다. 데이터의 순서·완전성·시의성을 봅니다.
    - id: d
      text: 데이터가 빠짐없이 순서대로 필요한지, 최신 상태를 제때 다루는 게 중요한지 봅니다
      feedback: 맞아요. 데이터가 요구하는 전달 특성에 따라 TCP와 UDP가 다른 선택이 될 수 있습니다.
    - id: e
      text: 프로그램이 사용하는 포트 번호가 짝수인지 홀수인지 봅니다
      feedback: 포트의 짝수·홀수는 선택 기준이 아닙니다. 데이터에 필요한 순서·확인·시의성을 고려합니다.
    answer: d
  - id: u8-l02-p08-q02
    kind: choice
    difficulty: medium
    prompt: HTTP/3가 UDP 위에서 동작한다는 설명을 바르게 이해한 것은 무엇인가요?
    choices:
    - id: a
      text: UDP 자체가 연결·암호화·흐름 제어를 모두 보장하므로 QUIC은 필요하지 않습니다
      feedback: UDP 자체가 이 기능을 보장하는 것은 아닙니다. HTTP/3는 UDP 위에서 필요한 기능을 제공하는 QUIC을 사용합니다.
    - id: b
      text: HTTP/3는 UDP 위에서 QUIC을 사용해 연결·암호화·흐름 제어 같은 기능을 제공합니다
      feedback: 맞아요. UDP를 사용하더라도 QUIC이 필요한 기능을 제공하므로 신뢰성이나 혼잡 제어가 전혀 없다는 뜻은 아닙니다.
    - id: c
      text: HTTP/3는 UDP를 쓰지 않고 TCP 헤더 안에 QUIC을 넣습니다
      feedback: 본문은 HTTP/3가 UDP 위에서 QUIC을 사용한다고 설명합니다.
    - id: d
      text: HTTP/3는 QUIC을 사용해 모든 데이터의 도착과 순서를 UDP 자체에 맡깁니다
      feedback: UDP 자체는 도착이나 순서를 보장하지 않습니다. QUIC은 UDP 위에서 필요한 전달 기능을 제공합니다.
    - id: e
      text: HTTP/3는 브라우저의 포트 번호를 QUIC으로 변환하는 이름 규칙입니다
      feedback: QUIC은 포트 이름을 바꾸는 규칙이 아니라 UDP 위에서 연결과 보안 등 필요한 기능을 제공하는 프로토콜입니다.
    answer: b
  illustrations:
  - file: assets/animations/l28-daily-registered-vs-postcard.svg
    title: "등기 우편과 엽서, 상황에 맞춰 골라요"
    alt: "등기 우편은 받았다고 확인하고 빠진 것은 다시 보내며 엽서는 그냥 보내고 확인은 보낸 사람이 정합니다. 빠짐없이 가야 하는지 제때 보는지가 기준이고, 엽서 위에 확인 규칙을 더한 서비스도 있습니다."
    caption: "어느 쪽이 더 좋은지는 내용에 따라 달라집니다."
    after_paragraph: 0
  - file: assets/animations/l28-choose-tcp-udp-quic.svg
    title: "TCP와 UDP는 상황에 맞춰 골라요"
    alt: "TCP는 순서 있는 바이트 흐름과 확인·재전송을, UDP는 데이터그램을 보내는 기본 기능을 제공합니다. 빠짐없는 전달과 최신 상태 처리 중 무엇이 중요한지가 기준이며, HTTP/3는 UDP 위의 QUIC이 연결·암호화·흐름 제어·혼잡 제어를 제공하므로 UDP를 쓴다고 신뢰성이나 혼잡 제어가 전혀 없다는 뜻은 아닙니다."
    caption: "TCP와 UDP는 앱에 제공하는 전달 방식이 다르며, 어느 쪽이 더 좋은지는 상황에 따라 달라집니다."
    after_paragraph: 1
animations_dir: units/05-tcp-and-udp/lessons/04-tcp-udp-헤더형식과-게임서버-특징/assets/animations
---

Unit 7에서는 TCP와 UDP가 데이터를 보내는 방식과 TCP 연결의 시작·종료를 배웠다. 이 Lesson에서는 TCP와 UDP의 헤더를 살펴보고, 두 방식이 게임 통신에서 어떤 선택으로 이어질 수 있는지 알아본다. **헤더**는 전송할 데이터 앞에 붙어, 어디서 왔고 어디로 가는지 또는 어떤 처리가 필요한지 알려 주는 정보다. 아래 학습 흐름도는 여덟 페이지의 순서를 보여 준다. 첫 페이지에서는 헤더 그림에서 필요한 칸을 찾아 읽는 방법부터 살펴본다.

## TCP와 UDP 헤더에서 무엇을 읽을까?

컴퓨터는 데이터를 보내면서 받는 프로그램과 전달에 필요한 정보를 함께 표시한다. 이 정보가 헤더에 들어간다. TCP는 순서와 확인 응답, 받을 수 있는 양 같은 정보를 여러 칸에 기록한다. UDP는 필요한 기본 정보를 더 짧은 헤더에 담는다. 먼저 아래 헤더 그림에서 각 칸의 이름을 살펴보자. 모든 칸의 크기를 외우기보다, 어떤 질문에 답을 주는 칸인지 알면 된다.

헤더는 사진이나 웹 문서 같은 **내용 자체**가 아니다. 내용 앞에 붙는 안내 정보다. 예를 들어 포트 번호는 받을 프로그램을 찾고, 순서 번호와 ACK는 TCP 바이트 흐름의 진행을 나타낸다. 뒤 페이지에서는 이 가운데 포트, 순서와 확인, 수신 여유를 차례로 읽는다.

**기억할 점:** 헤더 그림은 외울 표가 아니라, 전송에 필요한 안내 정보를 찾아 읽는 지도다.

## 포트 번호는 컴퓨터 안의 프로그램을 찾는다

IP 주소는 목적지 컴퓨터를 찾고, 포트 번호는 그 컴퓨터에서 통신할 프로그램을 구분한다. 아파트 주소에 빗대면 IP 주소가 건물과 동을, 포트 번호가 동 안의 호수를 가리킨다. 같은 컴퓨터에서 브라우저, 게임, 메신저가 함께 통신해도 포트 번호 덕분에 데이터가 알맞은 프로그램으로 간다.

| 헤더의 정보 | 어떤 쪽을 가리킬까? | 예 |
| --- | --- | --- |
| 출발지 포트 | 데이터를 보낸 프로그램 | 브라우저가 임시로 사용한 포트 `51514` |
| 목적지 포트 | 데이터를 받을 프로그램 | 웹 서버의 HTTPS 포트 `443` |

응답을 보낼 때는 각 끝의 역할이 반대로 보인다. 아까 요청의 출발지였던 브라우저 포트 `51514`가 응답에서는 목적지 포트가 된다. 포트 `80`은 HTTP, `443`은 HTTPS에서 흔히 쓰는 기본 포트다. 기본값은 약속이므로 다른 번호를 설정할 수도 있고, 그 경우 접속할 때 번호를 지정해야 한다. Well-known Port는 여러 서비스가 널리 사용하는 대표 번호를 말한다.

**기억할 점:** IP 주소는 컴퓨터를, 포트 번호는 그 컴퓨터 안의 통신 프로그램을 찾는다.

## TCP 헤더는 바이트 순서와 통신 상태를 기록한다

TCP는 데이터를 바이트의 흐름으로 다룬다. 순서 번호(Sequence Number)는 보낸 데이터가 바이트 흐름의 어디에서 시작하는지 나타내고, 확인 응답(ACK, Acknowledgement) 번호는 다음에 받기를 기대하는 위치를 알려 준다. 예를 들어 설명을 위해 1000번 바이트부터 100바이트를 보냈다고 하자. 이 데이터는 1000번부터 1099번까지를 차지하므로, 모두 받았다는 ACK는 다음에 기대하는 1100번을 가리킬 수 있다. 이 값은 Unit 8 Lesson 1에서 배운 누적 확인과 같은 원리다.

TCP 헤더에는 통신 상태를 알리는 제어 플래그도 있다. SYN은 연결을 시작할 때, FIN은 정상적으로 마칠 때, ACK는 확인 응답 번호가 유효함을 나타낼 때 쓰인다. RST는 연결을 초기화해야 할 때 사용한다. 이 신호들은 헤더 안의 켜짐/꺼짐 표시로 전달된다.

Data Offset은 TCP 헤더가 어디에서 끝나고 데이터가 어디서 시작하는지 알려 준다. 옵션이 붙으면 헤더 길이가 달라질 수 있다. Checksum(검사합)은 헤더와 데이터가 전송 중 손상됐는지 확인하는 데 쓰이지만, 도착 자체나 데이터의 의미를 보장하지는 않는다. 플래그 조합이나 옵션의 세부 동작은 지금 외우지 않아도 된다.

**기억할 점:** 순서 번호는 바이트의 위치, ACK는 다음에 기대하는 위치를 나타낸다.

## 흐름 제어는 받는 쪽의 여유를 살핀다

데이터를 보내는 쪽이 아무리 빨라도 받는 프로그램이 처리하지 못하면 수신 컴퓨터의 임시 저장 공간인 **수신 버퍼**가 찬다. 식당 주방에서 접시가 계속 나오는데 서빙대의 빈자리가 없으면 새 접시를 둘 수 없는 것과 비슷하다. 흐름 제어(Flow Control)는 받는 쪽이 감당할 수 있는 양을 보내는 쪽에 알려, 수신 버퍼가 넘치지 않게 돕는다.

TCP는 수신 버퍼의 여유를 수신 윈도(Receive Window) 값으로 알린다. 여유가 줄면 알리는 값도 작아지고, 버퍼에 공간이 없으면 Zero Window(제로 윈도)를 알릴 수 있다. 이때 송신 측은 새 데이터를 계속 밀어 넣지 않고, 수신 측에 공간이 생기는지 확인하며 전송을 조절한다. 아래 그림은 버퍼가 차면서 알릴 수 있는 여유가 줄어드는 모습을 보여 준다.

**기억할 점:** 흐름 제어는 길의 상태가 아니라 받는 컴퓨터가 데이터를 받아 둘 여유를 살핀다.

## 혼잡 제어는 네트워크 길의 붐빔을 살핀다

흐름 제어와 혼잡 제어는 모두 보내는 양을 조절하지만, 살피는 곳이 다르다. 흐름 제어가 **받는 컴퓨터**의 여유를 보는 일이라면, 혼잡 제어(Congestion Control)는 데이터가 지나는 **네트워크 경로**가 붐비는지 살피는 일이다. 좁은 도로에 차가 너무 많이 들어서면 모두 늦어지는 것처럼, 네트워크 장비나 링크가 감당할 양을 넘으면 지연이나 손실이 생길 수 있다.

송신 측 TCP는 이런 신호를 바탕으로 경로에 보낼 양을 조절한다. 실제 신호는 여러 원인으로 생길 수 있으므로 패킷 하나가 늦거나 사라졌다고 경로 혼잡이라고 단정할 수는 없다. 혼잡 제어의 구체적인 알고리즘은 이 Lesson의 범위가 아니다.

| 구분 | 흐름 제어 | 혼잡 제어 |
| --- | --- | --- |
| 무엇을 살필까? | 받는 쪽의 수신 버퍼 여유 | 네트워크 경로의 혼잡 |
| 누구를 보호할까? | 수신 프로그램과 컴퓨터 | 공유하는 네트워크 경로 |

**기억할 점:** 흐름 제어는 받는 쪽, 혼잡 제어는 네트워크 길을 살핀다.

## TCP 헤더와 UDP 헤더는 크기와 역할이 다르다

앞에서 본 TCP 헤더에는 포트뿐 아니라 순서 번호, ACK, 제어 플래그, Window 등 여러 정보가 들어간다. TCP 헤더는 옵션이 없을 때도 최소 20바이트이며, 옵션이 붙으면 더 길어진다. UDP 헤더는 출발지 포트, 목적지 포트, 길이, Checksum 네 칸으로 이루어져 있고 8바이트다.

같은 크기의 데이터를 보낸다고 가정하면, 전송 데이터 앞에 붙는 헤더만 비교했을 때 UDP 쪽이 더 짧다. 하지만 헤더가 짧다고 모든 상황에서 UDP가 더 빠르거나 더 좋은 것은 아니다. TCP가 제공하는 순서 있는 바이트 흐름과 재전송이 필요한 일에는 그 기능이 도움이 된다. UDP는 기본으로 맡아 주는 일이 적은 만큼, 필요한 동작을 사용하는 앱이나 그 위의 프로토콜이 정해야 한다.

**기억할 점:** 헤더 길이만 보고 빠르기를 판단하지 말고, 필요한 전달 기능을 함께 보자.

## 게임에서는 최신 상태가 더 중요할 때 UDP가 어울린다

게임에서 캐릭터 위치는 계속 바뀐다. 예를 들어 위치 갱신 3번이 늦거나 사라졌을 때, 이미 더 새 위치 5번이 도착했다면 오래된 위치 3번을 기다리는 것보다 5번을 바로 반영하는 편이 자연스러울 수 있다. TCP는 같은 연결의 바이트를 순서대로 앱에 제공하므로 중간 바이트가 빠지면 그 뒤 데이터도 앱에 전달되기 전에 기다릴 수 있다. UDP는 데이터그램의 도착이나 순서를 보장하지 않는다.

그렇다고 UDP가 스스로 빠진 위치를 건너뛰거나 최신 데이터만 골라 주는 것은 아니다. 앱이 각 업데이트에 번호나 시간을 넣고, 낡은 값은 버리고 최신 값을 적용하도록 정할 수 있다. 중요한 행동은 확인받고 위치 갱신은 최신 것을 택하는 식으로 데이터의 성격에 따라 규칙을 다르게 둘 수도 있다. 이런 선택 때문에 일부 실시간 게임이나 음성·영상 통신에서 UDP가 활용된다. 모든 게임이 UDP만 쓰는 것은 아니다.

여기서 지연(Latency)은 데이터가 상대에게 도착하기까지 걸리는 시간이다. 오래된 상태를 확실히 받느라 새 상태가 늦어지는 것보다, 최신 상태를 제때 보는 일이 중요한 상황이 있다.

**기억할 점:** 실시간 앱은 늦은 옛 정보보다 제때 도착한 새 정보를 택할 수 있지만, 그 선택은 앱이 해야 한다.

## 정리: 상황에 맞춰 TCP와 UDP를 고른다

TCP와 UDP는 헤더가 다른 데서 끝나지 않고, 앱에 제공하는 전달 방식도 다르다. TCP는 순서 있는 바이트 흐름과 확인·재전송 같은 기능을 제공한다. UDP는 데이터그램을 보내는 기본 기능에 집중하며, 앱에 도착·순서 보장을 제공하지 않는다. 어느 쪽이 더 좋은지는 데이터가 빠짐없이 전달되어야 하는지, 아니면 최신 상태를 제때 처리하는 일이 더 중요한지에 따라 달라진다.

HTTP/3는 UDP만으로 동작하는 것이 아니라, UDP 위에서 연결·암호화·흐름 제어·혼잡 제어 등 필요한 기능을 제공하는 QUIC을 사용한다. 따라서 “UDP를 쓴다”는 말이 “신뢰성이나 혼잡 제어가 전혀 없다”는 뜻은 아니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 흐름 제어는 받는 쪽의 여유를, 혼잡 제어는 네트워크 경로를 살핀다. TCP는 순서 있는 바이트 흐름을 제공하고 UDP는 데이터그램 전달을 앱에 맡긴다.
- **적용하기 (Apply):** 파일처럼 모든 바이트가 필요할 때와 게임 위치처럼 최신 값이 더 중요한 때에 TCP·UDP 선택이 달라질 수 있는 이유를 설명한다.
- **찾아보기 (Lookup):** 헤더의 실제 값과 옵션은 TCP·UDP 헤더 그림이나 패킷 캡처에서 확인한다. HTTP/3가 UDP 위에서 어떤 기능을 사용하는지는 QUIC을 찾아본다.
