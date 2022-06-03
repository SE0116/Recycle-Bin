```python
case_cnt = int(input())
for cnt in range(case_cnt):
    N, M = map(int, input().rstrip().split())
    fly_list = [list(map(int, input().rstrip().split())) for _ in range(N)]
    result = []

    for col in range(N-M+1):
        for row in range(N-M+1):
            total = 0
            for sub_col in range(col, col+M):
                for sub_row in range(row, row+M):
                    total += fly_list[sub_col][sub_row]
            result += [total]

    max_fly = result[0]
    for idx in range(len(result)):
        if max_fly < result[idx]:
            max_fly = result[idx]

    print('#{} {}'.format(cnt+1, max_fly))
```

