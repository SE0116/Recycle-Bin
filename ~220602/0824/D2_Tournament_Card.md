```python
def winner(a, b):
    if card[a] == card[b]:
        return a
    if (card[a] == 1 and card[b] == 3) or (card[a] == 2 and card[b] == 1) or (card[a] == 3 and card[b] == 2):
        return a
    else:
        return b


def dfs(s, e):
    if s == e:
        return s
    mid = (s+e) // 2
    a = dfs(s, mid)
    b = dfs(mid+1, e)
    result = winner(a, b)
    return result

case_cnt = int(input())
for cnt in range(case_cnt):
    card = [-1]
    N = int(input())
    card += list(map(int,input().split()))
    result = dfs(1, N)
    print('#{} {}'.format(cnt+1, result))
```

