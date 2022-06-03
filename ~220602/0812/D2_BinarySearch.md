```python
def b_search(left, right, target):
    cnt = 0 # return 값
    while left < right:
        cnt += 1
        mid = (left + right) // 2
        if mid == target :
            return cnt
        if mid < target : # left [left=]mid target right
            left = mid
        elif target < mid: # left  target   [right=]mid   right
            right = mid


case_cnt = int(input())
for cnt in range(case_cnt) :
    P, Pa, Pb = map(int, input().split())
    cnt_a = b_search(1, P, Pa) # left, right, target
    cnt_b = b_search(1, P, Pb)
    if cnt_a < cnt_b :
        print('#{} A'.format(cnt+1))
    elif cnt_b < cnt_a :
        print('#{} B'.format(cnt+1))
    else :
        print('#{} 0'.format(cnt+1))
```
