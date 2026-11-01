---
id: u4-l11-ipv4주소의-기본-구조
title: IPv4 주소는 네트워크와 호스트를 어떻게 구분할까?
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-11.md
additional_sources:
  - https://github.com/physical-spark/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/03-1.md
  - https://github.com/physical-spark/course-network/blob/90a5cc40dec981b0e37fa334f3fae8ba673c8f32/studio/wiki/honja-network/03-2.md
wiki_diagram: units/04-layer3-addressing/lessons/01-ipv4주소의-기본-구조/assets/diagrams/lesson-11.svg
animations_dir: units/04-layer3-addressing/lessons/01-ipv4주소의-기본-구조/assets/animations
page_metadata:
- terms:
  - MAC 주소 (Media Access Control address)
  - IP 주소 (Internet Protocol address)
  - 계층 (Layer)
  illustrations:
  - file: assets/animations/l11-daily-name-vs-address.svg
    title: "이름만 적은 택배는 어디로 갈까?"
    alt: "왼쪽 아파트 단지에 ‘나’와 ‘민수’의 집과 경비실이, 오른쪽 바다시 3동에 ‘지영’의 집과 경비실이 있고 가운데 물류센터가 두 동네를 잇습니다. 민수에게 보낸 상자는 경비실을 거쳐 바로 도착합니다. 이름만 적은 지영의 상자는 경비실에서 멈추고 ‘어느 동네로 보내지?’라는 물음이 뜹니다. 동네 주소를 적자 상자가 물류센터를 거쳐 바다시 3동 경비실에 닿고, 그곳에서 이름을 보고 지영의 집에 배달됩니다."
    caption: "이름은 누구에게 줄지, 주소는 어느 동네로 갈지 알려 줍니다. 먼 곳으로 보내려면 둘 다 필요해요."
    after_paragraph: -1
  - file: assets/animations/l11-mac-vs-ip-reach.svg
    title: "MAC 주소만으로 다른 LAN까지 갈까?"
    alt: "왼쪽 우리 LAN에 노트북, 프린터, 스위치가, 오른쪽 다른 네트워크에 친구 PC, 다른 PC, 스위치가 있고 가운데 라우터가 두 네트워크를 잇습니다. 목적지 MAC이 프린터인 프레임은 스위치를 거쳐 프린터에 도착합니다. 친구 PC의 MAC만 적은 프레임은 ‘이 LAN에 없는 MAC’이라는 표시와 함께 스위치에 머뭅니다. 목적지 IP 10.1.2.7을 담은 패킷은 라우터를 거쳐 다른 네트워크의 스위치에 닿고, 그 LAN 안에서 친구 PC의 MAC으로 마지막 전달됩니다."
    caption: "MAC 주소는 지금 연결 구간에서 받을 상대를, IP 주소는 목적지가 있는 네트워크를 가리킵니다. 실제 장치에는 두 주소가 함께 설정되어 각자 역할을 맡아요."
    after_paragraph: 3
  questions:
  - id: u4-01-p01-q01
    kind: choice
    difficulty: easy
    prompt: "같은 LAN 안에서 Ethernet 프레임을 전달할 때 스위치가 목적지로 확인하는 주소는 무엇인가요?"
    choices:
    - id: a
      text: "IP 주소"
      feedback: "다시 확인해 보세요. IP 주소."
    - id: b
      text: "MAC 주소"
      feedback: "맞아요. MAC 주소입니다."
    - id: c
      text: "프리픽스 길이"
      feedback: "다시 확인해 보세요. 프리픽스 길이."
    - id: d
      text: "포트 번호"
      feedback: "다시 확인해 보세요. 포트 번호."
    - id: e
      text: "호스트 이름"
      feedback: "다시 확인해 보세요. 호스트 이름."
    answer: b
  - id: u4-01-p01-q04
    kind: choice
    difficulty: easy
    prompt: 다른 네트워크에 있는 친구에게 데이터를 보내려면, MAC 주소와 함께 어떤 주소가 필요할까요?
    choices:
    - id: a
      text: IP 주소
      feedback: 맞아요. IP 주소입니다.
    - id: b
      text: 스위치 포트 번호
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: c
      text: 케이블 이름
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: d
      text: 호스트의 사용자 이름
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: e
      text: 프레임 크기
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    answer: a
  - id: u4-01-p01-q02
    kind: choice
    difficulty: medium
    prompt: "다른 도시의 네트워크에 있는 친구에게 데이터를 보내려 할 때, 목적지 네트워크를 찾아가는 데 쓰이는 주소는 무엇인가요?"
    choices:
    - id: a
      text: "친구의 MAC 주소만"
      feedback: "다시 확인해 보세요. 친구의 MAC 주소만."
    - id: b
      text: "스위치 포트 번호"
      feedback: "다시 확인해 보세요. 스위치 포트 번호."
    - id: c
      text: "현재 LAN 이름"
      feedback: "다시 확인해 보세요. 현재 LAN 이름."
    - id: d
      text: "IP 주소"
      feedback: "맞아요. IP 주소입니다."
    - id: e
      text: "Ethernet 케이블 번호"
      feedback: "다시 확인해 보세요. Ethernet 케이블 번호."
    answer: d
  question_placements:
  - question_id: u4-01-p01-q01
    after_paragraph: 1
  - question_id: u4-01-p01-q04
    after_paragraph: 2
  page_id: u4l11-ip-address-overview
  video:
    video_id: GK3h936Co-k
    title: 'IP주소를 알아봅시다! (Feat. 공인/사설/고정/유동IP, 포트포워딩, DMZ, DDNS)'
    creator: 얄팍한 코딩사전
    duration_seconds: 495

