---
id: u6-l31-한-번에-끝내는-dns
title: 한 번에 끝내는 DNS
source_wiki: https://github.com/physical-spark/course-network/blob/d1b650e39cb0fd01f4b67adb76926172dbd517c9/studio/wiki/oeweo-network/lesson-31.md
wiki_diagram: units/06-web-fundamentals/lessons/01-한-번에-끝내는-dns/assets/diagrams/lesson-31.svg
page_metadata:
- terms:
  - DNS(Domain Name System)
  - IP 주소
  animations:
  - file: l31-dns-phonebook.svg
    title: 이름을 번호로 바꿔 주는 DNS
    alt: 왼쪽 컴퓨터가 www.naver.com이라는 말풍선을 DNS 주소록 아이콘에 보내자, 주소록이 숫자 주소 하나를 담아 돌려보내고 컴퓨터가
      그 주소로 연결선을 긋는 장면입니다.
    caption: 브라우저가 이름을 들고 DNS에 물으면, DNS가 IP 주소를 돌려줍니다.
- terms:
  - 계층(hierarchy)
  - 분산(distributed)
- terms:
  - Domain name
  - Host name
- terms:
  - ISP
  - 공유기
- terms:
  - DNS 서버 주소
  - 8.8.8.8
- terms:
  - DNS Cache
  - TTL(Time To Live)
  animations:
  - file: l31-dns-cache-ttl.svg
    title: DNS 캐시와 유효 시간
    alt: PC의 메모에 3.3.3.3이 적히고 2시간 타이머가 줄어드는 동안 재접속은 바로 되다가, 타이머가 0이 되면 메모가 지워지고 다시
      DNS에 묻는 장면입니다.
    caption: 한 번 받은 답을 유효 시간 동안 기억해 두었다가 쓰고, 시간이 끝나면 다시 묻습니다.
- terms:
  - DNS 변조
- terms:
  - 주 DNS / 보조 DNS
- terms:
  - hosts 파일
  - DNS Forwarding
- terms:
  - 캐시 DNS
- terms:
  - Root DNS
- terms:
  - TLD(Top Level Domain)
  - 담당 서버
  animations:
  - file: l31-dns-hierarchy.svg
    title: 루트에서 담당 서버까지 따라가기
    alt: 캐시 DNS가 루트 서버에 묻자 .com 담당 서버를 안내받고, .com 서버에 묻자 naver.com 담당 서버를 안내받고, 마지막으로
      담당 서버에서 www의 IP 주소를 받는 세 단계의 장면입니다.
    caption: 캐시 DNS가 루트, .com, naver.com 담당 서버 순으로 안내를 받아 내려갑니다.
- terms:
  - 권한 있는 서버(담당 네임 서버)
animations_dir: units/06-web-fundamentals/lessons/01-한-번에-끝내는-dns/assets/animations
---

핵심 개념을 주제별로 정리했다.

## DNS가 필요한 이유
<!-- learn-page-id: dns-purpose -->

L1~L4를 애플리케이션의 통신을 받쳐 주는 인프라로 보면, 그 위의 서비스가 사용자가 실제로 이용하는 목적에 가깝다. 애플리케이션 수준의 서비스 중에서도 다른 서비스를 지원하는 인프라 역할을 하는 것이 DNS다. www.naver.com을 입력해 웹 서버에 접속하려면 먼저 IP 주소를 알아야 한다. DNS는 이름을 바탕으로 주소를 찾는 기능을 제공한다. 전화번호 안내 114나 이름으로 번호를 찾는 휴대전화 주소록에 비유할 수 있다. 이름 해석이 제대로 되지 않으면 서비스 접속 자체가 어려워지므로 DNS는 인터넷에서 중요한 자원이다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** DNS는 사람이 읽는 도메인 이름을 네트워크 주소로 찾도록 돕는다.
- **적용하기 (Apply):** URL 이름을 IP로 해석하는 이유와 접속 뒤 남는 일을 구별한다.
- **찾아보기 (Lookup):** DNS 응답의 type과 cache 동작은 DNS 설명에서 확인한다.

## 도메인 이름과 IP 주소

DNS의 기본 기능은 도메인 이름에 대응하는 IP 주소를 알려 주는 것이다. 이를 관리하는 체계는 계층적인 트리 형태의 분산 구조다. www.naver.com에서는 www가 naver.com에 속하고, naver.com은 더 큰 .com 체계 안에 속하는 방식으로 읽을 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 도메인 이름은 DNS 질의에 쓰이고 IP 주소는 Packet 전달에 쓰인다.
- **적용하기 (Apply):** 같은 도메인이 여러 IP를 돌려줄 수 있는 환경을 설명한다.
- **찾아보기 (Lookup):** 도메인 소유·레코드 정보는 권한 DNS와 조회 도구에서 확인한다.

## Host name과 Domain name
<!-- learn-page-id: domain-name-definition -->

