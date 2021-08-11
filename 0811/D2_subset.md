```python
for cnt in range(10):
    case_cnt = int(input())
    num_list = list(map(int, input().split()))
    sum_zero = 0
    for idx in range(1 << case_cnt):
        set_total = 0
        for idx2 in range(case_cnt):
            if idx & (1 << idx2):
                set_total += num_list[idx2]
    
        if set_total == 0:
                # set_total += num_list[idx2]
                # if set_total == 0:
            sum_zero += 1
    print('#{} {}'.format(cnt+1, sum_zero))
```

