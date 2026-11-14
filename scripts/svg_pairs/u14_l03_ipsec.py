#!/usr/bin/env python3
"""Unit 14 Lesson 3 (IPsec, 두 장비의 약속): one 4-step example SVG per Page (6). Run from repo root:
python3 scripts/svg_pairs/u14_l03_ipsec.py   (--svg-only skips the lesson.md edit).

Running example: 도쿄 SG 198.51.100.20 ↔ 서울 SG 198.51.100.25 (IKE/SA/ESP·AH), 박 팀장 집 192.168.0.20 / 공유기 192.0.2.123
(NAT-T), 서 이사 호텔 192.0.2.150 (SSL VPN). Step arc: ① 상황 → ② 동작 → ③ 결과 → ④ 기억할 점."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u14_l01_vpn import *  # noqa: F401,F403
from u14_l01_vpn import new, mark, tube, ip, site, build, ROOT, UNIT, Y


# 1 IPsec 네 조각 확인 순서 ---------------------------------------------------------
def p1():
    a = new()
    rows = ["① IKE 협상 시작 · UDP 500", "② NAT-T · UDP 4500", "③ 협상 내용 · 암호·수명·ESP/AH", "④ 상대 확인 · 사전 공유 키·인증서"]
    ys = [150 + i * 74 for i in range(4)]
    body = [booth(80, Y, "도쿄 SG"), booth(330, Y, "서울 SG"), line(125, Y, 285, Y, LINE, 4, "8 6"),
            cross(205, Y) + pill(205, 225, "터널이 안 서요", RED, 17, False, 190)]
    body += [cell(420, y, 500, 52, r, MUTED, 17) for y, r in zip(ys, rows)]
    body += [a.vis(cell(420, ys[0], 500, 52, rows[0], GREEN, 17), 2, 4), mark(420, ys[0], 500, 52, 2),
             a.vis(cell(420, ys[1], 500, 52, rows[1], GREEN, 17), 3, 4), mark(420, ys[1], 500, 52, 3),
             a.vis(cell(420, ys[2], 500, 52, rows[2], GREEN, 17) + cell(420, ys[3], 500, 52, rows[3], GREEN, 17), 4, 4),
             a.vis(pill(205, 380, "앞에서부터 순서대로", GREEN, 17, True, 210), 4, 4)]
    caps = ["터널이 안 서면 확인할 조각이 네 개예요", "먼저 두 SG가 협상을 시작하는지 봐요", "공유기가 있으면 NAT-T를 바로 다음에 봐요", "협상 내용과 상대 확인까지 차례로 따라가요"]
    return frame(a, "IPsec의 네 조각", "막혔을 때 앞에서부터 확인해요", caps, "".join(body))


# 2 IKE 협상과 SA --------------------------------------------------------------------
def p2():
    a = new()
    sa = "SA: 알고리즘·키·수명"
    body = [booth(200, 280, "도쿄 SG"), booth(760, 280, "서울 SG"), line(250, 280, 710, 280, LINE, 4, "8 6"),
            a.vis(ask(480, 280) + pill(480, 200, "처음 만난 두 장비", BLUE, 18, False), 1, 1),
            a.vis(pill(480, 200, "UDP 500 · 제안 주고받기", VIOLET, 18, True), 2, 2), mark(330, 180, 300, 40, 2),
            mv(a, packet(0, 0, VIOLET), [(260, 262), (700, 262)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, BLUE), [(700, 306), (260, 306)], 2, 2, 2, 0.1, 0.9),
            a.vis(cell(70, 365, 260, 52, sa, GREEN, 16) + cell(630, 365, 260, 52, sa, GREEN, 16) + check(480, 280), 3, 4),
            mark(66, 361, 268, 60, 3), mark(626, 361, 268, 60, 3),
            a.vis(pill(480, 447, "공통 조건 하나를 찾는 일이라 없으면 실패해요", BLUE, 18, True), 4, 4)]
    caps = ["처음 만난 두 SG가 약속을 정해야 해요", "IKE로 암호 방식과 키, 수명을 제안해요", "합의 결과를 SA 메모로 각자 기억해요", "공통으로 허용하는 조건이 없으면 협상이 실패해요"]
    return frame(a, "IKE 협상과 SA", "계약서를 쓰기 전에 조건부터 맞춰요", caps, "".join(body))


# 3 상대 확인 (PSK / 인증서) ------------------------------------------------------------
def p3():
    a = new()
    body = [box(40, 130, 420, 290, BLUE, PANEL, 16, dash=True, sw=3) + text(250, 162, "사전 공유 키 (PSK)", 19, BLUE, 700) + text(250, 192, "미리 정한 암구호", 16, MUTED),
            box(500, 130, 420, 290, VIOLET, PANEL, 16, dash=True, sw=3) + text(710, 162, "인증서", 19, VIOLET, 700) + text(710, 192, "기관이 보증한 신분증", 16, MUTED),
            a.vis(cell(70, 235, 175, 48, "도쿄 SG: 비밀값 A", BLUE, 15) + cell(255, 235, 175, 48, "서울 SG: 비밀값 A", BLUE, 15) + check(250, 320)
                  + pill(250, 375, "같은 값이면 상대를 믿어요", GREEN, 16, False, 250), 2, 4), mark(66, 231, 368, 56, 2),
            a.vis(cell(540, 235, 340, 48, "CA가 '본사 SG가 맞다'고 보증", VIOLET, 15) + check(710, 320)
                  + pill(710, 375, "인증서를 서로 보여 줘요", GREEN, 16, False, 250), 3, 4), mark(536, 231, 348, 56, 3),
            a.vis(pill(480, 457, "상대 확인과 암호화는 다른 일이에요", BLUE, 18, True), 4, 4)]
    caps = ["상대가 진짜 본사 SG인지 확인하는 방법이 둘이에요", "PSK는 양쪽에 미리 넣은 같은 비밀값을 믿어요", "인증서는 기관이 보증한 증명서를 믿어요", "인증은 상대를, 암호화는 내용을 다뤄요"]
    return frame(a, "상대가 진짜 본사 SG일까", "누가 본사 SG인 척하면 어쩌죠?", caps, "".join(body))


# 4 ESP와 AH --------------------------------------------------------------------------
def p4():
    a = new()
    ys = (245, 315, 385)
    names = ["기밀성", "무결성", "인증"]
    body = ["".join(box(100, y - 28, 800, 56, LINE, PANEL, 8, sw=1) + text(130, y + 8, n, 22, TXT, 700, "start") for y, n in zip(ys, names)),
            pill(530, 170, "ESP", GREEN, 20, True, 120), text(530, 206, "불투명 봉투 + 밀봉", 15, MUTED),
            pill(760, 170, "AH", BLUE, 20, True, 120), text(760, 206, "투명 봉투 + 밀봉", 15, MUTED),
            a.vis("".join(check(530, y) for y in ys), 2, 4), mark(465, 215, 130, 200, 2),
            a.vis(cross(760, ys[0]) + check(760, ys[1]) + check(760, ys[2]), 3, 4), mark(695, 215, 130, 200, 3),
            a.vis(pill(480, 453, "비밀 자료는 양쪽 모두 ESP로 맞춰요", GREEN, 18, True), 4, 4)]
    caps = ["보호 세 가지를 ESP와 AH가 어디까지 지킬까요", "ESP는 암호화로 세 가지를 모두 켤 수 있어요", "AH는 무결성·인증만 주고 내용은 그대로 보여요", "도면 같은 비밀 자료는 ESP를 골라요"]
    return frame(a, "ESP와 AH는 뭘 지켜 줄까", "보호 방식을 고르는 기준이에요", caps, "".join(body))


# 5 NAT-T ---------------------------------------------------------------------------------
def p5():
    a = new()
    body = [site(30, 140, 360, 250, "박 팀장 집", MUTED), laptop(110, Y, "박 팀장 노트북"), ip(110, 372, "192.168.0.20"),
            rt(290, Y, "공유기(NAT)"), ip(290, 372, "공인 192.0.2.123"), cloud(550, Y), booth(830, Y, "서울 SG"), ip(830, 372, "198.51.100.25"),
            line(150, Y, 250, Y, LINE, 4), line(330, Y, 480, Y, LINE, 4, "8 6"), line(620, Y, 790, Y, LINE, 4, "8 6"),
            mv(a, packet(0, 0, ORANGE), [(160, Y), (240, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(pill(560, 210, "ESP 패킷", ORANGE, 17, False, 150), 1, 1),
            a.vis(cross(290, 228) + pill(560, 210, "ESP에는 포트 번호가 없어요", RED, 17, False), 2, 2), mark(265, 203, 50, 50, 2),
            a.vis(pill(560, 210, "UDP 4500으로 한 번 더 포장", VIOLET, 17, True), 3, 3), mark(430, 190, 260, 40, 3),
            mv(a, packet(0, 0, VIOLET), [(340, Y), (780, Y)], 3, 3, 3, 0.1, 0.9), a.vis(check(830, 228), 3, 3),
            a.vis(pill(480, 447, "대가: 헤더 한 겹, 그리고 UDP 500·4500을 열어야 해요", BLUE, 17, False), 4, 4)]
    caps = ["집 공유기(NAT)가 끼면 연결이 멈춰요", "ESP에는 포트가 없어 NAT가 구분하지 못해요", "NAT-T가 ESP를 UDP 4500으로 한 번 더 감싸요", "포장만큼 커지고 UDP 500·4500이 열려 있어야 해요"]
    return frame(a, "집 공유기를 만나도 지나갈까", "NAT 통과(NAT-T)가 필요한 이유예요", caps, "".join(body))


# 6 SSL VPN ---------------------------------------------------------------------------------
def p6():
    a = new()
    body = [laptop(120, Y, "서 이사 노트북"), ip(120, 372, "호텔 192.0.2.150"),
            box(330, 220, 130, 160, MUTED, PANEL, 10, sw=3) + text(395, 255, "호텔", 17, TXT, 700) + text(395, 280, "와이파이", 17, TXT, 700),
            booth(820, Y, "본사 SG"), ip(820, 372, "198.51.100.25"),
            line(180, Y, 330, Y, LINE, 4, "8 6"), line(460, Y, 780, Y, LINE, 4, "8 6"),
            a.vis(pill(480, 190, "웹 위주로만 열려 있어요", BLUE, 17, False), 1, 1), mark(335, 170, 290, 40, 1),
            mv(a, packet(0, 0, ORANGE), [(190, Y), (310, Y)], 2, 2, 2, 0.1, 0.9),
            a.vis(cross(395, 200) + pill(480, 160, "IPsec: UDP 500·4500", RED, 17, False, 230), 2, 2), mark(370, 175, 50, 50, 2),
            mv(a, packet(0, 0, GREEN), [(190, Y), (770, Y)], 3, 3, 3, 0.1, 0.9),
            a.vis(pill(480, 160, "SSL VPN: TCP 443", GREEN, 17, True, 230) + check(820, 228), 3, 3), mark(365, 140, 230, 40, 3),
            a.vis(pill(480, 447, "웹이 열려 있으면 SSL VPN은 대개 통과해요", GREEN, 18, True), 4, 4)]
    caps = ["출장지 호텔 와이파이는 웹 위주로만 열려 있어요", "IPsec이 쓰는 UDP 500·4500은 막혀요", "TLS 위의 SSL VPN은 443번 포트로 지나가요", "환경에 따라 IPsec과 SSL VPN을 나눠 써요"]
    return frame(a, "브라우저로 붙는 SSL VPN", "호텔 와이파이에서 IPsec이 안 될 때예요", caps, "".join(body))


ITEMS = [
    ("u14-l03-p1-four-pieces", "IPsec의 네 조각", "터널이 안 설 때 IKE 협상(UDP 500), NAT-T(UDP 4500), 협상 내용, 상대 확인 순서로 앞에서부터 확인한다는 점검 순서입니다.", "터널이 안 서면 IKE, NAT-T, 협상 내용, 상대 확인 순으로 확인합니다.", 3, p1),
    ("u14-l03-p2-ike-sa", "IKE 협상과 SA", "도쿄 SG와 서울 SG가 UDP 500으로 암호 방식·키·수명을 제안해 합의하고, 결과를 각자 SA로 기억하는 모습입니다.", "IKE는 공통 조건을 협상해 SA로 남기며, 공통 조건이 없으면 실패합니다.", 2, p2),
    ("u14-l03-p3-auth", "상대가 진짜 본사 SG일까", "왼쪽은 양쪽이 같은 비밀값을 아는지로 믿는 사전 공유 키, 오른쪽은 인증 기관이 보증한 인증서를 서로 보여 주는 방식입니다.", "상대 확인은 사전 공유 키나 인증서로 하며, 암호화와는 다른 일입니다.", 1, p3),
    ("u14-l03-p4-esp-ah", "ESP와 AH는 뭘 지켜 줄까", "기밀성, 무결성, 인증 세 가지 중 ESP는 모두, AH는 기밀성을 뺀 둘만 지켜 준다는 표 형태의 비교입니다.", "내용이 비밀인 자료는 기밀성이 있는 ESP로 맞춥니다.", 2, p4),
    ("u14-l03-p5-nat-t", "집 공유기를 만나도 지나갈까", "박 팀장 노트북의 ESP 패킷이 포트 번호가 없어 집 공유기(NAT)에서 막히지만, NAT-T가 UDP 4500으로 한 번 더 감싸 서울 SG까지 지나가는 모습입니다.", "NAT가 있으면 ESP를 UDP 4500으로 감싸는 NAT-T를 씁니다.", 2, p5),
    ("u14-l03-p6-ssl-vpn", "브라우저로 붙는 SSL VPN", "호텔 와이파이에서 IPsec의 UDP 500·4500은 막히고 TLS 기반 SSL VPN은 TCP 443으로 본사 SG까지 지나가는 모습입니다.", "웹만 열린 환경에서는 TCP 443을 쓰는 SSL VPN이 대개 통과합니다.", 1, p6),
]
LESSON = next((ROOT / "units").glob(f"{UNIT}/03-*"))

if __name__ == "__main__":
    build(LESSON, ITEMS, "--svg-only" in sys.argv)