- terms:
  - 비트 (bit)
  - 바이트 (byte)
  illustrations:
  - file: assets/animations/l11-daily-light-switches.svg
    title: "스위치판 하나로 몇 가지를 만들까?"
    alt: "전등 스위치 하나가 꺼짐에서 켜짐으로 바뀝니다. 이어 스위치 여덟 개가 나란히 놓이고, 모두 꺼진 판은 조합 번호 0, 모두 켜진 판은 조합 번호 255로 표시됩니다. 마지막에 스위치판 네 개가 나란히 걸리고, 각 판의 켜진 모양 아래에 192, 168, 0, 10이 적힙니다."
    caption: "켜고 끄는 스위치 여덟 개로 256가지 모양을 만들 수 있어요. 0부터 세면 0~255입니다."
    after_paragraph: -1
  - file: assets/animations/l11-bits-to-ipv4.svg
    title: "IPv4 주소는 32비트"
    alt: "비트 한 칸이 0에서 1로 바뀝니다. 여덟 칸이 모두 0이면 0, 모두 1이면 255로 표시됩니다. 마지막에 8비트 묶음 네 개가 각각 192, 168, 0, 10으로 읽히고 점으로 이어집니다."
    caption: "8비트 한 묶음은 0부터 255까지 나타내고, 그런 묶음 네 개가 모여 32비트 IPv4 주소 하나가 됩니다."
    after_paragraph: 3
  questions:
  - id: u4-01-p02-q01
    kind: choice
    difficulty: easy
    prompt: "IPv4 주소 한 개는 몇 비트로 이루어져 있나요?"
    choices:
    - id: a
      text: "8비트"
      feedback: "다시 확인해 보세요. 8비트."
    - id: b
      text: "16비트"
      feedback: "다시 확인해 보세요. 16비트."
    - id: c
      text: "24비트"
      feedback: "다시 확인해 보세요. 24비트."
    - id: d
      text: "32비트"
      feedback: "맞아요. 32비트입니다."
    - id: e
      text: "64비트"
      feedback: "다시 확인해 보세요. 64비트."
    answer: d
  - id: u4-01-p02-q04
    kind: choice
    difficulty: easy
    prompt: IPv4 주소에서 점 사이 숫자 하나는 몇 비트씩 묶은 값인가요?
    choices:
    - id: a
      text: 8비트
      feedback: 맞아요. 8비트입니다.
    - id: b
      text: 1비트
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: c
      text: 4비트
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: d
      text: 16비트
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: e
      text: 32비트
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    answer: a
  - id: u4-01-p02-q02
    kind: choice
    difficulty: medium
    prompt: "IPv4 주소를 점으로 구분해 네 숫자로 적을 때, 각 숫자는 몇 비트 묶음을 나타내나요?"
    choices:
    - id: a
      text: "8비트"
      feedback: "맞아요. 8비트입니다."
    - id: b
      text: "4비트"
      feedback: "다시 확인해 보세요. 4비트."
    - id: c
      text: "16비트"
      feedback: "다시 확인해 보세요. 16비트."
    - id: d
      text: "24비트"
      feedback: "다시 확인해 보세요. 24비트."
    - id: e
      text: "32비트"
      feedback: "다시 확인해 보세요. 32비트."
    answer: a
  - id: u4-01-p02-q03
    kind: short
    prompt: "IPv4 주소를 이루며 0과 1로 표현되는 정보의 가장 작은 단위는 무엇인가요? (영어 단어로 답해주세요)"
    answers:
    - "bit"
    feedback: "정답은 bit입니다."
  question_placements:
  - question_id: u4-01-p02-q01
    after_paragraph: 1
  - question_id: u4-01-p02-q04
    after_paragraph: 3

- terms:
  - ipconfig
  - 사설 주소 (private address)
  illustrations:
  - file: assets/animations/l11-daily-weights.svg
    title: "추 여덟 개로 무게 만들기"
    alt: "128g, 64g, 32g, 16g, 8g, 4g, 2g, 1g 추가 한 줄로 놓여 있습니다. 128g과 64g 추가 주황색으로 바뀌어 192g, 이어서 128g·32g·8g 추가 바뀌어 168g이 표시됩니다. 마지막에 모든 추가 주황색이 되어 255g이 되고, 256g은 만들 수 없다는 표시가 나타납니다."
    caption: "올린 추의 무게만 더하면 전체 무게가 나옵니다. 추 여덟 개로 만들 수 있는 가장 무거운 무게는 255g이에요."
    after_paragraph: -1
  - file: assets/animations/l11-byte-place-values.svg
    title: "8비트 한 묶음을 10진수로 읽기"
    alt: "자릿값 128부터 1까지 적힌 비트 여덟 칸이 있습니다. 11000000이 128 + 64 = 192로, 10101000이 128 + 32 + 8 = 168로 읽힙니다. 마지막에 11111111이 255로 읽히고, 192.168.0.256은 쓸 수 없다는 표시가 나타납니다."
    caption: "1인 자리의 자릿값을 더하면 점 사이 숫자가 됩니다. 한 묶음의 가장 큰 값은 255예요."
    after_paragraph: 2
  questions:
  - id: u4-01-p03-q01
    kind: choice
    difficulty: easy
    prompt: "8비트로 나타낼 수 있는 값의 범위는 무엇인가요?"
    choices:
    - id: a
      text: "0~255"
      feedback: "맞아요. 0~255입니다."
    - id: b
      text: "0~15"
      feedback: "다시 확인해 보세요. 0~15."
    - id: c
      text: "0~31"
      feedback: "다시 확인해 보세요. 0~31."
    - id: d
      text: "0~127"
      feedback: "다시 확인해 보세요. 0~127."
    - id: e
      text: "1~256"
      feedback: "다시 확인해 보세요. 1~256."
    answer: a
  - id: u4-01-p03-q04
    kind: choice
    difficulty: easy
    prompt: 유선과 Wi-Fi 어댑터가 모두 연결된 컴퓨터에서 주소를 볼 때 함께 확인할 것은 무엇인가요?
    choices:
    - id: a
      text: 어느 네트워크 어댑터의 주소인지
      feedback: 맞아요. 어느 네트워크 어댑터의 주소인지입니다.
    - id: b
      text: 모니터 크기
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: c
      text: 키보드 언어
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: d
      text: 폴더 이름
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: e
      text: 화면 해상도
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    answer: a
  - id: u4-01-p03-q02
    kind: choice
    difficulty: medium
    prompt: "2진수 10101000에서 1인 자리의 값을 더한 결과는 얼마인가요?"
    choices:
    - id: a
      text: "160"
      feedback: "다시 확인해 보세요. 160."
    - id: b
      text: "170"
      feedback: "다시 확인해 보세요. 170."
    - id: c
      text: "184"
      feedback: "다시 확인해 보세요. 184."
    - id: d
      text: "200"
      feedback: "다시 확인해 보세요. 200."
    - id: e
      text: "168"
      feedback: "맞아요. 168입니다."
    answer: e
  question_placements:
  - question_id: u4-01-p03-q01
    after_paragraph: 2
  - question_id: u4-01-p03-q04
    after_paragraph: 4

