---
id: u3-l08-nic-l2-frame-lan-카드-그리고-mac-주소
title: 네트워크 연결 지점과 MAC 주소, 프레임
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-08.md
wiki_diagram: units/03-layer2-switching/lessons/01-nic-l2-frame-lan-카드-그리고-mac-주소/assets/diagrams/lesson-08.svg
page_metadata:
- terms:
  - NIC (Network Interface Card)
  - 인터페이스 (Interface)
  - 리얼텍 (Realtek)
  questions:
  - id: u3-01-p01-q01
    kind: choice
    difficulty: easy
    prompt: 컴퓨터가 네트워크와 정보를 주고받도록 연결해 주는 장치는 무엇인가요?
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
    kind: short
    prompt: 네트워크와 맞닿는 연결 지점을 장치와 구분해 부르는 말입니다. 영어로 답해주세요.
    answers:
    - network interface
    feedback: 정답은 network interface입니다.
  - id: u3-01-p01-q04
    kind: choice
    difficulty: medium
    prompt: "집의 문처럼 컴퓨터와 네트워크 사이에서 신호를 주고받게 해 주는 장치는 무엇인가요?"
    choices:
    - id: a
      text: "스위치 포트"
      feedback: "다시 본문을 확인해 보세요. 스위치 포트."
    - id: b
      text: "라우터"
      feedback: "다시 본문을 확인해 보세요. 라우터."
    - id: c
      text: "프레임"
      feedback: "다시 본문을 확인해 보세요. 프레임."
    - id: d
      text: "NIC"
      feedback: "맞아요. NIC입니다."
    - id: e
      text: "IP 주소"
      feedback: "다시 본문을 확인해 보세요. IP 주소."
    answer: d
  animations:
  - file: l08-nic-door.svg
    title: "NIC는 컴퓨터의 문"
    alt: "컴퓨터를 나타내는 네모 안에서 문서 작성과 계산 사이를 점이 오가며 집 안에서 끝나는 일을 보여 줍니다. 이어서 네모 가장자리에 NIC(LAN 카드)가 문처럼 나타나고, NIC가 네트워크와 맞닿는 자리에 인터페이스 점이 생기며, 주황 점이 그 연결 지점을 지나 네트워크로 나갑니다. 마지막에 ‘Realtek 무선 LAN’ 사양 문구에서 Realtek은 회사 이름, 무선 LAN은 NIC 종류라는 설명이 붙습니다."
    caption: "NIC는 컴퓨터가 네트워크와 신호를 주고받는 장치이고, 인터페이스는 NIC가 네트워크와 맞닿는 연결 지점입니다. 사양표의 Realtek은 NIC를 만든 회사 이름입니다."
- terms:
  - 호스트 (Host)
  - 액세스 포인트 (Access Point)
  - 인터페이스와 케이블 구멍
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
    prompt: 네트워크에 연결된 컴퓨터나 장치 한 대를 가리키는 말은 무엇인가요?
    choices:
    - id: a
      text: Host
      feedback: 맞아요. Host.
    - id: b
      text: Frame
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Interface
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: Switch
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: WAN
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
    feedback: 정답은 port입니다.
  - id: u3-01-p02-q04
    kind: choice
    difficulty: medium
    prompt: "노트북 한 대에 Wi-Fi와 USB Ethernet 연결이 모두 있다면 가장 알맞은 설명은 무엇인가요?"
    choices:
    - id: a
      text: "호스트 한 대에 네트워크 인터페이스가 두 개 있다"
      feedback: "맞아요. 호스트 한 대에 네트워크 인터페이스가 두 개 있다입니다."
    - id: b
      text: "컴퓨터가 두 대의 호스트가 된다"
      feedback: "다시 본문을 확인해 보세요. 컴퓨터가 두 대의 호스트가 된다."
    - id: c
      text: "두 NIC가 반드시 같은 MAC 주소를 쓴다"
      feedback: "다시 본문을 확인해 보세요. 두 NIC가 반드시 같은 MAC 주소를 쓴다."
    - id: d
      text: "Wi-Fi는 인터페이스로 세지 않는다"
      feedback: "다시 본문을 확인해 보세요. Wi-Fi는 인터페이스로 세지 않는다."
    - id: e
      text: "USB 어댑터가 액세스 스위치가 된다"
      feedback: "다시 본문을 확인해 보세요. USB 어댑터가 액세스 스위치가 된다."
    answer: a
