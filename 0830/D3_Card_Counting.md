```python
case_cnt = int(input())
for cnt in range(case_cnt):
    card_list = input().rstrip()
    spade, diamond, heart, clover = [], [], [], []
    err = 0
    for idx in range(0, len(card_list)-2, 3):
        if card_list[idx] == 'S':
            for num in spade:
                if card_list[idx+1:idx+3] == num:
                    print('#{} ERROR'.format(cnt+1))
                    err += 1
                    break
            if err == 1:
                break
            spade.append(card_list[idx + 1:idx + 3])
        elif card_list[idx] == 'D':
            for num in diamond:
                if card_list[idx+1:idx+3] == num:
                    print('#{} ERROR'.format(cnt+1))
                    err += 1
                    break
            if err == 1:
                break
            diamond.append(card_list[idx + 1:idx + 3])
        elif card_list[idx] == 'H':
            for num in heart:
                if card_list[idx+1:idx+3] == num:
                    print('#{} ERROR'.format(cnt+1))
                    err += 1
                    break
            if err == 1:
                break
            heart.append(card_list[idx + 1:idx + 3])
        elif card_list[idx] == 'C':
            for num in clover:
                if card_list[idx+1:idx+3] == num:
                    print('#{} ERROR'.format(cnt+1))
                    err += 1
                    break
            if err == 1:
                break
            clover.append(card_list[idx + 1:idx + 3])
    else:
        print('#{} {} {} {} {}'.format(cnt+1, 13-len(spade), 13-len(diamond), 13-len(heart), 13-len(clover)))
```

