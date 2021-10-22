```python
def dfs(col, row):
    global result

    if map_list[col][row] == 3:
        result = 1
        return
    for x, y in dx_dy:
        dx = col + x
        dy = row + y
        if map_list[dy][dx] != 1:
            map_list[col][row] = 1
            dfs(dy, dx)


for cnt in range(10):
    case_cnt = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(16)]
    result = 0
    dx_dy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    dfs(1, 1)

    print('#{} {}'.format(case_cnt, result))
```

