# Python_Intro



### 식별자

- 알파벳 대소문자 , 언더스코어, 숫자로 구성
- 첫 글자에 숫자 불가능
- 길이 제한 X, 대소문자 구별
- 내장함수 식별자로 사용 X



### 이스케이프 시퀀스

- `\n`    `\t`    `\r`    `\0`    `\\`    `\'`    `\"`



### String interpolation

- %-formating

  ```python
  print('이름 : %s' % name)
  ```

- str.format()

  ```python
  print('이름 : {}'.format(name))
  ```

- f-strings

  ```python
  print(f'이름 : {name}')
  ```



### 참 / 거짓 타입

- `0`    `0.0`    `()`     `{}`    `[]`    `''`    `None`  모두 `False`



### 형 변환

- `string` -> `integer` : 형식에 맞는 숫자만 가능



### 논리 연산자(단축평가)

- `A and B`    A가 거짓이면 A 리턴, 참이면 B 리턴
- `A or B`     A가 참이면 A 리턴, 거짓이면 B 리턴



### 표현식, 문장

- 표현식 : 하나의 값으로 환원될 수 있는 문장
- 문장 : 파이썬이 실행 가능한 최소한의 코드 단위



# 컨테이너

## 시퀀스형 컨테이너

- 순서 O, 특정 위치의 데이터 지정 가능

- `List`    `Tuple`    `Range`    `String`



### 리스트

```python
[value1, value2, value3, ...]
```



### 튜플

```python
(value1, value2)
```

- 수정 불가능, 읽기만 가능



## 비 시퀀스형 컨테이너

### Set

```python
{value1, value2, value3, ...}
```

- `set()`
- 순서, 중복값 X
- 집합과 처리 동일



### Dictionary

```python
{key1: value1, key2: value2, key3: value3, ...}
```

- `{}`    `dict()`



### 데이터의 분류

- `mutable`
  - `list`    `set`    `dictionary`
- `immutable`
  - `literal`    `range()`    `tuple()`



# 제어문

- 들여쓰기 유의

### 조건 표현식

```python
true_value if <expression> else false_value
```



### enumerate()

- 해당 값과 그에 맞는 인덱스를 튜플 형태로 반환



# 함수

- 특정한 기능을 하는 코드의 묶음
- `가독성`    `재사용성`    `유지보수`



### 함수의 return

- 함수는 반환되는 값이 있으며 어떤 종류라도 상관없지만, `단 하나` 의 객체만 반환



### 매개변수

```python
def func(x):			# x : 매개변수
	<code block>


func(num)				# num : 인자
```



### 함수의 인자

- 위치 인자
- 기본 인자 값
- 키워드 인자
- 가변 인자
- 가변 키워드 인자



### 이름 검색 규칙

- `Local`    `Enclosed`    `Global`    `Built-in`



### 예외 처리

```python
try:
	<code block>
except <ErrorName>:
	<code block>
else:
    <code block>
finally:
    <code block>
```



# 데이터 구조

## 문자열

### 조회 / 탐색

- `.find(x)`    `.index(x)`
- `.replace(old, new[, count])`    `.strip([chars])`    `.split([chars])`    `<separator>.join(iterable)`



## 리스트

- `.append(x)`    `.extend(iterable)`    `.insert(i, x)`    `.remove(x)`    `.pop(i)`    `.clear()`
- `.index(x)`    `.count(x)`    `.sort()`    `.reverse()`



### 리스트 복사 방법

- `slice` 연산자 사용
- `list()` 사용



### List comprehension

```python
[<expression> for var in iterable if <condition>]
```



### 데이터 구조에 적용 가능한 Built-in Function

- `map()`    `filter()`    `zip()`



## 세트(set)

- `.add(element)`    `.update(*others)`    `.remove(elem)`    `.discard(elem)`    `.pop()`



## 딕셔너리(Dictionary)

- `.get(key[, default])`    `.pop(key[, default])`    `.update()`



### Dictionary comprehension

```python
{key: value for var in iterable}

dict({key: value for var in iterable})
```

