---
id: m3-u03-l04
title: 정답
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/080_day02_pm_tests.md
  mission_id: GichanSource.m3-1022-pm-tests
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 정답

## 정답을 읽는 법

설명하는 답은 한 예이고, 핵심이 같으면 맞습니다.

---

## Exercise 3-1 정답

 **터미널에 입력합니다.**

```bash
python exercise3-1_broken.py
```

**채운 코드** (한 예)

```python
    try:                                                         # 아래를 시도한다
        with open(path, encoding="utf-8") as input_file:                  # 파일을 연다
            return json.load(input_file)                                  # 읽은 내용을 바로 리턴한다
    except FileNotFoundError:                                    # 파일이 없으면
        print("[경고] 설정 파일 없음:", path)                      # 경고를 남기고
        return default                                           # 기본값을 리턴한다
    except json.JSONDecodeError:                                 # JSON 이 깨졌으면
        print("[경고] 설정 파일 깨짐:", path)                      # 경고를 남기고
        return default                                           # 기본값을 리턴한다
```

**결과**

- 위 코드는 `load_json` 본문입니다. 줄 수가 달라도 주석이 말한 일을 하면 맞습니다.
- (가) 출력은 다음과 같습니다. 첫 경고는 파일이 없어서(`FileNotFoundError`), 둘째 경고는 마지막 쉼표 때문에 JSON 규칙이 틀려서(`JSONDecodeError`) 나왔습니다.

```
config/users.json -> 사용자 6 명을 읽음, 판정을 계속한다
[경고] 설정 파일 없음: config/users_typo.json
config/users_typo.json -> 사용자 0 명, 등록된 사용자가 없다
[경고] 설정 파일 깨짐: config/users_broken.json
config/users_broken.json -> 사용자 0 명, 등록된 사용자가 없다
```
- (나) 판정 프로그램이 오류로 멈추면 정산 포털이 판정을 받지 못해 업무가 막힙니다. 그러면 현장에서는 급한 업무를 위해 판정을 끄거나 건너뛰고 **모두 통과**시키기 쉽습니다. 빈 설정을 리턴하면 프로그램은 계속 돌면서 모든 요청을 거부하므로, 열려서는 안 되는 것이 열리는 일은 없습니다. 경고가 남아서 운영자는 무엇을 고쳐야 하는지 바로 압니다.
- (다) 추가할 것 예: ① 경고를 화면에만 찍지 않고 파일 로그에 남기고 담당자에게 메일 · 메신저로 알린다 ② 판정 프로그램이 지금 빈 설정으로 돌고 있는지 알려 주는 상태 확인 명령이나 화면을 둔다 ③ 마지막으로 정상이던 설정 사본을 보관해 두고 한 번에 되돌릴 수 있게 한다. 가장 먼저 할 것은 알림이 좋습니다. 모두 거부되는 상태를 모르면 업무가 왜 멈췄는지 찾는 데 시간이 걸리고, 그동안 현장에서 판정을 끄자는 요구가 커지기 때문입니다. 다른 것을 먼저 골라도 이유가 있으면 맞습니다.

**왜** — 실패를 피할 수는 없으니, 실패했을 때 어떻게 동작할지를 정해 둡니다. 접근통제는 실패하면 모두 막는 쪽이어야 합니다. 고장을 일부러 만들어 보면 실제 고장 때 어떻게 되는지 미리 알고, 기본값이 원래 자료와 같은 모양이어야 뒤의 코드가 그대로 동작합니다.

**자주 틀리는 곳** — `except JSONDecodeError:` 처럼 `json.` 을 빼서 `NameError` 가 나는 경우가 가장 많습니다. `except:` 만 써서 모든 오류를 그냥 넘기면 코드의 오타까지 숨겨져 원인을 찾기 어렵습니다. 오류 이름을 정확히 적습니다. `return default` 를 빼먹으면 `None` 이 리턴되어 시험 파일에서 `TypeError: argument of type 'NoneType' is not iterable` 이 납니다. `load_json(path)` 처럼 기본값을 빼면 `TypeError: missing 1 required positional argument` 가 납니다. 깨진 파일을 붙여 넣으면서 쉼표를 지워 정상 파일로 만들어 버리는 경우도 있습니다.

**관제에서는** — 「설정 파일 깨짐」 경고는 누군가 설정을 바꿨다는 뜻이기도 해서, 경고가 나면 최근 변경 이력(git)을 함께 봅니다. 고장 시험(장애 주입)을 정기적으로 해 두면, 실제로 모두 막혔을 때 원인을 설정에서 먼저 찾습니다.

---

## Exercise 3-2 정답

 **터미널에 입력합니다.**

```bash
python test_policy.py
python test_policy_extra.py
```

**채운 코드** (한 예)

```python
when = at("2026-10-22 14:00")                                    # 요청 시각을 만든다
is_allowed, reason = evaluate_access("seoyeon", "ACCOUNT", "CHANGE", when)  # 2. 권한 없음
assert is_allowed == False and reason == "권한 없음", "2. 권한 없음"      # 권한 없음으로 거부되는지 확인한다

when = at("2026-10-22 17:59")                                    # 요청 시각을 만든다
is_allowed, reason = evaluate_access("seoyeon", "SETTLE", "QUERY", when)  # 3. 만료 1분 전
assert is_allowed == True and reason == "예외 1번", "3-1. 만료 1분 전 허용"  # 만료 1분 전에는 예외 1번으로 허용되는지 확인한다
when = at("2026-10-22 18:00")                                    # 요청 시각을 만든다
is_allowed, reason = evaluate_access("seoyeon", "SETTLE", "QUERY", when)  # 3. 만료 정각
assert is_allowed == False, "3-2. 만료 정각 거부"                       # 만료 정각에는 거부되는지 확인한다

users = load_json("config/no_such.json", {})                     # 4. 없는 파일을 읽는다
assert "seoyeon" not in users, "4. 설정 고장이면 사용자 없음"                # 설정이 고장 나면 사용자 딕셔너리에 seoyeon 이 없어야 한다
```

