---
id: advanced-nat-mapping-filtering
title: '포트를 안 열어도 화상회의가 되는 이유: NAT 통과'
source_lesson_ids:
- u8-advanced-12-full-cone-방식과-내부-네트워크-접속-문제
- u8-advanced-13-restricted-cone-방식
- u8-advanced-14-port-restricted-cone-방식
- u8-advanced-10-공유기-작동원리-및-개요
- u8-advanced-11-symmetric-nat-방식
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-12.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-13.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-14.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-10.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-11.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/03-2.md#p158-b18
- https://www.rfc-editor.org/rfc/rfc4787.html
- https://www.rfc-editor.org/rfc/rfc5128.html
- https://www.rfc-editor.org/rfc/rfc8489.html
- https://www.rfc-editor.org/rfc/rfc8656.html
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-12.md
page_metadata:
- page_id: advanced-nat-mapping-filtering-page-01
  illustrations:
  - file: assets/animations/u12-l05-p01-video-call-no-port.svg
    title: "포트를 안 열었는데 화상회의는?"
    alt: "박 팀장과 협력사가 모두 공유기 뒤에 있어도 둘 다 화상회의 서버로 먼저 연결하면 포트를 열지 않아도 영상과 음성이 오가고, 일부 앱은 서버 없이 직접 연결도 시도한다는 그림입니다."
    caption: "안쪽에서 바깥으로 먼저 나가는 연결에는 포트 개방이 필요 없습니다."
    after_paragraph: 0
  questions:
  - id: u12-l05-p01-q01
    kind: choice
    difficulty: easy
    prompt: P2P 통신에 대한 설명으로 알맞은 것은 무엇인가?
    choices:
    - id: a
      text: 두 기기가 서로 직접 데이터를 주고받는 방식
      feedback: 맞다. 소개 서버가 상대를 알려 주더라도 데이터는 직접 오갈 수 있다.
    - id: b
      text: 모든 데이터가 반드시 중앙 서버를 거치는 방식
      feedback: 그것은 중계 방식이다. P2P는 두 기기가 직접 주고받는다.
    - id: c
      text: 공유기가 두 기기의 데이터를 대신 전달해 주는 방식
      feedback: 공유기는 주소를 바꿔 전달할 뿐 데이터를 대신 만들거나 중계하지 않는다.
    - id: d
      text: NAT를 끄고 두 기기가 공인 주소만 쓰는 방식
      feedback: P2P도 NAT 뒤에서 시도하는 경우가 많다.
    - id: e
      text: 한쪽 기기가 서버 역할을 하고 다른 쪽이 접속만 하는 방식
      feedback: 양쪽이 대등하게 직접 통신하는 것이 P2P다.
    answer: a
    feedback: P2P는 두 피어가 직접 주고받는 방식이고, 소개 서버는 상대를 알려 주는 역할에 가깝다.
  - id: u12-l05-p01-q02
    kind: choice
    difficulty: medium
    prompt: 지우와 재택 중인 박 팀장의 PC를 원격 지원 앱으로 연결했다. 앱에 소개 서버가 있다면 모든 화면 데이터가 반드시 그 서버를 지날까?
    choices:
    - id: a
      text: 그렇다. 소개 서버가 모든 데이터를 중계한다
      feedback: 소개 서버가 항상 중계까지 하는 것은 아니다.
    - id: b
      text: 그렇다. NAT 뒤 기기는 서버를 거쳐야만 통신할 수 있다
      feedback: 홀 펀칭 같은 방법으로 직접 연결할 수도 있다.
    - id: c
      text: 아니다. 소개 서버가 없어도 상대의 바깥 주소를 미리 알 수 있기 때문이다
      feedback: 상대의 바깥 주소는 서버가 관찰해 알려 주어야 알 수 있다.
    - id: d
      text: 아니다. 데이터는 항상 통신사 장비를 통해 직접 전달된다
      feedback: 통신사 장비가 데이터를 직접 연결해 주지 않는다.
    - id: e
      text: 아니다. 소개 서버는 상대를 알려 줄 뿐 직접 경로면 지나지 않는다
      feedback: 맞다. 소개와 데이터 전달은 별개의 일이다.
    answer: e
    feedback: '🧩 쪼개기: ''상대를 소개하는 일''과 ''데이터를 나르는 일''을 나누면 서버가 꼭 데이터를 지나는 것은 아님을 알 수 있다.'
  question_placements:
  - question_id: u12-l05-p01-q01
    after_paragraph: 3
