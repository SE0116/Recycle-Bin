```python
case_cnt = int(input())
for cnt in range(case_cnt):
    N, M = map(int, input().split())
    fly_list = []
    fly_result = [[0] * (N-M+1) for _ in range(N-M+1)]
    for idx in range(N):
        fly_list += [list(map(int, input().split()))]
    for col in range(len(fly_list)-M+1):
        for row in range(len(fly_list[col])-M+1):
            for col2 in range(col, col+M):
                for row2 in range(row, row+M):
                    fly_result[col][row] += fly_list[col2][row2]

    fly_max = fly_result[0][0]
    for col in range(len(fly_result)):
        for row in range(len(fly_result[col])):
            if fly_max < fly_result[col][row]:
                fly_max = fly_result[col][row]
    print('#{} {}'.format(cnt+1, fly_max))
```
