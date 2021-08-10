```python
case_cnt = int(input())
for cnt in range(case_cnt):
    num = int(input())
    x2, x3, x5, x7, x11 = 0, 0, 0, 0, 0
    while True:
        if num % 2 == 0:
            num = num // 2
            x2 += 1
        elif num % 3 == 0:
            num = num // 3
            x3 += 1
        elif num % 5 == 0:
            num = num // 5
            x5 += 1
        elif num % 7 == 0:
            num = num // 7
            x7 += 1
        elif num % 11 == 0:
            num = num // 11
            x11 += 1
        else:
            break

    print('#{} {} {} {} {} {}'.format(cnt+1, x2, x3, x5, x7, x11))

```

