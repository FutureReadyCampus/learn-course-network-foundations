#!/usr/bin/env python3
"""Unit 11 Lesson 6 (PC의 로컬 프록시로 통신 살펴보기) SVG review: Pages 2-5 get a main SVG + a second SVG each.
Pages 1 and 6 keep u11_l06_new_scenes.py's SVGs. Run from repo root: python3 scripts/svg_pairs/u11_l06_rev.py (--svg-only skips lesson.md).
Running example: 지우 PC 192.168.10.41 · 회사 프록시 192.168.10.5:8080 · 외부 클라우드 저장소 203.0.113.80:443 · 로컬 프록시 127.0.0.1:8080."""
import json
import sys
from u11_new_common import *  # noqa: F401,F403
from u12_l01_router import net  # noqa: F401


def pcbig(x, y, c=BLUE):
    return (box(x - 40, y - 34, 80, 56, c, PANEL, 6, sw=3) + box(x - 31, y - 26, 62, 40, LINE, LINE, 3, sw=0)
            + box(x - 6, y + 22, 12, 10, c, c, 0, sw=0) + box(x - 28, y + 32, 56, 6, c, c, 2, sw=0))


def file_icon(x, y, c=ORANGE):
    return box(x - 40, y - 50, 80, 100, c, PANEL, 8, sw=3) + "".join(box(x - 24, y - 32 + i * 16, 48, 5, c, c, 2, sw=0) for i in range(5))


def cert(x, y, c=ORANGE):
    return (box(x - 30, y - 24, 60, 48, c, PANEL, 5, sw=3) + box(x - 20, y - 14, 40, 5, c, c, 2, sw=0) + box(x - 20, y - 4, 26, 5, c, c, 2, sw=0)
            + f'<circle cx="{x + 16}" cy="{y + 10}" r="8" fill="{c}"/>')


# ---------------- Page 2 ----------------
def p2a():
    a = new()
    body = [net(40, 135, 560, 290, "지우 PC", GREEN), node(130, 285, "동기화 프로그램", None, 150, 70, VIOLET), server(850, 285, "클라우드 저장소"),
            a.vis(line(205, 285, 810, 285, LINE, 4, "10 8") + pill(730, 215, "요청이 바로 나가요", ORANGE, 17, False, 230), 1, 1),
            mv(a, packet(0, 0), [(245, 285), (770, 285)], 1, 1, 1, 0.1, 0.9),
            a.vis(node(420, 285, "로컬 프록시", None, 150, 70, BLUE) + line(205, 285, 345, 285, LINE, 4, "10 8") + line(495, 285, 810, 285, LINE, 4, "10 8"), 2, 4),
            mark(a, 345, 250, 150, 70, 2),
            mv(a, packet(0, 0), [(250, 285), (305, 285)], 2, 2, 2, 0.05, 0.45), mv(a, packet(0, 0), [(535, 285), (770, 285)], 2, 2, 2, 0.55, 0.95),
            a.vis(box(80, 365, 440, 44, GREEN, PANEL, 8, sw=2) + text(290, 394, "요청 한 건씩 URL · 헤더 · 본문이 남아요", 18, TXT, 700) + check(494, 387), 3, 4),
            mark(a, 80, 365, 440, 44, 3),
            a.vis(pill(480, 452, "PC 안에 프록시가 하나 더 생겨요", BLUE, 18, True, 360), 4, 4), mark(a, 300, 435, 360, 34, 4)]
    caps = ["동기화 프로그램은 저장소 서비스와 바로 이야기해요", "PC 안에 로컬 프록시를 먼저 거치게 해요", "요청이 한 건씩 목록으로 보여요", "프록시 하나가 더 생기는 구조예요"]
    return frame(a, "내 PC 안에 중계소 세우기", "도구가 통역사처럼 요청을 받아 적고 전달해요", caps, "".join(body))


