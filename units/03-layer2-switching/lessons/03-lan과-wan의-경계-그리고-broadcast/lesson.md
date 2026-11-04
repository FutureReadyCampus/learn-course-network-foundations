---
id: u3-l10-lan과-wan의-경계-그리고-broadcast
title: LAN과 WAN의 경계 그리고 Broadcast
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-10.md
wiki_diagram: units/03-layer2-switching/lessons/03-lan과-wan의-경계-그리고-broadcast/assets/diagrams/lesson-10.svg
page_metadata:
- terms:
  - 유니캐스트 (Unicast)
  - 브로드캐스트 (Broadcast)
  - 브로드캐스트 도메인 (Broadcast domain)
  questions:
  - id: u3-03-p01-q01
    kind: choice
    difficulty: easy
    prompt: 친구 한 명에게 쪽지를 직접 건네듯, 한 장치를 수신자로 지정해 보내는 방식은 무엇인가요?
    choices:
    - id: a
      text: Broadcast
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: Unicast
      feedback: 맞아요. Unicast.
    - id: c
      text: WAN
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: Flooding
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: VLAN
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: b
  - id: u3-03-p01-q05
    kind: choice
    difficulty: easy
    prompt: 친구 한 명에게 보내는 쪽지와 교실 전체에 하는 안내 방송 중, 여러 장치가 확인하게 하는 방식은 무엇인가요?
    choices:
    - id: a
      text: Unicast
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: Broadcast
      feedback: 맞아요. Broadcast.
    - id: c
      text: Routing
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: Header
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: Virtualization
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: b
  - id: u3-03-p01-q02
    kind: choice
    difficulty: medium
    prompt: Broadcast에서 “모두”가 가리키는 범위는 무엇인가요?
    choices:
    - id: a
      text: 같은 제조사의 컴퓨터만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 전 세계 인터넷에 연결된 모든 장치
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 같은 스위치에 직접 꽂힌 PC만 항상
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 같은 브로드캐스트 도메인에 속한 장치들
      feedback: 맞아요. 같은 브로드캐스트 도메인에 속한 장치들.
    - id: e
      text: 같은 IP 주소를 쓰는 장치만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p01-q03
    kind: short
    prompt: 같은 네트워크 범위 안의 모든 장치에게 전달되는 통신 방식입니다. 영어로 답해주세요.
    answers:
    - broadcast
    - 브로드캐스트
    feedback: 정답은 Broadcast(브로드캐스트)입니다.
  - id: u3-03-p01-q04
    kind: choice
    difficulty: medium
    prompt: 알 수 없는 Unicast와 Broadcast의 차이로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 둘 다 목적지가 모든 장치다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: Unicast는 특정 MAC을 찾지 못한 상태이고 Broadcast는 구역 전체를 수신자로 지정한다
      feedback: 맞아요. Unicast는 특정 MAC을 찾지 못한 상태이고 Broadcast는 구역 전체를 수신자로 지정한다.
    - id: c
      text: 둘 다 라우터가 만든다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: Broadcast는 한 장치만 받는다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: Unicast는 IP 주소를 쓰지 않는다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: b
  question_placements:
  - question_id: u3-03-p01-q01
    after_paragraph: 1
  - question_id: u3-03-p01-q05
    after_paragraph: 2
  animations:
  - file: l10-unicast-vs-broadcast.svg
    title: "Unicast와 Broadcast"
    alt: "PC 1이 점선 구역 안의 PC 2~5와 연결되어 있습니다. 먼저 파란 Unicast가 PC 4 한 대에만 가고, 이어서 주황 Broadcast가 구역 안 네 대에 한꺼번에 퍼진 뒤 네 대 모두 내용 확인 표시가 켜집니다. 마지막에 구역이 브로드캐스트 도메인으로 표시되고, 구역 밖 PC에는 닿지 않는다는 문구가 나옵니다."
    caption: "Unicast는 한 곳을 지정해 보내고, Broadcast는 같은 브로드캐스트 도메인 안의 모두에게 보냅니다. 받은 장치는 모두 내용을 확인해야 합니다."
- terms:
  - 브로드캐스트 도메인 (Broadcast Domain)
  - LAN 구역
  questions:
  - id: u3-03-p02-q01
    kind: choice
    difficulty: easy
    prompt: 아파트 안내 방송이 닿는 “이 구역”을 네트워크에서 가리키는 말은 무엇인가요?
    choices:
    - id: a
      text: IP 주소
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: 이더넷 케이블
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 브로드캐스트 도메인
      feedback: 맞아요. 브로드캐스트 도메인.
    - id: d
      text: 프레임 헤더
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 라우팅 표
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: c
  - id: u3-03-p02-q05
    kind: choice
    difficulty: easy
    prompt: 한 건물이 언제나 브로드캐스트 도메인 하나만으로 이루어져야 하나요?
    choices:
    - id: a
      text: 네, 건물마다 반드시 하나다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: 아니요, 관리 방식에 따라 여러 구역으로 나뉠 수 있다
      feedback: 맞아요. 아니요, 관리 방식에 따라 여러 구역으로 나뉠 수 있다.
    - id: c
      text: 네, 도메인은 한 PC만 포함한다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 아니요, 도메인은 스위치와 무관하다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: LAN에는 방송 구역이 없다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: b
  - id: u3-03-p02-q02
    kind: choice
    difficulty: medium
    prompt: Ethernet 브로드캐스트를 받는 장치의 범위를 설명하는 것은 무엇인가요?
    choices:
    - id: a
      text: 브로드캐스트 도메인의 크기와 경계
      feedback: 맞아요. 브로드캐스트 도메인의 크기와 경계.
    - id: b
      text: 인터넷 회선의 속도만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Wi-Fi 신호가 닿는 거리와 항상 동일한 범위
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: MAC 주소의 제조사 정보
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 프레임 안의 데이터 크기만
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-03-p02-q03
    kind: short
    prompt: 같은 건물 안에서도 두 구역이 서로 다른 브로드캐스트 도메인으로 나뉘어 있습니다. 한쪽에서 보낸 Ethernet 브로드캐스트가 다른 쪽에도 직접 전달될까요? 예 또는 아니요로 답하세요.
    answers:
    - 아니요
    - 아니오
    - "no"
    feedback: 정답은 아니요입니다. Ethernet 브로드캐스트는 보낸 쪽의 브로드캐스트 도메인 안에서 전달되며, 라우터는 기본적으로 이를 다른 도메인으로 전달하지 않습니다.
  question_placements:
  - question_id: u3-03-p02-q01
    after_paragraph: 1
  - question_id: u3-03-p02-q05
    after_paragraph: 2
  animations:
  - file: l10-apartment-broadcast-zone.svg
    title: "방송이 닿는 구역"
    alt: "왼쪽 아파트에서 관리실이 방송하자 연결된 여덟 세대가 모두 켜지고, 이어서 구역이 둘로 나뉘어 구역 1의 세대만 방송을 듣습니다. 오른쪽에서는 PC 1의 방송을 받은 스위치가 PC 2~4로 전달해 모두 확인하고, 그 범위가 브로드캐스트 도메인으로 묶여 표시됩니다."
    caption: "방송이 닿는 구역을 브로드캐스트 도메인이라고 합니다. 방송을 보낼 수 있는지만큼 어느 구역까지 들리게 할지가 중요합니다."
