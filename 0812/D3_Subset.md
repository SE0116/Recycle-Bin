```python
case_cnt = int(input())
for cnt in range(case_cnt):
    N, k = map(int, input().split())
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sum_k = 0
    for bit in range(1 << 12):
        set_total = 0
        set_cnt = 0
        for idx in range(12):
            if bit & (1 << idx):
                set_total += num_list[idx]
                set_cnt += 1

        if set_cnt == N and set_total == k:
            sum_k += 1

    print('#{} {}'.format(cnt + 1, sum_k))
```
