---
id: u8-advanced-11-symmetric-nat-방식
title: NAT 변환표로 통신 따라가기
source_lesson_ids:
- u8-advanced-11-symmetric-nat-방식
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-11.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b02
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b09
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b10
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p199-b14
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p200-b03
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p200-b08
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/04-1.md#p200-b12
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
  question_placements:
  - question_id: u12-l02-p01-q01
    after_paragraph: 1
  - question_id: u12-l02-p01-q02
    after_paragraph: 2
  questions:
  - id: u12-l02-p01-q01
    kind: choice
    difficulty: easy
    prompt: NAT 변환표는 무엇을 연결해 두는 기록인가요?
    choices:
    - id: a
      text: 외부 웹 서버와 그 서버가 쓰는 포트만
      feedback: 외부 상대만으로는 안쪽의 어느 통신에 응답을 보낼지 알 수 없습니다. 안쪽과 바깥쪽 통신을 연결해야 합니다.
    - id: b
      text: 집 안 모든 기기와 같은 사설 주소 하나
      feedback: 여러 기기의 통신이 섞이지 않도록 각각의 안쪽 통신과 바깥쪽 통신을 연결합니다.
    - id: c
      text: 서버가 직접 관리하는 집 안 사설 주소 목록
      feedback: 변환표는 공유기나 NAT 장비가 안쪽과 바깥쪽 통신을 연결해 두는 기록입니다. 서버가 관리하는 내부 주소 목록이 아닙니다.
    - id: d
      text: 안쪽 통신과 바깥에서 보이는 통신
      feedback: 맞아요. 요청 때 만든 대응 기록을 이용해 응답을 원래 안쪽 기기로 돌려보냅니다.
    - id: e
      text: 응답이 올 때마다 내부 기기를 새로 고르는 순서
      feedback: 응답마다 기기를 새로 고르는 것이 아니라 요청 때 만든 대응 기록을 찾아 원래 안쪽 기기로 돌려보냅니다.
    answer: d
  - id: u12-l02-p01-q02
    kind: choice
    difficulty: medium
    prompt: 192.168.0.10:3000이라는 표기에서 3000의 의미와 NAT 처리에 대한 설명으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 3000은 포트이며 NAT는 주소와 함께 포트도 바꿔 기록할 수 있습니다
      feedback: 맞아요. 콜론 뒤 숫자는 포트이며, NAT는 주소뿐 아니라 포트도 변환해 통신을 구별할 수 있습니다.
    - id: b
      text: 3000은 IP 주소의 마지막 부분이며 포트는 따로 없습니다
      feedback: IPv4 주소는 콜론 앞의 192.168.0.10입니다. 콜론 뒤 3000은 포트 번호입니다.
    - id: c
      text: 3000은 포트이며 NAT는 어떤 경우에도 포트를 바꾸지 않습니다
      feedback: 본문은 NAT가 IP뿐 아니라 TCP·UDP 통신을 구별하는 포트도 바꿔 기록할 수 있다고 설명합니다.
    - id: d
      text: 3000은 접속한 기기 수이며 NAT는 기기 수를 변환합니다
      feedback: 콜론 뒤 숫자는 기기 수가 아니라 해당 IP에서 통신을 구별하는 포트입니다.
    - id: e
      text: 3000은 전송 순서이며 NAT는 이 순서만 기록합니다
      feedback: 3000은 패킷 순서가 아니라 포트입니다. NAT는 안쪽과 바깥쪽의 주소·포트 관계를 기록합니다.
    answer: a
  illustrations:
  - file: assets/diagrams/source-11.svg
    title: Lesson의 11개 페이지 학습 흐름
    alt: NAT 변환표 소개부터 요청과 응답, 여러 PC의 통신 구별, Local·Remote·External 정리까지 11개 학습 단계를 제목과 화살표로 보여 주는 흐름도
    caption: NAT 변환표를 읽는 11개 주제가 어떤 순서로 이어지는지 보여 준다.
    after_paragraph: -1
- page_id: advanced-source-11-page-02
  question_placements:
  - question_id: u12-l02-p02-q01
    after_paragraph: 1
  - question_id: u12-l02-p02-q02
    after_paragraph: 3
  questions:
  - id: u12-l02-p02-q01
    kind: choice
    difficulty: easy
    prompt: 이 예에서 노트북이 기본 게이트웨이로 이용하는 것은 무엇인가요?
    choices:
    - id: a
      text: 사설 주소가 192.168.0.10인 노트북 자신
      feedback: 192.168.0.10은 통신을 시작하는 노트북입니다. 예시의 기본 게이트웨이는 공유기입니다.
    - id: b
      text: 외부 웹 서버 203.0.113.80
      feedback: 웹 서버는 통신 상대입니다. 집 안 노트북이 먼저 이용하는 기본 게이트웨이는 공유기입니다.
    - id: c
      text: 안쪽 주소가 192.168.0.1인 공유기
      feedback: 맞아요. 노트북은 공유기를 다음 길을 알려 주는 기본 게이트웨이로 이용합니다.
    - id: d
      text: 공유기를 건너뛴 인터넷 회사 장비
      feedback: 본문의 노트북은 공유기를 거쳐 ISP 쪽으로 이동합니다. 공유기를 건너뛰는 예시가 아닙니다.
    - id: e
      text: 집 안의 다른 노트북
      feedback: 본문은 다른 노트북이 아니라 안쪽 주소 192.168.0.1인 공유기를 기본 게이트웨이로 가정합니다.
    answer: c
  - id: u12-l02-p02-q02
    kind: choice
    difficulty: medium
    prompt: 이 Page의 네트워크 예시를 읽을 때 옳은 해석은 무엇인가요?
    choices:
    - id: a
      text: 두 문서용 주소에 접속하면 실제 예시 서버를 사용할 수 있습니다
      feedback: 198.51.100.25와 203.0.113.80은 문서 예시용 주소이며 실제 서비스 접속 주소가 아닙니다.
    - id: b
      text: 공유기 바깥 주소와 웹 서버 주소는 같은 위치의 주소입니다
      feedback: 바깥 주소는 공유기 쪽, 웹 서버 주소는 외부 통신 상대 쪽입니다. 위치를 구분해야 합니다.
    - id: c
      text: 모든 실제 가정에는 공유기와 통신사 NAT가 각각 하나씩 있습니다
      feedback: 이 예시는 공유기 하나이며 추가 통신사 NAT가 없다고 가정합니다. 모든 가정을 일반화하지 않습니다.
    - id: d
      text: 노트북은 공유기를 거치지 않고 문서용 서버로 바로 나갑니다
      feedback: 본문의 패킷은 노트북에서 공유기로, 공유기에서 ISP 쪽으로 이동합니다.
    - id: e
      text: 문서용 주소로 공유기 하나와 통신사 추가 NAT가 없는 구성을 설명합니다
      feedback: 맞아요. 바깥 주소와 서버 주소는 예시용이며, 이 Page는 추가 NAT가 없는 단순한 구성을 가정합니다.
    answer: e
