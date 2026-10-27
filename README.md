# learn-course-network-foundations
Markdown source for the Network Foundations course served by Learn

## Local preview

The local Learn preview must use GitHub `main`, never the current local branch. Fetch and build its exact commit with:

```sh
python3 scripts/build_main_preview.py
```

This records the source commit in the generated catalog and serves no lessons when GitHub `main` has no course content. `preview/` is generated and ignored. The content in an unmerged pull request will not appear in this preview.

## Unit 1 source

Unit 1 follows the Wiki catalog. Its source Markdown, beginner-guide JSON and supplied SVG files are preserved under `sources/wiki/oeweo-network/`; the Learn catalog is generated from the Wiki reading editions.
