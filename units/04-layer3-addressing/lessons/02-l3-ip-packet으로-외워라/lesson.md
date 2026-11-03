---
id: u4-l12-l3-ip-packet으로-외워라
title: IP 패킷은 어떤 정보를 담고 있을까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-12.md
wiki_diagram: units/04-layer3-addressing/lessons/02-l3-ip-packet으로-외워라/assets/diagrams/lesson-12.svg
page_metadata:
- terms:
  - 패킷 (Packet)
  - 데이터 (Data)
  - IP (Internet Protocol)
  - L3 (네트워크 계층)
  illustrations:
  - file: assets/animations/l12-daily-split-parcels.svg
    title: "큰 물건은 작은 상자로 나눠 보낸다"
    alt: "왼쪽에 ‘나’의 집, 오른쪽에 ‘친구’의 집이 있고 가운데에 큰 그림 한 점이 놓입니다. 그림이 작은 상자 네 개로 나뉘고, 상자마다 송장이 붙은 뒤 한 줄로 길을 따라 친구의 집으로 이동해 도착 표시가 나타납니다."
    caption: "큰 물건도 작은 상자로 나누고, 상자마다 송장을 붙여서 보냅니다."
    after_paragraph: -1
  - file: assets/animations/l12-packet-split.svg
    title: "데이터는 패킷이라는 작은 단위로 간다"
    alt: "왼쪽에 내 휴대전화, 오른쪽에 친구 휴대전화가 있고 가운데에 큰 사진 파일이 놓입니다. 파일이 작은 패킷 네 개로 나뉘고, 패킷마다 헤더가 붙은 뒤 차례로 친구 휴대전화로 이동해 도착 표시가 나타납니다."
    caption: "사진 한 장도 작은 패킷으로 나누고, 각 패킷에 헤더를 붙여 보냅니다. 사라진 패킷을 다시 보내는 일은 IP가 아니라 TCP 같은 전송 계층이 맡아요."
    after_paragraph: 1
  questions:
  - id: u4-l12-p01-q01
    kind: choice
    difficulty: easy
    prompt: 큰 사진 파일을 네트워크로 보낼 때, 컴퓨터가 전송하기 좋게 나누는 작은 단위를 무엇이라고 하나요?
    choices:
    - id: a
      text: 패킷
      feedback: 맞아요. 패킷은 네트워크를 통해 데이터를 옮기는 작은 전달 단위예요.
    - id: b
      text: IP 주소
      feedback: 다시 생각해 보세요. 파일 전체를 한 번에 보내는 것이 아니라, 잘게 나눈 전달 단위를 생각해 보세요.
    - id: c
      text: 헤더
      feedback: 다시 생각해 보세요. 파일 전체를 한 번에 보내는 것이 아니라, 잘게 나눈 전달 단위를 생각해 보세요.
    - id: d
      text: 페이로드
      feedback: 다시 생각해 보세요. 파일 전체를 한 번에 보내는 것이 아니라, 잘게 나눈 전달 단위를 생각해 보세요.
    - id: e
      text: MTU
      feedback: 다시 생각해 보세요. 파일 전체를 한 번에 보내는 것이 아니라, 잘게 나눈 전달 단위를 생각해 보세요.
    answer: a
  - id: u4-l12-p01-q04
    kind: choice
    difficulty: easy
    prompt: 패킷 하나가 사라졌을 때, IP가 알아서 다시 보내 주나요?
    choices:
    - id: a
      text: 네. 모든 IP 패킷은 반드시 두 번 보냅니다.
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: b
      text: 아니요. IP 자체는 재전송을 보장하지 않으며, TCP 같은 전송 계층 기능이 손실을 확인하고 다시 보낼 수 있습니다.
      feedback: 맞아요. 아니요. IP 자체는 재전송을 보장하지 않으며, TCP 같은 전송 계층 기능이 손실을 확인하고 다시 보낼 수 있습니다.입니다.
    - id: c
      text: 네. 라우터가 사진 파일 전체를 다시 만듭니다.
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: d
      text: 아니요. 패킷은 사라져도 수신자가 항상 복구합니다.
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: e
      text: 아니요. Ethernet 스위치가 인터넷 전체에서 재전송합니다.
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    answer: b
  - id: u4-l12-p01-q02
    kind: choice
    difficulty: medium
    prompt: 큰 사진을 여러 패킷으로 나누어 보낼 때 각 패킷은 어떤 역할을 하나요?
    choices:
    - id: a
      text: 사진 데이터의 일부를 담아 목적지로 전달된다
      feedback: 맞아요. 각 패킷은 큰 데이터의 일부를 실어 전달해요.
    - id: b
      text: 사진 파일 전체를 한 패킷에 담아 항상 한 번에 전달한다
      feedback: 다시 생각해 보세요. 사진 파일 전체를 나누어 보내는 이유를 떠올려 보세요.
    - id: c
      text: 최대 패킷 크기 기준을 정한다
      feedback: 다시 생각해 보세요. 사진 파일 전체를 나누어 보내는 이유를 떠올려 보세요.
    - id: d
      text: IP 주소와 MAC 주소를 바꾼다
      feedback: 다시 생각해 보세요. 사진 파일 전체를 나누어 보내는 이유를 떠올려 보세요.
    - id: e
      text: 16진수 필드의 의미를 해석한다
      feedback: 다시 생각해 보세요. 사진 파일 전체를 나누어 보내는 이유를 떠올려 보세요.
    answer: a
  - id: u4-l12-p01-q03
    kind: short
    prompt: 네트워크 계층에서 패킷 전달 규칙을 정하는 프로토콜을 무엇이라고 하나요?
    answers:
    - IP
    - Internet Protocol
    feedback: IP(Internet Protocol)는 네트워크 계층의 패킷 전달 규칙을 정해요.
  question_placements:
  - question_id: u4-l12-p01-q01
    after_paragraph: 1
  - question_id: u4-l12-p01-q04
    after_paragraph: 2

