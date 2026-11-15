#!/usr/bin/env python3
"""Unit 11 Lesson 5 SVG review: Page 1 +rule-order SVG, Page 3 +trust-list SVG, Page 5 replaces the stale 「공용 PC」 combined-box SVG.
Run from repo root: python3 scripts/svg_pairs/u11_l05_rev.py  (--svg-only skips lesson.md edit)."""
import sys
from u11_new_common import *  # noqa: F401,F403


def rule(x, y, s, c):
    return box(x, y, 400, 50, c, PANEL, 10, sw=3) + text(x + 16, y + 31, s, 17, TXT, 700, "start")


def p1b():
    a = new()
    LX, RX = 50, 510
    arrow = lambda x: line(x, 236, x, 252, LINE, 4) + f'<polygon points="{x},262 {x - 8},248 {x + 8},248" fill="{LINE}"/>'
    body = [text(250, 190, "차단 규칙을 위에 둔 경우", 20, RED, 700), text(710, 190, "허용 규칙을 위에 둔 경우", 20, GREEN, 700),
            rule(LX, 275, "① 사내 PC 192.168.10.0/24 → 차단", RED), rule(LX, 340, "② 프록시 192.168.10.5 → 허용", GREEN),
            rule(RX, 275, "① 프록시 192.168.10.5 → 허용", GREEN), rule(RX, 340, "② 사내 PC 192.168.10.0/24 → 차단", RED),
            a.vis(pill(480, 135, "프록시 192.168.10.5도 192.168.10.0/24 안에 있어요", ORANGE, 17, False, 590), 1, 3), mark(a, 185, 118, 590, 34, 1)]
    for cx in (250, 710):
        body += [mv(a, packet(0, 0), [(cx - 70, 205), (cx - 70, 232)], 2, 2, 4, 0.1, 0.7), a.vis(arrow(cx - 70) + text(cx - 38, 238, "프록시의 요청", 16, TXT, 700, "start"), 2, 4)]
    body += [mark(a, LX, 275, 400, 50, 2), mark(a, RX, 275, 400, 50, 2),
             a.vis(cross(LX + 376, 300) + pill(250, 425, "프록시도 못 나가요", RED, 17, False, 260), 3, 4),
             a.vis(check(RX + 376, 300) + pill(710, 425, "프록시는 나가요", GREEN, 17, False, 260), 3, 4),
             mark(a, 120, 408, 260, 34, 3), mark(a, 580, 408, 260, 34, 3),
             a.vis(pill(480, 135, "좁은 허용 규칙을 위에 두어요", BLUE, 18, True, 340), 4, 4), mark(a, 310, 118, 340, 34, 4)]
    caps = ["프록시 주소도 PC 대역 안에 들어 있어요", "요청은 위에서부터 규칙과 비교돼요", "처음 맞는 규칙에서 결과가 정해져요", "좁은 허용 규칙을 위에 두어요"]
    return frame(a, "방화벽 규칙은 위에서부터 읽어요", "프록시의 요청이 어느 규칙에 먼저 걸릴까요?", caps, "".join(body))


