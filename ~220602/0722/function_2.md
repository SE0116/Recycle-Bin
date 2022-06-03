# 1 함수(Function)

## 1.1 함수를 쓰는 이유

- 가독성
- 재사용성
- 유지보수

## 1.2 함수의 선언과 호출

- `def` 로 선언
- `들여쓰기(4spaces)` 로 함수의 body 작성
  - Docstring은 선택적 사용 가능
- 동작 후 `return` 을 통해 결과값 전달

- `함수명()` 로 호출

- **Python 함수는 일급 객체
  - 변수에 저장할 수 있음
  - 매개변수에 인자로 전달될 수 있음
  - 리턴으로 전달 가능



# 2 함수의 Output

## 2.1 함수의 `return`

- `return` 값은 오직 한 개의 객체만 반환
- 함수가 return되거나 종료되면, 함수를 호출한 곳으로 되돌아감



# 3 함수의 입력(Input)

## 3.1 매개변수(parameter) & 전달인자(argument)

### 3.1.1 매개변수

```
def func(x):
	return x + 2
```

- `x` 가 매개변수
- 입력을 받아 함수 내부에서 활용할 `변수`
- 함수의 정의 부분에서 볼 수 있음

### 3.1.2  전달인자

```
func(2)
```

- `2` 가 (전달)인자
- 실제로 전달되는 `입력값`
- 함수의 호출 부분에서 볼 수 있음

## 3.2 함수의 인자

- 함수는 `input` 으로 `인자` 를 넘겨줄 수 있음

### 3.2.1 위치 인자(Positional Arguments)

- 인자는 기본적으로 위치에 따라 함수 내에 전달

### 3.2.2 기본 인자 값(Default Argument Values)

```
def func(p1=v1):
	return p1
```

- 함수를 정의할 때, 기본값을 지정하여 정의된 것 보다 적은 수의 인자들로 호출 가능

- 기본 값이 있는 인자 값  뒤에 기본 값이 없는 인자 사용 불가

### 3.2.3 키워드 인자(Keyword Arguments)

```
def greeting(age, name):
	return f'{name}은 {age}살'
	
greeting(age=<25>, name='철수')
```



- 함수를 호출할 때 직접 변수의 이름으로 특정 인자를 전달

- `키워드 인자` 뒤에 `위치 인자` 활용 불가

## 3.3 정해지지 않은 여러 개의 인자 처리

### 3.3.1 가변(임의) 인자 리스트(Arbitrary Argument Lists)

```
def func(a, b, *args)
```

- `*args` 로 개수가 정해지지 않은 임의의 인자를 받음
- `tuple` 로 처리

### 3.3.2 가변 키워드 인자(Arbitrary Keyword Arguments)

- `**kwargs` 로 정해지지 않은 키워드 인자를 받음
- `dict` 형태로 처리
- 식별자는 숫자만으로 이루어질 수 없음
  - 함수 안에서 식별자로 쓰이기 때문



# 4 함수와 스코프(scope)

- 전역 스코프(`global scope`) : 코드 어디에서든 참조할 수 있는 공간

- 지역 스코프(`local scope`) : 함수 내부에서만 참조할 수 있는 공간

  

- 전역 변수(`global variable`) : 전역 스코프에 정의된 변수
- 지역 변수(`local variable`) : 지역 스코프에 정의된 변수

### 4.0.1 변수의 수명 주기(lifecycle)

- `built-in scope `  파이썬이 실행된 이후부터 영원히 유지
- `global scope`  모듈이 호출된 시점 또는 이름이 선언된 이후부터 인터프리터가 끝날 때 까지 유유지
- `local scope `  함수가 호출될 때 생성되고, 함수가 종료될 때 까지 유지

 ## 4.1 이름 검색(resolution) 규칙

- LEGB Rule
- Local -> Enclosed -> Global -> Built-in 순으로 이름 검색

# 5 재귀 함수

## 5.1 반복문과 재귀 함수

- 반복문 코드
  - n이 1보다 큰 경우 반복문을 돌며, n은 1씩 감소
  - 마지막에 n이 1이면 더 이상 반복문을 돌지 않음
- 재귀 함수 코드
  - 재귀 함수를 호출하며, n은 1씩 감소
  - 마지막에 n이 1이면 더 이상 추가 함수를 호출하지 않음
- 재귀 함수를 작성 시에는 반드시 `base case` 가 존재 하여야 함
- 재귀 호출은 `변수 사용` 을 줄여줄 수 있음
- 코드 상황에 맞춰 자연스러운 쪽 사용

## 5.2 최대 재귀 깊이

- 파이썬에서는 최대 재귀 깊이가 1,000으로 정해져 있음

## 5.3 팩토리얼

- `!` 로 표기
- 1부터 주어진 정수까지의 양의 정수를 차례대로 곱한 값 반환

## 5.4 피보나치 수열

- 첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열
- `(0), 1, 1, 2, 3, 5, 8, ...`



# 6 에러 & 예외 처리

## 6.1 에러(Error)

### 6.1.1 문법 에러(Syntax Error)

- `Syntax Error` 문구와 함께 상세내용을 보여줌
- `파일 이름`  `줄 번호`  `^`  문자를 통해 문제가 있는 위치 표시

### 6.1.2 예외(Exception)

- 문법적으로는 옳지만, 실행 시 발생하는 에러

- `Exception` 을 상속받이 이뤄짐

- `ZeroDivisionError`  `NameError`  `TypeError`

  `ValueError`  `IndexError`  `KeyError`  `ModuleNotFoundError``

  ``ImportError`  `KeyBoardInterrupt`

## 6.2 예외 처리(Exception Handling)

### 6.2.1 `try`  &  `except`

```
try:
	<code block>
except:
	<code block>
```

### 6.2.2 복수의 예외 처리

```
try:
	<code block>
except <ErrorName>:
	<code block>
except <ErrorName>:
	<code block>
```

- 괄호가 있는 `tuple` 로 여러 개의 예외를 지정 가능

### 6.2.3 `else`

```
try:
    <code block>
except <ErrorName>:
    <code block>
else:
    <code block>
```

### 6.2.4 `finally`

```
try:
    <code block>
except <ErrorName>:
    <code block>
finally:
    <code block>
```

- 반드시 수행해야 하는 문장이 있을 때 활용
- 예외의 발생 여부와 관계없이 `try` 문을 떠날 때 항상 실행

### 6.2.5 에러 메시지 처리 `as`

```
try:
    <code block>
except <ErrorName> as err:
    <code block>
```

## 6.3 예외 발생 시키기(Exception Raising)

### 6.3.1 `raise`

```
raise <ErrorName>('message')
```

- 예외를 강제로 발생

### 6.3.2 `assert`

```
assert Boolean expression, error message
assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
```

- 상태를 검증할 때 사용
- 무조건 `AsserionError` 발생