- terms:
  - 헤더 (Header)
  - 페이로드 (Payload)
  - 프레임 (Frame)
  illustrations:
  - file: assets/animations/l12-daily-box-in-box.svg
    title: "송장 붙은 상자 안의 상자"
    alt: "긴 상자의 왼쪽은 송장, 나머지는 내용물 칸입니다. 내용물 칸을 열자 안에서 송장과 내용물을 가진 작은 상자가 나타나고, 바깥은 큰 상자, 안쪽은 작은 상자라는 이름표가 붙습니다."
    caption: "송장은 길 안내, 내용물은 실어 나르는 물건입니다. 작은 상자는 큰 상자의 내용물이기도 해요."
    after_paragraph: -1
  - file: assets/animations/l12-header-payload-nesting.svg
    title: "패킷은 헤더와 페이로드로 이뤄진다"
    alt: "이더넷 프레임이 헤더와 페이로드 칸으로 나뉘어 있습니다. 페이로드 칸을 열자 안에서 헤더와 페이로드를 가진 IP 패킷이 나타나고, 바깥은 이더넷 프레임, 안쪽은 IP 패킷이라는 이름표가 붙습니다."
    caption: "헤더는 전달 정보, 페이로드는 내용입니다. 이더넷 프레임의 페이로드 안에 IP 패킷이 들어 있어요."
    after_paragraph: 2
  questions:
  - id: u4-l12-p02-q01
    kind: choice
    difficulty: easy
    prompt: 패킷에서 전달에 필요한 안내·처리 정보를 담는 부분은 무엇인가요?
    choices:
    - id: a
      text: 헤더
      feedback: 맞아요. 헤더는 전달과 처리에 필요한 정보를 담아요.
    - id: b
      text: 페이로드
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: c
      text: MTU
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: d
      text: 프레임
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: e
      text: 포트 번호
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    answer: a
  - id: u4-l12-p02-q04
    kind: choice
    difficulty: easy
    prompt: 이더넷 프레임 안에 들어가는 IP 패킷에서, 실제 전달할 내용을 담은 부분은 무엇인가요?
    choices:
    - id: a
      text: 헤더
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: b
      text: MAC 주소
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: c
      text: 포트 번호
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: d
      text: 페이로드
      feedback: 맞아요. 페이로드입니다.
    - id: e
      text: MTU
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    answer: d
  - id: u4-l12-p02-q02
    kind: choice
    difficulty: medium
    prompt: 상자 비유에서 주소가 적힌 송장에 해당하는 부분은 무엇인가요?
    choices:
    - id: a
      text: 페이로드
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: b
      text: IP 주소
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: c
      text: MAC 주소
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: d
      text: 포트 번호
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: e
      text: 헤더
      feedback: 맞아요. 송장의 역할에 해당하는 것은 헤더예요.
    answer: e
  - id: u4-l12-p02-q03
    kind: short
    prompt: 패킷의 실제 내용물을 담는 부분을 무엇이라고 하나요?
    answers:
    - 페이로드
    - payload
    feedback: 헤더는 전달에 필요한 정보를, 페이로드는 실제 실어 나르는 내용을 담아요.
  question_placements:
  - question_id: u4-l12-p02-q01
    after_paragraph: 1
  - question_id: u4-l12-p02-q04
    after_paragraph: 3

