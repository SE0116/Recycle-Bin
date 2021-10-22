```python
case_cnt = int(input())
for cnt in range(case_cnt):
    calc_list = input().split()
    idx = 0
    check = 0
    stack = []
    
    print("#{}".format(cnt+1), end=' ')
    
    while idx < len(calc_list):
        if check == 1:
            break
        if calc_list[idx].isdecimal():
            stack.append(int(calc_list[idx]))
        else:
            if calc_list[idx] == '.':
                if len(stack) < 1:
                    check = 1
                else:
                    ans = stack.pop()
            elif len(stack) < 2:
                check = 1
            else:
                b = stack.pop()
                a = stack.pop()
                if calc_list[idx] == '+': stack.append(a + b)
                if calc_list[idx] == '-': stack.append(a - b)
                if calc_list[idx] == '*': stack.append(a * b)
                if calc_list[idx] == '/':
                    if b == 0:
                        check = 1
                    else:
                        stack.append(a // b)
        idx += 1

    if stack:
        check = 1
    if check == 1:
        print("error")
    else:
        print(ans)
```

