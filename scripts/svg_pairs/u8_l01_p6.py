#!/usr/bin/env python3
"""Unit 8 Lesson 1, Page 6 (송수신 구조와 장애 원인 정리): extra SVGs. Run from the repo root:
python3 scripts/svg_pairs/u8_l01_p6.py   (add --svg-only to skip the lesson.md edit).

Adds 4 SVGs to the existing daily/network pair and re-places all six along the page text:
  after para 0 : l16-daily-tracking-marks (existing), l16-recap-path-with-marks (new)
  after para 1 : l16-capture-marks-questions (existing, next to the table), l16-daily-tracking-log-read (new)
  after para 2 : l16-capture-walkthrough (new), l16-one-mark-many-causes (new)"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import cell, hl, arrow, brace, person, dur  # reuse local helpers
from u7_l01 import mv
from u7_l02 import end
from u10_l01 import at, role, lanes, msg

ROOT = Path(__file__).resolve().parents[2]
LESSON = next((ROOT / "units").glob("08-tcp-udp-details/lessons/01-*"))
OUT = LESSON / "assets" / "animations"
PAGE_INDEX = 5  # Page 6


# ---------- recap: where each capture mark shows up on the sender -> receiver path ----------
def recap(n=4):
    a = Anim(n, dur(False, n))
    names = [("송신 프로그램", "송신 버퍼"), ("송신 TCP", "세그먼트·순서 번호"), ("네트워크 경로", "IP 패킷·프레임"), ("수신 TCP", "ACK·수신 윈도"), ("수신 버퍼", "프로그램이 읽어요")]
    cols = [BLUE, GREEN, MUTED, GREEN, ORANGE]
    xs = [30, 214, 398, 582, 766]
    chain = "".join(role(x, 190, 164, 84, t, s, c, 17) for x, (t, s), c in zip(xs, names, cols))
    chain += "".join(arrow(x + 166, x + 212, 232, MUTED, 3) for x in xs[:-1])
    tags = [("Unit 4", 0), ("Unit 7", 1), ("Unit 5·6", 2), ("Unit 8", 3), ("Unit 4", 4)]
    tg = "".join(text(xs[i] + 82, 178, t, 14, MUTED, 700) for t, i in tags)
    mk = lambda x, y, s, c: pill(x, y, s, c, 16, True, 150)
    body = [chain, tg,
            a.vis(text(480, 330, "앞에서 배운 길 위에 캡처 표식을 하나씩 놓아 봐요", 18, MUTED, 700), 1, 1),
            a.vis(mk(xs[1] + 82, 330, "재전송", ORANGE) + mk(xs[2] + 82, 330, "손실 세그먼트", RED)
                  + line(xs[1] + 82, 276, xs[1] + 82, 312, ORANGE, 3) + line(xs[2] + 82, 276, xs[2] + 82, 312, RED, 3), 2, 4),
            a.vis(mk(xs[3] + 82, 330, "순서 어긋남", BLUE) + mk(xs[3] + 82, 385, "중복 ACK", VIOLET)
                  + line(xs[3] + 82, 276, xs[3] + 82, 312, BLUE, 3), 3, 4),
            a.vis(mk(xs[4] + 82, 330, "제로 윈도", GREEN) + line(xs[4] + 82, 276, xs[4] + 82, 312, GREEN, 3)
                  + pill(480, 448, "표식은 길 위에서 어디를 살펴볼지 짚어 주는 단서예요", ORANGE, 17, True), 4, 4)]
    t, sub = "송수신 길 위에 캡처 표식 놓기", "표식마다 살펴볼 곳이 달라요"
    caps = ["Unit 4부터 이어 온 송신에서 수신까지의 길이에요", "재전송과 손실 세그먼트는 보낸 뒤 확인 단계에서 보여요", "순서 어긋남과 중복 ACK는 받는 쪽 TCP 근처에서 보여요", "제로 윈도는 수신 버퍼가 가득 찼다고 알릴 때 보여요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- reading a capture row by row ----------
def walkthrough(daily):
    a = Anim(4, dur(daily))
    cols = [BLUE, ORANGE, GREEN, VIOLET]
    rows = ([("1", "상자 → 받는 곳", "2번 상자가 먼저 도착", "순서 뒤바뀜", BLUE, "도착 순서와 번호 순서가 어디서 달라졌나?"),
             ("2", "받는 곳 → 보내는 곳", "“1번 주세요”", "같은 소식 반복", VIOLET, "받는 사람은 다음에 어떤 상자를 기다리나?"),
             ("3", "상자 → 받는 곳", "1번 상자가 다시 도착", "다시 배송", ORANGE, "같은 상자 번호를 다시 보냈나?"),
             ("4", "받는 곳 → 보내는 곳", "“3번 주세요”", "정상 확인", GREEN, "어느 상자까지 확인됐나?")] if daily else
            [("1", "송신 → 수신", "Seq 1501~2000", "Out of order", BLUE, "도착 순서와 바이트 순서가 어디서 달라졌나?"),
             ("2", "수신 → 송신", "ACK 1001", "Duplicate ACK", VIOLET, "수신 측은 다음에 어떤 바이트를 기다리나?"),
             ("3", "송신 → 수신", "Seq 1001~1500", "Retransmission", ORANGE, "같은 순서 번호 범위가 다시 전송됐나?"),
             ("4", "수신 → 송신", "ACK 2001", "정상 확인", GREEN, "어디까지 확인됐나?")])
    head = (text(60, 150, "번호", 15, MUTED, 700, "start") + text(120, 150, "방향", 15, MUTED, 700, "start") + text(330, 150, "내용", 15, MUTED, 700, "start") + text(520, 150, "표식", 15, MUTED, 700, "start"))
    body = [head, line(40, 160, 920, 160, LINE, 2)]
    for k, (no, d, c_, mark, c, q) in enumerate(rows, 1):
        y = 200 + (k - 1) * 62
        r = box(40, y - 26, 880, 52, c, PANEL, 8, sw=2) + text(62, y + 7, no, 20, c, 700, "start") + text(120, y + 6, d, 16, TXT, 600, "start") + text(330, y + 6, c_, 17, TXT, 700, "start") + pill(590, y, mark, c, 15, True, 150)
        body.append(a.vis(r, k, 4))
        body.append(a.vis(hl(40, y - 26, 880, 52, c, 8) + text(480, 462, "먼저 확인할 질문: " + q, 18, c, 700), k, k))
    if daily:
        t, sub = "배송 기록표를 한 줄씩 읽어요", "표식을 보고 먼저 물을 질문을 골라요"
        caps = ["2번 상자가 먼저 왔다면 도착 순서가 어디서 달라졌는지 봐요", "“1번 주세요”가 반복되면 받는 사람이 기다리는 상자를 봐요", "1번 상자가 다시 왔다면 같은 번호를 다시 보낸 거예요", "“3번 주세요”로 어디까지 확인됐는지 알 수 있어요"]
    else:
        t, sub = "캡처 목록을 한 줄씩 읽어요", "번호는 설명을 위한 예시예요"
        caps = ["Out of order: 도착 순서와 바이트 순서가 달라졌어요", "중복 ACK: 수신 측이 기다리는 바이트를 알려 줘요", "재전송: 같은 순서 번호 범위가 다시 갔어요", "ACK 2001: 2000까지 확인됐다는 뜻이에요"]
    return frame(a, t, sub, caps, "".join(body))


# ---------- one mark, several possible causes ----------
def many_causes():
    a = Anim(4, dur(False))
    colx = [40, 340, 640]
    spec = [("재전송", ORANGE, ["데이터가 도중에 사라짐", "데이터는 갔고 ACK가 늦음"], "캡처 위치와 지연도 함께 봐요"),
            ("제로 윈도", GREEN, ["수신 프로그램이 늦게 읽음", "연결 종료나 인터넷 정지는 아님"], "읽는 속도와 버퍼 상태를 봐요"),
            ("중복 ACK", VIOLET, ["빠진 구간이 있을 수 있음", "앞 구간이 차면 이어서 받음"], "순서 번호와 도착 순서를 비교해요")]
    body = []
    for k, ((m, c, causes, check), x) in enumerate(zip(spec, colx), 1):
        inner = box(x, 135, 280, 285, c, PANEL, 12, sw=3) + pill(x + 140, 172, m, c, 19, True, 190) + text(x + 140, 218, "가능한 이유", 16, MUTED, 700)
        for i, s in enumerate(causes):
            inner += text(x + 140, 260 + i * 44, "· " + s, 16, TXT)
        inner += line(x + 20, 352, x + 260, 352, LINE, 2) + text(x + 140, 378, "함께 볼 것", 15, MUTED, 700) + text(x + 140, 402, check, 15, c, 700)
        body.append(a.vis(inner, k, 4))
    body.append(a.vis(pill(480, 452, "표식 하나만으로 경로 문제인지 애플리케이션 문제인지 단정하지 않아요", RED, 17, True), 4, 4))
    caps = ["재전송은 데이터가 사라졌을 때도, ACK가 늦었을 때도 보일 수 있어요", "제로 윈도는 수신 프로그램이 읽는 속도와 버퍼 상태를 살펴보라는 신호예요", "중복 ACK는 빠진 구간이 있을 가능성을 알려 주는 단서예요", "표식 하나로 원인을 정하지 말고 주변 상황과 함께 살펴요"]
    return frame(a, "표식 하나, 가능한 이유는 여럿", "원인을 단정하기 전에 주변 자료를 함께 봐요", caps, "".join(body))


NEW = [
    ("l16-recap-path-with-marks", "송수신 길 위에 캡처 표식 놓기",
     "송신 프로그램, 송신 TCP, 네트워크 경로, 수신 TCP, 수신 버퍼가 한 줄로 있고, 재전송과 손실 세그먼트, 순서 어긋남과 중복 ACK, 제로 윈도 표식이 각각 어디를 살펴보라는 단서인지 차례로 놓입니다.",
     "표식은 앞에서 배운 길 위에서 어디를 살펴볼지 짚어 주는 단서입니다.", lambda: recap()),
    ("l16-daily-tracking-log-read", "배송 기록표를 한 줄씩 읽어요",
     "배송 기록표의 네 줄이 차례로 강조됩니다. 2번 상자가 먼저 도착, “1번 주세요” 반복, 1번 상자 재도착, “3번 주세요” 확인이며 줄마다 먼저 확인할 질문이 나옵니다.",
     "기록표의 표식을 보고 먼저 물을 질문을 고릅니다. 상자 번호는 예시입니다.", lambda: walkthrough(True)),
    ("l16-capture-walkthrough", "캡처 목록을 한 줄씩 읽어요",
     "캡처 목록 네 줄이 차례로 강조됩니다. Seq 1501~2000이 먼저 도착한 Out of order, ACK 1001의 Duplicate ACK, Seq 1001~1500의 Retransmission, ACK 2001의 정상 확인이며 줄마다 먼저 확인할 질문이 나옵니다.",
     "캡처 표식마다 먼저 확인할 질문이 다릅니다. 번호는 설명을 위한 예시이고 캡처 위치에 따라 보이는 모양이 다를 수 있습니다.", lambda: walkthrough(False)),
    ("l16-one-mark-many-causes", "표식 하나, 가능한 이유는 여럿",
     "재전송, 제로 윈도, 중복 ACK 세 표식이 각각 가능한 이유와 함께 볼 것을 보여 줍니다. 재전송은 데이터가 사라졌거나 ACK가 늦었을 수 있고, 제로 윈도는 수신 프로그램이 늦게 읽을 수 있으며 연결 종료가 아니고, 중복 ACK는 빠진 구간이 있을 수 있다는 단서입니다.",
     "표식 하나만으로 문제가 네트워크 경로인지 애플리케이션인지 단정할 수는 없습니다.", lambda: many_causes()),
]

# final layout of the Page: (file, after_paragraph)
LAYOUT = [("l16-daily-tracking-marks", 0), ("l16-recap-path-with-marks", 0),
          ("l16-capture-marks-questions", 1), ("l16-daily-tracking-log-read", 1),
          ("l16-capture-walkthrough", 2), ("l16-one-mark-many-causes", 2)]


def wire(lesson_md):
    q = lambda v: json.dumps(v, ensure_ascii=False)
    head, fm, body = Path(lesson_md).read_text(encoding="utf-8").split("---\n", 2)
    lines = fm.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith(("- terms:", "- page_id:"))]
    end_fm = next((i for i, l in enumerate(lines) if i > starts[-1] and l and not l.startswith((" ", "- "))), len(lines))
    bounds = starts + [end_fm]
    seg = lines[bounds[PAGE_INDEX]:bounds[PAGE_INDEX + 1]]
    new_chunks = {n: [f"  - file: assets/animations/{n}.svg", f"    title: {q(t)}", f"    alt: {q(al)}", f"    caption: {q(c)}"] for n, t, al, c, _ in NEW}
    pre, chunks, i = [], {}, 0
    while i < len(seg):
        if seg[i] == "  illustrations:":
            i += 1
            while i < len(seg) and (seg[i].startswith("  - file:") or seg[i].startswith("    ")):
                if seg[i].startswith("  - file:"):
                    key = Path(seg[i].split("file: ", 1)[1].strip()).stem
                    chunks[key] = [seg[i]]
                else:
                    chunks[key].append(seg[i])
                i += 1
            continue
        pre.append(seg[i]); i += 1
    block = ["  illustrations:"]
    for name, pos in LAYOUT:
        src = new_chunks.get(name) or [x for x in chunks[name] if not x.startswith("    after_paragraph:")]
        block += src + [f"    after_paragraph: {pos}"]
    while pre and pre[-1] == "":
        pre.pop()
    out = lines[:bounds[PAGE_INDEX]] + pre + block + lines[bounds[PAGE_INDEX + 1]:]
    text_ = "\n".join(out)
    if not text_.endswith("\n"):
        text_ += "\n"
    Path(lesson_md).write_text(head + "---\n" + text_ + "---\n" + body, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, *_rest, fn in NEW:
        write(OUT, name, fn())
    if "--svg-only" not in sys.argv:
        wire(LESSON / "lesson.md")
    print("ok", len(NEW), "svgs")
