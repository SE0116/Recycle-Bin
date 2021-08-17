```python
def is_palindrome(str_):
    n = len(str_)
    for i in range(n):
        if str_[i] != str_[n-1-i]:
            return 0
    return 1

case_cnt = int(input())
for cnt in range(case_cnt):
    N, M = map(int, input().split()) # N x N 2차원 리스트 / M 은 palindrome 길이
    MAP = []
    for idx in range(N):
        MAP.append(input())
    # 가로 회문 검사
    ans = ''
    for col in range(N):
        for row in range(N-M + 1):
            temp_str = MAP[col][row:row+M]
            ret = is_palindrome(temp_str) # O(M)
            if ret == 1:
                ans = temp_str
    # 세로 회문 검사
    for row in range(N):
        for col in range(N-M + 1):
            temp_str = ''
            # O(M)
            for idx in range(col, col + M):
                temp_str += MAP[idx][row]
            # O(M)
            ret = is_palindrome(temp_str)
            if ret == 1:
                ans = temp_str

    print("#{} {}".format(cnt+1, ans))
```