- terms:
  - LAN (Local Area Network)
  - MAN (Metropolitan Area Network)
  - WAN (Wide Area Network)
  questions:
  - id: u3-01-p03-q01
    kind: choice
    difficulty: easy
    prompt: LAN, MAN, WAN은 주로 네트워크의 어떤 점을 설명하나요?
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
    feedback: 정답은 LAN입니다.
  - id: u3-01-p03-q04
    kind: choice
    difficulty: medium
    prompt: "LAN, MAN, WAN을 나누는 주된 기준은 무엇인가요?"
    choices:
    - id: a
      text: "전송 속도의 높고 낮음"
      feedback: "다시 본문을 확인해 보세요. 전송 속도의 높고 낮음."
    - id: b
      text: "케이블과 무선 중 무엇을 쓰는지"
      feedback: "다시 본문을 확인해 보세요. 케이블과 무선 중 무엇을 쓰는지."
    - id: c
      text: "네트워크가 아우르는 지리적 범위"
      feedback: "맞아요. 네트워크가 아우르는 지리적 범위입니다."
    - id: d
      text: "연결된 컴퓨터의 개수만"
      feedback: "다시 본문을 확인해 보세요. 연결된 컴퓨터의 개수만."
    - id: e
      text: "MAC 주소의 길이"
      feedback: "다시 본문을 확인해 보세요. MAC 주소의 길이."
    answer: c
  animations:
  - file: l08-lan-man-wan.svg
    title: "LAN, MAN, WAN"
    alt: "집 공유기에 휴대전화와 태블릿은 Wi-Fi 점선으로, 데스크톱과 IPTV는 케이블 실선으로 연결되어 있습니다. 이 장치들을 LAN(마을) 테두리가 감싸고, 이웃 LAN을 포함한 MAN(도시) 테두리, 다른 도시와 먼 지역까지 포함한 WAN(더 넓은 지역) 테두리가 차례로 넓게 그려집니다. 마지막에 범위의 이름일 뿐 속도 순위가 아니라는 문구가 나옵니다."
    caption: "LAN·MAN·WAN은 네트워크가 어느 정도 범위에 걸쳐 있는지를 나타내는 이름입니다. 범위가 넓다고 더 빠르거나 품질이 좋은 것은 아닙니다."
- terms:
  - MAC 주소 (Media Access Control address)
  - 식별자 (identifier)
  - 16진수 (hexadecimal)
  - 임시 MAC 주소
  animations:
  - file: l08-mac-address-label.svg
    title: NIC에 붙는 문패, MAC 주소
    alt: NIC마다 MAC 주소가 붙는 모습, 일반 주소에서 주소를 할당한 조직을 나타내는 앞부분, 무선 연결에서 개인 정보 보호를 위해 다른 주소를 사용할 수 있다는 점을 보여 줍니다.
    caption: 각 NIC에는 MAC 주소가 쓰입니다. 보통의 전역 주소와 무선 연결에서 쓰는 개인 정보 보호용 주소가 다를 수 있어, 앞부분만 보고 항상 제조사를 알아낼 수 있는 것은 아닙니다.
  questions:
  - id: u3-01-p04-q01
    kind: choice
    difficulty: easy
    prompt: 네트워크 연결 지점을 구분하는 데 쓰는 주소는 무엇인가요?
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
  - id: u3-01-p04-q02
    kind: choice
    difficulty: medium
    prompt: Wi-Fi에서 개인 주소를 사용할 수 있다는 설명으로 맞는 것은 무엇인가요?
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
  - id: u3-01-p04-q03
    kind: short
    prompt: Wi-Fi에서 기기 고유 주소 대신 네트워크별로 사용할 수 있는 주소 유형입니다. 영어로 답해주세요.
    answers:
    - private address
    feedback: 정답은 private address입니다.
  - id: u3-01-p04-q04
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
- terms:
  - 프레임 (Frame)
  - L2 (Layer 2, 계층 2)
  - 패킷 (Packet)
  questions:
  - id: u3-01-p05-q01
    kind: choice
    difficulty: easy
    prompt: 다음 중 NIC의 형태로 볼 수 있는 것은 무엇인가요?
    choices:
    - id: a
      text: Host
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: WAN
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 기판 내장형, USB 유선형, 무선형 등 여러 형태
      feedback: 맞아요. 기판 내장형, USB 유선형, 무선형 등 여러 형태.
    - id: d
      text: NIC
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: Metric
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-01-p05-q02
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
  - id: u3-01-p05-q03
    kind: short
    prompt: 같은 L2 구간에서 데이터 전달에 사용하는 묶음을 영어로 무엇이라고 하나요?
    answers:
    - Frame
    feedback: 정답은 Frame입니다.
  - id: u3-01-p05-q04
    kind: choice
    difficulty: medium
    prompt: "패킷과 프레임의 관계를 가장 정확히 설명한 것은 무엇인가요?"
    choices:
    - id: a
      text: "프레임은 인터넷 전체에서 변하지 않는 포장이다"
      feedback: "다시 본문을 확인해 보세요. 프레임은 인터넷 전체에서 변하지 않는 포장이다."
    - id: b
      text: "패킷은 한 링크에서 전달되는 프레임의 데이터 부분에 실릴 수 있다"
      feedback: "맞아요. 패킷은 한 링크에서 전달되는 프레임의 데이터 부분에 실릴 수 있다입니다."
    - id: c
      text: "패킷은 MAC 주소이고 프레임은 IP 주소다"
      feedback: "다시 본문을 확인해 보세요. 패킷은 MAC 주소이고 프레임은 IP 주소다."
    - id: d
      text: "한 프레임에는 파일 하나만 들어간다"
      feedback: "다시 본문을 확인해 보세요. 한 프레임에는 파일 하나만 들어간다."
    - id: e
      text: "프레임은 라우터 사이에서 쓰이지 않는다"
      feedback: "다시 본문을 확인해 보세요. 프레임은 라우터 사이에서 쓰이지 않는다."
    answer: b
  animations:
  - file: l08-frame-per-link.svg
    title: "NIC가 주고받는 L2 프레임"
    alt: "기판에 끼우는 카드, USB 유선 어댑터, 무선 NIC 세 가지 모양이 먼저 나란히 보입니다. 노트북에서 주황 패킷이 준비되고, MAC 칸이 붙은 파란 Wi-Fi 프레임이 패킷을 감싼 채 무선 구간을 지나 공유기에 도착합니다. 공유기에서 포장이 민트색 Ethernet 프레임으로 바뀌고, 같은 패킷이 다음 장비로 이어집니다."
    caption: "NIC는 모양이 달라도 같은 역할을 하며, 같은 링크의 이웃에게 보낼 때 L2 단위인 프레임을 씁니다. 프레임은 패킷을 감싸는 한 구간용 포장이라 구간마다 새로 쓰일 수 있습니다."
