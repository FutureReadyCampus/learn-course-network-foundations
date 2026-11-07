---
id: u3-l08-nic-l2-frame-lan-카드-그리고-mac-주소
title: 네트워크 연결 지점과 MAC 주소, 프레임
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-08.md
wiki_diagram: units/03-layer2-switching/lessons/01-nic-l2-frame-lan-카드-그리고-mac-주소/assets/diagrams/lesson-08.svg
page_metadata:
- terms:
  - NIC (Network Interface Card)
  - 네트워크 인터페이스 (Network interface)
  inline_questions_after: 1
  questions:
  - id: u3-01-p01-q01
    kind: choice
    difficulty: easy
    prompt: 집의 문이 집과 바깥을 이어 주듯, 컴퓨터가 네트워크와 신호를 주고받게 해 주는 장치는 무엇인가요?
    choices:
    - id: a
      text: NIC
      feedback: 맞아요. NIC.
    - id: b
      text: LAN
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: MAC 주소
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 프레임
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 라우터
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-01-p01-q02
    kind: choice
    difficulty: medium
    prompt: NIC와 네트워크 인터페이스의 차이를 가장 정확히 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: NIC는 네트워크 주소이고, 인터페이스는 데이터 묶음이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: NIC는 IP 네트워크이고, 인터페이스는 WAN이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: NIC는 케이블 구멍만을 뜻하고 인터페이스는 프로그램 번호다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: NIC와 인터페이스는 언제나 서로 다른 장치 두 개다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: NIC는 연결 장치이고, 인터페이스는 네트워크와 맞닿는 연결 지점이다
      feedback: 맞아요. NIC는 연결 장치이고, 인터페이스는 네트워크와 맞닿는 연결 지점이다.
    answer: e
  - id: u3-01-p01-q03
    kind: choice
    difficulty: medium
    prompt: 네트워크와 맞닿는 연결 지점을 장치와 구분해 부르는 말은 무엇인가요?
    choices:
    - id: a
      text: Network interface(네트워크 인터페이스)
      feedback: 맞아요. 네트워크 인터페이스는 장치에서 네트워크와 맞닿는 연결 지점입니다.
    - id: b
      text: NIC(네트워크 연결 장치)
      feedback: NIC는 네트워크에 연결하는 장치이고, 인터페이스는 네트워크와 맞닿는 연결 지점입니다.
    - id: c
      text: MAC address(MAC 주소)
      feedback: MAC 주소는 네트워크 인터페이스를 식별하는 주소입니다.
    - id: d
      text: IP address(IP 주소)
      feedback: IP 주소는 네트워크에서 목적지를 찾는 데 사용합니다.
    - id: e
      text: Port number(포트 번호)
      feedback: 포트 번호는 장치 안에서 통신할 프로그램을 구분합니다.
    answer: a
  - id: u3-01-p01-q04
    kind: choice
    difficulty: medium
    prompt: "사양표의 'Realtek 무선 LAN'에서 Realtek은 무엇을 가리키나요?"
    choices:
    - id: a
      text: "무선 LAN을 만든 회사 이름"
      feedback: "맞아요. Realtek은 회사 이름입니다."
    - id: b
      text: "호스트의 네트워크 주소"
      feedback: "다시 본문을 확인해 보세요. 호스트의 네트워크 주소."
    - id: c
      text: "프레임을 보내는 통신 규칙"
      feedback: "다시 본문을 확인해 보세요. 프레임을 보내는 통신 규칙."
    - id: d
      text: "무선 네트워크의 연결 장치"
      feedback: "다시 본문을 확인해 보세요. 무선 네트워크의 연결 장치."
    - id: e
      text: "케이블 종류"
      feedback: "다시 본문을 확인해 보세요. 케이블 종류."
    answer: a
  - id: u3-01-p01-q05
    kind: choice
    difficulty: medium
    prompt: 노트북에 네트워크 카드가 따로 꽂혀 있지 않아도 네트워크에 연결될 수 있는 이유는 무엇인가요?
    choices:
    - id: a
      text: NIC가 메인보드에 내장될 수도 있기 때문이다
      feedback: 맞아요. NIC는 별도 카드가 아니라 메인보드에 내장될 수도 있습니다.
    - id: b
      text: 네트워크 연결에는 NIC가 필요 없기 때문이다
      feedback: 네트워크와 신호를 주고받으려면 연결 장치가 필요합니다.
    - id: c
      text: 인터페이스가 컴퓨터 안에서 NIC 역할을 대신하기 때문이다
      feedback: 인터페이스는 연결 지점이고, NIC는 연결 장치입니다.
    - id: d
      text: Realtek이 모든 컴퓨터의 NIC를 원격으로 제공하기 때문이다
      feedback: Realtek은 예시에서 NIC 제조사 이름입니다.
    - id: e
      text: 무선 연결은 컴퓨터의 네트워크 연결이 아니기 때문이다
      feedback: Wi-Fi도 네트워크와 신호를 주고받는 연결입니다.
    answer: a
  animations:
  - file: l08-nic-door.svg
    title: "NIC는 컴퓨터의 문"
    alt: "컴퓨터를 나타내는 네모 안에서 문서 작성과 계산 사이를 점이 오가며 집 안에서 끝나는 일을 보여 줍니다. 이어서 네모 가장자리에 NIC(LAN 카드)가 문처럼 나타나고, NIC가 네트워크와 맞닿는 자리에 인터페이스 점이 생기며, 주황 점이 그 연결 지점을 지나 네트워크로 나갑니다. 마지막에 ‘Realtek 무선 LAN’ 사양 문구에서 Realtek은 회사 이름, 무선 LAN은 NIC 종류라는 설명이 붙습니다."
    caption: "NIC는 컴퓨터가 네트워크와 신호를 주고받는 장치이고, 인터페이스는 NIC가 네트워크와 맞닿는 연결 지점입니다. 사양표의 Realtek은 NIC를 만든 회사 이름입니다."
- terms:
  - 호스트 (Host)
  - 액세스 포인트 (Access Point)
  - 포트 (Port)
  - 네트워크 인터페이스 (Network interface)
  inline_questions_after: 1
  animations:
  - file: l08-host-two-nics.svg
    title: 호스트 하나, 인터페이스 둘
    alt: 노트북 모양의 네모 하나에 진한 점이 처음엔 하나, 나중엔 둘로 늘어납니다. 점 하나는 무선으로 액세스 포인트에, 다른 하나는 선으로
      이어집니다. 마지막 장면에서도 점은 둘로 유지되고 ‘점 2개 = 인터페이스 2개’ 문구가 나옵니다.
    caption: 노트북 한 대에 무선 NIC와 USB 유선 NIC가 달리면 문이 두 개가 됩니다. 진한 점 하나가 인터페이스 하나이므로 점
      두 개는 인터페이스 두 개입니다.
  questions:
  - id: u3-01-p02-q01
    kind: choice
    difficulty: easy
    prompt: 집 한 채에 문이 두 개 있어도 집은 한 채이듯, Wi-Fi와 유선 연결이 모두 있는 노트북은 Host 몇 대인가요?
    choices:
    - id: a
      text: 1대
      feedback: 맞아요. 연결 지점은 둘이어도 노트북 Host는 한 대입니다.
    - id: b
      text: 2대
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 3대
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 4대
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 연결 지점 수와 같은 대수
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-01-p02-q02
    kind: choice
    difficulty: medium
    prompt: USB 유선 네트워크 장치를 추가해 노트북에 연결 지점이 하나 더 생겼습니다. 이 상황을 가장 잘 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 인터페이스가 둘이면 Host도 반드시 두 대다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Host는 케이블 구멍 하나만 가질 수 있다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 한 Host가 둘 이상의 네트워크 인터페이스를 가질 수 있다
      feedback: 맞아요. 한 Host가 둘 이상의 네트워크 인터페이스를 가질 수 있다.
    - id: d
      text: 무선 인터페이스에는 네트워크 연결 지점이 없다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 포트 번호와 물리 연결 지점은 항상 같은 뜻이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-01-p02-q03
    kind: short
    prompt: 일상적으로 케이블을 꽂는 물리적인 연결 구멍을 부르는 말입니다. 영어로 답해주세요.
    answers:
    - port
    - physical port
    - 포트
    - 물리 포트
    feedback: 정답은 port(포트)입니다.
  - id: u3-01-p02-q04
    kind: choice
    difficulty: medium
    prompt: "컴퓨터 옆 케이블 구멍과 프로그램의 포트 번호에 대한 설명으로 맞는 것은 무엇인가요?"
    choices:
    - id: a
      text: "둘 다 케이블을 꽂는 물리적인 구멍이다"
      feedback: "다시 본문을 확인해 보세요. 포트 번호는 프로그램 통신을 구분하는 번호입니다."
    - id: b
      text: "케이블 구멍은 물리 연결, 포트 번호는 프로그램 통신을 구분한다"
      feedback: "맞아요. 같은 '포트'라는 말이지만 문맥과 역할이 다릅니다."
    - id: c
      text: "포트 번호는 네트워크 인터페이스의 MAC 주소다"
      feedback: "다시 본문을 확인해 보세요. MAC 주소와 포트 번호는 다른 값입니다."
    - id: d
      text: "케이블 구멍은 프로그램을, 포트 번호는 케이블을 연결한다"
      feedback: "다시 본문을 확인해 보세요. 두 의미가 뒤바뀌었습니다."
    - id: e
      text: "Wi-Fi 연결에는 포트 번호가 없다"
      feedback: "다시 본문을 확인해 보세요. 프로그램의 포트 번호는 유선과 무선 모두에서 쓰입니다."
    answer: b

  - id: u3-01-p02-q05
    kind: choice
    difficulty: medium
    prompt: 노트북의 Wi-Fi가 무선 네트워크에 연결될 때 가까이에서 신호를 중계해 주는 장치는 무엇인가요?
    choices:
    - id: a
      text: MAC 주소
      feedback: MAC 주소는 연결 지점을 구분하는 값입니다.
    - id: b
      text: 프레임
      feedback: 프레임은 한 링크에서 전달하는 데이터 단위입니다.
    - id: c
      text: 액세스 포인트
      feedback: 맞아요. 액세스 포인트가 무선 연결을 중계합니다.
    - id: d
      text: TCP 포트 번호
      feedback: 포트 번호는 프로그램의 통신 통로를 구분합니다.
    - id: e
      text: Host
      feedback: Host는 네트워크에 연결된 장치입니다.
    answer: c
