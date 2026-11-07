# 심화 과정 Unit 11~15 구조 적용 계약

이 문서는 승인된 **5 Unit·20개 기술 Lesson** 구조를 실제 콘텐츠와 Learn에 적용하기 위한 계약이다. 기존 「강의소개 및 교육목표」 8페이지와 인쇄 자료 1페이지는 새 과정 항목으로 만들지 않는다. 감사 스냅샷에는 옛 원고를 보존하지만, 필요한 기술 설명만 관련 Lesson 본문에 옮기고 나머지는 새 목차에서 제외한다. 별도 PDF, 자료 화면, `resources` 카탈로그 필드를 추가하지 않는다.

새 Lesson은 Unit 11→15, 각 Unit 안에서는 Lesson 순서로 기존 전체 순차 잠금에 참여한다. Unit 자유 진입 예외는 만들지 않는다. 이번 구조 PR에서는 기존 Page 본문을 재배치하고 필요한 연결만 최소 수정한다. 충분한 본문 집필은 구조가 `stage`에 게시된 것을 확인한 뒤 기존 Unit별 이슈에서 Lesson 하나씩 진행한다.

## 목표 Unit과 Lesson ID

| Unit | Lesson | 안정 ID |
|---|---|---|
| 11 네트워크 장치의 배치와 프록시 | 장치가 트래픽을 다루는 세 가지 구조 | `u7-advanced-02-세-가지-네트워크-장치-구조` |
|  | 인라인 구조와 트래픽 처리 | `u7-advanced-03-inline-구조-강의자료-포함` |
|  | 경로 밖 관찰과 DPI | `u7-advanced-05-out-of-path-구조와-dpi-그리고-망중립` |
|  | 포워드 프록시와 클라이언트 측 중계 | `advanced-forward-proxy` |
|  | 리버스 프록시와 서버 앞단 | `u7-advanced-08-reverse-proxy` |
| 12 공유기와 NAT의 동작 | 사설 주소·공인 주소와 공유기 | `u8-advanced-10-공유기-작동원리-및-개요` |
|  | NAT 변환표로 통신 따라가기 | `u8-advanced-11-symmetric-nat-방식` |
|  | NAT의 매핑과 수신 허용 방식 | `advanced-nat-mapping-filtering` |
|  | 포트 포워딩으로 내부 서비스 연결하기 | `u8-advanced-15-포트-포워딩` |
|  | UPnP와 자동 포트 설정 | `u8-advanced-16-upnp와-nat` |
| 13 부하 분산과 서비스 가용성 | L4 부하 분산과 서버 상태 확인 | `advanced-l4-load-balancing` |
|  | 이중화로 장애에 대비하기 | `advanced-service-redundancy` |
|  | DNS 기반 부하 분산과 GSLB | `u9-advanced-18-대규모-부하분산을-위한-gslb` |
| 14 VPN과 원격 네트워크 연결 | 사설망을 인터넷으로 연결하는 VPN | `u10-advanced-19-pn과-vpn` |
|  | IPsec과 터널링 | `u10-advanced-20-ipsec-vpn과-터널링-개념` |
|  | 원격 접속 VPN과 사용 시 주의 | `advanced-remote-access-vpn` |
| 15 네트워크 보안 솔루션 | 보안 장치의 배치와 역할 | `advanced-security-placement` |
|  | NAC와 네트워크 접근 통제 | `advanced-network-access-control` |
|  | 방화벽과 연결 상태 추적 | `advanced-stateful-firewall` |
|  | 침입 탐지·차단과 보안 로그 분석 | `advanced-intrusion-and-logs` |

## 원고 범위

기준은 콘텐츠 stage `4269969b0021fa85a3ab55c73c1dde6a66334c75`의 감사 스냅샷이다. 기존 구 Unit 번호는 원고 출처를 뜻하고 새 Unit 번호는 목표 위치다.

