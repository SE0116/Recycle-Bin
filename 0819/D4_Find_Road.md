```python
def dfs(v):
    visited[v] = 1
    for w in range(1, 101):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)
    return

for cnt in range(10):
    case_cnt, length = map(int, input().split())
    road = list(map(int, input().split()))
    adj = [[0]* (101) for _ in range(101)]
    visited = [0] * (101)

    for i in range(length):
        adj[road[2*i]][road[2*i+1]] = 1

    dfs(0)

    if visited[99]:
        print("#{} 1".format(cnt+1))
    else:
        print("#{} 0".format(cnt+1))
```