- page_id: advanced-source-11-page-03
  question_placements:
  - question_id: u12-l02-p03-q01
    after_paragraph: 1
  - question_id: u12-l02-p03-q02
    after_paragraph: 3
  questions:
  - id: u12-l02-p03-q01
    kind: choice
    difficulty: easy
    prompt: 이 Page의 PC가 처음 만든 요청 패킷에서 출발지와 목적지는 무엇인가요?
    choices:
    - id: a
      text: 출발지 203.0.113.80:443, 목적지 192.168.0.10:3000
      feedback: 요청은 PC에서 서버로 갑니다. 두 값을 반대로 놓으면 요청의 방향이 바뀝니다.
    - id: b
      text: 출발지 192.168.0.10:3000, 목적지 203.0.113.80:443
      feedback: 맞아요. PC가 고른 출발지 포트와 서버의 HTTPS 목적지 포트를 구별해야 합니다.
    - id: c
      text: 출발지 192.168.0.10:443, 목적지 203.0.113.80:3000
      feedback: 예시에서 PC의 출발지 포트는 3000이고 서버의 목적지 포트는 443입니다.
    - id: d
      text: 출발지 192.168.0.10:3000, 목적지 192.168.0.10:443
      feedback: 목적지는 PC 자신이 아니라 외부 서버 203.0.113.80입니다.
    - id: e
      text: 출발지 203.0.113.80:3000, 목적지 203.0.113.80:443
      feedback: 출발지 IP는 요청을 시작하는 PC의 192.168.0.10입니다.
    answer: b
  - id: u12-l02-p03-q02
    kind: choice
    difficulty: medium
    prompt: PC가 HTTPS 서버에 접속하려는데 출발지 포트가 3000입니다. 서버 포트 443과 다르므로 잘못된 연결일까요?
    choices:
    - id: a
      text: 맞습니다. HTTPS라면 양쪽 포트가 반드시 443이어야 합니다
      feedback: 443은 이 예에서 서버가 받는 목적지 포트입니다. PC의 출발지 포트까지 같아야 하지는 않습니다.
    - id: b
      text: 맞습니다. 서버가 자신의 서비스 포트를 3000으로 바꿔야 합니다
      feedback: PC의 출발지 포트와 서버의 서비스 포트는 역할이 다릅니다. 이 예의 서버는 443을 사용합니다.
    - id: c
      text: 아닙니다. IP만 있으면 어느 통신인지 구별되므로 포트는 필요 없습니다
      feedback: 본문은 IP가 기기를, 포트가 기기 안의 통신을 구별한다고 설명합니다. 포트는 함께 기록해야 합니다.
    - id: d
      text: 아닙니다. 출발지와 서비스 포트는 역할이 달라 서로 달라도 됩니다
      feedback: 맞아요. 운영체제가 고른 출발지 포트가 서버 서비스 포트와 같아야 하는 것은 아닙니다.
    - id: e
      text: 맞습니다. PC는 서버와 같은 IP와 포트를 사용해야 합니다
      feedback: 출발지와 목적지는 서로 다른 기기와 통신을 가리킬 수 있습니다. 같은 IP·포트여야 하는 규칙은 아닙니다.
    answer: d
- page_id: advanced-source-11-page-04
  question_placements:
  - question_id: u12-l02-p04-q01
    after_paragraph: 1
  - question_id: u12-l02-p04-q02
    after_paragraph: 3
  questions:
  - id: u12-l02-p04-q01
    kind: choice
    difficulty: easy
    prompt: 이 Page에서 Outbound는 어느 방향의 패킷 이동인가요?
    choices:
    - id: a
      text: 공유기 안쪽에서 바깥쪽으로 나가는 이동
      feedback: 맞아요. 이 방향에서 예시의 출발지 주소와 필요한 경우 포트를 바꿉니다.
    - id: b
      text: 공유기 바깥쪽에서 안쪽으로 들어오는 이동
      feedback: Outbound는 안쪽에서 바깥쪽으로 나가는 방향입니다.
    - id: c
      text: 공유기를 거치지 않는 내부 PC끼리의 이동
      feedback: 본문에서 Outbound는 공유기의 안쪽과 바깥쪽 경계를 넘어 나가는 이동을 가리킵니다.
    - id: d
      text: 웹 서버 내부에서만 이루어지는 이동
      feedback: 이 Page는 웹 서버 내부가 아니라 공유기 안쪽에서 바깥쪽으로 나가는 패킷을 설명합니다.
    - id: e
      text: 공유기 안쪽과 바깥쪽의 모든 방향 이동
      feedback: Outbound는 모든 방향을 한꺼번에 부르는 말이 아니라 바깥으로 나가는 방향입니다.
    answer: a
  - id: u12-l02-p04-q02
    kind: choice
    difficulty: medium
    prompt: 표에서 출발지가 198.51.100.25:53001로 바뀐 요청을 어떻게 읽어야 하나요?
    choices:
    - id: a
      text: 서버의 서비스 포트도 443에서 53001로 바뀌었습니다
      feedback: 표의 목적지 203.0.113.80:443은 그대로입니다. 바뀐 것은 출발지 포트입니다.
    - id: b
      text: 공유기에서 53001 포트로 앱이 접속을 기다린다는 뜻입니다
      feedback: 본문은 배정된 변환 포트가 앱처럼 접속을 기다린다는 뜻은 아니라고 설명합니다.
    - id: c
      text: 출발지만 변환되었고 서버 목적지 203.0.113.80:443은 그대로입니다
      feedback: 맞아요. 53001은 이 예의 변환 포트이며, 공유기 앱의 대기 포트나 서버 포트를 뜻하지 않습니다.
    - id: d
      text: 요청의 목적지가 공유기의 바깥쪽 주소로 바뀌었습니다
      feedback: 공유기 바깥 주소는 변환 후 출발지입니다. 요청 목적지는 웹 서버입니다.
    - id: e
      text: IP만 바뀌었고 출발지 포트 3000은 그대로 남았습니다
      feedback: 이 예의 표에서는 출발지 포트도 3000에서 53001로 바뀌었습니다.
    answer: c
