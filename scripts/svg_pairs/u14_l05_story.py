#!/usr/bin/env python3
"""Unit 14 Lesson 5 situation SVGs (4 steps each, one per Page, 8 Pages): 신입 네트워크 관리자 지우 + 티켓.
Run from the repo root: python3 scripts/svg_pairs/u14_l05_story.py"""
from pathlib import Path

from hangyeol_cast import *  # noqa: F401,F403
from u11_l01_story import ppl, mk_bubble  # reuse the reference helpers (also applies the admin ROLES override)
from u11_new_common import server

ROOT = Path(__file__).resolve().parents[2]
OUT = next((ROOT / "units").glob("10-*/lessons/restructured/05-*")) / "assets" / "animations"
HY = 225


def mk_thought(a, x, y, s, t):
    lines = wrap(s)
    w = max(tw(ln, 18) for ln in lines) + 40
    h = 26 * len(lines) + 26
    return mark(a, x - w / 2 - 1, y - h / 2 - 1, w + 2, h + 2, t)


def p1():
    a = new()
    s = "화면 언어와 안내 문구가\n현지 기준으로 바뀌었어요"
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 560, "지우", [("normal", 1, 4)], role_step1=True),
         ppl(a, 880, "서 이사", [("normal", 1, 4)], facing="left", role_step1=True),
         a.vis(pill(150, 360, "해외 박람회", MUTED, 17), 1, 4),
         a.vis(monitor(330, 285, "ok", "현지 기준 화면"), 2, 4), mark(a, 230, 229, 200, 112, 2),
         a.vis(bubble(300, 160, s, tail_to=(165, 203), color=TERRACOTTA), 3, 3), mk_bubble(a, 300, 160, s, 3),
         question(a, "서비스는 내가 어디 있다고 볼까?")]
    caps = ["해외 박람회에 간 박 팀장이 지우에게 티켓을 보냈어요", "외부 클라우드 저장소 화면이 현지 기준으로 바뀌었어요",
            "박 팀장이 이유를 궁금해해요", "이 Page에서 서비스가 보는 위치를 알아봐요"]
    return scene(a, "내 화면이 왜 현지 기준일까", "해외 박람회에서 온 박 팀장의 티켓이에요", caps, "".join(b), bg="office")