- terms:
  - Ethernet
  - Jumbo Frame
  - 바이트 (Byte)
  questions:
  - id: u3-01-p06-q01
    kind: choice
    difficulty: easy
    prompt: 흔히 쓰는 Ethernet에서 데이터 부분의 최대 크기로 설명하는 값은 얼마인가요?
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
  - id: u3-01-p06-q02
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
  - id: u3-01-p06-q03
    kind: short
    prompt: 일반 Ethernet 프레임보다 더 큰 프레임을 허용하는 기능을 가리키는 영어 용어는 무엇인가요?
    answers:
    - Jumbo Frame
    feedback: 정답은 Jumbo Frame입니다.
  - id: u3-01-p06-q04
    kind: choice
    difficulty: medium
    prompt: "일반 Ethernet에서 MTU 1,500바이트가 가리키는 것은 무엇인가요?"
    choices:
    - id: a
      text: "헤더와 FCS를 포함한 프레임 전체 크기"
      feedback: "다시 본문을 확인해 보세요. 헤더와 FCS를 포함한 프레임 전체 크기."
    - id: b
      text: "Ethernet 헤더만의 크기"
      feedback: "다시 본문을 확인해 보세요. Ethernet 헤더만의 크기."
    - id: c
      text: "초당 전송 비트 수"
      feedback: "다시 본문을 확인해 보세요. 초당 전송 비트 수."
    - id: d
      text: "프레임의 데이터(payload) 부분 최대 크기"
      feedback: "맞아요. 프레임의 데이터(payload) 부분 최대 크기입니다."
    - id: e
      text: "MAC 주소의 크기"
      feedback: "다시 본문을 확인해 보세요. MAC 주소의 크기."
    answer: d
  animations:
  - file: l08-frame-size.svg
    title: "프레임 크기 세는 법"
    alt: "MTU 1,500 표시 아래 데이터(payload) 칸이 놓이고, 앞에 헤더 14바이트, 뒤에 FCS 4바이트 칸이 붙습니다. 전체를 세면 1,518바이트, FCS 칸이 흐려지면 1,514바이트라는 괄호가 나타납니다. 이어서 큰 사진 파일이 프레임 여러 개로 나뉘고, 마지막에 데이터 칸이 더 긴 Jumbo Frame이 크기는 장비·설정마다 다르다는 설명과 함께 나옵니다."
    caption: "일반 Ethernet의 1,500바이트는 데이터 부분의 최대 크기이고, 프레임 전체 크기는 헤더·FCS를 어떻게 세느냐에 따라 1,518 또는 1,514바이트로 적힙니다."
