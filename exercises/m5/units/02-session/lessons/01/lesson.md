---
id: m5-u02-l01
title: 시작하기
render: markdown
source:
  repository: FutureReadyCampus/learn-missions
  path: network/118_day02_am_context_route_safety.md
  mission_id: GichanSource.m5-1110-am-context-route-safety
  commit: 61cf07917bdf13aa2571a551160363c425443504
---

# 시작하기

## 이번 Unit에서 만들 것: 보강·분기·안전장치

이번 Unit은 SOAR 자동 대응의 판단 단계를 구현합니다. Exercise 2-1은 알림 보강(enrichment, 인리치먼트: 판단에 필요한 정보를 알림에 추가하는 일)을 다룹니다. Exercise 2-2는 맥락에 따른 조건 분기(branching, 브랜칭: 조건에 따라 처리 경로를 나누는 일)를 다룹니다. Exercise 2-3은 안전장치(guardrail, 가드레일: 자동 대응이 잘못 실행되어도 피해가 커지지 않도록 미리 두는 점검과 제한)를 다룹니다.

깃허브 업로드는 Unit 3의 Exercise 3-2 마지막에 합니다. 새 문법은 Exercise 2-2의 **튜플 리턴과 언패킹**(두 값을 한 번에 리턴하고 한 번에 받는 문법)과 Exercise 2-3의 **`startswith`**(문자열이 지정한 문자열로 시작하는지 확인하는 메서드) 둘입니다. 보고서에서 [핵심 질문]이 붙은 질문은 <mark>내 출력 값을 근거로 이유까지</mark> 씁니다. 들여쓰기는 미리 채운 줄에 맞춥니다. 각 번호 주석 바로 아래에 한 줄을 씁니다. 주석은 지우지 않습니다.

 **이전 파일**: Unit 1에서 만든 `incident.py` · `playbook_runner.py` · `incident_samples.json` · `config/playbook_registry.json` 을 씁니다. 없는 파일은 복구 안내 `unit04_recovery_files.md` 의 순서로 만듭니다(`config/playbook_registry.json` 만 `complete_files.md` 의 1절에서 만듭니다).

## Unit 1 파일 확인하고 데이터 파일 만들기

1. **[VS Code]** `security-agent-toolkit` 폴더를 오른쪽 클릭 › **Open in Integrated Terminal** 로 터미널을 엽니다.
2. **[터미널]** 5과목 폴더로 들어가 Unit 1 파일을 확인합니다. <mark>`ls` 결과에 `config` · `incident.py` · `incident_samples.json` · `playbook_runner.py` 가 보이면</mark> 됩니다.
   ```bash
   pwd
   cd soar_response
   ls
   ```
   - 명령 풀이: `pwd` 지금 있는 폴더의 위치 확인 · `cd 폴더이름` 그 폴더로 이동 · `ls` 폴더 안의 파일 이름 보기
   - `pwd` 가 이미 `…/soar_response` 로 끝나면 `cd soar_response` 는 건너뜁니다.
3. 오늘 받은 파일 두 개(안내 파일과 보고서)를 `soar_response` 폴더로 옮기고, 보고서 제목의 `이름` 을 내 이름으로 바꿉니다.
4. **[터미널]** 데이터 파일 세 개를 만들고 **[VS Code]** 에서 열어 아래 내용을 붙여 넣습니다.
   ```bash
   touch users_info.json source_ips.json trusted_ips.json
   ls
   ```

**`users_info.json`** — 계정 이름별 재직 여부(`employed`)와 VIP 계정(VIP account, 브이아이피 계정: 잠기면 업무에 미치는 영향이 큰 중요도가 높은 계정) 여부(`vip`)를 기록한 파일입니다. `true` 는 「그렇다」, `false` 는 「아니다」입니다. 실제 조직에서는 인사 시스템과 IAM(Identity and Access Management, 아이덴티티 앤 액세스 매니지먼트: 계정과 접근 권한을 관리하는 체계)이 보유한 정보이고, 오늘은 파일로 대신합니다. `dami` 는 퇴사자(`employed` 가 `false`), `gaeun` 은 VIP 계정(`vip` 가 `true`)입니다. Exercise 2-1 ~ Exercise 2-3에서 읽어 사용합니다.

