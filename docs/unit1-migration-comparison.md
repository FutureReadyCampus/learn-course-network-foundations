# Unit 1 migration comparison

This comparison covers the current Unit 1 working inputs and their Lesson destinations. It distinguishes the retained source archive from later working edits.

## Lesson prose and Page order

| Lesson | Reading-edition sections | Target `##` Pages | Result |
|---|---:|---:|---|
| `u1-prerequisites` | 5 | 5 | Section body text matches the migrated Lesson body; section headings now define Pages. |
| `u1-layers` | 2 | 2 | Section body text matches the migrated Lesson body; section headings now define Pages. |
| `u1-networking` | 2 | 2 | Section body text matches the migrated Lesson body; section headings now define Pages. |
| `u1-user-kernel` | 3 | 3 | Section body text matches the migrated Lesson body; section headings now define Pages. |

The comparison uses the four `reading-edition` sections identified in [unit1-content-mapping.md](unit1-content-mapping.md). Other source sections remain in `sources/` and were not treated as part of these four Learn Lessons.

## Guide prose and metadata

The current Guide working inputs have 49, 24, 29, and 35 `note` paragraphs for Lessons 1–4. Every paragraph is present in that Lesson's Markdown body. The note prose was therefore not duplicated into front matter.

Concept IDs, terms and definitions, authored animation descriptions, `tryit` data, Page concept groups, selected concepts, illustration positions, and authored illustration titles, alt text, captions, and paths were carried into Lesson front matter. The ordered `pages` lists have the same counts as the `##` headings. Asset references were rewritten to `assets/<filename>.svg`.

### Lesson 1 archive versus working copy

The retained `sources/.../newbie/specs/lesson-01.json` is an earlier archive snapshot than the current working input `units/01-before-networking/lesson-01-guide.json`. The archived JSON has 42 note paragraphs; the working input and migrated body have 49. Of the archived paragraphs, 35 match the migrated body exactly; the remaining source wording was revised or expanded in the current working version. The target preserves that current version.

These Guide fields also differ between the archive and the current working input:

- `concept-basic-01-02`: `note`, `terms`
- `concept-basic-01-04`: `anim`, `additional_anims`
- `concept-basic-01-05`: `note`, `anim`
- `concept-basic-01-06`: `anim`
- `concept-basic-01-08`: `note`, `terms`, `anim`
- `concept-basic-01-09`: `note`

The working input was used for the target front matter, preserving the local edits. The earlier archived file remains untouched for provenance.

The working Lesson 1 guide input was merged into the Lesson front matter and removed as a duplicate after this comparison. Its earlier archive snapshot remains under `sources/wiki/oeweo-network/newbie/specs/`.

## SVG assets

Twenty SVG files were copied to the four Lesson `assets/` folders: 10, 3, 3, and 4 respectively. Each copy was checked against its immediate source and is byte-for-byte identical. Reused authoring SVGs have a copy in each owning Lesson. Every SVG path in the Lesson front matter resolves to a file.

`anim-paced/` contains timed display derivatives and remains separate from the authored SVGs. Unit 1 archive files remain in `sources/` for provenance; the four locally authored Lesson 1 diagrams now live in that Lesson’s `assets/` folder.

## Result

No missing current Lesson prose, Guide note paragraphs, mapped Page metadata, or referenced SVGs were found in this comparison. The identified Lesson 1 archive/working-copy differences are recorded above; they are preserved rather than silently replacing the current working edits with the older archive snapshot.
