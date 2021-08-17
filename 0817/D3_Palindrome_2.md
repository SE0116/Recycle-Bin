```python
def is_palindrome(str_):
    n = len(str_)
    for i in range(n):
        if str_[i] != str_[n-1-i]:
            return 0
    return 1

for cnt in range(10):
    case_num = int(input())
    MAP = []
    for idx in range(100):
        MAP.append(input())
    # 가로 회문 검사
    max_list = []
    for idx in range(100):
        for col in range(100):
            for row in range(100-idx + 1):
                temp_str = MAP[col][row:row+idx]
                ret = is_palindrome(temp_str) # O(M)
                if ret == 1:
                    max_list += [len(temp_str)]
        # 세로 회문 검사
        for row in range(100):
            for col in range(100-idx + 1):
                temp_str = ''
                # O(M)
                for idx2 in range(col, col + idx):
                    temp_str += MAP[idx2][row]
                # O(M)
                ret = is_palindrome(temp_str)
                if ret == 1:
                    max_list += [len(temp_str)]

    max_len = max_list[0]
    for idx in range(1, len(max_list)):
        if max_len < max_list[idx]:
            max_len = max_list[idx]
    print("#{} {}".format(cnt+1, max_len))
```

