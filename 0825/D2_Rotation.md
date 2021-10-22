```python
case_cnt = int(input())
for cnt in range(case_cnt):
    N, M = map(int, input().split())
    front, rear = 0, N
    lst = [0] * (N+M)
    num_list = list(map(int, input().split()))
    for idx in range(N):
        lst[idx] = num_list[idx]
        rear += 1
    for idx in range(N, len(lst)):
        lst[idx] = num_list[idx % N]
        rear += 1
        front += 1
    print('#{} {}'.format(cnt+1, lst[front]))
```

