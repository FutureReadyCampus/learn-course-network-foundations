---
id: u6-l31-한-번에-끝내는-dns
title: DNS는 이름을 IP 주소로 바꿔 준다
description: 내 컴퓨터가 웹사이트 이름을 IP 주소로 찾는 과정을 살펴봅니다.
estimated_minutes: 18
source_url: https://github.com/FutureReadyCampus/course-network/wiki/외워서네트워크
page_metadata:
- terms:
  - DNS
  - IP 주소
  animations:
  - file: l31-dns-phonebook.svg
    title: 이름을 주소로 바꾸는 DNS
    alt: 컴퓨터가 도메인 이름을 DNS에 물어보고 IP 주소를 받아 연결하는 흐름입니다.
    caption: DNS가 이름을 IP 주소로 찾아줍니다.
  page_id: dns-purpose
  questions:
  - id: u9-l01-p01-q01
    kind: choice
    difficulty: easy
    prompt: DNS가 사이트 이름을 입력한 컴퓨터에 찾아 주는 것은 무엇인가요?
    choices:
    - id: a
      text: 그 서비스에 연결할 IP 주소
      feedback: 맞아요. 이름만으로 데이터를 보낼 수 없어 연결에 사용할 IP 주소를 찾습니다.
    - id: b
      text: 그 사이트가 보여 줄 웹 문서
      feedback: DNS는 웹 문서를 전달하는 대신 목적지 IP 주소를 찾습니다.
    - id: c
      text: 사이트 이름을 새로 짓는 방법
      feedback: DNS 조회는 이름을 새로 만드는 일이 아니라 주어진 이름의 주소를 찾는 일입니다.
    - id: d
      text: 모든 사이트가 함께 쓰는 고정 주소
      feedback: 서비스마다 주소가 다를 수 있으며 한 서비스도 여러 주소를 쓸 수 있습니다.
    - id: e
      text: 사용자가 입력해야 할 사이트 이름
      feedback: 이미 입력한 이름을 바탕으로 컴퓨터가 사용할 IP 주소를 찾습니다.
    answer: a
  - id: u9-l01-p01-q02
    kind: choice
    difficulty: medium
    prompt: 같은 사이트 이름에서 이전과 다른 IP 주소를 얻었습니다. 본문에 비추어 알맞은 판단은 무엇인가요?
    choices:
    - id: a
      text: 이름이 같으니 새 주소는 반드시 오류다
      feedback: 한 이름이 언제나 하나의 고정 IP 주소에만 대응하지는 않습니다.
    - id: b
      text: 서비스가 주소를 바꾸거나 여러 주소를 쓸 수 있다
      feedback: 맞아요. 서비스는 여러 주소를 사용하거나 주소를 바꿀 수 있으므로 주소 차이만으로 오류라고 단정할 수 없습니다.
    - id: c
      text: DNS 조회가 웹 문서까지 전달한 것이다
      feedback: 조회 결과는 연결에 쓸 주소이며 웹 문서 자체가 아닙니다.
    - id: d
      text: 이름을 알면 주소 없이도 데이터를 보낼 수 있다
      feedback: 네트워크에서 실제로 데이터를 보낼 때 목적지 IP 주소가 필요합니다.
    - id: e
      text: 사이트 이름도 반드시 다른 이름으로 바뀌었다
      feedback: 같은 이름을 유지하면서 서비스의 주소가 바뀔 수 있습니다.
    answer: b
  question_placements:
  - question_id: u9-l01-p01-q01
    after_paragraph: 1
  illustrations:
  - file: assets/animations/l31-daily-friend-classroom.svg
    title: "친구 이름과 교실 위치"
    alt: "나는 친구 민수의 이름만 알고 교실 위치는 모릅니다. 안내 데스크에 민수 교실이 어디인지 묻고 3층 2반이라는 위치를 들은 뒤, 그 위치를 따라 교실로 찾아갑니다."
    caption: "이름만 알아서는 찾아갈 수 없고, 위치를 알아야 찾아갈 수 있습니다."
    after_paragraph: -1
  - file: assets/animations/l31-dns-name-to-ip.svg
    title: "DNS는 이름을 IP 주소로 바꿔요"
    alt: "브라우저에 example.com을 입력하면 컴퓨터가 DNS에 이 이름의 IP 주소를 묻고, 예시 주소 203.0.113.10을 받아 그 주소의 서버로 데이터를 보냅니다. 한 이름이 여러 주소를 쓰거나 주소를 바꿀 수도 있다고 표시됩니다."
    caption: "데이터를 보내려면 IP 주소가 필요하고, DNS는 이름에 맞는 주소를 찾아 줍니다. 주소는 예시입니다."
    after_paragraph: 0