- terms:
  - MTU (Maximum Transmission Unit)
  - 바이트 (Byte)
  illustrations:
  - file: assets/animations/l12-daily-truck-limit.svg
    title: "상자 크기에는 한계가 있다"
    alt: "위쪽에 트럭 한 칸에 실을 수 있는 최대 크기를 나타내는 눈금이 있습니다. 작은 상자는 눈금 안에 들어가 통과하고, 눈금보다 큰 가구는 넘쳐서 안 됩니다. 큰 짐을 여러 상자로 나누면 각각 눈금 안에 들어갑니다. 마지막에 길마다 한계가 다를 수 있다는 점선 눈금이 나타납니다."
    caption: "한계보다 큰 짐은 여러 상자로 나눠 싣습니다. 길마다 한계는 다를 수 있어요."
    after_paragraph: -1
  - file: assets/animations/l12-mtu-limit.svg
    title: "MTU는 한 번에 보낼 크기의 한계다"
    alt: "위쪽에 한 번에 보낼 수 있는 최대 크기(MTU) 눈금이 있습니다. 작은 메시지는 눈금 안에 들어가고, 큰 사진은 눈금을 넘어 한 패킷에 못 담깁니다. 여러 패킷으로 나누면 각각 눈금 안에 들어갑니다. 마지막에 연결마다 MTU가 다를 수 있다는 점선 눈금이 나타납니다."
    caption: "예로 든 이더넷의 MTU 1,500바이트는 IP 패킷(헤더와 페이로드)의 최대 크기입니다. 연결마다 값이 다를 수 있어요."
    after_paragraph: 1
  questions:
  - id: u4-l12-p03-q01
    kind: choice
    difficulty: easy
    prompt: MTU는 무엇을 정하는 기준인가요?
    choices:
    - id: a
      text: 패킷 안 페이로드의 최소 크기
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: b
      text: 이더넷 프레임의 출발지 MAC 주소
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: c
      text: 한 번에 전달할 데이터 단위의 최대 크기
      feedback: 맞아요. MTU는 링크에서 한 번에 전달할 단위의 최대 크기 기준이에요.
    - id: d
      text: IP 주소의 바이트 수
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: e
      text: Wireshark가 읽는 숫자의 개수
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    answer: c
  - id: u4-l12-p03-q04
    kind: choice
    difficulty: easy
    prompt: MTU가 1,500바이트인 예에서 모든 IP 패킷을 꼭 1,500바이트로 채워야 하나요?
    choices:
    - id: a
      text: 네. 더 작은 패킷은 네트워크가 버립니다.
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: b
      text: 네. 빈 부분을 항상 0으로 채워야 합니다.
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: c
      text: 아니요. 1,500바이트는 최대값이므로 더 작은 패킷도 보낼 수 있습니다.
      feedback: 맞아요. 아니요. 1,500바이트는 최대값이므로 더 작은 패킷도 보낼 수 있습니다.입니다.
    - id: d
      text: 아니요. MTU는 IP 주소의 길이만 말합니다.
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: e
      text: 아니요. 1,500은 Ethernet 프레임 전체 크기를 뜻합니다.
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    answer: c
  - id: u4-l12-p03-q02
    kind: choice
    difficulty: medium
    prompt: 이더넷 MTU를 1,500바이트로 둔 경로에서 IP 패킷의 크기는 어떻게 되어야 하나요?
    choices:
    - id: a
      text: 모든 IP 패킷을 정확히 1,500바이트로 채운다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: b
      text: IP 패킷이 1,500바이트를 넘지 않도록 한다
      feedback: 맞아요. 이 예의 1,500바이트는 IP 헤더와 페이로드를 합한 IP 패킷의 최대값이에요.
    - id: c
      text: 이더넷 헤더까지 포함한 프레임 전체가 1,500바이트다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: d
      text: MAC 주소가 1,500바이트라는 뜻이다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: e
      text: 연결 방식과 무관하게 모든 네트워크에 적용된다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    answer: b
  question_placements:
  - question_id: u4-l12-p03-q01
    after_paragraph: 1
  - question_id: u4-l12-p03-q04
    after_paragraph: 2

