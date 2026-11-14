---
id: u8-advanced-11-symmetric-nat-방식
title: '답장은 어떻게 제자리로 돌아올까: NAT 변환표'
source_lesson_ids:
- u8-advanced-11-symmetric-nat-방식
- u8-advanced-15-포트-포워딩
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-11.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-15.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b01
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b02
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b06
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b09
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b10
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b14
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p200-b03
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p200-b08
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p200-b12
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p200-b14
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p200-b15
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p201-b02
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p201-b03
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p201-b08
- https://www.rfc-editor.org/rfc/rfc3022.html
- https://www.rfc-editor.org/rfc/rfc4787.html
- https://www.rfc-editor.org/rfc/rfc5382.html
- https://www.rfc-editor.org/rfc/rfc5737.html
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-11.md
page_metadata:
- page_id: advanced-source-11-page-01
  questions:
  - id: u12-l02-p01-q01
    kind: choice
    difficulty: easy
    prompt: '`192.168.10.41:3000`에서 `:3000`이 뜻하는 것은 무엇인가?'
    choices:
    - id: a
      text: 공유기가 접속을 기다리는 서비스 포트
      feedback: 3000은 지우 PC가 요청을 보낼 때 고른 번호다. 공유기와는 상관이 없다.
    - id: b
      text: 그 PC 안에서 이 통신을 구별하는 포트 번호
      feedback: 맞다. 주소가 기기를 가리킨다면 포트는 그 기기 안에서 통신을 구별하는 창구 번호다.
    - id: c
      text: AI API 서버가 제공하는 서비스의 종류(HTTPS)
      feedback: 서비스 포트는 목적지의 `443`이다. 3000은 출발지 쪽 번호다.
    - id: d
      text: PC의 서브넷 마스크를 줄여 쓴 값
      feedback: 서브넷 마스크는 `/24` 같은 별도의 정보다. `:3000`은 포트다.
    - id: e
      text: 통신이 끊기기 전까지 허용된 시간(초)
      feedback: 포트 번호는 시간과 무관한 구별용 번호다.
    answer: b
    feedback: '`주소:포트`는 어느 기기의 어느 창구인지를 함께 가리키는 표기이고, 변환표의 한 줄도 이 짝으로 적힌다.'
  - id: u12-l02-p01-q02
    kind: choice
    difficulty: medium
    prompt: 공유기 관리 화면에는 LAN `192.168.10.1`과 WAN `198.51.100.25`가 보이고, 디자인팀 PC `192.168.10.43:51515`가 이미지 생성 API를 호출한다. 이 요청이 공유기를 나갈 때 바꿔야 할 '출발지'로 알맞은 것은?
    choices:
    - id: a
      text: 공유기 자신의 LAN 주소 `192.168.10.1`과 포트 51515
      feedback: 공유기의 LAN 주소는 변환 대상이 아니다. 변환되는 것은 통신을 시작한 기기의 값이다.
    - id: b
      text: 공유기의 WAN 주소 `198.51.100.25`
      feedback: WAN 주소는 바뀐 뒤에 바깥에서 보이는 값이다. 바뀌기 전의 출발지는 아니다.
    - id: c
      text: 이미지 생성 API 서버의 주소
      feedback: API 서버는 목적지다. 목적지는 그대로 두고 출발지만 바꾼다.
    - id: d
      text: 통신을 시작한 PC의 `192.168.10.43:51515`
      feedback: 맞다. 변환 대상은 공유기가 아니라 통신을 시작한 기기의 주소와 포트다.
    - id: e
      text: LAN 주소와 WAN 주소 둘 다
      feedback: 두 주소는 공유기가 가진 값이고, 바뀌기 전 출발지는 PC의 값이다.
    answer: d
    feedback: '🧩 쪼개기: ''공유기가 가진 주소''와 ''통신을 시작한 기기의 주소''를 나누면 무엇이 바뀌는 칸인지 분명해진다.'
  question_placements:
  - question_id: u12-l02-p01-q01
    after_paragraph: 2