- terms:
  - 계층
  - 분산
  - 도메인 이름
  animations:
  - file: l31-dns-hierarchy.svg
    title: 도메인 이름의 범위
    alt: 도메인 이름의 오른쪽에서 왼쪽으로 범위가 좁아지는 구조입니다.
    caption: 오른쪽은 큰 범위, 왼쪽은 더 구체적인 이름입니다.
  page_id: domain-name-definition
  questions:
  - id: u9-l01-p02-q01
    kind: choice
    difficulty: easy
    prompt: www.example.com에서 이름의 범위를 큰 쪽부터 좁혀 읽은 순서는 무엇인가요?
    choices:
    - id: a
      text: www → example → com
      feedback: 왼쪽부터 읽은 순서입니다. 큰 범위는 오른쪽에 있습니다.
    - id: b
      text: example → com → www
      feedback: example보다 오른쪽의 com이 더 큰 범위입니다.
    - id: c
      text: com → example → www
      feedback: 맞아요. 오른쪽의 com에서 왼쪽으로 갈수록 더 구체적인 이름이 됩니다.
    - id: d
      text: com → www → example
      feedback: com 다음에는 그 안의 example, 그다음에는 www로 좁혀 갑니다.
    - id: e
      text: www → com → example
      feedback: www는 가장 큰 범위가 아니라 도메인 안에서 쓰는 이름입니다.
    answer: c
  - id: u9-l01-p02-q02
    kind: choice
    difficulty: medium
    prompt: DNS에서 이름의 범위를 나누고 정보를 여러 서버에 맡기는 이유를 본문대로 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 왼쪽 이름을 맡은 한 서버가 모든 정보를 관리한다
      feedback: DNS 정보는 한 서버에 몰리지 않고 여러 서버가 나누어 관리합니다.
    - id: b
      text: 모든 서버가 세상의 모든 이름을 각각 관리한다
      feedback: 분산은 모든 서버에 모든 이름을 맡기는 대신 정보를 나누어 맡기는 방식입니다.
    - id: c
      text: 점으로 나눈 각 이름이 같은 크기의 범위를 뜻한다
      feedback: 오른쪽은 큰 범위, 왼쪽은 더 구체적인 범위를 나타냅니다.
    - id: d
      text: 여러 서버가 나누어 맡아 필요한 이름의 담당 범위를 따라간다
      feedback: 맞아요. 이름의 계층과 분산 관리를 함께 이용해 담당 범위를 좁혀 갑니다.
    - id: e
      text: 서버마다 같은 이름을 서로 무관한 범위로 해석한다
      feedback: 점으로 나눈 이름의 범위를 따라 담당 서버를 찾는 구조입니다.
    answer: d
  question_placements:
  - question_id: u9-l01-p02-q01
    after_paragraph: 1
  illustrations:
  - file: assets/animations/l31-daily-address-scope.svg
    title: "큰 범위에서 작은 범위로"
    alt: "대한민국, 서울시, 한빛학교가 차례로 강조되며 큰 상자 안에 더 작은 상자가 하나씩 들어갑니다. 마지막에는 나라와 서울시가 각 범위를 맡아 관리한다고 표시됩니다."
    caption: "주소는 큰 범위에서 작은 범위로 좁혀 가며, 범위마다 맡아 관리하는 곳이 따로 있습니다."
    after_paragraph: -1
  - file: assets/animations/l31-domain-name-scope.svg
    title: "도메인 이름은 오른쪽이 큰 범위"
    alt: "www.example.com에서 오른쪽의 com, 그 안의 example, 마지막으로 www가 차례로 강조되며 큰 상자 안에 작은 상자가 들어갑니다. 마지막에는 com과 example.com을 각각 다른 담당 서버가 나누어 맡는다고 표시됩니다."
    caption: "도메인 이름은 오른쪽이 큰 범위이고, DNS 정보는 여러 서버가 범위를 나누어 관리합니다."
    after_paragraph: 0
