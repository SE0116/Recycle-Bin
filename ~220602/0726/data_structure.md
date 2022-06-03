# 데이터 구조

## 1 문자열

### 1.1 특징

- `Immutable`    `ordered`    `iterable`

### 1.2 메소드

- `slicing`

```python
s[<start>:<stop>:<step>]

| a | b | c | d | e | f | g | h | i	""
0	1	2	3	4	5	6	7	8	index
-9	-8	-7	-6	-5	-4	-3	-2	-1	slicing
```

- `.find(x)`
  - x의 첫 번째 위치를 반환하고, 없으면 `-1을 반환`
- `.index(x)`
  - x의 첫 번째 위치를 반환하고, 없으면 `오류 발생`
- `.replace(<old>, <new[,count]>)`
  - old를 new로 반환하고, count를 지정하면 해당 개수만큼만 시행
- `.strip([chars])`
  - 특정 문자 지정시 호출명에 따라 제거
  - 양쪽 `strip`    왼쪽 `lstrip`    오른쪽 `rstrip`
  - 문자열을 지정하지 않으면 공백 제거
- `.split([chars])`
  - 문자열을 특정한 단위로 나눠 리스트로 반환
- `<seperator>.join([iterable])`
  - iterable 요소들을 seperator로 합쳐 문자열 반환
- `.capitalize()`    `.title()`    `.upper()`    `.lower()`    `.swapcase()`
  - 대소문자 관련 메소드
-  `.isalpha()`    `.isupper()`    `.islower()`    `.istitle()`
  - 문자열 관련 검증 메소드



## 2 리스트

## 2.1 특징

- 순서가 있는 시퀀스, `index` 로 접근
- `mutable`    `ordered`    `iterable`

### 2.2 메소드

- `.append(x)`
  - 리스트에 값 추가
- `.extend(iterable)`
  - 리스트에 iterable 항목 추가
- `.insert(i, x)`
  - i 위치에 x값 추가
- `.remove(x)`
  - 리스트에서 값이 x인 것 삭제
- `.pop(i)`
  - 위치 i에 있는 값을 삭제하고 그 값을 반환하고, i가 없으면 마지막 항목 삭제 후 반환
- `.clear()`
  - 모든 항목 삭제
- `.index(x)`
  - x가 있는 index값 반환
- `.count(x)`
  - x값의 개수 반환
- `sort()`
  - 원본 리스트를 정렬하고 `None` 반환
  - `sorted(x)` 함수와 차이가 있음

``` python
numbers = [3, 2, 5, 1]
result = numbers.sort()
print(numbers, result)	# => [1, 2, 3, 5] None

numbers = [3, 2, 5, 1]
result = sorted(numbers)
print(numbers, result)	# => [3, 2, 5, 1] [1, 2, 3, 5]
```

- `.reserse()`
  - 순서를 반대로 변경(정렬 X)

### 2.3 리스트 복사

- 얕은 복사(shallow copy)
- 깊은 복사(deep copy)

### 2.4 List comprehension

```python
[<expression> for <variable> in <iterable>]
[<expression> for <variable> in <iterable> if <condition>]
```

### 2.5 Built-in Function

- `map(function, iterable)`
  - iterable의 모든 요소에 function을 적용하고 결과를 map object로 반환
- `filter(function, iterable)`
  - map과 유사하지만 결과가 True인 것만을 filter object로 반환
- `zip(*iterables)`
  - 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

## 3 세트

### 3. 1 특징

- 중복 없이 순서가 없음

- `mutable`    `unordered`    `iterable`

### 3.2 메소드

- `.add(element)`
  -  세트에 값을 추가
- `.update(*others)`
  - 여러 값을 추가
- `.remove(element)`
  - 세트에서 삭제하고, 없으면 KeyError
- `.discard(element)`
  - 세트에서 삭제하고 없어도 에러가 발생하지 않음
- `.pop()`
  - 임의의 원소를 제거하고 반환

## 4 딕셔너리

### 4.1 특징

- `key` 와 `value` 로 구성
- `mutable`    `unordered`    `iterable`

### 4.2 메소드

- `.get(key[, default])
  - key를 통해 values를 가져옴
  - KeyError가 발생하지 않으며 default값 설정 가능(기본값 None)
- `.pop(key[,default])`
  - key가 딕셔너리에 있으면 제거하고 해당 값을 반환하고 아니면 default를 반환
  - default값이 존재하지 않을 시 KeyError
- `.update()`
  - 값을 제공하는 key, value로 덮어씀
- `keys()`    `values()`    `items()`

### 4.3 Dictionary Comprehension

```python
{key: value for <variable> in <iterable>}
{key: value for <variable> in <iterable> if <condition>}
```

