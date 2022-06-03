# 1480. Running Sum of 1d Array

### Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

 

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.



### Acceptance - 40.9%

### Difficulty - Easy



### My Code

```python
class Solution(object):
    def isValid(self, s):
        paren = {'(': ')',
                 '{': '}',
                 '[': ']',}
        stack = []
        for letter in s:
            print(paren)
            if letter in paren:
                stack.append(letter)
            elif len(stack) == 0 or paren[stack.pop()] != letter:
                return False
        return len(stack) == 0
```



### Result

Runtime : 56ms ( 52.35% )

Memory Usage : 14.2MB ( 27.03% )



### Takeaway

```markdown
오랜만에 스택을 활용해 보려 했는데 생각보다 시간이 오래 걸렸다.
너무 오래 손을 놨나보다...
트리 / 스택 / 큐 부분을 더 공부할 필요성을 느꼈다.

그리고 딕셔너리에서 스택값을 비교할 때 언제 키를 쓰고 언제 밸류를 쓰는 지 확실히 알아가야 나중에 혼동없이 잘 쓸 수 있을 것 같다.
```

