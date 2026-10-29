# Unit 1 source-to-Lesson mapping

This inventory records the Unit 1 working copy used for migration, including its uncommitted edits. It does not claim that every source file came from the recorded upstream commit.

Page counts below match each target Lesson Markdown file’s `##` headings and its ordered `pages` metadata.

| Lesson ID | Current Markdown → target | Current guide JSON → target | Pages | Concept SVG → target |
|---|---|---|---:|---|
| `u1-prerequisites` | `sources/wiki/oeweo-network/lesson-01.md` → `units/01-before-networking/lessons/01-prerequisites/lesson.md` | the working `lesson-01-guide.json` input → Lesson front matter (merged into the Lesson; no duplicate sidecar retained) | 5 | `sources/wiki/oeweo-network/concepts/lesson-01.svg` → `lessons/01-prerequisites/assets/lesson-01.svg` |
| `u1-layers` | `sources/wiki/oeweo-network/lesson-02.md` → `units/01-before-networking/lessons/02-layered-structure/lesson.md` | `sources/wiki/oeweo-network/newbie/specs/lesson-02.json` → Lesson front matter (Guide prose is in the Markdown body) | 2 | `sources/wiki/oeweo-network/concepts/lesson-02.svg` → `lessons/02-layered-structure/assets/lesson-02.svg` |
| `u1-networking` | `sources/wiki/oeweo-network/lesson-03.md` → `units/01-before-networking/lessons/03-networking-concepts/lesson.md` | `sources/wiki/oeweo-network/newbie/specs/lesson-03.json` → Lesson front matter (Guide prose is in the Markdown body) | 2 | `sources/wiki/oeweo-network/concepts/lesson-03.svg` → `lessons/03-networking-concepts/assets/lesson-03.svg` |
| `u1-user-kernel` | `sources/wiki/oeweo-network/lesson-04.md` → `units/01-before-networking/lessons/04-user-and-kernel-mode/lesson.md` | `sources/wiki/oeweo-network/newbie/specs/lesson-04.json` → Lesson front matter (Guide prose is in the Markdown body) | 3 | `sources/wiki/oeweo-network/concepts/lesson-04.svg` → `lessons/04-user-and-kernel-mode/assets/lesson-04.svg` |

## Lesson media

The following authoring SVGs were copied into each owning Lesson's `assets/` folder with their filenames preserved. Reused files are copied into each Lesson so each Lesson remains self-contained. The retained source copies remain under `sources/` for provenance.

| Lesson ID | Authoring SVGs → `lessons/<folder>/assets/` |
|---|---|
| `u1-prerequisites` | From `sources/wiki/oeweo-network/newbie/anim/`: `l01-bits-bytes.svg`, `l01-and-mask.svg`, `l01-binary-hex.svg`, `l04-nic-driver-stack.svg`, `l04-layer-map.svg`. From the Unit 1 working copy’s locally authored animation folder: `l01-number-bases-fingers.svg`, `l01-program-process.svg`, `l01-osi-seven-layers.svg`, `l01-buffer-parcels.svg`. |
| `u1-layers` | From `sources/wiki/oeweo-network/newbie/anim/`: `l02-layer-dependency.svg`, `l04-layer-map.svg`. |
| `u1-networking` | From `sources/wiki/oeweo-network/newbie/anim/`: `l03-layers-dependency.svg`, `l04-layer-map.svg`. |
| `u1-user-kernel` | From `sources/wiki/oeweo-network/newbie/anim/`: `l04-nic-driver-stack.svg`, `l04-socket-handset.svg`, `l04-layer-map.svg`. |

`anim-paced/` contains display-timed derivatives of the source-provided authoring SVGs. The builder uses those runtime copies for the reader while the unmodified authoring SVGs stay beside their Lessons. Lesson 1 also retains four stage-badged local runtime copies under `assets/animations/` for its locally authored animations. The initial 0.3× review derivatives were removed, and playback settings remain in `docs/svg-playback.yaml`.

## Metadata to carry forward

- Keep the four Lesson IDs in `lesson.md` front matter and the Unit ID in `unit.md`.
- Page grouping, concept IDs and terms, authored animation metadata, illustration placement, alt text, and captions are now recorded in Lesson front matter. The ordered `pages` metadata matches the `##` Page heading order. The Guide `note` prose already matches the Lesson body and is not duplicated in front matter.
- SVG file references point to the Lesson `assets/` copies. Source-provided SVGs remain in `sources/`; the locally authored Lesson 1 SVGs now live beside that Lesson.
- The current Page model has no persistent Page ID; preserve heading order and do not manufacture IDs during this move.

This map records the completed Unit 1 migrations and their retained archive locations. The retained `sources/` archive remains available for later Units 2–10 mapping and any repository-level cleanup decision.

Comparison results, including the Lesson 1 archived-versus-working Guide differences, are recorded in [unit1-migration-comparison.md](unit1-migration-comparison.md).

## Remaining content and `sources/` cleanup scope

Units 2–10 still have catalog and Unit placeholders but no migrated Lesson folders. The current `sources/wiki/oeweo-network/` archive contains four Wiki Lesson Markdown files, the Unit catalog, four concept diagrams, four Unit 1 Guide JSON files, 89 authored animation SVGs, and 89 `anim-paced/` derivatives. Unit 1 references eight of the 89 authored animation SVGs; the other 81 are not yet assigned by the migrated Unit 1 content and may be needed while Units 2–10 are mapped.

`course.yaml`, `units/01-before-networking/unit.md`, and `scripts/build_course.py` still point to paths under `sources/`. Therefore the cleanup decision for this issue is:

1. Keep `sources/` intact for now; do not remove it as part of the Unit 1 content migration.
2. In the separate build/import work, remove build and preview dependencies on `sources/` and generate or resolve timed SVG derivatives from the Lesson assets.
3. When Units 2–10 are mapped, copy only referenced authored assets into their Lessons and identify remaining archive material.
4. After those references are gone and remaining material has an explicit disposition, remove the redundant source mirrors from the active content tree. Keep the provenance and migration-comparison records as the compact history of Unit 1.

This is a cleanup scope decision, not a deletion of `sources/`.