- terms:
  - LAN (Local Area Network)
  - MAN (Metropolitan Area Network)
  - WAN (Wide Area Network)
  inline_questions_after: 1
  questions:
  - id: u3-01-p03-q01
    kind: choice
    difficulty: easy
    prompt: 네트워크를 마을·도시·넓은 지역에 비유하면, LAN·MAN·WAN은 주로 무엇의 차이를 나타내나요?
    choices:
    - id: a
      text: MAC 주소의 길이
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 네트워크가 걸쳐 있는 범위
      feedback: 맞아요. 네트워크가 걸쳐 있는 범위.
    - id: c
      text: 프레임의 최대 크기
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 전송 속도의 순위
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 연결된 컴퓨터의 운영체제
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-01-p03-q02
    kind: choice
    difficulty: medium
    prompt: LAN과 MAN을 구분하는 거리에 대해 이 페이지가 설명한 내용은 무엇인가요?
    choices:
    - id: a
      text: 두 이름은 사용 장치의 수를 정확히 지정한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: MAN은 언제나 LAN보다 빠르다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: LAN은 반드시 유선이고 MAN은 반드시 무선이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 둘 사이에는 표준으로 정해진 하나의 고정 거리만 있다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 범위의 차이를 나타내지만 경계 거리가 딱 정해져 있지는 않다
      feedback: 맞아요. 범위의 차이를 나타내지만 경계 거리가 딱 정해져 있지는 않다.
    answer: e
  - id: u3-01-p03-q03
    kind: short
    prompt: 집이나 사무실처럼 비교적 가까운 범위의 네트워크를 부르는 이름입니다. 영어 약어로 답해주세요.
    answers:
    - LAN
    - local area network
    - 근거리 네트워크
    - 근거리 통신망
    feedback: 정답은 LAN(Local Area Network)입니다.
  - id: u3-01-p03-q04
    kind: choice
    difficulty: medium
    prompt: "LAN보다 넓은 범위를 가리키는 WAN을 볼 때 기억할 점은 무엇인가요?"
    choices:
    - id: a
      text: "WAN이 언제나 LAN보다 빠르다"
      feedback: "다시 본문을 확인해 보세요. 범위는 속도 순위를 뜻하지 않습니다."
    - id: b
      text: "WAN은 LAN보다 품질이 항상 좋다"
      feedback: "다시 본문을 확인해 보세요. 범위만으로 품질을 정할 수 없습니다."
    - id: c
      text: "WAN이라는 이름만으로 속도나 품질을 정할 수 없다"
      feedback: "맞아요. 이름은 범위를 나타내며 속도나 품질 순위는 아닙니다."
    - id: d
      text: "WAN에 연결된 컴퓨터 수는 항상 더 많다"
      feedback: "다시 본문을 확인해 보세요. 이름이 장치 수를 정하지는 않습니다."
    - id: e
      text: "WAN은 반드시 광섬유를 사용한다"
      feedback: "다시 본문을 확인해 보세요. LAN·MAN·WAN은 범위의 분류입니다."
    answer: c
  - id: u3-01-p03-q05
    kind: choice
    difficulty: medium
    prompt: 집 안의 휴대전화가 Wi-Fi로, 데스크톱이 랜 케이블로 연결되어 있습니다. 둘이 같은 LAN에 있을 수 있는 이유는 무엇인가요?
    choices:
    - id: a
      text: LAN은 케이블 방식만으로 정해지는 이름이기 때문에
      feedback: LAN은 유선·무선 중 어떤 방식을 쓰는지로 정하지 않습니다.
    - id: b
      text: Wi-Fi는 네트워크 범위 분류에서 제외되기 때문에
      feedback: Wi-Fi 장치도 가까운 LAN에 함께 연결될 수 있습니다.
    - id: c
      text: 장치의 연결 방식이 달라도 같은 가까운 범위의 네트워크일 수 있기 때문에
      feedback: 맞아요. LAN은 가까운 범위를 말하며 유선과 무선을 함께 쓸 수 있습니다.
    - id: d
      text: 랜 케이블을 쓰는 데스크톱이 나머지 장치의 속도를 정하기 때문에
      feedback: LAN은 속도나 특정 장치로 정하는 분류가 아닙니다.
    - id: e
      text: 무선 공유기가 두 장치의 MAC 주소를 하나로 합치기 때문에
      feedback: MAC 주소와 네트워크 범위는 서로 다른 개념입니다.
    answer: c
  animations:
  - file: l08-lan-man-wan.svg
    title: "LAN, MAN, WAN"
    alt: "집 공유기에 휴대전화와 태블릿은 Wi-Fi 점선으로, 데스크톱과 IPTV는 케이블 실선으로 연결되어 있습니다. 이 장치들을 LAN(마을) 테두리가 감싸고, 이웃 LAN을 포함한 MAN(도시) 테두리, 다른 도시와 먼 지역까지 포함한 WAN(더 넓은 지역) 테두리가 차례로 넓게 그려집니다. 마지막에 범위의 이름일 뿐 속도 순위가 아니라는 문구가 나옵니다."
    caption: "LAN·MAN·WAN은 네트워크가 어느 정도 범위에 걸쳐 있는지를 나타내는 이름입니다. 범위가 넓다고 더 빠르거나 품질이 좋은 것은 아닙니다."