```
{
  "dami": {"employed": false, "vip": false},
  "seoyeon": {"employed": true, "vip": false},
  "gaeun": {"employed": true, "vip": true},
  "jiwoo": {"employed": true, "vip": false},
  "junho": {"employed": true, "vip": false},
  "hana": {"employed": true, "vip": false}
}
```

**`source_ips.json`** — 사용자 이름별로 로그인에 사용한 접속 IP(source IP, 소스 아이피: 로그인 요청이 출발한 출발지 IP)를 기록한 파일입니다. 이 파일에 이름이 없는 사용자는 접속 IP 기록이 없는 사용자입니다. Exercise 2-1에서 읽습니다.

```
{
  "seoyeon": "203.0.113.80",
  "jiwoo": "203.0.113.80",
  "gaeun": "198.51.100.77",
  "junho": "192.0.2.41"
}
```

**`trusted_ips.json`** — **신뢰 IP**(trusted IP, 트러스티드 아이피: 정상 접속의 출처로 사전에 확인해 등록한 IP) 목록입니다. 협력사 사무실 IP 한 개가 등록되어 있고, `seoyeon` 과 `jiwoo` 가 이 IP 에서 접속합니다. Exercise 2-1에서 읽습니다.

```
[
  "203.0.113.80"
]
```

5. **[터미널]** 두 가지를 확인합니다. 먼저 데이터 파일입니다. <mark>`6 4 1` 이 나와야</mark> 합니다.
   ```bash
   python -c "import json; print(len(json.load(open('users_info.json', encoding='utf-8'))), len(json.load(open('source_ips.json', encoding='utf-8'))), len(json.load(open('trusted_ips.json', encoding='utf-8'))))"
   ```
6. **[터미널]** Unit 1에서 만든 플레이북(playbook, 플레이북: 알림 유형별 대응 절차를 사전에 정의한 문서)의 등록 값을 점검합니다. 오늘 출력이 문서와 일치하려면 이 값이 <mark>아래 출력과 같아야</mark> 합니다. 다르면 `config/playbook_registry.json` 을 열어 해당 값을 같게 고칩니다(Unit 1에서 만든 내 파일은 깃허브에 올라가 있습니다).
   ```bash
   python -c "import json; print([(p['id'], p['trigger_rule'], p['min_grade'], p['approval']) for p in json.load(open('config/playbook_registry.json', encoding='utf-8'))])"
   ```
   ```
   [('PB-001', '퇴사한 계정', 'high', '자동'), ('PB-002', '대량 다운로드', 'mid', '담당자 승인 필요'), ('PB-003', '경로 스캔', 'low', '담당자 승인 필요')]
   ```

## 오류가 나면

- `pwd` 가 `soar_response` 로 끝나는지, `ls` 로 <mark>파일 이름이 문서와 같은지</mark> 봅니다.
- `ModuleNotFoundError: No module named 'incident'` 는 <mark>Unit 1에서 만든 `incident.py` 가 이 폴더에 없다는 뜻</mark>입니다. `unit04_recovery_files.md` 의 3번에서 만듭니다.
- 오류 전체를 친 명령과 함께 AI 에게 붙여 넣어 묻습니다(`.env` · API 키는 지웁니다). 막히면 맨 아래 「정답」을 보고, 풀리지 않으면 보고서에 「모름 — 막힌 곳: …」 이라고 씁니다.

> 실행은 VS Code 의 ▶ 단추가 아니라 <mark>**터미널**에서</mark> 합니다.

---