- terms:
  - 16진수 (Hexadecimal)
  - 브로드캐스트 MAC 주소 (Broadcast MAC address)
  animations:
  - file: l10-broadcast-mac-all-ones.svg
    title: 전구 48개가 모두 켜진 주소는 ‘모두에게’
    alt: 전구 8개가 모두 켜져 FF가 되고, 이것이 여섯 칸 이어져 FF:FF:FF:FF:FF:FF가 되어 봉투의 받는 사람 칸에 들어가는
      장면입니다.
    caption: FF는 켜진 전구 8개이고, 6칸이 모두 FF인 MAC 주소는 브로드캐스트를 뜻합니다.
  questions:
  - id: u3-03-p03-q01
    kind: choice
    difficulty: easy
    prompt: 택배의 받는 사람 칸에 “이 구역 모두”라고 적는 것과 비슷한 Ethernet 주소의 목적은 무엇인가요?
    choices:
    - id: a
      text: 한 장치에만 보내기
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: 목적지 IP 찾기
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 스위치 포트 번호 기록하기
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 브로드캐스트 구역의 모두에게 알리기
      feedback: 맞아요. 브로드캐스트 구역의 모두에게 알리기.
    - id: e
      text: 파일 크기 표시하기
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: d
  - id: u3-03-p03-q05
    kind: choice
    difficulty: easy
    prompt: Ethernet 브로드캐스트 MAC 주소를 한눈에 알아보는 표기는 무엇인가요?
    choices:
    - id: a
      text: 00:00:00:00:00:00
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: 10.0.0.255
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: AA:BB:CC:11:22:33
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: FF:FF:FF:FF:FF:FF
      feedback: 맞아요. FF:FF:FF:FF:FF:FF.
    - id: e
      text: 01:00:5E:00:00:01
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: d
  - id: u3-03-p03-q02
    kind: choice
    difficulty: medium
    prompt: FF:FF:FF:FF:FF:FF가 48비트 모두 1을 나타내는 이유는 무엇인가요?
    choices:
    - id: a
      text: FF 쌍이 1비트씩 여섯 번 나타난다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 콜론이 네트워크 범위를 나타내기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: F 하나가 48비트를 뜻한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 16진수 F 하나가 4개의 1이고 여섯 쌍이 48비트를 채운다
      feedback: 맞아요. 16진수 F 하나가 4개의 1이고 여섯 쌍이 48비트를 채운다.
    - id: e
      text: 각 16진수 칸은 8비트여서 모두 6비트다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p03-q04
    kind: choice
    difficulty: medium
    prompt: FF:FF:FF:FF:FF:FF라는 값만 보면 언제나 Broadcast라고 부를 수 있나요?
    choices:
    - id: a
      text: 아니요. Ethernet 프레임의 목적지 MAC 주소 자리에 있을 때 Broadcast를 뜻한다
      feedback: 맞아요. 아니요. Ethernet 프레임의 목적지 MAC 주소 자리에 있을 때 Broadcast를 뜻한다.
    - id: b
      text: 네, 어떤 데이터의 어느 위치든 모두 Broadcast다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 숫자가 여섯 쌍이면 IP 주소다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 첫 쌍만 FF이면 항상 Broadcast다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: Broadcast는 숫자와 관계없다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: a
  question_placements:
  - question_id: u3-03-p03-q01
    after_paragraph: 1
  - question_id: u3-03-p03-q05
    after_paragraph: 2
- terms:
  - 프레임 (Frame)
  - 헤더 (Header)
  - 배포 스위치 (Distribution Switch)
  animations:
  - file: l10-broadcast-flood-switches.svg
    title: 방송 프레임은 스위치마다 갈라져 퍼진다
    alt: PC 1이 방송 프레임을 보내자 스위치 A, 배포 스위치 C, 스위치 B를 거쳐 모든 PC로 프레임이 복사되어 퍼지는 장면입니다.
    caption: 받는 곳이 FF:FF:FF:FF:FF:FF인 프레임은 스위치를 지날 때마다 여러 갈래로 복사됩니다.
  questions:
  - id: u3-03-p04-q01
    kind: choice
    difficulty: easy
    prompt: 택배 상자의 송장처럼, 프레임에서 출발지·목적지 MAC 주소를 담는 곳은 어디인가요?
    choices:
    - id: a
      text: Payload
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: 케이블
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 프레임 헤더
      feedback: 맞아요. 프레임 헤더.
    - id: d
      text: 브로드캐스트 도메인
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 라우터 표
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: c
  - id: u3-03-p04-q05
    kind: choice
    difficulty: easy
    prompt: PC가 브로드캐스트 프레임을 보내면 스위치는 보통 어떻게 하나요?
    choices:
    - id: a
      text: 받은 포트로만 되돌린다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: 프레임을 항상 버린다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 입력 포트를 제외한 여러 포트로 전달한다
      feedback: 맞아요. 입력 포트를 제외한 여러 포트로 전달한다.
    - id: d
      text: IP 주소를 바꾼다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 다른 IP 네트워크로 라우팅한다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: c
  - id: u3-03-p04-q03
    kind: short
    prompt: Ethernet 프레임의 앞부분에서 출발지·목적지 주소 같은 전달 정보를 담는 부분입니다. 무엇일까요? (영어로 답해주세요)
    answers:
    - header
    - frame header
    - 헤더
    - 프레임 헤더
    feedback: 정답은 header(프레임 헤더)입니다.
  - id: u3-03-p04-q04
    kind: choice
    difficulty: medium
    prompt: 브로드캐스트 프레임을 받은 스위치가 들어온 포트를 다시 제외하는 이유는 무엇인가요?
    choices:
    - id: a
      text: 보낸 쪽으로 같은 프레임을 되돌려 보내지 않기 위해
      feedback: 맞아요. 보낸 쪽으로 같은 프레임을 되돌려 보내지 않기 위해.
    - id: b
      text: IP 주소를 숨기기 위해
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 프레임의 MAC 주소를 지우기 위해
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 다른 VLAN을 만들기 위해
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 케이블 속도를 높이기 위해
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: a
  question_placements:
  - question_id: u3-03-p04-q01
    after_paragraph: 1
  - question_id: u3-03-p04-q05
    after_paragraph: 2
