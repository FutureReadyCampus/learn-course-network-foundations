#!/usr/bin/env python3
"""Module 4·5 구조 이전 도구(일회용): 옛 Unit 10개 -> 새 Unit 5개. (Module 3 은 restructure_m3.py)

    python3 scripts/restructure_exercises.py 4           # exercises/module/4/unit 를 새 구조로 바꾼다
    python3 scripts/restructure_exercises.py 5 --check   # 사람이 손볼 곳을 찾는다(바꾸지 않음)

규칙은 restructure_m3.py 와 같고, Module 4·5 때문에 다음이 다르다.
- 같은 새 Unit 에 묶인 옛 Unit 들의 「시작하기」를 모두 가져온다(데이터 파일이 Unit 마다 있어서). 두 번째부터는 REVIEW 표시를 붙인다.
- 실습 레슨 안의 마무리·깃허브 올리기 쪽은 새 Unit 의 마지막 핵심 실습으로 모은다.
- `Module N ... Unit k`(다른 Module 가리킴)와 그 뒤 `실습 a-b` 는 바꾸지 않는다.
- 완성본이 없거나 빈칸 템플릿뿐인 제공 파일은 TODO(assemble) 표시와 함께 템플릿을 넣는다.
- 본문 그림(f*.svg)은 가져온 레슨마다 이름 앞에 출처를 붙여 겹치지 않게 옮긴다.
"""
import re, shutil, sys
from pathlib import Path
import yaml

ROOT0 = Path(__file__).resolve().parent.parent / "exercises/module"

MODULES = {
    4: dict(
        unit_map={1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5},
        plan={
            1: ("로그를 같은 모양으로 맞추기", ["1-1", "2-1"], ["1-2", "2-2", "2-3"], []),
            2: ("판다스로 세고 기준 정하기", ["3-1", "3-2", "4-2"], ["4-1", "4-3"], []),
            3: ("요청 급증과 반복 거절 찾기", ["5-1", "6-1"], ["5-2", "6-2", "6-3"], []),
            4: ("위험 점수 매기고 오탐 줄이기", ["7-2", "8-2"], ["7-1", "8-1", "8-3"],
                ["saas_detection.py", "malicious_detection.py", "correlation.py"]),
            5: ("AI 요약과 총정리", ["10-1", "10-3"], ["9-1", "9-2", "10-2"], []),
        }),
    5: dict(
        unit_map={1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 4, 10: 5},
        plan={
            1: ("플레이북으로 알림 처리하기", ["1-1", "1-2", "2-1"], ["2-2", "2-3"], ["routing.py", "safe_runner.py"]),
            2: ("계정 잠그고 세션 끊기", ["4-1", "4-3"], ["3-1", "3-2", "4-2"], ["ip_actions.py", "audit.py", "approvals.py"]),
            3: ("되돌리고 티켓 남기기", ["5-1", "6-1"], ["5-2", "6-2", "6-3"], ["ticket_merge.py", "ticket_notice.py"]),
            4: ("승인 게이트와 오탐 되돌리기", ["8-2", "8-3"], ["7-1", "7-2", "8-1", "9-1", "9-2"], ["escalation.py", "report.py"]),
            5: ("통합 엔진과 최종 회고", ["10-1", "10-3"], ["10-2"], []),
        }),
}
KO = {"exercise": "실습", "challenge": "도전"}
DROP_RE = re.compile(r"마무리|완성본|^부록|정답 확인 후 점검")
CLOSING_RE = re.compile(r"마무리|깃허브에 올리기")
TEMPLATE_RE = re.compile(r"직접 씁니다|직접 쓰는")


