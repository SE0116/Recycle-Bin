```python
case_cnt = int(input())
for cnt in range(case_cnt):
    back_grid = [[0] * 10 for _ in range(10)]
    color_cnt = int(input())
    purple = 0
    for cnt2 in range(color_cnt):
        area_color = list(map(int, input().split()))
        for col in range(len(back_grid)):
            for row in range(len(back_grid[col])):
                if col >= area_color[0] and col <= area_color[2] and row >= area_color[1] and row <= area_color[3] :
                    back_grid[col][row] += area_color[4]
                    if back_grid[col][row] >= 3:
                        purple += 1
    print('#{} {}'.format(cnt+1, purple))
```