def p2b():
    a = new()
    L, R = 250, 710
    body = [box(50, 125, 400, 285, GREEN, PANEL, 16, dash=True, sw=3) + text(L, 156, "지우의 테스트 PC", 19, GREEN, 700),
            box(510, 125, 400, 285, MUTED, PANEL, 16, dash=True, sw=3) + text(R, 156, "박 팀장 PC", 19, MUTED, 700),
            pcbig(L - 70, 270), file_icon(L + 70, 262), lbl(L + 70, 335, "가짜 견적서", TXT, 16, 700),
            pcbig(R - 70, 270), file_icon(R + 70, 262), lbl(R + 70, 335, "실제 작업 파일", TXT, 16, 700),
            a.vis(eye(L - 70, 205) + lbl(L - 20, 211, "도구", TXT, 16, 700)
                  + pill(L - 20, 375, "내 통신 · 가짜 데이터", GREEN, 17, False, 250) + check(L + 135, 375), 2, 4), mark(a, L - 145, 358, 250, 34, 2),
            a.vis(eye(R - 70, 205) + lbl(R - 20, 211, "도구", TXT, 16, 700)
                  + pill(R - 20, 375, "몰래 설치 · 승인 없음", RED, 17, False, 250) + cross(R + 135, 375), 3, 4), mark(a, R - 145, 358, 250, 34, 3),
            a.vis(pill(480, 451, "내 통신이거나 승인된 범위만 봐요", BLUE, 18, True, 380), 4, 4), mark(a, 290, 434, 380, 34, 4)]
    caps = ["테스트용 PC와 다른 사람의 PC가 있어요", "내 PC에서 가짜 데이터를 보는 것은 괜찮아요", "남의 PC에 몰래 도구를 깔면 안 돼요", "봐도 되는 통신은 내 것이거나 승인된 것뿐이에요"]
    return frame(a, "봐도 되는 통신은 어디까지?", "도구가 보여 줄 수 있어도 봐도 되는 것은 아니에요", caps, "".join(body))


# ---------------- Page 3 ----------------
def p3a():
    a = new()
    body = [net(40, 130, 620, 300, "지우 PC", GREEN), node(200, 300, "브라우저", None, 130, 70, BLUE),
            pill(200, 215, "프록시 칸: 127.0.0.1:8080", BLUE, 16, False, 290),
            box(430, 232, 160, 150, LINE, PANEL, 12, sw=2) + text(510, 258, "8080번 포트", 16, MUTED, 700),
            a.vis(node(510, 325, "프록시 도구", None, 130, 56, VIOLET) + lbl(510, 412, "켜져 있어요", GREEN, 16, 700), 1, 2),
            a.vis(box(445, 292, 130, 66, RED, PANEL, 8, dash=True, sw=2) + lbl(510, 330, "비어 있어요", RED, 16, 700) + lbl(510, 412, "꺼져 있어요", RED, 16, 700), 3, 4),
            cloud(830, 300), line(660, 300, 760, 300, LINE, 3, "8 6"), line(265, 300, 430, 300, LINE, 4, "10 8"),
            mv(a, packet(0, 0), [(300, 300), (395, 300)], 2, 2, 2, 0.1, 0.9), mv(a, packet(0, 0), [(300, 300), (395, 300)], 3, 3, 4, 0.1, 0.9),
            a.vis(pill(338, 350, "밖으로 안 나가요", BLUE, 16, False, 150), 2, 2),
            mark(a, 430, 232, 160, 150, 2), a.vis(check(590, 232), 2, 2),
            mark(a, 430, 232, 160, 150, 3), a.vis(cross(590, 232), 3, 4),
            a.vis(pill(480, 455, "도구가 켜졌는지, 포트가 같은지 먼저 봐요", GREEN, 17, True, 400), 4, 4), mark(a, 280, 438, 400, 34, 4)]
    caps = ["브라우저 프록시 칸에 127.0.0.1:8080을 적어요", "연결은 PC 밖으로 나가지 않고 8080번 포트로 가요", "도구가 꺼져 있으면 8080번 포트가 비어 있어요", "모든 사이트가 안 열리면 도구와 포트부터 봐요"]
    return frame(a, "127.0.0.1:8080은 어디로 갈까?", "먼저 이 PC의 8080번 포트에 들르라는 뜻이에요", caps, "".join(body))