- page_id: advanced-source-11-page-05
  question_placements:
  - question_id: u12-l02-p05-q01
    after_paragraph: 1
  - question_id: u12-l02-p05-q02
    after_paragraph: 3
  questions:
  - id: u12-l02-p05-q01
    kind: choice
    difficulty: easy
    prompt: 웹 서버가 이 요청 패킷의 출발지로 보는 값은 무엇인가요?
    choices:
    - id: a
      text: 192.168.0.10:3000
      feedback: 이 값은 변환 전 내부 통신입니다. 서버는 NAT를 지난 바깥쪽 출발지를 봅니다.
    - id: b
      text: 198.51.100.25:3000
      feedback: 바깥 IP는 맞지만 예시에서는 출발지 포트도 53001로 변환되었습니다.
    - id: c
      text: 203.0.113.80:443
      feedback: 이 값은 요청을 받는 서버의 목적지이지, 서버가 보는 요청의 출발지가 아닙니다.
    - id: d
      text: 192.168.0.10:53001
      feedback: 내부 IP와 변환 후 포트를 섞었습니다. 서버가 보는 출발지는 바깥 IP와 변환 포트의 조합입니다.
    - id: e
      text: 198.51.100.25:53001
      feedback: 맞아요. 서버에 도착하기 전에 NAT가 출발지 주소와 포트를 바꿨습니다.
    answer: e
  - id: u12-l02-p05-q02
    kind: choice
    difficulty: medium
    prompt: 같은 NAT 바깥 주소로 접속한 두 사용자를 웹 서비스가 반드시 같은 사람으로 판단할까요?
    choices:
    - id: a
      text: 그렇습니다. 같은 바깥 IP면 로그인 정보도 항상 같습니다
      feedback: 같은 바깥 IP가 같은 로그인 사용자를 뜻하지 않습니다. 로그인 정보는 별도로 구별할 수 있습니다.
    - id: b
      text: 아닙니다. 로그인 정보나 쿠키 등으로 사용자를 구별할 수 있습니다
      feedback: 맞아요. 패킷의 출발지 정보와 서비스가 사용자를 식별하는 방법은 구별해야 합니다.
    - id: c
      text: 그렇습니다. NAT를 지나면 쿠키도 모두 같은 값이 됩니다
      feedback: 본문은 쿠키 같은 다른 방법으로 사용자를 구별할 수 있다고 설명합니다. NAT가 쿠키를 같게 만든다는 뜻이 아닙니다.
    - id: d
      text: 아닙니다. 서버는 패킷 출발지에서 두 기기의 사설 IP를 직접 봅니다
      feedback: 서버가 패킷에서 보는 출발지는 NAT 바깥쪽 정보입니다. 사용자 구별에는 로그인·쿠키 등을 쓸 수 있습니다.
    - id: e
      text: 그렇습니다. 서버 포트 443을 함께 쓰면 같은 사용자입니다
      feedback: 443은 서버의 서비스 포트입니다. 같은 서비스에 접속한다고 같은 사용자가 되지는 않습니다.
    answer: b
- page_id: advanced-source-11-page-06
  question_placements:
  - question_id: u12-l02-p06-q01
    after_paragraph: 3
  - question_id: u12-l02-p06-q02
    after_paragraph: 5
  questions:
  - id: u12-l02-p06-q01
    kind: choice
    difficulty: easy
    prompt: 표의 External 열에 적힌 198.51.100.25:53001은 무엇을 나타내나요?
    choices:
    - id: a
      text: 내부 PC의 원래 주소와 포트
      feedback: 원래 내부 통신은 Local 열의 192.168.0.10:3000입니다.
    - id: b
      text: 외부 웹 서버의 주소와 서비스 포트
      feedback: 외부 상대는 Remote 열의 203.0.113.80:443입니다. External과 구분해야 합니다.
    - id: c
      text: 이 통신이 바깥에서 보이는 주소와 포트
      feedback: 맞아요. External은 내부 통신이 NAT를 지난 뒤 바깥에서 어떻게 보이는지 나타냅니다.
    - id: d
      text: 공유기 안쪽 기기 전체가 똑같이 사용하는 통신 값
      feedback: 바깥 IP가 같아도 포트와 기록으로 여러 통신을 구별합니다. 모든 통신이 같은 값인 것은 아닙니다.
    - id: e
      text: 인터넷 전체가 공동으로 관리하는 기기 등록 정보
      feedback: NAT 변환표는 해당 NAT 장비가 내부적으로 유지하는 대응표입니다.
    answer: c
  - id: u12-l02-p06-q02
    kind: choice
    difficulty: medium
    prompt: 통신 중 자동으로 만들어진 NAT 변환 행은 언제까지 남는다고 이해하면 좋을까요?
    choices:
    - id: a
      text: 통신 방식과 장비의 시간 조건에 따라 사라질 수 있습니다
      feedback: 맞아요. 자동 변환 행은 통신 방식과 장비의 시간 조건에 따라 사라질 수 있습니다. 사용자가 등록한 포트 포워딩 같은 고정 규칙과는 구별해야 합니다.
    - id: b
      text: 한 번 기록되면 어떤 경우에도 영구히 남습니다
      feedback: 자동으로 만들어진 변환 행은 정리될 수 있지만, 사용자가 등록한 고정 규칙은 다르게 취급합니다.
    - id: c
      text: 모든 장비에서 같은 시간 뒤에 반드시 지워집니다
      feedback: 제거 시점은 통신 방식과 장비에 따라 다릅니다. 모든 장비가 같은 시간을 쓰지는 않습니다.
    - id: d
      text: 요청을 내보내는 즉시 지워지므로 응답에는 쓸 수 없습니다
      feedback: 응답이 돌아올 때 맞는 기록을 찾도록 연결 상태를 유지합니다. 요청 직후 무조건 지우는 기록이 아닙니다.
    - id: e
      text: 인터넷 전체 목록에 옮긴 뒤 공유기에서는 유지하지 않습니다
      feedback: 인터넷 전체가 공유하는 목록이 아니라 해당 장비가 내부적으로 유지하는 기록입니다.
    answer: a
- page_id: advanced-source-11-page-07
  question_placements:
  - question_id: u12-l02-p07-q01
    after_paragraph: 1
  - question_id: u12-l02-p07-q02
    after_paragraph: 3
  questions:
  - id: u12-l02-p07-q01
    kind: choice
    difficulty: easy
    prompt: 이 예에서 웹 서버가 돌려보낸 응답의 목적지는 무엇인가요?
    choices:
    - id: a
      text: 192.168.0.10:3000
      feedback: 인터넷에서 노트북의 사설 주소로 직접 돌아가는 것이 아니라 NAT 바깥 주소로 응답합니다.
    - id: b
      text: 203.0.113.80:443
      feedback: 이 값은 응답의 출발지인 웹 서버입니다. 목적지와 방향을 구별해야 합니다.
    - id: c
      text: 198.51.100.25:443
      feedback: 공유기 바깥 IP는 맞지만 응답 목적지 포트는 서버 포트 443이 아니라 변환 포트 53001입니다.
    - id: d
      text: 198.51.100.25:53001
      feedback: 맞아요. 서버는 요청 때 바깥에 보였던 주소·포트를 응답 목적지로 삼습니다.
    - id: e
      text: 192.168.0.10:53001
      feedback: 사설 IP와 바깥 변환 포트를 섞었습니다. 인터넷으로 돌아오는 응답은 바깥 주소·포트를 향합니다.
    answer: d
  - id: u12-l02-p07-q02
    kind: choice
    difficulty: medium
    prompt: 외부 상대(Remote)까지 허용 조건에 넣는 필터링 규칙이 있다면, 목적지는 맞지만 다른 서버에서 온 패킷도 통과할까요?
    choices:
    - id: a
      text: 그렇습니다. 바깥 목적지 IP만 맞으면 상대는 확인하지 않습니다
      feedback: 이 예시의 필터링 규칙은 외부 상대 주소와 포트까지 확인합니다.
    - id: b
      text: 아닙니다. 허용된 Remote와 다르면 패킷을 통과시키지 않을 수 있습니다
      feedback: 맞아요. 목적지에 맞는 변환 행이 있어도 필터링 규칙이 허용한 외부 상대와 다르면 통과하지 않을 수 있습니다. 매핑과 필터링은 별개의 기준입니다.
    - id: c
      text: 그렇습니다. 바깥 목적지 포트만 같으면 어떤 서버든 같은 응답입니다
      feedback: 이 예의 필터링 규칙은 목적지 포트뿐 아니라 외부 상대도 확인합니다.
    - id: d
      text: 아닙니다. NAT는 서버에서 돌아온 응답을 전부 막습니다
      feedback: 기록과 맞는 응답은 처리할 수 있습니다. 문제는 외부 통신 전체가 아니라 맞는 행을 찾는 조건입니다.
    - id: e
      text: 그렇습니다. 행이 없으면 아무 내부 기기에 새로 배정합니다
      feedback: 이 상황에서는 행이 있는지와 별도로, 필터링 규칙이 외부 상대를 확인하는지를 살펴야 합니다. 임의로 다른 기기에 보내지는 않습니다.
    answer: b
