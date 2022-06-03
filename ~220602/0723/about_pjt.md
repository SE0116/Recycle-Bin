# 기본 명령어

- `start .`  해당폴더 열기
- `touch <filename>`
- `cd ..`  상위 폴더로 이동

# Git

- `git init`  일반적인 디렉토리를 관리가 가능한 `repository` 로 만듬
- 작업 공간(Working Directory) / 스테이지(Staging Area) / 저장소(Commits)로 구분
- `Working Directory`  코드 작성 및 수정
- `Staging Area`  기록될 파일들의 변경사항들을 스테이지에 올리기
- `Commits`  스테이지 위의 변경사항들을 저장
- `git add`  WD -> SA로 가는 과정
- `git commit -m <message>`  SA -> C로 가는 과정
- `git status`  모니터링
- `git log`  저장소 내의 commit를 확인
- `git pull`  `git push`
- `.gitignore` 는 `add` 전에 반드시 먼저 작성