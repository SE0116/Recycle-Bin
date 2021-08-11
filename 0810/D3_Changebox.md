```python
case_cnt = int(input())
for cnt in range(case_cnt):
    n, q = map(int, input().split())
    num_list = [0] * n
    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            num_list[j-1] = i+1
    print('#{}'.format(cnt+1), end='')
    for i in range(len(num_list)):
        if i == len(num_list)-1:
            print(' {}'.format(num_list[i]))
        else:
            print(' {}'.format(num_list[i]), end='')
        
```

