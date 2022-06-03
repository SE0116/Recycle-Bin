Homework

## 2 매개변수와 인자, 그리고 반환

*(4) 가변 인자를 설정할 때는 인자 앞에 *을 붙이고, 이 때는 함수 내에서 tuple로 처리 된다

- 단어 혼용에 유의



# Workshop

## 1 

```python
def get_secret_word(numbers):
	for num in numbers:
		#print(chr(num))
    	result += chr(num)
	return result
res = get_secret_word([65, 2, 3, 4, 5])
print(res)
```



## 2 내 이름은 몇일까?

```python
def get_secret_number(word):
    result = 0
    for char in word:
        #print(char)
        result += ord(char)
    
    return result
res = get_secret_number('tom')
print(res)
```



## 3 강한 이름

```python
def get_strong_word(word1, word2):
    sum1 = get_secret_number(word1)
    sum2 = get_secret_number(word2)
    if sum1 >= sum2:
        return word1
	else:
        return word2
res1 = get_strong_word('z', 'a')
res2 = get_strong_word('tom', 'john')

print(res1, res2)
```