- terms:
  - 와이어샤크 (Wireshark)
  - 16진수 (Hexadecimal)
  - Type (이더넷 타입)
  illustrations:
  - file: assets/animations/l12-daily-code-row.svg
    title: "송장번호 한 줄을 칸으로 나눠 읽기"
    alt: "숫자 열여섯 칸이 한 줄로 놓여 있고 어디가 무슨 뜻인지 물음표가 뜹니다. 앞 여섯 칸은 받는 곳, 다음 여섯 칸은 보낸 곳, 그다음 두 칸은 종류로 색이 나뉩니다. 종류 칸이 0800이면 뒤에 안쪽 송장이 이어진다고 표시되고, 마지막에 바깥 송장, 안쪽 송장, 내용물이 차례로 펼쳐집니다."
    caption: "정해진 칸대로 나누어 읽으면 숫자의 의미가 보입니다. 이 숫자 값은 설명용 예시예요."
    after_paragraph: -1
  - file: assets/animations/l12-hex-fields.svg
    title: "16진수 숫자 줄에서 헤더 읽기"
    alt: "16진수 열여섯 칸이 한 줄로 놓여 있고 어디가 주소인지 물음표가 뜹니다. 앞 여섯 칸은 목적지 MAC, 다음 여섯 칸은 출발지 MAC, 그다음 두 칸은 Type으로 색이 나뉩니다. Type이 0800이면 뒤에 IPv4 패킷이 이어진다고 표시되고, 마지막에 이더넷, IP, TCP 또는 UDP가 차례로 펼쳐집니다."
    caption: "Wireshark는 프로토콜 규칙대로 필드를 나누어 보여 줍니다. 그림의 숫자 값은 설명용 예시예요."
    after_paragraph: 2
  questions:
  - id: u4-l12-p04-q01
    kind: choice
    difficulty: easy
    prompt: Wireshark는 주로 무엇을 도와주는 프로그램인가요?
    choices:
    - id: a
      text: 패킷을 캡처하고 프로토콜별 구조로 보여준다
      feedback: 맞아요. Wireshark는 캡처한 데이터를 프로토콜 구조에 따라 보여줘요.
    - id: b
      text: IP 주소와 MAC 주소를 자동으로 바꾼다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: c
      text: 데이터를 1,500바이트로 늘린다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: d
      text: 신뢰성 있는 재전송을 수행한다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: e
      text: 케이블을 통해 전기 신호를 보낸다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    answer: a
  - id: u4-l12-p04-q04
    kind: choice
    difficulty: easy
    prompt: 이더넷 Type 필드가 0800일 때, 뒤에 오는 패킷은 무엇인가요?
    choices:
    - id: a
      text: IPv4 패킷
      feedback: 맞아요. IPv4 패킷입니다.
    - id: b
      text: IPv6 패킷
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: c
      text: TCP 세그먼트
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: d
      text: DNS 이름
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: e
      text: Wireshark 캡처 파일
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    answer: a
  - id: u4-l12-p04-q02
    kind: choice
    difficulty: medium
    prompt: Wireshark의 16진수 표시를 읽을 때 필요한 것은 무엇인가요?
    choices:
    - id: a
      text: 모든 숫자를 IP 주소로 본다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: b
      text: 헤더를 무시하고 페이로드만 본다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: c
      text: 숫자를 아무 순서로나 문장처럼 바꾼다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: d
      text: 프로토콜이 정한 필드 구조를 따라 해석한다
      feedback: 맞아요. 프로토콜의 규칙이 각 필드의 위치와 의미를 정해요.
    - id: e
      text: 각 계층이 같은 헤더를 쓴다고 가정한다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    answer: d
  - id: u4-l12-p04-q03
    kind: short
    prompt: 통신에서 데이터 형식과 필드의 의미를 정하는 규칙을 무엇이라고 하나요?
    answers:
    - 프로토콜
    - protocol
    feedback: 프로토콜은 통신 장치가 데이터를 주고받고 해석하는 규칙이에요.
  page_id: wireshark-packet-inspection
  video:
    video_id: vBrQ3yzerMg
    title: '[따라學IT] 01. 네트워크란 무엇인가? - 실습2(Wireshark)'
    creator: 따라하면서 배우는 IT
    duration_seconds: 512
  question_placements:
  - question_id: u4-l12-p04-q01
    after_paragraph: 1
  - question_id: u4-l12-p04-q04
    after_paragraph: 3

