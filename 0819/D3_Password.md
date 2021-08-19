```python
for cnt in range(10):
    case_cnt, hint = input().split()
    pwd = []
    for num in hint:
        if pwd and pwd[-1] == num:
            pwd.pop()
        else:
            pwd.append(num)
    print('#{}'.format(cnt+1), end=' ')
    for idx in range(len(pwd)):
        print(pwd[idx], end='')
    print()
```

