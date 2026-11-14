---
id: u9-advanced-18-대규모-부하분산을-위한-gslb
title: '해외 고객에겐 왜 느릴까: DNS 부하 분산, GSLB, CDN'
source_lesson_ids:
- u9-advanced-18-대규모-부하분산을-위한-gslb
source_wikis:
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-18.md
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/05-1.md#p258-b01
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/05-1.md#p261-b11
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/05-1.md#p269-b07
- https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/honja-network/05-3.md#p317-b01
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/advanced/lesson-18.md
page_metadata:
- page_id: advanced-source-18-page-01
  illustrations:
  - file: assets/animations/u13-l03-p1-latency.svg
    title: "일본 고객에게만 왜 느릴까?"
    alt: "서울 사이트의 서버는 한산한데 일본 고객의 요청이 왕복 50ms를 20~30번 오가 첫 화면이 1~1.5초 더 걸리고, 도쿄 사이트를 두면 가까워지는 모습입니다."
    caption: "서버 대수가 아니라 손님과 서버 사이의 거리와 망 경로가 느림의 원인일 수 있습니다."
    after_paragraph: 1
  questions:
  - id: u13-l03-p01-q01
    kind: choice
    difficulty: easy
    prompt: 일본 고객만 한결봇이 느릴 때, 서울 서버 대수를 늘려도 해결되지 않는 이유로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: TCP가 한국에서만 작동해서
      feedback: TCP는 전 세계 어디서나 같은 방식으로 작동한다.
    - id: b
      text: 일본 고객이 쓰는 PC의 성능이 낮아 화면 그리기가 늦어서
      feedback: 특정 PC가 아니라 지역 전체가 느리다.
    - id: c
      text: 서울 서버가 일본어를 지원하지 않아서
      feedback: 언어 지원은 응답 내용의 문제이지 연결 지연의 원인이 아니다.
    - id: d
      text: 로드 밸런서가 일본 고객의 요청 일부를 거부해서 재시도가 계속 늘어나서
      feedback: 거부라면 접속이 안 되고, 느린 것은 다른 현상이다.
    - id: e
      text: 서버 대수는 처리 용량의 문제이고 느림은 쌓이는 왕복 지연 탓이라서
      feedback: 맞다. 처리 한계와 거리는 서로 다른 원인이다.
    answer: e
    feedback: 서버 수는 처리 용량을, 거리와 망 경로는 지연을 좌우한다. 원인이 다르면 해결도 달라진다.
  - id: u13-l03-p01-q02
    kind: choice
    difficulty: medium
    prompt: 국내 고객 중 특정 통신사를 쓰는 사람들만 저녁에 한결봇이 느리다고 한다. 서버 사용률은 낮다. 먼저 의심할 구간과 다음에 할 일로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 한결봇 서버의 GPU를 늘려 저녁 시간대에 처리할 수 있는 요청 수를 올린다
      feedback: 서버 사용률이 낮아 처리 용량이 원인이 아니다.
    - id: b
      text: 서버 사용률이 낮으니 DNS TTL을 줄여 안내를 빠르게 바꾼다
      feedback: TTL은 캐시 시간이고 특정 통신사의 저녁 지연과 관계가 없다.
    - id: c
      text: 그 통신사 망과 서버 망이 만나는 구간. 경로와 지연을 따로 확인한다
      feedback: 맞다. 느린 손님의 공통점으로 구간을 쪼개 의심할 곳을 좁혔다. 🧩 쪼개기를 썼다.
    - id: d
      text: 대화 기록 DB를 이중화한다
      feedback: 이중화는 가용성 문제이고 지역·망 지연의 원인이 아니다.
    - id: e
      text: 한결봇 안내 문구를 바꾼다
      feedback: 문구는 화면 내용이지 연결 속도와 관계가 없다.
    answer: c
    feedback: 공통점이 있는 손님만 느리면 그 공통 구간부터 확인한다. 서버가 한산하면 용량이 아닌 경로 문제일 수 있고, 서버 묶음을 더 두는 것은 확인 뒤의 마지막 수단이다.
  question_placements:
  - question_id: u13-l03-p01-q01
    after_paragraph: 3
- page_id: advanced-source-18-page-02
  illustrations:
  - file: assets/animations/u13-l03-p2-dns-rr.svg
    title: "DNS가 주소를 둘 알려 주면?"
    alt: "이름 하나에 서울과 도쿄 주소를 둘 다 등록했지만 도쿄 사이트가 점검 중이어도 DNS는 몰라서 손님을 도쿄로 안내하다 막히는 모습입니다."
    caption: "DNS 라운드 로빈은 살아 있는지 확인하지 않으므로 상태를 보는 GSLB가 필요합니다."
    after_paragraph: 1
  questions:
  - id: u13-l03-p02-q01
    kind: choice
    difficulty: easy
    prompt: DNS에서 TTL의 역할로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: DNS 응답을 캐시가 보관해도 되는 시간을 정한다
      feedback: 맞다. TTL이 지나야 캐시가 새로 묻는다.
    - id: b
      text: 서버가 응답하는 최대 속도를 정한다
      feedback: 응답 속도와는 관계없다.
    - id: c
      text: 로드 밸런서가 요청을 서버에 나눠 줄 때 고르는 순서를 정한다
      feedback: 서버 선택 정책은 로드 밸런서의 설정이다.
    - id: d
      text: TLS 인증서의 유효 기간을 정한다
      feedback: 인증서 유효 기간은 별개의 값이다.
    - id: e
      text: 손님의 IP 주소를 숨긴다
      feedback: TTL은 주소를 숨기는 기능이 아니다.
    answer: a
    feedback: TTL은 DNS 답을 캐시에 보관하는 시간이다. 짧으면 바뀐 내용이 빨리 퍼지고 길면 질의가 줄어든다.
  - id: u13-l03-p02-q02
    kind: choice
    difficulty: medium
    prompt: 서울 사이트 점검을 앞두고 지우가 DNS에서 서울 주소를 뺐는데, TTL이 3600초인 탓에 한동안 일부 손님이 서울로 접속한다. 다음 점검 때 미리 할 일의 순서로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 점검 당일 아침에 TTL을 60초로 낮추고 곧바로 주소를 빼 전환 시간을 줄인다
      feedback: 이미 보관 중인 긴 TTL 캐시는 예전 TTL이 끝날 때까지 남는다.
    - id: b
      text: 점검 전에 TTL을 낮추고 옛 TTL이 지난 뒤 주소를 뺀다
      feedback: 맞다. TTL이 퍼질 시간을 순서에 넣었다. 📋 순서대로 확인하기를 썼다.
    - id: c
      text: TTL을 30일로 길게 늘린다
      feedback: 길면 바뀐 내용이 더 늦게 퍼진다.
    - id: d
      text: 주소를 빼지 않고 사이트를 끈다
      feedback: 주소가 남아 있으면 손님이 꺼진 사이트로 계속 간다.
    - id: e
      text: TTL은 건드리지 않고 손님에게 브라우저를 재시작하게 한다
      feedback: 리졸버 캐시는 손님이 재시작해도 남는다.
    answer: b
    feedback: TTL 변경이 퍼지는 시간을 두고 순서를 잡아야 전환이 빠르다. 대가는 DNS 질의 증가다.
  question_placements:
  - question_id: u13-l03-p02-q01
    after_paragraph: 3
