# Unit 14 적용 대응표 (옛 page_id → 새 Lesson·Page)

Lesson (폴더는 `units/10-vpn-and-security/lessons/restructured/`)

| 새 Lesson | id | 폴더 | Page |
| - | - | - | - |
| 14-1 도쿄 쇼룸에서도 사내 AI를 쓰려면: 왜 VPN인가 | u10-advanced-19-pn과-vpn (유지) | 01-왜-vpn인가 | 7 |
| 14-2 봉투 속 봉투: 터널을 지나는 패킷 | u10-advanced-20-ipsec-vpn과-터널링-개념 (유지) | 02-터널을-지나는-패킷 | 6 |
| 14-3 터널을 열기 전 두 장비의 약속: IPsec | advanced-vpn-ipsec-agreement (신규) | 03-ipsec-두-장비의-약속 | 6 |
| 14-4 집에서 사내 AI 열기: 원격 접속 VPN | advanced-remote-access-vpn (유지) | 04-원격-접속-vpn | 7 |
| 14-5 VPN을 켜면 나는 어디에 있는 걸까: IP로 판단하는 한계 | advanced-vpn-ip-trust-limits (신규) | 05-ip로-판단하는-한계 | 8 |

Page (새 page_id는 흡수한 첫 옛 page_id, 없으면 `u14-l{LL}-page-{NN}`)

| 옛 page_id | 새 Page | 새 page_id |
| - | - | - |
| advanced-source-19-page-01, -02 | 14-1 p1 | advanced-source-19-page-01 |
| advanced-source-19-page-03, -04 | 14-1 p2 | advanced-source-19-page-03 |
| advanced-source-19-page-05 | 14-1 p3 | advanced-source-19-page-05 |
| advanced-source-19-page-06 | 14-1 p4 | advanced-source-19-page-06 |
| advanced-source-19-page-07, advanced-source-20-page-03 | 14-1 p5 | advanced-source-19-page-07 |
| advanced-source-19-page-08, advanced-source-20-page-02 | 14-1 p6 | advanced-source-19-page-08 |
| advanced-source-19-page-09 | 14-1 p7 | advanced-source-19-page-09 |
| advanced-source-20-page-07, -08, -09 | 14-2 p1 | advanced-source-20-page-07 |
| advanced-source-20-page-06, -12 | 14-2 p2 | advanced-source-20-page-06 |
| advanced-source-20-page-10 | 14-2 p3 | advanced-source-20-page-10 |
| advanced-source-20-page-11 | 14-2 p4 | advanced-source-20-page-11 |
| advanced-source-20-page-13 | 14-2 p5 | advanced-source-20-page-13 |
| (신규: MTU·포장 오버헤드) | 14-2 p6 | u14-l02-page-06 |
| advanced-source-20-page-01 | 14-3 p1 | advanced-source-20-page-01 |
| advanced-source-20-page-04 | 14-3 p2 | advanced-source-20-page-04 |
| (신규: PSK·인증서) | 14-3 p3 | u14-l03-page-03 |
| advanced-source-20-page-05 | 14-3 p4 | advanced-source-20-page-05 |
| (신규: NAT-T) | 14-3 p5 | u14-l03-page-05 |
| (신규: SSL/TLS VPN 비교) | 14-3 p6 | u14-l03-page-06 |
| advanced-source-21-page-01, -02 | 14-4 p1 | advanced-source-21-page-01 |
| advanced-source-21-page-03, -04 | 14-4 p2 | advanced-source-21-page-03 |
| advanced-source-21-page-05 | 14-4 p3 | advanced-source-21-page-05 |
| advanced-source-21-page-06 | 14-4 p4 | advanced-source-21-page-06 |
| advanced-source-21-page-07, -08 | 14-4 p5 | advanced-source-21-page-07 |
| advanced-source-21-page-09 | 14-4 p6 | advanced-source-21-page-09 |
| advanced-source-21-page-10 | 14-4 p7 | advanced-source-21-page-10 |
| advanced-source-22-page-01, -02 | 14-5 p1 | advanced-source-22-page-01 |
| advanced-source-22-page-03, -04 | 14-5 p2 | advanced-source-22-page-03 |
| advanced-source-22-page-05 | 14-5 p3 | advanced-source-22-page-05 |
| advanced-source-22-page-06 | 14-5 p4 | advanced-source-22-page-06 |
| advanced-source-22-page-07 | 14-5 p5 | advanced-source-22-page-07 |
| advanced-source-22-page-08 | 14-5 p6 | advanced-source-22-page-08 |
| advanced-source-22-page-09 | 14-5 p7 | advanced-source-22-page-09 |
| advanced-source-22-page-10 | 14-5 p8 | advanced-source-22-page-10 |

검산: 옛 42개 page_id가 한 번씩 흡수됨. 신규 Page 4개(14-2 p6, 14-3 p3·p5·p6). 옛 Lesson 3개에서 `advanced-source-22-*`는 14-5로, `-21-*`은 14-4로 이동.
