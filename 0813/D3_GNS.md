```python
case_cnt = int(input())
num_cnt = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for cnt in range(case_cnt):
    case_num, num = input().split()
    num_list = list(input().split())

    for idx in range(len(num_list)):
        if num_list[idx] == 'ZRO':
            num_list[idx] = 0
        elif num_list[idx] == 'ONE':
            num_list[idx] = 1
        elif num_list[idx] == 'TWO':
            num_list[idx] = 2
        elif num_list[idx] == 'THR':
            num_list[idx] = 3
        elif num_list[idx] == 'FOR':
            num_list[idx] = 4
        elif num_list[idx] == 'FIV':
            num_list[idx] = 5
        elif num_list[idx] == 'SIX':
            num_list[idx] = 6
        elif num_list[idx] == 'SVN':
            num_list[idx] = 7
        elif num_list[idx] == 'EGT':
            num_list[idx] = 8
        elif num_list[idx] == 'NIN':
            num_list[idx] = 9
    for idx in range(len(num_list)-1):
        for idx2 in range(len(num_list)-1-idx):
            if num_list[idx2] > num_list[idx2+1]:
                num_list[idx2], num_list[idx2+1] = num_list[idx2+1], num_list[idx2]

    for idx in range(len(num_list)):
        if num_list[idx] == 0:
            num_list[idx] = 'ZRO'
        elif num_list[idx] == 1:
            num_list[idx] = 'ONE'
        elif num_list[idx] == 2:
            num_list[idx] = 'TWO'
        elif num_list[idx] == 3:
            num_list[idx] = 'THR'
        elif num_list[idx] == 4:
            num_list[idx] = 'FOR'
        elif num_list[idx] == 5:
            num_list[idx] = 'FIV'
        elif num_list[idx] == 6:
            num_list[idx] = 'SIX'
        elif num_list[idx] == 7:
            num_list[idx] = 'SVN'
        elif num_list[idx] == 8:
            num_list[idx] = 'EGT'
        elif num_list[idx] == 9:
            num_list[idx] = 'NIN'

    print('#{}'.format(cnt+1), end=' ')
    for idx in range(len(num_list)):
        print(num_list[idx], end=' ')
    print()
```