def p3b():
    a = new()
    CY, PY = 372, 275  # 회사 프록시 y, 한 줄 y
    body = [net(30, 140, 370, 250, "지우 PC", GREEN), node(100, PY, "앱", None, 80, 60, BLUE), node(290, PY, "프록시 도구", "127.0.0.1:8080", 140, 60, VIOLET, 18),
            line(140, PY, 220, PY, LINE, 4, "10 8"), server(850, PY, "외부 클라우드 저장소", "203.0.113.80:443"),
            node(600, CY, "회사 프록시", "192.168.10.5:8080", 170, 60, BLUE),
            a.vis(packet(180, PY), 1, 1), mark(a, 220, PY - 30, 140, 60, 1),
            a.vis(pill(620, 195, "요청은 도구에 먼저 와요", ORANGE, 17, False, 260), 1, 1),
            a.vis(line(360, PY, 812, PY, RED, 4, "10 8") + cross(585, PY) + pill(620, 195, "바로 나가는 길은 막혀 있어요", RED, 17, False, 310), 2, 2),
            a.vis(line(330, PY + 30, 515, CY - 5, BLUE, 4) + line(685, CY - 5, 816, PY + 32, BLUE, 4) + check(850, 205)
                  + pill(600, 195, "상위 프록시 칸에 회사 프록시를 적어요", GREEN, 17, False, 340), 3, 4), mark(a, 515, CY - 30, 170, 60, 3),
            mv(a, packet(0, 0), [(365, 317), (470, 352)], 3, 3, 3, 0.05, 0.45), mv(a, packet(0, 0), [(720, 352), (765, 331)], 3, 3, 3, 0.55, 0.95),
            a.vis(pill(480, 458, "프록시 뒤에 프록시를 한 번 더 이어요", BLUE, 18, True, 380), 4, 4), mark(a, 290, 441, 380, 34, 4)]
    caps = ["앱의 요청은 도구에 먼저 도착해요", "도구가 바로 밖으로 나가려 하면 막혀요", "도구의 상위 프록시 칸에 회사 프록시를 적어요", "사무실에서는 프록시 뒤에 프록시가 와요"]
    return frame(a, "도구 뒤에 회사 프록시 잇기", "직접 외부 연결이 막힌 사무실 PC에서는요", caps, "".join(body))


# ---------------- Page 4 ----------------
def p4a():
    a = new()
    body = [a.vis(line(165, 290, 816, 290, VIOLET, 8), 1, 1),
            a.vis(line(165, 290, 385, 290, BLUE, 5) + line(575, 290, 816, 290, GREEN, 5), 2, 4),
            node(110, 290, "앱", None, 110, 70, BLUE), node(480, 290, "프록시 도구", None, 190, 70, VIOLET), server(850, 290, "클라우드 저장소"),
            a.vis(lock(480, 190, VIOLET) + pill(480, 375, "암호문을 그대로 흘려보내요", VIOLET, 17, False, 300), 1, 1),
            a.vis(lock(275, 185, BLUE) + pill(275, 245, "연결 ①", BLUE, 16, True, 110) + lock(695, 185, GREEN) + pill(695, 245, "연결 ②", GREEN, 16, True, 110)
                  + pill(480, 375, "TLS를 두 연결에서 따로 맺어요", BLUE, 17, False, 330), 2, 2), mark(a, 385, 255, 190, 70, 2),
            a.vis(lock(275, 185, BLUE) + pill(275, 245, "연결 ①", BLUE, 16, True, 110) + lock(695, 185, GREEN) + pill(695, 245, "연결 ②", GREEN, 16, True, 110)
                  + box(300, 350, 360, 46, GREEN, PANEL, 8, sw=2) + text(465, 380, "도구 안에서만 평문이 보여요", 18, TXT, 700) + check(633, 373), 3, 4), mark(a, 300, 350, 360, 46, 3),
            a.vis(pill(480, 445, "내용을 보려면 TLS를 따로 맺어야 해요", GREEN, 17, True, 400), 4, 4), mark(a, 280, 428, 400, 34, 4)]
    caps = ["처음엔 도구가 암호문을 그대로 전달하는 관이에요", "도구가 연결 ①②에서 TLS를 따로 맺어요", "그러면 도구 안에서만 평문이 드러나요", "내용을 보려면 TLS를 두 연결에서 따로 맺어요"]
    return frame(a, "HTTPS를 여는 방법: 연결 둘", "도구가 앱과 저장소 서비스를 따로 상대해요", caps, "".join(body))


