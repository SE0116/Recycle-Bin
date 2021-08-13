```python
case_cnt = int(input())
for cnt in range(case_cnt):
    N = int(input())
    num_list = list(map(int, input().split()))
    sort_list = []
    while num_list != []:
        max_num, min_num = num_list[0], num_list[0]
        max_idx, min_idx = 0, 0
        for idx in range(len(num_list)):
            if num_list[idx] > max_num:
                max_num = num_list[idx]
                max_idx = idx
            if num_list[idx] < min_num:
                min_num = num_list[idx]
                min_idx = idx
        sort_list += [max_num] + [min_num]
        num_list.remove(max_num)
        num_list.remove(min_num)

    print('#{} '.format(cnt+1), end='')
    for idx in range(9):
        print(sort_list[idx], end=' ')
    print(sort_list[9])
```