- page_id: advanced-source-18-page-05
  illustrations:
  - file: assets/animations/u13-l03-p3-cname.svg
    title: "이름 하나로 지역마다 다른 주소를"
    alt: "bot.hangyeol.example이 CNAME jp.bot.gslb.example을 거쳐 도쿄 주소 203.0.113.20으로 풀리는 세 단계 흐름입니다."
    caption: "지역 선택은 GSLB가 관리하는 이름을 푸는 단계에서 일어납니다."
    after_paragraph: 1
  questions:
  - id: u13-l03-p03-q01
    kind: choice
    difficulty: easy
    prompt: CNAME 레코드가 하는 일은 무엇인가요?
    choices:
    - id: a
      text: 이름을 곧바로 IPv4 주소 하나에 연결하는 가장 기본적인 레코드이다
      feedback: 그것은 A 레코드의 역할이다.
    - id: b
      text: 메일을 받을 서버를 지정한다
      feedback: 그것은 MX 레코드의 역할이다.
    - id: c
      text: TLS 인증서를 자동으로 발급한다
      feedback: DNS 레코드는 인증서를 발급하지 않는다.
    - id: d
      text: 한 이름이 다른 이름을 가리키게 하는 별칭을 만든다
      feedback: 맞다. 최종 주소는 가리킨 이름을 다시 물어서 얻는다.
    - id: e
      text: 손님 PC의 MAC 주소를 알려 준다
      feedback: MAC 주소는 DNS가 아닌 로컬 네트워크에서 다룬다.
    answer: d
    feedback: CNAME은 별칭이다. 이름 하나를 다른 이름으로 이어 주어, 지역 선택을 그 뒤에서 바꿀 수 있게 한다.
  - id: u13-l03-p03-q02
    kind: choice
    difficulty: medium
    prompt: 지우가 nslookup으로 `bot.hangyeol.example`을 조회하니 `bot.hangyeol.example` → `jp.bot.gslb.example` → `203.0.113.20` 순으로 나왔다. 손님 PC가 실제로 접속할 주소와 지역 선택이 일어난 단계로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 접속 주소는 가운데의 `jp.bot.gslb.example`이고, 지역은 마지막 IP 단계에서 정해졌다
      feedback: 이름은 중간 단계이고 실제 접속은 마지막 IP 주소로 한다.
    - id: b
      text: 접속 주소는 알 수 없고 nslookup을 한 번 더 실행해 지역이 다시 정해지게 해야 한다
      feedback: 마지막 줄의 주소가 접속 대상이다.
    - id: c
      text: 접속 주소는 `bot.hangyeol.example`이고 지역은 손님이 직접 골랐다
      feedback: 이름은 DNS로 풀어야 하고 지역은 GSLB가 골랐다.
    - id: d
      text: 접속 주소는 `203.0.113.20`이고 지역은 브라우저가 골랐다
      feedback: 브라우저가 아니라 DNS 응답 단계에서 정해졌다.
    - id: e
      text: 접속 주소는 끝의 `203.0.113.20`, 지역은 GSLB가 가운데 이름을 정할 때 골랐다
      feedback: 맞다. 이름에서 주소까지 순서를 따라가 어느 단계가 지역을 골랐는지 짚었다. 📋 순서대로 확인하기를 썼다.
    answer: e
    feedback: CNAME 체인은 이름이 이어지다 마지막에 IP로 끝난다. 접속은 마지막 IP로, 지역 선택은 중간 이름을 정하는 단계에서 일어난다.
  question_placements:
  - question_id: u13-l03-p03-q01
    after_paragraph: 2
