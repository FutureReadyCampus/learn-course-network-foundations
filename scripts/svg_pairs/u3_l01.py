#!/usr/bin/env python3
"""Unit 3 Lesson 1 (택배로 훑어보는 OSI 7계층): one light SVG per Page (9). Run from the repo root:
python3 scripts/svg_pairs/u3_l01.py   (add --svg-only to skip the lesson.md edit).

Every SVG shows the 7-layer stack on the left; a parcel token comes in from the layer above, the layer's job is
shown as a 택배 scene, the parcel is handed to the layer below, and on the receiving side it climbs back up."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, person, dur  # reuse local helpers
from u7_l01 import mv

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("03-layer2-switching/lessons/01-*"))
OUT = LESSON / "assets" / "animations"

LAYERS = [(7, "응용", BLUE), (6, "표현", VIOLET), (5, "세션", GREEN), (4, "전송", ORANGE), (3, "네트워크", BLUE), (2, "데이터 링크", GREEN), (1, "물리", MUTED)]
ROW0, PITCH = 150, 46  # y of the first row, pitch


def ry(n):  # y center of layer n
    return ROW0 + (7 - n) * PITCH


def stack(current=None, dim=True):
    out = ""
    for n, name, c in LAYERS:
        y = ry(n)
        if n == current:
            out += box(40, y - 19, 250, 38, c, c, 8, sw=3) + text(165, y + 7, f"{n} {name}", 19, BG, 700)
        else:
            out += box(40, y - 19, 250, 38, LINE, PANEL, 8, sw=2) + text(165, y + 7, f"{n} {name}", 18, MUTED if dim else TXT, 600)
    return out


def token(inner_color=ORANGE):
    return f'<rect x="-14" y="-12" width="28" height="24" rx="3" fill="{inner_color}"/><rect x="-3" y="-12" width="6" height="24" fill="{BG}" fill-opacity="0.25"/>'


def down_up(a, n, scene_steps=(2, 4)):
    """token arrives from above (step 1), sits on the layer (step 2), moves below (step 3), receiver climbs up (step 4)."""
    y = ry(n)
    above = y - PITCH if n < 7 else y - 36
    below = y + PITCH if n > 1 else y + 36
    parts = [mv(a, token(), [(318, above), (318, y)], 1, 1, 1, 0.1, 0.8),
             a.vis(f'<g transform="translate(318,{y})">{token()}</g>', 2, 2),
             mv(a, token(), [(318, y), (318, below)], 3, 3, 3, 0.1, 0.8),
             a.vis(arrow_up(318, ROW0 + 6 * PITCH + 22, ROW0 - 26, GREEN) + text(318, ROW0 + 6 * PITCH + 66, "받는 쪽", 13, GREEN, 700), 4, 4)]
    return "".join(parts)


def arrow_up(x, y0, y1, c):
    return line(x, y0, x, y1 + 14, c, 5) + f'<polygon points="{x},{y1} {x - 9},{y1 + 16} {x + 9},{y1 + 16}" fill="{c}"/>'


def hl_row(n, c):
    return hl(40, ry(n) - 19, 250, 38, c, 8)


# --------------------------------------------------------------------------------------- scenes
def scene7():
    return (person(450, 290, "보내는 사람") + pill(640, 215, "“이 책 한 권 보내 주세요”", BLUE, 19, True, 330) + parcel(600, 300)
            + pill(700, 372, "웹 페이지 요청 · 이름 주소 묻기", MUTED, 15, False, 330) + text(630, 440, "택배 앱이나 배달원 자체는 아니에요", 16, MUTED))


def scene6():
    doc = box(380, 210, 150, 120, VIOLET, PANEL, 10, sw=3) + text(455, 255, "안녕하세요", 19, TXT, 600) + text(455, 290, "Hello", 19, TXT, 600)
    env = box(650, 225, 140, 90, GREEN, PANEL, 10, sw=3) + lock(720, 245, GREEN) + text(720, 335, "봉투로 보호", 15, MUTED)
    return (doc + arrow(535, 645, 270, MUTED, 4) + env + text(455, 365, "서로 읽을 수 있는 형식", 17, VIOLET, 700) + text(720, 365, "필요하면 압축·암호화", 17, GREEN, 700)
            + text(630, 440, "별도의 한 계층에서만 일어나는 일은 아니에요", 16, MUTED))


def scene5():
    ps = [("배송 시작합니다", "시작"), ("지금 이동 중이에요", "이어 감"), ("배송 완료했어요", "마침")]
    out = ""
    for i, (t, tag) in enumerate(ps):
        x = 450 + i * 190
        out += pill(x, 270, t, GREEN, 16, True if i == 1 else False, 175) + text(x, 315, tag, 17, GREEN, 700)
        if i < 2:
            out += arrow(x + 90, x + 100, 270, MUTED, 3)
    return out + text(630, 200, "배송 알림 · 문의처럼 오가는 대화", 18, TXT, 700) + text(630, 440, "택배에 딱 맞는 담당자는 없어요", 16, MUTED)


def scene4():
    apps = ["브라우저", "게임", "메신저"]
    comp = box(640, 190, 250, 200, ORANGE, PANEL, 12, sw=3) + text(765, 220, "받는 컴퓨터", 17, ORANGE, 700)
    comp += "".join(cell(665, 238 + i * 48, 200, 38, t, ORANGE if i == 1 else LINE, 16, PANEL) for i, t in enumerate(apps))
    return (house(440, 300, "보내는 사람") + parcel(510, 290) + arrow(545, 636, 336, ORANGE, 4) + comp + hl(665, 286, 200, 38, GREEN, 8)
            + text(630, 440, "장치까지는 3계층, 그 안의 프로그램까지는 4계층이에요", 16, MUTED))


def scene3():
    hubs = [(470, 255), (640, 345), (810, 255), (810, 395)]
    out = line(470, 255, 640, 345, LINE, 3) + line(640, 345, 810, 255, LINE, 3) + line(640, 345, 810, 395, LINE, 3)
    out += line(470, 255, 640, 345, ORANGE, 6) + line(640, 345, 810, 395, ORANGE, 6)
    on = {(470, 255), (640, 345), (810, 395)}
    out += "".join(box(x - 28, y - 22, 56, 44, ORANGE if (x, y) in on else LINE, PANEL, 8, sw=3) for x, y in hubs)
    return out + text(470, 212, "출발", 15, MUTED, 700) + text(810, 445, "목적지", 15, ORANGE, 700) + text(560, 455, "주소를 읽고 지역과 경로를 골라요", 17, TXT, 700)


def scene2():
    return (laptop(470, 300, "노트북") + router(640, 300, "공유기") + house(850, 300, "목적지") + line(520, 300, 612, 300, GREEN, 8) + line(672, 300, 800, 300, LINE, 3, "8 6")
            + parcel(566, 270) + text(566, 215, "지금 이어진 한 구간", 17, GREEN, 700) + text(630, 440, "최종 목적지까지의 전체 경로와는 범위가 달라요", 16, MUTED))


def scene1():
    lanes = [("구리선", 215, ORANGE), ("광섬유", 290, BLUE), ("무선(공기)", 365, GREEN)]
    out = ""
    for t, y, c in lanes:
        out += line(420, y, 900, y, LINE, 10) + text(380, y + 6, t, 16, c, 700, "end") + packet(660, y, c)
    return out + text(660, 175, "비트를 전기·빛·전파 신호로", 18, TXT, 700) + text(630, 440, "도로와 차량처럼 이동의 바탕이에요", 16, MUTED)


SCENES = {7: scene7, 6: scene6, 5: scene5, 4: scene4, 3: scene3, 2: scene2, 1: scene1}
INFO = {
    7: ("응용 계층: 무엇을 보낼까", "프로그램이 주고받을 일을 정해요", "응용은 프로그램이 주고받을 일을 다룹니다.",
        ["위에서 사용자의 부탁이 내려와요", "택배 장면: 무엇을 보낼지 부탁을 정해요", "정한 부탁을 아래 표현 계층으로 넘겨요", "받는 쪽에서는 아래에서 위로 올라와 프로그램에 닿아요"]),
    6: ("표현 계층: 어떤 형식일까", "서로 읽을 수 있게 맞춰요", "표현은 데이터를 어떤 형식으로 읽을지 다룹니다.",
        ["위 응용 계층에서 내용이 내려와요", "택배 장면: 문서를 읽을 수 있는 형식과 봉투로 맞춰요", "맞춘 데이터를 아래 세션 계층으로 넘겨요", "받는 쪽에서는 아래에서 올라와 형식을 풀어요"]),
    5: ("세션 계층: 대화를 이어 가요", "시작하고, 이어 가고, 마쳐요", "세션은 통신 대화의 시작·유지·마무리를 다룹니다.",
        ["위 표현 계층에서 데이터가 내려와요", "택배 장면: 배송 알림처럼 대화가 시작되고 이어지고 끝나요", "대화 흐름과 함께 아래 전송 계층으로 넘겨요", "받는 쪽에서도 아래에서 위로 이어져요"]),
    4: ("전송 계층: 어느 프로그램까지", "끝에 있는 프로그램 사이의 전달이에요", "전송은 끝에 있는 프로그램 사이의 전달입니다.",
        ["위 세션 계층에서 데이터가 내려와요", "택배 장면: 보내는 사람에서 받는 사람 쪽 프로그램까지 맡아요", "아래 네트워크 계층에 목적지로 보내 달라고 넘겨요", "받는 쪽에서는 아래에서 올라와 알맞은 프로그램에 전해요"]),
    3: ("네트워크 계층: 어느 네트워크로", "주소를 보고 경로를 골라요", "네트워크는 목적지와 경로를 찾습니다.",
        ["위 전송 계층에서 데이터가 내려와요", "택배 장면: 주소를 읽고 지역과 분류 경로를 골라요", "다음 구간 전달을 아래 데이터 링크 계층에 맡겨요", "받는 쪽에서는 아래에서 올라와 목적지를 확인해요"]),
    2: ("데이터 링크: 다음 이웃에게", "지금 이어진 한 구간만 맡아요", "데이터 링크는 이웃 사이 한 구간을 잇습니다.",
        ["위 네트워크 계층에서 다음 구간 전달이 내려와요", "택배 장면: 상자를 가까운 다음 담당자에게 넘겨요", "프레임을 실어 보낼 신호는 아래 물리 계층에 맡겨요", "받는 쪽에서는 아래에서 올라와 이웃의 프레임을 받아요"]),
    1: ("물리 계층: 신호로 실어 보내요", "비트를 실제 신호와 매체로 보내요", "물리는 비트를 실제 신호로 보냅니다.",
        ["위 데이터 링크 계층에서 비트가 내려와요", "택배 장면: 도로와 차량처럼 실제 이동 수단이 돼요", "신호는 케이블·광섬유·공기를 타고 상대에게 가요", "받는 쪽에서는 이 신호가 위 계층으로 올라가는 출발점이에요"]),
}


def layer_page(n):
    title, sub, mem, caps = INFO[n]
    a = Anim(4, dur(True))
    c = dict((k, col) for k, _, col in LAYERS)[n]
    body = [stack(n), down_up(a, n)]
    if n < 7:
        body.append(a.vis(hl_row(n + 1, MUTED), 1, 1))
    if n > 1:
        body.append(a.vis(hl_row(n - 1, MUTED), 3, 3))
    body += [a.vis(SCENES[n](), 2, 4), a.vis(pill(630, 155, mem, c, 16, True, 520), 4, 4)]
    return frame(a, title, sub, caps, "".join(body))


# --------------------------------------------------------------------------------------- page 1 and 9
def page1():
    a = Anim(4, dur(True))
    words = {7: "무엇을 보낼지 (물건·부탁)", 6: "알아볼 수 있는 포장", 5: "배송 중 오가는 안내", 4: "보내는 사람 → 받는 사람", 3: "목적지 주소와 분류", 2: "가까운 구간 인계", 1: "실제 이동 수단 (도로·차량)"}
    groups = [(7, 5, 1), (4, 3, 2), (2, 1, 3)]
    body = [stack(None, False)]
    for hi, lo, step in groups:
        chips = "".join(arrow(296, 330, ry(n), MUTED, 3) + text(344, ry(n) + 7, words[n], 17, TXT, 700, "start") for n in range(hi, lo - 1, -1))
        body.append(a.vis(chips, step, 4))
    body += [mv(a, token(), [(318, ROW0 - 36), (318, ry(5))], 1, 1, 1, 0.1, 0.9), mv(a, token(), [(318, ry(5)), (318, ry(2) - 6)], 2, 2, 2, 0.1, 0.9),
             mv(a, token(), [(318, ry(2)), (318, ry(1) + 36)], 3, 3, 3, 0.1, 0.9),
             a.vis(arrow_up(318, ry(1) + 22, ROW0 - 26, GREEN) + pill(640, 480 - 22, "받는 쪽에서는 아래에서 위로 올라와요", GREEN, 17, True, 430), 4, 4)]
    caps = ["위쪽 세 역할: 무엇을 보낼지, 포장, 안내", "가운데 두 역할: 보내는 사람 → 받는 사람, 주소와 분류", "아래쪽 두 역할: 가까운 구간 인계, 실제 이동 수단", "받는 쪽에서는 같은 일곱 역할이 아래에서 위로 올라와요"]
    return frame(a, "택배 여정을 일곱 역할로", "위에서 아래로 내려가고, 받는 쪽에서는 올라와요", caps, "".join(body))


def page9():
    a = Anim(4, dur(True))
    grp = [("응·표·세", 7, 5, BLUE, "프로그램에 가까운 쪽"), ("전·네", 4, 3, ORANGE, "끝에서 끝까지, 목적지까지"), ("데·물", 2, 1, GREEN, "가까운 구간과 신호")]
    body = [stack(None, False)]
    for k, (t, hi, lo, c, d) in enumerate(grp, 1):
        y0, y1 = ry(hi) - 22, ry(lo) + 22
        body.append(a.vis(box(32, y0, 266, y1 - y0, c, "none", 10, sw=4) + text(620, (y0 + y1) / 2 - 4, t, 40, c, 700) + text(620, (y0 + y1) / 2 + 36, d, 20, MUTED, 700), k, k))
    body.append(a.vis(arrow_up(330, ry(1) + 22, ROW0 - 26, GREEN) + line(350, ROW0 - 20, 350, ry(1) + 6, ORANGE, 5)
                      + f'<polygon points="350,{ry(1) + 22} 341,{ry(1) + 6} 359,{ry(1) + 6}" fill="{ORANGE}"/>'
                      + text(450, 300, "보내는 쪽 ↓", 20, ORANGE, 700, "start") + text(450, 340, "받는 쪽 ↑", 20, GREEN, 700, "start")
                      + pill(640, 458, "택배는 기억을 돕는 장면일 뿐이에요", MUTED, 16, False, 380), 4, 4))
    caps = ["위쪽 세 계층: 응용·표현·세션", "가운데 두 계층: 전송·네트워크", "아래쪽 두 계층: 데이터 링크·물리", "보내는 쪽은 위에서 아래로, 받는 쪽은 아래에서 위로예요"]
    return frame(a, "응·표·세 / 전·네 / 데·물", "위에서 아래로 한 번 더 읽어 봐요", caps, "".join(body))


PAGES = [
    ("u3l01-osi-p1-parcel-seven-roles", "택배 여정을 일곱 역할로", "위에서 아래로 응용, 표현, 세션, 전송, 네트워크, 데이터 링크, 물리가 쌓여 있고 각 줄 옆에 무엇을 보낼지, 포장, 배송 안내, 보내는 사람에서 받는 사람, 주소와 분류, 가까운 구간 인계, 실제 이동 수단이 나타납니다. 택배 상자가 위에서 아래로 내려가고 받는 쪽에서는 아래에서 위로 올라옵니다.",
     "택배 장면은 낯선 역할을 기억하기 위한 비유이며, 택배와 네트워크가 일곱 부서로 똑같이 움직인다는 뜻은 아닙니다.", 1, page1),
    ("u3l01-osi-p2-application", "응용 계층: 무엇을 보낼까", "7계층이 강조된 계층 목록에서 위에서 내려온 택배 상자가 응용 계층에 머물고, 보내는 사람이 “이 책 한 권 보내 주세요”라고 부탁하는 장면과 웹 페이지 요청, 이름 주소 묻기 예시가 나옵니다. 상자는 아래 표현 계층으로 넘어가고 받는 쪽에서는 위로 올라옵니다.",
     "응용 계층은 프로그램이 주고받을 일을 다룹니다. 택배 앱이나 배달원 자체를 뜻하지는 않습니다.", 1, lambda: layer_page(7)),
    ("u3l01-osi-p3-presentation", "표현 계층: 어떤 형식일까", "6계층이 강조된 계층 목록에서 택배 상자가 표현 계층에 머물고, 안녕하세요와 Hello 문서가 읽을 수 있는 형식으로 맞춰지고 필요하면 압축이나 암호화가 되는 봉투 장면이 나옵니다. 상자는 아래 세션 계층으로 넘어갑니다.",
     "표현 계층은 데이터의 형식과 필요한 변환을 다룹니다. 실제 변환이나 암호화가 항상 별도의 한 계층에서만 일어나는 것은 아닙니다.", 1, lambda: layer_page(6)),
    ("u3l01-osi-p4-session", "세션 계층: 대화를 이어 가요", "5계층이 강조된 계층 목록에서 택배 상자가 세션 계층에 머물고, 배송 시작, 이동 중, 배송 완료 알림처럼 대화가 시작되고 이어지고 마치는 장면이 나옵니다. 택배에 딱 맞는 담당자는 없다고 표시됩니다.",
     "세션 계층은 통신 대화의 시작, 유지, 마무리를 다룹니다. 택배에는 정확히 같은 담당자가 없고 대화 흐름을 붙잡는 비유일 뿐입니다.", 1, lambda: layer_page(5)),
    ("u3l01-osi-p5-transport", "전송 계층: 어느 프로그램까지", "4계층이 강조된 계층 목록에서 택배 상자가 전송 계층에 머물고, 보내는 사람의 상자가 받는 컴퓨터 안의 브라우저, 게임, 메신저 중 알맞은 프로그램에 닿는 장면이 나옵니다.",
     "전송 계층은 통신 양 끝의 프로그램 사이에서 데이터를 전달합니다. 장치까지는 3계층, 그 안의 프로그램까지는 4계층입니다.", 1, lambda: layer_page(4)),
    ("u3l01-osi-p6-network", "네트워크 계층: 어느 네트워크로", "3계층이 강조된 계층 목록에서 택배 상자가 네트워크 계층에 머물고, 주소를 읽고 여러 지역 가운데 출발에서 목적지까지의 분류 경로를 고르는 장면이 나옵니다.",
     "네트워크 계층은 IP 주소를 바탕으로 목적지 네트워크까지의 경로를 찾습니다. 한 구간 전달을 맡는 데이터 링크 계층과 범위가 다릅니다.", 1, lambda: layer_page(3)),
    ("u3l01-osi-p7-data-link", "데이터 링크: 다음 이웃에게", "2계층이 강조된 계층 목록에서 택배 상자가 데이터 링크 계층에 머물고, 노트북에서 공유기로 건네는 한 구간이 강조되고 그 뒤 목적지까지는 점선으로 표시됩니다.",
     "데이터 링크 계층은 같은 네트워크 구간에서 이웃한 장치 사이로 프레임을 전달합니다. 최종 목적지까지의 전체 경로와는 범위가 다릅니다.", 1, lambda: layer_page(2)),
    ("u3l01-osi-p8-physical", "물리 계층: 신호로 실어 보내요", "1계층이 강조된 계층 목록에서 택배 상자가 물리 계층에 머물고, 구리선, 광섬유, 무선 세 길 위에서 비트가 전기, 빛, 전파 신호로 실려 가는 장면이 나옵니다.",
     "물리 계층은 비트를 전기, 빛, 무선 신호로 바꾸어 케이블, 광섬유, 공기를 통해 전달합니다.", 1, lambda: layer_page(1)),
    ("u3l01-osi-p9-order-recap", "응·표·세 / 전·네 / 데·물", "일곱 계층이 응·표·세, 전·네, 데·물 세 묶음으로 차례로 강조되고, 보내는 쪽은 위에서 아래로 받는 쪽은 아래에서 위로 읽는 화살표가 나옵니다. 택배는 기억을 돕는 장면일 뿐이라고 표시됩니다.",
     "응용, 표현, 세션, 전송, 네트워크, 데이터 링크, 물리를 위에서 아래로 끊어 읽으면 기억하기 쉽습니다. 택배 비유는 실제 네트워크와 일대일로 대응하지 않습니다.", 0, page9),
]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    head, fm, body = Path(lesson_md).read_text(encoding="utf-8").split("---\n", 2)
    lines = fm.split("\n")
    pm_start = lines.index("page_metadata:")
    starts = [i for i, l in enumerate(lines) if i > pm_start and l.startswith("- terms:")]
    assert len(starts) == len(PAGES), len(starts)
    end_fm = next(i for i, l in enumerate(lines) if i > starts[-1] and l and not l.startswith((" ", "- ")))
    bounds = starts + [end_fm]
    ours = {f"assets/animations/{p[0]}.svg" for p in PAGES}
    out = lines[:starts[0]]
    for i, (f, t, al, c, ap, _) in enumerate(PAGES):
        seg = lines[bounds[i]:bounds[i + 1]]
        kept, k = [], 0
        while k < len(seg):  # drop earlier generated illustrations / our position list
            if seg[k] == "  illustrations:" or seg[k].startswith("  illustration_after_paragraph:"):
                k += 1
                while k < len(seg) and (seg[k].startswith("  - file:") or seg[k].startswith("    ")):
                    k += 1
                continue
            kept.append(seg[k]); k += 1
        while kept and kept[-1] == "":
            kept.pop()
        kept += ["  illustrations:", f"  - file: assets/animations/{f}.svg", f"    title: {q(t)}", f"    alt: {q(al)}", f"    caption: {q(c)}", f"    after_paragraph: {ap}"]
        if i == 0:  # existing stack animation sits right before ours, where the text says "아래 그림"
            kept.append("  illustration_after_paragraph: [1]")
        out += kept
    out += lines[end_fm:]
    text_ = "\n".join(out)
    if not text_.endswith("\n"):
        text_ += "\n"
    Path(lesson_md).write_text(head + "---\n" + text_ + "---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f, *_rest, fn in PAGES:
        write(OUT, f, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
    print("ok", len(PAGES), "svgs")