- terms:
  - Network ID (네트워크 식별자)
  - Host ID (호스트 식별자)
  - 프리픽스 길이 (prefix length)
  - 호스트 (Host)
  illustrations:
  - file: assets/animations/l11-daily-shop-doors.svg
    title: "가게는 하나, 문마다 주소가 있다"
    alt: "가운데 가게 한 곳이 있습니다. 왼쪽 정문이 꽃길에 닿아 ‘꽃길 10’, 오른쪽 뒷문이 별길에 닿아 ‘별길 3’이라는 주소가 붙습니다. 마지막에 ‘꽃길 10’의 10에 테두리가 생기고, ‘가게 = 찾아가는 곳 자체’와 ‘10 = 주소 끝의 번지’가 서로 다르다는 표시가 나타납니다."
    caption: "가게는 하나여도 길에 닿은 문마다 주소가 따로 있습니다. 주소 끝의 번지와 가게 자체는 다른 것이에요."
    after_paragraph: -1
  - file: assets/animations/l11-host-interfaces.svg
    title: "호스트는 하나, 인터페이스마다 IP"
    alt: "가운데 노트북 한 대가 있습니다. 왼쪽 유선 NIC는 유선 LAN에 연결되어 192.168.0.10을, 오른쪽 Wi-Fi NIC는 Wi-Fi 네트워크에 연결되어 10.0.0.7을 받습니다. 마지막에 192.168.0.10의 10에 테두리가 생기고, ‘호스트 = 노트북 장치’와 ‘Host ID = 주소 안의 10’이 다르다는 표시가 나타납니다."
    caption: "IP 주소는 장치 전체가 아니라 각 네트워크 인터페이스에 설정됩니다. 호스트는 장치이고, Host ID는 주소의 뒷부분이에요. 이 그림은 /24를 가정합니다."
    after_paragraph: 1
  questions:
  - id: u4-01-p04-q01
    kind: choice
    difficulty: easy
    prompt: "네트워크에서 데이터를 주고받는 끝단 장치의 예로 알맞은 것은 무엇인가요?"
    choices:
    - id: a
      text: "라우터의 경로표만"
      feedback: "다시 확인해 보세요. 라우터의 경로표만."
    - id: b
      text: "프리픽스 길이"
      feedback: "다시 확인해 보세요. 프리픽스 길이."
    - id: c
      text: "Ethernet 프레임의 헤더"
      feedback: "다시 확인해 보세요. Ethernet 프레임의 헤더."
    - id: d
      text: "스위치 포트 번호만"
      feedback: "다시 확인해 보세요. 스위치 포트 번호만."
    - id: e
      text: "노트북"
      feedback: "맞아요. 노트북입니다."
    answer: e
  - id: u4-01-p04-q04
    kind: choice
    difficulty: easy
    prompt: 호스트(host)와 Host ID는 같은 것을 가리키나요?
    choices:
    - id: a
      text: 아니요. 호스트는 장치이고 Host ID는 IP 주소의 한 부분입니다.
      feedback: 맞아요. 아니요. 호스트는 장치이고 Host ID는 IP 주소의 한 부분입니다.입니다.
    - id: b
      text: 네. 둘 다 MAC 주소입니다.
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: c
      text: 네. 둘 다 라우터를 뜻합니다.
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: d
      text: 아니요. Host ID는 케이블 이름입니다.
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: e
      text: 아니요. 호스트는 네트워크 번호입니다.
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    answer: a
  - id: u4-01-p04-q02
    kind: choice
    difficulty: medium
    prompt: "노트북에 유선과 무선 연결이 모두 있을 때, 이 Lesson의 설명에 가장 잘 맞는 것은 무엇인가요?"
    choices:
    - id: a
      text: "노트북은 IP 주소를 하나만 가질 수 있다"
      feedback: "다시 확인해 보세요. 노트북은 IP 주소를 하나만 가질 수 있다."
    - id: b
      text: "각 연결은 별도의 네트워크 인터페이스로 동작할 수 있다"
      feedback: "맞아요. 각 연결은 별도의 네트워크 인터페이스로 동작할 수 있다입니다."
    - id: c
      text: "두 연결은 언제나 같은 MAC 주소다"
      feedback: "다시 확인해 보세요. 두 연결은 언제나 같은 MAC 주소다."
    - id: d
      text: "유선 연결만 호스트가 된다"
      feedback: "다시 확인해 보세요. 유선 연결만 호스트가 된다."
    - id: e
      text: "무선 연결에는 IP 주소가 필요 없다"
      feedback: "다시 확인해 보세요. 무선 연결에는 IP 주소가 필요 없다."
    answer: b
  - id: u4-01-p04-q03
    kind: short
    prompt: "네트워크에 연결되어 주소를 주고받는 장치를 가리키는 말은 무엇인가요? (영어 단어로 답해주세요)"
    answers:
    - "host"
    feedback: "정답은 host입니다."
  question_placements:
  - question_id: u4-01-p04-q01
    after_paragraph: 1
  - question_id: u4-01-p04-q04
    after_paragraph: 2

