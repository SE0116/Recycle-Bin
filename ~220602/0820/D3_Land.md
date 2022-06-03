```python
def is_exist(y1, x1, y2, x2):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if land[y][x] == 0: return True
    return False

def get_sum(y1, x1, y2, x2):
    total = 0
    for y in range(y1, y2+1) :
        for x in range(x1, x2+1) :
            total += land[y][x]
    return total

case_cnt = int(input())
for cnt in range(case_cnt):
    height, width = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(height)]

    max_sum = int(-21e8)
    for col1 in range(0,height):
        for row1 in range(0, width):
            for col2 in range(col1, height):
                for row2 in range(row1, width):
                    check = is_exist(col1, row1, col2, row2)
                    if check == False:
                        ret = get_sum(col1, row1, col2, row2)
                        if max_sum < ret :
                            max_sum = ret
    print('#{} {}'.format(cnt+1, max_sum))
```

