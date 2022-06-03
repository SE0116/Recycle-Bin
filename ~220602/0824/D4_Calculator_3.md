```python
for cnt in range(10):
    length = int(input())
    calc_list = input().rstrip()
    stack = []
    operate = []
    result = []

    for idx in range(len(calc_list)):
        if calc_list[idx] == '(':
            operate.append(calc_list[idx])

        elif calc_list[idx] == '+':
            while operate:
                if operate[-1] == '(':
                    break
                stack.append(operate.pop())
            operate.append(calc_list[idx])

        elif calc_list[idx] == '*':
            operate.append(calc_list[idx])

        elif calc_list[idx] == ')':
            while operate and operate[-1] != '(':
                stack.append(operate.pop())
            operate.pop()
        else:
            stack += calc_list[idx]

    while operate:
        stack += operate.pop()
    for idx in range(len(stack)):
        if stack[idx] == '+':
            b = int(result.pop())
            a = int(result.pop())
            result.append(a + b)
        elif stack[idx] == '*':
            b = int(result.pop())
            a = int(result.pop())
            result.append(a * b)
        else:
            result.append(stack[idx])

    print('#{} {}'.format(cnt + 1, result[0]))
```

