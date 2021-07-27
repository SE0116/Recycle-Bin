# Data Structure

## 1 문자열

### 1.1 조회 / 탐색

- `method` 와 `function` 을 구분하는 방법 => 구문 앞의 `.` 을 확인



## 2 리스트와 람다식

### 2.1 람다식

```python
(lambda <variable>: <code block>)(<factor>)
```

### 2.2 `map()` , `filter()` 와 람다식

````python
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
map_list = list(map(lambda x: x**2, num_list))
filter_list = list(filter(lambda x: not x % 2, num_list))
````

- `num_list` 의 모든 값에 대한 제곱수를 `map_list` 에 추가
- `num_list` 에서 짝수를 찾아내는 조건에 참인 숫자들만 뽑아내 `filter_list` 에 추가하는 식
