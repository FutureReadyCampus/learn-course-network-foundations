---
id: u7-advanced-09-pc에-설치하는-proxy
title: PC의 로컬 프록시로 통신 살펴보기
source_lesson_ids:
- u7-advanced-09-pc에-설치하는-proxy
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-09.md
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-09.md
page_metadata:
- page_id: advanced-source-09-page-01
  illustrations:
  - file: assets/animations/u11-fwd-09-01-encrypted-packet.svg
    title: "암호화된 패킷의 한계"
    alt: "암호화된 패킷의 한계: PC의 패킷을 캡처해 봐요 → IP·TCP 정보는 볼 수 있어요 → HTTPS 내용은 암호화되어 있어요 → 그래서 별도의 중계 지점을 만들어요"
    caption: "잡았다고 읽을 수 있는 건 아니에요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p15-q01
    kind: choice
    difficulty: easy
    prompt: Wireshark로 HTTPS 패킷을 캡처했을 때 일반적으로 생기는 한계는 무엇인가요?
    choices:
    - id: a
      text: 캡처하면 TCP가 사라진다
      feedback: 본문에서 캡처와 평문 분석은 별개의 일이며 TLS는 Payload를 암호화합니다. 확인해 보세요.
    - id: b
      text: IP 주소가 모두 파일명이 된다
      feedback: 본문에서 캡처와 평문 분석은 별개의 일이며 TLS는 Payload를 암호화합니다. 확인해 보세요.
    - id: c
      text: 암호화된 Payload를 바로 평문으로 읽기 어렵다
      feedback: 캡처와 평문 분석은 별개의 일이며 TLS는 Payload를 암호화합니다.
    - id: d
      text: 패킷이 브라우저 화면으로 변한다
      feedback: 본문에서 캡처와 평문 분석은 별개의 일이며 TLS는 Payload를 암호화합니다. 확인해 보세요.
    - id: e
      text: HTTPS는 패킷으로 전송되지 않는다
      feedback: 본문에서 캡처와 평문 분석은 별개의 일이며 TLS는 Payload를 암호화합니다. 확인해 보세요.
    answer: c
  - id: u11-l04-p15-q02
    kind: choice
    difficulty: medium
    prompt: 로컬 Proxy를 개발 분석에 쓰는 기본 이유는 무엇인가요?
    choices:
    - id: a
      text: 모든 네트워크 장치를 제거한다
      feedback: 본문에서 중계 지점에서 권한 범위 내의 요청과 응답을 분석할 수 있습니다. 확인해 보세요.
    - id: b
      text: 항상 서버의 암호 키를 알아낸다
      feedback: 본문에서 중계 지점에서 권한 범위 내의 요청과 응답을 분석할 수 있습니다. 확인해 보세요.
    - id: c
      text: 브라우저의 주소를 숨긴다
      feedback: 본문에서 중계 지점에서 권한 범위 내의 요청과 응답을 분석할 수 있습니다. 확인해 보세요.
    - id: d
      text: 인터넷 연결 없이 외부 서버를 연다
      feedback: 본문에서 중계 지점에서 권한 범위 내의 요청과 응답을 분석할 수 있습니다. 확인해 보세요.
    - id: e
      text: 브라우저와 서버 사이에 요청·응답 관찰 지점을 만든다
      feedback: 중계 지점에서 권한 범위 내의 요청과 응답을 분석할 수 있습니다.
    answer: e
