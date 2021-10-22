```python
from collections import deque

for _ in range(10):
    case_cnt = int(input())
    num_list = deque(list(map(int, input().split())))
    N = len(num_list)
    idx = 1

    while True:
        temp = num_list.popleft() - idx
        if temp <= 0:
            num_list.append(0)
            break
        else:
            num_list.append(temp)
        idx += 1
        if idx > 5:
            idx= 1

    print('#{}'.format(case_cnt), end=' ')
    for idx in range(len(num_list)):
        print(num_list[idx], end=' ')
    print()
```

