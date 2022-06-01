# 14. Longest Common Prefix

### Problem

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

 

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lower-case English letters.



### Acceptance - 39.6%

### Difficulty - Easy



### My Code

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strMin, strMax = min(strs), max(strs)
        temp = 0
        for idx in range(min(len(strMin), len(strMax))):
            if strMin[idx] == strMax[idx]:
                temp += 1
            else:
                break
        return strMax[:temp]
```



### Result

Runtime : 66ms ( 15.85% )

Memory Usage : 13.8MB ( 88.05% )



### Takeaway

```markdown
배열의 첫번 째 단어와 두 번째 단어를 비교하고 나온 접두사를 기준으로 이후의 단어를 비교하려 했는데 이 경우에 첫 접두사가 더 길면 코드상 오류가 날 수가 있어서 다시 설계를 했다.

배열을 비교할 때 코드와 같이 맨 앞과 맨 뒤의 문자만 비교를 해도 성립이 가능한데 이 부분이 이해가 잘 되질 않아 조금 더 고민을 해봐야 할 것 같다.
```

