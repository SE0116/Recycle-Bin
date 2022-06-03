```python
for cnt in range(10):
    case_cnt = int(input())
    build_num = list(map(int, input().split()))

    view_num = 0

    for i in range(2, len(build_num)-1):
        for j in range(1, build_num[i]+1):
            if j-build_num[i-2] >= 1 and j-build_num[i-1] >= 1 and j-build_num[i+1] >= 1 and j-build_num[i+2] >= 1:
                view_num += 1

    print(f'#{cnt+1} {view_num}')
```