- page_id: advanced-source-11-page-08
  question_placements:
  - question_id: u12-l02-p08-q01
    after_paragraph: 1
  - question_id: u12-l02-p08-q02
    after_paragraph: 3
  questions:
  - id: u12-l02-p08-q01
    kind: choice
    difficulty: easy
    prompt: 일치하는 변환표 행을 찾은 Inbound 처리에서는 응답 패킷의 어느 정보를 바꾸나요?
    choices:
    - id: a
      text: 서버 출발지 주소·포트를 내부 PC 주소·포트로 바꿉니다
      feedback: Inbound의 이 예는 목적지를 바꾸며, 응답 출발지인 서버 정보는 그대로 둡니다.
    - id: b
      text: 서버 출발지와 바깥쪽 목적지를 서로 맞바꿉니다
      feedback: 방향을 뒤집는 것이 아니라 목적지를 변환표의 내부 주소·포트로 복원합니다.
    - id: c
      text: 응답 목적지를 서버 주소·포트로 바꿉니다
      feedback: 응답은 서버로 되돌아가는 것이 아니라 원래 내부 PC로 전달되어야 합니다.
    - id: d
      text: 아무 정보도 바꾸지 않고 바깥쪽 목적지를 유지합니다
      feedback: 내부 PC로 보내기 위해 바깥 목적지 198.51.100.25:53001을 내부 목적지로 되돌립니다.
    - id: e
      text: 바깥쪽 목적지 주소·포트를 원래 내부 목적지로 바꿉니다
      feedback: 맞아요. 응답이 원래 PC에 도착하도록 목적지를 복원하고 서버 출발지는 그대로 둡니다.
    answer: e
  - id: u12-l02-p08-q02
    kind: choice
    difficulty: medium
    prompt: 요청이 나갈 때와 응답이 돌아올 때 NAT 처리를 함께 설명한 것으로 맞는 것은 무엇인가요?
    choices:
    - id: a
      text: 요청과 응답 모두 출발지만 바꾸며 서로 다른 기록을 임의로 씁니다
      feedback: 이 예에서는 요청의 출발지와 응답의 목적지가 바뀌고 같은 변환 기록을 이용합니다.
    - id: b
      text: 요청 때만 바꾸고 기록하지 않아도 응답을 원래 PC로 보낼 수 있습니다
      feedback: 요청 때 만든 기록이 있어야 돌아온 응답을 어느 PC에 연결할지 판단할 수 있습니다.
    - id: c
      text: 요청의 출발지와 응답의 목적지를 같은 변환 기록으로 연결합니다
      feedback: 맞아요. 나갈 때와 돌아올 때 바꾸는 쪽은 다르지만 같은 기록으로 하나의 통신을 이어 줍니다.
    - id: d
      text: 요청과 응답 모두 목적지만 바꾸며 서버를 내부 PC로 교체합니다
      feedback: 요청 때에는 출발지를, 응답 때에는 목적지를 바꿉니다. 서버를 다른 기기로 교체하는 흐름이 아닙니다.
    - id: e
      text: 응답마다 새 내부 PC를 골라 이전 요청과 무관하게 전달합니다
      feedback: 응답은 요청과 무관하게 나누지 않습니다. 같은 기록으로 원래 내부 통신에 연결합니다.
    answer: c
- page_id: advanced-source-11-page-09
  question_placements:
  - question_id: u12-l02-p09-q01
    after_paragraph: 2
  - question_id: u12-l02-p09-q02
    after_paragraph: 3
  questions:
  - id: u12-l02-p09-q01
    kind: choice
    difficulty: easy
    prompt: 표의 두 PC 통신이 바깥에서 함께 사용하는 값은 무엇인가요?
    choices:
    - id: a
      text: IP 주소 198.51.100.25
      feedback: 맞아요. 바깥 IP는 함께 쓰지만 포트 53001과 53002 및 변환표 행은 다릅니다.
    - id: b
      text: 포트 번호 53001
      feedback: 첫 통신은 53001, 둘째는 53002이므로 바깥 포트는 다릅니다.
    - id: c
      text: 포트 번호 53002
      feedback: 53002는 두 번째 통신의 바깥 포트입니다. 첫 번째는 53001을 사용합니다.
    - id: d
      text: IP와 포트를 합친 198.51.100.25:53001
      feedback: 두 통신이 공유하는 것은 바깥 IP입니다. 두 번째 통신의 포트는 53002입니다.
    - id: e
      text: IP와 포트를 합친 198.51.100.25:53002
      feedback: 이 조합은 두 번째 통신입니다. 첫 번째의 바깥 포트는 53001입니다.
    answer: a
  - id: u12-l02-p09-q02
    kind: choice
    difficulty: medium
    prompt: 웹 서버의 응답이 198.51.100.25:53002로 돌아왔다면, 표에 따라 어디로 전달해야 하나요?
    choices:
    - id: a
      text: 첫 번째 PC의 192.168.0.10:3000
      feedback: 첫 번째 PC는 바깥 포트 53001에 대응합니다. 53002는 두 번째 행을 찾아야 합니다.
    - id: b
      text: 두 번째 PC의 192.168.0.11:53002
      feedback: 53002는 바깥 포트입니다. 안쪽으로 전달할 때는 기록의 원래 포트 4000을 사용합니다.
    - id: c
      text: 첫 번째 PC의 192.168.0.10:4000
      feedback: 첫 번째 IP와 두 번째 포트를 섞었습니다. 53002의 행 전체를 따라가야 합니다.
    - id: d
      text: 두 PC 모두의 내부 주소와 포트
      feedback: 같은 바깥 IP라도 변환표 행으로 구별합니다. 두 기기에 모두 전달하는 방식이 아닙니다.
    - id: e
      text: 두 번째 PC의 192.168.0.11:4000
      feedback: 맞아요. 53002에 대응하는 변환표 행을 따라 두 번째 PC의 원래 통신으로 보냅니다.
    answer: e
