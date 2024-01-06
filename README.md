## JADNI

깃허브 잔디에 단어 쓰기

### Requirement

- git
- Python 3

### 사용법

1.  ```
    git clone https://github.com/s4ng/jandi
    ```
2. ```
   cd jandi
   ```
3. ```
   rm -rf .git
   ```
4. ```
   git init
   ```
5. config.json 수정
    - username, email 은 github 에 default 설정된 내용으로 수정
    - word 에 쓰고 싶은 영단어 입력(공백 포함 7자 이하)
    - weeksBefore 에는 단어를 왼쪽으로 옮기고 싶을 때 수정 (0으로 설정 시 제일 오른쪽에 써짐)
5. ```
   python jandi.py
   ```
6. 본인 Github 계정에 Repository 생성
7. ```
   git remote add origin (Your git repository)
   ```
8. ```
   git push -f origin main
   ```
9. https://github.com/s4ng/jandi 에 별 주기 (선택)