- page_id: advanced-source-18-page-06
  illustrations:
  - file: assets/animations/u13-l03-p4-resolver.svg
    title: "DNS는 손님 위치를 어떻게 알까?"
    alt: "도쿄 쇼룸의 노트북은 수동으로 적은 서울 쪽 공개 DNS를 써 서울로 안내되고, 다른 PC는 DHCP로 받은 도쿄 쪽 리졸버를 써 도쿄로 안내되는 비교입니다."
    caption: "권한 DNS는 손님이 아니라 질문을 대신 보낸 리졸버의 위치를 봅니다."
    after_paragraph: 1
  questions:
  - id: u13-l03-p04-q01
    kind: choice
    difficulty: easy
    prompt: 위치별로 다른 답을 주는 권한 DNS 서버가 기본으로 보는 주소는 무엇인가요?
    choices:
    - id: a
      text: 질의를 보낸 리졸버의 IP 주소
      feedback: 맞다. ECS가 없으면 권한 DNS는 손님 PC가 아니라 리졸버의 IP를 본다.
    - id: b
      text: 손님 PC의 MAC 주소
      feedback: MAC 주소는 같은 링크 안에서만 쓰인다.
    - id: c
      text: 손님이 사용하는 브라우저의 종류
      feedback: 브라우저 종류로 지역을 고르지 않는다.
    - id: d
      text: 한결디자인 서버의 위치
      feedback: 권한 DNS가 위치를 판단하는 대상은 질의한 쪽이다.
    - id: e
      text: 손님 PC에 설정된 사설 IP 주소와 서브넷 마스크
      feedback: 사설 주소는 인터넷에서 보이지 않는다.
    answer: a
    feedback: 권한 DNS가 보는 것은 질의한 리졸버의 IP다. ECS가 있으면 손님 주소의 앞부분도 힌트로 받는다.
  - id: u13-l03-p04-q02
    kind: choice
    difficulty: medium
    prompt: 도쿄 쇼룸 직원의 PC 한 대에 DNS 서버가 서울에 있는 공개 DNS 서비스로 직접 지정돼 있다. 이 서비스는 ECS를 보내지 않고 서울 쪽에서 질의한다. 이 PC에서 한결봇이 어느 사이트로 안내될지와 이유로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 도쿄 사이트. PC가 도쿄에 있고 DNS가 PC의 실제 위치를 기준으로 하기 때문이다
      feedback: DNS는 PC의 실제 위치가 아니라 리졸버를 본다.
    - id: b
      text: 매번 무작위로 서울과 도쿄를 번갈아 간다
      feedback: 이 상황에서는 리졸버 위치로 일정하게 판단된다.
    - id: c
      text: 서울 사이트. 권한 DNS는 리졸버가 있는 서울을 기준으로 판단한다
      feedback: 맞다. 질의한 쪽이 누구인지로 쪼개어 보면 쇼룸 PC가 도쿄에 있어도 서울 손님으로 보인다. 🧩 쪼개기를 썼다.
    - id: d
      text: 접속이 거부된다
      feedback: 접속 거부가 아니라 먼 사이트로 안내될 뿐이다.
    - id: e
      text: PC의 사설 IP 대역 `10.20.0.0/24`를 보고 도쿄로 안내한다
      feedback: 사설 주소는 인터넷의 권한 DNS가 볼 수 없다.
    answer: c
    feedback: DNS 위치 판단은 질의한 리졸버를 따른다. 쇼룸 PC가 서울 리졸버를 쓰면 서울 사이트로 안내된다.
  question_placements:
  - question_id: u13-l03-p04-q01
    after_paragraph: 3
- page_id: advanced-source-18-page-09
  illustrations:
  - file: assets/animations/u13-l03-p5-geoip.svg
    title: "IP 주소만 보고 나라를 알 수 있을까?"
    alt: "IP 위치 DB가 손님 IP 192.0.2.77을 일본·도쿄로 추정하지만, VPN을 쓰면 출구 위치로 보이는 한계를 함께 보여 줍니다."
    caption: "IP 위치는 가까운 지역 안내에만 쓰는 추정값이고 정확해야 하는 판단에는 다른 근거가 필요합니다."
    after_paragraph: 1
  questions:
  - id: u13-l03-p05-q01
    kind: choice
    difficulty: easy
    prompt: IP 주소로 위치를 알아내는 방법에 대한 설명으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: VPN을 써도 항상 실제 위치가 나온다
      feedback: VPN을 쓰면 출구 쪽 위치로 보일 수 있다.
    - id: b
      text: IP 주소에는 건물 단위의 정확한 위치가 들어 있어 틀릴 일이 없다
      feedback: IP 주소에는 집 주소가 들어 있지 않다.
    - id: c
      text: 위치 DB는 한 번 만들면 갱신이 필요 없다
      feedback: 주소 할당이 바뀌므로 계속 갱신해야 한다.
    - id: d
      text: IP 위치 데이터베이스로 추정하며 틀릴 수 있다
      feedback: 맞다. 추정값이라 VPN, 이동통신망, 주소 재할당으로 달라질 수 있다.
    - id: e
      text: 위치는 MAC 주소로만 알 수 있다
      feedback: MAC 주소는 인터넷 너머에서 보이지 않는다.
    answer: d
    feedback: IP 위치는 DB로 추정한 값이다. 안내에는 쓸 만하지만 정확해야 하는 판단에는 다른 근거가 필요하다.
  - id: u13-l03-p05-q02
    kind: choice
    difficulty: medium
    prompt: 서 이사가 "해외 IP를 막으면 해킹이 막히겠죠?"라며 IP 위치로 해외 접속 차단을 제안한다. 이 방법의 한계로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 위치 DB를 쓰면 요청마다 DB를 조회해 속도가 반으로 느려지는 것이 한계다
      feedback: 속도가 빨라지는 것은 한계가 아니다.
    - id: b
      text: VPN으로 우회되고 오판으로 정상 손님이 막힐 수 있다
      feedback: 맞다. 효과와 부작용을 함께 견줬다. ⚖️ 대가 따지기를 썼다.
    - id: c
      text: 한국 IP는 해킹에 쓰이지 않으므로 완벽하다
      feedback: 국내 IP도 공격에 쓰일 수 있다.
    - id: d
      text: 해외 IP는 DNS에 등록할 수 없어서 불가능하다
      feedback: DNS 등록과 무관하다.
    - id: e
      text: 차단하면 서버가 꺼지므로 위험하다
      feedback: 차단 때문에 서버가 꺼지지 않는다.
    answer: b
    feedback: IP 위치 차단은 우회와 오판이라는 한계가 있다. 효과만 보지 말고 부작용과 비용을 함께 따진다.
  question_placements:
  - question_id: u13-l03-p05-q01
    after_paragraph: 3
