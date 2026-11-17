#!/usr/bin/env python3
"""Unit 14 Lesson 3 (IPsec, 두 장비의 약속) SVG 점검 개정판. Run from repo root:
python3 scripts/svg_pairs/u14_l03_rev.py   (--svg-only skips the lesson.md edit).

공유 헬퍼는 import만 한다. 예시: 도쿄 SG 198.51.100.20 ↔ 서울 SG 198.51.100.25, 박 팀장 집 192.168.0.20 / 공유기 192.0.2.123,
서 이사 호텔 192.0.2.150. Step arc: ① 상황 → ② 동작 → ③ 결과 → ④ 기억할 점. 방금 바뀐 요소만 주황 테두리."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u14_l01_vpn import *  # noqa: F401,F403
from u14_l01_vpn import new, mark, ip, site, build, ROOT, UNIT, Y
from u6_l03 import arrow


def lab(a, x, y, s, color, t, filled=False, fs=17, t2=None):
    """단계 t(~t2)에 보이는 알약 라벨 + 같은 단계의 주황 테두리."""
    w = tw(s, fs) + 28
    h = fs + 16
    return (a.vis(pill(x, y, s, color, fs, filled, w), t, t2 or t) + a.vis(hl(x - w / 2, y - h / 2, w, h, ORANGE, h / 2), t, t))


def env(x, y, c, see_through=False, label="견적서"):
    """봉투 그림: 불투명(ESP) / 투명 + 밀봉 스티커(AH)."""
    top = f'<path d="M{x - 42} {y - 28} L{x} {y + 2} L{x + 42} {y - 28}" fill="none" stroke="{c}" stroke-width="3"/>'
    if see_through:
        return (box(x - 42, y - 28, 84, 56, c, "none", 6, dash=True, sw=3) + text(x - 8, y + 8, label, 16, TXT, 700)
                + f'<circle cx="{x + 29}" cy="{y + 19}" r="7" fill="{c}"/>')
    return box(x - 42, y - 28, 84, 56, c, PANEL, 6, sw=3) + top + f'<circle cx="{x}" cy="{y + 2}" r="8" fill="{c}"/>'


# 1 확인 순서 -------------------------------------------------------------------------
def p1():
    a = new()
    rows = [("협상 시작(IKE)", "시작도 못 하고 '협상 실패' · 의심: 두 SG 사이 UDP 500"),
            ("NAT 통과(NAT-T)", "공유기 뒤에서 '연결 중'만 반복 · 의심: NAT-T 설정, UDP 4500"),
            ("협상 내용(암호 방식·수명·ESP 또는 AH)", "협상 실패 메시지 · 의심: 양쪽 제안에 공통 조건이 있는가"),
            ("상대 확인", "인증 실패 메시지 · 의심: 사전 공유 키·인증서가 같은가")]
    X0, W, H = 320, 610, 66
    ys = [138 + 76 * i for i in range(4)]
    base, lit = [], []
    for i, ((n, s), y) in enumerate(zip(rows, ys)):
        assert tw(n, 18) <= W - 80 and tw(s, 15) <= W - 80, n
        base.append(box(X0, y, W, H, LINE, PANEL, 8, sw=2) + f'<circle cx="{X0 + 30}" cy="{y + H / 2}" r="15" fill="{LINE}"/>'
                    + text(X0 + 30, y + H / 2 + 6, str(i + 1), 18, TXT, 700)
                    + text(X0 + 62, y + 28, n, 18, TXT, 700, "start") + text(X0 + 62, y + 53, s, 15, MUTED, None, "start"))
        lit.append(box(X0, y, W, H, GREEN, "none", 8, sw=3) + f'<circle cx="{X0 + 30}" cy="{y + H / 2}" r="15" fill="{GREEN}"/>'
                   + text(X0 + 30, y + H / 2 + 6, str(i + 1), 18, BG, 700))
    body = ["".join(base),
            booth(70, 260, "도쿄 SG"), booth(270, 260, "서울 SG"), line(112, 260, 228, 260, LINE, 4, "8 6"),
            a.vis(cross(170, 260) + pill(170, 190, "터널이 안 서요", RED, 17, False, 190), 1, 2),
            a.vis(lit[0], 2, 4), mark(X0, ys[0], W, H, 2),
            a.vis(rt(170, 260, "공유기(NAT)"), 3, 4), a.vis(lit[1], 3, 4), mark(X0, ys[1], W, H, 3),
            a.vis(lit[2] + lit[3], 4, 4), mark(X0, ys[2], W, H, 4), mark(X0, ys[3], W, H, 4),
            a.vis(pill(170, 375, "앞에서부터 순서대로", GREEN, 17, True, 210), 4, 4)]
    caps = ["터널이 안 서면 확인할 조각이 네 개예요", "먼저 두 SG가 협상을 시작하는지 봐요", "공유기가 끼면 2번이 3·4번보다 먼저 막혀요", "나머지도 앞에서부터 순서대로 확인해요"]
    return frame(a, "터널이 안 뜰 때 확인 순서", "막히는 증상과 의심할 곳을 한 줄로 묶었어요", caps, "".join(body))


# 2 IKE 협상과 SA (정상) ---------------------------------------------------------------
def p2():
    a = new()
    sa = "SA: 알고리즘·키·수명"
    body = [mv(a, packet(0, 0, VIOLET), [(260, 262), (700, 262)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, BLUE), [(700, 306), (260, 306)], 2, 2, 2, 0.1, 0.9),
            booth(200, 280, "도쿄 SG"), booth(760, 280, "서울 SG"), line(250, 280, 710, 280, LINE, 4, "8 6"),
            a.vis(ask(480, 280) + pill(480, 200, "처음 만난 두 장비", BLUE, 18, False), 1, 1),
            lab(a, 480, 200, "IKE(키 교환 협상) · UDP 500", VIOLET, 2, True, 18),
            a.vis(text(480, 372, "암호 알고리즘·키·수명을 제안해요", 17, TXT), 2, 2),
            a.vis(cell(70, 365, 260, 52, sa, GREEN, 16) + cell(630, 365, 260, 52, sa, GREEN, 16) + check(480, 280), 3, 4),
            mark(70, 365, 260, 52, 3), mark(630, 365, 260, 52, 3),
            a.vis(arrow(290, 670, 240, VIOLET, 5) + arrow(670, 290, 336, BLUE, 5), 4, 4),
            a.vis(pill(480, 198, "도쿄→서울 SA", VIOLET, 17, True, 170) + pill(480, 378, "서울→도쿄 SA", BLUE, 17, True, 170), 4, 4),
            mark(290, 226, 380, 28, 4), mark(290, 322, 380, 28, 4)]
    caps = ["처음 만난 두 SG가 약속을 정해야 해요", "IKE로 암호 방식과 키, 수명을 제안해요", "합의 결과를 SA 메모로 각자 기억해요", "SA는 방향마다 따로 하나씩 생겨요"]
    return frame(a, "IKE 협상과 SA", "계약서를 쓰기 전에 조건부터 맞춰요", caps, "".join(body))


# 2b 협상 실패 -------------------------------------------------------------------------
def p2b():
    a = new()
    old, strong = "구형 암호 방식만 허용", "강한 암호 방식만 허용"
    body = [mv(a, packet(0, 0, VIOLET), [(260, 262), (700, 262)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, BLUE), [(700, 306), (260, 306)], 2, 2, 2, 0.1, 0.9),
            booth(200, 240, "새 도쿄 SG"), booth(760, 240, "본사 SG"), line(250, 240, 710, 240, LINE, 4, "8 6"),
            cell(70, 335, 260, 52, old, VIOLET, 16), cell(630, 335, 260, 52, strong, BLUE, 16),
            a.vis(pill(480, 170, "터널이 '협상 실패'에서 멈춰요", RED, 18, False), 1, 1),
            lab(a, 480, 170, "IKE 제안 주고받기 · UDP 500", VIOLET, 2, True, 18),
            a.vis(cross(480, 240) + pill(480, 432, "공통 조건이 없어 SA가 생기지 않아요", RED, 18, False), 3, 3), mark(455, 215, 50, 50, 3),
            a.vis(pill(480, 432, "제안·수명·UDP 500부터 대조해요", GREEN, 18, True), 4, 4)]
    caps = ["새 도쿄 SG와 본사 SG의 허용 조건이 달라요", "두 SG가 서로 제안을 주고받아요", "공통으로 허용하는 조건이 없어요", "그래서 두 SG의 제안이 맞는지 먼저 대조해요"]
    return frame(a, "공통 조건이 없으면 협상 실패", "협상은 공통 조건을 하나 찾는 일이에요", caps, "".join(body))


# 3 상대 확인 -------------------------------------------------------------------------
def p3():
    a = new()
    body = [booth(120, 150, "도쿄 SG"), booth(840, 150, "본사 SG라는 장비"), line(165, 150, 795, 150, LINE, 4, "8 6"), ask(480, 150),
            box(40, 225, 420, 200, BLUE, PANEL, 16, dash=True, sw=3) + text(250, 255, "사전 공유 키 (PSK)", 20, BLUE, 700) + text(250, 280, "미리 정한 암구호", 16, MUTED),
            box(500, 225, 420, 200, VIOLET, PANEL, 16, dash=True, sw=3) + text(710, 255, "인증서", 20, VIOLET, 700) + text(710, 280, "기관이 보증한 신분증", 16, MUTED),
            a.vis(cell(52, 298, 194, 46, "도쿄 SG: 비밀값 A", BLUE, 16) + cell(254, 298, 194, 46, "서울 SG: 비밀값 A", BLUE, 16)
                  + pill(250, 392, "같은 값이면 상대를 믿어요", GREEN, 17, False, 250) + check(412, 392), 2, 4), mark(52, 298, 396, 46, 2),
            a.vis(cell(512, 298, 396, 46, "CA가 '본사 SG가 맞다'고 보증", VIOLET, 16)
                  + pill(710, 392, "인증서를 서로 보여 줘요", GREEN, 17, False, 250) + check(872, 392), 3, 4), mark(512, 298, 396, 46, 3),
            a.vis(pill(480, 456, "상대 확인과 암호화는 다른 일이에요", BLUE, 18, True), 4, 4)]
    caps = ["상대가 진짜 본사 SG인지 확인하는 방법이 둘이에요", "PSK는 양쪽에 미리 넣은 같은 비밀값을 믿어요", "인증서는 기관이 보증한 증명서를 믿어요", "인증은 상대를, 암호화는 내용을 다뤄요"]
    return frame(a, "상대가 진짜 본사 SG일까", "누가 본사 SG인 척하면 어쩌죠?", caps, "".join(body))


# 4 ESP와 AH --------------------------------------------------------------------------
def p4():
    a = new()
    ys = (254, 314, 374)
    rows = [("기밀성", "내용을 못 읽게 가려요"), ("무결성", "내용이 안 바뀌었는지 확인해요"), ("인증", "상대가 맞는지 확인해요")]
    ex, ax = 590, 810
    body = ["".join(box(40, y, 880, 50, LINE, PANEL, 8, sw=1) + text(60, y + 33, n, 20, TXT, 700, "start") + text(150, y + 32, g, 16, MUTED, None, "start")
                    for y, (n, g) in zip(ys, rows)),
            env(ex, 160, GREEN) + pill(ex, 222, "ESP · 암호화 + 밀봉", GREEN, 17, True, 210),
            env(ax, 160, BLUE, True) + pill(ax, 222, "AH · 밀봉만", BLUE, 17, True, 210),
            a.vis("".join(check(ex, y + 25) for y in ys), 2, 4), mark(ex - 45, 250, 90, 178, 2),
            a.vis(cross(ax, ys[0] + 25) + check(ax, ys[1] + 25) + check(ax, ys[2] + 25), 3, 4), mark(ax - 45, 250, 90, 178, 3),
            a.vis(pill(480, 456, "비밀 자료는 양쪽 모두 ESP로 맞춰요", GREEN, 18, True), 4, 4)]
    caps = ["보호 세 가지를 ESP와 AH가 어디까지 지킬까요", "ESP는 암호화로 세 가지를 모두 켤 수 있어요", "AH는 무결성·인증만 주고 내용은 그대로 보여요", "거래처 자료 같은 비밀 자료는 ESP를 골라요"]
    return frame(a, "ESP와 AH는 뭘 지켜 줄까", "봉투로 떠올리면 쉬워요", caps, "".join(body))


# 5 AH는 NAT를 못 지난다 ---------------------------------------------------------------
def nat_scene():
    return [site(30, 140, 360, 250, "박 팀장 집", MUTED), laptop(110, Y, "박 팀장 노트북"), ip(110, 372, "192.168.0.20"),
            cloud(550, Y), booth(830, Y, "서울 SG"), ip(830, 372, "198.51.100.25")]


def p5():
    a = new()
    body = nat_scene()[:3]
    body += [line(150, Y, 250, Y, LINE, 4), line(330, Y, 480, Y, LINE, 4, "8 6"), line(620, Y, 790, Y, LINE, 4, "8 6"),
             rt(290, Y, "공유기(NAT)"), ip(290, 372, "공인 192.0.2.123")] + nat_scene()[3:]
    body += [mv(a, packet(0, 0, BLUE), [(160, Y), (232, Y)], 1, 1, 1, 0.1, 0.9)]
    body += [lab(a, 620, 195, "AH 패킷 · 출발 192.168.0.20", BLUE, 1),
             lab(a, 640, 195, "공유기가 출발을 192.0.2.123으로 바꿔요", ORANGE, 2),
             a.vis(packet(760, Y, BLUE) + cross(830, 228), 3, 3), mark(805, 203, 50, 50, 3),
             lab(a, 610, 195, "AH: 주소가 바뀌면 변조로 보고 버려요", RED, 3),
             lab(a, 640, 195, "그래서 NAT 뒤에서는 ESP를 써요", GREEN, 4, True)]
    # 2단계 이후 1단계 라벨은 위 lab의 t 범위(1~1)로 사라진다.
    caps = ["집 노트북의 AH 패킷이 공유기를 만나요", "공유기가 패킷의 출발 주소를 바꿔요", "AH는 바뀐 주소를 변조로 보고 버려요", "NAT 뒤에서는 ESP를 써야 해요"]
    return frame(a, "AH는 NAT를 못 지나가요", "주소가 바뀌면 AH는 변조로 봐요", caps, "".join(body))


# 5b NAT-T ----------------------------------------------------------------------------
def p5b():
    a = new()
    body = nat_scene()[:3]
    body += [line(150, Y, 250, Y, LINE, 4), line(330, Y, 480, Y, LINE, 4, "8 6"), line(620, Y, 790, Y, LINE, 4, "8 6"),
             rt(290, Y, "공유기(NAT)"), ip(290, 372, "공인 192.0.2.123")] + nat_scene()[3:]
    body += [mv(a, packet(0, 0, GREEN), [(160, Y), (232, Y)], 1, 1, 1, 0.1, 0.9),
             mv(a, packet(0, 0, VIOLET), [(350, Y), (430, 230), (550, 205), (670, 230), (765, Y)], 3, 3, 3, 0.1, 0.9)]
    body += [lab(a, 620, 165, "ESP 패킷", GREEN, 1),
             lab(a, 620, 165, "ESP에는 포트 번호가 없어요", RED, 2), a.vis(cross(290, 228), 2, 2), mark(265, 203, 50, 50, 2),
             lab(a, 620, 165, "UDP 4500으로 한 번 더 포장", VIOLET, 3, True), a.vis(check(830, 228), 3, 3),
             a.vis(pill(250, 410, "패킷이 포장만큼 커져요", BLUE, 17, False, 250) + pill(700, 410, "UDP 500·4500을 열어야 해요", BLUE, 17, False, 280)
                   + pill(480, 450, "NAT-T는 ESP를 감싸요 · AH는 못 살려요", GREEN, 17, True, 400), 4, 4)]
    caps = ["NAT 뒤에서 ESP 패킷을 보내요", "ESP에는 포트가 없어 NAT가 구분하지 못해요", "NAT-T가 ESP를 UDP 4500으로 한 번 더 감싸요", "대가는 커진 패킷과 열어야 할 UDP 500·4500이에요"]
    return frame(a, "집 공유기를 만나도 지나갈까", "NAT 통과(NAT-T)가 필요한 이유예요", caps, "".join(body))


# 6 SSL/TLS VPN -----------------------------------------------------------------------
def p6():
    a = new()
    body = [mv(a, packet(0, 0, ORANGE), [(190, Y), (310, Y)], 2, 2, 2, 0.1, 0.9),
            mv(a, packet(0, 0, GREEN), [(190, Y), (770, Y)], 3, 3, 3, 0.1, 0.9),
            laptop(120, Y, "서 이사 노트북"), ip(120, 372, "호텔 192.0.2.150"),
            line(180, Y, 330, Y, LINE, 4, "8 6"), line(460, Y, 780, Y, LINE, 4, "8 6"),
            box(330, 220, 130, 160, MUTED, PANEL, 10, sw=3) + text(395, 285, "호텔", 18, TXT, 700) + text(395, 312, "와이파이", 18, TXT, 700),
            booth(820, Y, "본사 SG"), ip(820, 372, "198.51.100.25"),
            lab(a, 395, 172, "웹 위주로만 열려 있어요", BLUE, 1),
            lab(a, 395, 172, "IPsec: UDP 500·4500", RED, 2), a.vis(cross(460, Y), 2, 2), mark(444, 284, 32, 32, 2),
            lab(a, 560, 172, "SSL/TLS VPN: TCP 443", GREEN, 3, True), a.vis(check(820, 228), 3, 3),
            a.vis(pill(480, 447, "웹이 열려 있으면 SSL/TLS VPN은 대개 통과해요", GREEN, 18, True), 4, 4)]
    caps = ["출장지 호텔 와이파이는 웹 위주로만 열려 있어요", "IPsec이 쓰는 UDP 500·4500은 막혀요", "TLS 위의 VPN은 443번 포트로 지나가요", "환경에 따라 IPsec과 SSL/TLS VPN을 나눠 써요"]
    return frame(a, "브라우저로 붙는 SSL/TLS VPN", "호텔 와이파이에서 IPsec이 안 될 때예요", caps, "".join(body))


# 6b 무엇에 무엇을 쓰나 ---------------------------------------------------------------------
def p6b():
    a = new()
    ys = [124, 222, 320]
    H = 90
    data = [(house, "지사끼리", "도쿄 지사 ↔ 서울 본사", "IPsec", VIOLET, "망 전체 연결", "IP 계층에서 통째로 이어요"),
            (laptop, "출장·재택 한 명", "서 이사 노트북", "SSL/TLS VPN", GREEN, "필요한 앱 몇 개", "앱별로 좁게 열어요"),
            (laptop, "외주 작업자", "그룹웨어 웹 한 곳, 2주만", "SSL/TLS VPN 웹 포털", GREEN, "웹 한 곳만", "클라이언트 설치가 거의 없어요")]
    body = ["".join(box(40, y, 880, H, LINE, PANEL, 10, sw=1) for y in ys)]
    for i, (ic, who, sub, how, c, scope, ssub) in enumerate(data):
        y = ys[i]
        icon = f'<g transform="translate(100,{y + 46}) scale(0.75)">{house(0, 0)}</g>' if ic is house else laptop(100, y + 46)
        row = (icon + text(170, y + 40, who, 20, TXT, 700, "start") + text(170, y + 68, sub, 16, MUTED, None, "start")
               + pill(530, y + 45, how, c, 18, True, tw(how, 18) + 36) + text(700, y + 40, scope, 20, TXT, 700, "start")
               + text(700, y + 68, ssub, 16, MUTED, None, "start"))
        body += [a.vis(row, i + 1, 4), mark(40, y, 880, H, i + 1)] if i < 3 else []
    body.append(a.vis(pill(480, 450, "연결 대상과 환경을 보고 골라요", BLUE, 18, True), 4, 4))
    caps = ["지사끼리 망 전체를 이을 때는 IPsec이에요", "출장·재택은 필요한 앱만 SSL/TLS VPN으로 붙어요", "웹 한 곳만 열어 줄 때는 웹 포털이 가벼워요", "정답은 없고 연결 대상과 환경을 보고 골라요"]
    return frame(a, "누구에게 어떤 VPN을 쓸까", "대상에 따라 나눠 쓰는 구성이 흔해요", caps, "".join(body))


ITEMS = [
    ("u14-l03-p1-check-order", "터널이 안 뜰 때 확인 순서", "터널이 안 서면 IKE 협상(UDP 500), NAT 통과(NAT-T, UDP 4500), 협상 내용, 상대 확인 순서로 앞에서부터 확인하고, 공유기가 있으면 2번이 3·4번보다 먼저 막힌다는 점검 순서입니다.", "터널이 안 서면 IKE, NAT-T, 협상 내용, 상대 확인 순으로 확인합니다.", 3, p1),
    ("u14-l03-p2-ike-sa-memo", "IKE 협상과 SA", "도쿄 SG와 서울 SG가 UDP 500으로 암호 방식·키·수명을 제안해 합의하고, 결과를 방향마다 따로 SA 메모로 기억하는 모습입니다.", "IKE는 공통 조건을 협상해 SA로 남기며 SA는 방향마다 따로 생깁니다.", 2, p2),
    ("u14-l03-p2b-ike-fail", "공통 조건이 없으면 협상 실패", "새 도쿄 SG는 구형 암호 방식만, 본사 SG는 강한 암호 방식만 허용해 공통 조건이 없으므로 SA가 생기지 않고 협상이 실패하는 모습입니다.", "공통 조건이 없으면 IKE 협상이 실패하니 양쪽 제안부터 대조합니다.", 4, p2b),
    ("u14-l03-p3-auth-who", "상대가 진짜 본사 SG일까", "본사 SG인 척하는 장비를 막기 위해, 왼쪽은 양쪽이 같은 비밀값을 아는지로 믿는 사전 공유 키, 오른쪽은 인증 기관이 보증한 인증서를 서로 보여 주는 방식입니다.", "상대 확인은 사전 공유 키나 인증서로 하며, 암호화와는 다른 일입니다.", 1, p3),
    ("u14-l03-p4-esp-ah-envelope", "ESP와 AH는 뭘 지켜 줄까", "기밀성, 무결성, 인증 세 가지 중 불투명 봉투 같은 ESP는 모두, 투명 봉투에 밀봉만 한 AH는 기밀성을 뺀 둘만 지켜 준다는 비교입니다.", "내용이 비밀인 자료는 기밀성이 있는 ESP로 맞춥니다.", 2, p4),
    ("u14-l03-p5-ah-nat", "AH는 NAT를 못 지나가요", "박 팀장 노트북의 AH 패킷이 집 공유기(NAT)를 지나며 출발 주소가 바뀌면, 서울 SG가 변조로 보고 버려서 NAT 뒤에서는 ESP를 써야 하는 모습입니다.", "AH는 NAT가 주소를 바꾸면 변조로 보고 버립니다.", 1, p5),
    ("u14-l03-p5b-nat-t", "집 공유기를 만나도 지나갈까", "ESP에는 포트 번호가 없어 NAT가 구분하지 못하지만, NAT-T가 ESP를 UDP 4500으로 한 번 더 감싸 서울 SG까지 지나가는 모습이며 AH는 구제하지 못합니다.", "NAT가 있으면 ESP를 UDP 4500으로 감싸는 NAT-T를 씁니다.", 2, p5b),
    ("u14-l03-p6-ssl-tls-vpn", "브라우저로 붙는 SSL/TLS VPN", "호텔 와이파이에서 IPsec의 UDP 500·4500은 막히고 TLS 기반 SSL/TLS VPN은 TCP 443으로 본사 SG까지 지나가는 모습입니다.", "웹만 열린 환경에서는 TCP 443을 쓰는 SSL/TLS VPN이 대개 통과합니다.", 1, p6),
    ("u14-l03-p6b-which-vpn", "누구에게 어떤 VPN을 쓸까", "지사끼리 망 전체를 이을 때는 IPsec, 출장·재택 한 명은 필요한 앱만 SSL/TLS VPN, 외주 작업자에게는 웹 한 곳만 웹 포털로 열어 주는 선택입니다.", "대상과 환경을 보고 IPsec과 SSL/TLS VPN을 나눠 씁니다.", 3, p6b),
]
LESSON = next((ROOT / "units").glob(f"{UNIT}/03-*"))

# Page마다 그림 묶음(표시 순서). 두 그림이면 after_paragraph는 오름차순.
PAGES = [["u14-l03-p1-check-order"], ["u14-l03-p2-ike-sa-memo", "u14-l03-p2b-ike-fail"], ["u14-l03-p3-auth-who"],
         ["u14-l03-p4-esp-ah-envelope"], ["u14-l03-p5-ah-nat", "u14-l03-p5b-nat-t"], ["u14-l03-p6-ssl-tls-vpn", "u14-l03-p6b-which-vpn"]]

if __name__ == "__main__":
    from kit import write, wire_items
    out = LESSON / "assets" / "animations"
    by = {f: (t, al, c, ap, fn) for f, t, al, c, ap, fn in ITEMS}
    for f, (_t, _al, _c, _ap, fn) in by.items():
        write(out, f, fn())
    if "--svg-only" not in sys.argv:
        wire_items(LESSON / "lesson.md", [[(f, by[f][0], by[f][1], by[f][2], by[f][3]) for f in page] for page in PAGES])
    print("ok", len(by), "svgs")
