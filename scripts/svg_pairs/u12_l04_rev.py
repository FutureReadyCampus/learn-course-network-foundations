#!/usr/bin/env python3
"""Unit 12 Lesson 4 (UPnP) SVG review: revised Pages 1,3,4(+4b),5,6. Page 2 kept as is.
Run from repo root: python3 scripts/svg_pairs/u12_l04_rev.py  (--svg-only skips the lesson.md edit)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from u12_new_common import *  # noqa: F401,F403

LESSON = lesson_dir(4)
OUT = LESSON / "assets" / "animations"
PC37, PC38 = "192.168.10.37", "192.168.10.38"
dim = lambda s: f'<g opacity="0.35">{s}</g>'


def p1():
    p = Pg("내가 연 적 없는 포트가 열려 있다?", "수동 포워딩 목록이 비어도 UPnP 목록은 따로 있어요",
           ["시연용 8080 규칙을 지워 수동 목록은 비었어요", "UPnP 목록에는 모르는 줄이 세 개 있어요",
            "지우의 기억에는 만든 적 없는 줄이에요", "수동 목록과 UPnP 목록을 따로 점검해요"])
    rows = [["TCP 6881", PC37 + ":6881"], ["UDP 27015", "192.168.10.44:27015"], ["UDP 50001", PC38 + ":50001"]]
    X, W = [345, 505, 755], [154, 244, 150]
    p.base(box(40, 125, 270, 300, MUTED, PANEL, 14, sw=2) + lbl(175, 158, "수동 포워딩 목록", MUTED, 18),
           box(330, 125, 590, 300, BLUE, PANEL, 14, sw=2) + lbl(625, 158, "공유기 UPnP 목록", BLUE, 18))
    p.at(cell(70, 240, 210, 54, "비어 있음", MUTED, 20), 1, mark=(70, 240, 210, 54))
    p.at(text(625, 290, "아직 열어 보지 않은 목록", 17, MUTED, 700), 1, 1)
    two = "".join(cell(X[i], 180, W[i], 36, h, MUTED, 16, BG) for i, h in enumerate(["외부 포트", "안쪽 대상"]))
    two += "".join(cell(X[i], 224 + r * 50, W[i], 42, v, GREEN, 17) for r, row in enumerate(rows) for i, v in enumerate(row))
    p.at(two, 2, mark=(345, 224, 404, 142))
    mem = cell(X[2], 180, W[2], 36, "지우의 기억", MUTED, 16, BG) + "".join(cell(X[2], 224 + r * 50, W[2], 42, "없음", RED, 17) for r in range(3))
    p.at(mem, 3, mark=(X[2], 224, W[2], 142))
    p.at(pill(480, 456, "수동 목록과 UPnP 목록을 따로 봐요", ORANGE, 17, True, 380), 4, 4)
    return p.render()


def p3():
    p = Pg("꽂기만 하면 되는 편리함, 네트워크로", "PnP의 발상을 공유기까지 넓힌 것이 UPnP예요",
           ["PnP는 장치를 꽂으면 알아서 준비해 줘요", "USB를 꽂으면 설정 없이 바로 써요",
            "UPnP는 프로그램이 공유기에 줄을 만들어요", "편해진 만큼 설정이 눈에서 멀어져요"])
    L, R = 50, 510
    p.base(box(L, 125, 400, 290, MUTED, PANEL, 16, sw=2) + lbl(L + 200, 158, "PnP", MUTED, 19) + pc(L + 290, 250, "PC"),
           box(R, 125, 400, 290, GREEN, PANEL, 16, sw=2) + lbl(R + 200, 158, "UPnP", GREEN, 19) + pc(R + 90, 250, PC37) + rt(R + 310, 250))
    p.at(usb(L + 100, 250), 1, 1)
    p.fly(usb(0, 0), [(L + 100, 250), (L + 215, 250)], 2, 0.1, 0.8)
    p.at(usb(L + 215, 250) + pill(L + 200, 355, "설정 없이 바로 사용", GREEN, 17, True, 230), 3, 4)
    p.at(pill(L + 200, 355, "설정 없이 바로 사용", GREEN, 17, True, 230), 2, 2, mark=(L + 85, 335, 230, 40))
    p.fly(packet(0, 0, ORANGE), [(R + 150, 250), (R + 232, 250)], 3, 0.1, 0.8)
    p.at(cell(R + 20, 335, 360, 44, f"6881 → {PC37}:6881", ORANGE, 17), 3, 4, mark=(R + 20, 335, 360, 44))
    p.at(pill(480, 456, "편해진 만큼 설정이 눈에서 멀어져요", ORANGE, 17, True, 380), 4, 4)
    return p.render()


def p4a():
    p = Pg("프로그램은 공유기에 어떻게 부탁할까?", "발견 → 요청 → 결과, 세 걸음이에요",
           ["① 발견: 설정을 받아 줄 장치를 찾아요", "② 요청: 6881번을 열어 달라고 부탁해요",
            "③ 결과: 공유기 변환표에 줄이 생겨요", "사람이 입력하지 않아도 줄이 생겨요"])
    p.base(pc(300, 285, PC37), rt(670, 285), line(360, 285, 640, 285, LINE, 4, "8 6"),
           lbl(670, 142, "공유기 변환표", MUTED, 16), box(500, 152, 340, 44, MUTED, PANEL, 6, dash=True, sw=2))
    p.fly(packet(0, 0, BLUE), [(380, 285), (590, 285)], 1, 0.05, 0.45)
    p.fly(packet(0, 0, GREEN), [(590, 285), (380, 285)], 1, 0.5, 0.95)
    p.at(pill(480, 225, "① 설정 받아 줄 장치 있나요?", BLUE, 16, True, 270), 1, 1, mark=(345, 205, 270, 40))
    p.fly(packet(0, 0, ORANGE), [(380, 285), (590, 285)], 2, 0.1, 0.9)
    p.at(pill(480, 225, "② 6881번 열어 주세요", ORANGE, 16, True, 270), 2, 2, mark=(345, 205, 270, 40))
    p.at(cell(500, 152, 340, 44, f"TCP 6881 → {PC37}:6881", GREEN, 16), 3, 4, mark=(500, 152, 340, 44))
    p.at(pill(480, 440, "사람이 입력하지 않아도 줄이 생겨요", ORANGE, 17, True, 380), 4, 4)
    return p.render()


def p4b():
    p = Pg("요청이 성공해도 닿는다는 보장은 없다", "줄이 생긴 것과 길이 열린 것은 별개예요",
           ["공유기에 줄이 생겨 요청은 성공했어요", "협력사 PC가 6881번으로 연결을 보내요",
            "통신사 NAT·방화벽·프로그램 중 한 곳이 막을 수 있어요", "요청 성공과 길이 열린 것은 별개예요"])
    p.base(pc(110, 270, PC37), rt(480, 270), laptop(850, 270, "협력사 PC"),
           line(170, 270, 450, 270, LINE, 4, "8 6"), line(510, 270, 800, 270, LINE, 4, "8 6"))
    p.at(cell(310, 140, 340, 44, f"TCP 6881 → {PC37}:6881", GREEN, 16) + pill(480, 212, "요청 성공", GREEN, 16, True, 130), 1, 4,
         mark=(310, 140, 340, 44))
    p.fly(packet(0, 0, RED), [(800, 270), (560, 270)], 2, 0.1, 0.9)
    p.at(cross(650, 270), 3, 4)
    p.at(pill(135, 395, "프로그램이 기다리지 않음", RED, 16, False, 240) + pill(480, 395, "방화벽이 막음", RED, 16, False, 160)
         + pill(760, 395, "통신사 NAT가 한 겹 더", RED, 16, False, 230), 3, 3, mark=(8, 372, 884, 46))
    p.at(pill(480, 456, "요청 성공과 길이 열린 것은 별개예요", ORANGE, 17, True, 380), 4, 4)
    return p.render()


def p5():
    p = Pg("비밀번호도 없이 포트를 열어 준다고?", "같은 LAN 안이면 믿어 버리는 방식이에요",
           ["지우가 UPnP 줄을 만든 관리자 로그인을 찾아봐요", "감염된 PC가 UPnP로 포트를 열어 달라고 해요",
            "공유기가 확인 없이 줄을 만들어요", "신분을 묻지 않고, 닿는 환경이면 노출돼요"])
    p.base(net(40, 125, 300, 300, "사무실 LAN", GREEN), laptop(190, 250, PC38, RED), rt(480, 255), person(850, 215, "공격자"),
           line(340, 252, 450, 254, LINE, 4, "8 6"), line(510, 255, 800, 235, LINE, 4, "8 6"))
    p.at(cell(365, 150, 250, 44, "관리자 로그인 기록: 없음", MUTED, 16), 1, 4, mark=(365, 150, 250, 44))
    p.fly(packet(0, 0, RED), [(250, 250), (410, 254)], 2, 0.1, 0.9)
    p.at(pill(190, 345, "UPnP 요청: 50001 열어 줘", RED, 16, False, 250), 2, 2, mark=(65, 325, 250, 40))
    p.at(cell(365, 370, 330, 44, f"UDP 50001 → {PC38}:50001", RED, 16), 3, 4, mark=(365, 370, 330, 44))
    p.at(pill(480, 452, "같은 LAN이면 신분을 묻지 않아요", ORANGE, 17, True, 340), 4, 4)
    return p.render()


def p6():
    p = Pg("UPnP, 켜 둘까 꺼 둘까?", "정답 대신 대가를 비교해요",
           ["켜면 편하고 끄면 통제할 수 있어요", "켠 쪽은 편하지만 목록을 열어 봐야 알아요",
            "끈 쪽은 일부 프로그램이 불편하지만 통제돼요", "우리 회사는 끄고 신청과 기록으로 가요"])
    L, R = 50, 510
    p.base(box(L, 125, 400, 290, GREEN, PANEL, 16, sw=2) + lbl(L + 200, 158, "UPnP 켜 둠", GREEN, 20) + rt(L + 200, 215),
           box(R, 125, 400, 290, BLUE, PANEL, 16, sw=2) + lbl(R + 200, 158, "UPnP 끔", BLUE, 20) + rt(R + 200, 215))
    left = cell(L + 25, 290, 350, 44, "프로그램이 알아서 연결해요", GREEN, 17) + cell(L + 25, 345, 350, 44, "열린 줄은 목록을 봐야 알아요", RED, 17)
    right = cell(R + 25, 290, 350, 44, "일부 P2P·게임은 불편해요", RED, 17) + cell(R + 25, 345, 350, 44, "신청받아 사람이 열고 기록해요", GREEN, 17)
    p.at(pill(L + 200, 320, "편해요", GREEN, 18, True, 150) + pill(R + 200, 320, "통제할 수 있어요", BLUE, 18, True, 220), 1, 1)
    p.at(left, 2, 3, mark=(L + 25, 290, 350, 99))
    p.at(dim(left), 4, 4)
    p.at(right, 3, 4, mark=(R + 25, 290, 350, 99))
    p.at(pill(480, 456, "우리 회사: 끄고 신청·기록으로 열기", ORANGE, 17, True, 400), 4, 4, mark=(R, 125, 400, 290))
    return p.render()


ITEMS = [
    ("u12-l04-p01-three-unknown-lines", p1, "내가 연 적 없는 포트가 열려 있다?",
     "수동 포워딩 목록은 비었는데 UPnP 목록에 192.168.10.37, .44, .38을 가리키는 TCP 6881, UDP 27015, UDP 50001 줄이 세 개 있고 지우의 기억에는 모두 없다는 그림입니다.",
     "수동 포워딩 목록과 UPnP 목록은 따로 점검합니다.", 0),
    ("u12-l04-p03-plug-to-network", p3, "꽂기만 하면 되는 편리함, 네트워크로",
     "USB를 꽂으면 설정 없이 바로 쓰이는 PnP와, 프로그램이 공유기에 포워딩 줄을 자동으로 만드는 UPnP를 나란히 보여 주고 편해진 만큼 설정이 눈에서 멀어진다고 짚습니다.",
     "UPnP는 PnP의 자동화 발상을 공유기 설정으로 넓힌 기능입니다.", 0),
    ("u12-l04-p04-discover-request-result", p4a, "프로그램은 공유기에 어떻게 부탁할까?",
     "PC 192.168.10.37의 프로그램이 공유기를 찾는 발견, 6881번 매핑을 요청하는 단계, 변환표에 줄이 생기는 결과를 차례로 보여 주고 사람이 입력하지 않아도 줄이 생긴다고 짚습니다.",
     "UPnP는 발견, 요청, 결과의 세 단계로 사람의 입력 없이 줄을 만듭니다.", 0),
    ("u12-l04-p4b-accepted-not-reachable", p4b, "요청이 성공해도 닿는다는 보장은 없다",
     "공유기 변환표에 6881번 줄이 생겨 요청은 성공했지만 협력사 PC의 연결은 통신사 NAT, 방화벽, 기다리지 않는 프로그램 중 한 곳에서 막힐 수 있어 요청 성공과 길이 열린 것은 별개라는 그림입니다.",
     "매핑 요청이 받아들여진 것과 바깥에서 실제로 닿는 것은 별개입니다.", 3),
    ("u12-l04-p05-no-login-no-check", p5, "비밀번호도 없이 포트를 열어 준다고?",
     "관리자 로그인 기록이 없는데 감염된 PC 192.168.10.38의 UPnP 요청으로 공유기가 UDP 50001 줄을 만들었고, 같은 LAN 요청이면 신분을 묻지 않아 바깥에서 닿는 환경이면 노출된다는 그림입니다.",
     "UPnP는 같은 LAN 안의 요청을 인증 없이 받아 주는 경우가 많습니다.", 0),
    ("u12-l04-p06-on-or-off-cost", p6, "UPnP, 켜 둘까 꺼 둘까?",
     "UPnP를 켜 두면 편하지만 열린 줄을 목록으로 확인해야 하고, 끄면 일부 프로그램이 불편하지만 신청과 기록으로 통제할 수 있다는 비교와 우리 회사의 선택입니다.",
     "우리 회사는 UPnP를 끄고 필요한 포트만 신청받아 열고 기록합니다.", 0),
]
PAGE_OF = [1, 3, 4, 4, 5, 6]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, fn, *_ in ITEMS:
        done(OUT, f, fn)
    if "--svg-only" not in sys.argv:
        pages = [[] for _ in range(6)]
        for (f, _, t, al, c, ap), pg in zip(ITEMS, PAGE_OF):
            pages[pg - 1].append((f, t, al, c, ap))
        pages[1] = None  # Page 2 kept
        wire_items(LESSON / "lesson.md", pages)
    print("ok", len(ITEMS), "svgs")
