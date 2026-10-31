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
animations_dir: units/03-layer2-switching/lessons/01-nic-l2-frame-lan-카드-그리고-mac-주소/assets/animations
---
앞 Lesson에서는 택배가 여러 사람과 장소를 거쳐 받는 사람에게 가는 큰 흐름을 살펴봤습니다. 이번 Lesson에서는 그 여정에 참여하는 컴퓨터와 네트워크가 어디에서 맞닿는지, 그 연결 지점에 어떤 안내가 붙는지 알아봅니다. 컴퓨터를 집, 연결 지점을 문, 가까운 범위의 네트워크를 마을이라고 생각해 보세요. 비유가 실제 구조와 완전히 같지는 않으니, 각 용어가 무엇을 가리키는지만 차근차근 연결하면 됩니다.

## NIC와 LAN 카드

새 노트북의 사양표에서 ‘무선 랜 카드’라는 말을 볼 수 있습니다. 컴퓨터가 네트워크와 정보를 주고받으려면 네트워크에 연결되는 장치가 필요합니다. 이 장치를 LAN 카드나 NIC(Network Interface Card)라고 부릅니다. 네트워크 인터페이스는 그 장치가 제공하는 연결 지점을 가리킵니다. 서로 다른 장치 세 개를 말하는 것은 아니지만, NIC는 장치이고 인터페이스는 연결 지점이라는 차이가 있습니다.

컴퓨터를 집 한 채라고 생각하면 NIC는 집과 바깥을 잇는 문, 인터페이스는 그 문을 통해 네트워크와 맞닿는 연결 지점입니다. 집 안의 일은 집 안에서 끝나고, 네트워크와 오가는 정보는 이 연결 지점을 지납니다. 이름에 ‘카드’가 들어가지만 반드시 카드 모양인 것은 아닙니다. ‘리얼텍 LAN 카드’와 ‘리얼텍 NIC’는 같은 종류의 장치를 가리킵니다.

## Host와 네트워크 인터페이스

네트워크에 연결된 컴퓨터나 장치 한 대를 이 Lesson에서는 호스트라고 부릅니다. 그림에서는 호스트를 네모로, 네트워크와 맞닿는 인터페이스를 진한 점으로 그리기도 합니다. 네모에 점이 두 개 있으면 한 장치에 연결 지점이 두 개 있다는 뜻입니다.

예를 들어 노트북에는 무선 연결 지점이 기본으로 들어 있고, USB 유선 장치를 더 연결하면 유선 연결 지점이 하나 더 생길 수 있습니다. 무선 쪽은 액세스 포인트와 연결하고, 유선 쪽에는 케이블을 꽂습니다. 집의 문과 달리 무선 인터페이스에는 케이블 구멍이 없습니다. 여기서 ‘인터페이스’는 구멍 모양이 아니라 네트워크와 맞닿는 연결 지점을 뜻합니다.

케이블을 꽂는 물리적인 구멍도 일상적으로 ‘포트’라고 부릅니다. 뒤에서 배울 통신 프로그램의 포트 번호와는 다른 뜻이니, 지금은 연결 지점과 케이블 구멍을 구분해 두면 됩니다.

## LAN과 네트워크 규모

LAN, MAN, WAN은 네트워크가 어느 정도 범위에 걸쳐 있는지 설명하는 이름입니다. LAN(Local Area Network)은 집이나 사무실처럼 비교적 가까운 범위, MAN(Metropolitan Area Network)은 도시 규모, WAN(Wide Area Network)은 그보다 넓은 범위를 가리킵니다. LAN을 마을, MAN을 도시, WAN을 더 넓은 지역이라고 비유할 수 있습니다.

집의 공유기에 휴대전화와 태블릿은 무선으로, 컴퓨터와 IPTV 수신기는 케이블로 연결되어 있다고 해 봅시다. 이처럼 가까운 장치들이 함께 이루는 집 안 네트워크를 LAN의 예로 볼 수 있습니다. LAN이나 MAN이라는 이름은 범위를 설명할 뿐 속도나 성능의 우열을 말하지 않습니다. 둘을 나누는 거리가 딱 정해져 있는 것도 아니므로, 지금은 작은 범위와 넓은 범위를 구분하는 이름이라고 이해하면 충분합니다.

## MAC 주소 · NIC의 식별자

집집마다 문패가 있듯이 네트워크 연결 지점에도 MAC(Media Access Control) 주소라는 값이 쓰입니다. MAC 주소는 같은 가까운 네트워크 안에서 어느 연결 지점으로 데이터를 건넬지 구분할 때 사용하는 주소입니다. 그래서 NIC에 붙은 문패라고 비유할 수 있습니다.

주소는 보통 `AA-BB-CC-11-22-33`처럼 두 글자씩 여섯 묶음으로 적습니다. 글자는 16진수 표기이며, 일반적인 전역 주소의 앞부분은 주소를 할당한 조직을 나타내는 데 쓰입니다. 하지만 모든 주소가 제조사 이름을 알려 주는 것은 아닙니다. 개인 정보 보호를 위해 Wi-Fi에서 기기 고유의 주소 대신 네트워크별 개인 주소를 쓸 수 있고, 이 주소는 제품에 적힌 값과 다를 수 있습니다.

