```python
for cnt in range(10):
    case_cnt = int(input())
    word = input()
    long = input()
    pattern_cnt = 0

    for idx in range(len(long)-len(word)+1):
        if long[idx:idx+len(word)] == word:
            pattern_cnt += 1

    print('#{} {}'.format(cnt+1, pattern_cnt))
```