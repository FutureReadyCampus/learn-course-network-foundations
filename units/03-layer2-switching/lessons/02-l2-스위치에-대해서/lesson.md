---
id: u3-l09-l2-스위치에-대해서
title: L2 스위치는 MAC 주소로 프레임을 전달한다
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-09.md
wiki_diagram: units/03-layer2-switching/lessons/02-l2-스위치에-대해서/assets/diagrams/lesson-09.svg
page_metadata:
- terms:
  - 액세스 스위치 (Access switch)
  - 엔드포인트 (Endpoint)
  - 포트 (Port)
  illustrations:
  - file: "assets/photos/switch-8-port.jpg"
    title: "8포트 데스크톱 스위치"
    alt: "회색 8포트 스위치의 앞면에 여러 네트워크 케이블이 꽂혀 있습니다."
    caption: "가정이나 교실용 소형 스위치도 여러 유선 장치를 연결하는 LAN 장비입니다."
    credit: "사진: Teoprofe / Wikimedia Commons (CC0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Switch_sobremesa_con_8_puertos_Ethernet.jpg"
    license_label: "CC0"
    license_url: "http://creativecommons.org/publicdomain/zero/1.0/deed.en"
    after_paragraph: 1
  - file: "assets/photos/switch-front-view.jpg"
    title: "Ethernet 스위치 앞면"
    alt: "책상 위 회색 Linksys 스위치의 앞면과 상태 표시등이 보입니다."
    caption: "제품 모양은 달라도 여러 장치의 케이블을 모으는 역할은 같습니다."
    credit: "사진: CCDBarcodeScanner / Wikimedia Commons (CC BY-SA 4.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Ethernet_Switch_(Front_View).jpg"
    license_label: "CC BY-SA 4.0"
    license_url: "https://creativecommons.org/licenses/by-sa/4.0"
    after_paragraph: 1
  questions:
  - id: u3-02-p01-q01
    kind: choice
    difficulty: easy
    prompt: 24포트 스위치의 포트 수가 직접 가리키는 것은 무엇인가요?
    choices:
    - id: a
      text: LAN의 개수
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 프레임의 개수
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 연결할 수 있는 케이블 끝의 수
      feedback: 맞아요. 연결할 수 있는 케이블 끝의 수.
    - id: d
      text: IP 네트워크 수
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 반드시 연결되는 PC 대수
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-02-p01-q02
    kind: choice
    difficulty: medium
    prompt: 24포트 스위치의 포트 수를 가장 정확히 해석한 것은 무엇인가요?
    choices:
    - id: a
      text: 연결된 LAN의 개수를 뜻한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 전송할 수 있는 프레임의 개수다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 반드시 PC 24대만 연결할 수 있다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 24개의 IP 네트워크가 있다는 뜻이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 연결할 수 있는 케이블 끝의 수이며, PC만 연결하는 것은 아니다
      feedback: 맞아요. 연결할 수 있는 케이블 끝의 수이며, PC만 연결하는 것은 아니다.
    answer: e
  - id: u3-02-p01-q03
    kind: short
    prompt: PC나 프린터 같은 단말을 가까이에서 연결하는 스위치입니다. 영어로 무엇일까요?
    answers:
    - Access switch
    feedback: 정답은 Access switch입니다.
  animations:
  - file: l09-access-switch-ports.svg
    title: "액세스 스위치에 단말 연결하기"
    alt: "1번부터 8번까지 포트가 있는 액세스 스위치 아래로 노트북, 프린터, PC가 각각 1번, 3번, 5번 포트에 케이블로 연결되고 단말(Endpoint) 표시가 붙습니다. 이어서 스위치 위쪽의 무선 AP와 다른 스위치도 6번, 8번 포트에 연결됩니다. 마지막에 8개 포트 전체가 강조되며 8포트는 케이블 끝 8개를 꽂을 수 있다는 뜻이라고 정리합니다."
    caption: "액세스 스위치는 단말 가까이에서 여러 기기를 네트워크에 연결합니다. 포트 하나에 PC만 꽂는 것은 아니므로, 포트 수는 연결할 수 있는 케이블 끝의 수로 이해합니다."