- terms:
  - 목적지 (destination)
  illustrations:
  - file: assets/animations/l11-daily-apartment-unit.svg
    title: "‘101동 1203호’를 두 단계로 읽기"
    alt: "‘101동 1203호’라는 주소가 파란색 101동과 주황색 1203호로 나뉩니다. 101동 1204호는 같은 동, 102동 1203호는 다른 동으로 표시됩니다. 마지막에 구분 없이 ‘1011203’만 남자 10|11203, 101|1203, 1011|203 세 가지 끊는 방법에 물음표가 붙습니다."
    caption: "동을 먼저 찾고 그 안에서 호를 찾습니다. 다만 구분 표시가 없으면 어디까지가 동인지 알 수 없어요."
    after_paragraph: -1
  - file: assets/animations/l11-network-host-id.svg
    title: "IP 주소를 네트워크 부분과 호스트 부분으로"
    alt: "192.168.0.10이 /24 기준으로 파란색 Network ID 192.168.0과 주황색 Host ID 10으로 나뉩니다. 192.168.0.11은 같은 네트워크, 192.168.1.10은 다른 네트워크로 표시됩니다. 마지막에 프리픽스 없이 주소만 남자 192|168.0.10, 192.168|0.10, 192.168.0|10 세 후보에 물음표가 붙습니다."
    caption: "/24라는 기준이 있을 때 앞 24비트가 네트워크 부분, 뒤 8비트가 호스트 부분입니다. 주소 숫자만으로는 경계를 알 수 없어요."
    after_paragraph: 2
  questions:
  - id: u4-01-p05-q01
    kind: choice
    difficulty: easy
    prompt: "IP 주소에서 장치가 속한 네트워크를 나타내는 부분은 무엇인가요?"
    choices:
    - id: a
      text: "Host ID"
      feedback: "다시 확인해 보세요. Host ID."
    - id: b
      text: "MAC 주소"
      feedback: "다시 확인해 보세요. MAC 주소."
    - id: c
      text: "Network ID"
      feedback: "맞아요. Network ID입니다."
    - id: d
      text: "포트 번호"
      feedback: "다시 확인해 보세요. 포트 번호."
    - id: e
      text: "기본 게이트웨이"
      feedback: "다시 확인해 보세요. 기본 게이트웨이."
    answer: c
  - id: u4-01-p05-q04
    kind: choice
    difficulty: easy
    prompt: 192.168.0.10/24와 192.168.0.11/24는 같은 네트워크에 속하나요?
    choices:
    - id: a
      text: 네. /24 기준에서 앞의 24비트가 같습니다.
      feedback: 맞아요. 네. /24 기준에서 앞의 24비트가 같습니다.입니다.
    - id: b
      text: 아니요. 마지막 숫자가 다르면 항상 다른 네트워크입니다.
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: c
      text: 아니요. IP 주소는 네트워크를 구분하지 않습니다.
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: d
      text: 네. 숫자가 네 개면 무조건 같은 네트워크입니다.
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: e
      text: 판단할 수 없습니다. MAC 주소가 같아야 합니다.
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    answer: a
  - id: u4-01-p05-q02
    kind: choice
    difficulty: medium
    prompt: "동네와 집 번호 비유에서, 먼저 어느 동네로 갈지 정하는 부분은 무엇에 해당하나요?"
    choices:
    - id: a
      text: "Host ID"
      feedback: "다시 확인해 보세요. Host ID."
    - id: b
      text: "MAC 주소"
      feedback: "다시 확인해 보세요. MAC 주소."
    - id: c
      text: "Network ID"
      feedback: "맞아요. Network ID입니다."
    - id: d
      text: "Ethernet 포트"
      feedback: "다시 확인해 보세요. Ethernet 포트."
    - id: e
      text: "라우터의 이름"
      feedback: "다시 확인해 보세요. 라우터의 이름."
    answer: c
  - id: u4-01-p05-q03
    kind: short
    prompt: "IP 주소를 네트워크 부분과 호스트 부분으로 나눌 때, 장치가 속한 네트워크를 가리키는 부분은 무엇인가요? (한글 또는 영어로 답해주세요)"
    answers:
    - "Network ID"
    - "network id"
    - "네트워크 ID"
    - "네트워크 부분"
    feedback: "정답은 Network ID입니다."
  question_placements:
  - question_id: u4-01-p05-q01
    after_paragraph: 1
  - question_id: u4-01-p05-q04
    after_paragraph: 2

- terms:
  - 라우터 (Router)
  illustrations:
  - file: assets/animations/l11-daily-divider-rule.svg
    title: "칸막이를 어디에 두느냐"
    alt: "여덟 자리 번호 1, 0, 1, 2, 0, 3, 1, 5 위에 ‘규칙: 앞 6자리’ 칸막이가 서 있어 앞 여섯 칸은 파란색 동네 번호, 뒤 두 칸은 주황색 집 번호가 됩니다. 집 번호는 100가지라고 표시됩니다. 칸막이가 ‘앞 4자리’로 옮겨지면 집 번호가 네 자리가 되어 10,000가지가 됩니다. 마지막에 전체 지도, 동네 먼저, 그다음 집 순서가 화살표로 이어집니다."
    caption: "칸막이를 어디에 두느냐에 따라 동네 번호와 집 번호의 경계가 달라지고, 구별할 수 있는 집의 수도 달라져요."
    after_paragraph: -1
  - file: assets/animations/l11-prefix-boundary.svg
    title: "프리픽스 길이가 경계를 정한다"
    alt: "192.168.0.10을 32비트로 펼친 칸 위에 /24 경계선이 있어 앞 24비트는 파란색 네트워크 부분, 뒤 8비트는 주황색 호스트 부분이 됩니다. 호스트 부분은 2⁸ = 256가지로 표시됩니다. 경계선이 /16으로 옮겨지면 호스트 부분이 16비트가 되어 2¹⁶ = 65,536가지가 됩니다. 마지막에 전체 주소 공간, 목적지 네트워크, 그 안의 인터페이스 순서가 화살표로 이어집니다."
    caption: "프리픽스 길이가 네트워크와 호스트의 경계를 정합니다. 그림의 수는 비트 조합의 수이고, 실제로 쓸 수 있는 주소 수는 서브넷과 CIDR Lesson에서 계산해요."
    after_paragraph: 3
  questions:
  - id: u4-01-p06-q01
    kind: choice
    difficulty: easy
    prompt: "192.168.0.10/24에서 /24가 알려 주는 것은 무엇인가요?"
    choices:
    - id: a
      text: "네트워크 부분으로 사용하는 비트 수"
      feedback: "맞아요. 네트워크 부분으로 사용하는 비트 수입니다."
    - id: b
      text: "주소가 24개라는 뜻"
      feedback: "다시 확인해 보세요. 주소가 24개라는 뜻."
    - id: c
      text: "호스트 이름의 길이"
      feedback: "다시 확인해 보세요. 호스트 이름의 길이."
    - id: d
      text: "MAC 주소의 크기"
      feedback: "다시 확인해 보세요. MAC 주소의 크기."
    - id: e
      text: "24개의 라우터가 있다는 뜻"
      feedback: "다시 확인해 보세요. 24개의 라우터가 있다는 뜻."
    answer: a
  - id: u4-01-p06-q07
    kind: choice
    difficulty: easy
    prompt: 192.168.0.10/16에서 네트워크 부분은 어디까지인가요?
    choices:
    - id: a
      text: '192.168'
      feedback: 맞아요. 192.168입니다.
    - id: b
      text: '192'
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: c
      text: 192.168.0
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: d
      text: 192.168.0.10 전체
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    - id: e
      text: '10'
      feedback: 다시 생각해 보세요. 바로 앞의 예시와 설명을 떠올려 보세요.
    answer: a
  - id: u4-01-p06-q02
    kind: choice
    difficulty: medium
    prompt: "192.168.0.10/16에서 네트워크 부분으로 사용하는 것은 몇 비트인가요?"
    choices:
    - id: a
      text: "8비트"
      feedback: "다시 확인해 보세요. 8비트."
    - id: b
      text: "24비트"
      feedback: "다시 확인해 보세요. 24비트."
    - id: c
      text: "32비트"
      feedback: "다시 확인해 보세요. 32비트."
    - id: d
      text: "48비트"
      feedback: "다시 확인해 보세요. 48비트."
    - id: e
      text: "16비트"
      feedback: "맞아요. 16비트입니다."
    answer: e
  - id: u4-01-p06-q03
    kind: short
    prompt: "IP 주소에서 네트워크와 호스트의 경계를 나타내는 /24 같은 표기를 무엇이라고 하나요? (한글 또는 영어로 답해주세요)"
    answers:
    - "prefix length"
    - "prefix-length"
    - "프리픽스 길이"
    feedback: "정답은 prefix length입니다."
  - id: u4-01-p06-q04
    kind: choice
    difficulty: medium
    prompt: "192.168.0.10/24에서 네트워크 부분에 해당하는 것은 무엇인가요?"
    choices:
    - id: a
      text: "192.168.0"
      feedback: "맞아요. /24는 앞의 24비트인 192.168.0을 네트워크 부분으로 정합니다."
    - id: b
      text: "마지막 숫자 10"
      feedback: "다시 생각해 보세요. /24에서는 마지막 8비트가 호스트 부분입니다."
    - id: c
      text: "192.168.0.10 전체가 네트워크 부분"
      feedback: "다시 생각해 보세요. /24에서는 뒤의 8비트가 호스트 부분으로 남습니다."
    - id: d
      text: "192.168"
      feedback: "다시 생각해 보세요. 192.168은 /16일 때의 네트워크 부분입니다."
    - id: e
      text: "10.0"
      feedback: "주소의 네트워크 경계와 각 숫자를 비교해 다시 확인해 보세요."
    answer: a
  - id: u4-01-p06-q05
    kind: choice
    difficulty: medium
    prompt: "IP 주소를 네트워크 부분과 호스트 부분으로 나누어 읽는 이유로 가장 알맞은 것은 무엇인가요?"
    choices:
    - id: a
      text: "각 숫자를 서로 다른 프로토콜로 바꾸기 위해서"
      feedback: "다시 생각해 보세요. 두 부분은 목적지가 속한 네트워크와 그 안의 장치를 구분합니다."
    - id: b
      text: "IP 주소를 MAC 주소로 변환하기 위해서"
      feedback: "다시 생각해 보세요. 이 구분은 MAC 주소 변환을 뜻하지 않습니다."
    - id: c
      text: "앞부분으로 네트워크를 찾고, 뒷부분으로 그 네트워크 안의 인터페이스를 구별하기 위해서"
      feedback: "맞아요. 네트워크 부분과 호스트 부분이 각각 그 역할을 합니다."
    - id: d
      text: "주소의 숫자를 항상 네 개로 만들기 위해서"
      feedback: "다시 생각해 보세요. 점으로 구분된 네 숫자와 네트워크 경계는 같은 뜻이 아닙니다."
    - id: e
      text: "패킷의 크기와 전송 속도를 나타내기 위해서"
      feedback: "다시 생각해 보세요. 이 부분은 주소에서 목적지를 구분하는 역할입니다."
    answer: c
  - id: u4-01-p06-q06
    kind: choice
    difficulty: medium
    prompt: "192.168.0.10/24와 같은 /24 네트워크에서 호스트 부분은 무엇을 구별하나요?"
    choices:
    - id: a
      text: "인터넷 서비스 제공자"
      feedback: "다시 생각해 보세요. 호스트 부분은 네트워크 안의 인터페이스를 구별합니다."
    - id: b
      text: "주소가 속한 네트워크"
      feedback: "이것은 네트워크 부분의 역할입니다. 호스트 부분이 구별하는 대상을 생각해 보세요."
    - id: c
      text: "라우터가 선택한 다음 경로"
      feedback: "다시 생각해 보세요. 호스트 부분은 경로 선택을 나타내지 않습니다."
    - id: d
      text: "IP 주소가 IPv4인지 IPv6인지"
      feedback: "다시 생각해 보세요. 호스트 부분은 IP 버전을 표시하지 않습니다."
    - id: e
      text: "그 네트워크 안의 장치 인터페이스"
      feedback: "맞아요. 호스트 부분은 해당 네트워크 안에서 인터페이스를 구별합니다."
    answer: e
  question_placements:
  - question_id: u4-01-p06-q01
    after_paragraph: 1
  - question_id: u4-01-p06-q07
    after_paragraph: 2

