```python
moum = [ 'a','e','i','o','u']
case_cnt = int(input())
for cnt in range(case_cnt):
    is_moum = [0 for _ in range(201)] # 0 ~ 200
    for i in range(5):
        val = ord(moum[i]) # 97 101 105 111 117
        is_moum[val] = 1
    s = input()
    print('#{}'.format(cnt+1), end=' ')
    for i in range(len(s)):
        val = ord(s[i]) # ord('a')
        if is_moum[val] == 0:
            print(chr(val), end ='')
    print()
```

