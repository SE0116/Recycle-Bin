```python
def get_set(n, total, cnt):
    global result
    if total > K:
        return
    if n >= 21:
        if total == K and cnt == N:
            result += 1
        return
 
    get_set(n+1, total+n, cnt+1)
    get_set(n+1, total, cnt)
 
 
case_cnt = int(input())
for cnt in range(case_cnt):
    N, K = map(int, input().split())
    result = 0
    get_set(1, 0, 0)
 
    print('#{} {}'.format(cnt+1, result))
```

