---
id: m5-u04-l12
title: 문제 해결 기록을 포트폴리오에 남기기
render: markdown
---

# 문제 해결 기록을 포트폴리오에 남기기

## 승인 기준과 복구 판단을 글로 남기기

핵심 실습에서 가장 고민했던 결정 하나를 골라 포트폴리오에 세 문장으로 남깁니다. 실행 출력과 상태는 `report_u4.md` 에 보관하고, 이 글에는 문제를 어떻게 이해하고 판단했는지 씁니다. 아직 GitHub Pages 블로그를 준비하지 않았다면 [M3 Unit 1의 Jekyll·GitHub Pages 설정 안내](__SITE__/exercises/module/3/unit/1/lesson/1/page/4)를 먼저 따라 합니다.

글감은 핵심 실습에서 하나 고릅니다.

1. 위험 점수와 대상 수를 함께 사용해 요청을 자동 · 승인 필요 · 차단 금지로 분류한 기준
2. 신고자의 정보만으로 계정을 복구하지 않고, 기록과 신고자 권한을 확인한 이유
3. 복구 시간이 기준을 넘거나 되돌릴 수 없는 조치가 남았을 때 담당자에게 전달할 내용

세 문장은 다음 순서로 씁니다.

1. 어떤 문제를 보았고, 출력이나 기록에서 무엇을 확인했는가?
2. 어떤 조건이나 대응을 선택했으며, 근거는 무엇이었는가?
3. 결과가 어떻게 달라졌고, 운영에서 다음에 무엇을 확인해야 하는가?

<!-- checklist -->
- [ ] 핵심 실습 하나를 골라 문제 · 판단 근거 · 결과를 세 문장으로 적었다
<!-- /checklist -->

틀이 필요하면 M3 Unit 1의 [글 틀 안내](__SITE__/exercises/module/3/unit/1/lesson/1/page/10)에서 `post-short` 또는 `post-stuck` 을 고릅니다.

## 글을 저장하고 올리기

1. 저장소 `network-study-notes` 의 `_posts` 폴더에서 오늘 날짜로 시작하는 새 Markdown 파일을 만듭니다. 예: `_posts/2026-11-25-m5-u4-approval-recovery.md`.
2. 글 틀을 붙여 넣고 머리말을 이 Unit에 맞게 씁니다.

   ```yaml
   module: 5
   unit: 4
   ```

3. 제목과 날짜를 바꾸고 세 문장을 저장합니다. 핵심 코드 몇 줄과 전체 파일 위치(`soar_response/approval_gate.py` 또는 `soar_response/false_positive.py`)를 적을 수 있습니다.
4. 저장소 루트에서 공개 전 점검을 실행하고 올립니다.

   ```bash
   python check_publish.py
   git status
   git add _posts/오늘-만든-파일.md
   git commit -m "Add M5 Unit 4 problem-solving record"
   git push
   ```

공개 전에 비밀키, `.env`, 토큰, 실제 사람의 개인정보가 들어 있지 않은지 확인합니다. 글이 사이트에 보이면 게시가 끝난 것입니다.

<!-- checklist -->
- [ ] 문제 해결 글을 게시하고 사이트에서 확인했다
<!-- /checklist -->
