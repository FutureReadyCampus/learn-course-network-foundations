---
id: m3-u02-l01
title: 준비 · 내 작업 폴더 열기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/077_day02_morning_seat_change.md
  mission_id: GichanSource.m3-1022-morning-seat-change
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 준비 · 내 작업 폴더 열기

## Unit 1 작업 이어서 하기

핵심 실습 전에 [블로그 초안 준비](__SITE__/exercises/module/3/unit/2/lesson/1/page/2)에서 이번 유닛의 글 파일을 엽니다.

Unit 1에서 사용한 내 컴퓨터와 저장소 `network-study-notes` 를 그대로 사용합니다. VS Code에서 **File › Open Folder** 를 누르고 `network-study-notes` 폴더를 엽니다. 저장소를 찾지 못하면 Unit 1 「시작하기」에서 저장소를 내려받은 위치를 확인하세요.

VS Code에서 **Terminal › New Terminal** 을 열고 터미널이 **Git Bash** 인지 확인합니다. 다음 명령으로 Unit 1의 작업 폴더에 들어갑니다.

```bash
cd access_control
pwd
```

`pwd` 결과가 `access_control` 로 끝나면 준비됐습니다. 이미 그 폴더에 있다면 `cd access_control` 을 다시 입력할 필요는 없습니다. 이제 다음 레슨 「시작하기」로 갑니다.

<!-- checklist -->
- [ ] VS Code에서 내 `network-study-notes` 폴더를 열고 Git Bash의 현재 위치가 `access_control` 인지 확인했다
<!-- /checklist -->

## 블로그 초안 준비

VS Code에서 저장소 `network-study-notes`를 엽니다. 블로그를 처음 설정한다면 [GitHub Pages 설정 안내](__SITE__/exercises/module/3/unit/1/lesson/1/page/4)를 먼저 따라 하세요.

1. 저장소 바로 아래에 `_posts` 폴더를 만듭니다. 이미 있으면 그 폴더를 엽니다.
2. **New File**을 누르고 `2026-11-20-m3-u2-request-review.md`처럼 이름을 짓습니다. 앞의 날짜는 오늘 날짜로 바꿉니다. 이번 유닛 글이 이미 있으면 그 파일을 이어 씁니다.
3. 새 파일에만 아래 틀을 복사하고 `date`를 파일명의 날짜와 맞춥니다. `published: false`는 초안을 블로그 목록에서 숨깁니다. GitHub에 올린 원본은 저장소에서 읽을 수 있으니 실습 데이터만 씁니다.

<pre class="copyable"><code>---
layout: post
title: "승인된 요청과 반려된 요청에서 어떤 값이 달랐나요?"
date: 2026-11-20
module: 3
unit: 2
published: false
---

&#35;# 문제

&#35;# 선택과 이유

&#35;# 검증 결과
</code></pre>

<h2>핵심 실습에서 고를 글감</h2>

1. 승인된 요청과 반려된 요청에서 어떤 값이 달랐나요?
2. 권한을 부여하기 전에 승인을 확인하는 이유는 무엇인가요?

하나를 골라 제목을 고칩니다. 실습 중에는 그 질문과 연결되는 입력과 출력 한두 줄을 ‘검증 결과’ 아래에 모으세요. 기존 실습 기록(`report_u2.md`)이 있다면 직접 확인한 근거 하나를 가져와 이어 씁니다.

<!-- checklist -->
- [ ] 이번 유닛의 글 파일을 열고 확인하고 싶은 질문을 제목에 적었다
<!-- /checklist -->
