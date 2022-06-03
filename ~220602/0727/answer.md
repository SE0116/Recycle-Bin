# Homework

## 1 모음은 몇 개나 있을까?

```python
def count_vowes(word):
    vowels = 'aeiou'
    total = 0
    for vowel in vowels:
        total += word.count(vowel)
    return total
```



## 2 문자열 조작

- `.strip([chars])` 은 특정 문자를 지정하지 않으면 공백을 제거한다.



## 3 정사각형만 만들기

```python
def only_square_area(value1, value2):
    #1 이중 for문
    area_list = []
	for v1 in value1:
		for v2 in value2:
			if v1 == v2:
            	area_list.append(v1**2)
	#2 list comprehension
    area_list = [v1**2 for v1 in value for v2 in value2 if v1 == v2]
return area_list
```



# Workshop

## 1 평균 점수 구하기

```python
def get_dict_avg(score_dict):
    #1 for문
    total = 0
    length = 0
    for score in score_dict.values():
        total += score
        length += 1
    return total / length
	#2 Built-in Function
	return sum(score_dict.values()) / len(score_dict)
```



## 2 혈액형 분류하기

```python
def count_blood(blood_list):
    #1
    blood_dict = {}
    for blood in blood_list:
        if blood_dict.get(blood):
            blood_dict[blood] += 1
        else:
            blood_dict[blood] = 1
    #2
    blood_dict = {}
	for blood in blood_list:
        blood_dict[blood] = blood_dict.get(blood, 0) + 1
    return blood_dict
```