def p3b():
    a = new()
    Y1, Y2 = 215, 385
    body = []
    for y, lab, miss in ((Y1, "사내 PC", False), (Y2, "회사 CA 없는 기기", True)):
        chip2 = (box(300, y - 17, 150, 34, RED, BG, 8, dash=True, sw=2) + text(375, y + 6, "회사 CA 없음", 16, RED, 700) if miss
                 else box(300, y - 17, 150, 34, GREEN, BG, 8, sw=2) + text(375, y + 6, "회사 CA", 16, GREEN, 700))
        body += [dev(lab, 95, y, None, laptop), box(180, y - 36, 280, 72, LINE, PANEL, 10, sw=2),
                 box(190, y - 17, 100, 34, BLUE, BG, 8, sw=2) + text(240, y + 6, "공인 CA", 16, BLUE, 700) + chip2,
                 node(740, y, "프록시", None, 200, 60)]
    body += [lbl(320, 152, "PC의 신뢰 목록", MUTED, 16), mark(a, 180, Y1 - 36, 280, 72, 1), mark(a, 180, Y2 - 36, 280, 72, 1)]
    for y in (Y1, Y2):
        body += [a.vis(box(580, y - 42, 320, 84, GREEN, PANEL, 10, sw=3) + text(740, y - 16, "프록시의 인증서", 16, MUTED, 700)
                       + text(740, y + 6, "ai-chat.example", 18, TXT, 700) + text(740, y + 30, "회사 CA 서명", 16, GREEN, 700)
                       + line(575, y, 484, y, LINE, 4) + f'<polygon points="466,{y} 486,{y - 9} 486,{y + 9}" fill="{LINE}"/>', 2, 4), mark(a, 580, y - 42, 320, 84, 2)]
    body += [a.vis(check(520, Y1) + pill(740, Y1 + 62, "회사 CA를 믿어서 연결돼요", GREEN, 17, False, 320), 3, 4),
             a.vis(cross(520, Y2) + pill(740, Y2 + 62, "믿는 CA가 아니라서 경고가 떠요", RED, 17, False, 330), 3, 4),
             mark(a, 580, Y1 + 45, 320, 34, 3), mark(a, 575, Y2 + 45, 330, 34, 3),
             a.vis(pill(480, 318, "인증서 경고는 무시하고 진행하면 안 돼요", BLUE, 17, True, 440), 4, 4), mark(a, 260, 301, 440, 34, 4)]
    caps = ["PC마다 믿는 CA 목록이 달라요", "프록시가 회사 CA 서명 인증서를 내밀어요", "회사 CA를 믿는 PC만 연결돼요", "경고가 떠도 무시하지 않아요"]
    return frame(a, "회사 CA를 믿는 PC만 열려요", "프록시가 내민 인증서를 PC가 받아들일까요?", caps, "".join(body))


def p5():
    a = new()
    YW, YM = 270, 420
    blk = lambda y0, c, s: box(470, y0, 200, 70, c, PANEL, 12, sw=3) + text(570, y0 + 28, s, 18, c, 700)
    body = [node(100, YW, "웹 · AI", None, 170, 60), node(100, YM, "메일 · 화상 회의", None, 170, 60),
            box(250, 160, 450, 295, GREEN, PANEL, 14, dash=True, sw=3) + text(475, 190, "통합 보안 장비 한 대", 18, MUTED, 700),
            box(272, 205, 90, 230, GREEN, BG, 10, sw=3) + text(317, 325, "방화벽", 18, GREEN, 700), blk(215, BLUE, "프록시"), blk(365, VIOLET, "IPS"),
            cloud(840, 345, "외부"),
            line(185, YW, 272, YW, LINE, 4, "10 8"), line(185, YM, 272, YM, LINE, 4, "10 8"),
            line(362, YW, 470, YW, LINE, 4, "10 8"), line(362, YM, 470, YM, LINE, 4, "10 8"),
            line(670, YW, 775, 330, LINE, 4, "10 8"), line(670, YM, 775, 360, LINE, 4, "10 8"),
            mark(a, 250, 160, 450, 295, 1),
            a.vis(pill(480, 135, "웹은 프록시를, 메일은 IPS를 거쳐요", BLUE, 18, False, 400), 2, 2), mark(a, 470, 215, 200, 70, 2), mark(a, 470, 365, 200, 70, 2),
            mv(a, packet(0, 0), [(210, YW), (317, YW), (570, YW), (770, 328)], 2, 2, 2, 0.05, 0.95),
            mv(a, packet(0, 0), [(210, YM), (317, YM), (570, YM), (770, 362)], 2, 2, 2, 0.05, 0.95),
            a.vis(blk(215, RED, "프록시") + lbl(570, 322, "CPU 100%", RED, 17, 700) + cross(722, 300) + check(722, 390), 3, 4), mark(a, 470, 215, 200, 70, 3),
            a.vis(pill(480, 135, "웹 · AI만 느리고 메일은 멀쩡해요", RED, 18, False, 390), 3, 3),
            a.vis(pill(480, 135, "기능별 사용률 · 연결 수 · 대기열을 따로 봐요", BLUE, 17, True, 520), 4, 4), mark(a, 220, 118, 520, 34, 4)]
    caps = ["물리적으로는 한 장비 한 대예요", "웹은 프록시를, 메일은 IPS를 거쳐요", "프록시만 바쁘면 웹과 AI만 느려져요", "기능별로 따로 확인해요"]
    return frame(a, "한 상자 안의 기능별 처리 경로", "웹만 느려지는 이유를 따라가 봐요", caps, "".join(body))