- page_id: u13-l03-page-06
  illustrations:
  - file: assets/animations/u13-l03-p6-sync.svg
    title: "서울과 도쿄가 다른 답을 한다면?"
    alt: "서울은 최신 지식 문서 버전이고 도쿄는 하루 전 버전이라 일본 고객이 예전 단가를 받다가, 서울 원본을 도쿄로 복사해 맞추는 모습입니다."
    caption: "여러 사이트의 내용은 한 곳을 원본으로 배포하고 버전 번호로 어긋남을 확인합니다."
    after_paragraph: 1
  questions:
  - id: u13-l03-p06-q01
    kind: choice
    difficulty: easy
    prompt: 서울과 도쿄 사이트가 서로 다른 답을 하는 일을 막으려면 무엇이 필요한가요?
    choices:
    - id: a
      text: DNS TTL을 하루로 늘려 두 사이트의 안내 주소를 오래 고정하는 것
      feedback: TTL은 안내 주소의 캐시 시간이고 내용 일치와 관계없다.
    - id: b
      text: 서울 서버만 남기고 도쿄를 끄는 것
      feedback: 그러면 거리 문제로 되돌아간다.
    - id: c
      text: 같은 버전의 모델과 문서를 두 곳에 배포하는 구조
      feedback: 맞다. 어느 사이트로 가도 같은 결과가 나오려면 내용이 같아야 한다.
    - id: d
      text: 고객이 직접 사이트를 고르게 하는 것
      feedback: 손님에게 부담을 넘기고 내용 불일치는 그대로다.
    - id: e
      text: 헬스 체크 주기를 줄이는 것
      feedback: 헬스 체크는 서버 상태 확인이고 버전 일치와는 다르다.
    answer: c
    feedback: 여러 지역이 같은 서비스를 하려면 내용의 동기화가 필요하다. 로드 분산과는 별개의 과제다.
  - id: u13-l03-p06-q02
    kind: choice
    difficulty: medium
    prompt: 상담 안내 문구를 고친 뒤 일부 고객만 예전 문구를 본다는 문의가 왔다. 서울·도쿄 사이트를 차례로 확인해 원인을 좁히는 순서로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 문구를 다시 고치지 않고 기다린다
      feedback: 시간이 지나도 사이트 버전이 다르면 계속 어긋난다.
    - id: b
      text: 도쿄 문구가 오래됐을 테니 확인 없이 서울 문구를 도쿄에 먼저 덮어쓴다
      feedback: 확인 없이 덮어쓰면 어느 사이트의 어느 버전이 원인인지 찾지 못하고 최신 내용까지 잃을 수 있다.
    - id: c
      text: DNS TTL을 줄여 모든 고객이 같은 사이트로 가게 한다
      feedback: TTL은 안내 주소의 캐시 시간이다. 사이트마다 내용 버전이 다른 문제와는 별개다.
    - id: d
      text: 안내 문구를 서버마다 직접 고쳐 쓴다
      feedback: 원본 없이 서버마다 고치면 버전이 더 어긋난다.
    - id: e
      text: 안내된 사이트를 먼저 확인하고 그 사이트의 문구 버전을 본다
      feedback: 맞다. 손님의 경로에서 사이트, 사이트의 버전 순으로 좁혔다. 📋 순서대로 확인하기를 썼다.
    answer: e
    feedback: 사이트마다 버전이 다를 수 있다. 손님이 간 사이트를 확인하고 그 사이트의 버전을 확인하는 순서가 원인을 좁힌다.
  question_placements:
  - question_id: u13-l03-p06-q01
    after_paragraph: 3
- page_id: advanced-source-18-page-07
  illustrations:
  - file: assets/animations/u13-l03-p7-cdn.svg
    title: "사진과 화면은 더 가까이 둘 수 없을까?"
    alt: "도쿄 손님이 서울 원본에서 3MB 사진을 받다가 도쿄 에지에 사본을 저장해 두고 이후 가까운 에지에서 바로 받으며, 개인 응답은 캐시하지 않는 모습입니다."
    caption: "CDN은 누구에게나 같은 정적 파일만 가까이 캐시하고 개인 응답은 캐시하지 않습니다."
    after_paragraph: 2
  questions:
  - id: u13-l03-p07-q01
    kind: choice
    difficulty: easy
    prompt: CDN에 맡기기에 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: 손님마다 입력이 달라서 매번 새로 생성되는 AI 견적 답변
      feedback: 개인별 답변은 캐시하지 않고 원본으로 보낸다.
    - id: b
      text: 모든 손님에게 똑같은 시공 사례 사진 파일
      feedback: 맞다. 모든 손님에게 같은 정적 파일은 가까운 에지에 캐시하기 좋다.
    - id: c
      text: 결제 승인 요청
      feedback: 요청마다 처리해야 하는 동작이라 캐시 대상이 아니다.
    - id: d
      text: 로그인한 손님의 개인 상담 기록과 견적 이력 전체
      feedback: 개인 내용은 캐시 대상이 아니다.
    - id: e
      text: 서버 상태 확인(헬스 체크) 요청
      feedback: 실시간 상태 확인은 캐시하면 의미가 없다.
    answer: b
    feedback: CDN은 공통 정적 파일을 손님 가까이에 캐시한다. 손님마다 다른 내용은 원본에서 만든다.
  - id: u13-l03-p07-q02
    kind: choice
    difficulty: medium
    prompt: CDN을 붙인 뒤 수정한 시공 사례 사진이 일부 지역에서 하루 동안 예전 사진으로 보인다. 원인과 다음에 바꿀 방법으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: DNS TTL이 짧아 옛 주소가 남은 탓이므로 TTL을 늘려 안정시키고 에지의 사본도 함께 늘린다
      feedback: 맞다. 신선도와 비용 사이의 균형을 따졌다. ⚖️ 대가 따지기를 썼다.
    - id: b
      text: DNS TTL이 짧아 옛 주소가 남은 탓이므로 TTL을 늘려 안정시킨다
      feedback: TTL이 아니라 에지에 보관된 사본의 캐시 시간이 원인이다.
    - id: c
      text: 사진 파일이 업로드 중 손상되어서이므로 모든 에지에 같은 파일을 새로 올리고 캐시 시간을 더 길게 잡는다
      feedback: 손상이 아니라 예전 사본이 남은 것이다.
    - id: d
      text: CDN을 끄면 해결되므로 끈다
      feedback: 끄면 해외 첫 화면이 다시 느려진다.
    - id: e
      text: 로드 밸런서를 액티브/액티브로 바꾼다
      feedback: 로드 밸런서와 관계없는 캐시 문제다.
    answer: a
    feedback: 캐시 시간이 길면 반응이 늦고 짧으면 원본 부담이 는다. 파일 이름 버전 붙이기로 둘의 균형을 맞춘다.
  question_placements:
  - question_id: u13-l03-p07-q01
    after_paragraph: 3
