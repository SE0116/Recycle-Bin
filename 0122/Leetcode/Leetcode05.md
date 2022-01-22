# 5. Longest Palindromic Substring

- Given a string `s`, return *the longest palindromic substring* in `s`.

   

  **Example 1:**

  ```
  Input: s = "babad"
  Output: "bab"
  Explanation: "aba" is also a valid answer.
  ```

  **Example 2:**

  ```
  Input: s = "cbbd"
  Output: "bb"
  ```

   

  **Constraints:**

  - `1 <= s.length <= 1000`
  - `s` consist of only digits and English letters.



### Acceptance - 31.6%

### Difficulty - Medium



### My Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        result = ''
        
        for idx in range(len(s)):
            for idx2 in range(idx+1, len(s)+1, 1):
                if s[idx:idx2] == s[idx:idx2][::-1]:
                    if len(s[idx:idx2]) >= len(result):
                        result = s[idx:idx2]
        return result
```



### Result

##### Time Limit Exceeded

Runtime : ??ms ( ??% )

Memory Usage : ??MB ( ??% )