- terms:
  - OSI 7계층 (OSI 7 layers)
  animations:
  - file: l08-osi-layer-stack.svg
    title: 일곱 층으로 나눠 보는 통신
    alt: 위에서 아래로 7 응용, 6 표현, 5 세션, 4 전송, 3 네트워크, 2 데이터 링크, 1 물리 계층이 쌓여 있습니다. 아래를 가리키는 화살표와 함께 계층이 차례로 강조됩니다.
    caption: 계층 이름과 순서를 그림으로 다시 확인한 뒤 아래 퀴즈를 풀어 보세요.
  questions:
  - id: u3-01-osi-q01
    kind: choice
    difficulty: easy
    prompt: 목적지 IP 주소를 바탕으로 데이터가 어느 네트워크와 경로를 거쳐 갈지 찾습니다. 이 역할을 하는 계층은 무엇인가요?
    choices:
    - id: a
      text: 전송 계층
      feedback: 전송 계층은 두 끝의 프로그램 사이에서 데이터를 전달합니다. 목적지 네트워크로 갈 경로를 찾는 역할은 네트워크 계층입니다.
    - id: b
      text: 표현 계층
      feedback: 표현 계층은 데이터 표현 형식을 맞추거나 바꾸고 보호하는 역할입니다.
    - id: c
      text: 네트워크 계층
      feedback: 맞아요. 네트워크 계층은 IP 주소를 바탕으로 목적지 쪽 경로를 찾습니다.
    - id: d
      text: 물리 계층
      feedback: 물리 계층은 비트를 전기·빛·무선 신호로 실어 보냅니다.
    answer: c
  - id: u3-01-osi-q02
    kind: choice
    difficulty: medium
    prompt: 비트를 케이블의 전기 신호, 광섬유의 빛, 무선 신호로 바꾸어 전달합니다. 이 역할을 하는 계층은 무엇인가요?
    choices:
    - id: a
      text: 데이터 링크 계층
      feedback: 데이터 링크 계층은 바로 이어진 구간에서 프레임을 전달합니다.
    - id: b
      text: 응용 계층
      feedback: 응용 계층은 프로그램이 네트워크로 이용하는 기능을 다룹니다.
    - id: c
      text: 네트워크 계층
      feedback: 네트워크 계층은 목적지까지 갈 경로를 찾습니다.
    - id: d
      text: 물리 계층
      feedback: 맞아요. 물리 계층은 비트를 전기·빛·무선 신호로 실어 매체를 통해 전달합니다.
    answer: d
  - id: u3-01-osi-q03
    kind: choice
    difficulty: medium
    prompt: 통신을 시작하고 이어 가며 마칠 수 있도록 두 프로그램 사이의 대화 상태를 다룹니다. 이 역할을 하는 계층은 무엇인가요?
    choices:
    - id: a
      text: 세션 계층
      feedback: 맞아요. 세션 계층은 통신 대화를 시작하고 이어 가고 마치는 역할을 맡습니다.
    - id: b
      text: 표현 계층
      feedback: 표현 계층은 데이터 표현 형식을 맞추고 필요하면 변환하거나 보호합니다.
    - id: c
      text: 전송 계층
      feedback: 전송 계층은 끝에 있는 프로그램 사이로 데이터를 전달합니다.
    - id: d
      text: 데이터 링크 계층
      feedback: 데이터 링크 계층은 바로 이어진 네트워크 구간에서 프레임을 전달합니다.
    answer: a
  - id: u3-01-osi-q04
    kind: choice
    difficulty: medium
    prompt: 같은 네트워크 구간에서 바로 이웃한 장치 사이로 프레임을 전달합니다. 이 역할을 하는 계층은 무엇인가요?
    choices:
    - id: a
      text: 네트워크 계층
      feedback: 네트워크 계층은 목적지까지 갈 경로를 찾습니다.
    - id: b
      text: 데이터 링크 계층
      feedback: 맞아요. 데이터 링크 계층은 한 구간에서 이웃한 장치 사이로 프레임을 전달합니다.
    - id: c
      text: 물리 계층
      feedback: 물리 계층은 프레임의 비트를 신호로 실어 매체를 통해 보냅니다.
    - id: d
      text: 전송 계층
      feedback: 전송 계층은 두 끝의 프로그램 사이에서 데이터를 전달합니다.
    answer: b
  - id: u3-01-osi-q05
    kind: choice
    difficulty: medium
    prompt: 웹 요청이나 이름 조회처럼 프로그램이 네트워크를 이용해 제공하거나 사용하는 기능을 다룹니다. 이 역할을 하는 계층은 무엇인가요?
    choices:
    - id: a
      text: 세션 계층
      feedback: 세션 계층은 프로그램 사이의 통신 대화를 시작하고 이어 가고 마칩니다.
    - id: b
      text: 물리 계층
      feedback: 물리 계층은 비트를 전기·빛·무선 신호로 실어 보냅니다.
    - id: c
      text: 표현 계층
      feedback: 표현 계층은 데이터가 표현되는 형식과 변환을 다룹니다.
    - id: d
      text: 응용 계층
      feedback: 맞아요. 응용 계층은 프로그램이 네트워크로 이용하는 기능과 규칙을 다룹니다.
    answer: d
  - id: u3-01-osi-q06
    kind: choice
    difficulty: medium
    prompt: 출발지와 목적지의 프로그램 끝점 사이에서 데이터를 전달합니다. 이 역할을 하는 계층은 무엇인가요?
    choices:
    - id: a
      text: 전송 계층
      feedback: 맞아요. 전송 계층은 통신하는 두 끝의 프로그램 사이로 데이터를 전달합니다.
    - id: b
      text: 네트워크 계층
      feedback: 네트워크 계층은 IP 주소를 바탕으로 목적지 네트워크와 경로를 찾습니다.
    - id: c
      text: 응용 계층
      feedback: 응용 계층은 프로그램이 네트워크를 이용해 제공하거나 사용하는 기능을 다룹니다.
    - id: d
      text: 데이터 링크 계층
      feedback: 데이터 링크 계층은 바로 이웃한 장치 사이의 한 구간에서 프레임을 전달합니다.
    answer: a
  - id: u3-01-osi-q07
    kind: choice
    difficulty: medium
    prompt: 데이터를 서로 다른 형식으로 표현하는 방식을 맞추고, 필요한 경우 형식을 변환하거나 암호화·압축합니다. 이 역할을 하는 계층은 무엇인가요?
    choices:
    - id: a
      text: 데이터 링크 계층
      feedback: 데이터 링크 계층은 같은 구간에서 프레임을 전달합니다.
    - id: b
      text: 네트워크 계층
      feedback: 네트워크 계층은 목적지까지 갈 경로를 찾습니다.
    - id: c
      text: 표현 계층
      feedback: 맞아요. 표현 계층은 데이터의 표현 형식과 필요한 변환을 다룹니다.
    - id: d
      text: 세션 계층
      feedback: 세션 계층은 통신 대화를 시작하고 이어 가고 마칩니다.
    answer: c
- terms:
  - MAC 주소 (Media Access Control address)
  - 식별자 (identifier)
  - 16진수 (hexadecimal)
  - 개인정보 보호용 임시 MAC 주소
  inline_questions_after: 1
  animations:
  - file: l08-mac-address-label.svg
    title: NIC에 붙는 문패, MAC 주소
    alt: NIC마다 MAC 주소가 붙는 모습, 일반 주소에서 주소를 할당한 조직을 나타내는 앞부분, 무선 연결에서 개인 정보 보호를 위해 다른 주소를 사용할 수 있다는 점을 보여 줍니다.
    caption: 각 NIC에는 MAC 주소가 쓰입니다. 보통의 전역 주소와 무선 연결에서 쓰는 개인 정보 보호용 주소가 다를 수 있어, 앞부분만 보고 항상 제조사를 알아낼 수 있는 것은 아닙니다.
  questions:
  - id: u3-01-p05-q01
    kind: choice
    difficulty: easy
    prompt: 집집마다 문패로 구분하듯, 가까운 네트워크에서 연결 지점을 구분하는 주소는 무엇인가요?
    choices:
    - id: a
      text: 프레임 크기
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: MAC 주소
      feedback: 맞아요. MAC 주소.
    - id: c
      text: HTTP 주소
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: bps
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: Metric
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-01-p05-q02
    kind: choice
    difficulty: medium
    prompt: Wi-Fi에서 네트워크별 임시 MAC 주소를 사용할 수 있다는 설명으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 개인 주소를 쓰면 연결 지점에 주소가 필요 없다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 모든 Wi-Fi 장치의 MAC 주소는 항상 제조사 이름을 그대로 담는다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 한 장치에는 NIC가 몇 개든 MAC 주소가 하나만 있다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 개인 주소는 IP 주소와 역할이 완전히 같다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 제품에 적힌 MAC 주소와 다른 네트워크별 주소를 사용할 수 있다
      feedback: 맞아요. 제품에 적힌 MAC 주소와 다른 네트워크별 주소를 사용할 수 있다.
    answer: e
  - id: u3-01-p05-q04
    kind: choice
    difficulty: medium
    prompt: "일반적인 MAC 주소는 보통 몇 비트인가요?"
    choices:
    - id: a
      text: "8비트"
      feedback: "다시 본문을 확인해 보세요. 8비트."
    - id: b
      text: "16비트"
      feedback: "다시 본문을 확인해 보세요. 16비트."
    - id: c
      text: "32비트"
      feedback: "다시 본문을 확인해 보세요. 32비트."
    - id: d
      text: "64비트"
      feedback: "다시 본문을 확인해 보세요. 64비트."
    - id: e
      text: "48비트"
      feedback: "맞아요. 48비트입니다."
    answer: e
  - id: u3-01-p05-q05
    kind: choice
    difficulty: medium
    prompt: Wi-Fi와 USB Ethernet NIC가 하나씩 있는 노트북의 MAC 주소를 어떻게 이해하면 좋나요?
    choices:
    - id: a
      text: 노트북 한 대이므로 MAC 주소도 반드시 하나다
      feedback: NIC가 여러 개면 연결 지점별 MAC 주소가 쓰일 수 있습니다.
    - id: b
      text: 두 인터페이스가 반드시 같은 MAC 주소를 쓴다
      feedback: 인터페이스마다 다른 MAC 주소를 쓸 수 있습니다.
    - id: c
      text: 두 NIC 모두 MAC 주소 대신 포트 번호를 쓴다
      feedback: 포트 번호와 MAC 주소는 다른 값입니다.
    - id: d
      text: 연결 지점마다 서로 다른 MAC 주소가 사용될 수 있다
      feedback: 맞아요. MAC 주소는 컴퓨터가 아니라 연결 지점별로 쓰일 수 있습니다.
    - id: e
      text: MAC 주소는 인터넷 전체의 경로를 선택한다
      feedback: MAC 주소는 가까운 네트워크에서 연결 지점을 구분합니다.
    answer: d
