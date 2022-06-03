# Homework

## 1 Built-in 함수와 메서드

```python
sotred([])	# => 원본 변경 X, 반환 O
[].sort()	# => 원본 변경 O, 반환 X
```



## 2 .extend() 와 .append()

```python
a = []
a.append('abc')	# => ['abc']			리스트 마지막에 인자를 추가
a.extend('abc')	# => ['a', 'b', 'c']	인자로 들어온 값을 요소별로 추가
```



## 3 복사가 잘 된 건가?

```python
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a, b)
```

- a와 b가 같은 주소를 참조하기 때문에 a == b
- 값을 다르게 하고 싶으면
  - `slicing`    `list()`    `copy.copy` 사용



# Workshop

## 1 무엇이 중복일까

```python
def duplicated_letters(word):
    #1 조건문으로 리스트에 중복값이 들어가지 않게 하는 방법
    result = []
    for char in word:
        if word.count(char) >= 1 and char not in result:
            result.append(char)
    
    #2 set으로 리스트의 중복값을 제거하는 방법
    result = []
    for char in word:
        if word.count(char) >= 1:
            result.append(char)
    print(list(set(result)))
        
```



## 2 소대소대

```python
def low_and_up(word):
    length = len(word)
    #1 for문
    result = ''
    for idx in range(length):
        if idx % 2:
            result += word[idx].upper()
        else:
            result += word[idx].lower()
    return result

    #2 List Comprehension + 조건표현식
    result = [char.upper() if idx % 2 else char.lower() for idx, char in enumerate(word)]
    #[char for idx, char in enumerate(word) if idx % 2]
    return ''.join(result)
```



## 3 숫자의 의미 

```python
def lonely(numbers):
    #1
    result = [numbers[0]]
    for num in numbers:
        if result[-1] != num:
            result.append(num)
    return result
	#2
    result = []
    for idx, num in enumerate(numbers):
        if idx == 0:
            result.append(num)
            
        if result[-1] != num:
            result.append(num)
    return result
```