- page_id: advanced-source-11-page-10
  question_placements:
  - question_id: u12-l02-p10-q01
    after_paragraph: 2
  - question_id: u12-l02-p10-q02
    after_paragraph: 4
  questions:
  - id: u12-l02-p10-q01
    kind: choice
    difficulty: easy
    prompt: 이 Page의 표에서 Local은 같은데 외부 서버가 달라졌을 때 달라지는 값은 무엇인가요?
    choices:
    - id: a
      text: 내부 PC의 IP가 192.168.0.10에서 다른 IP로 바뀝니다
      feedback: 표의 두 행은 내부 IP가 모두 192.168.0.10입니다. 외부 상대와 바깥 포트가 다릅니다.
    - id: b
      text: 바깥 포트가 53001과 53003으로 달라집니다
      feedback: 맞아요. 이 예시는 같은 내부 통신도 외부 상대에 따라 별도 바깥 매핑을 사용할 수 있음을 보여 줍니다.
    - id: c
      text: 내부 출발지 포트가 3000에서 443으로 바뀝니다
      feedback: Local은 두 행 모두 192.168.0.10:3000입니다. 443은 두 서버의 서비스 포트입니다.
    - id: d
      text: 공유기의 바깥 IP가 두 개로 나뉩니다
      feedback: 두 행의 바깥 IP는 모두 198.51.100.25이고 바깥 포트가 달라집니다.
    - id: e
      text: 서버의 서비스 포트가 443에서 3000으로 바뀝니다
      feedback: 서버 주소는 다르지만 표의 Remote 서비스 포트는 두 행 모두 443입니다.
    answer: b
  - id: u12-l02-p10-q02
    kind: choice
    difficulty: medium
    prompt: 이 Symmetric NAT 예시를 실제 장비에 적용할 때 알맞은 판단은 무엇인가요?
    choices:
    - id: a
      text: 다음 연결은 모든 NAT에서 반드시 53004를 사용합니다
      feedback: 본문은 포트 숫자가 예시일 뿐 실제 장비가 순서대로 배정하지는 않는다고 설명합니다.
    - id: b
      text: 이 이름이면 모든 현대 NAT의 동작과 보안 수준이 같습니다
      feedback: 옛 유형 이름은 모든 장비의 실제 동작이나 보안 수준을 나타내는 보편적 등급이 아닙니다.
    - id: c
      text: 바깥 포트를 정하는 방식만 알면 수신 허용 조건도 확정됩니다
      feedback: 주소·포트를 정하는 매핑과 외부 패킷을 받아들이는 필터링은 구분해야 합니다.
    - id: d
      text: 예시 숫자를 일반화하지 않고 매핑과 필터링을 나누어 봅니다
      feedback: 맞아요. 포트가 순서대로 배정된다는 보장도, 옛 유형 이름이 모든 장비 동작을 대표한다는 보장도 없습니다.
    - id: e
      text: TCP와 UDP의 NAT 요구사항은 프로토콜과 무관하게 모두 같습니다
      feedback: 본문은 TCP와 UDP의 요구사항이 프로토콜별 표준 문서에서 설명된다고 안내합니다. 이름만으로 같다고 단정하지 않습니다.
    answer: d
- page_id: advanced-source-11-page-11
  question_placements:
  - question_id: u12-l02-p11-q01
    after_paragraph: 1
  - question_id: u12-l02-p11-q02
    after_paragraph: 4
  questions:
  - id: u12-l02-p11-q01
    kind: choice
    difficulty: easy
    prompt: 이 Lesson에서 NAT 표의 Remote는 어느 쪽을 가리키나요?
    choices:
    - id: a
      text: 공유기 안쪽 기기와 그 통신 포트
      feedback: 공유기 안쪽의 원래 통신은 이 Lesson에서 Local이라고 부릅니다.
    - id: b
      text: NAT 뒤 바깥에서 보이는 주소와 포트
      feedback: 바깥에서 보이는 통신은 External입니다. Remote는 통신 상대 서버입니다.
    - id: c
      text: 통신 상대인 외부 서버와 그 포트
      feedback: 맞아요. Remote는 상대 서버이고, Local은 내부 기기, External은 바깥에 보이는 통신입니다.
    - id: d
      text: 공유기를 이용하는 모든 내부 기기의 주소 묶음
      feedback: Remote는 내부 기기 목록이 아니라 요청이 향하는 외부 상대 서버와 포트입니다.
    - id: e
      text: 공유기와 외부 서버의 주소를 합친 하나의 IP
      feedback: 표는 서로 다른 위치의 값을 나눠 적습니다. Remote는 외부 서버와 그 포트입니다.
    answer: c
  - id: u12-l02-p11-q02
    kind: choice
    difficulty: medium
    prompt: 제품 화면의 열 순서가 이 Lesson의 표와 다릅니다. 요청과 응답의 연결을 확인하는 적절한 방법은 무엇인가요?
    choices:
    - id: a
      text: 각 값의 위치 역할을 확인하고 기록된 Local·Remote·External 관계를 따라갑니다
      feedback: 맞아요. 제품마다 이름·배치가 달라도 내부 통신, 상대, 바깥 매핑의 관계로 읽으면 응답 경로를 찾을 수 있습니다.
    - id: b
      text: 열 순서는 항상 같으므로 첫 열을 무조건 Local로 읽습니다
      feedback: 본문은 제품마다 용어와 열 배치가 다를 수 있다고 설명합니다. 값이 어느 쪽인지 확인해야 합니다.
    - id: c
      text: 같은 바깥 IP를 쓰는 모든 Local을 하나의 내부 통신으로 합칩니다
      feedback: 여러 Local이 하나의 바깥 IP를 공유할 수 있지만, 포트와 상대를 포함한 기록으로 통신을 나눕니다.
    - id: d
      text: Remote를 내부 PC로 보고 그 서버 주소를 집 안 목적지로 씁니다
      feedback: Remote는 외부 상대입니다. 응답은 기록의 관계를 반대로 따라 Local 통신으로 전달합니다.
    - id: e
      text: External 포트만 외우고 상대와 내부 값은 버립니다
      feedback: 변환표는 세 값의 관계를 기록합니다. 내부 통신과 상대를 버리면 응답이 어디로 연결되는지 읽기 어렵습니다.
    answer: a
---

## 주소와 포트를 함께 바꾸기

<!-- learn-page-id: advanced-source-11-page-01 -->