- terms:
  - MAC 주소 (Media Access Control address)
  - IP 주소 (Internet Protocol address)
  - 포트 번호 (Port number)
  illustrations:
  - file: assets/animations/l12-daily-three-wheres.svg
    title: "배송에는 세 가지 ‘어디’가 있다"
    alt: "왼쪽 집에서 가운데 물류센터를 거쳐 오른쪽 건물로 가는 길이 있고, 건물에는 101호와 102호가 있습니다. 먼저 이번 구간 인수자가 첫 구간을, 그다음 최종 주소 건물이 전체 길을, 마지막으로 호수가 건물 안의 받을 사람을 가리킨다고 강조됩니다."
    caption: "구간 인수자, 최종 건물, 건물 안의 받을 사람은 서로 다른 범위를 가리킵니다."
    after_paragraph: -1
  - file: assets/animations/l12-mac-ip-port-scope.svg
    title: "MAC·IP·포트는 범위가 달라요"
    alt: "왼쪽 내 노트북에서 가운데 라우터를 거쳐 오른쪽 PC로 가는 길이 있고, PC에는 브라우저와 메신저가 있습니다. 먼저 MAC이 첫 링크를, 그다음 IP가 전체 길의 목적지를, 마지막으로 포트가 PC 안의 프로그램을 가리킨다고 강조됩니다."
    caption: "MAC은 현재 링크, IP는 네트워크 사이의 목적지, 포트는 기기 안의 프로그램을 가리킵니다. 이 포트는 스위치의 물리 포트가 아니에요. 포트 번호는 예시예요."
    after_paragraph: 3
  questions:
  - id: u4-l12-p05-q01
    kind: choice
    difficulty: easy
    prompt: 어느 주소가 현재 링크의 네트워크 인터페이스를 구분하나요?
    choices:
    - id: a
      text: IP 주소
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: b
      text: 포트 번호
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: c
      text: MTU
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: d
      text: EtherType
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: e
      text: MAC 주소
      feedback: 맞아요. MAC 주소는 현재 링크에서 프레임을 주고받을 인터페이스를 구분해요.
    answer: e
  - id: u4-l12-p05-q04
    kind: choice
    difficulty: easy
    prompt: 한 컴퓨터에서 브라우저와 메신저를 구분해 데이터를 전달할 때 쓰는 것은 무엇인가요?
    choices:
    - id: a
      text: MAC 주소
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: b
      text: IP 네트워크 부분
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: c
      text: 이더넷 케이블 길이
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: d
      text: 프레임 검사 값
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: e
      text: 포트 번호
      feedback: 맞아요. 포트 번호입니다.
    answer: e
  - id: u4-l12-p05-q02
    kind: choice
    difficulty: medium
    prompt: 포트 번호는 어떤 정보를 구분하는 데 쓰이나요?
    choices:
    - id: a
      text: 현재 링크의 프레임을 받을 인터페이스
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: b
      text: 네트워크 사이의 최종 목적지
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: c
      text: 같은 기기 안에서 데이터를 받을 프로그램
      feedback: 맞아요. 포트 번호는 전송 계층에서 같은 기기 안의 프로그램을 구분해요.
    - id: d
      text: 패킷의 최대 크기
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: e
      text: 이더넷 프레임 종류
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    answer: c
  - id: u4-l12-p05-q03
    kind: choice
    difficulty: medium
    prompt: 네트워크 사이의 출발지와 최종 목적지를 나타내는 주소는 무엇인가요?
    choices:
    - id: a
      text: MAC 주소
      feedback: MAC 주소는 현재 링크에서 프레임을 주고받을 인터페이스를 구분해요.
    - id: b
      text: IP 주소
      feedback: 맞아요. IP 주소는 네트워크 사이에서 출발지와 최종 목적지를 나타내요.
    - id: c
      text: 포트 번호
      feedback: 포트 번호는 같은 기기 안에서 데이터를 받을 프로그램을 구분해요.
    - id: d
      text: MTU
      feedback: MTU는 한 번에 전달할 수 있는 데이터 단위의 최대 크기를 정해요.
    - id: e
      text: EtherType
      feedback: EtherType은 Ethernet 프레임에 어떤 종류의 패킷이 담겼는지 나타내요.
    answer: b
  question_placements:
  - question_id: u4-l12-p05-q01
    after_paragraph: 2
  - question_id: u4-l12-p05-q04
    after_paragraph: 4

- terms: []
  illustrations:
  - file: assets/animations/l12-daily-tracking-log.svg
    title: "배송 기록을 보고 문제를 찾는다"
    alt: "왼쪽 집에서 오른쪽 받는 곳으로 가는 길 아래에 배송 기록판이 있습니다. 접수됨과 수령 확인이 차례로 기록되고, 한 번은 접수만 되고 이후 기록이 없어 물음표가 뜹니다. 마지막에 내 택배나 허가받은 기록만 조회해야 하고 남의 택배 정보는 안 된다고 표시됩니다."
    caption: "기록을 보면 어디서 끊겼는지 좁힐 수 있지만, 남의 정보는 함부로 볼 수 없습니다."
    after_paragraph: -1
  - file: assets/animations/l12-capture-observe.svg
    title: "캡처로 통신을 안전하게 관찰한다"
    alt: "왼쪽 내 PC에서 오른쪽 서버로 가는 길 아래에 캡처 도구 화면이 있습니다. 요청 나감과 응답 도착이 차례로 기록되고, 한 번은 요청만 나가고 응답이 없어 서버 쪽에 물음표가 뜹니다. 마지막에 내 장비나 허가받은 네트워크에서만 관찰해야 하고 허가 없는 남의 통신은 안 된다고 표시됩니다."
    caption: "캡처를 보면 요청과 응답을 확인해 문제 위치를 좁힐 수 있어요. 본인 장비나 허가받은 네트워크에서만 관찰하고, 파일을 공개하기 전에는 개인정보를 확인하세요."
    after_paragraph: 1
  questions:
  - id: u4-l12-p06-q01
    kind: choice
    difficulty: easy
    prompt: 패킷 캡처를 할 때 지켜야 할 원칙은 무엇인가요?
    choices:
    - id: a
      text: 주변 네트워크를 모두 허락 없이 캡처한다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: b
      text: 본인 장비나 허가받은 네트워크만 관찰한다
      feedback: 맞아요. 캡처에는 다른 사람의 통신이 포함될 수 있으므로 허가된 범위에서만 관찰해야 해요.
    - id: c
      text: 캡처 파일을 공개 게시한다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: d
      text: 비밀번호가 있으면 항상 캡처한다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: e
      text: MAC 주소를 숨기면 허가 없이 관찰한다
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    answer: b
  - id: u4-l12-p06-q04
    kind: choice
    difficulty: easy
    prompt: 패킷 헤더는 주로 어떤 정보를 담나요?
    choices:
    - id: a
      text: 사용자가 보는 화면의 색
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: b
      text: 전달하고 처리하는 데 필요한 안내 정보
      feedback: 맞아요. 전달하고 처리하는 데 필요한 안내 정보입니다.
    - id: c
      text: 네트워크 케이블의 길이
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: d
      text: 전달할 실제 파일 내용만
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    - id: e
      text: 컴퓨터의 키보드 설정
      feedback: 다시 생각해 보세요. 바로 앞의 설명에서 그 역할을 확인해 보세요.
    answer: b
  - id: u4-l12-p06-q02
    kind: choice
    difficulty: medium
    prompt: 인터넷 연결 문제를 살피려고 Wireshark를 쓸 때 가장 직접 확인할 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: 저장 장치에 있는 모든 파일 내용
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: b
      text: 무선 공유기의 물리적 위치
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: c
      text: 웹사이트의 디자인 코드
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: d
      text: 컴퓨터가 실행 중인 모든 프로그램의 비밀번호
      feedback: 이 선택지는 다른 개념의 역할이에요. 본문에서 이 Page의 핵심 구분을 다시 확인해 보세요.
    - id: e
      text: 요청이 나갔는지, 응답이 돌아왔는지
      feedback: 맞아요. 패킷 흐름을 보면 요청과 응답이 오갔는지 확인할 수 있어요.
    answer: e
  question_placements:
  - question_id: u4-l12-p06-q01
    after_paragraph: 2
  - question_id: u4-l12-p06-q04
    after_paragraph: 3