- page_id: advanced-source-11-page-03
  questions:
  - id: u12-l02-p02-q01
    kind: choice
    difficulty: easy
    prompt: 공유기를 안쪽에서 바깥쪽으로 나가는 Outbound 패킷에서 NAT가 바꾸는 것은 무엇인가?
    choices:
    - id: a
      text: 출발지 주소(포트도 바뀔 수 있음)
      feedback: 맞다. 출발지를 바꾸고 목적지는 그대로 둔다. 그래야 서버가 공유기 바깥 주소로 응답할 수 있다.
    - id: b
      text: 목적지 주소와 목적지 포트
      feedback: 목적지를 바꾸면 요청이 엉뚱한 곳으로 간다. 목적지는 그대로 둔다.
    - id: c
      text: 패킷에 실린 질문 내용
      feedback: NAT는 주소와 포트만 바꾸고 실린 내용은 건드리지 않는다.
    - id: d
      text: 사용하는 프로토콜(TCP를 UDP로)
      feedback: 프로토콜은 바뀌지 않는다.
    - id: e
      text: 출발지와 목적지의 주소 모두
      feedback: 목적지 주소는 바뀌지 않는다.
    answer: a
    feedback: Outbound에서는 출발지만 바꾸고, 바꾼 짝을 표에 기록해 응답을 되돌릴 수 있게 한다.
  - id: u12-l02-p02-q02
    kind: choice
    difficulty: medium
    prompt: 디자인팀 PC(`192.168.10.43:4000`)가 음성 받아쓰기 API(`203.0.113.90:443`)에 요청한다. 공유기를 지난 바깥쪽 패킷에서 값이 바뀌어 있는 칸은?
    choices:
    - id: a
      text: 목적지 주소와 목적지 포트
      feedback: 목적지는 바뀌지 않는다.
    - id: b
      text: 어느 칸도 바뀌지 않고 안쪽과 똑같다
      feedback: 바뀌지 않으면 사설 주소가 인터넷으로 나가게 되어 응답이 돌아올 수 없다.
    - id: c
      text: 출발지 주소와 목적지 주소 두 칸
      feedback: 출발지만 바뀌고 목적지 주소는 그대로다.
    - id: d
      text: 프로토콜과 패킷 길이
      feedback: 프로토콜과 길이는 이 변환에서 바뀌지 않는다.
    - id: e
      text: 출발지 주소(와 출발지 포트)
      feedback: 맞다. 목적지는 그대로이고 출발지가 공유기 바깥 주소로 바뀐다.
    answer: e
    feedback: '📋 순서대로 확인하기: 안쪽 → 공유기 → 바깥쪽 순으로 출발지와 목적지 칸을 한 줄씩 비교하면 바뀐 곳이 보인다.'
  question_placements:
  - question_id: u12-l02-p02-q01
    after_paragraph: 3
- page_id: advanced-source-11-page-05
  questions:
  - id: u12-l02-p03-q01
    kind: choice
    difficulty: easy
    prompt: 외부 AI 서비스 서버가 접속 기록에 남기는 출발지 주소는 무엇인가?
    choices:
    - id: a
      text: 직원 PC의 사설 주소 `192.168.10.41`
      feedback: 사설 주소는 인터넷으로 나오기 전에 바뀌므로 서버에는 닿지 않는다.
    - id: b
      text: 직원이 로그인한 이름
      feedback: 이름은 IP 주소가 아니라 애플리케이션이 따로 주고받는 정보다.
    - id: c
      text: NAT를 지난 공유기 바깥 주소와 포트
      feedback: 맞다. 서버가 보는 것은 NAT가 바꿔 단 바깥 주소와 포트다.
    - id: d
      text: GPU PC의 주소 `192.168.10.50`
      feedback: GPU PC는 이 접속과 관계가 없고, 사설 주소는 서버에 보이지 않는다.
    - id: e
      text: 공유기 안쪽 주소 `192.168.10.1`
      feedback: 공유기의 안쪽 주소도 사설 주소라 서버에 보이지 않는다.
    answer: c
    feedback: 서버가 보는 출발지는 NAT 뒤의 바깥 주소·포트이고, 사람 구별은 계정·키·쿠키가 맡는다.
  - id: u12-l02-p03-q02
    kind: choice
    difficulty: medium
    prompt: AI API 업체가 "접속을 허용할 IP를 등록하라"고 안내했다. 지우가 등록할 주소로 알맞은 것은?
    choices:
    - id: a
      text: 지우 PC의 주소 `192.168.10.41`
      feedback: 사설 주소는 업체 서버에 보이지 않아 등록해도 소용없다.
    - id: b
      text: 공유기 바깥 주소 `198.51.100.25`
      feedback: 맞다. 업체 서버가 보는 출발지가 이 주소이므로 이것을 등록해야 한다.
    - id: c
      text: 공유기의 안쪽 주소 `192.168.10.1`
      feedback: 안쪽 주소도 사설 주소라 업체 서버가 볼 수 없다.
    - id: d
      text: API 서버 자신의 주소 `203.0.113.80`
      feedback: 접속을 허용할 대상은 우리 쪽 출발지이고, 서버 주소가 아니다.
    - id: e
      text: 직원 PC 사설 주소 40개를 모두 등록한다
      feedback: 사설 주소는 서버에 닿지 않고, 하나만 등록하면 되는 편리함도 사라진다.
    answer: b
    feedback: '🧩 쪼개기: ''내 PC가 쓰는 주소''와 ''서버가 보는 주소''를 나누면 어느 주소를 등록해야 하는지 보인다.'
  question_placements:
  - question_id: u12-l02-p03-q01
    after_paragraph: 2
