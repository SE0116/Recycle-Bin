```python
case_cnt = int(input())
for cnt in range(case_cnt):
    str_ = input()
    stack = []
    for letter in str_:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    print('#{} {}'.format(cnt+1, len(stack)))
```