- terms:
  - hosts 파일
  - DNS Cache
  page_id: dns-local-check
  questions:
  - id: u9-l01-p03-q01
    kind: choice
    difficulty: easy
    prompt: hosts 파일과 컴퓨터의 DNS 캐시를 올바르게 구별한 것은 무엇인가요?
    choices:
    - id: a
      text: 둘 다 사용자가 직접 적어 둔 목록이다
      feedback: 직접 정해 둔 목록은 hosts 파일이고 캐시는 앞서 조회한 답입니다.
    - id: b
      text: 둘 다 인터넷 DNS 서버에만 보관된다
      feedback: 이 페이지의 hosts 파일과 캐시는 컴퓨터 안에서 확인할 수 있습니다.
    - id: c
      text: hosts는 조회 결과이고 캐시는 직접 적은 목록이다
      feedback: 둘의 역할이 반대입니다. hosts는 직접 적은 값, 캐시는 조회 결과입니다.
    - id: d
      text: hosts는 이름만, 캐시는 주소만 따로 보관한다
      feedback: 둘 다 이름에 대응하는 주소를 찾는 데 쓰이며 이 방식으로 나누지 않습니다.
    - id: e
      text: hosts는 직접 적은 목록이고 캐시는 앞서 조회한 답이다
      feedback: 맞아요. 값을 얻은 방식은 다르지만 둘 다 컴퓨터 안에서 사용할 답을 찾는 데 쓰입니다.
    answer: e
  - id: u9-l01-p03-q02
    kind: choice
    difficulty: medium
    prompt: 컴퓨터 안에 사용할 수 있는 이름 조회 답이 없습니다. 다음 행동으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 설정된 DNS 서버에 그 이름을 물어본다
      feedback: 맞아요. 사용할 로컬 답이 없으면 지정된 DNS 서버에 조회합니다.
    - id: b
      text: 조회할 수 없으므로 사이트가 없어졌다고 결론 낸다
      feedback: 컴퓨터 안에 답이 없는 것과 사이트가 없는 것은 다릅니다. DNS 서버에 물어볼 수 있습니다.
    - id: c
      text: hosts에 없으므로 목적지 주소 없이 바로 접속한다
      feedback: 로컬 답이 없으면 주소 없이 보내는 대신 DNS 서버에 물어봅니다.
    - id: d
      text: 항상 hosts를 직접 고친 뒤에만 접속한다
      feedback: hosts를 고치지 않아도 지정된 DNS 서버에 이름을 물어볼 수 있습니다.
    - id: e
      text: 모든 운영체제에서 같은 세부 확인 순서를 강제한다
      feedback: 세부 순서는 운영체제와 설정에 따라 다를 수 있습니다. 공통 흐름은 로컬 답이 없으면 DNS 서버에 묻는 것입니다.
    answer: a
  question_placements:
  - question_id: u9-l01-p03-q01
    after_paragraph: 1
  illustrations:
  - file: assets/animations/l31-daily-notebook-first.svg
    title: "먼저 내 수첩부터 봐요"
    alt: "나는 먼저 직접 적어 둔 수첩을 보고, 다음으로 전에 들은 답을 적은 최근 메모를 봅니다. 둘 다 없어서 동네 안내소에 묻고, 들은 답을 메모에 잠시 남깁니다."
    caption: "직접 적어 둔 수첩과 전에 들은 답을 적은 메모를 먼저 보고, 없으면 밖에 묻습니다."
    after_paragraph: -1
  - file: assets/animations/l31-hosts-cache-first.svg
    title: "hosts 파일과 DNS 캐시 먼저"
    alt: "컴퓨터가 먼저 직접 적은 이름과 주소의 목록인 hosts 파일을 보고, 다음으로 최근 조회한 답이 있는 DNS 캐시를 봅니다. 둘 다 없어서 지정된 DNS 서버에 묻고, 받은 답을 DNS 캐시에 잠시 기억합니다."
    caption: "hosts는 직접 적은 값이고 캐시는 조회 결과입니다. 확인 순서는 운영체제와 설정에 따라 다를 수 있습니다."
    after_paragraph: 0
- terms:
  - DNS 서버 주소
  - 공유기
  page_id: dns-local-server
  questions:
  - id: u9-l01-p04-q01
    kind: choice
    difficulty: easy
    prompt: 컴퓨터 안에서 답을 못 찾았을 때 DNS 질의를 먼저 보내는 대상은 무엇인가요?
    choices:
    - id: a
      text: 항상 집의 공유기 자체
      feedback: 집에서도 설정에 따라 다르며 공유기가 질의를 전달하기도 합니다.
    - id: b
      text: 컴퓨터에 설정된 DNS 서버
      feedback: 맞아요. 컴퓨터는 지정된 DNS 서버에 이름의 IP 주소를 묻습니다.
    - id: c
      text: 사용자가 열려는 웹 문서
      feedback: 웹 문서는 조회 대상 서버가 아닙니다. 설정된 DNS 서버에 이름을 보냅니다.
    - id: d
      text: 회사나 학교의 DNS 서버만
      feedback: 회사나 학교의 자체 서버는 가능한 사례이며 모든 환경에 해당하지 않습니다.
    - id: e
      text: 그 이름과 관계된 모든 DNS 서버 동시에
      feedback: 본문의 컴퓨터는 먼저 지정된 DNS 서버에 질의합니다.
    answer: b
  - id: u9-l01-p04-q02
    kind: choice
    difficulty: medium
    prompt: 집에서 공유기를 거쳐 DNS 질의가 전달됩니다. 역할을 알맞게 설명한 것은 무엇인가요?
    choices:
    - id: a
      text: 공유기가 보이면 공유기가 언제나 최종 답을 찾는다
      feedback: 공유기는 다른 DNS 서버에 질의를 전달하는 역할만 할 수도 있습니다.
    - id: b
      text: 컴퓨터는 질문하지 않고 DNS 서버가 먼저 주소를 보낸다
      feedback: 컴퓨터가 이름의 IP 주소를 묻는 질문을 시작합니다.
    - id: c
      text: 컴퓨터가 질문을 시작하고 DNS 서버는 답을 주거나 찾아온다
      feedback: 맞아요. 컴퓨터와 DNS 서버의 역할을 나누어 보아야 하며 공유기가 중간에 전달할 수도 있습니다.
    - id: d
      text: DNS 서버는 모르는 답을 다른 서버에 물을 수 없다
      feedback: 지정된 DNS 서버는 모르면 다른 DNS 서버에 물어 답을 찾아올 수 있습니다.
    - id: e
      text: 공유기가 있으면 컴퓨터의 DNS 설정은 쓰이지 않는다
      feedback: 컴퓨터는 설정된 DNS 서버로 질의하고 공유기가 그 과정에 참여할 수 있습니다.
    answer: c
  question_placements:
  - question_id: u9-l01-p04-q01
    after_paragraph: 1
  illustrations:
  - file: assets/animations/l31-daily-ask-local-desk.svg
    title: "동네 안내소에 물어봐요"
    alt: "나는 한빛학교가 어디인지 묻고, 경비실이 그 질문을 동네 안내소에 전해 줍니다. 동네 안내소는 알면 바로, 모르면 다른 안내소에 물어 답을 찾아오고, 본관 3층이라는 답을 나에게 알려 줍니다."
    caption: "질문은 내가 시작하고, 경비실은 전해 주기만 할 수 있으며, 답은 안내소가 찾아 줍니다."
    after_paragraph: -1
  - file: assets/animations/l31-local-dns-server-query.svg
    title: "지정된 DNS 서버에 질의해요"
    alt: "컴퓨터가 이름의 IP 주소를 묻는 질의를 시작하고, 공유기가 이 질의를 지정된 DNS 서버에 전달합니다. 지정된 DNS 서버는 알면 바로 답하고 모르면 다른 DNS 서버에 물어 답을 찾은 뒤, 예시 주소 203.0.113.10을 컴퓨터에 돌려줍니다."
    caption: "컴퓨터는 질의를 시작하고, 지정된 DNS 서버가 답을 돌려줍니다. 공유기는 질의를 전달만 할 수도 있습니다."
    after_paragraph: 0
