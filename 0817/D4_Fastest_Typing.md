```python
def is_same(start_idx, n):
    if start_idx + n - 1 >= len(str1):
        return 0
    for idx in range(n):
        if str1[start_idx+idx] != str2[idx]:
            return 0
    return 1

case_cnt = int(input())
for cnt in range(case_cnt):
    str1, str2 = input().split()
    idx = 0
    result = 0
    N = len(str1)
    while idx < N:
        ret = is_same(idx, len(str2))
        if ret == 1:
            idx += len(str2)
            result += 1
        else:
            idx += 1
            result += 1
    print('#{} {}'.format(cnt+1, result))
```

