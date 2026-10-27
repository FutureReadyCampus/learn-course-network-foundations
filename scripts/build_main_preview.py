#!/usr/bin/env python3
"""Build the local preview only from the GitHub origin/main commit."""

from __future__ import annotations

import json
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "preview/learn-network-course.json"
ASSETS = ROOT / "preview/main-assets"


def main() -> None:
    subprocess.run(["git", "fetch", "origin", "main"], cwd=ROOT, check=True)
    revision = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip()
    with tempfile.TemporaryDirectory(prefix="network-main-") as temporary:
        archive_path = Path(temporary) / "main.tar"
        with archive_path.open("wb") as archive:
            subprocess.run(["git", "archive", revision], cwd=ROOT, stdout=archive, check=True)
        source_root = Path(temporary) / "source"
        source_root.mkdir()
        with tarfile.open(archive_path) as archive:
            archive.extractall(source_root)

        if not (source_root / "course.yaml").exists():
            catalog = {
                "version": f"github-main-{revision}",
                "title": "네트워크 기초",
                "units": [],
                "lessons": [],
                "limits": "GitHub main has no course content at this commit.",
            }
            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            OUTPUT.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"GitHub main {revision} has no course.yaml; preview contains no lessons.")
            return

        if ASSETS.exists():
            shutil.rmtree(ASSETS)
        ASSETS.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source_root / "sources", ASSETS / "sources")
        subprocess.run([
            "python3", str(source_root / "scripts/build_course.py"),
            "--output", str(OUTPUT), "--source-revision", revision,
        ], check=True)
        print(f"Local preview generated from GitHub main {revision}.")


if __name__ == "__main__":
    main()
