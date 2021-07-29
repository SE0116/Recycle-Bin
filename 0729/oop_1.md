## 폴더 내 `__init__.py` 생성

- `__init__.py` 를 생성하면 해당 폴더가 패키지라는 것을 알려줌



# OOP

## 1 객체

### 1.1 타입(Type)과 인스턴스(Instance)

- `Type`    공통된 `attribute` 와 `method` 를 가진 객체들의 분류
- `instance`    특정 타이의 실제 데이터 예시
  - 파이썬에서의 모든 것은 객체이고, 모든 객체는 특정 타입의 인스턴스

### 1.2 속성(Attribute)과 메서드(Method)

- `attribute`    객체의 상태/데이터

```python
<object>.<attribute>
```

- `method`    특정 객체에 적용할 수 있는 행위

```python
<object>.<method>()
```



## 2 객체 지향 프로그래밍(OOP)

- OOP란?
  - 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것
- 객체 중심의 장단점
  - 코드의 `직관성`    활용의 `용이성`    변경의 `유연성`
  - 실행 속도 下, 코딩 난이도 上



## 3 클래스(Class)와 인스턴스(Instance)

### 3.1 클래스 생성

```python
class <ClassName>:
	<statement>
```

- `class` 키워드와 정의하고자 하는 `<클래스명>`(PascalCase) 으로 가능
- 클래스 내부에 데이터 및 함수 정의 가능, 데이터는 `attribute`    함수는 `method` 로 부름

### 3.2 인스턴스 생성

```python
<instance> = <Class>()
```

### 3.3 메서드 정의

```python
class <ClassName>:
    def <function>(self):
        <code block>
```

### 3.4 `self`

- Python 내 인스턴스 메서드는 호출 시 첫 번째 인자로 인스턴스 자신이 전달되게 설계
- 보통 `self` 를 첫 번째 인자로 정의

#### 3.4.1 생성자 매서드

```python
class <ClassName>:
    def __init__(self):
        <code block>
```

- 인스턴스가 생성될 때 인스턴스의 속성 정의 가능

#### 3.4.2 소멸자 메서드

```python
def __del__(self):
    <code block>
```

### 3.5 속성 정의

```python
class <ClassName>:
    def __init__(self, <variable_value>):
        self.<variable> = <value>
        
    def <method>(self):
        <code block>
```

### 3.6 매직 메서드

#### 3.6.1 `__str__(self)`

```python
class <ClassName>:
    def __str__(self):
        return <string>
```



## 4 인스턴스 & 클래스 변수

### 4.1 인스턴스 변수

```python
class <ClassName>:
    def __init__(self, <variable>):
        self.<variable> = <value>
```

- 인트선스의 속성
- 각 인스턴스들의 고유한 변수

### 4.2 클래스 변수

```python
class <ClassName>:
    <variable> = <value>
```

- 클래스의 속성
- 모든 인스턴스가 공유



## 5 인스턴스 & 클래스간의 이름공간

- `class` 와 `instance` 는 서로 다른 `namespace` 를 가지고 있음

- 인스턴스에서 특정한 attribute에 접근하게 되면 `인스턴스 -> 클래스` 순으로 탐색



## 6 메서드의 종류

### 6.1 인스턴스 메서드

```python
class <ClassName>:
    def instance_method(self, arg1, arg2, ...):
        ...
        
<sample_class> = <ClassName>
<sample_class>.instance_method(.., ..)
```

- 인스턴스가 사용할 메서드
- 클래스 내부에서 정의되는 메서드의 기본값은 인스턴스 메서드

### 6.2 클래스 메서드

```python
class <ClassName>:
    @classmethod
    def class_method(cls, arg1, arg2, ...):
        ...

<ClassName>.class_method(.., ..)
```

- 클래스가 사용할 메서드
- 호출 시 첫 번째 인자로 클래스 `cls` 가 전달

### 6.3 스태틱 메서드

```python
class <ClassName>:
    @staticmethod
    def static_method(arg1, arg2, ...):
        ...
        
<ClassName>.static_method(.., ..)
```

- 클래스가 사용할 메서드

- 호출 시 어떤 인자도 전달되지 않음

### 6.4 비교 정리

#### 3.4.1 인스턴스와 메서드

- 인스턴스는 3가지 메서드 모두 접근 가능
- 인스턴스가 할 행동은 인스턴스 메서드로 한정 지어서 설계 필요
- 인스턴스에서 클래스&스태틱 메서드는 되도록 호출하지 않도록 요구

#### 3.4.2 클래스와 메서드

- 클래스 자체 `cls` 와 그 속성에 접근할 필요가 있다면 `클래스 메서드` 로 정의
- 없다면 `정적 메서드` 로 정의
  - 정적 메서드는 `cls`  `self` 와 같이 묵시적인 첫 번째 인자를 받지 않음



## 7 상속

### 7.1 상속이란?

```python
class <ChildClass>(<ParentClass>):
    <code block>
```

- 클래스에서 가장 큰 특징으로, 부모 클래스의 모든속성을 자식 클래스가 이어 받아 사용 가능
- 상속으로 인해 코드 재사용성 上

### 7.2 `issubclass(class, classinfo)`

- class가 classinfo의 subclass면 True

### 7.3 `isinstance(object, classinfo)`

- object가 classinfo의 인스턴스거나 subclass인 경우 True

### 7.4 `super()`

```python
class <ChildClass>(<ParentClass>):
    def method(self, arg):
        super().method(arg)
```

- 자식 클래스에 메서드를 추가로 구현
- 부모 클래스의 내용을 사용하고자 할 때, 사용 가능



## 8 메서드 오버라이팅

- 상속 받은 메서드를 재정의
- 상속 받은 클래스에서 같은 이름의 메서드로 덮어씀

### 8.1 상속관계에서의 이름공간

- 인스턴스 -> 자식 클래스 -> 부모 클래스(기존 이름공간순에서 부모클래스만 추가)

## 9 다중 상속

- 두 개 이상의 클래스를 상속받는 경우 다중 상속으로 취급
- 상속 받은 모든 클래스의 요소를 활용 가능
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정