- terms: []
  illustrations:
  - file: assets/animations/l11-daily-parcel-hubs.svg
    title: "물류센터를 거쳐 가는 택배"
    alt: "출발 집, A 물류센터, B 물류센터, 바다시 3동의 7번지 집이 한 줄로 이어져 있습니다. 상자에는 ‘최종: 바다시 3동 7번지’ 스티커와 ‘이번 구간’ 스티커가 붙어 있습니다. 상자가 구간을 하나 지날 때마다 이번 구간 스티커는 A 센터, B 센터, 7번지 집으로 바뀌지만 최종 주소는 그대로입니다. 마지막에 두 스티커의 변화를 표로 보여 줍니다."
    caption: "최종 주소는 끝까지 같고, 이번 구간에 받을 곳만 바뀝니다."
    after_paragraph: -1
  - file: assets/animations/l11-router-hops.svg
    title: "라우터는 목적지 네트워크 쪽으로 전달한다"
    alt: "192.168.0.10 노트북, 라우터 1, 라우터 2, 10.1.2.0/24 네트워크의 서버 10.1.2.7이 한 줄로 이어져 있습니다. 패킷에는 목적지 IP 10.1.2.7과 프레임의 목적지 MAC이 함께 표시됩니다. 구간을 하나 지날 때마다 목적지 MAC은 라우터 1, 라우터 2, 서버로 바뀌지만 목적지 IP는 그대로입니다. 마지막에 두 값의 변화를 표로 보여 줍니다."
    caption: "목적지 IP는 최종 서버를 계속 가리키고, Ethernet 프레임의 목적지 MAC은 구간마다 다음 수신자로 바뀝니다. NAT 같은 주소 변환이 없는 경우예요."
    after_paragraph: 3
  questions:
  - id: u4-01-p07-q01
    kind: choice
    difficulty: easy
    prompt: "다른 네트워크로 향하는 패킷을 다음 네트워크 쪽으로 전달하는 장치는 무엇인가요?"
    choices:
    - id: a
      text: "스위치"
      feedback: "다시 확인해 보세요. 스위치."
    - id: b
      text: "프린터"
      feedback: "다시 확인해 보세요. 프린터."
    - id: c
      text: "네트워크 어댑터"
      feedback: "다시 확인해 보세요. 네트워크 어댑터."
    - id: d
      text: "라우터"
      feedback: "맞아요. 라우터입니다."
    - id: e
      text: "모뎀 케이블"
      feedback: "다시 확인해 보세요. 모뎀 케이블."
    answer: d
  - id: u4-01-p07-q02
    kind: choice
    difficulty: easy
    prompt: "다른 네트워크에 있는 서버로 보낼 때, 현재 LAN의 Ethernet 프레임은 보통 누구의 MAC 주소를 목적지로 사용하나요?"
    choices:
    - id: a
      text: "먼 서버의 MAC 주소"
      feedback: "다시 확인해 보세요. 먼 서버의 MAC 주소."
    - id: b
      text: "다음으로 받을 라우터의 MAC 주소"
      feedback: "맞아요. 다음으로 받을 라우터의 MAC 주소입니다."
    - id: c
      text: "보내는 노트북 자신의 MAC 주소"
      feedback: "다시 확인해 보세요. 보내는 노트북 자신의 MAC 주소."
    - id: d
      text: "DNS 서버의 MAC 주소"
      feedback: "다시 확인해 보세요. DNS 서버의 MAC 주소."
    - id: e
      text: "목적지 포트 번호"
      feedback: "다시 확인해 보세요. 목적지 포트 번호."
    answer: b
  - id: u4-01-p07-q03
    kind: short
    prompt: "목적지 IP와 경로 정보를 살펴 다음 네트워크 쪽으로 패킷을 전달하는 장치는 무엇인가요? (한글 또는 영어로 답해주세요)"
    answers:
    - "router"
    - "라우터"
    feedback: "정답은 router입니다."
  - id: u4-01-p07-q04
    kind: choice
    difficulty: medium
    prompt: "라우터가 다른 네트워크로 향하는 패킷을 받았을 때, 다음 전달 방향을 정하는 데 주로 확인하는 것은 무엇인가요?"
    choices:
    - id: a
      text: "패킷을 만든 프로그램의 이름"
      feedback: "다시 확인해 보세요. 라우터는 목적지와 경로 정보를 살펴 다음 방향을 정합니다."
    - id: b
      text: "Ethernet 케이블의 길이"
      feedback: "다시 확인해 보세요. 케이블 길이가 아니라 목적지와 경로 정보를 이용합니다."
    - id: c
      text: "출발지 장치의 화면 해상도"
      feedback: "다시 확인해 보세요. 화면 설정은 경로 선택 기준이 아닙니다."
    - id: d
      text: "목적지 IP 주소와 라우터가 가진 경로 정보"
      feedback: "맞아요. 라우터는 목적지 IP와 경로 정보를 보고 다음 방향을 고릅니다."
    - id: e
      text: "목적지 장치의 사용자 이름"
      feedback: "다시 확인해 보세요. 사용자 이름이 아니라 목적지 IP와 경로 정보를 살펴봅니다."
    answer: d
  - id: u4-01-p07-q05
    kind: choice
    difficulty: medium
    prompt: "일반적인 라우터 전달에서 여러 네트워크 구간을 지나도 최종 목적지를 계속 가리키는 주소는 무엇인가요?"
    choices:
    - id: a
      text: "목적지 IP 주소"
      feedback: "맞아요. 목적지 IP는 최종 목적지를 계속 가리킵니다."
    - id: b
      text: "매 구간의 목적지 MAC 주소"
      feedback: "다시 확인해 보세요. 각 구간의 MAC 주소는 다음 프레임 수신자에 맞게 달라질 수 있습니다."
    - id: c
      text: "라우터의 포트 번호"
      feedback: "다시 확인해 보세요. 포트 번호는 최종 목적지 IP를 대신하지 않습니다."
    - id: d
      text: "스위치의 포트 개수"
      feedback: "다시 확인해 보세요. 스위치의 포트 개수는 패킷의 최종 목적지를 나타내지 않습니다."
    - id: e
      text: "각 네트워크의 이름"
      feedback: "다시 확인해 보세요. 네트워크 이름이 패킷의 목적지 주소로 유지되는 것은 아닙니다."
    answer: a
  - id: u4-01-p07-q06
    kind: choice
    difficulty: medium
    prompt: "패킷이 목적지 네트워크에 도착한 뒤에는 무엇을 향해 전달되나요?"
    choices:
    - id: a
      text: "항상 출발지 네트워크의 라우터로 돌아간다"
      feedback: "다시 확인해 보세요. 목적지 네트워크 안에서 최종 장치를 향해 전달됩니다."
    - id: b
      text: "인터넷의 모든 장치에 복사된다"
      feedback: "다시 확인해 보세요. 브로드캐스트처럼 모든 장치에 보내는 것을 뜻하지 않습니다."
    - id: c
      text: "목적지 장치의 네트워크 인터페이스"
      feedback: "맞아요. 목적지 네트워크 안에서 해당 장치의 인터페이스로 전달됩니다."
    - id: d
      text: "가장 가까운 DNS 서버만"
      feedback: "다시 확인해 보세요. DNS 서버가 아니라 패킷의 목적지 장치를 향합니다."
    - id: e
      text: "보내는 장치의 MAC 주소"
      feedback: "다시 확인해 보세요. 목적지 네트워크 안에서 최종 목적지 인터페이스를 향합니다."
    answer: c
  question_placements:
  - question_id: u4-01-p07-q01
    after_paragraph: 1
  - question_id: u4-01-p07-q02
    after_paragraph: 2