- page_id: advanced-source-11-page-06
  questions:
  - id: u12-l02-p04-q01
    kind: choice
    difficulty: easy
    prompt: NAT 변환표의 Local 칸에 적히는 값으로 알맞은 것은 무엇인가?
    choices:
    - id: a
      text: 공유기 자신의 LAN 주소 `192.168.10.1`과 포트 51515
      feedback: Local은 공유기 주소가 아니라 통신을 시작한 기기의 값이다.
    - id: b
      text: 통신 상대인 서버의 주소와 포트
      feedback: 그것은 Remote 칸이다.
    - id: c
      text: 바깥에서 보이는 공유기 주소와 포트
      feedback: 그것은 External 칸이다.
    - id: d
      text: 관리자가 지정한 규칙의 이름
      feedback: 변환표 열은 주소와 포트를 적는 칸이고, 규칙의 이름이 아니다.
    - id: e
      text: 변환 전, 통신을 시작한 내부 기기의 주소와 포트
      feedback: 맞다. Local은 안쪽에서 통신을 시작한 기기의 값이다.
    answer: e
    feedback: Local은 안쪽 기기, Remote는 통신 상대, External은 바깥에서 보이는 값이다.
  - id: u12-l02-p04-q02
    kind: choice
    difficulty: medium
    prompt: 오래 켜 둔 원격 접속 프로그램이 한동안 아무것도 주고받지 않다가 갑자기 끊겼다. 변환표 관점에서 가장 그럴듯한 원인은?
    choices:
    - id: a
      text: 자동으로 만든 행이 유휴 시간이 지나 지워졌다
      feedback: 맞다. 자동 행은 연결이 끝나거나 유휴 시간이 지나면 사라질 수 있다.
    - id: b
      text: External 포트 번호가 너무 커서 공유기가 끊었다
      feedback: 포트 번호의 크기 때문에 끊기는 것이 아니다.
    - id: c
      text: 공유기가 Local 주소를 공유기 LAN 주소로 바꿔 버렸다
      feedback: Local은 통신을 시작한 기기의 값이고, 임의로 바뀌지 않는다.
    - id: d
      text: 원격 접속 프로그램은 NAT 뒤에서는 반드시 끊어진다
      feedback: 바깥으로 나가는 연결은 NAT 뒤에서도 정상적으로 유지된다.
    - id: e
      text: 누군가 고정 규칙을 지웠기 때문이다
      feedback: 고정 규칙은 원격 접속이 안쪽에서 시작한 연결과 관계가 없다.
    answer: a
    feedback: '🧩 쪼개기: ''자동 행''과 ''고정 규칙''을 나누면 오래 쉰 연결이 끊긴 이유가 유휴 시간 쪽에 있음을 알 수 있다.'
  question_placements:
  - question_id: u12-l02-p04-q01
    after_paragraph: 3
- page_id: advanced-source-11-page-07
  questions:
  - id: u12-l02-p05-q01
    kind: choice
    difficulty: easy
    prompt: Inbound, 곧 바깥에서 안쪽으로 응답이 돌아올 때 NAT가 바꾸는 것은 무엇인가?
    choices:
    - id: a
      text: 출발지 주소를 공유기 LAN 주소 `192.168.10.1`로 바꾼다
      feedback: 출발지는 그대로 둔다. 응답의 출발지는 AI API 서버다.
    - id: b
      text: 출발지와 목적지를 모두 지운다
      feedback: 주소를 지우면 전달할 수 없다.
    - id: c
      text: 목적지를 DNS로 다시 조회한다
      feedback: DNS는 이 과정에 쓰이지 않는다. 변환표만 본다.
    - id: d
      text: 목적지 주소와 포트를 변환표의 Local 값으로 되돌린다
      feedback: 맞다. 나갈 때 바꾼 출발지를 응답에서는 목적지로 되돌린다.
    - id: e
      text: 아무것도 바꾸지 않고 모든 PC에 복사해 보낸다
      feedback: 변환표로 한 곳을 정해서 보낸다.
    answer: d
    feedback: Inbound에서는 External로 행을 찾아 목적지를 Local 값으로 되돌린다. 출발지는 그대로다.
  - id: u12-l02-p05-q02
    kind: choice
    difficulty: medium
    prompt: 지우가 공유기를 재부팅한 직후, 재부팅 전에 보낸 AI 요청의 응답이 도착했다. 재부팅으로 자동 행이 지워졌다면 이 응답은 어떻게 될까?
    choices:
    - id: a
      text: 공유기가 지우 PC를 추측해 전달한다
      feedback: 공유기는 추측하지 않는다. 변환표에 적힌 대응만 쓴다.
    - id: b
      text: 안쪽 모든 PC에 복사해서 보낸다
      feedback: 여러 PC에 복사해 보내지 않는다. 행이 없으면 전달하지 않는다.
    - id: c
      text: 대응하는 행이 없어서 안쪽으로 전달되지 못하고 버려진다
      feedback: 맞다. 나갈 때 적어 둔 기록이 없으면 돌아온 패킷을 보낼 곳을 알 수 없다.
    - id: d
      text: 서버가 요청을 취소하고 새 행이 자동으로 만들어진다
      feedback: 행은 안쪽에서 나가는 요청이 만든다. 서버의 응답으로는 생기지 않는다.
    - id: e
      text: '`192.168.10.1`이 응답을 대신 받아 지우 PC에 넘긴다'
      feedback: 공유기 LAN 주소는 이 응답의 대응 상대가 아니다.
    answer: c
    feedback: '📋 순서대로 확인하기: ''나갈 때 기록 → 올 때 조회'' 순서에서 기록이 사라지면 조회가 실패한다.'
  question_placements:
  - question_id: u12-l02-p05-q01
    after_paragraph: 3
