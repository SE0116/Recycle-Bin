# Homework

## 2 중앙값

```
det get_middle_char(string):
	#print(string)
	length = 0
	for char in string:
		#print(char)
		length += 1
		
	idx = length // 2
	if length % 2:
		return string[idx]
	else:
		return string[idx-1:idx+1] 	
get_middle_char('mango') 	
get_middle_char('coding')
```



---



# Workshop

## 2 Dictionary

```
def dict_list_sum(dict_list):
	#pirnt(type(dict_list))
	total = 0
	for dictionary in dict_list:
		total += print(dictionary['age]'])
		#print(list(dictionary.values())[1])
	return total	
dict_list_sum([{'name': 'kim', 'age': 12},
                     {'name': 'lee', 'age': 4}]))
```

## 3 

```
def all_list_sum(num_list):
	total = 0
	for numbers in num_list:
		for number in numbers:
			total += number
	return total
	
result = all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
print(result)
```