---
## MAC 주소만으로 다른 LAN까지 보낼 수 있을까?
<!-- learn-page-id: u4l11-ip-address-overview -->

같은 집의 노트북에서 같은 집의 프린터로 파일을 보낸다고 해 보자. 두 기기가 같은 LAN에 연결되어 있다면, Ethernet 프레임은 프린터의 네트워크 인터페이스가 가진 MAC 주소를 목적지로 삼아 전달될 수 있다. 이때 스위치는 프레임의 목적지 MAC 주소를 보고 어느 포트 쪽으로 보낼지 판단한다.

택배 상자를 떠올려 보자. 상자에는 물건 자체를 구별하는 제품 번호와, 지금 상자가 도착해야 할 집 주소가 함께 필요하다. 제품 번호만으로는 택배 기사가 어느 동네의 어느 집으로 가야 할지 알 수 없다. 네트워크에서도 MAC 주소는 현재 연결된 구간에서 상대를 구별하고, IP 주소는 목적지가 어느 네트워크에 있는지 찾아갈 때 쓰인다.

그런데 노트북에서 다른 도시의 친구에게 데이터를 보내려면 어떻게 될까? 스위치가 친구의 MAC 주소를 안다고 해도, 그 MAC 주소만으로는 친구가 어느 네트워크에 있는지, 거기까지 어떤 길로 가야 하는지 알 수 없다. 모든 LAN의 모든 기기가 세상의 모든 MAC 주소와 위치를 관리하는 것도 현실적이지 않다.

택배에 받는 사람 이름만 적으면 배송할 수 없는 것과 비슷하다. 받는 사람을 알아보는 정보와 실제로 찾아갈 주소가 모두 필요하다. MAC 주소는 네트워크 인터페이스에 연결된 L2 식별자이고, IP 주소는 L3에서 네트워크와 그 안의 목적지를 찾는 논리적 주소다. 둘 중 하나만 쓰는 것이 아니라, 하나의 장치가 통신할 때 둘 다 각자의 역할을 맡는다.