class Ctx:
    def __init__(self, m):
        self.m = m
        self.root = ROOT0 / str(m)
        self.unit = self.root / "unit"
        cfg = MODULES[m]
        self.plan, self.unit_map = cfg["plan"], cfg["unit_map"]
        self.label = {}
        for nu, (_, core, chal, _p) in self.plan.items():
            for kind, lst in (("exercise", core), ("challenge", chal)):
                for n, old in enumerate(lst, 1):
                    self.label[old] = (kind, nu, n)

    def sub(self, text):
        keep = []
        def hold(m):
            keep.append(m[0]); return f"\x00{len(keep) - 1}\x00"
        # 다른 Module 을 가리키는 말은 그대로 둔다
        text = re.sub(r"Module \d+[^\n。.]{0,12}?Unit \d+(?:[^\n。.]{0,14}?실습 \d+-\d+)?", hold, text)
        def ex(m):
            k = self.label.get(f"{m['a']}-{m['b']}")
            return f"{KO[k[0]]} {k[1]}-{k[2]}" if k else m[0]
        text = re.sub(r"실습 (?P<a>\d+)-(?P<b>\d+)(?![-\d])", ex, text)
        def fn(m):
            k = self.label.get(f"{m['a']}-{m['b']}")
            return f"{k[0]}{k[1]}-{k[2]}{m['rest'] or ''}" if k else m[0]
        text = re.sub(r"(?<![A-Za-z])(?:exercise|challenge)(?P<a>\d+)-(?P<b>\d+)(?P<rest>-\d+)?", lambda m: fn(m) if m[0].startswith(("exercise", "challenge")) else m[0], text)
        text = re.sub(r"report_u(\d+)", lambda m: f"report_u{self.unit_map.get(int(m[1]), int(m[1]))}", text)
        um = self.unit_map
        text = re.sub(r"Unit (\d+)(?:~(\d+))?", lambda m: f"Unit {um.get(int(m[1]), int(m[1]))}" + (f"~{um.get(int(m[2]), int(m[2]))}" if m[2] else ""), text)
        return re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m[1])], text)


def split_fm(t):
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", t, re.S)
    return yaml.safe_load(m[1]), m[2]


def pages_of(body):
    out, cur, fence = [], None, ""
    for line in body.split("\n"):
        f = re.match(r"^(`{3,})", line)
        if f and not fence: fence = f[1]
        elif f and fence and len(f[1]) >= len(fence) and line.strip("`") == "": fence = ""
        m = None if fence else re.match(r"^## (.+)$", line)
        if m:
            cur = [m[1].strip(), []]; out.append(cur)
        elif cur is not None:
            cur[1].append(line)
    return [(t, "\n".join(b).strip("\n")) for t, b in out]


class Lesson:
    def __init__(self, path):
        self.dir = path.parent
        self.fm, body = split_fm(path.read_text())
        self.title = self.fm["title"]
        self.pages = pages_of(body)
        self.tag = f"u{self.dir.parent.parent.name}l{self.dir.name}"
        if self.fm.get("page_videos"):
            print(f"경고: page_videos 는 옮기지 않습니다 {path}")

    def svg(self, i):
        p = self.dir / "assets" / f"p{i:02d}.svg"
        return p if p.exists() else None

    def page(self, i):  # (제목, 본문, p-svg, 출처 Lesson)
        t, b = self.pages[i - 1]
        return (t, b, self.svg(i), self)


def load_old(c):
    old = {}
    for ud in sorted(c.unit.iterdir()):
        um = yaml.safe_load((ud / "unit.md").read_text().split("---")[1])
        old[int(ud.name)] = [Lesson(ud / l["path"]) for l in um["lessons"]]
    return old


def segment(l):
    """정답·보고서 Lesson 의 페이지를 옛 실습별로 나눈다(번호 없는 페이지는 앞 실습에 붙고, 맨 앞 공통은 None)."""
    segs, key = {}, None
    for i, (t, b) in enumerate(l.pages, 1):
        m = re.match(r"실습 (\d+-\d+)", t)
        if m: key = m[1]
        if DROP_RE.search(t): key = "DROP"
        elif re.match(r"보고서 (쓰는 법|작성 방법)", t): key = None
        segs.setdefault(key, []).append(l.page(i))
    return segs


def find_complete(old, name):
    """(코드, 완성본 여부). 가장 뒤의 '완성본' 표시 코드를 우선한다."""
    hits = []
    pat = re.compile(r"\*\*`" + re.escape(name) + r"`\*\*([^\n]*)\n+```python\n(.*?)\n```", re.S)
    for ls in old.values():
        for l in ls:
            for _, b in l.pages:
                for m in pat.finditer(b):
                    hits.append(("완성본" in m[1] and not TEMPLATE_RE.search(m[2]), m[2]))
    full = [code for ok, code in hits if ok]
    if full: return full[-1], True
    return (hits[-1][1] if hits else None), False