- page_id: advanced-source-09-page-02
  illustrations:
  - file: assets/animations/u11-fwd-09-02-local-proxy.svg
    title: "PC에 설치하는 Proxy"
    alt: "PC에 설치하는 Proxy: 브라우저는 내 PC 안에 있어요 → 분석 도구가 PC 안에서 Proxy로 동작해요 → 브라우저의 요청이 도구로 먼저 가요 → 도구가 서버로 전달하고 내용을 보여 줘요"
    caption: "내 PC 안에 중계 도구를 둬요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p16-q01
    kind: choice
    difficulty: easy
    prompt: Fiddler나 Burp Suite를 로컬 Proxy로 쓸 때 브라우저는 어디로 요청을 보내나요?
    choices:
    - id: a
      text: 목적지 웹사이트에 직접 요청을 보낸다
      feedback: 브라우저는 먼저 같은 PC의 로컬 Proxy 도구로 요청을 보내요.
    - id: b
      text: 기본 게이트웨이에 요청을 보낸다
      feedback: 브라우저는 먼저 같은 PC의 로컬 Proxy 도구로 요청을 보내요.
    - id: c
      text: DNS 서버에 요청 내용을 보낸다
      feedback: 브라우저는 먼저 같은 PC의 로컬 Proxy 도구로 요청을 보내요.
    - id: d
      text: 같은 PC에서 실행 중인 Proxy 도구
      feedback: 브라우저 Proxy 설정이 로컬 도구로 연결됩니다.
    - id: e
      text: 외부 웹 서버에 먼저 요청을 보낸다
      feedback: 브라우저는 먼저 같은 PC의 로컬 Proxy 도구로 요청을 보내요.
    answer: d
  - id: u11-l04-p16-q02
    kind: choice
    difficulty: medium
    prompt: 분석 도구를 사용할 때 지켜야 할 점은 무엇인가요?
    choices:
    - id: a
      text: 승인된 트래픽과 적절한 데이터 취급 기준 안에서 사용한다
      feedback: 분석 기능은 다른 사람의 통신을 볼 권한을 자동으로 주지 않습니다.
    - id: b
      text: 실제 이용자 통신을 무조건 복호화한다
      feedback: 본문에서 분석 기능은 다른 사람의 통신을 볼 권한을 자동으로 주지 않습니다. 확인해 보세요.
    - id: c
      text: 인증서 경고를 모두 끈다
      feedback: 본문에서 분석 기능은 다른 사람의 통신을 볼 권한을 자동으로 주지 않습니다. 확인해 보세요.
    - id: d
      text: 도구가 있으므로 권한을 생략한다
      feedback: 본문에서 분석 기능은 다른 사람의 통신을 볼 권한을 자동으로 주지 않습니다. 확인해 보세요.
    - id: e
      text: 기록을 누구에게나 공유한다
      feedback: 본문에서 분석 기능은 다른 사람의 통신을 볼 권한을 자동으로 주지 않습니다. 확인해 보세요.
    answer: a
- page_id: advanced-source-09-page-03
  illustrations:
  - file: assets/animations/u11-fwd-09-03-loopback.svg
    title: "Loopback에 Proxy 설정"
    alt: "Loopback에 Proxy 설정: 브라우저에 127.0.0.1:8080을 적어요 → 연결은 같은 PC 안에서만 오가요 → 포트 8080이 어느 프로그램인지 가려 줘요 → 도구가 꺼져 있으면 연결할 수 없어요"
    caption: "127.0.0.1은 내 컴퓨터를 가리켜요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p17-q01
    kind: choice
    difficulty: easy
    prompt: 127.0.0.1 Loopback 주소는 무엇을 가리키나요?
    choices:
    - id: a
      text: 인터넷의 공인 DNS 서버
      feedback: 본문에서 loopback 주소는 자기 컴퓨터를 가리킵니다. 확인해 보세요.
    - id: b
      text: 항상 외부 라우터
      feedback: 본문에서 loopback 주소는 자기 컴퓨터를 가리킵니다. 확인해 보세요.
    - id: c
      text: 동아리 신청 서버의 공인 주소
      feedback: 본문에서 loopback 주소는 자기 컴퓨터를 가리킵니다. 확인해 보세요.
    - id: d
      text: 스위치의 미러링 포트
      feedback: 본문에서 loopback 주소는 자기 컴퓨터를 가리킵니다. 확인해 보세요.
    - id: e
      text: 같은 호스트의 네트워크 연결 지점
      feedback: Loopback 주소는 자기 컴퓨터를 가리킵니다.
    answer: e
  - id: u11-l04-p17-q02
    kind: choice
    difficulty: medium
    prompt: Proxy 주소 뒤에 포트 번호를 적는 이유는 무엇인가요?
    choices:
    - id: a
      text: IP 주소를 암호화하기 위해
      feedback: 본문에서 포트 번호는 호스트 안에서 어느 서비스로 연결할지 구분합니다. 확인해 보세요.
    - id: b
      text: 같은 호스트에서 연결을 받을 프로그램을 구분하기 위해
      feedback: 포트 번호는 호스트 안에서 어느 서비스로 연결할지 구분합니다.
    - id: c
      text: 도메인 이름을 번역하기 위해
      feedback: 본문에서 포트 번호는 호스트 안에서 어느 서비스로 연결할지 구분합니다. 확인해 보세요.
    - id: d
      text: 패킷 크기를 줄이기 위해
      feedback: 본문에서 포트 번호는 호스트 안에서 어느 서비스로 연결할지 구분합니다. 확인해 보세요.
    - id: e
      text: 사용자 계정을 바꾸기 위해
      feedback: 본문에서 포트 번호는 호스트 안에서 어느 서비스로 연결할지 구분합니다. 확인해 보세요.
    answer: b