- terms:
  - MAC 주소 테이블
  - 출발지 MAC 주소
  - 학습 (Learning)
  illustrations:
  - file: "assets/photos/switch-ports-cisco.jpg"
    title: "Cisco 스위치의 RJ45 포트"
    alt: "번호가 매겨진 Cisco 스위치의 RJ45 포트 여러 개와 LED가 보입니다."
    caption: "포트 번호를 따라가면 각 케이블이 스위치의 어디에 꽂혔는지 확인할 수 있습니다."
    credit: "사진: Ben Franske / Wikimedia Commons (CC BY-SA 4.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:RJ45_Switch_Ports.jpg"
    license_label: "CC BY-SA 4.0"
    license_url: "https://creativecommons.org/licenses/by-sa/4.0"
    after_paragraph: 1
  - file: "assets/photos/switch-vintage.jpg"
    title: "초기형 Ethernet 스위치"
    alt: "작은 회색 상자형 Ethernet 스위치가 책상 위에 놓여 있습니다."
    caption: "오래된 실물 사진입니다. 모델과 세대에 따라 포트 수와 모양이 다릅니다."
    credit: "사진: Syced / Wikimedia Commons (CC0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Peabird_Ethernet_switch_in_2003.jpg"
    license_label: "CC0"
    license_url: "http://creativecommons.org/publicdomain/zero/1.0/deed.en"
    after_paragraph: 1
  questions:
  - id: u3-02-p02-q01
    kind: choice
    difficulty: easy
    prompt: 스위치가 MAC 주소 테이블을 배울 때 프레임에서 보는 주소는 무엇인가요?
    choices:
    - id: a
      text: HTTP 경로
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 출발지 MAC 주소
      feedback: 맞아요. 출발지 MAC 주소.
    - id: c
      text: 목적지 IP 주소
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: Metric
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 목적지 MAC 주소만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-02-p02-q02
    kind: choice
    difficulty: medium
    prompt: 출발지 MAC 주소 02:00:00:00:00:0A 프레임이 3번 포트로 들어왔습니다. 스위치는 어떤 관계를 기록하나요?
    choices:
    - id: a
      text: IP 주소와 웹 서비스 포트의 관계
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 목적지 MAC 주소가 3번 포트에서 보였다는 관계
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 모든 MAC 주소를 모든 포트에 복사
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 프레임 전체를 3번 포트에 영구 저장
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 출발지 MAC 주소가 3번 포트에서 보였다는 관계
      feedback: 맞아요. 출발지 MAC 주소가 3번 포트에서 보였다는 관계.
    answer: e
  - id: u3-02-p02-q03
    kind: short
    prompt: 스위치가 주소와 그 주소가 들어온 포트를 함께 기록해 둔 표입니다. 영어로 무엇일까요?
    answers:
    - MAC address table
    feedback: 정답은 MAC address table입니다.
  animations:
  - file: l09-mac-learning.svg
    title: "출발지 MAC과 포트를 기억한다"
    alt: "PC-A, PC-B, PC-C, PC-D가 L2 스위치의 1, 3, 5, 8번 포트에 연결되어 있고 오른쪽 MAC 주소 테이블은 비어 있습니다. PC-A의 프레임이 3번 포트로 들어오면 스위치가 출발지 MAC 02:00:00:00:00:0A와 들어온 포트 3번을 읽고, 테이블에 0A → 3번 줄을 적습니다. 이어서 PC-A의 케이블을 4번 포트로 옮겨 다시 프레임을 보내면 같은 줄의 포트가 4번으로 고쳐집니다."
    caption: "스위치는 들어온 프레임의 출발지 MAC 주소를 그 프레임이 들어온 포트와 짝지어 기억합니다. 목적지 주소로 배우지 않으며, 장치가 포트를 옮기면 기록도 바뀝니다."
- terms:
  - 목적지 MAC 주소
  - 유니캐스트 (Unicast)
  illustrations:
  - file: "assets/photos/switch-ethernet-with-cables.jpg"
    title: "스위치와 여러 Ethernet 케이블"
    alt: "검은색 스위치에 노랑, 파랑 등 여러 색의 Ethernet 케이블이 꽂혀 있습니다."
    caption: "같은 스위치의 서로 다른 포트에 각 장치의 케이블을 연결합니다."
    credit: "사진: Raysonho @ Open Grid Scheduler / Grid Engine / Wikimedia Commons (CC0)"
    source_url: "https://commons.wikimedia.org/wiki/File:EthernetSwitch.jpg"
    license_label: "CC0"
    license_url: "http://creativecommons.org/publicdomain/zero/1.0/deed.en"
    after_paragraph: 1
  - file: "assets/photos/switch-ports-connected.jpg"
    title: "케이블이 꽂힌 스위치 포트"
    alt: "스위치 포트에 흰색 케이블이 연결되어 있고 LED 표시가 보입니다."
    caption: "LED는 연결 상태나 활동을 살펴보는 단서입니다. 뜻은 장비 설명서에서 확인하세요."
    credit: "사진: Ben Stanfield / Wikimedia Commons (CC BY-SA 2.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Switch-Ethernet-Connection.jpg"
    license_label: "CC BY-SA 2.0"
    license_url: "https://creativecommons.org/licenses/by-sa/2.0"
    after_paragraph: 1
  questions:
  - id: u3-02-p03-q01
    kind: choice
    difficulty: easy
    prompt: 스위치가 목적지 MAC 주소와 포트를 이미 알고 있다면 프레임을 어디로 보내나요?
    choices:
    - id: a
      text: 그 목적지에 해당하는 포트
      feedback: 맞아요. 그 목적지에 해당하는 포트.
    - id: b
      text: 라우터의 WAN 포트로 보낸다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 모든 포트에 항상 복사한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 프레임이 들어온 포트로만 보낸다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 아무 포트로나 무작위 전송한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-02-p03-q02
    kind: choice
    difficulty: medium
    prompt: PC-A의 프레임이 3번 포트로 들어오고 PC-B가 8번 포트로 알려져 있습니다. 올바른 동작 순서는 무엇인가요?
    choices:
    - id: a
      text: 출발지 주소를 지운 뒤 입력 포트로 되돌려 보낸다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 목적지 MAC 대신 IP를 조회해 모든 포트로 보낸다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 출발지 A를 학습한 뒤 목적지 B를 찾아 8번 포트로 전달한다
      feedback: 맞아요. 출발지 A를 학습한 뒤 목적지 B를 찾아 8번 포트로 전달한다.
    - id: d
      text: MAC 주소 테이블을 비우고 프레임을 폐기한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 목적지 B로부터 출발지 A를 학습한 뒤 3번 포트로 보낸다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-02-p03-q03
    kind: short
    prompt: 프레임이 도착할 연결 지점을 식별하기 위해 확인하는 MAC 주소는 출발지와 목적지 중 어느 것인가요? (영어로 답해주세요)
    answers:
    - destination MAC address
    feedback: 정답은 destination MAC address입니다.
  animations:
  - file: l09-known-unicast.svg
    title: "목적지를 알면 그 포트로만"
    alt: "MAC 주소 테이블에 PC-B의 주소 02:00:00:00:00:0B가 8번 포트로 적혀 있습니다. PC-A가 PC-B에게 보낸 프레임이 3번 포트로 들어오면 스위치가 먼저 출발지 0A를 3번 포트로 학습하고, 이어 목적지 0B를 테이블에서 찾아 8번 포트를 고릅니다. 프레임은 8번 포트로만 나가 PC-B가 받고, PC-C와 PC-D 쪽으로는 가지 않습니다."
    caption: "스위치는 출발지 MAC으로 학습하고, 목적지 MAC을 테이블에서 찾아 해당 포트 하나로만 프레임을 보냅니다. 관련 없는 단말에는 복사하지 않습니다."