- terms:
  - 트래픽 (Traffic)
  - 호스트 (Host)
  questions:
  - id: u3-03-p05-q01
    kind: choice
    difficulty: easy
    prompt: 교실 전체에 안내 방송이 한 번 울리면 누가 들을 수 있나요?
    choices:
    - id: a
      text: 교실에 있는 모두가 들을 수 있다
      feedback: 맞아요. 교실에 있는 모두가 들을 수 있다.
    - id: b
      text: 옆 교실 한 사람만 듣는다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 방송한 사람만 듣는다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 아무도 들을 수 없다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 다른 건물에만 전달된다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: a
  - id: u3-03-p05-q05
    kind: choice
    difficulty: easy
    prompt: Broadcast 프레임이 많아지면 네트워크가 실제로 쓰는 자원은 무엇인가요?
    choices:
    - id: a
      text: 화면과 저장 공간
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: 링크 대역폭과 장치 처리 시간
      feedback: 맞아요. 링크 대역폭과 장치 처리 시간.
    - id: c
      text: IP 주소와 MAC 주소의 길이
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 키보드와 마우스
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 케이블과 포트 색상
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: b
  - id: u3-03-p05-q02
    kind: choice
    difficulty: medium
    prompt: Broadcast가 여러 링크와 장치의 자원을 쓰는 이유로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 프레임이 전달될 때 항상 1,000배로 커지기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 한 프레임이 전 세계 모든 케이블로 반드시 전달되기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 여러 스위치 방향으로 전달되고 범위 안 장치들이 확인하기 때문이다
      feedback: 맞아요. 여러 스위치 방향으로 전달되고 범위 안 장치들이 확인하기 때문이다.
    - id: d
      text: 브로드캐스트는 데이터 없이 LED만 켜기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 라우터가 매 프레임을 복제하기 때문이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  - id: u3-03-p05-q03
    kind: short
    prompt: 네트워크에서 장치 사이를 오가며 링크와 장치가 처리하는 데이터 흐름의 glossary 용어는 무엇인가요? (영어 또는 한글)
    answers:
    - traffic
    - network traffic
    - 트래픽
    - 네트워크 트래픽
    feedback: 정답은 traffic(네트워크 트래픽)입니다.
  - id: u3-03-p05-q04
    kind: choice
    difficulty: medium
    prompt: 브로드캐스트 트래픽이 지나치게 많아질 때 생길 수 있는 영향은 무엇인가요?
    choices:
    - id: a
      text: 모든 유니캐스트 통신이 반드시 즉시 중단된다
      feedback: 다시 본문을 확인해 보세요. 모든 유니캐스트 통신이 반드시 즉시 중단된다.
    - id: b
      text: MAC 주소가 자동으로 IP 주소로 바뀐다
      feedback: 다시 본문을 확인해 보세요. MAC 주소가 자동으로 IP 주소로 바뀐다.
    - id: c
      text: Ethernet 프레임 크기 한계가 사라진다
      feedback: 다시 본문을 확인해 보세요. Ethernet 프레임 크기 한계가 사라진다.
    - id: d
      text: 링크 대역폭과 장치 처리 자원을 차지해 다른 통신에 지연을 줄 수 있다
      feedback: 맞아요. 링크 대역폭과 장치 처리 자원을 차지해 다른 통신에 지연을 줄 수 있다입니다.
    - id: e
      text: 라우터가 더 많은 링크를 자동으로 만든다
      feedback: 다시 본문을 확인해 보세요. 라우터가 더 많은 링크를 자동으로 만든다.
    answer: d
  question_placements:
  - question_id: u3-03-p05-q01
    after_paragraph: 1
  - question_id: u3-03-p05-q05
    after_paragraph: 3
  animations:
  - file: l10-broadcast-uses-links.svg
    title: "방송이 잦으면 자원이 줄어든다"
    alt: "스위치 A·B·C와 PC 1~6이 이어진 망에서 PC 4가 PC 5에게 파란 데이터를 계속 보냅니다. PC 1의 주황 방송이 모든 링크를 타고 모든 PC로 퍼지고, 방송이 잦아지자 왼쪽 위의 링크 대역폭·장치 처리 막대에서 주황 부분이 커지며 파란 데이터가 느려집니다. 마지막에 방송이 줄자 막대도 줄어듭니다."
    caption: "방송 하나도 여러 링크와 장치의 자원을 씁니다. 방송량이 커지면 지연이나 성능 저하가 생길 수 있으니 필요할 때만 보내고 범위를 적절히 나눕니다."
- terms:
  - L3 (Layer 3)
  - L3 경계 (L3 boundary)
  - 라우팅 (Routing)
  - LAN 구역
  animations:
  - file: l10-l3-boundary-blocks-broadcast.svg
    title: 라우터는 L2 브로드캐스트를 전달하지 않는다
    alt: 서로 다른 IP 네트워크 사이에 있는 라우터가 왼쪽 네트워크에서 온 L2 브로드캐스트 프레임을 오른쪽으로 전달하지 않는 장면입니다.
    caption: Ethernet 브로드캐스트 프레임은 라우터를 지나 다른 IP 네트워크로 전달되지 않습니다.
  questions:
  - id: u3-03-p06-q01
    kind: choice
    difficulty: easy
    prompt: 아파트 안내 방송을 동별로 나누면 한 동의 방송은 다른 동에도 자동으로 울릴까요?
    choices:
    - id: a
      text: 아니요, 방송 구역이 나뉘면 다른 동에 자동으로 울리지 않는다
      feedback: 맞아요. 아니요, 방송 구역이 나뉘면 다른 동에 자동으로 울리지 않는다.
    - id: b
      text: 네, 모든 건물에 항상 울린다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 네, 인터넷 전체에 울린다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 아니요, 방송은 한 사람만 듣는다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 동이 달라도 케이블 색이 같으면 울린다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: a
  - id: u3-03-p06-q05
    kind: choice
    difficulty: easy
    prompt: 브로드캐스트 구역을 더 작게 나누면 운영자가 추가로 감당할 일은 무엇인가요?
    choices:
    - id: a
      text: 추가 구성과 관리
      feedback: 맞아요. 추가 구성과 관리.
    - id: b
      text: 컴퓨터 화면 교체
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: MAC 주소 길이 변경
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 모든 케이블 교체
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: IP 주소 삭제
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: a
  - id: u3-03-p06-q02
    kind: choice
    difficulty: medium
    prompt: 브로드캐스트가 L3 경계를 넘어야 할 때 사용할 수 있는 별도 기능의 예는 무엇인가요?
    choices:
    - id: a
      text: Unicast flooding
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: Link up LED
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: Jumbo Frame
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: DHCP relay
      feedback: 맞아요. DHCP relay.
    - id: e
      text: MAC address table aging
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p06-q04
    kind: choice
    difficulty: medium
    prompt: L3 경계에 대한 정확한 설명은 무엇인가요?
    choices:
    - id: a
      text: 일반 Ethernet 브로드캐스트는 다른 IP 네트워크로 그대로 가지 않지만, 모든 IP·멀티캐스트 트래픽이 똑같이 막힌다는 뜻은 아니다
      feedback: 맞아요. 일반 Ethernet 브로드캐스트는 다른 IP 네트워크로 그대로 가지 않지만, 모든 IP·멀티캐스트 트래픽이 똑같이 막힌다는 뜻은 아니다.
    - id: b
      text: 모든 IP 패킷을 항상 차단한다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 모든 멀티캐스트와 유니캐스트를 차단한다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 라우터가 모든 Ethernet 방송을 전달한다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 브로드캐스트 MAC을 IP 주소로 바꾼다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: a
  question_placements:
  - question_id: u3-03-p06-q01
    after_paragraph: 1
  - question_id: u3-03-p06-q05
    after_paragraph: 5
