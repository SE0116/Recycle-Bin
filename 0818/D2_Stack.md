```python
case_cnt = int(input())
for cnt in range(case_cnt):
    command_num = int(input())
    stack = []
    print('#{}'.format(cnt+1))
    for com in range(command_num):
        command = list(input().split())
        if command[0] == 'c':
            print(len(stack))
        elif command[0] == 'o':
            if stack:
                ret = stack.pop()
                print(ret)
            else:
                print('empty')
        elif command[0] == 'i':
            stack.append(command[1])
```