- page_id: advanced-source-18-page-08
  illustrations:
  - file: assets/animations/u13-l03-p8-two-layers.svg
    title: "지역을 고른 뒤엔 누가 서버를 고를까?"
    alt: "GSLB가 도쿄 지역을 고르고 도쿄 안의 L4가 서버를 고르며, 서버 한 대 고장은 L4가 빼고 서울 전체 장애는 GSLB가 도쿄로 돌리는 모습입니다."
    caption: "서버 한 대 고장은 지역 안 L4가, 사이트 전체 장애는 GSLB가 처리합니다."
    after_paragraph: 2
  questions:
  - id: u13-l03-p08-q01
    kind: choice
    difficulty: easy
    prompt: GSLB와 지역 안 L4 로드 밸런서의 역할 구분으로 알맞은 것은 무엇인가요?
    choices:
    - id: a
      text: GSLB가 지역 안의 서버 한 대 한 대의 CPU를 직접 보고 연결을 나눠 준다
      feedback: 서버 단위 분배는 지역 안 L4의 역할이다.
    - id: b
      text: L4가 DNS 단계에서 일본과 한국 손님을 나눈다
      feedback: DNS 단계의 지역 선택은 GSLB의 일이다.
    - id: c
      text: 둘은 같은 장치라서 구분이 없다
      feedback: 층이 다르고 반응 속도도 다르다.
    - id: d
      text: GSLB는 DNS에서 지역을, L4는 지역 안에서 서버를 고른다
      feedback: 맞다. 지역을 고르는 층과 서버를 고르는 층이 따로 있다.
    - id: e
      text: GSLB는 헬스 체크를 하지 못한다
      feedback: GSLB도 사이트 상태를 확인해 살아 있는 곳을 고른다.
    answer: d
    feedback: 두 층을 나누면 서버 하나의 고장은 지역 안에서, 사이트 전체의 장애는 DNS 단계에서 처리한다.
  - id: u13-l03-p08-q02
    kind: choice
    difficulty: medium
    prompt: 도쿄 사이트 서버 3대 중 1대가 고장 났는데 지우가 GSLB 설정에서 도쿄를 통째로 빼려 한다. 더 알맞은 대응과 이유는 무엇인가요?
    choices:
    - id: a
      text: GSLB에서 도쿄를 즉시 빼고 일본 고객도 서울 한 곳에서 받아 서버 한 대 고장의 영향을 없앤다
      feedback: 남은 두 대로 충분하다면 불필요하게 거리 지연과 서울 부하를 키운다.
    - id: b
      text: DNS TTL을 하루로 늘려 도쿄를 고정한다
      feedback: TTL이 길면 문제가 생겼을 때 전환이 늦어진다.
    - id: c
      text: L4의 헬스 체크로 그 서버만 빼고 도쿄는 그대로 둔다
      feedback: 맞다. 필요한 층만 쓰는 판단이다. 🗺️ 필요한 것만 남기기를 썼다.
    - id: d
      text: 고장 난 서버가 복구될 때까지 아무것도 하지 않는다
      feedback: 헬스 체크로 고장 난 서버를 풀에서 빼 주지 않으면 손님이 오류를 만난다.
    - id: e
      text: 도쿄 서버를 모두 한꺼번에 재시작한다
      feedback: 정상 서버까지 멈춰 오히려 장애가 커진다.
    answer: c
    feedback: 작은 고장은 지역 안에서 처리하고 GSLB는 사이트 단위 장애에 쓴다. 층마다 맡을 일을 구분한다.
  question_placements:
  - question_id: u13-l03-p08-q01
    after_paragraph: 3
---

## 일본 고객에게만 한결봇이 왜 느릴까?

<!-- learn-page-id: advanced-source-18-page-01 -->

한결디자인이 도쿄에 쇼룸을 열고 일본 고객에게도 한결봇 상담을 열었다. 그런데 서울 서버는 한산한데 일본 고객과 도쿄 쇼룸 직원만 첫 화면이 뜨는 데 1~2초씩 더 걸린다고 한다. 지우는 서울과 도쿄에서 각각 첫 화면 응답 시간을 재 보고, 서 이사에게 "서버 대수는 충분한데 왜 느린가"를 설명해야 한다.

멀리 있는 가게에 전화로 주문하는 상황을 떠올려 보자. 주문 전에 "영업하세요?", "재고 있나요?", "배달되나요?"를 여러 번 묻고 답을 기다려야 한다면, 통화 한 번의 지연이 크지 않아도 횟수만큼 쌓인다. 화면 하나를 여는 일도 한 번의 요청이 아니다. TCP와 TLS 연결을 맺는 데만 몇 번 오가야 하고, 화면을 이루는 사진·스크립트 같은 수십 개 파일을 받으려면 연결을 새로 맺을 때마다 같은 일이 되풀이된다. 브라우저가 파일을 동시에 받아도 한 번에 열 수 있는 연결에는 한계가 있어 왕복이 단계별로 쌓인다. 합쳐 왕복이 20~30번 안팎(가정)이고 서울과 도쿄 사이 왕복이 50ms(가정)라면 1~1.5초, 왕복이 150ms(가정)인 북미 고객이라면 3~4.5초가 된다.

같은 나라 안에서도 비슷한 일이 생긴다. 손님과 서버가 서로 다른 통신사(ISP) 망에 있으면, 망과 망이 만나는 구간을 건너며 경로가 길어지거나 막힐 수 있다. 한 곳의 L4 로드 밸런서와 서버 묶음은 "몇 대가 나눠 맡을까"는 풀어 주지만 "얼마나 먼가"는 풀지 못한다.