- terms:
  - 알 수 없는 유니캐스트
  - 플러딩 (Flooding)
  - 브로드캐스트 (Broadcast)
  illustrations:
  - file: "assets/photos/switch-cables-angle.jpg"
    title: "케이블이 연결된 Ethernet 스위치"
    alt: "스위치의 여러 포트에 회색과 검은색 케이블이 꽂혀 있습니다."
    caption: "사진은 장비의 외형을 보여 줍니다. 프레임이 퍼지는 범위는 본문에서 설명합니다."
    credit: "사진: Raysonho @ Open Grid Scheduler / Grid Engine / Wikimedia Commons (CC0)"
    source_url: "https://commons.wikimedia.org/wiki/File:EthernetSwitch2.jpg"
    license_label: "CC0"
    license_url: "http://creativecommons.org/publicdomain/zero/1.0/deed.en"
    after_paragraph: 1
  - file: "assets/photos/switch-front-view.jpg"
    title: "다중 포트 스위치"
    alt: "책상 위 회색 Linksys 스위치의 앞면과 상태 표시등이 보입니다."
    caption: "제품 모양은 달라도 여러 장치의 케이블을 모으는 역할은 같습니다."
    credit: "사진: CCDBarcodeScanner / Wikimedia Commons (CC BY-SA 4.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Ethernet_Switch_(Front_View).jpg"
    license_label: "CC BY-SA 4.0"
    license_url: "https://creativecommons.org/licenses/by-sa/4.0"
    after_paragraph: 1
  questions:
  - id: u3-02-p04-q01
    kind: choice
    difficulty: easy
    prompt: 목적지 MAC 주소를 테이블에서 찾지 못했을 때 스위치가 같은 LAN에 퍼뜨리는 동작은 무엇인가요?
    choices:
    - id: a
      text: Unicast
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Flooding
      feedback: 맞아요. Flooding.
    - id: c
      text: Routing
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: Link up
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: Encapsulation
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-02-p04-q02
    kind: choice
    difficulty: medium
    prompt: 알 수 없는 목적지 MAC 주소로 온 프레임을 플러딩할 때 스위치는 어디로 내보내나요?
    choices:
    - id: a
      text: 들어온 포트를 제외한 같은 LAN의 나머지 포트들
      feedback: 맞아요. 들어온 포트를 제외한 같은 LAN의 나머지 포트들.
    - id: b
      text: 들어온 포트를 포함한 인터넷의 모든 장치
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 스위치의 포트 수와 무관하게 항상 폐기
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 모든 라우터의 WAN 방향으로 전송
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 같은 LAN의 포트 하나만 무작위로 선택
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-02-p04-q03
    kind: short
    prompt: 보내는 이가 한 대의 특정 목적지를 지정하는 통신 방식입니다. 영어로 무엇일까요?
    answers:
    - Unicast
    feedback: 정답은 Unicast입니다.
  animations:
  - file: l09-unknown-flooding.svg
    title: "목적지를 모르면 플러딩"
    alt: "MAC 주소 테이블이 비어 있고 PC-B는 아직 프레임을 보낸 적이 없습니다. PC-A가 PC-B에게 보낸 프레임이 3번 포트로 들어오면 스위치는 출발지 0A를 3번 포트로 학습하지만, 목적지 0B는 표에 없습니다. 스위치는 들어온 3번 포트만 빼고 1, 5, 8번 포트로 프레임을 복사해 보내고, 목적지 MAC이 자기 주소와 같은 PC-B만 받고 PC-C와 PC-D는 버립니다."
    caption: "목적지 MAC을 테이블에서 찾지 못하면 스위치는 들어온 포트를 뺀 같은 LAN의 다른 포트들로 플러딩합니다. 각 PC는 목적지 MAC을 확인해 자기 주소일 때만 받아들입니다."