**결과**

- 위 코드는 `test_policy.py` 의 2 ~ 4번 테스트입니다. 줄 수가 달라도 주석이 말한 일을 하면 맞습니다. `python test_policy.py` 의 출력은 다음과 같습니다.

```
[경고] 설정 파일 없음: config/no_such.json
테스트 4개 모두 통과
```

- (가) 출력은 다음과 같습니다. 실패한 줄은 6번 `assert` 줄이고(아래 예에서는 `line 19`, 파일에 줄을 추가하거나 빼면 숫자가 달라집니다), 설명은 「6. 만료 정각에도 허용되어야 한다(팀원 제안)」입니다. 파일 앞의 폴더 경로도 PC 마다 다릅니다.

```
5 통과
Traceback (most recent call last):
  File "…/test_policy_extra.py", line 19, in <module>
    assert is_allowed == True, "6. 만료 정각에도 허용되어야 한다(팀원 제안)"           # 만료 정각에도 허용인지 확인한다
AssertionError: 6. 만료 정각에도 허용되어야 한다(팀원 제안)
```

- (나) **제안이 지금 정책과 다르다는 뜻입니다.** 「지금 시각이 만료 시각보다 앞일 때만 유효, 정각에는 이미 거부」로 정했고, 코드(`now < expires`)는 그대로 지키고 있습니다. 위의 3번 테스트(만료 정각 거부)도 같은 규칙을 확인해 통과했습니다. 그래서 코드를 고칠 일이 아니라, 제안을 받아들일지 정책으로 정할 일입니다.
- (다) 예: 3번 테스트(만료 17:59 허용, 18:00 거부)가 없으면, 누군가 정책 코드를 한 줄 고치다 비교를 잘못 써서 만료된 예외가 정각 뒤에도 열려 있어도 눈으로는 알아채지 못합니다. 그러면 퇴근 뒤 밤에 이미 끝난 예외로 정산 자료가 조회되고, 다음 날 감사에서야 발견됩니다. 다른 예: 4번 테스트(설정 없음)가 없으면 설정 파일 읽기를 고치다 「사용자가 없으면 허용」으로 바뀌어도 잡지 못해 모든 요청이 열립니다. 하나를 골라 구체적인 장면을 적으면 맞습니다.

**왜** — 테스트는 기대를 먼저 적고 실제와 비교합니다. 경계값을 넣어야 비교 기호 하나의 실수까지 잡습니다. 테스트 실패는 「무엇인가 서로 다르다」는 신호일 뿐, 어느 쪽이 틀렸는지는 정책을 보고 판단합니다. 실패를 없애려고 코드부터 바꾸면 정책이 알리지 않고 바뀝니다.

**자주 틀리는 곳** — `assert is_allowed == False and reason == "권한 없음"` 에서 `and` 대신 쉼표를 써서 `assert is_allowed == False, reason == "권한 없음"` 으로 쓰는 경우가 가장 많습니다. 그러면 뒤쪽은 설명으로 읽혀 이유를 검사하지 않습니다. 3번에서 두 번째 판정을 하지 않고 첫 `is_allowed` 를 다시 검사하는 실수도 있습니다. 6번이 실패하자 `exception_policy.py` 의 `<` 를 `<=` 로 고치는 경우도 많은데, 그러면 3번 테스트가 깨지고 정책이 알리지 않고 바뀝니다. `Traceback` 이 나왔다고 프로그램이 망가졌다고 생각하는 경우도 있지만, 이것은 테스트가 정상적으로 차이를 알려 준 것입니다.

**관제에서는** — 정책을 바꾸는 요청에는 「바꾼 뒤에도 통과해야 하는 테스트」를 함께 붙이게 합니다. 테스트가 없는 정책 변경은 받지 않습니다. 규칙 변경 요청은 「테스트로 적은 제안」 형태로 받으면 무엇이 바뀌는지 분명해지고, 실패한 테스트는 변경 검토 회의의 출발점이 됩니다.

---

## 정답 마무리

 **터미널에 입력합니다.**

```bash
cd ..
pwd
git status
git add .
git commit -m "Add access control day 2 role management, exceptions, policy and tests"
git push
```

**결과**

- (가) 한 예: 「줄이 열여섯 개였고(오늘 만든 `.py` 파일 열 개, `config` 의 새 JSON 두 개, 보고서 둘과 안내 문서 둘을 합친 네 개), `.env` · `.venv` 는 없었다」. 줄 수와 이름은 학생마다 다를 수 있습니다. `.env` 나 `.venv` 가 보였다면 `.gitignore` 에 한 줄을 적고 `git status` 를 다시 쳤다고 적습니다.

**왜** — 올리기 전에 올라갈 파일을 확인해야 비밀 키가 섞이지 않습니다. 정책 코드와 테스트가 함께 올라가야 다음에 누가 바꿔도 같은 기준으로 확인할 수 있습니다.

**자주 틀리는 곳** — `.env` 가 보이는데 그대로 `git add .` 를 하는 실수가 가장 위험합니다. `cd ..` 를 두 번 쳐서 `security-agent-toolkit` 바깥으로 나가는 경우도 있습니다. `pwd` 로 확인합니다.

**관제에서는** — 접근통제 정책과 테스트는 같은 커밋에 함께 올려, 어느 정책이 어느 테스트로 확인됐는지 이력으로 남깁니다.