- terms:
  - MAC 주소
  - IP 주소
  questions:
  - id: u3-03-p07-q01
    kind: choice
    difficulty: easy
    prompt: 같은 링크에서 Ethernet 프레임이 전달될 대상을 찾을 때 사용하는 주소는 무엇인가요?
    choices:
    - id: a
      text: DNS 이름
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: IP 주소
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: MAC 주소
      feedback: 맞아요. MAC 주소.
    - id: d
      text: 웹페이지 주소
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: TCP 포트 번호
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: c
  - id: u3-03-p07-q05
    kind: choice
    difficulty: easy
    prompt: 라우터를 지난 뒤 다음 링크에서 새로 만들어지는 것은 무엇인가요?
    choices:
    - id: a
      text: IP 주소
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: 원래 보낸 파일
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: Ethernet 프레임과 구간별 MAC 주소
      feedback: 맞아요. Ethernet 프레임과 구간별 MAC 주소.
    - id: d
      text: 목적지 네트워크
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: TCP 연결의 의미
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: c
  - id: u3-03-p07-q02
    kind: choice
    difficulty: medium
    prompt: LAN과 WAN을 물리 네트워크와 논리 네트워크에 대응시키는 그림은 어떻게 이해해야 하나요?
    choices:
    - id: a
      text: 처음 구조를 그리는 데 도움이 되는 요령이지 엄밀한 정의는 아니다
      feedback: 맞아요. 처음 구조를 그리는 데 도움이 되는 요령이지 엄밀한 정의는 아니다.
    - id: b
      text: 두 이름은 프레임과 패킷의 크기를 뜻한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: LAN에는 IP를 쓸 수 없고 WAN에만 쓸 수 있다는 뜻이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: WAN은 장비 없이 소프트웨어만 있다는 의미다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: LAN은 언제나 물리적이고 WAN은 언제나 논리적이라는 정의다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: a
  - id: u3-03-p07-q03
    kind: short
    prompt: PC에서 서버로 가는 패킷이 라우터를 지난 뒤 다음 링크에 맞게 프레임을 새로 만들 때, 일반적으로 유지되는 주소와 링크에 맞게 바뀌는 주소는 각각 무엇인가요? IP, MAC 순서로 답하세요.
    answers:
    - IP, MAC
    - IP address, MAC address
    - IP 주소, MAC 주소
    - IP는 유지되고 MAC은 바뀜
    - IP는 그대로이고 MAC은 바뀜
    feedback: 정답은 IP 주소는 보통 유지되고 MAC 주소는 다음 링크에 맞게 바뀐다는 것입니다. NAT 같은 기능이 있으면 IP 주소도 바뀔 수 있습니다.
  question_placements:
  - question_id: u3-03-p07-q01
    after_paragraph: 2
  - question_id: u3-03-p07-q05
    after_paragraph: 3
  animations:
  - file: l10-mac-changes-ip-stays.svg
    title: "MAC은 링크마다, IP는 끝까지"
    alt: "왼쪽에 물리 매체부터 HTTP까지 계층이 쌓여 있고, Ethernet 칸에는 목적지 MAC, IP 칸에는 목적지 IP가 표시됩니다. 오른쪽에서 PC가 라우터를 거쳐 서버로 보낼 때, 링크 1의 프레임은 목적지 MAC이 라우터이고 링크 2의 새 프레임은 목적지 MAC이 서버로 바뀌지만 목적지 IP는 두 프레임 모두 서버입니다. 마지막에 LAN=물리, WAN=논리라는 그림은 외우기 요령일 뿐이라는 안내가 나옵니다."
    caption: "L2 Ethernet은 같은 링크에서 목적지 MAC을, L3 IP는 네트워크 사이에서 목적지 IP를 봅니다. 라우터를 지나면 프레임과 MAC은 새로 바뀌고 IP는 보통 그대로입니다."
- terms:
  - 논리적 (Logical)
  questions:
  - id: u3-03-p08-q01
    kind: choice
    difficulty: easy
    prompt: 마우스 포인터는 책상 위에 작은 화살표 부품으로 놓여 있나요?
    choices:
    - id: a
      text: 아니요, 포인터는 화면에 그려지는 표시입니다
      feedback: 맞아요. 포인터는 화면에 표시되며 책상 위의 물체가 아닙니다.
    - id: b
      text: 네, 실제 화살표 부품이 책상 위에 놓여 있습니다
      feedback: 포인터는 책상 위에 놓인 물체가 아닙니다.
    - id: c
      text: 네, 포인터는 키보드 안의 부품입니다
      feedback: 포인터는 키보드 안의 부품이 아닙니다.
    - id: d
      text: 네, 포인터는 마우스 케이블에 인쇄된 기호입니다
      feedback: 포인터는 케이블에 인쇄된 기호가 아닙니다.
    - id: e
      text: 네, 포인터는 모니터 바깥에 붙은 스티커입니다
      feedback: 포인터는 화면에 그려지는 표시입니다.
    answer: a
  - id: u3-03-p08-q05
    kind: choice
    difficulty: easy
    prompt: “논리적 네트워크”라고 해도 실제 인터넷에서 그대로 쓰이는 것은 무엇인가요?
    choices:
    - id: a
      text: 광섬유·케이블·라우터 같은 물리 기반
      feedback: 맞아요. 광섬유·케이블·라우터 같은 물리 기반.
    - id: b
      text: 인터넷 주소
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 네트워크 규칙
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 연결된 장치
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 전송되는 데이터
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: a
  - id: u3-03-p08-q02
    kind: choice
    difficulty: medium
    prompt: 네트워크 그림에서 인터넷을 구름으로 표현할 때 주로 뜻하는 것은 무엇인가요?
    choices:
    - id: a
      text: 모든 데이터가 무선 구간만 통과한다는 뜻
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: IP 네트워크가 프레임을 사용하지 않는다는 뜻
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: 세부 물리 경로를 펼치지 않고 그 너머 네트워크와 통신한다는 표현
      feedback: 맞아요. 세부 물리 경로를 펼치지 않고 그 너머 네트워크와 통신한다는 표현.
    - id: d
      text: 인터넷이 날씨에 따라 통신한다는 뜻
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: 인터넷에는 물리 장비와 케이블이 없다는 사실
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: c
  question_placements:
  - question_id: u3-03-p08-q01
    after_paragraph: 1
  - question_id: u3-03-p08-q05
    after_paragraph: 4
  animations:
  - file: l10-cloud-over-cables.svg
    title: "포인터와 구름: 논리적이라는 말"
    alt: "왼쪽 모니터에서 마우스를 움직이면 화면의 포인터가 따라 움직이지만 책상 위에는 화살표가 없고, OS가 위치를 기억해 그린다는 표시가 붙습니다. 오른쪽에서는 PC와 서버 사이가 인터넷 구름으로 그려졌다가, 구름이 흐려지며 광섬유·해저 케이블·무선 구간과 라우터가 드러나고, 그 장비들 위로 PC에서 서버까지 가는 파란 경로가 표시되며 그 위의 주소·경로를 보는 관점이라는 문구가 나옵니다."
    caption: "IP 네트워크는 물리 링크 위에서 주소와 규칙으로 구성된 연결을 보는 추상화입니다. 논리적이라는 말은 장비가 없다는 뜻이 아닙니다."