- terms:
  - 프레임 (Frame)
  - L2 (Layer 2, 계층 2)
  - 패킷 (Packet)
  inline_questions_after: 2
  questions:
  - id: u3-01-p06-q01
    kind: choice
    difficulty: easy
    prompt: 택배 내용물 자체와 한 구간에서 쓰는 포장을 구분하듯, 한 링크에서 데이터를 전달하는 포장은 무엇인가요?
    choices:
    - id: a
      text: 패킷
      feedback: 패킷은 목적지까지 운반되는 데이터입니다.
    - id: b
      text: NIC
      feedback: NIC는 네트워크 연결 장치입니다.
    - id: c
      text: 프레임
      feedback: 맞아요. 프레임은 한 링크에서 데이터를 전달하는 포장에 비유할 수 있습니다.
    - id: d
      text: LAN
      feedback: LAN은 네트워크의 범위를 나타냅니다.
    - id: e
      text: MAC 주소
      feedback: MAC 주소는 네트워크 연결 지점을 구분하는 값입니다.
    answer: c
  - id: u3-01-p06-q02
    kind: choice
    difficulty: medium
    prompt: 패킷과 프레임의 관계를 가장 잘 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 패킷과 프레임은 크기와 역할이 늘 같다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 프레임은 네트워크 장치이고 패킷은 케이블이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 패킷은 목적지까지의 데이터이고 프레임은 가까운 링크 구간의 전달에 쓰인다
      feedback: 맞아요. 패킷은 목적지까지의 데이터이고 프레임은 가까운 링크 구간의 전달에 쓰인다.
    - id: d
      text: 프레임에는 MAC 주소를 사용할 수 없다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 프레임은 항상 인터넷 전체를 한 번에 건넌다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-01-p06-q03
    kind: short
    prompt: 같은 L2 구간에서 데이터 전달에 사용하는 묶음을 영어로 무엇이라고 하나요?
    answers:
    - frame
    - ethernet frame
    - 프레임
    - Ethernet 프레임
    feedback: 정답은 frame(Ethernet 프레임)입니다.
  - id: u3-01-p06-q04
    kind: choice
    difficulty: medium
    prompt: "노트북에서 공유기를 지나 다음 네트워크로 갈 때 프레임은 어떻게 될 수 있나요?"
    choices:
    - id: a
      text: "처음 만든 프레임을 목적지까지 그대로 사용한다"
      feedback: "프레임은 한 링크 구간에 쓰이는 포장입니다."
    - id: b
      text: "다음 구간의 링크에 맞춰 새 프레임으로 바뀔 수 있다"
      feedback: "맞아요. 링크 구간이 바뀌면 새 프레임을 사용할 수 있습니다."
    - id: c
      text: "프레임을 쓰면 패킷은 사라진다"
      feedback: "패킷은 프레임의 데이터 부분에 실릴 수 있습니다."
    - id: d
      text: "공유기는 프레임을 전달하지 않는다"
      feedback: "공유기를 지나는 각 링크에서 프레임을 사용할 수 있습니다."
    - id: e
      text: "패킷과 프레임은 항상 크기와 역할이 같다"
      feedback: "패킷은 목적지까지의 데이터이고 프레임은 한 링크용 포장입니다."
    answer: b
  - id: u3-01-p06-q05
    kind: choice
    difficulty: medium
    prompt: 기판 내장형, USB 유선형, 무선형 NIC는 모양과 연결 방식이 달라도 무엇이 같은가요?
    choices:
    - id: a
      text: 네트워크와 정보를 주고받는 연결 역할
      feedback: 맞아요. NIC는 모양과 연결 방식이 달라도 네트워크 연결 역할을 합니다.
    - id: b
      text: 반드시 같은 제조사가 만든다는 점
      feedback: 제조사가 달라도 같은 연결 역할을 할 수 있습니다.
    - id: c
      text: 모두 케이블을 꽂는 구멍이 있다는 점
      feedback: 무선 NIC에는 케이블 구멍이 없을 수 있습니다.
    - id: d
      text: 모두 컴퓨터 밖에 별도 부품으로 연결된다는 점
      feedback: 메인보드 내장형 NIC도 있습니다.
    - id: e
      text: 모두 무선 신호만 사용한다는 점
      feedback: 유선 NIC는 케이블로 연결될 수 있습니다.
    answer: a
  animations:
  - file: l08-frame-per-link.svg
    title: "NIC가 주고받는 L2 프레임"
    alt: "기판에 끼우는 카드, USB 유선 어댑터, 무선 NIC 세 가지 모양이 먼저 나란히 보입니다. 노트북에서 주황 패킷이 준비되고, MAC 칸이 붙은 파란 Wi-Fi 프레임이 패킷을 감싼 채 무선 구간을 지나 공유기에 도착합니다. 공유기에서 포장이 민트색 Ethernet 프레임으로 바뀌고, 같은 패킷이 다음 장비로 이어집니다."
    caption: "NIC는 모양이 달라도 같은 역할을 하며, 같은 링크의 이웃에게 보낼 때 L2 단위인 프레임을 씁니다. 프레임은 패킷을 감싸는 한 구간용 포장이라 구간마다 새로 쓰일 수 있습니다."
- terms:
  - Ethernet
  - MTU (Maximum Transmission Unit)
  - FCS (Frame Check Sequence)
  - Jumbo Frame
  - 바이트 (Byte)
  inline_questions_after: 1
  questions:
  - id: u3-01-p07-q01
    kind: choice
    difficulty: easy
    prompt: 일반 Ethernet의 MTU는 프레임 안에 담기는 데이터의 최대 크기를 얼마로 정하나요?
    choices:
    - id: a
      text: 48바이트
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 1,500바이트
      feedback: 맞아요. 1,500바이트.
    - id: c
      text: 1,024바이트
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 10KB로 항상 고정
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 1,514바이트
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-01-p07-q02
    kind: choice
    difficulty: medium
    prompt: Ethernet 프레임 크기가 문서에 따라 1,514바이트 또는 1,518바이트로 보일 수 있는 이유는 무엇인가요?
    choices:
    - id: a
      text: 모든 장비가 Jumbo Frame을 사용하기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 한 값은 비트 단위이고 다른 값은 초 단위다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 두 수치는 LAN과 WAN의 거리 차이를 뜻한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 프레임이 전송될 때마다 내용이 자동으로 두 배가 된다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 마지막 검사 값을 크기에 포함하는지 달라질 수 있다
      feedback: 맞아요. 마지막 검사 값을 크기에 포함하는지 달라질 수 있다.
    answer: e
  - id: u3-01-p07-q04
    kind: choice
    difficulty: medium
    prompt: "Jumbo Frame 크기에 대한 설명으로 맞는 것은 무엇인가요?"
    choices:
    - id: a
      text: "모든 네트워크에서 똑같이 10KB로 고정된다"
      feedback: "Jumbo Frame 크기는 장비와 설정에 따라 달라집니다."
    - id: b
      text: "장비와 설정에 따라 허용 크기가 달라질 수 있다"
      feedback: "맞아요. 모든 네트워크가 같은 크기를 쓰지는 않습니다."
    - id: c
      text: "항상 파일 하나를 프레임 하나에 담는 크기다"
      feedback: "큰 파일은 여러 프레임에 나뉘어 전송될 수 있습니다."
    - id: d
      text: "무선 네트워크에만 사용하는 프레임이다"
      feedback: "Jumbo Frame은 Ethernet의 큰 프레임을 허용하는 기능입니다."
    - id: e
      text: "MAC 주소가 길어진다는 뜻이다"
      feedback: "Jumbo Frame은 프레임 크기에 관한 말입니다."
    answer: b
  - id: u3-01-p07-q05
    kind: choice
    difficulty: medium
    prompt: 프레임 크기와 1Gbps 같은 전송 속도는 어떻게 다른가요?
    choices:
    - id: a
      text: 프레임 크기는 한 번에 담는 양, 속도는 시간당 보내는 양이다
      feedback: 맞아요. 한 번의 양과 시간에 따른 양은 다른 기준입니다.
    - id: b
      text: 두 값은 모두 MAC 주소의 길이를 나타낸다
      feedback: MAC 주소 길이와 프레임 크기·속도는 다릅니다.
    - id: c
      text: 프레임 크기는 초당 전송량이고 속도는 한 프레임의 크기다
      feedback: 두 설명이 뒤바뀌었습니다.
    - id: d
      text: 1Gbps는 프레임 하나가 1기가바이트라는 뜻이다
      feedback: Gbps는 초당 비트 수를 나타냅니다.
    - id: e
      text: 둘 다 네트워크 범위를 뜻한다
      feedback: 네트워크 범위는 LAN·MAN·WAN과 관련된 분류입니다.
    answer: a
  animations:
  - file: l08-frame-size.svg
    title: "프레임 크기 세는 법"
    alt: "MTU 1,500바이트 표시 아래 프레임 데이터 칸이 놓이고, 앞에 Ethernet 헤더 14바이트, 뒤에 오류 확인값 FCS 4바이트가 붙습니다. 모두 세면 1,518바이트이며, FCS를 제외해 표시하면 1,514바이트입니다. 이어서 큰 사진 파일은 여러 프레임으로 나뉘고, 데이터 칸이 더 큰 Jumbo Frame은 허용 크기가 장비와 설정마다 다르다는 점을 보여 줍니다."
    caption: "일반 Ethernet MTU 1,500바이트는 프레임 안 데이터의 최대 크기입니다. 헤더 14바이트와 FCS(오류 확인값) 4바이트를 더하면 1,518바이트이며, FCS를 제외해 세면 1,514바이트로 표시될 수 있습니다."