NAT 변환표는 공유기나 NAT 장비가 통신의 안쪽 주소와 바깥 주소를 어떻게 연결했는지 적어 두는 기록이다. 요청이 바깥으로 나갈 때 이 기록을 만들고, 응답이 돌아올 때 기록을 찾아 안쪽 기기에 돌려보낸다. 장비는 이 기록이 있어야 여러 기기의 통신을 섞지 않고 처리할 수 있다.

이번 Lesson에서는 집 안 PC `192.168.0.10`이 외부 웹 서버 `203.0.113.80`에 접속하는 예를 따라간다. IPv4 주소 뒤의 콜론과 숫자는 포트 번호다. 예를 들어 `192.168.0.10:3000`은 IP 주소 `192.168.0.10`의 포트 `3000`을 뜻한다. NAT는 IP 주소뿐 아니라 TCP나 UDP 통신을 구별하는 포트도 함께 바꿔 기록할 수 있다.

이번 Lesson에서는 같은 내부 기기가 접속하는 외부 상대에 따라 바깥쪽 주소·포트 연결이 달라질 수 있는 변환표 예시를 따라간다. 과거 자료에서는 이런 동작을 Symmetric NAT라고 부르기도 했다. 이 이름이 모든 공유기의 동작을 대표하는 것은 아니다. 여기서는 변환표를 읽는 한 가지 예로만 살펴보고, 여러 NAT 동작을 구분하는 기준은 다음 Lesson에서 설명한다.

**기억할 점:** NAT 변환표는 안쪽의 통신과 바깥쪽에 보이는 통신을 이어 주는 기록이다.

## 내부 사설망과 외부 공인망

<!-- learn-page-id: advanced-source-11-page-02 -->

공유기 안쪽에는 집 안 기기가 연결된 내부 네트워크가 있고, 바깥쪽은 인터넷 서비스 제공자(ISP)를 거쳐 인터넷으로 이어진다. 노트북 `192.168.0.10`은 공유기 안에서 쓰는 사설 주소다. 공유기의 안쪽 주소를 `192.168.0.1`이라고 가정하면, 노트북은 이 공유기를 다음 길을 알려 주는 기본 게이트웨이로 이용한다.

공유기의 바깥쪽 주소는 ISP가 연결에 배정한다. NAT 변환표에서 Local은 보통 변환 전 내부 기기의 통신 주소·포트를, External은 변환 뒤 바깥에서 보이는 주소·포트를 가리킨다. 여기서 Local은 공유기 자체의 안쪽 주소 `192.168.0.1`이 아니라 노트북처럼 통신을 시작한 기기의 값이다. 이 예에서는 설명을 위해 `198.51.100.25`를 사용한다. 외부 웹 서버 주소 `203.0.113.80`도 예시용 주소다. 두 주소는 문서에서 예제로 쓰도록 예약된 대역의 주소이며 실제 서비스에 접속할 주소가 아니다. 집 안 기기 주소, 공유기 주소, 공유기의 바깥 주소, 웹 서버 주소가 서로 다른 위치의 값이라는 점을 구별하자.

밖으로 나가는 패킷은 노트북에서 공유기로, 공유기에서 ISP 쪽으로 이동한다. 주소 변환은 바로 이 경계에서 일어난다. 다만 이 예에서는 통신사 쪽에 추가 NAT가 없고 공유기가 하나라는 단순한 구성을 가정한다. 공유기 뒤에 통신사 NAT가 더 있을 수 있는 경우는 앞 Lesson에서 살펴봤다.

**기억할 점:** Local은 NAT 변환 전 내부 기기의 통신 주소·포트이고, External은 변환 뒤 바깥에서 보이는 주소·포트다. Local은 공유기 자체의 LAN 주소를 뜻하지 않는다.

## 내부 PC가 연결을 시작

<!-- learn-page-id: advanced-source-11-page-03 -->

웹 브라우저가 HTTPS 서버에 연결한다고 하자. 서버는 예시 주소 `203.0.113.80`의 포트 `443`에서 HTTPS 요청을 받는다. PC의 운영체제는 이 연결에 쓸 출발지 포트를 하나 고른다. 여기서는 설명을 위해 `3000`이라고 하자. PC에서 처음 만들어진 패킷에는 출발지 `192.168.0.10:3000`, 목적지 `203.0.113.80:443`이 적힌다.

IP 주소는 어느 기기와 통신하는지를 나타내고, 포트 번호는 그 기기 안의 어느 통신에 해당하는지를 구별하는 데 쓰인다. 노트북에서 브라우저가 여러 웹사이트에 동시에 접속할 때 각 통신에는 서로 다른 포트 조합이 사용될 수 있다. 따라서 NAT가 여러 통신을 구별하려면 안쪽 IP만 적어 두지 않고 포트도 함께 기록한다.

이때 `3000`은 예를 들어 든 출발지 포트이고, `443`은 HTTPS 서버가 주로 사용하는 목적지 포트다. 둘은 역할이 다르다. 또 웹 요청을 보낼 때 운영체제가 고른 출발지 포트가 서버가 제공하는 서비스의 포트와 같아야 하는 것은 아니다.

**기억할 점:** 패킷에는 출발지와 목적지가 있고, 양쪽 주소 뒤의 포트로 통신을 더 자세히 구별한다.

## Outbound · 출발지 주소·포트 변환

<!-- learn-page-id: advanced-source-11-page-04 -->

패킷이 공유기의 안쪽에서 바깥쪽으로 나가는 일을 Outbound라고 부른다. 공유기는 출발지 주소 `192.168.0.10`을 바깥쪽 주소 `198.51.100.25`로 바꾼다. 여러 안쪽 통신이 같은 바깥 IP를 함께 쓸 때는 응답을 각각의 통신에 돌려보낼 수 있도록 구별해야 한다. NAT 장비는 상황에 따라 출발지 포트를 그대로 유지하거나 다른 번호를 배정할 수 있다. 이 예에서는 `3000`을 `53001`로 바꿨다고 하자. `53001`은 이 예에서 장비가 배정한 번호일 뿐, 공유기가 그 포트에서 앱처럼 접속을 기다린다는 뜻은 아니다.

| 구간 | 출발지 | 목적지 |
| --- | --- | --- |
| 공유기 안쪽 | `192.168.0.10:3000` | `203.0.113.80:443` |
| 공유기 바깥쪽 | `198.51.100.25:53001` | `203.0.113.80:443` |

표에서 보듯 NAT가 바꾼 것은 요청의 출발지 주소와 포트다. 목적지인 웹 서버의 주소와 서비스 포트는 그대로다. 이 변환으로 인터넷 쪽에서는 사설 IP 주소 대신 공유기의 바깥 주소를 향해 응답할 수 있다.

**기억할 점:** Outbound에서는 안쪽 출발지 정보를 바깥에서 사용할 주소·포트로 바꾸고 그 짝을 기록한다.

## 웹 서버가 보는 접속 주체

<!-- learn-page-id: advanced-source-11-page-05 -->