- page_id: advanced-source-11-page-09
  questions:
  - id: u12-l02-p06-q01
    kind: choice
    difficulty: easy
    prompt: 두 PC가 같은 서버에 동시에 요청해도 응답이 섞이지 않는 까닭은 무엇인가?
    choices:
    - id: a
      text: PC마다 서로 다른 공인 IP를 배정하기 때문이다
      feedback: 공인 주소는 하나이고, 그것을 함께 쓴다.
    - id: b
      text: 서버가 응답할 때 PC의 이름을 물어보기 때문이다
      feedback: 서버는 PC의 이름을 묻지 않는다. 주소와 포트만 본다.
    - id: c
      text: 먼저 요청한 PC에게만 응답이 가고 나머지는 다시 요청해야 한다
      feedback: 동시에 요청해도 각각 응답을 받는다.
    - id: d
      text: 응답이 모든 PC로 가고 각 PC가 자기 것만 골라 쓴다
      feedback: 공유기가 행으로 한 곳을 정해서 보낸다.
    - id: e
      text: 같은 바깥 IP를 쓰더라도 External 포트와 변환표 행이 달라서 응답을 구별할 수 있다
      feedback: 맞다. 주소는 같아도 포트와 행이 다르므로 응답이 각자의 PC로 간다.
    answer: e
    feedback: NAPT는 같은 바깥 주소에 External 포트를 달리 붙여 통신을 구별한다.
  - id: u12-l02-p06-q02
    kind: choice
    difficulty: medium
    prompt: 변환표에 `192.168.10.43:51000`↔`:53011`, `192.168.10.44:51000`↔`:53012`, `192.168.10.45:52000`↔`:53013`이 있다. 이미지 생성 API의 응답이 `198.51.100.25:53012`로 도착했다. 이 응답이 가야 할 PC는?
    choices:
    - id: a
      text: '`192.168.10.44`'
      feedback: 맞다. 응답의 목적지 포트 `53012`를 External 칸에서 찾으면 `.44`의 행이다.
    - id: b
      text: '`192.168.10.43`. 내부 포트가 같은 51000이라서'
      feedback: 내부 포트가 같아도 응답은 External 포트로 찾는다. `53012`는 `.44`의 행이다.
    - id: c
      text: '`192.168.10.45`'
      feedback: '`.45`의 External 포트는 `53013`이다.'
    - id: d
      text: 세 PC 모두에 보낸다
      feedback: 행을 찾아 한 곳으로 보낸다.
    - id: e
      text: 정할 수 없어서 버린다
      feedback: External 포트로 행을 하나 찾을 수 있다.
    answer: a
    feedback: '🔁 같은 모양 찾기: 응답의 목적지는 나갈 때 출발지를 거꾸로 읽은 것이므로, 같은 행을 반대 방향에서 찾으면 된다.'
  question_placements:
  - question_id: u12-l02-p06-q01
    after_paragraph: 3