def p2():
    a = new()
    t = "같은 사람, 같은 노트북인데\n위치가 달라지네"
    b = [ppl(a, 160, "박 팀장", [("normal", 1, 4)], role_step1=True),
         ppl(a, 820, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(pill(160, 360, "출장지", MUTED, 17), 1, 4),
         a.vis(laptop(330, 290, "박 팀장 노트북"), 1, 4),
         a.vis(pill(540, 250, "VPN 켬", BLUE, 18), 2, 4) + a.vis(pill(540, 310, "한국 접속", GREEN, 18), 2, 4), mark(a, 450, 220, 180, 120, 2),
         a.vis(thought(560, 158, t, tail_to=(805, 205), color=BLUE), 3, 3), mk_thought(a, 560, 158, t, 3),
         question(a, "VPN을 켜면 출구가 왜 바뀔까?")]
    caps = ["출장지의 박 팀장이 노트북을 열었어요", "회사 VPN을 켜자 서비스가 한국 접속으로 봐요",
            "VPN을 끄면 현지 접속이라 지우는 이상해요", "이 Page에서 출구가 바뀌는 까닭을 알아봐요"]
    return scene(a, "같은 노트북인데 위치가 달라요", "출장지에서 VPN을 켜고 끄는 박 팀장이에요", caps, "".join(b), bg="office")


def p3():
    a = new()
    q = "직원이 개인 VPN으로\n제한 서비스를 쓰면요?"
    t = "되는지가 아니라\n회사의 위험으로 답하자"
    b = [ppl(a, 150, "서 이사", [("normal", 1, 4)], role_step1=True),
         ppl(a, 820, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(laptop(480, 300, "직원 개인 VPN"), 2, 4), mark(a, 400, 260, 160, 112, 2),
         a.vis(bubble(300, 160, q, tail_to=(160, 203), color=VIOLET), 2, 2), mk_bubble(a, 300, 160, q, 2),
         a.vis(thought(710, 158, t, tail_to=(805, 205), color=BLUE), 3, 3), mk_thought(a, 710, 158, t, 3),
         question(a, "지역 제한을 VPN으로 넘으면 뭐가 문제일까?")]
    caps = ["서 이사가 지우에게 직원들의 VPN 이야기를 물어요", "개인 VPN으로 제한 서비스를 쓰면 어떻게 되는지 물어요",
            "지우는 되는지 안 되는지로 답하지 않기로 해요", "이 Page에서 그 일의 위험을 알아봐요"]
    return scene(a, "개인 VPN으로 제한 서비스를?", "서 이사가 묻고 지우가 답을 고민해요", caps, "".join(b), bg="office")


def p4():
    a = new()
    t = "우리는 잘못한 적 없는데\n왜 이런 일이 생길까?"
    b = [ppl(a, 190, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(pill(190, 360, "본사 공인 주소 198.51.100.25", MUTED, 17), 1, 4),
         a.vis(alert_card(700, 215, "정상 메일이 스팸함으로"), 2, 4) + a.vis(alert_card(700, 290, "캡차·일시 차단이 잦아짐"), 2, 4),
         mark(a, 530, 175, 340, 150, 2),
         a.vis(thought(340, 158, t, tail_to=(210, 205), color=BLUE), 3, 3), mk_thought(a, 340, 158, t, 3),
         question(a, "IP 주소에도 평판이 있다?")]
    caps = ["지우가 본사 공인 주소의 문제를 살펴봐요", "정상 메일이 스팸함으로 가고 일시 차단도 잦아져요",
            "회사는 아무 잘못도 하지 않았어요", "이 Page에서 주소의 평판을 알아봐요"]
    return scene(a, "정상 메일이 스팸함으로 가요", "본사 출구 주소에 무슨 일이 생겼어요", caps, "".join(b), bg="office")


def p5():
    a = new()
    t = "VPN 서버를 켠\n기억이 없는데"
    b = [ppl(a, 200, "박 팀장", [("normal", 1, 2), ("worried", 3, 4)], role_step1=True),
         ppl(a, 800, "지우", [("normal", 1, 4)], facing="left", role_step1=True),
         a.vis(pill(200, 360, "박 팀장 집", MUTED, 17), 1, 4),
         a.vis(monitor(500, 285, "error", "VPN 서버 켜짐"), 2, 4), mark(a, 395, 225, 210, 112, 2),
         a.vis(thought(340, 158, t, tail_to=(215, 205), color=TERRACOTTA), 3, 3), mk_thought(a, 340, 158, t, 3),
         question(a, "공유기 VPN 기능은 왜 위험해질까?")]
    caps = ["박 팀장 집에서 지우가 공유기 설정 화면을 같이 봐요", "설정 화면에 VPN 서버 메뉴가 켜져 있어요",
            "박 팀장은 켠 기억이 없어요", "이 Page에서 공유기 VPN의 위험을 알아봐요"]
    return scene(a, "켠 적 없는 공유기 VPN", "박 팀장 집 공유기 설정 화면이에요", caps, "".join(b), bg="home")


def p6():
    a = new()
    t = "우리는 한 적 없는데\n기록엔 우리 주소가 있네"
    b = [ppl(a, 200, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(server(800, 280), 1, 4),
         a.vis(alert_card(560, 200, "비정상적으로 많은 요청"), 2, 4) + a.vis(pill(560, 260, "198.51.100.25", MUTED, 18), 2, 4),
         mark(a, 380, 160, 360, 130, 2),
         a.vis(thought(340, 158, t, tail_to=(210, 205), color=BLUE), 3, 3), mk_thought(a, 340, 158, t, 3),
         question(a, "누가 한 일일까?")]
    caps = ["외부 클라우드 저장소 업체가 지우에게 연락해요", "귀하의 주소에서 비정상적으로 많은 요청이 왔대요",
            "회사는 그런 일을 한 적이 없어요", "이 Page에서 주소와 사람이 다름을 알아봐요"]
    return scene(a, "우리 주소에서 온 이상한 요청", "클라우드 업체의 연락을 받은 지우예요", caps, "".join(b), bg="office")


def p7():
    a = new()
    t = "필터가 막아 둔 사이트인데\n왜 못 막았지?"
    b = [ppl(a, 190, "지우", [("normal", 1, 2), ("thinking", 3, 4)], role_step1=True),
         a.vis(pc(700, 285, "직원 PC"), 1, 4),
         a.vis(pill(520, 250, "개인 VPN", BLUE, 18), 2, 4) + a.vis(alert_card(700, 200, "악성 코드가 들어옴"), 2, 4),
         mark(a, 460, 165, 320, 130, 2),
         a.vis(thought(340, 158, t, tail_to=(210, 205), color=BLUE), 3, 3), mk_thought(a, 340, 158, t, 3),
         question(a, "왜 필터가 못 막았을까?")]
    caps = ["지우가 사고 조사를 시작해요", "직원이 개인 VPN으로 막힌 사이트를 열고 악성 코드가 들어왔어요",
            "지우는 왜 필터가 못 막았는지 궁금해요", "이 Page에서 필터가 놓친 까닭을 알아봐요"]
    return scene(a, "막아 둔 사이트가 열렸어요", "필터를 지나친 파일이 사내 PC에 들어왔어요", caps, "".join(b), bg="office")


def p8():
    a = new()
    t = "주소만 보는 규칙은\n이 사람을 알아보지 못해"
    b = [ppl(a, 150, "박 팀장", [("normal", 1, 1), ("worried", 2, 4)], role_step1=True),
         ppl(a, 820, "지우", [("normal", 1, 2), ("thinking", 3, 4)], facing="left", role_step1=True),
         a.vis(doc(420, 300, "10.10.99.0/24 허용"), 1, 4),
         a.vis(alert_card(420, 225, "박 팀장 VPN 비밀번호 유출"), 2, 4), mark(a, 230, 195, 380, 60, 2),
         a.vis(thought(710, 158, t, tail_to=(805, 205), color=BLUE), 3, 3), mk_thought(a, 710, 158, t, 3),
         question(a, "IP만 보고 믿어도 될까?")]
    caps = ["사내 그룹웨어에 10.10.99.0/24 허용 규칙이 있어요", "박 팀장의 VPN 계정 비밀번호가 유출됐어요",
            "공격자도 10.10.99.x 주소를 받으면 통과해요", "이 Page에서 IP만 믿는 한계를 알아봐요"]
    return scene(a, "주소만 보는 허용 규칙", "박 팀장의 비밀번호가 유출된 뒤예요", caps, "".join(b), bg="office")


NAMES = ["service-view", "exit-changes", "region-risk", "ip-reputation", "router-vpn", "relay", "filter-blind", "ip-only"]

if __name__ == "__main__":
    for i, (fn, n) in enumerate(zip((p1, p2, p3, p4, p5, p6, p7, p8), NAMES), 1):
        write(OUT, f"u14-l05-p{i}-story-{n}", fn())
        print(f"u14-l05-p{i}-story-{n}.svg")