웹 서버가 요청을 받았을 때 출발지로 보는 값은 `192.168.0.10:3000`이 아니라 `198.51.100.25:53001`이다. 요청은 이미 NAT를 거쳐 출발지 주소와 포트가 바뀌었기 때문이다. 그래서 웹 서버는 집 안의 노트북 주소를 직접 알지 못하고, 공유기 바깥에서 보이는 연결 정보를 이용해 응답을 보낸다.

이것은 웹 서버가 모든 사용자를 똑같은 한 사람으로 본다는 뜻은 아니다. 브라우저나 서비스는 로그인 정보나 웹 브라우저에 저장되어 다음 요청에 함께 보낼 수 있는 작은 정보인 쿠키 등으로 사용자를 구별할 수 있다. 여기서 확인하는 것은 IP 네트워크 경로에서 서버가 받은 패킷의 출발지 주소와 포트다.

또 “공유기가 포트를 바꿨다”는 말은 서버의 포트를 변경했다는 뜻이 아니다. 이 예에서 서버가 사용하는 목적지 포트 `443`은 그대로이고, 바뀐 것은 요청의 출발지 포트 `3000`이다. 어느 쪽 포트인지 혼동하지 않도록 출발지와 목적지를 함께 읽는다.

**기억할 점:** 서버는 NAT가 바깥쪽에 표시한 출발지 주소·포트를 본다.

## NAT Table에 남기는 기록

<!-- learn-page-id: advanced-source-11-page-06 -->

공유기는 안쪽 통신과 바깥에 보이는 통신을 이어 주는 매핑을 내부적으로 유지한다. 이 Lesson의 표에는 외부 상대도 함께 적어, 어떤 서버와 통신하는 사례인지 알아보기 쉽게 했다. 실제 장비가 화면에 보여 주는 열이나 내부 기록 방식은 다를 수 있다. 요청이 나간 뒤 응답이 돌아오면 공유기는 바깥 주소·포트와 연결된 기록을 찾는다.

이번 예의 표를 간단히 적으면 다음과 같다.

| 프로토콜 | 내부 통신(Local) | 외부 상대(Remote) | 바깥 통신(External) |
| --- | --- | --- | --- |
| TCP | `192.168.0.10:3000` | `203.0.113.80:443` | `198.51.100.25:53001` |

한 줄은 “이 내부 통신이 NAT를 지나 바깥에서 어떤 주소·포트로 보이는가”를 나타낸다. Remote 열에는 통신 상대가 기록되어 있지만, 이 열이 있다고 해서 바깥쪽 매핑이 반드시 상대 서버마다 달라지는 것은 아니다. 여러 내부 기기가 같은 공유기 바깥 주소를 사용하더라도 외부 포트와 기록을 다르게 두면 통신을 구별할 수 있다. 주소 하나만 갈아 끼우는 표가 아니라, 통신의 어느 쪽과 연결되는지 적은 표라고 생각하면 된다.

통신 중 자동으로 만들어진 변환 행은 연결이 끝나거나 장비의 유휴 시간이 지나면 사라질 수 있다. UDP처럼 명시적인 연결 종료 절차가 없는 통신은 장비의 타이머가 중요한 역할을 한다. 사용자가 직접 등록한 포트 포워딩 같은 고정 규칙은 자동 생성된 행과 다르게 취급한다. 따라서 자동 변환 행과 사용자가 설정한 고정 규칙을 구별해서 보아야 한다.

**기억할 점:** NAT 변환표 한 줄을 읽을 때는 내부 주소, 외부 상대, 바깥쪽 주소를 함께 본다.

## 서버에서 응답이 돌아오기

<!-- learn-page-id: advanced-source-11-page-07 -->

웹 서버가 응답을 보내면 패킷의 출발지는 `203.0.113.80:443`, 목적지는 요청 때 바깥에 보였던 `198.51.100.25:53001`이다. 응답의 목적지는 노트북의 사설 주소가 아니라 NAT가 정한 바깥쪽 주소다. 인터넷에는 `192.168.0.10`으로 직접 돌아가는 경로가 없기 때문이다.

공유기에 응답이 도착하면 먼저 목적지 주소와 포트를 이용해 바깥쪽 매핑 기록을 찾는다. 여기서 매핑은 안쪽 통신과 바깥에서 보이는 주소·포트를 짝지어 기록하는 방식이다. 그다음 이 응답을 받아들일지는 외부 상대를 확인하는 필터링 규칙에 달려 있다. 필터링은 외부에서 온 패킷을 어떤 조건으로 통과시킬지 정하는 방식이다. 상대 서버 주소와 포트까지 확인하는 필터링이라면, 이 예의 응답 출발지 `203.0.113.80:443`도 허용 조건에 맞아야 한다. 이 예에서는 요청에 사용한 같은 서버의 정상 응답이 돌아온다고 가정한다. 모든 NAT가 같은 조건을 쓰지는 않으며, 다음 Lesson에서 이 두 기준을 나누어 살펴본다.

만약 표에서 맞는 행을 찾지 못하면 공유기는 어느 안쪽 기기로 보낼지 알 수 없다. 그러면 응답이 안쪽에 전달되지 않을 수 있다. 이것은 어떤 NAT든 같은 방식으로 처리한다는 뜻은 아니다. 실제 허용 조건은 다음 Lesson에서 매핑과 필터링을 나누어 살펴본다.

**기억할 점:** 돌아온 응답은 주소만 대충 보고 보내는 것이 아니라 변환표에서 통신 짝을 찾아간다.

## Inbound · 원래 PC로 되돌리기

<!-- learn-page-id: advanced-source-11-page-08 -->

변환표에서 일치하는 행을 찾으면 공유기는 응답 패킷의 목적지를 바꾼다. 바깥쪽 목적지 `198.51.100.25:53001`을 안쪽 목적지 `192.168.0.10:3000`으로 되돌린다. 이를 Inbound, 즉 바깥에서 안쪽으로 들어오는 방향의 처리라고 부른다. 응답의 출발지 `203.0.113.80:443`은 그대로 둔다.

요청을 보낼 때 내 PC는 패킷의 출발지였지만, 응답을 돌려받을 때는 패킷이 향하는 목적지가 된다. 그래서 요청 때에는 출발지 정보가 바뀌고 응답 때에는 목적지 정보가 바뀐다. 바꾸는 자리는 다르지만 공유기는 같은 변환표 기록을 이용해 응답을 원래 PC로 돌려보낸다. 요청이 지나갈 때 기록이 만들어지지 않았다면, 나중에 온 응답을 어느 PC로 보내야 하는지 판단하기 어렵다.

따라서 NAT는 “나갈 때 주소를 바꾸는 것”으로 끝나지 않는다. 바꾼 값을 기록해 두고 돌아오는 응답을 원래의 내부 통신과 연결하는 과정까지 이어진다.

**기억할 점:** Inbound에서는 바깥 주소·포트를 변환표에 기록된 내부 목적지로 복원한다.