해결 방향은 서버 묶음을 여러 지역·여러 망에 두고, 손님을 가까운 곳으로 안내하는 것이다. 손님은 `bot.hangyeol.example`이라는 이름으로 접속을 시작하므로, 안내는 이름을 주소로 바꾸는 DNS에서 할 수 있다. 서울과 도쿄에 각각 대표 주소(서울 `203.0.113.10`, 도쿄 `203.0.113.20`)를 두고 이름이 상황에 맞는 쪽을 알려 주는 식이다.

도쿄에 사이트를 두는 이유는 속도만이 아니다. 서울에 장애가 났을 때의 대피처 역할도 하며, 이는 마지막 Page에서 다시 본다. 대가는 운영할 사이트가 늘어나는 것과, 손님을 어디로 보낼지 정하는 장치가 새로 필요해진다는 점이다.

## DNS가 주소를 둘 알려 주면 해결될까?

<!-- learn-page-id: advanced-source-18-page-02 -->

지우는 `bot.hangyeol.example`에 서울 `203.0.113.10`과 도쿄 `203.0.113.20` 두 주소를 함께 등록했다. 그런데 도쿄 사이트를 점검하는 동안에도 일부 손님이 계속 도쿄로 가서 접속이 지연되거나 실패했다. 주소를 둘 등록하면 알아서 살아 있는 곳으로 갈 줄 알았다.

기본 DNS 방식(DNS 라운드 로빈)은 등록된 주소를 돌아가며 알려 줄 뿐이다. 두 지점의 전화번호가 적힌 전화번호부는 한 지점이 문을 닫아도 그 사실을 알지 못한다. DNS도 그 주소가 지금 살아 있는지 확인하지 않는다. 일부 브라우저는 첫 주소가 실패하면 다음 주소를 시도하지만 클라이언트마다 다르고 실패를 알아채는 데 시간이 걸린다. 서버가 보장하는 장애 전환이 아니다.

여기에 캐시가 겹친다. DNS 답은 TTL(Time To Live) 동안 리졸버, 운영체제, 브라우저에 보관된다. TTL이 3600초(1시간)라면 레코드를 바꿔도 캐시가 끝날 때까지 예전 주소로 간다. 그래서 레코드를 바꾼 순간 모든 손님이 바뀌는 것은 아니다.

해결의 출발점은 GSLB(Global Server Load Balancing)다. GSLB는 DNS가 사이트 상태를 확인해 살아 있는 곳만, 가까운 곳 위주로 알려 주는 방식이다. 이 Lesson에서는 이 DNS 방식을 본다. 점검처럼 바뀔 일이 있는 이름은 TTL을 미리 짧게 낮춰 둔다. 낮춘 TTL이 퍼진 뒤에 주소를 빼야 효과가 있다.

대가도 분명하다. TTL이 짧으면 DNS 질의가 늘고, 모든 캐시가 정한 TTL을 그대로 지킨다는 보장도 없어서 전환이 즉시 끝나지 않는다.

## 이름 하나로 지역마다 다른 주소를 주려면?

<!-- learn-page-id: advanced-source-18-page-05 -->

고객 안내문에는 `bot.hangyeol.example` 한 이름만 쓰고, 어느 지역으로 보낼지는 GSLB를 맡은 쪽에서 바꾸고 싶다. 안내문을 인쇄해 둔 뒤에도 지역 구성을 바꿀 수 있어야 하기 때문이다.

DNS는 최종 IP 주소 대신 다른 이름을 알려 줄 수 있다. 이것이 CNAME(별칭)이다. 명함에 "문의는 고객센터로"라고 적어 두는 것과 같다. 예를 들어 `bot.hangyeol.example`이 GSLB가 관리하는 이름 `jp.bot.gslb.example`을 가리키면, 리졸버는 그 이름을 다시 물어 주소를 받는다. 지역이 정해지는 곳은 GSLB가 이름을 풀어 주는 이 단계이고, 일본 쪽 손님에게는 도쿄 주소 `203.0.113.20`이, 한국 쪽 손님에게는 서울 주소 `203.0.113.10`이 돌아간다.

이 과정은 nslookup으로 직접 볼 수 있다. 아래는 이해를 돕는 예시이고, 실제 결과는 시점과 위치에 따라 다르다.

```text
> nslookup bot.hangyeol.example
bot.hangyeol.example    canonical name = jp.bot.gslb.example
jp.bot.gslb.example     Address: 203.0.113.20
```

이름 → CNAME(중간 이름) → 주소로 이어지는 단계를 짚으면 어느 단계에서 지역 선택이 일어났는지 알 수 있다. 큰 서비스를 조회하면 CDN이나 GSLB 사업자의 이름이 중간에 보이기도 한다.

대가는 묻는 단계가 늘어난다는 점과, 중간 이름을 관리하는 외부 사업자에 기대게 된다는 점이다.

## DNS는 손님이 어디 있는지 어떻게 알까?

<!-- learn-page-id: advanced-source-18-page-06 -->

도쿄 쇼룸의 노트북 한 대만 계속 서울 사이트로 안내된다. 같은 쇼룸의 다른 PC는 도쿄로 잘 가는데 이 노트북만 왜 다를까?

비서를 통해 문의하는 상황과 같다. 받는 쪽은 비서의 위치만 안다. 위치에 따라 다른 답을 주는 권한 DNS 서버가 보는 것은 손님 PC의 IP가 아니라 대신 물어 온 리졸버(로컬 네임 서버)의 IP다. 노트북이 서울에 있는 리졸버나 멀리 있는 공개 DNS를 쓰면 서울 손님으로 판단될 수 있다.

이를 보완하려고 일부 리졸버는 EDNS Client Subnet(ECS)으로 손님 주소의 앞부분(서브넷)을 함께 보낸다. 그러면 권한 DNS가 더 정확히 가까운 곳을 고른다. 다만 모든 리졸버가 ECS를 보내는 것은 아니다.