- terms:
  - Link up (링크 업)
  - Link down (링크 다운)
  - LED
  animations:
  - file: l09-link-up-down.svg
    title: 케이블 연결과 링크 상태
    alt: PC와 스위치 포트 사이의 케이블이 연결되어 링크가 올라오고, 케이블이 끊기면 링크가 내려가는 과정을 보여 줍니다.
    caption: 케이블을 꽂는 것만으로 끝나는 것이 아니라 양쪽 장치의 연결이 성립해야 Link up입니다.
  illustrations:
  - file: "assets/photos/switch-port-leds.jpg"
    title: "스위치 포트 LED 확대"
    alt: "D-Link 스위치의 포트 LED 광 가이드가 가까이에서 보입니다."
    caption: "스위치마다 LED 색과 깜박임의 뜻이 다르므로 모델 설명을 확인하세요."
    credit: "사진: Nixdorf / Wikimedia Commons (CC BY-SA 4.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Light_guide_LEDs_on_switch.jpg"
    license_label: "CC BY-SA 4.0"
    license_url: "https://creativecommons.org/licenses/by-sa/4.0"
    after_paragraph: 1
  - file: "assets/photos/switch-rack-leds.jpg"
    title: "랙에 설치된 스위치의 LED"
    alt: "랙에 설치된 네트워크 스위치와 포트의 점등 LED가 보입니다."
    caption: "LED는 링크나 데이터 활동을 확인하는 단서이며, 정확한 뜻은 장비마다 다릅니다."
    credit: "사진: Shixart1985 / Wikimedia Commons (CC BY 2.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Network_switches_arranged_in_a_server_rack_with_visible_LED_lights_indicating_connection_status_and_power_levels.jpg"
    license_label: "CC BY 2.0"
    license_url: "https://creativecommons.org/licenses/by/2.0"
    after_paragraph: 1
  questions:
  - id: u3-02-p05-q01
    kind: choice
    difficulty: easy
    prompt: PC와 스위치 양쪽의 연결이 성립한 상태를 무엇이라고 하나요?
    choices:
    - id: a
      text: Link down
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Flooding
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Distribution layer
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: Uplink
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: Link up
      feedback: 맞아요. Link up.
    answer: e
  - id: u3-02-p05-q02
    kind: choice
    difficulty: medium
    prompt: 포트 LED가 켜져 Link up으로 보여도 이 사실만으로 알 수 없는 것은 무엇인가요?
    choices:
    - id: a
      text: 해당 장치에서 LED가 켜져 있다는 점
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 물리 링크가 성립했을 가능성
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 포트가 데이터를 주고받을 연결 상태인지
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 연결 상태를 확인할 단서가 있다는 점
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: IP 설정이나 인터넷 연결까지 정상인지 여부
      feedback: 맞아요. IP 설정이나 인터넷 연결까지 정상인지 여부.
    answer: e
  - id: u3-02-p05-q03
    kind: short
    prompt: 케이블 연결이 성립하지 않았거나 포트가 비활성인 상태를 가리키는 말은 무엇인가요?
    answers:
    - Link down
    feedback: 정답은 Link down입니다.
- terms:
  - 업링크 (Uplink)
  - 배포 스위치 (Distribution switch)
  illustrations:
  - file: "assets/photos/switch-rack-patch-panels.jpg"
    title: "랙의 스위치와 패치 패널"
    alt: "랙 안에 스위치와 패치 패널이 설치되어 있고 많은 케이블이 연결되어 있습니다."
    caption: "여러 스위치와 케이블을 한곳에 모아 두는 네트워크 랙의 예입니다."
    credit: "사진: Dsimic / Wikimedia Commons (CC BY-SA 4.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:19-inch_rackmount_Ethernet_switches_and_patch_panels.jpg"
    license_label: "CC BY-SA 4.0"
    license_url: "https://creativecommons.org/licenses/by-sa/4.0"
    after_paragraph: 1
  - file: "assets/photos/switch-rack-cables.jpg"
    title: "케이블이 연결된 네트워크 랙"
    alt: "네트워크 랙에 여러 스위치와 케이블이 설치되어 있습니다."
    caption: "랙은 여러 네트워크 장비를 정리해 설치하는 구조물입니다."
    credit: "사진: Yann / Wikimedia Commons (CC BY-SA 3.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Computer_rack_with_switches_and_cables.jpg"
    license_label: "CC BY-SA 3.0"
    license_url: "http://creativecommons.org/licenses/by-sa/3.0/"
    after_paragraph: 1
  questions:
  - id: u3-02-p06-q01
    kind: choice
    difficulty: easy
    prompt: 액세스 스위치에서 상위 네트워크 장비 쪽으로 이어지는 연결을 무엇이라고 하나요?
    choices:
    - id: a
      text: Frame
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Link up
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Uplink
      feedback: 맞아요. Uplink.
    - id: d
      text: MAC address table
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: Broadcast domain
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-02-p06-q02
    kind: choice
    difficulty: medium
    prompt: Uplink와 Link up의 차이를 가장 정확히 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: Uplink는 연결의 역할이고 Link up은 연결이 성립한 상태다
      feedback: 맞아요. Uplink는 연결의 역할이고 Link up은 연결이 성립한 상태다.
    - id: b
      text: 둘 다 포트 LED의 색상 이름이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Uplink는 연결 상태, Link up은 스위치 계층이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 두 용어는 항상 서로 바꿔 써도 된다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: Uplink는 단말 포트만 뜻하고 Link up은 광섬유만 뜻한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-02-p06-q03
    kind: short
    prompt: 여러 액세스 스위치를 모아 상위로 연결하는 계층입니다. 영어로 무엇일까요?
    answers:
    - Distribution layer
    feedback: 정답은 Distribution layer입니다.
  animations:
  - file: l09-uplink-distribution.svg
    title: "업링크로 배포 스위치에 모으기"
    alt: "1층과 2층 액세스 스위치에 PC가 두 대씩 연결되어 있고 위쪽에 배포 스위치가 있습니다. 1층 액세스 스위치에서 배포 스위치로 가는 주황 연결에 업링크 표시가 붙고, 2층 업링크도 이어지며 배포 계층 표시가 나타납니다. 이어서 PC 연결은 Link up인데 2층 업링크는 점선으로 Link down이 되는 장면으로 역할과 상태가 다르다는 점을 보여 주고, 마지막에 각 계층의 역할이 정리됩니다."
    caption: "업링크는 액세스 스위치에서 상위 장비로 이어지는 연결의 역할이고, Link up·down은 그 연결이 성립했는지를 가리킵니다. 배포 스위치는 여러 액세스 스위치의 연결을 모읍니다."