- page_id: advanced-source-15-page-01
  illustrations:
  - file: assets/animations/u12-fwd-auto-review.svg
    title: 자동 매핑은 안에서 시작할 때만
    alt: 안쪽 PC가 먼저 바깥 서버에 접속하면 변환표에 자동으로 기록되지만, 바깥에서 먼저 오면 기록이 없어 막힌다는 그림입니다.
    caption: 나갈 때 적은 기록이 있어야 응답이 들어옵니다.
    after_paragraph: 0
  questions:
  - id: u12-l02-p07-q01
    kind: choice
    difficulty: easy
    prompt: 바깥에서 먼저 도착한 요청이 공유기에서 전달되지 못하는 까닭으로 알맞은 것은 무엇인가?
    choices:
    - id: a
      text: 공유기가 8080번 포트를 쓰지 못하게 제조사가 막아 두어서
      feedback: 제조사가 막은 것이 아니라 행이 없어서 전달할 곳을 모르는 것이다.
    - id: b
      text: 그 요청에 맞는 변환표 행이 없어서 어느 안쪽 기기로 보낼지 모른다
      feedback: 맞다. 자동 행은 안쪽에서 나갈 때 만들어지므로 바깥에서 먼저 온 요청에는 행이 없다.
    - id: c
      text: 공인 주소로는 사설 주소 기기에 패킷을 보낼 수 없다는 규칙 때문에
      feedback: 주소 규칙이 아니라 대응하는 기록이 없다는 문제다.
    - id: d
      text: GPU PC가 외부 요청을 거부하도록 기본 설정되어 있어서
      feedback: 요청은 GPU PC에 도달하기 전에 공유기에서 멈춘다.
    - id: e
      text: 응답이 너무 늦게 와서 행이 지워졌기 때문에
      feedback: 요청이 먼저 온 상황이라 지워질 행이 애초에 없다.
    answer: b
    feedback: 자동 행은 안에서 시작한 통신만 만들므로, 바깥에서 먼저 오는 요청은 사람이 미리 적은 줄이 있어야 전달된다.
  - id: u12-l02-p07-q02
    kind: choice
    difficulty: medium
    prompt: 고객사가 납품 도면을 사무실 PC로 '밀어 넣는' 방식은 계속 실패하고, 사무실 PC가 고객사 서버에서 도면을 '가져오는' 방식은 성공한다. 차이를 만든 원인은?
    choices:
    - id: a
      text: 가져올 때만 도면 파일 용량이 허용되기 때문이다
      feedback: 용량의 차이가 아니라 연결을 시작한 방향의 차이다.
    - id: b
      text: 고객사 서버가 사설 주소를 쓰고 있기 때문이다
      feedback: 그렇다면 두 방식 모두 실패해야 한다. 방향이 다르다.
    - id: c
      text: 가져오는 방식은 암호화되고 밀어 넣는 방식은 평문이기 때문이다
      feedback: 암호화 여부로 NAT 행이 만들어지지 않는다.
    - id: d
      text: 누가 먼저 연결을 시작했는가. 안쪽에서 시작해야 행이 생긴다
      feedback: 맞다. 가져오는 방식은 안쪽에서 연결을 시작해 행이 생기고, 밀어 넣는 방식은 행이 없다.
    - id: e
      text: 공유기가 업로드와 다운로드 속도를 다르게 제한하기 때문이다
      feedback: 속도 제한이 아니라 행의 유무 문제다.
    answer: d
    feedback: '📋 순서대로 확인하기: 누가 먼저 시작했는지, 그때 기록이 생겼는지 순서대로 따라가면 방향의 차이가 원인임이 보인다.'
  question_placements:
  - question_id: u12-l02-p07-q01
    after_paragraph: 2
---
## AI API의 답장은 어떻게 내 PC를 찾을까?

<!-- learn-page-id: advanced-source-11-page-01 -->

디자인팀 PC 여러 대가 동시에 외부 AI API에 시안 설명을 요청해도 답이 서로 섞이지 않는다. 그런데 박 팀장이 바깥에서 공유기 주소로 보낸 요청은 공유기에서 사라졌다. 이 두 현상은 공유기 안의 표 하나, NAT 변환표로 함께 설명된다. 먼저 쉬운 쪽부터 따라가 보자. 지우 PC(`192.168.10.41`)가 외부 AI API(`203.0.113.80:443`)를 부르면 답은 공유기 바깥 주소 `198.51.100.25`로 온다. 지우 PC의 사설 주소는 인터넷에서 쓸 수 없는데, 답은 어떻게 지우 PC까지 올까?

먼저 표기부터 짚자. `주소:포트`는 편지 봉투에 건물 주소와 호수를 함께 적는 것과 같다. 주소는 어느 기기인지를, 포트는 그 기기 안의 어느 창구인지를 가리킨다. `192.168.10.41:3000`은 지우 PC의 3000번 창구이고, `203.0.113.80:443`은 AI API 서버의 HTTPS 창구다. 3000은 지우 PC의 운영체제가 요청마다 임시로 고르는 번호이고, 443은 서버가 서비스를 받는 번호다.

지우 PC는 인터넷 쪽 목적지로 가는 패킷을 기본 게이트웨이, 곧 공유기 `192.168.10.1`에 넘긴다. 공유기는 안쪽과 바깥쪽의 경계에 서 있어서 이곳을 지나는 패킷의 주소를 바꿀 수 있다. 이때 바꾸는 대상은 공유기 자신의 주소가 아니라 통신을 시작한 기기의 주소와 포트다. 이 점이 뒤의 변환표를 읽을 때 헷갈리기 쉬운 부분이다.

