# Unit 13 적용 대응표 (옛 page_id → 새 Lesson·Page)

Lesson id와 폴더는 그대로 유지했다. 폴더는 `units/09-load-balancing/lessons/restructured/` 아래 `01-l4-부하-분산과-서버-상태-확인`, `02-이중화로-장애에-대비하기`, `03-dns-기반-부하-분산과-gslb`다. `unit.md`는 바꾸지 않았다.

| 옛 page_id | 새 Lesson·Page | 새 page_id | 비고 |
| - | - | - | - |
| advanced-source-17-page-01 | 13-1 p2 | advanced-source-17-page-01 | 그대로 |
| advanced-source-17-page-02 | 13-1 p3 | advanced-source-17-page-02 | 그대로 |
| advanced-source-17-page-03 | 13-1 p4 | advanced-source-17-page-03 | 그대로 |
| advanced-source-17-page-04 | 13-1 p5 | advanced-source-17-page-04 | 그대로 |
| advanced-source-17-page-05 | 13-1 p7 | advanced-source-17-page-05 | p2(NAT 대상 변경)는 p2에 흡수 |
| advanced-source-17-page-06 | 13-1 p8 | advanced-source-17-page-06 | 그대로 |
| advanced-source-17-page-07 | 13-2 p1 | advanced-source-17-page-07 | LB 자체 정지 문장에서 출발 |
| advanced-source-17-page-08 | 13-2 p2 | advanced-source-17-page-08 | VIP·가상 MAC은 p3 |
| advanced-source-17-page-09 | 13-2 p3 | advanced-source-17-page-09 | p4·p5에도 나눠 흡수 |
| advanced-source-17-page-10 | 13-2 p6 | advanced-source-17-page-10 | page-11 내용 합침 |
| advanced-source-17-page-11 | 13-2 p6 | (page-10 사용) | 합침 |
| advanced-source-18-page-01 | 13-3 p1 | advanced-source-18-page-01 | page-03·04 합침 |
| advanced-source-18-page-02 | 13-3 p2 | advanced-source-18-page-02 | 콘텐츠 일관성은 p6 |
| advanced-source-18-page-03 | 13-3 p1 | (page-01 사용) | 합침 |
| advanced-source-18-page-04 | 13-3 p1 | (page-01 사용) | 합침 |
| advanced-source-18-page-05 | 13-3 p3 | advanced-source-18-page-05 | |
| advanced-source-18-page-06 | 13-3 p4 | advanced-source-18-page-06 | |
| advanced-source-18-page-07 | 13-3 p7 | advanced-source-18-page-07 | |
| advanced-source-18-page-08 | 13-3 p8 | advanced-source-18-page-08 | nslookup 예는 p3 |
| advanced-source-18-page-09 | 13-3 p5 | advanced-source-18-page-09 | page-10 합침 |
| advanced-source-18-page-10 | 13-3 p5 | (page-09 사용) | 합침 |
| advanced-source-18-page-11 | 13-3 p8 | (page-08 사용) | 합침 |
| (신규) | 13-1 p1 | u13-l01-page-01 | |
| (신규) | 13-1 p6 | u13-l01-page-06 | L4/L7 |
| (신규) | 13-2 p4 | u13-l02-page-04 | |
| (신규) | 13-2 p5 | u13-l02-page-05 | |
| (신규) | 13-3 p6 | u13-l03-page-06 | |

참고: 블루프린트 표는 13-2 p3 대신 p5가 17-09를 받는 것으로 적었으나, "처음 흡수하는 미사용 old page_id" 규칙을 순서대로 적용해 p3가 받았다. `docs/advanced-route-aliases.json`은 건드리지 않았다.