- terms:
  - L2 경로
  - 같은 LAN
  animations:
  - file: l09-l2-path.svg
    title: 같은 LAN의 두 PC가 스위치를 거쳐 통신
    alt: PC 3의 프레임이 액세스 스위치 A, 배포 스위치, 액세스 스위치 B를 거쳐 PC 5에 도착하고 응답이 돌아옵니다.
    caption: 같은 LAN에 속한 두 PC는 여러 스위치를 지나도 L2 프레임으로 통신할 수 있습니다.
  illustrations:
  - file: "assets/photos/switch-pair-cat5.jpg"
    title: "케이블로 연결된 두 스위치"
    alt: "두 네트워크 스위치와 CAT5 케이블이 함께 보입니다."
    caption: "두 스위치도 케이블로 연결해 단말 사이의 LAN 경로를 구성할 수 있습니다."
    credit: "사진: ShakataGaNai / Wikimedia Commons (CC BY-SA 3.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Network_switches.jpg"
    license_label: "CC BY-SA 3.0"
    license_url: "https://creativecommons.org/licenses/by-sa/3.0"
    after_paragraph: 1
  - file: "assets/photos/switch-rack-patch-panels.jpg"
    title: "여러 스위치와 패치 패널"
    alt: "랙 안에 스위치와 패치 패널이 설치되어 있고 많은 케이블이 연결되어 있습니다."
    caption: "여러 스위치와 케이블을 한곳에 모아 두는 네트워크 랙의 예입니다."
    credit: "사진: Dsimic / Wikimedia Commons (CC BY-SA 4.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:19-inch_rackmount_Ethernet_switches_and_patch_panels.jpg"
    license_label: "CC BY-SA 4.0"
    license_url: "https://creativecommons.org/licenses/by-sa/4.0"
    after_paragraph: 1
  questions:
  - id: u3-02-p07-q01
    kind: choice
    difficulty: easy
    prompt: 서로 다른 LAN이나 IP 네트워크 사이의 통신에 필요한 L3 장비의 예는 무엇인가요?
    choices:
    - id: a
      text: NIC
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Access switch만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Router
      feedback: 맞아요. Router.
    - id: d
      text: Ethernet frame
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: MAC address table
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-02-p07-q02
    kind: choice
    difficulty: medium
    prompt: 두 PC가 같은 LAN에 있을 때 스위치들이 프레임을 전달하는 원리로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 매 스위치마다 목적지 IP를 보고 항상 라우팅한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 각 스위치가 목적지 MAC을 자기 테이블에서 찾아 다음 포트로 전달한다
      feedback: 맞아요. 각 스위치가 목적지 MAC을 자기 테이블에서 찾아 다음 포트로 전달한다.
    - id: c
      text: 출발 PC가 인터넷 전체의 스위치 경로를 모두 지정한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 프레임은 MAC 주소 없이 케이블을 따라 자동으로 목적지를 찾는다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 배포 스위치는 언제나 L3만 수행한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-02-p07-q03
    kind: short
    prompt: 서로 다른 네트워크 사이에서 L3 라우팅을 수행할 수 있는 스위치입니다. 무엇일까요? (영어로 답해주세요)
    answers:
    - L3 switch
    feedback: 정답은 L3 switch입니다.
