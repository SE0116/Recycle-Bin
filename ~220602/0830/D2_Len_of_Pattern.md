```python
case_cnt = int(input())
for cnt in range(case_cnt):
    str_list = input().rstrip() + '0'*2000
    pattern = ''

    for idx in range(len(str_list)):
        if str_list[0:idx] != str_list[0+idx:idx+idx]:
            continue
        else:
            pattern = str_list[0:idx]
            if not pattern:
                continue
            break

    print('#{} {}'.format(cnt+1, len(pattern)))
```

