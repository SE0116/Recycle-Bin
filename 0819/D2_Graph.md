```python
def dfs(now) :
    for next in range(1,V+1):
        if adj[now][next] == 0 : continue # now->next 없다
        if visited[next] == 1 : continue # 이미 방문 됨
        visited[next] = 1
        dfs(next)

case_cnt = int(input())
for cnt in range(case_cnt):
    V,E = map(int,input().split())
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        col, row = map(int, input().split())
        adj[col][row] = 1
    S,G = map(int, input().split())
    visited = [0 for _ in range(V+1)]
    visited[S] = 1 # 시작노드 재방문 금지
    dfs(S)
    if visited[G] == 1:
        print("#{} 1".format(cnt+1))
    else :
        print("#{} 0".format(cnt+1))
```

