# Unit 1 source and presentation

Unit 1 preserves the Wiki reading-edition sequence rather than introducing a new teaching pattern. The authored Learn text lives in the matching Unit Lesson Markdown so later edits do not depend on rebuilding from Wiki headings. Lesson front matter links to the exact source Wiki revision. Guides, diagrams and animation assets live beside the Lesson that uses them.

This records a source migration and authoring choice. It does not claim measured learning gains or establish a new teaching pattern.

The Unit 1 opening adapts the sequence in 혼자 공부하는 네트워크, Chapter 1, §01-1, “컴퓨터 네트워크를 알아야 하는 이유” (pp. 28–35; [publisher preview](https://fliphtml5.com/hkuy/rhmq/%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1_%E1%84%80%E1%85%A9%E1%86%AB%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%A6%E1%84%90%E1%85%B3%E1%84%8B%E1%85%AF%E1%84%8F%E1%85%B3_%E1%84%86%E1%85%B5%E1%84%85%E1%85%B5%E1%84%87%E1%85%A9%E1%84%80%E1%85%B5/)). The preview introduces networks and the Internet, explains how network knowledge supports building and maintaining programs, gives practical examples, and then broadens to network structure. Unit 1 adapts that progression into a short opening about communication and troubleshooting, followed by the existing four-Lesson sequence. This is an authoring choice, not a claim of measured learning gains.

# Unit 11 advanced-course opening

Unit 11's eight-Page guide follows one fictional club event-registration service from its first connection problem through traffic distribution and remote administration. It uses the development and maintenance examples in 혼자 공부하는 네트워크, Chapter 1, §01-1, pp. 30–33 ([HANBIT publisher preview](https://fliphtml5.com/hkuy/rhmq/)), as a reference for connecting network knowledge to practical questions. The sample introduces development, deployment, stability/security, and troubleshooting uses before moving to the larger network picture; it does not supply our club-service story. The story, the two comparison/roadmap tables, and the transition sentences in Unit 11's technical Lessons are our authoring choices, not claims of measured learning gains.

The guide keeps its existing Lesson ID and eight ordered Pages; the technical Lessons keep their Page boundaries. The old introductory outline SVG remains in the source archive but is no longer attached to the guide. The separate advanced-restructure snapshot remains unchanged: its byte/content hashes no longer describe these revised sources, so a future restructure must review the source revision and mapping again before using that preflight contract. This content revision does not implement the proposed resource separation, route migration, or progress transfer.

# Unit 11 technical Lessons

The five technical Lessons retain the approved Page order and stable Page IDs while expanding the explanations and adding two Page-level questions per Page. Their examples follow one fictional club event-registration service; the examples are an authoring choice, not a claim about a particular deployed system.

The inline-structure, out-of-path/DPI, forward-proxy, client-protection, local-proxy and reverse-proxy explanations were checked against the archived advanced-course source at `physical-spark/course-network` revision `d1b650e39cb0fd01f4b67adb76926172dbd517c9`: `studio/wiki/oeweo-network/advanced/lesson-03.md`, `lesson-05.md`, `lesson-06.md`, `lesson-07.md`, `lesson-08.md`, and `lesson-09.md`. Existing matching diagrams remain attached to their corresponding Pages.

The forward/reverse-proxy distinction was also compared with 혼자 공부하는 네트워크, Chapter 7, §07-1, “포워드 프록시와 리버스 프록시,” pp. 391–392, in the same course-network source revision. The relevant source anchors are `p391-b03`–`p391-b23` and `p392-b01`–`p392-b16`; the Lesson front matter links to the source section. The book informs the client-side versus origin-server-side explanation and comparison, while the club-service scenes and wording are newly authored. No extended passage or figure from the book is reproduced.

The revised text distinguishes packet forwarding from socket Stream processing; passive copied-traffic observation from active intervention; and TLS encryption from authorized TLS termination or inspection. It treats device performance, packet loss, logging and traffic collection as configuration-dependent concerns. This records the sources and authoring choices; it does not claim measured learning gains.
