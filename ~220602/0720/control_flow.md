# 1 조건문

## 1.1 `if` 조건문

```
if <expression>:
	<code block>
elif <expression>:
	<code block>
else:
	<code block>
```

- 조건이 `참` 인 경우 `if` 문 이하의 문장 수행
- 조건이 `거짓` 인 경우 `else` 문 이하의 문장 수행
- `elif` 는 여러 개 사용 가능, `else` 는 선택적 사용 가능
- 사용 시 `들여쓰기` 주의 ( PEP8에서 권장하는 4spaces 사용 권장)

## 1.2 중첩 조건문

```
if <expression>:
	if <expression>:
			...
		<code block>
	<code block>
else:
	<code block>
```

- 조건문 도중 다른 조건문을 추가로 써야 할 때 중첩 사용 가능

## 1.3 조건 표현식

```
true_value if <expression> else false_value
```

- 일반적으로 조건에 따라 값을 정할 때 사용

- `삼항 연산자` 라고도 표현

- 중앙 조건문이 참일 경우 `왼쪽` ,  거짓일 경우 `오른쪽`  값 반환

- 참 / 거짓 결과가 값 대입일 경우, 변수는 참일 경우 한 번만 써준다.

  - ```
    ex)num = '홀수' if num % 2 else '짝수'
    ```

---



# 2 반복문

## 2.1 `while` 반복문

### 2.1.1 활용법

```
while <expression>:
	<code block>
```

### 2.1.2 주의사항

- 콜론(`:`) 반드시 필요, 이후 4spaces
- 반드시 종료조건 설정

## 2.2 `for` 반복문

### 2.2.1 활용법

```
for <temporary variable> in <iterable data>:
	<code block>
```

- `for` 문 내부에서 임시 변수에 다른 값을 할당해도 반복구문에 영향 X

### 2.2.4 리스트 순회에서 index 활용

```
for <temporary variable> in range(len(list)):
	<code block>
```

#### 2.2.4.2 enumerate()

```
for <index>, <value> in enumerate(list):
	<code block>
```

- index와 value 함께 사용 가능

## 2.3 반복 제어

### 2.3.1 `break`

- 이후 과정을 무시하고 반복문 종료

### 2.3.2 `continue`

- continue 이하의 과정을 무시하고 다음 반복과정 진행

### 2.3.3 `for-else`

```
for <temporary variable> in <iterable data>:
	<code block>
	break
else:
	<code block>
```

- 반복문에서 최종과정까지 끝났을 때 실행
- 중간 `break` 로 인해 강제 종료됐을 때는 실행 X

### 2.3.4 pass

- 문법적으로 무언갈 넣어야 되지만 딱히 필요한 과정이 없을 때 자리 채우는 용도로 사용
  - 작업 중 다음 과정을 먼저 쓰고 싶을 때 `pass` 해놓고 추후 수정 가능
- `continue` 는 이하 과정을 생략하고 다음 반복을 시행하지만 `pass` 는 이하 과정도 그대로 진행