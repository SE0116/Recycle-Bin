```python
def paper(num):
    if num == 10:
        return 1
    if num == 20:
        return 3
    if num == 0:
        return

    return paper(num-10) + paper(num-20) * 2

case_cnt = int(input())
for cnt in range(case_cnt):
    length = int(input())
    print('#{} {}'.format(cnt+1, paper(length)))
```