- terms:
  - 가상화 (Virtualization)
  - 가상 머신 (Virtual Machine)
  - 가상 네트워크 인터페이스 (Virtual network interface)
  questions:
  - id: u3-03-p09-q05
    kind: choice
    difficulty: easy
    prompt: 실제 서버 한 대에 가상 머신을 만들면, 소프트웨어는 어떤 자원을 나누어 제공하나요?
    choices:
    - id: a
      text: CPU 시간·메모리·저장 공간과 네트워크 인터페이스
      feedback: 맞아요. CPU 시간·메모리·저장 공간과 네트워크 인터페이스.
    - id: b
      text: 화면 픽셀만
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 모니터 전원만
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 브로드캐스트 주소
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 키보드의 키만
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: a
  - id: u3-03-p09-q02
    kind: choice
    difficulty: medium
    prompt: “논리적” 또는 “가상” 네트워크라는 말의 의미로 가장 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 물리 장비가 전혀 없어서 실제 통신을 하지 않는다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: 모든 VM이 서로 같은 네트워크 주소를 써야 한다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: c
      text: LAN은 반드시 가상이고 WAN은 반드시 물리적이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: 물리 자원 위에 다른 규칙과 경계를 만들어 표현하고 관리한다
      feedback: 맞아요. 물리 자원 위에 다른 규칙과 경계를 만들어 표현하고 관리한다.
    - id: e
      text: 가짜 주소만 쓰고 실제 네트워크와 연결되지 않는다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: d
  - id: u3-03-p09-q04
    kind: choice
    difficulty: medium
    prompt: 가상화가 한 대의 실제 서버에서 여러 가상 머신을 제공할 수 있게 하는 방식으로 가장 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 서버 안에 같은 수의 물리 컴퓨터를 추가 설치한다
      feedback: 다시 본문을 확인해 보세요. 서버 안에 같은 수의 물리 컴퓨터를 추가 설치한다.
    - id: b
      text: 소프트웨어가 실제 컴퓨터 자원을 나누어 각 가상 머신에 제공한다
      feedback: 맞아요. 소프트웨어가 실제 컴퓨터 자원을 나누어 각 가상 머신에 제공한다입니다.
    - id: c
      text: 각 가상 머신이 별도의 인터넷을 물리적으로 만든다
      feedback: 다시 본문을 확인해 보세요. 각 가상 머신이 별도의 인터넷을 물리적으로 만든다.
    - id: d
      text: MAC 주소를 모두 같게 설정한다
      feedback: 다시 본문을 확인해 보세요. MAC 주소를 모두 같게 설정한다.
    - id: e
      text: 가상 머신은 네트워크 인터페이스를 사용할 수 없다
      feedback: 다시 본문을 확인해 보세요. 가상 머신은 네트워크 인터페이스를 사용할 수 없다.
    answer: b
  question_placements:
  - question_id: u3-03-p09-q05
    after_paragraph: 3
  animations:
  - file: l10-one-server-many-vms.svg
    title: "한 대를 여러 대처럼: 가상화"
    alt: "왼쪽에 CPU 시간·메모리·저장 공간·네트워크를 가진 실제 서버 한 대가 있고, 그 위에 가상화 소프트웨어가 놓인 뒤 자원이 세 색으로 나뉘어 VM 1~3에 배정됩니다. 오른쪽에서는 PC 네 대가 실제 스위치 하나에 케이블로 연결된 채 가상 네트워크 A와 B로 묶이고, 마지막에 실제 장비 위의 다른 규칙·경계라는 표시가 나옵니다."
    caption: "가상화는 소프트웨어가 실제 자원을 나눠 여러 대처럼 쓰게 하는 기술입니다. 가상 네트워크도 실제 케이블과 스위치 위에서 동작하며, 다른 규칙과 경계로 관리합니다."
