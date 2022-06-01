# 1480. Running Sum of 1d Array

### Problem

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

 

**Constraints:**

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`



### Acceptance - 89.9%

### Difficulty - Easy



### My Code

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        resultSum = []
        tempSum = 0
        for n in nums:
            tempSum += n
            resultSum += [tempSum]

        return resultSum
```



### Result

Runtime : 56ms ( 52.35% )

Memory Usage : 14.2MB ( 27.03% )



### Takeaway

```markdown
부끄럽지만 시작할 때 for문 사용법이 헷갈렸다.. 정신을 차려야 할 것 같다.

문제만 봤을 때는 이중 for문으로 풀어야 하나 싶었지만 다시 생각해보니 굳이 그럴 필요가 없는 것 같아 for문을 한 번만 쓰고 그 안에서 배열에 값을 넣어주는 식으로 코드를 작성했다.
```

