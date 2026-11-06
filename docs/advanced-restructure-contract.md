# 심화 재편: 자료·주소·기록의 적용 전 계약

[콘텐츠 #163](https://github.com/FutureReadyCampus/learn-course-network-foundations/issues/163) · [Learn #223](https://github.com/FutureReadyCampus/learn/issues/223)

이 문서는 **구조 적용 전 계약과 읽기 전용 검증 결과**다. 실제 목차는 14 Unit이며 안내·자료도 아직 기존 Lesson으로 제공된다. 아래 ID·라우트·자료 필드는 후속 구현에 사용할 명세다. 현재 빌더·API·화면이 이를 소비하거나 기록을 승계한 것은 아니다. 원문 집필·퀴즈·SVG·glossary 수정은 포함하지 않는다.

## 기준과 재현

- 원문 기준: [기존 스냅샷](advanced-restructure-snapshot.json)의 콘텐츠 `4269969b0021fa85a3ab55c73c1dde6a66334c75`.
- 현행 소스 대조: 콘텐츠 stage `5738ad552a5737ea061b304de60594dfaa05a5d1`. 심화 23개 파일·203개 Page JSON·22개 SVG 해시가 기존 스냅샷과 같아야 계획을 만들 수 있다.
- Learn 조사: `b8f7e877fd17c7d6c22e7c3f549aa5add5b34678` main. `network_routes.py`, `network_compat.py`, `network_mastery.py`, `models.py`, `platform.py`, 두 builder와 importer, `NetworkCourse.tsx`, `usePageProgress.ts`의 저장·이동 경로를 기준으로 했다.
- 기계 판독 명세: [advanced-restructure-contract.json](advanced-restructure-contract.json). `target_key`는 감사 키이고 `lesson_id`가 후속 적용 ID다. 아직 게시된 ID는 아니다.

```sh
python3 scripts/build_course.py --source-revision "$(git rev-parse HEAD)" \
  --output preview/restructure-source.json
python3 scripts/plan_advanced_restructure.py \
  --catalog preview/restructure-source.json \
  --learn-root /path/to/reviewed/learn \
  --output preview/advanced-restructure-plan.json
python3 scripts/test_advanced_restructure.py -v
```

출력은 `preview/`의 계획 파일 하나다. DB 연결·기록 갱신·카탈로그 덮어쓰기·게시 설정 변경 기능은 없다. `--learn-root`를 주면 Learn의 실제 builder로도 23개 원고의 Page JSON을 대조하고, 고정한 구주소 Lesson 표와 일치하는지 검사한다. 생략하면 Learn 대조를 수행했다고 기록하지 않는다. 보고서의 `runtime_ready`는 항상 `false`다.

## 1. Lesson·Page ID

- 내용 범위가 그대로인 11개 Lesson은 기존 ID를 유지한다. 제목이나 위치 변경만으로 ID를 바꾸지 않는다.
- 병합·분할한 9개 Lesson은 새 ID를 사용한다. 기존 완료 행 하나가 새 전체 Lesson의 완료로 잘못 읽히는 것을 막기 위해 기존 ID를 재사용하지 않는다.
- 원본 Page 203개에 기존 안정 ID가 없으므로 `advanced-source-{원고순번 두 자리}-page-{기존 Page 두 자리}`를 배정한다. 원고순번은 **고정 스냅샷의 1~23**이며 새 목차 순번이 아니다. 병합·분할 후에도 같은 원본은 같은 Page ID를 쓴다.
- 후속 본문 편집으로 원문 범위나 문항 계약이 달라지면 이 계획으로 자동 승계하지 않는다. 검토한 스냅샷과 적용 대상 SHA를 다시 고정해야 한다.

| 목표 | 후속 Lesson ID | 원고 |
| --- | --- | --- |
| U11L4 | `advanced-forward-proxy` | 구 U11L6·7·9 |
| U12L3 | `advanced-nat-mapping-filtering` | 구 U12L3·4·5 |
| U13L1 | `advanced-l4-load-balancing` | 구 U13L1 P1~7 |
| U13L2 | `advanced-service-redundancy` | 구 U13L1 P8~11; P10~11은 참고 역할 보존 |
| U14L3 | `advanced-remote-access-vpn` | 구 U14L3·4 |
| U15L1 | `advanced-security-placement` | 구 U14L5 P1~5 |
| U15L2 | `advanced-network-access-control` | 구 U14L5 P6~9 |
| U15L3 | `advanced-stateful-firewall` | 구 U14L5 P10~13 |
| U15L4 | `advanced-intrusion-and-logs` | 구 U14L5 P14~20 |

나머지 11개 기존 ID는 JSON 명세에 있다. 기본편 ID·원고·질문 집합은 그대로 둔다.

## 2. 안내·PDF 전달

후속 카탈로그 루트에 `resources`를 두고, 각 항목은 `id`, `kind`, `title`, `required: false`, `source_lesson_id`, `source_wiki`, `links`, `pages`를 전달한다. `pages`에는 현재 builder가 만든 제목·문단·그림 정보를 그대로 보존하고 안정 Page ID와 원본 Page 해시를 덧붙인다.

| 자료 ID | 종류 | 원고 | 후속 주소 |
| --- | --- | --- | --- |
| `advanced-guide` | `guide` | 구 U11L1의 8 Page | `/m2-network/resources/advanced-guide/page/{1~8}` |
| `advanced-materials` | `materials` | 구 U11L4의 1 Page·PDF 원본 링크 2개 | `/m2-network/resources/advanced-materials/page/1` |

후속 구현은 다음을 함께 충족해야 한다.

1. 자료를 `lessons`, `lesson_outline`, `published_path`, 선행 Lesson 검사, 완료 분모에 넣지 않는다. 필수 안내 퀴즈나 PDF 열람 완료 체크를 만들지 않는다.
2. 개요·사이드바에서 별도 ‘심화 안내·참고 자료’ 링크로 찾을 수 있게 하고 자료 상세에서 목차로 돌아갈 수 있게 한다. 기존 안내 첫 Page의 개요에서 나머지 원문으로 이어지게 하며 기술 Lesson 진입 장벽을 두지 않는다.
3. Unit의 공개 설정과 자료 노출 설정을 혼동하지 않는다. 현재 비공개 자료를 구조 이동만으로 공개하지 않는다. 별도 노출 설정이 마련되기 전에는 기존 원고의 공개 여부를 따르고 관리자 미리보기를 유지한다.
4. importer가 resource Page의 그림도 검증·복사하고 출처 manifest에 기록해야 한다. learner API로 자원 본문이 전달되고 실제 화면에 보이는 것까지 확인한다. `unit.md`에 링크만 옮기는 것은 완료가 아니다.
5. PDF 두 개는 기존 원본 URL을 그대로 남긴다. 다운로드하거나 공개 복사하지 않았으며 접근 가능성·권한은 **미확인**이다. 공개 자료 화면을 배포할 때 로그인/권한 안내와 실제 링크 응답을 확인해야 한다.

이 단계의 계획 출력에는 8+1 Page payload가 만들어지지만 현재 카탈로그나 화면에는 추가하지 않는다.

## 3. 주소와 읽던 위치

**재편 후 표준 주소는 `/m2-network/v3/unit/...`로 구별한다.** 현재 `/v2`는 14 Unit 목차의 기존 위치를 의미하도록 고정한다. Unit이 15개가 됐다는 이유만으로 기존 `/v2` 숫자를 새 목차에 대입하지 않는다.

계획은 전체 과정의 기존 주소를 원 Lesson ID·원 Page로 먼저 고정한 뒤 목적지로 옮긴다. 심화뿐 아니라 기본편 구주소도 같은 Lesson·Page로 유지한다. 다음 세 출발점을 구별한다.

| 출발점 | 의미 |
| --- | --- |
| `content-stage-14` | 콘텐츠 stage의 버전 없는 14 Unit 주소 |
| `learn-v2` | Learn의 `/v2` 14 Unit 주소 |
| `learn-unversioned` | Learn이 현재 지원하는 개편 전 10 Unit 주소; `network_legacy_units.json`의 고정 Lesson 표 |

문자열이 같은 버전 없는 URL도 origin/판본에 따라 의미가 다르다. 이를 하나의 전역 별칭 표로 합치지 않는다. 알려진 정확한 주소만 대응시키고 미등록·범위 밖 주소는 다른 내용으로 연결하지 않는다.

- 구 Learn `/v2/unit/11/lesson/7/page/2` → 새 U11L4 **P9**. 구 L6의 7 Page 뒤에 구 L7의 두 번째 Page가 온다. P8은 구 L7 P1이다.
- 구 `/v2/unit/14/lesson/5/page/14` → 새 U15L4 P1.
- 구 안내·자료 주소 → 해당 `resources` Page.

`LearningLocation`은 `learner_id`, `course_id`, `fragment`, `updated`를 저장한다. 위치는 완료 증거가 아니다. 후속 적용은 기존 fragment와 판본을 대응표로 해석하고 새 위치를 파생시켜야 한다. 원래 위치·시각과 대응 버전을 감사 기록으로 보존한 뒤 정상 저장 트랜잭션에서 갱신한다. 주소 해석 실패 시 원본을 지우거나 새 1페이지로 자동 덮어쓰지 않는다. 위치 이동 후에도 기존 공개·선행 Lesson/Page 제한을 통과해야 한다.

## 4. 완료·답안·공개 설정

`completion_preflight`는 **합성 입력의 승계 가능 여부**만 계산한다. 상태 행을 만들거나 기존 호환 코드를 대체하지 않는다. 현재 심화의 질문 ID는 0개다. 빈 필수 집합의 `all([])`, 열람 위치, 상태 행의 존재만으로 과거 완료를 추정하지 않는다.

| 기존 기록 | 계획의 판단 |
| --- | --- |
| 행 없음 / 빈 문제 집합 / 위치만 있음 | 완료 승계 불가 |
| 병합 원고 일부만 명시적으로 완료 | 해당 원고의 이력은 보존하되 새 Lesson 전체 완료 승계 불가 |
| 병합 원고 모두 명시적으로 완료 | 모든 원문 해시·버전이 검토된 경우에만 전체 완료 승계 후보 |
| 분할 원고 전체의 명시적 완료 | 원문 범위가 그대로인 각각의 분할 Lesson에 승계 후보; 원본 버전·revision·행 해시를 근거로 남김 |
| 분할 원고 일부 진행 | 부분 답안·통과를 보존하되 빈 문제만 보고 분할 Lesson 완료를 만들지 않음 |
| 검토하지 않은 과거 버전 | 자동 승계 불가. 해당 원문·질문 계약을 별도 대조 |

명시적 완료는 검토한 버전의 저장된 `check.complete is True`를 인정한다. `legacy_completion`으로 승격된 기록은 그 원래 `source_version`까지 검토했고 `complete is True`와 보관 fingerprint가 있을 때만 후보가 된다. 승격 후 현재 행의 버전만으로 이전 완료 근거를 검토했다고 간주하지 않는다. 이번 합성 검증의 허용 버전 집합은 실제 수강자 판본 허용 목록이 아니다. `completion_eligible`도 운영 상태의 `complete` 필드가 아니다.

실제 구현에는 다음 저장 계약이 필요하다.

- 기존 `NetworkState` 행과 append-only `NetworkEvent`를 삭제·재기록하지 않는다. 원본 행을 `NetworkImportArchive`의 fingerprint로 보존하고, 새 ID의 파생 상태에는 원본 ID·판본·revision·행 해시·원문 해시·대응 계약 해시를 남긴다.
- 여러 행과 새 상태를 한 트랜잭션에서 잠그고 생성한다. 재실행이 새 학습 결과를 덮지 않도록 멱등성을 검증한다. 충돌이나 누락은 중단한다. 이 단계에는 apply 옵션이 없다.
- 기존 질문이 있다면 안정 Question ID와 검토한 질문 계약을 기준으로 답안·획득 통과·최초 필수 집합을 새 소유 Page에 투영한다. ID 중복·상이한 답안 충돌을 단순 합집합으로 덮지 않는다. 새 문제를 기존 문제로 바꾸거나 새 학습 목표를 과거 통과로 꾸미지 않는다.
- 대기 답안은 원래 요청·UUID를 보존/보관한다. 새 소유 Lesson, Question ID와 선택지/채점 계약이 확인되고 새 요청 생성이 허용된 때에만 **새 UUID**로 재제출한다. 이미 기록된 이벤트의 payload나 UUID를 바꾸지 않는다. 판본·소유권이 불명확하면 자동 제출하지 않고 사용자에게 확인 경로를 제공한다.
- 병합 Lesson의 공개 승계는 모든 기여 원고가 명시적으로 공개돼 있을 때만 후보로 삼는다. 분할은 원본 공개 상태를 따른다. 비공개 원고 하나를 포함하는 병합이 공개 원고 때문에 전체 공개되지 않게 한다. importer의 기본 `published_path`는 공개 의도의 증거가 아니다.
- 기본편 완료를 심화·자료 미완료 때문에 취소하지 않는다. 기존 기본편 답안·완료·공개 설정은 그대로 둔다. 심화의 **전체 공개 순차 제한**도 유지한다.

## 5. 검증과 다음 적용 조건

로컬 합성 검사 14개는 203 Page 배정/해시, 22 SVG 해시, 11개 ID 유지·9개 새 ID, 비이수 자료, 구주소 출발점 구별, 병합 오프셋, 보안 분할 경계, 부분/전체 완료, 미검토 버전 거절, 부분 공개를 확인한다. 전체 과정 460개 기존 Page의 3종 출발점에서 **1,380개 별칭**을 만든다. 현재 고정 원고의 범위 안에서만 유효하며 실사용자의 진행 상태를 조사하거나 승계하지 않았다.

Gemini Flash의 읽기 전용 검수에서 자료 격리·페이지 오프셋·부분 완료·대기 답안 소유권 요구를 반영했다. ‘구 U11L7 P2→새 P8’ 제안은 산술을 바로잡아 **P9**로 고쳤고, 무조건 답안 합집합·자동 재전송은 채택하지 않았다.

다음 순서로 실제 소비 코드를 구현한다.

1. 두 builder·importer·API·reader의 `resources` 전달과 비이수 계산을 구현하고 로컬 인증 화면에서 확인한다. PDF 권한과 기존 공개 설정도 함께 확인한다.
2. `/v3` 발행과 3종 구주소 대응, 위치 이력 보존을 프런트·백엔드에 동일하게 구현한다. 기존 14 Unit 입력을 계속 지원한다.
3. 기존 기록 파생의 원자성·멱등성·충돌·취소/재시도, 질문 소유권과 대기 답안을 실제 저장 계층의 합성 fixture로 확인한다. 이 문서의 순수 함수 검사만으로 DB 보존 구현이 끝났다고 판단하지 않는다.
4. 앱 CI·배포와 인증 흐름 검증 후 콘텐츠의 실제 15 Unit 전환을 별도 PR로 적용한다. 그 전에는 기존 Lesson을 제거하거나 병합하지 않는다.

이번 PR은 준비 문서·계획 생성기·합성 검증만 변경한다. 서비스 동작 변경이 없으므로 앱 배포나 브라우저 검증 대상은 아니다. #163과 #223의 실제 자료 분리·기록 보존·목차 전환 체크는 계속 미완료로 둔다.