층을 나눈 건물처럼 위쪽 통신도 아래쪽 통신의 도움을 받는다. IP 패킷을 실은 Ethernet 프레임이 스위치를 지나가고, 그 위에서 TCP나 UDP, TLS, HTTP 같은 기능이 동작할 수 있다. 택배 비유는 주소의 역할이 다르다는 점을 이해하는 데까지만 사용하자. 실제 장치에는 MAC 주소와 IP 주소가 함께 설정될 수 있고, 이 정보가 택배 상자처럼 붙는 것도 아니다.

아래 영상은 **[참고용]**으로 가볍게 시청해 보자. 공인·사설 IP 같은 주변 개념도 함께 다루므로, 이 Lesson에서 배우는 IPv4 비트 구조와 프리픽스 경계를 대신하는 강의는 아니다.

## IPv4 주소는 32비트다

IP 주소는 네트워크에서 목적지를 표현하는 논리적인 주소다. 이 Lesson에서 먼저 다룰 IPv4 주소는 0과 1로 된 비트 32개로 이루어진다. 사람이 읽기 쉽도록 8비트씩 네 묶음으로 나누고, 각 묶음을 10진수로 적어 점으로 연결한다. 예를 들어 `192.168.0.10`은 IPv4 주소 한 개다.

전등 스위치 하나는 켜짐과 꺼짐 두 상태를 가진다고 생각해 보자. 컴퓨터의 비트(bit)도 둘 중 하나를 나타내며, 편의상 꺼짐을 `0`, 켜짐을 `1`로 적는다. 이런 스위치 여덟 개를 나란히 놓으면 각 자리마다 두 가지 선택이 있으므로 `2⁸`, 즉 256가지 조합이 생긴다. 여덟 비트를 묶은 단위가 바이트(byte)다.

여덟 칸이 모두 꺼진 `00000000`은 0이고 모두 켜진 `11111111`은 255다. 조합은 256가지지만 0부터 세기 때문에 한 묶음으로 나타내는 숫자는 `0`부터 `255`까지다. 따라서 `192.168.0.10`의 점 사이 숫자 하나는 각각 8비트 묶음을 읽기 쉽게 바꾼 값이다.

IPv4는 이런 비트 32개를 8개씩 네 묶음으로 나눠 적는다. `8 × 4 = 32`이므로 네 묶음이 주소 하나를 이룬다. 점은 사람에게 네 묶음을 보여 주는 구분 표시다. 다만 점으로 나눈 위치가 네트워크와 호스트의 경계까지 정해 주는 것은 아니다. 그 경계는 뒤에서 배울 프리픽스 길이가 알려 준다.

비트가 실제 컴퓨터 안에서 작은 전등으로 켜지는 것은 아니다. 전기 신호의 상태를 0과 1로 표현하는 것이고, 전등 스위치는 두 가지 상태의 조합을 떠올리기 위한 비유다.

## 8비트 한 묶음을 읽어 보자

내 컴퓨터의 IPv4 주소는 어디서 볼 수 있을까? Windows 명령 프롬프트에서 `ipconfig`를 실행하면 네트워크 어댑터별 설정이 나온다. 결과 중 `IPv4 주소` 항목에서 `192.168.0.10`처럼 점으로 나뉜 네 숫자를 찾아보자. 집이나 학교에서 `192.168`로 시작하는 주소를 볼 수 있지만, 환경에 따라 주소는 다를 수 있다.

점 사이의 숫자는 각자 8비트 한 묶음이므로 모두 `0`부터 `255` 사이여야 한다. 예를 들어 `192.168.0.256`은 마지막 묶음이 범위를 벗어나 IPv4의 올바른 표기가 아니다. 8비트 한 묶음에 256을 표현할 수 없기 때문이다.

숫자 하나를 2진수로 읽어 보자. `192`는 `11000000`이다. 8자리의 자릿값은 왼쪽부터 `128, 64, 32, 16, 8, 4, 2, 1`이므로, 켜진 두 자리 `128 + 64`를 더하면 192가 된다. 두 번째 숫자 `168`은 `10101000`이고, `128 + 32 + 8 = 168`이다. 점 사이 네 숫자는 이런 8비트 묶음을 각각 10진수로 바꿔 적은 것이다.

네트워크 어댑터가 여러 개라면 `ipconfig` 결과에도 여러 주소가 나올 수 있다.

유선 연결, 무선 연결, 가상 어댑터가 각자 주소를 가질 수 있기 때문이다. 주소를 볼 때는 숫자만 외우기보다 어느 어댑터에 속한 주소인지 함께 확인해 보자.

## 네트워크의 호스트와 주소의 Host ID

네트워크에서 호스트(host)는 데이터를 주고받는 끝단 장치를 가리키는 말이다. 노트북, 휴대전화, 서버, 프린터가 호스트가 될 수 있다. 다만 주소는 장치 전체에 막연히 붙는 이름이라기보다, 네트워크에 연결된 인터페이스를 구별하는 데 쓰인다. 노트북에 유선과 무선 연결이 모두 있다면 각각 별도의 네트워크 인터페이스로 동작할 수 있다.

이름이 비슷해 헷갈리지만, 호스트(host)와 Host ID는 같은 말이 아니다. 호스트는 네트워크에 연결된 컴퓨터나 장치를 가리키고, Host ID는 IP 주소 안에서 네트워크 부분과 나눈 나머지 부분을 가리킨다. 실제 주소는 장치 전체보다는 통신에 사용하는 네트워크 인터페이스에 설정된다고 생각하면 더 정확하다.

IP 주소는 직접 설정할 수도 있고, DHCP 같은 프로토콜로 자동으로 받을 수도 있다. 네트워크를 바꾸거나 설정이 달라지면 IP 주소도 달라질 수 있다. 반면 MAC 주소는 네트워크 인터페이스를 구별하는 L2 주소다. 둘은 크기와 역할이 다르며, MAC 주소가 있다고 해서 IP 주소가 필요 없어지는 것은 아니다.

## IP 주소를 네트워크 부분과 호스트 부분으로 나누기

IP 주소 한 줄에는 ‘어느 네트워크인가’와 ‘그 네트워크 안의 어느 인터페이스인가’라는 두 정보가 함께 담긴다. 앞부분을 네트워크 부분 또는 `Network ID`, 뒷부분을 호스트 부분 또는 `Host ID`라고 부른다.