- terms:
  - 루트 DNS 서버
  - TLD
  - 담당 DNS 서버
  page_id: dns-delegation
  questions:
  - id: u9-l01-p05-q01
    kind: choice
    difficulty: easy
    prompt: 어떤 도메인의 정보를 관리하도록 맡겨진 서버는 무엇인가요?
    choices:
    - id: a
      text: 모든 이름의 최종 주소를 관리하는 루트 서버
      feedback: 루트는 보통 다음 범위의 서버를 안내하며 모든 최종 주소를 관리하는 역할로 설명되지 않습니다.
    - id: b
      text: 최근 답만 잠시 저장하는 컴퓨터
      feedback: 임시 저장과 도메인의 정보를 맡아 관리하는 역할은 다릅니다.
    - id: c
      text: 질문을 시작하는 사용자 컴퓨터
      feedback: 사용자 컴퓨터는 질의를 시작하며 도메인 정보의 담당 서버와 구별됩니다.
    - id: d
      text: 그 도메인의 담당 DNS 서버
      feedback: 맞아요. 담당 DNS 서버는 해당 도메인의 정보를 관리하도록 맡겨진 서버입니다.
    - id: e
      text: 질의를 전달하는 모든 공유기
      feedback: 질의 전달만으로 해당 도메인의 정보를 관리하는 담당 서버가 되지는 않습니다.
    answer: d
  - id: u9-l01-p05-q02
    kind: choice
    difficulty: medium
    prompt: www.example.com의 답을 모르는 DNS 서버가 루트부터 안내를 따라갑니다. 본문의 예에 맞는 흐름은 무엇인가요?
    choices:
    - id: a
      text: 루트가 최종 IP를 모두 보관하므로 나머지는 생략한다
      feedback: 루트는 예에서 com 서버를 알려주며 최종 주소를 모두 알려주는 역할이 아닙니다.
    - id: b
      text: example.com 담당 → com 담당 → 루트 순으로 좁힌다
      feedback: 큰 범위인 루트에서 com을 거쳐 example.com 담당으로 좁혀 갑니다.
    - id: c
      text: com 담당이 루트를 찾은 뒤 사용자에게 이름을 다시 짓게 한다
      feedback: 서버 안내는 기존 이름의 담당 범위를 찾기 위한 것이며 이름을 새로 짓지 않습니다.
    - id: d
      text: 루트와 com 서버가 모두 같은 최종 IP를 직접 반환한다
      feedback: 앞 단계는 보통 다음 서버를 안내하고 마지막 담당 서버가 답을 줍니다.
    - id: e
      text: 루트가 com 담당을, com 담당이 example.com 담당을 안내한다
      feedback: 맞아요. 다음 범위를 맡은 서버를 따라가 마지막에 해당 이름의 답을 얻습니다.
    answer: e
  question_placements:
  - question_id: u9-l01-p05-q01
    after_paragraph: 2
  illustrations:
  - file: assets/animations/l31-daily-follow-desks.svg
    title: "안내소를 따라 좁혀 가요"
    alt: "답을 모르는 동네 안내소가 전국 안내소에 물으면 서울시 안내소를 알려 주고, 서울시 안내소는 한빛학교 교무실을 알려 주며, 한빛학교 교무실이 2반은 본관 3층이라고 정확히 알려 줍니다."
    caption: "앞 단계의 안내소는 방향만 알려 주고, 마지막 담당 교무실이 정확한 답을 줍니다."
    after_paragraph: -1
  - file: assets/animations/l31-root-tld-authoritative.svg
    title: "루트부터 담당 DNS 서버까지"
    alt: "지정된 DNS 서버가 루트 DNS 서버에 물으면 .com 서버를 안내받고, .com 서버는 example.com 담당 서버를 안내하며, example.com 담당 DNS 서버가 www.example.com의 예시 주소 203.0.113.10을 알려 줍니다."
    caption: "앞 단계의 서버는 다음에 물을 서버를 알려 주고, 담당 DNS 서버가 최종 답을 줍니다. 주소는 예시입니다."
    after_paragraph: 0
