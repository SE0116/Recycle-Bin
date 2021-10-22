```python
def find_start() :
    for y in range(N) :
        for x in range(N):
            if MAP[y][x] == '2':
                return (y, x)

    return (-1, -1)


def dfs(y, x):
    global check
    if MAP[y][x] == '3':
        check = 1
        return

    for t in range(4) :
        ny = y + dy[t]
        nx = x + dx[t]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        if MAP[ny][nx] == '1':
            continue
        if visited[ny][nx] == 1:
            continue
        visited[ny][nx] = 1
        dfs(ny,nx)
        if check == 1:
            return


case_cnt = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for cnt in range(case_cnt) :
    N = int(input())
    MAP = [input() for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 시작점 찾기
    sy, sx = find_start()
    check = 0
    visited[sy][sx] = 1
    dfs(sy, sx)

    print("#{} {}".format(cnt+1, check))
```

