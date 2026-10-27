# 왕초보 길잡이 36개와 Wiki 목차 대응 조사

- 기준 목차: `course-network/studio/wiki/oeweo-network/catalog.json`
- 왕초보 파일: `course-network/studio/wiki/oeweo-network/newbie/specs/lesson-01.json`–`lesson-36.json`
- 원본 저장소 checkout HEAD: `90a5cc40` (조사 시점). 보충 원고와 SVG는 로컬 미커밋 파일이므로 이 대응은 로컬 작업본 기준.

## 대응 결과

왕초보 길잡이 36개는 기초편의 강의 소개 1개를 제외한 원본 강의 항목 2–37과 번호가 한 칸 차이 나며 주제가 일치한다: `왕초보 lesson-NN` ↔ `기초편 원본 항목 NN+1`. 조사한 첫 항목은 비트/바이트, 마스크, 16진수, 프로세스, OSI, User/Kernel mode, 버퍼, 개념/구현 등 9개 개념을 풀어 쓴다. 파일 번호가 일치한다고 원문을 그대로 복제한다는 뜻은 아니다.

## Unit 후보별 배치

| Unit 후보 | Wiki 대분류 | 원본 항목 | 왕초보 보충 원고 | 판단 메모 |
|---:|---|---:|---:|---|
| 1 | 들어가기에 앞서... | 1–5 (5) | 01–04 (4개) | 선수지식·Layer·컴퓨터 기초가 포함되어 범위가 큼 |
| 2 | Internet 기반 네트워크 입문 | 6–8 (3) | 05–07 (3개) | Wiki 원문 강의 순서를 따름 |
| 3 | L2수준에서 외울 것들 | 9–11 (3) | 08–10 (3개) | Wiki 원문 강의 순서를 따름 |
| 4 | L3 수준에서 외울 것들 | 12–25 (14) | 11–24 (14개) | Wiki 원문 강의 순서를 따름 |
| 5 | L4 수준 대표주자 TCP와 UDP | 26–31 (6) | 25–30 (6개) | Wiki 원문 강의 순서를 따름 |
| 6 | 웹을 이루는 핵심기술 | 32–37 (6) | 31–36 (6개) | Wiki 원문 강의 순서를 따름 |
| 7 | 네트워크 장치의 구조 | 1–9 (9) | 없음 | 응용편 목차; 별도 왕초보 보충 파일 없음 |
| 8 | 인터넷 공유기 작동원리 | 10–16 (7) | 없음 | 응용편 목차; 별도 왕초보 보충 파일 없음 |
| 9 | 부하분산 시스템 작동원리 | 17–18 (2) | 없음 | 응용편 목차; 별도 왕초보 보충 파일 없음 |
| 10 | VPN과 네트워크 보안 솔루션 | 19–23 (5) | 없음 | 응용편 목차; 별도 왕초보 보충 파일 없음 |

## 세부 대응표

### Unit 후보 1: 들어가기에 앞서...

- 원본 항목 01 **강의소개** — 별도 왕초보 보충 파일 없음 (과정 소개)
- 원본 항목 02 **수강 전에 알고 있다고 가정하는 것들** ↔ 왕초보 `lesson-01.json` (9개 개념; 선수 지식(prerequisite), 비트(bit), AND 연산, 16진수)
- 원본 항목 03 **Layer와 Layered 구조** ↔ 왕초보 `lesson-02.json` (6개 개념; Layer(레이어), 시스템(system), 의존(dependence), 전제(premise))
- 원본 항목 04 **네트워크와 네트워킹 그리고 개념** ↔ 왕초보 `lesson-03.json` (6개 개념; 네트워크(Network), 상호작용 조건, 계층(Layer), 프로토콜(protocol))
- 원본 항목 05 **User mode와 Kernel mode** ↔ 왕초보 `lesson-04.json` (7개 개념; 하드웨어(Hardware), 장치 드라이버(Device driver), 인터페이스(Interface), 소켓(Socket))

### Unit 후보 2: Internet 기반 네트워크 입문

- 원본 항목 06 **OSI 7 layer와 식별자 (강의자료 PDF 포함)** ↔ 왕초보 `lesson-05.json` (9개 개념; OSI 7 layer, 장치 드라이버(Device driver), 식별자(Identifier), MAC 주소(MAC address))
- 원본 항목 07 **Host는 이렇게 외우자 (인쇄용 강의자료 PDF 포함)** ↔ 왕초보 `lesson-06.json` (8개 개념; 호스트(Host), 스위치(Switch), 엔드포인트(End point), 클라이언트(Client))
- 원본 항목 08 **스위치가 하는 일과 비용** ↔ 왕초보 `lesson-07.json` (8개 개념; 스위치(Switch), 패킷(Packet), MAC 주소, 메트릭(Metric))

### Unit 후보 3: L2수준에서 외울 것들

