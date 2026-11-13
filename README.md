# 성적 CSV 검증기

## ① 무엇을 하나요 (What · 현재 상태)

성적 CSV(name,score)를 읽어 유효한 (이름, 점수) 목록과, 건너뛴 줄의 줄 번호·원본·이유를 함께 돌려줍니다.

- 지금 되는 것: 0~100 정수 점수만 보관, 칸 수 오류·빈 이름·빈 점수·정수가 아닌 점수·범위 밖 점수는 건너뛰고 기록, 빈 줄은 기록 없이 건너뜀, 같은 이름은 모두 보관, 없는 파일은 FileNotFoundError
- 아직 안 되는 것: 평균·학점 계산은 하지 않습니다.

## ② 왜 만들었나요 (Why)

성적 파일에는 빈 칸, 105점 같은 범위 밖 점수, "결석" 같은 글자 점수가 섞여 있을 때가 많습니다.
이런 줄 하나 때문에 프로그램이 멈추거나 잘못된 점수가 섞이지 않도록, 문제 있는 줄은 이유와 함께 따로 남기고 나머지는 끝까지 읽게 만들었습니다.

## ③ 어떻게 쓰나요 (How)

Windows 명령 프롬프트(cmd) 기준입니다. 저장소 폴더에서 한 줄씩 실행합니다.
`python`이 실행되지 않으면 `py`로 바꿔서 입력합니다. (예: `py load_scores.py scores.csv`)

```
python --version
python -m pip install --user -U pytest~=7.0 pytest-cov
set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python load_scores.py scores.csv
```

`set` 줄은 pytest 플러그인 오류를 막는 설정이라, 새 터미널을 열 때마다 pytest 전에 한 번 입력합니다.

예상 결과: 읽은 줄 5개 / 건너뛴 줄 5개 (3·4·7·8·9행)

## ④ 어떻게 테스트하나요

```
python -m pytest test_load_scores.py -q
```

실제 결과: 12 passed (기본 11개 + weird.csv 보강 1개)

test_bug_A.py와 test_bug_B.py는 bug3_logic.py의 find_max(마지막 원소를 보지 않는 버그가 있음)를 두고 비교한 실험 파일이라 기본 테스트와 따로 실행합니다.

```
python -m pytest test_bug_A.py -q
python -m pytest test_bug_B.py -q
```

- test_bug_A.py: 1 failed, 3 passed — 최댓값이 마지막에 있는 [3, 5, 10]에서 버그를 찾아 실패
- test_bug_B.py: 4 passed — 최댓값이 마지막에 오는 입력이 없어 버그를 검사하지 못함

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| load_scores.py | CSV를 읽어 (kept, skipped)를 돌려주는 함수 |
| scores.csv · empty.csv · weird.csv | 정상 파일 · 헤더만 있는 파일 · 이상한 값이 많은 파일 (예제 데이터) |
| test_load_scores.py | load_scores 테스트 12개 (정상·빈 줄·쉼표 이름·없는 파일·헤더만·경계값 6개·weird.csv) |
| bug3_logic.py · test_bug_A.py · test_bug_B.py | 버그가 있는 find_max와, 코드를 준 경우(A)·명세만 준 경우(B)에 받은 테스트 |
| prompts.txt | 실험에 쓴 요청문 |

## ⑥ 만든 사람과 AI 사용

- 만든 사람 : jung-juan
- 사용한 AI 도구·모델 : VS Code Copilot Chat (Ask) / Copilot Fusion
- AI에게 도움받은 부분 : find_max 테스트 초안 (test_bug_A.py, test_bug_B.py — 받은 코드 그대로 보존)
- 내가 직접 판단·확인한 부분 : 명세를 보고 정한 기대값, load_scores 테스트와 커버리지 보강, A·B 실험 결과 판정, README 명령 실행 확인

## 라이선스

MIT License (LICENSE 파일 참고)
