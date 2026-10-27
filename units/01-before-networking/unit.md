---
id: before-networking
title: 들어가기에 앞서...
status: draft
source:
  repository: course-network
  path: studio/wiki/oeweo-network/catalog.json
  section: 기초편 1. 들어가기에 앞서...
---

# 들어가기에 앞서...

## 이 Unit의 목적

네트워크를 처음 배우는 사람이 컴퓨터의 정보와 작동 방식을 낯설어하지 않도록 바탕부터 익힌다. 앞서 알고 있어야 한다고 적힌 내용을 선행 지식으로 남겨 두지 않고, 이 Unit 안에서 차근차근 배운다.

## 출처 범위

Wiki 기초편 1번 대분류의 원본 항목 1–5와 왕초보 길잡이 `lesson-01.json`–`lesson-04.json`을 조사 대상으로 삼는다. 원본 항목의 순서는 유지하되, 겹치는 주제는 반복 설명하지 않고 한 학습 흐름으로 묶는다.

- 원본 1: 강의소개 — Unit 안내로 요약하는 방안
- 원본 2: 수강 전에 알고 있다고 가정하는 것들 — 정보를 나타내는 방법부터 실제 Lesson으로 풀기
- 원본 3: Layer와 Layered 구조 — OSI 이야기와 중복되지 않도록 통합 검토
- 원본 4: 네트워크와 네트워킹 그리고 개념 — 네트워크와 네트워킹의 차이를 배우기
- 원본 5: User mode와 Kernel mode — 운영체제 역할과 네트워크 기능이 놓이는 위치를 설명

## Lesson 구성 초안

Wiki 원본 순서를 유지하고 겹치는 선수 개념은 본 Lesson 경로에 한 번만 배치한다. Lesson 경계와 제목은 첫 Lesson을 검토한 뒤 확정한다.

1. 정보 표현의 단위: bit와 byte
2. 논리 연산과 마스크
3. 2진수와 16진수
4. 프로그램·프로세스·PID 구분
5. 계층과 OSI: Layer 개념을 먼저 익히고, Unit 2에서 식별자와 동작을 확장
6. 네트워크와 네트워킹 구분
7. User mode와 Kernel mode, 장치 드라이버와 소켓
8. 버퍼와 버퍼링
9. 개념과 구현

Wiki의 `강의소개`는 학생 완료 기록이 생기는 Lesson으로 만들기보다 Unit 안내에 흡수하는 안을 검토한다. Wiki의 Layer, Network/Networking, User/Kernel 설명은 위 경로의 관련 Lesson에 통합해 반복을 줄인다.

## 초안에서 보류한 범위

- `강의소개` 원본 항목을 완료 기록이 생기는 학생 Lesson으로 만들지, Unit 안내에 흡수할지
- byte 용량 단위와 1,000/1,024 기준을 어느 Lesson에서 설명할지
- 응용편에서 기초 개념을 다시 가르칠지, 앞 Unit으로 연결할지
- 영구 Lesson ID와 Learn 완료 기록의 대응

## 첫 시범 Lesson

`lessons/01-bits-and-bytes/lesson.md`에서 bit와 byte만 다룬다. 나머지 선수 지식 8개를 한 번에 소개하지 않는다.