def p4b():
    a = new()
    body = [net(40, 130, 880, 295, "지우 PC", GREEN), node(170, 260, "앱", None, 110, 70, BLUE), node(770, 260, "프록시 도구", None, 190, 70, VIOLET),
            line(225, 260, 675, 260, LINE, 4, "10 8"),
            a.vis(cert(470, 260) + lbl(470, 215, "도구가 서명한 인증서", ORANGE, 17, 700), 1, 4),
            a.vis(cross(170, 330) + pill(170, 385, "모르는 발급자예요", RED, 16, False, 200), 2, 2), mark(a, 115, 225, 110, 70, 2),
            a.vis(check(170, 330) + pill(170, 385, "인증서를 받아들여요", GREEN, 16, False, 220)
                  + box(330, 335, 300, 70, GREEN, PANEL, 8, sw=2) + lbl(480, 362, "PC의 신뢰 목록", MUTED, 16, 700) + text(480, 392, "도구의 루트 인증서", 18, GREEN, 700), 3, 4),
            mark(a, 330, 335, 300, 70, 3),
            a.vis(pill(480, 457, "분석이 끝나면 신뢰 목록에서 지워요", BLUE, 18, True, 380), 4, 4), mark(a, 290, 440, 380, 34, 4)]
    caps = ["도구가 자기 루트 인증서로 서명한 인증서를 내밀어요", "앱은 모르는 발급자라며 경고를 띄워요", "PC 주인이 루트 인증서를 신뢰 목록에 올려요", "분석이 끝나면 신뢰 목록에서 지워요"]
    return frame(a, "경고는 TLS가 일하는 증거", "신뢰는 PC 주인이 직접 준 것에서 나와요", caps, "".join(body))


# ---------------- Page 5 ----------------
def p5a():
    a = new()
    xs = [170, 325, 480, 635, 790]
    pieces = "".join(packet(x, 190) + lbl(x, 226, "조각 " + "①②③④⑤"[i], MUTED, 16, 700) for i, x in enumerate(xs))
    body = [pieces, a.vis(pill(480, 142, "요청 한 건이 조각 여러 개로 나뉘어요", ORANGE, 17, False, 380), 1, 1),
            a.vis(box(60, 268, 390, 160, BLUE, PANEL, 14, sw=2) + eye(125, 297) + text(280, 303, "캡처 도구가 보는 것", 18, BLUE, 700)
                  + cell(90, 322, 330, 30, "조각 ①", LINE, 16) + cell(90, 358, 330, 30, "조각 ②", LINE, 16) + cell(90, 394, 330, 26, "… 수천 줄", LINE, 16), 2, 4), mark(a, 60, 268, 390, 160, 2),
            a.vis(box(510, 268, 390, 160, GREEN, PANEL, 14, sw=2) + text(705, 303, "프록시가 보는 것", 18, GREEN, 700)
                  + cell(540, 328, 250, 70, "요청 1건", GREEN, 22), 3, 4), mark(a, 510, 268, 390, 160, 3),
            a.vis(check(840, 363), 3, 3), a.vis(lock(840, 349, RED), 4, 4),
            a.vis(pill(480, 456, "이어 붙여도 TLS 암호문이면 못 읽어요", RED, 17, False, 400), 4, 4), mark(a, 280, 439, 400, 34, 4)]
    caps = ["요청 한 건이 패킷 조각으로 나뉘어 가요", "캡처 도구는 조각을 그대로 찍어요", "프록시는 이어 붙인 Stream을 요청 한 건으로 봐요", "이어 붙이는 것과 암호를 푸는 것은 달라요"]
    return frame(a, "조각 대신 요청 한 건으로", "프록시는 이어 붙은 Stream을 읽어요", caps, "".join(body))


