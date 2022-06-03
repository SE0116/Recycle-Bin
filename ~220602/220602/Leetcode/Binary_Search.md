# 14. Longest Common Prefix

### Problem

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

 

**Constraints:**

- `1 <= nums.length <= 104`
- `-104 < nums[i], target < 104`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.



### Acceptance - 55.2%

### Difficulty - Easy



### My Code

```python
class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target: return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
```



### Result

Runtime : 440ms ( 12.64% )

Memory Usage : 15.5MB ( 22.24% )



### Takeaway

```markdown
이 문제를 풀고 다른 사람들의 코드를 찾아봤는데, 바다코끼리 연산자(:=)를 알게 되었다.
알아두면 코드도 더 간결하게 쓸 수 있을 것 같고 여러모로 요긴하게 쓰일 것 같다.
```