- terms:
  - MAC 주소 학습
  - 목적지 조회
  - 프레임 전달
  illustrations:
  - file: "assets/photos/switch-8-port.jpg"
    title: "8포트 스위치 다시 보기"
    alt: "회색 8포트 스위치의 앞면에 여러 네트워크 케이블이 꽂혀 있습니다."
    caption: "가정이나 교실용 소형 스위치도 여러 유선 장치를 연결하는 LAN 장비입니다."
    credit: "사진: Teoprofe / Wikimedia Commons (CC0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Switch_sobremesa_con_8_puertos_Ethernet.jpg"
    license_label: "CC0"
    license_url: "http://creativecommons.org/publicdomain/zero/1.0/deed.en"
    after_paragraph: 1
  - file: "assets/photos/switch-rack-leds.jpg"
    title: "랙 스위치 다시 보기"
    alt: "랙에 설치된 네트워크 스위치와 포트의 점등 LED가 보입니다."
    caption: "LED는 링크나 데이터 활동을 확인하는 단서이며, 정확한 뜻은 장비마다 다릅니다."
    credit: "사진: Shixart1985 / Wikimedia Commons (CC BY 2.0)"
    source_url: "https://commons.wikimedia.org/wiki/File:Network_switches_arranged_in_a_server_rack_with_visible_LED_lights_indicating_connection_status_and_power_levels.jpg"
    license_label: "CC BY 2.0"
    license_url: "https://creativecommons.org/licenses/by/2.0"
    after_paragraph: 1
  questions:
  - id: u3-02-p08-q01
    kind: choice
    difficulty: easy
    prompt: 스위치에서 프레임 전달의 첫 학습 단계에 해당하는 것은 무엇인가요?
    choices:
    - id: a
      text: 모든 포트로 무조건 프레임 복제
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 목적지 IP만 보고 인터넷 경로 계산
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 프레임 크기를 1,500바이트로 변경
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: LED 색에 따라 목적지 결정
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 출발지 MAC 주소와 들어온 포트 기록
      feedback: 맞아요. 출발지 MAC 주소와 들어온 포트 기록.
    answer: e
  - id: u3-02-p08-q02
    kind: choice
    difficulty: medium
    prompt: 목적지 MAC을 알고 있는 경우와 모르는 경우의 동작을 올바르게 비교한 것은 무엇인가요?
    choices:
    - id: a
      text: 알면 라우팅하고, 모르면 인터넷으로 폐기한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 알면 출발지 포트로 되돌리고, 모르면 테이블을 영구 보존한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 알면 플러딩하고, 모르면 항상 링크를 끊는다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 알면 해당 포트로 전달하고, 모르면 같은 LAN의 다른 포트로 플러딩한다
      feedback: 맞아요. 알면 해당 포트로 전달하고, 모르면 같은 LAN의 다른 포트로 플러딩한다.
    - id: e
      text: 둘 다 모든 포트로 무조건 전달한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-02-p08-q03
    kind: short
    prompt: 같은 LAN 안에서 목적지 MAC 주소가 알려졌을 때 프레임을 보내는 포트의 방향을 무엇으로 정하나요? (영어 용어로 답해주세요)
    answers:
    - forwarding
    feedback: 정답은 forwarding입니다.
  animations:
  - file: l09-l2-four-steps.svg
    title: "L2 스위치 동작 네 단계"
    alt: "PC-D의 케이블이 1번 포트에 연결되고, PC-A에게 보내는 프레임이 1번 포트로 들어옵니다. 스위치는 출발지 0D를 1번 포트로 테이블에 적고, 이미 아는 목적지 0A는 3번 포트로만 보냅니다. 이어서 PC-B에게 보낸 프레임은 목적지 0B가 표에 없어 1번을 뺀 3, 5, 8번 포트로 플러딩되고, PC-B만 받습니다. 오른쪽 아래에는 네 단계 목록이 하나씩 켜집니다."
    caption: "연결된 PC가 프레임을 보내면 스위치는 출발지 MAC과 들어온 포트를 배우고, 목적지 MAC을 찾아 아는 포트 하나로 전달합니다. 모르는 목적지는 같은 LAN의 다른 포트들로 플러딩합니다."
animations_dir: units/03-layer2-switching/lessons/02-l2-스위치에-대해서/assets/animations
---
이 Lesson에서는 L2 스위치가 프레임을 전달하는 순서를 배웁니다. 먼저 PC가 스위치에 연결되는 모습을 보고, 스위치가 출발지 MAC 주소를 기억하는 방법을 알아봅니다. 그다음 목적지 MAC 주소를 이미 아는 경우와 아직 모르는 경우를 비교하고, 여러 스위치를 거치는 경로까지 따라갑니다.

## Access switch · 단말을 네트워크에 연결하기

노트북이나 프린터를 유선 네트워크에 연결할 때 케이블 한쪽은 단말의 NIC에, 다른 쪽은 스위치의 포트에 꽂습니다. 이런 단말 가까이에서 여러 기기를 네트워크에 연결해 주는 스위치를 액세스 스위치(Access switch)라고 합니다. 회사나 학교의 한 교실에 컴퓨터와 프린터가 여럿 있다면, 각 기기의 케이블이 액세스 스위치의 서로 다른 포트에 연결되는 모습을 떠올리면 됩니다.

스위치의 포트는 데이터를 주고받는 연결 지점입니다. 예를 들어 24포트 스위치에는 장치를 연결할 수 있는 포트가 24개 있습니다. 다만 포트 하나가 항상 PC 한 대만을 뜻하는 것은 아닙니다. 다른 스위치나 무선 액세스 포인트처럼 네트워크 장비를 연결할 수도 있습니다. 그래서 포트 수는 “한 번에 연결할 수 있는 케이블 끝의 수”라고 이해하는 편이 정확합니다.

L2 스위치는 Ethernet 프레임을 전달할 때 목적지 MAC 주소를 사용합니다. MAC 주소는 네트워크 인터페이스를 구별하는 주소이고, 프레임은 같은 L2 구간에서 오가는 데이터 단위입니다. 이번 Lesson의 핵심 질문은 하나입니다. **스위치는 목적지 MAC 주소를 보고 어느 포트로 내보낼지 어떻게 알까요?**

## 스위치는 출발지 MAC과 포트를 기억한다

PC-A가 스위치의 3번 포트에 연결되어 있고 MAC 주소가 `02:00:00:00:00:0A`라고 해 봅시다. PC-A가 프레임을 보내면 스위치는 그 프레임이 들어온 포트 번호와 프레임의 **출발지 MAC 주소**를 함께 기록합니다. 스위치 안에는 이런 관계를 모아 둔 MAC 주소 테이블이 있습니다. 쉽게 말해 “이 주소의 장치는 이쪽 포트에서 보였다”는 메모입니다.