- terms:
  - LAN (Local Area Network)
  - WAN (Wide Area Network)
  questions:
  - id: u3-03-p10-q01
    kind: choice
    difficulty: easy
    prompt: 건물 안내 방송 비유에서 라우터 경계는 무엇을 막나요?
    choices:
    - id: a
      text: 한 구역의 방송이 다른 네트워크까지 그대로 퍼지는 것
      feedback: 맞아요. 한 구역의 방송이 다른 네트워크까지 그대로 퍼지는 것.
    - id: b
      text: 한 PC에서 다른 PC로 가는 Unicast
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: c
      text: 스위치가 출발지 MAC을 배우는 것
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: LAN 케이블이 꽂히는 것
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 모든 IP 통신을 차단하는 것
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: a
  - id: u3-03-p10-q05
    kind: choice
    difficulty: easy
    prompt: WAN도 실제 케이블·광섬유·무선 장비 위에서 동작하나요?
    choices:
    - id: a
      text: 아니요, WAN은 실제 장비가 필요 없다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: b
      text: 네, WAN도 실제 전송 장비와 링크를 사용한다
      feedback: 맞아요. WAN도 실제 전송 장비와 링크를 사용합니다.
    - id: c
      text: 맞다. LAN에만 케이블이 있다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: d
      text: 아니다. WAN은 MAC 주소만 사용한다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    - id: e
      text: 맞다. WAN은 구름 그림 자체를 말한다
      feedback: 다시 생각해 보세요. 방금 읽은 예시를 떠올려 보세요.
    answer: b
  - id: u3-03-p10-q02
    kind: choice
    difficulty: medium
    prompt: LAN과 WAN에 관한 설명으로 정확한 것은 무엇인가요?
    choices:
    - id: a
      text: LAN은 반드시 물리 연결이고 WAN은 반드시 논리 연결이다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: b
      text: LAN도 논리적으로 나뉠 수 있고 WAN도 물리 장비 위에서 구현된다
      feedback: 맞아요. LAN도 논리적으로 나뉠 수 있고 WAN도 물리 장비 위에서 구현된다.
    - id: c
      text: LAN은 MAC 주소를 쓰고 WAN은 IP 주소를 쓰지 않는다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: d
      text: LAN과 WAN은 각각 하나의 고정 거리로만 구분된다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    - id: e
      text: WAN에는 케이블이나 라우터가 필요 없다
      feedback: 다시 확인해 보세요. 이 페이지에서 다룬 내용을 기준으로 생각해 보세요.
    answer: b
  - id: u3-03-p10-q03
    kind: short
    prompt: 제한된 지역보다 더 넓은 범위를 잇는 네트워크를 가리키는 영어 약어입니다. 무엇일까요?
    answers:
    - WAN
    - wide area network
    - 광역 네트워크
    - 광역 통신망
    feedback: 정답은 WAN(Wide Area Network)입니다.
  question_placements:
  - question_id: u3-03-p10-q01
    after_paragraph: 2
  - question_id: u3-03-p10-q05
    after_paragraph: 4
  animations:
  - file: l10-lan-wan-summary.svg
    title: "LAN·WAN 한 장으로 정리"
    alt: "왼쪽 구역의 PC는 케이블로, 노트북은 Wi-Fi로 스위치에 연결되어 있고 그 링크 위로 파란 프레임이 오갑니다. 주황 방송은 왼쪽 구역 안에만 퍼지고 라우터에서 멈추며, 민트 IP 패킷은 라우터 두 개를 지나 오른쪽 구역의 PC까지 갑니다. 이어서 두 구역이 LAN, 전체가 WAN으로 묶이고, 마지막에 오른쪽 LAN의 VLAN 구분과 WAN의 광섬유·무선 구간, 범위·기술·운영 주체라는 판단 기준이 나타납니다."
    caption: "링크 위로 MAC 프레임이 오가고, 그 위에서 IP 패킷이 네트워크 사이를 이동합니다. LAN과 WAN은 물리·논리만으로 나뉘지 않으니 범위·기술·운영 주체 같은 문맥으로 판단합니다."
animations_dir: units/03-layer2-switching/lessons/03-lan과-wan의-경계-그리고-broadcast/assets/animations
---
네트워크에서 “모두에게 알려야 하는 말”은 어떻게 전달될까? 그리고 그 말은 어디까지 퍼져도 괜찮을까? 아파트 안내 방송과 택배 송장, 손에 잡히지 않는 마우스 포인터를 떠올리며 Broadcast와 LAN·WAN의 관계를 살펴보자.

## Broadcast · 모두에게 보내기
<!-- learn-page-id: broadcast-unicast-definition -->

친구 한 명에게 쪽지를 건네는 것과 교실 전체에 안내 방송을 하는 것을 비교해 보자. 한 사람을 지정해 보내는 통신이 Unicast이고, 같은 범위에 있는 여러 장치에게 한꺼번에 알리는 통신이 Broadcast다.

Broadcast는 “누군지 모르겠으니 이 범위 안의 모두에게 물어볼게”처럼 쓸모가 있다. 하지만 안내 방송이 잦으면 자기와 상관없는 학생도 듣느라 수업을 멈춰야 한다. 네트워크의 장치도 Broadcast를 받으면 내용을 확인해야 하므로, 필요하지 않은 방송이 많아질수록 다른 통신이 쓸 자원과 장치의 처리 시간이 줄어든다.

여기서 ‘모두’는 전 세계 모든 컴퓨터가 아니라, 한 교실처럼 방송이 닿는 정해진 구역 안의 장치들입니다. 브로드캐스트가 퍼지는 이 한 구역을 브로드캐스트 도메인(Broadcast Domain)이라고 합니다. 일반적인 스위치 구성에서는 같은 VLAN이 하나의 브로드캐스트 도메인을 이룹니다. 앞 Lesson에서 VLAN으로 포트를 나누었던 이유도 이 범위를 구분하기 위해서입니다. 라우터는 보통 Ethernet 브로드캐스트를 다른 IP 네트워크로 그대로 넘기지 않으므로, 라우터가 브로드캐스트 범위를 나누는 경계가 됩니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Broadcast는 같은 브로드캐스트 도메인 안의 여러 장치에게 동시에 알린다.
- **적용하기 (Apply):** 한 장치 대상 Unicast와 범위 내 전체 대상 Broadcast를 구분한다.
- **찾아보기 (Lookup):** 네트워크 구성도에서 같은 VLAN의 브로드캐스트가 어디까지 퍼지는지 따라가 본다.

## 브로드캐스트 도메인
<!-- learn-page-id: broadcast-domain-definition -->

아파트 관리실에서 “입주민 여러분, 정전 점검이 있습니다”라고 방송하면 그 방송은 한 집에만 전달되지 않는다. 같은 방송 장비에 연결된 세대 모두가 들을 수 있다. 이때 방송이 닿는 구역을 브로드캐스트 도메인이라고 생각하면 된다.

한 동 전체가 한 구역일 수도 있고, 관리 방식에 따라 여러 구역으로 나뉠 수도 있다. 다만 관리실만 방송하는 아파트와 달리 네트워크에서는 구역 안의 컴퓨터나 프린터도 브로드캐스트를 보낼 수 있다. 스위치는 같은 VLAN 안에서만 그 방송을 퍼뜨리고, 다른 VLAN이나 라우터 너머로는 전달하지 않는다. 그래서 VLAN과 라우터가 브로드캐스트 도메인의 경계가 된다.

네트워크에서도 브로드캐스트는 필요한 기능이지만, 스위치가 받은 방송을 같은 VLAN의 여러 포트로 전달하면 그 범위의 장치들이 모두 확인하게 된다. 그래서 “방송을 보낼 수 있나?”만큼 “어느 구역까지 들리게 할까?”가 중요하다. Ethernet의 특별한 브로드캐스트 MAC 주소는 48비트가 모두 1이며, 다음 페이지에서 실제 표기를 살펴본다. IP 브로드캐스트 주소는 주소 범위와 함께 뒤에서 따로 살펴본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Broadcast domain은 L2 브로드캐스트가 전달되는 범위다.
- **적용하기 (Apply):** 라우터 또는 VLAN 경계가 방송 구역을 어떻게 나누는지 도식으로 표시한다.
- **찾아보기 (Lookup):** 스위치 설정에서 포트별 VLAN을 찾아보고, 어느 포트끼리 같은 브로드캐스트 도메인에 속하는지 확인한다.

## 브로드캐스트 MAC 주소