- page_id: advanced-source-09-page-04
  illustrations:
  - file: assets/animations/u11-fwd-09-04-local-path.svg
    title: "로컬 Proxy를 통과하는 경로"
    alt: "로컬 Proxy를 통과하는 경로: 브라우저와 Proxy 사이의 연결이 있어요 → Proxy와 서버 사이의 연결이 따로 있어요 → HTTPS는 구간별로 따로 암호화될 수 있어요 → 허가 없이 복호화해서는 안 돼요"
    caption: "두 개의 구간을 차례로 따라가요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p18-q01
    kind: choice
    difficulty: easy
    prompt: 브라우저에서 로컬 Proxy를 거쳐 서버로 갈 때 연결은 몇 구간인가요?
    choices:
    - id: a
      text: 브라우저-Proxy와 Proxy-서버의 별도 두 연결
      feedback: Proxy가 양쪽 연결을 각각 맺고 중계합니다.
    - id: b
      text: Proxy를 제외한 한 연결만
      feedback: 본문에서 proxy가 양쪽 연결을 각각 맺고 중계합니다. 확인해 보세요.
    - id: c
      text: 연결이 전혀 없다
      feedback: 본문에서 proxy가 양쪽 연결을 각각 맺고 중계합니다. 확인해 보세요.
    - id: d
      text: DNS를 포함해 항상 일곱 개
      feedback: 본문에서 proxy가 양쪽 연결을 각각 맺고 중계합니다. 확인해 보세요.
    - id: e
      text: 브라우저가 만든 UDP 한 개만
      feedback: 본문에서 proxy가 양쪽 연결을 각각 맺고 중계합니다. 확인해 보세요.
    answer: a
  - id: u11-l04-p18-q02
    kind: choice
    difficulty: medium
    prompt: 로컬 Proxy가 HTTPS 내용을 볼 수 있는 조건은 무엇인가요?
    choices:
    - id: a
      text: Loopback 주소만 지정하면 항상 가능하다
      feedback: 본문에서 TLS 암호화는 단순한 Proxy 경유만으로 해제되지 않습니다. 확인해 보세요.
    - id: b
      text: 포트 번호를 443으로 바꾸면 된다
      feedback: 본문에서 TLS 암호화는 단순한 Proxy 경유만으로 해제되지 않습니다. 확인해 보세요.
    - id: c
      text: 적절한 TLS 중계 구성과 신뢰 설정이 갖춰져야 한다
      feedback: TLS 암호화는 단순한 Proxy 경유만으로 해제되지 않습니다.
    - id: d
      text: 패킷 복사만 켜면 된다
      feedback: 본문에서 TLS 암호화는 단순한 Proxy 경유만으로 해제되지 않습니다. 확인해 보세요.
    - id: e
      text: 모든 TLS는 평문으로 전송된다
      feedback: 본문에서 TLS 암호화는 단순한 Proxy 경유만으로 해제되지 않습니다. 확인해 보세요.
    answer: c
