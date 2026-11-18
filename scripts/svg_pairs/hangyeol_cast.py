"""Shared cast + props for the 한결디자인 "situation SVG" of the advanced course (Unit 11~).

Every situation SVG is a 4-step figure on the standard 960x540 `kit.frame` canvas.
Import with:  from hangyeol_cast import *      (it re-exports kit.* so one import is enough)

4-STEP CONVENTION (one change per step, highlighted with an ORANGE outline via `mark`)
  1. 장면      누가·어디서: 배경(office_bg) + 인물(person) + 장소 이름표. 말풍선 없음.
  2. 일어난 일  문제 하나가 생긴다: monitor("error")/alert_card/doc 등 소품 하나 + (선택) 1명의 말풍선.
  3. 말풍선·걱정 서 이사 / 박 팀장 / 지우 중 말하는 사람의 bubble 또는 thought. 한 단계에 말풍선은 최대 2개.
                 말풍선은 한 번에 하나씩 나타나게(a.vis(..., 3, 4)) 하고, 앞 단계 말풍선은 지워 화면을 비운다.
  4. 알아볼 것  이 Page가 답할 질문 하나를 question()으로 보여 준다(주황 채움 알약 하나).
Rules: 새 글자 라벨은 단계당 3개 이하, 모든 글자 >= 16px, 주황은 "방금 바뀐 것"에만 쓴다.

CANVAS SAFE AREA (frame이 제목 y<=110, 자막 띠 y>=478을 쓴다)
  본문은 y 120~468. 인물은 머리 중심 y~220~260이면 이름표가 y~350 근처에 놓인다.
  question()은 y=438 (알약) 이므로 그 위(y<=410)까지만 소품·이름표를 두면 겹치지 않는다.

COLOURS (색약 안전, 서로 밝기·색조가 다름. kit의 ORANGE=강조, GREEN=성공, RED=오류와 겹치지 않게)
  지우 BLUE #6ea8fe / 박 팀장 TERRACOTTA #e07b54 / 서 이사 VIOLET #c792ea / 직원 GREY #8f98a8 / 고객 TEAL #35c4cf
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import *  # noqa: F401,F403
from u6_l03 import hl, dur, cell  # noqa: F401

TERRACOTTA, GREY, TEAL = "#e07b54", "#8f98a8", "#35c4cf"
CAST = {"지우": BLUE, "박 팀장": TERRACOTTA, "서 이사": VIOLET, "직원": GREY, "고객": TEAL}
ROLES = {"지우": "IT·보안 담당", "박 팀장": "디자인팀장", "서 이사": "경영진"}
MOODS = ("normal", "worried", "surprised", "happy", "thinking")
EYE = "#0f1115"


# ------------------------------------------------------------------ people
def _face(mood):
    """Minimal face in head-local coords (head centre 0,0, r=24, drawn facing right)."""
    eyes = lambda dy=-3, r=3: "".join(f'<circle cx="{ex}" cy="{dy}" r="{r}" fill="{EYE}"/>' for ex in (-7, 11))
    st = f'fill="none" stroke="{EYE}" stroke-width="2.6" stroke-linecap="round"'
    if mood == "worried":
        return (eyes() + f'<path d="M-14 -9 L-4 -14 M18 -9 L8 -14" {st}/><path d="M-4 15 Q3 10 10 15" {st}/>'
                f'<path d="M26 -16 q-6 9 0 13 q6 -4 0 -13z" fill="#9fd8ff"/>')  # sweat drop
    if mood == "surprised":
        return eyes(-4, 4.5) + f'<ellipse cx="3" cy="12" rx="4" ry="5.5" {st}/>'
    if mood == "happy":
        return eyes() + f'<path d="M-7 8 Q3 20 13 8" {st}/>'
    if mood == "thinking":
        return (eyes(-6) + f'<path d="M-3 12 H9" {st}/>'
                + "".join(f'<circle cx="{34 + i * 9}" cy="{-4 - i * 3}" r="{3.2 - i * 0.4}" fill="{MUTED}"/>' for i in range(3)))
    return eyes() + f'<path d="M-5 10 Q3 16 11 10" {st}/>'  # normal


def _outfit(who):
    """Tiny per-role mark on the torso so the cast is distinguishable without colour."""
    if who == "지우":  # ID badge
        return f'<rect x="4" y="52" width="16" height="20" rx="3" fill="{BG}" fill-opacity="0.8"/>'
    if who == "박 팀장":  # tie
        return f'<polygon points="0,32 8,32 11,62 4,70 -3,62" fill="{BG}" fill-opacity="0.75"/>'
    if who == "서 이사":  # collar + tie
        return (f'<polygon points="-12,30 12,30 0,50" fill="{TXT}"/>'
                f'<polygon points="-3,46 3,46 5,70 0,76 -5,70" fill="{BG}" fill-opacity="0.75"/>')
    return ""


def person(x, y, who, mood="normal", scale=1.0, facing="right", role=False):
    """Avatar centred on (x, y) = HEAD centre (head r=24*scale, torso reaches y+90*scale).

    who: "지우" | "박 팀장" | "서 이사" | "직원" | "고객".  mood: normal|worried|surprised|happy|thinking.
    The name tag (>=17px) sits at y+114*scale; with role=True (only 지우/박 팀장/서 이사) a 16px role line follows
    at y+136*scale. Plan ~140*scale px below y. Width is about 64*scale (thinking dots add ~30px to the facing side)."""
    assert who in CAST and mood in MOODS and facing in ("left", "right"), (who, mood, facing)
    c = CAST[who]
    sx = scale if facing == "right" else -scale
    body = (f'<path d="M-30 90 V52 Q-30 30 -8 30 H8 Q30 30 30 52 V90 Z" fill="{c}"/>' + _outfit(who)
            + f'<circle r="24" fill="{c}"/>' + _face(mood))
    out = f'<g transform="translate({x},{y}) scale({sx},{scale})">{body}</g>'
    out += text(x, y + 114 * scale, who, 17, TXT, 700)
    if role and who in ROLES:
        out += text(x, y + 136 * scale, ROLES[who], 16, MUTED)
    return out


# ------------------------------------------------------------------ bubbles
def wrap(s, fs=18, max_lines=2):
    """Greedy wrap on spaces (or hard split) into <= max_lines lines of <= ~16 chars at 18px. '\\n' forces a break."""
    maxc = int(290 / (0.98 * fs))
    lines = []
    for part in s.split("\n"):
        cur = ""
        for word in part.split(" "):
            while len(word) > maxc:  # hard split Hangul runs with no spaces
                if cur:
                    lines.append(cur)
                    cur = ""
                lines.append(word[:maxc])
                word = word[maxc:]
            if cur and len(cur) + 1 + len(word) > maxc:
                lines.append(cur)
                cur = word
            else:
                cur = f"{cur} {word}" if cur else word
        lines.append(cur)
    assert len(lines) <= max_lines, f"bubble text too long ({len(lines)} lines): {s}"
    return lines


def _lines_svg(x, top, lines, fs, fill=TXT):
    return "".join(text(x, top + 24 + 26 * i + fs * 0.36, ln, fs, fill, 700) for i, ln in enumerate(lines))


def bubble(x, y, s, w=None, tail_to=None, color=LINE, fs=18):
    """Speech bubble CENTRED at (x, y). Text wraps to <= 2 lines (about 16 Korean chars per line at 18px).
    tail_to=(tx, ty): tail apex, drawn from the bottom/top edge (or a side edge if ty is level with the bubble).
    color = outline colour (use the speaker's CAST colour)."""
    lines = wrap(s, fs)
    w = w or max(tw(ln, fs) for ln in lines) + 36
    h = 26 * len(lines) + 22
    l, t, r, b = x - w / 2, y - h / 2, x + w / 2, y + h / 2
    tail = cover = ""
    if tail_to:
        tx, ty = tail_to
        if ty >= b or ty <= t:
            bx, ey = min(max(tx, l + 24), r - 24), (b if ty >= b else t)
            pts, seam = f"{bx - 10},{ey} {bx + 10},{ey} {tx},{ty}", (bx - 8, ey, bx + 8, ey)
        else:
            ex, by = (l if tx < x else r), min(max(ty, t + 14), b - 14)
            pts, seam = f"{ex},{by - 9} {ex},{by + 9} {tx},{ty}", (ex, by - 7, ex, by + 7)
        tail = f'<polygon points="{pts}" fill="{PANEL}" stroke="{color}" stroke-width="3" stroke-linejoin="round"/>'
        cover = f'<line x1="{seam[0]:.0f}" y1="{seam[1]:.0f}" x2="{seam[2]:.0f}" y2="{seam[3]:.0f}" stroke="{PANEL}" stroke-width="5"/>'
    return tail + box(l, t, w, h, color, PANEL, 16, sw=3) + cover + _lines_svg(x, t, lines, fs)


def thought(x, y, s, w=None, tail_to=None, color=MUTED, fs=18):
    """Thought bubble CENTRED at (x, y): dashed outline + a trail of 3 shrinking dots toward tail_to (the head)."""
    lines = wrap(s, fs)
    w = w or max(tw(ln, fs) for ln in lines) + 40
    h = 26 * len(lines) + 26
    t, b = y - h / 2, y + h / 2
    out = f'<rect x="{x - w / 2:.0f}" y="{t:.0f}" width="{w:.0f}" height="{h}" rx="{h / 2:.0f}" fill="{PANEL}" stroke="{color}" stroke-width="3" stroke-dasharray="7 5"/>'
    if tail_to:
        tx, ty = tail_to
        sx, sy = min(max(tx, x - w / 2 + 30), x + w / 2 - 30), (b if ty >= y else t)
        for f, r in ((0.2, 8), (0.5, 6), (0.8, 4)):
            out += f'<circle cx="{sx + (tx - sx) * f:.0f}" cy="{sy + (ty - sy) * f:.0f}" r="{r}" fill="{PANEL}" stroke="{color}" stroke-width="2.5"/>'
    return out + _lines_svg(x, t + 2, lines, fs)


# ------------------------------------------------------------------ props
def monitor(x, y, state="ok", msg=None):
    """Computer screen centred at (x, y) (screen 190+ x 112, stand below to y+76). state: ok | error | loading.
    msg (16px, ~11 Korean chars max) is printed inside under the icon."""
    c = {"ok": GREEN, "error": RED, "loading": BLUE}[state]
    w = max(190, tw(msg, 16) + 32) if msg else 190
    assert w <= 260, f"monitor msg too long: {msg}"
    icon = {"ok": check(x, y - 18), "error": cross(x, y - 18),
            "loading": "".join(f'<circle cx="{x + d}" cy="{y - 18}" r="6" fill="{BLUE}" fill-opacity="{o}"/>' for d, o in ((-20, 1), (0, 0.6), (20, 0.3)))}[state]
    return (box(x - w / 2, y - 56, w, 112, c, PANEL, 10, sw=4) + icon
            + (text(x, y + 38, msg, 16, TXT, 700) if msg else "")
            + f'<rect x="{x - 8}" y="{y + 56}" width="16" height="14" fill="{LINE}"/>'
            + f'<rect x="{x - 36}" y="{y + 70}" width="72" height="7" rx="3" fill="{LINE}"/>')


def chat_window(x, y, lines):
    """AI chat UI centred at (x, y), 270x150. lines[0] = the user's message (shown as text, <= ~14 chars);
    every further entry is drawn only as a grey reply bar whose length follows the entry's length."""
    w, h = 270, 150
    l, t = x - w / 2, y - h / 2
    first = lines[0]
    bw = tw(first, 16) + 24
    assert bw <= w - 32, f"chat line too long: {first}"
    bars = lines[1:] or ["", ""]
    out = (box(l, t, w, h, BLUE, PANEL, 12, sw=3) + f'<rect x="{l}" y="{t}" width="{w}" height="26" rx="12" fill="{BLUE}" fill-opacity="0.35"/>'
           + "".join(f'<circle cx="{l + 16 + i * 14}" cy="{t + 13}" r="4" fill="{TXT}" fill-opacity="0.8"/>' for i in range(3))
           + box(r_ := l + w - 16 - bw, t + 38, bw, 34, BLUE, BG, 10, sw=2) + text(r_ + 12, t + 61, first, 16, TXT, 700, "start"))
    for i, b in enumerate(bars[:2]):
        bl = min(max(len(b) * 12, 110), w - 40) if b else (190 if i == 0 else 130)
        out += f'<rect x="{l + 16}" y="{t + 88 + i * 24}" width="{bl}" height="12" rx="6" fill="{MUTED}" fill-opacity="0.55"/>'
    return out


def doc(x, y, label=None, c=BLUE):
    """Document / drawing icon centred at (x, y) (56x72) with a 17px label under it (e.g. "고객 도면")."""
    out = (f'<rect x="{x - 28}" y="{y - 36}" width="56" height="72" rx="4" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
           f'<polygon points="{x + 12},{y - 36} {x + 28},{y - 20} {x + 12},{y - 20}" fill="{c}"/>'
           + "".join(f'<rect x="{x - 18}" y="{y - 6 + i * 13}" width="{36 - i * 8}" height="5" rx="2" fill="{c}" fill-opacity="0.6"/>' for i in range(3)))
    return out + (text(x, y + 62, label, 17, TXT, 700) if label else "")


def alert_card(x, y, msg):
    """Red warning card centred at (x, y): triangle "!" + one 17px line (width follows the text)."""
    w = tw(msg, 17) + 76
    l = x - w / 2
    return (box(l, y - 26, w, 52, RED, PANEL, 12, sw=3)
            + f'<polygon points="{l + 28},{y - 14} {l + 44},{y + 14} {l + 12},{y + 14}" fill="{RED}"/>'
            + text(l + 28, y + 11, "!", 17, BG, 700) + text(l + 58, y + 6, msg, 17, TXT, 700, "start"))


def meeting_table(x, y):
    """Oval meeting table centred at (x, y), about 300 wide; seat people behind it (head y ~ y-90)."""
    return (f'<ellipse cx="{x}" cy="{y + 14}" rx="150" ry="34" fill="#1d232d"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="150" ry="34" fill="#262e3b" stroke="{LINE}" stroke-width="2"/>'
            + line(x - 90, y + 30, x - 90, y + 64, LINE, 6) + line(x + 90, y + 30, x + 90, y + 64, LINE, 6))


def clock(x, y, label=None, c=MUTED):
    """Wall/desk clock centred at (x, y) r=30; hands show 3 o'clock-ish. label (17px) goes under it (e.g. "오후 4시")."""
    out = (f'<circle cx="{x}" cy="{y}" r="30" fill="{PANEL}" stroke="{c}" stroke-width="3"/>'
           + "".join(f'<circle cx="{x + dx}" cy="{y + dy}" r="2.5" fill="{c}"/>' for dx, dy in ((0, -23), (23, 0), (0, 23), (-23, 0)))
           + f'<path d="M{x} {y} V{y - 16} M{x} {y} L{x + 12} {y + 6}" stroke="{c}" stroke-width="3.5" stroke-linecap="round"/>')
    return out + (text(x, y + 56, label, 17, TXT, 700) if label else "")


def office_bg(kind="office"):
    """Very low-contrast backdrop (below the title, above the caption bar). kind: office | client | home | server_room."""
    W, F, S = "#12151c", "#141922", "#1d2431"  # wall / floor tones and outline, barely above BG
    out = f'<rect x="0" y="410" width="960" height="68" fill="{F}"/>' + line(0, 410, 960, 410, S, 2)
    r = lambda x, y, w, h, f="none", s=S: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}" stroke="{s}" stroke-width="2"/>'
    if kind == "office":
        out += (r(690, 130, 200, 170, W) + line(790, 130, 790, 300) + line(690, 215, 890, 215)  # window
                + r(70, 150, 120, 80, W) + line(90, 180, 170, 180) + line(90, 200, 150, 200)  # wall chart
                )
    elif kind == "client":
        for bx, bh, bw in ((60, 230, 110), (200, 160, 90), (320, 290, 120), (700, 200, 110), (840, 260, 100)):
            out += r(bx, 410 - bh, bw, bh, W) + "".join(
                r(bx + 14 + i % 3 * (bw // 3), 410 - bh + 16 + i // 3 * 36, 16, 20, F) for i in range(min(9, (bh - 30) // 36 * 3)))
    elif kind == "home":
        out += (r(640, 130, 220, 180, W) + line(750, 130, 750, 310) + r(120, 300, 260, 110, W)  # window, sofa
                + r(120, 270, 260, 40, W) + line(520, 410, 520, 250) + f'<polygon points="495,250 545,250 535,215 505,215" fill="{W}" stroke="{S}" stroke-width="2"/>')
    else:  # server_room
        for i in range(6):
            bx = 90 + i * 140
            out += r(bx, 140, 100, 270, W) + "".join(line(bx + 14, 168 + j * 36, bx + 86, 168 + j * 36) + f'<circle cx="{bx + 22}" cy="{182 + j * 36}" r="3" fill="{S}"/>' for j in range(6))
    return out


# ------------------------------------------------------------------ frame helpers
def new():
    """Anim for the standard 4-step situation SVG (16s loop)."""
    return Anim(4, dur(False))


def mark(a, x, y, w, h, t):
    """Orange outline shown ONLY in step t: the one thing that just changed."""
    return a.vis(hl(x, y, w, h), t, t)


def question(a, s, y=438, step=4):
    """Step-4 element: small "이 Page에서 알아볼 것" label above ONE filled orange pill naming the Page's question."""
    return a.vis(text(480, y - 36, "이 Page에서 알아볼 것", 16, MUTED) + pill(480, y, s, ORANGE, 22, True), step, step)


def scene(a, title, subtitle, captions, body, bg=None):
    """kit.frame wrapper: asserts the 4-step shape, optionally prepends office_bg(bg), returns the SVG string.
    title <= ~20 Korean chars (32px), subtitle <= ~40 chars (22px), each caption <= ~36 chars (24px)."""
    assert a.n == 4 and len(captions) == 4, "situation SVGs have exactly 4 steps and 4 captions"
    return frame(a, title, subtitle, captions, (office_bg(bg) if bg else "") + body)