- terms:
  - 비트 (bit)
  - 바이트 (Byte)
  - bps (bits per second)
  - 기가비트 (Gigabit)
  animations:
  - file: l08-bit-vs-byte-speed.svg
    title: 소문자 b와 대문자 B, 8배의 차이
    alt: 작은 물방울 8개가 모여 병 하나가 되고, 그 아래 b와 B 글자가 나란히 놓입니다. 이어서 1Gbps 눈금이 약 125MB/s 눈금으로
      환산됩니다.
    caption: 8비트가 1바이트이므로 1Gbps는 초당 1GB가 아니라 약 0.125GB입니다.
  questions:
  - id: u3-01-p07-q01
    kind: choice
    difficulty: easy
    prompt: bps에서 소문자 b는 무엇을 뜻하나요?
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
  - id: u3-01-p07-q02
    kind: choice
    difficulty: medium
    prompt: 1Gbps를 이론상 바이트 전송량으로 바꾸면 초당 약 얼마인가요?
    choices:
    - id: a
      text: 125MB
      feedback: 맞아요. 125MB.
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
  - id: u3-01-p07-q03
    kind: short
    prompt: 8개의 bit가 모여 이루는 정보 용량 단위입니다. 영어 단어로 답해주세요.
    answers:
    - Byte
    feedback: 정답은 Byte입니다.
  - id: u3-01-p07-q04
    kind: choice
    difficulty: medium
    prompt: "1Gbps를 바이트 단위의 이론상 전송량으로 바꾸면 초당 약 얼마인가요?"
    choices:
    - id: a
      text: "125MB/s"
      feedback: "맞아요. 125MB/s입니다."
    - id: b
      text: "1MB/s"
      feedback: "다시 본문을 확인해 보세요. 1MB/s."
    - id: c
      text: "8MB/s"
      feedback: "다시 본문을 확인해 보세요. 8MB/s."
    - id: d
      text: "1GB/s"
      feedback: "다시 본문을 확인해 보세요. 1GB/s."
    - id: e
      text: "1,000MB/s"
      feedback: "다시 본문을 확인해 보세요. 1,000MB/s."
    answer: a
- terms:
  - 광섬유 케이블
  - 슬롯 (Slot)
  questions:
  - id: u3-01-p08-q01
    kind: choice
    difficulty: easy
    prompt: Windows에서 네트워크 연결 지점과 설정을 자세히 확인하는 명령은 무엇인가요?
    choices:
    - id: a
      text: ifconfig
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: mac print
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: ipconfig /all
      feedback: 맞아요. ipconfig /all.
    - id: d
      text: route print
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: ping /all
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-01-p08-q02
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
  - id: u3-01-p08-q03
    kind: short
    prompt: 유선 LAN에서 널리 쓰이며 데이터 프레임과 연결되는 네트워크 기술입니다. 영어로 답해주세요.
    answers:
    - Ethernet
    feedback: 정답은 Ethernet입니다.
  - id: u3-01-p08-q04
    kind: choice
    difficulty: medium
    prompt: "구리 케이블과 광섬유 케이블의 신호 전달 방식에 대한 설명으로 맞는 것은 무엇인가요?"
    choices:
    - id: a
      text: "구리와 광섬유 모두 반드시 전기 신호만 전달한다"
      feedback: "다시 본문을 확인해 보세요. 구리와 광섬유 모두 반드시 전기 신호만 전달한다."
    - id: b
      text: "광섬유는 IP 패킷을 직접 전달하므로 NIC가 필요 없다"
      feedback: "다시 본문을 확인해 보세요. 광섬유는 IP 패킷을 직접 전달하므로 NIC가 필요 없다."
    - id: c
      text: "구리 케이블은 전기 신호, 광섬유는 빛 신호를 전달한다"
      feedback: "맞아요. 구리 케이블은 전기 신호, 광섬유는 빛 신호를 전달한다입니다."
    - id: d
      text: "10Gbps 연결은 반드시 광섬유를 써야 한다"
      feedback: "다시 본문을 확인해 보세요. 10Gbps 연결은 반드시 광섬유를 써야 한다."
    - id: e
      text: "구리 케이블은 MAC 주소를 전달할 수 없다"
      feedback: "다시 본문을 확인해 보세요. 구리 케이블은 MAC 주소를 전달할 수 없다."
    answer: c

  animations:
  - file: l08-find-my-interface.svg
    title: "내 컴퓨터에서 연결 지점 찾기"
    alt: "명령 프롬프트 창에 ipconfig /all이 입력되고 무선 LAN 어댑터 Wi-Fi와 Ethernet 어댑터 항목이 나타납니다. 어댑터 이름 줄에는 인터페이스, Physical Address 줄에는 MAC 주소 꼬리표가 붙고, 두 어댑터가 모두 강조되어 인터페이스가 둘임을 보여 줍니다. 이어서 Mac 터미널의 ifconfig 화면에서 en0과 ether 값이 같은 방식으로 표시되고, 마지막에 전송률 866 Mbps를 8로 나눈 약 108 MB/s 카드가 나옵니다."
    caption: "ipconfig /all이나 ifconfig 화면에서 Wi-Fi·Ethernet 같은 항목 이름이 인터페이스, Physical Address나 ether 값이 MAC 주소입니다. Mbps를 8로 나눈 값은 단위를 바꾼 어림값이지 실제 다운로드 속도가 아닙니다."