- 원본 항목 09 **NIC, L2 Frame, LAN 카드 그리고 MAC 주소** ↔ 왕초보 `lesson-08.json` (8개 개념; NIC (Network Interface Card), 호스트 (Host), LAN (Local Area Network), MAC 주소 (Media Access Control address))
- 원본 항목 10 **L2 스위치에 대해서** ↔ 왕초보 `lesson-09.json` (8개 개념; 스위칭 (Switching), 도식, LED, Link up (링크 업))
- 원본 항목 11 **LAN과 WAN의 경계 그리고 Broadcast** ↔ 왕초보 `lesson-10.json` (10개 개념; 유니캐스트 (Unicast), 브로드캐스트 도메인 (Broadcast Domain), 16진수 (Hexadecimal), 프레임 (Frame))

### Unit 후보 4: L3 수준에서 외울 것들

- 원본 항목 12 **IPv4주소의 기본 구조** ↔ 왕초보 `lesson-11.json` (7개 개념; MAC 주소 (Media Access Control address), 비트 (bit), ipconfig, Network ID (네트워크 식별자))
- 원본 항목 13 **L3 IP Packet으로 외워라** ↔ 왕초보 `lesson-12.json` (7개 개념; 패킷 (Packet), IP (Internet Protocol), MTU (Maximum Transmission Unit), 헤더 (Header))
- 원본 항목 14 **Encapsulation과 Decapsulation** ↔ 왕초보 `lesson-13.json` (5개 개념; Encapsulation(캡슐화), 단위화, 세그먼트(Segment), Decapsulation(디캡슐화))
- 원본 항목 15 **패킷의 생성과 전달** ↔ 왕초보 `lesson-14.json` (9개 개념; 패킷 (packet), 호스트 (host), 프로세스 (process), 포트 번호 (port number))
- 원본 항목 16 **계층별 데이터 단위** ↔ 왕초보 `lesson-15.json` (6개 개념; Frame(프레임), Socket(소켓), MTU(Maximum Transmission Unit), Segmentation(분할))
- 원본 항목 17 **[※중요] 이해하면 인생이 바뀌는 TCP/IP 송·수신구조** ↔ 왕초보 `lesson-16.json` (14개 개념; MTU (Maximum Transmission Unit), 서버 (Server), 프로세스 (Process), 버퍼 (Buffer))
- 원본 항목 18 **IP 헤더 형식** ↔ 왕초보 `lesson-17.json` (8개 개념; 헤더 (Header), 비트 (bit), Total Length, 단편화 (Fragmentation))
- 원본 항목 19 **서브넷 마스크와 CIDR** ↔ 왕초보 `lesson-18.json` (6개 개념; 네트워크 ID(Network ID), 비트(bit), AND 연산, 클래스(Class))
- 원본 항목 20 **Broadcast IP주소** ↔ 왕초보 `lesson-19.json` (6개 개념; 비트(bit), 브로드캐스트 주소(broadcast address), 유니캐스트(unicast), 액세스 스위치(access switch))
- 원본 항목 21 **Host 자신을 가리키는 IP주소** ↔ 왕초보 `lesson-20.json` (6개 개념; 원격지(Remote), 프로세스(Process), 소켓(Socket), 인터페이스(Interface))
- 원본 항목 22 **TTL과 단편화** ↔ 왕초보 `lesson-21.json` (10개 개념; Router(라우터), Forwarding(전달), TTL(Time To Live), 8비트)
- 원본 항목 23 **인터넷 설정 자동화를 위한 DHCP** ↔ 왕초보 `lesson-22.json` (9개 개념; IP 주소, 수동 설정, DHCP, Static(정적))
- 원본 항목 24 **ARP** ↔ 왕초보 `lesson-23.json` (10개 개념; IP 주소, ARP, 브로드캐스트, 패킷(Packet))
- 원본 항목 25 **Ping과 RTT** ↔ 왕초보 `lesson-24.json` (7개 개념; 동기화(Synchronization), RTT(Round Trip Time), 응답 시간, DoS / DDoS)

### Unit 후보 5: L4 수준 대표주자 TCP와 UDP

- 원본 항목 26 **TCP와 UDP 개요** ↔ 왕초보 `lesson-25.json` (10개 개념; 프로토콜(protocol), 연결 지향(Connection-oriented), 순서번호(Sequence number), 바이트(byte))
- 원본 항목 27 **TCP 연결과정** ↔ 왕초보 `lesson-26.json` (8개 개념; 3-way handshake, RTT, SYN, ACK)
- 원본 항목 28 **TCP 연결종료 및 상태변화** ↔ 왕초보 `lesson-27.json` (9개 개념; FIN, 상태(State), CLOSE_WAIT, TIME_WAIT)
- 원본 항목 29 **TCP, UDP 헤더형식과 게임서버 특징** ↔ 왕초보 `lesson-28.json` (8개 개념; 포트 번호 (Port Number), Sequence Number, 제어 플래그 (Control Flag), Retransmission (재전송))
- 원본 항목 30 **TCP '연결'이라는 착각** ↔ 왕초보 `lesson-29.json` (8개 개념; LAN 케이블, 물리 계층(L1), 소켓(Socket), Heartbeat(하트비트))
- 원본 항목 31 **TCP 연결과 게임버그** ↔ 왕초보 `lesson-30.json` (7개 개념; 엔드포인트(endpoint), MMORPG, 동기화(synchronization), 아이템 복제 버그)

