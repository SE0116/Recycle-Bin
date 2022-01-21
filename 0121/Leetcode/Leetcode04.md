# 4. Median of Two Sorted Arrays

- Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

  The overall run time complexity should be `O(log (m+n))`.

   

  **Example 1:**

  ```
  Input: nums1 = [1,3], nums2 = [2]
  Output: 2.00000
  Explanation: merged array = [1,2,3] and median is 2.
  ```

  **Example 2:**

  ```
  Input: nums1 = [1,2], nums2 = [3,4]
  Output: 2.50000
  Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
  ```

   

  **Constraints:**

  - `nums1.length == m`
  - `nums2.length == n`
  - `0 <= m <= 1000`
  - `0 <= n <= 1000`
  - `1 <= m + n <= 2000`
  - `-106 <= nums1[i], nums2[i] <= 106`



### Acceptance - 33.5%

### Difficulty - Hard



### My Code

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
                
        len_1 = len(nums1)
        len_2 = len(nums2)
        max_len = len_1 + len_2
        start, end = 0, len_1
        
        if not nums2:
            if len_1 % 2:
                return (nums1[(len_1-1)//2])
            else:
                return (nums1[(len_1//2)-1] + nums1[len_1//2]) / 2
        while start <= end:
            pivot1 = (start + end) // 2
            pivot2 = (max_len + 1) // 2 - pivot1
            
            print(start, end)
            print(pivot1, pivot2)
            
            max_num1 = nums1[pivot1-1] if pivot1 != 0 else float('-inf')
            min_num1 = nums1[pivot1] if pivot1 != len_1  else float('inf')
            
            max_num2 = nums2[pivot2-1] if pivot2 != 0 else float('-inf')
            min_num2 = nums2[pivot2] if pivot2 != len_2 else float('inf')
            
            
            if max_num1 <= min_num2 and max_num2 <= min_num1:
                if max_len % 2 == 0:
                    return (max(max_num1, max_num2) + min(min_num1, min_num2)) / 2
                else:
                    return max(max_num1, max_num2)
            elif max_num1 > min_num2:
                end = pivot1 - 1
            else:
                start = pivot1 + 1
```



### Result

Runtime : 86ms ( 89.70% )

Memory Usage : 14.7MB ( 6.09% )