animations_dir: units/03-layer2-switching/lessons/01-nic-l2-frame-lan-카드-그리고-mac-주소/assets/animations
---
앞 Lesson에서는 택배가 여러 사람과 장소를 거쳐 받는 사람에게 가는 큰 흐름을 살펴봤습니다. 이번 Lesson에서는 그 여정에 참여하는 컴퓨터와 네트워크가 어디에서 맞닿는지, 그 연결 지점에 어떤 안내가 붙는지 알아봅니다. 컴퓨터를 집, 연결 지점을 문, 가까운 범위의 네트워크를 마을이라고 생각해 보세요. 비유가 실제 구조와 완전히 같지는 않으니, 각 용어가 무엇을 가리키는지만 차근차근 연결하면 됩니다.

## NIC와 LAN 카드

새 노트북의 사양표에서 ‘무선 랜 카드’라는 말을 볼 수 있습니다. 컴퓨터 안에서 문서를 만들거나 계산하는 것만으로는 다른 컴퓨터에 파일을 보낼 수 없습니다. 네트워크와 신호를 주고받을 장치가 있어야 합니다. 이 장치를 LAN 카드 또는 NIC(Network Interface Card)라고 부릅니다. 예를 들어 노트북 사양의 ‘Realtek 무선 LAN’은 무선 네트워크에 연결하는 NIC의 제조사와 종류를 나타내는 말입니다. Realtek은 연결 장치의 다른 이름이 아니라 회사 이름입니다.

컴퓨터를 집 한 채라고 생각하면 NIC는 집과 바깥을 잇는 문이고, 인터페이스는 그 문이 네트워크와 맞닿는 연결 지점입니다. 집 안에서 끝나는 일은 이 문을 지나지 않지만, 웹페이지를 열거나 사진을 보내는 정보는 네트워크로 나갈 때 연결 지점을 거칩니다. 비유가 실제 구조와 똑같지는 않습니다. 현관문은 사람이 드나드는 물리적인 문이지만 NIC는 데이터를 전기 신호나 무선 신호로 주고받는 전자 장치입니다. 또 이름에 ‘카드’가 들어가도 반드시 카드처럼 따로 꽂는 부품일 필요는 없습니다. 메인보드에 내장된 장치도 NIC입니다.

따라서 용어를 볼 때는 ‘LAN 카드’, ‘NIC’, ‘네트워크 인터페이스’를 문맥에 맞춰 연결해 읽으면 됩니다. 엄밀히 말하면 NIC는 장치이고 인터페이스는 네트워크와 맞닿는 논리적 연결 지점이지만, 입문 자료와 운영체제 화면에서는 이 둘을 가깝게 부르기도 합니다.

## Host와 네트워크 인터페이스

네트워크에 연결된 컴퓨터나 장치 한 대를 이 Lesson에서는 호스트(Host)라고 부릅니다. 노트북, 데스크톱, 서버, 네트워크에 연결된 프린터가 각각 호스트의 예입니다. 그림에서는 호스트를 네모 하나로, 네트워크와 맞닿는 인터페이스를 네모 가장자리의 진한 점으로 그리기도 합니다. 네모 하나에 점 두 개가 있으면 컴퓨터가 두 대라는 뜻이 아니라, 호스트 한 대에 연결 지점이 두 개 있다는 뜻입니다.

예를 들어 노트북에는 Wi-Fi NIC가 기본으로 들어 있고, USB 유선 어댑터를 꽂으면 Ethernet 연결 지점이 하나 더 생길 수 있습니다. 무선 쪽은 무선 신호를 중계하는 액세스 포인트(보통 가정용 공유기에 함께 들어 있음)에 연결하고, 유선 쪽에는 랜 케이블을 꽂습니다. 노트북 한 대가 두 연결 지점을 가진 셈입니다. 집의 문과 달리 Wi-Fi 인터페이스에는 케이블을 꽂는 구멍이 없지만, 네트워크와 이어지는 연결이므로 인터페이스 하나로 셉니다.