프레임이 3번 포트로 들어오고 출발지 주소가 `02:00:00:00:00:0A`라면, 스위치는 테이블에 `02:00:00:00:00:0A → 3번 포트`라고 배웁니다. 이 Lesson에서는 스위치에 연결된 PC들이 하나의 LAN에 있다고 가정합니다. 스위치가 주소를 배우는 방향은 **들어온 프레임의 출발지**에서 **들어온 포트**로입니다. 목적지 주소를 보고 그 주소가 어디에 있는지 배우는 것은 아닙니다.

PC-A가 다른 포트로 옮겨가 프레임을 보내면, 스위치는 같은 출발지 MAC 주소가 이번에는 새 포트에서 들어온 것을 확인하고 테이블을 갱신할 수 있습니다. 한동안 보이지 않는 장치의 기록은 시간이 지나면 삭제될 수도 있습니다. 그러므로 이 표는 영구적인 주소록이 아니라, 최근 프레임을 통해 배운 연결 정보를 담은 표입니다.

**외울 문장:** 스위치는 프레임의 출발지 MAC 주소를 보고, 그 프레임이 들어온 포트와 연결해 기억합니다.

## 목적지 MAC을 알면 그 포트로 보낸다

이제 PC-A가 PC-B에게 프레임을 보낸다고 합시다. 스위치는 먼저 프레임의 출발지 MAC 주소를 보고 PC-A가 들어온 포트를 학습합니다. 이어 목적지 MAC 주소를 테이블에서 찾습니다. PC-B가 8번 포트에 있다는 기록이 있다면, 스위치는 프레임을 8번 포트로 내보냅니다. 다른 포트로 같은 프레임을 모두 복사해 보내지 않습니다.

이 동작 덕분에 PC-A와 PC-B 사이의 통신이 관련 없는 모든 단말에게 매번 전달되지 않습니다. 식당에서 특정 테이블로 음식을 가져다주는 상황과 비슷합니다. 받는 테이블을 알고 있다면 식당의 모든 테이블에 음식을 하나씩 놓을 필요가 없습니다. 스위치가 테이블에서 목적지 MAC 주소를 찾아 해당 포트 쪽으로 전달하는 것이지요.

예를 들어 PC-A의 프레임이 3번 포트로 들어오고 목적지 PC-B가 8번 포트로 알려져 있으면 `3번 포트로 들어옴 → 출발지 A 기록 → 목적지 B 검색 → 8번 포트로 전달` 순서입니다. 스위치는 IP 주소나 웹 페이지 내용을 읽어 이 L2 전달을 결정하는 것이 아닙니다. 이 단계에서는 프레임의 MAC 주소와 MAC 주소 테이블이 기준입니다.

**외울 순서:** 출발지 MAC으로 학습하고, 목적지 MAC으로 찾아서, 해당 포트로 전달합니다.

## 목적지를 모르면 같은 LAN 안에 퍼뜨린다

스위치가 목적지 MAC 주소를 테이블에서 찾지 못하는 경우도 있습니다. 예를 들어 PC-B가 아직 한 번도 프레임을 보내지 않아 스위치가 어느 포트에 있는지 배우지 못했을 수 있습니다. 이때 스위치는 목적지 후보가 연결됐을 수 있는 포트들로 프레임을 퍼뜨립니다. 이 동작을 플러딩(Flooding)이라고 합니다. 단, 프레임이 들어온 포트로는 다시 내보내지 않습니다.

여기서 “모든 포트”는 스위치의 사용하지 않는 포트까지 무조건 뜻하지 않습니다. 프레임이 들어온 포트는 빼고, **같은 LAN에 속한 나머지 포트들**로 퍼집니다. 예를 들어 PC-A와 PC-B가 같은 LAN에 연결되어 있는데 스위치가 PC-B의 위치를 아직 모르면, PC-A에서 온 프레임을 PC-B가 있을 수 있는 여러 포트로 보냅니다. 그 포트에 연결된 PC들은 목적지 MAC 주소를 확인하고, 자기 주소와 일치하는 PC만 프레임을 받아들입니다. 다른 PC의 NIC는 자기에게 온 프레임이 아니면 일반적으로 해당 프레임을 상위 통신에 넘기지 않습니다. 다른 LAN으로 가야 하는 통신은 라우터나 L3 스위치가 전달합니다.

브로드캐스트 MAC 주소처럼 “이 구역의 모두에게” 보내는 프레임도 같은 LAN 안에서 퍼집니다. 알 수 없는 특정 MAC 주소로 보낸 프레임과 브로드캐스트는 목적지가 서로 다르지만, 스위치가 여러 포트로 복사해 내보내는 동작은 비슷해 보일 수 있습니다. 다음 Lesson에서는 브로드캐스트 주소와 브로드캐스트가 퍼지는 범위를 따로 자세히 살펴봅니다.

**기억할 구분:** 목적지를 알고 있으면 해당 포트로 전달하고, 목적지를 모르면 같은 LAN의 다른 포트들로 플러딩합니다.

## Link up · 케이블 연결과 통신 상태

케이블이 PC와 스위치에 연결되고 양쪽 인터페이스가 통신 가능한 상태를 이루면 링크가 올라왔다고 말합니다. 이를 Link up이라고 합니다. 케이블이 빠졌거나, 상대 장치의 전원이 꺼졌거나, 포트가 비활성화되어 연결이 성립하지 않으면 Link down일 수 있습니다. 따라서 케이블이 꽂혀 보인다는 사실만으로 링크가 반드시 정상이라고 단정할 수는 없습니다.