- page_id: advanced-nat-mapping-filtering-page-02
  illustrations:
  - file: assets/animations/u12-l05-p02-two-questions.svg
    title: "NAT에게 꼭 따로 물어야 할 두 가지"
    alt: "지우의 메모를 이름만 보고 판단한 것에서 매핑과 필터링을 따로 확인하는 것으로 고치고, 매핑은 External 칸, 필터링은 응답을 들여보내기 전의 조건이라는 두 질문을 보여 줍니다."
    caption: "NAT는 매핑과 필터링을 따로 확인합니다."
    after_paragraph: 0
  questions:
  - id: u12-l05-p02-q01
    kind: choice
    difficulty: easy
    prompt: NAT의 매핑과 필터링을 바르게 설명한 것은 무엇인가?
    choices:
    - id: a
      text: 매핑은 어떤 출발지의 패킷을 받을지를, 필터링은 바깥에 보이는 주소·포트를 정한다
      feedback: 두 개념을 서로 바꾸어 이해한 것이다.
    - id: b
      text: 매핑과 필터링은 방화벽 규칙을 부르는 두 가지 이름이다
      feedback: 둘 다 NAT 동작을 설명하는 기준이다.
    - id: c
      text: 매핑은 바깥에 보이는 주소·포트를, 필터링은 어떤 출발지의 패킷을 받을지를 정한다
      feedback: 맞다. 두 질문은 서로 독립적이다.
    - id: d
      text: 매핑은 TCP에만, 필터링은 UDP에만 적용된다
      feedback: 두 기준은 프로토콜별 구분이 아니다.
    - id: e
      text: 매핑은 공유기 안쪽에서, 필터링은 AI 서버에서 처리한다
      feedback: 둘 다 NAT 장비의 동작이다.
    answer: c
    feedback: 매핑은 바깥에 어떻게 보이는지, 필터링은 누구의 패킷을 받을지라는 서로 다른 질문이다.
  - id: u12-l05-p02-q02
    kind: choice
    difficulty: medium
    prompt: 지우의 메모에 "우리 공유기는 Port Restricted라서 화상회의가 안 될 거야"라고 적혀 있다. 이 메모를 고치려면 무엇을 따로 확인해야 할까?
    choices:
    - id: a
      text: 공유기의 제조사와 모델명이 무엇인지
      feedback: 모델명만으로는 동작을 알 수 없다.
    - id: b
      text: 바깥 포트가 상대마다 바뀌는지와 받는 출발지
      feedback: 맞다. 매핑과 필터링을 각각 확인해야 연결 가능성을 판단할 수 있다.
    - id: c
      text: AI 서버의 8080번 포트가 열려 있는지 여부
      feedback: 화상회의의 연결 가능성과는 다른 문제다.
    - id: d
      text: 공유기 WAN 주소가 공인 주소인지
      feedback: WAN 주소가 공인이어도 매핑과 필터링은 별개로 정해진다.
    - id: e
      text: UPnP가 꺼져 있는지
      feedback: UPnP 여부는 NAT의 매핑·필터링 동작을 대신 설명하지 못한다.
    answer: b
    feedback: '🗺️ 필요한 것만 남기기: 옛 유형 이름 대신 ''매핑''과 ''필터링'' 두 기준만 남기면 판단할 수 있다.'
  question_placements:
  - question_id: u12-l05-p02-q01
    after_paragraph: 3
- page_id: advanced-nat-mapping-filtering-page-03
  questions:
  - id: u12-l05-p03-q01
    kind: choice
    difficulty: easy
    prompt: 상대와 무관한 매핑(EIM)이란 무엇인가?
    choices:
    - id: a
      text: 상대마다 바깥 포트를 새로 정하는 매핑
      feedback: 그것은 상대에 따라 달라지는 매핑이다.
    - id: b
      text: 바깥에서 온 모든 패킷을 허용하는 필터링
      feedback: 허용 범위는 필터링의 문제이고 매핑과는 별개다.
    - id: c
      text: 안쪽 주소를 공인 주소로 영구히 고정하는 매핑
      feedback: 주소를 영구히 고정하는 것이 아니라 같은 바깥 endpoint를 재사용하는 동작이다.
    - id: d
      text: 상대가 바뀌어도 같은 바깥 주소·포트를 쓰는 매핑
      feedback: 맞다. 서버가 관찰한 바깥 주소를 다른 상대에게도 쓸 수 있다.
    - id: e
      text: TCP 연결이 끊기면 포트를 바로 반납하는 매핑
      feedback: 포트 반납 시점은 EIM의 정의가 아니다.
    answer: d
    feedback: EIM은 같은 내부 endpoint가 어느 상대와 통신하든 같은 바깥 endpoint를 쓰는 동작이다.
  - id: u12-l05-p03-q02
    kind: choice
    difficulty: medium
    prompt: 주소 확인 서버는 박 팀장 집 공유기를 `192.0.2.123:40001`로 봤는데, 협력사로 보낼 때는 `:40017`로 나간다. 어떤 매핑이며 직접 연결에 어떤 영향이 있을까?
    choices:
    - id: a
      text: 상대와 무관한 매핑이라 알려 준 주소가 그대로 맞아 연결이 쉽다
      feedback: 상대와 무관한 매핑이라면 포트가 같아야 한다. 이 경우 포트가 달라졌다.
    - id: b
      text: 필터링이 막은 것이라 포트 번호와는 무관하다
      feedback: 필터링이 아니라 매핑의 차이로 포트 번호가 달라졌다.
    - id: c
      text: UPnP 매핑이라서 항상 안정적으로 연결된다
      feedback: UPnP와 무관한 상황이다.
    - id: d
      text: 포트가 바뀐 것은 오류이므로 공유기를 교체해야 한다
      feedback: 상대에 따라 포트가 달라지는 것은 장비의 동작 방식 중 하나다.
    - id: e
      text: 상대에 따라 달라지는 매핑이라 알려 준 주소가 협력사에게 맞지 않는다
      feedback: 맞다. 상대마다 바깥 포트가 다르면 소개받은 주소로는 연결하기 어렵다.
    answer: e
    feedback: '🧩 쪼개기: 같은 통신을 ''서버에게 보일 때''와 ''협력사에게 보일 때''로 나누면 바깥 포트가 달라졌음이 보인다.'
  question_placements:
  - question_id: u12-l05-p03-q01
    after_paragraph: 3
  illustrations:
  - file: assets/animations/u12-l05-p03-mapping-by-peer.svg
    title: "상대가 바뀌면 바깥 포트도 바뀔까?"
    alt: "박 팀장 PC 192.168.0.20이 STUN 서버 203.0.113.60에는 192.0.2.123:40001로 보였지만 협력사에는 상대마다 다른 매핑이면 :40017로 보여 소개한 주소가 맞지 않는다는 비교입니다."
    caption: "소개 서버가 알려 준 주소가 맞으려면 매핑이 상대와 무관해야 합니다."
    after_paragraph: 0
