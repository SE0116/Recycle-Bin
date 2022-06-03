```python
for cnt in range(10):
    length = int(input())
    calc_list = input().rstrip()
    stack = []
    operate = []
    result = []
 
    for idx in range(len(calc_list)):
        if calc_list[idx] == '+':
            while operate:
                stack += operate.pop()
            operate.append(calc_list[idx])
        elif calc_list[idx] == '*':
            operate.append(calc_list[idx])
        else:
            stack += calc_list[idx]
             
    while operate:
        stack += operate.pop()
 
    for idx in range(len(stack)):
        if stack[idx] == '+':
            a = int(result.pop())
            b = int(result.pop())
            result.append(a+b)
        elif stack[idx] == '*':
            a = int(result.pop())
            b = int(result.pop())
            result.append(a*b)
        else:
            result.append(stack[idx])
             
    print('#{} {}'.format(cnt+1, result[0]))
```