주소 `192.168.0.10`을 동네와 집 번호에 비유해 보자. `/24`라는 기준을 함께 주면 앞의 24비트, 즉 `192.168.0`을 동네(Network ID), 뒤의 8비트 `10`을 그 동네 안의 번호(Host ID)로 볼 수 있다. 같은 기준에서 `192.168.0.11`도 같은 동네에 있는 다른 번호가 된다.

하지만 `192.168.0.10`만 보고 앞의 몇 비트가 동네인지 알 수는 없다. `192`까지일 수도, `192.168`까지일 수도, `192.168.0`까지일 수도 있다. 그리고 실제 네트워크 경계가 항상 앞의 24비트인 것도 아니다. `/24` 대 `/16` 같은 프리픽스 길이가 경계를 정하며, 다음 페이지에서 이 기준을 구체적으로 살펴본다.

이 비유에서 ‘동네와 번지’는 주소를 두 단계로 읽는다는 점을 설명한다. 실제 IP 주소에는 사람에게 읽히는 동네 이름이 적힌 것이 아니며, 경계도 주소 숫자만 보고 추측할 수 없다.

## 프리픽스 길이가 경계를 정한다

`192.168.0.10/24`에서 `/24`는 왼쪽부터 24비트를 네트워크 부분으로 사용한다는 뜻이다. 24비트는 8비트 묶음 세 개와 같으므로, 이 예에서는 `192.168.0`에 해당하는 앞 24비트가 네트워크를 나타내고 나머지 8비트가 그 안의 인터페이스를 구별한다.

같은 주소라도 프리픽스가 `/16`이면 결과가 달라진다. `192.168.0.10/16`에서는 앞 16비트, 즉 `192.168`에 해당하는 부분이 네트워크 부분이고 뒤 16비트가 호스트 부분이다. 그러므로 점으로 나눈 모양만 보고 경계를 외우면 안 된다. 주소를 읽을 때는 `/24`처럼 프리픽스도 같이 확인해야 한다.

왜 주소를 이런 두 부분으로 나눌까? 전 세계의 모든 장치를 번호 하나만으로 찾는다고 상상해 보자. 목적지가 어디에 있는지 알아내려면 모든 장치를 하나씩 확인해야 한다. 동네를 먼저 찾고 그 안에서 집 번호를 찾듯, 네트워크도 먼저 목적지 네트워크를 찾고 그 안에서 인터페이스를 찾으면 전달할 범위를 단계적으로 좁힐 수 있다.

경계가 달라지면 한 네트워크 안에서 구별할 수 있는 호스트 부분의 조합 수도 달라진다. `/24`는 호스트 부분이 8비트여서 `2⁸`가지, `/16`은 16비트여서 `2¹⁶`가지 조합을 표현한다. 그래서 `/16` 하나가 더 많은 조합을 담고, 네트워크 부분에 더 많은 비트를 쓰면 주소 공간을 더 작은 네트워크들로 나눌 수 있다. 실제 사용 가능 주소 수에는 네트워크 주소와 브로드캐스트 주소 같은 규칙이 적용되므로, 정확한 계산은 서브넷과 CIDR Lesson에서 다룬다.

이것은 ‘먼저 큰 범위를 찾고 그다음 안쪽을 찾는다’는 구조를 설명하는 비유다. 실제 네트워크 이름은 동네 이름처럼 사람이 읽는 단어가 아니며, 각 라우터는 설정된 경로 정보를 사용해 목적지 IP 패킷을 전달한다.

## 라우터는 목적지 네트워크 쪽으로 전달한다

택배 앱에서 상자의 배송 경로를 따라가 보면, 상자가 목적지 집으로 곧장 오지 않고 여러 물류센터를 거칠 수 있다. 센터에서 동네별 상자를 나누어 다음 지역으로 보내고, 목적지 지역에 도착한 뒤에는 개별 주소를 보고 마지막 배송을 한다. 네트워크에서도 라우터가 목적지 IP 주소와 자신이 가진 경로 정보를 보고 다음 네트워크 쪽으로 패킷을 전달한다.

노트북 `192.168.0.10/24`에서 다른 네트워크에 있는 서버로 데이터를 보내는 경우를 보자. 노트북은 목적지 IP가 자기 네트워크에 있는지 확인한다. 다른 네트워크라면 보통 기본 게이트웨이인 라우터로 먼저 프레임을 보낸다. 이 Ethernet 프레임의 목적지 MAC은 먼 서버의 MAC 주소가 아니라, 현재 LAN에서 다음으로 받을 라우터의 MAC 주소다.

라우터는 상자에 적힌 ‘최종 주소’를 읽고, 자신이 가진 경로 정보에서 그 목적지 네트워크로 갈 다음 방향을 고른다. 이처럼 목적지 IP와 경로 정보를 바탕으로 패킷의 다음 전달 방향을 결정하는 일을 라우팅이라고 한다. 네트워크 중간에 라우터가 여러 개 있으면 패킷은 여러 구간을 지나며, 각 라우터는 자기에게 도착한 패킷을 다음 방향으로 넘긴다.

Ethernet 구간을 하나 지날 때마다 다음 프레임을 받을 장치가 달라지므로 프레임의 출발지·목적지 MAC 주소도 해당 구간에 맞게 새로 정해진다. 반면 NAT 같은 주소 변환이 없는 일반적인 전달에서는 IP 패킷의 최종 목적지 IP가 목적지 서버를 계속 가리킨다. 목적지 네트워크에 들어선 뒤에는 그 LAN 안에서 최종 인터페이스까지 전달된다.

물류센터 비유도 한계가 있다. 실제 라우터는 상자를 창고에 쌓아 두고 분류하는 곳이 아니라, 패킷의 목적지와 경로 정보를 살펴 다음 연결로 전달하는 장치다. 핵심은 “Network ID로 목적지 네트워크 쪽을 찾고, 그 네트워크에 도착하면 Host ID가 가리키는 인터페이스까지 전달한다”는 순서다. MAC 주소는 현재 링크에서 다음 수신자를 구별하고, IP 주소는 네트워크 사이에서 최종 목적지를 가리킨다.

이제 `192.168.0.10/24`를 한 번에 읽어 보자. 점으로 구분한 네 숫자는 8비트씩 네 칸으로 표현한 IPv4 주소다. `/24`는 앞의 24비트가 네트워크 부분이고 뒤의 8비트가 호스트 부분이라고 알려 준다. 이 경계를 바탕으로 라우터는 목적지 네트워크를 향해 패킷을 전달한다. ‘네 칸으로 읽기’와 ‘네트워크와 호스트로 나누기’는 서로 다른 기준이지만, 둘 다 IP 주소를 이해하는 데 필요하다.
