```python
for cnt in range(10):
    num_list = []
    sum_diag, sum_revdiag = 0, 0
    sum_row = [0] * 100
    sum_column = [0] * 100
    total_sum = []
    case_cnt = int(input())
    for idx in range(100):
        num_list += [list(map(int, input().split()))]
    for idx in range(len(num_list)):
        for idx2 in range(len(num_list[idx])):
            sum_column[idx2] += num_list[idx][idx2]
            sum_row[idx] += num_list[idx][idx2]
            if idx == idx2:
                sum_diag += num_list[idx][idx2]
            if 99 - idx2 == idx:
                sum_revdiag += num_list[idx][idx2]

    total_sum += sum_row + sum_column + [sum_diag] + [sum_revdiag]
    max_sum = total_sum[0]
    for idx in range(1, len(total_sum)):
        if total_sum[idx] > max_sum:
            max_sum = total_sum[idx]

    print('#{} {}'.format(cnt+1, max_sum))
```