- terms:
  - DNS 캐시
  - TTL(Time To Live)
  animations:
  - file: l31-dns-cache-ttl.svg
    title: DNS 캐시와 유효 시간
    alt: 찾은 주소를 캐시에 저장해 TTL이 끝날 때까지 사용합니다.
    caption: TTL 동안 답을 기억하고 시간이 지나면 다시 조회합니다.
  page_id: dns-cache-ttl
  questions:
  - id: u9-l01-p06-q01
    kind: choice
    difficulty: easy
    prompt: DNS 정보의 TTL은 캐시에 대해 무엇을 정하나요?
    choices:
    - id: a
      text: 조회한 답을 캐시에서 사용할 시간
      feedback: 맞아요. TTL은 답을 무한히 기억하지 않도록 캐시에 사용할 시간을 정합니다.
    - id: b
      text: 같은 사이트를 방문할 수 있는 횟수
      feedback: TTL은 방문 횟수가 아니라 캐시된 답의 유효 시간과 관련됩니다.
    - id: c
      text: DNS 서버가 관리할 수 있는 도메인 수
      feedback: TTL은 관리할 이름의 수가 아니라 답을 기억할 시간입니다.
    - id: d
      text: 사이트가 새 주소를 만들 수 있는 횟수
      feedback: TTL은 주소 변경 횟수를 제한하지 않고 캐시 사용 시간을 정합니다.
    - id: e
      text: 웹 문서를 읽을 수 있는 시간
      feedback: 여기서 TTL은 웹 문서 열람 시간이 아니라 DNS 답의 캐시 시간입니다.
    answer: a
  - id: u9-l01-p06-q02
    kind: choice
    difficulty: medium
    prompt: 사이트 주소가 바뀌었는데 일부 DNS 캐시에 이전 답의 TTL이 남아 있습니다. 가능한 상황은 무엇인가요?
    choices:
    - id: a
      text: 주소 변경 즉시 모든 캐시가 반드시 함께 바뀐다
      feedback: 캐시가 같은 순간에 갱신되는 것은 아니므로 이전 답을 쓰는 곳이 남을 수 있습니다.
    - id: b
      text: 유효 시간이 남은 캐시는 이전 답을 잠시 사용할 수 있다
      feedback: 맞아요. 캐시는 TTL 동안 답을 사용할 수 있어 모든 곳에서 동시에 갱신되지 않을 수 있습니다.
    - id: c
      text: 한 번 저장한 답은 TTL이 지나도 계속 사용한다
      feedback: TTL이 지난 뒤에는 오래된 주소를 계속 쓰지 않도록 다시 조회합니다.
    - id: d
      text: TTL이 남아 있으면 담당 서버도 주소를 바꿀 수 없다
      feedback: TTL은 캐시의 사용 시간이며 담당 서버의 주소 변경을 막는 규칙이 아닙니다.
    - id: e
      text: 캐시마다 답이 다르면 반드시 DNS 변조가 발생했다
      feedback: 유효 시간이 서로 다른 캐시로도 갱신 시점 차이가 생길 수 있어 변조라고 단정할 수 없습니다.
    answer: b
  question_placements:
  - question_id: u9-l01-p06-q01
    after_paragraph: 1
  illustrations:
  - file: assets/animations/l31-daily-memo-expiry.svg
    title: "메모에 유효 시간을 적어요"
    alt: "동네 안내소가 교무실의 답을 5분 동안 쓸 수 있다고 메모하고, 같은 질문이 오면 메모를 보고 바로 답합니다. 5분이 지나면 그 메모를 더 쓰지 않고, 다시 물어 새 답을 받고 시간을 새로 셉니다."
    caption: "메모에 유효 시간을 적어 두면 빨리 답할 수 있고, 시간이 지나면 다시 물어봅니다."
    after_paragraph: -1
  - file: assets/animations/l31-cache-ttl-expiry.svg
    title: "DNS 캐시와 TTL"
    alt: "지정된 DNS 서버가 담당 서버의 답을 TTL 300초와 함께 캐시에 넣고, 같은 이름을 다시 물으면 캐시에서 바로 답합니다. TTL이 0초가 되면 그 답은 만료되어 더 쓰지 않고, 다시 조회해 새 답을 받으면 TTL을 새로 셉니다."
    caption: "DNS 캐시는 조회를 빠르게 하고, TTL은 답을 기억할 시간을 정합니다. 300초는 예시입니다."
    after_paragraph: 0