택배 상자에 받는 사람 주소가 적혀 있으면 특정 집으로 간다. 그런데 송장에 “이 구역의 모든 집”이라고 표시되어 있다면 배달 방식이 달라질 것이다. Ethernet 프레임에도 받는 곳을 적는 목적지 MAC 주소가 있고, 그 자리에 브로드캐스트 주소를 쓰면 “이 브로드캐스트 도메인 안의 모두가 확인해 주세요”라는 뜻이 된다.



그 주소를 2진수로 보면 48개의 자리가 전부 1이다.

MAC 주소를 보기 좋게 16진수 여섯 칸으로 적으므로 `FF:FF:FF:FF:FF:FF`가 된다. F 하나는 2진수 `1111`, FF는 `11111111`이다. 즉 F 두 개가 8비트 한 칸을 채우고, 그런 칸 여섯 개가 모여 48비트 전체를 채운다. 외울 때는 “여섯 칸의 FF, 받는 사람은 구역 안의 모두”라고 연결하면 된다. 이 값은 NIC 한 대에 배정된 개별 주소가 아니라 Ethernet 프레임의 목적지 자리에 쓰는 특별한 주소다. 모든 비트가 1인 값이 언제나 Broadcast라는 뜻은 아니며, 여기서는 Ethernet 목적지 MAC 주소라는 자리와 문맥이 함께 특별한 의미를 만든다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** `FF:FF:FF:FF:FF:FF`는 Ethernet의 브로드캐스트 목적지 MAC 주소다.
- **적용하기 (Apply):** 48개의 1비트가 `FF` 여섯 묶음(총 F 열두 글자)으로 표기되는 이유를 설명한다.
- **찾아보기 (Lookup):** 나중에 패킷 캡처 화면에서 목적지 MAC 주소가 `FF:FF:FF:FF:FF:FF`인 프레임을 찾아본다.

## 스위치에서 전파되는 과정

L2에서 주고받는 데이터 단위는 프레임이다. 프레임은 택배 상자, 헤더(Header)는 겉면의 송장이라고 떠올려 보자. 송장에는 보내는 곳과 받는 곳이 있어야 하듯 프레임 헤더에도 출발지 MAC 주소와 목적지 MAC 주소가 들어간다. Ethernet MAC 주소 하나는 48비트다. 헤더에는 이 밖에도 안에 담긴 데이터의 종류를 나타내는 Type 같은 정보가 있지만, 브로드캐스트를 퍼뜨릴 때 스위치는 목적지 MAC 주소를 기준으로 전달한다.



PC 1이 `FF:FF:FF:FF:FF:FF`를 목적지로 적은 프레임을 액세스 스위치 A에 보냈다고 하자. 스위치는 그 프레임이 속한 VLAN 안에서, 프레임이 들어온 포트를 제외한 나머지 활성 포트들로 복사해 보낸다. VLAN이 다른 포트로는 보내지 않는다. 분배 스위치 C와 반대편 액세스 스위치 B도 프레임을 받으면 같은 규칙을 적용한다. 각 스위치가 받은 포트로 되돌려 보내지 않고 같은 VLAN 안으로 전달하므로, 연결된 여러 스위치를 따라 방송이 퍼진다.

스위치가 내용을 새로 만들어 내는 것이 아니라, 목적지 주소가 “이 구역의 모두”라고 지정했기 때문에 전달한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 스위치는 들어온 브로드캐스트 프레임을 같은 VLAN의 다른 포트로 전달한다.
- **적용하기 (Apply):** PC 한 대의 브로드캐스트가 각 스위치를 거쳐 어디에 닿는지 따라간다.
- **찾아보기 (Lookup):** 관리형 스위치의 VLAN 설정에서 브로드캐스트가 전달될 포트 범위를 확인한다.

## 트래픽이 불어나는 문제

교실 한쪽에서 안내 방송을 한 번 하면 모두가 듣는다.

방송이 계속 반복되면 학생마다 듣는 시간은 짧아도 교실 전체의 시간이 조금씩 쓰인다. 네트워크에서 주고받는 데이터 흐름을 트래픽(Traffic)이라고 한다. PC 1의 방송 하나도 스위치들을 따라 여러 연결 구간(링크)으로 복사되어 전달되면서 장치의 처리 시간과 링크가 데이터를 나르는 통로의 폭(대역폭)을 사용한다. PC 4가 PC 5에게 필요한 데이터를 보내는 중에도 같은 구간을 지나는 장치들은 방송 프레임을 받고 확인해야 한다.

Broadcast가 곧바로 모든 Unicast를 멈춘다는 뜻은 아니지만, 방송량이 커지면 링크 대역폭과 장치의 처리 자원을 함께 차지해 지연이나 성능 저하를 일으킬 수 있다.

그래서 필요한 발견·안내에는 Broadcast를 쓰되, 불필요하게 자주 보내지 않고 범위를 적절히 나누는 것이 운영의 요령이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 브로드캐스트가 많으면 여러 장치와 링크가 처리해야 할 트래픽이 늘어난다.
- **적용하기 (Apply):** 브로드캐스트 비율이 높을 때 단말 부하와 링크 점유를 함께 살핀다.
- **찾아보기 (Lookup):** 스위치 설명서에서 포트별 브로드캐스트 프레임 수를 보여 주는 통계 항목을 찾아본다.

## L3 경계와 브로드캐스트

아파트 방송을 동별로 나눠 한 동의 안내가 다른 동에 자동으로 울리지 않게 하는 모습을 생각해 보자.

네트워크에서도 라우터는 한 네트워크에서 다른 네트워크로 데이터를 전달하지만, 일반적인 설정에서는 Ethernet 브로드캐스트 프레임을 다른 쪽에 퍼뜨리지 않는다. 라우터는 목적지가 정해진 일반 통신은 목적지 IP 주소를 보고 전달하지만, 브로드캐스트는 “이 구역의 모두”를 대상으로 하기 때문이다. 예를 들어 PC 1~3이 있는 쪽에서 나온 방송은 그 구역에 머물고, PC 4~6이 있는 다른 쪽에는 닿지 않게 설계할 수 있다.

이 경계는 방송의 범위를 제한해 불필요한 영향을 줄인다.

브로드캐스트가 라우터 경계에서 멈추면 한쪽 네트워크의 방송이 다른 쪽 장치까지 불필요하게 퍼지는 일을 줄일 수 있다. IP 주소 범위에서 브로드캐스트를 정하는 방법은 뒤의 IP 주소 단원에서 이어서 배운다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 일반 Ethernet 브로드캐스트는 라우터를 넘어 다른 IP 네트워크로 전달되지 않는다.
- **적용하기 (Apply):** 라우터 양쪽 LAN에서 방송이 각각 머무는 범위를 설명한다.
- **찾아보기 (Lookup):** 뒤의 IP 주소 단원에서 네트워크 주소 범위와 그 안의 브로드캐스트 주소가 어떻게 연결되는지 확인한다.