여기서 ‘포트’라는 말을 만나면 문맥을 살펴야 합니다. 컴퓨터 옆의 Ethernet 케이블 구멍도 일상적으로 포트라고 부르지만, 나중에 배울 TCP/UDP 포트 번호는 프로그램의 통신 통로를 구분하는 번호입니다. 구멍과 번호는 서로 다른 개념입니다. 또 서버를 제공하는 서비스도 ‘호스트’라 부르는 경우가 있지만, 이 Lesson에서는 네트워크에 연결된 장치 한 대라는 뜻으로 사용합니다.

케이블을 꽂는 물리적인 구멍도 일상적으로 ‘포트’라고 부릅니다. 뒤에서 배울 통신 프로그램의 포트 번호와는 다른 뜻이니, 지금은 연결 지점과 케이블 구멍을 구분해 두면 됩니다.

## LAN과 네트워크 규모

LAN, MAN, WAN은 네트워크가 어느 정도 범위에 걸쳐 있는지 설명하는 이름입니다. LAN(Local Area Network)은 집이나 사무실처럼 비교적 가까운 범위, MAN(Metropolitan Area Network)은 도시 규모, WAN(Wide Area Network)은 그보다 넓은 범위를 가리킵니다. LAN을 마을, MAN을 도시, WAN을 더 넓은 지역이라고 비유할 수 있습니다.

집의 공유기에 휴대전화와 태블릿은 Wi-Fi로, 방의 데스크톱과 IPTV 수신기는 랜 케이블로 연결되어 있다고 해 봅시다. 연결 방식은 달라도 이 장치들이 집 안에서 함께 통신하는 가까운 네트워크를 LAN의 예로 볼 수 있습니다. LAN이 반드시 케이블만 쓰거나 컴퓨터만 연결한다는 뜻은 아닙니다. 집, 사무실, 학교 실습실처럼 비교적 좁은 범위에서 여러 장치가 연결된 환경을 떠올리면 됩니다.

LAN을 마을 하나, MAN을 도시, WAN을 더 넓은 지역으로 생각하면 범위의 차이를 기억하기 쉽습니다. 다만 지도에서 도시의 넓이가 성능을 말해 주지 않듯이, LAN·MAN·WAN도 속도나 품질의 순위가 아닙니다. LAN과 MAN 사이에 몇 킬로미터라는 고정된 경계가 있는 것도 아닙니다. 이 이름들은 네트워크가 어느 정도의 범위를 아우르는지 설명하는 분류입니다.

## MAC 주소 · NIC의 식별자

집집마다 문패가 있듯이 네트워크 연결 지점에도 MAC(Media Access Control) 주소라는 값이 쓰입니다. MAC 주소는 같은 가까운 네트워크 안에서 어느 연결 지점으로 데이터를 건넬지 구분할 때 사용하는 주소입니다. 그래서 NIC에 붙은 문패라고 비유할 수 있습니다.

주소는 보통 `AA-BB-CC-11-22-33`처럼 두 글자씩 여섯 묶음으로 적습니다. 콜론으로 `AA:BB:CC:11:22:33`처럼 쓰기도 합니다. 한 글자는 0~9 또는 A~F를 쓰는 16진수 한 자리이고, 두 자리가 1바이트입니다. 여섯 묶음은 6바이트, 즉 48비트입니다. 이처럼 표기가 일정한 이유는 사람이 주소를 읽고 비교하기 쉽게 여러 덩어리로 나눴기 때문입니다.

전역으로 할당된 일반적인 MAC 주소에서는 앞부분이 주소를 할당받은 조직을 식별하는 데 쓰입니다. 그렇다고 화면에 보이는 모든 MAC 주소에서 제조사를 알아낼 수 있는 것은 아닙니다. 스마트폰과 노트북은 Wi-Fi에서 개인정보 보호를 위해 기기 고유 주소 대신 네트워크별 개인 주소를 사용할 수 있습니다. 예를 들어 집 Wi-Fi와 카페 Wi-Fi에서 서로 다른 주소를 보일 수 있고, 제품 라벨에 적힌 주소와도 다를 수 있습니다. 따라서 MAC 주소는 ‘연결 지점을 구분하는 문패’로 기억하되, 문패가 언제나 공장에서 붙인 값 그대로라고 생각하지는 마세요.