- terms:
  - DNS 변조
  - 주 DNS
  - 보조 DNS
  page_id: dns-failures
  questions:
  - id: u9-l01-p07-q01
    kind: choice
    difficulty: easy
    prompt: 사이트 이름으로 접속하지 못했을 때 본문에 맞는 첫 판단은 무엇인가요?
    choices:
    - id: a
      text: 웹 서버가 고장 났다고 바로 확정한다
      feedback: 이름을 주소로 바꾸는 단계에서 실패했을 수도 있어 웹 서버 고장으로 단정할 수 없습니다.
    - id: b
      text: 네트워크 전체가 끊겼다고 바로 확정한다
      feedback: DNS 조회 실패와 네트워크 전체 장애는 구별해야 합니다.
    - id: c
      text: 이름 조회 단계와 주소를 얻은 뒤 연결 단계를 나누어 살핀다
      feedback: 맞아요. 어느 단계가 실패했는지 나누어야 DNS 문제인지 그 뒤의 연결 문제인지 살필 수 있습니다.
    - id: d
      text: 보조 DNS가 있으면 모든 연결이 정상이라고 판단한다
      feedback: 보조 서버가 있어도 모든 접속 문제가 해결되는 것은 아닙니다.
    - id: e
      text: DNS 응답이 왔으면 그 주소는 반드시 옳다고 판단한다
      feedback: 잘못된 답을 보내는 변조에서는 응답이 와도 엉뚱한 주소일 수 있습니다.
    answer: c
  - id: u9-l01-p07-q02
    kind: choice
    difficulty: medium
    prompt: 주 DNS 외에 보조 DNS도 설정했고 DNS 응답도 받았습니다. 그래도 접속 문제를 살펴야 하는 이유는 무엇인가요?
    choices:
    - id: a
      text: 보조 DNS는 주 DNS 장애 때도 응답을 도울 수 없기 때문이다
      feedback: 보조 서버는 주 서버에 문제가 있을 때 응답을 도울 수 있습니다.
    - id: b
      text: 응답만 오면 그 뒤의 연결 문제는 자동으로 해결되기 때문이다
      feedback: DNS 응답은 주소를 얻는 단계이며 그 뒤 연결까지 보장하지 않습니다.
    - id: c
      text: DNS 변조가 있으면 서버가 반드시 무응답이기 때문이다
      feedback: 변조는 응답이 정상처럼 보여도 잘못된 주소를 보내는 형태일 수 있습니다.
    - id: d
      text: 보조 DNS가 모든 문제를 해결하지 않고 잘못된 답도 올 수 있기 때문이다
      feedback: 맞아요. 보조 서버는 도움을 줄 수 있지만 연결 문제나 변조를 모두 해결하지는 않아 답의 출처와 네트워크 상태를 함께 살펴야 합니다.
    - id: e
      text: 보조 DNS를 두면 이름 조회와 연결이 같은 단계가 되기 때문이다
      feedback: 보조 서버를 두어도 이름을 주소로 바꾸는 단계와 이후 연결은 구별됩니다.
    answer: d
  question_placements:
  - question_id: u9-l01-p07-q01
    after_paragraph: 1
  illustrations:
  - file: assets/animations/l31-daily-desk-down-or-wrong.svg
    title: "안내가 막히거나 틀리면"
    alt: "주 안내소가 대답하지 않으면 위치를 알 수 없고, 보조 안내소가 대신 알려 줄 수 있습니다. 가짜 안내를 믿으면 한빛학교가 아닌 엉뚱한 건물로 가게 됩니다. 마지막에는 위치 알아내기와 찾아가기가 두 단계로 나뉘어 표시됩니다."
    caption: "위치를 알아내는 단계와 찾아가는 단계를 나누어 보면 어디서 막혔는지 알 수 있습니다."
    after_paragraph: -1
  - file: assets/animations/l31-dns-failure-split.svg
    title: "DNS 문제와 연결 문제 구분"
    alt: "주 DNS 서버가 응답하지 않으면 이름 조회가 막히고, 보조 DNS 서버가 대신 응답을 도울 수 있습니다. DNS 변조가 일어나면 정상처럼 보이는 답을 믿고 진짜 서버가 아닌 엉뚱한 서버로 연결됩니다. 마지막에는 이름을 주소로 바꾸는 단계와 주소로 연결하는 단계가 나뉘어 표시됩니다."
    caption: "사이트 이름이 열리지 않으면 DNS 조회와 그 뒤의 연결을 나누어 살펴봅니다."
    after_paragraph: 0