그래서 이 Lesson에서는 변환표 한 줄을 처음부터 끝까지 따라가 본다. 요청이 나가는 길에서 무엇이 바뀌고 무엇이 기록되는지, 응답이 돌아오는 길에서 그 기록이 어떻게 쓰이는지를 차례로 볼 것이다. 한 줄만 제대로 읽으면 나머지 줄도 똑같이 읽힌다.

## 공유기를 나설 때 패킷의 무엇이 바뀔까?

<!-- learn-page-id: advanced-source-11-page-03 -->

지우 PC가 `203.0.113.80:443`으로 요청을 보냈다. 공유기 안쪽에서 이 패킷을 보면 출발지가 `192.168.10.41:3000`인데, 공유기 바깥쪽에서 보면 `198.51.100.25:53001`로 달라져 있다. 같은 요청인데 숫자가 다르다. 도대체 어디가 바뀐 것일까?

우편물을 생각해 보자. 직원이 쓴 편지의 보내는 사람 칸을 회사 대표 주소와 접수번호로 고쳐 쓰고, 받는 사람 칸은 그대로 두어 내보낸다. NAT도 이렇게 한다. 패킷이 안쪽에서 바깥쪽으로 나가는 방향을 Outbound라고 부르는데, 이때 공유기는 출발지 주소 `192.168.10.41`을 바깥 주소 `198.51.100.25`로 바꾼다. 여러 통신이 같은 바깥 주소를 함께 쓰므로 응답을 구별하려고 출발지 포트도 공유기가 정한 번호로 바꿀 수 있다. 이 예에서는 `3000`이 `53001`이 되었다.

| 구간 | 출발지 | 목적지 |
| --- | --- | --- |
| 공유기 안쪽 | `192.168.10.41:3000` | `203.0.113.80:443` |
| 공유기 바깥쪽 | `198.51.100.25:53001` | `203.0.113.80:443` |

표에서 바뀐 것은 출발지뿐이고 목적지인 서버의 주소와 서비스 포트는 그대로다. 그래서 서버는 사설 주소를 몰라도 `198.51.100.25:53001`로 응답할 수 있다. 한 가지 주의할 점은 `53001`이 공유기가 그 포트에서 접속을 기다린다는 뜻이 아니라는 것이다. 응답을 구별하려고 장비가 적어 두는 번호일 뿐이며, 장비에 따라 원래 포트를 그대로 둘 수도 있다.

그리고 이렇게 바꾸는 것만으로는 부족하다. 바뀐 짝, 곧 `192.168.10.41:3000`과 `198.51.100.25:53001`의 대응을 공유기가 표에 적어 둬야 나중에 응답이 왔을 때 원래 PC를 찾을 수 있다. 다음 Page들에서 그 표를 읽는 법을 본다.

## AI 서비스는 누가 접속했다고 볼까?

<!-- learn-page-id: advanced-source-11-page-05 -->

외부 AI API 관리 화면을 열어 본 서 이사가 고개를 갸웃한다. 접속 기록의 출발지가 직원 전원 똑같이 `198.51.100.25`로 찍혀 있다. "이 IP로 누가 썼는지 알 수 있나요? 도면을 올린 사람이 누구인지요."

회사 대표 전화로 걸려 온 통화 기록을 떠올리자. 기록에는 대표번호만 남고, 내선 몇 번 직원이 걸었는지는 상대방 통신사가 모른다. AI 서비스 서버도 마찬가지다. 서버가 보는 출발지는 NAT를 지난 뒤의 바깥 주소와 포트다. 지우 PC의 `192.168.10.41`은 인터넷에 나오지 못하므로 서버에는 한결디자인 공유기에서 왔다는 정보까지만 닿는다.

그러면 사용자는 무엇으로 구별할까? IP가 아니라 로그인 계정, API 키, 쿠키처럼 애플리케이션이 따로 주고받는 정보다. 서 이사가 알고 싶은 "누가 썼나"는 IP가 아니라 이 정보로 답해야 한다. IP는 어디서 왔는지, 곧 한결디자인 회선 쪽이라는 것만 알려 준다. 결국 서버 기록의 IP는 회사 단위의 흔적일 뿐 직원 단위의 흔적이 아니다. 사람별 사용 내역을 남기고 싶다면 직원마다 계정이나 키를 발급해야 한다.

AI 서비스 중에는 접속을 허용할 IP를 미리 등록하게 하는 곳이 있다. 이때는 직원 PC 주소를 일일이 적을 필요 없이 회사 바깥 주소 `198.51.100.25` 하나만 등록하면 되어 편하다. 대신 대가가 따른다. IP로는 직원을 구별할 수 없으니 사람별 키나 계정을 따로 써야 하고, 회선 계약에 따라 바깥 주소가 바뀌면 허용 목록도 고쳐야 한다. 고정 IP인지 확인하는 이유다.

