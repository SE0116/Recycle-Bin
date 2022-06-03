```python
case_cnt = int(input())
for cnt in range(case_cnt):
    str_num = int(input())
    str_list = list(input().split())

    print('#{}'.format(cnt+1))
    for idx in range(len(str_list)):
        print('{}'.format(str_list[idx][0].upper()), end=' ')
    print()
```