- terms:
  - 비트 (bit)
  - 바이트 (Byte)
  - bps (bits per second)
  - 기가비트 (Gigabit)
  inline_questions_after: 1
  animations:
  - file: l08-bit-vs-byte-speed.svg
    title: 소문자 b와 대문자 B, 8배의 차이
    alt: 작은 물방울 8개가 모여 병 하나가 되고, 그 아래 b와 B 글자가 나란히 놓입니다. 이어서 1Gbps 눈금이 약 125MB/s 눈금으로
      환산됩니다.
    caption: 8비트가 1바이트이므로 1Gbps는 초당 1GB가 아니라 약 0.125GB입니다.
  questions:
  - id: u3-01-p08-q01
    kind: choice
    difficulty: easy
    prompt: 수도꼭지에서 1초 동안 흐르는 물의 양을 세듯, bps에서 소문자 b는 어떤 정보 단위를 뜻하나요?
    choices:
    - id: a
      text: Byte
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Frame
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: second
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: bit
      feedback: 맞아요. bit.
    - id: e
      text: Host
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-01-p08-q02
    kind: choice
    difficulty: medium
    prompt: 1Gbps를 이론상 바이트 전송량으로 바꾸면 초당 약 얼마인가요?
    choices:
    - id: a
      text: 125MB/s
      feedback: 맞아요. 이론상 약 125MB/s입니다.
    - id: b
      text: 1,000MB
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 1GB
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 1MB
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 8MB
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-01-p08-q03
    kind: short
    prompt: 8개의 bit가 모여 이루는 정보 용량 단위입니다. 영어 단어로 답해주세요.
    answers:
    - byte
    - bytes
    - 바이트
    feedback: 정답은 byte(바이트)입니다.
  - id: u3-01-p08-q04
    kind: choice
    difficulty: medium
    prompt: "이론상 1GB 파일을 125MB/s로 보내면 최소 얼마나 걸릴까요?"
    choices:
    - id: a
      text: "약 8초"
      feedback: "맞아요. 1,000MB를 125MB/s로 나누면 약 8초입니다."
    - id: b
      text: "약 1초"
      feedback: "1,000MB를 125MB/s로 나누어 보세요."
    - id: c
      text: "약 8분"
      feedback: "1,000MB를 125MB/s로 나누면 초 단위가 나옵니다."
    - id: d
      text: "약 80초"
      feedback: "나눗셈을 다시 해 보세요. 1,000 ÷ 125입니다."
    - id: e
      text: "약 800초"
      feedback: "나눗셈을 다시 해 보세요. 1,000 ÷ 125입니다."
    answer: a
  - id: u3-01-p08-q05
    kind: choice
    difficulty: medium
    prompt: 실제 다운로드 속도가 1Gbps를 8로 나눈 값보다 낮을 수 있는 이유는 무엇인가요?
    choices:
    - id: a
      text: Byte와 bit가 같은 단위라서
      feedback: Byte는 8 bit입니다.
    - id: b
      text: bps는 초당 바이트 수라서
      feedback: bps는 초당 비트 수입니다.
    - id: c
      text: 파일 크기가 항상 bit로만 표시되어서
      feedback: 파일 크기 단위만으로 실제 속도가 정해지지는 않습니다.
    - id: d
      text: 1Gbps는 실제 전송 효율과 무관한 보장 속도라서
      feedback: 1Gbps라는 표기만으로 실제 다운로드 속도가 보장되지는 않습니다.
    - id: e
      text: 추가 정보와 장비 처리, 네트워크 혼잡 등의 영향이 있어서
      feedback: 맞아요. 실제 전송에는 여러 오버헤드와 환경 요인이 있습니다.
    answer: e
- terms:
  - 광섬유 케이블
  - Ethernet (이더넷)
  inline_questions_after: 1
  questions:
  - id: u3-01-p09-q01
    kind: choice
    difficulty: easy
    prompt: 구리 케이블이 전기 신호를 나르는 선이라면, 광섬유 케이블은 무엇을 이용해 신호를 전달하나요?
    choices:
    - id: a
      text: 전기 신호만
      feedback: 전기 신호는 구리 케이블에서 사용합니다.
    - id: b
      text: 전파 신호만
      feedback: 이 페이지에서는 광섬유가 빛 신호를 전달한다고 설명합니다.
    - id: c
      text: 빛 신호
      feedback: 맞아요. 광섬유는 빛 신호를 전달합니다.
    - id: d
      text: 소리 신호
      feedback: 이 페이지에서 설명한 신호 방식은 전기와 빛입니다.
    - id: e
      text: 자석의 힘만
      feedback: 이 페이지에서 설명한 신호 방식은 전기와 빛입니다.
    answer: c
  - id: u3-01-p09-q02
    kind: choice
    difficulty: medium
    prompt: Mac에서 연결 지점 이름과 ether 값을 확인할 때 사용할 수 있는 명령은 무엇인가요?
    choices:
    - id: a
      text: network speed
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: ipconfig /all
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: route print
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: ether print
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: ifconfig
      feedback: 맞아요. ifconfig.
    answer: e
  - id: u3-01-p09-q03
    kind: short
    prompt: 유선 LAN에서 널리 쓰이며 데이터 프레임과 연결되는 네트워크 기술입니다. 영어로 답해주세요.
    answers:
    - ethernet
    - 이더넷
    feedback: 정답은 Ethernet(이더넷)입니다.
  - id: u3-01-p09-q04
    kind: choice
    difficulty: medium
    prompt: "Windows에서 네트워크 연결 지점과 MAC 주소를 자세히 확인할 때 사용할 수 있는 명령은 무엇인가요?"
    choices:
    - id: a
      text: "ifconfig"
      feedback: "이 Lesson에서는 Windows에서 ipconfig /all, Mac에서 ifconfig를 소개합니다."
    - id: b
      text: "route print"
      feedback: "route print는 경로 정보를 확인하는 명령입니다."
    - id: c
      text: "ipconfig /all"
      feedback: "맞아요. Windows에서 ipconfig /all로 연결 항목과 주소를 확인할 수 있습니다."
    - id: d
      text: "ping /all"
      feedback: "이 Lesson에서 소개한 Windows 명령은 ipconfig /all입니다."
    - id: e
      text: "mac print"
      feedback: "이 Lesson에서 소개한 Windows 명령은 ipconfig /all입니다."
    answer: c
  - id: u3-01-p09-q05
    kind: choice
    difficulty: medium
    prompt: ipconfig /all 결과에서 'Physical Address' 또는 Mac의 ifconfig 결과에서 'ether' 옆에 보이는 값은 무엇인가요?
    choices:
    - id: a
      text: 링크 속도
      feedback: 링크 속도는 Mbps 등으로 표시됩니다.
    - id: b
      text: MAC 주소
      feedback: 맞아요. 해당 항목이 인터페이스의 MAC 주소입니다.
    - id: c
      text: 프레임 크기
      feedback: 프레임 크기는 이 출력의 Physical Address나 ether 값이 아닙니다.
    - id: d
      text: 포트 번호
      feedback: 포트 번호는 프로그램 통신을 구분하는 값입니다.
    - id: e
      text: 네트워크 이름
      feedback: 네트워크 이름은 Physical Address나 ether 값과 다릅니다.
    answer: b

  animations:
  - file: l08-find-my-interface.svg
    title: "내 컴퓨터에서 연결 지점 찾기"
    alt: "명령 프롬프트 창에 ipconfig /all이 입력되고 무선 LAN 어댑터 Wi-Fi와 Ethernet 어댑터 항목이 나타납니다. 어댑터 이름 줄에는 인터페이스, Physical Address 줄에는 MAC 주소 꼬리표가 붙고, 두 어댑터가 모두 강조되어 인터페이스가 둘임을 보여 줍니다. 이어서 Mac 터미널의 ifconfig 화면에서 en0과 ether 값이 같은 방식으로 표시되고, 마지막에 전송률 866 Mbps를 8로 나눈 약 108 MB/s 카드가 나옵니다."
    caption: "ipconfig /all이나 ifconfig 화면에서 Wi-Fi·Ethernet 같은 항목 이름이 인터페이스, Physical Address나 ether 값이 MAC 주소입니다. Mbps를 8로 나눈 값은 단위를 바꾼 어림값이지 실제 다운로드 속도가 아닙니다."