- page_id: advanced-source-09-page-05
  illustrations:
  - file: assets/animations/u11-fwd-09-05-stream.svg
    title: "Stream 수준의 해석"
    alt: "Stream 수준의 해석: 패킷은 조각으로 도착해요 → 조각을 이어야 요청 전체가 보여요 → 소켓에서는 이어진 흐름으로 읽어요 → TLS 내용은 별도 설정이 있어야 보여요"
    caption: "조각난 패킷을 하나의 요청으로 봐요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p19-q01
    kind: choice
    difficulty: easy
    prompt: TCP 소켓에서 애플리케이션이 받는 Stream은 무엇인가요?
    choices:
    - id: a
      text: 하나의 고정된 IP 패킷
      feedback: 본문에서 stream은 애플리케이션이 소켓에서 읽는 연속된 바이트 흐름입니다. 확인해 보세요.
    - id: b
      text: TCP 바이트의 연속된 흐름
      feedback: Stream은 애플리케이션이 소켓에서 읽는 연속된 바이트 흐름입니다.
    - id: c
      text: 케이블 위의 전기 신호만
      feedback: 본문에서 stream은 애플리케이션이 소켓에서 읽는 연속된 바이트 흐름입니다. 확인해 보세요.
    - id: d
      text: DNS 이름 목록
      feedback: 본문에서 stream은 애플리케이션이 소켓에서 읽는 연속된 바이트 흐름입니다. 확인해 보세요.
    - id: e
      text: 서버 화면 이미지
      feedback: 본문에서 stream은 애플리케이션이 소켓에서 읽는 연속된 바이트 흐름입니다. 확인해 보세요.
    answer: b
  - id: u11-l04-p19-q02
    kind: choice
    difficulty: medium
    prompt: Proxy가 소켓 Stream을 분석한다고 해서 무엇이 보장되지는 않나요?
    choices:
    - id: a
      text: 요청이 두 연결을 거칠 수 있다는 점
      feedback: 본문에서 stream 처리와 TLS 복호화는 별개의 문제입니다. 확인해 보세요.
    - id: b
      text: Proxy가 데이터를 중계할 수 있다는 점
      feedback: 본문에서 stream 처리와 TLS 복호화는 별개의 문제입니다. 확인해 보세요.
    - id: c
      text: TCP 데이터가 패킷으로 전달된다는 점
      feedback: 본문에서 stream 처리와 TLS 복호화는 별개의 문제입니다. 확인해 보세요.
    - id: d
      text: 암호화된 TLS 내용이 자동으로 평문이 되는 것
      feedback: Stream 처리와 TLS 복호화는 별개의 문제입니다.
    - id: e
      text: 애플리케이션 단위로 분석할 수 있다는 점
      feedback: 본문에서 stream 처리와 TLS 복호화는 별개의 문제입니다. 확인해 보세요.
    answer: d
- page_id: advanced-source-09-page-06
  illustrations:
  - file: assets/animations/u11-fwd-09-06-wrap-up.svg
    title: "Fiddler와 Proxy 활용 정리"
    alt: "Fiddler와 Proxy 활용 정리: 외부 출구로 연결하는 우회 사례 → 조직이 관리하는 정책·검사 지점 → 내 PC 안의 로컬 분석 도구 → 공통 원리는 대신 전달하는 중계예요"
    caption: "목적은 달라도 중계 원리는 같아요"
    after_paragraph: 0
  questions:
  - id: u11-l04-p20-q01
    kind: choice
    difficulty: easy
    prompt: 포워드 프록시 사례의 공통 구조는 무엇인가요?
    choices:
    - id: a
      text: 항상 파일을 삭제한다
      feedback: 본문에서 우회, 정책 관리, 개발 분석은 같은 중계 원리를 다른 목적으로 활용합니다. 확인해 보세요.
    - id: b
      text: 모든 접속을 원본 경로 밖에서 복사만 한다
      feedback: 본문에서 우회, 정책 관리, 개발 분석은 같은 중계 원리를 다른 목적으로 활용합니다. 확인해 보세요.
    - id: c
      text: 클라이언트 요청을 받아 다른 연결로 전달하고 응답을 돌려준다
      feedback: 우회, 정책 관리, 개발 분석은 같은 중계 원리를 다른 목적으로 활용합니다.
    - id: d
      text: 모든 Proxy가 같은 기록을 남긴다
      feedback: 본문에서 우회, 정책 관리, 개발 분석은 같은 중계 원리를 다른 목적으로 활용합니다. 확인해 보세요.
    - id: e
      text: 항상 사용자 IP를 숨긴다
      feedback: 본문에서 우회, 정책 관리, 개발 분석은 같은 중계 원리를 다른 목적으로 활용합니다. 확인해 보세요.
    answer: c
  - id: u11-l04-p20-q02
    kind: choice
    difficulty: medium
    prompt: Proxy의 역할과 정보 흐름을 판단할 때 제품 이름 외에 살펴볼 것은 무엇인가요?
    choices:
    - id: a
      text: Proxy가 지원하는 운영체제와 제품 버전만
      feedback: 이 요소들은 각각 참고가 되지만, Proxy의 역할과 정보 흐름을 보려면 배치·연결 방향·기능 설정·운영 정책을 함께 살펴야 해요.
    - id: b
      text: Proxy의 처리량과 저장 용량만
      feedback: 이 요소들은 각각 참고가 되지만, Proxy의 역할과 정보 흐름을 보려면 배치·연결 방향·기능 설정·운영 정책을 함께 살펴야 해요.
    - id: c
      text: TLS 연결을 종료하는지 여부만
      feedback: 이 요소들은 각각 참고가 되지만, Proxy의 역할과 정보 흐름을 보려면 배치·연결 방향·기능 설정·운영 정책을 함께 살펴야 해요.
    - id: d
      text: 로그 파일의 형식만
      feedback: 이 요소들은 각각 참고가 되지만, Proxy의 역할과 정보 흐름을 보려면 배치·연결 방향·기능 설정·운영 정책을 함께 살펴야 해요.
    - id: e
      text: 배치, 연결 방향, 기능 설정과 운영 정책
      feedback: 어디에 놓이고 무엇을 중계하는지에 따라 역할과 영향이 달라집니다.
    answer: e
