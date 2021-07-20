# 1 시퀀스형 컨테이너

## 1.1 특징

- 순서를 가짐
- 특정 위치의 데이터를 가리킴

## 1.2 종류

- `list`    `tuple`    `range`    `string`    `binary`

## 1.3 리스트

- `[]`  또는 `list()`  사용
- 값에 대한 접근은 `list[i]`

## 1.4 튜플(tuple)

- 리스트와 유사
- `()` 로 표현
- 수정 불가능(immutable), read only
- Python 내부에서 주로 활용

## 1.5 레인지

- 숫자의 시퀀스를 표현
- `range(n)`  0부터 `n-1` 까지
- `range(n, m)` n부터 `m-1` 까지
- `range(n, m, s)` n부터 m-1까지 `+s` 만큼 증가
- lazy evaluation

## 1.6 활용 가능한 연산자

- `in`    `+`    `*`
- `s[i]`  indexing    `s[i:j]`  slicing    `s[i:j:k]`  k간격으로 slicing
- `len(s)`    `min(s)`    `max(s)`
- `s.count(x)`  x의 개수

---



# 2 비 시퀀스형 컨테이너

## 2.1 set

- 순서와 중복된 값이 없음
- 수학에서의 집합과 동일처리
- `{}` 사용, 빈  set를 만드려면 `set()` 사용
- 연산자 `-`  `|`  `&`  사용 가능

## 2.2 dictionary

- `key` 와 `value` 의 쌍으로 이루어짐
- `{}`  또는  `dict()` 사용
- `key` 는 `변경 불가능` 한 데이터만 가능, `value` 는 `list` ,  `dictionary` 를 포함한 모든 것이 가능
- `.keys()`    `.values()`    `.items()` 로 각각의 목록 확인

## 2.3 컨테이너형 형변환

![typecasting](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)

## 2.4 데이터의 분류

### 2.4.1 변경 불가능한 데이터

- `literal`
  - ``number`  `string`  `bool`
- `range()`
- `tuple()`
- `frozenset()`

### 2.4.1 변경 가능한 데이터

- `list`    `dict`    `set`

---



# 3 정리

![container](https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png)

