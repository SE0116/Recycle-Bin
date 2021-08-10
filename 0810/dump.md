```python
for cnt in range(1, 11):
    dump_cnt = int(input())
    box_list = list(map(int, input().split()))
    for idx in range(dump_cnt):
        max_num, min_num, max_min = box_list[0], box_list[0], 0
        max_idx, min_idx = 0, 0
        for idx2 in range(len(box_list)):
            if box_list[idx2] > max_num:
                max_num = box_list[idx2]
                max_idx = idx2
            if box_list[idx2] < min_num:
                min_num = box_list[idx2]
                min_idx = idx2
        box_list[max_idx] -= 1
        box_list[min_idx] += 1
        max_num, min_num = box_list[0], box_list[0]
        for idx2 in range(len(box_list)):
            if box_list[idx2] > max_num:
                max_num = box_list[idx2]
            if box_list[idx2] < min_num:
                min_num = box_list[idx2]
    max_min = max_num - min_num

    print('#{} {}'.format(cnt, max_min))
```