- U11L2→새 U11L1, U11L3→새 U11L2, U11L5→새 U11L3.
- U11L6·L7·L9→새 U11L4. 우회·보호·감시·PC 도구 사례를 보존하고 클라이언트 편 중계라는 공통 원리로 연결한다.
- U11L8→새 U11L5. U11L1 소개 8페이지와 U11L4 인쇄자료 1페이지는 새 Lesson이 아니다.
- U12L1→새 U12L1, U12L2→새 U12L2, U12L3·L4·L5→새 U12L3, U12L6→새 U12L4, U12L7→새 U12L5.
- U13L1 P1~7→새 U13L1, P8~9→새 U13L2. P10~11은 이중화 Lesson의 참고 원고로 기록하되 구조 PR에서 자동 본문으로 합치지 않는다. U13L2→새 U13L3.
- U14L1→새 U14L1, U14L2→새 U14L2, U14L3·L4→새 U14L3.
- U14L5 P1~5 / P6~9 / P10~13 / P14~20→새 U15L1 / L2 / L3 / L4.

## 주소와 기록 호환

- 주소의 단원·Lesson 숫자를 새 순서에 바로 대입하지 않는다. 고정된 원본 경로 별칭을 원 Lesson/Page로 해석한 뒤 새 Lesson/Page로 바꾼다. U11L7 P2는 새 U11L4 P9다.
- 새 5 Unit 판본은 `/m2-network/v3/...` 주소를 쓴다. 이전 Learn `/v2` 주소와 콘텐츠 stage의 버전 없는 주소는 별도 namespace로 정확히 대응한다.
- 소개·자료 원고의 URL은 새 기술 Lesson으로 보내지 않는다. 매핑이 없거나 제외된 원고라면 잘못된 기술 내용을 조용히 열지 않고 해석 실패로 남긴다.
- 이전 `NetworkState`, 답안, 이벤트, 완료 기록은 삭제하거나 새 Lesson에 근거 없이 복사하지 않는다. 완전한 원 Lesson 완료 증거가 없으면 병합 Lesson의 완료를 추론하지 않는다. 기록을 바꾸는 승계는 아카이브와 원자적 처리 근거가 있을 때만 수행한다.
- 하나의 공개 원고를 여러 새 Lesson으로 분할할 때는 그 원고가 공개된 경우 각 분할 결과도 공개 후보가 된다. 병합 Lesson은 모든 원고 기여 범위가 공개된 경우에만 공개한다.
- Learn의 순차 완료 검사는 공개된 20개 기술 Lesson에 기존처럼 적용한다. 자료 항목은 없으며 선행 잠금 체인에도 포함되지 않는다.

## 감사 기준과 검증

스냅샷은 기존 원고 23개, 전체 203 Page, SVG 22개의 해시를 보존한다. 이 중 기술 원고 194 Page만 20개 목표 Lesson에 각각 한 번 배정한다. 소개 8 Page와 인쇄자료 1 Page는 audit-only 제외 항목이다. 콘텐츠 stage 및 Learn v2 원고 경로 별칭은 각각 453개, 구판 unversioned 경로 별칭은 447개다(기술 출처에만 연결). 준비 계약에서 사용하던 462/456 및 총 1,380 별칭은 소개·자료 URL까지 목적지에 보내던 과거 제안이며 현재 계약에서는 폐기했다.

`python3 scripts/plan_advanced_restructure.py`의 합성 테스트는 194개 기술 Page, 제외된 9개 Page, 22개 자산 해시, 주소 offset, 병합·분할 경계, 공개 조건 및 부분 완료 fail-closed를 확인한다. `python3 scripts/test_advanced_restructure.py -v`가 통과해야 한다.

Learn #223을 먼저 `main`에 반영하고 Deploy 및 관련 동작을 확인한다. 그 다음 구조 PR을 `stage`에 병합하고 콘텐츠 빌드·자산 참조·20 Lesson·라우트 별칭·기존 순차 제한을 검증한다. Stage의 실제 게시 SHA와 대표 Lesson/Page를 확인한 이후에만 #164~#167 및 #184의 본문 개선을 시작한다.
