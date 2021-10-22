```python
def dfs(level):
    global result
    if level == N:
        result += 1
        return
    for idx in range(N):
        if used[idx] == 1:
            continue
        used[idx] = 1
        dfs(level+1)
        used[idx] = 0
    return


for case_cnt in range(10):
    result = 0
    N = int(input())
    used = [0 for _ in range(N)]
    dfs(0)
    print('#{} {}'.format(case_cnt+1, result))
```