노트북에 Wi-Fi와 USB Ethernet, 두 NIC가 있다면 각각의 인터페이스에 서로 다른 MAC 주소가 사용됩니다. 그래서 MAC 주소는 컴퓨터 한 대에 무조건 하나만 있는 값이 아닙니다. 또 MAC 주소와 IP 주소는 둘 다 주소처럼 보이지만 역할이 다릅니다. 지금은 MAC 주소를 가까운 네트워크 구간에서 연결 지점을 구별할 때 쓰는 문패로 기억하고, IP 주소와 두 주소가 함께 쓰이는 과정은 뒤에서 배웁니다.

## 유선·무선 NIC 살펴보기

네트워크 연결 장치는 여러 모양으로 만들 수 있습니다. 컴퓨터 안 기판에 끼우는 카드도 있고, USB에 꽂아 케이블을 연결하는 장치나 무선으로 연결하는 장치도 있습니다. 모양과 연결 방식은 달라도 네트워크와 정보를 주고받는 연결 지점이라는 역할은 같습니다.

NIC를 통해 같은 링크의 이웃에게 데이터를 보낼 때 사용하는 L2 데이터 단위가 프레임(Frame)입니다. 예를 들어 노트북이 집 공유기로 데이터를 보낼 때, 그 한 구간에서 Ethernet 또는 Wi-Fi 프레임을 사용합니다. 앞에서 택배 상자에 비유한 패킷이 목적지를 향해 운반되는 내용이라면, 프레임은 한 구간을 건너기 위해 그 내용을 둘러싸는 운송 포장이라고 생각할 수 있습니다. 패킷을 프레임의 데이터 부분에 담고, 그 구간에서 보낼 곳과 보낸 곳을 식별하는 MAC 주소 같은 정보를 붙입니다.

택배 비유로 흐름을 따라가 보겠습니다. 노트북에서 공유기로 보내는 첫 구간에서는 노트북이 프레임을 만들어 무선으로 보냅니다. 공유기를 지난 다음 다른 네트워크로 향하는 구간에서는 링크 기술과 다음 전달 상대에 맞춰 새 프레임을 사용할 수 있습니다. 그러므로 프레임은 목적지까지 내내 그대로 따라가는 상자가 아니라, 링크 구간마다 쓰이는 포장에 가깝습니다. 비유는 ‘한 구간의 전달 단위’라는 점을 잡기 위한 것이며 실제 데이터 구조는 뒤에서 자세히 다룹니다.

## L2 Frame의 크기

택배 상자에 담을 수 있는 양에 한계가 있듯, 프레임의 데이터 부분에도 크기 한계가 있습니다. 일반 Ethernet에서 흔히 말하는 MTU 1,500바이트는 프레임 전체가 아니라 데이터(payload) 부분의 최대 크기입니다. 여기에 Ethernet 헤더 14바이트와 뒤의 FCS 4바이트를 더해 세면 프레임은 보통 1,518바이트가 됩니다. FCS를 제외해 표시하면 1,514바이트라고 적힐 수 있습니다. 장비 문서가 프레임 크기를 셀 때 어떤 항목을 포함하는지 확인해야 숫자를 제대로 비교할 수 있습니다.

일반 크기보다 큰 프레임을 허용하는 Jumbo Frame도 있지만, 어느 크기까지 쓸 수 있는지는 장비와 설정에 따라 달라집니다. 모든 네트워크가 같은 점보 프레임 크기를 쓰는 것은 아니므로 ‘항상 10KB’처럼 외우지 마세요. 큰 사진 파일 하나가 한 프레임에 통째로 들어가는 것도 아닙니다. 전송할 데이터는 프레임 크기에 맞춰 여러 단위로 나뉘어 오갈 수 있습니다. 지금은 `1,500바이트`가 일반 Ethernet의 데이터 부분 크기 기준이라는 점과, 프레임 전체 크기는 헤더·FCS 포함 여부에 따라 달라진다는 점을 기억하면 됩니다.

장비 사양에는 프레임 크기와 함께 `1Gbps` 같은 속도도 표시됩니다. 프레임 크기는 한 번에 담는 양이고, 속도는 일정 시간 동안 얼마나 많이 보내는지를 말하므로 서로 다른 값입니다.

## bps와 바이트 단위 구별

비트(bit)는 0 또는 1 하나를 담는 정보의 단위이고, 8비트가 모이면 1바이트(Byte)가 됩니다. 속도에 쓰는 `bps`는 초당 비트 수를 뜻합니다. 소문자 `b`는 bit, 대문자 `B`는 Byte이므로 글자 하나가 달라지면 단위도 달라집니다.

