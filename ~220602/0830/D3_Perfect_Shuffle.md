```python
case_cnt = int(input())
for cnt in range(case_cnt):
    N = int(input())
    card_list = list(input().rstrip().split())
    result = []
    if N % 2:
        front_half = card_list[:N//2+1]
        back_half = card_list[N//2+1:]
    else:
        front_half = card_list[:N//2]
        back_half = card_list[N//2:]
    for idx in range(N):
        if idx % 2 == 0:
            result.append(front_half[idx//2])
        else:
            result.append(back_half[idx//2])

    print('#{}'.format(cnt+1), end=' ')
    for idx in range(len(result)):
        print(result[idx], end=' ')
    print()
```

