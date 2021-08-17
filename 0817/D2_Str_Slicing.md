```python
case_cnt = int(input())
for cnt in range(case_cnt):
    str1 = input()
    str2 = input()
    result = 0
    for idx in range(len(str2)):
        if str1 == str2[idx:idx+len(str1)]:
        # slicing으로 str1이 str2와 일치하는 부분이 있는지 확인
            result = 1
            break
    print('#{} {}'.format(cnt+1, result))
```