예를 들어 `1Gbps`는 초당 약 10억 비트입니다. 8비트를 1바이트로 묶으므로 10억을 8로 나누면 초당 약 125MB입니다. 따라서 `1Gbps`는 `1GB/s`가 아니라 이론상 약 `125MB/s`입니다. 파일 크기가 `1GB`라면 1,000MB를 125MB/s로 나누어 최소 약 8초가 걸린다고 어림할 수 있습니다. 실제 파일 전송은 주소 같은 추가 정보와 장비 처리, 혼잡 등의 영향으로 더 오래 걸립니다. 같은 계산으로 `100Mbps ÷ 8 = 12.5MB/s`입니다. 속도 표기의 b/B가 헷갈릴 때는 먼저 비트인지 바이트인지 확인한 다음 8로 나누면 됩니다.

수도꼭지 비유로는 bps를 ‘1초 동안 흘러간 물의 양’으로 생각할 수 있습니다. 다만 물방울 하나하나가 항상 같은 크기인 것과 달리, 네트워크에서 실제로 파일이 전송되는 속도는 통신 상대와 장비, 무선 신호 상태에 따라 달라집니다. 따라서 8로 나눈 값은 표시 속도를 바이트 단위로 바꾼 이론적인 상한에 가깝고, 실제 다운로드 속도를 보장하지는 않습니다.

## 내 컴퓨터에서 연결 지점 찾아보기

`10Gbps`는 `1Gbps`의 열 배 속도입니다. 같은 1GB 파일을 전송한다고 가정하면, 다른 조건이 모두 같고 전송 효율도 완벽할 때 1Gbps에서는 약 8초, 10Gbps에서는 약 0.8초가 걸립니다. 실제 전송은 이 계산보다 느리지만, 속도 숫자가 열 배가 되면 이론상 시간은 10분의 1이 된다는 감각을 얻을 수 있습니다. 빠른 연결에서 광섬유 케이블을 쓰는 경우도 있습니다. 구리 케이블은 전기 신호를, 광섬유는 빛 신호를 전달하지만 10Gbps라고 해서 반드시 광섬유를 쓰는 것은 아닙니다.

이제 컴퓨터에서 배운 말을 찾아볼 수 있습니다. Windows에서는 명령 프롬프트를 열어 `ipconfig /all`을 입력하고 `무선 LAN 어댑터 Wi-Fi` 또는 `Ethernet 어댑터` 항목을 찾아봅니다. Mac에서는 터미널에서 `ifconfig`를 입력해 `en0`, `en1` 같은 항목을 보고, `ether` 옆의 값을 찾습니다. 운영체제와 장치에 따라 이름은 다르고, VPN이나 가상머신이 만든 가상 인터페이스도 목록에 섞일 수 있습니다. 당장은 익숙한 Wi-Fi와 Ethernet 항목을 중심으로 확인하면 됩니다.

화면에서 연결 항목을 하나 찾았다면, 그 이름이 인터페이스의 예이고 `Physical Address`(Windows) 또는 `ether`(Mac) 값이 MAC 주소의 예입니다. Wi-Fi와 Ethernet이 모두 보이면 인터페이스가 둘 이상일 수 있습니다. 실제 연결 속도는 Windows 설정의 네트워크 속성에서 링크 속도를 확인하거나, Mac에서는 Option 키를 누른 채 Wi-Fi 메뉴를 열어 전송률을 볼 수 있습니다. 화면 구성은 운영체제 버전에 따라 달라질 수 있습니다. 표시된 `Mbps`를 `MB/s`로 어림하려면 8로 나누세요. 예를 들어 `866 Mbps ÷ 8 ≈ 108 MB/s`입니다. 이는 단위를 바꾼 값이지 실제 다운로드 속도는 아닙니다.

마을 그림으로 되짚어 보면 호스트는 집 한 채, NIC는 네트워크와 이어지는 문, 인터페이스는 문이 네트워크와 맞닿는 연결 지점, MAC 주소는 그 문을 구별하는 문패, LAN은 가까운 집들이 모인 마을입니다. 한 호스트에 문이 여러 개일 수 있고 문마다 MAC 주소가 따로 쓰일 수 있습니다. 프레임은 한 구간을 건널 때 사용하는 포장이고, 속도는 그 포장을 초당 얼마나 많이 보낼 수 있는지를 나타냅니다. 비유가 맞지 않는 부분도 기억하세요. 현실의 집은 문이 여러 개여도 보통 주소 하나를 쓰지만, 네트워크에서는 연결 지점마다 MAC 주소가 사용되고 Wi-Fi는 개인정보 보호용 주소를 쓸 수도 있습니다.
