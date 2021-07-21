# Homework

## 1 Mutable & Immutable

- Mutable : `list`    `set`    `dictionary`
- Immutable : `String`    `Tuple`    `Range`



## 2 홀수만 담기

```
numbers = list(range(1, 51))
odd = numbers[::2]
# slicing에서 앞의 두 칸을 비우면 처음부터 끝까지 진행
print(odd)
```



# Workship

## 1 약수

```
user_input = int(input())
for i in range(1, user_input+1):
	if user_input % i == 0:
		print(i)
```



## 2 중간값(sorted)

```
numbers = [...]
sort_list = sorted(numbers)
length = 0
for num in numbers:
	length += 1
center = length // 2
print(sort_list[center])
```



## 3 계단

```
user_input = int(input())
for i in range(user_input):
	for j in range(1, i+2):
		print(f'{j}', end = '')
	print('')
```

