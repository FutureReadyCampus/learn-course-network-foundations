# learn-course-network-foundations
Markdown source for the Network Foundations course served by Learn

## Local preview

Use GitHub `main` for the current published-source view, or a GitHub PR head for a clearly labeled candidate review. Neither mode reads the current local branch:

```sh
python3 scripts/build_preview.py
python3 scripts/build_preview.py --pr 1
```

Each generated catalog records and displays the exact GitHub commit used. `preview/` is generated and ignored. A PR preview is a review candidate; only content merged to `main` is the published-source baseline.

## Unit 1 source

Each authored Unit lives under `units/NN-unit-name/`. Its `unit.md` lists Lesson source files under `lessons/NN-lesson-name/lesson.md`; each `##` heading in a Lesson is one learner-facing Page. Put Lesson-specific guides and media beside that Lesson under `assets/`.

Unit 1 follows the Wiki catalog. The authored Page text is in the Unit's Lesson Markdown. The original Wiki Markdown, beginner-guide JSON and source SVG files remain preserved under `sources/wiki/oeweo-network/` with references recorded in Lesson front matter. See [Content structure](docs/CONTENT_STRUCTURE.md).
