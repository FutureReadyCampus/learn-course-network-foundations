#!/usr/bin/env python3
"""Unit 5 Lesson 2 (subnet mask / CIDR) paired SVGs. Only the Pages listed in PAGE_FUNCS are generated;
every other Page keeps its media. Run from the repo root:
python3 scripts/svg_pairs/u5_l02.py   (add --svg-only to skip the lesson.md edit)."""
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("04-*/lessons/08-*"))
OUT = LESSON / "assets" / "animations"


# ---------- Page 2: one octet, ANDed column by column like a vertical multiplication ----------
IP, MASK = "10110101", "11110000"  # 181 AND 240 = 176
RES = "".join("1" if a == "1" and b == "1" else "0" for a, b in zip(IP, MASK))


def page2(daily):
    a = Anim(4, 15 if daily else 16)
    W, G, X0 = 64, 8, 190
    cx = lambda i: X0 + i * (W + G)
    Y1, Y2, Y3 = 150, 238, 342

    def stamp(x, y, on):
        c = x + W / 2
        if on:
            return f'<circle cx="{c}" cy="{y + 32}" r="18" fill="{ORANGE}"/><circle cx="{c}" cy="{y + 32}" r="8" fill="{BG}" fill-opacity=".35"/>'
        return f'<circle cx="{c}" cy="{y + 32}" r="18" fill="none" stroke="{LINE}" stroke-width="2" stroke-dasharray="4 4"/>'

    def top(i):  # the note / the IP octet
        x, on = cx(i), IP[i] == "1"
        if daily:
            return box(x, Y1, W, 64, ORANGE if on else LINE, PANEL, 8, sw=2) + stamp(x, Y1, on)
        return box(x, Y1, W, 64, BLUE if on else LINE, PANEL, 8, sw=2) + text(x + W / 2, Y1 + 44, IP[i], 34, BLUE if on else MUTED, 700)

    def mid(i):  # the stencil / the mask
        x, on = cx(i), MASK[i] == "1"
        if daily:
            return (box(x, Y2, W, 64, GREEN, BG, 8, dash=True, sw=3) + text(x + W / 2, Y2 + 40, "구멍", 17, GREEN, 700)) if on else \
                   (box(x, Y2, W, 64, MUTED, LINE, 8, sw=2) + text(x + W / 2, Y2 + 42, "✕", 26, BG, 700))
        return box(x, Y2, W, 64, GREEN if on else LINE, PANEL, 8, sw=2) + text(x + W / 2, Y2 + 44, MASK[i], 34, GREEN if on else MUTED, 700)

    def res(i):  # what is left
        x, on = cx(i), RES[i] == "1"
        if daily:
            return box(x, Y3, W, 64, ORANGE if on else LINE, PANEL, 8, sw=3 if on else 2) + (stamp(x, Y3, True) if on else "")
        return box(x, Y3, W, 64, GREEN if on else LINE, PANEL, 8, sw=3 if on else 2) + text(x + W / 2, Y3 + 44, RES[i], 34, GREEN if on else MUTED, 700)

    def calc(i):  # tiny "1×1" under each result column
        x = cx(i)
        return text(x + W / 2, Y3 + 88, f"{IP[i]}×{MASK[i]}", 17, TXT if RES[i] == "1" else MUTED, 700)

    lab = (("쪽지", "가림판", "보이는 것") if daily else ("IP 옥텟", "마스크", "AND 결과"))
    left = lambda y, s, c: text(X0 - 20, y + 42, s, 21, c, 700, "end")
    dec = lambda y, s, c: text(cx(7) + W + 22, y + 42, s, 20, c, 700, "start")
    rows12 = "".join(top(i) for i in range(8))
    body = [a.vis(rows12 + left(Y1, lab[0], ORANGE if daily else BLUE) + ("" if daily else dec(Y1, "= 181", BLUE)), 1, 4),
            a.vis("".join(mid(i) for i in range(8)) + left(Y2, lab[1], GREEN) + pill(60, Y2 + 32, "AND" if not daily else "겹치기", GREEN, 16, True) + ("" if daily else dec(Y2, "= 240", GREEN)), 2, 4),
            a.vis(line(X0 - 10, 326, cx(7) + W + 10, 326, TXT, 4), 3, 4)]
    for i in range(8):
        body.append(a.vis(res(i) + calc(i), 3 + i * 0.08, 4))
    body += [a.vis(left(Y3, lab[2], GREEN) + ("" if daily else dec(Y3, "= 176", GREEN)), 3.1, 4)]
    bx = cx(4) - G / 2
    body.append(a.vis(line(bx, 128, bx, 440, VIOLET, 4, "7 6")
                      + text((cx(0) + cx(3) + W) / 2, 126, "남는 쪽 (네트워크 부분)" if not daily else "남는 쪽", 19, GREEN, 700)
                      + text((cx(4) + cx(7) + W) / 2, 126, "지워지는 쪽 (호스트 부분)" if not daily else "가려지는 쪽", 19, MUTED, 700), 4, 4))
    if daily:
        t, sub = "가림판을 올려 보이는 것만 남기기", "구멍 위의 도장만 보이고, 막힌 칸은 가려져요"
        caps = ["쪽지 한 줄에 도장이 찍혀 있어요", "구멍과 막힌 칸이 있는 가림판을 올려요",
                "구멍 위에 도장이 있는 칸만 남아요", "구멍이 이어진 앞쪽만 남고 뒤쪽은 가려져요"]
    else:
        t, sub = "마스크는 8비트를 세로로 곱해요", "옥텟 하나를 예로, 한 칸씩 위아래를 AND 해요"
        caps = ["IP 주소의 옥텟 하나는 8비트예요", "마스크의 1은 남기고 0은 지워요",
                "세로 줄마다 1×1일 때만 1이에요", "1이 이어진 앞쪽이 네트워크 부분이에요"]
    return frame(a, t, sub, caps, "".join(body))


