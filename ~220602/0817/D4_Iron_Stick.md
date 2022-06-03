```python
case_cnt = int(input())
for cnt in range(case_cnt):
    line = list(input())
    iron_now = 0
    num = 0
    idx = 0
    while idx < len(line):
        if line[idx] == '(' and line[idx+1] == ')':
            num += iron_now
            idx += 2
        elif line[idx] == '(' and line[idx+1] == '(':
            iron_now += 1
            idx += 1
        else:
            iron_now -= 1
            num += 1
            idx += 1

    print('#{} {}'.format(cnt+1, num))
```