주소를 큰 단위부터 쓰는 한국식 주소와 달리 도메인 이름은 오른쪽으로 갈수록 더 큰 범위를 나타낸다. 이 예에서 naver.com은 도메인 이름, 그 안의 www는 호스트 이름으로 설명한다. 브라우저는 이 전체 이름을 이용해 주소를 질의하고, 운영체제와 함께 얻은 결과로 접속한다. 사용자가 이런 내부 동작을 직접 수행하지 않아도 된다는 점에서 이름과 IP의 연결 과정이 잘 드러나지 않을 수 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Hostname은 네트워크 장치의 이름이고 Domain name은 DNS 계층의 이름이다.
- **적용하기 (Apply):** PC hostname과 `www.example.com`의 서로 다른 범위를 구분한다.
- **찾아보기 (Lookup):** 검색 suffix와 완전한 도메인 이름 표기는 OS 설정에서 찾아본다.

## 분산된 DNS 서버

KT, LG U+, SK브로드밴드 같은 ISP의 회선을 이용하고, 집에서는 공유기에 여러 PC나 모바일 기기를 연결할 수 있다. 이 구성에서 한 PC의 사용자가 브라우저에 이름을 입력했을 때, 어느 DNS에 질의하고 어떻게 다른 서버들과 연결되는지 살펴보자.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** DNS는 계층적으로 위임된 여러 서버가 이름 정보를 나눠 관리한다.
- **적용하기 (Apply):** Resolver가 답을 찾기 위해 다른 DNS 서버를 조회하는 이유를 말한다.
- **찾아보기 (Lookup):** Recursive와 authoritative 역할은 DNS 구조도에서 확인한다.

## 주소를 입력한 뒤의 질의

PC는 네트워크 설정에 지정된 DNS 서버로 이름을 질의한다. 예시 주소는 환경과 시점에 따라 달라질 수 있으므로 실제 설정에서 확인한다. DNS가 www.naver.com의 IP를 응답하면 PC가 그 주소로 접속한다. 실제 서비스에는 부하분산 등의 추가 과정이 있을 수 있지만 여기서는 기본 흐름만 설명한다. DNS 응답이 느리면 웹 서버가 정상이어도 사용자는 사이트가 느리다고 느낄 수 있다. Google DNS 8.8.8.8처럼 공개 DNS를 사용할 수 있지만, ISP DNS와 질의 경로 및 정책이 다를 수 있으므로 사용 환경에 맞춰 선택한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 사용자는 이름을 입력하지만 Resolver가 캐시와 DNS 질의를 통해 주소를 찾는다.
- **적용하기 (Apply):** 브라우저 요청 전 DNS 질의가 발생하는 경로를 순서대로 설명한다.
- **찾아보기 (Lookup):** 브라우저·OS·공유기별 DNS cache 위치는 환경에서 확인한다.

## DNS Cache와 TTL
<!-- learn-page-id: dns-cache-ttl -->

DNS 응답에는 캐시할 수 있는 유효 시간이 함께 온다. www.naver.com의 주소를 설명용으로 3.3.3.3, 유효 시간을 2시간이라고 가정하면 PC는 그 대응 관계를 메모리에 저장한다. 이것이 DNS Cache다. 유효 기간 안에 같은 이름을 다시 사용하면 DNS에 매번 묻는 대신 캐시를 이용할 수 있다. 기간이 지나면 다시 질의한다. 이로써 질의 지연과 DNS의 부하를 줄인다. Windows의 displaydns 옵션으로 캐시를 조회하는 방법도 소개한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TTL은 DNS 레코드가 cache에 보관될 수 있는 시간을 정한다.
- **적용하기 (Apply):** 주소 변경 후 cache가 남아 즉시 바뀌지 않을 수 있음을 예측한다.
- **찾아보기 (Lookup):** 레코드 TTL 값과 cache flush 명령은 DNS 설정에서 확인한다.

## 잘못된 응답과 DNS 변조

이름 해석 결과가 잘못되면 사용자는 의도와 다른 주소로 접속할 수 있다. 네이버를 물었는데 다른 사이트의 주소를 알려 주는 가정으로 DNS 변조의 영향을 설명한다. 2000년대 초반의 1.25 인터넷 대란은 DNS 장애의 영향과 함께 언급되곤 한다. 사건의 세부 원인 분석과 별개로, DNS 장애와 변조가 많은 서비스에 영향을 줄 수 있다는 점을 기억한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 위조 DNS 응답은 잘못된 주소로 사용자를 유도할 수 있다.
- **적용하기 (Apply):** 의심스러운 응답을 정상 권한 서버와 비교해 검증한다.
- **찾아보기 (Lookup):** DNSSEC 검증과 보호 범위는 보안 문서에서 찾아본다.

## 주 DNS와 보조 DNS

DNS가 동작하지 않으면 이름을 이용하는 서비스 접속이 어려워진다. 웹 서비스에 대한 의존도가 높을수록 영향도 커질 수 있다. 다만 PC가 매번 외부 DNS에 직접 묻는 것은 아니다. 먼저 살펴본 DNS 캐시와 더불어 로컬의 이름 해석 정보도 알아둘 필요가 있다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 주·보조 DNS 서버는 이름 해석 가용성을 위해 함께 설정될 수 있다.
- **적용하기 (Apply):** 첫 Resolver 응답이 없을 때 보조 서버가 사용될 수 있음을 이해한다.
- **찾아보기 (Lookup):** 네트워크가 실제 사용하는 DNS 주소는 OS 설정에서 확인한다.