- page_id: advanced-nat-mapping-filtering-page-04
  questions:
  - id: u12-l05-p04-q01
    kind: choice
    difficulty: easy
    prompt: 같은 IP만 받음(ADF) 필터링은 어떤 패킷을 받아 주는가?
    choices:
    - id: a
      text: 이전에 통신한 원격 IP에서 온 패킷
      feedback: 맞다. IP가 같으면 포트가 달라도 받는다.
    - id: b
      text: 이전에 통신한 IP와 포트가 모두 같은 패킷만
      feedback: 그것은 APDF의 기준이다.
    - id: c
      text: 바깥의 모든 출발지에서 온 패킷
      feedback: 그것은 EIF의 기준이다.
    - id: d
      text: 같은 사설 대역 안에서 온 패킷만
      feedback: 필터링은 바깥에서 온 패킷을 대상으로 한다.
    - id: e
      text: TCP로 온 패킷만
      feedback: 프로토콜 종류가 아니라 출발지를 비교하는 기준이다.
    answer: a
    feedback: 필터링은 EIF(누구든) → ADF(같은 IP) → APDF(같은 IP와 포트) 순으로 받아 주는 범위가 좁아진다.
  - id: u12-l05-p04-q02
    kind: choice
    difficulty: medium
    prompt: 지우 PC가 협력사 서버 `203.0.113.15:6000`에 UDP 패킷을 먼저 보냈다. 이후 같은 IP의 `:6001`에서 패킷이 도착했다. 사무실 NAT가 같은 IP만 받음(ADF)일 때와 같은 IP·포트만 받음(APDF)일 때의 결과는?
    choices:
    - id: a
      text: ADF는 받지 않고 APDF는 받아 준다
      feedback: 두 방식을 서로 바꾸어 이해한 것이다.
    - id: b
      text: 둘 다 IP가 같으므로 받아 준다
      feedback: APDF는 포트까지 같아야 받는다.
    - id: c
      text: 둘 다 포트가 달라서 받지 않는다
      feedback: ADF는 IP만 비교하므로 받아 준다.
    - id: d
      text: ADF는 받아 주고 APDF는 받지 않는다
      feedback: 맞다. IP만 보면 같고, 포트까지 보면 다르다.
    - id: e
      text: 포트 포워딩 규칙이 있어야만 어느 쪽이든 받아 준다
      feedback: 규칙 없이도 먼저 나간 통신의 상대에게서 온 패킷은 필터링 기준으로 판단한다.
    answer: d
    feedback: '🧩 쪼개기: 출발지를 IP와 포트로 쪼개 이전 통신 상대와 하나씩 비교하면 방식별 결과가 갈린다.'
  question_placements:
  - question_id: u12-l05-p04-q01
    after_paragraph: 3
  illustrations:
  - file: assets/animations/u12-l05-p04-filtering.svg
    title: "누가 보낸 패킷까지 받아 줄까?"
    alt: "지우 PC가 203.0.113.15:5555로 먼저 보낸 뒤 바깥 매핑 198.51.100.25:42000으로 203.0.113.15:7777과 203.0.113.99:40000의 패킷이 도착할 때 누구든, 같은 IP만, 같은 IP·포트만 받는 방식이 어떻게 다른지 보여 줍니다."
    caption: "필터링이 꼼꼼할수록 받는 상대의 범위가 좁아집니다."
    after_paragraph: 0