---
## 암호화된 패킷을 보는 한계

<!-- learn-page-id: advanced-source-09-page-01 -->

앞에서는 공용 PC의 접속을 관리하는 조직용 Proxy를 살펴봤습니다. 이제 운영자 자신의 PC에서 동아리 사이트의 로그인 오류를 분석하려고 웹 브라우저 트래픽을 살펴봅니다. Wireshark로 PC의 네트워크 패킷을 캡처하면 IP·TCP 정보를 볼 수 있지만, HTTPS Payload는 TLS로 암호화되어 읽을 수 없는 경우가 일반적입니다. 패킷을 잡았다는 것과 웹 내용을 읽을 수 있다는 것은 다릅니다.

웹 요청을 분석하는 로컬 Proxy 도구를 사용하면 브라우저와 서버 사이에 별도의 중계 지점을 만들 수 있습니다. 이 도구는 브라우저의 요청을 받아 서버로 전달하고, 응답을 다시 브라우저에 보냅니다. 개발자는 자신의 권한 범위 안에서 요청·응답을 관찰해 오류를 찾을 수 있습니다.

HTTPS 내용을 확인하려면 브라우저와 Proxy 도구가 신뢰하도록 구성하는 인증서 등 별도 설정이 필요할 수 있습니다. 다음에는 Fiddler나 Burp Suite 같은 도구가 같은 PC에서 어떻게 동작하는지 살펴봅니다.

## PC에 설치하는 Proxy

<!-- learn-page-id: advanced-source-09-page-02 -->

Fiddler나 Burp Suite는 웹 요청과 응답을 분석할 때 사용할 수 있는 도구의 예입니다. 도구는 PC 안에서 Proxy 서버로 동작하고 브라우저는 그 주소로 요청을 보내도록 설정됩니다. 실제 지원 기능과 화면은 도구 버전과 설정에 따라 달라지지만, 여기서는 로컬 중계 구조를 이해하는 데 초점을 둡니다.

개발자는 테스트 요청의 URL, 헤더, 상태 코드와 본문을 살펴 오류를 진단할 수 있습니다. 다만 계정 정보나 실제 이용자 자료가 포함된 트래픽을 다룰 때에는 승인과 데이터 취급 기준을 따라야 합니다. 분석 도구는 권한을 넘어 통신을 감시해도 된다는 허가가 아닙니다.

브라우저가 Proxy를 사용하도록 설정하면 연결 흐름이 바뀝니다. 다음에는 `127.0.0.1`과 포트 번호를 사용해 브라우저가 자기 컴퓨터의 Proxy로 접속하는 방법을 따라가겠습니다.

## Loopback에 Proxy 설정

<!-- learn-page-id: advanced-source-09-page-03 -->

PC 안에서 실행 중인 분석 Proxy는 `127.0.0.1` 같은 Loopback 주소와 포트 번호로 요청을 받을 수 있습니다. `127.0.0.1`은 네트워크로 외부에 나가지 않고 같은 호스트를 가리키는 주소입니다. 예를 들어 도구가 8080 포트에서 연결을 기다리고 있다면, 브라우저 Proxy 설정에 `127.0.0.1:8080`을 지정할 수 있습니다.

