# Network Foundations course content

Markdown source for the Network Foundations course served by Learn. `main` is
the reviewed content source for Learn; `stage` publishes a public static reader
for reviewing the course outside Learn.

## Local preview

Use GitHub `main` for the current published-source view, or a GitHub PR head for a clearly labeled candidate review. Neither mode reads the current local branch:

```sh
python3 scripts/build_preview.py
python3 scripts/build_preview.py --pr 1
```

Each generated catalog records and displays the exact GitHub commit used. `preview/` is generated and ignored. A PR preview is a review candidate; only content merged to `main` is the published-source baseline.

## Public staging reader

Every push to `stage` builds the Markdown catalog and SVG assets, then publishes
the static reader to GitHub Pages. The reader identifies the branch and exact
source commit. Open the staging site at:

<https://futurereadycampus.github.io/learn-course-network-foundations/>

To preview locally:

```sh
python3 scripts/build_pages.py --source-revision local --source-label 'stage local preview'
python3 site/local_server.py
```

Learn deployment remains a separate release path from the `stage` Pages site.

## Unit 1 source

Each authored Unit lives under `units/NN-unit-name/`. Its `unit.md` lists Lesson source files under `lessons/NN-lesson-name/lesson.md`; each `##` heading in a Lesson is one learner-facing Page. Put Lesson-specific guides and media beside that Lesson under `assets/`.

Unit 1 follows the Wiki catalog. The authored Page text is in the Unit's Lesson Markdown. Each Lesson owns its guides, diagrams, authored animation sources and runtime animations under its `assets/` folder. Source attribution links to the original Wiki revision. See [Content structure](docs/CONTENT_STRUCTURE.md).
