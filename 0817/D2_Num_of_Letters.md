```python
case_cnt = int(input())
for cnt in range(case_cnt):
    str1 = input()
    str2 = input()
    max_cnt = 0
    for idx in range(len(str1)):
        str1[idx]
        result = 0
        for idx2 in range(len(str2)):
            if str1[idx] == str2[idx2] :
                result += 1
        if max_cnt < result:
            max_cnt = result
    print("#{} {}".format(cnt+1, max_cnt))
```
