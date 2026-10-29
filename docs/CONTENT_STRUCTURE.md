# Content structure

The source repository uses the learner-visible hierarchy **Unit → Lesson → Page**. URL position numbers are navigation only; they are not content IDs and do not appear in source paths.

```text
units/
  01-unit-name/
    unit.md
    lessons/
      01-lesson-name/
        lesson.md
        guide.json          # optional structured terms, questions, or interactions
        assets/
          diagrams/
          animations/
```

- `course.yaml` orders Units. A Unit's `unit.md` front matter gives it a stable ID and lists its Lesson source paths in order.
- Each Lesson's `lesson.md` front matter gives it a stable ID, title, and source references. Its `##` headings define Pages in learner reading order. Write Page content directly here; do not generate it by splitting Wiki headings.
- Store assets beside the Lesson that uses them. Keep authored Wiki Markdown and source diagrams under `sources/wiki/` and record their paths in Lesson front matter. Put per-Page terms and selected animation metadata in the Lesson front matter instead of a separate guide JSON when editing that Lesson.
- Use stable semantic IDs for Unit, Lesson, activities, and questions. Reordering a Lesson or Page changes its numeric URL position but does not change those IDs.
- Public Network routes use `/m2-network/unit/{unit}/lesson/{lesson}/page/{page}`. The retired `chapter/lesson/step` route is invalid. The page number is one-based and follows the order of `##` headings.
- `scripts/build_course.py` builds the runtime catalog from this structure. Do not hand-edit the generated preview catalog.

Before introducing a new teaching pattern, inspect a real publisher-provided textbook sample and record its exact source and observed sequence in `docs/PEDAGOGY.md`. Describe our adaptation as an authoring decision, not as measured learning evidence.