해결은 같은 망·지역의 리졸버를 쓰게 하는 것이다. 지우가 쇼룸 노트북의 DNS 서버 설정부터 열어 보니, 누군가 공개 DNS 서비스 주소를 손으로 적어 두었다. 이 서비스는 서울 쪽에서 질의를 내보내고 ECS를 보내지 않는다고 가정한다. 같은 쇼룸(`10.20.0.0/24`)의 다른 PC는 DHCP로 도쿄 쪽 리졸버를 자동으로 받고 있어서 도쿄로 잘 갔다. 노트북의 수동 값을 지우고 자동으로 되돌리자 이 노트북도 도쿄로 안내됐다.

대가도 있다. ECS는 손님 위치 정보를 더 넘기는 것이라 개인정보 때문에 꺼리는 리졸버가 있고, 지역별 응답을 관리하는 체계가 필요하다.

## IP 주소만 보고 나라를 알 수 있을까?

<!-- learn-page-id: advanced-source-18-page-09 -->

서 이사가 말한다. "한국 손님은 서울로, 일본 손님은 도쿄로 확실히 나눠 주세요." 손님이 어느 나라에서 왔는지 IP 주소만으로 확실히 알 수 있을까?

우편번호로 동네를 대강 알 수 있는 것과 비슷하다. IP 주소 블록은 지역과 ISP별로 나뉘어 할당되어서, IP 위치 데이터베이스(여러 업체가 판매하는 DB)로 국가, ISP, 도시를 추정할 수 있다. 앞 Page에서 본 리졸버 주소(ECS가 있으면 손님 주소의 앞부분)를 이 DB에 대어 위치를 추정하고, GSLB는 그 결과로 가까운 사이트를 고른다.

하지만 이것은 추정값이다. VPN이나 프록시를 쓰면 출구 쪽 위치로 보이고, 이동통신망이나 주소 재할당 때문에 실제 위치와 다를 수 있다. 같은 주소가 어제와 오늘 다른 지역으로 나올 수도 있다.

그래서 IP 위치 정보는 가까운 지역 서버로 "안내"하는 데는 쓰되, 접근 차단이나 법적 지역 구분처럼 정확해야 하는 판단에는 다른 근거를 함께 쓴다. DB는 계속 갱신해야 하므로 비용도 든다.

한결디자인의 일을 나눠 보자. 일본 손님의 첫 화면을 도쿄에서 주는 일은 위치 추정이 틀려도 조금 느릴 뿐이라 추정값으로 충분하다. 반면 특정 나라 손님에게만 약관을 보여 주는 일처럼 틀리면 곤란한 판단에는 손님이 직접 고른 국가 설정 같은 다른 근거를 더한다. 같은 위치 정보라도 틀렸을 때의 손해에 따라 쓰임이 달라진다.

한국 손님은 서울, 일본 손님은 도쿄로 안내하더라도 두 곳의 상담 내용이 같아야 하고 사이트 운영비도 든다. 위치 판단, 콘텐츠 동기화, 운영 비용을 함께 따져야 한다는 결론이다.

## 서울과 도쿄의 한결봇이 다른 답을 한다면?

<!-- learn-page-id: u13-l03-page-06 -->

시공 단가표를 바꾼 다음 날, 일본 고객만 예전 단가로 견적을 받았다. 같은 한결봇인데 서울과 도쿄에서 다른 답이 나오는 이유는 무엇일까?

본점 메뉴판만 바꾸고 지점 메뉴판을 그대로 두면, 어느 가게로 갔느냐에 따라 가격이 다르다. 한결봇도 새 모델과 상담 지식 문서를 서울에만 올렸고 도쿄 사이트는 그대로였다. 손님이 어느 사이트로 안내되느냐에 따라 결과가 달라진다.

여러 곳이 같은 서비스를 하려면 내용이 같아야 한다. 부하와 헬스 체크만큼 콘텐츠 배포와 동기화도 별도의 과제다. 해결은 원본을 한 곳에 두고 거기서 모든 지역으로 같은 버전을 내보내는 것이다. 각 사이트가 지금 어느 버전을 쓰는지 확인할 수 있게 해 두면 어긋남을 바로 찾는다.

지우는 두 사이트가 어느 버전인지 바로 보이도록, 각 사이트가 응답을 기록할 때 지식 문서 버전 번호(예: `kb-2026-11-12`)를 함께 남기게 했다(가정). 서울은 최신 번호, 도쿄는 하루 전 번호가 찍혀 있으면 어긋난 곳이 바로 보인다.

배포는 서울에서 만든 한 벌을 도쿄로 복사하고, 도쿄에서 확인이 끝난 뒤 완료로 표시하는 순서다. 복사하는 동안 몇 분은 서울만 새 버전일 수 있으므로, 단가표처럼 어긋나면 곤란한 내용은 상담이 적은 시간에 배포한다.

대가도 있다. 배포가 퍼지는 동안에는 잠시 버전이 섞인다. 또 상담 지식 문서와 달리 고객 대화 같은 개인 데이터를 국외로 복제하는 것은 서 이사가 우려하는 문제이므로, 복제할 대상은 최소로 정한다. 이번 Page는 AI가 쓰는 모델과 지식 문서의 동기화이고, 다음 Page는 화면에 뜨는 공통 파일을 가까이 두는 이야기다.

## 사진과 화면은 더 가까이 둘 수 없을까?

<!-- learn-page-id: advanced-source-18-page-07 -->

도쿄 고객은 특히 시공 사례 고화질 사진 때문에 첫 화면이 느렸다. 모든 손님에게 같은 사진과 화면 파일을 매번 서울에서 내려받게 하고 있었기 때문이다.

누구에게나 똑같은 정적 파일도 매번 원본 서버까지 먼 길을 오간다. 편의점 체인은 본사 창고까지 가지 않고 동네 편의점에서 물건을 바로 준다. CDN(콘텐츠 전송 네트워크)이 그런 역할이다. 여러 지역의 서버(에지)에 원본의 사본을 캐시해 두고, 손님을 가까운 에지로 안내해 거기서 바로 준다. 안내는 대개 CNAME과 DNS로 한다.