## LAN과 WAN을 보는 관점

LAN(Local Area Network)은 집·학교·사무실처럼 제한된 장소 안에서 기기들을 연결한 네트워크를 가리킨다. WAN(Wide Area Network)은 더 넓은 범위를 연결하며, 서로 떨어진 사무실이나 여러 LAN을 이어 주는 네트워크가 대표적인 예다. 이 말들은 네트워크가 어느 범위와 연결을 다루는지 설명한다.

LAN과 WAN은 각각 하나의 케이블이나 하나의 통신 규칙 이름이 아니다. LAN 안에서도 Ethernet과 무선 연결을 쓸 수 있고, WAN은 여러 종류의 통신망과 장비를 통해 구성될 수 있다.

앞에서 본 계층과 연결하면, Ethernet은 같은 링크에서 프레임을 전달할 때 목적지 MAC 주소를 보고, IP는 네트워크 사이에서 패킷을 전달할 때 IP 주소를 본다. 라우터를 지나도 보통 출발지·목적지 IP는 유지되지만, 각 링크에서 프레임은 새로 만들어지고 MAC 주소는 다음 구간의 이웃에 맞게 달라진다. MAC은 가까운 링크에서, IP는 목적지 네트워크까지 가는 경로에서 쓰인다고 기억하자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** LAN은 제한된 장소의 네트워크이고, WAN은 더 넓은 범위의 네트워크를 연결한다.
- **적용하기 (Apply):** 집 안 LAN에서 시작해 WAN을 거쳐 다른 지역의 LAN으로 가는 경로를 그려 본다.
- **찾아보기 (Lookup):** 그 경로에서 각 링크의 MAC 주소와 목적지 IP 주소가 맡는 일을 Ethernet·IP Page에서 다시 확인한다.

## 물리 네트워크와 논리 네트워크

물리 네트워크는 실제로 설치된 Ethernet 케이블·광섬유·무선 연결과 스위치·라우터 같은 장비가 이어진 모습이다. 논리 네트워크는 그 장비 위에서 주소와 설정 규칙으로 묶어 표현한 연결이다.

앞에서 본 VLAN이 한 예다. 한 대의 물리 스위치에 연결된 포트들을 설정으로 나누면, 같은 장비를 쓰면서도 서로 다른 LAN처럼 통신하는 논리적 구역을 만들 수 있다.

네트워크 그림에서 인터넷이나 통신사 망을 구름으로 표시하기도 한다. 구름은 그 안에 실제 케이블이나 장비가 없다는 뜻이 아니다. 해저 케이블·광섬유·무선 구간과 라우터가 이어진 복잡한 실제 경로를 생략하고, 그 너머의 네트워크와 연결된다는 점만 간단히 나타낸다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 물리 네트워크는 실제 연결이고, 논리 네트워크는 그 위에서 주소와 설정으로 나눈 연결이다.
- **적용하기 (Apply):** 구름으로 표시된 네트워크 경로에서 생략된 실제 장비와 케이블의 예를 든다.
- **찾아보기 (Lookup):** 네트워크 구성도에서 VLAN으로 물리 스위치를 나눈 사례를 찾아, 물리 연결과 논리 구역을 구별한다.

## 가상 네트워크라는 표현

앞 페이지에서는 물리 스위치의 포트를 설정으로 나누는 VLAN을 보았다. 가상 네트워크도 비슷하게 실제 케이블과 장비 위에 소프트웨어로 만든 논리적 연결이다.

화면의 마우스 포인터는 움직이지만, 화면 안에서 실제 화살표가 움직이는 것은 아니다. 컴퓨터가 위치를 기억해 화면에 그린 표시다. 네트워크 그림의 논리적 연결도 실제 케이블을 그대로 그리는 대신, 주소와 설정으로 연결을 나타낸다.

예를 들어 실제 서버 컴퓨터 한 대에서 여러 대의 가상 머신(Virtual Machine, VM)을 실행할 수 있다. 가상화(Virtualization)는 소프트웨어가 컴퓨터 자원을 나누어 각 가상 머신에 별도의 컴퓨터처럼 쓸 환경을 제공하는 기술이다. 각 가상 머신에는 네트워크에 연결되는 가상 네트워크 인터페이스(가상 NIC)가 생길 수 있다.

그래서 한 대의 서버 안에 있어도 네트워크에서는 여러 호스트가 연결된 것처럼 통신할 수 있다. “가상”은 가짜라는 뜻이 아니라 실제 장비 위에서 소프트웨어로 구성했다는 뜻이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 가상 네트워크는 실제 장비 위에서 소프트웨어로 구성한 논리적 연결이다.
- **적용하기 (Apply):** 한 서버에서 실행되는 가상 머신들이 각자 네트워크에 연결되려면 어떤 가상 인터페이스가 필요한지 설명한다.
- **찾아보기 (Lookup):** 내 컴퓨터에서 가상 머신 프로그램이나 VPN을 사용할 때 네트워크 설정에 추가되는 가상 어댑터 사례를 찾아본다.

## LAN·WAN의 구별 정리

이번 Lesson에서 배운 주소와 경계의 역할을 표로 정리해 보자.

| 구분 | 무엇을 설명하나? | 기억할 점 |
|---|---|---|
| Ethernet 프레임과 MAC | 같은 링크에서 프레임을 전달할 때 쓰는 주소 | 목적지가 `FF:FF:FF:FF:FF:FF`이면 스위치가 같은 브로드캐스트 도메인 안으로 퍼뜨린다. |
| IP 패킷과 라우터 | 서로 다른 네트워크 사이로 데이터를 전달하는 일 | 라우터는 일반적인 설정에서 Ethernet 브로드캐스트 프레임을 다른 네트워크로 넘기지 않는다. |
| LAN과 WAN | 네트워크가 연결하는 범위 | LAN은 보통 제한된 장소의 네트워크, WAN은 더 넓은 범위의 네트워크를 연결한다. 둘을 물리와 논리의 구분으로 보면 안 된다. |

물리 네트워크는 실제 케이블·무선 연결·장비를 말하고, 논리 네트워크는 그 위에서 주소와 설정으로 나눈 연결을 말한다. 예를 들어 LAN 안에서도 VLAN으로 구역을 나눌 수 있고, WAN도 실제 광섬유와 라우터 위에서 동작한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 스위치는 같은 브로드캐스트 도메인 안에 방송을 퍼뜨리고, 라우터는 그 L2 방송이 다른 네트워크로 넘어가는 경계를 만든다.
- **적용하기 (Apply):** 네트워크 그림에서 링크·브로드캐스트 도메인·라우터·LAN/WAN 범위를 각각 표시한다.
- **찾아보기 (Lookup):** 다음 IP 주소 단원에서 IP 주소로 나눈 네트워크 구역인 서브넷과 브로드캐스트 주소의 관계를 확인한다.