ILL = {
    "p1": ("u11-l05-p01-fw-rules", "프록시만 밖으로 나가게 하기",
           "방화벽 규칙으로 사내 PC 192.168.10.0/24의 직접 외부 연결은 막고 프록시 192.168.10.5의 연결만 허용하는 모습입니다.",
           "프록시 설정만으로는 직접 길이 남으므로 방화벽이 그 길을 막고, 좁은 허용 규칙을 위에 둡니다.", 3),
    "p1b": ("u11-l05-p1b-rule-order", "방화벽 규칙은 위에서부터 읽어요",
            "프록시 192.168.10.5의 요청이 차단 규칙이 위에 있으면 PC 대역 규칙에 먼저 맞아 막히고, 좁은 허용 규칙이 위에 있으면 허용되는 모습입니다.",
            "규칙은 위에서부터 처음 맞는 줄을 쓰므로, 프록시를 허용하는 좁은 규칙을 위에 둡니다.", 4),
    "p3": ("u11-l05-p03-tls-inspect", "암호화된 AI 대화 열어 보기",
           "프록시가 PC와 AI 서비스 사이의 TLS를 둘로 나눠 맺고, 풀린 요청에서 휴대전화 번호 형식을 찾아 업로드를 막는 모습입니다.",
           "TLS 검사는 회사 CA 신뢰가 있을 때만 되며 키 관리와 경고 무시 금지가 따릅니다.", 2),
    "p3b": ("u11-l05-p3b-trust-list", "회사 CA를 믿는 PC만 열려요",
            "프록시가 회사 CA 서명 인증서를 내밀면, 회사 CA가 신뢰 목록에 있는 사내 PC는 연결되고 회사 CA가 없는 기기는 인증서 경고를 보는 모습입니다.",
            "회사 CA를 신뢰 목록에 설치한 PC만 프록시의 인증서를 받아들이고, 없는 기기는 경고를 봅니다.", 3),
    "p5": ("u11-l05-p5-combined-box", "한 상자에 IPS와 프록시가 같이 있다면?",
           "통합 보안 장비 한 대 안에서 웹·AI 요청은 방화벽과 프록시를, 메일·화상 회의는 방화벽과 IPS를 거치고, 프록시 기능만 바빠지면 웹·AI만 느려지는 모습입니다.",
           "한 상자여도 기능마다 처리 경로가 달라서, 느려지는 트래픽도 기능별로 갈립니다.", 2),
}
GEN = {"p1b": p1b, "p3b": p3b, "p5": p5}

if __name__ == "__main__":
    d = lesson_dir(5)
    out = d / "assets" / "animations"
    for k, fn in GEN.items():
        write(out, ILL[k][0], fn())
    if "--svg-only" not in sys.argv:
        item = lambda k: (ILL[k][0], *ILL[k][1:])
        # pages 1..6 (page_id order); None leaves a Page untouched
        wire_items(d / "lesson.md", [[item("p1"), item("p1b")], None, [item("p3"), item("p3b")], None, [item("p5")], None])
    print("ok", d.name)