def p5b():
    a = new()
    Y = 265
    body = [file_icon(130, Y), lbl(130, Y + 82, "가짜 견적서", TXT, 18, 700), lbl(130, Y + 110, "3MB", ORANGE, 22, 700), server(850, Y, "클라우드 저장소"),
            a.vis(pill(480, 160, "가짜 견적서 하나를 올려요", ORANGE, 17, False, 280), 1, 1),
            a.vis(line(180, Y, 325, Y, LINE, 4, "10 8") + pill(252, Y - 40, "base64", BLUE, 16, True, 100)
                  + box(330, Y - 55, 300, 110, BLUE, PANEL, 12, sw=3) + lbl(480, Y - 68, "요청 본문", MUTED, 16, 700)
                  + text(480, Y - 15, "파일 이름", 18, TXT, 700) + text(480, Y + 25, "+ 긴 base64 글자", 18, BLUE, 700) + lbl(480, Y + 82, "약 4MB (3MB의 4/3배)", BLUE, 18, 700), 2, 4),
            mark(a, 330, Y - 55, 300, 110, 2),
            a.vis(pill(480, 392, "되돌리면 원본 파일과 같아요", GREEN, 17, False, 320) + check(300, 392), 3, 4), mark(a, 320, 375, 320, 34, 3),
            a.vis(line(630, Y, 812, Y, LINE, 4, "10 8"), 4, 4), mv(a, packet(0, 0), [(680, Y), (780, Y)], 4, 4, 4, 0.1, 0.9),
            a.vis(pill(480, 452, "견적서 파일 전체가 외부 클라우드 저장소로 가요", GREEN, 18, True, 500), 4, 4), mark(a, 230, 435, 500, 34, 4)]
    caps = ["지우가 가짜 견적서 3MB를 올려요", "요청 본문에는 base64 글자로 바뀌어 들어가요", "base64를 되돌리면 원본 파일과 같아요", "그래서 견적서 파일 전체가 클라우드 저장소로 가요"]
    return frame(a, "요청 본문 4MB의 정체", "파일을 글자로 바꾸면 크기가 약 4/3배가 돼요", caps, "".join(body))


