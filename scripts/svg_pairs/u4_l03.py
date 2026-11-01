#!/usr/bin/env python3
"""Unit 4 Lesson 3 paired SVGs (encapsulation / decapsulation). Run from the repo root:
python3 scripts/svg_pairs/u4_l03.py   (add --svg-only to skip the lesson.md edit)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("04-*/lessons/03-*"))
OUT = LESSON / "assets" / "animations"
DUR = {True: 15, False: 16}


# ---------- Page 1: content + label = one unit ----------
def page1(daily):
    a = Anim(4, DUR[daily])
    data = (box(480, 250, 160, 80, GREEN, PANEL, 8, sw=3)
            + text(560, 300, "책" if daily else "데이터 ‘안녕’", 26, GREEN, 700))
    head = (box(340, 250, 140, 80, ORANGE, PANEL, 8, sw=3) + text(410, 300, "송장" if daily else "헤더", 26, ORANGE, 700))
    outline = (box(326, 234, 328 + 4, 112, BLUE, "none", 14, sw=4)
               + pill(490, 218, "택배 상자" if daily else "전송 단위", BLUE, 17, True))
    arrow = (line(670, 290, 760, 290, ORANGE, 4) + f'<polygon points="760,278 784,290 760,302" fill="{ORANGE}"/>'
             + text(730, 330, "다음 방향", 18, ORANGE, 700))
    watch = line(410, 235, 410, 213, ORANGE, 3, "4 4") + eye(410, 190)
    t_head, t_out = (3, 2) if daily else (2, 3)
    body = [a.vis(data, 1, 4), a.vis(head, t_head, 4), a.vis(outline, t_out, 4),
            a.vis(watch + arrow + text(410, 372, "내용물은 열지 않아요", 20, MUTED, 700), 4, 4)]
    if daily:
        t, sub = "상자에 넣고 송장을 붙인다", "내용물은 그대로, 겉면 정보로 배달해요"
        caps = ["보낼 물건은 책 한 권이에요", "책을 상자에 넣어요", "겉면에 받는 곳 송장을 붙여요", "송장만 보고 어디로 보낼지 정해요"]
    else:
        t, sub = "캡슐화는 정보를 더해 단위로 만든다", "데이터 앞에 헤더를 붙여 하나의 단위가 돼요"
        caps = ["보낼 데이터가 있어요", "데이터 앞에 헤더를 붙여요", "헤더와 데이터가 하나의 단위가 돼요", "헤더 정보를 보고 전달 방향을 정해요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 2: unitizing, and wrapping is not encryption ----------
def page2(daily):
    a = Anim(4, DUR[daily])
    X = [240, 480, 720]
    Y = 290
    if daily:
        items = [f'<rect x="-46" y="-30" width="92" height="60" rx="4" fill="{ORANGE}"/><rect x="-6" y="-30" width="12" height="60" fill="{BG}" fill-opacity=".25"/>',
                 f'<circle cx="0" cy="-4" r="26" fill="{GREEN}"/><rect x="-3" y="20" width="6" height="22" fill="{GREEN}"/>',
                 f'<polygon points="0,-34 38,30 -38,30" fill="{BLUE}"/>']
        names, tag, unit = ["책", "꽃", "텐트"], "송장", "같은 크기의 상자"
    else:
        items = [box(-36, -18, 72, 36, GREEN, PANEL, 8, sw=3) + text(0, 8, "안녕", 20, GREEN, 700),
                 box(-50, -40, 100, 80, ORANGE, PANEL, 6, sw=3) + f'<polygon points="-44,34 -14,-6 8,18 22,2 44,34" fill="{LINE}"/>',
                 box(-60, -32, 120, 64, BLUE, PANEL, 6, sw=3) + f'<polygon points="-10,-14 18,0 -10,14" fill="{BLUE}"/>']
        names, tag, unit = ["문자", "사진", "영상"], "헤더", "같은 형식의 단위"

    def unit_box(content_i, with_tag=True):
        s = box(-80, -66, 160, 132, BLUE, PANEL, 12, sw=3) + f'<g transform="translate(0,12) scale(.8)">{items[content_i]}</g>'
        return s + (pill(0, -66, tag, ORANGE, 16, True) if with_tag else "")

    s1 = "".join(f'<g transform="translate({X[i]},{Y})">{items[i]}</g>' + text(X[i], Y + 78, names[i], 20, MUTED, 700) for i in range(3))
    s2 = "".join(f'<g transform="translate({X[i]},{Y})">{unit_box(i)}</g>' for i in range(3)) + text(480, 408, unit, 22, BLUE, 700)
    s3 = "".join(a.move(f'<g>{unit_box(i)}</g>', [(X[i] - 60, Y), (X[i] + 20, Y)], 3, 0.15, 0.65) for i in range(3))
    s3 += line(120, 380, 860, 380, LINE, 4) + text(480, 420, "한 덩어리로 다뤄요", 22, BLUE, 700)
    s4 = ("<g>" + f'<g transform="translate(400,{Y})">' + box(-80, -66, 160, 132, BLUE, PANEL, 12, sw=3)
          + f'<g transform="translate(0,12) scale(.8)">{items[1]}</g>' + pill(0, -66, tag, ORANGE, 16, True) + "</g>"
          + f'<g transform="translate(640,{Y})">{lock(0, -14, MUTED)}<path d="M-34 -42 L34 34" stroke="{RED}" stroke-width="6"/></g>'
          + text(400, 408, "내용은 그대로 보여요", 22, TXT, 700) + text(640, 408, "숨기려면 암호화가 따로 필요", 22, MUTED, 700) + "</g>")
    body = [a.vis(s1, 1, 1), a.vis(s2, 2, 2), a.vis(s3, 3, 3), a.vis(s4, 4, 4)]
    if daily:
        t, sub = "모양이 달라도 상자에 담으면 같은 단위", "포장은 다루기 쉽게 할 뿐, 내용을 숨기지는 않아요"
        caps = ["물건은 크기와 모양이 제각각이에요", "상자에 담고 송장을 붙이면 같은 단위가 돼요",
                "상자 단위로 한꺼번에 옮겨요", "포장했다고 내용물이 숨겨지진 않아요"]
    else:
        t, sub = "헤더를 붙이면 같은 형식의 단위", "캡슐화는 다루기 쉽게 할 뿐, 암호화가 아니에요"
        caps = ["데이터는 종류와 크기가 제각각이에요", "헤더를 붙이면 같은 형식의 단위가 돼요",
                "단위로 묶어서 한꺼번에 다뤄요", "캡슐화해도 내용이 숨겨지진 않아요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- shared nested-layers drawing for pages 3 and 4 ----------
# layer geometry (left, right, top, bottom) from innermost; each ring adds a 110px header strip on the left
GEO = {0: (510, 650, 290, 350), 1: (400, 662, 276, 364), 2: (290, 674, 262, 378), 3: (180, 686, 248, 392)}
COL = {0: GREEN, 1: ORANGE, 2: BLUE, 3: VIOLET}


def names(daily):
    if daily:
        return {"data": "책", "strip": ["", "송장", "송장", "송장"], "unit": ["책", "작은 상자", "중간 상자", "큰 상자"], "trailer": "봉인 테이프"}
    return {"data": "‘안녕’ 데이터", "strip": ["", "TCP 헤더", "IP 헤더", "프레임 헤더"], "unit": ["데이터", "세그먼트", "IP 패킷", "프레임"], "trailer": "FCS"}


def layer(k, daily, hl=None, pill_on=True):
    """Layer k as a ring (k>=1) or the innermost data box (k=0). hl: 'strip' | 'all' emphasises it."""
    n = names(daily)
    l, r, t, b = GEO[k]
    w = 4 if hl else 3
    if k == 0:
        s = box(l, t, r - l, b - t, GREEN, PANEL, 8, sw=w) + text((l + r) / 2, (t + b) / 2 + 9, n["data"], 20, GREEN, 700)
        return s
    s = box(l, t, r - l, b - t, COL[k], PANEL, 10, sw=3)
    s += line(l + 110, t, l + 110, b, COL[k], 2) + text(l + 55, (t + b) / 2 + 7, n["strip"][k], 18, COL[k], 700)
    if k == 3:
        s += line(r, t, r, b, COL[k], 2) + box(r, t, 100, b - t, COL[k], PANEL, 10, sw=3) + text(r + 50, (t + b) / 2 + 7, n["trailer"], 18, COL[k], 700)
    if hl:
        s += box(l - 4, t - 4, 118, b - t + 8, ORANGE, "none", 12, sw=5)
        if k == 3:
            s += box(r - 4, t - 4, 108, b - t + 8, ORANGE, "none", 12, sw=5)
    return s


def tag(k, daily):
    l, r, t, b = GEO[k]
    return pill(l + 60, t, names(daily)["unit"][k], COL[k], 16, True)


# ---------- Page 3: build the nesting from the inside out ----------
def page3(daily):
    a = Anim(4, DUR[daily])
    body = []
    for k in (3, 2, 1):  # outer first so inner rings draw on top
        body.append(a.vis(layer(k, daily) + tag(k, daily), k + 1, 4))
    body.append(a.vis(layer(0, daily), 1, 4))
    body.append(a.vis(pill(480, 215, names(daily)["unit"][0], GREEN, 20, True), 1, 1))
    for k in (1, 2, 3):
        body.append(a.vis(pill(480, 215, names(daily)["unit"][k] + " 완성", COL[k], 20, True), k + 1, k + 1))
    if daily:
        t, sub = "안쪽 상자부터 차례로 감싼다", "작은 상자 → 중간 상자 → 큰 상자, 상자마다 송장이 붙어요"
        caps = ["가장 안쪽에 책이 있어요", "작은 상자에 넣고 송장을 붙여요",
                "그 상자를 중간 상자에 넣고 송장을 붙여요", "마지막 큰 상자에는 송장과 봉인 테이프가 붙어요"]
    else:
        t, sub = "프레임 안에 패킷, 패킷 안에 세그먼트", "L4 → L3 → L2 순서로 계층마다 헤더를 붙여요"
        caps = ["보낼 데이터가 가장 안쪽에 있어요", "L4에서 TCP 헤더를 붙이면 세그먼트예요",
                "L3에서 IP 헤더를 붙이면 IP 패킷이에요", "L2에서 헤더와 FCS를 붙이면 프레임이에요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 4: peel from the outside in ----------
def page4(daily):
    a = Anim(4, DUR[daily])
    nm = names(daily)
    # outermost ring is emphasised in its own step; rings 1-2 stay plain until their step
    body = [a.vis(layer(3, daily, hl=True) + layer(2, daily) + tag(3, daily) + tag(2, daily), 1, 1),
            a.vis(layer(2, daily, hl=True) + tag(2, daily), 2, 2),
            a.vis(layer(1, daily) + tag(1, daily), 1, 1), a.vis(layer(1, daily) + tag(1, daily), 2, 2),
            a.vis(layer(1, daily, hl=True) + tag(1, daily), 3, 3),
            a.vis(layer(0, daily), 1, 3),
            a.vis(layer(0, daily, hl=True) + check(GEO[0][1] + 36, GEO[0][2] + 30), 4, 4)]
    notes = ([("큰 상자가 도착해요 — 송장과 테이프를 확인", ORANGE), ("테이프를 뜯으면 중간 상자가 나와요", BLUE),
              ("그 송장을 확인하고 작은 상자를 꺼내요", ORANGE), ("책이 받는 사람에게 전달돼요", GREEN)] if daily else
             [("프레임 도착 — 헤더와 FCS 확인", ORANGE), ("IP 헤더 확인 — 목적지 IP", BLUE),
              ("TCP 헤더 확인 — 통신 상대 찾기", ORANGE), ("데이터가 전달돼요", GREEN)])
    for i, (msg, col) in enumerate(notes, 1):
        body.append(a.vis(text(480, 442, msg, 22, col, 700), i, i))
    if daily:
        t, sub = "바깥 상자부터 차례로 푼다", "각 상자는 자기 겉면의 송장만 확인해요"
        caps = ["큰 상자의 송장과 테이프를 먼저 봐요", "겉 상자를 풀면 중간 상자가 나와요",
                "중간 상자의 송장을 확인해요", "마지막으로 책이 전달돼요"]
    else:
        t, sub = "바깥 헤더부터 처리해 안쪽을 꺼낸다", "각 계층은 자기 계층의 헤더만 읽어요"
        caps = ["L2가 프레임의 헤더와 FCS를 확인해요", "IP 패킷을 L3에 넘기면 IP 헤더를 읽어요",
                "세그먼트를 L4에 넘기면 TCP 헤더를 읽어요", "마지막으로 데이터가 전달돼요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- Page 5: same unit, different view; two directions ----------
def page5(daily):
    a = Anim(4, DUR[daily])
    nm = names(daily)
    hl, pl = ("송장", "내용물 (작은 상자)") if daily else ("IP 헤더", "페이로드 (세그먼트)")
    inner = (box(310, 220, 90, 70, BLUE, PANEL, 6, sw=3) + text(355, 262, hl, 18, BLUE, 700)
             + box(400, 220, 250, 70, GREEN, PANEL, 6, sw=3) + text(525, 262, pl, 18, GREEN, 700))
    outer = (box(180, 200, 600, 110, VIOLET, "none", 12, sw=3)
             + box(180, 200, 130, 110, VIOLET, PANEL, 12, sw=3) + text(245, 262, "큰 상자 송장" if daily else "프레임 헤더", 18, VIOLET, 700)
             + box(650, 200, 130, 110, VIOLET, PANEL, 12, sw=3) + text(715, 262, nm["trailer"], 18, VIOLET, 700))
    brace = (line(310, 186, 650, 186, GREEN, 4) + line(310, 186, 310, 198, GREEN, 4) + line(650, 186, 650, 198, GREEN, 4)
             + pill(480, 160, "큰 상자에는 전부 내용물" if daily else "L2에서는 패킷 전체가 페이로드", GREEN, 17, True))
    cmp1 = pill(480, 160, "중간 상자 눈에는 송장 + 내용물" if daily else "L3에서는 헤더 + 페이로드", BLUE, 17, True)
    chips_f = nm["unit"]
    def chips(order, col):
        out = []
        for i, k in enumerate(order):
            x = 215 + i * 190
            out.append(box(x - 75, 350, 150, 44, col, PANEL, 22, sw=3) + text(x, 380, chips_f[k], 20, col, 700))
            if i < 3:
                out.append(text(x + 95, 380, "→", 28, TXT, 700))
        return "".join(out)
    body = [a.vis(inner, 1, 4), a.vis(cmp1, 1, 1), a.vis(outer + brace, 2, 4),
            a.vis(chips([0, 1, 2, 3], BLUE) + text(480, 430, "보낼 때: 안쪽부터 감싸요", 22, BLUE, 700), 3, 3),
            a.vis(chips([3, 2, 1, 0], GREEN) + text(480, 430, "받을 때: 바깥부터 풀어요", 22, GREEN, 700), 4, 4)]
    if daily:
        t, sub = "누가 보느냐에 따라 달라지는 내용물", "중간 상자는 큰 상자 안에서는 내용물이에요"
        caps = ["중간 상자는 송장과 내용물로 이뤄져요", "큰 상자 눈에는 중간 상자 전체가 내용물이에요",
                "보낼 때는 안쪽 상자부터 감싸요", "받을 때는 바깥 상자부터 풀어요"]
    else:
        t, sub = "헤더와 페이로드는 계층에 따라 달라진다", "IP 패킷은 L3에서는 패킷, L2에서는 페이로드예요"
        caps = ["L3에서 IP 패킷은 헤더와 페이로드예요", "L2에서는 IP 패킷 전체가 프레임의 페이로드예요",
                "보낼 때: 데이터 → 세그먼트 → 패킷 → 프레임", "받을 때: 프레임 → 패킷 → 세그먼트 → 데이터"]
    return frame(a, t, sub, caps, "".join(body))


PAGES = [
    ("l13-daily-box-and-label", "l13-header-makes-unit", page1),
    ("l13-daily-unit-boxes", "l13-unit-not-encrypted", page2),
    ("l13-daily-boxes-nesting", "l13-frame-packet-segment", page3),
    ("l13-daily-unwrapping", "l13-decapsulation-order", page4),
    ("l13-daily-view-and-order", "l13-header-payload-by-layer", page5),
]

COPY = [
    (("상자에 넣고 송장을 붙인다",
      "가운데 책 한 권이 있습니다. 책이 상자에 들어가고 겉면에 송장이 붙어 하나의 택배 상자가 됩니다. 마지막에 눈 모양이 송장만 살피고 상자를 열지 않은 채 다음 방향으로 보내는 표시가 나타납니다.",
      "책을 상자에 넣고 송장을 붙이면 송장만 보고 배달할 수 있어요."),
     ("캡슐화는 정보를 더해 단위로 만든다",
      "가운데 ‘안녕’ 데이터가 있습니다. 데이터 앞에 헤더가 붙고 둘이 하나의 전송 단위로 묶입니다. 마지막에 눈 모양이 헤더만 살피고 다음 방향으로 보내는 표시가 나타납니다.",
      "캡슐화는 데이터에 헤더를 더해 하나의 전송 단위로 만드는 일이에요. 실제 네트워크의 단위는 손에 잡히는 상자가 아니라 0과 1로 된 구조입니다."), 1),
    (("모양이 달라도 상자에 담으면 같은 단위",
      "책, 꽃, 텐트처럼 모양이 다른 물건 세 개가 있습니다. 각각 송장이 붙은 같은 크기의 상자에 담기고, 상자들이 함께 한 줄로 이동합니다. 마지막에 상자 속 내용물이 그대로 보이고 자물쇠에 금지 표시가 붙어, 포장이 암호화가 아님을 보여 줍니다.",
      "포장은 다루기 쉬운 단위를 만들 뿐, 내용물을 숨기지는 않아요."),
     ("헤더를 붙이면 같은 형식의 단위",
      "문자, 사진, 영상처럼 종류가 다른 데이터 세 개가 있습니다. 각각 헤더가 붙은 같은 형식의 단위로 묶이고 함께 한 줄로 이동합니다. 마지막에 내용이 그대로 보이고 자물쇠에 금지 표시가 붙어, 캡슐화가 암호화가 아님을 보여 줍니다.",
      "캡슐화 자체는 내용을 숨기지 않아요. 보호하려면 암호화 같은 별도 기능이 필요합니다."), 2),
    (("안쪽 상자부터 차례로 감싼다",
      "가운데 책에서 시작해 작은 상자, 중간 상자, 큰 상자가 차례로 바깥을 감쌉니다. 상자마다 송장이 붙고, 가장 바깥 큰 상자에는 봉인 테이프도 붙습니다.",
      "안쪽부터 바깥으로 감싸고, 한 겹이 끝날 때마다 하나의 상자가 완성돼요."),
     ("프레임 안에 패킷, 패킷 안에 세그먼트",
      "가운데 ‘안녕’ 데이터에서 시작해 TCP 헤더가 붙은 세그먼트, IP 헤더가 붙은 IP 패킷, 프레임 헤더와 FCS가 붙은 프레임이 차례로 바깥을 감쌉니다.",
      "L4에서 세그먼트, L3에서 IP 패킷, L2에서 프레임이 완성됩니다. 실제 필드와 크기는 프로토콜마다 달라요."), 2),
    (("바깥 상자부터 차례로 푼다",
      "큰 상자가 도착해 송장과 봉인 테이프가 확인됩니다. 큰 상자가 사라지고 중간 상자의 송장이 확인되고, 다시 작은 상자의 송장이 확인된 뒤 책만 남아 전달됩니다.",
      "받는 쪽은 바깥 상자부터 풀고, 상자마다 자기 겉면의 송장만 확인해요."),
     ("바깥 헤더부터 처리해 안쪽을 꺼낸다",
      "프레임이 도착해 헤더와 FCS가 확인됩니다. 프레임이 벗겨지고 IP 헤더가 확인되고, 이어 세그먼트의 TCP 헤더가 확인된 뒤 데이터만 남아 전달됩니다.",
      "각 계층은 자기 계층의 헤더만 읽고 안쪽 단위를 다음 계층에 넘겨요."), 3),
    (("누가 보느냐에 따라 달라지는 내용물",
      "송장과 내용물로 이뤄진 중간 상자가 보입니다. 큰 상자의 송장과 봉인 테이프가 둘러싸면 중간 상자 전체가 큰 상자의 내용물이 됩니다. 이어 책에서 큰 상자까지 감싸는 순서와, 큰 상자에서 책까지 푸는 순서가 차례로 나타납니다.",
      "같은 상자도 보는 쪽에 따라 송장이 붙은 단위이거나 다른 상자의 내용물이 됩니다."),
     ("헤더와 페이로드는 계층에 따라 달라진다",
      "IP 헤더와 페이로드로 이뤄진 IP 패킷이 보입니다. 프레임 헤더와 FCS가 둘러싸면 IP 패킷 전체가 프레임의 페이로드가 됩니다. 이어 보낼 때는 데이터, 세그먼트, 패킷, 프레임 순서로, 받을 때는 그 반대 순서로 처리한다고 나타납니다.",
      "IP 패킷은 L3에서는 헤더와 페이로드를 가진 패킷이고, L2 프레임 안에서는 페이로드예요."), 2),
]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for (dn, nn, fn), (d, n, after) in zip(PAGES, COPY):
        write(OUT, dn, fn(True))
        write(OUT, nn, fn(False))
        rows.append((dn, *d, nn, *n, after))
        print(dn, nn)
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md", rows)