무엇을 맡길지는 파일의 성격으로 가른다. 사진, 스크립트처럼 누구에게나 같은 공통 파일은 CDN에 맡긴다. 반면 손님마다 다른 AI 답변과 개인 상담 내용은 캐시하지 않고 원본으로 보낸다. 이 구분은 HTTP의 Cache-Control 같은 헤더로 알린다. 개인 응답은 `Cache-Control: private`처럼 공용 캐시에 저장하지 말라고 표시해야 다른 손님에게 노출되지 않는다.

숫자로 보자. 사진 한 장이 3MB(가정)이고 먼 경로에서 왕복이 여러 번 필요하다면, 도쿄 손님이 서울에서 받아 오는 동안 화면이 비어 있다. CDN에 맡기면 각 지역의 에지마다 첫 요청만 원본까지 가고, 이후에는 도쿄 근처의 에지에 남아 있는 사본을 받는다. 같은 사진을 수백 명이 보는 날일수록 원본 서버 부담도 함께 줄어든다.

대가도 있다. 사본이 오래 남으면 고친 파일이 늦게 반영된다. 그래서 캐시 시간, 파일 이름에 버전 붙이기(예: `hero-v2.jpg`), 삭제 요청(purge)을 관리해야 한다. 사용량만큼 비용도 든다.

## 지역을 고른 뒤엔 누가 서버를 고를까?

<!-- learn-page-id: advanced-source-18-page-08 -->

도쿄 사이트에도 GPU 서버가 세 대 있다. 이 중 한 대가 고장 났을 때 GSLB가 도쿄 전체를 빼야 할까? 일본 고객 모두가 서울로 몰리면 이번에는 거리 문제가 다시 생긴다.

두 층이 일을 나눈다고 생각하면 쉽다. 공항 안내와 공항 안의 게이트 배정이다. 먼저 어느 공항(지역)으로 갈지를 정하고, 그 안에서 어느 게이트로 갈지를 정한다. 이 Lesson에서 본 DNS 방식의 GSLB는 DNS 단계에서 사이트 상태, 부하, 손님 위치(리졸버 IP·ECS), 응답 시간, 비용 같은 기준으로 지역을 고른다. 각 지역의 대표 주소(서울 `203.0.113.10`, 도쿄 `203.0.113.20`) 뒤에서는 다시 L4 로드 밸런서가 헬스 체크를 하며 서버를 고른다.

기준은 단순하다. 서버 한 대 고장은 지역 안 L4가 처리하고, 사이트 전체 장애는 GSLB가 처리한다.

서울 사이트 전체가 응답하지 않으면 GSLB가 상태 확인으로 알아채고 도쿄 주소만 알려 준다. TTL을 60초(가정)로 낮춰 두었다면 몇 분 안에 손님이 도쿄로 모이고, 그 사이 도쿄는 평소보다 많은 요청을 받는다.

대가는 속도 차이다. GSLB의 판단은 DNS 답이 캐시되는 동안 바뀌지 않으므로 사이트 전환은 지역 안 서버 전환보다 느리다. 그래서 작은 고장은 지역 안에서 빠르게 흡수하고, GSLB는 큰 장애에 맡기는 것이 합리적이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 멀리 있는 손님의 느림은 서버 대수가 아니라 거리와 망 경로 때문이다. DNS 기반 분산은 TTL 캐시와 리졸버 위치의 영향을 받고, GSLB는 지역을, 지역 안 L4는 서버를 고른다. CDN은 공통 정적 파일만 가까이 캐시한다.
- **적용하기 (Apply):** "해외 손님이 느리다"면 서버 사용률로 용량을 먼저 가르고, nslookup으로 이름 → CNAME → 주소를 따라가 손님이 어느 사이트로 안내됐는지 확인한다. 전환이 필요하면 TTL을 미리 낮춘다.
- **찾아보기 (Lookup):** DNS 관리 화면에서 레코드의 TTL과 CNAME을, 사용 중인 GSLB·CDN 서비스의 설정 화면에서 지역 선택 기준, 캐시 시간, 삭제(purge) 기능이 어디에 있는지 찾아본다.

### 🧠 이번에 쓴 생각법

- 🗺️ **필요한 것만 남기기:** 지역은 GSLB가, 서버는 지역 안 L4가 맡게 두 층의 일을 나눠 서버 한 대의 고장에 도쿄 전체를 빼지 않기로 했다.
- 📋 **순서대로 확인하기:** nslookup으로 이름 → CNAME → 주소를 차례로 따라가며 어느 단계에서 지역이 정해졌는지, 어느 리졸버가 물었는지 확인했다.
- ⚖️ **대가 따지기:** TTL의 길이, IP 위치 판단의 정확도, CDN 캐시의 신선도처럼 빠름과 최신성 사이의 대가를 견줬다.

한결봇을 서울과 도쿄에서 막힘없이 쓰게 만드는 일은 여기까지다. 하지만 도쿄 쇼룸 직원과 재택 근무 중인 박 팀장에게는 새 숙제가 남았다. 이들이 쓸 사내 AI는 인터넷에 공개한 한결봇이 아니라 사내 문서와 이어져야 쓸모가 있는데, 그 문서는 인터넷에 내놓을 수 없다. 다음 Unit 14에서는 사내망을 인터넷 너머로 안전하게 잇는 VPN으로 이 문제를 푼다. 한편 이번 Unit에서 지우는 서버를 풀에 넣고 뺄 때마다 헬스 체크 결과를 확인하고, 서울과 도쿄의 응답 시간을 일일이 재 보았다. 이런 수작업 확인은 사이트와 서버가 늘수록 평소와 다른 징후를 놓치기 쉬워, 자동으로 감지할 필요가 생긴다. 이는 Module 4(이상탐지 자동화)에서 다룬다.
