```python
case_cnt = int(input())
for cnt in range(case_cnt):
    num_cnt = int(input())
    num_list = list(map(int, (input())))
    cnt_list = [0] * 10

    max_idx = 0
    for idx in range(len(num_list)):
        for idx2 in range(1, 11):
            if num_list[idx] == idx2:
                cnt_list[idx2] += 1
    max_cnt = 0
    for idx in range(len(cnt_list)):
        if cnt_list[idx] >= max_cnt:
            max_idx = idx
            max_cnt = cnt_list[idx]

    print('#{} {} {}'.format(cnt+1, max_idx, max_cnt))
```