animations_dir: units/04-layer3-addressing/lessons/02-l3-ip-packet으로-외워라/assets/animations
additional_sources:
- https://github.com/physical-spark/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/01-3.md
- https://github.com/physical-spark/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/03-1.md

---

## 네트워크에서 데이터는 어떤 단위로 움직일까?

사진 한 장을 휴대전화에서 친구의 휴대전화로 보낸다고 해 보자. 사진 파일은 꽤 클 수 있지만, 네트워크는 파일 전체를 하나의 거대한 덩어리로 한 번에 옮기지 않는다. 데이터를 작은 단위로 나누고 각 단위에 전달에 필요한 정보를 붙여 보낸다. 이 작은 전달 단위를 **패킷(Packet)**이라고 한다.

택배 상자로 비유하면 사진은 보내려는 물건이고, 패킷은 운반하기 좋게 나눈 상자 하나다. 다만 인터넷에서 상자가 사라졌다고 IP가 자동으로 그 상자를 다시 보내는 것은 아니다. 손실을 확인하고 다시 보내는 동작은 TCP 같은 전송 계층의 신뢰성 기능과 관련되며, 뒤에서 배운다. 여기서는 패킷이 데이터를 실어 나르는 단위라는 점부터 잡자.

패킷은 네트워크에서 데이터를 전달하는 단위다. IP(Internet Protocol)는 OSI 3계층(L3), 즉 네트워크 계층에서 패킷을 전달할 때 따르는 규칙을 정한 프로토콜이다. 패킷의 안쪽이 어떻게 나뉘는지는 다음 페이지에서 헤더와 페이로드로 나누어 살펴보자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 패킷은 네트워크가 운반하는 데이터 단위이며 파일은 여러 패킷으로 나뉠 수 있다.
- **적용하기 (Apply):** 큰 파일을 보낼 때 단위별로 전달되는 이유를 설명한다.
- **찾아보기 (Lookup):** 패킷 헤더의 구체적인 필드는 IP header Page에서 찾아본다.

## 패킷은 안내 정보와 내용물로 이루어진다
<!-- learn-page-id: header-payload-definition -->

택배 상자에는 받는 곳을 찾는 데 필요한 송장이 붙고, 안에는 실제로 전달할 물건이 들어 있다. IP 패킷도 크게 두 부분으로 생각할 수 있다. **헤더(Header)**는 전달과 처리에 필요한 정보를 담고, **페이로드(Payload)**는 실제로 실어 나르는 내용을 담는다.

예를 들어 편지를 보내면 봉투 겉면의 주소가 우편물이 어디로 가야 하는지 알려주고, 봉투 안 종이에 편지 내용이 담긴다. 패킷에서도 헤더가 송장 역할을 하고 페이로드가 내용물 역할을 한다. 헤더가 단순히 주소만 담는 것은 아니다. 주소 외에도 패킷을 처리하는 데 필요한 여러 정보가 들어가며, 세부 필드는 다음 Unit의 Wireshark 실습에서 더 살펴본다.

