#!/usr/bin/env python3
"""Unit 14 Lesson 1 revision (Pages 1-6; Page 7 kept). Run from repo root: python3 scripts/svg_pairs/u14_l01_rev.py
Fixes: 16px+ labels, no packet over icons, non-empty step 1, no 'SG' before Page 6 explains it."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import u14_l01_vpn as C
from u14_l01_vpn import *  # noqa: F401,F403
from u14_l01_vpn import new, mark, tube, ip, server


def site2(x, y, w, h, label, c, sub=None):
    s = box(x, y, w, h, c, PANEL, 16, dash=True, sw=3) + text(x + w / 2, y + 28, label, 18, c, 700)
    return s + (text(x + w / 2, y + 52, sub, 16, MUTED) if sub else "")


def p1():
    a = new()
    body = [site2(30, 150, 270, 260, "박 팀장 집", MUTED), laptop(110, Y, "노트북"), ip(110, 372, "192.168.0.20", fs=16),
            site2(600, 150, 330, 260, "서울 본사", GREEN, "사설망 192.168.10.0/24"), booth(650, Y, "본사 경계"),
            server(850, Y), line(150, Y, 380, Y, LINE, 4, "8 6"), line(520, Y, 610, Y, LINE, 4, "8 6"), line(690, Y, 816, Y, LINE, 4),
            a.vis(pill(160, 230, "AI 주소 열기", BLUE, 16, True, 150), 1, 2), mark(80, 212, 160, 36, 1),
            mv(a, packet(0, 0, ORANGE), [(190, Y), (565, Y)], 2, 2, 3, 0.1, 0.9), cloud(450, Y),
            a.vis(cross(650, 232), 3, 4), a.vis(pill(770, 232, "방화벽이 막아요", RED, 16, False, 160), 3, 4), mark(625, 207, 50, 50, 3),
            mark(596, 146, 338, 268, 4),
            a.vis(pill(480, 447, "사설망 = 우리가 통제하는 범위, 문제는 그 경계예요", GREEN, 18, True), 4, 4)]
    caps = ["집 노트북으로 사내 AI 주소를 열어 봐요", "요청이 인터넷을 지나 본사 경계에 닿아요", "사설 주소라서 경계에서 막혀 응답이 없어요", "서버가 아니라 사설망의 경계가 문제예요"]
    return frame(a, "사설망의 경계", "집 노트북이 사내 AI에 닿지 못해요", caps, "".join(body))


def p2():
    a = new()
    xs = (60, 350, 640)
    chips = [("닿을 것", BLUE), ("노출 금지", VIOLET), ("내용 보호", GREEN)]
    bad = ["지사 업무가 멈춰요", "누구나 두드릴 수 있어요", "도면·개인정보가 새요"]
    body = [pc(110, 175, "쇼룸 직원") + laptop(850, 175, "박 팀장") + line(150, 175, 285, 175, LINE, 3) + line(675, 175, 800, 175, LINE, 3),
            pill(480, 175, "쇼룸도 박 팀장도 사내 AI 쓰게 해 주세요", BLUE, 18, True), mark(250, 150, 460, 50, 1),
            a.vis("".join(line(480, 200, x + 130, 250, LINE, 3) for x in xs) + "".join(cell(x, 250, 260, 56, t, c, 20) for x, (t, c) in zip(xs, chips)), 2, 4),
            mark(50, 240, 870, 76, 2),
            a.vis("".join(cell(x, 340, 260, 56, t, RED, 17) for x, t in zip(xs, bad)), 3, 4), mark(50, 330, 870, 76, 3),
            a.vis(pill(480, 447, "이 셋을 모두 채울 방법: 전용 회선 또는 VPN", GREEN, 18, True), 4, 4)]
    caps = ["월요일에 한 덩어리 요청이 들어왔어요", "요청을 세 가지 요구로 쪼개요", "하나라도 못 지키면 이런 문제가 생겨요", "세 요구를 모두 채우는 방법을 찾아요"]
    return frame(a, "요구를 세 가지로 쪼개기", "한 덩어리 요청을 따로 따져 봐요", caps, "".join(body))


def p3():
    a = new()
    body = [warehouse(110, 260, "서울 본사"), warehouse(850, 260, "도쿄 쇼룸"), line(150, 260, 810, 260, GREEN, 10),
            a.vis(pill(480, 175, "통신 사업자에게 빌린 전용 회선", BLUE, 18, False), 1, 3), mark(250, 150, 460, 50, 1),
            a.vis(check(322, 315) + pill(480, 315, "남과 섞이지 않아요", GREEN, 18, False, 260), 2, 2), mark(345, 295, 270, 40, 2),
            a.vis(line(152, 272, 445, 385, ORANGE, 6) + warehouse(480, 400, "현장 사무소")
                  + pill(760, 400, "지점마다 회선·요금 추가", RED, 17, False, 300), 3, 4), mark(425, 362, 110, 100, 3),
            a.vis(pill(480, 175, "안전하지만 비싸고 늘리기 어려워요", GREEN, 18, True), 4, 4)]
    caps = ["서울과 도쿄를 전용 회선으로 이어요", "길이 우리 몫이라 남과 섞이지 않아요", "현장 사무소가 늘면 회선도 하나 더 필요해요", "안전한 대신 비용과 확장이 부담이에요"]
    return frame(a, "전용 회선", "우리 몫의 길을 빌리는 방법이에요", caps, "".join(body))


def p4():
    a = new()
    xs = (60, 350, 640)
    bad = ["엿보기", "바꿔치기", "남인 척하기"]
    good = ["기밀성 · 암호화", "무결성", "인증"]
    body = [pc(110, 200, "서울 본사"), pc(850, 200, "도쿄 쇼룸"), line(160, 200, 410, 200, LINE, 4, "8 6"), line(550, 200, 800, 200, LINE, 4, "8 6"),
            mv(a, packet(0, 0, ORANGE), [(190, 200), (770, 200)], 1, 1, 1, 0.1, 0.9), cloud(480, 200),
            a.vis(pill(480, 135, "견적서가 그대로 흘러요", BLUE, 16, False), 1, 1),
            a.vis("".join(cell(x, 300, 260, 52, t, RED, 19) for x, t in zip(xs, bad)), 2, 4), mark(50, 290, 870, 72, 2),
            a.vis("".join(cell(x, 372, 260, 52, t, GREEN, 18) for x, t in zip(xs, good)), 3, 4), mark(50, 362, 870, 72, 3),
            a.vis(pill(480, 457, "세 걱정은 서로 달라서 따로 점검해요", GREEN, 18, True), 4, 4)]
    caps = ["견적서가 공용 인터넷 길을 지나가요", "중간에서 걱정할 일이 세 가지 있어요", "걱정마다 지키는 성질이 따로 있어요", "하나가 해결돼도 나머지는 남아요"]
    return frame(a, "인터넷을 그냥 쓰면", "공용망에서 걱정할 세 가지예요", caps, "".join(body))


def p5():
    a = new()
    body = [pc(90, Y, "서울 본사"), pc(870, Y, "도쿄 쇼룸"), line(124, Y, 170, Y, LINE, 4), line(790, Y, 836, Y, LINE, 4),
            box(170, 268, 620, 64, BLUE, PANEL, 32, sw=3), line(200, Y, 760, Y, LINE, 4, "8 6"), text(480, 374, "공용 인터넷 길", 18, BLUE, 700),
            a.vis(eye(480, 215), 1, 1), mv(a, packet(0, 0, ORANGE), [(220, Y), (740, Y)], 1, 1, 1, 0.1, 0.9),
            a.vis(tube(200, 760, Y), 2, 4), mark(190, 262, 580, 76, 2),
            a.vis(lock(480, 205, GREEN) + check(540, 225), 3, 4), mv(a, packet(0, 0, VIOLET), [(220, Y), (740, Y)], 3, 3, 3, 0.1, 0.9),
            a.vis(pill(480, 415, "VPN = 새 선이 아니라 인터넷 위의 통로", VIOLET, 18, True), 4, 4)]
    caps = ["열린 인터넷 길에서는 안이 훤히 보여요", "같은 길 위에 터널을 하나 더 만들어요", "터널 안에서는 내용이 가려져요", "새 선이 아니라 논리적인 통로예요"]
    return frame(a, "VPN은 인터넷 위의 터널", "같은 길인데 터널 안은 가려져요", caps, "".join(body))


def p6():
    a = new()
    base = (box(40, 130, 420, 290, GREEN, PANEL, 16, dash=True, sw=3) + text(250, 162, "G-to-G · 사이트 간", 19, GREEN, 700) + text(250, 188, "쇼룸의 PC 여러 대", 16, MUTED)
            + box(500, 130, 420, 290, BLUE, PANEL, 16, dash=True, sw=3) + text(710, 162, "G-to-E · 원격 접속", 19, BLUE, 700) + text(710, 188, "노트북 한 대", 16, MUTED)
            + pc(95, 290, "쇼룸 PC") + booth(195, 290, "도쿄 SG") + booth(390, 290, "본사 SG") + line(130, 290, 155, 290, LINE, 4) + line(235, 290, 350, 290, LINE, 4, "8 6")
            + laptop(580, 290, "박 팀장 노트북") + pill(605, 225, "VPN 클라이언트", BLUE, 16, False, 170) + booth(860, 290, "본사 SG") + line(640, 290, 820, 290, LINE, 4, "8 6"))
    body = [base,
            a.vis(tube(240, 350, 290) + pill(250, 385, "망 ↔ 망", GREEN, 17, True, 130), 2, 4), mark(46, 236, 405, 160, 2),
            a.vis(tube(660, 820, 290, BLUE) + pill(740, 385, "기기 ↔ 망", BLUE, 17, True, 130), 3, 4), mark(506, 206, 408, 190, 3),
            a.vis(pill(480, 457, "지사는 G-to-G, 재택은 G-to-E예요", GREEN, 18, True), 4, 4)]
    caps = ["연결할 대상의 규모가 달라요", "지사는 두 SG가 망과 망을 한 번에 이어요", "재택은 노트북 하나를 본사 SG에 붙여요", "둘 다 VPN이지만 잇는 방식이 달라요"]
    return frame(a, "지사용과 재택용 VPN", "게이트웨이(G)와 단말(E)의 조합이에요", caps, "".join(body))


ITEMS = [  # (file, title, alt, caption, after_paragraph, fn) ; Page 7 kept as is
    ("u14-l01-p1-private-boundary-scope", "사설망의 경계", "집 노트북이 사내 AI 192.168.10.50:8080 으로 보낸 요청이 본사 경계에서 방화벽에 막히고, 사설망은 우리가 통제하는 범위임을 짚습니다.", "사내 AI에 닿지 못하는 이유는 서버가 아니라 사설망의 경계입니다.", 3, p1),
    ("u14-l01-p2-three-needs-actors", "요구를 세 가지로 쪼개기", "쇼룸 직원과 박 팀장의 요청을 닿을 것, 노출 금지, 내용 보호로 쪼개고 각각 지키지 못하면 생기는 문제를 보여 줍니다.", "한 덩어리 요청은 닿을 것, 노출 금지, 내용 보호로 나눠 따집니다.", 2, p2),
    ("u14-l01-p3-leased-line-cost", "전용 회선", "서울 본사와 도쿄 쇼룸을 전용 회선으로 잇고, 현장 사무소가 늘면 회선과 요금이 함께 늘어나는 모습입니다.", "전용 회선은 안전하지만 비싸고 늘리기 어렵습니다.", 2, p3),
    ("u14-l01-p4-open-internet-flow", "인터넷을 그냥 쓰면", "공용 인터넷을 지나는 견적서에 엿보기, 바꿔치기, 남인 척하기 세 걱정이 있고 각각 기밀성, 무결성, 인증으로 지킨다는 그림입니다.", "공용망의 세 걱정은 기밀성, 무결성, 인증으로 따로 점검합니다.", 1, p4),
    ("u14-l01-p5-vpn-tunnel-road", "VPN은 인터넷 위의 터널", "서울 본사와 도쿄 쇼룸 사이의 같은 인터넷 길 위에 터널을 만들면 안의 내용이 가려지는 모습입니다.", "VPN은 새 선이 아니라 기존 인터넷 위의 논리적 통로입니다.", 1, p5),
    ("u14-l01-p6-gg-ge-setup", "지사용과 재택용 VPN", "왼쪽은 도쿄 SG와 본사 SG가 망과 망을 잇는 G-to-G, 오른쪽은 박 팀장 노트북이 본사 SG에 붙는 G-to-E입니다.", "지사는 G-to-G, 재택은 G-to-E로 잇습니다.", 3, p6),
]
P7 = ("u14-l01-p7-vpn-vs-leased", "VPN은 전용 회선만큼 안전할까", "전용 회선은 독립된 방의 금고처럼 길이 분리되고, VPN은 로비의 금고처럼 키와 계정 관리에 보호가 달려 있음을 비교합니다.", "VPN은 키와 계정 관리가 무너지면 보호도 무너집니다.", 1)

if __name__ == "__main__":
    out = C.LESSON / "assets" / "animations"
    for f, *_r, fn in ITEMS:
        write(out, f, fn())
    if "--svg-only" not in sys.argv:
        wire_items(C.LESSON / "lesson.md", [[(f, t, al, c, ap)] for f, t, al, c, ap, _ in ITEMS] + [[P7]])
    print("ok")
