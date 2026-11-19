#!/usr/bin/env python3
"""Module 3 구조 이전 도구(일회용): 옛 Unit 10개 -> 새 Unit 5개.

    python3 scripts/restructure_m3.py            # exercises/module/3/unit 를 새 구조로 바꾼다
    python3 scripts/restructure_m3.py --check    # 옛 번호가 남은 곳을 찾는다(바꾸지 않음)

규칙: 새 Unit 안에서 핵심은 `실습 U-n`, 선택은 `도전 U-n` 으로 다시 번호를 매기고,
본문의 옛 `실습 a-b`·`exerciseA-B_*.py`·`Unit k`·`report_uk.md` 를 한 번에 바꾼다.
(정규식 한 번 통과라 번호가 겹쳐도 두 번 바뀌지 않는다.)
"""
import re, shutil, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent / "exercises/module/3"
UNIT = ROOT / "unit"

# 새 Unit: 제목, 핵심(옛 번호), 도전(옛 번호), 제공 파일(이름: 완성본을 찾을 옛 실습)
PLAN = {
    1: ("역할로 권한 정하기", ["1-1", "1-2", "2-3"], ["1-3", "2-1", "2-2", "3-1", "3-2"],
        ["exception_policy.py", "config_loader.py"]),
    2: ("요청서로 권한 주기", ["4-1", "4-2"], ["4-3", "5-1", "5-2"], ["req_grant.py"]),
    3: ("안 쓰는 권한 점검하기", ["6-1", "6-3"], ["6-2", "7-1", "7-2"],
        ["review_rules.py", "overprivilege.py", "report_exclude.py"]),
    4: ("권한 거두기", ["8-2", "8-3"], ["8-1", "9-1", "9-2"], ["revoke_input.py", "revoke_plan.py"]),
    5: ("결과 보고하기", ["10-1", "10-3"], ["10-2"], ["log_summary.py", "weekly_report.py"]),
}
UNIT_MAP = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4, 9: 4, 10: 5}
LABEL = {}  # 옛 'a-b' -> (kind, 새 unit, n)
for nu, (_, core, chal, _p) in PLAN.items():
    for kind, lst in (("exercise", core), ("challenge", chal)):
        for n, old in enumerate(lst, 1):
            LABEL[old] = (kind, nu, n)
KO = {"exercise": "실습", "challenge": "도전"}
DROP_PAGES = ("마무리", "정답 마무리", "앞 실습 파일 완성본")


def sub(text):
    def ex(m):
        k, u, n = LABEL[f"{m['a']}-{m['b']}"]
        return f"{KO[k]} {u}-{n}"
    text = re.sub(r"실습 (?P<a>\d+)-(?P<b>\d+)(?![-\d])", ex, text)
    def fn(m):
        k, u, n = LABEL[f"{m['a']}-{m['b']}"]
        return f"{k}{u}-{n}{m['rest'] or ''}"
    text = re.sub(r"exercise(?P<a>\d+)-(?P<b>\d+)(?P<rest>-\d+)?", fn, text)
    text = re.sub(r"report_u(\d+)", lambda m: f"report_u{UNIT_MAP[int(m[1])]}", text)
    text = re.sub(r"Unit (\d+)", lambda m: f"Unit {UNIT_MAP.get(int(m[1]), int(m[1]))}", text)
    return text


def split_fm(t):
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", t, re.S)
    return yaml.safe_load(m[1]), m[2]


def pages_of(body):
    """fence-aware: '## ' 제목마다 한 페이지. [(제목, 본문)]"""
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
        self.pages = pages_of(body)  # 페이지 i(1부터) <-> assets/p{i:02d}.svg

    def svg(self, i):
        p = self.dir / "assets" / f"p{i:02d}.svg"
        return p if p.exists() else None


def load_old():
    old = {}
    for u in range(1, 11):
        ud = UNIT / f"{u:02d}"
        um = yaml.safe_load((ud / "unit.md").read_text().split("---")[1])
        old[u] = [Lesson(ud / l["path"]) for l in um["lessons"]]
    return old


