```python
def dfs(level, sum):
    global min_sum
    if min_sum < sum:
        return
    if level == N:
        if min_sum > sum:
            min_sum = sum
        return
    for idx in range(N):
        if used[idx] == 1:
            continue
        used[idx] = 1
        dfs(level+1, sum+MAP[level][idx])
        used[idx] = 0


case_cnt = int(input())
for cnt in range(case_cnt):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    used = [0 for _ in range(N)]
    min_sum = int(21e8)
    dfs(0, 0)
    print('#{} {}'.format(cnt+1, min_sum))
```

