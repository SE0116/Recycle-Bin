# Homework

## 2 Magic Method

```python
__init__	# 생성자
__del__		# 소멸자
__str__		# 문자열 print()할 때 보여지는 문자열 반환(외부 노출용)
__repr__	# 문자열 인스턴스의 정보에 대한 값을 반환(for developers)
```



# Workshop

## 2 Basic Usages

```python
from faker import Faker		# 1 패키지 내의 클래스를 불러와 사용준비를 하기 위한 코드
fake = Faker()				# 2 Faker는 class, fake는 instance
fake.name()					# 3 name()은 fake의 (instance) method
```



## 3

```python
class Faker():					# (a) init
    def __(a)__((b), (c)):		# (b) self
        pass					# (C) locale = 'en_US' (기본값 영어로 설정)
```



## 4 Seeding the Generator

```python
fake = Faker('ko_KR')
Faker.seed(4321)
print(fake.name())
fake2 = Faker('ko_KR')
print(fake2.name())
```

- `.seed()` 는 `class method` 로 클래스 변수가 변경되어 모든 인스턴스에 적용

```python
fake = Faerk('ko_KR')
fake.seed_instance(4321)
print(fake.name())
fake2 = Faker('ko_KR')
print(fake2.name())
```

- `.seed_instance()` 는 `instance method` 로 인스턴스 변수가 변경되고 해당 인스턴스에 적용