- page_id: advanced-nat-mapping-filtering-page-05
  illustrations:
  - file: assets/animations/u12-l05-p05-cone-names.svg
    title: "Full Cone, Symmetric은 어떻게 읽을까?"
    alt: "Full Cone, Restricted Cone, Port Restricted Cone은 매핑이 상대와 무관하고 필터링만 다르며, Symmetric은 매핑이 상대에 따라 달라진다는 옛 이름 풀이표입니다."
    caption: "옛 Cone 이름은 매핑과 필터링으로 풀어 읽습니다."
    after_paragraph: 0
  questions:
  - id: u12-l05-p05-q01
    kind: choice
    difficulty: easy
    prompt: Cone이라는 옛 이름을 바르게 이해한 것은 무엇인가?
    choices:
    - id: a
      text: Symmetric은 필터링이 가장 강한 NAT를 뜻하는 현재의 표준 등급이다
      feedback: Symmetric의 핵심은 매핑이 목적지에 따라 달라진다는 점이고, 등급이 아니다.
    - id: b
      text: Full Cone이면 어떤 상대와도 항상 연결에 성공한다
      feedback: 연결은 양쪽 조건과 방화벽에도 달려 있다.
    - id: c
      text: 옛 분류이므로 실제 동작은 매핑과 필터링을 따로 확인한다
      feedback: 맞다. 이름보다 두 기준을 확인하는 것이 정확하다.
    - id: d
      text: Cone 이름은 공유기의 처리 속도 등급이다
      feedback: 속도와 무관한 NAT 동작의 분류다.
    - id: e
      text: Restricted Cone은 목적지마다 매핑이 달라진다
      feedback: Restricted Cone은 보통 매핑이 목적지와 무관하다고 설명한다.
    answer: c
    feedback: 옛 Cone 이름은 두 기준을 묶은 말이므로 매핑 이야기인지 필터링 이야기인지 나눠 읽는다.
  - id: u12-l05-p05-q02
    kind: choice
    difficulty: medium
    prompt: 회사 공유기를 바꾸려는데 한 제품 설명에 "Full Cone 지원, P2P에 최적"이라고 적혀 있다. 서 이사에게 할 알맞은 조언은?
    choices:
    - id: a
      text: Full Cone이면 가장 안전하므로 바로 구매한다
      feedback: 넓게 받아 준다는 것은 오히려 노출이 크다는 뜻이다.
    - id: b
      text: 이름 대신 매핑·필터링 동작을 확인하고 노출도 따진다
      feedback: 맞다. 연결이 쉬워지는 대가로 노출이 늘어난다.
    - id: c
      text: Cone이라는 이름이 붙은 제품은 방화벽이 필요 없다
      feedback: NAT 동작과 방화벽 정책은 별개다.
    - id: d
      text: 광고 문구이므로 무시하고 가장 싼 제품을 산다
      feedback: P2P 연결이 업무에 필요하다면 동작을 확인할 이유가 있다.
    - id: e
      text: Symmetric이라고 적힌 제품이 가장 안전하니 그것만 본다
      feedback: Symmetric은 보안 등급이 아니다.
    answer: b
    feedback: '⚖️ 대가 따지기: P2P가 쉬워지는 편리함과 바깥에 더 열리는 노출을 함께 저울질한다.'
  question_placements:
  - question_id: u12-l05-p05-q01
    after_paragraph: 3
- page_id: advanced-nat-mapping-filtering-page-06
  illustrations:
  - file: assets/animations/u12-l05-p06-hole-punching.svg
    title: "양쪽에서 먼저 보내면 길이 열릴까?"
    alt: "박 팀장과 지우 PC가 STUN 서버 203.0.113.60으로 바깥 주소를 알아내고 소개 서버가 서로 알려 준 뒤 동시에 먼저 보내 임시 줄을 만들어 직접 연결하는 UDP 홀 펀칭 과정입니다."
    caption: "UDP 홀 펀칭은 조건이 맞을 때 직접 연결을 만듭니다."
    after_paragraph: 0
  questions:
  - id: u12-l05-p06-q01
    kind: choice
    difficulty: easy
    prompt: 홀 펀칭에서 양쪽이 서로에게 먼저 패킷을 보내는 이유는 무엇인가?
    choices:
    - id: a
      text: 공유기에 포트 포워딩 규칙을 자동으로 저장하려는 것
      feedback: 영구 규칙이 아니라 임시 상태를 만드는 것이다.
    - id: b
      text: 소개 서버에게 데이터를 대신 전달하도록 알리려는 것
      feedback: 그것은 중계 방식이고 홀 펀칭은 직접 경로를 만드는 방법이다.
    - id: c
      text: 방화벽을 일시적으로 꺼 두려는 것
      feedback: 방화벽을 끄는 것이 아니라 NAT의 상태를 이용하는 것이다.
    - id: d
      text: 상대 공유기의 관리자 암호를 얻으려는 것
      feedback: 암호를 얻는 것과는 관계가 없다.
    - id: e
      text: 각자의 NAT에 상대를 향한 허용 상태를 만들려는 것
      feedback: 맞다. 먼저 보낸 기록이 있어야 상대의 패킷을 받아 줄 수 있다.
    answer: e
    feedback: 먼저 보낸 패킷이 NAT에 '이 상대와 통신 중'이라는 상태를 만들어 상대의 패킷을 받아 준다.
  - id: u12-l05-p06-q02
    kind: choice
    difficulty: medium
    prompt: 박 팀장 집 PC와 지우 PC가 서로의 바깥 주소를 받았는데 박 팀장 쪽만 패킷을 보냈다. 지우 쪽 NAT가 같은 IP·포트만 받는 방식일 때 연결이 실패할 수 있는 이유는?
    choices:
    - id: a
      text: 소개 서버가 느려서 주소가 만료되었다
      feedback: 주소 만료가 아니라 상대 NAT의 상태 문제다.
    - id: b
      text: 박 팀장 쪽 NAT는 패킷을 바깥으로 보낼 수 없다
      feedback: 나가는 패킷은 문제없이 나간다.
    - id: c
      text: 지우 쪽 NAT에 박 팀장을 향해 나간 행이 없어 첫 패킷이 막힐 수 있다
      feedback: 맞다. 양쪽이 먼저 보내야 각자의 NAT가 상대를 받아 줄 상태가 된다.
    - id: d
      text: UDP는 한쪽만 보내면 항상 성공한다
      feedback: 한쪽만 보내면 상대 NAT가 막을 수 있다.
    - id: e
      text: 바깥 주소는 한 번 받으면 영구적이라 문제가 없다
      feedback: 바깥 주소와 매핑은 시간이 지나면 바뀔 수 있다.
    answer: c
    feedback: '📋 순서대로 확인하기: 소개 → 주소 교환 → 양쪽이 먼저 보내기라는 순서가 지켜져야 길이 열린다.'
  question_placements:
  - question_id: u12-l05-p06-q01
    after_paragraph: 3
