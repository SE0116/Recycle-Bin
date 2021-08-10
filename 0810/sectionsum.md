```python
case_cnt = int(input())
for cnt in range(case_cnt):
    case_size = list(map(int, input().split()))
    case_list = list(map(int, input().split()))
    sum_list = [0] * (case_size[0]-case_size[1]+1)
    result = 0
    for i in range(case_size[0]-case_size[1]+1):
        for j in range(i, i+case_size[1]):
            sum_list[i] += case_list[j]
    max_num = sum_list[0]
    min_num = sum_list[0]
    for i in range(len(sum_list)):
        if sum_list[i] > max_num:
            max_num = sum_list[i]
        if sum_list[i] < min_num:
            min_num = sum_list[i]
    result = max_num - min_num
    print('#{} {}'.format(cnt+1, result))
```

