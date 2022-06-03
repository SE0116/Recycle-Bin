# 7. Reverse Integer

- Given a signed 32-bit integer `x`, return `x` *with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

  **Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

   

  **Example 1:**

  ```
  Input: x = 123
  Output: 321
  ```

  **Example 2:**

  ```
  Input: x = -123
  Output: -321
  ```

  **Example 3:**

  ```
  Input: x = 120
  Output: 21
  ```

   

  **Constraints:**

  - `-231 <= x <= 231 - 1`



### Acceptance - 26.4%

### Difficulty - Medium



### My Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < -2**31 or x > 2**31 - 1:
            return 0
        reverse_x = ''
        minus = 0
        if x < 0:
            minus = 1
        
        x = abs(x)
        
        while x != 0:
            if x % 10 == 0:
                if reverse_x == 0:
                    x //= 10
            reverse_x += str(x % 10)
            x //= 10
        
        reverse_x = int(reverse_x)
        
        if minus == 1:
            reverse_x *= -1
        
        if reverse_x < -2**31 or reverse_x > 2**31 - 1:
            return 0
        return reverse_x
```



### Result

Runtime : 52ms ( 22.72% )

Memory Usage : 14MB ( 98.42% )
