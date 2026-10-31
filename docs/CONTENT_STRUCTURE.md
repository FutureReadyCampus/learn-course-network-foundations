# Content structure

The source repository uses the learner-visible hierarchy **Unit → Lesson → Page**. URL position numbers are navigation only; they are not content IDs.

```text
units/
  01-unit-name/
    unit.md
    lessons/
      01-lesson-name/
        lesson.md
        assets/
          diagrams/
          animations/
```

- `course.yaml` orders Units. Each Unit's `unit.md` front matter lists its Lesson Markdown paths in learner order.
- Each Lesson's `lesson.md` front matter stores its existing stable ID, title, source reference, concepts, and media metadata. Each `##` heading begins a Page; the ordered `pages` list must match those headings one for one.
- Page metadata names its concepts, illustration positions, and any additional illustrations. Concept terms and authored animation descriptions stay with their concepts. Optional page media can use a stable selector when page order or headings may change.
- Store authored assets beside their Lesson and reference them with paths relative to `lesson.md`. The builder selects same-named shared runtime SVGs when available; Lesson-local playback copies live under `assets/animations/`. Keep imported Wiki snapshots under `sources/wiki/` and record their provenance.
- New Unit 1 Lessons keep page prose and page metadata together in Markdown. Existing Lessons that still use `source_wiki` or `page_metadata` remain supported while they are migrated.
- `scripts/build_course.py` reads these sources and builds the preview catalog. Do not hand-edit the generated preview catalog.

```mermaid
flowchart LR
    C[course.yaml] --> U[unit.md<br/>Unit order and Lesson paths]
    U --> L[lesson.md<br/>stable ID, prose, Page metadata]
    L --> P[## headings<br/>ordered Pages]
    L --> A[Lesson assets<br/>SVG and other media]
    P --> B[scripts/build_course.py]
    A --> B
    B --> R[preview catalog or Pages reader]
```

Public Network routes use `/m2-network/unit/{unit}/lesson/{lesson}/page/{page}`. The page number is one-based and follows the order of `##` headings. Stable Page IDs select source metadata only; they do not replace route numbers or Lesson progress IDs. Put the ID comment immediately after its `##` heading:

```markdown
## Wireshark에서 패킷 보기
<!-- learn-page-id: wireshark-packet-inspection -->
```

Add a matching item to the Lesson's `page_metadata` front matter. Video metadata requires a `page_id`; the builder checks that the ID matches exactly one Page and that `video_id` is an 11-character YouTube ID. The learner-facing title is used as the iframe's accessible name. `creator` and `duration_seconds` are optional descriptive metadata.

```yaml
page_metadata:
  - page_id: wireshark-packet-inspection
    video:
      video_id: vBrQ3yzerMg
      title: "[따라學IT] 01. 네트워크란 무엇인가? - 실습2(Wireshark)"
      creator: 따라하면서 배우는 IT
      duration_seconds: 512
```

Before introducing a new teaching pattern, inspect a real publisher-provided textbook sample and record its exact source and observed sequence in `docs/PEDAGOGY.md`. Describe our adaptation as an authoring decision, not as measured learning evidence.