- page_id: advanced-nat-mapping-filtering-page-07
  illustrations:
  - file: assets/animations/u12-l05-p07-relay.svg
    title: "직접 못 만나면 누가 대신 전해 줄까?"
    alt: "직접 연결이 UDP 차단, 상대별 매핑, 통신사 NAT 때문에 막히면 양쪽이 TURN 서버 203.0.113.60으로 연결해 데이터를 중계받고, 확실한 대신 서버 비용과 지연이 든다는 그림입니다."
    caption: "중계는 직접 연결이 안 될 때의 확실한 대안이며 비용과 지연이 따릅니다."
    after_paragraph: 0
  questions:
  - id: u12-l05-p07-q01
    kind: choice
    difficulty: easy
    prompt: STUN과 TURN의 역할 차이로 알맞은 것은 무엇인가?
    choices:
    - id: a
      text: STUN은 바깥 주소를 알아내도록 돕고, TURN은 데이터를 대신 전달한다
      feedback: 맞다. 주소 확인과 데이터 중계는 서로 다른 일이다.
    - id: b
      text: STUN은 데이터를 대신 전달하고, TURN은 바깥 주소를 알려 준다
      feedback: 두 역할을 서로 바꾸어 이해한 것이다.
    - id: c
      text: 둘 다 통신 내용을 암호화하는 프로토콜이다
      feedback: 암호화가 주된 역할이 아니다.
    - id: d
      text: STUN은 포트 포워딩 규칙을 만들고 TURN은 UPnP 줄을 지운다
      feedback: 두 기술은 공유기 설정을 바꾸지 않는다.
    - id: e
      text: 둘 다 공유기 안에서 동작하는 NAT 기능이다
      feedback: 두 기술은 보통 바깥의 서버에서 동작한다.
    answer: a
    feedback: STUN은 내 바깥 주소를 알려 주고, TURN은 직접 경로가 안 될 때 데이터를 중계한다.
  - id: u12-l05-p07-q02
    kind: choice
    difficulty: medium
    prompt: 한결디자인 방화벽에 "외부로 나가는 UDP 차단" 규칙이 추가된 주부터 외부 영상 통화 서비스의 화질이 떨어지고 지연이 늘었다. 서비스 쪽에서는 중계 경로 사용이 늘었다는 통계가 나왔다. 가장 그럴듯한 연결 고리는?
    choices:
    - id: a
      text: 중계 서버가 UPnP로 포트를 열어 통화가 느려졌다
      feedback: UPnP가 트래픽을 늘리지 않는다.
    - id: b
      text: UDP를 막으면 영상 통화가 자동으로 더 많이 시작된다
      feedback: 통화 시도가 늘어난다는 근거가 없다.
    - id: c
      text: 방화벽 규칙과 트래픽 증가는 서로 무관한 우연이다
      feedback: UDP 차단은 직접 경로를 막아 중계로 넘어가게 하는 원인이 될 수 있다.
    - id: d
      text: 직접 UDP 경로가 막혀 중계로 넘어가 지연이 늘었다
      feedback: 맞다. 직접 경로가 막히면 연결은 이어지지만 중계를 거쳐 지연과 서버 부담이 는다.
    - id: e
      text: NAT 변환표가 가득 차서 중계가 생겼다
      feedback: 변환표 용량과 중계의 사용은 관련이 없다.
    answer: d
    feedback: '⚖️ 대가 따지기: 직접 경로가 막히면 연결은 이어지지만 중계 서버의 트래픽과 비용이라는 대가를 치른다.'
  question_placements:
  - question_id: u12-l05-p07-q01
    after_paragraph: 2
---
## 포트를 안 열었는데 화상회의는 어떻게 될까?

<!-- learn-page-id: advanced-nat-mapping-filtering-page-01 -->

UPnP를 끈 다음 날, 박 팀장이 걱정스레 묻는다. "해외 협력사랑 화상회의를 하다가 끊기면 어떡해요?" 그런데 회의는 멀쩡하다. 양쪽 모두 공유기 뒤에 있고 아무도 포트를 열어 주지 않았는데, 영상과 음성이 오간다. 바깥에서 먼저 온 요청은 막혀서 포트 포워딩이 필요했는데, 이 연결은 어떻게 된 걸까?

가장 흔한 답은 양쪽이 모두 서비스의 서버로 안쪽에서 바깥으로 먼저 연결하는 방식이다. 앞에서 본 대로 안쪽에서 먼저 나간 통신에는 자동 행이 생기므로, 영상과 음성이 서비스 서버를 거쳐 오가면 포트를 열 일이 없다. 이것이 가장 단순한 경우다.

일부 영상 통화나 원격 지원 앱은 지연을 줄이려고 두 기기(피어)가 서버를 거치지 않고 직접 주고받는 P2P 방식을 먼저 시도한다. 앱의 소개 서버는 상대의 바깥 주소를 알려 줄 뿐이고 데이터는 나르지 않는다. 그런데 직접 통신에는 걸림돌이 있다. 박 팀장이 상대 공유기로 먼저 보낸 패킷은 맞는 행이 없어 막힐 수 있다. 두 사람이 서로 다른 건물의 안내 데스크 뒤에 있고, 양쪽 데스크가 모두 "우리 직원이 먼저 연락한 손님만 들인다"고 하는 상황과 같다.

