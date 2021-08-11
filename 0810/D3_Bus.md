```python
case_cnt = int(input())
for idx in range(case_cnt):
    condition_list = list(map(int, input().split()))
    charge_stop = list(map(int, input().split()))
    charge_cnt = 0
    current_stop = 0
    while True:
        no_stop = 0
        if current_stop + condition_list[0] >= condition_list[1]:
            break
        for i in range(current_stop + condition_list[0], current_stop-1, -1):
            flag = 0
            for j in range(len(charge_stop)):
                if i == charge_stop[j]:
                    flag = 1
                    break
                else:
                    no_stop += 1
                print(current_stop, no_stop)
                if no_stop == condition_list[0]:
                    break
            if no_stop == condition_list[0]:
                break

            if flag == 1:
                current_stop = i
                charge_cnt += 1
                break

        if no_stop == condition_list[0]:
            break

    print('#{} {}'.format(idx + 1, charge_cnt))

```