SCENES = {
    2: [("u11-l06-p02-local-relay", "내 PC 안에 중계소 세우기", "지우 PC에서 동기화 프로그램이 저장소 서비스로 바로 보내던 요청이, PC 안에 로컬 프록시가 생기면 먼저 도착해 한 건씩 목록으로 남는 모습입니다.", "PC 안에 프록시가 하나 더 생기는 구조입니다.", 1, p2a),
        ("u11-l06-p02b-scope", "봐도 되는 통신은 어디까지?", "지우의 테스트 PC에서 가짜 데이터를 보는 것은 괜찮고, 박 팀장 PC에 몰래 도구를 설치하는 것은 안 된다는 비교입니다.", "봐도 되는 통신은 내 것이거나 조직이 승인한 범위뿐입니다.", 3, p2b)],
    3: [("u11-l06-p03-loopback-port", "127.0.0.1:8080은 어디로 갈까?", "브라우저 프록시 칸의 127.0.0.1:8080은 PC 밖으로 나가지 않고 이 PC의 8080번 포트로 가며, 도구가 꺼져 있으면 그 포트가 비어 연결이 거절됩니다.", "127.0.0.1은 이 PC 자신이고 8080은 도구가 기다리는 포트입니다.", 2, p3a),
        ("u11-l06-p03b-upstream", "도구 뒤에 회사 프록시 잇기", "사무실 PC에서 프록시 도구가 바로 외부로 나가는 길은 막혀 있어, 도구의 상위 프록시 칸에 회사 프록시를 적어 그 뒤로 클라우드 저장소에 연결합니다.", "프록시 도구 뒤에 회사 프록시를 한 번 더 잇습니다.", 3, p3b)],
    4: [("u11-l06-p04-two-tls", "HTTPS를 여는 방법: 연결 둘", "처음엔 암호문을 그대로 전달하던 도구가, 앱과 저장소 서비스 두 연결에서 TLS를 따로 맺으면 도구 안에서만 평문이 보이는 과정입니다.", "내용을 보려면 도구가 두 연결에서 TLS를 따로 맺어야 합니다.", 1, p4a),
        ("u11-l06-p04b-root-trust", "경고는 TLS가 일하는 증거", "도구가 자기 루트 인증서로 서명한 인증서를 내밀면 앱이 모르는 발급자라며 경고하고, PC 주인이 루트 인증서를 신뢰 목록에 올리면 받아들이며 분석이 끝나면 지웁니다.", "도구가 HTTPS를 여는 힘은 PC 주인이 준 신뢰에서 나옵니다.", 3, p4b)],
    5: [("u11-l06-p05-stream-view", "조각 대신 요청 한 건으로", "요청 한 건이 여러 패킷 조각으로 나뉘어 가고, 캡처 도구는 조각을 그대로 보지만 로컬 프록시는 이어 붙인 Stream을 요청 한 건으로 보며, 이어 붙여도 TLS 암호문이면 읽을 수 없는 모습입니다.", "Stream을 이어 붙이는 것과 TLS 암호를 푸는 것은 별개입니다.", 3, p5a),
        ("u11-l06-p05b-base64-size", "요청 본문 4MB의 정체", "3MB 가짜 견적서가 base64 글자로 바뀌어 약 4MB 요청 본문이 되고, 되돌리면 원본 파일과 같아 견적서 파일 전체가 외부 클라우드 저장소로 가는 것을 보여 줍니다.", "크기가 약 4/3배가 된 것은 base64 때문이며 본문은 파일 전체입니다.", 4, p5b)],
}


def wire(lesson, scenes):
    """Replace each listed Page's `illustrations:` block with the scenes' blocks (existing Pages 1/6 untouched)."""
    q = lambda v: json.dumps(v, ensure_ascii=False)
    md = lesson / "lesson.md"
    head, fm, body = md.read_text(encoding="utf-8").split("---\n", 2)
    lines = fm.split("\n")
    want = {f"advanced-source-09-page-{p:02d}": items for p, items in scenes.items()}
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        out.append(l)
        i += 1
        pid = l[len("- page_id: "):] if l.startswith("- page_id: ") else None
        if pid in want:
            out.append("  illustrations:")
            for stem, t, al, c, ap, _fn in want.pop(pid):
                out += [f"  - file: assets/animations/{stem}.svg", f"    title: {q(t)}", f"    alt: {q(al)}", f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
            if i < len(lines) and lines[i] == "  illustrations:":
                i += 1
                while i < len(lines) and lines[i].startswith(("  - file:", "    ")):
                    i += 1
    assert not want, list(want)
    md.write_text(head + "---\n" + "\n".join(out) + "---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    d = lesson_dir(6)
    outd = d / "assets" / "animations"
    for items in SCENES.values():
        for stem, *_r, fn in items:
            write(outd, stem, fn())
    if "--svg-only" not in sys.argv:
        wire(d, SCENES)
    print("ok", d.name)