브라우저는 외부 사이트에 직접 연결하지 않고 자신의 컴퓨터에 있는 Proxy 프로세스에 TCP 연결을 맺습니다. 그 프로세스는 별도의 연결로 외부 사이트에 접속합니다. 포트 번호는 같은 IP 주소에서 어느 프로그램으로 연결을 보낼지 구분하는 역할을 합니다.

도구가 실행 중이지 않거나 브라우저와 Proxy의 포트 설정이 다르면 연결은 실패합니다. 다음 Page에서는 브라우저와 로컬 Proxy, Proxy와 외부 서버 사이의 두 연결을 차례대로 따라가겠습니다.

## 로컬 Proxy를 통과하는 경로

<!-- learn-page-id: advanced-source-09-page-04 -->

브라우저가 로컬 Proxy에 요청을 보내면 Proxy는 외부 서버와 별도의 연결을 맺습니다. 따라서 브라우저와 Proxy 사이의 연결, Proxy와 서버 사이의 연결이 각각 존재합니다. 둘은 같은 TCP 연결의 양 끝이 아니라 Proxy 프로그램이 연결해 주는 두 개의 구간입니다.

HTTPS를 분석하려면 브라우저가 로컬 Proxy를 신뢰하도록 구성하고, Proxy가 브라우저와 서버 사이에서 TLS를 적절히 중계해야 할 수 있습니다. 이 구성에서 브라우저와 Proxy, Proxy와 서버 사이의 암호화 구간은 별도로 성립할 수 있습니다. 인증서 오류를 무시하거나 다른 사람의 통신을 허가 없이 복호화해서는 안 됩니다.

필요한 신뢰 설정이 없으면 Proxy도 암호화된 내용을 평문으로 볼 수 없습니다. 다음에는 패킷을 캡처하는 것과 소켓 Stream을 읽는 것이 분석에서 어떻게 다른지 살펴보겠습니다.

## Stream 수준의 해석과 분석

<!-- learn-page-id: advanced-source-09-page-05 -->

네트워크에서는 TCP 데이터가 여러 패킷으로 나뉘어 전달될 수 있습니다. 패킷 캡처 화면에서는 각 조각의 헤더와 순서를 볼 수 있지만, HTTP 요청 전체를 이해하려면 패킷을 재조립하고 프로토콜을 해석해야 할 수 있습니다. 반면 애플리케이션 Proxy는 소켓에서 TCP 바이트 Stream을 받아 HTTP 요청·응답 단위로 다룰 수 있습니다.

Stream은 패킷 경계와 같은 개념이 아닙니다. 브라우저가 한 번에 요청 하나를 보냈더라도 TCP는 데이터를 여러 세그먼트로 나눌 수 있고, 소켓을 읽는 프로그램은 바이트 흐름을 전달받습니다. Proxy 도구가 이 흐름을 분석해 요청 단위 화면으로 보여 주면 개발자가 문제를 찾기 편리합니다.

Stream 처리는 암호화 해제를 자동으로 의미하지 않습니다. TLS 내용이 보이려면 Proxy가 암호화 연결을 적절히 중계하고 신뢰 설정도 갖춰야 합니다. 다음 Page에서 여러 Proxy 활용 사례의 공통 구조와 다른 목적을 정리하겠습니다.

## Fiddler와 Proxy 활용 정리

<!-- learn-page-id: advanced-source-09-page-06 -->

지금까지 Proxy를 외부 경로로 연결하는 우회 사례, 내부 사용자의 정책 관리와 파일 검사, 운영자 PC의 로컬 분석 도구로 살펴봤습니다. 배치와 목적은 달라도 클라이언트의 요청을 받아 다른 연결로 전달하고 응답을 되돌려 준다는 중계 원리가 공통으로 나타납니다.

어떤 Proxy는 클라이언트 가까이에서 사용자가 선택한 요청을 전달하고, 어떤 Proxy는 조직이 관리하는 내부 통제 지점으로 쓰입니다. TLS를 중계하는지, 요청 내용을 기록하는지, 어떤 목적지로 연결하는지는 각각의 구성과 정책을 확인해야 합니다. Proxy라는 이름만으로 보안과 익명성, 분석 가능성을 가정하지 않습니다.

이제 클라이언트 요청을 대신하는 포워드 프록시를 보았습니다. 다음 Lesson에서는 방향을 뒤집어, 인터넷 사용자가 보는 서버 주소 앞에 놓여 실제 웹 서버의 요청을 대신 받는 Reverse Proxy를 살펴보겠습니다.
