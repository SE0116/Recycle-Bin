```python
case_cnt = int(input())
for cnt in range(case_cnt):
    N, K = map(int, input().split())
    num_list = []
    col_cnt = [0] * N
    result = 0
    for n in range(N):
        num_list += [list(map(int, input().split()))]
    for col in range(len(num_list)):
        row_cnt = 0
        for row in range(len(num_list[col])):
            if num_list[col][row] == 1:
                row_cnt += 1
                col_cnt[row] += 1
            else:
                if row_cnt == K:
                    result += 1
                if col_cnt[row] == K:
                    result += 1
                row_cnt = 0
                col_cnt[row] = 0

            if row == len(num_list[col])-1:
                if row_cnt == K:
                    result += 1
        if col == len(num_list[col])-1:
            for idx in range(len(col_cnt)):
                if col_cnt[idx] == K:
                    result += 1

    print('#{} {}'.format(cnt + 1, result))
```