그래서 직접 통신이 되려면 두 가지가 맞아야 한다. 내 쪽 공유기가 바깥에 어떤 주소·포트로 보이느냐와, 상대가 보낸 첫 패킷을 받아 주느냐다. 다음 Page에서 이 두 질문을 하나씩 살펴보자.

## NAT에게 꼭 따로 물어야 할 두 가지는?

<!-- learn-page-id: advanced-nat-mapping-filtering-page-02 -->

지우가 장애 메모를 쓴다. "우리 공유기는 Port Restricted라서 화상회의가 안 될 거야." 그런데 회의는 잘 되고 있다. 이름 하나로 연결 가능성을 판단한 것이 틀린 까닭은 NAT의 동작이 한 가지가 아니기 때문이다.

NAT에게는 서로 독립적인 두 가지를 물어야 한다. 첫째는 매핑이다. 안쪽 기기의 통신이 바깥에는 어떤 주소·포트로 보이는가, 상대가 달라져도 같은 번호를 쓰는가를 묻는다. 둘째는 필터링이다. 바깥에서 도착한 패킷을 누가 보낸 것까지 받아 주는가를 묻는다. 변환표로 말하면 매핑은 External 칸을 정하는 일이고, 필터링은 응답을 안쪽으로 돌려보내기 전에 적용하는 조건이다.

| 질문 | 무엇을 묻나 | 변환표에서 |
| --- | --- | --- |
| 매핑 | 안쪽 통신이 바깥에 어떤 주소·포트로 보이나 | External 칸을 정하는 방식 |
| 필터링 | 바깥의 누가 보낸 패킷까지 받아 주나 | 응답을 들여보내기 전의 조건 |

안내 데스크로 바꿔 말하면, 첫째 질문은 직원이 편지를 보낼 때 접수번호를 수신처마다 새로 붙이는지 같은 번호를 쓰는지이고, 둘째 질문은 돌아오는 우편을 이전에 편지를 받은 그 사람 것만 받는지 누구 것이든 받는지다. 두 질문은 따로 답할 수 있으므로, 한 단어 이름으로는 연결 가능성을 알 수 없다. 옛 이름이 두 질문을 어떻게 묶어 불렀는지는 뒤의 Page에서 풀어 읽는다.

그래서 지우는 메모를 이렇게 고친다. "매핑과 필터링을 따로 확인한다."

## 상대가 바뀌면 바깥 포트도 바뀔까?

<!-- learn-page-id: advanced-nat-mapping-filtering-page-03 -->

박 팀장이 집 PC(`192.168.0.20`)에서 화상회의 앱을 켠다. 주소 확인 서버(`203.0.113.60`)는 이 PC를 집 공유기의 바깥 주소 `192.0.2.123:40001`로 봤고, 앱이 그 주소를 협력사 담당자에게 알려 줬다. 그런데 협력사가 그 주소로 보낸 패킷이 도착하지 않는다. 주소는 맞게 전달됐는데 왜 안 될까?

핵심은 매핑이 상대에 따라 달라질 수 있다는 점이다. 같은 내부 통신이 어느 상대와 통신하든 같은 바깥 주소·포트를 쓰는 것을 상대와 무관한 매핑(EIM)이라 하고, 상대마다 다른 바깥 포트를 배정하는 것을 상대에 따라 달라지는 매핑이라 한다(상대의 IP만 볼지, IP·포트를 모두 볼지는 장비마다 다르다). 같은 직원이 편지를 보낼 때 접수번호를 늘 같게 쓰는지, 수신처마다 새로 붙이는지의 차이다. 집 PC `192.168.0.20:3000`이 주소 확인 서버와 협력사에 차례로 보내는 경우를 보자.

| 상대 | 상대와 무관한 매핑 | 상대에 따라 달라지는 매핑 |
| --- | --- | --- |
| 주소 확인 서버 `203.0.113.60:3478` | `192.0.2.123:40001` | `192.0.2.123:40001` |
| 협력사 `203.0.113.99:40000` | `192.0.2.123:40001` | `192.0.2.123:40017` |

상대와 무관하면 서버가 본 `:40001`이 협력사에게도 맞으므로 소개한 주소가 그대로 통한다. 상대에 따라 달라지면 협력사에게는 `:40017`로 나가서, 서버가 알려 준 주소가 협력사와의 통신에는 맞지 않는다. 표준(RFC 4787)은 UDP NAT에 상대와 무관한 매핑을 요구하지만 모든 장비가 따르는 것은 아니다.

그러니 연결이 안 될 때는 먼저 이렇게 묻는다. "같은 내부 통신이 다른 상대에게도 같은 바깥 주소·포트를 쓰는가?" 답이 아니오라면 소개 서버가 알려 준 주소만으로는 연결하기 어렵다.

## 누가 보낸 패킷까지 받아 줄까?

<!-- learn-page-id: advanced-nat-mapping-filtering-page-04 -->

같은 협력사 서버 IP에서 왔는데도 어떤 패킷은 지우의 공유기를 통과하고 어떤 패킷은 막힌다. 이번에는 매핑이 아니라 필터링의 문제다. 필터링은 바깥에서 도착한 패킷을 어떤 출발지까지 받아 줄지 정하는 기준이다.

세 가지를 같은 예로 비교해 보자. 지우 PC `192.168.10.41:3000`이 협력사 서버 `203.0.113.15:5555`에 UDP 패킷을 먼저 보냈고, 바깥 매핑은 `198.51.100.25:42000`이다. 이후 이 바깥 주소로 두 패킷이 도착한다.

