```python
case_cnt = int(input())
for cnt in range(case_cnt):
    b_list = input()

    print('#{}'.format(cnt + 1), end=' ')

    for idx in range(len(b_list)-1, -1, -1):
        if b_list[idx] == 'b':
            print('d', end='')
        elif b_list[idx] == 'd':
            print('b', end='')
        elif b_list[idx] == 'p':
            print('q', end='')
        elif b_list[idx] == 'q':
            print('p', end='')
    print()
```