PAGE_FUNCS = {2: ("l18-daily-stencil-mask", "l18-and-mask-column", page2)}

COPY = {
    "l18-daily-stencil-mask": (
        "가림판을 올려 보이는 것만 남기기",
        "도장이 찍힌 여덟 칸의 쪽지 위에 구멍과 막힌 칸이 있는 가림판이 올라갑니다. 세로 줄마다 구멍 위에 도장이 있는 칸만 아래에 도장이 남고, 나머지는 비어 있습니다. 마지막에 구멍이 이어진 앞쪽 네 칸은 남는 쪽, 막힌 뒤쪽 네 칸은 가려지는 쪽이라고 경계선이 그어집니다.",
        "구멍(1) 위의 도장은 남고, 막힌 칸(0) 아래의 도장은 가려집니다.", -1),
    "l18-and-mask-column": (
        "마스크는 8비트를 세로로 곱해요",
        "IP 주소의 옥텟 하나 10110101(181) 아래에 마스크 11110000(240)이 놓이고, 그 아래에 줄이 그어집니다. 세로 줄마다 두 비트를 곱해 1×1일 때만 1이 되어 결과 10110000(176)이 나옵니다. 마지막에 마스크의 1이 이어진 앞쪽 네 비트는 남는 쪽(네트워크 부분), 0이 이어진 뒤쪽 네 비트는 지워지는 쪽(호스트 부분)이라고 경계선이 그어집니다.",
        "AND는 비트를 세로로 곱하는 것과 같습니다. 이 8비트와 값은 설명용 예시이고, 실제 IPv4 마스크는 32비트로 쓰며 Page 3에서 이어집니다.", 1),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    lesson_md = LESSON / "lesson.md"
    meta = yaml.safe_load(lesson_md.read_text(encoding="utf-8").split("---\n", 2)[1])
    pages = [None] * len(meta["page_metadata"])
    for n, (dn, nn, fn) in PAGE_FUNCS.items():
        write(OUT, dn, fn(True))
        write(OUT, nn, fn(False))
        old = [(Path(x["file"]).stem, x["title"], x["alt"], x["caption"], -1) for x in meta["page_metadata"][n - 1].get("animations", [])]
        d, nw = COPY[dn], COPY[nn]
        pages[n - 1] = [(dn, *d[:3], d[3])] + old + [(nn, *nw[:3], nw[3])]
        print(dn, nn)
    if "--svg-only" not in sys.argv:
        wire_items(lesson_md, pages)