animations_dir: units/03-layer2-switching/lessons/01-nic-l2-frame-lan-카드-그리고-mac-주소/assets/animations
---
앞 Lesson에서는 택배가 여러 사람과 장소를 거쳐 받는 사람에게 가는 큰 흐름을 살펴봤습니다. 이번 Lesson에서는 그 여정에 참여하는 컴퓨터와 네트워크가 어디에서 맞닿는지, 그 연결 지점에 어떤 안내가 붙는지 알아봅니다. 컴퓨터를 집, 연결 지점을 문, 가까운 범위의 네트워크를 마을이라고 생각해 보세요. 비유가 실제 구조와 완전히 같지는 않으니, 각 용어가 무엇을 가리키는지만 차근차근 연결하면 됩니다.

## NIC와 LAN 카드
<!-- learn-page-id: interface-definition -->

새 노트북의 사양표에서 ‘무선 랜 카드’라는 말을 볼 수 있습니다. 컴퓨터 안에서 문서를 만들거나 계산하는 것만으로는 다른 컴퓨터에 파일을 보낼 수 없습니다. 네트워크와 신호를 주고받을 장치가 있어야 합니다. 이 장치를 LAN 카드 또는 NIC(Network Interface Card)라고 부릅니다. 예를 들어 노트북 사양의 ‘Realtek 무선 LAN’은 무선 네트워크에 연결하는 NIC의 제조사와 종류를 나타내는 말입니다. Realtek은 연결 장치의 다른 이름이 아니라 회사 이름입니다.

컴퓨터를 집 한 채라고 생각하면 NIC는 집과 바깥을 잇는 문이고, 인터페이스는 그 문이 네트워크와 맞닿는 연결 지점입니다. 집 안에서 끝나는 일은 이 문을 지나지 않지만, 웹페이지를 열거나 사진을 보내는 정보는 네트워크로 나갈 때 연결 지점을 거칩니다. 비유가 실제 구조와 똑같지는 않습니다. 현관문은 사람이 드나드는 물리적인 문이지만 NIC는 데이터를 전기 신호나 무선 신호로 주고받는 전자 장치입니다. 또 이름에 ‘카드’가 들어가도 반드시 카드처럼 따로 꽂는 부품일 필요는 없습니다. 메인보드에 내장된 장치도 NIC입니다.

따라서 용어를 볼 때는 ‘LAN 카드’, ‘NIC’, ‘네트워크 인터페이스’를 문맥에 맞춰 연결해 읽으면 됩니다. 엄밀히 말하면 NIC는 장치이고 인터페이스는 네트워크와 맞닿는 논리적 연결 지점이지만, 입문 자료와 운영체제 화면에서는 이 둘을 가깝게 부르기도 합니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** NIC는 네트워크와 신호를 주고받는 장치이고, 인터페이스는 네트워크와 맞닿는 연결 지점이다.
- **적용하기 (Apply):** 유선 NIC와 무선 NIC의 연결 방식이 달라도 같은 역할을 하는 이유를 말한다.
- **찾아보기 (Lookup):** NIC의 속도와 지원 규격은 운영체제 정보나 장치 사양에서 확인한다.

## Host와 네트워크 인터페이스

네트워크에 연결된 컴퓨터나 장치 한 대를 이 Lesson에서는 호스트(Host)라고 부릅니다. 노트북, 데스크톱, 서버, 네트워크에 연결된 프린터가 각각 호스트의 예입니다. 그림에서는 호스트를 네모 하나로, 네트워크와 맞닿는 인터페이스를 네모 가장자리의 진한 점으로 그리기도 합니다. 네모 하나에 점 두 개가 있으면 컴퓨터가 두 대라는 뜻이 아니라, 호스트 한 대에 연결 지점이 두 개 있다는 뜻입니다.

예를 들어 노트북에는 Wi-Fi NIC가 기본으로 들어 있고, USB 유선 어댑터를 꽂으면 유선 이더넷(Ethernet) 연결 지점이 하나 더 생길 수 있습니다. 무선 쪽은 무선 신호를 중계하는 액세스 포인트(보통 가정용 공유기에 함께 들어 있음)에 연결하고, 유선 쪽에는 랜 케이블을 꽂습니다. 노트북 한 대가 두 연결 지점을 가진 셈입니다. 집의 문과 달리 Wi-Fi 인터페이스에는 케이블을 꽂는 구멍이 없지만, 네트워크와 이어지는 연결이므로 인터페이스 하나로 셉니다.

여기서 ‘포트’라는 말을 만나면 문맥을 살펴야 합니다. 컴퓨터 옆의 Ethernet 케이블 구멍도 일상적으로 포트라고 부르지만, 나중에 배울 TCP/UDP 포트 번호는 프로그램의 통신 통로를 구분하는 번호입니다. 구멍과 번호는 서로 다른 개념입니다. 또 서버를 제공하는 서비스도 ‘호스트’라 부르는 경우가 있지만, 이 Lesson에서는 네트워크에 연결된 장치 한 대라는 뜻으로 사용합니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Host는 통신 끝 장치이고 네트워크 인터페이스는 네트워크에 닿는 연결점이다.
- **적용하기 (Apply):** 한 노트북에 Wi-Fi와 Ethernet 연결이 각각 있을 때 Host 수와 인터페이스 수를 구분한다.
- **찾아보기 (Lookup):** 운영체제의 네트워크 설정에서 Wi-Fi와 Ethernet처럼 컴퓨터에 등록된 인터페이스 목록을 찾아본다.

## LAN과 네트워크 규모
<!-- learn-page-id: lan-wan-definition -->

LAN, MAN, WAN은 네트워크가 어느 정도 범위에 걸쳐 있는지 설명하는 이름입니다. LAN(Local Area Network)은 집이나 사무실처럼 비교적 가까운 범위, MAN(Metropolitan Area Network)은 도시 규모, WAN(Wide Area Network)은 그보다 넓은 범위를 가리킵니다.

집의 공유기에 휴대전화와 태블릿은 Wi-Fi로, 방의 데스크톱과 TV 셋톱박스는 랜 케이블로 연결되어 있다고 해 봅시다. 연결 방식은 달라도 이 장치들이 집 안에서 함께 통신하는 가까운 네트워크를 LAN의 예로 볼 수 있습니다. LAN이 반드시 케이블만 쓰거나 컴퓨터만 연결한다는 뜻은 아닙니다. 집, 사무실, 학교 실습실처럼 비교적 좁은 범위에서 여러 장치가 연결된 환경을 떠올리면 됩니다.

LAN을 마을 하나, MAN을 도시, WAN을 더 넓은 지역으로 생각하면 범위의 차이를 기억하기 쉽습니다. 다만 지도에서 도시의 넓이가 성능을 말해 주지 않듯이, LAN·MAN·WAN도 속도나 품질의 순위가 아닙니다. LAN과 MAN 사이에 몇 킬로미터라는 고정된 경계가 있는 것도 아닙니다. 이 이름들은 네트워크가 어느 정도의 범위를 아우르는지 설명하는 분류입니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** LAN·MAN·WAN은 연결 범위의 크기를 설명하는 구분이다.
- **적용하기 (Apply):** 집·도시·광역 연결 사례를 범위에 따라 구분한다.
- **찾아보기 (Lookup):** 공유기에서 LAN과 WAN이라고 표시된 연결을 찾아보고, 장비의 포트 이름과 네트워크 범위의 뜻을 구별한다.

## 택배 여정으로 기억하는 OSI 7계층
<!-- learn-page-id: osi-seven-layer-order -->

Unit 1에서 계층을 층층이 그린 지도를 봤고, Unit 2에서는 상자가 여러 장소와 사람을 거쳐 도착하는 택배 여정을 따라갔습니다. 이제 그 지도를 네트워크 통신에 적용해 봅니다. OSI 7계층은 통신에서 필요한 일을 일곱 역할로 나누어 설명하는 모델입니다. 아래 표를 택배 여정과 함께 읽으며 먼저 이름과 순서를 익혀 보세요.

