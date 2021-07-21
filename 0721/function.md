# Function

- 특정한 기능을 하는 코드의 조각
  - 선언(정의) 부분과 호출 부분으로 나뉨

## 1.1 함수의 구조

- 이름
- 매개변수
- 바디 - `Docstring` 및 코드셋
  - `Docstring`  함수나 클래스에 대한 설명 표시

- 반환값 `return`

## 1.2 함수의 선언

- `def` 키워드 사용
- 들여쓰기에 유의하여 코드 작성
- `return` 을 통해 결과값 전달

## 1.3 함수의 호출

- `함수명()` 으로 호출
  - 매개변수가 있을 경우 괄호 안에 대입

## 1.4 함수의 리턴

- 함수는 항상 반환되는 값을 가짐
  - 명시된 반환값이 없을 경우 `None` 반환
- 오로지 하나의 객체만 반환됨
  - 여러 개의 객체를 `return` 하게 되면 `tuple` 로 묶여 하나의 객체로 반환

## 1.5 함수의 인자

### 1.5.1 위치 인자

- 인자 목록의 처음에 나오거나 `iterable` 앞에 *가 붙은 인자

### 1.5.2 기본 인자값

- 인자에 기본값을 지정하여 함수 호출시 별도로 설정을 하지 않게 하는 값

### 1.5.3 키워드 인자

- 함수 호출 시 식별자가 앞에 붙은 인자

### 1.5.4 가변 인자

- `*args`

- 함수가 복수의 인자로 호출 가능하게 지정
- 인자들은 `tuple` 로 처리

### 1.5.5 가변 키워드 인자

- `**kwargs`
- 가변 인자와 유사
- 인자들은 `dictionary` 로 처리

## 1.6 스코프(scope)

- 지역 스코프 / 전역 스코프
- 지역 변수 / 전역 변수
- built-in scope > global scope > local scope

### 1.6.1 이름 검색 규칙

- `LEGB Rule`
- 함수 -> 상위 함수 -> 함수 밖의 변수 -> 파이썬 내장 함수 순으로 검색
- 함수 내에서는 바깥 스코프의 변수에 접근 가능하나 수정 불가능
- 외부에서 내부로의 변수 접근은 불가능

### 1.6.2 global / nonlocal

```
a = 5						|		a = 5
def func1():				|		def func2():
	global a				|			a = 1
	a = 3					|			def func3():
print(a)					|				nonlocal a
func1()						|				a = 2
print(a)					|			func3()
							|			print(a)
							|		func1()
							|		print(a)
```

## 1.7 재귀함수

- 자기 자신을 호출하는 함수
- 1개 이상의 `base case` 존재
- `Factorial`  `Fibonacci`
- `stack overflow` 방지를 위해 최대 횟수를 1,000번으로 제한



# 2 에러 / 예외 처리

## 2.1 디버깅

- `print`문
- `python tutor`
- 에러 메시지가 발생하는 경우
  - 해당 위치를 찾아 해결
- 로직 에러가 발생하는 경우
  - 정상적으로 돌아가던 코드 이후 작성된 코드 생각
  - 전체 코드 다시 보기
  - 누군가에게 설명해보면서 오류 찾기
  - 내일의 나에게 맡기기

## 2.2 문법 에러(Syntax Error)

- 프로그램 실행 불가
- 파일 이름, 줄번호, `^` 문자를 통해 위치 표시
- `Invalid Syntax`  `assign to literal`  `EOL`  `EOF`

# 2.3 예외(Exception)

- 실행 도중 발견시 프로그램 실행 종료
- `ZeroDivisionError`  `NameError`  `TypeError`  `ValueError`  `IndexError`  `KeyError`, ...

## 2.4 예외 처리

```
try:
	<code block>
except <ErrorName>:
	<code block>
else:
	<code block>
finally:
	<code block>
```



- `try` / `except` 를 이용해 예외 처리 가능
- 예외가 발생하지 않으면 `except` 없이 실행 종료, `else` 가 있다면 실행
- 예외가 발생하면 `except` 이하 구문 실행
- `finally` 가 있다면 예외 발생 여부와 상관없이 실행