그림에서 큰 상자의 페이로드를 열면 작은 상자가 다시 나오는 모습을 보자. 큰 상자의 내용물이 작은 상자 전체일 수 있다는 뜻이다. 이더넷 프레임의 페이로드 안에는 IP 패킷이 들어가고, IP 패킷 안에는 다시 헤더와 페이로드가 있다.

같은 덩어리가 바깥 계층에서는 내용물, 안쪽 계층에서는 헤더와 내용물을 갖춘 전달 단위가 된다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** IP 패킷의 Header는 전달 정보, Payload는 실어 나르는 내용이다.
- **적용하기 (Apply):** Wireshark에서 헤더와 데이터 영역을 구분해 설명한다.
- **찾아보기 (Lookup):** IPv4 헤더의 필드별 길이와 역할은 IP header lesson에서 찾아본다.

## MTU는 한 번에 보낼 패킷의 크기 한계다
<!-- learn-page-id: mtu-definition -->

택배 운송 수단에는 실을 수 있는 상자 크기의 한계가 있다. 네트워크 연결에도 한 번에 전달할 수 있는 단위의 크기 기준이 있는데, 이를 **MTU(Maximum Transmission Unit, 최대 전송 단위)**라고 한다. 이 Lesson에서는 흔한 이더넷 환경의 MTU인 **1,500바이트(약 1.5KB)**를 예로 든다. 연결 방식과 설정에 따라 다른 값도 있다.

이 예에서 1,500바이트는 IP 패킷의 크기를 말한다. IP 헤더와 페이로드를 합친 크기다. 이더넷 프레임의 헤더와 뒤쪽 검사 정보는 이 크기에 더해지므로, 프레임 전체가 1,500바이트라는 뜻은 아니다. ‘최대’ 크기라는 말도 매 패킷이 반드시 그만큼 크다는 뜻은 아니다. 작은 메시지는 작은 패킷으로 갈 수 있다.

큰 사진은 1,500바이트보다 훨씬 크므로 전송 과정에서 여러 데이터 단위로 나뉠 수 있다. 여기서 1,500을 모든 네트워크에서 외워야 할 자연 법칙처럼 받아들이지 말자. MTU는 한 링크가 감당할 수 있는 최대 크기 기준이다. IP 단편화는 Unit 6 Lesson 1에서 살펴본다. TCP가 데이터를 세그먼트로 나누는 흐름은 이 Unit의 Lesson 5에서, TCP와 UDP의 차이는 Unit 7 Lesson 1에서 다룬다. IP 단편화와 TCP 세그먼트 분할은 서로 다른 동작이다. 필요하면 내 컴퓨터의 인터페이스 설정에서 MTU를 확인할 수 있지만, 명령어와 환경별 차이는 참고할 내용이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** MTU는 한 링크가 전달할 IP 패킷 크기의 상한이다.
- **적용하기 (Apply):** 1,500바이트 MTU와 더 큰 패킷이 만날 때 생길 일을 예측한다.
- **찾아보기 (Lookup):** 경로 MTU와 단편화의 차이는 TTL·단편화 Lesson에서 확인한다.

## Wireshark는 숫자 줄에서 패킷 구조를 보여준다
<!-- learn-page-id: wireshark-packet-inspection -->

네트워크에서 오가는 원자료는 컴퓨터가 다루는 0과 1이다. 화면에서는 이 값을 짧게 나타내려고 16진수 숫자로 보여주기도 한다. 숫자만 보면 어디가 주소이고 어디가 내용인지 알기 어렵다. **Wireshark**는 패킷을 캡처하고, 각 프로토콜의 규칙에 따라 해석한 결과를 보여주는 프로그램이다.

아래 영상은 설치, 캡처, HTTP 필터와 기본 화면을 따라 해 보는 보충 실습이다. 영상에서 모든 필드를 외울 필요는 없다. 지금은 Wireshark가 ‘숫자를 마법처럼 번역’하는 게 아니라, 프로토콜마다 정해진 헤더 구조와 규칙을 이용해 필드를 나눠 보여준다는 점을 확인하자.

아래 애니메이션은 한 줄의 16진수 중 일부가 어떤 필드에 대응하는지 보여준다. 예를 들어 이더넷 헤더의 Type 필드가 `0800`이면 뒤에 IPv4 패킷이 온다는 뜻이다. 이 숫자의 의미를 매번 암산하지 않아도 Wireshark는 이름과 값으로 구조를 펼쳐 보여준다. 첫 화면에서 이더넷을 확인하고, 그 안의 IP를 펼치고, 더 안쪽의 전송 계층 정보를 펼치는 식으로 계층을 따라 읽을 수 있다.

