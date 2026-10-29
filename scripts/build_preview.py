#!/usr/bin/env python3
"""Build the local preview only from the GitHub origin/main commit."""

from __future__ import annotations

import json
import argparse
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "preview/learn-network-course.json"
ASSETS = ROOT / "preview/source-assets"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr", type=int, help="Preview the exact GitHub pull request head commit")
    args = parser.parse_args()
    ref = f"pull/{args.pr}/head" if args.pr else "main"
    label = f"PR #{args.pr} candidate" if args.pr else "GitHub main"
    subprocess.run(["git", "fetch", "origin", ref], cwd=ROOT, check=True)
    revision = subprocess.check_output(["git", "rev-parse", "FETCH_HEAD"], cwd=ROOT, text=True).strip()
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
                "version": f"network-{revision}",
                "title": "네트워크 기초",
                "units": [],
                "lessons": [],
                "limits": f"PREVIEW ONLY · {label} · not published",
                "preview_source": {
                    "label": label,
                    "sha": revision,
                    "url": f"https://github.com/FutureReadyCampus/learn-course-network-foundations/commit/{revision}",
                },
            }
            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            OUTPUT.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            if ASSETS.exists():
                shutil.rmtree(ASSETS)
            print(f"{label} {revision} has no course.yaml; preview contains no lessons.")
            return

        subprocess.run([
            "python3", str(source_root / "scripts/build_course.py"),
            "--output", str(OUTPUT), "--source-revision", revision, "--source-label", label,
        ], check=True)
        catalog = json.loads(OUTPUT.read_text(encoding="utf-8"))
        if ASSETS.exists():
            shutil.rmtree(ASSETS)
        ASSETS.mkdir(parents=True, exist_ok=True)
        prefix = "/api/v1/network-course-assets/"
        for lesson in catalog["lessons"]:
            for page in lesson["pages"]:
                for illustration in page.get("illustrations", []):
                    src = illustration["src"]
                    if not src.startswith(prefix):
                        raise ValueError(f"Unexpected network course asset URL: {src}")
                    relative = Path(src.removeprefix(prefix))
                    if relative.is_absolute() or ".." in relative.parts:
                        raise ValueError(f"Unsafe catalog asset path: {relative}")
                    source_asset = source_root / relative
                    if not source_asset.is_file():
                        raise FileNotFoundError(f"Missing catalog asset: {relative}")
                    destination = ASSETS / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source_asset, destination)
        print(f"Local preview generated from {label} {revision}.")


if __name__ == "__main__":
    main()
