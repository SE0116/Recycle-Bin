# Homework

## 3 오류의 종류

- `ImportError`  패키지/모듈은 있는데 가져오려는 변수/함수/클래스 등이 없을 때
- `ModuleNotFoundError`  패키지/모듈을 찾을 수 없을 때(오타 or 설치X)



# Workshop

```python
class Point:
    def __init__(self, x: int, y: int) -> bool:
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
        
    def get_wid_leng(self):
        self.width = abs(self.p1.x - self.p2.x)
        self.length = abs(self.p1.y - self.p2.y)
        
    def get_area(self) -> int:
        return self.width * self.length
    
    def get_perimeter(self) -> int:
        return (self.width + self.length) * 2
    
    def is_square(self) -> bool:
        return self.width == self.length
```

