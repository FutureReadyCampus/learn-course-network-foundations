"""Serve the built staging reader with SPA-style deep links."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent / "dist"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path):
        clean = urlsplit(path).path.lstrip("/")
        candidate = ROOT / clean
        return str(candidate if candidate.is_file() else ROOT / "index.html")


ThreadingHTTPServer(("127.0.0.1", 15188), Handler).serve_forever()
