"""공개 전 점검: 저장소에 올리면 안 되는 비밀 값과 개인정보를 찾습니다.

사용법: python check_publish.py [폴더]
오류가 하나라도 있으면 종료 코드 1, 아니면 0입니다.
예시 코드처럼 일부러 남긴 줄은 끝에 `# check_publish: ignore` 를 붙이면 건너뜁니다.
"""
import os
import re
import sys

SKIP_DIRS = {".git", "_site", ".venv", "venv", "node_modules", "__pycache__"}
MAX_SIZE = 1024 * 1024
IGNORE = "check_publish: ignore"

ERRORS = [
    ("개인 키 블록", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("AWS 액세스 키", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("GitHub 토큰", re.compile(r"(?:gh[pos]_|github_pat_)[A-Za-z0-9_]{16,}")),
    ("Anthropic 키", re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}")),
    ("OpenAI 스타일 키", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("Google API 키", re.compile(r"AIza[0-9A-Za-z_-]{35}")),
    ("Slack 토큰", re.compile(r"xox[baprs]-[A-Za-z0-9-]{8,}")),
    ("비밀 값 대입",
     re.compile(r"(?:API_KEY|SECRET|TOKEN|PASSWORD)[A-Za-z0-9_]*\s*[:=]\s*[\"']?([^\s\"']{20,})", re.I)),
]
WARNS = [
    ("이메일 주소", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")),
    ("휴대전화 번호", re.compile(r"010-\d{4}-\d{4}")),
]
PLACEHOLDERS = ("<내 아이디>", "내 이름")


def mask(value):
    return value[:4] + "***"


def scan_file(path, rel, out):
    try:
        if os.path.getsize(path) > MAX_SIZE:
            return
        with open(path, "rb") as f:
            data = f.read()
    except OSError:
        return
    if b"\0" in data:
        return
    text = data.decode("utf-8", "replace")
    is_config = os.path.basename(path) == "_config.yml"
    for no, line in enumerate(text.splitlines(), 1):
        if IGNORE in line:
            continue
        for kind, rx in ERRORS:
            m = rx.search(line)
            if m:
                out.append(("오류", rel, no, kind, m.group(1) if m.groups() else m.group(0)))
        for kind, rx in WARNS:
            m = rx.search(line)
            if m:
                out.append(("주의", rel, no, kind, m.group(0)))
        if is_config:
            for p in PLACEHOLDERS:
                if p in line:
                    out.append(("주의", rel, no, "예시 값이 그대로 남아 있음", p))


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    root = argv[0] if argv else "."
    found = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, root)
            if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
                found.append(("오류", rel, 0, ".env 파일은 올리면 안 됩니다", None))
                continue
            scan_file(path, rel, found)
    for level, rel, no, kind, value in found:
        where = "%s:%d" % (rel, no) if no else rel
        tail = " (찾은 값: %s)" % mask(value) if value else ""
        print("[%s] %s  %s%s" % (level, where, kind, tail))
    errs = sum(1 for f in found if f[0] == "오류")
    warns = len(found) - errs
    print("\n요약: 오류 %d건, 주의 %d건" % (errs, warns))
    if errs:
        print("다음 할 일: 이미 올린 키가 있다면 지우기 전에 해당 서비스에서 키부터 폐기하세요. "
              "그다음 파일에서 값을 빼고 다시 점검하세요.")
    elif warns:
        print("다음 할 일: 주의 항목이 공개해도 되는 내용인지 확인한 뒤 올리세요.")
    else:
        print("다음 할 일: 문제가 없습니다. 올려도 됩니다.")
    return 1 if errs else 0


if __name__ == "__main__":
    raise SystemExit(main())
