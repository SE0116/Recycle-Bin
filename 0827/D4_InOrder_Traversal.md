```python
def dfs(now) :
    global result
    if len(node[now]) == 4 :
        dfs(int(node[now][2]))
        result += node[now][1]
        dfs(int(node[now][3]))

    elif len(node[now]) == 3:
        dfs(int(node[now][2]))
        result += node[now][1]

    else:
        result += node[now][1]

    return

for cnt in range(10):
    N = int(input())
    node = [[0]] + [list(input().split()) for _ in range(N)]
    result = ''
    dfs(1)
    print('#{} {}'.format(cnt+1, result))

```

