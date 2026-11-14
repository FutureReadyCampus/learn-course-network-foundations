#!/usr/bin/env python3
"""Unit 13 Lesson 1 (부하 분산과 서버 상태 확인): one 4-step example SVG per Page (8). Run from repo root:
python3 scripts/svg_pairs/u13_l01_lb.py   (--svg-only skips the lesson.md edit).

Running example = the Lesson body: VIP 203.0.113.10:443, 서버 풀 192.168.20.11~.13, 점심시간 회선 30% / GPU 100%(가정).
Step arc per Page: ① 상황 → ② 동작 → ③ 결과(✓/✗) → ④ 기억할 점. 단계마다 새로 생기는 요소만 주황 테두리.
Also holds the helpers shared by u13_l02_ha.py and u13_l03_gslb.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, dur, person, arrow
from u7_l01 import mv

ROOT = Path(__file__).resolve().parents[2]
UNIT = next((ROOT / "units").glob("09-load-balancing/lessons/restructured"))


def lesson_dir(n):
    return next(UNIT.glob(f"{n:02d}-*"))


LESSON = lesson_dir(1)
OUT = LESSON / "assets" / "animations"
VIP = "203.0.113.10:443"


# ---- shared helpers ----------------------------------------------------------------
def new(n=4):
    return Anim(n, dur(False))


def mk(a, x, y, w, h, t, rx=12):
    """주황 테두리: 단계 t에서만 보이는 '방금 바뀐 것' 표시."""
    return a.vis(hl(x, y, w, h, ORANGE, rx), t, t)


def fl(a, pts, step, c=BLUE):
    """한 단계 안에서만 움직이는 패킷."""
    return mv(a, packet(0, 0, c), pts, step, step, step, 0.1, 0.9)


def sv(x, y, label, c=GREEN, w=124, h=46, dash=False, tc=None):
    return (box(x - w / 2, y - h / 2, w, h, c, PANEL, 8, dash=dash, sw=3)
            + f'<rect x="{x - w / 2 + 9}" y="{y - h / 2 + 10}" width="6" height="{h - 20}" rx="3" fill="{c}"/>'
            + text(x + 7, y + 6, label, 17, tc or TXT, 700))


def lbx(x, y, label="로드 밸런서", sub=None, c=BLUE, w=150, h=64, dash=False):
    s = box(x - w / 2, y - h / 2, w, h, c, PANEL, 10, dash=dash, sw=3)
    if sub:
        return s + text(x, y - 4, label, 17, c, 700) + text(x, y + 18, sub, 14, MUTED, 700)
    return s + text(x, y + 6, label, 18, c, 700)


def bar(x, y, w, pct, c, h=18):
    return (box(x, y, w, h, LINE, BG, 5, sw=2)
            + f'<rect x="{x}" y="{y}" width="{max(4, w * pct / 100):.0f}" height="{h}" rx="5" fill="{c}"/>')


def panel(x, title, c, y=125, w=420, h=300):
    return box(x, y, w, h, c, PANEL, 16, dash=True, sw=3) + text(x + w / 2, y + 32, title, 19, c, 700)


def cloud(x, y, label="인터넷"):
    return (f'<ellipse cx="{x}" cy="{y}" rx="62" ry="38" fill="{PANEL}" stroke="{BLUE}" stroke-width="3"/>'
            + text(x, y + 7, label, 19, BLUE, 700))


def gear(x, y, c=ORANGE):
    return text(x, y, "⚙", 30, c, 700)


def pools(x, ys, labels=(".11", ".12", ".13"), c=GREEN):
    return "".join(sv(x, y, f"서버 {l}", c) for y, l in zip(ys, labels))


def write_all(items, out, wire_fn, lesson_md):
    out.mkdir(parents=True, exist_ok=True)
    for it in items:
        write(out, it[0], it[-1]())
    if "--svg-only" not in sys.argv:
        wire_fn(lesson_md, items)
    print("ok", len(items), "svgs")


def wire_pages(lesson_md, items):
    """Insert one illustration per Page right after its `- page_id:` line. items = (file, page_id, title, alt, caption, after_paragraph, fn)."""
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = Path(lesson_md)
    head, fm, body = md.read_text(encoding="utf-8").split("---\n", 2)
    for f, pid, t, al, c, ap, _ in items:
        if f"assets/animations/{f}.svg" in fm:
            continue
        blk = (f"  illustrations:\n  - file: assets/animations/{f}.svg\n    title: {q(t)}\n    alt: {q(al)}\n"
               f"    caption: {q(c)}\n    after_paragraph: {ap}\n")
        assert f"- page_id: {pid}\n" in fm, pid
        fm = fm.replace(f"- page_id: {pid}\n", f"- page_id: {pid}\n{blk}", 1)
    md.write_text(head + "---\n" + fm + "---\n" + body, encoding="utf-8")


# 1 손님이 몰리자 느려진 한결봇 ---------------------------------------------------------
def p1():
    a = new()
    crowd = person(70, 290) + person(110, 280) + person(150, 290)
    q = "".join(packet(716, y) for y in (250, 290, 330))
    body = [crowd + line(200, 290, 760, 290, LINE, 4, "10 8") + sv(820, 290, "서버 1대", GREEN, 120, 60),
            a.vis(pill(480, 165, "점심시간, 요청이 몰려요", BLUE, 18, False, 260), 1, 4),
            a.vis(bar(330, 250, 200, 30, GREEN) + text(430, 236, "회선 사용률 30%(가정)", 16, GREEN, 700), 2, 4), mk(a, 322, 224, 216, 60, 2),
            fl(a, [(210, 290), (680, 290)], 2),
            a.vis(bar(740, 365, 160, 100, RED) + text(820, 355, "GPU 100%", 16, RED, 700) + q + cross(820, 410), 3, 4), mk(a, 732, 338, 176, 60, 3),
            a.vis(pill(480, 435, "회선이 아니라 서버 한 대의 한계예요", ORANGE, 18, True, 380), 4, 4)]
    caps = ["점심시간에 요청이 서버 한 대로 몰려요", "회선은 30%만 써서 한가해요", "GPU는 100%라 요청이 줄 서 기다려요", "한 대의 한계라 여러 대로 나눠야 해요"]
    return frame(a, "한결봇은 왜 느려졌을까?", "회선과 서버 중 어디가 꽉 찼는지 나눠 봐요", caps, "".join(body))


# 2 포트 포워딩을 서버 여러 대로 늘리면? ----------------------------------------------------
def p2():
    a = new()
    L, R = 40, 500
    body = [panel(L, "포트 포워딩", MUTED), panel(R, "L4 로드 밸런서", BLUE),
            rt_(L + 80, 250), pools(L + 330, (210, 280, 350), c=MUTED),
            line(L + 130, 250, L + 266, 210, MUTED, 3),
            a.vis(text(L + 80, 320, "외부 443", 16, TXT, 700), 1, 4),
            a.vis(line(L + 130, 250, L + 266, 280, ORANGE, 3, "6 5") + pill(L + 210, 396, "443 → .12 규칙은 거부", RED, 15, False, 210)
                  + cross(L + 408, 280), 2, 4), mk(a, L + 266, 257, 128, 52, 2),
            a.vis(lbx(R + 100, 270, "로드 밸런서", VIP, BLUE, 170, 74)
                  + "".join(line(R + 185, 270, R + 270, y, BLUE, 3) for y in (210, 280, 350)) + pools(R + 335, (210, 280, 350)), 3, 4), mk(a, R + 15, 233, 170, 74, 3),
            fl(a, [(R + 60, 270), (R + 150, 270), (R + 250, 280)], 3, ORANGE),
            a.vis(pill(480, 450, "L4는 IP·포트만 보고 서버를 골라요", GREEN, 18, True, 360), 4, 4)]
    caps = ["포워딩은 포트 하나에 서버 한 대예요", "같은 443에 서버를 더 넣으려 해요", "로드 밸런서가 연결마다 서버를 골라요", "L4 장비는 IP·포트만 보고 나눠요"]
    return frame(a, "포트 포워딩을 서버 여러 대로?", "고정 안내판 vs 연결마다 고르는 장비", caps, "".join(body))


def rt_(x, y, label="공유기"):
    return router(x, y, label)


# 3 손님은 왜 주소 하나만 알면 될까? --------------------------------------------------------
def p3():
    a = new()
    body = [person(90, 280, "손님"), lbx(430, 300, "로드 밸런서", None, BLUE, 160, 64),
            pools(790, (190, 300, 410)) + line(510, 300, 725, 190, LINE, 3) + line(510, 300, 725, 300, LINE, 3) + line(510, 300, 725, 410, LINE, 3),
            line(150, 300, 350, 300, LINE, 3),
            a.vis(pill(200, 225, "bot.hangyeol.example", BLUE, 15, False, 210), 1, 4), mk(a, 95, 208, 210, 34, 1),
            a.vis(pill(440, 225, VIP, ORANGE, 16, True, 190), 2, 4), mk(a, 345, 208, 190, 34, 2),
            fl(a, [(160, 300), (360, 300)], 2),
            fl(a, [(500, 300), (640, 300), (725, 300)], 3, GREEN), a.vis(check(870, 300), 3, 4), mk(a, 727, 277, 128, 52, 3),
            a.vis(pill(480, 455, "서버가 늘어도 손님이 아는 주소는 그대로", GREEN, 18, True, 420), 4, 4)]
    caps = ["손님은 이름 하나만 알아요", "이름을 풀면 VIP 주소 하나가 나와요", "로드 밸런서가 서버 풀 중 하나로 넘겨요", "서버 수가 바뀌어도 주소는 그대로예요"]
    return frame(a, "손님은 주소 하나만 알면 돼요", "대표 주소(VIP)는 서버가 아니라 로드 밸런서 것이에요", caps, "".join(body))


# 4 대화 중에 한결봇이 앞말을 잊는다면? -----------------------------------------------------
def p4():
    a = new()
    body = [person(80, 290), lbx(260, 300, "로드 밸런서", None, BLUE, 150, 60) + line(140, 300, 185, 300, LINE, 3),
            sv(560, 190, "서버 .11") + sv(560, 300, "서버 .12") + sv(560, 410, "서버 .13", MUTED, tc=MUTED),
            line(335, 300, 498, 190, LINE, 3) + line(335, 300, 498, 300, LINE, 3),
            a.vis(pill(110, 215, "거실은 15평이에요", BLUE, 14, False, 170), 1, 1),
            fl(a, [(150, 300), (260, 300), (440, 200), (498, 190)], 1),
            a.vis(cell(630, 172, 90, 36, "15평", GREEN, 17), 1, 4), mk(a, 626, 168, 98, 42, 1),
            a.vis(pill(110, 215, "아까 평수로 계산해 줘", BLUE, 14, False, 190), 2, 2),
            fl(a, [(150, 300), (260, 300), (440, 300), (498, 300)], 2),
            a.vis(pill(715, 300, "처음 듣는 이야기", RED, 15, False, 160) + cross(820, 300), 3, 3), mk(a, 498, 277, 124, 46, 3),
            a.vis(box(790, 255, 130, 90, GREEN, PANEL, 10, sw=3) + text(855, 292, "공유 저장소", 16, GREEN, 700) + text(855, 322, "15평", 16, TXT, 700)
                  + line(720, 190, 790, 280, GREEN, 3) + line(620, 300, 790, 300, GREEN, 3) + line(620, 410, 790, 330, GREEN, 3) + check(855, 235), 4, 4), mk(a, 786, 251, 138, 98, 4),
            a.vis(pill(480, 455, "대화 기록은 서버 밖 저장소에 두면 안전해요", GREEN, 18, True, 420), 4, 4)]
    caps = ["첫 요청은 서버 .11이 받고 기억해요", "다음 요청은 다른 서버로 가요", "서버 .12는 앞말을 몰라요", "공유 저장소면 어느 서버든 기억해요"]
    return frame(a, "대화 중에 앞말을 잊는다면?", "요청마다 다른 서버가 받을 수 있어요", caps, "".join(body))


# 5 차례대로 나눠 주면 공평할까? ------------------------------------------------------------
def p5():
    a = new()
    ys = (190, 290, 390)
    body = [lbx(130, 290, "로드 밸런서", None, BLUE, 160, 64), pools(380, ys),
            "".join(line(210, 290, 318, y, LINE, 3) for y in ys),
            a.vis("".join(text(268, y - 16 + (290 - y) * 0.25, f"{i + 1}", 17, ORANGE, 700) for i, y in enumerate(ys)) + pill(130, 160, "라운드 로빈 1→2→3", BLUE, 16, False, 200), 1, 3), mk(a, 30, 143, 200, 34, 1),
            a.vis(bar(470, 181, 150, 15, BLUE) + bar(470, 281, 380, 95, RED) + bar(470, 381, 100, 20, BLUE), 2, 4),
            a.vis(text(660, 265, "긴 견적 계산", 16, RED, 700), 2, 4), mk(a, 462, 273, 396, 34, 2),
            a.vis(cross(880, 290) + text(660, 396, "놀고 있어요", 16, MUTED, 700), 3, 4), mk(a, 462, 373, 120, 38, 3),
            a.vis(pill(700, 150, "최소 연결: 한가한 서버로", GREEN, 18, True, 280) + check(880, 390), 4, 4)]
    caps = ["라운드 로빈은 순서대로 나눠 줘요", "그런데 요청 하나가 아주 길어요", "서버 .12만 막히고 .13은 놀아요", "최소 연결은 한가한 서버를 골라요"]
    return frame(a, "차례대로 나눠 주면 공평할까?", "개수만 세면 일의 크기를 몰라요", caps, "".join(body))


# 6 도면 질문만 큰 GPU로 보낼 수 있을까? ------------------------------------------------------
def p6():
    a = new()
    L, R = 40, 500
    body = [panel(L, "L4 · IP와 포트만 봐요", MUTED), panel(R, "L7 · 경로까지 읽어요", BLUE)]
    for x in (L, R):
        body += [packet(x + 70, 280, ORANGE) + text(x + 70, 320, "도면 요청", 15, ORANGE, 700),
                 lbx(x + 215, 280, "로드 밸런서", None, MUTED if x == L else BLUE, 130, 56) + line(x + 95, 280, x + 150, 280, LINE, 3),
                 sv(x + 345, 215, "작은 서버", GREEN, 110, 46) + sv(x + 345, 350, "큰 GPU", VIOLET, 110, 46)]
    body += [a.vis(fl_static(L + 280, 280, L + 345, 230) + cross(L + 400, 262) + pill(L + 215, 395, "내용은 안 보여요", RED, 15, False, 170), 2, 4), mk(a, L + 288, 192, 114, 46, 2),
             a.vis(line(R + 280, 280, R + 345, 340, GREEN, 4) + check(R + 400, 305) + pill(R + 215, 395, "/api/drawing 보고 구분", GREEN, 15, False, 230), 3, 4), mk(a, R + 288, 327, 114, 46, 3),
             a.vis(pill(480, 455, "경로·쿠키로 나누려면 L7이 필요해요", GREEN, 18, True, 380), 4, 4)]
    caps = ["도면 요청과 일반 문의가 섞여 와요", "L4는 겉봉만 봐서 가르지 못해요", "L7은 경로를 읽어 큰 GPU로 보내요", "경로·쿠키 기준이면 L7을 써요"]
    return frame(a, "도면 질문만 큰 GPU로?", "겉봉만 보는 L4 vs 내용을 읽는 L7", caps, "".join(body))


def fl_static(x1, y1, x2, y2, c=RED):
    return line(x1, y1, x2, y2, c, 4, "6 5")


# 7 모델을 싣는 중인 서버로 왜 요청이 갔을까? --------------------------------------------------
def p7():
    a = new()
    ys = (190, 290, 390)
    body = [lbx(150, 290, "로드 밸런서", None, BLUE, 170, 64), pools(560, ys),
            "".join(line(235, 290, 498, y, LINE, 3) for y in ys),
            a.vis(text(680, 296, "모델 싣는 중", 16, ORANGE, 700), 1, 2),
            a.vis(pill(150, 205, "ping 응답 정상", GREEN, 16, False, 160), 1, 4), mk(a, 70, 188, 160, 34, 1),
            fl(a, [(235, 290), (420, 290), (498, 290)], 2, ORANGE), a.vis(cross(640, 262), 2, 2), mk(a, 498, 267, 124, 46, 2),
            a.vis(sv(560, 290, "서버 .12", MUTED, dash=True, tc=MUTED) + text(700, 296, "풀에서 제외", 16, MUTED, 700) + check(790, 290), 3, 4), mk(a, 498, 267, 124, 46, 3),
            a.vis(pill(480, 455, "준비 완료까지 묻고, 연속 실패로 판단해요(가정)", GREEN, 17, True, 440), 4, 4)]
    caps = ["ping만 보면 .12가 정상으로 보여요", "요청이 가서 오류가 나요", "/health로 물으면 준비 전이라 빼요", "서비스가 준비됐는지를 확인해요"]
    return frame(a, "모델을 싣는 서버로 왜 갔을까?", "켜졌다고 일할 준비가 된 건 아니에요", caps, "".join(body))


# 8 서버 한 대를 빼도 손님이 모르게 하려면? -----------------------------------------------------
def p8():
    a = new()
    ys = (190, 290, 390)
    body = [lbx(130, 290, "로드 밸런서", None, BLUE, 160, 64), pools(380, ys),
            "".join(line(210, 290, 318, y, LINE, 3) for y in ys[1:]),
            a.vis(line(210, 290, 318, 190, LINE, 3), 1, 1),
            a.vis(bar(470, 181, 380, 80, RED) + bar(470, 281, 380, 60, GREEN) + bar(470, 381, 380, 60, GREEN)
                  + text(660, 165, "서버 .11 CPU 80%·오류", 15, RED, 700), 1, 2),
            a.vis(line(210, 290, 318, 190, RED, 3, "6 5") + pill(250, 215, "새 연결에서 제외", ORANGE, 15, False, 170)
                  + sv(380, 190, "서버 .11", MUTED, dash=True, tc=MUTED), 2, 4), mk(a, 318, 167, 124, 46, 2),
            a.vis(bar(470, 281, 380, 90, GREEN) + bar(470, 381, 380, 90, GREEN) + text(660, 265, "나머지 두 대가 90%(가정)", 15, ORANGE, 700) + check(890, 330), 3, 4), mk(a, 462, 273, 396, 34, 3),
            a.vis(pill(480, 455, "평소 여유가 있어야 한 대를 빼도 버텨요", GREEN, 18, True, 400), 4, 4)]
    caps = ["서버 .11이 계속 느리고 오류가 나요", "새 연결에서 먼저 빼요", "남은 두 대가 90%씩 맡아요(가정)", "빠진 몫을 받을 여유가 필요해요"]
    return frame(a, "서버 한 대를 빼도 손님이 모르게", "먼저 빼고, 남은 서버의 여유를 따져요", caps, "".join(body))


ITEMS = [
    ("u13-l01-p1-slow", "u13-l01-page-01", "한결봇은 왜 느려졌을까?", "점심시간 요청이 서버 한 대로 몰려 회선 사용률은 30%인데 GPU는 100%가 되고, 한 대의 한계라 여러 대로 나눠야 한다는 흐름입니다.", "회선이 아니라 서버 한 대의 처리 한계가 느림의 원인입니다.", 2, p1),
    ("u13-l01-p2-forwarding", "advanced-source-17-page-01", "포트 포워딩을 서버 여러 대로 늘리면?", "왼쪽은 외부 443이 서버 .11 한 대에만 연결돼 .12 규칙이 거부되고, 오른쪽은 로드 밸런서가 연결마다 서버 .11~.13 중 하나를 고르는 모습입니다.", "포트 포워딩은 목적지가 한 대뿐이고, L4 로드 밸런서는 연결마다 서버를 고릅니다.", 2, p2),
    ("u13-l01-p3-vip", "advanced-source-17-page-02", "손님은 주소 하나만 알면 돼요", "손님이 bot.hangyeol.example을 풀어 VIP 203.0.113.10:443을 받고, 로드 밸런서가 서버 풀 192.168.20.11~.13 중 하나로 넘기는 모습입니다.", "VIP는 로드 밸런서의 주소라서 서버가 늘거나 줄어도 손님이 쓰는 주소는 같습니다.", 2, p3),
    ("u13-l01-p4-session", "advanced-source-17-page-03", "대화 중에 앞말을 잊는다면?", "첫 요청은 서버 .11이 기억하지만 다음 요청이 서버 .12로 가면 앞말을 모르고, 공유 저장소에 두면 어느 서버든 같은 기록을 읽는 모습입니다.", "대화 기록을 서버 밖 공유 저장소에 두면 어느 서버가 받아도 맥락이 이어집니다.", 2, p4),
    ("u13-l01-p5-policy", "advanced-source-17-page-04", "차례대로 나눠 주면 공평할까?", "라운드 로빈은 순서대로 나누지만 긴 요청이 걸린 서버 .12만 막히고 .13은 놀며, 최소 연결은 한가한 서버를 고르는 모습입니다.", "라운드 로빈은 개수만 세므로 요청 처리 시간이 들쭉날쭉하면 최소 연결이 어울립니다.", 1, p5),
    ("u13-l01-p6-l7", "u13-l01-page-06", "도면 질문만 큰 GPU로?", "왼쪽 L4는 IP와 포트만 봐서 도면 요청을 가르지 못하고, 오른쪽 L7은 /api/drawing 경로를 읽어 큰 GPU 서버로 보내는 모습입니다.", "경로나 쿠키로 나누려면 요청 내용을 읽는 L7 로드 밸런서가 필요합니다.", 2, p6),
    ("u13-l01-p7-health", "advanced-source-17-page-05", "모델을 싣는 서버로 왜 갔을까?", "ping에는 정상으로 답하지만 모델을 싣는 중인 서버 .12로 요청이 가 오류가 나고, /health로 준비 여부를 물으면 풀에서 제외되는 모습입니다.", "헬스 체크는 서버가 켜졌는지가 아니라 서비스가 준비됐는지를 확인해야 합니다.", 2, p7),
    ("u13-l01-p8-drain", "advanced-source-17-page-06", "서버 한 대를 빼도 손님이 모르게", "오류가 잦은 서버 .11을 새 연결에서 먼저 빼면 남은 두 대가 90%씩 맡는 모습으로, 평소 여유가 있어야 버틴다는 뜻입니다.", "서버를 뺄 때는 새 연결에서 먼저 빼고 남은 서버의 여유를 따져야 합니다.", 2, p8),
]
assert len(ITEMS) == 8

if __name__ == "__main__":
    write_all(ITEMS, OUT, wire_pages, LESSON / "lesson.md")
