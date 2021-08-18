```python
case_cnt = int(input())
for cnt in range(case_cnt):
    pascal_cnt = int(input())
    pascal_list = [[0] * pascal_cnt for _ in range(pascal_cnt)]
    print('#{}'.format(cnt+1))
    for col in range(pascal_cnt):
        for row in range(col+1):
            if row == 0 or row == col:
                pascal_list[col][row] = 1
            else:
                pascal_list[col][row] = pascal_list[col-1][row-1] + pascal_list[col-1][row]
            print(pascal_list[col][row], end=' ')
        print()

```