## 변환표 한 줄에는 무엇이 적힐까?

<!-- learn-page-id: advanced-source-11-page-06 -->

공유기 관리 화면에서 NAT 세션 목록을 열어 본 지우는 열 이름이 낯설다. Local, Remote, External. 무엇이 어디에 적히는지 알아야 문제가 생겼을 때 표를 읽을 수 있다. 택배 접수 대장에 비유하면 이해가 쉽다. 대장 한 줄에는 보낸 사람, 받을 곳, 그리고 회사 대표 접수번호가 적힌다.

변환표 한 줄도 이렇게 세 가지를 잇는다. Local은 변환 전의 내부 기기 주소와 포트, Remote는 통신 상대의 주소와 포트, External은 바깥에서 보이는 주소와 포트다. Local이 공유기 자신의 LAN 주소가 아니라 통신을 시작한 기기의 값이라는 점에 주의하자.

| 프로토콜 | Local | Remote | External |
| --- | --- | --- | --- |
| TCP | `192.168.10.41:3000` | `203.0.113.80:443` | `198.51.100.25:53001` |

실제 매핑은 Local과 External을 잇는다. Remote 열은 어떤 상대와 통신 중인지 알려 주고, 필터링이 상대를 가리는 방식일 때 수신 허용 조건으로 쓰인다. 장비에 따라 화면의 열 이름과 배치는 다를 수 있으니 이름을 외우기보다 각 값이 어느 쪽에 있는지를 묻자. 안쪽 기기인가, 통신 상대인가, 바깥에서 보이는 값인가.

또 하나 알아 둘 것이 있다. 이 줄은 통신 중에 자동으로 만들어진 행이라 연결이 끝나거나 유휴 시간이 지나면 사라진다. UDP처럼 끝내는 절차가 없는 통신은 장비의 타이머가 더 중요하다. 반면 관리자가 직접 적어 넣은 고정 규칙은 자동 행과 다르게 다뤄진다. 두 종류를 구별해서 읽어야 한다.

## 돌아온 답장은 어느 PC로 갈까?

<!-- learn-page-id: advanced-source-11-page-07 -->

AI API 서버가 응답을 보낸다. 이 응답의 목적지는 지우 PC의 사설 주소가 아니라 `198.51.100.25:53001`이다. 응답을 보내는 쪽은 사설 주소를 알 수 없고 알 필요도 없다. 그러면 공유기는 이 응답을 어떻게 지우 PC로 돌려보낼까?

택배 회신을 생각해 보자. 회신 봉투에는 대표 접수번호 53001이 적혀 있고, 안내 데스크는 접수 대장에서 그 번호를 찾아 보낸 직원에게 돌려준다. 공유기가 하는 일도 같은 순서다. 먼저 응답의 목적지 주소·포트로 변환표의 External 칸을 찾는다. 찾으면 필터링 규칙, 곧 어느 출발지에서 온 패킷을 받을지에 대한 조건을 적용한다(마지막 Lesson에서 자세히 본다). 통과하면 목적지를 Local 값 `192.168.10.41:3000`으로 되돌려 안쪽으로 보낸다. 이 방향을 Inbound라고 한다.

| 구간 | 출발지 | 목적지 |
| --- | --- | --- |
| 공유기 바깥쪽 | `203.0.113.80:443` | `198.51.100.25:53001` |
| 공유기 안쪽 | `203.0.113.80:443` | `192.168.10.41:3000` |

표에서 보듯 Inbound에서 바뀌는 것은 목적지이고 출발지는 그대로다. 나갈 때 출발지를 바꾼 것을 응답이 올 때 목적지에서 거꾸로 되돌리는 셈이다.

여기서 중요한 점이 하나 있다. 이 되돌림은 나갈 때 적어 둔 기록이 있어야만 가능하다. 지우가 공유기를 재부팅하면 자동 행이 모두 사라질 수 있고, 그 직후에 재부팅 전에 보낸 요청의 응답이 도착하면 공유기는 찾을 행이 없다. 기록이 없으면 돌아온 패킷을 보낼 곳도 없다.

## 동시에 물어도 답이 왜 안 섞일까?

<!-- learn-page-id: advanced-source-11-page-09 -->

지우 PC(`192.168.10.41`)와 디자인팀 PC(`192.168.10.43`)가 같은 외부 AI API에 동시에 요청을 보낸다. 서버가 보는 출발지 주소는 둘 다 `198.51.100.25`로 똑같다. 그런데도 응답은 서로 섞이지 않고 각자의 PC로 간다. 어떻게 구별하는 걸까?

같은 대표번호로 걸어도 접수번호가 다르면 대장에서 구별된다. 공유기도 두 통신에 서로 다른 External 포트를 붙여 구별한다. 두 줄을 함께 놓고 보면 이렇다.