IP 헤더의 Version이나 IHL 같은 필드를 16진수에서 손으로 계산하는 일은 이 Lesson의 목표가 아니다. 처음에는 ‘어떤 계층의 헤더를 보고 있는가’, ‘출발지와 목적지 정보는 어디에 표시되는가’를 익히자. IP 헤더의 세부 필드는 Unit 5 Lesson 1 「IP 헤더 형식」에서 확인한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Wireshark는 캡처한 패킷을 프로토콜 구조에 따라 해석해 보여 준다.
- **적용하기 (Apply):** 캡처 한 건에서 Ethernet·IP 계층을 펼쳐 주소와 필드를 찾는다.
- **찾아보기 (Lookup):** 필터 문법과 캡처 권한은 Wireshark 공식 안내에서 확인한다.

## MAC·IP·포트는 각기 다른 범위를 가리킨다

택배를 전달할 때 한 가지 정보만으로 모든 일을 처리하지 않는다. 현재 배송 구간에서 상자를 전달할 대상과, 최종 목적지, 건물 안에서 받을 사람을 나누어 생각하면 편하다. 네트워크 헤더의 MAC 주소, IP 주소, 포트 번호도 이름은 비슷하게 ‘어디로’를 나타내지만 맡은 범위가 다르다.

**MAC 주소**는 Ethernet 헤더에 담겨 현재 링크에서 프레임을 주고받을 네트워크 인터페이스를 구분한다.

**IP 주소**는 IP 헤더에 담겨 네트워크 사이에서 출발지와 목적지를 나타낸다.

**포트 번호**는 TCP 또는 UDP 헤더에 담기는 전송 계층 정보로, 같은 기기 안에서 데이터를 받을 프로그램을 구분한다. 포트 번호는 IP 헤더가 아니라 TCP/UDP 헤더에 있다. 포트가 패킷 전달에서 어떻게 쓰이는지는 이 Unit의 Lesson 4에서, TCP와 UDP의 자세한 내용은 Unit 7 Lesson 1에서 살펴본다. 아래 그림은 이 세 식별자가 각기 다른 범위를 가리킨다는 점을 보여준다.

예를 들어 한 기기에서 브라우저와 메신저가 함께 통신할 때, 포트 번호가 어느 프로그램으로 데이터를 전달할지 구분하는 데 쓰인다. 여기서 말하는 포트 번호는 소프트웨어상의 번호다. 스위치에 케이블을 꽂는 물리 포트와 같은 뜻이 아니다. MAC은 현재 링크의 인터페이스, IP는 네트워크 사이의 목적지, 포트는 기기 안의 프로그램을 가리킨다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** MAC은 현재 링크, IP는 호스트/네트워크, Port는 호스트 안 프로그램을 구분한다.
- **적용하기 (Apply):** 하나의 연결에서 세 주소 정보가 각각 가리키는 대상을 말한다.
- **찾아보기 (Lookup):** 각 값이 어느 헤더에 있는지는 캡처 예시에서 확인한다.

## Wireshark로 통신을 관찰하고 배운 내용을 묶어 보자

의사가 청진기로 몸의 소리를 듣듯이, 네트워크 관리자는 캡처 도구로 오가는 패킷을 살펴볼 수 있다. 예를 들어 연결이 안 될 때 요청이 실제로 나갔는지, 응답이 돌아왔는지 확인하면 문제의 위치를 좁히는 데 도움이 된다. Wireshark는 패킷을 모아 프로토콜 구조를 보여주므로 네트워크 통신을 관찰하고 문제를 찾는 데 도움을 준다.

캡처 화면에는 다른 사람의 통신이 포함될 수 있다. 그러므로 본인 장비나 명시적으로 허가받은 네트워크에서만 관찰하고, 캡처 파일을 공개하기 전에는 개인정보나 비밀 정보가 담기지 않았는지 확인해야 한다. 이 Lesson의 목적은 도구를 마음껏 들여다보는 데 있지 않고, 네트워크 통신을 안전하게 관찰하는 기본 태도까지 익히는 것이다.

마지막으로 네 가지 연결을 정리해 보자. 패킷은 데이터를 옮기는 작은 단위이며, 헤더는 전달 정보를, 페이로드는 내용을 담는다.

MTU는 한 번에 전달할 IP 패킷 크기의 상한을 나타낸다. Wireshark에서는 계층별 헤더를 차례로 펼쳐 읽을 수 있고, MAC·IP·포트는 링크·네트워크·프로그램이라는 서로 다른 범위에서 전달을 돕는다. 이 관계를 알면 화면에 낯선 숫자가 많아도 어느 계층의 어떤 정보를 보는지부터 차근차근 물을 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 패킷 캡처는 요청·응답과 프로토콜 헤더를 관찰해 장애 범위를 좁힌다.
- **적용하기 (Apply):** 필요한 인터페이스만 선택해 본인 통신을 캡처하고 요청이 나갔는지 확인한다.
- **찾아보기 (Lookup):** 타인 트래픽 취급과 필터 사용은 Wireshark 안내 및 조직 정책을 확인한다.