포트 주변의 LED는 연결 상태나 데이터 활동을 확인하는 데 도움을 줍니다. 다만 색과 깜박임의 뜻은 장비 모델과 LED 모드에 따라 달라질 수 있습니다. 어떤 장비에서는 녹색 불이 링크 연결을, 녹색 깜박임이 데이터 송수신을 나타내지만, 다른 색을 같은 의미로 모든 장비에 적용할 수는 없습니다. 정확한 뜻은 해당 장비의 표시나 설명서를 확인해야 합니다.

문제가 생기면 `케이블 양쪽이 제대로 꽂혔는가 → PC와 스위치가 켜져 있는가 → 포트 LED가 무엇을 나타내는가` 순서로 살펴볼 수 있습니다. LED가 꺼져 있다면 연결 자체가 없거나 포트가 꺼져 있을 수 있습니다. 반대로 링크 표시가 켜져 있어도 IP 설정이나 인터넷 연결까지 정상이라는 뜻은 아닙니다. LED는 우선 물리 연결과 포트 상태를 살펴보는 단서입니다.

## Uplink와 Distribution switch · 스위치를 이어 붙이기

액세스 스위치의 포트는 PC뿐 아니라 다른 스위치와 연결하는 데도 쓸 수 있습니다. 액세스 스위치에서 상위 네트워크 장비 쪽으로 이어지는 연결을 업링크(Uplink)라고 부릅니다. 업링크는 “위쪽으로 연결하는 역할”을 가리키고, Link up은 “연결이 성립한 상태”를 가리킵니다. 업링크가 Link down일 수도 있고, 단말 연결 포트도 Link up일 수 있으므로 두 용어를 섞지 마세요.

액세스 스위치 여러 대를 한곳에 모으는 계층을 배포 계층(Distribution layer)이라고 합니다. 이 역할을 맡는 장비를 배포 스위치라고 부르기도 합니다. 건물의 각 층에 있는 액세스 스위치를 층의 배포 스위치에 연결한다고 상상해 보세요. 단말 연결을 가까이에서 맡는 장비와 여러 연결을 모아 상위로 이어 주는 장비의 역할이 구분됩니다.

배포 스위치가 언제나 L2 스위치만 한다고 외우면 안 됩니다. 실제 설계에서는 배포 장비가 아래쪽에서는 L2 프레임을 전달하고, 위쪽으로는 L3 라우팅도 할 수 있습니다. 어디에서 L2와 L3의 경계를 두는지는 네트워크 설계에 따라 달라집니다. 지금은 “액세스는 단말 연결을 받고, 배포는 여러 액세스 연결을 모은다”는 역할 관계를 먼저 기억하면 됩니다.

## 같은 LAN의 단말 사이에서 L2 경로 따라가기

PC 3은 액세스 스위치 A에, PC 5는 액세스 스위치 B에 연결되어 있다고 해 봅시다. 두 PC가 **같은 LAN**에 속하고 각 스위치가 상대 MAC 주소를 향한 경로를 알고 있다면, 프레임은 `PC 3 → 액세스 스위치 A → 배포 스위치 → 액세스 스위치 B → PC 5` 순서로 전달될 수 있습니다. 중간 스위치마다 프레임의 목적지 MAC 주소를 자신의 테이블에서 찾고, 다음 포트로 넘깁니다.

마지막 스위치 B는 PC 5가 연결된 포트를 찾아 프레임을 내보냅니다. PC 5가 응답하면 반대 방향의 프레임도 각 스위치에서 같은 원리로 전달됩니다. 중요한 점은 출발지 PC가 인터넷 전체의 길을 직접 지정하는 것이 아니라, 각 스위치가 자신의 테이블을 보고 다음 포트를 고른다는 것입니다.

이 예는 두 PC가 같은 LAN에 있는 경우입니다. 서로 다른 LAN이나 IP 네트워크에 속한 PC끼리 통신하려면 라우터나 L3 스위치가 네트워크 사이에서 L3 전달을 해 주어야 합니다. 따라서 그림을 볼 때는 “같은 LAN 안의 L2 전달인가, 다른 네트워크로 나가는 L3 전달인가?”를 먼저 확인하면 경로를 잘못 외우지 않습니다.

## L2 스위치 동작 네 단계로 복습하기

새 PC가 스위치에 연결되면 PC는 프레임을 보냅니다. 스위치는 들어온 포트와 출발지 MAC 주소를 MAC 주소 테이블에 기록합니다. 이후 목적지 MAC 주소를 조회해 알고 있는 포트 하나로 전달합니다. 목적지를 아직 모르면 같은 LAN의 다른 포트들로 플러딩합니다. 이 순서를 이해하면 포트와 업링크, 액세스·배포 구조도 하나의 전달 과정 안에서 연결됩니다.

노트북에서 같은 LAN의 프린터로 프레임을 보낸다고 상상하고 스스로 질문해 보세요. 프레임의 출발지 MAC으로 무엇을 배우나요? 목적지 MAC을 이미 알고 있으면 어디로 보내나요? 모르면 어디까지 퍼뜨리나요? 다른 LAN에 있는 장치라면 어떤 L3 장비가 필요할까요? 답은 각각 `출발지 MAC과 들어온 포트`, `목적지 포트`, `같은 LAN의 다른 포트들`, `라우터 또는 L3 스위치`입니다.

**한 줄 암기:** 출발지 MAC으로 포트를 배우고, 목적지 MAC으로 포트를 찾아, 모르면 같은 LAN 안에서 퍼뜨립니다. 링크 상태는 연결의 성립 여부이고, 업링크는 스위치 사이의 상향 연결 역할입니다.
