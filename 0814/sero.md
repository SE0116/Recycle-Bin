```python
case_cnt = int(input())
for cnt in range(case_cnt):
    str_list = [list(input()) for _ in range(5)]
    result = ''
    max_length = 0
    for idx in range(5):
        if len(str_list[idx]) > max_length:
            max_length = len(str_list[idx])
    for idx in range(max_length):
        for idx2 in range(5):
            if len(str_list[idx2]) > idx:
                result += str_list[idx2][idx]
    print("#{} {}".format(cnt+1 + 1, result))
```