| 프로토콜 | Local | Remote | External |
| --- | --- | --- | --- |
| TCP | `192.168.10.41:3000` | `203.0.113.80:443` | `198.51.100.25:53001` |
| TCP | `192.168.10.43:4000` | `203.0.113.80:443` | `198.51.100.25:53002` |

주소는 같지만 External 포트가 `53001`과 `53002`로 다르다. 응답이 `:53002`로 오면 두 번째 줄을 찾아 `192.168.10.43:4000`으로 돌려보낸다. 이렇게 주소와 포트를 함께 변환해 바깥 주소 하나를 여러 PC가 나눠 쓰게 하는 방식을 NAPT(또는 PAT)라고 한다. 혼공네트 04-1이 포트 기반 NAT라고 소개한 방식이 바로 이것이고, 일반 공유기의 N:1 공유가 이렇게 가능하다.

포트 번호는 TCP, UDP 각각 65,536개뿐이라 한 바깥 주소로 동시에 유지할 수 있는 변환 행에는 한계가 있다. 40명 규모의 사무실에서는 여유가 넘친다. 바깥 주소 하나를 아끼는 대신 지는 대가다.

## 박 팀장의 요청은 왜 공유기에서 사라질까?

<!-- learn-page-id: advanced-source-15-page-01 -->

지우가 이번에는 공유기 바깥 주소를 알려 줬다. 박 팀장이 고객사에서 `198.51.100.25:8080`으로 접속해 보지만 여전히 열리지 않는다. 이제 요청은 우리 공유기에 분명히 도착하는데도 AI 서버 화면은 나타나지 않는다. 지우는 앞에서 익힌 변환표로 이 문제를 풀어 보기로 한다.

지금까지 본 변환표의 줄은 모두 안쪽 PC가 먼저 요청을 보낼 때 공유기가 자동으로 만든 것이다. 박 팀장의 요청은 반대로 바깥에서 먼저 도착한다. 이 요청에 맞는 행은 어디에도 없다. 공유기는 이것을 GPU PC(`192.168.10.50`)로 보내야 할지, 지우 PC로 보내야 할지 알 수 없으므로 전달하지 않고 버린다.

안내 데스크 비유로 돌아가면, 대장에는 안쪽 직원이 먼저 연락한 손님만 적혀 있다. 박 팀장이 찾아온다는 기록은 없으니 안내 데스크는 어느 방으로 보낼지 모른다. 대장에 적는 사람은 지금까지 안내 데스크 자신이었지만, 바깥에서 먼저 찾아오는 손님은 안쪽에서 연락한 적이 없으니 자동으로 적을 기회가 없다.

첫 Lesson에서 NAT는 방화벽처럼 일부러 막는 것이 아니라고 했다. 막는 규칙이 아니라 갈 곳을 몰라서 못 가는 것이므로, 갈 곳을 알려 주는 줄 하나만 있으면 길이 열린다. 길이 열린다는 것은 곧 노출이 된다는 뜻이기도 해서, 그 대가는 다음 Lesson에서 따진다.

해결은 간단하다. 그 줄을 사람이 미리 적어 두면 된다. "바깥 8080으로 오는 요청은 `192.168.10.50:8080`으로 보내라"는 한 줄을 공유기에 넣는 것이다. 이것이 포트 포워딩이고, 다음 Lesson에서 직접 해 본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 변환표는 Local(통신을 시작한 내부 기기), Remote(통신 상대), External(바깥에서 보이는 주소·포트)을 이어 응답을 제자리로 돌려보낸다. 자동 행은 안쪽에서 먼저 시작한 통신만 만든다.
- **적용하기 (Apply):** 요청이 나갈 때와 응답이 돌아올 때를 한 칸씩 따라가며 응답의 목적지 포트로 External 칸을 찾아 Local로 읽는다. 외부 서비스의 IP 허용 목록에는 공유기 바깥 주소를 쓰되, 사람 구별은 계정·키로 한다.
- **찾아보기 (Lookup):** 공유기 관리 화면의 NAT 세션(변환표) 메뉴와 유휴 시간 설정, NAPT의 정의(혼공네트 04-1, RFC 3022)는 필요할 때 직접 찾아본다.

### 🧠 이번에 쓴 생각법

- 📋 **순서대로 확인하기**: 요청이 나갈 때와 응답이 돌아올 때를 한 칸씩 따라가며 어디서 기록이 생기고 어디서 쓰이는지 확인했다.
- 🧩 **쪼개기**: 변환표를 Local·Remote·External으로 나누고, 공유기가 가진 주소와 통신을 시작한 기기의 주소를 구별했다.
- 🔁 **같은 모양 찾기**: 나갈 때는 출발지를, 돌아올 때는 목적지를 바꾸는 것이 같은 줄을 거꾸로 읽는 일임을 알아보았다.
