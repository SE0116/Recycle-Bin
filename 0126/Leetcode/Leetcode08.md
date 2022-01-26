# 8. String to Integer ( atoi )

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. `"123" -> 123`, `"0032" -> 32`). If no digits were read, then the integer is `0`. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range `[-231, 231 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `-231` should be clamped to `-231`, and integers greater than `231 - 1` should be clamped to `231 - 1`.
6. Return the integer as the final result.

**Note:**

- Only the space character `' '` is considered a whitespace character.
- **Do not ignore** any characters other than the leading whitespace or the rest of the string after the digits.

 

**Example 1:**

```
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
```

**Example 2:**

```
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
```

**Example 3:**

```
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
```

 

**Constraints:**

- `0 <= s.length <= 200`
- `s` consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.



### Acceptance - 16.4%

### Difficulty - Medium



### My Code

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        # 입력받은 문자열에서 공백 제거
        s = s.strip()
        result, plus, minus = '', 0, 0
    
        for char in s:
            # 시작 따옴표와 +부호가 나올 때는 다음 문자열로 넘어가기
            # -부호로 시작할 때는 임의의 값으로 저장 후 다음 문자열 확인
            # 정수로 치환 가능한 경우만 result에 저장하고 불가능하다면 탐색 종료
            if char == '"':
                continue
            elif char == '+' or char == '-':
                if result != '':
                    result = ''
                    return result
                elif char == '+':
                    if minus == 1:
                        result = ''
                        return result
                    plus = 1
                elif char == '-':
                    if plus == 1:
                        result = ''
                        return result
                    minus = 1
            elif char.isdigit():
                result += char
            else:
                break
        # 시작점이 정수로 변환이 되지 않아 break가 됐다면 기본값을 0으로 변환
        if result == '':
            result = 0
        else:
            result = int(result)
        
        # 음수 계산
        if minus == 1:
            result *= -1
        
        # 문제에서 제시한 수치를 넘어갔을 경우 해당 값에 맞게 조정
        if result > 2**31-1:
            result = 2**31-1
        elif result < (-2)**31:
            result = (-2)**31
        return result
```



### Result

##### Wrong Answer + Runtime Error

Runtime : ??ms ( ??% )

Memory Usage : ??MB ( ??% )