def exercise_of(old_lessons):
    """옛 번호 -> (옛 Unit, 실습 Lesson)"""
    d = {}
    for u, ls in old_lessons.items():
        for l in ls:
            m = re.match(r"실습 (\d+-\d+) · ", l.title)
            if m: d[m[1]] = (u, l)
    return d


def segment(l, by_title=r"실습 (\d+-\d+)"):
    """정답·보고서 Lesson 의 페이지를 옛 실습별로 나눈다. 번호가 없는 페이지는 앞 실습 쪽에 붙고,
    맨 앞 공통 페이지는 key None."""
    segs, key = {}, None
    for i, (t, b) in enumerate(l.pages, 1):
        m = re.match(by_title, t)
        if m: key = m[1]
        if t in DROP_PAGES: key = "DROP"
        elif t == "보고서 쓰는 법": key = None
        segs.setdefault(key, []).append((i, t, b, l))
    return segs


def find_complete(old, name):
    """옛 Lesson 들에서 `name` 의 완성 코드를 찾는다(가장 뒤의 '완성본' 표시 우선)."""
    hits = []
    pat = re.compile(r"\*\*`" + re.escape(name) + r"`\*\*([^\n]*)\n+```python\n(.*?)\n```", re.S)
    for ls in old.values():
        for l in ls:
            for _, b in l.pages:
                for m in pat.finditer(b):
                    hits.append(("완성본" in m[1], m[2]))
    full = [c for ok, c in hits if ok]
    return (full or [c for _, c in hits] or [None])[-1]


def write_lesson(outdir, n, nu, title, pages, fm_extra=None):
    """pages: [(제목, 본문, 옛 svg 경로 또는 None)]"""
    d = outdir / "lesson" / f"{n:02d}"
    (d / "assets").mkdir(parents=True, exist_ok=True)
    fm = {"id": f"m3-u{nu:02d}-l{n:02d}", "title": title, "render": "markdown"}
    fm.update(fm_extra or {})
    parts, fig = [], 0
    for i, (t, b, svg) in enumerate(pages, 1):
        if svg:
            shutil.copy(svg, d / "assets" / f"p{i:02d}.svg")
            s = (d / "assets" / f"p{i:02d}.svg"); s.write_text(sub(s.read_text()))
        parts.append(f"## {sub(t)}\n\n{b}")
    text = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---\n\n# " + title + "\n\n" + "\n\n".join(parts) + "\n"
    (d / "lesson.md").write_text(text)
    return f"lesson/{n:02d}/lesson.md"