| 위에서 아래 | 이름 | 하는 일 한 줄 | 택배에서 떠올릴 장면 |
|---|---|---|---|
| 7 | 응용(Application) | 네트워크를 쓰는 프로그램이 제공할 일을 정한다 | 보내려는 물건이나 요청을 정한다 |
| 6 | 표현(Presentation) | 데이터의 표현 형식을 맞추고 필요하면 바꾸거나 보호한다 | 내용을 읽을 수 있는 형식으로 준비한다 |
| 5 | 세션(Session) | 통신 대화를 시작하고 이어 가고 마친다 | 배송에 필요한 대화를 열고 마무리한다 |
| 4 | 전송(Transport) | 두 끝의 프로그램 사이에서 데이터를 전달한다 | 보낸 쪽과 받을 쪽 사이의 배송을 맡긴다 |
| 3 | 네트워크(Network) | 목적지까지 갈 경로를 찾는다 | 주소를 보고 지역과 경로를 정한다 |
| 2 | 데이터 링크(Data Link) | 바로 이어진 네트워크 구간에서 프레임을 전달한다 | 이웃한 분류 장소 사이에서 상자를 넘긴다 |
| 1 | 물리(Physical) | 비트를 전기·빛·무선 신호로 실어 보낸다 | 도로와 차량처럼 실제 이동 수단을 떠올린다 |

위에서 아래로 읽으면 **응용 → 표현 → 세션 → 전송 → 네트워크 → 데이터 링크 → 물리**입니다. 짧게 소리 내어 “응·표·세 / 전·네 / 데·물”로 끊어 읽어도 좋아요. 이 이름과 순서가 오늘의 기억 목표입니다. 각 계층에서 실제로 어떤 프로토콜과 장치가 쓰이는지는 뒤 Unit에서 하나씩 만납니다.

택배 장면은 각 계층의 이름과 역할을 떠올리게 하는 기억 보조입니다. 실제 인터넷 통신이 택배 회사의 일곱 부서처럼 정확히 나뉘거나, 매번 같은 순서의 담당자를 거친다는 뜻은 아닙니다. OSI도 현실의 모든 프로토콜이 꼭 한 층씩 깔끔하게 들어맞는다는 규칙이 아니라 통신 기능을 설명하고 비교하는 참조 모델입니다. 여기서는 비유의 세부를 외우기보다 일곱 역할의 순서를 기억하세요.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** OSI 7계층을 위에서 아래로 응용·표현·세션·전송·네트워크·데이터 링크·물리 순서로 말한다.
- **적용하기 (Apply):** 네트워크 장치나 기술을 살펴볼 때 어느 계층의 역할과 관련 있는지 뒤의 학습과 연결한다.
- **찾아보기 (Lookup):** 계층별 구체적인 프로토콜과 데이터 단위는 뒤 Unit의 해당 Page에서 확인한다.

## MAC 주소 · NIC의 식별자
<!-- learn-page-id: mac-address-definition -->

집의 출입문마다 구별하는 번호표를 붙이듯, 네트워크 연결 지점마다 MAC(Media Access Control) 주소를 사용합니다. MAC 주소는 가까운 네트워크에서 데이터를 어느 연결 지점으로 보낼지 구별하는 값입니다. 그래서 앞 Page의 비유를 이어, MAC 주소를 네트워크 문에 붙은 문패라고 생각할 수 있습니다.

주소는 보통 `AA-BB-CC-11-22-33`처럼 두 글자씩 여섯 묶음으로 적습니다. 콜론으로 `AA:BB:CC:11:22:33`처럼 쓰기도 합니다. 각 글자는 0~9 또는 A~F를 쓰는 16진수 한 자리입니다. 16진수 한 자리는 4비트를 나타내므로 두 자리는 8비트, 즉 1바이트에 해당합니다. 여섯 묶음 전체는 6바이트(48비트)입니다. 이렇게 나누어 적으면 긴 값을 사람이 읽고 비교하기 쉽습니다.

공식적으로 배정된 일반 MAC 주소는 앞부분으로 주소를 배정받은 조직을 알아볼 수 있는 경우가 있습니다. 그 조직은 NIC 제조사일 수 있지만, 화면에 보이는 모든 MAC 주소가 제조사를 알려 주는 것은 아닙니다. 스마트폰과 노트북은 Wi-Fi에서 개인정보를 보호하려고 제품에 정해진 주소 대신 네트워크별 임시 MAC 주소를 사용할 수 있습니다. 예를 들어 집 Wi-Fi와 카페 Wi-Fi에서 서로 다른 주소를 보일 수 있고, 제품 라벨의 주소와도 다를 수 있습니다. 따라서 MAC 주소를 연결 지점의 문패로 기억하되, 문패가 언제나 제품에 적힌 값 그대로라고 생각하지는 마세요.

노트북에 Wi-Fi와 USB Ethernet, 두 NIC가 있다면 각각의 인터페이스에 서로 다른 MAC 주소가 사용됩니다. 그래서 MAC 주소는 컴퓨터 한 대에 무조건 하나만 있는 값이 아닙니다. 또 MAC 주소와 IP 주소는 둘 다 주소처럼 보이지만 역할이 다릅니다. 지금은 MAC 주소를 가까운 네트워크 구간에서 연결 지점을 구별할 때 쓰는 문패로 기억하고, IP 주소와 두 주소가 함께 쓰이는 과정은 뒤에서 배웁니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** MAC 주소는 가까운 네트워크에서 각 연결 지점을 구별하는 값이다.
- **적용하기 (Apply):** Wi-Fi와 유선 연결을 모두 가진 노트북에서 연결 지점마다 MAC 주소가 따로 쓰일 수 있는 이유를 설명한다.
- **찾아보기 (Lookup):** 네트워크 설정에서 Wi-Fi와 유선 인터페이스의 MAC 주소를 찾아보고, 임시 주소가 제품 라벨의 주소와 다를 수 있는 이유를 확인한다.

## NIC가 네트워크로 보내는 한 구간의 프레임
<!-- learn-page-id: frame-definition -->

네트워크 연결 장치는 여러 모양으로 만들 수 있습니다. 컴퓨터 안 기판에 끼우는 카드도 있고, USB에 꽂아 케이블을 연결하는 장치나 무선으로 연결하는 장치도 있습니다. 모양과 연결 방식은 달라도 네트워크와 정보를 주고받는 연결 지점이라는 역할은 같습니다.

NIC를 통해 직접 연결된 한 구간(링크, link)의 이웃 장치로 데이터를 보낼 때 사용하는 2계층(L2) 데이터 단위가 프레임(Frame)입니다. 예를 들어 노트북이 집 공유기로 데이터를 보낼 때, 그 한 구간에서 Ethernet 또는 Wi-Fi 프레임을 사용합니다. 앞에서 택배 상자에 비유한 패킷이 목적지를 향해 운반되는 내용이라면, 프레임은 한 구간을 건너기 위해 그 내용을 둘러싸는 운송 포장이라고 생각할 수 있습니다. 패킷을 프레임의 데이터 부분에 담고, 그 구간에서 보낼 곳과 보낸 곳을 식별하는 MAC 주소 같은 정보를 붙입니다.

택배 비유로 흐름을 따라가 보겠습니다. 노트북에서 공유기로 보내는 첫 구간에서는 노트북이 프레임을 만들어 무선으로 보냅니다. 공유기를 지난 다음 다른 네트워크로 향하는 구간에서는 링크 기술과 다음 전달 상대에 맞춰 새 프레임을 사용할 수 있습니다. 그러므로 프레임은 목적지까지 내내 그대로 따라가는 상자가 아니라, 링크 구간마다 쓰이는 포장에 가깝습니다. 비유는 ‘한 구간의 전달 단위’라는 점을 잡기 위한 것이며 실제 데이터 구조는 뒤에서 자세히 다룹니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** NIC는 네트워크 연결을 맡고, 프레임은 직접 연결된 한 구간에서 데이터를 전달한다.
- **적용하기 (Apply):** 노트북에서 공유기까지와 공유기 이후 구간에서 프레임이 달라질 수 있는 까닭을 설명한다.
- **찾아보기 (Lookup):** USB 유선 어댑터와 Wi-Fi 어댑터의 제품 사양에서 연결 방식과 지원 속도를 비교한다.

## Ethernet 프레임에는 얼마까지 담을 수 있을까?

앞 페이지에서 프레임은 한 구간을 건너기 위한 운송 포장이라고 배웠습니다. 이 포장에 담을 수 있는 데이터에도 크기 한계가 있습니다. 일반 Ethernet의 MTU(Maximum Transmission Unit, 최대 전송 단위) 1,500바이트는 프레임 전체가 아니라 그 안에 담기는 데이터 부분의 최대 크기입니다. 흔히 이 데이터가 IP 패킷입니다.

