# python-algorithm-automation 
파이썬 알고리즘 소스코드
> PS 코드 업로드할 거라 master branch로만 진행

## [CodeUp](https://www.codeup.kr/index.php)
- 기초 100제 `Completed`

## [Programmers](https://programmers.co.kr/)
- level 1 `Completed`
- level 2 `In Progress`

---

# Automation
- 해결한 문제의 소스코드를 가져와서 파일로 저장
- 해결할 문제의 정답 양식, 입력값, 출력값을 가져와서 파일로 저장

## Installation
[pip](https://pip.pypa.io/en/stable/)를 이용하여 라이브러리 설치 *Python Version: 3.8*
```bash
pip install -r requirements.txt
```
- `requests`, `selenium`, `bs4`, `lxml`, `json`

## CodeUp
해결한 문제의 소스코드 가져오기
> 로그인 필요

1. CodeUp 자동 로그인(로그인 정보는 json file 로드하여 사용)
2. 문제집 선택
3. 해당 문제집의 문제 중에서 해결한 문제의 소스코드 수집
4. 해당 문제집 폴더에 `.py` 파일로 저장

<img width="700" alt="example_codeup1" src="https://user-images.githubusercontent.com/46367323/78097865-72a9f700-7418-11ea-97ab-ec459b61c9df.gif"></img>
<img width="400" alt="example_codeup2" src="https://user-images.githubusercontent.com/46367323/78097885-8190a980-7418-11ea-9154-53831d968c48.png"></img>


## Programmers
해결할 문제 가져와서 자동으로 세팅
(`.py` 파일 생성)   

1. 문제의 레벨 입력 (레벨별 폴더를 나누기 위함)
2. 문제의 URL 입력

<img width="500" alt="example_programmers1" src="https://user-images.githubusercontent.com/46367323/78097772-28287a80-7418-11ea-8623-2aca341aaa8c.png"></img>
<img width="1261" alt="example_programmers3" src="https://user-images.githubusercontent.com/46367323/78097698-e1d31b80-7417-11ea-82b4-73bb9de5b991.png"></img>
<img width="1261" alt="example_programmers3" src="https://user-images.githubusercontent.com/46367323/78097747-07f8bb80-7418-11ea-8843-52d2af23b047.png"></img>