| 필터링 방식 | 받아 주는 기준 | `203.0.113.15:7777`에서 도착 | `203.0.113.99:40000`에서 도착 |
| --- | --- | --- | --- |
| 누구든 받음(EIF) | 출발지를 가리지 않음 | 받음 | 받음 |
| 같은 IP만 받음(ADF) | 이전에 통신한 IP면 받음 | 받음 | 받지 않음 |
| 같은 IP·포트만 받음(APDF) | IP와 포트가 모두 같아야 받음 | 받지 않음 | 받지 않음 |

가운데 줄이 핵심 비교다. 두 패킷 중 `203.0.113.15`에서 온 쪽은 출발지 포트만 다르다. 같은 IP만 받는 방식은 IP만 보므로 받아 주고, 같은 IP·포트만 받는 방식은 포트까지 보므로 받지 않는다. 우편을 이전에 편지를 주고받은 건물 번지만 보고 받는지, 호수까지 같아야 받는지의 차이다.

누구든 받는 쪽은 앞 Lesson의 원격지 제한 없는 포워딩과 닮았지만, 안쪽이 먼저 보내 만든 매핑이 살아 있는 동안만 해당한다. 또 필터링은 NAT가 수신을 허용하는 기준일 뿐 방화벽 정책이나 앱의 로그인을 대신하지 않는다. 장비마다 구현이 다르므로 이름 하나로 추측하지 말고 확인해야 한다.

## Full Cone, Symmetric은 어떻게 읽을까?

<!-- learn-page-id: advanced-nat-mapping-filtering-page-05 -->

공유기 교체를 검토하던 지우가 한 제품의 설명서에서 "Full Cone 지원, P2P에 최적"이라는 문구를 보았다. 서 이사가 묻는다. "Full Cone이 뭐예요? 좋은 건가요?" 블로그와 제품 설명에는 이런 옛 이름이 아직 많은데, 이름만으로는 실제 동작을 알 수 없다.

Full Cone 같은 이름은 매핑과 필터링을 묶어 부르던 옛 분류다(STUN 초판인 RFC 3489의 용어이고, 현재 표준 RFC 4787은 둘을 따로 설명한다). 앞의 두 Page를 연결하면 이름이 풀린다.

| 옛 이름 | 매핑 | 필터링 |
| --- | --- | --- |
| Full Cone | 상대와 무관 | 누구든 받음 |
| Restricted Cone | 상대와 무관 | 같은 IP만 받음 |
| Port Restricted Cone | 상대와 무관 | 같은 IP·포트만 받음 |
| Symmetric | 상대에 따라 달라짐 | 상대와 연관된 조건 |

Symmetric의 핵심은 매핑이 상대에 따라 달라진다는 점이다. 그래서 "필터링이 가장 강한 것"으로 외우면 매핑의 차이를 놓친다. 이 표는 용어를 읽기 위한 전통적 요약이고 모든 공유기의 동작을 보장하지 않는다.

서 이사에게는 이렇게 답할 수 있다. 이름을 보면 매핑 이야기인지 필터링 이야기인지부터 나눠 읽는다. 대가도 따진다. Full Cone도 안쪽이 먼저 보낸 매핑에 한해서만 열리지만, 그 매핑이 살아 있는 동안은 누구든 보낼 수 있다. P2P 연결이 쉬워지는 만큼 바깥에 더 열려 있다.

## 양쪽에서 먼저 보내면 길이 열릴까?

<!-- learn-page-id: advanced-nat-mapping-filtering-page-06 -->

박 팀장 집 PC와 지우 PC가 서로의 바깥 주소를 알게 되었다. 그런데 박 팀장 쪽이 먼저 패킷을 보내면 지우 쪽 공유기가 상대를 가려 받는 방식(같은 IP만, 같은 IP·포트만)일 때 그 패킷을 막을 수 있다. 우리 쪽에서 먼저 나간 기록이 없기 때문이다. 상대를 가리지 않고 받는 장비라면 통과하므로, 앞 Page의 필터링에 달린 일이다.

소개해 준 친구 덕분에 서로 모르는 두 사람이 동시에 인사하는 장면을 떠올려 보자. 양쪽이 동시에 먼저 인사하면 서로 상대가 먼저 말을 건 셈이 된다. 이 방법이 UDP 홀 펀칭이다. 여기서 STUN은 "내 바깥 주소가 어떻게 보이는지 알려 주는 서버"다. 홀 펀칭은 세 단계로 진행된다.

| 단계 | 일어나는 일 |
| --- | --- |
| ① | 양쪽이 STUN 서버(`203.0.113.60`)에 연락해 자기 바깥 주소·포트를 알아낸다 |
| ② | 앱의 소개 서버가 각자의 바깥 주소·포트를 상대에게 알려 준다 |
| ③ | 양쪽이 서로에게 거의 동시에 먼저 보내, 각자의 NAT에 상대를 향한 임시 변환표 행이 만들어진다 |

③에서 먼저 도착한 첫 패킷은 상대 쪽 NAT에 아직 이쪽을 향한 행이 없어 버려질 수 있다. 그래도 그 패킷을 보낸 순간 보낸 쪽 NAT에는 상대를 향한 행이 생겼다. 양쪽이 계속 보내면 곧 양쪽 모두에 행이 있게 되고, 그 뒤에 도착하는 패킷은 응답처럼 받아 준다. 첫 패킷은 버려져도 이후 패킷은 통과하는 이유다. 이 행은 UPnP 줄과 달리 관리자가 남긴 영구 규칙이 아니라 임시 행이라, 한동안 통신이 없으면 사라진다.