def write_lesson(c, outdir, n, nu, title, pages, fm_extra=None):
    """pages: [(제목, 본문, p-svg, 출처 Lesson)]"""
    d = outdir / "lesson" / f"{n:02d}"
    (d / "assets").mkdir(parents=True, exist_ok=True)
    fm = {"id": f"m{c.m}-u{nu:02d}-l{n:02d}", "title": title, "render": "markdown"}
    fm.update(fm_extra or {})
    parts = []
    for i, (t, b, svg, src) in enumerate(pages, 1):
        if svg:
            dst = d / "assets" / f"p{i:02d}.svg"
            shutil.copy(svg, dst); dst.write_text(c.sub(dst.read_text()))
        def fig(m, src=src):
            s = src.dir / "assets" / m[1]
            if not s.exists(): return m[0]
            name = f"{src.tag}_{m[1]}"
            (d / "assets" / name).write_text(c.sub(s.read_text()))
            return f"assets/{name}"
        parts.append(f"## {c.sub(t)}\n\n" + re.sub(r"assets/(f\d+\.svg)", fig, c.sub(b)))
    text = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---\n\n# " + title + "\n\n" + "\n\n".join(parts) + "\n"
    (d / "lesson.md").write_text(text)
    return f"lesson/{n:02d}/lesson.md"


def closing_pages(old, ex, o):
    """옛 실습 o 가 속한 옛 Unit 에서 마무리·깃허브 올리기 쪽을 가진 가장 뒤 실습 Lesson 의 쪽들"""
    u = ex[o][0]
    cands = [(k, l) for k, (uu, l) in ex.items() if uu == u and any(CLOSING_RE.search(t) for t, _ in l.pages[1:])]
    if not cands: return []
    _, l = sorted(cands, key=lambda x: [int(p) for p in x[0].split("-")])[-1]
    return [l.page(i) for i, (t, _) in enumerate(l.pages, 1) if i > 1 and CLOSING_RE.search(t)]


