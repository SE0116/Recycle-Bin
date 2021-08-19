```python
case_cnt = int(input())
for cnt in range(case_cnt):
    sentence = input()
    length = len(sentence)
    bracket = []
    check = 0
    result = 0
    idx = 0
    while idx < length:
        if sentence[idx] == '(' or sentence[idx] == '{':
            bracket.append(sentence[idx])
        if sentence[idx] == ')':
            if not bracket:
                check = 1
            else:
                if bracket[-1] != '(':
                    check = 1
                bracket.pop()

        if sentence[idx] == '}':
            if not bracket:
                check = 1
            else:
                if bracket[-1] != '{':
                    check = 1
                bracket.pop()
        if check == 1:
            break
        idx += 1

    if bracket:
        check = 1

    if check == 0:
        result = 1

    print('#{} {}'.format(cnt+1, result))
```