animations_dir: units/06-web-fundamentals/lessons/01-한-번에-끝내는-dns/assets/animations
---

## DNS는 사이트 이름을 IP 주소로 바꾼다

<!-- learn-page-id: dns-purpose -->

브라우저에 `example.com` 같은 이름을 입력하면 컴퓨터는 그 이름만으로 인터넷에서 상대를 찾을 수 없습니다. 네트워크에서 실제로 데이터를 보낼 때는 목적지의 IP 주소가 필요합니다. DNS(Domain Name System)는 사람이 기억하기 쉬운 도메인 이름을 해당 서비스의 IP 주소로 찾아 주는 체계입니다.

학교에서 친구 이름을 알고 있어도 교실을 찾아가려면 교실 위치를 알아야 하는 것과 비슷합니다. DNS에 이름을 물으면 컴퓨터가 연결에 사용할 주소를 얻습니다. 다만 한 사이트의 이름이 언제나 하나의 고정 IP 주소에만 대응한다고 생각하면 안 됩니다. 서비스는 여러 주소를 쓰거나 주소를 바꿀 수 있습니다.

기억할 한 줄: **DNS는 기억하기 쉬운 이름을 네트워크가 찾아갈 IP 주소로 연결한다.**

<!-- source: 외워서네트워크 lesson-31.md; 혼자공부하는네트워크 05-1 DNS와 자원, pp.252–254 -->

## 도메인 이름은 오른쪽부터 큰 범위를 나타낸다

<!-- learn-page-id: domain-name-definition -->

`www.example.com`을 보면 오른쪽의 `.com`은 더 넓은 이름의 범위를, 그 왼쪽의 `example`은 그 안의 도메인을 나타냅니다. `www`는 그 도메인 안에서 쓰이는 이름입니다. 점으로 나눈 이름은 오른쪽에서 왼쪽으로 읽으며, 오른쪽일수록 더 큰 범위입니다.

학교 주소를 `대한민국 → 서울시 → 어느 구 → 어느 학교`처럼 큰 범위에서 작은 범위로 좁혀 적는 모습과 비슷합니다. 인터넷에서는 모든 도메인 이름과 주소를 한 컴퓨터에 몰아넣지 않습니다. 여러 DNS 서버가 이름의 일부를 나누어 관리하는데, 이렇게 나누어 맡기는 방식을 **분산**이라고 합니다. 그래서 필요한 이름을 찾을 때 담당 범위를 차례로 따라갑니다.

기억할 한 줄: **도메인 이름은 오른쪽이 큰 범위이고, DNS 정보는 여러 서버가 나누어 관리한다.**

<!-- source: 외워서네트워크 lesson-31.md; 혼자공부하는네트워크 05-1 DNS와 자원, pp.254–257 -->

## 컴퓨터는 먼저 자기 안에서 답을 찾아본다

<!-- learn-page-id: dns-local-check -->

웹사이트에 접속할 때 컴퓨터는 매번 처음부터 인터넷의 DNS 서버를 찾아다니지 않습니다. 컴퓨터 안의 `hosts` 파일에는 이름과 주소를 직접 적어 둘 수 있고, 최근에 알아낸 DNS 답을 잠시 보관하는 캐시도 있습니다. 이미 쓸 수 있는 답이 있으면 다시 묻는 일을 줄일 수 있습니다.

`hosts` 파일은 사용자가 직접 정해 둔 이름과 주소의 목록이고, 캐시는 앞서 조회한 답을 잠시 기억한 것입니다. 운영체제와 설정에 따라 확인 세부 순서는 다를 수 있지만, 사용할 수 있는 로컬 답이 있는지 살펴본 뒤 없으면 지정된 DNS 서버에 물어봅니다. 둘 다 컴퓨터 안에서 확인할 수 있다는 점은 같지만, 하나는 직접 적은 값이고 다른 하나는 조회 결과를 임시로 기억한 값입니다.

기억할 한 줄: **먼저 컴퓨터 안에 사용할 답이 있는지 확인하고, 없으면 DNS 서버에 묻는다.**

<!-- source: 외워서네트워크 lesson-31.md; 혼자공부하는네트워크 05-1 DNS와 자원, pp.258–260 -->

## 모르면 컴퓨터가 지정된 DNS 서버에 묻는다

<!-- learn-page-id: dns-local-server -->

컴퓨터 안에서 답을 찾지 못하면 컴퓨터에 설정된 DNS 서버로 이름을 보냅니다. 이 요청을 DNS 질의라고 합니다. 집에서는 인터넷 공유기가 DNS 서버 주소를 알려주거나 질의를 다른 DNS 서버로 전달하도록 설정된 경우가 많고, 회사나 학교에서는 자체 DNS 서버를 사용할 수도 있습니다.