def build():
    old = load_old()
    ex = exercise_of(old)
    new_root = UNIT.parent / "unit.new"
    shutil.rmtree(new_root, ignore_errors=True)
    units = []
    for nu, (utitle, core, chal, provided) in PLAN.items():
        od = new_root / f"{nu:02d}"
        lessons, pending = [], []  # pending: (title, pages 만드는 함수)
        n = 0
        first_old = ex[core[0]][0]
        # 1) 시작하기 (+ Unit 1 은 포트폴리오 소개가 이 안에, Unit 2 는 준비 과제 앞에)
        if nu == 2:
            prep = old[2][0]
            n += 1
            lessons.append(("준비 · " + prep.title.split(" · ", 1)[-1] if " · " in prep.title else prep.title, prep, n))
        start = next(l for l in old[first_old] if l.title == "시작하기")
        n += 1; lessons.append(("시작하기", start, n))
        order = [("실습", core), ("도전", chal)]
        # 2) 핵심 실습 -> 제공 파일 -> 도전
        def exlesson(o):
            nonlocal n
            u, l = ex[o]
            n += 1
            lessons.append((l.title, l, n))  # 번호는 아래에서 sub() 가 한 번만 바꾼다
        for o in core: exlesson(o)
        n += 1; provided_no = n
        for o in chal: exlesson(o)
        # 3) 정답, 보고서
        answer_pages, report_pages = [], []
        for o in core + chal:
            u = ex[o][0]
            ans = next(l for l in old[u] if l.title == "정답")
            rep = next(l for l in old[u] if l.title == "보고서 쓰기")
            ans_seg, rep_seg = segment(ans), segment(rep)
            if not answer_pages:
                answer_pages += [(t, b, l.svg(i)) for i, t, b, l in ans_seg.get(None, [])][:1]
            answer_pages += [(t, b, l.svg(i)) for i, t, b, l in ans_seg.get(o, [])]
            if not report_pages:
                report_pages += [(t, b, l.svg(i)) for i, t, b, l in rep_seg.get(None, [])]
            report_pages += [(t, b, l.svg(i)) for i, t, b, l in rep_seg.get(o, [])]
        n += 1; answer_no = n
        n += 1; report_no = n
        # --- 쓰기
        out_lessons = []
        for title, l, num in lessons:
            if num == provided_no: continue
            pages = []
            for i, (t, b) in enumerate(l.pages, 1):
                pages.append((t, b, l.svg(i)))
            fm = {"source": l.fm["source"]} if "source" in l.fm else None
            out_lessons.append((num, write_lesson(od, num, nu, sub(title), [(t, sub(b), s) for t, b, s in pages], fm)))
            # 본문 그림(f*.svg)은 옛 Lesson 에서 그대로 복사하고 내용만 새 번호로 고친다
            for f in (l.dir / "assets").glob("f*.svg"):
                dst = od / "lesson" / f"{num:02d}" / "assets" / f.name
                dst.write_text(sub(f.read_text()))
        # 제공 파일
        ppages = []
        for name in provided:
            code = find_complete(old, name)
            body = (f"**`{name}`** 을 만들고 아래 내용을 붙여 넣습니다. 이 파일은 직접 만들지 않고 가져다 씁니다.\n\n```python\n{code}\n```"
                    if code else f"TODO(#{267 + nu - 1}): `{name}` 완성 코드를 옛 실습 시작 코드와 정답을 합쳐 채운다.")
            ppages.append((f"`{name}` 만들기", sub(body), None))
        out_lessons.append((provided_no, write_lesson(od, provided_no, nu, "제공 파일", ppages)))
        out_lessons.append((answer_no, write_lesson(od, answer_no, nu, "정답", [(t, sub(b), s) for t, b, s in answer_pages])))
        # 보고서의 그림(f*.svg)도 옛 보고서 Lesson 에서 이어 받는다
        out_lessons.append((report_no, write_lesson(od, report_no, nu, "보고서 쓰기", [(t, sub(b), s) for t, b, s in report_pages])))
        lesson_paths = [p for _, p in sorted(out_lessons)]
        um = {"id": f"m3-u{nu:02d}", "title": utitle, "lessons": [{"path": p} for p in lesson_paths]}
        (od / "unit.md").write_text("---\n" + yaml.safe_dump(um, allow_unicode=True, sort_keys=False, width=1000) + f"---\n\n# {utitle}\n")
        units.append({"id": um["id"], "title": utitle, "path": f"exercises/module/3/unit/{nu:02d}/unit.md"})
    # course.yaml
    cy = yaml.safe_load((ROOT / "course.yaml").read_text())
    cy["units"] = units
    (ROOT / "course.yaml").write_text(yaml.safe_dump(cy, allow_unicode=True, sort_keys=False, width=1000))
    shutil.rmtree(UNIT); new_root.rename(UNIT)


def check():
    """새 구조에서 사람이 고쳐야 할 곳(옛 표현·TODO)을 찾는다."""
    bad = 0
    for f in sorted(ROOT.glob("unit/*/lesson/*/lesson.md")):
        for no, line in enumerate(f.read_text().split("\n"), 1):
            if re.search(r"TODO|Unit \d+ ?(까지|의|에서)|앞 실습 파일 완성본|「정답」 레슨", line):
                print(f"{f.relative_to(ROOT)}:{no}: {line.strip()[:100]}"); bad += 1
    print(f"{bad} lines to review")


if __name__ == "__main__":
    check() if "--check" in sys.argv else build()