## hosts 파일과 우선 참조

Windows의 hosts 파일에는 이름과 IP 주소의 대응 관계를 직접 적을 수 있다. 해당 정보가 적용되면 외부 DNS에 묻지 않고 로컬의 값을 이용한다. 악성코드가 이를 변조한 사례가 있어 보안 프로그램이 hosts 파일을 보호하기도 한다. PC의 DNS 주소가 공유기 주소인 192.168.0.1로 설정될 수도 있다. 이때 공유기가 DNS Forwarding으로 실제 DNS에 질의를 전달하고 응답을 대신 중계하는 구성이 가능하다. 따라서 이름 해석에는 hosts 파일, 유효한 DNS 캐시, 공유기의 전달 기능 등이 개입할 수 있다. 항상 외부 DNS에 새 질의가 나가는 것은 아니다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** hosts 파일은 DNS 질의 전에 특정 이름을 주소에 대응시킬 수 있다.
- **적용하기 (Apply):** 로컬 hosts 항목이 외부 DNS 결과보다 우선할 수 있음을 진단한다.
- **찾아보기 (Lookup):** Windows·macOS·Linux hosts 파일 경로와 권한은 OS 문서에서 찾아본다.

## 처음 모르는 이름을 찾는 과정

ISP의 DNS 서버가 처음 접한 이름의 답을 모르는 상황을 생각해 보자. 서버의 설정에 따라 동작은 달라질 수 있으며, 다음은 설명을 위해 선택한 기본 예다. PC가 사용하는 서버는 결과를 저장하는 캐시 DNS로 설명한다. 이 서버에도 답이 없으면 계층적인 DNS 체계를 따라 담당 서버를 찾는다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** 처음 모르는 이름은 로컬 cache 확인 뒤 Resolver가 DNS 위임 경로를 따라 찾는다.
- **적용하기 (Apply):** 캐시 미스에서 권한 응답까지 한 질의가 이어지는 흐름을 그린다.
- **찾아보기 (Lookup):** 실제 질의 서버와 응답은 `dig`/`nslookup` 출력에서 확인한다.

## Root DNS

계층의 출발점에는 Root DNS가 있다. 캐시 DNS는 루트의 정보를 바탕으로 다음에 물어볼 담당 서버를 찾는다. 은행의 은행에 비유하면 DNS를 위한 DNS라는 역할로 이해할 수 있다. 루트 서버를 ‘약 13대’로 단순화해 설명하고 IANA.org의 주소 정보를 언급한다. 이 수량 표현을 실제 물리 서버 전체 개수로 이해할 수 있는지는 별도 확인이 필요하다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Root DNS는 TLD 서버의 위치를 알려 주는 계층 최상단의 DNS다.
- **적용하기 (Apply):** Root 서버가 최종 웹사이트 IP를 직접 모두 답하는 것은 아님을 구분한다.
- **찾아보기 (Lookup):** Root zone과 root server 주소 정보는 IANA 자료를 찾아본다.

## TLD와 담당 서버로 이어가기

www.naver.com을 찾는다면 루트 쪽에서 .com을 담당하는 DNS 정보를 얻고, 그 서버에 naver.com의 담당 서버를 질의하는 흐름이다. 각 단계에서 최종 IP를 바로 받는 대신 다음에 질의할 서버의 정보를 얻을 수 있다. 담당 서버가 여러 개라면 그 목록 중 하나로 이어서 질의한다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** TLD 서버는 `.com` 같은 영역의 담당 authoritative server를 안내한다.
- **적용하기 (Apply):** 도메인 끝부분을 기준으로 다음 담당 서버로 질의가 위임됨을 설명한다.
- **찾아보기 (Lookup):** 최상위 도메인의 정책과 담당 정보는 IANA root zone에서 확인한다.

## 권한 있는 서버에서 주소 찾기

최종적으로 naver.com의 담당 네임 서버에 www라는 호스트를 질의해 IP 주소를 얻는다. 캐시 DNS는 이름과 IP의 대응 관계를 저장하고 이후 같은 질의에 재사용한다. 매번 루트부터 전체 과정을 반복하는 것은 아니다. 도메인을 운영하면 그 안의 호스트와 하위 도메인 등을 담당 서버에서 관리한다. 이 정보가 변조되면 도메인 전체 서비스에 영향을 줄 수 있어 변경 권한과 보안 관리가 중요하다. 이러한 이름 해석을 바탕으로 이후 웹 기술을 살펴본다.

### 이 Lesson에서 가져갈 것

- **기억하기 (Recall):** Authoritative server는 해당 도메인의 공식 레코드 정보를 제공한다.
- **적용하기 (Apply):** Resolver가 최종 권한 서버 응답에서 A/AAAA 주소를 얻는 과정을 말한다.
- **찾아보기 (Lookup):** 레코드 변경과 위임 현황은 DNS 관리 도구에서 찾아본다.
