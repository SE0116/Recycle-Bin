# Practice 1

## 1.3 any() 구현하기

```python
(1)	for i in [1]:
		print(i)
	
(2)	for i in []:
		print(i)
```

- (1) 번의 경우 반복문이 1번 돌아감
- (2) 번의 경우 반복문이 0번 돌아감
- 빈 리스트로 반복문을 돌릴 경우 반복문 자체가 성립이 되질 않아 True값이 반환됨



# Practice 2

## 2.1 불쌍한 달팽이

```python
def snail(height, day, night):
	days = 0
    while True:
        days += 1
        height -= day
        if height <= 0:
            return days
        height += night
        
print(snail(100, 5, 2))
```

- 낮에 올라간 거리와 밤에 내려가는 거리를 한번에 계산하지 않기(일 수가 달라짐)

## 2.2 자릿수 더하기

```
def sum_of_digit(number):
    total = 0
    while number:
        remain = number % 10
        number = number // 10
        total += remain
        
    return total
```

