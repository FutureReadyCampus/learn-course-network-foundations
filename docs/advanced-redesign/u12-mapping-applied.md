# Unit 12 적용 대응표 (옛 page_id → 새 Lesson·Page)

Lesson 폴더: `units/08-router-and-nat/lessons/restructured/`

| 새 Lesson | id(유지) | 폴더 | Page |
| --- | --- | --- | --- |
| 12-1 사무실에선 되는데 밖에선 안 되는 AI 서버 | u8-advanced-10-공유기-작동원리-및-개요 | 01-사무실에선-되는데-밖에선-안-되는-ai-서버 | 6 |
| 12-2 답장은 어떻게 제자리로 돌아올까: NAT 변환표 | u8-advanced-11-symmetric-nat-방식 | 02-답장이-제자리로-돌아오는-nat-변환표 | 7 |
| 12-3 밖에서 사내 AI 서버로 들어오는 길: 포트 포워딩 | u8-advanced-15-포트-포워딩 | 03-밖에서-사내-ai-서버로-들어오는-포트-포워딩 | 7 |
| 12-4 누가 몰래 포트를 열었을까: UPnP | u8-advanced-16-upnp와-nat | 04-누가-몰래-포트를-열었나-upnp | 6 |
| 12-5 포트를 안 열어도 화상회의가 되는 이유: NAT 통과 | advanced-nat-mapping-filtering | 05-포트를-안-열어도-되는-nat-통과 | 7 |

## 새 Page의 page_id와 흡수한 옛 page_id

| 새 Page | page_id | 흡수한 옛 page_id |
| --- | --- | --- |
| 12-1 p1 | advanced-source-10-page-01 | 10-01, 10-06, 15-04 |
| 12-1 p2 | advanced-source-10-page-02 | 10-02 |
| 12-1 p3 | advanced-source-10-page-07 | 10-07 |
| 12-1 p4 | advanced-source-10-page-03 | 10-03 |
| 12-1 p5 | advanced-source-10-page-04 | 10-04 |
| 12-1 p6 | advanced-source-10-page-09 | 10-09 |
| 12-2 p1 | advanced-source-11-page-01 | 11-01, 11-02 |
| 12-2 p2 | advanced-source-11-page-03 | 11-03, 11-04 |
| 12-2 p3 | advanced-source-11-page-05 | 11-05 |
| 12-2 p4 | advanced-source-11-page-06 | 11-06, 11-11 |
| 12-2 p5 | advanced-source-11-page-07 | 11-07, 11-08 |
| 12-2 p6 | advanced-source-11-page-09 | 11-09 |
| 12-2 p7 | advanced-source-15-page-01 | 15-01 |
| 12-3 p1 | advanced-source-15-page-02 | 15-02 |
| 12-3 p2 | advanced-source-15-page-03 | 15-03 |
| 12-3 p3 | advanced-source-15-page-05 | 15-05, 15-06 |
| 12-3 p4 | advanced-source-15-page-07 | 15-07 |
| 12-3 p5 | u12-l03-page-05 | 없음(새 내용: 헤어핀 NAT) |
| 12-3 p6 | advanced-source-10-page-08 | 10-08 (CGNAT) |
| 12-3 p7 | u12-l03-page-07 | 없음(새 내용: 포트 개방의 대가) |
| 12-4 p1 | advanced-source-16-page-01 | 16-01 |
| 12-4 p2 | advanced-source-15-page-08 | 15-08, 16-04 |
| 12-4 p3 | advanced-source-16-page-02 | 16-02, 16-03 |
| 12-4 p4 | advanced-source-16-page-05 | 16-05, 16-06, 16-07 |
| 12-4 p5 | u12-l04-page-05 | 없음(새 내용: UPnP 무인증 위험) |
| 12-4 p6 | advanced-source-16-page-08 | 16-08 |
| 12-5 p1 | advanced-nat-mapping-filtering-page-01 | nm-01 |
| 12-5 p2 | advanced-nat-mapping-filtering-page-02 | nm-02, 10-05 |
| 12-5 p3 | advanced-nat-mapping-filtering-page-03 | nm-03, 11-10 |
| 12-5 p4 | advanced-nat-mapping-filtering-page-04 | nm-04 |
| 12-5 p5 | advanced-nat-mapping-filtering-page-05 | nm-05 |
| 12-5 p6 | advanced-nat-mapping-filtering-page-06 | nm-06 |
| 12-5 p7 | advanced-nat-mapping-filtering-page-07 | nm-07 |

`advanced-source-NN-page-MM`은 `NN`번 원천 Lesson의 Page MM. 다른 Page에 흡수되어 page_id가 사라진 옛 id: 10-05, 10-06, 11-02, 11-04, 11-08, 11-10, 11-11, 15-04, 15-06, 16-03, 16-04, 16-06, 16-07. `nm-NN`은 `advanced-nat-mapping-filtering-page-NN`.

## 그림
- 유지(내용·주소 일치): 12-1 p1 lan-wan, p4 door, p5 firewall / 12-2 p7 fwd-auto-review(이동) / 12-3 p4 fwd-two-homes, p6 router-cgnat(이동) / 12-4 p2 fwd-manual-pain(이동), p3 upnp-history, p4 upnp-manual-vs-auto, p6 upnp-compare / 12-5 p1 mapping-peers, p2 router-nat-types(이동), p5 mapping-cone, p6 hole-punching, p7 relay.
- 뺀 것(파일은 그대로 남음): `192.168.0.x` 주소가 든 u12-router-nat/public-private/private-ranges/summary, u12-nat-table-* 전체(11개), u12-fwd-private-fail/public-address/response/settings/static(3.3.3.3 등), u12-mapping-eim/filtering/vs-filtering(15.15.15.15 등), u12-upnp-coupon/mapping-request/torrent/dev/pnp.
- 새 그림이 필요한 Page: 12-1 p2·p3·p6, 12-2 p1~p6, 12-3 p1·p2·p3·p5·p7, 12-4 p1·p5, 12-5 p3·p4.