### Unit 후보 6: 웹을 이루는 핵심기술

- 원본 항목 32 **한 번에 끝내는 DNS** ↔ 왕초보 `lesson-31.json` (13개 개념; DNS(Domain Name System), 계층(hierarchy), Domain name, ISP)
- 원본 항목 33 **웹 기술 창시자와 대한민국 인터넷** ↔ 왕초보 `lesson-32.json` (9개 개념; 웹(Web), CERN, 하이퍼텍스트(Hypertext), 프로토콜(Protocol))
- 원본 항목 34 **URL과 URI** ↔ 왕초보 `lesson-33.json` (10개 개념; URL(Uniform Resource Locator), 자원(Resource), JSON, Scheme(스킴))
- 원본 항목 35 **굵고 짧게 살펴보는 HTTP** ↔ 왕초보 `lesson-34.json` (9개 개념; Stream(스트림), 헤더(header), Request / Response, Wireshark)
- 원본 항목 36 **그림 한 장으로 외워서 끝내는 웹 서비스 구조 기본이론** ↔ 왕초보 `lesson-35.json` (17개 개념; 스트림(Stream), 웹 클라이언트(Web Client), DNS(Domain Name System), 유지보수(Maintenance))
- 원본 항목 37 **WAS와 RESTful API 그리고 JVM** ↔ 왕초보 `lesson-36.json` (14개 개념; Tier(티어), APM, JVM, 런타임(runtime))

### Unit 후보 7: 네트워크 장치의 구조

- 원본 항목 01 **강의소개 및 교육목표** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 02 **세 가지 네트워크 장치 구조** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 03 **Inline 구조 (강의자료 포함)** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 04 **강의자료 - 인쇄용** — 대응하는 왕초보 보충 파일 없음 [다운로드 자료: 수업 Lesson 여부 결정 필요]
- 원본 항목 05 **Out of path 구조와 DPI 그리고 망중립** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 06 **Proxy - 우회** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 07 **Proxy - 보호와 감시** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 08 **Reverse Proxy** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 09 **PC에 설치하는 Proxy** — 대응하는 왕초보 보충 파일 없음

### Unit 후보 8: 인터넷 공유기 작동원리

- 원본 항목 10 **공유기 작동원리 및 개요** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 11 **Symmetric NAT 방식** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 12 **Full Cone 방식과 내부 네트워크 접속 문제** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 13 **Restricted Cone 방식** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 14 **Port Restricted Cone 방식** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 15 **포트 포워딩** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 16 **UPnP와 NAT** — 대응하는 왕초보 보충 파일 없음

### Unit 후보 9: 부하분산 시스템 작동원리

- 원본 항목 17 **L4 부하분산과 무정지 시스템** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 18 **대규모 부하분산을 위한 GSLB** — 대응하는 왕초보 보충 파일 없음

### Unit 후보 10: VPN과 네트워크 보안 솔루션

- 원본 항목 19 **PN과 VPN** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 20 **IPSec VPN과 터널링 개념** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 21 **VPN과 재택근무** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 22 **VPN 악용** — 대응하는 왕초보 보충 파일 없음
- 원본 항목 23 **네트워크 보안 솔루션 종류** — 대응하는 왕초보 보충 파일 없음

## 검토가 필요한 점

- 번호 기반 대응은 기초편의 36개 강의 원고와 보충 파일의 실제 주제를 표본 대조해 확인했다. Unit 1부터 Unit 6까지 순서대로 배치하는 것은 조사 결과이며, 최종 콘텐츠 Lesson 경계 승인과는 구분한다.
- 응용편 4개 대분류(Unit 후보 7–10)에는 별도 `newbie/specs` 대응 파일이 없다. 초보자 관점의 기초 설명이 필요한 용어를 응용편 안에서 보충할지, 기초편에서 연결 링크를 둘지는 아직 정하지 않았다.
- 원문 항목 가운데 인쇄 자료 다운로드가 별도 강의로 계산되어 있는 경우가 있다. Learn의 Lesson으로 옮기기 전에 읽기 자료/첨부 파일로 처리할지 판단해야 한다.
- 기초편 첫 대분류 안에는 소개 항목, 보충 lesson 4개, 선수지식 9개념 등이 있어, Unit 1이 긴 단일 묶음이 되는지 또는 Wiki 대분류를 유지하면서 내부 Lesson을 더 나누는지 검토가 필요하다.
