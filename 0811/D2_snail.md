```python
case_cnt = int(input())
for cnt in range(case_cnt):
    size_num = int(input())
    num_list = [[0] * size_num for _ in range(size_num)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0

    x = y = 0
    num_list[x][y] = 1

    for num in range(2, size_num**2+1):
        x += dx[idx]
        y += dy[idx]
        num_list[x][y] = num

        if 0 <= x + dx[idx] < size_num and 0 <= y + dy[idx] < size_num and not num_list[x+dx[idx]][y+dy[idx]]:
            continue
        if idx != 3:
            idx += 1
        else:
            idx = 0
            
    print('#{}'.format(cnt+1))
    for num in num_list:
        print(*num)
```

