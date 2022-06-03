```python
def is_valid(s1 ,s2) : # s1 > s2 인지? 내가 더 우선순위가 높은가?
    eval = {'+':1,'-':1,'*':2,'/':2,'(':0}
    if eval[s1] > eval[s2] : return True
    else : return False


case_cnt = int(input())
for cnt in range(case_cnt):
    calc_list = input().rstrip()
    stack = []  # 연산자
    i = 0

    print('#{}'.format(cnt+1), end=' ')

    while i < len(calc_list):
        if ord('0') <= ord(calc_list[i]) <= ord('9'):  # 숫자
            print(calc_list[i], end='')
        elif calc_list[i] == '(':
            stack.append(calc_list[i])
        elif calc_list[i] == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        # 나머지 연산자들은 우선순위에 따라서 처리
        else:
            while stack and not is_valid(calc_list[i], stack[-1]):  # s[i] vs stack[-1]
                print(stack.pop(), end='')
            stack.append(calc_list[i])
        i += 1

    while stack:
        print(stack.pop(), end='')

    print()
```