한 장치에 NIC가 둘 있으면 각각의 연결 지점에 별도의 MAC 주소가 쓰일 수 있습니다. MAC 주소는 뒤에서 배울 IP 주소와 역할이 다르므로, 지금은 “연결 지점에 붙는 문패”라는 비유부터 기억해 두세요.

## 유선·무선 NIC 살펴보기

네트워크 연결 장치는 여러 모양으로 만들 수 있습니다. 컴퓨터 안 기판에 끼우는 카드도 있고, USB에 꽂아 케이블을 연결하는 장치나 무선으로 연결하는 장치도 있습니다. 모양과 연결 방식은 달라도 네트워크와 정보를 주고받는 연결 지점이라는 역할은 같습니다.

그 연결 지점을 오가는 가까운 구간의 데이터 묶음을 프레임(Frame)이라고 부릅니다. 앞에서 본 패킷이 목적지까지 가는 택배 상자라면, 프레임은 다음 가까운 전달 지점까지 옮길 때 붙이는 지역 배송용 포장이라고 생각해 볼 수 있습니다. 상자 안의 내용이 그대로여도 다음 구간에 맞는 겉포장이 필요할 수 있습니다. 이 구간에서 프레임은 연결 지점의 MAC 주소를 사용합니다. 패킷과 프레임이 실제로 어떻게 함께 움직이는지는 뒤에서 더 자세히 보겠습니다.

## L2 Frame의 크기

택배 상자에 담을 수 있는 양에 한계가 있듯, 한 프레임에 담는 데이터에도 크기 한계가 있습니다. 흔히 쓰는 Ethernet에서는 데이터 부분의 크기를 최대 1,500바이트로 설명합니다. 다만 문서나 장비가 프레임 전체를 잴 때는 앞뒤 안내와 검사 값을 포함하는지에 따라 숫자가 달라질 수 있습니다. 예를 들어 1,514바이트는 마지막 검사 값을 빼고 센 크기이고, 이를 포함하면 보통 1,518바이트라고 합니다.

이보다 큰 프레임을 지원하는 Jumbo Frame도 있지만, 지원 크기는 장비와 설정에 따라 다릅니다. 따라서 ‘항상 10KB’처럼 고정된 값으로 외우기보다 일반 프레임보다 큰 크기를 허용하는 방식이라는 정도로 알아두면 됩니다. 10Base-T, 802.3, 802.5, 802.11 같은 규격 이름은 지금 외우지 않아도 됩니다.

장비 사양에는 프레임 크기와 함께 `1Gbps` 같은 속도도 표시됩니다. 프레임 크기는 한 번에 담는 양이고, 속도는 일정 시간 동안 얼마나 많이 보내는지를 말하므로 서로 다른 값입니다.

## bps와 바이트 단위 구별

비트(bit)는 0 또는 1 하나를 담는 정보의 단위이고, 8비트가 모이면 1바이트(Byte)가 됩니다. 속도에 쓰는 `bps`는 초당 비트 수를 뜻합니다. 소문자 `b`는 bit, 대문자 `B`는 Byte이므로 글자 하나가 달라지면 단위도 달라집니다.

예를 들어 `1Gbps`는 초당 약 10억 비트입니다. 이를 바이트로 바꾸면 이론상 초당 약 125MB입니다. 따라서 `1Gbps`를 `1GB/s`와 같은 뜻으로 읽으면 안 됩니다. `1GB` 파일을 `1Gbps`로 보낼 때도 이론상 약 8초가 걸리고, 실제 전송에는 추가 정보와 네트워크 상태가 영향을 줘 더 오래 걸릴 수 있습니다. `100Mbps`도 같은 계산으로 이론상 약 `12.5MB/s`입니다.

## 내 컴퓨터에서 연결 지점 찾아보기

`10Gbps`는 `1Gbps`보다 표시 속도가 열 배 높습니다. 빠른 연결에는 구리선을 쓰는 경우도 있고, 전기 신호 대신 빛을 보내는 광섬유 케이블을 쓰는 경우도 있습니다. NIC라는 이름에 ‘카드’가 남은 것은 예전부터 컴퓨터 안의 슬롯에 꽂는 카드 모양 장치가 있었기 때문입니다. 오늘날에는 기판에 내장되거나 USB로 연결되는 등 모양이 다양합니다.

앞의 비유를 한 번에 정리하면, 호스트는 집, NIC는 네트워크와 이어지는 문, MAC 주소는 그 문에 쓰이는 문패, LAN은 가까운 집들이 모인 마을입니다. 집과 달리 한 컴퓨터에 문이 여러 개 있을 수 있고, Wi-Fi에서는 문패로 쓰는 주소가 개인 정보 보호를 위해 달라질 수도 있습니다.

내 컴퓨터에서 연결 지점을 살펴보려면 Windows에서는 명령 프롬프트를 열어 `ipconfig /all`을 입력하고, Wi-Fi나 Ethernet 어댑터 항목을 찾습니다. Mac에서는 터미널에서 `ifconfig`를 실행한 뒤 `en0`, `en1` 같은 항목과 그 아래의 `ether` 값을 볼 수 있습니다. 목록에 가상 연결도 나타날 수 있으니, 지금은 Wi-Fi와 Ethernet처럼 익숙한 연결부터 찾아보세요. 장치에 따라 표시되는 이름과 개수는 다를 수 있습니다.
