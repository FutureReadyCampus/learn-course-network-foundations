# Unit 1 provenance

This record identifies the archived inputs used for the Unit 1 migration. The source repository was `course-network`, at HEAD `90a5cc40dec981b0e37fa334f3fae8ba673c8f32` when its contents were imported on 2026-10-28.

That SHA identifies the source checkout's committed baseline. It does **not** identify all imported content: the Wiki lesson Markdown had uncommitted edits, and the beginner-guide JSON and animation SVG additions were untracked. Required guide and media assets are stored beside their owning Unit Lessons. The `archive SHA-256` values below identify the source snapshots used during migration, not upstream Git blobs.

The original source checkout currently has the same HEAD but a later, changed worktree. Its current copies of the four lesson Markdown files and JSON files differ from this repository's archived snapshots. Do not treat the current worktree as the historical import source; use the retained snapshots below for migration comparison.

## Archived Unit 1 inputs

| Archived source path | State at import | Destination or use | Archive SHA-256 |
|---|---|---|---|
| `lesson-01.md` | Tracked at baseline; uncommitted edits | `lessons/01-prerequisites/lesson.md` | `fa4df3c4e33f61aa55573d2ee01a7d28c32b7443c28f623a81a8bfc883487d01` |
| `lesson-02.md` | Tracked at baseline; uncommitted edits | `lessons/02-layered-structure/lesson.md` | `584b56b2577f9eda37df87ecc9304bfe522636fe4a286d0f7e21b25150509e36` |
| `lesson-03.md` | Tracked at baseline; uncommitted edits | `lessons/03-networking-concepts/lesson.md` | `f657e54da29944f621ba7990623d2ff2ca23ae4203cc81f736d2672d10bff79f` |
| `lesson-04.md` | Tracked at baseline; uncommitted edits | `lessons/04-user-and-kernel-mode/lesson.md` | `539b72376ff72503c0f46605a3749f60e503db4a6bd92c3b670ada698f1cc5ec` |
| `newbie/specs/lesson-01.json` | Tracked at baseline; uncommitted edits | Unit 1 Lesson 1 guide input | `a6ee23ad85c0f1149cf696444bfce9e4a2de74fca20a579d4ee6b28331f3a719` |
| `newbie/specs/lesson-02.json` | Untracked beginner-guide addition | Lesson 2 guide input | `5a75c1dd41c4ebfd7cddbce13b01b47f67f32bde3412263ff537bda7f3a1a46a` |
| `newbie/specs/lesson-03.json` | Untracked beginner-guide addition | Lesson 3 guide input | `f5a3cf351061bc0eb6cc02b82fb62dafbbe17e28d4a6259dacd180cc096d201b` |
| `newbie/specs/lesson-04.json` | Untracked beginner-guide addition | Lesson 4 guide input | `df20c110ed65b846f88e376aace104f04e46dbde3598f38f342390739629ffe6` |
| `concepts/lesson-01.svg` | Tracked at baseline; unchanged in source worktree at inspection | Lesson 1 concept diagram | `1d2b7b98c6afc783a4d63562c58772234bf5dbfb25a8b54cb6e4c644a6675060` |
| `concepts/lesson-02.svg` | Tracked at baseline; unchanged in source worktree at inspection | Lesson 2 concept diagram | `c024a5ee50aa3e7aa8139e0cddd3a04d48afa9ba262dd08a550fa5fa49fcea14` |
| `concepts/lesson-03.svg` | Tracked at baseline; unchanged in source worktree at inspection | Lesson 3 concept diagram | `7aa19fe3023cf921eb0b7c7ef37e56c2a74b6b70504b87c8f1b6cce53aa26ab8` |
| `concepts/lesson-04.svg` | Tracked at baseline; unchanged in source worktree at inspection | Lesson 4 concept diagram | `a70a5f0b343eb5c25cf6a1081dce47844f62adbcde2738c1e412dce76c9f9c9a` |
| `newbie/anim/l01-bits-bytes.svg` | Untracked beginner-guide addition | Lesson 1 authored animation | `80e1245c15039bfd19c1975401735d552dd0edda81212a781bfc703ad34c003b` |
| `newbie/anim/l01-and-mask.svg` | Untracked beginner-guide addition | Lesson 1 authored animation | `5e3961162932d42c8de630b7ee56c925791310997467ef4d5f90dfccd2d7d8be` |
| `newbie/anim/l01-binary-hex.svg` | Untracked beginner-guide addition | Lesson 1 authored animation | `fd16edcfcf7ca3723302c84e12b05d4845ae6ce38d1239258e1ecc729fe3f208` |
| `newbie/anim/l02-layer-dependency.svg` | Untracked beginner-guide addition | Lesson 2 authored animation | `e3e12e2665623b3a8fc24fa75d41492eb130c458659967fb3b54ee3d7db9ee6e` |
| `newbie/anim/l03-layers-dependency.svg` | Untracked beginner-guide addition | Lesson 3 authored animation | `4b789c0cc05ea72ce21f074673d089ce894d58a62d80044c3e7291437da5bab8` |
| `newbie/anim/l04-nic-driver-stack.svg` | Untracked beginner-guide addition | Lesson 4 authored animation; reused by Lessons 1 and 4 | `9d83a5787cf61677f575669c9611ce5f5b34dcf066e04648b47291a57803e8d4` |
| `newbie/anim/l04-socket-handset.svg` | Untracked beginner-guide addition | Lesson 4 authored animation | `d529334d9225185e791fb7b73d4c50fdf6ae28c2259df84a11006f667288b45b` |
| `newbie/anim/l04-layer-map.svg` | Untracked beginner-guide addition | Lessons 1–4 authored animation | `225805eec3c82a02f8685d56532aa351de55077503a3c1985544ed9d81835dac` |

Unit 1 migration destinations and asset placements are mapped in [unit1-content-mapping.md](unit1-content-mapping.md). Locally authored Lesson 1 diagrams are not from `course-network`; they remain attributable to this content repository's own history.