## 다른 PC의 연결도 구분하기

<!-- learn-page-id: advanced-source-11-page-09 -->

이번에는 같은 웹 서버에 다른 PC `192.168.0.11`도 접속한다고 하자. 이 PC가 `4000` 포트에서 요청을 시작하면 내부 통신은 `192.168.0.11:4000 → 203.0.113.80:443`이다. 공유기는 앞서 본 첫 번째 통신과 구별되는 변환표 기록을 만든다. 예를 들어 바깥에서는 `198.51.100.25:53002`로 표시할 수 있다.

| 내부 통신(Local) | 외부 상대(Remote) | 바깥 통신(External) |
| --- | --- | --- |
| `192.168.0.10:3000` | `203.0.113.80:443` | `198.51.100.25:53001` |
| `192.168.0.11:4000` | `203.0.113.80:443` | `198.51.100.25:53002` |

두 통신은 공유기의 바깥 IP 주소를 함께 쓰지만 외부 포트와 변환표 항목이 다르다. 웹 서버에서 응답이 각각의 외부 포트로 돌아오면 공유기는 대응하는 행을 찾아 올바른 PC에 전달한다. NAT가 여러 내부 통신을 하나의 바깥 주소와 연결할 수 있는 이유를 이 표에서 확인할 수 있다. 여러 내부 기기의 IP 주소와 포트를 하나의 바깥 IP 주소와 포트들로 바꾸어 함께 통신하게 하는 방식을 NAPT(Network Address and Port Translation)라고 한다. PAT라는 이름도 사용된다.

**기억할 점:** 여러 기기가 바깥 IP 하나를 공유해도 포트와 변환표 기록으로 각 통신을 나눌 수 있다.

## 서버가 구별하는 연결

<!-- learn-page-id: advanced-source-11-page-10 -->

이제 첫 번째 PC `192.168.0.10:3000`이 웹 서버뿐 아니라 다른 서버 `203.0.113.81:443`에도 접속한다고 하자. 오래된 Symmetric NAT 설명에서는 같은 내부 통신이라도 외부 상대가 달라지면 별도의 바깥 포트와 변환표 행을 사용할 수 있다고 가정한다. 이 사례는 바깥쪽 매핑이 상대에 따라 달라질 수 있는 한 가지 동작을 보여 주는 예다. TCP·UDP NAT 행동 표준은 같은 내부 주소·포트에서 다른 상대와 통신할 때도 같은 바깥 매핑을 재사용하는 동작을 요구한다. 외부 상대를 제한하는지는 필터링에서 따로 다룬다. 그러므로 아래 표는 표준을 따르는 모든 NAT의 기본 동작이 아니라, 과거 Symmetric 분류에서 설명하던 사례다.

| 내부 통신(Local) | 외부 상대(Remote) | 바깥 통신(External) |
| --- | --- | --- |
| `192.168.0.10:3000` | `203.0.113.80:443` | `198.51.100.25:53001` |
| `192.168.0.10:3000` | `203.0.113.81:443` | `198.51.100.25:53003` |

이 방식에서는 NAT가 응답을 받을 때 외부 상대까지 확인해 어느 행에 대응하는지 구별할 수 있다. 단, 표의 포트 숫자는 설명을 위한 예시이며 실제 장비가 꼭 이처럼 순서대로 배정하지 않는다. NAT는 사용 중인 포트를 피해 다른 값을 고를 수 있다.

“Symmetric NAT”라는 이름은 과거 자료에서 여러 동작을 한데 묶어 부르던 표현이다. 모든 현대 장비의 동작이나 보안 수준을 나타내는 보편적 등급으로 외우면 안 된다. 매핑은 안쪽 통신과 바깥 주소·포트를 연결하는 방식이고, 필터링은 외부에서 온 패킷을 어떤 조건으로 통과시킬지 정하는 방식이다. 현대의 동작 기준은 이 둘을 나누어 살핀다. 다음 Lesson에서 각각의 기준을 비교한다.

**기억할 점:** 예전 Symmetric 예시의 핵심은 “외부 상대가 바뀌면 매핑도 달라질 수 있다”는 것이며 모든 NAT가 그렇다는 뜻은 아니다.

## Local·Remote·External 용어 정리

<!-- learn-page-id: advanced-source-11-page-11 -->

앞에서 요청과 응답을 따라가며 본 세 가지 정보는 NAT 변환표를 설명할 때 Local, Remote, External이라는 이름으로 정리할 수 있다. 이 이름들은 새 동작을 뜻하는 것이 아니라, 내부 통신·통신 상대·바깥에서 보이는 통신을 구분하는 표의 항목이다. 이 Lesson에서는 **Local**을 변환 전 내부 기기의 주소와 포트, **Remote**를 통신 상대 서버와 포트, **External**을 변환 뒤 바깥 네트워크에서 보이는 주소·포트로 사용했다. Local은 공유기 자체의 LAN 주소가 아니다. 제품에 따라 실제 관리 화면의 이름과 열 배치가 다를 수 있으므로 이름만 외우기보다 각 값이 어느 쪽에 있는지 확인한다.

| 이름 | 이 예에서 가리키는 값 | 확인할 질문 |
| --- | --- | --- |
| Local | `192.168.0.10:3000` | 집 안에서 요청을 시작한 기기와 통신 포트는 무엇인가? |
| Remote | `203.0.113.80:443` | 요청이 향한 외부 서버와 서비스 포트는 무엇인가? |
| External | `198.51.100.25:53001` | 바깥쪽에서 이 통신을 어떤 주소·포트로 보는가? |

이 Lesson의 표에서는 요청의 Local, 통신 상대인 Remote, 바깥에서 보이는 External을 나란히 비교한다. 실제 NAT 매핑은 Local과 External을 연결하며, Remote는 필터링 조건이나 통신 기록을 설명할 때 따로 고려할 수 있다. Remote가 표에 있다고 해서 모든 NAT가 이를 바깥 매핑을 정하는 기준으로 사용한다는 뜻은 아니다. 응답이 돌아오면 변환표에서 매핑을 찾고 해당 장비의 필터링 규칙도 적용한다. 여러 Local 통신은 하나의 외부 IP 주소를 공유할 수 있다.

이번 Lesson에서는 변환표 한 행을 따라 요청이 나가고 응답이 돌아오는 흐름을 살펴봤다. 다음 Lesson에서는 변환표를 만드는 매핑 방식과 외부 패킷을 허용하는 필터링 조건이 어떻게 다른지 비교한다. 예전 유형 이름만으로 실제 장비를 판단하지 말고, “주소·포트는 어떻게 매핑하는가?”와 “어떤 외부 패킷을 통과시키는가?”를 각각 살펴보자.

**한 줄 정리:** NAT 변환표는 내부 통신(Local), 통신 상대(Remote), 바깥에서 보이는 통신(External)을 연결해 응답을 제자리로 돌려보낸다.
