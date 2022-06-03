```python
time_num = int(input())
result = ''
num_list = [0] * 10
for cnt in range(time_num):
    bg_cnt = 0
    bg_num = list(map(int, list(input().strip())))
    for num in bg_num:
        num_list[num] += 1
    for i in range(len(num_list)):
        if num_list[i] >= 3:
            bg_cnt += 1
            num_list[i] -= 3
    for i in range(len(num_list)-2):
        if num_list[i] >= 1:
            if num_list[i+1] >= 1:
                if num_list[i+2] >= 1:
                    bg_cnt += 1
                    num_list[i] -= 1
                    num_list[i+1] -= 1
                    num_list[i+2] -= 1
    if bg_cnt == 2:
        result = 'Baby Gin'
    else:
        result = 'Lose'
    print(f'#{cnt+1} {result}')

```