프레임 크기는 앞쪽 Ethernet 헤더, 데이터, 뒤쪽 FCS를 더해 셉니다. FCS(Frame Check Sequence)는 전송 중 오류가 있었는지 확인하는 값입니다.

| Ethernet 프레임 부분 | 크기 | 역할 |
| --- | ---: | --- |
| 앞쪽 헤더 | 14바이트 | 프레임 전달에 필요한 정보 |
| 데이터 | 최대 1,500바이트 | 보통 IP 패킷을 담음 |
| 뒤쪽 FCS | 4바이트 | 오류 확인에 쓰는 값 |
| **전체** | **최대 1,518바이트** | **14 + 1,500 + 4** |

문서나 관찰 도구가 FCS를 세지 않으면 같은 프레임을 1,514바이트로 표시할 수 있습니다. 따라서 숫자를 비교할 때는 FCS를 포함했는지 확인해야 합니다.

일반 크기보다 큰 프레임을 허용하는 Jumbo Frame도 있지만, 어느 크기까지 쓸 수 있는지는 장비와 설정에 따라 달라집니다. 모든 네트워크가 같은 점보 프레임 크기를 쓰는 것은 아니므로 ‘항상 10KB’처럼 외우지 마세요. 큰 사진 파일 하나가 한 프레임에 통째로 들어가는 것도 아닙니다. 전송할 데이터는 프레임 크기에 맞춰 여러 단위로 나뉘어 오갈 수 있습니다. 지금은 `1,500바이트`가 일반 Ethernet의 데이터 부분 크기 기준이라는 점과, 프레임 전체 크기는 헤더·FCS 포함 여부에 따라 달라진다는 점을 기억하면 됩니다.

장비 사양에는 프레임 크기와 함께 `1Gbps` 같은 속도도 표시됩니다. 프레임 크기는 한 번에 담는 양이고, 속도는 일정 시간 동안 얼마나 많이 보내는지를 말하므로 서로 다른 값입니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 일반 Ethernet의 MTU 1,500바이트는 프레임 안의 데이터 부분 한도이며, 프레임 전체 크기와 다르다.
- **적용하기 (Apply):** Ethernet 헤더·데이터·FCS가 프레임 전체 크기에 어떻게 더해지는지 표를 보고 설명한다.
- **찾아보기 (Lookup):** 장비 설명서에서 Jumbo Frame 지원 여부와 허용하는 최대 크기를 찾아본다.

## bps와 바이트 단위 구별

비트(bit)는 0 또는 1 하나를 담는 정보의 단위이고, 8비트가 모이면 1바이트(Byte)가 됩니다. 속도에 쓰는 `bps`는 초당 비트 수를 뜻합니다. 소문자 `b`는 bit, 대문자 `B`는 Byte이므로 글자 하나가 달라지면 단위도 달라집니다.

예를 들어 `1Gbps`는 초당 10억 비트이며, `1,000Mbps`와 같습니다. 8비트가 1바이트이므로 `1,000 ÷ 8 = 125`를 계산하면 이론상 초당 약 `125MB`를 보낼 수 있습니다. 따라서 `1Gbps`는 `1GB/s`가 아닙니다. 여기서는 십진 단위로 `1GB ≈ 1,000MB`라고 보면, 1GB 파일을 보내는 데 이론상 약 8초가 걸립니다. 실제로는 주소 같은 추가 정보도 함께 보내고 장비 처리나 혼잡의 영향도 받아 더 오래 걸립니다. 같은 방법으로 `100Mbps ÷ 8 = 12.5MB/s`입니다. 소문자 `b`로 적힌 `bps`를 바이트/초로 바꾸고 싶을 때 8로 나눕니다. 대문자 `B/s`는 이미 바이트/초이므로 다시 나누지 않습니다.

수도꼭지로 비유하면 bps는 일정 시간 동안 수도관을 지나가는 물의 양을 재는 단위와 같습니다. 네트워크에서 `bps ÷ 8`로 얻은 값도 표시 속도를 바이트 단위로 바꾼 이론적인 최대치이며, 실제 다운로드 속도를 보장하지는 않습니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** `bps`는 초당 비트, `B/s`는 초당 바이트를 뜻한다.
- **적용하기 (Apply):** 1Gbps를 8로 나눠 이상적인 MB/s를 계산하고 실제 속도와 구분한다.
- **찾아보기 (Lookup):** 컴퓨터의 네트워크 연결 상태에서 실제 연결 속도를 찾아보고, 표시된 bps를 이론적인 B/s로 바꿔 본다.

## 내 컴퓨터에서 연결 지점 찾아보기

`10Gbps`는 `1Gbps`의 열 배 속도입니다. 같은 1GB 파일을 전송한다고 가정하면, 다른 조건이 모두 같고 전송 효율도 완벽할 때 1Gbps에서는 약 8초, 10Gbps에서는 약 0.8초가 걸립니다. 실제 전송은 이 계산보다 느리지만, 속도 숫자가 열 배가 되면 이론상 시간은 10분의 1이 된다는 감각을 얻을 수 있습니다. 빠른 연결에서 광섬유 케이블을 쓰는 경우도 있습니다. 구리 케이블은 전기 신호를, 광섬유는 빛 신호를 전달하지만 10Gbps라고 해서 반드시 광섬유를 쓰는 것은 아닙니다.

이제 컴퓨터에서 배운 말을 찾아볼 수 있습니다. Windows에서는 명령 프롬프트를 열어 `ipconfig /all`을 입력하고 `무선 LAN 어댑터 Wi-Fi` 또는 `Ethernet 어댑터` 항목을 찾아봅니다. Mac에서는 터미널에서 `ifconfig`를 입력해 `en0`, `en1` 같은 항목을 보고, 해당 인터페이스의 `ether` 옆 값을 찾습니다. 출력이 길면 Mac의 네트워크 설정에서 Wi-Fi 상세 정보나 주소 항목을 확인해도 됩니다. 운영체제와 장치에 따라 이름은 다르고, VPN이나 가상머신이 만든 가상 인터페이스도 목록에 섞일 수 있습니다. 당장은 익숙한 Wi-Fi와 Ethernet 항목을 중심으로 확인하면 됩니다.

화면에서 연결 항목을 하나 찾았다면, 그 이름이 인터페이스의 예이고 `물리적 주소(Physical Address)`(Windows) 또는 `ether`(Mac) 옆의 값이 MAC 주소의 예입니다. Wi-Fi와 Ethernet이 모두 보이면 인터페이스가 둘 이상일 수 있습니다. 연결 속도는 Windows 설정의 네트워크 속성이나 Mac의 Wi-Fi 메뉴에서 확인할 수 있고, 화면 구성은 운영체제 버전에 따라 달라질 수 있습니다. 이 값은 내 컴퓨터와 공유기 사이의 한 구간에서 협상된 링크 속도입니다. 표시된 `Mbps`를 `MB/s`로 어림하려면 8로 나누세요. 예를 들어 `866 Mbps ÷ 8 ≈ 108 MB/s`입니다. 이 값은 그 구간의 이론적인 최대 전송량을 바이트 단위로 바꾼 값이지, 공유기 바깥의 인터넷 회선이나 서버 상태까지 반영한 실제 다운로드 속도는 아닙니다.

마을 그림으로 되짚어 보면 호스트는 집 한 채, NIC는 네트워크와 이어지는 문, 인터페이스는 문이 네트워크와 맞닿는 연결 지점, MAC 주소는 그 문을 구별하는 문패, LAN은 가까운 집들이 모인 마을입니다. 한 호스트에 문이 여러 개일 수 있고 문마다 MAC 주소가 따로 쓰일 수 있습니다. 프레임은 한 구간을 건널 때 패킷을 감싸는 운송 포장이고, 속도는 그 구간에서 일정 시간에 전달할 수 있는 양을 나타냅니다. 비유가 맞지 않는 부분도 기억하세요. 현실의 집은 문이 여러 개여도 보통 주소 하나를 쓰지만, 네트워크에서는 연결 지점마다 MAC 주소가 사용되고 Wi-Fi는 개인정보 보호용 주소를 쓸 수도 있습니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 운영체제의 네트워크 정보에서 인터페이스 이름, MAC 주소, 링크 속도를 확인할 수 있다.
- **적용하기 (Apply):** 1Gbps와 10Gbps의 이론적 전송 시간을 비교하고 링크 속도와 실제 다운로드 속도가 다른 이유를 말한다.
- **찾아보기 (Lookup):** 내 장치의 NIC 링크 속도는 OS 네트워크 상태에서 확인한다.
