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

Unit 1 follows the Wiki catalog. Its source Markdown, beginner-guide JSON and supplied SVG files are preserved under `sources/wiki/oeweo-network/`; the Learn catalog is generated from the Wiki reading editions.