def build(m):
    c = Ctx(m)
    old = load_old(c)
    ex = {}
    for u, ls in old.items():
        for l in ls:
            mm = re.match(r"실습 (\d+-\d+) · ", l.title)
            if mm: ex[mm[1]] = (u, l)
    missing = [o for nu in c.plan.values() for o in nu[1] + nu[2] if o not in ex]
    assert not missing, f"옛 실습 없음: {missing}"
    new_root = c.unit.parent / "unit.new"
    shutil.rmtree(new_root, ignore_errors=True)
    units = []
    for nu, (utitle, core, chal, provided) in c.plan.items():
        od = new_root / f"{nu:02d}"
        out = []  # (번호, 경로)
        n = 0
        # 1) 시작하기: 핵심 실습이 있던 옛 Unit 들의 시작하기를 모두 모은다
        core_units = []
        for o in core:
            if ex[o][0] not in core_units: core_units.append(ex[o][0])
        start_pages = []
        for k, u in enumerate(core_units):
            st = next(l for l in old[u] if l.title == "시작하기")
            for i in range(1, len(st.pages) + 1):
                t, b, s, src = st.page(i)
                if k > 0:
                    b = f"<!-- REVIEW: 옛 Unit {u} 시작하기에서 가져온 쪽입니다. 새 Unit 시작하기에 맞게 합치거나 지우세요 -->\n\n" + b
                start_pages.append((t, b, s, src))
        n += 1; out.append((n, write_lesson(c, od, n, nu, "시작하기", start_pages, None)))
        last_core = core[-1]
        close = closing_pages(old, ex, last_core)
        # 2) 핵심 실습 -> 제공 파일 -> 도전
        def exlesson(o, extra=()):
            nonlocal n
            u, l = ex[o]
            pages = [l.page(i) for i, (t, _) in enumerate(l.pages, 1) if i == 1 or not CLOSING_RE.search(t)]
            pages += list(extra)
            fm = {"source": l.fm["source"]} if "source" in l.fm else None
            n += 1; out.append((n, write_lesson(c, od, n, nu, c.sub(l.title), pages, fm)))
        for o in core: exlesson(o, close if o == last_core else ())
        n += 1; provided_no = n
        for o in chal: exlesson(o)
        # 3) 제공 파일
        ppages = []
        for name in provided:
            code, ok = find_complete(old, name)
            if ok:
                body = f"**`{name}`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.\n\n```python\n{code}\n```"
            else:
                tpl = f"\n\n```python\n{code}\n```" if code else ""
                body = f"TODO(assemble): `{name}` 완성 코드를 옛 실습의 시작 코드와 정답을 합쳐 채운다.{tpl}"
            ppages.append((f"`{name}` 만들기", body, None, old[1][0]))
        if provided:
            out.append((provided_no, write_lesson(c, od, provided_no, nu, "제공 파일", ppages)))
        # 4) 정답, 보고서 (제공 파일이 없으면 번호를 한 칸 당긴다)
        answer_pages, report_pages = [], []
        for o in core + chal:
            u = ex[o][0]
            ans = next(l for l in old[u] if l.title == "정답")
            rep = next(l for l in old[u] if l.title == "보고서 쓰기")
            a, r = segment(ans), segment(rep)
            if not answer_pages: answer_pages += a.get(None, [])[:1]
            answer_pages += a.get(o, [])
            if not report_pages: report_pages += r.get(None, [])
            report_pages += r.get(o, [])
        nums = sorted(x for x, _ in out)
        base = max(nums) + 1
        out.append((base, write_lesson(c, od, base, nu, "정답", answer_pages)))
        out.append((base + 1, write_lesson(c, od, base + 1, nu, "보고서 쓰기", report_pages)))
        paths = [p for _, p in sorted(out)]
        # 제공 파일이 없을 때 번호를 연속으로 맞춘다
        if not provided:
            _renumber(od, paths, nu, c)
            paths = [f"lesson/{i:02d}/lesson.md" for i in range(1, len(paths) + 1)]
        um = {"id": f"m{c.m}-u{nu:02d}", "title": utitle, "lessons": [{"path": p} for p in paths]}
        (od / "unit.md").write_text("---\n" + yaml.safe_dump(um, allow_unicode=True, sort_keys=False, width=1000) + f"---\n\n# {utitle}\n")
        units.append({"id": um["id"], "title": utitle, "path": f"exercises/module/{c.m}/unit/{nu:02d}/unit.md"})
    cy = yaml.safe_load((c.root / "course.yaml").read_text())
    cy["units"] = units
    (c.root / "course.yaml").write_text(yaml.safe_dump(cy, allow_unicode=True, sort_keys=False, width=1000))
    shutil.rmtree(c.unit); new_root.rename(c.unit)


def _renumber(od, paths, nu, c):
    """lesson 폴더가 건너뛴 번호를 1..N 으로 당긴다(제공 파일이 없는 Unit)."""
    cur = sorted(int(Path(p).parent.name) for p in paths)
    for new, old_n in enumerate(cur, 1):
        if new != old_n:
            (od / "lesson" / f"{old_n:02d}").rename(od / "lesson" / f"{new:02d}")
            f = od / "lesson" / f"{new:02d}" / "lesson.md"
            f.write_text(re.sub(r"(?m)^id: m\d+-u\d+-l\d+$", f"id: m{c.m}-u{nu:02d}-l{new:02d}", f.read_text(), count=1))


def check(m):
    """새 구조에서 사람이 고칠 곳을 찾는다."""
    c = Ctx(m); bad = 0
    for f in sorted(c.root.glob("unit/*/lesson/*/lesson.md")):
        for no, line in enumerate(f.read_text().split("\n"), 1):
            if re.search(r"TODO|REVIEW:|Unit \d+ ?(까지|의|에서|부터)|앞 실습 파일 완성본|「정답」 레슨|부록", line):
                print(f"{f.relative_to(c.root)}:{no}: {line.strip()[:100]}"); bad += 1
    print(f"{bad} lines to review")


if __name__ == "__main__":
    mod = int(sys.argv[1])
    check(mod) if "--check" in sys.argv else build(mod)
