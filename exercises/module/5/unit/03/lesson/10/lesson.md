---
id: m5-u03-l10
title: 문제 해결 기록을 포트폴리오에 남기기
render: markdown
---

# 문제 해결 기록을 포트폴리오에 남기기

## 핵심 실습에서 내린 판단을 글로 남기기

오늘 한 핵심 실습에서 가장 고민했던 판단 하나를 골라, 포트폴리오에 세 문장으로 남깁니다. 실행 출력과 파일 목록은 `report_u3.md` 에 보관하고, 이 글에는 문제를 어떻게 이해하고 해결했는지 기록합니다. 아직 포트폴리오가 없다면 [M3 Unit 1 시작하기의 「내 기록 남기기: 소개」 페이지](__SITE__/exercises/module/3/unit/1/lesson/1/page/4)부터 설정합니다.

아래 중 하나를 골라 씁니다.

1. 실습 3-1에서 `before` 와 `after` 를 비교해 조치 전부터 잠겨 있던 `junho` 계정을 그대로 둔 이유
2. 자동 조치로 생긴 상태만 되돌리고, 세션 종료는 사람이 이어서 확인하도록 남긴 이유
3. 실습 3-2의 응답 기한과 직접 확인 표시가 담당자에게 알려 주는 것

세 문장은 다음 순서로 씁니다.

1. 어떤 문제가 있었고, 출력에서 무엇을 확인했는가?
2. 어떤 조건이나 구현을 선택했으며, 근거는 무엇이었는가?
3. 결과가 어떻게 달라졌고, 실제 업무에서 무엇을 확인해야 하는가?

틀을 고르는 데 막히면 M3 Unit 1의 [글 틀 안내](__SITE__/exercises/module/3/unit/1/lesson/1/page/10)에서 `post-short` 또는 `post-stuck`을 씁니다.

<!-- checklist -->
- [ ] 핵심 실습 하나를 골라 문제 · 판단 근거 · 결과를 세 문장으로 적었다
<!-- /checklist -->

## 글을 저장하고 올리기

1. 저장소 `network-study-notes` 의 `_posts` 폴더에서 오늘 날짜로 시작하는 새 Markdown 파일을 만듭니다. 예: `_posts/2026-11-25-m5-u3-rollback-ticket.md`.
2. 글 틀을 붙여 넣고 머리말을 이 Unit에 맞게 씁니다.

   ```yaml
   module: 5
   unit: 3
   ```

3. 제목과 날짜를 고치고 세 문장을 저장합니다. 글 안에는 핵심 코드 몇 줄과 전체 파일 위치(`soar_response/rollback.py` 또는 `soar_response/ticketing.py`)를 함께 적을 수 있습니다.
4. `network-study-notes` 저장소 루트에서 공개 전 점검을 실행하고 올립니다.

   ```bash
   python check_publish.py
   git status
   git add _posts/오늘-만든-파일.md
   git commit -m "Add M5 Unit 3 problem-solving record"
   git push
   ```

공개 전에 비밀키, `.env`, 토큰, 실제 사람의 개인정보가 들어 있지 않은지 확인합니다. 글이 사이트에 보이면 게시가 끝난 것입니다.

<!-- checklist -->
- [ ] 문제 해결 글을 게시하고 사이트에서 확인했다
<!-- /checklist -->