여기서 컴퓨터와 DNS 서버의 역할을 나누어 생각해 봅시다. 컴퓨터는 “이 이름의 IP 주소가 뭐야?”라고 질문을 시작합니다. 지정된 DNS 서버는 답을 이미 알고 있으면 돌려주고, 모르면 다른 DNS 서버에 물어 답을 찾아오는 일을 맡을 수 있습니다. 공유기가 중간에 질의를 전달하는 설정도 있지만, 공유기 자체가 언제나 최종 답을 찾아내는 것은 아닙니다.

기억할 한 줄: **내 컴퓨터는 지정된 DNS 서버에 먼저 질의하고, 그 서버가 답을 돌려준다.**

<!-- source: 외워서네트워크 lesson-31.md; 혼자공부하는네트워크 05-1 DNS와 자원, pp.260–262 -->

## 지정된 DNS 서버는 담당 서버를 따라 답을 찾는다

<!-- learn-page-id: dns-delegation -->

지정된 DNS 서버가 요청받은 이름의 답을 모르면 여러 DNS 서버에 차례로 물어볼 수 있습니다. 예를 들어 `www.example.com`을 찾을 때 루트 DNS 서버는 `.com`을 맡은 서버를 알려주고, `.com` 서버는 `example.com`을 맡은 DNS 서버를 알려줍니다. 마지막으로 `example.com`의 담당 DNS 서버가 `www.example.com`에 대한 답을 알려줍니다.

이처럼 어떤 도메인의 정보를 관리하도록 맡겨진 서버를 **담당 DNS 서버**라고 합니다. 다른 자료에서는 네임 서버 또는 권한 있는 DNS 서버라고도 부르지만, 여기서는 같은 역할을 가리키는 말로 이해하면 됩니다. 앞 단계의 서버는 보통 최종 IP 주소를 모두 알려주는 대신 다음에 물어볼 서버의 방향을 안내합니다.

기억할 한 줄: **답을 모르는 DNS 서버는 이름의 범위를 따라가며 그 이름을 맡은 담당 DNS 서버를 찾는다.**

<!-- source: 외워서네트워크 lesson-31.md; 혼자공부하는네트워크 05-1 DNS와 자원, pp.260–263 -->

## DNS 서버도 찾은 답을 잠시 기억한다

<!-- learn-page-id: dns-cache-ttl -->

DNS 서버는 한 번 찾은 답을 캐시에 보관해 같은 이름을 다시 물었을 때 더 빨리 답할 수 있습니다. 답을 무한정 보관하지는 않습니다. DNS 정보에는 TTL(Time To Live)이라는 시간이 설정되어 있고, 캐시는 그 시간이 지나면 답을 새로 확인해야 합니다.

예를 들어 TTL이 300초라면 DNS 서버는 그 답을 최대 300초 동안 캐시에 사용할 수 있습니다. TTL이 지난 뒤에는 오래된 주소를 계속 쓰지 않도록 다시 조회합니다. 따라서 한 사이트의 주소가 바뀌어도 모든 컴퓨터의 캐시가 같은 순간에 갱신되는 것은 아닙니다.

기억할 한 줄: **DNS 캐시는 조회를 빠르게 하고, TTL은 답을 기억할 시간을 정한다.**

<!-- source: 외워서네트워크 lesson-31.md; 혼자공부하는네트워크 05-1 DNS와 자원, pp.263–265 -->

## DNS에 문제가 생기면 이름으로 접속하기 어렵다

<!-- learn-page-id: dns-failures -->

DNS 서버가 응답하지 않거나 잘못된 주소를 돌려주면 브라우저는 사이트 이름으로 목적지 주소를 알아내지 못할 수 있습니다. 이름 조회에 실패해도 네트워크와 웹 서버가 모두 고장 났다고 바로 결론 내릴 수는 없습니다. 먼저 이름을 주소로 바꾸는 단계에서 문제가 생겼는지, 주소를 얻은 뒤 연결하는 단계에서 문제가 생겼는지 나누어 봐야 합니다.

컴퓨터나 네트워크에는 기본(주) DNS 서버 외에 보조 DNS 서버를 설정할 수 있습니다. 기본 서버에 문제가 있을 때 보조 서버가 응답을 도울 수 있지만, 보조 서버가 있다고 모든 접속 문제가 해결되는 것은 아닙니다. 또 잘못된 답을 보내 속이는 DNS 변조가 일어나면 서버 응답 자체가 정상처럼 보여도 엉뚱한 곳으로 연결될 수 있으므로 답의 출처와 네트워크 상태를 함께 확인해야 합니다.

기억할 한 줄: **사이트 이름이 열리지 않으면 DNS 조회와 그 뒤의 연결을 나누어 살펴본다.**

<!-- source: 외워서네트워크 lesson-31.md; 혼자공부하는네트워크 05-1 DNS와 자원, pp.265–266 -->