다만 성공이 보장되지는 않는다. 상대에 따라 바깥 포트가 바뀌는 매핑이면 서버가 알려 준 주소가 틀리고, 방화벽이 UDP를 막아도 실패한다. 그럴 때의 대안은 다음 Page에서 본다.

## 직접 못 만나면 누가 대신 전해 줄까?

<!-- learn-page-id: advanced-nat-mapping-filtering-page-07 -->

홀 펀칭이 항상 성공하지는 않는다. 상대에 따라 매핑이 달라지는 NAT, 회사 방화벽의 UDP 차단, 통신사 NAT가 여러 겹인 환경이 겹치면 직접 경로를 만들 수 없다. 직접 연결에 실패한 두 사람은 어떻게 대화를 이어 갈까?

직접 전화가 안 되면 교환원을 거쳐 통화한다. 이 교환원 역할을 하는 것이 TURN 같은 중계 서버다. STUN은 바깥 주소를 알려 주고, TURN은 실제 데이터를 중계한다. 대가는 서버가 모든 데이터를 지나게 하는 데서 생긴다. 서버 비용이 늘고 경로가 길어져 지연도 커진다. UDP가 막힌 환경에서는 TCP/TLS(443)로 중계하는 경우가 많다.

앞의 방법들과 합쳐 보면 선택지는 셋이다. 가장 흔한 것은 처음에 말한 서비스 서버 경유이고, 직접 경로를 먼저 시도하는 앱은 홀 펀칭에 실패할 때만 중계로 넘어간다.

| 방법 | 데이터가 가는 길 | 대가 |
| --- | --- | --- |
| 서비스 서버 경유 | 양쪽이 서버로 먼저 연결해 서버가 전달 | 서버 부담, 서비스에 의존 |
| P2P 직접(홀 펀칭) | 두 기기가 직접 | 성공이 보장되지 않음 |
| TURN 중계 | 양쪽이 중계 서버로 연결 | 서버 비용, 지연 |

어느 방법도 우리 공유기에 포트 개방 규칙이 필요 없다. 박 팀장의 화상회의가 끊기지 않은 것은 포트가 열려서가 아니라 이 셋 중 하나로 이어졌기 때문이다. 지우는 앱의 연결 정보나 로그에서 이번 회의가 어느 방식이었는지 확인해 박 팀장에게 알려 주기로 한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** NAT의 동작은 매핑(바깥에 어떤 주소·포트로 보이나)과 필터링(누가 보낸 패킷을 받나)이라는 두 질문으로 나눠 본다. 화상회의는 서비스 서버 경유가 가장 흔하고, P2P 앱은 홀 펀칭으로 직접 연결을 시도하다 안 되면 TURN 같은 중계를 쓴다.
- **적용하기 (Apply):** 연결 문제를 만나면 옛 Cone 이름 대신 매핑과 필터링을 따로 확인한다. 직접 경로가 안 되는 환경(UDP 차단, 통신사 NAT)에서는 중계 비용까지 따진다.
- **찾아보기 (Lookup):** NAT 동작 요구사항(RFC 4787), STUN(RFC 8489)과 TURN(RFC 8656) 문서, 쓰는 화상회의·원격 지원 서비스의 네트워크 요구사항은 필요할 때 직접 찾아본다.

### 🧠 이번에 쓴 생각법

- 🧩 **쪼개기**: NAT의 동작을 매핑과 필터링 두 질문으로 나누고, 소개하는 일과 데이터를 나르는 일도 나누어 보았다.
- 🗺️ **필요한 것만 남기기**: Full Cone 같은 옛 이름은 두 기준으로 풀어 읽고, 연결 가능성에 필요한 기준만 남겼다.
- ⚖️ **대가 따지기**: 직접 경로는 비용이 적지만 성공이 보장되지 않고, 중계는 확실하지만 서버 비용이 드는 선택을 따졌다.

이 Unit은 포트를 열고 닫는 방법에서 시작해 포트를 열지 않고도 연결하는 방법까지 왔다. 모두 주소와 포트를 바꿔 안쪽과 바깥쪽을 이어 주는 변환표 원리 위에 있다. 시연을 마친 8080 규칙은 이미 지웠고, 이제 서 이사가 새 계획을 꺼낸다. AI 상담 챗봇 「한결봇」을 고객에게 공개하자는 것이다. 한결봇은 사내 AI 서버(`192.168.10.50:8080`)를 열어 두는 방식이 아니라, 별도의 공개 주소(`203.0.113.10:443`)와 별도 서비스 구역의 서버 풀(`192.168.20.11`~`.13`)로 새로 연다. 고객이 몰려오면 포트 포워딩 한 줄과 서버 한 대로는 감당할 수 없다. 요청을 여러 서버에 나눠 보내는 장치가 다음 Unit의 L4 부하 분산기다.

그 뒤의 일도 하나 남았다. 지우는 매주 공유기 화면의 포트 매핑과 UPnP 목록을 열어, 승인 기록에 없는 줄이 생겼는지 눈으로 대조한다. 이 손작업이 반복되면 놓치기 쉽다. 이런 대조를 자동으로 하고 이상한 줄이 생기면 알려 주는 방법은 Module 4(이상탐지 자동화)에서 다룬다.
