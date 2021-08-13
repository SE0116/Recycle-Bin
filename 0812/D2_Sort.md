```python
case_cnt = int(input())
for cnt in range(case_cnt):
    N = int(input())
    num_list = list(map(int, input().split()))
    for idx in range(len(num_list)):
        for idx2 in range(1,len(num_list)-idx):
            if num_list[idx2] < num_list[idx2-1]:
                num_list[idx2], num_list[idx2-1] = num_list[idx2-1], num_list[idx2]

    print('#{} '.format(cnt+1), end='')
    for idx in range(N-1):
        print(num_list[idx], end=' ')
    print(num_list[N-1])
```
